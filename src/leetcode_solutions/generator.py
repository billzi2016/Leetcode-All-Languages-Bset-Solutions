"""串联数据、prompt、模型、断点续跑、日志和 Markdown 写入。

`SolutionGenerator` 是生成流程的编排层。它不直接关心 dataset 如何读取、
prompt 如何拼接、Markdown 如何解析、Ollama 如何调用；这些细节都在小模块中。
它只负责把这些能力按正确顺序组合起来：

1. 根据题目计算目标 Markdown 路径；
2. 读取已有代码，判断缺失语言；
3. 完整文件只检查语言顺序，必要时无模型调用重写；
4. 不完整文件只补缺失语言；
5. Hard 题每生成一种语言就落盘，降低长任务中断损失；
6. Easy/Medium 题等单题所有语言完成后一次性写入；
7. 模型失败不阻塞整个批次，而是记录 failures.jsonl 供后续补跑。
"""

from __future__ import annotations

from collections import OrderedDict
from pathlib import Path

from tqdm import tqdm

from .config import RETRY_LIMIT
from .dataset_loader import Problem
from .markdown_writer import (
    order_solutions,
    problem_output_path,
    read_existing_language_order,
    read_existing_solutions,
    write_problem,
)
from .prompt_builder import SYSTEM_PROMPT, build_language_prompt, build_problem_prompt
from .resume import missing_languages


class SolutionGenerator:
    """针对选定题目执行题解生成。

    参数：
        model_client: 实现 `generate(...)` 方法的模型客户端。生产环境使用
            `OllamaClient`，测试中注入 fake client。
        logger: 运行日志器，负责 info/warn/error 和结构化失败记录。
        output_root: 题解 Markdown 输出根目录。
        retry_limit: 单个语言最多尝试次数，默认来自全局配置。
    """

    def __init__(self, model_client, logger, output_root: Path, retry_limit: int = RETRY_LIMIT) -> None:
        """保存生成器依赖和重试策略。"""

        self.model_client = model_client
        self.logger = logger
        self.output_root = output_root
        self.retry_limit = retry_limit

    def generate_problem(self, problem: Problem) -> Path:
        """生成单题所有缺失语言，并返回目标 Markdown 路径。

        参数：
            problem: dataset 中的一道题，必须包含 `frontend_id`、`difficulty`、
                `problem_slug` 和 `code_snippets`。

        返回：
            Path: 该题对应的 Markdown 目标路径。即使所有语言都失败，也返回
            这个路径，便于调用方定位问题。

        关键行为：
            - 已完整的文件不会重复调用模型；
            - 已完整但语言顺序不标准的文件，会直接重写修复；
            - 部分完成的文件只生成缺失语言；
            - Hard 题边生成边写，Easy/Medium 题在单题末尾统一写。
        """

        output_path = problem_output_path(problem, self.output_root)
        snippets = problem.get("code_snippets") or {}
        languages = list(snippets.keys())
        existing_solutions: OrderedDict[str, str] = OrderedDict()
        if output_path.exists():
            existing_solutions = read_existing_solutions(output_path, languages)

        todo = missing_languages(output_path, languages)
        if not todo:
            if self._repair_language_order(output_path, problem, languages, existing_solutions):
                self.logger.warn(f"Repaired language order for {output_path}")
            self.logger.info(f"Skipping complete problem {problem.get('frontend_id')} {problem.get('problem_slug')}")
            return output_path

        if output_path.exists():
            self.logger.warn(f"Regenerating missing languages for {output_path}")

        problem_prompt = build_problem_prompt(problem)
        difficulty = str(problem.get("difficulty"))
        write_per_language = difficulty == "Hard"

        for language in tqdm(todo, desc=str(problem.get("problem_slug")), leave=False):
            code = self._generate_language(problem, language, snippets[language], problem_prompt)
            if code is None:
                continue
            existing_solutions[language] = code
            if write_per_language:
                write_problem(output_path, problem, order_solutions(languages, existing_solutions))

        if existing_solutions and not write_per_language:
            write_problem(output_path, problem, order_solutions(languages, existing_solutions))
        return output_path

    def _repair_language_order(
        self,
        output_path: Path,
        problem: Problem,
        languages: list[str],
        existing_solutions: OrderedDict[str, str],
    ) -> bool:
        """完整文件如果语言顺序异常，就无模型调用地重写为标准顺序。

        参数：
            output_path: 单题 Markdown 路径。
            problem: 当前题目数据，用于重渲染标题和路径相关内容。
            languages: dataset 中的预期语言顺序。
            existing_solutions: 已从旧 Markdown 读回的代码。

        返回：
            bool: True 表示发生了重写修复；False 表示原文件顺序已经正确。
        """

        actual_order = read_existing_language_order(output_path, languages)
        expected_order = [language for language in languages if language in existing_solutions]
        if actual_order == expected_order:
            return False

        write_problem(output_path, problem, order_solutions(languages, existing_solutions))
        return True

    def generate_many(self, problems: list[Problem], desc: str) -> None:
        """用 tqdm 跟踪并生成一组题目。

        参数：
            problems: 已经按调用方要求筛选和排序的题目列表。
            desc: tqdm 进度条描述，通常是难度名。
        """

        for problem in tqdm(problems, desc=desc):
            self.generate_problem(problem)

    def _generate_language(self, problem: Problem, language: str, starter_code: str, problem_prompt: str) -> str | None:
        """带重试地生成单个语言；失败后记录日志但不阻塞主流程。

        参数：
            problem: 当前题目数据，用于日志和难度选择。
            language: 当前要生成的语言 key。
            starter_code: LeetCode 官方 starter code，用于约束模型输出入口。
            problem_prompt: 同一道题所有语言共享的问题上下文 prompt。

        返回：
            str | None: 成功时返回模型生成的纯代码；达到重试上限仍失败时返回
            None，并把失败详情写入 logger.failure。
        """

        language_prompt = build_language_prompt(language, starter_code)
        for attempt in range(1, self.retry_limit + 1):
            try:
                return self.model_client.generate(
                    difficulty=str(problem.get("difficulty")),
                    system_prompt=SYSTEM_PROMPT,
                    problem_prompt=problem_prompt,
                    language_prompt=language_prompt,
                )
            except Exception as exc:  # pragma: no cover - 具体异常依赖本机 Ollama 运行状态
                self.logger.error(
                    f"{problem.get('frontend_id')}-{problem.get('problem_slug')} {language} "
                    f"retry={attempt} {exc}"
                )
                if attempt == self.retry_limit:
                    self.logger.failure(
                        {
                            "frontend_id": problem.get("frontend_id"),
                            "problem_slug": problem.get("problem_slug"),
                            "difficulty": problem.get("difficulty"),
                            "language": language,
                            "error": str(exc),
                            "retry_count": attempt,
                        }
                    )
        return None

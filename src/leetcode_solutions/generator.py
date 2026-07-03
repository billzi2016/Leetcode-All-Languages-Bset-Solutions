"""串联数据、prompt、模型、断点续跑、日志和 Markdown 写入。

本模块只负责调度；具体行为留在小模块中，保证职责清晰并便于测试。
"""

from __future__ import annotations

from collections import OrderedDict
from pathlib import Path

from tqdm import tqdm

from .config import RETRY_LIMIT
from .dataset_loader import Problem
from .markdown_writer import problem_output_path, write_problem
from .prompt_builder import SYSTEM_PROMPT, build_language_prompt, build_problem_prompt
from .resume import missing_languages


class SolutionGenerator:
    """针对选定题目执行题解生成。"""

    def __init__(self, model_client, logger, output_root: Path, retry_limit: int = RETRY_LIMIT) -> None:
        """连接模型客户端、日志器、输出根目录和重试策略。"""

        self.model_client = model_client
        self.logger = logger
        self.output_root = output_root
        self.retry_limit = retry_limit

    def generate_problem(self, problem: Problem) -> Path:
        """生成单题所有缺失语言，并返回目标 Markdown 路径。"""

        output_path = problem_output_path(problem, self.output_root)
        snippets = problem.get("code_snippets") or {}
        languages = list(snippets.keys())
        todo = missing_languages(output_path, languages)
        if not todo:
            self.logger.info(f"Skipping complete problem {problem.get('frontend_id')} {problem.get('problem_slug')}")
            return output_path

        existing_solutions: OrderedDict[str, str] = OrderedDict()
        if output_path.exists():
            # 当前对部分文件保持保守策略：发现文件不完整时，只补缺失语言。
            # 后续如果需要保留既有代码块，可在 markdown_writer 中增加完整解析。
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
                write_problem(output_path, problem, existing_solutions)

        if existing_solutions and not write_per_language:
            write_problem(output_path, problem, existing_solutions)
        return output_path

    def generate_many(self, problems: list[Problem], desc: str) -> None:
        """用 tqdm 跟踪并生成一组题目。"""

        for problem in tqdm(problems, desc=desc):
            self.generate_problem(problem)

    def _generate_language(self, problem: Problem, language: str, starter_code: str, problem_prompt: str) -> str | None:
        """带重试地生成单个语言；失败后记录日志但不阻塞主流程。"""

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

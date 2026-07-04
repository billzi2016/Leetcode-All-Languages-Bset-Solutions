#!/usr/bin/env python
"""题解生成命令行入口。

本脚本负责把用户输入的 CLI 参数转换为生成器调用。它不承载核心业务逻辑；
题目筛选、prompt 构造、模型调用、Markdown 写入和日志记录都放在
`src/leetcode_solutions/` 中。

典型用法：

- 不传参数：按 Easy、Medium、Hard 顺序生成全部题目；
- `--difficulty Easy`：只生成某个难度；
- `--only-frontend-id 1`：只生成单个题号；
- `--frontend-ids 1 2 4`：生成多个指定题号。

脚本会调用 Ollama，并可能写入或更新题解 Markdown 文件。
"""

from __future__ import annotations

import argparse
import warnings
from pathlib import Path

from leetcode_solutions.config import DIFFICULTY_ORDER, Paths, THINK_BY_DIFFICULTY
from leetcode_solutions.dataset_loader import filter_by_difficulty, find_by_frontend_id, load_questions
from leetcode_solutions.generator import SolutionGenerator
from leetcode_solutions.logger import RunLogger
from leetcode_solutions.ollama_client import OllamaClient


def suppress_environment_warnings() -> None:
    """屏蔽当前 Python 环境里无法由本项目直接修复的 requests 依赖版本告警。

    背景：
        某些本机 Python 环境会在导入依赖时打印 requests/urllib3/chardet
        版本组合 warning。项目实际模型调用使用 Python `ollama` 包，不直接
        通过 requests 调接口，因此这里屏蔽该环境噪音，避免长任务日志被污染。
    """

    warnings.filterwarnings(
        "ignore",
        message=r"urllib3 .* or chardet .*/charset_normalizer .* doesn't match a supported version!",
    )


suppress_environment_warnings()


def parse_args() -> argparse.Namespace:
    """解析命令行参数。

    返回：
        argparse.Namespace: 包含 root、only_frontend_id、frontend_ids、
        difficulty 的参数对象。
    """

    parser = argparse.ArgumentParser(description="Generate LeetCode all-language solutions.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root path.")
    parser.add_argument("--only-frontend-id", help="Generate only one LeetCode frontend id, such as 1.")
    parser.add_argument("--frontend-ids", nargs="+", help="Generate multiple LeetCode frontend ids, such as 1 2 4.")
    parser.add_argument(
        "--difficulty",
        choices=DIFFICULTY_ORDER,
        help="Generate one difficulty only when --only-frontend-id is not set.",
    )
    return parser.parse_args()


def main() -> int:
    """执行生成流程并返回进程退出码。

    返回：
        int: 成功执行参数对应流程时返回 0。单个题号不存在时会记录错误并
        继续处理其它题号，不把整个进程置为失败。

    执行顺序：
        1. 解析路径、读取 dataset；
        2. 创建日志器和 Ollama client；
        3. 如果指定题号，则按题号逐个生成；
        4. 否则按难度顺序批量生成；
        5. finally 中关闭日志文件。
    """

    args = parse_args()
    paths = Paths.from_root(args.root)
    questions = load_questions(paths.dataset)
    logger = RunLogger(paths.logs_root)
    client = OllamaClient(THINK_BY_DIFFICULTY)
    generator = SolutionGenerator(client, logger, paths.output_root)

    try:
        requested_ids = []
        if args.only_frontend_id:
            requested_ids.append(args.only_frontend_id)
        if args.frontend_ids:
            requested_ids.extend(args.frontend_ids)

        if requested_ids:
            for frontend_id in requested_ids:
                problem = find_by_frontend_id(questions, frontend_id)
                if problem is None:
                    logger.error(f"Cannot find frontend_id={frontend_id}")
                    continue
                generator.generate_problem(problem)
            return 0

        difficulties = [args.difficulty] if args.difficulty else list(DIFFICULTY_ORDER)
        for difficulty in difficulties:
            generator.generate_many(filter_by_difficulty(questions, difficulty), difficulty)
        return 0
    finally:
        logger.close()


if __name__ == "__main__":
    raise SystemExit(main())

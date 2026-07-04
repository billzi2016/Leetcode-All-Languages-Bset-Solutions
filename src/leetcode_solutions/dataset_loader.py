"""读取、校验和筛选 LeetCode 合并数据集。

本模块刻意只处理“数据集本身”的问题：读取 JSON、确认顶层结构、
按题号排序、按难度筛选、按 frontend_id 查找题目。它不构造 prompt、
不调用模型、不写日志、不写 Markdown 文件。

这样拆分的原因是：数据集的排序和筛选规则会被生成器、审计脚本、测试
共同复用。如果这些规则散落在不同入口里，很容易出现生成顺序和审计顺序
不一致的问题。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .config import DIFFICULTY_ORDER


Problem = dict[str, Any]


def load_questions(dataset_path: Path) -> list[Problem]:
    """读取 `merged_problems.json` 并返回顶层 `questions` 列表。

    参数：
        dataset_path: 本地数据集 JSON 文件路径。

    返回：
        list[Problem]: 原始题目字典列表。函数不主动排序，调用方可以
        根据需要再调用 `sort_questions()` 或 `filter_by_difficulty()`。

    抛出：
        ValueError: JSON 顶层没有 `questions`，或 `questions` 不是列表。
    """

    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    questions = data.get("questions")
    if not isinstance(questions, list):
        raise ValueError("dataset must contain a top-level questions list")
    return questions


def frontend_id_as_int(problem: Problem) -> int:
    """返回数字形式的 LeetCode frontend_id。

    参数：
        problem: dataset 中的一道题目字典。

    返回：
        int: 可用于排序、分桶和四位补零文件名的数字题号。

    抛出：
        ValueError: frontend_id 缺失或不是纯数字。这里选择直接失败，
        是因为输出路径依赖数字题号；静默跳过会让生成结果不可预测。
    """

    frontend_id = str(problem.get("frontend_id", "")).strip()
    if not frontend_id.isdigit():
        raise ValueError(f"frontend_id is not numeric: {frontend_id!r}")
    return int(frontend_id)


def sort_questions(questions: list[Problem]) -> list[Problem]:
    """按数字题号升序返回新的题目列表。

    参数：
        questions: 待排序的题目列表。

    返回：
        list[Problem]: 排序后的新列表，不会原地修改输入列表。
    """

    return sorted(questions, key=frontend_id_as_int)


def filter_by_difficulty(questions: list[Problem], difficulty: str) -> list[Problem]:
    """筛选指定难度并按题号升序排序。

    参数：
        questions: 全量或局部题目列表。
        difficulty: 目标难度，必须和 dataset 中的值一致，例如
            `Easy`、`Medium`、`Hard`。

    返回：
        list[Problem]: 只包含目标难度的题目，并已经按 frontend_id 排序。
    """

    return sort_questions([q for q in questions if q.get("difficulty") == difficulty])


def ordered_by_difficulty(questions: list[Problem]) -> list[Problem]:
    """按 Easy、Medium、Hard 分组排序后合并返回。

    参数：
        questions: 全量题目列表。

    返回：
        list[Problem]: 先 Easy、再 Medium、最后 Hard；每个难度内部按题号
        升序排列。这个顺序适合全量生成时先验证低风险题目，再处理难题。
    """

    ordered: list[Problem] = []
    for difficulty in DIFFICULTY_ORDER:
        ordered.extend(filter_by_difficulty(questions, difficulty))
    return ordered


def find_by_frontend_id(questions: list[Problem], frontend_id: str) -> Problem | None:
    """根据 LeetCode frontend_id 查找题目。

    参数：
        questions: 题目列表。
        frontend_id: 用户输入的题号，可以是字符串或可字符串化的值。

    返回：
        Problem | None: 找到时返回题目字典；找不到时返回 None，让 CLI
        能记录错误并继续处理其它题号。
    """

    target = str(frontend_id)
    for question in questions:
        if str(question.get("frontend_id")) == target:
            return question
    return None

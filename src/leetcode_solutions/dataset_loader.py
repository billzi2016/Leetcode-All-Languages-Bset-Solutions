"""读取和筛选 LeetCode 合并数据集。

本模块只负责数据集形状、难度筛选和题号排序，不处理 prompt、模型调用、日志或文件写入。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .config import DIFFICULTY_ORDER


Problem = dict[str, Any]


def load_questions(dataset_path: Path) -> list[Problem]:
    """读取 `merged_problems.json` 并返回顶层 `questions` 列表。"""

    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    questions = data.get("questions")
    if not isinstance(questions, list):
        raise ValueError("dataset must contain a top-level questions list")
    return questions


def frontend_id_as_int(problem: Problem) -> int:
    """返回数字形式的 frontend_id；非数字 ID 直接抛出异常。"""

    frontend_id = str(problem.get("frontend_id", "")).strip()
    if not frontend_id.isdigit():
        raise ValueError(f"frontend_id is not numeric: {frontend_id!r}")
    return int(frontend_id)


def sort_questions(questions: list[Problem]) -> list[Problem]:
    """按数字题号排序。"""

    return sorted(questions, key=frontend_id_as_int)


def filter_by_difficulty(questions: list[Problem], difficulty: str) -> list[Problem]:
    """筛选指定难度并按题号排序。"""

    return sort_questions([q for q in questions if q.get("difficulty") == difficulty])


def ordered_by_difficulty(questions: list[Problem]) -> list[Problem]:
    """按 Easy、Medium、Hard 分组排序后合并返回。"""

    ordered: list[Problem] = []
    for difficulty in DIFFICULTY_ORDER:
        ordered.extend(filter_by_difficulty(questions, difficulty))
    return ordered


def find_by_frontend_id(questions: list[Problem], frontend_id: str) -> Problem | None:
    """根据 LeetCode frontend_id 查找题目。"""

    target = str(frontend_id)
    for question in questions:
        if str(question.get("frontend_id")) == target:
            return question
    return None

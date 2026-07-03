"""检测生成文件是否完整或部分完成。

生成器用本模块避免重跑时重复调用模型。语言检测基于 Markdown 二级标题。
"""

from __future__ import annotations

from pathlib import Path

from .markdown_writer import language_heading, read_existing_languages


def missing_languages(path: Path, languages: list[str]) -> list[str]:
    """返回已有 Markdown 中缺失的语言 key。"""

    existing_headings = read_existing_languages(path)
    return [language for language in languages if language_heading(language) not in existing_headings]


def is_problem_complete(path: Path, languages: list[str]) -> bool:
    """判断目标 Markdown 是否已经包含所有预期语言。"""

    return path.exists() and not missing_languages(path, languages)

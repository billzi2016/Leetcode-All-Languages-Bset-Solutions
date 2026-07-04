"""检测生成文件是否完整或部分完成。

断点续跑的核心原则是：已有且非空的语言代码不要重复调用模型生成。
本模块只做“缺哪些语言”的判断，不负责读取代码内容，也不负责写回文件。

语言完成状态基于 Markdown 二级标题和非空代码块判断，具体解析逻辑复用
`markdown_writer.read_existing_languages()`。
"""

from __future__ import annotations

from pathlib import Path

from .markdown_writer import language_heading, read_existing_languages


def missing_languages(path: Path, languages: list[str]) -> list[str]:
    """返回已有 Markdown 中缺失的语言 key。

    参数：
        path: 单题 Markdown 文件路径。
        languages: dataset 中该题应包含的完整语言 key 列表。

    返回：
        list[str]: 仍需生成的语言 key，顺序与 `languages` 一致。
    """

    existing_headings = read_existing_languages(path)
    return [language for language in languages if language_heading(language) not in existing_headings]


def is_problem_complete(path: Path, languages: list[str]) -> bool:
    """判断目标 Markdown 是否已经包含所有预期语言。

    参数：
        path: 单题 Markdown 文件路径。
        languages: dataset 中该题应包含的完整语言 key 列表。

    返回：
        bool: 文件存在且没有缺失语言时为 True。
    """

    return path.exists() and not missing_languages(path, languages)

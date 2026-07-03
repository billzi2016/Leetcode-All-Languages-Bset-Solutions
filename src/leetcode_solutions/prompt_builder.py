"""构造题目和语言 prompt。

prompt 构造与模型调用分离，方便测试准确验证哪些字段进入模型。`images` 会被排除，因为目标 Ollama 模型不是多模态模型。
"""

from __future__ import annotations

from typing import Any


SYSTEM_PROMPT = """You are a senior algorithm engineer and LeetCode solution generator.

Generate only the optimal accepted solution for the requested target language.
Use the provided LeetCode starter code signature and style exactly.
Return raw code only. Do not wrap the answer in Markdown code fences.
Do not include the problem statement, explanations, complexity analysis, tests,
main functions, extra I/O, pseudocode, or unsupported dependencies.
If editorial or solution reference content is provided, use it only to improve
correctness and produce clean submit-ready code.
"""


def _append_section(lines: list[str], title: str, value: Any) -> None:
    """只在字段有值时追加一个 prompt 小节。"""

    if value in (None, "", [], {}):
        return
    lines.append(f"\n## {title}")
    if isinstance(value, list):
        for item in value:
            lines.append(_format_value(item))
    else:
        lines.append(_format_value(value))


def _format_value(value: Any) -> str:
    """格式化结构化字段，同时排除图片 URL。"""

    if isinstance(value, dict):
        filtered = {k: v for k, v in value.items() if k != "images" and v not in (None, "", [], {})}
        return "\n".join(f"- {key}: {_format_value(val)}" for key, val in filtered.items())
    if isinstance(value, list):
        return "\n".join(f"- {_format_value(item)}" for item in value)
    return str(value)


def build_problem_prompt(problem: dict[str, Any]) -> str:
    """构造同一道题所有语言复用的题目公共 prompt。"""

    lines: list[str] = ["# Problem Context"]
    metadata = {
        "title": problem.get("title"),
        "problem_id": problem.get("problem_id"),
        "frontend_id": problem.get("frontend_id"),
        "difficulty": problem.get("difficulty"),
        "problem_slug": problem.get("problem_slug"),
        "topics": problem.get("topics"),
    }
    _append_section(lines, "Problem Metadata", metadata)
    _append_section(lines, "Problem Statement", problem.get("description"))
    _append_section(lines, "Examples", problem.get("examples"))
    _append_section(lines, "Constraints", problem.get("constraints"))
    _append_section(lines, "Follow Ups", problem.get("follow_ups"))
    _append_section(lines, "Hints", problem.get("hints"))

    # 上游数据当前使用 `solution` 单数字段；这里同时兼容 `solutions`，
    # 避免 schema 轻微变化导致 editorial 内容丢失。
    editorial = problem.get("solutions") or problem.get("solution")
    _append_section(lines, "Editorial / Solution Reference", editorial)
    return "\n".join(lines).strip() + "\n"


def build_language_prompt(language: str, starter_code: str) -> str:
    """构造单个语言的 user prompt。"""

    return (
        f"Target Language: {language}\n\n"
        "Use this LeetCode starter code signature and style:\n\n"
        f"{starter_code}\n\n"
        "Generate the optimal accepted solution for this language.\n"
        "Return raw code only. Do not wrap the answer in Markdown code fences.\n"
    )

"""构造题目级 prompt 和语言级 prompt。

prompt 构造与模型调用分离，目的是让测试可以准确验证哪些字段会进入模型，
也让模型客户端只负责发送请求，不掺杂业务格式化逻辑。

本模块有两个层次：

- `build_problem_prompt()`：同一道题所有语言共用，包含题目元数据、题面、
  示例、约束、follow up、hint 和可用的参考解；
- `build_language_prompt()`：每种语言单独构造，重点传入目标语言和 LeetCode
  starter code，约束模型必须保留提交入口。

上游数据中可能包含 `images` 字段，但当前目标模型不是多模态模型，因此
格式化结构化字段时会排除图片 URL，避免把无用信息塞进上下文。
"""

from __future__ import annotations

from typing import Any


SYSTEM_PROMPT = """You are a senior algorithm engineer and LeetCode solution generator.

Generate only the optimal accepted solution for the requested target language.
Use the provided LeetCode starter code signature and style exactly.
The final answer must include the provided LeetCode submission entry point, such as the Solution class, impl block, function signature, module, or contract header.
The final answer must be directly pasteable into the LeetCode editor for the target language.
Think concisely, directly, and forcefully.
Return raw code only. Do not wrap the answer in Markdown code fences.
Do not include the problem statement, explanations, complexity analysis, tests,
main functions, extra I/O, pseudocode, or unsupported dependencies.
If editorial or solution reference content is provided, use it only to improve
correctness and produce clean submit-ready code.
"""


def _append_section(lines: list[str], title: str, value: Any) -> None:
    """只在字段有值时追加一个 prompt 小节。

    参数：
        lines: 正在构造的 prompt 行列表，会被原地追加内容。
        title: 小节标题，例如 `Problem Statement`。
        value: 小节内容。支持字符串、列表、字典；空值会被跳过。
    """

    if value in (None, "", [], {}):
        return
    lines.append(f"\n## {title}")
    if isinstance(value, list):
        for item in value:
            lines.append(_format_value(item))
    else:
        lines.append(_format_value(value))


def _format_value(value: Any) -> str:
    """格式化结构化字段，同时排除图片 URL。

    参数：
        value: dataset 中的任意字段值，可能是字符串、列表或字典。

    返回：
        str: 适合放进 prompt 的文本。字典会展开成 `- key: value`，
        列表会逐项展开，普通值直接转成字符串。
    """

    if isinstance(value, dict):
        filtered = {k: v for k, v in value.items() if k != "images" and v not in (None, "", [], {})}
        return "\n".join(f"- {key}: {_format_value(val)}" for key, val in filtered.items())
    if isinstance(value, list):
        return "\n".join(f"- {_format_value(item)}" for item in value)
    return str(value)


def build_problem_prompt(problem: dict[str, Any]) -> str:
    """构造同一道题所有语言复用的题目公共 prompt。

    参数：
        problem: dataset 中的一道题，可能包含题面、示例、约束、提示、
            topics 和参考解等字段。

    返回：
        str: 以 `# Problem Context` 开头的题目上下文 prompt。
    """

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
    """构造单个语言的 user prompt。

    参数：
        language: dataset 中的目标语言 key。
        starter_code: LeetCode 官方 starter code。模型必须沿用这里的函数
            签名、类名或模块入口。

    返回：
        str: 只针对当前语言的 prompt，要求模型返回 raw code。
    """

    return (
        f"Target Language: {language}\n\n"
        "Use this LeetCode starter code signature and style:\n\n"
        f"{starter_code}\n\n"
        "Generate the optimal accepted solution for this language.\n"
        "Return raw code only. Do not wrap the answer in Markdown code fences.\n"
    )

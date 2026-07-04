"""Ollama 模型客户端封装。

本模块是生成器和本机 Ollama 服务之间的边界层。生成器只依赖
`ModelClient` 协议，不直接导入 `ollama`，这样测试可以注入 fake client，
也能避免模型调用细节泄漏到调度逻辑里。

当前实现使用 Python `ollama` 包，不直接用 `requests` 调 HTTP。这里集中处理：

- 模型名；
- 最大输出 token 数；
- temperature；
- 按题目难度选择 think 强度；
- 移除模型偶尔返回的 Markdown code fence。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .config import MAX_OUTPUT_TOKENS, MODEL_NAME, RETRY_LIMIT, TEMPERATURE


class ModelClient(Protocol):
    """生成器依赖的最小模型接口。

    只定义生成器真正需要的方法，方便测试里用轻量 fake client 替代真实
    Ollama 调用。
    """

    def generate(self, *, difficulty: str, system_prompt: str, problem_prompt: str, language_prompt: str) -> str:
        """生成单个语言的题解。

        参数：
            difficulty: 题目难度，用于选择 think 强度。
            system_prompt: 全局系统提示词，约束输出必须是可提交代码。
            problem_prompt: 当前题目的公共上下文。
            language_prompt: 当前目标语言和 starter code。

        返回：
            str: 纯代码文本。
        """


@dataclass(frozen=True)
class OllamaOptions:
    """传给 Python ollama client 的稳定配置。

    参数：
        model: Ollama 模型名。
        max_output_tokens: `num_predict` 上限。题解生成需要保留足够空间，
            避免长代码被截断。
        temperature: 采样温度。当前使用较低值，减少代码输出随机性。
        retry_limit: 模型调用重试上限。这里保留该值是为了配置集中，但实际
            重试循环由 `SolutionGenerator` 执行。
    """

    model: str = MODEL_NAME
    max_output_tokens: int = MAX_OUTPUT_TOKENS
    temperature: float = TEMPERATURE
    retry_limit: int = RETRY_LIMIT


class OllamaClient:
    """通过 Python `ollama` 库生成题解。"""

    def __init__(self, think_by_difficulty: dict[str, str], options: OllamaOptions | None = None) -> None:
        """保存模型配置和难度到 think 模式的映射。

        参数：
            think_by_difficulty: 难度到 think 强度的映射，例如
                `{"Easy": "low", "Medium": "medium", "Hard": "high"}`。
            options: 可选模型配置；不传时使用项目默认配置。
        """

        self.think_by_difficulty = think_by_difficulty
        self.options = options or OllamaOptions()

    def build_options(self, difficulty: str) -> dict:
        """构造传给 `ollama.chat()` 的 options。

        参数：
            difficulty: 当前题目难度。

        返回：
            dict: 包含 think 强度、输出上限和 temperature 的 options。
        """

        return {
            "think": self.think_by_difficulty[difficulty],
            "num_predict": self.options.max_output_tokens,
            "temperature": self.options.temperature,
        }

    def generate(self, *, difficulty: str, system_prompt: str, problem_prompt: str, language_prompt: str) -> str:
        """调用 Ollama 并返回纯代码。

        参数：
            difficulty: 当前题目难度，用于选择 think 强度。
            system_prompt: 全局约束 prompt。
            problem_prompt: 当前题目的题面、示例、约束、提示和参考解信息。
            language_prompt: 当前目标语言及 starter code。

        返回：
            str: 去掉 Markdown code fence 后的代码文本。
        """

        import ollama

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": problem_prompt},
            {"role": "user", "content": language_prompt},
        ]
        response = ollama.chat(
            model=self.options.model,
            messages=messages,
            options=self.build_options(difficulty),
        )
        content = response.get("message", {}).get("content", "")
        return strip_code_fences(content)


def strip_code_fences(content: str) -> str:
    """移除模型意外输出的 Markdown 代码块包裹。

    参数：
        content: 模型返回的原始文本。

    返回：
        str: 如果外层是 fenced code block，则去掉第一行和最后一行 fence；
        否则只做首尾空白清理。

    说明：
        prompt 明确要求 raw code，但模型偶尔仍会返回 ```python 这类包裹。
        这里做保守修正，只移除最外层 fence，不尝试重写代码内容。
    """

    text = content.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text

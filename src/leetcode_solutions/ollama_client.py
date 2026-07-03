"""Ollama 模型客户端封装。

项目使用 Python `ollama` 库，不直接使用 requests 调 HTTP。本模块集中管理模型参数、think 模式和 100k 输出限制。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .config import MAX_OUTPUT_TOKENS, MODEL_NAME, RETRY_LIMIT, TEMPERATURE


class ModelClient(Protocol):
    """生成器依赖的模型接口，方便测试注入 fake client。"""

    def generate(self, *, difficulty: str, system_prompt: str, problem_prompt: str, language_prompt: str) -> str:
        """生成单个语言的题解。"""


@dataclass(frozen=True)
class OllamaOptions:
    """传给 Python ollama client 的配置。"""

    model: str = MODEL_NAME
    max_output_tokens: int = MAX_OUTPUT_TOKENS
    temperature: float = TEMPERATURE
    retry_limit: int = RETRY_LIMIT


class OllamaClient:
    """通过 Python `ollama` 库生成题解。"""

    def __init__(self, think_by_difficulty: dict[str, str], options: OllamaOptions | None = None) -> None:
        """保存模型配置和难度到 think 模式的映射。"""

        self.think_by_difficulty = think_by_difficulty
        self.options = options or OllamaOptions()

    def build_options(self, difficulty: str) -> dict:
        """构造包含 think 模式和 100k 输出限制的 Ollama options。"""

        return {
            "think": self.think_by_difficulty[difficulty],
            "num_predict": self.options.max_output_tokens,
            "temperature": self.options.temperature,
        }

    def generate(self, *, difficulty: str, system_prompt: str, problem_prompt: str, language_prompt: str) -> str:
        """调用 Ollama 并返回纯代码。"""

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
    """移除模型意外输出的 Markdown 代码块包裹。"""

    text = content.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text

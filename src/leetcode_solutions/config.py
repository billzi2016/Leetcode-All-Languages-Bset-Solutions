"""集中管理生成器配置。

本文件只放稳定默认值，例如模型名、think 映射、输出上限和路径约定，避免这些规则散落在多个模块里。
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


MODEL_NAME = "gpt-oss:120b"
MAX_OUTPUT_TOKENS = 100_000
RETRY_LIMIT = 3
DIFFICULTY_ORDER = ("Easy", "Medium", "Hard")
THINK_BY_DIFFICULTY = {
    "Easy": "low",
    "Medium": "medium",
    "Hard": "high",
}


@dataclass(frozen=True)
class Paths:
    """生成流程使用的文件系统路径。"""

    root: Path
    dataset: Path
    output_root: Path
    logs_root: Path

    @classmethod
    def from_root(cls, root: Path) -> "Paths":
        """根据仓库根目录构造默认路径。"""

        return cls(
            root=root,
            dataset=root / "dataset" / "merged_problems.json",
            output_root=root,
            logs_root=root / "logs",
        )

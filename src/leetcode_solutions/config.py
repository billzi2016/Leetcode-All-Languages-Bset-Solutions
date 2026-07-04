"""集中管理题解生成器的稳定配置。

这个模块的设计意图是把“全局默认值”和“约定路径”集中放在一处：

- 模型相关默认值，例如模型名、输出 token 上限、温度和重试次数；
- 难度顺序，例如全量生成时必须先 Easy、再 Medium、最后 Hard；
- 难度到 Ollama think 强度的映射；
- 从仓库根目录推导 dataset、输出目录和日志目录的规则。

业务模块不应该各自硬编码这些值，否则后续调整模型、路径或难度顺序时
容易出现一处改了、另一处没改的分叉。
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


MODEL_NAME = "gpt-oss:120b"
MAX_OUTPUT_TOKENS = 100_000
TEMPERATURE = 0.1
RETRY_LIMIT = 3
DIFFICULTY_ORDER = ("Easy", "Medium", "Hard")
THINK_BY_DIFFICULTY = {
    "Easy": "low",
    "Medium": "medium",
    "Hard": "high",
}


@dataclass(frozen=True)
class Paths:
    """生成流程需要反复使用的一组文件系统路径。

    参数：
        root: 仓库根目录。CLI 默认使用当前工作目录，也可以通过
            `--root` 显式传入其它仓库路径。
        dataset: 本地 LeetCode 合并数据集路径。当前项目约定为
            `dataset/merged_problems.json`。
        output_root: 题解 Markdown 的输出根目录。当前就是仓库根目录，
            因为题解按 `easy/`、`medium/`、`hard/` 直接落盘。
        logs_root: 每次生成运行的日志根目录，具体运行会在其下创建
            时间戳子目录。
    """

    root: Path
    dataset: Path
    output_root: Path
    logs_root: Path

    @classmethod
    def from_root(cls, root: Path) -> "Paths":
        """根据仓库根目录构造默认路径集合。

        参数：
            root: 仓库根目录。

        返回：
            Paths: 按项目约定推导出的 dataset、输出根目录和日志目录。
        """

        return cls(
            root=root,
            dataset=root / "dataset" / "merged_problems.json",
            output_root=root,
            logs_root=root / "logs",
        )

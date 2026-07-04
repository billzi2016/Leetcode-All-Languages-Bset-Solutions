"""运行日志分流器。

生成任务可能持续很久，且模型调用失败通常只影响某一道题的某一种语言。
本模块把日志拆成三类：

- stdout.log：普通进度和跳过信息；
- stderr.log：警告和错误；
- failures.jsonl：结构化失败记录，后续可以据此定向补跑。

普通日志仍然会打印到屏幕，方便实时观察；文件日志用于中断后排查。
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, TextIO


class RunLogger:
    """写入带时间戳的 stdout/stderr 日志和 JSONL 失败记录。

    参数：
        logs_root: 日志根目录。
        run_datetime: 可选运行时间字符串。测试可以传固定值，生产运行默认
            使用当前时间生成目录名。
    """

    def __init__(self, logs_root: Path, run_datetime: str | None = None) -> None:
        """创建本次运行目录并打开三个日志文件。"""

        self.run_datetime = run_datetime or datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.run_dir = logs_root / self.run_datetime
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self._stdout = (self.run_dir / "stdout.log").open("a", encoding="utf-8")
        self._stderr = (self.run_dir / "stderr.log").open("a", encoding="utf-8")
        self._failures = (self.run_dir / "failures.jsonl").open("a", encoding="utf-8")

    def close(self) -> None:
        """关闭所有日志文件句柄。

        生成脚本在 `finally` 中调用该方法，确保正常结束或异常退出时都尽量
        刷新并释放文件句柄。
        """

        self._stdout.close()
        self._stderr.close()
        self._failures.close()

    def info(self, message: str) -> None:
        """把普通信息写到 stdout 和 stdout.log。

        参数：
            message: 人类可读日志文本。
        """

        self._write(self._stdout, sys.stdout, "INFO", message)

    def warn(self, message: str) -> None:
        """把警告信息写到 stderr 和 stderr.log。

        参数：
            message: 人类可读警告文本。
        """

        self._write(self._stderr, sys.stderr, "WARN", message)

    def error(self, message: str) -> None:
        """把错误信息写到 stderr 和 stderr.log。

        参数：
            message: 人类可读错误文本。
        """

        self._write(self._stderr, sys.stderr, "ERROR", message)

    def failure(self, record: dict[str, Any]) -> None:
        """向 failures.jsonl 追加一条结构化失败记录。

        参数：
            record: 失败上下文，例如题号、slug、难度、语言、错误信息和
                重试次数。函数会自动补充当前时间。
        """

        payload = {"datetime": self._timestamp(), **record}
        self._failures.write(json.dumps(payload, ensure_ascii=False) + "\n")
        self._failures.flush()

    def _write(self, file: TextIO, stream: TextIO, level: str, message: str) -> None:
        """把同一行日志同时写到屏幕流和日志文件。

        参数：
            file: 已打开的日志文件句柄。
            stream: `sys.stdout` 或 `sys.stderr`。
            level: 日志级别文本。
            message: 日志正文。
        """

        line = f"{self._timestamp()} [{level}] {message}"
        print(line, file=stream)
        file.write(line + "\n")
        file.flush()

    @staticmethod
    def _timestamp() -> str:
        """返回日志使用的人类可读时间戳。"""

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

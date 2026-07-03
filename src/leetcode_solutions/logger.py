"""运行日志分流器。

stdout、stderr 和结构化失败记录会分别写入独立文件，同时 stdout/stderr 仍打印到屏幕，方便实时观察和后续复跑。
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, TextIO


class RunLogger:
    """写入带时间戳的 stdout/stderr 日志和 JSONL 失败记录。"""

    def __init__(self, logs_root: Path, run_datetime: str | None = None) -> None:
        """创建本次运行目录并打开三个日志文件。"""

        self.run_datetime = run_datetime or datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.run_dir = logs_root / self.run_datetime
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self._stdout = (self.run_dir / "stdout.log").open("a", encoding="utf-8")
        self._stderr = (self.run_dir / "stderr.log").open("a", encoding="utf-8")
        self._failures = (self.run_dir / "failures.jsonl").open("a", encoding="utf-8")

    def close(self) -> None:
        """关闭所有日志文件句柄。"""

        self._stdout.close()
        self._stderr.close()
        self._failures.close()

    def info(self, message: str) -> None:
        """把普通信息写到 stdout 和 stdout.log。"""

        self._write(self._stdout, sys.stdout, "INFO", message)

    def warn(self, message: str) -> None:
        """把警告信息写到 stderr 和 stderr.log。"""

        self._write(self._stderr, sys.stderr, "WARN", message)

    def error(self, message: str) -> None:
        """把错误信息写到 stderr 和 stderr.log。"""

        self._write(self._stderr, sys.stderr, "ERROR", message)

    def failure(self, record: dict[str, Any]) -> None:
        """向 failures.jsonl 追加一条结构化失败记录。"""

        payload = {"datetime": self._timestamp(), **record}
        self._failures.write(json.dumps(payload, ensure_ascii=False) + "\n")
        self._failures.flush()

    def _write(self, file: TextIO, stream: TextIO, level: str, message: str) -> None:
        """把同一行日志同时写到屏幕流和日志文件。"""

        line = f"{self._timestamp()} [{level}] {message}"
        print(line, file=stream)
        file.write(line + "\n")
        file.flush()

    @staticmethod
    def _timestamp() -> str:
        """返回日志使用的人类可读时间戳。"""

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

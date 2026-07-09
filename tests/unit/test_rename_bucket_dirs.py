"""历史题号分桶目录迁移脚本测试。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from migrate.rename_bucket_dirs import run


class RenameBucketDirsTest(unittest.TestCase):
    """验证旧分桶目录可以迁移到固定宽度分桶。"""

    def test_merge_into_existing_bucket_without_conflict(self) -> None:
        """目标分桶已存在时，应把旧分桶文件合并进去。"""

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old_bucket = root / "Leetcode-Easy" / "1-100"
            new_bucket = root / "Leetcode-Easy" / "0001-0100"
            old_bucket.mkdir(parents=True)
            new_bucket.mkdir(parents=True)
            (old_bucket / "0009-palindrome-number.md").write_text("new", encoding="utf-8")
            (new_bucket / "0001-two-sum.md").write_text("old", encoding="utf-8")

            exit_code = run(root, apply=True)

            self.assertEqual(0, exit_code)
            self.assertFalse(old_bucket.exists())
            self.assertEqual("new", (new_bucket / "0009-palindrome-number.md").read_text(encoding="utf-8"))
            self.assertEqual("old", (new_bucket / "0001-two-sum.md").read_text(encoding="utf-8"))

    def test_existing_file_conflict_requires_overwrite_flag(self) -> None:
        """默认遇到目标同名文件应中止，避免误覆盖。"""

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old_bucket = root / "Leetcode-Easy" / "1-100"
            new_bucket = root / "Leetcode-Easy" / "0001-0100"
            old_bucket.mkdir(parents=True)
            new_bucket.mkdir(parents=True)
            (old_bucket / "0001-two-sum.md").write_text("server", encoding="utf-8")
            (new_bucket / "0001-two-sum.md").write_text("local", encoding="utf-8")

            with self.assertRaises(SystemExit):
                run(root, apply=True)

            self.assertTrue(old_bucket.exists())
            self.assertEqual("local", (new_bucket / "0001-two-sum.md").read_text(encoding="utf-8"))

    def test_overwrite_files_replaces_existing_file(self) -> None:
        """显式允许覆盖时，应使用旧分桶文件替换目标同名文件。"""

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old_bucket = root / "Leetcode-Easy" / "1-100"
            new_bucket = root / "Leetcode-Easy" / "0001-0100"
            old_bucket.mkdir(parents=True)
            new_bucket.mkdir(parents=True)
            (old_bucket / "0001-two-sum.md").write_text("server", encoding="utf-8")
            (new_bucket / "0001-two-sum.md").write_text("local", encoding="utf-8")

            exit_code = run(root, apply=True, overwrite_files=True)

            self.assertEqual(0, exit_code)
            self.assertFalse(old_bucket.exists())
            self.assertEqual("server", (new_bucket / "0001-two-sum.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

"""markdown_writer 的单元测试。"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from leetcode_solutions.markdown_writer import bucket_name, problem_output_path, read_existing_languages, write_problem


class MarkdownWriterTest(unittest.TestCase):
    """验证路径分桶、文件名和 Markdown 格式。"""

    def test_bucket_and_path(self) -> None:
        """题号应按每 100 题分桶，并使用四位补零文件名。"""

        problem = {"frontend_id": "1", "difficulty": "Easy", "problem_slug": "two-sum"}
        path = problem_output_path(problem, Path("/tmp/out"))
        self.assertEqual("1-100", bucket_name(1))
        self.assertEqual(Path("/tmp/out/easy/1-100/0001-two-sum.md"), path)

    def test_write_and_read_languages(self) -> None:
        """写出的 Markdown 应能被 resume 逻辑读回语言标题。"""

        problem = {"frontend_id": "1", "difficulty": "Easy", "problem_slug": "two-sum", "title": "Two Sum"}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "easy/1-100/0001-two-sum.md"
            write_problem(path, problem, {"python3": "class Solution:\n    pass"})
            text = path.read_text(encoding="utf-8")
            languages = read_existing_languages(path)

        self.assertIn("# 0001. Two Sum", text)
        self.assertIn("## Python3", text)
        self.assertIn("```python", text)
        self.assertEqual({"Python3"}, languages)


if __name__ == "__main__":
    unittest.main()

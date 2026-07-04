# 迁移和维护脚本

这个目录放一次性迁移脚本或维护类脚本，不属于 `scripts/` 里的常规生成入口。

## `audit_missing_solutions.py`

用于审计已经生成的 Markdown 题解文件，报告：

- 缺失的语言 section
- 语言已经齐全、但顺序可以修复的文件

示例：

```bash
PYTHONPATH=src python migrate/audit_missing_solutions.py
PYTHONPATH=src python migrate/audit_missing_solutions.py --difficulty Hard
PYTHONPATH=src python migrate/audit_missing_solutions.py --frontend-ids 4 10
```

这个脚本是只读的。它不会调用 Ollama，不会重新生成代码，也不会修改 Markdown 文件。如果它报告问题，再用 `scripts/generate_solutions.py` 针对对应题目补齐或修复。

## `rename_bucket_dirs.py`

把旧分桶目录重命名为固定宽度范围：

```text
1-100 -> 0001-0100
101-200 -> 0101-0200
```

只预览，不修改：

```bash
python migrate/rename_bucket_dirs.py
```

实际执行重命名：

```bash
python migrate/rename_bucket_dirs.py --apply
```

这个迁移逻辑刻意和生成器分开。生成器只负责按新规则写新路径；历史目录需要调整时，用这个脚本单独处理。

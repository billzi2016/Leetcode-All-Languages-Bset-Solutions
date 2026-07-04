#!/usr/bin/env python
"""把旧的题号分桶目录重命名为固定宽度范围目录。

这个脚本用于一次性迁移历史目录名，不属于正常题解生成流程。业务代码中的
新路径规则已经由 `leetcode_solutions.markdown_writer.bucket_name()` 负责；
这里单独保留迁移脚本，是为了避免把“改老目录”的临时逻辑写进生成器。

迁移规则：

- `1-100` -> `0001-0100`
- `101-200` -> `0101-0200`
- `1301-1400` -> `1301-1400`

默认只打印计划，不修改文件系统。确认输出无误后，加 `--apply` 才会真正
执行重命名。
"""

from __future__ import annotations

import argparse
from pathlib import Path


DIFFICULTY_DIRS = ("easy", "medium", "hard")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。

    返回：
        argparse.Namespace: 包含仓库根目录和是否执行实际迁移的开关。
    """

    parser = argparse.ArgumentParser(description="Rename old problem bucket directories to fixed-width ranges.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root path.")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually rename directories. Without this flag the script only prints the plan.",
    )
    return parser.parse_args()


def fixed_width_bucket_name(name: str) -> str | None:
    """把旧分桶目录名转换为固定宽度目录名。

    参数：
        name: 目录名，例如 `1-100`、`101-200`。

    返回：
        str | None: 可迁移时返回新目录名；无法识别或已经是目标格式时返回 None。

    说明：
        这里只接受 `数字-数字` 形式。其它目录名，例如 README 文件、隐藏目录、
        或者已经不是题号范围的目录，都会被忽略。
    """

    if "-" not in name:
        return None

    left, right = name.split("-", 1)
    if not (left.isdigit() and right.isdigit()):
        return None

    new_name = f"{int(left):04d}-{int(right):04d}"
    if new_name == name:
        return None
    return new_name


def iter_rename_plan(root: Path) -> list[tuple[Path, Path]]:
    """收集需要重命名的目录计划。

    参数：
        root: 仓库根目录。

    返回：
        list[tuple[Path, Path]]: 每一项是 `(旧路径, 新路径)`。
    """

    plan: list[tuple[Path, Path]] = []
    for difficulty in DIFFICULTY_DIRS:
        difficulty_dir = root / difficulty
        if not difficulty_dir.exists():
            continue
        for path in sorted(difficulty_dir.iterdir()):
            if not path.is_dir():
                continue
            new_name = fixed_width_bucket_name(path.name)
            if new_name is None:
                continue
            plan.append((path, difficulty_dir / new_name))
    return plan


def validate_plan(plan: list[tuple[Path, Path]]) -> None:
    """执行重命名前检查目标路径是否冲突。

    参数：
        plan: `iter_rename_plan()` 生成的重命名计划。

    抛出：
        SystemExit: 目标目录已存在时中止，避免覆盖用户已有文件。
    """

    for old_path, new_path in plan:
        if new_path.exists() and new_path != old_path:
            raise SystemExit(f"target already exists: {new_path}")


def run(root: Path, apply: bool) -> int:
    """打印或执行目录重命名计划。

    参数：
        root: 仓库根目录。
        apply: True 表示实际执行重命名；False 表示只打印计划。

    返回：
        int: 成功返回 0。
    """

    plan = iter_rename_plan(root)
    if not plan:
        print("No bucket directories need renaming.")
        return 0

    validate_plan(plan)
    for old_path, new_path in plan:
        print(f"{old_path.relative_to(root)} -> {new_path.relative_to(root)}")
        if apply:
            old_path.rename(new_path)

    if not apply:
        print("Dry run only. Re-run with --apply to rename directories.")
    return 0


def main() -> int:
    """命令行入口。"""

    args = parse_args()
    return run(args.root, args.apply)


if __name__ == "__main__":
    raise SystemExit(main())

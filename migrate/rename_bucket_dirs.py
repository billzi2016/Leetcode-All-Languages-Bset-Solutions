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
执行迁移。

如果目标固定宽度目录已经存在，脚本会把旧目录里的文件合并进去。默认遇到
同名文件会中止，避免覆盖已有内容；确认需要以新文件覆盖旧文件时，额外加
`--overwrite-files`。
"""

from __future__ import annotations

import argparse
from pathlib import Path


DIFFICULTY_DIRS = ("Leetcode-Easy", "Leetcode-Medium", "Leetcode-Hard")


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
    parser.add_argument(
        "--overwrite-files",
        action="store_true",
        help="Allow files in old buckets to replace files with the same name in target buckets.",
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


def iter_child_moves(old_path: Path, new_path: Path) -> list[tuple[Path, Path]]:
    """生成旧目录内容合并到目标目录的文件移动计划。

    参数：
        old_path: 旧分桶目录，例如 `Leetcode-Easy/1-100`。
        new_path: 新分桶目录，例如 `Leetcode-Easy/0001-0100`。

    返回：
        list[tuple[Path, Path]]: 每一项是 `(旧文件路径, 新文件路径)`。

    说明：
        当前题解分桶目录只应包含 Markdown 文件。这里仍按目录内容通用处理，
        便于归档迁移时保留其它随题解一起生成的普通文件。
    """

    return [(child, new_path / child.name) for child in sorted(old_path.iterdir())]


def validate_plan(plan: list[tuple[Path, Path]], overwrite_files: bool) -> None:
    """执行迁移前检查目标路径是否冲突。

    参数：
        plan: `iter_rename_plan()` 生成的重命名计划。
        overwrite_files: True 表示允许同名文件覆盖。

    抛出：
        SystemExit: 目标路径不是目录、或遇到未允许覆盖的同名文件时中止。
    """

    for old_path, new_path in plan:
        if not new_path.exists():
            continue
        if not new_path.is_dir():
            raise SystemExit(f"target exists and is not a directory: {new_path}")
        for _child, target_child in iter_child_moves(old_path, new_path):
            if target_child.exists() and not overwrite_files:
                raise SystemExit(f"target file already exists: {target_child}")


def apply_move(old_path: Path, new_path: Path, overwrite_files: bool) -> None:
    """执行一次旧分桶到固定宽度分桶的迁移。

    参数：
        old_path: 旧分桶目录。
        new_path: 目标固定宽度分桶目录。
        overwrite_files: True 表示允许覆盖目标目录中的同名文件。
    """

    if not new_path.exists():
        old_path.rename(new_path)
        return

    new_path.mkdir(parents=True, exist_ok=True)
    for child, target_child in iter_child_moves(old_path, new_path):
        if target_child.exists():
            if not overwrite_files:
                raise SystemExit(f"target file already exists: {target_child}")
            if target_child.is_dir():
                raise SystemExit(f"target child is a directory and cannot be overwritten: {target_child}")
            target_child.unlink()
        child.rename(target_child)
    old_path.rmdir()


def run(root: Path, apply: bool, overwrite_files: bool = False) -> int:
    """打印或执行目录迁移计划。

    参数：
        root: 仓库根目录。
        apply: True 表示实际执行迁移；False 表示只打印计划。
        overwrite_files: True 表示允许旧分桶中的文件覆盖目标同名文件。

    返回：
        int: 成功返回 0。
    """

    plan = iter_rename_plan(root)
    if not plan:
        print("No bucket directories need renaming.")
        return 0

    validate_plan(plan, overwrite_files)
    for old_path, new_path in plan:
        action = "merge" if new_path.exists() else "rename"
        print(f"{action}: {old_path.relative_to(root)} -> {new_path.relative_to(root)}")
        if apply:
            apply_move(old_path, new_path, overwrite_files)

    if not apply:
        print("Dry run only. Re-run with --apply to migrate directories.")
    return 0


def main() -> int:
    """命令行入口。"""

    args = parse_args()
    return run(args.root, args.apply, args.overwrite_files)


if __name__ == "__main__":
    raise SystemExit(main())

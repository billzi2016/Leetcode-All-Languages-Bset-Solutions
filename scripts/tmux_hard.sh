#!/usr/bin/env bash
# 在后台 tmux session 中只生成 Hard 难度题解。
#
# 用途：
#   - Hard 题通常耗时更长，生成器会每完成一种语言就写回 Markdown，
#     降低长任务中断造成的损失。
#   - 默认 session 名为 leetcode-hard，也可以通过第一个参数覆盖。
set -euo pipefail

SESSION_NAME="${1:-leetcode-hard}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

python -m pip install -r requirements.txt

# 只传入 --difficulty Hard；模型 think 强度由 Python 配置按难度选择。
tmux new-session -d -s "$SESSION_NAME" \
  "PYTHONPATH=src python scripts/generate_solutions.py --difficulty Hard"

echo "Started tmux session: $SESSION_NAME"
echo
echo "View sessions:"
echo "  tmux ls"
echo
echo "Attach:"
echo "  tmux attach -t $SESSION_NAME"
echo
echo
echo "Cancel:"
echo "  tmux kill-session -t $SESSION_NAME"
echo "Cancel all tmux sessions:"
echo "  tmux kill-server"

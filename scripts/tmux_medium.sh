#!/usr/bin/env bash
# 在后台 tmux session 中只生成 Medium 难度题解。
#
# 用途：
#   - Medium 题量更大，适合在 Easy 验证通过后单独长时间运行。
#   - 默认 session 名为 leetcode-medium，也可以通过第一个参数覆盖。
set -euo pipefail

SESSION_NAME="${1:-leetcode-medium}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

python -m pip install -r requirements.txt

# 只传入 --difficulty Medium，保持 shell 脚本薄封装，核心逻辑仍在 Python 中。
tmux new-session -d -s "$SESSION_NAME" \
  "PYTHONPATH=src python scripts/generate_solutions.py --difficulty Medium"

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

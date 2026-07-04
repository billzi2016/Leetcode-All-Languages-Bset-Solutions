#!/usr/bin/env bash
# 在后台 tmux session 中只生成 Easy 难度题解。
#
# 用途：
#   - 先跑 Easy 可以快速验证本地依赖、Ollama、日志和输出路径是否正常。
#   - 默认 session 名为 leetcode-easy，也可以通过第一个参数覆盖。
set -euo pipefail

SESSION_NAME="${1:-leetcode-easy}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

python -m pip install -r requirements.txt

# 只传入 --difficulty Easy，其它筛选和生成逻辑仍由 Python CLI 统一处理。
tmux new-session -d -s "$SESSION_NAME" \
  "PYTHONPATH=src python scripts/generate_solutions.py --difficulty Easy"

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

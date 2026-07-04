#!/usr/bin/env bash
# 在后台 tmux session 中启动完整题解生成流程。
#
# 用途：
#   - 适合长时间全量生成，避免终端断开导致进程退出。
#   - 默认 session 名为 leetcode-all，也可以通过第一个参数覆盖。
#   - 进入仓库根目录后先安装 requirements.txt，再执行生成脚本。
set -euo pipefail

# 第一个参数是可选 session 名；不传时使用稳定默认名，便于 attach/kill。
SESSION_NAME="${1:-leetcode-all}"
# 通过脚本所在位置反推仓库根目录，保证从任意工作目录调用都能正确执行。
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

# 生成脚本依赖 tqdm、ollama 等包；这里显式安装，降低长任务启动失败概率。
python -m pip install -r requirements.txt

# -d 表示后台启动；命令内部设置 PYTHONPATH=src，让未安装成本地包的源码可导入。
tmux new-session -d -s "$SESSION_NAME" \
  "PYTHONPATH=src python scripts/generate_solutions.py"

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

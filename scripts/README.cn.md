# 脚本说明

这个目录放的是题解生成流程的可执行入口。

## `generate_solutions.py`

题解生成主入口。

它会读取 `dataset/merged_problems.json`，按题号或难度选择题目，调用 `src/leetcode_solutions/` 里的生成逻辑，并把 Markdown 输出到 `easy/`、`medium/`、`hard/`。

示例：

```bash
PYTHONPATH=src python scripts/generate_solutions.py
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Easy
PYTHONPATH=src python scripts/generate_solutions.py --only-frontend-id 1
PYTHONPATH=src python scripts/generate_solutions.py --frontend-ids 1 2 4
```

这个脚本会调用 Ollama，也会写入或更新题解 Markdown 文件。

## `tmux_all.sh`

先用 `requirements.txt` 安装 Python 依赖，然后启动一个后台 tmux session 跑完整生成流程。

默认 session 名：`leetcode-all`

```bash
scripts/tmux_all.sh
scripts/tmux_all.sh my-session-name
```

## `tmux_easy.sh`

在后台 tmux session 里只生成 Easy 题目。

默认 session 名：`leetcode-easy`

```bash
scripts/tmux_easy.sh
```

## `tmux_medium.sh`

在后台 tmux session 里只生成 Medium 题目。

默认 session 名：`leetcode-medium`

```bash
scripts/tmux_medium.sh
```

## `tmux_hard.sh`

在后台 tmux session 里只生成 Hard 题目。

默认 session 名：`leetcode-hard`

```bash
scripts/tmux_hard.sh
```

## 常用 tmux 命令

这些命令也会在 tmux 脚本启动后打印出来：

```bash
tmux ls
tmux attach -t leetcode-all
tmux kill-session -t leetcode-all
tmux kill-server
```


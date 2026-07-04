# Scripts

This directory contains the runnable entry points for generating LeetCode solution Markdown files.

## `generate_solutions.py`

Main CLI entry point for solution generation.

It reads `dataset/merged_problems.json`, selects problems by id or difficulty, calls the generator in `src/leetcode_solutions/`, and writes Markdown output under `easy/`, `medium/`, and `hard/`.

Examples:

```bash
PYTHONPATH=src python scripts/generate_solutions.py
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Easy
PYTHONPATH=src python scripts/generate_solutions.py --only-frontend-id 1
PYTHONPATH=src python scripts/generate_solutions.py --frontend-ids 1 2 4
```

This script can call Ollama and write or update solution Markdown files.

## `tmux_all.sh`

Installs Python dependencies from `requirements.txt`, then starts a detached tmux session that runs the full generation flow.

Default session name: `leetcode-all`

```bash
scripts/tmux_all.sh
scripts/tmux_all.sh my-session-name
```

## `tmux_easy.sh`

Runs generation for Easy problems in a detached tmux session.

Default session name: `leetcode-easy`

```bash
scripts/tmux_easy.sh
```

## `tmux_medium.sh`

Runs generation for Medium problems in a detached tmux session.

Default session name: `leetcode-medium`

```bash
scripts/tmux_medium.sh
```

## `tmux_hard.sh`

Runs generation for Hard problems in a detached tmux session.

Default session name: `leetcode-hard`

```bash
scripts/tmux_hard.sh
```

## tmux commands

Useful commands printed by the tmux scripts:

```bash
tmux ls
tmux attach -t leetcode-all
tmux kill-session -t leetcode-all
tmux kill-server
```


# Validation

The `validate/` directory provides a containerized validation environment for generated LeetCode solution Markdown files.

It reads examples from `dataset/merged_problems.json`, extracts language code blocks from `Leetcode-Easy/`, `Leetcode-Medium/`, and `Leetcode-Hard/`, runs the supported executable sections, and writes CSV matrices by difficulty:

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

Each CSV row is a problem. Each language column uses `1` for passed sample cases and `0` for other outcomes.

## Docker

Build from the repository root:

```bash
docker build -f validate/Dockerfile -t leetcode-solutions-validate .
```

Run from the repository root:

```bash
docker run --rm -v "$PWD":/workspace leetcode-solutions-validate
```

## Direct Command

```bash
python validate/run_validation.py --repo-root .
python validate/run_validation.py --repo-root . --dataset dataset/merged_problems.json
python validate/run_validation.py --repo-root . --reports-dir validate/reports
```

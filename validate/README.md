# Containerized Solution Validation

`validate/` contains a reproducible validation environment for generated LeetCode solution Markdown files. It reads examples from `dataset/merged_problems.json`, extracts language sections from `Leetcode-Easy/`, `Leetcode-Medium/`, and `Leetcode-Hard/`, compiles or runs supported languages, and writes one CSV matrix per difficulty.

CSV output:

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

Each row is a problem. Each language column uses:

```text
1 = sample cases passed
0 = sample cases not passed
```

## Build

Run from the repository root:

```bash
docker build -f validate/Dockerfile -t leetcode-solutions-validate .
```

## Run

Run from the repository root:

```bash
docker run --rm -v "$PWD":/workspace leetcode-solutions-validate
```

The default command writes CSV files under `validate/reports/`.

## Options

```bash
python validate/run_validation.py --repo-root /workspace
python validate/run_validation.py --repo-root /workspace --dataset dataset/merged_problems.json
python validate/run_validation.py --repo-root /workspace --reports-dir validate/reports
```

The CSV keeps the language columns declared by the dataset. The bundled executable runners cover Python, Python3, Cpp, Java, and JavaScript sections for supported problem shapes parsed from the dataset examples.

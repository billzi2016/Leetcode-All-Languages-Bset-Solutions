# 题解验证

`validate/` 目录提供容器化题解验证环境，用于验证已经生成的 LeetCode 题解 Markdown 文件。

它从 `dataset/merged_problems.json` 读取 LeetCode 样例，从 `Leetcode-Easy/`、`Leetcode-Medium/`、`Leetcode-Hard/` 提取各语言代码块，运行支持的可执行语言 section，并按难度写出 CSV 矩阵：

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

每个 CSV 行是一道题。每个语言列使用 `1` 表示样例通过，使用 `0` 表示其它结果。

## Docker

在仓库根目录构建：

```bash
docker build -f validate/Dockerfile -t leetcode-solutions-validate .
```

在仓库根目录运行：

```bash
docker run --rm -v "$PWD":/workspace leetcode-solutions-validate
```

## 直接命令

```bash
python validate/run_validation.py --repo-root .
python validate/run_validation.py --repo-root . --dataset dataset/merged_problems.json
python validate/run_validation.py --repo-root . --reports-dir validate/reports
```

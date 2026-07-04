# 容器化题解验证

`validate/` 提供一个可复现的题解验证环境。它从 `dataset/merged_problems.json` 读取 LeetCode 样例，解析 `Leetcode-Easy/`、`Leetcode-Medium/`、`Leetcode-Hard/` 中已经生成的题解 Markdown，提取各语言代码块，按语言编译或运行，并按难度写出 CSV 矩阵。

CSV 输出：

```text
validate/reports/easy.csv
validate/reports/medium.csv
validate/reports/hard.csv
```

每一行是一道题。每个语言列只使用：

```text
1 = 样例通过
0 = 样例未通过
```

## 构建

在仓库根目录执行：

```bash
docker build -f validate/Dockerfile -t leetcode-solutions-validate .
```

## 运行

在仓库根目录执行：

```bash
docker run --rm -v "$PWD":/workspace leetcode-solutions-validate
```

默认输出到 `validate/reports/`。

## 参数

```bash
python validate/run_validation.py --repo-root /workspace
python validate/run_validation.py --repo-root /workspace --dataset dataset/merged_problems.json
python validate/run_validation.py --repo-root /workspace --reports-dir validate/reports
```

CSV 会保留 dataset 声明的语言列。内置可执行 runner 覆盖 Python、Python3、Cpp、Java 和 JavaScript，并支持从 dataset 样例解析出的题型。

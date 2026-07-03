# LeetCode Problems Dataset

本目录用于说明如何获取 LeetCode 题目合并数据文件。数据文件 `merged_problems.json` 不随本仓库提交，如需使用请自行下载到本目录。

- 本地数据文件：`merged_problems.json`
- 来源仓库：https://github.com/neenza/leetcode-problems/tree/master
- 原始文件：https://github.com/neenza/leetcode-problems/blob/master/merged_problems.json
- 直接下载地址：https://raw.githubusercontent.com/neenza/leetcode-problems/master/merged_problems.json

## 这个 JSON 是怎么来的

`merged_problems.json` 来自 `neenza/leetcode-problems` 仓库根目录。该上游仓库同时包含一个 `problems/` 目录和一个已经合并好的 `merged_problems.json` 文件。

本项目没有重新爬取或重新生成 LeetCode 数据。需要使用数据时，请从上游仓库下载已经整理好的合并 JSON 文件，用于后续读取、分析或转换为其他语言/格式的题目数据。

## 数据结构

`merged_problems.json` 顶层包含 `questions` 字段，里面是题目对象数组。每个题目 JSON 对象通常包含以下字段：

Some fields (like solutions, images, follow_ups) may be missing for certain problems.

- `title`: 题目名称，例如 `Container With Most Water`。
- `problem_id`: LeetCode 内部题目 ID，字符串格式。
- `frontend_id`: LeetCode 前端展示 ID，字符串格式。
- `difficulty`: 题目难度，通常是 `Easy`、`Medium` 或 `Hard`。
- `problem_slug`: URL 友好的题目名称，例如 `container-with-most-water`。
- `topics`: 题目标签数组，例如 `Array`、`Two Pointers`。
- `description`: 完整题目描述，通常是 Markdown 或文本格式。
- `examples`: 示例数组，每个示例对象通常包含：
  - `example_num`: 示例编号。
  - `example_text`: 输入、输出和解释文本。
  - `images`: 图片 URL 数组，如果该示例包含图片则会出现在这里；生成模型 prompt 时不使用该字段。
- `constraints`: 题目约束条件数组。
- `follow_ups`: follow-up 问题数组，如果没有则通常为空数组。
- `hints`: 解题提示数组。
- `code_snippets`: 多语言 starter code 对象，例如 `python`、`cpp`、`java` 等。
- `solution` / `solutions`: 部分题目包含的官方题解或 editorial 内容，通常是 HTML 字符串。

## 如何更新

如果需要使用该数据，或需要同步上游最新版，可以在本仓库根目录下载：

```bash
curl -L -o dataset/merged_problems.json https://raw.githubusercontent.com/neenza/leetcode-problems/master/merged_problems.json
```

更新后建议检查文件是否为合法 JSON，并根据需要记录上游仓库的 commit 或下载日期。

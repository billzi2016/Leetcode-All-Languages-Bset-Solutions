# LeetCode 是什么

LeetCode 是一个以算法和数据结构题目为核心的在线编程练习平台。每道题通常包含题名、难度、标签、题目描述、示例、约束、提示、starter code，有些题目还包含官方题解或 editorial 内容。

本项目使用本地合并 JSON 数据集来生成题解文件。数据集不提交到仓库，需要运行生成流程时由用户自行下载。

## 题目信息

常见字段包括：

- `title`: 题目名称。
- `frontend_id`: LeetCode 对外展示题号。
- `difficulty`: `Easy`、`Medium` 或 `Hard`。
- `problem_slug`: URL 友好的题目 slug。
- `topics`: 标签，例如 Array、Hash Table、Dynamic Programming、Two Pointers。
- `description`: 题目描述。
- `examples`: 输入输出示例。
- `constraints`: 输入规模和取值限制。
- `hints`: 可选提示。
- `solution` 或 `solutions`: 可选题解参考。
- `code_snippets`: 每种语言的 starter code。

生成器会把有用的文本字段放入题目 prompt。图片 URL 不会传入模型，因为当前生成链路只处理文本。

## 输出目标

输出不是题目描述副本。每个生成的 Markdown 文件只包含各语言题解代码块。


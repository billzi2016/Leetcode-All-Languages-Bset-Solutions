# LeetCode All Languages Best Solutions

本项目用于生成和整理 LeetCode 所有支持语言的准确最优解，并按难度、题号区间和题目 slug 输出为 Markdown 文件。

文档站点：

- https://billzi2016.github.io/Leetcode-All-Languages-Bset-Solutions/

## 支持语言

本项目覆盖 LeetCode 数据集中提供 starter code 的全部语言。下面的代码头示例来自 LeetCode 1 `Two Sum`。

| 语言 | 简介 | LeetCode 代码头示例 |
| --- | --- | --- |
| C | 适合底层数组和指针操作。 | `int* twoSum(int* nums, int numsSize, int target, int* returnSize)` |
| C++ | 适合使用 STL 容器和算法。 | `class Solution { public: vector<int> twoSum(vector<int>& nums, int target) }` |
| Java | 适合强类型面向对象实现。 | `class Solution { public int[] twoSum(int[] nums, int target) }` |
| Python | 适合简洁表达算法逻辑。 | `class Solution(object): def twoSum(self, nums, target)` |
| Python3 | 适合类型标注和现代 Python 写法。 | `class Solution: def twoSum(self, nums: List[int], target: int) -> List[int]` |
| C# | 适合 .NET 风格强类型实现。 | `public class Solution { public int[] TwoSum(int[] nums, int target) }` |
| JavaScript | 适合动态类型函数提交。 | `var twoSum = function(nums, target)` |
| TypeScript | 适合带类型约束的 JavaScript 写法。 | `function twoSum(nums: number[], target: number): number[]` |
| PHP | 适合类方法形式提交。 | `class Solution { function twoSum($nums, $target) }` |
| Swift | 适合 Apple 生态强类型实现。 | `class Solution { func twoSum(_ nums: [Int], _ target: Int) -> [Int] }` |
| Kotlin | 适合 JVM 上的现代强类型写法。 | `class Solution { fun twoSum(nums: IntArray, target: Int): IntArray }` |
| Dart | 适合 Dart 生态语法。 | `class Solution { List<int> twoSum(List<int> nums, int target) }` |
| Go | 适合简洁函数式提交。 | `func twoSum(nums []int, target int) []int` |
| Ruby | 适合脚本风格表达。 | `def two_sum(nums, target)` |
| Scala | 适合 JVM 上的函数式和面向对象混合写法。 | `object Solution { def twoSum(nums: Array[Int], target: Int): Array[Int] }` |
| Rust | 适合强安全约束和高性能实现。 | `impl Solution { pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> }` |
| Racket | 适合函数式表达和 contract 定义。 | `(define/contract (two-sum nums target) ...)` |
| Erlang | 适合函数式并发语言风格。 | `-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].` |
| Elixir | 适合函数式管道和模式匹配风格。 | `defmodule Solution do ... def two_sum(nums, target) do ... end` |

## 输出目录示例

```text
easy/
  1-100/
    0001-two-sum.md
    0009-palindrome-number.md
    0013-roman-to-integer.md
    0014-longest-common-prefix.md
    0020-valid-parentheses.md
    ...

medium/
  1-100/
    0002-add-two-numbers.md
    0003-longest-substring-without-repeating-characters.md
    0005-longest-palindromic-substring.md
    0006-zigzag-conversion.md
    0007-reverse-integer.md
    ...

hard/
  1-100/
    0004-median-of-two-sorted-arrays.md
    0010-regular-expression-matching.md
    0023-merge-k-sorted-lists.md
    0025-reverse-nodes-in-k-group.md
    0030-substring-with-concatenation-of-all-words.md
    ...
```

## 当前状态

当前已完成基础工程结构和核心流程：

- 数据集读取和按难度/题号筛选
- prompt 构造，并排除 `images` 字段
- Python `ollama` 库调用封装
- Easy / Medium / Hard 对应 think 模式：`low` / `medium` / `high`
- 单次语言生成 100k tokens 输出限制
- 温度固定为 `0.1`
- Markdown 输出路径和文件格式
- 断点续跑和已生成题目跳过
- stdout / stderr / failures 日志分流
- `unittest` 测试覆盖

## 数据集

本仓库不提交 `dataset/merged_problems.json`。如需运行生成流程，请先自行下载：

```bash
curl -L -o dataset/merged_problems.json https://raw.githubusercontent.com/neenza/leetcode-problems/master/merged_problems.json
```

数据字段说明见：

- `dataset/dataset.md`
- `dataset/dataset.cn.md`

## 安装依赖

```bash
python -m pip install -r requirements.txt
```

依赖包括：

- `ollama`
- `tqdm`

## 运行测试

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

测试包含 LeetCode 1 / 2 / 4 的正式流程测试，分别覆盖 Easy、Medium、Hard，并验证第二次运行能正常跳过已生成文件。

## 生成单题

生成 LeetCode 1：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --only-frontend-id 1
```

一次生成 LeetCode 1 / 2 / 4：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --frontend-ids 1 2 4
```

生成某个难度：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Easy
```

生成 Medium：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Medium
```

生成 Hard：

```bash
PYTHONPATH=src python scripts/generate_solutions.py --difficulty Hard
```

生成全部难度：

```bash
PYTHONPATH=src python scripts/generate_solutions.py
```

## 文档

- `docs/PRD.md`: 英文产品需求和实现约束
- `docs/PRD.cn.md`: 中文产品需求和实现约束
- `docs/PROJECT_STRUCTURE.md`: 英文项目结构、模块职责、SOLID/DRY 和测试规划
- `docs/PROJECT_STRUCTURE.cn.md`: 中文项目结构、模块职责、SOLID/DRY 和测试规划
- `dataset/dataset.md`: 英文数据集来源和字段说明
- `dataset/dataset.cn.md`: 中文数据集来源和字段说明

## Prompt 复用策略

prompt 分为三层，以最大化复用和缓存命中：

- `SYSTEM_PROMPT`: 所有题目、所有语言完全相同，包含全局生成要求和输出约束。
- `problem_prompt`: 同一道题的所有语言完全相同，包含题目元信息、描述、示例、约束、提示和可用题解参考。
- `language_prompt`: 只包含目标语言和该语言的 LeetCode starter code，是每次调用中变化最小的部分。

切换语言时只改变 `language_prompt`；切换题目时 `SYSTEM_PROMPT` 仍保持不变。这个结构对 prompt cache 最友好。

`language_prompt` 中的 LeetCode starter code 和函数头必须出现在最终输出中。生成结果必须保留对应语言的提交入口，例如 `class Solution`、`impl Solution`、`func twoSum(...)` 或 `def two_sum(...)`，确保代码可以直接提交到 LeetCode。

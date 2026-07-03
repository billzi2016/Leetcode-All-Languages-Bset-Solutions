# 支持语言

数据集中为多种 LeetCode 语言提供 starter code。生成器必须以 starter code 作为提交入口的来源。

## 语言特点

下面用 LeetCode 1 `Two Sum` 展示每种语言的提交入口。生成结果必须保留 starter code 中的入口形态，不能把 LeetCode 需要的类、函数、模块、contract 或 spec 改掉。

## 提交入口规则

| 语言 | 语言特点 | LeetCode 1 提交入口示例 |
| --- | --- | --- |
| C | 显式内存和指针管理，适合理解底层数组行为。 | `int* twoSum(int* nums, int numsSize, int target, int* returnSize)` |
| C++ | 基于 STL 和 `class Solution` 的算法实现。 | `class Solution { public: vector<int> twoSum(vector<int>& nums, int target) }` |
| Java | 强类型面向对象提交。 | `class Solution { public int[] twoSum(int[] nums, int target) }` |
| Python | 简洁表达算法逻辑。 | `class Solution(object): def twoSum(self, nums, target)` |
| Python3 | 简洁表达算法逻辑，常用类型标注。 | `class Solution: def twoSum(self, nums: List[int], target: int) -> List[int]` |
| C# | .NET 风格强类型题解。 | `public class Solution { public int[] TwoSum(int[] nums, int target) }` |
| JavaScript | 函数式提交。 | `var twoSum = function(nums, target)` |
| TypeScript | 函数式提交，并增加类型约束。 | `function twoSum(nums: number[], target: number): number[]` |
| PHP | 类方法提交。 | `class Solution { function twoSum($nums, $target) }` |
| Swift | Apple 生态强类型语法。 | `class Solution { func twoSum(_ nums: [Int], _ target: Int) -> [Int] }` |
| Kotlin | 简洁的 JVM 强类型语言。 | `class Solution { fun twoSum(nums: IntArray, target: Int): IntArray }` |
| Dart | Dart 语法下的类提交。 | `class Solution { List<int> twoSum(List<int> nums, int target) }` |
| Go | 简洁的函数式提交。 | `func twoSum(nums []int, target int) []int` |
| Ruby | 脚本风格方法。 | `def two_sum(nums, target)` |
| Scala | JVM 上的函数式和面向对象混合风格。 | `object Solution { def twoSum(nums: Array[Int], target: Int): Array[Int] }` |
| Rust | `impl Solution` 中的内存安全实现。 | `impl Solution { pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> }` |
| Racket | 带 contract 的函数式题解。 | `(define/contract (two-sum nums target) ...)` |
| Erlang | spec 和函数定义风格。 | `-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].` |
| Elixir | 模块化函数式风格。 | `defmodule Solution do ... def two_sum(nums, target) do ... end` |

这些入口必须出现在最终代码里，这样生成代码才能直接粘贴到 LeetCode。

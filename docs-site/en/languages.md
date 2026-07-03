# Supported Languages

The dataset exposes starter code for many LeetCode languages. The generator should use the starter code as the source of truth for the submission entry point.

## Language Characteristics

The table below uses LeetCode 1, `Two Sum`, to show each language's submission entry point. Generated output must preserve the starter code entry shape, including the required class, function, module, contract, or spec.

## Submission Entry Point Rule

| Language | Language Characteristic | LeetCode 1 Submission Entry Example |
| --- | --- | --- |
| C | Explicit memory and pointer management; useful for understanding low-level array behavior. | `int* twoSum(int* nums, int numsSize, int target, int* returnSize)` |
| C++ | STL-based algorithm implementations with `class Solution`. | `class Solution { public: vector<int> twoSum(vector<int>& nums, int target) }` |
| Java | Strongly typed object-oriented submissions. | `class Solution { public int[] twoSum(int[] nums, int target) }` |
| Python | Concise algorithm expression. | `class Solution(object): def twoSum(self, nums, target)` |
| Python3 | Concise algorithm expression with common type annotations. | `class Solution: def twoSum(self, nums: List[int], target: int) -> List[int]` |
| C# | .NET-style strongly typed solutions. | `public class Solution { public int[] TwoSum(int[] nums, int target) }` |
| JavaScript | Function-based submissions. | `var twoSum = function(nums, target)` |
| TypeScript | Function-based submissions with type constraints. | `function twoSum(nums: number[], target: number): number[]` |
| PHP | Class-method submissions. | `class Solution { function twoSum($nums, $target) }` |
| Swift | Strongly typed Apple ecosystem syntax. | `class Solution { func twoSum(_ nums: [Int], _ target: Int) -> [Int] }` |
| Kotlin | Concise strongly typed JVM language. | `class Solution { fun twoSum(nums: IntArray, target: Int): IntArray }` |
| Dart | Class-based submissions in Dart syntax. | `class Solution { List<int> twoSum(List<int> nums, int target) }` |
| Go | Compact function-based submissions. | `func twoSum(nums []int, target int) []int` |
| Ruby | Script-style methods. | `def two_sum(nums, target)` |
| Scala | Mixed functional and object-oriented JVM style. | `object Solution { def twoSum(nums: Array[Int], target: Int): Array[Int] }` |
| Rust | Memory-safe implementations inside `impl Solution`. | `impl Solution { pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> }` |
| Racket | Functional solutions with contracts. | `(define/contract (two-sum nums target) ...)` |
| Erlang | Function and spec style. | `-spec two_sum(Nums :: [integer()], Target :: integer()) -> [integer()].` |
| Elixir | Module-based functional style. | `defmodule Solution do ... def two_sum(nums, target) do ... end` |

These entry points must appear in the final code so the generated solution can be pasted directly into LeetCode.

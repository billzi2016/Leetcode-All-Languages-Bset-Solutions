# 支持语言

数据集中为多种 LeetCode 语言提供 starter code。生成器必须以 starter code 作为提交入口的来源。

## 语言特点

- C: 显式内存和指针管理，适合理解底层数组行为。
- C++: 基于 STL 和 `class Solution` 的算法实现。
- Java: 强类型面向对象提交。
- Python / Python3: 简洁表达算法逻辑，Python3 常用类型标注。
- C#: .NET 风格强类型题解。
- JavaScript / TypeScript: 函数式提交，TypeScript 增加类型约束。
- PHP: 类方法提交。
- Swift: Apple 生态强类型语法。
- Kotlin: 简洁的 JVM 强类型语言。
- Dart: Dart 语法下的类提交。
- Go: 简洁的函数式提交。
- Ruby: 脚本风格方法。
- Scala: JVM 上的函数式和面向对象混合风格。
- Rust: `impl Solution` 中的内存安全实现。
- Racket: 带 contract 的函数式题解。
- Erlang: spec 和函数定义风格。
- Elixir: 模块化函数式风格。

## 提交入口规则

最终输出必须保留 starter code 中的 LeetCode 提交入口，例如：

- `class Solution`
- `impl Solution`
- `func twoSum(...)`
- `def two_sum(...)`
- `defmodule Solution do`
- `define/contract`

这样生成代码才能直接粘贴到 LeetCode。


# Supported Languages

The dataset exposes starter code for many LeetCode languages. The generator should use the starter code as the source of truth for the submission entry point.

## Language Characteristics

- C: explicit memory and pointer management; useful for understanding low-level array behavior.
- C++: STL-based solutions with `class Solution`.
- Java: strongly typed object-oriented submissions.
- Python / Python3: concise implementations; Python3 commonly uses type annotations.
- C#: .NET-style strongly typed solutions.
- JavaScript / TypeScript: function-based submissions, with TypeScript adding type annotations.
- PHP: class-method submissions.
- Swift: strongly typed Apple ecosystem syntax.
- Kotlin: concise JVM language with strong type support.
- Dart: class-based submissions in Dart syntax.
- Go: compact function-based submissions.
- Ruby: concise script-style methods.
- Scala: JVM-based functional/object-oriented style.
- Rust: memory-safe implementations inside `impl Solution`.
- Racket: functional solutions with contracts.
- Erlang: function and spec style.
- Elixir: module-based functional style.

## Submission Entry Point Rule

The generated output must preserve the LeetCode submission entry point from the starter code. Examples include:

- `class Solution`
- `impl Solution`
- `func twoSum(...)`
- `def two_sum(...)`
- `defmodule Solution do`
- `define/contract`

This rule ensures the code can be pasted directly into LeetCode.


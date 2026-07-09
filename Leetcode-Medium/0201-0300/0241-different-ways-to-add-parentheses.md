# 0241. Different Ways to Add Parentheses

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        return compute(expression);
    }
private:
    unordered_map<string, vector<int>> memo;
    
    vector<int> compute(const string& expr) {
        if (memo.count(expr)) return memo[expr];
        vector<int> results;
        for (int i = 0; i < (int)expr.size(); ++i) {
            char op = expr[i];
            if (op == '+' || op == '-' || op == '*') {
                string left = expr.substr(0, i);
                string right = expr.substr(i + 1);
                vector<int> leftVals = compute(left);
                vector<int> rightVals = compute(right);
                for (int a : leftVals) {
                    for (int b : rightVals) {
                        int val = 0;
                        if (op == '+') val = a + b;
                        else if (op == '-') val = a - b;
                        else val = a * b;
                        results.push_back(val);
                    }
                }
            }
        }
        if (results.empty()) { // expr is a pure number
            results.push_back(stoi(expr));
        }
        memo[expr] = results;
        return results;
    }
};
```

## Java

```java
class Solution {
    private final java.util.Map<String, java.util.List<Integer>> memo = new java.util.HashMap<>();
    
    public java.util.List<Integer> diffWaysToCompute(String expression) {
        return compute(expression);
    }
    
    private java.util.List<Integer> compute(String expr) {
        if (memo.containsKey(expr)) {
            return memo.get(expr);
        }
        java.util.List<Integer> results = new java.util.ArrayList<>();
        for (int i = 0; i < expr.length(); i++) {
            char ch = expr.charAt(i);
            if (ch == '+' || ch == '-' || ch == '*') {
                String leftPart = expr.substring(0, i);
                String rightPart = expr.substring(i + 1);
                java.util.List<Integer> leftResults = compute(leftPart);
                java.util.List<Integer> rightResults = compute(rightPart);
                for (int l : leftResults) {
                    for (int r : rightResults) {
                        int val;
                        if (ch == '+') {
                            val = l + r;
                        } else if (ch == '-') {
                            val = l - r;
                        } else { // '*'
                            val = l * r;
                        }
                        results.add(val);
                    }
                }
            }
        }
        if (results.isEmpty()) {
            // expr is a pure number
            results.add(Integer.parseInt(expr));
        }
        memo.put(expr, results);
        return results;
    }
}
```

## Python

```python
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        from functools import lru_cache

        @lru_cache(None)
        def compute(expr):
            if expr.isdigit():
                return [int(expr)]
            results = []
            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left_vals = compute(expr[:i])
                    right_vals = compute(expr[i + 1:])
                    for l in left_vals:
                        for r in right_vals:
                            if ch == '+':
                                results.append(l + r)
                            elif ch == '-':
                                results.append(l - r)
                            else:  # '*'
                                results.append(l * r)
            return results

        return compute(expression)
```

## Python3

```python
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]
            results = []
            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left_vals = compute(expr[:i])
                    right_vals = compute(expr[i + 1:])
                    for l in left_vals:
                        for r in right_vals:
                            if ch == '+':
                                results.append(l + r)
                            elif ch == '-':
                                results.append(l - r)
                            else:  # '*'
                                results.append(l * r)
            if not results:
                results.append(int(expr))
            memo[expr] = results
            return results

        return compute(expression)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *vals;
    int size;
} Result;

static Result *memo[21][21];
static char *gExpr;

/* Helper to add a value to result list with dynamic resizing */
static void addValue(Result *res, int val) {
    if (res->size == 0) {
        res->vals = malloc(sizeof(int) * 4);
        res->vals[0] = val;
        res->size = 1;
        return;
    }
    // Ensure capacity
    int cap = 0;
    // Find current allocated capacity (approximate by size*2 until enough)
    // Simpler: reallocate each time (acceptable for small constraints)
    res->vals = realloc(res->vals, sizeof(int) * (res->size + 1));
    res->vals[res->size] = val;
    res->size++;
}

/* Recursive computation for substring [l, r] inclusive */
static Result* compute(int l, int r) {
    if (memo[l][r]) return memo[l][r];

    Result *cur = malloc(sizeof(Result));
    cur->vals = NULL;
    cur->size = 0;

    for (int i = l; i <= r; ++i) {
        char c = gExpr[i];
        if (c == '+' || c == '-' || c == '*') {
            Result *left = compute(l, i - 1);
            Result *right = compute(i + 1, r);
            for (int li = 0; li < left->size; ++li) {
                for (int ri = 0; ri < right->size; ++ri) {
                    int v;
                    if (c == '+') v = left->vals[li] + right->vals[ri];
                    else if (c == '-') v = left->vals[li] - right->vals[ri];
                    else v = left->vals[li] * right->vals[ri];
                    addValue(cur, v);
                }
            }
        }
    }

    /* If no operator found, it's a number */
    if (cur->size == 0) {
        int num = 0;
        for (int i = l; i <= r; ++i) {
            num = num * 10 + (gExpr[i] - '0');
        }
        cur->vals = malloc(sizeof(int));
        cur->vals[0] = num;
        cur->size = 1;
    }

    memo[l][r] = cur;
    return cur;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* diffWaysToCompute(char* expression, int* returnSize) {
    memset(memo, 0, sizeof(memo));
    gExpr = expression;
    int len = (int)strlen(expression);
    Result *res = compute(0, len - 1);
    *returnSize = res->size;
    return res->vals;   // caller will free this array
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private readonly Dictionary<string, IList<int>> _memo = new Dictionary<string, IList<int>>();

    public IList<int> DiffWaysToCompute(string expression)
    {
        return Compute(expression);
    }

    private IList<int> Compute(string expr)
    {
        if (_memo.TryGetValue(expr, out var cached))
            return cached;

        var results = new List<int>();
        for (int i = 0; i < expr.Length; i++)
        {
            char ch = expr[i];
            if (ch == '+' || ch == '-' || ch == '*')
            {
                var left = Compute(expr.Substring(0, i));
                var right = Compute(expr.Substring(i + 1));

                foreach (int l in left)
                {
                    foreach (int r in right)
                    {
                        int val = ch switch
                        {
                            '+' => l + r,
                            '-' => l - r,
                            '*' => l * r,
                            _ => 0
                        };
                        results.Add(val);
                    }
                }
            }
        }

        if (results.Count == 0) // expr is a pure number
        {
            results.Add(int.Parse(expr));
        }

        _memo[expr] = results;
        return results;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} expression
 * @return {number[]}
 */
var diffWaysToCompute = function (expression) {
  const memo = new Map();

  const compute = (expr) => {
    if (memo.has(expr)) return memo.get(expr);
    const results = [];

    for (let i = 0; i < expr.length; i++) {
      const ch = expr[i];
      if (ch === '+' || ch === '-' || ch === '*') {
        const leftVals = compute(expr.substring(0, i));
        const rightVals = compute(expr.substring(i + 1));
        for (const l of leftVals) {
          for (const r of rightVals) {
            let val;
            if (ch === '+') val = l + r;
            else if (ch === '-') val = l - r;
            else val = l * r;
            results.push(val);
          }
        }
      }
    }

    if (results.length === 0) {
      results.push(parseInt(expr, 10));
    }

    memo.set(expr, results);
    return results;
  };

  return compute(expression);
};
```

## Typescript

```typescript
function diffWaysToCompute(expression: string): number[] {
    const memo = new Map<string, number[]>();
    const compute = (expr: string): number[] => {
        if (memo.has(expr)) return memo.get(expr)!;
        const results: number[] = [];
        for (let i = 0; i < expr.length; i++) {
            const ch = expr[i];
            if (ch === '+' || ch === '-' || ch === '*') {
                const left = compute(expr.substring(0, i));
                const right = compute(expr.substring(i + 1));
                for (const l of left) {
                    for (const r of right) {
                        let val: number;
                        if (ch === '+') val = l + r;
                        else if (ch === '-') val = l - r;
                        else val = l * r;
                        results.push(val);
                    }
                }
            }
        }
        if (results.length === 0) {
            results.push(parseInt(expr));
        }
        memo.set(expr, results);
        return results;
    };
    return compute(expression);
}
```

## Php

```php
class Solution {
    /**
     * @param String $expression
     * @return Integer[]
     */
    function diffWaysToCompute($expression) {
        $this->memo = [];
        return $this->compute($expression);
    }
    
    private $memo;
    
    private function compute(string $expr): array {
        if (isset($this->memo[$expr])) {
            return $this->memo[$expr];
        }
        
        $len = strlen($expr);
        $results = [];
        
        for ($i = 0; $i < $len; $i++) {
            $ch = $expr[$i];
            if ($ch === '+' || $ch === '-' || $ch === '*') {
                $leftPart  = substr($expr, 0, $i);
                $rightPart = substr($expr, $i + 1);
                
                $leftResults  = $this->compute($leftPart);
                $rightResults = $this->compute($rightPart);
                
                foreach ($leftResults as $l) {
                    foreach ($rightResults as $r) {
                        switch ($ch) {
                            case '+':
                                $results[] = $l + $r;
                                break;
                            case '-':
                                $results[] = $l - $r;
                                break;
                            case '*':
                                $results[] = $l * $r;
                                break;
                        }
                    }
                }
            }
        }
        
        if (empty($results)) {
            // expr is a pure number
            $results[] = intval($expr);
        }
        
        $this->memo[$expr] = $results;
        return $results;
    }
}
```

## Swift

```swift
class Solution {
    func diffWaysToCompute(_ expression: String) -> [Int] {
        var memo = [String: [Int]]()
        
        func compute(_ expr: Substring) -> [Int] {
            let key = String(expr)
            if let cached = memo[key] {
                return cached
            }
            
            var results = [Int]()
            var hasOperator = false
            
            for (i, ch) in expr.enumerated() {
                if ch == "+" || ch == "-" || ch == "*" {
                    hasOperator = true
                    let leftPart = compute(expr.prefix(i))
                    let rightPart = compute(expr.suffix(expr.count - i - 1))
                    
                    for l in leftPart {
                        for r in rightPart {
                            switch ch {
                            case "+":
                                results.append(l + r)
                            case "-":
                                results.append(l - r)
                            default: // "*"
                                results.append(l * r)
                            }
                        }
                    }
                }
            }
            
            if !hasOperator, let value = Int(key) {
                results.append(value)
            }
            
            memo[key] = results
            return results
        }
        
        return compute(expression[...])
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val memo = HashMap<String, List<Int>>()
    
    fun diffWaysToCompute(expression: String): List<Int> {
        return compute(expression)
    }
    
    private fun compute(expr: String): List<Int> {
        memo[expr]?.let { return it }
        val results = mutableListOf<Int>()
        for (i in expr.indices) {
            when (val ch = expr[i]) {
                '+', '-', '*' -> {
                    val left = compute(expr.substring(0, i))
                    val right = compute(expr.substring(i + 1))
                    for (l in left) {
                        for (r in right) {
                            results.add(
                                when (ch) {
                                    '+' -> l + r
                                    '-' -> l - r
                                    else -> l * r
                                }
                            )
                        }
                    }
                }
            }
        }
        if (results.isEmpty()) {
            results.add(expr.toInt())
        }
        memo[expr] = results
        return results
    }
}
```

## Dart

```dart
class Solution {
  final Map<String, List<int>> _memo = {};

  List<int> diffWaysToCompute(String expression) {
    return _compute(expression);
  }

  List<int> _compute(String exp) {
    if (_memo.containsKey(exp)) {
      return _memo[exp]!;
    }
    List<int> results = [];
    for (int i = 0; i < exp.length; i++) {
      String ch = exp[i];
      if (ch == '+' || ch == '-' || ch == '*') {
        List<int> left = _compute(exp.substring(0, i));
        List<int> right = _compute(exp.substring(i + 1));
        for (int l in left) {
          for (int r in right) {
            int val;
            if (ch == '+') {
              val = l + r;
            } else if (ch == '-') {
              val = l - r;
            } else {
              val = l * r;
            }
            results.add(val);
          }
        }
      }
    }
    if (results.isEmpty) {
      results.add(int.parse(exp));
    }
    _memo[exp] = results;
    return results;
  }
}
```

## Golang

```go
package main

import (
	"strconv"
)

var memo map[string][]int

func diffWaysToCompute(expression string) []int {
	memo = make(map[string][]int)
	return compute(expression)
}

func compute(expr string) []int {
	if v, ok := memo[expr]; ok {
		return v
	}
	var res []int
	for i, ch := range expr {
		if ch == '+' || ch == '-' || ch == '*' {
			left := compute(expr[:i])
			right := compute(expr[i+1:])
			for _, l := range left {
				for _, r := range right {
					var val int
					switch ch {
					case '+':
						val = l + r
					case '-':
						val = l - r
					case '*':
						val = l * r
					}
					res = append(res, val)
				}
			}
		}
	}
	if len(res) == 0 {
		num, _ := strconv.Atoi(expr)
		res = []int{num}
	}
	memo[expr] = res
	return res
}
```

## Ruby

```ruby
def diff_ways_to_compute(expression)
  memo = {}
  compute(expression, memo)
end

def compute(expr, memo)
  return memo[expr] if memo.key?(expr)

  # If the expression is a pure number, return it as the sole result.
  if expr =~ /\A\d+\z/
    memo[expr] = [expr.to_i]
    return memo[expr]
  end

  results = []
  (0...expr.length).each do |i|
    op = expr[i]
    next unless op == '+' || op == '-' || op == '*'

    left_vals  = compute(expr[0...i], memo)
    right_vals = compute(expr[(i + 1)..-1], memo)

    left_vals.each do |l|
      right_vals.each do |r|
        case op
        when '+'
          results << l + r
        when '-'
          results << l - r
        when '*'
          results << l * r
        end
      end
    end
  end

  memo[expr] = results
end
```

## Scala

```scala
object Solution {
    def diffWaysToCompute(expression: String): List[Int] = {
        val n = expression.length
        val memo = Array.ofDim[Option[List[Int]]](n, n)

        def compute(l: Int, r: Int): List[Int] = {
            memo(l)(r) match {
                case Some(v) => v
                case None =>
                    var results = List.empty[Int]
                    var i = l
                    while (i <= r) {
                        val ch = expression.charAt(i)
                        if (ch == '+' || ch == '-' || ch == '*') {
                            val left = compute(l, i - 1)
                            val right = compute(i + 1, r)
                            for (a <- left; b <- right) {
                                val v = ch match {
                                    case '+' => a + b
                                    case '-' => a - b
                                    case '*' => a * b
                                }
                                results = v :: results
                            }
                        }
                        i += 1
                    }
                    if (results.isEmpty) {
                        val num = expression.substring(l, r + 1).toInt
                        results = List(num)
                    }
                    memo(l)(r) = Some(results)
                    results
            }
        }

        compute(0, n - 1)
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
        let mut memo = HashMap::new();
        Self::compute(&expression, &mut memo)
    }

    fn compute(s: &str, memo: &mut HashMap<String, Vec<i32>>) -> Vec<i32> {
        if let Some(v) = memo.get(s) {
            return v.clone();
        }
        // pure number case
        if !s.contains('+') && !s.contains('-') && !s.contains('*') {
            let val: i32 = s.parse().unwrap();
            let res = vec![val];
            memo.insert(s.to_string(), res.clone());
            return res;
        }

        let mut results = Vec::new();
        for (i, ch) in s.char_indices() {
            if ch == '+' || ch == '-' || ch == '*' {
                let left = Self::compute(&s[0..i], memo);
                let right = Self::compute(&s[i + 1..], memo);
                for &l in &left {
                    for &r in &right {
                        let v = match ch {
                            '+' => l + r,
                            '-' => l - r,
                            '*' => l * r,
                            _ => unreachable!(),
                        };
                        results.push(v);
                    }
                }
            }
        }

        memo.insert(s.to_string(), results.clone());
        results
    }
}
```

## Racket

```racket
(define/contract (diff-ways-to-compute expression)
  (-> string? (listof exact-integer?))
  (let* ((len (string-length expression))
         (memo (make-hash)))
    (define (key s e) (cons s e))
    (letrec ((compute
              (lambda (s e)
                (define k (key s e))
                (if (hash-has-key? memo k)
                    (hash-ref memo k)
                    (begin
                      (define results '())
                      (define has-op #f)
                      (for ([i (in-range s (+ e 1))])
                        (define ch (string-ref expression i))
                        (when (or (char=? ch #\+) (char=? ch #\-) (char=? ch #\*))
                          (set! has-op #t)
                          (let ((left (compute s (- i 1)))
                                (right (compute (+ i 1) e)))
                            (for ([lv left])
                              (for ([rv right])
                                (define val
                                  (cond [(char=? ch #\+) (+ lv rv)]
                                        [(char=? ch #\-) (- lv rv)]
                                        [else (* lv rv)]))
                                (set! results (cons val results)))))))
                      (unless has-op
                        (let* ((sub (substring expression s (+ e 1)))
                               (num (string->number sub)))
                          (set! results (list num))))
                      (hash-set! memo k results)
                      results)))))
      (compute 0 (- len 1)))))
```

## Erlang

```erlang
-module(solution).
-export([diff_ways_to_compute/1]).

-spec diff_ways_to_compute(Expression :: unicode:unicode_binary()) -> [integer()].
diff_ways_to_compute(Expression) ->
    ExprList = binary_to_list(Expression),
    compute_range(ExprList, 0, length(ExprList) - 1).

compute_range(_List, Start, End) when Start > End ->
    [];
compute_range(List, Start, End) ->
    Sub = lists:sublist(List, Start + 1, End - Start + 1),
    case contains_operator(Sub) of
        false -> [list_to_integer(Sub)];
        true  -> results_from_ops(List, Start, End)
    end.

contains_operator([]) -> false;
contains_operator([C|Rest]) when C == $+; C == $-; C == $* -> true;
contains_operator([_|Rest]) -> contains_operator(Rest).

results_from_ops(List, Start, End) ->
    results_from_ops(List, Start, End, Start, []).

results_from_ops(_List, _Start, End, I, Acc) when I > End ->
    Acc;
results_from_ops(List, Start, End, I, Acc) ->
    Char = lists:nth(I + 1, List),
    case Char of
        $+; $-; $* ->
            Left = compute_range(List, Start, I - 1),
            Right = compute_range(List, I + 1, End),
            Combined = combine(Left, Right, Char),
            results_from_ops(List, Start, End, I + 1, Acc ++ Combined);
        _ ->
            results_from_ops(List, Start, End, I + 1, Acc)
    end.

combine(L, R, Op) ->
    [apply_op(A, B, Op) || A <- L, B <- R].

apply_op(A, B, $+) -> A + B;
apply_op(A, B, $-) -> A - B;
apply_op(A, B, $*) -> A * B.
```

## Elixir

```elixir
defmodule Solution do
  @spec diff_ways_to_compute(String.t()) :: [integer]
  def diff_ways_to_compute(expression) do
    n = String.length(expression)
    {result, _} = compute(expression, 0, n - 1, %{})
    result
  end

  defp compute(_expr, i, j, memo) when i > j, do: {[], memo}

  defp compute(expr, i, j, memo) do
    key = {i, j}
    case Map.fetch(memo, key) do
      {:ok, val} ->
        {val, memo}

      :error ->
        sub = String.slice(expr, i..j)

        if not String.contains?(sub, ["+", "-", "*"]) do
          num = String.to_integer(sub)
          new_memo = Map.put(memo, key, [num])
          {[num], new_memo}
        else
          {results, memo2} =
            Enum.reduce(i..j, {[], memo}, fn idx, {acc, mem} ->
              case String.at(expr, idx) do
                "+" -> combine(expr, i, j, idx, &Kernel.+/2, acc, mem)
                "-" -> combine(expr, i, j, idx, &Kernel.-/2, acc, mem)
                "*" -> combine(expr, i, j, idx, &Kernel.*/2, acc, mem)
                _ -> {acc, mem}
              end
            end)

          memo_final = Map.put(memo2, key, results)
          {results, memo_final}
        end
    end
  end

  defp combine(expr, i, j, idx, op_fun, acc, memo) do
    {left_vals, memo1} = compute(expr, i, idx - 1, memo)
    {right_vals, memo2} = compute(expr, idx + 1, j, memo1)

    combined =
      for l <- left_vals, r <- right_vals, do: op_fun.(l, r)

    {acc ++ combined, memo2}
  end
end
```

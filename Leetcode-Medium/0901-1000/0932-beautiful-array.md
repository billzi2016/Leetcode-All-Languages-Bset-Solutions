# 0932. Beautiful Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> beautifulArray(int n) {
        static unordered_map<int, vector<int>> memo;
        if (memo.count(n)) return memo[n];
        if (n == 1) return memo[1] = {1};
        vector<int> left = beautifulArray((n + 1) / 2);
        vector<int> right = beautifulArray(n / 2);
        vector<int> res;
        res.reserve(n);
        for (int x : left) res.push_back(2 * x - 1);   // odd numbers
        for (int x : right) res.push_back(2 * x);      // even numbers
        return memo[n] = move(res);
    }
};
```

## Java

```java
class Solution {
    public int[] beautifulArray(int n) {
        List<Integer> list = construct(n);
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = list.get(i);
        }
        return result;
    }

    private List<Integer> construct(int n) {
        if (n == 1) {
            List<Integer> base = new ArrayList<>(1);
            base.add(1);
            return base;
        }
        List<Integer> oddPart = construct((n + 1) / 2);
        List<Integer> evenPart = construct(n / 2);
        List<Integer> res = new ArrayList<>(n);
        for (int x : oddPart) {
            res.add(2 * x - 1);
        }
        for (int x : evenPart) {
            res.add(2 * x);
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        memo = {1: [1]}

        def helper(k):
            if k in memo:
                return memo[k]
            odds = helper((k + 1) // 2)
            evens = helper(k // 2)
            res = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            memo[k] = res
            return res

        return helper(n)
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        @lru_cache(None)
        def helper(k: int):
            if k == 1:
                return (1,)
            odds = [2 * x - 1 for x in helper((k + 1) // 2)]
            evens = [2 * x for x in helper(k // 2)]
            return tuple(odds + evens)
        return list(helper(n))
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* beautifulArray(int n, int* returnSize) {
    // Start with the base beautiful array [1]
    int curCap = 1;
    int *cur = (int*)malloc(sizeof(int));
    cur[0] = 1;

    while (curCap < n) {
        // The next array can be at most twice as large
        int *next = (int*)malloc(sizeof(int) * curCap * 2);
        int idx = 0;
        // First generate odd numbers: 2*x - 1
        for (int i = 0; i < curCap; ++i) {
            int val = 2 * cur[i] - 1;
            if (val <= n) {
                next[idx++] = val;
            }
        }
        // Then generate even numbers: 2*x
        for (int i = 0; i < curCap; ++i) {
            int val = 2 * cur[i];
            if (val <= n) {
                next[idx++] = val;
            }
        }
        free(cur);
        cur = next;
        curCap = idx;
    }

    // Copy the result into the array to be returned
    int *res = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) {
        res[i] = cur[i];
    }
    free(cur);

    *returnSize = n;
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    private readonly Dictionary<int, List<int>> _memo = new Dictionary<int, List<int>>();

    public int[] BeautifulArray(int n) {
        return Build(n).ToArray();
    }

    private List<int> Build(int n) {
        if (n == 1) return new List<int> { 1 };
        if (_memo.TryGetValue(n, out var cached)) return cached;

        var result = new List<int>();
        foreach (var x in Build((n + 1) / 2))
            result.Add(2 * x - 1);
        foreach (var x in Build(n / 2))
            result.Add(2 * x);

        _memo[n] = result;
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var beautifulArray = function(n) {
    const memo = new Map();
    const build = (len) => {
        if (memo.has(len)) return memo.get(len);
        let result;
        if (len === 1) {
            result = [1];
        } else {
            const odd = build((len + 1) >> 1).map(x => 2 * x - 1);
            const even = build(len >> 1).map(x => 2 * x);
            result = odd.concat(even);
        }
        memo.set(len, result);
        return result;
    };
    return build(n);
};
```

## Typescript

```typescript
function beautifulArray(n: number): number[] {
    const memo = new Map<number, number[]>();

    const build = (len: number): number[] => {
        if (memo.has(len)) return memo.get(len)!;
        let result: number[];
        if (len === 1) {
            result = [1];
        } else {
            const odds = build(Math.ceil(len / 2)).map(x => 2 * x - 1);
            const evens = build(Math.floor(len / 2)).map(x => 2 * x);
            result = odds.concat(evens);
        }
        memo.set(len, result);
        return result;
    };

    return build(n);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function beautifulArray($n) {
        $memo = [];

        $build = function ($len) use (&$build, &$memo) {
            if (isset($memo[$len])) {
                return $memo[$len];
            }
            if ($len == 1) {
                $res = [1];
            } else {
                $oddPart  = $build(intdiv($len + 1, 2));
                $evenPart = $build(intdiv($len, 2));

                $res = [];
                foreach ($oddPart as $v) {
                    $res[] = $v * 2 - 1; // map to odd numbers
                }
                foreach ($evenPart as $v) {
                    $res[] = $v * 2;     // map to even numbers
                }
            }
            $memo[$len] = $res;
            return $res;
        };

        return $build($n);
    }
}
```

## Swift

```swift
class Solution {
    func beautifulArray(_ n: Int) -> [Int] {
        var memo = [Int: [Int]]()
        
        func build(_ size: Int) -> [Int] {
            if let cached = memo[size] {
                return cached
            }
            var result: [Int]
            if size == 1 {
                result = [1]
            } else {
                let odds = build((size + 1) / 2).map { $0 * 2 - 1 }
                let evens = build(size / 2).map { $0 * 2 }
                result = odds + evens
            }
            memo[size] = result
            return result
        }
        
        return build(n)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val memo = HashMap<Int, IntArray>()
    
    fun beautifulArray(n: Int): IntArray {
        return build(n)
    }
    
    private fun build(n: Int): IntArray {
        memo[n]?.let { return it }
        if (n == 1) {
            val arr = intArrayOf(1)
            memo[1] = arr
            return arr
        }
        val left = build((n + 1) / 2).map { it * 2 - 1 }.toIntArray()
        val right = build(n / 2).map { it * 2 }.toIntArray()
        val result = IntArray(n)
        System.arraycopy(left, 0, result, 0, left.size)
        System.arraycopy(right, 0, result, left.size, right.size)
        memo[n] = result
        return result
    }
}
```

## Dart

```dart
class Solution {
  final Map<int, List<int>> _memo = {};

  List<int> beautifulArray(int n) {
    return _build(n);
  }

  List<int> _build(int n) {
    if (_memo.containsKey(n)) return _memo[n]!;
    List<int> result;
    if (n == 1) {
      result = [1];
    } else {
      var odd = _build((n + 1) ~/ 2).map((x) => 2 * x - 1);
      var even = _build(n ~/ 2).map((x) => 2 * x);
      result = [...odd, ...even];
    }
    _memo[n] = result;
    return result;
  }
}
```

## Golang

```go
var cache = map[int][]int{
	1: {1},
}

func build(n int) []int {
	if v, ok := cache[n]; ok {
		return v
	}
	odd := build((n + 1) / 2)
	even := build(n / 2)

	res := make([]int, 0, n)
	for _, x := range odd {
		res = append(res, 2*x-1)
	}
	for _, x := range even {
		res = append(res, 2*x)
	}
	cache[n] = res
	return res
}

func beautifulArray(n int) []int {
	return build(n)
}
```

## Ruby

```ruby
def beautiful_array(n)
  @cache ||= {}
  return @cache[n] if @cache.key?(n)

  res = if n == 1
    [1]
  else
    left = beautiful_array((n + 1) / 2).map { |x| 2 * x - 1 }
    right = beautiful_array(n / 2).map { |x| 2 * x }
    left + right
  end

  @cache[n] = res
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  private val memo = mutable.Map[Int, Array[Int]]()

  def beautifulArray(n: Int): Array[Int] = {
    def helper(k: Int): Array[Int] = {
      memo.getOrElseUpdate(k, {
        if (k == 1) Array(1)
        else {
          val odds = helper((k + 1) / 2).map(x => 2 * x - 1)
          val evens = helper(k / 2).map(x => 2 * x)
          odds ++ evens
        }
      })
    }
    helper(n)
  }
}
```

## Rust

```rust
use std::collections::HashMap;

fn helper(n: i32, memo: &mut HashMap<i32, Vec<i32>>) -> Vec<i32> {
    if let Some(v) = memo.get(&n) {
        return v.clone();
    }
    let mut res = Vec::new();
    if n == 1 {
        res.push(1);
    } else {
        // odd part
        for x in helper((n + 1) / 2, memo) {
            res.push(2 * x - 1);
        }
        // even part
        for x in helper(n / 2, memo) {
            res.push(2 * x);
        }
    }
    memo.insert(n, res.clone());
    res
}

impl Solution {
    pub fn beautiful_array(n: i32) -> Vec<i32> {
        let mut memo = HashMap::new();
        helper(n, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (beautiful-array n)
  (-> exact-integer? (listof exact-integer?))
  (letrec ((helper
            (lambda (m)
              (cond [(= m 1) '(1)]
                    [else
                     (let* ([odd-count (quotient (+ m 1) 2)]
                            [even-count (quotient m 2)]
                            [odd-list (map (lambda (x) (- (* 2 x) 1))
                                           (helper odd-count))]
                            [even-list (map (lambda (x) (* 2 x))
                                            (helper even-count))])
                       (append odd-list even-list))]))))
    (helper n)))
```

## Erlang

```erlang
-module(solution).
-export([beautiful_array/1]).

-spec beautiful_array(N :: integer()) -> [integer()].
beautiful_array(N) ->
    build(N).

%% Recursive construction of beautiful array
-spec build(integer()) -> [integer()].
build(1) ->
    [1];
build(N) when N > 1 ->
    OddsCount = (N + 1) div 2,
    EvensCount = N div 2,
    OddPart = build(OddsCount),
    EvenPart = build(EvensCount),
    lists:map(fun(X) -> 2 * X - 1 end, OddPart) ++
        lists:map(fun(X) -> 2 * X end, EvenPart).
```

## Elixir

```elixir
defmodule Solution do
  @spec beautiful_array(n :: integer) :: [integer]
  def beautiful_array(n) do
    build(n)
  end

  defp build(1), do: [1]

  defp build(n) do
    odds = build(div(n + 1, 2)) |> Enum.map(fn x -> x * 2 - 1 end)
    evens = build(div(n, 2)) |> Enum.map(fn x -> x * 2 end)
    odds ++ evens
  end
end
```

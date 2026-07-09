# 1553. Minimum Number of Days to Eat N Oranges

## Cpp

```cpp
class Solution {
public:
    int minDays(int n) {
        unordered_map<long long,int> dp;
        function<int(long long)> dfs = [&](long long x)->int{
            if (x <= 1) return (int)x;
            auto it = dp.find(x);
            if (it != dp.end()) return it->second;
            int res = 1 + min( (int)(x % 2) + dfs(x / 2),
                               (int)(x % 3) + dfs(x / 3) );
            dp[x] = res;
            return res;
        };
        return dfs(n);
    }
};
```

## Java

```java
class Solution {
    private final java.util.Map<Integer, Integer> memo = new java.util.HashMap<>();
    
    public int minDays(int n) {
        return dfs(n);
    }
    
    private int dfs(int n) {
        if (n <= 1) return n;
        Integer cached = memo.get(n);
        if (cached != null) return cached;
        int option2 = n % 2 + dfs(n / 2);
        int option3 = n % 3 + dfs(n / 3);
        int res = Math.min(option2, option3) + 1;
        memo.put(n, res);
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        from functools import lru_cache

        @lru_cache(None)
        def dfs(x):
            if x <= 1:
                return x
            # Make x divisible by 2 or 3 by eating the remainder,
            # then perform the division operation (counted as one day).
            return 1 + min(x % 2 + dfs(x // 2), x % 3 + dfs(x // 3))

        return dfs(n)
```

## Python3

```python
class Solution:
    def minDays(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(x: int) -> int:
            if x <= 1:
                return x
            # make divisible by 2 or 3 by eating the remainder directly,
            # then perform the optimal operation.
            take2 = x % 2 + dfs(x // 2)
            take3 = x % 3 + dfs(x // 3)
            return 1 + (take2 if take2 < take3 else take3)

        return dfs(n)
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int minDays(int n) {
    unordered_map<int, int> memo;
    function<int(int)> dfs = [&](int x) -> int {
        if (x <= 1) return x;
        auto it = memo.find(x);
        if (it != memo.end()) return it->second;
        int res = 1 + min(x % 2 + dfs(x / 2), x % 3 + dfs(x / 3));
        memo[x] = res;
        return res;
    };
    return dfs(n);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private readonly Dictionary<long, int> _memo = new Dictionary<long, int>();

    public int MinDays(int n)
    {
        return Dfs(n);
    }

    private int Dfs(long n)
    {
        if (n <= 1) return (int)n;
        if (_memo.TryGetValue(n, out var cached)) return cached;

        long r2 = n % 2;
        long r3 = n % 3;

        int daysVia2 = (int)(r2 + 1 + Dfs(n / 2));
        int daysVia3 = (int)(r3 + 1 + Dfs(n / 3));

        int result = Math.Min(daysVia2, daysVia3);
        _memo[n] = result;
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minDays = function(n) {
    const memo = new Map();
    const dfs = (x) => {
        if (x <= 1) return x;
        if (memo.has(x)) return memo.get(x);
        const daysVia2 = (x % 2) + 1 + dfs(Math.floor(x / 2));
        const daysVia3 = (x % 3) + 1 + dfs(Math.floor(x / 3));
        const ans = Math.min(daysVia2, daysVia3);
        memo.set(x, ans);
        return ans;
    };
    return dfs(n);
};
```

## Typescript

```typescript
function minDays(n: number): number {
    const memo = new Map<number, number>();
    function dfs(x: number): number {
        if (x <= 1) return x;
        if (memo.has(x)) return memo.get(x)!;
        const daysVia2 = (x % 2) + dfs(Math.floor(x / 2));
        const daysVia3 = (x % 3) + dfs(Math.floor(x / 3));
        const res = 1 + Math.min(daysVia2, daysVia3);
        memo.set(x, res);
        return res;
    }
    return dfs(n);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    private $memo = [];

    public function minDays($n) {
        return $this->dfs($n);
    }

    private function dfs(int $n): int {
        if ($n <= 1) {
            return $n;
        }
        if (isset($this->memo[$n])) {
            return $this->memo[$n];
        }

        // Make n divisible by 2
        $rem2 = $n % 2;
        $daysVia2 = $rem2 + 1 + $this->dfs(intdiv($n, 2));

        // Make n divisible by 3
        $rem3 = $n % 3;
        $daysVia3 = $rem3 + 1 + $this->dfs(intdiv($n, 3));

        $res = min($daysVia2, $daysVia3);
        $this->memo[$n] = $res;
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    private var memo = [Int:Int]()
    
    func minDays(_ n: Int) -> Int {
        return dfs(n)
    }
    
    private func dfs(_ n: Int) -> Int {
        if n <= 1 { return n }
        if let cached = memo[n] { return cached }
        
        let option2 = n % 2 + dfs(n / 2)
        let option3 = n % 3 + dfs(n / 3)
        let result = 1 + min(option2, option3)
        memo[n] = result
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val memo = HashMap<Long, Int>()
    
    fun minDays(n: Int): Int {
        return dfs(n.toLong())
    }
    
    private fun dfs(x: Long): Int {
        if (x <= 1L) return x.toInt()
        memo[x]?.let { return it }
        val opt2 = (x % 2).toInt() + dfs(x / 2)
        val opt3 = (x % 3).toInt() + dfs(x / 3)
        val res = 1 + kotlin.math.min(opt2, opt3)
        memo[x] = res
        return res
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  final Map<int, int> _memo = {};

  int minDays(int n) {
    return _dfs(n);
  }

  int _dfs(int n) {
    if (n <= 1) return n;
    if (_memo.containsKey(n)) return _memo[n]!;
    int option2 = n % 2 + 1 + _dfs(n ~/ 2);
    int option3 = n % 3 + 1 + _dfs(n ~/ 3);
    int res = min(option2, option3);
    _memo[n] = res;
    return res;
  }
}
```

## Golang

```go
func minDays(n int) int {
    memo := make(map[int]int)

    var dfs func(int) int
    dfs = func(k int) int {
        if k <= 1 {
            return k
        }
        if v, ok := memo[k]; ok {
            return v
        }
        // option: reduce to nearest multiple of 2 then divide, or to nearest multiple of 3 then divide
        opt2 := k%2 + dfs(k/2)
        opt3 := k%3 + dfs(k/3)
        if opt2 < opt3 {
            memo[k] = 1 + opt2
        } else {
            memo[k] = 1 + opt3
        }
        return memo[k]
    }

    return dfs(n)
}
```

## Ruby

```ruby
def min_days(n)
  @memo ||= {}
  return n if n <= 1
  return @memo[n] if @memo.key?(n)

  opt2 = n % 2 + min_days(n / 2)
  opt3 = n % 3 + min_days(n / 3)

  @memo[n] = 1 + (opt2 < opt3 ? opt2 : opt3)
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  def minDays(n: Int): Int = {
    val memo = mutable.HashMap[Long, Int]()

    def dfs(x: Long): Int = {
      if (x <= 1) return x.toInt
      memo.getOrElseUpdate(x, {
        val opt2 = (x % 2).toInt + 1 + dfs(x / 2)
        val opt3 = (x % 3).toInt + 1 + dfs(x / 3)
        Math.min(opt2, opt3)
      })
    }

    dfs(n.toLong)
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn min_days(n: i32) -> i32 {
        fn dfs(x: i64, memo: &mut HashMap<i64, i32>) -> i32 {
            if x <= 1 {
                return x as i32;
            }
            if let Some(&v) = memo.get(&x) {
                return v;
            }
            let take2 = (x % 2) as i32 + dfs(x / 2, memo);
            let take3 = (x % 3) as i32 + dfs(x / 3, memo);
            let res = 1 + std::cmp::min(take2, take3);
            memo.insert(x, res);
            res
        }
        let mut memo = HashMap::new();
        dfs(n as i64, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (min-days n)
  (-> exact-integer? exact-integer?)
  (let ([memo (make-hash)])
    (define (dfs k)
      (cond [(<= k 1) k]
            [else
             (let ([cached (hash-ref memo k #f)])
               (if cached
                   cached
                   (let* ([opt1 (+ (remainder k 2) (dfs (quotient k 2)))]
                          [opt2 (+ (remainder k 3) (dfs (quotient k 3)))])
                     (define res (+ 1 (min opt1 opt2)))
                     (hash-set! memo k res)
                     res))))]))
    (dfs n)))
```

## Erlang

```erlang
-module(solution).
-export([min_days/1]).

-spec min_days(integer()) -> integer().
min_days(N) ->
    {Ans, _} = min_days(N, #{}),
    Ans.

%% internal recursive function with memoization
-spec min_days(integer(), map()) -> {integer(), map()}.
min_days(0, Memo) -> {0, Memo};
min_days(1, Memo) -> {1, Memo};
min_days(N, Memo) when N > 1 ->
    case maps:get(N, Memo, undefined) of
        Value when is_integer(Value) ->
            {Value, Memo};
        undefined ->
            R2 = N rem 2,
            {D2, Memo1} = min_days(N div 2, Memo),
            Days2 = R2 + D2,
            R3 = N rem 3,
            {D3, Memo2} = min_days(N div 3, Memo1),
            Days3 = R3 + D3,
            MinDays = 1 + erlang:min(Days2, Days3),
            NewMemo = maps:put(N, MinDays, Memo2),
            {MinDays, NewMemo}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_days(n :: integer) :: integer
  def min_days(n) do
    {result, _} = dfs(n, %{})
    result
  end

  defp dfs(0, memo), do: {0, Map.put(memo, 0, 0)}
  defp dfs(1, memo), do: {1, Map.put(memo, 1, 1)}

  defp dfs(n, memo) do
    case Map.fetch(memo, n) do
      {:ok, val} ->
        {val, memo}

      :error ->
        {days2, memo2} = dfs(div(n, 2), memo)
        {days3, memo3} = dfs(div(n, 3), memo2)

        opt2 = rem(n, 2) + days2
        opt3 = rem(n, 3) + days3

        res = 1 + min(opt2, opt3)
        {res, Map.put(memo3, n, res)}
    end
  end
end
```

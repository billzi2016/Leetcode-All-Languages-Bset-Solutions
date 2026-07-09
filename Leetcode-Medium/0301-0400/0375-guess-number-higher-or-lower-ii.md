# 0375. Guess Number Higher or Lower II

## Cpp

```cpp
class Solution {
public:
    int getMoneyAmount(int n) {
        if (n <= 1) return 0;
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        for (int len = 2; len <= n; ++len) {
            for (int i = 1; i + len - 1 <= n; ++i) {
                int j = i + len - 1;
                int best = INT_MAX;
                for (int k = i; k <= j; ++k) {
                    int left = (k > i) ? dp[i][k - 1] : 0;
                    int right = (k < j) ? dp[k + 1][j] : 0;
                    int cost = k + max(left, right);
                    if (cost < best) best = cost;
                }
                dp[i][j] = best;
            }
        }
        return dp[1][n];
    }
};
```

## Java

```java
class Solution {
    public int getMoneyAmount(int n) {
        int[][] dp = new int[n + 2][n + 2];
        // dp[i][j] = 0 when i >= j (already zero-initialized)
        for (int len = 2; len <= n; len++) {
            for (int i = 1; i + len - 1 <= n; i++) {
                int j = i + len - 1;
                int best = Integer.MAX_VALUE;
                for (int k = i; k <= j; k++) {
                    int cost = k + Math.max(dp[i][k - 1], dp[k + 1][j]);
                    if (cost < best) {
                        best = cost;
                    }
                }
                dp[i][j] = best;
            }
        }
        return dp[1][n];
    }
}
```

## Python

```python
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        # dp[i][j] = minimum amount to guarantee a win in range [i, j]
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                best = float('inf')
                # try all possible pivots k in [i, j-1]; choosing j yields cost=j (right empty)
                for k in range(i, j):
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    if cost < best:
                        best = cost
                dp[i][j] = best
        return dp[1][n]
```

## Python3

```python
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                best = float('inf')
                for k in range(i, j + 1):
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    if cost < best:
                        best = cost
                dp[i][j] = best
        return dp[1][n]
```

## C

```c
#include <limits.h>

int getMoneyAmount(int n) {
    if (n <= 1) return 0;
    int dp[202][202] = {0};
    
    for (int len = 2; len <= n; ++len) {
        for (int i = 1; i + len - 1 <= n; ++i) {
            int j = i + len - 1;
            int best = INT_MAX;
            for (int k = i; k < j; ++k) {
                int left = dp[i][k - 1];
                int right = dp[k + 1][j];
                int cost = k + (left > right ? left : right);
                if (cost < best) best = cost;
            }
            dp[i][j] = best;
        }
    }
    
    return dp[1][n];
}
```

## Csharp

```csharp
public class Solution
{
    public int GetMoneyAmount(int n)
    {
        if (n <= 1) return 0;
        int[,] dp = new int[n + 2, n + 2];

        for (int len = 2; len <= n; ++len)
        {
            for (int i = 1; i + len - 1 <= n; ++i)
            {
                int j = i + len - 1;
                int best = int.MaxValue;

                for (int k = i; k <= j; ++k)
                {
                    int leftCost = k > i ? dp[i, k - 1] : 0;
                    int rightCost = k < j ? dp[k + 1, j] : 0;
                    int worst = leftCost > rightCost ? leftCost : rightCost;
                    int total = k + worst;

                    if (total < best)
                        best = total;
                }

                dp[i, j] = best;
            }
        }

        return dp[1, n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var getMoneyAmount = function(n) {
    const dp = Array.from({ length: n + 2 }, () => new Array(n + 2).fill(0));
    for (let len = 2; len <= n; ++len) {
        for (let i = 1; i + len - 1 <= n; ++i) {
            const j = i + len - 1;
            let best = Infinity;
            // start from middle to reduce iterations (optional)
            const start = i + Math.floor((len - 1) / 2);
            for (let k = start; k <= j; ++k) {
                const cost = k + Math.max(dp[i][k - 1], dp[k + 1][j]);
                if (cost < best) best = cost;
            }
            dp[i][j] = best;
        }
    }
    return dp[1][n];
};
```

## Typescript

```typescript
function getMoneyAmount(n: number): number {
    const dp: number[][] = Array.from({ length: n + 2 }, () => new Array(n + 2).fill(0));
    for (let len = 2; len <= n; ++len) {
        for (let i = 1; i + len - 1 <= n; ++i) {
            const j = i + len - 1;
            let best = Number.MAX_SAFE_INTEGER;
            for (let k = i; k < j; ++k) {
                const cost = k + Math.max(dp[i][k - 1], dp[k + 1][j]);
                if (cost < best) best = cost;
            }
            dp[i][j] = best;
        }
    }
    return dp[1][n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function getMoneyAmount($n) {
        if ($n <= 1) return 0;
        // dp[i][j] = minimum money to guarantee a win in range [i, j]
        $dp = array_fill(0, $n + 2, array_fill(0, $n + 2, 0));

        for ($len = 2; $len <= $n; $len++) {
            for ($i = 1; $i + $len - 1 <= $n; $i++) {
                $j = $i + $len - 1;
                $dp[$i][$j] = PHP_INT_MAX;

                // optional optimization: start from middle to reduce iterations
                $start = $i + intdiv($len - 1, 2);
                for ($k = $start; $k <= $j; $k++) {
                    $left  = ($k - 1 >= $i) ? $dp[$i][$k - 1] : 0;
                    $right = ($k + 1 <= $j) ? $dp[$k + 1][$j] : 0;
                    $cost = $k + max($left, $right);
                    if ($cost < $dp[$i][$j]) {
                        $dp[$i][$j] = $cost;
                    }
                }
            }
        }

        return $dp[1][$n];
    }
}
```

## Swift

```swift
class Solution {
    func getMoneyAmount(_ n: Int) -> Int {
        if n <= 1 { return 0 }
        var dp = Array(repeating: Array(repeating: 0, count: n + 2), count: n + 2)
        
        for length in 2...n {
            for i in 1...(n - length + 1) {
                let j = i + length - 1
                var best = Int.max
                for k in i...j {
                    let left = (k > i) ? dp[i][k - 1] : 0
                    let right = (k < j) ? dp[k + 1][j] : 0
                    let cost = k + max(left, right)
                    if cost < best {
                        best = cost
                    }
                }
                dp[i][j] = best
            }
        }
        return dp[1][n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMoneyAmount(n: Int): Int {
        if (n <= 1) return 0
        val dp = Array(n + 2) { IntArray(n + 2) }
        for (len in 2..n) {
            for (i in 1..n - len + 1) {
                val j = i + len - 1
                var best = Int.MAX_VALUE
                for (k in i..j) {
                    val cost = k + maxOf(dp[i][k - 1], dp[k + 1][j])
                    if (cost < best) best = cost
                }
                dp[i][j] = best
            }
        }
        return dp[1][n]
    }
}
```

## Dart

```dart
class Solution {
  int getMoneyAmount(int n) {
    if (n <= 1) return 0;
    List<List<int>> dp = List.generate(n + 2, (_) => List.filled(n + 2, 0));
    for (int len = 2; len <= n; ++len) {
      for (int i = 1; i + len - 1 <= n; ++i) {
        int j = i + len - 1;
        int best = 1 << 30;
        for (int k = i; k <= j; ++k) {
          int left = k > i ? dp[i][k - 1] : 0;
          int right = k < j ? dp[k + 1][j] : 0;
          int cost = k + (left > right ? left : right);
          if (cost < best) best = cost;
        }
        dp[i][j] = best;
      }
    }
    return dp[1][n];
  }
}
```

## Golang

```go
package leetcode

func getMoneyAmount(n int) int {
	if n <= 1 {
		return 0
	}
	dp := make([][]int, n+2)
	for i := range dp {
		dp[i] = make([]int, n+2)
	}
	const INF = 1 << 30
	for length := 2; length <= n; length++ {
		for i := 1; i+length-1 <= n; i++ {
			j := i + length - 1
			dp[i][j] = INF
			for k := i; k <= j; k++ {
				left, right := 0, 0
				if k > i {
					left = dp[i][k-1]
				}
				if k < j {
					right = dp[k+1][j]
				}
				cost := k + max(left, right)
				if cost < dp[i][j] {
					dp[i][j] = cost
				}
			}
		}
	}
	return dp[1][n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def get_money_amount(n)
  # dp[i][j] = minimum amount of money to guarantee a win for range [i, j]
  dp = Array.new(n + 2) { Array.new(n + 2, 0) }

  (2..n).each do |len|
    (1..(n - len + 1)).each do |i|
      j = i + len - 1
      best = Float::INFINITY
      (i..j).each do |k|
        cost = k + [dp[i][k - 1], dp[k + 1][j]].max
        best = cost if cost < best
      end
      dp[i][j] = best
    end
  end

  dp[1][n]
end
```

## Scala

```scala
object Solution {
  def getMoneyAmount(n: Int): Int = {
    if (n <= 1) return 0
    val dp = Array.ofDim[Int](n + 2, n + 2)

    for (len <- 2 to n) {
      var i = 1
      while (i + len - 1 <= n) {
        val j = i + len - 1
        var best = Int.MaxValue
        var pivot = i
        while (pivot <= j) {
          val left  = if (pivot > i) dp(i)(pivot - 1) else 0
          val right = if (pivot < j) dp(pivot + 1)(j) else 0
          val cost = pivot + Math.max(left, right)
          if (cost < best) best = cost
          pivot += 1
        }
        dp(i)(j) = best
        i += 1
      }
    }

    dp(1)(n)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn get_money_amount(n: i32) -> i32 {
        let n = n as usize;
        if n <= 1 {
            return 0;
        }
        // dp[i][j] = minimum amount needed to guarantee a win in range [i, j]
        let mut dp = vec![vec![0i32; n + 2]; n + 2];
        for len in 2..=n {
            for i in 1..=n - len + 1 {
                let j = i + len - 1;
                let mut best = i32::MAX;
                for k in i..=j {
                    let left = dp[i][k - 1];
                    let right = dp[k + 1][j];
                    let cost = (k as i32) + std::cmp::max(left, right);
                    if cost < best {
                        best = cost;
                    }
                }
                dp[i][j] = best;
            }
        }
        dp[1][n]
    }
}
```

## Racket

```racket
#lang racket

(define/contract (get-money-amount n)
  (-> exact-integer? exact-integer?)
  (if (= n 1)
      0
      (let* ((size (+ n 2))
             (dp (make-vector size)))
        ;; initialise inner vectors
        (for ([i (in-range size)])
          (vector-set! dp i (make-vector size 0)))
        ;; fill DP table
        (for ([len (in-range 2 (add1 n))])               ; segment length
          (for ([i (in-range 1 (+ (- n len) 2))])       ; start index
            (let* ((j (+ i len -1))
                   (best #f))
              (for ([k (in-range i (add1 j))])         ; pivot
                (define left (if (> k i)
                                 (vector-ref (vector-ref dp i) (- k 1))
                                 0))
                (define right (if (< k j)
                                  (vector-ref (vector-ref dp (+ k 1)) j)
                                  0))
                (define cost (+ k (max left right)))
                (when (or (not best) (< cost best))
                  (set! best cost)))
              (vector-set! (vector-ref dp i) j best))))
        (vector-ref (vector-ref dp 1) n))))
```

## Erlang

```erlang
-module(solution).
-export([get_money_amount/1]).

-spec get_money_amount(N :: integer()) -> integer().
get_money_amount(N) when N >= 1 ->
    Map0 = init_diag(N, #{}),
    Map1 = fill_lengths(2, N, N, Map0),
    maps:get({1, N}, Map1).

init_diag(N, Map) ->
    init_diag(1, N, Map).

init_diag(I, N, Map) when I =< N ->
    Map1 = maps:put({I, I}, 0, Map),
    init_diag(I + 1, N, Map1);
init_diag(_, _, Map) -> Map.

fill_lengths(Len, MaxLen, N, Map) when Len =< MaxLen ->
    Map1 = fill_len(Len, N, Map),
    fill_lengths(Len + 1, MaxLen, N, Map1);
fill_lengths(_, _, _, Map) -> Map.

fill_len(Len, N, Map) ->
    lists:foldl(fun(I, AccMap) ->
        J = I + Len - 1,
        MinCost = find_min_cost(I, J, AccMap),
        maps:put({I, J}, MinCost, AccMap)
    end, Map, lists:seq(1, N - Len + 1)).

find_min_cost(I, J, Map) ->
    Initial = 1 bsl 30,
    lists:foldl(fun(K, Best) ->
        Left = get_dp(Map, I, K - 1),
        Right = get_dp(Map, K + 1, J),
        Cost = K + max(Left, Right),
        if Cost < Best -> Cost; true -> Best end
    end, Initial, lists:seq(I, J)).

get_dp(_Map, I, J) when I > J ->
    0;
get_dp(Map, I, J) ->
    maps:get({I, J}, Map).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_money_amount(n :: integer) :: integer
  def get_money_amount(n) when n <= 1, do: 0

  def get_money_amount(n) do
    # dp map where key {i,j} stores the minimal guaranteed cost for range [i, j]
    dp_initial = Enum.reduce(1..n, %{}, fn i, acc -> Map.put(acc, {i, i}, 0) end)

    dp_filled =
      Enum.reduce(2..n, dp_initial, fn len, dp_acc ->
        Enum.reduce(1..(n - len + 1), dp_acc, fn i, dp_inner ->
          j = i + len - 1

          best_cost =
            Enum.reduce(i..j, 1_000_000_000, fn pivot, cur_best ->
              left_cost = if pivot > i, do: Map.get(dp_inner, {i, pivot - 1}), else: 0
              right_cost = if pivot < j, do: Map.get(dp_inner, {pivot + 1, j}), else: 0
              cost = pivot + max(left_cost, right_cost)

              if cost < cur_best, do: cost, else: cur_best
            end)

          Map.put(dp_inner, {i, j}, best_cost)
        end)
      end)

    Map.get(dp_filled, {1, n})
  end
end
```

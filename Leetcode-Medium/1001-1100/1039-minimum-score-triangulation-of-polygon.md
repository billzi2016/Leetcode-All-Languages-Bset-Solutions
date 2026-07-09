# 1039. Minimum Score Triangulation of Polygon

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minScoreTriangulation(vector<int>& values) {
        int n = values.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int len = 2; len < n; ++len) { // distance between i and j
            for (int i = 0; i + len < n; ++i) {
                int j = i + len;
                dp[i][j] = INT_MAX;
                for (int k = i + 1; k < j; ++k) {
                    int cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                    if (cost < dp[i][j]) dp[i][j] = cost;
                }
            }
        }
        return dp[0][n - 1];
    }
};
```

## Java

```java
class Solution {
    public int minScoreTriangulation(int[] values) {
        int n = values.length;
        int[][] dp = new int[n][n];
        // Initialize dp for intervals with less than 3 vertices to 0 (already default)
        for (int len = 2; len < n; ++len) { // length is distance between i and j
            for (int i = 0; i + len < n; ++i) {
                int j = i + len;
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = i + 1; k < j; ++k) {
                    int cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                    if (cost < dp[i][j]) {
                        dp[i][j] = cost;
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        # length is the distance between i and j
        for length in range(2, n):  # minimum triangle needs at least 2 edges apart
            for i in range(n - length):
                j = i + length
                min_cost = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < min_cost:
                        min_cost = cost
                dp[i][j] = min_cost
        return dp[0][n - 1]
```

## Python3

```python
from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        # length is the distance between i and j
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                min_cost = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    if cost < min_cost:
                        min_cost = cost
                dp[i][j] = min_cost
        return dp[0][n - 1]
```

## C

```c
int minScoreTriangulation(int* values, int valuesSize) {
    int n = valuesSize;
    int dp[55][55];
    const int INF = 1000000000; // sufficiently large
    
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            dp[i][j] = 0;
    
    for (int len = 2; len < n; ++len) {          // distance between i and j
        for (int i = 0; i + len < n; ++i) {
            int j = i + len;
            dp[i][j] = INF;
            for (int k = i + 1; k < j; ++k) {
                int cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                if (cost < dp[i][j])
                    dp[i][j] = cost;
            }
        }
    }
    
    return dp[0][n - 1];
}
```

## Csharp

```csharp
public class Solution {
    public int MinScoreTriangulation(int[] values) {
        int n = values.Length;
        int[,] dp = new int[n, n];
        
        // dp[i, j] is 0 for intervals with less than 2 edges (i.e., length < 2)
        for (int len = 2; len < n; ++len) {          // distance between i and j
            for (int i = 0; i + len < n; ++i) {
                int j = i + len;
                dp[i, j] = int.MaxValue;
                for (int k = i + 1; k < j; ++k) {
                    int cost = dp[i, k] + dp[k, j] + values[i] * values[k] * values[j];
                    if (cost < dp[i, j]) dp[i, j] = cost;
                }
            }
        }
        
        return dp[0, n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} values
 * @return {number}
 */
var minScoreTriangulation = function(values) {
    const n = values.length;
    // dp[i][j] = minimum score to triangulate polygon from i to j (inclusive)
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    
    // length is the distance between i and j
    for (let len = 2; len < n; ++len) { // need at least three vertices, so gap >=2
        for (let i = 0; i + len < n; ++i) {
            const j = i + len;
            let best = Number.MAX_SAFE_INTEGER;
            for (let k = i + 1; k < j; ++k) {
                const cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                if (cost < best) best = cost;
            }
            dp[i][j] = best;
        }
    }
    
    return dp[0][n - 1];
};
```

## Typescript

```typescript
function minScoreTriangulation(values: number[]): number {
    const n = values.length;
    const dp: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    for (let len = 2; len < n; ++len) { // distance between i and j
        for (let i = 0; i + len < n; ++i) {
            const j = i + len;
            let best = Number.MAX_SAFE_INTEGER;
            for (let k = i + 1; k < j; ++k) {
                const cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                if (cost < best) best = cost;
            }
            dp[i][j] = best;
        }
    }

    return dp[0][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $values
     * @return Integer
     */
    function minScoreTriangulation($values) {
        $n = count($values);
        // Initialize dp matrix
        $dp = array_fill(0, $n, array_fill(0, $n, 0));

        // length is the distance between i and j
        for ($len = 2; $len < $n; $len++) {
            for ($i = 0; $i + $len < $n; $i++) {
                $j = $i + $len;
                $dp[$i][$j] = PHP_INT_MAX;
                for ($k = $i + 1; $k < $j; $k++) {
                    $cost = $dp[$i][$k] + $dp[$k][$j] + $values[$i] * $values[$k] * $values[$j];
                    if ($cost < $dp[$i][$j]) {
                        $dp[$i][$j] = $cost;
                    }
                }
            }
        }

        return $dp[0][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func minScoreTriangulation(_ values: [Int]) -> Int {
        let n = values.count
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        
        if n < 3 { return 0 }
        
        // len is the distance between i and j
        for len in 2..<n {
            for i in 0..<(n - len) {
                let j = i + len
                var best = Int.max
                for k in (i + 1)..<j {
                    let cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < best {
                        best = cost
                    }
                }
                dp[i][j] = best
            }
        }
        
        return dp[0][n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minScoreTriangulation(values: IntArray): Int {
        val n = values.size
        val dp = Array(n) { IntArray(n) }
        for (len in 2 until n) { // len is distance between i and j
            for (i in 0 until n - len) {
                val j = i + len
                var best = Int.MAX_VALUE
                for (k in i + 1 until j) {
                    val cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if (cost < best) best = cost
                }
                dp[i][j] = if (best == Int.MAX_VALUE) 0 else best
            }
        }
        return dp[0][n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int minScoreTriangulation(List<int> values) {
    int n = values.length;
    const int INF = 0x7FFFFFFFFFFFFFFF; // large sentinel
    List<List<int>> dp = List.generate(n, (_) => List.filled(n, 0));

    for (int len = 2; len < n; ++len) {
      for (int i = 0; i + len < n; ++i) {
        int j = i + len;
        int best = INF;
        for (int k = i + 1; k < j; ++k) {
          int cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
          if (cost < best) best = cost;
        }
        dp[i][j] = best;
      }
    }

    return dp[0][n - 1];
  }
}
```

## Golang

```go
func minScoreTriangulation(values []int) int {
    n := len(values)
    dp := make([][]int, n)
    const INF = int(1 << 60)
    for i := 0; i < n; i++ {
        dp[i] = make([]int, n)
        for j := 0; j < n; j++ {
            dp[i][j] = INF
        }
    }
    for i := 0; i+1 < n; i++ {
        dp[i][i+1] = 0
    }
    for length := 2; length < n; length++ {
        for i := 0; i+length < n; i++ {
            j := i + length
            for k := i + 1; k < j; k++ {
                cost := dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]
                if cost < dp[i][j] {
                    dp[i][j] = cost
                }
            }
        }
    }
    return dp[0][n-1]
}
```

## Ruby

```ruby
def min_score_triangulation(values)
  n = values.length
  dp = Array.new(n) { Array.new(n, 0) }

  (2...n).each do |len|
    (0..n - len - 1).each do |i|
      j = i + len
      min_val = Float::INFINITY
      (i + 1...j).each do |k|
        cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
        min_val = cost if cost < min_val
      end
      dp[i][j] = min_val
    end
  end

  dp[0][n - 1]
end
```

## Scala

```scala
object Solution {
    def minScoreTriangulation(values: Array[Int]): Int = {
        val n = values.length
        val dp = Array.ofDim[Int](n, n)
        // Initialize with large value
        var i = 0
        while (i < n) {
            java.util.Arrays.fill(dp(i), Int.MaxValue)
            i += 1
        }
        // Base case: subpolygons of length 2 have zero cost
        i = 0
        while (i + 1 < n) {
            dp(i)(i + 1) = 0
            i += 1
        }

        var len = 3
        while (len <= n) {
            var start = 0
            while (start + len - 1 < n) {
                val end = start + len - 1
                var best = Int.MaxValue
                var k = start + 1
                while (k < end) {
                    val cost = dp(start)(k) + dp(k)(end) + values(start) * values(k) * values(end)
                    if (cost < best) best = cost
                    k += 1
                }
                dp(start)(end) = best
                start += 1
            }
            len += 1
        }

        dp(0)(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_score_triangulation(values: Vec<i32>) -> i32 {
        let n = values.len();
        let mut dp = vec![vec![0i32; n]; n];
        for len in 2..n { // distance between i and j
            for i in 0..n - len {
                let j = i + len;
                if j - i < 2 {
                    continue;
                }
                let mut best = i32::MAX;
                for k in (i + 1)..j {
                    let cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                    if cost < best {
                        best = cost;
                    }
                }
                dp[i][j] = best;
            }
        }
        dp[0][n - 1]
    }
}
```

## Racket

```racket
(define/contract (min-score-triangulation values)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length values))
         (vals (list->vector values))
         (dp (make-vector n)))
    ;; initialize dp matrix rows
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector n 0)))
    (define INF 1000000000) ; larger than any possible answer
    ;; DP over subpolygon lengths
    (for ([len (in-range 2 n)])               ; len = j - i
      (for ([i (in-range 0 (- n len))])       ; start index
        (let* ((j (+ i len))
               (row-i (vector-ref dp i)))
          (define min-cost INF)
          (for ([k (in-range (+ i 1) j)])     ; possible middle vertex
            (let* ((cost (+ (vector-ref (vector-ref dp i) k)
                            (vector-ref (vector-ref dp k) j)
                            (* (vector-ref vals i)
                               (vector-ref vals k)
                               (vector-ref vals j)))))
              (when (< cost min-cost)
                (set! min-cost cost))))
          (vector-set! row-i j min-cost))))
    (vector-ref (vector-ref dp 0) (- n 1))))
```

## Erlang

```erlang
-module(solution).
-export([min_score_triangulation/1]).

-spec min_score_triangulation(Values :: [integer()]) -> integer().
min_score_triangulation(Values) ->
    N = length(Values),
    DP = fill_dp(N, Values, #{}),
    maps:get({0, N - 1}, DP).

fill_dp(N, Values, DP) ->
    lists:foldl(
        fun(Len, DPrev) ->
            lists:foldl(
                fun(I, DAcc) ->
                    J = I + Len,
                    Min = compute_min(I, J, Values, DAcc),
                    maps:put({I, J}, Min, DAcc)
                end,
                DPrev,
                lists:seq(0, N - Len - 1)
            )
        end,
        DP,
        lists:seq(2, N - 1)
    ).

compute_min(I, J, Values, DP) ->
    Vi = lists:nth(I + 1, Values),
    Vj = lists:nth(J + 1, Values),
    Candidates =
        [ maps:get({I, K}, DP, 0) + maps:get({K, J}, DP, 0)
          + Vi * (lists:nth(K + 1, Values)) * Vj
          || K <- lists:seq(I + 1, J - 1) ],
    lists:min(Candidates).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_score_triangulation(values :: [integer]) :: integer
  def min_score_triangulation(values) do
    n = length(values)
    vals = List.to_tuple(values)

    dp =
      Enum.reduce(2..(n - 1), %{}, fn len, acc ->
        Enum.reduce(0..(n - len - 1), acc, fn i, acc2 ->
          j = i + len

          min_cost =
            Enum.reduce((i + 1)..(j - 1), 1_000_000_000, fn k, best ->
              left = Map.get(acc2, {i, k}, 0)
              right = Map.get(acc2, {k, j}, 0)

              cost = left + right + elem(vals, i) * elem(vals, k) * elem(vals, j)

              if cost < best, do: cost, else: best
            end)

          Map.put(acc2, {i, j}, min_cost)
        end)
      end)

    Map.get(dp, {0, n - 1})
  end
end
```

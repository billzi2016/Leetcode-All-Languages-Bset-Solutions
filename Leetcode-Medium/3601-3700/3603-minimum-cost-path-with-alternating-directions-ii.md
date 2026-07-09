# 3603. Minimum Cost Path with Alternating Directions II

## Cpp

```cpp
class Solution {
public:
    long long minCost(int m, int n, vector<vector<int>>& waitCost) {
        const long long INF = (1LL<<60);
        vector<long long> prev(n, INF), cur(n, INF);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) {
                    cur[0] = 1LL; // entrance cost of (0,0)
                } else {
                    long long best = INF;
                    if (i > 0) best = min(best, prev[j]);      // from top
                    if (j > 0) best = min(best, cur[j - 1]);   // from left
                    cur[j] = best + waitCost[i][j] + 1LL * (i + 1) * (j + 1);
                }
            }
            swap(prev, cur);
        }
        long long total = prev[n - 1] - waitCost[m - 1][n - 1];
        return total;
    }
};
```

## Java

```java
class Solution {
    public long minCost(int m, int n, int[][] waitCost) {
        int rows = m;
        int cols = n;
        long[] dp = new long[cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                long entrance = (long) (i + 1) * (j + 1);
                if (i == 0 && j == 0) {
                    dp[0] = entrance; // no wait cost at start
                } else {
                    long prev;
                    if (i == 0) {
                        prev = dp[j - 1];
                    } else if (j == 0) {
                        prev = dp[j]; // value from previous row, same column
                    } else {
                        prev = Math.min(dp[j], dp[j - 1]);
                    }
                    dp[j] = prev + waitCost[i][j] + entrance;
                }
            }
        }
        return dp[cols - 1] - waitCost[rows - 1][cols - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, m, n, waitCost):
        """
        :type m: int
        :type n: int
        :type waitCost: List[List[int]]
        :rtype: int
        """
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                cell_cost = (i + 1) * (j + 1)
                if i == 0 and j == 0:
                    dp[0] = cell_cost
                elif i == 0:
                    # can only come from left
                    dp[j] = dp[j - 1] + waitCost[i][j] + cell_cost
                elif j == 0:
                    # can only come from up (dp[0] holds previous row's value)
                    dp[0] = dp[0] + waitCost[i][j] + cell_cost
                else:
                    from_up = dp[j]          # value before overwrite (previous row)
                    from_left = dp[j - 1]    # already updated for current row
                    dp[j] = min(from_up, from_left) + waitCost[i][j] + cell_cost
        return dp[-1] - waitCost[m - 1][n - 1]
```

## Python3

```python
from typing import List

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = 10**18
        prev = [INF] * n
        for i in range(m):
            cur = [INF] * n
            for j in range(n):
                if i == 0 and j == 0:
                    cur[j] = (i + 1) * (j + 1)  # entrance cost, no wait
                else:
                    top = prev[j] if i > 0 else INF
                    left = cur[j - 1] if j > 0 else INF
                    best = top if top < left else left
                    cur[j] = best + (i + 1) * (j + 1) + waitCost[i][j]
            prev = cur
        return prev[-1] - waitCost[m - 1][n - 1]
```

## C

```c
long long minCost(int m, int n, int** waitCost, int waitCostSize, int* waitCostColSize) {
    const long long INF = 9e18;
    // Allocate two rows for DP
    long long *prev = (long long *)malloc(sizeof(long long) * n);
    long long *cur = (long long *)malloc(sizeof(long long) * n);
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            long long enterCost = (long long)(i + 1) * (j + 1);
            if (i == 0 && j == 0) {
                cur[j] = enterCost; // first cell, no wait cost
            } else {
                long long best = INF;
                if (i > 0) best = prev[j];
                if (j > 0 && cur[j - 1] < best) best = cur[j - 1];
                cur[j] = best + waitCost[i][j] + enterCost;
            }
        }
        // swap pointers for next iteration
        long long *tmp = prev;
        prev = cur;
        cur = tmp;
    }
    
    long long result = prev[n - 1] - waitCost[m - 1][n - 1];
    free(prev);
    free(cur);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public long MinCost(int m, int n, int[][] waitCost) {
        int rows = m;
        int cols = n;
        long[] dp = new long[cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                long entrance = (long)(i + 1) * (j + 1);
                if (i == 0 && j == 0) {
                    dp[j] = entrance;
                } else {
                    long minPrev;
                    if (i == 0) {
                        minPrev = dp[j - 1];
                    } else if (j == 0) {
                        minPrev = dp[j];
                    } else {
                        minPrev = Math.Min(dp[j], dp[j - 1]);
                    }
                    dp[j] = minPrev + waitCost[i][j] + entrance;
                }
            }
        }
        return dp[cols - 1] - waitCost[m - 1][n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} waitCost
 * @return {number}
 */
var minCost = function(m, n, waitCost) {
    const INF = Number.MAX_SAFE_INTEGER;
    let prev = new Array(n).fill(INF);
    let cur = new Array(n).fill(INF);
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const entrance = (i + 1) * (j + 1);
            if (i === 0 && j === 0) {
                cur[j] = entrance; // start cell, no wait cost
            } else {
                const up = i > 0 ? prev[j] : INF;
                const left = j > 0 ? cur[j - 1] : INF;
                cur[j] = Math.min(up, left) + waitCost[i][j] + entrance;
            }
        }
        // prepare for next row
        [prev, cur] = [cur, new Array(n).fill(INF)];
    }
    
    const total = prev[n - 1];
    return total - waitCost[m - 1][n - 1];
};
```

## Typescript

```typescript
function minCost(m: number, n: number, waitCost: number[][]): number {
    const dp = new Array<number>(n);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const entrance = (i + 1) * (j + 1);
            if (i === 0 && j === 0) {
                dp[0] = entrance;
            } else if (i === 0) {
                // first row, can only come from left
                dp[j] = dp[j - 1] + waitCost[i][j] + entrance;
            } else if (j === 0) {
                // first column, can only come from top (dp[0] holds previous row's value)
                dp[0] = dp[0] + waitCost[i][j] + entrance;
            } else {
                const fromTop = dp[j];      // value before overwrite: previous row same column
                const fromLeft = dp[j - 1]; // already updated for current row
                dp[j] = Math.min(fromTop, fromLeft) + waitCost[i][j] + entrance;
            }
        }
    }
    return dp[n - 1] - waitCost[m - 1][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $waitCost
     * @return Integer
     */
    function minCost($m, $n, $waitCost) {
        // dp[j] holds the minimum cost to reach cell (current row, j)
        $dp = array_fill(0, $n, 0);

        // Initialize first cell (0,0)
        $dp[0] = 1; // entrance cost (1*1)

        // First row (i = 0)
        for ($j = 1; $j < $n; $j++) {
            $entrance = ($j + 1);               // (0+1)*(j+1)
            $dp[$j] = $dp[$j - 1] + $waitCost[0][$j] + $entrance;
        }

        // Process remaining rows
        for ($i = 1; $i < $m; $i++) {
            // First column of current row
            $entrance = ($i + 1) * 1;            // (i+1)*(0+1)
            $dp[0] = $dp[0] + $waitCost[$i][0] + $entrance;

            for ($j = 1; $j < $n; $j++) {
                $entrance = ($i + 1) * ($j + 1);
                $dp[$j] = min($dp[$j - 1], $dp[$j]) + $waitCost[$i][$j] + $entrance;
            }
        }

        // Subtract wait cost at destination as we don't need to wait there
        return $dp[$n - 1] - $waitCost[$m - 1][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ m: Int, _ n: Int, _ waitCost: [[Int]]) -> Int {
        var dp = Array(repeating: 0, count: n)
        // Starting cell (0,0) entrance cost only
        dp[0] = 1
        
        // First row (i = 0)
        if m > 0 && n > 1 {
            for j in 1..<n {
                let entrance = (j + 1) * 1   // i = 0 => (i+1)=1
                dp[j] = dp[j - 1] + entrance + waitCost[0][j]
            }
        }
        
        // Remaining rows
        if m > 1 {
            for i in 1..<m {
                // First column of current row
                let entranceFirst = (i + 1) * 1   // j = 0 => (j+1)=1
                dp[0] = dp[0] + entranceFirst + waitCost[i][0]
                
                if n > 1 {
                    for j in 1..<n {
                        let entrance = (i + 1) * (j + 1)
                        let bestPrev = min(dp[j], dp[j - 1])
                        dp[j] = bestPrev + entrance + waitCost[i][j]
                    }
                }
            }
        }
        
        // Subtract wait cost of the destination cell, which shouldn't be added
        return dp[n - 1] - waitCost[m - 1][n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(m: Int, n: Int, waitCost: Array<IntArray>): Long {
        val dp = LongArray(n)
        for (i in 0 until m) {
            for (j in 0 until n) {
                val enter = ((i + 1).toLong() * (j + 1))
                if (i == 0 && j == 0) {
                    dp[0] = enter
                } else {
                    var best = Long.MAX_VALUE
                    if (i > 0) best = kotlin.math.min(best, dp[j])          // from above
                    if (j > 0) best = kotlin.math.min(best, dp[j - 1])      // from left
                    dp[j] = best + waitCost[i][j].toLong() + enter
                }
            }
        }
        return dp[n - 1] - waitCost[m - 1][n - 1].toLong()
    }
}
```

## Dart

```dart
class Solution {
  int minCost(int m, int n, List<List<int>> waitCost) {
    // dp[i][j] stores minimal cost to reach (i,j) including entrance and waiting costs,
    // except we will subtract the waiting cost at destination later.
    List<List<int>> dp = List.generate(m, (_) => List.filled(n, 0));

    // Starting cell: only entrance cost.
    dp[0][0] = 1; // (0+1)*(0+1)

    // First row.
    for (int j = 1; j < n; ++j) {
      int entrance = (j + 1); // (0+1)*(j+1)
      dp[0][j] = dp[0][j - 1] + waitCost[0][j] + entrance;
    }

    // First column.
    for (int i = 1; i < m; ++i) {
      int entrance = (i + 1); // (i+1)*(0+1)
      dp[i][0] = dp[i - 1][0] + waitCost[i][0] + entrance;
    }

    // Rest of the grid.
    for (int i = 1; i < m; ++i) {
      for (int j = 1; j < n; ++j) {
        int entrance = (i + 1) * (j + 1);
        int bestPrev = dp[i - 1][j] < dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1];
        dp[i][j] = bestPrev + waitCost[i][j] + entrance;
      }
    }

    // Subtract waiting cost at destination as we don't wait there.
    return dp[m - 1][n - 1] - waitCost[m - 1][n - 1];
  }
}
```

## Golang

```go
func minCost(m int, n int, waitCost [][]int) int64 {
    // dpPrev holds DP values for the previous row
    dpPrev := make([]int64, n)

    // Initialize first cell (0,0)
    dpPrev[0] = 1 // entrance cost (1*1)

    // First row initialization
    for j := 1; j < n; j++ {
        dpPrev[j] = dpPrev[j-1] + int64(waitCost[0][j]) + int64((j+1))
    }

    // Process remaining rows
    for i := 1; i < m; i++ {
        cur := make([]int64, n)
        // First column of current row
        cur[0] = dpPrev[0] + int64(waitCost[i][0]) + int64((i+1))
        // Rest of the columns
        for j := 1; j < n; j++ {
            up := dpPrev[j]
            left := cur[j-1]
            if left < up {
                up = left
            }
            cur[j] = up + int64(waitCost[i][j]) + int64((i+1)*(j+1))
        }
        dpPrev = cur
    }

    // Subtract wait cost at destination as we don't need to wait there
    return dpPrev[n-1] - int64(waitCost[m-1][n-1])
}
```

## Ruby

```ruby
def min_cost(m, n, wait_cost)
  inf = (1 << 62)
  prev = nil
  (0...m).each do |i|
    cur = Array.new(n, 0)
    (0...n).each do |j|
      entrance = (i + 1) * (j + 1)
      if i == 0 && j == 0
        cur[j] = entrance
      else
        up   = i > 0 ? prev[j] : inf
        left = j > 0 ? cur[j - 1] : inf
        best = up < left ? up : left
        cur[j] = best + wait_cost[i][j] + entrance
      end
    end
    prev = cur
  end
  result = prev[n - 1] - wait_cost[m - 1][n - 1]
  result
end
```

## Scala

```scala
object Solution {
    def minCost(m: Int, n: Int, waitCost: Array[Array[Int]]): Long = {
        val dp = Array.ofDim[Long](m, n)
        dp(0)(0) = 1L // entrance cost for (0,0)

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (i == 0 && j == 0) {
                    // already initialized
                } else {
                    val entrance = (i + 1).toLong * (j + 1)
                    var best = Long.MaxValue
                    if (i > 0) best = math.min(best, dp(i - 1)(j))
                    if (j > 0) best = math.min(best, dp(i)(j - 1))
                    dp(i)(j) = best + waitCost(i)(j).toLong + entrance
                }
            }
        }

        dp(m - 1)(n - 1) - waitCost(m - 1)(n - 1).toLong
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(m: i32, n: i32, wait_cost: Vec<Vec<i32>>) -> i64 {
        let m = m as usize;
        let n = n as usize;
        const INF: i64 = i64::MAX / 4;
        let mut dp0_prev = vec![INF; n];
        let mut dp1_prev = vec![INF; n];

        for i in 0..m {
            let mut dp0_cur = vec![INF; n];
            let mut dp1_cur = vec![INF; n];
            for j in 0..n {
                let entrance = ((i as i64 + 1) * (j as i64 + 1)) as i64;
                if i == 0 && j == 0 {
                    dp0_cur[0] = entrance;
                    dp1_cur[0] = entrance;
                    continue;
                }
                // arrive from top (down move)
                if i > 0 {
                    let up0 = dp0_prev[j];
                    if up0 != INF {
                        dp0_cur[j] = dp0_cur[j].min(up0 + entrance);
                    }
                    let up1 = dp1_prev[j];
                    if up1 != INF {
                        let wait = wait_cost[i - 1][j] as i64;
                        dp0_cur[j] = dp0_cur[j].min(up1 + wait + entrance);
                    }
                }
                // arrive from left (right move)
                if j > 0 {
                    let left1 = dp1_cur[j - 1];
                    if left1 != INF {
                        dp1_cur[j] = dp1_cur[j].min(left1 + entrance);
                    }
                    let left0 = dp0_cur[j - 1];
                    if left0 != INF {
                        let wait = wait_cost[i][j - 1] as i64;
                        dp1_cur[j] = dp1_cur[j].min(left0 + wait + entrance);
                    }
                }
            }
            dp0_prev = dp0_cur;
            dp1_prev = dp1_cur;
        }

        dp0_prev[n - 1].min(dp1_prev[n - 1])
    }
}
```

## Racket

```racket
(define/contract (min-cost m n waitCost)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([rows (list->vector (map list->vector waitCost))]
         [ncols n])
    (define prev (make-vector ncols))
    ;; first row
    (for ((j (in-range ncols)))
      (if (= j 0)
          (vector-set! prev 0 1)
          (let* ([left (vector-ref prev (sub1 j))]
                 [cost (+ left
                          (vector-ref (vector-ref rows 0) j)
                          (* 1 (+ j 1)))])
            (vector-set! prev j cost))))
    ;; subsequent rows
    (for ((i (in-range 1 m)))
      (define cur (make-vector ncols))
      (for ((j (in-range ncols)))
        (cond
          [(= j 0)
           (let* ([top (vector-ref prev 0)]
                  [cost (+ top
                           (vector-ref (vector-ref rows i) 0)
                           (* (+ i 1) 1))])
             (vector-set! cur 0 cost))]
          [else
           (let* ([top (vector-ref prev j)]
                  [left (vector-ref cur (sub1 j))]
                  [minprev (if (< top left) top left)]
                  [cost (+ minprev
                           (vector-ref (vector-ref rows i) j)
                           (* (+ i 1) (+ j 1)))])
             (vector-set! cur j cost))]))
      (set! prev cur))
    ;; answer
    (let* ([final (vector-ref prev (sub1 ncols))]
           [lastWait (vector-ref (vector-ref rows (sub1 m)) (sub1 ncols))])
      (- final lastWait))))
```

## Erlang

```erlang
-module(solution).
-export([min_cost/3]).

-spec min_cost(integer(), integer(), [[integer()]]) -> integer().
min_cost(M, N, WaitCost) ->
    FinalDP = process_rows(0, WaitCost, [], N),
    DestDP = lists:last(FinalDP),
    LastRow = lists:nth(M, WaitCost),
    DestWait = lists:nth(N, LastRow),
    DestDP - DestWait.

process_rows(_I, [], DPRow, _N) ->
    DPRow;
process_rows(I, [Row|RestRows], PrevDP, N) ->
    CurrDP = compute_row(I, Row, PrevDP),
    process_rows(I + 1, RestRows, CurrDP, N).

compute_row(I, RowVals, PrevDP) ->
    row_loop(I, 0, RowVals, PrevDP, [], undefined).

row_loop(_I, _J, [], [], AccRev, _Left) ->
    lists:reverse(AccRev);
% start cell (0,0)
row_loop(0, 0, [_W|Ws], [], AccRev, undefined) ->
    Entrance = 1,
    Curr = Entrance,
    row_loop(0, 1, Ws, [], [Curr | AccRev], Curr);
% first column for rows i>0
row_loop(I, 0, [W|Ws], [Up|RestPrev], AccRev, undefined) when I > 0 ->
    Entrance = (I + 1) * 1,
    Curr = Up + W + Entrance,
    row_loop(I, 1, Ws, RestPrev, [Curr | AccRev], Curr);
% first row (i=0), j>0
row_loop(0, J, [W|Ws], [], AccRev, Left) ->
    Entrance = (J + 1),
    Curr = Left + W + Entrance,
    row_loop(0, J + 1, Ws, [], [Curr | AccRev], Curr);
% general case i>0, j>0
row_loop(I, J, [W|Ws], [Up|RestPrev], AccRev, Left) ->
    Entrance = (I + 1) * (J + 1),
    MinPrev = erlang:min(Up, Left),
    Curr = MinPrev + W + Entrance,
    row_loop(I, J + 1, Ws, RestPrev, [Curr | AccRev], Curr).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(m :: integer, n :: integer, wait_cost :: [[integer]]) :: integer
  def min_cost(m, n, wait_cost) do
    # Compute DP for the first row
    first_row = List.at(wait_cost, 0) |> List.to_tuple()

    {dp_rev, _} =
      Enum.reduce(0..(n - 1), {[], nil}, fn j, {acc_rev, left} ->
        wait = elem(first_row, j)

        cost =
          if j == 0 do
            1
          else
            left + wait + (j + 1)
          end

        {[cost | acc_rev], cost}
      end)

    dp = Enum.reverse(dp_rev)

    # Process remaining rows
    dp =
      Enum.reduce(1..(m - 1), dp, fn i, prev_dp ->
        row_wait = List.at(wait_cost, i) |> List.to_tuple()
        prev_tuple = List.to_tuple(prev_dp)

        {new_rev, _} =
          Enum.reduce(0..(n - 1), {[], nil}, fn j, {acc_rev, left} ->
            wait = elem(row_wait, j)
            top = elem(prev_tuple, j)

            cost =
              if j == 0 do
                top + wait + (i + 1) * 1
              else
                min(top, left) + wait + (i + 1) * (j + 1)
              end

            {[cost | acc_rev], cost}
          end)

        Enum.reverse(new_rev)
      end)

    total = List.last(dp)
    last_wait = wait_cost |> List.at(m - 1) |> Enum.at(n - 1)
    total - last_wait
  end
end
```

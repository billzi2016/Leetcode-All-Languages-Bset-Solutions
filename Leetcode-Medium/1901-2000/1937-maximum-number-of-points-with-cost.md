# 1937. Maximum Number of Points with Cost

## Cpp

```cpp
class Solution {
public:
    long long maxPoints(std::vector<std::vector<int>>& points) {
        int m = points.size();
        int n = points[0].size();
        std::vector<long long> dp(n);
        for (int j = 0; j < n; ++j) dp[j] = points[0][j];
        std::vector<long long> left(n), right(n);
        for (int i = 1; i < m; ++i) {
            // left to right
            left[0] = dp[0];
            for (int j = 1; j < n; ++j) {
                left[j] = std::max(dp[j], left[j - 1] - 1);
            }
            // right to left
            right[n - 1] = dp[n - 1];
            for (int j = n - 2; j >= 0; --j) {
                right[j] = std::max(dp[j], right[j + 1] - 1);
            }
            // compute new dp
            for (int j = 0; j < n; ++j) {
                dp[j] = points[i][j] + std::max(left[j], right[j]);
            }
        }
        long long ans = dp[0];
        for (int j = 1; j < n; ++j) if (dp[j] > ans) ans = dp[j];
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxPoints(int[][] points) {
        int m = points.length;
        int n = points[0].length;
        long[] dp = new long[n];
        for (int j = 0; j < n; j++) {
            dp[j] = points[0][j];
        }
        for (int i = 1; i < m; i++) {
            long[] left = new long[n];
            left[0] = dp[0];
            for (int j = 1; j < n; j++) {
                left[j] = Math.max(dp[j], left[j - 1] - 1);
            }
            long[] right = new long[n];
            right[n - 1] = dp[n - 1];
            for (int j = n - 2; j >= 0; j--) {
                right[j] = Math.max(dp[j], right[j + 1] - 1);
            }
            for (int j = 0; j < n; j++) {
                dp[j] = Math.max(left[j], right[j]) + points[i][j];
            }
        }
        long ans = Long.MIN_VALUE;
        for (long v : dp) {
            if (v > ans) ans = v;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        n = len(points[0])
        dp = points[0][:]  # best scores ending at each column of the first row

        for r in range(1, m):
            left = [0] * n
            right = [0] * n

            # compute max from left side considering penalty -1 per step
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(dp[c], left[c - 1] - 1)

            # compute max from right side
            right[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right[c] = max(dp[c], right[c + 1] - 1)

            new_dp = [0] * n
            row = points[r]
            for c in range(n):
                best_prev = left[c] if left[c] > right[c] else right[c]
                new_dp[c] = row[c] + best_prev

            dp = new_dp

        return max(dp)
```

## Python3

```python
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = points[0][:]  # best scores ending at each column of the first row
        
        for r in range(1, m):
            left = [0] * n
            right = [0] * n
            
            # Left to right pass
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(dp[c], left[c - 1] - 1)
            
            # Right to left pass
            right[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right[c] = max(dp[c], right[c + 1] - 1)
            
            new_dp = [0] * n
            row = points[r]
            for c in range(n):
                best_prev = left[c] if left[c] > right[c] else right[c]
                new_dp[c] = best_prev + row[c]
            
            dp = new_dp
        
        return max(dp)
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static inline long long maxll(long long a, long long b) {
    return a > b ? a : b;
}

long long maxPoints(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize == 0) return 0;
    int m = pointsSize;
    int n = pointsColSize[0];
    
    long long *dp = (long long *)malloc(sizeof(long long) * n);
    for (int j = 0; j < n; ++j) {
        dp[j] = points[0][j];
    }
    
    for (int i = 1; i < m; ++i) {
        long long *left = (long long *)malloc(sizeof(long long) * n);
        long long *right = (long long *)malloc(sizeof(long long) * n);
        
        left[0] = dp[0];
        for (int j = 1; j < n; ++j) {
            left[j] = maxll(dp[j], left[j - 1] - 1);
        }
        
        right[n - 1] = dp[n - 1];
        for (int j = n - 2; j >= 0; --j) {
            right[j] = maxll(dp[j], right[j + 1] - 1);
        }
        
        for (int j = 0; j < n; ++j) {
            long long best = maxll(left[j], right[j]);
            dp[j] = best + points[i][j];
        }
        
        free(left);
        free(right);
    }
    
    long long ans = dp[0];
    for (int j = 1; j < n; ++j) {
        if (dp[j] > ans) ans = dp[j];
    }
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaxPoints(int[][] points)
    {
        int m = points.Length;
        int n = points[0].Length;

        long[] dp = new long[n];
        for (int j = 0; j < n; j++)
            dp[j] = points[0][j];

        for (int i = 1; i < m; i++)
        {
            long[] left = new long[n];
            left[0] = dp[0];
            for (int j = 1; j < n; j++)
            {
                long candidate = left[j - 1] - 1;
                left[j] = dp[j] > candidate ? dp[j] : candidate;
            }

            long[] right = new long[n];
            right[n - 1] = dp[n - 1];
            for (int j = n - 2; j >= 0; j--)
            {
                long candidate = right[j + 1] - 1;
                right[j] = dp[j] > candidate ? dp[j] : candidate;
            }

            long[] ndp = new long[n];
            for (int j = 0; j < n; j++)
            {
                long bestPrev = left[j] > right[j] ? left[j] : right[j];
                ndp[j] = bestPrev + points[i][j];
            }
            dp = ndp;
        }

        long ans = dp[0];
        for (int j = 1; j < n; j++)
            if (dp[j] > ans) ans = dp[j];

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxPoints = function(points) {
    const m = points.length;
    const n = points[0].length;
    let dp = points[0].slice(); // best scores for the first row

    for (let i = 1; i < m; ++i) {
        const left = new Array(n);
        const right = new Array(n);
        const cur = new Array(n);

        // left to right pass
        left[0] = dp[0];
        for (let j = 1; j < n; ++j) {
            left[j] = Math.max(dp[j], left[j - 1] - 1);
        }

        // right to left pass
        right[n - 1] = dp[n - 1];
        for (let j = n - 2; j >= 0; --j) {
            right[j] = Math.max(dp[j], right[j + 1] - 1);
        }

        // combine with current row values
        const rowVals = points[i];
        for (let j = 0; j < n; ++j) {
            cur[j] = rowVals[j] + Math.max(left[j], right[j]);
        }

        dp = cur;
    }

    let ans = dp[0];
    for (let i = 1; i < n; ++i) {
        if (dp[i] > ans) ans = dp[i];
    }
    return ans;
};
```

## Typescript

```typescript
function maxPoints(points: number[][]): number {
    const m = points.length;
    const n = points[0].length;
    let dp = points[0].slice(); // copy first row

    for (let i = 1; i < m; i++) {
        const left = new Array<number>(n);
        const right = new Array<number>(n);

        left[0] = dp[0];
        for (let j = 1; j < n; j++) {
            left[j] = Math.max(dp[j], left[j - 1] - 1);
        }

        right[n - 1] = dp[n - 1];
        for (let j = n - 2; j >= 0; j--) {
            right[j] = Math.max(dp[j], right[j + 1] - 1);
        }

        const newDp = new Array<number>(n);
        const row = points[i];
        for (let j = 0; j < n; j++) {
            newDp[j] = row[j] + Math.max(left[j], right[j]);
        }
        dp = newDp;
    }

    let ans = -Infinity;
    for (const v of dp) {
        if (v > ans) ans = v;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxPoints($points) {
        $m = count($points);
        if ($m == 0) return 0;
        $n = count($points[0]);
        // dp holds the best scores for previous row
        $dp = $points[0];

        for ($row = 1; $row < $m; ++$row) {
            // left to right pass
            $left = array_fill(0, $n, 0);
            $left[0] = $dp[0];
            for ($col = 1; $col < $n; ++$col) {
                $left[$col] = max($dp[$col], $left[$col - 1] - 1);
            }

            // right to left pass
            $right = array_fill(0, $n, 0);
            $right[$n - 1] = $dp[$n - 1];
            for ($col = $n - 2; $col >= 0; --$col) {
                $right[$col] = max($dp[$col], $right[$col + 1] - 1);
            }

            // compute current dp
            $newDp = array_fill(0, $n, 0);
            for ($col = 0; $col < $n; ++$col) {
                $bestPrev = max($left[$col], $right[$col]);
                $newDp[$col] = $points[$row][$col] + $bestPrev;
            }
            $dp = $newDp;
        }

        // answer is maximum in last dp row
        $ans = $dp[0];
        for ($i = 1; $i < $n; ++$i) {
            if ($dp[$i] > $ans) $ans = $dp[$i];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxPoints(_ points: [[Int]]) -> Int {
        let m = points.count
        let n = points[0].count
        var dp = points[0]   // DP for the previous row
        
        if m == 1 {
            return dp.max()!
        }
        
        for r in 1..<m {
            var left = [Int](repeating: 0, count: n)
            var right = [Int](repeating: 0, count: n)
            
            // Left to right pass
            left[0] = dp[0]
            if n > 1 {
                for c in 1..<n {
                    left[c] = max(dp[c], left[c - 1] - 1)
                }
            }
            
            // Right to left pass
            right[n - 1] = dp[n - 1]
            if n > 1 {
                for c in stride(from: n - 2, through: 0, by: -1) {
                    right[c] = max(dp[c], right[c + 1] - 1)
                }
            }
            
            // Compute current DP row
            var newDp = [Int](repeating: 0, count: n)
            for c in 0..<n {
                let bestPrev = max(left[c], right[c])
                newDp[c] = points[r][c] + bestPrev
            }
            dp = newDp
        }
        
        return dp.max()!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPoints(points: Array<IntArray>): Long {
        val m = points.size
        val n = points[0].size
        var dp = LongArray(n) { points[0][it].toLong() }
        for (i in 1 until m) {
            val left = LongArray(n)
            val right = LongArray(n)
            left[0] = dp[0]
            for (j in 1 until n) {
                left[j] = maxOf(dp[j], left[j - 1] - 1)
            }
            right[n - 1] = dp[n - 1]
            for (j in n - 2 downTo 0) {
                right[j] = maxOf(dp[j], right[j + 1] - 1)
            }
            val cur = LongArray(n)
            for (j in 0 until n) {
                cur[j] = maxOf(left[j], right[j]) + points[i][j].toLong()
            }
            dp = cur
        }
        var ans = dp[0]
        for (v in dp) if (v > ans) ans = v
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxPoints(List<List<int>> points) {
    int m = points.length;
    int n = points[0].length;
    List<int> prev = List.from(points[0]);

    for (int i = 1; i < m; i++) {
      List<int> left = List.filled(n, 0);
      List<int> right = List.filled(n, 0);

      left[0] = prev[0];
      for (int j = 1; j < n; j++) {
        left[j] = max(prev[j], left[j - 1] - 1);
      }

      right[n - 1] = prev[n - 1];
      for (int j = n - 2; j >= 0; j--) {
        right[j] = max(prev[j], right[j + 1] - 1);
      }

      List<int> cur = List.filled(n, 0);
      for (int j = 0; j < n; j++) {
        cur[j] = points[i][j] + max(left[j], right[j]);
      }
      prev = cur;
    }

    int ans = prev[0];
    for (int v in prev) {
      if (v > ans) ans = v;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func maxPoints(points [][]int) int64 {
	m := len(points)
	n := len(points[0])

	prev := make([]int64, n)
	for j := 0; j < n; j++ {
		prev[j] = int64(points[0][j])
	}

	for i := 1; i < m; i++ {
		left := make([]int64, n)
		right := make([]int64, n)

		// left to right pass
		left[0] = prev[0]
		for j := 1; j < n; j++ {
			if prev[j] > left[j-1]-1 {
				left[j] = prev[j]
			} else {
				left[j] = left[j-1] - 1
			}
		}

		// right to left pass
		right[n-1] = prev[n-1]
		for j := n - 2; j >= 0; j-- {
			if prev[j] > right[j+1]-1 {
				right[j] = prev[j]
			} else {
				right[j] = right[j+1] - 1
			}
		}

		cur := make([]int64, n)
		row := points[i]
		for j := 0; j < n; j++ {
			best := left[j]
			if right[j] > best {
				best = right[j]
			}
			cur[j] = best + int64(row[j])
		}
		prev = cur
	}

	ans := prev[0]
	for _, v := range prev {
		if v > ans {
			ans = v
		}
	}
	// In case of empty input (should not happen per constraints)
	if math.IsNaN(float64(ans)) {
		return 0
	}
	return ans
}
```

## Ruby

```ruby
def max_points(points)
  m = points.length
  n = points[0].length
  dp = points[0].dup

  (1...m).each do |i|
    left = Array.new(n)
    cur_max = -10**15
    (0...n).each do |j|
      cur_max = [cur_max - 1, dp[j]].max
      left[j] = cur_max
    end

    right_max = -10**15
    (n - 1).downto(0) do |j|
      right_max = [right_max - 1, dp[j]].max
      best = [left[j], right_max].max + points[i][j]
      left[j] = best
    end

    dp = left
  end

  dp.max
end
```

## Scala

```scala
object Solution {
  def maxPoints(points: Array[Array[Int]]): Long = {
    val m = points.length
    val n = points(0).length
    var prev = new Array[Long](n)
    // initialize with first row values
    for (j <- 0 until n) {
      prev(j) = points(0)(j).toLong
    }
    // process subsequent rows
    var i = 1
    while (i < m) {
      val left = new Array[Long](n)
      val right = new Array[Long](n)
      // left to right pass
      left(0) = prev(0)
      var j = 1
      while (j < n) {
        left(j) = math.max(prev(j), left(j - 1) - 1L)
        j += 1
      }
      // right to left pass
      right(n - 1) = prev(n - 1)
      j = n - 2
      while (j >= 0) {
        right(j) = math.max(prev(j), right(j + 1) - 1L)
        j -= 1
      }
      // compute current row dp
      val cur = new Array[Long](n)
      j = 0
      while (j < n) {
        val bestPrev = math.max(left(j), right(j))
        cur(j) = bestPrev + points(i)(j).toLong
        j += 1
      }
      prev = cur
      i += 1
    }
    // answer is max of last row dp
    var ans = Long.MinValue
    for (v <- prev) {
      if (v > ans) ans = v
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i64 {
        let m = points.len();
        if m == 0 {
            return 0;
        }
        let n = points[0].len();
        let mut dp: Vec<i64> = points[0].iter().map(|&x| x as i64).collect();

        for r in 1..m {
            let row = &points[r];
            // left to right pass
            let mut left = vec![0i64; n];
            left[0] = dp[0];
            for c in 1..n {
                left[c] = std::cmp::max(dp[c], left[c - 1] - 1);
            }
            // right to left pass
            let mut right = vec![0i64; n];
            right[n - 1] = dp[n - 1];
            for c in (0..n - 1).rev() {
                right[c] = std::cmp::max(dp[c], right[c + 1] - 1);
            }
            // combine
            let mut new_dp = vec![0i64; n];
            for c in 0..n {
                let best = std::cmp::max(left[c], right[c]);
                new_dp[c] = best + row[c] as i64;
            }
            dp = new_dp;
        }

        *dp.iter().max().unwrap()
    }
}
```

## Racket

```racket
(define/contract (max-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (map list->vector points))
         (m (length rows)))
    (if (= m 0)
        0
        (let loop ((i 1) (prev (list-ref rows 0))) ; prev holds DP values for previous row
          (if (= i m)
              (apply max (vector->list prev))
              (let* ((curr-row (list-ref rows i))
                     (n (vector-length prev))
                     (left (make-vector n))
                     (right (make-vector n)))
                ;; left-to-right pass
                (vector-set! left 0 (vector-ref prev 0))
                (for ([col (in-range 1 n)])
                  (let* ((val (vector-ref prev col))
                         (cand (- (vector-ref left (- col 1)) 1))
                         (best (if (> val cand) val cand)))
                    (vector-set! left col best)))
                ;; right-to-left pass
                (vector-set! right (- n 1) (vector-ref prev (- n 1)))
                (for ([col (in-range (- n 2) -1 -1)])
                  (let* ((val (vector-ref prev col))
                         (cand (- (vector-ref right (+ col 1)) 1))
                         (best (if (> val cand) val cand)))
                    (vector-set! right col best)))
                ;; compute DP for current row
                (define nxt (make-vector n))
                (for ([col (in-range n)])
                  (let* ((best (max (vector-ref left col)
                                    (vector-ref right col)))
                         (new (+ (vector-ref curr-row col) best)))
                    (vector-set! nxt col new)))
                (loop (+ i 1) nxt)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_points/1]).

-spec max_points(Points :: [[integer()]]) -> integer().
max_points([]) ->
    0;
max_points([FirstRow | RestRows]) ->
    DP0 = FirstRow,
    DPFinal = lists:foldl(
        fun(Row, PrevDP) ->
            Left = left_max(PrevDP),
            Right = right_max(PrevDP),
            combine(Row, Left, Right)
        end,
        DP0,
        RestRows
    ),
    lists:max(DPFinal).

left_max(List) ->
    {_, Rev} = lists:foldl(
        fun(H, {undefined, Acc}) ->
                {H, [H | Acc]};
           (H, {PrevBest, Acc}) ->
                NewBest = erlang:max(H, PrevBest - 1),
                {NewBest, [NewBest | Acc]}
        end,
        {undefined, []},
        List
    ),
    lists:reverse(Rev).

right_max(List) ->
    {_, Res} = lists:foldr(
        fun(H, {undefined, Acc}) ->
                {H, [H | Acc]};
           (H, {PrevBest, Acc}) ->
                NewBest = erlang:max(H, PrevBest - 1),
                {NewBest, [NewBest | Acc]}
        end,
        {undefined, []},
        List
    ),
    Res.

combine([], [], []) -> [];
combine([R | Rs], [L | Ls], [Rt | Rts]) ->
    MaxPrev = erlang:max(L, Rt),
    [R + MaxPrev | combine(Rs, Ls, Rts)].
```

## Elixir

```elixir
defmodule Solution do
  @spec max_points(points :: [[integer]]) :: integer
  def max_points(points) do
    [first_row | rest_rows] = points

    final_dp =
      Enum.reduce(rest_rows, first_row, fn cur_row, prev_dp ->
        left = compute_left(prev_dp)
        right = compute_right(prev_dp)

        List.zip([left, right, cur_row])
        |> Enum.map(fn {l, r, c} -> max(l, r) + c end)
      end)

    Enum.max(final_dp)
  end

  defp compute_left(prev) do
    {rev_res, _} =
      Enum.reduce(Enum.with_index(prev), {[], nil}, fn {val, idx}, {acc, prev_val} ->
        if idx == 0 do
          {[val | acc], val}
        else
          cur = max(val, prev_val - 1)
          {[cur | acc], cur}
        end
      end)

    Enum.reverse(rev_res)
  end

  defp compute_right(prev) do
    rev = Enum.reverse(prev)

    {res, _} =
      Enum.reduce(Enum.with_index(rev), {[], nil}, fn {val, idx}, {acc, prev_val} ->
        if idx == 0 do
          {[val | acc], val}
        else
          cur = max(val, prev_val - 1)
          {[cur | acc], cur}
        end
      end)

    res
  end
end
```

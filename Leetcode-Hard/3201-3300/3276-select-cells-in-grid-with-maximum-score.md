# 3276. Select Cells in Grid With Maximum Score

## Cpp

```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& grid) {
        int m = grid.size();          // rows
        int n = grid[0].size();       // columns
        int R = m;
        int C = n;
        // Ensure we iterate over the smaller dimension for mask size to keep DP small
        if (R > C) { // transpose to make rows <= columns
            vector<vector<int>> trans(C, vector<int>(R));
            for (int i = 0; i < R; ++i)
                for (int j = 0; j < C; ++j)
                    trans[j][i] = grid[i][j];
            grid.swap(trans);
            swap(R, C);
        }
        int maxMask = 1 << R;
        vector<int> dp(maxMask, INT_MIN);
        dp[0] = 0;
        for (int col = 0; col < C; ++col) {
            vector<int> ndp = dp; // option to skip this column
            for (int mask = 0; mask < maxMask; ++mask) {
                if (dp[mask] == INT_MIN) continue;
                for (int row = 0; row < R; ++row) {
                    if (!(mask & (1 << row))) {
                        int nmask = mask | (1 << row);
                        ndp[nmask] = max(ndp[nmask], dp[mask] + grid[row][col]);
                    }
                }
            }
            dp.swap(ndp);
        }
        int ans = 0;
        for (int mask = 1; mask < maxMask; ++mask) {
            ans = max(ans, dp[mask]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxScore(java.util.List<java.util.List<Integer>> grid) {
        int m = grid.size();
        int n = grid.get(0).size();
        int[][] a = new int[m][n];
        for (int i = 0; i < m; i++) {
            java.util.List<Integer> row = grid.get(i);
            for (int j = 0; j < n; j++) {
                a[i][j] = row.get(j);
            }
        }

        int maxMask = 1 << m;
        int[] dp = new int[maxMask];
        java.util.Arrays.fill(dp, Integer.MIN_VALUE / 2);
        dp[0] = 0;

        for (int col = 0; col < n; col++) {
            int[] ndp = dp.clone(); // option to skip this column
            for (int mask = 0; mask < maxMask; mask++) {
                if (dp[mask] < 0) continue;
                for (int row = 0; row < m; row++) {
                    if ((mask & (1 << row)) == 0) {
                        int newMask = mask | (1 << row);
                        ndp[newMask] = Math.max(ndp[newMask], dp[mask] + a[row][col]);
                    }
                }
            }
            dp = ndp;
        }

        int ans = 0;
        for (int val : dp) {
            if (val > ans) ans = val;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)          # rows
        n = len(grid[0])       # columns
        size = 1 << m
        NEG_INF = -10**9
        dp = [NEG_INF] * size
        dp[0] = 0

        for c in range(n):
            newdp = dp[:]  # option to skip this column
            for mask in range(size):
                if dp[mask] == NEG_INF:
                    continue
                # try to pick a row not used yet for this column
                available = (~mask) & (size - 1)
                r = 0
                while available:
                    if available & 1:
                        newmask = mask | (1 << r)
                        val = dp[mask] + grid[r][c]
                        if val > newdp[newmask]:
                            newdp[newmask] = val
                    available >>= 1
                    r += 1
            dp = newdp

        return max(dp)
```

## Python3

```python
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # Ensure we iterate over rows and mask columns (n <= 10)
        dp = [-10**9] * (1 << n)
        dp[0] = 0
        for i in range(m):
            ndp = dp[:]  # option to skip this row
            for mask in range(1 << n):
                cur = dp[mask]
                if cur < 0:
                    continue
                # try picking a column not used yet
                avail = (~mask) & ((1 << n) - 1)
                while avail:
                    lsb = avail & -avail
                    j = (lsb.bit_length() - 1)
                    new_mask = mask | lsb
                    val = cur + grid[i][j]
                    if val > ndp[new_mask]:
                        ndp[new_mask] = val
                    avail ^= lsb
            dp = ndp
        return max(dp)
```

## C

```c
#include <stdlib.h>
#include <string.h>

int maxScore(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = gridColSize[0];
    int maxMask = 1 << rows;
    const int NEG_INF = -1000000000;

    int *dp = (int *)malloc(sizeof(int) * maxMask);
    int *newdp = (int *)malloc(sizeof(int) * maxMask);

    for (int mask = 0; mask < maxMask; ++mask) dp[mask] = NEG_INF;
    dp[0] = 0;

    for (int c = 0; c < cols; ++c) {
        memcpy(newdp, dp, sizeof(int) * maxMask); // skip this column
        for (int r = 0; r < rows; ++r) {
            int val = grid[r][c];
            for (int mask = 0; mask < maxMask; ++mask) {
                if (dp[mask] == NEG_INF) continue;
                if ((mask & (1 << r)) == 0) {
                    int nmask = mask | (1 << r);
                    int cand = dp[mask] + val;
                    if (cand > newdp[nmask]) newdp[nmask] = cand;
                }
            }
        }
        int *tmp = dp;
        dp = newdp;
        newdp = tmp;
    }

    int ans = 0;
    for (int mask = 0; mask < maxMask; ++mask) {
        if (dp[mask] > ans) ans = dp[mask];
    }

    free(dp);
    free(newdp);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxScore(IList<IList<int>> grid) {
        int rows = grid.Count;
        int cols = grid[0].Count;
        int maxMask = 1 << rows;
        const int NEG_INF = int.MinValue / 2;
        int[] dp = new int[maxMask];
        for (int i = 0; i < maxMask; i++) dp[i] = NEG_INF;
        dp[0] = 0;

        for (int c = 0; c < cols; c++) {
            int[] ndp = new int[maxMask];
            Array.Copy(dp, ndp, maxMask); // case of not picking any cell in this column
            for (int mask = 0; mask < maxMask; mask++) {
                if (dp[mask] == NEG_INF) continue;
                for (int r = 0; r < rows; r++) {
                    int bit = 1 << r;
                    if ((mask & bit) != 0) continue; // row already used
                    int newMask = mask | bit;
                    int val = dp[mask] + grid[r][c];
                    if (val > ndp[newMask]) ndp[newMask] = val;
                }
            }
            dp = ndp;
        }

        int ans = 0;
        for (int m = 0; m < maxMask; m++) {
            if (dp[m] > ans) ans = dp[m];
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxScore = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const maskSize = 1 << rows;
    const NEG_INF = -1e15;
    
    let dp = new Array(maskSize).fill(NEG_INF);
    dp[0] = 0; // no row selected yet
    
    for (let c = 0; c < cols; ++c) {
        const ndp = dp.slice(); // copy to allow skipping this column
        for (let mask = 0; mask < maskSize; ++mask) {
            if (dp[mask] === NEG_INF) continue;
            for (let r = 0; r < rows; ++r) {
                if ((mask >> r) & 1) continue; // row already used
                const nMask = mask | (1 << r);
                const val = dp[mask] + grid[r][c];
                if (val > ndp[nMask]) ndp[nMask] = val;
            }
        }
        dp = ndp;
    }
    
    let ans = 0;
    for (let mask = 1; mask < maskSize; ++mask) {
        if (dp[mask] > ans) ans = dp[mask];
    }
    return ans;
};
```

## Typescript

```typescript
function maxScore(grid: number[][]): number {
    let rows = grid.length;
    let cols = grid[0].length;

    // Ensure we mask over the smaller dimension to keep 2^k manageable
    if (rows > cols) {
        const transposed: number[][] = Array.from({ length: cols }, (_, c) =>
            Array.from({ length: rows }, (_, r) => grid[r][c])
        );
        [rows, cols] = [cols, rows];
        grid = transposed;
    }

    const totalMask = 1 << rows;
    let dp = new Array(totalMask).fill(0);

    for (let c = 0; c < cols; ++c) {
        const ndp = dp.slice(); // case of skipping this column
        for (let mask = 0; mask < totalMask; ++mask) {
            const cur = dp[mask];
            let avail = (~mask) & (totalMask - 1); // rows not yet used
            while (avail) {
                const lsb = avail & -avail;
                const r = Math.log2(lsb) | 0; // row index
                const newMask = mask | lsb;
                const val = cur + grid[r][c];
                if (val > ndp[newMask]) ndp[newMask] = val;
                avail ^= lsb;
            }
        }
        dp = ndp;
    }

    let ans = 0;
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
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxScore($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);

        // Ensure rows <= cols to keep mask size minimal
        if ($rows > $cols) {
            $transposed = [];
            for ($c = 0; $c < $cols; $c++) {
                $newRow = [];
                for ($r = 0; $r < $rows; $r++) {
                    $newRow[] = $grid[$r][$c];
                }
                $transposed[] = $newRow;
            }
            $grid = $transposed;
            $tmp   = $rows;
            $rows  = $cols;
            $cols  = $tmp;
        }

        $size = 1 << $rows;
        $negInf = -PHP_INT_MAX;
        $dp = array_fill(0, $size, $negInf);
        $dp[0] = 0;

        for ($c = 0; $c < $cols; $c++) {
            $old = $dp; // snapshot before processing this column
            for ($r = 0; $r < $rows; $r++) {
                $val = $grid[$r][$c];
                $bit = 1 << $r;
                for ($mask = 0; $mask < $size; $mask++) {
                    if (($mask & $bit) === 0 && $old[$mask] !== $negInf) {
                        $newMask = $mask | $bit;
                        $candidate = $old[$mask] + $val;
                        if ($candidate > $dp[$newMask]) {
                            $dp[$newMask] = $candidate;
                        }
                    }
                }
            }
        }

        $ans = 0;
        for ($mask = 1; $mask < $size; $mask++) {
            if ($dp[$mask] > $ans) {
                $ans = $dp[$mask];
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        let cols = grid[0].count
        let fullMask = 1 << cols
        var dp = Array(repeating: Int.min / 2, count: fullMask)
        dp[0] = 0
        
        for i in 0..<rows {
            var newDP = dp
            for mask in 0..<fullMask {
                let cur = dp[mask]
                if cur < 0 { continue }
                var available = (~mask) & (fullMask - 1)
                while available != 0 {
                    let lsb = available & -available
                    let col = lsb.trailingZeroBitCount
                    let newMask = mask | (1 << col)
                    let val = cur + grid[i][col]
                    if val > newDP[newMask] {
                        newDP[newMask] = val
                    }
                    available ^= lsb
                }
            }
            dp = newDP
        }
        return dp.max()!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(grid: List<List<Int>>): Int {
        val rows = grid.size
        val cols = grid[0].size
        var dp = IntArray(1 shl cols) { Int.MIN_VALUE / 4 }
        dp[0] = 0
        for (i in 0 until rows) {
            val next = dp.clone()
            for (mask in 0 until (1 shl cols)) {
                val cur = dp[mask]
                if (cur < 0) continue
                for (j in 0 until cols) {
                    if ((mask and (1 shl j)) == 0) {
                        val nMask = mask or (1 shl j)
                        val cand = cur + grid[i][j]
                        if (cand > next[nMask]) next[nMask] = cand
                    }
                }
            }
            dp = next
        }
        var ans = 0
        for (v in dp) {
            if (v > ans) ans = v
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxScore(List<List<int>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    int maxMask = 1 << cols;
    const int NEG = -1000000000; // sufficiently small
    List<int> dp = List.filled(maxMask, NEG);
    dp[0] = 0;

    for (int r = 0; r < rows; r++) {
      List<int> ndp = List.from(dp); // allow skipping this row
      for (int mask = 0; mask < maxMask; mask++) {
        int cur = dp[mask];
        if (cur == NEG) continue;
        for (int c = 0; c < cols; c++) {
          if ((mask & (1 << c)) == 0) {
            int newMask = mask | (1 << c);
            ndp[newMask] = max(ndp[newMask], cur + grid[r][c]);
          }
        }
      }
      dp = ndp;
    }

    int ans = 0;
    for (int v in dp) {
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
	"sort"
)

func maxScore(grid [][]int) int {
	R := len(grid)
	if R == 0 {
		return 0
	}
	C := len(grid[0])

	type Cell struct {
		val int
		row int
	}
	cells := make([]Cell, 0, R*C)
	for i := 0; i < R; i++ {
		for j := 0; j < C; j++ {
			cells = append(cells, Cell{val: grid[i][j], row: i})
		}
	}

	sort.Slice(cells, func(i, j int) bool {
		return cells[i].val < cells[j].val
	})

	size := 1 << R
	const negInf = -1 << 60

	dp := make([]int, size)
	for i := range dp {
		dp[i] = negInf
	}
	dp[0] = 0

	idx := 0
	for idx < len(cells) {
		curVal := cells[idx].val
		prev := make([]int, size)
		copy(prev, dp)

		for idx < len(cells) && cells[idx].val == curVal {
			r := cells[idx].row
			bit := 1 << r
			for mask := 0; mask < size; mask++ {
				if prev[mask] == negInf {
					continue
				}
				if mask&bit == 0 {
					newMask := mask | bit
					sum := prev[mask] + curVal
					if sum > dp[newMask] {
						dp[newMask] = sum
					}
				}
			}
			idx++
		}
	}

	ans := 0
	for mask := 1; mask < size; mask++ {
		if dp[mask] > ans {
			ans = dp[mask]
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_score(grid)
  n = grid.size
  m = grid[0].size

  # Ensure we mask the smaller dimension for efficiency
  if n > m
    transposed = Array.new(m) { |i| Array.new(n) { |j| grid[j][i] } }
    grid = transposed
    n, m = m, n
  end

  max_mask = 1 << n
  dp = Array.new(max_mask, -Float::INFINITY)
  dp[0] = 0

  (0...m).each do |col|
    ndp = dp.clone
    (0...max_mask).each do |mask|
      cur = dp[mask]
      next if cur == -Float::INFINITY
      n.times do |row|
        bit = 1 << row
        next if (mask & bit) != 0
        new_mask = mask | bit
        val = cur + grid[row][col]
        ndp[new_mask] = val if val > ndp[new_mask]
      end
    end
    dp = ndp
  end

  dp.max.to_i
end
```

## Scala

```scala
object Solution {
  def maxScore(grid: List[List[Int]]): Int = {
    val rows = grid.length
    val cols = if (rows == 0) 0 else grid.head.length
    val mat = Array.ofDim[Int](rows, cols)
    for (i <- 0 until rows) {
      val rowArr = grid(i).toArray
      System.arraycopy(rowArr, 0, mat(i), 0, cols)
    }

    val maxMask = 1 << rows
    var dp = Array.fill(maxMask)(Int.MinValue / 2)
    dp(0) = 0

    for (c <- 0 until cols) {
      val ndp = dp.clone()
      for (mask <- 0 until maxMask) {
        val cur = dp(mask)
        if (cur > Int.MinValue / 4) {
          var r = 0
          while (r < rows) {
            if ((mask & (1 << r)) == 0) {
              val newMask = mask | (1 << r)
              val cand = cur + mat(r)(c)
              if (cand > ndp(newMask)) ndp(newMask) = cand
            }
            r += 1
          }
        }
      }
      dp = ndp
    }

    dp.max
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mask_size = 1usize << rows;
        const NEG_INF: i32 = -1_000_000_000;
        let mut dp = vec![NEG_INF; mask_size];
        dp[0] = 0;
        for c in 0..cols {
            let mut ndp = dp.clone(); // skipping this column
            for mask in 0..mask_size {
                if dp[mask] == NEG_INF {
                    continue;
                }
                for r in 0..rows {
                    if (mask >> r) & 1 == 0 {
                        let new_mask = mask | (1 << r);
                        let val = dp[mask] + grid[r][c];
                        if val > ndp[new_mask] {
                            ndp[new_mask] = val;
                        }
                    }
                }
            }
            dp = ndp;
        }
        *dp.iter().max().unwrap()
    }
}
```

## Racket

```racket
(define/contract (max-score grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (null? grid) 0 (length (car grid))))
         (size (expt 2 cols))
         (neg-inf -1000000000)
         (dp (make-vector size neg-inf)))
    (vector-set! dp 0 0)
    (for ([i rows])
      (let ((newdp (vector-copy dp))) ; keep the option of skipping this row
        (for ([mask size])
          (define cur (vector-ref dp mask))
          (when (> cur neg-inf)               ; reachable state
            (for ([j cols])
              (let ((bit (arithmetic-shift 1 j)))
                (when (= 0 (bitwise-and mask bit)) ; column j not used yet
                  (let* ((newmask (bitwise-ior mask bit))
                         (val (+ cur (list-ref (list-ref grid i) j))))
                    (when (> val (vector-ref newdp newmask))
                      (vector-set! newdp newmask val)))))))))
        (set! dp newdp)))
    ;; answer is the maximum over all masks
    (let loop ((m 0) (best neg-inf))
      (if (= m size)
          best
          (loop (+ m 1) (max best (vector-ref dp m)))))))
```

## Erlang

```erlang
-spec max_score(Grid :: [[integer()]]) -> integer().
max_score(Grid) ->
    R = length(Grid),
    C = length(hd(Grid)),
    Columns = build_columns(Grid, C),
    DP0 = #{0 => 0},
    FinalDP = lists:foldl(fun(ColVals, AccDP) -> process_column(ColVals, AccDP, R) end,
                          DP0, Columns),
    maps:fold(fun(_Mask, Score, MaxAcc) ->
                      if Score > MaxAcc -> Score; true -> MaxAcc end
              end, 0, FinalDP).

%% Build list of columns, each column is a list of values per row (top to bottom)
build_columns(_Grid, 0) -> [];
build_columns(Grid, ColIdx) when ColIdx > 0 ->
    ColVals = [lists:nth(ColIdx, Row) || Row <- Grid],
    Rest = build_columns(Grid, ColIdx - 1),
    [ColVals | Rest].

%% Process one column: try to add a cell from this column for each unused row.
process_column(ColVals, DP, R) ->
    %% Start with existing DP (skip this column)
    maps:fold(
      fun(Mask, Score, AccDP) ->
          lists:foldl(
            fun(RowIdx, InnerAcc) ->
                Bit = 1 bsl RowIdx,
                case Mask band Bit of
                    0 ->
                        NewMask = Mask bor Bit,
                        Val = lists:nth(RowIdx + 1, ColVals),
                        NewScore = Score + Val,
                        Existing = maps:get(NewMask, InnerAcc, -1000000),
                        if NewScore > Existing ->
                               maps:put(NewMask, NewScore, InnerAcc);
                           true -> InnerAcc
                        end;
                    _ -> InnerAcc
                end
            end,
            AccDP,
            lists:seq(0, R - 1))
      end,
      DP,
      DP).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(grid :: [[integer]]) :: integer
  def max_score(grid) do
    import Bitwise

    rows = length(grid)
    cols = length(hd(grid))

    {m, n, mat} =
      if rows <= cols do
        {rows, cols, grid}
      else
        # transpose to make number of rows <= columns for smaller mask size
        transposed = for j <- 0..(cols - 1) do
          for i <- 0..(rows - 1), do: Enum.at(grid, i) |> Enum.at(j)
        end
        {cols, rows, transposed}
      end

    max_mask = 1 <<< m
    dp = %{0 => 0}

    Enum.reduce(0..(n - 1), dp, fn col, cur_dp ->
      new_dp = Map.clone(cur_dp)

      for {mask, val} <- cur_dp do
        # try to pick a row not yet used in this mask
        0..(m - 1)
        |> Enum.each(fn row ->
          if (mask &&& (1 <<< row)) == 0 do
            new_mask = mask ||| (1 <<< row)
            sum = val + Enum.at(Enum.at(mat, row), col)
            prev = Map.get(new_dp, new_mask, -1_000_000)
            if sum > prev do
              new_dp = Map.put(new_dp, new_mask, sum)
            else
              new_dp = new_dp
            end
          end
        end)
      end

      new_dp
    end)
    |> Map.values()
    |> Enum.max()
  end
end
```

# 2304. Minimum Path Cost in a Grid

## Cpp

```cpp
class Solution {
public:
    int minPathCost(vector<vector<int>>& grid, vector<vector<int>>& moveCost) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> dpPrev(n);
        for (int j = 0; j < n; ++j) {
            dpPrev[j] = grid[0][j];
        }
        for (int i = 1; i < m; ++i) {
            vector<int> dpCurr(n, INT_MAX);
            for (int j = 0; j < n; ++j) { // current column
                int cellVal = grid[i][j];
                int best = INT_MAX;
                for (int k = 0; k < n; ++k) { // previous column
                    int prevVal = dpPrev[k];
                    int cost = moveCost[grid[i-1][k]][j];
                    if (prevVal + cost < best) {
                        best = prevVal + cost;
                    }
                }
                dpCurr[j] = cellVal + best;
            }
            dpPrev.swap(dpCurr);
        }
        return *min_element(dpPrev.begin(), dpPrev.end());
    }
};
```

## Java

```java
class Solution {
    public int minPathCost(int[][] grid, int[][] moveCost) {
        int m = grid.length;
        int n = grid[0].length;
        int[] dp = new int[n];
        for (int j = 0; j < n; j++) {
            dp[j] = grid[0][j];
        }
        for (int i = 1; i < m; i++) {
            int[] ndp = new int[n];
            java.util.Arrays.fill(ndp, Integer.MAX_VALUE);
            for (int cur = 0; cur < n; cur++) {
                int cellVal = grid[i][cur];
                int best = Integer.MAX_VALUE;
                for (int prev = 0; prev < n; prev++) {
                    if (dp[prev] == Integer.MAX_VALUE) continue;
                    int move = moveCost[grid[i - 1][prev]][cur];
                    int total = dp[prev] + move + cellVal;
                    if (total < best) best = total;
                }
                ndp[cur] = best;
            }
            dp = ndp;
        }
        int ans = Integer.MAX_VALUE;
        for (int v : dp) {
            if (v < ans) ans = v;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # dp for the first row is just the cell values
        prev = [grid[0][j] for j in range(n)]
        for i in range(1, m):
            cur = [float('inf')] * n
            for j in range(n):  # column in current row
                cell_val = grid[i][j]
                best = float('inf')
                for k in range(n):  # column in previous row
                    cost = prev[k] + moveCost[grid[i-1][k]][j]
                    if cost < best:
                        best = cost
                cur[j] = cell_val + best
            prev = cur
        return min(prev)
```

## Python3

```python
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [row[:] for row in grid]  # copy first row values; will be overwritten later
        # Initialize first row dp as just the cell values
        dp[0] = grid[0][:]
        for i in range(1, m):
            new_row = [float('inf')] * n
            for j in range(n):  # target column in current row
                cur_val = grid[i][j]
                best = float('inf')
                for k in range(n):  # source column from previous row
                    cost = dp[i-1][k] + moveCost[grid[i-1][k]][j]
                    if cost < best:
                        best = cost
                new_row[j] = cur_val + best
            dp[i] = new_row
        return min(dp[m-1])
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int minPathCost(int** grid, int gridSize, int* gridColSize, int** moveCost, int moveCostSize, int* moveCostColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    
    // Allocate DP array
    int **dp = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        dp[i] = (int *)malloc(n * sizeof(int));
    }
    
    // Initialize first row
    for (int j = 0; j < n; ++j) {
        dp[0][j] = grid[0][j];
    }
    
    // DP transition
    for (int i = 1; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int best = INT_MAX;
            for (int k = 0; k < n; ++k) {
                int prevVal = grid[i - 1][k];
                int cand = dp[i - 1][k] + moveCost[prevVal][j];
                if (cand < best) best = cand;
            }
            dp[i][j] = grid[i][j] + best;
        }
    }
    
    // Find answer in last row
    int ans = INT_MAX;
    for (int j = 0; j < n; ++j) {
        if (dp[m - 1][j] < ans) ans = dp[m - 1][j];
    }
    
    // Free memory
    for (int i = 0; i < m; ++i) {
        free(dp[i]);
    }
    free(dp);
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinPathCost(int[][] grid, int[][] moveCost) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[,] dp = new int[m, n];
        // Initialize first row
        for (int j = 0; j < n; ++j) {
            dp[0, j] = grid[0][j];
        }
        // DP transition
        for (int i = 1; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int best = int.MaxValue;
                for (int k = 0; k < n; ++k) {
                    int prevVal = dp[i - 1, k];
                    int cost = moveCost[grid[i - 1][k]][j];
                    if (prevVal + cost < best) {
                        best = prevVal + cost;
                    }
                }
                dp[i, j] = grid[i][j] + best;
            }
        }
        // Find minimum in last row
        int answer = int.MaxValue;
        for (int j = 0; j < n; ++j) {
            if (dp[m - 1, j] < answer) answer = dp[m - 1, j];
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number[][]} moveCost
 * @return {number}
 */
var minPathCost = function(grid, moveCost) {
    const m = grid.length;
    const n = grid[0].length;
    let dp = new Array(n);
    for (let j = 0; j < n; ++j) {
        dp[j] = grid[0][j];
    }
    for (let i = 1; i < m; ++i) {
        const next = new Array(n).fill(Infinity);
        for (let prev = 0; prev < n; ++prev) {
            const valPrev = grid[i - 1][prev];
            const base = dp[prev];
            for (let cur = 0; cur < n; ++cur) {
                const cost = base + moveCost[valPrev][cur] + grid[i][cur];
                if (cost < next[cur]) next[cur] = cost;
            }
        }
        dp = next;
    }
    return Math.min(...dp);
};
```

## Typescript

```typescript
function minPathCost(grid: number[][], moveCost: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let dpPrev = new Array<number>(n);
    for (let j = 0; j < n; ++j) {
        dpPrev[j] = grid[0][j];
    }
    for (let i = 1; i < m; ++i) {
        const dpCurr = new Array<number>(n).fill(Infinity);
        for (let j = 0; j < n; ++j) {
            let best = Infinity;
            for (let k = 0; k < n; ++k) {
                const cost = dpPrev[k] + moveCost[grid[i - 1][k]][j];
                if (cost < best) best = cost;
            }
            dpCurr[j] = grid[i][j] + best;
        }
        dpPrev = dpCurr;
    }
    return Math.min(...dpPrev);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer[][] $moveCost
     * @return Integer
     */
    function minPathCost($grid, $moveCost) {
        $m = count($grid);
        $n = count($grid[0]);
        // Initialize dp with the first row values
        $dp = [];
        for ($j = 0; $j < $n; $j++) {
            $dp[$j] = $grid[0][$j];
        }
        // Process subsequent rows
        for ($i = 1; $i < $m; $i++) {
            $new = array_fill(0, $n, PHP_INT_MAX);
            for ($j = 0; $j < $n; $j++) { // target column in current row
                $minPrev = PHP_INT_MAX;
                for ($k = 0; $k < $n; $k++) { // source column from previous row
                    $prevVal = $grid[$i - 1][$k];
                    $candidate = $dp[$k] + $moveCost[$prevVal][$j];
                    if ($candidate < $minPrev) {
                        $minPrev = $candidate;
                    }
                }
                $new[$j] = $grid[$i][$j] + $minPrev;
            }
            $dp = $new;
        }
        return min($dp);
    }
}
```

## Swift

```swift
class Solution {
    func minPathCost(_ grid: [[Int]], _ moveCost: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var dpPrev = grid[0]
        for i in 1..<m {
            var dpCurr = Array(repeating: Int.max, count: n)
            for j in 0..<n {
                var best = Int.max
                for k in 0..<n {
                    let total = dpPrev[k] + moveCost[grid[i-1][k]][j]
                    if total < best {
                        best = total
                    }
                }
                dpCurr[j] = grid[i][j] + best
            }
            dpPrev = dpCurr
        }
        return dpPrev.min()!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minPathCost(grid: Array<IntArray>, moveCost: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var dpPrev = IntArray(n) { idx -> grid[0][idx] }
        for (i in 1 until m) {
            val dpCurr = IntArray(n) { Int.MAX_VALUE / 2 }
            for (c in 0 until n) {
                var best = Int.MAX_VALUE / 2
                for (p in 0 until n) {
                    val cost = dpPrev[p] + moveCost[grid[i - 1][p]][c]
                    if (cost < best) best = cost
                }
                dpCurr[c] = grid[i][c] + best
            }
            dpPrev = dpCurr
        }
        var answer = Int.MAX_VALUE
        for (v in dpPrev) {
            if (v < answer) answer = v
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minPathCost(List<List<int>> grid, List<List<int>> moveCost) {
    int m = grid.length;
    int n = grid[0].length;

    // dpPrev[j] = minimum cost to reach cell (i-1, j)
    List<int> dpPrev = List.filled(n, 0);
    for (int j = 0; j < n; ++j) {
      dpPrev[j] = grid[0][j];
    }

    // Process each subsequent row
    for (int i = 1; i < m; ++i) {
      List<int> dpCurr = List.filled(n, 1 << 60);
      for (int prevCol = 0; prevCol < n; ++prevCol) {
        int prevCost = dpPrev[prevCol];
        int prevVal = grid[i - 1][prevCol];
        for (int curCol = 0; curCol < n; ++curCol) {
          int cost = prevCost + moveCost[prevVal][curCol] + grid[i][curCol];
          if (cost < dpCurr[curCol]) {
            dpCurr[curCol] = cost;
          }
        }
      }
      dpPrev = dpCurr;
    }

    // Minimum cost among the last row cells
    int answer = dpPrev[0];
    for (int v in dpPrev) {
      if (v < answer) answer = v;
    }
    return answer;
  }
}
```

## Golang

```go
func minPathCost(grid [][]int, moveCost [][]int) int {
	m := len(grid)
	n := len(grid[0])

	// dpPrev holds minimal cost to reach each cell in the previous row
	dpPrev := make([]int, n)
	for j := 0; j < n; j++ {
		dpPrev[j] = grid[0][j]
	}

	maxInt := int(^uint(0) >> 1)

	for i := 1; i < m; i++ {
		dpCurr := make([]int, n)
		for j := 0; j < n; j++ {
			best := maxInt
			for k := 0; k < n; k++ {
				cost := dpPrev[k] + moveCost[grid[i-1][k]][j]
				if cost < best {
					best = cost
				}
			}
			dpCurr[j] = grid[i][j] + best
		}
		dpPrev = dpCurr
	}

	ans := dpPrev[0]
	for _, v := range dpPrev {
		if v < ans {
			ans = v
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_path_cost(grid, move_cost)
  m = grid.length
  n = grid[0].length
  dp = Array.new(n) { |j| grid[0][j] }

  (1...m).each do |i|
    new_dp = Array.new(n, Float::INFINITY)
    n.times do |k|
      best = Float::INFINITY
      n.times do |j|
        cost = dp[j] + move_cost[grid[i - 1][j]][k]
        best = cost if cost < best
      end
      new_dp[k] = best + grid[i][k]
    end
    dp = new_dp
  end

  dp.min
end
```

## Scala

```scala
object Solution {
    def minPathCost(grid: Array[Array[Int]], moveCost: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        var dpPrev = new Array[Int](n)
        for (j <- 0 until n) {
            dpPrev(j) = grid(0)(j)
        }
        for (i <- 1 until m) {
            val dpCurr = new Array[Int](n)
            java.util.Arrays.fill(dpCurr, Int.MaxValue / 2)
            for (k <- 0 until n) {
                var best = Int.MaxValue / 2
                for (j <- 0 until n) {
                    val cost = dpPrev(j) + moveCost(grid(i - 1)(j))(k)
                    if (cost < best) best = cost
                }
                dpCurr(k) = best + grid(i)(k)
            }
            dpPrev = dpCurr
        }
        var ans = Int.MaxValue
        for (v <- dpPrev) {
            if (v < ans) ans = v
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_path_cost(grid: Vec<Vec<i32>>, move_cost: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        // dp holds minimal cost to reach each cell in the current row
        let mut dp = vec![0i32; n];
        for j in 0..n {
            dp[j] = grid[0][j];
        }

        for r in 1..m {
            let mut new_dp = vec![i32::MAX / 2; n];
            for prev_c in 0..n {
                let prev_cost = dp[prev_c];
                let val_at_prev = grid[r - 1][prev_c] as usize;
                for cur_c in 0..n {
                    let total = prev_cost
                        + move_cost[val_at_prev][cur_c]
                        + grid[r][cur_c];
                    if total < new_dp[cur_c] {
                        new_dp[cur_c] = total;
                    }
                }
            }
            dp = new_dp;
        }

        *dp.iter().min().unwrap()
    }
}
```

## Racket

```racket
(define/contract (min-path-cost grid moveCost)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      exact-integer?)
  (let* ((m (length grid))
         (n (length (first grid)))
         (initial-dp (map (lambda (v) v) (first grid))))
    (let loop ((row 1) (prev-dp initial-dp))
      (if (= row m)
          (apply min prev-dp)
          (let* ((prev-row (list-ref grid (- row 1)))
                 (curr-row (list-ref grid row))
                 (new-dp
                  (for/list ([j (in-range n)])
                    (define cell-val (list-ref curr-row j))
                    (define best
                      (apply min
                             (for/list ([k (in-range n)])
                               (+ (list-ref prev-dp k)
                                  (list-ref (list-ref moveCost (list-ref prev-row k)) j)))))
                    (+ cell-val best))))
            (loop (+ row 1) new-dp))))))
```

## Erlang

```erlang
-spec min_path_cost(Grid :: [[integer()]], MoveCost :: [[integer()]]) -> integer().
min_path_cost(Grid, MoveCost) ->
    [FirstRow|RestRows] = Grid,
    DP0 = FirstRow,
    process_rows(RestRows, DP0, FirstRow, MoveCost).

process_rows([], DP, _PrevVals, _MoveCost) ->
    lists:min(DP);
process_rows([CurrRow|Rest], PrevDP, PrevVals, MoveCost) ->
    N = length(CurrRow),
    Indices = lists:seq(0, N-1),
    NewDP = [calc_min_cost(K, CurrVal, PrevDP, PrevVals, MoveCost)
             || {K, CurrVal} <- lists:zip(Indices, CurrRow)],
    process_rows(Rest, NewDP, CurrRow, MoveCost).

calc_min_cost(K, CurrVal, PrevDP, PrevVals, MoveCost) ->
    PrevList = lists:zip(PrevDP, PrevVals),
    Costs = [PrevCost + move_cost(PrevVal, K, MoveCost) + CurrVal
             || {PrevCost, PrevVal} <- PrevList],
    lists:min(Costs).

move_cost(Value, K, MoveCost) ->
    Row = lists:nth(Value+1, MoveCost),
    lists:nth(K+1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_path_cost(grid :: [[integer]], move_cost :: [[integer]]) :: integer
  def min_path_cost(grid, move_cost) do
    [first_row | rest] = grid
    dp0 = first_row

    {_, final_dp} =
      Enum.reduce(rest, {first_row, dp0}, fn cur_row, {prev_vals, prev_dp} ->
        n = length(cur_row)

        new_dp =
          for k <- 0..(n - 1) do
            cur_val = Enum.at(cur_row, k)

            min_cost =
              Enum.with_index(prev_vals)
              |> Enum.reduce(:infinity, fn {v_prev, j}, acc ->
                move_c = Enum.at(Enum.at(move_cost, v_prev), k)
                cost = Enum.at(prev_dp, j) + move_c + cur_val
                if cost < acc, do: cost, else: acc
              end)

            min_cost
          end

        {cur_row, new_dp}
      end)

    Enum.min(final_dp)
  end
end
```

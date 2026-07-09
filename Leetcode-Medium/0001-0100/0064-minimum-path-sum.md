# 0064. Minimum Path Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) continue;
                else if (i == 0) grid[i][j] += grid[i][j - 1];
                else if (j == 0) grid[i][j] += grid[i - 1][j];
                else grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]);
            }
        }
        return grid[m - 1][n - 1];
    }
};
```

## Java

```java
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        // Initialize first cell already contains its value
        // Fill first row
        for (int j = 1; j < n; ++j) {
            grid[0][j] += grid[0][j - 1];
        }
        // Fill first column
        for (int i = 1; i < m; ++i) {
            grid[i][0] += grid[i - 1][0];
        }
        // Fill rest of the grid
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
            }
        }
        return grid[m - 1][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]
```

## Python3

```python
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
```

## C

```c
int minPathSum(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0 || gridColSize == NULL) return 0;
    int m = gridSize;
    int n = gridColSize[0];
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) continue;
            else if (i == 0) {
                grid[i][j] += grid[i][j - 1];
            } else if (j == 0) {
                grid[i][j] += grid[i - 1][j];
            } else {
                int up = grid[i - 1][j];
                int left = grid[i][j - 1];
                grid[i][j] += (up < left ? up : left);
            }
        }
    }
    return grid[m - 1][n - 1];
}
```

## Csharp

```csharp
public class Solution
{
    public int MinPathSum(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i == 0 && j == 0) continue;
                else if (i == 0)
                    grid[i][j] += grid[i][j - 1];
                else if (j == 0)
                    grid[i][j] += grid[i - 1][j];
                else
                    grid[i][j] += Math.Min(grid[i - 1][j], grid[i][j - 1]);
            }
        }

        return grid[m - 1][n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            else if (i === 0) grid[i][j] += grid[i][j - 1];
            else if (j === 0) grid[i][j] += grid[i - 1][j];
            else grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
        }
    }
    return grid[m - 1][n - 1];
};
```

## Typescript

```typescript
function minPathSum(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            else if (i === 0) grid[i][j] += grid[i][j - 1];
            else if (j === 0) grid[i][j] += grid[i - 1][j];
            else grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
        }
    }

    return grid[m - 1][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minPathSum($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i === 0 && $j === 0) {
                    continue;
                } elseif ($i === 0) {
                    $grid[$i][$j] += $grid[$i][$j - 1];
                } elseif ($j === 0) {
                    $grid[$i][$j] += $grid[$i - 1][$j];
                } else {
                    $grid[$i][$j] += min($grid[$i - 1][$j], $grid[$i][$j - 1]);
                }
            }
        }
        return $grid[$m - 1][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var dp = Array(repeating: 0, count: n)
        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 {
                    dp[j] = grid[i][j]
                } else if i == 0 {
                    dp[j] = dp[j - 1] + grid[i][j]
                } else if j == 0 {
                    dp[j] = dp[j] + grid[i][j]
                } else {
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                }
            }
        }
        return dp[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minPathSum(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        for (i in 0 until m) {
            for (j in 0 until n) {
                when {
                    i == 0 && j == 0 -> {}
                    i == 0 -> grid[i][j] += grid[i][j - 1]
                    j == 0 -> grid[i][j] += grid[i - 1][j]
                    else -> grid[i][j] += kotlin.math.min(grid[i - 1][j], grid[i][j - 1])
                }
            }
        }
        return grid[m - 1][n - 1]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minPathSum(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i == 0 && j == 0) continue;
        if (i == 0) {
          grid[i][j] += grid[i][j - 1];
        } else if (j == 0) {
          grid[i][j] += grid[i - 1][j];
        } else {
          grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]);
        }
      }
    }

    return grid[m - 1][n - 1];
  }
}
```

## Golang

```go
func minPathSum(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			if i == 0 {
				grid[i][j] += grid[i][j-1]
			} else if j == 0 {
				grid[i][j] += grid[i-1][j]
			} else {
				if grid[i-1][j] < grid[i][j-1] {
					grid[i][j] += grid[i-1][j]
				} else {
					grid[i][j] += grid[i][j-1]
				}
			}
		}
	}
	return grid[m-1][n-1]
}
```

## Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def min_path_sum(grid)
  m = grid.size
  n = grid[0].size

  (0...m).each do |i|
    (0...n).each do |j|
      next if i == 0 && j == 0
      if i == 0
        grid[i][j] += grid[i][j - 1]
      elsif j == 0
        grid[i][j] += grid[i - 1][j]
      else
        grid[i][j] += [grid[i - 1][j], grid[i][j - 1]].min
      end
    end
  end

  grid[m - 1][n - 1]
end
```

## Scala

```scala
object Solution {
    def minPathSum(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (i == 0 && j == 0) {
                    // start cell, nothing to do
                } else if (i == 0) {
                    grid(i)(j) += grid(i)(j - 1)
                } else if (j == 0) {
                    grid(i)(j) += grid(i - 1)(j)
                } else {
                    grid(i)(j) += math.min(grid(i - 1)(j), grid(i)(j - 1))
                }
            }
        }

        grid(m - 1)(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let mut dp = grid;
        let m = dp.len();
        let n = dp[0].len();

        for i in 0..m {
            for j in 0..n {
                if i == 0 && j == 0 {
                    continue;
                } else if i == 0 {
                    dp[i][j] += dp[i][j - 1];
                } else if j == 0 {
                    dp[i][j] += dp[i - 1][j];
                } else {
                    let min_prev = if dp[i - 1][j] < dp[i][j - 1] { dp[i - 1][j] } else { dp[i][j - 1] };
                    dp[i][j] += min_prev;
                }
            }
        }

        dp[m - 1][n - 1]
    }
}
```

## Racket

```racket
(define/contract (min-path-sum grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (car grid))))
         (grid-vec (list->vector (map list->vector grid)))
         (dp (make-vector m)))
    ;; initialize dp rows
    (for ([i (in-range m)])
      (vector-set! dp i (make-vector n 0)))
    ;; fill dp
    (for ([i (in-range m)])
      (let ((row-dp (vector-ref dp i))
            (row-grid (vector-ref grid-vec i)))
        (for ([j (in-range n)])
          (define val (vector-ref row-grid j))
          (cond
            [(and (= i 0) (= j 0))
             (vector-set! row-dp j val)]
            [(= i 0)
             (vector-set! row-dp j (+ val (vector-ref row-dp (- j 1))))]
            [(= j 0)
             (let ((up (vector-ref (vector-ref dp (- i 1)) j)))
               (vector-set! row-dp j (+ val up)))]
            [else
             (let* ((up (vector-ref (vector-ref dp (- i 1)) j))
                    (left (vector-ref row-dp (- j 1))))
               (vector-set! row-dp j (+ val (if (< up left) up left))))])))))
    (vector-ref (vector-ref dp (- m 1)) (- n 1))))
```

## Erlang

```erlang
-module(solution).
-export([min_path_sum/1]).

-spec min_path_sum(Grid :: [[integer()]]) -> integer().
min_path_sum([]) ->
    0;
min_path_sum([FirstRow | RestRows]) ->
    FirstDP = prefix_sum(FirstRow),
    FinalDP = lists:foldl(fun(Row, PrevDP) -> process_row(Row, PrevDP) end,
                         FirstDP, RestRows),
    lists:last(FinalDP).

-spec prefix_sum([integer()]) -> [integer()].
prefix_sum(List) ->
    {Rev, _} = lists:foldl(
        fun(Val, {AccRev, Sum}) ->
            NewSum = Sum + Val,
            {[NewSum | AccRev], NewSum}
        end,
        {[], 0},
        List),
    lists:reverse(Rev).

-spec process_row([integer()], [integer()]) -> [integer()].
process_row(Row, PrevDP) ->
    {Rev, _} = lists:foldl(
        fun({Cell, Prev}, {AccRev, Left}) ->
            NewVal =
                case AccRev of
                    [] -> Cell + Prev;
                    _  -> erlang:min(Prev, Left) + Cell
                end,
            {[NewVal | AccRev], NewVal}
        end,
        {[], 0},
        lists:zip(Row, PrevDP)),
    lists:reverse(Rev).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_path_sum(grid :: [[integer]]) :: integer
  def min_path_sum(grid) do
    {final_dp, _} =
      grid
      |> Enum.with_index()
      |> Enum.reduce({[], nil}, fn {row, i}, {dp_prev, _} ->
        {rev_dp_cur, _} =
          row
          |> Enum.with_index()
          |> Enum.reduce({[], nil}, fn {val, j}, {rev_acc, left} ->
            new_val =
              cond do
                i == 0 and j == 0 -> val
                i == 0 -> left + val
                j == 0 -> Enum.at(dp_prev, 0) + val
                true -> min(Enum.at(dp_prev, j), left) + val
              end

            {[new_val | rev_acc], new_val}
          end)

        dp_cur = Enum.reverse(rev_dp_cur)
        {dp_cur, nil}
      end)

    List.last(final_dp)
  end
end
```

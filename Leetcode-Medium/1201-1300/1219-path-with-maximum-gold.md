# 1219. Path with Maximum Gold

## Cpp

```cpp
class Solution {
public:
    int rows, cols;
    
    int dfs(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == 0)
            return 0;
        int gold = grid[r][c];
        grid[r][c] = 0; // mark visited
        
        static const int dr[4] = {-1, 1, 0, 0};
        static const int dc[4] = {0, 0, -1, 1};
        int best = 0;
        for (int k = 0; k < 4; ++k) {
            best = max(best, dfs(grid, r + dr[k], c + dc[k]));
        }
        
        grid[r][c] = gold; // backtrack
        return gold + best;
    }
    
    int getMaximumGold(vector<vector<int>>& grid) {
        rows = grid.size();
        cols = grid[0].size();
        int ans = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] > 0) {
                    ans = max(ans, dfs(grid, i, j));
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final int[] DR = {0, 1, 0, -1};
    private static final int[] DC = {1, 0, -1, 0};

    public int getMaximumGold(int[][] grid) {
        int maxGold = 0;
        int rows = grid.length;
        int cols = grid[0].length;

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] > 0) {
                    maxGold = Math.max(maxGold, dfs(grid, r, c));
                }
            }
        }
        return maxGold;
    }

    private int dfs(int[][] grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == 0) {
            return 0;
        }
        int currentGold = grid[r][c];
        grid[r][c] = 0; // mark as visited

        int maxNext = 0;
        for (int i = 0; i < 4; ++i) {
            int nr = r + DR[i];
            int nc = c + DC[i];
            maxNext = Math.max(maxNext, dfs(grid, nr, nc));
        }

        grid[r][c] = currentGold; // backtrack
        return currentGold + maxNext;
    }
}
```

## Python

```python
class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            gold = grid[r][c]
            grid[r][c] = 0  # mark visited
            max_next = 0
            for dr, dc in dirs:
                nxt = dfs(r + dr, c + dc)
                if nxt > max_next:
                    max_next = nxt
            grid[r][c] = gold  # backtrack
            return gold + max_next
        
        max_gold = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    collected = dfs(i, j)
                    if collected > max_gold:
                        max_gold = collected
        return max_gold
```

## Python3

```python
from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            gold = grid[r][c]
            grid[r][c] = 0  # mark as visited
            best = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                best = max(best, dfs(nr, nc))
            grid[r][c] = gold  # backtrack
            return gold + best

        max_gold = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold
```

## C

```c
int dfs(int** grid, int rows, int cols, int r, int c) {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == 0)
        return 0;
    int original = grid[r][c];
    grid[r][c] = 0; // mark visited
    int maxNext = 0;
    const int dr[4] = {0, 1, 0, -1};
    const int dc[4] = {1, 0, -1, 0};
    for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        int val = dfs(grid, rows, cols, nr, nc);
        if (val > maxNext)
            maxNext = val;
    }
    grid[r][c] = original; // backtrack
    return original + maxNext;
}

int getMaximumGold(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = gridColSize[0];
    int result = 0;
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] > 0) {
                int gold = dfs(grid, rows, cols, r, c);
                if (gold > result)
                    result = gold;
            }
        }
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private static readonly int[] dr = { -1, 1, 0, 0 };
    private static readonly int[] dc = { 0, 0, -1, 1 };

    public int GetMaximumGold(int[][] grid)
    {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int maxGold = 0;

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (grid[i][j] > 0)
                {
                    int gold = Dfs(grid, i, j, rows, cols);
                    if (gold > maxGold) maxGold = gold;
                }
            }
        }

        return maxGold;
    }

    private int Dfs(int[][] grid, int r, int c, int rows, int cols)
    {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == 0)
            return 0;

        int original = grid[r][c];
        grid[r][c] = 0; // mark visited

        int maxNext = 0;
        for (int k = 0; k < 4; k++)
        {
            int nr = r + dr[k];
            int nc = c + dc[k];
            int collected = Dfs(grid, nr, nc, rows, cols);
            if (collected > maxNext) maxNext = collected;
        }

        grid[r][c] = original; // backtrack
        return original + maxNext;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var getMaximumGold = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    let maxGold = 0;
    const dirs = [[0,1],[1,0],[0,-1],[-1,0]];
    
    function dfs(r, c) {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] === 0) return 0;
        const cur = grid[r][c];
        grid[r][c] = 0; // mark visited
        let best = 0;
        for (const [dr, dc] of dirs) {
            const val = dfs(r + dr, c + dc);
            if (val > best) best = val;
        }
        grid[r][c] = cur; // backtrack
        return cur + best;
    }
    
    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            if (grid[i][j] > 0) {
                const collected = dfs(i, j);
                if (collected > maxGold) maxGold = collected;
            }
        }
    }
    
    return maxGold;
};
```

## Typescript

```typescript
function getMaximumGold(grid: number[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;
    const directions = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ];

    function dfs(r: number, c: number): number {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] === 0) {
            return 0;
        }

        const gold = grid[r][c];
        grid[r][c] = 0; // mark as visited

        let maxNext = 0;
        for (const [dr, dc] of directions) {
            const nr = r + dr;
            const nc = c + dc;
            const collected = dfs(nr, nc);
            if (collected > maxNext) {
                maxNext = collected;
            }
        }

        grid[r][c] = gold; // backtrack
        return gold + maxNext;
    }

    let result = 0;
    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            if (grid[i][j] > 0) {
                const collected = dfs(i, j);
                if (collected > result) {
                    result = collected;
                }
            }
        }
    }

    return result;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function getMaximumGold($grid) {
        $rows = count($grid);
        if ($rows == 0) return 0;
        $cols = count($grid[0]);
        $maxGold = 0;

        $dfs = function($r, $c) use (&$grid, &$dfs, $rows, $cols) {
            if ($r < 0 || $r >= $rows || $c < 0 || $c >= $cols || $grid[$r][$c] == 0) {
                return 0;
            }
            $original = $grid[$r][$c];
            $grid[$r][$c] = 0; // mark visited
            $max = 0;
            $directions = [[0,1],[1,0],[0,-1],[-1,0]];
            foreach ($directions as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols && $grid[$nr][$nc] > 0) {
                    $collected = $dfs($nr, $nc);
                    if ($collected > $max) {
                        $max = $collected;
                    }
                }
            }
            $grid[$r][$c] = $original; // backtrack
            return $original + $max;
        };

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] > 0) {
                    $gold = $dfs($i, $j);
                    if ($gold > $maxGold) {
                        $maxGold = $gold;
                    }
                }
            }
        }

        return $maxGold;
    }
}
?>
```

## Swift

```swift
class Solution {
    func getMaximumGold(_ grid: [[Int]]) -> Int {
        var grid = grid
        let rows = grid.count
        let cols = grid[0].count
        var maxGold = 0
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        func dfs(_ r: Int, _ c: Int) -> Int {
            if r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == 0 {
                return 0
            }
            let gold = grid[r][c]
            grid[r][c] = 0
            var best = 0
            for d in dirs {
                let nr = r + d.0
                let nc = c + d.1
                best = max(best, dfs(nr, nc))
            }
            grid[r][c] = gold
            return gold + best
        }
        
        for i in 0..<rows {
            for j in 0..<cols where grid[i][j] > 0 {
                let collected = dfs(i, j)
                maxGold = max(maxGold, collected)
            }
        }
        return maxGold
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val dirs = intArrayOf(0, 1, 0, -1, 0)

    fun getMaximumGold(grid: Array<IntArray>): Int {
        var maxGold = 0
        val rows = grid.size
        val cols = grid[0].size
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (grid[r][c] > 0) {
                    val gold = dfs(grid, r, c)
                    if (gold > maxGold) maxGold = gold
                }
            }
        }
        return maxGold
    }

    private fun dfs(grid: Array<IntArray>, r: Int, c: Int): Int {
        if (r !in grid.indices || c !in grid[0].indices || grid[r][c] == 0) return 0
        val original = grid[r][c]
        grid[r][c] = 0 // mark visited
        var maxNext = 0
        for (i in 0 until 4) {
            val nr = r + dirs[i]
            val nc = c + dirs[i + 1]
            val collected = dfs(grid, nr, nc)
            if (collected > maxNext) maxNext = collected
        }
        grid[r][c] = original // backtrack
        return original + maxNext
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int getMaximumGold(List<List<int>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    int maxGold = 0;

    int dfs(int r, int c) {
      if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == 0) {
        return 0;
      }
      int original = grid[r][c];
      grid[r][c] = 0; // mark as visited
      int best = 0;
      const List<int> dirs = [0, 1, 0, -1, 0];
      for (int i = 0; i < 4; i++) {
        int nr = r + dirs[i];
        int nc = c + dirs[i + 1];
        best = max(best, dfs(nr, nc));
      }
      grid[r][c] = original; // backtrack
      return original + best;
    }

    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (grid[i][j] > 0) {
          maxGold = max(maxGold, dfs(i, j));
        }
      }
    }

    return maxGold;
  }
}
```

## Golang

```go
func getMaximumGold(grid [][]int) int {
	rows := len(grid)
	if rows == 0 {
		return 0
	}
	cols := len(grid[0])
	maxGold := 0

	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	var dfs func(int, int) int
	dfs = func(r, c int) int {
		if r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == 0 {
			return 0
		}
		gold := grid[r][c]
		grid[r][c] = 0 // mark visited

		best := 0
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if val := dfs(nr, nc); val > best {
				best = val
			}
		}

		grid[r][c] = gold // backtrack
		return gold + best
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] != 0 {
				if cur := dfs(i, j); cur > maxGold {
					maxGold = cur
				}
			}
		}
	}
	return maxGold
}
```

## Ruby

```ruby
def get_maximum_gold(grid)
  rows = grid.size
  cols = grid[0].size
  max_gold = 0

  dfs = lambda do |r, c|
    return 0 if r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == 0
    gold = grid[r][c]
    grid[r][c] = 0
    best = 0
    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
      val = dfs.call(r + dr, c + dc)
      best = val if val > best
    end
    grid[r][c] = gold
    gold + best
  end

  rows.times do |i|
    cols.times do |j|
      next if grid[i][j] == 0
      cur = dfs.call(i, j)
      max_gold = cur if cur > max_gold
    end
  end

  max_gold
end
```

## Scala

```scala
object Solution {
  def getMaximumGold(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = if (rows == 0) 0 else grid(0).length
    val dirs = Array((0, 1), (1, 0), (0, -1), (-1, 0))

    def dfs(r: Int, c: Int): Int = {
      if (r < 0 || r >= rows || c < 0 || c >= cols || grid(r)(c) == 0) return 0
      val gold = grid(r)(c)
      grid(r)(c) = 0
      var best = 0
      for ((dr, dc) <- dirs) {
        val cur = dfs(r + dr, c + dc)
        if (cur > best) best = cur
      }
      grid(r)(c) = gold
      gold + best
    }

    var ans = 0
    for (i <- 0 until rows; j <- 0 until cols) {
      if (grid(i)(j) > 0) {
        val cur = dfs(i, j)
        if (cur > ans) ans = cur
      }
    }
    ans
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn get_maximum_gold(mut grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len() as i32;
        if rows == 0 {
            return 0;
        }
        let cols = grid[0].len() as i32;
        let mut ans = 0;
        for r in 0..rows {
            for c in 0..cols {
                if grid[r as usize][c as usize] > 0 {
                    let gold = Self::dfs(&mut grid, r, c);
                    if gold > ans {
                        ans = gold;
                    }
                }
            }
        }
        ans
    }

    fn dfs(grid: &mut Vec<Vec<i32>>, r: i32, c: i32) -> i32 {
        let rows = grid.len() as i32;
        let cols = grid[0].len() as i32;
        if r < 0 || c < 0 || r >= rows || c >= cols || grid[r as usize][c as usize] == 0 {
            return 0;
        }
        let val = grid[r as usize][c as usize];
        grid[r as usize][c as usize] = 0;
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        let mut best = 0;
        for &(dr, dc) in &dirs {
            let gold = Self::dfs(grid, r + dr, c + dc);
            if gold > best {
                best = gold;
            }
        }
        grid[r as usize][c as usize] = val;
        val + best
    }
}
```

## Racket

```racket
(define/contract (get-maximum-gold grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((grid-v (list->vector (map list->vector grid)))
         (rows (vector-length grid-v))
         (cols (if (= rows 0) 0 (vector-length (vector-ref grid-v 0))))
         (directions '((0 1) (1 0) (0 -1) (-1 0)))
         (max-gold 0))
    (letrec ((dfs
               (lambda (r c)
                 (if (or (< r 0) (< c 0) (>= r rows) (>= c cols))
                     0
                     (let* ((cell (vector-ref (vector-ref grid-v r) c)))
                       (if (= cell 0)
                           0
                           (begin
                             ;; mark visited
                             (vector-set! (vector-ref grid-v r) c 0)
                             (let* ((neighbor-gains
                                      (map (lambda (d)
                                             (dfs (+ r (first d)) (+ c (second d))))
                                           directions))
                                    (best (apply max neighbor-gains)))
                               ;; restore cell value
                               (vector-set! (vector-ref grid-v r) c cell)
                               (+ cell best)))))))))
      (for ([r (in-range rows)])
        (for ([c (in-range cols)])
          (when (> (vector-ref (vector-ref grid-v r) c) 0)
            (let ((gold (dfs r c)))
              (when (> gold max-gold)
                (set! max-gold gold))))))
      max-gold)))
```

## Erlang

```erlang
-module(solution).
-export([get_maximum_gold/1]).

-spec get_maximum_gold(Grid :: [[integer()]]) -> integer().
get_maximum_gold(Grid) ->
    Rows = length(Grid),
    Cols = length(hd(Grid)),
    EmptyVisited = #{},
    MaxList = [ dfs(Grid, EmptyVisited, R, C)
                || R <- lists:seq(0, Rows - 1),
                   C <- lists:seq(0, Cols - 1) ],
    lists:max(MaxList).

-spec dfs([[integer()]], map(), integer(), integer()) -> integer().
dfs(Grid, Visited, R, C) ->
    Rows = length(Grid),
    Cols = length(hd(Grid)),
    if
        R < 0 orelse R >= Rows orelse C < 0 orelse C >= Cols ->
            0;
        maps:is_key({R, C}, Visited) ->
            0;
        true ->
            RowList = lists:nth(R + 1, Grid),
            Gold = lists:nth(C + 1, RowList),
            if
                Gold == 0 -> 0;
                true ->
                    NewVisited = maps:put({R, C}, true, Visited),
                    Directions = [{0,1},{1,0},{0,-1},{-1,0}],
                    MaxNext = lists:max(
                        [ dfs(Grid, NewVisited, R + DR, C + DC) || {DR, DC} <- Directions ]
                    ),
                    Gold + MaxNext
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_maximum_gold(grid :: [[integer]]) :: integer
  def get_maximum_gold(grid) do
    rows = length(grid)
    cols = if rows > 0, do: length(hd(grid)), else: 0

    positions =
      for r <- 0..(rows - 1),
          c <- 0..(cols - 1),
          do: {r, c}

    Enum.reduce(positions, 0, fn {r, c}, acc ->
      case get_val(grid, r, c) do
        0 -> acc
        _gold -> max(acc, dfs(grid, rows, cols, r, c, MapSet.new()))
      end
    end)
  end

  defp dfs(grid, rows, cols, r, c, visited) do
    cond do
      r < 0 or c < 0 or r >= rows or c >= cols ->
        0

      get_val(grid, r, c) == 0 ->
        0

      MapSet.member?(visited, {r, c}) ->
        0

      true ->
        current = get_val(grid, r, c)
        visited2 = MapSet.put(visited, {r, c})

        max_next =
          [
            dfs(grid, rows, cols, r + 1, c, visited2),
            dfs(grid, rows, cols, r - 1, c, visited2),
            dfs(grid, rows, cols, r, c + 1, visited2),
            dfs(grid, rows, cols, r, c - 1, visited2)
          ]
          |> Enum.max()

        current + max_next
    end
  end

  defp get_val(grid, r, c) do
    grid
    |> Enum.at(r)
    |> Enum.at(c)
  end
end
```

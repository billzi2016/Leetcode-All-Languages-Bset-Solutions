# 2658. Maximum Number of Fish in a Grid

## Cpp

```cpp
class Solution {
public:
    int findMaxFish(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        int maxFish = 0;
        const int dr[4] = {1, -1, 0, 0};
        const int dc[4] = {0, 0, 1, -1};

        function<int(int,int)> dfs = [&](int r, int c) -> int {
            if (r < 0 || r >= m || c < 0 || c >= n) return 0;
            if (grid[r][c] == 0 || visited[r][c]) return 0;
            visited[r][c] = true;
            int sum = grid[r][c];
            for (int k = 0; k < 4; ++k) {
                sum += dfs(r + dr[k], c + dc[k]);
            }
            return sum;
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    maxFish = max(maxFish, dfs(i, j));
                }
            }
        }
        return maxFish;
    }
};
```

## Java

```java
class Solution {
    public int findMaxFish(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int max = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    int sum = dfs(grid, visited, i, j);
                    if (sum > max) {
                        max = sum;
                    }
                }
            }
        }
        return max;
    }

    private int dfs(int[][] grid, boolean[][] visited, int r, int c) {
        int m = grid.length;
        int n = grid[0].length;
        if (r < 0 || r >= m || c < 0 || c >= n || visited[r][c] || grid[r][c] == 0) {
            return 0;
        }
        visited[r][c] = true;
        int sum = grid[r][c];
        sum += dfs(grid, visited, r + 1, c);
        sum += dfs(grid, visited, r - 1, c);
        sum += dfs(grid, visited, r, c + 1);
        sum += dfs(grid, visited, r, c - 1);
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        max_fish = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    stack = [(i, j)]
                    visited[i][j] = True
                    cur_sum = 0
                    while stack:
                        r, c = stack.pop()
                        cur_sum += grid[r][c]
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                stack.append((nr, nc))
                    max_fish = max(max_fish, cur_sum)
        return max_fish
```

## Python3

```python
from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m else 0
        visited = [[False] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int) -> int:
            stack = [(r, c)]
            total = 0
            while stack:
                x, y = stack.pop()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                total += grid[x][y]
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > 0:
                        stack.append((nx, ny))
            return total

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans
```

## C

```c
#include <stdlib.h>

static int dfs(int **grid, int rows, int cols, int r, int c, char *visited) {
    if (r < 0 || r >= rows || c < 0 || c >= cols) return 0;
    int idx = r * cols + c;
    if (visited[idx] || grid[r][c] == 0) return 0;
    visited[idx] = 1;
    int sum = grid[r][c];
    sum += dfs(grid, rows, cols, r + 1, c, visited);
    sum += dfs(grid, rows, cols, r - 1, c, visited);
    sum += dfs(grid, rows, cols, r, c + 1, visited);
    sum += dfs(grid, rows, cols, r, c - 1, visited);
    return sum;
}

int findMaxFish(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int rows = gridSize;
    int cols = gridColSize[0];
    char *visited = (char *)calloc(rows * cols, sizeof(char));
    int maxFish = 0;

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] > 0 && !visited[r * cols + c]) {
                int cur = dfs(grid, rows, cols, r, c, visited);
                if (cur > maxFish) maxFish = cur;
            }
        }
    }

    free(visited);
    return maxFish;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindMaxFish(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        bool[,] visited = new bool[m, n];
        int maxFish = 0;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] > 0 && !visited[i, j])
                {
                    int sum = Dfs(i, j);
                    if (sum > maxFish) maxFish = sum;
                }
            }
        }

        return maxFish;

        int Dfs(int r, int c)
        {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 || visited[r, c])
                return 0;

            visited[r, c] = true;
            int total = grid[r][c];
            total += Dfs(r + 1, c);
            total += Dfs(r - 1, c);
            total += Dfs(r, c + 1);
            total += Dfs(r, c - 1);
            return total;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var findMaxFish = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    function dfs(r, c) {
        if (r < 0 || r >= m || c < 0 || c >= n) return 0;
        if (grid[r][c] === 0 || visited[r][c]) return 0;
        visited[r][c] = true;
        let sum = grid[r][c];
        for (const [dr, dc] of dirs) {
            sum += dfs(r + dr, c + dc);
        }
        return sum;
    }
    
    let maxFish = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] > 0 && !visited[i][j]) {
                const total = dfs(i, j);
                if (total > maxFish) maxFish = total;
            }
        }
    }
    return maxFish;
};
```

## Typescript

```typescript
function findMaxFish(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    let maxFish = 0;

    function dfs(r: number, c: number): number {
        if (r < 0 || r >= m || c < 0 || c >= n) return 0;
        if (grid[r][c] === 0 || visited[r][c]) return 0;
        visited[r][c] = true;
        let sum = grid[r][c];
        sum += dfs(r + 1, c);
        sum += dfs(r - 1, c);
        sum += dfs(r, c + 1);
        sum += dfs(r, c - 1);
        return sum;
    }

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] > 0 && !visited[i][j]) {
                const fish = dfs(i, j);
                if (fish > maxFish) maxFish = fish;
            }
        }
    }

    return maxFish;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function findMaxFish($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $maxFish = 0;
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] > 0 && !$visited[$i][$j]) {
                    $stack = [[$i, $j]];
                    $visited[$i][$j] = true;
                    $sum = 0;
                    
                    while (!empty($stack)) {
                        [$r, $c] = array_pop($stack);
                        $sum += $grid[$r][$c];
                        
                        foreach ($dirs as $d) {
                            $nr = $r + $d[0];
                            $nc = $c + $d[1];
                            if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n &&
                                $grid[$nr][$nc] > 0 && !$visited[$nr][$nc]) {
                                $visited[$nr][$nc] = true;
                                $stack[] = [$nr, $nc];
                            }
                        }
                    }
                    
                    if ($sum > $maxFish) {
                        $maxFish = $sum;
                    }
                }
            }
        }
        
        return $maxFish;
    }
}
```

## Swift

```swift
class Solution {
    func findMaxFish(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        guard rows > 0 else { return 0 }
        let cols = grid[0].count
        var visited = Array(repeating: Array(repeating: false, count: cols), count: rows)
        var maxSum = 0
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in 0..<rows {
            for c in 0..<cols {
                if grid[r][c] > 0 && !visited[r][c] {
                    var stack: [(Int, Int)] = [(r, c)]
                    visited[r][c] = true
                    var currentSum = 0
                    
                    while let (cr, cc) = stack.popLast() {
                        currentSum += grid[cr][cc]
                        for (dr, dc) in directions {
                            let nr = cr + dr
                            let nc = cc + dc
                            if nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                                grid[nr][nc] > 0 && !visited[nr][nc] {
                                visited[nr][nc] = true
                                stack.append((nr, nc))
                            }
                        }
                    }
                    
                    maxSum = max(maxSum, currentSum)
                }
            }
        }
        
        return maxSum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaxFish(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val visited = Array(m) { BooleanArray(n) }
        var maxFish = 0

        fun dfs(r: Int, c: Int): Int {
            if (r !in 0 until m || c !in 0 until n) return 0
            if (grid[r][c] == 0 || visited[r][c]) return 0
            visited[r][c] = true
            var sum = grid[r][c]
            sum += dfs(r + 1, c)
            sum += dfs(r - 1, c)
            sum += dfs(r, c + 1)
            sum += dfs(r, c - 1)
            return sum
        }

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    val fish = dfs(i, j)
                    if (fish > maxFish) maxFish = fish
                }
            }
        }

        return maxFish
    }
}
```

## Dart

```dart
class Solution {
  int findMaxFish(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));
    int maxFish = 0;
    const List<int> dr = [1, -1, 0, 0];
    const List<int> dc = [0, 0, 1, -1];

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] > 0 && !visited[i][j]) {
          int sum = 0;
          List<int> stack = [i * n + j];
          while (stack.isNotEmpty) {
            int idx = stack.removeLast();
            int r = idx ~/ n;
            int c = idx % n;
            if (visited[r][c]) continue;
            visited[r][c] = true;
            sum += grid[r][c];
            for (int d = 0; d < 4; ++d) {
              int nr = r + dr[d];
              int nc = c + dc[d];
              if (nr >= 0 &&
                  nr < m &&
                  nc >= 0 &&
                  nc < n &&
                  grid[nr][nc] > 0 &&
                  !visited[nr][nc]) {
                stack.add(nr * n + nc);
              }
            }
          }
          if (sum > maxFish) maxFish = sum;
        }
      }
    }

    return maxFish;
  }
}
```

## Golang

```go
func findMaxFish(grid [][]int) int {
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	var dfs func(int, int) int
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	dfs = func(r, c int) int {
		if r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == 0 || visited[r][c] {
			return 0
		}
		visited[r][c] = true
		sum := grid[r][c]
		for _, d := range dirs {
			sum += dfs(r+d[0], c+d[1])
		}
		return sum
	}

	maxFish := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 && !visited[i][j] {
				fish := dfs(i, j)
				if fish > maxFish {
					maxFish = fish
				}
			}
		}
	}
	return maxFish
}
```

## Ruby

```ruby
def find_max_fish(grid)
  m = grid.size
  n = grid[0].size
  visited = Array.new(m) { Array.new(n, false) }
  max_sum = 0
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] == 0 || visited[i][j]

      sum = 0
      stack = [[i, j]]
      visited[i][j] = true

      until stack.empty?
        r, c = stack.pop
        sum += grid[r][c]
        dirs.each do |dr, dc|
          nr = r + dr
          nc = c + dc
          if nr.between?(0, m - 1) && nc.between?(0, n - 1) &&
             grid[nr][nc] > 0 && !visited[nr][nc]
            visited[nr][nc] = true
            stack << [nr, nc]
          end
        end
      end

      max_sum = sum if sum > max_sum
    end
  end

  max_sum
end
```

## Scala

```scala
object Solution {
    def findMaxFish(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        val visited = Array.ofDim[Boolean](m, n)
        var maxFish = 0

        def dfs(r: Int, c: Int): Int = {
            if (r < 0 || r >= m || c < 0 || c >= n) return 0
            if (visited(r)(c) || grid(r)(c) == 0) return 0
            visited(r)(c) = true
            var sum = grid(r)(c)
            sum += dfs(r + 1, c)
            sum += dfs(r - 1, c)
            sum += dfs(r, c + 1)
            sum += dfs(r, c - 1)
            sum
        }

        for (i <- 0 until m; j <- 0 until n) {
            if (!visited(i)(j) && grid(i)(j) > 0) {
                val fish = dfs(i, j)
                if (fish > maxFish) maxFish = fish
            }
        }
        maxFish
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_max_fish(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        let mut visited = vec![vec![false; n]; m];
        let mut max_fish = 0;

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] > 0 && !visited[i][j] {
                    let fish = Self::dfs(&grid, &mut visited, i as i32, j as i32);
                    if fish > max_fish {
                        max_fish = fish;
                    }
                }
            }
        }

        max_fish
    }

    fn dfs(grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, r: i32, c: i32) -> i32 {
        let rows = grid.len() as i32;
        let cols = grid[0].len() as i32;

        if r < 0 || r >= rows || c < 0 || c >= cols {
            return 0;
        }
        let (ur, uc) = (r as usize, c as usize);
        if visited[ur][uc] || grid[ur][uc] == 0 {
            return 0;
        }

        visited[ur][uc] = true;
        let mut sum = grid[ur][uc];
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        for &(dr, dc) in &dirs {
            sum += Self::dfs(grid, visited, r + dr, c + dc);
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (find-max-fish grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (= rows 0) 0 (length (first grid))))
         (gvec (list->vector (map list->vector grid)))
         (vis (make-vector rows)))
    (for ([i (in-range rows)])
      (vector-set! vis i (make-vector cols #f)))
    (define (in-bounds r c)
      (and (>= r 0) (< r rows) (>= c 0) (< c cols)))
    (define max-fish 0)
    (for ([r (in-range rows)])
      (for ([c (in-range cols)])
        (when (and (> (vector-ref (vector-ref gvec r) c) 0)
                   (not (vector-ref (vector-ref vis r) c)))
          (vector-set! (vector-ref vis r) c #t)
          (let loop ((stack (list (cons r c))) (sum 0))
            (if (null? stack)
                (set! max-fish (max max-fish sum))
                (let* ((rc (car stack)) (rest (cdr stack))
                       (rr (car rc)) (cc (cdr rc)))
                  (define cell-fish (vector-ref (vector-ref gvec rr) cc))
                  (let ((new-sum (+ sum cell-fish)))
                    (let ((new-stack rest))
                      (for ([d '((1 . 0) (-1 . 0) (0 . 1) (0 . -1))])
                        (define dr (car d))
                        (define dc (cdr d))
                        (let ((nr (+ rr dr)) (nc (+ cc dc)))
                          (when (and (in-bounds nr nc)
                                     (> (vector-ref (vector-ref gvec nr) nc) 0)
                                     (not (vector-ref (vector-ref vis nr) nc)))
                            (vector-set! (vector-ref vis nr) nc #t)
                            (set! new-stack (cons (cons nr nc) new-stack)))))
                      (loop new-stack new-sum))))))))))
    max-fish)))
```

## Erlang

```erlang
-spec find_max_fish(Grid :: [[integer()]]) -> integer().
find_max_fish(Grid) ->
    Rows = length(Grid),
    case Grid of
        [] -> 0;
        _ ->
            Cols = length(lists:nth(1, Grid)),
            iter(0, 0, Rows, Cols, Grid, #{}, 0)
    end.

iter(R, C, Rows, _Cols, _Grid, Visited, Max) when R >= Rows -> Max;
iter(R, C, Rows, Cols, Grid, Visited, Max) ->
    Val = get_cell(Grid, R, C),
    {NewMax, NewVisited} =
        if
            Val > 0 andalso not maps:is_key({R, C}, Visited) ->
                {Sum, V2} = dfs(R, C, Grid, Rows, Cols, Visited),
                {erlang:max(Max, Sum), V2};
            true -> {Max, Visited}
        end,
    if
        C + 1 < Cols ->
            iter(R, C + 1, Rows, Cols, Grid, NewVisited, NewMax);
        true ->
            iter(R + 1, 0, Rows, Cols, Grid, NewVisited, NewMax)
    end.

dfs(R, C, Grid, Rows, Cols, Visited) ->
    if
        R < 0 orelse R >= Rows orelse C < 0 orelse C >= Cols ->
            {0, Visited};
        maps:is_key({R, C}, Visited) ->
            {0, Visited};
        true ->
            Val = get_cell(Grid, R, C),
            if
                Val == 0 ->
                    {0, Visited};
                true ->
                    Vis1 = maps:put({R, C}, true, Visited),
                    {Sum1, Vis2} = dfs(R + 1, C, Grid, Rows, Cols, Vis1),
                    {Sum2, Vis3} = dfs(R - 1, C, Grid, Rows, Cols, Vis2),
                    {Sum3, Vis4} = dfs(R, C + 1, Grid, Rows, Cols, Vis3),
                    {Sum4, Vis5} = dfs(R, C - 1, Grid, Rows, Cols, Vis4),
                    Total = Val + Sum1 + Sum2 + Sum3 + Sum4,
                    {Total, Vis5}
            end
    end.

get_cell(Grid, R, C) ->
    Row = lists:nth(R + 1, Grid),
    lists:nth(C + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_fish(grid :: [[integer]]) :: integer
  def find_max_fish(grid) do
    rows = length(grid)
    cols = if rows == 0, do: 0, else: length(hd(grid))

    {max_sum, _visited} =
      Enum.reduce(0..rows - 1, {0, MapSet.new()}, fn r, {cur_max, visited} ->
        Enum.reduce(0..cols - 1, {cur_max, visited}, fn c, {cur_max2, visited2} ->
          if get(grid, r, c) > 0 and not MapSet.member?(visited2, {r, c}) do
            {comp_sum, new_visited} = dfs(grid, rows, cols, [{r, c}], visited2)
            {max(cur_max2, comp_sum), new_visited}
          else
            {cur_max2, visited2}
          end
        end)
      end)

    max_sum
  end

  defp get(grid, r, c) do
    grid |> Enum.at(r) |> Enum.at(c)
  end

  defp dfs(_grid, _rows, _cols, [], visited), do: {0, visited}

  defp dfs(grid, rows, cols, [{r, c} | stack], visited) do
    if MapSet.member?(visited, {r, c}) do
      dfs(grid, rows, cols, stack, visited)
    else
      val = get(grid, r, c)
      new_visited = MapSet.put(visited, {r, c})

      neighbors = [
        {r - 1, c},
        {r + 1, c},
        {r, c - 1},
        {r, c + 1}
      ]

      valid_neighbors =
        Enum.filter(neighbors, fn {nr, nc} ->
          nr >= 0 and nr < rows and nc >= 0 and nc < cols and
            get(grid, nr, nc) > 0 and not MapSet.member?(new_visited, {nr, nc})
        end)

      {sum_rest, final_vis} = dfs(grid, rows, cols, valid_neighbors ++ stack, new_visited)
      {val + sum_rest, final_vis}
    end
  end
end
```

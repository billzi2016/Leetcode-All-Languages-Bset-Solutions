# 0695. Max Area of Island

## Cpp

```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int maxArea = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == 1) {
                    int area = dfs(grid, i, j);
                    maxArea = max(maxArea, area);
                }
            }
        }
        return maxArea;
    }
private:
    int dfs(vector<vector<int>>& grid, int r, int c) {
        int rows = grid.size(), cols = grid[0].size();
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0)
            return 0;
        grid[r][c] = 0;
        int area = 1;
        area += dfs(grid, r + 1, c);
        area += dfs(grid, r - 1, c);
        area += dfs(grid, r, c + 1);
        area += dfs(grid, r, c - 1);
        return area;
    }
};
```

## Java

```java
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(grid, i, j);
                    if (area > maxArea) {
                        maxArea = area;
                    }
                }
            }
        }
        return maxArea;
    }

    private int dfs(int[][] grid, int r, int c) {
        int rows = grid.length;
        int cols = grid[0].length;
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0) {
            return 0;
        }
        grid[r][c] = 0; // mark as visited
        int area = 1;
        area += dfs(grid, r + 1, c);
        area += dfs(grid, r - 1, c);
        area += dfs(grid, r, c + 1);
        area += dfs(grid, r, c - 1);
        return area;
    }
}
```

## Python

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    stack = [(r, c)]
                    grid[r][c] = 0  # mark visited
                    while stack:
                        cr, cc = stack.pop()
                        area += 1
                        for dr, dc in directions:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                stack.append((nr, nc))
                                grid[nr][nc] = 0
                    max_area = max(max_area, area)

        return max_area
```

## Python3

```python
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return (1 + dfs(r - 1, c) + dfs(r + 1, c)
                      + dfs(r, c - 1) + dfs(r, c + 1))
        
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area
```

## C

```c
int dfs(int** grid, int r, int c, int rows, int cols) {
    if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0)
        return 0;
    grid[r][c] = 0; // mark visited
    int area = 1;
    area += dfs(grid, r + 1, c, rows, cols);
    area += dfs(grid, r - 1, c, rows, cols);
    area += dfs(grid, r, c + 1, rows, cols);
    area += dfs(grid, r, c - 1, rows, cols);
    return area;
}

int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize) {
    int maxArea = 0;
    for (int i = 0; i < gridSize; ++i) {
        int cols = gridColSize[i];
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                int area = dfs(grid, i, j, gridSize, cols);
                if (area > maxArea)
                    maxArea = area;
            }
        }
    }
    return maxArea;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxAreaOfIsland(int[][] grid)
    {
        if (grid == null || grid.Length == 0) return 0;
        int rows = grid.Length;
        int cols = grid[0].Length;
        int maxArea = 0;
        var directions = new int[] { -1, 0, 1, 0, -1 };

        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (grid[r][c] == 1)
                {
                    int area = 0;
                    var stack = new System.Collections.Generic.Stack<(int, int)>();
                    stack.Push((r, c));
                    grid[r][c] = 0; // mark visited

                    while (stack.Count > 0)
                    {
                        var (cr, cc) = stack.Pop();
                        area++;

                        for (int d = 0; d < 4; d++)
                        {
                            int nr = cr + directions[d];
                            int nc = cc + directions[d + 1];
                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1)
                            {
                                stack.Push((nr, nc));
                                grid[nr][nc] = 0; // mark visited
                            }
                        }
                    }

                    if (area > maxArea) maxArea = area;
                }
            }
        }

        return maxArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    
    const dfs = (r, c) => {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] === 0) return 0;
        grid[r][c] = 0; // mark visited
        let area = 1;
        area += dfs(r - 1, c);
        area += dfs(r + 1, c);
        area += dfs(r, c - 1);
        area += dfs(r, c + 1);
        return area;
    };
    
    let maxArea = 0;
    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            if (grid[i][j] === 1) {
                const curArea = dfs(i, j);
                if (curArea > maxArea) maxArea = curArea;
            }
        }
    }
    return maxArea;
};
```

## Typescript

```typescript
function maxAreaOfIsland(grid: number[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;
    const visited: boolean[][] = Array.from({ length: rows }, () => Array(cols).fill(false));
    let maxArea = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]] as const;

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] === 1 && !visited[i][j]) {
                let area = 0;
                const stack: [number, number][] = [[i, j]];
                visited[i][j] = true;

                while (stack.length) {
                    const [r, c] = stack.pop()!;
                    area++;
                    for (const [dr, dc] of dirs) {
                        const nr = r + dr;
                        const nc = c + dc;
                        if (
                            nr >= 0 && nr < rows &&
                            nc >= 0 && nc < cols &&
                            grid[nr][nc] === 1 &&
                            !visited[nr][nc]
                        ) {
                            visited[nr][nc] = true;
                            stack.push([nr, nc]);
                        }
                    }
                }

                if (area > maxArea) maxArea = area;
            }
        }
    }

    return maxArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxAreaOfIsland($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        // initialize visited matrix
        $visited = array_fill(0, $rows, array_fill(0, $cols, false));
        $maxArea = 0;
        $directions = [[1,0],[-1,0],[0,1],[0,-1]];
        
        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] === 1 && !$visited[$i][$j]) {
                    $area = 0;
                    $stack = [[$i, $j]];
                    $visited[$i][$j] = true;
                    
                    while (!empty($stack)) {
                        [$r, $c] = array_pop($stack);
                        $area++;
                        
                        foreach ($directions as $d) {
                            $nr = $r + $d[0];
                            $nc = $c + $d[1];
                            
                            if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols &&
                                $grid[$nr][$nc] === 1 && !$visited[$nr][$nc]) {
                                $visited[$nr][$nc] = true;
                                $stack[] = [$nr, $nc];
                            }
                        }
                    }
                    
                    if ($area > $maxArea) {
                        $maxArea = $area;
                    }
                }
            }
        }
        
        return $maxArea;
    }
}
```

## Swift

```swift
class Solution {
    func maxAreaOfIsland(_ grid: [[Int]]) -> Int {
        var grid = grid
        let rows = grid.count
        let cols = grid[0].count
        var maxArea = 0

        func dfs(_ r: Int, _ c: Int) -> Int {
            if r < 0 || r >= rows || c < 0 || c >= cols { return 0 }
            if grid[r][c] == 0 { return 0 }
            grid[r][c] = 0
            var area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
        }

        for i in 0..<rows {
            for j in 0..<cols {
                if grid[i][j] == 1 {
                    let currentArea = dfs(i, j)
                    maxArea = max(maxArea, currentArea)
                }
            }
        }
        return maxArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxAreaOfIsland(grid: Array<IntArray>): Int {
        val rows = grid.size
        if (rows == 0) return 0
        val cols = grid[0].size
        var maxArea = 0

        fun dfs(r: Int, c: Int): Int {
            if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0) return 0
            grid[r][c] = 0
            var area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
        }

        for (i in 0 until rows) {
            for (j in 0 until cols) {
                if (grid[i][j] == 1) {
                    val cur = dfs(i, j)
                    if (cur > maxArea) maxArea = cur
                }
            }
        }
        return maxArea
    }
}
```

## Dart

```dart
class Solution {
  int maxAreaOfIsland(List<List<int>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    int maxArea = 0;

    int dfs(int r, int c) {
      if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0) {
        return 0;
      }
      // Mark as visited
      grid[r][c] = 0;
      int area = 1;
      area += dfs(r + 1, c);
      area += dfs(r - 1, c);
      area += dfs(r, c + 1);
      area += dfs(r, c - 1);
      return area;
    }

    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        if (grid[i][j] == 1) {
          int currentArea = dfs(i, j);
          if (currentArea > maxArea) {
            maxArea = currentArea;
          }
        }
      }
    }

    return maxArea;
  }
}
```

## Golang

```go
func maxAreaOfIsland(grid [][]int) int {
    rows := len(grid)
    if rows == 0 {
        return 0
    }
    cols := len(grid[0])
    maxArea := 0

    var dfs func(int, int) int
    dfs = func(r, c int) int {
        if r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == 0 {
            return 0
        }
        grid[r][c] = 0
        area := 1
        area += dfs(r-1, c)
        area += dfs(r+1, c)
        area += dfs(r, c-1)
        area += dfs(r, c+1)
        return area
    }

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 1 {
                if a := dfs(i, j); a > maxArea {
                    maxArea = a
                }
            }
        }
    }
    return maxArea
}
```

## Ruby

```ruby
def max_area_of_island(grid)
  rows = grid.size
  cols = grid[0].size
  max_area = 0
  dirs = [[1,0],[-1,0],[0,1],[0,-1]]

  (0...rows).each do |i|
    (0...cols).each do |j|
      next unless grid[i][j] == 1
      area = 0
      stack = [[i, j]]
      grid[i][j] = 0

      until stack.empty?
        x, y = stack.pop
        area += 1
        dirs.each do |dx, dy|
          nx = x + dx
          ny = y + dy
          if nx.between?(0, rows - 1) && ny.between?(0, cols - 1) && grid[nx][ny] == 1
            stack << [nx, ny]
            grid[nx][ny] = 0
          end
        end
      end

      max_area = area if area > max_area
    end
  end

  max_area
end
```

## Scala

```scala
object Solution {
  def maxAreaOfIsland(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = if (rows == 0) 0 else grid(0).length
    val visited = Array.ofDim[Boolean](rows, cols)

    def dfs(r: Int, c: Int): Int = {
      if (r < 0 || c < 0 || r >= rows || c >= cols) return 0
      if (grid(r)(c) == 0 || visited(r)(c)) return 0
      visited(r)(c) = true
      1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
    }

    var maxArea = 0
    for (i <- 0 until rows; j <- 0 until cols) {
      if (grid(i)(j) == 1 && !visited(i)(j)) {
        val area = dfs(i, j)
        if (area > maxArea) maxArea = area
      }
    }
    maxArea
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        if rows == 0 {
            return 0;
        }
        let cols = grid[0].len();
        let mut max_area = 0;
        for r in 0..rows {
            for c in 0..cols {
                if grid[r][c] == 1 {
                    let area = Self::dfs(&mut grid, r, c);
                    if area > max_area {
                        max_area = area;
                    }
                }
            }
        }
        max_area
    }

    fn dfs(grid: &mut Vec<Vec<i32>>, r: usize, c: usize) -> i32 {
        if grid[r][c] == 0 {
            return 0;
        }
        grid[r][c] = 0;
        let mut area = 1;
        let rows = grid.len();
        let cols = grid[0].len();

        if r > 0 {
            area += Self::dfs(grid, r - 1, c);
        }
        if r + 1 < rows {
            area += Self::dfs(grid, r + 1, c);
        }
        if c > 0 {
            area += Self::dfs(grid, r, c - 1);
        }
        if c + 1 < cols {
            area += Self::dfs(grid, r, c + 1);
        }

        area
    }
}
```

## Racket

```racket
(define/contract (max-area-of-island grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (zero? rows) 0 (length (first grid))))
         (grid-vec (list->vector (map list->vector grid)))
         (visited (for/vector ([i rows]) (make-vector cols #f))))
    (define (in-bounds? r c)
      (and (>= r 0) (< r rows) (>= c 0) (< c cols)))
    (define (dfs r c)
      (if (not (in-bounds? r c))
          0
          (let* ((row-vec (vector-ref grid-vec r))
                 (cell (vector-ref row-vec c))
                 (vis-row (vector-ref visited r)))
            (if (or (= cell 0) (vector-ref vis-row c))
                0
                (begin
                  (vector-set! vis-row c #t)
                  (+ 1
                     (dfs (- r 1) c)
                     (dfs (+ r 1) c)
                     (dfs r (- c 1))
                     (dfs r (+ c 1))))))))
    (let loop ((r 0) (c 0) (max-area 0))
      (cond
        [(>= r rows) max-area]
        [(>= c cols) (loop (+ r 1) 0 max-area)]
        [else
         (define area (dfs r c))
         (loop r (+ c 1) (if (> area max-area) area max-area))]))))
```

## Erlang

```erlang
-module(solution).
-export([max_area_of_island/1]).
 
-spec max_area_of_island(Grid :: [[integer()]]) -> integer().
max_area_of_island(Grid) ->
    Rows = length(Grid),
    Cols = case Grid of
               [] -> 0;
               [FirstRow | _] -> length(FirstRow)
           end,
    Coords = [{R, C} || R <- lists:seq(0, Rows - 1), C <- lists:seq(0, Cols - 1)],
    {_, MaxArea} = lists:foldl(
        fun({R, C}, {Visited, CurMax}) ->
            case maps:is_key({R, C}, Visited) of
                true -> {Visited, CurMax};
                false ->
                    case cell(Grid, R, C) of
                        1 ->
                            {Area, NewVisited} = dfs([{R, C}], Grid, Rows, Cols, Visited, 0),
                            {NewVisited, erlang:max(CurMax, Area)};
                        _ -> {Visited, CurMax}
                    end
            end
        end,
        {maps:new(), 0},
        Coords),
    MaxArea.
 
%% Depth‑first search using an explicit stack.
-spec dfs(Stack :: [{integer(), integer()}],
          Grid :: [[integer()]],
          Rows :: integer(),
          Cols :: integer(),
          Visited :: map(),
          Acc :: integer()) -> {integer(), map()}.
dfs([], _Grid, _Rows, _Cols, Visited, Area) ->
    {Area, Visited};
dfs([{R, C} | Rest], Grid, Rows, Cols, Visited, Area) ->
    case maps:is_key({R, C}, Visited) of
        true ->
            dfs(Rest, Grid, Rows, Cols, Visited, Area);
        false ->
            if R < 0 orelse R >= Rows orelse C < 0 orelse C >= Cols ->
                    dfs(Rest, Grid, Rows, Cols, Visited, Area);
               true ->
                    case cell(Grid, R, C) of
                        1 ->
                            NewVisited = maps:put({R, C}, true, Visited),
                            Neigh = [{R - 1, C}, {R + 1, C}, {R, C - 1}, {R, C + 1}],
                            dfs(Neigh ++ Rest, Grid, Rows, Cols, NewVisited, Area + 1);
                        _ ->
                            dfs(Rest, Grid, Rows, Cols, Visited, Area)
                    end
            end
    end.
 
%% Retrieve the value at (R,C); assumes indices are within bounds.
-spec cell(Grid :: [[integer()]], R :: integer(), C :: integer()) -> integer().
cell(Grid, R, C) ->
    Row = lists:nth(R + 1, Grid),
    lists:nth(C + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_area_of_island(grid :: [[integer]]) :: integer
  def max_area_of_island(grid) do
    rows = length(grid)
    cols = if rows == 0, do: 0, else: length(hd(grid))

    {_, max_area} =
      Enum.reduce(0..rows - 1, {MapSet.new(), 0}, fn r, {visited, current_max} ->
        Enum.reduce(0..cols - 1, {visited, current_max}, fn c, {vis, cur_max} ->
          if get_cell(grid, r, c) == 1 and not MapSet.member?(vis, {r, c}) do
            {area, new_vis} = explore(r, c, grid, vis, rows, cols)
            {new_vis, max(cur_max, area)}
          else
            {vis, cur_max}
          end
        end)
      end)

    max_area
  end

  defp get_cell(grid, r, c) do
    grid |> Enum.at(r) |> Enum.at(c)
  end

  defp explore(r, c, grid, visited, rows, cols) do
    do_explore([{r, c}], visited, 0, grid, rows, cols)
  end

  defp do_explore([], visited, area, _grid, _rows, _cols), do: {area, visited}

  defp do_explore([{r, c} | rest], visited, area, grid, rows, cols) do
    cond do
      r < 0 or c < 0 or r >= rows or c >= cols ->
        do_explore(rest, visited, area, grid, rows, cols)

      MapSet.member?(visited, {r, c}) ->
        do_explore(rest, visited, area, grid, rows, cols)

      get_cell(grid, r, c) != 1 ->
        do_explore(rest, visited, area, grid, rows, cols)

      true ->
        visited = MapSet.put(visited, {r, c})
        new_stack = [{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1} | rest]
        do_explore(new_stack, visited, area + 1, grid, rows, cols)
    end
  end
end
```

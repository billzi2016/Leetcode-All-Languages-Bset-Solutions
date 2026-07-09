# 1254. Number of Closed Islands

## Cpp

```cpp
class Solution {
public:
    bool dfs(int i, int j, vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n) return false; // reached boundary
        if (grid[i][j] == 1) return true; // water or already visited
        grid[i][j] = 1; // mark as visited (convert to water)
        bool up    = dfs(i - 1, j, grid);
        bool down  = dfs(i + 1, j, grid);
        bool left  = dfs(i, j - 1, grid);
        bool right = dfs(i, j + 1, grid);
        return up && down && left && right;
    }
    
    int closedIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int count = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0 && dfs(i, j, grid)) {
                    ++count;
                }
            }
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    private void dfs(int[][] grid, int i, int j) {
        int m = grid.length;
        int n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != 0) return;
        grid[i][j] = 1; // mark as visited / water
        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }

    public int closedIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // Eliminate islands that touch the border
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) dfs(grid, i, 0);
            if (grid[i][n - 1] == 0) dfs(grid, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 0) dfs(grid, 0, j);
            if (grid[m - 1][j] == 0) dfs(grid, m - 1, j);
        }

        int closedCount = 0;
        for (int i = 1; i < m - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (grid[i][j] == 0) {
                    closedCount++;
                    dfs(grid, i, j);
                }
            }
        }

        return closedCount;
    }
}
```

## Python

```python
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(start_i, start_j):
            stack = [(start_i, start_j)]
            while stack:
                i, j = stack.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                    grid[i][j] = 1
                    stack.append((i + 1, j))
                    stack.append((i - 1, j))
                    stack.append((i, j + 1))
                    stack.append((i, j - 1))

        # Eliminate islands connected to the border
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n - 1] == 0:
                dfs(i, n - 1)
        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m - 1][j] == 0:
                dfs(m - 1, j)

        # Count closed islands
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        return count
```

## Python3

```python
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(si: int, sj: int) -> None:
            stack = [(si, sj)]
            while stack:
                i, j = stack.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                    grid[i][j] = 1
                    stack.append((i + 1, j))
                    stack.append((i - 1, j))
                    stack.append((i, j + 1))
                    stack.append((i, j - 1))

        # Eliminate islands connected to the border
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n - 1] == 0:
                dfs(i, n - 1)

        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m - 1][j] == 0:
                dfs(m - 1, j)

        # Count closed islands
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)

        return count
```

## C

```c
int dfs(int** grid, int r, int c, int rows, int cols) {
    if (r < 0 || r >= rows || c < 0 || c >= cols)
        return 0;                     // reached boundary -> not closed
    if (grid[r][c] == 1)
        return 1;                     // water or already visited
    grid[r][c] = 1;                    // mark as visited (turn to water)

    int up    = dfs(grid, r - 1, c, rows, cols);
    int down  = dfs(grid, r + 1, c, rows, cols);
    int left  = dfs(grid, r, c - 1, rows, cols);
    int right = dfs(grid, r, c + 1, rows, cols);

    return up && down && left && right;
}

int closedIsland(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0)
        return 0;

    int rows = gridSize;
    int cols = gridColSize[0];
    int count = 0;

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 0) {
                if (dfs(grid, i, j, rows, cols))
                    ++count;
            }
        }
    }

    return count;
}
```

## Csharp

```csharp
public class Solution
{
    private int[][] _grid;
    private bool[][] _visited;
    private int _rows;
    private int _cols;

    public int ClosedIsland(int[][] grid)
    {
        _grid = grid;
        _rows = grid.Length;
        _cols = grid[0].Length;
        _visited = new bool[_rows][];
        for (int i = 0; i < _rows; i++)
            _visited[i] = new bool[_cols];

        int count = 0;
        for (int i = 0; i < _rows; i++)
        {
            for (int j = 0; j < _cols; j++)
            {
                if (_grid[i][j] == 0 && !_visited[i][j])
                {
                    if (Dfs(i, j))
                        count++;
                }
            }
        }

        return count;
    }

    private bool Dfs(int r, int c)
    {
        // Out of bounds means the island touches the border -> not closed
        if (r < 0 || r >= _rows || c < 0 || c >= _cols)
            return false;

        // Water or already visited cell does not affect closure status
        if (_grid[r][c] == 1 || _visited[r][c])
            return true;

        _visited[r][c] = true;

        bool up = Dfs(r - 1, c);
        bool down = Dfs(r + 1, c);
        bool left = Dfs(r, c - 1);
        bool right = Dfs(r, c + 1);

        return up && down && left && right;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var closedIsland = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    let count = 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 0 && !visited[i][j]) {
                let isClosed = true;
                const stack = [[i, j]];
                visited[i][j] = true;
                
                while (stack.length) {
                    const [x, y] = stack.pop();
                    
                    // if touches border, not closed
                    if (x === 0 || x === m - 1 || y === 0 || y === n - 1) {
                        isClosed = false;
                    }
                    
                    for (const [dx, dy] of dirs) {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (
                            nx >= 0 && nx < m &&
                            ny >= 0 && ny < n &&
                            grid[nx][ny] === 0 &&
                            !visited[nx][ny]
                        ) {
                            visited[nx][ny] = true;
                            stack.push([nx, ny]);
                        }
                    }
                }
                
                if (isClosed) count++;
            }
        }
    }
    
    return count;
};
```

## Typescript

```typescript
function closedIsland(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    const dfs = (x: number, y: number): void => {
        const stack: [number, number][] = [[x, y]];
        visited[x][y] = true;
        while (stack.length) {
            const [cx, cy] = stack.pop()!;
            for (const [dx, dy] of dirs) {
                const nx = cx + dx;
                const ny = cy + dy;
                if (
                    nx >= 0 && nx < m &&
                    ny >= 0 && ny < n &&
                    grid[nx][ny] === 0 &&
                    !visited[nx][ny]
                ) {
                    visited[nx][ny] = true;
                    stack.push([nx, ny]);
                }
            }
        }
    };
    
    // Eliminate islands connected to the border
    for (let i = 0; i < m; i++) {
        if (grid[i][0] === 0 && !visited[i][0]) dfs(i, 0);
        if (grid[i][n - 1] === 0 && !visited[i][n - 1]) dfs(i, n - 1);
    }
    for (let j = 0; j < n; j++) {
        if (grid[0][j] === 0 && !visited[0][j]) dfs(0, j);
        if (grid[m - 1][j] === 0 && !visited[m - 1][j]) dfs(m - 1, j);
    }
    
    // Count closed islands
    let count = 0;
    for (let i = 1; i < m - 1; i++) {
        for (let j = 1; j < n - 1; j++) {
            if (grid[i][j] === 0 && !visited[i][j]) {
                count++;
                dfs(i, j);
            }
        }
    }
    
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function closedIsland($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $count = 0;
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 0 && !$visited[$i][$j]) {
                    $isClosed = true;
                    $queue = new SplQueue();
                    $queue->enqueue([$i, $j]);
                    $visited[$i][$j] = true;
                    
                    while (!$queue->isEmpty()) {
                        [$x, $y] = $queue->dequeue();
                        
                        if ($x == 0 || $x == $m - 1 || $y == 0 || $y == $n - 1) {
                            $isClosed = false;
                        }
                        
                        foreach ($dirs as $d) {
                            $nx = $x + $d[0];
                            $ny = $y + $d[1];
                            
                            if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n) {
                                if ($grid[$nx][$ny] == 0 && !$visited[$nx][$ny]) {
                                    $visited[$nx][$ny] = true;
                                    $queue->enqueue([$nx, $ny]);
                                }
                            }
                        }
                    }
                    
                    if ($isClosed) {
                        $count++;
                    }
                }
            }
        }
        
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func closedIsland(_ grid: [[Int]]) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        
        func dfs(_ i: Int, _ j: Int) -> Bool {
            if i < 0 || i >= m || j < 0 || j >= n {
                return false
            }
            if grid[i][j] == 1 || visited[i][j] {
                return true
            }
            visited[i][j] = true
            let up = dfs(i - 1, j)
            let down = dfs(i + 1, j)
            let left = dfs(i, j - 1)
            let right = dfs(i, j + 1)
            return up && down && left && right
        }
        
        var count = 0
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 0 && !visited[i][j] {
                    if dfs(i, j) {
                        count += 1
                    }
                }
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closedIsland(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val visited = Array(m) { BooleanArray(n) }
        var count = 0

        fun dfs(x: Int, y: Int): Boolean {
            if (x < 0 || x >= m || y < 0 || y >= n) return false
            if (grid[x][y] == 1) return true
            if (visited[x][y]) return true
            visited[x][y] = true
            val up = dfs(x - 1, y)
            val down = dfs(x + 1, y)
            val left = dfs(x, y - 1)
            val right = dfs(x, y + 1)
            return up && down && left && right
        }

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 0 && !visited[i][j]) {
                    if (dfs(i, j)) count++
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int closedIsland(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));

    bool dfs(int i, int j) {
      if (i < 0 || i >= m || j < 0 || j >= n) return false;
      if (grid[i][j] == 1 || visited[i][j]) return true;
      visited[i][j] = true;
      bool up = dfs(i - 1, j);
      bool down = dfs(i + 1, j);
      bool left = dfs(i, j - 1);
      bool right = dfs(i, j + 1);
      return up && down && left && right;
    }

    int count = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 0 && !visited[i][j]) {
          if (dfs(i, j)) count++;
        }
      }
    }
    return count;
  }
}
```

## Golang

```go
func closedIsland(grid [][]int) int {
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	var dfs func(int, int) bool
	dfs = func(x, y int) bool {
		if x < 0 || x >= m || y < 0 || y >= n {
			return false // reached outside -> not closed
		}
		if grid[x][y] == 1 || visited[x][y] {
			return true // water or already processed
		}
		visited[x][y] = true
		up := dfs(x-1, y)
		down := dfs(x+1, y)
		left := dfs(x, y-1)
		right := dfs(x, y+1)
		return up && down && left && right
	}

	count := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 && !visited[i][j] {
				if dfs(i, j) {
					count++
				}
			}
		}
	}
	return count
}
```

## Ruby

```ruby
def closed_island(grid)
  m = grid.length
  n = grid[0].length
  visited = Array.new(m) { Array.new(n, false) }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  count = 0

  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] == 1 || visited[i][j]

      queue = [[i, j]]
      head = 0
      visited[i][j] = true
      is_closed = true

      while head < queue.length
        x, y = queue[head]
        head += 1

        if x == 0 || y == 0 || x == m - 1 || y == n - 1
          is_closed = false
        end

        dirs.each do |dx, dy|
          nx = x + dx
          ny = y + dy
          if nx.between?(0, m - 1) && ny.between?(0, n - 1) &&
             grid[nx][ny] == 0 && !visited[nx][ny]
            visited[nx][ny] = true
            queue << [nx, ny]
          end
        end
      end

      count += 1 if is_closed
    end
  end

  count
end
```

## Scala

```scala
object Solution {
  def closedIsland(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    if (m == 0) return 0
    val n = grid(0).length
    val visited = Array.ofDim[Boolean](m, n)
    var count = 0
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    import scala.collection.mutable.Stack

    for (i <- 0 until m; j <- 0 until n) {
      if (grid(i)(j) == 0 && !visited(i)(j)) {
        var closed = true
        val stack = Stack[(Int, Int)]()
        stack.push((i, j))
        visited(i)(j) = true

        while (stack.nonEmpty) {
          val (x, y) = stack.pop()
          if (x == 0 || y == 0 || x == m - 1 || y == n - 1) closed = false
          for ((dx, dy) <- dirs) {
            val nx = x + dx
            val ny = y + dy
            if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
                grid(nx)(ny) == 0 && !visited(nx)(ny)) {
              visited(nx)(ny) = true
              stack.push((nx, ny))
            }
          }
        }

        if (closed) count += 1
      }
    }

    count
  }
}
```

## Rust

```rust
impl Solution {
    fn dfs(x: i32, y: i32, grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>) -> bool {
        let m = grid.len() as i32;
        let n = grid[0].len() as i32;

        if x < 0 || x >= m || y < 0 || y >= n {
            return false; // touches border, not closed
        }
        let ux = x as usize;
        let uy = y as usize;

        if grid[ux][uy] == 1 || visited[ux][uy] {
            return true; // water or already processed
        }

        visited[ux][uy] = true;
        let mut is_closed = true;
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        for (dx, dy) in dirs.iter() {
            if !Self::dfs(x + dx, y + dy, grid, visited) {
                is_closed = false;
            }
        }
        is_closed
    }

    pub fn closed_island(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();

        let mut visited = vec![vec![false; n]; m];
        let mut count = 0i32;

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 0 && !visited[i][j] {
                    if Self::dfs(i as i32, j as i32, &grid, &mut visited) {
                        count += 1;
                    }
                }
            }
        }

        count
    }
}
```

## Racket

```racket
(define/contract (closed-island grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([gvec (list->vector (map list->vector grid))]
         [rows (vector-length gvec)]
         [cols (if (> rows 0) (vector-length (vector-ref gvec 0)) 0)]
         [visited (for/vector ([i rows]) (make-vector cols #f))])
    (define (set-visited! i j)
      (vector-set! (vector-ref visited i) j #t))
    (define (visited? i j)
      (vector-ref (vector-ref visited i) j))
    (define (cell i j)
      (if (or (< i 0) (>= i rows) (< j 0) (>= j cols))
          1
          (vector-ref (vector-ref gvec i) j)))
    (define (flood start-i start-j)
      (let loop ((stack (list (cons start-i start-j))))
        (when (pair? stack)
          (define i (caar stack))
          (define j (cdar stack))
          (define rest (cdr stack))
          (if (or (< i 0) (>= i rows) (< j 0) (>= j cols))
              (loop rest)
              (let ([val (cell i j)])
                (if (or (= val 1) (visited? i j))
                    (loop rest)
                    (begin
                      (set-visited! i j)
                      (define neighbors (list (cons (+ i 1) j)
                                              (cons (- i 1) j)
                                              (cons i (+ j 1))
                                              (cons i (- j 1))))
                      (loop (append neighbors rest)))))))))
    ;; flood border lands
    (for ([i (in-range rows)])
      (for ([j (list 0 (- cols 1))])
        (when (and (= (cell i j) 0) (not (visited? i j)))
          (flood i j))))
    (for ([j (in-range cols)])
      (for ([i (list 0 (- rows 1))])
        (when (and (= (cell i j) 0) (not (visited? i j)))
          (flood i j))))
    ;; count interior islands
    (let loop ((i 1) (cnt 0))
      (if (>= i (- rows 1))
          cnt
          (let inner ((j 1) (c cnt))
            (if (>= j (- cols 1))
                (loop (+ i 1) c)
                (if (and (= (cell i j) 0) (not (visited? i j)))
                    (begin
                      (flood i j)
                      (inner (+ j 1) (+ c 1)))
                    (inner (+ j 1) c)))))))))
```

## Erlang

```erlang
-module(solution).
-export([closed_island/1]).

-spec closed_island(Grid :: [[integer()]]) -> integer().
closed_island(Grid) ->
    M = length(Grid),
    N = case Grid of [] -> 0; [Row|_] -> length(Row) end,
    iterate_rows(0, Grid, M, N, #{}, 0).

iterate_rows(R, _Grid, M, _N, Vis, Count) when R == M ->
    Count;
iterate_rows(R, Grid, M, N, Vis, Count) ->
    Row = lists:nth(R + 1, Grid),
    {NewVis, NewCount} = iterate_cols(0, Row, R, Grid, M, N, Vis, Count),
    iterate_rows(R + 1, Grid, M, N, NewVis, NewCount).

iterate_cols(C, RowList, _R, _Grid, _M, _N, Vis, Count) when C == length(RowList) ->
    {Vis, Count};
iterate_cols(C, RowList, R, Grid, M, N, Vis, Count) ->
    Val = lists:nth(C + 1, RowList),
    case Val of
        0 ->
            case maps:is_key({R, C}, Vis) of
                true ->
                    iterate_cols(C + 1, RowList, R, Grid, M, N, Vis, Count);
                false ->
                    {IsClosed, UpdatedVis} = dfs([{R, C}], Grid, M, N, Vis, true),
                    NewCount = if IsClosed -> Count + 1; true -> Count end,
                    iterate_cols(C + 1, RowList, R, Grid, M, N, UpdatedVis, NewCount)
            end;
        _ ->
            iterate_cols(C + 1, RowList, R, Grid, M, N, Vis, Count)
    end.

dfs([], _Grid, _M, _N, Vis, IsClosed) ->
    {IsClosed, Vis};
dfs([{R, C} | Rest], Grid, M, N, Vis, IsClosedAcc) ->
    case maps:is_key({R, C}, Vis) of
        true ->
            dfs(Rest, Grid, M, N, Vis, IsClosedAcc);
        false ->
            Val = get_cell(Grid, R, C),
            case Val of
                1 ->
                    dfs(Rest, Grid, M, N, Vis, IsClosedAcc);
                0 ->
                    NewVis = maps:put({R, C}, true, Vis),
                    Boundary = (R == 0) orelse (R == M - 1) orelse (C == 0) orelse (C == N - 1),
                    NewIsClosed = IsClosedAcc andalso not Boundary,
                    Neigh = [{R - 1, C}, {R + 1, C}, {R, C - 1}, {R, C + 1}],
                    dfs(Neigh ++ Rest, Grid, M, N, NewVis, NewIsClosed)
            end
    end.

get_cell(Grid, R, C) ->
    Row = lists:nth(R + 1, Grid),
    lists:nth(C + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec closed_island(grid :: [[integer]]) :: integer
  def closed_island(grid) do
    m = length(grid)
    n = grid |> hd() |> length()
    {count, _visited} =
      Enum.reduce(0..(m - 1), {0, MapSet.new()}, fn i, {cnt, visited} ->
        Enum.reduce(0..(n - 1), {cnt, visited}, fn j, {c2, v2} ->
          if cell(grid, i, j) == 0 and not MapSet.member?(v2, {i, j}) do
            {closed?, new_visited} = dfs(grid, i, j, m, n, v2)
            new_cnt = if closed?, do: c2 + 1, else: c2
            {new_cnt, new_visited}
          else
            {c2, v2}
          end
        end)
      end)

    count
  end

  defp cell(grid, i, j) do
    row = Enum.at(grid, i)
    Enum.at(row, j)
  end

  defp dfs(grid, i, j, m, n, visited) do
    do_dfs([{i, j}], grid, m, n, MapSet.put(visited, {i, j}), true)
  end

  defp do_dfs([], _grid, _m, _n, visited, closed), do: {closed, visited}

  defp do_dfs([{x, y} | rest], grid, m, n, visited, closed) do
    new_closed = if x == 0 or y == 0 or x == m - 1 or y == n - 1, do: false, else: closed

    {new_stack, new_visited} =
      Enum.reduce([{1, 0}, {-1, 0}, {0, 1}, {0, -1}], {rest, visited}, fn {dx, dy},
                                                                          {stack_acc,
                                                                           vis_acc} ->
        nx = x + dx
        ny = y + dy

        if nx >= 0 and nx < m and ny >= 0 and ny < n do
          if cell(grid, nx, ny) == 0 and not MapSet.member?(vis_acc, {nx, ny}) do
            {[{nx, ny} | stack_acc], MapSet.put(vis_acc, {nx, ny})}
          else
            {stack_acc, vis_acc}
          end
        else
          {stack_acc, vis_acc}
        end
      end)

    do_dfs(new_stack, grid, m, n, new_visited, new_closed)
  end
end
```

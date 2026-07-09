# 1034. Coloring A Border

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int row, int col, int color) {
        int m = grid.size(), n = grid[0].size();
        int orig = grid[row][col];
        vector<vector<int>> vis(m, vector<int>(n, 0));
        vector<pair<int,int>> border;
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        
        function<void(int,int)> dfs = [&](int r, int c) {
            vis[r][c] = 1;
            bool isBorder = false;
            for (auto &d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    isBorder = true;
                } else if (grid[nr][nc] != orig) {
                    isBorder = true;
                } else if (!vis[nr][nc]) {
                    dfs(nr, nc);
                }
            }
            if (isBorder) border.emplace_back(r, c);
        };
        
        dfs(row, col);
        for (auto &p : border) {
            grid[p.first][p.second] = color;
        }
        return grid;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[][] colorBorder(int[][] grid, int row, int col, int color) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        List<int[]> borders = new ArrayList<>();
        int original = grid[row][col];
        dfs(grid, row, col, original, visited, borders);
        for (int[] cell : borders) {
            grid[cell[0]][cell[1]] = color;
        }
        return grid;
    }

    private void dfs(int[][] grid, int r, int c, int original,
                     boolean[][] visited, List<int[]> borders) {
        int m = grid.length;
        int n = grid[0].length;
        visited[r][c] = true;
        boolean isBorder = false;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                isBorder = true;
            } else if (grid[nr][nc] != original) {
                isBorder = true;
            } else if (!visited[nr][nc]) {
                dfs(grid, nr, nc, original, visited, borders);
            }
        }
        if (isBorder) {
            borders.add(new int[]{r, c});
        }
    }
}
```

## Python

```python
class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        borders = []

        def dfs(r, c):
            visited[r][c] = True
            is_border = False
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    is_border = True
                elif grid[nr][nc] != orig:
                    is_border = True
                else:
                    if not visited[nr][nc]:
                        dfs(nr, nc)
            if is_border:
                borders.append((r, c))

        dfs(row, col)

        for r, c in borders:
            grid[r][c] = color
        return grid
```

## Python3

```python
from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        borders = []
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r: int, c: int):
            visited[r][c] = True
            is_border = False
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] != orig:
                    is_border = True
                else:
                    if not visited[nr][nc]:
                        dfs(nr, nc)
            if is_border:
                borders.append((r, c))

        dfs(row, col)

        for r, c in borders:
            grid[r][c] = color

        return grid
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void dfs(int r, int c, int **grid, int m, int n, int origColor,
                int **visited, int **border) {
    static const int dr[4] = {-1, 1, 0, 0};
    static const int dc[4] = {0, 0, -1, 1};

    visited[r][c] = 1;
    int isBorder = 0;

    for (int k = 0; k < 4; ++k) {
        int nr = r + dr[k];
        int nc = c + dc[k];

        if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
            isBorder = 1;
            continue;
        }
        if (grid[nr][nc] != origColor) {
            isBorder = 1;
            continue;
        }
        if (!visited[nr][nc]) {
            dfs(nr, nc, grid, m, n, origColor, visited, border);
        }
    }

    if (isBorder) {
        border[r][c] = 1;
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** colorBorder(int** grid, int gridSize, int* gridColSize, int row, int col,
                  int color, int* returnSize, int*** returnColumnSizes) {
    int m = gridSize;
    int n = gridColSize[0];  // matrix is rectangular per problem statement

    /* Allocate visited and border marker matrices */
    int **visited = (int **)malloc(m * sizeof(int *));
    int **border  = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        visited[i] = (int *)calloc(n, sizeof(int));
        border[i]  = (int *)calloc(n, sizeof(int));
    }

    int origColor = grid[row][col];
    dfs(row, col, grid, m, n, origColor, visited, border);

    /* Prepare result matrix */
    int **result = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        result[i] = (int *)malloc(n * sizeof(int));
        memcpy(result[i], grid[i], n * sizeof(int));
    }

    /* Apply new color to border cells */
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (border[i][j]) {
                result[i][j] = color;
            }
        }
    }

    /* Set return sizes */
    *returnSize = m;
    *returnColumnSizes = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        (*returnColumnSizes)[i] = (int *)malloc(sizeof(int));
        *((*returnColumnSizes)[i]) = n;
    }

    /* Free auxiliary matrices */
    for (int i = 0; i < m; ++i) {
        free(visited[i]);
        free(border[i]);
    }
    free(visited);
    free(border);

    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[][] ColorBorder(int[][] grid, int row, int col, int color) {
        int m = grid.Length;
        int n = grid[0].Length;
        bool[,] visited = new bool[m, n];
        List<(int r, int c)> borders = new List<(int, int)>();
        int original = grid[row][col];

        void Dfs(int r, int c) {
            visited[r, c] = true;
            bool isBorder = false;
            int[] dr = { -1, 1, 0, 0 };
            int[] dc = { 0, 0, -1, 1 };

            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    isBorder = true;
                } else if (grid[nr][nc] != original) {
                    isBorder = true;
                } else if (!visited[nr, nc]) {
                    Dfs(nr, nc);
                }
            }

            if (isBorder) {
                borders.Add((r, c));
            }
        }

        Dfs(row, col);

        foreach (var (r, c) in borders) {
            grid[r][c] = color;
        }

        return grid;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} row
 * @param {number} col
 * @param {number} color
 * @return {number[][]}
 */
var colorBorder = function(grid, row, col, color) {
    const m = grid.length;
    const n = grid[0].length;
    const original = grid[row][col];
    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const borders = [];
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    function dfs(r, c) {
        visited[r][c] = true;
        let isBorder = false;
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] !== original) {
                isBorder = true;
            } else if (!visited[nr][nc]) {
                dfs(nr, nc);
            }
        }
        if (isBorder) borders.push([r, c]);
    }
    
    dfs(row, col);
    for (const [r, c] of borders) {
        grid[r][c] = color;
    }
    return grid;
};
```

## Typescript

```typescript
function colorBorder(grid: number[][], row: number, col: number, color: number): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const original = grid[row][col];
    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const borders: [number, number][] = [];
    const dirs: number[][] = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    function dfs(r: number, c: number): void {
        visited[r][c] = true;
        let isBorder = false;
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                isBorder = true;
            } else if (grid[nr][nc] !== original) {
                isBorder = true;
            } else if (!visited[nr][nc]) {
                dfs(nr, nc);
            }
        }
        if (isBorder) borders.push([r, c]);
    }

    dfs(row, col);

    for (const [r, c] of borders) {
        grid[r][c] = color;
    }

    return grid;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $row
     * @param Integer $col
     * @param Integer $color
     * @return Integer[][]
     */
    function colorBorder($grid, $row, $col, $color) {
        $m = count($grid);
        $n = count($grid[0]);
        $orig = $grid[$row][$col];

        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $isBorder = array_fill(0, $m, array_fill(0, $n, false));

        $stack = [[$row, $col]];
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!empty($stack)) {
            [$i, $j] = array_pop($stack);
            if ($visited[$i][$j]) continue;
            $visited[$i][$j] = true;
            $border = false;

            foreach ($dirs as $d) {
                $ni = $i + $d[0];
                $nj = $j + $d[1];

                if ($ni < 0 || $ni >= $m || $nj < 0 || $nj >= $n) {
                    $border = true;
                } elseif ($grid[$ni][$nj] != $orig) {
                    $border = true;
                } else {
                    if (!$visited[$ni][$nj]) {
                        $stack[] = [$ni, $nj];
                    }
                }
            }

            if ($border) {
                $isBorder[$i][$j] = true;
            }
        }

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($isBorder[$i][$j]) {
                    $grid[$i][$j] = $color;
                }
            }
        }

        return $grid;
    }
}
```

## Swift

```swift
class Solution {
    func colorBorder(_ grid: [[Int]], _ row: Int, _ col: Int, _ color: Int) -> [[Int]] {
        let m = grid.count
        let n = grid[0].count
        var result = grid
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        let originalColor = grid[row][col]
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        func dfs(_ r: Int, _ c: Int) {
            visited[r][c] = true
            var isBorder = false
            for d in dirs {
                let nr = r + d.0
                let nc = c + d.1
                if nr < 0 || nr >= m || nc < 0 || nc >= n {
                    isBorder = true
                } else if grid[nr][nc] != originalColor {
                    isBorder = true
                } else if !visited[nr][nc] {
                    dfs(nr, nc)
                }
            }
            if isBorder {
                result[r][c] = color
            }
        }
        
        dfs(row, col)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun colorBorder(grid: Array<IntArray>, row: Int, col: Int, color: Int): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val original = grid[row][col]
        if (original == color) return grid

        val visited = Array(m) { BooleanArray(n) }
        val borders = mutableListOf<Pair<Int, Int>>()
        val dr = intArrayOf(-1, 1, 0, 0)
        val dc = intArrayOf(0, 0, -1, 1)

        fun dfs(r: Int, c: Int) {
            visited[r][c] = true
            var isBorder = false
            for (k in 0..3) {
                val nr = r + dr[k]
                val nc = c + dc[k]
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    isBorder = true
                } else if (grid[nr][nc] != original) {
                    isBorder = true
                } else if (!visited[nr][nc]) {
                    dfs(nr, nc)
                }
            }
            if (isBorder) borders.add(Pair(r, c))
        }

        dfs(row, col)

        for ((r, c) in borders) {
            grid[r][c] = color
        }
        return grid
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> colorBorder(List<List<int>> grid, int row, int col, int color) {
    int m = grid.length;
    int n = grid[0].length;
    int original = grid[row][col];
    List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));
    List<List<int>> borders = [];

    void dfs(int r, int c) {
      visited[r][c] = true;
      bool isBorder = false;
      const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
      ];
      for (var d in dirs) {
        int nr = r + d[0];
        int nc = c + d[1];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
          isBorder = true;
        } else if (grid[nr][nc] != original) {
          isBorder = true;
        } else if (!visited[nr][nc]) {
          dfs(nr, nc);
        }
      }
      if (isBorder) {
        borders.add([r, c]);
      }
    }

    dfs(row, col);

    for (var pos in borders) {
      grid[pos[0]][pos[1]] = color;
    }
    return grid;
  }
}
```

## Golang

```go
func colorBorder(grid [][]int, row int, col int, color int) [][]int {
	m := len(grid)
	n := len(grid[0])
	orig := grid[row][col]

	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	var borders [][2]int
	dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	var dfs func(int, int)
	dfs = func(r, c int) {
		visited[r][c] = true
		isBorder := false
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n {
				isBorder = true
				continue
			}
			if grid[nr][nc] != orig {
				isBorder = true
			} else if !visited[nr][nc] {
				dfs(nr, nc)
			}
		}
		if isBorder {
			borders = append(borders, [2]int{r, c})
		}
	}

	dfs(row, col)

	for _, p := range borders {
		grid[p[0]][p[1]] = color
	}
	return grid
}
```

## Ruby

```ruby
def color_border(grid, row, col, color)
  m = grid.size
  n = grid[0].size
  original = grid[row][col]
  visited = Array.new(m) { Array.new(n, false) }
  borders = []
  stack = [[row, col]]
  visited[row][col] = true
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  until stack.empty?
    i, j = stack.pop
    is_border = false
    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      if ni < 0 || ni >= m || nj < 0 || nj >= n
        is_border = true
      elsif grid[ni][nj] != original
        is_border = true
      else
        unless visited[ni][nj]
          visited[ni][nj] = true
          stack << [ni, nj]
        end
      end
    end
    borders << [i, j] if is_border
  end

  borders.each { |i, j| grid[i][j] = color }
  grid
end
```

## Scala

```scala
object Solution {
  def colorBorder(grid: Array[Array[Int]], row: Int, col: Int, color: Int): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val orig = grid(row)(col)
    val visited = Array.ofDim[Boolean](m, n)
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    import scala.collection.mutable.{Stack, ArrayBuffer}
    val stack = Stack[(Int, Int)]()
    val borders = ArrayBuffer[(Int, Int)]()

    stack.push((row, col))
    visited(row)(col) = true

    while (stack.nonEmpty) {
      val (r, c) = stack.pop()
      var isBorder = false
      for ((dr, dc) <- dirs) {
        val nr = r + dr
        val nc = c + dc
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
          isBorder = true
        } else if (grid(nr)(nc) != orig) {
          isBorder = true
        } else if (!visited(nr)(nc)) {
          visited(nr)(nc) = true
          stack.push((nr, nc))
        }
      }
      if (isBorder) borders += ((r, c))
    }

    for ((r, c) <- borders) {
      grid(r)(c) = color
    }

    grid
  }
}
```

## Rust

```rust
impl Solution {
    pub fn color_border(grid: Vec<Vec<i32>>, row: i32, col: i32, color: i32) -> Vec<Vec<i32>> {
        let mut g = grid;
        let m = g.len();
        let n = g[0].len();
        let sr = row as usize;
        let sc = col as usize;
        let original = g[sr][sc];
        if original == color {
            // No visual change needed, but still need to return the grid unchanged.
            return g;
        }

        fn dfs(
            r: usize,
            c: usize,
            orig: i32,
            m: usize,
            n: usize,
            grid: &Vec<Vec<i32>>,
            visited: &mut Vec<Vec<bool>>,
            borders: &mut Vec<(usize, usize)>,
        ) {
            visited[r][c] = true;
            let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
            let mut is_border = false;

            for (dr, dc) in dirs.iter() {
                let nr_i = r as i32 + dr;
                let nc_i = c as i32 + dc;
                if nr_i < 0 || nr_i >= m as i32 || nc_i < 0 || nc_i >= n as i32 {
                    is_border = true;
                } else {
                    let nr = nr_i as usize;
                    let nc = nc_i as usize;
                    if grid[nr][nc] != orig {
                        is_border = true;
                    } else if !visited[nr][nc] {
                        dfs(nr, nc, orig, m, n, grid, visited, borders);
                    }
                }
            }

            if is_border {
                borders.push((r, c));
            }
        }

        let mut visited = vec![vec![false; n]; m];
        let mut borders: Vec<(usize, usize)> = Vec::new();
        dfs(sr, sc, original, m, n, &g, &mut visited, &mut borders);

        for (r, c) in borders {
            g[r][c] = color;
        }

        g
    }
}
```

## Racket

```racket
#lang racket

(define/contract (color-border grid row col color)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?
       (listof (listof exact-integer?)))
  (let* ([vgrid (list->vector (map list->vector grid))]
         [m (vector-length vgrid)]
         [n (if (= m 0) 0 (vector-length (vector-ref vgrid 0)))]
         [orig-color (vector-ref (vector-ref vgrid row) col)]
         [visited (let ([vec (make-vector m)])
                    (for ([i (in-range m)])
                      (vector-set! vec i (make-vector n #f)))
                    vec)]
         [dirs '((1 0) (-1 0) (0 1) (0 -1))]
         [stack (list (cons row col))]
         [border-pos '()])
    (define (in-bounds? r c)
      (and (>= r 0) (< r m) (>= c 0) (< c n)))
    (let loop ()
      (when (not (null? stack))
        (define cur (car stack))
        (set! stack (cdr stack))
        (define r (car cur))
        (define c (cdr cur))
        (unless (vector-ref (vector-ref visited r) c)
          (vector-set! (vector-ref visited r) c #t)
          (define border? #f)
          (for ([d dirs])
            (define nr (+ r (first d)))
            (define nc (+ c (second d)))
            (cond
              [(not (in-bounds? nr nc))
               (set! border? #t)]
              [else
               (define neigh-color (vector-ref (vector-ref vgrid nr) nc))
               (if (= neigh-color orig-color)
                   (unless (vector-ref (vector-ref visited nr) nc)
                     (set! stack (cons (cons nr nc) stack)))
                   (set! border? #t))]))
          (when border?
            (set! border-pos (cons (cons r c) border-pos)))))
        (loop)))
    ;; recolor borders
    (for ([pos border-pos])
      (define r (car pos))
      (define c (cdr pos))
      (vector-set! (vector-ref vgrid r) c color))
    ;; convert back to list of lists
    (vector->list (vector-map vector->list vgrid))))
```

## Erlang

```erlang
-module(solution).
-export([color_border/4]).

-spec color_border(Grid :: [[integer()]], Row :: integer(), Col :: integer(), Color :: integer()) -> [[integer()]].
color_border(Grid, Row, Col, Color) ->
    OrigColor = get(Grid, Row, Col),
    M = length(Grid),
    N = length(hd(Grid)),
    Visited0 = maps:put({Row, Col}, true, #{}),
    Queue0 = [{Row, Col}],
    BorderSet = bfs(Queue0, Visited0, #{}, Grid, OrigColor, M, N),
    set_cells(Grid, BorderSet, Color).

%% Retrieve value at (R,C) assuming 0‑based indices.
-spec get([[integer()]], integer(), integer()) -> integer().
get(Grid, R, C) ->
    Row = lists:nth(R + 1, Grid),
    lists:nth(C + 1, Row).

%% Determine if a cell is on the border of its component.
-spec is_border(integer(), integer(), [[integer()]], integer(), integer(), integer()) -> boolean().
is_border(R, C, _Grid, _OrigColor, M, N) when R =:= 0; R =:= M - 1; C =:= 0; C =:= N - 1 ->
    true;
is_border(R, C, Grid, OrigColor, _M, _N) ->
    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
    lists:any(
        fun({DR,DC}) ->
            NR = R + DR,
            NC = C + DC,
            get(Grid, NR, NC) =/= OrigColor
        end,
        Directions).

%% BFS traversal to collect border cells.
-spec bfs([ {integer(), integer()} ], map(), map(),
          [[integer()]], integer(), integer(), integer()) -> map().
bfs([], _Visited, BorderSet, _Grid, _OrigColor, _M, _N) ->
    BorderSet;
bfs([{R,C}|Rest], Visited, BorderSet, Grid, OrigColor, M, N) ->
    IsBorder = is_border(R, C, Grid, OrigColor, M, N),
    NewBorderSet = if IsBorder -> maps:put({R,C}, true, BorderSet); true -> BorderSet end,
    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
    {NewQueue, NewVisited} =
        lists:foldl(
            fun({DR,DC}, {QAcc,VAcc}) ->
                NR = R + DR,
                NC = C + DC,
                if NR >= 0, NR < M, NC >= 0, NC < N,
                   get(Grid, NR, NC) == OrigColor,
                   not maps:is_key({NR,NC}, VAcc) ->
                        {QAcc ++ [{NR,NC}], maps:put({NR,NC}, true, VAcc)};
                   true -> {QAcc, VAcc}
                end
            end,
            {Rest, Visited},
            Directions),
    bfs(NewQueue, NewVisited, NewBorderSet, Grid, OrigColor, M, N).

%% Produce the final grid with border cells recolored.
-spec set_cells([[integer()]], map(), integer()) -> [[integer()]].
set_cells(Grid, BorderSet, Color) ->
    RowIndices = lists:seq(0, length(Grid) - 1),
    lists:map(
        fun({RowList, R}) ->
            ColIndices = lists:seq(0, length(RowList) - 1),
            lists:map(
                fun({Val, C}) ->
                    case maps:is_key({R,C}, BorderSet) of
                        true -> Color;
                        false -> Val
                    end
                end,
                lists:zip(RowList, ColIndices)
            )
        end,
        lists:zip(Grid, RowIndices)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec color_border(grid :: [[integer]], row :: integer, col :: integer, color :: integer) :: [[integer]]
  def color_border(grid, row, col, new_color) do
    orig = get_elem(grid, row, col)
    rows = length(grid)
    cols = length(hd(grid))
    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    queue = :queue.new() |> :queue.in({row, col})
    visited = MapSet.new()
    borders = bfs(queue, visited, MapSet.new(), grid, orig, rows, cols, dirs)

    Enum.with_index(grid)
    |> Enum.map(fn {rlist, i} ->
      Enum.with_index(rlist)
      |> Enum.map(fn {_val, j} ->
        if MapSet.member?(borders, {i, j}), do: new_color, else: get_elem(grid, i, j)
      end)
    end)
  end

  defp bfs(queue, visited, borders, grid, orig, rows, cols, dirs) do
    case :queue.out(queue) do
      {:empty, _} ->
        borders

      {{:value, {r, c}}, q2} ->
        if MapSet.member?(visited, {r, c}) do
          bfs(q2, visited, borders, grid, orig, rows, cols, dirs)
        else
          visited = MapSet.put(visited, {r, c})
          {is_border, q3} = process_cell(r, c, q2, visited, grid, orig, rows, cols, dirs)

          borders =
            if is_border do
              MapSet.put(borders, {r, c})
            else
              borders
            end

          bfs(q3, visited, borders, grid, orig, rows, cols, dirs)
        end
    end
  end

  defp process_cell(r, c, queue, visited, grid, orig, rows, cols, dirs) do
    Enum.reduce(dirs, {false, queue}, fn {dr, dc}, {border_acc, qacc} ->
      nr = r + dr
      nc = c + dc

      cond do
        nr < 0 or nr >= rows or nc < 0 or nc >= cols ->
          {true, qacc}

        true ->
          val = get_elem(grid, nr, nc)

          if val != orig do
            {true, qacc}
          else
            if MapSet.member?(visited, {nr, nc}) do
              {border_acc, qacc}
            else
              {border_acc, :queue.in({nr, nc}, qacc)}
            end
          end
      end
    end)
  end

  defp get_elem(grid, r, c) do
    grid |> Enum.at(r) |> Enum.at(c)
  end
end
```

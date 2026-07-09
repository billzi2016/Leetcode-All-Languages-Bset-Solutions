# 1559. Detect Cycles in 2D Grid

## Cpp

```cpp
class Solution {
public:
    bool containsCycle(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> visited(m, vector<int>(n, 0));
        bool hasCycle = false;
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        
        function<void(int,int,int,int)> dfs = [&](int x, int y, int px, int py) {
            if (hasCycle) return;
            visited[x][y] = 1;
            for (auto &d : dirs) {
                int nx = x + d[0];
                int ny = y + d[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] != grid[x][y]) continue;
                if (nx == px && ny == py) continue; // don't go back to parent
                if (visited[nx][ny]) {
                    hasCycle = true;
                    return;
                }
                dfs(nx, ny, x, y);
            }
        };
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!visited[i][j]) {
                    dfs(i, j, -1, -1);
                    if (hasCycle) return true;
                }
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean containsCycle(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    java.util.ArrayDeque<int[]> stack = new java.util.ArrayDeque<>();
                    // push current cell with parent coordinates set to -1,-1
                    stack.push(new int[]{i, j, -1, -1});
                    while (!stack.isEmpty()) {
                        int[] cur = stack.pop();
                        int x = cur[0], y = cur[1];
                        int px = cur[2], py = cur[3];

                        if (visited[x][y]) {
                            continue;
                        }
                        visited[x][y] = true;

                        for (int d = 0; d < 4; d++) {
                            int nx = x + dx[d];
                            int ny = y + dy[d];
                            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                            if (grid[nx][ny] != grid[x][y]) continue;

                            if (!visited[nx][ny]) {
                                stack.push(new int[]{nx, ny, x, y});
                            } else {
                                // visited neighbor that is not the immediate parent indicates a cycle
                                if (!(nx == px && ny == py)) {
                                    return true;
                                }
                            }
                        }
                    }
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    stack = [(i, j, -1, -1)]  # x, y, parent_x, parent_y
                    visited[i][j] = True
                    while stack:
                        x, y, px, py = stack.pop()
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y]:
                                if not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    stack.append((nx, ny, x, y))
                                elif (nx, ny) != (px, py):
                                    return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    stack = [(i, j, -1, -1)]
                    visited[i][j] = True
                    while stack:
                        x, y, px, py = stack.pop()
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y]:
                                if not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    stack.append((nx, ny, x, y))
                                elif nx != px or ny != py:
                                    return True
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int rows, cols;
static char **ggrid;
static bool **vis;

static bool dfs(int x, int y, int px, int py) {
    vis[x][y] = true;
    static const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    for (int k = 0; k < 4; ++k) {
        int nx = x + dirs[k][0];
        int ny = y + dirs[k][1];
        if (nx < 0 || nx >= rows || ny < 0 || ny >= cols) continue;
        if (ggrid[nx][ny] != ggrid[x][y]) continue;
        if (nx == px && ny == py) continue;
        if (vis[nx][ny]) return true;
        if (dfs(nx, ny, x, y)) return true;
    }
    return false;
}

bool containsCycle(char** grid, int gridSize, int* gridColSize) {
    rows = gridSize;
    cols = gridColSize[0];
    ggrid = grid;

    vis = (bool**)malloc(rows * sizeof(bool*));
    for (int i = 0; i < rows; ++i)
        vis[i] = (bool*)calloc(cols, sizeof(bool));

    bool result = false;
    for (int i = 0; i < rows && !result; ++i) {
        for (int j = 0; j < cols && !result; ++j) {
            if (!vis[i][j]) {
                if (dfs(i, j, -1, -1))
                    result = true;
            }
        }
    }

    for (int i = 0; i < rows; ++i)
        free(vis[i]);
    free(vis);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public bool ContainsCycle(char[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        bool[,] visited = new bool[m, n];
        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (visited[i, j]) continue;

                var stack = new Stack<(int x, int y, int px, int py)>();
                stack.Push((i, j, -1, -1));

                while (stack.Count > 0)
                {
                    var cur = stack.Pop();
                    int x = cur.x, y = cur.y, px = cur.px, py = cur.py;

                    if (visited[x, y]) continue;
                    visited[x, y] = true;
                    char c = grid[x][y];

                    for (int d = 0; d < 4; d++)
                    {
                        int nx = x + dx[d];
                        int ny = y + dy[d];
                        if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                        if (grid[nx][ny] != c) continue;

                        if (!visited[nx, ny])
                        {
                            stack.Push((nx, ny, x, y));
                        }
                        else if (!(nx == px && ny == py))
                        {
                            return true;
                        }
                    }
                }
            }
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var containsCycle = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (visited[i][j]) continue;
            const stack = [{x: i, y: j, px: -1, py: -1}];
            
            while (stack.length) {
                const {x, y, px, py} = stack.pop();
                
                if (!visited[x][y]) {
                    visited[x][y] = true;
                    const ch = grid[x][y];
                    
                    for (const [dx, dy] of dirs) {
                        const nx = x + dx;
                        const ny = y + dy;
                        
                        if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                        if (grid[nx][ny] !== ch) continue;
                        
                        if (!visited[nx][ny]) {
                            stack.push({x: nx, y: ny, px: x, py: y});
                        } else if (!(nx === px && ny === py)) {
                            return true; // cycle found
                        }
                    }
                }
            }
        }
    }
    
    return false;
};
```

## Typescript

```typescript
function containsCycle(grid: string[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const dirs = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
    ];

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (visited[i][j]) continue;

            const stack: number[][] = [];
            // push current cell with parent coordinates set to -1,-1
            stack.push([i, j, -1, -1]);

            while (stack.length) {
                const [x, y, px, py] = stack.pop()!;
                if (!visited[x][y]) visited[x][y] = true;

                for (const [dx, dy] of dirs) {
                    const nx = x + dx;
                    const ny = y + dy;
                    if (
                        nx < 0 ||
                        nx >= m ||
                        ny < 0 ||
                        ny >= n ||
                        grid[nx][ny] !== grid[x][y]
                    ) {
                        continue;
                    }
                    if (nx === px && ny === py) continue; // don't go back to parent
                    if (visited[nx][ny]) {
                        return true; // found a cycle
                    } else {
                        stack.push([nx, ny, x, y]);
                    }
                }
            }
        }
    }

    return false;
}
```

## Php

```php
class Solution {
    private $m;
    private $n;
    private $grid;
    private $visited;

    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function containsCycle($grid) {
        $this->grid = $grid;
        $this->m = count($grid);
        $this->n = count($grid[0]);
        $this->visited = array_fill(0, $this->m, array_fill(0, $this->n, false));

        for ($i = 0; $i < $this->m; $i++) {
            for ($j = 0; $j < $this->n; $j++) {
                if (!$this->visited[$i][$j]) {
                    if ($this->dfs($i, $j, -1, -1, $grid[$i][$j])) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private function dfs($x, $y, $px, $py, $char) {
        $this->visited[$x][$y] = true;
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];
        foreach ($dirs as $d) {
            $nx = $x + $d[0];
            $ny = $y + $d[1];
            if ($nx < 0 || $nx >= $this->m || $ny < 0 || $ny >= $this->n) continue;
            if ($this->grid[$nx][$ny] !== $char) continue;
            if (!$this->visited[$nx][$ny]) {
                if ($this->dfs($nx, $ny, $x, $y, $char)) return true;
            } else {
                if (!($nx == $px && $ny == $py)) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    private var rows = 0
    private var cols = 0
    private var board: [[Character]] = []
    private var visited: [[Bool]] = []

    func containsCycle(_ grid: [[Character]]) -> Bool {
        self.board = grid
        rows = grid.count
        cols = grid[0].count
        visited = Array(repeating: Array(repeating: false, count: cols), count: rows)

        for i in 0..<rows {
            for j in 0..<cols {
                if !visited[i][j] {
                    if dfs(i, j, -1, -1) {
                        return true
                    }
                }
            }
        }
        return false
    }

    private func dfs(_ x: Int, _ y: Int, _ px: Int, _ py: Int) -> Bool {
        visited[x][y] = true
        let directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for (dx, dy) in directions {
            let nx = x + dx
            let ny = y + dy
            if nx < 0 || nx >= rows || ny < 0 || ny >= cols { continue }
            if board[nx][ny] != board[x][y] { continue }
            if nx == px && ny == py { continue } // skip the cell we came from
            if visited[nx][ny] {
                return true // found a cycle
            }
            if dfs(nx, ny, x, y) {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun containsCycle(grid: Array<CharArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        val visited = Array(m) { BooleanArray(n) }
        val dirs = arrayOf(
            intArrayOf(0, 1),
            intArrayOf(1, 0),
            intArrayOf(0, -1),
            intArrayOf(-1, 0)
        )
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (!visited[i][j]) {
                    val stack = java.util.ArrayDeque<IntArray>()
                    stack.add(intArrayOf(i, j, -1, -1))
                    while (stack.isNotEmpty()) {
                        val cur = stack.removeLast()
                        val x = cur[0]
                        val y = cur[1]
                        val px = cur[2]
                        val py = cur[3]
                        if (!visited[x][y]) visited[x][y] = true
                        for (d in dirs) {
                            val nx = x + d[0]
                            val ny = y + d[1]
                            if (nx !in 0 until m || ny !in 0 until n) continue
                            if (grid[nx][ny] != grid[x][y]) continue
                            if (nx == px && ny == py) continue
                            if (visited[nx][ny]) return true
                            stack.add(intArrayOf(nx, ny, x, y))
                        }
                    }
                }
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool containsCycle(List<List<String>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<bool>> visited = List.generate(m, (_) => List.filled(n, false));
    const List<int> dx = [1, -1, 0, 0];
    const List<int> dy = [0, 0, 1, -1];

    bool dfs(int x, int y, int px, int py) {
      visited[x][y] = true;
      for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
        if (grid[nx][ny] != grid[x][y]) continue;
        if (!visited[nx][ny]) {
          if (dfs(nx, ny, x, y)) return true;
        } else if (!(nx == px && ny == py)) {
          return true;
        }
      }
      return false;
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (!visited[i][j]) {
          if (dfs(i, j, -1, -1)) return true;
        }
      }
    }
    return false;
  }
}
```

## Golang

```go
func containsCycle(grid [][]byte) bool {
	m, n := len(grid), len(grid[0])
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	var dfs func(x, y, px, py int) bool
	dfs = func(x, y, px, py int) bool {
		visited[x][y] = true
		for _, d := range dirs {
			nx, ny := x+d[0], y+d[1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n || grid[nx][ny] != grid[x][y] {
				continue
			}
			if !visited[nx][ny] {
				if dfs(nx, ny, x, y) {
					return true
				}
			} else if nx != px || ny != py {
				return true
			}
		}
		return false
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if !visited[i][j] {
				if dfs(i, j, -1, -1) {
					return true
				}
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def contains_cycle(grid)
  m = grid.size
  n = grid[0].size
  visited = Array.new(m) { Array.new(n, false) }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  (0...m).each do |i|
    (0...n).each do |j|
      next if visited[i][j]

      stack = []
      stack << [i, j, -1, -1]
      visited[i][j] = true

      until stack.empty?
        x, y, px, py = stack.pop
        dirs.each do |dx, dy|
          nx = x + dx
          ny = y + dy
          next if nx < 0 || nx >= m || ny < 0 || ny >= n
          next unless grid[nx][ny] == grid[x][y]

          if !visited[nx][ny]
            visited[nx][ny] = true
            stack << [nx, ny, x, y]
          else
            return true if !(nx == px && ny == py)
          end
        end
      end
    end
  end

  false
end
```

## Scala

```scala
object Solution {
  def containsCycle(grid: Array[Array[Char]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    val visited = Array.ofDim[Boolean](m, n)
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    for (i <- 0 until m) {
      for (j <- 0 until n) {
        if (!visited(i)(j)) {
          val stack = new java.util.ArrayDeque[(Int, Int, Int, Int)]()
          stack.addLast((i, j, -1, -1))

          while (!stack.isEmpty) {
            val cur = stack.removeLast()
            val x = cur._1
            val y = cur._2
            val px = cur._3
            val py = cur._4

            if (visited(x)(y)) return true
            visited(x)(y) = true

            for ((dx, dy) <- dirs) {
              val nx = x + dx
              val ny = y + dy
              if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid(nx)(ny) == grid(x)(y)) {
                if (!(nx == px && ny == py)) {
                  stack.addLast((nx, ny, x, y))
                }
              }
            }
          }
        }
      }
    }

    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn contains_cycle(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        if m == 0 { return false; }
        let n = grid[0].len();
        let mut visited = vec![vec![false; n]; m];
        const DIRS: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

        for i in 0..m {
            for j in 0..n {
                if visited[i][j] { continue; }
                let mut stack: Vec<(usize, usize, i32, i32)> = Vec::new();
                visited[i][j] = true;
                stack.push((i, j, -1, -1));

                while let Some((r, c, pr, pc)) = stack.pop() {
                    for &(dr, dc) in DIRS.iter() {
                        let nr = r as i32 + dr;
                        let nc = c as i32 + dc;
                        if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                            continue;
                        }
                        let nr_usize = nr as usize;
                        let nc_usize = nc as usize;
                        if grid[nr_usize][nc_usize] != grid[r][c] {
                            continue;
                        }
                        if !visited[nr_usize][nc_usize] {
                            visited[nr_usize][nc_usize] = true;
                            stack.push((nr_usize, nc_usize, r as i32, c as i32));
                        } else if !(nr == pr && nc == pc) {
                            return true;
                        }
                    }
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (contains-cycle grid)
  (-> (listof (listof char?)) boolean?)
  (call/cc
    (lambda (return)
      (let* ([m (length grid)]
             [n (if (= m 0) 0 (length (car grid)))]
             [grid-v (list->vector (map list->vector grid))]
             [visited (make-vector m #f)])
        (for ([i m])
          (vector-set! visited i (make-vector n #f)))
        (define dirs '((-1 . 0) (1 . 0) (0 . -1) (0 . 1)))
        (let outer ((r 0) (c 0))
          (cond
            [(>= r m) (return #f)]
            [(>= c n) (outer (+ r 1) 0)]
            [else
             (if (vector-ref (vector-ref visited r) c)
                 (outer r (+ c 1))
                 (let dfs ((stack (list (list r c -1 -1))))
                   (if (null? stack)
                       (outer r (+ c 1))
                       (let* ([cur (car stack)]
                              [rest (cdr stack)]
                              [x (list-ref cur 0)]
                              [y (list-ref cur 1)]
                              [px (list-ref cur 2)]
                              [py (list-ref cur 3)])
                         (if (vector-ref (vector-ref visited x) y)
                             (dfs rest)
                             (begin
                               (vector-set! (vector-ref visited x) y #t)
                               (let explore ((ds dirs) (newstack rest))
                                 (cond
                                   [(null? ds) (dfs newstack)]
                                   [else
                                    (define dx (car (car ds)))
                                    (define dy (cdr (car ds)))
                                    (define nx (+ x dx))
                                    (define ny (+ y dy))
                                    (cond
                                      [(or (< nx 0) (>= nx m) (< ny 0) (>= ny n))
                                       (explore (cdr ds) newstack)]
                                      [(not (char=? (vector-ref (vector-ref grid-v nx) ny)
                                                    (vector-ref (vector-ref grid-v x) y)))
                                       (explore (cdr ds) newstack)]
                                      [else
                                       (if (and (= nx px) (= ny py))
                                           (explore (cdr ds) newstack)
                                           (if (vector-ref (vector-ref visited nx) ny)
                                               (return #t)
                                               (explore (cdr ds)
                                                        (cons (list nx ny x y) newstack))))]))]))))))))
                 )])))))
```

## Erlang

```erlang
-export([contains_cycle/1]).
-spec contains_cycle(Grid :: [[char()]]) -> boolean().
contains_cycle(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    GridTuples = [list_to_tuple(Row) || Row <- Grid],
    G = list_to_tuple(GridTuples),
    Vis0 = #{},
    iter_cells(0, 0, M, N, G, Vis0).

%% iterate over all cells
iter_cells(R, C, M, _N, _G, _Vis) when R >= M -> false;
iter_cells(R, C, M, N, G, Vis) ->
    case maps:is_key({R, C}, Vis) of
        true ->
            {NextR, NextC} = next_pos(R, C, M, N),
            iter_cells(NextR, NextC, M, N, G, Vis);
        false ->
            Char = get_char(G, R, C),
            case dfs([{R, C, -1, -1}], G, M, N, Char, Vis) of
                {true, _} -> true;
                {false, NewVis} ->
                    {NextR, NextC} = next_pos(R, C, M, N),
                    iter_cells(NextR, NextC, M, N, G, NewVis)
            end
    end.

%% depth‑first search using an explicit stack
dfs(Stack, _G, _M, _N, _Char, Vis) when Stack =:= [] -> {false, Vis};
dfs([{R, C, PR, PC} | Rest], G, M, N, Char, Vis) ->
    case maps:is_key({R, C}, Vis) of
        true ->
            dfs(Rest, G, M, N, Char, Vis);
        false ->
            Vis1 = maps:put({R, C}, true, Vis),
            try
                Neighbors = [{R-1, C}, {R+1, C}, {R, C-1}, {R, C+1}],
                NewStack = lists:foldl(
                    fun ({NR, NC}, Acc) ->
                        if NR < 0 orelse NR >= M orelse NC < 0 orelse NC >= N ->
                                Acc;
                           true ->
                                case get_char(G, NR, NC) of
                                    Char2 when Char2 =:= Char ->
                                        if (NR =:= PR andalso NC =:= PC) ->
                                                Acc;
                                           maps:is_key({NR, NC}, Vis1) ->
                                                throw(cycle);
                                           true ->
                                                [{NR, NC, R, C} | Acc]
                                        end;
                                    _ -> Acc
                                end
                        end
                    end,
                    Rest,
                    Neighbors),
                dfs(NewStack, G, M, N, Char, Vis1)
            catch
                throw:cycle -> {true, Vis1}
            end
    end.

%% get next cell coordinates in row‑major order
next_pos(R, C, M, N) ->
    if C + 1 < N ->
            {R, C + 1};
       R + 1 < M ->
            {R + 1, 0};
       true ->
            {M, N}
    end.

%% retrieve character at (R, C)
get_char(G, R, C) ->
    RowTuple = element(R + 1, G),
    element(C + 1, RowTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec contains_cycle(grid :: [[char]]) :: boolean
  def contains_cycle(grid) do
    rows = length(grid)
    cols = length(hd(grid))
    grid_tuples = Enum.map(grid, &List.to_tuple/1)

    iterate(grid_tuples, rows, cols, 0, 0, MapSet.new())
  end

  # Iterate over all cells row by row.
  defp iterate(_grid, _rows, _cols, r, _c, _visited) when r == _rows, do: false

  defp iterate(grid, rows, cols, r, c, visited) when c == cols,
    do: iterate(grid, rows, cols, r + 1, 0, visited)

  defp iterate(grid, rows, cols, r, c, visited) do
    if MapSet.member?(visited, {r, c}) do
      iterate(grid, rows, cols, r, c + 1, visited)
    else
      char = elem(Enum.at(grid, r), c)

      case dfs_iter(r, c, char, grid, rows, cols, visited) do
        {:found, _} ->
          true

        {:ok, new_visited} ->
          iterate(grid, rows, cols, r, c + 1, new_visited)
      end
    end
  end

  # Depth‑first search using an explicit stack.
  defp dfs_iter(sr, sc, char, grid, rows, cols, visited) do
    dfs_loop([{sr, sc, -1, -1}], char, grid, rows, cols, visited)
  end

  defp dfs_loop([], _char, _grid, _rows, _cols, visited), do: {:ok, visited}

  defp dfs_loop([{r, c, pr, pc} | rest], char, grid, rows, cols, visited) do
    if MapSet.member?(visited, {r, c}) do
      dfs_loop(rest, char, grid, rows, cols, visited)
    else
      visited = MapSet.put(visited, {r, c})

      dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

      {found, new_stack, new_visited} =
        Enum.reduce(dirs, {false, rest, visited}, fn {dr, dc},
                                                    {found_acc, stack_acc,
                                                     vis_acc} ->
          if found_acc do
            {true, stack_acc, vis_acc}
          else
            nr = r + dr
            nc = c + dc

            cond do
              nr < 0 or nr >= rows or nc < 0 or nc >= cols ->
                {false, stack_acc, vis_acc}

              true ->
                row_tuple = Enum.at(grid, nr)

                if elem(row_tuple, nc) != char do
                  {false, stack_acc, vis_acc}
                else
                  if {nr, nc} == {pr, pc} do
                    {false, stack_acc, vis_acc}
                  else
                    if MapSet.member?(vis_acc, {nr, nc}) do
                      # Cycle detected
                      {true, [], vis_acc}
                    else
                      {false,
                       [{nr, nc, r, c} | stack_acc],
                       vis_acc}
                    end
                  end
                end
            end
          end
        end)

      if found do
        {:found, visited}
      else
        dfs_loop(new_stack, char, grid, rows, cols, new_visited)
      end
    end
  end
end
```

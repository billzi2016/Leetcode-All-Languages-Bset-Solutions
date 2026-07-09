# 0980. Unique Paths III

## Cpp

```cpp
class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int total = 0, sr = 0, sc = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] != -1) ++total;
                if (grid[i][j] == 1) { sr = i; sc = j; }
            }
        }
        int ans = 0;
        const int dr[4] = {1, -1, 0, 0};
        const int dc[4] = {0, 0, 1, -1};

        function<void(int,int,int)> dfs = [&](int r, int c, int remain) {
            if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == -1) return;
            if (grid[r][c] == 2) {
                if (remain == 0) ++ans;
                return;
            }
            int temp = grid[r][c];
            grid[r][c] = -1; // mark visited
            for (int k = 0; k < 4; ++k) {
                dfs(r + dr[k], c + dc[k], remain - 1);
            }
            grid[r][c] = temp; // backtrack
        };

        dfs(sr, sc, total - 1);
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int rows;
    private int cols;
    private int total;
    private int[][] grid;
    private int result = 0;
    private final int[] dr = {1, -1, 0, 0};
    private final int[] dc = {0, 0, 1, -1};

    public int uniquePathsIII(int[][] grid) {
        this.grid = grid;
        rows = grid.length;
        cols = grid[0].length;
        int startR = 0, startC = 0;
        total = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] != -1) total++;
                if (grid[i][j] == 1) {
                    startR = i;
                    startC = j;
                }
            }
        }
        dfs(startR, startC, 1);
        return result;
    }

    private void dfs(int r, int c, int visited) {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == -1) return;

        if (grid[r][c] == 2) {
            if (visited == total) result++;
            return;
        }

        int temp = grid[r][c];
        grid[r][c] = -1; // mark as visited

        for (int k = 0; k < 4; k++) {
            dfs(r + dr[k], c + dc[k], visited + 1);
        }

        grid[r][c] = temp; // backtrack
    }
}
```

## Python

```python
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        total = 0
        sx = sy = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total += 1
                if grid[i][j] == 1:
                    sx, sy = i, j

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(x, y, remain):
            # If we reach the ending square
            if grid[x][y] == 2:
                return 1 if remain == 0 else 0

            # Mark as visited
            temp = grid[x][y]
            grid[x][y] = -1
            paths = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    paths += dfs(nx, ny, remain - 1)
            # Unmark
            grid[x][y] = temp
            return paths

        return dfs(sx, sy, total - 1)
```

## Python3

```python
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        start = end = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total += 1
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)

        self.ans = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x: int, y: int, steps: int) -> None:
            if (x, y) == end:
                if steps == total:
                    self.ans += 1
                return

            temp = grid[x][y]
            grid[x][y] = -1  # mark visited
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    dfs(nx, ny, steps + 1)
            grid[x][y] = temp  # backtrack

        dfs(start[0], start[1], 1)
        return self.ans
```

## C

```c
int rows, cols;
int ans;

void dfs(int r, int c, int remain, int **grid) {
    if (grid[r][c] == 2) {
        if (remain == 1) ans++;
        return;
    }
    int cur = grid[r][c];
    grid[r][c] = -1; // mark visited
    static const int dr[4] = {-1, 1, 0, 0};
    static const int dc[4] = {0, 0, -1, 1};
    for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] != -1) {
            dfs(nr, nc, remain - 1, grid);
        }
    }
    grid[r][c] = cur; // backtrack
}

int uniquePathsIII(int** grid, int gridSize, int* gridColSize){
    rows = gridSize;
    cols = gridColSize[0];
    int total = 0, sr = -1, sc = -1;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] != -1) total++;
            if (grid[i][j] == 1) { sr = i; sc = j; }
        }
    }
    ans = 0;
    dfs(sr, sc, total, grid);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int UniquePathsIII(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int total = 0;
        int startX = 0, startY = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] != -1) total++;
                if (grid[i][j] == 1) {
                    startX = i;
                    startY = j;
                }
            }
        }

        int count = 0;

        void Dfs(int x, int y, int remain) {
            if (x < 0 || x >= rows || y < 0 || y >= cols || grid[x][y] == -1)
                return;

            if (grid[x][y] == 2) {
                if (remain == 1) count++;
                return;
            }

            int temp = grid[x][y];
            grid[x][y] = -1; // mark visited

            Dfs(x + 1, y, remain - 1);
            Dfs(x - 1, y, remain - 1);
            Dfs(x, y + 1, remain - 1);
            Dfs(x, y - 1, remain - 1);

            grid[x][y] = temp; // backtrack
        }

        Dfs(startX, startY, total);
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var uniquePathsIII = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    let empty = 0;
    let startR = 0, startC = 0;

    for (let r = 0; r < rows; ++r) {
        for (let c = 0; c < cols; ++c) {
            if (grid[r][c] !== -1) empty++;
            if (grid[r][c] === 1) {
                startR = r;
                startC = c;
            }
        }
    }

    let ans = 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];

    const dfs = (r, c, remain) => {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] === -1) return;
        if (grid[r][c] === 2) {
            if (remain === 0) ans++;
            return;
        }

        const temp = grid[r][c];
        grid[r][c] = -1; // mark visited

        for (const [dr, dc] of dirs) {
            dfs(r + dr, c + dc, remain - 1);
        }

        grid[r][c] = temp; // backtrack
    };

    dfs(startR, startC, empty - 1);
    return ans;
};
```

## Typescript

```typescript
function uniquePathsIII(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let startX = 0, startY = 0;
    let total = 0; // count of non-obstacle squares

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== -1) total++;
            if (grid[i][j] === 1) {
                startX = i;
                startY = j;
            }
        }
    }

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    let ans = 0;

    function dfs(x: number, y: number, remain: number): void {
        if (grid[x][y] === 2) {
            if (remain === 0) ans++;
            return;
        }

        const saved = grid[x][y];
        grid[x][y] = -1; // mark visited

        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
            if (grid[nx][ny] === -1) continue;
            dfs(nx, ny, remain - 1);
        }

        grid[x][y] = saved; // backtrack
    }

    dfs(startX, startY, total - 1); // start cell already counted

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
    function uniquePathsIII($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $empty = 0;
        $sx = $sy = 0;

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] != -1) {
                    $empty++;
                }
                if ($grid[$i][$j] == 1) {
                    $sx = $i;
                    $sy = $j;
                }
            }
        }

        $count = 0;
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        $dfs = function($x, $y, $remain) use (&$grid, &$dfs, &$count, $m, $n, $dirs) {
            if ($grid[$x][$y] == 2) {
                if ($remain == 0) {
                    $count++;
                }
                return;
            }

            $temp = $grid[$x][$y];
            $grid[$x][$y] = -1; // mark visited

            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;
                if ($grid[$nx][$ny] == -1) continue;
                $dfs($nx, $ny, $remain - 1);
            }

            $grid[$x][$y] = $temp; // backtrack
        };

        $dfs($sx, $sy, $empty - 1); // start cell already counted

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func uniquePathsIII(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var startR = 0, startC = 0
        var totalNonObstacles = 0
        
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] != -1 {
                    totalNonObstacles += 1
                }
                if grid[i][j] == 1 {
                    startR = i
                    startC = j
                }
            }
        }
        
        var result = 0
        let directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        func dfs(_ r: Int, _ c: Int, _ visitedCount: Int, _ mask: Int) {
            if grid[r][c] == 2 {
                if visitedCount == totalNonObstacles {
                    result += 1
                }
                return
            }
            
            for (dr, dc) in directions {
                let nr = r + dr
                let nc = c + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                if grid[nr][nc] == -1 { continue }
                let idx = nr * n + nc
                if (mask & (1 << idx)) != 0 { continue } // already visited
                dfs(nr, nc, visitedCount + 1, mask | (1 << idx))
            }
        }
        
        let startIdx = startR * n + startC
        dfs(startR, startC, 1, 1 << startIdx)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uniquePathsIII(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var startX = 0
        var startY = 0
        var total = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] != -1) total++
                if (grid[i][j] == 1) {
                    startX = i
                    startY = j
                }
            }
        }
        var ans = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        fun dfs(x: Int, y: Int, visited: Int) {
            if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == -1) return
            if (grid[x][y] == 2) {
                if (visited == total) ans++
                return
            }
            val temp = grid[x][y]
            grid[x][y] = -1
            for (d in dirs) {
                dfs(x + d[0], y + d[1], visited + 1)
            }
            grid[x][y] = temp
        }
        dfs(startX, startY, 1)
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int uniquePathsIII(List<List<int>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    int total = 0;
    int startX = 0, startY = 0;

    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        if (grid[i][j] != -1) total++;
        if (grid[i][j] == 1) {
          startX = i;
          startY = j;
        }
      }
    }

    int ans = 0;
    const List<List<int>> dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    void dfs(int x, int y, int steps) {
      if (grid[x][y] == 2) {
        if (steps == total) ans++;
        return;
      }

      int temp = grid[x][y];
      grid[x][y] = -1; // mark visited

      for (var d in dirs) {
        int nx = x + d[0];
        int ny = y + d[1];
        if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] != -1) {
          dfs(nx, ny, steps + 1);
        }
      }

      grid[x][y] = temp; // backtrack
    }

    dfs(startX, startY, 1);
    return ans;
  }
}
```

## Golang

```go
func uniquePathsIII(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	total := 0
	var sx, sy int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != -1 {
				total++
			}
			if grid[i][j] == 1 {
				sx, sy = i, j
			}
		}
	}

	ans := 0
	var dfs func(x, y, cnt int)
	dfs = func(x, y, cnt int) {
		if grid[x][y] == 2 {
			if cnt == total {
				ans++
			}
			return
		}
		tmp := grid[x][y]
		grid[x][y] = -1
		dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		for _, d := range dirs {
			nx, ny := x+d[0], y+d[1]
			if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] != -1 {
				dfs(nx, ny, cnt+1)
			}
		}
		grid[x][y] = tmp
	}

	dfs(sx, sy, 1)
	return ans
}
```

## Ruby

```ruby
def unique_paths_iii(grid)
  m = grid.size
  n = grid[0].size
  start_i = start_j = nil
  total = 0
  (0...m).each do |i|
    (0...n).each do |j|
      val = grid[i][j]
      total += 1 if val != -1
      if val == 1
        start_i, start_j = i, j
      end
    end
  end

  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  visited = Array.new(m) { Array.new(n, false) }
  ans = 0

  dfs = nil
  dfs = lambda do |i, j, count|
    if grid[i][j] == 2
      ans += 1 if count == total
      return
    end
    visited[i][j] = true
    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      next unless ni.between?(0, m - 1) && nj.between?(0, n - 1)
      next if grid[ni][nj] == -1 || visited[ni][nj]
      dfs.call(ni, nj, count + 1)
    end
    visited[i][j] = false
  end

  dfs.call(start_i, start_j, 1)
  ans
end
```

## Scala

```scala
object Solution {
    def uniquePathsIII(grid: Array[Array[Int]]): Int = {
        val rows = grid.length
        val cols = grid(0).length
        var startR = 0
        var startC = 0
        var total = 0

        for (i <- 0 until rows) {
            for (j <- 0 until cols) {
                if (grid(i)(j) != -1) total += 1
                if (grid(i)(j) == 1) {
                    startR = i
                    startC = j
                }
            }
        }

        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
        var result = 0

        def dfs(r: Int, c: Int, visited: Int): Unit = {
            if (grid(r)(c) == 2) {
                if (visited == total) result += 1
                return
            }

            val temp = grid(r)(c)
            grid(r)(c) = -1 // mark as visited

            for ((dr, dc) <- dirs) {
                val nr = r + dr
                val nc = c + dc
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid(nr)(nc) != -1) {
                    dfs(nr, nc, visited + 1)
                }
            }

            grid(r)(c) = temp // backtrack
        }

        dfs(startR, startC, 1)
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn unique_paths_iii(grid: Vec<Vec<i32>>) -> i32 {
        fn dfs(
            grid: &mut Vec<Vec<i32>>,
            x: usize,
            y: usize,
            remain: i32,
            m: usize,
            n: usize,
        ) -> i32 {
            if grid[x][y] == 2 {
                return if remain == 1 { 1 } else { 0 };
            }
            let temp = grid[x][y];
            grid[x][y] = -1; // mark visited
            let mut paths = 0;
            let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
            for &(dx, dy) in &dirs {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx >= 0 && nx < m as i32 && ny >= 0 && ny < n as i32 {
                    let ux = nx as usize;
                    let uy = ny as usize;
                    if grid[ux][uy] != -1 {
                        paths += dfs(grid, ux, uy, remain - 1, m, n);
                    }
                }
            }
            grid[x][y] = temp; // backtrack
            paths
        }

        let mut grid = grid;
        let m = grid.len();
        let n = grid[0].len();

        let mut total = 0i32;
        let (mut sx, mut sy) = (0usize, 0usize);
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] != -1 {
                    total += 1;
                }
                if grid[i][j] == 1 {
                    sx = i;
                    sy = j;
                }
            }
        }

        dfs(&mut grid, sx, sy, total, m, n)
    }
}
```

## Racket

```racket
(define/contract (unique-paths-iii grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (first grid))))
         (gridv (list->vector (map list->vector grid)))
         (start-r -1)
         (start-c -1)
         (total
          (let loop ((i 0) (cnt 0))
            (if (= i m) cnt
                (let inner ((j 0) (c cnt))
                  (if (= j n) (loop (+ i 1) c)
                      (begin
                        (when (= (vector-ref (vector-ref gridv i) j) 1)
                          (set! start-r i)
                          (set! start-c j))
                        (inner (+ j 1)
                               (if (= (vector-ref (vector-ref gridv i) j) -1) c (+ c 1))))))))))
    (define (pos-index r c) (+ (* r n) c))
    (define (dfs r c mask steps)
      (let ((cell (vector-ref (vector-ref gridv r) c)))
        (if (= cell 2)
            (if (= steps total) 1 0)
            (let loop ((dirs '((1 0) (-1 0) (0 1) (0 -1))) (sum 0))
              (if (null? dirs) sum
                  (let* ((dr (caar dirs)) (dc (cdar dirs))
                         (nr (+ r dr)) (nc (+ c dc)))
                    (if (and (>= nr 0) (< nr m) (>= nc 0) (< nc n))
                        (let ((val (vector-ref (vector-ref gridv nr) nc)))
                          (if (not (= val -1))
                              (let* ((idx (pos-index nr nc))
                                     (bit (arithmetic-shift 1 idx)))
                                (if (= (bitwise-and mask bit) 0)
                                    (loop (cdr dirs)
                                          (+ sum (dfs nr nc (bitwise-ior mask bit) (+ steps 1))))
                                    (loop (cdr dirs) sum)))
                              (loop (cdr dirs) sum)))
                        (loop (cdr dirs) sum)))))))
    (let ((start-bit (arithmetic-shift 1 (pos-index start-r start-c))))
      (dfs start-r start-c start-bit 1)))
```

## Erlang

```erlang
-module(solution).
-export([unique_paths_iii/1]).

-define(DIRS, [{-1,0},{1,0},{0,-1},{0,1}]).

unique_paths_iii(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    Flat = lists:flatten(Grid),
    {_, StartIdx, EndIdx, TargetMask} =
        lists:foldl(fun(Value, {Idx, S, E, Mask}) ->
            NewMask = case Value of
                -1 -> Mask;
                _  -> Mask bor (1 bsl Idx)
            end,
            NewS = if Value == 1 -> Idx; true -> S end,
            NewE = if Value == 2 -> Idx; true -> E end,
            {Idx+1, NewS, NewE, NewMask}
        end, {0, undefined, undefined, 0}, Flat),
    StartMask = 1 bsl StartIdx,
    dfs(StartIdx, StartMask, M, N, TargetMask, EndIdx).

dfs(PosIdx, VisMask, M, N, TargetMask, EndIdx) ->
    if PosIdx =:= EndIdx ->
            if VisMask =:= TargetMask -> 1; true -> 0 end;
       true ->
            Row = PosIdx div N,
            Col = PosIdx rem N,
            lists:foldl(fun({DR,DC}, Acc) ->
                NewR = Row + DR,
                NewC = Col + DC,
                if NewR >= 0, NewR < M, NewC >= 0, NewC < N ->
                        NIdx = NewR * N + NewC,
                        Bit = 1 bsl NIdx,
                        case (VisMask band Bit) of
                            0 when (TargetMask band Bit) =/= 0 ->
                                Acc + dfs(NIdx, VisMask bor Bit, M, N, TargetMask, EndIdx);
                            _ -> Acc
                        end;
                    true -> Acc
                end
            end, 0, ?DIRS).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec unique_paths_iii(grid :: [[integer]]) :: integer
  def unique_paths_iii(grid) do
    m = length(grid)
    n = length(List.first(grid))

    {sx, sy, ex, ey, total} =
      Enum.reduce(0..m - 1, {nil, nil, nil, nil, 0}, fn i, acc ->
        row = Enum.at(grid, i)

        Enum.reduce(0..n - 1, acc, fn j, {sx, sy, ex, ey, total} ->
          val = Enum.at(row, j)

          case val do
            1 -> {i, j, ex, ey, total + 1}
            2 -> {sx, sy, i, j, total + 1}
            -1 -> {sx, sy, ex, ey, total}
            _ -> {sx, sy, ex, ey, total + 1}
          end
        end)
      end)

    start_idx = sx * n + sy
    start_mask = 1 <<< start_idx

    dfs(grid, m, n, ex, ey, total, sx, sy, start_mask, 1)
  end

  defp dfs(_grid, _m, _n, ex, ey, total, x, y, _mask, visited_cnt) when x == ex and y == ey do
    if visited_cnt == total, do: 1, else: 0
  end

  defp dfs(grid, m, n, ex, ey, total, x, y, mask, visited_cnt) do
    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    Enum.reduce(dirs, 0, fn {dx, dy}, acc ->
      nx = x + dx
      ny = y + dy

      if nx >= 0 and nx < m and ny >= 0 and ny < n do
        val = Enum.at(Enum.at(grid, nx), ny)
        idx = nx * n + ny
        bit = 1 <<< idx

        if val != -1 and (mask &&& bit) == 0 do
          acc +
            dfs(
              grid,
              m,
              n,
              ex,
              ey,
              total,
              nx,
              ny,
              mask ||| bit,
              visited_cnt + 1
            )
        else
          acc
        end
      else
        acc
      end
    end)
  end
end
```

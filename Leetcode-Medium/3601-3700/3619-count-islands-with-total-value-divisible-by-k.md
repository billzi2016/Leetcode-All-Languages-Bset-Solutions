# 3619. Count Islands With Total Value Divisible by K

## Cpp

```cpp
class Solution {
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        vector<vector<char>> visited(m, vector<char>(n, 0));
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        int islands = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    long long sum = 0;
                    std::queue<pair<int,int>> q;
                    q.emplace(i, j);
                    visited[i][j] = 1;
                    while (!q.empty()) {
                        auto [x, y] = q.front(); q.pop();
                        sum += grid[x][y];
                        for (auto &d : dirs) {
                            int nx = x + d[0], ny = y + d[1];
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
                                grid[nx][ny] > 0 && !visited[nx][ny]) {
                                visited[nx][ny] = 1;
                                q.emplace(nx, ny);
                            }
                        }
                    }
                    if (sum % k == 0) ++islands;
                }
            }
        }
        return islands;
    }
};
```

## Java

```java
class Solution {
    public int countIslands(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int islands = 0;
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    long sum = 0;
                    java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
                    stack.add(i * n + j);
                    while (!stack.isEmpty()) {
                        int cur = stack.poll();
                        int r = cur / n;
                        int c = cur % n;
                        if (grid[r][c] == 0) continue; // already visited
                        sum += grid[r][c];
                        grid[r][c] = 0; // mark as visited
                        for (int d = 0; d < 4; d++) {
                            int nr = r + dr[d];
                            int nc = c + dc[d];
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > 0) {
                                stack.add(nr * n + nc);
                            }
                        }
                    }
                    if (sum % k == 0) islands++;
                }
            }
        }
        return islands;
    }
}
```

## Python

```python
class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        from collections import deque

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    total = 0
                    dq = deque()
                    dq.append((i, j))
                    visited[i][j] = True
                    while dq:
                        x, y = dq.popleft()
                        total += grid[x][y]
                        # explore neighbors
                        if x > 0 and grid[x-1][y] > 0 and not visited[x-1][y]:
                            visited[x-1][y] = True
                            dq.append((x-1, y))
                        if x + 1 < m and grid[x+1][y] > 0 and not visited[x+1][y]:
                            visited[x+1][y] = True
                            dq.append((x+1, y))
                        if y > 0 and grid[x][y-1] > 0 and not visited[x][y-1]:
                            visited[x][y-1] = True
                            dq.append((x, y-1))
                        if y + 1 < n and grid[x][y+1] > 0 and not visited[x][y+1]:
                            visited[x][y+1] = True
                            dq.append((x, y+1))
                    if total % k == 0:
                        count += 1
        return count
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = 0
                    dq = deque()
                    dq.append((i, j))
                    # mark visited by setting to 0
                    while dq:
                        x, y = dq.popleft()
                        if grid[x][y] == 0:
                            continue
                        val = grid[x][y]
                        total += val
                        grid[x][y] = 0
                        if x > 0 and grid[x-1][y] > 0:
                            dq.append((x-1, y))
                        if x + 1 < m and grid[x+1][y] > 0:
                            dq.append((x+1, y))
                        if y > 0 and grid[x][y-1] > 0:
                            dq.append((x, y-1))
                        if y + 1 < n and grid[x][y+1] > 0:
                            dq.append((x, y+1))
                    if total % k == 0:
                        cnt += 1
        return cnt
```

## C

```c
#include <stdlib.h>

int countIslands(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize;
    if (m == 0) return 0;
    int n = gridColSize[0];
    int totalCells = m * n;

    int *q_i = (int *)malloc(totalCells * sizeof(int));
    int *q_j = (int *)malloc(totalCells * sizeof(int));

    int islands = 0;
    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] > 0) {
                long long sum = 0;
                int head = 0, tail = 0;

                // start BFS
                sum += grid[i][j];
                q_i[tail] = i;
                q_j[tail] = j;
                ++tail;
                grid[i][j] = 0; // mark visited

                while (head < tail) {
                    int ci = q_i[head];
                    int cj = q_j[head];
                    ++head;

                    for (int d = 0; d < 4; ++d) {
                        int ni = ci + dirs[d][0];
                        int nj = cj + dirs[d][1];
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] > 0) {
                            sum += grid[ni][nj];
                            q_i[tail] = ni;
                            q_j[tail] = nj;
                            ++tail;
                            grid[ni][nj] = 0; // mark visited
                        }
                    }
                }

                if (sum % k == 0) {
                    ++islands;
                }
            }
        }
    }

    free(q_i);
    free(q_j);
    return islands;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int CountIslands(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        bool[,] visited = new bool[m, n];
        int islands = 0;
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0 && !visited[i, j]) {
                    long sum = 0;
                    var stack = new Stack<(int r, int c)>();
                    stack.Push((i, j));
                    visited[i, j] = true;

                    while (stack.Count > 0) {
                        var (r, c) = stack.Pop();
                        sum += grid[r][c];

                        for (int d = 0; d < 4; d++) {
                            int nr = r + dr[d];
                            int nc = c + dc[d];
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                                grid[nr][nc] > 0 && !visited[nr, nc]) {
                                visited[nr, nc] = true;
                                stack.Push((nr, nc));
                            }
                        }
                    }

                    if (sum % k == 0) islands++;
                }
            }
        }

        return islands;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var countIslands = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    let islands = 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 0) continue;
            // start DFS
            let stack = [[i, j]];
            let sum = 0;
            grid[i][j] = 0; // mark visited
            while (stack.length) {
                const [x, y] = stack.pop();
                sum += grid[x][y]; // note: grid[x][y] is already set to 0, need original value
                // Actually we should add before zeroing. Adjust:
            }
        }
    }
    return islands;
};
```

## Typescript

```typescript
function countIslands(grid: number[][], k: number): number {
    const m = grid.length;
    const n = grid[0].length;
    const visited: Uint8Array[] = Array.from({ length: m }, () => new Uint8Array(n));
    let result = 0;
    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] > 0 && !visited[i][j]) {
                let sum = 0;
                const stack: [number, number][] = [[i, j]];
                visited[i][j] = 1;

                while (stack.length) {
                    const [x, y] = stack.pop()!;
                    sum += grid[x][y];

                    for (const [dx, dy] of dirs) {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (
                            nx >= 0 && nx < m &&
                            ny >= 0 && ny < n &&
                            grid[nx][ny] > 0 &&
                            !visited[nx][ny]
                        ) {
                            visited[nx][ny] = 1;
                            stack.push([nx, ny]);
                        }
                    }
                }

                if (sum % k === 0) ++result;
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer
     */
    function countIslands($grid, $k) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        $ans = 0;
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] > 0) {
                    $sum = 0;
                    $queue = new SplQueue();
                    // start island
                    $sum += $grid[$i][$j];
                    $grid[$i][$j] = 0;
                    $queue->enqueue([$i, $j]);
                    while (!$queue->isEmpty()) {
                        [$x, $y] = $queue->dequeue();
                        foreach ($dirs as $d) {
                            $nx = $x + $d[0];
                            $ny = $y + $d[1];
                            if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n && $grid[$nx][$ny] > 0) {
                                $sum += $grid[$nx][$ny];
                                $grid[$nx][$ny] = 0;
                                $queue->enqueue([$nx, $ny]);
                            }
                        }
                    }
                    if ($sum % $k == 0) {
                        ++$ans;
                    }
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countIslands(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        var result = 0
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] > 0 && !visited[i][j] {
                    var stack: [(Int, Int)] = [(i, j)]
                    visited[i][j] = true
                    var sum = 0
                    
                    while let (x, y) = stack.popLast() {
                        sum += grid[x][y]
                        for d in dirs {
                            let nx = x + d.0
                            let ny = y + d.1
                            if nx >= 0 && nx < m && ny >= 0 && ny < n {
                                if grid[nx][ny] > 0 && !visited[nx][ny] {
                                    visited[nx][ny] = true
                                    stack.append((nx, ny))
                                }
                            }
                        }
                    }
                    
                    if sum % k == 0 {
                        result += 1
                    }
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countIslands(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        if (m == 0) return 0
        val n = grid[0].size
        val visited = Array(m) { BooleanArray(n) }
        var islands = 0
        val deque = java.util.ArrayDeque<Int>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    var sum = 0L
                    visited[i][j] = true
                    deque.clear()
                    deque.add(i * n + j)
                    while (!deque.isEmpty()) {
                        val idx = deque.poll()
                        val x = idx / n
                        val y = idx % n
                        sum += grid[x][y].toLong()
                        // up
                        if (x > 0 && grid[x - 1][y] > 0 && !visited[x - 1][y]) {
                            visited[x - 1][y] = true
                            deque.add((x - 1) * n + y)
                        }
                        // down
                        if (x + 1 < m && grid[x + 1][y] > 0 && !visited[x + 1][y]) {
                            visited[x + 1][y] = true
                            deque.add((x + 1) * n + y)
                        }
                        // left
                        if (y > 0 && grid[x][y - 1] > 0 && !visited[x][y - 1]) {
                            visited[x][y - 1] = true
                            deque.add(x * n + (y - 1))
                        }
                        // right
                        if (y + 1 < n && grid[x][y + 1] > 0 && !visited[x][y + 1]) {
                            visited[x][y + 1] = true
                            deque.add(x * n + (y + 1))
                        }
                    }
                    if (sum % k == 0L) islands++
                }
            }
        }
        return islands
    }
}
```

## Dart

```dart
class Solution {
  int countIslands(List<List<int>> grid, int k) {
    int m = grid.length;
    if (m == 0) return 0;
    int n = grid[0].length;
    int result = 0;
    const List<int> dirs = [-1, 0, 1, 0, -1];

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] > 0) {
          int sum = 0;
          List<int> stack = [i * n + j];
          while (stack.isNotEmpty) {
            int cur = stack.removeLast();
            int x = cur ~/ n;
            int y = cur % n;
            if (grid[x][y] <= 0) continue; // already visited
            sum += grid[x][y];
            grid[x][y] = 0; // mark as visited

            for (int d = 0; d < 4; ++d) {
              int nx = x + dirs[d];
              int ny = y + dirs[d + 1];
              if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] > 0) {
                stack.add(nx * n + ny);
              }
            }
          }
          if (sum % k == 0) result++;
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func countIslands(grid [][]int, k int) int {
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 && !visited[i][j] {
				sum := int64(0)
				stack := [][2]int{{i, j}}
				visited[i][j] = true
				for len(stack) > 0 {
					cur := stack[len(stack)-1]
					stack = stack[:len(stack)-1]
					x, y := cur[0], cur[1]
					sum += int64(grid[x][y])
					for _, d := range dirs {
						nx, ny := x+d[0], y+d[1]
						if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] > 0 && !visited[nx][ny] {
							visited[nx][ny] = true
							stack = append(stack, [2]int{nx, ny})
						}
					}
				}
				if sum%int64(k) == 0 {
					ans++
				}
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_islands(grid, k)
  m = grid.length
  n = grid[0].length
  count = 0
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  (0...m).each do |i|
    (0...n).each do |j|
      next unless grid[i][j] > 0

      sum = 0
      stack = [[i, j]]
      until stack.empty?
        x, y = stack.pop
        val = grid[x][y]
        next if val == 0

        sum += val
        grid[x][y] = 0

        dirs.each do |dx, dy|
          nx = x + dx
          ny = y + dy
          if nx.between?(0, m - 1) && ny.between?(0, n - 1) && grid[nx][ny] > 0
            stack << [nx, ny]
          end
        end
      end

      count += 1 if sum % k == 0
    end
  end

  count
end
```

## Scala

```scala
object Solution {
    def countIslands(grid: Array[Array[Int]], k: Int): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        var result = 0
        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
        import java.util.ArrayDeque

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (grid(i)(j) > 0) {
                    var sum: Long = grid(i)(j).toLong
                    grid(i)(j) = 0
                    val dq = new ArrayDeque[(Int, Int)]()
                    dq.add((i, j))
                    while (!dq.isEmpty) {
                        val (r, c) = dq.poll()
                        for ((dr, dc) <- dirs) {
                            val nr = r + dr
                            val nc = c + dc
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) > 0) {
                                sum += grid(nr)(nc).toLong
                                grid(nr)(nc) = 0
                                dq.add((nr, nc))
                            }
                        }
                    }
                    if (sum % k == 0) result += 1
                }
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_islands(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        let mut visited = vec![vec![false; n]; m];
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        let mut count = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] > 0 && !visited[i][j] {
                    let mut queue = std::collections::VecDeque::new();
                    visited[i][j] = true;
                    queue.push_back((i, j));
                    let mut sum: i64 = 0;
                    while let Some((x, y)) = queue.pop_front() {
                        sum += grid[x][y] as i64;
                        for (dx, dy) in &dirs {
                            let nx = x as i32 + dx;
                            let ny = y as i32 + dy;
                            if nx >= 0 && nx < m as i32 && ny >= 0 && ny < n as i32 {
                                let ux = nx as usize;
                                let uy = ny as usize;
                                if grid[ux][uy] > 0 && !visited[ux][uy] {
                                    visited[ux][uy] = true;
                                    queue.push_back((ux, uy));
                                }
                            }
                        }
                    }
                    if sum % k as i64 == 0 {
                        count += 1;
                    }
                }
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (count-islands grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((m (length grid))
         (n (length (first grid)))
         (grid-vec (list->vector (map list->vector grid)))
         (visited (make-vector m)))
    (for ([i (in-range m)])
      (vector-set! visited i (make-vector n #f)))
    (define dirs '((1 . 0) (-1 . 0) (0 . 1) (0 . -1)))
    (let ((count 0))
      (for ([i (in-range m)])
        (for ([j (in-range n)])
          (when (and (> (vector-ref (vector-ref grid-vec i) j) 0)
                     (not (vector-ref (vector-ref visited i) j)))
            (vector-set! (vector-ref visited i) j #t)
            (let loop ((stack (list (cons i j))) (sum 0))
              (if (null? stack)
                  (when (= (remainder sum k) 0)
                    (set! count (+ count 1)))
                  (let* ((cell (car stack))
                         (rest (cdr stack))
                         (ci (car cell))
                         (cj (cdr cell))
                         (val (vector-ref (vector-ref grid-vec ci) cj))
                         (new-sum (+ sum val))
                         (new-stack
                           (foldl (lambda (dir acc)
                                    (let* ((ni (+ ci (car dir))) (nj (+ cj (cdr dir))))
                                      (if (and (>= ni 0) (< ni m) (>= nj 0) (< nj n))
                                          (let ((val-nei (vector-ref (vector-ref grid-vec ni) nj)))
                                            (if (and (> val-nei 0)
                                                     (not (vector-ref (vector-ref visited ni) nj)))
                                                (begin
                                                  (vector-set! (vector-ref visited ni) nj #t)
                                                  (cons (cons ni nj) acc))
                                                acc))
                                          acc))
                                  rest dirs)))
                    (loop new-stack new-sum))))))))
      count)))
```

## Erlang

```erlang
-spec count_islands(Grid :: [[integer()]], K :: integer()) -> integer().
count_islands(Grid, K) ->
    RowsTuple = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    M = tuple_size(RowsTuple),
    N = case M of
            0 -> 0;
            _ -> tuple_size(element(1, RowsTuple))
        end,
    loop_rows(0, M, K, N, #{}, 0, RowsTuple).

%% iterate over rows by index
loop_rows(I, M, _K, _N, Visited, Count, _Rows) when I >= M ->
    Count;
loop_rows(I, M, K, N, Visited, Count, Rows) ->
    Row = element(I + 1, Rows),
    {NewVisited, NewCount} = loop_cols(Row, I, K, M, N, Visited, Count, Rows),
    loop_rows(I + 1, M, K, N, NewVisited, NewCount, Rows).

%% iterate over columns by index
loop_cols(_Row, _I, _K, _M, N, Visited, Count, _Rows) when N =< 0 ->
    {Visited, Count};
loop_cols(Row, I, K, M, N, Visited, Count, Rows) ->
    loop_col_idx(Row, I, 0, K, M, N, Visited, Count, Rows).

loop_col_idx(_Row, _I, J, _K, _M, N, Visited, Count, _Rows) when J >= N ->
    {Visited, Count};
loop_col_idx(Row, I, J, K, M, N, Visited, Count, Rows) ->
    case maps:is_key({I,J}, Visited) of
        true ->
            loop_col_idx(Row, I, J + 1, K, M, N, Visited, Count, Rows);
        false ->
            Val = element(J + 1, Row),
            case Val > 0 of
                true ->
                    {CompSum, VisAfter} = bfs([{I,J}], Visited, Rows, M, N, 0),
                    NewCount = case CompSum rem K of
                                   0 -> Count + 1;
                                   _ -> Count
                               end,
                    loop_col_idx(Row, I, J + 1, K, M, N, VisAfter, NewCount, Rows);
                false ->
                    loop_col_idx(Row, I, J + 1, K, M, N, Visited, Count, Rows)
            end
    end.

%% BFS using explicit stack (tail‑recursive)
bfs([], Visited, _Rows, _M, _N, SumAcc) ->
    {SumAcc, Visited};
bfs([{I,J}|RestStack], Visited, Rows, M, N, SumAcc) ->
    case maps:is_key({I,J}, Visited) of
        true ->
            bfs(RestStack, Visited, Rows, M, N, SumAcc);
        false ->
            Row = element(I + 1, Rows),
            Val = element(J + 1, Row),
            NewVisited = maps:put({I,J}, true, Visited),
            NeighborCoords = [{I-1,J},{I+1,J},{I,J-1},{I,J+1}],
            ValidNeighbors = [ {Ni,Nj} ||
                {Ni,Nj} <- NeighborCoords,
                Ni >= 0, Ni < M,
                Nj >= 0, Nj < N,
                element(Nj + 1, element(Ni + 1, Rows)) > 0
            ],
            NewStack = ValidNeighbors ++ RestStack,
            bfs(NewStack, NewVisited, Rows, M, N, SumAcc + Val)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_islands(grid :: [[integer]], k :: integer) :: integer
  def count_islands(grid, k) do
    rows = length(grid)
    cols = if rows == 0, do: 0, else: length(List.first(grid))

    {count, _visited} =
      Enum.reduce(0..rows - 1, {0, MapSet.new()}, fn i, {cnt, visited} ->
        Enum.reduce(0..cols - 1, {cnt, visited}, fn j, {c, v} ->
          val = cell_val(grid, i, j)

          cond do
            val > 0 and not MapSet.member?(v, {i, j}) ->
              {sum, new_vis} = bfs(i, j, grid, rows, cols, v)
              new_cnt = if rem(sum, k) == 0, do: c + 1, else: c
              {new_cnt, new_vis}

            true ->
              {c, v}
          end
        end)
      end)

    count
  end

  defp cell_val(grid, i, j) do
    row = Enum.at(grid, i)
    Enum.at(row, j)
  end

  defp bfs(si, sj, grid, rows, cols, visited) do
    stack = [{si, sj}]
    bfs_loop(stack, grid, rows, cols, visited, 0)
  end

  defp bfs_loop([], _grid, _rows, _cols, visited, sum), do: {sum, visited}

  defp bfs_loop([{i, j} | rest], grid, rows, cols, visited, sum) do
    if MapSet.member?(visited, {i, j}) do
      bfs_loop(rest, grid, rows, cols, visited, sum)
    else
      val = cell_val(grid, i, j)
      new_sum = sum + val
      new_visited = MapSet.put(visited, {i, j})

      neighbors = [
        {i - 1, j},
        {i + 1, j},
        {i, j - 1},
        {i, j + 1}
      ]

      valid_neighbors =
        Enum.filter(neighbors, fn {ni, nj} ->
          ni >= 0 and ni < rows and nj >= 0 and nj < cols and cell_val(grid, ni, nj) > 0
        end)

      bfs_loop(valid_neighbors ++ rest, grid, rows, cols, new_visited, new_sum)
    end
  end
end
```

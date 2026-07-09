# 1020. Number of Enclaves

## Cpp

```cpp
class Solution {
public:
    int numEnclaves(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        std::queue<std::pair<int,int>> q;
        // enqueue boundary land cells
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || i == m-1 || j == 0 || j == n-1) {
                    if (grid[i][j] == 1) {
                        q.emplace(i, j);
                        grid[i][j] = 0;
                    }
                }
            }
        }
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            for (auto &d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                    grid[nx][ny] = 0;
                    q.emplace(nx, ny);
                }
            }
        }
        int enclaves = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (grid[i][j] == 1) ++enclaves;
        return enclaves;
    }
};
```

## Java

```java
class Solution {
    public int numEnclaves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        java.util.ArrayDeque<int[]> queue = new java.util.ArrayDeque<>();

        // Add boundary land cells to the queue
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 1) queue.add(new int[]{i, 0});
            if (n > 1 && grid[i][n - 1] == 1) queue.add(new int[]{i, n - 1});
        }
        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 1) queue.add(new int[]{0, j});
            if (m > 1 && grid[m - 1][j] == 1) queue.add(new int[]{m - 1, j});
        }

        // BFS to eliminate all land cells reachable from the boundary
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];
            if (grid[r][c] == 0) continue;
            grid[r][c] = 0; // mark as visited / water
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                    queue.add(new int[]{nr, nc});
                }
            }
        }

        // Count remaining land cells
        int enclaves = 0;
        for (int[] row : grid) {
            for (int val : row) {
                if (val == 1) enclaves++;
            }
        }
        return enclaves;
    }
}
```

## Python

```python
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        from collections import deque
        q = deque()
        # enqueue all boundary land cells
        for i in range(m):
            for j in (0, n - 1):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q.append((i, j))
        for j in range(n):
            for i in (0, m - 1):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny))
        return sum(map(sum, grid))
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        q = deque()
        # enqueue all boundary land cells
        for i in range(m):
            for j in (0, n - 1):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
        for j in range(n):
            for i in (0, m - 1):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
        # BFS to eliminate reachable lands
        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny))
        # count remaining land cells
        return sum(cell for row in grid for cell in row)
```

## C

```c
int numEnclaves(int** grid, int gridSize, int* gridColSize){
    int m = gridSize;
    if (m == 0) return 0;
    int n = gridColSize[0];
    int total = 0;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            if (grid[i][j] == 1) ++total;

    int max = m * n;
    int *qr = (int*)malloc(max * sizeof(int));
    int *qc = (int*)malloc(max * sizeof(int));
    int front = 0, back = 0;

    // enqueue land cells on the left and right borders
    for (int i = 0; i < m; ++i) {
        if (grid[i][0] == 1) {
            qr[back] = i;
            qc[back] = 0;
            ++back;
            grid[i][0] = 0;
            --total;
        }
        if (n > 1 && grid[i][n - 1] == 1) {
            qr[back] = i;
            qc[back] = n - 1;
            ++back;
            grid[i][n - 1] = 0;
            --total;
        }
    }

    // enqueue land cells on the top and bottom borders
    for (int j = 0; j < n; ++j) {
        if (grid[0][j] == 1) {
            qr[back] = 0;
            qc[back] = j;
            ++back;
            grid[0][j] = 0;
            --total;
        }
        if (m > 1 && grid[m - 1][j] == 1) {
            qr[back] = m - 1;
            qc[back] = j;
            ++back;
            grid[m - 1][j] = 0;
            --total;
        }
    }

    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    while (front < back) {
        int r = qr[front];
        int c = qc[front];
        ++front;
        for (int k = 0; k < 4; ++k) {
            int nr = r + dirs[k][0];
            int nc = c + dirs[k][1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                grid[nr][nc] = 0;
                --total;
                qr[back] = nr;
                qc[back] = nc;
                ++back;
            }
        }
    }

    free(qr);
    free(qc);
    return total;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int NumEnclaves(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        var q = new Queue<(int, int)>();
        
        // Top and bottom rows
        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 1) {
                q.Enqueue((0, j));
                grid[0][j] = 0;
            }
            if (grid[m - 1][j] == 1) {
                q.Enqueue((m - 1, j));
                grid[m - 1][j] = 0;
            }
        }
        
        // Left and right columns (excluding corners already processed)
        for (int i = 1; i < m - 1; i++) {
            if (grid[i][0] == 1) {
                q.Enqueue((i, 0));
                grid[i][0] = 0;
            }
            if (grid[i][n - 1] == 1) {
                q.Enqueue((i, n - 1));
                grid[i][n - 1] = 0;
            }
        }
        
        int[][] dirs = new int[][] {
            new int[] {1, 0},
            new int[] {-1, 0},
            new int[] {0, 1},
            new int[] {0, -1}
        };
        
        while (q.Count > 0) {
            var (x, y) = q.Dequeue();
            foreach (var d in dirs) {
                int nx = x + d[0];
                int ny = y + d[1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                    grid[nx][ny] = 0;
                    q.Enqueue((nx, ny));
                }
            }
        }
        
        int enclaveCount = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) enclaveCount++;
            }
        }
        return enclaveCount;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var numEnclaves = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    const q = [];
    let head = 0;

    // enqueue boundary land cells
    for (let i = 0; i < m; ++i) {
        if (grid[i][0] === 1) { grid[i][0] = 0; q.push([i, 0]); }
        if (n > 1 && grid[i][n-1] === 1) { grid[i][n-1] = 0; q.push([i, n-1]); }
    }
    for (let j = 0; j < n; ++j) {
        if (grid[0][j] === 1) { grid[0][j] = 0; q.push([0, j]); }
        if (m > 1 && grid[m-1][j] === 1) { grid[m-1][j] = 0; q.push([m-1, j]); }
    }

    // BFS to eliminate reachable land
    while (head < q.length) {
        const [x, y] = q[head++];
        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] === 1) {
                grid[nx][ny] = 0;
                q.push([nx, ny]);
            }
        }
    }

    // count remaining land cells
    let enclaves = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) enclaves++;
        }
    }
    return enclaves;
};
```

## Typescript

```typescript
function numEnclaves(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const queue: [number, number][] = [];

    // enqueue all land cells on the boundary
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (
                grid[i][j] === 1 &&
                (i === 0 || i === m - 1 || j === 0 || j === n - 1) &&
                !visited[i][j]
            ) {
                visited[i][j] = true;
                queue.push([i, j]);
            }
        }
    }

    let idx = 0;
    while (idx < queue.length) {
        const [x, y] = queue[idx++];
        for (const [dx, dy] of dirs) {
            const nx = x + dx,
                ny = y + dy;
            if (
                nx >= 0 &&
                nx < m &&
                ny >= 0 &&
                ny < n &&
                grid[nx][ny] === 1 &&
                !visited[nx][ny]
            ) {
                visited[nx][ny] = true;
                queue.push([nx, ny]);
            }
        }
    }

    let count = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1 && !visited[i][j]) {
                count++;
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
    function numEnclaves($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        $queue = new SplQueue();

        // Enqueue all boundary land cells and mark them visited (set to 0)
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i == 0 || $i == $m - 1 || $j == 0 || $j == $n - 1) {
                    if ($grid[$i][$j] == 1) {
                        $grid[$i][$j] = 0;
                        $queue->enqueue([$i, $j]);
                    }
                }
            }
        }

        $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        while (!$queue->isEmpty()) {
            [$x, $y] = $queue->dequeue();
            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n && $grid[$nx][$ny] == 1) {
                    $grid[$nx][$ny] = 0;
                    $queue->enqueue([$nx, $ny]);
                }
            }
        }

        // Count remaining land cells
        $count = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 1) {
                    $count++;
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
    func numEnclaves(_ grid: [[Int]]) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var g = grid
        var queue = [(Int, Int)]()
        var head = 0
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        // Enqueue all boundary land cells
        for i in 0..<m {
            for j in 0..<n where i == 0 || i == m - 1 || j == 0 || j == n - 1 {
                if g[i][j] == 1 {
                    g[i][j] = 0
                    queue.append((i, j))
                }
            }
        }
        
        // BFS to eliminate all land reachable from boundary
        while head < queue.count {
            let (x, y) = queue[head]
            head += 1
            for d in dirs {
                let nx = x + d.0
                let ny = y + d.1
                if nx >= 0 && nx < m && ny >= 0 && ny < n && g[nx][ny] == 1 {
                    g[nx][ny] = 0
                    queue.append((nx, ny))
                }
            }
        }
        
        // Count remaining land cells
        var result = 0
        for row in g {
            for cell in row where cell == 1 {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun numEnclaves(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val q: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        // Add boundary land cells to queue and mark visited (set to 0)
        for (i in 0 until m) {
            if (grid[i][0] == 1) {
                q.add(Pair(i, 0))
                grid[i][0] = 0
            }
            if (n > 1 && grid[i][n - 1] == 1) {
                q.add(Pair(i, n - 1))
                grid[i][n - 1] = 0
            }
        }
        for (j in 0 until n) {
            if (grid[0][j] == 1) {
                q.add(Pair(0, j))
                grid[0][j] = 0
            }
            if (m > 1 && grid[m - 1][j] == 1) {
                q.add(Pair(m - 1, j))
                grid[m - 1][j] = 0
            }
        }

        val dirs = intArrayOf(-1, 0, 1, 0, -1)
        while (q.isNotEmpty()) {
            val (x, y) = q.removeFirst()
            for (k in 0 until 4) {
                val nx = x + dirs[k]
                val ny = y + dirs[k + 1]
                if (nx in 0 until m && ny in 0 until n && grid[nx][ny] == 1) {
                    grid[nx][ny] = 0
                    q.add(Pair(nx, ny))
                }
            }
        }

        var count = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numEnclaves(List<List<int>> grid) {
    int m = grid.length;
    if (m == 0) return 0;
    int n = grid[0].length;

    List<int> stack = [];

    void bfs(int i, int j) {
      stack.add(i * n + j);
      while (stack.isNotEmpty) {
        int idx = stack.removeLast();
        int x = idx ~/ n;
        int y = idx % n;
        if (grid[x][y] == 0) continue;
        grid[x][y] = 0;
        if (x > 0 && grid[x - 1][y] == 1) stack.add((x - 1) * n + y);
        if (x < m - 1 && grid[x + 1][y] == 1) stack.add((x + 1) * n + y);
        if (y > 0 && grid[x][y - 1] == 1) stack.add(x * n + (y - 1));
        if (y < n - 1 && grid[x][y + 1] == 1) stack.add(x * n + (y + 1));
      }
    }

    for (int j = 0; j < n; ++j) {
      if (grid[0][j] == 1) bfs(0, j);
      if (m > 1 && grid[m - 1][j] == 1) bfs(m - 1, j);
    }
    for (int i = 1; i < m - 1; ++i) {
      if (grid[i][0] == 1) bfs(i, 0);
      if (n > 1 && grid[i][n - 1] == 1) bfs(i, n - 1);
    }

    int count = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func numEnclaves(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	queue := make([]int, 0)

	// enqueue boundary land cells
	for i := 0; i < m; i++ {
		if grid[i][0] == 1 {
			grid[i][0] = 0
			queue = append(queue, i*n)
		}
		if n > 1 && grid[i][n-1] == 1 {
			grid[i][n-1] = 0
			queue = append(queue, i*n+n-1)
		}
	}
	for j := 0; j < n; j++ {
		if grid[0][j] == 1 {
			grid[0][j] = 0
			queue = append(queue, j)
		}
		if m > 1 && grid[m-1][j] == 1 {
			grid[m-1][j] = 0
			queue = append(queue, (m-1)*n+j)
		}
	}

	// BFS to eliminate reachable lands
	for head := 0; head < len(queue); head++ {
		idx := queue[head]
		x, y := idx/n, idx%n
		for _, d := range dirs {
			nx, ny := x+d[0], y+d[1]
			if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1 {
				grid[nx][ny] = 0
				queue = append(queue, nx*n+ny)
			}
		}
	}

	// count remaining enclaved lands
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				ans++
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def num_enclaves(grid)
  m = grid.size
  n = grid[0].size
  dirs = [[1,0],[-1,0],[0,1],[0,-1]]
  q = []
  head = 0

  (0...m).each do |i|
    [0, n - 1].each do |j|
      if grid[i][j] == 1
        q << [i, j]
        grid[i][j] = 0
      end
    end
  end

  (0...n).each do |j|
    [0, m - 1].each do |i|
      if grid[i][j] == 1
        q << [i, j]
        grid[i][j] = 0
      end
    end
  end

  while head < q.size
    i, j = q[head]
    head += 1
    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      if ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 1
        grid[ni][nj] = 0
        q << [ni, nj]
      end
    end
  end

  cnt = 0
  grid.each { |row| row.each { |v| cnt += 1 if v == 1 } }
  cnt
end
```

## Scala

```scala
object Solution {
    def numEnclaves(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        val dirs = Array((1,0), (-1,0), (0,1), (0,-1))
        val q = scala.collection.mutable.Queue[(Int, Int)]()

        // enqueue boundary land cells and mark them visited
        for (i <- 0 until m) {
            if (grid(i)(0) == 1) { q.enqueue((i, 0)); grid(i)(0) = 0 }
            if (n > 1 && grid(i)(n - 1) == 1) { q.enqueue((i, n - 1)); grid(i)(n - 1) = 0 }
        }
        for (j <- 0 until n) {
            if (grid(0)(j) == 1) { q.enqueue((0, j)); grid(0)(j) = 0 }
            if (m > 1 && grid(m - 1)(j) == 1) { q.enqueue((m - 1, j)); grid(m - 1)(j) = 0 }
        }

        while (q.nonEmpty) {
            val (x, y) = q.dequeue()
            for ((dx, dy) <- dirs) {
                val nx = x + dx
                val ny = y + dy
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid(nx)(ny) == 1) {
                    grid(nx)(ny) = 0
                    q.enqueue((nx, ny))
                }
            }
        }

        var count = 0
        for (i <- 0 until m; j <- 0 until n) {
            if (grid(i)(j) == 1) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_enclaves(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        use std::collections::VecDeque;
        let dirs = [(-1i32, 0i32), (1, 0), (0, -1), (0, 1)];
        let mut bfs = |r: usize, c: usize, g: &mut Vec<Vec<i32>>| {
            let mut q = VecDeque::new();
            q.push_back((r, c));
            g[r][c] = 0;
            while let Some((x, y)) = q.pop_front() {
                for &(dx, dy) in &dirs {
                    let nx = x as i32 + dx;
                    let ny = y as i32 + dy;
                    if nx >= 0 && nx < m as i32 && ny >= 0 && ny < n as i32 {
                        let ux = nx as usize;
                        let uy = ny as usize;
                        if g[ux][uy] == 1 {
                            g[ux][uy] = 0;
                            q.push_back((ux, uy));
                        }
                    }
                }
            }
        };
        // top and bottom rows
        for j in 0..n {
            if grid[0][j] == 1 {
                bfs(0, j, &mut grid);
            }
            if m > 1 && grid[m - 1][j] == 1 {
                bfs(m - 1, j, &mut grid);
            }
        }
        // left and right columns
        for i in 0..m {
            if grid[i][0] == 1 {
                bfs(i, 0, &mut grid);
            }
            if n > 1 && grid[i][n - 1] == 1 {
                bfs(i, n - 1, &mut grid);
            }
        }
        let mut ans = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    ans += 1;
                }
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (num-enclaves grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (> m 0) (length (first grid)) 0))
         (vgrid (list->vector (map list->vector grid)))
         (directions (list (cons 1 0) (cons -1 0) (cons 0 1) (cons 0 -1))))
    (define (in-bounds? x y)
      (and (>= x 0) (< x m) (>= y 0) (< y n)))
    ;; Remove land reachable from the boundary
    (for ([i (in-range m)])
      (for ([j (in-range n)])
        (when (or (= i 0) (= i (- m 1)) (= j 0) (= j (- n 1)))
          (when (= (vector-ref (vector-ref vgrid i) j) 1)
            (let loop ((stack (list (cons i j))))
              (unless (null? stack)
                (define pos (car stack))
                (define rest (cdr stack))
                (define x (car pos))
                (define y (cdr pos))
                (when (= (vector-ref (vector-ref vgrid x) y) 1)
                  (vector-set! (vector-ref vgrid x) y 0)
                  (let ((new-stack
                         (foldl (lambda (dir acc)
                                  (define nx (+ x (car dir)))
                                  (define ny (+ y (cdr dir)))
                                  (if (and (in-bounds? nx ny)
                                           (= (vector-ref (vector-ref vgrid nx) ny) 1))
                                      (cons (cons nx ny) acc)
                                      acc))
                                rest
                                directions)))
                    (loop new-stack)))))))))
    ;; Count remaining land cells
    (let ((cnt 0))
      (for ([i (in-range m)])
        (for ([j (in-range n)])
          (when (= (vector-ref (vector-ref vgrid i) j) 1)
            (set! cnt (+ cnt 1)))))
      cnt)))
```

## Erlang

```erlang
-module(solution).
-export([num_enclaves/1]).

-spec num_enclaves(Grid :: [[integer()]]) -> integer().
num_enclaves(Grid) ->
    M = length(Grid),
    N = case Grid of [] -> 0; [Row|_] -> length(Row) end,
    RowTuples = [list_to_tuple(Row) || Row <- Grid],
    GridT = list_to_tuple(RowTuples),

    Queue0 = queue:new(),
    Visited0 = #{},
    {Queue1, Visited1} = init_boundary(M, N, GridT, Queue0, Visited0),
    VisitedFinal = bfs(Queue1, GridT, M, N, Visited1),
    count_enclaves(GridT, M, N, VisitedFinal).

init_boundary(M, N, GridT, Queue, Visited) ->
    Positions = [{I, J} ||
        I <- lists:seq(0, M - 1),
        J <- lists:seq(0, N - 1),
        (I == 0 orelse I == M - 1 orelse J == 0 orelse J == N - 1)],
    lists:foldl(
      fun({R, C}, {Q, Vis}) ->
          case get_cell(GridT, R, C) of
              1 ->
                  case maps:is_key({R, C}, Vis) of
                      true -> {Q, Vis};
                      false -> {queue:in({R, C}, Q), maps:put({R, C}, true, Vis)}
                  end;
              _ -> {Q, Vis}
          end
      end,
      {Queue, Visited},
      Positions).

bfs(Queue, GridT, M, N, Visited) ->
    case queue:out(Queue) of
        {empty, _} -> Visited;
        {{value, {R, C}}, Queue1} ->
            Neigh = [{R - 1, C}, {R + 1, C}, {R, C - 1}, {R, C + 1}],
            {NewQ, NewVis} =
                lists:foldl(
                  fun({NR, NC}, {QAcc, VAcc}) ->
                      if
                          NR >= 0, NR < M,
                          NC >= 0, NC < N,
                          get_cell(GridT, NR, NC) == 1,
                          not maps:is_key({NR, NC}, VAcc) ->
                              {queue:in({NR, NC}, QAcc), maps:put({NR, NC}, true, VAcc)};
                          true -> {QAcc, VAcc}
                      end
                  end,
                  {Queue1, Visited},
                  Neigh),
            bfs(NewQ, GridT, M, N, NewVis)
    end.

count_enclaves(GridT, M, N, Visited) ->
    lists:foldl(
      fun(R, AccRow) ->
          RowTuple = element(R + 1, GridT),
          RowCount = count_row(RowTuple, R, N, Visited),
          AccRow + RowCount
      end,
      0,
      lists:seq(0, M - 1)).

count_row(RowTuple, R, N, Visited) ->
    lists:foldl(
      fun(C, Acc) ->
          case element(C + 1, RowTuple) of
              1 ->
                  case maps:is_key({R, C}, Visited) of
                      true -> Acc;
                      false -> Acc + 1
                  end;
              _ -> Acc
          end
      end,
      0,
      lists:seq(0, N - 1)).

get_cell(GridT, R, C) ->
    RowTuple = element(R + 1, GridT),
    element(C + 1, RowTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_enclaves(grid :: [[integer]]) :: integer
  def num_enclaves(grid) do
    m = length(grid)
    n = length(hd grid)

    rows =
      grid
      |> Enum.map(&List.to_tuple/1)
      |> List.to_tuple()

    # collect all boundary coordinates
    boundary_coords =
      Enum.concat(
        for i <- 0..(m - 1) do
          [{i, 0}, {i, n - 1}]
        end,
        for j <- 0..(n - 1) do
          [{0, j}, {m - 1, j}]
        end
      )

    visited =
      Enum.reduce(boundary_coords, MapSet.new(), fn {i, j}, vis ->
        if cell_one?(rows, i, j) and not MapSet.member?(vis, {i, j}) do
          dfs(i, j, rows, m, n, vis)
        else
          vis
        end
      end)

    # count remaining land cells not visited
    Enum.reduce(0..(m - 1), 0, fn i, acc ->
      row = elem(rows, i)

      cnt =
        Enum.reduce(0..(n - 1), 0, fn j, a2 ->
          if elem(row, j) == 1 and not MapSet.member?(visited, {i, j}) do
            a2 + 1
          else
            a2
          end
        end)

      acc + cnt
    end)
  end

  defp cell_one?(rows, i, j) do
    elem(elem(rows, i), j) == 1
  end

  defp dfs(i, j, rows, m, n, visited) do
    stack = [{i, j}]
    dfs_iter(stack, rows, m, n, visited)
  end

  defp dfs_iter([], _rows, _m, _n, visited), do: visited

  defp dfs_iter([{ci, cj} | rest], rows, m, n, visited) do
    if MapSet.member?(visited, {ci, cj}) do
      dfs_iter(rest, rows, m, n, visited)
    else
      if cell_one?(rows, ci, cj) do
        new_visited = MapSet.put(visited, {ci, cj})

        neighbors = []

        neighbors =
          if ci > 0, do: [{ci - 1, cj} | neighbors], else: neighbors

        neighbors =
          if ci < m - 1, do: [{ci + 1, cj} | neighbors], else: neighbors

        neighbors =
          if cj > 0, do: [{ci, cj - 1} | neighbors], else: neighbors

        neighbors =
          if cj < n - 1, do: [{ci, cj + 1} | neighbors], else: neighbors

        dfs_iter(neighbors ++ rest, rows, m, n, new_visited)
      else
        dfs_iter(rest, rows, m, n, visited)
      end
    end
  end
end
```

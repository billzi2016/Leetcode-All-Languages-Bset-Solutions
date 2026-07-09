# 0959. Regions Cut By Slashes

## Cpp

```cpp
class Solution {
public:
    int regionsBySlashes(std::vector<std::string>& grid) {
        int n = grid.size();
        int m = n * 3;
        std::vector<std::vector<int>> g(m, std::vector<int>(m, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                char c = grid[i][j];
                if (c == '/') {
                    g[i*3][j*3+2] = 1;
                    g[i*3+1][j*3+1] = 1;
                    g[i*3+2][j*3] = 1;
                } else if (c == '\\') {
                    g[i*3][j*3] = 1;
                    g[i*3+1][j*3+1] = 1;
                    g[i*3+2][j*3+2] = 1;
                }
            }
        }
        int regions = 0;
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < m; ++j) {
                if (g[i][j] == 0) {
                    ++regions;
                    std::deque<std::pair<int,int>> q;
                    q.emplace_back(i,j);
                    g[i][j] = 1;
                    while (!q.empty()) {
                        auto [r,c] = q.front(); q.pop_front();
                        for (auto &d : dirs) {
                            int nr = r + d[0];
                            int nc = c + d[1];
                            if (nr >= 0 && nr < m && nc >= 0 && nc < m && g[nr][nc] == 0) {
                                g[nr][nc] = 1;
                                q.emplace_back(nr,nc);
                            }
                        }
                    }
                }
            }
        }
        return regions;
    }
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int regionsBySlashes(String[] grid) {
        int n = grid.length;
        int N = n * 3;
        int[][] map = new int[N][N];

        for (int i = 0; i < n; i++) {
            String row = grid[i];
            for (int j = 0; j < n; j++) {
                char c = row.charAt(j);
                if (c == '/') {
                    map[i * 3][j * 3 + 2] = 1;
                    map[i * 3 + 1][j * 3 + 1] = 1;
                    map[i * 3 + 2][j * 3] = 1;
                } else if (c == '\\') {
                    map[i * 3][j * 3] = 1;
                    map[i * 3 + 1][j * 3 + 1] = 1;
                    map[i * 3 + 2][j * 3 + 2] = 1;
                }
            }
        }

        int regions = 0;
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 0) {
                    regions++;
                    Deque<int[]> stack = new ArrayDeque<>();
                    stack.push(new int[]{i, j});
                    map[i][j] = 1;
                    while (!stack.isEmpty()) {
                        int[] cur = stack.pop();
                        int r = cur[0], c = cur[1];
                        for (int d = 0; d < 4; d++) {
                            int nr = r + dr[d];
                            int nc = c + dc[d];
                            if (nr >= 0 && nr < N && nc >= 0 && nc < N && map[nr][nc] == 0) {
                                map[nr][nc] = 1;
                                stack.push(new int[]{nr, nc});
                            }
                        }
                    }
                }
            }
        }

        return regions;
    }
}
```

## Python

```python
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        N = n * 3
        expanded = [[0] * N for _ in range(N)]

        for i in range(n):
            row = grid[i]
            for j, ch in enumerate(row):
                r, c = i * 3, j * 3
                if ch == '/':
                    expanded[r][c + 2] = 1
                    expanded[r + 1][c + 1] = 1
                    expanded[r + 2][c] = 1
                elif ch == '\\':
                    expanded[r][c] = 1
                    expanded[r + 1][c + 1] = 1
                    expanded[r + 2][c + 2] = 1

        from collections import deque
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        regions = 0

        for i in range(N):
            for j in range(N):
                if expanded[i][j] == 0:
                    regions += 1
                    dq = deque()
                    dq.append((i, j))
                    expanded[i][j] = 1
                    while dq:
                        x, y = dq.popleft()
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < N and expanded[nx][ny] == 0:
                                expanded[nx][ny] = 1
                                dq.append((nx, ny))
        return regions
```

## Python3

```python
from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = n * 3
        expanded = [[0] * m for _ in range(m)]

        for i in range(n):
            row = grid[i]
            for j in range(n):
                ch = row[j]
                base_r, base_c = i * 3, j * 3
                if ch == '/':
                    expanded[base_r][base_c + 2] = 1
                    expanded[base_r + 1][base_c + 1] = 1
                    expanded[base_r + 2][base_c] = 1
                elif ch == '\\':
                    expanded[base_r][base_c] = 1
                    expanded[base_r + 1][base_c + 1] = 1
                    expanded[base_r + 2][base_c + 2] = 1

        def bfs(sr: int, sc: int) -> None:
            stack = [(sr, sc)]
            while stack:
                r, c = stack.pop()
                if r < 0 or r >= m or c < 0 or c >= m or expanded[r][c]:
                    continue
                expanded[r][c] = 1
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))

        regions = 0
        for i in range(m):
            for j in range(m):
                if expanded[i][j] == 0:
                    bfs(i, j)
                    regions += 1

        return regions
```

## C

```c
#include <stdlib.h>

static int find(int *parent, int x) {
    if (parent[x] == -1) return x;
    parent[x] = find(parent, parent[x]);
    return parent[x];
}

static void unite(int *parent, int *regions, int a, int b) {
    int pa = find(parent, a);
    int pb = find(parent, b);
    if (pa != pb) {
        parent[pa] = pb;
        (*regions)--;
    }
}

/* grid: array of strings, each string length == gridSize */
int regionsBySlashes(char** grid, int gridSize) {
    int n = gridSize;
    int total = n * n * 4;               // 4 triangles per cell
    int *parent = (int *)malloc(sizeof(int) * total);
    for (int i = 0; i < total; ++i) parent[i] = -1;

    int regions = total;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            char c = grid[i][j];
            int base = (i * n + j) * 4; // indices: 0 top,1 right,2 bottom,3 left

            if (i > 0) { // connect with cell above
                int upBase = ((i - 1) * n + j) * 4;
                unite(parent, &regions, base + 0, upBase + 2);
            }
            if (j > 0) { // connect with left cell
                int leftBase = (i * n + (j - 1)) * 4;
                unite(parent, &regions, base + 3, leftBase + 1);
            }

            if (c != '/') {
                unite(parent, &regions, base + 0, base + 1); // top-right
                unite(parent, &regions, base + 2, base + 3); // bottom-left
            }
            if (c != '\\') {
                unite(parent, &regions, base + 0, base + 3); // top-left
                unite(parent, &regions, base + 2, base + 1); // bottom-right
            }
        }
    }

    free(parent);
    return regions;
}
```

## Csharp

```csharp
public class Solution
{
    public int RegionsBySlashes(string[] grid)
    {
        int n = grid.Length;
        int N = n * 3;
        int[,] g = new int[N, N];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                char c = grid[i][j];
                if (c == '/')
                {
                    g[3 * i,     3 * j + 2] = 1;
                    g[3 * i + 1, 3 * j + 1] = 1;
                    g[3 * i + 2, 3 * j    ] = 1;
                }
                else if (c == '\\')
                {
                    g[3 * i,     3 * j    ] = 1;
                    g[3 * i + 1, 3 * j + 1] = 1;
                    g[3 * i + 2, 3 * j + 2] = 1;
                }
            }
        }

        int regions = 0;
        int[] dr = { -1, 1, 0, 0 };
        int[] dc = { 0, 0, -1, 1 };

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (g[i, j] == 0)
                {
                    regions++;
                    var q = new System.Collections.Generic.Queue<int>();
                    q.Enqueue(i * N + j);
                    g[i, j] = 1;

                    while (q.Count > 0)
                    {
                        int cur = q.Dequeue();
                        int r = cur / N;
                        int c = cur % N;

                        for (int d = 0; d < 4; d++)
                        {
                            int nr = r + dr[d];
                            int nc = c + dc[d];
                            if (nr >= 0 && nr < N && nc >= 0 && nc < N && g[nr, nc] == 0)
                            {
                                g[nr, nc] = 1;
                                q.Enqueue(nr * N + nc);
                            }
                        }
                    }
                }
            }
        }

        return regions;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} grid
 * @return {number}
 */
var regionsBySlashes = function(grid) {
    const n = grid.length;
    const N = n * 3;
    const expanded = Array.from({ length: N }, () => Array(N).fill(0));

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const ch = grid[i][j];
            const r = i * 3;
            const c = j * 3;
            if (ch === '/') {
                expanded[r][c + 2] = 1;
                expanded[r + 1][c + 1] = 1;
                expanded[r + 2][c] = 1;
            } else if (ch === '\\') {
                expanded[r][c] = 1;
                expanded[r + 1][c + 1] = 1;
                expanded[r + 2][c + 2] = 1;
            }
        }
    }

    let regions = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (expanded[i][j] === 0) {
                regions++;
                const stack = [[i, j]];
                expanded[i][j] = 1;
                while (stack.length) {
                    const [x, y] = stack.pop();
                    for (const [dx, dy] of dirs) {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (
                            nx >= 0 && nx < N &&
                            ny >= 0 && ny < N &&
                            expanded[nx][ny] === 0
                        ) {
                            expanded[nx][ny] = 1;
                            stack.push([nx, ny]);
                        }
                    }
                }
            }
        }
    }

    return regions;
};
```

## Typescript

```typescript
function regionsBySlashes(grid: string[]): number {
    const n = grid.length;
    const size = n * 3;
    const expanded: number[][] = Array.from({ length: size }, () => new Array<number>(size).fill(0));

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const ch = grid[i][j];
            const r = i * 3;
            const c = j * 3;
            if (ch === '/') {
                expanded[r][c + 2] = 1;
                expanded[r + 1][c + 1] = 1;
                expanded[r + 2][c] = 1;
            } else if (ch === '\\') {
                expanded[r][c] = 1;
                expanded[r + 1][c + 1] = 1;
                expanded[r + 2][c + 2] = 1;
            }
        }
    }

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    let regions = 0;
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            if (expanded[i][j] === 0) {
                regions++;
                const stack: [number, number][] = [[i, j]];
                expanded[i][j] = 1;
                while (stack.length) {
                    const [r, c] = stack.pop()!;
                    for (const [dr, dc] of dirs) {
                        const nr = r + dr;
                        const nc = c + dc;
                        if (
                            nr >= 0 &&
                            nr < size &&
                            nc >= 0 &&
                            nc < size &&
                            expanded[nr][nc] === 0
                        ) {
                            expanded[nr][nc] = 1;
                            stack.push([nr, nc]);
                        }
                    }
                }
            }
        }
    }

    return regions;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $grid
     * @return Integer
     */
    function regionsBySlashes($grid) {
        $n = count($grid);
        $size = $n * 3;
        // Initialize expanded grid with zeros
        $expanded = array_fill(0, $size, array_fill(0, $size, 0));
        
        for ($i = 0; $i < $n; $i++) {
            $rowStr = $grid[$i];
            for ($j = 0; $j < $n; $j++) {
                $c = $rowStr[$j];
                $baseR = $i * 3;
                $baseC = $j * 3;
                if ($c === '/') {
                    $expanded[$baseR + 0][$baseC + 2] = 1;
                    $expanded[$baseR + 1][$baseC + 1] = 1;
                    $expanded[$baseR + 2][$baseC + 0] = 1;
                } elseif ($c === '\\') {
                    $expanded[$baseR + 0][$baseC + 0] = 1;
                    $expanded[$baseR + 1][$baseC + 1] = 1;
                    $expanded[$baseR + 2][$baseC + 2] = 1;
                }
            }
        }
        
        $regions = 0;
        $dr = [1, -1, 0, 0];
        $dc = [0, 0, 1, -1];
        
        for ($r = 0; $r < $size; $r++) {
            for ($c = 0; $c < $size; $c++) {
                if ($expanded[$r][$c] === 0) {
                    $regions++;
                    // BFS to fill the region
                    $queue = new SplQueue();
                    $queue->enqueue([$r, $c]);
                    $expanded[$r][$c] = 1;
                    while (!$queue->isEmpty()) {
                        [$cr, $cc] = $queue->dequeue();
                        for ($k = 0; $k < 4; $k++) {
                            $nr = $cr + $dr[$k];
                            $nc = $cc + $dc[$k];
                            if ($nr >= 0 && $nr < $size && $nc >= 0 && $nc < $size && $expanded[$nr][$nc] === 0) {
                                $expanded[$nr][$nc] = 1;
                                $queue->enqueue([$nr, $nc]);
                            }
                        }
                    }
                }
            }
        }
        
        return $regions;
    }
}
```

## Swift

```swift
class Solution {
    func regionsBySlashes(_ grid: [String]) -> Int {
        let n = grid.count
        let size = n * 3
        var expanded = Array(repeating: Array(repeating: 0, count: size), count: size)
        
        for i in 0..<n {
            let chars = Array(grid[i])
            for j in 0..<n {
                let ch = chars[j]
                if ch == "/" {
                    expanded[i*3][j*3+2] = 1
                    expanded[i*3+1][j*3+1] = 1
                    expanded[i*3+2][j*3] = 1
                } else if ch == "\\" {
                    expanded[i*3][j*3] = 1
                    expanded[i*3+1][j*3+1] = 1
                    expanded[i*3+2][j*3+2] = 1
                }
            }
        }
        
        let dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        var regions = 0
        
        for i in 0..<size {
            for j in 0..<size {
                if expanded[i][j] == 0 {
                    regions += 1
                    var queue: [(Int, Int)] = [(i, j)]
                    expanded[i][j] = 1
                    var idx = 0
                    while idx < queue.count {
                        let (r, c) = queue[idx]
                        idx += 1
                        for d in dirs {
                            let nr = r + d.0
                            let nc = c + d.1
                            if nr >= 0 && nr < size && nc >= 0 && nc < size && expanded[nr][nc] == 0 {
                                expanded[nr][nc] = 1
                                queue.append((nr, nc))
                            }
                        }
                    }
                }
            }
        }
        
        return regions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun regionsBySlashes(grid: Array<String>): Int {
        val n = grid.size
        val size = n * 3
        val expanded = Array(size) { IntArray(size) }
        for (i in 0 until n) {
            val row = grid[i]
            for (j in 0 until n) {
                val ch = row[j]
                val r = i * 3
                val c = j * 3
                when (ch) {
                    '/' -> {
                        expanded[r][c + 2] = 1
                        expanded[r + 1][c + 1] = 1
                        expanded[r + 2][c] = 1
                    }
                    '\\' -> {
                        expanded[r][c] = 1
                        expanded[r + 1][c + 1] = 1
                        expanded[r + 2][c + 2] = 1
                    }
                }
            }
        }

        var regions = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        val deque: java.util.ArrayDeque<IntArray> = java.util.ArrayDeque()
        for (i in 0 until size) {
            for (j in 0 until size) {
                if (expanded[i][j] == 0) {
                    regions++
                    deque.clear()
                    deque.add(intArrayOf(i, j))
                    expanded[i][j] = 1
                    while (!deque.isEmpty()) {
                        val cur = deque.poll()
                        val x = cur[0]
                        val y = cur[1]
                        for (d in dirs) {
                            val nx = x + d[0]
                            val ny = y + d[1]
                            if (nx >= 0 && nx < size && ny >= 0 && ny < size && expanded[nx][ny] == 0) {
                                expanded[nx][ny] = 1
                                deque.add(intArrayOf(nx, ny))
                            }
                        }
                    }
                }
            }
        }

        return regions
    }
}
```

## Dart

```dart
class Solution {
  int regionsBySlashes(List<String> grid) {
    int n = grid.length;
    int N = n * 3;
    List<List<int>> expanded = List.generate(N, (_) => List.filled(N, 0));

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        String ch = grid[i][j];
        int baseRow = i * 3;
        int baseCol = j * 3;
        if (ch == '/') {
          expanded[baseRow][baseCol + 2] = 1;
          expanded[baseRow + 1][baseCol + 1] = 1;
          expanded[baseRow + 2][baseCol] = 1;
        } else if (ch == '\\') {
          expanded[baseRow][baseCol] = 1;
          expanded[baseRow + 1][baseCol + 1] = 1;
          expanded[baseRow + 2][baseCol + 2] = 1;
        }
      }
    }

    int regions = 0;
    List<List<int>> dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        if (expanded[i][j] == 0) {
          regions++;
          List<List<int>> stack = [];
          stack.add([i, j]);
          while (stack.isNotEmpty) {
            var cur = stack.removeLast();
            int x = cur[0];
            int y = cur[1];
            if (x < 0 || x >= N || y < 0 || y >= N || expanded[x][y] != 0) continue;
            expanded[x][y] = 1;
            for (var d in dirs) {
              stack.add([x + d[0], y + d[1]]);
            }
          }
        }
      }
    }

    return regions;
  }
}
```

## Golang

```go
func regionsBySlashes(grid []string) int {
	n := len(grid)
	size := n * 3
	expanded := make([][]int, size)
	for i := 0; i < size; i++ {
		expanded[i] = make([]int, size)
	}
	for i := 0; i < n; i++ {
		row := grid[i]
		for j := 0; j < n; j++ {
			ch := row[j]
			baseR, baseC := i*3, j*3
			if ch == '/' {
				expanded[baseR][baseC+2] = 1
				expanded[baseR+1][baseC+1] = 1
				expanded[baseR+2][baseC] = 1
			} else if ch == '\\' {
				expanded[baseR][baseC] = 1
				expanded[baseR+1][baseC+1] = 1
				expanded[baseR+2][baseC+2] = 1
			}
		}
	}

	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	regions := 0

	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			if expanded[i][j] == 0 {
				regions++
				queue := make([][2]int, 0)
				queue = append(queue, [2]int{i, j})
				expanded[i][j] = 1
				for len(queue) > 0 {
					cur := queue[0]
					queue = queue[1:]
					r, c := cur[0], cur[1]
					for _, d := range dirs {
						nr, nc := r+d[0], c+d[1]
						if nr >= 0 && nr < size && nc >= 0 && nc < size && expanded[nr][nc] == 0 {
							expanded[nr][nc] = 1
							queue = append(queue, [2]int{nr, nc})
						}
					}
				}
			}
		}
	}

	return regions
}
```

## Ruby

```ruby
def regions_by_slashes(grid)
  n = grid.size
  size = n * 3
  expanded = Array.new(size) { Array.new(size, 0) }

  (0...n).each do |i|
    row = grid[i]
    (0...n).each do |j|
      ch = row[j]
      r = i * 3
      c = j * 3
      if ch == '/'
        expanded[r][c + 2] = 1
        expanded[r + 1][c + 1] = 1
        expanded[r + 2][c] = 1
      elsif ch == '\\'
        expanded[r][c] = 1
        expanded[r + 1][c + 1] = 1
        expanded[r + 2][c + 2] = 1
      end
    end
  end

  visited = Array.new(size) { Array.new(size, false) }
  dirs = [[1,0],[-1,0],[0,1],[0,-1]]
  regions = 0

  (0...size).each do |i|
    (0...size).each do |j|
      next if expanded[i][j] == 1 || visited[i][j]
      queue = [[i, j]]
      visited[i][j] = true
      head = 0
      while head < queue.size
        x, y = queue[head]
        head += 1
        dirs.each do |dx, dy|
          nx = x + dx
          ny = y + dy
          if nx >= 0 && nx < size && ny >= 0 && ny < size &&
             expanded[nx][ny] == 0 && !visited[nx][ny]
            visited[nx][ny] = true
            queue << [nx, ny]
          end
        end
      end
      regions += 1
    end
  end

  regions
end
```

## Scala

```scala
object Solution {
    def regionsBySlashes(grid: Array[String]): Int = {
        val n = grid.length
        val total = n * n * 4
        val parent = Array.fill[Int](total)(-1)
        var count = total

        def find(x: Int): Int = {
            if (parent(x) == -1) x
            else {
                val p = find(parent(x))
                parent(x) = p
                p
            }
        }

        def union(a: Int, b: Int): Unit = {
            var pa = find(a)
            var pb = find(b)
            if (pa != pb) {
                parent(pa) = pb
                count -= 1
            }
        }

        for (i <- 0 until n) {
            for (j <- 0 until n) {
                val base = (i * n + j) * 4
                val ch = grid(i)(j)

                if (ch != '\\') {
                    union(base + 0, base + 1) // top - right
                    union(base + 2, base + 3) // bottom - left
                }
                if (ch != '/') {
                    union(base + 0, base + 3) // top - left
                    union(base + 2, base + 1) // bottom - right
                }

                if (i > 0) {
                    val above = ((i - 1) * n + j) * 4 + 2 // above cell's bottom triangle
                    union(base + 0, above)               // current top with above bottom
                }
                if (j > 0) {
                    val left = (i * n + (j - 1)) * 4 + 1 // left cell's right triangle
                    union(base + 3, left)                // current left with left right
                }
            }
        }

        count
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn regions_by_slashes(grid: Vec<String>) -> i32 {
        let n = grid.len();
        let size = n * 3;
        let mut expanded = vec![vec![0u8; size]; size];

        for (i, row) in grid.iter().enumerate() {
            let bytes = row.as_bytes();
            for j in 0..n {
                let ch = bytes[j] as char;
                let bi = i * 3;
                let bj = j * 3;
                match ch {
                    '/' => {
                        expanded[bi][bj + 2] = 1;
                        expanded[bi + 1][bj + 1] = 1;
                        expanded[bi + 2][bj] = 1;
                    }
                    '\\' => {
                        expanded[bi][bj] = 1;
                        expanded[bi + 1][bj + 1] = 1;
                        expanded[bi + 2][bj + 2] = 1;
                    }
                    _ => {}
                }
            }
        }

        let mut regions = 0i32;
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];

        for i in 0..size {
            for j in 0..size {
                if expanded[i][j] == 0 {
                    regions += 1;
                    let mut q = VecDeque::new();
                    q.push_back((i, j));
                    expanded[i][j] = 1;
                    while let Some((r, c)) = q.pop_front() {
                        for (dr, dc) in &dirs {
                            let nr = r as i32 + dr;
                            let nc = c as i32 + dc;
                            if nr >= 0 && nr < size as i32 && nc >= 0 && nc < size as i32 {
                                let ur = nr as usize;
                                let uc = nc as usize;
                                if expanded[ur][uc] == 0 {
                                    expanded[ur][uc] = 1;
                                    q.push_back((ur, uc));
                                }
                            }
                        }
                    }
                }
            }
        }

        regions
    }
}
```

## Racket

```racket
#lang racket

(define/contract (regions-by-slashes grid)
  (-> (listof string?) exact-integer?)
  (let* ((n (length grid))
         (m (* n 3))
         (g (make-vector m)))
    ;; initialize expanded grid with zeros
    (for ([i (in-range m)])
      (vector-set! g i (make-vector m 0)))
    ;; draw slashes as barriers
    (for ([i (in-range n)])
      (let ((row-str (list-ref grid i)))
        (for ([j (in-range n)])
          (let* ((ch (string-ref row-str j))
                 (base (* i 3))
                 (base-col (* j 3)))
            (cond [(char=? ch #\\)
                   (for ([k (in-range 3)])
                     (let ((r (+ base k))
                           (c (+ base-col k)))
                       (vector-set! (vector-ref g r) c 1)))]
                  [(char=? ch #\/)
                   (for ([k (in-range 3)])
                     (let ((r (+ base k))
                           (c (+ base-col (- 2 k))))
                       (vector-set! (vector-ref g r) c 1)))])))))
    ;; flood‑fill to count regions
    (define dirs '((0 1) (0 -1) (1 0) (-1 0)))
    (let ((count 0))
      (for ([i (in-range m)])
        (for ([j (in-range m)])
          (when (= (vector-ref (vector-ref g i) j) 0)
            (set! count (+ count 1))
            ;; depth‑first search using an explicit stack
            (let loop ((stack (list (cons i j))))
              (unless (null? stack)
                (define cur (car stack))
                (define rest (cdr stack))
                (define r (car cur))
                (define c (cdr cur))
                (if (= (vector-ref (vector-ref g r) c) 1)
                    (loop rest)
                    (begin
                      (vector-set! (vector-ref g r) c 1)
                      (let ((new-stack rest))
                        (for ([d dirs])
                          (define dr (car d))
                          (define dc (cadr d))
                          (define nr (+ r dr))
                          (define nc (+ c dc))
                          (when (and (>= nr 0) (< nr m)
                                     (>= nc 0) (< nc m)
                                     (= (vector-ref (vector-ref g nr) nc) 0))
                            (set! new-stack (cons (cons nr nc) new-stack))))
                        (loop new-stack)))))))))
      count)))
```

## Erlang

```erlang
-module(solution).
-export([regions_by_slashes/1]).
-spec regions_by_slashes(Grid :: [unicode:unicode_binary()]) -> integer().
regions_by_slashes(Grid) ->
    N = length(Grid),
    Size = N * 3,
    BlockedSet = build_blocked_set(Grid, N),
    {Count, _Visited} = process_rows(0, Size, BlockedSet, #{}, 0),
    Count.

%% Build blocked cells set
build_blocked_set(Grid, N) ->
    build_blocked_set(Grid, 0, #{}, N).

build_blocked_set([], _RowIdx, Acc, _N) -> Acc;
build_blocked_set([Bin|Rest], RowIdx, Acc, N) ->
    Str = binary_to_list(Bin),
    Acc1 = build_row(Str, RowIdx, 0, Acc, N),
    build_blocked_set(Rest, RowIdx + 1, Acc1, N).

build_row(_Str, _RowIdx, ColIdx, Acc, N) when ColIdx >= N -> Acc;
build_row(Str, RowIdx, ColIdx, Acc, N) ->
    Char = lists:nth(ColIdx + 1, Str),
    BaseR = RowIdx * 3,
    BaseC = ColIdx * 3,
    NewAcc = case Char of
        $\\ ->
            add_backslash(BaseR, BaseC, Acc);
        $/ ->
            add_slash(BaseR, BaseC, Acc);
        _ -> Acc
    end,
    build_row(Str, RowIdx, ColIdx + 1, NewAcc, N).

add_backslash(R, C, Acc) ->
    Acc1 = maps:put({R, C}, true, Acc),
    Acc2 = maps:put({R+1, C+1}, true, Acc1),
    maps:put({R+2, C+2}, true, Acc2).

add_slash(R, C, Acc) ->
    Acc1 = maps:put({R, C+2}, true, Acc),
    Acc2 = maps:put({R+1, C+1}, true, Acc1),
    maps:put({R+2, C}, true, Acc2).

%% Process rows to count regions
process_rows(R, Size, BlockedSet, Visited, Count) when R < Size ->
    {Visited1, Count1} = process_cols(R, 0, Size, BlockedSet, Visited, Count),
    process_rows(R + 1, Size, BlockedSet, Visited1, Count1);
process_rows(_, _, _, Visited, Count) -> {Count, Visited}.

%% Process columns within a row
process_cols(_R, C, _Size, _BlockedSet, Visited, Count) when C >= _Size ->
    {Visited, Count};
process_cols(R, C, Size, BlockedSet, Visited, Count) ->
    case (maps:is_key({R, C}, BlockedSet) orelse maps:is_key({R, C}, Visited)) of
        true ->
            process_cols(R, C + 1, Size, BlockedSet, Visited, Count);
        false ->
            Visited2 = bfs([{R, C}], BlockedSet, Visited, Size),
            process_cols(R, C + 1, Size, BlockedSet, Visited2, Count + 1)
    end.

%% BFS to mark all cells of a region
bfs(Queue, BlockedSet, Visited, Size) ->
    bfs_loop(Queue, BlockedSet, Visited, Size).

bfs_loop([], _BlockedSet, Visited, _Size) -> Visited;
bfs_loop([{R, C} | Rest], BlockedSet, Visited, Size) ->
    Visited1 = maps:put({R, C}, true, Visited),
    Neighs = [{R-1, C}, {R+1, C}, {R, C-1}, {R, C+1}],
    {Queue2, Visited2} = lists:foldl(
        fun({NR, NC}, {QAcc, VAcc}) ->
            if NR >= 0, NC >= 0, NR < Size, NC < Size,
               not maps:is_key({NR, NC}, BlockedSet),
               not maps:is_key({NR, NC}, VAcc) ->
                    {[{NR, NC} | QAcc], VAcc};
               true -> {QAcc, VAcc}
            end
        end,
        {Rest, Visited1},
        Neighs),
    bfs_loop(Queue2, BlockedSet, Visited2, Size).
```

## Elixir

```elixir
defmodule Solution do
  @spec regions_by_slashes(grid :: [String.t]) :: integer
  def regions_by_slashes(grid) do
    n = length(grid)

    # Convert each string to a charlist for easy indexing
    rows = Enum.map(grid, &String.to_charlist/1)

    # Build set of blocked cells in the expanded 3n x 3n grid
    blocked =
      Enum.reduce(0..(n - 1), MapSet.new(), fn i, acc ->
        row_chars = Enum.at(rows, i)

        Enum.reduce(0..(n - 1), acc, fn j, acc2 ->
          ch = Enum.at(row_chars, j)
          base_r = i * 3
          base_c = j * 3

          case ch do
            ?/ ->
              acc2
              |> MapSet.put({base_r, base_c + 2})
              |> MapSet.put({base_r + 1, base_c + 1})
              |> MapSet.put({base_r + 2, base_c})

            ?\\ ->
              acc2
              |> MapSet.put({base_r, base_c})
              |> MapSet.put({base_r + 1, base_c + 1})
              |> MapSet.put({base_r + 2, base_c + 2})

            _ ->
              acc2
          end
        end)
      end)

    size = n * 3

    {regions, _visited} =
      Enum.reduce(0..(size - 1), {0, MapSet.new()}, fn r, {reg_cnt, vis_set} ->
        Enum.reduce(0..(size - 1), {reg_cnt, vis_set}, fn c, {rc, vs} ->
          if MapSet.member?(blocked, {r, c}) or MapSet.member?(vs, {r, c}) do
            {rc, vs}
          else
            # start a new region BFS
            {new_vs, _queue} = bfs({r, c}, blocked, size, vs)
            {rc + 1, new_vs}
          end
        end)
      end)

    regions
  end

  defp bfs(start, blocked, size, visited) do
    q = :queue.new() |> :queue.in(start)
    visited = MapSet.put(visited, start)
    bfs_loop(q, blocked, size, visited)
  end

  defp bfs_loop(queue, blocked, size, visited) do
    case :queue.out(queue) do
      {:empty, _} ->
        {visited, queue}

      {{:value, {r, c}}, q2} ->
        dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

        {new_visited, new_queue} =
          Enum.reduce(dirs, {visited, q2}, fn {dr, dc}, {vis_acc, que_acc} ->
            nr = r + dr
            nc = c + dc

            cond do
              nr < 0 or nr >= size or nc < 0 or nc >= size ->
                {vis_acc, que_acc}

              MapSet.member?(blocked, {nr, nc}) ->
                {vis_acc, que_acc}

              MapSet.member?(vis_acc, {nr, nc}) ->
                {vis_acc, que_acc}

              true ->
                vis2 = MapSet.put(vis_acc, {nr, nc})
                que2 = :queue.in({nr, nc}, que_acc)
                {vis2, que2}
            end
          end)

        bfs_loop(new_queue, blocked, size, new_visited)
    end
  end
end
```

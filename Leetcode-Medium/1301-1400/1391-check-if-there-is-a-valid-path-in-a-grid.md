# 1391. Check if There is a Valid Path in a Grid

## Cpp

```cpp
class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if (m == 1 && n == 1) return true;
        
        // direction indices: 0=up,1=down,2=left,3=right
        const int dr[4] = {-1, 1, 0, 0};
        const int dc[4] = {0, 0, -1, 1};
        bool allow[7][4] = {}; // allow[type][dir]
        allow[1][2] = allow[1][3] = true;          // left, right
        allow[2][0] = allow[2][1] = true;          // up, down
        allow[3][1] = allow[3][2] = true;          // down, left
        allow[4][0] = allow[4][3] = true;          // up, right
        allow[5][0] = allow[5][2] = true;          // up, left
        allow[6][1] = allow[6][3] = true;          // down, right
        
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        queue<pair<int,int>> q;
        q.emplace(0,0);
        vis[0][0] = true;
        
        while (!q.empty()) {
            auto [r,c] = q.front(); q.pop();
            int type = grid[r][c];
            for (int d = 0; d < 4; ++d) {
                if (!allow[type][d]) continue;
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (vis[nr][nc]) continue;
                int nt = grid[nr][nc];
                int opp = d ^ 1; // opposite direction
                if (!allow[nt][opp]) continue;
                if (nr == m-1 && nc == n-1) return true;
                vis[nr][nc] = true;
                q.emplace(nr, nc);
            }
        }
        return false;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};

    public boolean hasValidPath(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> q = new ArrayDeque<>();
        visited[0][0] = true;
        q.offer(new int[]{0, 0});
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            if (x == m - 1 && y == n - 1) return true;
            int type = grid[x][y];
            for (int dir = 0; dir < 4; ++dir) {
                if (!connects(type, dir)) continue;
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                int ntype = grid[nx][ny];
                int opp = (dir + 2) % 4;
                if (!connects(ntype, opp)) continue;
                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
        return false;
    }

    private boolean connects(int type, int dir) {
        // dir: 0 up, 1 right, 2 down, 3 left
        switch (type) {
            case 1:
                return dir == 1 || dir == 3; // left-right
            case 2:
                return dir == 0 || dir == 2; // up-down
            case 3:
                return dir == 3 || dir == 2; // left-down
            case 4:
                return dir == 1 || dir == 2; // right-down
            case 5:
                return dir == 3 || dir == 0; // left-up
            case 6:
                return dir == 1 || dir == 0; // right-up
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        from collections import deque

        m, n = len(grid), len(grid[0])

        # connections for each street type
        conn = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }

        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((0, 0))
        visited[0][0] = True

        while q:
            x, y = q.popleft()
            if x == m - 1 and y == n - 1:
                return True
            for dx, dy in conn[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # check opposite direction exists in neighbor
                    if (-dx, -dy) in conn[grid[nx][ny]]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return False
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }
        opposite = {(0, -1): (0, 1), (0, 1): (0, -1), (-1, 0): (1, 0), (1, 0): (-1, 0)}
        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((0, 0))
        visited[0][0] = True

        while q:
            x, y = q.popleft()
            if x == m - 1 and y == n - 1:
                return True
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if opposite[(dx, dy)] in dirs[grid[nx][ny]]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool hasValidPath(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0 || gridColSize[0] == 0) return false;
    int m = gridSize;
    int n = gridColSize[0];

    // direction order: up, right, down, left
    const int dr[4] = {-1, 0, 1, 0};
    const int dc[4] = {0, 1, 0, -1};

    // connectivity for each street type (1..6) and direction
    bool conn[7][4] = {
        {false,false,false,false}, // placeholder for index 0
        {false,true ,false,true }, // 1: left <-> right
        {true ,false,true ,false}, // 2: up   <-> down
        {false,false,true ,true }, // 3: left <-> down
        {false,true ,true ,false}, // 4: right<-> down
        {true ,false,false,true }, // 5: left <-> up
        {true ,true ,false,false}  // 6: right<-> up
    };

    char *visited = (char *)calloc(m * n, sizeof(char));
    int *qr = (int *)malloc(m * n * sizeof(int));
    int *qc = (int *)malloc(m * n * sizeof(int));
    int head = 0, tail = 0;

    visited[0] = 1;
    qr[tail] = 0; qc[tail] = 0; tail++;

    while (head < tail) {
        int r = qr[head];
        int c = qc[head];
        head++;

        if (r == m - 1 && c == n - 1) {
            free(visited);
            free(qr);
            free(qc);
            return true;
        }

        int type = grid[r][c];
        for (int d = 0; d < 4; ++d) {
            if (!conn[type][d]) continue;
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;

            int ntype = grid[nr][nc];
            int opp = (d + 2) % 4; // opposite direction
            if (!conn[ntype][opp]) continue;

            int idx = nr * n + nc;
            if (!visited[idx]) {
                visited[idx] = 1;
                qr[tail] = nr;
                qc[tail] = nc;
                tail++;
            }
        }
    }

    free(visited);
    free(qr);
    free(qc);
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool HasValidPath(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        if (m == 1 && n == 1) return true;

        // directions: up, down, left, right
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        bool[,] conn = new bool[7, 4];
        conn[1, 2] = true; conn[1, 3] = true;               // left, right
        conn[2, 0] = true; conn[2, 1] = true;               // up, down
        conn[3, 1] = true; conn[3, 2] = true;               // down, left
        conn[4, 1] = true; conn[4, 3] = true;               // down, right
        conn[5, 0] = true; conn[5, 2] = true;               // up, left
        conn[6, 0] = true; conn[6, 3] = true;               // up, right

        bool[,] visited = new bool[m, n];
        var q = new System.Collections.Generic.Queue<(int, int)>();
        q.Enqueue((0, 0));
        visited[0, 0] = true;

        while (q.Count > 0) {
            var (r, c) = q.Dequeue();
            if (r == m - 1 && c == n - 1) return true;

            int type = grid[r][c];
            for (int dir = 0; dir < 4; ++dir) {
                if (!conn[type, dir]) continue;
                int nr = r + dr[dir];
                int nc = c + dc[dir];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;

                int neighborType = grid[nr][nc];
                int opp = dir ^ 1; // opposite direction
                if (!conn[neighborType, opp]) continue;

                if (!visited[nr, nc]) {
                    visited[nr, nc] = true;
                    q.Enqueue((nr, nc));
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
 * @param {number[][]} grid
 * @return {boolean}
 */
var hasValidPath = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    if (m === 1 && n === 1) return true;

    // direction vectors: [dx, dy]
    const dirMap = {
        1: [[0, -1], [0, 1]],      // left, right
        2: [[-1, 0], [1, 0]],      // up, down
        3: [[0, -1], [1, 0]],      // left, down
        4: [[0, 1], [-1, 0]],      // right, up
        5: [[0, -1], [-1, 0]],     // left, up
        6: [[0, 1], [1, 0]]        // right, down
    };

    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const queue = [];
    let qh = 0;
    queue.push([0, 0]);
    visited[0][0] = true;

    while (qh < queue.length) {
        const [x, y] = queue[qh++];
        if (x === m - 1 && y === n - 1) return true;

        for (const [dx, dy] of dirMap[grid[x][y]]) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            // check opposite direction exists in neighbor
            const oppDx = -dx, oppDy = -dy;
            const neighDirs = dirMap[grid[nx][ny]];
            let ok = false;
            for (const [ndx, ndy] of neighDirs) {
                if (ndx === oppDx && ndy === oppDy) {
                    ok = true;
                    break;
                }
            }
            if (ok && !visited[nx][ny]) {
                visited[nx][ny] = true;
                queue.push([nx, ny]);
            }
        }
    }

    return false;
};
```

## Typescript

```typescript
function hasValidPath(grid: number[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;

    // direction vectors: up, down, left, right
    const dirs: [number, number][] = [
        [-1, 0], // 0 up
        [1, 0],  // 1 down
        [0, -1], // 2 left
        [0, 1]   // 3 right
    ];

    // mapping pipe type -> allowed direction indices
    const pipeMap: { [key: number]: number[] } = {
        1: [2, 3], // left, right
        2: [0, 1], // up, down
        3: [2, 1], // left, down
        4: [3, 1], // right, down
        5: [2, 0], // left, up
        6: [3, 0]  // right, up
    };

    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const queue: [number, number][] = [[0, 0]];
    visited[0][0] = true;

    while (queue.length) {
        const [r, c] = queue.shift()!;
        if (r === m - 1 && c === n - 1) return true;

        const type = grid[r][c];
        for (const dirIdx of pipeMap[type]) {
            const nr = r + dirs[dirIdx][0];
            const nc = c + dirs[dirIdx][1];

            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (visited[nr][nc]) continue;

            const neighborType = grid[nr][nc];
            // opposite direction index
            const oppDir = dirIdx ^ 1; // flips 0<->1 and 2<->3

            if (pipeMap[neighborType].includes(oppDir)) {
                visited[nr][nc] = true;
                queue.push([nr, nc]);
            }
        }
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function hasValidPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $queue = new SplQueue();
        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $queue->enqueue([0, 0]);
        $visited[0][0] = true;

        // four possible directions: up, down, left, right
        $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];

        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();
            if ($r == $m - 1 && $c == $n - 1) {
                return true;
            }
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) {
                    continue;
                }
                if ($visited[$nr][$nc]) {
                    continue;
                }
                // check if current cell connects to neighbor and neighbor connects back
                if (
                    $this->hasConnection($grid[$r][$c], $d[0], $d[1]) &&
                    $this->hasConnection($grid[$nr][$nc], -$d[0], -$d[1])
                ) {
                    $visited[$nr][$nc] = true;
                    $queue->enqueue([$nr, $nc]);
                }
            }
        }

        return false;
    }

    private function hasConnection($type, $dx, $dy) {
        // returns true if the street type includes direction (dx, dy)
        switch ($type) {
            case 1: // left ↔ right
                return $dx == 0 && ($dy == -1 || $dy == 1);
            case 2: // up ↕ down
                return $dy == 0 && ($dx == -1 || $dx == 1);
            case 3: // left ↓
                return ($dx == 0 && $dy == -1) || ($dx == 1 && $dy == 0);
            case 4: // right ↑
                return ($dx == 0 && $dy == 1) || ($dx == -1 && $dy == 0);
            case 5: // left ↑
                return ($dx == 0 && $dy == -1) || ($dx == -1 && $dy == 0);
            case 6: // right ↓
                return ($dx == 0 && $dy == 1) || ($dx == 1 && $dy == 0);
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func hasValidPath(_ grid: [[Int]]) -> Bool {
        let m = grid.count
        let n = grid[0].count
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        
        // direction vectors: up, down, left, right
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        // connections for each street type (1-indexed)
        var conn = Array(repeating: [Int](), count: 7)
        conn[1] = [2, 3]   // left, right
        conn[2] = [0, 1]   // up, down
        conn[3] = [2, 1]   // left, down
        conn[4] = [3, 0]   // right, up
        conn[5] = [2, 0]   // left, up
        conn[6] = [3, 1]   // right, down
        
        func opposite(_ d: Int) -> Int {
            switch d {
            case 0: return 1   // up -> down
            case 1: return 0   // down -> up
            case 2: return 3   // left -> right
            default: return 2  // right -> left
            }
        }
        
        var queue = [(Int, Int)]()
        var idx = 0
        queue.append((0, 0))
        visited[0][0] = true
        
        while idx < queue.count {
            let (r, c) = queue[idx]
            idx += 1
            
            if r == m - 1 && c == n - 1 { return true }
            
            for dirIdx in conn[grid[r][c]] {
                let dr = dirs[dirIdx].0
                let dc = dirs[dirIdx].1
                let nr = r + dr
                let nc = c + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                
                let opp = opposite(dirIdx)
                if conn[grid[nr][nc]].contains(opp) && !visited[nr][nc] {
                    visited[nr][nc] = true
                    queue.append((nr, nc))
                }
            }
        }
        
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasValidPath(grid: Array<IntArray>): Boolean {
        val m = grid.size
        val n = grid[0].size

        // direction vectors: up, down, left, right
        val dx = intArrayOf(-1, 1, 0, 0)
        val dy = intArrayOf(0, 0, -1, 1)

        // allowed directions for each street type (index 1..6), order: up,down,left,right
        val dirsForType = Array(7) { BooleanArray(4) }
        // type 1: left <-> right
        dirsForType[1][2] = true
        dirsForType[1][3] = true
        // type 2: up <-> down
        dirsForType[2][0] = true
        dirsForType[2][1] = true
        // type 3: left <-> down
        dirsForType[3][2] = true
        dirsForType[3][1] = true
        // type 4: right <-> up
        dirsForType[4][3] = true
        dirsForType[4][0] = true
        // type 5: left <-> up
        dirsForType[5][2] = true
        dirsForType[5][0] = true
        // type 6: right <-> down
        dirsForType[6][3] = true
        dirsForType[6][1] = true

        val visited = Array(m) { BooleanArray(n) }
        val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        fun encode(x: Int, y: Int) = x * n + y

        queue.add(encode(0, 0))
        visited[0][0] = true

        while (queue.isNotEmpty()) {
            val cur = queue.poll()
            val x = cur / n
            val y = cur % n
            if (x == m - 1 && y == n - 1) return true

            val type = grid[x][y]
            for (dir in 0..3) {
                if (!dirsForType[type][dir]) continue
                val nx = x + dx[dir]
                val ny = y + dy[dir]
                if (nx !in 0 until m || ny !in 0 until n) continue
                if (visited[nx][ny]) continue

                // opposite direction index
                val opp = when (dir) {
                    0 -> 1   // up -> down
                    1 -> 0   // down -> up
                    2 -> 3   // left -> right
                    else -> 2 // right -> left
                }

                val nextType = grid[nx][ny]
                if (!dirsForType[nextType][opp]) continue

                visited[nx][ny] = true
                queue.add(encode(nx, ny))
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool hasValidPath(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // Directions: up, right, down, left
    const List<List<int>> dirs = [
      [-1, 0],
      [0, 1],
      [1, 0],
      [0, -1]
    ];

    // Mapping street type to allowed direction indices
    const Map<int, List<int>> typeDirs = {
      1: [1, 3], // left ↔ right
      2: [0, 2], // up ↔ down
      3: [2, 3], // left ↔ down
      4: [0, 1], // up ↔ right
      5: [0, 3], // up ↔ left
      6: [1, 2]  // right ↔ down
    };

    List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));

    List<List<int>> queue = [[0, 0]];
    int head = 0;
    visited[0][0] = true;

    while (head < queue.length) {
      var cur = queue[head++];
      int r = cur[0], c = cur[1];
      if (r == m - 1 && c == n - 1) return true;

      int curType = grid[r][c];
      for (int d in typeDirs[curType]!) {
        int nr = r + dirs[d][0];
        int nc = c + dirs[d][1];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
        if (visited[nr][nc]) continue;

        int nextType = grid[nr][nc];
        int opposite = (d + 2) % 4;
        if (typeDirs[nextType]!.contains(opposite)) {
          visited[nr][nc] = true;
          queue.add([nr, nc]);
        }
      }
    }

    return false;
  }
}
```

## Golang

```go
func hasValidPath(grid [][]int) bool {
	m := len(grid)
	n := len(grid[0])
	dirs := map[int][][]int{
		1: {{0, -1}, {0, 1}},   // left, right
		2: {{-1, 0}, {1, 0}},   // up, down
		3: {{0, -1}, {1, 0}},   // left, down
		4: {{0, 1}, {-1, 0}},   // right, up
		5: {{0, -1}, {-1, 0}},  // left, up
		6: {{0, 1}, {1, 0}},    // right, down
	}
	type point struct{ x, y int }
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	queue := []point{{0, 0}}
	visited[0][0] = true

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.x == m-1 && cur.y == n-1 {
			return true
		}
		for _, d := range dirs[grid[cur.x][cur.y]] {
			nx, ny := cur.x+d[0], cur.y+d[1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			ok := false
			for _, nd := range dirs[grid[nx][ny]] {
				if nd[0] == -d[0] && nd[1] == -d[1] {
					ok = true
					break
				}
			}
			if ok && !visited[nx][ny] {
				visited[nx][ny] = true
				queue = append(queue, point{nx, ny})
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def has_valid_path(grid)
  m = grid.length
  n = grid[0].length
  dirs = {
    1 => [[0, -1], [0, 1]],
    2 => [[-1, 0], [1, 0]],
    3 => [[0, -1], [1, 0]],
    4 => [[0, 1], [1, 0]],
    5 => [[0, -1], [-1, 0]],
    6 => [[0, 1], [-1, 0]]
  }
  visited = Array.new(m) { Array.new(n, false) }
  queue = [[0, 0]]
  visited[0][0] = true
  until queue.empty?
    i, j = queue.shift
    return true if i == m - 1 && j == n - 1
    dirs[grid[i][j]].each do |dx, dy|
      ni = i + dx
      nj = j + dy
      next unless ni.between?(0, m - 1) && nj.between?(0, n - 1)
      if dirs[grid[ni][nj]].any? { |odx, ody| odx == -dx && ody == -dy }
        unless visited[ni][nj]
          visited[ni][nj] = true
          queue << [ni, nj]
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
    def hasValidPath(grid: Array[Array[Int]]): Boolean = {
        val m = grid.length
        val n = grid(0).length

        val dirs = Map(
            1 -> List((0, -1), (0, 1)),          // left, right
            2 -> List((-1, 0), (1, 0)),          // up, down
            3 -> List((0, -1), (1, 0)),          // left, down
            4 -> List((0, 1), (-1, 0)),          // right, up
            5 -> List((0, -1), (-1, 0)),         // left, up
            6 -> List((0, 1), (1, 0))            // right, down
        )

        val opposite = Map(
            (0, -1) -> (0, 1),
            (0, 1)  -> (0, -1),
            (-1, 0) -> (1, 0),
            (1, 0)  -> (-1, 0)
        )

        val visited = Array.ofDim[Boolean](m, n)
        val queue = new java.util.ArrayDeque[(Int, Int)]()
        queue.offer((0, 0))
        visited(0)(0) = true

        while (!queue.isEmpty) {
            val (x, y) = queue.poll()
            if (x == m - 1 && y == n - 1) return true
            for ((dx, dy) <- dirs(grid(x)(y))) {
                val nx = x + dx
                val ny = y + dy
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited(nx)(ny)) {
                    val need = opposite((dx, dy))
                    if (dirs(grid(nx)(ny)).contains(need)) {
                        visited(nx)(ny) = true
                        queue.offer((nx, ny))
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
    pub fn has_valid_path(grid: Vec<Vec<i32>>) -> bool {
        use std::collections::VecDeque;
        let m = grid.len();
        let n = grid[0].len();

        // direction vectors: up, down, left, right
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        // connections for each street type (1-indexed)
        let mut conn: Vec<Vec<usize>> = vec![vec![]; 7];
        conn[1] = vec![2, 3]; // left, right
        conn[2] = vec![0, 1]; // up, down
        conn[3] = vec![2, 1]; // left, down
        conn[4] = vec![3, 0]; // right, up
        conn[5] = vec![2, 0]; // left, up
        conn[6] = vec![3, 1]; // right, down

        let mut visited = vec![vec![false; n]; m];
        let mut q = VecDeque::new();
        visited[0][0] = true;
        q.push_back((0usize, 0usize));

        while let Some((r, c)) = q.pop_front() {
            if r == m - 1 && c == n - 1 {
                return true;
            }
            let typ = grid[r][c] as usize;
            for &d in &conn[typ] {
                let nr_i32 = r as i32 + dirs[d].0;
                let nc_i32 = c as i32 + dirs[d].1;
                if nr_i32 < 0 || nr_i32 >= m as i32 || nc_i32 < 0 || nc_i32 >= n as i32 {
                    continue;
                }
                let nr = nr_i32 as usize;
                let nc = nc_i32 as usize;
                if visited[nr][nc] {
                    continue;
                }
                // opposite direction
                let opp = match d {
                    0 => 1,
                    1 => 0,
                    2 => 3,
                    _ => 2,
                };
                let ntyp = grid[nr][nc] as usize;
                if conn[ntyp].contains(&opp) {
                    visited[nr][nc] = true;
                    q.push_back((nr, nc));
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (has-valid-path grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (first grid))))
         (dir-mapping
          (hash 1 '((0 . -1) (0 . 1))
                2 '((-1 . 0) (1 . 0))
                3 '((0 . -1) (1 . 0))
                4 '((0 . 1) (-1 . 0))
                5 '((0 . -1) (-1 . 0))
                6 '((0 . 1) (1 . 0)))))
    (define (in-bounds r c)
      (and (>= r 0) (< r m) (>= c 0) (< c n)))
    (define (type-at r c)
      (list-ref (list-ref grid r) c))
    (define (allowed type)
      (hash-ref dir-mapping type))
    (define (opposite dx dy)
      (cond [(and (= dx -1) (= dy 0)) (values 1 0)]
            [(and (= dx 1) (= dy 0)) (values -1 0)]
            [(and (= dx 0) (= dy -1)) (values 0 1)]
            [(and (= dx 0) (= dy 1)) (values 0 -1)]))
    (define visited (make-hash))
    (define (mark r c)
      (hash-set! visited (cons r c) #t))
    (define (seen? r c)
      (hash-has-key? visited (cons r c)))
    (define queue (list (cons 0 0)))
    (mark 0 0)
    (let loop ((q queue))
      (cond
        [(null? q) #f]
        [else
         (define pos (car q))
         (define r (car pos))
         (define c (cdr pos))
         (if (and (= r (- m 1)) (= c (- n 1)))
             #t
             (let* ((type (type-at r c))
                    (dirs (allowed type)))
               (define new-pos
                 (for/list ([d dirs])
                   (define dx (car d))
                   (define dy (cdr d))
                   (define nr (+ r dx))
                   (define nc (+ c dy))
                   (if (and (in-bounds nr nc) (not (seen? nr nc)))
                       (let ((neighbor-type (type-at nr nc)))
                         (define-values (odx ody) (opposite dx dy))
                         (when (member (cons odx ody) (allowed neighbor-type))
                           (begin
                             (mark nr nc)
                             (cons nr nc))))
                       #f)))
               (define filtered (filter identity new-pos))
               (loop (append (cdr q) filtered)))]))))))
```

## Erlang

```erlang
-spec has_valid_path(Grid :: [[integer()]]) -> boolean().
has_valid_path(Grid) ->
    GridT = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    M = tuple_size(GridT),
    N = case M of
            0 -> 0;
            _ -> tuple_size(element(1, GridT))
        end,
    bfs(GridT, M, N, [{0,0}], #{ {0,0} => true }).

bfs(_, M, N, [], _) ->
    false;
bfs(GridT, M, N, [{R,C}|Rest], Visited) ->
    if R =:= M-1 andalso C =:= N-1 ->
            true;
       true ->
            Type = get_cell(GridT, R, C),
            Directions = dirs(Type),
            {NewQueue, NewVisited} =
                lists:foldl(fun(Dir, {Q, V}) ->
                    {DR, DC} = Dir,
                    NR = R + DR,
                    NC = C + DC,
                    if NR < 0 orelse NR >= M orelse NC < 0 orelse NC >= N ->
                            {Q, V};
                       true ->
                            case maps:is_key({NR, NC}, V) of
                                true -> {Q, V};
                                false ->
                                    NeighborType = get_cell(GridT, NR, NC),
                                    Opposite = opposite(Dir),
                                    if lists:member(Opposite, dirs(NeighborType)) ->
                                            {[{NR, NC} | Q], maps:put({NR, NC}, true, V)};
                                       true -> {Q, V}
                                    end
                            end
                    end
                end, {Rest, Visited}, Directions),
            bfs(GridT, M, N, NewQueue, NewVisited)
    end.

get_cell(GridT, R, C) ->
    RowTuple = element(R + 1, GridT),
    element(C + 1, RowTuple).

dirs(1) -> [{0,-1},{0,1}];
dirs(2) -> [{-1,0},{1,0}];
dirs(3) -> [{0,-1},{1,0}];
dirs(4) -> [{0,1},{1,0}];
dirs(5) -> [{0,-1},{-1,0}];
dirs(6) -> [{0,1},{-1,0}].

opposite({-1,0}) -> {1,0};
opposite({1,0})  -> {-1,0};
opposite({0,-1}) -> {0,1};
opposite({0,1})  -> {0,-1}.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_valid_path(grid :: [[integer]]) :: boolean
  def has_valid_path(grid) do
    m = length(grid)
    n = length(hd(grid))
    target = {m - 1, n - 1}

    dirs = %{
      1 => [:left, :right],
      2 => [:up, :down],
      3 => [:left, :down],
      4 => [:right, :down],
      5 => [:left, :up],
      6 => [:right, :up]
    }

    vec = %{
      up: {-1, 0},
      down: {1, 0},
      left: {0, -1},
      right: {0, 1}
    }

    opposite = %{up: :down, down: :up, left: :right, right: :left}

    start = {0, 0}
    visited = MapSet.new([start])
    dfs(grid, dirs, vec, opposite, target, visited, [start])
  end

  defp dfs(_grid, _dirs, _vec, _opposite, target, _visited, []) do
    false
  end

  defp dfs(grid, dirs, vec, opposite, target, visited, [{r, c} | stack]) do
    if {r, c} == target do
      true
    else
      type = cell(grid, r, c)
      allowed_dirs = Map.get(dirs, type)

      {new_visited, new_stack} =
        Enum.reduce(allowed_dirs, {visited, stack}, fn dir, {vis, stk} ->
          {dr, dc} = vec[dir]
          nr = r + dr
          nc = c + dc

          if nr < 0 or nr >= length(grid) or nc < 0 or nc >= length(hd(grid)) do
            {vis, stk}
          else
            ntype = cell(grid, nr, nc)
            opp_dir = opposite[dir]

            if opp_dir in Map.get(dirs, ntype) and not MapSet.member?(vis, {nr, nc}) do
              {MapSet.put(vis, {nr, nc}), [{nr, nc} | stk]}
            else
              {vis, stk}
            end
          end
        end)

      dfs(grid, dirs, vec, opposite, target, new_visited, new_stack)
    end
  end

  defp cell(grid, r, c) do
    grid |> Enum.at(r) |> Enum.at(c)
  end
end
```

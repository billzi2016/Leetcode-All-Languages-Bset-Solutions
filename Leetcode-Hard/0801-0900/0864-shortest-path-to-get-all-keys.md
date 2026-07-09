# 0864. Shortest Path to Get All Keys

## Cpp

```cpp
class Solution {
public:
    int shortestPathAllKeys(vector<string>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int totalKeys = 0;
        int startX = -1, startY = -1;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                char c = grid[i][j];
                if (c == '@') {
                    startX = i;
                    startY = j;
                } else if (c >= 'a' && c <= 'f') {
                    totalKeys = max(totalKeys, c - 'a' + 1);
                }
            }
        }
        int targetMask = (1 << totalKeys) - 1;
        vector<vector<vector<char>>> visited(m,
            vector<vector<char>>(n, vector<char>(1 << totalKeys, 0)));
        struct Node {int x, y, mask, dist;};
        queue<Node> q;
        q.push({startX, startY, 0, 0});
        visited[startX][startY][0] = 1;
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        while (!q.empty()) {
            Node cur = q.front(); q.pop();
            if (cur.mask == targetMask) return cur.dist;
            for (auto &d : dirs) {
                int nx = cur.x + d[0];
                int ny = cur.y + d[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                char cell = grid[nx][ny];
                if (cell == '#') continue;
                int newMask = cur.mask;
                if (cell >= 'a' && cell <= 'f') {
                    newMask |= 1 << (cell - 'a');
                }
                if (cell >= 'A' && cell <= 'F') {
                    if (!(newMask & (1 << (cell - 'A')))) continue; // lock without key
                }
                if (!visited[nx][ny][newMask]) {
                    visited[nx][ny][newMask] = 1;
                    q.push({nx, ny, newMask, cur.dist + 1});
                }
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int shortestPathAllKeys(String[] grid) {
        int m = grid.length;
        int n = grid[0].length();
        char[][] g = new char[m][];
        for (int i = 0; i < m; i++) {
            g[i] = grid[i].toCharArray();
        }

        int startX = -1, startY = -1;
        int targetMask = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = g[i][j];
                if (c == '@') {
                    startX = i;
                    startY = j;
                } else if (c >= 'a' && c <= 'f') {
                    targetMask |= 1 << (c - 'a');
                }
            }
        }

        boolean[][][] visited = new boolean[m][n][1 << 6];
        java.util.ArrayDeque<int[]> dq = new java.util.ArrayDeque<>();
        dq.offer(new int[]{startX, startY, 0, 0});
        visited[startX][startY][0] = true;

        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!dq.isEmpty()) {
            int[] cur = dq.poll();
            int x = cur[0], y = cur[1], mask = cur[2], steps = cur[3];
            if (mask == targetMask) return steps;
            for (int[] d : dirs) {
                int nx = x + d[0];
                int ny = y + d[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                char c = g[nx][ny];
                if (c == '#') continue;

                int newMask = mask;
                if (c >= 'a' && c <= 'f') {
                    newMask |= 1 << (c - 'a');
                }
                if (c >= 'A' && c <= 'F') {
                    if ((mask & (1 << (c - 'A'))) == 0) continue;
                }

                if (!visited[nx][ny][newMask]) {
                    visited[nx][ny][newMask] = true;
                    dq.offer(new int[]{nx, ny, newMask, steps + 1});
                }
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        start_x = start_y = -1
        total_keys = 0

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    start_x, start_y = i, j
                elif 'a' <= c <= 'f':
                    total_keys |= (1 << (ord(c) - ord('a')))

        target_mask = total_keys  # bits of all keys present

        # visited[x][y][mask] -> bool
        visited = [[[False] * (1 << 6) for _ in range(n)] for _ in range(m)]
        q = deque()
        start_mask = 0
        visited[start_x][start_y][start_mask] = True
        q.append((start_x, start_y, start_mask, 0))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y, mask, steps = q.popleft()
            if mask == target_mask:
                return steps
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                cell = grid[nx][ny]
                if cell == '#':
                    continue

                new_mask = mask
                # key
                if 'a' <= cell <= 'f':
                    new_mask |= (1 << (ord(cell) - ord('a')))
                # lock
                if 'A' <= cell <= 'F':
                    if not (mask & (1 << (ord(cell) - ord('A')))):
                        continue  # don't have key

                if not visited[nx][ny][new_mask]:
                    visited[nx][ny][new_mask] = True
                    q.append((nx, ny, new_mask, steps + 1))

        return -1
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start_x = start_y = -1
        total_keys = 0
        
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    start_x, start_y = i, j
                elif 'a' <= c <= 'f':
                    total_keys |= 1 << (ord(c) - ord('a'))
        # target mask with all bits of existing keys set
        target_mask = total_keys
        
        # BFS
        q = deque()
        q.append((start_x, start_y, 0, 0))  # x, y, mask, steps
        visited = [[[False] * (1 << 6) for _ in range(n)] for _ in range(m)]
        visited[start_x][start_y][0] = True
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            x, y, mask, steps = q.popleft()
            if mask == target_mask:
                return steps
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                cell = grid[nx][ny]
                if cell == '#':
                    continue
                new_mask = mask
                # key
                if 'a' <= cell <= 'f':
                    new_mask |= 1 << (ord(cell) - ord('a'))
                # lock
                if 'A' <= cell <= 'F':
                    if not (mask & (1 << (ord(cell) - ord('A')))):
                        continue
                if not visited[nx][ny][new_mask]:
                    visited[nx][ny][new_mask] = True
                    q.append((nx, ny, new_mask, steps + 1))
        return -1
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    int x;
    int y;
    int mask;
    int dist;
} Node;

int shortestPathAllKeys(char** grid, int gridSize) {
    if (gridSize == 0) return -1;
    int m = gridSize;
    int n = strlen(grid[0]);
    int startX = -1, startY = -1;
    int targetMask = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            char c = grid[i][j];
            if (c == '@') {
                startX = i;
                startY = j;
            } else if (c >= 'a' && c <= 'f') {
                targetMask |= 1 << (c - 'a');
            }
        }
    }

    const int MAXMASK = 1 << 6; // up to 6 keys
    static bool visited[30][30][64];
    memset(visited, 0, sizeof(visited));

    int maxStates = m * n * MAXMASK;
    Node* q = (Node*)malloc(sizeof(Node) * maxStates);
    int qs = 0, qe = 0;

    visited[startX][startY][0] = true;
    q[qe++] = (Node){startX, startY, 0, 0};

    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    while (qs < qe) {
        Node cur = q[qs++];
        if (cur.mask == targetMask) {
            free(q);
            return cur.dist;
        }
        for (int d = 0; d < 4; ++d) {
            int nx = cur.x + dirs[d][0];
            int ny = cur.y + dirs[d][1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            char cell = grid[nx][ny];
            if (cell == '#') continue;

            int newMask = cur.mask;
            if (cell >= 'a' && cell <= 'f') {
                newMask |= 1 << (cell - 'a');
            }
            if (cell >= 'A' && cell <= 'F') {
                if (!(cur.mask & (1 << (cell - 'A')))) continue; // lock without key
            }

            if (!visited[nx][ny][newMask]) {
                visited[nx][ny][newMask] = true;
                q[qe++] = (Node){nx, ny, newMask, cur.dist + 1};
            }
        }
    }

    free(q);
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int ShortestPathAllKeys(string[] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int startX = 0, startY = 0;
        int totalKeys = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = grid[i][j];
                if (c == '@') {
                    startX = i;
                    startY = j;
                } else if (c >= 'a' && c <= 'f') {
                    totalKeys = Math.Max(totalKeys, c - 'a' + 1);
                }
            }
        }

        int allMask = (1 << totalKeys) - 1;
        bool[,,] visited = new bool[m, n, 1 << 6]; // max 64 states
        var queue = new Queue<(int x, int y, int mask, int steps)>();
        queue.Enqueue((startX, startY, 0, 0));
        visited[startX, startY, 0] = true;

        int[] dirs = new int[] { -1, 0, 1, 0, -1 };

        while (queue.Count > 0) {
            var cur = queue.Dequeue();
            int x = cur.x, y = cur.y, mask = cur.mask, steps = cur.steps;

            if (mask == allMask) return steps;

            for (int d = 0; d < 4; d++) {
                int nx = x + dirs[d];
                int ny = y + dirs[d + 1];

                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                char c = grid[nx][ny];
                if (c == '#') continue;

                int newMask = mask;

                // lock
                if (c >= 'A' && c <= 'F') {
                    int needKeyBit = 1 << (c - 'A');
                    if ((mask & needKeyBit) == 0) continue; // key not owned
                }

                // key
                if (c >= 'a' && c <= 'f') {
                    newMask |= 1 << (c - 'a');
                }

                if (!visited[nx, ny, newMask]) {
                    visited[nx, ny, newMask] = true;
                    queue.Enqueue((nx, ny, newMask, steps + 1));
                }
            }
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} grid
 * @return {number}
 */
var shortestPathAllKeys = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let startX = 0, startY = 0;
    let allKeysMask = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const ch = grid[i][j];
            if (ch === '@') {
                startX = i;
                startY = j;
            } else if (ch >= 'a' && ch <= 'f') {
                allKeysMask |= 1 << (ch.charCodeAt(0) - 97);
            }
        }
    }

    const maxMask = 1 << 6; // 64, since at most 6 keys
    const visited = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => new Uint8Array(maxMask))
    );

    const qx = [];
    const qy = [];
    const qmask = [];
    let head = 0;

    qx.push(startX);
    qy.push(startY);
    qmask.push(0);
    visited[startX][startY][0] = 1;

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let steps = 0;

    while (head < qx.length) {
        const levelSize = qx.length - head;
        for (let s = 0; s < levelSize; s++) {
            const x = qx[head];
            const y = qy[head];
            const mask = qmask[head];
            head++;

            if (mask === allKeysMask) return steps;

            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;

                const cell = grid[nx][ny];
                if (cell === '#') continue;

                let newMask = mask;

                // key
                if (cell >= 'a' && cell <= 'f') {
                    newMask |= 1 << (cell.charCodeAt(0) - 97);
                }

                // lock
                if (cell >= 'A' && cell <= 'F') {
                    const need = 1 << (cell.charCodeAt(0) - 65);
                    if ((mask & need) === 0) continue;
                }

                if (!visited[nx][ny][newMask]) {
                    visited[nx][ny][newMask] = 1;
                    qx.push(nx);
                    qy.push(ny);
                    qmask.push(newMask);
                }
            }
        }
        steps++;
    }

    return -1;
};
```

## Typescript

```typescript
function shortestPathAllKeys(grid: string[]): number {
    const m = grid.length;
    const n = grid[0].length;
    let startX = 0, startY = 0;
    let totalKeys = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const ch = grid[i][j];
            if (ch === '@') {
                startX = i;
                startY = j;
            } else if (ch >= 'a' && ch <= 'f') {
                totalKeys++;
            }
        }
    }

    const allMask = (1 << totalKeys) - 1;
    // visited[x][y][mask] -> boolean
    const visited: Uint8Array[][] = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => new Uint8Array(1 << totalKeys))
    );

    const qx: number[] = [];
    const qy: number[] = [];
    const qmask: number[] = [];
    const qsteps: number[] = [];

    qx.push(startX);
    qy.push(startY);
    qmask.push(0);
    qsteps.push(0);
    visited[startX][startY][0] = 1;

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ];

    let head = 0;
    while (head < qx.length) {
        const x = qx[head];
        const y = qy[head];
        const mask = qmask[head];
        const steps = qsteps[head];
        head++;

        if (mask === allMask) return steps;

        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            const cell = grid[nx][ny];
            if (cell === '#') continue;

            let newMask = mask;

            // key
            if (cell >= 'a' && cell <= 'f') {
                const bit = 1 << (cell.charCodeAt(0) - 97);
                newMask |= bit;
            }

            // lock
            if (cell >= 'A' && cell <= 'F') {
                const bit = 1 << (cell.charCodeAt(0) - 65);
                if ((newMask & bit) === 0) continue; // cannot pass lock
            }

            if (!visited[nx][ny][newMask]) {
                visited[nx][ny][newMask] = 1;
                qx.push(nx);
                qy.push(ny);
                qmask.push(newMask);
                qsteps.push(steps + 1);
            }
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $grid
     * @return Integer
     */
    function shortestPathAllKeys($grid) {
        $m = count($grid);
        $n = strlen($grid[0]);
        $startX = $startY = -1;
        $keyCount = 0;

        // Find start position and total number of keys
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $c = $grid[$i][$j];
                if ($c === '@') {
                    $startX = $i;
                    $startY = $j;
                } elseif ($c >= 'a' && $c <= 'f') {
                    $keyCount = max($keyCount, ord($c) - ord('a') + 1);
                }
            }
        }

        $targetMask = (1 << $keyCount) - 1;

        $queue = new SplQueue();
        $queue->enqueue([$startX, $startY, 0, 0]); // x, y, mask, steps
        $visited = array_fill(0, $m, array_fill(0, $n, []));
        $visited[$startX][$startY][0] = true;

        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];

        while (!$queue->isEmpty()) {
            [$x, $y, $mask, $steps] = $queue->dequeue();

            if ($mask === $targetMask) {
                return $steps;
            }

            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];

                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;

                $cell = $grid[$nx][$ny];
                if ($cell === '#') continue;

                $newMask = $mask;

                // key
                if ($cell >= 'a' && $cell <= 'f') {
                    $bit = ord($cell) - ord('a');
                    $newMask |= (1 << $bit);
                }

                // lock
                if ($cell >= 'A' && $cell <= 'F') {
                    $bit = ord($cell) - ord('A');
                    if ((($mask >> $bit) & 1) === 0) continue; // key not owned
                }

                if (!isset($visited[$nx][$ny][$newMask])) {
                    $visited[$nx][$ny][$newMask] = true;
                    $queue->enqueue([$nx, $ny, $newMask, $steps + 1]);
                }
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func shortestPathAllKeys(_ grid: [String]) -> Int {
        let rows = grid.count
        guard rows > 0 else { return -1 }
        let cols = grid[0].count
        
        var board = [[Character]]()
        var startX = 0, startY = 0
        var allKeysMask = 0
        
        for i in 0..<rows {
            let rowChars = Array(grid[i])
            board.append(rowChars)
            for j in 0..<cols {
                let ch = rowChars[j]
                if ch == "@" {
                    startX = i
                    startY = j
                } else if isLower(ch) {
                    let bit = Int(ch.unicodeScalars.first!.value - UnicodeScalar("a").value)
                    allKeysMask |= (1 << bit)
                }
            }
        }
        
        let maxMask = 1 << 6   // keys <= 6
        var visited = Array(repeating: Array(repeating: Array(repeating: false, count: maxMask), count: cols), count: rows)
        var queue: [(x: Int, y: Int, mask: Int, steps: Int)] = []
        var head = 0
        
        queue.append((startX, startY, 0, 0))
        visited[startX][startY][0] = true
        let dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while head < queue.count {
            let cur = queue[head]
            head += 1
            
            if cur.mask == allKeysMask { return cur.steps }
            
            for d in dirs {
                let nx = cur.x + d.0
                let ny = cur.y + d.1
                if nx < 0 || nx >= rows || ny < 0 || ny >= cols { continue }
                
                let cell = board[nx][ny]
                if cell == "#" { continue }
                
                var newMask = cur.mask
                
                if isLower(cell) {
                    let bit = Int(cell.unicodeScalars.first!.value - UnicodeScalar("a").value)
                    newMask |= (1 << bit)
                }
                
                if isUpper(cell) {
                    let bit = Int(cell.unicodeScalars.first!.value - UnicodeScalar("A").value)
                    if (newMask & (1 << bit)) == 0 { continue } // lock without key
                }
                
                if !visited[nx][ny][newMask] {
                    visited[nx][ny][newMask] = true
                    queue.append((nx, ny, newMask, cur.steps + 1))
                }
            }
        }
        
        return -1
    }
    
    private func isLower(_ c: Character) -> Bool {
        guard let v = c.unicodeScalars.first?.value else { return false }
        return v >= UnicodeScalar("a").value && v <= UnicodeScalar("f").value
    }
    
    private func isUpper(_ c: Character) -> Bool {
        guard let v = c.unicodeScalars.first?.value else { return false }
        return v >= UnicodeScalar("A").value && v <= UnicodeScalar("F").value
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestPathAllKeys(grid: Array<String>): Int {
        val m = grid.size
        val n = grid[0].length
        var startX = 0
        var startY = 0
        val keySet = mutableSetOf<Char>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                when (val c = grid[i][j]) {
                    '@' -> { startX = i; startY = j }
                    in 'a'..'f' -> keySet.add(c)
                }
            }
        }
        var targetMask = 0
        for (c in keySet) {
            targetMask = targetMask or (1 shl (c - 'a'))
        }
        val maxMask = 1 shl 6 // up to 6 keys
        val visited = Array(m) { Array(n) { BooleanArray(maxMask) } }

        data class State(val x: Int, val y: Int, val mask: Int, val steps: Int)

        val queue: ArrayDeque<State> = ArrayDeque()
        queue.add(State(startX, startY, 0, 0))
        visited[startX][startY][0] = true

        val dirs = intArrayOf(-1, 0, 1, 0, -1)
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            if (cur.mask == targetMask) return cur.steps
            for (d in 0 until 4) {
                val nx = cur.x + dirs[d]
                val ny = cur.y + dirs[d + 1]
                if (nx !in 0 until m || ny !in 0 until n) continue
                var cell = grid[nx][ny]
                if (cell == '#') continue
                var newMask = cur.mask
                if (cell in 'a'..'f') {
                    newMask = newMask or (1 shl (cell - 'a'))
                }
                if (cell in 'A'..'F') {
                    val need = 1 shl (cell - 'A')
                    if ((newMask and need) == 0) continue
                }
                if (!visited[nx][ny][newMask]) {
                    visited[nx][ny][newMask] = true
                    queue.add(State(nx, ny, newMask, cur.steps + 1))
                }
            }
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int shortestPathAllKeys(List<String> grid) {
    int m = grid.length;
    int n = grid[0].length;

    int startX = -1, startY = -1;
    int totalKeys = 0;

    // Find start position and count keys
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        String ch = grid[i][j];
        if (ch == '@') {
          startX = i;
          startY = j;
        } else if (_isKey(ch)) {
          totalKeys++;
        }
      }
    }

    int allMask = (1 << totalKeys) - 1;

    // visited[x][y][mask]
    List<List<List<bool>>> visited = List.generate(
        m,
        (_) => List.generate(
            n, (_) => List.filled(1 << totalKeys, false)));

    Queue<List<int>> q = Queue();
    q.add([startX, startY, 0]);
    visited[startX][startY][0] = true;

    const List<int> dx = [1, -1, 0, 0];
    const List<int> dy = [0, 0, 1, -1];

    int steps = 0;
    while (q.isNotEmpty) {
      int size = q.length;
      for (int i = 0; i < size; i++) {
        var cur = q.removeFirst();
        int x = cur[0];
        int y = cur[1];
        int mask = cur[2];

        if (mask == allMask) return steps;

        for (int dir = 0; dir < 4; dir++) {
          int nx = x + dx[dir];
          int ny = y + dy[dir];
          if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
          String cell = grid[nx][ny];
          if (cell == '#') continue;

          int newMask = mask;

          if (_isKey(cell)) {
            int bit = cell.codeUnitAt(0) - 'a'.codeUnitAt(0);
            newMask |= (1 << bit);
          }

          if (_isLock(cell)) {
            int bit = cell.codeUnitAt(0) - 'A'.codeUnitAt(0);
            if ((mask & (1 << bit)) == 0) continue; // don't have key
          }

          if (!visited[nx][ny][newMask]) {
            visited[nx][ny][newMask] = true;
            q.add([nx, ny, newMask]);
          }
        }
      }
      steps++;
    }
    return -1;
  }

  bool _isKey(String ch) {
    int code = ch.codeUnitAt(0);
    return code >= 'a'.codeUnitAt(0) && code <= 'f'.codeUnitAt(0);
  }

  bool _isLock(String ch) {
    int code = ch.codeUnitAt(0);
    return code >= 'A'.codeUnitAt(0) && code <= 'F'.codeUnitAt(0);
  }
}
```

## Golang

```go
func shortestPathAllKeys(grid []string) int {
    m := len(grid)
    n := len(grid[0])

    var sx, sy int
    allMask := 0

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            c := grid[i][j]
            if c == '@' {
                sx, sy = i, j
            } else if c >= 'a' && c <= 'f' {
                allMask |= 1 << (c - 'a')
            }
        }
    }

    const maxKeys = 6
    maskSize := 1 << maxKeys
    visited := make([][][]bool, m)
    for i := 0; i < m; i++ {
        visited[i] = make([][]bool, n)
        for j := 0; j < n; j++ {
            visited[i][j] = make([]bool, maskSize)
        }
    }

    type node struct{ x, y, mask, dist int }
    q := []node{{sx, sy, 0, 0}}
    visited[sx][sy][0] = true

    dirs := []int{-1, 0, 1, 0, -1}
    for head := 0; head < len(q); head++ {
        cur := q[head]
        if cur.mask == allMask {
            return cur.dist
        }
        for d := 0; d < 4; d++ {
            nx := cur.x + dirs[d]
            ny := cur.y + dirs[d+1]
            if nx < 0 || nx >= m || ny < 0 || ny >= n {
                continue
            }
            cell := grid[nx][ny]
            if cell == '#' {
                continue
            }

            newMask := cur.mask

            // key
            if cell >= 'a' && cell <= 'f' {
                newMask |= 1 << (cell - 'a')
            }

            // lock
            if cell >= 'A' && cell <= 'F' {
                if (cur.mask & (1 << (cell - 'A'))) == 0 {
                    continue
                }
            }

            if !visited[nx][ny][newMask] {
                visited[nx][ny][newMask] = true
                q = append(q, node{nx, ny, newMask, cur.dist + 1})
            }
        }
    }

    return -1
}
```

## Ruby

```ruby
def shortest_path_all_keys(grid)
  m = grid.size
  n = grid[0].size
  start_x = start_y = nil
  total_keys = 0

  (0...m).each do |i|
    row = grid[i]
    (0...n).each do |j|
      ch = row.getbyte(j)
      if ch == '@'.ord
        start_x, start_y = i, j
      elsif ch >= 'a'.ord && ch <= 'f'.ord
        total_keys += 1
      end
    end
  end

  all_mask = (1 << total_keys) - 1
  queue = []
  head = 0
  visited = {}
  visited[[start_x, start_y, 0]] = true
  queue << [start_x, start_y, 0, 0]

  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  while head < queue.length
    x, y, mask, steps = queue[head]
    head += 1

    return steps if mask == all_mask

    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      next if nx < 0 || nx >= m || ny < 0 || ny >= n

      cell = grid[nx].getbyte(ny)
      next if cell == '#'.ord

      new_mask = mask

      if cell >= 'a'.ord && cell <= 'f'.ord
        bit = 1 << (cell - 'a'.ord)
        new_mask |= bit
      elsif cell >= 'A'.ord && cell <= 'F'.ord
        bit = 1 << (cell - 'A'.ord)
        next if (mask & bit).zero?
      end

      state = [nx, ny, new_mask]
      unless visited[state]
        visited[state] = true
        queue << [nx, ny, new_mask, steps + 1]
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def shortestPathAllKeys(grid: Array[String]): Int = {
        val m = grid.length
        val n = grid(0).length
        var startX = 0
        var startY = 0
        val keySet = scala.collection.mutable.Set[Char]()
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                val ch = grid(i)(j)
                if (ch == '@') {
                    startX = i
                    startY = j
                } else if (ch >= 'a' && ch <= 'f') {
                    keySet += ch
                }
            }
        }
        val totalKeys = keySet.size
        val allMask = (1 << totalKeys) - 1
        val maxMask = 1 << totalKeys
        val visited = Array.ofDim[Boolean](m, n, maxMask)

        import scala.collection.mutable.ArrayDeque
        val queue = ArrayDeque[(Int, Int, Int, Int)]()
        queue.append((startX, startY, 0, 0))
        visited(startX)(startY)(0) = true

        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

        while (queue.nonEmpty) {
            val (x, y, mask, dist) = queue.removeHead()
            if (mask == allMask) return dist
            for ((dx, dy) <- dirs) {
                val nx = x + dx
                val ny = y + dy
                if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                    val ch = grid(nx)(ny)
                    if (ch != '#') {
                        var canMove = true
                        var newMask = mask
                        if (ch >= 'A' && ch <= 'F') {
                            val need = 1 << (ch - 'A')
                            if ((mask & need) == 0) canMove = false
                        } else if (ch >= 'a' && ch <= 'f') {
                            newMask |= 1 << (ch - 'a')
                        }
                        if (canMove && !visited(nx)(ny)(newMask)) {
                            visited(nx)(ny)(newMask) = true
                            queue.append((nx, ny, newMask, dist + 1))
                        }
                    }
                }
            }
        }
        -1
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return -1;
        }
        let n = grid[0].len();

        // Convert grid to char matrix and locate start & target mask
        let mut g: Vec<Vec<char>> = vec![vec![' '; n]; m];
        let mut start_x = 0usize;
        let mut start_y = 0usize;
        let mut target_mask: usize = 0;

        for i in 0..m {
            let chars: Vec<char> = grid[i].chars().collect();
            for j in 0..n {
                g[i][j] = chars[j];
                match chars[j] {
                    '@' => {
                        start_x = i;
                        start_y = j;
                    }
                    c if c.is_ascii_lowercase() => {
                        let bit = (c as u8 - b'a') as usize;
                        target_mask |= 1 << bit;
                    }
                    _ => {}
                }
            }
        }

        // visited[x][y][mask]
        const MAX_KEYS: usize = 6;
        let mask_size = 1usize << MAX_KEYS;
        let mut visited = vec![vec![vec![false; mask_size]; n]; m];
        let mut q: VecDeque<(usize, usize, usize, i32)> = VecDeque::new();

        visited[start_x][start_y][0] = true;
        q.push_back((start_x, start_y, 0, 0));

        let dirs = [(0i32, 1i32), (0, -1), (1, 0), (-1, 0)];

        while let Some((x, y, mask, steps)) = q.pop_front() {
            if mask == target_mask {
                return steps;
            }
            for &(dx, dy) in &dirs {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx < 0 || ny < 0 || nx >= m as i32 || ny >= n as i32 {
                    continue;
                }
                let ux = nx as usize;
                let uy = ny as usize;
                let cell = g[ux][uy];
                if cell == '#' {
                    continue;
                }

                // If it's a lock, need the key
                if cell.is_ascii_uppercase() {
                    let bit = (cell as u8 - b'A') as usize;
                    if (mask & (1 << bit)) == 0 {
                        continue;
                    }
                }

                let mut new_mask = mask;
                // If it's a key, pick it up
                if cell.is_ascii_lowercase() {
                    let bit = (cell as u8 - b'a') as usize;
                    new_mask |= 1 << bit;
                }

                if !visited[ux][uy][new_mask] {
                    visited[ux][uy][new_mask] = true;
                    q.push_back((ux, uy, new_mask, steps + 1));
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
(define/contract (shortest-path-all-keys grid)
  (-> (listof string?) exact-integer?)
  (let* ((rows (length grid))
         (cols (string-length (first grid)))
         (grid-vec (list->vector grid))
         (lowercase?
          (lambda (ch)
            (and (>= (char->integer ch) (char->integer #\a))
                 (<= (char->integer ch) (char->integer #\f)))))
         (uppercase?
          (lambda (ch)
            (and (>= (char->integer ch) (char->integer #\A))
                 (<= (char->integer ch) (char->integer #\F)))))
         (startx -1)
         (starty -1)
         (allMask 0))

    ;; locate start and compute all keys mask
    (for ([i (in-range rows)])
      (let ((row (vector-ref grid-vec i)))
        (for ([j (in-range cols)])
          (define ch (string-ref row j))
          (cond [(char=? ch #\@) (set! startx i) (set! starty j)]
                [(lowercase? ch)
                 (set! allMask
                       (bitwise-ior allMask
                                    (arithmetic-shift 1
                                                       (- (char->integer ch)
                                                          (char->integer #\a)))))]))))

    ;; visited[x][y][mask] = #t if seen
    (define visited
      (let ((v (make-vector rows)))
        (for ([i (in-range rows)])
          (vector-set! v i
                       (let ((rowvec (make-vector cols)))
                         (for ([j (in-range cols)])
                           (vector-set! rowvec j (make-vector 64 #f)))
                         rowvec)))
        v))

    ;; mark start visited
    (vector-set!
     (vector-ref (vector-ref visited startx) starty)
     0
     #t)

    (define dirs '((0 1) (0 -1) (1 0) (-1 0)))

    (call-with-current-continuation
      (lambda (return)
        (let loop ((frontier (list (list startx starty 0))) (steps 0))
          (if (null? frontier)
              (return -1)
              (let ((next '()))
                (for ([state frontier])
                  (match-define (list x y mask) state)

                  ;; reached all keys?
                  (when (= mask allMask)
                    (return steps))

                  ;; explore neighbours
                  (for ([dir dirs])
                    (define dx (first dir))
                    (define dy (second dir))
                    (define nx (+ x dx))
                    (define ny (+ y dy))
                    (when (and (>= nx 0) (< nx rows)
                               (>= ny 0) (< ny cols))
                      (define ch (string-ref (vector-ref grid-vec nx) ny))
                      (cond
                        [(char=? ch #\#) (void)] ; wall
                        [else
                         (define newMask mask)
                         (when (lowercase? ch)
                           (set! newMask
                                 (bitwise-ior newMask
                                              (arithmetic-shift 1
                                                                 (- (char->integer ch)
                                                                    (char->integer #\a))))))
                         (when (uppercase? ch)
                           (define needBit
                             (arithmetic-shift 1
                                                (- (char->integer ch)
                                                   (char->integer #\A))))
                           (unless (zero? (bitwise-and mask needBit))
                             (void))) ; have key, continue
                         ;; after lock check, ensure we can move
                         (when (or (not (uppercase? ch))
                                   (let* ((needBit
                                           (arithmetic-shift 1
                                                              (- (char->integer ch)
                                                                 (char->integer #\A)))))
                                          (not (zero? (bitwise-and mask needBit)))))
                           (define cell-vec (vector-ref (vector-ref visited nx) ny))
                           (unless (vector-ref cell-vec newMask)
                             (vector-set! cell-vec newMask #t)
                             (set! next (cons (list nx ny newMask) next))))]))))
                (loop (reverse next) (+ steps 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([shortest_path_all_keys/1]).

-define(DIRS, [{-1,0},{1,0},{0,-1},{0,1}]).

-spec shortest_path_all_keys(Grid :: [unicode:unicode_binary()]) -> integer().
shortest_path_all_keys(Grid) ->
    Rows = [binary_to_list(Row) || Row <- Grid],
    M = length(Rows),
    N = length(hd(Rows)),
    {StartX, StartY, AllMask} = find_start_and_mask(Rows, 0, undefined, 0),
    bfs(queue:in({StartX, StartY, 0, 0}, queue:new()),
        #{encode(StartX, StartY, 0, N) => true},
        Rows, M, N, AllMask).

%% Find start position and compute mask of all keys
find_start_and_mask([], _RowIdx, {SX,SY}=Start, Mask) ->
    {SX, SY, Mask};
find_start_and_mask([Row|Rest], RowIdx, StartAcc, MaskAcc) ->
    case find_in_row(Row, 0, RowIdx, StartAcc, MaskAcc) of
        {NewStart, NewMask} -> find_start_and_mask(Rest, RowIdx + 1, NewStart, NewMask)
    end.

find_in_row([], _ColIdx, _RowIdx, Start, Mask) ->
    {Start, Mask};
find_in_row([C|Cs], ColIdx, RowIdx, undefined, MaskAcc) when C =:= $@ ->
    find_in_row(Cs, ColIdx + 1, RowIdx, {RowIdx, ColIdx}, MaskAcc);
find_in_row([C|Cs], ColIdx, RowIdx, StartAcc, MaskAcc) when C >= $a, C =< $f ->
    Bit = C - $a,
    NewMask = MaskAcc bor (1 bsl Bit),
    find_in_row(Cs, ColIdx + 1, RowIdx, StartAcc, NewMask);
find_in_row([C|Cs], ColIdx, RowIdx, StartAcc, MaskAcc) when C >= $A, C =< $F ->
    Bit = C - $A,
    NewMask = MaskAcc bor (1 bsl Bit),
    find_in_row(Cs, ColIdx + 1, RowIdx, StartAcc, NewMask);
find_in_row([_|Cs], ColIdx, RowIdx, StartAcc, MaskAcc) ->
    find_in_row(Cs, ColIdx + 1, RowIdx, StartAcc, MaskAcc).

%% BFS using queue
bfs(Q, Visited, Rows, M, N, AllMask) ->
    case queue:out(Q) of
        {{value, {X,Y,Mask,Dist}}, QRest} ->
            if Mask =:= AllMask ->
                    Dist;
               true ->
                    {QNew, VisNew} = explore_neighbors({X,Y,Mask,Dist}, QRest, Visited, Rows, M, N, AllMask),
                    bfs(QNew, VisNew, Rows, M, N, AllMask)
            end;
        {empty, _} -> -1
    end.

explore_neighbors({_X,_Y,_Mask,_Dist}=State, Q, Visited, Rows, M, N, AllMask) ->
    lists:foldl(fun(Dir, {QAcc, VisAcc}) ->
                        explore_one(State, Dir, QAcc, VisAcc, Rows, M, N)
                end, {Q, Visited}, ?DIRS).

explore_one({X,Y,Mask,Dist}, {DX,DY}, Q, Visited, Rows, M, N) ->
    NX = X + DX,
    NY = Y + DY,
    if NX < 0 orelse NX >= M orelse NY < 0 orelse NY >= N ->
            {Q, Visited};
       true ->
            Cell = cell_at(Rows, NX, NY),
            case Cell of
                $# -> {Q, Visited}; % wall
                C when C >= $a, C =< $f ->
                    Bit = C - $a,
                    NewMask = Mask bor (1 bsl Bit),
                    try_enqueue(NX, NY, NewMask, Dist+1, Q, Visited, N);
                C when C >= $A, C =< $F ->
                    Bit = C - $A,
                    if (Mask band (1 bsl Bit)) =/= 0 ->
                            try_enqueue(NX, NY, Mask, Dist+1, Q, Visited, N);
                       true -> {Q, Visited}
                    end;
                _ ->
                    try_enqueue(NX, NY, Mask, Dist+1, Q, Visited, N)
            end
    end.

try_enqueue(X, Y, Mask, Dist, Q, Visited, Cols) ->
    Key = encode(X, Y, Mask, Cols),
    case maps:is_key(Key, Visited) of
        true -> {Q, Visited};
        false ->
            NewQ = queue:in({X, Y, Mask, Dist}, Q),
            NewVis = maps:put(Key, true, Visited),
            {NewQ, NewVis}
    end.

cell_at(Rows, X, Y) ->
    Row = lists:nth(X+1, Rows),
    lists:nth(Y+1, Row).

encode(X, Y, Mask, Cols) ->
    ((X * Cols + Y) bsl 6) bor Mask.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_path_all_keys(grid :: [String.t]) :: integer
  def shortest_path_all_keys(grid) do
    import Bitwise

    rows = length(grid)
    cols = String.length(List.first(grid))

    grid_tup = grid |> Enum.map(&String.to_charlist/1) |> List.to_tuple()

    {start_x, start_y, total_keys} =
      Enum.reduce(0..rows - 1, {nil, nil, 0}, fn i, {sx, sy, cnt} ->
        row = elem(grid_tup, i)

        Enum.reduce(0..cols - 1, {sx, sy, cnt}, fn j, {sx2, sy2, cnt2} ->
          cell = Enum.at(row, j)

          cond do
            cell == ?@ -> {i, j, cnt2}
            cell in ?a..?f -> {sx2, sy2, cnt2 + 1}
            true -> {sx2, sy2, cnt2}
          end
        end)
      end)

    all_keys_mask = (1 <<< total_keys) - 1

    queue0 = :queue.new()
    queue = :queue.in({start_x, start_y, 0, 0}, queue0)
    visited = MapSet.new([{start_x, start_y, 0}])

    dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]
    bfs(queue, visited, grid_tup, rows, cols, all_keys_mask, dirs)
  end

  defp bfs(queue, visited, grid, rows, cols, target_mask, dirs) do
    import Bitwise

    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {x, y, mask, dist}}, qrest} ->
        if mask == target_mask do
          dist
        else
          {new_queue, new_visited} =
            Enum.reduce(dirs, {qrest, visited}, fn {dx, dy}, {qacc, vacc} ->
              nx = x + dx
              ny = y + dy

              if nx < 0 or nx >= rows or ny < 0 or ny >= cols do
                {qacc, vacc}
              else
                cell = get_cell(grid, nx, ny)

                cond do
                  cell == ?# ->
                    {qacc, vacc}

                  cell in ?A..?F ->
                    key_bit = 1 <<< (cell - ?A)

                    if (mask &&& key_bit) != 0 do
                      state = {nx, ny, mask}

                      if MapSet.member?(vacc, state) do
                        {qacc, vacc}
                      else
                        {
                          :queue.in({nx, ny, mask, dist + 1}, qacc),
                          MapSet.put(vacc, state)
                        }
                      end
                    else
                      {qacc, vacc}
                    end

                  true ->
                    new_mask =
                      if cell in ?a..?f do
                        mask ||| (1 <<< (cell - ?a))
                      else
                        mask
                      end

                    state = {nx, ny, new_mask}

                    if MapSet.member?(vacc, state) do
                      {qacc, vacc}
                    else
                      {
                        :queue.in({nx, ny, new_mask, dist + 1}, qacc),
                        MapSet.put(vacc, state)
                      }
                    end
                end
              end
            end)

          bfs(new_queue, new_visited, grid, rows, cols, target_mask, dirs)
        end
    end
  end

  defp get_cell(grid, x, y) do
    row = elem(grid, x)
    Enum.at(row, y)
  end
end
```

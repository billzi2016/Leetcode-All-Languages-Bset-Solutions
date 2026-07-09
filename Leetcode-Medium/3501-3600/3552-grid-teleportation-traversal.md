# 3552. Grid Teleportation Traversal

## Cpp

```cpp
class Solution {
public:
    int minMoves(vector<string>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<pair<int,int>>> portals(26);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                char c = matrix[i][j];
                if (c >= 'A' && c <= 'Z') {
                    portals[c - 'A'].push_back({i, j});
                }
            }
        }
        vector<vector<int>> dist(m, vector<int>(n, -1));
        deque<pair<int,int>> dq;
        dist[0][0] = 0;
        dq.push_back({0,0});
        bool usedLetter[26] = {false};
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        while (!dq.empty()) {
            auto [x,y] = dq.front();
            dq.pop_front();
            int d = dist[x][y];
            if (x == m-1 && y == n-1) return d;
            // adjacent moves
            for (auto &dir : dirs) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (matrix[nx][ny] == '#') continue;
                if (dist[nx][ny] != -1) continue;
                dist[nx][ny] = d + 1;
                dq.push_back({nx, ny});
            }
            // teleport
            char c = matrix[x][y];
            if (c >= 'A' && c <= 'Z') {
                int idx = c - 'A';
                if (!usedLetter[idx]) {
                    usedLetter[idx] = true;
                    for (auto &p : portals[idx]) {
                        int tx = p.first, ty = p.second;
                        if (dist[tx][ty] == -1) {
                            dist[tx][ty] = d; // zero cost
                            dq.push_front({tx, ty});
                        }
                    }
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
    public int minMoves(String[] matrix) {
        int m = matrix.length;
        int n = matrix[0].length();
        @SuppressWarnings("unchecked")
        List<Integer>[] portals = new ArrayList[26];
        for (int i = 0; i < 26; i++) portals[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            String row = matrix[i];
            for (int j = 0; j < n; j++) {
                char c = row.charAt(j);
                if (c >= 'A' && c <= 'Z') {
                    portals[c - 'A'].add(i * n + j);
                }
            }
        }

        boolean[][] visited = new boolean[m][n];
        int[][] dist = new int[m][n];
        for (int[] r : dist) java.util.Arrays.fill(r, -1);

        ArrayDeque<int[]> q = new ArrayDeque<>();
        visited[0][0] = true;
        dist[0][0] = 0;
        q.offer(new int[]{0, 0});

        boolean[] usedPortal = new boolean[26];
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            int d = dist[r][c];

            if (r == m - 1 && c == n - 1) return d;

            char ch = matrix[r].charAt(c);
            if (ch >= 'A' && ch <= 'Z') {
                int idx = ch - 'A';
                if (!usedPortal[idx]) {
                    usedPortal[idx] = true;
                    for (int code : portals[idx]) {
                        int nr = code / n;
                        int nc = code % n;
                        if (!visited[nr][nc]) {
                            visited[nr][nc] = true;
                            dist[nr][nc] = d; // teleport costs 0 moves
                            q.offerFirst(new int[]{nr, nc});
                        }
                    }
                }
            }

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (visited[nr][nc]) continue;
                if (matrix[nr].charAt(nc) == '#') continue;
                visited[nr][nc] = true;
                dist[nr][nc] = d + 1;
                q.offer(new int[]{nr, nc});
            }
        }

        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minMoves(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        from collections import deque, defaultdict

        m = len(matrix)
        n = len(matrix[0])

        # collect portal positions
        portals = defaultdict(list)
        for i in range(m):
            row = matrix[i]
            for j, ch in enumerate(row):
                if 'A' <= ch <= 'Z':
                    portals[ch].append((i, j))

        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((0, 0, 0))   # i, j, distance
        visited[0][0] = True

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            i, j, d = q.popleft()
            if i == m - 1 and j == n - 1:
                return d

            # teleport via portal (zero cost)
            ch = matrix[i][j]
            if 'A' <= ch <= 'Z':
                lst = portals.get(ch)
                if lst:
                    for pi, pj in lst:
                        if not visited[pi][pj]:
                            visited[pi][pj] = True
                            q.appendleft((pi, pj, d))   # same distance
                    portals[ch] = []  # portal used

            nd = d + 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    if matrix[ni][nj] != '#':
                        visited[ni][nj] = True
                        q.append((ni, nj, nd))

        return -1
```

## Python3

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        portals = defaultdict(list)
        for i in range(m):
            row = matrix[i]
            for j, ch in enumerate(row):
                if 'A' <= ch <= 'Z':
                    portals[ch].append((i, j))

        visited = [[False] * n for _ in range(m)]
        dq = deque()
        dq.append((0, 0, 0))
        visited[0][0] = True

        while dq:
            i, j, d = dq.popleft()
            if i == m - 1 and j == n - 1:
                return d

            # move to adjacent cells
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and matrix[ni][nj] != '#':
                    visited[ni][nj] = True
                    dq.append((ni, nj, d + 1))

            # teleport via portal (zero cost)
            ch = matrix[i][j]
            if 'A' <= ch <= 'Z' and ch in portals:
                for pi, pj in portals[ch]:
                    if not visited[pi][pj]:
                        visited[pi][pj] = True
                        dq.appendleft((pi, pj, d))  # zero-cost edge
                del portals[ch]  # portal can be used only once

        return -1
```

## C

```c
#include <stdlib.h>
#include <string.h>

int minMoves(char** matrix, int matrixSize) {
    if (matrixSize == 0) return -1;
    int m = matrixSize;
    int n = (int)strlen(matrix[0]);
    int total = m * n;

    // visited array
    char *vis = (char *)calloc(total, sizeof(char));
    if (!vis) return -1;

    // portal counting
    int cnt[26] = {0};
    for (int i = 0; i < m; ++i) {
        const char *row = matrix[i];
        for (int j = 0; j < n; ++j) {
            char c = row[j];
            if (c >= 'A' && c <= 'Z') cnt[c - 'A']++;
        }
    }

    // allocate storage for portal positions (flattened index)
    int *portalPos[26] = {0};
    for (int k = 0; k < 26; ++k) {
        if (cnt[k] > 0) {
            portalPos[k] = (int *)malloc(cnt[k] * sizeof(int));
            cnt[k] = 0; // reuse as fill counter
        }
    }

    // fill portal positions
    for (int i = 0; i < m; ++i) {
        const char *row = matrix[i];
        for (int j = 0; j < n; ++j) {
            char c = row[j];
            if (c >= 'A' && c <= 'Z') {
                int idx = i * n + j;
                int k = c - 'A';
                portalPos[k][cnt[k]++] = idx;
            }
        }
    }

    // BFS queue
    int *qx = (int *)malloc(total * sizeof(int));
    int *qy = (int *)malloc(total * sizeof(int));
    int *qd = (int *)malloc(total * sizeof(int));
    if (!qx || !qy || !qd) {
        free(vis);
        for (int k = 0; k < 26; ++k) if (portalPos[k]) free(portalPos[k]);
        return -1;
    }

    int head = 0, tail = 0;
    qx[tail] = 0;
    qy[tail] = 0;
    qd[tail] = 0;
    ++tail;
    vis[0] = 1;

    char usedLetter[26] = {0};
    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    while (head < tail) {
        int x = qx[head];
        int y = qy[head];
        int d = qd[head];
        ++head;

        if (x == m - 1 && y == n - 1) {
            // clean up
            free(vis);
            for (int k = 0; k < 26; ++k) if (portalPos[k]) free(portalPos[k]);
            free(qx); free(qy); free(qd);
            return d;
        }

        // normal moves
        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dirs[dir][0];
            int ny = y + dirs[dir][1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (matrix[nx][ny] == '#') continue;
            int nid = nx * n + ny;
            if (!vis[nid]) {
                vis[nid] = 1;
                qx[tail] = nx;
                qy[tail] = ny;
                qd[tail] = d + 1;
                ++tail;
            }
        }

        // portal teleportation
        char cur = matrix[x][y];
        if (cur >= 'A' && cur <= 'Z') {
            int k = cur - 'A';
            if (!usedLetter[k]) {
                usedLetter[k] = 1;
                for (int i = 0; i < cnt[k]; ++i) {
                    int pid = portalPos[k][i];
                    if (!vis[pid]) {
                        vis[pid] = 1;
                        qx[tail] = pid / n;
                        qy[tail] = pid % n;
                        qd[tail] = d; // teleport is free
                        ++tail;
                    }
                }
            }
        }
    }

    // not reachable
    free(vis);
    for (int k = 0; k < 26; ++k) if (portalPos[k]) free(portalPos[k]);
    free(qx); free(qy); free(qd);
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinMoves(string[] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        // Store portal positions for each letter A-Z
        List<(int r, int c)>[] portals = new List<(int, int)>[26];
        for (int i = 0; i < 26; i++) portals[i] = new List<(int, int)>();
        for (int i = 0; i < m; i++) {
            string row = matrix[i];
            for (int j = 0; j < n; j++) {
                char ch = row[j];
                if (ch >= 'A' && ch <= 'Z') {
                    portals[ch - 'A'].Add((i, j));
                }
            }
        }

        int[,] dist = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                dist[i, j] = -1;

        Queue<(int r, int c)> q = new Queue<(int, int)>();
        dist[0, 0] = 0;
        q.Enqueue((0, 0));

        bool[] usedLetter = new bool[26];
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (q.Count > 0) {
            var cur = q.Dequeue();
            int r = cur.r;
            int c = cur.c;
            int d = dist[r, c];

            if (r == m - 1 && c == n - 1) return d;

            char ch = matrix[r][c];
            if (ch >= 'A' && ch <= 'Z') {
                int idx = ch - 'A';
                if (!usedLetter[idx]) {
                    foreach (var pos in portals[idx]) {
                        int nr = pos.r, nc = pos.c;
                        if (dist[nr, nc] == -1) {
                            dist[nr, nc] = d; // teleport costs 0 moves
                            q.Enqueue((nr, nc));
                        }
                    }
                    usedLetter[idx] = true;
                }
            }

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    if (matrix[nr][nc] != '#' && dist[nr, nc] == -1) {
                        dist[nr, nc] = d + 1;
                        q.Enqueue((nr, nc));
                    }
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
 * @param {string[]} matrix
 * @return {number}
 */
var minMoves = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const total = m * n;

    // visited cells
    const visited = new Uint8Array(total);

    // map portal letter -> list of positions
    const portalMap = {};
    for (let i = 0; i < m; ++i) {
        const row = matrix[i];
        for (let j = 0; j < n; ++j) {
            const ch = row[j];
            if (ch >= 'A' && ch <= 'Z') {
                if (!portalMap[ch]) portalMap[ch] = [];
                portalMap[ch].push([i, j]);
            }
        }
    }

    // BFS queues
    const qRow = new Int32Array(total);
    const qCol = new Int32Array(total);
    const qDist = new Int32Array(total);
    let head = 0, tail = 0;

    function enqueue(r, c, d) {
        visited[r * n + c] = 1;
        qRow[tail] = r;
        qCol[tail] = c;
        qDist[tail] = d;
        ++tail;
    }

    enqueue(0, 0, 0);
    const usedPortal = {};

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];

    while (head < tail) {
        const r = qRow[head];
        const c = qCol[head];
        const d = qDist[head];
        ++head;

        if (r === m - 1 && c === n - 1) return d;

        // teleport via portal
        const ch = matrix[r][c];
        if (ch >= 'A' && ch <= 'Z' && !usedPortal[ch]) {
            usedPortal[ch] = true;
            const list = portalMap[ch];
            for (const [nr, nc] of list) {
                const idx = nr * n + nc;
                if (!visited[idx]) {
                    visited[idx] = 1;
                    qRow[tail] = nr;
                    qCol[tail] = nc;
                    qDist[tail] = d; // free teleport
                    ++tail;
                }
            }
        }

        // normal moves
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (matrix[nr][nc] === '#') continue;
            const idx = nr * n + nc;
            if (!visited[idx]) {
                visited[idx] = 1;
                qRow[tail] = nr;
                qCol[tail] = nc;
                qDist[tail] = d + 1;
                ++tail;
            }
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minMoves(matrix: string[]): number {
    const m = matrix.length;
    const n = matrix[0].length;
    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    // Map each portal letter to list of flattened indices
    const portalMap = new Map<string, number[]>();
    for (let i = 0; i < m; i++) {
        const row = matrix[i];
        for (let j = 0; j < n; j++) {
            const ch = row[j];
            if (ch >= 'A' && ch <= 'Z') {
                const idx = i * n + j;
                if (!portalMap.has(ch)) portalMap.set(ch, []);
                portalMap.get(ch)!.push(idx);
            }
        }
    }

    const total = m * n;
    const visited = new Uint8Array(total);
    const dist = new Int32Array(total);
    const queue: number[] = [];
    let head = 0;

    const startIdx = 0; // (0,0)
    visited[startIdx] = 1;
    dist[startIdx] = 0;
    queue.push(startIdx);

    const usedPortal = new Set<string>();

    while (head < queue.length) {
        const cur = queue[head++];
        const curDist = dist[cur];
        const i = Math.floor(cur / n);
        const j = cur % n;

        if (i === m - 1 && j === n - 1) return curDist;

        // Move to adjacent cells
        for (const [di, dj] of dirs) {
            const ni = i + di;
            const nj = j + dj;
            if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
            if (matrix[ni][nj] === '#') continue;
            const nxtIdx = ni * n + nj;
            if (!visited[nxtIdx]) {
                visited[nxtIdx] = 1;
                dist[nxtIdx] = curDist + 1;
                queue.push(nxtIdx);
            }
        }

        // Teleport via portal
        const ch = matrix[i][j];
        if (ch >= 'A' && ch <= 'Z' && !usedPortal.has(ch)) {
            usedPortal.add(ch);
            const list = portalMap.get(ch)!;
            for (const idx of list) {
                if (!visited[idx]) {
                    visited[idx] = 1;
                    dist[idx] = curDist; // teleport costs 0 moves
                    queue.push(idx);
                }
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
     * @param String[] $matrix
     * @return Integer
     */
    function minMoves($matrix) {
        $m = count($matrix);
        if ($m == 0) return -1;
        $n = strlen($matrix[0]);

        // Preprocess portals
        $portals = [];
        for ($i = 0; $i < $m; $i++) {
            $row = $matrix[$i];
            $len = strlen($row);
            for ($j = 0; $j < $len; $j++) {
                $ch = $row[$j];
                if ($ch >= 'A' && $ch <= 'Z') {
                    $portals[$ch][] = [$i, $j];
                }
            }
        }

        // Distance matrix, -1 means unvisited
        $dist = array_fill(0, $m, array_fill(0, $n, -1));

        $queue = new SplQueue();
        $queue->enqueue(0); // encode (0,0) as 0*$n + 0
        $dist[0][0] = 0;

        $usedPortal = [];

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$queue->isEmpty()) {
            $code = $queue->dequeue();
            $i = intdiv($code, $n);
            $j = $code % $n;
            $d = $dist[$i][$j];

            if ($i == $m - 1 && $j == $n - 1) {
                return $d;
            }

            // Move to adjacent cells
            foreach ($dirs as $dir) {
                $ni = $i + $dir[0];
                $nj = $j + $dir[1];
                if ($ni >= 0 && $ni < $m && $nj >= 0 && $nj < $n && $matrix[$ni][$nj] !== '#') {
                    if ($dist[$ni][$nj] == -1) {
                        $dist[$ni][$nj] = $d + 1;
                        $queue->enqueue($ni * $n + $nj);
                    }
                }
            }

            // Teleport via portal
            $c = $matrix[$i][$j];
            if ($c >= 'A' && $c <= 'Z') {
                if (!isset($usedPortal[$c])) {
                    $usedPortal[$c] = true;
                    foreach ($portals[$c] as $pos) {
                        $pi = $pos[0];
                        $pj = $pos[1];
                        if ($dist[$pi][$pj] == -1) {
                            $dist[$pi][$pj] = $d; // teleport costs 0 moves
                            $queue->enqueue($pi * $n + $pj);
                        }
                    }
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
    func minMoves(_ matrix: [String]) -> Int {
        let m = matrix.count
        guard m > 0 else { return -1 }
        let n = matrix[0].count
        if m == 1 && n == 1 { return 0 }
        
        // Convert to grid of characters
        var grid = [[Character]]()
        for row in matrix {
            grid.append(Array(row))
        }
        
        // Map portals: letter -> list of positions
        var portalMap = [Character: [(Int, Int)]]()
        for i in 0..<m {
            for j in 0..<n {
                let ch = grid[i][j]
                if ch != "." && ch != "#" {
                    portalMap[ch, default: []].append((i, j))
                }
            }
        }
        
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        struct Node { let x: Int; let y: Int; let d: Int }
        var queue = [Node]()
        var head = 0
        
        visited[0][0] = true
        queue.append(Node(x: 0, y: 0, d: 0))
        
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while head < queue.count {
            let cur = queue[head]
            head += 1
            if cur.x == m - 1 && cur.y == n - 1 {
                return cur.d
            }
            
            // Adjacent moves
            for (dx, dy) in dirs {
                let nx = cur.x + dx
                let ny = cur.y + dy
                if nx >= 0 && nx < m && ny >= 0 && ny < n &&
                    !visited[nx][ny] && grid[nx][ny] != "#" {
                    visited[nx][ny] = true
                    queue.append(Node(x: nx, y: ny, d: cur.d + 1))
                }
            }
            
            // Teleport via portal if not used yet
            let ch = grid[cur.x][cur.y]
            if ch != "." && ch != "#" {
                if let positions = portalMap[ch] {
                    for (px, py) in positions {
                        if !visited[px][py] {
                            visited[px][py] = true
                            queue.append(Node(x: px, y: py, d: cur.d)) // zero-cost move
                        }
                    }
                    portalMap[ch] = [] // mark portal as used
                }
            }
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMoves(matrix: Array<String>): Int {
        val m = matrix.size
        val n = matrix[0].length
        val total = m * n
        val visited = BooleanArray(total)
        val dist = IntArray(total) { -1 }
        val portalUsed = BooleanArray(26)
        val portals = Array(26) { mutableListOf<Int>() }

        // Preprocess portal positions
        for (i in 0 until m) {
            val row = matrix[i]
            for (j in 0 until n) {
                val c = row[j]
                if (c in 'A'..'Z') {
                    portals[c - 'A'].add(i * n + j)
                }
            }
        }

        val queue: ArrayDeque<Int> = ArrayDeque()
        visited[0] = true
        dist[0] = 0
        queue.add(0)

        val dirs = intArrayOf(-1, 0, 1, 0, -1) // for iteration

        while (queue.isNotEmpty()) {
            val idx = queue.removeFirst()
            val d = dist[idx]
            val i = idx / n
            val j = idx % n

            if (i == m - 1 && j == n - 1) return d

            // Move to adjacent cells
            for (k in 0 until 4) {
                val ni = i + dirs[k]
                val nj = j + dirs[k + 1]
                if (ni in 0 until m && nj in 0 until n) {
                    if (matrix[ni][nj] != '#') {
                        val nIdx = ni * n + nj
                        if (!visited[nIdx]) {
                            visited[nIdx] = true
                            dist[nIdx] = d + 1
                            queue.add(nIdx)
                        }
                    }
                }
            }

            // Teleport via portal if applicable
            val ch = matrix[i][j]
            if (ch in 'A'..'Z') {
                val p = ch - 'A'
                if (!portalUsed[p]) {
                    portalUsed[p] = true
                    for (otherIdx in portals[p]) {
                        if (!visited[otherIdx]) {
                            visited[otherIdx] = true
                            dist[otherIdx] = d // teleport costs 0 moves
                            queue.add(otherIdx)
                        }
                    }
                }
            }
        }

        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minMoves(List<String> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    int total = m * n;
    List<bool> visited = List.filled(total, false);
    List<int> dist = List.filled(total, 0);
    // portals per letter
    List<List<int>> portalPos = List.generate(26, (_) => []);
    for (int i = 0; i < m; ++i) {
      String row = matrix[i];
      for (int j = 0; j < n; ++j) {
        int code = row.codeUnitAt(j);
        if (code >= 65 && code <= 90) { // 'A'..'Z'
          portalPos[code - 65].add(i * n + j);
        }
      }
    }

    List<bool> usedPortal = List.filled(26, false);
    List<int> queue = [];
    int head = 0;

    int startIdx = 0;
    visited[startIdx] = true;
    dist[startIdx] = 0;
    queue.add(startIdx);

    int targetIdx = total - 1;
    const List<int> dirI = [-1, 1, 0, 0];
    const List<int> dirJ = [0, 0, -1, 1];

    while (head < queue.length) {
      int cur = queue[head++];
      if (cur == targetIdx) return dist[cur];
      int ci = cur ~/ n;
      int cj = cur % n;

      // normal moves
      for (int d = 0; d < 4; ++d) {
        int ni = ci + dirI[d];
        int nj = cj + dirJ[d];
        if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
        int code = matrix[ni].codeUnitAt(nj);
        if (code == 35) continue; // '#'
        int nxt = ni * n + nj;
        if (!visited[nxt]) {
          visited[nxt] = true;
          dist[nxt] = dist[cur] + 1;
          queue.add(nxt);
        }
      }

      // portal teleport
      int curCode = matrix[ci].codeUnitAt(cj);
      if (curCode >= 65 && curCode <= 90) {
        int idx = curCode - 65;
        if (!usedPortal[idx]) {
          usedPortal[idx] = true;
          for (int pos in portalPos[idx]) {
            if (!visited[pos]) {
              visited[pos] = true;
              dist[pos] = dist[cur]; // no extra move
              queue.add(pos);
            }
          }
        }
      }
    }

    return -1;
  }
}
```

## Golang

```go
func minMoves(matrix []string) int {
    m := len(matrix)
    n := len(matrix[0])

    type Pos struct{ x, y int }
    portals := make([][]Pos, 26)

    for i := 0; i < m; i++ {
        row := matrix[i]
        for j := 0; j < n; j++ {
            c := row[j]
            if c >= 'A' && c <= 'Z' {
                idx := c - 'A'
                portals[idx] = append(portals[idx], Pos{i, j})
            }
        }
    }

    visited := make([][]bool, m)
    for i := 0; i < m; i++ {
        visited[i] = make([]bool, n)
    }

    type Node struct{ x, y, d int }
    queue := make([]Node, 0, m*n)
    queue = append(queue, Node{0, 0, 0})
    visited[0][0] = true

    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    usedPortal := make([]bool, 26)

    for head := 0; head < len(queue); head++ {
        cur := queue[head]
        if cur.x == m-1 && cur.y == n-1 {
            return cur.d
        }

        c := matrix[cur.x][cur.y]
        if c >= 'A' && c <= 'Z' {
            idx := c - 'A'
            if !usedPortal[idx] {
                for _, p := range portals[idx] {
                    if !visited[p.x][p.y] {
                        visited[p.x][p.y] = true
                        queue = append(queue, Node{p.x, p.y, cur.d})
                    }
                }
                usedPortal[idx] = true
                portals[idx] = nil // free memory
            }
        }

        for _, d := range dirs {
            nx, ny := cur.x+d[0], cur.y+d[1]
            if nx < 0 || nx >= m || ny < 0 || ny >= n {
                continue
            }
            if visited[nx][ny] || matrix[nx][ny] == '#' {
                continue
            }
            visited[nx][ny] = true
            queue = append(queue, Node{nx, ny, cur.d + 1})
        }
    }

    return -1
}
```

## Ruby

```ruby
def min_moves(matrix)
  m = matrix.size
  n = matrix[0].size

  portals = Hash.new { |h, k| h[k] = [] }
  (0...m).each do |i|
    row = matrix[i]
    (0...n).each do |j|
      ch = row[j]
      if ('A' <= ch && ch <= 'Z')
        portals[ch] << [i, j]
      end
    end
  end

  visited = Array.new(m) { Array.new(n, false) }

  class Deque
    def initialize
      @front = []
      @back = []
    end

    def push_front(val)
      @front << val
    end

    def push_back(val)
      @back << val
    end

    def empty?
      @front.empty? && @back.empty?
    end

    def pop_front
      if @front.empty?
        while !@back.empty?
          @front << @back.pop
        end
      end
      @front.pop
    end
  end

  dq = Deque.new
  dq.push_back([0, 0, 0])
  visited[0][0] = true
  used_portal = {}

  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

  while !dq.empty?
    i, j, d = dq.pop_front
    return d if i == m - 1 && j == n - 1

    ch = matrix[i][j]
    if ('A' <= ch && ch <= 'Z') && !used_portal[ch]
      used_portal[ch] = true
      portals[ch].each do |pi, pj|
        next if visited[pi][pj]
        visited[pi][pj] = true
        dq.push_front([pi, pj, d])
      end
    end

    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      next if ni < 0 || nj < 0 || ni >= m || nj >= n
      next if matrix[ni][nj] == '#'
      next if visited[ni][nj]
      visited[ni][nj] = true
      dq.push_back([ni, nj, d + 1])
    end
  end

  -1
end
```

## Scala

```scala
import java.util.ArrayDeque

object Solution {
  def minMoves(matrix: Array[String]): Int = {
    val m = matrix.length
    val n = matrix(0).length
    val grid = matrix.map(_.toCharArray)

    // Collect portal positions for each letter A-Z
    val portals = Array.fill(26)(scala.collection.mutable.ArrayBuffer[(Int, Int)]())
    for (i <- 0 until m; j <- 0 until n) {
      val ch = grid(i)(j)
      if (ch >= 'A' && ch <= 'Z') {
        portals(ch - 'A').append((i, j))
      }
    }

    val visited = Array.ofDim[Boolean](m, n)
    val dist = Array.ofDim[Int](m, n)

    val usedPortal = new Array[Boolean](26)

    val deque: ArrayDeque[(Int, Int)] = new ArrayDeque()
    deque.addLast((0, 0))
    visited(0)(0) = true
    dist(0)(0) = 0

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (!deque.isEmpty) {
      val (r, c) = deque.pollFirst()
      val d = dist(r)(c)

      if (r == m - 1 && c == n - 1) return d

      // Normal moves
      var k = 0
      while (k < 4) {
        val nr = r + dirs(k)._1
        val nc = c + dirs(k)._2
        if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
            grid(nr)(nc) != '#' && !visited(nr)(nc)) {
          visited(nr)(nc) = true
          dist(nr)(nc) = d + 1
          deque.addLast((nr, nc))
        }
        k += 1
      }

      // Portal teleportation (zero cost)
      val ch = grid(r)(c)
      if (ch >= 'A' && ch <= 'Z') {
        val idx = ch - 'A'
        if (!usedPortal(idx)) {
          usedPortal(idx) = true
          val list = portals(idx)
          var i = 0
          while (i < list.length) {
            val (pr, pc) = list(i)
            if (!visited(pr)(pc)) {
              visited(pr)(pc) = true
              dist(pr)(pc) = d
              deque.addFirst((pr, pc))
            }
            i += 1
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
    pub fn min_moves(matrix: Vec<String>) -> i32 {
        let m = matrix.len();
        if m == 0 {
            return -1;
        }
        let n = matrix[0].len();
        let grid: Vec<Vec<u8>> = matrix.iter().map(|s| s.as_bytes().to_vec()).collect();

        // collect portal positions
        let mut portals: Vec<Vec<usize>> = vec![Vec::new(); 26];
        for r in 0..m {
            for c in 0..n {
                let ch = grid[r][c];
                if (b'A'..=b'Z').contains(&ch) {
                    portals[(ch - b'A') as usize].push(r * n + c);
                }
            }
        }

        let mut visited = vec![false; m * n];
        let mut portal_used = vec![false; 26];
        let mut deque: VecDeque<(usize, usize, i32)> = VecDeque::new();

        visited[0] = true;
        deque.push_back((0, 0, 0));

        while let Some((r, c, d)) = deque.pop_front() {
            if r == m - 1 && c == n - 1 {
                return d;
            }

            // move to adjacent cells (cost 1)
            const DIRS: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];
            for &(dr, dc) in &DIRS {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                    continue;
                }
                let ur = nr as usize;
                let uc = nc as usize;
                let idx = ur * n + uc;
                if !visited[idx] && grid[ur][uc] != b'#' {
                    visited[idx] = true;
                    deque.push_back((ur, uc, d + 1));
                }
            }

            // teleport via portal (cost 0)
            let ch = grid[r][c];
            if (b'A'..=b'Z').contains(&ch) {
                let pi = (ch - b'A') as usize;
                if !portal_used[pi] {
                    portal_used[pi] = true;
                    for &pos in portals[pi].iter() {
                        if !visited[pos] {
                            visited[pos] = true;
                            let pr = pos / n;
                            let pc = pos % n;
                            deque.push_front((pr, pc, d));
                        }
                    }
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
#lang racket
(require data/queue)

(define/contract (min-moves matrix)
  (-> (listof string?) exact-integer?)
  (let* ([m (length matrix)]
         [n (if (= m 0) 0 (string-length (first matrix)))]
         [dist (make-vector m)])
    ;; initialize distance vectors
    (for ([i (in-range m)])
      (vector-set! dist i (make-vector n -1)))
    ;; map portals
    (define portals (make-hash))
    (for ([r (in-range m)])
      (let ([row (list-ref matrix r)])
        (for ([c (in-range n)])
          (let* ([ch (string-ref row c)])
            (when (and (char-alphabetic? ch) (eq? ch (char-upcase ch)))
              (hash-update! portals ch
                            (lambda (lst) (cons (cons r c) lst))
                            '()))))))
    ;; BFS setup
    (define q (make-queue))
    (define (set-dist r c d)
      (vector-set! (vector-ref dist r) c d))
    (define (get-dist r c)
      (vector-ref (vector-ref dist r) c))
    (set-dist 0 0 0)
    (enqueue q (cons 0 0))
    (define used (make-hash))
    (let loop ()
      (if (queue-empty? q)
          -1
          (let* ([pos (dequeue q)]
                 [r (car pos)]
                 [c (cdr pos)]
                 [d (get-dist r c)])
            (if (and (= r (- m 1)) (= c (- n 1)))
                d
                (begin
                  ;; explore adjacent cells
                  (for ([dr '( -1 0 1 0 )] [dc '( 0 1 0 -1 )])
                    (let* ([nr (+ r dr)] [nc (+ c dc)])
                      (when (and (>= nr 0) (< nr m)
                                 (>= nc 0) (< nc n))
                        (let ([cell (string-ref (list-ref matrix nr) nc)])
                          (when (not (char=? cell #\#))
                            (when (= (get-dist nr nc) -1)
                              (set-dist nr nc (+ d 1))
                              (enqueue q (cons nr nc))))))))
                  ;; portal teleportation
                  (let ([ch (string-ref (list-ref matrix r) c)])
                    (when (and (char-alphabetic? ch) (eq? ch (char-upcase ch)))
                      (unless (hash-has-key? used ch)
                        (hash-set! used ch #t)
                        (for ([target (in-list (hash-ref portals ch))])
                          (let* ([tr (car target)] [tc (cdr target)])
                            (when (= (get-dist tr tc) -1)
                              (set-dist tr tc d)
                              (enqueue q (cons tr tc))))))))
                  (loop)))))))))
```

## Erlang

```erlang
-spec min_moves(Matrix :: [unicode:unicode_binary()]) -> integer().
min_moves(Matrix) ->
    RowsTuple = list_to_tuple(Matrix),
    M = tuple_size(RowsTuple),
    N = case M of
            0 -> 0;
            _ -> byte_size(element(1, RowsTuple))
        end,
    PortalsMap = build_portals(RowsTuple, M, N, #{}),
    Visited0 = maps:put({0,0}, true, #{}),
    bfs(0, [{0,0}], [], Visited0, PortalsMap, RowsTuple).

%% Build portals map: Letter -> list of positions
build_portals(RowsTuple, M, N, Acc) ->
    build_rows(0, RowsTuple, M, N, Acc).

build_rows(RowIdx, _RowsTuple, M, _N, Acc) when RowIdx >= M ->
    Acc;
build_rows(RowIdx, RowsTuple, M, N, Acc) ->
    RowBin = element(RowIdx + 1, RowsTuple),
    Acc2 = build_cols(RowIdx, 0, RowBin, N, Acc),
    build_rows(RowIdx + 1, RowsTuple, M, N, Acc2).

build_cols(_RowIdx, ColIdx, _RowBin, N, Acc) when ColIdx >= N ->
    Acc;
build_cols(RowIdx, ColIdx, RowBin, N, Acc) ->
    Char = binary:at(RowBin, ColIdx),
    NewAcc = if
        Char >= $A, Char =< $Z ->
            maps:update_with(Char,
                fun(List) -> [{RowIdx,ColIdx} | List] end,
                [{RowIdx,ColIdx}], Acc);
        true -> Acc
    end,
    build_cols(RowIdx, ColIdx + 1, RowBin, N, NewAcc).

%% BFS with level handling (0-cost teleport stays in same level)
bfs(_Dist, [], [], _Visited, _Portals, _Rows) ->
    -1;
bfs(Dist, [], NextQueue, Visited, Portals, Rows) ->
    bfs(Dist + 1, lists:reverse(NextQueue), [], Visited, Portals, Rows);
bfs(Dist,
    [{R,C}=Pos | Rest],
    NextQueue,
    Visited,
    Portals,
    Rows) ->

    M = tuple_size(Rows),
    N = byte_size(element(1, Rows)),
    case (R == M - 1) andalso (C == N - 1) of
        true -> Dist;
        false ->
            RowBin = element(R + 1, Rows),
            Char = binary:at(RowBin, C),

            %% Handle teleportation if portal not used yet
            {CurrAfterTeleport, PortalsAfterUse, VisitedAfterTeleport} =
                case (Char >= $A) andalso (Char =< $Z) of
                    true ->
                        case maps:is_key(Char, Portals) of
                            true ->
                                Positions = maps:get(Char, Portals),
                                Portals2 = maps:remove(Char, Portals),
                                {TelePosList, Visited2} = add_unvisited_positions(Positions, Visited, []),
                                {TelePosList ++ Rest, Portals2, Visited2};
                            false ->
                                {Rest, Portals, Visited}
                        end;
                    false -> {Rest, Portals, Visited}
                end,

            %% Explore 4-directional moves (cost 1)
            NeighborDirs = [{1,0}, {-1,0}, {0,1}, {0,-1}],
            {NewNextQueue, VisitedAfterNeighbors} =
                add_neighbors(NeighborDirs, R, C, Rows, VisitedAfterTeleport, NextQueue),

            bfs(Dist,
                CurrAfterTeleport,
                NewNextQueue,
                VisitedAfterNeighbors,
                PortalsAfterUse,
                Rows)
    end.

%% Add positions that are not yet visited; return list and updated visited map
add_unvisited_positions([], Visited, Acc) ->
    {lists:reverse(Acc), Visited};
add_unvisited_positions([Pos | Rest], Visited, Acc) ->
    case maps:is_key(Pos, Visited) of
        true -> add_unvisited_positions(Rest, Visited, Acc);
        false ->
            NewVisited = maps:put(Pos, true, Visited),
            add_unvisited_positions(Rest, NewVisited, [Pos | Acc])
    end.

%% Add valid neighbor positions (cost 1) to NextQueue (prepending)
add_neighbors([], _R, _C, _Rows, Visited, Next) ->
    {Next, Visited};
add_neighbors([{DR,DC} | RestDirs], R, C, Rows, Visited, Next) ->
    NR = R + DR,
    NC = C + DC,
    M = tuple_size(Rows),
    N = byte_size(element(1, Rows)),
    if
        NR >= 0, NR < M, NC >= 0, NC < N ->
            RowBin = element(NR + 1, Rows),
            Char = binary:at(RowBin, NC),
            case Char of
                $# -> add_neighbors(RestDirs, R, C, Rows, Visited, Next);
                _ ->
                    Pos = {NR, NC},
                    case maps:is_key(Pos, Visited) of
                        true -> add_neighbors(RestDirs, R, C, Rows, Visited, Next);
                        false ->
                            NewVisited = maps:put(Pos, true, Visited),
                            add_neighbors(RestDirs, R, C, Rows, NewVisited, [Pos | Next])
                    end
            end;
        true ->
            add_neighbors(RestDirs, R, C, Rows, Visited, Next)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves(matrix :: [String.t]) :: integer
  def min_moves(matrix) do
    rows = matrix
    m = length(rows)
    n = byte_size(hd(rows))
    target_idx = (m - 1) * n + (n - 1)

    # Build portal map: letter codepoint => list of flattened indices
    portals =
      Enum.with_index(rows)
      |> Enum.reduce(%{}, fn {row, r}, acc ->
        0..(n - 1)
        |> Enum.reduce(acc, fn c, a ->
          ch = :binary.at(row, c)

          if ?A <= ch and ch <= ?Z do
            Map.update(a, ch, [r * n + c], &[r * n + c | &1])
          else
            a
          end
        end)
      end)

    # Store rows in an Erlang array for O(1) access
    rows_arr = :array.from_list(rows)

    queue = :queue.new() |> :queue.in({0, 0})
    visited = MapSet.new([0])
    used_letters = MapSet.new()

    bfs(queue, visited, used_letters, rows_arr, m, n, target_idx, portals)
  end

  defp bfs(queue, visited, used, rows_arr, m, n, target, portals) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {idx, dist}}, q_rest} ->
        if idx == target do
          dist
        else
          r = div(idx, n)
          c = rem(idx, n)

          # Explore four adjacent cells
          {q_adj, visited_adj} =
            [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]
            |> Enum.reduce({q_rest, visited}, fn {dr, dc}, {q_acc, vis_acc} ->
              nr = r + dr
              nc = c + dc

              if nr >= 0 and nr < m and nc >= 0 and nc < n do
                row_bin = :array.get(nr, rows_arr)
                ch = :binary.at(row_bin, nc)

                if ch != ?# do
                  nid = nr * n + nc

                  if not MapSet.member?(vis_acc, nid) do
                    {
                      :queue.in({nid, dist + 1}, q_acc),
                      MapSet.put(vis_acc, nid)
                    }
                  else
                    {q_acc, vis_acc}
                  end
                else
                  {q_acc, vis_acc}
                end
              else
                {q_acc, vis_acc}
              end
            end)

          # Teleport via portal if applicable
          row_cur = :array.get(r, rows_arr)
          ch_cur = :binary.at(row_cur, c)

          if ?A <= ch_cur and ch_cur <= ?Z and not MapSet.member?(used, ch_cur) do
            portal_idxs = Map.get(portals, ch_cur, [])

            {q_portal, visited_portal} =
              Enum.reduce(portal_idxs, {q_adj, visited_adj}, fn pid, {q_acc, vis_acc} ->
                if not MapSet.member?(vis_acc, pid) do
                  {
                    :queue.in({pid, dist}, q_acc),
                    MapSet.put(vis_acc, pid)
                  }
                else
                  {q_acc, vis_acc}
                end
              end)

            bfs(q_portal, visited_portal, MapSet.put(used, ch_cur), rows_arr, m, n, target, portals)
          else
            bfs(q_adj, visited_adj, used, rows_arr, m, n, target, portals)
          end
        end
    end
  end
end
```

# 2812. Find the Safest Path in a Grid

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> dist(n, vector<int>(n, -1));
        queue<pair<int,int>> q;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0;
                    q.emplace(i, j);
                }
            }
        }
        const int dr[4] = {1,-1,0,0};
        const int dc[4] = {0,0,1,-1};
        while (!q.empty()) {
            auto [r,c] = q.front(); q.pop();
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr<0||nr>=n||nc<0||nc>=n) continue;
                if (dist[nr][nc] != -1) continue;
                dist[nr][nc] = dist[r][c] + 1;
                q.emplace(nr, nc);
            }
        }
        vector<vector<bool>> visited(n, vector<bool>(n,false));
        priority_queue<tuple<int,int,int>> pq; // (safety, r, c)
        pq.emplace(dist[0][0], 0, 0);
        while (!pq.empty()) {
            auto [safety, r, c] = pq.top(); pq.pop();
            if (visited[r][c]) continue;
            visited[r][c] = true;
            if (r == n-1 && c == n-1) return safety;
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr<0||nr>=n||nc<0||nc>=n) continue;
                if (visited[nr][nc]) continue;
                int newSafety = min(safety, dist[nr][nc]);
                pq.emplace(newSafety, nr, nc);
            }
        }
        return 0; // should never reach here
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();
        int[][] dist = new int[n][n];
        for (int[] row : dist) Arrays.fill(row, -1);
        ArrayDeque<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            List<Integer> row = grid.get(i);
            for (int j = 0; j < n; j++) {
                if (row.get(j) == 1) {
                    dist[i][j] = 0;
                    q.offer(new int[]{i, j});
                }
            }
        }
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.offer(new int[]{nr, nc});
                }
            }
        }

        boolean[][] visited = new boolean[n][n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        pq.offer(new int[]{dist[0][0], 0, 0});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int safety = cur[0];
            int r = cur[1];
            int c = cur[2];
            if (visited[r][c]) continue;
            visited[r][c] = true;
            if (r == n - 1 && c == n - 1) {
                return safety;
            }
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    int newSafety = Math.min(safety, dist[nr][nc]);
                    pq.offer(new int[]{newSafety, nr, nc});
                }
            }
        }
        return 0; // Should never reach here as a path always exists
    }
}
```

## Python

```python
import collections, heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # Multi-source BFS to compute distance to nearest thief for each cell
        dist = [[-1] * n for _ in range(n)]
        q = collections.deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.popleft()
            d = dist[x][y]
            nd = d + 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = nd
                    q.append((nx, ny))
        # Max-heap Dijkstra-like search for path maximizing minimal distance
        visited = [[False]*n for _ in range(n)]
        heap = [(-dist[0][0], 0, 0)]  # store negative safety to simulate max-heap
        while heap:
            neg_safety, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            visited[x][y] = True
            cur_safety = -neg_safety
            if x == n-1 and y == n-1:
                return cur_safety
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    next_safety = min(cur_safety, dist[nx][ny])
                    heapq.heappush(heap, (-next_safety, nx, ny))
        return 0  # fallback, though problem guarantees a path exists
```

## Python3

```python
class Solution:
    def maximumSafenessFactor(self, grid):
        from collections import deque
        import heapq

        n = len(grid)
        # Multi-source BFS to compute distance to nearest thief for each cell
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            d = dist[r][c] + 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = d
                    q.append((nr, nc))

        # Max-heap (using negative values) for maximin path search
        visited = [[False]*n for _ in range(n)]
        heap = [(-dist[0][0], 0, 0)]  # store negative safeness to simulate max-heap
        visited[0][0] = True

        while heap:
            neg_safeness, r, c = heapq.heappop(heap)
            cur_safeness = -neg_safeness
            if r == n-1 and c == n-1:
                return cur_safeness
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    next_safeness = min(cur_safeness, dist[nr][nc])
                    heapq.heappush(heap, (-next_safeness, nr, nc))
        return 0  # fallback, though problem guarantees a path exists
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int safety;
    int r;
    int c;
} Node;

static void heapSwap(Node *a, Node *b) {
    Node tmp = *a;
    *a = *b;
    *b = tmp;
}

/* max-heap based on safety */
static void heapPush(Node *heap, int *size, Node val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].safety >= heap[i].safety) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static Node heapPop(Node *heap, int *size) {
    Node top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0, n = *size;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= n) break;
        int best = l;
        if (r < n && heap[r].safety > heap[l].safety) best = r;
        if (heap[i].safety >= heap[best].safety) break;
        heapSwap(&heap[i], &heap[best]);
        i = best;
    }
    return top;
}

int maximumSafenessFactor(int** grid, int gridSize, int* gridColSize){
    int n = gridSize;
    if (n == 0) return 0;

    /* Directions */
    const int dr[4] = {1,-1,0,0};
    const int dc[4] = {0,0,1,-1};

    /* Compute distance from nearest thief using multi-source BFS */
    int **dist = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        dist[i] = (int*)malloc(n * sizeof(int));
        memset(dist[i], -1, n * sizeof(int));
    }

    int total = n * n;
    int *qr = (int*)malloc(total * sizeof(int));
    int *qc = (int*)malloc(total * sizeof(int));
    int qhead = 0, qtail = 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            if (grid[r][c] == 1) { // thief
                dist[r][c] = 0;
                qr[qtail] = r;
                qc[qtail] = c;
                qtail++;
            }
        }
    }

    while (qhead < qtail) {
        int r = qr[qhead];
        int c = qc[qhead];
        qhead++;
        int curd = dist[r][c];
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                dist[nr][nc] = curd + 1;
                qr[qtail] = nr;
                qc[qtail] = nc;
                qtail++;
            }
        }
    }

    free(qr);
    free(qc);

    /* Max-heap Dijkstra-like search for maximum minimum safety */
    int **vis = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        vis[i] = (int*)calloc(n, sizeof(int));
    }

    Node *heap = (Node*)malloc(total * sizeof(Node));
    int heapSize = 0;

    Node start;
    start.r = 0;
    start.c = 0;
    start.safety = dist[0][0];
    heapPush(heap, &heapSize, start);
    vis[0][0] = 1;

    while (heapSize > 0) {
        Node cur = heapPop(heap, &heapSize);
        if (cur.r == n-1 && cur.c == n-1) {
            int ans = cur.safety;
            /* cleanup */
            for (int i = 0; i < n; ++i) free(dist[i]);
            free(dist);
            for (int i = 0; i < n; ++i) free(vis[i]);
            free(vis);
            free(heap);
            return ans;
        }
        for (int k = 0; k < 4; ++k) {
            int nr = cur.r + dr[k];
            int nc = cur.c + dc[k];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && !vis[nr][nc]) {
                vis[nr][nc] = 1;
                Node nxt;
                nxt.r = nr;
                nxt.c = nc;
                int cand = dist[nr][nc];
                nxt.safety = cur.safety < cand ? cur.safety : cand; // min
                heapPush(heap, &heapSize, nxt);
            }
        }
    }

    /* Should never reach here as a path always exists */
    for (int i = 0; i < n; ++i) free(dist[i]);
    free(dist);
    for (int i = 0; i < n; ++i) free(vis[i]);
    free(vis);
    free(heap);
    return 0;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumSafenessFactor(IList<IList<int>> grid) {
        int n = grid.Count;
        int[,] dist = new int[n, n];
        var q = new Queue<(int r, int c)>();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dist[i, j] = 0;
                    q.Enqueue((i, j));
                } else {
                    dist[i, j] = -1;
                }
            }
        }
        
        int[] dr = new int[] { 1, -1, 0, 0 };
        int[] dc = new int[] { 0, 0, 1, -1 };
        
        // Multi-source BFS to compute distance to nearest thief
        while (q.Count > 0) {
            var (r, c) = q.Dequeue();
            foreach (var k in new int[] { 0, 1, 2, 3 }) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr, nc] == -1) {
                    dist[nr, nc] = dist[r, c] + 1;
                    q.Enqueue((nr, nc));
                }
            }
        }
        
        // Dijkstra-like maximin path using a max-heap (implemented via negative priority)
        var visited = new bool[n, n];
        var pq = new PriorityQueue<(int r, int c, int b), int>();
        int startB = dist[0, 0];
        pq.Enqueue((0, 0, startB), -startB);
        
        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            if (visited[cur.r, cur.c]) continue;
            visited[cur.r, cur.c] = true;
            
            if (cur.r == n - 1 && cur.c == n - 1) {
                return cur.b;
            }
            
            foreach (var k in new int[] { 0, 1, 2, 3 }) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr, nc]) {
                    int nb = Math.Min(cur.b, dist[nr, nc]);
                    pq.Enqueue((nr, nc, nb), -nb);
                }
            }
        }
        
        return 0;
    }
}
```

## Javascript

```javascript
function maximumSafenessFactor(grid) {
    const n = grid.length;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    // Multi-source BFS to compute distance to nearest thief
    const dist = Array.from({length: n}, () => new Int32Array(n).fill(-1));
    const qx = new Int32Array(n * n);
    const qy = new Int32Array(n * n);
    let head = 0, tail = 0;
    
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) {
                dist[i][j] = 0;
                qx[tail] = i;
                qy[tail] = j;
                tail++;
            }
        }
    }
    
    while (head < tail) {
        const x = qx[head];
        const y = qy[head];
        head++;
        const d = dist[x][y] + 1;
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] === -1) {
                dist[nx][ny] = d;
                qx[tail] = nx;
                qy[tail] = ny;
                tail++;
            }
        }
    }
    
    // Find max distance value for binary search upper bound
    let maxDist = 0;
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (dist[i][j] > maxDist) maxDist = dist[i][j];
        }
    }
    
    // Helper to check feasibility of a given safety value
    const canReach = (safety) => {
        if (dist[0][0] < safety || dist[n-1][n-1] < safety) return false;
        const visited = Array.from({length: n}, () => new Uint8Array(n));
        let h = 0, t = 0;
        const vx = new Int32Array(n * n);
        const vy = new Int32Array(n * n);
        vx[t] = 0; vy[t] = 0; t++;
        visited[0][0] = 1;
        while (h < t) {
            const x = vx[h];
            const y = vy[h];
            h++;
            if (x === n-1 && y === n-1) return true;
            for (const [dx, dy] of dirs) {
                const nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < n && ny >= 0 && ny < n &&
                    !visited[nx][ny] && dist[nx][ny] >= safety) {
                    visited[nx][ny] = 1;
                    vx[t] = nx; vy[t] = ny; t++;
                }
            }
        }
        return false;
    };
    
    // Binary search for maximum safety factor
    let lo = 0, hi = maxDist, ans = 0;
    while (lo <= hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (canReach(mid)) {
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return ans;
}
```

## Typescript

```typescript
function maximumSafenessFactor(grid: number[][]): number {
    const n = grid.length;
    const dist: number[][] = Array.from({ length: n }, () => Array(n).fill(-1));
    const q: [number, number][] = [];
    // Initialize BFS with all thieves
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                dist[i][j] = 0;
                q.push([i, j]);
            }
        }
    }
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    // Multi-source BFS to compute distance to nearest thief
    for (let head = 0; head < q.length; head++) {
        const [r, c] = q[head];
        const d = dist[r][c];
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] === -1) {
                dist[nr][nc] = d + 1;
                q.push([nr, nc]);
            }
        }
    }

    // Max-heap for Dijkstra-like maximin path
    class MaxHeap {
        data: number[][] = [];
        push(item: number[]) {
            const d = this.data;
            d.push(item);
            let i = d.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (d[p][0] >= d[i][0]) break;
                [d[p], d[i]] = [d[i], d[p]];
                i = p;
            }
        }
        pop(): number[] | undefined {
            const d = this.data;
            if (d.length === 0) return undefined;
            const top = d[0];
            const last = d.pop()!;
            if (d.length > 0) {
                d[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = l + 1;
                    let largest = i;
                    if (l < d.length && d[l][0] > d[largest][0]) largest = l;
                    if (r < d.length && d[r][0] > d[largest][0]) largest = r;
                    if (largest === i) break;
                    [d[i], d[largest]] = [d[largest], d[i]];
                    i = largest;
                }
            }
            return top;
        }
        size(): number {
            return this.data.length;
        }
    }

    const visited: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    const heap = new MaxHeap();
    heap.push([dist[0][0], 0, 0]);

    while (heap.size() > 0) {
        const cur = heap.pop()!;
        const safety = cur[0];
        const r = cur[1];
        const c = cur[2];
        if (visited[r][c]) continue;
        visited[r][c] = true;
        if (r === n - 1 && c === n - 1) {
            return safety;
        }
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                const newSafety = Math.min(safety, dist[nr][nc]);
                heap.push([newSafety, nr, nc]);
            }
        }
    }

    return 0; // Should never reach here as a path always exists
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumSafenessFactor($grid) {
        $n = count($grid);
        // distance to nearest thief for each cell
        $dist = array_fill(0, $n, array_fill(0, $n, -1));
        $queue = new SplQueue();

        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] == 1) {
                    $dist[$i][$j] = 0;
                    $queue->enqueue([$i, $j]);
                }
            }
        }

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();
            $curD = $dist[$r][$c];
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n && $dist[$nr][$nc] == -1) {
                    $dist[$nr][$nc] = $curD + 1;
                    $queue->enqueue([$nr, $nc]);
                }
            }
        }

        // Dijkstra-like max‑min path using a max heap
        $best = array_fill(0, $n, array_fill(0, $n, -1));
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $startSafety = $dist[0][0];
        $best[0][0] = $startSafety;
        $pq->insert([0, 0], $startSafety);

        while (!$pq->isEmpty()) {
            $extracted = $pq->extract(); // ['data'=>[r,c],'priority'=>safety]
            [$r, $c] = $extracted['data'];
            $safety = $extracted['priority'];

            if ($r == $n - 1 && $c == $n - 1) {
                return $safety;
            }

            // If we have already found a better safety for this cell, skip
            if ($safety < $best[$r][$c]) {
                continue;
            }

            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n) {
                    $newSafety = min($safety, $dist[$nr][$nc]);
                    if ($newSafety > $best[$nr][$nc]) {
                        $best[$nr][$nc] = $newSafety;
                        $pq->insert([$nr, $nc], $newSafety);
                    }
                }
            }
        }

        return 0; // should not reach here
    }
}
```

## Swift

```swift
class Solution {
    func maximumSafenessFactor(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var dist = Array(repeating: Array(repeating: -1, count: n), count: n)
        var qR = [Int]()
        var qC = [Int]()
        var head = 0
        
        // Initialize BFS with all thieves (cells with value 1)
        for i in 0..<n {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    dist[i][j] = 0
                    qR.append(i)
                    qC.append(j)
                }
            }
        }
        
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        // Multi-source BFS to compute distance to nearest thief for each cell
        while head < qR.count {
            let r = qR[head]
            let c = qC[head]
            head += 1
            let curDist = dist[r][c]
            for d in dirs {
                let nr = r + d.0
                let nc = c + d.1
                if nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1 {
                    dist[nr][nc] = curDist + 1
                    qR.append(nr)
                    qC.append(nc)
                }
            }
        }
        
        // Find maximum distance value to set binary search upper bound
        var maxDist = 0
        for i in 0..<n {
            for j in 0..<n {
                if dist[i][j] > maxDist {
                    maxDist = dist[i][j]
                }
            }
        }
        
        // Helper function to check reachability with minimum safety threshold
        func canReach(_ minSafety: Int) -> Bool {
            if dist[0][0] < minSafety || dist[n-1][n-1] < minSafety { return false }
            var visited = Array(repeating: Array(repeating: false, count: n), count: n)
            var qr = [Int]()
            var qc = [Int]()
            var h = 0
            qr.append(0)
            qc.append(0)
            visited[0][0] = true
            while h < qr.count {
                let r = qr[h]
                let c = qc[h]
                h += 1
                if r == n - 1 && c == n - 1 { return true }
                for d in dirs {
                    let nr = r + d.0
                    let nc = c + d.1
                    if nr >= 0 && nr < n && nc >= 0 && nc < n &&
                        !visited[nr][nc] && dist[nr][nc] >= minSafety {
                        visited[nr][nc] = true
                        qr.append(nr)
                        qc.append(nc)
                    }
                }
            }
            return false
        }
        
        // Binary search for the maximum safeness factor
        var low = 0
        var high = maxDist
        var answer = 0
        while low <= high {
            let mid = (low + high) / 2
            if canReach(mid) {
                answer = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSafenessFactor(grid: List<List<Int>>): Int {
        val n = grid.size
        val dist = Array(n) { IntArray(n) { -1 } }
        val queue: java.util.ArrayDeque<Pair<Int, Int>> = java.util.ArrayDeque()
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0
                    queue.add(Pair(i, j))
                }
            }
        }
        val dirs = intArrayOf(1, 0, -1, 0, 1)
        while (!queue.isEmpty()) {
            val (r, c) = queue.poll()
            val d = dist[r][c]
            for (k in 0 until 4) {
                val nr = r + dirs[k]
                val nc = c + dirs[k + 1]
                if (nr in 0 until n && nc in 0 until n && dist[nr][nc] == -1) {
                    dist[nr][nc] = d + 1
                    queue.add(Pair(nr, nc))
                }
            }
        }

        data class Node(val safety: Int, val r: Int, val c: Int)
        val pq = java.util.PriorityQueue<Node> { a, b -> b.safety - a.safety } // max-heap by safety
        val visited = Array(n) { BooleanArray(n) }
        pq.add(Node(dist[0][0], 0, 0))

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val r = cur.r
            val c = cur.c
            if (visited[r][c]) continue
            visited[r][c] = true
            if (r == n - 1 && c == n - 1) return cur.safety
            for (k in 0 until 4) {
                val nr = r + dirs[k]
                val nc = c + dirs[k + 1]
                if (nr in 0 until n && nc in 0 until n && !visited[nr][nc]) {
                    val newSafety = kotlin.math.min(cur.safety, dist[nr][nc])
                    pq.add(Node(newSafety, nr, nc))
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
import 'dart:math';

class _MaxHeap {
  final List<List<int>> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(List<int> item) {
    _data.add(item);
    _siftUp(_data.length - 1);
  }

  List<int> pop() {
    final top = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_data[parent][0] >= _data[idx][0]) break;
      final tmp = _data[parent];
      _data[parent] = _data[idx];
      _data[idx] = tmp;
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int largest = idx;
      if (left < n && _data[left][0] > _data[largest][0]) largest = left;
      if (right < n && _data[right][0] > _data[largest][0]) largest = right;
      if (largest == idx) break;
      final tmp = _data[idx];
      _data[idx] = _data[largest];
      _data[largest] = tmp;
      idx = largest;
    }
  }
}

class Solution {
  int maximumSafenessFactor(List<List<int>> grid) {
    final n = grid.length;
    const dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    // Multi-source BFS to compute distance to nearest thief
    List<List<int>> dist = List.generate(n, (_) => List.filled(n, -1));
    final queue = ListQueue<List<int>>();
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) {
          dist[i][j] = 0;
          queue.add([i, j]);
        }
      }
    }

    while (queue.isNotEmpty) {
      final cur = queue.removeFirst();
      int r = cur[0], c = cur[1];
      for (var d in dirs) {
        int nr = r + d[0];
        int nc = c + d[1];
        if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
        if (dist[nr][nc] != -1) continue;
        dist[nr][nc] = dist[r][c] + 1;
        queue.add([nr, nc]);
      }
    }

    // Maximin path using a max-heap (modified Dijkstra)
    List<List<int>> best = List.generate(n, (_) => List.filled(n, -1));
    final heap = _MaxHeap();
    best[0][0] = dist[0][0];
    heap.push([best[0][0], 0, 0]);

    while (!heap.isEmpty) {
      final cur = heap.pop();
      int value = cur[0];
      int r = cur[1];
      int c = cur[2];

      if (value < best[r][c]) continue; // outdated entry
      if (r == n - 1 && c == n - 1) return value;

      for (var d in dirs) {
        int nr = r + d[0];
        int nc = c + d[1];
        if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
        int cand = min(value, dist[nr][nc]);
        if (cand > best[nr][nc]) {
          best[nr][nc] = cand;
          heap.push([cand, nr, nc]);
        }
      }
    }

    return 0; // Should never reach here given problem constraints
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type item struct {
	safe int
	r    int
	c    int
}
type maxHeap []item

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i].safe > h[j].safe } // max-heap
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func maximumSafenessFactor(grid [][]int) int {
	n := len(grid)
	if n == 0 {
		return 0
	}
	// distances to nearest thief
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = -1
		}
	}
	type pair struct{ r, c int }
	q := make([]pair, 0)
	// initialize queue with thieves
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				dist[i][j] = 0
				q = append(q, pair{i, j})
			}
		}
	}
	dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	// BFS multi-source
	for head := 0; head < len(q); head++ {
		cur := q[head]
		for _, d := range dir {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1 {
				dist[nr][nc] = dist[cur.r][cur.c] + 1
				q = append(q, pair{nr, nc})
			}
		}
	}
	// Dijkstra-like max-min path using max-heap
	visited := make([][]bool, n)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	h := &maxHeap{}
	heap.Init(h)
	heap.Push(h, item{safe: dist[0][0], r: 0, c: 0})
	visited[0][0] = true
	for h.Len() > 0 {
		it := heap.Pop(h).(item)
		if it.r == n-1 && it.c == n-1 {
			return it.safe
		}
		for _, d := range dir {
			nr, nc := it.r+d[0], it.c+d[1]
			if nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc] {
				newSafe := it.safe
				if dist[nr][nc] < newSafe {
					newSafe = dist[nr][nc]
				}
				heap.Push(h, item{safe: newSafe, r: nr, c: nc})
				visited[nr][nc] = true
			}
		}
	}
	return 0
}
```

## Ruby

```ruby
def feasible?(dist, n, limit)
  return false if dist[0][0] < limit || dist[n - 1][n - 1] < limit

  visited = Array.new(n) { Array.new(n, false) }
  queue = [[0, 0]]
  visited[0][0] = true
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  head = 0

  while head < queue.size
    i, j = queue[head]
    head += 1
    return true if i == n - 1 && j == n - 1

    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      next if ni < 0 || ni >= n || nj < 0 || nj >= n
      next if visited[ni][nj]
      next if dist[ni][nj] < limit

      visited[ni][nj] = true
      queue << [ni, nj]
    end
  end

  false
end

# @param {Integer[][]} grid
# @return {Integer}
def maximum_safeness_factor(grid)
  n = grid.size
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  # Multi-source BFS to compute distance from nearest thief
  dist = Array.new(n) { Array.new(n, -1) }
  queue = []
  (0...n).each do |i|
    (0...n).each do |j|
      if grid[i][j] == 1
        dist[i][j] = 0
        queue << [i, j]
      end
    end
  end

  head = 0
  while head < queue.size
    i, j = queue[head]
    head += 1
    d = dist[i][j]

    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      next if ni < 0 || ni >= n || nj < 0 || nj >= n
      if dist[ni][nj] == -1
        dist[ni][nj] = d + 1
        queue << [ni, nj]
      end
    end
  end

  max_dist = 0
  (0...n).each do |i|
    (0...n).each do |j|
      max_dist = dist[i][j] if dist[i][j] > max_dist
    end
  end

  low = 0
  high = max_dist
  answer = 0

  while low <= high
    mid = (low + high) / 2
    if feasible?(dist, n, mid)
      answer = mid
      low = mid + 1
    else
      high = mid - 1
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
  def maximumSafenessFactor(grid: List[List[Int]]): Int = {
    val n = grid.length
    val dist = Array.ofDim[Int](n, n)
    for (i <- 0 until n; j <- 0 until n) dist(i)(j) = -1

    val bfs = new java.util.ArrayDeque[(Int, Int)]()
    for (i <- 0 until n; j <- 0 until n) {
      if (grid(i)(j) == 1) {
        dist(i)(j) = 0
        bfs.add((i, j))
      }
    }

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (!bfs.isEmpty) {
      val (r, c) = bfs.poll()
      val d = dist(r)(c)
      var k = 0
      while (k < 4) {
        val nr = r + dirs(k)._1
        val nc = c + dirs(k)._2
        if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist(nr)(nc) == -1) {
          dist(nr)(nc) = d + 1
          bfs.add((nr, nc))
        }
        k += 1
      }
    }

    case class Node(d: Int, r: Int, c: Int)
    implicit val ord: Ordering[Node] = Ordering.by[Node, Int](_.d)

    val pq = scala.collection.mutable.PriorityQueue.empty[Node]
    val visited = Array.ofDim[Boolean](n, n)

    pq.enqueue(Node(dist(0)(0), 0, 0))

    while (pq.nonEmpty) {
      val cur = pq.dequeue()
      if (!visited(cur.r)(cur.c)) {
        visited(cur.r)(cur.c) = true
        if (cur.r == n - 1 && cur.c == n - 1) return cur.d
        var k = 0
        while (k < 4) {
          val nr = cur.r + dirs(k)._1
          val nc = cur.c + dirs(k)._2
          if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited(nr)(nc)) {
            val nd = math.min(cur.d, dist(nr)(nc))
            pq.enqueue(Node(nd, nr, nc))
          }
          k += 1
        }
      }
    }

    0
  }
}
```

## Rust

```rust
use std::collections::{VecDeque, BinaryHeap};

impl Solution {
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 0 {
            return 0;
        }
        // Step 1: multi-source BFS to compute distance to nearest thief
        let mut dist = vec![vec![-1i32; n]; n];
        let mut q = VecDeque::new();
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 1 {
                    dist[i][j] = 0;
                    q.push_back((i, j));
                }
            }
        }
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        while let Some((r, c)) = q.pop_front() {
            let cur_d = dist[r][c];
            for &(dr, dc) in &dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < n as i32 && nc >= 0 && nc < n as i32 {
                    let (ur, uc) = (nr as usize, nc as usize);
                    if dist[ur][uc] == -1 {
                        dist[ur][uc] = cur_d + 1;
                        q.push_back((ur, uc));
                    }
                }
            }
        }

        // Step 2: Dijkstra-like maximin path using max-heap
        let mut heap = BinaryHeap::new();
        let start_safety = dist[0][0];
        heap.push((start_safety, 0usize, 0usize));
        let mut visited = vec![vec![false; n]; n];

        while let Some((safety, r, c)) = heap.pop() {
            if visited[r][c] {
                continue;
            }
            visited[r][c] = true;
            if r == n - 1 && c == n - 1 {
                return safety;
            }
            for &(dr, dc) in &dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < n as i32 && nc >= 0 && nc < n as i32 {
                    let (ur, uc) = (nr as usize, nc as usize);
                    if !visited[ur][uc] {
                        let new_safety = std::cmp::min(safety, dist[ur][uc]);
                        heap.push((new_safety, ur, uc));
                    }
                }
            }
        }

        0
    }
}
```

## Racket

```racket
(require data/heap)

(define (maximum-safeness-factor grid)
  (define n (length grid))
  ;; convert to vectors for O(1) indexing
  (define gvec (list->vector (map list->vector grid)))
  ;; distance matrix, -1 = unvisited
  (define dist (make-vector n))
  (for ([i (in-range n)])
    (vector-set! dist i (make-vector n -1)))
  ;; queue for multi‑source BFS
  (define total (* n n))
  (define q (make-vector total))
  (define front 0)
  (define back 0)
  ;; directions
  (define dr #(1 -1 0 0))
  (define dc #(0 0 1 -1))
  ;; initialize queue with all thieves
  (for ([r (in-range n)])
    (for ([c (in-range n)])
      (when (= (vector-ref (vector-ref gvec r) c) 1)
        (vector-set! (vector-ref dist r) c 0)
        (vector-set! q back (cons r c))
        (set! back (+ back 1)))))
  ;; BFS to compute minimum distance to any thief
  (let loop ()
    (when (< front back)
      (define rc (vector-ref q front))
      (define r (car rc))
      (define c (cdr rc))
      (set! front (+ front 1))
      (define curd (vector-ref (vector-ref dist r) c))
      (for ([k (in-range 4)])
        (define nr (+ r (vector-ref dr k)))
        (define nc (+ c (vector-ref dc k)))
        (when (and (>= nr 0) (< nr n)
                   (>= nc 0) (< nc n)
                   (= (vector-ref (vector-ref dist nr) nc) -1))
          (vector-set! (vector-ref dist nr) nc (+ curd 1))
          (vector-set! q back (cons nr nc))
          (set! back (+ back 1))))
      (loop)))
  ;; max‑heap for Dijkstra‑like search (store [safeness r c])
  (define heap (make-heap (lambda (a b) (> (first a) (first b)))))
  (define start-dist (vector-ref (vector-ref dist 0) 0))
  (heap-insert! heap (list start-dist 0 0))
  ;; visited matrix
  (define visited (make-vector n))
  (for ([i (in-range n)])
    (vector-set! visited i (make-vector n #f)))
  ;; search for path maximizing minimal distance
  (let search ()
    (if (heap-empty? heap)
        -1
        (let* ((node (heap-extract-min! heap))
               (safeness (first node))
               (r (second node))
               (c (third node)))
          (when (not (vector-ref (vector-ref visited r) c))
            (vector-set! (vector-ref visited r) c #t)
            (if (and (= r (- n 1)) (= c (- n 1)))
                safeness
                (begin
                  (for ([k (in-range 4)])
                    (define nr (+ r (vector-ref dr k)))
                    (define nc (+ c (vector-ref dc k)))
                    (when (and (>= nr 0) (< nr n)
                               (>= nc 0) (< nc n)
                               (not (vector-ref (vector-ref visited nr) nc)))
                      (define nd (min safeness
                                      (vector-ref (vector-ref dist nr) nc)))
                      (heap-insert! heap (list nd nr nc))))
                  (search)))))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_safeness_factor/1]).

-include_lib("kernel/include/logger.hrl").

-spec maximum_safeness_factor(Grid :: [[integer()]]) -> integer().
maximum_safeness_factor(Grid) ->
    N = length(Grid),
    % collect thief positions
    Thieves =
        lists:foldl(
          fun({Row, RIdx}, Acc) ->
                  lists:foldl(
                    fun({Val, CIdx}, A2) ->
                            case Val of
                                1 -> [{RIdx, CIdx} | A2];
                                _ -> A2
                            end
                    end,
                    Acc,
                    lists:zip(Row, lists:seq(0, N - 1))
                  )
          end,
          [],
          lists:zip(Grid, lists:seq(0, N - 1))
        ),
    % multi‑source BFS to compute distance to nearest thief
    {DistMap, MaxDist} = bfs_dist(N, Thieves),
    % binary search on answer
    binary_search(0, MaxDist, 0, DistMap, N).

%% BFS from all thieves, returns map of distances and maximal distance found
bfs_dist(N, Thieves) ->
    Queue0 = queue:new(),
    {Queue1, DistMap0, InitMax} =
        lists:foldl(
          fun({R, C}, {Q, M, CurMax}) ->
                  Q2 = queue:in({R, C, 0}, Q),
                  M2 = maps:put({R, C}, 0, M),
                  {Q2, M2, max(CurMax, 0)}
          end,
          {Queue0, #{}, 0},
          Thieves
        ),
    bfs_dist_loop(N, Queue1, DistMap0, InitMax).

bfs_dist_loop(N, Queue, DistMap, CurMax) ->
    case queue:out(Queue) of
        {{value, {R, C, D}}, RestQ} ->
            Neigh = [{R-1,C},{R+1,C},{R,C-1},{R,C+1}],
            {NewQ, NewMap, NewMax} =
                lists:foldl(
                  fun({NR, NC}, {QAcc, MAcc, MaxAcc}) ->
                          if NR >= 0, NR < N, NC >= 0, NC < N,
                             not maps:is_key({NR,NC}, MAcc) ->
                                 ND = D + 1,
                                 Q2 = queue:in({NR, NC, ND}, QAcc),
                                 M2 = maps:put({NR,NC}, ND, MAcc),
                                 {Q2, M2, max(MaxAcc, ND)};
                             true -> {QAcc, MAcc, MaxAcc}
                          end
                  end,
                  {RestQ, DistMap, CurMax},
                  Neigh),
            bfs_dist_loop(N, NewQ, NewMap, NewMax);
        empty ->
            {DistMap, CurMax}
    end.

%% binary search for maximal feasible safeness factor
binary_search(Low, High, Ans, DistMap, N) when Low =< High ->
    Mid = (Low + High) div 2,
    case can_reach(Mid, DistMap, N) of
        true -> binary_search(Mid + 1, High, Mid, DistMap, N);
        false -> binary_search(Low, Mid - 1, Ans, DistMap, N)
    end;
binary_search(_, _, Ans, _, _) ->
    Ans.

%% check if a path exists using only cells with distance >= Threshold
can_reach(Threshold, DistMap, N) ->
    case {maps:get({0,0}, DistMap), maps:get({N-1,N-1}, DistMap)} of
        {DStart, DEnd} when DStart >= Threshold, DEnd >= Threshold ->
            bfs_path(N, DistMap, Threshold);
        _ -> false
    end.

%% BFS on grid respecting the threshold
bfs_path(N, DistMap, Th) ->
    Vis0 = maps:put({0,0}, true, #{}),
    Q0 = queue:new(),
    Q1 = queue:in({0,0}, Q0),
    bfs_path_loop(N, DistMap, Th, Q1, Vis0).

bfs_path_loop(N, DistMap, Th, Queue, Visited) ->
    case queue:out(Queue) of
        {{value, {R, C}}, RestQ} ->
            if R =:= N-1, C =:= N-1 -> true;
               true ->
                Neigh = [{R-1,C},{R+1,C},{R,C-1},{R,C+1}],
                {NewQ, NewVis} =
                    lists:foldl(
                      fun({NR, NC}, {QAcc, VAcc}) ->
                              if NR >= 0, NR < N, NC >= 0, NC < N,
                                 maps:get({NR,NC}, DistMap) >= Th,
                                 not maps:is_key({NR,NC}, VAcc) ->
                                      Q2 = queue:in({NR,NC}, QAcc),
                                      V2 = maps:put({NR,NC}, true, VAcc),
                                      {Q2, V2};
                                 true -> {QAcc, VAcc}
                              end
                      end,
                      {RestQ, Visited},
                      Neigh),
                bfs_path_loop(N, DistMap, Th, NewQ, NewVis)
            end;
        empty -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_safeness_factor(grid :: [[integer]]) :: integer
  def maximum_safeness_factor(grid) do
    n = length(grid)
    dist_map = compute_distances(grid, n)

    max_dist = Enum.max(Map.values(dist_map))

    {answer, _} =
      binary_search(0, max_dist, 0, dist_map, n)

    answer
  end

  # Compute distance from each cell to the nearest thief using multi-source BFS
  defp compute_distances(grid, n) do
    thieves =
      for {row, r} <- Enum.with_index(grid),
          {val, c} <- Enum.with_index(row),
          val == 1,
          do: {r, c}

    initial_queue = :queue.from_list(thieves)

    initial_map =
      Enum.reduce(thieves, %{}, fn pos, acc -> Map.put(acc, pos, 0) end)

    bfs_fill(initial_queue, initial_map, n)
  end

  defp bfs_fill(queue, dist_map, n) do
    case :queue.out(queue) do
      {:empty, _} ->
        dist_map

      {{:value, {r, c}}, q_rest} ->
        cur = Map.get(dist_map, {r, c})

        {new_queue, new_dist_map} =
          Enum.reduce([{-1, 0}, {1, 0}, {0, -1}, {0, 1}], {q_rest, dist_map},
            fn {dr, dc}, {q_acc, map_acc} ->
              nr = r + dr
              nc = c + dc

              if nr >= 0 and nr < n and nc >= 0 and nc < n do
                key = {nr, nc}

                if Map.has_key?(map_acc, key) do
                  {q_acc, map_acc}
                else
                  {
                    :queue.in(key, q_acc),
                    Map.put(map_acc, key, cur + 1)
                  }
                end
              else
                {q_acc, map_acc}
              end
            end)

        bfs_fill(new_queue, new_dist_map, n)
    end
  end

  # Binary search over possible safeness factors
  defp binary_search(low, high, best, dist_map, n) do
    if low > high do
      {best, nil}
    else
      mid = div(low + high, 2)

      if reachable?(dist_map, n, mid) do
        binary_search(mid + 1, high, mid, dist_map, n)
      else
        binary_search(low, mid - 1, best, dist_map, n)
      end
    end
  end

  # Check if a path exists using only cells with distance >= min_safeness
  defp reachable?(dist_map, n, min_safeness) do
    start = {0, 0}
    dest = {n - 1, n - 1}

    cond do
      Map.get(dist_map, start, -1) < min_safeness ->
        false

      Map.get(dist_map, dest, -1) < min_safeness ->
        false

      true ->
        bfs_reach(:queue.in(start, :queue.new()), MapSet.new([start]), dist_map, n, min_safeness, dest)
    end
  end

  defp bfs_reach(queue, visited, dist_map, n, min_safeness, dest) do
    case :queue.out(queue) do
      {:empty, _} ->
        false

      {{:value, {r, c}}, q_rest} ->
        if {r, c} == dest do
          true
        else
          {new_queue, new_visited} =
            Enum.reduce([{-1, 0}, {1, 0}, {0, -1}, {0, 1}], {q_rest, visited},
              fn {dr, dc}, {q_acc, set_acc} ->
                nr = r + dr
                nc = c + dc

                if nr >= 0 and nr < n and nc >= 0 and nc < n do
                  key = {nr, nc}

                  cond do
                    Map.get(dist_map, key, -1) >= min_safeness and not MapSet.member?(set_acc, key) ->
                      {
                        :queue.in(key, q_acc),
                        MapSet.put(set_acc, key)
                      }

                    true ->
                      {q_acc, set_acc}
                  end
                else
                  {q_acc, set_acc}
                end
              end)

          bfs_reach(new_queue, new_visited, dist_map, n, min_safeness, dest)
        end
    end
  end
end
```

# 2577. Minimum Time to Visit a Cell In a Grid

## Cpp

```cpp
class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        // If both initial moves are impossible, return -1
        if (grid[0][1] > 1 && grid[1][0] > 1) return -1;
        
        const long long INF = 4e18;
        vector<vector<long long>> dist(m, vector<long long>(n, INF));
        using T = tuple<long long,int,int>;
        priority_queue<T, vector<T>, greater<T>> pq;
        dist[0][0] = 0;
        pq.emplace(0LL, 0, 0);
        
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.empty()) {
            auto [t, x, y] = pq.top(); pq.pop();
            if (t != dist[x][y]) continue;
            if (x == m-1 && y == n-1) return (int)t;
            for (auto &d : dirs) {
                int nx = x + d[0];
                int ny = y + d[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                long long nt = max<long long>(grid[nx][ny], t + 1);
                // Adjust for parity: we can only increase time by multiples of 2 while staying in current cell
                if ((nt - (t + 1)) % 2 == 1) ++nt;
                if (nt < dist[nx][ny]) {
                    dist[nx][ny] = nt;
                    pq.emplace(nt, nx, ny);
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
    public int minimumTime(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // If we cannot move from the start at time 1, impossible.
        if (m > 1 && n > 1 && grid[0][1] > 1 && grid[1][0] > 1) {
            return -1;
        }

        boolean[][] visited = new boolean[m][n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        // each entry: {time, row, col}
        pq.offer(new int[]{grid[0][0], 0, 0});

        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int time = cur[0];
            int r = cur[1];
            int c = cur[2];

            if (visited[r][c]) continue;
            visited[r][c] = true;

            if (r == m - 1 && c == n - 1) {
                return time;
            }

            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;

                int need = grid[nr][nc];
                int nextTime = Math.max(time + 1, need);
                // Adjust parity: we can only increase time by even amounts beyond 'need'
                if ((nextTime - need) % 2 == 1) {
                    nextTime++;
                }
                pq.offer(new int[]{nextTime, nr, nc});
            }
        }

        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        # If both possible first moves are blocked at time 1, impossible.
        right_blocked = n > 1 and grid[0][1] > 1
        down_blocked = m > 1 and grid[1][0] > 1
        if right_blocked and down_blocked:
            return -1

        INF = 10**18
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (time, row, col)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            t, r, c = heapq.heappop(pq)
            if t != dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    need = grid[nr][nc]
                    nxt = max(t + 1, need)
                    # adjust parity: can only add even increments to t+1
                    if (nxt - (t + 1)) & 1:
                        nxt += 1
                    if nxt < dist[nr][nc]:
                        dist[nr][nc] = nxt
                        heapq.heappush(pq, (nxt, nr, nc))
        return -1
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # If both immediate moves are impossible at time 1, no path exists.
        if (n > 1 and grid[0][1] > 1) and (m > 1 and grid[1][0] > 1):
            return -1

        visited = [[False] * n for _ in range(m)]
        heap = [(0, 0, 0)]  # (time, row, col)

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            t, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True

            if r == m - 1 and c == n - 1:
                return t

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    req = grid[nr][nc]
                    nt = max(t + 1, req)
                    # Adjust parity: need same parity as required time.
                    if (nt - req) & 1:
                        nt += 1
                    heapq.heappush(heap, (nt, nr, nc))

        return -1
```

## C

```c
#include <stdlib.h>

typedef struct {
    int t;
    int r;
    int c;
} Node;

static void heapSwap(Node *a, Node *b) {
    Node tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(Node *heap, int *size, Node val) {
    int i = ++(*size);
    heap[i] = val;
    while (i > 1 && heap[i].t < heap[i >> 1].t) {
        heapSwap(&heap[i], &heap[i >> 1]);
        i >>= 1;
    }
}

static Node heapPop(Node *heap, int *size) {
    Node top = heap[1];
    heap[1] = heap[(*size)--];
    int i = 1;
    while (1) {
        int l = i << 1, r = l + 1, smallest = i;
        if (l <= *size && heap[l].t < heap[smallest].t) smallest = l;
        if (r <= *size && heap[r].t < heap[smallest].t) smallest = r;
        if (smallest == i) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

int minimumTime(int** grid, int gridSize, int* gridColSize){
    int rows = gridSize;
    int cols = gridColSize[0];
    if (rows == 1 && cols == 1) return 0;

    int total = rows * cols;
    char *vis = (char*)calloc(total, sizeof(char));
    Node *heap = (Node*)malloc(sizeof(Node) * (total + 5));
    int heapSize = 0;

    heapPush(heap, &heapSize, (Node){0, 0, 0});

    const int dr[4] = {1,-1,0,0};
    const int dc[4] = {0,0,1,-1};

    while (heapSize) {
        Node cur = heapPop(heap, &heapSize);
        int idx = cur.r * cols + cur.c;
        if (vis[idx]) continue;
        vis[idx] = 1;
        if (cur.r == rows - 1 && cur.c == cols - 1) {
            free(vis);
            free(heap);
            return cur.t;
        }
        for (int k = 0; k < 4; ++k) {
            int nr = cur.r + dr[k];
            int nc = cur.c + dc[k];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            int nidx = nr * cols + nc;
            if (vis[nidx]) continue;

            int need = grid[nr][nc];
            int nt = cur.t + 1;               // move directly
            if (nt < need) {
                nt = need;
                if ((nt - cur.t) % 2 == 0) nt++;   // make difference odd
            } else {
                if ((nt - cur.t) % 2 == 0) nt++;   // ensure odd increment
            }
            heapPush(heap, &heapSize, (Node){nt, nr, nc});
        }
    }

    free(vis);
    free(heap);
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumTime(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        
        // Initial feasibility check
        if (grid[0][1] > 1 && grid[1][0] > 1) return -1;
        
        bool[,] visited = new bool[m, n];
        var pq = new PriorityQueue<(int r, int c, int t), int>();
        pq.Enqueue((0, 0, 0), 0);
        
        int[] dr = new int[] { 1, -1, 0, 0 };
        int[] dc = new int[] { 0, 0, 1, -1 };
        
        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int r = cur.r;
            int c = cur.c;
            int t = cur.t;
            
            if (visited[r, c]) continue;
            visited[r, c] = true;
            
            if (r == m - 1 && c == n - 1) return t;
            
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (visited[nr, nc]) continue;
                
                int nd = Math.Max(t + 1, grid[nr][nc]);
                if ((nd - t) % 2 == 0) nd++; // adjust for parity
                pq.Enqueue((nr, nc, nd), nd);
            }
        }
        
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumTime = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    // If we cannot move to either right or down at time 1, impossible.
    if (grid[0][1] > 1 && grid[1][0] > 1) return -1;

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    const visited = Array.from({length: m}, () => Array(n).fill(false));

    class MinHeap {
        constructor() { this.heap = []; }
        push(item) {
            this.heap.push(item);
            this._up(this.heap.length - 1);
        }
        _up(idx) {
            while (idx > 0) {
                const p = (idx - 1) >> 1;
                if (this.heap[p][0] <= this.heap[idx][0]) break;
                [this.heap[p], this.heap[idx]] = [this.heap[idx], this.heap[p]];
                idx = p;
            }
        }
        pop() {
            if (!this.heap.length) return null;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length) {
                this.heap[0] = end;
                this._down(0);
            }
            return top;
        }
        _down(idx) {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
        isEmpty() { return this.heap.length === 0; }
    }

    const pq = new MinHeap();
    pq.push([0, 0, 0]); // time, row, col

    while (!pq.isEmpty()) {
        const [time, r, c] = pq.pop();
        if (visited[r][c]) continue;
        visited[r][c] = true;
        if (r === m - 1 && c === n - 1) return time;

        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;
            const need = grid[nr][nc];
            let arrive = Math.max(time + 1, need);
            // Adjust parity: we can only wait in steps of 2.
            if ((arrive - need) % 2 === 1) arrive += 1;
            pq.push([arrive, nr, nc]);
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minimumTime(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    if (m === 1 && n === 1) return 0;

    // If both immediate moves are blocked at time 1, impossible.
    const rightBlocked = n > 1 && grid[0][1] > 1;
    const downBlocked = m > 1 && grid[1][0] > 1;
    if (rightBlocked && downBlocked) return -1;

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));

    class MinHeap {
        heap: [number, number, number][] = [];
        push(item: [number, number, number]): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        pop(): [number, number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.sinkDown(0);
            }
            return top;
        }
        sinkDown(idx: number): void {
            const len = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < len && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < len && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
        isEmpty(): boolean {
            return this.heap.length === 0;
        }
    }

    const pq = new MinHeap();
    pq.push([0, 0, 0]); // time, row, col

    while (!pq.isEmpty()) {
        const cur = pq.pop()!;
        const [time, r, c] = cur;
        if (visited[r][c]) continue;
        visited[r][c] = true;
        if (r === m - 1 && c === n - 1) return time;

        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;

            let arrive = Math.max(grid[nr][nc], time + 1);
            // If arrival parity matches the cell's required time, we need to wait an extra second.
            if ((arrive - grid[nr][nc]) % 2 === 0) {
                arrive++;
            }
            pq.push([arrive, nr, nc]);
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumTime($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        // If both initial moves are blocked, impossible to start.
        if ($m > 1 && $n > 1 && $grid[0][1] > 1 && $grid[1][0] > 1) {
            return -1;
        }

        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $pq = new SplPriorityQueue();
        // Extract only the data (no priority)
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        // start at (0,0) with time 0
        $pq->insert(['r' => 0, 'c' => 0, 't' => 0], 0); // priority = -time (0)

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$pq->isEmpty()) {
            $node = $pq->extract();
            $r = $node['r'];
            $c = $node['c'];
            $t = $node['t'];

            if ($visited[$r][$c]) continue;
            $visited[$r][$c] = true;

            if ($r == $m - 1 && $c == $n - 1) {
                return $t;
            }

            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                if ($visited[$nr][$nc]) continue;

                $need = $grid[$nr][$nc];
                // Minimum time to move one step
                $next = max($t + 1, $need);
                // Ensure the difference (next - t) is odd; otherwise add 1 second.
                if ((($next - $t) & 1) == 0) {
                    $next++;
                }
                $pq->insert(['r' => $nr, 'c' => $nc, 't' => $next], -$next);
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTime(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        if m == 1 && n == 1 { return 0 }
        // initial impossibility check
        if grid[0][1] > 1 && grid[1][0] > 1 {
            return -1
        }
        
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        let heap = MinHeap()
        heap.push(Node(time: 0, r: 0, c: 0))
        let dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while let cur = heap.pop() {
            if visited[cur.r][cur.c] { continue }
            visited[cur.r][cur.c] = true
            if cur.r == m - 1 && cur.c == n - 1 {
                return cur.time
            }
            for (dr, dc) in dirs {
                let nr = cur.r + dr
                let nc = cur.c + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                if visited[nr][nc] { continue }
                let need = grid[nr][nc]
                var nextTime = max(cur.time + 1, need)
                if (nextTime - need) % 2 == 1 {
                    nextTime += 1
                }
                heap.push(Node(time: nextTime, r: nr, c: nc))
            }
        }
        return -1
    }
}

// Helper structures for the min-heap
private struct Node {
    var time: Int
    var r: Int
    var c: Int
}

private final class MinHeap {
    private var heap: [Node] = []
    
    func isEmpty() -> Bool { heap.isEmpty }
    
    func push(_ node: Node) {
        heap.append(node)
        siftUp(heap.count - 1)
    }
    
    func pop() -> Node? {
        guard !heap.isEmpty else { return nil }
        let top = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            siftDown(0)
        }
        return top
    }
    
    private func siftUp(_ index: Int) {
        var childIdx = index
        while childIdx > 0 {
            let parentIdx = (childIdx - 1) >> 1
            if heap[childIdx].time < heap[parentIdx].time {
                heap.swapAt(childIdx, parentIdx)
                childIdx = parentIdx
            } else {
                break
            }
        }
    }
    
    private func siftDown(_ index: Int) {
        var parentIdx = index
        while true {
            let leftIdx = (parentIdx << 1) + 1
            let rightIdx = leftIdx + 1
            var smallestIdx = parentIdx
            
            if leftIdx < heap.count && heap[leftIdx].time < heap[smallestIdx].time {
                smallestIdx = leftIdx
            }
            if rightIdx < heap.count && heap[rightIdx].time < heap[smallestIdx].time {
                smallestIdx = rightIdx
            }
            if smallestIdx == parentIdx { break }
            heap.swapAt(parentIdx, smallestIdx)
            parentIdx = smallestIdx
        }
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue
import kotlin.math.max

class Solution {
    fun minimumTime(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        if (m == 1 && n == 1) return 0

        // Early impossibility check: cannot leave the start cell
        if (m > 1 && n > 1 && grid[1][0] > 1 && grid[0][1] > 1) {
            return -1
        }

        data class Node(val time: Int, val r: Int, val c: Int)

        val pq = PriorityQueue<Node>(compareBy { it.time })
        val visited = Array(m) { BooleanArray(n) }
        val dr = intArrayOf(-1, 1, 0, 0)
        val dc = intArrayOf(0, 0, -1, 1)

        pq.add(Node(0, 0, 0))

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (visited[cur.r][cur.c]) continue
            visited[cur.r][cur.c] = true

            if (cur.r == m - 1 && cur.c == n - 1) return cur.time

            for (k in 0 until 4) {
                val nr = cur.r + dr[k]
                val nc = cur.c + dc[k]
                if (nr !in 0 until m || nc !in 0 until n || visited[nr][nc]) continue

                var nextTime = max(cur.time + 1, grid[nr][nc])
                // Adjust parity: need odd difference to step exactly when cell opens
                if ((nextTime - grid[nr][nc]) % 2 == 0) {
                    nextTime++
                }
                pq.add(Node(nextTime, nr, nc))
            }
        }

        return -1
    }
}
```

## Dart

```dart
class MinHeap {
  final List<List<int>> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(List<int> item) {
    _data.add(item);
    _siftUp(_data.length - 1);
  }

  List<int> pop() {
    final result = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return result;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_data[parent][0] <= _data[idx][0]) break;
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
      int smallest = idx;
      if (left < n && _data[left][0] < _data[smallest][0]) smallest = left;
      if (right < n && _data[right][0] < _data[smallest][0]) smallest = right;
      if (smallest == idx) break;
      final tmp = _data[idx];
      _data[idx] = _data[smallest];
      _data[smallest] = tmp;
      idx = smallest;
    }
  }
}

class Solution {
  int minimumTime(List<List<int>> grid) {
    final m = grid.length;
    final n = grid[0].length;

    // Check if we can make the first move.
    bool canMove = false;
    if (n > 1 && grid[0][1] <= 1) canMove = true;
    if (m > 1 && grid[1][0] <= 1) canMove = true;
    if (!canMove) return -1;

    final visited = List.generate(m, (_) => List.filled(n, false));
    final heap = MinHeap();
    heap.push([0, 0, 0]); // [time, row, col]

    const dr = [1, -1, 0, 0];
    const dc = [0, 0, 1, -1];

    while (!heap.isEmpty) {
      final cur = heap.pop();
      final time = cur[0];
      final r = cur[1];
      final c = cur[2];

      if (visited[r][c]) continue;
      visited[r][c] = true;

      if (r == m - 1 && c == n - 1) return time;

      for (int k = 0; k < 4; ++k) {
        final nr = r + dr[k];
        final nc = c + dc[k];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
        if (visited[nr][nc]) continue;

        final need = grid[nr][nc];
        int nextTime;
        if (time + 1 >= need) {
          nextTime = time + 1;
        } else {
          // need > time + 1, must wait
          if ((need - time) % 2 == 0) {
            nextTime = need + 1;
          } else {
            nextTime = need;
          }
        }
        heap.push([nextTime, nr, nc]);
      }
    }

    return -1;
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
	t, r, c int
}
type priorityQueue []item

func (pq priorityQueue) Len() int { return len(pq) }
func (pq priorityQueue) Less(i, j int) bool {
	return pq[i].t < pq[j].t
}
func (pq priorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *priorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(item))
}
func (pq *priorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[:n-1]
	return it
}

func minimumTime(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	// early impossibility check
	if grid[0][1] > 1 && grid[1][0] > 1 {
		return -1
	}
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	pq := &priorityQueue{}
	heap.Init(pq)
	heap.Push(pq, item{t: 0, r: 0, c: 0})

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(item)
		if visited[cur.r][cur.c] {
			continue
		}
		visited[cur.r][cur.c] = true
		if cur.r == m-1 && cur.c == n-1 {
			return cur.t
		}
		for _, d := range dir {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc] {
				continue
			}
			nextTime := cur.t + 1
			req := grid[nr][nc]
			if nextTime < req {
				nextTime = req
			}
			if (nextTime%2) != (req%2) {
				nextTime++
			}
			heap.Push(pq, item{t: nextTime, r: nr, c: nc})
		}
	}
	return -1
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(item)
    @data << item
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    min
  end

  def empty?
    @data.empty?
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent][0] <= @data[idx][0]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < size && @data[left][0] < @data[smallest][0]
        smallest = left
      end
      if right < size && @data[right][0] < @data[smallest][0]
        smallest = right
      end
      break if smallest == idx
      @data[smallest], @data[idx] = @data[idx], @data[smallest]
      idx = smallest
    end
  end
end

# @param {Integer[][]} grid
# @return {Integer}
def minimum_time(grid)
  m = grid.size
  n = grid[0].size

  # Early impossibility check
  if grid[0][1] > 1 && grid[1][0] > 1
    return -1
  end

  visited = Array.new(m) { Array.new(n, false) }
  heap = MinHeap.new
  heap.push([0, 0, 0]) # [time, row, col]

  dirs = [[1,0],[-1,0],[0,1],[0,-1]]

  until heap.empty?
    t, r, c = heap.pop
    next if visited[r][c]
    visited[r][c] = true
    return t if r == m - 1 && c == n - 1

    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next unless nr.between?(0, m - 1) && nc.between?(0, n - 1)
      next if visited[nr][nc]

      nt = [t + 1, grid[nr][nc]].max
      # Ensure parity matches (extra waiting can only be in multiples of 2)
      if (nt % 2) != ((t + 1) % 2)
        nt += 1
      end
      heap.push([nt, nr, nc])
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
  import java.util.PriorityQueue

  private case class Node(time: Int, r: Int, c: Int)

  def minimumTime(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    if (m == 1 && n == 1) return 0

    // If both possible first moves are blocked, impossible.
    if (grid(0)(1) > 1 && grid(1)(0) > 1) return -1

    val visited = Array.ofDim[Boolean](m, n)
    val pq = new PriorityQueue[Node]((a: Node, b: Node) => Integer.compare(a.time, b.time))
    pq.offer(Node(0, 0, 0))

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (!pq.isEmpty) {
      val cur = pq.poll()
      val t = cur.time
      val r = cur.r
      val c = cur.c

      if (visited(r)(c)) {
        // already processed
      } else {
        visited(r)(c) = true
        if (r == m - 1 && c == n - 1) return t

        for ((dr, dc) <- dirs) {
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited(nr)(nc)) {
            var nt = Math.max(t + 1, grid(nr)(nc))
            // adjust for parity: need even difference to be able to wait using back‑and‑forth moves
            if ((nt - (t + 1)) % 2 == 1) nt += 1
            pq.offer(Node(nt, nr, nc))
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
use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub struct Solution;

impl Solution {
    pub fn minimum_time(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        // If both immediate moves require more than 1 second, impossible.
        if grid[0][1] > 1 && grid[1][0] > 1 {
            return -1;
        }

        let mut dist = vec![vec![i64::MAX; n]; m];
        let mut heap: BinaryHeap<Reverse<(i64, usize, usize)>> = BinaryHeap::new();

        dist[0][0] = 0;
        heap.push(Reverse((0_i64, 0usize, 0usize)));

        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];

        while let Some(Reverse((t, r, c))) = heap.pop() {
            if t != dist[r][c] {
                continue;
            }
            if r == m - 1 && c == n - 1 {
                return t as i32;
            }

            for (dr, dc) in dirs.iter() {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                    continue;
                }
                let nr_usize = nr as usize;
                let nc_usize = nc as usize;

                let need = grid[nr_usize][nc_usize] as i64;
                let mut nt = t + 1;
                if nt < need {
                    nt = need;
                }
                // Arrival time must have opposite parity to current time.
                if (nt % 2) == (t % 2) {
                    nt += 1;
                }

                if nt < dist[nr_usize][nc_usize] {
                    dist[nr_usize][nc_usize] = nt;
                    heap.push(Reverse((nt, nr_usize, nc_usize)));
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
(require data/heap
         racket/list)

(define/contract (minimum-time grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length grid)]
         [n (if (zero? m) 0 (length (first grid)))]
         [visited (make-vector m)])
    ;; initialize visited matrix
    (for ([i (in-range m)])
      (vector-set! visited i (make-vector n #f)))
    ;; priority queue ordered by smallest time
    (define heap (make-heap (lambda (a b) (< (first a) (first b)))))
    (heap-add! heap (list 0 0 0)) ; (time row col)

    (let loop ()
      (if (= (heap-count heap) 0)
          -1
          (let* ([item (heap-min heap)]
                 [time (first item)]
                 [r (second item)]
                 [c (third item)])
            (heap-remove-min! heap)
            (cond
              [(vector-ref (vector-ref visited r) c) (loop)]
              [(and (= r (- m 1)) (= c (- n 1))) time]
              [else
               (vector-set! (vector-ref visited r) c #t)
               (for ([dr (list -1 0 1 0)]
                     [dc (list 0 1 0 -1)])
                 (let* ([nr (+ r dr)] [nc (+ c dc)])
                   (when (and (>= nr 0) (< nr m) (>= nc 0) (< nc n))
                     (unless (vector-ref (vector-ref visited nr) nc)
                       (define base (+ time 1))
                       (define need (list-ref (list-ref grid nr) nc))
                       (define t (max base need))
                       (when (= (modulo (- t base) 2) 1)
                         (set! t (+ t 1)))
                       (heap-add! heap (list t nr nc))))))
               (loop)]))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_time/1]).

-define(INF, 1000000000000). % sufficiently large

minimum_time(Grid) ->
    Rows = length(Grid),
    Cols = length(hd(Grid)),
    %% Convert grid to tuple of tuples for O(1) access
    GridTuples = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    GetVal = fun(R, C) -> element(C + 1, element(R + 1, GridTuples)) end,
    %% Early impossibility check
    case {Rows > 1, Cols > 1} of
        {true, true} ->
            GRight = GetVal(0, 1),
            GDown  = GetVal(1, 0),
            if GRight > 1 andalso GDown > 1 -> -1;
               true -> dijkstra(Rows, Cols, GetVal)
            end;
        _ -> -1
    end.

dijkstra(Rows, Cols, GetVal) ->
    StartSet = gb_sets:add_element({0, 0, 0}, gb_sets:new()),
    Visited = #{},
    Dist = maps:put({0,0}, 0, #{}),
    loop(StartSet, Visited, Dist, Rows, Cols, GetVal).

loop(Set, Visited, _Dist, Rows, Cols, _GetVal) when gb_sets:is_empty(Set) ->
    -1;
loop(Set, Visited, Dist, Rows, Cols, GetVal) ->
    {{Time, R, C}, SetRest} = gb_sets:take_smallest(Set),
    case maps:get({R,C}, Visited, false) of
        true ->
            loop(SetRest, Visited, Dist, Rows, Cols, GetVal);
        false ->
            %% reached target?
            if R == Rows-1 andalso C == Cols-1 ->
                    Time;
               true ->
                    Visited2 = maps:put({R,C}, true, Visited),
                    {SetNew, DistNew} = process_neighbors(R, C, Time,
                                                         SetRest, Dist, Visited2,
                                                         Rows, Cols, GetVal),
                    loop(SetNew, Visited2, DistNew, Rows, Cols, GetVal)
            end
    end.

process_neighbors(_R, _C, _Time, Set, Dist, _Visited,
                  _Rows, _Cols, _GetVal) ->
    {Set, Dist}. % placeholder for empty neighbor list (should never be called)

process_neighbors(R, C, Time, Set, Dist, Visited,
                  Rows, Cols, GetVal) ->
    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
    lists:foldl(fun({DR,DC}, {AccSet, AccDist}) ->
        NR = R + DR,
        NC = C + DC,
        if NR < 0 orelse NR >= Rows orelse NC < 0 orelse NC >= Cols ->
                {AccSet, AccDist};
           true ->
                case maps:get({NR,NC}, Visited, false) of
                    true -> {AccSet, AccDist};
                    false ->
                        G = GetVal(NR, NC),
                        CurPlus1 = Time + 1,
                        Next0 = if CurPlus1 >= G -> CurPlus1; true -> G end,
                        NeededParity = CurPlus1 rem 2,
                        Next = if (Next0 rem 2) == NeededParity -> Next0;
                                  true -> Next0 + 1
                               end,
                        PrevDist = maps:get({NR,NC}, AccDist, ?INF),
                        if Next < PrevDist ->
                                NewDist = maps:put({NR,NC}, Next, AccDist),
                                NewSet = gb_sets:add_element({Next, NR, NC}, AccSet),
                                {NewSet, NewDist};
                           true -> {AccSet, AccDist}
                        end
                end
        end
    end, {Set, Dist}, Directions).

% Helper to get value from the tuple grid (captured in closure)
-get_val(R, C) ->
    element(C + 1, element(R + 1, GridTuples)).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time(grid :: [[integer]]) :: integer
  def minimum_time(grid) do
    rows = length(grid)
    cols = length(hd(grid))

    # early impossibility check
    if Enum.at(Enum.at(grid, 0), 1) > 1 and Enum.at(Enum.at(grid, 1), 0) > 1 do
      -1
    else
      total = rows * cols
      visited = :array.new(total, default: false)
      start_tree = push(:gb_trees.empty(), 0, {0, 0})
      dijkstra(grid, rows, cols, start_tree, visited)
    end
  end

  @dirs [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

  defp dijkstra(_grid, _rows, _cols, tree, _visited) when :gb_trees.is_empty(tree), do: -1

  defp dijkstra(grid, rows, cols, tree, visited) do
    {time, pos_list, rest_tree} = :gb_trees.take_smallest(tree)

    {new_tree, new_visited, result} =
      Enum.reduce(pos_list, {rest_tree, visited, nil}, fn {r, c},
                                                          {t_acc, v_acc, res} ->
        if res != nil do
          {t_acc, v_acc, res}
        else
          idx = r * cols + c

          if :array.get(idx, v_acc) do
            {t_acc, v_acc, nil}
          else
            v_acc = :array.set(idx, true, v_acc)

            if r == rows - 1 and c == cols - 1 do
              {t_acc, v_acc, time}
            else
              t_acc2 =
                Enum.reduce(@dirs, t_acc, fn {dr, dc}, acc ->
                  nr = r + dr
                  nc = c + dc

                  if nr < 0 or nr >= rows or nc < 0 or nc >= cols do
                    acc
                  else
                    nidx = nr * cols + nc

                    if :array.get(nidx, v_acc) do
                      acc
                    else
                      g = Enum.at(Enum.at(grid, nr), nc)
                      nt = arrival_time(time, g)
                      push(acc, nt, {nr, nc})
                    end
                  end
                end)

              {t_acc2, v_acc, nil}
            end
          end
        end
      end)

    case result do
      nil -> dijkstra(grid, rows, cols, new_tree, new_visited)
      _ -> result
    end
  end

  defp arrival_time(cur, g) do
    base = cur + 1

    if base >= g do
      base
    else
      diff = g - base

      if rem(diff, 2) == 0 do
        base + diff
      else
        base + diff + 1
      end
    end
  end

  defp push(tree, time, pos) do
    case :gb_trees.lookup(time, tree) do
      :none -> :gb_trees.insert(time, [pos], tree)
      {:value, list} -> :gb_trees.update(time, [pos | list], tree)
    end
  end
end
```

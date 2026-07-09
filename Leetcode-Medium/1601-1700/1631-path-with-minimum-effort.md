# 1631. Path With Minimum Effort

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int n = heights.size();
        int m = heights[0].size();
        const int INF = INT_MAX;
        vector<vector<int>> dist(n, vector<int>(m, INF));
        using T = tuple<int,int,int>; // effort, row, col
        priority_queue<T, vector<T>, greater<T>> pq;
        dist[0][0] = 0;
        pq.emplace(0, 0, 0);
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.empty()) {
            auto [eff, r, c] = pq.top();
            pq.pop();
            if (eff != dist[r][c]) continue;
            if (r == n - 1 && c == m - 1) return eff;
            for (auto &d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                int nd = max(eff, abs(heights[nr][nc] - heights[r][c]));
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    pq.emplace(nd, nr, nc);
                }
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
    public int minimumEffortPath(int[][] heights) {
        int rows = heights.length;
        int cols = heights[0].length;
        int[][] effort = new int[rows][cols];
        for (int[] row : effort) Arrays.fill(row, Integer.MAX_VALUE);
        effort[0][0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        pq.offer(new int[]{0, 0, 0}); // row, col, current effort

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int r = cur[0], c = cur[1], curEffort = cur[2];

            if (r == rows - 1 && c == cols - 1) return curEffort;
            if (curEffort > effort[r][c]) continue;

            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                int edge = Math.abs(heights[nr][nc] - heights[r][c]);
                int nextEffort = Math.max(curEffort, edge);
                if (nextEffort < effort[nr][nc]) {
                    effort[nr][nc] = nextEffort;
                    pq.offer(new int[]{nr, nc, nextEffort});
                }
            }
        }

        return 0; // unreachable case (should not happen with given constraints)
    }
}
```

## Python

```python
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        from collections import deque

        m, n = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can(limit):
            visited = [[False] * n for _ in range(m)]
            dq = deque()
            dq.append((0, 0))
            visited[0][0] = True
            while dq:
                x, y = dq.popleft()
                if x == m - 1 and y == n - 1:
                    return True
                cur_h = heights[x][y]
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if abs(cur_h - heights[nx][ny]) <= limit:
                            visited[nx][ny] = True
                            dq.append((nx, ny))
            return False

        low = 0
        high = max(max(row) for row in heights) - min(min(row) for row in heights)
        while low < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (effort, x, y)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            effort, x, y = heapq.heappop(heap)
            if (x, y) == (rows - 1, cols - 1):
                return effort
            if effort != dist[x][y]:
                continue
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    cur = abs(heights[nx][ny] - heights[x][y])
                    new_effort = max(effort, cur)
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(heap, (new_effort, nx, ny))
        return 0
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static bool canReach(int **heights, int rows, int cols, int limit) {
    int total = rows * cols;
    char *vis = (char *)calloc(total, 1);
    if (!vis) return false;
    int *qr = (int *)malloc(total * sizeof(int));
    int *qc = (int *)malloc(total * sizeof(int));
    if (!qr || !qc) {
        free(vis);
        free(qr);
        free(qc);
        return false;
    }

    const int dr[4] = {1, -1, 0, 0};
    const int dc[4] = {0, 0, 1, -1};

    int front = 0, rear = 0;
    vis[0] = 1;
    qr[rear] = 0;
    qc[rear] = 0;
    rear++;

    while (front < rear) {
        int r = qr[front];
        int c = qc[front];
        front++;
        if (r == rows - 1 && c == cols - 1) {
            free(vis);
            free(qr);
            free(qc);
            return true;
        }
        int curH = heights[r][c];
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            int idx = nr * cols + nc;
            if (vis[idx]) continue;
            int diff = curH > heights[nr][nc] ? curH - heights[nr][nc] : heights[nr][nc] - curH;
            if (diff <= limit) {
                vis[idx] = 1;
                qr[rear] = nr;
                qc[rear] = nc;
                rear++;
            }
        }
    }

    free(vis);
    free(qr);
    free(qc);
    return false;
}

int minimumEffortPath(int** heights, int heightsSize, int* heightsColSize) {
    int rows = heightsSize;
    int cols = heightsColSize[0];
    if (rows == 1 && cols == 1) return 0;

    int maxDiff = 0;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (i + 1 < rows) {
                int d = heights[i][j] > heights[i + 1][j] ? heights[i][j] - heights[i + 1][j]
                                                         : heights[i + 1][j] - heights[i][j];
                if (d > maxDiff) maxDiff = d;
            }
            if (j + 1 < cols) {
                int d = heights[i][j] > heights[i][j + 1] ? heights[i][j] - heights[i][j + 1]
                                                         : heights[i][j + 1] - heights[i][j];
                if (d > maxDiff) maxDiff = d;
            }
        }
    }

    int low = 0, high = maxDiff;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (canReach(heights, rows, cols, mid))
            high = mid;
        else
            low = mid + 1;
    }
    return low;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    public int MinimumEffortPath(int[][] heights)
    {
        int rows = heights.Length;
        int cols = heights[0].Length;
        int[,] dist = new int[rows, cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                dist[i, j] = int.MaxValue;

        var pq = new PriorityQueue<(int r, int c), int>();
        dist[0, 0] = 0;
        pq.Enqueue((0, 0), 0);

        int[] dr = { 1, -1, 0, 0 };
        int[] dc = { 0, 0, 1, -1 };

        while (pq.Count > 0)
        {
            var cur = pq.Dequeue();
            int r = cur.r;
            int c = cur.c;
            int curEffort = dist[r, c];

            if (r == rows - 1 && c == cols - 1)
                return curEffort;

            for (int k = 0; k < 4; k++)
            {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;

                int edge = Math.Abs(heights[nr][nc] - heights[r][c]);
                int nextEffort = Math.Max(curEffort, edge);
                if (nextEffort < dist[nr, nc])
                {
                    dist[nr, nc] = nextEffort;
                    pq.Enqueue((nr, nc), nextEffort);
                }
            }
        }

        return 0; // Should never reach here
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} heights
 * @return {number}
 */
var minimumEffortPath = function(heights) {
    const rows = heights.length;
    const cols = heights[0].length;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
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
        size() { return this.heap.length; }
    }
    
    const dist = Array.from({ length: rows }, () => Array(cols).fill(Infinity));
    dist[0][0] = 0;
    const heap = new MinHeap();
    heap.push([0, 0, 0]); // [effort, r, c]
    
    while (heap.size()) {
        const [effort, r, c] = heap.pop();
        if (r === rows - 1 && c === cols - 1) return effort;
        if (effort > dist[r][c]) continue;
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            const w = Math.abs(heights[nr][nc] - heights[r][c]);
            const newEffort = Math.max(effort, w);
            if (newEffort < dist[nr][nc]) {
                dist[nr][nc] = newEffort;
                heap.push([newEffort, nr, nc]);
            }
        }
    }
    
    return dist[rows - 1][cols - 1];
};
```

## Typescript

```typescript
function minimumEffortPath(heights: number[][]): number {
    const rows = heights.length;
    const cols = heights[0].length;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    class MinHeap {
        heap: [number, number, number][] = [];
        push(item: [number, number, number]): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): [number, number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }
        size(): number {
            return this.heap.length;
        }
        private bubbleUp(idx: number): void {
            const element = this.heap[idx];
            while (idx > 0) {
                const parentIdx = Math.floor((idx - 1) / 2);
                const parent = this.heap[parentIdx];
                if (element[0] >= parent[0]) break;
                this.heap[parentIdx] = element;
                this.heap[idx] = parent;
                idx = parentIdx;
            }
        }
        private bubbleDown(idx: number): void {
            const length = this.heap.length;
            const element = this.heap[idx];
            while (true) {
                let leftIdx = 2 * idx + 1;
                let rightIdx = 2 * idx + 2;
                let swapIdx: number | null = null;

                if (leftIdx < length) {
                    if (this.heap[leftIdx][0] < element[0]) {
                        swapIdx = leftIdx;
                    }
                }
                if (rightIdx < length) {
                    if (
                        (swapIdx === null && this.heap[rightIdx][0] < element[0]) ||
                        (swapIdx !== null && this.heap[rightIdx][0] < this.heap[leftIdx][0])
                    ) {
                        swapIdx = rightIdx;
                    }
                }
                if (swapIdx === null) break;
                this.heap[idx] = this.heap[swapIdx];
                this.heap[swapIdx] = element;
                idx = swapIdx;
            }
        }
    }

    const dist: number[][] = Array.from({ length: rows }, () => Array(cols).fill(Infinity));
    dist[0][0] = 0;
    const heap = new MinHeap();
    heap.push([0, 0, 0]); // [effort, x, y]

    while (heap.size() > 0) {
        const cur = heap.pop()!;
        const effort = cur[0];
        const x = cur[1];
        const y = cur[2];

        if (x === rows - 1 && y === cols - 1) return effort;
        if (effort > dist[x][y]) continue;

        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx < 0 || nx >= rows || ny < 0 || ny >= cols) continue;
            const nextEffort = Math.max(effort, Math.abs(heights[nx][ny] - heights[x][y]));
            if (nextEffort < dist[nx][ny]) {
                dist[nx][ny] = nextEffort;
                heap.push([nextEffort, nx, ny]);
            }
        }
    }

    return dist[rows - 1][cols - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $heights
     * @return Integer
     */
    function minimumEffortPath($heights) {
        $rows = count($heights);
        $cols = count($heights[0]);

        // Determine upper bound for binary search (max possible difference)
        $minVal = PHP_INT_MAX;
        $maxVal = PHP_INT_MIN;
        foreach ($heights as $row) {
            foreach ($row as $v) {
                if ($v < $minVal) $minVal = $v;
                if ($v > $maxVal) $maxVal = $v;
            }
        }
        $low = 0;
        $high = $maxVal - $minVal; // inclusive upper bound

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canReach($mid, $heights, $rows, $cols)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }

    private function canReach($limit, $heights, $rows, $cols) {
        $queue = new SplQueue();
        $queue->enqueue([0, 0]);
        $visited = array_fill(0, $rows, array_fill(0, $cols, false));
        $visited[0][0] = true;

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();
            if ($r == $rows - 1 && $c == $cols - 1) {
                return true;
            }
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $rows || $nc < 0 || $nc >= $cols) continue;
                if ($visited[$nr][$nc]) continue;
                $diff = abs($heights[$nr][$nc] - $heights[$r][$c]);
                if ($diff <= $limit) {
                    $visited[$nr][$nc] = true;
                    $queue->enqueue([$nr, $nc]);
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
    func minimumEffortPath(_ heights: [[Int]]) -> Int {
        let rows = heights.count
        let cols = heights[0].count
        var dist = Array(repeating: Array(repeating: Int.max, count: cols), count: rows)
        var heap = MinHeap()
        dist[0][0] = 0
        heap.push(Node(effort: 0, r: 0, c: 0))
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while let cur = heap.pop() {
            if cur.r == rows - 1 && cur.c == cols - 1 {
                return cur.effort
            }
            if cur.effort > dist[cur.r][cur.c] { continue }
            for d in dirs {
                let nr = cur.r + d.0
                let nc = cur.c + d.1
                if nr < 0 || nr >= rows || nc < 0 || nc >= cols { continue }
                let diff = abs(heights[nr][nc] - heights[cur.r][cur.c])
                let nextEffort = max(cur.effort, diff)
                if nextEffort < dist[nr][nc] {
                    dist[nr][nc] = nextEffort
                    heap.push(Node(effort: nextEffort, r: nr, c: nc))
                }
            }
        }
        return 0
    }
}

struct Node {
    var effort: Int
    var r: Int
    var c: Int
}

struct MinHeap {
    private var data: [Node] = []
    
    mutating func push(_ node: Node) {
        data.append(node)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Node? {
        guard !data.isEmpty else { return nil }
        if data.count == 1 {
            return data.removeLast()
        }
        let top = data[0]
        data[0] = data.removeLast()
        siftDown(0)
        return top
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[child].effort < data[parent].effort {
                data.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < data.count && data[left].effort < data[smallest].effort {
                smallest = left
            }
            if right < data.count && data[right].effort < data[smallest].effort {
                smallest = right
            }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumEffortPath(heights: Array<IntArray>): Int {
        val rows = heights.size
        val cols = heights[0].size
        if (rows == 1 && cols == 1) return 0

        data class Node(val r: Int, val c: Int, val effort: Int)

        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        val effort = Array(rows) { IntArray(cols) { Int.MAX_VALUE } }
        effort[0][0] = 0

        val pq = java.util.PriorityQueue<Node>(compareBy { it.effort })
        pq.add(Node(0, 0, 0))

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.r == rows - 1 && cur.c == cols - 1) return cur.effort
            if (cur.effort != effort[cur.r][cur.c]) continue

            for (d in dirs) {
                val nr = cur.r + d[0]
                val nc = cur.c + d[1]
                if (nr in 0 until rows && nc in 0 until cols) {
                    val diff = kotlin.math.abs(heights[nr][nc] - heights[cur.r][cur.c])
                    val nextEffort = maxOf(cur.effort, diff)
                    if (nextEffort < effort[nr][nc]) {
                        effort[nr][nc] = nextEffort
                        pq.add(Node(nr, nc, nextEffort))
                    }
                }
            }
        }
        return 0
    }
}
```

## Dart

```dart
class Solution {
  int minimumEffortPath(List<List<int>> heights) {
    final rows = heights.length;
    final cols = heights[0].length;

    // Upper bound for effort: maximum difference between any adjacent cells
    int high = 0;
    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        if (i + 1 < rows) {
          high = max(high, (heights[i][j] - heights[i + 1][j]).abs());
        }
        if (j + 1 < cols) {
          high = max(high, (heights[i][j] - heights[i][j + 1]).abs());
        }
      }
    }

    bool canReach(int limit) {
      final visited = List.generate(rows, (_) => List.filled(cols, false));
      final queue = List<int>.filled(rows * cols, 0);
      int head = 0, tail = 0;
      queue[tail++] = 0; // encode (0,0)
      visited[0][0] = true;

      const dr = [1, -1, 0, 0];
      const dc = [0, 0, 1, -1];

      while (head < tail) {
        final code = queue[head++];
        final r = code ~/ cols;
        final c = code % cols;
        if (r == rows - 1 && c == cols - 1) return true;

        for (int d = 0; d < 4; ++d) {
          final nr = r + dr[d];
          final nc = c + dc[d];
          if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
          if (visited[nr][nc]) continue;
          if ((heights[r][c] - heights[nr][nc]).abs() <= limit) {
            visited[nr][nc] = true;
            queue[tail++] = nr * cols + nc;
          }
        }
      }
      return false;
    }

    int low = 0;
    while (low < high) {
      final mid = (low + high) >> 1;
      if (canReach(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func minimumEffortPath(heights [][]int) int {
    n := len(heights)
    m := len(heights[0])

    can := func(limit int) bool {
        visited := make([][]bool, n)
        for i := range visited {
            visited[i] = make([]bool, m)
        }
        dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
        q := make([]int, 0, n*m)
        q = append(q, 0)
        visited[0][0] = true

        for head := 0; head < len(q); head++ {
            idx := q[head]
            r, c := idx/m, idx%m
            if r == n-1 && c == m-1 {
                return true
            }
            curH := heights[r][c]
            for _, d := range dirs {
                nr, nc := r+d[0], c+d[1]
                if nr < 0 || nr >= n || nc < 0 || nc >= m || visited[nr][nc] {
                    continue
                }
                diff := curH - heights[nr][nc]
                if diff < 0 {
                    diff = -diff
                }
                if diff <= limit {
                    visited[nr][nc] = true
                    q = append(q, nr*m+nc)
                }
            }
        }
        return false
    }

    low, high := 0, 1000000
    for low < high {
        mid := (low + high) / 2
        if can(mid) {
            high = mid
        } else {
            low = mid + 1
        }
    }
    return low
}
```

## Ruby

```ruby
def minimum_effort_path(heights)
  rows = heights.size
  cols = heights[0].size

  # maximum possible effort among all adjacent cells
  max_diff = 0
  (0...rows).each do |i|
    (0...cols).each do |j|
      if i + 1 < rows
        d = (heights[i][j] - heights[i + 1][j]).abs
        max_diff = d if d > max_diff
      end
      if j + 1 < cols
        d = (heights[i][j] - heights[i][j + 1]).abs
        max_diff = d if d > max_diff
      end
    end
  end

  dirs = [[1,0],[-1,0],[0,1],[0,-1]]

  reachable = lambda do |limit|
    visited = Array.new(rows) { Array.new(cols, false) }
    queue = [[0, 0]]
    visited[0][0] = true
    idx = 0

    while idx < queue.size
      r, c = queue[idx]
      idx += 1
      return true if r == rows - 1 && c == cols - 1

      dirs.each do |dr, dc|
        nr = r + dr
        nc = c + dc
        next unless nr.between?(0, rows - 1) && nc.between?(0, cols - 1)
        next if visited[nr][nc]
        diff = (heights[r][c] - heights[nr][nc]).abs
        if diff <= limit
          visited[nr][nc] = true
          queue << [nr, nc]
        end
      end
    end

    false
  end

  low = 0
  high = max_diff
  while low < high
    mid = (low + high) / 2
    if reachable.call(mid)
      high = mid
    else
      low = mid + 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
  import java.util.{PriorityQueue, Comparator}
  case class Node(e: Int, x: Int, y: Int)

  def minimumEffortPath(heights: Array[Array[Int]]): Int = {
    val rows = heights.length
    val cols = heights(0).length
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    val effort = Array.fill(rows, cols)(Int.MaxValue)
    effort(0)(0) = 0

    val cmp = new Comparator[Node] {
      override def compare(a: Node, b: Node): Int = Integer.compare(a.e, b.e)
    }
    val pq = new PriorityQueue[Node](cmp)
    pq.offer(Node(0, 0, 0))

    while (!pq.isEmpty) {
      val cur = pq.poll()
      val e = cur.e
      val x = cur.x
      val y = cur.y

      if (x == rows - 1 && y == cols - 1) return e
      if (e != effort(x)(y)) {
        // outdated entry, skip
      } else {
        for ((dx, dy) <- dirs) {
          val nx = x + dx
          val ny = y + dy
          if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
            val diff = Math.abs(heights(x)(y) - heights(nx)(ny))
            val ne = Math.max(e, diff)
            if (ne < effort(nx)(ny)) {
              effort(nx)(ny) = ne
              pq.offer(Node(ne, nx, ny))
            }
          }
        }
      }
    }
    0
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let n = heights.len();
        let m = heights[0].len();
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        let mut dist = vec![vec![i32::MAX; m]; n];
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;
        let mut heap = BinaryHeap::new();
        dist[0][0] = 0;
        heap.push((Reverse(0_i32), 0usize, 0usize));
        while let Some((Reverse(cost), x, y)) = heap.pop() {
            if cost > dist[x][y] {
                continue;
            }
            if x == n - 1 && y == m - 1 {
                return cost;
            }
            for &(dx, dy) in &dirs {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx >= 0 && (nx as usize) < n && ny >= 0 && (ny as usize) < m {
                    let nxu = nx as usize;
                    let nyu = ny as usize;
                    let edge = (heights[x][y] - heights[nxu][nyu]).abs();
                    let next_cost = if cost > edge { cost } else { edge };
                    if next_cost < dist[nxu][nyu] {
                        dist[nxu][nyu] = next_cost;
                        heap.push((Reverse(next_cost), nxu, nyu));
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
(define/contract (minimum-effort-path heights)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length heights))
         (cols (if (zero? rows) 0 (length (first heights))))
         (hv (list->vector (map list->vector heights)))
         (max-diff 1000000))
    (define (in-bounds r c)
      (and (>= r 0) (< r rows) (>= c 0) (< c cols)))
    (define (reachable? k)
      (let* ((visited (for/vector ([i rows]) (make-vector cols #f)))
             (queue (list (cons 0 0))))
        (vector-set! (vector-ref visited 0) 0 #t)
        (let bfs ((q queue))
          (cond
            [(null? q) #f]
            [else
              (define pos (car q))
              (define rest (cdr q))
              (define r (car pos))
              (define c (cdr pos))
              (if (and (= r (- rows 1)) (= c (- cols 1)))
                  #t
                  (let* ((curr-h (vector-ref (vector-ref hv r) c))
                         (neighbors (list (cons (+ r 1) c)
                                          (cons (- r 1) c)
                                          (cons r (+ c 1))
                                          (cons r (- c 1)))))
                    (define new-q rest)
                    (for ([nb neighbors])
                      (define nr (car nb))
                      (define nc (cdr nb))
                      (when (in-bounds nr nc)
                        (unless (vector-ref (vector-ref visited nr) nc)
                          (let ((nh (vector-ref (vector-ref hv nr) nc)))
                            (when (<= (abs (- curr-h nh)) k)
                              (vector-set! (vector-ref visited nr) nc #t)
                              (set! new-q (cons nb new-q)))))))
                    (bfs new-q)))]))))
    (let loop ((low 0) (high max-diff))
      (if (= low high)
          low
          (let ((mid (quotient (+ low high) 2)))
            (if (reachable? mid)
                (loop low mid)
                (loop (+ mid 1) high)))))))
```

## Erlang

```erlang
-spec minimum_effort_path(Heights :: [[integer()]]) -> integer().
minimum_effort_path(Heights) ->
    HeightRows = [list_to_tuple(Row) || Row <- Heights],
    Matrix = list_to_tuple(HeightRows),
    Rows = tuple_size(Matrix),
    Cols = case HeightRows of
               [] -> 0;
               [First|_] -> tuple_size(First)
           end,
    MaxDiff = 1000000,
    binary_search(Matrix, Rows, Cols, 0, MaxDiff).

binary_search(_, _, _, Low, High) when Low >= High ->
    Low;
binary_search(Matrix, Rows, Cols, Low, High) ->
    Mid = (Low + High) div 2,
    case can_reach(Matrix, Rows, Cols, Mid) of
        true -> binary_search(Matrix, Rows, Cols, Low, Mid);
        false -> binary_search(Matrix, Rows, Cols, Mid + 1, High)
    end.

can_reach(Matrix, Rows, Cols, Limit) ->
    Start = {0,0},
    Target = {Rows - 1, Cols - 1},
    bfs(Matrix, Rows, Cols, Limit, [Start], maps:put(Start, true, #{}), Target).

bfs(_, _, _, _, [], _, _) ->
    false;
bfs(Matrix, Rows, Cols, Limit, [{R,C}|QueueTail], Visited, Target) ->
    case {R,C} of
        T when T =:= Target -> true;
        _ ->
            CurrVal = get_val(Matrix, R, C),
            Neigh = neighbors(R, C, Rows, Cols),
            {NewQueue, NewVisited} =
                lists:foldl(
                    fun({Nr,Nc}, {QAcc,VAcc}) ->
                        case maps:is_key({Nr,Nc}, VAcc) of
                            true -> {QAcc, VAcc};
                            false ->
                                NextVal = get_val(Matrix, Nr, Nc),
                                Diff = abs(CurrVal - NextVal),
                                if Diff =< Limit ->
                                        {[{Nr,Nc}|QAcc], maps:put({Nr,Nc}, true, VAcc)};
                                   true -> {QAcc, VAcc}
                                end
                        end
                    end,
                    {QueueTail, Visited},
                    Neigh),
            bfs(Matrix, Rows, Cols, Limit, NewQueue, NewVisited, Target)
    end.

neighbors(R, C, Rows, Cols) ->
    Up = if R > 0 -> [{R-1, C}] else [] end,
    Down = if R < Rows - 1 -> [{R+1, C}] else [] end,
    Left = if C > 0 -> [{R, C-1}] else [] end,
    Right = if C < Cols - 1 -> [{R, C+1}] else [] end,
    Up ++ Down ++ Left ++ Right.

get_val(Matrix, R, C) ->
    RowTuple = element(R + 1, Matrix),
    element(C + 1, RowTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_effort_path(heights :: [[integer]]) :: integer
  def minimum_effort_path(heights) do
    rows = length(heights)
    cols = length(hd(heights))

    max_h = heights |> List.flatten() |> Enum.max()
    min_h = heights |> List.flatten() |> Enum.min()
    low = 0
    high = max_h - min_h

    binary_search(heights, rows, cols, low, high)
  end

  defp binary_search(_heights, _rows, _cols, low, high) when low == high, do: low

  defp binary_search(heights, rows, cols, low, high) do
    mid = div(low + high, 2)

    if reachable?(heights, rows, cols, mid) do
      binary_search(heights, rows, cols, low, mid)
    else
      binary_search(heights, rows, cols, mid + 1, high)
    end
  end

  defp reachable?(heights, rows, cols, limit) do
    target = {rows - 1, cols - 1}
    start_idx = 0
    visited = MapSet.new([start_idx])
    queue = :queue.from_list([{0, 0}])

    bfs(queue, heights, rows, cols, limit, visited, target)
  end

  defp bfs(queue, _heights, _rows, _cols, _limit, _visited, {tr, tc}) do
    case :queue.out(queue) do
      {:empty, _} ->
        false

      {{:value, {r, c}}, q2} ->
        if r == tr and c == tc do
          true
        else
          cur_val = get_val(_heights, r, c)

          dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

          {new_queue, new_visited} =
            Enum.reduce(dirs, {q2, _visited}, fn {dr, dc},
                                                {q_acc, vis_acc} ->
              nr = r + dr
              nc = c + dc

              if nr < 0 or nr >= _rows or nc < 0 or nc >= _cols do
                {q_acc, vis_acc}
              else
                idx = nr * _cols + nc

                if MapSet.member?(vis_acc, idx) do
                  {q_acc, vis_acc}
                else
                  nb_val = get_val(_heights, nr, nc)
                  diff = abs(cur_val - nb_val)

                  if diff <= _limit do
                    {
                      :queue.in({nr, nc}, q_acc),
                      MapSet.put(vis_acc, idx)
                    }
                  else
                    {q_acc, vis_acc}
                  end
                end
              end
            end)

          bfs(new_queue, _heights, _rows, _cols, _limit, new_visited, {tr,
               tc})
        end
    end
  end

  defp get_val(heights, r, c) do
    heights |> Enum.at(r) |> Enum.at(c)
  end
end
```

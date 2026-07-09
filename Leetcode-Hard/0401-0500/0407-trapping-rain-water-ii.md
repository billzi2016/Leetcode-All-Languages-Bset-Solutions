# 0407. Trapping Rain Water II

## Cpp

```cpp
class Solution {
public:
    struct Cell {
        int h, x, y;
        bool operator>(const Cell& other) const { return h > other.h; }
    };
    
    int trapRainWater(vector<vector<int>>& heightMap) {
        int m = heightMap.size();
        if (m == 0) return 0;
        int n = heightMap[0].size();
        if (m < 3 || n < 3) return 0;
        
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        priority_queue<Cell, vector<Cell>, greater<Cell>> pq;
        
        // push boundary cells
        for (int i = 0; i < m; ++i) {
            pq.push({heightMap[i][0], i, 0});
            visited[i][0] = true;
            pq.push({heightMap[i][n-1], i, n-1});
            visited[i][n-1] = true;
        }
        for (int j = 1; j < n-1; ++j) {
            pq.push({heightMap[0][j], 0, j});
            visited[0][j] = true;
            pq.push({heightMap[m-1][j], m-1, j});
            visited[m-1][j] = true;
        }
        
        const int dirs[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
        long long water = 0;
        
        while (!pq.empty()) {
            Cell cur = pq.top(); pq.pop();
            for (auto& d : dirs) {
                int nx = cur.x + d[0];
                int ny = cur.y + d[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n || visited[nx][ny]) continue;
                visited[nx][ny] = true;
                int nh = heightMap[nx][ny];
                if (cur.h > nh) water += cur.h - nh;
                pq.push({max(cur.h, nh), nx, ny});
            }
        }
        return (int)water;
    }
};
```

## Java

```java
class Solution {
    private static class Cell implements Comparable<Cell> {
        int height;
        int row;
        int col;
        Cell(int h, int r, int c) {
            this.height = h;
            this.row = r;
            this.col = c;
        }
        public int compareTo(Cell other) {
            return Integer.compare(this.height, other.height);
        }
    }

    public int trapRainWater(int[][] heightMap) {
        if (heightMap == null || heightMap.length == 0 || heightMap[0].length == 0) {
            return 0;
        }
        int m = heightMap.length;
        int n = heightMap[0].length;
        if (m <= 2 || n <= 2) {
            return 0;
        }

        boolean[][] visited = new boolean[m][n];
        PriorityQueue<Cell> pq = new PriorityQueue<>();

        // Add border cells to the heap
        for (int i = 0; i < m; i++) {
            pq.offer(new Cell(heightMap[i][0], i, 0));
            pq.offer(new Cell(heightMap[i][n - 1], i, n - 1));
            visited[i][0] = true;
            visited[i][n - 1] = true;
        }
        for (int j = 1; j < n - 1; j++) {
            pq.offer(new Cell(heightMap[0][j], 0, j));
            pq.offer(new Cell(heightMap[m - 1][j], m - 1, j));
            visited[0][j] = true;
            visited[m - 1][j] = true;
        }

        int[] dr = {0, 0, -1, 1};
        int[] dc = {-1, 1, 0, 0};

        long water = 0;

        while (!pq.isEmpty()) {
            Cell cur = pq.poll();
            for (int d = 0; d < 4; d++) {
                int nr = cur.row + dr[d];
                int nc = cur.col + dc[d];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) {
                    continue;
                }
                visited[nr][nc] = true;
                int neighborHeight = heightMap[nr][nc];
                if (neighborHeight < cur.height) {
                    water += (long) (cur.height - neighborHeight);
                }
                pq.offer(new Cell(Math.max(neighborHeight, cur.height), nr, nc));
            }
        }

        return (int) water;
    }
}
```

## Python

```python
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        import heapq

        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        heap = []

        # push all border cells into heap
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = visited[i][n - 1] = True
        for j in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = visited[m - 1][j] = True

        water = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            h, i, j = heapq.heappop(heap)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    nh = heightMap[ni][nj]
                    if h > nh:
                        water += h - nh
                    heapq.heappush(heap, (max(h, nh), ni, nj))

        return water
```

## Python3

```python
class Solution:
    def trapRainWater(self, heightMap):
        import heapq
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        heap = []

        # push border cells
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = visited[i][n - 1] = True
        for j in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = visited[m - 1][j] = True

        res = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while heap:
            h, x, y = heapq.heappop(heap)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    nh = heightMap[nx][ny]
                    if nh < h:
                        res += h - nh
                        heapq.heappush(heap, (h, nx, ny))
                    else:
                        heapq.heappush(heap, (nh, nx, ny))
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int h;
    int r;
    int c;
} Cell;

typedef struct {
    Cell *data;
    int size;
    int capacity;
} MinHeap;

static void heapPush(MinHeap *heap, Cell cell) {
    int i = heap->size++;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap->data[p].h <= cell.h) break;
        heap->data[i] = heap->data[p];
        i = p;
    }
    heap->data[i] = cell;
}

static Cell heapPop(MinHeap *heap) {
    Cell top = heap->data[0];
    Cell last = heap->data[--heap->size];
    int i = 0;
    while (1) {
        int left = i * 2 + 1;
        if (left >= heap->size) break;
        int right = left + 1;
        int smallest = left;
        if (right < heap->size && heap->data[right].h < heap->data[left].h)
            smallest = right;
        if (heap->data[smallest].h >= last.h) break;
        heap->data[i] = heap->data[smallest];
        i = smallest;
    }
    heap->data[i] = last;
    return top;
}

int trapRainWater(int** heightMap, int heightMapSize, int* heightMapColSize) {
    if (heightMapSize == 0) return 0;
    int m = heightMapSize;
    int n = heightMapColSize[0];
    if (m <= 2 || n <= 2) return 0;

    char *visited = (char *)calloc(m * n, sizeof(char));
    MinHeap heap;
    heap.capacity = m * n;
    heap.size = 0;
    heap.data = (Cell *)malloc(heap.capacity * sizeof(Cell));

    // push border cells
    for (int i = 0; i < m; ++i) {
        int cols[2] = {0, n - 1};
        for (int k = 0; k < 2; ++k) {
            int j = cols[k];
            if (!visited[i * n + j]) {
                visited[i * n + j] = 1;
                heapPush(&heap, (Cell){heightMap[i][j], i, j});
            }
        }
    }
    for (int j = 0; j < n; ++j) {
        int rows[2] = {0, m - 1};
        for (int k = 0; k < 2; ++k) {
            int i = rows[k];
            if (!visited[i * n + j]) {
                visited[i * n + j] = 1;
                heapPush(&heap, (Cell){heightMap[i][j], i, j});
            }
        }
    }

    const int dr[4] = {0, 0, -1, 1};
    const int dc[4] = {-1, 1, 0, 0};

    int total = 0;
    while (heap.size > 0) {
        Cell cur = heapPop(&heap);
        for (int d = 0; d < 4; ++d) {
            int nr = cur.r + dr[d];
            int nc = cur.c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (visited[nr * n + nc]) continue;
            visited[nr * n + nc] = 1;
            int nh = heightMap[nr][nc];
            if (nh < cur.h) total += cur.h - nh;
            int newH = nh > cur.h ? nh : cur.h;
            heapPush(&heap, (Cell){newH, nr, nc});
        }
    }

    free(visited);
    free(heap.data);
    return total;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private struct Cell {
        public int r;
        public int c;
        public int h;
        public Cell(int row, int col, int height) {
            r = row;
            c = col;
            h = height;
        }
    }

    private class MinHeap {
        private List<Cell> data = new List<Cell>();
        public int Count => data.Count;

        public void Push(Cell cell) {
            data.Add(cell);
            SiftUp(data.Count - 1);
        }

        public Cell Pop() {
            Cell top = data[0];
            Cell last = data[data.Count - 1];
            data.RemoveAt(data.Count - 1);
            if (data.Count > 0) {
                data[0] = last;
                SiftDown(0);
            }
            return top;
        }

        private void SiftUp(int i) {
            while (i > 0) {
                int p = (i - 1) / 2;
                if (data[p].h <= data[i].h) break;
                Swap(p, i);
                i = p;
            }
        }

        private void SiftDown(int i) {
            int n = data.Count;
            while (true) {
                int l = 2 * i + 1;
                int r = l + 1;
                int smallest = i;
                if (l < n && data[l].h < data[smallest].h) smallest = l;
                if (r < n && data[r].h < data[smallest].h) smallest = r;
                if (smallest == i) break;
                Swap(i, smallest);
                i = smallest;
            }
        }

        private void Swap(int i, int j) {
            Cell tmp = data[i];
            data[i] = data[j];
            data[j] = tmp;
        }
    }

    public int TrapRainWater(int[][] heightMap) {
        if (heightMap == null || heightMap.Length == 0) return 0;
        int m = heightMap.Length;
        int n = heightMap[0].Length;
        if (m <= 2 || n <= 2) return 0;

        bool[,] visited = new bool[m, n];
        MinHeap heap = new MinHeap();

        // Add border cells to heap
        for (int i = 0; i < m; i++) {
            heap.Push(new Cell(i, 0, heightMap[i][0]));
            visited[i, 0] = true;
            heap.Push(new Cell(i, n - 1, heightMap[i][n - 1]));
            visited[i, n - 1] = true;
        }
        for (int j = 1; j < n - 1; j++) {
            heap.Push(new Cell(0, j, heightMap[0][j]));
            visited[0, j] = true;
            heap.Push(new Cell(m - 1, j, heightMap[m - 1][j]));
            visited[m - 1, j] = true;
        }

        long water = 0;
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (heap.Count > 0) {
            Cell cur = heap.Pop();
            for (int d = 0; d < 4; d++) {
                int nr = cur.r + dr[d];
                int nc = cur.c + dc[d];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr, nc]) continue;
                visited[nr, nc] = true;
                int nh = heightMap[nr][nc];
                if (nh < cur.h) {
                    water += cur.h - nh;
                    heap.Push(new Cell(nr, nc, cur.h));
                } else {
                    heap.Push(new Cell(nr, nc, nh));
                }
            }
        }

        return (int)water;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} heightMap
 * @return {number}
 */
var trapRainWater = function(heightMap) {
    const m = heightMap.length;
    if (m === 0) return 0;
    const n = heightMap[0].length;
    if (m < 3 || n < 3) return 0;

    // Min-heap implementation
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(node) {
            const h = this.heap;
            h.push(node);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p].h <= h[i].h) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return null;
            const root = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let left = i * 2 + 1;
                    let right = left + 1;
                    let smallest = i;
                    if (left < h.length && h[left].h < h[smallest].h) smallest = left;
                    if (right < h.length && h[right].h < h[smallest].h) smallest = right;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return root;
        }
    }

    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const heap = new MinHeap();

    // push border cells
    for (let r = 0; r < m; ++r) {
        heap.push({ h: heightMap[r][0], r, c: 0 });
        visited[r][0] = true;
        heap.push({ h: heightMap[r][n - 1], r, c: n - 1 });
        visited[r][n - 1] = true;
    }
    for (let c = 1; c < n - 1; ++c) {
        heap.push({ h: heightMap[0][c], r: 0, c });
        visited[0][c] = true;
        heap.push({ h: heightMap[m - 1][c], r: m - 1, c });
        visited[m - 1][c] = true;
    }

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let water = 0;

    while (heap.size() > 0) {
        const cur = heap.pop();
        for (const [dr, dc] of dirs) {
            const nr = cur.r + dr;
            const nc = cur.c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;
            visited[nr][nc] = true;
            const nh = heightMap[nr][nc];
            if (cur.h > nh) water += cur.h - nh;
            heap.push({ h: Math.max(nh, cur.h), r: nr, c: nc });
        }
    }

    return water;
};
```

## Typescript

```typescript
function trapRainWater(heightMap: number[][]): number {
    const m = heightMap.length;
    if (m === 0) return 0;
    const n = heightMap[0].length;
    if (m <= 2 || n <= 2) return 0;

    class MinHeap {
        private heap: [number, number, number][] = [];
        size(): number { return this.heap.length; }
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
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        private bubbleDown(idx: number): void {
            const length = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let smallest = idx;

                if (left < length && this.heap[left][0] < this.heap[smallest][0]) {
                    smallest = left;
                }
                if (right < length && this.heap[right][0] < this.heap[smallest][0]) {
                    smallest = right;
                }
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const heap = new MinHeap();

    // push border cells
    for (let i = 0; i < m; i++) {
        heap.push([heightMap[i][0], i, 0]);
        visited[i][0] = true;
        heap.push([heightMap[i][n - 1], i, n - 1]);
        visited[i][n - 1] = true;
    }
    for (let j = 1; j < n - 1; j++) {
        heap.push([heightMap[0][j], 0, j]);
        visited[0][j] = true;
        heap.push([heightMap[m - 1][j], m - 1, j]);
        visited[m - 1][j] = true;
    }

    const dirs = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ];

    let total = 0;

    while (heap.size() > 0) {
        const cur = heap.pop()!;
        const curHeight = cur[0];
        const r = cur[1];
        const c = cur[2];

        for (const d of dirs) {
            const nr = r + d[0];
            const nc = c + d[1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;
            visited[nr][nc] = true;
            const neighborHeight = heightMap[nr][nc];
            if (neighborHeight < curHeight) {
                total += curHeight - neighborHeight;
                heap.push([curHeight, nr, nc]);
            } else {
                heap.push([neighborHeight, nr, nc]);
            }
        }
    }

    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $heightMap
     * @return Integer
     */
    function trapRainWater($heightMap) {
        if (empty($heightMap) || empty($heightMap[0])) {
            return 0;
        }
        $m = count($heightMap);
        $n = count($heightMap[0]);
        if ($m <= 2 || $n <= 2) {
            return 0;
        }

        $visited = array_fill(0, $m, array_fill(0, $n, false));

        $pq = new class extends SplPriorityQueue {
            public function compare($p1, $p2) {
                // smaller height should be extracted first (min-heap)
                if ($p1 === $p2) return 0;
                return ($p1 < $p2) ? 1 : -1; // reverse order
            }
        };
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        $push = function($r, $c) use (&$visited, &$heightMap, $pq) {
            $visited[$r][$c] = true;
            $h = $heightMap[$r][$c];
            $pq->insert([$r, $c, $h], $h);
        };

        // push border cells
        for ($i = 0; $i < $m; $i++) {
            if (!$visited[$i][0]) $push($i, 0);
            if ($n > 1 && !$visited[$i][$n - 1]) $push($i, $n - 1);
        }
        for ($j = 0; $j < $n; $j++) {
            if (!$visited[0][$j]) $push(0, $j);
            if ($m > 1 && !$visited[$m - 1][$j]) $push($m - 1, $j);
        }

        $water = 0;
        $dr = [-1, 1, 0, 0];
        $dc = [0, 0, -1, 1];

        while (!$pq->isEmpty()) {
            $cell = $pq->extract();
            list($r, $c, $h) = $cell;
            for ($k = 0; $k < 4; $k++) {
                $nr = $r + $dr[$k];
                $nc = $c + $dc[$k];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                if ($visited[$nr][$nc]) continue;

                $visited[$nr][$nc] = true;
                $nh = $heightMap[$nr][$nc];
                if ($nh < $h) {
                    $water += $h - $nh;
                    $pq->insert([$nr, $nc, $h], $h);
                } else {
                    $pq->insert([$nr, $nc, $nh], $nh);
                }
            }
        }

        return $water;
    }
}
```

## Swift

```swift
class Solution {
    struct Cell: Comparable {
        let height: Int
        let row: Int
        let col: Int
        static func < (lhs: Cell, rhs: Cell) -> Bool {
            return lhs.height < rhs.height
        }
    }

    struct MinHeap {
        private var data: [Cell] = []

        var isEmpty: Bool { data.isEmpty }

        mutating func push(_ element: Cell) {
            data.append(element)
            siftUp(data.count - 1)
        }

        mutating func pop() -> Cell? {
            guard !data.isEmpty else { return nil }
            if data.count == 1 {
                return data.removeLast()
            }
            let root = data[0]
            data[0] = data.removeLast()
            siftDown(0)
            return root
        }

        private mutating func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) / 2
                if data[child] < data[parent] {
                    data.swapAt(child, parent)
                    child = parent
                } else { break }
            }
        }

        private mutating func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < data.count && data[left] < data[smallest] {
                    smallest = left
                }
                if right < data.count && data[right] < data[smallest] {
                    smallest = right
                }
                if smallest == parent { break }
                data.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }

    func trapRainWater(_ heightMap: [[Int]]) -> Int {
        let m = heightMap.count
        guard m > 0 else { return 0 }
        let n = heightMap[0].count
        if m <= 2 || n <= 2 { return 0 }

        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        var heap = MinHeap()

        // Push border cells into heap
        for col in 0..<n {
            heap.push(Cell(height: heightMap[0][col], row: 0, col: col))
            visited[0][col] = true
            heap.push(Cell(height: heightMap[m - 1][col], row: m - 1, col: col))
            visited[m - 1][col] = true
        }
        for row in 1..<(m - 1) {
            heap.push(Cell(height: heightMap[row][0], row: row, col: 0))
            visited[row][0] = true
            heap.push(Cell(height: heightMap[row][n - 1], row: row, col: n - 1))
            visited[row][n - 1] = true
        }

        let dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        var water = 0

        while !heap.isEmpty {
            guard let cell = heap.pop() else { break }
            for (dr, dc) in dirs {
                let nr = cell.row + dr
                let nc = cell.col + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc] {
                    continue
                }
                visited[nr][nc] = true
                let neighborHeight = heightMap[nr][nc]
                if neighborHeight < cell.height {
                    water += cell.height - neighborHeight
                    heap.push(Cell(height: cell.height, row: nr, col: nc))
                } else {
                    heap.push(Cell(height: neighborHeight, row: nr, col: nc))
                }
            }
        }

        return water
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun trapRainWater(heightMap: Array<IntArray>): Int {
        val m = heightMap.size
        if (m == 0) return 0
        val n = heightMap[0].size
        if (m <= 2 || n <= 2) return 0

        val visited = Array(m) { BooleanArray(n) }
        val pq = java.util.PriorityQueue<Cell>(compareBy { it.height })

        // Add all border cells to the heap
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                    pq.add(Cell(heightMap[i][j], i, j))
                    visited[i][j] = true
                }
            }
        }

        val dirs = intArrayOf(-1, 0, 1, 0, -1)
        var total = 0L

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            for (k in 0 until 4) {
                val nr = cur.row + dirs[k]
                val nc = cur.col + dirs[k + 1]
                if (nr in 0 until m && nc in 0 until n && !visited[nr][nc]) {
                    visited[nr][nc] = true
                    val nh = heightMap[nr][nc]
                    if (cur.height > nh) {
                        total += (cur.height - nh).toLong()
                    }
                    val newHeight = maxOf(nh, cur.height)
                    pq.add(Cell(newHeight, nr, nc))
                }
            }
        }

        return total.toInt()
    }

    private data class Cell(val height: Int, val row: Int, val col: Int)
}
```

## Dart

```dart
class Solution {
  int trapRainWater(List<List<int>> heightMap) {
    int m = heightMap.length;
    if (m == 0) return 0;
    int n = heightMap[0].length;
    if (m <= 2 || n <= 2) return 0;

    List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));

    // Min-heap implementation
    final List<_Cell> heap = [];

    void _swap(int i, int j) {
      final tmp = heap[i];
      heap[i] = heap[j];
      heap[j] = tmp;
    }

    void _heapifyUp(int idx) {
      while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (heap[parent].height <= heap[idx].height) break;
        _swap(parent, idx);
        idx = parent;
      }
    }

    void _heapifyDown(int idx) {
      int size = heap.length;
      while (true) {
        int left = idx * 2 + 1;
        int right = left + 1;
        int smallest = idx;

        if (left < size && heap[left].height < heap[smallest].height) {
          smallest = left;
        }
        if (right < size && heap[right].height < heap[smallest].height) {
          smallest = right;
        }
        if (smallest == idx) break;
        _swap(idx, smallest);
        idx = smallest;
      }
    }

    void _push(_Cell cell) {
      heap.add(cell);
      _heapifyUp(heap.length - 1);
    }

    _Cell? _pop() {
      if (heap.isEmpty) return null;
      final top = heap[0];
      final last = heap.removeLast();
      if (heap.isNotEmpty) {
        heap[0] = last;
        _heapifyDown(0);
      }
      return top;
    }

    // Initialize border cells
    for (int i = 0; i < m; ++i) {
      visited[i][0] = true;
      visited[i][n - 1] = true;
      _push(_Cell(heightMap[i][0], i, 0));
      _push(_Cell(heightMap[i][n - 1], i, n - 1));
    }
    for (int j = 1; j < n - 1; ++j) {
      visited[0][j] = true;
      visited[m - 1][j] = true;
      _push(_Cell(heightMap[0][j], 0, j));
      _push(_Cell(heightMap[m - 1][j], m - 1, j));
    }

    const List<int> dr = [0, 0, -1, 1];
    const List<int> dc = [-1, 1, 0, 0];

    int totalWater = 0;

    while (heap.isNotEmpty) {
      final cell = _pop()!;
      int curHeight = cell.height;
      for (int k = 0; k < 4; ++k) {
        int nr = cell.row + dr[k];
        int nc = cell.col + dc[k];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
        if (visited[nr][nc]) continue;
        visited[nr][nc] = true;
        int neighborHeight = heightMap[nr][nc];
        if (neighborHeight < curHeight) {
          totalWater += curHeight - neighborHeight;
        }
        _push(_Cell(
            neighborHeight > curHeight ? neighborHeight : curHeight, nr, nc));
      }
    }

    return totalWater;
  }
}

class _Cell {
  int height;
  int row;
  int col;
  _Cell(this.height, this.row, this.col);
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type cell struct {
	h, r, c int
}

type minHeap []cell

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].h < h[j].h }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(cell)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func trapRainWater(heightMap [][]int) int {
	m := len(heightMap)
	if m == 0 {
		return 0
	}
	n := len(heightMap[0])
	if m < 3 || n < 3 {
		return 0
	}

	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	h := &minHeap{}
	heap.Init(h)

	// push border cells
	for c := 0; c < n; c++ {
		heap.Push(h, cell{heightMap[0][c], 0, c})
		visited[0][c] = true
		heap.Push(h, cell{heightMap[m-1][c], m - 1, c})
		visited[m-1][c] = true
	}
	for r := 1; r < m-1; r++ {
		heap.Push(h, cell{heightMap[r][0], r, 0})
		visited[r][0] = true
		heap.Push(h, cell{heightMap[r][n-1], r, n - 1})
		visited[r][n-1] = true
	}

	dr := []int{-1, 1, 0, 0}
	dc := []int{0, 0, -1, 1}
	total := 0

	for h.Len() > 0 {
		cur := heap.Pop(h).(cell)
		for k := 0; k < 4; k++ {
			nr, nc := cur.r+dr[k], cur.c+dc[k]
			if nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc] {
				continue
			}
			visited[nr][nc] = true
			nh := heightMap[nr][nc]
			if nh < cur.h {
				total += cur.h - nh
				nh = cur.h
			}
			heap.Push(h, cell{nh, nr, nc})
		}
	}

	return total
}
```

## Ruby

```ruby
def heap_push(heap, item)
  heap << item
  idx = heap.size - 1
  while idx > 0
    parent = (idx - 1) / 2
    break if heap[parent][0] <= heap[idx][0]
    heap[parent], heap[idx] = heap[idx], heap[parent]
    idx = parent
  end
end

def heap_pop(heap)
  top = heap[0]
  last = heap.pop
  unless heap.empty?
    heap[0] = last
    idx = 0
    size = heap.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      smallest = left if left < size && heap[left][0] < heap[smallest][0]
      smallest = right if right < size && heap[right][0] < heap[smallest][0]
      break if smallest == idx
      heap[idx], heap[smallest] = heap[smallest], heap[idx]
      idx = smallest
    end
  end
  top
end

# @param {Integer[][]} height_map
# @return {Integer}
def trap_rain_water(height_map)
  m = height_map.size
  return 0 if m == 0
  n = height_map[0].size
  return 0 if m <= 2 || n <= 2

  visited = Array.new(m) { Array.new(n, false) }
  heap = []

  (0...m).each do |i|
    [[i, 0], [i, n - 1]].each do |r, c|
      next if visited[r][c]
      visited[r][c] = true
      heap_push(heap, [height_map[r][c], r, c])
    end
  end

  (0...n).each do |j|
    [[0, j], [m - 1, j]].each do |r, c|
      next if visited[r][c]
      visited[r][c] = true
      heap_push(heap, [height_map[r][c], r, c])
    end
  end

  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  water = 0

  until heap.empty?
    h, r, c = heap_pop(heap)
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]
      visited[nr][nc] = true
      nh = height_map[nr][nc]
      if nh < h
        water += h - nh
        heap_push(heap, [h, nr, nc])
      else
        heap_push(heap, [nh, nr, nc])
      end
    end
  end

  water
end
```

## Scala

```scala
object Solution {
  def trapRainWater(heightMap: Array[Array[Int]]): Int = {
    val m = heightMap.length
    if (m == 0) return 0
    val n = heightMap(0).length
    if (m <= 2 || n <= 2) return 0

    val visited = Array.ofDim[Boolean](m, n)
    val pq = new java.util.PriorityQueue[Cell](
      (a: Cell, b: Cell) => Integer.compare(a.h, b.h)
    )

    // add border cells
    for (i <- 0 until m) {
      pq.offer(Cell(heightMap(i)(0), i, 0))
      visited(i)(0) = true
      if (n > 1) {
        pq.offer(Cell(heightMap(i)(n - 1), i, n - 1))
        visited(i)(n - 1) = true
      }
    }
    for (j <- 1 until n - 1) {
      pq.offer(Cell(heightMap(0)(j), 0, j))
      visited(0)(j) = true
      if (m > 1) {
        pq.offer(Cell(heightMap(m - 1)(j), m - 1, j))
        visited(m - 1)(j) = true
      }
    }

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    var total: Long = 0L

    while (!pq.isEmpty) {
      val cur = pq.poll()
      for ((dr, dc) <- dirs) {
        val nr = cur.r + dr
        val nc = cur.c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited(nr)(nc)) {
          visited(nr)(nc) = true
          val nh = heightMap(nr)(nc)
          if (cur.h > nh) total += (cur.h - nh).toLong
          val newH = Math.max(cur.h, nh)
          pq.offer(Cell(newH, nr, nc))
        }
      }
    }

    total.toInt
  }

  private case class Cell(h: Int, r: Int, c: Int)
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        if height_map.is_empty() || height_map[0].is_empty() {
            return 0;
        }
        let m = height_map.len();
        let n = height_map[0].len();

        let mut visited = vec![vec![false; n]; m];
        let mut heap: BinaryHeap<(Reverse<i32>, usize, usize)> = BinaryHeap::new();

        // Push all border cells into the heap
        for i in 0..m {
            for j in 0..n {
                if i == 0 || i + 1 == m || j == 0 || j + 1 == n {
                    heap.push((Reverse(height_map[i][j]), i, j));
                    visited[i][j] = true;
                }
            }
        }

        let dirs = [(-1i32, 0i32), (1, 0), (0, -1), (0, 1)];
        let mut water: i64 = 0;

        while let Some((Reverse(cur_h), r, c)) = heap.pop() {
            for &(dr, dc) in &dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                    continue;
                }
                let (nr_usize, nc_usize) = (nr as usize, nc as usize);
                if visited[nr_usize][nc_usize] {
                    continue;
                }
                visited[nr_usize][nc_usize] = true;
                let neigh_h = height_map[nr_usize][nc_usize];
                if neigh_h < cur_h {
                    water += (cur_h - neigh_h) as i64;
                    heap.push((Reverse(cur_h), nr_usize, nc_usize));
                } else {
                    heap.push((Reverse(neigh_h), nr_usize, nc_usize));
                }
            }
        }

        water as i32
    }
}
```

## Racket

```racket
(require data/priority-queue)

(define/contract (trap-rain-water heightMap)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length heightMap))
         (n (if (zero? m) 0 (length (first heightMap)))))
    (if (or (< m 3) (< n 3))
        0
        (let* ((rows (list->vector (map list->vector heightMap)))
               (visited (make-vector m #f))
               (pq (make-pq <)))
          ;; init visited vectors
          (for ([i m])
            (vector-set! visited i (make-vector n #f)))
          ;; push border cells
          (for* ([i m] [j n]
                 #:when (or (= i 0) (= i (- m 1)) (= j 0) (= j (- n 1))))
            (let ((h (vector-ref (vector-ref rows i) j)))
              (pq-push! pq (list h i j))
              (vector-set! (vector-ref visited i) j #t)))
          ;; directions
          (define dirs '((0 -1) (0 1) (-1 0) (1 0)))
          (let loop ((total 0))
            (if (pq-empty? pq)
                total
                (let* ((item (pq-pop! pq))
                       (h (first item))
                       (r (second item))
                       (c (third item)))
                  (for ([d dirs])
                    (define nr (+ r (first d)))
                    (define nc (+ c (second d)))
                    (when (and (>= nr 0) (< nr m)
                               (>= nc 0) (< nc n)
                               (not (vector-ref (vector-ref visited nr) nc)))
                      (let ((nh (vector-ref (vector-ref rows nr) nc)))
                        (define water (max 0 (- h nh)))
                        (when (> water 0)
                          (set! total (+ total water)))
                        (pq-push! pq (list (max h nh) nr nc))
                        (vector-set! (vector-ref visited nr) nc #t))))
                  (loop total)))))))))
```

## Erlang

```erlang
-module(solution).
-export([trap_rain_water/1]).

-spec trap_rain_water(HeightMap :: [[integer()]]) -> integer().
trap_rain_water(HeightMap) ->
    M = length(HeightMap),
    N = case HeightMap of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    if
        M =< 2 orelse N =< 2 ->
            0;
        true ->
            {Boundary0, Visited0} = init_boundary(HeightMap, M, N),
            process(Boundary0, Visited0, 0, HeightMap, M, N)
    end.

%% Initialize boundary heap with all edge cells
init_boundary(HM, M, N) ->
    Set0 = gb_sets:new(),
    Vis0 = #{},
    {Set1, Vis1} =
        lists:foldl(fun(R, {SAcc, VAcc}) ->
            % left column (c = 0)
            HLeft = get_height(HM, R, 0),
            S1 = gb_sets:add({HLeft, R, 0}, SAcc),
            V1 = maps:put({R,0}, true, VAcc),
            % right column (c = N-1) if different
            case N > 1 of
                true ->
                    CRight = N - 1,
                    HRight = get_height(HM, R, CRight),
                    S2 = gb_sets:add({HRight, R, CRight}, S1),
                    V2 = maps:put({R,CRight}, true, V1),
                    {S2, V2};
                false ->
                    {S1, V1}
            end
        end, {Set0, Vis0}, lists:seq(0, M-1)),
    % top row (r = 0) for columns 1..N-2
    {Set2, Vis2} =
        if N > 2 ->
                lists:foldl(fun(C, {SAcc, VAcc}) ->
                    case maps:is_key({0,C}, VAcc) of
                        true -> {SAcc, VAcc};
                        false ->
                            H = get_height(HM, 0, C),
                            S1 = gb_sets:add({H, 0, C}, SAcc),
                            V1 = maps:put({0,C}, true, VAcc),
                            {S1, V1}
                    end
                end, {Set1, Vis1}, lists:seq(1, N-2));
           true -> {Set1, Vis1}
        end,
    % bottom row (r = M-1) for columns 1..N-2 if different from top
    {Set3, Vis3} =
        if M > 1, N > 2 ->
                lists:foldl(fun(C, {SAcc, VAcc}) ->
                    case maps:is_key({M-1,C}, VAcc) of
                        true -> {SAcc, VAcc};
                        false ->
                            H = get_height(HM, M-1, C),
                            S1 = gb_sets:add({H, M-1, C}, SAcc),
                            V1 = maps:put({M-1,C}, true, VAcc),
                            {S1, V1}
                    end
                end, {Set2, Vis2}, lists:seq(1, N-2));
           true -> {Set2, Vis2}
        end,
    {Set3, Vis3}.

%% Main processing loop
process(Boundary, Visited, Total, HM, M, N) ->
    case gb_sets:is_empty(Boundary) of
        true -> Total;
        false ->
            Cell = gb_sets:choose(Boundary),
            Boundary1 = gb_sets:delete(Cell, Boundary),
            {Height, R, C} = Cell,
            Dirs = [{-1,0},{1,0},{0,-1},{0,1}],
            {NewBoundary, NewVisited, NewTotal} =
                lists:foldl(fun({DR,DC}, {BAcc,VAcc,TAcc}) ->
                    NR = R + DR,
                    NC = C + DC,
                    if
                        NR < 0 orelse NR >= M orelse NC < 0 orelse NC >= N ->
                            {BAcc,VAcc,TAcc};
                        maps:is_key({NR,NC}, VAcc) ->
                            {BAcc,VAcc,TAcc};
                        true ->
                            NH = get_height(HM, NR, NC),
                            Water = erlang:max(0, Height - NH),
                            T2 = TAcc + Water,
                            NewH = erlang:max(NH, Height),
                            B2 = gb_sets:add({NewH, NR, NC}, BAcc),
                            V2 = maps:put({NR,NC}, true, VAcc),
                            {B2,V2,T2}
                    end
                end, {Boundary1, Visited, Total}, Dirs),
            process(NewBoundary, NewVisited, NewTotal, HM, M, N)
    end.

%% Helper to fetch height from matrix
get_height(HM, R, C) ->
    Row = lists:nth(R + 1, HM),
    lists:nth(C + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec trap_rain_water(height_map :: [[integer]]) :: integer
  def trap_rain_water(height_map) do
    m = length(height_map)
    n = if m == 0, do: 0, else: length(hd(height_map))

    # No interior cells can hold water
    if m <= 2 or n <= 2 do
      0
    else
      border =
        (for i <- 0..(m - 1), j <- [0, n - 1], do: {i, j}) ++
          (for j <- 0..(n - 1), i <- [0, m - 1], do: {i, j})

      border = Enum.uniq(border)

      {tree, visited} =
        Enum.reduce(border, {:gb_trees.empty(), %{}}, fn {r, c}, {t, v} ->
          h = get_height(height_map, r, c)
          t = insert(t, h, {r, c})
          v = Map.put(v, {r, c}, true)
          {t, v}
        end)

      process(tree, visited, height_map, m, n, 0)
    end
  end

  # Recursive processing of the priority queue
  defp process(tree, _visited, _height_map, _m, _n, water) when :gb_trees.is_empty(tree), do: water

  defp process(tree, visited, height_map, m, n, water) do
    {height, cells, tree_rest} = :gb_trees.take_smallest(tree)
    [cell | rest] = cells

    new_tree =
      if rest == [] do
        tree_rest
      else
        :gb_trees.insert(height, rest, tree_rest)
      end

    {r, c} = cell
    dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

    {updated_tree, updated_visited, updated_water} =
      Enum.reduce(dirs, {new_tree, visited, water}, fn {dr, dc},
                                                       {t_acc, v_acc, w_acc} ->
        nr = r + dr
        nc = c + dc

        cond do
          nr < 0 or nr >= m or nc < 0 or nc >= n ->
            {t_acc, v_acc, w_acc}

          Map.has_key?(v_acc, {nr, nc}) ->
            {t_acc, v_acc, w_acc}

          true ->
            v_new = Map.put(v_acc, {nr, nc}, true)
            nh = get_height(height_map, nr, nc)

            if nh < height do
              w_new = w_acc + (height - nh)
              t_new = insert(t_acc, height, {nr, nc})
              {t_new, v_new, w_new}
            else
              t_new = insert(t_acc, nh, {nr, nc})
              {t_new, v_new, w_acc}
            end
        end
      end)

    process(updated_tree, updated_visited, height_map, m, n, updated_water)
  end

  # Insert a coordinate into the gb_tree keyed by its effective height
  defp insert(tree, h, coord) do
    case :gb_trees.lookup(h, tree) do
      :none -> :gb_trees.insert(h, [coord], tree)
      {:value, list} -> :gb_trees.update(h, [coord | list], tree)
    end
  end

  # Retrieve height from the matrix
  defp get_height(map, r, c) do
    map |> Enum.at(r) |> Enum.at(c)
  end
end
```

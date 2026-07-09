# 3341. Find Minimum Time to Reach Last Room I

## Cpp

```cpp
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        const long long INF = LLONG_MAX / 4;
        vector<vector<long long>> dist(n, vector<long long>(m, INF));
        using State = tuple<long long,int,int>;
        priority_queue<State, vector<State>, greater<State>> pq;
        dist[0][0] = 0;
        pq.emplace(0LL, 0, 0);
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.empty()) {
            auto [d, x, y] = pq.top();
            pq.pop();
            if (d != dist[x][y]) continue;
            if (x == n - 1 && y == m - 1) return static_cast<int>(d);
            for (auto &dir : dirs) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                long long nd = max(d, static_cast<long long>(moveTime[nx][ny])) + 1;
                if (nd < dist[nx][ny]) {
                    dist[nx][ny] = nd;
                    pq.emplace(nd, nx, ny);
                }
            }
        }
        return static_cast<int>(dist[n-1][m-1]);
    }
};
```

## Java

```java
class Solution {
    public int minTimeToReach(int[][] moveTime) {
        int n = moveTime.length;
        int m = moveTime[0].length;
        long INF = Long.MAX_VALUE / 4;
        long[][] dist = new long[n][m];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(dist[i], INF);
        }
        dist[0][0] = 0L;
        java.util.PriorityQueue<long[]> pq = new java.util.PriorityQueue<>(
                (a, b) -> Long.compare(a[0], b[0])
        );
        pq.offer(new long[]{0L, 0L, 0L}); // time, row, col

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int r = (int) cur[1];
            int c = (int) cur[2];
            if (d != dist[r][c]) continue;
            if (r == n - 1 && c == m - 1) break;

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                long nd = Math.max(d, (long) moveTime[nr][nc]) + 1L;
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    pq.offer(new long[]{nd, nr, nc});
                }
            }
        }

        return (int) dist[n - 1][m - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        import heapq
        n = len(moveTime)
        m = len(moveTime[0])
        INF = 10**20
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (time, i, j)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while heap:
            t, i, j = heapq.heappop(heap)
            if t != dist[i][j]:
                continue
            if i == n-1 and j == m-1:
                return t
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    nt = max(t, moveTime[ni][nj]) + 1
                    if nt < dist[ni][nj]:
                        dist[ni][nj] = nt
                        heapq.heappush(heap, (nt, ni, nj))
        return dist[n-1][m-1]
```

## Python3

```python
class Solution:
    def minTimeToReach(self, moveTime):
        import heapq
        n = len(moveTime)
        m = len(moveTime[0])
        INF = 10**20
        dist = [[INF] * m for _ in range(n)]
        # start at (0,0) at time max(0, moveTime[0][0]) but problem guarantees 0
        dist[0][0] = max(0, moveTime[0][0])
        heap = [(dist[0][0], 0, 0)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while heap:
            d, i, j = heapq.heappop(heap)
            if d != dist[i][j]:
                continue
            if i == n-1 and j == m-1:
                return d
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    nd = max(d, moveTime[ni][nj]) + 1
                    if nd < dist[ni][nj]:
                        dist[ni][nj] = nd
                        heapq.heappush(heap, (nd, ni, nj))
        return dist[n-1][m-1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long time;
    int idx;
} HeapNode;

static void heapSwap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapNode *heap, int *size, HeapNode node) {
    int i = (*size)++;
    heap[i] = node;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].time <= heap[i].time) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static HeapNode heapPop(HeapNode *heap, int *size) {
    HeapNode top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0, n = *size;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= n) break;
        int smallest = l;
        if (r < n && heap[r].time < heap[l].time) smallest = r;
        if (heap[i].time <= heap[smallest].time) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

int minTimeToReach(int** moveTime, int moveTimeSize, int* moveTimeColSize) {
    int n = moveTimeSize;
    int m = moveTimeColSize[0];
    int total = n * m;

    long long *dist = (long long *)malloc(total * sizeof(long long));
    char *vis = (char *)calloc(total, sizeof(char));

    for (int i = 0; i < total; ++i) dist[i] = LLONG_MAX;

    // heap capacity a bit larger than needed
    HeapNode *heap = (HeapNode *)malloc((total * 5 + 10) * sizeof(HeapNode));
    int heapSize = 0;

    long long startTime = moveTime[0][0];
    if (startTime < 0) startTime = 0;
    dist[0] = startTime;
    heapPush(heap, &heapSize, (HeapNode){startTime, 0});

    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    while (heapSize) {
        HeapNode cur = heapPop(heap, &heapSize);
        if (vis[cur.idx]) continue;
        vis[cur.idx] = 1;
        if (cur.idx == total - 1) break;

        int i = cur.idx / m;
        int j = cur.idx % m;

        for (int d = 0; d < 4; ++d) {
            int ni = i + dirs[d][0];
            int nj = j + dirs[d][1];
            if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
            int nidx = ni * m + nj;

            long long arrive = cur.time;
            if (arrive < moveTime[ni][nj]) arrive = moveTime[ni][nj];
            arrive += 1; // moving takes one second

            if (arrive < dist[nidx]) {
                dist[nidx] = arrive;
                heapPush(heap, &heapSize, (HeapNode){arrive, nidx});
            }
        }
    }

    int result = (int)dist[total - 1];
    free(dist);
    free(vis);
    free(heap);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinTimeToReach(int[][] moveTime) {
        int n = moveTime.Length;
        int m = moveTime[0].Length;
        int total = n * m;
        long[] dist = new long[total];
        for (int i = 0; i < total; i++) dist[i] = long.MaxValue;

        // start at (0,0) at time 0
        dist[0] = 0;
        var pq = new PriorityQueue<int, long>();
        pq.Enqueue(0, 0);

        int[] dirI = new int[] { -1, 1, 0, 0 };
        int[] dirJ = new int[] { 0, 0, -1, 1 };

        while (pq.Count > 0) {
            int idx = pq.Dequeue();
            long cur = dist[idx];
            int i = idx / m;
            int j = idx % m;

            if (i == n - 1 && j == m - 1) break; // reached target with minimal time

            for (int d = 0; d < 4; d++) {
                int ni = i + dirI[d];
                int nj = j + dirJ[d];
                if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
                int nIdx = ni * m + nj;
                long arrival = Math.Max(cur, (long)moveTime[ni][nj]) + 1;
                if (arrival < dist[nIdx]) {
                    dist[nIdx] = arrival;
                    pq.Enqueue(nIdx, arrival);
                }
            }
        }

        return (int)dist[total - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} moveTime
 * @return {number}
 */
var minTimeToReach = function(moveTime) {
    const n = moveTime.length;
    const m = moveTime[0].length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dist = Array.from({ length: n }, () => Array(m).fill(INF));
    
    // Min-heap implementation
    class MinHeap {
        constructor() { this.heap = []; }
        push(node) {
            this.heap.push(node);
            this._siftUp(this.heap.length - 1);
        }
        pop() {
            if (this.heap.length === 0) return null;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this._siftDown(0);
            }
            return top;
        }
        _siftUp(idx) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        _siftDown(idx) {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
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
    
    const heap = new MinHeap();
    dist[0][0] = moveTime[0][0];
    heap.push([dist[0][0], 0, 0]);
    
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    while (!heap.isEmpty()) {
        const [curTime, i, j] = heap.pop();
        if (curTime !== dist[i][j]) continue;
        if (i === n - 1 && j === m - 1) break; // reached target with minimal time
        for (const [dx, dy] of dirs) {
            const ni = i + dx, nj = j + dy;
            if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
            const nextTime = Math.max(curTime, moveTime[ni][nj]) + 1;
            if (nextTime < dist[ni][nj]) {
                dist[ni][nj] = nextTime;
                heap.push([nextTime, ni, nj]);
            }
        }
    }
    
    return dist[n - 1][m - 1];
};
```

## Typescript

```typescript
function minTimeToReach(moveTime: number[][]): number {
    const n = moveTime.length;
    const m = moveTime[0].length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dist: number[][] = Array.from({ length: n }, () => Array(m).fill(INF));
    dist[0][0] = 0;

    class MinHeap {
        data: [number, number, number][] = [];
        push(item: [number, number, number]): void {
            this.data.push(item);
            this.bubbleUp(this.data.length - 1);
        }
        bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.data[parent][0] <= this.data[idx][0]) break;
                [this.data[parent], this.data[idx]] = [this.data[idx], this.data[parent]];
                idx = parent;
            }
        }
        pop(): [number, number, number] | undefined {
            if (this.data.length === 0) return undefined;
            const top = this.data[0];
            const last = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        bubbleDown(idx: number): void {
            const n = this.data.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && this.data[left][0] < this.data[smallest][0]) smallest = left;
                if (right < n && this.data[right][0] < this.data[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.data[smallest], this.data[idx]] = [this.data[idx], this.data[smallest]];
                idx = smallest;
            }
        }
        size(): number {
            return this.data.length;
        }
    }

    const heap = new MinHeap();
    heap.push([0, 0, 0]);
    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ];

    while (heap.size() > 0) {
        const cur = heap.pop()!;
        const [time, i, j] = cur;
        if (time !== dist[i][j]) continue;
        if (i === n - 1 && j === m - 1) break;

        for (const [dx, dy] of dirs) {
            const ni = i + dx;
            const nj = j + dy;
            if (ni < 0 || nj < 0 || ni >= n || nj >= m) continue;
            const newTime = Math.max(time, moveTime[ni][nj]) + 1;
            if (newTime < dist[ni][nj]) {
                dist[ni][nj] = newTime;
                heap.push([newTime, ni, nj]);
            }
        }
    }

    return dist[n - 1][m - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $moveTime
     * @return Integer
     */
    function minTimeToReach($moveTime) {
        $n = count($moveTime);
        $m = count($moveTime[0]);
        $INF = PHP_INT_MAX;

        // distance matrix
        $dist = array_fill(0, $n, array_fill(0, $m, $INF));
        $dist[0][0] = 0; // start at time 0

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        // use negative priority because SplPriorityQueue is a max-heap
        $pq->insert([0, 0], 0); // priority 0 (max), we will invert when extracting

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$pq->isEmpty()) {
            $elem = $pq->extract();
            $pos = $elem['data'];
            $priority = $elem['priority']; // this is the stored priority (max-heap)
            $i = $pos[0];
            $j = $pos[1];
            // actual distance is negative of priority
            $curDist = -$priority;

            if ($curDist > $dist[$i][$j]) {
                continue;
            }

            foreach ($dirs as $d) {
                $ni = $i + $d[0];
                $nj = $j + $d[1];
                if ($ni < 0 || $ni >= $n || $nj < 0 || $nj >= $m) {
                    continue;
                }
                // time to move into neighbor
                $arrival = max($curDist, $moveTime[$ni][$nj]) + 1;
                if ($arrival < $dist[$ni][$nj]) {
                    $dist[$ni][$nj] = $arrival;
                    $pq->insert([$ni, $nj], -$arrival);
                }
            }
        }

        return $dist[$n-1][$m-1];
    }
}
```

## Swift

```swift
class Solution {
    func minTimeToReach(_ moveTime: [[Int]]) -> Int {
        let n = moveTime.count
        let m = moveTime[0].count
        var dist = Array(repeating: Array(repeating: Int.max, count: m), count: n)
        dist[0][0] = 0
        
        var pq = PriorityQueue()
        pq.push((0, 0, 0)) // (time, i, j)
        
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while let node = pq.pop() {
            let (curTime, i, j) = node
            if curTime != dist[i][j] { continue }
            if i == n - 1 && j == m - 1 {
                return curTime
            }
            for d in dirs {
                let ni = i + d.0
                let nj = j + d.1
                if ni < 0 || ni >= n || nj < 0 || nj >= m { continue }
                let nextTime = max(curTime, moveTime[ni][nj]) + 1
                if nextTime < dist[ni][nj] {
                    dist[ni][nj] = nextTime
                    pq.push((nextTime, ni, nj))
                }
            }
        }
        return dist[n-1][m-1]
    }
}

struct PriorityQueue {
    private var heap: [(Int, Int, Int)] = [] // (time, i, j)
    
    mutating func push(_ element: (Int, Int, Int)) {
        heap.append(element)
        siftUp(heap.count - 1)
    }
    
    mutating func pop() -> (Int, Int, Int)? {
        guard !heap.isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeFirst()
        }
        let top = heap[0]
        heap[0] = heap.removeLast()
        siftDown(0)
        return top
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if heap[child].0 < heap[parent].0 {
                heap.swapAt(child, parent)
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
            if left < heap.count && heap[left].0 < heap[smallest].0 {
                smallest = left
            }
            if right < heap.count && heap[right].0 < heap[smallest].0 {
                smallest = right
            }
            if smallest == parent { break }
            heap.swapAt(parent, smallest)
            parent = smallest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minTimeToReach(moveTime: Array<IntArray>): Int {
        val n = moveTime.size
        val m = moveTime[0].size
        val INF = Long.MAX_VALUE / 4
        val dist = Array(n) { LongArray(m) { INF } }
        data class Node(val time: Long, val x: Int, val y: Int)
        val pq = java.util.PriorityQueue<Node>(compareBy { it.time })
        dist[0][0] = 0L
        pq.add(Node(0L, 0, 0))
        val dirs = intArrayOf(-1, 0, 1, 0, -1)
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.time != dist[cur.x][cur.y]) continue
            if (cur.x == n - 1 && cur.y == m - 1) break
            for (k in 0 until 4) {
                val nx = cur.x + dirs[k]
                val ny = cur.y + dirs[k + 1]
                if (nx !in 0 until n || ny !in 0 until m) continue
                val wait = maxOf(cur.time, moveTime[nx][ny].toLong())
                val arrival = wait + 1L
                if (arrival < dist[nx][ny]) {
                    dist[nx][ny] = arrival
                    pq.add(Node(arrival, nx, ny))
                }
            }
        }
        return dist[n - 1][m - 1].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minTimeToReach(List<List<int>> moveTime) {
    final n = moveTime.length;
    final m = moveTime[0].length;
    const int INF = 1 << 60;

    List<List<int>> dist = List.generate(
        n, (_) => List.filled(m, INF, growable: false),
        growable: false);
    dist[0][0] = 0;

    final heap = _MinHeap();
    heap.push(_Node(0, 0, 0));

    const dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    while (!heap.isEmpty) {
      final cur = heap.pop()!;
      int t = cur.time;
      int i = cur.x;
      int j = cur.y;

      if (t != dist[i][j]) continue;
      if (i == n - 1 && j == m - 1) break;

      for (var d in dirs) {
        int ni = i + d[0];
        int nj = j + d[1];
        if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
        int nt = (t > moveTime[ni][nj] ? t : moveTime[ni][nj]) + 1;
        if (nt < dist[ni][nj]) {
          dist[ni][nj] = nt;
          heap.push(_Node(nt, ni, nj));
        }
      }
    }

    return dist[n - 1][m - 1];
  }
}

class _Node {
  int time;
  int x;
  int y;
  _Node(this.time, this.x, this.y);
}

class _MinHeap {
  final List<_Node> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(_Node node) {
    _data.add(node);
    _siftUp(_data.length - 1);
  }

  _Node? pop() {
    if (_data.isEmpty) return null;
    final root = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return root;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_data[parent].time <= _data[idx].time) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _data[left].time < _data[smallest].time) {
        smallest = left;
      }
      if (right < n && _data[right].time < _data[smallest].time) {
        smallest = right;
      }
      if (smallest == idx) break;
      _swap(idx, smallest);
      idx = smallest;
    }
  }

  void _swap(int i, int j) {
    final tmp = _data[i];
    _data[i] = _data[j];
    _data[j] = tmp;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type node struct {
	t, x, y int
}
type priorityQueue []node

func (pq priorityQueue) Len() int { return len(pq) }
func (pq priorityQueue) Less(i, j int) bool {
	return pq[i].t < pq[j].t
}
func (pq priorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *priorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(node))
}
func (pq *priorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[:n-1]
	return it
}

func minTimeToReach(moveTime [][]int) int {
	n, m := len(moveTime), len(moveTime[0])
	const INF = int(^uint(0) >> 1)

	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, m)
		for j := range dist[i] {
			dist[i][j] = INF
		}
	}
	dist[0][0] = 0

	pq := &priorityQueue{}
	heap.Init(pq)
	heap.Push(pq, node{t: 0, x: 0, y: 0})

	dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(node)
		if cur.t != dist[cur.x][cur.y] {
			continue
		}
		if cur.x == n-1 && cur.y == m-1 {
			return cur.t
		}
		for _, d := range dir {
			nx, ny := cur.x+d[0], cur.y+d[1]
			if nx < 0 || nx >= n || ny < 0 || ny >= m {
				continue
			}
			newT := max(cur.t, moveTime[nx][ny]) + 1
			if newT < dist[nx][ny] {
				dist[nx][ny] = newT
				heap.Push(pq, node{t: newT, x: nx, y: ny})
			}
		}
	}
	return dist[n-1][m-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def min_time_to_reach(move_time)
  n = move_time.size
  m = move_time[0].size
  INF = (1 << 62)

  dist = Array.new(n) { Array.new(m, INF) }
  dist[0][0] = 0

  heap = []
  # push helper
  push = lambda do |item|
    heap << item
    idx = heap.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      break if heap[parent][0] <= heap[idx][0]
      heap[parent], heap[idx] = heap[idx], heap[parent]
      idx = parent
    end
  end

  pop = lambda do
    return nil if heap.empty?
    min = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      idx = 0
      size = heap.size
      loop do
        left = idx * 2 + 1
        right = left + 1
        smallest = idx
        if left < size && heap[left][0] < heap[smallest][0]
          smallest = left
        end
        if right < size && heap[right][0] < heap[smallest][0]
          smallest = right
        end
        break if smallest == idx
        heap[smallest], heap[idx] = heap[idx], heap[smallest]
        idx = smallest
      end
    end
    min
  end

  push.call([0, 0, 0])

  dirs = [[1,0],[-1,0],[0,1],[0,-1]]

  until heap.empty?
    cur_time, r, c = pop.call
    next if cur_time != dist[r][c]

    return cur_time if r == n - 1 && c == m - 1

    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next unless nr.between?(0, n - 1) && nc.between?(0, m - 1)
      new_time = [cur_time, move_time[nr][nc]].max + 1
      if new_time < dist[nr][nc]
        dist[nr][nc] = new_time
        push.call([new_time, nr, nc])
      end
    end
  end

  dist[n - 1][m - 1]
end
```

## Scala

```scala
object Solution {
  def minTimeToReach(moveTime: Array[Array[Int]]): Int = {
    val n = moveTime.length
    val m = moveTime(0).length
    val INF: Long = Long.MaxValue / 4

    val dist = Array.fill(n, m)(INF)

    case class Node(t: Long, x: Int, y: Int)
    implicit val ord: Ordering[Node] = Ordering.by((node: Node) => -node.t)

    import scala.collection.mutable.PriorityQueue
    val pq = PriorityQueue.empty[Node]

    dist(0)(0) = 0L
    pq.enqueue(Node(0L, 0, 0))

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (pq.nonEmpty) {
      val cur = pq.dequeue()
      val t = cur.t
      val x = cur.x
      val y = cur.y

      if (t != dist(x)(y)) {
        // outdated entry
      } else {
        for ((dx, dy) <- dirs) {
          val nx = x + dx
          val ny = y + dy
          if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            val nt = math.max(t, moveTime(nx)(ny).toLong) + 1L
            if (nt < dist(nx)(ny)) {
              dist(nx)(ny) = nt
              pq.enqueue(Node(nt, nx, ny))
            }
          }
        }
      }
    }

    dist(n - 1)(m - 1).toInt
  }
}
```

## Rust

```rust
use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let n = move_time.len();
        let m = move_time[0].len();
        let mut dist = vec![vec![i64::MAX; m]; n];
        let start = move_time[0][0] as i64;
        dist[0][0] = start;
        let mut heap = BinaryHeap::new();
        heap.push(Reverse((start, 0usize, 0usize)));
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        while let Some(Reverse((time, x, y))) = heap.pop() {
            if time != dist[x][y] {
                continue;
            }
            if x == n - 1 && y == m - 1 {
                return time as i32;
            }
            for (dx, dy) in dirs.iter() {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx >= 0 && nx < n as i32 && ny >= 0 && ny < m as i32 {
                    let nxu = nx as usize;
                    let nyu = ny as usize;
                    let wait = move_time[nxu][nyu] as i64;
                    let arrival = std::cmp::max(time, wait) + 1;
                    if arrival < dist[nxu][nyu] {
                        dist[nxu][nyu] = arrival;
                        heap.push(Reverse((arrival, nxu, nyu)));
                    }
                }
            }
        }
        dist[n - 1][m - 1] as i32
    }
}
```

## Racket

```racket
(require racket/priority-queue)

(define/contract (min-time-to-reach moveTime)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length moveTime))
         (m (if (= n 0) 0 (length (first moveTime))))
         (INF (expt 10 15)))
    ;; distance matrix
    (define dist (make-vector n))
    (for ([i n])
      (vector-set! dist i (make-vector m INF)))
    (vector-set! (vector-ref dist 0) 0 0)

    ;; priority queue storing (time i j)
    (define pq (make-pq <))
    (pq-add! pq (list 0 0 0))

    (let loop ()
      (if (pq-empty? pq)
          (vector-ref (vector-ref dist (- n 1)) (- m 1))
          (let* ((item (pq-pop! pq))
                 (t (first item))
                 (i (second item))
                 (j (third item)))
            (if (> t (vector-ref (vector-ref dist i) j))
                (loop) ; outdated entry
                (if (and (= i (- n 1)) (= j (- m 1)))
                    t
                    (begin
                      (for ([dir '((1 0) (-1 0) (0 1) (0 -1))])
                        (define di (first dir))
                        (define dj (second dir))
                        (define ni (+ i di))
                        (define nj (+ j dj))
                        (when (and (>= ni 0) (< ni n) (>= nj 0) (< nj m))
                          (let* ((cell-time (list-ref (list-ref moveTime ni) nj))
                                 (newt (+ (max t cell-time) 1)))
                            (when (< newt (vector-ref (vector-ref dist ni) nj))
                              (vector-set! (vector-ref dist ni) nj newt)
                              (pq-add! pq (list newt ni nj)))))))
                      (loop)))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_time_to_reach/1]).

-define(INF, 1000000000000000000).

-spec min_time_to_reach(MoveTime :: [[integer()]]) -> integer().
min_time_to_reach(MoveTime) ->
    N = length(MoveTime),
    M = case MoveTime of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    DistMap0 = maps:put({0,0}, 0, #{}),
    Tree0 = gb_trees:insert({0,0,0}, true, gb_trees:empty()),
    dijkstra(Tree0, DistMap0, MoveTime, N, M).

dijkstra(Tree, DistMap, MoveTime, N, M) ->
    case gb_trees:is_empty(Tree) of
        true -> maps:get({N-1,M-1}, DistMap, -1);
        false ->
            {{Time,X,Y}, _Val, RestTree} = gb_trees:take_smallest(Tree),
            CurrentDist = maps:get({X,Y}, DistMap),
            if Time > CurrentDist ->
                    dijkstra(RestTree, DistMap, MoveTime, N, M);
               true ->
                    case {X == N-1, Y == M-1} of
                        {true, true} -> Time;
                        _ ->
                            Neighbors = [{X-1,Y},{X+1,Y},{X,Y-1},{X,Y+1}],
                            {NewTree, NewDistMap} = process_neighbors(Neighbors, Time, RestTree, DistMap, MoveTime, N, M),
                            dijkstra(NewTree, NewDistMap, MoveTime, N, M)
                    end
            end
    end.

process_neighbors([], _CurTime, Tree, DistMap, _MoveTime, _N, _M) ->
    {Tree, DistMap};
process_neighbors([{U,V}|Rest], CurTime, Tree, DistMap, MoveTime, N, M) ->
    if U >= 0, U < N, V >= 0, V < M ->
            CellTime = get_cell(MoveTime, U, V),
            NextTime = erlang:max(CurTime, CellTime) + 1,
            Existing = maps:get({U,V}, DistMap, ?INF),
            if NextTime < Existing ->
                    DistMap2 = maps:put({U,V}, NextTime, DistMap),
                    Tree2 = gb_trees:insert({NextTime,U,V}, true, Tree),
                    process_neighbors(Rest, CurTime, Tree2, DistMap2, MoveTime, N, M);
               true ->
                    process_neighbors(Rest, CurTime, Tree, DistMap, MoveTime, N, M)
            end;
       true ->
            process_neighbors(Rest, CurTime, Tree, DistMap, MoveTime, N, M)
    end.

get_cell(MoveTime, X, Y) ->
    Row = lists:nth(X+1, MoveTime),
    lists:nth(Y+1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time_to_reach(move_time :: [[integer]]) :: integer
  def min_time_to_reach(move_time) do
    n = length(move_time)
    m = move_time |> hd() |> length()
    inf = 1_000_000_000_000_000_000
    dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

    dist = %{{0, 0} => 0}
    queue = :gb_sets.singleton({0, 0, 0})

    get_time = fn i, j ->
      move_time |> Enum.at(i) |> Enum.at(j)
    end

    dijkstra(queue, dist, n, m, dirs, get_time, inf)
  end

  defp dijkstra(queue, dist, n, m, dirs, get_time, inf) do
    if :gb_sets.is_empty(queue) do
      -1
    else
      {{t, i, j}, queue} = :gb_sets.take_smallest(queue)

      cur_dist = Map.get(dist, {i, j}, inf)

      cond do
        t > cur_dist ->
          dijkstra(queue, dist, n, m, dirs, get_time, inf)

        i == n - 1 and j == m - 1 ->
          t

        true ->
          {new_dist, new_queue} =
            Enum.reduce(dirs, {dist, queue}, fn {dx, dy}, {d_acc, q_acc} ->
              ni = i + dx
              nj = j + dy

              if ni < 0 or ni >= n or nj < 0 or nj >= m do
                {d_acc, q_acc}
              else
                neighbor_time = get_time.(ni, nj)
                new_t = max(t, neighbor_time) + 1
                old = Map.get(d_acc, {ni, nj}, inf)

                if new_t < old do
                  d_new = Map.put(d_acc, {ni, nj}, new_t)
                  q_new = :gb_sets.add({new_t, ni, nj}, q_acc)
                  {d_new, q_new}
                else
                  {d_acc, q_acc}
                end
              end
            end)

          dijkstra(new_queue, new_dist, n, m, dirs, get_time, inf)
      end
    end
  end
end
```

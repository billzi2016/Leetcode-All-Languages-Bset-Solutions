# 3342. Find Minimum Time to Reach Last Room II

## Cpp

```cpp
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        const long long INF = LLONG_MAX / 4;
        vector<vector<long long>> dist(n, vector<long long>(m, INF));
        using Node = tuple<long long,int,int>;
        priority_queue<Node, vector<Node>, greater<Node>> pq;
        dist[0][0] = 0;
        pq.emplace(0LL, 0, 0);
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.empty()) {
            auto [d, x, y] = pq.top(); pq.pop();
            if (d != dist[x][y]) continue;
            if (x == n-1 && y == m-1) return (int)d;
            long long add = ((x + y) % 2) + 1; // cost of next move
            for (auto &dir : dirs) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                long long start = max(d, (long long)moveTime[nx][ny]);
                long long nd = start + add;
                if (nd < dist[nx][ny]) {
                    dist[nx][ny] = nd;
                    pq.emplace(nd, nx, ny);
                }
            }
        }
        return (int)dist[n-1][m-1];
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        long time;
        int i, j;
        Node(long t, int r, int c) {
            this.time = t;
            this.i = r;
            this.j = c;
        }
    }

    public int minTimeToReach(int[][] moveTime) {
        int n = moveTime.length;
        int m = moveTime[0].length;
        long INF = Long.MAX_VALUE / 4;
        long[][] dist = new long[n][m];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(dist[i], INF);
        }
        dist[0][0] = 0L;

        java.util.PriorityQueue<Node> pq = new java.util.PriorityQueue<>(
                (a, b) -> Long.compare(a.time, b.time));
        pq.offer(new Node(0L, 0, 0));

        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            long curTime = cur.time;
            int i = cur.i, j = cur.j;
            if (curTime != dist[i][j]) continue;
            if (i == n - 1 && j == m - 1) break;

            int stepCost = ((i + j) & 1) + 1; // 1 for even parity, 2 for odd
            for (int d = 0; d < 4; d++) {
                int ni = i + dr[d];
                int nj = j + dc[d];
                if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
                long start = Math.max(curTime, (long) moveTime[ni][nj]);
                long arrival = start + stepCost;
                if (arrival < dist[ni][nj]) {
                    dist[ni][nj] = arrival;
                    pq.offer(new Node(arrival, ni, nj));
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
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while heap:
            t, i, j = heapq.heappop(heap)
            if t != dist[i][j]:
                continue
            if i == n - 1 and j == m - 1:
                return t
            step_cost = ((i + j) & 1) + 1  # 1 if even parity, else 2
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    arrive = max(t, moveTime[ni][nj]) + step_cost
                    if arrive < dist[ni][nj]:
                        dist[ni][nj] = arrive
                        heapq.heappush(heap, (arrive, ni, nj))
        return dist[n - 1][m - 1]
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        INF = 10**18
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (time, i, j)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            cur, i, j = heapq.heappop(heap)
            if cur != dist[i][j]:
                continue
            if i == n - 1 and j == m - 1:
                return cur
            step_cost = (i + j) % 2 + 1  # 1 if even parity, 2 if odd
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    start_time = max(cur, moveTime[ni][nj])
                    arrival = start_time + step_cost
                    if arrival < dist[ni][nj]:
                        dist[ni][nj] = arrival
                        heapq.heappush(heap, (arrival, ni, nj))
        return dist[n - 1][m - 1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long d;
    int i;
    int j;
} Node;

static void heapSwap(Node *a, Node *b) {
    Node tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(Node *heap, int *size, Node val) {
    int idx = (*size)++;
    heap[idx] = val;
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (heap[parent].d <= heap[idx].d) break;
        heapSwap(&heap[parent], &heap[idx]);
        idx = parent;
    }
}

static Node heapPop(Node *heap, int *size) {
    Node top = heap[0];
    heap[0] = heap[--(*size)];
    int idx = 0;
    while (1) {
        int left = idx * 2 + 1;
        int right = left + 1;
        if (left >= *size) break;
        int smallest = left;
        if (right < *size && heap[right].d < heap[left].d)
            smallest = right;
        if (heap[idx].d <= heap[smallest].d) break;
        heapSwap(&heap[idx], &heap[smallest]);
        idx = smallest;
    }
    return top;
}

int minTimeToReach(int** moveTime, int moveTimeSize, int* moveTimeColSize){
    int n = moveTimeSize;
    int m = moveTimeColSize[0];
    long long INF = (1LL<<60);
    long long *dist = (long long*)malloc(sizeof(long long) * n * m);
    for (int i = 0; i < n*m; ++i) dist[i] = INF;
    dist[0] = 0;

    int capacity = n * m * 5;
    Node *heap = (Node*)malloc(sizeof(Node) * capacity);
    int heapSize = 0;
    heapPush(heap, &heapSize, (Node){0, 0, 0});

    const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

    while (heapSize) {
        Node cur = heapPop(heap, &heapSize);
        int i = cur.i, j = cur.j;
        long long d = cur.d;
        if (d != dist[i*m + j]) continue;
        if (i == n-1 && j == m-1) {
            free(dist);
            free(heap);
            return (int)d;
        }
        int parityCost = ((i + j) & 1) + 1; // 1 or 2
        for (int k = 0; k < 4; ++k) {
            int ni = i + dirs[k][0];
            int nj = j + dirs[k][1];
            if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
            long long start = d > moveTime[ni][nj] ? d : (long long)moveTime[ni][nj];
            long long nd = start + parityCost;
            int idx = ni*m + nj;
            if (nd < dist[idx]) {
                dist[idx] = nd;
                heapPush(heap, &heapSize, (Node){nd, ni, nj});
            }
        }
    }

    int ans = (int)dist[(n-1)*m + (m-1)];
    free(dist);
    free(heap);
    return ans;
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
        long[,] dist = new long[n, m];
        const long INF = long.MaxValue / 4;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dist[i, j] = INF;
            }
        }
        dist[0, 0] = 0;
        var pq = new PriorityQueue<(int i, int j), long>();
        pq.Enqueue((0, 0), 0);
        int[] dirs = new int[] { -1, 0, 1, 0, -1 };
        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int i = cur.i;
            int j = cur.j;
            long d = dist[i, j];
            if (i == n - 1 && j == m - 1) {
                return (int)d;
            }
            // Skip outdated entries
            // Since we don't store priority in the node, we rely on dist check after popping neighbors
            for (int k = 0; k < 4; k++) {
                int ni = i + dirs[k];
                int nj = j + dirs[k + 1];
                if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
                long wait = Math.Max(d, (long)moveTime[ni][nj]);
                int parity = (i + j) & 1; // 0 for odd move (cost 1), 1 for even move (cost 2)
                long nd = wait + parity + 1;
                if (nd < dist[ni, nj]) {
                    dist[ni, nj] = nd;
                    pq.Enqueue((ni, nj), nd);
                }
            }
        }
        return (int)dist[n - 1, m - 1];
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
    const dist = Array.from({ length: n }, () => new Array(m).fill(INF));
    dist[0][0] = 0;

    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
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
            const len = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let smallest = idx;
                if (left < len && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < len && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const heap = new MinHeap();
    heap.push([0, 0, 0]); // [time, i, j]

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];

    while (heap.size() > 0) {
        const [curTime, i, j] = heap.pop();
        if (curTime !== dist[i][j]) continue;
        if (i === n - 1 && j === m - 1) return curTime;

        const parityAdd = ((i + j) % 2) + 1; // 1 for even sum, 2 for odd sum

        for (const [dx, dy] of dirs) {
            const ni = i + dx;
            const nj = j + dy;
            if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;

            const startMove = Math.max(curTime, moveTime[ni][nj]);
            const nextTime = startMove + parityAdd;

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
                const parentIdx = (idx - 1) >> 1;
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
                let leftIdx = idx * 2 + 1;
                let rightIdx = idx * 2 + 2;
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

    const heap = new MinHeap();
    heap.push([0, 0, 0]); // [time, i, j]

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ];

    while (heap.size() > 0) {
        const cur = heap.pop()!;
        const time = cur[0];
        const i = cur[1];
        const j = cur[2];

        if (time !== dist[i][j]) continue;
        if (i === n - 1 && j === m - 1) return time;

        const travelCost = ((i + j) % 2 === 0) ? 1 : 2;

        for (const d of dirs) {
            const ni = i + d[0];
            const nj = j + d[1];
            if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
            const startMove = Math.max(time, moveTime[ni][nj]);
            const newTime = startMove + travelCost;
            if (newTime < dist[ni][nj]) {
                dist[ni][nj] = newTime;
                heap.push([newTime, ni, nj]);
            }
        }
    }

    return -1; // should never reach here as per problem guarantee
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
        $dist = array_fill(0, $n, array_fill(0, $m, $INF));
        $dist[0][0] = 0;

        $pq = new SplPriorityQueue();
        // SplPriorityQueue extracts highest priority first, so use negative time
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert([0, 0], 0); // priority 0 (negative of time 0)

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$pq->isEmpty()) {
            $elem = $pq->extract();
            $i = $elem['data'][0];
            $j = $elem['data'][1];
            $curTime = -$elem['priority']; // stored as negative

            if ($curTime != $dist[$i][$j]) {
                continue;
            }
            if ($i == $n-1 && $j == $m-1) {
                return $curTime;
            }

            $moveCost = (($i + $j) % 2 === 0) ? 1 : 2;

            foreach ($dirs as $d) {
                $ni = $i + $d[0];
                $nj = $j + $d[1];
                if ($ni < 0 || $ni >= $n || $nj < 0 || $nj >= $m) continue;
                $nextTime = max($curTime, $moveTime[$ni][$nj]) + $moveCost;
                if ($nextTime < $dist[$ni][$nj]) {
                    $dist[$ni][$nj] = $nextTime;
                    $pq->insert([$ni, $nj], -$nextTime);
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
    struct Node {
        var time: Int
        var x: Int
        var y: Int
    }
    
    class MinHeap {
        private var heap: [Node] = []
        
        func isEmpty() -> Bool {
            return heap.isEmpty
        }
        
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
            var child = index
            while child > 0 {
                let parent = (child - 1) >> 1
                if heap[child].time < heap[parent].time {
                    heap.swapAt(child, parent)
                    child = parent
                } else {
                    break
                }
            }
        }
        
        private func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < heap.count && heap[left].time < heap[smallest].time {
                    smallest = left
                }
                if right < heap.count && heap[right].time < heap[smallest].time {
                    smallest = right
                }
                if smallest == parent { break }
                heap.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }
    
    func minTimeToReach(_ moveTime: [[Int]]) -> Int {
        let n = moveTime.count
        let m = moveTime[0].count
        var dist = Array(repeating: Array(repeating: Int.max, count: m), count: n)
        let heap = MinHeap()
        dist[0][0] = 0
        heap.push(Node(time: 0, x: 0, y: 0))
        let dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while let cur = heap.pop() {
            let t = cur.time
            let i = cur.x
            let j = cur.y
            if t != dist[i][j] { continue }
            if i == n - 1 && j == m - 1 {
                return t
            }
            let edgeCost = ((i + j) & 1) == 0 ? 1 : 2
            for d in dirs {
                let ni = i + d.0
                let nj = j + d.1
                if ni < 0 || ni >= n || nj < 0 || nj >= m { continue }
                let start = max(t, moveTime[ni][nj])
                let newTime = start + edgeCost
                if newTime < dist[ni][nj] {
                    dist[ni][nj] = newTime
                    heap.push(Node(time: newTime, x: ni, y: nj))
                }
            }
        }
        return dist[n-1][m-1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    data class Node(val time: Long, val x: Int, val y: Int)

    fun minTimeToReach(moveTime: Array<IntArray>): Int {
        val n = moveTime.size
        val m = moveTime[0].size
        val total = n * m
        val INF = Long.MAX_VALUE / 4
        val dist = LongArray(total) { INF }
        fun idx(x: Int, y: Int) = x * m + y

        val pq = java.util.PriorityQueue<Node>(compareBy { it.time })
        dist[0] = 0L
        pq.add(Node(0L, 0, 0))

        val dirs = intArrayOf(-1, 0, 1, 0, -1)

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val dcur = cur.time
            val x = cur.x
            val y = cur.y
            if (dcur != dist[idx(x, y)]) continue
            if (x == n - 1 && y == m - 1) return dcur.toInt()

            val stepCost = ((x + y) % 2) + 1 // 1 or 2 seconds

            for (k in 0 until 4) {
                val nx = x + dirs[k]
                val ny = y + dirs[k + 1]
                if (nx !in 0 until n || ny !in 0 until m) continue

                var start = dcur
                val mt = moveTime[nx][ny].toLong()
                if (start < mt) start = mt
                val arrival = start + stepCost

                val nid = idx(nx, ny)
                if (arrival < dist[nid]) {
                    dist[nid] = arrival
                    pq.add(Node(arrival, nx, ny))
                }
            }
        }

        return dist[idx(n - 1, m - 1)].toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class MinHeap {
  final List<List<int>> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void push(List<int> item) {
    _heap.add(item);
    _siftUp(_heap.length - 1);
  }

  List<int> pop() {
    final top = _heap.first;
    final last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_heap[parent][0] <= _heap[idx][0]) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final n = _heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _heap[left][0] < _heap[smallest][0]) smallest = left;
      if (right < n && _heap[right][0] < _heap[smallest][0]) smallest = right;

      if (smallest == idx) break;
      _swap(idx, smallest);
      idx = smallest;
    }
  }

  void _swap(int i, int j) {
    final temp = _heap[i];
    _heap[i] = _heap[j];
    _heap[j] = temp;
  }
}

class Solution {
  int minTimeToReach(List<List<int>> moveTime) {
    final n = moveTime.length;
    final m = moveTime[0].length;
    const INF = 1 << 60;

    final dist = List.generate(n, (_) => List.filled(m, INF));
    dist[0][0] = 0;

    final heap = MinHeap();
    heap.push([0, 0, 0]); // [time, x, y]

    const dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    while (!heap.isEmpty) {
      final cur = heap.pop();
      final time = cur[0];
      final x = cur[1];
      final y = cur[2];

      if (time != dist[x][y]) continue;
      if (x == n - 1 && y == m - 1) return time;

      final moveCost = ((x + y) % 2) + 1; // 1 or 2 seconds

      for (final d in dirs) {
        final nx = x + d[0];
        final ny = y + d[1];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

        final startTime = max(time, moveTime[nx][ny]);
        final newDist = startTime + moveCost;
        if (newDist < dist[nx][ny]) {
          dist[nx][ny] = newDist;
          heap.push([newDist, nx, ny]);
        }
      }
    }

    return dist[n - 1][m - 1];
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
	t     int64
	x, y  int
	index int
}

type priorityQueue []item

func (pq priorityQueue) Len() int { return len(pq) }
func (pq priorityQueue) Less(i, j int) bool {
	return pq[i].t < pq[j].t
}
func (pq priorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}
func (pq *priorityQueue) Push(x interface{}) {
	it := x.(item)
	it.index = len(*pq)
	*pq = append(*pq, it)
}
func (pq *priorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[0 : n-1]
	return it
}

func minTimeToReach(moveTime [][]int) int {
	if len(moveTime) == 0 || len(moveTime[0]) == 0 {
		return 0
	}
	n, m := len(moveTime), len(moveTime[0])
	const INF int64 = 1<<63 - 1

	dist := make([][]int64, n)
	for i := range dist {
		dist[i] = make([]int64, m)
		for j := range dist[i] {
			dist[i][j] = INF
		}
	}
	dist[0][0] = 0

	pq := &priorityQueue{}
	heap.Init(pq)
	heap.Push(pq, item{t: 0, x: 0, y: 0})

	dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(item)
		if cur.t != dist[cur.x][cur.y] {
			continue
		}
		if cur.x == n-1 && cur.y == m-1 {
			return int(cur.t)
		}
		moveCost := (cur.x+cur.y)%2 + 1 // 1 or 2
		for _, d := range dir {
			nx, ny := cur.x+d[0], cur.y+d[1]
			if nx < 0 || nx >= n || ny < 0 || ny >= m {
				continue
			}
			start := cur.t
			if start < int64(moveTime[nx][ny]) {
				start = int64(moveTime[nx][ny])
			}
			newT := start + int64(moveCost)
			if newT < dist[nx][ny] {
				dist[nx][ny] = newT
				heap.Push(pq, item{t: newT, x: nx, y: ny})
			}
		}
	}
	return int(dist[n-1][m-1])
}
```

## Ruby

```ruby
def min_time_to_reach(move_time)
  n = move_time.size
  m = move_time[0].size
  inf = (1 << 60)

  dist = Array.new(n) { Array.new(m, inf) }
  dist[0][0] = 0

  class MinHeap
    def initialize
      @data = []
    end

    def push(item)
      @data << item
      idx = @data.size - 1
      while idx > 0
        parent = (idx - 1) / 2
        break if @data[parent][0] <= @data[idx][0]
        @data[parent], @data[idx] = @data[idx], @data[parent]
        idx = parent
      end
    end

    def pop
      return nil if @data.empty?
      top = @data[0]
      last = @data.pop
      unless @data.empty?
        @data[0] = last
        idx = 0
        n = @data.size
        loop do
          left = idx * 2 + 1
          right = left + 1
          smallest = idx
          smallest = left if left < n && @data[left][0] < @data[smallest][0]
          smallest = right if right < n && @data[right][0] < @data[smallest][0]
          break if smallest == idx
          @data[smallest], @data[idx] = @data[idx], @data[smallest]
          idx = smallest
        end
      end
      top
    end

    def empty?
      @data.empty?
    end
  end

  pq = MinHeap.new
  pq.push([0, 0, 0])

  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  until pq.empty?
    cur_time, i, j = pq.pop
    next if cur_time != dist[i][j]
    return cur_time if i == n - 1 && j == m - 1

    add = ((i + j) & 1) + 1
    dirs.each do |dx, dy|
      ni = i + dx
      nj = j + dy
      next unless ni.between?(0, n - 1) && nj.between?(0, m - 1)
      depart = cur_time > move_time[ni][nj] ? cur_time : move_time[ni][nj]
      new_time = depart + add
      if new_time < dist[ni][nj]
        dist[ni][nj] = new_time
        pq.push([new_time, ni, nj])
      end
    end
  end

  dist[n - 1][m - 1]
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.PriorityQueue

  case class Node(time: Long, x: Int, y: Int)

  def minTimeToReach(moveTime: Array[Array[Int]]): Int = {
    val n = moveTime.length
    val m = moveTime(0).length
    val INF = Long.MaxValue / 4
    val dist = Array.fill(n, m)(INF)
    dist(0)(0) = 0L

    implicit val ordering: Ordering[Node] = Ordering.by(-_.time)
    val pq = PriorityQueue.empty[Node]

    pq.enqueue(Node(0L, 0, 0))

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (pq.nonEmpty) {
      val cur = pq.dequeue()
      if (cur.time != dist(cur.x)(cur.y)) {
        // stale entry
      } else {
        if (cur.x == n - 1 && cur.y == m - 1) return cur.time.toInt

        val stepCost = ((cur.x + cur.y) % 2) + 1 // 1 or 2

        for ((dx, dy) <- dirs) {
          val nx = cur.x + dx
          val ny = cur.y + dy
          if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            val waitTime = math.max(cur.time, moveTime(nx)(ny).toLong)
            val newTime = waitTime + stepCost
            if (newTime < dist(nx)(ny)) {
              dist(nx)(ny) = newTime
              pq.enqueue(Node(newTime, nx, ny))
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
impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let n = move_time.len();
        let m = move_time[0].len();
        let mut dist = vec![vec![i64::MAX; m]; n];
        dist[0][0] = 0;

        let mut heap: BinaryHeap<(Reverse<i64>, usize, usize)> = BinaryHeap::new();
        heap.push((Reverse(0), 0, 0));

        let dirs = [(1_i32, 0_i32), (-1, 0), (0, 1), (0, -1)];

        while let Some((Reverse(cur), i, j)) = heap.pop() {
            if cur != dist[i][j] {
                continue;
            }
            if i == n - 1 && j == m - 1 {
                return cur as i32;
            }

            let step_cost = ((i + j) % 2) as i64 + 1;

            for &(dx, dy) in &dirs {
                let ni = i as i32 + dx;
                let nj = j as i32 + dy;
                if ni < 0 || nj < 0 {
                    continue;
                }
                let ni = ni as usize;
                let nj = nj as usize;
                if ni >= n || nj >= m {
                    continue;
                }

                let wait_start = if cur > move_time[ni][nj] as i64 {
                    cur
                } else {
                    move_time[ni][nj] as i64
                };
                let ndist = wait_start + step_cost;
                if ndist < dist[ni][nj] {
                    dist[ni][nj] = ndist;
                    heap.push((Reverse(ndist), ni, nj));
                }
            }
        }

        // Should never reach here because a path always exists
        dist[n - 1][m - 1] as i32
    }
}
```

## Racket

```racket
(require racket/heap)

(define INF (expt 2 60))

(define/contract (min-time-to-reach moveTime)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length moveTime))
         (m (if (= n 0) 0 (length (first moveTime))))
         (mt (list->vector (map list->vector moveTime)))
         (dist (make-vector n)))
    ;; initialize distance matrix
    (for ([i (in-range n)])
      (vector-set! dist i (make-vector m INF)))
    (vector-set! (vector-ref dist 0) 0 0)
    ;; priority queue: elements are (list time i j)
    (define (cmp a b) (< (first a) (first b)))
    (define pq (make-heap cmp))
    (heap-insert! pq (list 0 0 0))
    (let search ()
      (if (heap-empty? pq)
          (vector-ref (vector-ref dist (- n 1)) (- m 1))
          (let* ((node (heap-extract-min! pq))
                 (time (first node))
                 (i (second node))
                 (j (third node)))
            (if (> time (vector-ref (vector-ref dist i) j))
                (search)
                (if (and (= i (- n 1)) (= j (- m 1)))
                    time
                    (begin
                      (for ([dir '((1 0) (-1 0) (0 1) (0 -1))])
                        (let* ((ni (+ i (first dir)))
                               (nj (+ j (second dir))))
                          (when (and (>= ni 0) (< ni n)
                                     (>= nj 0) (< nj m))
                            (define wait (max time (vector-ref (vector-ref mt ni) nj)))
                            (define cost (+ (modulo (+ i j) 2) 1))
                            (define newt (+ wait cost))
                            (when (< newt (vector-ref (vector-ref dist ni) nj))
                              (vector-set! (vector-ref dist ni) nj newt)
                              (heap-insert! pq (list newt ni nj)))))))
                      (search)))))))))
```

## Erlang

```erlang
-spec min_time_to_reach(MoveTime :: [[integer()]]) -> integer().
min_time_to_reach(MoveTime) ->
    N = length(MoveTime),
    M = length(hd(MoveTime)),
    % build 2‑D array for O(1) access
    RowArrays = [array:from_list(Row) || Row <- MoveTime],
    Grid = array:from_list(RowArrays),

    GetMove = fun(I, J) ->
        RowArr = array:get(I, Grid),
        array:get(J, RowArr)
    end,

    Inf = 1 bsl 60,
    StartKey = {0,0},
    DistMap0 = maps:put(StartKey, 0, #{}),

    Heap0 = gb_sets:add({0,0,0}, gb_sets:new()),

    dijkstra(N, M, GetMove, Inf, Heap0, DistMap0).

dijkstra(N, M, GetMove, Inf, Heap, DistMap) ->
    case gb_sets:is_empty(Heap) of
        true -> 0; % should never happen
        false ->
            {{Dist, I, J}, RestHeap} = gb_sets:take_smallest(Heap),
            Key = {I,J},
            Stored = maps:get(Key, DistMap, Inf),
            if Dist > Stored ->
                    dijkstra(N, M, GetMove, Inf, RestHeap, DistMap);
               true ->
                    case I == N-1 andalso J == M-1 of
                        true -> Dist;
                        false ->
                            ParityAdd = ((I + J) band 1) + 1,
                            Neighs = [{I-1,J},{I+1,J},{I,J-1},{I,J+1}],
                            {NewHeap, NewDistMap} =
                                lists:foldl(
                                    fun({U,V}, {HAcc, DAcc}) ->
                                        if U >=0, U < N, V >=0, V < M ->
                                                MoveT = GetMove(U, V),
                                                NewDist = max(Dist, MoveT) + ParityAdd,
                                                NK = {U,V},
                                                OldDist = maps:get(NK, DAcc, Inf),
                                                if NewDist < OldDist ->
                                                        {gb_sets:add({NewDist,U,V}, HAcc),
                                                         maps:put(NK, NewDist, DAcc)};
                                                   true ->
                                                        {HAcc, DAcc}
                                                end;
                                           true -> {HAcc, DAcc}
                                        end
                                    end,
                                    {RestHeap, DistMap},
                                    Neighs),
                            dijkstra(N, M, GetMove, Inf, NewHeap, NewDistMap)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time_to_reach(move_time :: [[integer]]) :: integer
  def min_time_to_reach(move_time) do
    n = length(move_time)
    m = length(hd(move_time))
    size = n * m
    inf = 1 <<< 60

    flat = List.flatten(move_time)
    move_arr = :array.from_list(flat)

    start_idx = 0
    start_dist = max(0, :array.get(start_idx, move_arr))

    dist_arr =
      :array.new(size, default: inf)
      |> :array.set(start_idx, start_dist)

    heap = push(:gb_trees.empty(), start_dist, 0, 0)

    dijkstra(n, m, move_arr, dist_arr, heap)
  end

  defp dijkstra(n, m, move_arr, dist_arr, heap) do
    if :gb_trees.is_empty(heap) do
      raise "unreachable"
    else
      {{cur_dist, {i, j}}, heap2} = pop(heap)

      idx = i * m + j
      stored = :array.get(idx, dist_arr)

      cond do
        cur_dist != stored ->
          dijkstra(n, m, move_arr, dist_arr, heap2)

        i == n - 1 and j == m - 1 ->
          cur_dist

        true ->
          add = rem(i + j, 2) + 1

          {new_dist_arr, new_heap} =
            [{i + 1, j}, {i - 1, j}, {i, j + 1}, {i, j - 1}]
            |> Enum.reduce({dist_arr, heap2}, fn {ni, nj}, {darr, h} ->
              if ni < 0 or nj < 0 or ni >= n or nj >= m do
                {darr, h}
              else
                nidx = ni * m + nj
                move_t = :array.get(nidx, move_arr)
                wait = max(cur_dist, move_t)
                ndist = wait + add

                cur_best = :array.get(nidx, darr)

                if ndist < cur_best do
                  { :array.set(nidx, ndist, dar), push(h, ndist, ni, nj) }
                else
                  {darr, h}
                end
              end
            end)

          dijkstra(n, m, move_arr, new_dist_arr, new_heap)
      end
    end
  end

  defp push(tree, dist, i, j) do
    case :gb_trees.lookup(dist, tree) do
      {:ok, lst} -> :gb_trees.update(dist, [{i, j} | lst], tree)
      :none -> :gb_trees.insert(dist, [{i, j}], tree)
    end
  end

  defp pop(tree) do
    {dist, nodes, rest} = :gb_trees.take_smallest(tree)
    [head | tail] = nodes

    new_tree =
      case tail do
        [] -> rest
        _ -> :gb_trees.insert(dist, tail, rest)
      end

    {{dist, head}, new_tree}
  end
end
```

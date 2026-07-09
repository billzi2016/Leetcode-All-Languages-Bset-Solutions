# 3112. Minimum Time to Visit Disappearing Nodes

## Cpp

```cpp
class Solution {
public:
    vector<int> minimumTime(int n, vector<vector<int>>& edges, vector<int>& disappear) {
        const long long INF = 4e18;
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        vector<long long> dist(n, INF);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        if (0 < disappear[0]) {
            dist[0] = 0;
            pq.push({0, 0});
        }
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto &pr : adj[u]) {
                int v = pr.first;
                long long nd = d + pr.second;
                if (nd < disappear[v] && nd < dist[v]) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            ans[i] = (dist[i] == INF ? -1 : static_cast<int>(dist[i]));
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] minimumTime(int n, int[][] edges, int[] disappear) {
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        long INF = Long.MAX_VALUE / 4;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[0] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[1]));
        // store {node, distance}
        pq.offer(new long[]{0, 0});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            int u = (int) cur[0];
            long d = cur[1];
            if (d != dist[u]) continue;
            // No need to check disappearance for current node; it was validated when inserted
            for (int[] nb : graph[u]) {
                int v = nb[0];
                int w = nb[1];
                long nd = d + w;
                if (nd <= disappear[v] && nd < dist[v]) {
                    dist[v] = nd;
                    pq.offer(new long[]{v, nd});
                }
            }
        }

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = dist[i] == INF ? -1 : (int) dist[i];
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTime(self, n, edges, disappear):
        """
        :type n: int
        :type edges: List[List[int]]
        :type disappear: List[int]
        :rtype: List[int]
        """
        import heapq

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = 10**18
        dist = [INF] * n
        ans = [-1] * n

        # start from node 0 if it can be visited at time 0
        if 0 < disappear[0]:
            dist[0] = 0
            ans[0] = 0
            heap = [(0, 0)]
        else:
            heap = []

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            # cannot stay at node if arrival time is not strictly before disappearance
            if d >= disappear[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v] and nd < disappear[v]:
                    dist[v] = nd
                    ans[v] = nd
                    heapq.heappush(heap, (nd, v))

        return ans
```

## Python3

```python
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        import heapq
        INF = 10**18
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [INF] * n
        if 0 < disappear[0]:
            dist[0] = 0
            heap = [(0, 0)]
        else:
            # start node already disappeared; all unreachable
            return [-1] * n

        while heap:
            t, u = heapq.heappop(heap)
            if t != dist[u]:
                continue
            if t >= disappear[u]:
                continue
            for v, w in adj[u]:
                nt = t + w
                if nt < disappear[v] and nt < dist[v]:
                    dist[v] = nt
                    heapq.heappush(heap, (nt, v))

        return [d if d != INF else -1 for d in dist]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long dist;
    int node;
} HeapNode;

static void heapSwap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapNode *heap, int *size, long long dist, int node) {
    int i = (*size)++;
    heap[i].dist = dist;
    heap[i].node = node;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].dist <= heap[i].dist) break;
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
        if (r < n && heap[r].dist < heap[l].dist) smallest = r;
        if (heap[i].dist <= heap[smallest].dist) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

int* minimumTime(int n, int** edges, int edgesSize, int* edgesColSize,
                 int* disappear, int disappearSize, int* returnSize) {
    // Build adjacency list
    int m = edgesSize;
    int total = 2 * m;
    int *head = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    int *to = (int*)malloc(total * sizeof(int));
    int *weight = (int*)malloc(total * sizeof(int));
    int *next = (int*)malloc(total * sizeof(int));
    int idx = 0;
    for (int i = 0; i < m; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];
        to[idx] = v; weight[idx] = w; next[idx] = head[u]; head[u] = idx++;
        to[idx] = u; weight[idx] = w; next[idx] = head[v]; head[v] = idx++;
    }

    const long long INF = LLONG_MAX / 4;
    long long *dist = (long long*)malloc(n * sizeof(long long));
    for (int i = 0; i < n; ++i) dist[i] = INF;

    // Heap allocation
    int heapCap = total + n + 5;
    HeapNode *heap = (HeapNode*)malloc(heapCap * sizeof(HeapNode));
    int heapSize = 0;

    if (0 < disappear[0]) {
        dist[0] = 0;
        heapPush(heap, &heapSize, 0LL, 0);
    }

    while (heapSize) {
        HeapNode cur = heapPop(heap, &heapSize);
        long long d = cur.dist;
        int u = cur.node;
        if (d != dist[u]) continue;               // outdated entry
        if (d >= disappear[u]) continue;          // node already disappeared

        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            long long nd = d + weight[e];
            if (nd < dist[v] && nd < disappear[v]) {
                dist[v] = nd;
                heapPush(heap, &heapSize, nd, v);
            }
        }
    }

    // Prepare answer
    int *ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (dist[i] == INF || dist[i] >= disappear[i]) ans[i] = -1;
        else ans[i] = (int)dist[i];
    }

    *returnSize = n;

    // Clean up
    free(head);
    free(to);
    free(weight);
    free(next);
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
    public int[] MinimumTime(int n, int[][] edges, int[] disappear) {
        var graph = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].Add((v, w));
            graph[v].Add((u, w));
        }

        const long INF = long.MaxValue / 4;
        var dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[0] = 0;

        var pq = new PriorityQueue<int, long>();
        pq.Enqueue(0, 0);

        while (pq.Count > 0) {
            int u = pq.Dequeue();
            long d = dist[u];
            if (d >= disappear[u]) continue; // cannot stay or leave after disappearance
            foreach (var (v, w) in graph[u]) {
                long nd = d + w;
                if (nd < disappear[v] && nd < dist[v]) {
                    dist[v] = nd;
                    pq.Enqueue(v, nd);
                }
            }
        }

        var answer = new int[n];
        for (int i = 0; i < n; i++) {
            if (dist[i] == INF || dist[i] >= disappear[i]) answer[i] = -1;
            else answer[i] = (int)dist[i];
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} disappear
 * @return {number[]}
 */
var minimumTime = function(n, edges, disappear) {
    // Build adjacency list
    const adj = Array.from({length: n}, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    // Min-heap implementation
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(item) {
            const h = this.heap;
            h.push(item);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p][0] <= h[i][0]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return null;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = i * 2 + 2, smallest = i;
                    if (l < h.length && h[l][0] < h[smallest][0]) smallest = l;
                    if (r < h.length && h[r][0] < h[smallest][0]) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const ans = new Array(n).fill(-1);
    // Starting node 0 is reachable at time 0 if it disappears after time 0
    if (0 < disappear[0]) {
        ans[0] = 0;
        const heap = new MinHeap();
        heap.push([0, 0]);
        while (heap.size()) {
            const [dist, u] = heap.pop();
            if (dist !== ans[u]) continue; // outdated entry
            for (const [v, w] of adj[u]) {
                const nd = dist + w;
                if (nd < disappear[v] && (ans[v] === -1 || nd < ans[v])) {
                    ans[v] = nd;
                    heap.push([nd, v]);
                }
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimumTime(n: number, edges: number[][], disappear: number[]): number[] {
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const e of edges) {
        const u = e[0], v = e[1], w = e[2];
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    class MinHeap {
        private data: [number, number][] = [];
        size(): number { return this.data.length; }
        push(item: [number, number]): void {
            let i = this.data.length;
            this.data.push(item);
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.data[p][0] <= this.data[i][0]) break;
                [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
                i = p;
            }
        }
        pop(): [number, number] | undefined {
            if (this.data.length === 0) return undefined;
            const top = this.data[0];
            const last = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, smallest = i;
                    if (l < this.data.length && this.data[l][0] < this.data[smallest][0]) smallest = l;
                    if (r < this.data.length && this.data[r][0] < this.data[smallest][0]) smallest = r;
                    if (smallest === i) break;
                    [this.data[i], this.data[smallest]] = [this.data[smallest], this.data[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    const dist: number[] = new Array(n).fill(INF);
    const visited: boolean[] = new Array(n).fill(false);
    const heap = new MinHeap();

    if (0 < disappear[0]) {
        dist[0] = 0;
        heap.push([0, 0]);
    }

    while (heap.size()) {
        const cur = heap.pop()!;
        const d = cur[0], u = cur[1];
        if (visited[u]) continue;
        if (d >= disappear[u]) continue; // cannot stay at a disappeared node
        visited[u] = true;

        for (const edge of adj[u]) {
            const v = edge[0], w = edge[1];
            const nd = d + w;
            if (nd < dist[v] && nd < disappear[v]) {
                dist[v] = nd;
                heap.push([nd, v]);
            }
        }
    }

    const ans: number[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        ans[i] = dist[i] === INF ? -1 : dist[i];
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $disappear
     * @return Integer[]
     */
    function minimumTime($n, $edges, $disappear) {
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $len = $e[2];
            $adj[$u][] = [$v, $len];
            $adj[$v][] = [$u, $len];
        }

        // Initialize distances
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n, $INF);

        // Priority queue for Dijkstra (min-heap via negative priority)
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        // Start from node 0 if it can be visited
        if ($disappear[0] > 0) {
            $dist[0] = 0;
            $pq->insert([0, 0], 0); // priority = -distance (0)
        }

        while (!$pq->isEmpty()) {
            $item = $pq->extract(); // [node, distance]
            $u = $item[0];
            $d = $item[1];

            if ($d != $dist[$u]) {
                continue; // outdated entry
            }

            foreach ($adj[$u] as $edge) {
                $v = $edge[0];
                $len = $edge[1];
                $newDist = $d + $len;

                // Can only visit v if arrival time is strictly before its disappearance
                if ($newDist < $disappear[$v] && $newDist < $dist[$v]) {
                    $dist[$v] = $newDist;
                    $pq->insert([$v, $newDist], -$newDist);
                }
            }
        }

        // Build answer array
        $answer = [];
        for ($i = 0; $i < $n; ++$i) {
            $answer[$i] = ($dist[$i] === $INF) ? -1 : $dist[$i];
        }
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTime(_ n: Int, _ edges: [[Int]], _ disappear: [Int]) -> [Int] {
        var graph = Array(repeating: [(to: Int, w: Int)](), count: n)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            graph[u].append((to: v, w: w))
            graph[v].append((to: u, w: w))
        }
        
        var dist = Array(repeating: Int.max, count: n)
        dist[0] = 0
        
        let heap = MinHeap()
        heap.push((0, 0)) // (distance, node)
        
        while let top = heap.pop() {
            let d = top.0
            let u = top.1
            if d != dist[u] { continue }          // outdated entry
            if d > disappear[u] { continue }      // arrived after disappearance, cannot proceed
            
            for edge in graph[u] {
                let v = edge.to
                let nd = d + edge.w
                if nd < dist[v] && nd <= disappear[v] {
                    dist[v] = nd
                    heap.push((nd, v))
                }
            }
        }
        
        var answer = [Int](repeating: -1, count: n)
        for i in 0..<n {
            if dist[i] != Int.max {
                answer[i] = dist[i]
            }
        }
        return answer
    }
}

// Simple binary min-heap for (distance, node) pairs
private final class MinHeap {
    private var data: [(Int, Int)] = [] // (dist, node)
    
    func push(_ element: (Int, Int)) {
        data.append(element)
        siftUp(from: data.count - 1)
    }
    
    func pop() -> (Int, Int)? {
        guard !data.isEmpty else { return nil }
        if data.count == 1 {
            return data.removeLast()
        }
        let top = data[0]
        data[0] = data.removeLast()
        siftDown(from: 0)
        return top
    }
    
    private func siftUp(from index: Int) {
        var childIdx = index
        while childIdx > 0 {
            let parentIdx = (childIdx - 1) >> 1
            if data[childIdx].0 < data[parentIdx].0 {
                data.swapAt(childIdx, parentIdx)
                childIdx = parentIdx
            } else {
                break
            }
        }
    }
    
    private func siftDown(from index: Int) {
        var parentIdx = index
        while true {
            let leftIdx = parentIdx * 2 + 1
            let rightIdx = leftIdx + 1
            var smallestIdx = parentIdx
            
            if leftIdx < data.count && data[leftIdx].0 < data[smallestIdx].0 {
                smallestIdx = leftIdx
            }
            if rightIdx < data.count && data[rightIdx].0 < data[smallestIdx].0 {
                smallestIdx = rightIdx
            }
            if smallestIdx == parentIdx { break }
            data.swapAt(parentIdx, smallestIdx)
            parentIdx = smallestIdx
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTime(n: Int, edges: Array<IntArray>, disappear: IntArray): IntArray {
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        data class State(val dist: Long, val node: Int) : Comparable<State> {
            override fun compareTo(other: State): Int = dist.compareTo(other.dist)
        }

        val INF = Long.MAX_VALUE
        val dist = LongArray(n) { INF }
        dist[0] = 0L

        val pq = java.util.PriorityQueue<State>()
        pq.add(State(0L, 0))

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.dist != dist[cur.node]) continue
            // No need to check disappearance for current node because we only push valid distances
            for ((to, w) in adj[cur.node]) {
                val nd = cur.dist + w.toLong()
                if (nd < dist[to] && nd < disappear[to].toLong()) {
                    dist[to] = nd
                    pq.add(State(nd, to))
                }
            }
        }

        val answer = IntArray(n)
        for (i in 0 until n) {
            answer[i] = if (dist[i] == INF) -1 else dist[i].toInt()
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> minimumTime(int n, List<List<int>> edges, List<int> disappear) {
    // Build adjacency list
    List<List<List<int>>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      int w = e[2];
      adj[u].add([v, w]);
      adj[v].add([u, w]);
    }

    // Answer array initialized to -1
    List<int> ans = List.filled(n, -1);

    // Min-heap for Dijkstra
    final heap = _MinHeap();

    if (0 < disappear[0]) {
      ans[0] = 0;
      heap.push(0, 0);
    }

    while (!heap.isEmpty) {
      var cur = heap.pop();
      int d = cur.dist;
      int u = cur.node;

      // Skip outdated entries
      if (ans[u] != d) continue;

      for (var edge in adj[u]) {
        int v = edge[0];
        int w = edge[1];
        int nd = d + w;
        if (nd < disappear[v] && (ans[v] == -1 || nd < ans[v])) {
          ans[v] = nd;
          heap.push(nd, v);
        }
      }
    }

    return ans;
  }
}

class _Item {
  int dist;
  int node;
  _Item(this.dist, this.node);
}

class _MinHeap {
  final List<_Item> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void push(int dist, int node) {
    _heap.add(_Item(dist, node));
    _siftUp(_heap.length - 1);
  }

  _Item pop() {
    var top = _heap[0];
    var last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int i) {
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_heap[p].dist <= _heap[i].dist) break;
      var tmp = _heap[p];
      _heap[p] = _heap[i];
      _heap[i] = tmp;
      i = p;
    }
  }

  void _siftDown(int i) {
    int n = _heap.length;
    while (true) {
      int l = i * 2 + 1;
      int r = l + 1;
      int smallest = i;
      if (l < n && _heap[l].dist < _heap[smallest].dist) smallest = l;
      if (r < n && _heap[r].dist < _heap[smallest].dist) smallest = r;
      if (smallest == i) break;
      var tmp = _heap[i];
      _heap[i] = _heap[smallest];
      _heap[smallest] = tmp;
      i = smallest;
    }
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type edge struct {
	to   int
	cost int
}

type item struct {
	node int
	dist int64
}
type priorityQueue []item

func (pq priorityQueue) Len() int { return len(pq) }
func (pq priorityQueue) Less(i, j int) bool {
	return pq[i].dist < pq[j].dist
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

func minimumTime(n int, edges [][]int, disappear []int) []int {
	graph := make([][]edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		graph[u] = append(graph[u], edge{v, w})
		graph[v] = append(graph[v], edge{u, w})
	}

	const INF int64 = 1 << 60
	dist := make([]int64, n)
	for i := range dist {
		dist[i] = INF
	}
	dist[0] = 0

	pq := &priorityQueue{}
	heap.Push(pq, item{node: 0, dist: 0})

	for pq.Len() > 0 {
		it := heap.Pop(pq).(item)
		u, d := it.node, it.dist
		if d != dist[u] {
			continue
		}
		if int64(disappear[u]) <= d { // node already disappeared
			continue
		}
		for _, e := range graph[u] {
			nd := d + int64(e.cost)
			if nd < dist[e.to] && nd < int64(disappear[e.to]) {
				dist[e.to] = nd
				heap.Push(pq, item{node: e.to, dist: nd})
			}
		}
	}

	ans := make([]int, n)
	for i := 0; i < n; i++ {
		if i == 0 {
			ans[i] = 0
			continue
		}
		if dist[i] == INF {
			ans[i] = -1
		} else {
			ans[i] = int(dist[i])
		}
	}
	return ans
}
```

## Ruby

```ruby
def minimum_time(n, edges, disappear)
  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  dist = Array.new(n, Float::INFINITY)

  # Simple binary min-heap
  heap = []
  push = lambda do |pair|
    heap << pair
    i = heap.size - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p][0] <= heap[i][0]
      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  pop = lambda do
    return nil if heap.empty?
    min = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      i = 0
      nsize = heap.size
      loop do
        l = i * 2 + 1
        r = i * 2 + 2
        smallest = i
        smallest = l if l < nsize && heap[l][0] < heap[smallest][0]
        smallest = r if r < nsize && heap[r][0] < heap[smallest][0]
        break if smallest == i
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
      end
    end
    min
  end

  # start from node 0 if it can be visited at time 0
  if 0 <= disappear[0]
    dist[0] = 0
    push.call([0, 0])
  end

  until heap.empty?
    d, u = pop.call
    next if d != dist[u]          # outdated entry
    next if d > disappear[u]      # cannot stay after disappearance (safety)

    adj[u].each do |v, w|
      nd = d + w
      next if nd > disappear[v]
      if nd < dist[v]
        dist[v] = nd
        push.call([nd, v])
      end
    end
  end

  dist.map { |d| d == Float::INFINITY ? -1 : d.to_i }
end
```

## Scala

```scala
object Solution {
  def minimumTime(n: Int, edges: Array[Array[Int]], disappear: Array[Int]): Array[Int] = {
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[(Int, Int)]())
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      val u = e(0)
      val v = e(1)
      val w = e(2)
      adj(u).append((v, w))
      adj(v).append((u, w))
      i += 1
    }

    val INF: Long = Long.MaxValue / 4
    val dist = Array.fill[Long](n)(INF)
    if (0L < disappear(0).toLong) {
      dist(0) = 0L
    }

    import java.util.PriorityQueue
    val pq = new PriorityQueue[(Long, Int)]((a: (Long, Int), b: (Long, Int)) => java.lang.Long.compare(a._1, b._1))
    if (dist(0) == 0L) {
      pq.offer((0L, 0))
    }

    while (!pq.isEmpty) {
      val cur = pq.poll()
      val d = cur._1
      val u = cur._2
      if (d != dist(u)) {
        // outdated entry
      } else {
        var idx = 0
        val list = adj(u)
        while (idx < list.size) {
          val (v, w) = list(idx)
          val nd = d + w.toLong
          if (nd < dist(v) && nd < disappear(v).toLong) {
            dist(v) = nd
            pq.offer((nd, v))
          }
          idx += 1
        }
      }
    }

    val ans = new Array[Int](n)
    var j = 0
    while (j < n) {
      if (dist(j) == INF) ans(j) = -1
      else ans(j) = dist(j).toInt
      j += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_time(n: i32, edges: Vec<Vec<i32>>, disappear: Vec<i32>) -> Vec<i32> {
        let n_usize = n as usize;
        let mut graph: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as i64;
            graph[u].push((v, w));
            graph[v].push((u, w));
        }

        let mut dist: Vec<i64> = vec![i64::MAX / 4; n_usize];
        // start at node 0 if it hasn't disappeared yet
        if 0 < disappear[0] as i64 {
            dist[0] = 0;
        }
        let mut heap: BinaryHeap<(Reverse<i64>, usize)> = BinaryHeap::new();
        heap.push((Reverse(0_i64), 0));

        while let Some((Reverse(d), u)) = heap.pop() {
            if d != dist[u] {
                continue;
            }
            // cannot stay at a node that has already disappeared
            if d >= disappear[u] as i64 {
                continue;
            }
            for &(v, w) in &graph[u] {
                let nd = d + w;
                if nd < dist[v] && nd < disappear[v] as i64 {
                    dist[v] = nd;
                    heap.push((Reverse(nd), v));
                }
            }
        }

        let mut answer: Vec<i32> = vec![-1; n_usize];
        for i in 0..n_usize {
            if dist[i] < i64::MAX / 4 && dist[i] < disappear[i] as i64 {
                answer[i] = dist[i] as i32;
            }
        }
        answer
    }
}
```

## Racket

```racket
#lang racket
(require data/heap)

(define (minimum-time n edges disappear)
  (define adj (make-vector n '()))
  (for ([e edges])
    (let* ((u (list-ref e 0))
           (v (list-ref e 1))
           (len (list-ref e 2)))
      (vector-set! adj u (cons (list v len) (vector-ref adj u)))
      (vector-set! adj v (cons (list u len) (vector-ref adj v)))))
  (define INF (expt 2 60))
  (define dist (make-vector n INF))
  (vector-set! dist 0 0)
  (define pq (make-heap (lambda (a b) (< (first a) (first b)))))
  (heap-insert! pq (list 0 0))
  (let loop ()
    (when (not (heap-empty? pq))
      (define top (heap-extract-min! pq))
      (define d (first top))
      (define u (second top))
      (when (= d (vector-ref dist u))
        (for ([edge (vector-ref adj u)])
          (let* ((v (first edge))
                 (w (second edge))
                 (nd (+ d w)))
            (when (and (<= nd (list-ref disappear v))
                       (< nd (vector-ref dist v)))
              (vector-set! dist v nd)
              (heap-insert! pq (list nd v))))))
      (loop)))
  (for/list ([i (in-range n)])
    (let ((d (vector-ref dist i)))
      (if (= d INF) -1 d))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_time/3]).
-spec minimum_time(N :: integer(), Edges :: [[integer()]], Disappear :: [integer()]) -> [integer()].
minimum_time(N, Edges, Disappear) ->
    Adj = build_adj(Edges, #{}),
    DisArr = list_to_array(Disappear, N),
    Dist0 = array:set(0, 0, array:new(N, {default, -1})),
    Heap0 = gb_sets:add({0, 0}, gb_sets:new()),
    FinalDist = dijkstra(Heap0, Adj, DisArr, Dist0),
    [array:get(I, FinalDist) || I <- lists:seq(0, N-1)].

build_adj([], M) -> M;
build_adj([[U,V,W]|Rest], M) ->
    M1 = maps:update_with(U,
            fun(L) -> [{V,W}|L] end,
            [{V,W}], M),
    M2 = maps:update_with(V,
            fun(L) -> [{U,W}|L] end,
            [{U,W}], M1),
    build_adj(Rest, M2).

list_to_array(List, N) ->
    Arr0 = array:new(N, {default, 0}),
    lists:foldl(fun({Idx, Val}, Acc) -> array:set(Idx, Val, Acc) end,
                Arr0,
                lists:zip(lists:seq(0, N-1), List)).

dijkstra(Heap, Adj, DisArr, DistArr) ->
    case gb_sets:is_empty(Heap) of
        true -> DistArr;
        false ->
            {{Dist, Node}, Heap1} = gb_sets:take_smallest(Heap),
            CurDist = array:get(Node, DistArr),
            if CurDist =/= -1 andalso CurDist < Dist ->
                    dijkstra(Heap1, Adj, DisArr, DistArr);
               true ->
                    DisTime = array:get(Node, DisArr),
                    if Dist >= DisTime ->
                            dijkstra(Heap1, Adj, DisArr, DistArr);
                       true ->
                            Neighs = maps:get(Node, Adj, []),
                            {NewHeap, NewDist} = lists:foldl(
                                fun({Nei, W}, {HAcc, DAcc}) ->
                                    NewDist = Dist + W,
                                    NeiDis = array:get(Nei, DisArr),
                                    if NewDist < NeiDis ->
                                            Old = array:get(Nei, DAcc),
                                            if Old == -1 orelse NewDist < Old ->
                                                    D2 = array:set(Nei, NewDist, DAcc),
                                                    H2 = gb_sets:add({NewDist, Nei}, HAcc),
                                                    {H2, D2};
                                               true -> {HAcc, DAcc}
                                            end;
                                       true -> {HAcc, DAcc}
                                    end
                                end,
                                {Heap1, DistArr},
                                Neighs),
                            dijkstra(NewHeap, Adj, DisArr, NewDist)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time(n :: integer, edges :: [[integer]], disappear :: [integer]) :: [integer]
  def minimum_time(n, edges, disappear) do
    adj = :array.new(n, default: [])
    adj =
      Enum.reduce(edges, adj, fn [u, v, w], a ->
        a = :array.set(u, [{v, w} | :array.get(u, a)], a)
        a = :array.set(v, [{u, w} | :array.get(v, a)], a)
        a
      end)

    dist = %{0 => 0}
    heap = :gb_sets.add({0, 0}, :gb_sets.new())
    {dist, _} = do_dijkstra(adj, disappear, dist, heap)

    for i <- 0..(n - 1) do
      case Map.get(dist, i) do
        nil -> -1
        d when d < Enum.at(disappear, i) -> d
        _ -> -1
      end
    end
  end

  defp do_dijkstra(_adj, _disappear, dist, heap) when :gb_sets.is_empty(heap), do: {dist, heap}

  defp do_dijkstra(adj, disappear, dist, heap) do
    {{d, u}, heap_rest} = :gb_sets.take_smallest(heap)

    case Map.get(dist, u) do
      ^d ->
        neighs = :array.get(u, adj)

        {new_dist, new_heap} =
          Enum.reduce(neighs, {dist, heap_rest}, fn {v, w}, {dm, hp} ->
            nd = d + w

            if nd < Enum.at(disappear, v) do
              case Map.get(dm, v) do
                nil ->
                  {Map.put(dm, v, nd), :gb_sets.add({nd, v}, hp)}

                existing when nd < existing ->
                  {Map.put(dm, v, nd), :gb_sets.add({nd, v}, hp)}

                _ ->
                  {dm, hp}
              end
            else
              {dm, hp}
            end
          end)

        do_dijkstra(adj, disappear, new_dist, new_heap)

      _other ->
        do_dijkstra(adj, disappear, dist, heap_rest)
    end
  end
end
```

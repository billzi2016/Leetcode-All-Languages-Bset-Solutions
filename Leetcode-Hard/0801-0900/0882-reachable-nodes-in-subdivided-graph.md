# 0882. Reachable Nodes In Subdivided Graph

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], cnt = e[2];
            int w = cnt + 1;
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        const long long INF = (long long)4e18;
        vector<long long> dist(n, INF);
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        dist[0] = 0;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto &pr : adj[u]) {
                int v = pr.first, w = pr.second;
                long long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            if (dist[i] <= maxMoves) ++ans;
        }
        for (auto &e : edges) {
            int u = e[0], v = e[1], cnt = e[2];
            long long a = (dist[u] == INF) ? 0 : max(0LL, (long long)maxMoves - dist[u]);
            long long b = (dist[v] == INF) ? 0 : max(0LL, (long long)maxMoves - dist[v]);
            ans += min((long long)cnt, a + b);
        }
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int reachableNodes(int[][] edges, int maxMoves, int n) {
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], cnt = e[2];
            int w = cnt + 1;
            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        long INF = Long.MAX_VALUE / 4;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[0] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0L, 0L});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int node = (int) cur[1];
            if (d != dist[node]) continue;
            for (int[] nb : graph[node]) {
                int nei = nb[0];
                int w = nb[1];
                long nd = d + w;
                if (nd < dist[nei]) {
                    dist[nei] = nd;
                    pq.offer(new long[]{nd, nei});
                }
            }
        }

        long reachableOriginal = 0;
        for (int i = 0; i < n; i++) {
            if (dist[i] <= maxMoves) reachableOriginal++;
        }

        long ans = reachableOriginal;
        for (int[] e : edges) {
            int u = e[0], v = e[1], cnt = e[2];
            long fromU = dist[u] == INF ? 0 : Math.max(0, maxMoves - dist[u]);
            long fromV = dist[v] == INF ? 0 : Math.max(0, maxMoves - dist[v]);
            ans += Math.min(cnt, fromU + fromV);
        }

        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        """
        :type edges: List[List[int]]
        :type maxMoves: int
        :type n: int
        :rtype: int
        """
        import heapq

        # Build adjacency list with edge weight = cnt + 1 (number of moves to traverse whole edge)
        adj = [[] for _ in range(n)]
        for u, v, cnt in edges:
            w = cnt + 1
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = 10 ** 18
        dist = [INF] * n
        dist[0] = 0
        heap = [(0, 0)]

        # Dijkstra limited to distances <= maxMoves (farther nodes cannot contribute)
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            if d > maxMoves:   # no need to expand further from this node
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v] and nd <= maxMoves:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # Count original nodes reachable within maxMoves
        ans = sum(1 for d in dist if d != INF)

        # Add reachable subdivided nodes on each edge
        for u, v, cnt in edges:
            used_u = max(0, maxMoves - dist[u]) if dist[u] != INF else 0
            used_v = max(0, maxMoves - dist[v]) if dist[v] != INF else 0
            ans += min(cnt, used_u + used_v)

        return ans
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cnt in edges:
            w = cnt + 1
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        reachable_original = sum(1 for d in dist if d <= maxMoves)
        total = reachable_original

        for u, v, cnt in edges:
            used_u = 0
            used_v = 0
            if dist[u] != INF:
                used_u = max(0, maxMoves - dist[u])
            if dist[v] != INF:
                used_v = max(0, maxMoves - dist[v])
            total += min(cnt, used_u + used_v)

        return total
```

## C

```c
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

static void heapPush(HeapNode *heap, int *size, HeapNode val) {
    int i = ++(*size);
    heap[i] = val;
    while (i > 1 && heap[i].dist < heap[i >> 1].dist) {
        heapSwap(&heap[i], &heap[i >> 1]);
        i >>= 1;
    }
}

static HeapNode heapPop(HeapNode *heap, int *size) {
    HeapNode top = heap[1];
    heap[1] = heap[*size];
    (*size)--;
    int i = 1, n = *size;
    while (1) {
        int l = i << 1, r = l + 1, smallest = i;
        if (l <= n && heap[l].dist < heap[smallest].dist) smallest = l;
        if (r <= n && heap[r].dist < heap[smallest].dist) smallest = r;
        if (smallest == i) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

int reachableNodes(int** edges, int edgesSize, int* edgesColSize, int maxMoves, int n) {
    // adjacency list using arrays
    int totalEdges = edgesSize * 2;
    int *head = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;

    int *to = (int*)malloc(totalEdges * sizeof(int));
    int *weight = (int*)malloc(totalEdges * sizeof(int));
    int *cntArr = (int*)malloc(totalEdges * sizeof(int));
    int *next = (int*)malloc(totalEdges * sizeof(int));

    int idx = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int c = edges[i][2];
        int w = c + 1;

        // u -> v
        to[idx] = v;
        weight[idx] = w;
        cntArr[idx] = c;
        next[idx] = head[u];
        head[u] = idx++;
        // v -> u
        to[idx] = u;
        weight[idx] = w;
        cntArr[idx] = c;
        next[idx] = head[v];
        head[v] = idx++;
    }

    // Dijkstra
    long long *dist = (long long*)malloc(n * sizeof(long long));
    for (int i = 0; i < n; ++i) dist[i] = LLONG_MAX;
    dist[0] = 0;

    HeapNode *heap = (HeapNode*)malloc((n + totalEdges + 5) * sizeof(HeapNode));
    int heapSize = 0;
    heapPush(heap, &heapSize, (HeapNode){0LL, 0});

    while (heapSize) {
        HeapNode cur = heapPop(heap, &heapSize);
        long long d = cur.dist;
        int u = cur.node;
        if (d != dist[u]) continue;
        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            long long nd = d + weight[e];
            if (nd < dist[v]) {
                dist[v] = nd;
                heapPush(heap, &heapSize, (HeapNode){nd, v});
            }
        }
    }

    // count reachable original nodes
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        if (dist[i] <= maxMoves) ans++;
    }

    // add reachable subdivided nodes on each edge
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int c = edges[i][2];
        long long fromU = dist[u] <= maxMoves ? (long long)maxMoves - dist[u] : 0LL;
        long long fromV = dist[v] <= maxMoves ? (long long)maxMoves - dist[v] : 0LL;
        long long used = fromU + fromV;
        if (used > c) used = c;
        ans += used;
    }

    free(head);
    free(to);
    free(weight);
    free(cntArr);
    free(next);
    free(dist);
    free(heap);

    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int ReachableNodes(int[][] edges, int maxMoves, int n)
    {
        const long INF = long.MaxValue / 4;
        var graph = new List<(int to, int weight)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges)
        {
            int u = e[0], v = e[1], cnt = e[2];
            int w = cnt + 1;
            graph[u].Add((v, w));
            graph[v].Add((u, w));
        }

        var dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[0] = 0;

        var pq = new PriorityQueue<int, long>();
        pq.Enqueue(0, 0);

        while (pq.Count > 0)
        {
            int node = pq.Dequeue();
            long d = dist[node];
            // Since PriorityQueue does not provide priority on Dequeue,
            // we rely on stored distances; if outdated, skip.
            foreach (var (nei, w) in graph[node])
            {
                long nd = d + w;
                if (nd < dist[nei] && nd <= maxMoves)
                {
                    dist[nei] = nd;
                    pq.Enqueue(nei, nd);
                }
                else if (nd < dist[nei])
                {
                    // still update distance even if beyond maxMoves,
                    // because it may affect edge utilization later.
                    dist[nei] = nd;
                    pq.Enqueue(nei, nd);
                }
            }
        }

        long reachableOriginal = 0;
        for (int i = 0; i < n; i++)
            if (dist[i] <= maxMoves) reachableOriginal++;

        long extra = 0;
        foreach (var e in edges)
        {
            int u = e[0], v = e[1], cnt = e[2];
            long fromU = dist[u] <= maxMoves ? Math.Min(cnt, (long)maxMoves - dist[u]) : 0;
            long fromV = dist[v] <= maxMoves ? Math.Min(cnt, (long)maxMoves - dist[v]) : 0;
            extra += Math.Min(cnt, fromU + fromV);
        }

        return (int)(reachableOriginal + extra);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number} maxMoves
 * @param {number} n
 * @return {number}
 */
var reachableNodes = function(edges, maxMoves, n) {
    // Build adjacency list with weight = cnt + 1
    const adj = Array.from({length: n}, () => []);
    for (const [u, v, cnt] of edges) {
        const w = cnt + 1;
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

    const dist = new Array(n).fill(Infinity);
    dist[0] = 0;
    const heap = new MinHeap();
    heap.push([0, 0]);

    while (heap.size()) {
        const [d, u] = heap.pop();
        if (d !== dist[u]) continue; // outdated entry
        if (d > maxMoves) continue; // no need to explore further from this node
        for (const [v, w] of adj[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                heap.push([nd, v]);
            }
        }
    }

    let ans = 0;
    // count reachable original nodes
    for (let i = 0; i < n; ++i) {
        if (dist[i] <= maxMoves) ans += 1;
    }

    // add reachable subdivided nodes on each edge
    for (const [u, v, cnt] of edges) {
        const a = Math.max(0, maxMoves - dist[u]);
        const b = Math.max(0, maxMoves - dist[v]);
        ans += Math.min(cnt, a + b);
    }

    return ans;
};
```

## Typescript

```typescript
function reachableNodes(edges: number[][], maxMoves: number, n: number): number {
    // Build adjacency list with weight = cnt + 1
    const adj: Array<Array<[number, number]>> = Array.from({ length: n }, () => []);
    for (const [u, v, cnt] of edges) {
        const w = cnt + 1;
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    // Min-heap priority queue
    class MinHeap {
        private heap: Array<[number, number]> = [];
        push(item: [number, number]): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.sinkDown(0);
            }
            return top;
        }
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parentIdx = (idx - 1) >> 1;
                if (this.heap[parentIdx][0] <= this.heap[idx][0]) break;
                [this.heap[parentIdx], this.heap[idx]] = [this.heap[idx], this.heap[parentIdx]];
                idx = parentIdx;
            }
        }
        private sinkDown(idx: number): void {
            const length = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let smallest = idx;

                if (left < length && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < length && this.heap[right][0] < this.heap[smallest][0]) smallest = right;

                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
        isEmpty(): boolean {
            return this.heap.length === 0;
        }
    }

    // Dijkstra
    const dist: number[] = new Array(n).fill(Infinity);
    dist[0] = 0;
    const pq = new MinHeap();
    pq.push([0, 0]);

    while (!pq.isEmpty()) {
        const cur = pq.pop()!;
        const d = cur[0];
        const node = cur[1];
        if (d !== dist[node]) continue; // stale entry
        for (const [nei, w] of adj[node]) {
            const nd = d + w;
            if (nd < dist[nei]) {
                dist[nei] = nd;
                pq.push([nd, nei]);
            }
        }
    }

    // Count reachable original nodes
    let result = 0;
    for (let i = 0; i < n; ++i) {
        if (dist[i] <= maxMoves) result++;
    }

    // Add reachable subdivided nodes on each edge
    for (const [u, v, cnt] of edges) {
        const fromU = dist[u] <= maxMoves ? Math.max(0, maxMoves - dist[u]) : 0;
        const fromV = dist[v] <= maxMoves ? Math.max(0, maxMoves - dist[v]) : 0;
        result += Math.min(cnt, fromU + fromV);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer $maxMoves
     * @param Integer $n
     * @return Integer
     */
    function reachableNodes($edges, $maxMoves, $n) {
        // Build adjacency list with edge weight = cnt + 1
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $cnt] = $e;
            $w = $cnt + 1;
            $graph[$u][] = [$v, $w];
            $graph[$v][] = [$u, $w];
        }

        // Dijkstra's algorithm
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n, $INF);
        $dist[0] = 0;

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        // priority is negative distance to simulate min-heap
        $pq->insert([0, 0], 0);

        while (!$pq->isEmpty()) {
            $curr = $pq->extract(); // [node, currentDist]
            $node = $curr[0];
            $d = $curr[1];

            if ($d != $dist[$node]) {
                continue; // outdated entry
            }

            foreach ($graph[$node] as $edge) {
                [$nei, $weight] = $edge;
                $nd = $d + $weight;
                if ($nd < $dist[$nei]) {
                    $dist[$nei] = $nd;
                    $pq->insert([$nei, $nd], -$nd);
                }
            }
        }

        // Count reachable original nodes
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dist[$i] <= $maxMoves) {
                $ans++;
            }
        }

        // Add reachable subdivided nodes on each edge
        foreach ($edges as $e) {
            [$u, $v, $cnt] = $e;
            $remU = ($dist[$u] <= $maxMoves) ? $maxMoves - $dist[$u] : 0;
            $remV = ($dist[$v] <= $maxMoves) ? $maxMoves - $dist[$v] : 0;
            $used = min($cnt, $remU + $remV);
            $ans += $used;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func reachableNodes(_ edges: [[Int]], _ maxMoves: Int, _ n: Int) -> Int {
        var graph = Array(repeating: [(to: Int, weight: Int, cnt: Int)](), count: n)
        for e in edges {
            let u = e[0], v = e[1], cnt = e[2]
            let w = cnt + 1
            graph[u].append((to: v, weight: w, cnt: cnt))
            graph[v].append((to: u, weight: w, cnt: cnt))
        }
        
        var dist = Array(repeating: Int.max / 2, count: n)
        dist[0] = 0
        var heap = MinHeap()
        heap.push((0, 0))
        
        while let (d, u) = heap.pop() {
            if d != dist[u] { continue }
            for edge in graph[u] {
                let v = edge.to
                let nd = d + edge.weight
                if nd < dist[v] {
                    dist[v] = nd
                    heap.push((nd, v))
                }
            }
        }
        
        var reachableOriginal = 0
        for i in 0..<n where dist[i] <= maxMoves {
            reachableOriginal += 1
        }
        
        var extra = 0
        for e in edges {
            let u = e[0], v = e[1], cnt = e[2]
            var fromU = 0
            if dist[u] <= maxMoves {
                fromU = min(cnt, maxMoves - dist[u])
            }
            var fromV = 0
            if dist[v] <= maxMoves {
                fromV = min(cnt, maxMoves - dist[v])
            }
            extra += min(cnt, fromU + fromV)
        }
        
        return reachableOriginal + extra
    }
}

struct MinHeap {
    private var heap: [(Int, Int)] = [] // (dist, node)
    
    mutating func push(_ element: (Int, Int)) {
        heap.append(element)
        siftUp(heap.count - 1)
    }
    
    mutating func pop() -> (Int, Int)? {
        guard !heap.isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeLast()
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
            } else { break }
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
    fun reachableNodes(edges: Array<IntArray>, maxMoves: Int, n: Int): Int {
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val cnt = e[2]
            val w = cnt + 1
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        val INF = Long.MAX_VALUE / 4
        val dist = LongArray(n) { INF }
        dist[0] = 0L

        val pq = java.util.PriorityQueue<Pair<Long, Int>>(compareBy { it.first })
        pq.add(Pair(0L, 0))

        while (pq.isNotEmpty()) {
            val (d, node) = pq.poll()
            if (d != dist[node]) continue
            for ((nei, w) in adj[node]) {
                val nd = d + w
                if (nd < dist[nei]) {
                    dist[nei] = nd
                    pq.add(Pair(nd, nei))
                }
            }
        }

        var result = 0L
        val maxMovesL = maxMoves.toLong()
        for (d in dist) {
            if (d <= maxMovesL) result++
        }

        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val cnt = e[2].toLong()

            var usedFromU = 0L
            var usedFromV = 0L

            if (dist[u] <= maxMovesL) {
                usedFromU = kotlin.math.min(cnt, maxMovesL - dist[u])
            }
            if (dist[v] <= maxMovesL) {
                usedFromV = kotlin.math.min(cnt, maxMovesL - dist[v])
            }

            result += kotlin.math.min(cnt, usedFromU + usedFromV)
        }

        return result.toInt()
    }
}
```

## Dart

```dart
class Edge {
  int to;
  int w;
  Edge(this.to, this.w);
}

class HeapNode {
  int dist;
  int node;
  HeapNode(this.dist, this.node);
}

class MinHeap {
  final List<HeapNode> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(HeapNode x) {
    _data.add(x);
    _siftUp(_data.length - 1);
  }

  HeapNode pop() {
    var res = _data[0];
    var last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return res;
  }

  void _siftUp(int i) {
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_data[p].dist <= _data[i].dist) break;
      var tmp = _data[p];
      _data[p] = _data[i];
      _data[i] = tmp;
      i = p;
    }
  }

  void _siftDown(int i) {
    int n = _data.length;
    while (true) {
      int l = i * 2 + 1;
      int r = l + 1;
      int smallest = i;
      if (l < n && _data[l].dist < _data[smallest].dist) smallest = l;
      if (r < n && _data[r].dist < _data[smallest].dist) smallest = r;
      if (smallest == i) break;
      var tmp = _data[i];
      _data[i] = _data[smallest];
      _data[smallest] = tmp;
      i = smallest;
    }
  }
}

class Solution {
  int reachableNodes(List<List<int>> edges, int maxMoves, int n) {
    const int INF = 1 << 60;

    // Build graph with edge weight = cnt + 1
    List<List<Edge>> graph = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      int cnt = e[2];
      int w = cnt + 1;
      graph[u].add(Edge(v, w));
      graph[v].add(Edge(u, w));
    }

    // Dijkstra
    List<int> dist = List.filled(n, INF);
    dist[0] = 0;
    MinHeap heap = MinHeap();
    heap.push(HeapNode(0, 0));

    while (!heap.isEmpty) {
      var cur = heap.pop();
      if (cur.dist != dist[cur.node]) continue;
      for (var edge in graph[cur.node]) {
        int nd = cur.dist + edge.w;
        if (nd < dist[edge.to]) {
          dist[edge.to] = nd;
          heap.push(HeapNode(nd, edge.to));
        }
      }
    }

    // Count reachable original nodes
    int reachable = 0;
    for (int i = 0; i < n; ++i) {
      if (dist[i] <= maxMoves) reachable++;
    }

    // Add reachable subdivided nodes on each edge
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      int cnt = e[2];

      int usedFromU = 0;
      if (dist[u] != INF) {
        int rem = maxMoves - dist[u];
        if (rem > 0) usedFromU = rem > cnt ? cnt : rem;
      }

      int usedFromV = 0;
      if (dist[v] != INF) {
        int rem = maxMoves - dist[v];
        if (rem > 0) usedFromV = rem > cnt ? cnt : rem;
      }

      int totalOnEdge = usedFromU + usedFromV;
      reachable += totalOnEdge > cnt ? cnt : totalOnEdge;
    }

    return reachable;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type edgeInfo struct {
	to int
	w  int
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

func reachableNodes(edges [][]int, maxMoves int, n int) int {
	adj := make([][]edgeInfo, n)
	for _, e := range edges {
		u, v, cnt := e[0], e[1], e[2]
		w := cnt + 1
		adj[u] = append(adj[u], edgeInfo{v, w})
		adj[v] = append(adj[v], edgeInfo{u, w})
	}

	const INF int64 = 1 << 60
	dist := make([]int64, n)
	for i := range dist {
		dist[i] = INF
	}
	dist[0] = 0

	pq := &priorityQueue{}
	heap.Init(pq)
	heap.Push(pq, item{node: 0, dist: 0})

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(item)
		if cur.dist != dist[cur.node] {
			continue
		}
		for _, nb := range adj[cur.node] {
			nd := cur.dist + int64(nb.w)
			if nd < dist[nb.to] {
				dist[nb.to] = nd
				heap.Push(pq, item{node: nb.to, dist: nd})
			}
		}
	}

	ans := 0
	for i := 0; i < n; i++ {
		if dist[i] <= int64(maxMoves) {
			ans++
		}
	}

	for _, e := range edges {
		u, v, cnt := e[0], e[1], e[2]
		remU := int64(maxMoves) - dist[u]
		if remU < 0 {
			remU = 0
		}
		usedU := int(remU)
		if usedU > cnt {
			usedU = cnt
		}

		remV := int64(maxMoves) - dist[v]
		if remV < 0 {
			remV = 0
		}
		usedV := int(remV)
		if usedV > cnt {
			usedV = cnt
		}

		total := usedU + usedV
		if total > cnt {
			total = cnt
		}
		ans += total
	}

	return ans
}
```

## Ruby

```ruby
def reachable_nodes(edges, max_moves, n)
  adj = Array.new(n) { [] }
  edges.each do |u, v, cnt|
    w = cnt + 1
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

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
    def sift_up(i)
      while i > 0
        p = (i - 1) / 2
        break if @data[p][0] <= @data[i][0]
        @data[p], @data[i] = @data[i], @data[p]
        i = p
      end
    end
    def sift_down(i)
      n = @data.size
      loop do
        l = i * 2 + 1
        r = i * 2 + 2
        smallest = i
        if l < n && @data[l][0] < @data[smallest][0]
          smallest = l
        end
        if r < n && @data[r][0] < @data[smallest][0]
          smallest = r
        end
        break if smallest == i
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
  end

  dist = Array.new(n, Float::INFINITY)
  dist[0] = 0
  heap = MinHeap.new
  heap.push([0, 0])

  until heap.empty?
    d, u = heap.pop
    next if d > dist[u]
    adj[u].each do |v, w|
      nd = d + w
      if nd < dist[v]
        dist[v] = nd
        heap.push([nd, v])
      end
    end
  end

  ans = 0
  dist.each { |d| ans += 1 if d <= max_moves }

  edges.each do |u, v, cnt|
    used_u = dist[u] <= max_moves ? [cnt, max_moves - dist[u]].min : 0
    used_v = dist[v] <= max_moves ? [cnt, max_moves - dist[v]].min : 0
    ans += [cnt, used_u + used_v].min
  end

  ans
end
```

## Scala

```scala
object Solution {
  def reachableNodes(edges: Array[Array[Int]], maxMoves: Int, n: Int): Int = {
    val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer[(Int, Int)]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val cnt = e(2)
      val w = cnt + 1
      adj(u).append((v, w))
      adj(v).append((u, w))
    }

    import scala.collection.mutable.PriorityQueue
    val INF: Long = Long.MaxValue / 4
    val dist = Array.fill[Long](n)(INF)
    dist(0) = 0L

    implicit val ord: Ordering[(Long, Int)] = Ordering.by[(Long, Int), Long](_._1).reverse
    val pq = PriorityQueue.empty[(Long, Int)]
    pq.enqueue((0L, 0))

    while (pq.nonEmpty) {
      val (d, u) = pq.dequeue()
      if (d == dist(u)) {
        for ((v, w) <- adj(u)) {
          val nd = d + w
          if (nd < dist(v)) {
            dist(v) = nd
            pq.enqueue((nd, v))
          }
        }
      }
    }

    var result: Long = 0L
    val maxM = maxMoves.toLong

    for (i <- 0 until n) {
      if (dist(i) <= maxM) result += 1
    }

    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val cnt = e(2).toLong
      var a: Long = 0L
      var b: Long = 0L
      if (dist(u) != INF) a = math.max(0L, maxM - dist(u))
      if (dist(v) != INF) b = math.max(0L, maxM - dist(v))
      result += math.min(cnt, a + b)
    }

    result.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn reachable_nodes(edges: Vec<Vec<i32>>, max_moves: i32, n: i32) -> i32 {
        let n_usize = n as usize;
        let mut graph: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize];
        for e in &edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let cnt = e[2] as i64;
            let w = cnt + 1; // moves needed to traverse the whole edge
            graph[u].push((v, w));
            graph[v].push((u, w));
        }

        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        const INF: i64 = i64::MAX / 4;
        let mut dist = vec![INF; n_usize];
        dist[0] = 0;
        let mut heap = BinaryHeap::new();
        heap.push((Reverse(0_i64), 0usize));

        while let Some(((Reverse(d)), u)) = heap.pop() {
            if d != dist[u] {
                continue;
            }
            for &(v, w) in &graph[u] {
                let nd = d + w;
                if nd < dist[v] {
                    dist[v] = nd;
                    heap.push((Reverse(nd), v));
                }
            }
        }

        let max_moves_i64 = max_moves as i64;
        let mut ans: i64 = 0;

        // count original nodes reachable
        for &d in &dist {
            if d <= max_moves_i64 {
                ans += 1;
            }
        }

        // count subdivided nodes reachable on each edge
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let cnt = e[2] as i64;

            let mut used_u = 0_i64;
            if dist[u] <= max_moves_i64 {
                used_u = std::cmp::min(cnt, max_moves_i64 - dist[u]);
            }
            let mut used_v = 0_i64;
            if dist[v] <= max_moves_i64 {
                used_v = std::cmp::min(cnt, max_moves_i64 - dist[v]);
            }

            ans += std::cmp::min(cnt, used_u + used_v);
        }

        ans as i32
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (reachable-nodes edges maxMoves n)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  (let* ([adj (make-vector n '())]
         [edge-list edges])
    ;; build adjacency list
    (for-each (lambda (e)
                (define u (list-ref e 0))
                (define v (list-ref e 1))
                (define cnt (list-ref e 2))
                (vector-set! adj u (cons (list v cnt) (vector-ref adj u)))
                (vector-set! adj v (cons (list u cnt) (vector-ref adj v))))
              edge-list)
    ;; Dijkstra's algorithm on original nodes
    (define dist (make-vector n (expt 2 60))) ; large sentinel
    (vector-set! dist 0 0)
    (define heap (make-heap (lambda (a b) (< (first a) (first b)))))
    (heap-add! heap (list 0 0)) ; (distance node)
    (let recur ()
      (unless (heap-empty? heap)
        (define cur (heap-min heap))
        (heap-remove! heap)
        (define d (first cur))
        (define u (second cur))
        (when (= d (vector-ref dist u))
          (for-each (lambda (nbr)
                      (define v (first nbr))
                      (define cnt (second nbr))
                      (define nd (+ d cnt 1))
                      (when (< nd (vector-ref dist v))
                        (vector-set! dist v nd)
                        (heap-add! heap (list nd v))))
                    (vector-ref adj u)))
        (recur)))
    ;; count reachable original nodes
    (define reachable-original
      (for/sum ([i (in-range n)])
        (if (<= (vector-ref dist i) maxMoves) 1 0)))
    ;; count reachable subdivided nodes on each edge
    (define used-intermediate
      (for/sum ([e edge-list])
        (let* ((u (list-ref e 0))
               (v (list-ref e 1))
               (cnt (list-ref e 2))
               (du (vector-ref dist u))
               (dv (vector-ref dist v))
               (use-u (if (> du maxMoves) 0 (min cnt (- maxMoves du))))
               (use-v (if (> dv maxMoves) 0 (min cnt (- maxMoves dv)))))
          (min cnt (+ use-u use-v)))))
    (+ reachable-original used-intermediate)))
```

## Erlang

```erlang
-module(solution).
-export([reachable_nodes/3]).

-spec reachable_nodes(Edges :: [[integer()]], MaxMoves :: integer(), N :: integer()) -> integer().
reachable_nodes(Edges, MaxMoves, _N) ->
    Adj = build_adj(Edges),
    DistMap = dijkstra(Adj),
    %% count original nodes reachable
    ReachableOriginal =
        maps:fold(fun(_Node, Dist, Acc) ->
                          if Dist =< MaxMoves -> Acc + 1; true -> Acc end
                  end, 0, DistMap),
    %% count reachable subdivided nodes on each edge
    EdgeReach =
        lists:foldl(fun([U, V, Cnt], Acc) ->
                            Du = maps:get(U, DistMap, inf()),
                            Dv = maps:get(V, DistMap, inf()),
                            UsedU = if Du =< MaxMoves -> MaxMoves - Du; true -> 0 end,
                            UsedV = if Dv =< MaxMoves -> MaxMoves - Dv; true -> 0 end,
                            ReachEdge = erlang:min(Cnt, UsedU + UsedV),
                            Acc + ReachEdge
                    end, 0, Edges),
    ReachableOriginal + EdgeReach.

%% Build adjacency map: Node => [{Neighbor, Weight}]
build_adj(Edges) ->
    lists:foldl(fun([U, V, Cnt], Acc) ->
                        W = Cnt + 1,
                        Acc1 = maps:update_with(U,
                                                fun(L) -> [{V, W} | L] end,
                                                [{V, W}],
                                                Acc),
                        maps:update_with(V,
                                         fun(L) -> [{U, W} | L] end,
                                         [{U, W}],
                                         Acc1)
                end, #{}, Edges).

%% Dijkstra's algorithm on the original graph
dijkstra(Adj) ->
    INF = inf(),
    Dist0 = maps:from_list([{0, 0}]),
    Set0 = gb_sets:add_element({0, 0}, gb_sets:new()),
    dijkstra_loop(Set0, Adj, Dist0, INF).

dijkstra_loop(Set, _Adj, DistMap, _INF) when gb_sets:is_empty(Set) ->
    DistMap;
dijkstra_loop(Set, Adj, DistMap, INF) ->
    {Dist, Node} = gb_sets:smallest(Set),
    Set1 = gb_sets:del_element({Dist, Node}, Set),
    case maps:get(Node, DistMap) of
        CurrentDist when Dist > CurrentDist ->
            dijkstra_loop(Set1, Adj, DistMap, INF);
        _ ->
            Neighbors = maps:get(Node, Adj, []),
            {Set2, DistMap2} =
                lists:foldl(fun({Nei, Weight}, {SAcc, DAcc}) ->
                                    NewDist = Dist + Weight,
                                    OldDist = maps:get(Nei, DAcc, INF),
                                    if NewDist < OldDist ->
                                            DNew = maps:put(Nei, NewDist, DAcc),
                                            SNew = gb_sets:add_element({NewDist, Nei}, SAcc),
                                            {SNew, DNew};
                                       true ->
                                            {SAcc, DAcc}
                                    end
                            end,
                            {Set1, DistMap},
                            Neighbors),
            dijkstra_loop(Set2, Adj, DistMap2, INF)
    end.

inf() -> 1 bsl 60.
```

## Elixir

```elixir
defmodule Solution do
  @spec reachable_nodes(edges :: [[integer]], max_moves :: integer, n :: integer) :: integer
  def reachable_nodes(edges, max_moves, n) do
    {adj, _} =
      Enum.reduce(edges, {%{}, []}, fn [u, v, cnt], {adj_acc, list} ->
        w = cnt + 1

        adj_acc =
          Map.update(adj_acc, u, [{v, w}], fn l -> [{v, w} | l] end)

        adj_acc =
          Map.update(adj_acc, v, [{u, w}], fn l -> [{u, w} | l] end)

        {adj_acc, list}
      end)

    dist = dijkstra(n, adj, max_moves)

    reachable_original =
      Enum.count(dist, fn {_node, d} -> d <= max_moves end)

    total =
      Enum.reduce(edges, reachable_original, fn [u, v, cnt], acc ->
        du = Map.get(dist, u)
        dv = Map.get(dist, v)

        used_u = if du <= max_moves, do: max_moves - du, else: 0
        used_v = if dv <= max_moves, do: max_moves - dv, else: 0

        acc + min(cnt, used_u + used_v)
      end)

    total
  end

  defp dijkstra(n, adj, max_moves) do
    inf = 1 <<< 60

    dist =
      Enum.reduce(0..(n - 1), %{}, fn i, m ->
        Map.put(m, i, inf)
      end)
      |> Map.put(0, 0)

    set = :gb_sets.singleton({0, 0})
    dijkstra_loop(set, dist, adj, max_moves)
  end

  defp dijkstra_loop(set, dist, adj, max_moves) do
    if :gb_sets.is_empty(set) do
      dist
    else
      {{d, node}, set_rest} = :gb_sets.take_smallest(set)

      cur = Map.get(dist, node)

      if d != cur do
        dijkstra_loop(set_rest, dist, adj, max_moves)
      else
        {new_set, new_dist} =
          Enum.reduce(Map.get(adj, node, []), {set_rest, dist}, fn {nei, weight},
                                                                 {s, dm} ->
            nd = d + weight

            if nd < Map.get(dm, nei) and nd <= max_moves do
              dm2 = Map.put(dm, nei, nd)
              s2 = :gb_sets.add({nd, nei}, s)
              {s2, dm2}
            else
              {s, dm}
            end
          end)

        dijkstra_loop(new_set, new_dist, adj, max_moves)
      end
    end
  end
end
```

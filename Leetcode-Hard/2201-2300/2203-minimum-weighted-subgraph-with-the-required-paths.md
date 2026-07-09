# 2203. Minimum Weighted Subgraph With the Required Paths

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<long long> dijkstra(int start, const vector<vector<pair<int,int>>>& adj) {
        const long long INF = (1LL<<60);
        int n = adj.size();
        vector<long long> dist(n, INF);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        dist[start] = 0;
        pq.emplace(0LL, start);
        while (!pq.empty()) {
            auto [d,u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto [v,w] : adj[u]) {
                long long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.emplace(nd, v);
                }
            }
        }
        return dist;
    }

    long long minimumWeight(int n, vector<vector<int>>& edges, int src1, int src2, int dest) {
        vector<vector<pair<int,int>>> adj(n), revAdj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v,w});
            revAdj[v].push_back({u,w}); // reverse edge
        }
        auto d1 = dijkstra(src1, adj);
        auto d2 = dijkstra(src2, adj);
        auto dr = dijkstra(dest, revAdj); // distances to dest in original graph

        const long long INF = (1LL<<60);
        long long ans = INF;
        for (int v = 0; v < n; ++v) {
            if (d1[v] == INF || d2[v] == INF || dr[v] == INF) continue;
            long long total = d1[v] + d2[v] + dr[v];
            if (total < ans) ans = total;
        }
        return ans == INF ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    private static final long INF = Long.MAX_VALUE / 4;

    public long minimumWeight(int n, int[][] edges, int src1, int src2, int dest) {
        @SuppressWarnings("unchecked")
        java.util.List<int[]>[] graph = new java.util.ArrayList[n];
        @SuppressWarnings("unchecked")
        java.util.List<int[]>[] revGraph = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new java.util.ArrayList<>();
            revGraph[i] = new java.util.ArrayList<>();
        }
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].add(new int[]{v, w});
            revGraph[v].add(new int[]{u, w}); // reversed edge
        }

        long[] dFromSrc1 = dijkstra(n, src1, graph);
        long[] dFromSrc2 = dijkstra(n, src2, graph);
        long[] dToDest   = dijkstra(n, dest, revGraph); // distances to dest in original graph

        long ans = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (dFromSrc1[i] == INF || dFromSrc2[i] == INF || dToDest[i] == INF) continue;
            long total = dFromSrc1[i] + dFromSrc2[i] + dToDest[i];
            if (total < ans) ans = total;
        }
        return ans == Long.MAX_VALUE ? -1 : ans;
    }

    private long[] dijkstra(int n, int start, java.util.List<int[]>[] adj) {
        long[] dist = new long[n];
        java.util.Arrays.fill(dist, INF);
        dist[start] = 0L;
        java.util.PriorityQueue<long[]> pq = new java.util.PriorityQueue<>(
                (a, b) -> Long.compare(a[0], b[0])
        );
        pq.offer(new long[]{0L, start});
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int u = (int) cur[1];
            if (d != dist[u]) continue;
            for (int[] edge : adj[u]) {
                int v = edge[0];
                int w = edge[1];
                long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.offer(new long[]{nd, v});
                }
            }
        }
        return dist;
    }
}
```

## Python

```python
class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """
        import heapq

        INF = 10**18

        # build adjacency lists for forward and reverse graphs
        graph = [[] for _ in range(n)]
        rev_graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))

        def dijkstra(start, g):
            dist = [INF] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in g[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist

        # distances from src1 and src2 using forward graph
        d1 = dijkstra(src1, graph)
        d2 = dijkstra(src2, graph)
        # distances to dest: run Dijkstra from dest on reversed graph
        d3 = dijkstra(dest, rev_graph)

        ans = INF
        for v in range(n):
            total = d1[v] + d2[v] + d3[v]
            if total < ans:
                ans = total

        return -1 if ans >= INF else ans
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        INF = 10**18
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            rg[v].append((u, w))

        def dijkstra(start: int) -> List[int]:
            dist = [INF] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in g[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist

        def dijkstra_rev(start: int) -> List[int]:
            dist = [INF] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in rg[u]:   # edge v -> u in original graph
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist

        d1 = dijkstra(src1)
        d2 = dijkstra(src2)
        dr = dijkstra_rev(dest)

        ans = INF
        for i in range(n):
            total = d1[i] + d2[i] + dr[i]
            if total < ans:
                ans = total

        return -1 if ans == INF else ans
```

## C

```c
#include <limits.h>
#include <stdlib.h>

typedef struct {
    int to;
    int w;
    int next;
} Edge;

static void heapSwap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

typedef struct {
    long long dist;
    int node;
} HeapNode;

static void heapPush(HeapNode *heap, int *size, int node, long long dist) {
    int i = ++(*size);
    heap[i].node = node;
    heap[i].dist = dist;
    while (i > 1 && heap[i].dist < heap[i >> 1].dist) {
        heapSwap(&heap[i], &heap[i >> 1]);
        i >>= 1;
    }
}

static HeapNode heapPop(HeapNode *heap, int *size) {
    HeapNode top = heap[1];
    heap[1] = heap[(*size)--];
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

static long long* dijkstra(int n, int src, int *head, Edge *edges) {
    const long long INF = LLONG_MAX / 4;
    long long *dist = (long long*)malloc(n * sizeof(long long));
    for (int i = 0; i < n; ++i) dist[i] = INF;
    dist[src] = 0;

    int heapCap = n + 5;
    HeapNode *heap = (HeapNode*)malloc(heapCap * sizeof(HeapNode));
    int heapSize = 0;
    heapPush(heap, &heapSize, src, 0);

    while (heapSize) {
        HeapNode cur = heapPop(heap, &heapSize);
        long long d = cur.dist;
        int u = cur.node;
        if (d != dist[u]) continue;
        for (int e = head[u]; e != -1; e = edges[e].next) {
            int v = edges[e].to;
            long long nd = d + edges[e].w;
            if (nd < dist[v]) {
                dist[v] = nd;
                heapPush(heap, &heapSize, v, nd);
            }
        }
    }

    free(heap);
    return dist;
}

long long minimumWeight(int n, int** edges, int edgesSize, int* edgesColSize,
                        int src1, int src2, int dest) {
    (void)edgesColSize; // unused

    Edge *fwd = (Edge*)malloc(edgesSize * sizeof(Edge));
    Edge *rev = (Edge*)malloc(edgesSize * sizeof(Edge));
    int *headF = (int*)calloc(n, sizeof(int));
    int *headR = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) {
        headF[i] = -1;
        headR[i] = -1;
    }

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];

        fwd[i].to = v;
        fwd[i].w = w;
        fwd[i].next = headF[u];
        headF[u] = i;

        rev[i].to = u;
        rev[i].w = w;
        rev[i].next = headR[v];
        headR[v] = i;
    }

    long long *dist1 = dijkstra(n, src1, headF, fwd);
    long long *dist2 = dijkstra(n, src2, headF, fwd);
    long long *distD = dijkstra(n, dest, headR, rev);

    const long long INF = LLONG_MAX / 4;
    long long ans = INF;
    for (int i = 0; i < n; ++i) {
        if (dist1[i] == INF || dist2[i] == INF || distD[i] == INF) continue;
        long long total = dist1[i] + dist2[i] + distD[i];
        if (total < ans) ans = total;
    }

    free(fwd);
    free(rev);
    free(headF);
    free(headR);
    free(dist1);
    free(dist2);
    free(distD);

    return (ans == INF) ? -1 : ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MinimumWeight(int n, int[][] edges, int src1, int src2, int dest) {
        var graph = new List<(int to, int w)>[n];
        var revGraph = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new List<(int to, int w)>();
            revGraph[i] = new List<(int to, int w)>();
        }
        foreach (var e in edges) {
            int from = e[0], to = e[1], w = e[2];
            graph[from].Add((to, w));
            revGraph[to].Add((from, w));
        }

        var d1 = Dijkstra(n, graph, src1);
        var d2 = Dijkstra(n, graph, src2);
        var dDest = Dijkstra(n, revGraph, dest); // distances to dest

        const long INF = long.MaxValue / 4;
        long ans = INF;
        for (int i = 0; i < n; i++) {
            if (d1[i] == INF || d2[i] == INF || dDest[i] == INF) continue;
            long total = d1[i] + d2[i] + dDest[i];
            if (total < ans) ans = total;
        }
        return ans == INF ? -1 : ans;
    }

    private static long[] Dijkstra(int n, List<(int to, int w)>[] adj, int start) {
        const long INF = long.MaxValue / 4;
        var dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[start] = 0;

        var pq = new PriorityQueue<(int node, long dist), long>();
        pq.Enqueue((start, 0L), 0L);

        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int u = cur.node;
            long d = cur.dist;
            if (d != dist[u]) continue;

            foreach (var edge in adj[u]) {
                int v = edge.to;
                long nd = d + edge.w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.Enqueue((v, nd), nd);
                }
            }
        }

        return dist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} src1
 * @param {number} src2
 * @param {number} dest
 * @return {number}
 */
var minimumWeight = function (n, edges, src1, src2, dest) {
    const graph = Array.from({ length: n }, () => []);
    const revGraph = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        revGraph[v].push([u, w]); // reverse edge
    }

    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(item) {
            this.heap.push(item);
            this._up(this.heap.length - 1);
        }
        pop() {
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length) {
                this.heap[0] = end;
                this._down(0);
            }
            return top;
        }
        _up(idx) {
            while (idx > 0) {
                const p = (idx - 1) >> 1;
                if (this.heap[p][0] <= this.heap[idx][0]) break;
                [this.heap[p], this.heap[idx]] = [this.heap[idx], this.heap[p]];
                idx = p;
            }
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
                [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
                idx = smallest;
            }
        }
    }

    const dijkstra = (start, g) => {
        const dist = new Array(n).fill(Infinity);
        dist[start] = 0;
        const pq = new MinHeap();
        pq.push([0, start]);
        while (pq.size()) {
            const [d, u] = pq.pop();
            if (d !== dist[u]) continue;
            for (const [v, w] of g[u]) {
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push([nd, v]);
                }
            }
        }
        return dist;
    };

    const d1 = dijkstra(src1, graph);
    const d2 = dijkstra(src2, graph);
    const d3 = dijkstra(dest, revGraph); // distances to dest

    let ans = Infinity;
    for (let i = 0; i < n; ++i) {
        const a = d1[i], b = d2[i], c = d3[i];
        if (a === Infinity || b === Infinity || c === Infinity) continue;
        const total = a + b + c;
        if (total < ans) ans = total;
    }
    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
class MinHeap {
    heap: [number, number][];
    constructor() {
        this.heap = [];
    }
    size(): number {
        return this.heap.length;
    }
    push(item: [number, number]): void {
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
    pop(): [number, number] {
        const top = this.heap[0];
        const end = this.heap.pop()!;
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.bubbleDown(0);
        }
        return top;
    }
    bubbleDown(idx: number): void {
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
}

function minimumWeight(n: number, edges: number[][], src1: number, src2: number, dest: number): number {
    const adj: Array<[number, number][]> = Array.from({ length: n }, () => []);
    const revAdj: Array<[number, number][]> = Array.from({ length: n }, () => []);

    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        revAdj[v].push([u, w]); // reverse edge
    }

    const INF = Number.MAX_SAFE_INTEGER;

    function dijkstra(start: number, graph: Array<[number, number][]>): number[] {
        const dist = new Array<number>(n).fill(INF);
        dist[start] = 0;
        const heap = new MinHeap();
        heap.push([0, start]);

        while (heap.size()) {
            const [d, u] = heap.pop();
            if (d !== dist[u]) continue;
            for (const [v, w] of graph[u]) {
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    heap.push([nd, v]);
                }
            }
        }
        return dist;
    }

    const dist1 = dijkstra(src1, adj);
    const dist2 = dijkstra(src2, adj);
    const distDest = dijkstra(dest, revAdj); // distances to dest

    let ans = INF;
    for (let i = 0; i < n; i++) {
        if (dist1[i] === INF || dist2[i] === INF || distDest[i] === INF) continue;
        const total = dist1[i] + dist2[i] + distDest[i];
        if (total < ans) ans = total;
    }

    return ans === INF ? -1 : ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $src1
     * @param Integer $src2
     * @param Integer $dest
     * @return Integer
     */
    function minimumWeight($n, $edges, $src1, $src2, $dest) {
        // Build adjacency lists for original and reversed graph
        $g = array_fill(0, $n, []);
        $rg = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            $g[$u][] = [$v, $w];
            $rg[$v][] = [$u, $w]; // reversed edge
        }
        
        $dist1 = $this->dijkstra($n, $g, $src1);
        $dist2 = $this->dijkstra($n, $g, $src2);
        $distDest = $this->dijkstra($n, $rg, $dest); // distances to dest
        
        $INF = PHP_INT_MAX;
        $ans = $INF;
        for ($i = 0; $i < $n; ++$i) {
            if ($dist1[$i] === $INF || $dist2[$i] === $INF || $distDest[$i] === $INF) continue;
            $total = $dist1[$i] + $dist2[$i] + $distDest[$i];
            if ($total < $ans) $ans = $total;
        }
        return $ans === $INF ? -1 : $ans;
    }
    
    private function dijkstra($n, $adj, $src) {
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n, $INF);
        $dist[$src] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert($src, 0); // priority is negative distance (0)
        
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $node = $cur['data'];
            $d = -$cur['priority']; // convert back to positive distance
            if ($d > $dist[$node]) continue;
            foreach ($adj[$node] as $edge) {
                [$to, $w] = $edge;
                $nd = $d + $w;
                if ($nd < $dist[$to]) {
                    $dist[$to] = $nd;
                    $pq->insert($to, -$nd);
                }
            }
        }
        return $dist;
    }
}
```

## Swift

```swift
class Solution {
    private let INF: Int64 = Int64.max / 4

    private struct HeapElement {
        var dist: Int64
        var node: Int
    }

    private class MinHeap {
        private var data: [HeapElement] = []

        var isEmpty: Bool { data.isEmpty }

        func push(_ element: HeapElement) {
            data.append(element)
            var idx = data.count - 1
            while idx > 0 {
                let parent = (idx - 1) >> 1
                if data[parent].dist <= data[idx].dist { break }
                data.swapAt(parent, idx)
                idx = parent
            }
        }

        func pop() -> HeapElement? {
            guard !data.isEmpty else { return nil }
            let result = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var idx = 0
                while true {
                    let left = idx * 2 + 1
                    let right = left + 1
                    var smallest = idx
                    if left < data.count && data[left].dist < data[smallest].dist {
                        smallest = left
                    }
                    if right < data.count && data[right].dist < data[smallest].dist {
                        smallest = right
                    }
                    if smallest == idx { break }
                    data.swapAt(idx, smallest)
                    idx = smallest
                }
            }
            return result
        }
    }

    private func dijkstra(_ start: Int, _ graph: [[(to: Int, w: Int)]]) -> [Int64] {
        let n = graph.count
        var dist = Array(repeating: INF, count: n)
        dist[start] = 0
        let heap = MinHeap()
        heap.push(HeapElement(dist: 0, node: start))
        while let top = heap.pop() {
            if top.dist != dist[top.node] { continue }
            for edge in graph[top.node] {
                let nd = top.dist + Int64(edge.w)
                if nd < dist[edge.to] {
                    dist[edge.to] = nd
                    heap.push(HeapElement(dist: nd, node: edge.to))
                }
            }
        }
        return dist
    }

    func minimumWeight(_ n: Int, _ edges: [[Int]], _ src1: Int, _ src2: Int, _ dest: Int) -> Int {
        var adj = Array(repeating: [(to: Int, w: Int)](), count: n)
        var revAdj = Array(repeating: [(to: Int, w: Int)](), count: n)

        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            adj[u].append((to: v, w: w))
            revAdj[v].append((to: u, w: w))
        }

        let dFromSrc1 = dijkstra(src1, adj)
        let dFromSrc2 = dijkstra(src2, adj)
        let dToDest = dijkstra(dest, revAdj)

        var answer: Int64 = INF
        for i in 0..<n {
            let a = dFromSrc1[i]
            let b = dFromSrc2[i]
            let c = dToDest[i]
            if a == INF || b == INF || c == INF { continue }
            let total = a + b + c
            if total < answer { answer = total }
        }

        return answer == INF ? -1 : Int(answer)
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    private data class NodeDist(val d: Long, val v: Int)

    private fun dijkstra(start: Int, adj: Array<MutableList<Pair<Int, Int>>>): LongArray {
        val n = adj.size
        val INF = Long.MAX_VALUE / 4
        val dist = LongArray(n) { INF }
        dist[start] = 0L
        val pq = PriorityQueue<NodeDist>(compareBy { it.d })
        pq.add(NodeDist(0L, start))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.d != dist[cur.v]) continue
            for ((to, w) in adj[cur.v]) {
                val nd = cur.d + w.toLong()
                if (nd < dist[to]) {
                    dist[to] = nd
                    pq.add(NodeDist(nd, to))
                }
            }
        }
        return dist
    }

    fun minimumWeight(n: Int, edges: Array<IntArray>, src1: Int, src2: Int, dest: Int): Long {
        val forward = Array(n) { mutableListOf<Pair<Int, Int>>() }
        val reverse = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            forward[u].add(Pair(v, w))
            reverse[v].add(Pair(u, w)) // reversed edge
        }

        val distFromSrc1 = dijkstra(src1, forward)
        val distFromSrc2 = dijkstra(src2, forward)
        val distToDest = dijkstra(dest, reverse) // distances from any node to dest

        val INF = Long.MAX_VALUE / 4
        var ans = INF
        for (i in 0 until n) {
            val a = distFromSrc1[i]
            val b = distFromSrc2[i]
            val c = distToDest[i]
            if (a == INF || b == INF || c == INF) continue
            val total = a + b + c
            if (total < ans) ans = total
        }
        return if (ans == INF) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumWeight(int n, List<List<int>> edges, int src1, int src2, int dest) {
    const int INF = 1 << 60;

    // Build adjacency lists for forward and reverse graphs
    List<List<List<int>>> graph = List.generate(n, (_) => []);
    List<List<List<int>>> rev = List.generate(n, (_) => []);
    for (var e in edges) {
      int from = e[0];
      int to = e[1];
      int w = e[2];
      graph[from].add([to, w]);
      rev[to].add([from, w]);
    }

    // Dijkstra implementation using a binary min-heap
    List<int> dijkstra(List<List<List<int>>> g, int start) {
      List<int> dist = List.filled(n, INF);
      dist[start] = 0;
      var heap = _MinHeap();
      heap.push([0, start]);
      while (!heap.isEmpty) {
        var cur = heap.pop();
        int d = cur[0];
        int u = cur[1];
        if (d != dist[u]) continue;
        for (var e in g[u]) {
          int v = e[0];
          int w = e[1];
          int nd = d + w;
          if (nd < dist[v]) {
            dist[v] = nd;
            heap.push([nd, v]);
          }
        }
      }
      return dist;
    }

    List<int> d1 = dijkstra(graph, src1);
    List<int> d2 = dijkstra(graph, src2);
    List<int> dDest = dijkstra(rev, dest); // distances to dest

    int ans = INF;
    for (int i = 0; i < n; ++i) {
      if (d1[i] == INF || d2[i] == INF || dDest[i] == INF) continue;
      int total = d1[i] + d2[i] + dDest[i];
      if (total < ans) ans = total;
    }
    return ans == INF ? -1 : ans;
  }
}

// Simple binary min-heap for pairs [dist, node]
class _MinHeap {
  final List<List<int>> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(List<int> item) {
    _data.add(item);
    _siftUp(_data.length - 1);
  }

  List<int> pop() {
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
      if (_data[p][0] <= _data[i][0]) break;
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
      if (l < n && _data[l][0] < _data[smallest][0]) smallest = l;
      if (r < n && _data[r][0] < _data[smallest][0]) smallest = r;
      if (smallest == i) break;
      var tmp = _data[i];
      _data[i] = _data[smallest];
      _data[smallest] = tmp;
      i = smallest;
    }
  }
}
```

## Golang

```go
func minimumWeight(n int, edges [][]int, src1 int, src2 int, dest int) int64 {
	type Edge struct {
		to int
		w  int
	}
	adj := make([][]Edge, n)
	revAdj := make([][]Edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		adj[u] = append(adj[u], Edge{to: v, w: w})
		revAdj[v] = append(revAdj[v], Edge{to: u, w: w})
	}

	const INF int64 = 1 << 60

	type Item struct {
		node int
		dist int64
	}
	type PriorityQueue []Item

	func (pq PriorityQueue) Len() int { return len(pq) }
	func (pq PriorityQueue) Less(i, j int) bool { return pq[i].dist < pq[j].dist }
	func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
	func (pq *PriorityQueue) Push(x interface{}) {
		*pq = append(*pq, x.(Item))
	}
	func (pq *PriorityQueue) Pop() interface{} {
		old := *pq
		n := len(old)
		it := old[n-1]
		*pq = old[:n-1]
		return it
	}

	dijkstra := func(start int, graph [][]Edge) []int64 {
		dist := make([]int64, n)
		for i := range dist {
			dist[i] = INF
		}
		dist[start] = 0
		pq := &PriorityQueue{}
		heap.Init(pq)
		heap.Push(pq, Item{node: start, dist: 0})
		for pq.Len() > 0 {
			cur := heap.Pop(pq).(Item)
			if cur.dist != dist[cur.node] {
				continue
			}
			u := cur.node
			for _, e := range graph[u] {
				nd := cur.dist + int64(e.w)
				if nd < dist[e.to] {
					dist[e.to] = nd
					heap.Push(pq, Item{node: e.to, dist: nd})
				}
			}
		}
		return dist
	}

	dist1 := dijkstra(src1, adj)
	dist2 := dijkstra(src2, adj)
	distDest := dijkstra(dest, revAdj)

	ans := INF
	for v := 0; v < n; v++ {
		if dist1[v] == INF || dist2[v] == INF || distDest[v] == INF {
			continue
		}
		total := dist1[v] + dist2[v] + distDest[v]
		if total < ans {
			ans = total
		}
	}
	if ans == INF {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
INF = 1 << 60

def heap_push(heap, item)
  heap << item
  i = heap.size - 1
  while i > 0
    p = (i - 1) / 2
    break if heap[p][0] <= heap[i][0]
    heap[p], heap[i] = heap[i], heap[p]
    i = p
  end
end

def heap_pop(heap)
  top = heap[0]
  last = heap.pop
  if !heap.empty?
    heap[0] = last
    i = 0
    size = heap.size
    loop do
      l = i * 2 + 1
      r = i * 2 + 2
      break if l >= size
      child = (r < size && heap[r][0] < heap[l][0]) ? r : l
      break if heap[i][0] <= heap[child][0]
      heap[i], heap[child] = heap[child], heap[i]
      i = child
    end
  end
  top
end

def dijkstra(start, graph)
  n = graph.size
  dist = Array.new(n, INF)
  dist[start] = 0
  heap = []
  heap_push(heap, [0, start])
  until heap.empty?
    d, u = heap_pop(heap)
    next if d != dist[u]
    graph[u].each do |v, w|
      nd = d + w
      if nd < dist[v]
        dist[v] = nd
        heap_push(heap, [nd, v])
      end
    end
  end
  dist
end

def minimum_weight(n, edges, src1, src2, dest)
  graph = Array.new(n) { [] }
  rev   = Array.new(n) { [] }

  edges.each do |e|
    u, v, w = e
    graph[u] << [v, w]
    rev[v]   << [u, w]
  end

  d1 = dijkstra(src1, graph)
  d2 = dijkstra(src2, graph)
  ddest = dijkstra(dest, rev) # distance from any node to dest in original graph

  ans = INF
  n.times do |i|
    next if d1[i] == INF || d2[i] == INF || ddest[i] == INF
    total = d1[i] + d2[i] + ddest[i]
    ans = total if total < ans
  end

  ans == INF ? -1 : ans
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, PriorityQueue}
object Solution {
  private val INF: Long = Long.MaxValue / 4

  private def dijkstra(start: Int, graph: Array[ArrayBuffer[(Int, Int)]]): Array[Long] = {
    val n = graph.length
    val dist = Array.fill[Long](n)(INF)
    dist(start) = 0L
    implicit val ord: Ordering[(Long, Int)] = Ordering.by[(Long, Int), Long](_._1)
    val pq = PriorityQueue.empty[(Long, Int)](ord.reverse) // min-heap
    pq.enqueue((0L, start))
    while (pq.nonEmpty) {
      val (d, u) = pq.dequeue()
      if (d != dist(u)) {
        // outdated entry
      } else {
        for ((v, w) <- graph(u)) {
          val nd = d + w.toLong
          if (nd < dist(v)) {
            dist(v) = nd
            pq.enqueue((nd, v))
          }
        }
      }
    }
    dist
  }

  def minimumWeight(n: Int, edges: Array[Array[Int]], src1: Int, src2: Int, dest: Int): Long = {
    val g = Array.fill[ArrayBuffer[(Int, Int)]](n)(new ArrayBuffer[(Int, Int)]())
    val rg = Array.fill[ArrayBuffer[(Int, Int)]](n)(new ArrayBuffer[(Int, Int)]())
    for (e <- edges) {
      val from = e(0)
      val to   = e(1)
      val w    = e(2)
      g(from).append((to, w))
      rg(to).append((from, w))
    }

    val d1 = dijkstra(src1, g)
    val d2 = dijkstra(src2, g)
    val dd = dijkstra(dest, rg) // distances from any node to dest

    var ans: Long = INF
    for (v <- 0 until n) {
      if (d1(v) != INF && d2(v) != INF && dd(v) != INF) {
        val total = d1(v) + d2(v) + dd(v)
        if (total < ans) ans = total
      }
    }

    if (ans == INF) -1L else ans
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_weight(
        n: i32,
        edges: Vec<Vec<i32>>,
        src1: i32,
        src2: i32,
        dest: i32,
    ) -> i64 {
        let n_usize = n as usize;
        let mut graph: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize];
        let mut rev_graph: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize];

        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as i64;
            graph[u].push((v, w));
            rev_graph[v].push((u, w)); // reverse edge
        }

        const INF: i64 = i64::MAX / 4;

        fn dijkstra(start: usize, g: &Vec<Vec<(usize, i64)>>) -> Vec<i64> {
            let n = g.len();
            let mut dist = vec![INF; n];
            let mut heap: BinaryHeap<(Reverse<i64>, usize)> = BinaryHeap::new();

            dist[start] = 0;
            heap.push((Reverse(0i64), start));

            while let Some((Reverse(d), u)) = heap.pop() {
                if d != dist[u] {
                    continue;
                }
                for &(v, w) in &g[u] {
                    let nd = d + w;
                    if nd < dist[v] {
                        dist[v] = nd;
                        heap.push((Reverse(nd), v));
                    }
                }
            }
            dist
        }

        let s1 = src1 as usize;
        let s2 = src2 as usize;
        let d = dest as usize;

        let d1 = dijkstra(s1, &graph);
        let d2 = dijkstra(s2, &graph);
        let d3 = dijkstra(d, &rev_graph); // distances to dest

        let mut answer = INF;
        for i in 0..n_usize {
            if d1[i] == INF || d2[i] == INF || d3[i] == INF {
                continue;
            }
            let total = d1[i] + d2[i] + d3[i];
            if total < answer {
                answer = total;
            }
        }

        if answer == INF {
            -1
        } else {
            answer
        }
    }
}
```

## Racket

```racket
(require racket/heap)

(define INF 1000000000000) ; sufficiently large sentinel

;; Dijkstra's algorithm returning a vector of distances from start
(define (dijkstra start adj n)
  (define dist (make-vector n INF))
  (vector-set! dist start 0)
  (define heap (make-heap (lambda (a b) (< (first a) (first b)))))
  (heap-add! heap (list 0 start))
  (let loop ()
    (unless (heap-empty? heap)
      (define cur (heap-min heap))
      (heap-remove-min! heap)
      (define d (first cur))
      (define u (second cur))
      (when (= d (vector-ref dist u))          ; skip outdated entries
        (for ([edge (vector-ref adj u)])
          (define v (first edge))
          (define w (second edge))
          (define nd (+ d w))
          (when (< nd (vector-ref dist v))
            (vector-set! dist v nd)
            (heap-add! heap (list nd v)))))
      (loop)))
  dist)

(define/contract (minimum-weight n edges src1 src2 dest)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((forward (make-vector n '()))
         (reverse (make-vector n '())))
    ;; build adjacency lists
    (for ([e edges])
      (match-define (list from to w) e)
      (vector-set! forward from (cons (list to w) (vector-ref forward from)))
      (vector-set! reverse to   (cons (list from w) (vector-ref reverse to))))
    ;; shortest distances
    (define dist1 (dijkstra src1 forward n))
    (define dist2 (dijkstra src2 forward n))
    (define distDest (dijkstra dest reverse n))
    ;; evaluate best meeting point
    (define ans INF)
    (for ([i (in-range n)])
      (let ((d1 (vector-ref dist1 i))
            (d2 (vector-ref dist2 i))
            (dd (vector-ref distDest i)))
        (when (and (< d1 INF) (< d2 INF) (< dd INF))
          (define total (+ d1 d2 dd))
          (when (< total ans)
            (set! ans total)))))
    (if (= ans INF) -1 ans)))
```

## Erlang

```erlang
-spec minimum_weight(N :: integer(), Edges :: [[integer()]], Src1 :: integer(), Src2 :: integer(), Dest :: integer()) -> integer().
minimum_weight(N, Edges, Src1, Src2, Dest) ->
    Graph = build_graph(Edges, forward),
    RevGraph = build_graph(Edges, reverse),
    Dist1 = dijkstra(Graph, Src1),
    Dist2 = dijkstra(Graph, Src2),
    DistDest = dijkstra(RevGraph, Dest),
    Inf = 1 bsl 60,
    Min = find_min(N, Dist1, Dist2, DistDest, Inf),
    case Min >= Inf of
        true -> -1;
        false -> Min
    end.

build_graph(Edges, forward) ->
    lists:foldl(
      fun([U, V, W], Acc) ->
          maps:update_with(
            U,
            fun(L) -> [{V, W} | L] end,
            [{V, W}],
            Acc)
      end,
      #{},
      Edges);
build_graph(Edges, reverse) ->
    lists:foldl(
      fun([U, V, W], Acc) ->
          maps:update_with(
            V,
            fun(L) -> [{U, W} | L] end,
            [{U, W}],
            Acc)
      end,
      #{},
      Edges).

dijkstra(Graph, Start) ->
    Inf = 1 bsl 60,
    Dist0 = maps:put(Start, 0, #{}),
    PQ0 = gb_sets:singleton({0, Start}),
    dijkstra_loop(Graph, Dist0, PQ0, Inf).

dijkstra_loop(_Graph, DistMap, PQ, _Inf) when gb_sets:is_empty(PQ) ->
    DistMap;
dijkstra_loop(Graph, DistMap, PQ, Inf) ->
    {DistNode, Node} = gb_sets:choose(PQ),
    PQ1 = gb_sets:delete_any({DistNode, Node}, PQ),
    CurrentDist = maps:get(Node, DistMap, Inf),
    if
        DistNode > CurrentDist ->
            dijkstra_loop(Graph, DistMap, PQ1, Inf);
        true ->
            Neighbors = maps:get(Node, Graph, []),
            {NewDistMap, NewPQ} = process_neighbors(Neighbors, DistNode, DistMap, PQ1, Inf),
            dijkstra_loop(Graph, NewDistMap, NewPQ, Inf)
    end.

process_neighbors(Neighbors, DistNode, DistMap, PQ, Inf) ->
    lists:foldl(
      fun({Nei, W}, {DM, Q}) ->
          NewDist = DistNode + W,
          OldDist = maps:get(Nei, DM, Inf),
          if
              NewDist < OldDist ->
                  {maps:put(Nei, NewDist, DM), gb_sets:add({NewDist, Nei}, Q)};
              true ->
                  {DM, Q}
          end
      end,
      {DistMap, PQ},
      Neighbors).

find_min(N, D1, D2, DD, Inf) ->
    lists:foldl(
      fun(Node, Acc) ->
          D1v = maps:get(Node, D1, Inf),
          D2v = maps:get(Node, D2, Inf),
          DDv = maps:get(Node, DD, Inf),
          if
              D1v < Inf, D2v < Inf, DDv < Inf ->
                  Sum = D1v + D2v + DDv,
                  case Sum < Acc of
                      true -> Sum;
                      false -> Acc
                  end;
              true -> Acc
          end
      end,
      Inf,
      lists:seq(0, N - 1)).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_weight(integer, [[integer]], integer, integer, integer) :: integer
  def minimum_weight(n, edges, src1, src2, dest) do
    {adj, rev_adj} = build_graphs(edges)

    dist1 = dijkstra(src1, adj, n)
    dist2 = dijkstra(src2, adj, n)
    dist_dest = dijkstra(dest, rev_adj, n)

    inf = 1 <<< 60

    ans =
      Enum.reduce(0..(n - 1), inf, fn i, acc ->
        d1 = Map.get(dist1, i, inf)
        d2 = Map.get(dist2, i, inf)
        dd = Map.get(dist_dest, i, inf)

        if d1 < inf and d2 < inf and dd < inf do
          total = d1 + d2 + dd
          if total < acc, do: total, else: acc
        else
          acc
        end
      end)

    if ans == inf, do: -1, else: ans
  end

  defp build_graphs(edges) do
    Enum.reduce(edges, {%{}, %{}}, fn [u, v, w], {adj, rev} ->
      adj = Map.update(adj, u, [{v, w}], fn list -> [{v, w} | list] end)
      rev = Map.update(rev, v, [{u, w}], fn list -> [{u, w} | list] end)
      {adj, rev}
    end)
  end

  defp dijkstra(start, adj, _n) do
    inf = 1 <<< 60
    dist = %{start => 0}
    pq = :gb_sets.singleton({0, start})
    dijkstra_loop(pq, adj, dist, inf)
  end

  defp dijkstra_loop(pq, adj, dist, inf) do
    if :gb_sets.is_empty(pq) do
      dist
    else
      {{d, u}, pq_rest} = :gb_sets.take_smallest(pq)

      cur = Map.get(dist, u, inf)

      if d > cur do
        dijkstra_loop(pq_rest, adj, dist, inf)
      else
        {pq_new, dist_new} =
          Enum.reduce(Map.get(adj, u, []), {pq_rest, dist}, fn {v, w},
                                                             {p_acc, d_acc} ->
            nd = d + w
            old = Map.get(d_acc, v, inf)

            if nd < old do
              {:gb_sets.add({nd, v}, p_acc), Map.put(d_acc, v, nd)}
            else
              {p_acc, d_acc}
            end
          end)

        dijkstra_loop(pq_new, adj, dist_new, inf)
      end
    end
  end
end
```

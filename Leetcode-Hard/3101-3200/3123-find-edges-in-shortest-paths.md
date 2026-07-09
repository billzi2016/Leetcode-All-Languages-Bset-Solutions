# 3123. Find Edges in Shortest Paths

## Cpp

```cpp
class Solution {
public:
    using ll = long long;
    const ll INF = (1LL<<60);
    
    vector<ll> dijkstra(int n, const vector<vector<pair<int,int>>>& adj, int src) {
        vector<ll> dist(n, INF);
        priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
        dist[src] = 0;
        pq.emplace(0LL, src);
        while (!pq.empty()) {
            auto [d,u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto [v,w]: adj[u]) {
                ll nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.emplace(nd, v);
                }
            }
        }
        return dist;
    }
    
    vector<bool> findAnswer(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e: edges) {
            int u=e[0], v=e[1], w=e[2];
            adj[u].push_back({v,w});
            adj[v].push_back({u,w});
        }
        vector<ll> distS = dijkstra(n, adj, 0);
        vector<ll> distT = dijkstra(n, adj, n-1);
        ll shortest = distS[n-1];
        vector<bool> ans(edges.size(), false);
        if (shortest == INF) return ans; // no path exists
        for (size_t i=0;i<edges.size();++i){
            int u=edges[i][0], v=edges[i][1], w=edges[i][2];
            bool ok = false;
            if (distS[u]!=INF && distT[v]!=INF) {
                ll sum = distS[u] + (ll)w + distT[v];
                if (sum == shortest) ok = true;
            }
            if (!ok && distS[v]!=INF && distT[u]!=INF) {
                ll sum = distS[v] + (ll)w + distT[u];
                if (sum == shortest) ok = true;
            }
            ans[i]=ok;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public boolean[] findAnswer(int n, int[][] edges) {
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        long[] distFromStart = dijkstra(0, n, adj);
        long[] distFromEnd = dijkstra(n - 1, n, adj);
        long shortest = distFromStart[n - 1];

        boolean[] answer = new boolean[edges.length];
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            if (distFromStart[u] != Long.MAX_VALUE && distFromEnd[v] != Long.MAX_VALUE &&
                distFromStart[u] + w + distFromEnd[v] == shortest) {
                answer[i] = true;
            } else if (distFromStart[v] != Long.MAX_VALUE && distFromEnd[u] != Long.MAX_VALUE &&
                       distFromStart[v] + w + distFromEnd[u] == shortest) {
                answer[i] = true;
            }
        }
        return answer;
    }

    private long[] dijkstra(int src, int n, List<int[]>[] adj) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[src] = 0L;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0L, src});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int u = (int) cur[1];
            if (d != dist[u]) continue;

            for (int[] e : adj[u]) {
                int v = e[0];
                int w = e[1];
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
    def findAnswer(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[bool]
        """
        import heapq

        adj = [[] for _ in range(n)]
        for idx, (u, v, w) in enumerate(edges):
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist

        dist0 = dijkstra(0)
        distT = dijkstra(n - 1)
        total = dist0[n - 1]

        if total == float('inf'):
            return [False] * len(edges)

        ans = []
        for u, v, w in edges:
            on_path = (dist0[u] + w + distT[v] == total) or (dist0[v] + w + distT[u] == total)
            ans.append(on_path)
        return ans
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        INF = 10**18
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))

        def dijkstra(start: int) -> List[int]:
            dist = [INF] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist

        dist0 = dijkstra(0)
        distN = dijkstra(n - 1)
        shortest = dist0[n - 1]

        if shortest == INF:
            return [False] * len(edges)

        ans = []
        for a, b, w in edges:
            ok = (dist0[a] + w + distN[b] == shortest) or (dist0[b] + w + distN[a] == shortest)
            ans.append(ok)
        return ans
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long d;
    int v;
} HeapNode;

static void heapPush(HeapNode *heap, int *size, int cap, long long dist, int node) {
    if (*size + 1 > cap) return; // should not happen
    ++(*size);
    int i = *size;
    while (i > 1 && heap[i >> 1].d > dist) {
        heap[i] = heap[i >> 1];
        i >>= 1;
    }
    heap[i].d = dist;
    heap[i].v = node;
}

static HeapNode heapPop(HeapNode *heap, int *size) {
    HeapNode top = heap[1];
    heap[1] = heap[*size];
    --(*size);
    int i = 1;
    while (true) {
        int l = i << 1;
        if (l > *size) break;
        int r = l + 1;
        int smallest = l;
        if (r <= *size && heap[r].d < heap[l].d) smallest = r;
        if (heap[smallest].d >= heap[i].d) break;
        HeapNode tmp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = tmp;
        i = smallest;
    }
    return top;
}

static void dijkstra(int n, int *head, int *to, int *weight, int *next,
                     long long *dist, int src) {
    const long long INF = (1LL << 60);
    for (int i = 0; i < n; ++i) dist[i] = INF;
    dist[src] = 0;

    int cap = n + 2 * n; // enough space
    HeapNode *heap = (HeapNode *)malloc((cap + 5) * sizeof(HeapNode));
    int heapSize = 0;
    heapPush(heap, &heapSize, cap, 0LL, src);

    while (heapSize) {
        HeapNode cur = heapPop(heap, &heapSize);
        long long d = cur.d;
        int u = cur.v;
        if (d != dist[u]) continue;
        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            long long nd = d + weight[e];
            if (nd < dist[v]) {
                dist[v] = nd;
                heapPush(heap, &heapSize, cap, nd, v);
            }
        }
    }
    free(heap);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* findAnswer(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    // Build adjacency list
    int m = edgesSize;
    int totalAdj = 2 * m;
    int *head = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;

    int *to = (int *)malloc(totalAdj * sizeof(int));
    int *weight = (int *)malloc(totalAdj * sizeof(int));
    int *next = (int *)malloc(totalAdj * sizeof(int));

    int idx = 0;
    for (int i = 0; i < m; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];

        to[idx] = v; weight[idx] = w; next[idx] = head[u]; head[u] = idx++;
        to[idx] = u; weight[idx] = w; next[idx] = head[v]; head[v] = idx++;
    }

    // Dijkstra from source (0) and target (n-1)
    long long *distS = (long long *)malloc(n * sizeof(long long));
    long long *distT = (long long *)malloc(n * sizeof(long long));

    dijkstra(n, head, to, weight, next, distS, 0);
    dijkstra(n, head, to, weight, next, distT, n - 1);

    const long long INF = (1LL << 60);
    long long shortest = distS[n - 1];
    bool *ans = (bool *)malloc(m * sizeof(bool));
    for (int i = 0; i < m; ++i) ans[i] = false;

    if (shortest != INF) {
        for (int i = 0; i < m; ++i) {
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];
            long long path1 = distS[u] + w + distT[v];
            long long path2 = distS[v] + w + distT[u];
            if (path1 == shortest || path2 == shortest) {
                ans[i] = true;
            }
        }
    }

    free(head);
    free(to);
    free(weight);
    free(next);
    free(distS);
    free(distT);

    *returnSize = m;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public bool[] FindAnswer(int n, int[][] edges) {
        var graph = new List<(int to, int w, int idx)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int, int)>();
        for (int i = 0; i < edges.Length; i++) {
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            graph[u].Add((v, w, i));
            graph[v].Add((u, w, i));
        }

        var distS = Dijkstra(n, graph, 0);
        var distT = Dijkstra(n, graph, n - 1);

        const long INF = long.MaxValue / 4;
        long shortest = distS[n - 1];
        bool[] ans = new bool[edges.Length];
        if (shortest == INF) return ans;

        for (int i = 0; i < edges.Length; i++) {
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            long d1 = (distS[u] == INF || distT[v] == INF) ? INF : distS[u] + w + distT[v];
            long d2 = (distS[v] == INF || distT[u] == INF) ? INF : distS[v] + w + distT[u];
            if (d1 == shortest || d2 == shortest) ans[i] = true;
        }
        return ans;
    }

    private long[] Dijkstra(int n, List<(int to, int w, int idx)>[] graph, int start) {
        const long INF = long.MaxValue / 4;
        var dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[start] = 0;

        var pq = new PriorityQueue<(int node, long dist), long>();
        pq.Enqueue((start, 0), 0);

        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int u = cur.node;
            long d = cur.dist;
            if (d != dist[u]) continue;

            foreach (var e in graph[u]) {
                long nd = d + e.w;
                if (nd < dist[e.to]) {
                    dist[e.to] = nd;
                    pq.Enqueue((e.to, nd), nd);
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
 * @return {boolean[]}
 */
var findAnswer = function(n, edges) {
    const adj = Array.from({length: n}, () => []);
    for (let i = 0; i < edges.length; ++i) {
        const [a, b, w] = edges[i];
        adj[a].push([b, w]);
        adj[b].push([a, w]);
    }

    class MinHeap {
        constructor() { this.heap = []; }
        push(item) {
            this.heap.push(item);
            let i = this.heap.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.heap[p][0] <= this.heap[i][0]) break;
                [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
                i = p;
            }
        }
        pop() {
            if (!this.heap.length) return null;
            const top = this.heap[0];
            const last = this.heap.pop();
            if (this.heap.length) {
                this.heap[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, smallest = i;
                    if (l < this.heap.length && this.heap[l][0] < this.heap[smallest][0]) smallest = l;
                    if (r < this.heap.length && this.heap[r][0] < this.heap[smallest][0]) smallest = r;
                    if (smallest === i) break;
                    [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
                    i = smallest;
                }
            }
            return top;
        }
        size() { return this.heap.length; }
    }

    const dijkstra = (src) => {
        const dist = new Array(n).fill(Infinity);
        dist[src] = 0;
        const heap = new MinHeap();
        heap.push([0, src]);
        while (heap.size()) {
            const [d, u] = heap.pop();
            if (d !== dist[u]) continue;
            for (const [v, w] of adj[u]) {
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    heap.push([nd, v]);
                }
            }
        }
        return dist;
    };

    const distS = dijkstra(0);
    const distT = dijkstra(n - 1);
    const shortest = distS[n - 1];
    const ans = new Array(edges.length).fill(false);
    if (shortest === Infinity) return ans;

    for (let i = 0; i < edges.length; ++i) {
        const [a, b, w] = edges[i];
        if (distS[a] + w + distT[b] === shortest || distS[b] + w + distT[a] === shortest) {
            ans[i] = true;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function findAnswer(n: number, edges: number[][]): boolean[] {
    const adj: Array<Array<[number, number]>> = Array.from({ length: n }, () => []);
    for (const [a, b, w] of edges) {
        adj[a].push([b, w]);
        adj[b].push([a, w]);
    }

    const INF = Number.MAX_SAFE_INTEGER;

    class MinHeap {
        heap: Array<[number, number]> = [];
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
        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const last = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = last;
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

    function dijkstra(src: number): number[] {
        const dist = new Array<number>(n).fill(INF);
        dist[src] = 0;
        const heap = new MinHeap();
        heap.push([0, src]);
        while (true) {
            const cur = heap.pop();
            if (!cur) break;
            const [d, u] = cur;
            if (d !== dist[u]) continue;
            for (const [v, w] of adj[u]) {
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    heap.push([nd, v]);
                }
            }
        }
        return dist;
    }

    const distStart = dijkstra(0);
    const distEnd = dijkstra(n - 1);
    const totalDist = distStart[n - 1];
    const ans: boolean[] = new Array(edges.length).fill(false);

    if (totalDist !== INF) {
        for (let i = 0; i < edges.length; ++i) {
            const [u, v, w] = edges[i];
            if (
                (distStart[u] !== INF && distEnd[v] !== INF && distStart[u] + w + distEnd[v] === totalDist) ||
                (distStart[v] !== INF && distEnd[u] !== INF && distStart[v] + w + distEnd[u] === totalDist)
            ) {
                ans[i] = true;
            }
        }
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
     * @return Boolean[]
     */
    function findAnswer($n, $edges) {
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$a, $b, $w] = $e;
            $adj[$a][] = [$b, $w];
            $adj[$b][] = [$a, $w];
        }

        // Dijkstra from source
        $distS = $this->dijkstra($n, $adj, 0);
        // Dijkstra from target
        $distT = $this->dijkstra($n, $adj, $n - 1);

        $shortest = $distS[$n - 1];
        $ans = [];

        foreach ($edges as $e) {
            [$a, $b, $w] = $e;
            $ok = false;

            if ($distS[$a] !== PHP_INT_MAX && $distT[$b] !== PHP_INT_MAX) {
                if ($distS[$a] + $w + $distT[$b] == $shortest) {
                    $ok = true;
                }
            }
            if (!$ok && $distS[$b] !== PHP_INT_MAX && $distT[$a] !== PHP_INT_MAX) {
                if ($distS[$b] + $w + $distT[$a] == $shortest) {
                    $ok = true;
                }
            }

            $ans[] = $ok;
        }

        return $ans;
    }

    private function dijkstra($n, $adj, $src) {
        $dist = array_fill(0, $n, PHP_INT_MAX);
        $dist[$src] = 0;

        $pq = new SplPriorityQueue();
        // we need to extract both data and priority
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        // use negative distance because SplPriorityQueue is a max-heap
        $pq->insert($src, 0);

        while (!$pq->isEmpty()) {
            $ex = $pq->extract();
            $u = $ex['data'];
            $d = -$ex['priority'];

            if ($d > $dist[$u]) {
                continue;
            }

            foreach ($adj[$u] as $edge) {
                [$v, $w] = $edge;
                $nd = $d + $w;
                if ($nd < $dist[$v]) {
                    $dist[$v] = $nd;
                    $pq->insert($v, -$nd);
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
    struct Heap<T> {
        var elements: [T] = []
        let priorityFunction: (T, T) -> Bool
        init(sort: @escaping (T, T) -> Bool) {
            self.priorityFunction = sort
        }
        var isEmpty: Bool { elements.isEmpty }
        mutating func insert(_ value: T) {
            elements.append(value)
            siftUp(elements.count - 1)
        }
        mutating func remove() -> T? {
            guard !elements.isEmpty else { return nil }
            if elements.count == 1 {
                return elements.removeLast()
            } else {
                let value = elements[0]
                elements[0] = elements.removeLast()
                siftDown(0)
                return value
            }
        }
        mutating private func siftUp(_ index: Int) {
            var child = index
            var parent = (child - 1) / 2
            while child > 0 && priorityFunction(elements[child], elements[parent]) {
                elements.swapAt(child, parent)
                child = parent
                parent = (child - 1) / 2
            }
        }
        mutating private func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = 2 * parent + 1
                let right = left + 1
                var candidate = parent
                if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                    candidate = left
                }
                if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                    candidate = right
                }
                if candidate == parent { return }
                elements.swapAt(parent, candidate)
                parent = candidate
            }
        }
    }

    func findAnswer(_ n: Int, _ edges: [[Int]]) -> [Bool] {
        var adj = Array(repeating: [(to: Int, w: Int)](), count: n)
        for e in edges {
            let a = e[0], b = e[1], w = e[2]
            adj[a].append((to: b, w: w))
            adj[b].append((to: a, w: w))
        }

        func dijkstra(_ start: Int) -> [Int64] {
            let INF = Int64.max / 4
            var dist = Array(repeating: INF, count: n)
            dist[start] = 0
            var heap = Heap<(Int64, Int)>(sort: { $0.0 < $1.0 })
            heap.insert((0, start))
            while let top = heap.remove() {
                let (d, u) = top
                if d != dist[u] { continue }
                for edge in adj[u] {
                    let v = edge.to
                    let nd = d + Int64(edge.w)
                    if nd < dist[v] {
                        dist[v] = nd
                        heap.insert((nd, v))
                    }
                }
            }
            return dist
        }

        let distS = dijkstra(0)
        let distT = dijkstra(n - 1)
        let INF = Int64.max / 4
        let shortest = distS[n - 1]
        var answer = Array(repeating: false, count: edges.count)

        if shortest == INF {
            return answer
        }

        for (i, e) in edges.enumerated() {
            let a = e[0], b = e[1], w = e[2]
            let w64 = Int64(w)
            if distS[a] != INF && distT[b] != INF && distS[a] + w64 + distT[b] == shortest {
                answer[i] = true
            } else if distS[b] != INF && distT[a] != INF && distS[b] + w64 + distT[a] == shortest {
                answer[i] = true
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findAnswer(n: Int, edges: Array<IntArray>): BooleanArray {
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (i in edges.indices) {
            val a = edges[i][0]
            val b = edges[i][1]
            val w = edges[i][2]
            adj[a].add(Pair(b, w))
            adj[b].add(Pair(a, w))
        }

        fun dijkstra(start: Int): LongArray {
            val INF = Long.MAX_VALUE / 4
            val dist = LongArray(n) { INF }
            dist[start] = 0L
            data class Node(val v: Int, val d: Long)
            val pq = java.util.PriorityQueue<Node>(compareBy { it.d })
            pq.add(Node(start, 0L))
            while (pq.isNotEmpty()) {
                val cur = pq.poll()
                if (cur.d != dist[cur.v]) continue
                for ((to, w) in adj[cur.v]) {
                    val nd = cur.d + w.toLong()
                    if (nd < dist[to]) {
                        dist[to] = nd
                        pq.add(Node(to, nd))
                    }
                }
            }
            return dist
        }

        val distS = dijkstra(0)
        val distT = dijkstra(n - 1)
        val INF = Long.MAX_VALUE / 4
        val shortest = distS[n - 1]
        val m = edges.size
        val ans = BooleanArray(m)

        if (shortest == INF) return ans

        for (i in 0 until m) {
            val a = edges[i][0]
            val b = edges[i][1]
            val w = edges[i][2].toLong()
            var ok = false
            if (distS[a] != INF && distT[b] != INF && distS[a] + w + distT[b] == shortest) {
                ok = true
            } else if (distS[b] != INF && distT[a] != INF && distS[b] + w + distT[a] == shortest) {
                ok = true
            }
            ans[i] = ok
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<bool> findAnswer(int n, List<List<int>> edges) {
    const int INF = 1 << 60;

    // adjacency list
    List<List<_Adj>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      int w = e[2];
      adj[u].add(_Adj(v, w));
      adj[v].add(_Adj(u, w));
    }

    List<int> dijkstra(int start) {
      List<int> dist = List.filled(n, INF);
      dist[start] = 0;
      _MinHeap heap = _MinHeap();
      heap.push(_Item(start, 0));
      while (!heap.isEmpty) {
        var cur = heap.pop();
        int u = cur.node;
        int d = cur.dist;
        if (d != dist[u]) continue; // outdated entry
        for (var edge in adj[u]) {
          int v = edge.to;
          int nd = d + edge.w;
          if (nd < dist[v]) {
            dist[v] = nd;
            heap.push(_Item(v, nd));
          }
        }
      }
      return dist;
    }

    List<int> distS = dijkstra(0);
    List<int> distT = dijkstra(n - 1);
    int shortest = distS[n - 1];
    List<bool> ans = List.filled(edges.length, false);

    if (shortest == INF) {
      // no path exists; all remain false
      return ans;
    }

    for (int i = 0; i < edges.length; ++i) {
      int u = edges[i][0];
      int v = edges[i][1];
      int w = edges[i][2];
      bool ok = false;
      if (distS[u] != INF && distT[v] != INF &&
          distS[u] + w + distT[v] == shortest) {
        ok = true;
      } else if (distS[v] != INF && distT[u] != INF &&
          distS[v] + w + distT[u] == shortest) {
        ok = true;
      }
      ans[i] = ok;
    }

    return ans;
  }
}

class _Adj {
  int to;
  int w;
  _Adj(this.to, this.w);
}

class _Item {
  int node;
  int dist;
  _Item(this.node, this.dist);
}

class _MinHeap {
  final List<_Item> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void push(_Item item) {
    _heap.add(item);
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

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_heap[parent].dist <= _heap[idx].dist) break;
      var tmp = _heap[parent];
      _heap[parent] = _heap[idx];
      _heap[idx] = tmp;
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    int n = _heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _heap[left].dist < _heap[smallest].dist) {
        smallest = left;
      }
      if (right < n && _heap[right].dist < _heap[smallest].dist) {
        smallest = right;
      }
      if (smallest == idx) break;

      var tmp = _heap[idx];
      _heap[idx] = _heap[smallest];
      _heap[smallest] = tmp;
      idx = smallest;
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

const INF int64 = 1 << 60

type Edge struct {
	to int
	w  int
}

type Item struct {
	node int
	dist int64
}
type PQ []Item

func (pq PQ) Len() int { return len(pq) }
func (pq PQ) Less(i, j int) bool { return pq[i].dist < pq[j].dist }
func (pq PQ) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PQ) Push(x interface{}) { *pq = append(*pq, x.(Item)) }
func (pq *PQ) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[:n-1]
	return it
}

func dijkstra(start int, adj [][]Edge) []int64 {
	n := len(adj)
	dist := make([]int64, n)
	for i := 0; i < n; i++ {
		dist[i] = INF
	}
	dist[start] = 0
	pq := &PQ{}
	heap.Push(pq, Item{node: start, dist: 0})
	for pq.Len() > 0 {
		it := heap.Pop(pq).(Item)
		u := it.node
		d := it.dist
		if d != dist[u] {
			continue
		}
		for _, e := range adj[u] {
			v := e.to
			w := int64(e.w)
			nd := d + w
			if nd < dist[v] {
				dist[v] = nd
				heap.Push(pq, Item{node: v, dist: nd})
			}
		}
	}
	return dist
}

func findAnswer(n int, edges [][]int) []bool {
	adj := make([][]Edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		adj[u] = append(adj[u], Edge{to: v, w: w})
		adj[v] = append(adj[v], Edge{to: u, w: w})
	}
	distS := dijkstra(0, adj)
	distT := dijkstra(n-1, adj)
	shortest := distS[n-1]
	ans := make([]bool, len(edges))
	if shortest == INF {
		return ans
	}
	for i, e := range edges {
		u, v, w := e[0], e[1], int64(e[2])
		if distS[u] != INF && distT[v] != INF && distS[u]+w+distT[v] == shortest {
			ans[i] = true
			continue
		}
		if distS[v] != INF && distT[u] != INF && distS[v]+w+distT[u] == shortest {
			ans[i] = true
		}
	}
	return ans
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @heap = []
  end

  def push(item)
    @heap << item
    sift_up(@heap.size - 1)
  end

  def pop
    return nil if @heap.empty?
    min = @heap[0]
    last = @heap.pop
    unless @heap.empty?
      @heap[0] = last
      sift_down(0)
    end
    min
  end

  def empty?
    @heap.empty?
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @heap[parent][0] <= @heap[idx][0]
      @heap[parent], @heap[idx] = @heap[idx], @heap[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    size = @heap.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < size && @heap[left][0] < @heap[smallest][0]
        smallest = left
      end
      if right < size && @heap[right][0] < @heap[smallest][0]
        smallest = right
      end
      break if smallest == idx
      @heap[smallest], @heap[idx] = @heap[idx], @heap[smallest]
      idx = smallest
    end
  end
end

def dijkstra(start, adj, n)
  inf = (1 << 60)
  dist = Array.new(n, inf)
  dist[start] = 0
  heap = MinHeap.new
  heap.push([0, start])
  until heap.empty?
    d_u = heap.pop
    d = d_u[0]
    u = d_u[1]
    next if d != dist[u]
    adj[u].each do |v_w|
      v = v_w[0]
      w = v_w[1]
      nd = d + w
      if nd < dist[v]
        dist[v] = nd
        heap.push([nd, v])
      end
    end
  end
  dist
end

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Boolean[]}
def find_answer(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |e|
    a, b, w = e
    adj[a] << [b, w]
    adj[b] << [a, w]
  end

  dist_s = dijkstra(0, adj, n)
  dist_t = dijkstra(n - 1, adj, n)

  shortest = dist_s[n - 1]
  inf = (1 << 60)
  answer = Array.new(edges.length, false)
  return answer if shortest == inf

  edges.each_with_index do |e, idx|
    a, b, w = e
    if dist_s[a] + w + dist_t[b] == shortest || dist_s[b] + w + dist_t[a] == shortest
      answer[idx] = true
    end
  end
  answer
end
```

## Scala

```scala
object Solution {
  def findAnswer(n: Int, edges: Array[Array[Int]]): Array[Boolean] = {
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[(Int, Int)]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val w = e(2)
      adj(u).append((v, w))
      adj(v).append((u, w))
    }

    def dijkstra(src: Int): Array[Long] = {
      val INF = Long.MaxValue / 4
      val dist = Array.fill[Long](n)(INF)
      dist(src) = 0L
      val pq = new java.util.PriorityQueue[(Long, Int)](
        (a: (Long, Int), b: (Long, Int)) => java.lang.Long.compare(a._1, b._1)
      )
      pq.offer((0L, src))
      while (!pq.isEmpty) {
        val (d, u) = pq.poll()
        if (d != dist(u)) {
          // outdated entry
        } else {
          for ((v, w) <- adj(u)) {
            val nd = d + w.toLong
            if (nd < dist(v)) {
              dist(v) = nd
              pq.offer((nd, v))
            }
          }
        }
      }
      dist
    }

    val distS = dijkstra(0)
    val distT = dijkstra(n - 1)
    val shortest = distS(n - 1)

    val ans = new Array[Boolean](edges.length)
    for (i <- edges.indices) {
      val u = edges(i)(0)
      val v = edges(i)(1)
      val w = edges(i)(2).toLong
      var ok = false
      if (distS(u) != Long.MaxValue / 4 && distT(v) != Long.MaxValue / 4 &&
          distS(u) + w + distT(v) == shortest) {
        ok = true
      } else if (distS(v) != Long.MaxValue / 4 && distT(u) != Long.MaxValue / 4 &&
                 distS(v) + w + distT(u) == shortest) {
        ok = true
      }
      ans(i) = ok
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
    pub fn find_answer(n: i32, edges: Vec<Vec<i32>>) -> Vec<bool> {
        let n_usize = n as usize;
        let m = edges.len();
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize];
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            let w = e[2] as i64;
            adj[a].push((b, w));
            adj[b].push((a, w));
        }

        fn dijkstra(start: usize, adj: &Vec<Vec<(usize, i64)>>) -> Vec<i64> {
            let n = adj.len();
            let inf: i64 = i64::MAX / 4;
            let mut dist = vec![inf; n];
            let mut heap = BinaryHeap::new();
            dist[start] = 0;
            heap.push((Reverse(0_i64), start));
            while let Some((Reverse(d), u)) = heap.pop() {
                if d != dist[u] {
                    continue;
                }
                for &(v, w) in &adj[u] {
                    let nd = d + w;
                    if nd < dist[v] {
                        dist[v] = nd;
                        heap.push((Reverse(nd), v));
                    }
                }
            }
            dist
        }

        let dist_start = dijkstra(0, &adj);
        let dist_end = dijkstra(n_usize - 1, &adj);
        let inf: i64 = i64::MAX / 4;
        let shortest = dist_start[n_usize - 1];
        let mut answer = vec![false; m];

        if shortest == inf {
            return answer;
        }

        for (i, e) in edges.iter().enumerate() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            let w = e[2] as i64;

            let mut ok = false;
            if dist_start[a] != inf && dist_end[b] != inf {
                if dist_start[a] + w + dist_end[b] == shortest {
                    ok = true;
                }
            }
            if !ok && dist_start[b] != inf && dist_end[a] != inf {
                if dist_start[b] + w + dist_end[a] == shortest {
                    ok = true;
                }
            }
            answer[i] = ok;
        }

        answer
    }
}
```

## Racket

```racket
#lang racket
(require data/heap)
(require racket/match)

(define (dijkstra n adj src)
  (let* ((INF (expt 2 60))
         (dist (make-vector n INF)))
    (vector-set! dist src 0)
    (define heap (make-heap (lambda (a b) (< (first a) (first b)))))
    (heap-add! heap (list 0 src))
    (let loop ()
      (unless (heap-empty? heap)
        (define cur (heap-remove-min! heap))
        (define d (first cur))
        (define u (second cur))
        (when (= d (vector-ref dist u))
          (for ([e (in-list (vector-ref adj u))])
            (define v (first e))
            (define w (second e))
            (define nd (+ d w))
            (when (< nd (vector-ref dist v))
              (vector-set! dist v nd)
              (heap-add! heap (list nd v)))))
        (loop)))
    dist))

(define/contract (find-answer n edges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof boolean?))
  (let* ((adj (make-vector n '()))
         (m (length edges)))
    (for ([i (in-range m)])
      (match-define (list u v w) (list-ref edges i))
      (vector-set! adj u (cons (list v w) (vector-ref adj u)))
      (vector-set! adj v (cons (list u w) (vector-ref adj v))))
    (define dist0 (dijkstra n adj 0))
    (define distT (dijkstra n adj (- n 1)))
    (define INF (expt 2 60))
    (define total (vector-ref dist0 (- n 1)))
    (if (>= total INF)
        (make-list m #f)
        (let loop ((i 0) (ans '()))
          (if (= i m)
              (reverse ans)
              (begin
                (match-define (list u v w) (list-ref edges i))
                (define on?
                  (or (and (< (vector-ref dist0 u) INF)
                           (< (vector-ref distT v) INF)
                           (= (+ (vector-ref dist0 u) w (vector-ref distT v)) total))
                      (and (< (vector-ref dist0 v) INF)
                           (< (vector-ref distT u) INF)
                           (= (+ (vector-ref dist0 v) w (vector-ref distT u)) total))))
                (loop (+ i 1) (cons on? ans))))))))
```

## Erlang

```erlang
-define(INF, 1 bsl 60).

-spec find_answer(N :: integer(), Edges :: [[integer()]]) -> [boolean()].
find_answer(N, Edges) ->
    Adj = build_adj(Edges, #{}),
    Dist0 = dijkstra(N, Adj, 0),
    DistT = dijkstra(N, Adj, N - 1),
    Total = maps:get(N - 1, Dist0, ?INF),
    case Total of
        ?INF -> lists:duplicate(length(Edges), false);
        _ ->
            lists:map(fun([U, V, W]) ->
                D0U = maps:get(U, Dist0, ?INF),
                D0V = maps:get(V, Dist0, ?INF),
                DTU = maps:get(U, DistT, ?INF),
                DTV = maps:get(V, DistT, ?INF),
                (D0U + W + DTV == Total) orelse (D0V + W + DTU == Total)
            end, Edges)
    end.

build_adj([], Adj) -> Adj;
build_adj([[A, B, W] | Rest], Adj) ->
    L1 = maps:get(A, Adj, []),
    Adj1 = maps:put(A, [{B, W} | L1], Adj),
    L2 = maps:get(B, Adj1, []),
    Adj2 = maps:put(B, [{A, W} | L2], Adj1),
    build_adj(Rest, Adj2).

dijkstra(_N, Adj, Src) ->
    Dist0 = maps:put(Src, 0, #{}),
    PQ0 = gb_sets:add({0, Src}, gb_sets:new()),
    dijkstra_loop(Adj, Dist0, PQ0).

dijkstra_loop(_Adj, DistMap, PQ) when gb_sets:is_empty(PQ) ->
    DistMap;
dijkstra_loop(Adj, DistMap, PQ) ->
    Min = gb_sets:smallest(PQ),
    RestPQ = gb_sets:del_element(Min, PQ),
    {Dist, Node} = Min,
    CurrentDist = maps:get(Node, DistMap, ?INF),
    if
        Dist > CurrentDist ->
            dijkstra_loop(Adj, DistMap, RestPQ);
        true ->
            AdjList = maps:get(Node, Adj, []),
            {NewDistMap, NewPQ} = lists:foldl(
                fun({Nei, W}, {DM, Q}) ->
                    ND = Dist + W,
                    OldD = maps:get(Nei, DM, ?INF),
                    if
                        ND < OldD ->
                            {maps:put(Nei, ND, DM), gb_sets:add({ND, Nei}, Q)};
                        true ->
                            {DM, Q}
                    end
                end,
                {DistMap, RestPQ},
                AdjList
            ),
            dijkstra_loop(Adj, NewDistMap, NewPQ)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_answer(n :: integer, edges :: [[integer]]) :: [boolean]
  def find_answer(n, edges) do
    adj = build_adj(edges)

    dist_start = dijkstra(0, n, adj)
    dist_end = dijkstra(n - 1, n, adj)

    inf = 1 <<< 60
    shortest = Map.get(dist_start, n - 1, inf)

    if shortest == inf do
      Enum.map(edges, fn _ -> false end)
    else
      Enum.map(edges, fn [a, b, w] ->
        da = Map.get(dist_start, a, inf)
        db = Map.get(dist_start, b, inf)
        ta = Map.get(dist_end, a, inf)
        tb = Map.get(dist_end, b, inf)

        (da + w + tb == shortest) or (db + w + ta == shortest)
      end)
    end
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [a, b, w], acc ->
      acc
      |> Map.update(a, [{b, w}], fn lst -> [{b, w} | lst] end)
      |> Map.update(b, [{a, w}], fn lst -> [{a, w} | lst] end)
    end)
  end

  defp dijkstra(start, n, adj) do
    inf = 1 <<< 60

    dist =
      Enum.reduce(0..n - 1, %{}, fn i, acc ->
        Map.put(acc, i, inf)
      end)
      |> Map.put(start, 0)

    pq = :gb_sets.singleton({0, start})
    dijkstra_loop(pq, dist, adj, inf)
  end

  defp dijkstra_loop(pq, dist, adj, inf) do
    if :gb_sets.is_empty(pq) do
      dist
    else
      {{d, u}, pq_rest} = :gb_sets.take_smallest(pq)

      if d > Map.get(dist, u, inf) do
        dijkstra_loop(pq_rest, dist, adj, inf)
      else
        {dist2, pq2} =
          Enum.reduce(Map.get(adj, u, []), {dist, pq_rest}, fn {v, w},
                                                             {dacc, pacc} ->
            nd = d + w

            if nd < Map.get(dacc, v, inf) do
              {Map.put(dacc, v, nd), :gb_sets.add({nd, v}, pacc)}
            else
              {dacc, pacc}
            end
          end)

        dijkstra_loop(pq2, dist2, adj, inf)
      end
    end
  end
end
```

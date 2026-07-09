# 1786. Number of Restricted Paths From First to Last Node

## Cpp

```cpp
class Solution {
public:
    int countRestrictedPaths(int n, vector<vector<int>>& edges) {
        const int MOD = 1'000'000'007;
        vector<vector<pair<int,int>>> adj(n + 1);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        // Dijkstra from node n
        const long long INF = (1LL<<60);
        vector<long long> dist(n + 1, INF);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        dist[n] = 0;
        pq.push({0, n});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto &[v, w] : adj[u]) {
                long long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        // Order nodes by distance ascending
        vector<int> order(n);
        iota(order.begin(), order.end(), 1);
        sort(order.begin(), order.end(), [&](int a, int b){
            return dist[a] < dist[b];
        });
        vector<int> dp(n + 1, 0);
        dp[n] = 1;
        for (int u : order) {
            if (u == n) continue;
            long long sum = 0;
            for (auto &[v, w] : adj[u]) {
                if (dist[u] > dist[v]) {
                    sum += dp[v];
                    if (sum >= MOD) sum -= MOD;
                }
            }
            dp[u] = (int)(sum % MOD);
        }
        return dp[1];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int countRestrictedPaths(int n, int[][] edges) {
        // Build graph
        @SuppressWarnings("unchecked")
        java.util.List<int[]>[] graph = new java.util.ArrayList[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        // Dijkstra from node n
        long[] dist = new long[n + 1];
        java.util.Arrays.fill(dist, Long.MAX_VALUE);
        dist[n] = 0;
        java.util.PriorityQueue<long[]> pq = new java.util.PriorityQueue<>(
                (a, b) -> Long.compare(a[1], b[1])
        );
        pq.offer(new long[]{n, 0});
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            int u = (int) cur[0];
            long d = cur[1];
            if (d != dist[u]) continue;
            for (int[] nb : graph[u]) {
                int v = nb[0];
                int w = nb[1];
                long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.offer(new long[]{v, nd});
                }
            }
        }

        // Nodes sorted by distance ascending
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i + 1;
        java.util.Arrays.sort(order, (a, b) -> Long.compare(dist[a], dist[b]));

        long[] dp = new long[n + 1];
        dp[n] = 1; // base case

        for (int u : order) {
            if (u == n) continue; // already set
            long ways = 0;
            for (int[] nb : graph[u]) {
                int v = nb[0];
                if (dist[u] > dist[v]) {
                    ways += dp[v];
                    if (ways >= MOD) ways -= MOD;
                }
            }
            dp[u] = ways;
        }

        return (int) dp[1];
    }
}
```

## Python

```python
class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        import heapq
        from functools import lru_cache

        MOD = 10**9 + 7

        # Build adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra from node n to get shortest distances to n
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # DP with memoization: count restricted paths from u to n
        @lru_cache(None)
        def dfs(u):
            if u == n:
                return 1
            total = 0
            du = dist[u]
            for v, _ in graph[u]:
                if du > dist[v]:
                    total += dfs(v)
                    if total >= MOD:
                        total -= MOD
            return total

        return dfs(1) % MOD
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Dijkstra from node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # DP over nodes sorted by distance ascending
        order = sorted(range(1, n + 1), key=lambda x: dist[x])
        dp = [0] * (n + 1)
        dp[n] = 1
        for u in order:
            if u == n:
                continue
            total = 0
            du = dist[u]
            for v, _ in graph[u]:
                if du > dist[v]:
                    total += dp[v]
            dp[u] = total % MOD

        return dp[1]
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MOD 1000000007LL
typedef long long ll;

static int N;
static ll *distArr;
static int *headArr, *toArr, *weightArr, *nextArr;
static int edgeIdx;
static int *dpArr;

/* adjacency list insertion */
static void addEdge(int u, int v, int w) {
    toArr[edgeIdx] = v;
    weightArr[edgeIdx] = w;
    nextArr[edgeIdx] = headArr[u];
    headArr[u] = edgeIdx++;
}

/* min-heap for Dijkstra */
typedef struct {
    int node;
    ll dist;
} HeapNode;

static void heapSwap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapNode **heap, int *size, int node, ll dist) {
    ++(*size);
    int i = *size;
    (*heap)[i].node = node;
    (*heap)[i].dist = dist;
    while (i > 1 && (*heap)[i].dist < (*heap)[i >> 1].dist) {
        heapSwap(&(*heap)[i], &(*heap)[i >> 1]);
        i >>= 1;
    }
}

static HeapNode heapPop(HeapNode **heap, int *size) {
    HeapNode top = (*heap)[1];
    (*heap)[1] = (*heap)[*size];
    --(*size);
    int i = 1;
    while (1) {
        int l = i << 1, r = l + 1, smallest = i;
        if (l <= *size && (*heap)[l].dist < (*heap)[smallest].dist) smallest = l;
        if (r <= *size && (*heap)[r].dist < (*heap)[smallest].dist) smallest = r;
        if (smallest == i) break;
        heapSwap(&(*heap)[i], &(*heap)[smallest]);
        i = smallest;
    }
    return top;
}

/* Dijkstra from node N */
static void dijkstra() {
    const ll INF = (1LL << 60);
    for (int i = 1; i <= N; ++i) distArr[i] = INF;
    distArr[N] = 0;

    int heapCap = 2 * N + 5;
    HeapNode *heap = (HeapNode *)malloc(sizeof(HeapNode) * (heapCap));
    int heapSize = 0;
    heapPush(&heap, &heapSize, N, 0);

    while (heapSize) {
        HeapNode cur = heapPop(&heap, &heapSize);
        int u = cur.node;
        ll d = cur.dist;
        if (d != distArr[u]) continue;
        for (int e = headArr[u]; e != -1; e = nextArr[e]) {
            int v = toArr[e];
            ll nd = d + weightArr[e];
            if (nd < distArr[v]) {
                distArr[v] = nd;
                heapPush(&heap, &heapSize, v, nd);
            }
        }
    }
    free(heap);
}

/* DFS with memoization for counting restricted paths */
static int dfs(int u) {
    if (u == N) return 1;
    if (dpArr[u] != -1) return dpArr[u];
    ll ans = 0;
    for (int e = headArr[u]; e != -1; e = nextArr[e]) {
        int v = toArr[e];
        if (distArr[u] > distArr[v]) {
            ans += dfs(v);
            if (ans >= MOD) ans -= MOD;
        }
    }
    dpArr[u] = (int)ans;
    return dpArr[u];
}

int countRestrictedPaths(int n, int** edges, int edgesSize, int* edgesColSize){
    N = n;
    int maxEdges = edgesSize * 2;

    headArr = (int *)malloc(sizeof(int) * (N + 1));
    for (int i = 0; i <= N; ++i) headArr[i] = -1;

    toArr = (int *)malloc(sizeof(int) * maxEdges);
    weightArr = (int *)malloc(sizeof(int) * maxEdges);
    nextArr = (int *)malloc(sizeof(int) * maxEdges);
    edgeIdx = 0;

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];
        addEdge(u, v, w);
        addEdge(v, u, w);
    }

    distArr = (ll *)malloc(sizeof(ll) * (N + 1));
    dijkstra();

    dpArr = (int *)malloc(sizeof(int) * (N + 1));
    for (int i = 0; i <= N; ++i) dpArr[i] = -1;

    int result = dfs(1);

    free(headArr);
    free(toArr);
    free(weightArr);
    free(nextArr);
    free(distArr);
    free(dpArr);

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    private long[] dist;
    private List<(int to, int w)>[] adj;
    private int n;
    private int[] memo;
    private bool[] visited;

    public int CountRestrictedPaths(int n, int[][] edges) {
        this.n = n;
        adj = new List<(int to, int w)>[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new List<(int to, int w)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].Add((v, w));
            adj[v].Add((u, w));
        }

        // Dijkstra from node n
        dist = new long[n + 1];
        const long INF = long.MaxValue / 4;
        for (int i = 1; i <= n; i++) dist[i] = INF;
        dist[n] = 0;

        var pq = new PriorityQueue<int, long>();
        pq.Enqueue(n, 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out int u, out long d);
            if (d != dist[u]) continue; // outdated entry
            foreach (var (v, w) in adj[u]) {
                long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.Enqueue(v, nd);
                }
            }
        }

        memo = new int[n + 1];
        visited = new bool[n + 1];
        return Dfs(1);
    }

    private int Dfs(int u) {
        if (u == n) return 1;
        if (visited[u]) return memo[u];
        long ans = 0;
        foreach (var (v, _) in adj[u]) {
            if (dist[u] > dist[v]) {
                ans += Dfs(v);
                if (ans >= MOD) ans -= MOD; // keep within range
            }
        }
        ans %= MOD;
        memo[u] = (int)ans;
        visited[u] = true;
        return memo[u];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countRestrictedPaths = function(n, edges) {
    const MOD = 1_000_000_007;
    const adj = Array.from({length: n + 1}, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    // Dijkstra from node n
    const dist = new Array(n + 1).fill(Infinity);
    dist[n] = 0;
    const heap = new MinHeap();
    heap.push([0, n]); // [distance, node]

    while (!heap.isEmpty()) {
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

    // Nodes sorted by distance ascending
    const order = Array.from({length: n}, (_, i) => i + 1);
    order.sort((a, b) => dist[a] - dist[b]);

    const dp = new Array(n + 1).fill(0);
    dp[n] = 1;
    for (const u of order) {
        if (u === n) continue;
        let sum = 0;
        for (const [v] of adj[u]) {
            if (dist[u] > dist[v]) {
                sum += dp[v];
                if (sum >= MOD) sum -= MOD;
            }
        }
        dp[u] = sum;
    }

    return dp[1];
};

class MinHeap {
    constructor() {
        this.heap = [];
    }
    isEmpty() {
        return this.heap.length === 0;
    }
    push(item) {
        this.heap.push(item);
        this._bubbleUp(this.heap.length - 1);
    }
    pop() {
        if (this.heap.length === 0) return null;
        const top = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this._bubbleDown(0);
        }
        return top;
    }
    _bubbleUp(idx) {
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (this.heap[parent][0] <= this.heap[idx][0]) break;
            [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
            idx = parent;
        }
    }
    _bubbleDown(idx) {
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
```

## Typescript

```typescript
function countRestrictedPaths(n: number, edges: number[][]): number {
    const MOD = 1_000_000_007;
    const graph: Array<Array<[number, number]>> = Array.from({ length: n + 1 }, () => []);
    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }

    // Dijkstra from node n
    const dist: number[] = new Array(n + 1).fill(Infinity);
    dist[n] = 0;

    class MinHeap {
        heap: Array<[number, number]> = [];
        push(item: [number, number]) {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(idx: number) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        private bubbleDown(idx: number) {
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
    }

    const pq = new MinHeap();
    pq.push([0, n]);

    while (true) {
        const cur = pq.pop();
        if (!cur) break;
        const [d, u] = cur;
        if (d !== dist[u]) continue;
        for (const [v, w] of graph[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                pq.push([nd, v]);
            }
        }
    }

    // DP on DAG defined by decreasing distances
    const order: number[] = Array.from({ length: n }, (_, i) => i + 1);
    order.sort((a, b) => dist[a] - dist[b]); // ascending distance

    const dp: number[] = new Array(n + 1).fill(0);
    dp[n] = 1;

    for (const u of order) {
        if (u === n) continue;
        let sum = 0;
        for (const [v] of graph[u]) {
            if (dist[u] > dist[v]) {
                sum += dp[v];
                if (sum >= MOD) sum -= MOD;
            }
        }
        dp[u] = sum;
    }

    return dp[1] % MOD;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function countRestrictedPaths($n, $edges) {
        $MOD = 1000000007;
        // Build adjacency list
        $graph = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            [$u, $v, $w] = $e;
            $graph[$u][] = [$v, $w];
            $graph[$v][] = [$u, $w];
        }
        // Dijkstra from node n
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n + 1, $INF);
        $dist[$n] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert($n, 0); // priority = -distance (0)
        while (!$pq->isEmpty()) {
            $item = $pq->extract(); // ['data'=>node,'priority'=>prio]
            $u = $item['data'];
            $d = -$item['priority']; // convert back to distance
            if ($d > $dist[$u]) continue;
            foreach ($graph[$u] as $edge) {
                [$v, $w] = $edge;
                $nd = $d + $w;
                if ($nd < $dist[$v]) {
                    $dist[$v] = $nd;
                    $pq->insert($v, -$nd);
                }
            }
        }
        // Order nodes by increasing distance
        $order = range(1, $n);
        usort($order, function($a, $b) use ($dist) {
            if ($dist[$a] == $dist[$b]) return 0;
            return ($dist[$a] < $dist[$b]) ? -1 : 1;
        });
        // DP: number of restricted paths from each node to n
        $dp = array_fill(0, $n + 1, 0);
        $dp[$n] = 1;
        foreach ($order as $u) {
            if ($u == $n) continue;
            foreach ($graph[$u] as $edge) {
                [$v, $w] = $edge;
                if ($dist[$u] > $dist[$v]) {
                    $dp[$u] = ($dp[$u] + $dp[$v]) % $MOD;
                }
            }
        }
        return $dp[1];
    }
}
```

## Swift

```swift
class Solution {
    let MOD = 1_000_000_007
    var graph: [[(to: Int, weight: Int)]] = []
    var dist: [Int64] = []
    var memo: [Int] = []
    var nNodes: Int = 0

    func countRestrictedPaths(_ n: Int, _ edges: [[Int]]) -> Int {
        nNodes = n
        graph = Array(repeating: [], count: n + 1)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            graph[u].append((to: v, weight: w))
            graph[v].append((to: u, weight: w))
        }
        dist = Array(repeating: Int64.max, count: n + 1)
        dijkstra()
        memo = Array(repeating: -1, count: n + 1)
        return dfs(1) % MOD
    }

    private func dijkstra() {
        var heap = MinHeap()
        dist[nNodes] = 0
        heap.push((0, nNodes))
        while let (d, u) = heap.pop() {
            if d != dist[u] { continue }
            for edge in graph[u] {
                let v = edge.to
                let nd = d + Int64(edge.weight)
                if nd < dist[v] {
                    dist[v] = nd
                    heap.push((nd, v))
                }
            }
        }
    }

    private func dfs(_ u: Int) -> Int {
        if u == nNodes { return 1 }
        if memo[u] != -1 { return memo[u] }
        var ans = 0
        for edge in graph[u] {
            let v = edge.to
            if dist[u] > dist[v] {
                ans += dfs(v)
                if ans >= MOD { ans -= MOD }
            }
        }
        memo[u] = ans % MOD
        return memo[u]
    }

    private struct MinHeap {
        var heap: [(Int64, Int)] = []

        mutating func push(_ item: (Int64, Int)) {
            heap.append(item)
            siftUp(heap.count - 1)
        }

        mutating func pop() -> (Int64, Int)? {
            guard !heap.isEmpty else { return nil }
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                siftDown(0)
            }
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
}
```

## Kotlin

```kotlin
class Solution {
    fun countRestrictedPaths(n: Int, edges: Array<IntArray>): Int {
        val adj = Array(n + 1) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        // Dijkstra from node n to compute shortest distances to n
        val dist = LongArray(n + 1) { Long.MAX_VALUE }
        dist[n] = 0L
        data class Node(val d: Long, val v: Int)
        val pq = java.util.PriorityQueue<Node>(compareBy { it.d })
        pq.add(Node(0L, n))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.d != dist[cur.v]) continue
            for ((to, w) in adj[cur.v]) {
                val nd = cur.d + w
                if (nd < dist[to]) {
                    dist[to] = nd
                    pq.add(Node(nd, to))
                }
            }
        }

        // DP: number of restricted paths from each node to n
        val order = (1..n).sortedBy { dist[it] }  // increasing distance
        val MOD = 1_000_000_007L
        val dp = LongArray(n + 1)
        dp[n] = 1L

        for (u in order) {
            if (u == n) continue
            var sum = 0L
            for ((v, _) in adj[u]) {
                if (dist[v] < dist[u]) {
                    sum += dp[v]
                    if (sum >= MOD) sum -= MOD
                }
            }
            dp[u] = sum % MOD
        }

        return (dp[1] % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countRestrictedPaths(int n, List<List<int>> edges) {
    // Build adjacency list
    final List<List<_Edge>> adj = List.generate(n + 1, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1], w = e[2];
      adj[u].add(_Edge(v, w));
      adj[v].add(_Edge(u, w));
    }

    // Dijkstra from node n
    final List<int> dist = List.filled(n + 1, 1 << 60);
    dist[n] = 0;
    final _MinHeap heap = _MinHeap();
    heap.push(_Node(0, n));

    while (!heap.isEmpty) {
      final cur = heap.pop();
      int d = cur.dist;
      int u = cur.node;
      if (d != dist[u]) continue; // outdated entry
      for (var e in adj[u]) {
        int v = e.to;
        int nd = d + e.w;
        if (nd < dist[v]) {
          dist[v] = nd;
          heap.push(_Node(nd, v));
        }
      }
    }

    // Order nodes by distance ascending
    List<int> order = List.generate(n, (i) => i + 1);
    order.sort((a, b) => dist[a].compareTo(dist[b]));

    // DP counting restricted paths
    final List<int> dp = List.filled(n + 1, 0);
    dp[n] = 1;
    for (int u in order) {
      if (u == n) continue;
      int total = 0;
      for (var e in adj[u]) {
        int v = e.to;
        if (dist[u] > dist[v]) {
          total += dp[v];
          if (total >= _mod) total -= _mod;
        }
      }
      dp[u] = total;
    }

    return dp[1];
  }
}

class _Edge {
  final int to;
  final int w;
  _Edge(this.to, this.w);
}

class _Node {
  final int dist;
  final int node;
  _Node(this.dist, this.node);
}

class _MinHeap {
  final List<_Node> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void push(_Node item) {
    _heap.add(item);
    _siftUp(_heap.length - 1);
  }

  _Node pop() {
    final top = _heap[0];
    final last = _heap.removeLast();
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
      final tmp = _heap[p];
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
      final tmp = _heap[i];
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

const MOD = 1000000007
const INF int64 = 1<<60 - 1

type Edge struct {
	to int
	w  int
}

type Item struct {
	node int
	dist int64
}
type PriorityQueue []Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].dist < pq[j].dist
}
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

func countRestrictedPaths(n int, edges [][]int) int {
	graph := make([][]Edge, n+1)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		graph[u] = append(graph[u], Edge{to: v, w: w})
		graph[v] = append(graph[v], Edge{to: u, w: w})
	}

	// Dijkstra from node n
	dist := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		dist[i] = INF
	}
	dist[n] = 0
	pq := &PriorityQueue{}
	heap.Init(pq)
	heap.Push(pq, Item{node: n, dist: 0})

	for pq.Len() > 0 {
		it := heap.Pop(pq).(Item)
		u := it.node
		if it.dist != dist[u] {
			continue
		}
		for _, e := range graph[u] {
			v := e.to
			newDist := dist[u] + int64(e.w)
			if newDist < dist[v] {
				dist[v] = newDist
				heap.Push(pq, Item{node: v, dist: newDist})
			}
		}
	}

	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = -1
	}
	var dfs func(int) int
	dfs = func(u int) int {
		if u == n {
			return 1
		}
		if dp[u] != -1 {
			return dp[u]
		}
		total := 0
		for _, e := range graph[u] {
			v := e.to
			if dist[u] > dist[v] {
				total += dfs(v)
				if total >= MOD {
					total -= MOD
				}
			}
		}
		dp[u] = total
		return total
	}

	return dfs(1)
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

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_restricted_paths(n, edges)
  adj = Array.new(n + 1) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  inf = (1 << 60)
  dist = Array.new(n + 1, inf)
  dist[n] = 0
  heap = MinHeap.new
  heap.push([0, n])

  until heap.empty?
    d_u, u = heap.pop
    next if d_u != dist[u]
    adj[u].each do |v, w|
      nd = d_u + w
      if nd < dist[v]
        dist[v] = nd
        heap.push([nd, v])
      end
    end
  end

  order = (1..n).to_a.sort_by { |i| dist[i] }
  mod = 1_000_000_007
  dp = Array.new(n + 1, 0)
  dp[n] = 1

  order.each do |u|
    adj[u].each do |v, _|
      if dist[v] > dist[u]
        dp[v] += dp[u]
        dp[v] -= mod if dp[v] >= mod
      end
    end
  end

  dp[1] % mod
end
```

## Scala

```scala
object Solution {
  def countRestrictedPaths(n: Int, edges: Array[Array[Int]]): Int = {
    val adj = Array.fill(n + 1)(new scala.collection.mutable.ArrayBuffer[(Int, Int)]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val w = e(2)
      adj(u).append((v, w))
      adj(v).append((u, w))
    }

    val INF = Long.MaxValue / 4
    val dist = Array.fill[Long](n + 1)(INF)
    dist(n) = 0L

    val pq = new java.util.PriorityQueue[(Long, Int)](
      (a: (Long, Int), b: (Long, Int)) => {
        if (a._1 < b._1) -1 else if (a._1 > b._1) 1 else 0
      }
    )
    pq.offer((0L, n))

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

    val order = (1 to n).toArray.sortBy(dist(_))

    val MOD = 1000000007L
    val dp = Array.fill[Long](n + 1)(0L)
    dp(n) = 1L

    for (node <- order) {
      if (node != n) {
        var sum = 0L
        for ((v, _) <- adj(node)) {
          if (dist(node) > dist(v)) {
            sum += dp(v)
            if (sum >= MOD) sum -= MOD
          }
        }
        dp(node) = sum % MOD
      }
    }

    dp(1).toInt
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn count_restricted_paths(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let u = (e[0] - 1) as usize;
            let v = (e[1] - 1) as usize;
            let w = e[2] as i64;
            adj[u].push((v, w));
            adj[v].push((u, w));
        }

        // Dijkstra from node n-1
        const INF: i64 = i64::MAX / 4;
        let mut dist = vec![INF; n_usize];
        let target = n_usize - 1;
        dist[target] = 0;
        let mut heap = BinaryHeap::new();
        heap.push(Reverse((0_i64, target)));

        while let Some(Reverse((d, u))) = heap.pop() {
            if d != dist[u] {
                continue;
            }
            for &(v, w) in &adj[u] {
                let nd = d + w;
                if nd < dist[v] {
                    dist[v] = nd;
                    heap.push(Reverse((nd, v)));
                }
            }
        }

        // DP over nodes sorted by distance ascending
        const MOD: i64 = 1_000_000_007;
        let mut order: Vec<usize> = (0..n_usize).collect();
        order.sort_by_key(|&i| dist[i]);

        let mut dp = vec![0_i64; n_usize];
        dp[target] = 1;

        for &u in order.iter() {
            let cur = dp[u];
            if cur == 0 {
                continue;
            }
            for &(v, _) in &adj[u] {
                if dist[u] < dist[v] {
                    dp[v] += cur;
                    if dp[v] >= MOD {
                        dp[v] -= MOD;
                    }
                }
            }
        }

        dp[0] as i32
    }
}
```

## Racket

```racket
(require racket/heap)

(define MOD 1000000007)

(define (count-restricted-paths n edges)
  (let* ([adj (make-vector (+ n 1) '())]
         ;; build adjacency list
         [_ (for ([e edges])
              (match-define (list u v w) e)
              (vector-set! adj u (cons (list v w) (vector-ref adj u)))
              (vector-set! adj v (cons (list u w) (vector-ref adj v))))]
         ;; Dijkstra from node n
         [dist (make-vector (+ n 1) (expt 10 15))]
         [_ (vector-set! dist n 0)]
         [heap (make-heap (lambda (a b) (< (first a) (first b))))])
    (heap-add! heap (list 0 n))
    (let loop ()
      (unless (heap-empty? heap)
        (define cur (heap-min heap))
        (heap-remove-min! heap)
        (define d (first cur))
        (define u (second cur))
        (when (= d (vector-ref dist u)) ; skip outdated entries
          (for ([nbr (vector-ref adj u)])
            (match-define (list v w) nbr)
            (define nd (+ d w))
            (when (< nd (vector-ref dist v))
              (vector-set! dist v nd)
              (heap-add! heap (list nd v)))))
        (loop))))
    ;; DP with memoization
    (let ([memo (make-vector (+ n 1) -1)])
      (define (dfs u)
        (cond [(= u n) 1]
              [(not (= (vector-ref memo u) -1)) (vector-ref memo u)]
              [else
               (define total 0)
               (for ([nbr (vector-ref adj u)])
                 (match-define (list v w) nbr)
                 (when (> (vector-ref dist u) (vector-ref dist v))
                   (set! total (modulo (+ total (dfs v)) MOD))))
               (vector-set! memo u total)
               total]))
      (modulo (dfs 1) MOD))))
```

## Erlang

```erlang
-module(solution).
-export([count_restricted_paths/2]).

-define(MOD, 1000000007).

count_restricted_paths(N, Edges) ->
    Adj = build_adj(Edges, #{}),
    DistMap = dijkstra(N, Adj),
    Nodes = lists:seq(1, N),
    SortedNodes = lists:keysort(2,
        [{Node, maps:get(Node, DistMap)} || Node <- Nodes]),
    DP0 = #{N => 1},
    DP = compute_dp(SortedNodes, Adj, DistMap, DP0),
    maps:get(1, DP, 0).

build_adj([], Adj) -> Adj;
build_adj([[U,V,W]|Rest], Adj) ->
    Adj1 = add_edge(Adj, U, {V, W}),
    Adj2 = add_edge(Adj1, V, {U, W}),
    build_adj(Rest, Adj2).

add_edge(Adj, From, Edge) ->
    case maps:find(From, Adj) of
        {ok, List} -> maps:put(From, [Edge|List], Adj);
        error -> maps:put(From, [Edge], Adj)
    end.

dijkstra(N, Adj) ->
    Inf = 1 bsl 60,
    Dist0 = init_dist(N, Inf),
    Dist1 = maps:put(N, 0, Dist0),
    Heap0 = gb_tree_insert(gb_trees:empty(), 0, N),
    dijkstra_loop(Adj, Dist1, Heap0).

init_dist(N, Inf) ->
    lists:foldl(fun(I, Acc) -> maps:put(I, Inf, Acc) end,
                #{},
                lists:seq(1, N)).

dijkstra_loop(_Adj, Dist, Heap) when gb_trees:is_empty(Heap) ->
    Dist;
dijkstra_loop(Adj, Dist, Heap) ->
    {DistU, U, Heap1} = gb_tree_pop_min(Heap),
    CurrentDistU = maps:get(U, Dist),
    if
        DistU > CurrentDistU ->
            dijkstra_loop(Adj, Dist, Heap1);
        true ->
            Neighs = maps:get(U, Adj, []),
            {Dist2, Heap2} = lists:foldl(
                fun({V, W}, {DAcc, HAcc}) ->
                    NewDist = DistU + W,
                    OldDistV = maps:get(V, DAcc),
                    if
                        NewDist < OldDistV ->
                            DNew = maps:put(V, NewDist, DAcc),
                            HNew = gb_tree_insert(HAcc, NewDist, V),
                            {DNew, HNew};
                        true -> {DAcc, HAcc}
                    end
                end,
                {Dist, Heap1},
                Neighs),
            dijkstra_loop(Adj, Dist2, Heap2)
    end.

gb_tree_insert(Tree, Key, Node) ->
    case gb_trees:lookup(Key, Tree) of
        {value, List} -> gb_trees:update(Key, [Node|List], Tree);
        none -> gb_trees:insert(Key, [Node], Tree)
    end.

gb_tree_pop_min(Tree) ->
    {{Key, List}, RestTree0} = gb_trees:take_smallest(Tree),
    case List of
        [Node|Rest] ->
            NewTree = if Rest == [] -> RestTree0; true -> gb_trees:update(Key, Rest, RestTree0) end,
            {Key, Node, NewTree};
        [] -> % shouldn't happen
            gb_tree_pop_min(RestTree0)
    end.

compute_dp(SortedNodes, Adj, DistMap, DPAcc) ->
    lists:foldl(
        fun({U,_DistU}, DPPrev) ->
            case maps:is_key(U, DPPrev) of
                true -> DPPrev;
                false ->
                    Neighs = maps:get(U, Adj, []),
                    Sum = lists:foldl(
                        fun({V,_W}, Acc) ->
                            DistU = maps:get(U, DistMap),
                            DistV = maps:get(V, DistMap),
                            if
                                DistU > DistV ->
                                    (Acc + maps:get(V, DPPrev, 0)) rem ?MOD;
                                true -> Acc
                            end
                        end,
                        0,
                        Neighs),
                    maps:put(U, Sum, DPPrev)
            end
        end,
        DPAcc,
        SortedNodes).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  def count_restricted_paths(n, edges) do
    adj = build_adj(n, edges)
    dist = dijkstra(n, adj)
    count_paths(n, adj, dist)
  end

  # Build adjacency list: node => [{neighbor, weight}, ...]
  defp build_adj(_n, edges) do
    Enum.reduce(edges, %{}, fn [u, v, w], acc ->
      acc
      |> Map.update(u, [{v, w}], fn lst -> [{v, w} | lst] end)
      |> Map.update(v, [{u, w}], fn lst -> [{u, w} | lst] end)
    end)
  end

  # Dijkstra from node n to all nodes
  defp dijkstra(n, adj) do
    inf = 1_000_000_000_000
    dist0 = for i <- 1..n, into: %{}, do: {i, inf}
    dist0 = Map.put(dist0, n, 0)

    heap0 = MinHeap.push(MinHeap.new(), {0, n})
    dijkstra_loop(adj, dist0, heap0)
  end

  defp dijkstra_loop(_adj, dist, {:empty, _}) do
    dist
  end

  defp dijkstra_loop(adj, dist, heap) do
    case MinHeap.pop(heap) do
      {{:ok, {d, u}}, new_heap} ->
        if d > Map.get(dist, u) do
          dijkstra_loop(adj, dist, new_heap)
        else
          {dist2, heap2} =
            Enum.reduce(Map.get(adj, u, []), {dist, new_heap}, fn {v, w},
                                                                {dacc, hacc} ->
              nd = d + w

              if nd < Map.get(dacc, v) do
                dacc = Map.put(dacc, v, nd)
                hacc = MinHeap.push(hacc, {nd, v})
                {dacc, hacc}
              else
                {dacc, hacc}
              end
            end)

          dijkstra_loop(adj, dist2, heap2)
        end

      {:empty, _} ->
        dist
    end
  end

  # Count restricted paths using DP on DAG induced by distance ordering
  defp count_paths(n, adj, dist) do
    mod = 1_000_000_007

    nodes_sorted =
      Enum.sort_by(1..n, fn i -> Map.get(dist, i) end)

    dp_initial = %{n => 1}

    {dp, _} =
      Enum.reduce(nodes_sorted, {dp_initial, nil}, fn node,
                                                      {dp_acc, _} ->
        if node == n do
          {dp_acc, nil}
        else
          sum =
            Enum.reduce(Map.get(adj, node, []), 0, fn {v, _w}, acc ->
              if Map.get(dist, node) > Map.get(dist, v) do
                rem(acc + Map.get(dp_acc, v, 0), mod)
              else
                acc
              end
            end)

          dp_acc = Map.put(dp_acc, node, sum)
          {dp_acc, nil}
        end
      end)

    Map.get(dp, 1, 0)
  end

  # Simple binary min-heap implementation using a map for index storage
  defmodule MinHeap do
    @moduledoc false

    def new(), do: {0, %{}}

    def push({size, map}, elem) do
      idx = size + 1
      map = Map.put(map, idx, elem)
      bubble_up(idx, size + 1, map)
    end

    defp bubble_up(1, size, map), do: {size, map}

    defp bubble_up(idx, size, map) when idx > 1 do
      parent = div(idx, 2)

      {c_dist, _} = Map.fetch!(map, idx)
      {p_dist, _} = Map.fetch!(map, parent)

      if c_dist < p_dist do
        c_elem = Map.get(map, idx)
        p_elem = Map.get(map, parent)

        map =
          map
          |> Map.put(idx, p_elem)
          |> Map.put(parent, c_elem)

        bubble_up(parent, size, map)
      else
        {size, map}
      end
    end

    def pop({0, _} = heap), do: {:empty, heap}

    def pop({size, map}) do
      min = Map.fetch!(map, 1)

      if size == 1 do
        {{:ok, min}, {0, %{}}}
      else
        last = Map.fetch!(map, size)
        map = map |> Map.put(1, last) |> Map.delete(size)
        bubble_down(1, size - 1, map) |> then(fn {new_size, new_map} ->
          {{:ok, min}, {new_size, new_map}}
        end)
      end
    end

    defp bubble_down(idx, size, map) do
      left = idx * 2
      right = left + 1

      smallest =
        cond do
          left <= size and elem(Map.fetch!(map, left), 0) < elem(Map.fetch!(map, idx), 0) ->
            left

          true ->
            idx
        end

      smallest =
        if right <= size and elem(Map.fetch!(map, right), 0) <
             elem(Map.fetch!(map, smallest), 0) do
          right
        else
          smallest
        end

      if smallest != idx do
        elem_idx = Map.get(map, idx)
        elem_small = Map.get(map, smallest)

        map =
          map
          |> Map.put(idx, elem_small)
          |> Map.put(smallest, elem_idx)

        bubble_down(smallest, size, map)
      else
        {size, map}
      end
    end
  end
end
```

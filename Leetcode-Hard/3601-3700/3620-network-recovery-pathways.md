# 3620. Network Recovery Pathways

## Cpp

```cpp
class Solution {
public:
    int findMaxPathScore(vector<vector<int>>& edges, vector<bool>& online, long long k) {
        int n = online.size();
        vector<vector<pair<int,int>>> adj(n);
        vector<int> indeg(n, 0);
        int maxCost = 0;
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            ++indeg[v];
            if (w > maxCost) maxCost = w;
        }
        // Topological order
        queue<int> q;
        for (int i = 0; i < n; ++i) if (indeg[i] == 0) q.push(i);
        vector<int> topo;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            topo.push_back(u);
            for (auto &p : adj[u]) {
                int v = p.first;
                if (--indeg[v] == 0) q.push(v);
            }
        }
        auto feasible = [&](int minEdge) -> bool {
            const long long INF = (1LL << 60);
            vector<long long> dp(n, INF);
            if (!online[0]) return false;
            dp[0] = 0;
            for (int u : topo) {
                if (!online[u]) continue;
                long long du = dp[u];
                if (du == INF) continue;
                for (auto &p : adj[u]) {
                    int v = p.first, w = p.second;
                    if (w < minEdge) continue;
                    if (!online[v]) continue;
                    long long nd = du + w;
                    if (nd < dp[v]) dp[v] = nd;
                }
            }
            return dp[n - 1] <= k;
        };
        int lo = 0, hi = maxCost, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private List<int[]>[] graph;
    private int[] topoOrder;
    private boolean[] online;
    private long limitK;
    private int n;

    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        this.n = online.length;
        this.online = online;
        this.limitK = k;
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        int[] indeg = new int[n];
        int maxCost = 0;
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].add(new int[]{v, w});
            indeg[v]++;
            if (w > maxCost) maxCost = w;
        }
        topoOrder = new int[n];
        int idx = 0;
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) dq.add(i);
        while (!dq.isEmpty()) {
            int u = dq.poll();
            topoOrder[idx++] = u;
            for (int[] e : graph[u]) {
                int v = e[0];
                indeg[v]--;
                if (indeg[v] == 0) dq.add(v);
            }
        }

        int lo = 0, hi = maxCost;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return can(lo) ? lo : -1;
    }

    private boolean can(int minEdge) {
        long INF = Long.MAX_VALUE / 4;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        if (!online[0]) return false;
        dist[0] = 0L;

        for (int u : topoOrder) {
            if (!online[u]) continue;
            long du = dist[u];
            if (du == INF) continue;
            for (int[] e : graph[u]) {
                int v = e[0];
                int w = e[1];
                if (w < minEdge) continue;
                if (!online[v]) continue;
                long nd = du + w;
                if (nd < dist[v]) dist[v] = nd;
            }
        }
        return dist[n - 1] <= limitK;
    }
}
```

## Python

```python
class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        max_cost = 0
        for u, v, w in edges:
            adj[u].append((v, w))
            indeg[v] += 1
            if online[u] and online[v]:
                if w > max_cost:
                    max_cost = w

        # topological order (Kahn)
        from collections import deque
        q = deque([i for i in range(n) if indeg[i] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        INF = 10**18

        def feasible(threshold):
            # shortest path using only edges with weight >= threshold and online nodes
            dist = [INF] * n
            if not online[0]:
                return False
            dist[0] = 0
            for u in topo:
                if not online[u] or dist[u] == INF:
                    continue
                du = dist[u]
                for v, w in adj[u]:
                    if not online[v] or w < threshold:
                        continue
                    nd = du + w
                    if nd < dist[v]:
                        dist[v] = nd
            return dist[n - 1] <= k

        # quick check: any path at all?
        if not feasible(0):
            return -1

        lo, hi = 0, max_cost
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        max_cost = 0
        for u, v, w in edges:
            adj[u].append((v, w))
            indeg[v] += 1
            if w > max_cost:
                max_cost = w

        # topological order of the whole DAG
        q = deque([i for i in range(n) if indeg[i] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        INF = 10**20

        def feasible(threshold: int) -> bool:
            dist = [INF] * n
            if not online[0]:
                return False
            dist[0] = 0
            for u in topo:
                if not online[u]:
                    continue
                du = dist[u]
                if du == INF:
                    continue
                for v, w in adj[u]:
                    if w < threshold or not online[v]:
                        continue
                    nd = du + w
                    if nd < dist[v]:
                        dist[v] = nd
            return dist[n - 1] <= k

        # quick check: any path at all?
        if not feasible(0):
            return -1

        lo, hi = 0, max_cost
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int to;
    int cost;
    int next;
} Edge;

static int n;
static bool *onlineArr;
static long long K;
static Edge *edgesArr;
static int *head;
static int *topoOrder;

/* Check if there exists a path from 0 to n-1 using only edges with
   cost >= thr and total sum <= K. */
static bool feasible(int thr) {
    const long long INF = LLONG_MAX / 4;
    long long *dist = (long long *)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; ++i) dist[i] = INF;
    if (!onlineArr[0]) { free(dist); return false; }
    dist[0] = 0;

    for (int idx = 0; idx < n; ++idx) {
        int u = topoOrder[idx];
        if (!onlineArr[u]) continue;
        long long du = dist[u];
        if (du == INF) continue;
        for (int e = head[u]; e != -1; e = edgesArr[e].next) {
            int v = edgesArr[e].to;
            int c = edgesArr[e].cost;
            if (c < thr) continue;
            if (!onlineArr[v]) continue;
            long long nd = du + (long long)c;
            if (nd < dist[v]) dist[v] = nd;
        }
    }

    bool ok = (dist[n - 1] != INF && dist[n - 1] <= K);
    free(dist);
    return ok;
}

int findMaxPathScore(int** edges, int edgesSize, int* edgesColSize,
                     bool* online, int onlineSize, long long k) {
    n = onlineSize;
    onlineArr = online;
    K = k;

    head = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;

    edgesArr = (Edge *)malloc(sizeof(Edge) * edgesSize);
    int *indeg = (int *)calloc(n, sizeof(int));

    int maxCost = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int c = edges[i][2];
        edgesArr[i].to = v;
        edgesArr[i].cost = c;
        edgesArr[i].next = head[u];
        head[u] = i;
        indeg[v]++;
        if (c > maxCost) maxCost = c;
    }

    /* Topological order using Kahn's algorithm */
    int *queue = (int *)malloc(sizeof(int) * n);
    int qh = 0, qt = 0;
    for (int i = 0; i < n; ++i)
        if (indeg[i] == 0) queue[qt++] = i;

    topoOrder = (int *)malloc(sizeof(int) * n);
    int orderCnt = 0;
    while (qh < qt) {
        int u = queue[qh++];
        topoOrder[orderCnt++] = u;
        for (int e = head[u]; e != -1; e = edgesArr[e].next) {
            int v = edgesArr[e].to;
            if (--indeg[v] == 0) queue[qt++] = v;
        }
    }

    free(queue);
    free(indeg);

    int lo = 0, hi = maxCost, ans = -1;
    while (lo <= hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (feasible(mid)) {
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    free(head);
    free(edgesArr);
    free(topoOrder);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int FindMaxPathScore(int[][] edges, bool[] online, long k) {
        int n = online.Length;
        var adj = new List<(int to, int cost)>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<(int, int)>();
        int[] indeg = new int[n];
        int maxCost = 0;
        foreach (var e in edges) {
            int u = e[0], v = e[1], c = e[2];
            adj[u].Add((v, c));
            indeg[v]++;
            if (c > maxCost) maxCost = c;
        }

        var q = new Queue<int>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.Enqueue(i);
        var topo = new List<int>(n);
        while (q.Count > 0) {
            int u = q.Dequeue();
            topo.Add(u);
            foreach (var (v, _) in adj[u]) {
                indeg[v]--;
                if (indeg[v] == 0) q.Enqueue(v);
            }
        }

        bool Feasible(int minEdge) {
            const long INF = long.MaxValue / 4;
            var dist = new long[n];
            for (int i = 0; i < n; i++) dist[i] = INF;
            if (!online[0]) return false;
            dist[0] = 0;
            foreach (int u in topo) {
                if (!online[u]) continue;
                long du = dist[u];
                if (du == INF) continue;
                foreach (var (v, cost) in adj[u]) {
                    if (cost < minEdge) continue;
                    if (!online[v]) continue;
                    long nd = du + cost;
                    if (nd < dist[v]) dist[v] = nd;
                }
            }
            return dist[n - 1] != INF && dist[n - 1] <= k;
        }

        int lo = 0, hi = maxCost, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (Feasible(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {boolean[]} online
 * @param {number} k
 * @return {number}
 */
var findMaxPathScore = function(edges, online, k) {
    const n = online.length;
    if (n === 0) return -1;

    // Build adjacency list and indegree for topological order
    const adj = Array.from({length: n}, () => []);
    const indeg = new Int32Array(n);
    let maxCost = 0;
    for (let i = 0; i < edges.length; ++i) {
        const [u, v, c] = edges[i];
        adj[u].push([v, c]);
        indeg[v]++;
        if (c > maxCost) maxCost = c;
    }

    // Topological order using Kahn's algorithm
    const queue = new Array(n);
    let qh = 0, qt = 0;
    for (let i = 0; i < n; ++i) {
        if (indeg[i] === 0) queue[qt++] = i;
    }
    const topo = [];
    while (qh < qt) {
        const u = queue[qh++];
        topo.push(u);
        const edgesU = adj[u];
        for (let j = 0; j < edgesU.length; ++j) {
            const v = edgesU[j][0];
            indeg[v]--;
            if (indeg[v] === 0) queue[qt++] = v;
        }
    }

    // Feasibility check for a given threshold mid
    function feasible(mid) {
        const dist = new Array(n).fill(Infinity);
        dist[0] = 0; // online[0] guaranteed true

        for (let i = 0; i < topo.length; ++i) {
            const u = topo[i];
            if (!online[u]) continue;
            const du = dist[u];
            if (du === Infinity) continue;

            const edgesU = adj[u];
            for (let j = 0; j < edgesU.length; ++j) {
                const [v, c] = edgesU[j];
                if (c < mid) continue;
                if (!online[v]) continue;
                const nd = du + c;
                if (nd < dist[v]) dist[v] = nd;
            }
        }
        return dist[n - 1] <= k;
    }

    // If even threshold 0 is not feasible, answer is -1
    if (!feasible(0)) return -1;

    let lo = 0, hi = maxCost;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (feasible(mid)) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    return lo;
};
```

## Typescript

```typescript
function findMaxPathScore(edges: number[][], online: boolean[], k: number): number {
    const n = online.length;
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    const indeg = new Int32Array(n);
    let maxCost = 0;

    for (const e of edges) {
        const u = e[0], v = e[1], c = e[2];
        adj[u].push([v, c]);
        indeg[v]++;
        if (c > maxCost) maxCost = c;
    }

    // topological order of the whole DAG
    const queue: number[] = [];
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0) queue.push(i);
    }
    const topo: number[] = [];
    let qIdx = 0;
    while (qIdx < queue.length) {
        const u = queue[qIdx++];
        topo.push(u);
        for (const [v] of adj[u]) {
            indeg[v]--;
            if (indeg[v] === 0) queue.push(v);
        }
    }

    function feasible(threshold: number): boolean {
        const INF = Number.MAX_SAFE_INTEGER;
        const dist = new Array<number>(n).fill(INF);
        if (!online[0]) return false; // safety, though guaranteed true
        dist[0] = 0;

        for (const u of topo) {
            if (!online[u]) continue;
            const du = dist[u];
            if (du === INF) continue;
            for (const [v, c] of adj[u]) {
                if (c >= threshold && online[v]) {
                    const nd = du + c;
                    if (nd < dist[v]) dist[v] = nd;
                }
            }
        }
        return dist[n - 1] <= k;
    }

    let low = 0, high = maxCost, ans = -1;
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (feasible(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $edges
     * @param Boolean[] $online
     * @param Integer $k
     * @return Integer
     */
    function findMaxPathScore($edges, $online, $k) {
        $n = count($online);
        // Build adjacency list and indegree for topological order
        $adj = array_fill(0, $n, []);
        $indeg = array_fill(0, $n, 0);
        $maxCost = 0;
        foreach ($edges as $e) {
            [$u, $v, $c] = $e;
            $adj[$u][] = [$v, $c];
            $indeg[$v]++;
            if ($c > $maxCost) $maxCost = $c;
        }
        // Topological sort (Kahn's algorithm)
        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] == 0) $queue->enqueue($i);
        }
        $topo = [];
        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            $topo[] = $u;
            foreach ($adj[$u] as $edge) {
                $v = $edge[0];
                $indeg[$v]--;
                if ($indeg[$v] == 0) $queue->enqueue($v);
            }
        }
        // Helper function to test a threshold
        $can = function(int $thr) use ($adj, $online, $topo, $k, $n): bool {
            $INF = PHP_INT_MAX;
            $dist = array_fill(0, $n, $INF);
            if (!$online[0]) return false;
            $dist[0] = 0;
            foreach ($topo as $u) {
                if (!$online[$u]) continue;
                $du = $dist[$u];
                if ($du === $INF) continue;
                foreach ($adj[$u] as $edge) {
                    [$v, $c] = $edge;
                    if (!$online[$v]) continue;
                    if ($c < $thr) continue;
                    $new = $du + $c;
                    if ($new < $dist[$v]) {
                        $dist[$v] = $new;
                    }
                }
            }
            return $dist[$n - 1] <= $k;
        };
        // Binary search on answer
        $low = 0;
        $high = $maxCost;
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($can($mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $can($low) ? $low : -1;
    }
}
```

## Swift

```swift
class Solution {
    func findMaxPathScore(_ edges: [[Int]], _ online: [Bool], _ k: Int) -> Int {
        let n = online.count
        var adj = Array(repeating: [(to: Int, w: Int)](), count: n)
        var indeg = Array(repeating: 0, count: n)
        var maxCost = 0
        
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            if !online[u] || !online[v] { continue }
            adj[u].append((to: v, w: w))
            indeg[v] += 1
            if w > maxCost { maxCost = w }
        }
        
        // Topological order (Kahn's algorithm)
        var queue = [Int]()
        for i in 0..<n where online[i] && indeg[i] == 0 {
            queue.append(i)
        }
        var order = [Int]()
        var idx = 0
        while idx < queue.count {
            let u = queue[idx]
            idx += 1
            order.append(u)
            for edge in adj[u] {
                indeg[edge.to] -= 1
                if indeg[edge.to] == 0 && online[edge.to] {
                    queue.append(edge.to)
                }
            }
        }
        
        let INF = Int64.max / 4
        func feasible(_ minEdge: Int) -> Bool {
            var dist = Array(repeating: INF, count: n)
            dist[0] = 0
            for u in order {
                if dist[u] == INF { continue }
                for edge in adj[u] {
                    if edge.w < minEdge { continue }
                    let v = edge.to
                    let nd = dist[u] + Int64(edge.w)
                    if nd < dist[v] {
                        dist[v] = nd
                    }
                }
            }
            return dist[n - 1] <= Int64(k)
        }
        
        var left = 0, right = maxCost, ans = -1
        while left <= right {
            let mid = (left + right) / 2
            if feasible(mid) {
                ans = mid
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    data class Edge(val to: Int, val w: Int)

    fun findMaxPathScore(edges: Array<IntArray>, online: BooleanArray, k: Long): Int {
        val n = online.size
        val adj = Array(n) { mutableListOf<Edge>() }
        val indeg = IntArray(n)
        var maxCost = 0
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Edge(v, w))
            indeg[v]++
            if (w > maxCost) maxCost = w
        }

        // topological order of the whole DAG
        val topo = IntArray(n)
        var tIdx = 0
        val q: ArrayDeque<Int> = ArrayDeque()
        for (i in 0 until n) {
            if (indeg[i] == 0) q.add(i)
        }
        while (!q.isEmpty()) {
            val u = q.removeFirst()
            topo[tIdx++] = u
            for (e in adj[u]) {
                indeg[e.to]--
                if (indeg[e.to] == 0) q.add(e.to)
            }
        }

        fun feasible(threshold: Int): Boolean {
            val INF = Long.MAX_VALUE / 4
            val dist = LongArray(n) { INF }
            if (!online[0]) return false
            dist[0] = 0L
            for (u in topo) {
                if (!online[u]) continue
                val du = dist[u]
                if (du == INF) continue
                for (e in adj[u]) {
                    if (e.w < threshold) continue
                    val v = e.to
                    if (!online[v]) continue
                    val nd = du + e.w
                    if (nd < dist[v]) {
                        dist[v] = nd
                    }
                }
            }
            return dist[n - 1] <= k
        }

        var lo = 0
        var hi = maxCost
        var ans = -1
        while (lo <= hi) {
            val mid = lo + ((hi - lo) ushr 1)
            if (feasible(mid)) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';

class _Edge {
  final int to;
  final int cost;
  _Edge(this.to, this.cost);
}

class Solution {
  int findMaxPathScore(List<List<int>> edges, List<bool> online, int k) {
    int n = online.length;
    List<List<_Edge>> adj = List.generate(n, (_) => []);
    List<int> indeg = List.filled(n, 0);
    int maxCost = 0;

    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      int w = e[2];
      adj[u].add(_Edge(v, w));
      indeg[v]++;
      if (w > maxCost) maxCost = w;
    }

    // Topological order using Kahn's algorithm
    List<int> topo = [];
    Queue<int> q = Queue<int>();
    for (int i = 0; i < n; i++) {
      if (indeg[i] == 0) q.add(i);
    }
    while (q.isNotEmpty) {
      int u = q.removeFirst();
      topo.add(u);
      for (var e in adj[u]) {
        indeg[e.to]--;
        if (indeg[e.to] == 0) q.add(e.to);
      }
    }

    bool feasible(int minEdge) {
      const int INF = 1 << 60;
      List<int> dist = List.filled(n, INF);
      if (!online[0]) return false; // safety, though guaranteed true
      dist[0] = 0;

      for (int u in topo) {
        if (!online[u]) continue;
        int du = dist[u];
        if (du == INF) continue;
        for (var e in adj[u]) {
          if (e.cost < minEdge) continue;
          int v = e.to;
          if (!online[v]) continue;
          int nd = du + e.cost;
          if (nd < dist[v]) dist[v] = nd;
        }
      }
      return dist[n - 1] <= k;
    }

    int left = 0, right = maxCost;
    int ans = -1;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      if (feasible(mid)) {
        ans = mid;
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
type edge struct {
	to   int
	cost int64
}

func findMaxPathScore(edges [][]int, online []bool, k int64) int {
	n := len(online)
	adj := make([][]edge, n)
	indeg := make([]int, n)
	maxCost := 0

	for _, e := range edges {
		u, v, c := e[0], e[1], e[2]
		adj[u] = append(adj[u], edge{to: v, cost: int64(c)})
		indeg[v]++
		if c > maxCost {
			maxCost = c
		}
	}

	// topological order (Kahn's algorithm)
	order := make([]int, 0, n)
	queue := make([]int, 0)
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			queue = append(queue, i)
		}
	}
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		order = append(order, u)
		for _, e := range adj[u] {
			indeg[e.to]--
			if indeg[e.to] == 0 {
				queue = append(queue, e.to)
			}
		}
	}

	const INF int64 = 1<<63 - 1

	feasible := func(th int) bool {
		dist := make([]int64, n)
		for i := 0; i < n; i++ {
			dist[i] = INF
		}
		if !online[0] {
			return false
		}
		dist[0] = 0

		for _, u := range order {
			if !online[u] || dist[u] == INF {
				continue
			}
			for _, e := range adj[u] {
				if !online[e.to] {
					continue
				}
				if e.cost < int64(th) {
					continue
				}
				newDist := dist[u] + e.cost
				if newDist < dist[e.to] {
					dist[e.to] = newDist
				}
			}
		}
		return dist[n-1] != INF && dist[n-1] <= k
	}

	if !feasible(0) {
		return -1
	}

	lo, hi := 0, maxCost+1
	for lo+1 < hi {
		mid := (lo + hi) / 2
		if feasible(mid) {
			lo = mid
		} else {
			hi = mid
		}
	}
	return lo
}
```

## Ruby

```ruby
def find_max_path_score(edges, online, k)
  n = online.length
  adj = Array.new(n) { [] }
  indeg = Array.new(n, 0)
  max_cost = 0

  edges.each do |u, v, c|
    adj[u] << [v, c]
    indeg[v] += 1
    max_cost = c if c > max_cost
  end

  # Topological order (Kahn's algorithm)
  queue = []
  indeg.each_with_index { |d, i| queue << i if d.zero? }
  topo = []
  q_idx = 0
  while q_idx < queue.size
    u = queue[q_idx]
    q_idx += 1
    topo << u
    adj[u].each do |v, _|
      indeg[v] -= 1
      queue << v if indeg[v].zero?
    end
  end

  feasible = lambda do |threshold|
    INF = (1 << 62)
    dist = Array.new(n, INF)
    return false unless online[0]
    dist[0] = 0

    topo.each do |u|
      next unless online[u]
      du = dist[u]
      next if du == INF
      adj[u].each do |v, cost|
        next unless online[v]
        next if cost < threshold
        nd = du + cost
        next if nd > k
        dist[v] = nd if nd < dist[v]
      end
    end

    dist[n - 1] <= k
  end

  ans = -1
  l = 0
  r = max_cost
  while l <= r
    mid = (l + r) / 2
    if feasible.call(mid)
      ans = mid
      l = mid + 1
    else
      r = mid - 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def findMaxPathScore(edges: Array[Array[Int]], online: Array[Boolean], k: Long): Int = {
    val n = online.length
    import scala.collection.mutable.ArrayBuffer
    val adj = Array.fill(n)(new ArrayBuffer[(Int, Int)]())
    var maxCost = 0
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val c = e(2)
      adj(u).append((v, c))
      if (c > maxCost) maxCost = c
    }

    def feasible(threshold: Int): Boolean = {
      if (!online(0) || !online(n - 1)) return false
      val INF = Long.MaxValue / 4
      val dist = Array.fill[Long](n)(INF)
      val pq = new java.util.PriorityQueue[(Long, Int)](
        new java.util.Comparator[(Long, Int)] {
          override def compare(a: (Long, Int), b: (Long, Int)): Int =
            java.lang.Long.compare(a._1, b._1)
        }
      )
      dist(0) = 0L
      pq.offer((0L, 0))
      while (!pq.isEmpty) {
        val cur = pq.poll()
        val d = cur._1
        val u = cur._2
        if (d != dist(u)) {
          // outdated entry
        } else {
          for ((v, cost) <- adj(u)) {
            if (online(v) && cost >= threshold) {
              val nd = d + cost.toLong
              if (nd < dist(v) && nd <= k) {
                dist(v) = nd
                pq.offer((nd, v))
              }
            }
          }
        }
      }
      dist(n - 1) <= k
    }

    var low = 0
    var high = maxCost
    while (low < high) {
      val mid = low + (high - low + 1) / 2
      if (feasible(mid)) low = mid else high = mid - 1
    }
    if (feasible(low)) low else -1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_max_path_score(edges: Vec<Vec<i32>>, online: Vec<bool>, k: i64) -> i32 {
        let n = online.len();
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n];
        let mut indeg = vec![0usize; n];
        let mut max_cost = 0i64;
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as i64;
            adj[u].push((v, w));
            indeg[v] += 1;
            if w > max_cost {
                max_cost = w;
            }
        }

        // Topological order (graph is a DAG)
        use std::collections::VecDeque;
        let mut q = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }
        let mut topo = Vec::with_capacity(n);
        while let Some(u) = q.pop_front() {
            topo.push(u);
            for &(v, _) in adj[u].iter() {
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    q.push_back(v);
                }
            }
        }

        fn possible(
            threshold: i64,
            n: usize,
            online: &Vec<bool>,
            k: i64,
            topo: &Vec<usize>,
            adj: &Vec<Vec<(usize, i64)>>,
        ) -> bool {
            const INF: i64 = i64::MAX / 4;
            let mut dist = vec![INF; n];
            if !online[0] {
                return false;
            }
            dist[0] = 0;
            for &u in topo.iter() {
                if !online[u] {
                    continue;
                }
                let du = dist[u];
                if du == INF {
                    continue;
                }
                for &(v, w) in adj[u].iter() {
                    if w < threshold || !online[v] {
                        continue;
                    }
                    let nd = du + w;
                    if nd < dist[v] {
                        dist[v] = nd;
                    }
                }
            }
            dist[n - 1] <= k
        }

        let mut lo = 0i64;
        let mut hi = max_cost;
        let mut ans = -1i32;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if possible(mid, n, &online, k, &topo, &adj) {
                ans = mid as i32;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-max-path-score edges online k)
  (-> (listof (listof exact-integer?)) (listof boolean?) exact-integer? exact-integer?)
  (let* ((n (length online))
         (online-vec (list->vector online))
         (adj (make-vector n '()))
         (indeg (make-vector n 0)))
    ;; build adjacency list and indegrees
    (for ([e edges])
      (let* ((u (list-ref e 0))
             (v (list-ref e 1))
             (c (list-ref e 2)))
        (vector-set! adj u (cons (list v c) (vector-ref adj u)))
        (vector-set! indeg v (+ (vector-ref indeg v) 1))))
    ;; topological order (Kahn)
    (define queue (make-vector n 0))
    (define qhead 0)
    (define qtail 0)
    (for ([i (in-range n)])
      (when (= (vector-ref indeg i) 0)
        (vector-set! queue qtail i)
        (set! qtail (+ qtail 1))))
    (define topo-rev '())
    (let loop ()
      (when (< qhead qtail)
        (let ((u (vector-ref queue qhead)))
          (set! qhead (+ qhead 1))
          (set! topo-rev (cons u topo-rev))
          (for ([edge (vector-ref adj u)])
            (let ((v (list-ref edge 0)))
              (vector-set! indeg v (- (vector-ref indeg v) 1))
              (when (= (vector-ref indeg v) 0)
                (vector-set! queue qtail v)
                (set! qtail (+ qtail 1))))))
        (loop)))
    (define topo (reverse topo-rev))
    ;; max edge cost
    (define max-cost -1)
    (for ([e edges])
      (let ((c (list-ref e 2)))
        (when (> c max-cost) (set! max-cost c))))
    (if (= max-cost -1)
        -1
        (let loop-binary ((lo 0) (hi max-cost) (ans -1))
          (if (> lo hi)
              ans
              (let* ((mid (quotient (+ lo hi) 2))
                     (feasible
                      (let ()
                        (define INF (expt 10 18))
                        (define dist (make-vector n INF))
                        (vector-set! dist 0 0)
                        (for ([u topo])
                          (when (and (vector-ref online-vec u)
                                     (< (vector-ref dist u) INF))
                            (for ([edge (vector-ref adj u)])
                              (let* ((v (list-ref edge 0))
                                     (c (list-ref edge 1)))
                                (when (and (>= c mid) (vector-ref online-vec v))
                                  (define newd (+ (vector-ref dist u) c))
                                  (when (< newd (vector-ref dist v))
                                    (vector-set! dist v newd)))))))
                        (let ((final (vector-ref dist (- n 1))))
                          (and (< final INF) (<= final k))))) )
                (if feasible
                    (loop-binary (+ mid 1) hi mid)
                    (loop-binary lo (- mid 1) ans)))))))))
```

## Erlang

```erlang
-module(solution).
-export([find_max_path_score/3]).

-spec find_max_path_score(Edges :: [[integer()]], Online :: [boolean()], K :: integer()) -> integer().
find_max_path_score(Edges, Online, K) ->
    N = length(Online),
    {AdjMap, IndegMap} = build_graph(Edges, #{}, #{}),
    TopoOrder = topo_sort(N, AdjMap, IndegMap),
    OnlineMap = maps:from_list(lists:zip(lists:seq(0, N - 1), Online)),
    MaxCost = max_edge_cost(Edges, 0),
    case feasible(0, N, K, AdjMap, TopoOrder, OnlineMap) of
        false -> -1;
        true ->
            binary_search(0, MaxCost, N, K, AdjMap, TopoOrder, OnlineMap)
    end.

build_graph([], Adj, Indeg) -> {Adj, Indeg};
build_graph([[U, V, C] | Rest], Adj, Indeg) ->
    Adj1 = maps:update_with(U,
            fun(L) -> [{V, C} | L] end,
            [{V, C}],
            Adj),
    Indeg1 = maps:update_with(V,
            fun(I) -> I + 1 end,
            1,
            Indeg),
    build_graph(Rest, Adj1, Indeg1).

topo_sort(N, AdjMap, IndegMap) ->
    Queue0 = [Node || Node <- lists:seq(0, N - 1), maps:get(Node, IndegMap, 0) == 0],
    loop_topo(Queue0, IndegMap, AdjMap, []).

loop_topo([], _Indeg, _Adj, Order) -> lists:reverse(Order);
loop_topo([H | T], Indeg, Adj, Order) ->
    Neighs = maps:get(H, Adj, []),
    {NewIndeg, NewQueue} = lists:foldl(
        fun({V, _C}, {IAcc, QAcc}) ->
            Cur = maps:get(V, IAcc, 0) - 1,
            I2 = maps:put(V, Cur, IAcc),
            if Cur == 0 -> {I2, [V | QAcc]};
               true -> {I2, QAcc}
            end
        end,
        {Indeg, T},
        Neighs),
    loop_topo(NewQueue, NewIndeg, Adj, [H | Order]).

max_edge_cost([], Max) -> Max;
max_edge_cost([[_, _, C] | Rest], Max) ->
    max_edge_cost(Rest, erlang:max(C, Max)).

feasible(MinEdge, N, K, AdjMap, TopoOrder, OnlineMap) ->
    Inf = K + 1,
    Dist0 = maps:put(0, 0, #{}),
    DistMap = lists:foldl(
        fun(Node, DAcc) ->
            case maps:get(Node, OnlineMap) of
                false -> DAcc;
                true ->
                    DistU = maps:get(Node, DAcc, Inf),
                    if DistU > K -> DAcc;
                       true ->
                           Neighs = maps:get(Node, AdjMap, []),
                           lists:foldl(
                               fun({V, C}, DInner) ->
                                   case maps:get(V, OnlineMap) of
                                       false -> DInner;
                                       true ->
                                           if C >= MinEdge ->
                                                   NewDist = DistU + C,
                                                   OldDistV = maps:get(V, DInner, Inf),
                                                   if NewDist < OldDistV ->
                                                          maps:put(V, NewDist, DInner);
                                                      true -> DInner
                                                   end;
                                              true -> DInner
                                           end
                                   end
                               end,
                               DAcc,
                               Neighs)
                    end
            end
        end,
        Dist0,
        TopoOrder),
    case maps:get(N - 1, DistMap, Inf) of
        D when D =< K -> true;
        _ -> false
    end.

binary_search(Low, High, N, K, AdjMap, TopoOrder, OnlineMap) ->
    binary_search_loop(Low, High, N, K, AdjMap, TopoOrder, OnlineMap).

binary_search_loop(Low, High, N, K, AdjMap, TopoOrder, OnlineMap) when Low < High ->
    Mid = (Low + High + 1) div 2,
    case feasible(Mid, N, K, AdjMap, TopoOrder, OnlineMap) of
        true -> binary_search_loop(Mid, High, N, K, AdjMap, TopoOrder, OnlineMap);
        false -> binary_search_loop(Low, Mid - 1, N, K, AdjMap, TopoOrder, OnlineMap)
    end;
binary_search_loop(Ans, _High, _N, _K, _AdjMap, _TopoOrder, _OnlineMap) ->
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_path_score(edges :: [[integer]], online :: [boolean], k :: integer) :: integer
  def find_max_path_score(edges, online, k) do
    n = length(online)

    {adj, indeg_arr} = build_graph(edges, n)
    order = topological_order(adj, indeg_arr, n)
    online_arr = :array.from_list(online)

    max_cost =
      case edges do
        [] -> -1
        _ -> Enum.map(edges, fn [_u, _v, c] -> c end) |> Enum.max()
      end

    if max_cost == -1 do
      -1
    else
      binary_search(0, max_cost, -1, n, adj, online_arr, order, k)
    end
  end

  defp build_graph(edges, n) do
    indeg = :array.new(n, default: 0)

    {adj, indeg} =
      Enum.reduce(edges, {%{}, indeg}, fn [u, v, c], {a, ind} ->
        a2 = Map.update(a, u, [{v, c}], fn lst -> [{v, c} | lst] end)
        cur = :array.get(v, ind)
        ind2 = :array.set(v, cur + 1, ind)
        {a2, ind2}
      end)

    {adj, indeg}
  end

  defp topological_order(adj, indeg_arr, n) do
    zeros =
      0..(n - 1)
      |> Enum.filter(fn i -> :array.get(i, indeg_arr) == 0 end)

    q = :queue.from_list(zeros)
    {order_rev, _} = kahn(q, [], indeg_arr, adj)
    Enum.reverse(order_rev)
  end

  defp kahn(queue, order_rev, indeg_arr, adj) do
    case :queue.out(queue) do
      {:empty, _} ->
        {order_rev, indeg_arr}

      {{:value, node}, q2} ->
        {indeg_updated, q_updated} =
          Enum.reduce(Map.get(adj, node, []), {indeg_arr, q2}, fn {v, _c},
                                                               {ind, qq} ->
            cur = :array.get(v, ind)
            new = cur - 1
            ind2 = :array.set(v, new, ind)

            if new == 0 do
              {ind2, :queue.in(v, qq)}
            else
              {ind2, qq}
            end
          end)

        kahn(q_updated, [node | order_rev], indeg_updated, adj)
    end
  end

  defp binary_search(lo, hi, ans, n, adj, online_arr, order, k) when lo <= hi do
    mid = div(lo + hi, 2)

    if feasible?(mid, n, adj, online_arr, order, k) do
      binary_search(mid + 1, hi, mid, n, adj, online_arr, order, k)
    else
      binary_search(lo, mid - 1, ans, n, adj, online_arr, order, k)
    end
  end

  defp binary_search(_lo, _hi, ans, _n, _adj, _online_arr, _order, _k), do: ans

  defp feasible?(threshold, n, adj, online_arr, order, k) do
    inf = :erlang.max(k + 1, 1 <<< 60)
    dist0 = :array.new(n, default: inf)
    dist = :array.set(0, 0, dist0)

    final_dist =
      Enum.reduce(order, dist, fn node, d_arr ->
        if not :array.get(node, online_arr) do
          d_arr
        else
          cur = :array.get(node, d_arr)

          if cur > k do
            d_arr
          else
            Enum.reduce(Map.get(adj, node, []), d_arr, fn {v, c}, acc ->
              if c >= threshold and :array.get(v, online_arr) do
                nd = cur + c

                prev = :array.get(v, acc)

                if nd < prev do
                  :array.set(v, nd, acc)
                else
                  acc
                end
              else
                acc
              end
            end)
          end
        end
      end)

    :array.get(n - 1, final_dist) <= k
  end
end
```

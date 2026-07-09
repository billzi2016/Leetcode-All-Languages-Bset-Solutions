# 3553. Minimum Weighted Subgraph With the Required Paths II

## Cpp

```cpp
class Solution {
public:
    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        int LOG = 1;
        while ((1 << LOG) <= n) ++LOG;
        vector<vector<int>> parent(LOG, vector<int>(n));
        vector<int> depth(n, 0);
        vector<long long> dist(n, 0);
        
        // iterative DFS/BFS to fill parent[0], depth and dist
        vector<int> stack = {0};
        parent[0][0] = 0;
        while (!stack.empty()) {
            int v = stack.back();
            stack.pop_back();
            for (auto &pr : adj[v]) {
                int to = pr.first, w = pr.second;
                if (to == parent[0][v]) continue;
                parent[0][to] = v;
                depth[to] = depth[v] + 1;
                dist[to] = dist[v] + w;
                stack.push_back(to);
            }
        }
        // binary lifting table
        for (int k = 1; k < LOG; ++k) {
            for (int v = 0; v < n; ++v) {
                parent[k][v] = parent[k-1][parent[k-1][v]];
            }
        }
        auto lca = [&](int a, int b) -> int {
            if (depth[a] < depth[b]) swap(a, b);
            int diff = depth[a] - depth[b];
            for (int k = LOG - 1; k >= 0; --k) {
                if (diff & (1 << k)) a = parent[k][a];
            }
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; --k) {
                if (parent[k][a] != parent[k][b]) {
                    a = parent[k][a];
                    b = parent[k][b];
                }
            }
            return parent[0][a];
        };
        auto distBetween = [&](int u, int v) -> long long {
            int w = lca(u, v);
            return dist[u] + dist[v] - 2 * dist[w];
        };
        
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &q : queries) {
            int a = q[0], b = q[1], c = q[2];
            long long dab = distBetween(a, b);
            long long dbc = distBetween(b, c);
            long long dca = distBetween(c, a);
            long long total = (dab + dbc + dca) / 2;
            ans.push_back((int)total);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private int LOG;
    private int[][] up;
    private int[] depth;
    private long[] dist;

    private int lca(int a, int b) {
        if (depth[a] < depth[b]) {
            int tmp = a; a = b; b = tmp;
        }
        int diff = depth[a] - depth[b];
        for (int k = 0; diff > 0; k++) {
            if ((diff & 1) == 1) {
                a = up[k][a];
            }
            diff >>= 1;
        }
        if (a == b) return a;
        for (int k = LOG - 1; k >= 0; k--) {
            if (up[k][a] != up[k][b]) {
                a = up[k][a];
                b = up[k][b];
            }
        }
        return up[0][a];
    }

    private long distance(int u, int v) {
        int l = lca(u, v);
        return dist[u] + dist[v] - 2L * dist[l];
    }

    public int[] minimumWeight(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        up = new int[LOG][n];
        depth = new int[n];
        dist = new long[n];

        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        up[0][0] = 0;
        depth[0] = 0;
        dist[0] = 0L;

        while (!stack.isEmpty()) {
            int u = stack.pop();
            for (int[] e : adj[u]) {
                int v = e[0];
                int w = e[1];
                if (v == up[0][u]) continue;
                up[0][v] = u;
                depth[v] = depth[u] + 1;
                dist[v] = dist[u] + w;
                stack.push(v);
            }
        }

        for (int k = 1; k < LOG; k++) {
            for (int v = 0; v < n; v++) {
                up[k][v] = up[k - 1][up[k - 1][v]];
            }
        }

        int qlen = queries.length;
        int[] ans = new int[qlen];
        for (int i = 0; i < qlen; i++) {
            int src1 = queries[i][0];
            int src2 = queries[i][1];
            int dest = queries[i][2];
            long d12 = distance(src1, src2);
            long d23 = distance(src2, dest);
            long d31 = distance(dest, src1);
            ans[i] = (int) ((d12 + d23 + d31) / 2L);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumWeight(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = 0
        while (1 << LOG) <= n:
            LOG += 1

        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n

        stack = [(0, -1, 0)]  # node, parent, weight from parent
        while stack:
            node, par, w = stack.pop()
            parent[0][node] = par
            if par != -1:
                depth[node] = depth[par] + 1
                dist[node] = dist[par] + w
            for nb, wt in adj[node]:
                if nb == par:
                    continue
                stack.append((nb, node, wt))

        for k in range(1, LOG):
            prev = parent[k - 1]
            cur = parent[k]
            for v in range(n):
                anc = prev[v]
                cur[v] = -1 if anc == -1 else prev[anc]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                pu = parent[k][u]
                pv = parent[k][v]
                if pu != -1 and pu != pv:
                    u = pu
                    v = pv
            return parent[0][u]

        res = []
        for a, b, c in queries:
            dab = dist[a] + dist[b] - 2 * dist[lca(a, b)]
            dac = dist[a] + dist[c] - 2 * dist[lca(a, c)]
            dbc = dist[b] + dist[c] - 2 * dist[lca(b, c)]
            res.append((dab + dac + dbc) // 2)
        return res
```

## Python3

```python
class Solution:
    def minimumWeight(self, edges, queries):
        import sys
        sys.setrecursionlimit(1 << 25)
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        LOG = 1
        while (1 << LOG) <= n:
            LOG += 1

        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n
        stack = [0]
        visited = [False] * n
        visited[0] = True
        parent[0][0] = 0

        while stack:
            u = stack.pop()
            for v, w in g[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    parent[0][v] = u
                    stack.append(v)

        for k in range(1, LOG):
            pk = parent[k - 1]
            ppk = parent[k]
            for v in range(n):
                ppk[v] = pk[pk[v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        ans = []
        for a, b, c in queries:
            dab = dist[a] + dist[b] - 2 * dist[lca(a, b)]
            dbc = dist[b] + dist[c] - 2 * dist[lca(b, c)]
            dca = dist[c] + dist[a] - 2 * dist[lca(c, a)]
            ans.append((dab + dbc + dca) // 2)
        return ans
```

## C

```c
#include <stdlib.h>

static int N;
static int LOGV;
static int *head;
static int *toArr;
static int *wArr;
static int *nextArr;
static int edgeCnt;

static int *depthArr;
static long long *distArr;
static int *upArr; // size N * LOGV

static void addEdge(int u, int v, int w) {
    toArr[edgeCnt] = v;
    wArr[edgeCnt] = w;
    nextArr[edgeCnt] = head[u];
    head[u] = edgeCnt++;
}

static int lca(int u, int v) {
    if (depthArr[u] < depthArr[v]) {
        int tmp = u; u = v; v = tmp;
    }
    int diff = depthArr[u] - depthArr[v];
    for (int k = 0; diff; ++k) {
        if (diff & 1) u = upArr[u * LOGV + k];
        diff >>= 1;
    }
    if (u == v) return u;
    for (int k = LOGV - 1; k >= 0; --k) {
        int pu = upArr[u * LOGV + k];
        int pv = upArr[v * LOGV + k];
        if (pu != pv) {
            u = pu;
            v = pv;
        }
    }
    return upArr[u * LOGV]; // parent
}

static long long dist(int a, int b) {
    int c = lca(a, b);
    return distArr[a] + distArr[b] - 2LL * distArr[c];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minimumWeight(int** edges, int edgesSize, int* edgesColSize,
                   int** queries, int queriesSize, int* queriesColSize,
                   int* returnSize) {
    N = edgesSize + 1;
    // compute LOGV
    LOGV = 1;
    while ((1 << LOGV) <= N) ++LOGV;

    head = (int*)malloc(N * sizeof(int));
    for (int i = 0; i < N; ++i) head[i] = -1;
    toArr = (int*)malloc(2 * edgesSize * sizeof(int));
    wArr = (int*)malloc(2 * edgesSize * sizeof(int));
    nextArr = (int*)malloc(2 * edgesSize * sizeof(int));
    edgeCnt = 0;

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];
        addEdge(u, v, w);
        addEdge(v, u, w);
    }

    depthArr = (int*)malloc(N * sizeof(int));
    distArr = (long long*)malloc(N * sizeof(long long));
    upArr = (int*)malloc(N * LOGV * sizeof(int));

    // BFS from node 0
    int *queue = (int*)malloc(N * sizeof(int));
    int front = 0, back = 0;
    queue[back++] = 0;
    depthArr[0] = 0;
    distArr[0] = 0LL;
    upArr[0 * LOGV + 0] = 0;

    while (front < back) {
        int u = queue[front++];
        for (int e = head[u]; e != -1; e = nextArr[e]) {
            int v = toArr[e];
            if (v == upArr[u * LOGV + 0] && u != 0) continue;
            depthArr[v] = depthArr[u] + 1;
            distArr[v] = distArr[u] + wArr[e];
            upArr[v * LOGV + 0] = u;
            queue[back++] = v;
        }
    }

    // binary lifting table
    for (int k = 1; k < LOGV; ++k) {
        for (int i = 0; i < N; ++i) {
            int mid = upArr[i * LOGV + (k - 1)];
            upArr[i * LOGV + k] = upArr[mid * LOGV + (k - 1)];
        }
    }

    int *ans = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int a = queries[i][0];
        int b = queries[i][1];
        int c = queries[i][2];
        long long total = dist(a, b) + dist(b, c) + dist(c, a);
        ans[i] = (int)(total / 2);
    }

    *returnSize = queriesSize;

    // free temporary allocations (optional)
    free(head);
    free(toArr);
    free(wArr);
    free(nextArr);
    free(depthArr);
    free(distArr);
    free(upArr);
    free(queue);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] MinimumWeight(int[][] edges, int[][] queries) {
        int n = edges.Length + 1;
        var graph = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].Add((v, w));
            graph[v].Add((u, w));
        }

        // compute LOG
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;

        int[] depth = new int[n];
        long[] distRoot = new long[n];
        int[][] up = new int[LOG][];
        for (int k = 0; k < LOG; k++) up[k] = new int[n];

        // BFS/DFS to fill parent, depth, distRoot
        var stack = new Stack<int>();
        stack.Push(0);
        up[0][0] = -1;
        depth[0] = 0;
        distRoot[0] = 0;

        while (stack.Count > 0) {
            int u = stack.Pop();
            foreach (var (v, w) in graph[u]) {
                if (v == up[0][u]) continue; // parent
                up[0][v] = u;
                depth[v] = depth[u] + 1;
                distRoot[v] = distRoot[u] + w;
                stack.Push(v);
            }
        }

        // binary lifting table
        for (int k = 1; k < LOG; k++) {
            for (int v = 0; v < n; v++) {
                int mid = up[k - 1][v];
                up[k][v] = mid == -1 ? -1 : up[k - 1][mid];
            }
        }

        // LCA function
        int Lca(int a, int b) {
            if (depth[a] < depth[b]) { int tmp = a; a = b; b = tmp; }
            int diff = depth[a] - depth[b];
            for (int k = 0; diff > 0; k++) {
                if ((diff & 1) == 1) a = up[k][a];
                diff >>= 1;
            }
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; k--) {
                if (up[k][a] != -1 && up[k][a] != up[k][b]) {
                    a = up[k][a];
                    b = up[k][b];
                }
            }
            return up[0][a];
        }

        long Dist(int x, int y) {
            int l = Lca(x, y);
            return distRoot[x] + distRoot[y] - 2L * distRoot[l];
        }

        int qlen = queries.Length;
        int[] answer = new int[qlen];
        for (int i = 0; i < qlen; i++) {
            int src1 = queries[i][0];
            int src2 = queries[i][1];
            int dest = queries[i][2];
            long d1 = Dist(src1, src2);
            long d2 = Dist(src2, dest);
            long d3 = Dist(dest, src1);
            long total = (d1 + d2 + d3) / 2;
            answer[i] = (int)total;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[][]} queries
 * @return {number[]}
 */
var minimumWeight = function(edges, queries) {
    const n = edges.length + 1;
    const adj = Array.from({length: n}, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }
    const LOG = Math.ceil(Math.log2(n)) + 1;
    const up = Array.from({length: LOG}, () => new Int32Array(n).fill(-1));
    const depth = new Int32Array(n);
    const dist = new Float64Array(n);
    
    // iterative DFS to fill parent[0], depth, dist
    const stack = [[0, -1]];
    while (stack.length) {
        const [node, parent] = stack.pop();
        up[0][node] = parent;
        for (const [to, w] of adj[node]) {
            if (to === parent) continue;
            depth[to] = depth[node] + 1;
            dist[to] = dist[node] + w;
            stack.push([to, node]);
        }
    }
    
    // binary lifting table
    for (let k = 1; k < LOG; ++k) {
        const prev = up[k - 1];
        const cur = up[k];
        for (let i = 0; i < n; ++i) {
            const p = prev[i];
            cur[i] = p === -1 ? -1 : prev[p];
        }
    }
    
    function lca(u, v) {
        if (depth[u] < depth[v]) { let tmp = u; u = v; v = tmp; }
        // lift u up to depth of v
        let diff = depth[u] - depth[v];
        for (let k = 0; diff > 0; ++k) {
            if (diff & 1) u = up[k][u];
            diff >>= 1;
        }
        if (u === v) return u;
        for (let k = LOG - 1; k >= 0; --k) {
            if (up[k][u] !== up[k][v]) {
                u = up[k][u];
                v = up[k][v];
            }
        }
        return up[0][u];
    }
    
    function distance(u, v) {
        const w = lca(u, v);
        return dist[u] + dist[v] - 2 * dist[w];
    }
    
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [a, b, c] = queries[i];
        const dAB = distance(a, b);
        const dAC = distance(a, c);
        const dBC = distance(b, c);
        ans[i] = (dAB + dAC + dBC) / 2;
    }
    return ans;
};
```

## Typescript

```typescript
function minimumWeight(edges: number[][], queries: number[][]): number[] {
    const n = edges.length + 1;
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    const LOG = Math.ceil(Math.log2(n)) + 1;
    const up: number[][] = Array.from({ length: LOG }, () => Array(n).fill(-1));
    const depth = new Int32Array(n);
    const dist = new Float64Array(n);
    const parent = new Int32Array(n);
    parent[0] = -1;

    // iterative DFS/BFS to set depth, dist and up[0]
    const stack: number[] = [0];
    while (stack.length) {
        const u = stack.pop()!;
        for (const [v, w] of adj[u]) {
            if (v === parent[u]) continue;
            parent[v] = u;
            depth[v] = depth[u] + 1;
            dist[v] = dist[u] + w;
            up[0][v] = u;
            stack.push(v);
        }
    }

    // binary lifting table
    for (let k = 1; k < LOG; ++k) {
        const prev = up[k - 1];
        const cur = up[k];
        for (let v = 0; v < n; ++v) {
            const mid = prev[v];
            cur[v] = mid === -1 ? -1 : prev[mid];
        }
    }

    function lca(a: number, b: number): number {
        if (depth[a] < depth[b]) [a, b] = [b, a];
        let diff = depth[a] - depth[b];
        for (let k = 0; diff > 0; ++k) {
            if (diff & 1) a = up[k][a];
            diff >>= 1;
        }
        if (a === b) return a;
        for (let k = LOG - 1; k >= 0; --k) {
            if (up[k][a] !== up[k][b]) {
                a = up[k][a];
                b = up[k][b];
            }
        }
        return up[0][a];
    }

    function distance(u: number, v: number): number {
        const anc = lca(u, v);
        return dist[u] + dist[v] - 2 * dist[anc];
    }

    const ans: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [src1, src2, dest] = queries[i];
        const d12 = distance(src1, src2);
        const d23 = distance(src2, dest);
        const d31 = distance(dest, src1);
        ans[i] = (d12 + d23 + d31) / 2;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $edges
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function minimumWeight($edges, $queries) {
        $n = count($edges) + 1;
        // build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            $adj[$u][] = [$v, $w];
            $adj[$v][] = [$u, $w];
        }

        // binary lifting parameters
        $maxLog = 0;
        while ((1 << $maxLog) <= $n) {
            $maxLog++;
        }

        $up    = array_fill(0, $maxLog, array_fill(0, $n, 0));
        $depth = array_fill(0, $n, 0);
        $dist  = array_fill(0, $n, 0);

        // iterative DFS to fill depth, dist and up[0]
        $stack = [[0, -1, 0]]; // node, parent, weightFromParent
        while (!empty($stack)) {
            $item = array_pop($stack);
            [$node, $parent, $w] = $item;
            if ($parent != -1) {
                $depth[$node] = $depth[$parent] + 1;
                $dist[$node]  = $dist[$parent] + $w;
            }
            $up[0][$node] = ($parent == -1) ? $node : $parent;

            foreach ($adj[$node] as $edge) {
                [$nei, $wt] = $edge;
                if ($nei == $parent) continue;
                $stack[] = [$nei, $node, $wt];
            }
        }

        // build binary lifting table
        for ($k = 1; $k < $maxLog; $k++) {
            for ($v = 0; $v < $n; $v++) {
                $mid = $up[$k - 1][$v];
                $up[$k][$v] = $up[$k - 1][$mid];
            }
        }

        // helper functions as closures to capture by reference
        $lca = function (int $u, int $v) use (&$depth, &$up, $maxLog): int {
            if ($depth[$u] < $depth[$v]) {
                $tmp = $u; $u = $v; $v = $tmp;
            }
            $diff = $depth[$u] - $depth[$v];
            $k = 0;
            while ($diff) {
                if ($diff & 1) $u = $up[$k][$u];
                $diff >>= 1;
                $k++;
            }
            if ($u == $v) return $u;
            for ($k = $maxLog - 1; $k >= 0; $k--) {
                if ($up[$k][$u] != $up[$k][$v]) {
                    $u = $up[$k][$u];
                    $v = $up[$k][$v];
                }
            }
            return $up[0][$u];
        };

        $distance = function (int $a, int $b) use (&$dist, &$depth, $lca): int {
            $anc = $lca($a, $b);
            return $dist[$a] + $dist[$b] - 2 * $dist[$anc];
        };

        $ans = [];
        foreach ($queries as $q) {
            [$src1, $src2, $dest] = $q;
            $d12 = $distance($src1, $src2);
            $d23 = $distance($src2, $dest);
            $d31 = $distance($dest, $src1);
            $total = intdiv($d12 + $d23 + $d31, 2);
            $ans[] = $total;
        }
        return $ans;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func minimumWeight(_ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        let n = edges.count + 1
        var adj = Array(repeating: [(to: Int, w: Int)](), count: n)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            adj[u].append((v, w))
            adj[v].append((u, w))
        }
        
        var LOG = 0
        while (1 << LOG) <= n { LOG += 1 }
        var parent = Array(repeating: Array(repeating: -1, count: n), count: LOG)
        var depth = [Int](repeating: 0, count: n)
        var distRoot = [Int64](repeating: 0, count: n)
        
        // iterative DFS to fill depth, distRoot and parent[0]
        var stack: [(Int, Int)] = [(0, -1)]
        while let (u, p) = stack.popLast() {
            parent[0][u] = p
            for edge in adj[u] where edge.to != p {
                depth[edge.to] = depth[u] + 1
                distRoot[edge.to] = distRoot[u] + Int64(edge.w)
                stack.append((edge.to, u))
            }
        }
        
        // binary lifting table
        if LOG > 1 {
            for k in 1..<LOG {
                for v in 0..<n {
                    let mid = parent[k - 1][v]
                    if mid != -1 {
                        parent[k][v] = parent[k - 1][mid]
                    }
                }
            }
        }
        
        func lca(_ a: Int, _ b: Int) -> Int {
            var u = a, v = b
            if depth[u] < depth[v] { swap(&u, &v) }
            var diff = depth[u] - depth[v]
            var k = 0
            while diff > 0 {
                if (diff & 1) == 1 {
                    u = parent[k][u]
                }
                diff >>= 1
                k += 1
            }
            if u == v { return u }
            for i in stride(from: LOG - 1, through: 0, by: -1) {
                let pu = parent[i][u]
                let pv = parent[i][v]
                if pu != -1 && pu != pv {
                    u = pu
                    v = pv
                }
            }
            return parent[0][u]
        }
        
        func distance(_ x: Int, _ y: Int) -> Int64 {
            let w = lca(x, y)
            return distRoot[x] + distRoot[y] - 2 * distRoot[w]
        }
        
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let a = q[0], b = q[1], c = q[2]
            let dAB = distance(a, b)
            let dAC = distance(a, c)
            let dBC = distance(b, c)
            let ans = (dAB + dAC + dBC) / 2
            result.append(Int(ans))
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumWeight(edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val n = edges.size + 1
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        var maxLog = 1
        while ((1 shl maxLog) <= n) maxLog++
        val up = Array(maxLog) { IntArray(n) }
        val depth = IntArray(n)
        val dist = LongArray(n)

        val deque: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        deque.add(0)
        val visited = BooleanArray(n)
        visited[0] = true
        up[0][0] = 0

        while (deque.isNotEmpty()) {
            val u = deque.removeFirst()
            for ((v, w) in adj[u]) {
                if (!visited[v]) {
                    visited[v] = true
                    depth[v] = depth[u] + 1
                    up[0][v] = u
                    dist[v] = dist[u] + w.toLong()
                    deque.add(v)
                }
            }
        }

        for (k in 1 until maxLog) {
            for (i in 0 until n) {
                up[k][i] = up[k - 1][up[k - 1][i]]
            }
        }

        fun lca(a: Int, b: Int): Int {
            var u = a
            var v = b
            if (depth[u] < depth[v]) {
                val tmp = u; u = v; v = tmp
            }
            var diff = depth[u] - depth[v]
            var i = 0
            while (diff > 0) {
                if ((diff and 1) == 1) {
                    u = up[i][u]
                }
                diff = diff shr 1
                i++
            }
            if (u == v) return u
            for (k in maxLog - 1 downTo 0) {
                if (up[k][u] != up[k][v]) {
                    u = up[k][u]
                    v = up[k][v]
                }
            }
            return up[0][u]
        }

        fun distance(u: Int, v: Int): Long {
            val w = lca(u, v)
            return dist[u] + dist[v] - 2L * dist[w]
        }

        val ans = IntArray(queries.size)
        for (idx in queries.indices) {
            val a = queries[idx][0]
            val b = queries[idx][1]
            val c = queries[idx][2]
            val sum = distance(a, b) + distance(b, c) + distance(c, a)
            ans[idx] = (sum / 2).toInt()
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> minimumWeight(List<List<int>> edges, List<List<int>> queries) {
    int n = edges.length + 1;
    // adjacency list
    List<List<_Edge>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1], w = e[2];
      adj[u].add(_Edge(v, w));
      adj[v].add(_Edge(u, w));
    }

    // compute LOG
    int LOG = 1;
    while ((1 << LOG) <= n) LOG++;

    List<int> depth = List.filled(n, 0);
    List<int> parent = List.filled(n, -1);
    List<int> distRoot = List.filled(n, 0);
    // binary lifting table
    List<List<int>> up = List.generate(LOG, (_) => List.filled(n, -1));

    // iterative DFS/BFS from node 0 as root
    List<int> stack = [0];
    parent[0] = -1;
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      for (var e in adj[node]) {
        if (e.to == parent[node]) continue;
        parent[e.to] = node;
        depth[e.to] = depth[node] + 1;
        distRoot[e.to] = distRoot[node] + e.w;
        stack.add(e.to);
      }
    }

    // fill up table
    for (int i = 0; i < n; i++) {
      up[0][i] = parent[i];
    }
    for (int k = 1; k < LOG; k++) {
      for (int i = 0; i < n; i++) {
        int mid = up[k - 1][i];
        up[k][i] = (mid == -1) ? -1 : up[k - 1][mid];
      }
    }

    int lca(int u, int v) {
      if (depth[u] < depth[v]) {
        int tmp = u;
        u = v;
        v = tmp;
      }
      int diff = depth[u] - depth[v];
      int bit = 0;
      while (diff > 0) {
        if ((diff & 1) == 1) {
          u = up[bit][u];
        }
        diff >>= 1;
        bit++;
      }
      if (u == v) return u;
      for (int k = LOG - 1; k >= 0; k--) {
        int pu = up[k][u];
        int pv = up[k][v];
        if (pu != -1 && pu != pv) {
          u = pu;
          v = pv;
        }
      }
      return parent[u];
    }

    int distance(int a, int b) {
      int anc = lca(a, b);
      return distRoot[a] + distRoot[b] - 2 * distRoot[anc];
    }

    List<int> ans = List.filled(queries.length, 0);
    for (int i = 0; i < queries.length; i++) {
      int a = queries[i][0];
      int b = queries[i][1];
      int c = queries[i][2];
      int dAB = distance(a, b);
      int dBC = distance(b, c);
      int dCA = distance(c, a);
      ans[i] = ((dAB + dBC + dCA) ~/ 2);
    }
    return ans;
  }
}

class _Edge {
  final int to;
  final int w;
  _Edge(this.to, this.w);
}
```

## Golang

```go
func minimumWeight(edges [][]int, queries [][]int) []int {
    n := len(edges) + 1
    type edge struct{ to, w int }
    adj := make([][]edge, n)
    for _, e := range edges {
        u, v, w := e[0], e[1], e[2]
        adj[u] = append(adj[u], edge{v, w})
        adj[v] = append(adj[v], edge{u, w})
    }

    LOG := 0
    for (1 << LOG) <= n {
        LOG++
    }
    parent := make([][]int, LOG)
    for i := 0; i < LOG; i++ {
        parent[i] = make([]int, n)
        for j := 0; j < n; j++ {
            parent[i][j] = -1
        }
    }
    depth := make([]int, n)
    distRoot := make([]int64, n)

    // DFS to fill parent[0], depth, distRoot
    stack := []int{0}
    visited := make([]bool, n)
    visited[0] = true
    for len(stack) > 0 {
        v := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        for _, e := range adj[v] {
            if !visited[e.to] {
                visited[e.to] = true
                parent[0][e.to] = v
                depth[e.to] = depth[v] + 1
                distRoot[e.to] = distRoot[v] + int64(e.w)
                stack = append(stack, e.to)
            }
        }
    }

    for k := 1; k < LOG; k++ {
        for v := 0; v < n; v++ {
            if parent[k-1][v] != -1 {
                parent[k][v] = parent[k-1][parent[k-1][v]]
            }
        }
    }

    lca := func(u, v int) int {
        if depth[u] < depth[v] {
            u, v = v, u
        }
        diff := depth[u] - depth[v]
        for k := 0; k < LOG; k++ {
            if (diff>>k)&1 == 1 {
                u = parent[k][u]
            }
        }
        if u == v {
            return u
        }
        for k := LOG - 1; k >= 0; k-- {
            if parent[k][u] != -1 && parent[k][u] != parent[k][v] {
                u = parent[k][u]
                v = parent[k][v]
            }
        }
        return parent[0][u]
    }

    dist := func(u, v int) int64 {
        w := lca(u, v)
        return distRoot[u] + distRoot[v] - 2*distRoot[w]
    }

    ans := make([]int, len(queries))
    for i, q := range queries {
        a, b, c := q[0], q[1], q[2]
        total := dist(a, b) + dist(a, c) + dist(b, c)
        ans[i] = int(total / 2)
    }
    return ans
}
```

## Ruby

```ruby
def minimum_weight(edges, queries)
  n = edges.size + 1
  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  log = Math.log2(n).to_i + 1
  parent = Array.new(log) { Array.new(n, -1) }
  depth = Array.new(n, 0)
  dist = Array.new(n, 0)

  stack = [[0, -1]]
  while (node, par = stack.pop)
    parent[0][node] = par
    adj[node].each do |nei, w|
      next if nei == par
      depth[nei] = depth[node] + 1
      dist[nei] = dist[node] + w
      stack << [nei, node]
    end
  end

  (1...log).each do |k|
    (0...n).each do |v|
      p = parent[k - 1][v]
      parent[k][v] = p == -1 ? -1 : parent[k - 1][p]
    end
  end

  lca = lambda do |u, v|
    if depth[u] < depth[v]
      u, v = v, u
    end
    diff = depth[u] - depth[v]
    bit = 0
    while diff > 0
      if (diff & 1) == 1
        u = parent[bit][u]
      end
      diff >>= 1
      bit += 1
    end
    return u if u == v
    (log - 1).downto(0) do |k|
      pu = parent[k][u]
      pv = parent[k][v]
      if pu != -1 && pu != pv
        u = pu
        v = pv
      end
    end
    parent[0][u]
  end

  distance = lambda do |a, b|
    l = lca.call(a, b)
    dist[a] + dist[b] - 2 * dist[l]
  end

  result = []
  queries.each do |s1, s2, d|
    d12 = distance.call(s1, s2)
    d1d = distance.call(s1, d)
    d2d = distance.call(s2, d)
    result << (d12 + d1d + d2d) / 2
  end
  result
end
```

## Scala

```scala
object Solution {
  def minimumWeight(edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer[(Int, Int)]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val w = e(2)
      adj(u).append((v, w))
      adj(v).append((u, w))
    }

    var maxLog = 0
    while ((1 << maxLog) <= n) maxLog += 1

    val parent = Array.ofDim[Int](maxLog, n)
    val depth = new Array[Int](n)
    val dist = new Array[Long](n)

    // BFS/DFS to set depth, parent[0], and distance from root
    val visited = new Array[Boolean](n)
    val stack = new java.util.ArrayDeque[Int]()
    visited(0) = true
    stack.push(0)
    while (!stack.isEmpty) {
      val u = stack.pop()
      for ((v, w) <- adj(u)) {
        if (!visited(v)) {
          visited(v) = true
          parent(0)(v) = u
          depth(v) = depth(u) + 1
          dist(v) = dist(u) + w
          stack.push(v)
        }
      }
    }

    // binary lifting table
    for (k <- 1 until maxLog) {
      var v = 0
      while (v < n) {
        val mid = parent(k - 1)(v)
        parent(k)(v) = parent(k - 1)(mid)
        v += 1
      }
    }

    def lca(u0: Int, v0: Int): Int = {
      var u = u0
      var v = v0
      if (depth(u) < depth(v)) { val tmp = u; u = v; v = tmp }
      var diff = depth(u) - depth(v)
      var i = 0
      while (diff > 0) {
        if ((diff & 1) == 1) u = parent(i)(u)
        diff >>= 1
        i += 1
      }
      if (u == v) return u
      for (k <- maxLog - 1 to 0 by -1) {
        if (parent(k)(u) != parent(k)(v)) {
          u = parent(k)(u)
          v = parent(k)(v)
        }
      }
      parent(0)(u)
    }

    def distance(u: Int, v: Int): Long = {
      val w = lca(u, v)
      dist(u) + dist(v) - 2L * dist(w)
    }

    val ans = new Array[Int](queries.length)
    var idx = 0
    while (idx < queries.length) {
      val a = queries(idx)(0)
      val b = queries(idx)(1)
      val c = queries(idx)(2)
      val dAB = distance(a, b)
      val dBC = distance(b, c)
      val dCA = distance(c, a)
      ans(idx) = ((dAB + dBC + dCA) / 2L).toInt
      idx += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::cmp::max;

impl Solution {
    pub fn minimum_weight(edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len() + 1;
        // build adjacency list
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as i64;
            adj[u].push((v, w));
            adj[v].push((u, w));
        }

        // compute LOG
        let mut log = 1usize;
        while (1usize << log) <= n {
            log += 1;
        }

        // up[k][v] = 2^k ancestor of v
        let mut up: Vec<Vec<usize>> = vec![vec![0; n]; log];
        let mut depth: Vec<usize> = vec![0; n];
        let mut dist_root: Vec<i64> = vec![0; n];

        // iterative DFS from root 0
        let mut stack: Vec<(usize, usize, i64)> = Vec::new(); // node, parent, weight_from_parent
        stack.push((0, 0, 0));
        while let Some((node, parent, w)) = stack.pop() {
            up[0][node] = if node == 0 { 0 } else { parent };
            if node != 0 {
                depth[node] = depth[parent] + 1;
                dist_root[node] = dist_root[parent] + w;
            }
            for &(nei, weight) in adj[node].iter() {
                if nei != parent {
                    stack.push((nei, node, weight));
                }
            }
        }

        // binary lifting table
        for k in 1..log {
            for v in 0..n {
                let mid = up[k - 1][v];
                up[k][v] = up[k - 1][mid];
            }
        }

        // helper closure for LCA
        let lca = |mut a: usize, mut b: usize,
                   depth: &Vec<usize>,
                   up: &Vec<Vec<usize>>| -> usize {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }
            let diff = depth[a] - depth[b];
            for k in 0..up.len() {
                if (diff >> k) & 1 == 1 {
                    a = up[k][a];
                }
            }
            if a == b {
                return a;
            }
            for k_rev in (0..up.len()).rev() {
                if up[k_rev][a] != up[k_rev][b] {
                    a = up[k_rev][a];
                    b = up[k_rev][b];
                }
            }
            up[0][a]
        };

        // distance function using LCA
        let distance = |u: usize, v: usize,
                        depth: &Vec<usize>,
                        up: &Vec<Vec<usize>>,
                        dist_root: &Vec<i64>| -> i64 {
            let anc = lca(u, v, depth, up);
            dist_root[u] + dist_root[v] - 2 * dist_root[anc]
        };

        // answer queries
        let mut ans: Vec<i32> = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let a = q[0] as usize;
            let b = q[1] as usize;
            let c = q[2] as usize;
            let d_ab = distance(a, b, &depth, &up, &dist_root);
            let d_ac = distance(a, c, &depth, &up, &dist_root);
            let d_bc = distance(b, c, &depth, &up, &dist_root);
            let total = (d_ab + d_ac + d_bc) / 2;
            ans.push(total as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-weight edges queries)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ((n (+ 1 (length edges)))
         ;; adjacency list: each entry is a list of vectors #[neighbor weight]
         (adj (make-vector n '()))
         (_ (for-each
              (lambda (e)
                (let* ((u (list-ref e 0))
                       (v (list-ref e 1))
                       (w (list-ref e 2)))
                  (vector-set! adj u (cons (vector v w) (vector-ref adj u)))
                  (vector-set! adj v (cons (vector u w) (vector-ref adj v)))))
              edges))
         ;; depth, distance from root, parent[0]
         (depth (make-vector n -1))
         (dist-vec (make-vector n 0))
         (parent0 (make-vector n -1))
         ;; iterative DFS using explicit stack
         (stack (make-vector n -1))
         (top 0)
         (_ (begin
              (vector-set! depth 0 0)
              (vector-set! dist-vec 0 0)
              (vector-set! parent0 0 -1)
              (vector-set! stack top 0)
              (set! top (+ top 1))
              (let loop ()
                (when (> top 0)
                  (set! top (- top 1))
                  (let ((node (vector-ref stack top)))
                    (for-each
                     (lambda (pair)
                       (let ((nbr (vector-ref pair 0))
                             (w   (vector-ref pair 1)))
                         (when (not (= nbr (vector-ref parent0 node)))
                           (vector-set! parent0 nbr node)
                           (vector-set! depth nbr (+ 1 (vector-ref depth node)))
                           (vector-set! dist-vec nbr (+ (vector-ref dist-vec node) w))
                           (vector-set! stack top nbr)
                           (set! top (+ top 1)))))
                     (vector-ref adj node))))
                  (loop))))))
         ;; binary lifting table
         (LOG (let loop ((k 0) (pow 1))
                (if (>= pow n) k (loop (+ k 1) (* pow 2)))))
         (up (make-vector LOG)))
    ;; level 0
    (vector-set! up 0 parent0)
    ;; higher levels
    (for ([k (in-range 1 LOG)])
      (let ((prev (vector-ref up (- k 1)))
            (curr (make-vector n -1)))
        (for ([v (in-range n)])
          (let ((p (vector-ref prev v)))
            (if (= p -1)
                (vector-set! curr v -1)
                (vector-set! curr v (vector-ref prev p)))))
        (vector-set! up k curr)))
    ;; helper: lift node by diff using binary lifting
    (define (lift u diff)
      (let loop ((i 0) (node u))
        (if (= i LOG)
            node
            (let ((node'
                   (if (zero? (bitwise-and diff (arithmetic-shift 1 i)))
                       node
                       (vector-ref (vector-ref up i) node))))
              (loop (+ i 1) node')))))
    ;; LCA
    (define (lca u v)
      (let* ((du (vector-ref depth u))
             (dv (vector-ref depth v))
             (u2 (if (> du dv) (lift u (- du dv)) u))
             (v2 (if (> dv du) (lift v (- dv du)) v)))
        (if (= u2 v2)
            u2
            (let loop ((k (- LOG 1)) (a u2) (b v2))
              (if (< k 0)
                  (vector-ref parent0 a)
                  (let ((pa (vector-ref (vector-ref up k) a))
                        (pb (vector-ref (vector-ref up k) b)))
                    (if (and (not (= pa -1)) (not (= pb -1)) (not (= pa pb)))
                        (loop (- k 1) pa pb)
                        (loop (- k 1) a b))))))))
    ;; distance between two nodes
    (define (dist u v)
      (let ((l (lca u v)))
        (+ (vector-ref dist-vec u)
           (vector-ref dist-vec v)
           (* -2 (vector-ref dist-vec l)))))
    ;; answer each query
    (map (lambda (q)
           (let* ((a (list-ref q 0))
                  (b (list-ref q 1))
                  (c (list-ref q 2))
                  (d1 (dist a b))
                  (d2 (dist b c))
                  (d3 (dist c a)))
             (/ (+ d1 d2 d3) 2)))
         queries)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_weight/2]).
-spec minimum_weight(Edges :: [[integer()]], Queries :: [[integer()]]) -> [integer()].
minimum_weight(Edges, Queries) ->
    N = length(Edges) + 1,
    Adj = build_adj(Edges),
    {LevelArr, DistArr, Parent0} = bfs(N, Adj),
    MaxLog = ceil_log2(N),
    Parents = build_parents(MaxLog, N, Parent0),
    lists:map(
      fun([A,B,C]) ->
          DAB = distance(A, B, LevelArr, DistArr, Parents, MaxLog),
          DBC = distance(B, C, LevelArr, DistArr, Parents, MaxLog),
          DCA = distance(C, A, LevelArr, DistArr, Parents, MaxLog),
          (DAB + DBC + DCA) div 2
      end,
      Queries).

%% Build adjacency map: node -> [{Neighbor,Weight}]
build_adj(Edges) ->
    lists:foldl(
      fun([U,V,W], Acc) ->
              Acc1 = maps:update_with(U,
                       fun(L) -> [{V,W}|L] end,
                       [{V,W}], Acc),
              maps:update_with(V,
                       fun(L) -> [{U,W}|L] end,
                       [{U,W}], Acc1)
      end, #{}, Edges).

%% BFS/DFS to compute level, distance from root and immediate parent
bfs(N, Adj) ->
    Level0 = array:new(N, {default,0}),
    Dist0  = array:new(N, {default,0}),
    Parent0= array:new(N, {default,-1}),
    Stack0 = [{0,-1,0}],
    bfs_loop(Stack0, Adj, Level0, Dist0, Parent0).

bfs_loop([], _Adj, Level, Dist, Parent) ->
    {Level, Dist, Parent};
bfs_loop([{Node,Par,DistSoFar}|Rest], Adj, LevelAcc, DistAcc, ParentAcc) ->
    Lvl = if Par == -1 -> 0; true -> (array:get(Par, LevelAcc)) + 1 end,
    LevelAcc1 = array:set(Node, Lvl, LevelAcc),
    DistAcc1  = array:set(Node, DistSoFar, DistAcc),
    ParentAcc1= array:set(Node, Par, ParentAcc),
    Neighs = maps:get(Node, Adj, []),
    NewStack = lists:foldl(
                 fun({Nb,W}, Acc) ->
                         if Nb =/= Par -> [{Nb, Node, DistSoFar+W}|Acc];
                            true      -> Acc
                         end
                 end,
                 Rest, Neighs),
    bfs_loop(NewStack, Adj, LevelAcc1, DistAcc1, ParentAcc1).

%% Build binary lifting tables
build_parents(MaxLog, N, Parent0) ->
    build_parents_loop(MaxLog-1, N, [Parent0]).

build_parents_loop(0, _N, Acc) -> lists:reverse(Acc);
build_parents_loop(K, N, [Prev|Rest]=Acc) ->
    New = build_one_level(N, Prev),
    build_parents_loop(K-1, N, [New | Acc]).

build_one_level(N, PrevArr) ->
    Indices = lists:seq(0, N-1),
    lists:foldl(
      fun(I, Arr) ->
              P = array:get(I, PrevArr),
              PP = if P == -1 -> -1; true -> array:get(P, PrevArr) end,
              array:set(I, PP, Arr)
      end,
      array:new(N, {default,-1}),
      Indices).

%% Compute ceil(log2(N))
ceil_log2(N) ->
    ceil_log2(N, 0).
ceil_log2(N, K) when (1 bsl K) >= N -> K + 1;
ceil_log2(N, K) -> ceil_log2(N, K + 1).

%% Distance between two nodes using LCA
distance(X, Y, LevelArr, DistArr, Parents, MaxLog) ->
    L = lca(X, Y, LevelArr, Parents, MaxLog),
    DX = array:get(X, DistArr),
    DY = array:get(Y, DistArr),
    DL = array:get(L, DistArr),
    DX + DY - 2 * DL.

lca(A, B, LevelArr, Parents, MaxLog) ->
    LA = array:get(A, LevelArr),
    LB = array:get(B, LevelArr),
    {U,V} = if LA < LB -> {B,A}; true -> {A,B} end,
    Diff = abs(LA - LB),
    U1 = lift_node(U, Diff, Parents),
    V1 = V,
    if U1 == V1 ->
            U1;
       true ->
            lca_up(U1, V1, MaxLog-1, Parents)
    end.

lift_node(Node, 0, _Parents) -> Node;
lift_node(Node, Diff, Parents) ->
    lift_node_bits(Node, Diff, 0, Parents).

lift_node_bits(Node, Diff, K, Parents) when Diff =:= 0 -> Node;
lift_node_bits(Node, Diff, K, Parents) ->
    if (Diff band (1 bsl K)) =/= 0 ->
            ParentArr = lists:nth(K+1, Parents),
            NewNode = array:get(Node, ParentArr),
            lift_node_bits(NewNode, Diff band bnot(1 bsl K), K+1, Parents);
       true ->
            lift_node_bits(Node, Diff, K+1, Parents)
    end.

lca_up(A, B, -1, Parents) ->
    ParentArr = lists:nth(1, Parents),
    array:get(A, ParentArr);
lca_up(A, B, K, Parents) ->
    PA = array:get(A, lists:nth(K+1, Parents)),
    PB = array:get(B, lists:nth(K+1, Parents)),
    if PA =/= -1 andalso PA =/= PB ->
            lca_up(PA, PB, K-1, Parents);
       true ->
            lca_up(A, B, K-1, Parents)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec minimum_weight(edges :: [[integer]], queries :: [[integer]]) :: [integer]
  def minimum_weight(edges, queries) do
    n = length(edges) + 1

    # adjacency list
    adj =
      Enum.reduce(edges, %{}, fn [u, v, w], acc ->
        acc
        |> Map.update(u, [{v, w}], fn lst -> [{v, w} | lst] end)
        |> Map.update(v, [{u, w}], fn lst -> [{u, w} | lst] end)
      end)

    # bfs to get depth, distance from root and immediate parent
    {depth, dist, parent} = bfs(adj, n)

    # compute LOG such that 2^LOG >= n
    log =
      (fn f ->
         Enum.reduce_while(0..30, 0, fn i, _acc ->
           if (1 <<< i) >= n, do: {:halt, i}, else: {:cont, i + 1}
         end)
       end).()

    anc_maps = build_ancestors(parent, n, log)

    Enum.map(queries, fn [a, b, c] ->
      dab = distance(a, b, depth, dist, parent, anc_maps, log)
      dbc = distance(b, c, depth, dist, parent, anc_maps, log)
      dca = distance(c, a, depth, dist, parent, anc_maps, log)

      (dab + dbc + dca) >>> 1
    end)
  end

  # BFS using Erlang queue
  defp bfs(adj, n) do
    import :queue
    q0 = from_list([0])
    depth = %{0 => 0}
    dist = %{0 => 0}
    parent = %{0 => -1}
    bfs_loop(q0, adj, depth, dist, parent)
  end

  defp bfs_loop(queue, adj, depth, dist, parent) do
    case :queue.out(queue) do
      {:empty, _} ->
        {depth, dist, parent}

      {{:value, node}, q2} ->
        neighbors = Map.get(adj, node, [])

        {new_depth, new_dist, new_parent, new_queue} =
          Enum.reduce(neighbors, {depth, dist, parent, q2}, fn {nbr, w},
                                                             {d_acc, di_acc,
                                                              p_acc, q_acc} ->
            if Map.has_key?(d_acc, nbr) do
              {d_acc, di_acc, p_acc, q_acc}
            else
              d_node = Map.get(d_acc, node)
              di_node = Map.get(di_acc, node)

              d_acc = Map.put(d_acc, nbr, d_node + 1)
              di_acc = Map.put(di_acc, nbr, di_node + w)
              p_acc = Map.put(p_acc, nbr, node)
              q_acc = :queue.in(nbr, q_acc)
              {d_acc, di_acc, p_acc, q_acc}
            end
          end)

        bfs_loop(new_queue, adj, new_depth, new_dist, new_parent)
    end
  end

  # Build binary lifting tables
  defp build_ancestors(parent, n, log) do
    levels = [parent]

    Enum.reduce(1..(log - 1), levels, fn _k, acc ->
      prev = List.last(acc)

      cur =
        Enum.reduce(0..(n - 1), %{}, fn i, m ->
          p = Map.get(prev, i, -1)
          anc = if p == -1, do: -1, else: Map.get(prev, p, -1)
          Map.put(m, i, anc)
        end)

      acc ++ [cur]
    end)
  end

  # LCA using binary lifting
  defp lca(a, b, depth, parent, anc_maps, log) do
    {a, b} =
      if Map.get(depth, a) < Map.get(depth, b), do: {b, a}, else: {a, b}

    diff = Map.get(depth, a) - Map.get(depth, b)
    a = lift_node(a, diff, anc_maps)

    if a == b do
      a
    else
      {a_final, _} =
        Enum.reduce((log - 1)..0, {a, b}, fn k, {x, y} ->
          ax = Map.get(Enum.at(anc_maps, k), x, -1)
          ay = Map.get(Enum.at(anc_maps, k), y, -1)

          if ax != -1 and ax != ay do
            {ax, ay}
          else
            {x, y}
          end
        end)

      Map.get(parent, a_final)
    end
  end

  defp lift_node(node, diff, anc_maps) do
    Enum.reduce(0..(length(anc_maps) - 1), node, fn k, cur ->
      if (diff &&& (1 <<< k)) != 0 do
        Map.get(Enum.at(anc_maps, k), cur, -1)
      else
        cur
      end
    end)
  end

  # distance between two nodes
  defp distance(x, y, depth, dist, parent, anc_maps, log) do
    l = lca(x, y, depth, parent, anc_maps, log)

    Map.get(dist, x) + Map.get(dist, y) - 2 * Map.get(dist, l)
  end
end
```

# 3559. Number of Ways to Assign Edge Weights II

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n + 1);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        int LOG = 1;
        while ((1 << LOG) <= n) ++LOG;
        vector<vector<int>> up(LOG, vector<int>(n + 1, 0));
        vector<int> depth(n + 1, 0);
        // BFS to set depths and first ancestors
        queue<int> q;
        q.push(1);
        depth[1] = 0;
        up[0][1] = 0;
        vector<int> visited(n + 1, 0);
        visited[1] = 1;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) if (!visited[v]) {
                visited[v] = 1;
                depth[v] = depth[u] + 1;
                up[0][v] = u;
                q.push(v);
            }
        }
        // binary lifting table
        for (int k = 1; k < LOG; ++k) {
            for (int v = 1; v <= n; ++v) {
                int mid = up[k - 1][v];
                up[k][v] = mid ? up[k - 1][mid] : 0;
            }
        }
        auto lca = [&](int a, int b) {
            if (depth[a] < depth[b]) swap(a, b);
            int diff = depth[a] - depth[b];
            for (int k = 0; diff; ++k) {
                if (diff & 1) a = up[k][a];
                diff >>= 1;
            }
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; --k) {
                if (up[k][a] != up[k][b]) {
                    a = up[k][a];
                    b = up[k][b];
                }
            }
            return up[0][a];
        };
        // precompute powers of two
        vector<int> pow2(n + 1, 1);
        for (int i = 1; i <= n; ++i) {
            pow2[i] = (long long)pow2[i - 1] * 2 % MOD;
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &qr : queries) {
            int u = qr[0], v = qr[1];
            int w = lca(u, v);
            int len = depth[u] + depth[v] - 2 * depth[w]; // number of edges on path
            if (len == 0) ans.push_back(0);
            else ans.push_back(pow2[len - 1]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] adj = new java.util.ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            adj[u].add(v);
            adj[v].add(u);
        }
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        int[][] up = new int[LOG][n + 1];
        int[] depth = new int[n + 1];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        stack.push(1);
        up[0][1] = 0;
        depth[1] = 0;
        boolean[] visited = new boolean[n + 1];
        visited[1] = true;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            for (int nb : adj[node]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    depth[nb] = depth[node] + 1;
                    up[0][nb] = node;
                    stack.push(nb);
                }
            }
        }
        for (int k = 1; k < LOG; k++) {
            for (int v = 1; v <= n; v++) {
                int mid = up[k - 1][v];
                up[k][v] = mid == 0 ? 0 : up[k - 1][mid];
            }
        }
        long[] pow2 = new long[n + 1];
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow2[i] = (pow2[i - 1] << 1) % MOD;
        }
        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            if (u == v) {
                ans[i] = 0;
                continue;
            }
            int lca = getLCA(u, v, depth, up, LOG);
            int dist = depth[u] + depth[v] - 2 * depth[lca];
            long ways = pow2[dist - 1];
            ans[i] = (int) ways;
        }
        return ans;
    }

    private int getLCA(int u, int v, int[] depth, int[][] up, int LOG) {
        if (depth[u] < depth[v]) {
            int tmp = u; u = v; v = tmp;
        }
        int diff = depth[u] - depth[v];
        for (int k = 0; diff > 0; k++) {
            if ((diff & 1) == 1) {
                u = up[k][u];
            }
            diff >>= 1;
        }
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--) {
            if (up[k][u] != up[k][v]) {
                u = up[k][u];
                v = up[k][v];
            }
        }
        return up[0][u];
    }
}
```

## Python

```python
class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = (n).bit_length()
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        # iterative DFS to fill parent[0] and depth
        stack = [(1, 0)]
        while stack:
            node, par = stack.pop()
            parent[0][node] = par
            for nb in adj[node]:
                if nb != par:
                    depth[nb] = depth[node] + 1
                    stack.append((nb, node))

        # binary lifting table
        for k in range(1, LOG):
            pk = parent[k - 1]
            ppk = parent[k]
            for v in range(1, n + 1):
                anc = pk[v]
                ppk[v] = pk[anc] if anc else 0

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # lift u up to depth of v
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

        res = []
        pow2_cache = {0: 1}
        for u, v in queries:
            if u == v:
                res.append(0)
                continue
            w = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[w]
            # compute 2^(dist-1) mod MOD
            exp = dist - 1
            ans = pow(2, exp, MOD)
            res.append(ans)
        return res
```

## Python3

```python
import sys
sys.setrecursionlimit(300000)

class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = (n).bit_length()
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        stack = [(1, 0)]
        order = []
        while stack:
            node, parent = stack.pop()
            up[0][node] = parent
            depth[node] = depth[parent] + 1 if parent else 0
            order.append(node)
            for nb in g[node]:
                if nb != parent:
                    stack.append((nb, node))

        for k in range(1, LOG):
            uk = up[k]
            ukm1 = up[k - 1]
            for v in range(1, n + 1):
                anc = ukm1[v]
                uk[v] = ukm1[anc] if anc else 0

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            bit = 0
            while diff:
                if diff & 1:
                    a = up[bit][a]
                diff >>= 1
                bit += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        res = []
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        for u, v in queries:
            w = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[w]
            if d == 0:
                res.append(0)
            else:
                # 2^(d-1) mod MOD
                res.append(pow2[d - 1])
        return res
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007

static int getLCA(int u, int v, int LOG, int *depth, int **up) {
    if (depth[u] < depth[v]) {
        int tmp = u; u = v; v = tmp;
    }
    int diff = depth[u] - depth[v];
    for (int k = 0; diff; ++k) {
        if (diff & 1) u = up[k][u];
        diff >>= 1;
    }
    if (u == v) return u;
    for (int k = LOG - 1; k >= 0; --k) {
        if (up[k][u] != up[k][v]) {
            u = up[k][u];
            v = up[k][v];
        }
    }
    return up[0][u];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* assignEdgeWeights(int** edges, int edgesSize, int* edgesColSize,
                       int** queries, int queriesSize, int* queriesColSize,
                       int* returnSize) {
    int n = edgesSize + 1;
    int *deg = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }

    int **adj = (int **)malloc((n + 1) * sizeof(int *));
    for (int i = 1; i <= n; ++i) {
        adj[i] = (int *)malloc(deg[i] * sizeof(int));
    }
    int *idx = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][idx[u]++] = v;
        adj[v][idx[v]++] = u;
    }
    free(idx);

    /* compute LOG */
    int LOG = 0;
    while ((1 << LOG) <= n) ++LOG;

    int **up = (int **)malloc(LOG * sizeof(int *));
    for (int k = 0; k < LOG; ++k) {
        up[k] = (int *)calloc(n + 1, sizeof(int));
    }
    int *depth = (int *)calloc(n + 1, sizeof(int));

    /* BFS to set parent[0] and depth */
    int *queue = (int *)malloc(n * sizeof(int));
    int head = 0, tail = 0;
    queue[tail++] = 1;
    up[0][1] = 0;
    depth[1] = 0;

    while (head < tail) {
        int u = queue[head++];
        for (int i = 0; i < deg[u]; ++i) {
            int v = adj[u][i];
            if (v == up[0][u]) continue;
            up[0][v] = u;
            depth[v] = depth[u] + 1;
            queue[tail++] = v;
        }
    }

    /* binary lifting table */
    for (int k = 1; k < LOG; ++k) {
        for (int v = 1; v <= n; ++v) {
            int mid = up[k - 1][v];
            up[k][v] = mid ? up[k - 1][mid] : 0;
        }
    }

    /* precompute powers of two */
    int *pow2 = (int *)malloc((n + 1) * sizeof(int));
    pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
        long long val = (long long)pow2[i - 1] * 2 % MOD;
        pow2[i] = (int)val;
    }

    int *ans = (int *)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int u = queries[i][0];
        int v = queries[i][1];
        if (u == v) {
            ans[i] = 0;
            continue;
        }
        int w = getLCA(u, v, LOG, depth, up);
        int dist = depth[u] + depth[v] - 2 * depth[w];
        ans[i] = pow2[dist - 1];
    }

    /* cleanup */
    for (int i = 1; i <= n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    for (int k = 0; k < LOG; ++k) free(up[k]);
    free(up);
    free(depth);
    free(queue);
    free(pow2);

    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    public int[] AssignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.Length + 1;
        var adj = new List<int>[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        // compute log
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        var up = new int[LOG, n + 1];
        var depth = new int[n + 1];

        // BFS to set depth and first ancestors
        var q = new Queue<int>();
        q.Enqueue(1);
        up[0, 1] = 0;
        depth[1] = 0;
        while (q.Count > 0) {
            int v = q.Dequeue();
            foreach (int nb in adj[v]) {
                if (nb == up[0, v]) continue;
                up[0, nb] = v;
                depth[nb] = depth[v] + 1;
                q.Enqueue(nb);
            }
        }

        // binary lifting table
        for (int k = 1; k < LOG; k++) {
            for (int v = 1; v <= n; v++) {
                int mid = up[k - 1, v];
                up[k, v] = mid == 0 ? 0 : up[k - 1, mid];
            }
        }

        // precompute powers of two
        var pow2 = new int[n + 1];
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) {
            long val = (long)pow2[i - 1] * 2 % MOD;
            pow2[i] = (int)val;
        }

        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int u = queries[i][0], v = queries[i][1];
            int lca = LCA(u, v, depth, up, LOG);
            int dist = depth[u] + depth[v] - 2 * depth[lca];
            if (dist == 0) {
                ans[i] = 0;
            } else {
                ans[i] = pow2[dist - 1];
            }
        }

        return ans;
    }

    private int LCA(int u, int v, int[] depth, int[,] up, int LOG) {
        if (depth[u] < depth[v]) {
            int tmp = u; u = v; v = tmp;
        }
        int diff = depth[u] - depth[v];
        for (int k = 0; diff > 0; k++) {
            if ((diff & 1) == 1) u = up[k, u];
            diff >>= 1;
        }
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--) {
            if (up[k, u] != up[k, v]) {
                u = up[k, u];
                v = up[k, v];
            }
        }
        return up[0, u];
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
var assignEdgeWeights = function(edges, queries) {
    const MOD = 1000000007;
    const n = edges.length + 1;

    // build adjacency list
    const adj = Array.from({length: n + 1}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // binary lifting preparation
    const LOG = Math.ceil(Math.log2(n)) + 1;
    const up = Array.from({length: LOG}, () => new Uint32Array(n + 1));
    const depth = new Int32Array(n + 1);

    // iterative DFS/BFS to set depth and first ancestors
    const stack = [1];
    up[0][1] = 0;
    depth[1] = 0;
    while (stack.length) {
        const node = stack.pop();
        for (const nb of adj[node]) {
            if (nb === up[0][node]) continue;
            up[0][nb] = node;
            depth[nb] = depth[node] + 1;
            stack.push(nb);
        }
    }

    // fill higher ancestors
    for (let k = 1; k < LOG; ++k) {
        const prev = up[k - 1];
        const cur = up[k];
        for (let v = 1; v <= n; ++v) {
            const mid = prev[v];
            cur[v] = mid ? prev[mid] : 0;
        }
    }

    // precompute powers of two
    const pow2 = new Uint32Array(n);
    pow2[0] = 1;
    for (let i = 1; i < n; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    // LCA function
    const lca = (u, v) => {
        if (depth[u] < depth[v]) [u, v] = [v, u];
        let diff = depth[u] - depth[v];
        for (let k = LOG - 1; k >= 0; --k) {
            if ((diff >> k) & 1) {
                u = up[k][u];
            }
        }
        if (u === v) return u;
        for (let k = LOG - 1; k >= 0; --k) {
            if (up[k][u] !== up[k][v]) {
                u = up[k][u];
                v = up[k][v];
            }
        }
        return up[0][u];
    };

    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        let [u, v] = queries[i];
        const w = lca(u, v);
        const dist = depth[u] + depth[v] - 2 * depth[w]; // number of edges on path
        if (dist === 0) {
            ans[i] = 0;
        } else {
            ans[i] = pow2[dist - 1];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function assignEdgeWeights(edges: number[][], queries: number[][]): number[] {
    const MOD = 1000000007;
    const n = edges.length + 1;

    // Build adjacency list
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const LOG = Math.ceil(Math.log2(n)) + 1;
    const up: number[][] = Array.from({ length: n + 1 }, () => new Array(LOG).fill(0));
    const depth = new Int32Array(n + 1);

    // BFS/DFS to fill depth and binary lifting table
    const stack: number[] = [1];
    const visited = new Uint8Array(n + 1);
    visited[1] = 1;
    up[1][0] = 1; // parent of root is itself
    for (let j = 1; j < LOG; ++j) up[1][j] = 1;

    while (stack.length) {
        const u = stack.pop()!;
        for (const v of adj[u]) {
            if (!visited[v]) {
                visited[v] = 1;
                depth[v] = depth[u] + 1;
                up[v][0] = u;
                for (let j = 1; j < LOG; ++j) {
                    up[v][j] = up[up[v][j - 1]][j - 1];
                }
                stack.push(v);
            }
        }
    }

    function lca(a: number, b: number): number {
        if (depth[a] < depth[b]) [a, b] = [b, a];
        let diff = depth[a] - depth[b];
        for (let j = 0; j < LOG; ++j) {
            if ((diff >> j) & 1) a = up[a][j];
        }
        if (a === b) return a;
        for (let j = LOG - 1; j >= 0; --j) {
            if (up[a][j] !== up[b][j]) {
                a = up[a][j];
                b = up[b][j];
            }
        }
        return up[a][0];
    }

    // Precompute powers of two modulo MOD
    const pow2 = new Int32Array(n + 1);
    pow2[0] = 1;
    for (let i = 1; i <= n; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    const answer: number[] = [];
    for (const [u, v] of queries) {
        const w = lca(u, v);
        const dist = depth[u] + depth[v] - 2 * depth[w];
        if (dist === 0) {
            answer.push(0);
        } else {
            answer.push(pow2[dist - 1]);
        }
    }

    return answer;
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
    function assignEdgeWeights($edges, $queries) {
        $MOD = 1000000007;
        $n = count($edges) + 1;

        // build adjacency list
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        // binary lifting preparation
        $LOG = 0;
        while ((1 << $LOG) <= $n) {
            $LOG++;
        }
        $up = array_fill(0, $LOG, []);
        for ($i = 0; $i < $LOG; $i++) {
            $up[$i] = array_fill(0, $n + 1, 0);
        }
        $depth = array_fill(0, $n + 1, 0);

        // iterative DFS/BFS from root=1
        $stack = [1];
        $parent = array_fill(0, $n + 1, 0);
        $parent[1] = 0;
        $depth[1] = 0;
        while ($stack) {
            $node = array_pop($stack);
            foreach ($adj[$node] as $nei) {
                if ($nei == $parent[$node]) continue;
                $parent[$nei] = $node;
                $depth[$nei] = $depth[$node] + 1;
                $up[0][$nei] = $node;
                $stack[] = $nei;
            }
        }

        // fill ancestors
        for ($k = 1; $k < $LOG; $k++) {
            for ($v = 1; $v <= $n; $v++) {
                $mid = $up[$k - 1][$v];
                $up[$k][$v] = $mid ? $up[$k - 1][$mid] : 0;
            }
        }

        // precompute powers of two
        $pow2 = array_fill(0, $n + 1, 0);
        $pow2[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $pow2[$i] = ($pow2[$i - 1] * 2) % $MOD;
        }

        // helper LCA function (closure)
        $lcaFunc = function($u, $v) use (&$depth, &$up, $LOG) {
            if ($depth[$u] < $depth[$v]) {
                $tmp = $u; $u = $v; $v = $tmp;
            }
            // lift u up
            $diff = $depth[$u] - $depth[$v];
            $k = 0;
            while ($diff) {
                if ($diff & 1) {
                    $u = $up[$k][$u];
                }
                $diff >>= 1;
                $k++;
            }
            if ($u == $v) return $u;
            for ($k = $LOG - 1; $k >= 0; $k--) {
                if ($up[$k][$u] != $up[$k][$v]) {
                    $u = $up[$k][$u];
                    $v = $up[$k][$v];
                }
            }
            return $up[0][$u];
        };

        $ans = [];
        foreach ($queries as $q) {
            $u = $q[0];
            $v = $q[1];
            $lca = $lcaFunc($u, $v);
            $dist = $depth[$u] + $depth[$v] - 2 * $depth[$lca];
            if ($dist == 0) {
                $ans[] = 0;
            } else {
                $ans[] = $pow2[$dist - 1];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func assignEdgeWeights(_ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        let n = edges.count + 1
        var adj = [[Int]](repeating: [], count: n + 1)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        var LOG = 0
        while (1 << LOG) <= n { LOG += 1 }
        var parent = Array(repeating: Array(repeating: 0, count: LOG), count: n + 1)
        var depth = Array(repeating: 0, count: n + 1)
        var stack = [Int]()
        var visited = Array(repeating: false, count: n + 1)
        stack.append(1)
        visited[1] = true
        while let node = stack.popLast() {
            for nb in adj[node] where !visited[nb] {
                visited[nb] = true
                depth[nb] = depth[node] + 1
                parent[nb][0] = node
                stack.append(nb)
            }
        }
        if LOG > 1 {
            for j in 1..<LOG {
                for v in 1...n {
                    let mid = parent[v][j - 1]
                    if mid != 0 {
                        parent[v][j] = parent[mid][j - 1]
                    }
                }
            }
        }
        func lca(_ a: Int, _ b: Int) -> Int {
            var u = a, v = b
            if depth[u] < depth[v] { swap(&u, &v) }
            let diff = depth[u] - depth[v]
            for i in 0..<LOG where ((diff >> i) & 1) == 1 {
                u = parent[u][i]
            }
            if u == v { return u }
            for k in stride(from: LOG - 1, through: 0, by: -1) {
                if parent[u][k] != parent[v][k] {
                    u = parent[u][k]
                    v = parent[v][k]
                }
            }
            return parent[u][0]
        }
        let MOD = 1_000_000_007
        var pow2 = [Int](repeating: 0, count: n + 1)
        pow2[0] = 1
        if n >= 1 {
            for i in 1...n {
                pow2[i] = Int((Int64(pow2[i - 1]) * 2) % Int64(MOD))
            }
        }
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let u = q[0], v = q[1]
            let w = lca(u, v)
            let dist = depth[u] + depth[v] - 2 * depth[w]
            if dist == 0 {
                result.append(0)
            } else {
                result.append(pow2[dist - 1])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun assignEdgeWeights(edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val n = edges.size + 1
        val adj = Array(n + 1) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        var maxLog = 1
        while ((1 shl maxLog) <= n) maxLog++
        val up = Array(maxLog) { IntArray(n + 1) }
        val depth = IntArray(n + 1)

        val stack = ArrayDeque<Int>()
        stack.add(1)
        depth[1] = 0
        up[0][1] = 1
        val visited = BooleanArray(n + 1)
        visited[1] = true

        while (stack.isNotEmpty()) {
            val u = stack.removeFirst()
            for (v in adj[u]) {
                if (!visited[v]) {
                    visited[v] = true
                    depth[v] = depth[u] + 1
                    up[0][v] = u
                    stack.add(v)
                }
            }
        }

        for (k in 1 until maxLog) {
            for (i in 1..n) {
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
            var bit = 0
            while (diff > 0) {
                if ((diff and 1) == 1) {
                    u = up[bit][u]
                }
                diff = diff shr 1
                bit++
            }
            if (u == v) return u
            for (i in maxLog - 1 downTo 0) {
                if (up[i][u] != up[i][v]) {
                    u = up[i][u]
                    v = up[i][v]
                }
            }
            return up[0][u]
        }

        val MOD = 1_000_000_007L
        val pow2 = LongArray(n + 1)
        pow2[0] = 1L
        for (i in 1..n) {
            pow2[i] = (pow2[i - 1] * 2) % MOD
        }

        val answer = IntArray(queries.size)
        for (idx in queries.indices) {
            val u = queries[idx][0]
            val v = queries[idx][1]
            if (u == v) {
                answer[idx] = 0
                continue
            }
            val w = lca(u, v)
            val dist = depth[u] + depth[v] - 2 * depth[w]
            val res = pow2[dist - 1] % MOD
            answer[idx] = res.toInt()
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;
  List<int> assignEdgeWeights(List<List<int>> edges, List<List<int>> queries) {
    int n = edges.length + 1;
    List<List<int>> g = List.generate(n + 1, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1];
      g[u].add(v);
      g[v].add(u);
    }
    int LOG = 0;
    while ((1 << LOG) <= n) LOG++;
    List<int> depth = List.filled(n + 1, 0);
    List<List<int>> up = List.generate(LOG, (_) => List.filled(n + 1, 0));
    List<int> parent = List.filled(n + 1, 0);
    List<int> stack = [1];
    parent[1] = 0;
    depth[1] = 0;
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      for (int nb in g[node]) {
        if (nb == parent[node]) continue;
        parent[nb] = node;
        depth[nb] = depth[node] + 1;
        up[0][nb] = node;
        stack.add(nb);
      }
    }
    for (int k = 1; k < LOG; k++) {
      for (int v = 1; v <= n; v++) {
        int mid = up[k - 1][v];
        up[k][v] = mid == 0 ? 0 : up[k - 1][mid];
      }
    }
    List<int> pow2 = List.filled(n + 1, 0);
    pow2[0] = 1;
    for (int i = 1; i <= n; i++) {
      pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    int lca(int a, int b) {
      if (depth[a] < depth[b]) {
        int tmp = a;
        a = b;
        b = tmp;
      }
      int diff = depth[a] - depth[b];
      for (int k = 0; k < LOG; k++) {
        if ((diff >> k) & 1 == 1) {
          a = up[k][a];
        }
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
    List<int> ans = [];
    for (var q in queries) {
      int u = q[0], v = q[1];
      int w = lca(u, v);
      int dist = depth[u] + depth[v] - 2 * depth[w];
      if (dist == 0) {
        ans.add(0);
      } else {
        ans.add(pow2[dist - 1]);
      }
    }
    return ans;
  }
}
```

## Golang

```go
func assignEdgeWeights(edges [][]int, queries [][]int) []int {
	const MOD = 1000000007

	n := len(edges) + 1
	adj := make([][]int, n+1)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	// compute LOG such that 2^LOG > n
	LOG := 0
	for (1 << LOG) <= n {
		LOG++
	}
	up := make([][]int, LOG)
	for i := 0; i < LOG; i++ {
		up[i] = make([]int, n+1)
	}
	depth := make([]int, n+1)

	// iterative DFS to fill parent and depth
	stack := []int{1}
	parent := make([]int, n+1)
	parent[1] = 1
	visited := make([]bool, n+1)
	visited[1] = true
	for len(stack) > 0 {
		u := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, v := range adj[u] {
			if !visited[v] {
				visited[v] = true
				parent[v] = u
				depth[v] = depth[u] + 1
				stack = append(stack, v)
			}
		}
	}

	// fill binary lifting table
	for i := 1; i <= n; i++ {
		up[0][i] = parent[i]
	}
	for k := 1; k < LOG; k++ {
		for i := 1; i <= n; i++ {
			up[k][i] = up[k-1][up[k-1][i]]
		}
	}

	lca := func(a, b int) int {
		if depth[a] < depth[b] {
			a, b = b, a
		}
		// lift a to depth of b
		diff := depth[a] - depth[b]
		for k := 0; diff > 0; k++ {
			if diff&1 == 1 {
				a = up[k][a]
			}
			diff >>= 1
		}
		if a == b {
			return a
		}
		for k := LOG - 1; k >= 0; k-- {
			if up[k][a] != up[k][b] {
				a = up[k][a]
				b = up[k][b]
			}
		}
		return parent[a]
	}

	// precompute powers of two
	maxDist := n - 1
	pow2 := make([]int, maxDist+1)
	pow2[0] = 1
	for i := 1; i <= maxDist; i++ {
		pow2[i] = (pow2[i-1] * 2) % MOD
	}

	ans := make([]int, len(queries))
	for i, q := range queries {
		u, v := q[0], q[1]
		if u == v {
			ans[i] = 0
			continue
		}
		w := lca(u, v)
		dist := depth[u] + depth[v] - 2*depth[w]
		ans[i] = pow2[dist-1]
	}
	return ans
}
```

## Ruby

```ruby
def assign_edge_weights(edges, queries)
  mod = 1_000_000_007
  n = edges.length + 1

  adj = Array.new(n + 1) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  log = Math.log2(n).to_i + 1
  up = Array.new(log) { Array.new(n + 1, 0) }
  depth = Array.new(n + 1, 0)

  stack = [1]
  visited = Array.new(n + 1, false)
  visited[1] = true

  while (v = stack.pop)
    adj[v].each do |to|
      next if visited[to]
      visited[to] = true
      depth[to] = depth[v] + 1
      up[0][to] = v
      (1...log).each do |k|
        anc = up[k - 1][to]
        up[k][to] = anc.zero? ? 0 : up[k - 1][anc]
      end
      stack << to
    end
  end

  pow2 = Array.new(n + 1, 1)
  (1..n).each { |i| pow2[i] = (pow2[i - 1] * 2) % mod }

  answers = []

  queries.each do |u_orig, v_orig|
    u = u_orig
    v = v_orig

    if depth[u] < depth[v]
      u, v = v, u
    end

    diff = depth[u] - depth[v]
    k = 0
    while diff > 0
      if (diff & 1) == 1
        u = up[k][u]
      end
      diff >>= 1
      k += 1
    end

    lca = nil
    if u == v
      lca = u
    else
      (log - 1).downto(0) do |i|
        if up[i][u] != 0 && up[i][u] != up[i][v]
          u = up[i][u]
          v = up[i][v]
        end
      end
      lca = up[0][u]
    end

    dist = depth[u_orig] + depth[v_orig] - 2 * depth[lca]
    answers << (dist.zero? ? 0 : pow2[dist - 1])
  end

  answers
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007

    def assignEdgeWeights(edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
        val n = edges.length + 1
        // adjacency list
        val adj = Array.ofDim[List[Int]](n + 1)
        for (i <- 0 to n) adj(i) = Nil
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u) = v :: adj(u)
            adj(v) = u :: adj(v)
        }

        // compute maxLog such that 2^maxLog > n
        var maxLog = 0
        while ((1 << maxLog) <= n) maxLog += 1

        val up = Array.ofDim[Int](maxLog, n + 1)
        val depth = new Array[Int](n + 1)

        // BFS to set depth and first ancestors
        val dq = new java.util.ArrayDeque[Int]()
        dq.add(1)
        depth(1) = 0
        up(0)(1) = 0
        while (!dq.isEmpty) {
            val u = dq.poll()
            for (v <- adj(u)) {
                if (v != up(0)(u)) {
                    depth(v) = depth(u) + 1
                    up(0)(v) = u
                    dq.add(v)
                }
            }
        }

        // binary lifting table
        for (k <- 1 until maxLog) {
            for (v <- 1 to n) {
                val mid = up(k - 1)(v)
                up(k)(v) = if (mid != 0) up(k - 1)(mid) else 0
            }
        }

        def lca(a: Int, b: Int): Int = {
            var u = a
            var v = b
            if (depth(u) < depth(v)) {
                val tmp = u; u = v; v = tmp
            }
            // lift u up to depth of v
            var diff = depth(u) - depth(v)
            var bit = 0
            while (diff > 0) {
                if ((diff & 1) == 1) u = up(bit)(u)
                diff >>= 1
                bit += 1
            }
            if (u == v) return u
            for (i <- (maxLog - 1) to 0 by -1) {
                if (up(i)(u) != up(i)(v)) {
                    u = up(i)(u)
                    v = up(i)(v)
                }
            }
            up(0)(u)
        }

        // powers of two
        val pow2 = new Array[Int](n + 1)
        pow2(0) = 1
        for (i <- 1 to n) {
            pow2(i) = ((pow2(i - 1).toLong * 2) % MOD).toInt
        }

        val ans = new Array[Int](queries.length)
        var idx = 0
        while (idx < queries.length) {
            val u = queries(idx)(0)
            val v = queries(idx)(1)
            if (u == v) {
                ans(idx) = 0
            } else {
                val w = lca(u, v)
                val dist = depth(u) + depth(v) - 2 * depth(w)
                ans(idx) = pow2(dist - 1)
            }
            idx += 1
        }
        ans
    }
}
```

## Rust

```rust
use std::cmp::max;

const MOD_I64: i64 = 1_000_000_007;

impl Solution {
    pub fn assign_edge_weights(edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        // depth and immediate parent
        let mut depth: Vec<usize> = vec![0; n + 1];
        let mut parent: Vec<usize> = vec![0; n + 1];
        let mut stack: Vec<(usize, usize)> = Vec::new();
        stack.push((1, 1));
        while let Some((node, par)) = stack.pop() {
            parent[node] = par;
            if node == par {
                depth[node] = 0;
            } else {
                depth[node] = depth[par] + 1;
            }
            for &nbr in adj[node].iter() {
                if nbr != par {
                    stack.push((nbr, node));
                }
            }
        }

        // binary lifting table
        let mut LOG: usize = 1;
        while (1usize << LOG) <= n {
            LOG += 1;
        }
        let mut up: Vec<Vec<usize>> = vec![vec![0; n + 1]; LOG];
        for v in 1..=n {
            up[0][v] = parent[v];
        }
        for k in 1..LOG {
            for v in 1..=n {
                let mid = up[k - 1][v];
                up[k][v] = up[k - 1][mid];
            }
        }

        // precompute powers of two
        let mut pow2: Vec<i64> = vec![0; n];
        pow2[0] = 1;
        for i in 1..n {
            pow2[i] = (pow2[i - 1] * 2) % MOD_I64;
        }

        // helper LCA
        let lca = |mut a: usize, mut b: usize,
                   depth: &Vec<usize>,
                   up: &Vec<Vec<usize>>,
                   LOG: usize| -> usize {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }
            let diff = depth[a] - depth[b];
            for k in 0..LOG {
                if (diff >> k) & 1 == 1 {
                    a = up[k][a];
                }
            }
            if a == b {
                return a;
            }
            for k in (0..LOG).rev() {
                if up[k][a] != up[k][b] {
                    a = up[k][a];
                    b = up[k][b];
                }
            }
            up[0][a]
        };

        let mut ans: Vec<i32> = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let u = q[0] as usize;
            let v = q[1] as usize;
            let w = lca(u, v, &depth, &up, LOG);
            let dist = depth[u] + depth[v] - 2 * depth[w];
            if dist == 0 {
                ans.push(0);
            } else {
                let val = pow2[dist - 1];
                ans.push((val % MOD_I64) as i32);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (assign-edge-weights edges queries)
  (let* ((n (+ (length edges) 1))
         (logN (add1 (integer-length n))) ; enough bits for binary lifting
         ;; adjacency list
         (adj (make-vector (+ n 1) '()))
         ;; depth and parent vectors
         (depth (make-vector (+ n 1) -1))
         (parent (make-vector (+ n 1) 0))
         ;; up table: vector of vectors
         (up (let ((vec (make-vector (+ n 1) #f)))
               (for ([i (in-range (+ n 1))])
                 (vector-set! vec i (make-vector logN 0)))
               vec))
         ;; power of two modulo MOD
         (pow2 (let ((v (make-vector (+ n 1) 0)))
                 (vector-set! v 0 1)
                 (for ([i (in-range 1 (+ n 1))])
                   (vector-set! v i (modulo (* (vector-ref v (- i 1)) 2) MOD)))
                 v))
         ;; build adjacency
         )
    ;; add edges
    (for ([e edges])
      (let* ((u (first e))
             (v (second e)))
        (vector-set! adj u (cons v (vector-ref adj u)))
        (vector-set! adj v (cons u (vector-ref adj v)))))
    ;; iterative DFS/BFS to compute depth and parent
    (let ((stack (make-vector (+ n 1) 0))
          (top 0))
      (vector-set! depth 1 0)
      (vector-set! parent 1 0)
      (vector-set! stack top 1)
      (set! top (+ top 1))
      (let loop ()
        (when (> top 0)
          (set! top (- top 1))
          (let ((node (vector-ref stack top)))
            (for ([nbr (vector-ref adj node)])
              (when (= (vector-ref depth nbr) -1)
                (vector-set! depth nbr (+ (vector-ref depth node) 1))
                (vector-set! parent nbr node)
                (vector-set! stack top nbr)
                (set! top (+ top 1)))))
          (loop))))
    ;; fill up table
    (for ([i (in-range 1 (+ n 1))])
      (vector-set! (vector-ref up i) 0 (vector-ref parent i)))
    (for ([k (in-range 1 logN)])
      (for ([i (in-range 1 (+ n 1))])
        (let* ((mid (vector-ref (vector-ref up i) (- k 1))))
          (vector-set! (vector-ref up i) k
                       (if (= mid 0)
                           0
                           (vector-ref (vector-ref up mid) (- k 1)))))))
    ;; LCA function
    (define (lca u v)
      (when (< (vector-ref depth u) (vector-ref depth v))
        (let ((tmp u))
          (set! u v)
          (set! v tmp)))
      ;; raise u to depth of v
      (let ((diff (- (vector-ref depth u) (vector-ref depth v))))
        (for ([k (in-range logN)])
          (when (not (= (bitwise-and diff (arithmetic-shift 1 k)) 0))
            (set! u (vector-ref (vector-ref up u) k)))))
      (if (= u v)
          u
          (let loop ((k (- logN 1)) (uu u) (vv v))
            (if (< k 0)
                (vector-ref (vector-ref up uu) 0)
                (if (not (= (vector-ref (vector-ref up uu) k)
                            (vector-ref (vector-ref up vv) k)))
                    (loop (- k 1)
                          (vector-ref (vector-ref up uu) k)
                          (vector-ref (vector-ref up vv) k))
                    (loop (- k 1) uu vv))))))
    ;; process queries
    (let ((ans (make-vector (length queries) 0)))
      (let loop ((idx 0) (qs queries))
        (if (null? qs)
            (void)
            (let* ((q (car qs))
                   (u (first q))
                   (v (second q))
                   (anc (lca u v))
                   (dist (- (+ (vector-ref depth u) (vector-ref depth v))
                            (* 2 (vector-ref depth anc)))))
              (vector-set! ans idx
                           (if (= dist 0)
                               0
                               (vector-ref pow2 (- dist 1))))
              (loop (+ idx 1) (cdr qs)))))
      (vector->list ans))))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec assign_edge_weights(Edges :: [[integer()]], Queries :: [[integer()]]) -> [integer()].
assign_edge_weights(Edges, Queries) ->
    N = length(Edges) + 1,
    LogF = math:log2(N),
    LOG = trunc(math:ceil(LogF)) + 1,

    Adj0 = build_adj(Edges, #{}),

    {DepthMap, ParentMap} = dfs([{1,0}], #{1 => 0}, #{1 => 0}, Adj0),

    UpList = build_up(ParentMap, LOG),

    lists:map(
      fun([U,V]) ->
          Len = path_len(U, V, DepthMap, UpList),
          case Len of
              0 -> 0;
              _ -> pow_mod(2, Len-1)
          end
      end,
      Queries).

%% Build adjacency map
build_adj([], Adj) -> Adj;
build_adj([[U,V]|Rest], Adj) ->
    ListU = maps:get(U, Adj, []),
    ListV = maps:get(V, Adj, []),
    Adj1 = maps:put(U, [V|ListU], Adj),
    Adj2 = maps:put(V, [U|ListV], Adj1),
    build_adj(Rest, Adj2).

%% Depth-first traversal to fill depth and parent maps
dfs([], Depth, Parent, _Adj) -> {Depth, Parent};
dfs([{Node,Par}|Stack], Depth, Parent, Adj) ->
    Neigh = maps:get(Node, Adj, []),
    {NewDepth, NewParent, NewStack} =
        lists:foldl(
          fun(Nei, {DAcc,PAcc,SAcc}) ->
              case maps:is_key(Nei, DAcc) of
                  true -> {DAcc,PAcc,SAcc};
                  false ->
                      D1 = maps:put(Nei, maps:get(Node,DAcc)+1, DAcc),
                      P1 = maps:put(Nei, Node, PAcc),
                      {D1,P1,[{Nei,Node}|SAcc]}
              end
          end,
          {Depth, Parent, Stack},
          Neigh),
    dfs(NewStack, NewDepth, NewParent, Adj).

%% Build binary lifting tables
build_up(ParentMap, LOG) ->
    build_up_loop(1, LOG-1, [ParentMap], ParentMap).

build_up_loop(K, MaxK, UpAcc, PrevMap) when K =< MaxK ->
    NewMap = maps:fold(
               fun(Node,_Val,Acc) ->
                   AncPrev = maps:get(Node, PrevMap, 0),
                   Anc2 = case maps:get(AncPrev, PrevMap, 0) of
                              undefined -> 0;
                              A -> A
                          end,
                   maps:put(Node, Anc2, Acc)
               end,
               #{},
               PrevMap),
    build_up_loop(K+1, MaxK, UpAcc ++ [NewMap], NewMap);
build_up_loop(_, _, UpAcc, _) -> UpAcc.

%% Compute path length between two nodes
path_len(U, V, DepthMap, UpList) ->
    LCA = lca(U, V, DepthMap, UpList),
    DU = maps:get(U, DepthMap),
    DV = maps:get(V, DepthMap),
    DL = maps:get(LCA, DepthMap),
    DU + DV - 2*DL.

%% Lowest Common Ancestor using binary lifting
lca(U, V, DepthMap, UpList) ->
    DU = maps:get(U, DepthMap),
    DV = maps:get(V, DepthMap),
    {U1,V1} = if DU < DV -> {V,U}; true -> {U,V} end,
    Diff = abs(DU - DV),
    U2 = lift(U1, Diff, UpList),
    V2 = V1,
    case U2 == V2 of
        true -> U2;
        false ->
            MaxIdx = length(UpList) - 1,
            lca_up(U2, V2, MaxIdx, UpList)
    end.

lift(Node, 0, _UpList) -> Node;
lift(Node, Diff, UpList) ->
    lift(Node, Diff, 0, UpList).

lift(Node, 0, _K, _UpList) -> Node;
lift(Node, Diff, K, UpList) when Diff > 0 ->
    case (Diff band 1) of
        1 ->
            Map = lists:nth(K+1, UpList),
            NewNode = maps:get(Node, Map, 0),
            lift(NewNode, Diff bsr 1, K+1, UpList);
        0 ->
            lift(Node, Diff bsr 1, K+1, UpList)
    end.

lca_up(U, V, -1, UpList) ->
    % after processing all levels, parent of U (or V) is LCA
    ParentMap = lists:nth(1, UpList),
    maps:get(U, ParentMap, 0);
lca_up(U, V, Idx, UpList) ->
    Map = lists:nth(Idx+1, UpList),
    AncU = maps:get(U, Map, 0),
    AncV = maps:get(V, Map, 0),
    if
        AncU =/= AncV andalso AncU =/= 0 ->
            lca_up(AncU, AncV, Idx-1, UpList);
        true ->
            lca_up(U, V, Idx-1, UpList)
    end.

%% Fast modular exponentiation
pow_mod(_, 0) -> 1;
pow_mod(Base, Exp) when (Exp band 1) =:= 1 ->
    (Base * pow_mod((Base*Base) rem ?MOD, Exp bsr 1)) rem ?MOD;
pow_mod(Base, Exp) ->
    pow_mod((Base*Base) rem ?MOD, Exp bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec assign_edge_weights(edges :: [[integer]], queries :: [[integer]]) :: [integer]
  def assign_edge_weights(edges, queries) do
    n = length(edges) + 1
    mod = 1_000_000_007

    # build adjacency map
    adj =
      Enum.reduce(edges, %{}, fn [u, v], acc ->
        acc
        |> Map.update(u, [v], &[v | &1])
        |> Map.update(v, [u], &[u | &1])
      end)

    # DFS iterative to compute depth and parent (level 0 ancestor)
    {depth, parent} = dfs(1, adj, n)

    # binary lifting tables
    max_log = 
      :math.log2(n) |> Float.ceil() |> trunc()

    ancestors = build_ancestors(parent, max_log, n)

    # process queries
    Enum.map(queries, fn [u, v] ->
      l = lca(u, v, depth, ancestors, max_log)
      dist = depth[u] + depth[v] - 2 * depth[l]
      if dist == 0 do
        0
      else
        pow_mod(2, dist - 1, mod)
      end
    end)
  end

  # Depth-first search using a stack to avoid recursion limits
  defp dfs(root, adj, n) do
    depth = %{}
    parent = %{}
    stack = [{root, 0}]
    {depth, parent} =
      Enum.reduce_while(stack, {depth, parent}, fn _ , acc -> 
        # placeholder; actual loop handled below
        {:cont, acc}
      end)
    # Use explicit while-like recursion
    dfs_loop([{root, 0}], depth, parent, adj)
  end

  defp dfs_loop([], depth, parent, _adj), do: {depth, parent}
  defp dfs_loop([{node, par} | rest], depth, parent, adj) do
    d = if par == 0, do: 0, else: Map.get(depth, par) + 1
    depth = Map.put(depth, node, d)
    parent = Map.put(parent, node, par)

    children =
      Map.get(adj, node, [])
      |> Enum.filter(fn nb -> nb != par end)
      |> Enum.map(&{&1, node})

    dfs_loop(children ++ rest, depth, parent, adj)
  end

  # Build ancestors tables up to max_log
  defp build_ancestors(parent, max_log, n) do
    # ancestors list where anc[0] = parent map
    anc0 = parent
    build_ancestors([anc0], max_log, 1)
  end

  defp build_ancestors(anc_list, max_log, k) when k > max_log, do: Enum.reverse(anc_list)

  defp build_ancestors(anc_list, max_log, k) do
    prev = hd(anc_list)
    cur =
      Enum.reduce(1..length(prev), %{}, fn node, acc ->
        p = Map.get(prev, node, 0)
        pp = if p == 0, do: 0, else: Map.get(prev, p, 0)
        Map.put(acc, node, pp)
      end)

    build_ancestors([cur | anc_list], max_log, k + 1)
  end

  # Lowest Common Ancestor using binary lifting
  defp lca(u, v, depth, ancestors, max_log) do
    {u, v} =
      if Map.get(depth, u) < Map.get(depth, v) do
        {v, u}
      else
        {u, v}
      end

    diff = Map.get(depth, u) - Map.get(depth, v)
    u = lift(u, diff, ancestors)

    if u == v do
      u
    else
      {u_final, _v_final} =
        Enum.reduce((max_log)..0, {u, v}, fn k, {a, b} ->
          anc_k = Enum.at(ancestors, k)
          pa = Map.get(anc_k, a, 0)
          pb = Map.get(anc_k, b, 0)

          if pa != pb and pa != 0 do
            {pa, pb}
          else
            {a, b}
          end
        end)

      # parent of u_final is the LCA
      anc0 = hd(ancestors)
      Map.get(anc0, u_final, 0)
    end
  end

  defp lift(node, 0, _ancestors), do: node
  defp lift(node, diff, ancestors) do
    Enum.reduce(0..(length(ancestors) - 1), node, fn k, cur ->
      if (diff &&& (1 <<< k)) != 0 do
        anc_k = Enum.at(ancestors, k)
        Map.get(anc_k, cur, 0)
      else
        cur
      end
    end)
  end

  # fast modular exponentiation
  defp pow_mod(_base, 0, _mod), do: 1
  defp pow_mod(base, exp, mod) do
    rec_pow(base, exp, 1, mod)
  end

  defp rec_pow(_base, 0, acc, _mod), do: acc
  defp rec_pow(base, exp, acc, mod) do
    acc = if (exp &&& 1) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    rec_pow(base, exp >>> 1, acc, mod)
  end

  # import Bitwise for bit operations
  use Bitwise
end
```

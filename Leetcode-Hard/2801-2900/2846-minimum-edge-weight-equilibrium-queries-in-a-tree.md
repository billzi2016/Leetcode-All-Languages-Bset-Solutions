# 2846. Minimum Edge Weight Equilibrium Queries in a Tree

## Cpp

```cpp
class Solution {
public:
    vector<int> minOperationsQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        const int LOG = 15; // since 2^14 > 1e4
        const int MAXW = 27; // weights 1..26
        
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u=e[0], v=e[1], w=e[2];
            adj[u].push_back({v,w});
            adj[v].push_back({u,w});
        }
        
        vector<array<int,MAXW>> freq(n);
        for (int i=0;i<n;++i) freq[i].fill(0);
        vector<int> depth(n,0);
        vector<vector<int>> up(n, vector<int>(LOG,0));
        
        // DFS stack
        vector<int> st = {0};
        vector<int> parent(n,-1);
        parent[0]=0;
        while(!st.empty()){
            int u=st.back(); st.pop_back();
            for (auto [v,w]: adj[u]){
                if(v==parent[u]) continue;
                parent[v]=u;
                depth[v]=depth[u]+1;
                up[v][0]=u;
                for(int k=1;k<LOG;++k){
                    up[v][k]=up[ up[v][k-1] ][k-1];
                }
                freq[v]=freq[u];
                freq[v][w]++; // edge weight counted on path root->v
                st.push_back(v);
            }
        }
        // ensure root ancestors point to itself
        for(int k=0;k<LOG;++k) up[0][k]=0;
        
        auto lca = [&](int a, int b){
            if(depth[a]<depth[b]) swap(a,b);
            int diff=depth[a]-depth[b];
            for(int k=0;k<LOG;++k){
                if(diff>>k & 1) a=up[a][k];
            }
            if(a==b) return a;
            for(int k=LOG-1;k>=0;--k){
                if(up[a][k]!=up[b][k]){
                    a=up[a][k];
                    b=up[b][k];
                }
            }
            return up[a][0];
        };
        
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &q: queries) {
            int a=q[0], b=q[1];
            int L = lca(a,b);
            int totalEdges = depth[a] + depth[b] - 2*depth[L];
            int best = 0;
            for(int w=1; w<MAXW; ++w){
                int cnt = freq[a][w] + freq[b][w] - 2*freq[L][w];
                if(cnt>best) best=cnt;
            }
            ans.push_back(totalEdges - best);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MAXW = 26;
    private int LOG;
    private int[][] up;
    private int[] depth;
    private int[][] freq;

    public int[] minOperationsQueries(int n, int[][] edges, int[][] queries) {
        @SuppressWarnings("unchecked")
        java.util.List<int[]>[] adj = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        up = new int[LOG][n];
        depth = new int[n];
        freq = new int[n][MAXW + 1];

        boolean[] visited = new boolean[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        stack.push(0);
        visited[0] = true;
        up[0][0] = 0;

        while (!stack.isEmpty()) {
            int u = stack.pop();
            for (int[] vw : adj[u]) {
                int v = vw[0], w = vw[1];
                if (!visited[v]) {
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    up[0][v] = u;
                    System.arraycopy(freq[u], 0, freq[v], 0, MAXW + 1);
                    freq[v][w]++;
                    stack.push(v);
                }
            }
        }

        for (int k = 1; k < LOG; k++) {
            for (int v = 0; v < n; v++) {
                up[k][v] = up[k - 1][up[k - 1][v]];
            }
        }

        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int a = queries[i][0], b = queries[i][1];
            int L = lca(a, b);
            int totalEdges = depth[a] + depth[b] - 2 * depth[L];
            int maxCnt = 0;
            for (int w = 1; w <= MAXW; w++) {
                int cnt = freq[a][w] + freq[b][w] - 2 * freq[L][w];
                if (cnt > maxCnt) maxCnt = cnt;
            }
            ans[i] = totalEdges - maxCnt;
        }
        return ans;
    }

    private int lca(int a, int b) {
        if (depth[a] < depth[b]) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        int diff = depth[a] - depth[b];
        for (int k = 0; k < LOG; k++) {
            if (((diff >> k) & 1) == 1) {
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
}
```

## Python

```python
class Solution(object):
    def minOperationsQueries(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque

        # build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = (n).bit_length()
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        # pref[node][weight] = count of edges with that weight from root to node
        pref = [[0] * 27 for _ in range(n)]

        # BFS/DFS from root 0
        stack = deque([0])
        visited = [False] * n
        visited[0] = True
        while stack:
            u = stack.pop()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u
                    # copy prefix counts
                    pref[v][:] = pref[u][:]
                    pref[v][w] += 1
                    stack.append(v)

        # binary lifting table
        for k in range(1, LOG):
            pk = parent[k - 1]
            ppk = parent[k]
            for v in range(n):
                anc = pk[v]
                if anc != -1:
                    ppk[v] = pk[anc]

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
                pu, pv = parent[k][u], parent[k][v]
                if pu != -1 and pu != pv:
                    u, v = pu, pv
            return parent[0][u]

        ans = []
        for a, b in queries:
            anc = lca(a, b)
            path_len = depth[a] + depth[b] - 2 * depth[anc]
            maxfreq = 0
            # compute frequencies for each weight
            pa = pref[a]
            pb = pref[b]
            pc = pref[anc]
            for w in range(1, 27):
                freq = pa[w] + pb[w] - 2 * pc[w]
                if freq > maxfreq:
                    maxfreq = freq
            ans.append(path_len - maxfreq)
        return ans
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = (n).bit_length()
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        freq = [[0] * 27 for _ in range(n)]

        dq = deque([0])
        visited = [False] * n
        visited[0] = True
        while dq:
            u = dq.popleft()
            fu = freq[u]
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    fv = freq[v]
                    fv[:] = fu[:]
                    fv[w] += 1
                    dq.append(v)

        for k in range(1, LOG):
            pk = parent[k - 1]
            ppk = parent[k]
            for v in range(n):
                if pk[v] != -1:
                    ppk[v] = pk[pk[v]]

        def lca(u: int, v: int) -> int:
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
                pu, pv = parent[k][u], parent[k][v]
                if pu != -1 and pu != pv:
                    u, v = pu, pv
            return parent[0][u]

        ans = []
        for a, b in queries:
            l = lca(a, b)
            path_len = depth[a] + depth[b] - 2 * depth[l]
            fa, fb, fl = freq[a], freq[b], freq[l]
            maxcnt = 0
            for w in range(1, 27):
                cnt = fa[w] + fb[w] - 2 * fl[w]
                if cnt > maxcnt:
                    maxcnt = cnt
            ans.append(path_len - maxcnt)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MAXW 27   // weights are 1..26

static int LOGN;

/* adjacency list */
typedef struct {
    int to;
    int w;
    int next;
} Edge;

static int *head;
static Edge *edgesArr;
static int edgeCnt;

/* tree data */
static int n;
static int **freq;          // freq[node][weight]
static int *depth;
static int **up;            // up[node][k]

/* add undirected edge */
static void addEdge(int u, int v, int w) {
    edgesArr[edgeCnt].to = v;
    edgesArr[edgeCnt].w = w;
    edgesArr[edgeCnt].next = head[u];
    head[u] = edgeCnt++;
}

/* LCA using binary lifting */
static int lca(int a, int b) {
    if (depth[a] < depth[b]) {
        int tmp = a; a = b; b = tmp;
    }
    int diff = depth[a] - depth[b];
    for (int k = 0; diff; ++k) {
        if (diff & 1) a = up[a][k];
        diff >>= 1;
    }
    if (a == b) return a;
    for (int k = LOGN - 1; k >= 0; --k) {
        if (up[a][k] != up[b][k]) {
            a = up[a][k];
            b = up[b][k];
        }
    }
    return up[a][0];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minOperationsQueries(int n_, int** edges, int edgesSize, int* edgesColSize,
                          int** queries, int queriesSize, int* queriesColSize,
                          int* returnSize) {
    n = n_;
    /* compute LOGN */
    LOGN = 1;
    while ((1 << LOGN) <= n) ++LOGN;

    /* allocate adjacency */
    head = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    edgesArr = (Edge*)malloc(sizeof(Edge) * (2 * (n - 1)));
    edgeCnt = 0;

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];   // weight in [1,26]
        addEdge(u, v, w);
        addEdge(v, u, w);
    }

    /* allocate structures */
    depth = (int*)calloc(n, sizeof(int));
    up = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; ++i) up[i] = (int*)calloc(LOGN, sizeof(int));

    freq = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; ++i) {
        freq[i] = (int*)calloc(MAXW, sizeof(int));
    }

    /* BFS/DFS from root 0 */
    int *queue = (int*)malloc(sizeof(int) * n);
    int qh = 0, qt = 0;
    queue[qt++] = 0;
    up[0][0] = 0;   // parent of root is itself
    depth[0] = 0;

    while (qh < qt) {
        int u = queue[qh++];
        for (int e = head[u]; e != -1; e = edgesArr[e].next) {
            int v = edgesArr[e].to;
            int w = edgesArr[e].w;
            if (v == up[u][0] && u != 0) continue; // avoid going back to parent
            if (v == 0 && u != 0 && up[v][0] != 0) {
                /* already visited root from another child, skip */
                continue;
            }
            if (v != up[u][0]) {   // not parent
                depth[v] = depth[u] + 1;
                up[v][0] = u;
                memcpy(freq[v], freq[u], sizeof(int) * MAXW);
                ++freq[v][w];
                queue[qt++] = v;
            }
        }
    }

    /* binary lifting table */
    for (int k = 1; k < LOGN; ++k) {
        for (int i = 0; i < n; ++i) {
            up[i][k] = up[ up[i][k-1] ][k-1];
        }
    }

    /* answer queries */
    int *ans = (int*)malloc(sizeof(int) * queriesSize);
    for (int qi = 0; qi < queriesSize; ++qi) {
        int a = queries[qi][0];
        int b = queries[qi][1];
        int c = lca(a, b);
        int pathLen = depth[a] + depth[b] - 2 * depth[c];
        int best = 0;
        for (int w = 1; w < MAXW; ++w) {
            int cnt = freq[a][w] + freq[b][w] - 2 * freq[c][w];
            if (cnt > best) best = cnt;
        }
        ans[qi] = pathLen - best;
    }

    *returnSize = queriesSize;

    /* free temporary allocations (optional, as LeetCode does not require) */
    free(queue);
    for (int i = 0; i < n; ++i) {
        free(up[i]);
        free(freq[i]);
    }
    free(up);
    free(freq);
    free(depth);
    free(head);
    free(edgesArr);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] MinOperationsQueries(int n, int[][] edges, int[][] queries) {
        const int MAXW = 26;
        int LOG = 15; // since 2^14 > 10000

        var graph = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].Add((v, w));
            graph[v].Add((u, w));
        }

        int[,] freq = new int[n, MAXW + 1]; // weight index 1..26
        int[] depth = new int[n];
        int[][] parent = new int[LOG][];
        for (int i = 0; i < LOG; i++) parent[i] = new int[n];

        // iterative DFS from root 0
        var stack = new Stack<(int node, int par)>();
        stack.Push((0, -1));
        depth[0] = 0;
        parent[0][0] = 0;

        while (stack.Count > 0) {
            var cur = stack.Pop();
            int u = cur.node, p = cur.par;
            foreach (var edge in graph[u]) {
                int v = edge.to;
                if (v == p) continue;
                depth[v] = depth[u] + 1;
                parent[0][v] = u;
                // copy frequencies
                for (int w = 1; w <= MAXW; w++) {
                    freq[v, w] = freq[u, w];
                }
                freq[v, edge.w]++; // include this edge
                stack.Push((v, u));
            }
        }

        // binary lifting table
        for (int k = 1; k < LOG; k++) {
            for (int v = 0; v < n; v++) {
                parent[k][v] = parent[k - 1][parent[k - 1][v]];
            }
        }

        int Lca(int a, int b) {
            if (depth[a] < depth[b]) { int tmp = a; a = b; b = tmp; }
            int diff = depth[a] - depth[b];
            for (int i = 0; diff > 0; i++) {
                if ((diff & 1) == 1) a = parent[i][a];
                diff >>= 1;
            }
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; k--) {
                if (parent[k][a] != parent[k][b]) {
                    a = parent[k][a];
                    b = parent[k][b];
                }
            }
            return parent[0][a];
        }

        int m = queries.Length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int a = queries[i][0];
            int b = queries[i][1];
            int l = Lca(a, b);
            int pathLen = depth[a] + depth[b] - 2 * depth[l];
            int maxFreq = 0;
            for (int w = 1; w <= MAXW; w++) {
                int cnt = freq[a, w] + freq[b, w] - 2 * freq[l, w];
                if (cnt > maxFreq) maxFreq = cnt;
            }
            ans[i] = pathLen - maxFreq;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[][]} queries
 * @return {number[]}
 */
var minOperationsQueries = function(n, edges, queries) {
    const adj = Array.from({length: n}, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    const LOG = Math.ceil(Math.log2(n)) + 1;
    const up = Array.from({length: LOG}, () => new Uint16Array(n));
    const depth = new Uint16Array(n);
    const freq = new Array(n);
    // root at 0
    freq[0] = new Uint16Array(27); // weights are 1..26

    const parent = new Uint16Array(n);
    parent[0] = 0;
    up[0][0] = 0;

    // BFS/DFS to fill depth, parent, freq
    const order = [0];
    for (let idx = 0; idx < order.length; ++idx) {
        const u = order[idx];
        for (const [v, w] of adj[u]) {
            if (v === parent[u]) continue;
            parent[v] = u;
            up[0][v] = u;
            depth[v] = depth[u] + 1;
            const arr = new Uint16Array(27);
            arr.set(freq[u]);
            arr[w]++; // weight index
            freq[v] = arr;
            order.push(v);
        }
    }

    // binary lifting table
    for (let k = 1; k < LOG; ++k) {
        const prev = up[k - 1];
        const cur = up[k];
        for (let v = 0; v < n; ++v) {
            cur[v] = prev[prev[v]];
        }
    }

    function lca(u, v) {
        if (depth[u] < depth[v]) {
            [u, v] = [v, u];
        }
        // lift u up to depth of v
        let diff = depth[u] - depth[v];
        let k = 0;
        while (diff) {
            if (diff & 1) u = up[k][u];
            diff >>= 1;
            ++k;
        }
        if (u === v) return u;
        for (let i = LOG - 1; i >= 0; --i) {
            if (up[i][u] !== up[i][v]) {
                u = up[i][u];
                v = up[i][v];
            }
        }
        return up[0][u];
    }

    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [a, b] = queries[i];
        const anc = lca(a, b);
        const pathLen = depth[a] + depth[b] - 2 * depth[anc];
        let maxCnt = 0;
        const fa = freq[a], fb = freq[b], fc = freq[anc];
        for (let w = 1; w <= 26; ++w) {
            const cnt = fa[w] + fb[w] - 2 * fc[w];
            if (cnt > maxCnt) maxCnt = cnt;
        }
        ans[i] = pathLen - maxCnt;
    }
    return ans;
};
```

## Typescript

```typescript
function minOperationsQueries(n: number, edges: number[][], queries: number[][]): number[] {
    const LOG = Math.ceil(Math.log2(Math.max(1, n))) + 1;
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    const depth = new Int32Array(n);
    const up: number[][] = Array.from({ length: LOG }, () => Array(n).fill(-1));
    const freq: Uint16Array[] = new Array(n);

    // BFS/DFS to set parent, depth and prefix frequencies
    const stack: number[] = [0];
    const visited = new Uint8Array(n);
    visited[0] = 1;
    freq[0] = new Uint16Array(27); // indices 1..26 used

    while (stack.length) {
        const node = stack.pop() as number;
        for (const [to, w] of adj[node]) {
            if (visited[to]) continue;
            visited[to] = 1;
            depth[to] = depth[node] + 1;
            up[0][to] = node;

            const curFreq = new Uint16Array(27);
            const parentFreq = freq[node];
            for (let i = 1; i <= 26; ++i) {
                curFreq[i] = parentFreq[i];
            }
            curFreq[w]++;
            freq[to] = curFreq;

            stack.push(to);
        }
    }

    // binary lifting table
    for (let k = 1; k < LOG; ++k) {
        const prev = up[k - 1];
        const curr = up[k];
        for (let v = 0; v < n; ++v) {
            const mid = prev[v];
            curr[v] = mid === -1 ? -1 : prev[mid];
        }
    }

    function lca(u0: number, v0: number): number {
        let u = u0, v = v0;
        if (depth[u] < depth[v]) {
            const tmp = u; u = v; v = tmp;
        }
        // lift u up to depth of v
        let diff = depth[u] - depth[v];
        let k = 0;
        while (diff) {
            if (diff & 1) u = up[k][u];
            diff >>= 1;
            ++k;
        }
        if (u === v) return u;
        for (let i = LOG - 1; i >= 0; --i) {
            const pu = up[i][u];
            const pv = up[i][v];
            if (pu !== pv) {
                u = pu;
                v = pv;
            }
        }
        return up[0][u];
    }

    const ans: number[] = new Array(queries.length);
    for (let idx = 0; idx < queries.length; ++idx) {
        const [a, b] = queries[idx];
        if (a === b) {
            ans[idx] = 0;
            continue;
        }
        const anc = lca(a, b);
        const pathLen = depth[a] + depth[b] - 2 * depth[anc];
        let maxCnt = 0;
        const freqA = freq[a];
        const freqB = freq[b];
        const freqAnc = freq[anc];
        for (let w = 1; w <= 26; ++w) {
            const cnt = freqA[w] + freqB[w] - 2 * freqAnc[w];
            if (cnt > maxCnt) maxCnt = cnt;
        }
        ans[idx] = pathLen - maxCnt;
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
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function minOperationsQueries($n, $edges, $queries) {
        // compute log for binary lifting
        $LOG = 0;
        while ((1 << $LOG) <= $n) {
            $LOG++;
        }

        // build adjacency list
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $w] = $e;
            $graph[$u][] = [$v, $w];
            $graph[$v][] = [$u, $w];
        }

        // arrays for depth, ancestors and frequency prefix
        $depth = array_fill(0, $n, 0);
        $up = [];
        for ($k = 0; $k < $LOG; $k++) {
            $up[$k] = array_fill(0, $n, -1);
        }
        // freq[node][weight] (weights are 1..26)
        $freq = array_fill(0, $n, array_fill(0, 27, 0));

        // iterative DFS to fill depth, up[0], and freq
        $stack = [[0, -1]];
        while ($stack) {
            [$u, $p] = array_pop($stack);
            foreach ($graph[$u] as $edge) {
                [$v, $w] = $edge;
                if ($v == $p) continue;
                $depth[$v] = $depth[$u] + 1;
                $up[0][$v] = $u;
                // copy frequency from parent and add current edge weight
                $freq[$v] = $freq[$u];
                $freq[$v][$w] += 1;
                $stack[] = [$v, $u];
            }
        }

        // binary lifting table
        for ($k = 1; $k < $LOG; $k++) {
            for ($v = 0; $v < $n; $v++) {
                $mid = $up[$k - 1][$v];
                if ($mid != -1) {
                    $up[$k][$v] = $up[$k - 1][$mid];
                } else {
                    $up[$k][$v] = -1;
                }
            }
        }

        // LCA closure
        $lca = function($a, $b) use (&$depth, &$up, $LOG) {
            if ($depth[$a] < $depth[$b]) {
                $tmp = $a; $a = $b; $b = $tmp;
            }
            $diff = $depth[$a] - $depth[$b];
            for ($k = 0; $k < $LOG; $k++) {
                if (($diff >> $k) & 1) {
                    $a = $up[$k][$a];
                }
            }
            if ($a == $b) return $a;
            for ($k = $LOG - 1; $k >= 0; $k--) {
                if ($up[$k][$a] != -1 && $up[$k][$a] != $up[$k][$b]) {
                    $a = $up[$k][$a];
                    $b = $up[$k][$b];
                }
            }
            return $up[0][$a];
        };

        // answer queries
        $answers = [];
        foreach ($queries as $qr) {
            [$a, $b] = $qr;
            $l = $lca($a, $b);
            $len = $depth[$a] + $depth[$b] - 2 * $depth[$l];
            $maxCnt = 0;
            for ($w = 1; $w <= 26; $w++) {
                $cnt = $freq[$a][$w] + $freq[$b][$w] - 2 * $freq[$l][$w];
                if ($cnt > $maxCnt) $maxCnt = $cnt;
            }
            $answers[] = $len - $maxCnt;
        }

        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    func minOperationsQueries(_ n: Int, _ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        let LOG = 15
        var graph = Array(repeating: [(to: Int, w: Int)](), count: n)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            graph[u].append((v, w))
            graph[v].append((u, w))
        }
        
        var depth = Array(repeating: 0, count: n)
        var up = Array(repeating: Array(repeating: -1, count: LOG), count: n)
        var freq = Array(repeating: Array(repeating: 0, count: 27), count: n) // weights 1..26
        
        var stack: [(Int, Int)] = [(0, -1)]
        while let (node, parent) = stack.popLast() {
            up[node][0] = parent
            if parent != -1 {
                depth[node] = depth[parent] + 1
                freq[node] = freq[parent]
            }
            for edge in graph[node] {
                if edge.to == parent { continue }
                // copy current frequencies and add this edge weight
                var childFreq = freq[node]
                childFreq[edge.w] += 1
                freq[edge.to] = childFreq
                stack.append((edge.to, node))
            }
        }
        
        // binary lifting table
        if LOG > 1 {
            for k in 1..<LOG {
                for v in 0..<n {
                    let mid = up[v][k - 1]
                    if mid != -1 {
                        up[v][k] = up[mid][k - 1]
                    } else {
                        up[v][k] = -1
                    }
                }
            }
        }
        
        func lca(_ a: Int, _ b: Int) -> Int {
            var u = a, v = b
            if depth[u] < depth[v] { swap(&u, &v) }
            var diff = depth[u] - depth[v]
            var bit = 0
            while diff > 0 {
                if (diff & 1) == 1 {
                    u = up[u][bit]
                }
                diff >>= 1
                bit += 1
            }
            if u == v { return u }
            for k in stride(from: LOG - 1, through: 0, by: -1) {
                if up[u][k] != up[v][k] {
                    u = up[u][k]
                    v = up[v][k]
                }
            }
            return up[u][0]
        }
        
        var answer = [Int]()
        for q in queries {
            let a = q[0], b = q[1]
            let anc = lca(a, b)
            let pathLen = depth[a] + depth[b] - 2 * depth[anc]
            var maxCnt = 0
            for w in 1...26 {
                let cnt = freq[a][w] + freq[b][w] - 2 * freq[anc][w]
                if cnt > maxCnt { maxCnt = cnt }
            }
            answer.append(pathLen - maxCnt)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperationsQueries(n: Int, edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val LOG = 15
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        val parent = Array(LOG) { IntArray(n) { -1 } }
        val depth = IntArray(n)
        val cnt = Array(n) { IntArray(27) } // weight 1..26

        fun dfs(u: Int, p: Int) {
            for ((v, w) in adj[u]) {
                if (v == p) continue
                parent[0][v] = u
                depth[v] = depth[u] + 1
                val cur = cnt[v]
                val prev = cnt[u]
                for (i in 1..26) {
                    cur[i] = prev[i]
                }
                cur[w]++
                dfs(v, u)
            }
        }

        // root at 0
        dfs(0, -1)

        for (k in 1 until LOG) {
            for (v in 0 until n) {
                val mid = parent[k - 1][v]
                parent[k][v] = if (mid == -1) -1 else parent[k - 1][mid]
            }
        }

        fun lca(u0: Int, v0: Int): Int {
            var u = u0
            var v = v0
            if (depth[u] < depth[v]) {
                val tmp = u; u = v; v = tmp
            }
            var diff = depth[u] - depth[v]
            var bit = 0
            while (diff > 0) {
                if ((diff and 1) == 1) {
                    u = parent[bit][u]
                }
                diff = diff shr 1
                bit++
            }
            if (u == v) return u
            for (k in LOG - 1 downTo 0) {
                val pu = parent[k][u]
                val pv = parent[k][v]
                if (pu != -1 && pu != pv) {
                    u = pu
                    v = pv
                }
            }
            return parent[0][u]
        }

        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val a = queries[i][0]
            val b = queries[i][1]
            val l = lca(a, b)
            val pathLen = depth[a] + depth[b] - 2 * depth[l]
            var maxFreq = 0
            for (w in 1..26) {
                val freq = cnt[a][w] + cnt[b][w] - 2 * cnt[l][w]
                if (freq > maxFreq) maxFreq = freq
            }
            ans[i] = pathLen - maxFreq
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> minOperationsQueries(int n, List<List<int>> edges, List<List<int>> queries) {
    const int MAX_W = 26;
    // Build adjacency list
    List<List<List<int>>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      int w = e[2];
      adj[u].add([v, w]);
      adj[v].add([u, w]);
    }

    // Log size for binary lifting
    int LOG = 1;
    while ((1 << LOG) <= n) LOG++;
    // ancestors[node][k]
    List<List<int>> anc = List.generate(n, (_) => List.filled(LOG, -1));
    List<int> depth = List.filled(n, 0);
    // cumulative frequencies of weights from root to node
    List<List<int>> cum = List.generate(n, (_) => List.filled(MAX_W + 1, 0));

    // Iterative DFS from root (node 0)
    List<int> stackNode = [0];
    List<int> stackParent = [-1];
    while (stackNode.isNotEmpty) {
      int node = stackNode.removeLast();
      int parent = stackParent.removeLast();

      for (var e in adj[node]) {
        int nb = e[0];
        int w = e[1];
        if (nb == parent) continue;
        depth[nb] = depth[node] + 1;
        anc[nb][0] = node;
        for (int k = 1; k < LOG; k++) {
          int prev = anc[nb][k - 1];
          anc[nb][k] = (prev == -1) ? -1 : anc[prev][k - 1];
        }
        // copy cumulative frequencies and add current edge weight
        List<int> parentCum = cum[node];
        List<int> childCum = cum[nb];
        for (int i = 1; i <= MAX_W; i++) {
          childCum[i] = parentCum[i];
        }
        childCum[w] += 1;

        stackNode.add(nb);
        stackParent.add(node);
      }
    }

    int lca(int a, int b) {
      if (depth[a] < depth[b]) {
        int tmp = a;
        a = b;
        b = tmp;
      }
      int diff = depth[a] - depth[b];
      for (int k = 0; k < LOG; k++) {
        if ((diff & (1 << k)) != 0) {
          a = anc[a][k];
        }
      }
      if (a == b) return a;
      for (int k = LOG - 1; k >= 0; k--) {
        if (anc[a][k] != -1 && anc[a][k] != anc[b][k]) {
          a = anc[a][k];
          b = anc[b][k];
        }
      }
      return anc[a][0];
    }

    List<int> answer = [];
    for (var q in queries) {
      int a = q[0];
      int b = q[1];
      int l = lca(a, b);
      int pathLen = depth[a] + depth[b] - 2 * depth[l];
      int maxFreq = 0;
      for (int w = 1; w <= MAX_W; w++) {
        int freq = cum[a][w] + cum[b][w] - 2 * cum[l][w];
        if (freq > maxFreq) maxFreq = freq;
      }
      answer.add(pathLen - maxFreq);
    }

    return answer;
  }
}
```

## Golang

```go
func minOperationsQueries(n int, edges [][]int, queries [][]int) []int {
	const maxW = 26
	const LOG = 15

	type Edge struct{ to, w int }
	adj := make([][]Edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		adj[u] = append(adj[u], Edge{v, w})
		adj[v] = append(adj[v], Edge{u, w})
	}

	depth := make([]int, n)
	parent := make([][]int, LOG)
	for i := 0; i < LOG; i++ {
		parent[i] = make([]int, n)
		for j := 0; j < n; j++ {
			parent[i][j] = -1
		}
	}
	freq := make([][maxW + 1]int, n)

	var dfs func(u, p int)
	dfs = func(u, p int) {
		for _, e := range adj[u] {
			v := e.to
			if v == p {
				continue
			}
			depth[v] = depth[u] + 1
			parent[0][v] = u
			freq[v] = freq[u]
			freq[v][e.w]++
			dfs(v, u)
		}
	}
	dfs(0, -1)

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
		bit := 0
		for diff > 0 {
			if diff&1 == 1 {
				u = parent[bit][u]
			}
			diff >>= 1
			bit++
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

	ans := make([]int, len(queries))
	for i, q := range queries {
		a, b := q[0], q[1]
		anc := lca(a, b)
		pathLen := depth[a] + depth[b] - 2*depth[anc]
		maxCnt := 0
		for w := 1; w <= maxW; w++ {
			cnt := freq[a][w] + freq[b][w] - 2*freq[anc][w]
			if cnt > maxCnt {
				maxCnt = cnt
			}
		}
		ans[i] = pathLen - maxCnt
	}
	return ans
}
```

## Ruby

```ruby
def min_operations_queries(n, edges, queries)
  # Build adjacency list
  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  # Prepare structures
  log = 0
  while (1 << log) <= n
    log += 1
  end
  up = Array.new(log) { Array.new(n, -1) }
  depth = Array.new(n, 0)
  freq = Array.new(n) { Array.new(27, 0) } # weights are 1..26

  # BFS/DFS from root 0 to fill parent, depth and prefix frequencies
  queue = [0]
  head = 0
  while head < queue.size
    u = queue[head]
    head += 1
    adj[u].each do |v, w|
      next if v == up[0][u] # already visited (parent)
      depth[v] = depth[u] + 1
      up[0][v] = u
      freq[v] = freq[u].dup
      freq[v][w] += 1
      queue << v
    end
  end

  # Binary lifting table
  (1...log).each do |k|
    n.times do |v|
      anc = up[k - 1][v]
      up[k][v] = anc == -1 ? -1 : up[k - 1][anc]
    end
  end

  # LCA lambda using closure variables
  lca = lambda do |a, b|
    if depth[a] < depth[b]
      a, b = b, a
    end
    diff = depth[a] - depth[b]
    k = 0
    while diff > 0
      if (diff & 1) == 1
        a = up[k][a]
      end
      diff >>= 1
      k += 1
    end
    return a if a == b
    (log - 1).downto(0) do |k2|
      if up[k2][a] != -1 && up[k2][a] != up[k2][b]
        a = up[k2][a]
        b = up[k2][b]
      end
    end
    up[0][a]
  end

  # Process queries
  ans = []
  queries.each do |a, b|
    anc = lca.call(a, b)
    path_len = depth[a] + depth[b] - 2 * depth[anc]
    max_cnt = 0
    (1..26).each do |w|
      cnt = freq[a][w] + freq[b][w] - 2 * freq[anc][w]
      max_cnt = cnt if cnt > max_cnt
    end
    ans << (path_len - max_cnt)
  end

  ans
end
```

## Scala

```scala
object Solution {
  def minOperationsQueries(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val LOG = 15 // since n <= 1e4, 2^14=16384
    val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val w = e(2)
      adj(u).append((v, w))
      adj(v).append((u, w))
    }

    val parent = Array.ofDim[Int](LOG, n)
    for (k <- 0 until LOG) java.util.Arrays.fill(parent(k), -1)
    val depth = new Array[Int](n)
    val freq = Array.ofDim[Int](n, 27) // weights are 1..26

    // iterative DFS to fill parent[0], depth and freq
    val stack = scala.collection.mutable.Stack[(Int, Int)]()
    stack.push((0, -1))
    while (stack.nonEmpty) {
      val (u, p) = stack.pop()
      parent(0)(u) = p
      if (p != -1) depth(u) = depth(p) + 1
      for ((v, w) <- adj(u)) {
        if (v != p) {
          // copy freq from u to v
          System.arraycopy(freq(u), 0, freq(v), 0, 27)
          freq(v)(w) += 1
          stack.push((v, u))
        }
      }
    }

    // binary lifting table
    for (k <- 1 until LOG) {
      for (v <- 0 until n) {
        val mid = parent(k - 1)(v)
        if (mid != -1) parent(k)(v) = parent(k - 1)(mid)
      }
    }

    def lca(u0: Int, v0: Int): Int = {
      var u = u0
      var v = v0
      if (depth(u) < depth(v)) {
        val tmp = u; u = v; v = tmp
      }
      // lift u up to depth of v
      var diff = depth(u) - depth(v)
      var k = 0
      while (diff > 0) {
        if ((diff & 1) == 1) u = parent(k)(u)
        diff >>= 1
        k += 1
      }
      if (u == v) return u
      for (i <- LOG - 1 to 0 by -1) {
        val pu = parent(i)(u)
        val pv = parent(i)(v)
        if (pu != -1 && pu != pv) {
          u = pu
          v = pv
        }
      }
      parent(0)(u)
    }

    val ans = new Array[Int](queries.length)
    for (idx <- queries.indices) {
      val a = queries(idx)(0)
      val b = queries(idx)(1)
      if (a == b) {
        ans(idx) = 0
      } else {
        val anc = lca(a, b)
        val pathLen = depth(a) + depth(b) - 2 * depth(anc)
        var maxCnt = 0
        var w = 1
        while (w <= 26) {
          val cnt = freq(a)(w) + freq(b)(w) - 2 * freq(anc)(w)
          if (cnt > maxCnt) maxCnt = cnt
          w += 1
        }
        ans(idx) = pathLen - maxCnt
      }
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations_queries(n: i32, edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<(usize, u8)>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as u8;
            adj[u].push((v, w));
            adj[v].push((u, w));
        }

        // compute log size
        let mut max_log = 0usize;
        while (1usize << max_log) <= n_usize {
            max_log += 1;
        }
        let LOG = max_log;

        let mut parent: Vec<Vec<usize>> = vec![vec![0; n_usize]; LOG];
        let mut depth: Vec<usize> = vec![0; n_usize];
        let mut freq: Vec<[i32; 27]> = vec![[0; 27]; n_usize];

        // DFS stack
        let root = 0usize;
        let mut stack: Vec<(usize, usize, u8)> = Vec::new();
        stack.push((root, root, 0));
        while let Some((node, par, w)) = stack.pop() {
            if node == par {
                depth[node] = 0;
            } else {
                depth[node] = depth[par] + 1;
            }
            parent[0][node] = par;
            freq[node] = freq[par];
            if node != root {
                let wi = w as usize;
                freq[node][wi] += 1;
            }
            for &(nei, wt) in &adj[node] {
                if nei == par {
                    continue;
                }
                stack.push((nei, node, wt));
            }
        }

        // binary lifting
        for k in 1..LOG {
            for v in 0..n_usize {
                let mid = parent[k - 1][v];
                parent[k][v] = parent[k - 1][mid];
            }
        }

        // LCA closure
        let lca = |mut u: usize, mut v: usize,
                   depth: &Vec<usize>,
                   parent: &Vec<Vec<usize>>| -> usize {
            if depth[u] < depth[v] {
                std::mem::swap(&mut u, &mut v);
            }
            let diff = depth[u] - depth[v];
            for k in 0..LOG {
                if (diff >> k) & 1 == 1 {
                    u = parent[k][u];
                }
            }
            if u == v {
                return u;
            }
            for k in (0..LOG).rev() {
                if parent[k][u] != parent[k][v] {
                    u = parent[k][u];
                    v = parent[k][v];
                }
            }
            parent[0][u]
        };

        let mut ans: Vec<i32> = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let a = q[0] as usize;
            let b = q[1] as usize;
            let l = lca(a, b, &depth, &parent);
            let path_len = depth[a] + depth[b] - 2 * depth[l];
            let mut max_cnt: i32 = 0;
            for w in 1..=26 {
                let cnt = freq[a][w] + freq[b][w] - 2 * freq[l][w];
                if cnt > max_cnt {
                    max_cnt = cnt;
                }
            }
            ans.push(path_len as i32 - max_cnt);
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-operations-queries n edges queries)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ((LOG
          (let loop ((k 0) (v 1))
            (if (>= v n) k (loop (+ k 1) (* v 2)))))
         (adj (make-vector n '()))
         ;; build adjacency list
         )
    ;; add edges to adjacency
    (for ([e edges])
      (define u (list-ref e 0))
      (define v (list-ref e 1))
      (define w (list-ref e 2))
      (vector-set! adj u (cons (list v w) (vector-ref adj u)))
      (vector-set! adj v (cons (list u w) (vector-ref adj v))))
    ;; vectors for parent, depth, cumulative frequencies
    (define parent0 (make-vector n -1))
    (define depth   (make-vector n 0))
    (define freqVec (make-vector n #f)) ; each entry will be a vector of size 27
    ;; DFS to fill parent, depth and freq
    (letrec ((dfs
              (lambda (u p w)
                (vector-set! parent0 u p)
                (if (= p -1)
                    (begin
                      (vector-set! depth u 0)
                      (define f (make-vector 27 0))
                      (vector-set! freqVec u f))
                    (begin
                      (vector-set! depth u (+ (vector-ref depth p) 1))
                      (define pf (vector-ref freqVec p))
                      (define f (make-vector 27 0))
                      (for ([i (in-range 27)])
                        (vector-set! f i (vector-ref pf i)))
                      (when (> w 0)
                        (vector-set! f w (+ (vector-ref f w) 1)))
                      (vector-set! freqVec u f)))
                (for ([nbr (in-list (vector-ref adj u))])
                  (define v (first nbr))
                  (define wt (second nbr))
                  (when (not (= v p))
                    (dfs v u wt))))))
      (dfs 0 -1 0))
    ;; binary lifting table
    (define up (make-vector LOG #f))
    (vector-set! up 0 (make-vector n -1))
    (for ([i (in-range n)])
      (vector-set! (vector-ref up 0) i (vector-ref parent0 i)))
    (let loop ((k 1))
      (when (< k LOG)
        (define prev (vector-ref up (- k 1)))
        (define cur (make-vector n -1))
        (for ([i (in-range n)])
          (define mid (vector-ref prev i))
          (if (= mid -1)
              (vector-set! cur i -1)
              (vector-set! cur i (vector-ref prev mid))))
        (vector-set! up k cur)
        (loop (+ k 1))))
    ;; lca function
    (define (lca u v)
      (let* ((du (vector-ref depth u))
             (dv (vector-ref depth v))
             (a u) (b v) (da du) (db dv))
        (when (< da db)
          (let ((tmp a)) (set! a b) (set! b tmp))
          (let ((tmp da)) (set! da db) (set! db tmp)))
        ;; lift a to depth of b
        (define diff (- da db))
        (for ([k (in-range LOG)])
          (when (not (= (bitwise-and diff (arithmetic-shift 1 k)) 0))
            (set! a (vector-ref (vector-ref up k) a))))
        (if (= a b)
            a
            (begin
              (for ([k (in-list (reverse (range LOG)))])
                (define ancA (vector-ref (vector-ref up k) a))
                (define ancB (vector-ref (vector-ref up k) b))
                (when (and (not (= ancA -1)) (not (= ancB -1)) (not (= ancA ancB)))
                  (set! a ancA)
                  (set! b ancB)))
              (vector-ref (vector-ref up 0) a)))))
    ;; answer each query
    (for/list ([qr queries])
      (let* ((a (list-ref qr 0))
             (b (list-ref qr 1))
             (l (lca a b))
             (path-len (- (+ (vector-ref depth a) (vector-ref depth b))
                          (* 2 (vector-ref depth l))))
             (freqA (vector-ref freqVec a))
             (freqB (vector-ref freqVec b))
             (freqL (vector-ref freqVec l))
             (maxc
              (let loop ((w 1) (best 0))
                (if (> w 26)
                    best
                    (let ((cnt (+ (vector-ref freqA w)
                                  (vector-ref freqB w)
                                  (- (* 2 (vector-ref freqL w))))))
                      (loop (+ w 1) (if (> cnt best) cnt best)))))))
        (- path-len maxc)))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations_queries/3]).

-define(LOG_MAX, 15).   % enough for n <= 10^4

min_operations_queries(N, Edges, Queries) ->
    Adj = build_adj(Edges, #{}),
    Root = 0,
    {DepthMap, ParentMap, FreqMap} = bfs([{Root, -1}], Adj,
                                         #{Root => 0},
                                         #{Root => -1},
                                         #{Root => zero_freq()}),

    UpMaps = build_up_maps(?LOG_MAX, ParentMap),

    lists:map(fun([A,B]) ->
        L = lca(A, B, DepthMap, ParentMap, UpMaps),
        LenPath = maps:get(A, DepthMap) + maps:get(B, DepthMap) - 2 * maps:get(L, DepthMap),
        Fa = maps:get(A, FreqMap),
        Fb = maps:get(B, FreqMap),
        Fl = maps:get(L, FreqMap),
        MaxCnt = max_weight_count(Fa, Fb, Fl, 1, 0),
        LenPath - MaxCnt
    end, Queries).

%% Build adjacency map: Node -> [{Neighbor,Weight},...]
build_adj([], Adj) -> Adj;
build_adj([[U,V,W]|Rest], Adj) ->
    Adj1 = maps:update_with(U,
            fun(L) -> [{V,W}|L] end,
            [{V,W}], Adj),
    Adj2 = maps:update_with(V,
            fun(L) -> [{U,W}|L] end,
            [{U,W}], Adj1),
    build_adj(Rest, Adj2).

%% BFS to compute depth, parent and frequency tuples
bfs([], _Adj, DepthMap, ParentMap, FreqMap) ->
    {DepthMap, ParentMap, FreqMap};
bfs([{Node,Par}|Queue], Adj, DepthMap, ParentMap, FreqMap) ->
    Neigh = maps:get(Node, Adj, []),
    {NewDepthMap, NewParentMap, NewFreqMap, AddQueue} =
        lists:foldl(fun({Nei,W}, {DM,PM,FM,Q}) ->
            if Nei =/= Par ->
                DChild = maps:get(Node, DM) + 1,
                DM2 = maps:put(Nei, DChild, DM),
                PM2 = maps:put(Nei, Node, PM),
                PF = maps:get(Node, FM),
                PrevCnt = element(W+1, PF),
                NewFreq = set_elem(PF, W+1, PrevCnt + 1),
                FM2 = maps:put(Nei, NewFreq, FM),
                {DM2, PM2, FM2, [{Nei, Node}|Q]};
               true ->
                {DM, PM, FM, Q}
            end
        end, {DepthMap, ParentMap, FreqMap, []}, Neigh),
    bfs(Queue ++ AddQueue, Adj, NewDepthMap, NewParentMap, NewFreqMap).

zero_freq() -> erlang:make_tuple(27, 0).

%% Build binary lifting tables up to LOG_MAX levels
build_up_maps(Log, ParentMap) ->
    build_up_maps(1, Log, ParentMap, [ParentMap]).

build_up_maps(K, Log, PrevUp, Acc) when K < Log ->
    NextUp = maps:fold(fun(Node,_Val, M) ->
                Anc = maps:get(Node, PrevUp),
                NewAnc = if Anc == -1 -> -1; true -> maps:get(Anc, PrevUp) end,
                maps:put(Node, NewAnc, M)
            end, #{}, PrevUp),
    build_up_maps(K+1, Log, NextUp, [NextUp|Acc]);
build_up_maps(_K, _Log, _PrevUp, Acc) ->
    lists:reverse(Acc).

%% LCA using binary lifting
lca(A, B, DepthMap, ParentMap, UpMaps) ->
    {U,V} = if maps:get(A, DepthMap) < maps:get(B, DepthMap) -> {B,A}; true -> {A,B} end,
    Diff = abs(maps:get(U, DepthMap) - maps:get(V, DepthMap)),
    U1 = lift_node(U, Diff, UpMaps),
    V1 = V,
    if U1 == V1 ->
        U1;
       true ->
        lca_equal_depth(U1, V1, ParentMap, UpMaps)
    end.

lift_node(Node, 0, _UpMaps) -> Node;
lift_node(Node, Diff, UpMaps) ->
    lift_node(Node, Diff, UpMaps, 0).

lift_node(Node, Diff, UpMaps, K) when K < ?LOG_MAX ->
    case (Diff band (1 bsl K)) of
        0 -> lift_node(Node, Diff, UpMaps, K+1);
        _ ->
            AncMap = lists:nth(K+1, UpMaps),
            NewNode = maps:get(Node, AncMap, -1),
            lift_node(NewNode, Diff, UpMaps, K+1)
    end;
lift_node(Node, _Diff, _UpMaps, _K) -> Node.

lca_equal_depth(U, V, ParentMap, UpMaps) ->
    lca_descend(U, V, ?LOG_MAX-1, ParentMap, UpMaps).

lca_descend(U, V, -1, ParentMap, _UpMaps) ->
    maps:get(U, ParentMap);
lca_descend(U, V, K, ParentMap, UpMaps) when K >= 0 ->
    AncU = get_up(U, K, UpMaps),
    AncV = get_up(V, K, UpMaps),
    if AncU =/= -1 andalso AncU =/= AncV ->
            lca_descend(AncU, AncV, K-1, ParentMap, UpMaps);
       true ->
            lca_descend(U, V, K-1, ParentMap, UpMaps)
    end.

get_up(Node, K, UpMaps) ->
    maps:get(Node, lists:nth(K+1, UpMaps), -1).

%% Compute maximum frequency of any weight on the path
max_weight_count(_Fa,_Fb,_Fl,27, Max) -> Max;
max_weight_count(Fa,Fb,Fl,W, Max) ->
    C = element(W+1, Fa) + element(W+1, Fb) - 2*element(W+1, Fl),
    NewMax = if C > Max -> C; true -> Max end,
    max_weight_count(Fa,Fb,Fl,W+1, NewMax).

%% Helper to set tuple element
set_elem(Tuple, Index, Value) ->
    erlang:setelement(Index, Tuple, Value).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec min_operations_queries(n :: integer, edges :: [[integer]], queries :: [[integer]]) :: [integer]
  def min_operations_queries(n, edges, queries) do
    # Build adjacency list
    adj =
      Enum.reduce(edges, %{}, fn [u, v, w], acc ->
        acc
        |> Map.update(u, [{v, w}], fn lst -> [{v, w} | lst] end)
        |> Map.update(v, [{u, w}], fn lst -> [{u, w} | lst] end)
      end)

    root = 0
    log = ceil_log2(n) + 1

    depth_arr = :array.new(n, default: 0) |> :array.set(0, 0)
    parent0_arr = :array.new(n, default: -1) |> :array.set(0, -1)
    cum_arr = :array.new(n, default: List.duplicate(0, 27)) |> :array.set(0, List.duplicate(0, 27))

    {depth_arr, parent0_arr, cum_arr} =
      dfs([{root, -1}], adj, depth_arr, parent0_arr, cum_arr)

    anc = build_ancestors(parent0_arr, n, log)

    Enum.map(queries, fn [a, b] ->
      l = lca(a, b, depth_arr, anc, log)
      da = :array.get(a, depth_arr)
      db = :array.get(b, depth_arr)
      dl = :array.get(l, depth_arr)
      path_len = da + db - 2 * dl

      cnt_a = :array.get(a, cum_arr)
      cnt_b = :array.get(b, cum_arr)
      cnt_l = :array.get(l, cum_arr)

      max_freq =
        Enum.reduce(1..26, 0, fn w, acc ->
          freq = Enum.at(cnt_a, w) + Enum.at(cnt_b, w) - 2 * Enum.at(cnt_l, w)
          if freq > acc, do: freq, else: acc
        end)

      path_len - max_freq
    end)
  end

  defp dfs([], _adj, depth_arr, parent0_arr, cum_arr), do: {depth_arr, parent0_arr, cum_arr}

  defp dfs([{node, par} | rest], adj, depth_arr, parent0_arr, cum_arr) do
    cnt_node = :array.get(node, cum_arr)

    {new_depth_arr, new_parent0_arr, new_cum_arr, new_stack} =
      Enum.reduce(Map.get(adj, node, []), {depth_arr, parent0_arr, cum_arr, rest}, fn
        {nbr, w}, {darr, p0arr, carr, stk} ->
          if nbr == par do
            {darr, p0arr, carr, stk}
          else
            depth_n = :array.get(node, darr) + 1
            d_arr = :array.set(nbr, depth_n, darr)
            p0_arr = :array.set(nbr, node, p0arr)
            cnt_child = List.update_at(cnt_node, w, &(&1 + 1))
            c_arr = :array.set(nbr, cnt_child, carr)
            {d_arr, p0_arr, c_arr, [{nbr, node} | stk]}
          end
      end)

    dfs(new_stack, adj, new_depth_arr, new_parent0_arr, new_cum_arr)
  end

  defp ceil_log2(x) do
    :math.log2(x) |> Float.ceil() |> trunc()
  end

  defp build_ancestors(parent0_arr, n, log) do
    anc = [parent0_arr]

    Enum.reduce(1..log - 1, anc, fn _k, acc ->
      prev = List.last(acc)

      cur =
        Enum.reduce(0..n - 1, :array.new(n, default: -1), fn node, arr ->
          p = :array.get(node, prev)

          pp =
            if p != -1 do
              :array.get(p, prev)
            else
              -1
            end

          :array.set(node, pp, arr)
        end)

      acc ++ [cur]
    end)
  end

  defp lca(a, b, depth_arr, anc, log) do
    da = :array.get(a, depth_arr)
    db = :array.get(b, depth_arr)

    {a, b, da, db} =
      if da < db do
        {b, a, db, da}
      else
        {a, b, da, db}
      end

    diff = da - db
    a = lift_node(a, diff, anc, log)

    if a == b do
      a
    else
      {a_final, _} =
        Enum.reduce((log - 1)..0, {a, b}, fn i, {x, y} ->
          ax = :array.get(x, Enum.at(anc, i))
          by = :array.get(y, Enum.at(anc, i))

          if ax != -1 and ax != by do
            {ax, by}
          else
            {x, y}
          end
        end)

      :array.get(a_final, Enum.at(anc, 0))
    end
  end

  defp lift_node(node, diff, anc, log) do
    Enum.reduce(0..log - 1, node, fn i, cur ->
      if (diff &&& (1 <<< i)) != 0 do
        :array.get(cur, Enum.at(anc, i))
      else
        cur
      end
    end)
  end
end
```

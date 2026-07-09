# 3585. Find Weighted Median Node in Tree

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findMedian(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        const int LOG = 17 + 1; // since 2^17 > 1e5
        vector<vector<pair<int,long long>>> adj(n);
        for (auto &e: edges) {
            int u=e[0], v=e[1];
            long long w=e[2];
            adj[u].push_back({v,w});
            adj[v].push_back({u,w});
        }
        vector<int> depth(n,0), parent(LOG*n,-1);
        vector<long long> distRoot(n,0);
        vector<vector<int>> up(LOG, vector<int>(n, -1));
        vector<vector<long long>> wup(LOG, vector<long long>(n, 0));

        // BFS/DFS from root 0
        stack<int> st;
        st.push(0);
        vector<int> order;
        vector<int> visited(n,0);
        visited[0]=1;
        while(!st.empty()){
            int u=st.top(); st.pop();
            order.push_back(u);
            for(auto &pr: adj[u]){
                int v=pr.first; long long w=pr.second;
                if(!visited[v]){
                    visited[v]=1;
                    depth[v]=depth[u]+1;
                    up[0][v]=u;
                    wup[0][v]=w;
                    distRoot[v]=distRoot[u]+w;
                    st.push(v);
                }
            }
        }
        // binary lifting tables
        for(int k=1;k<LOG;++k){
            for(int v=0;v<n;++v){
                int mid = up[k-1][v];
                if(mid!=-1){
                    up[k][v]=up[k-1][mid];
                    wup[k][v]=wup[k-1][v]+wup[k-1][mid];
                }
            }
        }

        auto lca = [&](int a,int b)->int{
            if(depth[a]<depth[b]) swap(a,b);
            int diff=depth[a]-depth[b];
            for(int k=LOG-1;k>=0;--k){
                if(diff&(1<<k)) a=up[k][a];
            }
            if(a==b) return a;
            for(int k=LOG-1;k>=0;--k){
                if(up[k][a]!=-1 && up[k][a]!=up[k][b]){
                    a=up[k][a];
                    b=up[k][b];
                }
            }
            return up[0][a];
        };

        vector<int> ans;
        ans.reserve(queries.size());
        for(auto &qr: queries){
            int u=qr[0], v=qr[1];
            int l=lca(u,v);
            long long total = distRoot[u]+distRoot[v]-2*distRoot[l];
            long long need = (total+1)/2; // ceil(total/2)

            // try upward from u towards l
            int cur=u;
            long long cum=0;
            int steps = depth[u]-depth[l];
            for(int k=LOG-1;k>=0;--k){
                if((1<<k) <= steps && cum + wup[k][cur] < need){
                    cum += wup[k][cur];
                    cur = up[k][cur];
                    steps -= (1<<k);
                }
            }
            // check next edge upward if possible
            if(steps>0 && cum + wup[0][cur] >= need){
                ans.push_back(up[0][cur]);
                continue;
            }

            // median lies on the down path from l to v
            long long remain = need - cum; // >0
            long long targetDist = distRoot[l] + remain;
            cur=v;
            for(int k=LOG-1;k>=0;--k){
                int anc = up[k][cur];
                if(anc!=-1 && distRoot[anc] >= targetDist){
                    cur = anc;
                }
            }
            ans.push_back(cur);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] findMedian(int n, int[][] edges, int[][] queries) {
        // Build adjacency list
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        // Determine log size
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;

        int[][] upParent = new int[LOG][n];
        long[][] upWeight = new long[LOG][n];
        int[] depth = new int[n];
        long[] distRoot = new long[n];

        // BFS to set parent, depth, distance
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(0);
        Arrays.fill(upParent[0], -1);
        depth[0] = 0;
        distRoot[0] = 0;

        while (!dq.isEmpty()) {
            int u = dq.poll();
            for (int[] e : graph[u]) {
                int v = e[0];
                int w = e[1];
                if (v == upParent[0][u]) continue;
                upParent[0][v] = u;
                upWeight[0][v] = w;
                depth[v] = depth[u] + 1;
                distRoot[v] = distRoot[u] + w;
                dq.add(v);
            }
        }

        // Build binary lifting tables
        for (int k = 1; k < LOG; k++) {
            for (int v = 0; v < n; v++) {
                int mid = upParent[k - 1][v];
                if (mid != -1) {
                    upParent[k][v] = upParent[k - 1][mid];
                    upWeight[k][v] = upWeight[k - 1][v] + upWeight[k - 1][mid];
                } else {
                    upParent[k][v] = -1;
                    upWeight[k][v] = upWeight[k - 1][v];
                }
            }
        }

        // Helper lambdas
        java.util.function.BiFunction<Integer, Integer, Integer> lcaFunc = (a0, b0) -> {
            int a = a0, b = b0;
            if (depth[a] < depth[b]) { int tmp = a; a = b; b = tmp; }
            int diff = depth[a] - depth[b];
            for (int k = LOG - 1; k >= 0; k--) {
                if (((diff >> k) & 1) == 1) {
                    a = upParent[k][a];
                }
            }
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; k--) {
                if (upParent[k][a] != -1 && upParent[k][a] != upParent[k][b]) {
                    a = upParent[k][a];
                    b = upParent[k][b];
                }
            }
            return upParent[0][a];
        };

        java.util.function.BiFunction<Integer, Long, Integer> climbByWeight = (nodeStart, weight) -> {
            int node = nodeStart;
            long remain = weight;
            for (int k = LOG - 1; k >= 0; k--) {
                if (upParent[k][node] != -1 && upWeight[k][node] <= remain) {
                    remain -= upWeight[k][node];
                    node = upParent[k][node];
                }
            }
            return node;
        };

        java.util.function.BiFunction<Integer, Long, Integer> findOnPathUp = (uStart, target) -> {
            int node = uStart;
            long sum = 0;
            for (int k = LOG - 1; k >= 0; k--) {
                int anc = upParent[k][node];
                if (anc != -1 && sum + upWeight[k][node] < target) {
                    sum += upWeight[k][node];
                    node = anc;
                }
            }
            return upParent[0][node];
        };

        int q = queries.length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            int l = lcaFunc.apply(u, v);
            long sumUtoL = distRoot[u] - distRoot[l];
            long sumVtoL = distRoot[v] - distRoot[l];
            long total = sumUtoL + sumVtoL;
            long target = (total + 1) / 2; // ceil(total/2)

            if (sumUtoL >= target) {
                ans[i] = findOnPathUp.apply(u, target);
            } else {
                long need = target - sumUtoL;
                long moveUpWeight = sumVtoL - need;
                ans[i] = climbByWeight.apply(v, moveUpWeight);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findMedian(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(1 << 25)
        LOG = (n).bit_length() + 1

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        up = [[-1] * n for _ in range(LOG)]
        wup = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        distRoot = [0] * n

        # iterative DFS to fill level 0 tables
        stack = [(0, -1, 0)]  # node, parent, weight from parent
        while stack:
            node, par, wpar = stack.pop()
            up[0][node] = par
            wup[0][node] = wpar
            if par != -1:
                depth[node] = depth[par] + 1
                distRoot[node] = distRoot[par] + wpar
            for nb, w in adj[node]:
                if nb == par:
                    continue
                stack.append((nb, node, w))

        # build binary lifting tables
        for k in range(1, LOG):
            upk = up[k]
            upkm1 = up[k - 1]
            wupk = wup[k]
            wupkm1 = wup[k - 1]
            for v in range(n):
                anc = upkm1[v]
                if anc != -1:
                    upk[v] = upkm1[anc]
                    wupk[v] = wupkm1[v] + wupkm1[anc]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != -1 and up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        def climb(node, need):
            """move up from node until accumulated weight >= need,
               return the first node where this holds."""
            if need <= 0:
                return node
            cur = node
            acc = 0
            for k in range(LOG - 1, -1, -1):
                anc = up[k][cur]
                if anc != -1 and acc + wup[k][cur] < need:
                    acc += wup[k][cur]
                    cur = anc
            # one more step reaches or exceeds need
            return up[0][cur]

        def node_at_distance(u, v, dist):
            """return node that is exactly 'dist' weight away from u towards v"""
            l = lca(u, v)
            du = distRoot[u] - distRoot[l]
            if dist <= du:
                return climb(u, dist)
            total = distRoot[u] + distRoot[v] - 2 * distRoot[l]
            # remaining distance after reaching LCA
            up_needed = total - dist  # weight to go up from v to target
            return climb(v, up_needed)

        ans = []
        for u, v in queries:
            l = lca(u, v)
            total = distRoot[u] + distRoot[v] - 2 * distRoot[l]
            need = (total + 1) // 2  # ceil(total/2)
            median_node = node_at_distance(u, v, need)
            ans.append(median_node)
        return ans
```

## Python3

```python
import sys
sys.setrecursionlimit(1 << 25)
from typing import List

class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        LOG = (n).bit_length()
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [[-1] * n for _ in range(LOG)]
        wsum = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        distRoot = [0] * n

        # DFS to set level 0 ancestors
        stack = [(0, -1, 0, 0)]  # node, par, d, dist
        while stack:
            node, par, d, dist = stack.pop()
            parent[0][node] = par
            depth[node] = d
            distRoot[node] = dist
            for nb, w in adj[node]:
                if nb == par:
                    continue
                stack.append((nb, node, d + 1, dist + w))

        # binary lifting tables
        for k in range(1, LOG):
            pu = parent[k - 1]
            pp = parent[k]
            ws_prev = wsum[k - 1]
            ws_cur = wsum[k]
            for v in range(n):
                mid = pu[v]
                if mid != -1:
                    pp[v] = pu[mid]
                    ws_cur[v] = ws_prev[v] + ws_prev[mid]

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
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        def dist(u: int, v: int) -> int:
            l = lca(u, v)
            return distRoot[u] + distRoot[v] - 2 * distRoot[l]

        ans = []
        for u, v in queries:
            l = lca(u, v)
            total = distRoot[u] + distRoot[v] - 2 * distRoot[l]
            half = (total + 1) // 2
            du = distRoot[u] - distRoot[l]

            if half <= du:
                cur = u
                cur_sum = 0
                for k in range(LOG - 1, -1, -1):
                    nxt = parent[k][cur]
                    if nxt != -1 and cur_sum + wsum[k][cur] < half:
                        cur_sum += wsum[k][cur]
                        cur = nxt
                ans.append(parent[0][cur])
            else:
                max_from_v = total - half  # floor(total/2)
                cur = v
                cur_sum = 0
                for k in range(LOG - 1, -1, -1):
                    nxt = parent[k][cur]
                    if nxt != -1 and cur_sum + wsum[k][cur] <= max_from_v:
                        cur_sum += wsum[k][cur]
                        cur = nxt
                ans.append(cur)

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct Edge {
    int to;
    int next;
    long long w;
} Edge;

int maxLogGlobal;

/* LCA and binary lifting structures */
static int **up;          // up[k][v] = 2^k-th ancestor of v
static long long **ws;   // ws[k][v] = sum of weights on that jump
static int *depthArr;
static long long *distArr;

int lca(int u, int v) {
    if (depthArr[u] < depthArr[v]) {
        int tmp = u; u = v; v = tmp;
    }
    int diff = depthArr[u] - depthArr[v];
    for (int k = maxLogGlobal - 1; k >= 0; --k) {
        if ((diff >> k) & 1) {
            u = up[k][u];
        }
    }
    if (u == v) return u;
    for (int k = maxLogGlobal - 1; k >= 0; --k) {
        if (up[k][u] != -1 && up[k][u] != up[k][v]) {
            u = up[k][u];
            v = up[k][v];
        }
    }
    return up[0][u];
}

/* Find first node from start towards ancestor where cumulative sum >= target */
int climb_until(int start, long long target) {
    long long cum = 0;
    int cur = start;
    for (int k = maxLogGlobal - 1; k >= 0; --k) {
        if (up[k][cur] != -1 && cum + ws[k][cur] < target) {
            cum += ws[k][cur];
            cur = up[k][cur];
        }
    }
    return up[0][cur]; // next node reaches or exceeds target
}

/* Main function */
int* findMedian(int n, int** edges, int edgesSize, int* edgesColSize,
                int** queries, int queriesSize, int* queriesColSize,
                int* returnSize) {
    /* Build adjacency list */
    int m = (n - 1) * 2;
    Edge *elist = (Edge *)malloc(sizeof(Edge) * m);
    int *head = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) head[i] = -1;
    int eidx = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        long long w = (long long)edges[i][2];
        elist[eidx].to = v;
        elist[eidx].w = w;
        elist[eidx].next = head[u];
        head[u] = eidx++;
        elist[eidx].to = u;
        elist[eidx].w = w;
        elist[eidx].next = head[v];
        head[v] = eidx++;
    }

    /* Determine maxLog */
    maxLogGlobal = 0;
    while ((1 << maxLogGlobal) <= n) ++maxLogGlobal;

    up = (int **)malloc(sizeof(int *) * maxLogGlobal);
    ws = (long long **)malloc(sizeof(long long *) * maxLogGlobal);
    for (int k = 0; k < maxLogGlobal; ++k) {
        up[k] = (int *)malloc(sizeof(int) * n);
        ws[k] = (long long *)malloc(sizeof(long long) * n);
    }

    depthArr = (int *)malloc(sizeof(int) * n);
    distArr = (long long *)malloc(sizeof(long long) * n);

    /* DFS/BFS to set level 0 ancestors */
    for (int i = 0; i < n; ++i) {
        up[0][i] = -1;
        ws[0][i] = 0;
    }
    int *stack = (int *)malloc(sizeof(int) * n);
    int top = 0;
    stack[top++] = 0;
    depthArr[0] = 0;
    distArr[0] = 0;
    up[0][0] = -1;
    ws[0][0] = 0;

    while (top) {
        int u = stack[--top];
        for (int e = head[u]; e != -1; e = elist[e].next) {
            int v = elist[e].to;
            if (v == up[0][u]) continue;
            up[0][v] = u;
            ws[0][v] = elist[e].w;
            depthArr[v] = depthArr[u] + 1;
            distArr[v] = distArr[u] + elist[e].w;
            stack[top++] = v;
        }
    }

    /* Build binary lifting tables */
    for (int k = 1; k < maxLogGlobal; ++k) {
        for (int i = 0; i < n; ++i) {
            int mid = up[k - 1][i];
            if (mid != -1) {
                up[k][i] = up[k - 1][mid];
                ws[k][i] = ws[k - 1][i] + ws[k - 1][mid];
            } else {
                up[k][i] = -1;
                ws[k][i] = ws[k - 1][i];
            }
        }
    }

    /* Process queries */
    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        int u = queries[i][0];
        int v = queries[i][1];
        if (u == v) {
            ans[i] = u;
            continue;
        }
        int l = lca(u, v);
        long long total = distArr[u] + distArr[v] - 2LL * distArr[l];
        long long need = (total + 1) / 2;               // ceil(total/2)
        long long upDistU = distArr[u] - distArr[l];    // distance from u up to l

        if (need <= upDistU) {
            ans[i] = climb_until(u, need);
        } else {
            long long remaining = need - upDistU;               // needed downwards from l
            long long downDistV = distArr[v] - distArr[l];
            long long upNeeded = downDistV - remaining;         // distance to move up from v
            if (upNeeded == 0) {
                ans[i] = v;
            } else {
                ans[i] = climb_until(v, upNeeded);
            }
        }
    }

    *returnSize = queriesSize;

    /* Free temporary structures (optional in LeetCode environment) */
    free(elist);
    free(head);
    for (int k = 0; k < maxLogGlobal; ++k) {
        free(up[k]);
        free(ws[k]);
    }
    free(up);
    free(ws);
    free(depthArr);
    free(distArr);
    free(stack);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindMedian(int n, int[][] edges, int[][] queries) {
        // Build graph
        var graph = new List<(int to, long w)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, long)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            long w = e[2];
            graph[u].Add((v, w));
            graph[v].Add((u, w));
        }

        // Determine LOG
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;

        int[][] parent = new int[LOG][];
        long[][] upWeight = new long[LOG][];
        for (int k = 0; k < LOG; k++) {
            parent[k] = new int[n];
            upWeight[k] = new long[n];
            for (int i = 0; i < n; i++) parent[k][i] = -1;
        }

        int[] depth = new int[n];
        long[] distRoot = new long[n];
        for (int i = 0; i < n; i++) depth[i] = -1;

        // DFS/BFS to set depth, parent[0], upWeight[0], distRoot
        var stack = new Stack<int>();
        stack.Push(0);
        depth[0] = 0;
        parent[0][0] = -1;
        upWeight[0][0] = 0;
        while (stack.Count > 0) {
            int node = stack.Pop();
            foreach (var (to, w) in graph[node]) {
                if (depth[to] != -1) continue;
                depth[to] = depth[node] + 1;
                distRoot[to] = distRoot[node] + w;
                parent[0][to] = node;
                upWeight[0][to] = w;
                stack.Push(to);
            }
        }

        // Build binary lifting tables
        for (int k = 1; k < LOG; k++) {
            for (int v = 0; v < n; v++) {
                int mid = parent[k - 1][v];
                if (mid != -1) {
                    parent[k][v] = parent[k - 1][mid];
                    upWeight[k][v] = upWeight[k - 1][v] + upWeight[k - 1][mid];
                }
            }
        }

        // LCA function
        int LCA(int a, int b) {
            if (depth[a] < depth[b]) { int tmp = a; a = b; b = tmp; }
            int diff = depth[a] - depth[b];
            for (int k = 0; k < LOG; k++) {
                if (((diff >> k) & 1) == 1) a = parent[k][a];
            }
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; k--) {
                if (parent[k][a] != -1 && parent[k][a] != parent[k][b]) {
                    a = parent[k][a];
                    b = parent[k][b];
                }
            }
            return parent[0][a];
        }

        int q = queries.Length;
        int[] ans = new int[q];

        for (int i = 0; i < q; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            int l = LCA(u, v);
            long total = distRoot[u] + distRoot[v] - 2 * distRoot[l];
            long needed = (total + 1) / 2; // ceil(total/2)

            // Climb from u towards l while distance < needed
            int cur = u;
            long curDist = 0;
            for (int k = LOG - 1; k >= 0; k--) {
                int anc = parent[k][cur];
                if (anc != -1 && depth[anc] >= depth[l]) {
                    long ndist = curDist + upWeight[k][cur];
                    if (ndist < needed) {
                        curDist = ndist;
                        cur = anc;
                    }
                }
            }

            int medianNode;
            if (cur != l) {
                medianNode = parent[0][cur]; // one step closer to l
            } else {
                long limit = total - needed; // max distance we can stay away from v
                int cur2 = v;
                long cum = 0;
                for (int k = LOG - 1; k >= 0; k--) {
                    int anc = parent[k][cur2];
                    if (anc != -1 && depth[anc] >= depth[l]) {
                        long ndist = cum + upWeight[k][cur2];
                        if (ndist <= limit) {
                            cum = ndist;
                            cur2 = anc;
                        }
                    }
                }
                medianNode = cur2; // node reached after climbing from v within limit
            }

            ans[i] = medianNode;
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
var findMedian = function(n, edges, queries) {
    const LOG = Math.ceil(Math.log2(n)) + 1;
    const adj = Array.from({length: n}, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    const parent = Array.from({length: LOG}, () => new Int32Array(n).fill(-1));
    const upWeight = Array.from({length: LOG}, () => new Float64Array(n).fill(0));
    const depth = new Int32Array(n);
    const dist = new Float64Array(n);

    // iterative DFS from root 0
    const stack = [[0, -1, 0]];
    while (stack.length) {
        const [node, par, w] = stack.pop();
        if (par !== -1) {
            parent[0][node] = par;
            upWeight[0][node] = w;
            depth[node] = depth[par] + 1;
            dist[node] = dist[par] + w;
        }
        for (const [to, wt] of adj[node]) {
            if (to === par) continue;
            stack.push([to, node, wt]);
        }
    }

    // binary lifting tables
    for (let k = 1; k < LOG; ++k) {
        const pk = parent[k - 1];
        const ppk = parent[k];
        const wkPrev = upWeight[k - 1];
        const wk = upWeight[k];
        for (let i = 0; i < n; ++i) {
            const mid = pk[i];
            if (mid !== -1) {
                ppk[i] = pk[mid];
                wk[i] = wkPrev[i] + wkPrev[mid];
            } else {
                ppk[i] = -1;
                wk[i] = wkPrev[i];
            }
        }
    }

    const lca = (u, v) => {
        if (depth[u] < depth[v]) { let tmp = u; u = v; v = tmp; }
        let diff = depth[u] - depth[v];
        for (let k = LOG - 1; k >= 0; --k) {
            if ((diff >> k) & 1) {
                u = parent[k][u];
            }
        }
        if (u === v) return u;
        for (let k = LOG - 1; k >= 0; --k) {
            if (parent[k][u] !== -1 && parent[k][u] !== parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        }
        return parent[0][u];
    };

    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; ++qi) {
        let [u, v] = queries[qi];
        if (u === v) { ans[qi] = u; continue; }
        const l = lca(u, v);
        const totalDist = dist[u] + dist[v] - 2 * dist[l];
        const target = Math.floor((totalDist + 1) / 2); // ceil
        const duL = dist[u] - dist[l];
        const dvL = dist[v] - dist[l];

        if (target <= duL) {
            // climb from u upwards
            let cur = u;
            let acc = 0;
            for (let k = LOG - 1; k >= 0; --k) {
                const nxt = parent[k][cur];
                if (nxt !== -1 && acc + upWeight[k][cur] < target) {
                    acc += upWeight[k][cur];
                    cur = nxt;
                }
            }
            ans[qi] = parent[0][cur];
        } else {
            const rem = target - duL;          // distance needed after l
            const needUp = dvL - rem;           // max weight we can climb from v
            let cur = v;
            let acc = 0;
            for (let k = LOG - 1; k >= 0; --k) {
                const nxt = parent[k][cur];
                if (nxt !== -1 && acc + upWeight[k][cur] <= needUp) {
                    acc += upWeight[k][cur];
                    cur = nxt;
                }
            }
            ans[qi] = cur;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function findMedian(n: number, edges: number[][], queries: number[][]): number[] {
    const LOG = Math.ceil(Math.log2(n)) + 1;
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    const parent: Int32Array[] = Array.from({ length: LOG }, () => new Int32Array(n).fill(-1));
    const upWeight: Float64Array[] = Array.from({ length: LOG }, () => new Float64Array(n));
    const depth = new Int32Array(n);
    const distRoot = new Float64Array(n);

    // iterative DFS/BFS to set level 0 parents
    const stack: number[] = [0];
    parent[0][0] = -1;
    depth[0] = 0;
    distRoot[0] = 0;

    while (stack.length) {
        const node = stack.pop() as number;
        for (const [to, w] of adj[node]) {
            if (to === parent[0][node]) continue;
            parent[0][to] = node;
            upWeight[0][to] = w;
            depth[to] = depth[node] + 1;
            distRoot[to] = distRoot[node] + w;
            stack.push(to);
        }
    }

    // binary lifting tables
    for (let k = 1; k < LOG; ++k) {
        const pk = parent[k - 1];
        const pkPrev = parent[k];
        const wkPrev = upWeight[k - 1];
        const wk = upWeight[k];
        for (let i = 0; i < n; ++i) {
            const mid = pk[i];
            if (mid !== -1) {
                pkPrev[i] = pk[mid];
                wk[i] = wkPrev[i] + wkPrev[mid];
            } else {
                pkPrev[i] = -1;
                wk[i] = 0;
            }
        }
    }

    const lca = (u0: number, v0: number): number => {
        let u = u0, v = v0;
        if (depth[u] < depth[v]) {
            [u, v] = [v, u];
        }
        let diff = depth[u] - depth[v];
        for (let k = 0; diff > 0; ++k) {
            if ((diff & 1) !== 0) {
                u = parent[k][u];
            }
            diff >>= 1;
        }
        if (u === v) return u;
        for (let k = LOG - 1; k >= 0; --k) {
            if (parent[k][u] !== -1 && parent[k][u] !== parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        }
        return parent[0][u];
    };

    const res: number[] = [];

    for (const [uq, vq] of queries) {
        const l = lca(uq, vq);
        const duL = distRoot[uq] - distRoot[l];
        const dvL = distRoot[vq] - distRoot[l];
        const tot = duL + dvL;

        if (duL * 2 >= tot) {
            // median on upward path from u to l
            let cur = uq;
            let cum = 0;
            for (let k = LOG - 1; k >= 0; --k) {
                const anc = parent[k][cur];
                if (anc !== -1 && depth[anc] >= depth[l]) {
                    const w = upWeight[k][cur];
                    if ((cum + w) * 2 < tot) {
                        cum += w;
                        cur = anc;
                    }
                }
            }
            res.push(parent[0][cur]);
        } else {
            // median on downward path from l to v
            const needFromL = Math.ceil(tot / 2) - duL; // distance needed from l
            let cur = vq;
            for (let k = LOG - 1; k >= 0; --k) {
                const anc = parent[k][cur];
                if (anc !== -1 && depth[anc] >= depth[l]) {
                    const distAncToL = distRoot[anc] - distRoot[l];
                    if (distAncToL > needFromL) {
                        cur = anc;
                    }
                }
            }
            const distCurToL = distRoot[cur] - distRoot[l];
            if (distCurToL >= needFromL) {
                res.push(cur);
            } else {
                res.push(parent[0][cur]);
            }
        }
    }

    return res;
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
    function findMedian($n, $edges, $queries) {
        // build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $w] = $e;
            $adj[$u][] = [$v, $w];
            $adj[$v][] = [$u, $w];
        }

        // prepare arrays
        $depth = array_fill(0, $n, 0);
        $parent0 = array_fill(0, $n, -1);
        $distRoot = array_fill(0, $n, 0);
        $weightToParent = array_fill(0, $n, 0);

        // iterative DFS/BFS from root 0
        $stack = [0];
        $visited = array_fill(0, $n, false);
        $visited[0] = true;
        while (!empty($stack)) {
            $node = array_pop($stack);
            foreach ($adj[$node] as $edge) {
                [$to, $w] = $edge;
                if (!$visited[$to]) {
                    $visited[$to] = true;
                    $parent0[$to] = $node;
                    $weightToParent[$to] = $w;
                    $depth[$to] = $depth[$node] + 1;
                    $distRoot[$to] = $distRoot[$node] + $w;
                    $stack[] = $to;
                }
            }
        }

        // binary lifting size
        $LOG = 0;
        while ((1 << $LOG) <= $n) $LOG++;
        $up = array_fill(0, $LOG, []);
        $sumW = array_fill(0, $LOG, []);

        for ($k = 0; $k < $LOG; $k++) {
            $up[$k] = array_fill(0, $n, -1);
            $sumW[$k] = array_fill(0, $n, 0);
        }

        for ($v = 0; $v < $n; $v++) {
            $up[0][$v] = $parent0[$v];
            $sumW[0][$v] = $weightToParent[$v];
        }

        for ($k = 1; $k < $LOG; $k++) {
            for ($v = 0; $v < $n; $v++) {
                $mid = $up[$k - 1][$v];
                if ($mid != -1) {
                    $up[$k][$v] = $up[$k - 1][$mid];
                    $sumW[$k][$v] = $sumW[$k - 1][$v] + $sumW[$k - 1][$mid];
                } else {
                    $up[$k][$v] = -1;
                    $sumW[$k][$v] = $sumW[$k - 1][$v];
                }
            }
        }

        // LCA closure
        $lca = function($u, $v) use (&$depth, &$up, $LOG) {
            if ($depth[$u] < $depth[$v]) {
                $tmp = $u; $u = $v; $v = $tmp;
            }
            $diff = $depth[$u] - $depth[$v];
            for ($k = 0; $k < $LOG; $k++) {
                if (($diff >> $k) & 1) {
                    $u = $up[$k][$u];
                }
            }
            if ($u == $v) return $u;
            for ($k = $LOG - 1; $k >= 0; $k--) {
                if ($up[$k][$u] != -1 && $up[$k][$u] != $up[$k][$v]) {
                    $u = $up[$k][$u];
                    $v = $up[$k][$v];
                }
            }
            return $up[0][$u];
        };

        $ans = [];
        foreach ($queries as $q) {
            [$u, $v] = $q;
            $l = $lca($u, $v);
            $tot = $distRoot[$u] + $distRoot[$v] - 2 * $distRoot[$l];
            $need = intdiv($tot + 1, 2); // ceil(tot/2)

            // climb from u towards l while sum < need
            $cur = $u;
            $acc = 0;
            for ($k = $LOG - 1; $k >= 0; $k--) {
                $anc = $up[$k][$cur];
                if ($anc != -1 && $depth[$anc] >= $depth[$l]) {
                    $nextAcc = $acc + $sumW[$k][$cur];
                    if ($nextAcc < $need) {
                        $acc = $nextAcc;
                        $cur = $anc;
                    }
                }
            }

            if ($depth[$cur] > $depth[$l]) {
                // median is parent of cur
                $ans[] = $up[0][$cur];
                continue;
            }

            // now at l, still not reached need
            $sumUtoL = $acc; // equals distRoot[u] - distRoot[l]
            $rem = $need - $sumUtoL; // positive

            // climb from v towards l while distance from l >= rem
            $curV = $v;
            for ($k = $LOG - 1; $k >= 0; $k--) {
                $anc = $up[$k][$curV];
                if ($anc != -1 && $depth[$anc] >= $depth[$l]) {
                    $distFromLtoAnc = $distRoot[$anc] - $distRoot[$l];
                    if ($distFromLtoAnc >= $rem) {
                        $curV = $anc;
                    }
                }
            }
            $ans[] = $curV;
        }

        return $ans;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func findMedian(_ n: Int, _ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        var adj = [[(to: Int, w: Int64)]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1]
            let w = Int64(e[2])
            adj[u].append((v, w))
            adj[v].append((u, w))
        }
        
        // compute LOG
        var LOG = 1
        while (1 << LOG) <= n { LOG += 1 }
        
        var depth = [Int](repeating: 0, count: n)
        var dist = [Int64](repeating: 0, count: n)
        var up = [[Int]](repeating: [Int](repeating: -1, count: n), count: LOG)
        var upW = [[Int64]](repeating: [Int64](repeating: 0, count: n), count: LOG)
        
        // iterative DFS
        var stack: [(node: Int, parent: Int)] = [(0, -1)]
        while let (node, parent) = stack.popLast() {
            for edge in adj[node] {
                if edge.to == parent { continue }
                depth[edge.to] = depth[node] + 1
                dist[edge.to] = dist[node] + edge.w
                up[0][edge.to] = node
                upW[0][edge.to] = edge.w
                stack.append((edge.to, node))
            }
        }
        
        // binary lifting tables
        if LOG > 1 {
            for k in 1..<LOG {
                for v in 0..<n {
                    let mid = up[k-1][v]
                    if mid != -1 {
                        up[k][v] = up[k-1][mid]
                        upW[k][v] = upW[k-1][v] + upW[k-1][mid]
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
                    u = up[bit][u]
                }
                diff >>= 1
                bit += 1
            }
            if u == v { return u }
            for k in stride(from: LOG - 1, through: 0, by: -1) {
                if up[k][u] != -1 && up[k][u] != up[k][v] {
                    u = up[k][u]
                    v = up[k][v]
                }
            }
            return up[0][u]
        }
        
        var result = [Int]()
        result.reserveCapacity(queries.count)
        
        for q in queries {
            let u = q[0], v = q[1]
            let l = lca(u, v)
            let total = dist[u] + dist[v] - 2 * dist[l]
            let need = (total + 1) / 2   // ceil(total/2)
            let upDistUtoL = dist[u] - dist[l]
            
            if upDistUtoL >= need {
                var cur = u
                var cum: Int64 = 0
                for k in stride(from: LOG - 1, through: 0, by: -1) {
                    let anc = up[k][cur]
                    if anc != -1 && depth[anc] >= depth[l] {
                        let newCum = cum + upW[k][cur]
                        if newCum < need {
                            cur = anc
                            cum = newCum
                        }
                    }
                }
                let ansNode = up[0][cur]
                result.append(ansNode)
            } else {
                let remaining = need - upDistUtoL          // distance needed from l downwards
                let downDist = dist[v] - dist[l]
                let maxUp = downDist - remaining           // maximal allowed upward distance from v
                var cur = v
                var cum: Int64 = 0
                for k in stride(from: LOG - 1, through: 0, by: -1) {
                    let anc = up[k][cur]
                    if anc != -1 && depth[anc] >= depth[l] {
                        let newCum = cum + upW[k][cur]
                        if newCum <= maxUp {
                            cur = anc
                            cum = newCum
                        }
                    }
                }
                let ansNode: Int
                if cum == maxUp {
                    ansNode = cur
                } else {
                    ansNode = up[0][cur]
                }
                result.append(ansNode)
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import kotlin.math.max

class Solution {
    fun findMedian(n: Int, edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        // Build adjacency list
        val adj = Array(n) { mutableListOf<Pair<Int, Long>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2].toLong()
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        // Determine LOG
        var LOG = 1
        while ((1 shl LOG) <= n) LOG++

        val parent = Array(LOG) { IntArray(n) { -1 } }
        val upWeight = Array(LOG) { LongArray(n) }
        val depth = IntArray(n)
        val dist = LongArray(n)

        // DFS/BFS to set depth, parent[0], upWeight[0], dist
        val stack: ArrayDeque<Int> = ArrayDeque()
        stack.add(0)
        parent[0][0] = -1
        depth[0] = 0
        dist[0] = 0L

        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            for ((nei, w) in adj[node]) {
                if (nei == parent[0][node]) continue
                parent[0][nei] = node
                upWeight[0][nei] = w
                depth[nei] = depth[node] + 1
                dist[nei] = dist[node] + w
                stack.add(nei)
            }
        }

        // Binary lifting tables
        for (k in 1 until LOG) {
            for (v in 0 until n) {
                val mid = parent[k - 1][v]
                if (mid != -1) {
                    parent[k][v] = parent[k - 1][mid]
                    upWeight[k][v] = upWeight[k - 1][v] + upWeight[k - 1][mid]
                }
            }
        }

        fun lca(a0: Int, b0: Int): Int {
            var a = a0
            var b = b0
            if (depth[a] < depth[b]) {
                val tmp = a; a = b; b = tmp
            }
            var diff = depth[a] - depth[b]
            var bit = 0
            while (diff > 0) {
                if ((diff and 1) == 1) {
                    a = parent[bit][a]
                }
                diff = diff shr 1
                bit++
            }
            if (a == b) return a
            for (i in LOG - 1 downTo 0) {
                if (parent[i][a] != parent[i][b]) {
                    a = parent[i][a]
                    b = parent[i][b]
                }
            }
            return parent[0][a]
        }

        val q = queries.size
        val ans = IntArray(q)

        for (idx in 0 until q) {
            var u = queries[idx][0]
            var v = queries[idx][1]
            val l = lca(u, v)
            val total = dist[u] + dist[v] - 2L * dist[l]
            val target = (total + 1) / 2 // ceil(total/2)

            val upDist = dist[u] - dist[l]

            if (target <= upDist) {
                var cur = u
                var acc = 0L
                for (i in LOG - 1 downTo 0) {
                    val p = parent[i][cur]
                    if (p != -1 && acc + upWeight[i][cur] < target) {
                        acc += upWeight[i][cur]
                        cur = p
                    }
                }
                ans[idx] = parent[0][cur]
            } else {
                val remaining = target - upDist // >0
                val downDist = dist[v] - dist[l]
                val limit = downDist - remaining // non‑negative
                var cur = v
                var acc = 0L
                for (i in LOG - 1 downTo 0) {
                    val p = parent[i][cur]
                    if (p != -1 && acc + upWeight[i][cur] <= limit) {
                        acc += upWeight[i][cur]
                        cur = p
                    }
                }
                ans[idx] = cur
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> findMedian(int n, List<List<int>> edges, List<List<int>> queries) {
    // Build adjacency list
    final adj = List<List<_Edge>>.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1], w = e[2];
      adj[u].add(_Edge(v, w));
      adj[v].add(_Edge(u, w));
    }

    // Compute LOG
    int LOG = 1;
    while ((1 << LOG) <= n) LOG++;

    // Binary lifting tables
    final up = List<List<int>>.generate(LOG, (_) => List.filled(n, -1));
    final sumUp = List<List<int>>.generate(LOG, (_) => List.filled(n, 0));
    final depth = List.filled(n, 0);
    final dist = List.filled(n, 0);

    // DFS stack to fill level 0 tables
    final stack = <int>[];
    final parentStack = <int>[];
    stack.add(0);
    parentStack.add(-1);
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      int par = parentStack.removeLast();
      for (var e in adj[node]) {
        if (e.to == par) continue;
        depth[e.to] = depth[node] + 1;
        dist[e.to] = dist[node] + e.w;
        up[0][e.to] = node;
        sumUp[0][e.to] = e.w;
        stack.add(e.to);
        parentStack.add(node);
      }
    }

    // Build higher levels
    for (int k = 1; k < LOG; ++k) {
      for (int v = 0; v < n; ++v) {
        int mid = up[k - 1][v];
        if (mid != -1) {
          up[k][v] = up[k - 1][mid];
          sumUp[k][v] = sumUp[k - 1][v] + sumUp[k - 1][mid];
        }
      }
    }

    int lca(int a, int b) {
      if (depth[a] < depth[b]) {
        int tmp = a;
        a = b;
        b = tmp;
      }
      int diff = depth[a] - depth[b];
      for (int k = LOG - 1; k >= 0; --k) {
        if ((diff >> k & 1) == 1) {
          a = up[k][a];
        }
      }
      if (a == b) return a;
      for (int k = LOG - 1; k >= 0; --k) {
        if (up[k][a] != -1 && up[k][a] != up[k][b]) {
          a = up[k][a];
          b = up[k][b];
        }
      }
      return up[0][a];
    }

    List<int> ans = [];

    for (var q in queries) {
      int u = q[0], v = q[1];
      if (u == v) {
        ans.add(u);
        continue;
      }
      int l = lca(u, v);
      int tot = dist[u] + dist[v] - 2 * dist[l];

      // climb from u towards l while sum*2 < tot
      int cur = u;
      int currSum = 0;
      for (int k = LOG - 1; k >= 0; --k) {
        int anc = up[k][cur];
        if (anc != -1 && depth[anc] >= depth[l]) {
          int potential = currSum + sumUp[k][cur];
          if ((potential * 2) < tot) {
            currSum = potential;
            cur = anc;
          }
        }
      }
      int nextNode = up[0][cur];
      if (nextNode != -1 && depth[nextNode] >= depth[l]) {
        ans.add(nextNode);
        continue;
      }

      // median lies on the down segment
      int sumU = dist[u] - dist[l];
      int need = ((tot + 1) >> 1); // ceil(tot/2)
      int downNeed = need - sumU;
      if (downNeed <= 0) {
        ans.add(l);
        continue;
      }
      int totalDown = dist[v] - dist[l];
      int wUp = totalDown - downNeed; // weight to move up from v
      int node = v;
      int rem = wUp;
      for (int k = LOG - 1; k >= 0; --k) {
        if (up[k][node] != -1 && sumUp[k][node] <= rem) {
          rem -= sumUp[k][node];
          node = up[k][node];
        }
      }
      ans.add(node);
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
func findMedian(n int, edges [][]int, queries [][]int) []int {
    type Edge struct {
        to   int
        w    int64
    }
    adj := make([][]Edge, n)
    for _, e := range edges {
        u, v, w := e[0], e[1], int64(e[2])
        adj[u] = append(adj[u], Edge{v, w})
        adj[v] = append(adj[v], Edge{u, w})
    }

    // compute LOG
    LOG := 0
    for (1 << LOG) <= n {
        LOG++
    }

    up := make([][]int, LOG)
    sumUp := make([][]int64, LOG)
    depth := make([]int, n)
    dist := make([]int64, n)

    for i := 0; i < LOG; i++ {
        up[i] = make([]int, n)
        sumUp[i] = make([]int64, n)
        for j := 0; j < n; j++ {
            up[i][j] = -1
        }
    }

    // iterative DFS from root 0
    stack := []int{0}
    parent := make([]int, n)
    parent[0] = -1
    visited := make([]bool, n)
    visited[0] = true
    for len(stack) > 0 {
        v := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        for _, e := range adj[v] {
            if !visited[e.to] {
                visited[e.to] = true
                parent[e.to] = v
                up[0][e.to] = v
                sumUp[0][e.to] = e.w
                depth[e.to] = depth[v] + 1
                dist[e.to] = dist[v] + e.w
                stack = append(stack, e.to)
            }
        }
    }

    // binary lifting tables
    for k := 1; k < LOG; k++ {
        for v := 0; v < n; v++ {
            if up[k-1][v] != -1 {
                anc := up[k-1][v]
                up[k][v] = up[k-1][anc]
                sumUp[k][v] = sumUp[k-1][v] + sumUp[k-1][anc]
            }
        }
    }

    lca := func(u, v int) int {
        if depth[u] < depth[v] {
            u, v = v, u
        }
        diff := depth[u] - depth[v]
        for k := LOG - 1; k >= 0; k-- {
            if (diff>>k)&1 == 1 {
                u = up[k][u]
            }
        }
        if u == v {
            return u
        }
        for k := LOG - 1; k >= 0; k-- {
            if up[k][u] != -1 && up[k][u] != up[k][v] {
                u = up[k][u]
                v = up[k][v]
            }
        }
        return up[0][u]
    }

    ans := make([]int, len(queries))
    for idx, q := range queries {
        u, v := q[0], q[1]
        if u == v {
            ans[idx] = u
            continue
        }
        l := lca(u, v)
        tot := dist[u] + dist[v] - 2*dist[l]

        // climb from u towards l while 2*sum < tot
        cur := u
        var sum int64 = 0
        for k := LOG - 1; k >= 0; k-- {
            anc := up[k][cur]
            if anc != -1 && depth[anc] >= depth[l] {
                if 2*(sum+sumUp[k][cur]) < tot {
                    sum += sumUp[k][cur]
                    cur = anc
                }
            }
        }
        // after loop, check if median already found on u side
        if cur != l || 2*sum >= tot {
            ans[idx] = up[0][cur]
            continue
        }

        // need to find on v side
        limit := tot / 2 // floor
        cur = v
        sum = 0
        for k := LOG - 1; k >= 0; k-- {
            anc := up[k][cur]
            if anc != -1 && depth[anc] >= depth[l] && sum+sumUp[k][cur] <= limit {
                sum += sumUp[k][cur]
                cur = anc
            }
        }
        ans[idx] = cur
    }
    return ans
}
```

## Ruby

```ruby
def find_median(n, edges, queries)
  # compute max power for binary lifting
  log = 0
  while (1 << log) <= n
    log += 1
  end

  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  parent = Array.new(n, -1)
  depth = Array.new(n, 0)
  dist_root = Array.new(n, 0)

  up = Array.new(n) { Array.new(log, -1) }
  sum_up = Array.new(n) { Array.new(log, 0) }

  # iterative DFS to fill parent, depth, dist_root, level-0 tables
  stack = [0]
  while !stack.empty?
    node = stack.pop
    adj[node].each do |nei, w|
      next if nei == parent[node]
      parent[nei] = node
      depth[nei] = depth[node] + 1
      dist_root[nei] = dist_root[node] + w
      up[nei][0] = node
      sum_up[nei][0] = w
      stack << nei
    end
  end

  # binary lifting tables
  (1...log).each do |k|
    n.times do |v|
      anc = up[v][k - 1]
      if anc != -1
        up[v][k] = up[anc][k - 1]
        sum_up[v][k] = sum_up[v][k - 1] + sum_up[anc][k - 1]
      else
        up[v][k] = -1
        sum_up[v][k] = 0
      end
    end
  end

  # LCA lambda
  lca = lambda do |a, b|
    if depth[a] < depth[b]
      a, b = b, a
    end
    diff = depth[a] - depth[b]
    bit = 0
    while diff > 0
      if (diff & 1) == 1
        a = up[a][bit]
      end
      diff >>= 1
      bit += 1
    end
    return a if a == b
    (log - 1).downto(0) do |i|
      if up[a][i] != -1 && up[a][i] != up[b][i]
        a = up[a][i]
        b = up[b][i]
      end
    end
    up[a][0]
  end

  ans = []

  queries.each do |u, v|
    l = lca.call(u, v)
    total = dist_root[u] + dist_root[v] - 2 * dist_root[l]

    # try to find median on u -> l side
    cur = u
    cum = 0
    (log - 1).downto(0) do |i|
      anc = up[cur][i]
      if anc != -1 && 2 * (cum + sum_up[cur][i]) < total
        cum += sum_up[cur][i]
        cur = anc
      end
    end
    cand = up[cur][0]
    if cand != -1 && depth[cand] >= depth[l]
      ans << cand
      next
    end

    # median lies on l -> v side
    dist_u_to_l = dist_root[u] - dist_root[l]
    need = (total + 1) / 2          # ceil(total/2)
    extra_needed = need - dist_u_to_l
    d_up = (dist_root[v] - dist_root[l]) - extra_needed

    cur = v
    cum2 = 0
    (log - 1).downto(0) do |i|
      if up[cur][i] != -1 && cum2 + sum_up[cur][i] <= d_up
        cum2 += sum_up[cur][i]
        cur = up[cur][i]
      end
    end
    ans << cur
  end

  ans
end
```

## Scala

```scala
object Solution {
    def findMedian(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
        val adj = Array.fill(n)(new scala.collection.mutable.ListBuffer[(Int, Long)]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            val w = e(2).toLong
            adj(u) += ((v, w))
            adj(v) += ((u, w))
        }

        var LOG = 1
        while ((1 << LOG) <= n) LOG += 1

        val parent = Array.ofDim[Int](LOG, n)
        val depth = new Array[Int](n)
        val dist = new Array[Long](n)

        // iterative DFS to set parent[0], depth, dist
        val stack = new scala.collection.mutable.Stack[Int]()
        stack.push(0)
        parent(0)(0) = -1
        depth(0) = 0
        dist(0) = 0L

        while (stack.nonEmpty) {
            val node = stack.pop()
            for ((nei, w) <- adj(node)) {
                if (nei != parent(0)(node)) {
                    parent(0)(nei) = node
                    depth(nei) = depth(node) + 1
                    dist(nei) = dist(node) + w
                    stack.push(nei)
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
            var diff = depth(u) - depth(v)
            var bit = 0
            while (diff > 0) {
                if ((diff & 1) == 1) u = parent(bit)(u)
                diff >>= 1
                bit += 1
            }
            if (u == v) return u
            for (k <- LOG - 1 to 0 by -1) {
                val pu = parent(k)(u)
                val pv = parent(k)(v)
                if (pu != -1 && pu != pv) {
                    u = pu
                    v = pv
                }
            }
            parent(0)(u)
        }

        val m = queries.length
        val ans = new Array[Int](m)

        for (i <- 0 until m) {
            val u = queries(i)(0)
            val v = queries(i)(1)
            val l = lca(u, v)
            val total = dist(u) + dist(v) - 2L * dist(l)
            val half = (total + 1) / 2

            // try to find median on u -> l side
            var curU = u
            for (k <- LOG - 1 to 0 by -1) {
                val anc = parent(k)(curU)
                if (anc != -1 && depth(anc) >= depth(l)) {
                    val duAnc = dist(u) - dist(anc)
                    if (duAnc * 2 < total) curU = anc
                }
            }

            if (curU != l) {
                ans(i) = parent(0)(curU)
            } else {
                // median lies on l -> v side
                val need = half - (dist(u) - dist(l)) // distance needed from l
                var curV = v
                for (k <- LOG - 1 to 0 by -1) {
                    val anc = parent(k)(curV)
                    if (anc != -1 && depth(anc) >= depth(l)) {
                        val dFromLAnc = dist(anc) - dist(l)
                        if (dFromLAnc >= need) curV = anc
                    }
                }
                ans(i) = curV
            }
        }

        ans
    }
}
```

## Rust

```rust
use std::cmp::max;

pub struct Solution;

impl Solution {
    pub fn find_median(n: i32, edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
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

        const INF: usize = usize::MAX;

        // parent[k][v], dist_up[k][v]
        let mut parent: Vec<Vec<usize>> = vec![vec![INF; n]; log];
        let mut dist_up: Vec<Vec<i64>> = vec![vec![0i64; n]; log];
        let mut depth: Vec<usize> = vec![0; n];
        let mut depth_dist: Vec<i64> = vec![0; n];

        // iterative stack for DFS
        let mut stack: Vec<(usize, usize)> = Vec::new(); // (node, parent)
        stack.push((0, INF));
        while let Some((v, p)) = stack.pop() {
            parent[0][v] = p;
            for &(to, w) in adj[v].iter() {
                if to == p { continue; }
                depth[to] = depth[v] + 1;
                depth_dist[to] = depth_dist[v] + w;
                dist_up[0][to] = w;
                stack.push((to, v));
            }
        }

        // binary lifting tables
        for k in 1..log {
            for v in 0..n {
                let mid = parent[k - 1][v];
                if mid != INF {
                    parent[k][v] = parent[k - 1][mid];
                    dist_up[k][v] = dist_up[k - 1][v] + dist_up[k - 1][mid];
                }
            }
        }

        // LCA function
        let lca = |mut a: usize, mut b: usize,
                   depth: &Vec<usize>,
                   parent: &Vec<Vec<usize>>,
                   log: usize| -> usize {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }
            let diff = depth[a] - depth[b];
            for k in 0..log {
                if (diff >> k) & 1 == 1 {
                    a = parent[k][a];
                }
            }
            if a == b { return a; }
            for k in (0..log).rev() {
                if parent[k][a] != INF && parent[k][a] != parent[k][b] {
                    a = parent[k][a];
                    b = parent[k][b];
                }
            }
            parent[0][a]
        };

        let mut answer: Vec<i32> = Vec::with_capacity(queries.len());

        for q in queries.iter() {
            let u = q[0] as usize;
            let v = q[1] as usize;
            if u == v {
                answer.push(u as i32);
                continue;
            }
            let l = lca(u, v, &depth, &parent, log);
            let du = depth_dist[u] - depth_dist[l];
            let dv = depth_dist[v] - depth_dist[l];
            let tot = du + dv;
            let need = (tot + 1) / 2; // ceil(tot/2)

            if du >= need {
                // climb from u
                let mut cur = u;
                let mut sum = 0i64;
                for k in (0..log).rev() {
                    let p = parent[k][cur];
                    if p != INF && sum + dist_up[k][cur] < need {
                        sum += dist_up[k][cur];
                        cur = p;
                    }
                }
                let ans_node = if parent[0][cur] == INF { cur } else { parent[0][cur] };
                answer.push(ans_node as i32);
            } else {
                // median on v side
                let need_from_v = tot - need; // distance needed from v upwards
                let mut cur = v;
                let mut sum = 0i64;
                for k in (0..log).rev() {
                    let p = parent[k][cur];
                    if p != INF && sum + dist_up[k][cur] < need_from_v {
                        sum += dist_up[k][cur];
                        cur = p;
                    }
                }
                let ans_node = if parent[0][cur] == INF { cur } else { parent[0][cur] };
                answer.push(ans_node as i32);
            }
        }

        answer
    }
}
```

## Racket

```racket
(define (find-median n edges queries)
  (let* ((LOG (+ 1 (exact-floor (log n 2))))
         ;; adjacency list
         (adj (make-vector n '()))
         (_ (for-each (lambda (e)
                        (let* ((u (list-ref e 0))
                               (v (list-ref e 1))
                               (w (list-ref e 2)))
                          (vector-set! adj u (cons (list v w) (vector-ref adj u)))
                          (vector-set! adj v (cons (list u w) (vector-ref adj v)))))
                      edges))
         ;; tables
         (parent (make-vector n (make-vector LOG -1)))
         (sum-up (make-vector n (make-vector LOG 0)))
         (depth-level (make-vector n 0))
         (depth-dist (make-vector n 0))
         ;; DFS stack
         (stack (list (list 0 -1 0))) ; node, parent, weight-from-parent
         )
    ;; iterative DFS to fill level 0 tables
    (let loop ((stk stack))
      (when (pair? stk)
        (let* ((item (car stk))
               (node (list-ref item 0))
               (par  (list-ref item 1))
               (wpar (list-ref item 2)))
          (when (> par -1)
            (vector-set! (vector-ref parent node) 0 par)
            (vector-set! (vector-ref sum-up node) 0 wpar)
            (vector-set! depth-level node (+ (vector-ref depth-level par) 1))
            (vector-set! depth-dist node (+ (vector-ref depth-dist par) wpar)))
          (for-each
           (lambda (nbr)
             (let ((to (list-ref nbr 0))
                   (wt (list-ref nbr 1)))
               (when (not (= to par))
                 (set! stk (cons (list to node wt) stk)))))
           (vector-ref adj node))
          (loop (cdr stk)))))

    ;; build binary lifting tables
    (for ([k (in-range 1 LOG)])
      (for ([v (in-range n)])
        (let* ((mid (vector-ref (vector-ref parent v) (- k 1))))
          (when (not (= mid -1))
            (vector-set! (vector-ref parent v) k
                         (vector-ref (vector-ref parent mid) (- k 1)))
            (vector-set! (vector-ref sum-up v) k
                         (+ (vector-ref (vector-ref sum-up v) (- k 1))
                            (vector-ref (vector-ref sum-up mid) (- k 1))))))))

    ;; helper: lift node up by weight w, returning the ancestor reached after consuming exactly w
    (define (ascend node w)
      (let loop ((cur node) (rem w) (k (- LOG 1)))
        (if (< k 0)
            cur
            (let* ((anc (vector-ref (vector-ref parent cur) k))
                   (add (vector-ref (vector-ref sum-up cur) k)))
              (if (and (not (= anc -1)) (<= add rem))
                  (loop anc (- rem add) (- k 1))
                  (loop cur rem (- k 1)))))))

    ;; helper: find first node on upward path where cumulative >= target
    (define (first-above u target)
      (let loop ((cur u) (acc 0) (k (- LOG 1)))
        (if (< k 0)
            (vector-ref (vector-ref parent cur) 0) ; immediate parent crosses threshold
            (let* ((anc (vector-ref (vector-ref parent cur) k))
                   (add (vector-ref (vector-ref sum-up cur) k)))
              (if (and anc (not (= anc -1)) (< (+ acc add) target))
                  (loop anc (+ acc add) (- k 1))
                  (loop cur acc (- k 1)))))))

    ;; LCA using binary lifting on levels
    (define (lca u v)
      (let* ((du (vector-ref depth-level u))
             (dv (vector-ref depth-level v)))
        (let loop-raise ((a u) (b v) (da du) (db dv))
          (cond [(> da db)
                 (loop-raise (ascend a (- da db)) b (db) db)]
                [(< da db)
                 (loop-raise a (ascend b (- db da)) da (da))]
                [else
                 (if (= a b) a
                     (let inner ((x a) (y b) (k (- LOG 1)))
                       (if (< k 0)
                           (vector-ref (vector-ref parent x) 0)
                           (let* ((px (vector-ref (vector-ref parent x) k))
                                  (py (vector-ref (vector-ref parent y) k)))
                             (if (or (= px -1) (= py -1) (not (= px py)))
                                 (inner x y (- k 1))
                                 (inner px py (- k 1))))))])))))

    ;; process queries
    (let ((ans (make-vector (length queries) 0)))
      (for ([idx (in-naturals)] [q queries])
        (let* ((u (list-ref q 0))
               (v (list-ref q 1))
               (l (lca u v))
               (tot (- (+ (vector-ref depth-dist u)
                          (vector-ref depth-dist v))
                       (* 2 (vector-ref depth-dist l))))
               (need (quotient (+ tot 1) 2)) ; ceil(tot/2)
               (dist-u-l (- (vector-ref depth-dist u)
                            (vector-ref depth-dist l))))
          (if (<= need dist-u-l)
              (let ((node (first-above u need)))
                (vector-set! ans idx node))
              (let* ((remaining (- need dist-u-l))
                     (dist-v-l (- (vector-ref depth-dist v)
                                  (vector-ref depth-dist l)))
                     (up-from-v (- dist-v-l remaining))
                     (node (ascend v up-from-v)))
                (vector-set! ans idx node)))))
      (vector->list ans))))
```

## Erlang

```erlang
-module(solution).
-export([find_median/3]).

find_median(N, Edges, Queries) ->
    Adj0 = array:new(N, [{default, []}]),
    Adj = lists:foldl(fun([U,V,W], Acc) ->
        L1 = array:get(U, Acc),
        L2 = array:get(V, Acc),
        Acc1 = array:set(U, [{V,W}|L1], Acc),
        array:set(V, [{U,W}|L2], Acc1)
    end, Adj0, Edges),

    Parent0 = array:new(N, [{default, -1}]),
    Depth0  = array:new(N, [{default, 0}]),
    Dist0   = array:new(N, [{default, 0}]),
    EdgeW0  = array:new(N, [{default, 0}]),

    Stack0 = [{0, -1, 0, 0, 0}],
    {Parent1, Depth1, Dist1, EdgeW1} =
        dfs(Stack0, Adj, Parent0, Depth0, Dist0, EdgeW0),

    Log = log_limit(N) + 1,
    {ParentsTuple, UpsTuple} = build_tables(Log, N, Parent1, EdgeW1),

    AnswersRev = process_queries(Queries, ParentsTuple, UpsTuple,
                                 Depth1, Dist1, Log),
    lists:reverse(AnswersRev).

dfs([], _Adj, Parent, Depth, Dist, EdgeW) ->
    {Parent, Depth, Dist, EdgeW};
dfs([{Node, Par, Dep, DistAcc, EW}|Rest], Adj, Parent, Depth, Dist, EdgeW) ->
    P1 = array:set(Node, Par, Parent),
    D1 = array:set(Node, Dep, Depth),
    Di1 = array:set(Node, DistAcc, Dist),
    Ew1 = array:set(Node, EW, EdgeW),
    Neighs = array:get(Node, Adj),
    NewStack = lists:foldl(fun({To,W}, Acc) ->
                if To =/= Par -> [{To, Node, Dep+1, DistAcc+W, W}|Acc];
                   true -> Acc
                end
            end, Rest, Neighs),
    dfs(NewStack, Adj, P1, D1, Di1, Ew1).

log_limit(N) ->
    log_limit(N, 0).
log_limit(N, L) when (1 bsl L) >= N -> L;
log_limit(N, L) -> log_limit(N, L+1).

build_tables(Log, N, Parent0, Up0) ->
    build_levels(1, Log-1, N, Parent0, Up0, [Parent0], [Up0]).

build_levels(_K, MaxK, _N, _PrevP, _PrevU, AccP, AccU) when _K > MaxK ->
    {list_to_tuple(lists:reverse(AccP)), list_to_tuple(lists:reverse(AccU))};
build_levels(K, MaxK, N, PrevP, PrevU, AccP, AccU) ->
    NewP = array:new(N, [{default,-1}]),
    NewU = array:new(N, [{default,0}]),
    {NewP2, NewU2} = fill_level(0, N-1, PrevP, PrevU, NewP, NewU),
    build_levels(K+1, MaxK, N, NewP2, NewU2,
                 [NewP2|AccP], [NewU2|AccU]).

fill_level(I, MaxI, PrevP, PrevU, CurP, CurU) when I > MaxI ->
    {CurP, CurU};
fill_level(I, MaxI, PrevP, PrevU, CurP, CurU) ->
    P = array:get(I, PrevP),
    case P of
        -1 ->
            CP1 = array:set(I, -1, CurP),
            CU1 = array:set(I, 0, CurU);
        _ ->
            PP = array:get(P, PrevP),
            W = array:get(I, PrevU) + array:get(P, PrevU),
            CP1 = array:set(I, PP, CurP),
            CU1 = array:set(I, W, CurU)
    end,
    fill_level(I+1, MaxI, PrevP, PrevU, CP1, CU1).

process_queries([], _Parents, _Ups, _Depth, _Dist, _Log) ->
    [];
process_queries([[U,V]|Rest], Parents, Ups, DepthArr, DistArr, Log) ->
    Ans = query_median(U, V, Parents, Ups, DepthArr, DistArr, Log),
    [Ans | process_queries(Rest, Parents, Ups, DepthArr, DistArr, Log)].

query_median(U, V, Parents, Ups, DepthArr, DistArr, Log) ->
    if U == V -> U;
       true ->
        L = lca(U, V, Parents, DepthArr, Log),
        Tot = array:get(U, DistArr) + array:get(V, DistArr) - 2*array:get(L, DistArr),
        Target = (Tot + 1) div 2,
        if Target == 0 -> U;
           true ->
            LDepth = array:get(L, DepthArr),
            {CurU, SumU} = climb_u(Log-1, U, 0, LDepth, Target, Parents, Ups, DepthArr),
            ParentCurU = get_parent(0, CurU, Parents),
            case ParentCurU of
                -1 -> median_v_side(U, V, LDepth, SumU, Target,
                                    Parents, Ups, DepthArr, Log);
                _ ->
                    if array:get(ParentCurU, DepthArr) >= LDepth ->
                        ParentCurU;
                       true ->
                        median_v_side(U, V, LDepth, SumU, Target,
                                      Parents, Ups, DepthArr, Log)
                    end
            end
        end
    end.

climb_u(-1, Node, Sum, _LDepth, _Target, _Parents, _Ups, _Depth) ->
    {Node, Sum};
climb_u(K, Node, Sum, LDepth, Target, Parents, Ups, DepthArr) ->
    Anc = get_parent(K, Node, Parents),
    case Anc of
        -1 -> climb_u(K-1, Node, Sum, LDepth, Target, Parents, Ups, DepthArr);
        _ ->
            if array:get(Anc, DepthArr) >= LDepth ->
                NewSum = Sum + get_up(K, Node, Ups),
                if NewSum < Target ->
                    climb_u(K, Anc, NewSum, LDepth, Target, Parents, Ups, DepthArr);
                true ->
                    climb_u(K-1, Node, Sum, LDepth, Target, Parents, Ups, DepthArr)
                end;
               true ->
                climb_u(K-1, Node, Sum, LDepth, Target, Parents, Ups, DepthArr)
            end
    end.

median_v_side(_U, V, LDepth, SumU, Target,
              Parents, Ups, DepthArr, Log) ->
    {CurV, _} = climb_v(Log-1, V, 0, LDepth, Target, SumU,
                        Parents, Ups, DepthArr),
    get_parent(0, CurV, Parents).

climb_v(-1, Node, Sum, _LDepth, _Target, _BaseSum, _Parents, _Ups, _Depth) ->
    {Node, Sum};
climb_v(K, Node, Sum, LDepth, Target, BaseSum, Parents, Ups, DepthArr) ->
    Anc = get_parent(K, Node, Parents),
    case Anc of
        -1 -> climb_v(K-1, Node, Sum, LDepth, Target, BaseSum, Parents, Ups, DepthArr);
        _ ->
            if array:get(Anc, DepthArr) > LDepth ->
                NewSum = Sum + get_up(K, Node, Ups),
                if BaseSum + NewSum < Target ->
                    climb_v(K, Anc, NewSum, LDepth, Target, BaseSum,
                            Parents, Ups, DepthArr);
                true ->
                    climb_v(K-1, Node, Sum, LDepth, Target, BaseSum,
                            Parents, Ups, DepthArr)
                end;
               true ->
                climb_v(K-1, Node, Sum, LDepth, Target, BaseSum,
                        Parents, Ups, DepthArr)
            end
    end.

lca(U, V, Parents, DepthArr, Log) ->
    DU = array:get(U, DepthArr),
    DV = array:get(V, DepthArr),
    {U1,V1} = if DU < DV -> {V,U}; true -> {U,V} end,
    Diff = erlang:abs(DU - DV),
    U2 = lift_node(U1, Diff, Parents, Log),
    V2 = V1,
    if U2 == V2 -> U2;
       true -> lca_up(U2, V2, Parents, DepthArr, Log)
    end.

lift_node(Node, 0, _Parents, _Log) ->
    Node;
lift_node(Node, Dist, Parents, Log) ->
    lift_node_loop(Log-1, Node, Dist, Parents).

lift_node_loop(-1, Node, _Dist, _Parents) ->
    Node;
lift_node_loop(K, Node, Dist, Parents) ->
    if (Dist band (1 bsl K)) =/= 0 ->
        NewNode = get_parent(K, Node, Parents),
        lift_node_loop(K-1, NewNode, Dist, Parents);
       true ->
        lift_node_loop(K-1, Node, Dist, Parents)
    end.

lca_up(U, V, Parents, DepthArr, Log) ->
    lca_up_loop(Log-1, U, V, Parents, DepthArr).

lca_up_loop(-1, U, _V, _Parents, _DepthArr) ->
    U;
lca_up_loop(K, U, V, Parents, DepthArr) ->
    PU = get_parent(K, U, Parents),
    PV = get_parent(K, V, Parents),
    if PU =/= -1 andalso PU =/= PV ->
        lca_up_loop(K-1, PU, PV, Parents, DepthArr);
       true ->
        lca_up_loop(K-1, U, V, Parents, DepthArr)
    end.

get_parent(Level, Node, Parents) ->
    array:get(Node, element(Level+1, Parents)).

get_up(Level, Node, Ups) ->
    array:get(Node, element(Level+1, Ups)).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec find_median(integer, [[integer]], [[integer]]) :: [integer]
  def find_median(n, edges, queries) do
    max_log = :math.ceil(:math.log2(n)) |> trunc |> Kernel.+(1)

    # build adjacency list
    adj0 = :array.new(n, default: [])
    adj =
      Enum.reduce(edges, adj0, fn [u, v, w], acc ->
        upd1 = update_adj(acc, u, {v, w})
        update_adj(upd1, v, {u, w})
      end)

    # dfs to fill depth, dist, parent[0], upWeight[0]
    {depth, dist, parent0, upW0} = dfs_build(n, adj)

    # binary lifting tables
    {parents, upWs} = build_lift(parent0, upW0, max_log, n)

    Enum.map(queries, fn [u, v] ->
      median_node(u, v, depth, dist, parents, upWs, max_log)
    end)
  end

  # update adjacency list
  defp update_adj(arr, node, edge) do
    lst = :array.get(node, arr)
    :array.set(node, [edge | lst], arr)
  end

  # DFS iterative stack to fill basic arrays
  defp dfs_build(n, adj) do
    depth = :array.new(n, default: 0)
    dist = :array.new(n, default: 0)
    parent0 = :array.new(n, default: -1)
    upW0 = :array.new(n, default: 0)

    stack = [{0, -1, 0}]
    visited = MapSet.new()

    {depth, dist, parent0, upW0} =
      dfs_loop(stack, visited, depth, dist, parent0, upW0, adj)

    {depth, dist, parent0, upW0}
  end

  defp dfs_loop([], _vis, depth, dist, par, upw, _adj), do: {depth, dist, par, upw}

  defp dfs_loop([{node, p, w} | rest], visited, depth, dist, par, upw, adj) do
    if MapSet.member?(visited, node) do
      dfs_loop(rest, visited, depth, dist, par, upw, adj)
    else
      visited = MapSet.put(visited, node)

      dval =
        if p == -1, do: 0, else: (:array.get(p, depth) + 1)

      dist_val =
        if p == -1, do: 0, else: (:array.get(p, dist) + w)

      depth = :array.set(node, dval, depth)
      dist = :array.set(node, dist_val, dist)
      par = :array.set(node, p, par)
      upw = :array.set(node, w, upw)

      neigh = :array.get(node, adj)

      new_stack =
        Enum.reduce(neigh, rest, fn {to, wt}, acc ->
          if to != p do
            [{to, node, wt} | acc]
          else
            acc
          end
        end)

      dfs_loop(new_stack, visited, depth, dist, par, upw, adj)
    end
  end

  # build binary lifting tables
  defp build_lift(parent0, upW0, max_log, n) do
    parents = [parent0]
    upWs = [upW0]

    {parents, upWs} =
      Enum.reduce(1..max_log - 1, {parents, upWs}, fn _k,
                                                    {ps_acc, us_acc} ->
        prev_par = List.last(ps_acc)
        prev_up = List.last(us_acc)

        {cur_par, cur_up} =
          Enum.reduce(0..n - 1, {:array.new(n, default: -1),
                                 :array.new(n, default: 0)}, fn i,
                                                                      {par_acc,
                                                                       up_acc} ->
            p = :array.get(i, prev_par)

            if p != -1 do
              pp = :array.get(p, prev_par)
              pu = :array.get(i, prev_up) + :array.get(p, prev_up)

              {
                :array.set(i, pp, par_acc),
                :array.set(i, pu, up_acc)
              }
            else
              {par_acc, up_acc}
            end
          end)

        {[cur_par | ps_acc], [cur_up | us_acc]}
      end)

    # reverse to maintain order 0..max_log-1
    {Enum.reverse(parents), Enum.reverse(upWs)}
  end

  # LCA using binary lifting
  defp lca(u, v, depth, parents, max_log) do
    du = :array.get(u, depth)
    dv = :array.get(v, depth)

    {a, b, diff} =
      if du < dv do
        {v, u, dv - du}
      else
        {u, v, du - dv}
      end

    a = lift_by_depth(a, diff, parents, max_log)

    if a == b do
      a
    else
      {a2, b2} =
        Enum.reduce((max_log - 1)..0, {a, b}, fn k, {x, y} ->
          px = :array.get(x, Enum.at(parents, k))
          py = :array.get(y, Enum.at(parents, k))

          if px != -1 and px != py do
            {px, py}
          else
            {x, y}
          end
        end)

      :array.get(a2, Enum.at(parents, 0))
    end
  end

  defp lift_by_depth(node, steps, parents, max_log) do
    Enum.reduce(0..max_log - 1, node, fn k, cur ->
      if (steps &&& (1 <<< k)) != 0 do
        p = :array.get(cur, Enum.at(parents, k))
        if p == -1, do: cur, else: p
      else
        cur
      end
    end)
  end

  # climb up by exact weight
  defp climb_up_by_weight(node, w, parents, upWs, max_log) do
    {res, _} =
      Enum.reduce((max_log - 1)..0, {node, w}, fn k, {cur, rem} ->
        pw = :array.get(cur, Enum.at(upWs, k))

        if pw <= rem do
          p = :array.get(cur, Enum.at(parents, k))
          {p, rem - pw}
        else
          {cur, rem}
        end
      end)

    res
  end

  # answer for a single query
  defp median_node(u, v, depth, dist, parents, upWs, max_log) do
    if u == v do
      u
    else
      l = lca(u, v, depth, parents, max_log)

      total =
        :array.get(u, dist) + :array.get(v, dist) -
          2 * :array.get(l, dist)

      need = div(total + 1, 2)

      du_l = :array.get(u, dist) - :array.get(l, dist)

      if need <= du_l do
        # median on u -> l side
        {node, cum} =
          Enum.reduce((max_log - 1)..0, {u, 0}, fn k,
                                                {cur, cur_sum} ->
            pw = :array.get(cur, Enum.at(upWs, k))

            if cur_sum + pw < need do
              p = :array.get(cur, Enum.at(parents, k))
              {p, cur_sum + pw}
            else
              {cur, cur_sum}
            end
          end)

        ans = :array.get(node, Enum.at(parents, 0))

        if ans == -1, do: node, else: ans
      else
        # median on l -> v side
        rem = need - du_l
        dv_l = :array.get(v, dist) - :array.get(l, dist)
        steps_up_weight = dv_l - rem

        climb_up_by_weight(v, steps_up_weight, parents, upWs, max_log)
      end
    end
  end
end
```

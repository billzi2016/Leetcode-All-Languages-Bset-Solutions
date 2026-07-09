# 2699. Modify Graph Edge Weights

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    const long long INF = (1LL<<60);
    const int MAXW = 2000000000;
    
    vector<long long> dijkstra(int n, const vector<vector<int>>& edges,
                               const vector<vector<pair<int,int>>>& adj,
                               int src, long long wMinusOne) {
        vector<long long> dist(n, INF);
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        dist[src]=0;
        pq.push({0,src});
        while(!pq.empty()){
            auto [d,u]=pq.top(); pq.pop();
            if(d!=dist[u]) continue;
            for(auto [v,ei]: adj[u]){
                long long w = edges[ei][2];
                if(w==-1) w = wMinusOne;
                if(dist[v] > d + w){
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }
        return dist;
    }
    
    long long dijkstraSingle(int n, const vector<vector<int>>& edges,
                             const vector<vector<pair<int,int>>>& adj,
                             int src, int dst, long long wMinusOne) {
        auto dist = dijkstra(n, edges, adj, src, wMinusOne);
        return dist[dst];
    }
    
    vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges,
                                           int source, int destination, int target) {
        // build adjacency list with edge indices
        vector<vector<pair<int,int>>> adj(n);
        for(int i=0;i<(int)edges.size();++i){
            int u=edges[i][0], v=edges[i][1];
            adj[u].push_back({v,i});
            adj[v].push_back({u,i});
        }
        
        // shortest distance using only fixed edges (treat -1 as INF)
        long long d_fixed = dijkstraSingle(n, edges, adj, source, destination, INF);
        if(d_fixed < target) return {};
        if(d_fixed == target){
            vector<vector<int>> ans = edges;
            for(auto &e: ans) if(e[2]==-1) e[2]=MAXW;
            return ans;
        }
        
        // distances with -1 treated as 1
        auto ds = dijkstra(n, edges, adj, source, 1);
        auto dt = dijkstra(n, edges, adj, destination, 1);
        
        int chosenIdx=-1;
        long long chosenWeight=0;
        for(int i=0;i<(int)edges.size();++i){
            if(edges[i][2]!=-1) continue;
            int u=edges[i][0], v=edges[i][1];
            // orientation u->v
            if(ds[u]!=INF && dt[v]!=INF){
                long long need = (long long)target - ds[u] - dt[v];
                if(need>=1 && need<=MAXW){
                    chosenIdx=i;
                    chosenWeight=need;
                    break;
                }
            }
            // orientation v->u
            if(ds[v]!=INF && dt[u]!=INF){
                long long need = (long long)target - ds[v] - dt[u];
                if(need>=1 && need<=MAXW){
                    chosenIdx=i;
                    chosenWeight=need;
                    break;
                }
            }
        }
        if(chosenIdx==-1) return {};
        
        vector<vector<int>> ans = edges;
        for(int i=0;i<(int)ans.size();++i){
            if(ans[i][2]==-1){
                ans[i][2] = (i==chosenIdx)? (int)chosenWeight : MAXW;
            }
        }
        // final verification optional (skip for speed)
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class EdgeInfo {
        int to;
        int idx;
        EdgeInfo(int to, int idx) { this.to = to; this.idx = idx; }
    }

    private long[] dijkstra(int n, List<EdgeInfo>[] graph, long[] w, int start) {
        long INF = Long.MAX_VALUE / 4;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[start] = 0;
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0L, start});
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int u = (int)cur[1];
            if (d != dist[u]) continue;
            for (EdgeInfo e : graph[u]) {
                int v = e.to;
                long weight = w[e.idx];
                long nd = d + weight;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.offer(new long[]{nd, v});
                }
            }
        }
        return dist;
    }

    public int[][] modifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        int m = edges.length;
        List<EdgeInfo>[] graph = new ArrayList[n];
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int i = 0; i < m; ++i) {
            int u = edges[i][0], v = edges[i][1];
            graph[u].add(new EdgeInfo(v, i));
            graph[v].add(new EdgeInfo(u, i));
        }

        final long MAX_W = 2_000_000_000L;
        // weights with -1 as 1 (minimum)
        long[] wMin = new long[m];
        for (int i = 0; i < m; ++i) {
            wMin[i] = edges[i][2] == -1 ? 1L : edges[i][2];
        }
        long[] distSMin = dijkstra(n, graph, wMin, source);
        long[] distTMin = dijkstra(n, graph, wMin, destination);

        if (distSMin[destination] > target) return new int[0][];

        // weights with -1 as MAX_W (effectively ignored)
        long[] wMax = new long[m];
        for (int i = 0; i < m; ++i) {
            wMax[i] = edges[i][2] == -1 ? MAX_W : edges[i][2];
        }
        long[] distSMax = dijkstra(n, graph, wMax, source);
        if (distSMax[destination] < target) return new int[0][];

        // Try to adjust each unknown edge
        for (int i = 0; i < m; ++i) {
            if (edges[i][2] != -1) continue;
            int u = edges[i][0];
            int v = edges[i][1];

            long du = distSMin[u];
            long dv = distTMin[v];
            if (du == Long.MAX_VALUE/4 || dv == Long.MAX_VALUE/4) {
                // try opposite direction
                du = distSMin[v];
                dv = distTMin[u];
                if (du == Long.MAX_VALUE/4 || dv == Long.MAX_VALUE/4) continue;
                long need = target - du - dv;
                if (need < 1L || need > MAX_W) continue;
                long[] wTrial = Arrays.copyOf(wMax, m);
                wTrial[i] = need;
                long[] distCheck = dijkstra(n, graph, wTrial, source);
                if (distCheck[destination] == target) {
                    int[][] res = new int[m][3];
                    for (int j = 0; j < m; ++j) {
                        res[j][0] = edges[j][0];
                        res[j][1] = edges[j][1];
                        res[j][2] = (edges[j][2] == -1) ? (int)wTrial[j] : edges[j][2];
                    }
                    return res;
                }
            } else {
                long need = target - du - dv;
                if (need < 1L || need > MAX_W) continue;
                long[] wTrial = Arrays.copyOf(wMax, m);
                wTrial[i] = need;
                long[] distCheck = dijkstra(n, graph, wTrial, source);
                if (distCheck[destination] == target) {
                    int[][] res = new int[m][3];
                    for (int j = 0; j < m; ++j) {
                        res[j][0] = edges[j][0];
                        res[j][1] = edges[j][1];
                        res[j][2] = (edges[j][2] == -1) ? (int)wTrial[j] : edges[j][2];
                    }
                    return res;
                }
            }
        }

        // If no single edge adjustment works, set all unknown to large weight if already feasible
        if (distSMax[destination] == target) {
            int[][] res = new int[m][3];
            for (int i = 0; i < m; ++i) {
                res[i][0] = edges[i][0];
                res[i][1] = edges[i][1];
                res[i][2] = edges[i][2] == -1 ? (int)MAX_W : edges[i][2];
            }
            return res;
        }

        return new int[0][];
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :type target: int
        :rtype: List[List[int]]
        """
        INF = 10**18
        BIG = 2000000001  # > 2e9

        m = len(edges)

        def dijkstra(weights, start):
            adj = [[] for _ in range(n)]
            for idx, (u, v, _) in enumerate(edges):
                w = weights[idx]
                adj[u].append((v, w))
                adj[v].append((u, w))
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

        # weights with -1 as 1 (minimum)
        min_weights = [1 if w == -1 else w for _, _, w in edges]
        dist_min = dijkstra(min_weights, source)[destination]
        if dist_min > target:
            return []

        # weights with -1 as BIG (effectively ignored)
        max_weights = [BIG if w == -1 else w for _, _, w in edges]
        dist_max = dijkstra(max_weights, source)[destination]
        if dist_max < target:
            return []
        if dist_max == target:
            res = [list(e) for e in edges]
            for i in range(m):
                if res[i][2] == -1:
                    res[i][2] = BIG
            return res

        # distances from source and destination using min weights (treat -1 as 1)
        ds = dijkstra(min_weights, source)
        dt = dijkstra(min_weights, destination)

        for i in range(m):
            u, v, w_orig = edges[i]
            if w_orig != -1:
                continue
            du = ds[u]
            dv = dt[v]
            if du == INF or dv == INF:
                # try opposite direction as graph undirected
                du = ds[v]
                dv = dt[u]
                if du == INF or dv == INF:
                    continue
                u, v = v, u  # swap for calculation consistency

            total = du + dv
            if total < target:
                needed = target - total
                if needed <= 0:
                    continue
                # build temporary weights: this edge gets 'needed', others BIG
                temp_weights = []
                for j in range(m):
                    _, _, wj = edges[j]
                    if wj != -1:
                        temp_weights.append(wj)
                    else:
                        temp_weights.append(needed if j == i else BIG)
                cur_dist = dijkstra(temp_weights, source)[destination]
                if cur_dist == target:
                    res = [list(e) for e in edges]
                    for j in range(m):
                        if res[j][2] != -1:
                            continue
                        res[j][2] = needed if j == i else BIG
                    return res

        return []
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        INF = 2_000_000_000
        m = len(edges)
        # adjacency list stores (neighbor, edge_index)
        adj = [[] for _ in range(n)]
        for idx, (u, v, w) in enumerate(edges):
            adj[u].append((v, idx))
            adj[v].append((u, idx))

        # assigned_weights[i] is None if not yet decided, otherwise the final weight
        assigned = [None] * m

        def dijkstra(use_one: bool):
            dist = [float('inf')] * n
            parent = [-1] * n
            dist[source] = 0
            heap = [(0, source)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, idx in adj[u]:
                    w_orig = edges[idx][2]
                    if assigned[idx] is not None:
                        wgt = assigned[idx]
                    elif w_orig != -1:
                        wgt = w_orig
                    else:
                        wgt = 1 if use_one else INF
                    nd = d + wgt
                    if nd < dist[v]:
                        dist[v] = nd
                        parent[v] = idx
                        heapq.heappush(heap, (nd, v))
            return dist[destination], parent

        # 1) Check with -1 edges set to huge value
        dist_inf, _ = dijkstra(False)
        if dist_inf < target:
            return []
        if dist_inf == target:
            for i in range(m):
                if edges[i][2] == -1:
                    assigned[i] = INF
            return [[edges[i][0], edges[i][1], assigned[i]] for i in range(m)]

        # 2) Check with -1 edges set to 1
        dist_one, parent = dijkstra(True)
        if dist_one > target:
            return []
        if dist_one == target:
            for i in range(m):
                if edges[i][2] == -1:
                    assigned[i] = INF
            return [[edges[i][0], edges[i][1], assigned[i]] for i in range(m)]

        # Need to increase some -1 edge on the shortest path
        need = target - dist_one  # positive
        cur = destination
        while cur != source:
            idx = parent[cur]
            if idx == -1:   # should not happen
                return []
            u, v, w_orig = edges[idx]
            nxt = u if v == cur else v
            if w_orig == -1:
                # increase this edge
                assigned[idx] = 1 + need
                break
            cur = nxt

        # If no modifiable edge found (should not happen), impossible
        if assigned[parent[destination]] is None and all(edges[i][2] != -1 or assigned[i] is not None for i in range(m)):
            return []

        # Set remaining unknown edges to INF
        for i in range(m):
            if edges[i][2] == -1 and assigned[i] is None:
                assigned[i] = INF

        # Verify final distance equals target
        final_dist, _ = dijkstra(False)  # now all weights are concrete via assigned
        if final_dist != target:
            return []

        return [[edges[i][0], edges[i][1], assigned[i]] for i in range(m)]
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static void dijkstra(int n, int **edges, int edgesSize, long long replaceMinusOne,
                     int src, long long *dist) {
    const long long INF = (1LL << 60);
    for (int i = 0; i < n; ++i) dist[i] = INF;
    bool visited[101] = {false};
    dist[src] = 0;

    for (int iter = 0; iter < n; ++iter) {
        int u = -1;
        long long best = INF;
        for (int i = 0; i < n; ++i) {
            if (!visited[i] && dist[i] < best) {
                best = dist[i];
                u = i;
            }
        }
        if (u == -1) break;
        visited[u] = true;

        for (int e = 0; e < edgesSize; ++e) {
            int a = edges[e][0];
            int b = edges[e][1];
            long long wOrig = edges[e][2];
            long long w = (wOrig == -1 ? replaceMinusOne : wOrig);
            if (a == u && !visited[b]) {
                if (dist[u] + w < dist[b]) dist[b] = dist[u] + w;
            } else if (b == u && !visited[a]) {
                if (dist[u] + w < dist[a]) dist[a] = dist[u] + w;
            }
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** modifiedGraphEdges(int n, int** edges, int edgesSize, int* edgesColSize,
                         int source, int destination, int target,
                         int* returnSize, int** returnColumnSizes) {
    const long long INFLL = (1LL << 60);
    const int BIG = 2000000000; // max allowed weight for unused -1 edges

    long long *distInf = (long long *)malloc(n * sizeof(long long));
    dijkstra(n, edges, edgesSize, INFLL, source, distInf);
    if (distInf[destination] < target) {
        free(distInf);
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    if (distInf[destination] == target) {
        int **ans = (int **)malloc(edgesSize * sizeof(int *));
        *returnColumnSizes = (int *)malloc(edgesSize * sizeof(int));
        for (int i = 0; i < edgesSize; ++i) {
            ans[i] = (int *)malloc(3 * sizeof(int));
            ans[i][0] = edges[i][0];
            ans[i][1] = edges[i][1];
            int w = edges[i][2];
            if (w == -1) w = BIG;
            ans[i][2] = w;
            (*returnColumnSizes)[i] = 3;
        }
        *returnSize = edgesSize;
        free(distInf);
        return ans;
    }

    long long *distS = (long long *)malloc(n * sizeof(long long));
    long long *distT = (long long *)malloc(n * sizeof(long long));
    dijkstra(n, edges, edgesSize, 1LL, source, distS);
    dijkstra(n, edges, edgesSize, 1LL, destination, distT);

    int chosenIdx = -1;
    long long chosenWeight = -1;

    for (int i = 0; i < edgesSize; ++i) {
        if (edges[i][2] != -1) continue;
        int u = edges[i][0];
        int v = edges[i][1];

        long long du = distS[u];
        long long dv = distT[v];
        if (du != INFLL && dv != INFLL && du + dv < target) {
            chosenIdx = i;
            chosenWeight = target - du - dv;
            break;
        }
        du = distS[v];
        dv = distT[u];
        if (du != INFLL && dv != INFLL && du + dv < target) {
            chosenIdx = i;
            chosenWeight = target - du - dv;
            break;
        }
    }

    free(distInf);
    free(distS);
    free(distT);

    if (chosenIdx == -1) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int **ans = (int **)malloc(edgesSize * sizeof(int *));
    *returnColumnSizes = (int *)malloc(edgesSize * sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        ans[i] = (int *)malloc(3 * sizeof(int));
        ans[i][0] = edges[i][0];
        ans[i][1] = edges[i][1];
        int w = edges[i][2];
        if (w == -1) {
            if (i == chosenIdx) w = (int)chosenWeight;
            else w = BIG;
        }
        ans[i][2] = w;
        (*returnColumnSizes)[i] = 3;
    }
    *returnSize = edgesSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long INF = 2000000001L; // larger than allowed weight
    private const long BIG = 2000000000L; // max allowed weight

    public int[][] ModifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        int m = edges.Length;
        int[] a = new int[m];
        int[] b = new int[m];
        long[] wOrig = new long[m];
        var adj = new List<(int to, int idx)>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<(int, int)>();
        for (int i = 0; i < m; i++) {
            a[i] = edges[i][0];
            b[i] = edges[i][1];
            wOrig[i] = edges[i][2];
            adj[a[i]].Add((b[i], i));
            adj[b[i]].Add((a[i], i));
        }

        // distances without using -1 edges (treat them as INF)
        long[] distInf = Dijkstra(source, n, adj, wOrig, false);
        if (distInf[destination] < target) return Array.Empty<int[]>();
        if (distInf[destination] == target) {
            var resExact = BuildResult(m, a, b, wOrig, BIG);
            return resExact;
        }

        // distances with -1 edges as weight 1 (minimum possible)
        long[] distLowS = Dijkstra(source, n, adj, wOrig, true);
        if (distLowS[destination] > target) return Array.Empty<int[]>();
        long[] distLowD = Dijkstra(destination, n, adj, wOrig, true);

        // Try to adjust one -1 edge
        for (int i = 0; i < m; i++) {
            if (wOrig[i] != -1) continue;
            int u = a[i], v = b[i];

            // orientation u -> v
            long need = target - distLowS[u] - distLowD[v];
            if (need >= 1 && need <= BIG) {
                var finalW = new long[m];
                for (int j = 0; j < m; j++) finalW[j] = wOrig[j] == -1 ? BIG : wOrig[j];
                finalW[i] = need;
                long[] distFinal = Dijkstra(source, n, adj, finalW, false);
                if (distFinal[destination] == target) {
                    var res = BuildResult(m, a, b, finalW, 0);
                    return res;
                }
            }

            // orientation v -> u
            need = target - distLowS[v] - distLowD[u];
            if (need >= 1 && need <= BIG) {
                var finalW = new long[m];
                for (int j = 0; j < m; j++) finalW[j] = wOrig[j] == -1 ? BIG : wOrig[j];
                finalW[i] = need;
                long[] distFinal = Dijkstra(source, n, adj, finalW, false);
                if (distFinal[destination] == target) {
                    var res = BuildResult(m, a, b, finalW, 0);
                    return res;
                }
            }
        }

        return Array.Empty<int[]>();
    }

    private long[] Dijkstra(int start, int n, List<(int to, int idx)>[] adj, long[] weights, bool useOneForMinusOne) {
        var dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        var pq = new PriorityQueue<(int node, long d), long>();
        dist[start] = 0;
        pq.Enqueue((start, 0L), 0L);
        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int u = cur.node;
            long du = cur.d;
            if (du != dist[u]) continue;
            foreach (var edge in adj[u]) {
                int v = edge.to;
                int idx = edge.idx;
                long w = weights[idx];
                if (w == -1) w = useOneForMinusOne ? 1L : INF;
                long nd = du + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.Enqueue((v, nd), nd);
                }
            }
        }
        return dist;
    }

    private int[][] BuildResult(int m, int[] a, int[] b, long[] wArr, long defaultBig) {
        var res = new int[m][];
        for (int i = 0; i < m; i++) {
            long w = wArr[i];
            if (w == -1) w = defaultBig;
            res[i] = new int[] { a[i], b[i], (int)w };
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @param {number} target
 * @return {number[][]}
 */
var modifiedGraphEdges = function(n, edges, source, destination, target) {
    const MAXW = 2000000000;
    const INF_DIST = Number.MAX_SAFE_INTEGER;

    // build adjacency list with edge indices
    const adj = Array.from({length: n}, () => []);
    for (let i = 0; i < edges.length; ++i) {
        const [u, v] = edges[i];
        adj[u].push({to: v, idx: i});
        adj[v].push({to: u, idx: i});
    }

    class MinHeap {
        constructor() { this.heap = []; }
        push(item) {
            this.heap.push(item);
            this._up(this.heap.length - 1);
        }
        _up(i) {
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
            const end = this.heap.pop();
            if (this.heap.length) {
                this.heap[0] = end;
                this._down(0);
            }
            return top;
        }
        _down(i) {
            const n = this.heap.length;
            while (true) {
                let l = i * 2 + 1, r = l + 1, smallest = i;
                if (l < n && this.heap[l][0] < this.heap[smallest][0]) smallest = l;
                if (r < n && this.heap[r][0] < this.heap[smallest][0]) smallest = r;
                if (smallest === i) break;
                [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
                i = smallest;
            }
        }
        isEmpty() { return this.heap.length === 0; }
    }

    const dijkstra = (start, wts) => {
        const dist = new Array(n).fill(INF_DIST);
        dist[start] = 0;
        const heap = new MinHeap();
        heap.push([0, start]);
        while (!heap.isEmpty()) {
            const [d, u] = heap.pop();
            if (d !== dist[u]) continue;
            for (const {to: v, idx} of adj[u]) {
                const w = wts[idx];
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    heap.push([nd, v]);
                }
            }
        }
        return dist;
    };

    // original weights
    const origW = edges.map(e => e[2]);

    // 1) shortest distance without using -1 edges (treat them as very large)
    let curW = origW.slice();
    for (let i = 0; i < curW.length; ++i) {
        if (curW[i] === -1) curW[i] = MAXW;
    }
    const distNoMod = dijkstra(source, curW)[destination];
    if (distNoMod < target) return [];

    // 2) shortest distance with all -1 edges set to 1
    curW = origW.slice();
    for (let i = 0; i < curW.length; ++i) {
        if (curW[i] === -1) curW[i] = 1;
    }
    const distMinFromSrc = dijkstra(source, curW);
    const distMinToDst = dijkstra(destination, curW);
    if (distMinFromSrc[destination] > target) return [];

    // 3) try to adjust one -1 edge
    for (let i = 0; i < edges.length; ++i) {
        if (origW[i] !== -1) continue;
        const [u, v] = edges[i];

        // orientation u -> v
        let need = target - distMinFromSrc[u] - distMinToDst[v];
        if (need >= 1 && need <= MAXW) {
            const testW = origW.slice();
            for (let j = 0; j < testW.length; ++j) {
                if (testW[j] === -1) testW[j] = (j === i ? need : MAXW);
            }
            const finalDist = dijkstra(source, testW)[destination];
            if (finalDist === target) {
                return edges.map((e, idx) => {
                    let w = e[2];
                    if (w === -1) w = (idx === i ? need : MAXW);
                    return [e[0], e[1], w];
                });
            }
        }

        // orientation v -> u
        need = target - distMinFromSrc[v] - distMinToDst[u];
        if (need >= 1 && need <= MAXW) {
            const testW = origW.slice();
            for (let j = 0; j < testW.length; ++j) {
                if (testW[j] === -1) testW[j] = (j === i ? need : MAXW);
            }
            const finalDist = dijkstra(source, testW)[destination];
            if (finalDist === target) {
                return edges.map((e, idx) => {
                    let w = e[2];
                    if (w === -1) w = (idx === i ? need : MAXW);
                    return [e[0], e[1], w];
                });
            }
        }
    }

    // no solution found
    return [];
};
```

## Typescript

```typescript
function modifiedGraphEdges(
    n: number,
    edges: number[][],
    source: number,
    destination: number,
    target: number
): number[][] {
    const INF = 1e18;
    const MAX_W = 2_000_000_000;

    // Build adjacency list with given weight selector
    const buildAdj = (weightFn: (w: number) => number): Array<Array<[number, number]>> => {
        const adj: Array<Array<[number, number]>> = Array.from({ length: n }, () => []);
        for (const [u, v, w] of edges) {
            const wt = weightFn(w);
            if (wt >= 0) { // ignore edges with weight set to -1 when we want to omit them
                adj[u].push([v, wt]);
                adj[v].push([u, wt]);
            }
        }
        return adj;
    };

    // Dijkstra without heap (n <= 100)
    const dijkstra = (start: number, adj: Array<Array<[number, number]>>): number[] => {
        const dist = new Array(n).fill(INF);
        const visited = new Array(n).fill(false);
        dist[start] = 0;
        for (let i = 0; i < n; ++i) {
            let u = -1;
            let best = INF;
            for (let v = 0; v < n; ++v) {
                if (!visited[v] && dist[v] < best) {
                    best = dist[v];
                    u = v;
                }
            }
            if (u === -1) break;
            visited[u] = true;
            for (const [to, w] of adj[u]) {
                if (dist[to] > dist[u] + w) {
                    dist[to] = dist[u] + w;
                }
            }
        }
        return dist;
    };

    // 1. Distances using only known positive edges (ignore -1)
    const adjKnown = buildAdj((w) => (w === -1 ? -1 : w));
    const ds = dijkstra(source, adjKnown);
    if (ds[destination] < target) return [];

    // If already exactly target, set all -1 to large value and return
    if (ds[destination] === target) {
        const res = edges.map((e) => (e[2] === -1 ? [e[0], e[1], MAX_W] : [...e]));
        return res;
    }

    // 2. Distances when all -1 edges are weight 1
    const adjMin = buildAdj((w) => (w === -1 ? 1 : w));
    const dmin = dijkstra(source, adjMin);
    if (dmin[destination] > target) return [];

    // 3. Distances from destination using only known edges (for convenience)
    const dt = dijkstra(destination, adjKnown);

    // Prepare answer copy
    const ans: number[][] = edges.map((e) => e.slice());

    let found = false;
    for (let i = 0; i < edges.length; ++i) {
        if (edges[i][2] !== -1) continue;
        const u = edges[i][0];
        const v = edges[i][1];

        // try direction u -> v
        if (ds[u] < INF && dt[v] < INF) {
            const need = target - ds[u] - dt[v];
            if (need >= 1 && need <= MAX_W) {
                ans[i][2] = need;
                found = true;
                break;
            }
        }
        // try direction v -> u
        if (ds[v] < INF && dt[u] < INF) {
            const need = target - ds[v] - dt[u];
            if (need >= 1 && need <= MAX_W) {
                ans[i][2] = need;
                found = true;
                break;
            }
        }
    }

    if (!found) return [];

    // Set remaining -1 edges to large weight
    for (let i = 0; i < ans.length; ++i) {
        if (ans[i][2] === -1) ans[i][2] = MAX_W;
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
     * @param Integer $source
     * @param Integer $destination
     * @param Integer $target
     * @return Integer[][]
     */
    function modifiedGraphEdges($n, $edges, $source, $destination, $target) {
        $INF = 1 << 60;               // large enough for "infinite"
        $BIG = 2000000000;            // maximum allowed weight

        // Dijkstra with custom weights
        $dijkstra = function($n, $edges, $src, $customWeights, $defaultMinusOneWeight) use ($INF) {
            // build adjacency list
            $adj = array_fill(0, $n, []);
            foreach ($edges as $idx => $e) {
                [$u, $v, $w] = $e;
                if ($w == -1) {
                    $weight = $defaultMinusOneWeight;
                    if (isset($customWeights[$idx])) {
                        $weight = $customWeights[$idx];
                    }
                } else {
                    $weight = $w;
                }
                $adj[$u][] = [$v, $weight];
                $adj[$v][] = [$u, $weight];
            }

            // simple O(n^2) Dijkstra (n <= 100)
            $dist = array_fill(0, $n, $INF);
            $vis  = array_fill(0, $n, false);
            $dist[$src] = 0;
            for ($i = 0; $i < $n; $i++) {
                $u = -1;
                $best = $INF;
                for ($j = 0; $j < $n; $j++) {
                    if (!$vis[$j] && $dist[$j] < $best) {
                        $best = $dist[$j];
                        $u = $j;
                    }
                }
                if ($u == -1) break;
                $vis[$u] = true;
                foreach ($adj[$u] as $edge) {
                    [$v, $wgt] = $edge;
                    if (!$vis[$v] && $dist[$u] + $wgt < $dist[$v]) {
                        $dist[$v] = $dist[$u] + $wgt;
                    }
                }
            }
            return $dist;
        };

        // 1) shortest distance without using -1 edges (set them to huge)
        $distNoMinus = $dijkstra($n, $edges, $source, [], $INF);
        if ($distNoMinus[$destination] < $target) {
            return [];
        }

        // 2) distances when all -1 edges are weight 1
        $distFromSrc = $dijkstra($n, $edges, $source, [], 1);
        $distFromDst = $dijkstra($n, $edges, $destination, [], 1);
        if ($distFromSrc[$destination] > $target) {
            return [];
        }

        // Try to adjust one -1 edge
        foreach ($edges as $idx => $e) {
            [$u, $v, $w] = $e;
            if ($w != -1) continue;

            // option 1: path source->u + w + v->dest
            $need = $target - $distFromSrc[$u] - $distFromDst[$v];
            if ($need >= 1 && $need <= $BIG) {
                $custom = [$idx => $need];
                $finalDist = $dijkstra($n, $edges, $source, $custom, $BIG);
                if ($finalDist[$destination] == $target) {
                    // build answer
                    $ans = $edges;
                    foreach ($ans as $i => $edge) {
                        if ($edge[2] == -1) {
                            $ans[$i][2] = $custom[$idx] ?? $BIG;
                        }
                    }
                    return $ans;
                }
            }

            // option 2: path source->v + w + u->dest
            $need = $target - $distFromSrc[$v] - $distFromDst[$u];
            if ($need >= 1 && $need <= $BIG) {
                $custom = [$idx => $need];
                $finalDist = $dijkstra($n, $edges, $source, $custom, $BIG);
                if ($finalDist[$destination] == $target) {
                    // build answer
                    $ans = $edges;
                    foreach ($ans as $i => $edge) {
                        if ($edge[2] == -1) {
                            $ans[$i][2] = $custom[$idx] ?? $BIG;
                        }
                    }
                    return $ans;
                }
            }
        }

        // No suitable edge found
        return [];
    }
}
```

## Swift

```swift
class Solution {
    func modifiedGraphEdges(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int, _ target: Int) -> [[Int]] {
        let INF_WEIGHT: Int64 = 2_000_000_000
        var u = [Int](), v = [Int](), wOrig = [Int]()
        for e in edges {
            u.append(e[0])
            v.append(e[1])
            wOrig.append(e[2])
        }
        let m = edges.count
        
        func buildAdj(_ weights: [Int64]) -> [[(to: Int, weight: Int64)]] {
            var adj = Array(repeating: [(to: Int, weight: Int64)](), count: n)
            for i in 0..<m {
                let a = u[i], b = v[i]
                let w = weights[i]
                adj[a].append((b, w))
                adj[b].append((a, w))
            }
            return adj
        }
        
        func dijkstra(_ start: Int, _ adj: [[(to: Int, weight: Int64)]]) -> [Int64] {
            var dist = [Int64](repeating: INF_WEIGHT, count: n)
            var visited = [Bool](repeating: false, count: n)
            dist[start] = 0
            for _ in 0..<n {
                var vtx = -1
                var best = INF_WEIGHT
                for i in 0..<n where !visited[i] && dist[i] < best {
                    best = dist[i]
                    vtx = i
                }
                if vtx == -1 { break }
                visited[vtx] = true
                for e in adj[vtx] {
                    let nd = dist[vtx] + e.weight
                    if nd < dist[e.to] {
                        dist[e.to] = nd
                    }
                }
            }
            return dist
        }
        
        // 1) shortest path without using any -1 edges (treat them as INF)
        var weightsNoMod = [Int64](repeating: INF_WEIGHT, count: m)
        for i in 0..<m where wOrig[i] != -1 {
            weightsNoMod[i] = Int64(wOrig[i])
        }
        let adjNoMod = buildAdj(weightsNoMod)
        let distNoMod = dijkstra(source, adjNoMod)
        if distNoMod[destination] < Int64(target) {
            return []
        }
        
        // 2) shortest path with all -1 edges set to 1
        var weightsMin = [Int64](repeating: 1, count: m)
        for i in 0..<m where wOrig[i] != -1 {
            weightsMin[i] = Int64(wOrig[i])
        }
        let adjMin = buildAdj(weightsMin)
        let distFromSource = dijkstra(source, adjMin)
        let curDist = distFromSource[destination]
        if curDist > Int64(target) {
            return []
        }
        let distFromDest = dijkstra(destination, adjMin)
        
        var resultEdges = edges
        
        // Try to adjust a single -1 edge
        for i in 0..<m where wOrig[i] == -1 {
            // direction u -> v
            var need = Int64(target) - distFromSource[u[i]] - distFromDest[v[i]]
            if need >= 1 && need <= INF_WEIGHT {
                var testWeights = [Int64](repeating: INF_WEIGHT, count: m)
                for j in 0..<m where wOrig[j] != -1 {
                    testWeights[j] = Int64(wOrig[j])
                }
                testWeights[i] = need
                let adjTest = buildAdj(testWeights)
                let d = dijkstra(source, adjTest)[destination]
                if d == Int64(target) {
                    for j in 0..<m where wOrig[j] == -1 {
                        resultEdges[j][2] = (j == i) ? Int(need) : Int(INF_WEIGHT)
                    }
                    return resultEdges
                }
            }
            // direction v -> u
            need = Int64(target) - distFromSource[v[i]] - distFromDest[u[i]]
            if need >= 1 && need <= INF_WEIGHT {
                var testWeights = [Int64](repeating: INF_WEIGHT, count: m)
                for j in 0..<m where wOrig[j] != -1 {
                    testWeights[j] = Int64(wOrig[j])
                }
                testWeights[i] = need
                let adjTest = buildAdj(testWeights)
                let d = dijkstra(source, adjTest)[destination]
                if d == Int64(target) {
                    for j in 0..<m where wOrig[j] == -1 {
                        resultEdges[j][2] = (j == i) ? Int(need) : Int(INF_WEIGHT)
                    }
                    return resultEdges
                }
            }
        }
        
        // If current minimal distance already equals target, keep all -1 edges as 1
        if curDist == Int64(target) {
            for i in 0..<m where wOrig[i] == -1 {
                resultEdges[i][2] = 1
            }
            return resultEdges
        }
        
        return []
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    private data class Node(val dist: Long, val v: Int)

    fun modifiedGraphEdges(
        n: Int,
        edges: Array<IntArray>,
        source: Int,
        destination: Int,
        target: Int
    ): Array<IntArray> {
        val m = edges.size
        val us = IntArray(m)
        val vs = IntArray(m)
        val origW = IntArray(m)
        for (i in 0 until m) {
            us[i] = edges[i][0]
            vs[i] = edges[i][1]
            origW[i] = edges[i][2]
        }

        // adjacency list: pair of neighbor node and edge index
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (i in 0 until m) {
            val u = us[i]
            val v = vs[i]
            adj[u].add(Pair(v, i))
            adj[v].add(Pair(u, i))
        }

        val INF_WEIGHT = 2_000_000_000L
        val INF_DIST = Long.MAX_VALUE / 4

        fun dijkstra(start: Int, weights: LongArray): Pair<LongArray, IntArray> {
            val dist = LongArray(n) { INF_DIST }
            val pred = IntArray(n) { -1 }
            val pq = PriorityQueue<Node>(compareBy { it.dist })
            dist[start] = 0L
            pq.add(Node(0L, start))
            while (pq.isNotEmpty()) {
                val cur = pq.poll()
                if (cur.dist != dist[cur.v]) continue
                for ((to, idx) in adj[cur.v]) {
                    val w = weights[idx]
                    val nd = cur.dist + w
                    if (nd < dist[to]) {
                        dist[to] = nd
                        pred[to] = idx
                        pq.add(Node(nd, to))
                    }
                }
            }
            return Pair(dist, pred)
        }

        // 1) shortest path without using -1 edges (set them huge)
        val curWeight = LongArray(m)
        for (i in 0 until m) {
            curWeight[i] = if (origW[i] == -1) INF_WEIGHT else origW[i].toLong()
        }
        var (distNo, _) = dijkstra(source, curWeight)
        if (distNo[destination] < target.toLong()) return arrayOf()

        // 2) shortest path with all -1 edges set to 1
        for (i in 0 until m) {
            curWeight[i] = if (origW[i] == -1) 1L else origW[i].toLong()
        }
        val (distFromSrc, pred) = dijkstra(source, curWeight)
        val minDist = distFromSrc[destination]
        if (minDist > target.toLong()) return arrayOf()
        if (minDist == target.toLong()) {
            // all -1 become 1
            val ans = Array(m) { IntArray(3) }
            for (i in 0 until m) {
                val w = if (origW[i] == -1) 1 else origW[i]
                ans[i][0] = us[i]
                ans[i][1] = vs[i]
                ans[i][2] = w
            }
            return ans
        }

        // distances from destination with weight=1 for unknown edges
        val (distToDest, _) = dijkstra(destination, curWeight)

        // reconstruct one shortest path and try to adjust a -1 edge on it
        var node = destination
        var candidateIdx = -1
        var neededWeight = 0L
        while (node != source) {
            val eIdx = pred[node]
            if (eIdx == -1) break
            val u = us[eIdx]
            val v = vs[eIdx]
            val prev = if (u == node) v else u
            if (origW[eIdx] == -1) {
                val need = target.toLong() - (distFromSrc[prev] + distToDest[node])
                if (need >= 1 && need <= INF_WEIGHT) {
                    candidateIdx = eIdx
                    neededWeight = need
                    break
                }
            }
            node = prev
        }

        if (candidateIdx == -1) return arrayOf()

        // set final weights: chosen edge gets neededWeight, others -1 become large
        for (i in 0 until m) {
            curWeight[i] = when {
                origW[i] != -1 -> origW[i].toLong()
                i == candidateIdx -> neededWeight
                else -> INF_WEIGHT
            }
        }

        val (finalDist, _) = dijkstra(source, curWeight)
        if (finalDist[destination] != target.toLong()) return arrayOf()

        // build answer
        val ans = Array(m) { IntArray(3) }
        for (i in 0 until m) {
            val w = when {
                origW[i] != -1 -> origW[i]
                i == candidateIdx -> neededWeight.toInt()
                else -> INF_WEIGHT.toInt()
            }
            ans[i][0] = us[i]
            ans[i][1] = vs[i]
            ans[i][2] = w
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  static const int _INF_WEIGHT = 2000000000;
  static const int _INF_DIST = 1 << 60;

  List<List<int>> modifiedGraphEdges(int n, List<List<int>> edges, int source,
      int destination, int target) {
    int m = edges.length;
    // original weights
    List<int> origW = List.filled(m, 0);
    for (int i = 0; i < m; ++i) origW[i] = edges[i][2];

    // adjacency list of edge indices
    List<List<int>> adj = List.generate(n, (_) => []);
    for (int i = 0; i < m; ++i) {
      int u = edges[i][0];
      int v = edges[i][1];
      adj[u].add(i);
      adj[v].add(i);
    }

    // helper Dijkstra
    List<int> dijkstra(int start, List<int> w) {
      List<int> dist = List.filled(n, _INF_DIST);
      List<bool> vis = List.filled(n, false);
      dist[start] = 0;
      for (int iter = 0; iter < n; ++iter) {
        int u = -1;
        int best = _INF_DIST;
        for (int i = 0; i < n; ++i) {
          if (!vis[i] && dist[i] < best) {
            best = dist[i];
            u = i;
          }
        }
        if (u == -1) break;
        vis[u] = true;
        for (int ei in adj[u]) {
          int a = edges[ei][0];
          int b = edges[ei][1];
          int v = a ^ b ^ u; // other endpoint
          int weight = w[ei];
          if (weight >= _INF_DIST) continue;
          int nd = dist[u] + weight;
          if (nd < dist[v]) {
            dist[v] = nd;
          }
        }
      }
      return dist;
    }

    // low weights (treat -1 as huge)
    List<int> lowW = List.filled(m, 0);
    for (int i = 0; i < m; ++i) {
      lowW[i] = origW[i] == -1 ? _INF_DIST : origW[i];
    }
    int lowDist = dijkstra(source, lowW)[destination];
    if (lowDist < target) return [];

    // high weights (treat -1 as 1)
    List<int> highW = List.filled(m, 0);
    for (int i = 0; i < m; ++i) {
      highW[i] = origW[i] == -1 ? 1 : origW[i];
    }
    int highDist = dijkstra(source, highW)[destination];
    if (highDist > target) return [];

    // If already equal, set all -1 to large weight and return
    if (highDist == target) {
      for (int i = 0; i < m; ++i) {
        if (origW[i] == -1) edges[i][2] = _INF_WEIGHT;
      }
      return edges;
    }

    // distances from source and destination with weight=1 for unknowns
    List<int> ds = dijkstra(source, highW);
    List<int> dt = dijkstra(destination, highW);

    int chosenIdx = -1;
    int neededWeight = -1;

    for (int i = 0; i < m; ++i) {
      if (origW[i] != -1) continue;
      int u = edges[i][0];
      int v = edges[i][1];

      // direction u -> v
      if (ds[u] != _INF_DIST && dt[v] != _INF_DIST) {
        long sum = ds[u] + 1 + dt[v];
        if (sum < target) {
          int w = target - ds[u] - dt[v];
          if (w >= 1 && w <= _INF_WEIGHT) {
            chosenIdx = i;
            neededWeight = w;
            break;
          }
        }
      }
      // direction v -> u
      if (ds[v] != _INF_DIST && dt[u] != _INF_DIST) {
        long sum = ds[v] + 1 + dt[u];
        if (sum < target) {
          int w = target - ds[v] - dt[u];
          if (w >= 1 && w <= _INF_WEIGHT) {
            chosenIdx = i;
            neededWeight = w;
            break;
          }
        }
      }
    }

    if (chosenIdx == -1) return [];

    // Build final weight array
    List<int> finalW = List.filled(m, 0);
    for (int i = 0; i < m; ++i) {
      if (origW[i] != -1) {
        finalW[i] = origW[i];
      } else if (i == chosenIdx) {
        finalW[i] = neededWeight;
      } else {
        finalW[i] = _INF_WEIGHT;
      }
    }

    int finalDist = dijkstra(source, finalW)[destination];
    if (finalDist != target) return [];

    // Apply to edges list
    for (int i = 0; i < m; ++i) {
      if (origW[i] == -1) edges[i][2] = finalW[i];
    }
    return edges;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type Edge struct {
	to  int
	idx int
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

const INF int64 = 1 << 60

func dijkstra(src int, n int, adj [][]Edge, curWeight []int64) ([]int64, []int) {
	dist := make([]int64, n)
	parent := make([]int, n)
	for i := 0; i < n; i++ {
		dist[i] = INF
		parent[i] = -1
	}
	pq := &PriorityQueue{}
	heap.Init(pq)
	dist[src] = 0
	heap.Push(pq, Item{node: src, dist: 0})
	for pq.Len() > 0 {
		it := heap.Pop(pq).(Item)
		if it.dist != dist[it.node] {
			continue
		}
		u := it.node
		for _, e := range adj[u] {
			w := curWeight[e.idx]
			v := e.to
			nd := it.dist + w
			if nd < dist[v] {
				dist[v] = nd
				parent[v] = e.idx
				heap.Push(pq, Item{node: v, dist: nd})
			}
		}
	}
	return dist, parent
}

func modifiedGraphEdges(n int, edges [][]int, source int, destination int, target int) [][]int {
	m := len(edges)
	origW := make([]int64, m)
	for i, e := range edges {
		origW[i] = int64(e[2])
	}
	adj := make([][]Edge, n)
	for i, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], Edge{to: v, idx: i})
		adj[v] = append(adj[v], Edge{to: u, idx: i})
	}
	// First Dijkstra: treat -1 as INF
	curWeight := make([]int64, m)
	for i := 0; i < m; i++ {
		if origW[i] == -1 {
			curWeight[i] = INF
		} else {
			curWeight[i] = origW[i]
		}
	}
	dist0, _ := dijkstra(source, n, adj, curWeight)
	if dist0[destination] < int64(target) {
		return [][]int{}
	}
	if dist0[destination] == int64(target) {
		res := make([][]int, m)
		for i, e := range edges {
			w := e[2]
			if w == -1 {
				w = 2000000000
			}
			res[i] = []int{e[0], e[1], w}
		}
		return res
	}
	// Second Dijkstra: treat -1 as 1
	curWeight = make([]int64, m)
	for i := 0; i < m; i++ {
		if origW[i] == -1 {
			curWeight[i] = 1
		} else {
			curWeight[i] = origW[i]
		}
	}
	dist1, parent := dijkstra(source, n, adj, curWeight)
	if dist1[destination] > int64(target) {
		return [][]int{}
	}
	if dist1[destination] == int64(target) {
		res := make([][]int, m)
		for i, e := range edges {
			w := e[2]
			if w == -1 {
				w = 2000000000
			}
			res[i] = []int{e[0], e[1], w}
		}
		return res
	}
	// Reconstruct one shortest path from source to destination
	pathEdges := []int{}
	node := destination
	for node != source {
		eIdx := parent[node]
		if eIdx == -1 {
			break
		}
		pathEdges = append(pathEdges, eIdx)
		u, v := edges[eIdx][0], edges[eIdx][1]
		if node == v {
			node = u
		} else {
			node = v
		}
	}
	for _, eIdx := range pathEdges {
		if origW[eIdx] != -1 {
			continue
		}
		delta := int64(target) - dist1[destination]
		newWeight := 1 + delta
		cur2 := make([]int64, m)
		copy(cur2, curWeight)
		cur2[eIdx] = newWeight
		for i := 0; i < m; i++ {
			if origW[i] == -1 && i != eIdx {
				cur2[i] = INF
			}
		}
		distCheck, _ := dijkstra(source, n, adj, cur2)
		if distCheck[destination] == int64(target) {
			res := make([][]int, m)
			for i, e := range edges {
				w := e[2]
				if w == -1 {
					if i == eIdx {
						w = int(newWeight)
					} else {
						w = 2000000000
					}
				}
				res[i] = []int{e[0], e[1], w}
			}
			return res
		}
	}
	return [][]int{}
}
```

## Ruby

```ruby
def modified_graph_edges(n, edges, source, destination, target)
  INF_WEIGHT = 2_000_000_000
  unknown_idxs = []
  edges.each_with_index { |e, i| unknown_idxs << i if e[2] == -1 }

  dijkstra = lambda do |start, assigned|
    inf_dist = (1 << 60)
    dist = Array.new(n, inf_dist)
    visited = Array.new(n, false)
    dist[start] = 0
    loop do
      u = -1
      min = inf_dist
      n.times do |i|
        if !visited[i] && dist[i] < min
          min = dist[i]
          u = i
        end
      end
      break if u == -1
      visited[u] = true
      edges.each_with_index do |e, idx|
        a, b, w = e
        weight = (w == -1) ? assigned[idx] : w
        next if weight.nil?
        if a == u && !visited[b]
          nd = dist[u] + weight
          dist[b] = nd if nd < dist[b]
        elsif b == u && !visited[a]
          nd = dist[u] + weight
          dist[a] = nd if nd < dist[a]
        end
      end
    end
    dist
  end

  assign_inf = Array.new(edges.size, nil)
  unknown_idxs.each { |i| assign_inf[i] = INF_WEIGHT }
  dist_low = dijkstra.call(source, assign_inf)

  return [] if dist_low[destination] < target

  if dist_low[destination] == target
    return edges.map { |e| e[2] == -1 ? [e[0], e[1], INF_WEIGHT] : e }
  end

  assign_one = Array.new(edges.size, nil)
  unknown_idxs.each { |i| assign_one[i] = 1 }
  dist_one_src = dijkstra.call(source, assign_one)
  return [] if dist_one_src[destination] > target
  dist_one_dst = dijkstra.call(destination, assign_one)

  unknown_idxs.each do |idx|
    a, b, _ = edges[idx]

    need = target - dist_one_src[a] - dist_one_dst[b]
    if need > 0 && need <= INF_WEIGHT
      final_assign = Array.new(edges.size, nil)
      unknown_idxs.each { |i| final_assign[i] = (i == idx) ? need : INF_WEIGHT }
      final_dist = dijkstra.call(source, final_assign)[destination]
      if final_dist == target
        return edges.map.with_index do |e, i|
          e[2] == -1 ? [e[0], e[1], final_assign[i]] : e
        end
      end
    end

    need = target - dist_one_src[b] - dist_one_dst[a]
    if need > 0 && need <= INF_WEIGHT
      final_assign = Array.new(edges.size, nil)
      unknown_idxs.each { |i| final_assign[i] = (i == idx) ? need : INF_WEIGHT }
      final_dist = dijkstra.call(source, final_assign)[destination]
      if final_dist == target
        return edges.map.with_index do |e, i|
          e[2] == -1 ? [e[0], e[1], final_assign[i]] : e
        end
      end
    end
  end

  []
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

object Solution {
  def modifiedGraphEdges(n: Int, edges: Array[Array[Int]], source: Int, destination: Int, target: Int): Array[Array[Int]] = {
    val INF_ASSIGN: Long = 2000000000L          // weight for unused -1 edges
    val BIG: Long = (1L << 60)                 // effectively infinity for Dijkstra

    def buildAdj(weightForMinusOne: Long): Array[ArrayBuffer[(Int, Long)]] = {
      val adj = Array.fill(n)(new ArrayBuffer[(Int, Long)]())
      for (i <- edges.indices) {
        val a = edges(i)(0)
        val b = edges(i)(1)
        val wOrig = edges(i)(2)
        val w = if (wOrig == -1) weightForMinusOne else wOrig.toLong
        adj(a).append((b, w))
        adj(b).append((a, w))
      }
      adj
    }

    def dijkstra(start: Int, adj: Array[ArrayBuffer[(Int, Long)]]): Array[Long] = {
      val dist = Array.fill[Long](n)(BIG)
      val pq = new java.util.PriorityQueue[(Long, Int)](Ordering.by(_._1))
      dist(start) = 0L
      pq.offer((0L, start))
      while (!pq.isEmpty) {
        val cur = pq.poll()
        val d = cur._1
        val u = cur._2
        if (d != dist(u)) {
          // outdated entry
        } else {
          for ((v, w) <- adj(u)) {
            if (w >= BIG) {
              // effectively ignore this edge
            } else {
              val nd = d + w
              if (nd < dist(v)) {
                dist(v) = nd
                pq.offer((nd, v))
              }
            }
          }
        }
      }
      dist
    }

    // 1. Shortest distance without using any -1 edges (treat them as huge)
    val adjInf = buildAdj(BIG)
    val distInf = dijkstra(source, adjInf)
    if (distInf(destination) < target.toLong) return Array.empty[Array[Int]]
    if (distInf(destination) == target.toLong) {
      // any assignment with large weights works
      return edges.map { e =>
        if (e(2) == -1) Array(e(0), e(1), INF_ASSIGN.toInt) else e.clone()
      }
    }

    // 2. Shortest distances when all -1 edges have weight 1
    val adjMin = buildAdj(1L)
    val ds = dijkstra(source, adjMin)
    if (ds(destination) > target.toLong) return Array.empty[Array[Int]]
    val dt = dijkstra(destination, adjMin)

    // Find a modifiable edge to set exact needed weight
    var chosenIdx = -1
    var needWeight: Long = 0L
    for (i <- edges.indices if chosenIdx == -1 && edges(i)(2) == -1) {
      val u = edges(i)(0)
      val v = edges(i)(1)

      var need = target.toLong - ds(u) - dt(v)
      if (need > 0 && need <= INF_ASSIGN) {
        chosenIdx = i
        needWeight = need
      } else {
        need = target.toLong - ds(v) - dt(u)
        if (need > 0 && need <= INF_ASSIGN) {
          chosenIdx = i
          needWeight = need
        }
      }
    }

    if (chosenIdx == -1) return Array.empty[Array[Int]]

    // Assign final weights
    val finalWeights = new Array[Long](edges.length)
    for (i <- edges.indices) {
      if (edges(i)(2) != -1) finalWeights(i) = edges(i)(2).toLong
      else finalWeights(i) = INF_ASSIGN
    }
    finalWeights(chosenIdx) = needWeight

    // Verify the resulting shortest path equals target
    val adjFinal = Array.fill(n)(new ArrayBuffer[(Int, Long)]())
    for (i <- edges.indices) {
      val a = edges(i)(0)
      val b = edges(i)(1)
      val w = finalWeights(i)
      adjFinal(a).append((b, w))
      adjFinal(b).append((a, w))
    }
    val finalDist = dijkstra(source, adjFinal)
    if (finalDist(destination) != target.toLong) return Array.empty[Array[Int]]

    // Build result array
    edges.indices.map { i =>
      Array(edges(i)(0), edges(i)(1), finalWeights(i).toInt)
    }.toArray
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub struct Solution;

impl Solution {
    pub fn modified_graph_edges(
        n: i32,
        edges: Vec<Vec<i32>>,
        source: i32,
        destination: i32,
        target: i32,
    ) -> Vec<Vec<i32>> {
        let n_usize = n as usize;
        let m = edges.len();
        let src = source as usize;
        let dst = destination as usize;
        const INF: i64 = 1_i64 << 60;
        const BIG: i64 = 2_000_000_000;

        // store original data
        let mut u: Vec<usize> = Vec::with_capacity(m);
        let mut v: Vec<usize> = Vec::with_capacity(m);
        let mut orig_w: Vec<i64> = Vec::with_capacity(m);
        for e in &edges {
            u.push(e[0] as usize);
            v.push(e[1] as usize);
            orig_w.push(e[2] as i64);
        }

        // adjacency list with edge indices
        let mut adj: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n_usize];
        for idx in 0..m {
            let a = u[idx];
            let b = v[idx];
            adj[a].push((b, idx));
            adj[b].push((a, idx));
        }

        // Dijkstra from destination ignoring -1 edges (treat as INF)
        fn dijkstra(
            start: usize,
            n: usize,
            adj: &Vec<Vec<(usize, usize)>>,
            orig_w: &Vec<i64>,
            treat_unknown_as_inf: bool,
        ) -> Vec<i64> {
            const INF: i64 = 1_i64 << 60;
            let mut dist = vec![INF; n];
            let mut heap = BinaryHeap::new();
            dist[start] = 0;
            heap.push((Reverse(0_i64), start));
            while let Some(((Reverse(d), u))) = heap.pop() {
                if d != dist[u] {
                    continue;
                }
                for &(v, idx) in &adj[u] {
                    let w = orig_w[idx];
                    let weight = if w == -1 && treat_unknown_as_inf { INF } else { w };
                    if weight >= INF {
                        continue;
                    }
                    let nd = d + weight;
                    if nd < dist[v] {
                        dist[v] = nd;
                        heap.push((Reverse(nd), v));
                    }
                }
            }
            dist
        }

        // distances from each node to destination using only known edges
        let dist_to_dst = dijkstra(dst, n_usize, &adj, &orig_w, true);

        if dist_to_dst[src] < target as i64 {
            return vec![];
        }
        if dist_to_dst[src] == target as i64 {
            // set all -1 to BIG
            let mut res: Vec<Vec<i32>> = Vec::with_capacity(m);
            for i in 0..m {
                let w = if orig_w[i] == -1 { BIG } else { orig_w[i] };
                res.push(vec![u[i] as i32, v[i] as i32, w as i32]);
            }
            return res;
        }

        // Dijkstra from source with unknown edges weight = 1 (minimum)
        let mut min_w: Vec<i64> = orig_w.clone();
        for w in &mut min_w {
            if *w == -1 {
                *w = 1;
            }
        }
        let dist_min = dijkstra(src, n_usize, &adj, &min_w, false);
        if dist_min[dst] > target as i64 {
            return vec![];
        }

        // Modified Dijkstra to assign appropriate weight
        let mut cur_w: Vec<i64> = orig_w.clone(); // -1 for unknown not yet assigned
        let mut dist = vec![INF; n_usize];
        let mut heap = BinaryHeap::new();
        dist[src] = 0;
        heap.push((Reverse(0_i64), src));

        while let Some(((Reverse(d), u))) = heap.pop() {
            if d != dist[u] {
                continue;
            }
            for &(v, idx) in &adj[u] {
                let weight = if orig_w[idx] != -1 {
                    orig_w[idx]
                } else {
                    // unknown edge
                    if cur_w[idx] == -1 {
                        // try to set a suitable weight
                        let need = target as i64 - d - dist_to_dst[v];
                        if need > 0 && need <= BIG {
                            cur_w[idx] = need;
                        } else {
                            cur_w[idx] = INF; // make it unusable for shortest path
                        }
                    }
                    cur_w[idx]
                };
                if weight >= INF {
                    continue;
                }
                let nd = d + weight;
                if nd < dist[v] {
                    dist[v] = nd;
                    heap.push((Reverse(nd), v));
                }
            }
        }

        if dist[dst] != target as i64 {
            return vec![];
        }

        // finalize edge weights
        let mut result: Vec<Vec<i32>> = Vec::with_capacity(m);
        for i in 0..m {
            let w = if orig_w[i] != -1 {
                orig_w[i]
            } else {
                let assigned = cur_w[i];
                if assigned == -1 || assigned >= INF {
                    BIG
                } else {
                    assigned
                }
            };
            result.push(vec![u[i] as i32, v[i] as i32, w as i32]);
        }
        result
    }
}
```

## Racket

```racket
(define INF 1000000000000000) ; sufficiently large

;; Dijkstra with O(n^2), returns a vector of distances from src
(define (dijkstra n adj edge-weights src)
  (let ([dist (make-vector n INF)]
        [vis  (make-vector n #f)])
    (vector-set! dist src 0)
    (for ([iter (in-range n)])
      (let ([u -1]
            [best INF])
        (for ([i (in-range n)])
          (when (and (not (vector-ref vis i))
                     (< (vector-ref dist i) best))
            (set! u i)
            (set! best (vector-ref dist i))))
        (when (= u -1) (break))
        (vector-set! vis u #t)
        (for ([nbr-pair (vector-ref adj u)])
          (let* ([v   (first nbr-pair)]
                 [eid (second nbr-pair)]
                 [w   (vector-ref edge-weights eid)])
            (when (< w INF)
              (let ([nd (+ (vector-ref dist u) w)])
                (when (< nd (vector-ref dist v))
                  (vector-set! dist v nd))))))))
    dist))

;; Main function
(define/contract (modified-graph-edges n edges source destination target)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?
      (listof (listof exact-integer?)))
  (let* ([m (length edges)]
         [adj (make-vector n '())]
         ;; original weights vector
         [orig-w (make-vector m -1)])
    ;; build adjacency and orig weight vectors
    (for ([i (in-range m)] [e edges])
      (let* ([a (list-ref e 0)]
             [b (list-ref e 1)]
             [w (list-ref e 2)])
        (vector-set! orig-w i w)
        (vector-set! adj a (cons (list b i) (vector-ref adj a)))
        (vector-set! adj b (cons (list a i) (vector-ref adj b)))))
    ;; helper to create weight vector with given replacement for -1 edges
    (define (make-weights replace-fn)
      (let ([vec (make-vector m INF)])
        (for ([i (in-range m)])
          (let ([w (vector-ref orig-w i)])
            (if (= w -1)
                (vector-set! vec i (replace-fn i))
                (vector-set! vec i w))))
        vec))
    ;; first run: treat unknown edges as INF
    (define weights-inf (make-weights (lambda (_) INF)))
    (define ds (dijkstra n adj weights-inf source))
    (define d0 (vector-ref ds destination))
    (cond
      [(< d0 target) '()] ; impossible, even with huge weights distance too small
      [else
       ;; if already equal, set all -1 to large allowed value and return
       (if (= d0 target)
           (let ([final-w (make-vector m 0)])
             (for ([i (in-range m)])
               (let ([w (vector-ref orig-w i)])
                 (vector-set! final-w i (if (= w -1) 2000000000 w))))
             (map (lambda (e idx)
                    (list (list-ref e 0) (list-ref e 1) (vector-ref final-w idx)))
                  edges (in-range m)))
           ;; otherwise need to adjust one edge
           (begin
             ;; distances from destination using INF weights
             (define dt (dijkstra n adj weights-inf destination))
             
             (let loop ([i 0] [found #f] [chosen-weight 0] [chosen-eid -1])
               (if (or found (= i m))
                   (if (not found)
                       '() ; no suitable edge
                       ;; construct final weights, verify distance equals target
                       (let* ([final-weights (make-vector m INF)])
                         (for ([j (in-range m)])
                           (let ([w (vector-ref orig-w j)])
                             (cond
                               [(= w -1)
                                (if (= j chosen-eid)
                                    (vector-set! final-weights j chosen-weight)
                                    (vector-set! final-weights j 2000000000))]
                               [else (vector-set! final-weights j w)])))
                         (define d-final (vector-ref (dijkstra n adj final-weights source) destination))
                         (if (= d-final target)
                             (let ([result (map (lambda (e idx)
                                                  (list (list-ref e 0)
                                                        (list-ref e 1)
                                                        (vector-ref final-weights idx)))
                                                edges (in-range m))])
                               result)
                             '()))))
                   (let* ([w (vector-ref orig-w i)])
                     (if (not (= w -1))
                         (loop (+ i 1) found chosen-weight chosen-eid)
                         (let* ([a (list-ref (list-ref edges i) 0)]
                                [b (list-ref (list-ref edges i) 1)]
                                [da (vector-ref ds a)]
                                [db (vector-ref ds b)]
                                [dta (vector-ref dt a)]
                                [dtb (vector-ref dt b)])
                           ;; orientation a->b
                           (if (and (< da INF) (< dtb INF))
                               (let ([need (- target (+ da dtb))])
                                 (if (and (>= need 1) (<= need 2000000000))
                                     (loop (+ i 1) #t need i)
                                     (begin
                                       ;; orientation b->a
                                       (if (and (< db INF) (< dta INF))
                                           (let ([need2 (- target (+ db dta))])
                                             (if (and (>= need2 1) (<= need2 2000000000))
                                                 (loop (+ i 1) #t need2 i)
                                                 (loop (+ i 1) found chosen-weight chosen-eid)))
                                           (loop (+ i 1) found chosen-weight chosen-eid)))))
                               ;; try other orientation directly
                               (if (and (< db INF) (< dta INF))
                                   (let ([need (- target (+ db dta))])
                                     (if (and (>= need 1) (<= need 2000000000))
                                         (loop (+ i 1) #t need i)
                                         (loop (+ i 1) found chosen-weight chosen-eid)))
                                   (loop (+ i 1) found chosen-weight chosen-eid)))))))))]))))
```

## Erlang

```erlang
-spec modified_graph_edges(N :: integer(), Edges :: [[integer()]], Source :: integer(), Destination :: integer(), Target :: integer()) -> [[integer()]].
modified_graph_edges(N, Edges, Source, Destination, Target) ->
    EdgeInfos = [list_to_tuple(E) || E <- Edges],
    M = length(EdgeInfos),
    Adj = build_adj(N, EdgeInfos),

    INF_W = 2000000000,
    %% weights with -1 as INF
    WeightsInf = array:from_list([case W of -1 -> INF_W; _ -> W end || {_U,_V,W} <- EdgeInfos]),
    DistInf = dijkstra_dist(N, Source, Destination, Adj, WeightsInf),
    if DistInf < Target ->
            [];
       true ->
            %% weights with -1 as 1
            WeightsOne = array:from_list([case W of -1 -> 1; _ -> W end || {_U,_V,W} <- EdgeInfos]),
            DistOne = dijkstra_dist(N, Source, Destination, Adj, WeightsOne),
            if DistOne > Target ->
                    [];
               true ->
                    Ds = dijkstra_all(N, Source, Adj, WeightsOne),
                    Dt = dijkstra_all(N, Destination, Adj, WeightsOne),

                    case array:get(Destination, Ds) of
                        D when D == Target ->
                            FinalW = array:from_list([case W of -1 -> INF_W; _ -> W end || {_U,_V,W} <- EdgeInfos]),
                            build_result(EdgeInfos, FinalW);
                        _ ->
                            case find_candidate(EdgeInfos, Ds, Dt, Target, INF_W) of
                                none ->
                                    [];
                                {IdxChosen, NewWeight} ->
                                    FinalList = [case W of
                                                    -1 ->
                                                        if I == IdxChosen -> NewWeight; true -> INF_W end;
                                                    _ -> W
                                                end || {{_U,_V,W},I} <- lists:zip(EdgeInfos, lists:seq(0,M-1))],
                                    FinalW = array:from_list(FinalList),
                                    case dijkstra_dist(N, Source, Destination, Adj, FinalW) of
                                        Target -> build_result(EdgeInfos, FinalW);
                                        _ -> []
                                    end
                            end
                    end
            end
    end.

%% Build adjacency list as array where each entry is [{Neighbor, EdgeIdx}]
build_adj(N, EdgeInfos) ->
    Empty = array:new(N, [{default, []}]),
    build_adj_loop(EdgeInfos, 0, Empty).

build_adj_loop([], _Idx, Adj) -> Adj;
build_adj_loop([{U,V,_W}|Rest], Idx, Adj) ->
    L1 = array:get(U, Adj),
    Adj1 = array:set(U, [{V,Idx}|L1], Adj),
    L2 = array:get(V, Adj1),
    Adj2 = array:set(V, [{U,Idx}|L2], Adj1),
    build_adj_loop(Rest, Idx+1, Adj2).

%% Dijkstra returning distance from Src to Dest
dijkstra_dist(N, Src, Dest, Adj, Weights) ->
    DistArr = dijkstra_all(N, Src, Adj, Weights),
    array:get(Dest, DistArr).

%% Dijkstra returning full distance array
dijkstra_all(N, Src, Adj, Weights) ->
    Inf = 1 bsl 60,
    Dist0 = array:new(N, [{default, Inf}]),
    Dist1 = array:set(Src, 0, Dist0),
    Visited0 = array:new(N, [{default,false}]),
    dijkstra_loop(N, Adj, Weights, Dist1, Visited0).

dijkstra_loop(N, Adj, Weights, Dist, Visited) ->
    case find_min_unvisited(N, Dist, Visited) of
        none -> Dist;
        {U, DU} ->
            Visited1 = array:set(U, true, Visited),
            Neigh = array:get(U, Adj),
            Dist1 = relax_neighbors(Neigh, DU, Dist, Weights),
            dijkstra_loop(N, Adj, Weights, Dist1, Visited1)
    end.

find_min_unvisited(N, Dist, Visited) ->
    find_min_unvisited(0, N-1, none, 1 bsl 60, Dist, Visited).

find_min_unvisited(I, Max, none, BestDist, _Dist, _Visited) when I > Max -> none;
find_min_unvisited(I, Max, none, BestDist, Dist, Visited) ->
    case array:get(I, Visited) of
        true -> find_min_unvisited(I+1, Max, none, BestDist, Dist, Visited);
        false ->
            D = array:get(I, Dist),
            if D < BestDist ->
                    find_min_unvisited(I+1, Max, {I,D}, D, Dist, Visited);
               true ->
                    find_min_unvisited(I+1, Max, none, BestDist, Dist, Visited)
            end
    end;
find_min_unvisited(I, Max, {BestIdx,BestDist}, CurBest, Dist, Visited) when I > Max -> {BestIdx,BestDist};
find_min_unvisited(I, Max, {BestIdx,BestDist}, CurBest, Dist, Visited) ->
    case array:get(I, Visited) of
        true -> find_min_unvisited(I+1, Max, {BestIdx,BestDist}, CurBest, Dist, Visited);
        false ->
            D = array:get(I, Dist),
            if D < CurBest ->
                    find_min_unvisited(I+1, Max, {I,D}, D, Dist, Visited);
               true ->
                    find_min_unvisited(I+1, Max, {BestIdx,BestDist}, CurBest, Dist, Visited)
            end
    end.

relax_neighbors([], _DU, Dist, _Weights) -> Dist;
relax_neighbors([{V,EdgeIdx}|Rest], DU, Dist, Weights) ->
    W = array:get(EdgeIdx, Weights),
    NewDist = DU + W,
    OldDist = array:get(V, Dist),
    Dist1 = if NewDist < OldDist -> array:set(V, NewDist, Dist); true -> Dist end,
    relax_neighbors(Rest, DU, Dist1, Weights).

%% Find candidate edge to adjust
find_candidate(EdgeInfos, Ds, Dt, Target, INF_W) ->
    find_candidate_loop(lists:zip(EdgeInfos, lists:seq(0,length(EdgeInfos)-1)), Target, INF_W, Ds, Dt).

find_candidate_loop([], _Target, _INF_W, _Ds, _Dt) -> none;
find_candidate_loop([{{U,V,W},Idx}|Rest], Target, INF_W, Ds, Dt) ->
    case W of
        -1 ->
            Du = array:get(U, Ds),
            Dv = array:get(V, Dt),
            Need = Target - Du - Dv,
            if Need >= 1, Need =< INF_W -> {Idx,Need};
               true ->
                   Dvu = array:get(V, Ds),
                   Dut = array:get(U, Dt),
                   Need2 = Target - Dvu - Dut,
                   if Need2 >= 1, Need2 =< INF_W -> {Idx,Need2};
                      true -> find_candidate_loop(Rest, Target, INF_W, Ds, Dt)
                   end
            end;
        _ -> find_candidate_loop(Rest, Target, INF_W, Ds, Dt)
    end.

%% Build final result list of edges with modified weights
build_result(EdgeInfos, WeightsArr) ->
    [ [U,V,array:get(I,WeightsArr)] || {{U,V,_},I} <- lists:zip(EdgeInfos, lists:seq(0,length(EdgeInfos)-1)) ].
```

## Elixir

```elixir
defmodule Solution do
  @spec modified_graph_edges(
          n :: integer,
          edges :: [[integer]],
          source :: integer,
          destination :: integer,
          target :: integer
        ) :: [[integer]]
  def modified_graph_edges(n, edges, source, destination, target) do
    max_weight = 2_000_000_000

    m = length(edges)

    # original weights list
    orig_weights =
      Enum.map(edges, fn [_a, _b, w] -> w end)

    # build adjacency map {node => [{neighbor, edge_idx}, ...]}
    adj =
      Enum.with_index(edges)
      |> Enum.reduce(%{}, fn {[a, b, _w], idx}, acc ->
        acc
        |> Map.update(a, [{b, idx}], fn lst -> [{b, idx} | lst] end)
        |> Map.update(b, [{a, idx}], fn lst -> [{a, idx} | lst] end)
      end)

    # helper Dijkstra (O(n^2) enough for n<=100)
    dijkstra = fn weights, src ->
      inf = 1 <<< 60

      dist = List.duplicate(inf, n) |> List.replace_at(src, 0)
      visited = List.duplicate(false, n)

      dijkstra_loop = fn
        0, _dist, _vis -> :ok
        cnt, cur_dist, cur_vis ->
          # find unvisited node with minimal distance
          {u, min_d} =
            Enum.with_index(cur_dist)
            |> Enum.reduce({nil, inf}, fn {d, i}, {best_u, best_d} ->
              if not Enum.at(cur_vis, i) and d < best_d, do: {i, d}, else: {best_u, best_d}
            end)

          if u == nil or min_d == inf do
            :ok
          else
            cur_vis = List.replace_at(cur_vis, u, true)
            cur_dist =
              Enum.reduce(Map.get(adj, u, []), cur_dist, fn {v, eidx}, dacc ->
                w = Enum.at(weights, eidx)
                nd = min_d + w
                if nd < Enum.at(dacc, v) do
                  List.replace_at(dacc, v, nd)
                else
                  dacc
                end
              end)

            dijkstra_loop.(cnt - 1, cur_dist, cur_vis)
          end
      end

      dijkstra_loop.(n, dist, visited)
      |> elem(0) # final distances list
    end

    # distances with minimal possible weights (replace -1 by 1)
    min_weights = Enum.map(orig_weights, fn w -> if w == -1, do: 1, else: w end)
    dist_s_min = dijkstra.(min_weights, source)

    if Enum.at(dist_s_min, destination) > target do
      []
    else
      # distances with maximal weights (replace -1 by large value)
      max_weights =
        Enum.map(orig_weights, fn w -> if w == -1, do: max_weight, else: w end)

      dist_s_max = dijkstra.(max_weights, source)

      if Enum.at(dist_s_max, destination) < target do
        []
      else
        # exact match with minimal weights
        if Enum.at(dist_s_min, destination) == target do
          Enum.map(edges, fn [a, b, w] ->
            if w == -1, do: [a, b, max_weight], else: [a, b, w]
          end)
        else
          # distances from destination with minimal weights
          dist_t_min = dijkstra.(min_weights, destination)

          found =
            Enum.with_index(edges)
            |> Enum.reduce_while(nil, fn {[a, b, _w] = _edge, idx}, _acc ->
              if orig_weights |> Enum.at(idx) != -1 do
                {:cont, nil}
              else
                needed1 = target - Enum.at(dist_s_min, a) - Enum.at(dist_t_min, b)
                cond1 = needed1 > 0 and needed1 <= max_weight

                needed2 = target - Enum.at(dist_s_min, b) - Enum.at(dist_t_min, a)
                cond2 = needed2 > 0 and needed2 <= max_weight

                test_edge = fn need ->
                  # build current weights: all unknown -> max_weight except this edge
                  cur_weights =
                    Enum.map(0..(m - 1), fn i ->
                      w = Enum.at(orig_weights, i)
                      if w != -1, do: w, else: max_weight
                    end)

                  cur_weights = List.replace_at(cur_weights, idx, need)

                  dist = dijkstra.(cur_weights, source)

                  if Enum.at(dist, destination) == target do
                    # construct result edges
                    res =
                      Enum.map(0..(m - 1), fn i ->
                        [ea, eb, _ew] = Enum.at(edges, i)
                        ow = Enum.at(orig_weights, i)

                        cond do
                          ow != -1 -> [ea, eb, ow]
                          i == idx -> [ea, eb, need]
                          true -> [ea, eb, max_weight]
                        end
                      end)

                    {:halt, res}
                  else
                    :continue
                  end
                end

                cond do
                  cond1 ->
                    case test_edge.(needed1) do
                      {:halt, res} -> {:halt, res}
                      _ ->
                        if cond2 do
                          case test_edge.(needed2) do
                            {:halt, res} -> {:halt, res}
                            _ -> {:cont, nil}
                          end
                        else
                          {:cont, nil}
                        end
                    end

                  cond2 ->
                    case test_edge.(needed2) do
                      {:halt, res} -> {:halt, res}
                      _ -> {:cont, nil}
                    end

                  true ->
                    {:cont, nil}
                end
              end
            end)

          case found do
            nil -> []
            result -> result
          end
        end
      end
    end
  end
end
```

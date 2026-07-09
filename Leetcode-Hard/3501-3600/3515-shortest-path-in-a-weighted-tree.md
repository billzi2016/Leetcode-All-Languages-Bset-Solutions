# 3515. Shortest Path in a Weighted Tree

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Fenwick {
    int n;
    vector<long long> bit;
public:
    Fenwick(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 2, 0);
    }
    void add(int idx, long long val) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    }
    long long sum(int idx) const {
        long long res = 0;
        for (; idx > 0; idx -= idx & -idx) res += bit[idx];
        return res;
    }
};

class Solution {
public:
    vector<int> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        // adjacency list with edge id
        vector<vector<pair<int,int>>> adj(n + 1);
        int m = edges.size(); // n-1
        vector<int> w(m);
        for (int i = 0; i < m; ++i) {
            int u = edges[i][0], v = edges[i][1], wt = edges[i][2];
            adj[u].push_back({v, i});
            adj[v].push_back({u, i});
            w[i] = wt;
        }
        // map edge (min,max) -> id
        unordered_map<long long,int> edgeId;
        edgeId.reserve(m*2);
        for (int i = 0; i < m; ++i) {
            int a = edges[i][0], b = edges[i][1];
            if (a > b) swap(a,b);
            long long key = ((long long)a << 32) | (unsigned long long)b;
            edgeId[key] = i;
        }
        // euler tour
        vector<int> tin(n + 1), tout(n + 1), childNode(m, -1);
        vector<long long> dist(n + 1, 0);
        int timer = 1;
        function<void(int,int)> dfs = [&](int u, int p){
            tin[u] = timer++;
            for (auto [v, eid] : adj[u]) {
                if (v == p) continue;
                childNode[eid] = v; // v is deeper
                dist[v] = dist[u] + w[eid];
                dfs(v, u);
            }
            tout[u] = timer - 1;
        };
        dfs(1, 0);
        
        Fenwick bit(n+2);
        vector<int> answer;
        for (const auto& q : queries) {
            if (q[0] == 1) { // update edge weight
                int u = q[1], v = q[2], newW = q[3];
                int a = min(u, v), b = max(u, v);
                long long key = ((long long)a << 32) | (unsigned long long)b;
                int eid = edgeId[key];
                long long delta = (long long)newW - w[eid];
                if (delta != 0) {
                    int child = childNode[eid]; // deeper node
                    bit.add(tin[child], delta);
                    bit.add(tout[child] + 1, -delta);
                    w[eid] = newW;
                }
            } else { // query distance to x
                int x = q[1];
                long long curDist = dist[x] + bit.sum(tin[x]);
                answer.push_back((int)curDist);
            }
        }
        return answer;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class BIT {
        int n;
        long[] bit;
        BIT(int n) {
            this.n = n;
            bit = new long[n + 2];
        }
        void add(int idx, long val) {
            for (int i = idx; i <= n; i += i & -i) {
                bit[i] += val;
            }
        }
        void rangeAdd(int l, int r, long val) {
            add(l, val);
            if (r + 1 <= n) add(r + 1, -val);
        }
        long query(int idx) {
            long res = 0;
            for (int i = idx; i > 0; i -= i & -i) {
                res += bit[i];
            }
            return res;
        }
    }

    public int[] treeQueries(int n, int[][] edges, int[][] queries) {
        List<int[]>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        int[] parent = new int[n + 1];
        int[] depth = new int[n + 1];
        long[] dist0 = new long[n + 1];
        long[] weightToParent = new long[n + 1];
        int[] tin = new int[n + 1];
        int[] tout = new int[n + 1];

        int timer = 0;
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{1, 0}); // node, state (0=enter,1=exit)
        parent[1] = 0;
        depth[1] = 0;
        dist0[1] = 0;

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int node = cur[0];
            int state = cur[1];
            if (state == 0) {
                tin[node] = ++timer;
                stack.push(new int[]{node, 1}); // exit later
                for (int[] nb : adj[node]) {
                    int to = nb[0], w = nb[1];
                    if (to == parent[node]) continue;
                    parent[to] = node;
                    depth[to] = depth[node] + 1;
                    dist0[to] = dist0[node] + w;
                    weightToParent[to] = w;
                    stack.push(new int[]{to, 0});
                }
            } else {
                tout[node] = timer;
            }
        }

        BIT bit = new BIT(n);
        List<Integer> answers = new ArrayList<>();

        for (int[] q : queries) {
            if (q[0] == 1) { // update edge weight
                int u = q[1], v = q[2];
                int wNew = q[3];
                int child = depth[u] > depth[v] ? u : v;
                long delta = (long) wNew - weightToParent[child];
                if (delta != 0) {
                    weightToParent[child] = wNew;
                    bit.rangeAdd(tin[child], tout[child], delta);
                }
            } else { // query distance
                int x = q[1];
                long res = dist0[x] + bit.query(tin[x]);
                answers.add((int) res);
            }
        }

        int[] result = new int[answers.size()];
        for (int i = 0; i < answers.size(); i++) {
            result[i] = answers.get(i);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def treeQueries(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(300000)

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [0] * (n + 1)
        depth = [0] * (n + 1)
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        dist0 = [0] * (n + 1)

        # edge_key -> current weight, and child node of that edge
        edge_weight = {}
        child_of_edge = {}

        timer = 0

        def dfs(u, p):
            nonlocal timer
            timer += 1
            tin[u] = timer
            for v, w in adj[u]:
                if v == p:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                dist0[v] = dist0[u] + w
                key = (u, v) if u < v else (v, u)
                edge_weight[key] = w
                child_of_edge[key] = v  # v is deeper than u
                dfs(v, u)
            tout[u] = timer

        dfs(1, 0)

        class BIT:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 2)

            def _add(self, i, delta):
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i

            def range_add(self, l, r, delta):
                self._add(l, delta)
                if r + 1 <= self.n:
                    self._add(r + 1, -delta)

            def query(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s

        bit = BIT(n)
        ans = []

        for q in queries:
            if q[0] == 1:
                _, u, v, wnew = q
                key = (u, v) if u < v else (v, u)
                child = child_of_edge[key]
                old = edge_weight[key]
                delta = wnew - old
                if delta != 0:
                    edge_weight[key] = wnew
                    bit.range_add(tin[child], tout[child], delta)
            else:  # query type 2
                _, x = q
                ans.append(dist0[x] + bit.query(tin[x]))

        return ans
```

## Python3

```python
import sys
from typing import List

class BIT:
    def __init__(self, n: int):
        self.n = n + 2
        self.bit = [0] * (self.n)

    def add(self, idx: int, val: int):
        i = idx
        while i < self.n:
            self.bit[i] += val
            i += i & -i

    def prefix_sum(self, idx: int) -> int:
        res = 0
        i = idx
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        sys.setrecursionlimit(300000)
        adj = [[] for _ in range(n + 1)]
        edge_weight = {}
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            key = (u, v) if u < v else (v, u)
            edge_weight[key] = w

        parent = [0] * (n + 1)
        depth = [0] * (n + 1)
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        dist_root = [0] * (n + 1)

        timer = 0
        def dfs(u: int, p: int):
            nonlocal timer
            timer += 1
            tin[u] = timer
            for v, w in adj[u]:
                if v == p:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                dist_root[v] = dist_root[u] + w
                dfs(v, u)
            tout[u] = timer

        dfs(1, 0)

        bit = BIT(n)

        ans = []
        for q in queries:
            if q[0] == 1:
                _, u, v, new_w = q
                key = (u, v) if u < v else (v, u)
                old_w = edge_weight[key]
                delta = new_w - old_w
                if delta != 0:
                    edge_weight[key] = new_w
                    # determine child node (deeper one)
                    if parent[u] == v:
                        child = u
                    elif parent[v] == u:
                        child = v
                    else:
                        # should not happen in a tree
                        continue
                    bit.add(tin[child], delta)
                    bit.add(tout[child] + 1, -delta)
            else:  # query type 2
                _, x = q
                cur = dist_root[x] + bit.prefix_sum(tin[x])
                ans.append(cur)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    long long key;
    int val;
} HashEntry;

static inline unsigned int hash_idx(long long key, unsigned int mask) {
    unsigned long long h = (unsigned long long)key;
    h ^= h >> 33;
    return (unsigned int)(h & mask);
}

static void hashmap_put(HashEntry *table, unsigned int mask, long long key, int val) {
    unsigned int idx = hash_idx(key, mask);
    while (table[idx].key != -1 && table[idx].key != key) {
        idx = (idx + 1) & mask;
    }
    table[idx].key = key;
    table[idx].val = val;
}

static int hashmap_get(HashEntry *table, unsigned int mask, long long key) {
    unsigned int idx = hash_idx(key, mask);
    while (table[idx].key != -1) {
        if (table[idx].key == key) return table[idx].val;
        idx = (idx + 1) & mask;
    }
    return -1; // should not happen
}

/* Fenwick Tree for range add / point query */
static void bit_add(long long *bit, int n, int idx, long long val) {
    while (idx <= n) {
        bit[idx] += val;
        idx += idx & -idx;
    }
}
static long long bit_sum(long long *bit, int idx) {
    long long s = 0;
    while (idx > 0) {
        s += bit[idx];
        idx -= idx & -idx;
    }
    return s;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* treeQueries(int n, int** edges, int edgesSize, int* edgesColSize,
                 int** queries, int queriesSize, int* queriesColSize,
                 int* returnSize) {
    /* adjacency list */
    int m = edgesSize;
    int maxE = 2 * m;
    int *to = (int *)malloc(sizeof(int) * maxE);
    int *next = (int *)malloc(sizeof(int) * maxE);
    int *eid = (int *)malloc(sizeof(int) * maxE);
    int *head = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i <= n; ++i) head[i] = -1;
    int ecnt = 0;

    /* edge data */
    int *curWeight = (int *)malloc(sizeof(int) * m);
    int *edgeChild = (int *)malloc(sizeof(int) * m);

    /* hashmap for unordered pair -> edge index */
    unsigned int hsize = 1;
    while (hsize < (unsigned)(m * 4)) hsize <<= 1; // power of two
    unsigned int hmask = hsize - 1;
    HashEntry *htable = (HashEntry *)malloc(sizeof(HashEntry) * hsize);
    for (unsigned int i = 0; i < hsize; ++i) htable[i].key = -1;

    for (int i = 0; i < m; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];
        curWeight[i] = w;
        /* adjacency */
        to[ecnt] = v; eid[ecnt] = i; next[ecnt] = head[u]; head[u] = ecnt++; 
        to[ecnt] = u; eid[ecnt] = i; next[ecnt] = head[v]; head[v] = ecnt++;
        /* hashmap key (min,max) */
        int a = u < v ? u : v;
        int b = u < v ? v : u;
        long long key = ((long long)a << 32) | (unsigned int)b;
        hashmap_put(htable, hmask, key, i);
    }

    /* Euler tour arrays */
    int *tin = (int *)malloc(sizeof(int) * (n + 1));
    int *tout = (int *)malloc(sizeof(int) * (n + 1));
    long long *distInit = (long long *)malloc(sizeof(long long) * (n + 1));
    int *depth = (int *)malloc(sizeof(int) * (n + 1));
    int *parent = (int *)malloc(sizeof(int) * (n + 1));

    /* iterative DFS */
    int timer = 0;
    int stackSize = 2 * n + 5;
    int *stkNode = (int *)malloc(sizeof(int) * stackSize);
    int *stkPar = (int *)malloc(sizeof(int) * stackSize);
    char *stkState = (char *)malloc(sizeof(char) * stackSize);
    int sp = 0;
    stkNode[sp] = 1; stkPar[sp] = 0; stkState[sp] = 0; ++sp;

    depth[1] = 0;
    distInit[1] = 0;
    parent[1] = 0;

    while (sp) {
        --sp;
        int node = stkNode[sp];
        int par = stkPar[sp];
        char state = stkState[sp];
        if (state == 0) {
            tin[node] = ++timer;
            /* push exit marker */
            stkNode[sp] = node; stkPar[sp] = par; stkState[sp] = 1; ++sp;
            for (int e = head[node]; e != -1; e = next[e]) {
                int nb = to[e];
                if (nb == par) continue;
                parent[nb] = node;
                depth[nb] = depth[node] + 1;
                distInit[nb] = distInit[node] + curWeight[eid[e]];
                edgeChild[eid[e]] = nb; /* child is deeper */
                stkNode[sp] = nb; stkPar[sp] = node; stkState[sp] = 0; ++sp;
            }
        } else {
            tout[node] = timer;
        }
    }

    /* Fenwick tree */
    int BITN = n + 2;
    long long *bit = (long long *)calloc(BITN + 1, sizeof(long long));

    int *answers = (int *)malloc(sizeof(int) * queriesSize);
    int ansCnt = 0;

    for (int i = 0; i < queriesSize; ++i) {
        int type = queries[i][0];
        if (type == 1) {
            int u = queries[i][1];
            int v = queries[i][2];
            int wnew = queries[i][3];
            int a = u < v ? u : v;
            int b = u < v ? v : u;
            long long key = ((long long)a << 32) | (unsigned int)b;
            int eidx = hashmap_get(htable, hmask, key);
            long long delta = (long long)wnew - curWeight[eidx];
            if (delta != 0) {
                curWeight[eidx] = wnew;
                int child = edgeChild[eidx];
                bit_add(bit, BITN, tin[child], delta);
                bit_add(bit, BITN, tout[child] + 1, -delta);
            }
        } else { /* type == 2 */
            int x = queries[i][1];
            long long res = distInit[x] + bit_sum(bit, tin[x]);
            answers[ansCnt++] = (int)res;
        }
    }

    *returnSize = ansCnt;

    free(to);
    free(next);
    free(eid);
    free(head);
    free(curWeight);
    free(edgeChild);
    free(htable);
    free(tin);
    free(tout);
    free(distInit);
    free(depth);
    free(parent);
    free(stkNode);
    free(stkPar);
    free(stkState);
    free(bit);

    return answers;
}
```

## Csharp

```csharp
public class Solution {
    public int[] TreeQueries(int n, int[][] edges, int[][] queries) {
        // adjacency list
        var adj = new List<(int to, int w, int id)>[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new List<(int, int, int)>();
        int m = edges.Length;
        long[] curWeight = new long[m];
        var edgeMap = new Dictionary<long, int>(m * 2);
        for (int i = 0; i < m; i++) {
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            adj[u].Add((v, w, i));
            adj[v].Add((u, w, i));
            curWeight[i] = w;
            long key = ((long)Math.Min(u, v) << 32) | (uint)Math.Max(u, v);
            edgeMap[key] = i;
        }

        int[] parent = new int[n + 1];
        int[] tin = new int[n + 1];
        int[] tout = new int[n + 1];
        long[] distInit = new long[n + 1];
        int[] childOfEdge = new int[m];

        // iterative DFS for Euler tour
        int timer = 0;
        var stack = new Stack<(int node, int par, int state)>();
        stack.Push((1, 0, 0));
        while (stack.Count > 0) {
            var cur = stack.Pop();
            int node = cur.node, par = cur.par, state = cur.state;
            if (state == 0) {
                parent[node] = par;
                tin[node] = ++timer;
                // push exit marker
                stack.Push((node, par, 1));
                foreach (var e in adj[node]) {
                    if (e.to == par) continue;
                    distInit[e.to] = distInit[node] + e.w;
                    childOfEdge[e.id] = e.to;          // deeper node is the child
                    stack.Push((e.to, node, 0));
                }
            } else {
                tout[node] = timer;
            }
        }

        var bit = new Fenwick(n + 2);
        var answers = new List<int>();

        foreach (var q in queries) {
            if (q[0] == 1) { // update edge weight
                int u = q[1], v = q[2];
                long wNew = q[3];
                long key = ((long)Math.Min(u, v) << 32) | (uint)Math.Max(u, v);
                int eid = edgeMap[key];
                long delta = wNew - curWeight[eid];
                if (delta != 0) {
                    int child = childOfEdge[eid];
                    bit.Add(tin[child], delta);
                    bit.Add(tout[child] + 1, -delta);
                    curWeight[eid] = wNew;
                }
            } else { // query distance
                int x = q[1];
                long ans = distInit[x] + bit.Sum(tin[x]);
                answers.Add((int)ans);
            }
        }

        return answers.ToArray();
    }

    private class Fenwick {
        private readonly long[] tree;
        public Fenwick(int size) {
            tree = new long[size + 1];
        }
        public void Add(int idx, long delta) {
            for (int i = idx; i < tree.Length; i += i & -i)
                tree[i] += delta;
        }
        public long Sum(int idx) {
            long res = 0;
            for (int i = idx; i > 0; i -= i & -i)
                res += tree[i];
            return res;
        }
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
var treeQueries = function(n, edges, queries) {
    // adjacency list: [neighbor, weight, edgeId]
    const adj = Array.from({length: n + 1}, () => []);
    const edgeMap = new Map(); // key "u#v" -> edge id
    for (let i = 0; i < edges.length; ++i) {
        const [u, v, w] = edges[i];
        adj[u].push([v, w, i]);
        adj[v].push([u, w, i]);
        const key = u < v ? `${u}#${v}` : `${v}#${u}`;
        edgeMap.set(key, i);
    }

    // Euler tour arrays
    const tin = new Array(n + 1);
    const tout = new Array(n + 1);
    const baseDist = new Array(n + 1).fill(0);
    const childNode = new Array(edges.length);   // deeper endpoint for each edge
    const curWeight = new Array(edges.length);   // current weight of each edge

    // iterative DFS to fill tin, tout, baseDist, childNode, curWeight
    let timer = 1;
    const stack = [[1, 0, 0]]; // [node, parent, state] state 0=enter,1=exit
    while (stack.length) {
        const [u, p, state] = stack.pop();
        if (state === 0) {
            tin[u] = timer++;
            // exit marker
            stack.push([u, p, 1]);
            for (const [v, w, eid] of adj[u]) {
                if (v === p) continue;
                baseDist[v] = baseDist[u] + w;
                curWeight[eid] = w;
                childNode[eid] = v; // v is deeper
                stack.push([v, u, 0]);
            }
        } else {
            tout[u] = timer - 1;
        }
    }

    // Fenwick tree for range add / point query (using difference array)
    class Fenwick {
        constructor(size) {
            this.n = size;
            this.bit = new Array(size + 2).fill(0);
        }
        add(idx, delta) {
            for (let i = idx; i <= this.n; i += i & -i) {
                this.bit[i] += delta;
            }
        }
        sum(idx) {
            let res = 0;
            for (let i = idx; i > 0; i -= i & -i) {
                res += this.bit[i];
            }
            return res;
        }
    }

    const fenwick = new Fenwick(n + 2); // allow index n+1

    const ans = [];
    for (const q of queries) {
        if (q[0] === 1) { // update edge weight
            const u = q[1], v = q[2], wNew = q[3];
            const key = u < v ? `${u}#${v}` : `${v}#${u}`;
            const eid = edgeMap.get(key);
            const delta = wNew - curWeight[eid];
            if (delta !== 0) {
                const child = childNode[eid];
                fenwick.add(tin[child], delta);
                fenwick.add(tout[child] + 1, -delta);
                curWeight[eid] = wNew;
            }
        } else { // query distance from root to x
            const x = q[1];
            const dist = baseDist[x] + fenwick.sum(tin[x]);
            ans.push(dist);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function treeQueries(n: number, edges: number[][], queries: number[][]): number[] {
    const adj: { to: number; w: number; idx: number }[][] = Array.from({ length: n + 1 }, () => []);
    const edgeU = new Int32Array(edges.length);
    const edgeV = new Int32Array(edges.length);
    const edgeW = new Int32Array(edges.length);
    for (let i = 0; i < edges.length; ++i) {
        const [u, v, w] = edges[i];
        edgeU[i] = u;
        edgeV[i] = v;
        edgeW[i] = w;
        adj[u].push({ to: v, w, idx: i });
        adj[v].push({ to: u, w, idx: i });
    }

    const parent = new Int32Array(n + 1);
    const dist = new Float64Array(n + 1);
    const tin = new Int32Array(n + 1);
    const tout = new Int32Array(n + 1);
    const edgeChild = new Int32Array(edges.length); // child node for each edge

    let timer = 0;
    // iterative DFS to avoid recursion depth issues
    type StackItem = { node: number; parent: number; state: 0 | 1 };
    const stack: StackItem[] = [{ node: 1, parent: 0, state: 0 }];
    while (stack.length) {
        const cur = stack.pop() as StackItem;
        if (cur.state === 0) {
            timer++;
            tin[cur.node] = timer;
            // push post-visit marker
            stack.push({ node: cur.node, parent: cur.parent, state: 1 });
            for (const e of adj[cur.node]) {
                if (e.to === cur.parent) continue;
                parent[e.to] = cur.node;
                dist[e.to] = dist[cur.node] + e.w;
                // record child for this edge
                edgeChild[e.idx] = e.to; // e.to is the deeper node
                stack.push({ node: e.to, parent: cur.node, state: 0 });
            }
        } else {
            tout[cur.node] = timer;
        }
    }

    // map from unordered edge pair to its index
    const edgeMap = new Map<string, number>();
    for (let i = 0; i < edges.length; ++i) {
        const a = edgeU[i];
        const b = edgeV[i];
        const key = a < b ? `${a}_${b}` : `${b}_${a}`;
        edgeMap.set(key, i);
    }

    class BIT {
        n: number;
        tree: Float64Array;
        constructor(n: number) {
            this.n = n;
            this.tree = new Float64Array(n + 2);
        }
        add(idx: number, val: number): void {
            for (let i = idx; i <= this.n; i += i & -i) {
                this.tree[i] += val;
            }
        }
        prefixSum(idx: number): number {
            let res = 0;
            for (let i = idx; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
        rangeAdd(l: number, r: number, val: number): void {
            if (l > r) return;
            this.add(l, val);
            if (r + 1 <= this.n) this.add(r + 1, -val);
        }
    }

    const bit = new BIT(n);
    const ans: number[] = [];

    for (const q of queries) {
        if (q[0] === 1) {
            // update edge weight
            const [, u, v, wNew] = q;
            const key = u < v ? `${u}_${v}` : `${v}_${u}`;
            const idx = edgeMap.get(key)!;
            const oldW = edgeW[idx];
            if (oldW !== wNew) {
                const delta = wNew - oldW;
                edgeW[idx] = wNew;
                const child = edgeChild[idx];
                bit.rangeAdd(tin[child], tout[child], delta);
            }
        } else {
            // query distance from root to x
            const [, x] = q;
            const res = dist[x] + bit.prefixSum(tin[x]);
            ans.push(res);
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
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function treeQueries($n, $edges, $queries) {
        // Build adjacency list
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            [$u, $v, $w] = $e;
            $adj[$u][] = [$v, $w];
            $adj[$v][] = [$u, $w];
        }

        // Iterative DFS to get parent, distance and preorder
        $parent = array_fill(0, $n + 1, 0);
        $weightToParent = array_fill(0, $n + 1, 0);
        $dist = array_fill(0, $n + 1, 0);
        $order = [];

        $stack = [1];
        while (!empty($stack)) {
            $node = array_pop($stack);
            $order[] = $node;
            foreach ($adj[$node] as $edge) {
                [$nei, $w] = $edge;
                if ($nei == $parent[$node]) continue;
                $parent[$nei] = $node;
                $weightToParent[$nei] = $w;
                $dist[$nei] = $dist[$node] + $w;
                $stack[] = $nei;
            }
        }

        // Euler tour indices
        $tin = array_fill(0, $n + 1, 0);
        $subSize = array_fill(0, $n + 1, 1);
        $cnt = count($order);
        for ($i = 0; $i < $cnt; $i++) {
            $node = $order[$i];
            $tin[$node] = $i + 1; // 1‑based
        }
        for ($i = $cnt - 1; $i > 0; $i--) { // skip root at index 0
            $node = $order[$i];
            $par = $parent[$node];
            if ($par != 0) {
                $subSize[$par] += $subSize[$node];
            }
        }
        $tout = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $tout[$i] = $tin[$i] + $subSize[$i] - 1;
        }

        // Fenwick tree supporting range add & point query
        class BIT {
            public $size;
            public $tree;
            function __construct($n) {
                $this->size = $n;
                $this->tree = array_fill(0, $n + 2, 0);
            }
            private function add($idx, $delta) {
                $n = $this->size;
                while ($idx <= $n) {
                    $this->tree[$idx] += $delta;
                    $idx += $idx & (-$idx);
                }
            }
            public function rangeAdd($l, $r, $delta) {
                $this->add($l, $delta);
                if ($r + 1 <= $this->size) $this->add($r + 1, -$delta);
            }
            public function query($idx) {
                $res = 0;
                while ($idx > 0) {
                    $res += $this->tree[$idx];
                    $idx -= $idx & (-$idx);
                }
                return $res;
            }
        }

        $bit = new BIT($n);
        $ansList = [];

        foreach ($queries as $q) {
            if ($q[0] == 1) { // update edge weight
                [$type, $u, $v, $newW] = $q;
                // child is the deeper node (has parent equal to the other)
                if ($parent[$u] == $v) {
                    $child = $u;
                } else {
                    $child = $v;
                }
                $oldW = $weightToParent[$child];
                $delta = $newW - $oldW;
                if ($delta != 0) {
                    $weightToParent[$child] = $newW;
                    $l = $tin[$child];
                    $r = $tout[$child];
                    $bit->rangeAdd($l, $r, $delta);
                }
            } else { // query distance from root
                [$type, $x] = $q;
                $curDist = $dist[$x] + $bit->query($tin[$x]);
                $ansList[] = $curDist;
            }
        }

        return $ansList;
    }
}
```

## Swift

```swift
class Solution {
    struct Fenwick {
        let n: Int
        var tree: [Int64]
        init(_ n: Int) {
            self.n = n
            self.tree = Array(repeating: 0, count: n + 2)
        }
        mutating func add(_ idx: Int, _ delta: Int64) {
            var i = idx
            while i <= n {
                tree[i] += delta
                i += i & -i
            }
        }
        mutating func rangeAdd(l: Int, r: Int, delta: Int64) {
            add(l, delta)
            if r + 1 <= n {
                add(r + 1, -delta)
            }
        }
        func query(_ idx: Int) -> Int64 {
            var res: Int64 = 0
            var i = idx
            while i > 0 {
                res += tree[i]
                i -= i & -i
            }
            return res
        }
    }

    struct EdgeInfo {
        var child: Int
        var weight: Int
    }

    func treeQueries(_ n: Int, _ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        // Build adjacency list
        var adj = [[(to: Int, w: Int)]](repeating: [], count: n + 1)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            adj[u].append((v, w))
            adj[v].append((u, w))
        }

        var parent = [Int](repeating: 0, count: n + 1)
        var tin = [Int](repeating: 0, count: n + 1)
        var tout = [Int](repeating: 0, count: n + 1)
        var dist = [Int64](repeating: 0, count: n + 1)

        var edgeMap = [UInt64: EdgeInfo]()

        // Iterative DFS for Euler tour
        var timer = 0
        var stack: [(node: Int, parent: Int, visited: Bool)] = [(1, 0, false)]
        while let last = stack.popLast() {
            let u = last.node
            let p = last.parent
            if !last.visited {
                parent[u] = p
                timer += 1
                tin[u] = timer
                // push exit marker
                stack.append((u, p, true))
                // process children
                for (v, w) in adj[u].reversed() {
                    if v == p { continue }
                    dist[v] = dist[u] + Int64(w)
                    let a = min(u, v), b = max(u, v)
                    let key = (UInt64(a) << 32) | UInt64(b)
                    edgeMap[key] = EdgeInfo(child: v, weight: w)
                    stack.append((v, u, false))
                }
            } else {
                tout[u] = timer
            }
        }

        var bit = Fenwick(n)
        var answer = [Int]()

        for q in queries {
            if q[0] == 1 {
                let u = q[1], v = q[2], wNew = q[3]
                let a = min(u, v), b = max(u, v)
                let key = (UInt64(a) << 32) | UInt64(b)
                if var info = edgeMap[key] {
                    let delta = Int64(wNew - info.weight)
                    if delta != 0 {
                        bit.rangeAdd(l: tin[info.child], r: tout[info.child], delta: delta)
                        info.weight = wNew
                        edgeMap[key] = info
                    }
                }
            } else { // query type 2
                let x = q[1]
                let res = dist[x] + bit.query(tin[x])
                answer.append(Int(res))
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun treeQueries(n: Int, edges: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val adj = Array(n + 1) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        val parent = IntArray(n + 1)
        val tin = IntArray(n + 1)
        val tout = IntArray(n + 1)
        val dist = LongArray(n + 1)
        val weightToParent = IntArray(n + 1)

        var timer = 0
        fun dfs(u: Int, p: Int, acc: Long) {
            parent[u] = p
            dist[u] = acc
            tin[u] = ++timer
            for ((v, w) in adj[u]) {
                if (v == p) continue
                weightToParent[v] = w
                dfs(v, u, acc + w)
            }
            tout[u] = timer
        }

        dfs(1, 0, 0L)

        val bit = Fenwick(n + 2)
        val answerCount = queries.count { it[0] == 2 }
        val answers = IntArray(answerCount)
        var ansIdx = 0

        for (q in queries) {
            if (q[0] == 1) {
                val u = q[1]
                val v = q[2]
                val wNew = q[3]

                val child = if (parent[u] == v) u else v
                val oldW = weightToParent[child]
                val delta = wNew - oldW
                if (delta != 0) {
                    weightToParent[child] = wNew
                    val l = tin[child]
                    val r = tout[child]
                    bit.add(l, delta.toLong())
                    bit.add(r + 1, (-delta).toLong())
                }
            } else { // type 2
                val x = q[1]
                val curDist = dist[x] + bit.sum(tin[x])
                answers[ansIdx++] = curDist.toInt()
            }
        }

        return answers
    }

    private class Fenwick(size: Int) {
        private val n = size
        private val tree = LongArray(n + 1)

        fun add(idx: Int, delta: Long) {
            var i = idx
            while (i <= n) {
                tree[i] += delta
                i += i and -i
            }
        }

        fun sum(idx: Int): Long {
            var i = idx
            var res = 0L
            while (i > 0) {
                res += tree[i]
                i -= i and -i
            }
            return res
        }
    }
}
```

## Dart

```dart
class Solution {
  List<int> treeQueries(int n, List<List<int>> edges, List<List<int>> queries) {
    // adjacency list
    List<List<List<int>>> adj = List.generate(n + 1, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1], w = e[2];
      adj[u].add([v, w]);
      adj[v].add([u, w]);
    }

    // arrays
    List<int> parent = List.filled(n + 1, 0);
    List<int> depth = List.filled(n + 1, 0);
    List<int> tin = List.filled(n + 1, 0);
    List<int> tout = List.filled(n + 1, 0);
    List<int> dist = List.filled(n + 1, 0);
    List<int> edgeWeight = List.filled(n + 1, 0); // weight from parent to node

    int timer = 0;

    class StackItem {
      int node;
      int par;
      bool processed;
      StackItem(this.node, this.par, this.processed);
    }

    List<StackItem> stack = [StackItem(1, 0, false)];
    while (stack.isNotEmpty) {
      var cur = stack.removeLast();
      if (!cur.processed) {
        // entry
        tin[cur.node] = ++timer;
        parent[cur.node] = cur.par;
        // push exit marker
        stack.add(StackItem(cur.node, cur.par, true));
        for (var nb in adj[cur.node]) {
          int v = nb[0];
          int w = nb[1];
          if (v == cur.par) continue;
          dist[v] = dist[cur.node] + w;
          edgeWeight[v] = w;
          depth[v] = depth[cur.node] + 1;
          stack.add(StackItem(v, cur.node, false));
        }
      } else {
        // exit
        tout[cur.node] = timer;
      }
    }

    // Fenwick Tree for range add / point query
    class BIT {
      int n;
      List<int> bit;
      BIT(this.n) : bit = List.filled(n + 2, 0);
      void _add(int idx, int delta) {
        for (int i = idx; i <= n; i += i & -i) {
          bit[i] += delta;
        }
      }

      void rangeAdd(int l, int r, int delta) {
        if (l > r) return;
        _add(l, delta);
        _add(r + 1, -delta);
      }

      int query(int idx) {
        int res = 0;
        for (int i = idx; i > 0; i -= i & -i) {
          res += bit[i];
        }
        return res;
      }
    }

    BIT fenwick = BIT(n + 2);

    List<int> answer = [];
    for (var q in queries) {
      if (q[0] == 1) {
        int u = q[1], v = q[2], wNew = q[3];
        int child;
        if (parent[u] == v) {
          child = u;
        } else {
          child = v;
        }
        int delta = wNew - edgeWeight[child];
        if (delta != 0) {
          edgeWeight[child] = wNew;
          fenwick.rangeAdd(tin[child], tout[child], delta);
        }
      } else {
        int x = q[1];
        int curDist = dist[x] + fenwick.query(tin[x]);
        answer.add(curDist);
      }
    }

    return answer;
  }
}
```

## Golang

```go
func treeQueries(n int, edges [][]int, queries [][]int) []int {
	type Edge struct {
		to   int
		w    int
		idx  int
	}
	adj := make([][]Edge, n+1)
	edgeWeight := make([]int, len(edges))
	edgeChild := make([]int, len(edges))
	edgeMap := make(map[int64]int)

	for i, e := range edges {
		u, v, w := e[0], e[1], e[2]
		adj[u] = append(adj[u], Edge{v, w, i})
		adj[v] = append(adj[v], Edge{u, w, i})
		edgeWeight[i] = w
		a, b := u, v
		if a > b {
			a, b = b, a
		}
		key := int64(a)<<32 | int64(b)
		edgeMap[key] = i
	}

	parent := make([]int, n+1)
	initDist := make([]int64, n+1)

	// DFS to set parent, initDist and edgeChild
	stack := []int{1}
	parent[1] = 0
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, e := range adj[v] {
			if e.to == parent[v] {
				continue
			}
			parent[e.to] = v
			initDist[e.to] = initDist[v] + int64(e.w)
			edgeChild[e.idx] = e.to // child is the deeper node
			stack = append(stack, e.to)
		}
	}

	// Euler tour for subtree intervals
	tin := make([]int, n+1)
	tout := make([]int, n+1)
	timer := 0
	type NodeIter struct {
		v int
		i int
	}
	st := []NodeIter{{1, 0}}
	visited := make([]bool, n+1)
	for len(st) > 0 {
		top := &st[len(st)-1]
		if !visited[top.v] {
			visited[top.v] = true
			timer++
			tin[top.v] = timer
		}
		if top.i < len(adj[top.v]) {
			e := adj[top.v][top.i]
			top.i++
			if e.to == parent[top.v] {
				continue
			}
			st = append(st, NodeIter{e.to, 0})
		} else {
			tout[top.v] = timer
			st = st[:len(st)-1]
		}
	}

	size := n + 2
	bit := make([]int64, size)
	add := func(idx int, val int64) {
		for i := idx; i < size; i += i & -i {
			bit[i] += val
		}
	}
	sum := func(idx int) int64 {
		res := int64(0)
		for i := idx; i > 0; i -= i & -i {
			res += bit[i]
		}
		return res
	}

	ans := []int{}
	for _, q := range queries {
		if q[0] == 1 { // update edge weight
			u, v, wnew := q[1], q[2], q[3]
			a, b := u, v
			if a > b {
				a, b = b, a
			}
			key := int64(a)<<32 | int64(b)
			idx := edgeMap[key]
			delta := int64(wnew - edgeWeight[idx])
			if delta != 0 {
				child := edgeChild[idx]
				add(tin[child], delta)
				add(tout[child]+1, -delta)
				edgeWeight[idx] = wnew
			}
		} else { // query distance
			x := q[1]
			dist := initDist[x] + sum(tin[x])
			ans = append(ans, int(dist))
		}
	}
	return ans
}
```

## Ruby

```ruby
def tree_queries(n, edges, queries)
  # Build adjacency list
  adj = Array.new(n + 1) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  parent = Array.new(n + 1, 0)
  edge_weight_to_parent = Array.new(n + 1, 0)
  tin = Array.new(n + 1, 0)
  tout = Array.new(n + 1, 0)
  base_dist = Array.new(n + 1, 0)

  timer = 0
  stack = [[1, 0, 0, 0]] # node, parent, weight_from_parent, state (0=enter,1=exit)
  while !stack.empty?
    node, par, w, st = stack.pop
    if st == 0
      parent[node] = par
      edge_weight_to_parent[node] = w
      timer += 1
      tin[node] = timer
      base_dist[node] = (par == 0 ? 0 : base_dist[par] + w)
      stack << [node, par, w, 1]
      adj[node].each do |nbr, wt|
        next if nbr == par
        stack << [nbr, node, wt, 0]
      end
    else
      tout[node] = timer
    end
  end

  # Fenwick Tree for range add / point query
  class BIT
    def initialize(n)
      @n = n
      @bit = Array.new(n + 2, 0)
    end
    def add(idx, val)
      while idx <= @n
        @bit[idx] += val
        idx += idx & -idx
      end
    end
    def sum(idx)
      res = 0
      while idx > 0
        res += @bit[idx]
        idx -= idx & -idx
      end
      res
    end
  end

  bit = BIT.new(n)

  answers = []
  queries.each do |q|
    if q[0] == 1
      _, u, v, w_new = q
      child = parent[u] == v ? u : v
      delta = w_new - edge_weight_to_parent[child]
      next if delta == 0
      edge_weight_to_parent[child] = w_new
      l = tin[child]
      r = tout[child]
      bit.add(l, delta)
      bit.add(r + 1, -delta) if r < n
    else
      _, x = q
      answers << base_dist[x] + bit.sum(tin[x])
    end
  end

  answers
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, HashMap}

  class BIT(val n: Int) {
    private val bit = new Array[Long](n + 2)
    def add(idx: Int, delta: Long): Unit = {
      var i = idx
      while (i <= n) {
        bit(i) += delta
        i += i & -i
      }
    }
    def sum(idx: Int): Long = {
      var res: Long = 0L
      var i = idx
      while (i > 0) {
        res += bit(i)
        i -= i & -i
      }
      res
    }
  }

  def treeQueries(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    // adjacency list with (neighbor, weight, edgeId)
    val adj = Array.fill(n + 1)(new ArrayBuffer[(Int, Int, Int)]())
    val m = edges.length
    val edgeU = new Array[Int](m)
    val edgeV = new Array[Int](m)
    val curWeight = new Array[Int](m)

    for (i <- 0 until m) {
      val u = edges(i)(0)
      val v = edges(i)(1)
      val w = edges(i)(2)
      edgeU(i) = u
      edgeV(i) = v
      curWeight(i) = w
      adj(u).append((v, w, i))
      adj(v).append((u, w, i))
    }

    // map unordered pair to edge id for quick lookup
    val edgeMap = new HashMap[Long, Int]()
    def key(a: Int, b: Int): Long = {
      if (a < b) a.toLong << 32 | b.toLong else b.toLong << 32 | a.toLong
    }
    for (i <- 0 until m) {
      edgeMap(key(edgeU(i), edgeV(i))) = i
    }

    // arrays for Euler tour and distances
    val in = new Array[Int](n + 1)
    val out = new Array[Int](n + 1)
    val depth = new Array[Int](n + 1)
    val parent = new Array[Int](n + 1)
    val initDist = new Array[Long](n + 1)

    // iterative DFS for Euler tour
    var timer = 0
    val stack = new ArrayBuffer[(Int, Int, Int)]() // (node, parent, state) state:0 enter,1 exit
    stack.append((1, 0, 0))
    depth(1) = 0
    initDist(1) = 0L
    while (stack.nonEmpty) {
      val (node, par, state) = stack.remove(stack.size - 1)
      if (state == 0) {
        timer += 1
        in(node) = timer
        parent(node) = par
        // push exit marker
        stack.append((node, par, 1))
        // process children
        for ((nbr, w, _) <- adj(node).reverse) { // reverse to keep original order not required
          if (nbr != par) {
            depth(nbr) = depth(node) + 1
            initDist(nbr) = initDist(node) + w
            stack.append((nbr, node, 0))
          }
        }
      } else {
        out(node) = timer
      }
    }

    // Determine child endpoint for each edge (deeper node)
    val edgeChild = new Array[Int](m)
    for (i <- 0 until m) {
      val u = edgeU(i)
      val v = edgeV(i)
      if (depth(u) > depth(v)) edgeChild(i) = u
      else edgeChild(i) = v
    }

    // BIT for range add, point query via prefix sum on in-order index
    val bit = new BIT(n + 2)

    val answers = new ArrayBuffer[Int]()

    for (q <- queries) {
      if (q(0) == 1) {
        val u = q(1)
        val v = q(2)
        val wNew = q(3)
        val eId = edgeMap(key(u, v))
        val delta = wNew - curWeight(eId)
        if (delta != 0) {
          val child = edgeChild(eId)
          // apply delta to subtree of child
          bit.add(in(child), delta.toLong)
          bit.add(out(child) + 1, -delta.toLong)
          curWeight(eId) = wNew
        }
      } else { // query type 2
        val x = q(1)
        val dist = initDist(x) + bit.sum(in(x))
        answers.append(dist.toInt)
      }
    }

    answers.toArray
  }
}
```

## Rust

```rust
use std::collections::HashMap;

struct BIT {
    n: usize,
    bit: Vec<i64>,
}
impl BIT {
    fn new(n: usize) -> Self {
        BIT { n, bit: vec![0; n + 2] }
    }
    fn add(&mut self, mut idx: usize, delta: i64) {
        while idx <= self.n {
            self.bit[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }
    fn range_add(&mut self, l: usize, r: usize, delta: i64) {
        if l > r { return; }
        self.add(l, delta);
        if r + 1 <= self.n {
            self.add(r + 1, -delta);
        }
    }
    fn sum(&self, mut idx: usize) -> i64 {
        let mut res = 0i64;
        while idx > 0 {
            res += self.bit[idx];
            idx &= idx - 1;
        }
        res
    }
}

impl Solution {
    pub fn tree_queries(n: i32, edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        // adjacency list with weight
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize + 1];
        let mut weight_map: HashMap<(usize, usize), i64> = HashMap::new();

        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as i64;
            adj[u].push((v, w));
            adj[v].push((u, w));
            let key = if u < v { (u, v) } else { (v, u) };
            weight_map.insert(key, w);
        }

        // Euler tour, parent, dist
        let mut parent = vec![0usize; n_usize + 1];
        let mut tin = vec![0usize; n_usize + 1];
        let mut tout = vec![0usize; n_usize + 1];
        let mut dist = vec![0i64; n_usize + 1];

        let mut order: usize = 0;
        // stack of (node, parent, visited_flag)
        let mut stack: Vec<(usize, usize, bool)> = Vec::new();
        stack.push((1, 0, false));

        while let Some((node, par, visited)) = stack.pop() {
            if !visited {
                parent[node] = par;
                order += 1;
                tin[node] = order;
                // push exit marker
                stack.push((node, par, true));
                // traverse children
                for &(nei, w) in adj[node].iter().rev() {
                    if nei == par { continue; }
                    dist[nei] = dist[node] + w;
                    stack.push((nei, node, false));
                }
            } else {
                tout[node] = order;
            }
        }

        let mut bit = BIT::new(n_usize + 2);
        let mut answers: Vec<i32> = Vec::new();

        for q in queries.iter() {
            if q[0] == 1 {
                let u = q[1] as usize;
                let v = q[2] as usize;
                let new_w = q[3] as i64;
                let key = if u < v { (u, v) } else { (v, u) };
                let old_w = *weight_map.get(&key).unwrap();
                let delta = new_w - old_w;
                if delta != 0 {
                    // determine which node is child
                    let child = if parent[u] == v { u } else { v };
                    bit.range_add(tin[child], tout[child], delta);
                }
                weight_map.insert(key, new_w);
            } else {
                let x = q[1] as usize;
                let cur_dist = dist[x] + bit.sum(tin[x]);
                answers.push(cur_dist as i32);
            }
        }

        answers
    }
}
```

## Racket

```racket
(define/contract (tree-queries n edges queries)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ((adj (make-vector (+ n 1) '()))                     ; adjacency list
         ;; build adjacency
         (add-edge
          (lambda (u v w)
            (vector-set! adj u (cons (cons v w) (vector-ref adj u)))
            (vector-set! adj v (cons (cons u w) (vector-ref adj v)))))
         (_ (for-each (lambda (e)
                        (let ((u (list-ref e 0))
                              (v (list-ref e 1))
                              (w (list-ref e 2)))
                          (add-edge u v w)))
                      edges))
         ;; vectors for dfs info
         (parent (make-vector (+ n 1) 0))
         (tin    (make-vector (+ n 1) 0))
         (tout   (make-vector (+ n 1) 0))
         (dist   (make-vector (+ n 1) 0))
         (weight (make-vector (+ n 1) 0))                     ; weight of edge from parent to node
         (timer 0)
         ;; iterative dfs using explicit stack
         (stack (list (list 1 0 'enter)))                    ; each frame: (node parent state)
         (process-dfs
          (lambda ()
            (let loop ((stk stack) (tmr timer))
              (if (null? stk)
                  (set! timer tmr)
                  (let* ((frame (car stk))
                         (rest  (cdr stk))
                         (node  (list-ref frame 0))
                         (par   (list-ref frame 1))
                         (state (list-ref frame 2)))
                    (cond
                      [(eq? state 'enter)
                       (set! tmr (+ tmr 1))
                       (vector-set! tin node tmr)
                       ;; push exit frame first, then children enters
                       (let ((new-stk (cons (list node par 'exit) rest)))
                         (let recur ((neighbors (vector-ref adj node)) (stk2 new-stk))
                           (if (null? neighbors)
                               (loop stk2 tmr)
                               (let* ((nb   (car neighbors))
                                      (v    (car nb))
                                      (w    (cdr nb)))
                                 (if (= v par)
                                     (recur (cdr neighbors) stk2)
                                     (begin
                                       (vector-set! parent v node)
                                       (vector-set! dist v (+ (vector-ref dist node) w))
                                       (vector-set! weight v w)
                                       (recur (cdr neighbors)
                                              (cons (list v node 'enter) stk2))))))))]
                      [else ; exit
                       (vector-set! tout node tmr)
                       (loop rest tmr)])))))))
    (process-dfs)

    ;; BIT for range add / point query
    (let* ((size (+ n 2))
           (bit  (make-vector size 0))
           (bit-add!
            (lambda (idx delta)
              (let loop ((i idx))
                (when (<= i (- size 1))
                  (vector-set! bit i (+ (vector-ref bit i) delta))
                  (loop (+ i (bitwise-and i (- i))))))))
           (range-add
            (lambda (node delta)
              (let ((l (vector-ref tin node))
                    (r (vector-ref tout node)))
                (bit-add! l delta)
                (bit-add! (+ r 1) (- delta)))))
           (bit-sum
            (lambda (idx)
              (let loop ((i idx) (acc 0))
                (if (= i 0)
                    acc
                    (loop (bitwise-and i (- i)) (+ acc (vector-ref bit i))))))))
      ;; process queries
      (let ((answers '()))
        (for-each
         (lambda (q)
           (let ((type (list-ref q 0)))
             (cond
               [(= type 1) ; update edge weight
                (let* ((u (list-ref q 1))
                       (v (list-ref q 2))
                       (neww (list-ref q 3))
                       (child (if (= (vector-ref parent u) v) u v))
                       (oldw (vector-ref weight child))
                       (delta (- neww oldw)))
                  (when (not (= delta 0))
                    (vector-set! weight child neww)
                    (range-add child delta)))]
               [(= type 2) ; query distance
                (let* ((x (list-ref q 1))
                       (ans (+ (vector-ref dist x)
                               (bit-sum (vector-ref tin x)))))
                  (set! answers (cons ans answers)))])))
         queries)
        (reverse answers)))))
```

## Erlang

```erlang
-module(solution).
-export([tree_queries/3]).

-import(array, [new/2, set/3, get/2]).

-spec tree_queries(N :: integer(), Edges :: [[integer()]], Queries :: [[integer()]]) -> [integer()].
tree_queries(N, Edges, Queries) ->
    Adj = build_adj(Edges, #{}),
    {TinArr, ToutArr, DistArr, EdgeMap} = dfs(N, Adj),
    BitTable = ets:new(bit_table, [set, private]),
    init_bit(BitTable, N + 2),
    AnswersRev = process_queries(Queries, TinArr, ToutArr, DistArr, EdgeMap, BitTable, N, []),
    lists:reverse(AnswersRev).

%% Build adjacency map
build_adj([], Adj) -> Adj;
build_adj([[U,V,W]|Rest], Adj) ->
    Adj1 = maps:update_with(U,
            fun(L) -> [{V,W}|L] end,
            [{V,W}],
            Adj),
    Adj2 = maps:update_with(V,
            fun(L) -> [{U,W}|L] end,
            [{U,W}],
            Adj1),
    build_adj(Rest, Adj2).

%% DFS to compute tin, tout, distances and edge info
dfs(N, Adj) ->
    Tin0   = array:new(N+1, {default,0}),
    Tout0  = array:new(N+1, {default,0}),
    Dist0  = array:new(N+1, {default,0}),
    EdgeMap0 = #{},
    Stack0 = [{1,0,0,0}], % {Node,Parent,State,WeightFromParent}
    {Tin, Tout, Dist, EdgeMap, _Timer} = dfs_loop(Stack0, Adj, Tin0, Tout0, Dist0, EdgeMap0, 0),
    {Tin, Tout, Dist, EdgeMap}.

dfs_loop([], _Adj, Tin, Tout, Dist, EdgeMap, Timer) ->
    {Tin, Tout, Dist, EdgeMap, Timer};
dfs_loop([{Node,Parent,State,W}|Rest], Adj, Tin, Tout, Dist, EdgeMap, Timer) ->
    case State of
        0 -> % entering node
            NewTimer = Timer + 1,
            Tin2 = array:set(Node, NewTimer, Tin),
            ParentDist = if Parent == 0 -> 0; true -> array:get(Parent, Dist) end,
            NodeDist = ParentDist + W,
            Dist2 = array:set(Node, NodeDist, Dist),

            % push exit marker
            Stack1 = [{Node,Parent,1,W}|Rest],

            Neighs = maps:get(Node, Adj, []),
            {StackChildren, EdgeMap2} = lists:foldl(
                fun({V,Wv}, {AccStk, EM}) ->
                    if V =:= Parent ->
                        {AccStk, EM};
                       true ->
                           Key = if Node < V -> {Node,V}; true -> {V,Node} end,
                           EM2 = maps:put(Key, #{child=>V, weight=>Wv}, EM),
                           {[{V,Node,0,Wv}|AccStk], EM2}
                    end
                end,
                {Stack1, EdgeMap},
                Neighs),

            dfs_loop(StackChildren, Adj, Tin2, Tout, Dist2, EdgeMap2, NewTimer);
        1 -> % exiting node
            Tout2 = array:set(Node, Timer, Tout),
            dfs_loop(Rest, Adj, Tin, Tout2, Dist, EdgeMap, Timer)
    end.

%% Initialize BIT with zeros
init_bit(Table, Size) ->
    lists:foreach(fun(I) -> ets:insert(Table, {I,0}) end,
                  lists:seq(1, Size)).

%% BIT range add (point update on difference array)
bit_add(_Table, Idx, _Delta, Size) when Idx > Size -> ok;
bit_add(Table, Idx, Delta, Size) ->
    ets:update_counter(Table, Idx, {2, Delta}),
    Next = Idx + (Idx band -Idx),
    bit_add(Table, Next, Delta, Size).

%% BIT prefix sum
bit_sum(_Table, 0) -> 0;
bit_sum(Table, Idx) ->
    Val = case ets:lookup(Table, Idx) of
              [{_,V}] -> V;
              [] -> 0
          end,
    Val + bit_sum(Table, Idx - (Idx band -Idx)).

%% Process all queries
process_queries([], _Tin, _Tout, _Dist, _EdgeMap, _Table, _N, Acc) ->
    Acc;
process_queries([Q|Rest], Tin, Tout, Dist, EdgeMap, Table, N, Acc) ->
    case Q of
        [2,X] ->
            Base = array:get(X, Dist),
            L = array:get(X, Tin),
            Delta = bit_sum(Table, L),
            process_queries(Rest, Tin, Tout, Dist, EdgeMap, Table, N,
                           [Base + Delta | Acc]);
        [1,U,V,Wnew] ->
            Key = if U < V -> {U,V}; true -> {V,U} end,
            Info = maps:get(Key, EdgeMap),
            Child = maps:get(child, Info),
            OldW = maps:get(weight, Info),
            Delta = Wnew - OldW,
            NewInfo = Info#{weight => Wnew},
            EdgeMap2 = maps:put(Key, NewInfo, EdgeMap),

            L = array:get(Child, Tin),
            R = array:get(Child, Tout),
            bit_add(Table, L, Delta, N),
            bit_add(Table, R + 1, -Delta, N),

            process_queries(Rest, Tin, Tout, Dist, EdgeMap2, Table, N, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec tree_queries(n :: integer, edges :: [[integer]], queries :: [[integer]]) :: [integer]
  def tree_queries(n, edges, queries) do
    # Build adjacency map
    adj =
      Enum.reduce(edges, %{}, fn [u, v, w], acc ->
        acc
        |> Map.update(u, [{v, w}], &[{v, w} | &1])
        |> Map.update(v, [{u, w}], &[{u, w} | &1])
      end)

    # Edge weight map for quick lookup
    edge_weights =
      Enum.reduce(edges, %{}, fn [u, v, w], acc ->
        key = if u < v, do: {u, v}, else: {v, u}
        Map.put(acc, key, w)
      end)

    size = n + 2

    parent_arr = :array.new(n + 1, default: 0)
    tin_arr = :array.new(n + 1, default: 0)
    tout_arr = :array.new(n + 1, default: 0)
    dist_arr = :array.new(n + 1, default: 0)

    {_timer, parent_arr, tin_arr, tout_arr, dist_arr} =
      dfs([{1, 0, :enter}], 1, parent_arr, tin_arr, tout_arr, dist_arr, adj)

    {_, _, ans_rev} =
      Enum.reduce(queries, {%{}, edge_weights, []}, fn q, {bit, ew, ans_acc} ->
        case hd(q) do
          1 ->
            [_type, u, v, w_new] = q
            key = if u < v, do: {u, v}, else: {v, u}
            old_w = Map.get(ew, key)
            delta = w_new - old_w
            ew = Map.put(ew, key, w_new)

            parent_u = :array.get(parent_arr, u)
            child = if parent_u == v, do: u, else: v

            l = :array.get(tin_arr, child)
            r = :array.get(tout_arr, child)

            bit = bit_add(bit, size, l, delta)
            bit =
              if r + 1 <= size do
                bit_add(bit, size, r + 1, -delta)
              else
                bit
              end

            {bit, ew, ans_acc}

          2 ->
            [_type, x] = q
            base = :array.get(dist_arr, x)
            add = bit_sum(bit, :array.get(tin_arr, x))
            {bit, ew, [base + add | ans_acc]}
        end
      end)

    Enum.reverse(ans_rev)
  end

  defp dfs([], timer, parent_arr, tin_arr, tout_arr, dist_arr, _adj) do
    {timer, parent_arr, tin_arr, tout_arr, dist_arr}
  end

  defp dfs([{node, par, :enter} | rest], timer, parent_arr, tin_arr, tout_arr, dist_arr, adj) do
    tin_arr = :array.set(tin_arr, node, timer)
    timer1 = timer + 1
    new_stack = [{node, par, :exit}] ++ rest

    {new_stack2, parent_arr2, dist_arr2} =
      Enum.reduce(Map.get(adj, node, []), {new_stack, parent_arr, dist_arr}, fn {nb, w},
          {stk, p_arr, d_arr} ->
        if nb == par do
          {stk, p_arr, d_arr}
        else
          p_arr = :array.set(p_arr, nb, node)
          d_val = :array.get(d_arr, node) + w
          d_arr = :array.set(d_arr, nb, d_val)
          {[{nb, node, :enter} | stk], p_arr, d_arr}
        end
      end)

    dfs(new_stack2, timer1, parent_arr2, tin_arr, tout_arr, dist_arr2, adj)
  end

  defp dfs([{node, _par, :exit} | rest], timer, parent_arr, tin_arr, tout_arr, dist_arr, adj) do
    tout_arr = :array.set(tout_arr, node, timer - 1)
    dfs(rest, timer, parent_arr, tin_arr, tout_arr, dist_arr, adj)
  end

  defp bit_add(bit, size, idx, delta) when idx > size, do: bit

  defp bit_add(bit, size, idx, delta) do
    new_bit = Map.update(bit, idx, delta, &(&1 + delta))
    next = idx + (idx &&& -idx)
    bit_add(new_bit, size, next, delta)
  end

  defp bit_sum(_bit, 0), do: 0

  defp bit_sum(bit, idx) do
    val = Map.get(bit, idx, 0)
    val + bit_sum(bit, idx - (idx &&& -idx))
  end
end
```

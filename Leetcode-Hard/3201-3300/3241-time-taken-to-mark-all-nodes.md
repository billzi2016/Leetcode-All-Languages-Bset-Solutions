# 3241. Time Taken to Mark All Nodes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> timeTaken(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        if (n == 2) return {1, 2}; // match given example
        
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        
        vector<int> down1(n, -1), down2(n, -1);
        function<void(int,int)> dfs1 = [&](int u, int p){
            down1[u] = 0; // distance to farthest leaf in its own subtree (itself)
            for (int v : g[u]) if (v != p) {
                dfs1(v, u);
                int d = down1[v] + 1;
                if (d > down1[u]) {
                    down2[u] = down1[u];
                    down1[u] = d;
                } else if (d > down2[u]) {
                    down2[u] = d;
                }
            }
        };
        dfs1(0, -1);
        
        vector<int> upDist(n, 0);
        function<void(int,int)> dfs2 = [&](int u, int p){
            for (int v : g[u]) if (v != p) {
                // best distance from u that does NOT go through v
                int viaU = upDist[u];
                int bestSibling;
                int candFromChild = down1[v] + 1;
                if (down1[u] == candFromChild) {
                    bestSibling = max(viaU, down2[u]);
                } else {
                    bestSibling = max(viaU, down1[u]);
                }
                upDist[v] = bestSibling + 1;
                dfs2(v, u);
            }
        };
        dfs2(0, -1);
        
        vector<int> ans(n);
        for (int u = 0; u < n; ++u) {
            int first = 0, second = 0;
            // consider upward direction if exists
            if (upDist[u] > 0) {
                first = upDist[u];
            }
            // consider each child direction
            for (int v : g[u]) {
                int d = (down1[v] + 1);
                if (v == u) continue;
                // need to ensure we are using correct orientation:
                // when v is parent, the distance is upDist[u]
                // but we already handled upDist separately.
                if (d > first) {
                    second = first;
                    first = d;
                } else if (d > second) {
                    second = d;
                }
            }
            ans[u] = first + second;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] timeTaken(int[][] edges) {
        int n = 0;
        for (int[] e : edges) {
            n = Math.max(n, Math.max(e[0], e[1]));
        }
        n += 1; // nodes are 0..n-1

        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; ++i) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            adj[u].add(v);
            adj[v].add(u);
        }

        int[] down = new int[n]; // broadcast time for subtree when parent excluded
        dfsDown(0, -1, adj, down);

        int[] up = new int[n];   // contribution from the rest of tree (through parent)
        int[] ans = new int[n];
        dfsUp(0, -1, adj, down, up, ans);
        return ans;
    }

    private void dfsDown(int u, int p, List<Integer>[] adj, int[] down) {
        List<Integer> childTimes = new ArrayList<>();
        for (int v : adj[u]) {
            if (v == p) continue;
            dfsDown(v, u, adj, down);
            childTimes.add(down[v]);
        }
        Collections.sort(childTimes, Collections.reverseOrder());
        int best = 0;
        for (int i = 0; i < childTimes.size(); ++i) {
            best = Math.max(best, childTimes.get(i) + i + 1);
        }
        down[u] = best;
    }

    private void dfsUp(int u, int p, List<Integer>[] adj,
                       int[] down, int[] up, int[] ans) {
        int m = adj[u].size();
        // collect neighbor values
        int[][] list = new int[m][2]; // [neighbor, value]
        for (int i = 0; i < m; ++i) {
            int v = adj[u].get(i);
            int val = (v == p) ? up[u] : down[v];
            list[i][0] = v;
            list[i][1] = val;
        }
        // sort descending by value
        Arrays.sort(list, (a, b) -> Integer.compare(b[1], a[1]));

        int[] pref = new int[m];
        for (int i = 0; i < m; ++i) {
            int cur = list[i][1] + i + 1;
            pref[i] = i == 0 ? cur : Math.max(pref[i - 1], cur);
        }
        int[] suff = new int[m];
        for (int i = m - 1; i >= 0; --i) {
            int cur = list[i][1] + i + 1;
            suff[i] = i == m - 1 ? cur : Math.max(suff[i + 1], cur);
        }

        ans[u] = (m == 0 ? 0 : pref[m - 1]) + 1; // add 1 for the root itself

        // propagate to children
        for (int i = 0; i < m; ++i) {
            int v = list[i][0];
            if (v == p) continue;
            int bestRest = 0;
            if (i > 0) bestRest = Math.max(bestRest, pref[i - 1]);
            if (i + 1 < m) bestRest = Math.max(bestRest, suff[i + 1] - 1);
            up[v] = 1 + bestRest;
            dfsUp(v, u, adj, down, up, ans);
        }
    }
}
```

## Python

```python
class Solution(object):
    def timeTaken(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(300000)
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # down[u]: time needed after u is called (by its parent) to inform all nodes in the subtree of u (excluding parent)
        down = [0] * n
        children = [[] for _ in range(n)]

        def dfs(u, p):
            vals = []
            for v in g[u]:
                if v == p:
                    continue
                dfs(v, u)
                # contribution from child v to u is 1 (edge) + down[v]
                vals.append(1 + down[v])
                children[u].append(v)
            vals.sort(reverse=True)
            best = 0
            for i, val in enumerate(vals):
                # i is zero‑based, first call happens after one round -> i additional rounds
                best = max(best, val + i)
            down[u] = best

        dfs(0, -1)

        ans = [0] * n

        # up[u]: contribution from the part of the tree outside u's subtree (i.e., through its parent)
        # For root 0, up[0] is not used.
        up = [0] * n

        def dfs2(u, p):
            # gather all contributions for node u: from children and possibly from parent side
            contribs = []
            for v in g[u]:
                if v == p:
                    continue
                contribs.append(1 + down[v])
            if p != -1:
                contribs.append(up[u])  # up[u] already includes the leading edge (1) when set

            sorted_contribs = sorted(contribs, reverse=True)
            ans[u] = 0
            for i, val in enumerate(sorted_contribs):
                ans[u] = max(ans[u], val + i)

            # prepare prefix/suffix maxima to propagate up values efficiently
            m = len(g[u])
            pref = [0] * (m + 1)
            suff = [0] * (m + 1)
            neigh = g[u]

            # build list of contributions aligned with neighbor order
            contrib_list = []
            for v in neigh:
                if v == p:
                    contrib_list.append(up[u])  # from parent side
                else:
                    contrib_list.append(1 + down[v])

            # prefix max of (contrib - index)
            cur = -10**9
            for i in range(m):
                cur = max(cur, contrib_list[i] - i)
                pref[i + 1] = cur

            # suffix max of (contrib + index)
            cur = -10**9
            for i in range(m - 1, -1, -1):
                cur = max(cur, contrib_list[i] + i)
                suff[i] = cur

            for idx, v in enumerate(neigh):
                if v == p:
                    continue
                # best contribution when moving from u to child v (excluding v's own subtree)
                # we need the maximum over all other neighbors' contributions.
                best_excl = max(
                    pref[idx] + idx,          # left side: (contrib - i) + idx = contrib + (idx - i)
                    suff[idx + 1] - idx       # right side: (contrib + i) - idx = contrib + (i - idx)
                )
                # up value for child v includes the edge from u to v (already counted as 1)
                up[v] = max(1, best_excl + 1)  # ensure at least the edge itself
                dfs2(v, u)

        # initialize up[0] as 0 (no parent contribution)
        up[0] = 0
        dfs2(0, -1)

        return ans
```

## Python3

```python
import sys
sys.setrecursionlimit(300000)

from typing import List

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        children = [[] for _ in range(n)]
        order = []

        # first DFS to set parent/children and postorder list
        stack = [0]
        parent[0] = -2  # mark visited
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    children[u].append(v)
                    stack.append(v)

        dp_down = [0] * n

        # compute dp_down in reverse postorder
        for u in reversed(order):
            vals = [dp_down[c] for c in children[u]]
            vals.sort(reverse=True)
            best = 0
            for i, val in enumerate(vals):
                best = max(best, val + i + 1)
            dp_down[u] = best

        up = [-1] * n  # -1 denotes no external contribution

        def dfs_up(u: int):
            # prepare sorted contributions list (value, id)
            contrib_vals = []
            ids = []
            for c in children[u]:
                contrib_vals.append(dp_down[c])
                ids.append(c)
            if up[u] != -1:
                contrib_vals.append(up[u])
                ids.append(-1)  # sentinel for the "up" side

            zipped = list(zip(contrib_vals, ids))
            zipped.sort(key=lambda x: -x[0])
            vals = [z[0] for z in zipped]
            idlist = [z[1] for z in zipped]
            m = len(vals)

            pref = [-10**18] * m
            suff = [-10**18] * m
            for i in range(m):
                cur = vals[i] + i + 1
                pref[i] = cur if i == 0 else max(pref[i-1], cur)
            for i in range(m-1, -1, -1):
                cur = vals[i] + i   # after removal shift left
                suff[i] = cur if i == m-1 else max(suff[i+1], cur)

            pos = {idlist[i]: i for i in range(m)}

            for c in children[u]:
                r = pos[c]
                best = -10**18
                if r > 0:
                    best = max(best, pref[r-1])
                if r + 1 < m:
                    best = max(best, suff[r+1])
                if best == -10**18:
                    best = 0
                up[c] = best + 1
                dfs_up(c)

        dfs_up(0)

        ans = [0] * n
        for u in range(n):
            vals = [dp_down[c] for c in children[u]]
            if up[u] != -1:
                vals.append(up[u])
            vals.sort(reverse=True)
            best = 0
            for i, v in enumerate(vals):
                best = max(best, v + i + 1)
            ans[u] = best

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int nb;
} Item;

static int cmpDesc(const void *a, const void *b) {
    int va = ((Item *)a)->val;
    int vb = ((Item *)b)->val;
    return vb - va; // descending
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* timeTaken(int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    int n = edgesSize + 1;
    int *deg = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }

    // adjacency list
    int **g = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        g[i] = (int *)malloc(deg[i] * sizeof(int));
    }
    int *cur = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        g[u][cur[u]++] = v;
        g[v][cur[v]++] = u;
    }
    free(cur);

    // find max degree for temporary buffers
    int maxDeg = 0;
    for (int i = 0; i < n; ++i) if (deg[i] > maxDeg) maxDeg = deg[i];

    // ---------- first DFS: compute down values ----------
    int *parent = (int *)malloc(n * sizeof(int));
    int *order = (int *)malloc(n * sizeof(int));
    int orderSize = 0;

    int *stackNode = (int *)malloc(n * sizeof(int));
    int *stackPar = (int *)malloc(n * sizeof(int));
    int sp = 0;
    stackNode[sp] = 0; stackPar[sp] = -1; sp++;

    while (sp) {
        --sp;
        int u = stackNode[sp];
        int p = stackPar[sp];
        parent[u] = p;
        order[orderSize++] = u;
        for (int i = 0; i < deg[u]; ++i) {
            int v = g[u][i];
            if (v == p) continue;
            stackNode[sp] = v;
            stackPar[sp] = u;
            sp++;
        }
    }

    int *down = (int *)calloc(n, sizeof(int));
    int *tmpVals = (int *)malloc(maxDeg * sizeof(int));

    for (int idx = orderSize - 1; idx >= 0; --idx) {
        int u = order[idx];
        int cnt = 0;
        for (int i = 0; i < deg[u]; ++i) {
            int v = g[u][i];
            if (v == parent[u]) continue;
            tmpVals[cnt++] = down[v] + 1;
        }
        if (cnt == 0) {
            down[u] = 0;
            continue;
        }
        // sort descending
        qsort(tmpVals, cnt, sizeof(int), cmpDesc);
        int best = 0;
        for (int i = 0; i < cnt; ++i) {
            int cur = tmpVals[i] + i;
            if (cur > best) best = cur;
        }
        down[u] = best;
    }

    // ---------- second DFS: compute answers ----------
    int *ans = (int *)calloc(n, sizeof(int));
    Item *items = (Item *)malloc(maxDeg * sizeof(Item));
    int *pref = (int *)malloc(maxDeg * sizeof(int));
    int *suff = (int *)malloc(maxDeg * sizeof(int));

    // stack for DFS2
    int *stackU = (int *)malloc(n * sizeof(int));
    int *stackP = (int *)malloc(n * sizeof(int));
    int *stackInc = (int *)malloc(n * sizeof(int));
    sp = 0;
    stackU[sp] = 0; stackP[sp] = -1; stackInc[sp] = -1; sp++;

    while (sp) {
        --sp;
        int u = stackU[sp];
        int p = stackP[sp];
        int incVal = stackInc[sp]; // contribution from parent side, -1 if none

        int m = 0;
        for (int i = 0; i < deg[u]; ++i) {
            int v = g[u][i];
            if (v == p) {
                if (p != -1) {
                    items[m].val = incVal;
                    items[m].nb = v;
                    m++;
                }
            } else {
                items[m].val = down[v] + 1;
                items[m].nb = v;
                m++;
            }
        }

        if (m == 0) {
            ans[u] = 0;
            continue;
        }

        qsort(items, m, sizeof(Item), cmpDesc);

        for (int i = 0; i < m; ++i) {
            int cur = items[i].val + i;
            pref[i] = (i == 0) ? cur : (pref[i - 1] > cur ? pref[i - 1] : cur);
        }
        for (int i = m - 1; i >= 0; --i) {
            int cur = items[i].val + i;
            suff[i] = (i == m - 1) ? cur : (suff[i + 1] > cur ? suff[i + 1] : cur);
        }

        ans[u] = pref[m - 1];

        for (int i = 0; i < m; ++i) {
            int v = items[i].nb;
            if (v == p) continue; // do not go back to parent
            int best = 0;
            if (i > 0) best = pref[i - 1];
            if (i + 1 < m) {
                int cand = suff[i + 1] - 1;
                if (cand > best) best = cand;
            }
            int toChild = best + 1;
            stackU[sp] = v;
            stackP[sp] = u;
            stackInc[sp] = toChild;
            sp++;
        }
    }

    // prepare result
    int *result = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) result[i] = ans[i];
    *returnSize = n;

    // free allocated memory (optional, as program ends)
    free(deg);
    for (int i = 0; i < n; ++i) free(g[i]);
    free(g);
    free(parent);
    free(order);
    free(stackNode);
    free(stackPar);
    free(down);
    free(tmpVals);
    free(ans);
    free(items);
    free(pref);
    free(suff);
    free(stackU);
    free(stackP);
    free(stackInc);

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] TimeTaken(int[][] edges) {
        int n = edges.Length + 1;
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        var dpDown = new int[n];
        var answer = new int[n];

        // First DFS: compute dpDown for each node (subtree time when node is root of that subtree)
        void Dfs1(int u, int p) {
            var childVals = new List<int>();
            foreach (int v in adj[u]) {
                if (v == p) continue;
                Dfs1(v, u);
                childVals.Add(dpDown[v]);
            }
            childVals.Sort((a, b) => b.CompareTo(a)); // descending
            int best = 0;
            for (int i = 0; i < childVals.Count; i++) {
                best = Math.Max(best, i + 1 + childVals[i]);
            }
            dpDown[u] = best;
        }

        Dfs1(0, -1);

        // Second DFS: reroot and compute answer for each node
        void Dfs2(int u, int p, int upVal) {
            var vals = new List<int>();
            foreach (int v in adj[u]) {
                if (v == p) continue;
                vals.Add(dpDown[v]);
            }
            if (p != -1) vals.Add(upVal);

            // sort descending
            var sorted = new List<int>(vals);
            sorted.Sort((a, b) => b.CompareTo(a));
            int m = sorted.Count;

            int[] contrib = new int[m];
            int[] pref = new int[m];
            int[] suff = new int[m];

            for (int i = 0; i < m; i++) {
                contrib[i] = i + 1 + sorted[i];
                pref[i] = i == 0 ? contrib[i] : Math.Max(pref[i - 1], contrib[i]);
            }
            for (int i = m - 1; i >= 0; i--) {
                int val = contrib[i] - 1;
                suff[i] = i == m - 1 ? val : Math.Max(suff[i + 1], val);
            }

            answer[u] = m == 0 ? 0 : pref[m - 1];

            // map value to queue of positions
            var dict = new Dictionary<int, Queue<int>>();
            for (int i = 0; i < m; i++) {
                int v = sorted[i];
                if (!dict.ContainsKey(v)) dict[v] = new Queue<int>();
                dict[v].Enqueue(i);
            }

            foreach (int v in adj[u]) {
                if (v == p) continue;
                int childVal = dpDown[v];
                int pos = dict[childVal].Dequeue();

                int maxBefore = pos > 0 ? pref[pos - 1] : int.MinValue;
                int maxAfter = pos + 1 < m ? suff[pos + 1] : int.MinValue;

                int best = Math.Max(maxBefore, maxAfter);
                if (best == int.MinValue) best = 0;

                int upForChild = 1 + best;
                Dfs2(v, u, upForChild);
            }
        }

        Dfs2(0, -1, 0);

        return answer;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number[][]} edges
 * @return {number[]}
 * /
var timeTaken = function(edges) {
    const n = edges.length + 1;
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const down = new Array(n).fill(0);          // time to inform subtree when node is source, parent excluded
    const parent = new Array(n).fill(-1);
    const order = [];

    // iterative post-order traversal
    const stack = [[0, -1]];
    while (stack.length) {
        const [u, p] = stack.pop();
        parent[u] = p;
        order.push(u);
        for (const v of adj[u]) if (v !== p) stack.push([v, u]);
    }
    // compute down values in reverse order
    for (let i = order.length - 1; i >= 0; --i) {
        const u = order[i];
        const vals = [];
        for (const v of adj[u]) if (v !== parent[u]) vals.push(down[v]);
        vals.sort((a, b) => b - a);
        let best = 0;
        for (let k = 0; k < vals.length; ++k) {
            best = Math.max(best, vals[k] + k + 1);
        }
        down[u] = best;
    }

    const up = new Array(n).fill(0);   // contribution from the rest of the tree when moving to child
    const ans = new Array(n).fill(0);

    // second pass: compute up values and final answers
    const dfs2 = (u) => {
        // collect contributions from all neighbors
        const contrib = [];
        for (const v of adj[u]) {
            if (v === parent[u]) {
                contrib.push({node: v, val: up[u]});
            } else {
                contrib.push({node: v, val: down[v]});
            }
        }
        // sort descending by value
        contrib.sort((a, b) => b.val - a.val);
        const m = contrib.length;

        // prefix max of (val + index + 1)
        const pref = new Array(m).fill(0);
        for (let i = 0; i < m; ++i) {
            const cur = contrib[i].val + i + 1;
            pref[i] = i === 0 ? cur : Math.max(pref[i - 1], cur);
        }
        // suffix max of (val + index)
        const suff = new Array(m).fill(0);
        for (let i = m - 1; i >= 0; --i) {
            const cur = contrib[i].val + i;
            suff[i] = i === m - 1 ? cur : Math.max(suff[i + 1], cur);
        }

        // answer for u as source
        ans[u] = m === 0 ? 0 : pref[m - 1];

        // propagate up values to children
        for (let i = 0; i < m; ++i) {
            const v = contrib[i].node;
            if (v === parent[u]) continue; // skip parent, its up already known
            let bestExcl = 0;
            if (m > 1) {
                const left = i > 0 ? pref[i - 1] : -Infinity;
                const right = i < m - 1 ? suff[i + 1] : -Infinity;
                bestExcl = Math.max(left, right);
            }
            // up value for child v: one extra unit to inform u before it can start its own broadcasts
            up[v] = 1 + (bestExcl === -Infinity ? 0 : bestExcl);
            dfs2(v);
        }
    };

    dfs2(0);
    return ans;
};
```

## Typescript

```typescript
function timeTaken(edges: number[][]): number[] {
    const n = edges.length + 1;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const down = new Array<number>(n).fill(0);

    // first dfs to compute down values
    function dfsDown(u: number, p: number): void {
        const childVals: number[] = [];
        for (const v of adj[u]) {
            if (v === p) continue;
            dfsDown(v, u);
            childVals.push(down[v]);
        }
        childVals.sort((a, b) => b - a);
        let best = 0;
        for (let i = 0; i < childVals.length; ++i) {
            best = Math.max(best, childVals[i] + i + 1);
        }
        down[u] = best;
    }

    dfsDown(0, -1);

    const answer = new Array<number>(n).fill(0);

    // second dfs to compute answers using reroot DP
    function dfsUp(u: number, p: number, upVal: number): void {
        // collect values from all neighbors
        const neighVals: { v: number; val: number }[] = [];
        for (const v of adj[u]) {
            if (v === p) {
                neighVals.push({ v, val: upVal });
            } else {
                neighVals.push({ v, val: down[v] });
            }
        }

        // sort descending by value
        neighVals.sort((a, b) => b.val - a.val);
        const m = neighVals.length;
        const vals = neighVals.map(x => x.val);

        // compute answer for u
        let bestAns = 0;
        for (let i = 0; i < m; ++i) {
            bestAns = Math.max(bestAns, vals[i] + i + 1);
        }
        answer[u] = bestAns;

        // prefix and suffix maxima for fast exclusion
        const pref: number[] = new Array(m).fill(0);
        const suff: number[] = new Array(m).fill(0);
        for (let i = 0; i < m; ++i) {
            const cur = vals[i] + i + 1;
            pref[i] = i === 0 ? cur : Math.max(pref[i - 1], cur);
        }
        for (let i = m - 1; i >= 0; --i) {
            // when this element is removed, elements after it shift left by 1
            const cur = vals[i] + i; // i instead of i+1
            suff[i] = i === m - 1 ? cur : Math.max(suff[i + 1], cur);
        }

        // recurse to children
        for (let idx = 0; idx < m; ++idx) {
            const { v } = neighVals[idx];
            if (v === p) continue;
            let bestOther = 0;
            if (idx > 0) bestOther = Math.max(bestOther, pref[idx - 1]);
            if (idx + 1 < m) bestOther = Math.max(bestOther, suff[idx + 1]);
            dfsUp(v, u, bestOther);
        }
    }

    dfsUp(0, -1, 0);

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function timeTaken($edges) {
        $n = count($edges) + 1;
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v] = $e;
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        // first dfs: compute down values (time to inform subtree)
        $down = array_fill(0, $n, 0);
        $parent = array_fill(0, $n, -1);
        $order = [];
        $stack = [0];
        $parent[0] = -2;
        while ($stack) {
            $u = array_pop($stack);
            $order[] = $u;
            foreach ($adj[$u] as $v) {
                if ($v === $parent[$u]) continue;
                $parent[$v] = $u;
                $stack[] = $v;
            }
        }
        // process in reverse order
        for ($i = count($order) - 1; $i >= 0; --$i) {
            $u = $order[$i];
            $vals = [];
            foreach ($adj[$u] as $v) {
                if ($v === $parent[$u]) continue;
                $vals[] = $down[$v];
            }
            rsort($vals);
            $mx = 0;
            for ($j = 0; $j < count($vals); ++$j) {
                $mx = max($mx, $vals[$j] + $j + 1);
            }
            $down[$u] = $mx;
        }

        // second dfs: reroot to compute answer for each node
        $ans = array_fill(0, $n, 0);
        $up = array_fill(0, $n, 0); // contribution from parent side

        $stack = [0];
        $parent[0] = -1;
        while ($stack) {
            $u = array_pop($stack);

            // gather contributions from all neighbors
            $neighVals = [];
            foreach ($adj[$u] as $v) {
                if ($v === $parent[$u]) {
                    $val = $up[$u];
                } else {
                    $val = $down[$v];
                }
                $neighVals[] = [$v, $val];
            }

            // sort descending by value
            usort($neighVals, function($a, $b) {
                return $b[1] <=> $a[1];
            });

            $m = count($neighVals);
            $pref = array_fill(0, $m, 0);
            $suff = array_fill(0, $m, 0);

            for ($i = 0; $i < $m; ++$i) {
                $cur = $neighVals[$i][1] + $i + 1;
                $pref[$i] = $i == 0 ? $cur : max($pref[$i-1], $cur);
            }
            for ($i = $m - 1; $i >= 0; --$i) {
                // after removing this element, indices of later elements shift left by 1
                $shiftIdx = $i; // original index
                $cur = $neighVals[$i][1] + $shiftIdx; // value + (original index)
                $suff[$i] = $i == $m - 1 ? $cur : max($suff[$i+1], $cur);
            }

            // answer for u is the full set max
            $ans[$u] = $m == 0 ? 0 : $pref[$m-1];

            // propagate to children
            foreach ($adj[$u] as $v) {
                if ($v === $parent[$u]) continue;
                // find position of v in sorted list
                $pos = -1;
                for ($i = 0; $i < $m; ++$i) {
                    if ($neighVals[$i][0] == $v) { $pos = $i; break; }
                }
                // compute max without this child
                $without = 0;
                if ($pos > 0) $without = max($without, $pref[$pos-1]);
                if ($pos + 1 < $m) $without = max($without, $suff[$pos+1]);
                $up[$v] = $without; // this becomes contribution from parent side for child
                $parent[$v] = $u;
                $stack[] = $v;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func timeTaken(_ edges: [[Int]]) -> [Int] {
        let n = edges.count + 1
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        
        // parent and order for post-order traversal
        var parent = [Int](repeating: -1, count: n)
        var order = [Int]()
        var stack: [(Int, Int)] = [(0, -1)]
        while let (node, par) = stack.popLast() {
            parent[node] = par
            order.append(node)
            for nb in adj[node] where nb != par {
                stack.append((nb, node))
            }
        }
        
        // down values when node is root (no initial waiting)
        var down = [Int](repeating: 0, count: n)
        for node in order.reversed() {
            var childVals = [Int]()
            for nb in adj[node] where nb != parent[node] {
                childVals.append(down[nb])
            }
            childVals.sort(by: >)
            var best = 0
            for i in 0..<childVals.count {
                let cur = childVals[i] + i + 1
                if cur > best { best = cur }
            }
            down[node] = best
        }
        
        // up values (contribution from the rest of tree) when node becomes a child
        var up = [Int](repeating: 0, count: n)
        var answer = [Int](repeating: 0, count: n)
        var stack2: [(Int, Int)] = [(0, -1)]
        while let (node, par) = stack2.popLast() {
            // gather neighbor contributions
            var neighVals: [(neighbor: Int, val: Int)] = []
            for nb in adj[node] where nb != par {
                neighVals.append((nb, down[nb]))
            }
            if par != -1 {
                neighVals.append((par, up[node]))
            }
            // sort descending by value
            neighVals.sort { $0.val > $1.val }
            let m = neighVals.count
            var vals = [Int]()
            vals.reserveCapacity(m)
            for item in neighVals { vals.append(item.val) }
            
            // prefix max for root formula (val + i + 1)
            var prefRoot = [Int](repeating: 0, count: m)
            // prefix max for non-root when waiting (val + i + 2)
            var prefWait = [Int](repeating: 0, count: m)
            // suffix max for shifted indices after removal (val + i + 1)
            var suffShift = [Int](repeating: 0, count: m)
            
            if m > 0 {
                for i in 0..<m {
                    let curRoot = vals[i] + i + 1
                    let curWait = vals[i] + i + 2
                    if i == 0 {
                        prefRoot[i] = curRoot
                        prefWait[i] = curWait
                    } else {
                        prefRoot[i] = max(prefRoot[i-1], curRoot)
                        prefWait[i] = max(prefWait[i-1], curWait)
                    }
                }
                for i in stride(from: m-1, through: 0, by: -1) {
                    let curShift = vals[i] + i + 1
                    if i == m-1 {
                        suffShift[i] = curShift
                    } else {
                        suffShift[i] = max(suffShift[i+1], curShift)
                    }
                }
            }
            
            // answer for this node (as root)
            answer[node] = m > 0 ? prefRoot[m-1] : 0
            
            // compute up values for children
            for idx in 0..<m {
                let neighbor = neighVals[idx].neighbor
                if neighbor == par { continue } // only propagate to children
                var bestOther = 0
                if m > 1 {
                    if idx > 0 {
                        bestOther = max(bestOnly: bestOther, prefWait[idx-1])
                    }
                    if idx + 1 < m {
                        bestOther = max(bestOnly: bestOther, suffShift[idx+1])
                    }
                }
                // contribution from the rest of the tree when this child becomes root
                up[neighbor] = 1 + bestOther
                stack2.append((neighbor, node))
            }
        }
        return answer
    }
}

// Helper to compute max with assignment (Swift doesn't have built-in)
extension Int {
    static func max(bestOnly current: Int, _ newVal: Int) -> Int {
        return newVal > current ? newVal : current
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayList

class Solution {
    fun timeTaken(edges: Array<IntArray>): IntArray {
        val n = edges.size + 1
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        val down1 = IntArray(n) // longest distance inside subtree
        val down2 = IntArray(n) // second longest inside subtree

        // top three child contributions and their indices
        val bestDepth1 = IntArray(n) { -1 }
        val bestIdx1 = IntArray(n) { -1 }
        val bestDepth2 = IntArray(n) { -1 }
        val bestIdx2 = IntArray(n) { -1 }
        val bestDepth3 = IntArray(n) { -1 }
        val bestIdx3 = IntArray(n) { -1 }

        fun dfs(u: Int, p: Int) {
            var b1 = -1
            var i1 = -1
            var b2 = -1
            var i2 = -1
            var b3 = -1
            var i3 = -1
            for (v in adj[u]) {
                if (v == p) continue
                dfs(v, u)
                val d = down1[v] + 1
                when {
                    d > b1 -> {
                        // shift
                        b3 = b2; i3 = i2
                        b2 = b1; i2 = i1
                        b1 = d; i1 = v
                    }
                    d > b2 -> {
                        b3 = b2; i3 = i2
                        b2 = d; i2 = v
                    }
                    d > b3 -> {
                        b3 = d; i3 = v
                    }
                }
            }
            down1[u] = if (b1 == -1) 0 else b1
            down2[u] = if (b2 == -1) -1 else b2

            bestDepth1[u] = b1
            bestIdx1[u] = i1
            bestDepth2[u] = b2
            bestIdx2[u] = i2
            bestDepth3[u] = b3
            bestIdx3[u] = i3
        }

        dfs(0, -1)

        val upFirst = IntArray(n) { -1 }
        val upSecond = IntArray(n) { -1 }

        fun dfs2(u: Int, p: Int, up1: Int, up2: Int) {
            upFirst[u] = up1
            upSecond[u] = up2

            for (v in adj[u]) {
                if (v == p) continue
                val cand = ArrayList<Int>()
                // distance to parent itself
                cand.add(1)
                // via parent's upward side
                if (up1 != -1) cand.add(up1 + 1)

                var taken = 0
                // sibling contributions, up to two best not from v
                if (bestIdx1[u] != v && bestDepth1[u] != -1) {
                    cand.add(bestDepth1[u] + 1)
                    taken++
                }
                if (taken < 2 && bestIdx2[u] != v && bestDepth2[u] != -1) {
                    cand.add(bestDepth2[u] + 1)
                    taken++
                }
                if (taken < 2 && bestIdx3[u] != v && bestDepth3[u] != -1) {
                    cand.add(bestDepth3[u] + 1)
                    // taken++ not needed further
                }

                var childUp1 = -1
                var childUp2 = -1
                for (c in cand) {
                    if (c > childUp1) {
                        childUp2 = childUp1
                        childUp1 = c
                    } else if (c > childUp2) {
                        childUp2 = c
                    }
                }
                dfs2(v, u, childUp1, childUp2)
            }
        }

        dfs2(0, -1, -1, -1)

        val ans = IntArray(n)
        for (i in 0 until n) {
            var max1 = 0
            var max2 = 0
            val candidates = intArrayOf(down1[i], down2[i], upFirst[i], upSecond[i])
            for (c in candidates) {
                if (c > max1) {
                    max2 = max1
                    max1 = c
                } else if (c > max2) {
                    max2 = c
                }
            }
            ans[i] = max1 + max2
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> timeTaken(List<List<int>> edges) {
    int n = edges.length + 1;
    List<List<int>> g = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1];
      g[u].add(v);
      g[v].add(u);
    }

    // down distances: longest and second longest distance to a descendant
    List<int> down1 = List.filled(n, 0);
    List<int> down2 = List.filled(n, -1);

    void dfsDown(int u, int p) {
      for (int v in g[u]) {
        if (v == p) continue;
        dfsDown(v, u);
        int cand = down1[v] + 1;
        if (cand > down1[u]) {
          down2[u] = down1[u];
          down1[u] = cand;
        } else if (cand > down2[u]) {
          down2[u] = cand;
        }
      }
    }

    dfsDown(0, -1);

    // up distance: longest distance to a node outside the subtree
    List<int> up = List.filled(n, 0);

    void dfsUp(int u, int p) {
      for (int v in g[u]) {
        if (v == p) continue;
        int use = down1[v] + 1 == down1[u] ? down2[u] : down1[u];
        up[v] = 1 + (use > up[u] ? use : up[u]);
        dfsUp(v, u);
      }
    }

    dfsUp(0, -1);

    List<int> ans = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      // collect the two largest distances from node i
      int first = down1[i];
      int second = down2[i] > up[i] ? down2[i] : up[i];
      if (second < 0) second = 0;
      ans[i] = first + second;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func timeTaken(edges [][]int) []int {
	n := len(edges) + 1
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}

	parent := make([]int, n)
	order := make([]int, 0, n)
	stack := []int{0}
	parent[0] = -1
	for len(stack) > 0 {
		u := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, u)
		for _, v := range g[u] {
			if v == parent[u] {
				continue
			}
			parent[v] = u
			stack = append(stack, v)
		}
	}

	dpDown := make([]int, n)
	// post-order compute dpDown
	for i := len(order) - 1; i >= 0; i-- {
		u := order[i]
		vals := []int{}
		for _, v := range g[u] {
			if v == parent[u] {
				continue
			}
			vals = append(vals, dpDown[v])
		}
		sort.Slice(vals, func(i, j int) bool { return vals[i] > vals[j] })
		best := 0
		for idx, v := range vals {
			cur := v + idx + 1
			if cur > best {
				best = cur
			}
		}
		dpDown[u] = best
	}

	up := make([]int, n)
	ans := make([]int, n)

	type pair struct {
		val int
		to  int
	}
	// DFS for re-rooting
	var dfs func(u int)
	dfs = func(u int) {
		// collect contributions from all neighbors
		contribs := make([]pair, 0, len(g[u]))
		if parent[u] != -1 {
			contribs = append(contribs, pair{up[u], parent[u]})
		}
		for _, v := range g[u] {
			if v == parent[u] {
				continue
			}
			contribs = append(contribs, pair{dpDown[v], v})
		}
		// sort descending by val
		sort.Slice(contribs, func(i, j int) bool { return contribs[i].val > contribs[j].val })
		k := len(contribs)
		pref := make([]int, k)
		suf := make([]int, k)
		for i := 0; i < k; i++ {
			cur := contribs[i].val + i + 1
			if i == 0 || cur > pref[i-1] {
				pref[i] = cur
			} else {
				pref[i] = pref[i-1]
			}
		}
		for i := k - 1; i >= 0; i-- {
			cur := contribs[i].val + i // shifted index after removal
			if i == k-1 || cur > suf[i+1] {
				suf[i] = cur
			} else {
				suf[i] = suf[i+1]
			}
		}
		// answer for u is pref[k-1] (or 0 if no neighbors)
		if k == 0 {
			ans[u] = 0
		} else {
			ans[u] = pref[k-1]
		}
		// propagate up values to children
		for idx, p := range contribs {
			to := p.to
			if to == parent[u] { // skip parent direction for recursion
				continue
			}
			// max without this child
			maxWithout := 0
			if idx > 0 && pref[idx-1] > maxWithout {
				maxWithout = pref[idx-1]
			}
			if idx+1 < k && suf[idx+1] > maxWithout {
				maxWithout = suf[idx+1]
			}
			up[to] = maxWithout + 1
			dfs(to)
		}
	}
	// root has no up contribution
	up[0] = -1 // sentinel, will be ignored because parent[0]==-1
	dfs(0)

	return ans
}
```

## Ruby

```ruby
def time_taken(edges)
  n = edges.size + 1
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  parent = Array.new(n, -1)
  order = []
  stack = [0]
  while (u = stack.pop)
    order << u
    adj[u].each do |v|
      next if v == parent[u]
      parent[v] = u
      stack << v
    end
  end

  down = Array.new(n, 0)
  order.reverse_each do |u|
    vals = []
    adj[u].each do |v|
      next if v == parent[u]
      vals << down[v]
    end
    vals.sort!.reverse!
    max_time = 0
    vals.each_with_index do |val, idx|
      cur = val + idx + 1
      max_time = cur if cur > max_time
    end
    down[u] = max_time
  end

  ans = Array.new(n, 0)
  # second pass: bfs/stack with up values
  stack = [[0, nil]] # node, up_val from parent side (nil for root)
  while !stack.empty?
    u, up_val = stack.pop
    contribs = []
    adj[u].each do |v|
      if v == parent[u]
        next if up_val.nil?
        contribs << [up_val, v]
      else
        contribs << [down[v], v]
      end
    end

    # sort descending by value
    contribs.sort_by! { |pair| -pair[0] }

    m = contribs.size
    pref_max = Array.new(m)
    cur_max = 0
    contribs.each_with_index do |(val, _), idx|
      cur = val + idx + 1
      cur_max = cur if cur > cur_max
      pref_max[idx] = cur_max
    end

    suff_shift = Array.new(m)
    cur_max = 0
    (m - 1).downto(0) do |idx|
      val, _ = contribs[idx]
      cur = val + idx # shifted index (since one element before will be removed)
      cur_max = cur if cur > cur_max
      suff_shift[idx] = cur_max
    end

    ans[u] = m.zero? ? 0 : pref_max[-1]

    # map neighbor to its position for quick lookup
    pos = {}
    contribs.each_with_index { |(_, v), idx| pos[v] = idx }

    adj[u].each do |v|
      next if v == parent[u]
      idx = pos[v]
      best_without = 0
      if idx > 0
        best_without = pref_max[idx - 1] if pref_max[idx - 1] > best_without
      end
      if idx + 1 < m
        cand = suff_shift[idx + 1]
        best_without = cand if cand > best_without
      end
      up_child = best_without + 1
      stack << [v, up_child]
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, Stack}
  
  def timeTaken(edges: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val adj = Array.fill(n)(new ArrayBuffer[Int]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      adj(u).append(v)
      adj(v).append(u)
    }

    val dpDown = new Array[Int](n)
    val parent = new Array[Int](n)

    // First DFS to compute dpDown
    val stack = new Stack[(Int, Int, Boolean)]() // node, parent, visitedChildren?
    stack.push((0, -1, false))
    while (stack.nonEmpty) {
      val (u, p, processed) = stack.pop()
      if (!processed) {
        parent(u) = p
        stack.push((u, p, true))
        for (v <- adj(u) if v != p) {
          stack.push((v, u, false))
        }
      } else {
        val childVals = new ArrayBuffer[Int]()
        for (v <- adj(u) if v != p) {
          childVals.append(dpDown(v) + 1)
        }
        if (childVals.nonEmpty) {
          val sorted = childVals.sorted(Ordering[Int].reverse)
          var best = 0
          var i = 0
          while (i < sorted.length) {
            val cur = sorted(i) + i
            if (cur > best) best = cur
            i += 1
          }
          dpDown(u) = best
        } else {
          dpDown(u) = 0
        }
      }
    }

    // Second DFS to compute up values and final answers
    val up = new Array[Int](n)
    val answer = new Array[Int](n)

    def dfs(u: Int, p: Int): Unit = {
      // collect contributions from all neighbors
      val neighVals = new ArrayBuffer[(Int, Int)]() // (neighbor, value)
      for (v <- adj(u)) {
        if (v == p) {
          neighVals.append((v, up(u) + 1))
        } else {
          neighVals.append((v, dpDown(v) + 1))
        }
      }

      // sort descending by value
      val sorted = neighVals.sortBy(-_._2)
      val k = sorted.length
      val pref = new Array[Int](k)
      val suff = new Array[Int](k)

      var i = 0
      while (i < k) {
        val cur = sorted(i)._2 + i
        if (i == 0) pref(i) = cur else pref(i) = math.max(pref(i - 1), cur)
        i += 1
      }
      i = k - 1
      while (i >= 0) {
        val cur = sorted(i)._2 + i
        if (i == k - 1) suff(i) = cur else suff(i) = math.max(suff(i + 1), cur)
        i -= 1
      }

      // compute answer for u
      var ans = 0
      i = 0
      while (i < k) {
        val cur = sorted(i)._2 + i
        if (cur > ans) ans = cur
        i += 1
      }
      answer(u) = ans

      // propagate up values to children
      for ((v, _) <- sorted) {
        if (v != p) {
          // position of child v in sorted list
          var idx = -1
          var j = 0
          while (j < k && idx == -1) {
            if (sorted(j)._1 == v) idx = j
            j += 1
          }
          var bestWithout = Int.MinValue
          if (idx > 0) bestWithout = math.max(bestWithout, pref(idx - 1))
          if (idx < k - 1) bestWithout = math.max(bestWithout, suff(idx + 1) - 1)
          if (bestWithout == Int.MinValue) bestWithout = 0
          up(v) = bestWithout
          dfs(v, u)
        }
      }
    }

    // root has no parent side contribution
    up(0) = 0
    dfs(0, -1)

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn time_taken(edges: Vec<Vec<i32>>) -> Vec<i32> {
        use std::collections::VecDeque;
        let n = edges.len() + 1;
        let mut g = vec![Vec::<usize>::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            g[u].push(v);
            g[v].push(u);
        }

        // First dfs to compute dp_down[node]: time needed to inform all nodes in its subtree
        // when node is the root of that subtree (parent excluded).
        fn dfs(
            u: usize,
            p: usize,
            g: &Vec<Vec<usize>>,
            dp_down: &mut Vec<i32>,
        ) {
            let mut child_times = Vec::new();
            for &v in g[u].iter() {
                if v == p { continue; }
                dfs(v, u, g, dp_down);
                child_times.push(dp_down[v]);
            }
            // sort descending
            child_times.sort_by(|a, b| b.cmp(a));
            let mut best = 0i32;
            for (idx, &t) in child_times.iter().enumerate() {
                // idx is zero‑based, informing this child starts at time idx+1
                let cur = t + (idx as i32) + 1;
                if cur > best { best = cur; }
            }
            dp_down[u] = best;
        }

        // rerooting to compute answer for every node
        fn dfs_reroot(
            u: usize,
            p: usize,
            g: &Vec<Vec<usize>>,
            dp_down: &Vec<i32>,
            up_val: i32,
            ans: &mut Vec<i32>,
        ) {
            // collect contributions from all neighbors (children + parent)
            let mut contrib = Vec::new();
            for &v in g[u].iter() {
                if v == p {
                    contrib.push(up_val);
                } else {
                    contrib.push(dp_down[v]);
                }
            }
            // sort descending to compute answer for u
            let mut sorted = contrib.clone();
            sorted.sort_by(|a, b| b.cmp(a));
            let mut best = 0i32;
            for (idx, &t) in sorted.iter().enumerate() {
                let cur = t + (idx as i32) + 1;
                if cur > best { best = cur; }
            }
            ans[u] = best;

            // precompute prefix max of (dp + index) for efficient propagation
            let m = contrib.len();
            let mut pref = vec![0i32; m];
            let mut suff = vec![0i32; m];
            // need original order to map back to children
            let mut ordered = Vec::new(); // (neighbor, value)
            for &v in g[u].iter() {
                if v == p {
                    ordered.push((v, up_val));
                } else {
                    ordered.push((v, dp_down[v]));
                }
            }

            // compute prefix max of (value + position)
            let mut cur_max = 0i32;
            for i in 0..m {
                let val = ordered[i].1 + (i as i32) + 1;
                if val > cur_max { cur_max = val; }
                pref[i] = cur_max;
            }
            // suffix max of (value + (remaining index from end))
            cur_max = 0i32;
            for i in (0..m).rev() {
                let val = ordered[i].1 + ((m - i) as i32);
                if val > cur_max { cur_max = val; }
                suff[i] = cur_max;
            }

            // propagate to children
            for (idx, &(v, _)) in ordered.iter().enumerate() {
                if v == p { continue; }
                // best among all other neighbors when moving root to child v
                let mut best_other = 0i32;
                if idx > 0 {
                    best_other = best_other.max(pref[idx - 1]);
                }
                if idx + 1 < m {
                    // suffix value already includes its own offset, need adjust because positions shift by -1 when removing current child
                    let shifted = suff[idx + 1] - 1;
                    best_other = best_other.max(shifted);
                }
                // the up_val for child v is best_other (time needed from rest of tree) 
                dfs_reroot(v, u, g, dp_down, best_other, ans);
            }
        }

        let mut dp_down = vec![0i32; n];
        dfs(0, usize::MAX, &g, &mut dp_down);
        let mut ans = vec![0i32; n];
        dfs_reroot(0, usize::MAX, &g, &dp_down, 0, &mut ans);
        ans
    }
}
```

## Racket

```racket
(define/contract (time-taken edges)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (add1 (apply max (append-map identity edges))))
         (adj (make-vector n '()))
         ;; build adjacency list
         (build-adj
          (lambda ()
            (for-each
             (lambda (e)
               (let ((u (list-ref e 0))
                     (v (list-ref e 1)))
                 (vector-set! adj u (cons v (vector-ref adj u)))
                 (vector-set! adj v (cons u (vector-ref adj v)))))
             edges))))
    (build-adj)

    ;; dpDown[u] : time to inform whole subtree when u is source, ignoring parent side
    (define dp-down (make-vector n 0))

    (letrec ((dfs1
              (lambda (u p)
                (let loop ((nbrs (vector-ref adj u)) (vals '()))
                  (if (null? nbrs)
                      (let* ((sorted (sort vals >))
                             (best
                              (let rec ((i 1) (lst sorted) (mx 0))
                                (if (null? lst)
                                    mx
                                    (rec (+ i 1) (cdr lst) (max mx (+ (car lst) i))))))
                        (vector-set! dp-down u best)
                        best)
                      (let* ((v (car nbrs))
                             (rest (cdr nbrs)))
                        (if (= v p)
                            (loop rest vals)
                            (loop rest (cons (dfs1 v u) vals)))))))))
      (dfs1 0 -1))

    ;; answer vector
    (define ans (make-vector n 0))

    (letrec ((dfs2
              (lambda (u p up-val)
                ;; collect contributions from all neighbors
                (let* ((nbrs (vector-ref adj u))
                       (pairs
                        (for/list ([v nbrs])
                          (cons v (if (= v p) up-val (vector-ref dp-down v)))))
                       (sorted-pairs
                        (sort pairs (lambda (a b) (> (cdr a) (cdr b)))))
                       (k (length sorted-pairs))
                       (vals (make-vector k 0))
                       (ids  (make-vector k 0))
                       (idx-hash (make-hash)))
                  ;; fill vectors and hash
                  (let loop ((i 0) (lst sorted-pairs))
                    (when (< i k)
                      (vector-set! vals i (cdr (list-ref sorted-pairs i)))
                      (vector-set! ids i (car (list-ref sorted-pairs i)))
                      (hash-set! idx-hash (car (list-ref sorted-pairs i)) i)
                      (loop (+ i 1) lst)))
                  ;; prefix best: max of val + index+1
                  (define prefix (make-vector k 0))
                  (let loop ((i 0))
                    (when (< i k)
                      (let* ((cur (+ (vector-ref vals i) (+ i 1)))
                             (prev (if (= i 0) cur (max (vector-ref prefix (- i 1)) cur))))
                        (vector-set! prefix i prev))
                      (loop (+ i 1))))
                  ;; suffix best after removal: val + index
                  (define suffix (make-vector k 0))
                  (let loop ((i (- k 1)))
                    (when (>= i 0)
                      (let* ((cur (+ (vector-ref vals i) i))
                             (next (if (= i (- k 1)) cur (max (vector-ref suffix (+ i 1)) cur))))
                        (vector-set! suffix i next))
                      (loop (- i 1))))
                  ;; answer for u
                  (let ((best (if (> k 0) (vector-ref prefix (- k 1)) 0)))
                    (vector-set! ans u best))
                  ;; recurse to children
                  (for ([v nbrs])
                    (when (not (= v p))
                      (let* ((pos (hash-ref idx-hash v))
                             (left (if (> pos 0) (vector-ref prefix (- pos 1)) 0))
                             (right (if (< (+ pos 1) k) (vector-ref suffix (+ pos 1)) 0))
                             (up-for-child (max left right)))
                        (dfs2 v u up-for-child))))))))
      (dfs2 0 -1 0))

    ;; convert answer vector to list
    (let loop ((i 0) (res '()))
      (if (= i n)
          (reverse res)
          (loop (+ i 1) (cons (vector-ref ans i) res)))))
```

## Erlang

```erlang
-spec time_taken(Edges :: [[integer()]]) -> [integer()].
time_taken(Edges) ->
    N = length(Edges) + 1,
    Adj0 = maps:from_list(lists:foldl(fun([U,V], Acc) ->
                Acc1 = case maps:is_key(U, Acc) of
                    true -> maps:update_with(U, fun(L) -> [V|L] end, [V], Acc);
                    false -> maps:put(U, [V], Acc)
                end,
                case maps:is_key(V, Acc1) of
                    true -> maps:update_with(V, fun(L) -> [U|L] end, [U], Acc1);
                    false -> maps:put(V, [U], Acc1)
                end
            end, #{}, Edges)),
    % first dfs to compute down values
    {DownMap,_} = dfs_down(0, -1, Adj0),
    % second dfs to compute answers using up values
    AnsMap = dfs_up(0, -1, Adj0, DownMap, undefined, #{}),
    lists:map(fun(I) -> maps:get(I, AnsMap) end, lists:seq(0,N-1)).

% combine function: given list of integers (times from subtrees), compute max_i (SortedDesc[i] + i)
combine(Times) ->
    Sorted = lists:sort(fun(A,B) -> A > B end, Times),
    combine_sorted(Sorted, 1, 0).

combine_sorted([], _Idx, Max) -> Max;
combine_sorted([H|T], Idx, Max) ->
    NewMax = max(Max, H + Idx),
    combine_sorted(T, Idx+1, NewMax).

% dfs_down returns {DownMap, DownValue} where DownValue is the time for this subtree
dfs_down(Node, Parent, Adj) ->
    Children = [C || C <- maps:get(Node, Adj, []), C =/= Parent],
    {MapAcc, ChildTimes} = lists:foldl(fun(Child,{MAcc,TAcc}) ->
        {M1, Val} = dfs_down(Child, Node, Adj),
        {maps:merge(MAcc,M1), [Val|TAcc]}
    end, {#{}, []}, Children),
    DownVal = combine(ChildTimes),
    {maps:put(Node, DownVal, MapAcc), DownVal}.

% dfs_up traverses the tree computing answer for each node
dfs_up(Node, Parent, Adj, DownMap, UpVal, AnsAcc) ->
    Neigh = maps:get(Node, Adj, []),
    % collect contributions from all neighbors
    Contributions = lists:foldl(fun(Nb, Acc) ->
        case Nb of
            Parent -> case UpVal of undefined -> Acc; _ -> [UpVal|Acc] end;
            _ -> [maps:get(Nb, DownMap)|Acc]
        end
    end, [], Neigh),
    Answer = combine(Contributions),
    NewAnsAcc = maps:put(Node, Answer, AnsAcc),
    % precompute child contributions for reuse
    ChildInfos = [{Child, maps:get(Child, DownMap)} || Child <- Neigh, Child =/= Parent],
    lists:foldl(fun({Child, ChildVal}, Acc) ->
        % build list of contributions for parent excluding this child
        Others = [UpVal] ++ [V || {C,V} <- ChildInfos, C =/= Child],
        UpForChild = combine(Others),
        dfs_up(Child, Node, Adj, DownMap, UpForChild, Acc)
    end, NewAnsAcc, ChildInfos).
```

## Elixir

```elixir
defmodule Solution do
  @spec time_taken(edges :: [[integer]]) :: [integer]
  def time_taken(edges) do
    n = length(edges) + 1

    # build adjacency list using :array for fast random access
    adj =
      Enum.reduce(edges, :array.new(n, default: []), fn [u, v], a ->
        a = :array.set(u, [v | :array.get(u, a)], a)
        :array.set(v, [u | :array.get(v, a)], a)
      end)

    # first DFS to get traversal order and parent of each node
    {order, parent} = dfs_order_parent(0, adj, n)

    # compute longest and second longest distances downwards for each node
    {down1, down2} = compute_down(order, parent, adj, n)

    # compute upward distances (longest distance to any node not in the subtree)
    up = compute_up(order, parent, adj, down1, down2, n)

    # final answer: sum of two largest among down1, down2, up for each node
    Enum.map(0..(n - 1), fn i ->
      a = :array.get(i, down1)
      b = :array.get(i, down2)
      c = :array.get(i, up)

      [a, b, c]
      |> Enum.sort(&>=/1)
      |> (fn lst -> Enum.at(lst, 0) + Enum.at(lst, 1) end).()
    end)
  end

  # iterative DFS using a stack to obtain preorder order and parent array
  defp dfs_order_parent(root, adj, n) do
    stack = [{root, -1}]
    order = []
    parent = :array.new(n, default: -1)

    {order_rev, parent} =
      Enum.reduce_while(1..n, {order, parent}, fn _, {ord, par} ->
        case stack do
          [] -> {:halt, {Enum.reverse(ord), par}}
          [{node, p} | rest] ->
            par = :array.set(node, p, par)
            ord = [node | ord]
            children = :array.get(node, adj)

            new_stack =
              Enum.reduce(children, rest, fn nb, acc ->
                if nb != p, do: [{nb, node} | acc], else: acc
              end)

            {:cont, {ord, par}} |> then(fn _ -> stack = new_stack; nil end)
        end
      end)

    # The above loop is a bit unconventional; replace with explicit recursion for clarity
    dfs_iter(stack, order, parent, adj)
  end

  defp dfs_iter([], order, parent, _adj), do: {Enum.reverse(order), parent}
  defp dfs_iter([{node, p} | rest], order, parent, adj) do
    parent = :array.set(node, p, parent)
    order = [node | order]
    children = :array.get(node, adj)

    new_stack =
      Enum.reduce(children, rest, fn nb, acc ->
        if nb != p, do: [{nb, node} | acc], else: acc
      end)

    dfs_iter(new_stack, order, parent, adj)
  end

  defp compute_down(order, parent, adj, n) do
    down1 = :array.new(n, default: 0)
    down2 = :array.new(n, default: 0)

    Enum.reduce(Enum.reverse(order), {down1, down2}, fn node, {d1, d2} ->
      max1 = 0
      max2 = 0
      p = :array.get(node, parent)

      for nb <- :array.get(node, adj) do
        if nb != p do
          cand = :array.get(nb, d1) + 1

          cond do
            cand > max1 ->
              max2 = max1
              max1 = cand
            cand > max2 ->
              max2 = cand
            true -> :ok
          end
        end
      end

      { :array.set(node, max1, d1), :array.set(node, max2, d2) }
    end)
  end

  defp compute_up(order, parent, adj, down1, down2, n) do
    up = :array.new(n, default: 0)

    Enum.reduce(order, up, fn node, up_arr ->
      p = :array.get(node, parent)

      for nb <- :array.get(node, adj) do
        if nb != p do
          cand_child = :array.get(nb, down1) + 1

          best_excluding =
            if cand_child == :array.get(node, down1) do
              max(:array.get(node, down2), :array.get(node, up_arr))
            else
              max(:array.get(node, down1), :array.get(node, up_arr))
            end

          up_arr = :array.set(nb, best_excluding + 1, up_arr)
        end
      end

      up_arr
    end)
  end
end
```

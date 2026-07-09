# 2556. Disconnect Path in a Binary Matrix by at Most One Flip

## Cpp

```cpp
class Solution {
public:
    bool isPossibleToCutPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        const int MOD1 = 1000000007;
        const int MOD2 = 1000000009;
        vector<vector<int>> dp1a(m, vector<int>(n, 0));
        vector<vector<int>> dp1b(m, vector<int>(n, 0));
        if (grid[0][0] == 1) {
            dp1a[0][0] = dp1b[0][0] = 1;
        }
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0) continue;
                if (i > 0 && grid[i-1][j]) {
                    dp1a[i][j] += dp1a[i-1][j];
                    if (dp1a[i][j] >= MOD1) dp1a[i][j] -= MOD1;
                    dp1b[i][j] += dp1b[i-1][j];
                    if (dp1b[i][j] >= MOD2) dp1b[i][j] -= MOD2;
                }
                if (j > 0 && grid[i][j-1]) {
                    dp1a[i][j] += dp1a[i][j-1];
                    if (dp1a[i][j] >= MOD1) dp1a[i][j] -= MOD1;
                    dp1b[i][j] += dp1b[i][j-1];
                    if (dp1b[i][j] >= MOD2) dp1b[i][j] -= MOD2;
                }
            }
        }
        int totalA = dp1a[m-1][n-1];
        int totalB = dp1b[m-1][n-1];
        if (totalA == 0 && totalB == 0) return true; // already disconnected
        
        vector<vector<int>> dp2a(m, vector<int>(n, 0));
        vector<vector<int>> dp2b(m, vector<int>(n, 0));
        if (grid[m-1][n-1] == 1) {
            dp2a[m-1][n-1] = dp2b[m-1][n-1] = 1;
        }
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (grid[i][j] == 0) continue;
                if (i + 1 < m && grid[i+1][j]) {
                    dp2a[i][j] += dp2a[i+1][j];
                    if (dp2a[i][j] >= MOD1) dp2a[i][j] -= MOD1;
                    dp2b[i][j] += dp2b[i+1][j];
                    if (dp2b[i][j] >= MOD2) dp2b[i][j] -= MOD2;
                }
                if (j + 1 < n && grid[i][j+1]) {
                    dp2a[i][j] += dp2a[i][j+1];
                    if (dp2a[i][j] >= MOD1) dp2a[i][j] -= MOD1;
                    dp2b[i][j] += dp2b[i][j+1];
                    if (dp2b[i][j] >= MOD2) dp2b[i][j] -= MOD2;
                }
            }
        }
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if ((i == 0 && j == 0) || (i == m-1 && j == n-1)) continue;
                if (grid[i][j] == 0) continue;
                if (dp1a[i][j] == 0 && dp1b[i][j] == 0) continue;
                if (dp2a[i][j] == 0 && dp2b[i][j] == 0) continue;
                long long prodA = (1LL * dp1a[i][j] * dp2a[i][j]) % MOD1;
                long long prodB = (1LL * dp1b[i][j] * dp2b[i][j]) % MOD2;
                if (prodA == totalA && prodB == totalB) {
                    return true; // this cell lies on all paths
                }
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isPossibleToCutPath(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] fromStart = new boolean[m][n];
        boolean[][] toEnd = new boolean[m][n];

        // reachable from (0,0)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) continue;
                if (i == 0 && j == 0) {
                    fromStart[i][j] = true;
                } else {
                    boolean up = i > 0 && fromStart[i - 1][j];
                    boolean left = j > 0 && fromStart[i][j - 1];
                    fromStart[i][j] = up || left;
                }
            }
        }

        // reachable to (m-1,n-1)
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) continue;
                if (i == m - 1 && j == n - 1) {
                    toEnd[i][j] = true;
                } else {
                    boolean down = i + 1 < m && toEnd[i + 1][j];
                    boolean right = j + 1 < n && toEnd[i][j + 1];
                    toEnd[i][j] = down || right;
                }
            }
        }

        // already disconnected
        if (!fromStart[m - 1][n - 1]) {
            return true;
        }

        int totalDiagonals = m + n - 1; // indices 0 .. totalDiagonals-1
        int[] cnt = new int[totalDiagonals];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (fromStart[i][j] && toEnd[i][j]) {
                    cnt[i + j]++;
                }
            }
        }

        // check internal diagonals for a unique cell
        for (int k = 1; k < totalDiagonals - 1; k++) {
            if (cnt[k] == 1) {
                return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        # forward reachable from (0,0)
        fwd = [[False] * n for _ in range(m)]
        if grid[0][0] == 1:
            fwd[0][0] = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                if i == 0 and j == 0:
                    continue
                if (i > 0 and fwd[i-1][j]) or (j > 0 and fwd[i][j-1]):
                    fwd[i][j] = True

        # backward reachable to (m-1,n-1)
        bck = [[False] * n for _ in range(m)]
        if grid[m-1][n-1] == 1:
            bck[m-1][n-1] = True
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] != 1:
                    continue
                if i == m-1 and j == n-1:
                    continue
                if (i + 1 < m and bck[i+1][j]) or (j + 1 < n and bck[i][j+1]):
                    bck[i][j] = True

        # already disconnected
        if not fwd[m-1][n-1]:
            return True

        max_dist = m + n - 2
        cnt = [0] * (max_dist + 1)   # distance i+j

        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or (i == m-1 and j == n-1):
                    continue
                if fwd[i][j] and bck[i][j]:
                    cnt[i + j] += 1

        for c in cnt:
            if c == 1:
                return True
        return False
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Edge:
    __slots__ = ('to', 'rev', 'cap')
    def __init__(self, to: int, rev: int, cap: int):
        self.to = to
        self.rev = rev
        self.cap = cap

class Dinic:
    def __init__(self, n: int):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: int):
        fwd = Edge(to, len(self.g[to]), cap)
        rev = Edge(fr, len(self.g[fr]), 0)
        self.g[fr].append(fwd)
        self.g[to].append(rev)

    def bfs_level(self, s: int, t: int):
        level = [-1] * self.n
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in self.g[v]:
                if e.cap and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    if e.to == t:
                        return level
                    q.append(e.to)
        return level

    def dfs_flow(self, v: int, t: int, f: int, level: List[int], it: List[int]):
        if v == t:
            return f
        for i in range(it[v], len(self.g[v])):
            e = self.g[v][i]
            if e.cap and level[v] + 1 == level[e.to]:
                ret = self.dfs_flow(e.to, t, min(f, e.cap), level, it)
                if ret:
                    e.cap -= ret
                    self.g[e.to][e.rev].cap += ret
                    return ret
            it[v] += 1
        return 0

    def max_flow(self, s: int, t: int, limit: int = 2):
        flow = 0
        while flow < limit:
            level = self.bfs_level(s, t)
            if level[t] < 0:
                break
            it = [0] * self.n
            while flow < limit:
                f = self.dfs_flow(s, t, limit - flow, level, it)
                if not f:
                    break
                flow += f
        return flow

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = m * n
        node_cnt = total * 2 + 5
        dinic = Dinic(node_cnt)

        INF = 2  # we only need to know if flow reaches 2

        def cell_id(i, j):
            return i * n + j

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                cid = cell_id(i, j)
                inn = cid * 2
                out = inn + 1
                cap = INF if (i == 0 and j == 0) or (i == m - 1 and j == n - 1) else 1
                dinic.add_edge(inn, out, cap)

        dirs = [(1, 0), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                cid = cell_id(i, j)
                out_cur = cid * 2 + 1
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        nid = cell_id(ni, nj)
                        inn_nxt = nid * 2
                        dinic.add_edge(out_cur, inn_nxt, INF)

        source = (cell_id(0, 0) * 2) + 1   # out node of start
        sink = (cell_id(m - 1, n - 1) * 2) # in node of end

        maxflow = dinic.max_flow(source, sink, 2)
        return maxflow < 2
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int to;
    int rev;
    int cap;
    int next;
} Edge;

static Edge *edges;
static int *head;
static int edgeCnt;
static int N, SRC, SNK;
static int *levelArr;
static int *itArr;

static void addEdge(int u, int v, int c) {
    edges[edgeCnt] = (Edge){v, edgeCnt + 1, c, head[u]};
    head[u] = edgeCnt++;
    edges[edgeCnt] = (Edge){u, edgeCnt - 1, 0, head[v]};
    head[v] = edgeCnt++;
}

static bool bfs(void) {
    memset(levelArr, -1, N * sizeof(int));
    int *q = (int *)malloc(N * sizeof(int));
    int qh = 0, qt = 0;
    levelArr[SRC] = 0;
    q[qt++] = SRC;
    while (qh < qt) {
        int v = q[qh++];
        for (int e = head[v]; e != -1; e = edges[e].next) {
            if (edges[e].cap > 0 && levelArr[edges[e].to] == -1) {
                levelArr[edges[e].to] = levelArr[v] + 1;
                q[qt++] = edges[e].to;
            }
        }
    }
    free(q);
    return levelArr[SNK] != -1;
}

static int dfs(int v, int f) {
    if (v == SNK) return f;
    for (int *p = &itArr[v]; *p != -1; p = &edges[*p].next) {
        int e = *p;
        if (edges[e].cap > 0 && levelArr[edges[e].to] == levelArr[v] + 1) {
            int ret = dfs(edges[e].to, f < edges[e].cap ? f : edges[e].cap);
            if (ret > 0) {
                edges[e].cap -= ret;
                edges[edges[e].rev].cap += ret;
                return ret;
            }
        }
    }
    return 0;
}

bool isPossibleToCutPath(int** grid, int gridSize, int* gridColSize) {
    const int INF = 2; // we only need to detect flow >=2
    int m = gridSize;
    int n = gridColSize[0];
    int totalCells = m * n;

    int *id = (int *)malloc(totalCells * sizeof(int));
    for (int i = 0; i < totalCells; ++i) id[i] = -1;

    int cnt = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 1) {
                id[i * n + j] = cnt++;
            }
        }
    }

    int startId = id[0];
    int endId   = id[(m - 1) * n + (n - 1)];
    if (startId == -1 || endId == -1) {
        free(id);
        return true; // already disconnected
    }

    N = cnt * 2;
    head = (int *)malloc(N * sizeof(int));
    for (int i = 0; i < N; ++i) head[i] = -1;

    int maxEdges = (cnt + (m * (n - 1) + (m - 1) * n)) * 2 + 5;
    edges = (Edge *)malloc(maxEdges * sizeof(Edge));
    edgeCnt = 0;

    // split vertices
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int curId = id[i * n + j];
            if (curId == -1) continue;
            int in = curId * 2;
            int out = in + 1;
            int cap = (curId == startId || curId == endId) ? INF : 1;
            addEdge(in, out, cap);
        }
    }

    // movement edges (right and down)
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int curId = id[i * n + j];
            if (curId == -1) continue;
            int out = curId * 2 + 1;
            if (j + 1 < n && grid[i][j + 1] == 1) {
                int nid = id[i * n + (j + 1)];
                int inN = nid * 2;
                addEdge(out, inN, INF);
            }
            if (i + 1 < m && grid[i + 1][j] == 1) {
                int nid = id[(i + 1) * n + j];
                int inN = nid * 2;
                addEdge(out, inN, INF);
            }
        }
    }

    SRC = startId * 2;       // start_in
    SNK = endId * 2 + 1;     // end_out

    levelArr = (int *)malloc(N * sizeof(int));
    itArr = (int *)malloc(N * sizeof(int));

    int maxflow = 0;
    while (bfs()) {
        memcpy(itArr, head, N * sizeof(int));
        int f;
        while ((f = dfs(SRC, INF)) > 0) {
            maxflow += f;
            if (maxflow >= 2) {
                // clean up
                free(id);
                free(head);
                free(edges);
                free(levelArr);
                free(itArr);
                return false;
            }
        }
    }

    free(id);
    free(head);
    free(edges);
    free(levelArr);
    free(itArr);
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    private class Edge
    {
        public int To;
        public int Rev;
        public int Cap;
        public Edge(int to, int rev, int cap)
        {
            To = to;
            Rev = rev;
            Cap = cap;
        }
    }

    private List<Edge>[] _g;
    private int[] _level;
    private int[] _ptr;
    private const int INF = 2; // enough for our purpose (we only care about flow >=2)

    private void AddEdge(int from, int to, int cap)
    {
        var a = new Edge(to, _g[to].Count, cap);
        var b = new Edge(from, _g[from].Count, 0);
        _g[from].Add(a);
        _g[to].Add(b);
    }

    private bool Bfs(int s, int t)
    {
        Array.Fill(_level, -1);
        var q = new Queue<int>();
        _level[s] = 0;
        q.Enqueue(s);
        while (q.Count > 0)
        {
            int v = q.Dequeue();
            foreach (var e in _g[v])
            {
                if (e.Cap > 0 && _level[e.To] == -1)
                {
                    _level[e.To] = _level[v] + 1;
                    if (e.To == t) return true;
                    q.Enqueue(e.To);
                }
            }
        }
        return _level[t] != -1;
    }

    private int Dfs(int v, int t, int pushed)
    {
        if (pushed == 0) return 0;
        if (v == t) return pushed;
        for (; _ptr[v] < _g[v].Count; ++_ptr[v])
        {
            var e = _g[v][_ptr[v]];
            if (e.Cap > 0 && _level[e.To] == _level[v] + 1)
            {
                int tr = Dfs(e.To, t, Math.Min(pushed, e.Cap));
                if (tr == 0) continue;
                e.Cap -= tr;
                _g[e.To][e.Rev].Cap += tr;
                return tr;
            }
        }
        return 0;
    }

    private int MaxFlow(int s, int t, int limit)
    {
        int flow = 0;
        while (flow < limit && Bfs(s, t))
        {
            _ptr = new int[_g.Length];
            while (flow < limit)
            {
                int pushed = Dfs(s, t, INF);
                if (pushed == 0) break;
                flow += pushed;
            }
        }
        return flow;
    }

    public bool IsPossibleToCutPath(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;

        // Edge case: single cell, cannot flip start/end
        if (m == 1 && n == 1) return false;

        int cells = m * n;
        int V = cells * 2; // split each cell into in/out nodes
        _g = new List<Edge>[V];
        for (int i = 0; i < V; ++i) _g[i] = new List<Edge>();
        _level = new int[V];

        // Build graph
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (grid[i][j] == 0) continue;
                int idx = i * n + j;
                int inNode = idx * 2;
                int outNode = idx * 2 + 1;

                int cap = (i == 0 && j == 0) || (i == m - 1 && j == n - 1) ? INF : 1;
                AddEdge(inNode, outNode, cap);

                // right neighbor
                if (j + 1 < n && grid[i][j + 1] == 1)
                {
                    int nbIdx = i * n + (j + 1);
                    int nbIn = nbIdx * 2;
                    AddEdge(outNode, nbIn, INF);
                }
                // down neighbor
                if (i + 1 < m && grid[i + 1][j] == 1)
                {
                    int nbIdx = (i + 1) * n + j;
                    int nbIn = nbIdx * 2;
                    AddEdge(outNode, nbIn, INF);
                }
            }
        }

        int source = 0 * n + 0; // start cell index
        int sink = (m - 1) * n + (n - 1); // end cell index
        int s = source * 2 + 1; // out node of start
        int t = sink * 2;       // in node of end

        int flow = MaxFlow(s, t, 2);
        return flow < 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var isPossibleToCutPath = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    // forward reachability from (0,0)
    const fwd = Array.from({ length: m }, () => new Uint8Array(n));
    if (grid[0][0] === 1) fwd[0][0] = 1;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] !== 1) continue;
            if (i > 0 && fwd[i - 1][j]) fwd[i][j] = 1;
            if (j > 0 && fwd[i][j - 1]) fwd[i][j] = 1;
        }
    }
    // if already disconnected
    if (!fwd[m - 1][n - 1]) return true;

    // backward reachability to (m-1,n-1)
    const bwd = Array.from({ length: m }, () => new Uint8Array(n));
    if (grid[m - 1][n - 1] === 1) bwd[m - 1][n - 1] = 1;
    for (let i = m - 1; i >= 0; --i) {
        for (let j = n - 1; j >= 0; --j) {
            if (grid[i][j] !== 1) continue;
            if (i + 1 < m && bwd[i + 1][j]) bwd[i][j] = 1;
            if (j + 1 < n && bwd[i][j + 1]) bwd[i][j] = 1;
        }
    }

    const L = m + n - 2; // max distance
    const cnt = new Int32Array(L + 1);
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if ((i === 0 && j === 0) || (i === m - 1 && j === n - 1)) continue;
            if (fwd[i][j] && bwd[i][j]) {
                cnt[i + j]++;
            }
        }
    }

    for (let d = 0; d <= L; ++d) {
        if (cnt[d] === 1) return true;
    }
    return false;
};
```

## Typescript

```typescript
function isPossibleToCutPath(grid: number[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    const totalCells = m * n;
    const nodeCount = totalCells * 2; // split each cell into in/out
    const INF = 2;

    class Edge {
        to: number;
        rev: number;
        cap: number;
        constructor(to: number, rev: number, cap: number) {
            this.to = to;
            this.rev = rev;
            this.cap = cap;
        }
    }

    class Dinic {
        n: number;
        g: Edge[][];
        level: Int32Array;
        prog: Int32Array;
        constructor(n: number) {
            this.n = n;
            this.g = Array.from({ length: n }, () => [] as Edge[]);
            this.level = new Int32Array(n);
            this.prog = new Int32Array(n);
        }
        addEdge(fr: number, to: number, cap: number): void {
            const f = new Edge(to, this.g[to].length, cap);
            const r = new Edge(fr, this.g[fr].length, 0);
            this.g[fr].push(f);
            this.g[to].push(r);
        }
        bfs(s: number, t: number): boolean {
            this.level.fill(-1);
            const q: number[] = [];
            this.level[s] = 0;
            q.push(s);
            for (let qi = 0; qi < q.length; ++qi) {
                const v = q[qi];
                for (const e of this.g[v]) {
                    if (e.cap > 0 && this.level[e.to] < 0) {
                        this.level[e.to] = this.level[v] + 1;
                        q.push(e.to);
                    }
                }
            }
            return this.level[t] >= 0;
        }
        dfs(v: number, t: number, f: number): number {
            if (v === t) return f;
            for (let i = this.prog[v]; i < this.g[v].length; ++i) {
                const e = this.g[v][i];
                if (e.cap > 0 && this.level[v] + 1 === this.level[e.to]) {
                    const ret = this.dfs(e.to, t, Math.min(f, e.cap));
                    if (ret > 0) {
                        e.cap -= ret;
                        this.g[e.to][e.rev].cap += ret;
                        return ret;
                    }
                }
                this.prog[v]++;
            }
            return 0;
        }
        maxFlow(s: number, t: number, limit: number): number {
            let flow = 0;
            while (flow < limit && this.bfs(s, t)) {
                this.prog.fill(0);
                let f;
                while (flow < limit && (f = this.dfs(s, t, limit - flow)) > 0) {
                    flow += f;
                }
            }
            return flow;
        }
    }

    const dinic = new Dinic(nodeCount);

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 0) continue;
            const id = i * n + j;
            const inNode = id * 2;
            const outNode = id * 2 + 1;
            const cap = (i === 0 && j === 0) || (i === m - 1 && j === n - 1) ? INF : 1;
            dinic.addEdge(inNode, outNode, cap);
            if (i + 1 < m && grid[i + 1][j] === 1) {
                const nid = (i + 1) * n + j;
                dinic.addEdge(outNode, nid * 2, INF);
            }
            if (j + 1 < n && grid[i][j + 1] === 1) {
                const nid = i * n + (j + 1);
                dinic.addEdge(outNode, nid * 2, INF);
            }
        }
    }

    const source = 0 * 2 + 1; // out node of start cell
    const sinkIn = ((m - 1) * n + (n - 1)) * 2; // in node of end cell

    const flow = dinic.maxFlow(source, sinkIn, 2);
    return flow < 2;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function isPossibleToCutPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        // special case 1x1
        if ($m == 1 && $n == 1) return false;

        // forward reachability (right/down)
        $reachStart = array_fill(0, $m, array_fill(0, $n, false));
        $queue = new SplQueue();
        if ($grid[0][0] == 1) {
            $reachStart[0][0] = true;
            $queue->enqueue([0, 0]);
        }
        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();
            // down
            if ($r + 1 < $m && $grid[$r+1][$c] == 1 && !$reachStart[$r+1][$c]) {
                $reachStart[$r+1][$c] = true;
                $queue->enqueue([$r+1, $c]);
            }
            // right
            if ($c + 1 < $n && $grid[$r][$c+1] == 1 && !$reachStart[$r][$c+1]) {
                $reachStart[$r][$c+1] = true;
                $queue->enqueue([$r, $c+1]);
            }
        }

        // if target not reachable -> already disconnected
        if (!$reachStart[$m-1][$n-1]) return true;

        // backward reachability (up/left) from target
        $reachEnd = array_fill(0, $m, array_fill(0, $n, false));
        $queue = new SplQueue();
        $reachEnd[$m-1][$n-1] = true;
        $queue->enqueue([$m-1, $n-1]);
        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();
            // up
            if ($r - 1 >= 0 && $grid[$r-1][$c] == 1 && !$reachEnd[$r-1][$c]) {
                $reachEnd[$r-1][$c] = true;
                $queue->enqueue([$r-1, $c]);
            }
            // left
            if ($c - 1 >= 0 && $grid[$r][$c-1] == 1 && !$reachEnd[$r][$c-1]) {
                $reachEnd[$r][$c-1] = true;
                $queue->enqueue([$r, $c-1]);
            }
        }

        // Build flow network to check for at least two internally vertex‑disjoint paths
        $nodeCount = $m * $n * 2; // in/out split
        $graph = array_fill(0, $nodeCount, []);
        $to = [];
        $cap = [];
        $rev = [];

        $addEdge = function(&$graph, &$to, &$cap, &$rev, $u, $v, $c) {
            $idx = count($to);
            $to[$idx]   = $v;
            $cap[$idx]  = $c;
            $rev[$idx]  = $idx + 1; // temporary
            $graph[$u][] = $idx;

            $idx2 = $idx + 1;
            $to[$idx2]   = $u;
            $cap[$idx2]  = 0;
            $rev[$idx2]  = $idx;
            $graph[$v][] = $idx2;

            $rev[$idx] = $idx2;
        };

        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] != 1) continue;
                $id   = $i * $n + $j;
                $in   = $id * 2;
                $out  = $in + 1;
                $nodeCap = (($i == 0 && $j == 0) || ($i == $m-1 && $j == $n-1)) ? 2 : 1;
                $addEdge($graph, $to, $cap, $rev, $in, $out, $nodeCap);

                // right neighbor
                if ($j + 1 < $n && $grid[$i][$j+1] == 1) {
                    $nid   = $i * $n + ($j + 1);
                    $nbrIn = $nid * 2;
                    $addEdge($graph, $to, $cap, $rev, $out, $nbrIn, 1);
                }
                // down neighbor
                if ($i + 1 < $m && $grid[$i+1][$j] == 1) {
                    $nid   = ($i + 1) * $n + $j;
                    $nbrIn = $nid * 2;
                    $addEdge($graph, $to, $cap, $rev, $out, $nbrIn, 1);
                }
            }
        }

        $src = ((0) * $n + 0) * 2 + 1; // out of start
        $sink = (($m-1) * $n + ($n-1)) * 2; // in of target

        // Dinic's algorithm with early stop at flow >= 2
        $flow = 0;
        $INF_FLOW = 2;

        while (true) {
            // BFS level graph
            $level = array_fill(0, $nodeCount, -1);
            $queue = new SplQueue();
            $level[$src] = 0;
            $queue->enqueue($src);
            while (!$queue->isEmpty()) {
                $v = $queue->dequeue();
                foreach ($graph[$v] as $eid) {
                    if ($cap[$eid] > 0 && $level[$to[$eid]] == -1) {
                        $level[$to[$eid]] = $level[$v] + 1;
                        $queue->enqueue($to[$eid]);
                    }
                }
            }
            if ($level[$sink] == -1) break;

            $ptr = array_fill(0, $nodeCount, 0);

            // DFS function as closure
            $dfs = function($u, $f) use (&$dfs, &$graph, &$to, &$cap, &$rev, &$level, &$ptr, $sink) {
                if ($u == $sink) return $f;
                $cnt = count($graph[$u]);
                for (; $ptr[$u] < $cnt; ++$ptr[$u]) {
                    $eid = $graph[$u][$ptr[$u]];
                    $v   = $to[$eid];
                    if ($cap[$eid] > 0 && $level[$v] == $level[$u] + 1) {
                        $ret = $dfs($v, min($f, $cap[$eid]));
                        if ($ret > 0) {
                            $cap[$eid] -= $ret;
                            $cap[$rev[$eid]] += $ret;
                            return $ret;
                        }
                    }
                }
                return 0;
            };

            while (true) {
                $pushed = $dfs($src, PHP_INT_MAX);
                if ($pushed == 0) break;
                $flow += $pushed;
                if ($flow >= $INF_FLOW) break 2; // enough to decide
            }
        }

        if ($flow >= 2) return false; // cannot disconnect with one flip

        // flow is 0 (already disconnected) or 1 (unique path)
        // need at least one internal cell on the unique path
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] == 1 && $reachStart[$i][$j] && $reachEnd[$i][$j]) {
                    if (!($i == 0 && $j == 0) && !($i == $m-1 && $j == $n-1)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isPossibleToCutPath(_ grid: [[Int]]) -> Bool {
        let m = grid.count
        let n = grid[0].count
        let MOD = 1_000_000_007

        // forward DP
        var f = Array(repeating: Array(repeating: 0, count: n), count: m)
        if grid[0][0] == 1 {
            f[0][0] = 1
        }
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 0 { continue }
                if i > 0 {
                    f[i][j] = (f[i][j] + f[i - 1][j]) % MOD
                }
                if j > 0 {
                    f[i][j] = (f[i][j] + f[i][j - 1]) % MOD
                }
            }
        }

        let total = f[m - 1][n - 1]
        // already disconnected
        if total == 0 { return true }

        // backward DP
        var b = Array(repeating: Array(repeating: 0, count: n), count: m)
        if grid[m - 1][n - 1] == 1 {
            b[m - 1][n - 1] = 1
        }
        for i in stride(from: m - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                if grid[i][j] == 0 { continue }
                if i + 1 < m {
                    b[i][j] = (b[i][j] + b[i + 1][j]) % MOD
                }
                if j + 1 < n {
                    b[i][j] = (b[i][j] + b[i][j + 1]) % MOD
                }
            }
        }

        // check for a critical cell
        for i in 0..<m {
            for j in 0..<n {
                if (i == 0 && j == 0) || (i == m - 1 && j == n - 1) { continue }
                if grid[i][j] == 0 { continue }
                let prod = Int((Int64(f[i][j]) * Int64(b[i][j])) % Int64(MOD))
                if prod == total {
                    return true
                }
            }
        }

        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPossibleToCutPath(grid: Array<IntArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        // reachable from start
        val reachFromStart = Array(m) { BooleanArray(n) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    if (i == 0 && j == 0) {
                        reachFromStart[i][j] = true
                    } else {
                        val up = i > 0 && reachFromStart[i - 1][j]
                        val left = j > 0 && reachFromStart[i][j - 1]
                        reachFromStart[i][j] = up || left
                    }
                }
            }
        }
        // if already disconnected
        if (!reachFromStart[m - 1][n - 1]) return true

        // reachable to end (reverse)
        val reachToEnd = Array(m) { BooleanArray(n) }
        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (grid[i][j] == 1) {
                    if (i == m - 1 && j == n - 1) {
                        reachToEnd[i][j] = true
                    } else {
                        val down = i + 1 < m && reachToEnd[i + 1][j]
                        val right = j + 1 < n && reachToEnd[i][j + 1]
                        reachToEnd[i][j] = down || right
                    }
                }
            }
        }

        // count cells on each layer that lie on some path
        val totalLayers = m + n - 1
        val cnt = IntArray(totalLayers)
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (reachFromStart[i][j] && reachToEnd[i][j]) {
                    cnt[i + j]++
                }
            }
        }

        // check for a unique cell on any intermediate layer
        for (layer in 1 until totalLayers - 1) { // exclude start and end layers
            if (cnt[layer] == 1) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isPossibleToCutPath(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // Reachable from (0,0)
    List<List<bool>> fromStart =
        List.generate(m, (_) => List.filled(n, false));
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          if (i == 0 && j == 0) {
            fromStart[i][j] = true;
          } else {
            bool up = i > 0 && fromStart[i - 1][j];
            bool left = j > 0 && fromStart[i][j - 1];
            fromStart[i][j] = up || left;
          }
        }
      }
    }

    // Already disconnected
    if (!fromStart[m - 1][n - 1]) return true;

    // Reachable to (m-1,n-1)
    List<List<bool>> toEnd =
        List.generate(m, (_) => List.filled(n, false));
    for (int i = m - 1; i >= 0; i--) {
      for (int j = n - 1; j >= 0; j--) {
        if (grid[i][j] == 1) {
          if (i == m - 1 && j == n - 1) {
            toEnd[i][j] = true;
          } else {
            bool down = i + 1 < m && toEnd[i + 1][j];
            bool right = j + 1 < n && toEnd[i][j + 1];
            toEnd[i][j] = down || right;
          }
        }
      }
    }

    int maxDiag = m + n - 2; // sum of indices for (m-1,n-1)

    for (int d = 0; d <= maxDiag; d++) {
      int cnt = 0;

      int startI = d - (n - 1);
      if (startI < 0) startI = 0;
      int endI = d;
      if (endI > m - 1) endI = m - 1;

      for (int i = startI; i <= endI; i++) {
        int j = d - i;
        if (j < 0 || j >= n) continue;
        if (fromStart[i][j] && toEnd[i][j]) {
          cnt++;
          if (cnt > 1) break;
        }
      }

      if (cnt == 1 && d != 0 && d != maxDiag) return true;
    }

    return false;
  }
}
```

## Golang

```go
type edge struct {
	to   int
	rev  int
	cap  int
}

func isPossibleToCutPath(grid [][]int) bool {
	m := len(grid)
	n := len(grid[0])
	if m == 1 && n == 1 {
		return false
	}
	totalCells := m * n
	nodeCount := totalCells * 2
	graph := make([][]edge, nodeCount)

	addEdge := func(u, v, c int) {
		graph[u] = append(graph[u], edge{to: v, rev: len(graph[v]), cap: c})
		graph[v] = append(graph[v], edge{to: u, rev: len(graph[u]) - 1, cap: 0})
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				continue
			}
			idx := i*n + j
			inNode := idx * 2
			outNode := idx*2 + 1
			capacity := 1
			if (i == 0 && j == 0) || (i == m-1 && j == n-1) {
				capacity = 2 // enough for flow up to 2
			}
			addEdge(inNode, outNode, capacity)

			if j+1 < n && grid[i][j+1] == 1 {
				nbIdx := i*n + (j + 1)
				nbIn := nbIdx * 2
				addEdge(outNode, nbIn, 2) // infinite for our purpose
			}
			if i+1 < m && grid[i+1][j] == 1 {
				nbIdx := (i+1)*n + j
				nbIn := nbIdx * 2
				addEdge(outNode, nbIn, 2)
			}
		}
	}

	srcOut := 0*2 + 1
	sinkIn := ((m-1)*n + (n - 1)) * 2

	level := make([]int, nodeCount)

	bfs := func() bool {
		for i := range level {
			level[i] = -1
		}
		queue := []int{srcOut}
		level[srcOut] = 0
		for head := 0; head < len(queue); head++ {
			v := queue[head]
			for _, e := range graph[v] {
				if e.cap > 0 && level[e.to] == -1 {
					level[e.to] = level[v] + 1
					queue = append(queue, e.to)
				}
			}
		}
		return level[sinkIn] != -1
	}

	var dfs func(v, f int) int
	dfs = func(v, f int) int {
		if v == sinkIn {
			return f
		}
		for i := 0; i < len(graph[v]); i++ {
			e := &graph[v][i]
			if e.cap > 0 && level[e.to] == level[v]+1 {
				minf := f
				if e.cap < minf {
					minf = e.cap
				}
				pushed := dfs(e.to, minf)
				if pushed > 0 {
					e.cap -= pushed
					rev := &graph[e.to][e.rev]
					rev.cap += pushed
					return pushed
				}
			}
		}
		level[v] = -1
		return 0
	}

	flow := 0
	for flow < 2 && bfs() {
		for {
			pushed := dfs(srcOut, 2-flow)
			if pushed == 0 {
				break
			}
			flow += pushed
			if flow >= 2 {
				break
			}
		}
	}

	return flow < 2
}
```

## Ruby

```ruby
def is_possible_to_cut_path(grid)
  m = grid.length
  n = grid[0].length

  # forward reachability from (0,0)
  fwd = Array.new(m) { Array.new(n, false) }
  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] == 0
      if i == 0 && j == 0
        fwd[i][j] = true
      else
        fwd[i][j] = (i > 0 && fwd[i - 1][j]) || (j > 0 && fwd[i][j - 1])
      end
    end
  end

  # already disconnected
  return true unless fwd[m - 1][n - 1]

  # backward reachability to (m-1,n-1)
  bwd = Array.new(m) { Array.new(n, false) }
  (m - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      next if grid[i][j] == 0
      if i == m - 1 && j == n - 1
        bwd[i][j] = true
      else
        bwd[i][j] = (i + 1 < m && bwd[i + 1][j]) || (j + 1 < n && bwd[i][j + 1])
      end
    end
  end

  max_sum = m + n - 2
  cnt = Array.new(max_sum + 1, 0)

  (0...m).each do |i|
    (0...n).each do |j|
      if fwd[i][j] && bwd[i][j]
        s = i + j
        cnt[s] += 1
      end
    end
  end

  # check for a diagonal with exactly one viable internal cell
  (1...max_sum).each do |s|
    return true if cnt[s] == 1
  end

  false
end
```

## Scala

```scala
object Solution {
    def isPossibleToCutPath(grid: Array[Array[Int]]): Boolean = {
        val m = grid.length
        val n = grid(0).length

        // forward reachable from (0,0)
        val reachFromStart = Array.ofDim[Boolean](m, n)
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (grid(i)(j) == 1) {
                    if (i == 0 && j == 0) {
                        reachFromStart(i)(j) = true
                    } else {
                        val up   = if (i > 0) reachFromStart(i - 1)(j) else false
                        val left = if (j > 0) reachFromStart(i)(j - 1) else false
                        reachFromStart(i)(j) = up || left
                    }
                }
            }
        }

        // already disconnected
        if (!reachFromStart(m - 1)(n - 1)) return true

        // backward reachable to (m-1,n-1)
        val canReachEnd = Array.ofDim[Boolean](m, n)
        for (i <- (0 until m).reverse) {
            for (j <- (0 until n).reverse) {
                if (grid(i)(j) == 1) {
                    if (i == m - 1 && j == n - 1) {
                        canReachEnd(i)(j) = true
                    } else {
                        val down  = if (i + 1 < m) canReachEnd(i + 1)(j) else false
                        val right = if (j + 1 < n) canReachEnd(i)(j + 1) else false
                        canReachEnd(i)(j) = down || right
                    }
                }
            }
        }

        // count viable cells per diagonal layer (i+j)
        val layers = m + n - 1
        val cnt = new Array[Int](layers)
        for (i <- 0 until m; j <- 0 until n) {
            if (reachFromStart(i)(j) && canReachEnd(i)(j)) {
                cnt(i + j) += 1
            }
        }

        // any internal layer with exactly one viable cell -> cut possible
        for (k <- 1 until layers - 1) {
            if (cnt(k) == 1) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_possible_to_cut_path(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();

        // forward reachable from (0,0)
        let mut f = vec![vec![false; n]; m];
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    if i == 0 && j == 0 {
                        f[i][j] = true;
                    } else {
                        let up = if i > 0 { f[i - 1][j] } else { false };
                        let left = if j > 0 { f[i][j - 1] } else { false };
                        f[i][j] = up || left;
                    }
                }
            }
        }

        // already disconnected
        if !f[m - 1][n - 1] {
            return true;
        }

        // backward reachable to (m-1,n-1)
        let mut b = vec![vec![false; n]; m];
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                if grid[i][j] == 1 {
                    if i == m - 1 && j == n - 1 {
                        b[i][j] = true;
                    } else {
                        let down = if i + 1 < m { b[i + 1][j] } else { false };
                        let right = if j + 1 < n { b[i][j + 1] } else { false };
                        b[i][j] = down || right;
                    }
                }
            }
        }

        let total_dist = m + n - 2; // distance from start to end
        let mut cnt = vec![0usize; total_dist + 1];
        for i in 0..m {
            for j in 0..n {
                if f[i][j] && b[i][j] {
                    let d = i + j;
                    cnt[d] += 1;
                }
            }
        }

        // check each layer (excluding start and end) for a unique critical cell
        for d in 1..total_dist {
            if cnt[d] == 1 {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (is-possible-to-cut-path grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (first grid))))
         (gridv (list->vector (map list->vector grid)))
         (dp1 (make-vector m))
         (dp2 (make-vector m)))
    ;; initialise dp tables
    (for ([i (in-range m)])
      (vector-set! dp1 i (make-vector n #f))
      (vector-set! dp2 i (make-vector n #f)))
    ;; forward reachability
    (for ([i (in-range m)])
      (for ([j (in-range n)])
        (when (= (vector-ref (vector-ref gridv i) j) 1)
          (if (and (= i 0) (= j 0))
              (vector-set! (vector-ref dp1 i) j #t)
              (let ((up   (and (> i 0) (vector-ref (vector-ref dp1 (- i 1)) j)))
                    (left (and (> j 0) (vector-ref (vector-ref dp1 i)       (- j 1)))))
                (when (or up left)
                  (vector-set! (vector-ref dp1 i) j #t)))))))
    ;; backward reachability
    (for ([i (in-range (sub1 m) -1 -1)])
      (for ([j (in-range (sub1 n) -1 -1)])
        (when (= (vector-ref (vector-ref gridv i) j) 1)
          (if (and (= i (sub1 m)) (= j (sub1 n)))
              (vector-set! (vector-ref dp2 i) j #t)
              (let ((down  (and (< i (sub1 m)) (vector-ref (vector-ref dp2 (+ i 1)) j)))
                    (right (and (< j (sub1 n)) (vector-ref (vector-ref dp2 i)       (+ j 1)))))
                (when (or down right)
                  (vector-set! (vector-ref dp2 i) j #t)))))))
    ;; already disconnected?
    (if (not (vector-ref (vector-ref dp1 (sub1 m)) (sub1 n)))
        #t
        (let loop ((s 1) (max-s (+ m n -3))) ; sums from 1 to m+n-3 inclusive
          (cond [(> s max-s) #f]
                [else
                 (define cnt
                   (let ((c 0))
                     (for* ([i (in-range m)]
                            [j (in-range n)])
                       (when (= (+ i j) s)
                         (when (and (vector-ref (vector-ref dp1 i) j)
                                    (vector-ref (vector-ref dp2 i) j))
                           (set! c (+ c 1)))))
                     c))
                 (if (= cnt 1)
                     #t
                     (loop (+ s 1) max-s))])))))
```

## Erlang

```erlang
-spec is_possible_to_cut_path(Grid :: [[integer()]]) -> boolean().
is_possible_to_cut_path(Grid) ->
    M = length(Grid),
    N = case Grid of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    ForwardRows = forward(Grid),
    EndReachable =
        case lists:nth(M, ForwardRows) of
            RowEnd -> lists:nth(N, RowEnd)
        end,
    if not EndReachable ->
            true;
       true ->
            RevGrid = [lists:reverse(R) || R <- lists:reverse(Grid)],
            ForwardRevRows = forward(RevGrid),
            BackwardRows = [lists:reverse(R) || R <- lists:reverse(ForwardRevRows)],
            MaxDist = M + N - 2,
            CountsMap = count_paths(ForwardRows, BackwardRows, 0, #{}),
            maps:fold(
                fun(Dist, Count, Acc) ->
                    if Dist > 0 andalso Dist < MaxDist andalso Count == 1 -> true;
                       true -> Acc
                    end
                end,
                false,
                CountsMap)
    end.

%% compute forward reachable matrix
forward(Grid) ->
    forward_rows(Grid, 0, [], []).

forward_rows([], _RowIdx, _PrevRow, AccRows) ->
    lists:reverse(AccRows);
forward_rows([RowVals|Rest], RowIdx, PrevRow, AccRows) ->
    CurrRow = process_row(RowVals, PrevRow, RowIdx),
    forward_rows(Rest, RowIdx + 1, CurrRow, [CurrRow | AccRows]).

process_row(RowVals, PrevRow, RowIdx) ->
    process_cells(RowVals, PrevRow, RowIdx, 0, false, []).

process_cells([], [], _RowIdx, _ColIdx, _LeftReachable, Acc) ->
    lists:reverse(Acc);
process_cells([Cell|RestCells], [], RowIdx, ColIdx, LeftReachable, Acc) ->
    Reach =
        if Cell =:= 1 ->
                (RowIdx =:= 0 andalso ColIdx =:= 0) orelse LeftReachable;
           true -> false
        end,
    process_cells(RestCells, [], RowIdx, ColIdx + 1, Reach, [Reach | Acc]);
process_cells([Cell|RestCells], [Above|RestPrev], RowIdx, ColIdx, LeftReachable, Acc) ->
    Reach =
        if Cell =:= 1 ->
                (RowIdx =:= 0 andalso ColIdx =:= 0) orelse Above orelse LeftReachable;
           true -> false
        end,
    process_cells(RestCells, RestPrev, RowIdx, ColIdx + 1, Reach, [Reach | Acc]).

%% count cells that lie on some path per distance
count_paths([], [], _I, Map) ->
    Map;
count_paths([FRow|FRest], [BRow|BRest], I, Map) ->
    NewMap = count_row(FRow, BRow, I, 0, Map),
    count_paths(FRest, BRest, I + 1, NewMap).

count_row([], [], _I, _J, Map) ->
    Map;
count_row([F|FRest], [B|BRest], I, J, Map) ->
    UpdatedMap =
        case (F andalso B) of
            true ->
                Dist = I + J,
                Prev = maps:get(Dist, Map, 0),
                maps:put(Dist, Prev + 1, Map);
            false -> Map
        end,
    count_row(FRest, BRest, I, J + 1, UpdatedMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_possible_to_cut_path(grid :: [[integer]]) :: boolean
  def is_possible_to_cut_path(grid) do
    m = length(grid)
    n = grid |> List.first() |> length()

    # Special case: start equals end (1x1) or no internal cells
    if m == 1 and n == 1 do
      false
    else
      # Forward reachable DP
      forward =
        Enum.reduce(0..(m - 1), [], fn i, acc_rev ->
          prev_row = case acc_rev do
            [] -> List.duplicate(false, n)
            [h | _] -> h
          end

          cur_grid_row = Enum.at(grid, i)

          cur_forward_row =
            Enum.reduce(0..(n - 1), [], fn j, row_acc_rev ->
              left = case row_acc_rev do
                [] -> false
                [h | _] -> h
              end

              up = if i > 0, do: Enum.at(prev_row, j), else: false

              reachable =
                (Enum.at(cur_grid_row, j) == 1) and
                  ((i == 0 and j == 0) or up or left)

              [reachable | row_acc_rev]
            end)
            |> Enum.reverse()

          [cur_forward_row | acc_rev]
        end)
        |> Enum.reverse()

      # If end not reachable, already disconnected
      if not Enum.at(Enum.at(forward, m - 1), n - 1) do
        true
      else
        # Backward reachable DP (from end moving up/left)
        backward =
          Enum.reduce((m - 1)..0, [], fn i, acc_rev ->
            next_row = case acc_rev do
              [] -> List.duplicate(false, n)
              [h | _] -> h
            end

            cur_grid_row = Enum.at(grid, i)

            cur_backward_row =
              Enum.reduce((n - 1)..0, [], fn j, row_acc_rev ->
                right = case row_acc_rev do
                  [] -> false
                  [h | _] -> h
                end

                down = if i < m - 1, do: Enum.at(next_row, j), else: false

                reachable =
                  (Enum.at(cur_grid_row, j) == 1) and
                    ((i == m - 1 and j == n - 1) or down or right)

                [reachable | row_acc_rev]
              end)
              |> Enum.reverse()

            [cur_backward_row | acc_rev]
          end)
          |> Enum.reverse()

        # Count cells on some path per layer (i + j)
        counts =
          Enum.reduce(0..(m - 1), %{}, fn i, map ->
            row_f = Enum.at(forward, i)
            row_b = Enum.at(backward, i)

            Enum.reduce(0..(n - 1), map, fn j, acc ->
              if Enum.at(row_f, j) and Enum.at(row_b, j) do
                k = i + j
                Map.update(acc, k, 1, &(&1 + 1))
              else
                acc
              end
            end)
          end)

        total_layers = m + n - 2

        # Find minimal count among internal layers (exclude start layer 0 and end layer total_layers)
        min_count =
          Enum.reduce(1..(total_layers - 1), :infinity, fn k, cur_min ->
            cnt = Map.get(counts, k, 0)
            if cnt < cur_min, do: cnt, else: cur_min
          end)

        # If there is no internal layer (grid size 1x2 or 2x1) min_count stays :infinity -> treat as false
        cond do
          min_count == :infinity -> false
          min_count <= 1 -> true
          true -> false
        end
      end
    end
  end
end
```

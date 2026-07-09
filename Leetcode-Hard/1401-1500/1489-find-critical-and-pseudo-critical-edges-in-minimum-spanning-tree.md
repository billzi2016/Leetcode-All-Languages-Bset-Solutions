# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> p, r;
        DSU(int n): p(n), r(n,0) { iota(p.begin(), p.end(), 0); }
        int find(int x){ return p[x]==x?x:p[x]=find(p[x]); }
        bool unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return false;
            if(r[a]<r[b]) swap(a,b);
            p[b]=a;
            if(r[a]==r[b]) ++r[a];
            return true;
        }
    };
    
    struct Edge {
        int u,v,w,idx;
    };
    
    long long mstWeight(int n, const vector<Edge>& edges, int skipIdx, int forceIdx) {
        DSU dsu(n);
        long long total = 0;
        int used = 0;
        if (forceIdx != -1) {
            const Edge& e = edges[forceIdx];
            if (dsu.unite(e.u, e.v)) {
                total += e.w;
                ++used;
            }
        }
        for (int i = 0; i < (int)edges.size(); ++i) {
            if (i == skipIdx || i == forceIdx) continue;
            const Edge& e = edges[i];
            if (dsu.unite(e.u, e.v)) {
                total += e.w;
                ++used;
                if (used == n-1) break;
            }
        }
        return used == n-1 ? total : (long long)4e18;
    }
    
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edgesInput) {
        int m = edgesInput.size();
        vector<Edge> edges(m);
        for (int i = 0; i < m; ++i) {
            edges[i] = {edgesInput[i][0], edgesInput[i][1], edgesInput[i][2], i};
        }
        sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b){ return a.w < b.w; });
        
        // map sorted position to original index for skip/force handling
        vector<int> posToIdx(m);
        for (int i = 0; i < m; ++i) posToIdx[i] = edges[i].idx;
        
        long long baseWeight = mstWeight(n, edges, -1, -1);
        vector<int> critical, pseudo;
        for (int i = 0; i < m; ++i) {
            // Critical test: skip this edge
            long long wSkip = mstWeight(n, edges, i, -1);
            if (wSkip > baseWeight) {
                critical.push_back(edges[i].idx);
            } else {
                // Pseudo-critical test: force include this edge
                long long wForce = mstWeight(n, edges, -1, i);
                if (wForce == baseWeight) {
                    pseudo.push_back(edges[i].idx);
                }
            }
        }
        return {critical, pseudo};
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int u, v, w, idx;
        Edge(int u, int v, int w, int idx) {
            this.u = u;
            this.v = v;
            this.w = w;
            this.idx = idx;
        }
    }

    static class DSU {
        int[] parent, rank;
        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        boolean union(int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return false;
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb;
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra;
            } else {
                parent[rb] = ra;
                rank[ra]++;
            }
            return true;
        }
    }

    private int kruskal(int n, Edge[] edges, Edge forced, int skipIdx) {
        DSU dsu = new DSU(n);
        int weight = 0;
        int used = 0;

        if (forced != null) {
            if (dsu.union(forced.u, forced.v)) {
                weight += forced.w;
                used++;
            }
        }

        for (Edge e : edges) {
            if (e.idx == skipIdx) continue;
            if (forced != null && e.idx == forced.idx) continue;
            if (dsu.union(e.u, e.v)) {
                weight += e.w;
                used++;
                if (used == n - 1) break;
            }
        }

        return used == n - 1 ? weight : Integer.MAX_VALUE;
    }

    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edgesInput) {
        int m = edgesInput.length;
        Edge[] edges = new Edge[m];
        for (int i = 0; i < m; i++) {
            edges[i] = new Edge(edgesInput[i][0], edgesInput[i][1], edgesInput[i][2], i);
        }
        Arrays.sort(edges, Comparator.comparingInt(e -> e.w));

        int originalMST = kruskal(n, edges, null, -1);

        List<Integer> critical = new ArrayList<>();
        List<Integer> pseudo = new ArrayList<>();

        for (Edge e : edges) {
            // Test if edge is critical
            int weightWithout = kruskal(n, edges, null, e.idx);
            if (weightWithout > originalMST) {
                critical.add(e.idx);
            } else {
                // Test if edge is pseudo-critical
                int weightWith = kruskal(n, edges, e, -1);
                if (weightWith == originalMST) {
                    pseudo.add(e.idx);
                }
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        result.add(critical);
        result.add(pseudo);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        # augment edges with original index
        indexed_edges = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[0])

        class UnionFind:
            __slots__ = ('parent', 'rank')
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0] * size
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return False
                if self.rank[ra] < self.rank[rb]:
                    self.parent[ra] = rb
                elif self.rank[ra] > self.rank[rb]:
                    self.parent[rb] = ra
                else:
                    self.parent[rb] = ra
                    self.rank[ra] += 1
                return True

        def mst(skip_idx=None, force_idx=None):
            uf = UnionFind(n)
            total = 0
            edges_used = 0
            # if we must include an edge first
            if force_idx is not None:
                w, u, v, i = indexed_edges[force_idx]
                if uf.union(u, v):
                    total += w
                    edges_used += 1
            for idx, (w, u, v, i) in enumerate(indexed_edges):
                if i == skip_idx or i == (indexed_edges[force_idx][3] if force_idx is not None else -1):
                    continue
                if uf.union(u, v):
                    total += w
                    edges_used += 1
                    if edges_used == n - 1:
                        break
            return total if edges_used == n - 1 else float('inf')

        # compute original MST weight
        orig_weight = mst()

        critical = []
        pseudo = []

        # map from edge index to its position in sorted list for fast force lookup
        idx_to_pos = {i: pos for pos, (_, _, _, i) in enumerate(indexed_edges)}

        for i in range(len(edges)):
            if mst(skip_idx=i) > orig_weight:
                critical.append(i)
            elif mst(force_idx=idx_to_pos[i]) == orig_weight:
                pseudo.append(i)

        return [critical, pseudo]
```

## Python3

```python
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # store edge info with original index
        indexed_edges = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        sorted_edges = sorted(indexed_edges, key=lambda x: x[0])
        edge_by_idx = {i: (w, u, v) for w, u, v, i in indexed_edges}
        INF = float('inf')

        def mst(skip: int = -1, force: int = -1) -> int:
            uf = UnionFind(n)
            total = 0
            used = 0
            if force != -1:
                w, u, v = edge_by_idx[force]
                if uf.union(u, v):
                    total += w
                    used += 1
            for w, u, v, idx in sorted_edges:
                if idx == skip or idx == force:
                    continue
                if uf.union(u, v):
                    total += w
                    used += 1
                    if used == n - 1:
                        break
            return total if used == n - 1 else INF

        original_weight = mst()
        critical = []
        pseudo = []

        for i in range(len(edges)):
            # test critical
            if mst(skip=i) > original_weight:
                critical.append(i)
            else:
                # test pseudo-critical
                if mst(force=i) == original_weight:
                    pseudo.append(i)

        return [critical, pseudo]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef struct {
    int u;
    int v;
    int w;
    int idx;
} Edge;

static int cmp_edge(const void *a, const void *b) {
    const Edge *ea = (const Edge *)a;
    const Edge *eb = (const Edge *)b;
    if (ea->w != eb->w) return ea->w - eb->w;
    return ea->idx - eb->idx;
}

static int find_set(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static int union_set(int *parent, int *rank, int a, int b) {
    int pa = find_set(parent, a);
    int pb = find_set(parent, b);
    if (pa == pb) return 0;
    if (rank[pa] < rank[pb]) parent[pa] = pb;
    else if (rank[pa] > rank[pb]) parent[pb] = pa;
    else {
        parent[pb] = pa;
        rank[pa]++;
    }
    return 1;
}

/* Kruskal with optional skip or forced edge.
   skipIdx / forcedIdx refer to positions in the sorted edges array. */
static int kruskal(int n, Edge *edges, int m, int skipIdx, int forcedIdx) {
    int *parent = (int *)malloc(n * sizeof(int));
    int *rank = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    int totalWeight = 0;
    int used = 0;

    if (forcedIdx != -1) {
        Edge e = edges[forcedIdx];
        if (union_set(parent, rank, e.u, e.v)) {
            totalWeight += e.w;
            used++;
        }
    }

    for (int i = 0; i < m; ++i) {
        if (i == skipIdx || i == forcedIdx) continue;
        Edge e = edges[i];
        if (union_set(parent, rank, e.u, e.v)) {
            totalWeight += e.w;
            used++;
            if (used == n - 1) break;
        }
    }

    free(parent);
    free(rank);
    return (used == n - 1) ? totalWeight : INT_MAX;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findCriticalAndPseudoCriticalEdges(int n, int** edges, int edgesSize, int* edgesColSize,
                                         int* returnSize, int*** returnColumnSizes) {
    (void)edgesColSize; // unused

    Edge *sorted = (Edge *)malloc(edgesSize * sizeof(Edge));
    for (int i = 0; i < edgesSize; ++i) {
        sorted[i].u = edges[i][0];
        sorted[i].v = edges[i][1];
        sorted[i].w = edges[i][2];
        sorted[i].idx = i;
    }
    qsort(sorted, edgesSize, sizeof(Edge), cmp_edge);

    int originalWeight = kruskal(n, sorted, edgesSize, -1, -1);

    int *critTmp = (int *)malloc(edgesSize * sizeof(int));
    int *pseudoTmp = (int *)malloc(edgesSize * sizeof(int));
    int critCnt = 0, pseudoCnt = 0;

    for (int i = 0; i < edgesSize; ++i) {
        int wSkip = kruskal(n, sorted, edgesSize, i, -1);
        if (wSkip > originalWeight) {
            critTmp[critCnt++] = sorted[i].idx;
        } else {
            int wForce = kruskal(n, sorted, edgesSize, -1, i);
            if (wForce == originalWeight) {
                pseudoTmp[pseudoCnt++] = sorted[i].idx;
            }
        }
    }

    int **result = (int **)malloc(2 * sizeof(int *));
    int *colSizes = (int *)malloc(2 * sizeof(int));

    result[0] = (int *)malloc(critCnt * sizeof(int));
    memcpy(result[0], critTmp, critCnt * sizeof(int));
    colSizes[0] = critCnt;

    result[1] = (int *)malloc(pseudoCnt * sizeof(int));
    memcpy(result[1], pseudoTmp, pseudoCnt * sizeof(int));
    colSizes[1] = pseudoCnt;

    free(critTmp);
    free(pseudoTmp);
    free(sorted);

    *returnSize = 2;
    *returnColumnSizes = &colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    private class Edge {
        public int u;
        public int v;
        public int w;
        public int idx;
        public Edge(int u, int v, int w, int idx) {
            this.u = u;
            this.v = v;
            this.w = w;
            this.idx = idx;
        }
    }

    private class DSU {
        private int[] parent;
        private int[] rank;
        public DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }
        public int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        public bool Union(int a, int b) {
            int pa = Find(a);
            int pb = Find(b);
            if (pa == pb) return false;
            if (rank[pa] < rank[pb]) {
                parent[pa] = pb;
            } else if (rank[pa] > rank[pb]) {
                parent[pb] = pa;
            } else {
                parent[pb] = pa;
                rank[pa]++;
            }
            return true;
        }
    }

    private int Kruskal(int n, Edge[] edges, int skipIdx, Edge forced) {
        DSU dsu = new DSU(n);
        int weight = 0;
        int used = 0;
        if (forced != null) {
            if (dsu.Union(forced.u, forced.v)) {
                weight += forced.w;
                used++;
            }
        }
        foreach (var e in edges) {
            if (e.idx == skipIdx) continue;
            if (forced != null && e.idx == forced.idx) continue;
            if (dsu.Union(e.u, e.v)) {
                weight += e.w;
                used++;
                if (used == n - 1) break;
            }
        }
        return used == n - 1 ? weight : int.MaxValue;
    }

    public IList<IList<int>> FindCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        int m = edges.Length;
        Edge[] edgeObjs = new Edge[m];
        for (int i = 0; i < m; i++) {
            edgeObjs[i] = new Edge(edges[i][0], edges[i][1], edges[i][2], i);
        }
        Array.Sort(edgeObjs, (a, b) => a.w.CompareTo(b.w));
        int originalWeight = Kruskal(n, edgeObjs, -1, null);

        List<int> critical = new List<int>();
        List<int> pseudo = new List<int>();

        foreach (var e in edgeObjs) {
            int wSkip = Kruskal(n, edgeObjs, e.idx, null);
            if (wSkip > originalWeight) {
                critical.Add(e.idx);
            } else {
                int wForce = Kruskal(n, edgeObjs, -1, e);
                if (wForce == originalWeight) {
                    pseudo.Add(e.idx);
                }
            }
        }

        IList<IList<int>> result = new List<IList<int>>(2);
        result.Add(critical);
        result.Add(pseudo);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[][]}
 */
var findCriticalAndPseudoCriticalEdges = function(n, edges) {
    class UnionFind {
        constructor(size) {
            this.parent = new Array(size);
            this.rank = new Array(size).fill(0);
            for (let i = 0; i < size; i++) this.parent[i] = i;
        }
        find(x) {
            while (this.parent[x] !== x) {
                this.parent[x] = this.parent[this.parent[x]];
                x = this.parent[x];
            }
            return x;
        }
        union(a, b) {
            let pa = this.find(a), pb = this.find(b);
            if (pa === pb) return false;
            if (this.rank[pa] < this.rank[pb]) [pa, pb] = [pb, pa];
            this.parent[pb] = pa;
            if (this.rank[pa] === this.rank[pb]) this.rank[pa]++;
            return true;
        }
    }

    const sortedEdges = edges.map((e, idx) => [e[0], e[1], e[2], idx])
                             .sort((a, b) => a[2] - b[2]);

    const INF = Number.MAX_SAFE_INTEGER;

    function kruskal(skipEdgeIdx, forcedEdgeIdx) {
        const uf = new UnionFind(n);
        let totalWeight = 0;
        let used = 0;

        if (forcedEdgeIdx !== -1) {
            for (const e of sortedEdges) {
                if (e[3] === forcedEdgeIdx) {
                    if (uf.union(e[0], e[1])) {
                        totalWeight += e[2];
                        used++;
                    }
                    break;
                }
            }
        }

        for (const e of sortedEdges) {
            const [u, v, w, idx] = e;
            if (idx === skipEdgeIdx || idx === forcedEdgeIdx) continue;
            if (uf.union(u, v)) {
                totalWeight += w;
                used++;
                if (used === n - 1) break;
            }
        }

        return used === n - 1 ? totalWeight : INF;
    }

    const originalMST = kruskal(-1, -1);
    const critical = [];
    const pseudo = [];

    for (let i = 0; i < edges.length; i++) {
        // Test if edge i is critical
        const weightWithout = kruskal(i, -1);
        if (weightWithout > originalMST) {
            critical.push(i);
        } else {
            // Test if edge i can be pseudo‑critical
            const weightWith = kruskal(-1, i);
            if (weightWith === originalMST) {
                pseudo.push(i);
            }
        }
    }

    return [critical, pseudo];
};
```

## Typescript

```typescript
function findCriticalAndPseudoCriticalEdges(n: number, edges: number[][]): number[][] {
    class UnionFind {
        parent: number[];
        rank: number[];
        constructor(size: number) {
            this.parent = new Array(size);
            this.rank = new Array(size).fill(0);
            for (let i = 0; i < size; i++) this.parent[i] = i;
        }
        find(x: number): number {
            if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
            return this.parent[x];
        }
        union(a: number, b: number): boolean {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return false;
            if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
            this.parent[rb] = ra;
            if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
            return true;
        }
    }

    const m = edges.length;
    const edgeObjs: { u: number; v: number; w: number; idx: number }[] = edges.map((e, i) => ({
        u: e[0],
        v: e[1],
        w: e[2],
        idx: i,
    }));
    const sortedEdges = [...edgeObjs].sort((a, b) => a.w - b.w);

    function mstWeight(skipIdx?: number, forceIdx?: number): number {
        const uf = new UnionFind(n);
        let total = 0;
        let used = 0;

        if (forceIdx !== undefined) {
            const e = edgeObjs[forceIdx];
            if (uf.union(e.u, e.v)) {
                total += e.w;
                used++;
            }
        }

        for (const e of sortedEdges) {
            if (e.idx === skipIdx) continue;
            if (forceIdx !== undefined && e.idx === forceIdx) continue;
            if (uf.union(e.u, e.v)) {
                total += e.w;
                used++;
                if (used === n - 1) break;
            }
        }

        return used === n - 1 ? total : Number.MAX_SAFE_INTEGER;
    }

    const originalWeight = mstWeight();

    const critical: number[] = [];
    const pseudo: number[] = [];

    for (let i = 0; i < m; i++) {
        const weightWithout = mstWeight(i);
        if (weightWithout > originalWeight) {
            critical.push(i);
        } else {
            const weightWith = mstWeight(undefined, i);
            if (weightWith === originalWeight) pseudo.push(i);
        }
    }

    return [critical, pseudo];
}
```

## Php

```php
class UnionFind {
    public array $parent;
    public array $rank;

    public function __construct(int $size) {
        $this->parent = range(0, $size - 1);
        $this->rank = array_fill(0, $size, 0);
    }

    public function find(int $x): int {
        while ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->parent[$this->parent[$x]];
            $x = $this->parent[$x];
        }
        return $x;
    }

    public function union(int $x, int $y): bool {
        $rootX = $this->find($x);
        $rootY = $this->find($y);
        if ($rootX === $rootY) {
            return false;
        }
        if ($this->rank[$rootX] < $this->rank[$rootY]) {
            $this->parent[$rootX] = $rootY;
        } elseif ($this->rank[$rootX] > $this->rank[$rootY]) {
            $this->parent[$rootY] = $rootX;
        } else {
            $this->parent[$rootY] = $rootX;
            $this->rank[$rootX]++;
        }
        return true;
    }
}

class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[][]
     */
    function findCriticalAndPseudoCriticalEdges($n, $edges) {
        // Append original index to each edge
        $indexedEdges = [];
        foreach ($edges as $i => $e) {
            $indexedEdges[] = [$e[0], $e[1], $e[2], $i];
        }
        // Sort by weight then index
        usort($indexedEdges, function($a, $b) {
            if ($a[2] === $b[2]) {
                return $a[3] <=> $b[3];
            }
            return $a[2] <=> $b[2];
        });

        $originalWeight = $this->mstWeight($n, $indexedEdges);

        $critical = [];
        $pseudo = [];

        foreach ($indexedEdges as $edge) {
            $idx = $edge[3];

            // Test critical: skip this edge
            $weightSkip = $this->mstWeight($n, $indexedEdges, $idx);
            if ($weightSkip > $originalWeight) {
                $critical[] = $idx;
                continue;
            }

            // Test pseudo-critical: force include this edge
            $weightPick = $this->mstWeight($n, $indexedEdges, -1, $idx);
            if ($weightPick === $originalWeight) {
                $pseudo[] = $idx;
            }
        }

        return [$critical, $pseudo];
    }

    private function mstWeight(int $n, array $edges, int $skipIdx = -1, int $pickIdx = -1): int {
        $uf = new UnionFind($n);
        $total = 0;
        $used = 0;

        // If we need to force include an edge first
        if ($pickIdx !== -1) {
            foreach ($edges as $e) {
                if ($e[3] === $pickIdx) {
                    if ($uf->union($e[0], $e[1])) {
                        $total += $e[2];
                        $used++;
                    }
                    break;
                }
            }
        }

        foreach ($edges as $e) {
            $idx = $e[3];
            if ($idx === $skipIdx) continue;
            if ($pickIdx !== -1 && $idx === $pickIdx) continue; // already added
            if ($uf->union($e[0], $e[1])) {
                $total += $e[2];
                $used++;
                if ($used === $n - 1) break;
            }
        }

        return ($used === $n - 1) ? $total : PHP_INT_MAX;
    }
}
```

## Swift

```swift
class Solution {
    private struct Edge {
        let u: Int
        let v: Int
        let w: Int
        let idx: Int
    }
    
    private class DSU {
        var parent: [Int]
        var rank: [Int]
        init(_ n: Int) {
            parent = Array(0..<n)
            rank = [Int](repeating: 0, count: n)
        }
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        @discardableResult
        func union(_ a: Int, _ b: Int) -> Bool {
            var pa = find(a)
            var pb = find(b)
            if pa == pb { return false }
            if rank[pa] < rank[pb] {
                swap(&pa, &pb)
            }
            parent[pb] = pa
            if rank[pa] == rank[pb] {
                rank[pa] += 1
            }
            return true
        }
    }
    
    private func mstWeight(_ n: Int, _ edges: [Edge], _ skip: Int?, _ force: Int?) -> Int {
        let dsu = DSU(n)
        var total = 0
        var used = 0
        
        if let f = force {
            for e in edges where e.idx == f {
                if dsu.union(e.u, e.v) {
                    total += e.w
                    used += 1
                }
                break
            }
        }
        
        for e in edges {
            if let s = skip, e.idx == s { continue }
            if let f = force, e.idx == f { continue } // already taken
            if dsu.union(e.u, e.v) {
                total += e.w
                used += 1
                if used == n - 1 { break }
            }
        }
        return used == n - 1 ? total : Int.max
    }
    
    func findCriticalAndPseudoCriticalEdges(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var edgeList: [Edge] = []
        for (i, e) in edges.enumerated() {
            edgeList.append(Edge(u: e[0], v: e[1], w: e[2], idx: i))
        }
        edgeList.sort { $0.w < $1.w }
        
        let originalWeight = mstWeight(n, edgeList, nil, nil)
        var critical: [Int] = []
        var pseudo: [Int] = []
        
        for i in 0..<edges.count {
            // Check if edge i is critical
            let weightSkip = mstWeight(n, edgeList, i, nil)
            if weightSkip > originalWeight {
                critical.append(i)
            } else {
                // Check if edge i is pseudo-critical
                let weightForce = mstWeight(n, edgeList, nil, i)
                if weightForce == originalWeight {
                    pseudo.append(i)
                }
            }
        }
        
        return [critical, pseudo]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findCriticalAndPseudoCriticalEdges(n: Int, edges: Array<IntArray>): List<List<Int>> {
        data class Edge(val u: Int, val v: Int, val w: Int, val idx: Int)
        val edgeList = mutableListOf<Edge>()
        for (i in edges.indices) {
            val e = edges[i]
            edgeList.add(Edge(e[0], e[1], e[2], i))
        }
        val sortedEdges = edgeList.sortedBy { it.w }

        class UnionFind(size: Int) {
            private val parent = IntArray(size) { it }
            private val rank = IntArray(size)
            fun find(x: Int): Int {
                var v = x
                while (parent[v] != v) {
                    parent[v] = parent[parent[v]]
                    v = parent[v]
                }
                return v
            }

            fun union(a: Int, b: Int): Boolean {
                var pa = find(a)
                var pb = find(b)
                if (pa == pb) return false
                if (rank[pa] < rank[pb]) {
                    val tmp = pa; pa = pb; pb = tmp
                }
                parent[pb] = pa
                if (rank[pa] == rank[pb]) rank[pa]++
                return true
            }
        }

        fun mstWeight(skipIdx: Int = -1, forceIdx: Int = -1): Int {
            val uf = UnionFind(n)
            var total = 0
            var used = 0
            if (forceIdx != -1) {
                val e = edgeList[forceIdx]
                if (uf.union(e.u, e.v)) {
                    total += e.w
                    used++
                }
            }
            for (e in sortedEdges) {
                if (e.idx == skipIdx) continue
                if (forceIdx != -1 && e.idx == forceIdx) continue
                if (uf.union(e.u, e.v)) {
                    total += e.w
                    used++
                    if (used == n - 1) break
                }
            }
            return if (used == n - 1) total else Int.MAX_VALUE
        }

        val originalWeight = mstWeight()
        val critical = mutableListOf<Int>()
        val pseudo = mutableListOf<Int>()

        for (e in edgeList) {
            val wSkip = mstWeight(skipIdx = e.idx)
            if (wSkip > originalWeight) {
                critical.add(e.idx)
            } else {
                val wForce = mstWeight(forceIdx = e.idx)
                if (wForce == originalWeight) pseudo.add(e.idx)
            }
        }

        return listOf(critical, pseudo)
    }
}
```

## Dart

```dart
class Edge {
  int u;
  int v;
  int w;
  int idx;
  Edge(this.u, this.v, this.w, this.idx);
}

class UnionFind {
  List<int> parent;
  List<int> rank;
  UnionFind(int n)
      : parent = List.generate(n, (i) => i),
        rank = List.filled(n, 0);

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  bool union(int x, int y) {
    int rx = find(x);
    int ry = find(y);
    if (rx == ry) return false;
    if (rank[rx] < rank[ry]) {
      parent[rx] = ry;
    } else if (rank[rx] > rank[ry]) {
      parent[ry] = rx;
    } else {
      parent[ry] = rx;
      rank[rx]++;
    }
    return true;
  }
}

class Solution {
  List<List<int>> findCriticalAndPseudoCriticalEdges(int n, List<List<int>> edges) {
    int m = edges.length;
    List<Edge> edgeObjs = [];
    for (int i = 0; i < m; i++) {
      var e = edges[i];
      edgeObjs.add(Edge(e[0], e[1], e[2], i));
    }
    edgeObjs.sort((a, b) => a.w.compareTo(b.w));

    int originalWeight = _kruskal(n, edgeObjs);
    List<int> critical = [];
    List<int> pseudo = [];

    for (Edge e in edgeObjs) {
      int weightWithout = _kruskal(n, edgeObjs, skip: e.idx);
      if (weightWithout > originalWeight) {
        critical.add(e.idx);
      } else {
        int weightWith = _kruskal(n, edgeObjs, forced: e);
        if (weightWith == originalWeight) {
          pseudo.add(e.idx);
        }
      }
    }

    return [critical, pseudo];
  }

  int _kruskal(int n, List<Edge> edgesSorted, {int? skip, Edge? forced}) {
    UnionFind uf = UnionFind(n);
    int weight = 0;
    int used = 0;

    if (forced != null) {
      if (uf.union(forced.u, forced.v)) {
        weight += forced.w;
        used++;
      }
    }

    for (Edge e in edgesSorted) {
      if (skip != null && e.idx == skip) continue;
      if (uf.union(e.u, e.v)) {
        weight += e.w;
        used++;
        if (used == n - 1) break;
      }
    }

    if (used == n - 1) return weight;
    // Return a large sentinel value indicating MST not possible
    return 1 << 30;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

type edge struct {
	u, v, w, idx int
}

type dsu struct {
	parent []int
	rank   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	r := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
	}
	return &dsu{parent: p, rank: r}
}

func (d *dsu) find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.find(d.parent[x])
	}
	return d.parent[x]
}

func (d *dsu) union(a, b int) bool {
	ra := d.find(a)
	rb := d.find(b)
	if ra == rb {
		return false
	}
	if d.rank[ra] < d.rank[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	if d.rank[ra] == d.rank[rb] {
		d.rank[ra]++
	}
	return true
}

// kruskal computes MST weight with optional skip and forced edge.
// Returns total weight and number of edges used.
func kruskal(n int, edges []edge, skipIdx int, forced *edge) (int, int) {
	ds := newDSU(n)
	totalWeight := 0
	used := 0

	if forced != nil {
		if ds.union(forced.u, forced.v) {
			totalWeight += forced.w
			used++
		}
	}

	for _, e := range edges {
		if e.idx == skipIdx {
			continue
		}
		if forced != nil && e.idx == forced.idx {
			continue
		}
		if ds.union(e.u, e.v) {
			totalWeight += e.w
			used++
			if used == n-1 {
				break
			}
		}
	}
	return totalWeight, used
}

func findCriticalAndPseudoCriticalEdges(n int, edgesInput [][]int) [][]int {
	m := len(edgesInput)
	edges := make([]edge, m)
	for i, e := range edgesInput {
		edges[i] = edge{u: e[0], v: e[1], w: e[2], idx: i}
	}

	sort.Slice(edges, func(i, j int) bool {
		if edges[i].w == edges[j].w {
			return edges[i].idx < edges[j].idx
		}
		return edges[i].w < edges[j].w
	})

	origWeight, used := kruskal(n, edges, -1, nil)
	if used != n-1 {
		// graph is guaranteed to be connected per problem statement,
		// but guard against unexpected input.
		return [][]int{{}, {}}
	}

	critical := []int{}
	pseudo := []int{}

	for _, e := range edges {
		// Test critical: skip this edge
		w, cnt := kruskal(n, edges, e.idx, nil)
		if cnt != n-1 || w > origWeight {
			critical = append(critical, e.idx)
			continue
		}
		// Test pseudo-critical: force include this edge
		forced := e
		w2, cnt2 := kruskal(n, edges, -1, &forced)
		if cnt2 == n-1 && w2 == origWeight {
			pseudo = append(pseudo, e.idx)
		}
	}

	return [][]int{critical, pseudo}
}
```

## Ruby

```ruby
class UnionFind
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @rank = Array.new(n, 0)
  end

  def find(x)
    while @parent[x] != x
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(a, b)
    ra = find(a)
    rb = find(b)
    return false if ra == rb
    if @rank[ra] < @rank[rb]
      @parent[ra] = rb
    elsif @rank[ra] > @rank[rb]
      @parent[rb] = ra
    else
      @parent[rb] = ra
      @rank[ra] += 1
    end
    true
  end
end

def find_critical_and_pseudo_critical_edges(n, edges)
  indexed = edges.each_with_index.map { |(u, v, w), i| [u, v, w, i] }
  sorted = indexed.sort_by { |e| e[2] }

  mst_total = lambda do |skip_idx = nil, forced_edge = nil|
    uf = UnionFind.new(n)
    total = 0
    used = 0

    if forced_edge
      u, v, w, _ = forced_edge
      if uf.union(u, v)
        total += w
        used += 1
      end
    end

    sorted.each do |u, v, w, idx|
      next if idx == skip_idx
      next if forced_edge && idx == forced_edge[3]
      if uf.union(u, v)
        total += w
        used += 1
        break if used == n - 1
      end
    end

    used == n - 1 ? total : Float::INFINITY
  end

  original = mst_total.call

  critical = []
  pseudo = []

  indexed.each do |edge|
    idx = edge[3]
    weight_without = mst_total.call(idx, nil)
    if weight_without > original || weight_without == Float::INFINITY
      critical << idx
    else
      weight_with = mst_total.call(nil, edge)
      pseudo << idx if weight_with == original
    end
  end

  [critical, pseudo]
end
```

## Scala

```scala
object Solution {
  def findCriticalAndPseudoCriticalEdges(n: Int, edges: Array[Array[Int]]): List[List[Int]] = {
    case class Edge(u: Int, v: Int, w: Int, idx: Int)

    val edgeList: Array[Edge] = edges.zipWithIndex.map { case (e, i) => Edge(e(0), e(1), e(2), i) }
    val sortedEdges: Array[Edge] = edgeList.sortBy(_.w)
    val edgeMap: Array[Edge] = new Array[Edge](edges.length)
    edgeList.foreach(e => edgeMap(e.idx) = e)

    class DSU(val n: Int) {
      private val parent: Array[Int] = (0 until n).toArray
      private val rank: Array[Int] = Array.fill(n)(0)

      def find(x: Int): Int = {
        if (parent(x) != x) parent(x) = find(parent(x))
        parent(x)
      }

      def union(a: Int, b: Int): Boolean = {
        var x = find(a)
        var y = find(b)
        if (x == y) return false
        if (rank(x) < rank(y)) { val t = x; x = y; y = t }
        parent(y) = x
        if (rank(x) == rank(y)) rank(x) += 1
        true
      }
    }

    def kruskal(skipIdx: Int = -1, forcedIdx: Int = -1): (Int, Int) = {
      val dsu = new DSU(n)
      var totalWeight = 0
      var edgesUsed = 0

      if (forcedIdx != -1) {
        val e = edgeMap(forcedIdx)
        if (dsu.union(e.u, e.v)) {
          totalWeight += e.w
          edgesUsed += 1
        }
      }

      for (e <- sortedEdges) {
        if (e.idx == skipIdx || e.idx == forcedIdx) {
          // skip this edge
        } else if (dsu.union(e.u, e.v)) {
          totalWeight += e.w
          edgesUsed += 1
        }
      }
      (totalWeight, edgesUsed)
    }

    val mstWeight = kruskal()._1

    val critical = scala.collection.mutable.ListBuffer[Int]()
    val pseudo = scala.collection.mutable.ListBuffer[Int]()

    for (e <- edgeList) {
      val (wSkip, cntSkip) = kruskal(skipIdx = e.idx)
      if (cntSkip < n - 1 || wSkip > mstWeight) {
        critical += e.idx
      } else {
        val (wForced, cntForced) = kruskal(forcedIdx = e.idx)
        if (wForced == mstWeight && cntForced == n - 1) {
          pseudo += e.idx
        }
      }
    }

    List(critical.toList, pseudo.toList)
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn find_critical_and_pseudo_critical_edges(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        #[derive(Clone)]
        struct Edge {
            u: usize,
            v: usize,
            w: i32,
            idx: usize,
        }

        struct UnionFind {
            parent: Vec<usize>,
            rank: Vec<i32>,
        }
        impl UnionFind {
            fn new(size: usize) -> Self {
                let mut parent = Vec::with_capacity(size);
                for i in 0..size {
                    parent.push(i);
                }
                UnionFind {
                    parent,
                    rank: vec![0; size],
                }
            }
            fn find(&mut self, x: usize) -> usize {
                if self.parent[x] != x {
                    let root = self.find(self.parent[x]);
                    self.parent[x] = root;
                }
                self.parent[x]
            }
            fn union(&mut self, a: usize, b: usize) -> bool {
                let mut ra = self.find(a);
                let mut rb = self.find(b);
                if ra == rb {
                    return false;
                }
                if self.rank[ra] < self.rank[rb] {
                    std::mem::swap(&mut ra, &mut rb);
                }
                self.parent[rb] = ra;
                if self.rank[ra] == self.rank[rb] {
                    self.rank[ra] += 1;
                }
                true
            }
        }

        fn kruskal(
            n: usize,
            edges: &Vec<Edge>,
            skip: Option<usize>,
            forced: Option<usize>,
        ) -> i32 {
            let mut uf = UnionFind::new(n);
            let mut weight: i32 = 0;
            let mut used: usize = 0;

            if let Some(fi) = forced {
                let e = &edges[fi];
                if uf.union(e.u, e.v) {
                    weight += e.w;
                    used += 1;
                }
            }

            for (i, e) in edges.iter().enumerate() {
                if Some(i) == skip {
                    continue;
                }
                if Some(i) == forced {
                    continue;
                }
                if uf.union(e.u, e.v) {
                    weight += e.w;
                    used += 1;
                    if used == n - 1 {
                        break;
                    }
                }
            }

            if used == n - 1 {
                weight
            } else {
                i32::MAX
            }
        }

        let m = edges.len();
        let mut edge_list: Vec<Edge> = edges
            .iter()
            .enumerate()
            .map(|(i, e)| Edge {
                u: e[0] as usize,
                v: e[1] as usize,
                w: e[2],
                idx: i,
            })
            .collect();

        edge_list.sort_by_key(|e| (e.w, e.idx));

        let mut pos = vec![0usize; m];
        for (i, e) in edge_list.iter().enumerate() {
            pos[e.idx] = i;
        }

        let orig_weight = kruskal(n as usize, &edge_list, None, None);

        let mut critical: Vec<i32> = Vec::new();
        let mut pseudo: Vec<i32> = Vec::new();

        for i in 0..m {
            let p = pos[i];
            let w_skip = kruskal(n as usize, &edge_list, Some(p), None);
            if w_skip > orig_weight {
                critical.push(i as i32);
            } else {
                let w_forced = kruskal(n as usize, &edge_list, None, Some(p));
                if w_forced == orig_weight {
                    pseudo.push(i as i32);
                }
            }
        }

        vec![critical, pseudo]
    }
}
```

## Racket

```racket
(define/contract (find-critical-and-pseudo-critical-edges n edges)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let* ([edge-list
          (for/list ([e edges] [i (in-naturals)])
            (match-define (list u v w) e)
            (struct edge (u v w idx) #:transparent)
            (edge u v w i))]
         [m (length edge-list)]
         [edges-by-index (make-vector m)]
         [_ (for ([e edge-list])
              (vector-set! edges-by-index (edge-idx e) e))]
         [sorted-edges
          (sort edge-list
                (lambda (a b)
                  (if (= (edge-w a) (edge-w b))
                      (< (edge-idx a) (edge-idx b))
                      (< (edge-w a) (edge-w b)))))]
         ;; DSU helpers
         [find
          (lambda (parent x)
            (let loop ((x x))
              (let ((p (vector-ref parent x)))
                (if (= p x)
                    x
                    (let ((root (loop p)))
                      (vector-set! parent x root)
                      root)))))]
         [union
          (lambda (parent rank x y)
            (let* ((rx ((find) parent x))
                   (ry ((find) parent y)))
              (if (= rx ry)
                  #f
                  (begin
                    (cond [(< (vector-ref rank rx) (vector-ref rank ry))
                           (vector-set! parent rx ry)]
                          [(> (vector-ref rank rx) (vector-ref rank ry))
                           (vector-set! parent ry rx)]
                          [else
                           (vector-set! parent ry rx)
                           (vector-set! rank rx (+ (vector-ref rank rx) 1))])
                    #t)))))]
         ;; MST weight calculator
         [mst-weight
          (lambda (include-idx exclude-idx)
            (let ([parent (make-vector n (lambda (i) i))]
                  [rank   (make-vector n 0)]
                  [total 0]
                  [cnt   0])
              (when (not (eq? include-idx #f))
                (let* ((e (vector-ref edges-by-index include-idx))
                       (u (edge-u e)) (v (edge-v e)))
                  (when ((union) parent rank u v)
                    (set! total (+ total (edge-w e)))
                    (set! cnt   (+ cnt 1)))))
              (for ([e sorted-edges])
                (let ((idx (edge-idx e)))
                  (when (and (not (= idx exclude-idx))
                             (or (eq? include-idx #f) (not (= idx include-idx))))
                    (when ((union) parent rank (edge-u e) (edge-v e))
                      (set! total (+ total (edge-w e)))
                      (set! cnt   (+ cnt 1))))))
              (if (= cnt (- n 1)) total #f)))])
    (let* ([orig-weight (mst-weight #f #f)]
           [critical '()]
           [pseudo   '()])
      (for ([i (in-range m)])
        (let ((w-excl (mst-weight #f i)))
          (if (or (not w-excl) (> w-excl orig-weight))
              (set! critical (cons i critical))
              (let ((w-incl (mst-weight i #f)))
                (when (= w-incl orig-weight)
                  (set! pseudo (cons i pseudo)))))))
      (list (reverse critical) (reverse pseudo)))))
```

## Erlang

```erlang
-module(solution).
-export([find_critical_and_pseudo_critical_edges/2]).

-spec find_critical_and_pseudo_critical_edges(N :: integer(), Edges :: [[integer()]]) -> [[integer()]].
find_critical_and_pseudo_critical_edges(N, Edges) ->
    IndexedEdges = index_edges(Edges, 0, []),
    SortedEdges = lists:keysort(1, IndexedEdges),

    {OrigWeight, OrigCount} = mst(N, SortedEdges, -1, -1),

    Len = length(Edges),
    {CriticalRev, PseudoRev} =
        lists:foldl(
          fun(I, {CritAcc, PsAcc}) ->
                  {WSkip, CSkip} = mst(N, SortedEdges, I, -1),
                  case (Cskip < N-1) orelse (WSkip > OrigWeight) of
                      true -> {[I | CritAcc], PsAcc};
                      false ->
                          {WForce, _} = mst(N, SortedEdges, -1, I),
                          if WForce == OrigWeight ->
                                 {CritAcc, [I | PsAcc]};
                             true ->
                                 {CritAcc, PsAcc}
                          end
                  end
          end,
          {[], []},
          lists:seq(0, Len-1)
        ),
    [lists:reverse(CriticalRev), lists:reverse(PseudoRev)].

%% --------------------------------------------------------------------
%% Helpers
%% --------------------------------------------------------------------

index_edges([], _Idx, Acc) -> Acc;
index_edges([[U,V,W] | Rest], Idx, Acc) ->
    index_edges(Rest, Idx + 1, [{W, U, V, Idx} | Acc]).

mst(N, SortedEdges, SkipIdx, ForceIdx) ->
    Parent0 = init_parent(N),
    Rank0   = init_rank(N),

    {Parent1, Rank1, Weight1, Count1} =
        case ForceIdx of
            -1 -> {Parent0, Rank0, 0, 0};
            _  ->
                EdgeF = find_edge_by_index(SortedEdges, ForceIdx),
                {_Wf, Uf, Vf, _} = EdgeF,
                {P, R, true} = union(Parent0, Rank0, Uf, Vf),
                {_Wf, P, R, 1}
        end,

    {FinalParent, FinalRank, TotalWeight, EdgeCnt} =
        lists:foldl(
          fun({W, U, V, Idx}, {Par, Ran, Wt, Cnt}) ->
                  if Idx =:= SkipIdx orelse Idx =:= ForceIdx ->
                          {Par, Ran, Wt, Cnt};
                     true ->
                          {NewPar, NewRan, Merged} = union(Par, Ran, U, V),
                          if Merged ->
                                  {NewPar, NewRan, Wt + W, Cnt + 1};
                             true ->
                                  {Par, Ran, Wt, Cnt}
                          end
                  end
          end,
          {Parent1, Rank1, Weight1, Count1},
          SortedEdges),

    {TotalWeight, EdgeCnt}.

find_edge_by_index([E | Rest], Idx) ->
    case E of
        {_W, _U, _V, Idx} -> E;
        _ -> find_edge_by_index(Rest, Idx)
    end;
find_edge_by_index([], _) -> erlang:error(not_found).

init_parent(N) ->
    list_to_tuple(lists:seq(0, N-1)).

init_rank(N) ->
    list_to_tuple([0 || _ <- lists:seq(1, N)]).

find_root(Parent, X) ->
    Px = element(X + 1, Parent),
    if
        Px =:= X -> {X, Parent};
        true ->
            {Root, Updated} = find_root(Parent, Px),
            NewParent = setelement(X + 1, Updated, Root),
            {Root, NewParent}
    end.

union(Parent, Rank, X, Y) ->
    {RootX, Par1} = find_root(Parent, X),
    {RootY, Par2} = find_root(Par1, Y),
    if
        RootX =:= RootY ->
            {Par2, Rank, false};
        true ->
            RankX = element(RootX + 1, Rank),
            RankY = element(RootY + 1, Rank),
            cond_merge(RankX, RankY, RootX, RootY, Par2, Rank)
    end.

cond_merge(RankX, RankY, Rx, Ry, Parent, Rank) when RankX < RankY ->
    NewParent = setelement(Rx + 1, Parent, Ry),
    {NewParent, Rank, true};
cond_merge(RankX, RankY, Rx, Ry, Parent, Rank) when RankX > RankY ->
    NewParent = setelement(Ry + 1, Parent, Rx),
    {NewParent, Rank, true};
cond_merge(RankX, RankY, Rx, Ry, Parent, Rank) -> % equal
    TempParent = setelement(Ry + 1, Parent, Rx),
    NewRank = setelement(Rx + 1, Rank, RankX + 1),
    {TempParent, NewRank, true}.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_critical_and_pseudo_critical_edges(n :: integer, edges :: [[integer]]) :: [[integer]]
  def find_critical_and_pseudo_critical_edges(n, edges) do
    enriched =
      Enum.with_index(edges)
      |> Enum.map(fn {[u, v, w], idx} -> %{u: u, v: v, w: w, idx: idx} end)

    sorted = Enum.sort_by(enriched, fn e -> {e.w, e.idx} end)

    {orig_weight, _} = mst_weight(n, sorted, nil, nil)

    {critical, pseudo} =
      Enum.reduce(enriched, {[], []}, fn edge, {crit_acc, pseudo_acc} ->
        {skip_w, ok_skip} = mst_weight(n, sorted, edge.idx, nil)

        if (!ok_skip) or (skip_w > orig_weight) do
          {[edge.idx | crit_acc], pseudo_acc}
        else
          {force_w, ok_force} = mst_weight(n, sorted, nil, edge.idx)

          if ok_force and force_w == orig_weight do
            {crit_acc, [edge.idx | pseudo_acc]}
          else
            {crit_acc, pseudo_acc}
          end
        end
      end)

    [Enum.reverse(critical), Enum.reverse(pseudo)]
  end

  defp init_dsu(n) do
    parent = Enum.map(0..(n - 1), fn i -> i end) |> List.to_tuple()
    rank = :erlang.make_tuple(n, 0)
    {parent, rank}
  end

  defp find(parent, x) do
    if elem(parent, x) == x do
      {x, parent}
    else
      {root, updated_parent} = find(parent, elem(parent, x))
      new_parent = put_elem(updated_parent, x, root)
      {root, new_parent}
    end
  end

  defp union(parent, rank, x, y) do
    {rx, parent1} = find(parent, x)
    {ry, parent2} = find(parent1, y)

    if rx == ry do
      {parent2, rank, false}
    else
      rank_rx = elem(rank, rx)
      rank_ry = elem(rank, ry)

      cond do
        rank_rx < rank_ry ->
          new_parent = put_elem(parent2, rx, ry)
          {new_parent, rank, true}

        rank_rx > rank_ry ->
          new_parent = put_elem(parent2, ry, rx)
          {new_parent, rank, true}

        true ->
          new_parent = put_elem(parent2, ry, rx)
          new_rank = put_elem(rank, rx, rank_rx + 1)
          {new_parent, new_rank, true}
      end
    end
  end

  defp mst_weight(n, edges, skip_idx, force_idx) do
    {parent0, rank0} = init_dsu(n)

    {parent1, rank1, total0, cnt0, valid} =
      if force_idx != nil do
        case Enum.find(edges, fn e -> e.idx == force_idx end) do
          nil ->
            {parent0, rank0, 0, 0, true}

          fe ->
            {p, r, merged} = union(parent0, rank0, fe.u, fe.v)

            if merged do
              {p, r, fe.w, 1, true}
            else
              {parent0, rank0, 0, 0, false}
            end
        end
      else
        {parent0, rank0, 0, 0, true}
      end

    if not valid do
      {0, false}
    else
      {_, _, total, cnt} =
        Enum.reduce_while(edges, {parent1, rank1, total0, cnt0}, fn e, acc ->
          {p, r, t, c} = acc

          cond do
            e.idx == skip_idx or e.idx == force_idx ->
              {:cont, {p, r, t, c}}

            true ->
              {new_p, new_r, merged} = union(p, r, e.u, e.v)

              if merged do
                new_t = t + e.w
                new_c = c + 1

                if new_c == n - 1 do
                  {:halt, {new_p, new_r, new_t, new_c}}
                else
                  {:cont, {new_p, new_r, new_t, new_c}}
                end
              else
                {:cont, {p, r, t, c}}
              end
          end
        end)

      if cnt == n - 1 do
        {total, true}
      else
        {total, false}
      end
    end
  end
end
```

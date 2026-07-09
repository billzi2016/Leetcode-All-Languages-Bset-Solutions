# 1697. Checking Existence of Edge Length Limited Paths

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent, size;
        DSU(int n): parent(n), size(n,1) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x]==x) return x;
            return parent[x]=find(parent[x]);
        }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(size[a]<size[b]) swap(a,b);
            parent[b]=a;
            size[a]+=size[b];
        }
    };
    
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        // sort edges by weight
        sort(edgeList.begin(), edgeList.end(),
             [](const vector<int>& a, const vector<int>& b){ return a[2] < b[2]; });
        
        struct Query {int p,q,limit,idx;};
        int m = queries.size();
        vector<Query> qs;
        qs.reserve(m);
        for(int i=0;i<m;++i){
            qs.push_back({queries[i][0], queries[i][1], queries[i][2], i});
        }
        sort(qs.begin(), qs.end(),
             [](const Query& a, const Query& b){ return a.limit < b.limit; });
        
        DSU dsu(n);
        vector<bool> ans(m);
        int eIdx = 0;
        for(const auto& q: qs){
            while(eIdx < (int)edgeList.size() && edgeList[eIdx][2] < q.limit){
                dsu.unite(edgeList[eIdx][0], edgeList[eIdx][1]);
                ++eIdx;
            }
            ans[q.idx] = (dsu.find(q.p) == dsu.find(q.q));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Edge {
        int u, v, w;
        Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
    }

    private static class Query {
        int p, q, limit, idx;
        Query(int p, int q, int limit, int idx) {
            this.p = p;
            this.q = q;
            this.limit = limit;
            this.idx = idx;
        }
    }

    private static class DSU {
        int[] parent;
        int[] size;
        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                parent[ra] = rb;
                size[rb] += size[ra];
            } else {
                parent[rb] = ra;
                size[ra] += size[rb];
            }
        }
    }

    public boolean[] distanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries) {
        Edge[] edges = new Edge[edgeList.length];
        for (int i = 0; i < edgeList.length; i++) {
            edges[i] = new Edge(edgeList[i][0], edgeList[i][1], edgeList[i][2]);
        }
        java.util.Arrays.sort(edges, (a, b) -> Integer.compare(a.w, b.w));

        Query[] qs = new Query[queries.length];
        for (int i = 0; i < queries.length; i++) {
            qs[i] = new Query(queries[i][0], queries[i][1], queries[i][2], i);
        }
        java.util.Arrays.sort(qs, (a, b) -> Integer.compare(a.limit, b.limit));

        boolean[] ans = new boolean[queries.length];
        DSU dsu = new DSU(n);
        int eIdx = 0;
        for (Query q : qs) {
            while (eIdx < edges.length && edges[eIdx].w < q.limit) {
                dsu.union(edges[eIdx].u, edges[eIdx].v);
                eIdx++;
            }
            ans[q.idx] = dsu.find(q.p) == dsu.find(q.q);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Union-Find (Disjoint Set Union)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Sort edges by weight
        edgeList.sort(key=lambda e: e[2])

        # Prepare queries with original indices and sort by limit
        q_with_idx = [(limit, p, q, i) for i, (p, q, limit) in enumerate(queries)]
        q_with_idx.sort(key=lambda x: x[0])

        ans = [False] * len(queries)
        e_ptr = 0
        m = len(edgeList)

        for limit, p, q, idx in q_with_idx:
            # Add all edges with weight < limit
            while e_ptr < m and edgeList[e_ptr][2] < limit:
                u, v, _ = edgeList[e_ptr]
                union(u, v)
                e_ptr += 1
            ans[idx] = find(p) == find(q)

        return ans
```

## Python3

```python
class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        from typing import List

        # Union-Find (Disjoint Set Union)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Sort edges by weight
        edgeList.sort(key=lambda e: e[2])

        # Prepare queries with original indices and sort by limit
        indexed_queries = [(p, q, limit, idx) for idx, (p, q, limit) in enumerate(queries)]
        indexed_queries.sort(key=lambda x: x[2])  # sort by limit

        ans = [False] * len(queries)
        e_idx = 0
        m = len(edgeList)

        for p, q, limit, idx in indexed_queries:
            # Add all edges with weight < limit
            while e_idx < m and edgeList[e_idx][2] < limit:
                u, v, _ = edgeList[e_idx]
                union(u, v)
                e_idx += 1
            ans[idx] = find(p) == find(q)

        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int u;
    int v;
    int w;
} Edge;

typedef struct {
    int p;
    int q;
    int limit;
    int idx;
} Query;

/* Union-Find */
static int find_set(int *parent, int x) {
    if (parent[x] != x) parent[x] = find_set(parent, parent[x]);
    return parent[x];
}

static void union_set(int *parent, int *rank, int a, int b) {
    int ra = find_set(parent, a);
    int rb = find_set(parent, b);
    if (ra == rb) return;
    if (rank[ra] < rank[rb]) {
        parent[ra] = rb;
    } else if (rank[ra] > rank[rb]) {
        parent[rb] = ra;
    } else {
        parent[rb] = ra;
        rank[ra]++;
    }
}

/* Comparators for qsort */
static int cmp_edge(const void *a, const void *b) {
    const Edge *ea = (const Edge *)a;
    const Edge *eb = (const Edge *)b;
    return ea->w - eb->w;
}

static int cmp_query(const void *a, const void *b) {
    const Query *qa = (const Query *)a;
    const Query *qb = (const Query *)b;
    if (qa->limit != qb->limit)
        return qa->limit - qb->limit;
    return qa->idx - qb->idx;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* distanceLimitedPathsExist(int n, int** edgeList, int edgeListSize, int* edgeListColSize,
                                int** queries, int queriesSize, int* queriesColSize,
                                int* returnSize) {
    Edge *edges = (Edge *)malloc(sizeof(Edge) * edgeListSize);
    for (int i = 0; i < edgeListSize; ++i) {
        edges[i].u = edgeList[i][0];
        edges[i].v = edgeList[i][1];
        edges[i].w = edgeList[i][2];
    }
    qsort(edges, edgeListSize, sizeof(Edge), cmp_edge);
    
    Query *qs = (Query *)malloc(sizeof(Query) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        qs[i].p = queries[i][0];
        qs[i].q = queries[i][1];
        qs[i].limit = queries[i][2];
        qs[i].idx = i;
    }
    qsort(qs, queriesSize, sizeof(Query), cmp_query);
    
    int *parent = (int *)malloc(sizeof(int) * n);
    int *rank   = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) {
        parent[i] = i;
        rank[i] = 0;
    }
    
    bool *ans = (bool *)malloc(sizeof(bool) * queriesSize);
    int e = 0;
    for (int i = 0; i < queriesSize; ++i) {
        while (e < edgeListSize && edges[e].w < qs[i].limit) {
            union_set(parent, rank, edges[e].u, edges[e].v);
            ++e;
        }
        ans[qs[i].idx] = (find_set(parent, qs[i].p) == find_set(parent, qs[i].q));
    }
    
    free(edges);
    free(qs);
    free(parent);
    free(rank);
    
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    private class UnionFind
    {
        private int[] parent;
        private int[] rank;

        public UnionFind(int size)
        {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++)
                parent[i] = i;
        }

        public int Find(int x)
        {
            if (parent[x] != x)
                parent[x] = Find(parent[x]);
            return parent[x];
        }

        public void Union(int x, int y)
        {
            int rootX = Find(x);
            int rootY = Find(y);
            if (rootX == rootY) return;

            if (rank[rootX] < rank[rootY])
                parent[rootX] = rootY;
            else if (rank[rootX] > rank[rootY])
                parent[rootY] = rootX;
            else
            {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }

        public bool Connected(int x, int y)
        {
            return Find(x) == Find(y);
        }
    }

    private struct Query
    {
        public int p;
        public int q;
        public int limit;
        public int index;
    }

    public bool[] DistanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries)
    {
        // Sort edges by weight
        Array.Sort(edgeList, (a, b) => a[2].CompareTo(b[2]));

        // Prepare and sort queries by limit while keeping original indices
        Query[] qs = new Query[queries.Length];
        for (int i = 0; i < queries.Length; i++)
        {
            qs[i] = new Query
            {
                p = queries[i][0],
                q = queries[i][1],
                limit = queries[i][2],
                index = i
            };
        }
        Array.Sort(qs, (a, b) => a.limit.CompareTo(b.limit));

        bool[] answer = new bool[queries.Length];
        UnionFind uf = new UnionFind(n);
        int edgeIdx = 0;
        int m = edgeList.Length;

        foreach (var q in qs)
        {
            // Add all edges with weight < current query limit
            while (edgeIdx < m && edgeList[edgeIdx][2] < q.limit)
            {
                uf.Union(edgeList[edgeIdx][0], edgeList[edgeIdx][1]);
                edgeIdx++;
            }

            answer[q.index] = uf.Connected(q.p, q.q);
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edgeList
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var distanceLimitedPathsExist = function(n, edgeList, queries) {
    // Disjoint Set Union (Union-Find)
    class DSU {
        constructor(size) {
            this.parent = new Int32Array(size);
            this.rank = new Int8Array(size);
            for (let i = 0; i < size; ++i) this.parent[i] = i;
        }
        find(x) {
            const p = this.parent;
            while (p[x] !== x) {
                p[x] = p[p[x]];
                x = p[x];
            }
            return x;
        }
        union(a, b) {
            let ra = this.find(a);
            let rb = this.find(b);
            if (ra === rb) return;
            const r = this.rank;
            if (r[ra] < r[rb]) {
                this.parent[ra] = rb;
            } else if (r[ra] > r[rb]) {
                this.parent[rb] = ra;
            } else {
                this.parent[rb] = ra;
                r[ra]++;
            }
        }
    }

    // Sort edges by weight
    edgeList.sort((a, b) => a[2] - b[2]);

    // Attach original indices to queries and sort by limit
    const qWithIdx = queries.map((q, idx) => [q[0], q[1], q[2], idx]);
    qWithIdx.sort((a, b) => a[2] - b[2]);

    const dsu = new DSU(n);
    const ans = new Array(queries.length);
    let ePos = 0;

    for (const [p, q, limit, origIdx] of qWithIdx) {
        while (ePos < edgeList.length && edgeList[ePos][2] < limit) {
            dsu.union(edgeList[ePos][0], edgeList[ePos][1]);
            ePos++;
        }
        ans[origIdx] = dsu.find(p) === dsu.find(q);
    }

    return ans;
};
```

## Typescript

```typescript
function distanceLimitedPathsExist(n: number, edgeList: number[][], queries: number[][]): boolean[] {
    // Union-Find (Disjoint Set Union) implementation
    class UnionFind {
        parent: number[];
        size: number[];
        constructor(size: number) {
            this.parent = new Array(size);
            this.size = new Array(size);
            for (let i = 0; i < size; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
        }
        find(x: number): number {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }
        union(a: number, b: number): void {
            let ra = this.find(a);
            let rb = this.find(b);
            if (ra === rb) return;
            // Union by size
            if (this.size[ra] < this.size[rb]) {
                [ra, rb] = [rb, ra];
            }
            this.parent[rb] = ra;
            this.size[ra] += this.size[rb];
        }
    }

    // Sort edges by weight ascending
    edgeList.sort((a, b) => a[2] - b[2]);

    // Attach original indices to queries and sort by limit ascending
    const qWithIdx: [number, number, number, number][] = queries.map((q, idx) => [q[0], q[1], q[2], idx]);
    qWithIdx.sort((a, b) => a[2] - b[2]);

    const uf = new UnionFind(n);
    const ans: boolean[] = new Array(queries.length);
    let e = 0; // pointer for edges

    for (const [p, q, limit, idx] of qWithIdx) {
        while (e < edgeList.length && edgeList[e][2] < limit) {
            uf.union(edgeList[e][0], edgeList[e][1]);
            e++;
        }
        ans[idx] = uf.find(p) === uf.find(q);
    }

    return ans;
}
```

## Php

```php
class DSU {
    public array $parent;
    public array $rank;

    public function __construct(int $n) {
        $this->parent = [];
        $this->rank = [];
        for ($i = 0; $i < $n; $i++) {
            $this->parent[$i] = $i;
            $this->rank[$i] = 0;
        }
    }

    public function find(int $x): int {
        while ($this->parent[$x] !== $x) {
            // Path compression (halving)
            $this->parent[$x] = $this->parent[$this->parent[$x]];
            $x = $this->parent[$x];
        }
        return $x;
    }

    public function union(int $a, int $b): void {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) {
            return;
        }
        if ($this->rank[$pa] < $this->rank[$pb]) {
            $this->parent[$pa] = $pb;
        } elseif ($this->rank[$pa] > $this->rank[$pb]) {
            $this->parent[$pb] = $pa;
        } else {
            $this->parent[$pb] = $pa;
            $this->rank[$pa]++;
        }
    }
}

class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edgeList
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function distanceLimitedPathsExist($n, $edgeList, $queries) {
        // Sort edges by weight
        usort($edgeList, function($a, $b) {
            return $a[2] <=> $b[2];
        });

        // Prepare queries with original indices and sort by limit
        $qArr = [];
        foreach ($queries as $idx => $qr) {
            // [limit, p, q, originalIndex]
            $qArr[] = [$qr[2], $qr[0], $qr[1], $idx];
        }
        usort($qArr, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $dsu = new DSU($n);
        $edgeIdx = 0;
        $m = count($edgeList);
        $answer = array_fill(0, count($queries), false);

        foreach ($qArr as $item) {
            [$limit, $p, $qv, $origIdx] = $item;

            while ($edgeIdx < $m && $edgeList[$edgeIdx][2] < $limit) {
                $dsu->union($edgeList[$edgeIdx][0], $edgeList[$edgeIdx][1]);
                $edgeIdx++;
            }

            $answer[$origIdx] = ($dsu->find($p) === $dsu->find($qv));
        }

        return $answer;
    }
}
```

## Swift

```swift
class DSU {
    private var parent: [Int]
    private var rank: [Int]

    init(_ n: Int) {
        parent = Array(0..<n)
        rank = Array(repeating: 0, count: n)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ x: Int, _ y: Int) {
        var xr = find(x)
        var yr = find(y)
        if xr == yr { return }
        if rank[xr] < rank[yr] {
            parent[xr] = yr
        } else if rank[xr] > rank[yr] {
            parent[yr] = xr
        } else {
            parent[yr] = xr
            rank[xr] += 1
        }
    }
}

class Solution {
    func distanceLimitedPathsExist(_ n: Int, _ edgeList: [[Int]], _ queries: [[Int]]) -> [Bool] {
        var edges = edgeList.map { (u: $0[0], v: $0[1], w: $0[2]) }
        edges.sort { $0.w < $1.w }

        var sortedQueries = [(p: Int, q: Int, limit: Int, idx: Int)]()
        for (i, q) in queries.enumerated() {
            sortedQueries.append((p: q[0], q: q[1], limit: q[2], idx: i))
        }
        sortedQueries.sort { $0.limit < $1.limit }

        var dsu = DSU(n)
        var answer = Array(repeating: false, count: queries.count)

        var eIdx = 0
        for query in sortedQueries {
            while eIdx < edges.count && edges[eIdx].w < query.limit {
                dsu.union(edges[eIdx].u, edges[eIdx].v)
                eIdx += 1
            }
            answer[query.idx] = dsu.find(query.p) == dsu.find(query.q)
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distanceLimitedPathsExist(n: Int, edgeList: Array<IntArray>, queries: Array<IntArray>): BooleanArray {
        data class Query(val p: Int, val q: Int, val limit: Int, val idx: Int)

        // Sort edges by weight
        val sortedEdges = edgeList.sortedBy { it[2] }

        // Prepare and sort queries by limit
        val queryObjs = Array(queries.size) { i ->
            Query(queries[i][0], queries[i][1], queries[i][2], i)
        }.sortedBy { it.limit }

        // Union-Find structure
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

            fun union(a: Int, b: Int) {
                var rootA = find(a)
                var rootB = find(b)
                if (rootA == rootB) return
                if (rank[rootA] < rank[rootB]) {
                    parent[rootA] = rootB
                } else if (rank[rootA] > rank[rootB]) {
                    parent[rootB] = rootA
                } else {
                    parent[rootB] = rootA
                    rank[rootA]++
                }
            }
        }

        val uf = UnionFind(n)
        val answer = BooleanArray(queries.size)

        var eIdx = 0
        for (q in queryObjs) {
            while (eIdx < sortedEdges.size && sortedEdges[eIdx][2] < q.limit) {
                uf.union(sortedEdges[eIdx][0], sortedEdges[eIdx][1])
                eIdx++
            }
            answer[q.idx] = uf.find(q.p) == uf.find(q.q)
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<bool> distanceLimitedPathsExist(
      int n, List<List<int>> edgeList, List<List<int>> queries) {
    // Sort edges by weight
    edgeList.sort((a, b) => a[2].compareTo(b[2]));

    // Prepare queries with original indices and sort by limit
    int m = queries.length;
    List<List<int>> qWithIdx = List.generate(m, (i) {
      var q = queries[i];
      return [q[2], q[0], q[1], i]; // [limit, p, q, originalIndex]
    });
    qWithIdx.sort((a, b) => a[0].compareTo(b[0]));

    // DSU initialization
    List<int> parent = List.generate(n, (i) => i);
    List<int> rank = List.filled(n, 0);

    int find(int x) {
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    }

    void union(int a, int b) {
      int pa = find(a);
      int pb = find(b);
      if (pa == pb) return;
      if (rank[pa] < rank[pb]) {
        parent[pa] = pb;
      } else if (rank[pa] > rank[pb]) {
        parent[pb] = pa;
      } else {
        parent[pb] = pa;
        rank[pa]++;
      }
    }

    List<bool> answer = List.filled(m, false);
    int eIdx = 0;
    for (var q in qWithIdx) {
      int limit = q[0];
      int p = q[1];
      int r = q[2];
      int idx = q[3];

      while (eIdx < edgeList.length && edgeList[eIdx][2] < limit) {
        union(edgeList[eIdx][0], edgeList[eIdx][1]);
        eIdx++;
      }

      answer[idx] = find(p) == find(r);
    }

    return answer;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

type dsu struct {
	parent []int
	size   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	s := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
		s[i] = 1
	}
	return &dsu{parent: p, size: s}
}

func (d *dsu) find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.find(d.parent[x])
	}
	return d.parent[x]
}

func (d *dsu) union(a, b int) {
	ra := d.find(a)
	rb := d.find(b)
	if ra == rb {
		return
	}
	if d.size[ra] < d.size[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	d.size[ra] += d.size[rb]
}

type query struct {
	p, q   int
	limit  int
	idx    int
}

func distanceLimitedPathsExist(n int, edgeList [][]int, queries [][]int) []bool {
	// sort edges by weight
	sort.Slice(edgeList, func(i, j int) bool {
		return edgeList[i][2] < edgeList[j][2]
	})

	qs := make([]query, len(queries))
	for i, q := range queries {
		qs[i] = query{p: q[0], q: q[1], limit: q[2], idx: i}
	}
	sort.Slice(qs, func(i, j int) bool {
		return qs[i].limit < qs[j].limit
	})

	ans := make([]bool, len(queries))
	ds := newDSU(n)
	ei := 0
	for _, qu := range qs {
		for ei < len(edgeList) && edgeList[ei][2] < qu.limit {
			ds.union(edgeList[ei][0], edgeList[ei][1])
			ei++
		}
		if ds.find(qu.p) == ds.find(qu.q) {
			ans[qu.idx] = true
		}
	}
	return ans
}
```

## Ruby

```ruby
def distance_limited_paths_exist(n, edge_list, queries)
  edges = edge_list.sort_by { |e| e[2] }
  q_with_idx = queries.each_with_index.map { |q, i| [q[2], q[0], q[1], i] }.sort_by { |a| a[0] }

  parent = Array.new(n) { |i| i }
  size   = Array.new(n, 1)

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if size[ra] < size[rb]
      ra, rb = rb, ra
    end
    parent[rb] = ra
    size[ra] += size[rb]
  end

  ans = Array.new(queries.length)
  e_idx = 0
  edges_len = edges.length

  q_with_idx.each do |limit, p, q, idx|
    while e_idx < edges_len && edges[e_idx][2] < limit
      union.call(edges[e_idx][0], edges[e_idx][1])
      e_idx += 1
    end
    ans[idx] = (find.call(p) == find.call(q))
  end

  ans
end
```

## Scala

```scala
object Solution {
  def distanceLimitedPathsExist(n: Int, edgeList: Array[Array[Int]], queries: Array[Array[Int]]): Array[Boolean] = {
    // Sort edges by weight
    val edges = edgeList.sortBy(_(2))

    // Attach original index to each query and sort by limit
    val indexedQueries = queries.zipWithIndex.map { case (q, idx) =>
      (q(0), q(1), q(2), idx)
    }.sortBy(_._3)

    val dsu = new DSU(n)
    val answer = new Array[Boolean](queries.length)

    var ePos = 0
    for ((p, q, limit, idx) <- indexedQueries) {
      while (ePos < edges.length && edges(ePos)(2) < limit) {
        dsu.union(edges(ePos)(0), edges(ePos)(1))
        ePos += 1
      }
      answer(idx) = dsu.find(p) == dsu.find(q)
    }

    answer
  }

  private class DSU(n: Int) {
    private val parent: Array[Int] = (0 until n).toArray
    private val rank: Array[Int] = new Array[Int](n)

    def find(x: Int): Int = {
      var v = x
      while (parent(v) != v) {
        parent(v) = parent(parent(v))
        v = parent(v)
      }
      v
    }

    def union(a: Int, b: Int): Unit = {
      var pa = find(a)
      var pb = find(b)
      if (pa == pb) return
      if (rank(pa) < rank(pb)) {
        val tmp = pa; pa = pb; pb = tmp
      }
      parent(pb) = pa
      if (rank(pa) == rank(pb)) rank(pa) += 1
    }
  }
}
```

## Rust

```rust
struct DSU {
    parent: Vec<usize>,
    rank: Vec<u8>,
}

impl DSU {
    fn new(size: usize) -> Self {
        let mut parent = Vec::with_capacity(size);
        for i in 0..size {
            parent.push(i);
        }
        let rank = vec![0; size];
        DSU { parent, rank }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }

    fn union(&mut self, a: usize, b: usize) {
        let mut ra = self.find(a);
        let mut rb = self.find(b);
        if ra == rb {
            return;
        }
        if self.rank[ra] < self.rank[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        if self.rank[ra] == self.rank[rb] {
            self.rank[ra] += 1;
        }
    }

    fn connected(&mut self, a: usize, b: usize) -> bool {
        self.find(a) == self.find(b)
    }
}

impl Solution {
    pub fn distance_limited_paths_exist(
        n: i32,
        edge_list: Vec<Vec<i32>>,
        queries: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        let mut edges: Vec<(i32, usize, usize)> = edge_list
            .into_iter()
            .map(|e| (e[2], e[0] as usize, e[1] as usize))
            .collect();
        edges.sort_by_key(|k| k.0);

        let mut queries_with_idx: Vec<(i32, usize, usize, usize)> = queries
            .into_iter()
            .enumerate()
            .map(|(idx, q)| (q[2], q[0] as usize, q[1] as usize, idx))
            .collect();
        queries_with_idx.sort_by_key(|k| k.0);

        let mut ans = vec![false; queries_with_idx.len()];
        let mut dsu = DSU::new(n as usize);
        let mut e_ptr = 0usize;

        for (limit, p, q, idx) in queries_with_idx {
            while e_ptr < edges.len() && edges[e_ptr].0 < limit {
                let (_, u, v) = edges[e_ptr];
                dsu.union(u, v);
                e_ptr += 1;
            }
            ans[idx] = dsu.connected(p, q);
        }

        ans
    }
}
```

## Racket

```racket
(define (make-dsu n)
  (let ((parent (make-vector n))
        (rank   (make-vector n 0)))
    (for ([i (in-range n)])
      (vector-set! parent i i))
    (list parent rank)))

(define (find dsu x)
  (let* ((parent (first dsu))
         (px (vector-ref parent x)))
    (if (= px x)
        x
        (let ((root (find dsu px)))
          (vector-set! parent x root)
          root))))

(define (union dsu a b)
  (let* ((parent (first dsu))
         (rank   (second dsu))
         (ra (find dsu a))
         (rb (find dsu b)))
    (when (not (= ra rb))
      (if (< (vector-ref rank ra) (vector-ref rank rb))
          (vector-set! parent ra rb)
          (begin
            (vector-set! parent rb ra)
            (when (= (vector-ref rank ra) (vector-ref rank rb))
              (vector-set! rank ra (+ 1 (vector-ref rank ra)))))))))

(define/contract (distance-limited-paths-exist n edgeList queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof boolean?))
  (let* ((sorted-edges (sort edgeList
                             (lambda (e1 e2) (< (list-ref e1 2) (list-ref e2 2)))))
         (queries-with-index
          (map (lambda (q idx) (list (list-ref q 0)
                                    (list-ref q 1)
                                    (list-ref q 2)
                                    idx))
               queries
               (in-naturals)))
         (sorted-queries (sort queries-with-index
                               (lambda (a b) (< (list-ref a 2) (list-ref b 2)))))
         (dsu (make-dsu n))
         (answers (make-vector (length queries) #f))
         (e-count (length sorted-edges)))
    (let loop ((q-list sorted-queries)
               (edge-pos 0))
      (if (null? q-list)
          (vector->list answers)
          (let* ((q (car q-list))
                 (p (list-ref q 0))
                 (r (list-ref q 1))
                 (limit (list-ref q 2))
                 (idx (list-ref q 3)))
            (let inner ((pos edge-pos))
              (if (and (< pos e-count)
                       (< (list-ref (list-ref sorted-edges pos) 2) limit))
                  (begin
                    (let* ((e (list-ref sorted-edges pos))
                           (u (list-ref e 0))
                           (v (list-ref e 1)))
                      (union dsu u v))
                    (inner (+ pos 1)))
                  (begin
                    (vector-set! answers idx (= (find dsu p) (find dsu r)))
                    (loop (cdr q-list) pos)))))))))
```

## Erlang

```erlang
-spec distance_limited_paths_exist(N :: integer(), EdgeList :: [[integer()]], Queries :: [[integer()]]) -> [boolean()].
distance_limited_paths_exist(N, EdgeList, Queries) ->
    EdgesSorted = lists:sort(fun(A, B) -> element(3, A) < element(3, B) end, EdgeList),
    QIdx = enumerate_queries(Queries, 0, []),
    QueriesSorted = lists:sort(fun(A, B) -> element(1, A) < element(1, B) end, QIdx),

    Parent0 = array:new(N),
    Parent = init_parent(0, N - 1, Parent0),
    Rank0 = array:new(N),
    Rank = init_rank(0, N - 1, Rank0),

    process_queries(QueriesSorted, EdgesSorted, Parent, Rank, []).

enumerate_queries([], _Idx, Acc) ->
    lists:reverse(Acc);
enumerate_queries([{P, Q, Limit} | Rest], Idx, Acc) ->
    enumerate_queries(Rest, Idx + 1, [{Limit, P, Q, Idx} | Acc]).

init_parent(Cur, Max, Arr) when Cur > Max ->
    Arr;
init_parent(Cur, Max, Arr) ->
    NewArr = array:set(Cur + 1, Cur, Arr),
    init_parent(Cur + 1, Max, NewArr).

init_rank(Cur, Max, Arr) when Cur > Max ->
    Arr;
init_rank(Cur, Max, Arr) ->
    NewArr = array:set(Cur + 1, 0, Arr),
    init_rank(Cur + 1, Max, NewArr).

find(Node, Parent) ->
    Index = Node + 1,
    case array:get(Index, Parent) of
        Node -> {Node, Parent};
        PNode ->
            {Root, UpdatedParent} = find(PNode, Parent),
            NewParent = array:set(Index, Root, UpdatedParent),
            {Root, NewParent}
    end.

union(U, V, Parent, Rank) ->
    {RootU, P1} = find(U, Parent),
    {RootV, P2} = find(V, P1),
    if
        RootU == RootV -> {P2, Rank};
        true ->
            RUIdx = RootU + 1,
            RVIdx = RootV + 1,
            RankU = array:get(RUIdx, Rank),
            RankV = array:get(RVIdx, Rank),
            case RankU < RankV of
                true ->
                    NewParent = array:set(RUIdx, RootV, P2),
                    {NewParent, Rank};
                false ->
                    case RankU > RankV of
                        true ->
                            NewParent = array:set(RVIdx, RootU, P2),
                            {NewParent, Rank};
                        false -> % equal ranks
                            TempParent = array:set(RVIdx, RootU, P2),
                            NewRank = array:set(RUIdx, RankU + 1, Rank),
                            {TempParent, NewRank}
                    end
            end
    end.

consume_edges(_Limit, [], Parent, Rank) ->
    {Parent, Rank, []};
consume_edges(Limit, [Edge | Rest] = Edges, Parent, Rank) ->
    Weight = element(3, Edge),
    if
        Weight < Limit ->
            U = element(1, Edge),
            V = element(2, Edge),
            {P2, R2} = union(U, V, Parent, Rank),
            consume_edges(Limit, Rest, P2, R2);
        true ->
            {Parent, Rank, Edges}
    end.

process_queries([], _EdgesRem, _Parent, _Rank, Answers) ->
    Sorted = lists:keysort(1, Answers),
    [Bool || {_Idx, Bool} <- Sorted];
process_queries([{Limit, P, Q, Idx} | Rest], EdgesRem, Parent, Rank, Answers) ->
    {P2, R2, EdgesAfter} = consume_edges(Limit, EdgesRem, Parent, Rank),
    {RootP, P3} = find(P, P2),
    {RootQ, P4} = find(Q, P3),
    Connected = (RootP == RootQ),
    process_queries(Rest, EdgesAfter, P4, R2, [{Idx, Connected} | Answers]).
```

## Elixir

```elixir
defmodule Solution do
  @spec distance_limited_paths_exist(integer, [[integer]], [[integer]]) :: [boolean]
  def distance_limited_paths_exist(n, edge_list, queries) do
    edges =
      edge_list
      |> Enum.map(fn [u, v, w] -> {u, v, w} end)
      |> Enum.sort_by(fn {_u, _v, w} -> w end)

    queries_with_idx =
      queries
      |> Enum.with_index()
      |> Enum.map(fn {[p, q, limit], idx} -> {limit, p, q, idx} end)
      |> Enum.sort_by(fn {limit, _, _, _} -> limit end)

    parent = :array.from_list(Enum.to_list(0..n - 1))
    size = :array.from_list(Enum.map(0..n - 1, fn _ -> 1 end))

    answers_map = process_queries(queries_with_idx, edges, parent, size, %{})

    Enum.map(0..(length(queries) - 1), fn i -> Map.get(answers_map, i) end)
  end

  defp process_queries([], _edges, _parent, _size, answers), do: answers

  defp process_queries([{limit, p, q, idx} | rest], edges, parent, size, answers) do
    {parent2, size2, remaining_edges} = add_edges_until(limit, edges, parent, size)
    same = root(parent2, p) == root(parent2, q)
    answers2 = Map.put(answers, idx, same)
    process_queries(rest, remaining_edges, parent2, size2, answers2)
  end

  defp add_edges_until(_limit, [], parent, size), do: {parent, size, []}

  defp add_edges_until(limit, [{u, v, w} | rest] = edges, parent, size) when w < limit do
    {parent2, size2} = union(parent, size, u, v)
    add_edges_until(limit, rest, parent2, size2)
  end

  defp add_edges_until(_limit, edges, parent, size), do: {parent, size, edges}

  defp union(parent, size, u, v) do
    ru = root(parent, u)
    rv = root(parent, v)

    if ru == rv do
      {parent, size}
    else
      su = :array.get(ru, size)
      sv = :array.get(rv, size)

      if su < sv do
        # attach ru under rv
        parent2 = :array.set(ru, rv, parent)
        size2 = :array.set(rv, su + sv, size)
        {parent2, size2}
      else
        # attach rv under ru
        parent2 = :array.set(rv, ru, parent)
        size2 = :array.set(ru, su + sv, size)
        {parent2, size2}
      end
    end
  end

  defp root(parent, x) do
    p = :array.get(x, parent)

    if p == x do
      x
    else
      root(parent, p)
    end
  end
end
```

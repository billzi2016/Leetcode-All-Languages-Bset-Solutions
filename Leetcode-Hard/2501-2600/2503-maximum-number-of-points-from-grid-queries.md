# 2503. Maximum Number of Points From Grid Queries

## Cpp

```cpp
class Solution {
public:
    struct UnionFind {
        vector<int> parent;
        vector<int> sz;
        UnionFind(int n) : parent(n), sz(n, 1) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }
        void unite(int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return;
            if (sz[ra] < sz[rb]) swap(ra, rb);
            parent[rb] = ra;
            sz[ra] += sz[rb];
        }
        int size(int x) {
            return sz[find(x)];
        }
    };
    
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        int m = grid.size(), n = grid[0].size();
        int total = m * n;
        struct Cell {int val; int idx;};
        vector<Cell> cells;
        cells.reserve(total);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cells.push_back({grid[i][j], i * n + j});
            }
        }
        sort(cells.begin(), cells.end(), [](const Cell& a, const Cell& b){ return a.val < b.val; });
        
        struct Q {int val; int id;};
        vector<Q> qs;
        qs.reserve(queries.size());
        for (int i = 0; i < (int)queries.size(); ++i) qs.push_back({queries[i], i});
        sort(qs.begin(), qs.end(), [](const Q& a, const Q& b){ return a.val < b.val; });
        
        vector<int> ans(queries.size());
        UnionFind uf(total);
        vector<char> active(total, 0);
        int ptr = 0;
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        for (const auto& q : qs) {
            while (ptr < total && cells[ptr].val < q.val) {
                int idx = cells[ptr].idx;
                active[idx] = 1;
                int x = idx / n;
                int y = idx % n;
                for (auto &d : dirs) {
                    int nx = x + d[0], ny = y + d[1];
                    if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                    int nidx = nx * n + ny;
                    if (active[nidx]) uf.unite(idx, nidx);
                }
                ++ptr;
            }
            if (active[0])
                ans[q.id] = uf.size(0);
            else
                ans[q.id] = 0;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
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
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
        int getSize(int x) {
            return size[find(x)];
        }
    }

    private static class Cell {
        int val;
        int idx;
        Cell(int v, int i) { val = v; idx = i; }
    }

    private static class Query {
        int val;
        int idx;
        Query(int v, int i) { val = v; idx = i; }
    }

    public int[] maxPoints(int[][] grid, int[] queries) {
        int m = grid.length;
        int n = grid[0].length;
        int total = m * n;

        Cell[] cells = new Cell[total];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int id = r * n + c;
                cells[id] = new Cell(grid[r][c], id);
            }
        }
        java.util.Arrays.sort(cells, (a, b) -> Integer.compare(a.val, b.val));

        Query[] qs = new Query[queries.length];
        for (int i = 0; i < queries.length; i++) {
            qs[i] = new Query(queries[i], i);
        }
        java.util.Arrays.sort(qs, (a, b) -> Integer.compare(a.val, b.val));

        DSU dsu = new DSU(total);
        boolean[] active = new boolean[total];
        int[] ans = new int[queries.length];

        int ptr = 0;
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        for (Query q : qs) {
            while (ptr < total && cells[ptr].val < q.val) {
                int idx = cells[ptr].idx;
                active[idx] = true;
                int r = idx / n;
                int c = idx % n;
                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        int nid = nr * n + nc;
                        if (active[nid]) {
                            dsu.union(idx, nid);
                        }
                    }
                }
                ptr++;
            }
            if (active[0]) {
                ans[q.idx] = dsu.getSize(0);
            } else {
                ans[q.idx] = 0;
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        rows = len(grid)
        cols = len(grid[0])
        total = rows * cols

        # Flatten cells with their values
        cells = []
        for i in range(rows):
            for j in range(cols):
                cells.append((grid[i][j], i, j))
        cells.sort(key=lambda x: x[0])

        # Sort queries while keeping original indices
        q_with_idx = [(val, idx) for idx, val in enumerate(queries)]
        q_with_idx.sort(key=lambda x: x[0])

        parent = list(range(total))
        size = [1] * total
        visited = [False] * total

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = [0] * len(queries)
        cell_ptr = 0

        for q_val, q_idx in q_with_idx:
            while cell_ptr < total and cells[cell_ptr][0] < q_val:
                _, r, c = cells[cell_ptr]
                idx = r * cols + c
                visited[idx] = True
                # union with already visited neighbors
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        nidx = nr * cols + nc
                        if visited[nidx]:
                            union(idx, nidx)
                cell_ptr += 1

            start_idx = 0  # (0,0) position
            if visited[start_idx]:
                ans[q_idx] = size[find(start_idx)]
            else:
                ans[q_idx] = 0

        return ans
```

## Python3

```python
class Solution:
    def maxPoints(self, grid, queries):
        m, n = len(grid), len(grid[0])
        total = m * n

        # Flatten cells with (value, index)
        cells = []
        for i in range(m):
            row = grid[i]
            base = i * n
            for j in range(n):
                cells.append((row[j], base + j))
        cells.sort(key=lambda x: x[0])

        # Prepare queries with original indices
        qlist = [(val, idx) for idx, val in enumerate(queries)]
        qlist.sort(key=lambda x: x[0])

        parent = list(range(total))
        size = [1] * total
        active = [False] * total

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

        # Directions for neighbors
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ans = [0] * len(queries)
        ptr = 0  # pointer in cells

        for qval, qidx in qlist:
            while ptr < total and cells[ptr][0] < qval:
                val, idx = cells[ptr]
                active[idx] = True
                x, y = divmod(idx, n)
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        nidx = nx * n + ny
                        if active[nidx]:
                            union(idx, nidx)
                ptr += 1
            # answer for this query
            if active[0]:
                ans[qidx] = size[find(0)]
            else:
                ans[qidx] = 0

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int idx;
} Cell;

typedef struct {
    int val;
    int idx;
} Query;

static int cmpCell(const void *a, const void *b) {
    int av = ((Cell *)a)->val;
    int bv = ((Cell *)b)->val;
    return av - bv;
}

static int cmpQuery(const void *a, const void *b) {
    int av = ((Query *)a)->val;
    int bv = ((Query *)b)->val;
    return av - bv;
}

static int findRoot(int x, int *parent) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxPoints(int** grid, int gridSize, int* gridColSize, int* queries, int queriesSize, int* returnSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int total = m * n;

    Cell *cells = (Cell *)malloc(total * sizeof(Cell));
    int pos = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cells[pos].val = grid[i][j];
            cells[pos].idx = pos;
            ++pos;
        }
    }
    qsort(cells, total, sizeof(Cell), cmpCell);

    Query *qs = (Query *)malloc(queriesSize * sizeof(Query));
    for (int i = 0; i < queriesSize; ++i) {
        qs[i].val = queries[i];
        qs[i].idx = i;
    }
    qsort(qs, queriesSize, sizeof(Query), cmpQuery);

    int *parent = (int *)malloc(total * sizeof(int));
    int *sz = (int *)malloc(total * sizeof(int));
    char *active = (char *)calloc(total, sizeof(char));

    for (int i = 0; i < total; ++i) {
        parent[i] = i;
        sz[i] = 1;
    }

    int *ans = (int *)malloc(queriesSize * sizeof(int));
    int cellPos = 0;
    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    int startIdx = 0; // top-left cell index

    for (int q = 0; q < queriesSize; ++q) {
        int limit = qs[q].val;
        while (cellPos < total && cells[cellPos].val < limit) {
            int curIdx = cells[cellPos].idx;
            active[curIdx] = 1;

            int r = curIdx / n;
            int c = curIdx % n;
            for (int d = 0; d < 4; ++d) {
                int nr = r + dirs[d][0];
                int nc = c + dirs[d][1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int nbIdx = nr * n + nc;
                    if (active[nbIdx]) {
                        int ra = findRoot(curIdx, parent);
                        int rb = findRoot(nbIdx, parent);
                        if (ra != rb) {
                            if (sz[ra] < sz[rb]) {
                                parent[ra] = rb;
                                sz[rb] += sz[ra];
                            } else {
                                parent[rb] = ra;
                                sz[ra] += sz[rb];
                            }
                        }
                    }
                }
            }
            ++cellPos;
        }

        if (active[startIdx]) {
            int root = findRoot(startIdx, parent);
            ans[qs[q].idx] = sz[root];
        } else {
            ans[qs[q].idx] = 0;
        }
    }

    *returnSize = queriesSize;

    free(cells);
    free(qs);
    free(parent);
    free(sz);
    free(active);

    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    private struct Cell
    {
        public int val;
        public int idx;
    }

    private struct Query
    {
        public int val;
        public int idx;
    }

    private class UnionFind
    {
        private readonly int[] parent;
        private readonly int[] size;

        public UnionFind(int n)
        {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++)
            {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int Find(int x)
        {
            if (parent[x] != x)
                parent[x] = Find(parent[x]);
            return parent[x];
        }

        public void Union(int a, int b)
        {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb])
            {
                parent[ra] = rb;
                size[rb] += size[ra];
            }
            else
            {
                parent[rb] = ra;
                size[ra] += size[rb];
            }
        }

        public int GetSize(int x)
        {
            return size[Find(x)];
        }
    }

    public int[] MaxPoints(int[][] grid, int[] queries)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int total = m * n;

        Cell[] cells = new Cell[total];
        int p = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cells[p++] = new Cell { val = grid[i][j], idx = i * n + j };
            }
        }

        Array.Sort(cells, (a, b) => a.val.CompareTo(b.val));

        Query[] qs = new Query[queries.Length];
        for (int i = 0; i < queries.Length; i++)
        {
            qs[i] = new Query { val = queries[i], idx = i };
        }
        Array.Sort(qs, (a, b) => a.val.CompareTo(b.val));

        bool[] active = new bool[total];
        UnionFind uf = new UnionFind(total);
        int[] answer = new int[queries.Length];

        int cellPtr = 0;
        foreach (var q in qs)
        {
            while (cellPtr < total && cells[cellPtr].val < q.val)
            {
                int id = cells[cellPtr].idx;
                active[id] = true;

                int r = id / n;
                int c = id % n;

                // up
                if (r > 0)
                {
                    int nb = id - n;
                    if (active[nb]) uf.Union(id, nb);
                }
                // down
                if (r + 1 < m)
                {
                    int nb = id + n;
                    if (active[nb]) uf.Union(id, nb);
                }
                // left
                if (c > 0)
                {
                    int nb = id - 1;
                    if (active[nb]) uf.Union(id, nb);
                }
                // right
                if (c + 1 < n)
                {
                    int nb = id + 1;
                    if (active[nb]) uf.Union(id, nb);
                }

                cellPtr++;
            }

            answer[q.idx] = active[0] ? uf.GetSize(0) : 0;
        }

        return answer;
    }
}
```

## Javascript

```javascript
class UnionFind {
    constructor(n) {
        this.parent = new Int32Array(n);
        this.size = new Int32Array(n);
        for (let i = 0; i < n; i++) {
            this.parent[i] = i;
            this.size[i] = 1;
        }
    }
    find(x) {
        while (this.parent[x] !== x) {
            this.parent[x] = this.parent[this.parent[x]];
            x = this.parent[x];
        }
        return x;
    }
    union(a, b) {
        let ra = this.find(a);
        let rb = this.find(b);
        if (ra === rb) return;
        if (this.size[ra] < this.size[rb]) {
            const tmp = ra;
            ra = rb;
            rb = tmp;
        }
        this.parent[rb] = ra;
        this.size[ra] += this.size[rb];
    }
    getSize(x) {
        return this.size[this.find(x)];
    }
}

/**
 * @param {number[][]} grid
 * @param {number[]} queries
 * @return {number[]}
 */
var maxPoints = function(grid, queries) {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;

    // flatten cells with their values and indices
    const cells = new Array(total);
    let pos = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            cells[pos] = { val: grid[i][j], idx: pos };
            pos++;
        }
    }
    cells.sort((a, b) => a.val - b.val);

    // queries with original indices
    const qArr = queries.map((v, i) => ({ val: v, idx: i }));
    qArr.sort((a, b) => a.val - b.val);

    const uf = new UnionFind(total);
    const visited = new Uint8Array(total); // 0 = not added, 1 = added
    let cellPtr = 0;
    const ans = new Array(queries.length);

    for (const q of qArr) {
        while (cellPtr < total && cells[cellPtr].val < q.val) {
            const curIdx = cells[cellPtr].idx;
            visited[curIdx] = 1;

            const r = Math.floor(curIdx / n);
            const c = curIdx % n;

            // up
            if (r > 0) {
                const nb = curIdx - n;
                if (visited[nb]) uf.union(curIdx, nb);
            }
            // down
            if (r < m - 1) {
                const nb = curIdx + n;
                if (visited[nb]) uf.union(curIdx, nb);
            }
            // left
            if (c > 0) {
                const nb = curIdx - 1;
                if (visited[nb]) uf.union(curIdx, nb);
            }
            // right
            if (c < n - 1) {
                const nb = curIdx + 1;
                if (visited[nb]) uf.union(curIdx, nb);
            }

            cellPtr++;
        }
        ans[q.idx] = visited[0] ? uf.getSize(0) : 0;
    }

    return ans;
};
```

## Typescript

```typescript
function maxPoints(grid: number[][], queries: number[]): number[] {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;

    // collect all cells with their values and linear indices
    const cells: { val: number; idx: number }[] = new Array(total);
    let pos = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            cells[pos++] = { val: grid[i][j], idx: i * n + j };
        }
    }
    cells.sort((a, b) => a.val - b.val);

    // queries with original indices
    const qObjs: { val: number; idx: number }[] = queries.map((v, i) => ({ val: v, idx: i }));
    qObjs.sort((a, b) => a.val - b.val);

    class UnionFind {
        parent: Int32Array;
        size: Int32Array;
        constructor(sz: number) {
            this.parent = new Int32Array(sz);
            this.size = new Int32Array(sz);
            for (let i = 0; i < sz; i++) this.parent[i] = -1; // inactive
        }
        isActive(x: number): boolean {
            return this.parent[x] !== -1;
        }
        activate(x: number): void {
            this.parent[x] = x;
            this.size[x] = 1;
        }
        find(x: number): number {
            let root = x;
            while (this.parent[root] !== root) {
                root = this.parent[root];
            }
            // path compression
            while (this.parent[x] !== x) {
                const p = this.parent[x];
                this.parent[x] = root;
                x = p;
            }
            return root;
        }
        union(a: number, b: number): void {
            let ra = this.find(a);
            let rb = this.find(b);
            if (ra === rb) return;
            // union by size
            if (this.size[ra] < this.size[rb]) {
                const tmp = ra;
                ra = rb;
                rb = tmp;
            }
            this.parent[rb] = ra;
            this.size[ra] += this.size[rb];
        }
        getSize(x: number): number {
            if (!this.isActive(x)) return 0;
            const r = this.find(x);
            return this.size[r];
        }
    }

    const uf = new UnionFind(total);
    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ];
    let cellPtr = 0;
    const ans: number[] = new Array(queries.length).fill(0);
    const startIdx = 0; // (0,0)

    for (const q of qObjs) {
        const limit = q.val;
        while (cellPtr < total && cells[cellPtr].val < limit) {
            const idx = cells[cellPtr].idx;
            uf.activate(idx);
            const r = Math.floor(idx / n);
            const c = idx % n;
            for (const [dr, dc] of dirs) {
                const nr = r + dr;
                const nc = c + dc;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                const nIdx = nr * n + nc;
                if (uf.isActive(nIdx)) {
                    uf.union(idx, nIdx);
                }
            }
            cellPtr++;
        }
        ans[q.idx] = uf.getSize(startIdx);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer[] $queries
     * @return Integer[]
     */
    function maxPoints($grid, $queries) {
        $m = count($grid);
        $n = count($grid[0]);
        $total = $m * $n;

        // flatten cells with their values and indices
        $cells = [];
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $idx = $i * $n + $j;
                $cells[] = [$grid[$i][$j], $idx];
            }
        }
        usort($cells, function($a, $b) { return $a[0] <=> $b[0]; });

        // queries with original indices
        $qInfo = [];
        foreach ($queries as $idx => $val) {
            $qInfo[] = ['val' => $val, 'idx' => $idx];
        }
        usort($qInfo, function($a, $b) { return $a['val'] <=> $b['val']; });

        // Union-Find structures
        $parent = array_fill(0, $total, -1);
        $size   = array_fill(0, $total, 1);
        $active = array_fill(0, $total, false);

        // find with path compression (closure)
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] != $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        // union by size (closure)
        $union = function($a, $b) use (&$parent, &$size, &$find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra == $rb) return;
            if ($size[$ra] < $size[$rb]) {
                $tmp = $ra; $ra = $rb; $rb = $tmp;
            }
            $parent[$rb] = $ra;
            $size[$ra] += $size[$rb];
        };

        $answers = array_fill(0, count($queries), 0);
        $cellPtr = 0;
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];

        foreach ($qInfo as $q) {
            $threshold = $q['val'];
            // activate all cells with value < threshold
            while ($cellPtr < $total && $cells[$cellPtr][0] < $threshold) {
                $idx = $cells[$cellPtr][1];
                $active[$idx] = true;
                $parent[$idx] = $idx; // initialize its own set

                $r = intdiv($idx, $n);
                $c = $idx % $n;

                foreach ($dirs as $d) {
                    $nr = $r + $d[0];
                    $nc = $c + $d[1];
                    if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                    $nid = $nr * $n + $nc;
                    if ($active[$nid]) {
                        $union($idx, $nid);
                    }
                }
                ++$cellPtr;
            }

            // answer for this query
            $startIdx = 0; // (0,0)
            if ($active[$startIdx]) {
                $root = $find($startIdx);
                $answers[$q['idx']] = $size[$root];
            } else {
                $answers[$q['idx']] = 0;
            }
        }

        return $answers;
    }
}
```

## Swift

```swift
class UnionFind {
    private var parent: [Int]
    private var size: [Int]

    init(_ n: Int) {
        parent = Array(0..<n)
        size = Array(repeating: 1, count: n)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ a: Int, _ b: Int) {
        var rootA = find(a)
        var rootB = find(b)
        if rootA == rootB { return }
        if size[rootA] < size[rootB] {
            swap(&rootA, &rootB)
        }
        parent[rootB] = rootA
        size[rootA] += size[rootB]
    }

    func getSize(_ x: Int) -> Int {
        let root = find(x)
        return size[root]
    }
}

class Solution {
    func maxPoints(_ grid: [[Int]], _ queries: [Int]) -> [Int] {
        let m = grid.count
        let n = grid[0].count
        let total = m * n

        var cells = [(val: Int, idx: Int)]()
        cells.reserveCapacity(total)
        for i in 0..<m {
            for j in 0..<n {
                cells.append((grid[i][j], i * n + j))
            }
        }
        cells.sort { $0.val < $1.val }

        var q = [(val: Int, idx: Int)]()
        q.reserveCapacity(queries.count)
        for (i, v) in queries.enumerated() {
            q.append((v, i))
        }
        q.sort { $0.val < $1.val }

        var answer = Array(repeating: 0, count: queries.count)
        var visited = Array(repeating: false, count: total)
        let uf = UnionFind(total)

        var cellPtr = 0
        for query in q {
            while cellPtr < cells.count && cells[cellPtr].val < query.val {
                let idx = cells[cellPtr].idx
                visited[idx] = true
                let r = idx / n
                let c = idx % n

                if r > 0 {
                    let nb = (r - 1) * n + c
                    if visited[nb] { uf.union(idx, nb) }
                }
                if r + 1 < m {
                    let nb = (r + 1) * n + c
                    if visited[nb] { uf.union(idx, nb) }
                }
                if c > 0 {
                    let nb = r * n + (c - 1)
                    if visited[nb] { uf.union(idx, nb) }
                }
                if c + 1 < n {
                    let nb = r * n + (c + 1)
                    if visited[nb] { uf.union(idx, nb) }
                }

                cellPtr += 1
            }
            if visited[0] {
                answer[query.idx] = uf.getSize(0)
            } else {
                answer[query.idx] = 0
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPoints(grid: Array<IntArray>, queries: IntArray): IntArray {
        val m = grid.size
        val n = grid[0].size
        val total = m * n

        data class Cell(val value: Int, val idx: Int)
        val cells = ArrayList<Cell>(total)
        for (i in 0 until m) {
            for (j in 0 until n) {
                cells.add(Cell(grid[i][j], i * n + j))
            }
        }
        cells.sortBy { it.value }

        data class Q(val value: Int, val idx: Int)
        val qs = ArrayList<Q>(queries.size)
        for (i in queries.indices) {
            qs.add(Q(queries[i], i))
        }
        qs.sortBy { it.value }

        val parent = IntArray(total) { -1 }
        val size = IntArray(total) { 1 }
        val active = BooleanArray(total)

        fun find(x: Int): Int {
            var p = x
            while (parent[p] != p) {
                parent[p] = parent[parent[p]]
                p = parent[p]
            }
            return p
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (size[ra] < size[rb]) {
                val tmp = ra; ra = rb; rb = tmp
            }
            parent[rb] = ra
            size[ra] += size[rb]
        }

        var cellIdx = 0
        val ans = IntArray(queries.size)
        for (q in qs) {
            while (cellIdx < total && cells[cellIdx].value < q.value) {
                val idx = cells[cellIdx].idx
                active[idx] = true
                parent[idx] = idx

                val r = idx / n
                val c = idx % n
                if (r > 0 && active[idx - n]) union(idx, idx - n)
                if (r < m - 1 && active[idx + n]) union(idx, idx + n)
                if (c > 0 && active[idx - 1]) union(idx, idx - 1)
                if (c < n - 1 && active[idx + 1]) union(idx, idx + 1)

                cellIdx++
            }
            val startIdx = 0
            ans[q.idx] = if (active[startIdx]) size[find(startIdx)] else 0
        }

        return ans
    }
}
```

## Dart

```dart
class UnionFind {
  late List<int> parent;
  late List<int> size;

  UnionFind(int n) {
    parent = List.filled(n, -1);
    size = List.filled(n, 1);
  }

  int find(int x) {
    if (parent[x] == -1) return x;
    parent[x] = find(parent[x]);
    return parent[x];
  }

  void union(int a, int b) {
    int ra = find(a);
    int rb = find(b);
    if (ra == rb) return;
    if (size[ra] < size[rb]) {
      int tmp = ra;
      ra = rb;
      rb = tmp;
    }
    parent[rb] = ra;
    size[ra] += size[rb];
  }

  int getSize(int x) => size[find(x)];
}

class Solution {
  List<int> maxPoints(List<List<int>> grid, List<int> queries) {
    int m = grid.length;
    int n = grid[0].length;
    int total = m * n;

    // Flatten cells with their values and indices
    List<List<int>> cells = List.generate(total, (i) => [0, 0]);
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        int idx = i * n + j;
        cells[idx][0] = grid[i][j];
        cells[idx][1] = idx;
      }
    }
    cells.sort((a, b) => a[0].compareTo(b[0]));

    // Prepare sorted queries with original indices
    List<List<int>> qSorted = List.generate(queries.length, (i) => [queries[i], i]);
    qSorted.sort((a, b) => a[0].compareTo(b[0]));

    UnionFind uf = UnionFind(total);
    List<bool> active = List.filled(total, false);
    List<int> answer = List.filled(queries.length, 0);

    int cellPtr = 0;
    const List<int> dr = [-1, 1, 0, 0];
    const List<int> dc = [0, 0, -1, 1];

    for (var q in qSorted) {
      int limit = q[0];
      int qIdx = q[1];

      while (cellPtr < total && cells[cellPtr][0] < limit) {
        int idx = cells[cellPtr][1];
        active[idx] = true;
        int r = idx ~/ n;
        int c = idx % n;

        for (int d = 0; d < 4; ++d) {
          int nr = r + dr[d];
          int nc = c + dc[d];
          if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
            int nIdx = nr * n + nc;
            if (active[nIdx]) {
              uf.union(idx, nIdx);
            }
          }
        }
        cellPtr++;
      }

      if (active[0]) {
        answer[qIdx] = uf.getSize(0);
      } else {
        answer[qIdx] = 0;
      }
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
		p[i] = -1 // not active yet
	}
	return &dsu{parent: p, size: s}
}

func (d *dsu) activate(x int) {
	d.parent[x] = x
	d.size[x] = 1
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

func (d *dsu) getSize(x int) int {
	return d.size[d.find(x)]
}

type cell struct {
	val int
	idx int
}

type query struct {
	val int
	idx int
}

func maxPoints(grid [][]int, queries []int) []int {
	m := len(grid)
	n := len(grid[0])
	total := m * n

	// collect cells
	cells := make([]cell, 0, total)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			idx := i*n + j
			cells = append(cells, cell{val: grid[i][j], idx: idx})
		}
	}
	sort.Slice(cells, func(i, j int) bool { return cells[i].val < cells[j].val })

	// collect queries with original indices
	qrs := make([]query, len(queries))
	for i, v := range queries {
		qrs[i] = query{val: v, idx: i}
	}
	sort.Slice(qrs, func(i, j int) bool { return qrs[i].val < qrs[j].val })

	ds := newDSU(total)
	active := make([]bool, total)

	ans := make([]int, len(queries))
	cellPtr := 0
	dirR := []int{-1, 1, 0, 0}
	dirC := []int{0, 0, -1, 1}

	for _, q := range qrs {
		// add all cells with value < query.val
		for cellPtr < total && cells[cellPtr].val < q.val {
			idx := cells[cellPtr].idx
			active[idx] = true
			ds.activate(idx)

			r := idx / n
			c := idx % n
			for d := 0; d < 4; d++ {
				nr, nc := r+dirR[d], c+dirC[d]
				if nr >= 0 && nr < m && nc >= 0 && nc < n {
					neighborIdx := nr*n + nc
					if active[neighborIdx] {
						ds.union(idx, neighborIdx)
					}
				}
			}
			cellPtr++
		}
		startIdx := 0 // (0,0)
		if active[startIdx] {
			ans[q.idx] = ds.getSize(startIdx)
		} else {
			ans[q.idx] = 0
		}
	}

	return ans
}
```

## Ruby

```ruby
class UnionFind
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @size = Array.new(n, 1)
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
    # union by size
    if @size[ra] < @size[rb]
      ra, rb = rb, ra
    end
    @parent[rb] = ra
    @size[ra] += @size[rb]
    true
  end

  def size(x)
    root = find(x)
    @size[root]
  end
end

# @param {Integer[][]} grid
# @param {Integer[]} queries
# @return {Integer[]}
def max_points(grid, queries)
  rows = grid.length
  cols = grid[0].length
  total = rows * cols

  cells = []
  rows.times do |r|
    cols.times do |c|
      idx = r * cols + c
      cells << [grid[r][c], idx]
    end
  end
  cells.sort_by! { |v| v[0] }

  q_with_idx = queries.each_with_index.map { |val, i| [val, i] }
  q_with_idx.sort_by! { |v| v[0] }

  uf = UnionFind.new(total)
  active = Array.new(total, false)

  res = Array.new(queries.length, 0)
  cell_ptr = 0
  start_idx = 0

  q_with_idx.each do |q_val, q_idx|
    while cell_ptr < total && cells[cell_ptr][0] < q_val
      _, idx = cells[cell_ptr]
      active[idx] = true
      r = idx / cols
      c = idx % cols

      if r > 0
        nb = idx - cols
        uf.union(idx, nb) if active[nb]
      end
      if r + 1 < rows
        nb = idx + cols
        uf.union(idx, nb) if active[nb]
      end
      if c > 0
        nb = idx - 1
        uf.union(idx, nb) if active[nb]
      end
      if c + 1 < cols
        nb = idx + 1
        uf.union(idx, nb) if active[nb]
      end

      cell_ptr += 1
    end

    res[q_idx] = active[start_idx] ? uf.size(start_idx) : 0
  end

  res
end
```

## Scala

```scala
object Solution {
  def maxPoints(grid: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val total = m * n

    // Flatten cells with their values and indices
    val cells = new Array[(Int, Int)](total)
    var idx = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        cells(idx) = (grid(i)(j), i * n + j)
        idx += 1
        j += 1
      }
      i += 1
    }
    val sortedCells = cells.sortBy(_._1)

    // Sort queries with original indices
    val qWithIdx = queries.zipWithIndex.sortBy(_._1)

    // Union-Find structure
    class DSU(val size: Int) {
      val parent: Array[Int] = Array.fill(size)(-1)
      val sz: Array[Int] = Array.fill(size)(0)

      def activate(x: Int): Unit = {
        parent(x) = x
        sz(x) = 1
      }

      def find(x: Int): Int = {
        var p = parent(x)
        if (p == -1) return -1
        while (p != parent(p)) {
          parent(p) = parent(parent(p))
          p = parent(p)
        }
        // Path compression
        var cur = x
        while (cur != p) {
          val next = parent(cur)
          parent(cur) = p
          cur = next
        }
        p
      }

      def union(a: Int, b: Int): Unit = {
        var ra = find(a)
        var rb = find(b)
        if (ra == -1 || rb == -1 || ra == rb) return
        // Union by size
        if (sz(ra) < sz(rb)) {
          val tmp = ra; ra = rb; rb = tmp
        }
        parent(rb) = ra
        sz(ra) += sz(rb)
      }

      def componentSize(x: Int): Int = {
        val r = find(x)
        if (r == -1) 0 else sz(r)
      }
    }

    val dsu = new DSU(total)
    val active = Array.fill[Boolean](total)(false)

    val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))

    var cellPtr = 0
    val ans = new Array[Int](queries.length)

    for ((qVal, qIdx) <- qWithIdx) {
      while (cellPtr < total && sortedCells(cellPtr)._1 < qVal) {
        val pos = sortedCells(cellPtr)._2
        dsu.activate(pos)
        active(pos) = true

        val r = pos / n
        val c = pos % n

        var d = 0
        while (d < 4) {
          val nr = r + dirs(d)._1
          val nc = c + dirs(d)._2
          if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
            val nb = nr * n + nc
            if (active(nb)) dsu.union(pos, nb)
          }
          d += 1
        }

        cellPtr += 1
      }
      ans(qIdx) = if (active(0)) dsu.componentSize(0) else 0
    }

    ans
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        DSU {
            parent,
            size: vec![1; n],
        }
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
        // union by size
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }

    fn get_size(&mut self, x: usize) -> usize {
        let r = self.find(x);
        self.size[r]
    }
}

impl Solution {
    pub fn max_points(grid: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let rows = grid.len();
        let cols = grid[0].len();
        let total = rows * cols;
        // flatten cells with values
        let mut cells: Vec<(i32, usize)> = Vec::with_capacity(total);
        for i in 0..rows {
            for j in 0..cols {
                let idx = i * cols + j;
                cells.push((grid[i][j], idx));
            }
        }
        cells.sort_by(|a, b| a.0.cmp(&b.0));

        // sort queries with original indices
        let mut qvec: Vec<(i32, usize)> = queries.iter().cloned().enumerate().map(|(i, v)| (v, i)).collect();
        qvec.sort_by(|a, b| a.0.cmp(&b.0));

        let mut dsu = DSU::new(total);
        let mut active = vec![false; total];
        let mut ans = vec![0i32; queries.len()];
        let mut cell_ptr = 0usize;
        let start_idx = 0usize; // (0,0)

        let dirs = [(1_i32, 0_i32), (-1, 0), (0, 1), (0, -1)];

        for (q_val, q_idx) in qvec {
            while cell_ptr < cells.len() && cells[cell_ptr].0 < q_val {
                let idx = cells[cell_ptr].1;
                active[idx] = true;
                let r = idx / cols;
                let c = idx % cols;
                for &(dr, dc) in &dirs {
                    let nr = r as i32 + dr;
                    let nc = c as i32 + dc;
                    if nr >= 0 && nr < rows as i32 && nc >= 0 && nc < cols as i32 {
                        let nidx = nr as usize * cols + nc as usize;
                        if active[nidx] {
                            dsu.union(idx, nidx);
                        }
                    }
                }
                cell_ptr += 1;
            }
            if active[start_idx] {
                ans[q_idx] = dsu.get_size(start_idx) as i32;
            } else {
                ans[q_idx] = 0;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-points grid queries)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  (let* ((rows (length grid))
         (cols (if (null? grid) 0 (length (first grid))))
         (total (* rows cols)))
    ;; structs
    (struct cell (value idx) #:transparent)
    (struct query (value idx) #:transparent)

    ;; flatten and sort cells
    (define cells-list
      (for*/list ([i (in-range rows)]
                  [j (in-range cols)])
        (cell (list-ref (list-ref grid i) j) (+ (* i cols) j))))
    (define sorted-cells
      (sort cells-list < #:key cell-value))
    (define cells-vec (list->vector sorted-cells))

    ;; prepare queries with original indices and sort them
    (define queries-with-index
      (for/list ([q (in-list queries)] [i (in-naturals)])
        (query q i)))
    (define sorted-queries
      (sort queries-with-index < #:key query-value))
    
    ;; Union-Find structures
    (define parent (make-vector total -1)) ; -1 means not activated yet
    (define size   (make-vector total 0))

    (define (find x)
      (let ((p (vector-ref parent x)))
        (if (= p x)
            x
            (let ((root (find p)))
              (vector-set! parent x root)
              root))))

    (define (union a b)
      (let* ((ra (find a))
             (rb (find b)))
        (when (not (= ra rb))
          (let ((size-a (vector-ref size ra))
                (size-b (vector-ref size rb)))
            (if (< size-a size-b)
                (begin
                  (vector-set! parent ra rb)
                  (vector-set! size rb (+ size-a size-b)))
                (begin
                  (vector-set! parent rb ra)
                  (vector-set! size ra (+ size-a size-b))))))))

    (define (activate idx)
      (vector-set! parent idx idx)
      (vector-set! size   idx 1))

    ;; processing
    (define answers (make-vector (length queries) 0))
    (let ((cell-ptr 0))
      (for ([q sorted-queries])
        (define th   (query-value q))
        (define orig (query-index q))
        ;; activate all cells with value < th
        (let loop ()
          (when (and (< cell-ptr total)
                     (< (cell-value (vector-ref cells-vec cell-ptr)) th))
            (define c   (vector-ref cells-vec cell-ptr))
            (define idx (cell-idx c))
            (activate idx)
            ;; union with already activated neighbours
            (define i (quotient idx cols))
            (define j (remainder idx cols))
            (for ([d '((-1 0) (1 0) (0 -1) (0 1))])
              (define ni (+ i (first d)))
              (define nj (+ j (second d)))
              (when (and (>= ni 0) (< ni rows)
                         (>= nj 0) (< nj cols))
                (define nidx (+ (* ni cols) nj))
                (when (not (= (vector-ref parent nidx) -1))
                  (union idx nidx))))
            (set! cell-ptr (+ cell-ptr 1))
            (loop)))
        ;; compute answer for this query
        (if (= (vector-ref parent 0) -1)
            (vector-set! answers orig 0)
            (let ((root (find 0)))
              (vector-set! answers orig (vector-ref size root))))))
    (vector->list answers)))
```

## Erlang

```erlang
-spec max_points(Grid :: [[integer()]], Queries :: [integer()]) -> [integer()].
max_points(Grid, Queries) ->
    Rows = length(Grid),
    Cols = length(hd(Grid)),
    N = Rows * Cols,
    Cells0 = flatten_grid(Grid, 0, Cols, []),
    SortedCells = lists:sort(Cells0),
    IndexedQueries = [{Q, I} || {Q,I} <- lists:zip(Queries, lists:seq(0, length(Queries)-1))],
    SortedQueries = lists:sort(fun({A,_},{B,_}) -> A < B end, IndexedQueries),
    Parent0 = array:new(N, {default, -1}),
    Size0 = array:new(N, {default, 1}),
    Active0 = array:new(N, {default, false}),
    ResultPairs = process_queries(SortedQueries, SortedCells, Rows, Cols, Parent0, Size0, Active0, []),
    SortedResult = lists:keysort(1, ResultPairs),
    [Ans || {_Idx, Ans} <- SortedResult].

flatten_grid([], _RowIdx, _Cols, Acc) -> Acc;
flatten_grid([Row|Rest], RowIdx, Cols, Acc) ->
    Cells = flatten_row(Row, RowIdx, 0, Cols, []),
    flatten_grid(Rest, RowIdx+1, Cols, Cells ++ Acc).

flatten_row([], _RowIdx, _ColIdx, _Cols, Acc) -> Acc;
flatten_row([Val|RestVals], RowIdx, ColIdx, Cols, Acc) ->
    Index = RowIdx*Cols + ColIdx,
    flatten_row(RestVals, RowIdx, ColIdx+1, Cols, [{Val,Index}|Acc]).

process_queries([], _Cells, _Rows, _Cols, _Parent, _Size, _Active, Acc) -> Acc;
process_queries([{QVal,QIdx}|RestQs], Cells, Rows, Cols, Parent, Size, Active, Acc) ->
    {NewParent, NewSize, NewActive, RemainingCells} = activate_cells(Cells, QVal, Rows, Cols, Parent, Size, Active),
    Answer =
        case array:get(0, NewActive) of
            true ->
                {Root,_}=find(0, NewParent),
                array:get(Root, NewSize);
            false -> 0
        end,
    process_queries(RestQs, RemainingCells, Rows, Cols, NewParent, NewSize, NewActive, [{QIdx,Answer}|Acc]).

activate_cells([], _QVal, _Rows, _Cols, Parent, Size, Active) ->
    {Parent, Size, Active, []};
activate_cells([{Val,Idx}=Cell|Rest], QVal, Rows, Cols, Parent, Size, Active) when Val < QVal ->
    P1 = array:set(Idx, Idx, Parent),
    S1 = array:set(Idx, 1, Size),
    A1 = array:set(Idx, true, Active),
    {P2,S2} = union_with_neighbors(Idx, Rows, Cols, P1, S1, A1),
    activate_cells(Rest, QVal, Rows, Cols, P2, S2, A1);
activate_cells(Cells, _QVal, _Rows, _Cols, Parent, Size, Active) ->
    {Parent, Size, Active, Cells}.

union_with_neighbors(Index, Rows, Cols, Parent, Size, Active) ->
    Row = Index div Cols,
    Col = Index rem Cols,
    NeighborCoords = [{Row-1,Col},{Row+1,Col},{Row,Col-1},{Row,Col+1}],
    lists:foldl(fun({R,C}, {PAcc,SAcc}) ->
        if R >= 0, R < Rows, C >= 0, C < Cols ->
                NIdx = R*Cols + C,
                case array:get(NIdx, Active) of
                    true ->
                        {PNew,SNew} = union(Index,NIdx,PAcc,SAcc),
                        {PNew,SNew};
                    false -> {PAcc,SAcc}
                end;
           true -> {PAcc,SAcc}
        end
    end, {Parent,Size}, NeighborCoords).

find(I, Parent) ->
    case array:get(I, Parent) of
        -1 -> {I, Parent};
        P when P == I -> {I, Parent};
        P ->
            {Root, UpdatedParent} = find(P, Parent),
            NewParent = array:set(I, Root, UpdatedParent),
            {Root, NewParent}
    end.

union(A,B, Parent, Size) ->
    {ra, P1} = find(A, Parent),
    {rb, P2} = find(B, P1),
    if ra == rb -> {P2, Size};
       true ->
           Sa = array:get(ra, Size),
           Sb = array:get(rb, Size),
           if Sa < Sb ->
               NewParent = array:set(ra, rb, P2),
               NewSize = array:set(rb, Sa+Sb, Size);
              true ->
               NewParent = array:set(rb, ra, P2),
               NewSize = array:set(ra, Sa+Sb, Size)
           end,
           {NewParent, NewSize}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_points(grid :: [[integer]], queries :: [integer]) :: [integer]
  def max_points(grid, queries) do
    rows = length(grid)
    cols = length(hd(grid))
    total = rows * cols

    cells =
      for r <- 0..rows - 1,
          c <- 0..cols - 1,
          into: [] do
        val = Enum.at(Enum.at(grid, r), c)
        {val, r * cols + c}
      end

    cells_sorted = Enum.sort_by(cells, fn {v, _} -> v end)

    queries_with_idx =
      queries
      |> Enum.with_index()
      |> Enum.map(fn {q, i} -> {q, i} end)

    queries_sorted = Enum.sort_by(queries_with_idx, fn {q, _} -> q end)

    parent = :array.from_list(Enum.to_list(0..total - 1))
    size_arr = :array.from_list(Enum.map(0..total - 1, fn _ -> 1 end))
    visited = :array.new(total, default: false)

    {answers_map, _, _, _, _} =
      process_queries(
        cells_sorted,
        queries_sorted,
        parent,
        size_arr,
        visited,
        %{},
        cols
      )

    Enum.map(0..length(queries) - 1, fn i -> Map.get(answers_map, i) end)
  end

  defp process_queries(cells, [], parent, size, visited, answers, _cols) do
    {answers, parent, size, visited, cells}
  end

  defp process_queries(cells, [{qval, qidx} | rest], parent, size, visited, answers, cols) do
    {parent2, size2, visited2, cells_rest} =
      add_cells_until(cells, qval, parent, size, visited, cols)

    if :array.get(0, visited2) do
      {root, parent3} = find(parent2, 0)
      ans_val = :array.get(root, size2)
      answers2 = Map.put(answers, qidx, ans_val)
      process_queries(cells_rest, rest, parent3, size2, visited2, answers2, cols)
    else
      answers2 = Map.put(answers, qidx, 0)
      process_queries(cells_rest, rest, parent2, size2, visited2, answers2, cols)
    end
  end

  defp add_cells_until(cells, limit, parent, size, visited, cols) do
    case cells do
      [] ->
        {parent, size, visited, []}

      [{val, idx} | rest] ->
        if val < limit do
          visited2 = :array.set(idx, true, visited)
          {parent2, size2} = union_neighbors(idx, parent, size, visited2, cols)

          add_cells_until(rest, limit, parent2, size2, visited2, cols)
        else
          {parent, size, visited, cells}
        end
    end
  end

  defp union_neighbors(idx, parent, size, visited, cols) do
    row = div(idx, cols)
    col = rem(idx, cols)

    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]
    total_cells = :array.size(visited)
    rows = div(total_cells, cols)

    Enum.reduce(dirs, {parent, size}, fn {dr, dc}, {p_acc, s_acc} ->
      nr = row + dr
      nc = col + dc

      if nr >= 0 and nr < rows and nc >= 0 and nc < cols do
        nidx = nr * cols + nc

        if :array.get(nidx, visited) do
          union(p_acc, s_acc, idx, nidx)
        else
          {p_acc, s_acc}
        end
      else
        {p_acc, s_acc}
      end
    end)
  end

  defp union(parent, size, a, b) do
    {ra, parent1} = find(parent, a)
    {rb, parent2} = find(parent1, b)

    if ra == rb do
      {parent2, size}
    else
      sz_a = :array.get(ra, size)
      sz_b = :array.get(rb, size)

      if sz_a < sz_b do
        parent3 = :array.set(ra, rb, parent2)
        size3 = :array.set(rb, sz_a + sz_b, size)
        {parent3, size3}
      else
        parent3 = :array.set(rb, ra, parent2)
        size3 = :array.set(ra, sz_a + sz_b, size)
        {parent3, size3}
      end
    end
  end

  defp find(parent, x) do
    p = :array.get(x, parent)

    if p == x do
      {x, parent}
    else
      {root, parent2} = find(parent, p)
      parent3 = :array.set(x, root, parent2)
      {root, parent3}
    end
  end
end
```

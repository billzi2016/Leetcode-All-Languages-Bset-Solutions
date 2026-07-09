# 1632. Rank Transform of a Matrix

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        struct Cell {int val, r, c;};
        vector<Cell> cells;
        cells.reserve(m * n);
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                cells.push_back({matrix[i][j], i, j});
        sort(cells.begin(), cells.end(), [](const Cell& a, const Cell& b){ return a.val < b.val; });
        
        vector<int> rowRank(m, 0), colRank(n, 0);
        vector<vector<int>> ans(m, vector<int>(n));
        vector<int> parent(m + n);
        function<int(int)> find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra != rb) parent[ra] = rb;
        };
        
        size_t i = 0, sz = cells.size();
        while (i < sz) {
            size_t j = i;
            while (j < sz && cells[j].val == cells[i].val) ++j;
            
            // collect unique nodes for this group
            vector<int> nodes;
            nodes.reserve((j - i) * 2);
            for (size_t k = i; k < j; ++k) {
                nodes.push_back(cells[k].r);
                nodes.push_back(cells[k].c + m);
            }
            sort(nodes.begin(), nodes.end());
            nodes.erase(unique(nodes.begin(), nodes.end()), nodes.end());
            for (int node : nodes) parent[node] = node;
            
            // union rows and columns of equal values
            for (size_t k = i; k < j; ++k)
                unite(cells[k].r, cells[k].c + m);
            
            unordered_map<int,int> rootMax;
            rootMax.reserve(nodes.size()*2);
            // compute max rank needed per component
            for (size_t k = i; k < j; ++k) {
                int r = cells[k].r, c = cells[k].c;
                int root = find(r);
                int cur = max(rowRank[r], colRank[c]);
                if (cur > rootMax[root]) rootMax[root] = cur;
            }
            // assign ranks
            for (size_t k = i; k < j; ++k) {
                int r = cells[k].r, c = cells[k].c;
                int root = find(r);
                int rank = rootMax[root] + 1;
                ans[r][c] = rank;
            }
            // update row and column ranks
            for (size_t k = i; k < j; ++k) {
                int r = cells[k].r, c = cells[k].c;
                int rank = ans[r][c];
                rowRank[r] = colRank[c] = rank;
            }
            i = j;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Cell {
        int r, c, v;
        Cell(int r, int c, int v) {
            this.r = r;
            this.c = c;
            this.v = v;
        }
    }

    private static class UnionFind {
        int[] parent;
        int[] size;
        UnionFind(int n) {
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
            int ra = find(a), rb = find(b);
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

    public int[][] matrixRankTransform(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int total = m * n;
        Cell[] cells = new Cell[total];
        int idx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cells[idx++] = new Cell(i, j, matrix[i][j]);
            }
        }
        java.util.Arrays.sort(cells, (a, b) -> Integer.compare(a.v, b.v));

        int[] rowMax = new int[m];
        int[] colMax = new int[n];
        int[][] answer = new int[m][n];

        for (int i = 0; i < total; ) {
            int j = i;
            while (j < total && cells[j].v == cells[i].v) j++;

            UnionFind uf = new UnionFind(m + n);
            // union rows and columns for this value
            for (int k = i; k < j; k++) {
                Cell cell = cells[k];
                uf.union(cell.r, m + cell.c);
            }

            java.util.HashMap<Integer, Integer> rootMax = new java.util.HashMap<>();
            // compute max rank needed for each component
            for (int k = i; k < j; k++) {
                Cell cell = cells[k];
                int root = uf.find(cell.r);
                int cur = Math.max(rowMax[cell.r], colMax[cell.c]);
                Integer prev = rootMax.get(root);
                if (prev == null || cur > prev) rootMax.put(root, cur);
            }

            // assign ranks
            for (int k = i; k < j; k++) {
                Cell cell = cells[k];
                int root = uf.find(cell.r);
                int rank = rootMax.get(root) + 1;
                answer[cell.r][cell.c] = rank;
            }

            // update row and column max ranks
            for (int k = i; k < j; k++) {
                Cell cell = cells[k];
                int rank = answer[cell.r][cell.c];
                if (rank > rowMax[cell.r]) rowMax[cell.r] = rank;
                if (rank > colMax[cell.c]) colMax[cell.c] = rank;
            }

            i = j;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((matrix[i][j], i, j))
        cells.sort(key=lambda x: x[0])

        parent = list(range(m + n))
        rank = [0] * (m + n)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[ry] = rx
                if rank[rx] == rank[ry]:
                    rank[rx] += 1

        rowMax = [0] * m
        colMax = [0] * n
        answer = [[0] * n for _ in range(m)]

        i = 0
        while i < len(cells):
            j = i
            # group by same value
            while j < len(cells) and cells[j][0] == cells[i][0]:
                j += 1

            # reset DSU for this group (only need fresh parents for involved nodes)
            # We'll reuse parent array but reinitialize only needed indices.
            # Simpler: create new DSU structures limited to m+n size each group.
            parent = list(range(m + n))
            rank = [0] * (m + n)

            # union rows and columns for cells in this group
            for k in range(i, j):
                _, r, c = cells[k]
                union(r, c + m)

            # compute the max rank for each component
            compMax = {}
            for k in range(i, j):
                _, r, c = cells[k]
                root = find(r)
                cur = max(rowMax[r], colMax[c])
                if root not in compMax or cur > compMax[root]:
                    compMax[root] = cur

            # assign ranks and update row/col maxima
            for k in range(i, j):
                _, r, c = cells[k]
                root = find(r)
                rank_val = compMax[root] + 1
                answer[r][c] = rank_val
                rowMax[r] = rank_val
                colMax[c] = rank_val

            i = j

        return answer
```

## Python3

```python
class Solution:
    def matrixRankTransform(self, matrix):
        from collections import defaultdict
        m, n = len(matrix), len(matrix[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((matrix[i][j], i, j))
        cells.sort(key=lambda x: x[0])

        row_max = [0] * m
        col_max = [0] * n
        ans = [[0] * n for _ in range(m)]

        class DSU:
            __slots__ = ("parent", "rank")
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
                    return
                if self.rank[ra] < self.rank[rb]:
                    self.parent[ra] = rb
                elif self.rank[ra] > self.rank[rb]:
                    self.parent[rb] = ra
                else:
                    self.parent[rb] = ra
                    self.rank[ra] += 1

        idx = 0
        total = len(cells)
        while idx < total:
            val = cells[idx][0]
            group = []
            while idx < total and cells[idx][0] == val:
                _, r, c = cells[idx]
                group.append((r, c))
                idx += 1

            dsu = DSU(m + n)
            for r, c in group:
                dsu.union(r, c + m)

            comp_max = {}
            for r, c in group:
                root = dsu.find(r)
                cur = max(row_max[r], col_max[c])
                if root not in comp_max or cur > comp_max[root]:
                    comp_max[root] = cur

            for r, c in group:
                root = dsu.find(r)
                rank = comp_max[root] + 1
                ans[r][c] = rank

            for r, c in group:
                rank = ans[r][c]
                if row_max[r] < rank:
                    row_max[r] = rank
                if col_max[c] < rank:
                    col_max[c] = rank

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int r;
    int c;
    int idx;
} Cell;

static int cmpCell(const void *a, const void *b) {
    const Cell *ca = (const Cell *)a;
    const Cell *cb = (const Cell *)b;
    if (ca->val < cb->val) return -1;
    if (ca->val > cb->val) return 1;
    return 0;
}

/* Union-Find */
static int findRoot(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unionSet(int *parent, int *rankUF, int x, int y) {
    int rx = findRoot(parent, x);
    int ry = findRoot(parent, y);
    if (rx == ry) return;
    if (rankUF[rx] < rankUF[ry]) {
        parent[rx] = ry;
    } else if (rankUF[rx] > rankUF[ry]) {
        parent[ry] = rx;
    } else {
        parent[ry] = rx;
        rankUF[rx]++;
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixRankTransform(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int*** returnColumnSizes) {
    int m = matrixSize;
    int n = matrixColSize[0];
    int total = m * n;

    /* collect cells */
    Cell *cells = (Cell *)malloc(total * sizeof(Cell));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int idx = i * n + j;
            cells[idx].val = matrix[i][j];
            cells[idx].r = i;
            cells[idx].c = j;
            cells[idx].idx = idx;
        }
    }

    qsort(cells, total, sizeof(Cell), cmpCell);

    /* answer allocation */
    int **ans = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        ans[i] = (int *)malloc(n * sizeof(int));
    }
    *returnSize = m;
    *returnColumnSizes = (int **)malloc(sizeof(int *));
    **returnColumnSizes = (int *)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) {
        (**returnColumnSizes)[i] = n;
    }

    /* row and column max ranks so far */
    int *rowMax = (int *)calloc(m, sizeof(int));
    int *colMax = (int *)calloc(n, sizeof(int));

    /* union-find structures */
    int *parent = (int *)malloc(total * sizeof(int));
    int *rankUF = (int *)malloc(total * sizeof(int));

    /* temporary maps for rows and columns within a group */
    int *rowMap = (int *)malloc(m * sizeof(int));
    int *colMap = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < m; ++i) rowMap[i] = -1;
    for (int j = 0; j < n; ++j) colMap[j] = -1;

    /* component max rank tracking */
    int *compMax = (int *)malloc(total * sizeof(int));
    int *vis = (int *)calloc(total, sizeof(int));
    int curVis = 1;

    int i = 0;
    while (i < total) {
        int j = i;
        while (j < total && cells[j].val == cells[i].val) ++j; /* group [i, j) */

        /* initialize union-find for this group and build connections */
        for (int k = i; k < j; ++k) {
            int idx = cells[k].idx;
            parent[idx] = idx;
            rankUF[idx] = 0;
        }

        /* rows/cols used in this group to reset later */
        int *usedRows = (int *)malloc((j - i) * sizeof(int));
        int *usedCols = (int *)malloc((j - i) * sizeof(int));
        int rCnt = 0, cCnt = 0;

        for (int k = i; k < j; ++k) {
            int idx = cells[k].idx;
            int r = cells[k].r;
            int c = cells[k].c;

            if (rowMap[r] == -1) {
                rowMap[r] = idx;
                usedRows[rCnt++] = r;
            } else {
                unionSet(parent, rankUF, idx, rowMap[r]);
            }

            if (colMap[c] == -1) {
                colMap[c] = idx;
                usedCols[cCnt++] = c;
            } else {
                unionSet(parent, rankUF, idx, colMap[c]);
            }
        }

        /* compute component max rank */
        for (int k = i; k < j; ++k) {
            int idx = cells[k].idx;
            int r = cells[k].r;
            int c = cells[k].c;
            int root = findRoot(parent, idx);
            int curRank = (rowMax[r] > colMax[c] ? rowMax[r] : colMax[c]) + 1;

            if (vis[root] != curVis) {
                vis[root] = curVis;
                compMax[root] = curRank;
            } else if (curRank > compMax[root]) {
                compMax[root] = curRank;
            }
        }

        /* assign ranks */
        for (int k = i; k < j; ++k) {
            int idx = cells[k].idx;
            int r = cells[k].r;
            int c = cells[k].c;
            int root = findRoot(parent, idx);
            int rank = compMax[root];
            ans[r][c] = rank;
        }

        /* update row and column maxes */
        for (int k = i; k < j; ++k) {
            int r = cells[k].r;
            int c = cells[k].c;
            int rank = ans[r][c];
            if (rank > rowMax[r]) rowMax[r] = rank;
            if (rank > colMax[c]) colMax[c] = rank;
        }

        /* reset maps */
        for (int t = 0; t < rCnt; ++t) rowMap[usedRows[t]] = -1;
        for (int t = 0; t < cCnt; ++t) colMap[usedCols[t]] = -1;

        free(usedRows);
        free(usedCols);

        curVis++; /* move to next group */
        i = j;
    }

    free(cells);
    free(parent);
    free(rankUF);
    free(rowMap);
    free(colMap);
    free(compMax);
    free(vis);
    free(rowMax);
    free(colMax);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] MatrixRankTransform(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int total = m * n;
        var cells = new Cell[total];
        int idx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cells[idx++] = new Cell { val = matrix[i][j], i = i, j = j };
            }
        }
        Array.Sort(cells, (a, b) => a.val.CompareTo(b.val));

        int[][] answer = new int[m][];
        for (int i = 0; i < m; i++) answer[i] = new int[n];

        int[] rowRank = new int[m];
        int[] colRank = new int[n];

        int pos = 0;
        while (pos < total) {
            int curVal = cells[pos].val;
            int end = pos;
            while (end < total && cells[end].val == curVal) end++;
            int groupSize = end - pos;

            var dsu = new DSU(groupSize);
            var rowMap = new Dictionary<int, int>();
            var colMap = new Dictionary<int, int>();

            for (int k = 0; k < groupSize; k++) {
                var c = cells[pos + k];
                if (rowMap.TryGetValue(c.i, out int prevRow)) dsu.Union(k, prevRow);
                else rowMap[c.i] = k;

                if (colMap.TryGetValue(c.j, out int prevCol)) dsu.Union(k, prevCol);
                else colMap[c.j] = k;
            }

            var rootMaxPrev = new Dictionary<int, int>();
            for (int k = 0; k < groupSize; k++) {
                var c = cells[pos + k];
                int root = dsu.Find(k);
                int prev = Math.Max(rowRank[c.i], colRank[c.j]);
                if (rootMaxPrev.TryGetValue(root, out int cur) ) {
                    if (prev > cur) rootMaxPrev[root] = prev;
                } else {
                    rootMaxPrev[root] = prev;
                }
            }

            for (int k = 0; k < groupSize; k++) {
                var c = cells[pos + k];
                int root = dsu.Find(k);
                int rank = rootMaxPrev[root] + 1;
                answer[c.i][c.j] = rank;
                rowRank[c.i] = Math.Max(rowRank[c.i], rank);
                colRank[c.j] = Math.Max(colRank[c.j], rank);
            }

            pos = end;
        }

        return answer;
    }

    private struct Cell {
        public int val;
        public int i;
        public int j;
    }

    private class DSU {
        private int[] parent;
        private int[] size;

        public DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }

        public void Union(int a, int b) {
            int ra = Find(a);
            int rb = Find(b);
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
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var matrixRankTransform = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const cells = [];
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            cells.push([matrix[i][j], i, j]);
        }
    }
    cells.sort((a, b) => a[0] - b[0]);

    const rowRank = new Int32Array(m);
    const colRank = new Int32Array(n);
    const answer = Array.from({ length: m }, () => new Int32Array(n));

    const parent = new Int32Array(m + n);
    const seen = new Int32Array(m + n);
    let version = 1;

    const find = (x) => {
        if (seen[x] !== version) {
            parent[x] = x;
            seen[x] = version;
        }
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };

    const union = (a, b) => {
        let ra = find(a);
        let rb = find(b);
        if (ra !== rb) parent[rb] = ra;
    };

    let idx = 0;
    while (idx < cells.length) {
        let j = idx;
        const val = cells[idx][0];
        while (j < cells.length && cells[j][0] === val) ++j;

        version++; // new DSU context for this group

        // Union rows and columns within the same value group
        for (let k = idx; k < j; ++k) {
            const r = cells[k][1];
            const c = cells[k][2];
            union(r, m + c);
        }

        // Determine max previous rank per component
        const compMax = new Map();
        for (let k = idx; k < j; ++k) {
            const r = cells[k][1];
            const c = cells[k][2];
            const root = find(r);
            const prev = Math.max(rowRank[r], colRank[c]);
            const cur = compMax.get(root);
            if (cur === undefined || prev > cur) compMax.set(root, prev);
        }

        // Assign ranks
        for (let k = idx; k < j; ++k) {
            const r = cells[k][1];
            const c = cells[k][2];
            const root = find(r);
            const rank = compMax.get(root) + 1;
            answer[r][c] = rank;
        }

        // Update row and column ranks
        for (let k = idx; k < j; ++k) {
            const r = cells[k][1];
            const c = cells[k][2];
            const rank = answer[r][c];
            if (rank > rowRank[r]) rowRank[r] = rank;
            if (rank > colRank[c]) colRank[c] = rank;
        }

        idx = j;
    }

    // Convert Int32Array rows to regular arrays for output
    return answer.map(row => Array.from(row));
};
```

## Typescript

```typescript
function matrixRankTransform(matrix: number[][]): number[][] {
    const m = matrix.length;
    const n = matrix[0].length;
    const ans: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    const rowRank = new Int32Array(m);
    const colRank = new Int32Array(n);

    interface Cell { v: number; r: number; c: number; }
    const cells: Cell[] = [];
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            cells.push({ v: matrix[i][j], r: i, c: j });
        }
    }
    cells.sort((a, b) => a.v - b.v);

    class DSU {
        parent: Int32Array;
        constructor(size: number) {
            this.parent = new Int32Array(size);
            for (let i = 0; i < size; ++i) this.parent[i] = i;
        }
        find(x: number): number {
            const p = this.parent[x];
            if (p !== x) this.parent[x] = this.find(p);
            return this.parent[x];
        }
        union(a: number, b: number): void {
            let ra = this.find(a), rb = this.find(b);
            if (ra !== rb) this.parent[rb] = ra;
        }
    }

    let idx = 0;
    while (idx < cells.length) {
        const start = idx;
        const val = cells[start].v;
        while (idx < cells.length && cells[idx].v === val) idx++;

        const dsu = new DSU(m + n);
        for (let k = start; k < idx; ++k) {
            const { r, c } = cells[k];
            dsu.union(r, c + m);
        }

        const compMax = new Map<number, number>();
        for (let k = start; k < idx; ++k) {
            const { r, c } = cells[k];
            const root = dsu.find(r);
            const cur = Math.max(rowRank[r], colRank[c]);
            const prev = compMax.get(root) ?? 0;
            if (cur > prev) compMax.set(root, cur);
        }

        for (let k = start; k < idx; ++k) {
            const { r, c } = cells[k];
            const root = dsu.find(r);
            const rank = (compMax.get(root) ?? 0) + 1;
            ans[r][c] = rank;
            rowRank[r] = rank;
            colRank[c] = rank;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function matrixRankTransform($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $cells = [];
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $cells[] = [$matrix[$r][$c], $r, $c];
            }
        }
        usort($cells, function($a, $b) { return $a[0] <=> $b[0]; });
        
        $rowMax = array_fill(0, $m, 0);
        $colMax = array_fill(0, $n, 0);
        $ans = array_fill(0, $m, array_fill(0, $n, 0));
        
        $total = count($cells);
        $i = 0;
        while ($i < $total) {
            $j = $i;
            while ($j < $total && $cells[$j][0] == $cells[$i][0]) {
                $j++;
            }
            
            // initialize DSU
            $size = $m + $n;
            $parent = [];
            for ($k = 0; $k < $size; $k++) {
                $parent[$k] = $k;
            }
            
            // union rows and columns for this value group
            for ($p = $i; $p < $j; $p++) {
                $r = $cells[$p][1];
                $c = $cells[$p][2];
                $x = $r;
                $y = $c + $m;
                $rx = $this->find($parent, $x);
                $ry = $this->find($parent, $y);
                if ($rx != $ry) {
                    $parent[$rx] = $ry;
                }
            }
            
            // compute max rank for each component
            $compMax = [];
            for ($p = $i; $p < $j; $p++) {
                $r = $cells[$p][1];
                $c = $cells[$p][2];
                $root = $this->find($parent, $r);
                $candidate = max($rowMax[$r], $colMax[$c]);
                if (!isset($compMax[$root]) || $compMax[$root] < $candidate) {
                    $compMax[$root] = $candidate;
                }
            }
            
            // assign ranks
            for ($p = $i; $p < $j; $p++) {
                $r = $cells[$p][1];
                $c = $cells[$p][2];
                $root = $this->find($parent, $r);
                $rank = $compMax[$root] + 1;
                $ans[$r][$c] = $rank;
            }
            
            // update row and column max ranks
            for ($p = $i; $p < $j; $p++) {
                $r = $cells[$p][1];
                $c = $cells[$p][2];
                $rank = $ans[$r][$c];
                if ($rowMax[$r] < $rank) $rowMax[$r] = $rank;
                if ($colMax[$c] < $rank) $colMax[$c] = $rank;
            }
            
            $i = $j;
        }
        
        return $ans;
    }
    
    private function find(&$parent, $x) {
        while ($parent[$x] != $x) {
            $parent[$x] = $parent[$parent[$x]];
            $x = $parent[$x];
        }
        return $x;
    }
}
```

## Swift

```swift
class Solution {
    func matrixRankTransform(_ matrix: [[Int]]) -> [[Int]] {
        let m = matrix.count
        let n = matrix[0].count
        var cells = [(value: Int, r: Int, c: Int)]()
        cells.reserveCapacity(m * n)
        for i in 0..<m {
            for j in 0..<n {
                cells.append((matrix[i][j], i, j))
            }
        }
        cells.sort { $0.value < $1.value }

        var rowRank = Array(repeating: 0, count: m)
        var colRank = Array(repeating: 0, count: n)
        var answer = Array(repeating: Array(repeating: 0, count: n), count: m)

        var idx = 0
        while idx < cells.count {
            let curVal = cells[idx].value
            var group = [(r: Int, c: Int)]()
            while idx < cells.count && cells[idx].value == curVal {
                group.append((cells[idx].r, cells[idx].c))
                idx += 1
            }

            // DSU for this value group
            let size = m + n
            var parent = Array(0..<size)
            func find(_ x: Int) -> Int {
                var x = x
                while parent[x] != x {
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                }
                return x
            }
            func union(_ a: Int, _ b: Int) {
                let ra = find(a)
                let rb = find(b)
                if ra != rb { parent[ra] = rb }
            }

            for cell in group {
                union(cell.r, cell.c + m)
            }

            var maxRank = Array(repeating: 0, count: size)
            for cell in group {
                let root = find(cell.r)
                let cur = max(rowRank[cell.r], colRank[cell.c])
                if cur > maxRank[root] { maxRank[root] = cur }
            }

            for cell in group {
                let rank = maxRank[find(cell.r)] + 1
                answer[cell.r][cell.c] = rank
            }

            for cell in group {
                let rank = answer[cell.r][cell.c]
                if rank > rowRank[cell.r] { rowRank[cell.r] = rank }
                if rank > colRank[cell.c] { colRank[cell.c] = rank }
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun matrixRankTransform(matrix: Array<IntArray>): Array<IntArray> {
        val m = matrix.size
        val n = matrix[0].size
        data class Cell(val value: Int, val i: Int, val j: Int)
        val cells = mutableListOf<Cell>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                cells.add(Cell(matrix[i][j], i, j))
            }
        }
        cells.sortWith(compareBy<Cell> { it.value })
        val answer = Array(m) { IntArray(n) }
        val rowRank = IntArray(m)
        val colRank = IntArray(n)

        var idx = 0
        while (idx < cells.size) {
            val start = idx
            val curVal = cells[idx].value
            while (idx < cells.size && cells[idx].value == curVal) idx++

            // DSU for this group
            val parent = IntArray(m + n) { it }
            fun find(x: Int): Int {
                var p = x
                while (parent[p] != p) {
                    parent[p] = parent[parent[p]]
                    p = parent[p]
                }
                return p
            }
            fun union(a: Int, b: Int) {
                val ra = find(a)
                val rb = find(b)
                if (ra != rb) {
                    parent[rb] = ra
                }
            }

            // Union rows and columns for cells with same value
            for (k in start until idx) {
                val i = cells[k].i
                val j = cells[k].j
                union(i, m + j)
            }

            // Compute max rank needed for each component
            val compMax = HashMap<Int, Int>()
            for (k in start until idx) {
                val i = cells[k].i
                val j = cells[k].j
                val root = find(i)
                val cur = kotlin.math.max(rowRank[i], colRank[j])
                val prev = compMax[root]
                if (prev == null || cur > prev) {
                    compMax[root] = cur
                }
            }

            // Assign ranks
            for (k in start until idx) {
                val i = cells[k].i
                val j = cells[k].j
                val root = find(i)
                val newRank = compMax[root]!! + 1
                answer[i][j] = newRank
            }

            // Update row and column ranks
            for (k in start until idx) {
                val i = cells[k].i
                val j = cells[k].j
                val r = answer[i][j]
                if (r > rowRank[i]) rowRank[i] = r
                if (r > colRank[j]) colRank[j] = r
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> matrixRankTransform(List<List<int>> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    List<List<int>> ans = List.generate(m, (_) => List.filled(n, 0));
    List<int> rank = List.filled(m + n, 0);

    // collect cells
    List<List<int>> cells = [];
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        cells.add([matrix[i][j], i, j]);
      }
    }
    cells.sort((a, b) => a[0].compareTo(b[0]));

    int idx = 0;
    while (idx < cells.length) {
      int start = idx;
      int val = cells[idx][0];
      while (idx < cells.length && cells[idx][0] == val) idx++;
      // process group [start, idx)
      DSU dsu = DSU(m + n);
      for (int k = start; k < idx; ++k) {
        int r = cells[k][1];
        int c = cells[k][2];
        dsu.union(r, m + c);
      }

      // compute max rank per component
      Map<int, int> compMax = {};
      for (int k = start; k < idx; ++k) {
        int r = cells[k][1];
        int c = cells[k][2];
        int root = dsu.find(r);
        int cur = rank[r] > rank[m + c] ? rank[r] : rank[m + c];
        compMax[root] = compMax.containsKey(root)
            ? (compMax[root]! > cur ? compMax[root]! : cur)
            : cur;
      }

      // assign new ranks and update row/col ranks
      for (int k = start; k < idx; ++k) {
        int r = cells[k][1];
        int c = cells[k][2];
        int root = dsu.find(r);
        int newRank = compMax[root]! + 1;
        ans[r][c] = newRank;
      }
      for (int k = start; k < idx; ++k) {
        int r = cells[k][1];
        int c = cells[k][2];
        int root = dsu.find(r);
        int newRank = compMax[root]! + 1;
        rank[r] = newRank;
        rank[m + c] = newRank;
      }
    }

    return ans;
  }
}

class DSU {
  List<int> parent;
  List<int> rank;

  DSU(int size)
      : parent = List.generate(size, (i) => i),
        rank = List.filled(size, 0);

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  void union(int x, int y) {
    int rx = find(x);
    int ry = find(y);
    if (rx == ry) return;
    if (rank[rx] < rank[ry]) {
      parent[rx] = ry;
    } else if (rank[rx] > rank[ry]) {
      parent[ry] = rx;
    } else {
      parent[ry] = rx;
      rank[rx]++;
    }
  }
}
```

## Golang

```go
import "sort"

type cell struct {
	val int
	r   int
	c   int
}

func matrixRankTransform(matrix [][]int) [][]int {
	m, n := len(matrix), len(matrix[0])
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	rowRank := make([]int, m)
	colRank := make([]int, n)

	cells := make([]cell, 0, m*n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			cells = append(cells, cell{val: matrix[i][j], r: i, c: j})
		}
	}
	sort.Slice(cells, func(i, j int) bool { return cells[i].val < cells[j].val })

	for i := 0; i < len(cells); {
		j := i
		for j < len(cells) && cells[j].val == cells[i].val {
			j++
		}
		// DSU for this group
		parent := make(map[int]int)

		var find func(int) int
		find = func(x int) int {
			if parent[x] != x {
				parent[x] = find(parent[x])
			}
			return parent[x]
		}
		union := func(a, b int) {
			ra, rb := find(a), find(b)
			if ra != rb {
				parent[ra] = rb
			}
		}

		// union rows and columns for cells with same value
		for k := i; k < j; k++ {
			r, c := cells[k].r, cells[k].c
			u := r
			v := m + c
			if _, ok := parent[u]; !ok {
				parent[u] = u
			}
			if _, ok := parent[v]; !ok {
				parent[v] = v
			}
			union(u, v)
		}

		// compute max rank for each component
		compMax := make(map[int]int)
		for k := i; k < j; k++ {
			r, c := cells[k].r, cells[k].c
			root := find(r) // row node belongs to its component
			cur := rowRank[r]
			if colRank[c] > cur {
				cur = colRank[c]
			}
			if prev, ok := compMax[root]; !ok || cur > prev {
				compMax[root] = cur
			}
		}

		// assign new ranks and update row/col ranks
		for k := i; k < j; k++ {
			r, c := cells[k].r, cells[k].c
			root := find(r)
			newRank := compMax[root] + 1
			ans[r][c] = newRank
			rowRank[r] = newRank
			colRank[c] = newRank
		}

		i = j
	}
	return ans
}
```

## Ruby

```ruby
class UnionFind
  def initialize
    @parent = {}
  end

  def find(x)
    @parent[x] = x unless @parent.key?(x)
    while @parent[x] != x
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(x, y)
    rx = find(x)
    ry = find(y)
    return if rx == ry
    @parent[ry] = rx
  end
end

# @param {Integer[][]} matrix
# @return {Integer[][]}
def matrix_rank_transform(matrix)
  m = matrix.size
  n = matrix[0].size
  cells = []
  matrix.each_with_index do |row, i|
    row.each_with_index do |val, j|
      cells << [val, i, j]
    end
  end
  cells.sort_by! { |c| c[0] }

  answer = Array.new(m) { Array.new(n, 0) }
  row_rank = Array.new(m, 0)
  col_rank = Array.new(n, 0)

  idx = 0
  while idx < cells.size
    val = cells[idx][0]
    group = []
    while idx < cells.size && cells[idx][0] == val
      group << cells[idx]
      idx += 1
    end

    uf = UnionFind.new
    offset = m # to differentiate column ids
    group.each do |_, i, j|
      uf.union(i, offset + j)
    end

    comp_max = Hash.new(0)
    group.each do |_, i, j|
      root = uf.find(i)
      cur = row_rank[i] > col_rank[j] ? row_rank[i] : col_rank[j]
      comp_max[root] = cur if cur > comp_max[root]
    end

    group.each do |_, i, j|
      root = uf.find(i)
      rank = comp_max[root] + 1
      answer[i][j] = rank
    end

    group.each do |_, i, j|
      r = answer[i][j]
      row_rank[i] = r if r > row_rank[i]
      col_rank[j] = r if r > col_rank[j]
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
  def matrixRankTransform(matrix: Array[Array[Int]]): Array[Array[Int]] = {
    val m = matrix.length
    val n = matrix(0).length
    val cells = new scala.collection.mutable.ArrayBuffer[(Int, Int, Int)]()
    for (i <- 0 until m; j <- 0 until n) cells += ((matrix(i)(j), i, j))
    implicit val ord: Ordering[(Int, Int, Int)] = Ordering.by[(Int, Int, Int), Int](_._1)
    val sorted = cells.sorted

    val rowRank = Array.fill(m)(0)
    val colRank = Array.fill(n)(0)
    val answer = Array.ofDim[Int](m, n)

    var idx = 0
    while (idx < sorted.length) {
      val start = idx
      val value = sorted(idx)._1
      while (idx < sorted.length && sorted(idx)._1 == value) idx += 1
      val end = idx

      val dsu = new DSU(m + n)

      var k = start
      while (k < end) {
        val (_, r, c) = sorted(k)
        dsu.union(r, c + m)
        k += 1
      }

      import scala.collection.mutable
      val rootMax = mutable.Map[Int, Int]()

      k = start
      while (k < end) {
        val (_, r, c) = sorted(k)
        val root = dsu.find(r)
        val prev = math.max(rowRank(r), colRank(c))
        val cur = rootMax.getOrElse(root, 0)
        if (prev > cur) rootMax.update(root, prev)
        k += 1
      }

      k = start
      while (k < end) {
        val (_, r, c) = sorted(k)
        val root = dsu.find(r)
        val rank = rootMax(root) + 1
        answer(r)(c) = rank
        k += 1
      }

      k = start
      while (k < end) {
        val (_, r, c) = sorted(k)
        val rank = answer(r)(c)
        if (rank > rowRank(r)) rowRank(r) = rank
        if (rank > colRank(c)) colRank(c) = rank
        k += 1
      }
    }

    answer
  }

  private class DSU(val n: Int) {
    private val parent = Array.tabulate(n)(i => i)
    private val sizeArr = Array.fill(n)(1)

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def union(a: Int, b: Int): Unit = {
      var x = find(a)
      var y = find(b)
      if (x == y) return
      if (sizeArr(x) < sizeArr(y)) {
        val tmp = x; x = y; y = tmp
      }
      parent(y) = x
      sizeArr(x) += sizeArr(y)
    }
  }
}
```

## Rust

```rust
use std::collections::HashMap;

struct DSU {
    parent: Vec<usize>,
    rank: Vec<usize>,
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
            let p = self.find(self.parent[x]);
            self.parent[x] = p;
        }
        self.parent[x]
    }
    fn union(&mut self, x: usize, y: usize) {
        let mut xr = self.find(x);
        let mut yr = self.find(y);
        if xr == yr {
            return;
        }
        if self.rank[xr] < self.rank[yr] {
            std::mem::swap(&mut xr, &mut yr);
        }
        self.parent[yr] = xr;
        if self.rank[xr] == self.rank[yr] {
            self.rank[xr] += 1;
        }
    }
}

impl Solution {
    pub fn matrix_rank_transform(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut ans = vec![vec![0i32; n]; m];
        let mut cells = Vec::with_capacity(m * n);
        for i in 0..m {
            for j in 0..n {
                cells.push((matrix[i][j], i, j));
            }
        }
        cells.sort_by_key(|k| k.0);

        let mut row_rank = vec![0i32; m];
        let mut col_rank = vec![0i32; n];

        let mut idx = 0;
        while idx < cells.len() {
            let val = cells[idx].0;
            let mut end = idx;
            while end < cells.len() && cells[end].0 == val {
                end += 1;
            }

            let mut dsu = DSU::new(m + n);
            for k in idx..end {
                let r = cells[k].1;
                let c = cells[k].2;
                dsu.union(r, m + c);
            }

            let mut comp_max: HashMap<usize, i32> = HashMap::new();
            for k in idx..end {
                let r = cells[k].1;
                let c = cells[k].2;
                let root = dsu.find(r);
                let cur = row_rank[r].max(col_rank[c]);
                comp_max
                    .entry(root)
                    .and_modify(|e| if cur > *e { *e = cur })
                    .or_insert(cur);
            }

            for k in idx..end {
                let r = cells[k].1;
                let c = cells[k].2;
                let root = dsu.find(r);
                let rank = comp_max[&root] + 1;
                ans[r][c] = rank;
                row_rank[r] = rank;
                col_rank[c] = rank;
            }

            idx = end;
        }
        ans
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (matrix-rank-transform matrix)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((m (length matrix))
         (n (if (= m 0) 0 (length (first matrix))))
         (entries
          (let loop ((i 0) (acc '()))
            (if (= i m)
                acc
                (loop (add1 i)
                      (let inner-loop ((j 0) (inner-acc acc))
                        (if (= j n)
                            inner-acc
                            (inner-loop (add1 j)
                                        (cons (list (list-ref (list-ref matrix i) j) i j)
                                              inner-acc)))))))))
    (define sorted-entries (sort entries (lambda (a b) (< (first a) (first b)))))
    (define row-max (make-vector m 0))
    (define col-max (make-vector n 0))
    (define ans (make-vector m (make-vector n 0)))
    (let process ((idx 0) (len (length sorted-entries)))
      (if (= idx len)
          ;; convert answer vectors to list of lists
          (let ((result '()))
            (for ([i (in-range m)])
              (set! result (cons (vector->list (vector-ref ans i)) result)))
            (reverse result))
          (let* ((val (first (list-ref sorted-entries idx)))
                 ;; find end index of this value group
                 (end (let loop2 ((k idx))
                        (if (and (< k len) (= (first (list-ref sorted-entries k)) val))
                            (loop2 (add1 k))
                            k))))
            ;; union‑find structures for current group
            (define parent (make-hash))
            (define size (make-hash))
            (define (make-set id)
              (hash-set! parent id id)
              (hash-set! size id 1))
            (define (find x)
              (let ((p (hash-ref parent x)))
                (if (= p x)
                    x
                    (let ((root (find p)))
                      (hash-set! parent x root)
                      root))))
            (define (union a b)
              (let* ((ra (find a)) (rb (find b)))
                (when (not (= ra rb))
                  (let ((sa (hash-ref size ra))
                        (sb (hash-ref size rb)))
                    (if (> sa sb)
                        (begin
                          (hash-set! parent rb ra)
                          (hash-set! size ra (+ sa sb)))
                        (begin
                          (hash-set! parent ra rb)
                          (hash-set! size rb (+ sa sb))))))))
            (define row-first (make-hash))
            (define col-first (make-hash))
            ;; initialize sets and union equal‑value cells sharing rows/cols
            (for ([k (in-range idx end)])
              (let* ((cell (list-ref sorted-entries k))
                     (r (second cell)) (c (third cell))
                     (id (+ (* r n) c)))
                (make-set id)
                (if (hash-has-key? row-first r)
                    (union id (hash-ref row-first r))
                    (hash-set! row-first r id))
                (if (hash-has-key? col-first c)
                    (union id (hash-ref col-first c))
                    (hash-set! col-first c id))))
            ;; compute max rank needed for each component
            (define comp-max (make-hash))
            (for ([k (in-range idx end)])
              (let* ((cell (list-ref sorted-entries k))
                     (r (second cell)) (c (third cell))
                     (id (+ (* r n) c))
                     (root (find id))
                     (cur (max (vector-ref row-max r) (vector-ref col-max c))))
                (hash-set! comp-max root
                           (max (hash-ref comp-max root 0) cur))))
            ;; assign ranks and fill answer matrix
            (for ([k (in-range idx end)])
              (let* ((cell (list-ref sorted-entries k))
                     (r (second cell)) (c (third cell))
                     (id (+ (* r n) c))
                     (root (find id))
                     (rank (+ 1 (hash-ref comp-max root))))
                (vector-set! (vector-ref ans r) c rank)))
            ;; update row‑max and col‑max
            (for ([k (in-range idx end)])
              (let* ((cell (list-ref sorted-entries k))
                     (r (second cell)) (c (third cell))
                     (rank (vector-ref (vector-ref ans r) c)))
                (when (> rank (vector-ref row-max r))
                  (vector-set! row-max r rank))
                (when (> rank (vector-ref col-max c))
                  (vector-set! col-max c rank))))
            ;; continue with next group
            (process end len))))))
```

## Erlang

```erlang
-module(solution).
-export([matrix_rank_transform/1]).

-spec matrix_rank_transform(Matrix :: [[integer()]]) -> [[integer()]].
matrix_rank_transform(Matrix) ->
    RowCount = length(Matrix),
    ColCount = case Matrix of
        [] -> 0;
        [FirstRow|_] -> length(FirstRow)
    end,
    RowsIdx = lists:seq(0, RowCount - 1),
    ColsIdx = lists:seq(0, ColCount - 1),

    Cells = [
        {V, R, C}
        || {R, Row} <- lists:zip(RowsIdx, Matrix),
           {C, V}   <- lists:zip(ColsIdx, Row)
    ],

    Sorted = lists:sort(fun({V1, _, _}, {V2, _, _}) -> V1 =< V2 end, Cells),

    {_FinalRowRank, _FinalColRank, RankMap} =
        process(Sorted, #{}, #{}, #{}),

    [
        [ maps:get({R, C}, RankMap) || C <- lists:seq(0, ColCount - 1) ]
        || R <- lists:seq(0, RowCount - 1)
    ].

%% Process sorted cells group by group
process([], RowRank, ColRank, AccRanks) ->
    {RowRank, ColRank, AccRanks};
process([First|Rest], RowRank, ColRank, AccRanks) ->
    Val = element(1, First),
    {Group, Rest2} = take_group([First|Rest], Val, []),

    Positions = [{R, C} || {_V, R, C} <- Group],
    Len = length(Positions),

    Parent0 = maps:from_list([{Idx, Idx} || Idx <- lists:seq(1, Len)]),
    {ParentAfterUnion, _, _} = union_build(Positions, 1, Parent0, #{}, #{}),

    {ParentAfterFind, RootMaxMap} =
        compute_root_max(Positions, 1, ParentAfterUnion, RowRank, ColRank, #{}),

    {AccRanks2, RowRank2, ColRank2} =
        assign_ranks(Positions, 1, ParentAfterFind, RootMaxMap,
                     AccRanks, RowRank, ColRank),

    process(Rest2, RowRank2, ColRank2, AccRanks2).

%% Take consecutive cells with same value
take_group([], _Val, Acc) ->
    {lists:reverse(Acc), []};
take_group([H|T], Val, Acc) ->
    case element(1, H) of
        V when V =:= Val -> take_group(T, Val, [H|Acc]);
        _Other           -> {lists:reverse(Acc), [H|T]}
    end.

%% Union-Find helpers
find(Id, Parent) ->
    case maps:get(Id, Parent) of
        Id -> {Id, Parent};
        P  ->
            {Root, UpdatedParent} = find(P, Parent),
            NewParent = maps:put(Id, Root, UpdatedParent),
            {Root, NewParent}
    end.

union(A, B, Parent) ->
    {RootA, P1} = find(A, Parent),
    {RootB, P2} = find(B, P1),
    if
        RootA == RootB -> P2;
        true           -> maps:put(RootB, RootA, P2)
    end.

%% Build unions within a group based on rows and columns
union_build([], _Idx, Parent, RowFirst, ColFirst) ->
    {Parent, RowFirst, ColFirst};
union_build([{R, C}|Rest], Idx, Parent0, RowFirst0, ColFirst0) ->
    %% Row handling
    {Parent1, RowFirst1} =
        case maps:find(R, RowFirst0) of
            error -> {Parent0, maps:put(R, Idx, RowFirst0)};
            {ok, PrevIdx} -> {union(Idx, PrevIdx, Parent0), RowFirst0}
        end,
    %% Column handling
    {Parent2, ColFirst1} =
        case maps:find(C, ColFirst0) of
            error -> {Parent1, maps:put(C, Idx, ColFirst0)};
            {ok, PrevIdxC} -> {union(Idx, PrevIdxC, Parent1), ColFirst0}
        end,
    union_build(Rest, Idx + 1, Parent2, RowFirst1, ColFirst1).

%% Compute maximum existing rank for each component
compute_root_max([], _Idx, Parent, _RowRank, _ColRank, RootMax) ->
    {Parent, RootMax};
compute_root_max([{R, C}|Rest], Idx, Parent0, RowRank, ColRank, RootMax0) ->
    {Root, Parent1} = find(Idx, Parent0),
    Cur = max(maps:get(R, RowRank, 0), maps:get(C, ColRank, 0)),
    Prev = maps:get(Root, RootMax0, 0),
    NewRootMax = if Cur > Prev -> maps:put(Root, Cur, RootMax0); true -> RootMax0 end,
    compute_root_max(Rest, Idx + 1, Parent1, RowRank, ColRank, NewRootMax).

%% Assign final ranks and update row/col rank maps
assign_ranks([], _Idx, Parent, _RootMax, AccRanks, RowRank, ColRank) ->
    {AccRanks, RowRank, ColRank};
assign_ranks([{R, C}|Rest], Idx, Parent0, RootMaxMap,
             AccRanks0, RowRank0, ColRank0) ->
    {Root, Parent1} = find(Idx, Parent0),
    MaxVal = maps:get(Root, RootMaxMap),
    Rank = MaxVal + 1,
    AccRanks1 = maps:put({R, C}, Rank, AccRanks0),

    RowPrev = maps:get(R, RowRank0, 0),
    ColPrev = maps:get(C, ColRank0, 0),

    RowRank1 = if Rank > RowPrev -> maps:put(R, Rank, RowRank0); true -> RowRank0 end,
    ColRank1 = if Rank > ColPrev -> maps:put(C, Rank, ColRank0); true -> ColRank0 end,

    assign_ranks(Rest, Idx + 1, Parent1, RootMaxMap,
                 AccRanks1, RowRank1, ColRank1).
```

## Elixir

```elixir
defmodule Solution do
  @spec matrix_rank_transform(matrix :: [[integer]]) :: [[integer]]
  def matrix_rank_transform(matrix) do
    m = length(matrix)
    n = length(hd(matrix))

    cells =
      for {row, i} <- Enum.with_index(matrix),
          {val, j} <- Enum.with_index(row),
          do: {val, i, j}

    sorted = Enum.sort_by(cells, fn {v, _, _} -> v end)

    row_rank = :array.new(m, default: 0)
    col_rank = :array.new(n, default: 0)

    rows_arrays =
      Enum.reduce(0..(m - 1), :array.new(m, default: nil), fn i, acc ->
        :array.set(i, :array.new(n, default: 0), acc)
      end)

    process(sorted, m, n, row_rank, col_rank, rows_arrays)
  end

  defp process([], _m, _n, _row_rank, _col_rank, rows_arrays) do
    Enum.map(0..(:array.size(rows_arrays) - 1), fn i ->
      :array.get(i, rows_arrays) |> :array.to_list()
    end)
  end

  defp process(cells, m, n, row_rank, col_rank, rows_arrays) do
    [{first_val, _, _} | _] = cells
    {group, rest} = Enum.split_while(cells, fn {v, _, _} -> v == first_val end)

    parent = build_union(group, m, %{})

    root_max =
      Enum.reduce(group, %{}, fn {_v, i, j}, acc ->
        root = find(i, parent)
        cur = max(:array.get(i, row_rank), :array.get(j, col_rank))
        Map.update(acc, root, cur, &max(&1, cur))
      end)

    root_rank = Enum.into(root_max, %{}, fn {root, mx} -> {root, mx + 1} end)

    {new_row_rank, new_col_rank, new_rows_arrays} =
      Enum.reduce(group, {row_rank, col_rank, rows_arrays}, fn {_v, i, j},
                                                               {rr, cr, ra} ->
        root = find(i, parent)
        rank = Map.fetch!(root_rank, root)

        row_arr = :array.get(i, ra)
        new_row_arr = :array.set(j, rank, row_arr)
        ra2 = :array.set(i, new_row_arr, ra)

        rr2 = :array.set(i, max(:array.get(i, rr), rank), rr)
        cr2 = :array.set(j, max(:array.get(j, cr), rank), cr)

        {rr2, cr2, ra2}
      end)

    process(rest, m, n, new_row_rank, new_col_rank, new_rows_arrays)
  end

  defp build_union(group, m, parent) do
    Enum.reduce(group, parent, fn {_v, i, j}, acc ->
      a = i
      b = j + m
      acc1 = Map.put_new(acc, a, a)
      acc2 = Map.put_new(acc1, b, b)
      union(a, b, acc2)
    end)
  end

  defp find(x, parent) do
    p = Map.get(parent, x)
    if p == x, do: x, else: find(p, parent)
  end

  defp union(a, b, parent) do
    ra = find(a, parent)
    rb = find(b, parent)

    if ra == rb, do: parent, else: Map.put(parent, rb, ra)
  end
end
```

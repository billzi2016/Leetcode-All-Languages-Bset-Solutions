# 0803. Bricks Falling When Hit

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent, sz;
        DSU(int n): parent(n), sz(n,1) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x){
            if(parent[x]==x) return x;
            return parent[x]=find(parent[x]);
        }
        void unite(int a,int b){
            int ra=find(a), rb=find(b);
            if(ra==rb) return;
            if(sz[ra] < sz[rb]) swap(ra,rb);
            parent[rb]=ra;
            sz[ra]+=sz[rb];
        }
        int size(int x){
            return sz[find(x)];
        }
    };
    
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        int m = grid.size(), n = grid[0].size();
        auto copy = grid;
        for (auto &h: hits) {
            int r=h[0], c=h[1];
            if (copy[r][c]==1) copy[r][c]=0; // apply hit
        }
        DSU dsu(m*n+1);
        int roof = m*n; // virtual node
        
        auto idx = [&](int r,int c){ return r*n + c; };
        const vector<int> dr{ -1, 1, 0, 0 };
        const vector<int> dc{ 0, 0, -1, 1 };
        
        // initial unions after all hits
        for(int r=0;r<m;++r){
            for(int c=0;c<n;++c){
                if(copy[r][c]==0) continue;
                int cur = idx(r,c);
                if(r==0) dsu.unite(cur, roof);
                for(int k=0;k<4;++k){
                    int nr=r+dr[k], nc=c+dc[k];
                    if(nr<0||nr>=m||nc<0||nc>=n) continue;
                    if(copy[nr][nc]==1){
                        dsu.unite(cur, idx(nr,nc));
                    }
                }
            }
        }
        
        vector<int> ans(hits.size());
        for(int i = (int)hits.size()-1; i>=0; --i){
            int r=hits[i][0], c=hits[i][1];
            if(grid[r][c]==0){ // no brick originally
                ans[i]=0;
                continue;
            }
            int preSize = dsu.size(roof);
            // add back the brick
            copy[r][c]=1;
            int curIdx = idx(r,c);
            if(r==0) dsu.unite(curIdx, roof);
            for(int k=0;k<4;++k){
                int nr=r+dr[k], nc=c+dc[k];
                if(nr<0||nr>=m||nc<0||nc>=n) continue;
                if(copy[nr][nc]==1){
                    dsu.unite(curIdx, idx(nr,nc));
                }
            }
            int postSize = dsu.size(roof);
            ans[i] = max(0, postSize - preSize - 1); // exclude the brick just added
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
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        void union(int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
        void setOne(int x) {
            size[x] = 1;
        }
        int getSize(int x) {
            return size[find(x)];
        }
    }

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int m = grid.length, n = grid[0].length;
        int total = m * n;
        int roof = total; // extra node
        DSU dsu = new DSU(total + 1);

        int[][] copy = new int[m][n];
        for (int i = 0; i < m; i++) {
            System.arraycopy(grid[i], 0, copy[i], 0, n);
        }
        // apply all hits
        for (int[] hit : hits) {
            int r = hit[0], c = hit[1];
            if (copy[r][c] == 1) copy[r][c] = 0;
        }

        // initialize DSU with remaining bricks
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (copy[i][j] != 1) continue;
                int idx = i * n + j;
                dsu.setOne(idx);
                if (i == 0) dsu.union(idx, roof);
                // up
                if (i > 0 && copy[i - 1][j] == 1) {
                    dsu.union(idx, (i - 1) * n + j);
                }
                // left
                if (j > 0 && copy[i][j - 1] == 1) {
                    dsu.union(idx, i * n + (j - 1));
                }
            }
        }

        int[] res = new int[hits.length];
        int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};
        for (int k = hits.length - 1; k >= 0; --k) {
            int r = hits[k][0], c = hits[k][1];
            if (grid[r][c] == 0) { // no brick originally
                res[k] = 0;
                continue;
            }
            int preRoofSize = dsu.getSize(roof);
            // add the brick back
            copy[r][c] = 1;
            int idx = r * n + c;
            dsu.setOne(idx);
            if (r == 0) dsu.union(idx, roof);
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (copy[nr][nc] == 1) {
                    dsu.union(idx, nr * n + nc);
                }
            }
            int postRoofSize = dsu.getSize(roof);
            int fallen = Math.max(0, postRoofSize - preRoofSize - 1);
            res[k] = fallen;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        size = m * n
        top = size  # virtual node index

        # DSU implementation
        parent = [i for i in range(size + 1)]
        sz = [1] * (size + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if sz[ra] < sz[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            sz[ra] += sz[rb]

        def getSize(x):
            return sz[find(x)]

        # copy grid and apply all hits (remove bricks)
        A = [row[:] for row in grid]
        for r, c in hits:
            if A[r][c] == 1:
                A[r][c] = 0

        # initial unions on the remaining bricks
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(m):
            for j in range(n):
                if A[i][j] != 1:
                    continue
                idx = i * n + j
                if i == 0:
                    union(idx, top)
                for dr, dc in ((1,0), (0,1)):
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 1:
                        union(idx, ni * n + nj)

        res = [0] * len(hits)
        # process hits in reverse
        for k in range(len(hits) - 1, -1, -1):
            r, c = hits[k]
            if grid[r][c] == 0:   # original cell was empty
                continue
            preRoof = getSize(top)

            idx = r * n + c
            A[r][c] = 1  # add brick back

            # connect to top if on first row
            if r == 0:
                union(idx, top)
            # connect with existing neighbours
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and A[nr][nc] == 1:
                    union(idx, nr * n + nc)

            postRoof = getSize(top)
            fallen = max(0, postRoof - preRoof - 1)
            res[k] = fallen

        return res
```

## Python3

```python
class Solution:
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])
        total = m * n
        top = total  # virtual node

        # copy grid and apply all hits
        A = [row[:] for row in grid]
        for x, y in hits:
            if A[x][y] == 1:
                A[x][y] = 0

        parent = list(range(total + 1))
        size = [1] * (total + 1)

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

        # initial unions on the grid after all hits
        for i in range(m):
            for j in range(n):
                if A[i][j] != 1:
                    continue
                idx = i * n + j
                if i == 0:
                    union(idx, top)
                for di, dj in ((1, 0), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 1:
                        nidx = ni * n + nj
                        union(idx, nidx)

        def top_size():
            return size[find(top)]

        prev_top = top_size()
        ans = []

        # process hits in reverse
        for x, y in reversed(hits):
            if grid[x][y] == 0:
                ans.append(0)
                continue

            idx = x * n + y
            A[x][y] = 1  # restore brick

            # union with existing neighbors
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + di, y + dj
                if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 1:
                    union(idx, nx * n + ny)

            if x == 0:
                union(idx, top)

            new_top = top_size()
            fallen = max(0, new_top - prev_top - 1)
            ans.append(fallen)
            prev_top = new_top

        return ans[::-1]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *parent;
    int *sz;
    int n;
} DSU;

static int find_set(DSU *d, int x) {
    while (d->parent[x] != x) {
        d->parent[x] = d->parent[d->parent[x]];
        x = d->parent[x];
    }
    return x;
}

static void union_set(DSU *d, int a, int b) {
    int ra = find_set(d, a);
    int rb = find_set(d, b);
    if (ra == rb) return;
    if (d->sz[ra] < d->sz[rb]) {
        int tmp = ra; ra = rb; rb = tmp;
    }
    d->parent[rb] = ra;
    d->sz[ra] += d->sz[rb];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* hitBricks(int** grid, int gridSize, int* gridColSize,
               int** hits, int hitsSize, int* hitsColSize,
               int* returnSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int total = m * n;
    int roof = total; // extra node

    // copy original grid and apply all hits (mark as 0)
    int *copy = (int *)malloc(total * sizeof(int));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            copy[i * n + j] = grid[i][j];
        }
    }

    // record which hits actually hit a brick
    int *originalBrick = (int *)malloc(total * sizeof(int));
    for (int i = 0; i < total; ++i) originalBrick[i] = grid[i / n][i % n];

    for (int k = 0; k < hitsSize; ++k) {
        int r = hits[k][0];
        int c = hits[k][1];
        int idx = r * n + c;
        if (copy[idx] == 1) copy[idx] = 0;
    }

    // initialize DSU
    DSU dsu;
    dsu.n = total + 1;
    dsu.parent = (int *)malloc(dsu.n * sizeof(int));
    dsu.sz = (int *)calloc(dsu.n, sizeof(int)); // zero-initialized

    for (int i = 0; i < dsu.n; ++i) dsu.parent[i] = i;

    // union existing bricks after all hits
    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    for (int r = 0; r < m; ++r) {
        for (int c = 0; c < n; ++c) {
            int idx = r * n + c;
            if (copy[idx] != 1) continue;
            dsu.sz[idx] = 1;
            if (r == 0) union_set(&dsu, idx, roof);
            // check four directions, but only union with already processed cells to avoid double work
            for (int dir = 0; dir < 4; ++dir) {
                int nr = r + dr[dir];
                int nc = c + dc[dir];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nidx = nr * n + nc;
                if (copy[nidx] == 1) {
                    union_set(&dsu, idx, nidx);
                }
            }
        }
    }

    // prepare result array
    int *res = (int *)malloc(hitsSize * sizeof(int));
    for (int i = hitsSize - 1; i >= 0; --i) {
        int r = hits[i][0];
        int c = hits[i][1];
        int idx = r * n + c;

        // if there was no brick originally, nothing falls
        if (originalBrick[idx] == 0) {
            res[i] = 0;
            continue;
        }

        // current roof size before adding back
        int prevRoofSize = dsu.sz[find_set(&dsu, roof)];

        // add the brick back
        copy[idx] = 1;
        dsu.sz[idx] = 1;          // make it a component of size 1
        dsu.parent[idx] = idx;    // reset parent (it may have been isolated)

        if (r == 0) union_set(&dsu, idx, roof);

        for (int dir = 0; dir < 4; ++dir) {
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            int nidx = nr * n + nc;
            if (copy[nidx] == 1) {
                union_set(&dsu, idx, nidx);
            }
        }

        int newRoofSize = dsu.sz[find_set(&dsu, roof)];
        int fallen = newRoofSize - prevRoofSize - 1; // exclude the brick we just added
        if (fallen < 0) fallen = 0;
        res[i] = fallen;
    }

    *returnSize = hitsSize;

    free(copy);
    free(originalBrick);
    free(dsu.parent);
    free(dsu.sz);

    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] HitBricks(int[][] grid, int[][] hits) {
        int m = grid.Length;
        int n = grid[0].Length;
        int total = m * n;
        int roof = total; // extra node representing the ceiling

        DSU dsu = new DSU(total + 1);
        int[][] copy = new int[m][];
        for (int i = 0; i < m; i++) {
            copy[i] = new int[n];
            Array.Copy(grid[i], copy[i], n);
        }

        // Apply all hits upfront
        foreach (var hit in hits) {
            int r = hit[0], c = hit[1];
            if (copy[r][c] == 1) copy[r][c] = 0;
        }

        // Initial unions after all removals
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (copy[i][j] != 1) continue;
                int id = i * n + j;
                if (i == 0) dsu.Union(id, roof);
                if (i > 0 && copy[i - 1][j] == 1) dsu.Union(id, (i - 1) * n + j);
                if (j > 0 && copy[i][j - 1] == 1) dsu.Union(id, i * n + (j - 1));
            }
        }

        int q = hits.Length;
        int[] res = new int[q];
        int[][] dirs = new int[][] {
            new int[]{-1,0}, new int[]{1,0},
            new int[]{0,-1}, new int[]{0,1}
        };

        // Process hits in reverse
        for (int k = q - 1; k >= 0; k--) {
            int r = hits[k][0], c = hits[k][1];
            if (grid[r][c] == 0) {
                res[k] = 0;
                continue;
            }

            int prevRoofSize = dsu.GetSize(roof);
            copy[r][c] = 1; // add brick back
            int id = r * n + c;

            if (r == 0) dsu.Union(id, roof);
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && copy[nr][nc] == 1) {
                    dsu.Union(id, nr * n + nc);
                }
            }

            int newRoofSize = dsu.GetSize(roof);
            int fallen = Math.Max(0, newRoofSize - prevRoofSize - 1);
            res[k] = fallen;
        }

        return res;
    }

    private class DSU {
        private readonly int[] parent;
        private readonly int[] size;

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
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }

        public int GetSize(int x) {
            return size[Find(x)];
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number[][]} hits
 * @return {number[]}
 */
var hitBricks = function(grid, hits) {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;
    const roof = total; // extra node
    
    // copy grid and apply all hits (remove bricks)
    const copy = new Array(m);
    for (let i = 0; i < m; ++i) {
        copy[i] = grid[i].slice();
    }
    for (const [x, y] of hits) {
        if (copy[x][y] === 1) copy[x][y] = 0;
    }
    
    // DSU structures
    const parent = new Int32Array(total + 1);
    const size = new Int32Array(total + 1);
    for (let i = 0; i <= total; ++i) {
        parent[i] = i;
        size[i] = (i === roof ? 0 : 1);
    }
    
    function find(x) {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    
    function union(a, b) {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        // attach smaller to larger
        if (size[ra] < size[rb]) {
            parent[ra] = rb;
            size[rb] += size[ra];
        } else {
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }
    
    // helper to convert (i,j) to index
    const idx = (i, j) => i * n + j;
    
    // initial unions on the grid after all hits
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (copy[i][j] !== 1) continue;
            const cur = idx(i, j);
            if (i === 0) union(cur, roof);
            // up
            if (i > 0 && copy[i - 1][j] === 1) union(cur, idx(i - 1, j));
            // left
            if (j > 0 && copy[i][j - 1] === 1) union(cur, idx(i, j - 1));
        }
    }
    
    const res = new Array(hits.length);
    const dirs = [[-1,0],[1,0],[0,-1],[0,1]];
    
    // process hits in reverse
    for (let k = hits.length - 1; k >= 0; --k) {
        const [x, y] = hits[k];
        if (grid[x][y] === 0) { // no brick originally
            res[k] = 0;
            continue;
        }
        const prevRoofSize = size[find(roof)];
        
        // add the brick back
        copy[x][y] = 1;
        const curIdx = idx(x, y);
        if (x === 0) union(curIdx, roof);
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (copy[nx][ny] === 1) union(curIdx, idx(nx, ny));
        }
        
        const newRoofSize = size[find(roof)];
        const fallen = Math.max(0, newRoofSize - prevRoofSize - 1);
        res[k] = fallen;
    }
    
    return res;
};
```

## Typescript

```typescript
function hitBricks(grid: number[][], hits: number[][]): number[] {
    const m = grid.length;
    const n = grid[0].length;
    const copy = grid.map(row => row.slice());

    // Apply all hits
    for (const [x, y] of hits) {
        if (copy[x][y] === 1) copy[x][y] = 0;
    }

    const total = m * n;
    const roof = total; // extra node representing the ceiling

    const parent = new Int32Array(total + 1);
    const size = new Int32Array(total + 1);
    for (let i = 0; i <= total; i++) {
        parent[i] = i;
        size[i] = i === roof ? 0 : 1; // bricks have size 1, roof starts with 0
    }

    const find = (x: number): number => {
        let cur = x;
        while (parent[cur] !== cur) {
            parent[cur] = parent[parent[cur]];
            cur = parent[cur];
        }
        return cur;
    };

    const union = (a: number, b: number): void => {
        let ra = find(a);
        let rb = find(b);
        if (ra === rb) return;
        // attach smaller to larger
        if (size[ra] < size[rb]) {
            const tmp = ra;
            ra = rb;
            rb = tmp;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
    };

    const idx = (r: number, c: number): number => r * n + c;

    // Initial unions on the grid after all hits
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (copy[r][c] !== 1) continue;
            const cur = idx(r, c);
            if (r === 0) union(cur, roof);
            if (r > 0 && copy[r - 1][c] === 1) union(cur, idx(r - 1, c));
            if (c > 0 && copy[r][c - 1] === 1) union(cur, idx(r, c - 1));
        }
    }

    const res = new Array<number>(hits.length);
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]] as const;

    // Process hits in reverse
    for (let i = hits.length - 1; i >= 0; i--) {
        const [r, c] = hits[i];
        if (grid[r][c] === 0) {
            res[i] = 0;
            continue;
        }

        const prevRoofSize = size[find(roof)];

        // Restore the brick
        copy[r][c] = 1;
        const cur = idx(r, c);
        if (r === 0) union(cur, roof);

        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && copy[nr][nc] === 1) {
                union(cur, idx(nr, nc));
            }
        }

        const newRoofSize = size[find(roof)];
        const fallen = Math.max(0, newRoofSize - prevRoofSize - 1);
        res[i] = fallen;
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer[][] $hits
     * @return Integer[]
     */
    function hitBricks($grid, $hits) {
        $m = count($grid);
        $n = count($grid[0]);
        $totalCells = $m * $n;
        // copy grid and apply all hits (remove bricks)
        $copy = [];
        for ($i = 0; $i < $m; $i++) {
            $copy[$i] = $grid[$i];
        }
        foreach ($hits as $h) {
            $r = $h[0];
            $c = $h[1];
            if ($copy[$r][$c] == 1) {
                $copy[$r][$c] = 0;
            }
        }

        // DSU initialization
        $roof = $totalCells;               // extra node representing the roof
        $size = $totalCells + 1;           // total nodes including roof
        $parent = array_fill(0, $size, 0);
        $sz = array_fill(0, $size, 0);
        for ($i = 0; $i < $size; $i++) {
            $parent[$i] = $i;
            $sz[$i] = ($i == $roof) ? 0 : 1;   // roof starts with size 0
        }

        // find with path compression
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] != $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        // union by size
        $union = function($a, $b) use (&$parent, &$sz, &$find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra == $rb) return;
            if ($sz[$ra] < $sz[$rb]) {
                $tmp = $ra; $ra = $rb; $rb = $tmp;
            }
            $parent[$rb] = $ra;
            $sz[$ra] += $sz[$rb];
        };

        // initial unions on the grid after all hits
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($copy[$i][$j] == 1) {
                    $idx = $i * $n + $j;
                    if ($i == 0) {
                        $union($idx, $roof);
                    }
                    // up
                    if ($i > 0 && $copy[$i - 1][$j] == 1) {
                        $union($idx, ($i - 1) * $n + $j);
                    }
                    // left
                    if ($j > 0 && $copy[$i][$j - 1] == 1) {
                        $union($idx, $i * $n + ($j - 1));
                    }
                }
            }
        }

        $res = array_fill(0, count($hits), 0);
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        // process hits in reverse order
        for ($k = count($hits) - 1; $k >= 0; $k--) {
            $r = $hits[$k][0];
            $c = $hits[$k][1];

            if ($grid[$r][$c] == 0) {          // original cell had no brick
                $res[$k] = 0;
                continue;
            }

            // size of roof component before adding the brick back
            $roofRoot = $find($roof);
            $prevSize = $sz[$roofRoot];

            // add brick back
            $copy[$r][$c] = 1;
            $idx = $r * $n + $c;

            if ($r == 0) {
                $union($idx, $roof);
            }
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $copy[$nr][$nc] == 1) {
                    $union($idx, $nr * $n + $nc);
                }
            }

            // size after unions
            $roofRoot = $find($roof);
            $newSize = $sz[$roofRoot];
            $fallen = $newSize - $prevSize - 1;   // exclude the brick we just added
            if ($fallen < 0) $fallen = 0;
            $res[$k] = $fallen;
        }

        return $res;
    }
}
```

## Swift

```swift
class DSU {
    var parent: [Int]
    var size: [Int]

    init(_ n: Int) {
        parent = Array(0..<n)
        size = Array(repeating: 1, count: n)
    }

    func find(_ x: Int) -> Int {
        var x = x
        while parent[x] != x {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
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
    func hitBricks(_ grid: [[Int]], _ hits: [[Int]]) -> [Int] {
        let m = grid.count
        let n = grid[0].count
        var copy = grid.map { $0 }   // mutable copy after all hits

        for hit in hits {
            let r = hit[0], c = hit[1]
            if copy[r][c] == 1 {
                copy[r][c] = 0
            }
        }

        let total = m * n
        let roof = total               // extra node representing the top
        let dsu = DSU(total + 1)
        dsu.size[roof] = 0             // roof itself doesn't count as a brick

        func index(_ r: Int, _ c: Int) -> Int {
            return r * n + c
        }

        // initial unions on the grid after all hits
        for i in 0..<m {
            for j in 0..<n {
                if copy[i][j] == 1 {
                    let idx = index(i, j)
                    if i == 0 {
                        dsu.union(idx, roof)
                    }
                    // up
                    if i > 0 && copy[i - 1][j] == 1 {
                        dsu.union(idx, index(i - 1, j))
                    }
                    // left
                    if j > 0 && copy[i][j - 1] == 1 {
                        dsu.union(idx, index(i, j - 1))
                    }
                }
            }
        }

        var result = Array(repeating: 0, count: hits.count)
        let dr = [-1, 1, 0, 0]
        let dc = [0, 0, -1, 1]

        for k in stride(from: hits.count - 1, through: 0, by: -1) {
            let r = hits[k][0], c = hits[k][1]
            if grid[r][c] == 0 {   // original cell had no brick
                result[k] = 0
                continue
            }

            let preSize = dsu.getSize(roof)

            // add the brick back
            copy[r][c] = 1
            let idx = index(r, c)

            if r == 0 {
                dsu.union(idx, roof)
            }
            for dir in 0..<4 {
                let nr = r + dr[dir]
                let nc = c + dc[dir]
                if nr >= 0 && nr < m && nc >= 0 && nc < n && copy[nr][nc] == 1 {
                    dsu.union(idx, index(nr, nc))
                }
            }

            let postSize = dsu.getSize(roof)
            var fallen = postSize - preSize - 1
            if fallen < 0 { fallen = 0 }
            result[k] = fallen
        }

        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class DSU(n: Int) {
        private val parent = IntArray(n) { it }
        private val size = IntArray(n) { 1 }

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var x = find(a)
            var y = find(b)
            if (x == y) return
            if (size[x] < size[y]) {
                val tmp = x
                x = y
                y = tmp
            }
            parent[y] = x
            size[x] += size[y]
        }

        fun componentSize(x: Int): Int = size[find(x)]
    }

    fun hitBricks(grid: Array<IntArray>, hits: Array<IntArray>): IntArray {
        val m = grid.size
        val n = grid[0].size
        val copy = Array(m) { IntArray(n) }
        for (i in 0 until m) {
            System.arraycopy(grid[i], 0, copy[i], 0, n)
        }

        // Apply all hits
        for (hit in hits) {
            val r = hit[0]
            val c = hit[1]
            if (copy[r][c] == 1) copy[r][c] = 0
        }

        val total = m * n
        val roof = total // extra node representing the top
        val dsu = DSU(total + 1)

        // Initial unions after all hits
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (copy[i][j] == 1) {
                    val idx = i * n + j
                    if (i == 0) dsu.union(idx, roof)
                    if (i > 0 && copy[i - 1][j] == 1) dsu.union(idx, (i - 1) * n + j)
                    if (j > 0 && copy[i][j - 1] == 1) dsu.union(idx, i * n + (j - 1))
                }
            }
        }

        val res = IntArray(hits.size)
        val dr = intArrayOf(-1, 1, 0, 0)
        val dc = intArrayOf(0, 0, -1, 1)

        for (k in hits.indices.reversed()) {
            val r = hits[k][0]
            val c = hits[k][1]

            // If there was no brick originally, nothing falls
            if (grid[r][c] == 0) {
                res[k] = 0
                continue
            }

            val before = dsu.componentSize(roof)

            // Add the brick back
            copy[r][c] = 1
            val idx = r * n + c

            if (r == 0) dsu.union(idx, roof)

            for (d in 0..3) {
                val nr = r + dr[d]
                val nc = c + dc[d]
                if (nr in 0 until m && nc in 0 until n && copy[nr][nc] == 1) {
                    dsu.union(idx, nr * n + nc)
                }
            }

            val after = dsu.componentSize(roof)
            var added = after - before - 1
            if (added < 0) added = 0
            res[k] = added
        }

        return res
    }
}
```

## Dart

```dart
class DSU {
  List<int> parent;
  List<int> size;

  DSU(int n) {
    parent = List.generate(n, (i) => i);
    size = List.filled(n, 1);
  }

  int find(int x) {
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
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
  List<int> hitBricks(List<List<int>> grid, List<List<int>> hits) {
    final m = grid.length;
    final n = grid[0].length;
    // copy original grid
    final cur = List.generate(m, (i) => List.from(grid[i]));
    // apply all hits
    for (var hit in hits) {
      int r = hit[0], c = hit[1];
      if (cur[r][c] == 1) cur[r][c] = 0;
    }

    final total = m * n;
    final roof = total; // extra node
    final dsu = DSU(total + 1);

    // initial unions after all hits
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (cur[i][j] != 1) continue;
        int idx = i * n + j;
        if (i == 0) dsu.union(idx, roof);
        // up
        if (i > 0 && cur[i - 1][j] == 1) {
          dsu.union(idx, (i - 1) * n + j);
        }
        // left
        if (j > 0 && cur[i][j - 1] == 1) {
          dsu.union(idx, i * n + (j - 1));
        }
      }
    }

    final ans = List<int>.filled(hits.length, 0);
    for (int k = hits.length - 1; k >= 0; --k) {
      int r = hits[k][0];
      int c = hits[k][1];
      if (grid[r][c] == 0) {
        ans[k] = 0;
        continue;
      }
      int preSize = dsu.getSize(roof);
      // add brick back
      cur[r][c] = 1;
      int idx = r * n + c;
      if (r == 0) dsu.union(idx, roof);
      const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
      ];
      for (var d in dirs) {
        int nr = r + d[0];
        int nc = c + d[1];
        if (nr < 0 ||
            nr >= m ||
            nc < 0 ||
            nc >= n ||
            cur[nr][nc] != 1) continue;
        dsu.union(idx, nr * n + nc);
      }
      int postSize = dsu.getSize(roof);
      ans[k] = postSize - preSize - 1;
      if (ans[k] < 0) ans[k] = 0;
    }

    return ans;
  }
}
```

## Golang

```go
type dsu struct {
	parent []int
	size   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	sz := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
		sz[i] = 1
	}
	return &dsu{parent: p, size: sz}
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

func (d *dsu) compSize(x int) int {
	return d.size[d.find(x)]
}

func hitBricks(grid [][]int, hits [][]int) []int {
	m := len(grid)
	n := len(grid[0])
	// copy grid and apply all hits
	copyGrid := make([][]int, m)
	for i := 0; i < m; i++ {
		copyGrid[i] = make([]int, n)
		copy(copyGrid[i], grid[i])
	}
	for _, h := range hits {
		r, c := h[0], h[1]
		if copyGrid[r][c] == 1 {
			copyGrid[r][c] = 0
		}
	}

	total := m * n
	virtualTop := total
	ds := newDSU(total + 1)

	id := func(i, j int) int { return i*n + j }

	// initial unions for remaining bricks
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if copyGrid[i][j] != 1 {
				continue
			}
			cur := id(i, j)
			if i == 0 {
				ds.union(cur, virtualTop)
			}
			// up and left to avoid double work
			if i > 0 && copyGrid[i-1][j] == 1 {
				ds.union(cur, id(i-1, j))
			}
			if j > 0 && copyGrid[i][j-1] == 1 {
				ds.union(cur, id(i, j-1))
			}
		}
	}

	ans := make([]int, len(hits))

	for k := len(hits) - 1; k >= 0; k-- {
		r, c := hits[k][0], hits[k][1]
		if grid[r][c] == 0 { // no brick originally
			ans[k] = 0
			continue
		}
		prevTopSize := ds.compSize(virtualTop)

		// add the brick back
		copyGrid[r][c] = 1
		cur := id(r, c)
		if r == 0 {
			ds.union(cur, virtualTop)
		}
		dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && copyGrid[nr][nc] == 1 {
				ds.union(cur, id(nr, nc))
			}
		}

		newTopSize := ds.compSize(virtualTop)
		fallen := newTopSize - prevTopSize
		if fallen > 0 {
			fallen-- // exclude the brick we just added
		} else {
			fallen = 0
		}
		ans[k] = fallen
	}

	return ans
}
```

## Ruby

```ruby
class DSU
  attr_accessor :parent, :size

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
    return if ra == rb
    if @size[ra] < @size[rb]
      ra, rb = rb, ra
    end
    @parent[rb] = ra
    @size[ra] += @size[rb]
  end
end

# @param {Integer[][]} grid
# @param {Integer[][]} hits
# @return {Integer[]}
def hit_bricks(grid, hits)
  m = grid.length
  n = grid[0].length
  total = m * n
  roof = total

  dsu = DSU.new(total + 1)
  dsu.size[roof] = 0

  # copy grid and apply all hits
  cur = grid.map(&:dup)
  hits.each do |r, c|
    cur[r][c] = 0 if cur[r][c] == 1
  end

  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

  # initial unions for remaining bricks
  (0...m).each do |i|
    (0...n).each do |j|
      next if cur[i][j] == 0
      idx = i * n + j
      dsu.union(idx, roof) if i == 0
      dirs.each do |dx, dy|
        ni = i + dx
        nj = j + dy
        next unless ni.between?(0, m - 1) && nj.between?(0, n - 1)
        next if cur[ni][nj] == 0
        nidx = ni * n + nj
        dsu.union(idx, nidx)
      end
    end
  end

  res = Array.new(hits.length, 0)

  (hits.length - 1).downto(0) do |k|
    r, c = hits[k]
    # if there was no brick originally, nothing falls
    next if grid[r][c] == 0

    prev_roof = dsu.size[dsu.find(roof)]

    # add the brick back
    cur[r][c] = 1
    idx = r * n + c
    dsu.union(idx, roof) if r == 0
    dirs.each do |dx, dy|
      ni = r + dx
      nj = c + dy
      next unless ni.between?(0, m - 1) && nj.between?(0, n - 1)
      next if cur[ni][nj] == 0
      nidx = ni * n + nj
      dsu.union(idx, nidx)
    end

    new_roof = dsu.size[dsu.find(roof)]
    fallen = new_roof - prev_roof - 1
    res[k] = fallen > 0 ? fallen : 0
  end

  res
end
```

## Scala

```scala
object Solution {
  def hitBricks(grid: Array[Array[Int]], hits: Array[Array[Int]]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val total = m * n
    val roof = total // extra node index

    // copy of grid after all hits applied
    val cur = Array.ofDim[Int](m, n)
    for (i <- 0 until m) {
      System.arraycopy(grid(i), 0, cur(i), 0, n)
    }
    for (h <- hits) {
      val r = h(0)
      val c = h(1)
      if (cur(r)(c) == 1) cur(r)(c) = 0
    }

    // DSU structure
    class DSU(val sz: Int) {
      val parent: Array[Int] = Array.tabulate(sz)(i => i)
      val size: Array[Int] = Array.fill(sz)(1)

      def find(x: Int): Int = {
        var p = x
        while (parent(p) != p) {
          parent(p) = parent(parent(p))
          p = parent(p)
        }
        p
      }

      def union(a: Int, b: Int): Unit = {
        var x = find(a)
        var y = find(b)
        if (x == y) return
        if (size(x) < size(y)) { val t = x; x = y; y = t }
        parent(y) = x
        size(x) += size(y)
      }

      def componentSize(x: Int): Int = size(find(x))
    }

    val dsu = new DSU(total + 1)

    // helper to convert (r,c) to index
    def idx(r: Int, c: Int): Int = r * n + c

    // initial unions on the grid after all hits
    for (i <- 0 until m; j <- 0 until n if cur(i)(j) == 1) {
      val id = idx(i, j)
      if (i == 0) dsu.union(id, roof)
      if (i > 0 && cur(i - 1)(j) == 1) dsu.union(id, idx(i - 1, j))
      if (j > 0 && cur(i)(j - 1) == 1) dsu.union(id, idx(i, j - 1))
    }

    val res = new Array[Int](hits.length)

    // process hits in reverse
    for (k <- hits.indices.reverse) {
      val r = hits(k)(0)
      val c = hits(k)(1)
      if (grid(r)(c) == 0) {
        res(k) = 0
      } else {
        val prevRoofSize = dsu.componentSize(roof) - 1 // exclude roof node

        // add brick back
        cur(r)(c) = 1
        val id = idx(r, c)
        if (r == 0) dsu.union(id, roof)

        // union with existing neighbors
        val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))
        for ((dr, dc) <- dirs) {
          val nr = r + dr
          val nc = c + dc
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && cur(nr)(nc) == 1) {
            dsu.union(id, idx(nr, nc))
          }
        }

        val newRoofSize = dsu.componentSize(roof) - 1
        var fallen = newRoofSize - prevRoofSize
        if (fallen < 0) fallen = 0
        res(k) = fallen
      }
    }

    res
  }
}
```

## Rust

```rust
use std::cmp::max;

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let parent = (0..n).collect();
        let size = vec![1; n];
        DSU { parent, size }
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
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }

    fn component_size(&mut self, x: usize) -> usize {
        let root = self.find(x);
        self.size[root]
    }
}

impl Solution {
    pub fn hit_bricks(grid: Vec<Vec<i32>>, hits: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len();
        let total = m * n;
        let top = total; // virtual node

        // copy of original grid to check existence of bricks
        let orig_grid = grid.clone();

        // apply all hits to a mutable copy
        let mut cur_grid = grid.clone();
        for h in &hits {
            let r = h[0] as usize;
            let c = h[1] as usize;
            if cur_grid[r][c] == 1 {
                cur_grid[r][c] = 0;
            }
        }

        // initialize DSU with current grid state
        let mut dsu = DSU::new(total + 1);
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];

        for i in 0..m {
            for j in 0..n {
                if cur_grid[i][j] != 1 {
                    continue;
                }
                let idx = i * n + j;
                if i == 0 {
                    dsu.union(idx, top);
                }
                for (dr, dc) in &dirs {
                    let ni = i as i32 + dr;
                    let nj = j as i32 + dc;
                    if ni >= 0 && ni < m as i32 && nj >= 0 && nj < n as i32 {
                        let ui = ni as usize;
                        let uj = nj as usize;
                        if cur_grid[ui][uj] == 1 {
                            dsu.union(idx, ui * n + uj);
                        }
                    }
                }
            }
        }

        // process hits in reverse
        let mut result_rev: Vec<i32> = Vec::with_capacity(hits.len());
        for h in hits.iter().rev() {
            let r = h[0] as usize;
            let c = h[1] as usize;

            if orig_grid[r][c] == 0 {
                // no brick originally
                result_rev.push(0);
                continue;
            }

            let before = dsu.component_size(top);

            // add the brick back
            cur_grid[r][c] = 1;
            let idx = r * n + c;

            if r == 0 {
                dsu.union(idx, top);
            }
            for (dr, dc) in &dirs {
                let ni = r as i32 + dr;
                let nj = c as i32 + dc;
                if ni >= 0 && ni < m as i32 && nj >= 0 && nj < n as i32 {
                    let ui = ni as usize;
                    let uj = nj as usize;
                    if cur_grid[ui][uj] == 1 {
                        dsu.union(idx, ui * n + uj);
                    }
                }
            }

            let after = dsu.component_size(top);
            let fallen = if after > before { (after - before - 1) as i32 } else { 0 };
            result_rev.push(fallen);
        }

        result_rev.reverse();
        result_rev
    }
}
```

## Racket

```racket
(define/contract (hit-bricks grid hits)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (car grid))))
         (N (* m n))
         (top N)
         ;; flatten original grid
         (orig (let ((vec (make-vector N 0)))
                 (for ([r (in-range m)])
                   (for ([c (in-range n)])
                     (vector-set! vec (+ (* r n) c) (list-ref (list-ref grid r) c))))
                 vec))
         ;; mutable copy after all hits
         (g (make-vector N 0))
         ;; record whether each hit actually removed a brick
         (hit-count (length hits))
         (has-brick (make-vector hit-count #f))
         (hit-vec (list->vector hits)))
    ;; initialize g with original values
    (for ([i (in-range N)]) (vector-set! g i (vector-ref orig i)))
    ;; apply all hits
    (for ([i (in-range hit-count)])
      (let* ((pair (vector-ref hit-vec i))
             (r (car pair))
             (c (cadr pair))
             (idx (+ (* r n) c)))
        (when (= (vector-ref orig idx) 1)
          (vector-set! has-brick i #t)
          (vector-set! g idx 0))))
    ;; DSU structures
    (define parent (make-vector (+ N 1) 0))
    (define size   (make-vector (+ N 1) 1))
    (for ([i (in-range (+ N 1))]) (vector-set! parent i i))
    (define (find x)
      (let loop ((x x))
        (let ((p (vector-ref parent x)))
          (if (= p x)
              x
              (let ((root (loop p)))
                (vector-set! parent x root)
                root)))))
    (define (union a b)
      (let* ((ra (find a)) (rb (find b)))
        (when (not (= ra rb))
          (let ((sa (vector-ref size ra))
                (sb (vector-ref size rb)))
            (if (> sa sb)
                (begin
                  (vector-set! parent rb ra)
                  (vector-set! size ra (+ sa sb)))
                (begin
                  (vector-set! parent ra rb)
                  (vector-set! size rb (+ sa sb))))))))
    ;; helper to get current top component size
    (define (top-size) (vector-ref size (find top)))
    ;; build initial unions from grid after all hits
    (for ([r (in-range m)])
      (for ([c (in-range n)])
        (let ((idx (+ (* r n) c)))
          (when (= (vector-ref g idx) 1)
            (when (= r 0) (union idx top))
            (when (> r 0)
              (let ((up-idx (- idx n)))
                (when (= (vector-ref g up-idx) 1) (union idx up-idx))))
            (when (> c 0)
              (let ((left-idx (sub1 idx)))
                (when (= (vector-ref g left-idx) 1) (union idx left-idx))))))))
    ;; process hits in reverse
    (define res (make-vector hit-count 0))
    (for ([k (in-range (- hit-count 1) -1 -1)])
      (let* ((pair (vector-ref hit-vec k))
             (r (car pair))
             (c (cadr pair))
             (idx (+ (* r n) c)))
        (if (not (vector-ref has-brick k))
            (vector-set! res k 0)
            (begin
              (define size-before (top-size))
              ;; restore brick
              (vector-set! g idx 1)
              (when (= r 0) (union idx top))
              (for ([dr (in-list '(-1 1 0 0))]
                    [dc (in-list '(0 0 -1 1))])
                (let ((nr (+ r dr))
                      (nc (+ c dc)))
                  (when (and (>= nr 0) (< nr m) (>= nc 0) (< nc n))
                    (let ((nidx (+ (* nr n) nc)))
                      (when (= (vector-ref g nidx) 1)
                        (union idx nidx))))))
              (define size-after (top-size))
              (define fallen (- size-after size-before 1))
              (when (< fallen 0) (set! fallen 0))
              (vector-set! res k fallen)))))
    (vector->list res)))
```

## Erlang

```erlang
-export([hit_bricks/2]).

-spec hit_bricks(Grid :: [[integer()]], Hits :: [[integer()]]) -> [integer()].
hit_bricks(Grid, Hits) ->
    M = length(Grid),
    N = length(hd(Grid)),
    Roof = M * N,
    % original bricks set
    OrigIdxs = [
        (R * N + C)
     || {Row, R} <- lists:zip(Grid, lists:seq(0, M - 1)),
        {Val, C} <- lists:zip(Row, lists:seq(0, N - 1)),
        Val == 1
    ],
    OrigSet = maps:from_list([{Idx, true} || Idx <- OrigIdxs]),
    % hits map for quick removal
    HitsMap = maps:from_list(
        [{R * N + C, true}
         || [R, C] <- Hits]
    ),
    % present bricks after all hits
    Present0 = maps:filter(fun(Idx, _) -> not maps:is_key(Idx, HitsMap) end, OrigSet),

    ParentTab = ets:new(parent_tab, [set, private]),
    SizeTab   = ets:new(size_tab,   [set, private]),

    % insert roof node
    ets:insert(ParentTab, {Roof, Roof}),
    ets:insert(SizeTab,   {Roof, 0}),

    % insert present bricks as separate sets
    maps:fold(fun(Idx, _, _) ->
        ets:insert(ParentTab, {Idx, Idx}),
        ets:insert(SizeTab,   {Idx, 1})
    end, ok, Present0),

    % union initial connections (up and left) and top row with roof
    lists:foreach(
        fun(Idx) ->
            R = Idx div N,
            C = Idx rem N,
            if R == 0 -> union(Idx, Roof, ParentTab, SizeTab); true -> ok end,
            % up neighbor
            case R > 0 of
                true ->
                    UpIdx = (R - 1) * N + C,
                    case maps:is_key(UpIdx, Present0) of
                        true -> union(Idx, UpIdx, ParentTab, SizeTab);
                        false -> ok
                    end;
                false -> ok
            end,
            % left neighbor
            case C > 0 of
                true ->
                    LeftIdx = R * N + (C - 1),
                    case maps:is_key(LeftIdx, Present0) of
                        true -> union(Idx, LeftIdx, ParentTab, SizeTab);
                        false -> ok
                    end;
                false -> ok
            end
        end,
        maps:keys(Present0)
    ),

    % process hits in reverse order
    HitsRev = lists:reverse(Hits),
    {AnsRev, _FinalPres} =
        lists:foldl(
            fun([R, C], {Acc, Pres}) ->
                Idx = R * N + C,
                case maps:is_key(Idx, OrigSet) of
                    false ->
                        {[0 | Acc], Pres};
                    true ->
                        OldSize = root_size(Roof, ParentTab, SizeTab),
                        % add brick back
                        ets:insert(ParentTab, {Idx, Idx}),
                        ets:insert(SizeTab,   {Idx, 1}),
                        NewPres = maps:put(Idx, true, Pres),

                        if R == 0 -> union(Idx, Roof, ParentTab, SizeTab); true -> ok end,

                        NeighborOffsets = [{-1,0},{1,0},{0,-1},{0,1}],
                        lists:foreach(
                            fun({DR, DC}) ->
                                NR = R + DR,
                                NC = C + DC,
                                if NR >= 0, NR < M, NC >= 0, NC < N ->
                                        NIdx = NR * N + NC,
                                        case maps:is_key(NIdx, NewPres) of
                                            true -> union(Idx, NIdx, ParentTab, SizeTab);
                                            false -> ok
                                        end;
                                   true -> ok
                                end
                            end,
                            NeighborOffsets),

                        NewSize = root_size(Roof, ParentTab, SizeTab),
                        Diff = NewSize - OldSize,
                        Fallen = if Diff > 0 -> Diff - 1; true -> 0 end,
                        {[Fallen | Acc], NewPres}
                end
            end,
            {[], Present0},
            HitsRev),

    lists:reverse(AnsRev).

%% Union-Find helpers

find(X, ParentTab) ->
    case ets:lookup(ParentTab, X) of
        [{X, P}] when X =:= P -> X;
        [{X, P}] ->
            Root = find(P, ParentTab),
            ets:insert(ParentTab, {X, Root}),
            Root
    end.

root_size(RootIdx, ParentTab, SizeTab) ->
    R = find(RootIdx, ParentTab),
    case ets:lookup(SizeTab, R) of
        [{R, Sz}] -> Sz;
        [] -> 0
    end.

union(A, B, ParentTab, SizeTab) ->
    RA = find(A, ParentTab),
    RB = find(B, ParentTab),
    if RA =:= RB -> ok;
       true ->
           SA = case ets:lookup(SizeTab, RA) of [{RA, S}] -> S; [] -> 0 end,
           SB = case ets:lookup(SizeTab, RB) of [{RB, S}] -> S; [] -> 0 end,
           if SA < SB ->
                   ets:insert(ParentTab, {RA, RB}),
                   ets:insert(SizeTab,   {RB, SA + SB});
              true ->
                   ets:insert(ParentTab, {RB, RA}),
                   ets:insert(SizeTab,   {RA, SA + SB})
           end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec hit_bricks(grid :: [[integer]], hits :: [[integer]]) :: [integer]
  def hit_bricks(grid, hits) do
    m = length(grid)
    n = grid |> hd() |> length()
    total = m * n
    roof = total

    parent_tab = :ets.new(:parent, [:set, :private])
    size_tab = :ets.new(:size, [:set, :private])
    present_tab = :ets.new(:present, [:set, :private])

    # initialize DSU nodes
    Enum.each(0..total, fn i ->
      :ets.insert(parent_tab, {i, i})
      sz = if i == roof, do: 0, else: 1
      :ets.insert(size_tab, {i, sz})
    end)

    # fill present with original bricks
    Enum.each(0..(m - 1), fn r ->
      row = Enum.at(grid, r)
      Enum.each(0..(n - 1), fn c ->
        if Enum.at(row, c) == 1 do
          idx = r * n + c
          :ets.insert(present_tab, {idx, 1})
        end
      end)
    end)

    # apply hits: remove bricks that exist originally
    Enum.each(hits, fn [r, c] ->
      if Enum.at(Enum.at(grid, r), c) == 1 do
        idx = r * n + c
        :ets.delete(present_tab, idx)
      end
    end)

    # union initial present bricks
    Enum.each(0..(m - 1), fn r ->
      Enum.each(0..(n - 1), fn c ->
        idx = r * n + c

        if present?(present_tab, idx) do
          if r == 0, do: union_to_root(parent_tab, size_tab, idx, roof)

          # right neighbor
          if c + 1 < n do
            nb = r * n + (c + 1)

            if present?(present_tab, nb) do
              union(parent_tab, size_tab, idx, nb)
            end
          end

          # down neighbor
          if r + 1 < m do
            nb = (r + 1) * n + c

            if present?(present_tab, nb) do
              union(parent_tab, size_tab, idx, nb)
            end
          end
        end
      end)
    end)

    # process hits in reverse order
    Enum.reduce(Enum.reverse(hits), [], fn [r, c], acc ->
      if Enum.at(Enum.at(grid, r), c) == 0 do
        [0 | acc]
      else
        idx = r * n + c
        pre_size = component_size(parent_tab, size_tab, roof)

        # add brick back
        :ets.insert(present_tab, {idx, 1})

        if r == 0, do: union_to_root(parent_tab, size_tab, idx, roof)

        dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

        Enum.each(dirs, fn {dr, dc} ->
          nr = r + dr
          nc = c + dc

          if nr >= 0 and nr < m and nc >= 0 and nc < n do
            nb_idx = nr * n + nc

            if present?(present_tab, nb_idx) do
              union(parent_tab, size_tab, idx, nb_idx)
            end
          end
        end)

        post_size = component_size(parent_tab, size_tab, roof)
        fallen = max(post_size - pre_size - 1, 0)
        [fallen | acc]
      end
    end)
  end

  # ----- DSU helper functions -----
  defp present?(tab, idx) do
    case :ets.lookup(tab, idx) do
      [] -> false
      _ -> true
    end
  end

  defp find(parent_tab, x) do
    [{^x, p}] = :ets.lookup(parent_tab, x)

    if p == x do
      x
    else
      root = find(parent_tab, p)
      :ets.insert(parent_tab, {x, root})
      root
    end
  end

  defp get_size(size_tab, root) do
    [{^root, sz}] = :ets.lookup(size_tab, root)
    sz
  end

  defp union(parent_tab, size_tab, a, b) do
    ra = find(parent_tab, a)
    rb = find(parent_tab, b)

    if ra != rb do
      sa = get_size(size_tab, ra)
      sb = get_size(size_tab, rb)

      if sa < sb do
        :ets.insert(parent_tab, {ra, rb})
        :ets.insert(size_tab, {rb, sa + sb})
      else
        :ets.insert(parent_tab, {rb, ra})
        :ets.insert(size_tab, {ra, sa + sb})
      end
    end
  end

  defp union_to_root(parent_tab, size_tab, a, roof) do
    ra = find(parent_tab, a)
    rb = find(parent_tab, roof)

    if ra != rb do
      sa = get_size(size_tab, ra)
      sb = get_size(size_tab, rb)
      :ets.insert(parent_tab, {ra, rb})
      :ets.insert(size_tab, {rb, sa + sb})
    end
  end

  defp component_size(parent_tab, size_tab, node) do
    root = find(parent_tab, node)
    get_size(size_tab, root)
  end
end
```

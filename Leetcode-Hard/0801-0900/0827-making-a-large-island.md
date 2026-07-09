# 0827. Making A Large Island

## Cpp

```cpp
class Solution {
public:
    int largestIsland(std::vector<std::vector<int>>& grid) {
        int n = grid.size();
        if (n == 0) return 0;
        std::vector<int> area(n * n + 2, 0);
        int id = 2; // start labeling islands from 2
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        
        // Label each island with a unique id and compute its area
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    int cnt = 0;
                    std::queue<std::pair<int,int>> q;
                    q.emplace(i, j);
                    grid[i][j] = id;
                    while (!q.empty()) {
                        auto [r, c] = q.front(); q.pop();
                        ++cnt;
                        for (auto &d : dirs) {
                            int nr = r + d[0], nc = c + d[1];
                            if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                                grid[nr][nc] = id;
                                q.emplace(nr, nc);
                            }
                        }
                    }
                    area[id] = cnt;
                    ++id;
                }
            }
        }
        
        int maxArea = 0;
        bool hasZero = false;
        // Try flipping each zero and compute potential island size
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0) {
                    hasZero = true;
                    std::unordered_set<int> seen;
                    int cur = 1; // the flipped cell itself
                    for (auto &d : dirs) {
                        int ni = i + d[0], nj = j + d[1];
                        if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                            int nid = grid[ni][nj];
                            if (nid > 1 && seen.insert(nid).second) {
                                cur += area[nid];
                            }
                        }
                    }
                    maxArea = std::max(maxArea, cur);
                }
            }
        }
        
        if (!hasZero) return n * n; // grid already full of ones
        
        int existingMax = 0;
        for (int k = 2; k < id; ++k) {
            existingMax = std::max(existingMax, area[k]);
        }
        return std::max(maxArea, existingMax);
    }
};
```

## Java

```java
class Solution {
    public int largestIsland(int[][] grid) {
        int n = grid.length;
        int total = n * n;
        int[] parent = new int[total];
        int[] size = new int[total];

        // Initialize Union-Find structures
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int id = i * n + j;
                parent[id] = id;
                if (grid[i][j] == 1) {
                    size[id] = 1;
                }
            }
        }

        // Union adjacent lands
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != 1) continue;
                int id = i * n + j;
                // right neighbor
                if (j + 1 < n && grid[i][j + 1] == 1) {
                    union(id, i * n + (j + 1), parent, size);
                }
                // down neighbor
                if (i + 1 < n && grid[i + 1][j] == 1) {
                    union(id, (i + 1) * n + j, parent, size);
                }
            }
        }

        boolean hasZero = false;
        int maxIsland = 0;

        // Find current maximum island size and check for zeros
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0) {
                    hasZero = true;
                } else {
                    int root = find(i * n + j, parent);
                    maxIsland = Math.max(maxIsland, size[root]);
                }
            }
        }

        // If there is no zero, whole grid is land
        if (!hasZero) return n * n;

        int answer = maxIsland;
        int[] dirs = {-1, 0, 1, 0, -1};

        // Evaluate each zero cell
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != 0) continue;
                int sum = 1;
                int[] neighborRoots = new int[4];
                int cnt = 0;

                for (int d = 0; d < 4; ++d) {
                    int ni = i + dirs[d];
                    int nj = j + dirs[d + 1];
                    if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;
                    if (grid[ni][nj] != 1) continue;
                    int root = find(ni * n + nj, parent);
                    boolean duplicate = false;
                    for (int k = 0; k < cnt; ++k) {
                        if (neighborRoots[k] == root) {
                            duplicate = true;
                            break;
                        }
                    }
                    if (!duplicate) {
                        sum += size[root];
                        neighborRoots[cnt++] = root;
                    }
                }
                answer = Math.max(answer, sum);
            }
        }

        return answer;
    }

    private int find(int x, int[] parent) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int a, int b, int[] parent, int[] size) {
        int ra = find(a, parent);
        int rb = find(b, parent);
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
```

## Python

```python
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island_id = 2  # start labeling from 2 to distinguish from 0 and 1
        sizes = {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                stack = [(i, j)]
                grid[i][j] = island_id
                area = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = island_id
                            stack.append((nx, ny))
                sizes[island_id] = area
                island_id += 1

        max_area = max(sizes.values()) if sizes else 0
        has_zero = False

        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                has_zero = True
                neighbor_ids = set()
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                        neighbor_ids.add(grid[ni][nj])
                combined = 1  # the flipped cell itself
                for nid in neighbor_ids:
                    combined += sizes[nid]
                max_area = max(max_area, combined)

        if not has_zero:
            return n * n
        return max_area
```

## Python3

```python
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = [i for i in range(n * n)]
        size = [0] * (n * n)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Initialize sizes for land cells
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    idx = i * n + j
                    size[idx] = 1

        # Union adjacent lands (right and down to avoid duplicates)
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                idx = i * n + j
                if i + 1 < n and grid[i + 1][j] == 1:
                    union(idx, (i + 1) * n + j)
                if j + 1 < n and grid[i][j + 1] == 1:
                    union(idx, i * n + (j + 1))

        # Current maximum island size without any flip
        max_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    root = find(i * n + j)
                    max_island = max(max_island, size[root])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        has_zero = False

        # Try flipping each zero
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    has_zero = True
                    neighbor_roots = set()
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            neighbor_roots.add(find(ni * n + nj))
                    total = 1  # the flipped cell itself
                    for r in neighbor_roots:
                        total += size[r]
                    max_island = max(max_island, total)

        if not has_zero:
            return n * n
        return max_island
```

## C

```c
#include <stdlib.h>

static int find_root(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void union_sets(int *parent, int *sz, int a, int b) {
    int ra = find_root(parent, a);
    int rb = find_root(parent, b);
    if (ra == rb) return;
    if (sz[ra] < sz[rb]) {
        parent[ra] = rb;
        sz[rb] += sz[ra];
    } else {
        parent[rb] = ra;
        sz[ra] += sz[rb];
    }
}

int largestIsland(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int n = gridSize;
    int m = gridColSize[0];
    int total = n * m;

    int *parent = (int *)malloc(total * sizeof(int));
    int *sz = (int *)malloc(total * sizeof(int));

    for (int i = 0; i < total; ++i) {
        parent[i] = i;
        sz[i] = 0;
    }

    // First pass: initialize sizes and union adjacent lands
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 1) {
                int idx = i * m + j;
                sz[idx] = 1;
                // four directions
                if (i > 0 && grid[i - 1][j] == 1) {
                    union_sets(parent, sz, idx, (i - 1) * m + j);
                }
                if (i + 1 < n && grid[i + 1][j] == 1) {
                    union_sets(parent, sz, idx, (i + 1) * m + j);
                }
                if (j > 0 && grid[i][j - 1] == 1) {
                    union_sets(parent, sz, idx, i * m + (j - 1));
                }
                if (j + 1 < m && grid[i][j + 1] == 1) {
                    union_sets(parent, sz, idx, i * m + (j + 1));
                }
            }
        }
    }

    int maxIsland = 0;
    int hasZero = 0;

    // Compute current maximum island size
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 1) {
                int idx = i * m + j;
                int root = find_root(parent, idx);
                if (sz[root] > maxIsland) maxIsland = sz[root];
            } else {
                hasZero = 1;
            }
        }
    }

    // Evaluate flipping each zero
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] != 0) continue;

            int uniq[4];
            int cnt = 0;

            // up
            if (i > 0 && grid[i - 1][j] == 1) {
                int r = find_root(parent, (i - 1) * m + j);
                int dup = 0;
                for (int k = 0; k < cnt; ++k) if (uniq[k] == r) { dup = 1; break; }
                if (!dup) uniq[cnt++] = r;
            }
            // down
            if (i + 1 < n && grid[i + 1][j] == 1) {
                int r = find_root(parent, (i + 1) * m + j);
                int dup = 0;
                for (int k = 0; k < cnt; ++k) if (uniq[k] == r) { dup = 1; break; }
                if (!dup) uniq[cnt++] = r;
            }
            // left
            if (j > 0 && grid[i][j - 1] == 1) {
                int r = find_root(parent, i * m + (j - 1));
                int dup = 0;
                for (int k = 0; k < cnt; ++k) if (uniq[k] == r) { dup = 1; break; }
                if (!dup) uniq[cnt++] = r;
            }
            // right
            if (j + 1 < m && grid[i][j + 1] == 1) {
                int r = find_root(parent, i * m + (j + 1));
                int dup = 0;
                for (int k = 0; k < cnt; ++k) if (uniq[k] == r) { dup = 1; break; }
                if (!dup) uniq[cnt++] = r;
            }

            int curSize = 1; // the flipped cell
            for (int k = 0; k < cnt; ++k) {
                curSize += sz[uniq[k]];
            }
            if (curSize > maxIsland) maxIsland = curSize;
        }
    }

    free(parent);
    free(sz);

    if (!hasZero) return n * m;
    return maxIsland;
}
```

## Csharp

```csharp
public class Solution
{
    public int LargestIsland(int[][] grid)
    {
        int n = grid.Length;
        if (n == 0) return 0;

        var area = new System.Collections.Generic.Dictionary<int, int>();
        int islandId = 2; // start from 2 to distinguish from 0 and 1
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        for (int r = 0; r < n; r++)
        {
            for (int c = 0; c < n; c++)
            {
                if (grid[r][c] != 1) continue;

                int size = 0;
                var stack = new System.Collections.Generic.Stack<(int, int)>();
                stack.Push((r, c));
                grid[r][c] = islandId;

                while (stack.Count > 0)
                {
                    var (cr, cc) = stack.Pop();
                    size++;

                    for (int k = 0; k < 4; k++)
                    {
                        int nr = cr + dr[k];
                        int nc = cc + dc[k];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1)
                        {
                            grid[nr][nc] = islandId;
                            stack.Push((nr, nc));
                        }
                    }
                }

                area[islandId] = size;
                islandId++;
            }
        }

        int maxIsland = 0;
        bool hasZero = false;

        for (int r = 0; r < n; r++)
        {
            for (int c = 0; c < n; c++)
            {
                if (grid[r][c] != 0) continue;

                hasZero = true;
                var neighborIds = new System.Collections.Generic.HashSet<int>();
                for (int k = 0; k < 4; k++)
                {
                    int nr = r + dr[k];
                    int nc = c + dc[k];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n)
                    {
                        int nid = grid[nr][nc];
                        if (nid > 1) neighborIds.Add(nid);
                    }
                }

                int curSize = 1; // the flipped cell
                foreach (int id in neighborIds)
                {
                    curSize += area[id];
                }

                if (curSize > maxIsland) maxIsland = curSize;
            }
        }

        if (!hasZero) return n * n; // all ones
        return maxIsland == 0 ? 1 : maxIsland;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var largestIsland = function(grid) {
    const n = grid.length;
    if (n === 0) return 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let islandId = 2; // start labeling from 2
    const sizeMap = new Map(); // id -> area
    
    // First pass: label islands and compute their sizes
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] !== 1) continue;
            let area = 0;
            const stack = [[i, j]];
            grid[i][j] = islandId;
            while (stack.length) {
                const [r, c] = stack.pop();
                area++;
                for (const [dr, dc] of dirs) {
                    const nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] === 1) {
                        grid[nr][nc] = islandId;
                        stack.push([nr, nc]);
                    }
                }
            }
            sizeMap.set(islandId, area);
            islandId++;
        }
    }
    
    // If there were no islands at all
    if (sizeMap.size === 0) return 1;
    
    let maxArea = 0;
    for (const val of sizeMap.values()) {
        if (val > maxArea) maxArea = val;
    }
    
    // Second pass: try flipping each zero
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] !== 0) continue;
            const seen = new Set();
            let area = 1; // the flipped cell
            for (const [dr, dc] of dirs) {
                const nr = i + dr, nc = j + dc;
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    const id = grid[nr][nc];
                    if (id > 1 && !seen.has(id)) {
                        seen.add(id);
                        area += sizeMap.get(id);
                    }
                }
            }
            if (area > maxArea) maxArea = area;
        }
    }
    
    // If the grid is all ones, maxArea already equals n*n
    return maxArea;
};
```

## Typescript

```typescript
function largestIsland(grid: number[][]): number {
    const n = grid.length;
    if (n === 0) return 0;

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    // island ids start from 2 to distinguish from original 0/1
    let islandId = 2;
    const sizes: number[] = new Array(n * n + 2).fill(0);

    // label islands and compute their sizes
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== 1) continue;
            let size = 0;
            const stack: [number, number][] = [[i, j]];
            grid[i][j] = islandId;

            while (stack.length) {
                const [r, c] = stack.pop()!;
                size++;
                for (const [dr, dc] of dirs) {
                    const nr = r + dr;
                    const nc = c + dc;
                    if (
                        nr >= 0 &&
                        nr < n &&
                        nc >= 0 &&
                        nc < n &&
                        grid[nr][nc] === 1
                    ) {
                        grid[nr][nc] = islandId;
                        stack.push([nr, nc]);
                    }
                }
            }

            sizes[islandId] = size;
            islandId++;
        }
    }

    let maxSize = 0;
    let hasZero = false;

    // evaluate flipping each zero
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] !== 0) continue;
            hasZero = true;
            const neighborIds = new Set<number>();
            for (const [dr, dc] of dirs) {
                const nr = i + dr;
                const nc = j + dc;
                if (
                    nr >= 0 &&
                    nr < n &&
                    nc >= 0 &&
                    nc < n &&
                    grid[nr][nc] > 1
                ) {
                    neighborIds.add(grid[nr][nc]);
                }
            }

            let curSize = 1; // the flipped cell itself
            for (const id of neighborIds) {
                curSize += sizes[id];
            }
            if (curSize > maxSize) maxSize = curSize;
        }
    }

    if (!hasZero) return n * n; // all ones

    // In case flipping any zero yields smaller than an existing island
    // (possible when zeros are isolated), consider the largest original island.
    for (let id = 2; id < islandId; id++) {
        if (sizes[id] > maxSize) maxSize = sizes[id];
    }

    return maxSize;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largestIsland($grid) {
        $n = count($grid);
        if ($n == 0) return 0;
        $total = $n * $n;
        $parent = array_fill(0, $total, -1);
        $size   = array_fill(0, $total, 0);

        // Initialize DSU for land cells
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] == 1) {
                    $idx = $i * $n + $j;
                    $parent[$idx] = $idx;
                    $size[$idx]   = 1;
                }
            }
        }

        // Union adjacent lands (up and left to avoid double work)
        $dirs = [[-1,0],[0,-1]];
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] != 1) continue;
                $idx = $i * $n + $j;
                foreach ($dirs as $d) {
                    $ni = $i + $d[0];
                    $nj = $j + $d[1];
                    if ($ni >= 0 && $ni < $n && $nj >= 0 && $nj < $n && $grid[$ni][$nj] == 1) {
                        $nIdx = $ni * $n + $nj;
                        $this->union($idx, $nIdx, $parent, $size);
                    }
                }
            }
        }

        // Find current maximum island size
        $maxIsland = 0;
        for ($i = 0; $i < $total; ++$i) {
            if ($parent[$i] != -1) {
                $root = $this->find($i, $parent);
                if ($size[$root] > $maxIsland) $maxIsland = $size[$root];
            }
        }

        // Evaluate flipping each zero
        $hasZero = false;
        $dirs4 = [[-1,0],[1,0],[0,-1],[0,1]];
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] != 0) continue;
                $hasZero = true;
                $uniqueRoots = [];
                foreach ($dirs4 as $d) {
                    $ni = $i + $d[0];
                    $nj = $j + $d[1];
                    if ($ni >= 0 && $ni < $n && $nj >= 0 && $nj < $n && $grid[$ni][$nj] == 1) {
                        $neighborIdx = $ni * $n + $nj;
                        $root = $this->find($neighborIdx, $parent);
                        $uniqueRoots[$root] = true;
                    }
                }
                $potential = 1; // the flipped cell
                foreach ($uniqueRoots as $r => $_) {
                    $potential += $size[$r];
                }
                if ($potential > $maxIsland) $maxIsland = $potential;
            }
        }

        // If there was no zero, whole grid is land
        if (!$hasZero) return $n * $n;
        return $maxIsland;
    }

    private function find($x, &$parent) {
        if ($parent[$x] != $x) {
            $parent[$x] = $this->find($parent[$x], $parent);
        }
        return $parent[$x];
    }

    private function union($a, $b, &$parent, &$size) {
        $ra = $this->find($a, $parent);
        $rb = $this->find($b, $parent);
        if ($ra == $rb) return;
        // Union by size
        if ($size[$ra] < $size[$rb]) {
            $parent[$ra] = $rb;
            $size[$rb] += $size[$ra];
        } else {
            $parent[$rb] = $ra;
            $size[$ra] += $size[$rb];
        }
    }
}
```

## Swift

```swift
class Solution {
    class DSU {
        var parent: [Int]
        var sz: [Int]
        init(_ n: Int) {
            parent = Array(0..<n)
            sz = Array(repeating: 1, count: n)
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
            let ra = find(a)
            let rb = find(b)
            if ra == rb { return }
            if sz[ra] < sz[rb] {
                parent[ra] = rb
                sz[rb] += sz[ra]
            } else {
                parent[rb] = ra
                sz[ra] += sz[rb]
            }
        }
        func size(ofRoot root: Int) -> Int {
            return sz[root]
        }
    }

    func largestIsland(_ grid: [[Int]]) -> Int {
        let n = grid.count
        if n == 0 { return 0 }
        let total = n * n
        let dsu = DSU(total)
        var hasZero = false

        // Union adjacent lands
        for i in 0..<n {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    let idx = i * n + j
                    let directions = [(1,0), (0,1)]
                    for (dx, dy) in directions {
                        let ni = i + dx
                        let nj = j + dy
                        if ni >= 0 && ni < n && nj >= 0 && nj < n && grid[ni][nj] == 1 {
                            let nIdx = ni * n + nj
                            dsu.union(idx, nIdx)
                        }
                    }
                } else {
                    hasZero = true
                }
            }
        }

        // Compute current max island size without any flip
        var maxSize = 0
        for i in 0..<n {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    let root = dsu.find(i * n + j)
                    maxSize = max(maxSize, dsu.size(ofRoot: root))
                }
            }
        }

        // If no zero exists, whole grid is land
        if !hasZero { return total }

        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        // Try flipping each zero
        for i in 0..<n {
            for j in 0..<n where grid[i][j] == 0 {
                var seen = Set<Int>()
                var curSize = 1   // the flipped cell itself
                for (dx, dy) in dirs {
                    let ni = i + dx
                    let nj = j + dy
                    if ni >= 0 && ni < n && nj >= 0 && nj < n && grid[ni][nj] == 1 {
                        let root = dsu.find(ni * n + nj)
                        if !seen.contains(root) {
                            seen.insert(root)
                            curSize += dsu.size(ofRoot: root)
                        }
                    }
                }
                maxSize = max(maxSize, curSize)
            }
        }

        return maxSize
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestIsland(grid: Array<IntArray>): Int {
        val n = grid.size
        val total = n * n
        val parent = IntArray(total) { it }
        val size = IntArray(total)

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
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

        // Initialize land cells and union adjacent lands
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    val idx = i * n + j
                    size[idx] = 1
                    if (i + 1 < n && grid[i + 1][j] == 1) {
                        union(idx, (i + 1) * n + j)
                    }
                    if (j + 1 < n && grid[i][j + 1] == 1) {
                        union(idx, i * n + (j + 1))
                    }
                }
            }
        }

        var maxIsland = 0
        // Existing largest island size
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    val root = find(i * n + j)
                    if (size[root] > maxIsland) maxIsland = size[root]
                }
            }
        }

        var hasZero = false
        val dirs = intArrayOf(-1, 0, 1, 0, -1)

        for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] == 0) {
                    hasZero = true
                    var sum = 1
                    val seen = HashSet<Int>()
                    for (k in 0 until 4) {
                        val ni = i + dirs[k]
                        val nj = j + dirs[k + 1]
                        if (ni in 0 until n && nj in 0 until n && grid[ni][nj] == 1) {
                            val root = find(ni * n + nj)
                            if (seen.add(root)) {
                                sum += size[root]
                            }
                        }
                    }
                    if (sum > maxIsland) maxIsland = sum
                }
            }
        }

        return if (!hasZero) n * n else maxIsland
    }
}
```

## Dart

```dart
class Solution {
  int largestIsland(List<List<int>> grid) {
    int n = grid.length;
    int total = n * n;
    List<int> parent = List.filled(total, -1);
    List<int> sz = List.filled(total, 0);

    // Initialize DSU for land cells
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) {
          int idx = i * n + j;
          parent[idx] = idx;
          sz[idx] = 1;
        }
      }
    }

    List<int> dr = [1, -1, 0, 0];
    List<int> dc = [0, 0, 1, -1];

    // Union adjacent lands
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] != 1) continue;
        int idx = i * n + j;
        for (int d = 0; d < 4; ++d) {
          int ni = i + dr[d];
          int nj = j + dc[d];
          if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;
          if (grid[ni][nj] != 1) continue;
          int nIdx = ni * n + nj;
          _union(parent, sz, idx, nIdx);
        }
      }
    }

    // Current maximum island size
    int maxSize = 0;
    for (int i = 0; i < total; ++i) {
      if (parent[i] != -1 && parent[i] == i && sz[i] > maxSize) {
        maxSize = sz[i];
      }
    }

    bool hasZero = false;

    // Try flipping each zero
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) continue;
        hasZero = true;
        Set<int> seen = {};
        int curSize = 1; // the flipped cell
        for (int d = 0; d < 4; ++d) {
          int ni = i + dr[d];
          int nj = j + dc[d];
          if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;
          if (grid[ni][nj] != 1) continue;
          int nIdx = ni * n + nj;
          int root = _find(parent, nIdx);
          if (!seen.contains(root)) {
            seen.add(root);
            curSize += sz[root];
          }
        }
        if (curSize > maxSize) maxSize = curSize;
      }
    }

    if (!hasZero) return total; // all ones
    return maxSize;
  }

  int _find(List<int> parent, int x) {
    int p = parent[x];
    if (p != x) {
      parent[x] = _find(parent, p);
    }
    return parent[x];
  }

  void _union(List<int> parent, List<int> sz, int a, int b) {
    int ra = _find(parent, a);
    int rb = _find(parent, b);
    if (ra == rb) return;
    if (sz[ra] < sz[rb]) {
      parent[ra] = rb;
      sz[rb] += sz[ra];
    } else {
      parent[rb] = ra;
      sz[ra] += sz[rb];
    }
  }
}
```

## Golang

```go
func largestIsland(grid [][]int) int {
    n := len(grid)
    if n == 0 {
        return 0
    }
    // Map island id to its area
    islandArea := make(map[int]int)
    id := 2 // start labeling islands from 2

    var dfs func(r, c, label int) int
    dfs = func(r, c, label int) int {
        if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1 {
            return 0
        }
        grid[r][c] = label
        area := 1
        dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
        for _, d := range dirs {
            area += dfs(r+d[0], c+d[1], label)
        }
        return area
    }

    // First pass: label each island and compute its size
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                area := dfs(i, j, id)
                islandArea[id] = area
                id++
            }
        }
    }

    maxSize := 0
    hasZero := false
    dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    // Second pass: try flipping each zero
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 0 {
                hasZero = true
                seen := make(map[int]struct{})
                size := 1 // the flipped cell itself
                for _, d := range dirs {
                    ni, nj := i+d[0], j+d[1]
                    if ni >= 0 && ni < n && nj >= 0 && nj < n {
                        neighborID := grid[ni][nj]
                        if neighborID > 1 {
                            if _, ok := seen[neighborID]; !ok {
                                seen[neighborID] = struct{}{}
                                size += islandArea[neighborID]
                            }
                        }
                    }
                }
                if size > maxSize {
                    maxSize = size
                }
            }
        }
    }

    if !hasZero {
        return n * n
    }
    if maxSize == 0 { // all zeros case
        return 1
    }
    return maxSize
}
```

## Ruby

```ruby
def largest_island(grid)
  n = grid.size
  return 0 if n == 0

  total = n * n
  parent = Array.new(total) { |i| i }
  size   = Array.new(total, 1)

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
      parent[ra] = rb
      size[rb] += size[ra]
    else
      parent[rb] = ra
      size[ra] += size[rb]
    end
  end

  dirs = [[1,0],[0,1],[-1,0],[0,-1]]

  # Union adjacent lands
  n.times do |r|
    n.times do |c|
      next unless grid[r][c] == 1
      idx = r * n + c
      # only right and down to avoid duplicate work
      if r + 1 < n && grid[r+1][c] == 1
        union.call(idx, (r+1) * n + c)
      end
      if c + 1 < n && grid[r][c+1] == 1
        union.call(idx, r * n + (c+1))
      end
    end
  end

  max_island = 0
  # compute current max island size
  n.times do |r|
    n.times do |c|
      if grid[r][c] == 1
        root = find.call(r * n + c)
        max_island = [max_island, size[root]].max
      end
    end
  end

  has_zero = false
  # evaluate flipping each zero
  n.times do |r|
    n.times do |c|
      next unless grid[r][c] == 0
      has_zero = true
      seen = Set.new
      dirs.each do |dr, dc|
        nr = r + dr
        nc = c + dc
        next if nr < 0 || nr >= n || nc < 0 || nc >= n
        next unless grid[nr][nc] == 1
        root = find.call(nr * n + nc)
        seen.add(root)
      end
      cur_size = 1
      seen.each { |root| cur_size += size[root] }
      max_island = [max_island, cur_size].max
    end
  end

  return max_island if has_zero
  # all ones
  n * n
end
```

## Scala

```scala
object Solution {
    def largestIsland(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        val total = n * n
        val parent = new Array[Int](total)
        val sz = new Array[Int](total)

        for (i <- 0 until total) {
            parent(i) = i
            sz(i) = 0
        }

        def idx(r: Int, c: Int): Int = r * n + c

        def find(x: Int): Int = {
            var p = x
            while (parent(p) != p) {
                parent(p) = parent(parent(p))
                p = parent(p)
            }
            p
        }

        def union(a: Int, b: Int): Unit = {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (sz(ra) < sz(rb)) {
                val tmp = ra; ra = rb; rb = tmp
            }
            parent(rb) = ra
            sz(ra) += sz(rb)
        }

        // Initialize sizes for land cells
        for (r <- 0 until n; c <- 0 until n) {
            if (grid(r)(c) == 1) {
                val id = idx(r, c)
                sz(id) = 1
            }
        }

        // Union adjacent lands (right and down to avoid duplicates)
        val dirs = Array((1, 0), (0, 1))
        for (r <- 0 until n; c <- 0 until n if grid(r)(c) == 1) {
            val id = idx(r, c)
            for ((dr, dc) <- dirs) {
                val nr = r + dr
                val nc = c + dc
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid(nr)(nc) == 1) {
                    union(id, idx(nr, nc))
                }
            }
        }

        var maxIsland = 0
        for (i <- 0 until total) {
            if (parent(i) == i && sz(i) > maxIsland) maxIsland = sz(i)
        }

        var hasZero = false
        var result = maxIsland
        val neigh = Array((-1, 0), (1, 0), (0, -1), (0, 1))

        for (r <- 0 until n; c <- 0 until n) {
            if (grid(r)(c) == 0) {
                hasZero = true
                val seen = scala.collection.mutable.Set[Int]()
                var sum = 1 // the flipped cell itself
                for ((dr, dc) <- neigh) {
                    val nr = r + dr
                    val nc = c + dc
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid(nr)(nc) == 1) {
                        val root = find(idx(nr, nc))
                        if (!seen.contains(root)) {
                            seen.add(root)
                            sum += sz(root)
                        }
                    }
                }
                if (sum > result) result = sum
            }
        }

        if (!hasZero) n * n else result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 0 {
            return 0;
        }
        let m = grid[0].len();
        let total = n * m;
        // island ids start from 2 to avoid confusion with 0 and 1
        let mut sizes = vec![0usize; total + 2];
        let mut island_id: usize = 2;
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];

        // label islands and compute their areas
        for i in 0..n {
            for j in 0..m {
                if grid[i][j] == 1 {
                    let mut stack = Vec::new();
                    stack.push((i, j));
                    grid[i][j] = island_id as i32;
                    let mut area = 0usize;

                    while let Some((x, y)) = stack.pop() {
                        area += 1;
                        for (dx, dy) in &dirs {
                            let nx = x as i32 + dx;
                            let ny = y as i32 + dy;
                            if nx >= 0 && nx < n as i32 && ny >= 0 && ny < m as i32 {
                                let ux = nx as usize;
                                let uy = ny as usize;
                                if grid[ux][uy] == 1 {
                                    grid[ux][uy] = island_id as i32;
                                    stack.push((ux, uy));
                                }
                            }
                        }
                    }

                    sizes[island_id] = area;
                    island_id += 1;
                }
            }
        }

        // current maximum island size (without any flip)
        let mut max_area = *sizes.iter().max().unwrap_or(&0);
        let mut has_zero = false;

        // try flipping each zero
        for i in 0..n {
            for j in 0..m {
                if grid[i][j] == 0 {
                    has_zero = true;
                    let mut neighbor_ids = [0usize; 4];
                    let mut cnt = 0usize;

                    for (dx, dy) in &dirs {
                        let nx = i as i32 + dx;
                        let ny = j as i32 + dy;
                        if nx >= 0 && nx < n as i32 && ny >= 0 && ny < m as i32 {
                            let id = grid[nx as usize][ny as usize] as usize;
                            if id > 1 {
                                // ensure uniqueness
                                let mut duplicate = false;
                                for k in 0..cnt {
                                    if neighbor_ids[k] == id {
                                        duplicate = true;
                                        break;
                                    }
                                }
                                if !duplicate {
                                    neighbor_ids[cnt] = id;
                                    cnt += 1;
                                }
                            }
                        }
                    }

                    let mut combined = 1usize; // the flipped cell itself
                    for k in 0..cnt {
                        combined += sizes[neighbor_ids[k]];
                    }
                    if combined > max_area {
                        max_area = combined;
                    }
                }
            }
        }

        if !has_zero {
            // grid is all ones
            return (n * m) as i32;
        }
        max_area as i32
    }
}
```

## Racket

```racket
(define/contract (largest-island grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (= rows 0) 0 (length (first grid))))
         ;; mutable copy of the grid
         (g (list->vector (map list->vector grid)))
         (dirs (list (cons 1 0) (cons -1 0) (cons 0 1) (cons 0 -1)))
         (id-sizes (make-hash))
         (next-id 2))

    ;; label islands with DFS using an explicit stack
    (for ([i (in-range rows)])
      (for ([j (in-range cols)])
        (when (= (vector-ref (vector-ref g i) j) 1)
          (let loop ((stack (list (cons i j))) (size 0))
            (if (null? stack)
                (begin
                  (hash-set! id-sizes next-id size)
                  (set! next-id (+ next-id 1)))
                (let* ((rc (car stack))
                       (rest (cdr stack))
                       (r (car rc)) (c (cdr rc))
                       (val (vector-ref (vector-ref g r) c)))
                  (if (= val next-id)                     ; already visited
                      (loop rest size)
                      (begin
                        (vector-set! (vector-ref g r) c next-id)
                        (let ((new-size (+ size 1))
                              (new-stack rest))
                          (for ([d dirs])
                            (define nr (+ r (car d)))
                            (define nc (+ c (cdr d)))
                            (when (and (>= nr 0) (< nr rows)
                                       (>= nc 0) (< nc cols)
                                       (= (vector-ref (vector-ref g nr) nc) 1))
                              (set! new-stack (cons (cons nr nc) new-stack))))
                          (loop new-stack new-size)))))))))

    ;; initial maximum island size (without any flip)
    (define max-island
      (if (hash-empty? id-sizes)
          0
          (apply max (hash-values id-sizes))))

    (define has-zero #f)

    ;; try flipping each zero cell
    (for ([i (in-range rows)])
      (for ([j (in-range cols)])
        (when (= (vector-ref (vector-ref g i) j) 0)
          (set! has-zero #t)
          (let ((seen (make-hash))
                (total 1))
            (for ([d dirs])
              (define nr (+ i (car d)))
              (define nc (+ j (cdr d)))
              (when (and (>= nr 0) (< nr rows)
                         (>= nc 0) (< nc cols))
                (let ((nid (vector-ref (vector-ref g nr) nc)))
                  (when (>= nid 2)
                    (unless (hash-has-key? seen nid)
                      (set! total (+ total (hash-ref id-sizes nid)))
                      (hash-set! seen nid #t))))))
            (when (> total max-island) (set! max-island total))))))

    (if has-zero
        max-island
        (* rows cols))) )
```

## Erlang

```erlang
-export([largest_island/1]).

-spec largest_island(Grid :: [[integer()]]) -> integer().
largest_island(Grid) ->
    N = length(Grid),
    M = case Grid of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    Total = N * M,
    FlatList = lists:flatten(Grid),
    FlatArr = array:from_list(FlatList),

    ets:new(parent, [named_table, public]),
    ets:new(size,   [named_table, public]),

    first_pass(0, Total, FlatArr),
    second_pass(0, Total, M, N, FlatArr),

    MaxCurrent = ets:foldl(fun({_Idx,Size}, Acc) -> if Size > Acc -> Size; true -> Acc end end,
                           0, size),

    {HasZero, MaxAfter} = loop_zero(0, Total, M, N, FlatArr, MaxCurrent, false),

    Result = case HasZero of
                 true -> MaxAfter;
                 false -> N * M
             end,

    ets:delete(parent),
    ets:delete(size),
    Result.

first_pass(Index, Total, FlatArr) when Index < Total ->
    case array:get(Index, FlatArr) of
        1 ->
            ets:insert(parent,{Index, Index}),
            ets:insert(size,{Index,1});
        _ -> ok
    end,
    first_pass(Index+1, Total, FlatArr);
first_pass(_, _, _) -> ok.

second_pass(Index, Total, M, N, FlatArr) when Index < Total ->
    case array:get(Index, FlatArr) of
        1 ->
            I = Index div M,
            J = Index rem M,
            (if J + 1 < M ->
                    IdxR = Index + 1,
                    case array:get(IdxR, FlatArr) of
                        1 -> union(Index, IdxR);
                        _ -> ok
                    end;
                true -> ok),
            (if I + 1 < N ->
                    IdxD = Index + M,
                    case array:get(IdxD, FlatArr) of
                        1 -> union(Index, IdxD);
                        _ -> ok
                    end;
                true -> ok),
            second_pass(Index+1, Total, M, N, FlatArr);
        _ ->
            second_pass(Index+1, Total, M, N, FlatArr)
    end;
second_pass(_, _, _, _, _) -> ok.

union(A,B) ->
    RA = find(A),
    RB = find(B),
    if RA =/= RB ->
            [{_, SizeA}] = ets:lookup(size, RA),
            [{_, SizeB}] = ets:lookup(size, RB),
            if SizeA >= SizeB ->
                    ets:insert(parent,{RB,RA}),
                    ets:update_counter(size, RA, {2, SizeB});
               true ->
                    ets:insert(parent,{RA,RB}),
                    ets:update_counter(size, RB, {2, SizeA})
            end;
       true -> ok
    end.

find(X) ->
    case ets:lookup(parent, X) of
        [{_, X}] -> X;
        [{_, P}] ->
            Root = find(P),
            ets:insert(parent,{X,Root}),
            Root
    end.

loop_zero(Index, Total, M, N, FlatArr, MaxSoFar, HasZero) when Index < Total ->
    case array:get(Index, FlatArr) of
        0 ->
            I = Index div M,
            J = Index rem M,
            SumSize = neighbor_sum(I, J, M, N, FlatArr, #{}),
            TotalSize = 1 + SumSize,
            NewMax = if TotalSize > MaxSoFar -> TotalSize; true -> MaxSoFar end,
            loop_zero(Index+1, Total, M, N, FlatArr, NewMax, true);
        _ ->
            loop_zero(Index+1, Total, M, N, FlatArr, MaxSoFar, HasZero)
    end;
loop_zero(_, _, _, _, _, Max, HasZero) -> {HasZero, Max}.

neighbor_sum(I,J,M,N,FlatArr,Seen) ->
    Dirs = [{-1,0},{1,0},{0,-1},{0,1}],
    {_, Sum} = lists:foldl(
        fun({DI,DJ}, {Map,Acc}) ->
            NI = I + DI,
            NJ = J + DJ,
            if NI >= 0, NI < N, NJ >= 0, NJ < M ->
                    Idx = NI * M + NJ,
                    case array:get(Idx, FlatArr) of
                        1 ->
                            Root = find(Idx),
                            case maps:is_key(Root, Map) of
                                true -> {Map, Acc};
                                false ->
                                    [{_,Size}] = ets:lookup(size, Root),
                                    {maps:put(Root,true,Map), Acc + Size}
                            end;
                        _ -> {Map, Acc}
                    end;
               true -> {Map, Acc}
            end
        end,
        {Seen,0},
        Dirs),
    Sum.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_island(grid :: [[integer]]) :: integer
  def largest_island(grid) do
    rows = length(grid)
    cols = rows
    total = rows * cols

    # flatten grid to a one‑dimensional array for fast access
    land_list = List.flatten(grid)
    land = :array.from_list(land_list)

    ids = :array.new(total, default: 0)

    {ids, sizes, _next_id} =
      Enum.reduce(0..(total - 1), {ids, %{}, 2}, fn idx, {ids_acc, sizes_acc, cur_id} ->
        if :array.get(idx, land) == 1 and :array.get(idx, ids_acc) == 0 do
          {new_ids, area} = bfs([idx], ids_acc, cur_id, 0, rows, cols, land)
          {new_ids, Map.put(sizes_acc, cur_id, area), cur_id + 1}
        else
          {ids_acc, sizes_acc, cur_id}
        end
      end)

    # evaluate each zero cell
    {max_island, has_zero} =
      Enum.reduce(0..(total - 1), {0, false}, fn idx, {cur_max, zero_flag} ->
        if :array.get(idx, land) == 0 do
          r = div(idx, cols)
          c = rem(idx, cols)

          neighbor_ids =
            []
            |> maybe_add(r > 0, (r - 1) * cols + c, ids, land)
            |> maybe_add(c > 0, r * cols + (c - 1), ids, land)
            |> maybe_add(r < rows - 1, (r + 1) * cols + c, ids, land)
            |> maybe_add(c < cols - 1, r * cols + (c + 1), ids, land)

          sum =
            Enum.reduce(neighbor_ids, 1, fn nid, acc ->
              acc + Map.get(sizes, nid, 0)
            end)

          {max(cur_max, sum), true}
        else
          {cur_max, zero_flag}
        end
      end)

    if not has_zero do
      rows * cols
    else
      max_island
    end
  end

  # depth‑first search using an explicit stack (tail‑recursive)
  defp bfs([], ids, _island_id, area, _rows, _cols, _land), do: {ids, area}

  defp bfs([idx | rest], ids, island_id, area, rows, cols, land) do
    if :array.get(idx, ids) != 0 do
      bfs(rest, ids, island_id, area, rows, cols, land)
    else
      ids1 = :array.set(idx, island_id, ids)
      r = div(idx, cols)
      c = rem(idx, cols)

      neighbor_idxs =
        []
        |> maybe_push(r > 0, (r - 1) * cols + c, ids1, land)
        |> maybe_push(c > 0, r * cols + (c - 1), ids1, land)
        |> maybe_push(r < rows - 1, (r + 1) * cols + c, ids1, land)
        |> maybe_push(c < cols - 1, r * cols + (c + 1), ids1, land)

      bfs(neighbor_idxs ++ rest, ids1, island_id, area + 1, rows, cols, land)
    end
  end

  # helper to conditionally add an island id to a list
  defp maybe_add(list, true, nidx, ids, land) do
    if :array.get(nidx, land) == 1 and :array.get(nidx, ids) != 0 do
      [ :array.get(nidx, ids) | list ]
    else
      list
    end
  end

  defp maybe_add(list, false, _nidx, _ids, _land), do: list

  # helper to conditionally push neighbor index onto stack during BFS
  defp maybe_push(list, true, nidx, ids, land) do
    if :array.get(nidx, land) == 1 and :array.get(nidx, ids) == 0 do
      [nidx | list]
    else
      list
    end
  end

  defp maybe_push(list, false, _nidx, _ids, _land), do: list
end
```

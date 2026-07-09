# 2617. Minimum Number of Visited Cells in a Grid

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumVisitedCells(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector< set<int> > rowSet(m);
        vector< set<int> > colSet(n);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rowSet[i].insert(j);
                colSet[j].insert(i);
            }
        }
        vector<vector<int>> dist(m, vector<int>(n, -1));
        queue<pair<int,int>> q;
        dist[0][0] = 1;
        q.emplace(0,0);
        rowSet[0].erase(0);
        colSet[0].erase(0);
        while (!q.empty()) {
            auto [i,j] = q.front(); q.pop();
            int step = grid[i][j];
            // move right
            int maxR = min(n-1, j + step);
            auto it = rowSet[i].lower_bound(j+1);
            while (it != rowSet[i].end() && *it <= maxR) {
                int y = *it;
                dist[i][y] = dist[i][j] + 1;
                q.emplace(i, y);
                colSet[y].erase(i);
                it = rowSet[i].erase(it);
            }
            // move down
            int maxD = min(m-1, i + step);
            auto it2 = colSet[j].lower_bound(i+1);
            while (it2 != colSet[j].end() && *it2 <= maxD) {
                int x = *it2;
                dist[x][j] = dist[i][j] + 1;
                q.emplace(x, j);
                rowSet[x].erase(j);
                it2 = colSet[j].erase(it2);
            }
        }
        return dist[m-1][n-1];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumVisitedCells(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        @SuppressWarnings("unchecked")
        TreeSet<Integer>[] rowSets = new TreeSet[m];
        for (int i = 0; i < m; i++) {
            rowSets[i] = new TreeSet<>();
            for (int j = 0; j < n; j++) {
                rowSets[i].add(j);
            }
        }

        @SuppressWarnings("unchecked")
        TreeSet<Integer>[] colSets = new TreeSet[n];
        for (int j = 0; j < n; j++) {
            colSets[j] = new TreeSet<>();
            for (int i = 0; i < m; i++) {
                colSets[j].add(i);
            }
        }

        boolean[][] visited = new boolean[m][n];
        int[][] dist = new int[m][n];
        ArrayDeque<int[]> q = new ArrayDeque<>();

        visited[0][0] = true;
        dist[0][0] = 1;
        q.add(new int[]{0, 0});
        rowSets[0].remove(0);
        colSets[0].remove(0);

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int i = cur[0];
            int j = cur[1];

            if (i == m - 1 && j == n - 1) {
                return dist[i][j];
            }

            int jump = grid[i][j];

            // Move right within the same row
            TreeSet<Integer> rset = rowSets[i];
            Integer col = rset.ceiling(j + 1);
            while (col != null && col <= j + jump) {
                visited[i][col] = true;
                dist[i][col] = dist[i][j] + 1;
                q.add(new int[]{i, col});
                // remove from both row and column sets
                rset.remove(col);
                colSets[col].remove(i);
                col = rset.ceiling(j + 1);
            }

            // Move down within the same column
            TreeSet<Integer> cset = colSets[j];
            Integer row = cset.ceiling(i + 1);
            while (row != null && row <= i + jump) {
                visited[row][j] = true;
                dist[row][j] = dist[i][j] + 1;
                q.add(new int[]{row, j});
                // remove from both column and row sets
                cset.remove(row);
                rowSets[row].remove(j);
                row = cset.ceiling(i + 1);
            }
        }

        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumVisitedCells(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1

        # DSU "next" structures for rows and columns
        row_next = [list(range(n + 1)) for _ in range(m)]   # row_next[i][c] -> next unvisited column >= c in row i
        col_next = [list(range(m + 1)) for _ in range(n)]   # col_next[j][r] -> next unvisited row    >= r in column j

        def find_row(i, c):
            nxt = row_next[i]
            while nxt[c] != c:
                nxt[c] = nxt[nxt[c]]
                c = nxt[c]
            return c

        def find_col(j, r):
            nxt = col_next[j]
            while nxt[r] != r:
                nxt[r] = nxt[nxt[r]]
                r = nxt[r]
            return r

        visited = [[False] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]

        q = deque()
        q.append((0, 0))
        visited[0][0] = True
        dist[0][0] = 1

        # remove start cell from both DSU sets
        row_next[0][0] = find_row(0, 1)
        col_next[0][0] = find_col(0, 1)

        while q:
            i, j = q.popleft()
            cur_d = dist[i][j]
            step = grid[i][j]

            # move right in the same row
            max_c = min(n - 1, j + step)
            c = find_row(i, j + 1)
            while c <= max_c:
                visited[i][c] = True
                dist[i][c] = cur_d + 1
                if i == m - 1 and c == n - 1:
                    return dist[i][c]
                q.append((i, c))

                # remove (i,c) from row set
                row_next[i][c] = find_row(i, c + 1)
                # also remove from column set
                col_next[c][i] = find_col(c, i + 1)

                c = find_row(i, c)   # next unvisited column after removal

            # move down in the same column
            max_r = min(m - 1, i + step)
            r = find_col(j, i + 1)
            while r <= max_r:
                visited[r][j] = True
                dist[r][j] = cur_d + 1
                if r == m - 1 and j == n - 1:
                    return dist[r][j]
                q.append((r, j))

                # remove (r,j) from column set
                col_next[j][r] = find_col(j, r + 1)
                # also remove from row set
                row_next[r][j] = find_row(r, j + 1)

                r = find_col(j, r)   # next unvisited row after removal

        return -1
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1

        # DSU "next" structures for rows and columns
        parent_row = [list(range(n + 1)) for _ in range(m)]   # size n+1, sentinel at n
        parent_col = [list(range(m + 1)) for _ in range(n)]   # size m+1, sentinel at m

        def find_row(r: int, x: int) -> int:
            pr = parent_row[r]
            while pr[x] != x:
                pr[x] = pr[pr[x]]
                x = pr[x]
            return x

        def find_col(c: int, x: int) -> int:
            pc = parent_col[c]
            while pc[x] != x:
                pc[x] = pc[pc[x]]
                x = pc[x]
            return x

        visited = [[False] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]

        q = deque()
        visited[0][0] = True
        dist[0][0] = 1
        q.append((0, 0))

        # remove start from both DSUs
        parent_row[0][0] = find_row(0, 1)
        parent_col[0][0] = find_col(0, 1)

        while q:
            i, j = q.popleft()
            d = dist[i][j]
            step = grid[i][j]

            # move right in the same row
            left = j + 1
            right = min(n - 1, j + step)
            c = find_row(i, left)
            while c <= right:
                if not visited[i][c]:
                    visited[i][c] = True
                    dist[i][c] = d + 1
                    q.append((i, c))
                    # remove from column DSU
                    parent_col[c][i] = find_col(c, i + 1)
                # skip this column for future traversals in this row
                parent_row[i][c] = find_row(i, c + 1)
                c = find_row(i, c)

            # move down in the same column
            top = i + 1
            bottom = min(m - 1, i + step)
            r = find_col(j, top)
            while r <= bottom:
                if not visited[r][j]:
                    visited[r][j] = True
                    dist[r][j] = d + 1
                    q.append((r, j))
                    # remove from row DSU
                    parent_row[r][j] = find_row(r, j + 1)
                # skip this row for future traversals in this column
                parent_col[j][r] = find_col(j, r + 1)
                r = find_col(j, r)

            if visited[m - 1][n - 1]:
                return dist[m - 1][n - 1]

        return -1
```

## C

```c
#include <stdlib.h>

static int *rowParent;   // size: m * (n + 1)
static int *colParent;   // size: n * (m + 1)
static int m, n;

static int findRow(int i, int x) {
    int base = i * (n + 1);
    int *p = rowParent + base;
    if (x > n) return n;
    if (p[x] == x) return x;
    p[x] = findRow(i, p[x]);
    return p[x];
}

static int findCol(int j, int x) {
    int base = j * (m + 1);
    int *p = colParent + base;
    if (x > m) return m;
    if (p[x] == x) return x;
    p[x] = findCol(j, p[x]);
    return p[x];
}

int minimumVisitedCells(int** grid, int gridSize, int* gridColSize){
    m = gridSize;
    n = gridColSize[0];

    int total = m * n;

    /* allocate DSU structures */
    rowParent = (int*)malloc(sizeof(int) * m * (n + 1));
    colParent = (int*)malloc(sizeof(int) * n * (m + 1));

    for (int i = 0; i < m; ++i) {
        int base = i * (n + 1);
        for (int j = 0; j <= n; ++j)
            rowParent[base + j] = j;
    }
    for (int j = 0; j < n; ++j) {
        int base = j * (m + 1);
        for (int i = 0; i <= m; ++i)
            colParent[base + i] = i;
    }

    /* distance array */
    int *dist = (int*)malloc(sizeof(int) * total);
    for (int i = 0; i < total; ++i) dist[i] = -1;

    /* BFS queue */
    int *queue = (int*)malloc(sizeof(int) * total);
    int head = 0, tail = 0;

    /* start cell */
    dist[0] = 1;
    queue[tail++] = 0;
    rowParent[0 * (n + 1) + 0] = findRow(0, 1);
    colParent[0 * (m + 1) + 0] = findCol(0, 1);

    while (head < tail) {
        int id = queue[head++];
        int i = id / n;
        int j = id % n;
        int curDist = dist[id];

        if (i == m - 1 && j == n - 1) {
            free(rowParent);
            free(colParent);
            free(dist);
            free(queue);
            return curDist;
        }

        int step = grid[i][j];
        /* move right */
        int maxR = j + step;
        if (maxR >= n) maxR = n - 1;
        int colIdx = findRow(i, j + 1);
        while (colIdx <= maxR) {
            int nid = i * n + colIdx;
            dist[nid] = curDist + 1;
            queue[tail++] = nid;

            /* remove from row set */
            rowParent[i * (n + 1) + colIdx] = findRow(i, colIdx + 1);
            /* remove from column set */
            colParent[colIdx * (m + 1) + i] = findCol(colIdx, i + 1);

            colIdx = findRow(i, colIdx);   // next unvisited in this row
        }

        /* move down */
        int maxD = i + step;
        if (maxD >= m) maxD = m - 1;
        int rowIdx = findCol(j, i + 1);
        while (rowIdx <= maxD) {
            int nid = rowIdx * n + j;
            dist[nid] = curDist + 1;
            queue[tail++] = nid;

            /* remove from column set */
            colParent[j * (m + 1) + rowIdx] = findCol(j, rowIdx + 1);
            /* remove from row set */
            rowParent[rowIdx * (n + 1) + j] = findRow(rowIdx, j + 1);

            rowIdx = findCol(j, rowIdx);   // next unvisited in this column
        }
    }

    free(rowParent);
    free(colParent);
    free(dist);
    free(queue);
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinimumVisitedCells(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[,] dist = new int[m, n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) dist[i, j] = -1;
        }

        // Row sets: columns not yet visited in each row
        SortedSet<int>[] rowSets = new SortedSet<int>[m];
        for (int i = 0; i < m; i++) {
            var set = new SortedSet<int>();
            for (int j = 0; j < n; j++) set.Add(j);
            rowSets[i] = set;
        }

        // Column sets: rows not yet visited in each column
        SortedSet<int>[] colSets = new SortedSet<int>[n];
        for (int j = 0; j < n; j++) {
            var set = new SortedSet<int>();
            for (int i = 0; i < m; i++) set.Add(i);
            colSets[j] = set;
        }

        Queue<(int, int)> q = new Queue<(int, int)>();
        dist[0, 0] = 1;
        q.Enqueue((0, 0));
        rowSets[0].Remove(0);
        colSets[0].Remove(0);

        while (q.Count > 0) {
            var (i, j) = q.Dequeue();
            if (i == m - 1 && j == n - 1) return dist[i, j];

            int step = grid[i][j];
            // Move right in the same row
            int maxCol = Math.Min(n - 1, j + step);
            if (j + 1 <= maxCol) {
                var view = rowSets[i].GetViewBetween(j + 1, maxCol);
                foreach (int col in view.ToList()) {
                    dist[i, col] = dist[i, j] + 1;
                    q.Enqueue((i, col));
                    rowSets[i].Remove(col);
                    colSets[col].Remove(i);
                }
            }

            // Move down in the same column
            int maxRow = Math.Min(m - 1, i + step);
            if (i + 1 <= maxRow) {
                var view = colSets[j].GetViewBetween(i + 1, maxRow);
                foreach (int row in view.ToList()) {
                    dist[row, j] = dist[i, j] + 1;
                    q.Enqueue((row, j));
                    colSets[j].Remove(row);
                    rowSets[row].Remove(j);
                }
            }
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumVisitedCells = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const total = m * n;

    // distance (visited cells count), 0 means unvisited
    const dist = new Int32Array(total);
    // row DSU: for each row, next unvisited column index
    const rowParent = new Array(m);
    for (let i = 0; i < m; ++i) {
        const arr = new Int32Array(n + 1);
        for (let k = 0; k <= n; ++k) arr[k] = k;
        rowParent[i] = arr;
    }
    // column DSU: for each column, next unvisited row index
    const colParent = new Array(n);
    for (let j = 0; j < n; ++j) {
        const arr = new Int32Array(m + 1);
        for (let k = 0; k <= m; ++k) arr[k] = k;
        colParent[j] = arr;
    }

    function findRow(row, x) {
        const parent = rowParent[row];
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function findCol(col, x) {
        const parent = colParent[col];
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    // BFS queue
    const q = new Int32Array(total);
    let head = 0, tail = 0;
    q[tail++] = 0;               // start index (0,0)
    dist[0] = 1;                 // count includes starting cell

    while (head < tail) {
        const curIdx = q[head++];
        const i = Math.floor(curIdx / n);
        const j = curIdx % n;

        if (i === m - 1 && j === n - 1) return dist[curIdx];

        const step = grid[i][j];
        // Horizontal moves to the right
        let maxC = Math.min(n - 1, j + step);
        let c = findRow(i, j + 1);
        while (c <= maxC) {
            const idx2 = i * n + c;
            if (dist[idx2] === 0) {
                dist[idx2] = dist[curIdx] + 1;
                q[tail++] = idx2;
            }
            // remove (i,c) from both DSUs
            rowParent[i][c] = c + 1;
            colParent[c][i] = i + 1;
            c = findRow(i, c);
        }

        // Vertical moves downwards
        let maxR = Math.min(m - 1, i + step);
        let r = findCol(j, i + 1);
        while (r <= maxR) {
            const idx2 = r * n + j;
            if (dist[idx2] === 0) {
                dist[idx2] = dist[curIdx] + 1;
                q[tail++] = idx2;
            }
            // remove (r,j) from both DSUs
            rowParent[r][j] = j + 1;
            colParent[j][r] = r + 1;
            r = findCol(j, r);
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minimumVisitedCells(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dist: number[][] = Array.from({ length: m }, () => Array(n).fill(INF));

    // DSU for rows and columns
    const rowNext: number[][] = new Array(m);
    for (let i = 0; i < m; i++) {
        rowNext[i] = new Array(n + 1);
        for (let j = 0; j <= n; j++) rowNext[i][j] = j;
    }
    const colNext: number[][] = new Array(n);
    for (let j = 0; j < n; j++) {
        colNext[j] = new Array(m + 1);
        for (let i = 0; i <= m; i++) colNext[j][i] = i;
    }

    const findRow = (i: number, j: number): number => {
        const arr = rowNext[i];
        while (arr[j] !== j) {
            arr[j] = arr[arr[j]];
            j = arr[j];
        }
        return j;
    };
    const unionRow = (i: number, j: number): void => {
        rowNext[i][j] = findRow(i, j + 1);
    };

    const findCol = (j: number, i: number): number => {
        const arr = colNext[j];
        while (arr[i] !== i) {
            arr[i] = arr[arr[i]];
            i = arr[i];
        }
        return i;
    };
    const unionCol = (j: number, i: number): void => {
        colNext[j][i] = findCol(j, i + 1);
    };

    // BFS queue
    const qx: number[] = [];
    const qy: number[] = [];
    let head = 0;

    dist[0][0] = 1;
    qx.push(0);
    qy.push(0);
    unionRow(0, 0);
    unionCol(0, 0);

    while (head < qx.length) {
        const i = qx[head];
        const j = qy[head];
        const d = dist[i][j];
        head++;

        if (i === m - 1 && j === n - 1) return d;

        // Move right
        const maxRight = Math.min(n - 1, j + grid[i][j]);
        let c = findRow(i, j + 1);
        while (c <= maxRight) {
            dist[i][c] = d + 1;
            qx.push(i);
            qy.push(c);
            unionRow(i, c);
            unionCol(c, i);
            c = findRow(i, c + 1);
        }

        // Move down
        const maxDown = Math.min(m - 1, i + grid[i][j]);
        let r = findCol(j, i + 1);
        while (r <= maxDown) {
            dist[r][j] = d + 1;
            qx.push(r);
            qy.push(j);
            unionRow(r, j);
            unionCol(j, r);
            r = findCol(j, r + 1);
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumVisitedCells($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        // distance matrix, -1 means unvisited
        $dist = array_fill(0, $m, null);
        for ($i = 0; $i < $m; ++$i) {
            $dist[$i] = array_fill(0, $n, -1);
        }

        // DSU-like "next" arrays for rows and columns
        $rowNext = array_fill(0, $m, null);
        for ($i = 0; $i < $m; ++$i) {
            $rowNext[$i] = range(0, $n); // size n+1, sentinel at n
        }
        $colNext = array_fill(0, $n, null);
        for ($j = 0; $j < $n; ++$j) {
            $colNext[$j] = range(0, $m); // size m+1, sentinel at m
        }

        // helper functions (closures) for find with path compression
        $findRow = function (&$rowNext, $i, $j) use (&$findRow) {
            while ($rowNext[$i][$j] != $j) {
                $rowNext[$i][$j] = $rowNext[$i][$rowNext[$i][$j]];
                $j = $rowNext[$i][$j];
            }
            return $j;
        };
        $findCol = function (&$colNext, $j, $i) use (&$findCol) {
            while ($colNext[$j][$i] != $i) {
                $colNext[$j][$i] = $colNext[$j][$colNext[$j][$i]];
                $i = $colNext[$j][$i];
            }
            return $i;
        };

        $queue = new SplQueue();
        $dist[0][0] = 1;
        $queue->enqueue([0, 0]);

        // remove start cell from DSU structures
        $rowNext[0][0] = $findRow($rowNext, 0, 1);
        $colNext[0][0] = $findCol($colNext, 0, 1);

        while (!$queue->isEmpty()) {
            [$i, $j] = $queue->dequeue();
            $d = $dist[$i][$j];
            if ($i == $m - 1 && $j == $n - 1) {
                return $d;
            }
            $step = $grid[$i][$j];

            // Move right
            $rightLimit = min($n - 1, $j + $step);
            $col = $findRow($rowNext, $i, $j + 1);
            while ($col <= $rightLimit) {
                $dist[$i][$col] = $d + 1;
                $queue->enqueue([$i, $col]);

                // remove from row set
                $nextCol = $findRow($rowNext, $i, $col + 1);
                $rowNext[$i][$col] = $nextCol;

                // also remove from column set
                $nextRowInCol = $findCol($colNext, $col, $i + 1);
                $colNext[$col][$i] = $nextRowInCol;

                $col = $nextCol;
            }

            // Move down
            $downLimit = min($m - 1, $i + $step);
            $rowIdx = $findCol($colNext, $j, $i + 1);
            while ($rowIdx <= $downLimit) {
                $dist[$rowIdx][$j] = $d + 1;
                $queue->enqueue([$rowIdx, $j]);

                // remove from column set
                $nextRow = $findCol($colNext, $j, $rowIdx + 1);
                $colNext[$j][$rowIdx] = $nextRow;

                // also remove from row set
                $nextColInRow = $findRow($rowNext, $rowIdx, $j + 1);
                $rowNext[$rowIdx][$j] = $nextColInRow;

                $rowIdx = $nextRow;
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumVisitedCells(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        if m == 1 && n == 1 { return 1 }
        
        var rowNext = Array(repeating: [Int](), count: m)
        for i in 0..<m {
            rowNext[i] = Array(0...n)   // size n+1, sentinel at n
        }
        var colNext = Array(repeating: [Int](), count: n)
        for j in 0..<n {
            colNext[j] = Array(0...m)   // size m+1, sentinel at m
        }
        
        func findRow(_ i: Int, _ x: Int) -> Int {
            if rowNext[i][x] == x { return x }
            let r = findRow(i, rowNext[i][x])
            rowNext[i][x] = r
            return r
        }
        func findCol(_ j: Int, _ x: Int) -> Int {
            if colNext[j][x] == x { return x }
            let r = findCol(j, colNext[j][x])
            colNext[j][x] = r
            return r
        }
        
        var visited = [Bool](repeating: false, count: m * n)
        var dist = [Int](repeating: 0, count: m * n)
        var queue: [(Int, Int)] = []
        var head = 0
        
        visited[0] = true
        dist[0] = 1
        queue.append((0, 0))
        
        while head < queue.count {
            let (i, j) = queue[head]
            head += 1
            let curDist = dist[i * n + j]
            if i == m - 1 && j == n - 1 { return curDist }
            let limit = grid[i][j]
            
            // move right in the same row
            var col = findRow(i, j + 1)
            while col < n && col <= j + limit {
                let idx = i * n + col
                if !visited[idx] {
                    visited[idx] = true
                    dist[idx] = curDist + 1
                    queue.append((i, col))
                }
                // remove this column from row set
                rowNext[i][col] = findRow(i, col + 1)
                // also remove the cell from its column set
                colNext[col][i] = findCol(col, i + 1)
                col = findRow(i, col)   // next unvisited column in this row
            }
            
            // move down in the same column
            var row = findCol(j, i + 1)
            while row < m && row <= i + limit {
                let idx = row * n + j
                if !visited[idx] {
                    visited[idx] = true
                    dist[idx] = curDist + 1
                    queue.append((row, j))
                }
                // remove this row from column set
                colNext[j][row] = findCol(j, row + 1)
                // also remove the cell from its row set
                rowNext[row][j] = findRow(row, j + 1)
                row = findCol(j, row)   // next unvisited row in this column
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumVisitedCells(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        if (m == 1 && n == 1) return 1

        // distance array, -1 means unvisited
        val dist = Array(m) { IntArray(n) { -1 } }

        // sets of unvisited columns for each row and rows for each column
        val rowSets = Array(m) { java.util.TreeSet<Int>() }
        for (i in 0 until m) {
            for (j in 0 until n) rowSets[i].add(j)
        }
        val colSets = Array(n) { java.util.TreeSet<Int>() }
        for (j in 0 until n) {
            for (i in 0 until m) colSets[j].add(i)
        }

        val q: java.util.ArrayDeque<Pair<Int, Int>> = java.util.ArrayDeque()
        dist[0][0] = 1
        q.add(Pair(0, 0))
        rowSets[0].remove(0)
        colSets[0].remove(0)

        while (q.isNotEmpty()) {
            val (i, j) = q.removeFirst()
            val steps = grid[i][j]

            // explore right moves in the same row
            var nextCol: Int? = rowSets[i].higher(j)
            while (nextCol != null && nextCol <= j + steps) {
                // mark visited and enqueue
                rowSets[i].remove(nextCol)
                colSets[nextCol]!!.remove(i)
                dist[i][nextCol] = dist[i][j] + 1
                if (i == m - 1 && nextCol == n - 1) return dist[i][nextCol]
                q.add(Pair(i, nextCol))
                // get the next candidate
                nextCol = rowSets[i].higher(nextCol)
            }

            // explore down moves in the same column
            var nextRow: Int? = colSets[j].higher(i)
            while (nextRow != null && nextRow <= i + steps) {
                colSets[j].remove(nextRow)
                rowSets[nextRow]!!.remove(j)
                dist[nextRow][j] = dist[i][j] + 1
                if (nextRow == m - 1 && j == n - 1) return dist[nextRow][j]
                q.add(Pair(nextRow, j))
                nextRow = colSets[j].higher(nextRow)
            }
        }

        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minimumVisitedCells(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // distance matrix, 0 means unvisited
    List<List<int>> dist = List.generate(m, (_) => List.filled(n, 0));

    // DSU parents for rows (next column) and columns (next row)
    List<List<int>> rowParent =
        List.generate(m, (_) => List.filled(n + 1, 0));
    List<List<int>> colParent =
        List.generate(n, (_) => List.filled(m + 1, 0));

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j <= n; ++j) rowParent[i][j] = j;
    }
    for (int j = 0; j < n; ++j) {
      for (int i = 0; i <= m; ++i) colParent[j][i] = i;
    }

    // iterative find with path compression
    int findRow(int i, int x) {
      var parent = rowParent[i];
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    }

    int findCol(int j, int x) {
      var parent = colParent[j];
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    }

    // BFS queue
    List<int> qx = [];
    List<int> qy = [];
    int head = 0;

    dist[0][0] = 1;
    qx.add(0);
    qy.add(0);

    // remove start cell from DSU structures
    rowParent[0][0] = 1;
    colParent[0][0] = 1;

    while (head < qx.length) {
      int i = qx[head];
      int j = qy[head];
      head++;

      if (i == m - 1 && j == n - 1) return dist[i][j];

      int step = grid[i][j];

      // move right
      int startCol = j + 1;
      int endCol = j + step;
      if (endCol >= n) endCol = n - 1;
      while (true) {
        int colIdx = findRow(i, startCol);
        if (colIdx > endCol) break;

        dist[i][colIdx] = dist[i][j] + 1;
        qx.add(i);
        qy.add(colIdx);

        // remove from row DSU
        rowParent[i][colIdx] = colIdx + 1;
        // remove from column DSU
        colParent[colIdx][i] = i + 1;

        // next search starts from same colIdx (now points to next)
        startCol = colIdx; // findRow will move forward on next iteration
      }

      // move down
      int startRow = i + 1;
      int endRow = i + step;
      if (endRow >= m) endRow = m - 1;
      while (true) {
        int rowIdx = findCol(j, startRow);
        if (rowIdx > endRow) break;

        dist[rowIdx][j] = dist[i][j] + 1;
        qx.add(rowIdx);
        qy.add(j);

        // remove from column DSU
        colParent[j][rowIdx] = rowIdx + 1;
        // remove from row DSU
        rowParent[rowIdx][j] = j + 1;

        startRow = rowIdx; // advance for next iteration
      }
    }

    return -1;
  }
}
```

## Golang

```go
func minimumVisitedCells(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])

    // distance array, 0 means unvisited
    dist := make([][]int, m)
    for i := range dist {
        dist[i] = make([]int, n)
    }

    // DSU for next unvisited column in each row
    rowNext := make([][]int, m)
    for i := 0; i < m; i++ {
        rowNext[i] = make([]int, n+1) // sentinel at n
        for j := 0; j <= n; j++ {
            rowNext[i][j] = j
        }
    }

    // DSU for next unvisited row in each column
    colNext := make([][]int, n)
    for j := 0; j < n; j++ {
        colNext[j] = make([]int, m+1) // sentinel at m
        for i := 0; i <= m; i++ {
            colNext[j][i] = i
        }
    }

    var findRow func(int, int) int
    findRow = func(r, x int) int {
        parent := rowNext[r]
        for parent[x] != x {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    var findCol func(int, int) int
    findCol = func(c, x int) int {
        parent := colNext[c]
        for parent[x] != x {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    type pair struct{ i, j int }
    q := make([]pair, 0, m*n)
    head := 0

    // start cell
    dist[0][0] = 1
    q = append(q, pair{0, 0})
    // mark visited in DSUs
    rowNext[0][0] = findRow(0, 1)
    colNext[0][0] = findCol(0, 1)

    for head < len(q) {
        cur := q[head]
        head++
        d := dist[cur.i][cur.j]

        if cur.i == m-1 && cur.j == n-1 {
            return d
        }

        step := grid[cur.i][cur.j]

        // move right in the same row
        startCol := cur.j + 1
        endCol := cur.j + step
        if endCol >= n {
            endCol = n - 1
        }
        colIdx := findRow(cur.i, startCol)
        for colIdx <= endCol {
            dist[cur.i][colIdx] = d + 1
            q = append(q, pair{cur.i, colIdx})

            // remove from row DSU
            rowNext[cur.i][colIdx] = findRow(cur.i, colIdx+1)
            // remove from column DSU
            colNext[colIdx][cur.i] = findCol(colIdx, cur.i+1)

            colIdx = findRow(cur.i, colIdx) // next unvisited in this row
        }

        // move down in the same column
        startRow := cur.i + 1
        endRow := cur.i + step
        if endRow >= m {
            endRow = m - 1
        }
        rowIdx := findCol(cur.j, startRow)
        for rowIdx <= endRow {
            dist[rowIdx][cur.j] = d + 1
            q = append(q, pair{rowIdx, cur.j})

            // remove from column DSU
            colNext[cur.j][rowIdx] = findCol(cur.j, rowIdx+1)
            // remove from row DSU
            rowNext[rowIdx][cur.j] = findRow(rowIdx, cur.j+1)

            rowIdx = findCol(cur.j, rowIdx) // next unvisited in this column
        }
    }

    return -1
}
```

## Ruby

```ruby
def minimum_visited_cells(grid)
  m = grid.length
  n = grid[0].length

  # distance matrix, -1 means unvisited
  dist = Array.new(m) { Array.new(n, -1) }

  # DSU for rows: each row has columns 0..n (n is sentinel)
  row_parent = Array.new(m) { Array.new(n + 1) { |i| i } }
  # DSU for columns: each column has rows 0..m (m is sentinel)
  col_parent = Array.new(n) { Array.new(m + 1) { |i| i } }

  # find with path compression for row
  row_find = lambda do |par, x|
    while par[x] != x
      par[x] = par[par[x]]
      x = par[x]
    end
    x
  end

  # find with path compression for column
  col_find = lambda do |par, x|
    while par[x] != x
      par[x] = par[par[x]]
      x = par[x]
    end
    x
  end

  # initialize BFS
  queue = [[0, 0]]
  head = 0
  dist[0][0] = 1

  # mark start cell as visited in both DSUs
  row_parent[0][0] = row_find.call(row_parent[0], 1)
  col_parent[0][0] = col_find.call(col_parent[0], 1)

  while head < queue.length
    i, j = queue[head]
    head += 1
    d = dist[i][j]
    step = grid[i][j]

    # move right within the same row
    max_col = [n - 1, j + step].min
    col = row_find.call(row_parent[i], j + 1)
    while col <= max_col
      dist[i][col] = d + 1
      queue << [i, col]

      # remove (i,col) from row DSU
      row_parent[i][col] = row_find.call(row_parent[i], col + 1)
      # also remove from column DSU
      col_parent[col][i] = col_find.call(col_parent[col], i + 1)

      col = row_find.call(row_parent[i], col)
    end

    # move down within the same column
    max_row = [m - 1, i + step].min
    row_idx = col_find.call(col_parent[j], i + 1)
    while row_idx <= max_row
      dist[row_idx][j] = d + 1
      queue << [row_idx, j]

      # remove (row_idx,j) from column DSU
      col_parent[j][row_idx] = col_find.call(col_parent[j], row_idx + 1)
      # also remove from row DSU
      row_parent[row_idx][j] = row_find.call(row_parent[row_idx], j + 1)

      row_idx = col_find.call(col_parent[j], row_idx)
    end
  end

  dist[m - 1][n - 1]
end
```

## Scala

```scala
import java.util.{ArrayDeque, TreeSet}

object Solution {
  def minimumVisitedCells(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length

    // Sets of unvisited columns for each row and rows for each column
    val rowSets = Array.fill(m)(new TreeSet[Int]())
    var i = 0
    while (i < m) {
      var c = 0
      while (c < n) {
        rowSets(i).add(c)
        c += 1
      }
      i += 1
    }

    val colSets = Array.fill(n)(new TreeSet[Int]())
    var j = 0
    while (j < n) {
      var r = 0
      while (r < m) {
        colSets(j).add(r)
        r += 1
      }
      j += 1
    }

    val dist = Array.fill(m, n)(-1)
    val q: ArrayDeque[(Int, Int)] = new ArrayDeque[(Int, Int)]()

    dist(0)(0) = 1
    q.add((0, 0))
    rowSets(0).remove(0)
    colSets(0).remove(0)

    while (!q.isEmpty) {
      val (x, y) = q.poll()
      if (x == m - 1 && y == n - 1) return dist(x)(y)

      val limit = grid(x)(y)

      // Move right in the same row
      var col = rowSets(x).ceiling(y + 1)
      while (col != null && col <= y + limit) {
        dist(x)(col) = dist(x)(y) + 1
        q.add((x, col))
        rowSets(x).remove(col)
        colSets(col).remove(x)
        col = rowSets(x).ceiling(y + 1)
      }

      // Move down in the same column
      var row = colSets(y).ceiling(x + 1)
      while (row != null && row <= x + limit) {
        dist(row)(y) = dist(x)(y) + 1
        q.add((row, y))
        rowSets(row).remove(y)
        colSets(y).remove(row)
        row = colSets(y).ceiling(x + 1)
      }
    }

    -1
  }
}
```

## Rust

```rust
use std::collections::{BTreeSet, VecDeque};
use std::ops::Bound::{Excluded, Included};

impl Solution {
    pub fn minimum_visited_cells(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        // sets of unvisited positions for each row and column
        let mut row_sets: Vec<BTreeSet<usize>> = (0..m).map(|_| BTreeSet::new()).collect();
        let mut col_sets: Vec<BTreeSet<usize>> = (0..n).map(|_| BTreeSet::new()).collect();

        for i in 0..m {
            for j in 0..n {
                row_sets[i].insert(j);
                col_sets[j].insert(i);
            }
        }

        let mut dist = vec![vec![-1i32; n]; m];
        let mut q = VecDeque::new();

        // start cell
        dist[0][0] = 1;
        q.push_back((0usize, 0usize));
        row_sets[0].remove(&0);
        col_sets[0].remove(&0);

        while let Some((i, j)) = q.pop_front() {
            let d = dist[i][j];
            if i == m - 1 && j == n - 1 {
                return d;
            }

            // move right
            let max_right = std::cmp::min(n - 1, j + grid[i][j] as usize);
            loop {
                let next_col_opt = row_sets[i]
                    .range((Excluded(j), Included(max_right)))
                    .next()
                    .cloned();
                match next_col_opt {
                    Some(c) => {
                        row_sets[i].remove(&c);
                        col_sets[c].remove(&i);
                        dist[i][c] = d + 1;
                        q.push_back((i, c));
                    }
                    None => break,
                }
            }

            // move down
            let max_down = std::cmp::min(m - 1, i + grid[i][j] as usize);
            loop {
                let next_row_opt = col_sets[j]
                    .range((Excluded(i), Included(max_down)))
                    .next()
                    .cloned();
                match next_row_opt {
                    Some(r) => {
                        col_sets[j].remove(&r);
                        row_sets[r].remove(&j);
                        dist[r][j] = d + 1;
                        q.push_back((r, j));
                    }
                    None => break,
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
(define/contract (minimum-visited-cells grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (first grid))))
         (total (* m n))
         (row-next (make-vector (* m (+ n 1)) -1))
         (col-next (make-vector (* n (+ m 1)) -1))
         (visited (make-vector total #f))
         (dist (make-vector total -1))
         (queue (make-vector total))
         (head 0)
         (tail 0))

    ;; initialise next pointers
    (for ([i (in-range m)])
      (let ((base (* i (+ n 1))))
        (for ([j (in-range (+ n 1))])
          (vector-set! row-next (+ base j) j))))
    (for ([j (in-range n)])
      (let ((base (* j (+ m 1))))
        (for ([i (in-range (+ m 1))])
          (vector-set! col-next (+ base i) i))))

    ;; find functions with path compression
    (define (find-row i j)
      (if (>= j n)
          j
          (let* ((base (* i (+ n 1)))
                 (p (vector-ref row-next (+ base j))))
            (if (= p j)
                j
                (let ((rep (find-row i p)))
                  (vector-set! row-next (+ base j) rep)
                  rep)))))
    (define (remove-row i j)
      (let* ((base (* i (+ n 1)))
             (next (find-row i (+ j 1))))
        (vector-set! row-next (+ base j) next)))

    (define (find-col j i)
      (if (>= i m)
          i
          (let* ((base (* j (+ m 1)))
                 (p (vector-ref col-next (+ base i))))
            (if (= p i)
                i
                (let ((rep (find-col j p)))
                  (vector-set! col-next (+ base i) rep)
                  rep)))))
    (define (remove-col j i)
      (let* ((base (* j (+ m 1)))
             (next (find-col j (+ i 1))))
        (vector-set! col-next (+ base i) next)))

    ;; start cell
    (when (> total 0)
      (vector-set! visited 0 #t)
      (vector-set! dist 0 1)
      (vector-set! queue tail 0)
      (set! tail (+ tail 1))
      (remove-row 0 0)
      (remove-col 0 0))

    ;; BFS
    (let bfs ()
      (when (< head tail)
        (define cur (vector-ref queue head))
        (set! head (+ head 1))
        (define i (quotient cur n))
        (define j (remainder cur n))
        (define steps (list-ref (list-ref grid i) j))

        ;; move right in the same row
        (let loop ((col (find-row i (+ j 1))))
          (when (and (< col n) (<= col (+ j steps)))
            (define nid (+ (* i n) col))
            (unless (vector-ref visited nid)
              (vector-set! visited nid #t)
              (vector-set! dist nid (+ 1 (vector-ref dist cur)))
              (vector-set! queue tail nid)
              (set! tail (+ tail 1))
              (remove-row i col)
              (remove-col col i))
            (loop (find-row i (+ col 1)))))

        ;; move down in the same column
        (let loop ((row (find-col j (+ i 1))))
          (when (and (< row m) (<= row (+ i steps)))
            (define nid (+ (* row n) j))
            (unless (vector-ref visited nid)
              (vector-set! visited nid #t)
              (vector-set! dist nid (+ 1 (vector-ref dist cur)))
              (vector-set! queue tail nid)
              (set! tail (+ tail 1))
              (remove-col j row)
              (remove-row row j))
            (loop (find-col j (+ row 1)))))

        (bfs))))

    (if (and (> total 0) (vector-ref visited (- total 1)))
        (vector-ref dist (- total 1))
        -1)))
```

## Erlang

```erlang
-spec minimum_visited_cells(Grid :: [[integer()]]) -> integer().
minimum_visited_cells(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    case {M, N} of
        {1, 1} -> 1;
        _ ->
            % convert grid to tuple of tuples for O(1) access
            GridTuples = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
            RowMap0 = init_row_map(M, N),
            ColMap0 = init_col_map(N, M),
            {RowMap1, ColMap1} = remove_cell(RowMap0, ColMap0, 0, 0),
            Q0 = queue:in({0, 0, 1}, queue:new()),
            bfs(Q0, GridTuples, M, N, RowMap1, ColMap1)
    end.

%% BFS loop
bfs(Q, _Grid, M, N, _RowMap, _ColMap) when queue:is_empty(Q) ->
    -1;
bfs(Q, Grid, M, N, RowMap, ColMap) ->
    {{value, {I, J, D}}, QRest} = queue:out(Q),
    if I == M-1, J == N-1 ->
            D;
       true ->
            Jump = element(J + 1, element(I + 1, Grid)),
            MaxRight = erlang:min(N - 1, J + Jump),
            MaxDown  = erlang:min(M - 1, I + Jump),

            {RowNeighbors, RowMap1} = collect_row_neighbors(I, J + 1, MaxRight, RowMap),
            {ColNeighbors, ColMap1} = collect_col_neighbors(J, I + 1, MaxDown, ColMap),

            AllNeighbors = RowNeighbors ++ ColNeighbors,

            {FinalRowMap, FinalColMap, NewQ} =
                lists:foldl(
                    fun({Ni, Nj}, {RM, CM, QAcc}) ->
                        RM1 = delete_from_row(RM, Ni, Nj),
                        CM1 = delete_from_col(CM, Nj, Ni),
                        {RM1, CM1, queue:in({Ni, Nj, D + 1}, QAcc)}
                    end,
                    {RowMap1, ColMap1, QRest},
                    AllNeighbors),

            bfs(NewQ, Grid, M, N, FinalRowMap, FinalColMap)
    end.

%% Initialize row map: each row -> tree of all column indices
init_row_map(M, N) ->
    lists:foldl(
        fun(I, Acc) ->
            Tree = build_tree(0, N - 1),
            maps:put(I, Tree, Acc)
        end,
        #{},
        lists:seq(0, M - 1)).

%% Initialize column map: each column -> tree of all row indices
init_col_map(N, M) ->
    lists:foldl(
        fun(J, Acc) ->
            Tree = build_tree(0, M - 1),
            maps:put(J, Tree, Acc)
        end,
        #{},
        lists:seq(0, N - 1)).

%% Build a gb_tree containing keys from Low to High (inclusive)
build_tree(Low, High) when Low > High ->
    gb_trees:empty();
build_tree(Low, High) ->
    lists:foldl(
        fun(K, T) -> gb_trees:insert(K, true, T) end,
        gb_trees:empty(),
        lists:seq(Low, High)).

%% Remove a cell from both row and column maps
remove_cell(RowMap, ColMap, I, J) ->
    {delete_from_row(RowMap, I, J), delete_from_col(ColMap, J, I)}.

%% Delete entry (I,J) from row map
delete_from_row(RowMap, I, J) ->
    Tree = maps:get(I, RowMap),
    NewTree = gb_trees:delete_any(J, Tree),
    maps:put(I, NewTree, RowMap).

%% Delete entry (J,I) from column map
delete_from_col(ColMap, J, I) ->
    Tree = maps:get(J, ColMap),
    NewTree = gb_trees:delete_any(I, Tree),
    maps:put(J, NewTree, ColMap).

%% Collect unvisited columns in row I within [From, To]
collect_row_neighbors(I, From, To, RowMap) when From > To ->
    {[], RowMap};
collect_row_neighbors(I, From, To, RowMap) ->
    Tree = maps:get(I, RowMap),
    {Cols, NewTree} = collect_keys_in_range(Tree, From, To, []),
    Positions = [{I, C} || C <- Cols],
    UpdatedRowMap = maps:put(I, NewTree, RowMap),
    {Positions, UpdatedRowMap}.

%% Collect unvisited rows in column J within [From, To]
collect_col_neighbors(J, From, To, ColMap) when From > To ->
    {[], ColMap};
collect_col_neighbors(J, From, To, ColMap) ->
    Tree = maps:get(J, ColMap),
    {Rows, NewTree} = collect_keys_in_range(Tree, From, To, []),
    Positions = [{R, J} || R <- Rows],
    UpdatedColMap = maps:put(J, NewTree, ColMap),
    {Positions, UpdatedColMap}.

%% Helper to collect keys in [Low, High] from a gb_tree and delete them
collect_keys_in_range(Tree, Low, High, Acc) ->
    case gb_trees:iterator_from(Low, Tree) of
        none ->
            {lists:reverse(Acc), Tree};
        {Key, _Val, _Iter} when Key =< High ->
            Tree1 = gb_trees:delete(Key, Tree),
            collect_keys_in_range(Tree1, Key + 1, High, [Key | Acc]);
        _Other ->
            {lists:reverse(Acc), Tree}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_visited_cells(grid :: [[integer]]) :: integer
  def minimum_visited_cells(grid) do
    m = length(grid)
    n = length(hd(grid))
    total = m * n

    # Convert grid to array of arrays for O(1) access
    grid_rows =
      Enum.map(grid, fn row -> :array.from_list(row) end)

    grid_arr = :array.from_list(grid_rows)

    start_idx = 0
    dist_arr = :array.new(total, default: -1)
    dist_arr = :array.set(start_idx, 1, dist_arr)

    row_arr = build_row_array(m, n)
    col_arr = build_col_array(m, n)

    # Remove start cell from row and column sets
    row_tree0 = :array.get(0, row_arr) |> :gb_trees.delete(0)
    row_arr = :array.set(0, row_tree0, row_arr)

    col_tree0 = :array.get(0, col_arr) |> :gb_trees.delete(0)
    col_arr = :array.set(0, col_tree0, col_arr)

    q = :queue.in({0, 0}, :queue.new())
    bfs(q, m, n, grid_arr, row_arr, col_arr, dist_arr)
  end

  defp bfs(queue, m, n, grid_arr, row_arr, col_arr, dist_arr) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {i, j}}, q2} ->
        cur_dist = :array.get(i * n + j, dist_arr)

        if i == m - 1 and j == n - 1 do
          cur_dist
        else
          val = :array.get(j, :array.get(i, grid_arr))

          {row_arr, col_arr, q3, dist_arr} =
            process_row(i, j, val, cur_dist, m, n, row_arr, col_arr, q2, dist_arr)

          {row_arr, col_arr, q4, dist_arr} =
            process_col(i, j, val, cur_dist, m, n, row_arr, col_arr, q3, dist_arr)

          bfs(q4, m, n, grid_arr, row_arr, col_arr, dist_arr)
        end
    end
  end

  defp process_row(i, j, val, cur_dist, _m, n, row_arr, col_arr, queue, dist_arr) do
    max_col = min(n - 1, j + val)

    if max_col > j do
      row_tree = :array.get(i, row_arr)
      keys = range_keys(row_tree, j + 1, max_col)

      {row_tree_updated, col_arr2, queue2, dist_arr2} =
        Enum.reduce(keys, {row_tree, col_arr, queue, dist_arr}, fn k,
                                                                 {rt, ca, qacc, da} ->
          idx = i * n + k
          da = :array.set(idx, cur_dist + 1, da)
          qacc = :queue.in({i, k}, qacc)

          col_tree = :array.get(k, ca) |> :gb_trees.delete(i)
          ca = :array.set(k, col_tree, ca)

          {rt, ca, qacc, da}
        end)

      # delete processed keys from row tree
      rt_final =
        Enum.reduce(keys, row_tree_updated, fn key, acc -> :gb_trees.delete(key, acc) end)

      row_arr = :array.set(i, rt_final, row_arr)
      {row_arr, col_arr2, queue2, dist_arr2}
    else
      {row_arr, col_arr, queue, dist_arr}
    end
  end

  defp process_col(i, j, val, cur_dist, m, _n, row_arr, col_arr, queue, dist_arr) do
    max_row = min(m - 1, i + val)

    if max_row > i do
      col_tree = :array.get(j, col_arr)
      keys = range_keys(col_tree, i + 1, max_row)

      {col_tree_updated, row_arr2, queue2, dist_arr2} =
        Enum.reduce(keys, {col_tree, row_arr, queue, dist_arr}, fn r,
                                                                 {ct, ra, qacc, da} ->
          idx = r * (length(row_arr) |> :array.size()) + j
          da = :array.set(idx, cur_dist + 1, da)
          qacc = :queue.in({r, j}, qacc)

          row_tree = :array.get(r, ra) |> :gb_trees.delete(j)
          ra = :array.set(r, row_tree, ra)

          {ct, ra, qacc, da}
        end)

      ct_final =
        Enum.reduce(keys, col_tree_updated, fn key, acc -> :gb_trees.delete(key, acc) end)

      col_arr = :array.set(j, ct_final, col_arr)
      {row_arr2, col_arr, queue2, dist_arr2}
    else
      {row_arr, col_arr, queue, dist_arr}
    end
  end

  defp build_row_array(m, n) do
    Enum.reduce(0..(m - 1), :array.new(m, default: nil), fn i, acc ->
      tree = Enum.reduce(0..(n - 1), :gb_trees.empty(), fn col, t -> :gb_trees.insert(col, true, t) end)
      :array.set(i, tree, acc)
    end)
  end

  defp build_col_array(m, n) do
    Enum.reduce(0..(n - 1), :array.new(n, default: nil), fn j, acc ->
      tree = Enum.reduce(0..(m - 1), :gb_trees.empty(), fn row, t -> :gb_trees.insert(row, true, t) end)
      :array.set(j, tree, acc)
    end)
  end

  defp range_keys(tree, low, high) do
    iter = :gb_trees.iterator_from(low, tree)
    collect_keys(iter, high, [])
  end

  defp collect_keys(nil, _high, acc), do: Enum.reverse(acc)

  defp collect_keys({key, _, next_iter} = it, high, acc) when key <= high do
    collect_keys(:gb_trees.next(it), high, [key | acc])
  end

  defp collect_keys(_it, _high, acc), do: Enum.reverse(acc)
end
```

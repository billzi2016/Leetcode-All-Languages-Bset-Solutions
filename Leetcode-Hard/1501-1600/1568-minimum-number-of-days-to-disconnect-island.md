# 1568. Minimum Number of Days to Disconnect Island

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int m, n;
    vector<vector<int>> dirs{{1,0},{-1,0},{0,1},{0,-1}};
    
    void dfsCount(int r, int c, vector<vector<int>>& grid, vector<vector<bool>>& vis) {
        vis[r][c] = true;
        for (auto &d: dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr>=0 && nr<m && nc>=0 && nc<n && !vis[nr][nc] && grid[nr][nc]==1)
                dfsCount(nr,nc,grid,vis);
        }
    }
    
    int countIslands(const vector<vector<int>>& grid) {
        vector<vector<bool>> vis(m, vector<bool>(n,false));
        int cnt = 0;
        for (int i=0;i<m;++i){
            for (int j=0;j<n;++j){
                if (!vis[i][j] && grid[i][j]==1){
                    ++cnt;
                    // use stack to avoid recursion depth issues
                    dfsCount(i,j,const_cast<vector<vector<int>>&>(grid),vis);
                }
            }
        }
        return cnt;
    }
    
    bool hasArticulation = false;
    vector<vector<int>> disc, low;
    int timer = 0;
    
    void tarjan(int r, int c, int pr, int pc, const vector<vector<int>>& grid) {
        disc[r][c] = low[r][c] = ++timer;
        int children = 0;
        for (auto &d: dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr<0||nr>=m||nc<0||nc>=n||grid[nr][nc]==0) continue;
            if (disc[nr][nc]==0) { // unvisited
                ++children;
                tarjan(nr,nc,r,c,grid);
                low[r][c] = min(low[r][c], low[nr][nc]);
                if (pr!=-1 && low[nr][nc] >= disc[r][c])
                    hasArticulation = true;
            } else if (!(nr==pr && nc==pc)) {
                low[r][c] = min(low[r][c], disc[nr][nc]);
            }
        }
        if (pr==-1 && children > 1)
            hasArticulation = true;
    }
    
    int minDays(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        
        // check initial connectivity
        if (countIslands(grid) != 1) return 0;
        
        // count land cells
        int landCnt = 0;
        int sr=-1, sc=-1;
        for (int i=0;i<m;++i){
            for (int j=0;j<n;++j){
                if (grid[i][j]==1){
                    ++landCnt;
                    sr=i; sc=j;
                }
            }
        }
        if (landCnt <= 1) return 1; // removing the only cell disconnects
        
        disc.assign(m, vector<int>(n,0));
        low.assign(m, vector<int>(n,0));
        timer = 0;
        hasArticulation = false;
        
        tarjan(sr, sc, -1, -1, grid);
        return hasArticulation ? 1 : 2;
    }
};
```

## Java

```java
class Solution {
    private int rows;
    private int cols;
    private int[][] grid;
    private int time;
    private boolean hasArticulation;
    private int[][] disc;
    private int[][] low;
    private final int[] dr = {1, -1, 0, 0};
    private final int[] dc = {0, 0, 1, -1};

    public int minDays(int[][] grid) {
        this.grid = grid;
        rows = grid.length;
        cols = grid[0].length;

        boolean[][] visited = new boolean[rows][cols];
        int islands = 0;
        int totalLand = 0;
        int startR = -1, startC = -1;

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 1) {
                    totalLand++;
                    if (!visited[r][c]) {
                        islands++;
                        startR = r;
                        startC = c;
                        dfsCount(r, c, visited);
                    }
                }
            }
        }

        // Already disconnected or no land
        if (islands != 1) return 0;

        // Only one land cell
        if (totalLand == 1) return 1;

        // Check for articulation point using Tarjan's algorithm
        disc = new int[rows][cols];
        low = new int[rows][cols];
        time = 0;
        hasArticulation = false;
        dfsTarjan(startR, startC, -1);
        return hasArticulation ? 1 : 2;
    }

    private void dfsCount(int r, int c, boolean[][] visited) {
        visited[r][c] = true;
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                grid[nr][nc] == 1 && !visited[nr][nc]) {
                dfsCount(nr, nc, visited);
            }
        }
    }

    private void dfsTarjan(int r, int c, int parentId) {
        disc[r][c] = low[r][c] = ++time;
        int children = 0;
        int curId = r * cols + c;

        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == 0)
                continue;
            int nid = nr * cols + nc;
            if (disc[nr][nc] == 0) {
                children++;
                dfsTarjan(nr, nc, curId);
                low[r][c] = Math.min(low[r][c], low[nr][nc]);

                // Non-root articulation point
                if (parentId != -1 && low[nr][nc] >= disc[r][c]) {
                    hasArticulation = true;
                }
            } else if (nid != parentId) { // back edge
                low[r][c] = Math.min(low[r][c], disc[nr][nc]);
            }
        }

        // Root articulation point
        if (parentId == -1 && children > 1) {
            hasArticulation = true;
        }
    }
}
```

## Python

```python
class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def count_islands(g):
            visited = [[False] * n for _ in range(m)]
            islands = 0
            for i in range(m):
                for j in range(n):
                    if g[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        stack = [(i, j)]
                        visited[i][j] = True
                        while stack:
                            x, y = stack.pop()
                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n and g[nx][ny] == 1 and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    stack.append((nx, ny))
            return islands

        # If already disconnected (0 or >1 islands)
        if count_islands(grid) != 1:
            return 0

        # Try removing each land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands(grid) != 1:
                        grid[i][j] = 1
                        return 1
                    grid[i][j] = 1

        # Otherwise, need at most two days
        return 2
```

## Python3

```python
from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r: int, c: int, visited: List[List[bool]]) -> None:
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 1:
                        stack.append((nx, ny))

        def count_islands() -> int:
            visited = [[False] * cols for _ in range(rows)]
            cnt = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and not visited[i][j]:
                        cnt += 1
                        dfs(i, j, visited)
            return cnt

        initial = count_islands()
        if initial == 0 or initial > 1:
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        grid[i][j] = 1
                        return 1
                    grid[i][j] = 1

        return 2
```

## C

```c
#include <stdlib.h>

static int rows, cols;
static int **g;
static int *discArr;
static int *lowArr;
static int *parentArr;
static int articulationFound;

static const int dr[4] = {-1, 0, 1, 0};
static const int dc[4] = {0, 1, 0, -1};

static inline int idx(int r, int c) {
    return r * cols + c;
}

static int isLand(int r, int c) {
    return (r >= 0 && r < rows && c >= 0 && c < cols && g[r][c] == 1);
}

/* DFS for Tarjan articulation points */
static void dfs(int r, int c, int *timePtr) {
    int cur = idx(r, c);
    discArr[cur] = lowArr[cur] = (*timePtr)++;
    int children = 0;

    for (int k = 0; k < 4; ++k) {
        int nr = r + dr[k];
        int nc = c + dc[k];
        if (!isLand(nr, nc)) continue;
        int nxt = idx(nr, nc);
        if (discArr[nxt] == -1) {               // tree edge
            parentArr[nxt] = cur;
            ++children;
            dfs(nr, nc, timePtr);
            if (lowArr[nxt] < lowArr[cur]) lowArr[cur] = lowArr[nxt];
            if (parentArr[cur] != -1 && lowArr[nxt] >= discArr[cur])
                articulationFound = 1;
        } else if (nxt != parentArr[cur]) {    // back edge
            if (discArr[nxt] < lowArr[cur]) lowArr[cur] = discArr[nxt];
        }
    }

    if (parentArr[cur] == -1 && children > 1)
        articulationFound = 1;
}

/* Count islands using simple DFS */
static void countDFS(int r, int c, char *vis) {
    int stackSize = rows * cols;
    int *stackR = (int *)malloc(stackSize * sizeof(int));
    int *stackC = (int *)malloc(stackSize * sizeof(int));
    int top = 0;
    stackR[top] = r; stackC[top] = c; ++top;
    vis[idx(r, c)] = 1;

    while (top) {
        --top;
        int cr = stackR[top];
        int cc = stackC[top];
        for (int k = 0; k < 4; ++k) {
            int nr = cr + dr[k];
            int nc = cc + dc[k];
            if (isLand(nr, nc) && !vis[idx(nr, nc)]) {
                vis[idx(nr, nc)] = 1;
                stackR[top] = nr;
                stackC[top] = nc;
                ++top;
            }
        }
    }

    free(stackR);
    free(stackC);
}

/* Main function */
int minDays(int** grid, int gridSize, int* gridColSize) {
    rows = gridSize;
    cols = gridColSize[0];
    g = grid;

    int totalCells = rows * cols;
    char *visited = (char *)calloc(totalCells, sizeof(char));
    int islandCount = 0;
    int landCells = 0;

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (g[r][c] == 1) {
                ++landCells;
                if (!visited[idx(r, c)]) {
                    countDFS(r, c, visited);
                    ++islandCount;
                }
            }
        }
    }

    free(visited);

    if (islandCount != 1) return 0;          // already disconnected
    if (landCells == 1) return 1;           // removing the only land cell

    /* Prepare for Tarjan */
    discArr = (int *)malloc(totalCells * sizeof(int));
    lowArr = (int *)malloc(totalCells * sizeof(int));
    parentArr = (int *)malloc(totalCells * sizeof(int));
    for (int i = 0; i < totalCells; ++i) {
        discArr[i] = -1;
        lowArr[i] = -1;
        parentArr[i] = -1;
    }
    articulationFound = 0;

    int startR = -1, startC = -1;
    for (int r = 0; r < rows && startR == -1; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (g[r][c] == 1) { startR = r; startC = c; break; }
        }
    }

    int time = 0;
    dfs(startR, startC, &time);

    free(discArr);
    free(lowArr);
    free(parentArr);

    return articulationFound ? 1 : 2;
}
```

## Csharp

```csharp
using System;
public class Solution {
    private int rows;
    private int cols;
    private int[][] grid;
    private int[,] disc;
    private int[,] low;
    private int[,] parentIdx;
    private int time;
    private bool hasArticulation;

    private readonly int[] dr = new int[] { 1, -1, 0, 0 };
    private readonly int[] dc = new int[] { 0, 0, 1, -1 };

    public int MinDays(int[][] grid) {
        this.grid = grid;
        rows = grid.Length;
        cols = grid[0].Length;

        int islandCount = CountIslands();
        if (islandCount == 0 || islandCount > 1) return 0;

        int landCells = 0;
        foreach (var row in grid)
            foreach (int cell in row)
                if (cell == 1) landCells++;

        if (landCells <= 1) return 1; // removing the only land makes it disconnected

        disc = new int[rows, cols];
        low = new int[rows, cols];
        parentIdx = new int[rows, cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++) {
                disc[i, j] = -1;
                low[i, j] = -1;
                parentIdx[i, j] = -1;
            }

        time = 0;
        hasArticulation = false;

        // start DFS from any land cell (there is exactly one island)
        bool started = false;
        for (int i = 0; i < rows && !started; i++) {
            for (int j = 0; j < cols && !started; j++) {
                if (grid[i][j] == 1) {
                    Dfs(i, j);
                    started = true;
                }
            }
        }

        return hasArticulation ? 1 : 2;
    }

    private void Dfs(int r, int c) {
        disc[r, c] = time;
        low[r, c] = time;
        time++;
        int children = 0;

        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (!IsValidLand(nr, nc)) continue;

            if (disc[nr, nc] == -1) { // tree edge
                parentIdx[nr, nc] = r * cols + c;
                children++;
                Dfs(nr, nc);
                low[r, c] = Math.Min(low[r, c], low[nr, nc]);

                if (parentIdx[r, c] != -1 && low[nr, nc] >= disc[r, c])
                    hasArticulation = true;
            } else {
                int parentId = parentIdx[r, c];
                int neighborId = nr * cols + nc;
                if (neighborId != parentId) { // back edge
                    low[r, c] = Math.Min(low[r, c], disc[nr, nc]);
                }
            }
        }

        // root articulation check
        if (parentIdx[r, c] == -1 && children > 1)
            hasArticulation = true;
    }

    private bool IsValidLand(int r, int c) {
        return r >= 0 && r < rows && c >= 0 && c < cols && grid[r][c] == 1;
    }

    private int CountIslands() {
        bool[,] visited = new bool[rows, cols];
        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1 && !visited[i, j]) {
                    Explore(i, j, visited);
                    count++;
                }
            }
        }
        return count;
    }

    private void Explore(int r, int c, bool[,] visited) {
        var stack = new System.Collections.Generic.Stack<(int, int)>();
        stack.Push((r, c));
        visited[r, c] = true;
        while (stack.Count > 0) {
            var (cr, cc) = stack.Pop();
            for (int k = 0; k < 4; k++) {
                int nr = cr + dr[k];
                int nc = cc + dc[k];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                    grid[nr][nc] == 1 && !visited[nr, nc]) {
                    visited[nr, nc] = true;
                    stack.Push((nr, nc));
                }
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minDays = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    const countIslands = (g) => {
        const visited = Array.from({length: rows}, () => Array(cols).fill(false));
        let cnt = 0;
        const dfs = (r,c) => {
            const stack = [[r,c]];
            visited[r][c] = true;
            while (stack.length) {
                const [cr, cc] = stack.pop();
                for (const [dr, dc] of dirs) {
                    const nr = cr + dr, nc = cc + dc;
                    if (nr>=0 && nr<rows && nc>=0 && nc<cols &&
                        !visited[nr][nc] && g[nr][nc] === 1) {
                        visited[nr][nc] = true;
                        stack.push([nr,nc]);
                    }
                }
            }
        };
        for (let i=0;i<rows;i++) {
            for (let j=0;j<cols;j++) {
                if (!visited[i][j] && g[i][j] === 1) {
                    cnt++;
                    dfs(i,j);
                }
            }
        }
        return cnt;
    };
    
    const initial = countIslands(grid);
    if (initial !== 1) return 0; // already disconnected or no land
    
    for (let i=0;i<rows;i++) {
        for (let j=0;j<cols;j++) {
            if (grid[i][j] === 1) {
                grid[i][j] = 0;
                const after = countIslands(grid);
                grid[i][j] = 1; // revert
                if (after !== 1) return 1;
            }
        }
    }
    return 2;
};
```

## Typescript

```typescript
function minDays(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]] as const;

    const countIslands = (): number => {
        const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
        let islands = 0;
        const stack: [number, number][] = [];

        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (grid[i][j] === 1 && !visited[i][j]) {
                    islands++;
                    stack.push([i, j]);
                    visited[i][j] = true;
                    while (stack.length) {
                        const [r, c] = stack.pop()!;
                        for (const [dr, dc] of dirs) {
                            const nr = r + dr, nc = c + dc;
                            if (
                                nr >= 0 && nr < m &&
                                nc >= 0 && nc < n &&
                                grid[nr][nc] === 1 && !visited[nr][nc]
                            ) {
                                visited[nr][nc] = true;
                                stack.push([nr, nc]);
                            }
                        }
                    }
                }
            }
        }

        return islands;
    };

    const initial = countIslands();
    if (initial !== 1) return 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                grid[i][j] = 0;
                const after = countIslands();
                grid[i][j] = 1;
                if (after !== 1) return 1;
            }
        }
    }

    return 2;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minDays($grid) {
        $rows = count($grid);
        $cols = $rows ? count($grid[0]) : 0;
        
        // If already disconnected (0 or >1 islands)
        if ($this->countIslands($grid) != 1) {
            return 0;
        }
        
        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] == 1) {
                    // remove this land cell
                    $grid[$i][$j] = 0;
                    if ($this->countIslands($grid) != 1) {
                        return 1;
                    }
                    // revert
                    $grid[$i][$j] = 1;
                }
            }
        }
        return 2;
    }
    
    private function countIslands(&$grid) {
        $rows = count($grid);
        $cols = $rows ? count($grid[0]) : 0;
        $visited = array_fill(0, $rows, array_fill(0, $cols, false));
        $islandCount = 0;
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        
        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] == 1 && !$visited[$i][$j]) {
                    $islandCount++;
                    // DFS stack
                    $stack = [[$i,$j]];
                    $visited[$i][$j] = true;
                    while (!empty($stack)) {
                        [$r,$c] = array_pop($stack);
                        foreach ($dirs as $d) {
                            $nr = $r + $d[0];
                            $nc = $c + $d[1];
                            if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols &&
                                $grid[$nr][$nc] == 1 && !$visited[$nr][$nc]) {
                                $visited[$nr][$nc] = true;
                                $stack[] = [$nr,$nc];
                            }
                        }
                    }
                }
            }
        }
        return $islandCount;
    }
}
```

## Swift

```swift
class Solution {
    func minDays(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        let cols = grid[0].count
        // Helper to count islands in a given grid
        func countIslands(_ g: [[Int]]) -> Int {
            var visited = Array(repeating: Array(repeating: false, count: cols), count: rows)
            var islandCount = 0
            let directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for i in 0..<rows {
                for j in 0..<cols {
                    if g[i][j] == 1 && !visited[i][j] {
                        islandCount += 1
                        // iterative DFS
                        var stack = [(i, j)]
                        visited[i][j] = true
                        while let (r, c) = stack.popLast() {
                            for d in directions {
                                let nr = r + d.0
                                let nc = c + d.1
                                if nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                                    g[nr][nc] == 1 && !visited[nr][nc] {
                                    visited[nr][nc] = true
                                    stack.append((nr, nc))
                                }
                            }
                        }
                    }
                }
            }
            return islandCount
        }
        
        // If already disconnected (0 or >1 islands)
        if countIslands(grid) != 1 {
            return 0
        }
        
        var mutableGrid = grid
        for i in 0..<rows {
            for j in 0..<cols where mutableGrid[i][j] == 1 {
                mutableGrid[i][j] = 0
                if countIslands(mutableGrid) != 1 {
                    return 1
                }
                mutableGrid[i][j] = 1
            }
        }
        return 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))

    fun minDays(grid: Array<IntArray>): Int {
        if (countIslands(grid) != 1) return 0
        val m = grid.size
        val n = grid[0].size
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0
                    if (countIslands(grid) != 1) {
                        grid[i][j] = 1
                        return 1
                    }
                    grid[i][j] = 1
                }
            }
        }
        return 2
    }

    private fun countIslands(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val visited = Array(m) { BooleanArray(n) }
        var islands = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (!visited[i][j] && grid[i][j] == 1) {
                    dfs(grid, i, j, visited)
                    islands++
                }
            }
        }
        return islands
    }

    private fun dfs(grid: Array<IntArray>, sr: Int, sc: Int, visited: Array<BooleanArray>) {
        val m = grid.size
        val n = grid[0].size
        val stack = java.util.ArrayDeque<Pair<Int, Int>>()
        stack.add(Pair(sr, sc))
        visited[sr][sc] = true
        while (stack.isNotEmpty()) {
            val (r, c) = stack.removeLast()
            for (d in dirs) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr in 0 until m && nc in 0 until n && !visited[nr][nc] && grid[nr][nc] == 1) {
                    visited[nr][nc] = true
                    stack.add(Pair(nr, nc))
                }
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  static const List<List<int>> _dirs = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
  ];

  int minDays(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    int initialIslands = _countIslands(grid);
    if (initialIslands != 1) return 0;

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) {
          grid[i][j] = 0;
          int islandsAfterRemoval = _countIslands(grid);
          grid[i][j] = 1;
          if (islandsAfterRemoval != 1) return 1;
        }
      }
    }

    return 2;
  }

  int _countIslands(List<List<int>> g) {
    int m = g.length;
    int n = g[0].length;
    List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));
    int islands = 0;

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (!visited[i][j] && g[i][j] == 1) {
          islands++;
          _dfs(g, visited, i, j);
        }
      }
    }

    return islands;
  }

  void _dfs(List<List<int>> g, List<List<bool>> visited, int sr, int sc) {
    int m = g.length;
    int n = g[0].length;
    var stack = <List<int>>[];
    stack.add([sr, sc]);
    visited[sr][sc] = true;

    while (stack.isNotEmpty) {
      var cur = stack.removeLast();
      int r = cur[0];
      int c = cur[1];

      for (var d in _dirs) {
        int nr = r + d[0];
        int nc = c + d[1];
        if (nr >= 0 &&
            nr < m &&
            nc >= 0 &&
            nc < n &&
            !visited[nr][nc] &&
            g[nr][nc] == 1) {
          visited[nr][nc] = true;
          stack.add([nr, nc]);
        }
      }
    }
  }
}
```

## Golang

```go
func minDays(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	islandCount, landCount := 0, 0
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	var dfsCount func(int, int)
	dfsCount = func(r, c int) {
		visited[r][c] = true
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] && grid[nr][nc] == 1 {
				dfsCount(nr, nc)
			}
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				landCount++
				if !visited[i][j] {
					islandCount++
					dfsCount(i, j)
				}
			}
		}
	}

	if islandCount != 1 {
		return 0
	}
	if landCount <= 1 {
		return 1
	}

	total := m * n
	discovery := make([]int, total)
	low := make([]int, total)
	for i := range discovery {
		discovery[i] = -1
		low[i] = -1
	}
	time := 0
	hasAP := false

	var dfsAP func(int, int)
	dfsAP = func(u, parent int) {
		discovery[u] = time
		low[u] = time
		time++
		children := 0
		r, c := u/n, u%n
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0 {
				continue
			}
			v := nr*n + nc
			if discovery[v] == -1 {
				children++
				dfsAP(v, u)
				if low[v] < low[u] {
					low[u] = low[v]
				}
				if parent != -1 && low[v] >= discovery[u] {
					hasAP = true
				}
			} else if v != parent {
				if discovery[v] < low[u] {
					low[u] = discovery[v]
				}
			}
		}
		if parent == -1 && children > 1 {
			hasAP = true
		}
	}

	start := -1
	for i := 0; i < m && start == -1; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				start = i*n + j
				break
			}
		}
	}
	dfsAP(start, -1)

	if hasAP {
		return 1
	}
	return 2
}
```

## Ruby

```ruby
def count_islands(grid)
  m = grid.size
  n = grid[0].size
  visited = Array.new(m) { Array.new(n, false) }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  islands = 0

  (0...m).each do |i|
    (0...n).each do |j|
      next if visited[i][j] || grid[i][j] == 0
      islands += 1
      stack = [[i, j]]
      visited[i][j] = true
      until stack.empty?
        x, y = stack.pop
        dirs.each do |dx, dy|
          nx = x + dx
          ny = y + dy
          if nx.between?(0, m - 1) && ny.between?(0, n - 1) &&
             !visited[nx][ny] && grid[nx][ny] == 1
            visited[nx][ny] = true
            stack << [nx, ny]
          end
        end
      end
    end
  end

  islands
end

# @param {Integer[][]} grid
# @return {Integer}
def min_days(grid)
  return 0 if count_islands(grid) != 1

  m = grid.size
  n = grid[0].size

  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] == 0
      grid[i][j] = 0
      return 1 if count_islands(grid) != 1
      grid[i][j] = 1
    end
  end

  2
end
```

## Scala

```scala
object Solution {
  def minDays(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    def countIslands(): Int = {
      val visited = Array.ofDim[Boolean](m, n)
      var islands = 0

      for (i <- 0 until m; j <- 0 until n) {
        if (grid(i)(j) == 1 && !visited(i)(j)) {
          islands += 1
          val stack = scala.collection.mutable.Stack[(Int, Int)]()
          stack.push((i, j))
          visited(i)(j) = true

          while (stack.nonEmpty) {
            val (r, c) = stack.pop()
            for ((dr, dc) <- dirs) {
              val nr = r + dr
              val nc = c + dc
              if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                  grid(nr)(nc) == 1 && !visited(nr)(nc)) {
                visited(nr)(nc) = true
                stack.push((nr, nc))
              }
            }
          }
        }
      }

      islands
    }

    // If already disconnected (0 or >1 islands)
    if (countIslands() != 1) return 0

    // Try removing each land cell once
    for (i <- 0 until m; j <- 0 until n) {
      if (grid(i)(j) == 1) {
        grid(i)(j) = 0
        val islandsAfterRemoval = countIslands()
        grid(i)(j) = 1
        if (islandsAfterRemoval != 1) return 1
      }
    }

    // Otherwise, need at most two removals
    2
  }
}
```

## Rust

```rust
use std::cmp::min;

fn count_islands(grid: &Vec<Vec<i32>>) -> i32 {
    let m = grid.len();
    let n = grid[0].len();
    let mut visited = vec![false; m * n];
    let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
    let mut cnt = 0;
    for i in 0..m {
        for j in 0..n {
            if grid[i][j] == 1 {
                let id = i * n + j;
                if !visited[id] {
                    cnt += 1;
                    let mut stack = vec![(i, j)];
                    visited[id] = true;
                    while let Some((r, c)) = stack.pop() {
                        for (dr, dc) in dirs.iter() {
                            let nr = r as i32 + dr;
                            let nc = c as i32 + dc;
                            if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                                continue;
                            }
                            let ur = nr as usize;
                            let uc = nc as usize;
                            if grid[ur][uc] == 1 {
                                let nid = ur * n + uc;
                                if !visited[nid] {
                                    visited[nid] = true;
                                    stack.push((ur, uc));
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cnt
}

fn dfs(
    r: usize,
    c: usize,
    pr: i32,
    pc: i32,
    grid: &Vec<Vec<i32>>,
    disc: &mut Vec<i32>,
    low: &mut Vec<i32>,
    time: &mut i32,
    has_articulation: &mut bool,
    m: usize,
    n: usize,
) {
    let id = r * n + c;
    *time += 1;
    disc[id] = *time;
    low[id] = *time;
    let mut children = 0;
    let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
    for (dr, dc) in dirs.iter() {
        let nr = r as i32 + dr;
        let nc = c as i32 + dc;
        if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
            continue;
        }
        let ur = nr as usize;
        let uc = nc as usize;
        if grid[ur][uc] == 0 {
            continue;
        }
        let nid = ur * n + uc;
        if disc[nid] == -1 {
            children += 1;
            dfs(
                ur,
                uc,
                r as i32,
                c as i32,
                grid,
                disc,
                low,
                time,
                has_articulation,
                m,
                n,
            );
            low[id] = min(low[id], low[nid]);
            if pr != -1 && low[nid] >= disc[id] {
                *has_articulation = true;
            }
        } else if !(pr == ur as i32 && pc == uc as i32) {
            low[id] = min(low[id], disc[nid]);
        }
    }
    if pr == -1 && children > 1 {
        *has_articulation = true;
    }
}

impl Solution {
    pub fn min_days(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        // If already disconnected
        if count_islands(&grid) != 1 {
            return 0;
        }

        // Count land cells
        let mut land = 0;
        for row in &grid {
            for &v in row {
                if v == 1 {
                    land += 1;
                }
            }
        }
        if land <= 1 {
            return land as i32; // 0 or 1
        }

        // Find articulation point using Tarjan's algorithm
        let size = m * n;
        let mut disc = vec![-1i32; size];
        let mut low = vec![-1i32; size];
        let mut time = 0i32;
        let mut has_articulation = false;

        'outer: for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    dfs(
                        i,
                        j,
                        -1,
                        -1,
                        &grid,
                        &mut disc,
                        &mut low,
                        &mut time,
                        &mut has_articulation,
                        m,
                        n,
                    );
                    break 'outer;
                }
            }
        }

        if has_articulation {
            1
        } else {
            2
        }
    }
}
```

## Racket

```racket
#lang racket

(define DIRS '((0 1) (0 -1) (1 0) (-1 0)))

;; Count number of islands in a mutable grid represented as vector of vectors
(define (count-islands gridV)
  (let* ((rows (vector-length gridV))
         (cols (if (= rows 0) 0 (vector-length (vector-ref gridV 0))))
         (visited (make-vector rows)))
    (for ([i (in-range rows)])
      (vector-set! visited i (make-vector cols #f)))
    (let ((cnt 0))
      (for ([i (in-range rows)])
        (for ([j (in-range cols)])
          (when (and (= (vector-ref (vector-ref gridV i) j) 1)
                     (not (vector-ref (vector-ref visited i) j)))
            (set! cnt (+ cnt 1))
            ;; DFS using explicit stack
            (let ((stack (list (cons i j))))
              (let loop ()
                (when (not (null? stack))
                  (define cur (car stack))
                  (set! stack (cdr stack))
                  (define r (car cur))
                  (define c (cdr cur))
                  (unless (vector-ref (vector-ref visited r) c)
                    (vector-set! (vector-ref visited r) c #t)
                    (for ([d DIRS])
                      (let ((nr (+ r (first d)))
                            (nc (+ c (second d))))
                        (when (and (>= nr 0) (< nr rows)
                                   (>= nc 0) (< nc cols)
                                   (= (vector-ref (vector-ref gridV nr) nc) 1)
                                   (not (vector-ref (vector-ref visited nr) nc)))
                          (set! stack (cons (cons nr nc) stack))))))
                  (loop)))))))
      cnt)))

;; Main function
(define/contract (min-days grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (= rows 0) 0 (length (first grid))))
         (gridV (list->vector (map list->vector grid)))
         (initial (count-islands gridV)))
    (cond
      [(not (= initial 1)) 0]
      [else
       (let ((ans
               (call/cc
                (lambda (return)
                  (for ([i (in-range rows)])
                    (for ([j (in-range cols)])
                      (when (= (vector-ref (vector-ref gridV i) j) 1)
                        (vector-set! (vector-ref gridV i) j 0)
                        (let ((c (count-islands gridV)))
                          (vector-set! (vector-ref gridV i) j 1)
                          (when (not (= c 1))
                            (return 1))))))))))
         (if ans ans 2))])))
```

## Erlang

```erlang
-module(solution).
-export([min_days/1]).

-spec min_days(Grid :: [[integer()]]) -> integer().
min_days(Grid) ->
    case count_islands(Grid, undefined) of
        Count when Count =/= 1 -> 0;
        _ -> 
            Rows = length(Grid),
            Cols = case Grid of [] -> 0; [First|_] -> length(First) end,
            try_cells(0, Rows, Cols, Grid)
    end.

%% Try removing each land cell to see if one day is enough
try_cells(Row, Rows, _Cols, _Grid) when Row == Rows ->
    2;
try_cells(Row, Rows, Cols, Grid) ->
    case try_cols(Row, 0, Cols, Grid) of
        true -> 1;
        false -> try_cells(Row + 1, Rows, Cols, Grid)
    end.

try_cols(_Row, Col, Cols, _Grid) when Col == Cols ->
    false;
try_cols(Row, Col, Cols, Grid) ->
    case get_cell(Grid, Row, Col) of
        1 ->
            case count_islands(Grid, {Row, Col}) of
                Count when Count =/= 1 -> true;
                _ -> try_cols(Row, Col + 1, Cols, Grid)
            end;
        _ ->
            try_cols(Row, Col + 1, Cols, Grid)
    end.

%% Count islands, optionally ignoring a specific cell
count_islands(Grid, Ignore) ->
    Rows = length(Grid),
    Cols = case Grid of [] -> 0; [First|_] -> length(First) end,
    scan_rows(0, Rows, Cols, Grid, Ignore, 0, #{}).

scan_rows(Row, Rows, _Cols, _Grid, _Ignore, Count, _Visited) when Row == Rows ->
    Count;
scan_rows(Row, Rows, Cols, Grid, Ignore, Count, Visited) ->
    {NewCount, NewVisited} = scan_cols(Row, 0, Cols, Grid, Ignore, Count, Visited),
    scan_rows(Row + 1, Rows, Cols, Grid, Ignore, NewCount, NewVisited).

scan_cols(_Row, Col, Cols, _Grid, _Ignore, Count, Visited) when Col == Cols ->
    {Count, Visited};
scan_cols(Row, Col, Cols, Grid, Ignore, Count, Visited) ->
    case is_land(Grid, Row, Col, Ignore) of
        true ->
            Key = {Row, Col},
            case maps:is_key(Key, Visited) of
                true ->
                    scan_cols(Row, Col + 1, Cols, Grid, Ignore, Count, Visited);
                false ->
                    Visited2 = dfs(Grid, Ignore, [{Row, Col}], Visited),
                    scan_cols(Row, Col + 1, Cols, Grid, Ignore, Count + 1, Visited2)
            end;
        false ->
            scan_cols(Row, Col + 1, Cols, Grid, Ignore, Count, Visited)
    end.

%% Depth‑first search to mark all cells of one island
dfs(_Grid, _Ignore, [], Visited) ->
    Visited;
dfs(Grid, Ignore, [{R, C} | Rest], Visited) ->
    Key = {R, C},
    case maps:is_key(Key, Visited) of
        true ->
            dfs(Grid, Ignore, Rest, Visited);
        false ->
            Visited1 = maps:put(Key, true, Visited),
            Neighs = neighbors(R, C, Grid, Ignore, Visited1),
            dfs(Grid, Ignore, Neighs ++ Rest, Visited1)
    end.

neighbors(R, C, Grid, Ignore, Visited) ->
    Dirs = [{-1,0},{1,0},{0,-1},{0,1}],
    lists:foldl(fun({DR, DC}, Acc) ->
        NR = R + DR,
        NC = C + DC,
        case valid(NR, NC, Grid) andalso is_land(Grid, NR, NC, Ignore) of
            true ->
                K = {NR, NC},
                case maps:is_key(K, Visited) of
                    true -> Acc;
                    false -> [{NR, NC} | Acc]
                end;
            false -> Acc
        end
    end, [], Dirs).

valid(R, C, Grid) ->
    Rows = length(Grid),
    Cols = case Grid of [] -> 0; [First|_] -> length(First) end,
    R >= 0 andalso R < Rows andalso C >= 0 andalso C < Cols.

is_land(Grid, R, C, Ignore) ->
    case get_cell(Grid, R, C) of
        1 ->
            case Ignore of
                {IR, IC} when IR =:= R, IC =:= C -> false;
                _ -> true
            end;
        _ -> false
    end.

get_cell(Grid, R, C) ->
    RowList = lists:nth(R + 1, Grid),
    lists:nth(C + 1, RowList).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_days(grid :: [[integer]]) :: integer
  def min_days(grid) do
    rows = length(grid)
    cols = grid |> hd() |> length()

    if count_islands(grid, rows, cols) != 1 do
      0
    else
      found =
        Enum.any?(0..rows - 1, fn r ->
          Enum.any?(0..cols - 1, fn c ->
            if get(grid, r, c) == 1 do
              new_grid = set_cell(grid, r, c, 0)
              count_islands(new_grid, rows, cols) != 1
            else
              false
            end
          end)
        end)

      if found, do: 1, else: 2
    end
  end

  @dirs [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

  defp get(grid, r, c) do
    grid |> Enum.at(r) |> Enum.at(c)
  end

  defp set_cell(grid, r, c, val) do
    row = Enum.at(grid, r)
    new_row = List.replace_at(row, c, val)
    List.replace_at(grid, r, new_row)
  end

  defp count_islands(grid, rows, cols) do
    visited = MapSet.new()

    {cnt, _} =
      Enum.reduce(0..rows - 1, {0, visited}, fn r, {count, vis} ->
        Enum.reduce(0..cols - 1, {count, vis}, fn c, {c_cnt, c_vis} ->
          if get(grid, r, c) == 1 and not MapSet.member?(c_vis, {r, c}) do
            new_vis = dfs(grid, r, c, rows, cols, c_vis)
            {c_cnt + 1, new_vis}
          else
            {c_cnt, c_vis}
          end
        end)
      end)

    cnt
  end

  defp dfs(grid, sr, sc, rows, cols, visited) do
    stack = [{sr, sc}]
    dfs_iter(grid, rows, cols, visited, stack)
  end

  defp dfs_iter(_grid, _rows, _cols, visited, []) do
    visited
  end

  defp dfs_iter(grid, rows, cols, visited, [{r, c} | rest]) do
    if MapSet.member?(visited, {r, c}) do
      dfs_iter(grid, rows, cols, visited, rest)
    else
      visited = MapSet.put(visited, {r, c})

      neighbors =
        for {dr, dc} <- @dirs,
            nr = r + dr,
            nc = c + dc,
            nr >= 0 and nr < rows and nc >= 0 and nc < cols,
            get(grid, nr, nc) == 1,
            not MapSet.member?(visited, {nr, nc}),
            do: {nr, nc}

      dfs_iter(grid, rows, cols, visited, neighbors ++ rest)
    end
  end
end
```

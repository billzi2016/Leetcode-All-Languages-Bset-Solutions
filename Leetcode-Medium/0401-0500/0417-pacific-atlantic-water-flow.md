# 0417. Pacific Atlantic Water Flow

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        if (m == 0) return {};
        int n = heights[0].size();
        vector<vector<bool>> pac(m, vector<bool>(n, false));
        vector<vector<bool>> atl(m, vector<bool>(n, false));
        queue<pair<int,int>> q;
        // Pacific borders: top row and left column
        for (int i = 0; i < m; ++i) {
            pac[i][0] = true;
            q.emplace(i, 0);
        }
        for (int j = 1; j < n; ++j) { // avoid duplicate corner
            pac[0][j] = true;
            q.emplace(0, j);
        }
        bfs(heights, pac, q);
        // Atlantic borders: bottom row and right column
        while (!q.empty()) q.pop();
        for (int i = 0; i < m; ++i) {
            atl[i][n-1] = true;
            q.emplace(i, n-1);
        }
        for (int j = 0; j < n-1; ++j) { // avoid duplicate corner
            atl[m-1][j] = true;
            q.emplace(m-1, j);
        }
        bfs(heights, atl, q);
        vector<vector<int>> res;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (pac[i][j] && atl[i][j])
                    res.push_back({i, j});
        return res;
    }
private:
    void bfs(const vector<vector<int>>& heights,
             vector<vector<bool>>& visited,
             queue<pair<int,int>>& q) {
        int m = heights.size(), n = heights[0].size();
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty()) {
            auto [r,c] = q.front(); q.pop();
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (visited[nr][nc]) continue;
                if (heights[nr][nc] < heights[r][c]) continue; // can only flow from higher/equal
                visited[nr][nc] = true;
                q.emplace(nr, nc);
            }
        }
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        Queue<int[]> pQueue = new ArrayDeque<>();
        Queue<int[]> aQueue = new ArrayDeque<>();

        // Pacific borders (top row and left column)
        for (int i = 0; i < m; i++) {
            pacific[i][0] = true;
            pQueue.offer(new int[]{i, 0});
        }
        for (int j = 1; j < n; j++) { // start from 1 to avoid duplicate corner
            pacific[0][j] = true;
            pQueue.offer(new int[]{0, j});
        }

        // Atlantic borders (bottom row and right column)
        for (int i = 0; i < m; i++) {
            atlantic[i][n - 1] = true;
            aQueue.offer(new int[]{i, n - 1});
        }
        for (int j = 0; j < n - 1; j++) { // up to n-2 to avoid duplicate corner
            atlantic[m - 1][j] = true;
            aQueue.offer(new int[]{m - 1, j});
        }

        bfs(pQueue, pacific, heights);
        bfs(aQueue, atlantic, heights);

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    List<Integer> cell = new ArrayList<>(2);
                    cell.add(i);
                    cell.add(j);
                    result.add(cell);
                }
            }
        }
        return result;
    }

    private void bfs(Queue<int[]> queue, boolean[][] visited, int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (visited[nr][nc]) continue;
                // Can flow from neighbor to current cell if neighbor height >= current height
                if (heights[nr][nc] >= heights[r][c]) {
                    visited[nr][nc] = true;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        from collections import deque

        def bfs(starts):
            visited = [[False] * n for _ in range(m)]
            q = deque(starts)
            for r, c in starts:
                visited[r][c] = True
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        if heights[nr][nc] >= heights[r][c]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
            return visited

        pacific_starts = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        atlantic_starts = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]

        pacific_reach = bfs(pacific_starts)
        atlantic_reach = bfs(atlantic_starts)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reach[i][j] and atlantic_reach[i][j]:
                    result.append([i, j])
        return result
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def bfs(starts, reachable):
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not reachable[nr][nc]:
                        if heights[nr][nc] >= heights[r][c]:
                            reachable[nr][nc] = True
                            q.append((nr, nc))

        pacific_starts = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        atlantic_starts = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]

        for r, c in pacific_starts:
            pacific[r][c] = True
        for r, c in atlantic_starts:
            atlantic[r][c] = True

        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pacificAtlantic(int** heights, int heightsSize, int* heightsColSize, int* returnSize, int*** returnColumnSizes) {
    int m = heightsSize;
    if (m == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int n = heightsColSize[0];
    int total = m * n;

    char *pac = (char *)calloc(total, sizeof(char));
    char *atl = (char *)calloc(total, sizeof(char));
    int *queue = (int *)malloc(total * sizeof(int));

    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    // Pacific BFS (top row and left column)
    int front = 0, back = 0;
    for (int c = 0; c < n; ++c) {
        int idx = c;               // row 0
        pac[idx] = 1;
        queue[back++] = idx;
    }
    for (int r = 0; r < m; ++r) {
        int idx = r * n;           // col 0
        if (!pac[idx]) {
            pac[idx] = 1;
            queue[back++] = idx;
        }
    }
    while (front < back) {
        int cur = queue[front++];
        int r = cur / n, c = cur % n;
        int h = heights[r][c];
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            int nid = nr * n + nc;
            if (pac[nid]) continue;
            if (heights[nr][nc] >= h) {
                pac[nid] = 1;
                queue[back++] = nid;
            }
        }
    }

    // Atlantic BFS (bottom row and right column)
    front = back = 0;
    for (int c = 0; c < n; ++c) {
        int idx = (m - 1) * n + c; // bottom row
        atl[idx] = 1;
        queue[back++] = idx;
    }
    for (int r = 0; r < m; ++r) {
        int idx = r * n + (n - 1); // right column
        if (!atl[idx]) {
            atl[idx] = 1;
            queue[back++] = idx;
        }
    }
    while (front < back) {
        int cur = queue[front++];
        int r = cur / n, c = cur % n;
        int h = heights[r][c];
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            int nid = nr * n + nc;
            if (atl[nid]) continue;
            if (heights[nr][nc] >= h) {
                atl[nid] = 1;
                queue[back++] = nid;
            }
        }
    }

    // Collect results
    int count = 0;
    for (int i = 0; i < total; ++i)
        if (pac[i] && atl[i]) ++count;

    *returnSize = count;
    *returnColumnSizes = (int **)malloc(count * sizeof(int *));
    int **result = (int **)malloc(count * sizeof(int *));
    for (int i = 0; i < count; ++i) {
        (*returnColumnSizes)[i] = (int *)malloc(sizeof(int));
        *((*returnColumnSizes)[i]) = 2;
        result[i] = (int *)malloc(2 * sizeof(int));
    }

    int idxRes = 0;
    for (int r = 0; r < m; ++r) {
        for (int c = 0; c < n; ++c) {
            int i = r * n + c;
            if (pac[i] && atl[i]) {
                result[idxRes][0] = r;
                result[idxRes][1] = c;
                ++idxRes;
            }
        }
    }

    free(pac);
    free(atl);
    free(queue);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> PacificAtlantic(int[][] heights) {
        int m = heights.Length;
        int n = heights[0].Length;
        bool[,] pacific = new bool[m, n];
        bool[,] atlantic = new bool[m, n];
        var dirs = new int[] { -1, 0, 1, 0, -1 };
        
        Queue<int[]> qPacific = new Queue<int[]>();
        Queue<int[]> qAtlantic = new Queue<int[]>();
        
        // Initialize border cells
        for (int i = 0; i < m; i++) {
            pacific[i, 0] = true;
            qPacific.Enqueue(new int[]{i, 0});
            atlantic[i, n - 1] = true;
            qAtlantic.Enqueue(new int[]{i, n - 1});
        }
        for (int j = 0; j < n; j++) {
            pacific[0, j] = true;
            qPacific.Enqueue(new int[]{0, j});
            atlantic[m - 1, j] = true;
            qAtlantic.Enqueue(new int[]{m - 1, j});
        }
        
        BFS(heights, pacific, qPacific, m, n, dirs);
        BFS(heights, atlantic, qAtlantic, m, n, dirs);
        
        IList<IList<int>> result = new List<IList<int>>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i, j] && atlantic[i, j]) {
                    result.Add(new List<int>{i, j});
                }
            }
        }
        return result;
    }
    
    private void BFS(int[][] heights, bool[,] visited, Queue<int[]> q, int m, int n, int[] dirs) {
        while (q.Count > 0) {
            var cell = q.Dequeue();
            int r = cell[0], c = cell[1];
            for (int d = 0; d < 4; d++) {
                int nr = r + dirs[d];
                int nc = c + dirs[d + 1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (visited[nr, nc]) continue;
                if (heights[nr][nc] < heights[r][c]) continue;
                visited[nr, nc] = true;
                q.Enqueue(new int[]{nr, nc});
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacific Atlantic = function (heights) {
    if (!heights || heights.length === 0 || heights[0].length === 0) return [];
    const m = heights.length;
    const n = heights[0].length;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    function bfs(starts) {
        const visited = Array.from({ length: m }, () => Array(n).fill(false));
        const queue = [];
        let qIdx = 0;
        for (const [r, c] of starts) {
            if (!visited[r][c]) {
                visited[r][c] = true;
                queue.push([r, c]);
            }
        }
        while (qIdx < queue.length) {
            const [r, c] = queue[qIdx++];
            const curH = heights[r][c];
            for (const [dr, dc] of dirs) {
                const nr = r + dr;
                const nc = c + dc;
                if (
                    nr >= 0 && nr < m &&
                    nc >= 0 && nc < n &&
                    !visited[nr][nc] &&
                    heights[nr][nc] >= curH
                ) {
                    visited[nr][nc] = true;
                    queue.push([nr, nc]);
                }
            }
        }
        return visited;
    }
    
    const pacificStarts = [];
    for (let i = 0; i < m; i++) pacificStarts.push([i, 0]);
    for (let j = 0; j < n; j++) pacificStarts.push([0, j]);
    
    const atlanticStarts = [];
    for (let i = 0; i < m; i++) atlanticStarts.push([i, n - 1]);
    for (let j = 0; j < n; j++) atlanticStarts.push([m - 1, j]);
    
    const pacificReach = bfs(pacificStarts);
    const atlanticReach = bfs(atlanticStarts);
    
    const result = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (pacificReach[i][j] && atlanticReach[i][j]) {
                result.push([i, j]);
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function pacificAtlantic(heights: number[][]): number[][] {
    const m = heights.length;
    if (m === 0) return [];
    const n = heights[0].length;

    const pac: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const atl: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    const bfs = (queue: [number, number][], visited: boolean[][]) => {
        let head = 0;
        while (head < queue.length) {
            const [r, c] = queue[head++];
            for (const [dr, dc] of dirs) {
                const nr = r + dr;
                const nc = c + dc;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (visited[nr][nc]) continue;
                if (heights[nr][nc] >= heights[r][c]) {
                    visited[nr][nc] = true;
                    queue.push([nr, nc]);
                }
            }
        }
    };

    const pacQueue: [number, number][] = [];
    const atlQueue: [number, number][] = [];

    // Pacific borders (top row and left column)
    for (let i = 0; i < m; i++) {
        pac[i][0] = true;
        pacQueue.push([i, 0]);
    }
    for (let j = 0; j < n; j++) {
        pac[0][j] = true;
        pacQueue.push([0, j]);
    }

    // Atlantic borders (bottom row and right column)
    for (let i = 0; i < m; i++) {
        atl[i][n - 1] = true;
        atlQueue.push([i, n - 1]);
    }
    for (let j = 0; j < n; j++) {
        atl[m - 1][j] = true;
        atlQueue.push([m - 1, j]);
    }

    bfs(pacQueue, pac);
    bfs(atlQueue, atl);

    const result: number[][] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (pac[i][j] && atl[i][j]) {
                result.push([i, j]);
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $heights
     * @return Integer[][]
     */
    function pacificAtlantic($heights) {
        $m = count($heights);
        if ($m == 0) return [];
        $n = count($heights[0]);

        // visited matrices
        $pacific = array_fill(0, $m, array_fill(0, $n, false));
        $atlantic = array_fill(0, $m, array_fill(0, $n, false));

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        // BFS for Pacific
        $queue = new SplQueue();
        for ($i = 0; $i < $m; $i++) {
            $pacific[$i][0] = true;
            $queue->enqueue([$i, 0]);
        }
        for ($j = 0; $j < $n; $j++) {
            $pacific[0][$j] = true;
            $queue->enqueue([0, $j]);
        }

        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                if ($pacific[$nr][$nc]) continue;
                if ($heights[$nr][$nc] < $heights[$r][$c]) continue;
                $pacific[$nr][$nc] = true;
                $queue->enqueue([$nr, $nc]);
            }
        }

        // BFS for Atlantic
        $queue = new SplQueue();
        for ($i = 0; $i < $m; $i++) {
            $atlantic[$i][$n-1] = true;
            $queue->enqueue([$i, $n-1]);
        }
        for ($j = 0; $j < $n; $j++) {
            $atlantic[$m-1][$j] = true;
            $queue->enqueue([$m-1, $j]);
        }

        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                if ($atlantic[$nr][$nc]) continue;
                if ($heights[$nr][$nc] < $heights[$r][$c]) continue;
                $atlantic[$nr][$nc] = true;
                $queue->enqueue([$nr, $nc]);
            }
        }

        // Collect result
        $result = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($pacific[$i][$j] && $atlantic[$i][$j]) {
                    $result[] = [$i, $j];
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func pacificAtlantic(_ heights: [[Int]]) -> [[Int]] {
        let m = heights.count
        guard m > 0 else { return [] }
        let n = heights[0].count
        
        var pacific = Array(repeating: Array(repeating: false, count: n), count: m)
        var atlantic = Array(repeating: Array(repeating: false, count: n), count: m)
        
        var pQueue = [(Int, Int)]()
        var aQueue = [(Int, Int)]()
        
        // Pacific borders: top row and left column
        for i in 0..<m {
            pacific[i][0] = true
            pQueue.append((i, 0))
        }
        for j in 0..<n {
            pacific[0][j] = true
            pQueue.append((0, j))
        }
        
        // Atlantic borders: bottom row and right column
        for i in 0..<m {
            atlantic[i][n - 1] = true
            aQueue.append((i, n - 1))
        }
        for j in 0..<n {
            atlantic[m - 1][j] = true
            aQueue.append((m - 1, j))
        }
        
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        func bfs(_ queue: inout [(Int, Int)], _ visited: inout [[Bool]]) {
            var head = 0
            while head < queue.count {
                let (r, c) = queue[head]
                head += 1
                for d in dirs {
                    let nr = r + d.0
                    let nc = c + d.1
                    if nr >= 0 && nr < m && nc >= 0 && nc < n &&
                        !visited[nr][nc] && heights[nr][nc] >= heights[r][c] {
                        visited[nr][nc] = true
                        queue.append((nr, nc))
                    }
                }
            }
        }
        
        bfs(&pQueue, &pacific)
        bfs(&aQueue, &atlantic)
        
        var result = [[Int]]()
        for i in 0..<m {
            for j in 0..<n {
                if pacific[i][j] && atlantic[i][j] {
                    result.append([i, j])
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pacificAtlantic(heights: Array<IntArray>): List<List<Int>> {
        val m = heights.size
        if (m == 0) return emptyList()
        val n = heights[0].size
        val pac = Array(m) { BooleanArray(n) }
        val atl = Array(m) { BooleanArray(n) }
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

        fun bfs(starts: List<Pair<Int, Int>>, visited: Array<BooleanArray>) {
            val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
            for ((r, c) in starts) {
                if (!visited[r][c]) {
                    visited[r][c] = true
                    queue.add(Pair(r, c))
                }
            }
            while (queue.isNotEmpty()) {
                val (r, c) = queue.removeFirst()
                for (d in dirs) {
                    val nr = r + d[0]
                    val nc = c + d[1]
                    if (nr !in 0 until m || nc !in 0 until n) continue
                    if (visited[nr][nc]) continue
                    if (heights[nr][nc] < heights[r][c]) continue
                    visited[nr][nc] = true
                    queue.add(Pair(nr, nc))
                }
            }
        }

        val pacStarts = mutableListOf<Pair<Int, Int>>()
        val atlStarts = mutableListOf<Pair<Int, Int>>()

        for (i in 0 until m) {
            pacStarts.add(Pair(i, 0))
            atlStarts.add(Pair(i, n - 1))
        }
        for (j in 0 until n) {
            pacStarts.add(Pair(0, j))
            atlStarts.add(Pair(m - 1, j))
        }

        bfs(pacStarts, pac)
        bfs(atlStarts, atl)

        val result = mutableListOf<List<Int>>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (pac[i][j] && atl[i][j]) {
                    result.add(listOf(i, j))
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<List<int>> pacificAtlantic(List<List<int>> heights) {
    int m = heights.length;
    if (m == 0) return [];
    int n = heights[0].length;

    List<List<bool>> pac = List.generate(m, (_) => List.filled(n, false));
    List<List<bool>> atl = List.generate(m, (_) => List.filled(n, false));

    Queue<List<int>> queue = Queue();

    // Pacific borders (top row and left column)
    for (int i = 0; i < m; ++i) {
      pac[i][0] = true;
      queue.add([i, 0]);
    }
    for (int j = 1; j < n; ++j) {
      pac[0][j] = true;
      queue.add([0, j]);
    }
    _bfs(queue, heights, pac);

    // Atlantic borders (bottom row and right column)
    queue.clear();
    for (int i = 0; i < m; ++i) {
      atl[i][n - 1] = true;
      queue.add([i, n - 1]);
    }
    for (int j = 0; j < n - 1; ++j) {
      atl[m - 1][j] = true;
      queue.add([m - 1, j]);
    }
    _bfs(queue, heights, atl);

    List<List<int>> result = [];
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (pac[i][j] && atl[i][j]) {
          result.add([i, j]);
        }
      }
    }
    return result;
  }

  void _bfs(Queue<List<int>> queue, List<List<int>> heights,
      List<List<bool>> visited) {
    int m = heights.length;
    int n = heights[0].length;
    const dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    while (queue.isNotEmpty) {
      List<int> cell = queue.removeFirst();
      int r = cell[0];
      int c = cell[1];

      for (var d in dirs) {
        int nr = r + d[0];
        int nc = c + d[1];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
        if (visited[nr][nc]) continue;
        if (heights[nr][nc] >= heights[r][c]) {
          visited[nr][nc] = true;
          queue.add([nr, nc]);
        }
      }
    }
  }
}
```

## Golang

```go
func pacificAtlantic(heights [][]int) [][]int {
    m := len(heights)
    if m == 0 {
        return [][]int{}
    }
    n := len(heights[0])

    pac := make([][]bool, m)
    atl := make([][]bool, m)
    for i := 0; i < m; i++ {
        pac[i] = make([]bool, n)
        atl[i] = make([]bool, n)
    }

    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

    bfs := func(starts [][]int, visited [][]bool) {
        q := make([][2]int, 0, len(starts))
        for _, s := range starts {
            r, c := s[0], s[1]
            if !visited[r][c] {
                visited[r][c] = true
                q = append(q, [2]int{r, c})
            }
        }
        for head := 0; head < len(q); head++ {
            cur := q[head]
            r, c := cur[0], cur[1]
            for _, d := range dirs {
                nr, nc := r+d[0], c+d[1]
                if nr < 0 || nr >= m || nc < 0 || nc >= n {
                    continue
                }
                if visited[nr][nc] {
                    continue
                }
                if heights[nr][nc] < heights[r][c] {
                    continue
                }
                visited[nr][nc] = true
                q = append(q, [2]int{nr, nc})
            }
        }
    }

    pacStarts := make([][]int, 0, m+n)
    for i := 0; i < m; i++ {
        pacStarts = append(pacStarts, []int{i, 0})
    }
    for j := 1; j < n; j++ {
        pacStarts = append(pacStarts, []int{0, j})
    }

    atlStarts := make([][]int, 0, m+n)
    for i := 0; i < m; i++ {
        atlStarts = append(atlStarts, []int{i, n - 1})
    }
    for j := 0; j < n-1; j++ {
        atlStarts = append(atlStarts, []int{m - 1, j})
    }

    bfs(pacStarts, pac)
    bfs(atlStarts, atl)

    res := make([][]int, 0)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if pac[i][j] && atl[i][j] {
                res = append(res, []int{i, j})
            }
        }
    }
    return res
}
```

## Ruby

```ruby
def pacific_atlantic(heights)
  m = heights.size
  n = heights[0].size
  pacific = Array.new(m) { Array.new(n, false) }
  atlantic = Array.new(m) { Array.new(n, false) }

  p_queue = []
  a_queue = []

  (0...m).each do |i|
    pacific[i][0] = true
    p_queue << [i, 0]
    atlantic[i][n - 1] = true
    a_queue << [i, n - 1]
  end

  (0...n).each do |j|
    pacific[0][j] = true
    p_queue << [0, j]
    atlantic[m - 1][j] = true
    a_queue << [m - 1, j]
  end

  bfs = lambda do |queue, visited|
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    idx = 0
    while idx < queue.length
      r, c = queue[idx]
      idx += 1
      cur_h = heights[r][c]
      dirs.each do |dr, dc|
        nr = r + dr
        nc = c + dc
        next if nr < 0 || nr >= m || nc < 0 || nc >= n
        next if visited[nr][nc]
        if heights[nr][nc] >= cur_h
          visited[nr][nc] = true
          queue << [nr, nc]
        end
      end
    end
  end

  bfs.call(p_queue, pacific)
  bfs.call(a_queue, atlantic)

  result = []
  (0...m).each do |i|
    (0...n).each do |j|
      result << [i, j] if pacific[i][j] && atlantic[i][j]
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def pacificAtlantic(heights: Array[Array[Int]]): List[List[Int]] = {
        val m = heights.length
        if (m == 0) return Nil
        val n = heights(0).length

        val pac = Array.ofDim[Boolean](m, n)
        val atl = Array.ofDim[Boolean](m, n)

        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

        import scala.collection.mutable.ArrayDeque

        def bfs(starts: Seq[(Int, Int)], visited: Array[Array[Boolean]]): Unit = {
            val q = ArrayDeque[(Int, Int)]()
            for ((r, c) <- starts) {
                if (!visited(r)(c)) {
                    visited(r)(c) = true
                    q.append((r, c))
                }
            }
            while (q.nonEmpty) {
                val (r, c) = q.removeHead()
                for ((dr, dc) <- dirs) {
                    val nr = r + dr
                    val nc = c + dc
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                        !visited(nr)(nc) && heights(nr)(nc) >= heights(r)(c)) {
                        visited(nr)(nc) = true
                        q.append((nr, nc))
                    }
                }
            }
        }

        // Pacific ocean borders (top row and left column)
        val pacStarts = (0 until n).map(c => (0, c)) ++ (1 until m).map(r => (r, 0))
        bfs(pacStarts, pac)

        // Atlantic ocean borders (bottom row and right column)
        val atlStarts = (0 until n).map(c => (m - 1, c)) ++ (0 until m - 1).map(r => (r, n - 1))
        bfs(atlStarts, atl)

        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        for (r <- 0 until m; c <- 0 until n) {
            if (pac(r)(c) && atl(r)(c)) {
                result += List(r, c)
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = heights.len();
        if m == 0 {
            return vec![];
        }
        let n = heights[0].len();

        let mut pacific = vec![vec![false; n]; m];
        let mut atlantic = vec![vec![false; n]; m];

        fn bfs(heights: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, starts: &[(usize, usize)]) {
            use std::collections::VecDeque;
            let m = heights.len();
            let n = heights[0].len();
            let dirs = [(-1i32, 0i32), (1, 0), (0, -1), (0, 1)];
            let mut q: VecDeque<(usize, usize)> = VecDeque::new();

            for &(r, c) in starts {
                if !visited[r][c] {
                    visited[r][c] = true;
                    q.push_back((r, c));
                }
            }

            while let Some((r, c)) = q.pop_front() {
                let cur_h = heights[r][c];
                for (dr, dc) in dirs.iter() {
                    let nr_i32 = r as i32 + dr;
                    let nc_i32 = c as i32 + dc;
                    if nr_i32 < 0 || nr_i32 >= m as i32 || nc_i32 < 0 || nc_i32 >= n as i32 {
                        continue;
                    }
                    let nr = nr_i32 as usize;
                    let nc = nc_i32 as usize;
                    if visited[nr][nc] {
                        continue;
                    }
                    if heights[nr][nc] >= cur_h {
                        visited[nr][nc] = true;
                        q.push_back((nr, nc));
                    }
                }
            }
        }

        // Pacific border cells
        let mut pacific_starts = Vec::new();
        for c in 0..n {
            pacific_starts.push((0usize, c));
        }
        for r in 0..m {
            pacific_starts.push((r, 0usize));
        }

        // Atlantic border cells
        let mut atlantic_starts = Vec::new();
        for c in 0..n {
            atlantic_starts.push((m - 1, c));
        }
        for r in 0..m {
            atlantic_starts.push((r, n - 1));
        }

        bfs(&heights, &mut pacific, &pacific_starts);
        bfs(&heights, &mut atlantic, &atlantic_starts);

        let mut result = Vec::new();
        for r in 0..m {
            for c in 0..n {
                if pacific[r][c] && atlantic[r][c] {
                    result.push(vec![r as i32, c as i32]);
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (pacific-atlantic heights)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ([m (length heights)]
         [n (if (= m 0) 0 (length (first heights)))]
         ;; convert to vector of vectors for O(1) indexing
         [grid (list->vector (map list->vector heights))]
         ;; visited matrices
         [pac-vis (build-vector m (lambda (_) (make-vector n #f)))]
         [atl-vis (build-vector m (lambda (_) (make-vector n #f)))]

         ;; directions
         [dirs '((1 0) (-1 0) (0 1) (0 -1))]
         
         ;; BFS procedure
         (define (bfs starts vis)
           (let* ([size (* m n)]
                  [queue (make-vector size)])
             (let loop ((front 0) (rear 0))
               (when (< front rear)
                 (let* ([pos (vector-ref queue front)]
                        [r (first pos)] [c (second pos)])
                   (for-each
                    (lambda (d)
                      (define dr (first d)) (define dc (second d))
                      (define nr (+ r dr)) (define nc (+ c dc))
                      (when (and (>= nr 0) (< nr m) (>= nc 0) (< nc n))
                        (unless (vector-ref (vector-ref vis nr) nc)
                          (when (<= (vector-ref (vector-ref grid r) c)
                                    (vector-ref (vector-ref grid nr) nc))
                            (vector-set! (vector-ref vis nr) nc #t)
                            (vector-set! queue rear (list nr nc))
                            (set! rear (+ rear 1))))))
                    dirs)))
                 (loop (+ front 1) rear))
               ;; initial enqueue already done
               ))
           ;; after BFS, nothing to return; vis mutated
           )
         
         ;; initialize start cells for Pacific and Atlantic
         [pac-starts
          (let ([list '()])
            (for ([c (in-range n)])
              (set! list (cons (list 0 c) list))
              (vector-set! (vector-ref pac-vis 0) c #t))
            (for ([r (in-range m)])
              (set! list (cons (list r 0) list))
              (vector-set! (vector-ref pac-vis r) 0 #t))
            list)]
         
         [atl-starts
          (let ([list '()])
            (for ([c (in-range n)])
              (set! list (cons (list (- m 1) c) list))
              (vector-set! (vector-ref atl-vis (- m 1)) c #t))
            (for ([r (in-range m)])
              (set! list (cons (list r (- n 1)) list))
              (vector-set! (vector-ref atl-vis r) (- n 1) #t))
            list)])

    ;; run BFS for both oceans
    (bfs pac-starts pac-vis)
    (bfs atl-starts atl-vis)

    ;; collect intersection cells
    (let ([result '()])
      (for ([r (in-range m)])
        (for ([c (in-range n)])
          (when (and (vector-ref (vector-ref pac-vis r) c)
                     (vector-ref (vector-ref atl-vis r) c))
            (set! result (cons (list r c) result)))))
      (reverse result))))
```

## Erlang

```erlang
-module(solution).
-export([pacific_atlantic/1]).

-spec pacific_atlantic(Heights :: [[integer()]]) -> [[integer()]].
pacific_atlantic([]) ->
    [];
pacific_atlantic(Heights) ->
    M = length(Heights),
    N = length(hd(Heights)),
    HeightMap = build_height_map(Heights, 0, #{}),

    PacificStarts = start_coords(M, N, pacific),
    AtlanticStarts = start_coords(M, N, atlantic),

    VisP = bfs(PacificStarts, HeightMap, M, N, #{}),
    VisA = bfs(AtlanticStarts, HeightMap, M, N, #{}),

    Intersection = maps:fold(
        fun(Key, _, Acc) ->
            case maps:is_key(Key, VisA) of
                true -> [tuple_to_list(Key) | Acc];
                false -> Acc
            end
        end,
        [],
        VisP),
    lists:reverse(Intersection).

%% Build map from {Row,Col} to Height
build_height_map([], _, Map) ->
    Map;
build_height_map([Row|RestRows], R, Map) ->
    NewMap = build_row(Row, R, 0, Map),
    build_height_map(RestRows, R + 1, NewMap).

build_row([], _, _, Map) ->
    Map;
build_row([H|RestCols], R, C, Map) ->
    Updated = maps:put({R, C}, H, Map),
    build_row(RestCols, R, C + 1, Updated).

%% Starting coordinates for each ocean
start_coords(M, N, pacific) ->
    Top = [{0, C} || C <- lists:seq(0, N - 1)],
    Left = [{R, 0} || R <- lists:seq(0, M - 1)],
    lists:usort(Top ++ Left);
start_coords(M, N, atlantic) ->
    Bottom = [{M - 1, C} || C <- lists:seq(0, N - 1)],
    Right = [{R, N - 1} || R <- lists:seq(0, M - 1)],
    lists:usort(Bottom ++ Right).

%% BFS from given start cells
bfs([], _, _, _, Visited) ->
    Visited;
bfs([{R, C} | Rest], HeightMap, M, N, Visited) ->
    case maps:is_key({R, C}, Visited) of
        true ->
            bfs(Rest, HeightMap, M, N, Visited);
        false ->
            CurrH = maps:get({R, C}, HeightMap),
            NewVisited = maps:put({R, C}, true, Visited),
            Neighs = neighbors(R, C, M, N),
            {NewQueue, UpdatedVis} = lists:foldl(
                fun({Nr, Nc}, {QAcc, VAcc}) ->
                    case maps:is_key({Nr, Nc}, VAcc) of
                        true -> {QAcc, VAcc};
                        false ->
                            Nh = maps:get({Nr, Nc}, HeightMap),
                            if Nh >= CurrH ->
                                    {[{Nr, Nc} | QAcc], VAcc};
                               true ->
                                    {QAcc, VAcc}
                            end
                    end
                end,
                {Rest, NewVisited},
                Neighs),
            bfs(NewQueue, HeightMap, M, N, UpdatedVis)
    end.

%% Valid neighboring cells (4-directional)
neighbors(R, C, M, N) ->
    Dirs = [{-1,0}, {1,0}, {0,-1}, {0,1}],
    [ {Nr, Nc} ||
        {Dr, Dc} <- Dirs,
        Nr = R + Dr,
        Nc = C + Dc,
        Nr >= 0, Nr < M,
        Nc >= 0, Nc < N ].
```

## Elixir

```elixir
defmodule Solution do
  @spec pacific_atlantic(heights :: [[integer]]) :: [[integer]]
  def pacific_atlantic(heights) do
    m = length(heights)
    n = if m == 0, do: 0, else: length(hd(heights))

    pacific_starts =
      Enum.map(0..(n - 1), fn c -> {0, c} end) ++
        Enum.map(0..(m - 1), fn r -> {r, 0} end)

    atlantic_starts =
      Enum.map(0..(n - 1), fn c -> {m - 1, c} end) ++
        Enum.map(0..(m - 1), fn r -> {r, n - 1} end)

    pacific = bfs(pacific_starts, heights, m, n)
    atlantic = bfs(atlantic_starts, heights, m, n)

    MapSet.intersection(pacific, atlantic)
    |> Enum.map(fn {r, c} -> [r, c] end)
  end

  defp bfs(starts, heights, m, n) do
    queue = Enum.reduce(starts, :queue.new(), fn pos, acc -> :queue.in(pos, acc) end)
    visited = MapSet.new(starts)
    bfs_queue(queue, visited, heights, m, n)
  end

  defp bfs_queue(queue, visited, heights, m, n) do
    case :queue.out(queue) do
      {:empty, _} ->
        visited

      {{:value, {r, c}}, q2} ->
        cur_h = get_height(heights, r, c)

        dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

        {queue3, visited3} =
          Enum.reduce(dirs, {q2, visited}, fn {dr, dc}, {qacc, vacc} ->
            nr = r + dr
            nc = c + dc

            if nr >= 0 and nr < m and nc >= 0 and nc < n do
              nh = get_height(heights, nr, nc)

              if nh >= cur_h and not MapSet.member?(vacc, {nr, nc}) do
                {:queue.in({nr, nc}, qacc), MapSet.put(vacc, {nr, nc})}
              else
                {qacc, vacc}
              end
            else
              {qacc, vacc}
            end
          end)

        bfs_queue(queue3, visited3, heights, m, n)
    end
  end

  defp get_height(heights, r, c) do
    heights |> Enum.at(r) |> Enum.at(c)
  end
end
```

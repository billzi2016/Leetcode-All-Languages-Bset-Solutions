# 0749. Contain Virus

## Cpp

```cpp
class Solution {
public:
    int containVirus(vector<vector<int>>& isInfected) {
        const int m = isInfected.size();
        const int n = isInfected[0].size();
        const vector<pair<int,int>> dirs{{-1,0},{1,0},{0,-1},{0,1}};
        int totalWalls = 0;
        
        while (true) {
            vector<vector<int>> visited(m, vector<int>(n, 0));
            struct Region {
                vector<pair<int,int>> cells;
                unordered_set<int> frontiers;
                int walls = 0;
            };
            vector<Region> regions;
            
            // Find all infected regions
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (isInfected[i][j] == 1 && !visited[i][j]) {
                        Region reg;
                        queue<pair<int,int>> q;
                        q.emplace(i,j);
                        visited[i][j] = 1;
                        while (!q.empty()) {
                            auto [x,y] = q.front(); q.pop();
                            reg.cells.emplace_back(x,y);
                            for (auto [dx,dy]: dirs) {
                                int nx = x + dx, ny = y + dy;
                                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                                if (isInfected[nx][ny] == 0) {
                                    ++reg.walls;
                                    reg.frontiers.insert(nx * n + ny);
                                } else if (isInfected[nx][ny] == 1 && !visited[nx][ny]) {
                                    visited[nx][ny] = 1;
                                    q.emplace(nx,ny);
                                }
                            }
                        }
                        regions.push_back(std::move(reg));
                    }
                }
            }
            
            if (regions.empty()) break; // no more infected cells
            
            // Find region with largest frontier
            int idxMax = -1, maxFrontier = 0;
            for (int i = 0; i < (int)regions.size(); ++i) {
                int sz = regions[i].frontiers.size();
                if (sz > maxFrontier) {
                    maxFrontier = sz;
                    idxMax = i;
                }
            }
            
            // If no region can spread further, stop
            if (maxFrontier == 0) break;
            
            // Build walls around the chosen region
            totalWalls += regions[idxMax].walls;
            for (auto &p : regions[idxMax].cells) {
                isInfected[p.first][p.second] = -1; // contained
            }
            
            // Spread virus from other regions
            unordered_set<int> toInfect;
            for (int i = 0; i < (int)regions.size(); ++i) {
                if (i == idxMax) continue;
                for (int pos : regions[i].frontiers) {
                    toInfect.insert(pos);
                }
            }
            for (int pos : toInfect) {
                int x = pos / n;
                int y = pos % n;
                if (isInfected[x][y] == 0) isInfected[x][y] = 1;
            }
        }
        
        return totalWalls;
    }
};
```

## Java

```java
class Solution {
    public int containVirus(int[][] isInfected) {
        int m = isInfected.length;
        int n = isInfected[0].length;
        int totalWalls = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        
        while (true) {
            boolean[][] visited = new boolean[m][n];
            List<List<int[]>> regions = new ArrayList<>();
            List<Set<Integer>> frontiers = new ArrayList<>();
            List<Integer> walls = new ArrayList<>();
            
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (isInfected[i][j] == 1 && !visited[i][j]) {
                        Queue<int[]> q = new LinkedList<>();
                        q.offer(new int[]{i, j});
                        visited[i][j] = true;
                        
                        List<int[]> cells = new ArrayList<>();
                        Set<Integer> frontierSet = new HashSet<>();
                        int wallCount = 0;
                        
                        while (!q.isEmpty()) {
                            int[] cur = q.poll();
                            int x = cur[0], y = cur[1];
                            cells.add(cur);
                            
                            for (int[] d : dirs) {
                                int nx = x + d[0];
                                int ny = y + d[1];
                                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                                
                                if (isInfected[nx][ny] == 0) {
                                    wallCount++;
                                    frontierSet.add(nx * n + ny);
                                } else if (isInfected[nx][ny] == 1 && !visited[nx][ny]) {
                                    visited[nx][ny] = true;
                                    q.offer(new int[]{nx, ny});
                                }
                            }
                        }
                        
                        regions.add(cells);
                        frontiers.add(frontierSet);
                        walls.add(wallCount);
                    }
                }
            }
            
            // find region with largest frontier
            int maxIdx = -1;
            int maxFrontierSize = 0;
            for (int i = 0; i < frontiers.size(); i++) {
                int size = frontiers.get(i).size();
                if (size > maxFrontierSize) {
                    maxFrontierSize = size;
                    maxIdx = i;
                }
            }
            
            if (maxIdx == -1 || maxFrontierSize == 0) break; // no more spread possible
            
            // quarantine the chosen region
            totalWalls += walls.get(maxIdx);
            for (int[] cell : regions.get(maxIdx)) {
                isInfected[cell[0]][cell[1]] = -1; // contained
            }
            
            // spread virus from other regions
            Set<Integer> toInfect = new HashSet<>();
            for (int i = 0; i < regions.size(); i++) {
                if (i == maxIdx) continue;
                toInfect.addAll(frontiers.get(i));
            }
            for (int pos : toInfect) {
                int x = pos / n;
                int y = pos % n;
                if (isInfected[x][y] == 0) {
                    isInfected[x][y] = 1;
                }
            }
        }
        
        return totalWalls;
    }
}
```

## Python

```python
class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """
        m, n = len(isInfected), len(isInfected[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0

        while True:
            visited = [[False] * n for _ in range(m)]
            regions = []

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        queue = [(i, j)]
                        visited[i][j] = True
                        cells = []
                        frontier = set()
                        walls = 0
                        q_idx = 0
                        while q_idx < len(queue):
                            x, y = queue[q_idx]
                            q_idx += 1
                            cells.append((x, y))
                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        walls += 1
                                    elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        queue.append((nx, ny))
                        regions.append({'cells': cells, 'frontier': frontier, 'walls': walls})

            # select region with largest frontier
            max_frontier = 0
            quarantine_idx = -1
            for idx, reg in enumerate(regions):
                if len(reg['frontier']) > max_frontier:
                    max_frontier = len(reg['frontier'])
                    quarantine_idx = idx

            if max_frontier == 0:   # no more spread possible
                break

            # build walls around selected region
            ans += regions[quarantine_idx]['walls']
            for x, y in regions[quarantine_idx]['cells']:
                isInfected[x][y] = 2   # quarantined

            # spread virus from other regions
            to_infect = set()
            for idx, reg in enumerate(regions):
                if idx != quarantine_idx:
                    to_infect.update(reg['frontier'])
            for x, y in to_infect:
                if isInfected[x][y] == 0:
                    isInfected[x][y] = 1

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total_walls = 0

        while True:
            visited = [[False] * n for _ in range(m)]
            regions = []
            frontiers = []
            walls_needed = []

            # discover all infected regions
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        stack = [(i, j)]
                        visited[i][j] = True
                        region_cells = []
                        frontier_cells = set()
                        walls = 0

                        while stack:
                            x, y = stack.pop()
                            region_cells.append((x, y))
                            for dx, dy in dirs:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 0:
                                        walls += 1
                                        frontier_cells.add((nx, ny))
                                    elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        stack.append((nx, ny))

                        regions.append(region_cells)
                        frontiers.append(frontier_cells)
                        walls_needed.append(walls)

            if not regions:
                break

            # select region that threatens most uninfected cells
            max_idx = 0
            max_frontier = len(frontiers[0])
            for idx in range(1, len(regions)):
                if len(frontiers[idx]) > max_frontier:
                    max_frontier = len(frontiers[idx])
                    max_idx = idx

            # build walls around the chosen region
            total_walls += walls_needed[max_idx]
            for x, y in regions[max_idx]:
                isInfected[x][y] = 2   # mark as quarantined

            # spread virus from other regions
            for idx, frontier in enumerate(frontiers):
                if idx == max_idx:
                    continue
                for x, y in frontier:
                    if isInfected[x][y] == 0:
                        isInfected[x][y] = 1

        return total_walls
```

## C

```c
#include <stdlib.h>
#include <string.h>

int containVirus(int** isInfected, int isInfectedSize, int* isInfectedColSize) {
    int m = isInfectedSize;
    int n = isInfectedColSize[0];
    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    int totalWalls = 0;

    // auxiliary grids (max size 50)
    static int regionId[55][55];
    static int frontierSeen[55][55];
    static char infectMark[55][55];

    while (1) {
        memset(regionId, -1, sizeof(regionId));
        memset(frontierSeen, -1, sizeof(frontierSeen));

        int maxFrontier = 0;
        int maxIdx = -1;

        // store per region data
        int *walls = (int*)malloc(m*n*sizeof(int));
        int *frontSize = (int*)malloc(m*n*sizeof(int));
        int regionCnt = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (isInfected[i][j] == 1 && regionId[i][j] == -1) {
                    // BFS
                    int qx[m*n];
                    int qy[m*n];
                    int head = 0, tail = 0;
                    qx[tail] = i; qy[tail++] = j;
                    regionId[i][j] = regionCnt;

                    int wallCount = 0;
                    int frontCnt = 0;

                    while (head < tail) {
                        int x = qx[head];
                        int y = qy[head++];
                        for (int d = 0; d < 4; ++d) {
                            int nx = x + dirs[d][0];
                            int ny = y + dirs[d][1];
                            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                            if (isInfected[nx][ny] == -1) continue; // already contained
                            if (isInfected[nx][ny] == 0) {
                                wallCount++;
                                if (frontierSeen[nx][ny] != regionCnt) {
                                    frontierSeen[nx][ny] = regionCnt;
                                    frontCnt++;
                                }
                            } else if (isInfected[nx][ny] == 1 && regionId[nx][ny] == -1) {
                                regionId[nx][ny] = regionCnt;
                                qx[tail] = nx;
                                qy[tail++] = ny;
                            }
                        }
                    }

                    walls[regionCnt] = wallCount;
                    frontSize[regionCnt] = frontCnt;
                    if (frontCnt > maxFrontier) {
                        maxFrontier = frontCnt;
                        maxIdx = regionCnt;
                    }
                    ++regionCnt;
                }
            }
        }

        if (maxFrontier == 0) { // no more spread possible
            free(walls);
            free(frontSize);
            break;
        }

        totalWalls += walls[maxIdx];

        // quarantine the most threatening region
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (regionId[i][j] == maxIdx)
                    isInfected[i][j] = -1;

        // spread virus from remaining regions
        memset(infectMark, 0, sizeof(infectMark));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (isInfected[i][j] == 1) {
                    for (int d = 0; d < 4; ++d) {
                        int nx = i + dirs[d][0];
                        int ny = j + dirs[d][1];
                        if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                        if (isInfected[nx][ny] == 0 && !infectMark[nx][ny]) {
                            infectMark[nx][ny] = 1;
                        }
                    }
                }
            }
        }

        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (infectMark[i][j])
                    isInfected[i][j] = 1;

        free(walls);
        free(frontSize);
    }

    return totalWalls;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int ContainVirus(int[][] isInfected) {
        int m = isInfected.Length;
        int n = isInfected[0].Length;
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };
        int answer = 0;

        while (true) {
            bool[,] visited = new bool[m, n];
            List<List<int>> regions = new List<List<int>>();
            List<HashSet<int>> frontiers = new List<HashSet<int>>();
            List<int> perimeters = new List<int>();

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (isInfected[i][j] == 1 && !visited[i, j]) {
                        Queue<int> q = new Queue<int>();
                        q.Enqueue(i * n + j);
                        visited[i, j] = true;
                        List<int> cells = new List<int>();
                        HashSet<int> frontier = new HashSet<int>();
                        int walls = 0;

                        while (q.Count > 0) {
                            int cur = q.Dequeue();
                            int r = cur / n;
                            int c = cur % n;
                            cells.Add(cur);

                            for (int d = 0; d < 4; d++) {
                                int nr = r + dr[d];
                                int nc = c + dc[d];
                                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;

                                if (isInfected[nr][nc] == 0) {
                                    walls++;
                                    frontier.Add(nr * n + nc);
                                } else if (isInfected[nr][nc] == 1 && !visited[nr, nc]) {
                                    visited[nr, nc] = true;
                                    q.Enqueue(nr * n + nc);
                                }
                            }
                        }

                        regions.Add(cells);
                        frontiers.Add(frontier);
                        perimeters.Add(walls);
                    }
                }
            }

            // Find the region that threatens most uninfected cells
            int maxIdx = -1, maxFrontierSize = 0;
            for (int i = 0; i < frontiers.Count; i++) {
                if (frontiers[i].Count > maxFrontierSize) {
                    maxFrontierSize = frontiers[i].Count;
                    maxIdx = i;
                }
            }

            // No region can spread further
            if (maxIdx == -1) break;

            // Build walls around the chosen region
            answer += perimeters[maxIdx];
            foreach (int pos in regions[maxIdx]) {
                int r = pos / n;
                int c = pos % n;
                isInfected[r][c] = -1; // quarantined
            }

            // Spread virus from other regions
            for (int i = 0; i < regions.Count; i++) {
                if (i == maxIdx) continue;
                foreach (int pos in frontiers[i]) {
                    int r = pos / n;
                    int c = pos % n;
                    if (isInfected[r][c] == 0) {
                        isInfected[r][c] = 1;
                    }
                }
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} isInfected
 * @return {number}
 */
var containVirus = function(isInfected) {
    const m = isInfected.length;
    const n = isInfected[0].length;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let totalWalls = 0;

    while (true) {
        const visited = Array.from({length: m}, () => Array(n).fill(false));
        const regions = [];

        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (isInfected[i][j] === 1 && !visited[i][j]) {
                    const cells = [];
                    const frontierSet = new Set();
                    const frontierList = [];
                    let walls = 0;
                    const stack = [[i, j]];
                    visited[i][j] = true;

                    while (stack.length) {
                        const [x, y] = stack.pop();
                        cells.push([x, y]);

                        for (const [dx, dy] of dirs) {
                            const nx = x + dx;
                            const ny = y + dy;
                            if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;

                            if (isInfected[nx][ny] === 0) {
                                walls++;
                                const key = nx + ',' + ny;
                                if (!frontierSet.has(key)) {
                                    frontierSet.add(key);
                                    frontierList.push([nx, ny]);
                                }
                            } else if (isInfected[nx][ny] === 1 && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                stack.push([nx, ny]);
                            }
                        }
                    }

                    regions.push({cells, frontierSet, frontierList, walls});
                }
            }
        }

        if (regions.length === 0) break;

        let maxIdx = -1;
        let maxFrontierSize = 0;
        for (let i = 0; i < regions.length; i++) {
            const sz = regions[i].frontierSet.size;
            if (sz > maxFrontierSize) {
                maxFrontierSize = sz;
                maxIdx = i;
            }
        }

        if (maxFrontierSize === 0) break;

        totalWalls += regions[maxIdx].walls;

        // quarantine the most threatening region
        for (const [x, y] of regions[maxIdx].cells) {
            isInfected[x][y] = -1;
        }

        // spread virus from other regions
        for (let i = 0; i < regions.length; i++) {
            if (i === maxIdx) continue;
            for (const [x, y] of regions[i].frontierList) {
                if (isInfected[x][y] === 0) {
                    isInfected[x][y] = 1;
                }
            }
        }
    }

    return totalWalls;
};
```

## Typescript

```typescript
function containVirus(isInfected: number[][]): number {
    const m = isInfected.length;
    const n = isInfected[0].length;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let totalWalls = 0;

    while (true) {
        const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
        const regions: { cells: number[][]; frontier: Set<string>; walls: number }[] = [];

        for (let i = 0; i < m; ++i) {
            for (let j = 0; j < n; ++j) {
                if (isInfected[i][j] === 1 && !visited[i][j]) {
                    const stack: number[][] = [[i, j]];
                    visited[i][j] = true;
                    const cells: number[][] = [];
                    const frontier = new Set<string>();
                    let walls = 0;

                    while (stack.length) {
                        const [x, y] = stack.pop()!;
                        cells.push([x, y]);

                        for (const [dx, dy] of dirs) {
                            const nx = x + dx;
                            const ny = y + dy;
                            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;

                            if (isInfected[nx][ny] === 0) {
                                walls++;
                                frontier.add(`${nx},${ny}`);
                            } else if (isInfected[nx][ny] === 1 && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                stack.push([nx, ny]);
                            }
                        }
                    }

                    regions.push({ cells, frontier, walls });
                }
            }
        }

        // Find the region with the largest frontier
        let maxIdx = -1;
        let maxFrontierSize = 0;
        for (let i = 0; i < regions.length; ++i) {
            const size = regions[i].frontier.size;
            if (size > maxFrontierSize) {
                maxFrontierSize = size;
                maxIdx = i;
            }
        }

        // No more spread possible
        if (maxIdx === -1) break;

        // Quarantine the most dangerous region
        totalWalls += regions[maxIdx].walls;
        for (const [x, y] of regions[maxIdx].cells) {
            isInfected[x][y] = -1; // contained
        }

        // Spread virus from other regions
        for (let i = 0; i < regions.length; ++i) {
            if (i === maxIdx) continue;
            for (const pos of regions[i].frontier) {
                const [fxStr, fyStr] = pos.split(',');
                const fx = parseInt(fxStr, 10);
                const fy = parseInt(fyStr, 10);
                if (isInfected[fx][fy] === 0) {
                    isInfected[fx][fy] = 1;
                }
            }
        }
    }

    return totalWalls;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $isInfected
     * @return Integer
     */
    function containVirus($isInfected) {
        $m = count($isInfected);
        $n = count($isInfected[0]);
        $ans = 0;
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];
        while (true) {
            // find all infected regions
            $visited = array_fill(0, $m, array_fill(0, $n, false));
            $regions = [];
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    if ($isInfected[$i][$j] == 1 && !$visited[$i][$j]) {
                        $queue = [[$i, $j]];
                        $head = 0;
                        $visited[$i][$j] = true;
                        $cells = [];
                        $frontierSet = []; // associative set of "x,y"
                        $walls = 0;
                        while ($head < count($queue)) {
                            [$x, $y] = $queue[$head++];
                            $cells[] = [$x, $y];
                            foreach ($dirs as $d) {
                                $nx = $x + $d[0];
                                $ny = $y + $d[1];
                                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;
                                if ($isInfected[$nx][$ny] == 0) {
                                    $walls++;
                                    $key = $nx . ',' . $ny;
                                    $frontierSet[$key] = true;
                                } elseif ($isInfected[$nx][$ny] == 1 && !$visited[$nx][$ny]) {
                                    $visited[$nx][$ny] = true;
                                    $queue[] = [$nx, $ny];
                                }
                            }
                        }
                        $regions[] = [
                            'cells' => $cells,
                            'frontier' => array_keys($frontierSet),
                            'walls' => $walls
                        ];
                    }
                }
            }

            if (empty($regions)) break;

            // choose region with largest frontier
            $maxIdx = -1;
            $maxSize = 0;
            foreach ($regions as $idx => $reg) {
                $size = count($reg['frontier']);
                if ($size > $maxSize) {
                    $maxSize = $size;
                    $maxIdx = $idx;
                }
            }

            // no region can spread further
            if ($maxIdx == -1 || $maxSize == 0) break;

            // build walls for chosen region
            $ans += $regions[$maxIdx]['walls'];
            foreach ($regions[$maxIdx]['cells'] as $cell) {
                [$x, $y] = $cell;
                $isInfected[$x][$y] = 2; // quarantined
            }

            // spread virus from other regions
            for ($idx = 0; $idx < count($regions); $idx++) {
                if ($idx == $maxIdx) continue;
                foreach ($regions[$idx]['frontier'] as $key) {
                    [$x, $y] = array_map('intval', explode(',', $key));
                    if ($isInfected[$x][$y] == 0) {
                        $isInfected[$x][$y] = 1;
                    }
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
struct Region {
    var cells: [(Int, Int)]
    var frontiers: Set<Int>
    var walls: Int
}

class Solution {
    func containVirus(_ isInfected: [[Int]]) -> Int {
        var grid = isInfected
        let m = grid.count
        let n = grid[0].count
        let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        var totalWalls = 0

        while true {
            var visited = Array(repeating: Array(repeating: false, count: n), count: m)
            var regions: [Region] = []

            for i in 0..<m {
                for j in 0..<n {
                    if grid[i][j] == 1 && !visited[i][j] {
                        var queue: [(Int, Int)] = [(i, j)]
                        visited[i][j] = true
                        var idx = 0
                        var cells: [(Int, Int)] = []
                        var frontiers = Set<Int>()
                        var walls = 0

                        while idx < queue.count {
                            let (x, y) = queue[idx]
                            idx += 1
                            cells.append((x, y))

                            for d in dirs {
                                let nx = x + d.0
                                let ny = y + d.1
                                if nx < 0 || nx >= m || ny < 0 || ny >= n { continue }
                                if grid[nx][ny] == 0 {
                                    walls += 1
                                    frontiers.insert(nx * n + ny)
                                } else if grid[nx][ny] == 1 && !visited[nx][ny] {
                                    visited[nx][ny] = true
                                    queue.append((nx, ny))
                                }
                            }
                        }

                        regions.append(Region(cells: cells, frontiers: frontiers, walls: walls))
                    }
                }
            }

            if regions.isEmpty { break }

            var maxIdx = -1
            var maxFrontier = 0
            for (idx, reg) in regions.enumerated() {
                if reg.frontiers.count > maxFrontier {
                    maxFrontier = reg.frontiers.count
                    maxIdx = idx
                }
            }

            if maxFrontier == 0 { break }

            let selected = regions[maxIdx]
            totalWalls += selected.walls
            for (x, y) in selected.cells {
                grid[x][y] = -1   // quarantined region
            }

            for (idx, reg) in regions.enumerated() where idx != maxIdx {
                for pos in reg.frontiers {
                    let x = pos / n
                    let y = pos % n
                    if grid[x][y] == 0 {
                        grid[x][y] = 1
                    }
                }
            }
        }

        return totalWalls
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun containVirus(isInfected: Array<IntArray>): Int {
        val m = isInfected.size
        val n = isInfected[0].size
        var answer = 0
        val dirs = arrayOf(intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1))

        while (true) {
            val visited = Array(m) { BooleanArray(n) }
            val regions = mutableListOf<Region>()

            for (i in 0 until m) {
                for (j in 0 until n) {
                    if (isInfected[i][j] == 1 && !visited[i][j]) {
                        val cells = mutableListOf<Pair<Int, Int>>()
                        val frontier = mutableSetOf<Int>()
                        var walls = 0
                        val q: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
                        q.add(Pair(i, j))
                        visited[i][j] = true

                        while (q.isNotEmpty()) {
                            val (x, y) = q.removeFirst()
                            cells.add(Pair(x, y))

                            for (d in dirs) {
                                val nx = x + d[0]
                                val ny = y + d[1]
                                if (nx !in 0 until m || ny !in 0 until n) continue
                                when (isInfected[nx][ny]) {
                                    0 -> {
                                        walls++
                                        frontier.add(nx * n + ny)
                                    }
                                    1 -> {
                                        if (!visited[nx][ny]) {
                                            visited[nx][ny] = true
                                            q.add(Pair(nx, ny))
                                        }
                                    }
                                }
                            }
                        }

                        regions.add(Region(cells, frontier, walls))
                    }
                }
            }

            if (regions.isEmpty()) break

            var maxIdx = -1
            var maxFrontierSize = 0
            for (idx in regions.indices) {
                val sz = regions[idx].frontier.size
                if (sz > maxFrontierSize) {
                    maxFrontierSize = sz
                    maxIdx = idx
                }
            }

            if (maxFrontierSize == 0) break

            // Quarantine the most threatening region
            answer += regions[maxIdx].walls
            for ((x, y) in regions[maxIdx].cells) {
                isInfected[x][y] = -1
            }

            // Spread virus from other regions
            for (idx in regions.indices) {
                if (idx == maxIdx) continue
                for (pos in regions[idx].frontier) {
                    val x = pos / n
                    val y = pos % n
                    if (isInfected[x][y] == 0) {
                        isInfected[x][y] = 1
                    }
                }
            }
        }

        return answer
    }

    private data class Region(
        val cells: MutableList<Pair<Int, Int>>,
        val frontier: MutableSet<Int>,
        var walls: Int
    )
}
```

## Dart

```dart
import 'dart:collection';

class _Point {
  int x, y;
  _Point(this.x, this.y);
}

class Solution {
  int containVirus(List<List<int>> isInfected) {
    int m = isInfected.length;
    int n = isInfected[0].length;
    const List<int> dx = [1, -1, 0, 0];
    const List<int> dy = [0, 0, 1, -1];

    int totalWalls = 0;

    while (true) {
      List<List<_Point>> regionsCells = [];
      List<Set<int>> regionsFrontiers = [];
      List<int> wallsList = [];

      List<List<bool>> visited =
          List.generate(m, (_) => List.filled(n, false));

      for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
          if (isInfected[i][j] == 1 && !visited[i][j]) {
            Queue<_Point> q = Queue();
            q.add(_Point(i, j));
            visited[i][j] = true;

            List<_Point> cells = [];
            Set<int> frontier = {};
            int walls = 0;

            while (q.isNotEmpty) {
              _Point p = q.removeFirst();
              cells.add(p);
              for (int dir = 0; dir < 4; ++dir) {
                int ni = p.x + dx[dir];
                int nj = p.y + dy[dir];
                if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
                if (isInfected[ni][nj] == 0) {
                  walls++;
                  frontier.add(ni * n + nj);
                } else if (isInfected[ni][nj] == 1 && !visited[ni][nj]) {
                  visited[ni][nj] = true;
                  q.add(_Point(ni, nj));
                }
              }
            }

            regionsCells.add(cells);
            regionsFrontiers.add(frontier);
            wallsList.add(walls);
          }
        }
      }

      // Find the region with the largest frontier
      int maxIdx = -1;
      int maxSize = 0;
      for (int i = 0; i < regionsFrontiers.length; ++i) {
        if (regionsFrontiers[i].length > maxSize) {
          maxSize = regionsFrontiers[i].length;
          maxIdx = i;
        }
      }

      // No more spread possible
      if (maxIdx == -1 || maxSize == 0) break;

      // Build walls around the most threatening region
      totalWalls += wallsList[maxIdx];
      for (var p in regionsCells[maxIdx]) {
        isInfected[p.x][p.y] = -1; // quarantined
      }

      // Spread virus from other regions
      Set<int> toInfect = {};
      for (int i = 0; i < regionsFrontiers.length; ++i) {
        if (i == maxIdx) continue;
        toInfect.addAll(regionsFrontiers[i]);
      }
      for (int idx in toInfect) {
        int r = idx ~/ n;
        int c = idx % n;
        if (isInfected[r][c] == 0) {
          isInfected[r][c] = 1;
        }
      }
    }

    return totalWalls;
  }
}
```

## Golang

```go
func containVirus(isInfected [][]int) int {
	m, n := len(isInfected), len(isInfected[0])
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	totalWalls := 0

	for {
		visited := make([][]bool, m)
		for i := range visited {
			visited[i] = make([]bool, n)
		}
		var regions [][][2]int
		var frontiers []map[int]struct{}
		var wallsList []int

		// discover all infected regions
		for i := 0; i < m; i++ {
			for j := 0; j < n; j++ {
				if isInfected[i][j] == 1 && !visited[i][j] {
					queue := [][2]int{{i, j}}
					visited[i][j] = true
					cells := make([][2]int, 0)
					frontier := make(map[int]struct{})
					walls := 0

					for q := 0; q < len(queue); q++ {
						x, y := queue[q][0], queue[q][1]
						cells = append(cells, [2]int{x, y})
						for _, d := range dirs {
							nx, ny := x+d[0], y+d[1]
							if nx < 0 || nx >= m || ny < 0 || ny >= n {
								continue
							}
							if isInfected[nx][ny] == 0 {
								walls++
								key := nx*n + ny
								frontier[key] = struct{}{}
							} else if isInfected[nx][ny] == 1 && !visited[nx][ny] {
								visited[nx][ny] = true
								queue = append(queue, [2]int{nx, ny})
							}
						}
					}

					regions = append(regions, cells)
					frontiers = append(frontiers, frontier)
					wallsList = append(wallsList, walls)
				}
			}
		}

		// select region with largest frontier
		maxIdx := -1
		maxSize := 0
		for i, f := range frontiers {
			if len(f) > maxSize {
				maxSize = len(f)
				maxIdx = i
			}
		}
		if maxIdx == -1 || maxSize == 0 {
			break
		}

		// build walls around selected region
		totalWalls += wallsList[maxIdx]
		for _, cell := range regions[maxIdx] {
			isInfected[cell[0]][cell[1]] = 2 // quarantined
		}

		// spread virus from other regions
		for i, f := range frontiers {
			if i == maxIdx {
				continue
			}
			for key := range f {
				x, y := key/n, key%n
				if isInfected[x][y] == 0 {
					isInfected[x][y] = 1
				}
			}
		}
	}

	return totalWalls
}
```

## Ruby

```ruby
require 'set'

# @param {Integer[][]} is_infected
# @return {Integer}
def contain_virus(is_infected)
  m = is_infected.size
  n = is_infected[0].size
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  answer = 0

  loop do
    visited = Array.new(m) { Array.new(n, false) }
    regions = []

    (0...m).each do |i|
      (0...n).each do |j|
        next unless is_infected[i][j] == 1 && !visited[i][j]

        cells = []
        frontiers = Set.new
        walls = 0
        stack = [[i, j]]
        visited[i][j] = true

        until stack.empty?
          r, c = stack.pop
          cells << [r, c]
          dirs.each do |dr, dc|
            nr = r + dr
            nc = c + dc
            next unless nr.between?(0, m - 1) && nc.between?(0, n - 1)

            if is_infected[nr][nc] == 0
              walls += 1
              frontiers << [nr, nc]
            elsif is_infected[nr][nc] == 1 && !visited[nr][nc]
              visited[nr][nc] = true
              stack << [nr, nc]
            end
          end
        end

        regions << { cells: cells, frontiers: frontiers, walls: walls }
      end
    end

    # Find region with the largest frontier
    max_frontier = 0
    quarantine_idx = -1
    regions.each_with_index do |reg, idx|
      sz = reg[:frontiers].size
      if sz > max_frontier
        max_frontier = sz
        quarantine_idx = idx
      end
    end

    break if max_frontier == 0 # no more spread possible

    # Quarantine the selected region
    quarantine = regions[quarantine_idx]
    answer += quarantine[:walls]
    quarantine[:cells].each do |r, c|
      is_infected[r][c] = -1
    end

    # Spread virus from other regions
    regions.each_with_index do |reg, idx|
      next if idx == quarantine_idx
      reg[:frontiers].each do |cell|
        r, c = cell
        is_infected[r][c] = 1 if is_infected[r][c] == 0
      end
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
  def containVirus(isInfected: Array[Array[Int]]): Int = {
    val m = isInfected.length
    val n = isInfected(0).length
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    var totalWalls = 0

    while (true) {
      val visited = Array.ofDim[Boolean](m, n)
      import scala.collection.mutable.{ArrayBuffer, Set, Queue}
      val regions = new ArrayBuffer[(ArrayBuffer[(Int, Int)], Set[(Int, Int)], Int)]()

      for (i <- 0 until m; j <- 0 until n) {
        if (isInfected(i)(j) == 1 && !visited(i)(j)) {
          val cells = new ArrayBuffer[(Int, Int)]()
          val frontier = Set.empty[(Int, Int)]
          var walls = 0
          val q = Queue.empty[(Int, Int)]
          q.enqueue((i, j))
          visited(i)(j) = true

          while (q.nonEmpty) {
            val (x, y) = q.dequeue()
            cells.append((x, y))
            for ((dx, dy) <- dirs) {
              val nx = x + dx
              val ny = y + dy
              if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                isInfected(nx)(ny) match {
                  case 0 =>
                    walls += 1
                    frontier.add((nx, ny))
                  case 1 =>
                    if (!visited(nx)(ny)) {
                      visited(nx)(ny) = true
                      q.enqueue((nx, ny))
                    }
                  case -1 => // already contained, treat as wall
                }
              } else {
                // outside grid, no wall needed
              }
            }
          }

          regions.append((cells, frontier, walls))
        }
      }

      if (regions.isEmpty) return totalWalls

      var maxIdx = -1
      var maxFrontierSize = 0
      for (idx <- regions.indices) {
        val sz = regions(idx)._2.size
        if (sz > maxFrontierSize) {
          maxFrontierSize = sz
          maxIdx = idx
        }
      }

      if (maxFrontierSize == 0) return totalWalls

      // Quarantine the most threatening region
      val (quarCells, _, quarWalls) = regions(maxIdx)
      totalWalls += quarWalls
      for ((x, y) <- quarCells) {
        isInfected(x)(y) = -1
      }

      // Spread virus from other regions
      val toInfect = Set.empty[(Int, Int)]
      for (idx <- regions.indices if idx != maxIdx) {
        toInfect ++= regions(idx)._2
      }
      for ((x, y) <- toInfect) {
        isInfected(x)(y) = 1
      }
    }

    totalWalls // unreachable
  }
}
```

## Rust

```rust
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn contain_virus(is_infected: Vec<Vec<i32>>) -> i32 {
        let m = is_infected.len();
        let n = is_infected[0].len();
        let mut grid = is_infected;
        let dirs = [(-1i32, 0i32), (1, 0), (0, -1), (0, 1)];
        let mut answer: i32 = 0;

        loop {
            let mut visited = vec![vec![false; n]; m];
            let mut regions: Vec<Vec<(usize, usize)>> = Vec::new();
            let mut frontiers: Vec<HashSet<(usize, usize)>> = Vec::new();
            let mut perimeters: Vec<i32> = Vec::new();

            for i in 0..m {
                for j in 0..n {
                    if grid[i][j] == 1 && !visited[i][j] {
                        let mut q = VecDeque::new();
                        q.push_back((i, j));
                        visited[i][j] = true;
                        let mut cells: Vec<(usize, usize)> = Vec::new();
                        let mut frontier_set: HashSet<(usize, usize)> = HashSet::new();
                        let mut perimeter: i32 = 0;

                        while let Some((x, y)) = q.pop_front() {
                            cells.push((x, y));
                            for (dx, dy) in dirs.iter() {
                                let nx = x as i32 + dx;
                                let ny = y as i32 + dy;
                                if nx < 0 || ny < 0 || nx >= m as i32 || ny >= n as i32 {
                                    continue;
                                }
                                let ux = nx as usize;
                                let uy = ny as usize;
                                match grid[ux][uy] {
                                    0 => {
                                        perimeter += 1;
                                        frontier_set.insert((ux, uy));
                                    }
                                    1 => {
                                        if !visited[ux][uy] {
                                            visited[ux][uy] = true;
                                            q.push_back((ux, uy));
                                        }
                                    }
                                    _ => {} // -1 (quarantined) or other values are ignored
                                }
                            }
                        }

                        regions.push(cells);
                        frontiers.push(frontier_set);
                        perimeters.push(perimeter);
                    }
                }
            }

            // Find the region with the largest frontier
            let mut max_idx: Option<usize> = None;
            let mut max_frontier_size: usize = 0;
            for (idx, fset) in frontiers.iter().enumerate() {
                if fset.len() > max_frontier_size {
                    max_frontier_size = fset.len();
                    max_idx = Some(idx);
                }
            }

            // No more spread possible
            if max_idx.is_none() || max_frontier_size == 0 {
                break;
            }

            let quarantine_idx = max_idx.unwrap();

            // Build walls for the chosen region
            answer += perimeters[quarantine_idx];

            // Quarantine: mark its cells as -1
            for &(x, y) in &regions[quarantine_idx] {
                grid[x][y] = -1;
            }

            // Spread virus from other regions
            for (idx, fset) in frontiers.iter().enumerate() {
                if idx == quarantine_idx {
                    continue;
                }
                for &(x, y) in fset {
                    if grid[x][y] == 0 {
                        grid[x][y] = 1;
                    }
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (contain-virus isInfected)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length isInfected))
         (cols (if (= rows 0) 0 (length (first isInfected))))
         (grid (list->vector
                (map (lambda (row) (list->vector row)) isInfected)))
         (dirs '((-1 . 0) (1 . 0) (0 . -1) (0 . 1))))
    (define (in-bounds i j)
      (and (>= i 0) (< i rows) (>= j 0) (< j cols)))
    (define (get i j)
      (vector-ref (vector-ref grid i) j))
    (define (set-cell i j v)
      (vector-set! (vector-ref grid i) j v))
    (let loop ((walls 0))
      ;; discover all infected regions
      (let ((visited (make-vector rows)))
        (do ((i 0 (+ i 1))) ((= i rows))
          (vector-set! visited i (make-vector cols #f)))
        (define regions '())
        (do ((i 0 (+ i 1))) ((= i rows))
          (do ((j 0 (+ j 1))) ((= j cols))
            (when (and (= (get i j) 1)
                       (not (vector-ref (vector-ref visited i) j)))
              ;; BFS for a region
              (let ((stack (list (cons i j)))
                    (cells '())
                    (frontier (make-hash))
                    (perim 0))
                (vector-set! (vector-ref visited i) j #t)
                (let bfs ()
                  (when (not (null? stack))
                    (define cur (car stack))
                    (set! stack (cdr stack))
                    (define ci (car cur))
                    (define cj (cdr cur))
                    (set! cells (cons cur cells))
                    (for ([d dirs])
                      (define ni (+ ci (car d)))
                      (define nj (+ cj (cdr d)))
                      (when (in-bounds ni nj)
                        (define val (get ni nj))
                        (cond
                          [(= val 0)
                           (hash-set! frontier (cons ni nj) #t)
                           (set! perim (+ perim 1))]
                          [(and (= val 1)
                                (not (vector-ref (vector-ref visited ni) nj)))
                           (vector-set! (vector-ref visited ni) nj #t)
                           (set! stack (cons (cons ni nj) stack))])))
                    (bfs))))
                (set! regions (cons (list cells frontier perim) regions)))))))
        (if (null? regions)
            walls
            (let* ((max-frontier -1)
                   (best-region #f))
              (for ([r regions])
                (define fsize (hash-count (cadr r)))
                (when (> fsize max-frontier)
                  (set! max-frontier fsize)
                  (set! best-region r)))
              (if (= max-frontier 0)
                  walls
                  (let ((new-walls (+ walls (caddr best-region))))
                    ;; quarantine the chosen region
                    (for ([pos (car best-region)])
                      (set-cell (car pos) (cdr pos) -1))
                    ;; spread virus from other regions
                    (let ((toInfect (make-hash)))
                      (for ([r regions])
                        (unless (eq? r best-region)
                          (hash-for-each (cadr r)
                                         (lambda (k v) (hash-set! toInfect k #t)))))
                      (hash-for-each toInfect
                                     (lambda (k v)
                                       (define i (car k))
                                       (define j (cdr k))
                                       (when (= (get i j) 0)
                                         (set-cell i j 1))))
                      (loop new-walls))))))))))
```

## Erlang

```erlang
-module(solution).
-export([contain_virus/1]).

-spec contain_virus(IsInfected :: [[integer()]]) -> integer().
contain_virus(IsInfected) ->
    M = length(IsInfected),
    N = case IsInfected of [] -> 0; [Row|_] -> length(Row) end,
    GridMap = build_map(IsInfected, 0, #{}),
    loop(GridMap, M, N, 0).

build_map([], _, Acc) -> Acc;
build_map([Row|Rest], R, Acc) ->
    Acc1 = build_row(Row, R, 0, Acc),
    build_map(Rest, R + 1, Acc1).

build_row([], _, _, Acc) -> Acc;
build_row([Val|RestVals], R, C, Acc) ->
    NewAcc = maps:put({R, C}, Val, Acc),
    build_row(RestVals, R, C + 1, NewAcc).

loop(GridMap, M, N, Walls) ->
    Regions = find_regions(GridMap, M, N),
    case Regions of
        [] -> Walls;
        _ ->
            MaxRegion = select_max_region(Regions),
            case MaxRegion of
                undefined -> Walls;
                {SelRegCells, SelFrontier, SelPerim} ->
                    if sets:size(SelFrontier) == 0 ->
                        Walls;
                       true ->
                         NewWalls = Walls + SelPerim,
                         Grid1 = set_cells(GridMap, SelRegCells, 2),
                         FrontiersUnion =
                             lists:foldl(
                               fun({_, F, _}, Acc) ->
                                   case F == SelFrontier of
                                       true -> Acc;
                                       false -> sets:union(F, Acc)
                                   end
                               end,
                               sets:new(),
                               Regions),
                         Grid2 = set_cells(Grid1, FrontiersUnion, 1),
                         loop(Grid2, M, N, NewWalls)
                    end
            end
    end.

find_regions(GridMap, M, N) ->
    {_, RegionsRev} =
        maps:fold(
          fun(Pos, Val, {VisitedAcc, RegsAcc}) ->
              case Val of
                  1 when not sets:is_element(Pos, VisitedAcc) ->
                      {RegionSet, FrontierSet, Perim, NewVisited} = bfs(Pos, GridMap, M, N, VisitedAcc),
                      {NewVisited, [{RegionSet, FrontierSet, Perim} | RegsAcc]};
                  _ -> {VisitedAcc, RegsAcc}
              end
          end,
          {sets:new(), []},
          GridMap),
    lists:reverse(RegionsRev).

bfs(StartPos, GridMap, M, N, Visited0) ->
    bfs_queue([StartPos], sets:add_element(StartPos, Visited0), sets:new(), sets:new(), 0, GridMap, M, N).

bfs_queue([], Visited, RegionSet, FrontierSet, Perim, _GM, _M, _N) ->
    {RegionSet, FrontierSet, Perim, Visited};
bfs_queue([Cur | RestQueue], Visited, RegionSet, FrontierSet, Perim, GridMap, M, N) ->
    RegSet1 = sets:add_element(Cur, RegionSet),
    {NewQueue, NewVisited, NewFrontier, AddPerim} =
        bfs_neighbors(Cur, RestQueue, Visited, FrontierSet, GridMap, M, N),
    bfs_queue(NewQueue, NewVisited, RegSet1, NewFrontier, Perim + AddPerim,
              GridMap, M, N).

bfs_neighbors({R, C}, QueueAcc, Visited, FrontierSet, GridMap, M, N) ->
    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
    bfs_dirs(Directions, {R, C}, QueueAcc, Visited, FrontierSet, 0,
             GridMap, M, N).

bfs_dirs([], _Pos, Q, V, F, PerimAcc, _GM, _M, _N) ->
    {Q, V, F, PerimAcc};
bfs_dirs([{DR, DC} | Rest], {R, C}, QueueAcc, Visited, FrontierSet,
         PerimAcc, GridMap, M, N) ->
    NR = R + DR,
    NC = C + DC,
    if NR < 0 orelse NR >= M orelse NC < 0 orelse NC >= N ->
            bfs_dirs(Rest, {R, C}, QueueAcc, Visited, FrontierSet,
                     PerimAcc, GridMap, M, N);
       true ->
            Val = maps:get({NR, NC}, GridMap, 0),
            case Val of
                1 ->
                    if sets:is_element({NR, NC}, Visited) ->
                            bfs_dirs(Rest, {R, C}, QueueAcc, Visited,
                                     FrontierSet, PerimAcc, GridMap, M, N);
                       true ->
                            NewVisited = sets:add_element({NR, NC}, Visited),
                            bfs_dirs(Rest, {R, C},
                                     [{NR, NC} | QueueAcc], NewVisited,
                                     FrontierSet, PerimAcc, GridMap, M, N)
                    end;
                0 ->
                    NewFrontier = sets:add_element({NR, NC}, FrontierSet),
                    bfs_dirs(Rest, {R, C}, QueueAcc, Visited,
                             NewFrontier, PerimAcc + 1, GridMap, M, N);
                _ -> % value 2 or others
                    bfs_dirs(Rest, {R, C}, QueueAcc, Visited,
                             FrontierSet, PerimAcc, GridMap, M, N)
            end
    end.

select_max_region(Regions) ->
    case Regions of
        [] -> undefined;
        _ ->
            MaxSize = lists:max([sets:size(F) || {_R, F, _P} <- Regions]),
            [Region] = [Reg || Reg={_,F,_} <- Regions,
                               sets:size(F) == MaxSize],
            Region
    end.

set_cells(GridMap, PosSet, Val) ->
    lists:foldl(fun(Pos, Acc) -> maps:put(Pos, Val, Acc) end,
                GridMap,
                sets:to_list(PosSet)).
```

## Elixir

```elixir
defmodule Solution do
  @spec contain_virus(is_infected :: [[integer]]) :: integer
  def contain_virus(is_infected) do
    m = length(is_infected)
    n = if m == 0, do: 0, else: is_infected |> List.first() |> length()
    loop(is_infected, m, n, 0)
  end

  # Main simulation loop
  defp loop(grid, m, n, ans) do
    {regions, _} = find_regions(grid, m, n)

    regions_with_frontier =
      Enum.filter(regions, fn r -> MapSet.size(r.frontier) > 0 end)

    if regions_with_frontier == [] do
      ans
    else
      {max_region, other_regions} = pick_max(regions_with_frontier)
      ans2 = ans + max_region.perimeter
      grid1 = quarantine(grid, max_region.cells)
      grid2 = spread(grid1, other_regions, m, n)
      loop(grid2, m, n, ans2)
    end
  end

  # Find all infected regions (value == 1)
  defp find_regions(grid, m, n) do
    visited = MapSet.new()
    {regions, _visited} =
      Enum.reduce(0..(m - 1), {[], visited}, fn i, {regs, vis} ->
        Enum.reduce(0..(n - 1), {regs, vis}, fn j, {regs2, vis2} ->
          if get(grid, i, j) == 1 and not MapSet.member?(vis2, {i, j}) do
            {region, new_vis} = bfs(i, j, grid, m, n, vis2)
            {[region | regs2], new_vis}
          else
            {regs2, vis2}
          end
        end)
      end)

    {Enum.reverse(regions), visited}
  end

  # BFS to collect a region's cells, frontier and perimeter
  defp bfs(i, j, grid, m, n, visited) do
    stack = [{i, j}]
    visited = MapSet.put(visited, {i, j})
    cells = []
    frontier = MapSet.new()
    perimeter = 0

    {cells, frontier, perimeter, visited} =
      bfs_process(stack, grid, m, n, visited, cells, frontier, perimeter)

    {%{cells: cells, frontier: frontier, perimeter: perimeter}, visited}
  end

  defp bfs_process([], _grid, _m, _n, visited, cells, frontier, perim) do
    {cells, frontier, perim, visited}
  end

  defp bfs_process([{i, j} | rest], grid, m, n, visited, cells, frontier, perim) do
    cells = [{i, j} | cells]

    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    {visited2, stack2, frontier2, perim2} =
      Enum.reduce(dirs, {visited, rest, frontier, perim}, fn {dx, dy},
                                                             {vis, stk, fr, p} ->
        ni = i + dx
        nj = j + dy

        cond do
          ni < 0 or ni >= m or nj < 0 or nj >= n ->
            {vis, stk, fr, p}

          true ->
            val = get(grid, ni, nj)

            cond do
              val == 0 ->
                {vis, stk, MapSet.put(fr, {ni, nj}), p + 1}

              val == 1 and not MapSet.member?(vis, {ni, nj}) ->
                {MapSet.put(vis, {ni, nj}), [{ni, nj} | stk], fr, p}

              true ->
                # val == 2 or already visited infected cell
                {vis, stk, fr, p}
            end
        end
      end)

    bfs_process(stack2, grid, m, n, visited2, cells, frontier2, perim2)
  end

  # Choose region with largest frontier size
  defp pick_max(regions) do
    {max_region, idx} =
      regions
      |> Enum.with_index()
      |> Enum.max_by(fn {reg, _idx} -> MapSet.size(reg.frontier) end)

    other_regions = List.delete_at(regions, idx)
    {max_region, other_regions}
  end

  # Quarantine selected region (set its cells to 2)
  defp quarantine(grid, cells) do
    Enum.reduce(cells, grid, fn {i, j}, acc -> set(acc, i, j, 2) end)
  end

  # Spread virus from remaining regions into their frontiers
  defp spread(grid, regions, _m, _n) do
    Enum.reduce(regions, grid, fn region, acc ->
      Enum.reduce(region.frontier, acc, fn {i, j}, g ->
        if get(g, i, j) == 0 do
          set(g, i, j, 1)
        else
          g
        end
      end)
    end)
  end

  # Helper to get value at (i,j)
  defp get(grid, i, j) do
    row = Enum.at(grid, i)
    Enum.at(row, j)
  end

  # Helper to set value at (i,j), returns new grid
  defp set(grid, i, j, val) do
    row = Enum.at(grid, i)
    new_row = List.replace_at(row, j, val)
    List.replace_at(grid, i, new_row)
  end
end
```

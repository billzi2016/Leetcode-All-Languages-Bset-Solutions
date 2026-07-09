# 2258. Escape the Spreading Fire

## Cpp

```cpp
class Solution {
public:
    int maximumMinutes(vector<vector<int>>& grid) {
        const int m = grid.size();
        const int n = grid[0].size();
        const int INF = 1e9;
        vector<vector<int>> fireDist(m, vector<int>(n, INF));
        queue<pair<int,int>> q;
        // multi-source BFS for fire
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 2) {
                    fireDist[i][j] = 0;
                    q.emplace(i, j);
                }
            }
        }
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty()) {
            auto [x,y] = q.front(); q.pop();
            for (auto &d: dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx<0||ny<0||nx>=m||ny>=n) continue;
                if (grid[nx][ny] == 1) continue; // wall blocks fire
                if (fireDist[nx][ny] != INF) continue;
                fireDist[nx][ny] = fireDist[x][y] + 1;
                q.emplace(nx, ny);
            }
        }
        // check reachability ignoring fire
        auto reachableWithoutFire = [&]() -> bool {
            vector<vector<int>> vis(m, vector<int>(n, 0));
            queue<pair<int,int>> qq;
            if (grid[0][0] == 1) return false;
            qq.emplace(0,0);
            vis[0][0]=1;
            while(!qq.empty()){
                auto [x,y]=qq.front();qq.pop();
                if(x==m-1 && y==n-1) return true;
                for(auto &d:dirs){
                    int nx=x+d[0], ny=y+d[1];
                    if(nx<0||ny<0||nx>=m||ny>=n) continue;
                    if(grid[nx][ny]==1||vis[nx][ny]) continue;
                    vis[nx][ny]=1;
                    qq.emplace(nx,ny);
                }
            }
            return false;
        };
        if (!reachableWithoutFire()) return -1;
        if (fireDist[m-1][n-1] == INF) return 1000000000;
        
        auto canReach = [&](int wait)->bool{
            if (wait >= fireDist[0][0]) return false; // start burns before we move
            vector<vector<int>> best(m, vector<int>(n, INF));
            queue<tuple<int,int,int>> qq;
            best[0][0] = wait;
            qq.emplace(0,0,wait);
            while(!qq.empty()){
                auto [x,y,t]=qq.front(); qq.pop();
                if (x==m-1 && y==n-1) return true; // arrival time already < fireDist due to checks below
                for(auto &d:dirs){
                    int nx=x+d[0], ny=y+d[1];
                    if(nx<0||ny<0||nx>=m||ny>=n) continue;
                    if(grid[nx][ny]==1) continue;
                    int nt = t+1;
                    if (nt >= fireDist[nx][ny]) continue; // cannot step into or stay on burning cell
                    if (nt < best[nx][ny]){
                        best[nx][ny]=nt;
                        qq.emplace(nx,ny,nt);
                    }
                }
            }
            return false;
        };
        
        int lo = 0, hi = m*n; // upper bound sufficient
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (canReach(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    private static final int INF = 1_000_000_007;
    private static final int[] DX = {1, -1, 0, 0};
    private static final int[] DY = {0, 0, 1, -1};

    public int maximumMinutes(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] fireDist = new int[m][n];
        for (int i = 0; i < m; i++) {
            java.util.Arrays.fill(fireDist[i], INF);
        }

        java.util.ArrayDeque<int[]> q = new java.util.ArrayDeque<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    fireDist[i][j] = 0;
                    q.add(new int[]{i, j});
                }
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            int d = fireDist[x][y];
            for (int dir = 0; dir < 4; dir++) {
                int nx = x + DX[dir];
                int ny = y + DY[dir];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] == 1) continue; // wall
                if (fireDist[nx][ny] > d + 1) {
                    fireDist[nx][ny] = d + 1;
                    q.add(new int[]{nx, ny});
                }
            }
        }

        int low = 0, high = 1_000_000_000;
        int ans = -1;
        while (low <= high) {
            int mid = low + ((high - low) >> 1);
            if (canReach(grid, fireDist, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans == 1_000_000_000 ? 1_000_000_000 : ans;
    }

    private boolean canReach(int[][] grid, int[][] fireDist, int wait) {
        int m = grid.length, n = grid[0].length;
        if (wait >= fireDist[0][0]) return false; // start would be on fire

        java.util.ArrayDeque<int[]> q = new java.util.ArrayDeque<>();
        boolean[][] visited = new boolean[m][n];
        q.add(new int[]{0, 0, wait});
        visited[0][0] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1], t = cur[2];

            if (x == m - 1 && y == n - 1) {
                // destination: can arrive at same time as fire
                return t <= fireDist[x][y];
            }

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + DX[dir];
                int ny = y + DY[dir];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] == 1) continue; // wall
                if (visited[nx][ny]) continue;

                int nt = t + 1;
                if (nx == m - 1 && ny == n - 1) {
                    if (nt <= fireDist[nx][ny]) {
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny, nt});
                    }
                } else {
                    if (nt < fireDist[nx][ny]) {
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny, nt});
                    }
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        INF = 10**9

        # multi-source BFS for fire spread times
        fire_dist = [[INF] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    fire_dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            i, j = q.popleft()
            d = fire_dist[i][j]
            nd = d + 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != 1 and fire_dist[ni][nj] == INF:
                    fire_dist[ni][nj] = nd
                    q.append((ni, nj))

        # If destination never catches fire -> answer is 10^9
        if fire_dist[m-1][n-1] == INF:
            return 10**9

        dest = (m-1, n-1)

        def can(wait):
            # cannot stay longer than fire reaches start
            if wait >= fire_dist[0][0]:
                return False
            visited = [[False]*n for _ in range(m)]
            dq = deque()
            dq.append((0, 0, wait))
            visited[0][0] = True
            while dq:
                i, j, t = dq.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == 1:
                        continue
                    nt = t + 1
                    # destination special condition: can arrive at same time as fire
                    if (ni, nj) == dest:
                        if nt <= fire_dist[ni][nj]:
                            return True
                        else:
                            continue
                    if nt < fire_dist[ni][nj] and not visited[ni][nj]:
                        visited[ni][nj] = True
                        dq.append((ni, nj, nt))
            return False

        # binary search maximum waiting time
        lo, hi = 0, 10**9  # hi large enough
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo if can(lo) else -1
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**9

        # Multi-source BFS for fire spread times
        fire_dist = [[INF] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    fire_dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x, y = q.popleft()
            d = fire_dist[x][y]
            nd = d + 1
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 1 and fire_dist[nx][ny] == INF:
                    fire_dist[nx][ny] = nd
                    q.append((nx, ny))

        # If destination never catches fire -> answer is 1e9
        if fire_dist[m-1][n-1] == INF:
            return 10**9

        def can_reach(wait: int) -> bool:
            if fire_dist[0][0] <= wait:
                return False
            visited = [[False]*n for _ in range(m)]
            dq = deque()
            dq.append((0, 0, wait))
            visited[0][0] = True
            while dq:
                x, y, t = dq.popleft()
                if (x, y) == (m-1, n-1):
                    return True
                nt = t + 1
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 1:
                        # must arrive before fire reaches the cell
                        if nt >= fire_dist[nx][ny]:
                            continue
                        visited[nx][ny] = True
                        dq.append((nx, ny, nt))
            return False

        low, high = 0, fire_dist[m-1][n-1] - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 1000000000

static int m, n;
static int *fireDist;   // size m*n
static int **gridPtr;

int bfs_can(int wait) {
    if (wait >= fireDist[0]) return 0; // start burns before we leave

    int total = m * n;
    char *vis = (char *)calloc(total, sizeof(char));
    if (!vis) return 0;

    // queues
    int *qx = (int *)malloc(total * sizeof(int));
    int *qy = (int *)malloc(total * sizeof(int));
    int *qs = (int *)malloc(total * sizeof(int));
    int head = 0, tail = 0;

    qx[tail] = 0;
    qy[tail] = 0;
    qs[tail] = 0; // steps taken from start
    vis[0] = 1;
    tail++;

    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    while (head < tail) {
        int x = qx[head];
        int y = qy[head];
        int steps = qs[head];
        head++;

        if (x == m - 1 && y == n - 1) {
            free(vis); free(qx); free(qy); free(qs);
            return 1;
        }

        for (int d = 0; d < 4; ++d) {
            int nx = x + dirs[d][0];
            int ny = y + dirs[d][1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (gridPtr[nx][ny] == 1) continue; // wall
            int idx = nx * n + ny;
            if (vis[idx]) continue;

            int arrival = wait + steps + 1;
            if (nx == m - 1 && ny == n - 1) {
                if (arrival <= fireDist[idx]) {
                    vis[idx] = 1;
                    qx[tail] = nx; qy[tail] = ny; qs[tail] = steps + 1;
                    tail++;
                }
            } else {
                if (arrival < fireDist[idx]) {
                    vis[idx] = 1;
                    qx[tail] = nx; qy[tail] = ny; qs[tail] = steps + 1;
                    tail++;
                }
            }
        }
    }

    free(vis); free(qx); free(qy); free(qs);
    return 0;
}

int maximumMinutes(int** grid, int gridSize, int* gridColSize){
    m = gridSize;
    n = gridColSize[0];
    gridPtr = grid;

    int total = m * n;
    fireDist = (int *)malloc(total * sizeof(int));
    for (int i = 0; i < total; ++i) fireDist[i] = INF;

    // multi-source BFS for fire
    int *qx = (int *)malloc(total * sizeof(int));
    int *qy = (int *)malloc(total * sizeof(int));
    int head = 0, tail = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 2) {
                int idx = i * n + j;
                fireDist[idx] = 0;
                qx[tail] = i;
                qy[tail] = j;
                tail++;
            }
        }
    }

    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    while (head < tail) {
        int x = qx[head];
        int y = qy[head];
        head++;
        int curIdx = x * n + y;
        int curDist = fireDist[curIdx];

        for (int d = 0; d < 4; ++d) {
            int nx = x + dirs[d][0];
            int ny = y + dirs[d][1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (grid[nx][ny] == 1) continue; // wall blocks fire
            int nIdx = nx * n + ny;
            if (fireDist[nIdx] > curDist + 1) {
                fireDist[nIdx] = curDist + 1;
                qx[tail] = nx;
                qy[tail] = ny;
                tail++;
            }
        }
    }

    free(qx); free(qy);

    // If destination never catches fire, answer is large constant
    if (fireDist[(m-1)*n + (n-1)] == INF) {
        free(fireDist);
        return 1000000000;
    }

    int low = 0, high = m * n; // upper bound sufficient
    while (low < high) {
        int mid = (low + high + 1) / 2;
        if (bfs_can(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }

    free(fireDist);
    return low;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int INF = 1_000_000_007;
    private static readonly int[] dirs = new int[] { 1, 0, -1, 0, 1 };

    public int MaximumMinutes(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;

        // fire distances
        int[,] fireDist = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                fireDist[i, j] = INF;

        var q = new Queue<(int x, int y)>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    fireDist[i, j] = 0;
                    q.Enqueue((i, j));
                }
            }
        }

        while (q.Count > 0) {
            var (x, y) = q.Dequeue();
            int d = fireDist[x, y];
            for (int k = 0; k < 4; k++) {
                int nx = x + dirs[k], ny = y + dirs[k + 1];
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                if (grid[nx][ny] == 1) continue; // wall blocks fire
                if (fireDist[nx, ny] != INF) continue;
                fireDist[nx, ny] = d + 1;
                q.Enqueue((nx, ny));
            }
        }

        // check reachability ignoring fire
        bool[,] reachable = new bool[m, n];
        var qq = new Queue<(int x, int y)>();
        reachable[0, 0] = true;
        qq.Enqueue((0, 0));
        while (qq.Count > 0) {
            var (x, y) = qq.Dequeue();
            for (int k = 0; k < 4; k++) {
                int nx = x + dirs[k], ny = y + dirs[k + 1];
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                if (grid[nx][ny] == 1) continue;
                if (reachable[nx, ny]) continue;
                reachable[nx, ny] = true;
                qq.Enqueue((nx, ny));
            }
        }
        if (!reachable[m - 1, n - 1]) return -1;

        // infinite case
        if (fireDist[m - 1, n - 1] == INF) return 1_000_000_000;

        int lo = 0;
        int hi = fireDist[0, 0] == INF ? 1_000_000_000 : fireDist[0, 0] - 1;
        if (hi > 1_000_000_000) hi = 1_000_000_000;

        int ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (CanWait(mid, grid, fireDist)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }

    private bool CanWait(int wait, int[][] grid, int[,] fireDist) {
        int m = grid.Length, n = grid[0].Length;
        if (wait >= fireDist[0, 0]) return false; // fire reaches start before we leave

        var q = new Queue<(int x, int y, int t)>();
        bool[,] visited = new bool[m, n];
        q.Enqueue((0, 0, wait));
        visited[0, 0] = true;

        while (q.Count > 0) {
            var (x, y, t) = q.Dequeue();
            if (x == m - 1 && y == n - 1) return true; // reached safely

            for (int k = 0; k < 4; k++) {
                int nx = x + dirs[k], ny = y + dirs[k + 1];
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                if (grid[nx][ny] == 1) continue; // wall
                if (visited[nx, ny]) continue;

                int nt = t + 1;
                if (nx == m - 1 && ny == n - 1) {
                    // destination: allow arrival at same time as fire
                    if (nt > fireDist[nx, ny]) continue;
                } else {
                    if (nt >= fireDist[nx, ny]) continue;
                }

                visited[nx, ny] = true;
                q.Enqueue((nx, ny, nt));
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumMinutes = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const INF = 1e9; // sufficiently large
    
    // fire distance matrix
    const fireDist = Array.from({ length: m }, () => Array(n).fill(INF));
    const qx = [], qy = [];
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 2) {
                fireDist[i][j] = 0;
                qx.push(i);
                qy.push(j);
            }
        }
    }
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let head = 0;
    while (head < qx.length) {
        const x = qx[head];
        const y = qy[head];
        ++head;
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (grid[nx][ny] === 1) continue; // wall blocks fire
            if (fireDist[nx][ny] !== INF) continue;
            fireDist[nx][ny] = fireDist[x][y] + 1;
            qx.push(nx);
            qy.push(ny);
        }
    }
    
    // Check for infinite safe path (all cells on some path never catch fire)
    const visInf = Array.from({ length: m }, () => Array(n).fill(false));
    const iqx = [0], iqy = [0];
    visInf[0][0] = true;
    let ihead = 0;
    while (ihead < iqx.length) {
        const x = iqx[ihead];
        const y = iqy[ihead];
        ++ihead;
        if (x === m-1 && y === n-1) return 1000000000;
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (grid[nx][ny] === 1) continue;
            if (fireDist[nx][ny] !== INF) continue; // fire reaches this cell eventually
            if (!visInf[nx][ny]) {
                visInf[nx][ny] = true;
                iqx.push(nx);
                iqy.push(ny);
            }
        }
    }
    
    const canReachWithDelay = (delay) => {
        if (fireDist[0][0] !== INF && delay >= fireDist[0][0]) return false;
        const visited = Array.from({ length: m }, () => Array(n).fill(false));
        const qx2 = [0], qy2 = [0], qt2 = [delay];
        visited[0][0] = true;
        let h = 0;
        while (h < qx2.length) {
            const x = qx2[h];
            const y = qy2[h];
            const t = qt2[h];
            ++h;
            if (x === m-1 && y === n-1) return true; // reached destination safely
            for (const [dx, dy] of dirs) {
                const nx = x + dx, ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] === 1) continue; // wall
                if (visited[nx][ny]) continue;
                const nt = t + 1;
                if (nx === m-1 && ny === n-1) {
                    // destination: can arrive at same time as fire
                    if (fireDist[nx][ny] === INF || nt <= fireDist[nx][ny]) return true;
                    continue;
                }
                if (fireDist[nx][ny] !== INF && nt >= fireDist[nx][ny]) continue; // fire arrives too early or same time
                visited[nx][ny] = true;
                qx2.push(nx);
                qy2.push(ny);
                qt2.push(nt);
            }
        }
        return false;
    };
    
    if (!canReachWithDelay(0)) return -1;
    
    let low = 0, high = m * n; // upper bound sufficient
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (canReachWithDelay(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function maximumMinutes(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const INF = 1e9; // sufficiently large
    
    const fireDist: number[][] = Array.from({ length: m }, () => Array(n).fill(INF));
    const qx: number[] = [];
    const qy: number[] = [];
    const qd: number[] = [];
    let head = 0;
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 2) {
                fireDist[i][j] = 0;
                qx.push(i);
                qy.push(j);
                qd.push(0);
            }
        }
    }
    
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    while (head < qx.length) {
        const x = qx[head];
        const y = qy[head];
        const d = qd[head];
        head++;
        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (grid[nx][ny] === 1) continue; // wall
            if (fireDist[nx][ny] !== INF) continue;
            fireDist[nx][ny] = d + 1;
            qx.push(nx);
            qy.push(ny);
            qd.push(d + 1);
        }
    }
    
    // Check for infinite wait possibility
    if (fireDist[m-1][n-1] === INF) {
        const vis: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
        const qqx: number[] = [];
        const qqy: number[] = [];
        let h2 = 0;
        if (fireDist[0][0] === INF) {
            vis[0][0] = true;
            qqx.push(0);
            qqy.push(0);
        }
        while (h2 < qqx.length) {
            const x = qqx[h2];
            const y = qqy[h2];
            h2++;
            if (x === m-1 && y === n-1) return 1000000000;
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] === 1) continue;
                if (vis[nx][ny]) continue;
                if (fireDist[nx][ny] !== INF) continue;
                vis[nx][ny] = true;
                qqx.push(nx);
                qqy.push(ny);
            }
        }
    }
    
    const canReach = (wait: number): boolean => {
        if (wait >= fireDist[0][0]) return false; // start burns before we move
        const vis: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
        const qx2: number[] = [];
        const qy2: number[] = [];
        const qt2: number[] = [];
        let h3 = 0;
        qx2.push(0);
        qy2.push(0);
        qt2.push(wait);
        vis[0][0] = true;
        while (h3 < qx2.length) {
            const x = qx2[h3];
            const y = qy2[h3];
            const t = qt2[h3];
            h3++;
            if (x === m-1 && y === n-1) {
                // destination can be reached even if fire arrives at same time
                return t <= fireDist[x][y];
            }
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] === 1) continue;
                if (vis[nx][ny]) continue;
                const nt = t + 1;
                const f = fireDist[nx][ny];
                if (nx === m-1 && ny === n-1) {
                    if (nt > f) continue; // need <= for destination
                } else {
                    if (nt >= f) continue; // need strictly less
                }
                vis[nx][ny] = true;
                qx2.push(nx);
                qy2.push(ny);
                qt2.push(nt);
            }
        }
        return false;
    };
    
    let low = 0, high = m * n; // upper bound sufficient
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (canReach(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumMinutes($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = 1000000007;

        // Compute fire arrival times using multi-source BFS
        $dist = array_fill(0, $m, array_fill(0, $n, $INF));
        $queue = new SplQueue();

        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] == 2) {
                    $dist[$i][$j] = 0;
                    $queue->enqueue([$i, $j]);
                }
            }
        }

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        while (!$queue->isEmpty()) {
            [$x, $y] = $queue->dequeue();
            $cur = $dist[$x][$y];
            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;
                if ($grid[$nx][$ny] == 1) continue; // wall blocks fire
                if ($dist[$nx][$ny] > $cur + 1) {
                    $dist[$nx][$ny] = $cur + 1;
                    $queue->enqueue([$nx, $ny]);
                }
            }
        }

        // If fire never reaches the safehouse, answer is 1e9
        if ($dist[$m-1][$n-1] == $INF) {
            return 1000000000;
        }

        // Helper to check feasibility with given waiting time
        $canReach = function($wait) use (&$grid, &$dist, $m, $n, $dirs, $INF) {
            if ($dist[0][0] != $INF && $wait >= $dist[0][0]) return false;

            $visited = array_fill(0, $m, array_fill(0, $n, false));
            $q = new SplQueue();
            $q->enqueue([0, 0, $wait]);
            $visited[0][0] = true;

            while (!$q->isEmpty()) {
                [$x, $y, $t] = $q->dequeue();

                if ($x == $m-1 && $y == $n-1) return true; // reached safely

                foreach ($dirs as $d) {
                    $nx = $x + $d[0];
                    $ny = $y + $d[1];
                    if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;
                    if ($grid[$nx][$ny] == 1) continue; // wall

                    $nt = $t + 1;

                    if ($nx == $m-1 && $ny == $n-1) {
                        // Destination: allow arrival at same time as fire
                        if ($dist[$nx][$ny] != $INF && $nt > $dist[$nx][$ny]) continue;
                    } else {
                        if ($dist[$nx][$ny] != $INF && $nt >= $dist[$nx][$ny]) continue;
                    }

                    if (!$visited[$nx][$ny]) {
                        $visited[$nx][$ny] = true;
                        $q->enqueue([$nx, $ny, $nt]);
                    }
                }
            }
            return false;
        };

        // Binary search maximum waiting time
        $low = 0;
        $high = $m * $n; // upper bound sufficient

        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($canReach($mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }

        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func maximumMinutes(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        let INF = 1_000_000_000
        var fireDist = Array(repeating: Array(repeating: INF, count: n), count: m)
        var qx = [Int]()
        var qy = [Int]()
        // multi-source BFS for fire
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 2 {
                    fireDist[i][j] = 0
                    qx.append(i)
                    qy.append(j)
                }
            }
        }
        var head = 0
        let dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while head < qx.count {
            let x = qx[head]
            let y = qy[head]
            head += 1
            for (dx, dy) in dirs {
                let nx = x + dx
                let ny = y + dy
                if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] != 1 && fireDist[nx][ny] == INF {
                    fireDist[nx][ny] = fireDist[x][y] + 1
                    qx.append(nx)
                    qy.append(ny)
                }
            }
        }
        // If safehouse never catches fire, answer is 1e9 if reachable at all.
        if fireDist[m-1][n-1] == INF {
            var vis = Array(repeating: Array(repeating: false, count: n), count: m)
            var sx = [Int](), sy = [Int]()
            var h = 0
            sx.append(0); sy.append(0)
            vis[0][0] = true
            while h < sx.count {
                let x = sx[h], y = sy[h]; h += 1
                if x == m-1 && y == n-1 { return 1_000_000_000 }
                for (dx, dy) in dirs {
                    let nx = x + dx, ny = y + dy
                    if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] != 1 && !vis[nx][ny] {
                        vis[nx][ny] = true
                        sx.append(nx); sy.append(ny)
                    }
                }
            }
            return -1
        }
        // Helper to test feasibility with given delay
        func can(_ delay: Int) -> Bool {
            if delay >= fireDist[0][0] { return false }
            var visited = Array(repeating: Array(repeating: false, count: n), count: m)
            var qx2 = [Int](), qy2 = [Int](), qt2 = [Int]()
            var h = 0
            visited[0][0] = true
            qx2.append(0); qy2.append(0); qt2.append(delay)
            while h < qx2.count {
                let x = qx2[h], y = qy2[h], time = qt2[h]
                h += 1
                if x == m-1 && y == n-1 { return true }
                for (dx, dy) in dirs {
                    let nx = x + dx, ny = y + dy
                    if nx < 0 || nx >= m || ny < 0 || ny >= n { continue }
                    if grid[nx][ny] == 1 || visited[nx][ny] { continue }
                    let nt = time + 1
                    if nx == m-1 && ny == n-1 {
                        if nt <= fireDist[nx][ny] { return true }
                    } else {
                        if nt < fireDist[nx][ny] {
                            visited[nx][ny] = true
                            qx2.append(nx); qy2.append(ny); qt2.append(nt)
                        }
                    }
                }
            }
            return false
        }
        // If cannot even start, return -1
        if !can(0) { return -1 }
        var low = 0
        var high = m * n + 5   // sufficient upper bound
        while low < high {
            let mid = (low + high + 1) >> 1
            if can(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun maximumMinutes(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val INF = Int.MAX_VALUE / 4

        // Fire BFS
        val fireDist = Array(m) { IntArray(n) { INF } }
        val qFire: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 2) {
                    fireDist[i][j] = 0
                    qFire.add(Pair(i, j))
                }
            }
        }
        val dirs = intArrayOf(1, 0, -1, 0, 1)
        while (!qFire.isEmpty()) {
            val (x, y) = qFire.poll()
            val d = fireDist[x][y]
            for (k in 0 until 4) {
                val nx = x + dirs[k]
                val ny = y + dirs[k + 1]
                if (nx in 0 until m && ny in 0 until n && grid[nx][ny] != 1 && fireDist[nx][ny] == INF) {
                    fireDist[nx][ny] = d + 1
                    qFire.add(Pair(nx, ny))
                }
            }
        }

        // Check simple reachability ignoring fire
        fun reachableWithoutFire(): Boolean {
            val visited = Array(m) { BooleanArray(n) }
            val dq: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
            dq.add(Pair(0, 0))
            visited[0][0] = true
            while (!dq.isEmpty()) {
                val (x, y) = dq.poll()
                if (x == m - 1 && y == n - 1) return true
                for (k in 0 until 4) {
                    val nx = x + dirs[k]
                    val ny = y + dirs[k + 1]
                    if (nx in 0 until m && ny in 0 until n && grid[nx][ny] != 1 && !visited[nx][ny]) {
                        visited[nx][ny] = true
                        dq.add(Pair(nx, ny))
                    }
                }
            }
            return false
        }

        if (!reachableWithoutFire()) return -1

        // If fire never reaches start, answer is 1e9
        if (fireDist[0][0] == INF) return 1_000_000_000

        fun canWait(wait: Int): Boolean {
            if (fireDist[0][0] <= wait) return false
            val visited = Array(m) { BooleanArray(n) }
            data class Node(val x: Int, val y: Int, val d: Int)
            val dq: ArrayDeque<Node> = ArrayDeque()
            dq.add(Node(0, 0, 0))
            visited[0][0] = true
            while (!dq.isEmpty()) {
                val cur = dq.poll()
                val curTime = wait + cur.d
                if (cur.x == m - 1 && cur.y == n - 1) {
                    // destination can be reached when time <= fireDist
                    return curTime <= fireDist[cur.x][cur.y]
                }
                for (k in 0 until 4) {
                    val nx = cur.x + dirs[k]
                    val ny = cur.y + dirs[k + 1]
                    if (nx !in 0 until m || ny !in 0 until n) continue
                    if (grid[nx][ny] == 1) continue
                    if (visited[nx][ny]) continue
                    val nextTime = curTime + 1
                    if (nx == m - 1 && ny == n - 1) {
                        if (nextTime <= fireDist[nx][ny]) {
                            visited[nx][ny] = true
                            dq.add(Node(nx, ny, cur.d + 1))
                        }
                    } else {
                        if (nextTime < fireDist[nx][ny]) {
                            visited[nx][ny] = true
                            dq.add(Node(nx, ny, cur.d + 1))
                        }
                    }
                }
            }
            return false
        }

        var lo = 0
        var hi = fireDist[0][0] - 1
        var ans = -1
        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            if (canWait(mid)) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  static const int _INF = 1 << 30;
  static const int _DIRS = 4;
  final List<int> _dx = [0, 1, 0, -1];
  final List<int> _dy = [1, 0, -1, 0];

  int maximumMinutes(List<List<int>> grid) {
    final int m = grid.length;
    final int n = grid[0].length;

    // Fire distance BFS
    List<List<int>> fireDist =
        List.generate(m, (_) => List.filled(n, _INF), growable: false);
    List<int> qx = [];
    List<int> qy = [];
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 2) {
          fireDist[i][j] = 0;
          qx.add(i);
          qy.add(j);
        }
      }
    }
    int head = 0;
    while (head < qx.length) {
      int x = qx[head];
      int y = qy[head];
      ++head;
      int d = fireDist[x][y] + 1;
      for (int dir = 0; dir < _DIRS; ++dir) {
        int nx = x + _dx[dir];
        int ny = y + _dy[dir];
        if (nx < 0 ||
            nx >= m ||
            ny < 0 ||
            ny >= n ||
            grid[nx][ny] == 1 ||
            fireDist[nx][ny] <= d) continue;
        fireDist[nx][ny] = d;
        qx.add(nx);
        qy.add(ny);
      }
    }

    // Check for infinite waiting possibility
    if (fireDist[m - 1][n - 1] == _INF) {
      List<List<bool>> vis =
          List.generate(m, (_) => List.filled(n, false), growable: false);
      qx = [0];
      qy = [0];
      head = 0;
      vis[0][0] = true;
      while (head < qx.length) {
        int x = qx[head];
        int y = qy[head];
        ++head;
        if (x == m - 1 && y == n - 1) return 1000000000;
        for (int dir = 0; dir < _DIRS; ++dir) {
          int nx = x + _dx[dir];
          int ny = y + _dy[dir];
          if (nx < 0 ||
              nx >= m ||
              ny < 0 ||
              ny >= n ||
              grid[nx][ny] == 1 ||
              fireDist[nx][ny] != _INF ||
              vis[nx][ny]) continue;
          vis[nx][ny] = true;
          qx.add(nx);
          qy.add(ny);
        }
      }
    }

    // Binary search on waiting time
    int lo = 0, hi = 1000000000;
    while (lo < hi) {
      int mid = ((lo + hi + 1) >> 1);
      if (_canReach(grid, fireDist, mid)) {
        lo = mid;
      } else {
        hi = mid - 1;
      }
    }
    return lo;
  }

  bool _canReach(
      List<List<int>> grid, List<List<int>> fireDist, int wait) {
    final int m = grid.length;
    final int n = grid[0].length;

    if (fireDist[0][0] <= wait) return false;

    List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false), growable: false);
    List<int> qx = [0];
    List<int> qy = [0];
    List<int> qt = [wait];
    int head = 0;
    visited[0][0] = true;

    while (head < qx.length) {
      int x = qx[head];
      int y = qy[head];
      int t = qt[head];
      ++head;

      if (x == m - 1 && y == n - 1) return true;

      for (int dir = 0; dir < _DIRS; ++dir) {
        int nx = x + _dx[dir];
        int ny = y + _dy[dir];
        if (nx < 0 ||
            nx >= m ||
            ny < 0 ||
            ny >= n ||
            grid[nx][ny] == 1 ||
            visited[nx][ny]) continue;
        int nt = t + 1;

        if (nx == m - 1 && ny == n - 1) {
          // Destination can be reached when fire arrives at same time
          if (fireDist[nx][ny] >= nt) {
            visited[nx][ny] = true;
            qx.add(nx);
            qy.add(ny);
            qt.add(nt);
          }
        } else {
          if (fireDist[nx][ny] > nt) {
            visited[nx][ny] = true;
            qx.add(nx);
            qy.add(ny);
            qt.add(nt);
          }
        }
      }
    }
    return false;
  }
}
```

## Golang

```go
func maximumMinutes(grid [][]int) int {
	const INF = 1 << 30
	m, n := len(grid), len(grid[0])
	fireDist := make([][]int, m)
	for i := range fireDist {
		fireDist[i] = make([]int, n)
		for j := range fireDist[i] {
			fireDist[i][j] = INF
		}
	}
	type pair struct{ x, y int }
	q := make([]pair, 0)
	// multi-source BFS for fire
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 2 {
				fireDist[i][j] = 0
				q = append(q, pair{i, j})
			}
		}
	}
	dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	head := 0
	for head < len(q) {
		cur := q[head]
		head++
		cd := fireDist[cur.x][cur.y]
		for _, d := range dir {
			nx, ny := cur.x+d[0], cur.y+d[1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			if grid[nx][ny] == 1 { // wall blocks fire spread
				continue
			}
			if fireDist[nx][ny] > cd+1 {
				fireDist[nx][ny] = cd + 1
				q = append(q, pair{nx, ny})
			}
		}
	}
	destX, destY := m-1, n-1
	if fireDist[destX][destY] == INF {
		return 1000000000
	}

	// helper to test if waiting t minutes works
	canReach := func(t int) bool {
		if fireDist[0][0] != INF && t >= fireDist[0][0] {
			return false
		}
		type node struct{ x, y, time int }
		queue := []node{{0, 0, t}}
		visited := make([][]bool, m)
		for i := range visited {
			visited[i] = make([]bool, n)
		}
		visited[0][0] = true
		head := 0
		for head < len(queue) {
			cur := queue[head]
			head++
			if cur.x == destX && cur.y == destY {
				return true
			}
			for _, d := range dir {
				nx, ny := cur.x+d[0], cur.y+d[1]
				if nx < 0 || nx >= m || ny < 0 || ny >= n {
					continue
				}
				if grid[nx][ny] == 1 { // wall
					continue
				}
				if visited[nx][ny] {
					continue
				}
				nt := cur.time + 1
				// fire condition
				if fireDist[nx][ny] != INF && nt >= fireDist[nx][ny] {
					// destination allows equality
					if !(nx == destX && ny == destY && nt <= fireDist[nx][ny]) {
						continue
					}
				}
				visited[nx][ny] = true
				queue = append(queue, node{nx, ny, nt})
			}
		}
		return false
	}

	low, high := 0, m*n+5 // sufficient upper bound
	ans := -1
	for low <= high {
		mid := (low + high) / 2
		if canReach(mid) {
			ans = mid
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return ans
}
```

## Ruby

```ruby
def maximum_minutes(grid)
  m = grid.size
  n = grid[0].size
  INF = 1 << 60

  # compute earliest fire arrival time for each cell
  fire = Array.new(m) { Array.new(n, INF) }
  q = []
  head = 0
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 2
        fire[i][j] = 0
        q << [i, j]
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  while head < q.size
    x, y = q[head]; head += 1
    d = fire[x][y] + 1
    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      next if nx < 0 || nx >= m || ny < 0 || ny >= n
      next if grid[nx][ny] == 1
      if fire[nx][ny] > d
        fire[nx][ny] = d
        q << [nx, ny]
      end
    end
  end

  # fire never reaches destination -> infinite wait possible
  return 1_000_000_000 if fire[m - 1][n - 1] == INF

  can_reach = lambda do |wait|
    return false unless wait < fire[0][0]
    visited = Array.new(m) { Array.new(n, false) }
    q2 = []
    h2 = 0
    q2 << [0, 0, wait]
    visited[0][0] = true
    while h2 < q2.size
      x, y, t = q2[h2]; h2 += 1
      return true if x == m - 1 && y == n - 1
      dirs.each do |dx, dy|
        nx = x + dx
        ny = y + dy
        next if nx < 0 || nx >= m || ny < 0 || ny >= n
        next if grid[nx][ny] == 1
        nt = t + 1
        if nx == m - 1 && ny == n - 1
          next unless nt <= fire[nx][ny]
        else
          next unless nt < fire[nx][ny]
        end
        next if visited[nx][ny]
        visited[nx][ny] = true
        q2 << [nx, ny, nt]
      end
    end
    false
  end

  return -1 unless can_reach.call(0)

  low = 0
  high = 1_000_000_000
  while low < high
    mid = (low + high + 1) / 2
    if can_reach.call(mid)
      low = mid
    else
      high = mid - 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable
  def maximumMinutes(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val INF = Int.MaxValue / 2
    val fireDist = Array.fill(m)(Array.fill(n)(INF))
    val qFire = new mutable.Queue[(Int, Int)]()
    for (i <- 0 until m; j <- 0 until n) {
      if (grid(i)(j) == 2) {
        fireDist(i)(j) = 0
        qFire.enqueue((i, j))
      }
    }
    val dirs = Array((1,0),(-1,0),(0,1),(0,-1))
    while (qFire.nonEmpty) {
      val (x, y) = qFire.dequeue()
      val d = fireDist(x)(y)
      for ((dx, dy) <- dirs) {
        val nx = x + dx
        val ny = y + dy
        if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid(nx)(ny) != 1 && fireDist(nx)(ny) == INF) {
          fireDist(nx)(ny) = d + 1
          qFire.enqueue((nx, ny))
        }
      }
    }

    val destX = m - 1
    val destY = n - 1

    // If fire never reaches destination, answer is 1e9 provided a path exists.
    if (fireDist(destX)(destY) == INF) {
      // check reachability without fire constraints
      if (canReach(0, grid, fireDist)) 1_000_000_000 else -1
    } else {
      var lo = 0
      var hi = m * n   // sufficient upper bound
      var ans = -1
      while (lo <= hi) {
        val mid = lo + (hi - lo) / 2
        if (canReach(mid, grid, fireDist)) {
          ans = mid
          lo = mid + 1
        } else {
          hi = mid - 1
        }
      }
      ans
    }
  }

  private def canReach(wait: Int,
                       grid: Array[Array[Int]],
                       fireDist: Array[Array[Int]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    val destX = m - 1
    val destY = n - 1
    if (wait >= fireDist(0)(0)) return false

    val visited = Array.fill(m)(Array.fill(n)(false))
    val q = new mutable.Queue[(Int, Int, Int)]() // x, y, time
    q.enqueue((0, 0, wait))
    visited(0)(0) = true
    val dirs = Array((1,0),(-1,0),(0,1),(0,-1))

    while (q.nonEmpty) {
      val (x, y, t) = q.dequeue()
      if (x == destX && y == destY) return true
      for ((dx, dy) <- dirs) {
        val nx = x + dx
        val ny = y + dy
        if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid(nx)(ny) != 1 && !visited(nx)(ny)) {
          val nt = t + 1
          if (nx == destX && ny == destY) {
            if (nt <= fireDist(nx)(ny)) {
              visited(nx)(ny) = true
              q.enqueue((nx, ny, nt))
            }
          } else {
            if (nt < fireDist(nx)(ny)) {
              visited(nx)(ny) = true
              q.enqueue((nx, ny, nt))
            }
          }
        }
      }
    }
    false
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn maximum_minutes(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const INF: i32 = 1_000_000_007;
        // fire arrival times
        let mut fire_time = vec![vec![INF; n]; m];
        let mut q: VecDeque<(usize, usize)> = VecDeque::new();
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 2 {
                    fire_time[i][j] = 0;
                    q.push_back((i, j));
                }
            }
        }
        let dirs = [(1_i32, 0_i32), (-1, 0), (0, 1), (0, -1)];
        while let Some((x, y)) = q.pop_front() {
            let cur = fire_time[x][y];
            for &(dx, dy) in &dirs {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx < 0 || ny < 0 || nx >= m as i32 || ny >= n as i32 {
                    continue;
                }
                let ux = nx as usize;
                let uy = ny as usize;
                if grid[ux][uy] == 1 { // wall
                    continue;
                }
                if fire_time[ux][uy] == INF {
                    fire_time[ux][uy] = cur + 1;
                    q.push_back((ux, uy));
                }
            }
        }

        // check reachability ignoring fire
        let mut reachable = vec![vec![false; n]; m];
        let mut qq: VecDeque<(usize, usize)> = VecDeque::new();
        reachable[0][0] = true;
        qq.push_back((0, 0));
        while let Some((x, y)) = qq.pop_front() {
            for &(dx, dy) in &dirs {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx < 0 || ny < 0 || nx >= m as i32 || ny >= n as i32 {
                    continue;
                }
                let ux = nx as usize;
                let uy = ny as usize;
                if grid[ux][uy] == 1 { continue; }
                if !reachable[ux][uy] {
                    reachable[ux][uy] = true;
                    qq.push_back((ux, uy));
                }
            }
        }
        if !reachable[m-1][n-1] {
            return -1;
        }

        // infinite case
        if fire_time[m-1][n-1] == INF {
            return 1_000_000_000;
        }

        // feasibility check for a given delay t
        let can = |t: i32,
                   fire_time: &Vec<Vec<i32>>,
                   grid: &Vec<Vec<i32>>| -> bool {
            if t >= fire_time[0][0] { return false; }
            let mut visited = vec![vec![false; n]; m];
            let mut dq: VecDeque<(usize, usize, i32)> = VecDeque::new();
            visited[0][0] = true;
            dq.push_back((0, 0, t));
            while let Some((x, y, cur)) = dq.pop_front() {
                if x == m-1 && y == n-1 {
                    return true;
                }
                for &(dx, dy) in &dirs {
                    let nx = x as i32 + dx;
                    let ny = y as i32 + dy;
                    if nx < 0 || ny < 0 || nx >= m as i32 || ny >= n as i32 { continue; }
                    let ux = nx as usize;
                    let uy = ny as usize;
                    if grid[ux][uy] == 1 { continue; }
                    if visited[ux][uy] { continue; }
                    let nt = cur + 1;
                    if ux == m-1 && uy == n-1 {
                        if nt <= fire_time[ux][uy] {
                            return true;
                        } else {
                            continue;
                        }
                    } else {
                        if nt < fire_time[ux][uy] {
                            visited[ux][uy] = true;
                            dq.push_back((ux, uy, nt));
                        }
                    }
                }
            }
            false
        };

        // binary search maximum t
        let mut lo: i32 = 0;
        let mut hi: i32 = m as i32 * n as i32; // upper bound sufficient
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if can(mid, &fire_time, &grid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
```

## Racket

```racket
(define (maximum-minutes grid)
  (let* ((m (length grid))
         (n (length (car grid)))
         (gridv (list->vector (map list->vector grid)))
         (INF 1000000000)
         ;; fire distance matrix
         (fireDist (make-vector m)))
    (for ([i (in-range m)])
      (vector-set! fireDist i (make-vector n INF)))
    ;; BFS queue for fire spread
    (define qx (make-vector (* m n) 0))
    (define qy (make-vector (* m n) 0))
    (define front 0)
    (define back 0)
    (for ([i (in-range m)])
      (let ((row (vector-ref gridv i)))
        (for ([j (in-range n)])
          (when (= (vector-ref row j) 2)
            (vector-set! (vector-ref fireDist i) j 0)
            (vector-set! qx back i)
            (vector-set! qy back j)
            (set! back (+ back 1))))))
    (define dirs '#((0 1) (1 0) (0 -1) (-1 0)))
    (let bfs-fire ()
      (when (< front back)
        (let* ((x (vector-ref qx front))
               (y (vector-ref qy front))
               (d (vector-ref (vector-ref fireDist x) y)))
          (set! front (+ front 1))
          (for ([dir dirs])
            (define nx (+ x (vector-ref dir 0)))
            (define ny (+ y (vector-ref dir 1)))
            (when (and (>= nx 0) (< nx m)
                       (>= ny 0) (< ny n)
                       (not (= (vector-ref (vector-ref gridv nx) ny) 1))
                       (> (vector-ref (vector-ref fireDist nx) ny) (+ d 1)))
              (vector-set! (vector-ref fireDist nx) ny (+ d 1))
              (vector-set! qx back nx)
              (vector-set! qy back ny)
              (set! back (+ back 1)))))
        (bfs-fire)))
    ;; helper: reachable ignoring fire
    (define (reachable-no-fire?)
      (let ((visited (make-vector m)))
        (for ([i (in-range m)]) (vector-set! visited i (make-vector n #f)))
        (define qx2 (make-vector (* m n) 0))
        (define qy2 (make-vector (* m n) 0))
        (define f 0)
        (define b 0)
        (vector-set! (vector-ref visited 0) 0 #t)
        (vector-set! qx2 b 0)
        (vector-set! qy2 b 0)
        (set! b (+ b 1))
        (let bfs ()
          (when (< f b)
            (define x (vector-ref qx2 f))
            (define y (vector-ref qy2 f))
            (set! f (+ f 1))
            (when (and (= x (- m 1)) (= y (- n 1))) (return #t))
            (for ([dir dirs])
              (define nx (+ x (vector-ref dir 0)))
              (define ny (+ y (vector-ref dir 1)))
              (when (and (>= nx 0) (< nx m)
                         (>= ny 0) (< ny n)
                         (not (= (vector-ref (vector-ref gridv nx) ny) 1))
                         (not (vector-ref (vector-ref visited nx) ny)))
                (vector-set! (vector-ref visited nx) ny #t)
                (vector-set! qx2 b nx)
                (vector-set! qy2 b ny)
                (set! b (+ b 1))))
            (bfs)))))
        #f))
    (unless (reachable-no-fire?) (return -1))
    ;; infinite case
    (when (= (vector-ref (vector-ref fireDist (- m 1)) (- n 1)) INF)
      (return 1000000000))
    ;; can-reach with waiting w
    (define (can-reach? w)
      (if (> (vector-ref (vector-ref fireDist 0) 0) w)
          (call/cc
            (lambda (ret)
              (let ((visited (make-vector m)))
                (for ([i (in-range m)]) (vector-set! visited i (make-vector n #f)))
                (define qx3 (make-vector (* m n) 0))
                (define qy3 (make-vector (* m n) 0))
                (define qt (make-vector (* m n) 0))
                (define f 0)
                (define b 0)
                (vector-set! (vector-ref visited 0) 0 #t)
                (vector-set! qx3 b 0)
                (vector-set! qy3 b 0)
                (vector-set! qt b w)
                (set! b (+ b 1))
                (let bfs ()
                  (when (< f b)
                    (define x (vector-ref qx3 f))
                    (define y (vector-ref qy3 f))
                    (define t (vector-ref qt f))
                    (set! f (+ f 1))
                    (when (and (= x (- m 1)) (= y (- n 1)))
                      (ret #t))
                    (for ([dir dirs])
                      (define nx (+ x (vector-ref dir 0)))
                      (define ny (+ y (vector-ref dir 1)))
                      (when (and (>= nx 0) (< nx m)
                                 (>= ny 0) (< ny n)
                                 (not (= (vector-ref (vector-ref gridv nx) ny) 1))
                                 (not (vector-ref (vector-ref visited nx) ny))
                                 (> (vector-ref (vector-ref fireDist nx) ny) (+ t 1)))
                        (vector-set! (vector-ref visited nx) ny #t)
                        (vector-set! qx3 b nx)
                        (vector-set! qy3 b ny)
                        (vector-set! qt b (+ t 1))
                        (set! b (+ b 1))))
                    (bfs)))))
                #f))
          #f))
    ;; binary search
    (let* ((startFire (vector-ref (vector-ref fireDist 0) 0))
           (high (if (= startFire INF) (* m n) (- startFire 1)))
           (low 0))
      (let loop ()
        (if (> low high)
            low
            (let ((mid (quotient (+ low high 1) 2))) ; ceil division
              (if (can-reach? mid)
                  (begin (set! low mid) (loop))
                  (begin (set! high (- mid 1)) (loop)))))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_minutes/1]).

-define(INF, 1000000000).

%% Public API
-spec maximum_minutes(Grid :: [[integer()]]) -> integer().
maximum_minutes(Grid) ->
    {M, N} = dimensions(Grid),
    FireDist = fire_bfs(Grid, M, N),
    GoalKey = {M - 1, N - 1},
    case maps:get(GoalKey, FireDist, ?INF) of
        Dist when Dist >= ?INF -> ?INF;
        _ ->
            case can(0, Grid, FireDist, M, N) of
                false -> -1;
                true -> binary_search(0, 1000000000, Grid, FireDist, M, N)
            end
    end.

%% Helpers

dimensions(Grid) ->
    M = length(Grid),
    [FirstRow | _] = Grid,
    N = length(FirstRow),
    {M, N}.

cell(Grid, X, Y) ->
    Row = lists:nth(X + 1, Grid),
    lists:nth(Y + 1, Row).

neighbors(X, Y, M, N) ->
    [{X - 1, Y}, {X + 1, Y}, {X, Y - 1}, {X, Y + 1}]
    |> lists:filter(
           fun({NX, NY}) ->
               NX >= 0 andalso NX < M andalso NY >= 0 andalso NY < N
           end).

%% Fire BFS (multi‑source)
fire_bfs(Grid, M, N) ->
    FirePos = [{X, Y} ||
                 X <- lists:seq(0, M - 1),
                 Y <- lists:seq(0, N - 1),
                 cell(Grid, X, Y) == 2],
    DistMap0 = maps:from_list([{Pos, 0} || Pos <- FirePos]),
    Queue0 = lists:foldl(fun(Pos, Q) -> :queue.in(Pos, Q) end,
                         :queue.new(),
                         FirePos),
    bfs_fire(Queue0, DistMap0, Grid, M, N).

bfs_fire(Queue, DistMap, Grid, M, N) ->
    case :queue.out(Queue) of
        {{value, {X, Y}}, Q1} ->
            D = maps:get({X, Y}, DistMap),
            Neighs = neighbors(X, Y, M, N),
            {Q2, DistMap2} =
                lists:foldl(
                  fun({NX, NY}, {QAcc, DM}) ->
                          case cell(Grid, NX, NY) of
                              1 -> {QAcc, DM};
                              _ ->
                                  Prev = maps:get({NX, NY}, DM, ?INF),
                                  if D + 1 < Prev ->
                                          QNew = :queue.in({NX, NY}, QAcc),
                                          {QNew, maps:put({NX, NY}, D + 1, DM)};
                                     true -> {QAcc, DM}
                                  end
                          end
                  end,
                  {Q1, DistMap},
                  Neighs),
            bfs_fire(Q2, DistMap2, Grid, M, N);
        {empty, _} ->
            DistMap
    end.

%% Check feasibility with a given waiting time
can(Wait, Grid, FireDist, M, N) ->
    StartKey = {0, 0},
    case maps:get(StartKey, FireDist, ?INF) of
        D when D =< Wait -> false;
        _ ->
            Visited = maps:put(StartKey, true, #{}),
            Q0 = :queue.in({0, 0, Wait}, :queue.new()),
            can_bfs(Q0, Visited, Grid, FireDist, M, N)
    end.

can_bfs(Queue, Visited, Grid, FireDist, M, N) ->
    case :queue.out(Queue) of
        {{value, {X, Y, T}}, Q1} ->
            if X =:= M - 1 andalso Y =:= N - 1 ->
                    true;
               true ->
                    Neighs = neighbors(X, Y, M, N),
                    {Q2, Vis2} =
                        lists:foldl(
                          fun({NX, NY}, {QAcc, VAcc}) ->
                                  case cell(Grid, NX, NY) of
                                      1 -> {QAcc, VAcc};
                                      _ ->
                                          Nt = T + 1,
                                          FireTime = maps:get({NX, NY}, FireDist, ?INF),
                                          if (NX =:= M - 1 andalso NY =:= N - 1) ->
                                                  if FireTime > Nt ->
                                                          QNew = :queue.in({NX, NY, Nt}, QAcc),
                                                          VNew = maps:put({NX, NY}, true, VAcc),
                                                          {QNew, VNew};
                                                     true -> {QAcc, VAcc}
                                                  end;
                                             true ->
                                                  case (FireTime > Nt) andalso not maps:is_key({NX, NY}, VAcc) of
                                                      true ->
                                                          QNew = :queue.in({NX, NY, Nt}, QAcc),
                                                          VNew = maps:put({NX, NY}, true, VAcc),
                                                          {QNew, VNew};
                                                      false -> {QAcc, VAcc}
                                                  end
                                          end
                                  end
                          end,
                          {Q1, Visited},
                          Neighs),
                    can_bfs(Q2, Vis2, Grid, FireDist, M, N)
            end;
        {empty, _} ->
            false
    end.

%% Binary search for maximum waiting time
binary_search(Low, High, Grid, FireDist, M, N) ->
    if Low < High ->
            Mid = (Low + High + 1) div 2,
            case can(Mid, Grid, FireDist, M, N) of
                true -> binary_search(Mid, High, Grid, FireDist, M, N);
                false -> binary_search(Low, Mid - 1, Grid, FireDist, M, N)
            end;
       true ->
            Low
    end.
```

## Elixir

```elixir
defmodule Solution do
  @inf 1_000_000_000

  @spec maximum_minutes(grid :: [[integer]]) :: integer
  def maximum_minutes(grid) do
    m = length(grid)
    n = length(List.first(grid))

    {queue0, fire_dist0} =
      Enum.reduce(0..m - 1, {:queue.new(), %{}}, fn i, {q, fd} ->
        row = Enum.at(grid, i)

        Enum.reduce(0..n - 1, {q, fd}, fn j, {qq, fdd} ->
          if Enum.at(row, j) == 2 do
            {:queue.in({i, j}, qq), Map.put(fdd, {i, j}, 0)}
          else
            {qq, fdd}
          end
        end)
      end)

    fire_dist = bfs_fire(grid, m, n, queue0, fire_dist0)

    dest_time = Map.get(fire_dist, {m - 1, n - 1}, @inf)

    if dest_time == @inf do
      1_000_000_000
    else
      {ans, _} = binary_search(0, m * n + 5, -1, grid, fire_dist, m, n)
      ans
    end
  end

  defp bfs_fire(grid, m, n, queue, fire_dist) do
    case :queue.out(queue) do
      {{:value, {i, j}}, q} ->
        cur = Map.get(fire_dist, {i, j})

        dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

        {new_q, new_fd} =
          Enum.reduce(dirs, {q, fire_dist}, fn {dx, dy}, {qq, fd} ->
            ni = i + dx
            nj = j + dy

            if ni >= 0 and ni < m and nj >= 0 and nj < n do
              cell = cell(grid, ni, nj)

              if cell != 1 and not Map.has_key?(fd, {ni, nj}) do
                {:queue.in({ni, nj}, qq), Map.put(fd, {ni, nj}, cur + 1)}
              else
                {qq, fd}
              end
            else
              {qq, fd}
            end
          end)

        bfs_fire(grid, m, n, new_q, new_fd)

      {:empty, _} ->
        fire_dist
    end
  end

  defp binary_search(low, high, best, grid, fire_dist, m, n) do
    if low > high do
      {best, nil}
    else
      mid = div(low + high, 2)

      if can_reach?(mid, grid, fire_dist, m, n) do
        binary_search(mid + 1, high, mid, grid, fire_dist, m, n)
      else
        binary_search(low, mid - 1, best, grid, fire_dist, m, n)
      end
    end
  end

  defp can_reach?(t, grid, fire_dist, m, n) do
    start_fire = Map.get(fire_dist, {0, 0}, @inf)

    if t >= start_fire do
      false
    else
      bfs_person(:queue.in({0, 0, t}, :queue.new()), MapSet.new([{0, 0}]), grid, fire_dist, m, n)
    end
  end

  defp bfs_person(queue, visited, grid, fire_dist, m, n) do
    case :queue.out(queue) do
      {{:value, {i, j, time}}, q} ->
        if i == m - 1 and j == n - 1 do
          true
        else
          dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

          {new_q, new_vis} =
            Enum.reduce(dirs, {q, visited}, fn {dx, dy}, {qq, vv} ->
              ni = i + dx
              nj = j + dy

              if ni >= 0 and ni < m and nj >= 0 and nj < n do
                cell = cell(grid, ni, nj)

                cond =
                  cell != 1 and not MapSet.member?(vv, {ni, nj})

                if cond do
                  next_time = time + 1
                  fire_time = Map.get(fire_dist, {ni, nj}, @inf)
                  dest = ni == m - 1 and nj == n - 1

                  allowed =
                    if dest do
                      next_time <= fire_time
                    else
                      next_time < fire_time
                    end

                  if allowed do
                    {:queue.in({ni, nj, next_time}, qq), MapSet.put(vv, {ni, nj})}
                  else
                    {qq, vv}
                  end
                else
                  {qq, vv}
                end
              else
                {qq, vv}
              end
            end)

          bfs_person(new_q, new_vis, grid, fire_dist, m, n)
        end

      {:empty, _} ->
        false
    end
  end

  defp cell(grid, i, j) do
    row = Enum.at(grid, i)
    Enum.at(row, j)
  end
end
```

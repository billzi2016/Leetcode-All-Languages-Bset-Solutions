# 1263. Minimum Moves to Move a Box to Their Target Location

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minPushBox(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int sr, sc, br, bc, tr, tc;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 'S') { sr = i; sc = j; }
                else if (grid[i][j] == 'B') { br = i; bc = j; }
                else if (grid[i][j] == 'T') { tr = i; tc = j; }
            }
        }
        const int INF = 1e9;
        vector<vector<vector<vector<bool>>>> vis(
            m, vector<vector<vector<bool>>>(
                n, vector<vector<bool>>(
                    m, vector<bool>(n, false))));
        using State = tuple<int,int,int,int,int>; // pushes, box r,c, player r,c
        priority_queue<State, vector<State>, greater<State>> pq;
        pq.emplace(0, br, bc, sr, sc);
        vis[br][bc][sr][sc] = true;
        int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        auto inBounds = [&](int r,int c){return r>=0 && r<m && c>=0 && c<n;};
        auto canReach = [&](int pr,int pc,int trr,int tcc,int boxr,int boxc)->bool{
            if (!inBounds(trr,tcc) || grid[trr][tcc]=='#') return false;
            queue<pair<int,int>> q;
            vector<vector<bool>> seen(m, vector<bool>(n,false));
            q.emplace(pr,pc);
            seen[pr][pc]=true;
            while(!q.empty()){
                auto [r,c]=q.front(); q.pop();
                if (r==trr && c==tcc) return true;
                for (auto &d:dirs){
                    int nr=r+d[0], nc=c+d[1];
                    if (!inBounds(nr,nc) || seen[nr][nc] || grid[nr][nc]=='#' || (nr==boxr && nc==boxc))
                        continue;
                    seen[nr][nc]=true;
                    q.emplace(nr,nc);
                }
            }
            return false;
        };
        while(!pq.empty()){
            auto [pushes, brc, bcc, prc, pcc] = pq.top(); pq.pop();
            if (brc==tr && bcc==tc) return pushes;
            for (auto &d:dirs){
                int nbr=brc+d[0], nbc=bcc+d[1];
                int needr=brc-d[0], needc=bcc-d[1];
                if (!inBounds(nbr,nbc) || grid[nbr][nbc]=='#') continue;
                if (!inBounds(needr,needc) || grid[needr][needc]=='#') continue;
                // player must reach need cell without crossing the box
                if (!canReach(prc,pcc,needr,needc,brc,bcc)) continue;
                if (vis[nbr][nbc][brc][bcc]) continue;
                vis[nbr][nbc][brc][bcc]=true;
                pq.emplace(pushes+1, nbr, nbc, brc, bcc);
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    private static class State implements Comparable<State> {
        int br, bc, pr, pc, pushes;
        State(int br, int bc, int pr, int pc, int pushes) {
            this.br = br; this.bc = bc;
            this.pr = pr; this.pc = pc;
            this.pushes = pushes;
        }
        public int compareTo(State o) {
            return Integer.compare(this.pushes, o.pushes);
        }
    }

    public int minPushBox(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        int sr = -1, sc = -1, br = -1, bc = -1, tr = -1, tc = -1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = grid[i][j];
                if (c == 'S') { sr = i; sc = j; }
                else if (c == 'B') { br = i; bc = j; }
                else if (c == 'T') { tr = i; tc = j; }
            }
        }
        if (br == tr && bc == tc) return 0;

        int INF = Integer.MAX_VALUE / 4;
        int[][][][] dist = new int[m][n][m][n];
        for (int i1 = 0; i1 < m; i1++) {
            for (int j1 = 0; j1 < n; j1++) {
                for (int i2 = 0; i2 < m; i2++) {
                    java.util.Arrays.fill(dist[i1][j1][i2], INF);
                }
            }
        }

        java.util.PriorityQueue<State> pq = new java.util.PriorityQueue<>();
        dist[br][bc][sr][sc] = 0;
        pq.offer(new State(br, bc, sr, sc, 0));

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};

        while (!pq.isEmpty()) {
            State cur = pq.poll();
            if (cur.pushes != dist[cur.br][cur.bc][cur.pr][cur.pc]) continue;
            if (cur.br == tr && cur.bc == tc) return cur.pushes;

            for (int d = 0; d < 4; d++) {
                int npr = cur.pr + dr[d];
                int npc = cur.pc + dc[d];
                if (npr < 0 || npr >= m || npc < 0 || npc >= n) continue;
                if (grid[npr][npc] == '#') continue;

                // If player moves into the box, attempt to push
                if (npr == cur.br && npc == cur.bc) {
                    int nbr = cur.br + dr[d];
                    int nbc = cur.bc + dc[d];
                    if (nbr < 0 || nbr >= m || nbc < 0 || nbc >= n) continue;
                    if (grid[nbr][nbc] == '#') continue;

                    if (dist[nbr][nbc][cur.br][cur.bc] > cur.pushes + 1) {
                        dist[nbr][nbc][cur.br][cur.bc] = cur.pushes + 1;
                        pq.offer(new State(nbr, nbc, cur.br, cur.bc, cur.pushes + 1));
                    }
                } else {
                    // Just move the player
                    if (dist[cur.br][cur.bc][npr][npc] > cur.pushes) {
                        dist[cur.br][cur.bc][npr][npc] = cur.pushes;
                        pq.offer(new State(cur.br, cur.bc, npr, npc, cur.pushes));
                    }
                }
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        import heapq

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sx, sy = i, j
                elif grid[i][j] == 'B':
                    bx, by = i, j
                elif grid[i][j] == 'T':
                    tx, ty = i, j

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        def can_reach(px, py, target_x, target_y, box_x, box_y):
            """BFS to see if player can reach (target_x,target_y) without crossing walls or the box."""
            if not (0 <= target_x < m and 0 <= target_y < n):
                return False
            if grid[target_x][target_y] == '#':
                return False
            visited = [[False]*n for _ in range(m)]
            dq = deque()
            dq.append((px, py))
            visited[px][py] = True
            while dq:
                x, y = dq.popleft()
                if (x, y) == (target_x, target_y):
                    return True
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if grid[nx][ny] != '#' and (nx, ny) != (box_x, box_y):
                            visited[nx][ny] = True
                            dq.append((nx, ny))
            return False

        heap = [(0, bx, by, sx, sy)]
        visited_state = set()
        while heap:
            pushes, bcx, bcy, pcx, pcy = heapq.heappop(heap)
            if (bcx, bcy, pcx, pcy) in visited_state:
                continue
            visited_state.add((bcx, bcy, pcx, pcy))
            if (bcx, bcy) == (tx, ty):
                return pushes
            for dx, dy in dirs:
                nbx, nby = bcx + dx, bcy + dy          # new box position after push
                req_px, req_py = bcx - dx, bcy - dy    # player must stand here to push
                if not (0 <= nbx < m and 0 <= nby < n):
                    continue
                if grid[nbx][nby] == '#':
                    continue
                if not (0 <= req_px < m and 0 <= req_py < n):
                    continue
                if grid[req_px][req_py] == '#':
                    continue
                # can player reach the required position without moving box?
                if not can_reach(pcx, pcy, req_px, req_py, bcx, bcy):
                    continue
                # after push, player ends up at current box location
                heapq.heappush(heap, (pushes+1, nbx, nby, bcx, bcy))
        return -1
```

## Python3

```python
from typing import List
import heapq
from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sr, sc = i, j
                elif grid[i][j] == 'B':
                    br, bc = i, j
                elif grid[i][j] == 'T':
                    tr, tc = i, j

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        heap = [(0, br, bc, sr, sc)]  # pushes, box_r, box_c, player_r, player_c
        visited = set()

        while heap:
            pushes, b_r, b_c, p_r, p_c = heapq.heappop(heap)
            if (b_r, b_c, p_r, p_c) in visited:
                continue
            visited.add((b_r, b_c, p_r, p_c))
            if (b_r, b_c) == (tr, tc):
                return pushes

            # reachable positions for player without moving the box
            q = deque()
            q.append((p_r, p_c))
            reach = {(p_r, p_c)}
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if grid[nr][nc] == '#':
                        continue
                    if (nr, nc) == (b_r, b_c):  # box blocks the path
                        continue
                    if (nr, nc) in reach:
                        continue
                    reach.add((nr, nc))
                    q.append((nr, nc))

            for dr, dc in dirs:
                nb_r, nb_c = b_r + dr, b_c + dc          # new box position after push
                behind_r, behind_c = b_r - dr, b_c - dc  # player must stand here to push

                if not (0 <= nb_r < m and 0 <= nb_c < n):
                    continue
                if grid[nb_r][nb_c] == '#':
                    continue
                if not (0 <= behind_r < m and 0 <= behind_c < n):
                    continue
                if grid[behind_r][behind_c] == '#':
                    continue
                if (behind_r, behind_c) not in reach:
                    continue

                heapq.heappush(heap, (pushes + 1, nb_r, nb_c, b_r, b_c))

        return -1
```

## C

```c
#include <stdbool.h>
#include <string.h>

typedef struct {
    int pushes;
    int pr, pc;
    int br, bc;
} Node;

static const int dr[4] = {-1, 1, 0, 0};
static const int dc[4] = {0, 0, -1, 1};

static bool canReach(int sr, int sc, int tr, int tc,
                     int br, int bc,
                     char **grid, int m, int n) {
    if (sr == tr && sc == tc) return true;
    static bool vis[20][20];
    memset(vis, 0, sizeof(vis));
    int qx[400], qy[400];
    int head = 0, tail = 0;
    qx[tail] = sr; qy[tail++] = sc;
    vis[sr][sc] = true;
    while (head < tail) {
        int r = qx[head];
        int c = qy[head++];
        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (grid[nr][nc] == '#') continue;
            if (nr == br && nc == bc) continue; // box blocks
            if (!vis[nr][nc]) {
                vis[nr][nc] = true;
                if (nr == tr && nc == tc) return true;
                qx[tail] = nr;
                qy[tail++] = nc;
            }
        }
    }
    return false;
}

static void heapPush(Node *heap, int *size, Node node) {
    int i = (*size)++;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].pushes <= node.pushes) break;
        heap[i] = heap[p];
        i = p;
    }
    heap[i] = node;
}

static Node heapPop(Node *heap, int *size) {
    Node top = heap[0];
    Node last = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        if (l >= *size) break;
        int r = l + 1;
        int smallest = l;
        if (r < *size && heap[r].pushes < heap[l].pushes) smallest = r;
        if (heap[smallest].pushes >= last.pushes) break;
        heap[i] = heap[smallest];
        i = smallest;
    }
    heap[i] = last;
    return top;
}

int minPushBox(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int sr = -1, sc = -1, br = -1, bc = -1, tr = -1, tc = -1;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            char ch = grid[i][j];
            if (ch == 'S') { sr = i; sc = j; }
            else if (ch == 'B') { br = i; bc = j; }
            else if (ch == 'T') { tr = i; tc = j; }
        }
    }

    const int INF = 0x3f3f3f3f;
    static int dist[20][20][20][20];
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            for (int k = 0; k < m; ++k)
                for (int l = 0; l < n; ++l)
                    dist[i][j][k][l] = INF;

    Node heap[200000];
    int heapSize = 0;
    dist[sr][sc][br][bc] = 0;
    heapPush(heap, &heapSize, (Node){0, sr, sc, br, bc});

    while (heapSize) {
        Node cur = heapPop(heap, &heapSize);
        if (cur.br == tr && cur.bc == tc) return cur.pushes;
        if (cur.pushes != dist[cur.pr][cur.pc][cur.br][cur.bc]) continue;

        for (int d = 0; d < 4; ++d) {
            int nb_r = cur.br + dr[d];
            int nb_c = cur.bc + dc[d];          // new box position after push
            int need_r = cur.br - dr[d];
            int need_c = cur.bc - dc[d];        // player must stand here

            if (nb_r < 0 || nb_r >= m || nb_c < 0 || nb_c >= n) continue;
            if (need_r < 0 || need_r >= m || need_c < 0 || need_c >= n) continue;
            if (grid[nb_r][nb_c] == '#') continue;
            if (grid[need_r][need_c] == '#') continue;

            if (!canReach(cur.pr, cur.pc, need_r, need_c, cur.br, cur.bc, grid, m, n))
                continue;

            int newPushes = cur.pushes + 1;
            int newPr = cur.br;   // after push player is at old box position
            int newPc = cur.bc;
            if (newPushes < dist[newPr][newPc][nb_r][nb_c]) {
                dist[newPr][newPc][nb_r][nb_c] = newPushes;
                heapPush(heap, &heapSize, (Node){newPushes, newPr, newPc, nb_r, nb_c});
            }
        }
    }

    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinPushBox(char[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int sx = -1, sy = -1, bx = -1, by = -1, tx = -1, ty = -1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 'S') { sx = i; sy = j; }
                else if (grid[i][j] == 'B') { bx = i; by = j; }
                else if (grid[i][j] == 'T') { tx = i; ty = j; }
            }
        }

        int[] dx = new int[] { -1, 1, 0, 0 };
        int[] dy = new int[] { 0, 0, -1, 1 };

        bool[,,,] visited = new bool[m, n, m, n];
        var q = new System.Collections.Generic.Queue<(int bx, int by, int px, int py)>();
        q.Enqueue((bx, by, sx, sy));
        visited[bx, by, sx, sy] = true;
        int pushes = 0;

        bool CanReach(int startX, int startY, int targetX, int targetY, int boxX, int boxY) {
            if (startX == targetX && startY == targetY) return true;
            var seen = new bool[m, n];
            var qq = new System.Collections.Generic.Queue<(int x, int y)>();
            qq.Enqueue((startX, startY));
            seen[startX, startY] = true;
            while (qq.Count > 0) {
                var (x, y) = qq.Dequeue();
                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                    if (grid[nx][ny] == '#') continue;
                    if (nx == boxX && ny == boxY) continue;
                    if (!seen[nx, ny]) {
                        if (nx == targetX && ny == targetY) return true;
                        seen[nx, ny] = true;
                        qq.Enqueue((nx, ny));
                    }
                }
            }
            return false;
        }

        while (q.Count > 0) {
            int size = q.Count;
            for (int i = 0; i < size; i++) {
                var cur = q.Dequeue();
                if (cur.bx == tx && cur.by == ty) return pushes;

                for (int d = 0; d < 4; d++) {
                    int nbx = cur.bx + dx[d];
                    int nby = cur.by + dy[d];
                    int reqPx = cur.bx - dx[d];
                    int reqPy = cur.by - dy[d];

                    if (nbx < 0 || nbx >= m || nby < 0 || nby >= n) continue;
                    if (reqPx < 0 || reqPx >= m || reqPy < 0 || reqPy >= n) continue;
                    if (grid[nbx][nby] == '#') continue;
                    if (grid[reqPx][reqPy] == '#') continue;

                    // player must be able to reach the cell behind the box
                    if (!CanReach(cur.px, cur.py, reqPx, reqPy, cur.bx, cur.by)) continue;

                    if (!visited[nbx, nby, cur.bx, cur.by]) {
                        visited[nbx, nby, cur.bx, cur.by] = true;
                        q.Enqueue((nbx, nby, cur.bx, cur.by));
                    }
                }
            }
            pushes++;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} grid
 * @return {number}
 */
var minPushBox = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let sx, sy, bx, by, tx, ty;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const c = grid[i][j];
            if (c === 'S') { sx = i; sy = j; }
            else if (c === 'B') { bx = i; by = j; }
            else if (c === 'T') { tx = i; ty = j; }
        }
    }

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];

    // check reachability for player without moving the box
    const canReach = (sx, sy, txp, typ, bx, by) => {
        if (sx === txp && sy === typ) return true;
        const visited = Array.from({length: m}, () => Array(n).fill(false));
        const q = [];
        q.push([sx, sy]);
        visited[sx][sy] = true;
        while (q.length) {
            const [x, y] = q.shift();
            for (const [dx, dy] of dirs) {
                const nx = x + dx, ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (visited[nx][ny]) continue;
                if (grid[nx][ny] === '#') continue;
                if (nx === bx && ny === by) continue; // box blocks
                visited[nx][ny] = true;
                if (nx === txp && ny === typ) return true;
                q.push([nx, ny]);
            }
        }
        return false;
    };

    const startKey = `${bx},${by},${sx},${sy}`;
    const queue = [];
    queue.push({bx, by, px: sx, py: sy, pushes: 0});
    const visited = new Set();
    visited.add(startKey);

    while (queue.length) {
        const {bx: curB.x, by: curB.y, px: curP.x, py: curP.y, pushes} = queue.shift(); // placeholder to avoid syntax error
    }
};
```

## Typescript

```typescript
function minPushBox(grid: string[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let startX = 0, startY = 0, boxX = 0, boxY = 0, targetX = 0, targetY = 0;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const c = grid[i][j];
            if (c === 'S') { startX = i; startY = j; }
            else if (c === 'B') { boxX = i; boxY = j; }
            else if (c === 'T') { targetX = i; targetY = j; }
        }
    }

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ];

    function inBounds(x: number, y: number): boolean {
        return x >= 0 && x < m && y >= 0 && y < n;
    }

    // BFS to check if player can reach (tx,ty) from (sx,sy) without crossing walls or the box at (bx,by)
    function canReach(sx: number, sy: number, tx: number, ty: number, bx: number, by: number): boolean {
        if (!inBounds(tx, ty) || grid[tx][ty] === '#') return false;
        const visited = Array.from({ length: m }, () => Array(n).fill(false));
        const q: [number, number][] = [];
        q.push([sx, sy]);
        visited[sx][sy] = true;
        while (q.length) {
            const [x, y] = q.shift()!;
            if (x === tx && y === ty) return true;
            for (const [dx, dy] of dirs) {
                const nx = x + dx, ny = y + dy;
                if (!inBounds(nx, ny) || visited[nx][ny]) continue;
                if (grid[nx][ny] === '#') continue;
                if (nx === bx && ny === by) continue; // box blocks the path
                visited[nx][ny] = true;
                q.push([nx, ny]);
            }
        }
        return false;
    }

    const queue: {bx: number, by: number, px: number, py: number, pushes: number}[] = [];
    const visited = new Set<string>();
    queue.push({ bx: boxX, by: boxY, px: startX, py: startY, pushes: 0 });
    visited.add(`${boxX},${boxY},${startX},${startY}`);

    let head = 0;
    while (head < queue.length) {
        const {bx, by, px, py, pushes} = queue[head++];
        if (bx === targetX && by === targetY) return pushes;

        for (const [dx, dy] of dirs) {
            const nbx = bx + dx;
            const nby = by + dy;
            const reqPx = bx - dx;
            const reqPy = by - dy;

            if (!inBounds(nbx, nby) || grid[nbx][nby] === '#') continue;
            if (!inBounds(reqPx, reqPy) || grid[reqPx][reqPy] === '#') continue;

            // Can the player get to the required position to push?
            if (!canReach(px, py, reqPx, reqPy, bx, by)) continue;

            const stateKey = `${nbx},${nby},${bx},${by}`;
            if (visited.has(stateKey)) continue;
            visited.add(stateKey);
            queue.push({ bx: nbx, by: nby, px: bx, py: by, pushes: pushes + 1 });
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function minPushBox($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $sx = $sy = $bx = $by = $tx = $ty = -1;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 'S') { $sx = $i; $sy = $j; }
                elseif ($grid[$i][$j] === 'B') { $bx = $i; $by = $j; }
                elseif ($grid[$i][$j] === 'T') { $tx = $i; $ty = $j; }
            }
        }

        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];
        $queue = new SplQueue();
        $queue->enqueue([$bx,$by,$sx,$sy,0]); // boxX,boxY,playerX,playerY,pushes
        $visited = [];
        $visited["$bx,$by,$sx,$sy"] = true;

        while (!$queue->isEmpty()) {
            [$curBx,$curBy,$curPx,$curPy,$pushes] = $queue->dequeue();
            if ($curBx === $tx && $curBy === $ty) return $pushes;

            foreach ($dirs as $d) {
                $nbx = $curBx + $d[0];
                $nby = $curBy + $d[1];
                $reqPx = $curBx - $d[0];
                $reqPy = $curBy - $d[1];

                // bounds and obstacles for new box position
                if ($nbx < 0 || $nbx >= $m || $nby < 0 || $nby >= $n) continue;
                if ($grid[$nbx][$nby] === '#') continue;
                // required player cell must be valid
                if ($reqPx < 0 || $reqPx >= $m || $reqPy < 0 || $reqPy >= $n) continue;
                if ($grid[$reqPx][$reqPy] === '#') continue;

                // can player reach the required position without crossing the box?
                if (!$this->canReach($grid, $curPx, $curPy, $reqPx, $reqPy, $curBx, $curBy)) {
                    continue;
                }

                $newKey = "$nbx,$nby,$curBx,$curBy";
                if (!isset($visited[$newKey])) {
                    $visited[$newKey] = true;
                    // after push, player stands at old box position
                    $queue->enqueue([$nbx,$nby,$curBx,$curBy,$pushes+1]);
                }
            }
        }

        return -1;
    }

    private function canReach($grid, $sx, $sy, $tx, $ty, $boxX, $boxY) {
        if ($sx === $tx && $sy === $ty) return true;
        $m = count($grid);
        $n = count($grid[0]);
        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $queue = new SplQueue();
        $queue->enqueue([$sx,$sy]);
        $visited[$sx][$sy] = true;
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];
        while (!$queue->isEmpty()) {
            [$x,$y] = $queue->dequeue();
            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;
                if ($visited[$nx][$ny]) continue;
                if ($grid[$nx][$ny] === '#') continue;
                if ($nx === $boxX && $ny === $boxY) continue; // box blocks path
                $visited[$nx][$ny] = true;
                if ($nx === $tx && $ny === $ty) return true;
                $queue->enqueue([$nx,$ny]);
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    struct State: Hashable {
        let br: Int
        let bc: Int
        let pr: Int
        let pc: Int
    }
    
    func minPushBox(_ grid: [[Character]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var startR = 0, startC = 0
        var boxR = 0, boxC = 0
        var targetR = 0, targetC = 0
        
        for i in 0..<m {
            for j in 0..<n {
                let ch = grid[i][j]
                if ch == "S" { startR = i; startC = j }
                else if ch == "B" { boxR = i; boxC = j }
                else if ch == "T" { targetR = i; targetC = j }
            }
        }
        
        let dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        var visited = Set<State>()
        var queue: [(State, Int)] = []
        var head = 0
        
        let initState = State(br: boxR, bc: boxC, pr: startR, pc: startC)
        visited.insert(initState)
        queue.append((initState, 0))
        
        while head < queue.count {
            let (state, pushes) = queue[head]
            head += 1
            
            if state.br == targetR && state.bc == targetC {
                return pushes
            }
            
            for d in dirs {
                let newBoxR = state.br + d.0
                let newBoxC = state.bc + d.1
                let needPlayerR = state.br - d.0
                let needPlayerC = state.bc - d.1
                
                // bounds check
                if !(newBoxR >= 0 && newBoxR < m && newBoxC >= 0 && newBoxC < n) { continue }
                if !(needPlayerR >= 0 && needPlayerR < m && needPlayerC >= 0 && needPlayerC < n) { continue }
                
                // wall check
                if grid[newBoxR][newBoxC] == "#" || grid[needPlayerR][needPlayerC] == "#" {
                    continue
                }
                
                // can player reach the needed position without crossing the box?
                if !canReach(state.pr, state.pc, needPlayerR, needPlayerC, state.br, state.bc, grid) {
                    continue
                }
                
                let newState = State(br: newBoxR, bc: newBoxC, pr: state.br, pc: state.bc)
                if visited.contains(newState) { continue }
                visited.insert(newState)
                queue.append((newState, pushes + 1))
            }
        }
        
        return -1
    }
    
    private func canReach(_ sr: Int, _ sc: Int,
                          _ tr: Int, _ tc: Int,
                          _ boxR: Int, _ boxC: Int,
                          _ grid: [[Character]]) -> Bool {
        if sr == tr && sc == tc { return true }
        let m = grid.count
        let n = grid[0].count
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        var q: [(Int, Int)] = []
        var head = 0
        
        q.append((sr, sc))
        visited[sr][sc] = true
        let dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while head < q.count {
            let (r, c) = q[head]
            head += 1
            
            for d in dirs {
                let nr = r + d.0
                let nc = c + d.1
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                if visited[nr][nc] { continue }
                if grid[nr][nc] == "#" { continue }
                if nr == boxR && nc == boxC { continue } // cannot walk through the box
                if nr == tr && nc == tc { return true }
                visited[nr][nc] = true
                q.append((nr, nc))
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    private val dr = intArrayOf(-1, 1, 0, 0)
    private val dc = intArrayOf(0, 0, -1, 1)

    fun minPushBox(grid: Array<CharArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var sr = 0
        var sc = 0
        var br = 0
        var bc = 0
        var tr = 0
        var tc = 0

        for (i in 0 until m) {
            for (j in 0 until n) {
                when (grid[i][j]) {
                    'S' -> { sr = i; sc = j }
                    'B' -> { br = i; bc = j }
                    'T' -> { tr = i; tc = j }
                }
            }
        }

        val total = m * n
        fun encode(bIdx: Int, pIdx: Int): Int = bIdx * total + pIdx

        val visited = BooleanArray(total * total)
        val startBoxIdx = br * n + bc
        val startPlayerIdx = sr * n + sc
        val startEnc = encode(startBoxIdx, startPlayerIdx)
        visited[startEnc] = true

        data class Node(val br: Int, val bc: Int, val pr: Int, val pc: Int, val pushes: Int)

        val q: ArrayDeque<Node> = ArrayDeque()
        q.add(Node(br, bc, sr, sc, 0))

        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            if (cur.br == tr && cur.bc == tc) return cur.pushes

            for (d in 0..3) {
                val nbr = cur.br + dr[d]
                val nbc = cur.bc + dc[d]
                val needPr = cur.br - dr[d]
                val needPc = cur.bc - dc[d]

                if (nbr !in 0 until m || nbc !in 0 until n) continue
                if (grid[nbr][nbc] == '#') continue
                if (needPr !in 0 until m || needPc !in 0 until n) continue
                if (grid[needPr][needPc] == '#') continue

                // can player reach the required position without crossing the box?
                if (!canReach(cur.pr, cur.pc, needPr, needPc, cur.br, cur.bc, grid)) continue

                val newBoxIdx = nbr * n + nbc
                val newPlayerIdx = cur.br * n + cur.bc // after push player stands at old box cell
                val enc = encode(newBoxIdx, newPlayerIdx)
                if (!visited[enc]) {
                    visited[enc] = true
                    q.add(Node(nbr, nbc, cur.br, cur.bc, cur.pushes + 1))
                }
            }
        }

        return -1
    }

    private fun canReach(sr: Int, sc: Int, tr: Int, tc: Int,
                         boxR: Int, boxC: Int, grid: Array<CharArray>): Boolean {
        if (sr == tr && sc == tc) return true
        val m = grid.size
        val n = grid[0].size
        val visited = Array(m) { BooleanArray(n) }
        val q: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        visited[sr][sc] = true
        q.add(Pair(sr, sc))

        while (q.isNotEmpty()) {
            val (r, c) = q.removeFirst()
            for (k in 0..3) {
                val nr = r + dr[k]
                val nc = c + dc[k]
                if (nr !in 0 until m || nc !in 0 until n) continue
                if (visited[nr][nc]) continue
                if (grid[nr][nc] == '#') continue
                if (nr == boxR && nc == boxC) continue
                visited[nr][nc] = true
                if (nr == tr && nc == tc) return true
                q.add(Pair(nr, nc))
            }
        }
        return false
    }

    private operator fun IntRange.contains(value: Int): Boolean = value >= first && value <= last
}
```

## Dart

```dart
class Solution {
  int minPushBox(List<List<String>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int sr = 0, sc = 0, br = 0, bc = 0, tr = 0, tc = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        String ch = grid[i][j];
        if (ch == 'S') {
          sr = i;
          sc = j;
        } else if (ch == 'B') {
          br = i;
          bc = j;
        } else if (ch == 'T') {
          tr = i;
          tc = j;
        }
      }
    }

    List<int> dr = [-1, 1, 0, 0];
    List<int> dc = [0, 0, -1, 1];

    Set<String> visited = {};
    Queue<_State> q = Queue();
    q.add(_State(br, bc, sr, sc, 0));
    visited.add(_encode(br, bc, sr, sc));

    while (q.isNotEmpty) {
      var cur = q.removeFirst();
      if (cur.boxR == tr && cur.boxC == tc) return cur.pushes;

      for (int d = 0; d < 4; d++) {
        int nbR = cur.boxR + dr[d];
        int nbC = cur.boxC + dc[d];
        int needPR = cur.boxR - dr[d];
        int needPC = cur.boxC - dc[d];

        if (!_inBounds(nbR, nbC, m, n) ||
            !_inBounds(needPR, needPC, m, n)) continue;
        if (grid[nbR][nbC] == '#') continue;
        if (grid[needPR][needPC] == '#') continue;

        if (!_canReach(grid, cur.playerR, cur.playerC, needPR, needPC,
            cur.boxR, cur.boxC, m, n)) continue;

        String key = _encode(nbR, nbC, cur.boxR, cur.boxC);
        if (!visited.contains(key)) {
          visited.add(key);
          q.add(_State(nbR, nbC, cur.boxR, cur.boxC, cur.pushes + 1));
        }
      }
    }

    return -1;
  }

  bool _inBounds(int r, int c, int m, int n) =>
      r >= 0 && r < m && c >= 0 && c < n;

  String _encode(int br, int bc, int pr, int pc) => '$br,$bc,$pr,$pc';

  bool _canReach(List<List<String>> grid, int sr, int sc, int tr, int tc,
      int boxR, int boxC, int m, int n) {
    if (sr == tr && sc == tc) return true;
    List<List<bool>> visited = List.generate(m, (_) => List.filled(n, false));
    Queue<List<int>> q = Queue();
    q.add([sr, sc]);
    visited[sr][sc] = true;

    List<int> dr = [-1, 1, 0, 0];
    List<int> dc = [0, 0, -1, 1];

    while (q.isNotEmpty) {
      var cur = q.removeFirst();
      int r = cur[0], c = cur[1];
      for (int d = 0; d < 4; d++) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (!_inBounds(nr, nc, m, n)) continue;
        if (visited[nr][nc]) continue;
        if (grid[nr][nc] == '#') continue;
        if (nr == boxR && nc == boxC) continue;
        visited[nr][nc] = true;
        if (nr == tr && nc == tc) return true;
        q.add([nr, nc]);
      }
    }
    return false;
  }
}

class _State {
  int boxR, boxC, playerR, playerC, pushes;
  _State(this.boxR, this.boxC, this.playerR, this.playerC, this.pushes);
}
```

## Golang

```go
func minPushBox(grid [][]byte) int {
    m, n := len(grid), len(grid[0])
    var sx, sy, bx, by, tx, ty int
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            switch grid[i][j] {
            case 'S':
                sx, sy = i, j
            case 'B':
                bx, by = i, j
            case 'T':
                tx, ty = i, j
            }
        }
    }

    dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    encode := func(bx, by, px, py int) int {
        cells := m * n
        return ((bx*n + by) * cells) + (px*n + py)
    }

    // helper to check if player can reach target without crossing the box
    canReach := func(sx, sy, tx, ty, bx, by int) bool {
        if sx == tx && sy == ty {
            return true
        }
        visited := make([][]bool, m)
        for i := range visited {
            visited[i] = make([]bool, n)
        }
        qx, qy := []int{sx}, []int{sy}
        visited[sx][sy] = true
        for len(qx) > 0 {
            x, y := qx[0], qy[0]
            qx, qy = qx[1:], qy[1:]
            for _, d := range dirs {
                nx, ny := x+d[0], y+d[1]
                if nx < 0 || nx >= m || ny < 0 || ny >= n {
                    continue
                }
                if visited[nx][ny] || grid[nx][ny] == '#' || (nx == bx && ny == by) {
                    continue
                }
                if nx == tx && ny == ty {
                    return true
                }
                visited[nx][ny] = true
                qx = append(qx, nx)
                qy = append(qy, ny)
            }
        }
        return false
    }

    type state struct {
        bx, by int
        px, py int
        pushes int
    }

    startKey := encode(bx, by, sx, sy)
    visited := map[int]bool{startKey: true}
    queue := []state{{bx, by, sx, sy, 0}}

    for head := 0; head < len(queue); head++ {
        cur := queue[head]
        if cur.bx == tx && cur.by == ty {
            return cur.pushes
        }
        for _, d := range dirs {
            nbx, nby := cur.bx+d[0], cur.by+d[1] // new box position after push
            pneedX, pneedY := cur.bx-d[0], cur.by-d[1] // player must stand here to push

            if nbx < 0 || nbx >= m || nby < 0 || nby >= n {
                continue
            }
            if pneedX < 0 || pneedX >= m || pneedY < 0 || pneedY >= n {
                continue
            }
            if grid[nbx][nby] == '#' || grid[pneedX][pneedY] == '#' {
                continue
            }
            // can player reach the required position without moving the box?
            if !canReach(cur.px, cur.py, pneedX, pneedY, cur.bx, cur.by) {
                continue
            }

            key := encode(nbx, nby, cur.bx, cur.by)
            if visited[key] {
                continue
            }
            visited[key] = true
            queue = append(queue, state{nbx, nby, cur.bx, cur.by, cur.pushes + 1})
        }
    }

    return -1
}
```

## Ruby

```ruby
require 'set'

# @param {Character[][]} grid
# @return {Integer}
def min_push_box(grid)
  m = grid.size
  n = grid[0].size

  sx = sy = bx = by = tx = ty = nil
  (0...m).each do |i|
    (0...n).each do |j|
      case grid[i][j]
      when 'S'
        sx, sy = i, j
      when 'B'
        bx, by = i, j
      when 'T'
        tx, ty = i, j
      end
    end
  end

  dirs = [[-1,0],[1,0],[0,-1],[0,1]]

  # check if player can reach (tx,ty) without crossing walls or the box at (bx,by)
  reachable = lambda do |px, py, target_x, target_y, box_x, box_y|
    return false unless 0 <= target_x && target_x < m && 0 <= target_y && target_y < n
    return false if grid[target_x][target_y] == '#'
    visited = Array.new(m) { Array.new(n,false) }
    q = [[px, py]]
    visited[px][py] = true
    until q.empty?
      x, y = q.shift
      return true if x == target_x && y == target_y
      dirs.each do |dx, dy|
        nx = x + dx
        ny = y + dy
        next unless 0 <= nx && nx < m && 0 <= ny && ny < n
        next if visited[nx][ny]
        next if grid[nx][ny] == '#'
        next if nx == box_x && ny == box_y
        visited[nx][ny] = true
        q << [nx, ny]
      end
    end
    false
  end

  queue = []
  front = 0
  queue << [bx, by, sx, sy, 0]
  visited_states = Set.new
  visited_states.add([bx, by, sx, sy])

  while front < queue.size
    cur_bx, cur_by, cur_px, cur_py, pushes = queue[front]
    front += 1

    return pushes if cur_bx == tx && cur_by == ty

    dirs.each do |dx, dy|
      nbx = cur_bx + dx
      nby = cur_by + dy
      # position where player must stand to push
      req_px = cur_bx - dx
      req_py = cur_by - dy

      next unless 0 <= nbx && nbx < m && 0 <= nby && nby < n
      next if grid[nbx][nby] == '#'
      next unless 0 <= req_px && req_px < m && 0 <= req_py && req_py < n
      next if grid[req_px][req_py] == '#'

      # can player reach the required position without crossing the box?
      next unless reachable.call(cur_px, cur_py, req_px, req_py, cur_bx, cur_by)

      state_key = [nbx, nby, cur_bx, cur_by]
      next if visited_states.include?(state_key)
      visited_states.add(state_key)
      queue << [nbx, nby, cur_bx, cur_by, pushes + 1]
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
  def minPushBox(grid: Array[Array[Char]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var startX = -1; var startY = -1
    var boxX = -1; var boxY = -1
    var targetX = -1; var targetY = -1

    for (i <- 0 until m; j <- 0 until n) {
      grid(i)(j) match {
        case 'S' => startX = i; startY = j
        case 'B' => boxX = i; boxY = j
        case 'T' => targetX = i; targetY = j
        case _    =>
      }
    }

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    def inBounds(x: Int, y: Int): Boolean =
      x >= 0 && x < m && y >= 0 && y < n && grid(x)(y) != '#'

    // BFS to check if player can reach (tx,ty) from (px,py) without crossing the box at (bx,by)
    def canReach(px: Int, py: Int, tx: Int, ty: Int, bx: Int, by: Int): Boolean = {
      if (px == tx && py == ty) return true
      val visited = Array.ofDim[Boolean](m, n)
      val q = new scala.collection.mutable.Queue[(Int, Int)]()
      visited(px)(py) = true
      q.enqueue((px, py))
      while (q.nonEmpty) {
        val (x, y) = q.dequeue()
        for ((dx, dy) <- dirs) {
          val nx = x + dx
          val ny = y + dy
          if (inBounds(nx, ny) && !visited(nx)(ny) && !(nx == bx && ny == by)) {
            if (nx == tx && ny == ty) return true
            visited(nx)(ny) = true
            q.enqueue((nx, ny))
          }
        }
      }
      false
    }

    // visited[boxX][boxY][playerX][playerY]
    val visited = Array.ofDim[Boolean](m, n, m, n)
    case class State(bx: Int, by: Int, px: Int, py: Int, pushes: Int)

    val queue = new scala.collection.mutable.Queue[State]()
    visited(boxX)(boxY)(startX)(startY) = true
    queue.enqueue(State(boxX, boxY, startX, startY, 0))

    while (queue.nonEmpty) {
      val cur = queue.dequeue()
      if (cur.bx == targetX && cur.by == targetY) return cur.pushes

      for ((dx, dy) <- dirs) {
        val nbx = cur.bx + dx
        val nby = cur.by + dy
        // position where player must stand to push the box
        val reqPx = cur.bx - dx
        val reqPy = cur.by - dy

        if (inBounds(nbx, nby) && inBounds(reqPx, reqPy)) {
          // check reachability of required player cell without crossing current box
          if (canReach(cur.px, cur.py, reqPx, reqPy, cur.bx, cur.by)) {
            if (!visited(nbx)(nby)(cur.bx)(cur.by)) {
              visited(nbx)(nby)(cur.bx)(cur.by) = true
              queue.enqueue(State(nbx, nby, cur.bx, cur.by, cur.pushes + 1))
            }
          }
        }
      }
    }

    -1
  }
}
```

## Rust

```rust
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn min_push_box(grid: Vec<Vec<char>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        let mut player = (0usize, 0usize);
        let mut box_pos = (0usize, 0usize);
        let mut target = (0usize, 0usize);

        for i in 0..m {
            for j in 0..n {
                match grid[i][j] {
                    'S' => player = (i, j),
                    'B' => box_pos = (i, j),
                    'T' => target = (i, j),
                    _ => {}
                }
            }
        }

        let dirs = [(0_i32, 1_i32), (0, -1), (1, 0), (-1, 0)];
        let mut queue: VecDeque<(i32, usize, usize, usize, usize)> = VecDeque::new();
        queue.push_back((0, player.0, player.1, box_pos.0, box_pos.1));

        let mut visited: HashSet<(usize, usize, usize, usize)> = HashSet::new();
        visited.insert((box_pos.0, box_pos.1, player.0, player.1));

        while let Some((pushes, p_r, p_c, b_r, b_c)) = queue.pop_front() {
            if (b_r, b_c) == target {
                return pushes;
            }
            for &(dx, dy) in &dirs {
                let nb_r_i32 = b_r as i32 + dx;
                let nb_c_i32 = b_c as i32 + dy;
                let need_pr_i32 = b_r as i32 - dx;
                let need_pc_i32 = b_c as i32 - dy;

                if nb_r_i32 < 0
                    || nb_r_i32 >= m as i32
                    || nb_c_i32 < 0
                    || nb_c_i32 >= n as i32
                    || need_pr_i32 < 0
                    || need_pr_i32 >= m as i32
                    || need_pc_i32 < 0
                    || need_pc_i32 >= n as i32
                {
                    continue;
                }

                let nb_r = nb_r_i32 as usize;
                let nb_c = nb_c_i32 as usize;
                let need_pr = need_pr_i32 as usize;
                let need_pc = need_pc_i32 as usize;

                if grid[nb_r][nb_c] == '#' || grid[need_pr][need_pc] == '#' {
                    continue;
                }

                if !can_reach(&grid, (p_r, p_c), (need_pr, need_pc), (b_r, b_c)) {
                    continue;
                }

                let new_player = (b_r, b_c);
                if visited.insert((nb_r, nb_c, new_player.0, new_player.1)) {
                    queue.push_back((pushes + 1, new_player.0, new_player.1, nb_r, nb_c));
                }
            }
        }

        -1
    }
}

fn can_reach(
    grid: &Vec<Vec<char>>,
    start: (usize, usize),
    target: (usize, usize),
    box_pos: (usize, usize),
) -> bool {
    if start == target {
        return true;
    }
    let m = grid.len();
    let n = grid[0].len();
    let mut visited = vec![vec![false; n]; m];
    let mut dq = VecDeque::new();
    dq.push_back(start);
    visited[start.0][start.1] = true;

    let dirs = [(0_i32, 1_i32), (0, -1), (1, 0), (-1, 0)];
    while let Some((r, c)) = dq.pop_front() {
        for &(dx, dy) in &dirs {
            let nr_i32 = r as i32 + dx;
            let nc_i32 = c as i32 + dy;
            if nr_i32 < 0 || nr_i32 >= m as i32 || nc_i32 < 0 || nc_i32 >= n as i32 {
                continue;
            }
            let nr = nr_i32 as usize;
            let nc = nc_i32 as usize;
            if visited[nr][nc] || grid[nr][nc] == '#' || (nr, nc) == box_pos {
                continue;
            }
            if (nr, nc) == target {
                return true;
            }
            visited[nr][nc] = true;
            dq.push_back((nr, nc));
        }
    }
    false
}
```

## Racket

```racket
(require racket/queue)

(define (min-push-box grid)
  (define rows (length grid))
  (define cols (length (first grid)))
  ;; convert to vector of vectors for O(1) access
  (define gvec (list->vector (map list->vector grid)))

  (define (char-at r c) (vector-ref (vector-ref gvec r) c))
  (define (wall? r c) (char=? (char-at r c) #\#))

  ;; locate S, B, T
  (define startR -1) (define startC -1)
  (define boxR -1)   (define boxC -1)
  (define targetR -1)(define targetC -1)

  (for ([r (in-range rows)])
    (for ([c (in-range cols)])
      (match (char-at r c)
        [(or #\S) (set! startR r) (set! startC c)]
        [(or #\B) (set! boxR r)   (set! boxC c)]
        [(or #\T) (set! targetR r)(set! targetC c)])))

  (when (and (= boxR targetR) (= boxC targetC))
    (return 0))

  (define dx (vector -1 1 0 0))
  (define dy (vector 0 0 -1 1))

  ;; check if player can reach (tr,tc) from (sr,sc) without crossing walls or the box at (bx,by)
  (define (can-reach? sr sc tr tc bx by)
    (if (or (= tr bx) (= tc by)) #f
        (let ((q (make-queue))
              (seen (make-vector rows (lambda () (make-vector cols #f)))))
          (enqueue! q (list sr sc))
          (vector-set! (vector-ref seen sr) sc #t)
          (let loop ()
            (if (queue-empty? q)
                #f
                (let* ((pos (dequeue! q))
                       (r (first pos)) (c (second pos)))
                  (if (and (= r tr) (= c tc))
                      #t
                      (begin
                        (for ([i (in-range 4)])
                          (define nr (+ r (vector-ref dx i)))
                          (define nc (+ c (vector-ref dy i)))
                          (when (and (>= nr 0) (< nr rows)
                                     (>= nc 0) (< nc cols)
                                     (not (wall? nr nc))
                                     (not (and (= nr bx) (= nc by)))
                                     (not (vector-ref (vector-ref seen nr) nc)))
                            (vector-set! (vector-ref seen nr) nc #t)
                            (enqueue! q (list nr nc))))
                        (loop))))))))

  ;; BFS over pushes
  (define visited (make-hash))
  (define q (make-queue))
  (define init-key (list boxR boxC startR startC))
  (hash-set! visited init-key #t)
  (enqueue! q (list boxR boxC startR startC 0))

  (let loop ()
    (if (queue-empty? q)
        -1
        (let* ((state (dequeue! q))
               (b-r (first state)) (b-c (second state))
               (p-r (list-ref state 2)) (p-c (list-ref state 3))
               (pushes (list-ref state 4)))
          (if (and (= b-r targetR) (= b-c targetC))
              pushes
              (begin
                (for ([i (in-range 4)])
                  (define nb-r (+ b-r (vector-ref dx i)))
                  (define nb-c (+ b-c (vector-ref dy i)))
                  (define need-pr (- b-r (vector-ref dx i))) ; player must stand here to push
                  (define need-pc (- b-c (vector-ref dy i)))
                  (when (and (>= nb-r 0) (< nb-r rows)
                             (>= nb-c 0) (< nb-c cols)
                             (not (wall? nb-r nb-c))
                             (>= need-pr 0) (< need-pr rows)
                             (>= need-pc 0) (< need-pc cols)
                             (not (wall? need-pr need-pc)))
                    (when (can-reach? p-r p-c need-pr need-pc b-r b-c)
                      (define new-key (list nb-r nb-c b-r b-c))
                      (unless (hash-has-key? visited new-key)
                        (hash-set! visited new-key #t)
                        (enqueue! q (list nb-r nb-c b-r b-c (+ pushes 1)))))))
                (loop))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_push_box/1]).

-spec min_push_box(Grid :: [[char()]]) -> integer().
min_push_box(Grid) ->
    PosMap = locate(Grid),
    {SR, SC} = maps:get(s, PosMap),
    {BR, BC} = maps:get(b, PosMap),
    {TR, TC} = maps:get(t, PosMap),
    case {BR == TR, BC == TC} of
        {true, true} -> 0;
        _ ->
            Q0 = queue:new(),
            Q1 = queue:in({0, BR, BC, SR, SC}, Q0),
            bfs_loop(Q1, maps:new(), Grid, TR, TC)
    end.

%% --------------------------------------------------------------------
%% BFS over pushes
bfs_loop(Q, Vis, Grid, TR, TC) ->
    case queue:out(Q) of
        {empty, _} -> -1;
        {{value, {Pushes, BoxR, BoxC, PlayerR, PlayerC}}, Q2} ->
            if BoxR == TR andalso BoxC == TC ->
                    Pushes;
               true ->
                    VisKey = {BoxR, BoxC, PlayerR, PlayerC},
                    case maps:is_key(VisKey, Vis) of
                        true -> bfs_loop(Q2, Vis, Grid, TR, TC);
                        false ->
                            Vis1 = maps:put(VisKey, true, Vis),
                            PushList = possible_pushes(BoxR, BoxC, PlayerR, PlayerC, Grid),
                            Q3 = lists:foldl(
                                    fun({NB_R, NB_C, NP_R, NP_C}, AccQ) ->
                                            queue:in({Pushes + 1, NB_R, NB_C, NP_R, NP_C}, AccQ)
                                    end,
                                    Q2,
                                    PushList),
                            bfs_loop(Q3, Vis1, Grid, TR, TC)
                    end
            end
    end.

%% --------------------------------------------------------------------
%% Generate possible pushes from current state
possible_pushes(BoxR, BoxC, PlayerR, PlayerC, Grid) ->
    Dirs = [{-1,0}, {1,0}, {0,-1}, {0,1}],
    M = length(Grid),
    N = length(lists:nth(1, Grid)),
    lists:foldl(
        fun({DR, DC}, Acc) ->
            NewBR = BoxR + DR,
            NewBC = BoxC + DC,
            NeedPR = BoxR - DR,
            NeedPC = BoxC - DC,
            case {0 =< NewBR, NewBR < M, 0 =< NewBC, NewBC < N,
                  not is_wall(Grid, NewBR, NewBC),
                  0 =< NeedPR, NeedPR < M, 0 =< NeedPC, NeedPC < N,
                  not is_wall(Grid, NeedPR, NeedPC)} of
                {true, true, true, true, true, true, true, true, true} ->
                    case reachable(PlayerR, PlayerC, NeedPR, NeedPC, Grid, BoxR, BoxC) of
                        true -> [{NewBR, NewBC, BoxR, BoxC} | Acc];
                        false -> Acc
                    end;
                _ -> Acc
            end
        end,
        [],
        Dirs).

%% --------------------------------------------------------------------
%% Check if player can reach target cell without crossing walls or the box
reachable(SR, SC, TR, TC, Grid, BR, BC) ->
    M = length(Grid),
    N = length(lists:nth(1, Grid)),
    Vis0 = maps:new(),
    Q0 = queue:in({SR, SC}, queue:new()),
    reachable_bfs(Q0, Vis0, TR, TC, Grid, BR, BC, M, N).

reachable_bfs(Q, Vis, TR, TC, Grid, BR, BC, M, N) ->
    case queue:out(Q) of
        {empty, _} -> false;
        {{value, {R, C}}, Q2} ->
            if maps:is_key({R, C}, Vis) ->
                    reachable_bfs(Q2, Vis, TR, TC, Grid, BR, BC, M, N);
               true ->
                    if R == TR andalso C == TC -> true;
                       true ->
                            Vis1 = maps:put({R, C}, true, Vis),
                            Dirs = [{-1,0}, {1,0}, {0,-1}, {0,1}],
                            Q3 = lists:foldl(
                                    fun({DR, DC}, AccQ) ->
                                        R2 = R + DR,
                                        C2 = C + DC,
                                        case {0 =< R2, R2 < M, 0 =< C2, C2 < N,
                                              not is_wall(Grid, R2, C2),
                                              not (R2 == BR andalso C2 == BC)} of
                                            {true, true, true, true, true, true} ->
                                                queue:in({R2, C2}, AccQ);
                                            _ -> AccQ
                                        end
                                    end,
                                    Q2,
                                    Dirs),
                            reachable_bfs(Q3, Vis1, TR, TC, Grid, BR, BC, M, N)
                    end
            end
    end.

%% --------------------------------------------------------------------
%% Locate positions of S, B, T
locate(Grid) ->
    locate_rows(Grid, 0, maps:new()).

locate_rows([], _RowIdx, Acc) -> Acc;
locate_rows([Row | Rest], RowIdx, Acc) ->
    Acc1 = locate_cols(Row, RowIdx, 0, Acc),
    locate_rows(Rest, RowIdx + 1, Acc1).

locate_cols([], _R, _C, Acc) -> Acc;
locate_cols([Ch | Rest], R, C, Acc) ->
    NewAcc = case Ch of
        $S -> maps:put(s, {R, C}, Acc);
        $B -> maps:put(b, {R, C}, Acc);
        $T -> maps:put(t, {R, C}, Acc);
        _   -> Acc
    end,
    locate_cols(Rest, R, C + 1, NewAcc).

%% --------------------------------------------------------------------
is_wall(Grid, R, C) ->
    Row = lists:nth(R + 1, Grid),
    Cell = lists:nth(C + 1, Row),
    Cell == $#.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_push_box(grid :: [[char]]) :: integer
  def min_push_box(grid) do
    {sr, sc, br, bc, tr, tc} = find_positions(grid)

    if br == tr and bc == tc do
      0
    else
      m = length(grid)
      n = length(hd(grid))

      start_state = {br, bc, sr, sc}
      visited = MapSet.new([start_state])
      queue = :queue.new() |> :queue.in({0, start_state})

      bfs(queue, visited, grid, m, n, tr, tc)
    end
  end

  defp bfs(queue, visited, grid, m, n, tr, tc) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {pushes, {br, bc, pr, pc}}}, q2} ->
        if br == tr and bc == tc do
          pushes
        else
          dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

          {new_queue, new_visited} =
            Enum.reduce(dirs, {q2, visited}, fn {dr, dc},
                                                {qacc, vacc} ->
              nb_r = br + dr
              nb_c = bc + dc
              need_r = br - dr
              need_c = bc - dc

              cond do
                not in_bounds?(nb_r, nb_c, m, n) or not passable?(grid, nb_r, nb_c) ->
                  {qacc, vacc}

                not in_bounds?(need_r, need_c, m, n) or not passable?(grid, need_r, need_c) ->
                  {qacc, vacc}

                not reachable?(grid, m, n, pr, pc, need_r, need_c, {br, bc}) ->
                  {qacc, vacc}

                true ->
                  new_state = {nb_r, nb_c, br, bc}
                  if MapSet.member?(vacc, new_state) do
                    {qacc, vacc}
                  else
                    {
                      :queue.in({pushes + 1, new_state}, qacc),
                      MapSet.put(vacc, new_state)
                    }
                  end
              end
            end)

          bfs(new_queue, new_visited, grid, m, n, tr, tc)
        end
    end
  end

  defp in_bounds?(r, c, m, n), do: r >= 0 and r < m and c >= 0 and c < n

  defp passable?(grid, r, c) do
    cell = Enum.at(Enum.at(grid, r), c)
    cell != "#"
  end

  defp reachable?(grid, m, n, sr, sc, tr, tc, {br, bc}) do
    if sr == tr and sc == tc do
      true
    else
      visited = MapSet.new()
      q = :queue.new() |> :queue.in({sr, sc})
      bfs_reach(q, visited, grid, m, n, tr, tc, br, bc)
    end
  end

  defp bfs_reach(queue, visited, grid, m, n, target_r, target_c, br, bc) do
    case :queue.out(queue) do
      {:empty, _} ->
        false

      {{:value, {r, c}}, q2} ->
        if r == target_r and c == target_c do
          true
        else
          visited = MapSet.put(visited, {r, c})
          dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

          new_q =
            Enum.reduce(dirs, q2, fn {dr, dc}, acc ->
              nr = r + dr
              nc = c + dc

              cond do
                not in_bounds?(nr, nc, m, n) -> acc
                nr == br and nc == bc -> acc
                not passable?(grid, nr, nc) -> acc
                MapSet.member?(visited, {nr, nc}) -> acc
                true -> :queue.in({nr, nc}, acc)
              end
            end)

          bfs_reach(new_q, visited, grid, m, n, target_r, target_c, br, bc)
        end
    end
  end

  defp find_positions(grid) do
    m = length(grid)
    n = length(hd(grid))

    Enum.reduce(0..(m - 1), {nil, nil, nil, nil, nil, nil}, fn r,
                                                             {sr, sc, br, bc, tr,
                                                              tc} ->
      row = Enum.at(grid, r)

      Enum.reduce(0..(n - 1), {sr, sc, br, bc, tr, tc}, fn c,
                                                          {sr2, sc2, br2, bc2,
                                                           tr2, tc2} ->
        ch = Enum.at(row, c)

        case ch do
          "S" -> {r, c, br2, bc2, tr2, tc2}
          "B" -> {sr2, sc2, r, c, tr2, tc2}
          "T" -> {sr2, sc2, br2, bc2, r, c}
          _ -> {sr2, sc2, br2, bc2, tr2, tc2}
        end
      end)
    end)
  end
end
```

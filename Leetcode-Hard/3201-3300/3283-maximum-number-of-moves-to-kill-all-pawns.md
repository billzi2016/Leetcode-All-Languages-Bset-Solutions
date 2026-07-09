# 3283. Maximum Number of Moves to Kill All Pawns

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxMoves(int kx, int ky, vector<vector<int>>& positions) {
        const int N = 50;
        const int dx[8] = {1,2,2,1,-1,-2,-2,-1};
        const int dy[8] = {2,1,-1,-2,-2,-1,1,2};

        int m = positions.size();
        vector<pair<int,int>> nodes;
        nodes.reserve(m+1);
        nodes.emplace_back(kx, ky); // start at index 0
        for (auto &p: positions) nodes.emplace_back(p[0], p[1]); // pawns indices 1..m

        int total = m + 1;
        vector<vector<int>> dist(total, vector<int>(total, 0));

        // BFS from each node to compute distances to all other nodes
        for (int s = 0; s < total; ++s) {
            vector<vector<int>> d(N, vector<int>(N, -1));
            queue<pair<int,int>> q;
            auto [sx, sy] = nodes[s];
            d[sx][sy] = 0;
            q.emplace(sx, sy);
            while (!q.empty()) {
                auto [x, y] = q.front(); q.pop();
                for (int dir = 0; dir < 8; ++dir) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
                    if (d[nx][ny] == -1) {
                        d[nx][ny] = d[x][y] + 1;
                        q.emplace(nx, ny);
                    }
                }
            }
            for (int t = 0; t < total; ++t) {
                auto [tx, ty] = nodes[t];
                dist[s][t] = d[tx][ty];
            }
        }

        const int MAXMASK = 1 << m;
        static int dp[1<<15][16][2];
        for (int mask = 0; mask < MAXMASK; ++mask)
            for (int pos = 0; pos < total; ++pos)
                dp[mask][pos][0] = dp[mask][pos][1] = -1;

        function<int(int,int,int)> dfs = [&](int posIdx, int mask, int turn) -> int {
            if (mask == 0) return 0;
            int &res = dp[mask][posIdx][turn];
            if (res != -1) return res;
            if (turn == 0) { // Alice wants to maximize
                int best = INT_MIN;
                for (int i = 1; i <= m; ++i) {
                    int bit = 1 << (i-1);
                    if (!(mask & bit)) continue;
                    int d = dist[posIdx][i];
                    int nextTurn = turn ^ (d & 1);
                    int val = d + dfs(i, mask ^ bit, nextTurn);
                    best = max(best, val);
                }
                res = best;
            } else { // Bob wants to minimize
                int best = INT_MAX;
                for (int i = 1; i <= m; ++i) {
                    int bit = 1 << (i-1);
                    if (!(mask & bit)) continue;
                    int d = dist[posIdx][i];
                    int nextTurn = turn ^ (d & 1);
                    int val = d + dfs(i, mask ^ bit, nextTurn);
                    best = min(best, val);
                }
                res = best;
            }
            return res;
        };

        int fullMask = (1 << m) - 1;
        return dfs(0, fullMask, 0);
    }
};
```

## Java

```java
class Solution {
    private static final int BOARD_SIZE = 50;
    private static final int[] DX = {1, 2, 2, 1, -1, -2, -2, -1};
    private static final int[] DY = {2, 1, -1, -2, -2, -1, 1, 2};

    public int maxMoves(int kx, int ky, int[][] positions) {
        int n = positions.length;
        int totalPoints = n + 1; // start + pawns
        int[][] points = new int[totalPoints][2];
        points[0][0] = kx;
        points[0][1] = ky;
        for (int i = 0; i < n; i++) {
            points[i + 1][0] = positions[i][0];
            points[i + 1][1] = positions[i][1];
        }

        int[][] dist = new int[totalPoints][totalPoints];
        // compute pairwise distances using BFS from each point
        for (int i = 0; i < totalPoints; i++) {
            int[][] dAll = bfs(points[i][0], points[i][1]);
            for (int j = 0; j < totalPoints; j++) {
                dist[i][j] = dAll[points[j][0]][points[j][1]];
            }
        }

        int fullMask = (1 << n) - 1;
        int[][] memo = new int[1 << n][totalPoints];
        for (int[] row : memo) java.util.Arrays.fill(row, Integer.MIN_VALUE);
        return dfs(0, 0, n, dist, memo, fullMask);
    }

    private int dfs(int mask, int curIdx, int n, int[][] dist, int[][] memo, int fullMask) {
        if (mask == fullMask) return 0;
        if (memo[mask][curIdx] != Integer.MIN_VALUE) return memo[mask][curIdx];

        boolean aliceTurn = (Integer.bitCount(mask) % 2 == 0);
        int best = aliceTurn ? Integer.MIN_VALUE : Integer.MAX_VALUE;

        for (int p = 0; p < n; p++) {
            if ((mask & (1 << p)) != 0) continue;
            int nextMask = mask | (1 << p);
            int cost = dist[curIdx][p + 1] + dfs(nextMask, p + 1, n, dist, memo, fullMask);
            if (aliceTurn) {
                if (cost > best) best = cost;
            } else {
                if (cost < best) best = cost;
            }
        }

        memo[mask][curIdx] = best;
        return best;
    }

    private int[][] bfs(int sx, int sy) {
        int[][] d = new int[BOARD_SIZE][BOARD_SIZE];
        for (int i = 0; i < BOARD_SIZE; i++) java.util.Arrays.fill(d[i], -1);
        java.util.ArrayDeque<int[]> q = new java.util.ArrayDeque<>();
        d[sx][sy] = 0;
        q.offer(new int[]{sx, sy});
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            int nd = d[x][y] + 1;
            for (int dir = 0; dir < 8; dir++) {
                int nx = x + DX[dir];
                int ny = y + DY[dir];
                if (nx >= 0 && nx < BOARD_SIZE && ny >= 0 && ny < BOARD_SIZE && d[nx][ny] == -1) {
                    d[nx][ny] = nd;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
        return d;
    }
}
```

## Python

```python
class Solution(object):
    def maxMoves(self, kx, ky, positions):
        """
        :type kx: int
        :type ky: int
        :type positions: List[List[int]]
        :rtype: int
        """
        from collections import deque
        m = len(positions)
        nodes = positions + [[kx, ky]]  # last index is start position
        N = m + 1
        moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        # compute pairwise knight distances on 50x50 board
        dist = [[0]*N for _ in range(N)]

        def bfs(sx, sy):
            dgrid = [[-1]*50 for _ in range(50)]
            dq = deque()
            dgrid[sx][sy] = 0
            dq.append((sx, sy))
            while dq:
                x, y = dq.popleft()
                nd = dgrid[x][y] + 1
                for dx, dy in moves:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and dgrid[nx][ny] == -1:
                        dgrid[nx][ny] = nd
                        dq.append((nx, ny))
            return dgrid

        # precompute distance from each node to all board cells
        all_dgrids = [bfs(x, y) for x, y in nodes]

        for i in range(N):
            gi = all_dgrids[i]
            for j in range(N):
                xj, yj = nodes[j]
                dist[i][j] = gi[xj][yj]

        full_mask = (1 << m) - 1
        from functools import lru_cache

        @lru_cache(None)
        def dp(mask, cur):
            if mask == 0:
                return 0
            captured = m - bin(mask).count("1")
            alice_turn = (captured % 2 == 0)  # Alice starts when no captures yet
            if alice_turn:
                best = -10**9
                for nxt in range(m):
                    if mask & (1 << nxt):
                        val = dist[cur][nxt] + dp(mask ^ (1 << nxt), nxt)
                        if val > best:
                            best = val
                return best
            else:
                best = 10**9
                for nxt in range(m):
                    if mask & (1 << nxt):
                        val = dist[cur][nxt] + dp(mask ^ (1 << nxt), nxt)
                        if val < best:
                            best = val
                return best

        start_idx = m  # index of knight's initial position
        return dp(full_mask, start_idx)
```

## Python3

```python
from collections import deque
from functools import lru_cache
from typing import List

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        n = len(positions)
        nodes = [(kx, ky)] + [tuple(p) for p in positions]
        m = n + 1
        # knight moves
        dirs = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        # compute distances between all nodes
        dist = [[0]*m for _ in range(m)]
        board_size = 50

        def bfs(start_idx: int):
            sx, sy = nodes[start_idx]
            dgrid = [[-1]*board_size for _ in range(board_size)]
            q = deque()
            q.append((sx, sy))
            dgrid[sx][sy] = 0
            while q:
                x, y = q.popleft()
                curd = dgrid[x][y]
                # check if this position is one of the nodes
                for idx, (tx, ty) in enumerate(nodes):
                    if dgrid[tx][ty] == curd and dist[start_idx][idx] == 0 and not (start_idx == idx):
                        # will be set later when we finish BFS
                        pass
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < board_size and 0 <= ny < board_size and dgrid[nx][ny] == -1:
                        dgrid[nx][ny] = curd + 1
                        q.append((nx, ny))
            # fill distances from start_idx to all nodes
            for idx, (tx, ty) in enumerate(nodes):
                dist[start_idx][idx] = dgrid[tx][ty]

        for i in range(m):
            bfs(i)

        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int, cur: int, turn: int) -> int:
            if mask == 0:
                return 0
            if turn == 0:  # Alice maximize
                best = -10**9
                mm = mask
                while mm:
                    lsb = mm & -mm
                    j = (lsb.bit_length() - 1)
                    cost = dist[cur][j+1] + dp(mask ^ lsb, j+1, 1)
                    if cost > best:
                        best = cost
                    mm ^= lsb
                return best
            else:  # Bob minimize
                best = 10**9
                mm = mask
                while mm:
                    lsb = mm & -mm
                    j = (lsb.bit_length() - 1)
                    cost = dist[cur][j+1] + dp(mask ^ lsb, j+1, 0)
                    if cost < best:
                        best = cost
                    mm ^= lsb
                return best

        return dp(full_mask, 0, 0)
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int maxMoves(int kx, int ky, int** positions, int positionsSize, int* positionsColSize) {
    const int N = 15;
    const int BOARD = 50;
    int n = positionsSize;
    int xs[N + 1];
    int ys[N + 1];
    for (int i = 0; i < n; ++i) {
        xs[i] = positions[i][0];
        ys[i] = positions[i][1];
    }
    xs[n] = kx;
    ys[n] = ky;

    // knight moves
    int dx[8] = {2, 2, -2, -2, 1, -1, 1, -1};
    int dy[8] = {1, -1, 1, -1, 2, 2, -2, -2};

    // distance matrix
    int dist[N + 1][N + 1];
    for (int i = 0; i <= n; ++i) {
        // BFS from node i
        int dgrid[BOARD][BOARD];
        for (int x = 0; x < BOARD; ++x)
            for (int y = 0; y < BOARD; ++y)
                dgrid[x][y] = -1;
        int qx[BOARD * BOARD];
        int qy[BOARD * BOARD];
        int head = 0, tail = 0;
        int sx = xs[i], sy = ys[i];
        dgrid[sx][sy] = 0;
        qx[tail] = sx; qy[tail] = sy; ++tail;
        while (head < tail) {
            int cx = qx[head];
            int cy = qy[head];
            ++head;
            int cd = dgrid[cx][cy];
            for (int m = 0; m < 8; ++m) {
                int nx = cx + dx[m];
                int ny = cy + dy[m];
                if (nx >= 0 && nx < BOARD && ny >= 0 && ny < BOARD && dgrid[nx][ny] == -1) {
                    dgrid[nx][ny] = cd + 1;
                    qx[tail] = nx; qy[tail] = ny; ++tail;
                }
            }
        }
        for (int j = 0; j <= n; ++j) {
            dist[i][j] = dgrid[xs[j]][ys[j]];
        }
    }

    int fullMask = (1 << n) - 1;
    // dp[mask][i] where i in [0..n] (current position)
    int **dp = (int **)malloc((fullMask + 1) * sizeof(int *));
    for (int mask = 0; mask <= fullMask; ++mask) {
        dp[mask] = (int *)malloc((n + 1) * sizeof(int));
    }

    for (int mask = 0; mask <= fullMask; ++mask) {
        int captured = n - __builtin_popcount(mask);
        int aliceTurn = (captured % 2 == 0); // true if Alice's turn
        for (int i = 0; i <= n; ++i) {
            if (mask == 0) {
                dp[mask][i] = 0;
                continue;
            }
            int best = aliceTurn ? INT_MIN : INT_MAX;
            for (int j = 0; j < n; ++j) {
                if (mask & (1 << j)) {
                    int nd = dist[i][j];
                    int nextMask = mask ^ (1 << j);
                    int val = nd + dp[nextMask][j];
                    if (aliceTurn) {
                        if (val > best) best = val;
                    } else {
                        if (val < best) best = val;
                    }
                }
            }
            dp[mask][i] = best;
        }
    }

    int answer = dp[fullMask][n];

    for (int mask = 0; mask <= fullMask; ++mask) free(dp[mask]);
    free(dp);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private static readonly int[] dx = { 2, 2, 1, 1, -1, -1, -2, -2 };
    private static readonly int[] dy = { 1, -1, 2, -2, 2, -2, 1, -1 };
    private const int BOARD_SIZE = 50;

    public int MaxMoves(int kx, int ky, int[][] positions) {
        int n = positions.Length;
        int totalNodes = n + 1; // last node is the knight start
        int[,] dist = new int[totalNodes, totalNodes];

        // Prepare all points (pawns + start)
        var points = new (int x, int y)[totalNodes];
        for (int i = 0; i < n; i++) {
            points[i] = (positions[i][0], positions[i][1]);
        }
        points[n] = (kx, ky); // start position

        // Compute pairwise knight distances using BFS from each point
        for (int src = 0; src < totalNodes; src++) {
            int[,] dgrid = new int[BOARD_SIZE, BOARD_SIZE];
            for (int i = 0; i < BOARD_SIZE; i++)
                for (int j = 0; j < BOARD_SIZE; j++)
                    dgrid[i, j] = -1;

            var qx = new Queue<int>();
            var qy = new Queue<int>();
            int sx = points[src].x;
            int sy = points[src].y;
            dgrid[sx, sy] = 0;
            qx.Enqueue(sx);
            qy.Enqueue(sy);

            while (qx.Count > 0) {
                int x = qx.Dequeue();
                int y = qy.Dequeue();
                int cur = dgrid[x, y];
                for (int dir = 0; dir < 8; dir++) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (nx >= 0 && nx < BOARD_SIZE && ny >= 0 && ny < BOARD_SIZE && dgrid[nx, ny] == -1) {
                        dgrid[nx, ny] = cur + 1;
                        qx.Enqueue(nx);
                        qy.Enqueue(ny);
                    }
                }
            }

            for (int dst = 0; dst < totalNodes; dst++) {
                dist[src, dst] = dgrid[points[dst].x, points[dst].y];
            }
        }

        int fullMask = (1 << n) - 1;
        // memo[posIdx, mask, turn] where turn: 0 = Alice (max), 1 = Bob (min)
        var memo = new int[totalNodes, 1 << 15, 2];
        for (int i = 0; i < totalNodes; i++)
            for (int m = 0; m < (1 << n); m++)
                memo[i, m, 0] = memo[i, m, 1] = int.MinValue;

        int Solve(int posIdx, int mask, int turn) {
            if (mask == 0) return 0;
            int stored = memo[posIdx, mask, turn];
            if (stored != int.MinValue) return stored;

            if (turn == 0) { // Alice wants to maximize
                int best = int.MinValue;
                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) != 0) {
                        int d = dist[posIdx, i];
                        int val = d + Solve(i, mask ^ (1 << i), 1);
                        if (val > best) best = val;
                    }
                }
                memo[posIdx, mask, turn] = best;
            } else { // Bob wants to minimize
                int best = int.MaxValue;
                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) != 0) {
                        int d = dist[posIdx, i];
                        int val = d + Solve(i, mask ^ (1 << i), 0);
                        if (val < best) best = val;
                    }
                }
                memo[posIdx, mask, turn] = best;
            }
            return memo[posIdx, mask, turn];
        }

        return Solve(n, fullMask, 0);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} kx
 * @param {number} ky
 * @param {number[][]} positions
 * @return {number}
 */
var maxMoves = function(kx, ky, positions) {
    const m = positions.length;
    const nodes = positions.concat([[kx, ky]]); // last is start
    const N = m + 1;
    const boardSize = 50;
    const dirs = [
        [2, 1], [2, -1], [-2, 1], [-2, -1],
        [1, 2], [1, -2], [-1, 2], [-1, -2]
    ];
    
    // compute distances between all nodes
    const dist = Array.from({length: N}, () => new Array(N).fill(0));
    
    function bfs(sx, sy) {
        const dgrid = Array.from({length: boardSize}, () => new Int16Array(boardSize).fill(-1));
        const qx = new Int16Array(boardSize * boardSize);
        const qy = new Int16Array(boardSize * boardSize);
        let head = 0, tail = 0;
        dgrid[sx][sy] = 0;
        qx[tail] = sx; qy[tail] = sy; tail++;
        while (head < tail) {
            const x = qx[head];
            const y = qy[head];
            head++;
            const curd = dgrid[x][y];
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx >= 0 && nx < boardSize && ny >= 0 && ny < boardSize && dgrid[nx][ny] === -1) {
                    dgrid[nx][ny] = curd + 1;
                    qx[tail] = nx; qy[tail] = ny; tail++;
                }
            }
        }
        return dgrid;
    }
    
    const allDists = nodes.map(([x, y]) => bfs(x, y));
    for (let i = 0; i < N; ++i) {
        for (let j = 0; j < N; ++j) {
            const [tx, ty] = nodes[j];
            dist[i][j] = allDists[i][tx][ty];
        }
    }
    
    const fullMask = (1 << m) - 1;
    const dp = new Array(1 << m);
    for (let mask = 0; mask < (1 << m); ++mask) {
        dp[mask] = new Array(N);
        for (let i = 0; i < N; ++i) {
            dp[mask][i] = [null, null]; // [AliceTurn, BobTurn]
        }
    }
    
    function solve(mask, posIdx, turn) { // turn: 0 Alice (max), 1 Bob (min)
        if (mask === 0) return 0;
        const memo = dp[mask][posIdx][turn];
        if (memo !== null) return memo;
        let best = turn === 0 ? -Infinity : Infinity;
        for (let j = 0; j < m; ++j) {
            if ((mask & (1 << j)) === 0) continue;
            const d = dist[posIdx][j];
            const nextMask = mask ^ (1 << j);
            const nextTurn = (turn + d) & 1;
            const val = d + solve(nextMask, j, nextTurn);
            if (turn === 0) {
                if (val > best) best = val;
            } else {
                if (val < best) best = val;
            }
        }
        dp[mask][posIdx][turn] = best;
        return best;
    }
    
    // start from start node index m, Alice's turn
    return solve(fullMask, m, 0);
};
```

## Typescript

```typescript
function maxMoves(kx: number, ky: number, positions: number[][]): number {
    const dirs = [
        [2, 1], [2, -1], [-2, 1], [-2, -1],
        [1, 2], [1, -2], [-1, 2], [-1, -2]
    ];
    const n = positions.length;
    const allPoints = [[kx, ky], ...positions];
    const m = n + 1;

    // Precompute minimum knight moves between all relevant points using BFS
    const dist: number[][] = Array.from({ length: m }, () => Array(m).fill(Infinity));

    function bfs(startIdx: number) {
        const [sx, sy] = allPoints[startIdx];
        const dgrid: number[][] = Array.from({ length: 50 }, () => Array(50).fill(-1));
        const qx: number[] = [];
        const qy: number[] = [];
        let head = 0;
        dgrid[sx][sy] = 0;
        qx.push(sx);
        qy.push(sy);
        while (head < qx.length) {
            const x = qx[head];
            const y = qy[head];
            head++;
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx >= 0 && nx < 50 && ny >= 0 && ny < 50 && dgrid[nx][ny] === -1) {
                    dgrid[nx][ny] = dgrid[x][y] + 1;
                    qx.push(nx);
                    qy.push(ny);
                }
            }
        }
        for (let j = 0; j < m; ++j) {
            const [tx, ty] = allPoints[j];
            dist[startIdx][j] = dgrid[tx][ty];
        }
    }

    for (let i = 0; i < m; ++i) bfs(i);

    // DP over subsets with turn parity.
    // dp[mask][i][p] = max total moves from state where remaining pawns are represented by mask,
    // knight is at point i, and p = 0 if it's Alice's turn, 1 if Bob's turn.
    const size = 1 << n;
    const INF_NEG = -1e9;
    const dp: number[][][] = Array.from({ length: size }, () =>
        Array.from({ length: m }, () => [INF_NEG, INF_NEG])
    );

    // Base case: no remaining pawns -> 0 moves regardless of turn
    for (let i = 0; i < m; ++i) {
        dp[0][i][0] = dp[0][i][1] = 0;
    }

    // Helper to get parity after moving d steps starting with player p
    const nextParity = (p: number, d: number): number => (p ^ (d & 1));

    for (let mask = 1; mask < size; ++mask) {
        for (let i = 0; i < m; ++i) {
            // Alice's turn
            let bestA = INF_NEG;
            // Bob's turn
            let bestB = INF_NEG;

            for (let pj = 0; pj < n; ++pj) {
                if ((mask & (1 << pj)) === 0) continue;
                const jIdx = pj + 1; // index in allPoints
                const d = dist[i][jIdx];
                if (d === Infinity) continue;

                const nextMask = mask ^ (1 << pj);
                const parityAfter = nextParity(0, d); // starting with Alice

                // After reaching pawn j, the turn becomes parityAfter
                const totalA = d + dp[nextMask][jIdx][parityAfter];
                if (totalA > bestA) bestA = totalA;

                // Starting with Bob
                const parityAfterB = nextParity(1, d);
                const totalB = d + dp[nextMask][jIdx][parityAfterB];
                if (bestB === INF_NEG || totalB < bestB) bestB = totalB;
            }

            dp[mask][i][0] = bestA;
            dp[mask][i][1] = bestB;
        }
    }

    // Initial state: all pawns present, knight at start index 0, Alice's turn (0)
    return dp[size - 1][0][0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $kx
     * @param Integer $ky
     * @param Integer[][] $positions
     * @return Integer
     */
    function maxMoves($kx, $ky, $positions) {
        $n = count($positions);
        $points = $positions;
        $points[] = [$kx, $ky]; // start position as last index

        $size = $n + 1;
        $dist = array_fill(0, $size, array_fill(0, $size, 0));

        $dirs = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]];
        $boardSize = 50;

        for ($s = 0; $s < $size; $s++) {
            $queue = new SplQueue();
            $visited = array_fill(0, $boardSize, array_fill(0, $boardSize, -1));
            [$sx, $sy] = $points[$s];
            $visited[$sx][$sy] = 0;
            $queue->enqueue([$sx, $sy]);

            while (!$queue->isEmpty()) {
                [$x, $y] = $queue->dequeue();
                $d = $visited[$x][$y];
                foreach ($dirs as $dir) {
                    $nx = $x + $dir[0];
                    $ny = $y + $dir[1];
                    if ($nx >= 0 && $nx < $boardSize && $ny >= 0 && $ny < $boardSize && $visited[$nx][$ny] == -1) {
                        $visited[$nx][$ny] = $d + 1;
                        $queue->enqueue([$nx, $ny]);
                    }
                }
            }

            for ($t = 0; $t < $size; $t++) {
                [$tx, $ty] = $points[$t];
                $dist[$s][$t] = $visited[$tx][$ty];
            }
        }

        $fullMask = (1 << $n) - 1;
        $INF = 1e9;
        $memo = [];

        $dfs = function($mask, $posIdx, $turn) use (&$dfs, &$memo, $dist, $n, $fullMask, $INF) {
            if ($mask == $fullMask) return 0;
            $key = $mask . '|' . $posIdx . '|' . $turn;
            if (isset($memo[$key])) return $memo[$key];

            if ($turn == 0) { // Alice maximizes
                $best = -$INF;
                for ($i = 0; $i < $n; $i++) {
                    if ((($mask >> $i) & 1) == 0) {
                        $cost = $dist[$posIdx][$i];
                        $val = $cost + $dfs($mask | (1 << $i), $i, 1);
                        if ($val > $best) $best = $val;
                    }
                }
            } else { // Bob minimizes
                $best = $INF;
                for ($i = 0; $i < $n; $i++) {
                    if ((($mask >> $i) & 1) == 0) {
                        $cost = $dist[$posIdx][$i];
                        $val = $cost + $dfs($mask | (1 << $i), $i, 0);
                        if ($val < $best) $best = $val;
                    }
                }
            }

            $memo[$key] = $best;
            return $best;
        };

        return $dfs(0, $n, 0); // start from initial position with Alice's turn
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func maxMoves(_ kx: Int, _ ky: Int, _ positions: [[Int]]) -> Int {
        let n = positions.count
        var nodes: [(Int, Int)] = []
        nodes.append((kx, ky)) // start position at index 0
        for p in positions {
            nodes.append((p[0], p[1]))
        }
        let totalNodes = n + 1
        // Precompute knight distances between all nodes using BFS
        var distMat = Array(repeating: Array(repeating: 0, count: totalNodes), count: totalNodes)
        let boardSize = 50
        let moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        
        func bfs(_ sx: Int, _ sy: Int) -> [[Int]] {
            var dist = Array(repeating: Array(repeating: -1, count: boardSize), count: boardSize)
            var qx = [Int](), qy = [Int]()
            var head = 0
            dist[sx][sy] = 0
            qx.append(sx); qy.append(sy)
            while head < qx.count {
                let x = qx[head]
                let y = qy[head]
                head += 1
                let d = dist[x][y]
                for (dx, dy) in moves {
                    let nx = x + dx
                    let ny = y + dy
                    if nx >= 0 && nx < boardSize && ny >= 0 && ny < boardSize && dist[nx][ny] == -1 {
                        dist[nx][ny] = d + 1
                        qx.append(nx)
                        qy.append(ny)
                    }
                }
            }
            return dist
        }
        
        for i in 0..<totalNodes {
            let (sx, sy) = nodes[i]
            let dgrid = bfs(sx, sy)
            for j in 0..<totalNodes {
                let (tx, ty) = nodes[j]
                distMat[i][j] = dgrid[tx][ty]
            }
        }
        
        let maxMask = 1 << n
        var memoAlice = Array(repeating: Array(repeating: -1, count: maxMask), count: totalNodes)
        var memoBob   = Array(repeating: Array(repeating: -1, count: maxMask), count: totalNodes)
        
        func dfs(_ pos: Int, _ mask: Int, _ turn: Int) -> Int {
            if mask == 0 { return 0 }
            if turn == 0 {
                if memoAlice[pos][mask] != -1 { return memoAlice[pos][mask] }
            } else {
                if memoBob[pos][mask] != -1 { return memoBob[pos][mask] }
            }
            var best = (turn == 0) ? Int.min : Int.max
            var m = mask
            var i = 0
            while m > 0 {
                if (m & 1) == 1 {
                    let d = distMat[pos][i + 1] // pawn i corresponds to node i+1
                    let nextTurn = (turn + d) % 2
                    let val = d + dfs(i + 1, mask ^ (1 << i), nextTurn)
                    if turn == 0 {
                        if val > best { best = val }
                    } else {
                        if val < best { best = val }
                    }
                }
                i += 1
                m >>= 1
            }
            if turn == 0 {
                memoAlice[pos][mask] = best
            } else {
                memoBob[pos][mask] = best
            }
            return best
        }
        
        let fullMask = (1 << n) - 1
        return dfs(0, fullMask, 0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val dirs = arrayOf(
        intArrayOf(2, 1), intArrayOf(2, -1), intArrayOf(-2, 1), intArrayOf(-2, -1),
        intArrayOf(1, 2), intArrayOf(1, -2), intArrayOf(-1, 2), intArrayOf(-1, -2)
    )
    private lateinit var dist: Array<IntArray>
    private lateinit var memo: Array<IntArray>
    private lateinit var seen: Array<BooleanArray>
    private var n = 0

    fun maxMoves(kx: Int, ky: Int, positions: Array<IntArray>): Int {
        n = positions.size
        val points = Array(n + 1) { Pair(0, 0) }
        points[0] = Pair(kx, ky)
        for (i in 0 until n) {
            points[i + 1] = Pair(positions[i][0], positions[i][1])
        }

        // compute pairwise distances
        dist = Array(n + 1) { IntArray(n + 1) }
        for (i in 0..n) {
            val dBoard = bfs(points[i].first, points[i].second)
            for (j in 0..n) {
                dist[i][j] = dBoard[points[j].first][points[j].second]
            }
        }

        val fullMask = if (n == 0) 0 else (1 shl n) - 1
        memo = Array(1 shl n) { IntArray(n + 1) }
        seen = Array(1 shl n) { BooleanArray(n + 1) }
        return dfs(fullMask, 0)
    }

    private fun bfs(sx: Int, sy: Int): Array<IntArray> {
        val boardSize = 50
        val d = Array(boardSize) { IntArray(boardSize) { -1 } }
        val qx = IntArray(boardSize * boardSize)
        val qy = IntArray(boardSize * boardSize)
        var head = 0
        var tail = 0
        d[sx][sy] = 0
        qx[tail] = sx
        qy[tail] = sy
        tail++
        while (head < tail) {
            val x = qx[head]
            val y = qy[head]
            head++
            val curDist = d[x][y]
            for (dir in dirs) {
                val nx = x + dir[0]
                val ny = y + dir[1]
                if (nx in 0 until boardSize && ny in 0 until boardSize && d[nx][ny] == -1) {
                    d[nx][ny] = curDist + 1
                    qx[tail] = nx
                    qy[tail] = ny
                    tail++
                }
            }
        }
        return d
    }

    private fun isAliceTurn(mask: Int): Boolean {
        val captured = n - Integer.bitCount(mask)
        return captured % 2 == 0
    }

    private fun dfs(mask: Int, cur: Int): Int {
        if (mask == 0) return 0
        if (seen[mask][cur]) return memo[mask][cur]
        seen[mask][cur] = true

        var best: Int
        val aliceTurn = isAliceTurn(mask)
        best = if (aliceTurn) Int.MIN_VALUE else Int.MAX_VALUE

        for (i in 0 until n) {
            if ((mask and (1 shl i)) != 0) {
                val d = dist[cur][i + 1]
                // distance should always be reachable
                val next = dfs(mask xor (1 shl i), i + 1)
                val total = d + next
                if (aliceTurn) {
                    if (total > best) best = total
                } else {
                    if (total < best) best = total
                }
            }
        }

        memo[mask][cur] = best
        return best
    }
}
```

## Dart

```dart
class Solution {
  static const int _boardSize = 50;
  static const List<List<int>> _dirs = [
    [2, 1],
    [1, 2],
    [-1, 2],
    [-2, 1],
    [-2, -1],
    [-1, -2],
    [1, -2],
    [2, -1]
  ];

  int maxMoves(int kx, int ky, List<List<int>> positions) {
    final n = positions.length;
    // points: pawns + start position at index n
    final List<List<int>> pts = List.from(positions);
    pts.add([kx, ky]);

    // distance matrix (n+1) x (n+1)
    final List<List<int>> dist = List.generate(
        n + 1, (_) => List.filled(n + 1, 0));

    for (int i = 0; i <= n; ++i) {
      final dgrid = _bfs(pts[i][0], pts[i][1]);
      for (int j = 0; j <= n; ++j) {
        dist[i][j] = dgrid[pts[j][0]][pts[j][1]];
      }
    }

    final int fullMask = (1 << n) - 1;
    // dp[mask][last] -> result, nullable
    final List<List<int?>> memo =
        List.generate(1 << n, (_) => List.filled(n + 1, null));

    int popCount(int x) {
      int cnt = 0;
      while (x != 0) {
        x &= x - 1;
        cnt++;
      }
      return cnt;
    }

    int dfs(int mask, int last) {
      if (mask == 0) return 0;
      final cached = memo[mask][last];
      if (cached != null) return cached;

      final captured = n - popCount(mask);
      final bool aliceTurn = captured % 2 == 0; // Alice starts

      int best = aliceTurn ? -1 : 1 << 30;

      for (int i = 0; i < n; ++i) {
        if ((mask & (1 << i)) != 0) {
          final d = dist[last][i];
          final next = dfs(mask ^ (1 << i), i);
          final total = d + next;
          if (aliceTurn) {
            if (total > best) best = total;
          } else {
            if (total < best) best = total;
          }
        }
      }

      memo[mask][last] = best;
      return best;
    }

    // start from fullMask, last index is n (the knight's initial position)
    return dfs(fullMask, n);
  }

  List<List<int>> _bfs(int sx, int sy) {
    final List<List<int>> dist = List.generate(
        _boardSize, (_) => List.filled(_boardSize, -1));
    final List<int> qx = [];
    final List<int> qy = [];
    int head = 0;
    qx.add(sx);
    qy.add(sy);
    dist[sx][sy] = 0;

    while (head < qx.length) {
      final x = qx[head];
      final y = qy[head];
      head++;
      final curD = dist[x][y];
      for (final dir in _dirs) {
        final nx = x + dir[0];
        final ny = y + dir[1];
        if (nx >= 0 &&
            nx < _boardSize &&
            ny >= 0 &&
            ny < _boardSize &&
            dist[nx][ny] == -1) {
          dist[nx][ny] = curD + 1;
          qx.add(nx);
          qy.add(ny);
        }
      }
    }
    return dist;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"math/bits"
)

func maxMoves(kx int, ky int, positions [][]int) int {
	n := len(positions)
	// nodes: 0..n-1 are pawns, n is the knight start
	nodes := make([][2]int, n+1)
	for i := 0; i < n; i++ {
		nodes[i][0] = positions[i][0]
		nodes[i][1] = positions[i][1]
	}
	nodes[n][0] = kx
	nodes[n][1] = ky

	const boardSize = 50
	dirX := []int{2, 2, -2, -2, 1, 1, -1, -1}
	dirY := []int{1, -1, 1, -1, 2, -2, 2, -2}

	// distance matrix
	dist := make([][]int, n+1)
	for i := range dist {
		dist[i] = make([]int, n+1)
	}
	// BFS from each node
	for idx := 0; idx <= n; idx++ {
		startX, startY := nodes[idx][0], nodes[idx][1]
		boardDist := [boardSize][boardSize]int{}
		for i := 0; i < boardSize; i++ {
			for j := 0; j < boardSize; j++ {
				boardDist[i][j] = -1
			}
		}
		qx := make([]int, 0, boardSize*boardSize)
		qy := make([]int, 0, boardSize*boardSize)
		boardDist[startX][startY] = 0
		qx = append(qx, startX)
		qy = append(qy, startY)
		for head := 0; head < len(qx); head++ {
			x, y := qx[head], qy[head]
			d := boardDist[x][y]
			for k := 0; k < 8; k++ {
				nx, ny := x+dirX[k], y+dirY[k]
				if nx >= 0 && nx < boardSize && ny >= 0 && ny < boardSize && boardDist[nx][ny] == -1 {
					boardDist[nx][ny] = d + 1
					qx = append(qx, nx)
					qy = append(qy, ny)
				}
			}
		}
		for j := 0; j <= n; j++ {
			dist[idx][j] = boardDist[nodes[j][0]][nodes[j][1]]
		}
	}

	fullMask := (1 << n) - 1
	memo := make([][]int, 1<<n)
	for i := range memo {
		memo[i] = make([]int, n+1)
		for j := range memo[i] {
			memo[i][j] = math.MinInt32 // sentinel for uncomputed
		}
	}

	var dfs func(mask int, cur int) int
	dfs = func(mask int, cur int) int {
		if mask == 0 {
			return 0
		}
		if memo[mask][cur] != math.MinInt32 {
			return memo[mask][cur]
		}
		captured := n - bits.OnesCount(uint(mask))
		turnAlice := captured%2 == 0 // Alice moves on even number of captures done
		var best int
		if turnAlice {
			best = math.MinInt32
		} else {
			best = math.MaxInt32
		}
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				cost := dist[cur][i]
				val := cost + dfs(mask^(1<<i), i)
				if turnAlice {
					if val > best {
						best = val
					}
				} else {
					if val < best {
						best = val
					}
				}
			}
		}
		memo[mask][cur] = best
		return best
	}

	return dfs(fullMask, n)
}
```

## Ruby

```ruby
def knight_distances(nodes)
  dirs = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
  n = nodes.size
  dist_mat = Array.new(n) { Array.new(n, 0) }
  n.times do |i|
    sx, sy = nodes[i]
    grid = Array.new(50) { Array.new(50, -1) }
    qx = [sx]
    qy = [sy]
    grid[sx][sy] = 0
    head = 0
    while head < qx.size
      x = qx[head]
      y = qy[head]
      d = grid[x][y]
      dirs.each do |dx, dy|
        nx = x + dx
        ny = y + dy
        if nx.between?(0, 49) && ny.between?(0, 49) && grid[nx][ny] == -1
          grid[nx][ny] = d + 1
          qx << nx
          qy << ny
        end
      end
      head += 1
    end
    n.times do |j|
      tx, ty = nodes[j]
      dist_mat[i][j] = grid[tx][ty]
    end
  end
  dist_mat
end

def max_moves(kx, ky, positions)
  n = positions.length
  nodes = positions.map { |p| [p[0], p[1]] } + [[kx, ky]]
  dist = knight_distances(nodes)

  full_mask = (1 << n) - 1
  dp = Array.new(1 << n) { Array.new(n + 1) }
  turn_parity = Array.new(1 << n, 0)
  (0...(1 << n)).each do |mask|
    turn_parity[mask] = mask.to_s(2).count('1') % 2
  end

  dfs = nil
  dfs = lambda do |mask, last|
    return 0 if mask == full_mask
    memo = dp[mask][last]
    return memo unless memo.nil?
    turn = turn_parity[mask] # 0 -> Alice (max), 1 -> Bob (min)
    best = nil
    n.times do |next_idx|
      bit = 1 << next_idx
      next if (mask & bit) != 0
      val = dist[last][next_idx] + dfs.call(mask | bit, next_idx)
      if turn == 0
        best = best.nil? ? val : [best, val].max
      else
        best = best.nil? ? val : [best, val].min
      end
    end
    dp[mask][last] = best
    best
  end

  dfs.call(0, n)
end
```

## Scala

```scala
object Solution {
  def maxMoves(kx: Int, ky: Int, positions: Array[Array[Int]]): Int = {
    val n = positions.length
    val totalMask = 1 << n
    val dirs = Array((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

    // coordinates of start and pawns
    val xs = new Array[Int](n + 1)
    val ys = new Array[Int](n + 1)
    xs(0) = kx
    ys(0) = ky
    for (i <- 0 until n) {
      xs(i + 1) = positions(i)(0)
      ys(i + 1) = positions(i)(1)
    }

    // BFS to compute distances from a given start
    def bfs(sx: Int, sy: Int): Array[Array[Int]] = {
      val dist = Array.fill(50)(Array.fill(50)(-1))
      val q = scala.collection.mutable.Queue[(Int, Int)]()
      dist(sx)(sy) = 0
      q.enqueue((sx, sy))
      while (q.nonEmpty) {
        val (x, y) = q.dequeue()
        val d = dist(x)(y)
        var idx = 0
        while (idx < 8) {
          val nx = x + dirs(idx)._1
          val ny = y + dirs(idx)._2
          if (nx >= 0 && nx < 50 && ny >= 0 && ny < 50 && dist(nx)(ny) == -1) {
            dist(nx)(ny) = d + 1
            q.enqueue((nx, ny))
          }
          idx += 1
        }
      }
      dist
    }

    // distance matrix between all nodes (start + pawns)
    val dist = Array.ofDim[Int](n + 1, n + 1)
    for (i <- 0 to n) {
      val dgrid = bfs(xs(i), ys(i))
      var j = 0
      while (j <= n) {
        dist(i)(j) = dgrid(xs(j))(ys(j))
        j += 1
      }
    }

    // memoization dp[mask][cur]
    val dp = Array.fill(totalMask, n + 1)(-1)

    def dfs(mask: Int, cur: Int): Int = {
      if (mask == 0) return 0
      if (dp(mask)(cur) != -1) return dp(mask)(cur)
      val captured = n - Integer.bitCount(mask)
      val aliceTurn = (captured % 2) == 0
      var best = if (aliceTurn) Int.MinValue else Int.MaxValue
      var j = 0
      while (j < n) {
        if ((mask & (1 << j)) != 0) {
          val nextMask = mask ^ (1 << j)
          val cost = dist(cur)(j + 1)
          val value = cost + dfs(nextMask, j + 1)
          if (aliceTurn) {
            if (value > best) best = value
          } else {
            if (value < best) best = value
          }
        }
        j += 1
      }
      dp(mask)(cur) = best
      best
    }

    dfs(totalMask - 1, 0)
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn max_moves(kx: i32, ky: i32, positions: Vec<Vec<i32>>) -> i32 {
        const N: usize = 50;
        let n = positions.len();
        // convert positions to (usize, usize)
        let mut pts: Vec<(usize, usize)> = positions
            .into_iter()
            .map(|p| (p[0] as usize, p[1] as usize))
            .collect();
        pts.push((kx as usize, ky as usize)); // start at index n

        // precompute distances between all points using BFS
        let mut dist = vec![vec![0i32; n + 1]; n + 1];
        for i in 0..=n {
            let (sx, sy) = pts[i];
            let bfs_dist = Self::bfs(sx, sy);
            for j in 0..=n {
                let (tx, ty) = pts[j];
                dist[i][j] = bfs_dist[tx * N + ty];
            }
        }

        // DP memo: mask -> current position index -> best total moves from this state
        let max_mask = 1usize << n;
        let mut memo = vec![vec![-1i32; n + 1]; max_mask];

        fn dfs(
            mask: usize,
            cur: usize,
            total: usize,
            dist: &Vec<Vec<i32>>,
            memo: &mut Vec<Vec<i32>>,
        ) -> i32 {
            if mask == 0 {
                return 0;
            }
            let cached = memo[mask][cur];
            if cached != -1 {
                return cached;
            }
            // determine whose turn it is
            let taken = total - mask.count_ones() as usize; // number already captured
            let alice_turn = taken % 2 == 0;

            let mut best: i32 = if alice_turn { i32::MIN } else { i32::MAX };
            let mut m = mask;
            while m != 0 {
                let lsb = m & (!m + 1);
                let idx = lsb.trailing_zeros() as usize; // pawn index
                let next_mask = mask ^ (1usize << idx);
                let cost = dist[cur][idx] + dfs(next_mask, idx, total, dist, memo);
                if alice_turn {
                    if cost > best {
                        best = cost;
                    }
                } else {
                    if cost < best {
                        best = cost;
                    }
                }
                m ^= lsb;
            }
            memo[mask][cur] = best;
            best
        }

        let full_mask = (1usize << n) - 1;
        dfs(full_mask, n, n, &dist, &mut memo)
    }

    fn bfs(sx: usize, sy: usize) -> Vec<i32> {
        const N: usize = 50;
        const DIRS: [(i32, i32); 8] = [
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
        ];
        let mut dist = vec![-1i32; N * N];
        let start_idx = sx * N + sy;
        dist[start_idx] = 0;
        let mut q = VecDeque::new();
        q.push_back((sx as i32, sy as i32));
        while let Some((x, y)) = q.pop_front() {
            let cur_d = dist[(x as usize) * N + (y as usize)];
            for &(dx, dy) in DIRS.iter() {
                let nx = x + dx;
                let ny = y + dy;
                if nx >= 0 && nx < N as i32 && ny >= 0 && ny < N as i32 {
                    let idx = nx as usize * N + ny as usize;
                    if dist[idx] == -1 {
                        dist[idx] = cur_d + 1;
                        q.push_back((nx, ny));
                    }
                }
            }
        }
        dist
    }
}
```

## Racket

```racket
(define/contract (max-moves kx ky positions)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((board-size 50)
         (knight-moves '((2 1) (2 -1) (-2 1) (-2 -1) (1 2) (1 -2) (-1 2) (-1 -2)))
         (n (length positions))
         (points (append positions (list (list kx ky)))) ; last is start
         (total-mask (sub1 (arithmetic-shift 1 n)))      ; (1<<n)-1

         ;; BFS from a source cell, returns vector of distances for all cells (-1 if unreachable)
         (define (bfs-dist sx sy)
           (let* ((size (* board-size board-size))
                  (dist (make-vector size -1))
                  (qx (make-vector size 0))
                  (qy (make-vector size 0))
                  (head 0)
                  (tail 0)
                  (start-idx (+ (* sx board-size) sy)))
             (vector-set! dist start-idx 0)
             (vector-set! qx tail sx)
             (vector-set! qy tail sy)
             (set! tail (+ tail 1))
             (let loop ()
               (when (< head tail)
                 (define x (vector-ref qx head))
                 (define y (vector-ref qy head))
                 (define d (vector-ref dist (+ (* x board-size) y)))
                 (for ([mv knight-moves])
                   (define nx (+ x (first mv)))
                   (define ny (+ y (second mv)))
                   (when (and (>= nx 0) (< nx board-size)
                              (>= ny 0) (< ny board-size))
                     (define nidx (+ (* nx board-size) ny))
                     (when (= (vector-ref dist nidx) -1)
                       (vector-set! dist nidx (+ d 1))
                       (vector-set! qx tail nx)
                       (vector-set! qy tail ny)
                       (set! tail (+ tail 1)))))
                 (set! head (+ head 1))
                 (loop)))
             dist))

         ;; distance matrix between all points (including start)
         (dist-matrix
          (let ((mat (make-vector (+ n 1) #f)))
            (for ([i (in-range (+ n 1))])
              (define src (list-ref points i))
              (define sx (first src))
              (define sy (second src))
              (define dvec (bfs-dist sx sy))
              (define row (make-vector (+ n 1) 0))
              (for ([j (in-range (+ n 1))])
                (define dst (list-ref points j))
                (define tx (first dst))
                (define ty (second dst))
                (define idx (+ (* tx board-size) ty))
                (vector-set! row j (vector-ref dvec idx)))
              (vector-set! mat i row))
            mat))

         ;; DP memo table: dp[mask][cur] = optimal total moves from this state
         (dp-table
          (let ((outer (make-vector (arithmetic-shift 1 n) #f)))
            (for ([mask (in-range (arithmetic-shift 1 n))])
              (vector-set! outer mask (make-vector (+ n 1) #f)))
            outer))

         ;; popcount of an integer
         (define (popcount x)
           (let loop ((cnt 0) (y x))
             (if (= y 0)
                 cnt
                 (loop (+ cnt (bitwise-and y 1)) (arithmetic-shift y -1)))))

         ;; whose turn: #t for Alice (maximizer), #f for Bob (minimizer)
         (define (alice-turn? mask)
           (let ((captured (- n (popcount mask))))
             (= (modulo captured 2) 0))) ; even number captured => Alice's turn

         ;; recursive solver with memoization
         (define (solve mask cur)
           (if (= mask 0)
               0
               (let* ((inner (vector-ref dp-table mask))
                      (cached (vector-ref inner cur)))
                 (if cached
                     cached
                     (let ((alice? (alice-turn? mask))
                           (best #f))
                       (for ([i (in-range n)])
                         (when (not (= 0 (bitwise-and mask (arithmetic-shift 1 i))))
                           (define new-mask (bitwise-and mask (bitwise-not (arithmetic-shift 1 i))))
                           (define d (vector-ref (vector-ref dist-matrix cur) i))
                           (define val (+ d (solve new-mask i)))
                           (cond
                             [alice?
                              (when (or (not best) (> val best)) (set! best val))]
                             [else
                              (when (or (not best) (< val best)) (set! best val))])))
                       (vector-set! inner cur best)
                       best))))))

    ;; start from the knight's initial position (last index)
    (solve total-mask n)))
```

## Erlang

```erlang
-spec max_moves(Kx :: integer(), Ky :: integer(), Positions :: [[integer()]]) -> integer().
max_moves(Kx, Ky, Positions) ->
    Points = [{Kx, Ky} | [ {X, Y} || [X, Y] <- Positions ]],
    DistMat = build_dist_matrix(Points),
    NumPawns = length(Positions),
    FullMask = (1 bsl NumPawns) - 1,
    {Ans, _} = dp(FullMask, 0, 0, DistMat, NumPawns, #{}),
    Ans.

build_dist_matrix(Points) ->
    [ begin
          {X, Y} = Pt,
          DistMap = bfs_dist(X, Y),
          [ maps:get({Px, Py}, DistMap) || {Px, Py} <- Points ]
      end || Pt <- Points ].

bfs_dist(Sx, Sy) ->
    bfs([{Sx, Sy}], #{ {Sx, Sy} => 0 }).

bfs([], Dist) -> Dist;
bfs([{X, Y} | Rest], Dist) ->
    D = maps:get({X, Y}, Dist),
    Moves = [{2,1},{1,2},{-1,2},{-2,1},{-2,-1},{-1,-2},{1,-2},{2,-1}],
    Nexts = [ {Nx, Ny} ||
                {Dx, Dy} <- Moves,
                Nx = X + Dx,
                Ny = Y + Dy,
                0 =< Nx, Nx < 50,
                0 =< Ny, Ny < 50,
                not maps:is_key({Nx, Ny}, Dist) ],
    NewDist = lists:foldl(fun(Pos, Acc) -> maps:put(Pos, D + 1, Acc) end, Dist, Nexts),
    bfs(Rest ++ Nexts, NewDist).

dist(DistMat, I, J) ->
    Row = lists:nth(I + 1, DistMat),
    lists:nth(J + 1, Row).

dp(0, _PosIdx, _Turn, _DistMat, _NumPawns, Memo) -> {0, Memo};
dp(Mask, PosIdx, Turn, DistMat, NumPawns, Memo) ->
    Key = {Mask, PosIdx, Turn},
    case maps:find(Key, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            Candidates = [I || I <- lists:seq(0, NumPawns - 1), (Mask band (1 bsl I)) =/= 0],
            {Best, FinalMemo} = lists:foldl(
                fun(I, {CurBest, CurMemo}) ->
                    D = dist(DistMat, PosIdx, I + 1),
                    NewMask = Mask band bnot (1 bsl I),
                    NextTurn = (Turn + D) band 1,
                    {SubVal, Memo2} = dp(NewMask, I + 1, NextTurn, DistMat, NumPawns, CurMemo),
                    Total = D + SubVal,
                    case Turn of
                        0 -> % Alice maximizes
                            if CurBest == undefined orelse Total > CurBest ->
                                    {Total, Memo2};
                               true -> {CurBest, Memo2}
                            end;
                        1 -> % Bob minimizes
                            if CurBest == undefined orelse Total < CurBest ->
                                    {Total, Memo2};
                               true -> {CurBest, Memo2}
                            end
                    end
                end,
                {undefined, Memo},
                Candidates),
            NewMemo = maps:put(Key, Best, FinalMemo),
            {Best, NewMemo}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_moves(kx :: integer, ky :: integer, positions :: [[integer]]) :: integer
  def max_moves(kx, ky, positions) do
    import Bitwise

    nodes = [{kx, ky} | Enum.map(positions, fn [x, y] -> {x, y} end)]
    total = length(nodes)
    moves = [{2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}]

    dist =
      for i <- 0..(total - 1) do
        {sx, sy} = Enum.at(nodes, i)
        bfs_map = bfs(sx, sy, moves)

        for j <- 0..(total - 1) do
          {tx, ty} = Enum.at(nodes, j)
          Map.get(bfs_map, {tx, ty})
        end
      end

    n = length(positions)
    full_mask = (1 <<< n) - 1
    {ans, _} = dfs(0, full_mask, dist, n, %{})
    ans
  end

  defp bfs(sx, sy, moves) do
    q = :queue.new() |> :queue.in({sx, sy})
    visited = %{{sx, sy} => 0}
    bfs_loop(q, visited, moves)
  end

  defp bfs_loop(queue, visited, moves) do
    case :queue.out(queue) do
      {:empty, _} ->
        visited

      {{:value, {x, y}}, q2} ->
        d = Map.get(visited, {x, y})

        {q3, visited2} =
          Enum.reduce(moves, {q2, visited}, fn {dx, dy}, {qq, vis} ->
            nx = x + dx
            ny = y + dy

            if nx >= 0 and nx < 50 and ny >= 0 and ny < 50 and not Map.has_key?(vis, {nx, ny}) do
              vis2 = Map.put(vis, {nx, ny}, d + 1)
              qq2 = :queue.in({nx, ny}, qq)
              {qq2, vis2}
            else
              {qq, vis}
            end
          end)

        bfs_loop(q3, visited2, moves)
    end
  end

  defp dfs(cur, mask, dist, n, memo) do
    import Bitwise
    key = {cur, mask}

    case Map.fetch(memo, key) do
      {:ok, val} ->
        {val, memo}

      :error ->
        if mask == 0 do
          {0, Map.put(memo, key, 0)}
        else
          turn_alice = rem(n - Integer.bit_count(mask), 2) == 0

          init_best =
            if turn_alice do
              -1_000_000_000
            else
              1_000_000_000
            end

          {best, memo2} =
            Enum.reduce(0..(n - 1), {init_best, memo}, fn i, {b, mem_acc} ->
              if (mask &&& (1 <<< i)) != 0 do
                next_cur = i + 1
                d = Enum.at(Enum.at(dist, cur), next_cur)

                {sub_val, mem_next} =
                  dfs(next_cur, mask &&& bnot(1 <<< i), dist, n, mem_acc)

                total = d + sub_val

                new_best =
                  if turn_alice do
                    max(b, total)
                  else
                    min(b, total)
                  end

                {new_best, mem_next}
              else
                {b, mem_acc}
              end
            end)

          memo_final = Map.put(memo2, key, best)
          {best, memo_final}
        end
    end
  end
end
```

# 1728. Cat and Mouse II

## Cpp

```cpp
class Solution {
public:
    int R, C, limit;
    vector<string> g;
    vector<vector<int>> mouseMoves, catMoves;
    vector<vector<vector<int>>> memo; // -1 unknown, 0 lose, 1 win

    int id(int r, int c) { return r * C + c; }

    void buildMoves(int jump, vector<vector<int>>& moves) {
        moves.assign(R * C, {});
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                if (g[r][c] == '#') continue;
                int cur = id(r,c);
                moves[cur].push_back(cur); // stay
                for (auto& d : dirs) {
                    for (int step = 1; step <= jump; ++step) {
                        int nr = r + d[0]*step, nc = c + d[1]*step;
                        if (nr < 0 || nr >= R || nc < 0 || nc >= C) break;
                        if (g[nr][nc] == '#') break;
                        moves[cur].push_back(id(nr,nc));
                    }
                }
            }
        }
    }

    bool dfs(int mPos, int cPos, int turn, int steps) {
        if (steps >= limit) return false;
        // base cases
        if (mPos == cPos) return false; // cat catches mouse
        char mf = g[mPos / C][mPos % C];
        char cf = g[cPos / C][cPos % C];
        if (mf == 'F') return true;   // mouse reaches food
        if (cf == 'F') return false;  // cat reaches food

        int &res = memo[mPos][cPos][turn];
        if (res != -1) return res == 1;

        bool mouseTurn = (turn == 0);
        if (mouseTurn) {
            // Mouse tries to find a winning move
            for (int nxt : mouseMoves[mPos]) {
                if (nxt == cPos) continue; // moving onto cat means loss, skip as not beneficial
                char ch = g[nxt / C][nxt % C];
                if (ch == 'F') { res = 1; return true; }
                if (dfs(nxt, cPos, 1, steps + 1)) {
                    res = 1;
                    return true;
                }
            }
            res = 0;
            return false;
        } else {
            // Cat tries to force mouse loss
            for (int nxt : catMoves[cPos]) {
                if (nxt == mPos) { res = 0; return false; } // catches mouse
                char ch = g[nxt / C][nxt % C];
                if (ch == 'F') { res = 0; return false; }   // reaches food
                if (!dfs(mPos, nxt, 0, steps + 1)) {
                    res = 0;
                    return false;
                }
            }
            res = 1;
            return true;
        }
    }

    bool canMouseWin(vector<string>& grid, int catJump, int mouseJump) {
        g = grid;
        R = g.size();
        C = g[0].size();
        limit = 2 * R * C;

        int mStart=-1, cStart=-1;
        for (int r=0;r<R;++r){
            for(int c=0;c<C;++c){
                if(g[r][c]=='M') mStart=id(r,c);
                else if(g[r][c]=='C') cStart=id(r,c);
            }
        }

        buildMoves(mouseJump, mouseMoves);
        buildMoves(catJump, catMoves);

        memo.assign(R*C, vector<vector<int>>(R*C, vector<int>(2, -1)));
        return dfs(mStart, cStart, 0, 0);
    }
};
```

## Java

```java
class Solution {
    private int rows, cols;
    private char[][] board;
    private int mouseJump, catJump;
    private int foodPos, mouseStart, catStart;
    private int[] dr = {-1, 1, 0, 0};
    private int[] dc = {0, 0, -1, 1};
    private int[][][] memo; // -1 unknown, 0 lose for mouse, 1 win for mouse
    private boolean[][][] inStack;

    public boolean canMouseWin(String[] grid, int catJump, int mouseJump) {
        this.rows = grid.length;
        this.cols = grid[0].length();
        this.board = new char[rows][cols];
        for (int i = 0; i < rows; ++i) board[i] = grid[i].toCharArray();

        this.mouseJump = mouseJump;
        this.catJump = catJump;

        int total = rows * cols;
        memo = new int[total][total][2];
        inStack = new boolean[total][total][2];
        for (int i = 0; i < total; ++i)
            for (int j = 0; j < total; ++j)
                java.util.Arrays.fill(memo[i][j], -1);

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                char ch = board[r][c];
                if (ch == 'M') mouseStart = r * cols + c;
                else if (ch == 'C') catStart = r * cols + c;
                else if (ch == 'F') foodPos = r * cols + c;
            }
        }

        return dfs(mouseStart, catStart, 0) == 1;
    }

    private int dfs(int mousePos, int catPos, int turn) {
        // turn: 0 -> mouse, 1 -> cat
        if (mousePos == foodPos) return 1;          // mouse reaches food
        if (catPos == foodPos) return 0;            // cat reaches food first
        if (mousePos == catPos) return 0;           // cat catches mouse

        if (memo[mousePos][catPos][turn] != -1)
            return memo[mousePos][catPos][turn];

        if (inStack[mousePos][catPos][turn]) {
            // cycle detected -> treat as loss for mouse
            memo[mousePos][catPos][turn] = 0;
            return 0;
        }
        inStack[mousePos][catPos][turn] = true;

        boolean mouseTurn = (turn == 0);
        int jump = mouseTurn ? mouseJump : catJump;
        int curPos = mouseTurn ? mousePos : catPos;
        java.util.List<Integer> nextPositions = generateMoves(curPos, jump);

        if (mouseTurn) {
            // Mouse tries to find any winning move
            for (int np : nextPositions) {
                if (dfs(np, catPos, 1) == 1) {
                    memo[mousePos][catPos][turn] = 1;
                    inStack[mousePos][catPos][turn] = false;
                    return 1;
                }
            }
            memo[mousePos][catPos][turn] = 0; // all moves lead to loss
        } else {
            // Cat tries to force mouse lose; mouse wins only if every cat move keeps mouse winning
            for (int np : nextPositions) {
                if (dfs(mousePos, np, 0) == 0) {
                    memo[mousePos][catPos][turn] = 0;
                    inStack[mousePos][catPos][turn] = false;
                    return 0;
                }
            }
            memo[mousePos][catPos][turn] = 1; // all cat moves still let mouse win
        }

        inStack[mousePos][catPos][turn] = false;
        return memo[mousePos][catPos][turn];
    }

    private java.util.List<Integer> generateMoves(int pos, int maxJump) {
        java.util.ArrayList<Integer> list = new java.util.ArrayList<>();
        int r0 = pos / cols;
        int c0 = pos % cols;
        // staying in place is always allowed
        list.add(pos);
        for (int d = 0; d < 4; ++d) {
            for (int step = 1; step <= maxJump; ++step) {
                int nr = r0 + dr[d] * step;
                int nc = c0 + dc[d] * step;
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
                if (board[nr][nc] == '#') break;
                list.add(nr * cols + nc);
            }
        }
        return list;
    }
}
```

## Python

```python
class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        R, C = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # locate positions
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'M':
                    mx0, my0 = i, j
                elif grid[i][j] == 'C':
                    cx0, cy0 = i, j
                elif grid[i][j] == 'F':
                    fx, fy = i, j
        
        # precompute reachable cells for each position and jump length
        def build_moves(jump):
            moves = {}
            for x in range(R):
                for y in range(C):
                    if grid[x][y] == '#':
                        continue
                    lst = [(x, y)]  # staying put is allowed
                    for dx, dy in dirs:
                        nx, ny = x, y
                        for _ in range(jump):
                            nx += dx
                            ny += dy
                            if not (0 <= nx < R and 0 <= ny < C) or grid[nx][ny] == '#':
                                break
                            lst.append((nx, ny))
                    moves[(x, y)] = lst
            return moves
        
        mouse_moves = build_moves(mouseJump)
        cat_moves   = build_moves(catJump)
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(mx, my, cx, cy, turn, steps):
            # steps counts total turns taken so far (mouse+cat moves)
            if steps >= 1000:
                return False
            # terminal conditions
            if (mx, my) == (fx, fy):
                return True
            if (cx, cy) == (fx, fy):
                return False
            if mx == cx and my == cy:
                return False
            
            if turn == 0:   # mouse's move
                for nx, ny in mouse_moves[(mx, my)]:
                    if dfs(nx, ny, cx, cy, 1, steps + 1):
                        return True
                return False
            else:           # cat's move
                for nx, ny in cat_moves[(cx, cy)]:
                    # cat catches mouse immediately
                    if (nx, ny) == (mx, my):
                        return False
                    if not dfs(mx, my, nx, ny, 0, steps + 1):
                        return False
                return True
        
        return dfs(mx0, my0, cx0, cy0, 0, 0)
```

## Python3

```python
import sys
sys.setrecursionlimit(10000)
from typing import List

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        walls = [[c == '#' for c in row] for row in grid]

        # locate positions
        mx = my = cx = cy = fx = fy = -1
        for i in range(rows):
            for j in range(cols):
                ch = grid[i][j]
                if ch == 'M':
                    mx, my = i, j
                elif ch == 'C':
                    cx, cy = i, j
                elif ch == 'F':
                    fx, fy = i, j

        food = (fx, fy)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        maxDepth = 1000   # safe upper bound per editorial

        from functools import lru_cache

        def reachable(x: int, y: int, jump: int):
            res = [(x, y)]  # staying put is allowed
            for dx, dy in dirs:
                nx, ny = x, y
                for _ in range(jump):
                    nx += dx
                    ny += dy
                    if not (0 <= nx < rows and 0 <= ny < cols) or walls[nx][ny]:
                        break
                    res.append((nx, ny))
            return res

        @lru_cache(None)
        def dfs(mx: int, my: int, cx: int, cy: int, turn: int, steps: int) -> bool:
            # turn 0 = mouse, 1 = cat
            if (mx, my) == food:
                return True
            if (cx, cy) == food:
                return False
            if mx == cx and my == cy:
                return False
            if steps >= maxDepth:
                return False

            if turn == 0:  # mouse's move
                for nx, ny in reachable(mx, my, mouseJump):
                    if (nx, ny) == food:
                        return True
                    if dfs(nx, ny, cx, cy, 1, steps + 1):
                        return True
                return False
            else:          # cat's move
                for nx, ny in reachable(cx, cy, catJump):
                    if (nx, ny) == food:
                        return False
                    if nx == mx and ny == my:
                        return False
                    if not dfs(mx, my, nx, ny, 0, steps + 1):
                        return False
                return True

        return dfs(mx, my, cx, cy, 0, 0)
```

## C

```c
#include <stdbool.h>
#include <string.h>

static int R, C;
static int catJumpLim, mouseJumpLim;
static char **G;

static int dp[64][64][2];
static bool vis[64][64][2];

static inline int pos(int r, int c) { return r * C + c; }

static int dfs(int mPos, int cPos, int turn, int steps) {
    if (steps > 1000) return 0; // mouse loses by timeout

    int mr = mPos / C, mc = mPos % C;
    int cr = cPos / C, cc = cPos % C;

    /* terminal states */
    if (G[mr][mc] == 'F') return 1;          // mouse reaches food
    if (G[cr][cc] == 'F') return 0;          // cat reaches food first
    if (mPos == cPos)   return 0;            // cat catches mouse

    int cached = dp[mPos][cPos][turn];
    if (cached != -1) return cached;

    if (vis[mPos][cPos][turn]) {
        /* cycle detected -> treat as loss for mouse */
        dp[mPos][cPos][turn] = 0;
        return 0;
    }
    vis[mPos][cPos][turn] = true;

    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    bool outcome;

    if (turn == 0) { /* mouse's turn */
        outcome = false;
        /* stay in place */
        if (dfs(mPos, cPos, 1, steps + 1)) {
            outcome = true;
        } else {
            for (int d = 0; d < 4 && !outcome; ++d) {
                int dr = dirs[d][0], dc = dirs[d][1];
                for (int step = 1; step <= mouseJumpLim; ++step) {
                    int nr = mr + dr * step;
                    int nc = mc + dc * step;
                    if (nr < 0 || nr >= R || nc < 0 || nc >= C) break;
                    if (G[nr][nc] == '#') break;
                    int newMPos = pos(nr, nc);
                    if (dfs(newMPos, cPos, 1, steps + 1)) {
                        outcome = true;
                        break;
                    }
                }
            }
        }
        dp[mPos][cPos][turn] = outcome ? 1 : 0;
    } else { /* cat's turn */
        outcome = true; /* assume mouse can win unless cat forces loss */
        /* stay in place */
        if (!dfs(mPos, cPos, 0, steps + 1)) {
            outcome = false;
        } else {
            for (int d = 0; d < 4 && outcome; ++d) {
                int dr = dirs[d][0], dc = dirs[d][1];
                for (int step = 1; step <= catJumpLim; ++step) {
                    int nr = cr + dr * step;
                    int nc = cc + dc * step;
                    if (nr < 0 || nr >= R || nc < 0 || nc >= C) break;
                    if (G[nr][nc] == '#') break;
                    int newCPos = pos(nr, nc);
                    if (!dfs(mPos, newCPos, 0, steps + 1)) {
                        outcome = false;
                        break;
                    }
                }
            }
        }
        dp[mPos][cPos][turn] = outcome ? 1 : 0;
    }

    vis[mPos][cPos][turn] = false;
    return dp[mPos][cPos][turn];
}

bool canMouseWin(char** grid, int gridSize, int catJump, int mouseJump) {
    R = gridSize;
    C = (int)strlen(grid[0]);
    G = grid;
    catJumpLim = catJump;
    mouseJumpLim = mouseJump;

    int mPos = -1, cPos = -1;
    for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
            if (grid[r][c] == 'M') mPos = pos(r, c);
            else if (grid[r][c] == 'C') cPos = pos(r, c);
        }
    }

    memset(dp, -1, sizeof(dp));
    memset(vis, 0, sizeof(vis));

    return dfs(mPos, cPos, 0, 0) == 1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private int rows, cols;
    private char[][] board;
    private int catJump, mouseJump;
    private int foodPos;
    private int[] dr = new int[] { -1, 1, 0, 0 };
    private int[] dc = new int[] { 0, 0, -1, 1 };
    // memo[posMouse][posCat][turn] : -1 unknown, 0 lose for mouse, 1 win for mouse
    private sbyte[,,] memo;
    
    public bool CanMouseWin(string[] grid, int catJump, int mouseJump) {
        this.rows = grid.Length;
        this.cols = grid[0].Length;
        this.board = new char[rows][];
        for (int i = 0; i < rows; i++) board[i] = grid[i].ToCharArray();
        this.catJump = catJump;
        this.mouseJump = mouseJump;
        
        int mousePos = -1, catPos = -1;
        foodPos = -1;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                char ch = board[r][c];
                if (ch == 'M') mousePos = r * cols + c;
                else if (ch == 'C') catPos = r * cols + c;
                else if (ch == 'F') foodPos = r * cols + c;
            }
        }
        
        int totalCells = rows * cols;
        memo = new sbyte[totalCells, totalCells, 2];
        for (int i = 0; i < totalCells; i++)
            for (int j = 0; j < totalCells; j++)
                memo[i, j, 0] = memo[i, j, 1] = -1;
        
        return Dfs(mousePos, catPos, 0, 0);
    }
    
    private bool Dfs(int mousePos, int catPos, int turn, int moves) {
        // turn: 0 -> mouse, 1 -> cat
        if (moves >= 1000) return false; // too many moves, mouse loses
        
        if (mousePos == foodPos) return true;
        if (catPos == foodPos) return false;
        if (mousePos == catPos) return false;
        
        sbyte cached = memo[mousePos, catPos, turn];
        if (cached != -1) return cached == 1;
        
        bool result;
        if (turn == 0) { // mouse's move
            result = false;
            foreach (int nextMouse in GetMoves(mousePos, mouseJump)) {
                if (nextMouse == catPos) continue; // moving onto cat loses immediately
                if (nextMouse == foodPos) {
                    result = true;
                    break;
                }
                bool win = Dfs(nextMouse, catPos, 1, moves + 1);
                if (win) {
                    result = true;
                    break;
                }
            }
        } else { // cat's move
            result = true; // assume mouse can win unless cat finds a winning move
            foreach (int nextCat in GetMoves(catPos, catJump)) {
                if (nextCat == mousePos) {
                    result = false;
                    break;
                }
                if (nextCat == foodPos) {
                    result = false;
                    break;
                }
                bool win = Dfs(mousePos, nextCat, 0, moves + 1);
                if (!win) {
                    result = false;
                    break;
                }
            }
        }
        
        memo[mousePos, catPos, turn] = (sbyte)(result ? 1 : 0);
        return result;
    }
    
    private IEnumerable<int> GetMoves(int startPos, int maxJump) {
        int sr = startPos / cols;
        int sc = startPos % cols;
        // staying in place is always allowed
        yield return startPos;
        for (int d = 0; d < 4; d++) {
            int nr = sr, nc = sc;
            for (int step = 1; step <= maxJump; step++) {
                nr += dr[d];
                nc += dc[d];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
                if (board[nr][nc] == '#') break;
                yield return nr * cols + nc;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} grid
 * @param {number} catJump
 * @param {number} mouseJump
 * @return {boolean}
 */
var canMouseWin = function(grid, catJump, mouseJump) {
    const rows = grid.length;
    const cols = grid[0].length;
    const total = rows * cols;
    const idx = (r, c) => r * cols + c;

    let mouseStart = -1, catStart = -1, foodIdx = -1;
    for (let r = 0; r < rows; ++r) {
        for (let c = 0; c < cols; ++c) {
            const ch = grid[r][c];
            if (ch === 'M') mouseStart = idx(r, c);
            else if (ch === 'C') catStart = idx(r, c);
            else if (ch === 'F') foodIdx = idx(r, c);
        }
    }

    // Precompute moves for each cell
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    const mouseMoves = Array.from({length: total}, () => []);
    const catMoves   = Array.from({length: total}, () => []);

    const isWall = (r,c) => grid[r][c] === '#';

    for (let r = 0; r < rows; ++r) {
        for (let c = 0; c < cols; ++c) {
            if (isWall(r,c)) continue;
            const curIdx = idx(r,c);
            // staying put is always allowed
            mouseMoves[curIdx].push(curIdx);
            catMoves[curIdx].push(curIdx);

            // mouse moves
            for (const [dr,dc] of dirs) {
                for (let step = 1; step <= mouseJump; ++step) {
                    const nr = r + dr*step;
                    const nc = c + dc*step;
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
                    if (isWall(nr,nc)) break;
                    mouseMoves[curIdx].push(idx(nr,nc));
                }
            }

            // cat moves
            for (const [dr,dc] of dirs) {
                for (let step = 1; step <= catJump; ++step) {
                    const nr = r + dr*step;
                    const nc = c + dc*step;
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
                    if (isWall(nr,nc)) break;
                    catMoves[curIdx].push(idx(nr,nc));
                }
            }
        }
    }

    const memo = new Map();

    function dfs(mPos, cPos, turn, steps, stack) {
        // step limit per problem statement
        if (steps >= 1000) return false;

        // terminal conditions
        if (mPos === foodIdx) return true;
        if (cPos === foodIdx || mPos === cPos) return false;

        const key = `${mPos},${cPos},${turn}`;
        if (memo.has(key)) return memo.get(key);
        if (stack.has(key)) {
            // cycle -> game would exceed 1000 turns, mouse loses
            memo.set(key, false);
            return false;
        }

        stack.add(key);
        let result;
        if (turn === 0) { // mouse's turn: wants any move leading to win
            result = false;
            for (const nextM of mouseMoves[mPos]) {
                if (dfs(nextM, cPos, 1, steps + 1, stack)) {
                    result = true;
                    break;
                }
            }
        } else { // cat's turn: mouse wins only if all cat moves still lead to win
            result = true;
            for (const nextC of catMoves[cPos]) {
                if (!dfs(mPos, nextC, 0, steps + 1, stack)) {
                    result = false;
                    break;
                }
            }
        }

        stack.delete(key);
        memo.set(key, result);
        return result;
    }

    return dfs(mouseStart, catStart, 0, 0, new Set());
};
```

## Typescript

```typescript
function canMouseWin(grid: string[], catJump: number, mouseJump: number): boolean {
    const rows = grid.length;
    const cols = grid[0].length;
    const total = rows * cols;
    const idx = (r: number, c: number) => r * cols + c;

    let mouseStart = -1, catStart = -1, foodIdx = -1;
    for (let r = 0; r < rows; ++r) {
        for (let c = 0; c < cols; ++c) {
            const ch = grid[r][c];
            if (ch === 'M') mouseStart = idx(r, c);
            else if (ch === 'C') catStart = idx(r, c);
            else if (ch === 'F') foodIdx = idx(r, c);
        }
    }

    // Precompute reachable positions for each cell
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    const mouseMoves: number[][] = Array.from({length: total}, () => []);
    const catMoves: number[][] = Array.from({length: total}, () => []);

    const isWall = (r: number, c: number) => grid[r][c] === '#';

    for (let r = 0; r < rows; ++r) {
        for (let c = 0; c < cols; ++c) {
            if (isWall(r,c)) continue;
            const curIdx = idx(r,c);
            // staying still is allowed
            mouseMoves[curIdx].push(curIdx);
            catMoves[curIdx].push(curIdx);

            for (const [dr, dc] of dirs) {
                // mouse
                for (let step = 1; step <= mouseJump; ++step) {
                    const nr = r + dr * step;
                    const nc = c + dc * step;
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
                    if (isWall(nr, nc)) break;
                    mouseMoves[curIdx].push(idx(nr, nc));
                }
                // cat
                for (let step = 1; step <= catJump; ++step) {
                    const nr = r + dr * step;
                    const nc = c + dc * step;
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
                    if (isWall(nr, nc)) break;
                    catMoves[curIdx].push(idx(nr, nc));
                }
            }
        }
    }

    const MAX_TURNS = 1000;

    // memo[mouse][cat][turn] = -1 unknown, 0 false, 1 true
    const memo: Int8Array[] = [];
    for (let i = 0; i < total * total * 2; ++i) memo.push(new Int8Array(1).fill(-1));
    const getMemo = (m: number, c: number, t: number) => memo[(m * total + c) * 2 + t][0];
    const setMemo = (m: number, c: number, t: number, v: number) => { memo[(m * total + c) * 2 + t][0] = v; };

    // visiting flag to detect cycles
    const visiting: Uint8Array[] = [];
    for (let i = 0; i < total * total * 2; ++i) visiting.push(new Uint8Array(1));

    function dfs(mPos: number, cPos: number, turn: number, moves: number): boolean {
        if (moves >= MAX_TURNS) return false;
        if (mPos === foodIdx) return true;
        if (cPos === foodIdx) return false;
        if (mPos === cPos) return false;

        const memoVal = getMemo(mPos, cPos, turn);
        if (memoVal !== -1) return memoVal === 1;

        const visitKey = (mPos * total + cPos) * 2 + turn;
        if (visiting[visitKey][0]) {
            // cycle detected -> treat as loss for mouse
            setMemo(mPos, cPos, turn, 0);
            return false;
        }
        visiting[visitKey][0] = 1;

        let result: boolean;
        if (turn === 0) { // mouse's turn, wants any winning move
            result = false;
            for (const nextM of mouseMoves[mPos]) {
                if (nextM === cPos) continue; // moving onto cat loses immediately
                if (dfs(nextM, cPos, 1, moves + 1)) {
                    result = true;
                    break;
                }
            }
        } else { // cat's turn, wants to force mouse loss
            result = true;
            for (const nextC of catMoves[cPos]) {
                if (nextC === mPos) {
                    result = false; // cat catches mouse
                    break;
                }
                if (!dfs(mPos, nextC, 0, moves + 1)) {
                    result = false;
                    break;
                }
            }
        }

        visiting[visitKey][0] = 0;
        setMemo(mPos, cPos, turn, result ? 1 : 0);
        return result;
    }

    return dfs(mouseStart, catStart, 0, 0);
}
```

## Php

```php
class Solution {
    private $rows;
    private $cols;
    private $grid;
    private $foodPos;
    private $catJump;
    private $mouseJump;
    private $memo = [];
    private $maxSteps = 1000;

    /**
     * @param String[] $grid
     * @param Integer $catJump
     * @param Integer $mouseJump
     * @return Boolean
     */
    function canMouseWin($grid, $catJump, $mouseJump) {
        $this->grid = $grid;
        $this->rows = count($grid);
        $this->cols = strlen($grid[0]);
        $this->catJump = $catJump;
        $this->mouseJump = $mouseJump;

        $mousePos = $catPos = -1;
        for ($i = 0; $i < $this->rows; $i++) {
            for ($j = 0; $j < $this->cols; $j++) {
                $ch = $grid[$i][$j];
                if ($ch === 'M') {
                    $mousePos = $i * $this->cols + $j;
                } elseif ($ch === 'C') {
                    $catPos = $i * $this->cols + $j;
                } elseif ($ch === 'F') {
                    $this->foodPos = $i * $this->cols + $j;
                }
            }
        }

        return $this->dfs($mousePos, $catPos, 0, 0);
    }

    private function dfs($mousePos, $catPos, $turn, $steps) {
        if ($steps >= $this->maxSteps) {
            return false;
        }
        if ($mousePos === $this->foodPos) {
            return true;
        }
        if ($catPos === $this->foodPos) {
            return false;
        }
        if ($mousePos === $catPos) {
            return false;
        }

        $key = $mousePos . ',' . $catPos . ',' . $turn;
        if (isset($this->memo[$key])) {
            return $this->memo[$key];
        }

        if ($turn === 0) { // mouse's turn
            $moves = $this->getMoves($mousePos, $this->mouseJump);
            foreach ($moves as $nextMouse) {
                if ($this->dfs($nextMouse, $catPos, 1, $steps + 1)) {
                    $this->memo[$key] = true;
                    return true;
                }
            }
            $this->memo[$key] = false;
            return false;
        } else { // cat's turn
            $moves = $this->getMoves($catPos, $this->catJump);
            foreach ($moves as $nextCat) {
                if (!$this->dfs($mousePos, $nextCat, 0, $steps + 1)) {
                    $this->memo[$key] = false;
                    return false;
                }
            }
            $this->memo[$key] = true;
            return true;
        }
    }

    private function getMoves($pos, $jump) {
        $r = intdiv($pos, $this->cols);
        $c = $pos % $this->cols;
        $result = [$pos]; // staying in place is allowed
        $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        foreach ($dirs as $d) {
            $nr = $r;
            $nc = $c;
            for ($step = 1; $step <= $jump; $step++) {
                $nr += $d[0];
                $nc += $d[1];
                if ($nr < 0 || $nr >= $this->rows || $nc < 0 || $nc >= $this->cols) {
                    break;
                }
                if ($this->grid[$nr][$nc] === '#') {
                    break;
                }
                $result[] = $nr * $this->cols + $nc;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    struct State: Hashable {
        let mouse: Int
        let cat: Int
        let turn: Int   // 0 = mouse, 1 = cat
    }
    
    var rows = 0
    var cols = 0
    var total = 0
    var foodPos = 0
    var mouseJump = 0
    var catJump = 0
    var mouseMoves: [[Int]] = []
    var catMoves: [[Int]] = []
    var memo: [State: Bool] = [:]
    
    func canMouseWin(_ grid: [String], _ catJump: Int, _ mouseJump: Int) -> Bool {
        self.rows = grid.count
        self.cols = grid[0].count
        self.total = rows * cols
        self.catJump = catJump
        self.mouseJump = mouseJump
        
        var mousePos = 0
        var catPos = 0
        for r in 0..<rows {
            let chars = Array(grid[r])
            for c in 0..<cols {
                let idx = r * cols + c
                switch chars[c] {
                case "M":
                    mousePos = idx
                case "C":
                    catPos = idx
                case "F":
                    foodPos = idx
                default:
                    break
                }
            }
        }
        
        // precompute moves for each cell
        mouseMoves = Array(repeating: [], count: total)
        catMoves = Array(repeating: [], count: total)
        let dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        var board = Array(repeating: false, count: total) // true if wall
        for r in 0..<rows {
            let chars = Array(grid[r])
            for c in 0..<cols {
                if chars[c] == "#" {
                    board[r*cols + c] = true
                }
            }
        }
        
        func computeMoves(_ jump: Int, _ movesArr: inout [[Int]]) {
            for r in 0..<rows {
                for c in 0..<cols {
                    let start = r * cols + c
                    if board[start] { continue } // wall, no moves needed
                    var list: [Int] = [start]   // staying is allowed
                    for (dx, dy) in dirs {
                        var nr = r
                        var nc = c
                        for _ in 1...jump {
                            nr += dx
                            nc += dy
                            if nr < 0 || nr >= rows || nc < 0 || nc >= cols { break }
                            let nid = nr * cols + nc
                            if board[nid] { break }
                            list.append(nid)
                        }
                    }
                    movesArr[start] = list
                }
            }
        }
        
        computeMoves(mouseJump, &mouseMoves)
        computeMoves(catJump, &catMoves)
        
        return dfs(mousePos, catPos, 0, 0)
    }
    
    private func dfs(_ mouse: Int, _ cat: Int, _ turn: Int, _ steps: Int) -> Bool {
        if steps > 1000 { return false }               // too many moves, mouse loses
        if mouse == foodPos { return true }            // mouse reached food
        if cat == foodPos { return false }             // cat reached food first
        if mouse == cat { return false }               // cat caught mouse
        
        let state = State(mouse: mouse, cat: cat, turn: turn)
        if let cached = memo[state] {
            return cached
        }
        
        var result: Bool
        if turn == 0 { // mouse's turn, wants at least one winning move
            result = false
            for nextMouse in mouseMoves[mouse] {
                if nextMouse == cat { continue } // moving onto cat loses immediately
                let win = dfs(nextMouse, cat, 1, steps + 1)
                if win {
                    result = true
                    break
                }
            }
        } else { // cat's turn, wants to force mouse loss
            result = true   // assume mouse can win unless cat finds a losing move for mouse
            for nextCat in catMoves[cat] {
                if nextCat == mouse { // cat catches mouse
                    result = false
                    break
                }
                let win = dfs(mouse, nextCat, 0, steps + 1)
                if !win {
                    result = false
                    break
                }
            }
        }
        
        memo[state] = result
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun canMouseWin(grid: Array<String>, catJump: Int, mouseJump: Int): Boolean {
        val rows = grid.size
        val cols = grid[0].length
        val total = rows * cols

        fun idx(r: Int, c: Int) = r * cols + c

        var mouseStart = -1
        var catStart = -1
        var foodPos = -1
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                when (grid[r][c]) {
                    'M' -> mouseStart = idx(r, c)
                    'C' -> catStart = idx(r, c)
                    'F' -> foodPos = idx(r, c)
                }
            }
        }

        // Precompute moves for mouse and cat
        val movesMouse = Array(total) { IntArray(0) }
        val movesCat = Array(total) { IntArray(0) }
        val revMovesMouse = Array(total) { mutableListOf<Int>() }
        val revMovesCat = Array(total) { mutableListOf<Int>() }

        val dirs = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))

        fun computeMoves(jump: Int, movesArr: Array<IntArray>) {
            for (r in 0 until rows) {
                for (c in 0 until cols) {
                    val start = idx(r, c)
                    if (grid[r][c] == '#') continue
                    val list = mutableListOf<Int>()
                    list.add(start) // stay
                    for (d in dirs) {
                        var nr = r
                        var nc = c
                        for (step in 1..jump) {
                            nr += d[0]
                            nc += d[1]
                            if (nr !in 0 until rows || nc !in 0 until cols) break
                            if (grid[nr][nc] == '#') break
                            list.add(idx(nr, nc))
                        }
                    }
                    movesArr[start] = list.toIntArray()
                }
            }
        }

        computeMoves(mouseJump, movesMouse)
        computeMoves(catJump, movesCat)

        // Build reverse adjacency
        for (src in 0 until total) {
            if (grid[src / cols][src % cols] == '#') continue
            for (dest in movesMouse[src]) revMovesMouse[dest].add(src)
            for (dest in movesCat[src]) revMovesCat[dest].add(src)
        }

        val stateSize = total * total * 2
        val result = IntArray(stateSize) { -1 } // -1 unknown, 0 mouse loses, 1 mouse wins
        val degree = IntArray(stateSize)

        // Initialize degrees
        for (m in 0 until total) {
            if (grid[m / cols][m % cols] == '#') continue
            for (c in 0 until total) {
                if (grid[c / cols][c % cols] == '#') continue
                val base = (m * total + c) * 2
                degree[base] = movesMouse[m].size          // mouse turn
                degree[base + 1] = movesCat[c].size         // cat turn
            }
        }

        val queue: ArrayDeque<Int> = ArrayDeque()

        // Terminal states
        for (m in 0 until total) {
            if (grid[m / cols][m % cols] == '#') continue
            for (c in 0 until total) {
                if (grid[c / cols][c % cols] == '#') continue
                val base = (m * total + c) * 2
                // Mouse already at food -> mouse wins
                if (m == foodPos) {
                    for (t in 0..1) {
                        val id = base + t
                        if (result[id] == -1) {
                            result[id] = 1
                            queue.add(id)
                        }
                    }
                } else if (c == foodPos) { // Cat at food -> mouse loses
                    for (t in 0..1) {
                        val id = base + t
                        if (result[id] == -1) {
                            result[id] = 0
                            queue.add(id)
                        }
                    }
                } else if (m == c) { // Cat catches mouse -> mouse loses
                    for (t in 0..1) {
                        val id = base + t
                        if (result[id] == -1) {
                            result[id] = 0
                            queue.add(id)
                        }
                    }
                }
            }
        }

        while (!queue.isEmpty()) {
            val cur = queue.removeFirst()
            val turn = cur and 1 // 0 mouse, 1 cat
            val tmp = cur shr 1
            val catPos = tmp % total
            val mousePos = tmp / total
            val curRes = result[cur] // 0 lose for mouse, 1 win for mouse

            val prevTurn = 1 - turn
            if (prevTurn == 0) {
                // predecessor had mouse's move
                for (pm in revMovesMouse[mousePos]) {
                    val preIdx = ((pm * total + catPos) * 2) + prevTurn
                    if (result[preIdx] != -1) continue
                    if (curRes == 1) {
                        result[preIdx] = 1
                        queue.add(preIdx)
                    } else {
                        degree[preIdx]--
                        if (degree[preIdx] == 0) {
                            result[preIdx] = 0
                            queue.add(preIdx)
                        }
                    }
                }
            } else {
                // predecessor had cat's move
                for (pc in revMovesCat[catPos]) {
                    val preIdx = ((mousePos * total + pc) * 2) + prevTurn
                    if (result[preIdx] != -1) continue
                    if (curRes == 0) {
                        result[preIdx] = 0
                        queue.add(preIdx)
                    } else {
                        degree[preIdx]--
                        if (degree[preIdx] == 0) {
                            result[preIdx] = 1
                            queue.add(preIdx)
                        }
                    }
                }
            }
        }

        val startState = ((mouseStart * total + catStart) * 2) // mouse's turn
        return result[startState] == 1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  bool canMouseWin(List<String> grid, int catJump, int mouseJump) {
    int rows = grid.length;
    int cols = grid[0].length;
    int n = rows * cols;

    int foodIdx = -1;
    int catStart = -1;
    int mouseStart = -1;

    for (int r = 0; r < rows; ++r) {
      for (int c = 0; c < cols; ++c) {
        int idx = r * cols + c;
        String ch = grid[r][c];
        if (ch == 'F') foodIdx = idx;
        if (ch == 'C') catStart = idx;
        if (ch == 'M') mouseStart = idx;
      }
    }

    List<int> dr = [-1, 1, 0, 0];
    List<int> dc = [0, 0, -1, 1];

    List<List<int>> mouseMoves = List.generate(n, (_) => []);
    List<List<int>> catMoves = List.generate(n, (_) => []);

    for (int r = 0; r < rows; ++r) {
      for (int c = 0; c < cols; ++c) {
        if (grid[r][c] == '#') continue;
        int idx = r * cols + c;

        List<int> mlist = [idx];
        for (int d = 0; d < 4; ++d) {
          for (int step = 1; step <= mouseJump; ++step) {
            int nr = r + dr[d] * step;
            int nc = c + dc[d] * step;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
            if (grid[nr][nc] == '#') break;
            mlist.add(nr * cols + nc);
          }
        }
        mouseMoves[idx] = mlist;

        List<int> clist = [idx];
        for (int d = 0; d < 4; ++d) {
          for (int step = 1; step <= catJump; ++step) {
            int nr = r + dr[d] * step;
            int nc = c + dc[d] * step;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
            if (grid[nr][nc] == '#') break;
            clist.add(nr * cols + nc);
          }
        }
        catMoves[idx] = clist;
      }
    }

    List<List<int>> revMouse = List.generate(n, (_) => []);
    List<List<int>> revCat = List.generate(n, (_) => []);

    for (int src = 0; src < n; ++src) {
      for (int dst in mouseMoves[src]) revMouse[dst].add(src);
      for (int dst in catMoves[src]) revCat[dst].add(src);
    }

    List<List<List<int>>> result =
        List.generate(n, (_) => List.generate(n, (_) => List.filled(2, -1)));
    List<List<List<int>>> degree =
        List.generate(n, (_) => List.generate(n, (_) => List.filled(2, 0)));

    for (int c = 0; c < n; ++c) {
      for (int m = 0; m < n; ++m) {
        degree[c][m][0] = mouseMoves[m].length;
        degree[c][m][1] = catMoves[c].length;
      }
    }

    Queue<List<int>> q = Queue();

    for (int c = 0; c < n; ++c) {
      for (int m = 0; m < n; ++m) {
        if (c == m) {
          result[c][m][0] = 0;
          result[c][m][1] = 0;
          q.add([c, m, 0]);
          q.add([c, m, 1]);
        } else if (m == foodIdx) {
          result[c][m][0] = 1;
          result[c][m][1] = 1;
          q.add([c, m, 0]);
          q.add([c, m, 1]);
        } else if (c == foodIdx) {
          result[c][m][0] = 0;
          result[c][m][1] = 0;
          q.add([c, m, 0]);
          q.add([c, m, 1]);
        }
      }
    }

    while (q.isNotEmpty) {
      var cur = q.removeFirst();
      int cPos = cur[0];
      int mPos = cur[1];
      int turn = cur[2];
      int curRes = result[cPos][mPos][turn];

      if (turn == 0) {
        // mouse's turn now, predecessor was cat move
        for (int pc in revCat[cPos]) {
          if (result[pc][mPos][1] != -1) continue;
          if (curRes == 0) {
            result[pc][mPos][1] = 0;
            q.add([pc, mPos, 1]);
          } else {
            degree[pc][mPos][1]--;
            if (degree[pc][mPos][1] == 0) {
              result[pc][mPos][1] = 1;
              q.add([pc, mPos, 1]);
            }
          }
        }
      } else {
        // cat's turn now, predecessor was mouse move
        for (int pm in revMouse[mPos]) {
          if (result[cPos][pm][0] != -1) continue;
          if (curRes == 1) {
            result[cPos][pm][0] = 1;
            q.add([cPos, pm, 0]);
          } else {
            degree[cPos][pm][0]--;
            if (degree[cPos][pm][0] == 0) {
              result[cPos][pm][0] = 0;
              q.add([cPos, pm, 0]);
            }
          }
        }
      }
    }

    return result[catStart][mouseStart][0] == 1;
  }
}
```

## Golang

```go
package main

func canMouseWin(grid []string, catJump int, mouseJump int) bool {
	rows := len(grid)
	cols := len(grid[0])

	type pos struct{ r, c int }
	var mousePos, catPos, foodPos pos
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			switch grid[i][j] {
			case 'M':
				mousePos = pos{i, j}
			case 'C':
				catPos = pos{i, j}
			case 'F':
				foodPos = pos{i, j}
			}
		}
	}

	idx := func(p pos) int { return p.r*cols + p.c }
	mIdx := idx(mousePos)
	cIdx := idx(catPos)
	fIdx := idx(foodPos)

	const maxStates = 64
	var memo [maxStates][maxStates][2]int8 // -1 unknown,0 lose,1 win
	var visited [maxStates][maxStates][2]bool

	// initialize memo to -1
	for i := 0; i < maxStates; i++ {
		for j := 0; j < maxStates; j++ {
			memo[i][j][0] = -1
			memo[i][j][1] = -1
		}
	}

	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	var dfs func(m, c, turn, depth int) bool
	dfs = func(m, c, turn, depth int) bool {
		if depth >= 1000 {
			return false
		}
		if m == fIdx {
			return true
		}
		if c == fIdx || m == c {
			return false
		}
		if memo[m][c][turn] != -1 {
			return memo[m][c][turn] == 1
		}
		if visited[m][c][turn] {
			return false
		}
		visited[m][c][turn] = true

		var win bool
		if turn == 0 { // mouse's turn
			win = false
			// generate moves for mouse (including staying)
			mr, mc := m/cols, m%cols
			possible := []int{m}
			for _, d := range dirs {
				for step := 1; step <= mouseJump; step++ {
					nr, nc := mr+d[0]*step, mc+d[1]*step
					if nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == '#' {
						break
					}
					possible = append(possible, idx(pos{nr, nc}))
				}
			}
			for _, nm := range possible {
				if nm == fIdx {
					win = true
					break
				}
				if nm == c { // mouse moves onto cat -> lose, skip
					continue
				}
				if dfs(nm, c, 1, depth+1) {
					win = true
					break
				}
			}
		} else { // cat's turn
			win = true // assume mouse can win unless cat has a forcing move
			cr, cc := c/cols, c%cols
			possible := []int{c}
			for _, d := range dirs {
				for step := 1; step <= catJump; step++ {
					nr, nc := cr+d[0]*step, cc+d[1]*step
					if nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == '#' {
						break
					}
					possible = append(possible, idx(pos{nr, nc}))
				}
			}
			for _, ncPos := range possible {
				if ncPos == fIdx || ncPos == m {
					win = false
					break
				}
				if !dfs(m, ncPos, 0, depth+1) {
					win = false
					break
				}
			}
		}

		visited[m][c][turn] = false
		if win {
			memo[m][c][turn] = 1
		} else {
			memo[m][c][turn] = 0
		}
		return win
	}

	return dfs(mIdx, cIdx, 0, 0)
}
```

## Ruby

```ruby
def can_mouse_win(grid, cat_jump, mouse_jump)
  @rows = grid.size
  @cols = grid[0].size
  @grid = grid.map { |row| row.chars }
  @cat_jump = cat_jump
  @mouse_jump = mouse_jump

  @food_r = @food_c = nil
  mouse_start = cat_start = nil

  (0...@rows).each do |r|
    (0...@cols).each do |c|
      case @grid[r][c]
      when 'F'
        @food_r, @food_c = r, c
      when 'M'
        mouse_start = [r, c]
      when 'C'
        cat_start = [r, c]
      end
    end
  end

  @memo = {}
  dfs(mouse_start[0], mouse_start[1], cat_start[0], cat_start[1], 0, 0)
end

def dfs(mr, mc, cr, cc, turn, moves)
  return false if moves >= 1000
  return true if mr == @food_r && mc == @food_c
  return false if cr == @food_r && cc == @food_c
  return false if mr == cr && mc == cc

  key = [mr, mc, cr, cc, turn]
  cached = @memo[key]
  return cached unless cached.nil?

  if turn.zero? # mouse's turn
    possible_moves(mr, mc, @mouse_jump).each do |nr, nc|
      if dfs(nr, nc, cr, cc, 1, moves + 1)
        @memo[key] = true
        return true
      end
    end
    @memo[key] = false
    false
  else # cat's turn
    possible_moves(cr, cc, @cat_jump).each do |nr, nc|
      unless dfs(mr, mc, nr, nc, 0, moves + 1)
        @memo[key] = false
        return false
      end
    end
    @memo[key] = true
    true
  end
end

def possible_moves(r, c, jump)
  res = [[r, c]]
  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  dirs.each do |dr, dc|
    nr = r
    nc = c
    (1..jump).each do
      nr += dr
      nc += dc
      break unless in_bounds?(nr, nc) && @grid[nr][nc] != '#'
      res << [nr, nc]
    end
  end
  res
end

def in_bounds?(r, c)
  r >= 0 && r < @rows && c >= 0 && c < @cols
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.{ArrayBuffer, ArrayDeque}

    def canMouseWin(grid: Array[String], catJump: Int, mouseJump: Int): Boolean = {
        val rows = grid.length
        val cols = grid(0).length
        val n = rows * cols

        var mouseStart = -1
        var catStart = -1
        var foodIdx = -1
        val walls = new Array[Boolean](n)

        for (r <- 0 until rows; c <- 0 until cols) {
            val idx = r * cols + c
            grid(r)(c) match {
                case 'M' => mouseStart = idx
                case 'C' => catStart = idx
                case 'F' => foodIdx = idx
                case '#' => walls(idx) = true
                case _   =>
            }
        }

        def computeMoves(jump: Int): Array[Array[Int]] = {
            val moves = new Array[Array[Int]](n)
            val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
            for (r <- 0 until rows; c <- 0 until cols) {
                val idx = r * cols + c
                if (walls(idx)) {
                    moves(idx) = Array.emptyIntArray
                } else {
                    val buf = ArrayBuffer[Int]()
                    buf += idx // stay
                    for ((dr, dc) <- dirs) {
                        var step = 1
                        while (step <= jump) {
                            val nr = r + dr * step
                            val nc = c + dc * step
                            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                                // out of bounds, stop this direction
                                step = jump + 1
                            } else {
                                val nIdx = nr * cols + nc
                                if (walls(nIdx)) {
                                    // blocked by wall
                                    step = jump + 1
                                } else {
                                    buf += nIdx
                                    step += 1
                                }
                            }
                        }
                    }
                    moves(idx) = buf.toArray
                }
            }
            moves
        }

        val mouseMoves = computeMoves(mouseJump)
        val catMoves   = computeMoves(catJump)

        // reverse adjacency lists
        val revMouseBuf = Array.fill(n)(ArrayBuffer[Int]())
        for (src <- 0 until n) {
            for (dst <- mouseMoves(src)) revMouseBuf(dst) += src
        }
        val revMouse = revMouseBuf.map(_.toArray)

        val revCatBuf = Array.fill(n)(ArrayBuffer[Int]())
        for (src <- 0 until n) {
            for (dst <- catMoves(src)) revCatBuf(dst) += src
        }
        val revCat = revCatBuf.map(_.toArray)

        // degree and result arrays
        val degree = Array.ofDim[Int](n, n, 2)
        val result = Array.ofDim[Int](n, n, 2) // 0 unknown, 1 mouse win, 2 cat win

        for (m <- 0 until n; c <- 0 until n) {
            if (!walls(m) && !walls(c)) {
                degree(m)(c)(0) = mouseMoves(m).length
                degree(m)(c)(1) = catMoves(c).length
            }
        }

        val queue = ArrayDeque[(Int, Int, Int)]()

        // terminal states: mouse on food -> mouse win
        for (c <- 0 until n; t <- 0 to 1) {
            if (result(foodIdx)(c)(t) == 0) {
                result(foodIdx)(c)(t) = 1
                queue.append((foodIdx, c, t))
            }
        }

        // terminal states: cat on food or cat catches mouse -> cat win
        for (m <- 0 until n; t <- 0 to 1) {
            if (result(m)(foodIdx)(t) == 0) {
                result(m)(foodIdx)(t) = 2
                queue.append((m, foodIdx, t))
            }
            if (result(m)(m)(t) == 0) {
                result(m)(m)(t) = 2
                queue.append((m, m, t))
            }
        }

        while (queue.nonEmpty) {
            val (mPos, cPos, turn) = queue.removeHead()
            val res = result(mPos)(cPos)(turn)
            val prevTurn = 1 - turn

            if (prevTurn == 0) { // predecessor where mouse moves
                for (pm <- revMouse(mPos)) {
                    if (result(pm)(cPos)(prevTurn) == 0) {
                        if (res == 1) {
                            result(pm)(cPos)(prevTurn) = 1
                            queue.append((pm, cPos, prevTurn))
                        } else { // res == 2 cat win
                            degree(pm)(cPos)(prevTurn) -= 1
                            if (degree(pm)(cPos)(prevTurn) == 0) {
                                result(pm)(cPos)(prevTurn) = 2
                                queue.append((pm, cPos, prevTurn))
                            }
                        }
                    }
                }
            } else { // predecessor where cat moves
                for (pc <- revCat(cPos)) {
                    if (result(mPos)(pc)(prevTurn) == 0) {
                        if (res == 2) {
                            result(mPos)(pc)(prevTurn) = 2
                            queue.append((mPos, pc, prevTurn))
                        } else { // res == 1 mouse win
                            degree(mPos)(pc)(prevTurn) -= 1
                            if (degree(mPos)(pc)(prevTurn) == 0) {
                                result(mPos)(pc)(prevTurn) = 1
                                queue.append((mPos, pc, prevTurn))
                            }
                        }
                    }
                }
            }
        }

        result(mouseStart)(catStart)(0) == 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_mouse_win(grid: Vec<String>, cat_jump: i32, mouse_jump: i32) -> bool {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut board = vec![vec![' '; cols]; rows];
        for (i, row_str) in grid.iter().enumerate() {
            for (j, ch) in row_str.chars().enumerate() {
                board[i][j] = ch;
            }
        }

        let total = rows * cols;
        let mut mouse_start = 0usize;
        let mut cat_start = 0usize;
        let mut food = 0usize;

        for i in 0..rows {
            for j in 0..cols {
                let idx = i * cols + j;
                match board[i][j] {
                    'M' => mouse_start = idx,
                    'C' => cat_start = idx,
                    'F' => food = idx,
                    _ => {}
                }
            }
        }

        // Pre‑compute reachable positions for each cell.
        let dirs = [(1_i32, 0_i32), (-1, 0), (0, 1), (0, -1)];
        let mut mouse_moves: Vec<Vec<usize>> = vec![Vec::new(); total];
        let mut cat_moves: Vec<Vec<usize>> = vec![Vec::new(); total];

        for i in 0..rows {
            for j in 0..cols {
                if board[i][j] == '#' {
                    continue;
                }
                let idx = i * cols + j;

                // mouse moves
                let mut list = Vec::new();
                list.push(idx); // stay
                for &(dx, dy) in &dirs {
                    for step in 1..=mouse_jump as usize {
                        let ni = i as i32 + dx * step as i32;
                        let nj = j as i32 + dy * step as i32;
                        if ni < 0 || nj < 0 || ni >= rows as i32 || nj >= cols as i32 {
                            break;
                        }
                        let ui = ni as usize;
                        let uj = nj as usize;
                        if board[ui][uj] == '#' {
                            break;
                        }
                        list.push(ui * cols + uj);
                    }
                }
                mouse_moves[idx] = list;

                // cat moves
                let mut clist = Vec::new();
                clist.push(idx); // stay
                for &(dx, dy) in &dirs {
                    for step in 1..=cat_jump as usize {
                        let ni = i as i32 + dx * step as i32;
                        let nj = j as i32 + dy * step as i32;
                        if ni < 0 || nj < 0 || ni >= rows as i32 || nj >= cols as i32 {
                            break;
                        }
                        let ui = ni as usize;
                        let uj = nj as usize;
                        if board[ui][uj] == '#' {
                            break;
                        }
                        clist.push(ui * cols + uj);
                    }
                }
                cat_moves[idx] = clist;
            }
        }

        // dp[mouse][cat][turn] : -1 unknown, 0 lose, 1 win
        let mut dp: Vec<Vec<[i8; 2]>> = vec![vec![[ -1; 2]; total]; total];
        // visited for cycle detection
        let mut vis: Vec<Vec<[bool; 2]>> = vec![vec![[ false; 2]; total]; total];

        fn dfs(
            mouse: usize,
            cat: usize,
            turn: usize, // 0 -> mouse, 1 -> cat
            food: usize,
            mouse_moves: &Vec<Vec<usize>>,
            cat_moves: &Vec<Vec<usize>>,
            dp: &mut Vec<Vec<[i8; 2]>>,
            vis: &mut Vec<Vec<[bool; 2]>>,
        ) -> bool {
            if mouse == food {
                return true;
            }
            if cat == food || mouse == cat {
                return false;
            }

            if dp[mouse][cat][turn] != -1 {
                return dp[mouse][cat][turn] == 1;
            }
            if vis[mouse][cat][turn] {
                // cycle -> treat as loss for mouse
                dp[mouse][cat][turn] = 0;
                return false;
            }

            vis[mouse][cat][turn] = true;

            let result = if turn == 0 {
                // Mouse's turn: try to find any winning move.
                let mut win = false;
                for &next_mouse in &mouse_moves[mouse] {
                    if dfs(
                        next_mouse,
                        cat,
                        1,
                        food,
                        mouse_moves,
                        cat_moves,
                        dp,
                        vis,
                    ) {
                        win = true;
                        break;
                    }
                }
                win
            } else {
                // Cat's turn: it tries to force a loss for the mouse.
                let mut all_win = true;
                for &next_cat in &cat_moves[cat] {
                    if !dfs(
                        mouse,
                        next_cat,
                        0,
                        food,
                        mouse_moves,
                        cat_moves,
                        dp,
                        vis,
                    ) {
                        all_win = false;
                        break;
                    }
                }
                all_win
            };

            vis[mouse][cat][turn] = false;
            dp[mouse][cat][turn] = if result { 1 } else { 0 };
            result
        }

        dfs(
            mouse_start,
            cat_start,
            0,
            food,
            &mouse_moves,
            &cat_moves,
            &mut dp,
            &mut vis,
        )
    }
}
```

## Racket

```racket
#lang racket

(define (can-mouse-win grid catJump mouseJump)
  (define rows (length grid))
  (define cols (string-length (first grid)))
  (define n (* rows cols))

  (define (pos->idx r c) (+ (* r cols) c))
  (define (idx->rc idx) (values (quotient idx cols) (remainder idx cols)))

  ;; locate special cells and walls
  (define mouse-start -1)
  (define cat-start -1)
  (define food-pos -1)
  (define walls (make-vector n #f))

  (for ([r (in-range rows)])
    (let ((row-str (list-ref grid r)))
      (for ([c (in-range cols)])
        (define ch (string-ref row-str c))
        (define idx (pos->idx r c))
        (cond
          [(char=? ch #\#) (vector-set! walls idx #t)]
          [(char=? ch #\M) (set! mouse-start idx)]
          [(char=? ch #\C) (set! cat-start idx)]
          [(char=? ch #\F) (set! food-pos idx)]))))

  ;; precompute reachable positions for a given jump length
  (define (precompute jump)
    (define moves (make-vector n '()))
    (for ([r (in-range rows)])
      (for ([c (in-range cols)])
        (define idx (pos->idx r c))
        (when (not (vector-ref walls idx))
          (define reachable (list idx)) ; staying is allowed
          (for* ([dir '((0 1) (0 -1) (1 0) (-1 0))]
                 [step (in-range 1 (+ jump 1))])
            (define dr (first dir))
            (define dc (second dir))
            (define nr (+ r (* dr step)))
            (define nc (+ c (* dc step)))
            (when (and (>= nr 0) (< nr rows)
                       (>= nc 0) (< nc cols))
              (define nidx (pos->idx nr nc))
              (if (vector-ref walls nidx)
                  (break) ; hit a wall, stop this direction
                  (set! reachable (cons nidx reachable)))))
          (vector-set! moves idx (reverse reachable)))))
    moves)

  (define mouse-moves (precompute mouseJump))
  (define cat-moves   (precompute catJump))

  (define maxMoves (* 1000 rows cols)) ; generous bound

  (define memo (make-hash))

  (define (dfs m c turn steps)
    (cond
      [(= m food-pos) #t]
      [(= c m) #f]
      [(>= steps maxMoves) #f]
      [else
       (define key (list m c turn))
       (cond
         [(hash-has-key? memo key)
          (= (hash-ref memo key) 1)]
         [else
          (hash-set! memo key -2) ; placeholder to avoid re‑entering
          (define result
            (if (= turn 0) ; mouse's turn
                (let loop ((lst (vector-ref mouse-moves m)))
                  (cond
                    [(null? lst) #f]
                    [else
                     (define nm (car lst))
                     (if (or (= nm food-pos)
                             (dfs nm c 1 (+ steps 1)))
                         (begin (hash-set! memo key 1) #t)
                         (loop (cdr lst)))]))
                ; cat's turn: mouse wins only if every cat move keeps mouse safe
                (let loop ((lst (vector-ref cat-moves c)))
                  (cond
                    [(null? lst)
                     (if (dfs m c 0 (+ steps 1))
                         (begin (hash-set! memo key 1) #t)
                         (begin (hash-set! memo key 0) #f))]
                    [else
                     (define nc (car lst))
                     (if (or (= nc m) ; cat catches mouse immediately
                             (not (dfs m nc 0 (+ steps 1))))
                         (begin (hash-set! memo key 0) #f)
                         (loop (cdr lst)))])))))
          (when result (hash-set! memo key 1))
          (unless result (hash-set! memo key 0))
          result]))))

  (dfs mouse-start cat-start 0 0))
```

## Erlang

```erlang
-module(solution).
-export([can_mouse_win/3]).

-spec can_mouse_win(Grid :: [unicode:unicode_binary()], CatJump :: integer(), MouseJump :: integer()) -> boolean().
can_mouse_win(Grid, CatJump, MouseJump) ->
    Rows = length(Grid),
    FirstRow = binary_to_list(lists:nth(1, Grid)),
    Cols = length(FirstRow),

    % parse grid
    {MStart, CStart, FoodPos, Walls} = parse_grid([binary_to_list(R) || R <- Grid]),

    Total = Rows * Cols,

    MovesMouse = build_moves(Total, MouseJump, Rows, Cols, Walls),
    MovesCat   = build_moves(Total, CatJump,   Rows, Cols, Walls),

    RevMouse = build_rev(MovesMouse),
    RevCat   = build_rev(MovesCat),

    {ResultMap0, DegreeMap0, Queue0} =
        init_states(Total, MStart, CStart, FoodPos, MovesMouse, MovesCat, Walls),

    FinalResultMap = bfs(Queue0, ResultMap0, DegreeMap0, RevMouse, RevCat, Total),

    InitStateId = encode(MStart, CStart, 0, Total),
    case maps:get(InitStateId, FinalResultMap, -1) of
        1 -> true;
        _ -> false
    end.

%% --------------------------------------------------------------------
%% Grid parsing
parse_grid(RowsList) ->
    parse_rows(RowsList, 0, #{}, undefined, undefined, undefined).

parse_rows([], _RowIdx, Walls, MPos, CPos, FPos) ->
    {MPos, CPos, FPos, Walls};
parse_rows([Row|Rest], RowIdx, WallsAcc, MPosAcc, CPosAcc, FPosAcc) ->
    Cols = length(Row),
    {NewWalls, NewM, NewC, NewF} =
        parse_row(Row, RowIdx, 0, Cols, WallsAcc, MPosAcc, CPosAcc, FPosAcc),
    parse_rows(Rest, RowIdx + 1, NewWalls, NewM, NewC, NewF).

parse_row([], _RowIdx, _ColIdx, _Cols, Walls, MPos, CPos, FPos) ->
    {Walls, MPos, CPos, FPos};
parse_row([Char|Rest], RowIdx, ColIdx, Cols, WallsAcc, MPosAcc, CPosAcc, FPosAcc) ->
    Idx = RowIdx * Cols + ColIdx,
    case Char of
        $# -> parse_row(Rest, RowIdx, ColIdx + 1, Cols,
                        maps:put(Idx, true, WallsAcc), MPosAcc, CPosAcc, FPosAcc);
        $M -> parse_row(Rest, RowIdx, ColIdx + 1, Cols,
                        WallsAcc, Idx, CPosAcc, FPosAcc);
        $C -> parse_row(Rest, RowIdx, ColIdx + 1, Cols,
                        WallsAcc, MPosAcc, Idx, FPosAcc);
        $F -> parse_row(Rest, RowIdx, ColIdx + 1, Cols,
                        WallsAcc, MPosAcc, CPosAcc, Idx);
        _  -> parse_row(Rest, RowIdx, ColIdx + 1, Cols,
                        WallsAcc, MPosAcc, CPosAcc, FPosAcc)
    end.

%% --------------------------------------------------------------------
%% Moves generation
build_moves(Total, Jump, Rows, Cols, Walls) ->
    lists:foldl(fun(Pos, Acc) ->
        case maps:is_key(Pos, Walls) of
            true -> maps:put(Pos, [], Acc);
            false ->
                Moves = gen_moves(Pos, Jump, Rows, Cols, Walls),
                maps:put(Pos, Moves, Acc)
        end
    end, #{}, lists:seq(0, Total - 1)).

gen_moves(Pos, Jump, Rows, Cols, Walls) ->
    X = Pos div Cols,
    Y = Pos rem Cols,
    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
    Base = [Pos],
    lists:foldl(fun({DX,DY}, Acc) ->
        walk_dir(X, Y, DX, DY, Jump, Rows, Cols, Walls, Acc)
    end, Base, Directions).

walk_dir(_X,_Y,_DX,_DY,0,_Rows,_Cols,_Walls,Acc) -> Acc;
walk_dir(X,Y,DX,DY,Step,Rows,Cols,Walls,Acc) ->
    NX = X + DX * Step,
    NY = Y + DY * Step,
    if NX < 0 orelse NX >= Rows orelse NY < 0 orelse NY >= Cols ->
            Acc;
       true ->
            Idx = NX * Cols + NY,
            case maps:is_key(Idx, Walls) of
                true -> Acc; % blocked, stop this direction
                false ->
                    walk_dir(X,Y,DX,DY,Step-1,Rows,Cols,Walls,[Idx|Acc])
            end
    end.

build_rev(MovesMap) ->
    Rev0 = #{},
    maps:fold(fun(Src, Dests, RevAcc) ->
        lists:foldl(fun(Dest, R) ->
            case maps:is_key(Dest, R) of
                true -> maps:update_with(Dest,
                                         fun(L) -> [Src|L] end,
                                         [Src],
                                         R);
                false -> maps:put(Dest, [Src], R)
            end
        end, RevAcc, Dests)
    end, Rev0, MovesMap).

%% --------------------------------------------------------------------
%% State initialization
init_states(Total, MStart, CStart, FoodPos, MovesMouse, MovesCat, Walls) ->
    Valid = [Idx || Idx <- lists:seq(0, Total - 1), not maps:is_key(Idx, Walls)],
    init_loop(Valid, Valid, Total, MovesMouse, MovesCat, FoodPos, #{}, #{}, []).

init_loop([], _Cats, _Total, _MM, _MC, _Food, ResMap, DegMap, Queue) ->
    {ResMap, DegMap, Queue};
init_loop([M|Ms], Cats, Total, MM, MC, Food, ResMap, DegMap, Queue) ->
    {ResMap1, DegMap1, Queue1} =
        init_cat_loop(M, Cats, Total, MM, MC, Food, ResMap, DegMap, Queue),
    init_loop(Ms, Cats, Total, MM, MC, Food, ResMap1, DegMap1, Queue1).

init_cat_loop(_M, [], _Total, _MM, _MC, _Food, ResMap, DegMap, Queue) ->
    {ResMap, DegMap, Queue};
init_cat_loop(M, [C|Cs], Total, MM, MC, Food, ResMap, DegMap, Queue) ->
    {ResMap1, DegMap1, Queue1} =
        init_state_pair(M, C, Total, MM, MC, Food, ResMap, DegMap, Queue),
    init_cat_loop(M, Cs, Total, MM, MC, Food, ResMap1, DegMap1, Queue1).

init_state_pair(MPos, CPos, Total, MovesMouse, MovesCat, Food,
                ResMap, DegMap, Queue) ->
    lists:foldl(fun(Turn, {RAcc,DAcc,QAcc}) ->
        StateId = encode(MPos, CPos, Turn, Total),
        Cond =
            if MPos == Food -> win;
               CPos == Food orelse MPos == CPos -> lose;
               true -> other
            end,
        case Cond of
            win ->
                {maps:put(StateId, 1, RAcc), DAcc, [StateId|QAcc]};
            lose ->
                {maps:put(StateId, -1, RAcc), DAcc, [StateId|QAcc]};
            other ->
                Moves = if Turn == 0 -> maps:get(MPos, MovesMouse);
                           true      -> maps:get(CPos, MovesCat)
                        end,
                Deg = length(Moves),
                {RAcc, maps:put(StateId, Deg, DAcc), QAcc}
        end
    end, {ResMap, DegMap, Queue}, [0,1]).

%% --------------------------------------------------------------------
%% BFS retrograde analysis
bfs([], ResultMap, _DegMap, _RevM, _RevC, _Total) ->
    ResultMap;
bfs([StateId|Rest], ResultMap, DegreeMap, RevMouse, RevCat, Total) ->
    Res = maps:get(StateId, ResultMap),
    Turn = StateId rem 2,
    Tmp = StateId div 2,
    CPos = Tmp rem Total,
    MPos = Tmp div Total,
    PrevTurn = 1 - Turn,
    {NewResMap, NewDegMap, NewQueue} =
        if Turn == 0 ->
                SrcList = maps:get(CPos, RevCat, []),
                process_predecessors(SrcList, MPos, CPos, PrevTurn, Res,
                                    ResultMap, DegreeMap, Rest);
           true ->
                SrcList = maps:get(MPos, RevMouse, []),
                process_predecessors(SrcList, MPos, CPos, PrevTurn, Res,
                                    ResultMap, DegreeMap, Rest)
        end,
    bfs(NewQueue, NewResMap, NewDegMap, RevMouse, RevCat, Total).

process_predecessors(SrcList, MPos, CPos, PrevTurn, ResCurr,
                    ResultMap, DegreeMap, Queue) ->
    lists:foldl(fun(Src, {RAcc,DAcc,QAcc}) ->
        PrevStateId = if PrevTurn == 0 -> encode(Src, CPos, 0, get_total(RAcc));
                         true      -> encode(MPos, Src, 1, get_total(RAcc))
                      end,
        case maps:is_key(PrevStateId, RAcc) of
            true ->
                {RAcc,DAcc,QAcc};
            false ->
                Favorable = (PrevTurn == 0 andalso ResCurr == 1) orelse
                            (PrevTurn == 1 andalso ResCurr == -1),
                if Favorable ->
                        NewR = maps:put(PrevStateId, ResCurr, RAcc),
                        {NewR,DAcc,[PrevStateId|QAcc]};
                   true ->
                        Deg = maps:get(PrevStateId, DAcc) - 1,
                        NewD = maps:put(PrevStateId, Deg, DAcc),
                        if Deg == 0 ->
                                ResPrev = if PrevTurn == 0 -> 1; true -> -1 end,
                                NewR2 = maps:put(PrevStateId, ResPrev, RAcc),
                                {NewR2,NewD,[PrevStateId|QAcc]};
                           true ->
                                {RAcc,NewD,QAcc}
                        end
                end
        end
    end, {ResultMap, DegreeMap, Queue}, SrcList).

%% Helper to retrieve total cells from any map (stored globally via closure)
get_total(_Map) -> erlang:put(total_cells, erlang:get(total_cells)), erlang:get(total_cells).
% The above is a placeholder; actual total will be passed directly in encode calls.

encode(MPos, CPos, Turn, Total) ->
    ((MPos * Total + CPos) * 2) + Turn.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_mouse_win(grid :: [String.t()], cat_jump :: integer, mouse_jump :: integer) :: boolean
  def can_mouse_win(grid, cat_jump, mouse_jump) do
    rows = length(grid)
    cols = String.length(List.first(grid))
    grid_chars = Enum.map(grid, &String.to_charlist/1)

    {mx, my} = find_pos(grid_chars, ?M)
    {cx, cy} = find_pos(grid_chars, ?C)
    {fx, fy} = find_pos(grid_chars, ?F)

    :ets.new(:cache, [:named_table, :public, read_concurrency: true])

    result =
      dfs(
        mx,
        my,
        cx,
        cy,
        0,
        MapSet.new(),
        grid_chars,
        rows,
        cols,
        fx,
        fy,
        cat_jump,
        mouse_jump
      )

    :ets.delete(:cache)
    result
  end

  defp find_pos(grid, target) do
    rows = length(grid)

    Enum.reduce_while(0..rows - 1, nil, fn r, _acc ->
      row = Enum.at(grid, r)

      case Enum.find_index(row, fn ch -> ch == target end) do
        nil -> {:cont, nil}
        c -> {:halt, {r, c}}
      end
    end)
  end

  defp dfs(mx, my, cx, cy, turn, visited, grid, rows, cols, fx, fy, cat_jump, mouse_jump) do
    key = {mx, my, cx, cy, turn}

    case :ets.lookup(:cache, key) do
      [{^key, val}] ->
        val

      [] ->
        if MapSet.member?(visited, key) do
          false
        else
          visited2 = MapSet.put(visited, key)

          result =
            cond do
              mx == fx and my == fy ->
                true

              cx == fx and cy == fy ->
                false

              mx == cx and my == cy ->
                false

              turn == 0 ->
                moves = [{mx, my} | get_moves(mx, my, mouse_jump, grid, rows, cols)]

                Enum.any?(moves, fn {nx, ny} ->
                  dfs(
                    nx,
                    ny,
                    cx,
                    cy,
                    1,
                    visited2,
                    grid,
                    rows,
                    cols,
                    fx,
                    fy,
                    cat_jump,
                    mouse_jump
                  )
                end)

              true ->
                moves = [{cx, cy} | get_moves(cx, cy, cat_jump, grid, rows, cols)]

                Enum.all?(moves, fn {nx, ny} ->
                  dfs(
                    mx,
                    my,
                    nx,
                    ny,
                    0,
                    visited2,
                    grid,
                    rows,
                    cols,
                    fx,
                    fy,
                    cat_jump,
                    mouse_jump
                  )
                end)
            end

          :ets.insert(:cache, {key, result})
          result
        end
    end
  end

  defp get_moves(x, y, jump, grid, rows, cols) do
    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    Enum.flat_map(dirs, fn {dx, dy} ->
      Enum.reduce_while(1..jump, [], fn step, acc ->
        nx = x + dx * step
        ny = y + dy * step

        cond do
          nx < 0 or nx >= rows or ny < 0 or ny >= cols ->
            {:halt, acc}

          true ->
            cell = Enum.at(Enum.at(grid, nx), ny)

            if cell == ?# do
              {:halt, acc}
            else
              {:cont, [{nx, ny} | acc]}
            end
        end
      end)
      |> Enum.reverse()
    end)
  end
end
```

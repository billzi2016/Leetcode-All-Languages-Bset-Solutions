# 0913. Cat and Mouse

## Cpp

```cpp
class Solution {
public:
    int catMouseGame(vector<vector<int>>& graph) {
        const int MOUSE = 1, CAT = 2, DRAW = 0;
        int n = graph.size();
        // dp[m][c][t] outcome
        vector<vector<array<int,2>>> dp(n, vector<array<int,2>>(n, {DRAW,DRAW}));
        // degree[t][m][c]
        vector<vector<array<int,2>>> deg(n, vector<array<int,2>>(n, {0,0}));
        
        for (int m = 0; m < n; ++m) {
            for (int c = 0; c < n; ++c) {
                deg[m][c][0] = graph[m].size(); // mouse turn
                int cnt = 0;
                for (int nxt : graph[c]) if (nxt != 0) ++cnt; // cat cannot go to hole
                deg[m][c][1] = cnt; // cat turn
            }
        }
        
        deque<tuple<int,int,int>> q;
        // terminal: mouse at hole -> mouse wins
        for (int c = 0; c < n; ++c) {
            if (dp[0][c][0] == DRAW) { dp[0][c][0] = MOUSE; q.emplace_back(0,c,0); }
            if (dp[0][c][1] == DRAW) { dp[0][c][1] = MOUSE; q.emplace_back(0,c,1); }
        }
        // terminal: cat catches mouse -> cat wins
        for (int i = 1; i < n; ++i) {
            if (dp[i][i][0] == DRAW) { dp[i][i][0] = CAT; q.emplace_back(i,i,0); }
            if (dp[i][i][1] == DRAW) { dp[i][i][1] = CAT; q.emplace_back(i,i,1); }
        }
        
        while (!q.empty()) {
            auto [m,c,t] = q.front(); q.pop_front();
            int result = dp[m][c][t];
            // find parents
            if (t == 0) { // mouse's turn, parent was cat move
                for (int pcPrev : graph[c]) {
                    if (pcPrev == 0) continue; // cat cannot be at hole
                    int pm = m;
                    int pt = 1; // cat's turn in parent
                    if (dp[pm][pcPrev][pt] != DRAW) continue;
                    if (result == CAT) {
                        dp[pm][pcPrev][pt] = CAT;
                        q.emplace_back(pm, pcPrev, pt);
                    } else {
                        deg[pm][pcPrev][pt]--;
                        if (deg[pm][pcPrev][pt] == 0) {
                            dp[pm][pcPrev][pt] = MOUSE;
                            q.emplace_back(pm, pcPrev, pt);
                        }
                    }
                }
            } else { // cat's turn, parent was mouse move
                for (int pmPrev : graph[m]) {
                    int pc = c;
                    int pt = 0; // mouse's turn in parent
                    if (dp[pmPrev][pc][pt] != DRAW) continue;
                    if (result == MOUSE) {
                        dp[pmPrev][pc][pt] = MOUSE;
                        q.emplace_back(pmPrev, pc, pt);
                    } else {
                        deg[pmPrev][pc][pt]--;
                        if (deg[pmPrev][pc][pt] == 0) {
                            dp[pmPrev][pc][pt] = CAT;
                            q.emplace_back(pmPrev, pc, pt);
                        }
                    }
                }
            }
        }
        return dp[1][2][0];
    }
};
```

## Java

```java
class Solution {
    public int catMouseGame(int[][] graph) {
        int n = graph.length;
        // 0: unknown/draw, 1: mouse wins, 2: cat wins
        int[][][] color = new int[n][n][2];
        int[][][] degree = new int[n][n][2];

        // Initialize degrees
        for (int m = 0; m < n; ++m) {
            for (int c = 0; c < n; ++c) {
                // mouse's turn
                degree[m][c][0] = graph[m].length;
                // cat's turn (cannot move to hole)
                int cnt = 0;
                for (int nb : graph[c]) {
                    if (nb != 0) cnt++;
                }
                degree[m][c][1] = cnt;
            }
        }

        java.util.ArrayDeque<int[]> q = new java.util.ArrayDeque<>();

        // Terminal states
        for (int i = 0; i < n; ++i) {
            // Mouse at hole -> mouse wins
            if (color[0][i][0] == 0) {
                color[0][i][0] = 1;
                q.add(new int[]{0, i, 0});
            }
            if (color[0][i][1] == 0) {
                color[0][i][1] = 1;
                q.add(new int[]{0, i, 1});
            }
            // Cat catches mouse (except hole)
            if (i != 0) {
                if (color[i][i][0] == 0) {
                    color[i][i][0] = 2;
                    q.add(new int[]{i, i, 0});
                }
                if (color[i][i][1] == 0) {
                    color[i][i][1] = 2;
                    q.add(new int[]{i, i, 1});
                }
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int m = cur[0], c = cur[1], t = cur[2];
            int result = color[m][c][t];
            int prevTurn = 1 - t;

            if (prevTurn == 0) { // previous move was mouse
                for (int pm : graph[m]) {
                    if (color[pm][c][0] != 0) continue;
                    if (result == 1) { // mouse can force a win
                        color[pm][c][0] = 1;
                        q.add(new int[]{pm, c, 0});
                    } else {
                        degree[pm][c][0]--;
                        if (degree[pm][c][0] == 0) {
                            color[pm][c][0] = 2; // cat wins
                            q.add(new int[]{pm, c, 0});
                        }
                    }
                }
            } else { // previous move was cat
                for (int pc : graph[c]) {
                    if (pc == 0) continue; // cat cannot go to hole
                    if (color[m][pc][1] != 0) continue;
                    if (result == 2) { // cat can force a win
                        color[m][pc][1] = 2;
                        q.add(new int[]{m, pc, 1});
                    } else {
                        degree[m][pc][1]--;
                        if (degree[m][pc][1] == 0) {
                            color[m][pc][1] = 1; // mouse wins
                            q.add(new int[]{m, pc, 1});
                        }
                    }
                }
            }
        }

        return color[1][2][0];
    }
}
```

## Python

```python
class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        from collections import deque

        DRAW, MOUSE, CAT = 0, 1, 2
        n = len(graph)

        # result[m][c][turn] where turn: 0 mouse's move, 1 cat's move
        result = [[[DRAW for _ in range(2)] for __ in range(n)] for ___ in range(n)]
        degree = [[[0 for _ in range(2)] for __ in range(n)] for ___ in range(n)]

        # initialize degrees
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])                     # mouse's options
                cnt = 0
                for nxt in graph[c]:
                    if nxt != 0:                                   # cat cannot go to hole
                        cnt += 1
                degree[m][c][1] = cnt                               # cat's options

        q = deque()

        # terminal states
        for i in range(n):
            for t in (0, 1):
                if result[0][i][t] == DRAW:
                    result[0][i][t] = MOUSE
                    q.append((0, i, t))
                if i != 0 and result[i][i][t] == DRAW:
                    result[i][i][t] = CAT
                    q.append((i, i, t))

        while q:
            m, c, turn = q.popleft()
            cur_res = result[m][c][turn]

            # find parent states that can move to (m,c,turn)
            if turn == 0:   # mouse's turn now -> previous move was cat
                prev_turn = 1
                for pc in graph[c]:
                    if pc == 0:
                        continue          # cat cannot have been at hole
                    pm = m
                    if result[pm][pc][prev_turn] != DRAW:
                        continue
                    if cur_res == CAT:    # cat can force a win by moving here
                        result[pm][pc][prev_turn] = CAT
                        q.append((pm, pc, prev_turn))
                    else:                 # mouse wins in child -> bad for cat
                        degree[pm][pc][prev_turn] -= 1
                        if degree[pm][pc][prev_turn] == 0:
                            result[pm][pc][prev_turn] = MOUSE
                            q.append((pm, pc, prev_turn))
            else:           # turn == 1, cat's turn now -> previous move was mouse
                prev_turn = 0
                for pm in graph[m]:
                    pc = c
                    if result[pm][pc][prev_turn] != DRAW:
                        continue
                    if cur_res == MOUSE:   # mouse can force a win by moving here
                        result[pm][pc][prev_turn] = MOUSE
                        q.append((pm, pc, prev_turn))
                    else:                  # cat wins in child -> bad for mouse
                        degree[pm][pc][prev_turn] -= 1
                        if degree[pm][pc][prev_turn] == 0:
                            result[pm][pc][prev_turn] = CAT
                            q.append((pm, pc, prev_turn))

        return result[1][2][0]
```

## Python3

```python
import collections
from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2

        # reverse adjacency for quick parent lookup
        rev = [[] for _ in range(N)]
        for u, neigh in enumerate(graph):
            for v in neigh:
                rev[v].append(u)

        # result[m][c][t] where t:0 mouse turn,1 cat turn
        result = [[[DRAW] * 2 for _ in range(N)] for __ in range(N)]
        degree = [[[0] * 2 for _ in range(N)] for __ in range(N)]

        for m in range(N):
            for c in range(N):
                # mouse move options
                degree[m][c][0] = len(graph[m])
                # cat move options (cannot go to hole 0)
                cnt = 0
                for nxt in graph[c]:
                    if nxt != 0:
                        cnt += 1
                degree[m][c][1] = cnt

        q = collections.deque()

        # initialize terminal states
        for m in range(N):
            for c in range(N):
                if m == 0:  # mouse at hole -> mouse wins
                    for t in (0, 1):
                        if result[m][c][t] == DRAW:
                            result[m][c][t] = MOUSE
                            q.append((m, c, t))
                elif m == c:  # cat catches mouse -> cat wins
                    for t in (0, 1):
                        if result[m][c][t] == DRAW:
                            result[m][c][t] = CAT
                            q.append((m, c, t))

        while q:
            m, c, turn = q.popleft()
            cur_res = result[m][c][turn]
            prev_turn = 1 - turn

            if turn == 0:  # mouse just moved, parent was cat's turn
                for pm in rev[m]:
                    if result[pm][c][prev_turn] != DRAW:
                        continue
                    # parent player is CAT
                    if cur_res == CAT:
                        result[pm][c][prev_turn] = CAT
                        q.append((pm, c, prev_turn))
                    else:
                        degree[pm][c][prev_turn] -= 1
                        if degree[pm][c][prev_turn] == 0:
                            result[pm][c][prev_turn] = MOUSE
                            q.append((pm, c, prev_turn))
            else:  # cat just moved, parent was mouse's turn
                for pc in rev[c]:
                    if pc == 0:   # cat cannot be at the hole
                        continue
                    if result[m][pc][prev_turn] != DRAW:
                        continue
                    # parent player is MOUSE
                    if cur_res == MOUSE:
                        result[m][pc][prev_turn] = MOUSE
                        q.append((m, pc, prev_turn))
                    else:
                        degree[m][pc][prev_turn] -= 1
                        if degree[m][pc][prev_turn] == 0:
                            result[m][pc][prev_turn] = CAT
                            q.append((m, pc, prev_turn))

        return result[1][2][0]
```

## C

```c
#include <stddef.h>
#include <stdlib.h>

int catMouseGame(int** graph, int graphSize, int* graphColSize) {
    const int DRAW = 0;
    const int MOUSE_WIN = 1;
    const int CAT_WIN = 2;

    int n = graphSize;
    static int result[50][50][2];
    static int degree[50][50][2];

    // initialize degrees
    for (int m = 0; m < n; ++m) {
        for (int c = 0; c < n; ++c) {
            degree[m][c][0] = graphColSize[m];               // mouse turn
            int cnt = 0;
            for (int i = 0; i < graphColSize[c]; ++i) {
                if (graph[c][i] != 0) cnt++;                 // cat cannot go to hole
            }
            degree[m][c][1] = cnt;                           // cat turn
        }
    }

    // queue for BFS
    struct State { short m, c, t; };
    static struct State q[5005];
    int head = 0, tail = 0;

    // enqueue terminal states
    for (int c = 0; c < n; ++c) {
        if (result[0][c][0] == DRAW) { result[0][c][0] = MOUSE_WIN; q[tail++] = (struct State){0, c, 0}; }
        if (result[0][c][1] == DRAW) { result[0][c][1] = MOUSE_WIN; q[tail++] = (struct State){0, c, 1}; }
    }
    for (int m = 1; m < n; ++m) {
        if (result[m][m][0] == DRAW) { result[m][m][0] = CAT_WIN; q[tail++] = (struct State){m, m, 0}; }
        if (result[m][m][1] == DRAW) { result[m][m][1] = CAT_WIN; q[tail++] = (struct State){m, m, 1}; }
    }

    while (head < tail) {
        struct State cur = q[head++];
        int m = cur.m, c = cur.c, t = cur.t;
        int curRes = result[m][c][t];
        int prevTurn = 1 - t;

        if (prevTurn == 0) { // previous was mouse's turn
            // parents: mouse moved from pm to m, cat stayed at c
            for (int i = 0; i < graphColSize[m]; ++i) {
                int pm = graph[m][i];
                if (result[pm][c][0] != DRAW) continue;
                if (curRes == MOUSE_WIN) {
                    result[pm][c][0] = MOUSE_WIN;
                    q[tail++] = (struct State){pm, c, 0};
                } else { // curRes == CAT_WIN
                    if (--degree[pm][c][0] == 0) {
                        result[pm][c][0] = CAT_WIN;
                        q[tail++] = (struct State){pm, c, 0};
                    }
                }
            }
        } else { // previous was cat's turn
            // parents: cat moved from pc to c, mouse stayed at m
            for (int i = 0; i < graphColSize[c]; ++i) {
                int pc = graph[c][i];
                if (pc == 0) continue;               // cat cannot be in the hole
                if (result[m][pc][1] != DRAW) continue;
                if (curRes == CAT_WIN) {
                    result[m][pc][1] = CAT_WIN;
                    q[tail++] = (struct State){m, pc, 1};
                } else { // curRes == MOUSE_WIN
                    if (--degree[m][pc][1] == 0) {
                        result[m][pc][1] = MOUSE_WIN;
                        q[tail++] = (struct State){m, pc, 1};
                    }
                }
            }
        }
    }

    return result[1][2][0];
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int CatMouseGame(int[][] graph) {
        int n = graph.Length;
        const int DRAW = 0, MOUSE = 1, CAT = 2;

        int[,,] result = new int[n, n, 2];
        int[,,] degree = new int[n, n, 2];

        Queue<(int m, int c, int t)> q = new Queue<(int, int, int)>();

        for (int m = 0; m < n; ++m) {
            for (int c = 0; c < n; ++c) {
                // degree for mouse turn
                degree[m, c, 0] = graph[m].Length;
                // degree for cat turn (cannot move to hole)
                int cnt = 0;
                foreach (int nb in graph[c]) if (nb != 0) ++cnt;
                degree[m, c, 1] = cnt;

                // terminal states
                if (m == 0) {
                    result[m, c, 0] = MOUSE;
                    result[m, c, 1] = MOUSE;
                    q.Enqueue((m, c, 0));
                    q.Enqueue((m, c, 1));
                } else if (m == c) {
                    result[m, c, 0] = CAT;
                    result[m, c, 1] = CAT;
                    q.Enqueue((m, c, 0));
                    q.Enqueue((m, c, 1));
                }
            }
        }

        while (q.Count > 0) {
            var cur = q.Dequeue();
            int m = cur.m, c = cur.c, t = cur.t;
            int curRes = result[m, c, t];

            // Find all parent states that can move to (m,c,t)
            if (t == 0) { // mouse's turn now -> previous move was by cat
                foreach (int pc in graph[c]) {
                    if (pc == 0) continue; // cat cannot go to hole
                    int pm = m;
                    int pt = 1; // cat's turn before moving
                    ProcessParent(pm, pc, pt);
                }
            } else { // cat's turn now -> previous move was by mouse
                foreach (int pm in graph[m]) {
                    int pc = c;
                    int pt = 0; // mouse's turn before moving
                    ProcessParent(pm, pc, pt);
                }
            }

            void ProcessParent(int pm, int pc, int pt) {
                if (result[pm, pc, pt] != DRAW) return;

                // If the player whose turn it is can force a win by moving to curRes
                if ((pt == 0 && curRes == MOUSE) || (pt == 1 && curRes == CAT)) {
                    result[pm, pc, pt] = curRes;
                    q.Enqueue((pm, pc, pt));
                } else {
                    // Otherwise, this move is bad for the player; decrement remaining options
                    degree[pm, pc, pt]--;
                    if (degree[pm, pc, pt] == 0) {
                        int oppRes = pt == 0 ? CAT : MOUSE;
                        result[pm, pc, pt] = oppRes;
                        q.Enqueue((pm, pc, pt));
                    }
                }
            }
        }

        return result[1, 2, 0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} graph
 * @return {number}
 */
var catMouseGame = function(graph) {
    const n = graph.length;
    // result[m][c][t] : 0 unknown/draw, 1 mouse wins, 2 cat wins
    const result = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => [0, 0])
    );
    // degree[m][c][t] : number of moves from this state
    const degree = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => [0, 0])
    );

    const queue = [];
    // initialize degrees and terminal states
    for (let m = 0; m < n; ++m) {
        for (let c = 0; c < n; ++c) {
            if (m === 0) { // mouse in hole -> mouse wins
                result[m][c][0] = 1;
                result[m][c][1] = 1;
                queue.push([m, c, 0]);
                queue.push([m, c, 1]);
            } else if (m === c) { // cat catches mouse -> cat wins
                result[m][c][0] = 2;
                result[m][c][1] = 2;
                queue.push([m, c, 0]);
                queue.push([m, c, 1]);
            } else {
                degree[m][c][0] = graph[m].length; // mouse turn
                let cnt = 0;
                for (const nb of graph[c]) if (nb !== 0) ++cnt; // cat cannot go to hole
                degree[m][c][1] = cnt; // cat turn
            }
        }
    }

    let head = 0;
    while (head < queue.length) {
        const [m, c, t] = queue[head++];
        const curRes = result[m][c][t];
        const prevTurn = 1 - t;

        if (prevTurn === 0) { // previous move was mouse
            for (const pm of graph[m]) {
                if (result[pm][c][0] !== 0) continue;
                if (curRes === 1) { // mouse can force a win
                    result[pm][c][0] = 1;
                    queue.push([pm, c, 0]);
                } else { // child is cat win
                    degree[pm][c][0]--;
                    if (degree[pm][c][0] === 0) {
                        result[pm][c][0] = 2;
                        queue.push([pm, c, 0]);
                    }
                }
            }
        } else { // previous move was cat
            for (const pc of graph[c]) {
                if (pc === 0) continue; // cat cannot be in hole
                if (result[m][pc][1] !== 0) continue;
                if (curRes === 2) { // cat can force a win
                    result[m][pc][1] = 2;
                    queue.push([m, pc, 1]);
                } else { // child is mouse win
                    degree[m][pc][1]--;
                    if (degree[m][pc][1] === 0) {
                        result[m][pc][1] = 1;
                        queue.push([m, pc, 1]);
                    }
                }
            }
        }
    }

    return result[1][2][0];
};
```

## Typescript

```typescript
function catMouseGame(graph: number[][]): number {
    const MOUSE = 0;
    const CAT = 1;
    const DRAW = 2;
    const UNKNOWN = -1;
    const n = graph.length;

    // dp[m][c][t] = result for state (mouse=m, cat=c, turn=t) where t:0 mouse,1 cat
    const dp: number[][][] = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => [UNKNOWN, UNKNOWN])
    );

    // degree[m][c][t] = number of moves from this state
    const degree: number[][][] = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => [0, 0])
    );

    for (let m = 0; m < n; ++m) {
        for (let c = 0; c < n; ++c) {
            degree[m][c][0] = graph[m].length;
            let cnt = 0;
            for (const nb of graph[c]) if (nb !== 0) ++cnt;
            degree[m][c][1] = cnt;
        }
    }

    const queue: [number, number, number][] = [];

    function setState(m: number, c: number, t: number, val: number): void {
        if (dp[m][c][t] === UNKNOWN) {
            dp[m][c][t] = val;
            queue.push([m, c, t]);
        }
    }

    // Initialize terminal states
    for (let m = 0; m < n; ++m) {
        for (let c = 0; c < n; ++c) {
            for (let t = 0; t < 2; ++t) {
                if (m === 0) {
                    setState(m, c, t, MOUSE);
                } else if (m === c) {
                    setState(m, c, t, CAT);
                }
            }
        }
    }

    let head = 0;
    while (head < queue.length) {
        const [m, c, turn] = queue[head++];
        const result = dp[m][c][turn];

        if (turn === 0) { // mouse's turn, parents are cat's turn states
            for (const pc of graph[c]) {
                if (pc === 0) continue; // cat cannot come from hole
                const pm = m;
                const pt = 1;
                if (dp[pm][pc][pt] !== UNKNOWN) continue;

                if (result === CAT) { // cat can force a win
                    setState(pm, pc, pt, CAT);
                } else { // result is MOUSE
                    degree[pm][pc][pt]--;
                    if (degree[pm][pc][pt] === 0) {
                        setState(pm, pc, pt, MOUSE);
                    }
                }
            }
        } else { // cat's turn, parents are mouse's turn states
            for (const pm of graph[m]) {
                const pc = c;
                const pt = 0;
                if (dp[pm][pc][pt] !== UNKNOWN) continue;

                if (result === MOUSE) { // mouse can force a win
                    setState(pm, pc, pt, MOUSE);
                } else { // result is CAT
                    degree[pm][pc][pt]--;
                    if (degree[pm][pc][pt] === 0) {
                        setState(pm, pc, pt, CAT);
                    }
                }
            }
        }
    }

    const ans = dp[1][2][0];
    return ans === UNKNOWN ? DRAW : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function catMouseGame($graph) {
        $n = count($graph);
        // dp[mouse][cat][turn] : 0 unknown, 1 mouse wins, 2 cat wins
        $dp = array_fill(0, $n, null);
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = array_fill(0, $n, [0, 0]);
        }
        // degree[mouse][cat][turn]
        $degree = array_fill(0, $n, null);
        for ($i = 0; $i < $n; $i++) {
            $degree[$i] = array_fill(0, $n, [0, 0]);
        }

        // compute degrees
        for ($m = 0; $m < $n; $m++) {
            for ($c = 0; $c < $n; $c++) {
                $degree[$m][$c][0] = count($graph[$m]); // mouse turn
                $cnt = 0;
                foreach ($graph[$c] as $next) {
                    if ($next != 0) $cnt++;
                }
                $degree[$m][$c][1] = $cnt; // cat turn (cannot go to hole)
            }
        }

        $queue = new SplQueue();

        // terminal states: mouse at hole -> mouse wins
        for ($c = 0; $c < $n; $c++) {
            if ($dp[0][$c][0] == 0) {
                $dp[0][$c][0] = 1;
                $queue->enqueue([0, $c, 0]);
            }
            if ($dp[0][$c][1] == 0) {
                $dp[0][$c][1] = 1;
                $queue->enqueue([0, $c, 1]);
            }
        }

        // terminal states: cat catches mouse -> cat wins
        for ($m = 1; $m < $n; $m++) {
            if ($dp[$m][$m][0] == 0) {
                $dp[$m][$m][0] = 2;
                $queue->enqueue([$m, $m, 0]);
            }
            if ($dp[$m][$m][1] == 0) {
                $dp[$m][$m][1] = 2;
                $queue->enqueue([$m, $m, 1]);
            }
        }

        while (!$queue->isEmpty()) {
            [$m, $c, $t] = $queue->dequeue();
            $result = $dp[$m][$c][$t]; // winner from this state

            if ($t == 0) { // mouse's turn, came from cat move
                if ($c == 0) continue; // illegal parent (cat cannot move to hole)
                foreach ($graph[$c] as $prevC) {
                    if ($prevC == 0) continue; // cat cannot be at hole
                    $pm = $m;
                    $pc = $prevC;
                    $pt = 1; // cat's turn in parent
                    if ($dp[$pm][$pc][$pt] != 0) continue;

                    if ($result == 2) { // cat wins, good for cat parent
                        $dp[$pm][$pc][$pt] = 2;
                        $queue->enqueue([$pm, $pc, $pt]);
                    } else {
                        // mouse win, bad for cat parent
                        $degree[$pm][$pc][$pt]--;
                        if ($degree[$pm][$pc][$pt] == 0) {
                            $dp[$pm][$pc][$pt] = 1;
                            $queue->enqueue([$pm, $pc, $pt]);
                        }
                    }
                }
            } else { // cat's turn, came from mouse move
                foreach ($graph[$m] as $prevM) {
                    $pm = $prevM;
                    $pc = $c;
                    $pt = 0; // mouse's turn in parent
                    if ($dp[$pm][$pc][$pt] != 0) continue;

                    if ($result == 1) { // mouse wins, good for mouse parent
                        $dp[$pm][$pc][$pt] = 1;
                        $queue->enqueue([$pm, $pc, $pt]);
                    } else {
                        // cat win, bad for mouse parent
                        $degree[$pm][$pc][$pt]--;
                        if ($degree[$pm][$pc][$pt] == 0) {
                            $dp[$pm][$pc][$pt] = 2;
                            $queue->enqueue([$pm, $pc, $pt]);
                        }
                    }
                }
            }
        }

        return $dp[1][2][0];
    }
}
```

## Swift

```swift
class Solution {
    func catMouseGame(_ graph: [[Int]]) -> Int {
        let n = graph.count
        let DRAW = 0, MOUSE = 1, CAT = 2
        
        // result[mouse][cat][turn] : 0 draw/unknown, 1 mouse wins, 2 cat wins
        var result = Array(repeating: Array(repeating: Array(repeating: DRAW, count: 2), count: n), count: n)
        // degree counts remaining moves that are not yet known to lead to a win for the opponent
        var degree = Array(repeating: Array(repeating: Array(repeating: 0, count: 2), count: n), count: n)
        
        // compute out-degree for each state
        for m in 0..<n {
            for c in 0..<n {
                degree[m][c][0] = graph[m].count                     // mouse's turn
                var cnt = 0                                          // cat's turn (cannot go to hole)
                for nxt in graph[c] where nxt != 0 { cnt += 1 }
                degree[m][c][1] = cnt
            }
        }
        
        struct State {
            let m: Int
            let c: Int
            let t: Int   // 0 mouse turn, 1 cat turn
        }
        var queue = [State]()
        var qIdx = 0
        
        // terminal states
        for i in 0..<n {
            for turn in 0...1 {
                // mouse reaches hole -> mouse wins
                result[0][i][turn] = MOUSE
                queue.append(State(m: 0, c: i, t: turn))
                
                // cat catches mouse (except when both at hole, which is impossible)
                if i != 0 {
                    result[i][i][turn] = CAT
                    queue.append(State(m: i, c: i, t: turn))
                }
            }
        }
        
        while qIdx < queue.count {
            let cur = queue[qIdx]
            qIdx += 1
            let mPos = cur.m
            let cPos = cur.c
            let turn = cur.t
            let curRes = result[mPos][cPos][turn]
            
            // find all parent states that can move to (mPos, cPos, turn)
            if turn == 0 { // mouse's turn now -> previous move was by cat
                for prevCat in graph[cPos] where prevCat != 0 {
                    let pm = mPos
                    let pc = prevCat
                    let pTurn = 1   // it was cat's turn before moving to cPos
                    if result[pm][pc][pTurn] != DRAW { continue }
                    
                    if (curRes == MOUSE && pTurn == 0) || (curRes == CAT && pTurn == 1) {
                        result[pm][pc][pTurn] = curRes
                        queue.append(State(m: pm, c: pc, t: pTurn))
                    } else {
                        degree[pm][pc][pTurn] -= 1
                        if degree[pm][pc][pTurn] == 0 {
                            let win = (pTurn == 0) ? CAT : MOUSE
                            result[pm][pc][pTurn] = win
                            queue.append(State(m: pm, c: pc, t: pTurn))
                        }
                    }
                }
            } else { // cat's turn now -> previous move was by mouse
                for prevMouse in graph[mPos] {
                    let pm = prevMouse
                    let pc = cPos
                    let pTurn = 0   // it was mouse's turn before moving to mPos
                    if result[pm][pc][pTurn] != DRAW { continue }
                    
                    if (curRes == MOUSE && pTurn == 0) || (curRes == CAT && pTurn == 1) {
                        result[pm][pc][pTurn] = curRes
                        queue.append(State(m: pm, c: pc, t: pTurn))
                    } else {
                        degree[pm][pc][pTurn] -= 1
                        if degree[pm][pc][pTurn] == 0 {
                            let win = (pTurn == 0) ? CAT : MOUSE
                            result[pm][pc][pTurn] = win
                            queue.append(State(m: pm, c: pc, t: pTurn))
                        }
                    }
                }
            }
        }
        
        return result[1][2][0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun catMouseGame(graph: Array<IntArray>): Int {
        val n = graph.size
        val DRAW = 0
        val MOUSE = 1
        val CAT = 2
        val MOUSE_TURN = 0
        val CAT_TURN = 1

        // dp[mouse][cat][turn] = result
        val dp = Array(n) { Array(n) { IntArray(2) } }
        // degree counts remaining moves that are not yet known to lead to a win for the player
        val degree = Array(n) { Array(n) { IntArray(2) } }

        for (m in 0 until n) {
            for (c in 0 until n) {
                degree[m][c][MOUSE_TURN] = graph[m].size
                var cnt = 0
                for (next in graph[c]) if (next != 0) cnt++
                degree[m][c][CAT_TURN] = cnt
            }
        }

        val queue: ArrayDeque<Triple<Int, Int, Int>> = ArrayDeque()

        // terminal states: mouse at hole -> Mouse wins
        for (c in 0 until n) {
            if (dp[0][c][MOUSE_TURN] == DRAW) {
                dp[0][c][MOUSE_TURN] = MOUSE
                queue.add(Triple(0, c, MOUSE_TURN))
            }
            if (dp[0][c][CAT_TURN] == DRAW) {
                dp[0][c][CAT_TURN] = MOUSE
                queue.add(Triple(0, c, CAT_TURN))
            }
        }

        // terminal states: cat catches mouse -> Cat wins (mouse not at hole)
        for (m in 1 until n) {
            if (dp[m][m][MOUSE_TURN] == DRAW) {
                dp[m][m][MOUSE_TURN] = CAT
                queue.add(Triple(m, m, MOUSE_TURN))
            }
            if (dp[m][m][CAT_TURN] == DRAW) {
                dp[m][m][CAT_TURN] = CAT
                queue.add(Triple(m, m, CAT_TURN))
            }
        }

        while (queue.isNotEmpty()) {
            val (mousePos, catPos, turn) = queue.removeFirst()
            val result = dp[mousePos][catPos][turn]

            // Find all parent states that can move to (mousePos, catPos, turn)
            if (turn == MOUSE_TURN) {
                // Previous move was by Cat
                val prevTurn = CAT_TURN
                for (prevCat in graph[catPos]) {
                    if (prevCat == 0) continue // cat cannot be at the hole
                    if (dp[mousePos][prevCat][prevTurn] != DRAW) continue

                    if (result == CAT) {
                        dp[mousePos][prevCat][prevTurn] = CAT
                        queue.add(Triple(mousePos, prevCat, prevTurn))
                    } else {
                        degree[mousePos][prevCat][prevTurn]--
                        if (degree[mousePos][prevCat][prevTurn] == 0) {
                            dp[mousePos][prevCat][prevTurn] = MOUSE
                            queue.add(Triple(mousePos, prevCat, prevTurn))
                        }
                    }
                }
            } else { // turn == CAT_TURN
                // Previous move was by Mouse
                val prevTurn = MOUSE_TURN
                for (prevMouse in graph[mousePos]) {
                    if (dp[prevMouse][catPos][prevTurn] != DRAW) continue

                    if (result == MOUSE) {
                        dp[prevMouse][catPos][prevTurn] = MOUSE
                        queue.add(Triple(prevMouse, catPos, prevTurn))
                    } else {
                        degree[prevMouse][catPos][prevTurn]--
                        if (degree[prevMouse][catPos][prevTurn] == 0) {
                            dp[prevMouse][catPos][prevTurn] = CAT
                            queue.add(Triple(prevMouse, catPos, prevTurn))
                        }
                    }
                }
            }
        }

        return dp[1][2][MOUSE_TURN]
    }
}
```

## Dart

```dart
class Solution {
  int catMouseGame(List<List<int>> graph) {
    const int MOUSE_WIN = 1;
    const int CAT_WIN = 2;
    int n = graph.length;

    // dp[m][c][t] : result of state (mouse=m, cat=c, turn=t) where t=0 mouse's turn, t=1 cat's turn
    List<List<List<int>>> dp = List.generate(
        n, (_) => List.generate(n, (_) => List.filled(2, 0)));

    // degree[m][c][t] : number of moves from state (m,c,t)
    List<List<List<int>>> degree = List.generate(
        n, (_) => List.generate(n, (_) => List.filled(2, 0)));

    for (int m = 0; m < n; ++m) {
      for (int c = 0; c < n; ++c) {
        // mouse moves
        degree[m][c][0] = graph[m].length;
        // cat moves (cannot go to hole 0)
        int cnt = 0;
        for (int nb in graph[c]) {
          if (nb != 0) cnt++;
        }
        degree[m][c][1] = cnt;
      }
    }

    List<List<int>> queue = [];
    // Initialize terminal states
    for (int c = 0; c < n; ++c) {
      dp[0][c][0] = MOUSE_WIN;
      dp[0][c][1] = MOUSE_WIN;
      queue.add([0, c, 0]);
      queue.add([0, c, 1]);
    }
    for (int m = 1; m < n; ++m) {
      dp[m][m][0] = CAT_WIN;
      dp[m][m][1] = CAT_WIN;
      queue.add([m, m, 0]);
      queue.add([m, m, 1]);
    }

    int head = 0;
    while (head < queue.length) {
      var cur = queue[head++];
      int mouse = cur[0];
      int cat = cur[1];
      int turn = cur[2];
      int result = dp[mouse][cat][turn];

      // Find all parent states that can move to (mouse,cat,turn)
      if (turn == 0) {
        // Current turn is mouse, so previous turn was cat
        // Cat moved from some prevCat -> cat
        for (int prevCat in graph[cat]) {
          if (prevCat == 0) continue; // cat cannot be at hole
          int prevMouse = mouse;
          int prevTurn = 1; // cat's turn
          if (dp[prevMouse][prevCat][prevTurn] != 0) continue;

          if (result == CAT_WIN) {
            dp[prevMouse][prevCat][prevTurn] = CAT_WIN;
            queue.add([prevMouse, prevCat, prevTurn]);
          } else {
            degree[prevMouse][prevCat][prevTurn]--;
            if (degree[prevMouse][prevCat][prevTurn] == 0) {
              dp[prevMouse][prevCat][prevTurn] = MOUSE_WIN;
              queue.add([prevMouse, prevCat, prevTurn]);
            }
          }
        }
      } else {
        // Current turn is cat, previous was mouse
        for (int prevMouse in graph[mouse]) {
          int prevCat = cat;
          int prevTurn = 0; // mouse's turn
          if (dp[prevMouse][prevCat][prevTurn] != 0) continue;

          if (result == MOUSE_WIN) {
            dp[prevMouse][prevCat][prevTurn] = MOUSE_WIN;
            queue.add([prevMouse, prevCat, prevTurn]);
          } else {
            degree[prevMouse][prevCat][prevTurn]--;
            if (degree[prevMouse][prevCat][prevTurn] == 0) {
              dp[prevMouse][prevCat][prevTurn] = CAT_WIN;
              queue.add([prevMouse, prevCat, prevTurn]);
            }
          }
        }
      }
    }

    return dp[1][2][0];
  }
}
```

## Golang

```go
package main

func catMouseGame(graph [][]int) int {
	type state struct{ m, c, t int }

	n := len(graph)
	// dp[m][c][t]: 0 = draw/unknown, 1 = mouse wins, 2 = cat wins
	dp := make([][][]int, n)
	deg := make([][][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]int, n)
		deg[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]int, 2)
			deg[i][j] = make([]int, 2)
		}
	}

	// Initialize degrees
	for m := 0; m < n; m++ {
		for c := 0; c < n; c++ {
			deg[m][c][0] = len(graph[m]) // mouse's turn
			cnt := 0
			for _, nb := range graph[c] { // cat's turn, cannot move to hole (0)
				if nb != 0 {
					cnt++
				}
			}
			deg[m][c][1] = cnt
		}
	}

	queue := make([]state, 0)
	// Initialize terminal states
	for m := 0; m < n; m++ {
		for c := 0; c < n; c++ {
			if m == 0 { // mouse already in hole -> mouse wins
				dp[m][c][0] = 1
				dp[m][c][1] = 1
				queue = append(queue, state{m, c, 0})
				queue = append(queue, state{m, c, 1})
			} else if m == c { // cat catches mouse -> cat wins (except hole case already handled)
				dp[m][c][0] = 2
				dp[m][c][1] = 2
				queue = append(queue, state{m, c, 0})
				queue = append(queue, state{m, c, 1})
			}
		}
	}

	head := 0
	for head < len(queue) {
		cur := queue[head]
		head++
		res := dp[cur.m][cur.c][cur.t]

		if cur.t == 0 { // current turn was mouse, so parent turn is cat
			pt := 1
			pc := cur.c
			for _, pm := range graph[cur.m] {
				if dp[pm][pc][pt] != 0 {
					continue
				}
				if res == 2 { // cat can force a win from this child
					dp[pm][pc][pt] = 2
					queue = append(queue, state{pm, pc, pt})
				} else {
					deg[pm][pc][pt]--
					if deg[pm][pc][pt] == 0 {
						// all moves lead to mouse win -> cat loses
						dp[pm][pc][pt] = 1
						queue = append(queue, state{pm, pc, pt})
					}
				}
			}
		} else { // current turn was cat, parent turn is mouse
			pt := 0
			pm := cur.m
			for _, pc := range graph[cur.c] {
				if pc == 0 { // cat cannot be in the hole
					continue
				}
				if dp[pm][pc][pt] != 0 {
					continue
				}
				if res == 1 { // mouse can force a win from this child
					dp[pm][pc][pt] = 1
					queue = append(queue, state{pm, pc, pt})
				} else {
					deg[pm][pc][pt]--
					if deg[pm][pc][pt] == 0 {
						// all moves lead to cat win -> mouse loses
						dp[pm][pc][pt] = 2
						queue = append(queue, state{pm, pc, pt})
					}
				}
			}
		}
	}

	return dp[1][2][0]
}
```

## Ruby

```ruby
def cat_mouse_game(graph)
  n = graph.length
  DRAW = 0
  MOUSE = 1
  CAT = 2

  result = Array.new(n) { Array.new(n) { [DRAW, DRAW] } }
  degree = Array.new(n) { Array.new(n) { [0, 0] } }

  n.times do |m|
    n.times do |c|
      degree[m][c][0] = graph[m].size
      cnt = 0
      graph[c].each { |next_node| cnt += 1 unless next_node == 0 }
      degree[m][c][1] = cnt
    end
  end

  queue = []
  head = 0

  n.times do |m|
    n.times do |c|
      if m == 0
        result[0][c][0] = MOUSE
        result[0][c][1] = MOUSE
        queue << [0, c, 0]
        queue << [0, c, 1]
      elsif m == c && m != 0
        result[m][m][0] = CAT
        result[m][m][1] = CAT
        queue << [m, m, 0]
        queue << [m, m, 1]
      end
    end
  end

  while head < queue.size
    m, c, t = queue[head]
    head += 1
    cur = result[m][c][t]

    if t == 0 # Mouse just moved; previous turn was Cat
      prev_turn = 1
      graph[c].each do |pc|
        next if pc == 0
        next unless result[m][pc][prev_turn] == DRAW
        if cur == CAT
          result[m][pc][prev_turn] = CAT
          queue << [m, pc, prev_turn]
        else
          degree[m][pc][prev_turn] -= 1
          if degree[m][pc][prev_turn] == 0
            result[m][pc][prev_turn] = MOUSE
            queue << [m, pc, prev_turn]
          end
        end
      end
    else # t == 1, Cat just moved; previous turn was Mouse
      prev_turn = 0
      graph[m].each do |pm|
        next unless result[pm][c][prev_turn] == DRAW
        if cur == MOUSE
          result[pm][c][prev_turn] = MOUSE
          queue << [pm, c, prev_turn]
        else
          degree[pm][c][prev_turn] -= 1
          if degree[pm][c][prev_turn] == 0
            result[pm][c][prev_turn] = CAT
            queue << [pm, c, prev_turn]
          end
        end
      end
    end
  end

  result[1][2][0]
end
```

## Scala

```scala
object Solution {
    def catMouseGame(graph: Array[Array[Int]]): Int = {
        val n = graph.length
        val DRAW = 0
        val MOUSE_WIN = 1
        val CAT_WIN = 2

        // result[m][c][turn]
        val result = Array.ofDim[Int](n, n, 2)
        // degree of moves from each state
        val degree = Array.ofDim[Int](n, n, 2)

        for (m <- 0 until n; c <- 0 until n) {
            degree(m)(c)(0) = graph(m).length
            var cnt = 0
            for (next <- graph(c)) if (next != 0) cnt += 1
            degree(m)(c)(1) = cnt
        }

        import scala.collection.mutable.ArrayDeque
        val queue = ArrayDeque[(Int, Int, Int)]()

        // Mouse reaches hole -> mouse wins
        for (c <- 0 until n; t <- 0 to 1) {
            if (result(0)(c)(t) == DRAW) {
                result(0)(c)(t) = MOUSE_WIN
                queue.append((0, c, t))
            }
        }

        // Cat catches mouse -> cat wins (except when both at hole)
        for (m <- 1 until n; t <- 0 to 1) {
            if (result(m)(m)(t) == DRAW) {
                result(m)(m)(t) = CAT_WIN
                queue.append((m, m, t))
            }
        }

        while (queue.nonEmpty) {
            val (m, c, turn) = queue.removeHead()
            val curRes = result(m)(c)(turn)

            if (turn == 0) { // mouse just moved, previous was cat's move
                for (prevC <- graph(c) if prevC != 0) {
                    val pm = m
                    val pc = prevC
                    val pTurn = 1
                    if (result(pm)(pc)(pTurn) == DRAW) {
                        if (curRes == CAT_WIN) {
                            result(pm)(pc)(pTurn) = CAT_WIN
                            queue.append((pm, pc, pTurn))
                        } else { // curRes == MOUSE_WIN
                            degree(pm)(pc)(pTurn) -= 1
                            if (degree(pm)(pc)(pTurn) == 0) {
                                result(pm)(pc)(pTurn) = MOUSE_WIN
                                queue.append((pm, pc, pTurn))
                            }
                        }
                    }
                }
            } else { // turn == 1, cat just moved, previous was mouse's move
                for (prevM <- graph(m)) {
                    val pm = prevM
                    val pc = c
                    val pTurn = 0
                    if (result(pm)(pc)(pTurn) == DRAW) {
                        if (curRes == MOUSE_WIN) {
                            result(pm)(pc)(pTurn) = MOUSE_WIN
                            queue.append((pm, pc, pTurn))
                        } else { // curRes == CAT_WIN
                            degree(pm)(pc)(pTurn) -= 1
                            if (degree(pm)(pc)(pTurn) == 0) {
                                result(pm)(pc)(pTurn) = CAT_WIN
                                queue.append((pm, pc, pTurn))
                            }
                        }
                    }
                }
            }
        }

        result(1)(2)(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn cat_mouse_game(graph: Vec<Vec<i32>>) -> i32 {
        let n = graph.len();
        // convert to usize adjacency list
        let mut g: Vec<Vec<usize>> = vec![vec![]; n];
        for i in 0..n {
            g[i] = graph[i].iter().map(|&x| x as usize).collect();
        }

        const DRAW: u8 = 0;
        const MOUSE_WIN: u8 = 1;
        const CAT_WIN: u8 = 2;

        // color[mouse][cat][turn]
        let mut color = vec![vec![[DRAW; 2]; n]; n];
        // degree[mouse][cat][turn]
        let mut degree = vec![vec![[0usize; 2]; n]; n];

        for m in 0..n {
            for c in 0..n {
                degree[m][c][0] = g[m].len(); // mouse's turn
                let mut cnt = 0;
                for &next in &g[c] {
                    if next != 0 {
                        cnt += 1; // cat cannot move to hole
                    }
                }
                degree[m][c][1] = cnt; // cat's turn
            }
        }

        use std::collections::VecDeque;
        let mut q: VecDeque<(usize, usize, usize)> = VecDeque::new();

        // terminal states: mouse at hole -> mouse wins
        for c in 0..n {
            if color[0][c][0] == DRAW {
                color[0][c][0] = MOUSE_WIN;
                q.push_back((0, c, 0));
            }
            if color[0][c][1] == DRAW {
                color[0][c][1] = MOUSE_WIN;
                q.push_back((0, c, 1));
            }
        }

        // terminal states: cat catches mouse (except hole) -> cat wins
        for m in 1..n {
            if color[m][m][0] == DRAW {
                color[m][m][0] = CAT_WIN;
                q.push_back((m, m, 0));
            }
            if color[m][m][1] == DRAW {
                color[m][m][1] = CAT_WIN;
                q.push_back((m, m, 1));
            }
        }

        while let Some((m, c, t)) = q.pop_front() {
            let cur_res = color[m][c][t];
            if t == 0 {
                // mouse just moved, parent was cat's turn
                for &prev_c in &g[c] {
                    if prev_c == 0 { continue; } // cat cannot be at hole
                    let pm = m;
                    let pt = 1; // cat's turn
                    if color[pm][prev_c][pt] != DRAW {
                        continue;
                    }
                    if cur_res == CAT_WIN {
                        color[pm][prev_c][pt] = CAT_WIN;
                        q.push_back((pm, prev_c, pt));
                    } else {
                        degree[pm][prev_c][pt] -= 1;
                        if degree[pm][prev_c][pt] == 0 {
                            // all moves lead to mouse win -> cat loses
                            color[pm][prev_c][pt] = MOUSE_WIN;
                            q.push_back((pm, prev_c, pt));
                        }
                    }
                }
            } else {
                // cat just moved, parent was mouse's turn
                for &prev_m in &g[m] {
                    let pm = prev_m;
                    let pc = c;
                    let pt = 0; // mouse's turn
                    if color[pm][pc][pt] != DRAW {
                        continue;
                    }
                    if cur_res == MOUSE_WIN {
                        color[pm][pc][pt] = MOUSE_WIN;
                        q.push_back((pm, pc, pt));
                    } else {
                        degree[pm][pc][pt] -= 1;
                        if degree[pm][pc][pt] == 0 {
                            // all moves lead to cat win -> mouse loses
                            color[pm][pc][pt] = CAT_WIN;
                            q.push_back((pm, pc, pt));
                        }
                    }
                }
            }
        }

        color[1][2][0] as i32
    }
}
```

## Racket

```racket
(define/contract (cat-mouse-game graph)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length graph))
         ;; convert adjacency list to vector of vectors for fast access
         (gvec (list->vector (map list->vector graph)))
         ;; result[m][c][t] = -1 unknown, 0 mouse wins, 1 cat wins
         (result (let ([outer (make-vector n)])
                   (for ([i (in-range n)])
                     (let ([mid (make-vector n)])
                       (for ([j (in-range n)])
                         (vector-set! mid j (vector -1 -1))) ; turn 0,1
                       (vector-set! outer i mid)))
                   outer))
         ;; degree[m][c][t] = number of moves from this state
         (degree (let ([outer (make-vector n)])
                   (for ([i (in-range n)])
                     (let ([mid (make-vector n)])
                       (for ([j (in-range n)])
                         (vector-set! mid j (vector 0 0))) ; turn 0,1
                       (vector-set! outer i mid)))
                   outer))
         ;; queue for BFS
         (max-queue (* n n 2))
         (queue (make-vector max-queue))
         (head 0)
         (tail 0))

    ;; helper to set/get result and degree
    (define (set-result! m c t v)
      (vector-set! (vector-ref (vector-ref result m) c) t v))
    (define (get-result m c t)
      (vector-ref (vector-ref result m) c t))
    (define (set-degree! m c t v)
      (vector-set! (vector-ref (vector-ref degree m) c) t v))
    (define (dec-degree! m c t)
      (let* ((vec (vector-ref (vector-ref degree m) c))
             (old (vector-ref vec t)))
        (vector-set! vec t (- old 1))))
    (define (get-degree m c t)
      (vector-ref (vector-ref degree m) c t))

    ;; enqueue function
    (define (enqueue state)
      (vector-set! queue tail state)
      (set! tail (+ tail 1)))

    ;; initialize degrees and terminal states
    (for ([m (in-range n)])
      (for ([c (in-range n)])
        (for ([t (in-list '(0 1))])
          (cond
            [(= t 0) ; mouse turn
             (set-degree! m c t (vector-length (vector-ref gvec m)))]
            [else   ; cat turn
             (let* ((neighbors (vector-ref gvec c))
                    (cnt (for/sum ([nb (in-vector neighbors)])
                           (if (= nb 0) 0 1))))
               (set-degree! m c t cnt))]))))

    ;; enqueue terminal states
    (for ([m (in-range n)]
          [c (in-range n)])
      (cond
        [(= m 0)
         (for ([t (in-list '(0 1))])
           (when (= (get-result m c t) -1)
             (set-result! m c t 0)
             (enqueue (vector m c t))))]
        [(= m c)
         (for ([t (in-list '(0 1))])
           (when (= (get-result m c t) -1)
             (set-result! m c t 1)
             (enqueue (vector m c t))))]))

    ;; BFS propagation
    (let loop ()
      (when (< head tail)
        (define state (vector-ref queue head))
        (set! head (+ head 1))
        (define m (vector-ref state 0))
        (define c (vector-ref state 1))
        (define t (vector-ref state 2))
        (define cur-res (get-result m c t))

        ;; find parents
        (if (= t 0) ; current turn is mouse, so parent was cat's move
            (for ([pc (in-vector (vector-ref gvec c))])
              (when (not (= pc 0)) ; cat cannot be at hole
                (define pm m)
                (define pt 1) ; cat's turn in parent
                (when (= (get-result pm pc pt) -1)
                  (if (and (= cur-res 1) (= pt 1)) ; cat can force win
                      (begin
                        (set-result! pm pc pt cur-res)
                        (enqueue (vector pm pc pt)))
                      (begin
                        (dec-degree! pm pc pt)
                        (when (= (get-degree pm pc pt) 0)
                          (define win (if (= pt 0) 1 0)) ; opponent wins
                          (set-result! pm pc pt win)
                          (enqueue (vector pm pc pt))))))))
            ;; t == 1, current turn is cat, parent was mouse's move
            (for ([pm (in-vector (vector-ref gvec m))])
              (define pc c)
              (define pt 0) ; mouse's turn in parent
              (when (= (get-result pm pc pt) -1)
                (if (and (= cur-res 0) (= pt 0)) ; mouse can force win
                    (begin
                      (set-result! pm pc pt cur-res)
                      (enqueue (vector pm pc pt)))
                    (begin
                      (dec-degree! pm pc pt)
                      (when (= (get-degree pm pc pt) 0)
                        (define win (if (= pt 0) 1 0)) ; opponent wins
                        (set-result! pm pc pt win)
                        (enqueue (vector pm pc pt)))))))))
        (loop)))

    ;; final answer from start state (mouse at 1, cat at 2, mouse turn)
    (let ((ans (get-result 1 2 0)))
      (if (= ans -1) 2 ans))))
```

## Erlang

```erlang
-spec cat_mouse_game(Graph :: [[integer()]]) -> integer().
cat_mouse_game(Graph) ->
    N = length(Graph),
    MouseWin = 0,
    CatWin = 1,
    Draw = 2,

    Adj = Graph,
    DegreeMap = build_degree(N, Adj),

    % result map stores only resolved states (non-draw)
    Result0 = #{},
    Queue0 = queue:new(),
    {Result1, Queue1} = init_terminal_states(N, MouseWin, CatWin, Result0, Queue0),

    FinalResult = bfs(Adj, DegreeMap, Result1, Queue1, MouseWin, CatWin, Draw),
    maps:get({1, 2, 0}, FinalResult).

build_degree(N, Adj) ->
    lists:foldl(fun(M, AccM) ->
        lists:foldl(fun(C, AccC) ->
            MouseMoves = length(lists:nth(M + 1, Adj)),
            CatNeighbors = [X || X <- lists:nth(C + 1, Adj), X =/= 0],
            CatMoves = length(CatNeighbors),
            Acc1 = maps:put({M, C, 0}, MouseMoves, AccC),
            maps:put({M, C, 1}, CatMoves, Acc1)
        end, AccM, lists:seq(0, N - 1))
    end, #{}, lists:seq(0, N - 1)).

init_terminal_states(N, MouseWin, CatWin, ResultMap, Queue) ->
    lists:foldl(fun(M, {ResAcc, QAcc}) ->
        lists:foldl(fun(C, {ResAcc2, QAcc2}) ->
            lists:foldl(fun(T, {ResAcc3, QAcc3}) ->
                case {M == 0, M == C, M =/= 0} of
                    {true, _, _} ->
                        Key = {M, C, T},
                        NewRes = maps:put(Key, MouseWin, ResAcc3),
                        NewQ = queue:in(Key, QAcc3),
                        {NewRes, NewQ};
                    {false, true, true} ->
                        Key = {M, C, T},
                        NewRes = maps:put(Key, CatWin, ResAcc3),
                        NewQ = queue:in(Key, QAcc3),
                        {NewRes, NewQ};
                    _ ->
                        {ResAcc3, QAcc3}
                end
            end, {ResAcc2, QAcc2}, [0,1])
        end, {ResAcc, QAcc}, lists:seq(0, N - 1))
    end, {ResultMap, Queue}, lists:seq(0, N - 1)).

bfs(Adj, DegMap, ResMap, Queue, MouseWin, CatWin, Draw) ->
    case queue:out(Queue) of
        {empty, _} -> ResMap;
        {{value, State = {M, C, T}}, RestQ} ->
            R = maps:get(State, ResMap),
            ParentTurn = 1 - T,
            Parents = get_parents(State, Adj),
            {NewRes, NewDeg, NewQ} =
                process_parents(Parents, R, ParentTurn, ResMap, DegMap, RestQ, MouseWin, CatWin, Draw),
            bfs(Adj, NewDeg, NewRes, NewQ, MouseWin, CatWin, Draw)
    end.

get_parents({M, C, T}, Adj) ->
    PT = 1 - T,
    case PT of
        0 -> % mouse moved last
            PrevMouse = lists:nth(M + 1, Adj),
            [{Pm, C, 0} || Pm <- PrevMouse];
        1 -> % cat moved last
            PrevCat = [Pc || Pc <- lists:nth(C + 1, Adj), Pc =/= 0],
            [{M, Pc, 1} || Pc <- PrevCat]
    end.

process_parents([], _R, _PT, ResMap, DegMap, Queue, _MouseWin, _CatWin, _Draw) ->
    {ResMap, DegMap, Queue};
process_parents([P | Rest], R, PT, ResMap, DegMap, Queue, MouseWin, CatWin, Draw) ->
    case maps:get(P, ResMap, Draw) of
        Draw ->
            if R =:= PT ->
                    NewRes = maps:put(P, PT, ResMap),
                    NewQ = queue:in(P, Queue),
                    process_parents(Rest, R, PT, NewRes, DegMap, NewQ, MouseWin, CatWin, Draw);
               true ->
                    OldDeg = maps:get(P, DegMap),
                    NewDegVal = OldDeg - 1,
                    DegMap2 = maps:put(P, NewDegVal, DegMap),
                    if NewDegVal =:= 0 ->
                            Opp = 1 - PT,
                            NewRes2 = maps:put(P, Opp, ResMap),
                            NewQ2 = queue:in(P, Queue),
                            process_parents(Rest, R, PT, NewRes2, DegMap2, NewQ2, MouseWin, CatWin, Draw);
                       true ->
                            process_parents(Rest, R, PT, ResMap, DegMap2, Queue, MouseWin, CatWin, Draw)
                    end
            end;
        _Other -> % already resolved
            process_parents(Rest, R, PT, ResMap, DegMap, Queue, MouseWin, CatWin, Draw)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec cat_mouse_game(graph :: [[integer]]) :: integer
  def cat_mouse_game(graph) do
    n = length(graph)

    # degree of each state (mouse,cat,turn)
    degree =
      for m <- 0..(n - 1), c <- 0..(n - 1), t <- [0, 1], into: %{} do
        key = {m, c, t}

        cond do
          m == 0 or (m == c and m != 0) ->
            {key, 0}

          t == 0 ->
            {key, length(Enum.at(graph, m))}

          true ->
            cnt = Enum.count(Enum.at(graph, c), fn nb -> nb != 0 end)
            {key, cnt}
        end
      end

    # result map: 0 unknown (not stored), 1 mouse wins, 2 cat wins
    {result, queue} =
      Enum.reduce(0..(n - 1), {%{}, :queue.new()}, fn m, {res_acc, q_acc} ->
        Enum.reduce(0..(n - 1), {res_acc, q_acc}, fn c, {res_inner, q_inner} ->
          cond do
            m == 0 ->
              {res_tmp, q_tmp} = set_result(res_inner, q_inner, {m, c, 0}, 1)
              set_result(res_tmp, q_tmp, {m, c, 1}, 1)

            m == c and m != 0 ->
              {res_tmp, q_tmp} = set_result(res_inner, q_inner, {m, c, 0}, 2)
              set_result(res_tmp, q_tmp, {m, c, 1}, 2)

            true ->
              {res_inner, q_inner}
          end
        end)
      end)

    final_result = bfs(queue, result, degree, graph, n)
    Map.get(final_result, {1, 2, 0}, 0)
  end

  defp set_result(res, q, state, val) do
    if Map.has_key?(res, state) do
      {res, q}
    else
      {Map.put(res, state, val), :queue.in(state, q)}
    end
  end

  defp bfs(queue, result, degree, graph, n) do
    case :queue.out(queue) do
      {:empty, _} ->
        result

      {{:value, {m, c, t}}, q_rest} ->
        cur_res = Map.fetch!(result, {m, c, t})
        parents = get_parents(m, c, t, graph, n)

        {new_result, new_queue, new_degree} =
          Enum.reduce(parents, {result, q_rest, degree}, fn parent,
                                                          {res_acc, q_acc, deg_acc} ->
            if Map.has_key?(res_acc, parent) do
              {res_acc, q_acc, deg_acc}
            else
              {pm, pc, pt} = parent
              player_win = if pt == 0, do: 1, else: 2

              if cur_res == player_win do
                # parent can force a win for the player whose turn it is
                {
                  Map.put(res_acc, parent, player_win),
                  :queue.in(parent, q_acc),
                  deg_acc
                }
              else
                # move leads to opponent's win; decrement degree
                deg_key = parent
                deg_val = Map.get(deg_acc, deg_key) - 1
                deg_map = Map.put(deg_acc, deg_key, deg_val)

                if deg_val == 0 do
                  opp_win = if pt == 0, do: 2, else: 1

                  {
                    Map.put(res_acc, parent, opp_win),
                    :queue.in(parent, q_acc),
                    deg_map
                  }
                else
                  {res_acc, q_acc, deg_map}
                end
              end
            end
          end)

        bfs(new_queue, new_result, new_degree, graph, n)
    end
  end

  defp get_parents(m, c, t, graph, n) do
    if t == 0 do
      # mouse's turn now -> previous move was by cat
      for pc <- 0..(n - 1),
          pc != 0,
          Enum.member?(Enum.at(graph, pc), c),
          do: {m, pc, 1}
    else
      # cat's turn now -> previous move was by mouse
      for pm <- 0..(n - 1),
          Enum.member?(Enum.at(graph, pm), m),
          do: {pm, c, 0}
    end
  end
end
```

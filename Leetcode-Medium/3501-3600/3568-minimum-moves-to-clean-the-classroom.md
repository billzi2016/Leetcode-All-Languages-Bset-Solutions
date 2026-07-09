# 3568. Minimum Moves to Clean the Classroom

## Cpp

```cpp
class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size();
        int n = classroom[0].size();
        int sx=-1, sy=-1;
        vector<vector<int>> idx(m, vector<int>(n, -1));
        int lcnt = 0;
        for (int i=0;i<m;++i){
            for (int j=0;j<n;++j){
                char c = classroom[i][j];
                if (c=='S'){
                    sx=i; sy=j;
                } else if (c=='L'){
                    idx[i][j]=lcnt++;
                }
            }
        }
        int fullMask = (1<<lcnt)-1;
        const int INF_NEG = -1;
        vector<vector<vector<int>>> best(m, vector<vector<int>>(n, vector<int>(1<<lcnt, INF_NEG)));
        struct State{
            int x,y,mask,e,steps;
        };
        queue<State> q;
        q.push({sx,sy,0,energy,0});
        best[sx][sy][0]=energy;
        int dirs[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
        while(!q.empty()){
            State cur = q.front(); q.pop();
            if (cur.mask==fullMask) return cur.steps;
            // cannot move further if no energy left
            if (cur.e==0) continue;
            for (auto &d:dirs){
                int nx=cur.x+d[0];
                int ny=cur.y+d[1];
                if (nx<0||ny<0||nx>=m||ny>=n) continue;
                char nc = classroom[nx][ny];
                if (nc=='X') continue;
                int ne = cur.e-1; // spend energy to move
                if (ne<0) continue;
                int nmask = cur.mask;
                if (nc=='L'){
                    int id = idx[nx][ny];
                    nmask |= (1<<id);
                }
                if (nc=='R'){
                    ne = energy; // reset upon arrival
                }
                if (best[nx][ny][nmask] >= ne) continue;
                best[nx][ny][nmask]=ne;
                q.push({nx,ny,nmask,ne,cur.steps+1});
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();
        char[][] grid = new char[m][n];
        for (int i = 0; i < m; i++) grid[i] = classroom[i].toCharArray();

        int sx = -1, sy = -1;
        int lCount = 0;
        int[][] lIdx = new int[m][n];
        for (int i = 0; i < m; i++) {
            java.util.Arrays.fill(lIdx[i], -1);
            for (int j = 0; j < n; j++) {
                char c = grid[i][j];
                if (c == 'S') {
                    sx = i;
                    sy = j;
                } else if (c == 'L') {
                    lIdx[i][j] = lCount++;
                }
            }
        }

        int fullMask = (1 << lCount) - 1;
        if (fullMask == 0) return 0; // no litter to collect

        int[][][] best = new int[m][n][1 << lCount];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                java.util.Arrays.fill(best[i][j], -1);
            }
        }

        class State {
            int x, y, mask, e, steps;
            State(int x, int y, int mask, int e, int steps) {
                this.x = x; this.y = y; this.mask = mask; this.e = e; this.steps = steps;
            }
        }

        java.util.ArrayDeque<State> q = new java.util.ArrayDeque<>();
        best[sx][sy][0] = energy;
        q.add(new State(sx, sy, 0, energy, 0));

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        while (!q.isEmpty()) {
            State cur = q.poll();
            if (cur.mask == fullMask) return cur.steps;

            // If current cell is a reset area, ensure energy is refreshed
            int curEnergy = cur.e;
            if (grid[cur.x][cur.y] == 'R') curEnergy = energy;

            for (int dir = 0; dir < 4; dir++) {
                int nx = cur.x + dx[dir];
                int ny = cur.y + dy[dir];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                char c = grid[nx][ny];
                if (c == 'X') continue; // obstacle

                if (curEnergy == 0) continue; // cannot move without energy
                int ne = curEnergy - 1;
                int nmask = cur.mask;

                if (c == 'L') {
                    int idx = lIdx[nx][ny];
                    nmask |= (1 << idx);
                }
                if (c == 'R') {
                    ne = energy; // reset after arriving
                }

                if (best[nx][ny][nmask] >= ne) continue;
                best[nx][ny][nmask] = ne;
                q.add(new State(nx, ny, nmask, ne, cur.steps + 1));
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        from collections import deque

        m = len(classroom)
        n = len(classroom[0])
        maxE = energy

        # locate start and litter cells
        l_idx = {}
        k = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    l_idx[(i, j)] = k
                    k += 1

        fullMask = (1 << k) - 1

        # bestEnergy[x][y][mask] = max remaining energy seen
        bestEnergy = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        dq = deque()
        dq.append((sx, sy, 0, maxE, 0))  # x, y, mask, cur_energy, steps
        bestEnergy[sx][sy][0] = maxE

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while dq:
            x, y, mask, e, steps = dq.popleft()
            if mask == fullMask:
                return steps

            # reset energy on recharge cell
            cur_e = e
            if classroom[x][y] == 'R':
                cur_e = maxE

            if cur_e == 0:
                continue  # cannot move further from non‑recharge cell with no energy

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                cell = classroom[nx][ny]
                if cell == 'X':
                    continue

                ne = cur_e - 1
                nmask = mask
                if cell == 'L':
                    idx = l_idx[(nx, ny)]
                    nmask |= (1 << idx)

                # store state only if we have more remaining energy than before
                if ne > bestEnergy[nx][ny][nmask]:
                    bestEnergy[nx][ny][nmask] = ne
                    dq.append((nx, ny, nmask, ne, steps + 1))

        return -1
```

## Python3

```python
import collections
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        sx = sy = -1
        litter_idx = {}
        k = 0
        for i in range(m):
            for j, ch in enumerate(classroom[i]):
                if ch == 'S':
                    sx, sy = i, j
                elif ch == 'L':
                    litter_idx[(i, j)] = k
                    k += 1

        full_mask = (1 << k) - 1
        # best[x][y][mask] = max remaining energy seen
        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        dq = collections.deque()
        dq.append((sx, sy, 0, energy, 0))
        best[sx][sy][0] = energy

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while dq:
            x, y, mask, e, steps = dq.popleft()
            if mask == full_mask:
                return steps
            if e == 0 and classroom[x][y] != 'R':
                continue  # cannot move further

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                ne = e - 1
                if ne < 0:
                    continue
                nmask = mask
                cell = classroom[nx][ny]
                if cell == 'L':
                    idx = litter_idx[(nx, ny)]
                    nmask |= (1 << idx)
                if cell == 'R':
                    ne = energy
                if best[nx][ny][nmask] >= ne:
                    continue
                best[nx][ny][nmask] = ne
                dq.append((nx, ny, nmask, ne, steps + 1))

        return -1
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minMoves(char** classroom, int classroomSize, int energy) {
    int m = classroomSize;
    int n = strlen(classroom[0]);
    int sx = -1, sy = -1;
    int idxMap[20][20];
    memset(idxMap, -1, sizeof(idxMap));
    int Lcnt = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            char c = classroom[i][j];
            if (c == 'S') { sx = i; sy = j; }
            else if (c == 'L') { idxMap[i][j] = Lcnt++; }
        }
    }

    int fullMask = (1 << Lcnt) - 1;

    static int best[20][20][1024];
    memset(best, -1, sizeof(best));

    struct Node {
        int x, y;
        int mask;
        int e;
        int steps;
    };

    int maxStates = m * n * (1 << Lcnt) + 5;
    struct Node* q = (struct Node*)malloc(maxStates * sizeof(struct Node));
    int head = 0, tail = 0;

    best[sx][sy][0] = energy;
    q[tail++] = (struct Node){sx, sy, 0, energy, 0};

    const int dx[4] = {1, -1, 0, 0};
    const int dy[4] = {0, 0, 1, -1};

    while (head < tail) {
        struct Node cur = q[head++];
        if (cur.mask == fullMask) {
            free(q);
            return cur.steps;
        }

        int curE = cur.e;
        if (classroom[cur.x][cur.y] == 'R' && curE < energy) curE = energy;

        for (int d = 0; d < 4; ++d) {
            int nx = cur.x + dx[d];
            int ny = cur.y + dy[d];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            char nc = classroom[nx][ny];
            if (nc == 'X') continue;
            if (curE == 0) continue;          // not enough energy to move
            int ne = curE - 1;                // spend energy for the step
            if (nc == 'R') ne = energy;       // reset on landing
            int nmask = cur.mask;
            if (idxMap[nx][ny] != -1) {
                nmask |= (1 << idxMap[nx][ny]);
            }
            if (ne <= best[nx][ny][nmask]) continue;
            best[nx][ny][nmask] = ne;
            q[tail++] = (struct Node){nx, ny, nmask, ne, cur.steps + 1};
        }
    }

    free(q);
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinMoves(string[] classroom, int energy) {
        int m = classroom.Length;
        int n = classroom[0].Length;
        char[,] grid = new char[m, n];
        int sx = -1, sy = -1;
        int lCount = 0;
        int[,] lIdx = new int[m, n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = classroom[i][j];
                grid[i, j] = c;
                if (c == 'S') { sx = i; sy = j; }
                if (c == 'L') {
                    lIdx[i, j] = lCount++;
                } else {
                    lIdx[i, j] = -1;
                }
            }
        }

        int fullMask = (1 << lCount) - 1;
        int maskSize = fullMask + 1;

        // best[x,y,mask] = max remaining energy seen
        int[,,] best = new int[m, n, maskSize];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < maskSize; k++) {
                    best[i, j, k] = -1;
                }
            }
        }

        var q = new Queue<State>();
        q.Enqueue(new State(sx, sy, 0, energy, 0));
        best[sx, sy, 0] = energy;

        int[] dx = new int[] { -1, 1, 0, 0 };
        int[] dy = new int[] { 0, 0, -1, 1 };

        while (q.Count > 0) {
            State cur = q.Dequeue();
            if (cur.Mask == fullMask) return cur.Steps;

            for (int dir = 0; dir < 4; dir++) {
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                char cell = grid[nx, ny];
                if (cell == 'X') continue;
                if (cur.Energy <= 0) continue; // cannot move further

                int ne = cur.Energy - 1;
                int nmask = cur.Mask;

                if (cell == 'L') {
                    int idx = lIdx[nx, ny];
                    if (idx >= 0) nmask |= (1 << idx);
                }

                if (cell == 'R') {
                    ne = energy; // reset after arriving
                }

                if (best[nx, ny, nmask] >= ne) continue;
                best[nx, ny, nmask] = ne;
                q.Enqueue(new State(nx, ny, nmask, ne, cur.Steps + 1));
            }
        }

        return -1;
    }

    private struct State {
        public int X;
        public int Y;
        public int Mask;
        public int Energy;
        public int Steps;
        public State(int x, int y, int mask, int energy, int steps) {
            X = x; Y = y; Mask = mask; Energy = energy; Steps = steps;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} classroom
 * @param {number} energy
 * @return {number}
 */
var minMoves = function(classroom, energy) {
    const m = classroom.length;
    const n = classroom[0].length;
    let sx = -1, sy = -1;
    const lPos = [];
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const ch = classroom[i][j];
            if (ch === 'S') {
                sx = i; sy = j;
            } else if (ch === 'L') {
                lPos.push([i, j]);
            }
        }
    }
    const totalL = lPos.length;
    const fullMask = (1 << totalL) - 1;

    // map each L cell to its bit index
    const lIdx = Array.from({ length: m }, () => Array(n).fill(-1));
    for (let i = 0; i < totalL; ++i) {
        const [x, y] = lPos[i];
        lIdx[x][y] = i;
    }

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    const queue = [];
    let head = 0;
    // state: x, y, mask, remaining energy, steps
    queue.push([sx, sy, 0, energy, 0]);
    const best = new Map(); // key -> max remaining energy seen
    const startKey = `${sx},${sy},0`;
    best.set(startKey, energy);

    while (head < queue.length) {
        const [x, y, mask, e, steps] = queue[head++];
        if (mask === fullMask) return steps;
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            const cell = classroom[nx][ny];
            if (cell === 'X') continue; // obstacle
            let ne = e - 1;
            if (ne < 0) continue; // not enough energy to move
            let nmask = mask;
            const idx = lIdx[nx][ny];
            if (idx !== -1) {
                nmask = mask | (1 << idx);
            }
            if (cell === 'R') {
                ne = energy; // reset energy on recharge cell
            }
            const key = `${nx},${ny},${nmask}`;
            const prev = best.get(key);
            if (prev !== undefined && prev >= ne) continue;
            best.set(key, ne);
            queue.push([nx, ny, nmask, ne, steps + 1]);
        }
    }
    return -1;
};
```

## Typescript

```typescript
function minMoves(classroom: string[], energy: number): number {
    const m = classroom.length;
    const n = classroom[0].length;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let sx = -1, sy = -1;
    const lId: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
    let lCount = 0;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const ch = classroom[i][j];
            if (ch === 'S') {
                sx = i;
                sy = j;
            } else if (ch === 'L') {
                lId[i][j] = lCount++;
            }
        }
    }

    const fullMask = (1 << lCount) - 1;
    if (fullMask === 0) return 0; // no litter to collect

    // best[x][y][mask] = max remaining energy seen
    const best: Int16Array[][][] = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => new Int16Array(1 << lCount).fill(-1))
    );

    const qx: number[] = [];
    const qy: number[] = [];
    const qmask: number[] = [];
    const qe: number[] = [];
    const qstep: number[] = [];

    let startMask = 0;
    if (classroom[sx][sy] === 'L') {
        const id = lId[sx][sy];
        startMask |= (1 << id);
    }
    best[sx][sy][startMask] = energy;
    qx.push(sx);
    qy.push(sy);
    qmask.push(startMask);
    qe.push(energy);
    qstep.push(0);

    let head = 0;
    while (head < qx.length) {
        const x = qx[head];
        const y = qy[head];
        let mask = qmask[head];
        let e = qe[head];
        const steps = qstep[head];
        ++head;

        if (mask === fullMask) return steps;

        const cell = classroom[x][y];
        if (cell === 'R' && e < energy) {
            e = energy; // reset energy
        }

        if (e <= best[x][y][mask]) continue;
        best[x][y][mask] = e;

        if (e === 0) continue; // cannot move further

        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            const nch = classroom[nx][ny];
            if (nch === 'X') continue; // obstacle

            let newMask = mask;
            if (nch === 'L') {
                const id = lId[nx][ny];
                newMask |= (1 << id);
            }

            const newE = e - 1;
            if (best[nx][ny][newMask] >= newE) continue;

            qx.push(nx);
            qy.push(ny);
            qmask.push(newMask);
            qe.push(newE);
            qstep.push(steps + 1);
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $classroom
     * @param Integer $energy
     * @return Integer
     */
    function minMoves($classroom, $energy) {
        $m = count($classroom);
        $n = strlen($classroom[0]);
        $sx = $sy = -1;
        $lIndex = [];
        $lCount = 0;

        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $ch = $classroom[$i][$j];
                if ($ch === 'S') {
                    $sx = $i;
                    $sy = $j;
                } elseif ($ch === 'L') {
                    $lIndex["$i,$j"] = $lCount++;
                }
            }
        }

        $fullMask = (1 << $lCount) - 1;
        if ($fullMask == 0) return 0; // no litter

        $totalStates = $m * $n * (1 << $lCount);
        $best = array_fill(0, $totalStates, -1);

        $queue = new SplQueue();
        $startIdx = (($sx * $n + $sy) << $lCount) | 0; // mask=0
        $best[$startIdx] = $energy;
        $queue->enqueue([$sx, $sy, 0, $energy, 0]); // x,y,mask,e,steps

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$queue->isEmpty()) {
            [$x,$y,$mask,$e,$steps] = $queue->dequeue();

            if ($mask === $fullMask) return $steps;

            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;
                $cell = $classroom[$nx][$ny];
                if ($cell === 'X') continue; // obstacle

                $ne = $e - 1;
                if ($ne < 0) continue; // cannot move further

                if ($cell === 'R') {
                    $ne = $energy; // reset
                }

                $nmask = $mask;
                if ($cell === 'L') {
                    $idx = $lIndex["$nx,$ny"];
                    $nmask |= (1 << $idx);
                }

                $stateIdx = ((($nx * $n + $ny) << $lCount) | $nmask);
                if ($best[$stateIdx] >= $ne) continue;
                $best[$stateIdx] = $ne;
                $queue->enqueue([$nx, $ny, $nmask, $ne, $steps + 1]);
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minMoves(_ classroom: [String], _ energy: Int) -> Int {
        let m = classroom.count
        guard m > 0 else { return -1 }
        let n = classroom[0].count
        
        // Convert grid to character matrix
        var grid = [[Character]]()
        for row in classroom {
            grid.append(Array(row))
        }
        
        var startX = 0, startY = 0
        var litterIndex = [Int:Int]()   // key: x*n + y , value: bit index
        var lCount = 0
        
        for i in 0..<m {
            for j in 0..<n {
                let ch = grid[i][j]
                if ch == "S" {
                    startX = i
                    startY = j
                } else if ch == "L" {
                    litterIndex[i * n + j] = lCount
                    lCount += 1
                }
            }
        }
        
        let fullMask = (1 << lCount) - 1
        if fullMask == 0 { return 0 }   // no litter to collect
        
        let maskCount = 1 << lCount
        var best = Array(repeating: -1, count: m * n * maskCount)
        func index(_ x:Int,_ y:Int,_ mask:Int) -> Int {
            ((x * n) + y) * maskCount + mask
        }
        
        struct Node {
            let x: Int
            let y: Int
            let mask: Int
            let e: Int
            let steps: Int
        }
        
        var queue = [Node]()
        var head = 0
        let startIdx = index(startX, startY, 0)
        best[startIdx] = energy
        queue.append(Node(x: startX, y: startY, mask: 0, e: energy, steps: 0))
        
        let dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while head < queue.count {
            let cur = queue[head]
            head += 1
            
            // cannot move if no energy left
            if cur.e == 0 { continue }
            
            for d in dirs {
                let nx = cur.x + d.0
                let ny = cur.y + d.1
                if nx < 0 || nx >= m || ny < 0 || ny >= n { continue }
                let cell = grid[nx][ny]
                if cell == "X" { continue }
                
                var ne = cur.e - 1
                if cell == "R" {
                    ne = energy
                }
                
                var nmask = cur.mask
                if cell == "L" {
                    if let bit = litterIndex[nx * n + ny] {
                        nmask |= (1 << bit)
                    }
                }
                
                if nmask == fullMask {
                    return cur.steps + 1
                }
                
                let idx = index(nx, ny, nmask)
                if ne > best[idx] {
                    best[idx] = ne
                    queue.append(Node(x: nx, y: ny, mask: nmask, e: ne, steps: cur.steps + 1))
                }
            }
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMoves(classroom: Array<String>, energy: Int): Int {
        val m = classroom.size
        val n = classroom[0].length
        val grid = Array(m) { CharArray(n) }
        var sx = 0
        var sy = 0
        val lIdx = Array(m) { IntArray(n) { -1 } }
        var lCount = 0
        for (i in 0 until m) {
            val row = classroom[i]
            for (j in 0 until n) {
                val c = row[j]
                grid[i][j] = c
                when (c) {
                    'S' -> {
                        sx = i
                        sy = j
                    }
                    'L' -> {
                        lIdx[i][j] = lCount++
                    }
                }
            }
        }
        val fullMask = if (lCount == 0) 0 else (1 shl lCount) - 1
        val bestEnergy = Array(m) { Array(n) { IntArray(1 shl lCount) { -1 } } }
        data class State(val x: Int, val y: Int, val mask: Int, val e: Int, val steps: Int)
        val queue: ArrayDeque<State> = ArrayDeque()
        queue.add(State(sx, sy, 0, energy, 0))
        bestEnergy[sx][sy][0] = energy
        val dx = intArrayOf(-1, 1, 0, 0)
        val dy = intArrayOf(0, 0, -1, 1)
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            if (cur.mask == fullMask) return cur.steps
            if (cur.e == 0) continue
            for (dir in 0..3) {
                val nx = cur.x + dx[dir]
                val ny = cur.y + dy[dir]
                if (nx !in 0 until m || ny !in 0 until n) continue
                val cell = grid[nx][ny]
                if (cell == 'X') continue
                var ne = cur.e - 1
                var nmask = cur.mask
                if (cell == 'L') {
                    val idx = lIdx[nx][ny]
                    nmask = nmask or (1 shl idx)
                }
                if (cell == 'R') {
                    ne = energy
                }
                if (ne <= bestEnergy[nx][ny][nmask]) continue
                bestEnergy[nx][ny][nmask] = ne
                queue.add(State(nx, ny, nmask, ne, cur.steps + 1))
            }
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minMoves(List<String> classroom, int energy) {
    int m = classroom.length;
    int n = classroom[0].length;

    // Index for each litter cell
    List<List<int>> lIdx = List.generate(m, (_) => List.filled(n, -1));
    int sx = 0, sy = 0;
    int lCount = 0;

    for (int i = 0; i < m; i++) {
      String row = classroom[i];
      for (int j = 0; j < n; j++) {
        String ch = row[j];
        if (ch == 'S') {
          sx = i;
          sy = j;
        } else if (ch == 'L') {
          lIdx[i][j] = lCount;
          lCount++;
        }
      }
    }

    int fullMask = (1 << lCount) - 1;

    // best[x][y][mask] = max remaining energy seen for this state
    List<List<List<int>>> best = List.generate(
        m, (_) => List.generate(n, (_) => List.filled(1 << lCount, -1)));

    List<List<int>> queue = [];
    int head = 0;

    best[sx][sy][0] = energy;
    queue.add([sx, sy, 0, energy, 0]); // x, y, mask, remainingEnergy, steps

    List<List<int>> dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1]
    ];

    while (head < queue.length) {
      var cur = queue[head++];
      int x = cur[0];
      int y = cur[1];
      int mask = cur[2];
      int e = cur[3];
      int steps = cur[4];

      if (mask == fullMask) return steps;

      for (var d in dirs) {
        int nx = x + d[0];
        int ny = y + d[1];
        if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
        String cell = classroom[nx][ny];
        if (cell == 'X') continue; // obstacle
        if (e == 0) continue; // cannot move without energy

        int ne = e - 1;
        if (cell == 'R') {
          ne = energy; // reset energy
        }

        int nmask = mask;
        if (cell == 'L') {
          int idx = lIdx[nx][ny];
          nmask = mask | (1 << idx);
        }

        if (best[nx][ny][nmask] >= ne) continue;
        best[nx][ny][nmask] = ne;
        queue.add([nx, ny, nmask, ne, steps + 1]);
      }
    }

    return -1;
  }
}
```

## Golang

```go
func minMoves(classroom []string, energy int) int {
	type state struct {
		x, y   int
		mask   int
		e      int
		steps  int
	}
	m := len(classroom)
	n := len(classroom[0])

	var sx, sy int
	lIdx := make([][]int, m)
	for i := 0; i < m; i++ {
		lIdx[i] = make([]int, n)
		for j := 0; j < n; j++ {
			lIdx[i][j] = -1
		}
	}
	lCount := 0
	for i := 0; i < m; i++ {
		row := classroom[i]
		for j := 0; j < n; j++ {
			switch row[j] {
			case 'S':
				sx, sy = i, j
			case 'L':
				lIdx[i][j] = lCount
				lCount++
			}
		}
	}
	if lCount == 0 {
		return 0
	}
	fullMask := (1 << lCount) - 1
	maskSize := 1 << lCount
	totalStates := m * n * maskSize
	best := make([]int, totalStates)
	for i := range best {
		best[i] = -1
	}
	index := func(x, y, mask int) int {
		return ((x*n)+y)*maskSize + mask
	}
	startIdx := index(sx, sy, 0)
	best[startIdx] = energy

	q := make([]state, 0, totalStates)
	q = append(q, state{sx, sy, 0, energy, 0})
	head := 0
	dir := []int{-1, 0, 1, 0, -1}
	for head < len(q) {
		cur := q[head]
		head++
		if cur.mask == fullMask {
			return cur.steps
		}
		if cur.e == 0 {
			continue // cannot move further unless on R, but moving costs energy first
		}
		for d := 0; d < 4; d++ {
			nx := cur.x + dir[d]
			ny := cur.y + dir[d+1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			cell := classroom[nx][ny]
			if cell == 'X' {
				continue
			}
			ne := cur.e - 1
			nmask := cur.mask
			if cell == 'L' {
				idx := lIdx[nx][ny]
				if idx >= 0 {
					nmask |= 1 << idx
				}
			}
			if cell == 'R' {
				ne = energy
			}
			if ne < 0 {
				continue
			}
			ni := index(nx, ny, nmask)
			if ne <= best[ni] {
				continue
			}
			best[ni] = ne
			q = append(q, state{nx, ny, nmask, ne, cur.steps + 1})
		}
	}
	return -1
}
```

## Ruby

```ruby
def min_moves(classroom, energy)
  m = classroom.size
  n = classroom[0].size
  grid = classroom.map { |row| row.chars }

  sx = sy = nil
  litter_idx = {}
  idx = 0

  (0...m).each do |i|
    (0...n).each do |j|
      case grid[i][j]
      when 'S'
        sx, sy = i, j
      when 'L'
        litter_idx[[i, j]] = idx
        idx += 1
      end
    end
  end

  full_mask = (1 << idx) - 1
  best = Array.new(m) { Array.new(n) { Array.new(1 << idx, -1) } }

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  queue = []
  head = 0
  best[sx][sy][0] = energy
  queue << [sx, sy, 0, energy, 0]

  while head < queue.length
    x, y, mask, e, steps = queue[head]
    head += 1

    return steps if mask == full_mask

    4.times do |dir|
      nx = x + dx[dir]
      ny = y + dy[dir]
      next unless nx.between?(0, m - 1) && ny.between?(0, n - 1)
      cell = grid[nx][ny]
      next if cell == 'X'
      next if e <= 0

      ne = e - 1
      nmask = mask
      if cell == 'L'
        bit = litter_idx[[nx, ny]]
        nmask |= (1 << bit)
      end
      if cell == 'R'
        ne = energy
      end

      next if ne <= best[nx][ny][nmask]

      best[nx][ny][nmask] = ne
      queue << [nx, ny, nmask, ne, steps + 1]
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def minMoves(classroom: Array[String], energy: Int): Int = {
        val m = classroom.length
        val n = classroom(0).length
        val grid = classroom.map(_.toCharArray)

        var startX = 0
        var startY = 0

        // assign index to each L cell
        val lIdx = Array.ofDim[Int](m, n)
        for (i <- 0 until m; j <- 0 until n) {
            lIdx(i)(j) = -1
            grid(i)(j) match {
                case 'S' => startX = i; startY = j
                case _   =>
            }
        }

        var lCount = 0
        for (i <- 0 until m; j <- 0 until n) {
            if (grid(i)(j) == 'L') {
                lIdx(i)(j) = lCount
                lCount += 1
            }
        }

        val fullMask = (1 << lCount) - 1
        if (fullMask == 0) return 0

        val maskSize = 1 << lCount
        val best = Array.fill(m, n, maskSize)(-1)

        import scala.collection.mutable.ArrayDeque
        val dq = new ArrayDeque[(Int, Int, Int, Int, Int)]()
        dq.append((startX, startY, 0, energy, 0))
        best(startX)(startY)(0) = energy

        val dirs = Array((1,0), (-1,0), (0,1), (0,-1))

        while (dq.nonEmpty) {
            val (x, y, mask, e, steps) = dq.removeHead()
            if (mask == fullMask) return steps
            for ((dx, dy) <- dirs) {
                val nx = x + dx
                val ny = y + dy
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid(nx)(ny) != 'X') {
                    if (e == 0) {
                        // cannot move without energy
                    } else {
                        var ne = e - 1
                        var nmask = mask
                        grid(nx)(ny) match {
                            case 'L' =>
                                val idx = lIdx(nx)(ny)
                                nmask |= (1 << idx)
                            case 'R' =>
                                ne = energy
                            case _ => // nothing
                        }
                        if (best(nx)(ny)(nmask) < ne) {
                            best(nx)(ny)(nmask) = ne
                            dq.append((nx, ny, nmask, ne, steps + 1))
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
use std::collections::VecDeque;

impl Solution {
    pub fn min_moves(classroom: Vec<String>, energy: i32) -> i32 {
        let m = classroom.len();
        if m == 0 {
            return -1;
        }
        let n = classroom[0].len();

        // grid characters
        let mut grid: Vec<Vec<char>> = vec![vec![' '; n]; m];
        // litter index mapping
        let mut litter_idx: Vec<Vec<Option<usize>>> = vec![vec![None; n]; m];

        let mut sx = 0usize;
        let mut sy = 0usize;
        let mut litter_cnt = 0usize;

        for (i, row) in classroom.iter().enumerate() {
            for (j, ch) in row.chars().enumerate() {
                grid[i][j] = ch;
                match ch {
                    'S' => {
                        sx = i;
                        sy = j;
                    }
                    'L' => {
                        litter_idx[i][j] = Some(litter_cnt);
                        litter_cnt += 1;
                    }
                    _ => {}
                }
            }
        }

        let full_mask: u16 = if litter_cnt == 0 { 0 } else { ((1u32 << litter_cnt) - 1) as u16 };
        if full_mask == 0 {
            return 0;
        }

        // best energy seen for (x, y, mask)
        let mask_size = 1usize << litter_cnt;
        let mut best: Vec<Vec<Vec<i32>>> = vec![vec![vec![-1; mask_size]; n]; m];
        let mut deque: VecDeque<(usize, usize, u16, i32, i32)> = VecDeque::new(); // x, y, mask, energy, steps

        best[sx][sy][0] = energy;
        deque.push_back((sx, sy, 0u16, energy, 0i32));

        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];

        while let Some((x, y, mask, e, steps)) = deque.pop_front() {
            if mask == full_mask {
                return steps;
            }
            for &(dx, dy) in &dirs {
                let nx_i = x as i32 + dx;
                let ny_i = y as i32 + dy;
                if nx_i < 0 || ny_i < 0 || nx_i >= m as i32 || ny_i >= n as i32 {
                    continue;
                }
                let nx = nx_i as usize;
                let ny = ny_i as usize;
                let cell = grid[nx][ny];
                if cell == 'X' {
                    continue;
                }

                let mut ne = e - 1;
                if ne < 0 {
                    continue;
                }
                // reset energy on R
                if cell == 'R' {
                    ne = energy;
                }

                let mut nmask = mask;
                if cell == 'L' {
                    if let Some(idx) = litter_idx[nx][ny] {
                        nmask |= 1u16 << idx;
                    }
                }

                if ne <= best[nx][ny][nmask as usize] {
                    continue;
                }
                best[nx][ny][nmask as usize] = ne;
                deque.push_back((nx, ny, nmask, ne, steps + 1));
            }
        }

        -1
    }
}
```

## Racket

```racket
#lang racket
(require racket/queue)

(define/contract (min-moves classroom energy)
  (-> (listof string?) exact-integer? exact-integer?)
  (define m (length classroom))
  (define n (if (= m 0) 0 (string-length (first classroom))))
  (define start-x -1)
  (define start-y -1)
  (define l-index (make-hash))
  (define lcnt 0)
  (for ([i (in-range m)])
    (let ([row (list-ref classroom i)])
      (for ([j (in-range n)])
        (define ch (string-ref row j))
        (cond
          [(char=? ch #\S) (set! start-x i) (set! start-y j)]
          [(char=? ch #\L)
           (hash-set! l-index (cons i j) lcnt)
           (set! lcnt (+ lcnt 1))]))))
  (define fullMask (if (= lcnt 0) 0 (sub1 (arithmetic-shift 1 lcnt))))
  (define maskSize (+ fullMask 1))
  (define best
    (for/vector ([i m])
      (for/vector ([j n])
        (make-vector maskSize -1))))
  (struct node (x y mask e steps) #:transparent)
  (define q (make-queue))
  ;; initialize start state
  (let* ([maskVec (vector-ref (vector-ref best start-x) start-y)])
    (vector-set! maskVec 0 energy)
    (enqueue! q (node start-x start-y 0 energy 0)))
  (define dirs '((0 1) (1 0) (0 -1) (-1 0)))
  (let loop ()
    (if (queue-empty? q)
        -1
        (let* ([cur (dequeue! q)]
               [x (node-x cur)] [y (node-y cur)] [mask (node-mask cur)]
               [e (node-e cur)] [steps (node-steps cur)])
          (if (= mask fullMask)
              steps
              (begin
                (for ([d dirs])
                  (define nx (+ x (first d)))
                  (define ny (+ y (second d)))
                  (when (and (>= nx 0) (< nx m) (>= ny 0) (< ny n))
                    (let ([cell (string-ref (list-ref classroom nx) ny)])
                      (unless (char=? cell #\X)
                        (let* ([e2 (- e 1)])
                          (when (>= e2 0)
                            (define e3 (if (char=? cell #\R) energy e2))
                            (define mask2
                              (if (char=? cell #\L)
                                  (let ([idx (hash-ref l-index (cons nx ny))])
                                    (bitwise-ior mask (arithmetic-shift 1 idx)))
                                  mask))
                            (let ([maskVec2 (vector-ref (vector-ref best nx) ny)])
                              (when (> e3 (vector-ref maskVec2 mask2))
                                (vector-set! maskVec2 mask2 e3)
                                (enqueue! q (node nx ny mask2 e3 (+ steps 1))))))))))))
                (loop)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_moves/2]).

-include_lib("kernel/include/logger.hrl").

-spec min_moves(Classroom :: [unicode:unicode_binary()], Energy :: integer()) -> integer().
min_moves(Classroom, MaxEnergy) ->
    % grid dimensions
    M = length(Classroom),
    N = case Classroom of
            [] -> 0;
            [Row|_] -> byte_size(Row)
        end,
    % locate start and litter positions
    {StartX, StartY, LMap, LCount} = locate(classify_grid(Classroom), 0, 0, #{}, undefined, 0),
    FullMask = (1 bsl LCount) - 1,
    Queue0 = queue:new(),
    Queue1 = queue:in({StartX, StartY, 0, MaxEnergy, 0}, Queue0),
    Best0 = maps:put({StartX, StartY, 0}, MaxEnergy, #{}),
    bfs(Queue1, Best0, Classroom, M, N, LMap, FullMask, MaxEnergy).

% Convert list of binaries to list (unchanged) for easy access
classify_grid(Grid) -> Grid.

locate([], _X, _Y, LMap, StartPos, Count) ->
    {element(1, StartPos), element(2, StartPos), LMap, Count};
locate([Row|Rest], X, Y, LMap, StartPos, Count) when Y >= byte_size(Row) ->
    locate(Rest, X+1, 0, LMap, StartPos, Count);
locate([Row|Rest]=Grid, X, Y, LMap, StartPos, Count) ->
    Char = binary:at(Row, Y),
    case Char of
        $S -> locate(Grid, X, Y+1, LMap, {X,Y}, Count);
        $L -> 
            NewIdx = Count,
            NewLMap = maps:put({X,Y}, NewIdx, LMap),
            locate(Grid, X, Y+1, NewLMap, StartPos, Count+1);
        _ ->
            locate(Grid, X, Y+1, LMap, StartPos, Count)
    end.

bfs(Queue, BestMap, Grid, M, N, LMap, FullMask, MaxEnergy) ->
    case queue:out(Queue) of
        {empty, _} -> -1;
        {{value, {X,Y,Mask,E,Steps}}, QRest} ->
            if Mask =:= FullMask ->
                    Steps;
               true ->
                    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
                    {NewQueue, NewBest} = lists:foldl(
                        fun({DX,DY}, {QAcc,BAcc}) ->
                            NX = X + DX,
                            NY = Y + DY,
                            if NX < 0 orelse NX >= M orelse NY < 0 orelse NY >= N ->
                                    {QAcc, BAcc};
                               true ->
                                    Char = get_char(Grid, NX, NY),
                                    case Char of
                                        $X -> {QAcc, BAcc}; % obstacle
                                        _ ->
                                            NewE0 = E - 1,
                                            if NewE0 < 0 ->
                                                    {QAcc, BAcc};
                                               true ->
                                                    NewE = case Char of
                                                               $R -> MaxEnergy;
                                                               _ -> NewE0
                                                           end,
                                                    NewMask = case Char of
                                                                  $L ->
                                                                      case maps:find({NX,NY}, LMap) of
                                                                          {ok, Idx} -> Mask bor (1 bsl Idx);
                                                                          error -> Mask
                                                                      end;
                                                                  _ -> Mask
                                                              end,
                                                    Key = {NX,NY,NewMask},
                                                    PrevE = maps:get(Key, BAcc, -1),
                                                    if NewE > PrevE ->
                                                            QNext = queue:in({NX,NY,NewMask,NewE,Steps+1}, QAcc),
                                                            BNext = maps:put(Key, NewE, BAcc),
                                                            {QNext, BNext};
                                                       true -> {QAcc, BAcc}
                                                    end
                                            end
                                    end
                            end
                        end,
                        {QRest, BestMap},
                        Directions),
                    bfs(NewQueue, NewBest, Grid, M, N, LMap, FullMask, MaxEnergy)
            end
    end.

get_char(Grid, X, Y) ->
    Row = lists:nth(X+1, Grid),
    binary:at(Row, Y).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves(classroom :: [String.t()], energy :: integer) :: integer
  def min_moves(classroom, energy) do
    # Convert classroom to a tuple of tuples for O(1) access
    grid =
      classroom
      |> Enum.map(fn row -> String.to_charlist(row) |> List.to_tuple() end)
      |> List.to_tuple()

    m = tuple_size(grid)
    n = tuple_size(elem(grid, 0))

    # Find start position and litter positions
    {start, litter_map, litter_count} =
      Enum.reduce(0..(m - 1), {{0, 0}, %{}, 0}, fn i, {s_acc, lm_acc, cnt_acc} ->
        row = elem(grid, i)

        {s_row, lm_row, cnt_row} =
          Enum.reduce(0..(n - 1), {s_acc, lm_acc, cnt_acc}, fn j, {s2, lm2, c2} ->
            cell = elem(row, j)

            cond do
              cell == ?S -> {{i, j}, lm2, c2}
              cell == ?L -> {s2, Map.put(lm2, {i, j}, c2), c2 + 1}
              true -> {s2, lm2, c2}
            end
          end)

        {s_row, lm_row, cnt_row}
      end)

    full_mask = (1 <<< litter_count) - 1

    bfs(grid, energy, start, litter_map, full_mask)
  end

  defp bfs(grid, max_e, {sx, sy}, litter_map, full_mask) do
    init_state = {sx, sy, 0, max_e, 0}
    queue = :queue.new() |> :queue.in(init_state)
    best = %{{sx, sy, 0} => max_e}
    bfs_loop(grid, max_e, litter_map, full_mask, queue, best)
  end

  defp bfs_loop(_grid, _max_e, _litter_map, full_mask, queue, _best) do
    case :queue.out(queue) do
      {:empty, _} -> -1
      {{:value, {_x, _y, mask, _e, steps}}, _rest_queue} when mask == full_mask ->
        steps

      _ -> :ok
    end
  end

  defp bfs_loop(grid, max_e, litter_map, full_mask, queue, best) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {x, y, mask, e, steps}}, rest_queue} ->
        if mask == full_mask do
          steps
        else
          cur_e =
            if cell_at(grid, x, y) == ?R and e < max_e do
              max_e
            else
              e
            end

          dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

          {new_queue, new_best} =
            Enum.reduce(dirs, {rest_queue, best}, fn {dx, dy}, {q_acc, b_acc} ->
              nx = x + dx
              ny = y + dy

              if nx < 0 or ny < 0 or nx >= tuple_size(grid) or ny >= tuple_size(elem(grid, 0)) do
                {q_acc, b_acc}
              else
                new_e = cur_e - 1

                c2 = cell_at(grid, nx, ny)

                new_mask =
                  if c2 == ?L do
                    idx = Map.get(litter_map, {nx, ny})
                    mask ||| (1 <<< idx)
                  else
                    mask
                  end

                key = {nx, ny, new_mask}
                prev_e = Map.get(b_acc, key, -1)

                if new_e > prev_e do
                  b2 = Map.put(b_acc, key, new_e)
                  q2 = :queue.in({nx, ny, new_mask, new_e, steps + 1}, q_acc)
                  {q2, b2}
                else
                  {q_acc, b_acc}
                end
              end
            end)

          bfs_loop(grid, max_e, litter_map, full_mask, new_queue, new_best)
        end
    end
  end

  defp cell_at(grid, x, y) do
    row = elem(grid, x)
    elem(row, y)
  end
end
```

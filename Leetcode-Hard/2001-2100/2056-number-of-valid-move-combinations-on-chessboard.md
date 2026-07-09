# 2056. Number of Valid Move Combinations On Chessboard

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Option{
        int dr, dc;      // destination
        int dx, dy;      // step direction per second
        int dist;        // number of steps to reach
    };
    
    bool reachable(const string& type, int sr, int sc, int tr, int tc){
        if(sr==tr && sc==tc) return true;
        if(type=="rook") return (sr==tr)||(sc==tc);
        if(type=="bishop") return abs(sr-tr)==abs(sc-tc);
        // queen
        return (sr==tr)||(sc==tc)|| (abs(sr-tr)==abs(sc-tc));
    }
    
    int sign(int x){ return (x>0)-(x<0); }
    
    bool validCombination(const vector<pair<int,int>>& starts,
                           const vector<Option>& chosen){
        int n = starts.size();
        int maxDist = 0;
        for(const auto& o: chosen) maxDist = max(maxDist, o.dist);
        // simulate each second
        for(int t=0; t<=maxDist; ++t){
            bool occ[64]={false};
            for(int i=0;i<n;++i){
                int steps = min(t, chosen[i].dist);
                int r = starts[i].first + chosen[i].dx * steps;
                int c = starts[i].second+ chosen[i].dy * steps;
                int id = (r-1)*8 + (c-1);
                if(occ[id]) return false;
                occ[id]=true;
            }
        }
        return true;
    }
    
    int countCombinations(vector<string>& pieces, vector<vector<int>>& positions) {
        int n = pieces.size();
        vector<pair<int,int>> starts(n);
        for(int i=0;i<n;++i){
            starts[i] = {positions[i][0], positions[i][1]};
        }
        // generate options per piece
        vector<vector<Option>> opts(n);
        for(int i=0;i<n;++i){
            int sr = starts[i].first, sc = starts[i].second;
            for(int r=1;r<=8;++r){
                for(int c=1;c<=8;++c){
                    if(!reachable(pieces[i], sr, sc, r, c)) continue;
                    Option o;
                    o.dr=r; o.dc=c;
                    o.dx = sign(r - sr);
                    o.dy = sign(c - sc);
                    o.dist = max(abs(r - sr), abs(c - sc));
                    opts[i].push_back(o);
                }
            }
        }
        long long ans=0;
        vector<Option> chosen(n);
        function<void(int)> dfs = [&](int idx){
            if(idx==n){
                if(validCombination(starts, chosen)) ++ans;
                return;
            }
            for(const auto& o: opts[idx]){
                chosen[idx]=o;
                dfs(idx+1);
            }
        };
        dfs(0);
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countCombinations(String[] pieces, int[][] positions) {
        int n = pieces.length;
        int[] startR = new int[n];
        int[] startC = new int[n];
        for (int i = 0; i < n; i++) {
            startR[i] = positions[i][0];
            startC[i] = positions[i][1];
        }

        // possible destinations for each piece
        List<List<int[]>> options = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            List<int[]> list = new ArrayList<>();
            for (int r = 1; r <= 8; r++) {
                for (int c = 1; c <= 8; c++) {
                    if (canReach(pieces[i], startR[i], startC[i], r, c)) {
                        list.add(new int[]{r, c});
                    }
                }
            }
            options.add(list);
        }

        int[] destR = new int[n];
        int[] destC = new int[n];
        return dfs(0, n, pieces, startR, startC, options, destR, destC);
    }

    private int dfs(int idx, int n, String[] pieces, int[] sr, int[] sc,
                    List<List<int[]>> opts, int[] dr, int[] dc) {
        if (idx == n) {
            return isValid(sr, sc, dr, dc, n) ? 1 : 0;
        }
        int count = 0;
        for (int[] pos : opts.get(idx)) {
            dr[idx] = pos[0];
            dc[idx] = pos[1];
            count += dfs(idx + 1, n, pieces, sr, sc, opts, dr, dc);
        }
        return count;
    }

    private boolean isValid(int[] sr, int[] sc, int[] dr, int[] dc, int n) {
        int[] steps = new int[n];
        int[] dx = new int[n];
        int[] dy = new int[n];
        int maxSteps = 0;
        for (int i = 0; i < n; i++) {
            int dR = dr[i] - sr[i];
            int dC = dc[i] - sc[i];
            steps[i] = Math.max(Math.abs(dR), Math.abs(dC));
            dx[i] = Integer.compare(dR, 0);
            dy[i] = Integer.compare(dC, 0);
            if (steps[i] > maxSteps) maxSteps = steps[i];
        }

        for (int t = 0; t <= maxSteps; t++) {
            boolean[][] occ = new boolean[9][9]; // 1..8 used
            for (int i = 0; i < n; i++) {
                int r, c;
                if (t >= steps[i]) {
                    r = dr[i];
                    c = dc[i];
                } else {
                    r = sr[i] + dx[i] * t;
                    c = sc[i] + dy[i] * t;
                }
                if (occ[r][c]) return false;
                occ[r][c] = true;
            }
        }
        return true;
    }

    private boolean canReach(String piece, int sr, int sc, int r, int c) {
        if (r == sr && c == sc) return true;
        switch (piece) {
            case "rook":
                return r == sr || c == sc;
            case "bishop":
                return Math.abs(r - sr) == Math.abs(c - sc);
            case "queen":
                return r == sr || c == sc || Math.abs(r - sr) == Math.abs(c - sc);
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def countCombinations(self, pieces, positions):
        """
        :type pieces: List[str]
        :type positions: List[List[int]]
        :rtype: int
        """
        # Precompute possible destinations for each piece (including staying)
        dirs = {
            "rook": [(1,0),(-1,0),(0,1),(0,-1)],
            "bishop": [(1,1),(1,-1),(-1,1),(-1,-1)],
            "queen": [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        }
        n = len(pieces)
        possible = []
        for idx in range(n):
            typ = pieces[idx]
            r0,c0 = positions[idx]
            dests = [(r0,c0)]  # staying put
            for dr,dc in dirs[typ]:
                nr,nc = r0+dr, c0+dc
                while 1 <= nr <= 8 and 1 <= nc <= 8:
                    dests.append((nr,nc))
                    nr += dr
                    nc += dc
            possible.append(dests)

        def sign(x):
            return (x > 0) - (x < 0)

        def valid(combo):
            # combo: list of destination tuples for each piece
            steps = []
            dirs_piece = []
            for i in range(n):
                r0,c0 = positions[i]
                rd,cd = combo[i]
                dr = sign(rd - r0)
                dc = sign(cd - c0)
                steps_needed = max(abs(rd - r0), abs(cd - c0))
                steps.append(steps_needed)
                dirs_piece.append((dr,dc))
            max_step = max(steps)
            for t in range(max_step+1):
                seen = set()
                for i in range(n):
                    r0,c0 = positions[i]
                    dr,dc = dirs_piece[i]
                    move = min(t, steps[i])
                    pos = (r0 + dr*move, c0 + dc*move)
                    if pos in seen:
                        return False
                    seen.add(pos)
            return True

        count = 0
        combo = [None]*n
        def backtrack(idx):
            nonlocal count
            if idx == n:
                if valid(combo):
                    count += 1
                return
            for dest in possible[idx]:
                combo[idx] = dest
                backtrack(idx+1)
        backtrack(0)
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        n = len(pieces)
        all_moves = []
        for i in range(n):
            r0, c0 = positions[i]
            piece = pieces[i]
            if piece == "rook":
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            elif piece == "bishop":
                dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            else:  # queen
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)]

            moves_i = [(r0, c0, 0, 0, 0)]  # stay
            for dr, dc in dirs:
                step = 1
                while 1 <= r0 + dr * step <= 8 and 1 <= c0 + dc * step <= 8:
                    dest_r = r0 + dr * step
                    dest_c = c0 + dc * step
                    moves_i.append((dest_r, dest_c, dr, dc, step))
                    step += 1
            all_moves.append(moves_i)

        total = 0
        chosen = [None] * n

        def dfs(idx: int):
            nonlocal total
            if idx == n:
                max_dist = max(chosen[i][4] for i in range(n))
                for t in range(max_dist + 1):
                    seen = set()
                    for i in range(n):
                        r0, c0 = positions[i]
                        dr, dc, dist = chosen[i][2], chosen[i][3], chosen[i][4]
                        step = t if t <= dist else dist
                        pos = (r0 + dr * step, c0 + dc * step)
                        if pos in seen:
                            return
                        seen.add(pos)
                total += 1
                return

            for mv in all_moves[idx]:
                chosen[idx] = mv
                dfs(idx + 1)

        dfs(0)
        return total
```

## C

```c
#include <string.h>
#include <stdlib.h>

static int sign(int x) {
    return (x > 0) - (x < 0);
}

static int n;
static int startR[4], startC[4];
static int destR[4], destC[4];

typedef struct {int r, c;} Pair;
static Pair options[4][28];
static int optCnt[4];

static int validCombination() {
    int len[4], dr[4], dc[4];
    int maxLen = 0;
    for (int i = 0; i < n; ++i) {
        int dR = destR[i] - startR[i];
        int dC = destC[i] - startC[i];
        dr[i] = sign(dR);
        dc[i] = sign(dC);
        len[i] = (abs(dR) > abs(dC)) ? abs(dR) : abs(dC);
        if (len[i] > maxLen) maxLen = len[i];
    }
    for (int t = 0; t <= maxLen; ++t) {
        int occ[9][9] = {{0}};
        for (int i = 0; i < n; ++i) {
            int r, c;
            if (t <= len[i]) {
                r = startR[i] + dr[i] * t;
                c = startC[i] + dc[i] * t;
            } else {
                r = destR[i];
                c = destC[i];
            }
            if (occ[r][c]) return 0;
            occ[r][c] = 1;
        }
    }
    return 1;
}

static int dfs(int idx) {
    if (idx == n) {
        return validCombination();
    }
    int total = 0;
    for (int k = 0; k < optCnt[idx]; ++k) {
        destR[idx] = options[idx][k].r;
        destC[idx] = options[idx][k].c;
        total += dfs(idx + 1);
    }
    return total;
}

int countCombinations(char** pieces, int piecesSize, int** positions, int positionsSize, int* positionsColSize) {
    n = piecesSize;
    for (int i = 0; i < n; ++i) {
        startR[i] = positions[i][0];
        startC[i] = positions[i][1];
    }

    for (int i = 0; i < n; ++i) {
        int sr = startR[i], sc = startC[i];
        optCnt[i] = 0;
        // stay
        options[i][optCnt[i]++] = (Pair){sr, sc};

        if (strcmp(pieces[i], "rook") == 0 || strcmp(pieces[i], "queen") == 0) {
            for (int r = 1; r <= 8; ++r) {
                if (r != sr) options[i][optCnt[i]++] = (Pair){r, sc};
            }
            for (int c = 1; c <= 8; ++c) {
                if (c != sc) options[i][optCnt[i]++] = (Pair){sr, c};
            }
        }

        if (strcmp(pieces[i], "bishop") == 0 || strcmp(pieces[i], "queen") == 0) {
            int drs[4] = {1, 1, -1, -1};
            int dcs[4] = {1, -1, 1, -1};
            for (int dir = 0; dir < 4; ++dir) {
                int r = sr + drs[dir];
                int c = sc + dcs[dir];
                while (r >= 1 && r <= 8 && c >= 1 && c <= 8) {
                    options[i][optCnt[i]++] = (Pair){r, c};
                    r += drs[dir];
                    c += dcs[dir];
                }
            }
        }
    }

    return dfs(0);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    public int CountCombinations(string[] pieces, int[][] positions)
    {
        int n = pieces.Length;
        int[] startR = new int[n];
        int[] startC = new int[n];
        for (int i = 0; i < n; i++)
        {
            startR[i] = positions[i][0];
            startC[i] = positions[i][1];
        }

        // Precompute possible destinations for each piece
        List<(int r, int c)>[] destLists = new List<(int r, int c)>[n];
        for (int i = 0; i < n; i++)
        {
            destLists[i] = new List<(int r, int c)>();
            for (int r = 1; r <= 8; r++)
            {
                for (int c = 1; c <= 8; c++)
                {
                    if (CanReach(pieces[i], startR[i], startC[i], r, c))
                        destLists[i].Add((r, c));
                }
            }
        }

        int[] chosenR = new int[n];
        int[] chosenC = new int[n];
        int count = 0;

        void Dfs(int idx)
        {
            if (idx == n)
            {
                if (IsValid())
                    count++;
                return;
            }

            foreach (var dest in destLists[idx])
            {
                chosenR[idx] = dest.r;
                chosenC[idx] = dest.c;
                Dfs(idx + 1);
            }
        }

        bool IsValid()
        {
            int[] dr = new int[n];
            int[] dc = new int[n];
            int[] steps = new int[n];
            int maxSteps = 0;

            for (int i = 0; i < n; i++)
            {
                dr[i] = Math.Sign(chosenR[i] - startR[i]);
                dc[i] = Math.Sign(chosenC[i] - startC[i]);
                steps[i] = Math.Max(Math.Abs(chosenR[i] - startR[i]), Math.Abs(chosenC[i] - startC[i]));
                if (steps[i] > maxSteps) maxSteps = steps[i];
            }

            for (int t = 0; t <= maxSteps; t++)
            {
                var occupied = new HashSet<(int, int)>();
                for (int i = 0; i < n; i++)
                {
                    int r, c;
                    if (t <= steps[i])
                    {
                        r = startR[i] + dr[i] * t;
                        c = startC[i] + dc[i] * t;
                    }
                    else
                    {
                        r = chosenR[i];
                        c = chosenC[i];
                    }

                    var pos = (r, c);
                    if (!occupied.Add(pos))
                        return false; // collision
                }
            }
            return true;
        }

        Dfs(0);
        return count;
    }

    private bool CanReach(string piece, int sr, int sc, int tr, int tc)
    {
        if (sr == tr && sc == tc) return true;

        switch (piece)
        {
            case "rook":
                return sr == tr || sc == tc;
            case "bishop":
                return Math.Abs(sr - tr) == Math.Abs(sc - tc);
            case "queen":
                return sr == tr || sc == tc || Math.Abs(sr - tr) == Math.Abs(sc - tc);
            default:
                return false;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} pieces
 * @param {number[][]} positions
 * @return {number}
 */
var countCombinations = function(pieces, positions) {
    const dirs = {
        rook: [[1,0],[-1,0],[0,1],[0,-1]],
        bishop: [[1,1],[1,-1],[-1,1],[-1,-1]],
        queen: [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    };
    
    const n = pieces.length;
    const movesList = []; // array of arrays per piece
    
    for (let i = 0; i < n; ++i) {
        const type = pieces[i];
        const [r, c] = positions[i];
        const dirsArr = dirs[type];
        const curMoves = [];
        // staying
        curMoves.push({dx:0, dy:0, len:0, destR:r, destC:c});
        for (const [dx, dy] of dirsArr) {
            let step = 1;
            while (true) {
                const nr = r + dx * step;
                const nc = c + dy * step;
                if (nr < 1 || nr > 8 || nc < 1 || nc > 8) break;
                curMoves.push({dx, dy, len:step, destR:nr, destC:nc});
                ++step;
            }
        }
        movesList.push(curMoves);
    }
    
    let count = 0;
    
    const chosen = new Array(n);
    
    function validate() {
        // compute max length
        let maxLen = 0;
        for (let i = 0; i < n; ++i) {
            if (chosen[i].len > maxLen) maxLen = chosen[i].len;
        }
        const startPos = positions.map(p=>[p[0], p[1]]);
        for (let t = 0; t <= maxLen; ++t) {
            const seen = new Set();
            for (let i = 0; i < n; ++i) {
                let r, c;
                if (t <= chosen[i].len) {
                    r = startPos[i][0] + chosen[i].dx * t;
                    c = startPos[i][1] + chosen[i].dy * t;
                } else {
                    r = chosen[i].destR;
                    c = chosen[i].destC;
                }
                const key = r + ',' + c;
                if (seen.has(key)) return false;
                seen.add(key);
            }
        }
        return true;
    }
    
    function dfs(idx) {
        if (idx === n) {
            if (validate()) count++;
            return;
        }
        for (const mv of movesList[idx]) {
            chosen[idx] = mv;
            dfs(idx + 1);
        }
    }
    
    dfs(0);
    return count;
};
```

## Typescript

```typescript
function countCombinations(pieces: string[], positions: number[][]): number {
    const n = pieces.length;
    // generate all possible moves for each piece
    const allMoves: { path: number[][]; dist: number }[][] = [];
    for (let i = 0; i < n; ++i) {
        const [r, c] = positions[i];
        allMoves.push(generateMoves(pieces[i], r, c));
    }

    let ans = 0;
    const selected: { path: number[][]; dist: number }[] = [];

    function dfs(idx: number): void {
        if (idx === n) {
            // validate this combination
            let maxDist = 0;
            for (const m of selected) {
                if (m.dist > maxDist) maxDist = m.dist;
            }
            for (let t = 0; t <= maxDist; ++t) {
                const seen = new Set<string>();
                for (const m of selected) {
                    const pos =
                        t <= m.dist ? m.path[t] : m.path[m.dist];
                    const key = pos[0] + ',' + pos[1];
                    if (seen.has(key)) return; // collision
                    seen.add(key);
                }
            }
            ++ans;
            return;
        }
        for (const mv of allMoves[idx]) {
            selected.push(mv);
            dfs(idx + 1);
            selected.pop();
        }
    }

    dfs(0);
    return ans;
}

function generateMoves(piece: string, r: number, c: number): { path: number[][]; dist: number }[] {
    const dirs: number[][] = [];
    if (piece === 'rook' || piece === 'queen') {
        dirs.push([1, 0], [-1, 0], [0, 1], [0, -1]);
    }
    if (piece === 'bishop' || piece === 'queen') {
        dirs.push([1, 1], [1, -1], [-1, 1], [-1, -1]);
    }

    const moves: { path: number[][]; dist: number }[] = [];
    // staying in place
    moves.push({ path: [[r, c]], dist: 0 });

    for (const [dr, dc] of dirs) {
        let nr = r + dr;
        let nc = c + dc;
        while (nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) {
            const dist = Math.max(Math.abs(nr - r), Math.abs(nc - c));
            const path: number[][] = [];
            for (let step = 0; step <= dist; ++step) {
                path.push([r + dr * step, c + dc * step]);
            }
            moves.push({ path, dist });
            nr += dr;
            nc += dc;
        }
    }

    return moves;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $pieces
     * @param Integer[][] $positions
     * @return Integer
     */
    function countCombinations($pieces, $positions) {
        $n = count($pieces);
        // Precompute possible destinations for each piece
        $options = [];
        for ($i = 0; $i < $n; ++$i) {
            [$r0, $c0] = $positions[$i];
            $list = [];
            for ($r = 1; $r <= 8; ++$r) {
                for ($c = 1; $c <= 8; ++$c) {
                    if ($this->canReach($pieces[$i], $r0, $c0, $r, $c)) {
                        $list[] = [$r, $c];
                    }
                }
            }
            $options[$i] = $list;
        }

        $count = 0;
        $chosen = array_fill(0, $n, null);
        $starts = $positions;

        // Depth‑first search over all combinations
        $dfs = function($idx) use (&$dfs, &$count, $n, $options, &$chosen, $starts) {
            if ($idx == $n) {
                if ($this->isValidCombo($starts, $chosen)) {
                    ++$count;
                }
                return;
            }
            foreach ($options[$idx] as $dest) {
                $chosen[$idx] = $dest;
                $dfs($idx + 1);
            }
        };

        $dfs(0);
        return $count;
    }

    private function canReach(string $type, int $r0, int $c0, int $r, int $c): bool {
        if ($r == $r0 && $c == $c0) {
            return true; // staying is allowed
        }
        $dr = $r - $r0;
        $dc = $c - $c0;
        switch ($type) {
            case 'rook':
                return $r0 == $r || $c0 == $c;
            case 'bishop':
                return abs($dr) == abs($dc);
            case 'queen':
                return $r0 == $r || $c0 == $c || abs($dr) == abs($dc);
        }
        return false;
    }

    private function isValidCombo(array $starts, array $dests): bool {
        $n = count($starts);
        $stepsNeeded = [];
        $drStep = [];
        $dcStep = [];

        $maxSteps = 0;
        for ($i = 0; $i < $n; ++$i) {
            [$sr, $sc] = $starts[$i];
            [$tr, $tc] = $dests[$i];
            $dr = $tr - $sr;
            $dc = $tc - $sc;
            $steps = max(abs($dr), abs($dc));
            $stepsNeeded[$i] = $steps;
            $maxSteps = max($maxSteps, $steps);
            $drStep[$i] = $steps == 0 ? 0 : ($dr > 0 ? 1 : ($dr < 0 ? -1 : 0));
            $dcStep[$i] = $steps == 0 ? 0 : ($dc > 0 ? 1 : ($dc < 0 ? -1 : 0));
        }

        for ($t = 0; $t <= $maxSteps; ++$t) {
            $occupied = [];
            for ($i = 0; $i < $n; ++$i) {
                if ($t >= $stepsNeeded[$i]) {
                    $r = $dests[$i][0];
                    $c = $dests[$i][1];
                } else {
                    $r = $starts[$i][0] + $drStep[$i] * $t;
                    $c = $starts[$i][1] + $dcStep[$i] * $t;
                }
                $key = $r . ',' . $c;
                if (isset($occupied[$key])) {
                    return false;
                }
                $occupied[$key] = true;
            }
        }
        return true;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    struct MoveOption {
        let dr: Int
        let dc: Int
        let dist: Int
    }
    
    func generateMoves(_ type: String, _ r: Int, _ c: Int) -> [MoveOption] {
        var res: [MoveOption] = []
        // stay in place
        res.append(MoveOption(dr: 0, dc: 0, dist: 0))
        
        let dirs: [[Int]]
        if type == "rook" {
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        } else if type == "bishop" {
            dirs = [[1,1],[1,-1],[-1,1],[-1,-1]]
        } else { // queen
            dirs = [[1,0],[-1,0],[0,1],[0,-1],
                    [1,1],[1,-1],[-1,1],[-1,-1]]
        }
        
        for d in dirs {
            var nr = r + d[0]
            var nc = c + d[1]
            while nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8 {
                let dr = d[0]
                let dc = d[1]
                let dist = max(abs(nr - r), abs(nc - c))
                res.append(MoveOption(dr: dr, dc: dc, dist: dist))
                nr += d[0]
                nc += d[1]
            }
        }
        return res
    }
    
    func countCombinations(_ pieces: [String], _ positions: [[Int]]) -> Int {
        let n = pieces.count
        var movesList = [[MoveOption]]()
        for i in 0..<n {
            let r = positions[i][0]
            let c = positions[i][1]
            movesList.append(generateMoves(pieces[i], r, c))
        }
        
        var chosen = [Int](repeating: 0, count: n)
        var total = 0
        
        func dfs(_ idx: Int) {
            if idx == n {
                // validate this combination
                var maxDist = 0
                for i in 0..<n {
                    let opt = movesList[i][chosen[i]]
                    if opt.dist > maxDist { maxDist = opt.dist }
                }
                
                var valid = true
                for t in 0...maxDist where valid {
                    var occupied = Set<Int>()
                    for i in 0..<n {
                        let startR = positions[i][0]
                        let startC = positions[i][1]
                        let opt = movesList[i][chosen[i]]
                        let step = min(t, opt.dist)
                        let r = startR + opt.dr * step
                        let c = startC + opt.dc * step
                        let key = (r - 1) * 8 + (c - 1)
                        if occupied.contains(key) {
                            valid = false
                            break
                        }
                        occupied.insert(key)
                    }
                }
                
                if valid { total += 1 }
                return
            }
            
            for j in 0..<movesList[idx].count {
                chosen[idx] = j
                dfs(idx + 1)
            }
        }
        
        dfs(0)
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countCombinations(pieces: Array<String>, positions: Array<IntArray>): Int {
        val n = pieces.size
        val startR = IntArray(n)
        val startC = IntArray(n)
        for (i in 0 until n) {
            startR[i] = positions[i][0]
            startC[i] = positions[i][1]
        }

        // possible destinations for each piece (including staying)
        val destLists = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (i in 0 until n) {
            val r0 = startR[i]
            val c0 = startC[i]
            for (r in 1..8) {
                for (c in 1..8) {
                    when (pieces[i]) {
                        "rook" -> if (r == r0 || c == c0) destLists[i].add(Pair(r, c))
                        "bishop" -> if (kotlin.math.abs(r - r0) == kotlin.math.abs(c - c0)) destLists[i].add(Pair(r, c))
                        "queen" -> if (r == r0 || c == c0 || kotlin.math.abs(r - r0) == kotlin.math.abs(c - c0)) destLists[i].add(Pair(r, c))
                    }
                }
            }
        }

        val destR = IntArray(n)
        val destC = IntArray(n)
        var answer = 0

        fun isValid(): Boolean {
            val curR = IntArray(n) { startR[it] }
            val curC = IntArray(n) { startC[it] }
            val stepR = IntArray(n)
            val stepC = IntArray(n)
            var maxSteps = 0
            for (i in 0 until n) {
                val dr = destR[i] - startR[i]
                val dc = destC[i] - startC[i]
                stepR[i] = when {
                    dr > 0 -> 1
                    dr < 0 -> -1
                    else -> 0
                }
                stepC[i] = when {
                    dc > 0 -> 1
                    dc < 0 -> -1
                    else -> 0
                }
                maxSteps = kotlin.math.max(
                    maxSteps,
                    kotlin.math.max(kotlin.math.abs(dr), kotlin.math.abs(dc))
                )
            }

            for (t in 1..maxSteps) {
                val seen = HashSet<Int>()
                for (i in 0 until n) {
                    if (curR[i] != destR[i] || curC[i] != destC[i]) {
                        curR[i] += stepR[i]
                        curC[i] += stepC[i]
                    }
                    val code = curR[i] * 10 + curC[i] // unique encoding for 1..8 board
                    if (!seen.add(code)) return false
                }
            }
            return true
        }

        fun dfs(idx: Int) {
            if (idx == n) {
                if (isValid()) answer++
                return
            }
            for ((r, c) in destLists[idx]) {
                destR[idx] = r
                destC[idx] = c
                dfs(idx + 1)
            }
        }

        dfs(0)
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int countCombinations(List<String> pieces, List<List<int>> positions) {
    int n = pieces.length;
    // Generate possible destinations for each piece
    List<List<List<int>>> options = List.generate(n, (_) => []);
    for (int i = 0; i < n; i++) {
      String type = pieces[i];
      int sr = positions[i][0];
      int sc = positions[i][1];
      for (int r = 1; r <= 8; r++) {
        for (int c = 1; c <= 8; c++) {
          if (_canReach(type, sr, sc, r, c)) {
            options[i].add([r, c]);
          }
        }
      }
    }

    int count = 0;
    List<List<int>> chosen = [];

    void dfs(int idx) {
      if (idx == n) {
        if (_isValid(chosen, positions)) count++;
        return;
      }
      for (var dest in options[idx]) {
        chosen.add(dest);
        dfs(idx + 1);
        chosen.removeLast();
      }
    }

    dfs(0);
    return count;
  }

  bool _canReach(String type, int sr, int sc, int r, int c) {
    if (type == "rook") {
      return sr == r || sc == c;
    } else if (type == "bishop") {
      return (sr - r).abs() == (sc - c).abs();
    } else { // queen
      return sr == r || sc == c || (sr - r).abs() == (sc - c).abs();
    }
  }

  bool _isValid(List<List<int>> dests, List<List<int>> starts) {
    int n = dests.length;
    List<int> stepR = List.filled(n, 0);
    List<int> stepC = List.filled(n, 0);
    List<int> dist = List.filled(n, 0);

    for (int i = 0; i < n; i++) {
      int sr = starts[i][0];
      int sc = starts[i][1];
      int dr = dests[i][0];
      int dc = dests[i][1];
      stepR[i] = _sign(dr - sr);
      stepC[i] = _sign(dc - sc);
      dist[i] = (dr - sr).abs().max((dc - sc).abs());
    }

    int maxDist = 0;
    for (int d in dist) if (d > maxDist) maxDist = d;

    for (int t = 0; t <= maxDist; t++) {
      Set<String> occupied = {};
      for (int i = 0; i < n; i++) {
        int r, c;
        if (t >= dist[i]) {
          r = dests[i][0];
          c = dests[i][1];
        } else {
          r = starts[i][0] + stepR[i] * t;
          c = starts[i][1] + stepC[i] * t;
        }
        String key = "$r,$c";
        if (occupied.contains(key)) return false;
        occupied.add(key);
      }
    }
    return true;
  }

  int _sign(int x) {
    if (x > 0) return 1;
    if (x < 0) return -1;
    return 0;
  }
}

extension on int {
  int max(int other) => this > other ? this : other;
}
```

## Golang

```go
type Position struct {
	r, c int
}

func countCombinations(pieces []string, positions [][]int) int {
	n := len(pieces)

	// store start positions
	starts := make([]Position, n)
	for i := 0; i < n; i++ {
		starts[i] = Position{positions[i][0], positions[i][1]}
	}

	// precompute possible destinations for each piece (including staying)
	dests := make([][]Position, n)
	for i := 0; i < n; i++ {
		r, c := starts[i].r, starts[i].c
		switch pieces[i] {
		case "rook":
			var list []Position
			list = append(list, Position{r, c}) // stay
			for cc := 1; cc <= 8; cc++ {
				if cc != c {
					list = append(list, Position{r, cc})
				}
			}
			for rr := 1; rr <= 8; rr++ {
				if rr != r {
					list = append(list, Position{rr, c})
				}
			}
			dests[i] = list
		case "bishop":
			m := make(map[int]bool)
			var list []Position
			list = append(list, Position{r, c}) // stay
			dir := [][2]int{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
			for _, d := range dir {
				rr, cc := r+d[0], c+d[1]
				for rr >= 1 && rr <= 8 && cc >= 1 && cc <= 8 {
					key := rr*10 + cc
					if !m[key] {
						m[key] = true
						list = append(list, Position{rr, cc})
					}
					rr += d[0]
					cc += d[1]
				}
			}
			dests[i] = list
		case "queen":
			m := make(map[int]bool)
			var list []Position
			add := func(p Position) {
				key := p.r*10 + p.c
				if !m[key] {
					m[key] = true
					list = append(list, p)
				}
			}
			add(Position{r, c}) // stay
			// rook moves
			for cc := 1; cc <= 8; cc++ {
				if cc != c {
					add(Position{r, cc})
				}
			}
			for rr := 1; rr <= 8; rr++ {
				if rr != r {
					add(Position{rr, c})
				}
			}
			// bishop moves
			dir := [][2]int{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
			for _, d := range dir {
				rr, cc := r+d[0], c+d[1]
				for rr >= 1 && rr <= 8 && cc >= 1 && cc <= 8 {
					add(Position{rr, cc})
					rr += d[0]
					cc += d[1]
				}
			}
			dests[i] = list
		}
	}

	total := 0

	var dfs func(idx int, chosen []Position)
	dfs = func(idx int, chosen []Position) {
		if idx == n {
			if isValid(starts, chosen) {
				total++
			}
			return
		}
		for _, p := range dests[idx] {
			dfs(idx+1, append(chosen, p))
		}
	}

	dfs(0, []Position{})
	return total
}

func isValid(starts []Position, dests []Position) bool {
	n := len(starts)
	maxSteps := 0
	steps := make([]int, n)
	dirX := make([]int, n)
	dirY := make([]int, n)

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	for i := 0; i < n; i++ {
		dr := dests[i].r - starts[i].r
		dc := dests[i].c - starts[i].c
		step := max(abs(dr), abs(dc))
		steps[i] = step
		if step > maxSteps {
			maxSteps = step
		}
		if dr != 0 {
			dirX[i] = dr / abs(dr)
		} else {
			dirX[i] = 0
		}
		if dc != 0 {
			dirY[i] = dc / abs(dc)
		} else {
			dirY[i] = 0
		}
	}

	for t := 0; t <= maxSteps; t++ {
		occ := make(map[int]bool, n)
		for i := 0; i < n; i++ {
			var r, c int
			if t <= steps[i] {
				r = starts[i].r + dirX[i]*t
				c = starts[i].c + dirY[i]*t
			} else {
				r = dests[i].r
				c = dests[i].c
			}
			key := r*10 + c
			if occ[key] {
				return false
			}
			occ[key] = true
		}
	}
	return true
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def count_combinations(pieces, positions)
  n = pieces.size
  # generate possible destinations for each piece (including staying)
  moves = []
  pieces.each_with_index do |type, idx|
    r, c = positions[idx]
    list = [[r, c]]
    (-1..1).each do |dr|
      (-1..1).each do |dc|
        next if dr == 0 && dc == 0
        allowed = case type
                  when "rook"
                    (dr == 0) ^ (dc == 0)
                  when "bishop"
                    dr.abs == dc.abs
                  else # queen
                    true
                  end
        next unless allowed
        step = 1
        loop do
          nr = r + dr * step
          nc = c + dc * step
          break if nr < 1 || nr > 8 || nc < 1 || nc > 8
          list << [nr, nc]
          step += 1
        end
      end
    end
    moves << list
  end

  start_pos = positions.map { |p| p.dup }
  dests = Array.new(n)
  dirs = Array.new(n)

  # check if a combination is valid
  valid_combo = lambda do |dests_arr, dirs_arr|
    cur = start_pos.map(&:dup)
    loop do
      n.times do |i|
        if cur[i][0] != dests_arr[i][0] || cur[i][1] != dests_arr[i][1]
          cur[i][0] += dirs_arr[i][0]
          cur[i][1] += dirs_arr[i][1]
        end
      end
      seen = {}
      n.times do |i|
        key = cur[i][0] * 10 + cur[i][1]
        return false if seen[key]
        seen[key] = true
      end
      all_done = true
      n.times do |i|
        unless cur[i][0] == dests_arr[i][0] && cur[i][1] == dests_arr[i][1]
          all_done = false
          break
        end
      end
      return true if all_done
    end
  end

  count = 0
  dfs = nil
  dfs = lambda do |idx|
    if idx == n
      count += 1 if valid_combo.call(dests, dirs)
    else
      moves[idx].each do |dest|
        dests[idx] = dest
        dr = dest[0] - start_pos[idx][0]
        dc = dest[1] - start_pos[idx][1]
        dr = dr <=> 0 if dr != 0
        dc = dc <=> 0 if dc != 0
        dirs[idx] = [dr, dc]
        dfs.call(idx + 1)
      end
    end
  end

  dfs.call(0)
  count
end
```

## Scala

```scala
object Solution {
  def countCombinations(pieces: Array[String], positions: Array[Array[Int]]): Int = {
    val n = pieces.length
    val starts = positions.map(p => (p(0), p(1)))

    def reachable(tpe: String, sr: Int, sc: Int, r: Int, c: Int): Boolean = {
      if (sr == r && sc == c) true
      else tpe match {
        case "rook"   => sr == r || sc == c
        case "bishop" => math.abs(sr - r) == math.abs(sc - c)
        case "queen"  => sr == r || sc == c || math.abs(sr - r) == math.abs(sc - c)
        case _        => false
      }
    }

    val options = Array.ofDim[Array[(Int, Int)]](n)
    for (i <- 0 until n) {
      val buf = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
      val (sr, sc) = starts(i)
      for (r <- 1 to 8; c <- 1 to 8) {
        if (reachable(pieces(i), sr, sc, r, c)) buf += ((r, c))
      }
      options(i) = buf.toArray
    }

    def sign(x: Int): Int = if (x > 0) 1 else if (x < 0) -1 else 0

    def isValid(dests: Array[(Int, Int)]): Boolean = {
      val stepsArr = new Array[Int](n)
      val drArr = new Array[Int](n)
      val dcArr = new Array[Int](n)
      var maxSteps = 0
      for (i <- 0 until n) {
        val (sr, sc) = starts(i)
        val (dr, dc) = dests(i)
        val steps = math.max(math.abs(dr - sr), math.abs(dc - sc))
        stepsArr(i) = steps
        drArr(i) = sign(dr - sr)
        dcArr(i) = sign(dc - sc)
        if (steps > maxSteps) maxSteps = steps
      }
      for (t <- 0 to maxSteps) {
        val seen = scala.collection.mutable.HashSet.empty[(Int, Int)]
        var i = 0
        while (i < n) {
          val (sr, sc) = starts(i)
          val curR = if (t >= stepsArr(i)) dests(i)._1 else sr + drArr(i) * t
          val curC = if (t >= stepsArr(i)) dests(i)._2 else sc + dcArr(i) * t
          val pos = (curR, curC)
          if (!seen.add(pos)) return false
          i += 1
        }
      }
      true
    }

    var count = 0L
    val chosen = new Array[(Int, Int)](n)

    def dfs(idx: Int): Unit = {
      if (idx == n) {
        if (isValid(chosen)) count += 1
        return
      }
      for (dest <- options(idx)) {
        chosen(idx) = dest
        dfs(idx + 1)
      }
    }

    dfs(0)
    count.toInt
  }
}
```

## Rust

```rust
use std::collections::HashSet;

fn generate_moves(kind: u8, r: i32, c: i32) -> Vec<(i32, i32)> {
    let mut res = Vec::new();
    // stay
    res.push((r, c));
    let dirs: &[(i32, i32)] = match kind {
        0 => &[ (1, 0), (-1, 0), (0, 1), (0, -1) ],                 // rook
        1 => &[ (1, 1), (1, -1), (-1, 1), (-1, -1) ],               // bishop
        _ => &[ (1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1) ],              // queen
    };
    for &(dr, dc) in dirs.iter() {
        let mut nr = r + dr;
        let mut nc = c + dc;
        while (1..=8).contains(&nr) && (1..=8).contains(&nc) {
            res.push((nr, nc));
            nr += dr;
            nc += dc;
        }
    }
    res
}

fn is_valid(start: &[(i32, i32)], dests: &[(i32, i32)]) -> bool {
    let n = start.len();
    let mut dirs = vec![(0_i32, 0_i32); n];
    let mut dists = vec![0_usize; n];
    for i in 0..n {
        let (sr, sc) = start[i];
        let (dr, dc) = dests[i];
        let step_r = (dr - sr).signum();
        let step_c = (dc - sc).signum();
        dirs[i] = (step_r, step_c);
        dists[i] = std::cmp::max((dr - sr).abs(), (dc - sc).abs()) as usize;
    }
    let max_dist = *dists.iter().max().unwrap_or(&0);
    for t in 0..=max_dist {
        let mut seen: HashSet<(i32, i32)> = HashSet::new();
        for i in 0..n {
            let (sr, sc) = start[i];
            let pos = if t >= dists[i] {
                dests[i]
            } else {
                let (step_r, step_c) = dirs[i];
                (sr + step_r * t as i32, sc + step_c * t as i32)
            };
            if !seen.insert(pos) {
                return false;
            }
        }
    }
    true
}

impl Solution {
    pub fn count_combinations(pieces: Vec<String>, positions: Vec<Vec<i32>>) -> i32 {
        let n = pieces.len();
        let mut kinds: Vec<u8> = Vec::with_capacity(n);
        for p in pieces.iter() {
            match p.as_str() {
                "rook" => kinds.push(0),
                "bishop" => kinds.push(1),
                "queen" => kinds.push(2),
                _ => unreachable!(),
            }
        }
        let mut starts: Vec<(i32, i32)> = Vec::with_capacity(n);
        for pos in positions.iter() {
            starts.push((pos[0], pos[1]));
        }

        // precompute possible destinations for each piece
        let mut options: Vec<Vec<(i32, i32)>> = Vec::with_capacity(n);
        for i in 0..n {
            let (r, c) = starts[i];
            options.push(generate_moves(kinds[i], r, c));
        }

        // depth‑first enumeration of all combinations
        fn dfs(
            idx: usize,
            n: usize,
            start_ref: &[(i32, i32)],
            opts: &Vec<Vec<(i32, i32)>>,
            cur: &mut Vec<(i32, i32)>,
            ans: &mut i32,
        ) {
            if idx == n {
                if is_valid(start_ref, cur) {
                    *ans += 1;
                }
                return;
            }
            for &(dr, dc) in opts[idx].iter() {
                cur.push((dr, dc));
                dfs(idx + 1, n, start_ref, opts, cur, ans);
                cur.pop();
            }
        }

        let mut answer: i32 = 0;
        let mut current: Vec<(i32, i32)> = Vec::with_capacity(n);
        dfs(0, n, &starts, &options, &mut current, &mut answer);
        answer
    }
}
```

## Racket

```racket
(define (sign x)
  (cond [(> x 0) 1] [(< x 0) -1] [else 0]))

(define (path-from-to r1 c1 r2 c2)
  (let* ((dr (sign (- r2 r1)))
         (dc (sign (- c2 c1)))
         (len (max (abs (- r2 r1)) (abs (- c2 c1)))))
    (let loop ((i 0) (acc '()))
      (if (> i len)
          (reverse acc)
          (loop (+ i 1)
                (cons (list (+ r1 (* dr i)) (+ c1 (* dc i))) acc))))))

(define (has-duplicate? lst)
  (let ((seen (make-hash)))
    (for/or ([p lst])
      (if (hash-has-key? seen p)
          #t
          (begin (hash-set! seen p #t) #f)))))

(define (valid-combination? paths)
  (let* ((lens (map length paths))
         (maxlen (apply max lens)))
    (let loop ((t 0))
      (if (> t maxlen)
          #t
          (let ((positions-at-t
                 (map (lambda (p len)
                        (if (< t len) (list-ref p t) (last p)))
                      paths lens)))
            (if (has-duplicate? positions-at-t)
                #f
                (loop (+ t 1))))))))

(define/contract (count-combinations pieces positions)
  (-> (listof string?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length pieces))
         ;; possible destinations for each piece (including staying)
         (piece-dests
          (map (lambda (ptype pos)
                 (let ((r (first pos)) (c (second pos)))
                   (define dirs
                     (cond [(string=? ptype "rook")
                            '((1 0) (-1 0) (0 1) (0 -1))]
                           [(string=? ptype "bishop")
                            '((1 1) (1 -1) (-1 1) (-1 -1))]
                           [else ; queen
                            '((1 0) (-1 0) (0 1) (0 -1)
                              (1 1) (1 -1) (-1 1) (-1 -1))]))
                   (let loop ((ds dirs) (acc (list (list r c)))) ; start square
                     (if (null? ds)
                         acc
                         (let* ((dr (first (first ds)))
                                (dc (second (first ds)))
                                (squares
                                 (let rec ((nr (+ r dr)) (nc (+ c dc)) (a '()))
                                   (if (or (< nr 1) (> nr 8) (< nc 1) (> nc 8))
                                       (reverse a)
                                       (rec (+ nr dr) (+ nc dc) (cons (list nr nc) a))))))
                           (loop (rest ds) (append acc squares)))))))
               pieces positions))
         ;; for each piece, list of [dest path] pairs
         (dest-paths-list
          (map (lambda (ptype pos dests)
                 (let ((r0 (first pos)) (c0 (second pos)))
                   (map (lambda (d)
                          (list d (path-from-to r0 c0 (first d) (second d))))
                        dests)))
               pieces positions piece-dests))
         (total 0))

    (define (dfs idx chosen-paths)
      (if (= idx n)
          (when (valid-combination? chosen-paths)
            (set! total (+ total 1)))
          (for ([entry (list-ref dest-paths-list idx)])
            (let ((path (second entry))) ; path list
              (dfs (+ idx 1) (cons path chosen-paths))))))
    (dfs 0 '())
    total))
```

## Erlang

```erlang
-module(solution).
-export([count_combinations/2]).

%% Entry point
-spec count_combinations(Pieces :: [unicode:unicode_binary()], Positions :: [[integer()]]) -> integer().
count_combinations(Pieces, Positions) ->
    Starts = [list_to_tuple(Pos) || Pos <- Positions],
    DestOptions = [destinations(Piece, Start) || {Piece, Start} <- lists:zip(Pieces, Starts)],
    dfs(0, [], DestOptions, Pieces, Starts, 0).

%% Depth‑first enumeration of all destination combinations
dfs(Index, CurrDests, DestOptions, Pieces, Starts, Count) when Index < length(DestOptions) ->
    Options = lists:nth(Index + 1, DestOptions),
    lists:foldl(
        fun(Dest, Acc) ->
            dfs(Index + 1, [Dest | CurrDests], DestOptions, Pieces, Starts, Acc)
        end,
        Count,
        Options);
dfs(Index, CurrDests, _DestOptions, Pieces, Starts, Count) when Index == length(Pieces) ->
    Dests = lists:reverse(CurrDests),
    case valid_combination(Starts, Dests) of
        true -> Count + 1;
        false -> Count
    end.

%% Generate all reachable squares (including staying)
destinations(Piece, {R, C}) ->
    Directions = case Piece of
        <<"rook">>   -> [{1,0}, {-1,0}, {0,1}, {0,-1}];
        <<"bishop">> -> [{1,1}, {1,-1}, {-1,1}, {-1,-1}];
        <<"queen">>  -> [{1,0}, {-1,0}, {0,1}, {0,-1},
                        {1,1}, {1,-1}, {-1,1}, {-1,-1}]
    end,
    Squares = lists:foldl(
        fun({DR, DC}, Acc) ->
            generate_dir(R + DR, C + DC, DR, DC, Acc)
        end,
        [],
        Directions),
    [{R, C} | Squares].

generate_dir(R, C, DR, DC, Acc) when R >= 1, R =< 8, C >= 1, C =< 8 ->
    generate_dir(R + DR, C + DC, DR, DC, [{R, C} | Acc]);
generate_dir(_, _, _, _, Acc) -> Acc.

%% Check if a combination of destinations is collision‑free
valid_combination(Starts, Dests) ->
    Infos = [
        begin
            DiffR = DestR - StartR,
            DiffC = DestC - StartC,
            Dx = sign(DiffR),
            Dy = sign(DiffC),
            Dist = max(abs(DiffR), abs(DiffC)),
            {Dx, Dy, Dist, {StartR, StartC}, {DestR, DestC}}
        end
        || {{StartR, StartC}, {DestR, DestC}} <- lists:zip(Starts, Dests)
    ],
    MaxDist = case Infos of
        [] -> 0;
        _  -> lists:max([Dist || {_Dx,_Dy,Dist,_S,_D} <- Infos])
    end,
    check_times(0, MaxDist, Infos).

check_times(T, MaxDist, Infos) when T =< MaxDist ->
    case positions_at_time(T, Infos, #{}) of
        ok -> check_times(T + 1, MaxDist, Infos);
        error -> false
    end;
check_times(_, _, _) -> true.

positions_at_time(_T, [], _Map) -> ok;
positions_at_time(T,
                  [{Dx, Dy, Dist, Start, Dest} | Rest],
                  Map) ->
    Pos = if
        T >= Dist -> Dest;
        true ->
            {SR, SC} = Start,
            {SR + Dx * T, SC + Dy * T}
    end,
    case maps:is_key(Pos, Map) of
        true -> error;
        false -> positions_at_time(T, Rest, maps:put(Pos, true, Map))
    end.

sign(N) when N > 0 -> 1;
sign(N) when N < 0 -> -1;
sign(0) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_combinations(pieces :: [String.t()], positions :: [[integer]]) :: integer
  def count_combinations(pieces, positions) do
    start_pos = Enum.map(positions, fn [r, c] -> {r, c} end)

    possible_lists =
      Enum.zip(pieces, start_pos)
      |> Enum.map(fn {type, pos} -> possible_destinations(type, pos) end)

    combos = cartesian_product(possible_lists)

    Enum.count(combos, fn dests ->
      valid_combo?(Enum.zip(start_pos, dests))
    end)
  end

  # generate all reachable squares (including staying) for each piece type
  defp possible_destinations("rook", {r, c}) do
    horiz = for col <- 1..8, col != c, do: {r, col}
    vert  = for row <- 1..8, row != r, do: {row, c}
    MapSet.new(horiz ++ vert ++ [{r, c}]) |> MapSet.to_list()
  end

  defp possible_destinations("bishop", {r, c}) do
    dirs = [{-1, -1}, {-1, 1}, {1, -1}, {1, 1}]
    squares =
      for {dr, dc} <- dirs,
          step <- 1..7,
          nr = r + dr * step,
          nc = c + dc * step,
          nr in 1..8,
          nc in 1..8,
          do: {nr, nc}
    MapSet.new(squares ++ [{r, c}]) |> MapSet.to_list()
  end

  defp possible_destinations("queen", pos) do
    rook = possible_destinations("rook", pos)
    bishop = possible_destinations("bishop", pos)
    MapSet.new(rook ++ bishop) |> MapSet.to_list()
  end

  # Cartesian product of list of lists
  defp cartesian_product(lists) do
    Enum.reduce(lists, [[]], fn lst, acc ->
      for combo <- acc, elem <- lst, do: [elem | combo]
    end)
    |> Enum.map(&Enum.reverse/1)
  end

  # Check if a particular combination of destinations is collision‑free
  defp valid_combo?(starts_and_dests) do
    moves =
      Enum.map(starts_and_dests, fn {{sr, sc}, {tr, tc}} ->
        steps = max(abs(tr - sr), abs(tc - sc))
        dr = sign(tr - sr)
        dc = sign(tc - sc)
        {sr, sc, tr, tc, steps, dr, dc}
      end)

    max_steps = moves |> Enum.map(fn {_sr, _sc, _tr, _tc, s, _dr, _dc} -> s end) |> Enum.max()

    0..max_steps
    |> Enum.all?(fn t ->
      positions =
        Enum.map(moves, fn {sr, sc, tr, tc, steps, dr, dc} ->
          if t >= steps do
            {tr, tc}
          else
            {sr + dr * t, sc + dc * t}
          end
        end)

      length(positions) == MapSet.size(MapSet.new(positions))
    end)
  end

  defp sign(x) when x > 0, do: 1
  defp sign(x) when x < 0, do: -1
  defp sign(_), do: 0
end
```

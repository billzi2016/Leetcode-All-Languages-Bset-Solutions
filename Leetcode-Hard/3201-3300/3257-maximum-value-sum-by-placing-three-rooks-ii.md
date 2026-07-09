# 3257. Maximum Value Sum by Placing Three Rooks II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to, rev;
    int cap;
    long long cost;
};

class MinCostMaxFlow {
public:
    int N;
    vector<vector<Edge>> G;
    vector<long long> h; // potential
    vector<long long> dist;
    vector<int> prevv, preve;

    MinCostMaxFlow(int n) : N(n), G(n), h(n), dist(n), prevv(n), preve(n) {}

    void addEdge(int from, int to, int cap, long long cost) {
        Edge a{to, (int)G[to].size(), cap, cost};
        Edge b{from, (int)G[from].size(), 0, -cost};
        G[from].push_back(a);
        G[to].push_back(b);
    }

    // returns pair {flow, cost}
    pair<int,long long> minCostFlow(int s, int t, int maxf) {
        const long long INF = (1LL<<60);
        int flow = 0;
        long long cost = 0;
        fill(h.begin(), h.end(), 0);
        // Bellman-Ford to find initial potentials if negative edges exist
        // Not needed because we will use Dijkstra with non-negative reduced costs after first iteration,
        // but we can run a simple relaxation.
        for (int iter = 0; iter < N; ++iter) {
            bool updated = false;
            for (int v = 0; v < N; ++v) {
                if (h[v] == INF) continue;
                for (auto &e : G[v]) {
                    if (e.cap > 0 && h[e.to] > h[v] + e.cost) {
                        h[e.to] = h[v] + e.cost;
                        updated = true;
                    }
                }
            }
            if (!updated) break;
        }

        while (flow < maxf) {
            priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
            fill(dist.begin(), dist.end(), INF);
            dist[s] = 0;
            pq.emplace(0, s);
            while (!pq.empty()) {
                auto [d, v] = pq.top(); pq.pop();
                if (dist[v] < d) continue;
                for (int i = 0; i < (int)G[v].size(); ++i) {
                    Edge &e = G[v][i];
                    if (e.cap > 0 && dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]) {
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
                        prevv[e.to] = v;
                        preve[e.to] = i;
                        pq.emplace(dist[e.to], e.to);
                    }
                }
            }
            if (dist[t] == INF) break; // cannot flow more
            for (int v = 0; v < N; ++v) h[v] += dist[v];
            int d = maxf - flow;
            for (int v = t; v != s; v = prevv[v]) {
                d = min(d, G[prevv[v]][preve[v]].cap);
            }
            flow += d;
            cost += (long long)d * h[t];
            for (int v = t; v != s; v = prevv[v]) {
                Edge &e = G[prevv[v]][preve[v]];
                e.cap -= d;
                G[v][e.rev].cap += d;
            }
        }
        return {flow, cost};
    }
};

class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        int V = m + n + 2;
        int S = m + n;      // source index
        int T = m + n + 1;  // sink index
        MinCostMaxFlow mcmf(V);
        // edges from source to rows
        for (int i = 0; i < m; ++i) {
            mcmf.addEdge(S, i, 1, 0);
        }
        // edges from columns to sink
        for (int j = 0; j < n; ++j) {
            mcmf.addEdge(m + j, T, 1, 0);
        }
        // edges row -> column with cost = -value
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                long long cost = -(long long)board[i][j];
                mcmf.addEdge(i, m + j, 1, cost);
            }
        }
        auto res = mcmf.minCostFlow(S, T, 3);
        // flow should be 3 (guaranteed by constraints)
        return -res.second;
    }
};
```

## Java

```java
class Solution {
    private static class Cell {
        int row;
        int col;
        long val;
        Cell(int r, int c, long v) {
            this.row = r;
            this.col = c;
            this.val = v;
        }
    }

    public long maximumValueSum(int[][] board) {
        int m = board.length;
        int n = board[0].length;

        // top 3 cells per row
        Cell[][] top = new Cell[m][3];
        int[] topCnt = new int[m];

        for (int i = 0; i < m; i++) {
            Cell[] curTop = new Cell[3];
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                long v = board[i][j];
                // insert into curTop maintaining descending order
                int pos = 0;
                while (pos < cnt && curTop[pos].val > v) pos++;
                if (pos < 3) {
                    // shift right
                    for (int k = Math.min(cnt, 2); k > pos; k--) {
                        curTop[k] = curTop[k - 1];
                    }
                    curTop[pos] = new Cell(i, j, v);
                    if (cnt < 3) cnt++;
                }
            }
            top[i] = curTop;
            topCnt[i] = cnt;
        }

        long answer = Long.MIN_VALUE;

        // iterate over first rook choices
        for (int r0 = 0; r0 < m; r0++) {
            for (int idxA = 0; idxA < topCnt[r0]; idxA++) {
                Cell a = top[r0][idxA];
                int colA = a.col;
                long valA = a.val;

                // collect candidates from other rows, excluding column colA
                java.util.ArrayList<Cell> cand = new java.util.ArrayList<>(3 * (m - 1));
                for (int i = 0; i < m; i++) {
                    if (i == r0) continue;
                    for (int k = 0; k < topCnt[i]; k++) {
                        Cell c = top[i][k];
                        if (c.col == colA) continue;
                        cand.add(c);
                    }
                }

                // sort descending by value
                cand.sort((c1, c2) -> Long.compare(c2.val, c1.val));

                int limit = Math.min(4, cand.size());
                for (int i = 0; i < limit; i++) {
                    Cell b = cand.get(i);
                    for (int j = i + 1; j < limit; j++) {
                        Cell c = cand.get(j);
                        if (b.row == c.row) continue;
                        if (b.col == c.col) continue;
                        long sum = valA + b.val + c.val;
                        if (sum > answer) answer = sum;
                    }
                }
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maximumValueSum(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        # top 3 values per row with distinct columns
        row_top = []
        for i in range(m):
            best = []
            for j in range(n):
                v = board[i][j]
                if len(best) < 3:
                    best.append((v, j))
                    best.sort(key=lambda x: -x[0])
                else:
                    if v > best[-1][0]:
                        best[-1] = (v, j)
                        best.sort(key=lambda x: -x[0])
            row_top.append(best)

        INF_NEG = -(10**30)
        ans = INF_NEG

        for i in range(m):
            for val0, col0 in row_top[i]:
                # collect candidates from other rows
                cand = []
                for r in range(m):
                    if r == i:
                        continue
                    chosen = None
                    for v, c in row_top[r]:
                        if c != col0:
                            chosen = (v, c)
                            break
                    if chosen:
                        cand.append(chosen)

                if len(cand) < 2:
                    continue

                # sort descending by value
                cand.sort(key=lambda x: -x[0])

                best1_val, best1_col = INF_NEG, -1
                best2_val, best2_col = INF_NEG, -1

                for v, c in cand:
                    # try combine with previous bests (which have higher values)
                    if best1_col != -1 and c != best1_col:
                        total = val0 + v + best1_val
                        if total > ans:
                            ans = total
                    elif best2_col != -1 and c != best2_col:
                        total = val0 + v + best2_val
                        if total > ans:
                            ans = total

                    # update best1 and best2 with current (v,c)
                    if v > best1_val:
                        if c == best1_col:
                            best1_val = v  # same column, just replace value
                        else:
                            best2_val, best2_col = best1_val, best1_col
                            best1_val, best1_col = v, c
                    elif v > best2_val and c != best1_col:
                        best2_val, best2_col = v, c

        return ans
```

## Python3

```python
from typing import List
import math

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        # top 3 values per row: list of (value, col)
        top_per_row = []
        for i in range(m):
            row_vals = board[i]
            # get indices of top 3 values
            cols = sorted(range(n), key=lambda c: row_vals[c], reverse=True)[:3]
            top_per_row.append([(row_vals[c], c) for c in cols])

        ans = -10**18

        for i in range(m):
            for val1, col1 in top_per_row[i]:
                # collect candidates from other rows
                cand = []
                for r in range(m):
                    if r == i:
                        continue
                    for v, c in top_per_row[r]:
                        if c == col1:
                            continue
                        cand.append((v, r, c))
                if len(cand) < 2:
                    continue
                # keep only top 4 candidates by value
                cand.sort(key=lambda x: x[0], reverse=True)
                cand = cand[:4]

                # brute force choose two distinct rows and columns
                L = len(cand)
                for a in range(L):
                    v2, r2, c2 = cand[a]
                    for b in range(a + 1, L):
                        v3, r3, c3 = cand[b]
                        if r2 == r3 or c2 == c3:
                            continue
                        total = val1 + v2 + v3
                        if total > ans:
                            ans = total
        return ans
```

## C

```c
#include <limits.h>

long long maximumValueSum(int** board, int boardSize, int* boardColSize) {
    int m = boardSize;
    int n = boardColSize[0];
    
    static long long topVal[500][3];
    static int topCol[500][3];
    
    // Precompute top 3 values for each row
    for (int i = 0; i < m; ++i) {
        topVal[i][0] = topVal[i][1] = topVal[i][2] = LLONG_MIN;
        topCol[i][0] = topCol[i][1] = topCol[i][2] = -1;
        for (int j = 0; j < n; ++j) {
            long long v = board[i][j];
            if (v > topVal[i][0]) {
                topVal[i][2] = topVal[i][1]; topCol[i][2] = topCol[i][1];
                topVal[i][1] = topVal[i][0]; topCol[i][1] = topCol[i][0];
                topVal[i][0] = v;            topCol[i][0] = j;
            } else if (v > topVal[i][1]) {
                topVal[i][2] = topVal[i][1]; topCol[i][2] = topCol[i][1];
                topVal[i][1] = v;            topCol[i][1] = j;
            } else if (v > topVal[i][2]) {
                topVal[i][2] = v;            topCol[i][2] = j;
            }
        }
    }
    
    long long answer = LLONG_MIN;
    static long long colBest[500];
    
    for (int i = 0; i < m; ++i) {
        for (int c = 0; c < n; ++c) {
            long long firstVal = board[i][c];
            
            // initialize per-iteration structures
            for (int k = 0; k < n; ++k) colBest[k] = LLONG_MIN;
            long long max1Val = LLONG_MIN, max2Val = LLONG_MIN;
            int max1Col = -1, max2Col = -1;
            
            for (int r = 0; r < m; ++r) {
                if (r == i) continue;
                
                // best candidate in row r not using column c
                long long candVal = LLONG_MIN;
                int candCol = -1;
                for (int t = 0; t < 3; ++t) {
                    if (topCol[r][t] == -1) break;
                    if (topCol[r][t] != c) {
                        candVal = topVal[r][t];
                        candCol = topCol[r][t];
                        break;
                    }
                }
                // fallback scan if needed
                if (candCol == -1) {
                    for (int j = 0; j < n; ++j) {
                        if (j == c) continue;
                        long long v = board[r][j];
                        if (v > candVal) {
                            candVal = v;
                            candCol = j;
                        }
                    }
                }
                
                // combine with best previous candidate having different column
                long long partner = (candCol != max1Col) ? max1Val : max2Val;
                if (partner != LLONG_MIN) {
                    long long total = firstVal + candVal + partner;
                    if (total > answer) answer = total;
                }
                
                // update structures with current candidate
                if (candVal > colBest[candCol]) {
                    colBest[candCol] = candVal;
                    if (candCol == max1Col) {
                        max1Val = candVal;
                    } else {
                        if (candVal > max1Val) {
                            // shift max1 to max2
                            max2Val = max1Val;
                            max2Col = max1Col;
                            max1Val = candVal;
                            max1Col = candCol;
                        } else if (candVal > max2Val && candCol != max1Col) {
                            max2Val = candVal;
                            max2Col = candCol;
                        }
                    }
                }
            }
        }
    }
    
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumValueSum(int[][] board) {
        int m = board.Length;
        int n = board[0].Length;
        // Store top 3 values per row
        List<(long val, int col)>[] top = new List<(long, int)>[m];
        for (int i = 0; i < m; i++) {
            var list = new List<(long, int)>(n);
            for (int j = 0; j < n; j++) {
                list.Add(((long)board[i][j], j));
            }
            list.Sort((a, b) => b.val.CompareTo(a.val));
            if (list.Count > 3) list.RemoveRange(3, list.Count - 3);
            top[i] = list;
        }

        long ans = long.MinValue;

        for (int r1 = 0; r1 < m; r1++) {
            foreach (var first in top[r1]) {
                // collect candidates from other rows excluding column of first
                var cand = new List<(long val, int row, int col)>();
                for (int r = 0; r < m; r++) {
                    if (r == r1) continue;
                    foreach (var p in top[r]) {
                        if (p.col == first.col) continue;
                        cand.Add((p.val, r, p.col));
                    }
                }
                // sort descending by value
                cand.Sort((a, b) => b.val.CompareTo(a.val));
                int limit = Math.Min(4, cand.Count);
                var shortList = cand.GetRange(0, limit);
                for (int i = 0; i < shortList.Count; i++) {
                    for (int j = i + 1; j < shortList.Count; j++) {
                        var a = shortList[i];
                        var b = shortList[j];
                        if (a.row != b.row && a.col != b.col) {
                            long sum = first.val + a.val + b.val;
                            if (sum > ans) ans = sum;
                        }
                    }
                }
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} board
 * @return {number}
 */
var maximumValueSum = function(board) {
    const m = board.length;
    const n = board[0].length;

    // For each row, store columns sorted by value descending
    const rowsVals = new Array(m);
    const rowsCols = new Array(m);
    const topThree = new Array(m); // up to 3 best entries per row

    for (let r = 0; r < m; ++r) {
        const cols = new Array(n);
        const vals = new Array(n);
        for (let c = 0; c < n; ++c) {
            cols[c] = c;
            vals[c] = board[r][c];
        }
        // sort indices by value descending
        cols.sort((a, b) => vals[b] - vals[a]);
        const sortedVals = new Array(n);
        for (let i = 0; i < n; ++i) {
            sortedVals[i] = board[r][cols[i]];
        }
        rowsCols[r] = cols;
        rowsVals[r] = sortedVals;

        const top = [];
        const limit = Math.min(3, n);
        for (let i = 0; i < limit; ++i) {
            top.push({val: sortedVals[i], col: cols[i]});
        }
        topThree[r] = top;
    }

    let answer = -Infinity;

    // iterate over pairs of rows
    for (let r1 = 0; r1 < m; ++r1) {
        const list1 = topThree[r1];
        for (let r2 = r1 + 1; r2 < m; ++r2) {
            const list2 = topThree[r2];
            // try each combination of columns from the two rows
            for (let i = 0; i < list1.length; ++i) {
                const a = list1[i];
                for (let j = 0; j < list2.length; ++j) {
                    const b = list2[j];
                    if (a.col === b.col) continue; // same column not allowed
                    const sum12 = a.val + b.val;
                    let bestThird = -Infinity;

                    // find best third rook among remaining rows
                    for (let r3 = 0; r3 < m; ++r3) {
                        if (r3 === r1 || r3 === r2) continue;
                        const colsArr = rowsCols[r3];
                        const valsArr = rowsVals[r3];
                        // first column not equal to a.col or b.col
                        for (let k = 0; k < n; ++k) {
                            const c = colsArr[k];
                            if (c !== a.col && c !== b.col) {
                                const cand = valsArr[k];
                                if (cand > bestThird) bestThird = cand;
                                break;
                            }
                        }
                    }

                    const total = sum12 + bestThird;
                    if (total > answer) answer = total;
                }
            }
        }
    }

    return answer;
};
```

## Typescript

```typescript
function maximumValueSum(board: number[][]): number {
    const m = board.length;
    const n = board[0].length;

    // store top three values and their columns for each row
    const topVals: number[][] = new Array(m);
    const topCols: number[][] = new Array(m);

    for (let i = 0; i < m; i++) {
        const vals = [-Infinity, -Infinity, -Infinity];
        const cols = [-1, -1, -1];
        const row = board[i];
        for (let j = 0; j < n; j++) {
            const v = row[j];
            if (v > vals[0]) {
                vals[2] = vals[1]; cols[2] = cols[1];
                vals[1] = vals[0]; cols[1] = cols[0];
                vals[0] = v;       cols[0] = j;
            } else if (v > vals[1]) {
                vals[2] = vals[1]; cols[2] = cols[1];
                vals[1] = v;       cols[1] = j;
            } else if (v > vals[2]) {
                vals[2] = v;       cols[2] = j;
            }
        }
        topVals[i] = vals;
        topCols[i] = cols;
    }

    let ans = -Infinity;

    for (let i = 0; i < m - 2; i++) {
        const vi = topVals[i];
        const ci = topCols[i];
        for (let j = i + 1; j < m - 1; j++) {
            const vj = topVals[j];
            const cj = topCols[j];
            for (let k = j + 1; k < m; k++) {
                const vk = topVals[k];
                const ck = topCols[k];

                for (let a = 0; a < 3; a++) {
                    const valA = vi[a];
                    if (valA === -Infinity) continue;
                    const colA = ci[a];
                    for (let b = 0; b < 3; b++) {
                        const valB = vj[b];
                        if (valB === -Infinity) continue;
                        const colB = cj[b];
                        if (colB === colA) continue;
                        for (let c = 0; c < 3; c++) {
                            const valC = vk[c];
                            if (valC === -Infinity) continue;
                            const colC = ck[c];
                            if (colC === colA || colC === colB) continue;
                            const sum = valA + valB + valC;
                            if (sum > ans) ans = sum;
                        }
                    }
                }
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $board
     * @return Integer
     */
    function maximumValueSum($board) {
        $m = count($board);
        $n = count($board[0]);
        // top 3 values per row with their columns
        $topRows = [];
        for ($i = 0; $i < $m; $i++) {
            $entries = [];
            for ($j = 0; $j < $n; $j++) {
                $entries[] = ['val' => $board[$i][$j], 'col' => $j];
            }
            usort($entries, function ($a, $b) {
                return $b['val'] <=> $a['val'];
            });
            $topRows[$i] = array_slice($entries, 0, 3);
        }

        $ans = -PHP_INT_MAX;

        for ($i = 0; $i < $m; $i++) {
            foreach ($topRows[$i] as $first) {
                $c1 = $first['col'];
                $v1 = $first['val'];

                // collect candidates from other rows, excluding column c1
                $cand = [];
                for ($j = 0; $j < $m; $j++) {
                    if ($j == $i) continue;
                    foreach ($topRows[$j] as $e) {
                        if ($e['col'] == $c1) continue;
                        $cand[] = ['val' => $e['val'], 'row' => $j, 'col' => $e['col']];
                    }
                }

                if (count($cand) < 2) continue;

                usort($cand, function ($a, $b) {
                    return $b['val'] <=> $a['val'];
                });
                $top = array_slice($cand, 0, 4);
                $len = count($top);

                for ($a = 0; $a < $len; $a++) {
                    for ($b = $a + 1; $b < $len; $b++) {
                        if ($top[$a]['row'] != $top[$b]['row'] && $top[$a]['col'] != $top[$b]['col']) {
                            $sum = $v1 + $top[$a]['val'] + $top[$b]['val'];
                            if ($sum > $ans) $ans = $sum;
                        }
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
class Solution {
    func maximumValueSum(_ board: [[Int]]) -> Int {
        let m = board.count
        let n = board[0].count
        var bestPerRow = Array(repeating: [(Int, Int)](), count: m)
        for i in 0..<m {
            var top = [(Int, Int)]()
            for j in 0..<n {
                let val = board[i][j]
                if top.count < 3 {
                    top.append((val, j))
                    if top.count == 3 {
                        top.sort { $0.0 > $1.0 }
                    }
                } else if val > top[2].0 {
                    top[2] = (val, j)
                    var idx = 2
                    while idx > 0 && top[idx].0 > top[idx - 1].0 {
                        top.swapAt(idx, idx - 1)
                        idx -= 1
                    }
                }
            }
            bestPerRow[i] = top
        }

        var ans = Int.min

        for i in 0..<(m - 2) {
            let listI = bestPerRow[i]
            let lenI = listI.count
            if lenI == 0 { continue }
            for j in (i + 1)..<(m - 1) {
                let listJ = bestPerRow[j]
                let lenJ = listJ.count
                if lenJ == 0 { continue }
                for k in (j + 1)..<m {
                    let listK = bestPerRow[k]
                    let lenK = listK.count
                    if lenK == 0 { continue }
                    var ii = 0
                    while ii < lenI {
                        let aVal = listI[ii].0
                        let aCol = listI[ii].1
                        var jj = 0
                        while jj < lenJ {
                            let bVal = listJ[jj].0
                            let bCol = listJ[jj].1
                            if aCol == bCol { jj += 1; continue }
                            var kk = 0
                            while kk < lenK {
                                let cVal = listK[kk].0
                                let cCol = listK[kk].1
                                if cCol == aCol || cCol == bCol {
                                    kk += 1
                                    continue
                                }
                                let sum = aVal + bVal + cVal
                                if sum > ans { ans = sum }
                                kk += 1
                            }
                            jj += 1
                        }
                        ii += 1
                    }
                }
            }
        }

        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumValueSum(board: Array<IntArray>): Long {
        val m = board.size
        val n = board[0].size
        val rowVals = Array(m) { LongArray(0) }
        val rowCols = Array(m) { IntArray(0) }

        for (i in 0 until m) {
            val list = mutableListOf<Pair<Long, Int>>()
            for (j in 0 until n) {
                list.add(Pair(board[i][j].toLong(), j))
            }
            list.sortByDescending { it.first }
            val sz = if (list.size > 3) 3 else list.size
            val vals = LongArray(sz)
            val cols = IntArray(sz)
            for (t in 0 until sz) {
                vals[t] = list[t].first
                cols[t] = list[t].second
            }
            rowVals[i] = vals
            rowCols[i] = cols
        }

        var ans = Long.MIN_VALUE

        for (i in 0 until m - 2) {
            val viArr = rowVals[i]
            val ciArr = rowCols[i]
            for (j in i + 1 until m - 1) {
                val vjArr = rowVals[j]
                val cjArr = rowCols[j]
                for (k in j + 1 until m) {
                    val vkArr = rowVals[k]
                    val ckArr = rowCols[k]

                    var aIdx = 0
                    while (aIdx < viArr.size) {
                        val vi = viArr[aIdx]
                        val ci = ciArr[aIdx]
                        var bIdx = 0
                        while (bIdx < vjArr.size) {
                            val vj = vjArr[bIdx]
                            val cj = cjArr[bIdx]
                            if (cj == ci) {
                                bIdx++
                                continue
                            }
                            var cIdx = 0
                            while (cIdx < vkArr.size) {
                                val vk = vkArr[cIdx]
                                val ck = ckArr[cIdx]
                                if (ck == ci || ck == cj) {
                                    cIdx++
                                    continue
                                }
                                val sum = vi + vj + vk
                                if (sum > ans) ans = sum
                                cIdx++
                            }
                            bIdx++
                        }
                        aIdx++
                    }
                }
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumValueSum(List<List<int>> board) {
    const int NEG_INF = -0x7FFFFFFFFFFFFF; // sufficiently small
    int m = board.length;
    int n = board[0].length;

    // top three (value, column) for each row
    List<List<int>> top = List.generate(m, (_) => []);

    for (int i = 0; i < m; ++i) {
      int v0 = NEG_INF, c0 = -1;
      int v1 = NEG_INF, c1 = -1;
      int v2 = NEG_INF, c2 = -1;
      for (int j = 0; j < n; ++j) {
        int val = board[i][j];
        if (val > v0) {
          v2 = v1; c2 = c1;
          v1 = v0; c1 = c0;
          v0 = val; c0 = j;
        } else if (val > v1) {
          v2 = v1; c2 = c1;
          v1 = val; c1 = j;
        } else if (val > v2) {
          v2 = val; c2 = j;
        }
      }
      List<int> lst = [];
      if (v0 != NEG_INF) { lst.add(v0); lst.add(c0); }
      if (v1 != NEG_INF) { lst.add(v1); lst.add(c1); }
      if (v2 != NEG_INF) { lst.add(v2); lst.add(c2); }
      top[i] = lst;
    }

    int answer = NEG_INF;

    for (int i = 0; i < m; ++i) {
      List<int> ti = top[i];
      for (int j = i + 1; j < m; ++j) {
        List<int> tj = top[j];
        int bestPairSum = NEG_INF;
        int pc1 = -1, pc2 = -1;

        // evaluate combinations of top entries from rows i and j
        for (int a = 0; a < ti.length; a += 2) {
          int vi = ti[a];
          int ci = ti[a + 1];
          for (int b = 0; b < tj.length; b += 2) {
            int vj = tj[b];
            int cj = tj[b + 1];
            if (ci == cj) continue;
            int sum = vi + vj;
            if (sum > bestPairSum) {
              bestPairSum = sum;
              pc1 = ci;
              pc2 = cj;
            }
          }
        }

        if (bestPairSum == NEG_INF) continue; // no valid pair

        for (int k = 0; k < m; ++k) {
          if (k == i || k == j) continue;
          List<int> tk = top[k];
          int bestThird = NEG_INF;
          for (int c = 0; c < tk.length; c += 2) {
            int vk = tk[c];
            int ck = tk[c + 1];
            if (ck == pc1 || ck == pc2) continue;
            if (vk > bestThird) bestThird = vk;
          }
          if (bestThird == NEG_INF) continue;
          int total = bestPairSum + bestThird;
          if (total > answer) answer = total;
        }
      }
    }

    return answer;
  }
}
```

## Golang

```go
func maximumValueSum(board [][]int) int64 {
	type entry struct {
		val int64
		col int
	}
	m := len(board)
	if m == 0 {
		return 0
	}
	n := len(board[0])

	// top three entries per row
	top := make([][]entry, m)

	for i := 0; i < m; i++ {
		rowTop := make([]entry, 0, 3)
		for j := 0; j < n; j++ {
			v := int64(board[i][j])
			if len(rowTop) < 3 {
				rowTop = append(rowTop, entry{v, j})
				if len(rowTop) == 3 {
					// sort descending
					if rowTop[0].val < rowTop[1].val {
						rowTop[0], rowTop[1] = rowTop[1], rowTop[0]
					}
					if rowTop[1].val < rowTop[2].val {
						rowTop[1], rowTop[2] = rowTop[2], rowTop[1]
					}
					if rowTop[0].val < rowTop[1].val {
						rowTop[0], rowTop[1] = rowTop[1], rowTop[0]
					}
				}
			} else {
				// find smallest among the three
				minIdx := 0
				if rowTop[1].val < rowTop[minIdx].val {
					minIdx = 1
				}
				if rowTop[2].val < rowTop[minIdx].val {
					minIdx = 2
				}
				if v > rowTop[minIdx].val {
					rowTop[minIdx] = entry{v, j}
					// bubble up to keep descending order
					if minIdx == 0 && rowTop[0].val < rowTop[1].val {
						rowTop[0], rowTop[1] = rowTop[1], rowTop[0]
						minIdx = 1
					}
					if (minIdx == 0 || minIdx == 1) && rowTop[minIdx].val < rowTop[2].val {
						rowTop[minIdx], rowTop[2] = rowTop[2], rowTop[minIdx]
					}
				}
			}
		}
		top[i] = rowTop
	}

	const inf int64 = -1 << 63
	ans := inf

	for i := 0; i < m; i++ {
		for _, a := range top[i] {
			for j := i + 1; j < m; j++ {
				for _, b := range top[j] {
					if b.col == a.col {
						continue
					}
					for k := j + 1; k < m; k++ {
						for _, c := range top[k] {
							if c.col == a.col || c.col == b.col {
								continue
							}
							sum := a.val + b.val + c.val
							if sum > ans {
								ans = sum
							}
						}
					}
				}
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def maximum_value_sum(board)
  m = board.size
  # top three cells per row: array of [value, column]
  row_top = Array.new(m) { [] }
  (0...m).each do |r|
    vals = []
    board[r].each_with_index { |v, c| vals << [v, c] }
    row_top[r] = vals.sort_by { |vc| -vc[0] }[0, 3]
  end

  neg_inf = -(1 << 62)
  answer = neg_inf

  (0...m).each do |i|
    row_top[i].each do |val_a, col_a|
      candidates = []
      (0...m).each do |r|
        next if r == i
        best = nil
        row_top[r].each do |v, c|
          if c != col_a
            best = [v, c, r] # value, column, row
            break
          end
        end
        candidates << best if best
      end

      next if candidates.size < 2
      top4 = candidates.sort_by { |e| -e[0] }[0, 4]

      best_pair = neg_inf
      n = top4.length
      (0...n).each do |p|
        ((p + 1)...n).each do |q|
          e1 = top4[p]
          e2 = top4[q]
          next if e1[2] == e2[2]   # same row, shouldn't happen but safe
          next if e1[1] == e2[1]   # same column conflict
          sum_pair = e1[0] + e2[0]
          best_pair = sum_pair if sum_pair > best_pair
        end
      end

      next if best_pair == neg_inf
      total = val_a + best_pair
      answer = total if total > answer
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
    def maximumValueSum(board: Array[Array[Int]]): Long = {
        val m = board.length
        val n = board(0).length

        // top 3 values per row (value, column)
        val topPerRow = new Array[Array[(Long, Int)]](m)

        var i = 0
        while (i < m) {
            val buf = scala.collection.mutable.ArrayBuffer.empty[(Long, Int)]
            var j = 0
            while (j < n) {
                val v = board(i)(j).toLong
                // insert maintaining descending order, keep at most 3
                var inserted = false
                var k = 0
                while (k < buf.length && !inserted) {
                    if (v > buf(k)._1) {
                        buf.insert(k, (v, j))
                        inserted = true
                    }
                    k += 1
                }
                if (!inserted && buf.length < 3) {
                    buf.append((v, j))
                }
                if (buf.length > 3) buf.remove(3)
                j += 1
            }
            topPerRow(i) = buf.toArray
            i += 1
        }

        var ans = Long.MinValue

        i = 0
        while (i < m) {
            val rowTop = topPerRow(i)
            var tIdx = 0
            while (tIdx < rowTop.length) {
                val (v1, c1) = rowTop(tIdx)

                // collect candidates from other rows excluding column c1
                val cand = scala.collection.mutable.ArrayBuffer.empty[(Long, Int, Int)]
                var r = 0
                while (r < m) {
                    if (r != i) {
                        val arrR = topPerRow(r)
                        var idx = 0
                        while (idx < arrR.length) {
                            val (v, c) = arrR(idx)
                            if (c != c1) cand.append((v, r, c))
                            idx += 1
                        }
                    }
                    r += 1
                }

                // sort descending by value and keep top 4
                import scala.util.Sorting
                val sorted = cand.toArray
                Sorting.stableSort(sorted)(Ordering.by[(Long, Int, Int), Long](_._1).reverse)
                val limit = math.min(4, sorted.length)

                var a = 0
                while (a < limit) {
                    val (vA, rA, cA) = sorted(a)
                    var b = a + 1
                    while (b < limit) {
                        val (vB, rB, cB) = sorted(b)
                        if (rA != rB && cA != cB) {
                            val sum = v1 + vA + vB
                            if (sum > ans) ans = sum
                        }
                        b += 1
                    }
                    a += 1
                }

                tIdx += 1
            }
            i += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_value_sum(board: Vec<Vec<i32>>) -> i64 {
        let m = board.len();
        let n = board[0].len();

        // top three values per row (value, column)
        let mut row_top: Vec<Vec<(i64, usize)>> = vec![Vec::new(); m];
        for i in 0..m {
            let mut tops: Vec<(i64, usize)> = Vec::with_capacity(3);
            for j in 0..n {
                let val = board[i][j] as i64;
                if tops.len() < 3 {
                    tops.push((val, j));
                } else {
                    // find smallest among current tops
                    let mut min_idx = 0;
                    for k in 1..3 {
                        if tops[k].0 < tops[min_idx].0 {
                            min_idx = k;
                        }
                    }
                    if val > tops[min_idx].0 {
                        tops[min_idx] = (val, j);
                    }
                }
            }
            tops.sort_by(|a, b| b.0.cmp(&a.0));
            row_top[i] = tops;
        }

        let mut answer: i64 = i64::MIN;

        // arrays to keep best two values per column among rows != r1 and col != c1
        let mut first_val = vec![i64::MIN; n];
        let mut first_row = vec![usize::MAX; n];
        let mut second_val = vec![i64::MIN; n];
        let mut second_row = vec![usize::MAX; n];

        for r1 in 0..m {
            for &(v1, c1) in &row_top[r1] {
                // reset column info
                for col in 0..n {
                    first_val[col] = i64::MIN;
                    second_val[col] = i64::MIN;
                    first_row[col] = usize::MAX;
                    second_row[col] = usize::MAX;
                }

                // fill best two per column from other rows
                for r2 in 0..m {
                    if r2 == r1 { continue; }
                    for &(val, col) in &row_top[r2] {
                        if col == c1 { continue; }
                        if val > first_val[col] {
                            second_val[col] = first_val[col];
                            second_row[col] = first_row[col];
                            first_val[col] = val;
                            first_row[col] = r2;
                        } else if val > second_val[col] {
                            second_val[col] = val;
                            second_row[col] = r2;
                        }
                    }
                }

                // collect columns that have at least one candidate
                let mut cols: Vec<usize> = Vec::new();
                for col in 0..n {
                    if first_val[col] != i64::MIN {
                        cols.push(col);
                    }
                }

                let mut best_two_sum = i64::MIN;
                let len = cols.len();
                for idx1 in 0..len {
                    let j = cols[idx1];
                    for idx2 in (idx1 + 1)..len {
                        let k = cols[idx2];
                        let mut cur = i64::MIN;
                        if first_row[j] != first_row[k] {
                            cur = first_val[j] + first_val[k];
                        } else {
                            if second_val[k] != i64::MIN {
                                cur = cur.max(first_val[j] + second_val[k]);
                            }
                            if second_val[j] != i64::MIN {
                                cur = cur.max(second_val[j] + first_val[k]);
                            }
                        }
                        if cur > best_two_sum {
                            best_two_sum = cur;
                        }
                    }
                }

                if best_two_sum != i64::MIN {
                    let total = v1 + best_two_sum;
                    if total > answer {
                        answer = total;
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
(define/contract (maximum-value-sum board)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length board))
         (n (if (= m 0) 0 (length (car board))))
         ;; compute top‑3 values for each row: list of (col . val) sorted descending
         (row-top-vals
          (list->vector
           (for/list ([row board])
             (let* ((pairs (for/list ([j (in-range n)])
                             (cons j (list-ref row j))))
                    (sorted (sort pairs (lambda (a b) (> (cdr a) (cdr b)))))
                    (top (if (< (length sorted) 3) sorted (take sorted 3))))
               top)))))
    (define min-sum (- (* 4 (expt 10 9)))) ; lower than any possible answer
    (define max-sum min-sum)
    ;; iterate over first rook choices
    (for ([r0 (in-range m)])
      (let ((top0 (vector-ref row-top-vals r0)))
        (for ([p0 top0])
          (define c0 (car p0))
          (define v0 (cdr p0))
          ;; collect candidates from other rows, avoiding column c0
          (define cand '())
          (for ([r (in-range m)])
            (when (not (= r r0))
              (for ([p (in-list (vector-ref row-top-vals r))])
                (when (not (= (car p) c0))
                  (set! cand (cons (list r (car p) (cdr p)) cand))))))
          ;; keep the best 4 candidates by value
          (define sorted-cand (sort cand (lambda (a b) (> (caddr a) (caddr b)))))
          (define topcand (if (< (length sorted-cand) 4)
                              sorted-cand
                              (take sorted-cand 4)))
          ;; find best pair among top candidates with distinct rows and columns
          (define best2 min-sum)
          (for ([i (in-range (length topcand))])
            (for ([j (in-range (+ i 1) (length topcand))])
              (let* ((ci (list-ref topcand i))
                     (cj (list-ref topcand j))
                     (ri (car ci)) (rj (car cj))
                     (cidi (cadr ci)) (cidj (cadr cj)))
                (when (and (not (= ri rj)) (not (= cidi cidj)))
                  (define sum (+ (caddr ci) (caddr cj)))
                  (when (> sum best2) (set! best2 sum))))))
          (when (> best2 min-sum)
            (define total (+ v0 best2))
            (when (> total max-sum) (set! max-sum total)))))))
    max-sum))
```

## Erlang

```erlang
-spec maximum_value_sum(Board :: [[integer()]]) -> integer().
maximum_value_sum(Board) ->
    RowsTop = compute_top3(Board),
    Arr = array:from_list(RowsTop),
    M = length(RowsTop),
    MinInf = - (1 bsl 62), % sufficiently small
    max_i(0, M, Arr, MinInf).

%% iterate over first row index
max_i(I, M, _Arr, Max) when I >= M - 2 ->
    Max;
max_i(I, M, Arr, Max) ->
    Ti = array:get(I, Arr),
    Max1 = max_j(I + 1, M, Arr, Ti, Max),
    max_i(I + 1, M, Arr, Max1).

%% iterate over second row index
max_j(J, M, _Arr, _Ti, Max) when J >= M - 1 ->
    Max;
max_j(J, M, Arr, Ti, Max) ->
    Tj = array:get(J, Arr),
    Max1 = max_k(J + 1, M, Arr, Ti, Tj, Max),
    max_j(J + 1, M, Arr, Ti, Max1).

%% iterate over third row index
max_k(K, M, _Arr, _Ti, _Tj, Max) when K >= M ->
    Max;
max_k(K, M, Arr, Ti, Tj, Max) ->
    Tk = array:get(K, Arr),
    NewMax = evaluate_triplet(Ti, Tj, Tk, Max),
    max_k(K + 1, M, Arr, Ti, Tj, NewMax).

%% evaluate all combinations of up to three candidates per row
evaluate_triplet(Ti, Tj, Tk, CurMax) ->
    lists:foldl(
      fun({Vi, Ci}, Acc1) ->
          lists:foldl(
            fun({Vj, Cj}, Acc2) when Cj =/= Ci ->
                lists:foldl(
                  fun({Vk, Ck}, Acc3) when Ck =/= Ci, Ck =/= Cj ->
                      Sum = Vi + Vj + Vk,
                      if Sum > Acc3 -> Sum; true -> Acc3 end
                  end,
                  Acc2,
                  Tk)
            ;(_,Acc2) -> Acc2
            end,
            Acc1,
            Tj)
      end,
      CurMax,
      Ti).

%% compute top 3 values (value, column) for each row
compute_top3(Board) ->
    lists:map(fun(Row) -> top3_row(Row) end, Board).

top3_row(Row) ->
    Indexed = enumerate(Row, 0, []),
    Sorted = lists:sort(fun({V1,_}, {V2,_}) -> V1 > V2 end, Indexed),
    take_n(Sorted, 3).

enumerate([], _Idx, Acc) ->
    lists:reverse(Acc);
enumerate([H|T], Idx, Acc) ->
    enumerate(T, Idx + 1, [{H, Idx}|Acc]).

take_n(_List, 0) -> [];
take_n([], _N) -> [];
take_n([H|T], N) when N > 0 ->
    [H | take_n(T, N - 1)].
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_value_sum(board :: [[integer]]) :: integer
  def maximum_value_sum(board) do
    rows =
      board
      |> Enum.with_index()
      |> Enum.map(fn {row_vals, idx} ->
        top =
          row_vals
          |> Enum.with_index()
          |> Enum.map(fn {v, c} -> {c, v} end)
          |> Enum.sort_by(fn {_c, v} -> -v end)
          |> Enum.take(3)

        max = case top do
          [] -> -9_000_000_000_000
          [{_, v} | _] -> v
        end

        %{idx: idx, top: top, max: max}
      end)
      |> Enum.sort_by(& &1.max, :desc)

    len = length(rows)
    loop_i(0, rows, len, -9_000_000_000_000)
  end

  defp loop_i(i, _rows, len, ans) when i > len - 3, do: ans
  defp loop_i(i, rows, len, ans) do
    ri = Enum.at(rows, i)

    ans1 =
      loop_j(i + 1, i, ri, rows, len, ans)

    loop_i(i + 1, rows, len, ans1)
  end

  defp loop_j(j, _i, _ri, _rows, len, ans) when j > len - 2, do: ans
  defp loop_j(j, i, ri, rows, len, ans) do
    rj = Enum.at(rows, j)

    # pruning for inner k loop start
    if i + 1 < len and ri.max + rj.max + (Enum.at(rows, i + 1).max) <= ans do
      # no better possible with any k, skip remaining j's as well
      ans
    else
      ans1 = loop_k(j + 1, ri, rj, rows, len, ans)
      loop_j(j + 1, i, ri, rows, len, ans1)
    end
  end

  defp loop_k(k, _ri, _rj, _rows, len, ans) when k > len - 1, do: ans
  defp loop_k(k, ri, rj, rows, len, ans) do
    rk = Enum.at(rows, k)
    potential = ri.max + rj.max + rk.max

    if potential <= ans do
      # further ks will have even smaller max (rows sorted), break
      ans
    else
      new_ans =
        for {c1, v1} <- ri.top,
            {c2, v2} <- rj.top,
            {c3, v3} <- rk.top,
            c1 != c2 and c1 != c3 and c2 != c3 do
          v1 + v2 + v3
        end
        |> Enum.max(fn -> ans end)
        |> max(ans)

      loop_k(k + 1, ri, rj, rows, len, new_ans)
    end
  end
end
```

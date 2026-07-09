# 3256. Maximum Value Sum by Placing Three Rooks I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        // store top three column values for each pair of rows
        struct Top3{
            long long val[3];
            int col[3];
            int cnt=0;
        };
        vector<vector<Top3>> top(m, vector<Top3>(m));
        
        // precompute for every unordered pair of rows
        for (int r1 = 0; r1 < m; ++r1) {
            for (int r2 = r1 + 1; r2 < m; ++r2) {
                vector<long long> colMax(n, LLONG_MIN);
                for (int r = 0; r < m; ++r) if (r != r1 && r != r2) {
                    for (int c = 0; c < n; ++c) {
                        colMax[c] = max(colMax[c], (long long)board[r][c]);
                    }
                }
                vector<pair<long long,int>> vec;
                vec.reserve(n);
                for (int c = 0; c < n; ++c) vec.emplace_back(colMax[c], c);
                sort(vec.begin(), vec.end(),
                     [](const auto& a, const auto& b){ return a.first > b.first; });
                Top3 t;
                t.cnt = min(3, (int)vec.size());
                for (int i = 0; i < t.cnt; ++i) {
                    t.val[i] = vec[i].first;
                    t.col[i] = vec[i].second;
                }
                top[r1][r2] = t;
            }
        }
        
        long long ans = LLONG_MIN;
        // iterate over unordered pair of rows and ordered columns
        for (int r1 = 0; r1 < m; ++r1) {
            for (int r2 = r1 + 1; r2 < m; ++r2) {
                const Top3& t = top[r1][r2];
                for (int c1 = 0; c1 < n; ++c1) {
                    long long v1 = board[r1][c1];
                    for (int c2 = 0; c2 < n; ++c2) if (c2 != c1) {
                        long long v2 = board[r2][c2];
                        long long third = LLONG_MIN;
                        for (int k = 0; k < t.cnt; ++k) {
                            int col = t.col[k];
                            if (col != c1 && col != c2) {
                                third = t.val[k];
                                break;
                            }
                        }
                        // fallback (should not happen with n>=3)
                        if (third == LLONG_MIN) {
                            for (int col = 0; col < n; ++col) {
                                if (col == c1 || col == c2) continue;
                                third = max(third, (long long)board[0][0]); // placeholder
                            }
                        }
                        ans = max(ans, v1 + v2 + third);
                    }
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Pair {
        long val;
        int col;
        Pair(long v, int c) { val = v; col = c; }
    }

    public long maximumValueSum(int[][] board) {
        int m = board.length;
        int n = board[0].length;

        long[][] bestVals = new long[m][3];
        int[][] bestCols = new int[m][3];

        for (int i = 0; i < m; i++) {
            Pair[] arr = new Pair[n];
            for (int j = 0; j < n; j++) {
                arr[j] = new Pair(board[i][j], j);
            }
            java.util.Arrays.sort(arr, (a, b) -> Long.compare(b.val, a.val));
            for (int k = 0; k < 3; k++) {
                if (k < n) {
                    bestVals[i][k] = arr[k].val;
                    bestCols[i][k] = arr[k].col;
                } else {
                    bestVals[i][k] = Long.MIN_VALUE;
                    bestCols[i][k] = -1;
                }
            }
        }

        long ans = Long.MIN_VALUE;

        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < m; j++) {
                for (int k = j + 1; k < m; k++) {
                    for (int a = 0; a < 3; a++) {
                        int colA = bestCols[i][a];
                        if (colA == -1) continue;
                        long valA = bestVals[i][a];
                        for (int b = 0; b < 3; b++) {
                            int colB = bestCols[j][b];
                            if (colB == -1 || colB == colA) continue;
                            long valB = bestVals[j][b];
                            for (int c = 0; c < 3; c++) {
                                int colC = bestCols[k][c];
                                if (colC == -1 || colC == colA || colC == colB) continue;
                                long sum = valA + valB + bestVals[k][c];
                                if (sum > ans) ans = sum;
                            }
                        }
                    }
                }
            }
        }

        return ans;
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
        m, n = len(board), len(board[0])
        INF_NEG = -10**18

        # Precompute for each excluded column the top few (up to 5) pair sums
        top_pairs_per_col = [[] for _ in range(n)]

        for excl_c in range(n):
            # best two values per row excluding column excl_c
            best1_val = [INF_NEG] * m
            best1_col = [-1] * m
            best2_val = [INF_NEG] * m
            best2_col = [-1] * m

            for i in range(m):
                v1, c1 = INF_NEG, -1
                v2, c2 = INF_NEG, -1
                row = board[i]
                for j in range(n):
                    if j == excl_c:
                        continue
                    val = row[j]
                    if val > v1:
                        v2, c2 = v1, c1
                        v1, c1 = val, j
                    elif val > v2:
                        v2, c2 = val, j
                best1_val[i] = v1
                best1_col[i] = c1
                best2_val[i] = v2
                best2_col[i] = c2

            # evaluate all row pairs and keep top few sums
            import heapq
            heap = []  # min-heap of (sum, r1, r2)
            for i in range(m):
                for j in range(i + 1, m):
                    if best1_col[i] != best1_col[j]:
                        s = best1_val[i] + best1_val[j]
                    else:
                        cand = INF_NEG
                        if best2_col[i] != -1:
                            cand = max(cand, best2_val[i] + best1_val[j])
                        if best2_col[j] != -1:
                            cand = max(cand, best1_val[i] + best2_val[j])
                        s = cand
                    if len(heap) < 5:
                        heapq.heappush(heap, (s, i, j))
                    else:
                        if s > heap[0][0]:
                            heapq.heapreplace(heap, (s, i, j))

            top_pairs_per_col[excl_c] = sorted(heap, key=lambda x: -x[0])

        ans = INF_NEG
        for r0 in range(m):
            row = board[r0]
            for c0 in range(n):
                base = row[c0]
                for s, r1, r2 in top_pairs_per_col[c0]:
                    if r1 != r0 and r2 != r0:
                        total = base + s
                        if total > ans:
                            ans = total
                        break  # best valid pair found

        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        INF_NEG = -10**18

        # precompute for each pair of columns the best value per row (excluding those two columns)
        pair_best = [[[] for _ in range(n)] for __ in range(n)]
        for a in range(n):
            for b in range(a + 1, n):
                best_row = [INF_NEG] * m
                for i in range(m):
                    row = board[i]
                    # iterate columns not a or b
                    for j in range(n):
                        if j == a or j == b:
                            continue
                        v = row[j]
                        if v > best_row[i]:
                            best_row[i] = v
                # take top three distinct rows
                top = sorted(((best_row[i], i) for i in range(m)), reverse=True)[:3]
                pair_best[a][b] = [(val, r) for val, r in top]

        ans = INF_NEG
        for r1 in range(m):
            row1 = board[r1]
            for c1 in range(n):
                v1 = row1[c1]
                for r2 in range(r1 + 1, m):
                    row2 = board[r2]
                    for c2 in range(n):
                        if c2 == c1:
                            continue
                        v2 = row2[c2]
                        a, b = (c1, c2) if c1 < c2 else (c2, c1)
                        cand = pair_best[a][b]
                        # find best third rook not using rows r1 or r2
                        for v3, r3 in cand:
                            if r3 != r1 and r3 != r2:
                                total = v1 + v2 + v3
                                if total > ans:
                                    ans = total
                                break
        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef struct Edge {
    int to;
    int rev;
    int cap;
    long long cost;
} Edge;

#define MAXV 205   // max nodes (100 rows + 100 cols + source + sink)

static Edge graph[MAXV][210];
static int gsize[MAXV];

static void add_edge(int from, int to, int cap, long long cost) {
    Edge a = {to, gsize[to], cap, cost};
    Edge b = {from, gsize[from], 0, -cost};
    graph[from][gsize[from]++] = a;
    graph[to][gsize[to]++] = b;
}

long long maximumValueSum(int** board, int boardSize, int* boardColSize) {
    int m = boardSize;
    int n = boardColSize[0];
    int V = m + n + 2;
    int S = 0;
    int T = V - 1;

    // initialize graph sizes
    for (int i = 0; i < V; ++i) gsize[i] = 0;

    // source to rows
    for (int i = 0; i < m; ++i) {
        add_edge(S, 1 + i, 1, 0);
    }
    // cols to sink
    for (int j = 0; j < n; ++j) {
        add_edge(1 + m + j, T, 1, 0);
    }
    // row to col edges with cost = -value
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            add_edge(1 + i, 1 + m + j, 1, -(long long)board[i][j]);
        }
    }

    int maxf = 3;
    int flow = 0;
    long long cost = 0;
    const long long INF = (1LL<<60);

    while (flow < maxf) {
        // SPFA to find shortest augmenting path
        static long long dist[MAXV];
        static int inqueue[MAXV];
        static int prevv[MAXV];
        static int preve[MAXV];

        for (int i = 0; i < V; ++i) {
            dist[i] = INF;
            inqueue[i] = 0;
        }
        dist[S] = 0;

        int qhead = 0, qtail = 0;
        static int que[MAXV];
        que[qtail++] = S;
        inqueue[S] = 1;

        while (qhead != qtail) {
            int v = que[qhead++];
            if (qhead == MAXV) qhead = 0;
            inqueue[v] = 0;
            for (int i = 0; i < gsize[v]; ++i) {
                Edge *e = &graph[v][i];
                if (e->cap > 0 && dist[e->to] > dist[v] + e->cost) {
                    dist[e->to] = dist[v] + e->cost;
                    prevv[e->to] = v;
                    preve[e->to] = i;
                    if (!inqueue[e->to]) {
                        que[qtail++] = e->to;
                        if (qtail == MAXV) qtail = 0;
                        inqueue[e->to] = 1;
                    }
                }
            }
        }

        if (dist[T] == INF) break; // cannot flow more

        int d = maxf - flow;
        for (int v = T; v != S; v = prevv[v]) {
            Edge *e = &graph[prevv[v]][preve[v]];
            if (d > e->cap) d = e->cap;
        }
        flow += d;
        cost += (long long)d * dist[T];
        for (int v = T; v != S; v = prevv[v]) {
            Edge *e = &graph[prevv[v]][preve[v]];
            e->cap -= d;
            graph[e->to][e->rev].cap += d;
        }
    }

    // answer is -cost because we minimized negative values
    return -cost;
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

        // top three values for each row
        var top3 = new (long val, int col)[m][];
        for (int r = 0; r < m; r++) {
            var list = new List<(long val, int col)>(n);
            for (int c = 0; c < n; c++) {
                list.Add(((long)board[r][c], c));
            }
            list.Sort((a, b) => b.val.CompareTo(a.val));
            int cnt = Math.Min(3, list.Count);
            top3[r] = new (long val, int col)[cnt];
            for (int i = 0; i < cnt; i++) {
                top3[r][i] = list[i];
            }
        }

        // pairBest[i][j][e] = best sum of rows i and j using columns not equal to e
        long[][][] pairBest = new long[m][][];
        for (int i = 0; i < m; i++) {
            pairBest[i] = new long[m][];
            for (int j = i + 1; j < m; j++) {
                var arr = new long[n];
                for (int e = 0; e < n; e++) {
                    long best = long.MinValue;
                    for (int a = 0; a < n; a++) {
                        if (a == e) continue;
                        long vi = board[i][a];
                        long vj = GetBestFromRow(j, a, e, top3);
                        if (vj != long.MinValue) {
                            long sum = vi + vj;
                            if (sum > best) best = sum;
                        }
                    }
                    arr[e] = best;
                }
                pairBest[i][j] = arr;
            }
        }

        long answer = long.MinValue;
        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < m; j++) {
                var arr = pairBest[i][j];
                for (int k = j + 1; k < m; k++) {
                    for (int c = 0; c < n; c++) {
                        long sumPair = arr[c];
                        if (sumPair == long.MinValue) continue;
                        long total = sumPair + board[k][c];
                        if (total > answer) answer = total;
                    }
                }
            }
        }

        return answer;
    }

    private static long GetBestFromRow(int rowIdx, int forbid1, int forbid2, (long val, int col)[][] top3) {
        foreach (var p in top3[rowIdx]) {
            if (p.col != forbid1 && p.col != forbid2) return p.val;
        }
        return long.MinValue;
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
    const topPerRow = new Array(m);
    
    for (let i = 0; i < m; ++i) {
        const arr = [];
        for (let j = 0; j < n; ++j) {
            arr.push({val: board[i][j], col: j});
        }
        arr.sort((a, b) => b.val - a.val);
        topPerRow[i] = arr.slice(0, Math.min(3, n));
    }
    
    let best = -Infinity;
    
    for (let i = 0; i < m - 2; ++i) {
        const rowI = topPerRow[i];
        for (let j = i + 1; j < m - 1; ++j) {
            const rowJ = topPerRow[j];
            for (let k = j + 1; k < m; ++k) {
                const rowK = topPerRow[k];
                for (const a of rowI) {
                    for (const b of rowJ) {
                        if (b.col === a.col) continue;
                        for (const c of rowK) {
                            if (c.col === a.col || c.col === b.col) continue;
                            const sum = a.val + b.val + c.val;
                            if (sum > best) best = sum;
                        }
                    }
                }
            }
        }
    }
    
    return best;
};
```

## Typescript

```typescript
function maximumValueSum(board: number[][]): number {
    const m = board.length;
    const n = board[0].length;
    let best = Number.NEGATIVE_INFINITY;

    for (let r1 = 0; r1 < m - 2; ++r1) {
        for (let r2 = r1 + 1; r2 < m - 1; ++r2) {
            for (let r3 = r2 + 1; r3 < m; ++r3) {
                const dp = new Float64Array(8);
                const ndp = new Float64Array(8);
                for (let i = 0; i < 8; ++i) dp[i] = Number.NEGATIVE_INFINITY;
                dp[0] = 0;

                for (let c = 0; c < n; ++c) {
                    // copy current dp to ndp
                    for (let mask = 0; mask < 8; ++mask) ndp[mask] = dp[mask];

                    const v0 = board[r1][c];
                    const v1 = board[r2][c];
                    const v2 = board[r3][c];

                    for (let mask = 0; mask < 8; ++mask) {
                        const cur = dp[mask];
                        if (cur === Number.NEGATIVE_INFINITY) continue;

                        if ((mask & 1) === 0) {
                            const newMask = mask | 1;
                            const cand = cur + v0;
                            if (cand > ndp[newMask]) ndp[newMask] = cand;
                        }
                        if ((mask & 2) === 0) {
                            const newMask = mask | 2;
                            const cand = cur + v1;
                            if (cand > ndp[newMask]) ndp[newMask] = cand;
                        }
                        if ((mask & 4) === 0) {
                            const newMask = mask | 4;
                            const cand = cur + v2;
                            if (cand > ndp[newMask]) ndp[newMask] = cand;
                        }
                    }

                    // copy back to dp for next column
                    for (let mask = 0; mask < 8; ++mask) dp[mask] = ndp[mask];
                }

                const val = dp[7];
                if (val > best) best = val;
            }
        }
    }

    return best;
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
        $INF_NEG = -PHP_INT_MAX;
        $ans = $INF_NEG;

        // Enumerate all triples of distinct rows
        for ($i = 0; $i < $m - 2; ++$i) {
            for ($j = $i + 1; $j < $m - 1; ++$j) {
                for ($k = $j + 1; $k < $m; ++$k) {
                    // DP over columns, mask of selected rows (3 bits)
                    $dp = array_fill(0, 8, $INF_NEG);
                    $dp[0] = 0;
                    for ($c = 0; $c < $n; ++$c) {
                        $next = $dp; // copy current states
                        $vals = [
                            $board[$i][$c],
                            $board[$j][$c],
                            $board[$k][$c]
                        ];
                        for ($mask = 0; $mask < 8; ++$mask) {
                            if ($dp[$mask] === $INF_NEG) continue;
                            // try to take one row in this column
                            for ($r = 0; $r < 3; ++$r) {
                                $bit = 1 << $r;
                                if (($mask & $bit) == 0) {
                                    $newMask = $mask | $bit;
                                    $cand = $dp[$mask] + $vals[$r];
                                    if ($cand > $next[$newMask]) {
                                        $next[$newMask] = $cand;
                                    }
                                }
                            }
                        }
                        $dp = $next;
                    }
                    if ($dp[7] > $ans) {
                        $ans = $dp[7];
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
        let base = n
        var dp1 = [Int:Int]()          // column -> max sum with 1 rook
        var dp2 = [Int:Int]()          // encoded pair -> max sum with 2 rooks
        var dp3 = [Int:Int]()          // encoded triple -> max sum with 3 rooks
        
        for r in 0..<m {
            let row = board[r]
            var newDp1 = dp1
            var newDp2 = dp2
            var newDp3 = dp3
            
            for col in 0..<n {
                let val = row[col]
                
                // Update dp1 (place rook only on this row)
                if let cur = newDp1[col] {
                    if val > cur { newDp1[col] = val }
                } else {
                    newDp1[col] = val
                }
                
                // Combine with existing single-rook states to form two rooks
                for (c1, sum1) in dp1 {
                    if c1 == col { continue }
                    let a = min(c1, col)
                    let b = max(c1, col)
                    let key = a * base + b
                    let newSum = sum1 + val
                    if let cur = newDp2[key] {
                        if newSum > cur { newDp2[key] = newSum }
                    } else {
                        newDp2[key] = newSum
                    }
                }
                
                // Combine with existing two-rook states to form three rooks
                for (pairKey, sum2) in dp2 {
                    let c1 = pairKey / base
                    let c2 = pairKey % base
                    if col == c1 || col == c2 { continue }
                    var cols = [c1, c2, col]
                    cols.sort()
                    let key3 = (cols[0] * base + cols[1]) * base + cols[2]
                    let newSum = sum2 + val
                    if let cur = newDp3[key3] {
                        if newSum > cur { newDp3[key3] = newSum }
                    } else {
                        newDp3[key3] = newSum
                    }
                }
            }
            
            dp1 = newDp1
            dp2 = newDp2
            dp3 = newDp3
        }
        
        var answer = Int.min
        for (_, v) in dp3 {
            if v > answer { answer = v }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumValueSum(board: Array<IntArray>): Long {
        val m = board.size
        val n = board[0].size
        var best = Long.MIN_VALUE

        for (r1 in 0 until m - 2) {
            for (r2 in r1 + 1 until m - 1) {
                for (r3 in r2 + 1 until m) {
                    var dp = LongArray(8) { Long.MIN_VALUE }
                    dp[0] = 0L
                    for (c in 0 until n) {
                        val v1 = board[r1][c].toLong()
                        val v2 = board[r2][c].toLong()
                        val v3 = board[r3][c].toLong()
                        val ndp = dp.clone()
                        for (mask in 0..7) {
                            val cur = dp[mask]
                            if (cur == Long.MIN_VALUE) continue
                            // assign to row r1
                            if ((mask and 1) == 0) {
                                val newMask = mask or 1
                                val cand = cur + v1
                                if (cand > ndp[newMask]) ndp[newMask] = cand
                            }
                            // assign to row r2
                            if ((mask and 2) == 0) {
                                val newMask = mask or 2
                                val cand = cur + v2
                                if (cand > ndp[newMask]) ndp[newMask] = cand
                            }
                            // assign to row r3
                            if ((mask and 4) == 0) {
                                val newMask = mask or 4
                                val cand = cur + v3
                                if (cand > ndp[newMask]) ndp[newMask] = cand
                            }
                        }
                        dp = ndp
                    }
                    if (dp[7] > best) best = dp[7]
                }
            }
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maximumValueSum(List<List<int>> board) {
    int m = board.length;
    int n = board[0].length;
    const int NEG_INF = -1 << 60;

    // Precompute top three column values for each pair of rows
    List<List<int>> topVals = [];
    List<List<int>> topCols = [];

    for (int r1 = 0; r1 < m; ++r1) {
      for (int r2 = r1 + 1; r2 < m; ++r2) {
        // best value in each column excluding rows r1 and r2
        List<int> colBest = List.filled(n, NEG_INF);
        for (int c = 0; c < n; ++c) {
          int maxV = NEG_INF;
          for (int r = 0; r < m; ++r) {
            if (r == r1 || r == r2) continue;
            int v = board[r][c];
            if (v > maxV) maxV = v;
          }
          colBest[c] = maxV;
        }

        // keep top three columns
        List<int> vals = [NEG_INF, NEG_INF, NEG_INF];
        List<int> cols = [-1, -1, -1];
        for (int c = 0; c < n; ++c) {
          int v = colBest[c];
          if (v > vals[0]) {
            vals[2] = vals[1];
            cols[2] = cols[1];
            vals[1] = vals[0];
            cols[1] = cols[0];
            vals[0] = v;
            cols[0] = c;
          } else if (v > vals[1]) {
            vals[2] = vals[1];
            cols[2] = cols[1];
            vals[1] = v;
            cols[1] = c;
          } else if (v > vals[2]) {
            vals[2] = v;
            cols[2] = c;
          }
        }
        topVals.add(vals);
        topCols.add(cols);
      }
    }

    int ans = NEG_INF;
    int pairIdx = 0;
    for (int r1 = 0; r1 < m; ++r1) {
      for (int r2 = r1 + 1; r2 < m; ++r2) {
        List<int> vals = topVals[pairIdx];
        List<int> cols = topCols[pairIdx];

        for (int c1 = 0; c1 < n; ++c1) {
          for (int c2 = c1 + 1; c2 < n; ++c2) {
            // find best third rook value not using columns c1 or c2
            int third = NEG_INF;
            for (int k = 0; k < 3; ++k) {
              int colIdx = cols[k];
              if (colIdx != -1 && colIdx != c1 && colIdx != c2) {
                third = vals[k];
                break;
              }
            }

            // two possible assignments for the first two rooks
            int sumA = board[r1][c1] + board[r2][c2];
            int sumB = board[r1][c2] + board[r2][c1];

            if (third != NEG_INF) {
              int totalA = sumA + third;
              if (totalA > ans) ans = totalA;
              int totalB = sumB + third;
              if (totalB > ans) ans = totalB;
            }
          }
        }

        pairIdx++;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maximumValueSum(board [][]int) int64 {
    m := len(board)
    n := len(board[0])

    type pair struct {
        val int64
        row int
    }

    // top three values per column with their rows
    topCol := make([][3]pair, n)
    for c := 0; c < n; c++ {
        vals := make([]pair, m)
        for r := 0; r < m; r++ {
            vals[r] = pair{int64(board[r][c]), r}
        }
        // simple selection sort for top three (m <= 100)
        for i := 0; i < 3 && i < m; i++ {
            maxIdx := i
            for j := i + 1; j < m; j++ {
                if vals[j].val > vals[maxIdx].val {
                    maxIdx = j
                }
            }
            vals[i], vals[maxIdx] = vals[maxIdx], vals[i]
            topCol[c][i] = vals[i]
        }
        // fill remaining slots with sentinel
        for i := 3; i < 3; i++ {
            topCol[c][i] = pair{val: -(1 << 60), row: -1}
        }
    }

    // precompute for each unordered pair of rows the best three columns (value, column)
    pairBestVals := make([][3]int64, m*m)
    pairBestCols := make([][3]int, m*m)

    const INF_NEG int64 = -(1 << 60)

    for i := 0; i < m; i++ {
        for j := i + 1; j < m; j++ {
            idx := i*m + j
            var bestVals [3]int64
            var bestCols [3]int
            for t := 0; t < 3; t++ {
                bestVals[t] = INF_NEG
                bestCols[t] = -1
            }
            for c := 0; c < n; c++ {
                // find best value in column c whose row is not i or j
                val := INF_NEG
                for k := 0; k < 3; k++ {
                    r := topCol[c][k].row
                    if r != -1 && r != i && r != j {
                        val = topCol[c][k].val
                        break
                    }
                }
                // insert into top three lists for this pair
                for t := 0; t < 3; t++ {
                    if val > bestVals[t] {
                        // shift down
                        for s := 2; s > t; s-- {
                            bestVals[s] = bestVals[s-1]
                            bestCols[s] = bestCols[s-1]
                        }
                        bestVals[t] = val
                        bestCols[t] = c
                        break
                    }
                }
            }
            pairBestVals[idx] = bestVals
            pairBestCols[idx] = bestCols
        }
    }

    ans := INF_NEG

    for i := 0; i < m; i++ {
        for j := i + 1; j < m; j++ {
            idx := i*m + j
            topVals := pairBestVals[idx]
            topCols := pairBestCols[idx]

            for c1 := 0; c1 < n; c1++ {
                v1 := int64(board[i][c1])
                for c2 := 0; c2 < n; c2++ {
                    if c2 == c1 {
                        continue
                    }
                    sum12 := v1 + int64(board[j][c2])

                    third := INF_NEG
                    for t := 0; t < 3; t++ {
                        col := topCols[t]
                        if col != -1 && col != c1 && col != c2 {
                            third = topVals[t]
                            break
                        }
                    }
                    total := sum12 + third
                    if total > ans {
                        ans = total
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
  n = board[0].size
  INF_NEG = -(1 << 60)

  if n <= m
    # Process columns: keep top 3 values per column (value, row)
    col_top = Array.new(n) { [] }
    m.times do |r|
      n.times do |c|
        val = board[r][c]
        top = col_top[c]
        if top.size < 3
          top << [val, r]
          top.sort_by! { |p| -p[0] }
        elsif val > top[-1][0]
          top[-1] = [val, r]
          top.sort_by! { |p| -p[0] }
        end
      end
    end

    ans = INF_NEG
    (0...n).to_a.combination(3) do |c1, c2, c3|
      col_top[c1].each do |v1, r1|
        col_top[c2].each do |v2, r2|
          next if r2 == r1
          col_top[c3].each do |v3, r3|
            next if r3 == r1 || r3 == r2
            sum = v1 + v2 + v3
            ans = sum if sum > ans
          end
        end
      end
    end
    ans
  else
    # Process rows: keep top 3 values per row (value, col)
    row_top = Array.new(m) { [] }
    m.times do |r|
      n.times do |c|
        val = board[r][c]
        top = row_top[r]
        if top.size < 3
          top << [val, c]
          top.sort_by! { |p| -p[0] }
        elsif val > top[-1][0]
          top[-1] = [val, c]
          top.sort_by! { |p| -p[0] }
        end
      end
    end

    ans = INF_NEG
    (0...m).to_a.combination(3) do |r1, r2, r3|
      row_top[r1].each do |v1, c1|
        row_top[r2].each do |v2, c2|
          next if c2 == c1
          row_top[r3].each do |v3, c3|
            next if c3 == c1 || c3 == c2
            sum = v1 + v2 + v3
            ans = sum if sum > ans
          end
        end
      end
    end
    ans
  end
end
```

## Scala

```scala
object Solution {
    def maximumValueSum(board: Array[Array[Int]]): Long = {
        val m = board.length
        val n = board(0).length
        val cells = scala.collection.mutable.ArrayBuffer[(Int, Int, Int)]()
        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                cells.append((board(i)(j), i, j))
                j += 1
            }
            i += 1
        }
        val sorted = cells.sortWith(_._1 > _._1) // descending by value
        val N = sorted.length
        val globalMax = sorted(0)._1
        var ans: Long = Long.MinValue

        var a = 0
        while (a < N) {
            val (va, ra, ca) = sorted(a)
            var b = a + 1
            while (b < N) {
                val (vb, rb, cb) = sorted(b)
                if (ra != rb && ca != cb) {
                    // prune using the best possible third value
                    if (va.toLong + vb + globalMax > ans) {
                        var sum: Long = va.toLong + vb
                        var cIdx = 0
                        var found = false
                        while (!found && cIdx < N) {
                            val (vc, rc, cc) = sorted(cIdx)
                            if (rc != ra && rc != rb && cc != ca && cc != cb) {
                                sum += vc
                                found = true
                            }
                            cIdx += 1
                        }
                        if (found && sum > ans) ans = sum
                    }
                }
                b += 1
            }
            a += 1
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
        let mut answer = i64::MIN;
        const NEG: i64 = i64::MIN / 4; // safe negative sentinel
        for r1 in 0..m - 2 {
            for r2 in (r1 + 1)..m - 1 {
                for r3 in (r2 + 1)..m {
                    let mut dp = [NEG; 8];
                    dp[0] = 0;
                    for c in 0..n {
                        let vals = [
                            board[r1][c] as i64,
                            board[r2][c] as i64,
                            board[r3][c] as i64,
                        ];
                        let mut ndp = dp;
                        for mask in 0..8 {
                            if dp[mask] == NEG {
                                continue;
                            }
                            for row_idx in 0..3 {
                                if (mask >> row_idx) & 1 == 0 {
                                    let new_mask = mask | (1 << row_idx);
                                    let cand = dp[mask] + vals[row_idx];
                                    if cand > ndp[new_mask] {
                                        ndp[new_mask] = cand;
                                    }
                                }
                            }
                        }
                        dp = ndp;
                    }
                    if dp[7] > answer {
                        answer = dp[7];
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
  (let* ([m (length board)]
         [n (if (null? board) 0 (length (first board)))]
         [L (min m 6)]
         ;; precompute top L rows for each column
         [top-cols
          (for/vector ([c n])
            (let* ([pairs
                    (for/list ([r m])
                      (list r (list-ref (list-ref board r) c)))]
                   [sorted (sort pairs > #:key (lambda (p) (second p)))])
              (if (> (length sorted) L)
                  (take sorted L)
                  sorted)))])
    (define best -4000000000) ; less than minimal possible sum (-3e9)
    (for ([c1 (in-range n)])
      (for ([c2 (in-range (+ c1 1) n)])
        (for ([c3 (in-range (+ c2 1) n)])
          (let* ([list1 (vector-ref top-cols c1)]
                 [list2 (vector-ref top-cols c2)]
                 [list3 (vector-ref top-cols c3)])
            (for ([p1 list1])
              (define r1 (first p1))
              (define v1 (second p1))
              (for ([p2 list2])
                (define r2 (first p2))
                (when (not (= r1 r2))
                  (define v2 (second p2))
                  (for ([p3 list3])
                    (define r3 (first p3))
                    (when (and (not (= r1 r3)) (not (= r2 r3)))
                      (define sum (+ v1 v2 (second p3)))
                      (when (> sum best)
                        (set! best sum))))))))))))
    best)))
```

## Erlang

```erlang
-spec maximum_value_sum(Board :: [[integer()]]) -> integer().
maximum_value_sum(Board) ->
    M = length(Board),
    N = case Board of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    PairMap = build_pair_map(Board, M, N, #{}),
    MinVal = -1 bsl 60,
    max_triple_sum(0, M, N, Board, PairMap, MinVal).

%% Build map of pair (I,J) -> list of best sums excluding each column
build_pair_map(_Board, I, _N, Acc) when I >= length(_Board) ->
    Acc;
build_pair_map(Board, I, N, Acc) ->
    Acc1 = build_pair_row(I, I+1, Board, N, Acc),
    build_pair_map(Board, I+1, N, Acc1).

build_pair_row(_I, J, _Board, _N, Acc) when J >= length(_Board) ->
    Acc;
build_pair_row(I, J, Board, N, Acc) ->
    RowI = lists:nth(I+1, Board),
    RowJ = lists:nth(J+1, Board),
    Sorted = sort_sums(RowI, RowJ, N),
    BestExcl = best_excluding(N, Sorted),
    NewAcc = maps:put({I,J}, BestExcl, Acc),
    build_pair_row(I, J+1, Board, N, NewAcc).

%% Generate all sums for distinct columns and sort descending
sort_sums(RowI, RowJ, N) ->
    Sums = [{RowIVal + RowJVal, C1, C2} ||
            C1 <- lists:seq(0, N-1),
            C2 <- lists:seq(0, N-1),
            C1 =/= C2,
            RowIVal = lists:nth(C1+1, RowI),
            RowJVal = lists:nth(C2+1, RowJ)],
    lists:sort(fun({S1,_,_}, {S2,_,_}) -> S1 > S2 end, Sums).

%% For each excluded column compute the best sum not using it
best_excluding(N, Sorted) ->
    [find_best_for_excl(E, Sorted) || E <- lists:seq(0, N-1)].

find_best_for_excl(Excl, [{Sum,C1,C2}|Rest]) ->
    if C1 =/= Excl, C2 =/= Excl -> Sum;
       true -> find_best_for_excl(Excl, Rest)
    end;
find_best_for_excl(_Excl, []) -> 0.

%% Iterate over all triples of rows and compute maximum sum
max_triple_sum(I, M, N, Board, PairMap, CurrentMax) when I >= M-2 ->
    CurrentMax;
max_triple_sum(I, M, N, Board, PairMap, CurrentMax) ->
    MaxAfterJ = max_triple_j(I, I+1, M, N, Board, PairMap, CurrentMax),
    max_triple_sum(I+1, M, N, Board, PairMap, MaxAfterJ).

max_triple_j(_I, J, M, _N, _Board, _PairMap, Cur) when J >= M-1 ->
    Cur;
max_triple_j(I, J, M, N, Board, PairMap, Cur) ->
    MaxAfterK = max_triple_k(I, J, J+1, M, N, Board, PairMap, Cur),
    max_triple_j(I, J+1, M, N, Board, PairMap, MaxAfterK).

max_triple_k(_I, _J, K, M, _N, _Board, _PairMap, Cur) when K >= M ->
    Cur;
max_triple_k(I, J, K, M, N, Board, PairMap, Cur) ->
    RowI = lists:nth(I+1, Board),
    PairBest = maps:get({J,K}, PairMap),
    NewMax = max_for_row_i(RowI, PairBest, N, Cur),
    max_triple_k(I, J, K+1, M, N, Board, PairMap, NewMax).

max_for_row_i(_RowI, _PairBest, 0, Max) ->
    Max;
max_for_row_i(RowI, PairBest, ColIdx, Max) when ColIdx > 0 ->
    C = ColIdx - 1,
    ValI = lists:nth(C+1, RowI),
    Sum = ValI + lists:nth(C+1, PairBest),
    NewMax = if Sum > Max -> Sum; true -> Max end,
    max_for_row_i(RowI, PairBest, C, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_value_sum(board :: [[integer]]) :: integer
  def maximum_value_sum(board) do
    m = length(board)
    n = length(hd(board))
    inf = -9_223_372_036_854_775_808

    max_sum =
      Enum.reduce(0..(m - 3), inf, fn i, acc_i ->
        Enum.reduce((i + 1)..(m - 2), acc_i, fn j, acc_j ->
          Enum.reduce((j + 1)..(m - 1), acc_j, fn k, acc_k ->
            dp = :array.new(8, default: inf) |> :array.set(0, 0)
            final_dp =
              Enum.reduce(0..(n - 1), dp, fn col, cur_dp ->
                vi = Enum.at(board[i], col)
                vj = Enum.at(board[j], col)
                vk = Enum.at(board[k], col)

                Enum.reduce(Enum.reverse(0..7), cur_dp, fn mask, dp_acc ->
                  cur_val = :array.get(mask, dp_acc)

                  if cur_val == inf do
                    dp_acc
                  else
                    dp1 =
                      if (mask &&& 1) == 0 do
                        new_mask = mask ||| 1
                        val = cur_val + vi
                        old = :array.get(new_mask, dp_acc)
                        if val > old, do: :array.set(new_mask, val, dp_acc), else: dp_acc
                      else
                        dp_acc
                      end

                    dp2 =
                      if (mask &&& 2) == 0 do
                        new_mask = mask ||| 2
                        val = cur_val + vj
                        old = :array.get(new_mask, dp1)
                        if val > old, do: :array.set(new_mask, val, dp1), else: dp1
                      else
                        dp1
                      end

                    dp3 =
                      if (mask &&& 4) == 0 do
                        new_mask = mask ||| 4
                        val = cur_val + vk
                        old = :array.get(new_mask, dp2)
                        if val > old, do: :array.set(new_mask, val, dp2), else: dp2
                      else
                        dp2
                      end

                    dp3
                  end
                end)
              end)

            cur_max = :array.get(7, final_dp)
            if cur_max > acc_k, do: cur_max, else: acc_k
          end)
        end)
      end)

    max_sum
  end
end
```

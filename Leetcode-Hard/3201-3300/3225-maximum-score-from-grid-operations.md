# 3225. Maximum Score From Grid Operations

## Cpp

```cpp
class Solution {
public:
    long long maximumScore(vector<vector<int>>& grid) {
        int n = grid.size();
        // prefix sums for each column
        vector<vector<long long>> pref(n, vector<long long>(n + 1, 0));
        for (int col = 0; col < n; ++col) {
            for (int row = 0; row < n; ++row) {
                pref[col][row + 1] = pref[col][row] + grid[row][col];
            }
        }

        int H = n + 1; // possible heights: 0..n
        const long long NEG = LLONG_MIN / 4;
        vector<long long> dpPrev(H, 0), dpCur(H, NEG);

        for (int col = 1; col < n; ++col) {
            fill(dpCur.begin(), dpCur.end(), NEG);
            for (int prev = 0; prev <= n; ++prev) {
                if (dpPrev[prev] == NEG) continue;
                for (int cur = 0; cur <= n; ++cur) {
                    long long add = 0;
                    if (prev > cur) {
                        // current column is white in rows [cur, prev-1]
                        add = pref[col][prev] - pref[col][cur];
                    } else if (cur > prev) {
                        // previous column is white in rows [prev, cur-1]
                        add = pref[col - 1][cur] - pref[col - 1][prev];
                    }
                    long long cand = dpPrev[prev] + add;
                    if (cand > dpCur[cur]) dpCur[cur] = cand;
                }
            }
            dpPrev.swap(dpCur);
        }

        return *max_element(dpPrev.begin(), dpPrev.end());
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long maximumScore(int[][] grid) {
        int n = grid.length;
        long[][] pref = new long[n][n + 1];
        for (int col = 0; col < n; col++) {
            for (int row = 0; row < n; row++) {
                pref[col][row + 1] = pref[col][row] + grid[row][col];
            }
        }

        long NEG = Long.MIN_VALUE / 4;
        long[][] dp = new long[n][n + 1];
        for (int h = 0; h <= n; h++) {
            dp[0][h] = 0;
        }

        for (int col = 1; col < n; col++) {
            Arrays.fill(dp[col], NEG);
            for (int h = 0; h <= n; h++) {
                long best = NEG;
                for (int hp = 0; hp <= n; hp++) {
                    long prev = dp[col - 1][hp];
                    if (prev == NEG) continue;
                    long add;
                    if (hp > h) {
                        add = pref[col][hp] - pref[col][h];
                    } else if (h > hp) {
                        add = pref[col - 1][h] - pref[col - 1][hp];
                    } else {
                        add = 0;
                    }
                    long cand = prev + add;
                    if (cand > best) best = cand;
                }
                dp[col][h] = best;
            }
        }

        long ans = 0;
        for (int h = 0; h <= n; h++) {
            ans = Math.max(ans, dp[n - 1][h]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # prefix sums for each column
        pref = [[0] * (n + 1) for _ in range(n)]
        for col in range(n):
            s = 0
            pref[col][0] = 0
            for row in range(n):
                s += grid[row][col]
                pref[col][row + 1] = s

        INF_NEG = -10**18
        dp = [0] * (n + 1)  # dp[height of current column]

        for col in range(n - 1):
            new_dp = [INF_NEG] * (n + 1)
            for prev_h in range(n + 1):
                base = dp[prev_h]
                if base == INF_NEG:
                    continue
                pref_left = pref[col]
                pref_right = pref[col + 1]
                for cur_h in range(n + 1):
                    add = 0
                    if prev_h > cur_h:
                        # extra black rows in left column, white cells are in right column
                        add = pref_right[prev_h] - pref_right[cur_h]
                    elif cur_h > prev_h:
                        # extra black rows in right column, white cells are in left column
                        add = pref_left[cur_h] - pref_left[prev_h]
                    val = base + add
                    if val > new_dp[cur_h]:
                        new_dp[cur_h] = val
            dp = new_dp

        return max(dp)
```

## Python3

```python
import sys
from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # prefix sums for each column
        pref = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            s = 0
            col = pref[j]
            for i in range(n):
                s += grid[i][j]
                col[i + 1] = s

        NEG = -10**30
        dp = [[NEG] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # heights of dummy columns -2 and -1 are 0

        for col_idx in range(n):
            new_dp = [[NEG] * (n + 1) for _ in range(n + 1)]
            left_col = col_idx - 1
            pref_left = pref[left_col] if left_col >= 0 else None
            for h_leftprev in range(n + 1):
                row_dp = dp[h_leftprev]
                for h_curprev in range(n + 1):
                    base = row_dp[h_curprev]
                    if base == NEG:
                        continue
                    # try all possible height for current column
                    for h_cur in range(n + 1):
                        add = 0
                        if left_col >= 0:
                            max_h = h_leftprev if h_leftprev > h_cur else h_cur
                            if max_h > h_curprev:
                                add = pref_left[max_h] - pref_left[h_curprev]
                        val = base + add
                        if val > new_dp[h_curprev][h_cur]:
                            new_dp[h_curprev][h_cur] = val
            dp = new_dp

        ans = 0
        last_pref = pref[n - 1]
        for h_leftprev in range(n + 1):
            row_dp = dp[h_leftprev]
            for h_last in range(n + 1):
                cur = row_dp[h_last]
                if cur == NEG:
                    continue
                # right neighbor dummy height = 0
                max_h = h_leftprev  # since right is 0
                add = 0
                if max_h > h_last:
                    add = last_pref[max_h] - last_pref[h_last]
                total = cur + add
                if total > ans:
                    ans = total
        return ans
```

## C

```c
#include <stddef.h>
#include <limits.h>

long long maximumScore(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    if (n == 0) return 0;

    // prefix sums for each column
    static long long pref[101][101];
    for (int col = 0; col < n; ++col) {
        pref[col][0] = grid[0][col];
        for (int row = 1; row < n; ++row) {
            pref[col][row] = pref[col][row - 1] + grid[row][col];
        }
    }

    // helper lambda to get sum in column col from l..r inclusive
    #define COLSUM(col,l,r) ( ((l) > (r)) ? 0LL : ( (l)==0 ? pref[(col)][(r)] : pref[(col)][(r)] - pref[(col)][(l)-1] ) )

    int H = n + 1; // number of possible heights (-1 .. n-1)
    static long long dpPrev[101][101];
    static long long dpCurr[101][101];
    const long long NEG_INF = -(1LL<<60);

    for (int i = 0; i < H; ++i)
        for (int j = 0; j < H; ++j)
            dpPrev[i][j] = NEG_INF;

    // initialize for first column, a = -1 (index 0)
    for (int h = -1; h <= n - 1; ++h) {
        int idx = h + 1;
        dpPrev[0][idx] = 0LL;
    }

    // process columns 1 .. n-1
    for (int col = 1; col < n; ++col) {
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < H; ++j)
                dpCurr[i][j] = NEG_INF;

        for (int aIdx = 0; aIdx < H; ++aIdx) {
            for (int bIdx = 0; bIdx < H; ++bIdx) {
                long long base = dpPrev[aIdx][bIdx];
                if (base == NEG_INF) continue;
                int a = aIdx - 1; // height of column col-2
                int b = bIdx - 1; // height of column col-1

                for (int c = -1; c <= n - 1; ++c) {
                    int cIdx = c + 1; // height of current column col
                    int maxHeight = (a > c) ? a : c;
                    long long add = 0LL;
                    if (maxHeight > b) {
                        int L = b + 1;
                        int R = maxHeight;
                        add = COLSUM(col - 1, L, R);
                    }
                    long long val = base + add;
                    if (val > dpCurr[bIdx][cIdx]) dpCurr[bIdx][cIdx] = val;
                }
            }
        }

        // swap dpPrev and dpCurr
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < H; ++j)
                dpPrev[i][j] = dpCurr[i][j];
    }

    long long answer = 0LL;
    // finalize contribution of last column using right neighbor height = -1
    for (int aIdx = 0; aIdx < H; ++aIdx) {
        for (int bIdx = 0; bIdx < H; ++bIdx) {
            long long base = dpPrev[aIdx][bIdx];
            if (base == NEG_INF) continue;
            int a = aIdx - 1; // height of column n-2
            int b = bIdx - 1; // height of column n-1
            int c = -1;       // right neighbor absent
            int maxHeight = (a > c) ? a : c; // essentially a
            long long add = 0LL;
            if (maxHeight > b) {
                int L = b + 1;
                int R = maxHeight;
                add = COLSUM(n - 1, L, R);
            }
            long long total = base + add;
            if (total > answer) answer = total;
        }
    }

    #undef COLSUM
    return answer;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MaximumScore(int[][] grid) {
        int n = grid.Length;
        // Prefix sums for each column
        long[,] pref = new long[n, n + 1];
        for (int col = 0; col < n; col++) {
            pref[col, 0] = 0;
            for (int row = 0; row < n; row++) {
                pref[col, row + 1] = pref[col, row] + grid[row][col];
            }
        }

        int H = n; // heights from 0..n
        long NEG = long.MinValue / 4;

        long[,] dpPrev = new long[H + 1, H + 1];
        long[,] dpNext = new long[H + 1, H + 1];

        for (int i = 0; i <= H; i++) {
            for (int j = 0; j <= H; j++) {
                dpPrev[i, j] = NEG;
            }
        }

        // Initialize for first column: left height is 0
        for (int h0 = 0; h0 <= H; h0++) {
            dpPrev[0, h0] = 0;
        }

        // DP over columns
        for (int col = 0; col < n - 1; col++) {
            // reset dpNext to NEG
            for (int i = 0; i <= H; i++) {
                for (int j = 0; j <= H; j++) {
                    dpNext[i, j] = NEG;
                }
            }

            for (int leftH = 0; leftH <= H; leftH++) {
                for (int curH = 0; curH <= H; curH++) {
                    long val = dpPrev[leftH, curH];
                    if (val == NEG) continue;

                    for (int newH = 0; newH <= H; newH++) {
                        // contribution of column 'col' using leftH, curH, newH
                        int maxNeighbor = Math.Max(leftH, newH);
                        long add = 0;
                        if (maxNeighbor > curH) {
                            add = pref[col, maxNeighbor] - pref[col, curH];
                        }
                        long nv = val + add;
                        if (nv > dpNext[curH, newH]) {
                            dpNext[curH, newH] = nv;
                        }
                    }
                }
            }

            // swap
            var temp = dpPrev;
            dpPrev = dpNext;
            dpNext = temp;
        }

        long answer = NEG;

        // handle last column (n-1) with right neighbor height 0
        int lastCol = n - 1;
        for (int leftH = 0; leftH <= H; leftH++) {
            for (int curH = 0; curH <= H; curH++) {
                long val = dpPrev[leftH, curH];
                if (val == NEG) continue;

                int maxNeighbor = Math.Max(leftH, 0);
                long add = 0;
                if (maxNeighbor > curH) {
                    add = pref[lastCol, maxNeighbor] - pref[lastCol, curH];
                }
                long total = val + add;
                if (total > answer) answer = total;
            }
        }

        // Edge case when n == 1 (loop above not executed)
        if (n == 1) {
            answer = NEG;
            for (int h0 = 0; h0 <= H; h0++) {
                int maxNeighbor = Math.Max(0, 0);
                long add = 0;
                if (maxNeighbor > h0) {
                    add = pref[0, maxNeighbor] - pref[0, h0];
                }
                if (add > answer) answer = add;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumScore = function(grid) {
    const n = grid.length;
    // prefix sums for each column: pref[col][k] = sum of grid[0..k-1][col]
    const pref = Array.from({ length: n }, () => new Array(n + 1).fill(0));
    for (let col = 0; col < n; col++) {
        for (let row = 0; row < n; row++) {
            pref[col][row + 1] = pref[col][row] + grid[row][col];
        }
    }

    // dpPrev[h] = max score up to previous column with its height = h
    let dpPrev = new Array(n + 1).fill(0); // after processing column 0 (no contribution)

    for (let col = 1; col < n; col++) {
        const dpCurr = new Array(n + 1).fill(-Infinity);
        for (let hPrev = 0; hPrev <= n; hPrev++) {
            const base = dpPrev[hPrev];
            if (base === -Infinity) continue;
            for (let hCur = 0; hCur <= n; hCur++) {
                let add = 0;
                if (hPrev > hCur) {
                    // rows where column col-1 is black and column col is white
                    add = pref[col][hPrev] - pref[col][hCur];
                }
                const val = base + add;
                if (val > dpCurr[hCur]) dpCurr[hCur] = val;
            }
        }
        dpPrev = dpCurr;
    }

    let ans = 0;
    for (let h = 0; h <= n; h++) {
        if (dpPrev[h] > ans) ans = dpPrev[h];
    }
    return ans;
};
```

## Typescript

```typescript
function maximumScore(grid: number[][]): number {
    const n = grid.length;
    // prefix sums for each column
    const pre: number[][] = Array.from({ length: n }, () => new Array(n + 1).fill(0));
    for (let j = 0; j < n; ++j) {
        for (let i = 0; i < n; ++i) {
            pre[j][i + 1] = pre[j][i] + grid[i][j];
        }
    }

    const NEG_INF = -1e18;
    // dpPrev[h] = max score up to current column with its height = h
    let dpPrev: number[] = new Array(n + 1).fill(0); // first column, no contribution yet

    for (let col = 1; col < n; ++col) {
        const dpCurr: number[] = new Array(n + 1).fill(NEG_INF);
        for (let hPrev = 0; hPrev <= n; ++hPrev) {
            const base = dpPrev[hPrev];
            if (base === NEG_INF) continue;
            for (let hCurr = 0; hCurr <= n; ++hCurr) {
                let add: number;
                if (hPrev <= hCurr) {
                    // left column white, right column black
                    add = pre[col - 1][hCurr] - pre[col - 1][hPrev];
                } else {
                    // right column white, left column black
                    add = pre[col][hPrev] - pre[col][hCurr];
                }
                const val = base + add;
                if (val > dpCurr[hCurr]) dpCurr[hCurr] = val;
            }
        }
        dpPrev = dpCurr;
    }

    let ans = 0;
    for (let h = 0; h <= n; ++h) {
        if (dpPrev[h] > ans) ans = dpPrev[h];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumScore($grid) {
        $n = count($grid);
        // prefix sums for each column
        $pref = array_fill(0, $n, []);
        for ($j = 0; $j < $n; $j++) {
            $pref[$j] = array_fill(0, $n + 1, 0);
            for ($i = 0; $i < $n; $i++) {
                $pref[$j][$i + 1] = $pref[$j][$i] + $grid[$i][$j];
            }
        }

        $NEG = -PHP_INT_MAX;
        // dpPrev[height_of_last_column][height_of_before_last] = max score
        $dpPrev = [];
        for ($h = 0; $h <= $n; $h++) {
            $dpPrev[$h] = array_fill(0, $n + 1, $NEG);
            // imaginary column before the first has height 0
            $dpPrev[$h][0] = 0;
        }

        for ($col = 1; $col < $n; $col++) {
            $newdp = [];
            for ($h = 0; $h <= $n; $h++) {
                $newdp[$h] = array_fill(0, $n + 1, $NEG);
            }
            $prefCol = $pref[$col - 1];
            for ($prevHeight = 0; $prevHeight <= $n; $prevHeight++) {
                $rowPrev = $dpPrev[$prevHeight];
                for ($prevPrevHeight = 0; $prevPrevHeight <= $n; $prevPrevHeight++) {
                    $base = $rowPrev[$prevPrevHeight];
                    if ($base === $NEG) continue;
                    $startBase = max($prevHeight, $prevPrevHeight);
                    // iterate possible height for current column
                    for ($h = 0; $h <= $n; $h++) {
                        $add = 0;
                        if ($h > $startBase) {
                            $add = $prefCol[$h] - $prefCol[$startBase];
                        }
                        $val = $base + $add;
                        if ($val > $newdp[$h][$prevHeight]) {
                            $newdp[$h][$prevHeight] = $val;
                        }
                    }
                }
            }
            $dpPrev = $newdp;
        }

        $ans = $NEG;
        for ($h = 0; $h <= $n; $h++) {
            for ($prev = 0; $prev <= $n; $prev++) {
                if ($dpPrev[$h][$prev] > $ans) {
                    $ans = $dpPrev[$h][$prev];
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
    func maximumScore(_ grid: [[Int]]) -> Int {
        let n = grid.count
        // Prefix sums for each column
        var pref = Array(repeating: Array(repeating: Int64(0), count: n + 1), count: n)
        for col in 0..<n {
            var sum: Int64 = 0
            pref[col][0] = 0
            for row in 0..<n {
                sum += Int64(grid[row][col])
                pref[col][row + 1] = sum
            }
        }

        let size = n + 1
        let INF = Int64.min / 4

        // dp[leftHeight][midHeight] = max score up to current column (exclusive)
        var dp = Array(repeating: Array(repeating: INF, count: size), count: size)
        for h0 in 0...n {
            dp[0][h0] = 0   // dummy left height = 0 before first column
        }

        if n >= 2 {
            for col in 1..<n {          // processing column 'col' as the new right neighbor
                var newDP = Array(repeating: Array(repeating: INF, count: size), count: size)
                let prefPrev = pref[col - 1]   // prefix of column col-1 whose contribution we finalize now
                for left in 0...n {
                    let dpLeft = dp[left]
                    for mid in 0...n {
                        let curVal = dpLeft[mid]
                        if curVal == INF { continue }
                        for cur in 0...n {
                            var add: Int64 = 0
                            let maxH = left > cur ? left : cur
                            if maxH > mid {
                                add = prefPrev[maxH] - prefPrev[mid]
                            }
                            let total = curVal + add
                            if total > newDP[mid][cur] {
                                newDP[mid][cur] = total
                            }
                        }
                    }
                }
                dp = newDP
            }
        }

        // Finalize contribution of the last column (right dummy height = 0)
        var answer: Int64 = 0
        let prefLast = pref[n - 1]
        for left in 0...n {
            let dpLeft = dp[left]
            for mid in 0...n {
                let curVal = dpLeft[mid]
                if curVal == INF { continue }
                var add: Int64 = 0
                // right dummy height is 0, so max(left,0) = left
                if left > mid {
                    add = prefLast[left] - prefLast[mid]
                }
                let total = curVal + add
                if total > answer { answer = total }
            }
        }

        return Int(answer)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun maximumScore(grid: Array<IntArray>): Long {
        val n = grid.size
        if (n == 0) return 0L

        // prefix sums per column
        val colPref = Array(n) { LongArray(n + 1) }
        for (j in 0 until n) {
            var sum = 0L
            colPref[j][0] = 0L
            for (i in 0 until n) {
                sum += grid[i][j].toLong()
                colPref[j][i + 1] = sum
            }
        }

        val NEG = Long.MIN_VALUE / 4
        var dpPrev = Array(n + 1) { LongArray(n + 1) { NEG } }
        // dummy left height = 0, set initial heights for column 0
        for (h0 in 0..n) {
            dpPrev[0][h0] = 0L
        }

        // process columns 1 .. n-1
        for (col in 1 until n) {
            val dpNext = Array(n + 1) { LongArray(n + 1) { NEG } }
            for (a in 0..n) {
                for (b in 0..n) {
                    val curVal = dpPrev[a][b]
                    if (curVal == NEG) continue
                    for (c in 0..n) {
                        var add = 0L
                        val maxH = if (a > c) a else c
                        if (maxH > b) {
                            add = colPref[col - 1][maxH] - colPref[col - 1][b]
                        }
                        val newVal = curVal + add
                        if (newVal > dpNext[b][c]) {
                            dpNext[b][c] = newVal
                        }
                    }
                }
            }
            dpPrev = dpNext
        }

        var answer = 0L
        // finalize contribution of last column (n-1) with right neighbor height = 0
        for (a in 0..n) {
            for (b in 0..n) {
                val curVal = dpPrev[a][b]
                if (curVal == NEG) continue
                var add = 0L
                val maxH = a // right neighbor height is 0
                if (maxH > b) {
                    add = colPref[n - 1][maxH] - colPref[n - 1][b]
                }
                val total = curVal + add
                if (total > answer) answer = total
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximumScore(List<List<int>> grid) {
    int n = grid.length;
    // Prefix sums for each column
    List<List<int>> pref = List.generate(n, (_) => List.filled(n + 1, 0));
    for (int j = 0; j < n; j++) {
      for (int i = 0; i < n; i++) {
        pref[j][i + 1] = pref[j][i] + grid[i][j];
      }
    }

    const int NEG_INF = -(1 << 60);
    // dp[col][h] = max score up to column 'col' with height h at this column
    List<List<int>> dp =
        List.generate(n, (_) => List.filled(n + 1, NEG_INF));

    for (int h = 0; h <= n; h++) {
      dp[0][h] = 0;
    }

    for (int col = 1; col < n; col++) {
      for (int hCur = 0; hCur <= n; hCur++) {
        int best = NEG_INF;
        for (int hPrev = 0; hPrev <= n; hPrev++) {
          int contrib = 0;
          if (hPrev > hCur) {
            // left column higher: add right column cells in [hCur, hPrev-1]
            contrib = pref[col][hPrev] - pref[col][hCur];
          } else if (hCur > hPrev) {
            // right column higher: add left column cells in [hPrev, hCur-1]
            contrib = pref[col - 1][hCur] - pref[col - 1][hPrev];
          }
          int val = dp[col - 1][hPrev] + contrib;
          if (val > best) best = val;
        }
        dp[col][hCur] = best;
      }
    }

    int ans = 0;
    for (int h = 0; h <= n; h++) {
      if (dp[n - 1][h] > ans) ans = dp[n - 1][h];
    }
    return ans;
  }
}
```

## Golang

```go
func maximumScore(grid [][]int) int64 {
    n := len(grid)
    if n == 0 {
        return 0
    }
    // prefix sums for each column
    colPref := make([][]int64, n)
    for j := 0; j < n; j++ {
        colPref[j] = make([]int64, n+1)
        for i := 0; i < n; i++ {
            colPref[j][i+1] = colPref[j][i] + int64(grid[i][j])
        }
    }

    // dpPrev[h] = max score up to previous column with height h
    dpPrev := make([]int64, n+1)
    for h := 0; h <= n; h++ {
        dpPrev[h] = 0
    }

    const INF int64 = -1 << 60

    for col := 1; col < n; col++ {
        dpCurr := make([]int64, n+1)
        for h := 0; h <= n; h++ {
            best := INF
            for hp := 0; hp <= n; hp++ {
                val := dpPrev[hp]
                if hp > h { // left column higher, right lower
                    val += colPref[col][hp+1] - colPref[col][h+1]
                } else if h > hp { // right column higher, left lower
                    val += colPref[col-1][h+1] - colPref[col-1][hp+1]
                }
                if val > best {
                    best = val
                }
            }
            dpCurr[h] = best
        }
        dpPrev = dpCurr
    }

    ans := int64(0)
    for h := 0; h <= n; h++ {
        if dpPrev[h] > ans {
            ans = dpPrev[h]
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_score(grid)
  n = grid.length
  pref = Array.new(n) { Array.new(n + 1, 0) }
  (0...n).each do |j|
    sum = 0
    (0...n).each do |i|
      sum += grid[i][j]
      pref[j][i + 1] = sum
    end
  end

  dp_prev = Array.new(n + 1, 0)

  (1...n).each do |col|
    dp_cur = Array.new(n + 1, -Float::INFINITY)
    (0..n).each do |h|
      best = -Float::INFINITY
      (0..n).each do |hp|
        add =
          if hp > h
            pref[col][hp] - pref[col][h]
          elsif h > hp
            pref[col - 1][h] - pref[col - 1][hp]
          else
            0
          end
        total = dp_prev[hp] + add
        best = total if total > best
      end
      dp_cur[h] = best
    end
    dp_prev = dp_cur
  end

  dp_prev.max
end
```

## Scala

```scala
object Solution {
    def maximumScore(grid: Array[Array[Int]]): Long = {
        val n = grid.length
        if (n <= 1) return 0L

        // prefix sums per column
        val pref = Array.ofDim[Long](n, n + 1)
        var c = 0
        while (c < n) {
            var sum: Long = 0L
            pref(c)(0) = 0L
            var r = 0
            while (r < n) {
                sum += grid(r)(c).toLong
                pref(c)(r + 1) = sum
                r += 1
            }
            c += 1
        }

        // helper to compute contribution for a column given heights
        def contrib(col: Int, hSelf: Int, H: Int): Long = {
            if (H <= hSelf) 0L
            else pref(col)(H + 1) - pref(col)(hSelf + 1)
        }

        val m = n + 1 // number of possible heights (-1 .. n-1), index = height+1
        val NEG = Long.MinValue / 4

        var cur = Array.fill[Long](m, m)(NEG)
        // initialize with column 0 height choices, left neighbor is -1 (index 0)
        var h0 = -1
        while (h0 <= n - 1) {
            val idxPrevPrev = 0               // height -1
            val idxPrev = h0 + 1
            cur(idxPrevPrev)(idxPrev) = 0L
            h0 += 1
        }

        var col = 1
        while (col < n) { // processing column 'col' as the new right neighbor
            val next = Array.fill[Long](m, m)(NEG)
            var ppIdx = 0
            while (ppIdx < m) {
                var pIdx = 0
                while (pIdx < m) {
                    val baseScore = cur(ppIdx)(pIdx)
                    if (baseScore != NEG) {
                        val hPrevPrev = ppIdx - 1
                        val hPrev = pIdx - 1
                        var hCurr = -1
                        while (hCurr <= n - 1) {
                            val maxAdj = if (hPrevPrev > hCurr) hPrevPrev else hCurr
                            val added = contrib(col - 1, hPrev, maxAdj)
                            val newScore = baseScore + added
                            val newPpIdx = pIdx          // becomes previous height
                            val newPIdx = hCurr + 1       // current height index
                            if (newScore > next(newPpIdx)(newPIdx)) {
                                next(newPpIdx)(newPIdx) = newScore
                            }
                            hCurr += 1
                        }
                    }
                    pIdx += 1
                }
                ppIdx += 1
            }
            cur = next
            col += 1
        }

        // finalize contribution for the last column (n-1)
        var answer: Long = NEG
        var ppIdx = 0
        while (ppIdx < m) {
            var pIdx = 0
            while (pIdx < m) {
                val baseScore = cur(ppIdx)(pIdx)
                if (baseScore != NEG) {
                    val hPrevPrev = ppIdx - 1   // height of column n-2
                    val hLast = pIdx - 1        // height of column n-1
                    val added = contrib(n - 1, hLast, hPrevPrev)
                    val total = baseScore + added
                    if (total > answer) answer = total
                }
                pIdx += 1
            }
            ppIdx += 1
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_score(grid: Vec<Vec<i32>>) -> i64 {
        let n = grid.len();
        if n <= 1 {
            return 0;
        }
        let h = n + 1; // possible heights 0..n
        // prefix sums for each column
        let mut pref: Vec<Vec<i64>> = vec![vec![0; h]; n];
        for col in 0..n {
            for row in 0..n {
                pref[col][row + 1] = pref[col][row] + grid[row][col] as i64;
            }
        }

        const NEG_INF: i64 = i64::MIN / 4;

        // dp[prev][last] where prev = h_{i-2}, last = h_{i-1}
        let mut dp: Vec<Vec<i64>> = vec![vec![NEG_INF; h]; h];

        // initialize with first two columns (indices 0 and 1)
        for h0 in 0..=n {
            for h1 in 0..=n {
                let contrib = if h1 > h0 {
                    pref[0][h1] - pref[0][h0]
                } else {
                    0
                };
                dp[h0][h1] = dp[h0][h1].max(contrib);
            }
        }

        // process columns 2 .. n-1
        for col in 2..n {
            let mut ndp: Vec<Vec<i64>> = vec![vec![NEG_INF; h]; h];
            for prev in 0..=n {
                for last in 0..=n {
                    let cur_val = dp[prev][last];
                    if cur_val == NEG_INF {
                        continue;
                    }
                    for cur in 0..=n {
                        let max_neighbor = if prev > cur { prev } else { cur };
                        let contrib = if max_neighbor > last {
                            pref[col - 1][max_neighbor] - pref[col - 1][last]
                        } else {
                            0
                        };
                        let new_val = cur_val + contrib;
                        if new_val > ndp[last][cur] {
                            ndp[last][cur] = new_val;
                        }
                    }
                }
            }
            dp = ndp;
        }

        // add contribution of the last column (n-1) using only left neighbor
        let mut answer: i64 = 0;
        for prev in 0..=n {
            for last in 0..=n {
                let cur_val = dp[prev][last];
                if cur_val == NEG_INF {
                    continue;
                }
                let contrib_last = if prev > last {
                    pref[n - 1][prev] - pref[n - 1][last]
                } else {
                    0
                };
                answer = answer.max(cur_val + contrib_last);
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (maximum-score grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (grid-v (list->vector (map list->vector grid)))
         ;; prefix sums for each column
         (prefix (make-vector n)))
    ;; build column-wise prefix sums
    (do ((j 0 (+ j 1))) ((= j n))
      (let ((pref (make-vector (+ n 1) 0)))
        (do ((i 0 (+ i 1))) ((= i n))
          (vector-set! pref (+ i 1)
                       (+ (vector-ref pref i)
                          (vector-ref (vector-ref grid-v i) j))))
        (vector-set! prefix j pref)))
    ;; DP tables: dp[last][before] = max score so far
    (define INF -1000000000000000)
    (define dp (make-vector (+ n 1)))
    (do ((i 0 (+ i 1))) ((= i (+ n 1)))
      (vector-set! dp i (make-vector (+ n 1) INF)))
    ;; initial state: no columns processed, heights are zero
    (vector-set! (vector-ref dp 0) 0 0)
    ;; process each column
    (do ((col 0 (+ col 1))) ((= col n))
      (let ((newdp (make-vector (+ n 1))))
        (do ((i 0 (+ i 1))) ((= i (+ n 1)))
          (vector-set! newdp i (make-vector (+ n 1) INF)))
        ;; transition
        (do ((last 0 (+ last 1))) ((> last n))
          (let ((rowvec (vector-ref dp last)))
            (do ((before 0 (+ before 1))) ((> before n))
              (let ((val (vector-ref rowvec before)))
                (when (> val INF)
                  (do ((cur 0 (+ cur 1))) ((> cur n))
                    (define add 0)
                    (when (> col 0)
                      (define start (max last before))
                      (define end (- cur 1))
                      (when (<= start end)
                        (let* ((pref (vector-ref prefix (- col 1)))
                               (sum (- (vector-ref pref (+ end 1))
                                       (vector-ref pref start))))
                          (set! add sum))))
                    (let* ((newrow (vector-ref newdp cur))
                           (prev (vector-ref newrow last))
                           (candidate (+ val add)))
                      (when (> candidate prev)
                        (vector-set! newrow last candidate))))))))))
        (set! dp newdp)))
    ;; add contributions for the last column from its left neighbor
    (define ans INF)
    (do ((last 0 (+ last 1))) ((> last n))
      (do ((before 0 (+ before 1))) ((> before n))
        (let ((val (vector-ref (vector-ref dp last) before)))
          (when (> val INF)
            (define extra 0)
            (when (> before last)
              (let* ((pref (vector-ref prefix (- n 1)))
                     (sum (- (vector-ref pref before)
                             (vector-ref pref last))))
                (set! extra sum)))
            (define total (+ val extra))
            (when (> total ans) (set! ans total))))))
    ans)))
```

## Erlang

```erlang
-spec maximum_score(Grid :: [[integer()]]) -> integer().
maximum_score(Grid) ->
    N = length(Grid),
    Size = (N + 1) * (N + 1),
    NegInf = -1000000000000000,
    %% build column prefix sums as tuples for O(1) access
    ColPrefTuples = list_to_tuple(build_col_prefixes(Grid, N)),
    %% initial dp state: heights of column -2 and -1 are both 0
    Idx00 = idx(0, 0, N),
    DP0 = array:new(Size, {default, NegInf}),
    DPInit = array:set(Idx00, 0, DP0),
    %% iterate over columns
    FinalDP = column_loop(0, N, DPInit, ColPrefTuples, NegInf),
    %% compute answer adding contribution of last column with right neighbor height 0
    Pairs = [{L, B} || L <- lists:seq(0, N), B <- lists:seq(0, N)],
    lists:foldl(
        fun({Last, Before}, Acc) ->
            Val = array:get(idx(Last, Before, N), FinalDP),
            if
                Val == NegInf -> Acc;
                true ->
                    Add = column_contrib(ColPrefTuples, N - 1, Last, Before, 0),
                    Total = Val + Add,
                    if Total > Acc -> Total; true -> Acc end
            end
        end,
        NegInf,
        Pairs).

%% Build prefix sums for each column, returns list of tuples (length N+1)
build_col_prefixes(Grid, N) ->
    build_col_prefixes(0, N, Grid, []).

build_col_prefixes(C, N, _Grid, Acc) when C >= N -> lists:reverse(Acc);
build_col_prefixes(C, N, Grid, Acc) ->
    PrefixList = column_prefix(Grid, C, N),
    build_col_prefixes(C + 1, N, Grid, [list_to_tuple(PrefixList) | Acc]).

%% Compute prefix sums for a single column C
column_prefix(Grid, C, N) ->
    column_prefix(0, N, Grid, C, [0]).

column_prefix(R, N, _Grid, _C, PrefixAcc) when R >= N -> lists:reverse(PrefixAcc);
column_prefix(R, N, Grid, C, PrefixAcc) ->
    Row = lists:nth(R + 1, Grid),
    Val = lists:nth(C + 1, Row),
    [PrevSum | _] = PrefixAcc,
    NewSum = PrevSum + Val,
    column_prefix(R + 1, N, Grid, C, [NewSum | PrefixAcc]).

%% Loop over columns to fill DP
column_loop(I, N, DPCurrent, ColPrefTuples, NegInf) when I >= N ->
    DPCurrent;
column_loop(I, N, DPCurrent, ColPrefTuples, NegInf) ->
    Size = (N + 1) * (N + 1),
    DPNext = array:new(Size, {default, NegInf}),
    Pairs = [{L, B} || L <- lists:seq(0, N), B <- lists:seq(0, N)],
    IsFirst = (I == 0),
    NewDP = lists:foldl(
        fun({Last, Before}, AccDP) ->
            Val = array:get(idx(Last, Before, N), DPCurrent),
            if
                Val == NegInf -> AccDP;
                true ->
                    process_heights(I, IsFirst, Last, Before, Val,
                                    ColPrefTuples, N, AccDP)
            end
        end,
        DPNext,
        Pairs),
    column_loop(I + 1, N, NewDP, ColPrefTuples, NegInf).

%% Process all possible new heights for a given state
process_heights(ColIdx, IsFirst, Last, Before, Val,
                ColPrefTuples, N, DPAcc) ->
    Heights = lists:seq(0, N),
    lists:foldl(
        fun(H, AccDP) ->
            Add = if
                      IsFirst -> 0;
                      true -> column_contrib(ColPrefTuples, ColIdx - 1,
                                            Last, Before, H)
                  end,
            NewVal = Val + Add,
            Idx2 = idx(H, Last, N),
            Prev = array:get(Idx2, AccDP),
            MaxV = if NewVal > Prev -> NewVal; true -> Prev end,
            array:set(Idx2, MaxV, AccDP)
        end,
        DPAcc,
        Heights).

%% Contribution of column C given its own height Hc and neighbor heights
column_contrib(ColPrefTuples, C, Hc, LeftH, RightH) ->
    Max = max(LeftH, RightH),
    if
        Max =< Hc -> 0;
        true ->
            PrefTuple = element(C + 1, ColPrefTuples),
            element(Max + 1, PrefTuple) - element(Hc + 1, PrefTuple)
    end.

%% Convert (lastHeight, beforeLastHeight) to single index
idx(Last, Before, N) -> Last * (N + 1) + Before.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_score(grid :: [[integer]]) :: integer
  def maximum_score(grid) do
    n = length(grid)
    size = n + 1
    neg_inf = -1_000_000_000_000_000_000

    # build column prefix sums as Erlang arrays
    prefixes =
      Enum.map(0..n - 1, fn j ->
        arr = :array.new(n + 1, default: 0)

        {arr_filled, _} =
          Enum.reduce(0..n - 1, {arr, 0}, fn i, {a, sum} ->
            val = grid |> Enum.at(i) |> Enum.at(j)
            new_sum = sum + val
            a2 = :array.set(i + 1, new_sum, a)
            {a2, new_sum}
          end)

        arr_filled
      end)

    # initial dp: map of {prevPrevHeight, prevHeight} -> score
    dp0 = %{{0, 0} => 0}

    dp_final =
      Enum.reduce(0..n - 1, dp0, fn col_idx, dp ->
        pref = if col_idx > 0, do: Enum.at(prefixes, col_idx - 1), else: nil

        Enum.reduce(dp, %{}, fn {{a, b}, cur_score}, acc ->
          Enum.reduce(0..n, acc, fn c, acc2 ->
            add =
              if pref == nil do
                0
              else
                max_h = if a > c, do: a, else: c

                if max_h <= b do
                  0
                else
                  :array.get(max_h, pref) - :array.get(b, pref)
                end
              end

            new_score = cur_score + add
            key = {b, c}
            existing = Map.get(acc2, key, neg_inf)

            if new_score > existing do
              Map.put(acc2, key, new_score)
            else
              acc2
            end
          end)
        end)
      end)

    # finalize contributions for the last real column using right sentinel height 0
    pref_last = Enum.at(prefixes, n - 1)

    ans =
      Enum.reduce(dp_final, neg_inf, fn {{a, b}, cur_score}, best ->
        max_h = a

        add =
          if max_h <= b do
            0
          else
            :array.get(max_h, pref_last) - :array.get(b, pref_last)
          end

        total = cur_score + add
        if total > best, do: total, else: best
      end)

    ans
  end
end
```

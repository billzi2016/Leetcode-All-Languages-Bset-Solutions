# 3418. Maximum Amount of Money Robot Can Earn

## Cpp

```cpp
class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        int m = coins.size();
        int n = coins[0].size();
        const long long NEG = LLONG_MIN / 4;
        vector<vector<array<long long,3>>> dp(m, vector<array<long long,3>>(n));
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                dp[i][j] = {NEG, NEG, NEG};

        // initialize start cell
        if (coins[0][0] >= 0) {
            dp[0][0][0] = coins[0][0];
        } else {
            dp[0][0][0] = coins[0][0];   // not neutralized
            dp[0][0][1] = 0;             // neutralized
        }

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) continue;
                array<long long,3> best = {NEG, NEG, NEG};

                auto process = [&](const array<long long,3>& prev) {
                    for (int k = 0; k <= 2; ++k) {
                        if (prev[k] == NEG) continue;
                        long long val = coins[i][j];
                        // take value as is
                        best[k] = max(best[k], prev[k] + val);
                        // neutralize if negative and we have remaining capacity
                        if (val < 0 && k < 2) {
                            best[k+1] = max(best[k+1], prev[k]); // add 0 instead of val
                        }
                    }
                };

                if (i > 0) process(dp[i-1][j]);
                if (j > 0) process(dp[i][j-1]);

                dp[i][j] = best;
            }
        }

        long long ans = NEG;
        for (int k = 0; k <= 2; ++k) ans = max(ans, dp[m-1][n-1][k]);
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int maximumAmount(int[][] coins) {
        int m = coins.length;
        int n = coins[0].length;
        int K = 2; // maximum neutralizations
        int NEG_INF = Integer.MIN_VALUE / 4;

        int[][][] dp = new int[m][n][K + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k <= K; k++) {
                    dp[i][j][k] = NEG_INF;
                }
            }
        }

        // initialize start cell
        dp[0][0][0] = coins[0][0];
        for (int k = 1; k <= K; k++) {
            dp[0][0][k] = 0; // neutralize the starting cell
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int k = 0; k <= K; k++) {
                    int bestNot = NEG_INF;
                    if (i > 0) bestNot = Math.max(bestNot, dp[i - 1][j][k]);
                    if (j > 0) bestNot = Math.max(bestNot, dp[i][j - 1][k]);
                    if (bestNot != NEG_INF) {
                        dp[i][j][k] = bestNot + coins[i][j];
                    }
                    if (k > 0) {
                        int bestNeu = NEG_INF;
                        if (i > 0) bestNeu = Math.max(bestNeu, dp[i - 1][j][k - 1]);
                        if (j > 0) bestNeu = Math.max(bestNeu, dp[i][j - 1][k - 1]);
                        if (bestNeu != NEG_INF) {
                            dp[i][j][k] = Math.max(dp[i][j][k], bestNeu); // neutralize current cell
                        }
                    }
                }
            }
        }

        int ans = NEG_INF;
        for (int k = 0; k <= K; k++) {
            ans = Math.max(ans, dp[m - 1][n - 1][k]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        m = len(coins)
        n = len(coins[0])
        NEG_INF = -10**15

        # dp[i][j][k]: max profit to reach (i,j) using k neutralizations
        dp = [[[NEG_INF] * 3 for _ in range(n)] for __ in range(m)]

        # initialize start cell
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # use one neutralization here

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cell_val = coins[i][j]
                for k in range(3):
                    best = NEG_INF

                    # come from top without using a new neutralization
                    if i > 0:
                        prev = dp[i-1][j][k]
                        if prev != NEG_INF:
                            best = max(best, prev + cell_val)

                    # come from left without using a new neutralization
                    if j > 0:
                        prev = dp[i][j-1][k]
                        if prev != NEG_INF:
                            best = max(best, prev + cell_val)

                    # use a neutralization on this cell (only useful if negative)
                    if cell_val < 0 and k > 0:
                        cand = NEG_INF
                        if i > 0:
                            prev = dp[i-1][j][k-1]
                            if prev != NEG_INF:
                                cand = max(cand, prev)   # add 0 instead of negative value
                        if j > 0:
                            prev = dp[i][j-1][k-1]
                            if prev != NEG_INF:
                                cand = max(cand, prev)
                        best = max(best, cand)

                    dp[i][j][k] = best

        return max(dp[m-1][n-1])
```

## Python3

```python
from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = -10**15
        dp = [[[NEG_INF] * 3 for _ in range(n)] for __ in range(m)]

        # initialize start cell
        dp[0][0][0] = coins[0][0]
        neutral_start = max(coins[0][0], 0)
        dp[0][0][1] = neutral_start
        dp[0][0][2] = neutral_start

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    best = NEG_INF
                    # move from top without using a new neutralization
                    if i > 0:
                        prev = dp[i - 1][j][k]
                        if prev != NEG_INF:
                            best = max(best, prev + coins[i][j])
                    # move from left without using a new neutralization
                    if j > 0:
                        prev = dp[i][j - 1][k]
                        if prev != NEG_INF:
                            best = max(best, prev + coins[i][j])
                    # use a neutralization on current cell (if any left)
                    if k > 0:
                        if i > 0:
                            prev = dp[i - 1][j][k - 1]
                            if prev != NEG_INF:
                                best = max(best, prev)   # add 0
                        if j > 0:
                            prev = dp[i][j - 1][k - 1]
                            if prev != NEG_INF:
                                best = max(best, prev)
                    dp[i][j][k] = best

        return max(dp[m - 1][n - 1])
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int maximumAmount(int** coins, int coinsSize, int* coinsColSize) {
    int m = coinsSize;
    int n = coinsColSize[0];
    const int NEG_INF = -1000000000; // sufficiently small
    
    int totalCells = m * n;
    int *dp = (int *)malloc(totalCells * 3 * sizeof(int));
    if (!dp) return 0;
    
    for (int i = 0; i < totalCells * 3; ++i) dp[i] = NEG_INF;
    
    // initialize start cell
    int v00 = coins[0][0];
    dp[0] = v00;                     // k = 0
    if (v00 < 0) dp[1] = 0;          // use one neutralization
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) continue;
            int curIdx = (i * n + j) * 3;
            int cellVal = coins[i][j];
            
            // from top
            if (i > 0) {
                int prevIdx = ((i - 1) * n + j) * 3;
                for (int k = 0; k <= 2; ++k) {
                    int base = dp[prevIdx + k];
                    if (base == NEG_INF) continue;
                    
                    // not neutralize
                    int val = base + cellVal;
                    if (val > dp[curIdx + k]) dp[curIdx + k] = val;
                    
                    // neutralize if possible
                    if (cellVal < 0 && k < 2) {
                        if (base > dp[curIdx + k + 1]) dp[curIdx + k + 1] = base;
                    }
                }
            }
            
            // from left
            if (j > 0) {
                int prevIdx = (i * n + (j - 1)) * 3;
                for (int k = 0; k <= 2; ++k) {
                    int base = dp[prevIdx + k];
                    if (base == NEG_INF) continue;
                    
                    // not neutralize
                    int val = base + cellVal;
                    if (val > dp[curIdx + k]) dp[curIdx + k] = val;
                    
                    // neutralize if possible
                    if (cellVal < 0 && k < 2) {
                        if (base > dp[curIdx + k + 1]) dp[curIdx + k + 1] = base;
                    }
                }
            }
        }
    }
    
    int lastIdx = ((m - 1) * n + (n - 1)) * 3;
    int ans = NEG_INF;
    for (int k = 0; k <= 2; ++k) {
        if (dp[lastIdx + k] > ans) ans = dp[lastIdx + k];
    }
    
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumAmount(int[][] coins) {
        int m = coins.Length;
        int n = coins[0].Length;
        const int K = 3; // up to 2 neutralizations
        int INF_NEG = int.MinValue / 4;

        int[,,] dp = new int[m, n, K];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < K; k++) dp[i, j, k] = INF_NEG;
            }
        }

        // initialize start cell
        dp[0, 0, 0] = coins[0][0];
        if (coins[0][0] < 0) {
            dp[0, 0, 1] = 0; // neutralize the first cell
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int k = 0; k < K; k++) {
                    int bestPrev = INF_NEG;

                    // from top
                    if (i > 0) bestPrev = Math.Max(bestPrev, dp[i - 1, j, k]);
                    // from left
                    if (j > 0) bestPrev = Math.Max(bestPrev, dp[i, j - 1, k]);

                    if (bestPrev != INF_NEG) {
                        // not neutralizing current cell
                        dp[i, j, k] = Math.Max(dp[i, j, k], bestPrev + coins[i][j]);
                    }

                    // try neutralizing current cell if it's negative and we have spare capacity
                    if (coins[i][j] < 0 && k > 0) {
                        int prevBest = INF_NEG;
                        if (i > 0) prevBest = Math.Max(prevBest, dp[i - 1, j, k - 1]);
                        if (j > 0) prevBest = Math.Max(prevBest, dp[i, j - 1, k - 1]);
                        if (prevBest != INF_NEG) {
                            // neutralize: add 0 instead of coins[i][j]
                            dp[i, j, k] = Math.Max(dp[i, j, k], prevBest);
                        }
                    }
                }
            }
        }

        int result = INF_NEG;
        for (int k = 0; k < K; k++) {
            result = Math.Max(result, dp[m - 1, n - 1, k]);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} coins
 * @return {number}
 */
var maximumAmount = function(coins) {
    const m = coins.length;
    const n = coins[0].length;
    const K = 2; // max neutralizations
    const NEG = -1e18; // sufficiently small
    
    // dp arrays: prev row and current row, each cell holds K+1 states
    let prev = Array.from({ length: n }, () => new Array(K + 1).fill(NEG));
    let curr = Array.from({ length: n }, () => new Array(K + 1).fill(NEG));
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const val = coins[i][j];
            const best = new Array(K + 1).fill(NEG);
            
            if (i === 0 && j === 0) {
                // start cell
                best[0] = val;   // no neutralization
                best[1] = 0;     // neutralize start cell
            } else {
                // transition from top
                if (i > 0) {
                    const up = prev[j];
                    for (let k = 0; k <= K; ++k) {
                        if (up[k] !== NEG) {
                            best[k] = Math.max(best[k], up[k] + val); // keep current value
                        }
                        if (k > 0 && up[k - 1] !== NEG) {
                            best[k] = Math.max(best[k], up[k - 1]);   // neutralize current cell
                        }
                    }
                }
                // transition from left
                if (j > 0) {
                    const left = curr[j - 1];
                    for (let k = 0; k <= K; ++k) {
                        if (left[k] !== NEG) {
                            best[k] = Math.max(best[k], left[k] + val);
                        }
                        if (k > 0 && left[k - 1] !== NEG) {
                            best[k] = Math.max(best[k], left[k - 1]);
                        }
                    }
                }
            }
            curr[j] = best;
        }
        // prepare for next row
        [prev, curr] = [curr, prev];
        for (let j = 0; j < n; ++j) {
            const arr = curr[j];
            for (let k = 0; k <= K; ++k) arr[k] = NEG;
        }
    }
    
    let ans = NEG;
    const lastCell = prev[n - 1];
    for (let k = 0; k <= K; ++k) {
        if (lastCell[k] > ans) ans = lastCell[k];
    }
    return ans;
};
```

## Typescript

```typescript
function maximumAmount(coins: number[][]): number {
    const m = coins.length;
    const n = coins[0].length;
    const NEG_INF = -1e15;

    let prevRow: number[][] = Array.from({ length: n }, () => [NEG_INF, NEG_INF, NEG_INF]);

    for (let i = 0; i < m; i++) {
        const curRow: number[][] = Array.from({ length: n }, () => [NEG_INF, NEG_INF, NEG_INF]);
        for (let j = 0; j < n; j++) {
            const val = coins[i][j];
            if (i === 0 && j === 0) {
                if (val >= 0) {
                    curRow[0][0] = val;
                } else {
                    curRow[0][0] = val;   // take negative as is
                    curRow[0][1] = 0;     // neutralize it
                }
                continue;
            }

            const sources: number[][] = [];
            if (i > 0) sources.push(prevRow[j]);
            if (j > 0) sources.push(curRow[j - 1]);

            for (const src of sources) {
                for (let k = 0; k <= 2; k++) {
                    const prevVal = src[k];
                    if (prevVal === NEG_INF) continue;
                    if (val >= 0) {
                        const cand = prevVal + val;
                        if (cand > curRow[j][k]) curRow[j][k] = cand;
                    } else {
                        // take the negative value
                        const candNeg = prevVal + val;
                        if (candNeg > curRow[j][k]) curRow[j][k] = candNeg;
                        // neutralize if we have remaining capacity
                        if (k < 2 && prevVal > curRow[j][k + 1]) {
                            curRow[j][k + 1] = prevVal;
                        }
                    }
                }
            }
        }
        prevRow = curRow;
    }

    const last = prevRow[n - 1];
    return Math.max(last[0], last[1], last[2]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $coins
     * @return Integer
     */
    function maximumAmount($coins) {
        $m = count($coins);
        $n = count($coins[0]);
        // a very small number as negative infinity
        $negInf = -1000000000000000; // -1e15

        $dpPrev = array_fill(0, $n, [$negInf, $negInf, $negInf]);

        for ($i = 0; $i < $m; $i++) {
            $dpCurr = array_fill(0, $n, [$negInf, $negInf, $negInf]);
            for ($j = 0; $j < $n; $j++) {
                if ($i == 0 && $j == 0) {
                    $val = $coins[0][0];
                    $dpCurr[0][0] = $val;   // no neutralization
                    $dpCurr[0][1] = 0;      // neutralize start cell
                    continue;
                }

                // From top cell (i-1, j)
                if ($i > 0) {
                    $src = $dpPrev[$j];
                    for ($k = 0; $k <= 2; $k++) {
                        $prevVal = $src[$k];
                        if ($prevVal > $negInf) {
                            // Not neutralizing current cell
                            $newVal = $prevVal + $coins[$i][$j];
                            if ($newVal > $dpCurr[$j][$k]) {
                                $dpCurr[$j][$k] = $newVal;
                            }
                            // Neutralize current cell if we still have quota
                            if ($k < 2) {
                                $newNeutral = $prevVal; // add 0 instead of coins[i][j]
                                if ($newNeutral > $dpCurr[$j][$k + 1]) {
                                    $dpCurr[$j][$k + 1] = $newNeutral;
                                }
                            }
                        }
                    }
                }

                // From left cell (i, j-1)
                if ($j > 0) {
                    $src = $dpCurr[$j - 1];
                    for ($k = 0; $k <= 2; $k++) {
                        $prevVal = $src[$k];
                        if ($prevVal > $negInf) {
                            // Not neutralizing current cell
                            $newVal = $prevVal + $coins[$i][$j];
                            if ($newVal > $dpCurr[$j][$k]) {
                                $dpCurr[$j][$k] = $newVal;
                            }
                            // Neutralize current cell if we still have quota
                            if ($k < 2) {
                                $newNeutral = $prevVal; // add 0 instead of coins[i][j]
                                if ($newNeutral > $dpCurr[$j][$k + 1]) {
                                    $dpCurr[$j][$k + 1] = $newNeutral;
                                }
                            }
                        }
                    }
                }
            }
            $dpPrev = $dpCurr;
        }

        $finalStates = $dpPrev[$n - 1];
        return max($finalStates);
    }
}
```

## Swift

```swift
class Solution {
    func maximumAmount(_ coins: [[Int]]) -> Int {
        let m = coins.count
        let n = coins[0].count
        let K = 3 // 0,1,2 neutralizations
        let NEG_INF = Int.min / 4
        
        var dp = Array(repeating: Array(repeating: Array(repeating: NEG_INF, count: K), count: n), count: m)
        
        // Initialize start cell
        dp[0][0][0] = coins[0][0]
        for k in 1..<K {
            if coins[0][0] < 0 {
                dp[0][0][k] = 0   // neutralize the negative value
            } else {
                dp[0][0][k] = coins[0][0]
            }
        }
        
        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 { continue }
                for k in 0..<K {
                    var best = NEG_INF
                    
                    // Move from top or left without neutralizing current cell
                    var prev = NEG_INF
                    if i > 0 {
                        prev = max(prev, dp[i-1][j][k])
                    }
                    if j > 0 {
                        prev = max(prev, dp[i][j-1][k])
                    }
                    if prev != NEG_INF {
                        best = max(best, prev + coins[i][j])
                    }
                    
                    // Neutralize current cell (only useful if value is negative)
                    if k > 0 && coins[i][j] < 0 {
                        var prevNeutral = NEG_INF
                        if i > 0 {
                            prevNeutral = max(prevNeutral, dp[i-1][j][k-1])
                        }
                        if j > 0 {
                            prevNeutral = max(prevNeutral, dp[i][j-1][k-1])
                        }
                        if prevNeutral != NEG_INF {
                            best = max(best, prevNeutral) // add 0 after neutralization
                        }
                    }
                    
                    dp[i][j][k] = best
                }
            }
        }
        
        let lastRow = m - 1
        let lastCol = n - 1
        var answer = NEG_INF
        for k in 0..<K {
            answer = max(answer, dp[lastRow][lastCol][k])
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumAmount(coins: Array<IntArray>): Int {
        val m = coins.size
        val n = coins[0].size
        val INF_NEG = -1_000_000_000
        // dp[i][j][k]: max sum to (i,j) using exactly k neutralizations
        val dp = Array(m) { Array(n) { IntArray(3) { INF_NEG } } }

        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = 0          // neutralize the starting cell
        // using two neutralizations on the first cell is impossible, keep as -inf

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue
                for (k in 0..2) {
                    var best = INF_NEG
                    // from top
                    if (i > 0) {
                        val prevNoNeutral = dp[i - 1][j][k]
                        if (prevNoNeutral != INF_NEG) {
                            best = maxOf(best, prevNoNeutral + coins[i][j])
                        }
                        if (k > 0) {
                            val prevWithNeutral = dp[i - 1][j][k - 1]
                            if (prevWithNeutral != INF_NEG) {
                                // neutralize current cell -> add 0
                                best = maxOf(best, prevWithNeutral)
                            }
                        }
                    }
                    // from left
                    if (j > 0) {
                        val prevNoNeutral = dp[i][j - 1][k]
                        if (prevNoNeutral != INF_NEG) {
                            best = maxOf(best, prevNoNeutral + coins[i][j])
                        }
                        if (k > 0) {
                            val prevWithNeutral = dp[i][j - 1][k - 1]
                            if (prevWithNeutral != INF_NEG) {
                                best = maxOf(best, prevWithNeutral)
                            }
                        }
                    }
                    dp[i][j][k] = best
                }
            }
        }

        var answer = INF_NEG
        for (k in 0..2) {
            answer = maxOf(answer, dp[m - 1][n - 1][k])
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maximumAmount(List<List<int>> coins) {
    int m = coins.length;
    int n = coins[0].length;
    const int NEG_INF = -1 << 60;

    List<List<int>> dp0 =
        List.generate(m, (_) => List.filled(n, NEG_INF));
    List<List<int>> dp1 =
        List.generate(m, (_) => List.filled(n, NEG_INF));
    List<List<int>> dp2 =
        List.generate(m, (_) => List.filled(n, NEG_INF));

    int startVal = coins[0][0];
    if (startVal >= 0) {
      dp0[0][0] = startVal;
    } else {
      dp0[0][0] = startVal; // not neutralized
      dp1[0][0] = 0;        // neutralize start cell
    }

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == 0 && j == 0) continue;

        int prev0 = NEG_INF, prev1 = NEG_INF, prev2 = NEG_INF;
        if (i > 0) {
          prev0 = max(prev0, dp0[i - 1][j]);
          prev1 = max(prev1, dp1[i - 1][j]);
          prev2 = max(prev2, dp2[i - 1][j]);
        }
        if (j > 0) {
          prev0 = max(prev0, dp0[i][j - 1]);
          prev1 = max(prev1, dp1[i][j - 1]);
          prev2 = max(prev2, dp2[i][j - 1]);
        }

        int v = coins[i][j];
        if (v >= 0) {
          if (prev0 != NEG_INF) dp0[i][j] = max(dp0[i][j], prev0 + v);
          if (prev1 != NEG_INF) dp1[i][j] = max(dp1[i][j], prev1 + v);
          if (prev2 != NEG_INF) dp2[i][j] = max(dp2[i][j], prev2 + v);
        } else {
          // take as is
          if (prev0 != NEG_INF) dp0[i][j] = max(dp0[i][j], prev0 + v);
          if (prev1 != NEG_INF) dp1[i][j] = max(dp1[i][j], prev1 + v);
          if (prev2 != NEG_INF) dp2[i][j] = max(dp2[i][j], prev2 + v);
          // neutralize using one more ability
          if (prev0 != NEG_INF) dp1[i][j] = max(dp1[i][j], prev0); // add 0
          if (prev1 != NEG_INF) dp2[i][j] = max(dp2[i][j], prev1);
        }
      }
    }

    int end0 = dp0[m - 1][n - 1];
    int end1 = dp1[m - 1][n - 1];
    int end2 = dp2[m - 1][n - 1];
    return max(end0, max(end1, end2));
  }
}
```

## Golang

```go
func maximumAmount(coins [][]int) int {
    m := len(coins)
    n := len(coins[0])
    const K = 3
    negInf := -1 << 60

    dp := make([][][]int, m)
    for i := 0; i < m; i++ {
        dp[i] = make([][]int, n)
        for j := 0; j < n; j++ {
            dp[i][j] = make([]int, K)
            for k := 0; k < K; k++ {
                dp[i][j][k] = negInf
            }
        }
    }

    if coins[0][0] >= 0 {
        dp[0][0][0] = coins[0][0]
    } else {
        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = 0
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i == 0 && j == 0 {
                continue
            }
            for k := 0; k < K; k++ {
                best := negInf

                if i > 0 {
                    if dp[i-1][j][k] != negInf {
                        val := dp[i-1][j][k] + coins[i][j]
                        if val > best {
                            best = val
                        }
                    }
                    if k > 0 && coins[i][j] < 0 && dp[i-1][j][k-1] != negInf {
                        val := dp[i-1][j][k-1]
                        if val > best {
                            best = val
                        }
                    }
                }

                if j > 0 {
                    if dp[i][j-1][k] != negInf {
                        val := dp[i][j-1][k] + coins[i][j]
                        if val > best {
                            best = val
                        }
                    }
                    if k > 0 && coins[i][j] < 0 && dp[i][j-1][k-1] != negInf {
                        val := dp[i][j-1][k-1]
                        if val > best {
                            best = val
                        }
                    }
                }

                dp[i][j][k] = best
            }
        }
    }

    ans := negInf
    for k := 0; k < K; k++ {
        if dp[m-1][n-1][k] > ans {
            ans = dp[m-1][n-1][k]
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_amount(coins)
  m = coins.size
  n = coins[0].size
  neg_inf = -10**15

  prev = Array.new(n) { [neg_inf, neg_inf, neg_inf] }
  cur = Array.new(n) { [neg_inf, neg_inf, neg_inf] }

  (0...m).each do |i|
    (0...n).each do |j|
      cell_dp = [neg_inf, neg_inf, neg_inf]

      if i == 0 && j == 0
        cell_dp[0] = coins[0][0]
        cell_dp[1] = 0
      else
        sources = []
        sources << prev[j] if i > 0
        sources << cur[j - 1] if j > 0

        sources.each do |src|
          (0..2).each do |k|
            val = src[k]
            next if val == neg_inf

            # take the coin value
            new_val = val + coins[i][j]
            cell_dp[k] = new_val if new_val > cell_dp[k]

            # neutralize this cell if we still have capacity
            if k < 2
              cell_dp[k + 1] = val if val > cell_dp[k + 1]
            end
          end
        end
      end

      cur[j] = cell_dp
    end
    prev, cur = cur, Array.new(n) { [neg_inf, neg_inf, neg_inf] }
  end

  prev[n - 1].max
end
```

## Scala

```scala
object Solution {
  def maximumAmount(coins: Array[Array[Int]]): Int = {
    val m = coins.length
    val n = coins(0).length
    val K = 3 // allow 0,1,2 neutralizations
    val INF = Int.MinValue / 4

    val dp = Array.ofDim[Int](m, n, K)
    for (i <- 0 until m; j <- 0 until n; k <- 0 until K) {
      dp(i)(j)(k) = INF
    }

    // base cell
    dp(0)(0)(0) = coins(0)(0)
    if (coins(0)(0) < 0) {
      dp(0)(0)(1) = 0
    }

    for (i <- 0 until m) {
      for (j <- 0 until n) {
        if (i == 0 && j == 0) {
          // already initialized
        } else {
          val v = coins(i)(j)

          // without using a new neutralization at this cell
          for (k <- 0 until K) {
            var best = INF
            if (i > 0 && dp(i - 1)(j)(k) != INF) {
              best = math.max(best, dp(i - 1)(j)(k) + v)
            }
            if (j > 0 && dp(i)(j - 1)(k) != INF) {
              best = math.max(best, dp(i)(j - 1)(k) + v)
            }
            dp(i)(j)(k) = best
          }

          // using a neutralization on this cell (skip its value)
          for (k <- 1 until K) {
            var bestNeutral = INF
            if (i > 0 && dp(i - 1)(j)(k - 1) != INF) {
              bestNeutral = math.max(bestNeutral, dp(i - 1)(j)(k - 1))
            }
            if (j > 0 && dp(i)(j - 1)(k - 1) != INF) {
              bestNeutral = math.max(bestNeutral, dp(i)(j - 1)(k - 1))
            }
            dp(i)(j)(k) = math.max(dp(i)(j)(k), bestNeutral)
          }
        }
      }
    }

    var answer = INF
    for (k <- 0 until K) {
      answer = math.max(answer, dp(m - 1)(n - 1)(k))
    }
    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_amount(coins: Vec<Vec<i32>>) -> i32 {
        let m = coins.len();
        let n = coins[0].len();
        const INF_NEG: i32 = -1_000_000_000;
        // dp[j][k]: best profit up to current row at column j using up to k neutralizations
        let mut dp = vec![vec![INF_NEG; 3]; n];
        for i in 0..m {
            let mut cur = vec![vec![INF_NEG; 3]; n];
            for j in 0..n {
                if i == 0 && j == 0 {
                    // start cell initialization
                    let val = coins[0][0];
                    cur[0][0] = val;
                    for k in 1..=2 {
                        cur[0][k] = std::cmp::max(val, 0);
                    }
                    continue;
                }
                for k in 0..=2 {
                    // best from top or left without neutralizing current cell
                    let mut best = INF_NEG;
                    if i > 0 {
                        best = best.max(dp[j][k]);
                    }
                    if j > 0 {
                        best = best.max(cur[j - 1][k]);
                    }
                    if best != INF_NEG {
                        cur[j][k] = cur[j][k].max(best + coins[i][j]);
                    }
                    // consider neutralizing current cell (use one allowance)
                    if k > 0 {
                        let mut best2 = INF_NEG;
                        if i > 0 {
                            best2 = best2.max(dp[j][k - 1]);
                        }
                        if j > 0 {
                            best2 = best2.max(cur[j - 1][k - 1]);
                        }
                        // also possible that we neutralize the start cell, but that's already handled
                        if best2 != INF_NEG {
                            cur[j][k] = cur[j][k].max(best2); // add 0 for neutralized cell
                        }
                    }
                }
            }
            dp = cur;
        }
        dp[n - 1][2]
    }
}
```

## Racket

```racket
(define/contract (maximum-amount coins)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length coins))
         (n (if (= m 0) 0 (length (first coins))))
         (UNREACHABLE -1000000000000)
         (grid (list->vector (map list->vector coins)))
         (dpPrev (make-vector n #f))
         (dpCurr (make-vector n #f)))
    (for ([i (in-range m)])
      (set! dpCurr (make-vector n #f))
      (for ([j (in-range n)])
        (define cell-val (vector-ref (vector-ref grid i) j))
        (define cur (make-vector 3 UNREACHABLE))
        (for ([k (in-range 3)])
          (define best UNREACHABLE)
          (if (and (= i 0) (= j 0))
              (begin
                ;; not neutralize
                (when (= k 0)
                  (set! best (max best (+ cell-val))))
                ;; neutralize current cell
                (when (> k 0)
                  (set! best (max best 0))))
              (begin
                ;; from top
                (when (> i 0)
                  (define prev-vec (vector-ref dpPrev j))
                  (define same (vector-ref prev-vec k))
                  (unless (= same UNREACHABLE)
                    (set! best (max best (+ same cell-val))))
                  (when (> k 0)
                    (define less (vector-ref prev-vec (- k 1)))
                    (unless (= less UNREACHABLE)
                      (set! best (max best less))))) ; neutralize current adds 0
                ;; from left
                (when (> j 0)
                  (define left-vec (vector-ref dpCurr (- j 1)))
                  (define same (vector-ref left-vec k))
                  (unless (= same UNREACHABLE)
                    (set! best (max best (+ same cell-val))))
                  (when (> k 0)
                    (define less (vector-ref left-vec (- k 1)))
                    (unless (= less UNREACHABLE)
                      (set! best (max best less)))))))
          (vector-set! cur k best))
        (vector-set! dpCurr j cur))
      (set! dpPrev dpCurr))
    (let ((final-vec (vector-ref dpPrev (- n 1))))
      (apply max (vector->list final-vec)))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_amount/1]).

-define(NEG_INF, -(1 bsl 60)).

-spec maximum_amount(Coins :: [[integer()]]) -> integer().
maximum_amount(Coins) ->
    case Coins of
        [] -> 0;
        _ ->
            N = length(hd(Coins)),
            {FinalRowTuple,_} = lists:foldl(
                fun(RowVals, {PrevRowTuple, RowIdx}) ->
                    CurrRowList = process_row(RowVals, PrevRowTuple, RowIdx),
                    CurrRowTuple = list_to_tuple(CurrRowList),
                    {CurrRowTuple, RowIdx + 1}
                end,
                {undefined, 0},
                Coins
            ),
            LastTuple = element(N, FinalRowTuple),
            lists:max(tuple_to_list(LastTuple))
    end.

process_row(RowVals, PrevRowTuple, I) ->
    {RevList,_} = lists:foldl(
        fun(V, {Acc, J}) ->
            Tuple = compute_cell(I, J, V, PrevRowTuple, Acc),
            {[Tuple | Acc], J + 1}
        end,
        {[], 0},
        RowVals
    ),
    lists:reverse(RevList).

compute_cell(I, J, V, PrevRowTuple, LeftAcc) ->
    case {I, J} of
        {0, 0} ->
            {V, 0, 0};
        _ ->
            Top = if I == 0 -> undefined; true -> element(J + 1, PrevRowTuple) end,
            Left = if J == 0 -> undefined; true -> hd(LeftAcc) end,
            KVals = [best_for_k(K, V, Top, Left) || K <- [0,1,2]],
            list_to_tuple(KVals)
    end.

best_for_k(K, V, Top, Left) ->
    CandFrom = fun(Tuple) ->
        NotNeutral = element(K + 1, Tuple) + V,
        Neutral = if K > 0 -> [element(K, Tuple)]; true -> [] end,
        [NotNeutral] ++ Neutral
    end,
    Candidates = case Top of
        undefined -> [];
        _ -> CandFrom(Top)
    end ++ case Left of
        undefined -> [];
        _ -> CandFrom(Left)
    end,
    case Candidates of
        [] -> ?NEG_INF;
        _  -> lists:max(Candidates)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_amount(coins :: [[integer]]) :: integer
  def maximum_amount(coins) do
    m = length(coins)
    n = length(List.first(coins))
    neg_inf = -1_000_000_000

    size = m * n
    dp = :array.new(size, default: {neg_inf, neg_inf, neg_inf})

    dp =
      Enum.reduce(0..(m - 1), dp, fn i, dp_acc ->
        Enum.reduce(0..(n - 1), dp_acc, fn j, dp_inner ->
          v = coins |> Enum.at(i) |> Enum.at(j)
          idx = i * n + j

          cell_tuple =
            if i == 0 and j == 0 do
              k0 = v
              k1 = if v < 0, do: 0, else: neg_inf
              {k0, k1, neg_inf}
            else
              top = if i > 0, do: :array.get((i - 1) * n + j, dp_inner), else: nil
              left = if j > 0, do: :array.get(i * n + (j - 1), dp_inner), else: nil

              vals =
                Enum.map(0..2, fn k ->
                  candidates =
                    Enum.reduce([top, left], [], fn
                      nil, acc -> acc
                      prev, acc ->
                        pk = elem(prev, k)
                        acc = [pk + v | acc]

                        if v < 0 and k > 0 do
                          pk_prev = elem(prev, k - 1)
                          [pk_prev | acc]
                        else
                          acc
                        end
                    end)

                  Enum.max([neg_inf | candidates])
                end)

              List.to_tuple(vals)
            end

          :array.set(idx, cell_tuple, dp_inner)
        end)
      end)

    final_idx = (m - 1) * n + (n - 1)
    {a, b, c} = :array.get(final_idx, dp)
    Enum.max([a, b, c])
  end
end
```

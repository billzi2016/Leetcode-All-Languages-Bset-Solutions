# 1473. Paint House III

## Cpp

```cpp
class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        const int INF = 1e9;
        // dp[t][c] = min cost for processed houses with t neighborhoods ending with color c
        vector<vector<int>> dpPrev(target + 1, vector<int>(n + 1, INF));
        
        // Initialize for the first house
        if (houses[0] == 0) {
            for (int c = 1; c <= n; ++c) {
                dpPrev[1][c] = cost[0][c - 1];
            }
        } else {
            int c = houses[0];
            dpPrev[1][c] = 0;
        }
        
        // Process remaining houses
        for (int i = 1; i < m; ++i) {
            vector<vector<int>> dpCurr(target + 1, vector<int>(n + 1, INF));
            for (int t = 1; t <= target; ++t) {
                for (int c = 1; c <= n; ++c) {
                    if (houses[i] != 0 && houses[i] != c) continue; // color not allowed
                    int paintCost = (houses[i] == 0) ? cost[i][c - 1] : 0;
                    
                    int bestPrev = INF;
                    // Same color as previous house, neighborhoods unchanged
                    bestPrev = min(bestPrev, dpPrev[t][c]);
                    
                    // Different color from previous house, neighborhoods increase by 1
                    if (t > 1) {
                        for (int pc = 1; pc <= n; ++pc) {
                            if (pc == c) continue;
                            bestPrev = min(bestPrev, dpPrev[t - 1][pc]);
                        }
                    }
                    
                    if (bestPrev >= INF) continue;
                    dpCurr[t][c] = bestPrev + paintCost;
                }
            }
            dpPrev.swap(dpCurr);
        }
        
        int ans = INF;
        for (int c = 1; c <= n; ++c) {
            ans = min(ans, dpPrev[target][c]);
        }
        return ans == INF ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
        final int INF = 1_000_000_007;
        int[][][] dp = new int[m][target + 1][n];
        for (int i = 0; i < m; i++) {
            for (int t = 0; t <= target; t++) {
                java.util.Arrays.fill(dp[i][t], INF);
            }
        }

        // initialize first house
        if (houses[0] != 0) {
            int col = houses[0] - 1;
            dp[0][1][col] = 0;
        } else {
            for (int c = 0; c < n; c++) {
                dp[0][1][c] = cost[0][c];
            }
        }

        // DP transition
        for (int i = 1; i < m; i++) {
            for (int t = 1; t <= target; t++) {
                for (int cur = 0; cur < n; cur++) {
                    if (houses[i] != 0 && cur != houses[i] - 1) continue;
                    int paintCost = (houses[i] == 0) ? cost[i][cur] : 0;

                    // same color as previous house, neighborhoods unchanged
                    if (dp[i - 1][t][cur] != INF) {
                        dp[i][t][cur] = Math.min(dp[i][t][cur], dp[i - 1][t][cur] + paintCost);
                    }

                    // different color from previous house, neighborhoods increase by 1
                    if (t > 1) {
                        for (int prev = 0; prev < n; prev++) {
                            if (prev == cur) continue;
                            if (dp[i - 1][t - 1][prev] != INF) {
                                dp[i][t][cur] = Math.min(dp[i][t][cur],
                                        dp[i - 1][t - 1][prev] + paintCost);
                            }
                        }
                    }
                }
            }
        }

        int ans = INF;
        for (int c = 0; c < n; c++) {
            ans = Math.min(ans, dp[m - 1][target][c]);
        }
        return ans == INF ? -1 : ans;
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        INF = 10**15
        # dp[t][c] = min cost for processed houses with t neighborhoods, last color c (1-indexed)
        dp_prev = [[INF] * (n + 1) for _ in range(target + 1)]
        
        # initialize first house
        if houses[0] == 0:
            for c in range(1, n + 1):
                dp_prev[1][c] = cost[0][c - 1]
        else:
            c = houses[0]
            dp_prev[1][c] = 0
        
        # process remaining houses
        for i in range(1, m):
            dp_cur = [[INF] * (n + 1) for _ in range(target + 1)]
            for t in range(1, target + 1):
                for c in range(1, n + 1):
                    # skip colors not allowed by pre-painted house
                    if houses[i] != 0 and c != houses[i]:
                        continue
                    cur_cost = 0 if houses[i] != 0 else cost[i][c - 1]
                    
                    # same color as previous house -> neighborhoods unchanged
                    if dp_prev[t][c] < INF:
                        val = dp_prev[t][c] + cur_cost
                        if val < dp_cur[t][c]:
                            dp_cur[t][c] = val
                    
                    # different color -> neighborhoods increase by 1
                    if t > 1:
                        min_prev = INF
                        for pc in range(1, n + 1):
                            if pc == c:
                                continue
                            prev_val = dp_prev[t - 1][pc]
                            if prev_val < min_prev:
                                min_prev = prev_val
                        if min_prev < INF:
                            val = min_prev + cur_cost
                            if val < dp_cur[t][c]:
                                dp_cur[t][c] = val
            dp_prev = dp_cur
        
        ans = min(dp_prev[target][1:])  # ignore index 0
        return -1 if ans >= INF else ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = 10**15
        # dp[k][c] for previous house
        prev = [[INF] * n for _ in range(target + 1)]
        # initialize first house
        if houses[0] == 0:
            for c in range(n):
                prev[1][c] = cost[0][c]
        else:
            c = houses[0] - 1
            prev[1][c] = 0

        for i in range(1, m):
            cur = [[INF] * n for _ in range(target + 1)]
            allowed_colors = [houses[i] - 1] if houses[i] != 0 else list(range(n))
            paint_costs = [0] * n
            if houses[i] == 0:
                for c in range(n):
                    paint_costs[c] = cost[i][c]

            for k in range(1, target + 1):
                for c in allowed_colors:
                    # same color as previous house -> neighborhoods unchanged
                    same = prev[k][c]
                    best = same
                    if k > 1:
                        diff_min = INF
                        for pc in range(n):
                            if pc == c:
                                continue
                            val = prev[k - 1][pc]
                            if val < diff_min:
                                diff_min = val
                        if diff_min < best:
                            best = diff_min
                    if best != INF:
                        cur_cost = best + paint_costs[c]
                        if cur_cost < cur[k][c]:
                            cur[k][c] = cur_cost
            prev = cur

        ans = min(prev[target])
        return -1 if ans >= INF else ans
```

## C

```c
int minCost(int* houses, int housesSize, int** cost, int costSize, int* costColSize, int m, int n, int target) {
    const int INF = 1000000000;
    static int dp[101][101][21];
    for (int i = 0; i < m; ++i)
        for (int k = 0; k <= target; ++k)
            for (int c = 0; c < n; ++c)
                dp[i][k][c] = INF;

    if (houses[0] != 0) {
        int col = houses[0] - 1;
        dp[0][1][col] = 0;
    } else {
        for (int c = 0; c < n; ++c)
            dp[0][1][c] = cost[0][c];
    }

    for (int i = 1; i < m; ++i) {
        for (int k = 1; k <= target; ++k) {
            for (int cur = 0; cur < n; ++cur) {
                if (houses[i] != 0 && houses[i] - 1 != cur)
                    continue;
                int add = (houses[i] == 0) ? cost[i][cur] : 0;
                int best = INF;

                if (dp[i - 1][k][cur] < INF) {
                    int val = dp[i - 1][k][cur] + add;
                    if (val < best) best = val;
                }

                if (k > 1) {
                    for (int pc = 0; pc < n; ++pc) {
                        if (pc == cur) continue;
                        if (dp[i - 1][k - 1][pc] < INF) {
                            int val = dp[i - 1][k - 1][pc] + add;
                            if (val < best) best = val;
                        }
                    }
                }

                dp[i][k][cur] = best;
            }
        }
    }

    int ans = INF;
    for (int c = 0; c < n; ++c)
        if (dp[m - 1][target][c] < ans) ans = dp[m - 1][target][c];

    return ans == INF ? -1 : ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinCost(int[] houses, int[][] cost, int m, int n, int target) {
        const int INF = 1000000007;
        int[,,] dp = new int[m, target + 1, n];
        for (int i = 0; i < m; i++) {
            for (int t = 0; t <= target; t++) {
                for (int c = 0; c < n; c++) {
                    dp[i, t, c] = INF;
                }
            }
        }

        // Initialize first house
        if (houses[0] == 0) {
            for (int c = 0; c < n; c++) {
                dp[0, 1, c] = cost[0][c];
            }
        } else {
            int painted = houses[0] - 1;
            dp[0, 1, painted] = 0;
        }

        for (int i = 1; i < m; i++) {
            if (houses[i] == 0) {
                // house can be painted any color
                for (int pc = 0; pc < n; pc++) {
                    for (int tPrev = 1; tPrev <= target; tPrev++) {
                        int prevCost = dp[i - 1, tPrev, pc];
                        if (prevCost == INF) continue;
                        for (int cur = 0; cur < n; cur++) {
                            int newT = (cur == pc) ? tPrev : tPrev + 1;
                            if (newT > target) continue;
                            int curCost = prevCost + cost[i][cur];
                            if (curCost < dp[i, newT, cur]) {
                                dp[i, newT, cur] = curCost;
                            }
                        }
                    }
                }
            } else {
                // house already painted
                int cur = houses[i] - 1;
                for (int pc = 0; pc < n; pc++) {
                    for (int tPrev = 1; tPrev <= target; tPrev++) {
                        int prevCost = dp[i - 1, tPrev, pc];
                        if (prevCost == INF) continue;
                        int newT = (cur == pc) ? tPrev : tPrev + 1;
                        if (newT > target) continue;
                        if (prevCost < dp[i, newT, cur]) {
                            dp[i, newT, cur] = prevCost;
                        }
                    }
                }
            }
        }

        int answer = INF;
        for (int c = 0; c < n; c++) {
            if (dp[m - 1, target, c] < answer) {
                answer = dp[m - 1, target, c];
            }
        }
        return answer == INF ? -1 : answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} houses
 * @param {number[][]} cost
 * @param {number} m
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var minCost = function(houses, cost, m, n, target) {
    const INF = 1e15;
    // dp[i][t][c] = min cost for first i+1 houses, t neighborhoods, house i painted color c (1-indexed)
    const dp = Array.from({ length: m }, () =>
        Array.from({ length: target + 1 }, () => Array(n + 1).fill(INF))
    );

    // base case for first house
    if (houses[0] !== 0) {
        const c = houses[0];
        dp[0][1][c] = 0;
    } else {
        for (let c = 1; c <= n; ++c) {
            dp[0][1][c] = cost[0][c - 1];
        }
    }

    for (let i = 1; i < m; ++i) {
        for (let t = 1; t <= target; ++t) {
            // iterate possible current colors
            const allowedColors = houses[i] === 0 ? null : [houses[i]];
            if (allowedColors) {
                for (const cur of allowedColors) {
                    const paintCost = 0;
                    // same color as previous
                    if (dp[i - 1][t][cur] < INF) {
                        dp[i][t][cur] = Math.min(dp[i][t][cur], dp[i - 1][t][cur] + paintCost);
                    }
                    // different color -> neighborhoods increase by 1
                    if (t > 1) {
                        for (let pc = 1; pc <= n; ++pc) {
                            if (pc === cur) continue;
                            const prevVal = dp[i - 1][t - 1][pc];
                            if (prevVal < INF) {
                                dp[i][t][cur] = Math.min(dp[i][t][cur], prevVal + paintCost);
                            }
                        }
                    }
                }
            } else {
                for (let cur = 1; cur <= n; ++cur) {
                    const paintCost = cost[i][cur - 1];
                    // same color as previous
                    if (dp[i - 1][t][cur] < INF) {
                        dp[i][t][cur] = Math.min(dp[i][t][cur], dp[i - 1][t][cur] + paintCost);
                    }
                    // different color -> neighborhoods increase by 1
                    if (t > 1) {
                        for (let pc = 1; pc <= n; ++pc) {
                            if (pc === cur) continue;
                            const prevVal = dp[i - 1][t - 1][pc];
                            if (prevVal < INF) {
                                dp[i][t][cur] = Math.min(dp[i][t][cur], prevVal + paintCost);
                            }
                        }
                    }
                }
            }
        }
    }

    let ans = INF;
    for (let c = 1; c <= n; ++c) {
        ans = Math.min(ans, dp[m - 1][target][c]);
    }
    return ans >= INF ? -1 : ans;
};
```

## Typescript

```typescript
function minCost(houses: number[], cost: number[][], m: number, n: number, target: number): number {
    const INF = Number.MAX_SAFE_INTEGER;
    let dpPrev: number[][] = Array.from({ length: target + 1 }, () => new Array(n + 1).fill(INF));

    // initialize for the first house
    if (houses[0] !== 0) {
        const c = houses[0];
        dpPrev[1][c] = 0;
    } else {
        for (let color = 1; color <= n; ++color) {
            dpPrev[1][color] = cost[0][color - 1];
        }
    }

    for (let i = 1; i < m; ++i) {
        const dpCur: number[][] = Array.from({ length: target + 1 }, () => new Array(n + 1).fill(INF));

        if (houses[i] !== 0) {
            const curColor = houses[i];
            for (let neighPrev = 1; neighPrev <= target; ++neighPrev) {
                for (let prevColor = 1; prevColor <= n; ++prevColor) {
                    const prevVal = dpPrev[neighPrev][prevColor];
                    if (prevVal === INF) continue;
                    const newNeigh = neighPrev + (curColor !== prevColor ? 1 : 0);
                    if (newNeigh > target) continue;
                    if (prevVal < dpCur[newNeigh][curColor]) {
                        dpCur[newNeigh][curColor] = prevVal;
                    }
                }
            }
        } else {
            for (let curColor = 1; curColor <= n; ++curColor) {
                const paintCost = cost[i][curColor - 1];
                for (let neighPrev = 1; neighPrev <= target; ++neighPrev) {
                    for (let prevColor = 1; prevColor <= n; ++prevColor) {
                        const prevVal = dpPrev[neighPrev][prevColor];
                        if (prevVal === INF) continue;
                        const newNeigh = neighPrev + (curColor !== prevColor ? 1 : 0);
                        if (newNeigh > target) continue;
                        const total = prevVal + paintCost;
                        if (total < dpCur[newNeigh][curColor]) {
                            dpCur[newNeigh][curColor] = total;
                        }
                    }
                }
            }
        }

        dpPrev = dpCur;
    }

    let answer = INF;
    for (let color = 1; color <= n; ++color) {
        if (dpPrev[target][color] < answer) answer = dpPrev[target][color];
    }
    return answer === INF ? -1 : answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $houses
     * @param Integer[][] $cost
     * @param Integer $m
     * @param Integer $n
     * @param Integer $target
     * @return Integer
     */
    function minCost($houses, $cost, $m, $n, $target) {
        $INF = 1 << 60; // sufficiently large
        
        // dp[color][neighborhoods] = min cost up to current house
        $dp = [];
        for ($c = 1; $c <= $n; $c++) {
            $dp[$c] = array_fill(0, $target + 1, $INF);
        }
        
        // Initialize for the first house
        if ($houses[0] != 0) {
            $color = $houses[0];
            $dp[$color][1] = 0;
        } else {
            for ($c = 1; $c <= $n; $c++) {
                $dp[$c][1] = $cost[0][$c - 1];
            }
        }
        
        // Process remaining houses
        for ($i = 1; $i < $m; $i++) {
            $next = [];
            for ($c = 1; $c <= $n; $c++) {
                $next[$c] = array_fill(0, $target + 1, $INF);
            }
            
            if ($houses[$i] != 0) { // already painted
                $curColor = $houses[$i];
                for ($prevColor = 1; $prevColor <= $n; $prevColor++) {
                    for ($k = 1; $k <= $target; $k++) {
                        if ($dp[$prevColor][$k] >= $INF) continue;
                        $newK = $k + ($curColor != $prevColor ? 1 : 0);
                        if ($newK > $target) continue;
                        $next[$curColor][$newK] = min($next[$curColor][$newK], $dp[$prevColor][$k]);
                    }
                }
            } else { // need to paint
                for ($curColor = 1; $curColor <= $n; $curColor++) {
                    $paintCost = $cost[$i][$curColor - 1];
                    for ($prevColor = 1; $prevColor <= $n; $prevColor++) {
                        for ($k = 1; $k <= $target; $k++) {
                            if ($dp[$prevColor][$k] >= $INF) continue;
                            $newK = $k + ($curColor != $prevColor ? 1 : 0);
                            if ($newK > $target) continue;
                            $totalCost = $dp[$prevColor][$k] + $paintCost;
                            $next[$curColor][$newK] = min($next[$curColor][$newK], $totalCost);
                        }
                    }
                }
            }
            
            $dp = $next;
        }
        
        // Find answer
        $ans = $INF;
        for ($c = 1; $c <= $n; $c++) {
            $ans = min($ans, $dp[$c][$target]);
        }
        return $ans >= $INF ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ houses: [Int], _ cost: [[Int]], _ m: Int, _ n: Int, _ target: Int) -> Int {
        let INF = Int.max / 2
        var dpPrev = Array(repeating: Array(repeating: INF, count: n), count: target + 1)
        
        // Initialize for the first house
        if houses[0] != 0 {
            let c = houses[0] - 1
            if target >= 1 {
                dpPrev[1][c] = 0
            }
        } else {
            for c in 0..<n {
                dpPrev[1][c] = cost[0][c]
            }
        }
        
        // Process remaining houses
        if m > 1 {
            for i in 1..<m {
                var dpCurr = Array(repeating: Array(repeating: INF, count: n), count: target + 1)
                for prevK in 1...target {
                    for pc in 0..<n {
                        let prevVal = dpPrev[prevK][pc]
                        if prevVal >= INF { continue }
                        for c in 0..<n {
                            if houses[i] != 0 && c != houses[i] - 1 { continue }
                            let newK = prevK + (c == pc ? 0 : 1)
                            if newK > target { continue }
                            let addCost = (houses[i] == 0) ? cost[i][c] : 0
                            let curCost = prevVal + addCost
                            if curCost < dpCurr[newK][c] {
                                dpCurr[newK][c] = curCost
                            }
                        }
                    }
                }
                dpPrev = dpCurr
            }
        }
        
        var ans = INF
        for c in 0..<n {
            ans = min(ans, dpPrev[target][c])
        }
        return ans == INF ? -1 : ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(houses: IntArray, cost: Array<IntArray>, m: Int, n: Int, target: Int): Int {
        if (target > m) return -1
        val INF = Long.MAX_VALUE / 4
        var dpPrev = Array(target + 1) { LongArray(n + 1) { INF } }

        // initialize for first house
        if (houses[0] != 0) {
            val c = houses[0]
            dpPrev[1][c] = 0L
        } else {
            for (color in 1..n) {
                dpPrev[1][color] = cost[0][color - 1].toLong()
            }
        }

        // process remaining houses
        for (i in 1 until m) {
            val dpCurr = Array(target + 1) { LongArray(n + 1) { INF } }
            for (t in 1..target) {
                for (curColor in 1..n) {
                    if (houses[i] != 0 && houses[i] != curColor) continue
                    val paintCost = if (houses[i] == 0) cost[i][curColor - 1].toLong() else 0L

                    // same color as previous house, neighborhoods unchanged
                    if (dpPrev[t][curColor] < INF) {
                        dpCurr[t][curColor] = minOf(dpCurr[t][curColor], dpPrev[t][curColor] + paintCost)
                    }

                    // different color -> new neighborhood
                    if (t > 1) {
                        var best = INF
                        for (prevColor in 1..n) {
                            if (prevColor == curColor) continue
                            val prevVal = dpPrev[t - 1][prevColor]
                            if (prevVal < best) best = prevVal
                        }
                        if (best < INF) {
                            dpCurr[t][curColor] = minOf(dpCurr[t][curColor], best + paintCost)
                        }
                    }
                }
            }
            dpPrev = dpCurr
        }

        var answer = INF
        for (color in 1..n) {
            if (dpPrev[target][color] < answer) answer = dpPrev[target][color]
        }
        return if (answer >= INF / 2) -1 else answer.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minCost(List<int> houses, List<List<int>> cost, int m, int n, int target) {
    const int INF = 1 << 60;
    // dp[i][t][c] = min cost for first i+1 houses, t neighborhoods, house i painted color c
    var dp = List.generate(
        m, (_) => List.generate(target + 1, (_) => List.filled(n + 1, INF)));

    for (int i = 0; i < m; ++i) {
      List<int> possibleColors;
      if (houses[i] != 0) {
        possibleColors = [houses[i]];
      } else {
        possibleColors = List.generate(n, (idx) => idx + 1);
      }

      for (int curColor in possibleColors) {
        int paintCost = houses[i] == 0 ? cost[i][curColor - 1] : 0;

        for (int t = 1; t <= target; ++t) {
          if (i == 0) {
            // First house can only form one neighborhood
            if (t == 1) {
              dp[0][1][curColor] =
                  paintCost < dp[0][1][curColor] ? paintCost : dp[0][1][curColor];
            }
            continue;
          }

          for (int prevColor = 1; prevColor <= n; ++prevColor) {
            int delta = (prevColor == curColor) ? 0 : 1;
            if (t - delta < 1) continue;
            int prevVal = dp[i - 1][t - delta][prevColor];
            if (prevVal >= INF) continue;
            int newCost = prevVal + paintCost;
            if (newCost < dp[i][t][curColor]) {
              dp[i][t][curColor] = newCost;
            }
          }
        }
      }
    }

    int ans = INF;
    for (int c = 1; c <= n; ++c) {
      if (dp[m - 1][target][c] < ans) ans = dp[m - 1][target][c];
    }
    return ans >= INF ? -1 : ans;
  }
}
```

## Golang

```go
func minCost(houses []int, cost [][]int, m int, n int, target int) int {
	const INF = int(1 << 60)

	// dp[t][c] = min cost for first i houses with t neighborhoods and i-th house color c
	dp := make([][]int, target+1)
	for i := 0; i <= target; i++ {
		dp[i] = make([]int, n+1)
		for j := 1; j <= n; j++ {
			dp[i][j] = INF
		}
	}

	if houses[0] != 0 {
		c := houses[0]
		dp[1][c] = 0
	} else {
		for c := 1; c <= n; c++ {
			dp[1][c] = cost[0][c-1]
		}
	}

	for i := 1; i < m; i++ {
		newDP := make([][]int, target+1)
		for t := 0; t <= target; t++ {
			newDP[t] = make([]int, n+1)
			for c := 1; c <= n; c++ {
				newDP[t][c] = INF
			}
		}

		var colors []int
		if houses[i] != 0 {
			colors = []int{houses[i]}
		} else {
			colors = make([]int, n)
			for c := 1; c <= n; c++ {
				colors[c-1] = c
			}
		}

		for tPrev := 1; tPrev <= target; tPrev++ {
			for pc := 1; pc <= n; pc++ {
				prevCost := dp[tPrev][pc]
				if prevCost == INF {
					continue
				}
				for _, cc := range colors {
					add := 0
					if houses[i] == 0 {
						add = cost[i][cc-1]
					}
					tNew := tPrev
					if cc != pc {
						tNew++
					}
					if tNew > target {
						continue
					}
					curCost := prevCost + add
					if curCost < newDP[tNew][cc] {
						newDP[tNew][cc] = curCost
					}
				}
			}
		}
		dp = newDP
	}

	ans := INF
	for c := 1; c <= n; c++ {
		if dp[target][c] < ans {
			ans = dp[target][c]
		}
	}
	if ans == INF {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def min_cost(houses, cost, m, n, target)
  INF = 10**15
  # dp[t][c] = min cost for processed houses with t neighborhoods ending with color c (0-indexed)
  dp_prev = Array.new(target + 1) { Array.new(n, INF) }

  if houses[0] == 0
    n.times do |c|
      dp_prev[1][c] = cost[0][c]
    end
  else
    c = houses[0] - 1
    dp_prev[1][c] = 0
  end

  (1...m).each do |i|
    dp_cur = Array.new(target + 1) { Array.new(n, INF) }
    (1..target).each do |t|
      n.times do |prev_c|
        prev_cost = dp_prev[t][prev_c]
        next if prev_cost == INF
        if houses[i] == 0
          n.times do |cur_c|
            new_t = t + (cur_c == prev_c ? 0 : 1)
            next if new_t > target
            cur_cost = prev_cost + cost[i][cur_c]
            dp_cur[new_t][cur_c] = cur_cost if cur_cost < dp_cur[new_t][cur_c]
          end
        else
          cur_c = houses[i] - 1
          new_t = t + (cur_c == prev_c ? 0 : 1)
          next if new_t > target
          cur_cost = prev_cost
          dp_cur[new_t][cur_c] = cur_cost if cur_cost < dp_cur[new_t][cur_c]
        end
      end
    end
    dp_prev = dp_cur
  end

  ans = INF
  n.times do |c|
    ans = dp_prev[target][c] if dp_prev[target][c] < ans
  end
  ans == INF ? -1 : ans
end
```

## Scala

```scala
object Solution {
  def minCost(houses: Array[Int], cost: Array[Array[Int]], m: Int, n: Int, target: Int): Int = {
    if (target > m) return -1
    val INF: Long = 1L << 60

    var dpPrev = Array.fill(target + 1, n + 1)(INF)

    // initialize for first house
    if (houses(0) != 0) {
      val c = houses(0)
      dpPrev(1)(c) = 0L
    } else {
      for (c <- 1 to n) {
        dpPrev(1)(c) = cost(0)(c - 1).toLong
      }
    }

    // process remaining houses
    for (i <- 1 until m) {
      val dpCurr = Array.fill(target + 1, n + 1)(INF)
      val painted = houses(i)

      val allowedColors: Seq[Int] =
        if (painted != 0) Seq(painted) else (1 to n)

      for (t <- 1 to target) {
        for (curC <- allowedColors) {
          val paintCost = if (painted == 0) cost(i)(curC - 1).toLong else 0L

          // same color as previous house
          var best = dpPrev(t)(curC)

          // different color -> neighborhoods increase by 1
          if (t > 1) {
            var minDiff = INF
            for (prevC <- 1 to n if prevC != curC) {
              val v = dpPrev(t - 1)(prevC)
              if (v < minDiff) minDiff = v
            }
            if (minDiff < best) best = minDiff
          }

          if (best < INF) {
            val newCost = best + paintCost
            if (newCost < dpCurr(t)(curC)) dpCurr(t)(curC) = newCost
          }
        }
      }
      dpPrev = dpCurr
    }

    var ans = INF
    for (c <- 1 to n) {
      if (dpPrev(target)(c) < ans) ans = dpPrev(target)(c)
    }
    if (ans >= INF / 2) -1 else ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(houses: Vec<i32>, cost: Vec<Vec<i32>>, m: i32, n: i32, target: i32) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let target = target as usize;
        const INF: i32 = 1_000_000_000;

        // dp[t][c] = min cost for first processed houses with t neighborhoods, ending with color c
        let mut dp_prev = vec![vec![INF; n]; target + 1];

        // initialization for the first house
        if houses[0] != 0 {
            let c = (houses[0] - 1) as usize;
            dp_prev[1][c] = 0;
        } else {
            for c in 0..n {
                dp_prev[1][c] = cost[0][c];
            }
        }

        // process remaining houses
        for i in 1..m {
            let mut dp_cur = vec![vec![INF; n]; target + 1];
            for t in 1..=target {
                for c in 0..n {
                    // if house already painted with a different color, skip
                    if houses[i] != 0 && (houses[i] - 1) as usize != c {
                        continue;
                    }
                    let add = if houses[i] == 0 { cost[i][c] } else { 0 };
                    // case: same color as previous house -> neighborhoods unchanged
                    let mut best = dp_prev[t][c];
                    // case: different color -> new neighborhood, need t-1 before
                    if t > 1 {
                        let mut min_other = INF;
                        for pc in 0..n {
                            if pc == c { continue; }
                            if dp_prev[t - 1][pc] < min_other {
                                min_other = dp_prev[t - 1][pc];
                            }
                        }
                        if min_other < best {
                            best = min_other;
                        }
                    }
                    if best != INF {
                        let val = best + add;
                        if val < dp_cur[t][c] {
                            dp_cur[t][c] = val;
                        }
                    }
                }
            }
            dp_prev = dp_cur;
        }

        // answer: minimum cost with exactly target neighborhoods
        let mut ans = INF;
        for c in 0..n {
            if dp_prev[target][c] < ans {
                ans = dp_prev[target][c];
            }
        }
        if ans >= INF / 2 { -1 } else { ans }
    }
}
```

## Racket

```racket
(define INF 1000000000)

(define/contract (min-cost houses cost m n target)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((dp (make-vector (+ target 1) (lambda () (make-vector n INF)))))
    (for ([i (in-range m)])
      (define cur-house (list-ref houses i))
      (define cur-costs (list-ref cost i))
      (define newdp (make-vector (+ target 1) (lambda () (make-vector n INF))))
      (for ([c (in-range n)])
        (when (or (= cur-house 0) (= cur-house (+ c 1)))
          (define paint-cost (if (= cur-house 0) (list-ref cur-costs c) 0))
          (for ([k (in-range 1 (add1 target))])
            (cond
              [(= i 0)
               (when (= k 1)
                 (vector-set! (vector-ref newdp k) c paint-cost))]
              [else
               ;; same color continuation
               (define prev-same (vector-ref (vector-ref dp k) c))
               (when (< prev-same INF)
                 (let ([newc (+ prev-same paint-cost)])
                   (when (< newc (vector-ref (vector-ref newdp k) c))
                     (vector-set! (vector-ref newdp k) c newc))))
               ;; different color, start new neighborhood
               (when (> k 1)
                 (for ([p (in-range n)])
                   (unless (= p c)
                     (define prev-diff (vector-ref (vector-ref dp (- k 1)) p))
                     (when (< prev-diff INF)
                       (let ([newc (+ prev-diff paint-cost)])
                         (when (< newc (vector-ref (vector-ref newdp k) c))
                           (vector-set! (vector-ref newdp k) c newc)))))))])])))
      (set! dp newdp))
    (define ans INF)
    (for ([c (in-range n)])
      (define v (vector-ref (vector-ref dp target) c))
      (when (< v ans) (set! ans v)))
    (if (= ans INF) -1 ans)))
```

## Erlang

```erlang
-export([min_cost/5]).
-define(INF, 1 bsl 60).

min_cost(Houses, Cost, M, N, Target) ->
    CostRows = [list_to_tuple(Row) || Row <- Cost],
    INF = ?INF,
    FirstHouseColor = lists:nth(1, Houses),
    Row1 = lists:nth(1, CostRows),
    DP0 = case FirstHouseColor of
        0 ->
            maps:from_list([{{1, C}, element(C, Row1)} || C <- lists:seq(1, N)]);
        Color when Color >= 1, Color =< N ->
            #{ {1, Color} => 0 }
    end,
    DPFinal = loop(2, M, Houses, CostRows, N, Target, DP0),
    Ans = lists:foldl(fun(C, Min) ->
                Val = maps:get({Target, C}, DPFinal, INF),
                if Val < Min -> Val; true -> Min end
            end, INF, lists:seq(1, N)),
    case Ans >= INF of
        true -> -1;
        false -> Ans
    end.

loop(I, M, _Houses, _CostRows, _N, _Target, DPPrev) when I > M ->
    DPPrev;
loop(I, M, Houses, CostRows, N, Target, DPPrev) ->
    Row = lists:nth(I, CostRows),
    HouseColor = lists:nth(I, Houses),
    AllowedColors = case HouseColor of
        0 -> lists:seq(1, N);
        C -> [C]
    end,
    MaxT = erlang:min(I, Target),
    DPCurrent = maps:new(),
    DPNext = build_dp(1, MaxT, AllowedColors, Row, HouseColor, N, DPPrev, DPCurrent),
    loop(I + 1, M, Houses, CostRows, N, Target, DPNext).

build_dp(T, MaxT, _AllowedColors, _Row, _HouseColor, _N, DPPrev, DPMap) when T > MaxT ->
    DPMap;
build_dp(T, MaxT, AllowedColors, Row, HouseColor, N, DPPrev, DPMap) ->
    DPMap1 = lists:foldl(fun(C, AccMap) ->
                AddCost = case HouseColor of
                    0 -> element(C, Row);
                    _ -> 0
                end,
                Best = find_best(T, C, N, DPPrev, AddCost),
                case Best of
                    undefined -> AccMap;
                    Val -> maps:put({T, C}, Val, AccMap)
                end
            end, DPMap, AllowedColors),
    build_dp(T + 1, MaxT, AllowedColors, Row, HouseColor, N, DPPrev, DPMap1).

find_best(T, C, N, DPPrev, AddCost) ->
    INF = ?INF,
    MinVal = lists:foldl(fun(PC, CurMin) ->
                Delta = if C == PC -> 0; true -> 1 end,
                PrevT = T - Delta,
                case PrevT >= 1 of
                    true ->
                        PrevCost = maps:get({PrevT, PC}, DPPrev, INF),
                        Cand = PrevCost + AddCost,
                        if Cand < CurMin -> Cand; true -> CurMin end;
                    false -> CurMin
                end
            end, INF, lists:seq(1, N)),
    case MinVal of
        INF -> undefined;
        _   -> MinVal
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(houses :: [integer], cost :: [[integer]], m :: integer, n :: integer, target :: integer) :: integer
  def min_cost(houses, cost, m, n, target) do
    inf = 1_000_000_000_000

    dp0 =
      if hd(houses) != 0 do
        c = hd(houses)
        %{{1, c} => 0}
      else
        Enum.reduce(1..n, %{}, fn cur, acc ->
          Map.put(acc, {1, cur}, Enum.at(cost, 0) |> Enum.at(cur - 1))
        end)
      end

    dp_final =
      Enum.reduce(1..(m - 1), dp0, fn i, dp_prev ->
        house_color = Enum.at(houses, i)

        dp_cur =
          Enum.reduce(1..target, %{}, fn t, acc_t ->
            Enum.reduce(1..n, acc_t, fn cur, acc_c ->
              cond do
                house_color != 0 and house_color != cur ->
                  acc_c

                true ->
                  paint_cost =
                    if house_color == 0,
                      do: Enum.at(cost, i) |> Enum.at(cur - 1),
                      else: 0

                  min_val =
                    Enum.reduce(1..n, inf, fn prev, best ->
                      delta = if cur == prev, do: 0, else: 1
                      prev_t = t - delta

                      if prev_t >= 1 do
                        prev_cost = Map.get(dp_prev, {prev_t, prev}, inf)

                        if prev_cost != inf do
                          total = prev_cost + paint_cost
                          if total < best, do: total, else: best
                        else
                          best
                        end
                      else
                        best
                      end
                    end)

                  if min_val < inf do
                    Map.put(acc_c, {t, cur}, min_val)
                  else
                    acc_c
                  end
              end
            end)
          end)

        dp_cur
      end)

    ans =
      Enum.reduce(1..n, inf, fn cur, best ->
        val = Map.get(dp_final, {target, cur}, inf)
        if val < best, do: val, else: best
      end)

    if ans == inf, do: -1, else: ans
  end
end
```

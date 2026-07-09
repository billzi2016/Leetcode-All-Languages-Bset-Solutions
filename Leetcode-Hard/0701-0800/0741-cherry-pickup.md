# 0741. Cherry Pickup

## Cpp

```cpp
class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int n = grid.size();
        const int INF_NEG = -1e9;
        vector<vector<int>> dp(n, vector<int>(n, INF_NEG));
        dp[0][0] = grid[0][0];
        for (int t = 1; t <= 2 * (n - 1); ++t) {
            vector<vector<int>> ndp(n, vector<int>(n, INF_NEG));
            int c1_min = max(0, t - (n - 1));
            int c1_max = min(n - 1, t);
            for (int c1 = c1_min; c1 <= c1_max; ++c1) {
                int r1 = t - c1;
                if (grid[r1][c1] == -1) continue;
                int c2_min = c1_min; // same range for c2
                int c2_max = c1_max;
                for (int c2 = c2_min; c2 <= c2_max; ++c2) {
                    int r2 = t - c2;
                    if (grid[r2][c2] == -1) continue;
                    int bestPrev = INF_NEG;
                    // four possible previous states
                    if (c1 > 0 && c2 > 0) bestPrev = max(bestPrev, dp[c1 - 1][c2 - 1]);
                    if (c1 > 0)          bestPrev = max(bestPrev, dp[c1 - 1][c2]);
                    if (c2 > 0)          bestPrev = max(bestPrev, dp[c1][c2 - 1]);
                                         bestPrev = max(bestPrev, dp[c1][c2]);
                    if (bestPrev == INF_NEG) continue;
                    int add = grid[r1][c1];
                    if (c1 != c2) add += grid[r2][c2];
                    ndp[c1][c2] = bestPrev + add;
                }
            }
            dp.swap(ndp);
        }
        return max(0, dp[n - 1][n - 1]);
    }
};
```

## Java

```java
class Solution {
    public int cherryPickup(int[][] grid) {
        int n = grid.length;
        int INF_NEG = Integer.MIN_VALUE / 4; // safe negative infinity
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(dp[i], INF_NEG);
        }
        dp[0][0] = grid[0][0]; // both start at (0,0)

        for (int t = 1; t <= 2 * (n - 1); t++) {
            int[][] ndp = new int[n][n];
            for (int i = 0; i < n; i++) java.util.Arrays.fill(ndp[i], INF_NEG);

            int cStart = Math.max(0, t - (n - 1));
            int cEnd = Math.min(n - 1, t);
            for (int c1 = cStart; c1 <= cEnd; c1++) {
                int r1 = t - c1;
                if (r1 < 0 || r1 >= n) continue;
                if (grid[r1][c1] == -1) continue;

                for (int c2 = cStart; c2 <= cEnd; c2++) {
                    int r2 = t - c2;
                    if (r2 < 0 || r2 >= n) continue;
                    if (grid[r2][c2] == -1) continue;

                    int curVal = grid[r1][c1];
                    if (c1 != c2) curVal += grid[r2][c2];

                    int bestPrev = INF_NEG;
                    // previous positions: (r-1,c) or (r,c-1)
                    for (int dc1 = 0; dc1 >= -1; dc1--) {
                        int pc1 = c1 + dc1;
                        int pr1 = t - 1 - pc1;
                        if (pc1 < 0 || pc1 >= n || pr1 < 0 || pr1 >= n) continue;

                        for (int dc2 = 0; dc2 >= -1; dc2--) {
                            int pc2 = c2 + dc2;
                            int pr2 = t - 1 - pc2;
                            if (pc2 < 0 || pc2 >= n || pr2 < 0 || pr2 >= n) continue;

                            bestPrev = Math.max(bestPrev, dp[pc1][pc2]);
                        }
                    }

                    if (bestPrev == INF_NEG) continue;
                    ndp[c1][c2] = bestPrev + curVal;
                }
            }
            dp = ndp;
        }

        int result = dp[n - 1][n - 1];
        return Math.max(result, 0);
    }
}
```

## Python

```python
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        INF = -10**9
        dp = [[INF] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for t in range(1, 2 * n - 1):
            dp2 = [[INF] * n for _ in range(n)]
            c_start = max(0, t - (n - 1))
            c_end = min(n - 1, t)
            for c1 in range(c_start, c_end + 1):
                r1 = t - c1
                if r1 < 0 or r1 >= n:
                    continue
                for c2 in range(c_start, c_end + 1):
                    r2 = t - c2
                    if r2 < 0 or r2 >= n:
                        continue
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue

                    cur = grid[r1][c1]
                    if c1 != c2:
                        cur += grid[r2][c2]

                    best = INF
                    # four possible previous states
                    for pc1 in (c1, c1 - 1):
                        for pc2 in (c2, c2 - 1):
                            if pc1 >= 0 and pc2 >= 0:
                                best = max(best, dp[pc1][pc2])
                    if best == INF:
                        continue
                    dp2[c1][c2] = best + cur
            dp = dp2

        return max(dp[n - 1][n - 1], 0)
```

## Python3

```python
class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        INF_NEG = -10**9
        dp = [[INF_NEG] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        for t in range(1, 2 * n - 1):
            ndp = [[INF_NEG] * n for _ in range(n)]
            c1_min = max(0, t - (n - 1))
            c1_max = min(n - 1, t)
            for c1 in range(c1_min, c1_max + 1):
                r1 = t - c1
                if grid[r1][c1] == -1:
                    continue
                c2_min = c1_min
                c2_max = c1_max
                for c2 in range(c2_min, c2_max + 1):
                    r2 = t - c2
                    if grid[r2][c2] == -1:
                        continue
                    best = INF_NEG
                    # previous positions: (r1-1,c1) or (r1,c1-1) for person1
                    # and similarly for person2
                    for dc1 in (0, 1):
                        for dc2 in (0, 1):
                            pc1 = c1 - dc1
                            pc2 = c2 - dc2
                            if pc1 < 0 or pc2 < 0:
                                continue
                            prev = dp[pc1][pc2]
                            if prev > best:
                                best = prev
                    if best == INF_NEG:
                        continue
                    val = best + grid[r1][c1]
                    if c1 != c2:
                        val += grid[r2][c2]
                    ndp[c1][c2] = val
            dp = ndp
        return max(0, dp[n - 1][n - 1])
```

## C

```c
#include <limits.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int cherryPickup(int** grid, int gridSize, int* gridColSize){
    int n = gridSize;
    static int dp[51][51];
    static int ndp[51][51];
    
    // Initialize dp with very small value
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            dp[i][j] = INT_MIN;
    
    dp[0][0] = grid[0][0]; // starting cell, guaranteed not -1
    
    int maxStep = 2 * (n - 1);
    for (int t = 1; t <= maxStep; ++t) {
        // reset ndp
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                ndp[i][j] = INT_MIN;
        
        int cStart = t - (n - 1);
        if (cStart < 0) cStart = 0;
        int cEnd = t;
        if (cEnd > n - 1) cEnd = n - 1;
        
        for (int c1 = cStart; c1 <= cEnd; ++c1) {
            int r1 = t - c1;
            if (r1 < 0 || r1 >= n) continue;
            for (int c2 = cStart; c2 <= cEnd; ++c2) {
                int r2 = t - c2;
                if (r2 < 0 || r2 >= n) continue;
                
                if (grid[r1][c1] == -1 || grid[r2][c2] == -1) continue;
                
                int curVal = grid[r1][c1];
                if (c1 != c2) curVal += grid[r2][c2];
                
                int bestPrev = INT_MIN;
                // both came from up
                if (r1 > 0 && r2 > 0)
                    bestPrev = max(bestPrev, dp[c1][c2]);
                // person1 up, person2 left
                if (r1 > 0 && c2 > 0)
                    bestPrev = max(bestPrev, dp[c1][c2 - 1]);
                // person1 left, person2 up
                if (c1 > 0 && r2 > 0)
                    bestPrev = max(bestPrev, dp[c1 - 1][c2]);
                // both came from left
                if (c1 > 0 && c2 > 0)
                    bestPrev = max(bestPrev, dp[c1 - 1][c2 - 1]);
                
                if (bestPrev == INT_MIN) continue;
                
                ndp[c1][c2] = bestPrev + curVal;
            }
        }
        
        // copy ndp to dp for next iteration
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                dp[i][j] = ndp[i][j];
    }
    
    int result = dp[n - 1][n - 1];
    return result < 0 ? 0 : result;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int CherryPickup(int[][] grid) {
        int n = grid.Length;
        const int NEG_INF = int.MinValue / 4; // safe negative infinity
        
        int[,] dp = new int[n, n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                dp[i, j] = NEG_INF;
        
        dp[0, 0] = grid[0][0]; // start position
        
        int maxStep = 2 * n - 2;
        for (int t = 1; t <= maxStep; t++) {
            int[,] ndp = new int[n, n];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    ndp[i, j] = NEG_INF;
            
            int cStart = Math.Max(0, t - (n - 1));
            int cEnd   = Math.Min(n - 1, t);
            for (int c1 = cStart; c1 <= cEnd; c1++) {
                int r1 = t - c1;
                if (r1 < 0 || r1 >= n) continue;
                if (grid[r1][c1] == -1) continue;
                
                for (int c2 = cStart; c2 <= cEnd; c2++) {
                    int r2 = t - c2;
                    if (r2 < 0 || r2 >= n) continue;
                    if (grid[r2][c2] == -1) continue;
                    
                    int bestPrev = NEG_INF;
                    // both came from up
                    bestPrev = Math.Max(bestPrev, dp[c1, c2]);
                    // person1 came from left, person2 from up
                    if (c1 > 0) bestPrev = Math.Max(bestPrev, dp[c1 - 1, c2]);
                    // person1 from up, person2 from left
                    if (c2 > 0) bestPrev = Math.Max(bestPrev, dp[c1, c2 - 1]);
                    // both came from left
                    if (c1 > 0 && c2 > 0) bestPrev = Math.Max(bestPrev, dp[c1 - 1, c2 - 1]);
                    
                    if (bestPrev < 0) continue; // unreachable state
                    
                    int add = grid[r1][c1];
                    if (r1 != r2 || c1 != c2) add += grid[r2][c2]; // avoid double count
                    ndp[c1, c2] = bestPrev + add;
                }
            }
            dp = ndp;
        }
        
        int result = dp[n - 1, n - 1];
        return Math.Max(result, 0);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var cherryPickup = function(grid) {
    const n = grid.length;
    // dp[c1][c2] where both have taken the same number of steps t,
    // and are at (r1 = t - c1, c1) and (r2 = t - c2, c2)
    let dp = Array.from({ length: n }, () => Array(n).fill(-Infinity));
    dp[0][0] = grid[0][0]; // start position

    const maxT = 2 * (n - 1);
    for (let t = 1; t <= maxT; ++t) {
        const ndp = Array.from({ length: n }, () => Array(n).fill(-Infinity));
        const cStart = Math.max(0, t - (n - 1));
        const cEnd = Math.min(n - 1, t);
        for (let c1 = cStart; c1 <= cEnd; ++c1) {
            const r1 = t - c1;
            if (r1 < 0 || r1 >= n || grid[r1][c1] === -1) continue;
            for (let c2 = cStart; c2 <= cEnd; ++c2) {
                const r2 = t - c2;
                if (r2 < 0 || r2 >= n || grid[r2][c2] === -1) continue;

                let best = -Infinity;
                // both came from up (down move)
                best = Math.max(best, dp[c1][c2]);
                // person1 left, person2 up
                if (c1 > 0) best = Math.max(best, dp[c1 - 1][c2]);
                // person1 up, person2 left
                if (c2 > 0) best = Math.max(best, dp[c1][c2 - 1]);
                // both left (right move)
                if (c1 > 0 && c2 > 0) best = Math.max(best, dp[c1 - 1][c2 - 1]);

                if (best === -Infinity) continue;

                let add = grid[r1][c1];
                if (r1 !== r2 || c1 !== c2) add += grid[r2][c2];
                ndp[c1][c2] = best + add;
            }
        }
        dp = ndp;
    }

    const result = dp[n - 1][n - 1];
    return result < 0 ? 0 : result;
};
```

## Typescript

```typescript
function cherryPickup(grid: number[][]): number {
    const n = grid.length;
    const NEG_INF = -1e9;
    let dpPrev: number[][] = Array.from({ length: n }, () => Array(n).fill(NEG_INF));
    dpPrev[0][0] = grid[0][0];

    for (let t = 1; t <= 2 * n - 2; ++t) {
        const dp: number[][] = Array.from({ length: n }, () => Array(n).fill(NEG_INF));
        const cStart = Math.max(0, t - (n - 1));
        const cEnd = Math.min(n - 1, t);
        for (let c1 = cStart; c1 <= cEnd; ++c1) {
            const r1 = t - c1;
            if (r1 < 0 || r1 >= n || grid[r1][c1] === -1) continue;
            for (let c2 = cStart; c2 <= cEnd; ++c2) {
                const r2 = t - c2;
                if (r2 < 0 || r2 >= n || grid[r2][c2] === -1) continue;

                let best = NEG_INF;
                // both came from up
                if (dpPrev[c1][c2] > best) best = dpPrev[c1][c2];
                // p1 left, p2 up
                if (c1 > 0 && dpPrev[c1 - 1][c2] > best) best = dpPrev[c1 - 1][c2];
                // p1 up, p2 left
                if (c2 > 0 && dpPrev[c1][c2 - 1] > best) best = dpPrev[c1][c2 - 1];
                // both left
                if (c1 > 0 && c2 > 0 && dpPrev[c1 - 1][c2 - 1] > best) best = dpPrev[c1 - 1][c2 - 1];

                if (best === NEG_INF) continue;

                let add = grid[r1][c1];
                if (r1 !== r2 || c1 !== c2) {
                    add += grid[r2][c2];
                }
                dp[c1][c2] = best + add;
            }
        }
        dpPrev = dp;
    }

    const result = dpPrev[n - 1][n - 1];
    return Math.max(0, result);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function cherryPickup($grid) {
        $n = count($grid);
        $INF = -1000000; // sufficiently small negative number
        
        // dp[c1][c2] for current layer t
        $dp = array_fill(0, $n, array_fill(0, $n, $INF));
        $dp[0][0] = $grid[0][0];
        
        $maxT = 2 * $n - 2;
        for ($t = 1; $t <= $maxT; $t++) {
            $dpNext = array_fill(0, $n, array_fill(0, $n, $INF));
            $cMin = max(0, $t - ($n - 1));
            $cMax = min($n - 1, $t);
            
            for ($c1 = $cMin; $c1 <= $cMax; $c1++) {
                $r1 = $t - $c1;
                if ($grid[$r1][$c1] == -1) continue;
                
                for ($c2 = $cMin; $c2 <= $cMax; $c2++) {
                    $r2 = $t - $c2;
                    if ($grid[$r2][$c2] == -1) continue;
                    
                    $best = $INF;
                    // both came from up (down move)
                    $best = max($best, $dp[$c1][$c2]);
                    // p1 right, p2 down
                    if ($c1 > 0) $best = max($best, $dp[$c1 - 1][$c2]);
                    // p1 down, p2 right
                    if ($c2 > 0) $best = max($best, $dp[$c1][$c2 - 1]);
                    // both right
                    if ($c1 > 0 && $c2 > 0) $best = max($best, $dp[$c1 - 1][$c2 - 1]);
                    
                    if ($best < $INF / 2) continue; // unreachable state
                    
                    $add = $grid[$r1][$c1];
                    if (!($r1 == $r2 && $c1 == $c2)) {
                        $add += $grid[$r2][$c2];
                    }
                    
                    $dpNext[$c1][$c2] = $best + $add;
                }
            }
            $dp = $dpNext;
        }
        
        $ans = $dp[$n - 1][$n - 1];
        return max(0, $ans);
    }
}
```

## Swift

```swift
class Solution {
    func cherryPickup(_ grid: [[Int]]) -> Int {
        let n = grid.count
        let NEG_INF = -1_000_000_000
        var dp = Array(repeating: Array(repeating: NEG_INF, count: n), count: n)
        dp[0][0] = grid[0][0]
        
        if n == 1 {
            return max(0, dp[0][0])
        }
        
        for t in 1...(2 * n - 2) {
            var newDP = Array(repeating: Array(repeating: NEG_INF, count: n), count: n)
            let cStart = max(0, t - (n - 1))
            let cEnd = min(n - 1, t)
            if cStart > cEnd { continue }
            for c1 in cStart...cEnd {
                let r1 = t - c1
                if r1 < 0 || r1 >= n { continue }
                if grid[r1][c1] == -1 { continue }
                for c2 in cStart...cEnd {
                    let r2 = t - c2
                    if r2 < 0 || r2 >= n { continue }
                    if grid[r2][c2] == -1 { continue }
                    
                    var best = NEG_INF
                    // both came from up (down move)
                    best = max(best, dp[c1][c2])
                    // person1 came from left, person2 from up
                    if c1 > 0 {
                        best = max(best, dp[c1 - 1][c2])
                    }
                    // person1 from up, person2 from left
                    if c2 > 0 {
                        best = max(best, dp[c1][c2 - 1])
                    }
                    // both came from left
                    if c1 > 0 && c2 > 0 {
                        best = max(best, dp[c1 - 1][c2 - 1])
                    }
                    
                    if best == NEG_INF { continue }
                    
                    var cur = best + grid[r1][c1]
                    if r1 != r2 || c1 != c2 {
                        cur += grid[r2][c2]
                    }
                    newDP[c1][c2] = max(newDP[c1][c2], cur)
                }
            }
            dp = newDP
        }
        
        let result = dp[n - 1][n - 1]
        return max(0, result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun cherryPickup(grid: Array<IntArray>): Int {
        val n = grid.size
        val INF = -1_000_000_0
        var dp = Array(n) { IntArray(n) { INF } }
        dp[0][0] = if (grid[0][0] == -1) INF else grid[0][0]
        for (t in 1 until 2 * n - 1) {
            val ndp = Array(n) { IntArray(n) { INF } }
            val cStart = maxOf(0, t - (n - 1))
            val cEnd = minOf(n - 1, t)
            for (c1 in cStart..cEnd) {
                val r1 = t - c1
                if (r1 !in 0 until n) continue
                if (grid[r1][c1] == -1) continue
                for (c2 in cStart..cEnd) {
                    val r2 = t - c2
                    if (r2 !in 0 until n) continue
                    if (grid[r2][c2] == -1) continue
                    var best = INF
                    // both came from up
                    best = maxOf(best, dp[c1][c2])
                    // person1 left, person2 up
                    if (c1 > 0) best = maxOf(best, dp[c1 - 1][c2])
                    // person1 up, person2 left
                    if (c2 > 0) best = maxOf(best, dp[c1][c2 - 1])
                    // both came from left
                    if (c1 > 0 && c2 > 0) best = maxOf(best, dp[c1 - 1][c2 - 1])
                    if (best == INF) continue
                    var add = grid[r1][c1]
                    if (r1 != r2 || c1 != c2) {
                        add += grid[r2][c2]
                    }
                    ndp[c1][c2] = best + add
                }
            }
            dp = ndp
        }
        val result = dp[n - 1][n - 1]
        return if (result < 0) 0 else result
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int cherryPickup(List<List<int>> grid) {
    int n = grid.length;
    const int NEG_INF = -1000000000;

    List<List<int>> dp =
        List.generate(n, (_) => List.filled(n, NEG_INF), growable: false);
    dp[0][0] = grid[0][0];

    for (int t = 1; t <= 2 * (n - 1); ++t) {
      List<List<int>> ndp =
          List.generate(n, (_) => List.filled(n, NEG_INF), growable: false);
      int cStart = max(0, t - (n - 1));
      int cEnd = min(n - 1, t);

      for (int c1 = cStart; c1 <= cEnd; ++c1) {
        int r1 = t - c1;
        if (r1 < 0 || r1 >= n) continue;
        if (grid[r1][c1] == -1) continue;

        for (int c2 = cStart; c2 <= cEnd; ++c2) {
          int r2 = t - c2;
          if (r2 < 0 || r2 >= n) continue;
          if (grid[r2][c2] == -1) continue;

          int best = NEG_INF;
          for (int d1 = 0; d1 <= 1; ++d1) {
            for (int d2 = 0; d2 <= 1; ++d2) {
              int pc1 = c1 - d1;
              int pc2 = c2 - d2;
              if (pc1 < 0 || pc2 < 0) continue;
              best = max(best, dp[pc1][pc2]);
            }
          }

          if (best == NEG_INF) continue;

          int cur = grid[r1][c1];
          if (r1 != r2 || c1 != c2) cur += grid[r2][c2];
          ndp[c1][c2] = best + cur;
        }
      }
      dp = ndp;
    }

    int result = dp[n - 1][n - 1];
    return max(result, 0);
  }
}
```

## Golang

```go
func cherryPickup(grid [][]int) int {
	const INF = -1000000000
	n := len(grid)
	// dp[c1][c2] for previous layer
	prev := make([][]int, n)
	for i := 0; i < n; i++ {
		prev[i] = make([]int, n)
		for j := 0; j < n; j++ {
			prev[i][j] = INF
		}
	}
	if grid[0][0] != -1 {
		prev[0][0] = grid[0][0]
	}

	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	for t := 1; t <= 2*n-2; t++ {
		cur := make([][]int, n)
		for i := 0; i < n; i++ {
			cur[i] = make([]int, n)
			for j := 0; j < n; j++ {
				cur[i][j] = INF
			}
		}
		cLow := max(0, t-(n-1))
		cHigh := min(n-1, t)
		for c1 := cLow; c1 <= cHigh; c1++ {
			r1 := t - c1
			if r1 < 0 || r1 >= n || grid[r1][c1] == -1 {
				continue
			}
			for c2 := cLow; c2 <= cHigh; c2++ {
				r2 := t - c2
				if r2 < 0 || r2 >= n || grid[r2][c2] == -1 {
					continue
				}
				bestPrev := INF
				// both came from up (down move)
				bestPrev = max(bestPrev, prev[c1][c2])
				// p1 left, p2 up
				if c1 > 0 {
					bestPrev = max(bestPrev, prev[c1-1][c2])
				}
				// p1 up, p2 left
				if c2 > 0 {
					bestPrev = max(bestPrev, prev[c1][c2-1])
				}
				// both left (right move)
				if c1 > 0 && c2 > 0 {
					bestPrev = max(bestPrev, prev[c1-1][c2-1])
				}
				if bestPrev == INF {
					continue
				}
				val := bestPrev + grid[r1][c1]
				if r1 != r2 || c1 != c2 {
					val += grid[r2][c2]
				}
				cur[c1][c2] = val
			}
		}
		prev = cur
	}
	ans := prev[n-1][n-1]
	if ans < 0 {
		return 0
	}
	return ans
}
```

## Ruby

```ruby
def cherry_pickup(grid)
  n = grid.size
  max_t = 2 * (n - 1)
  neg_inf = -Float::INFINITY

  prev = Array.new(n) { Array.new(n, neg_inf) }
  prev[0][0] = grid[0][0]

  (1..max_t).each do |t|
    curr = Array.new(n) { Array.new(n, neg_inf) }

    c_min = [0, t - (n - 1)].max
    c_max = [n - 1, t].min

    (c_min..c_max).each do |c1|
      r1 = t - c1
      next if r1 < 0 || r1 >= n
      (c_min..c_max).each do |c2|
        r2 = t - c2
        next if r2 < 0 || r2 >= n
        next if grid[r1][c1] == -1 || grid[r2][c2] == -1

        max_prev = prev[c1][c2]
        max_prev = [max_prev, prev[c1 - 1][c2]].max if c1 > 0
        max_prev = [max_prev, prev[c1][c2 - 1]].max if c2 > 0
        max_prev = [max_prev, prev[c1 - 1][c2 - 1]].max if c1 > 0 && c2 > 0
        next if max_prev == neg_inf

        add = grid[r1][c1]
        add += grid[r2][c2] if r1 != r2 || c1 != c2
        curr[c1][c2] = max_prev + add
      end
    end

    prev = curr
  end

  result = prev[n - 1][n - 1]
  result < 0 ? 0 : result.to_i
end
```

## Scala

```scala
object Solution {
  def cherryPickup(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val NEG = -1000000000
    var dp = Array.fill(n, n)(NEG)
    dp(0)(0) = grid(0)(0)

    for (t <- 1 to 2 * (n - 1)) {
      val ndp = Array.fill(n, n)(NEG)
      val cStart = math.max(0, t - (n - 1))
      val cEnd   = math.min(n - 1, t)

      var c1 = cStart
      while (c1 <= cEnd) {
        val r1 = t - c1
        if (r1 < n && grid(r1)(c1) != -1) {
          var c2 = cStart
          while (c2 <= cEnd) {
            val r2 = t - c2
            if (r2 < n && grid(r2)(c2) != -1) {
              var best = NEG
              // both moved down
              best = math.max(best, dp(c1)(c2))
              // p1 right, p2 down
              if (c1 > 0) best = math.max(best, dp(c1 - 1)(c2))
              // p1 down, p2 right
              if (c2 > 0) best = math.max(best, dp(c1)(c2 - 1))
              // both moved right
              if (c1 > 0 && c2 > 0) best = math.max(best, dp(c1 - 1)(c2 - 1))

              if (best != NEG) {
                var add = grid(r1)(c1)
                if (r1 != r2 || c1 != c2) add += grid(r2)(c2)
                ndp(c1)(c2) = best + add
              }
            }
            c2 += 1
          }
        }
        c1 += 1
      }

      dp = ndp
    }

    val ans = dp(n - 1)(n - 1)
    if (ans < 0) 0 else ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        const NEG_INF: i32 = -1_000_000_000;
        let mut dp = vec![vec![NEG_INF; n]; n];
        dp[0][0] = grid[0][0];

        for t in 1..(2 * n - 1) {
            let mut ndp = vec![vec![NEG_INF; n]; n];
            let c_start = if t >= n { t - (n - 1) } else { 0 };
            let c_end = std::cmp::min(n - 1, t);
            for c1 in c_start..=c_end {
                let r1 = t - c1;
                if r1 >= n || grid[r1][c1] == -1 {
                    continue;
                }
                for c2 in c_start..=c_end {
                    let r2 = t - c2;
                    if r2 >= n || grid[r2][c2] == -1 {
                        continue;
                    }

                    // find best previous state
                    let mut best = NEG_INF;
                    for &dc1 in &[0, 1] {
                        for &dc2 in &[0, 1] {
                            if dc1 == 1 && c1 == 0 { continue; }
                            if dc2 == 1 && c2 == 0 { continue; }
                            let pc1 = c1 - dc1;
                            let pc2 = c2 - dc2;
                            best = best.max(dp[pc1][pc2]);
                        }
                    }
                    if best == NEG_INF {
                        continue;
                    }

                    let mut val = grid[r1][c1];
                    if c1 != c2 {
                        val += grid[r2][c2];
                    }
                    ndp[c1][c2] = best + val;
                }
            }
            dp = ndp;
        }

        let ans = dp[n - 1][n - 1];
        if ans < 0 { 0 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (cherry-pickup grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (gridV (list->vector (map list->vector grid)))
         (INF -1000000)
         (dp (make-vector n (lambda () (make-vector n INF)))))
    ;; start position
    (vector-set! (vector-ref dp 0) 0 (vector-ref (vector-ref gridV 0) 0))
    (let loop ((t 1) (dp dp))
      (if (> t (* 2 (- n 1)))
          (max 0 (vector-ref (vector-ref dp (sub1 n)) (sub1 n)))
          (let* ((dp2 (make-vector n (lambda () (make-vector n INF))))
                 (c-start (max 0 (- t (- n 1))))
                 (c-end (min (- n 1) t)))
            (for ([c1 (in-range c-start (add1 c-end))])
              (let ((r1 (- t c1)))
                (when (< r1 n)
                  (for ([c2 (in-range c-start (add1 c-end))])
                    (let ((r2 (- t c2)))
                      (when (< r2 n)
                        (let ((cell1 (vector-ref (vector-ref gridV r1) c1))
                              (cell2 (vector-ref (vector-ref gridV r2) c2)))
                          (when (and (not (= cell1 -1)) (not (= cell2 -1)))
                            (let ((best INF))
                              ;; both came from up
                              (let ((prev (vector-ref (vector-ref dp c1) c2)))
                                (when (> prev best) (set! best prev)))
                              ;; person1 right, person2 down
                              (when (> c1 0)
                                (let ((prev (vector-ref (vector-ref dp (sub1 c1)) c2)))
                                  (when (> prev best) (set! best prev))))
                              ;; person1 down, person2 right
                              (when (> c2 0)
                                (let ((prev (vector-ref (vector-ref dp c1) (sub1 c2))))
                                  (when (> prev best) (set! best prev))))
                              ;; both right
                              (when (and (> c1 0) (> c2 0))
                                (let ((prev (vector-ref (vector-ref dp (sub1 c1)) (sub1 c2))))
                                  (when (> prev best) (set! best prev))))
                              (unless (= best INF)
                                (let ((add cell1))
                                  (when (or (not (= r1 r2)) (not (= c1 c2)))
                                    (set! add (+ add cell2)))
                                  (vector-set! (vector-ref dp2 c1) c2 (+ best add)))))))))))))
            (loop (add1 t) dp2))))))
```

## Erlang

```erlang
-module(solution).
-export([cherry_pickup/1]).

-spec cherry_pickup(Grid :: [[integer()]]) -> integer().
cherry_pickup(Grid) ->
    N = length(Grid),
    StartVal = get_cell(Grid, 0, 0),
    DP0 = #{ {0,0} => StartVal },
    MaxT = 2 * (N - 1),
    FinalDP = iterate_layers(1, MaxT, N, Grid, DP0),
    case maps:get({N-1,N-1}, FinalDP, undefined) of
        undefined -> 0;
        Val when Val < 0 -> 0;
        Val -> Val
    end.

%% Iterate over layers t = Cur .. MaxT
iterate_layers(Cur, MaxT, _N, _Grid, DP) when Cur > MaxT ->
    DP;
iterate_layers(Cur, MaxT, N, Grid, DPPrev) ->
    DPCurr = process_layer(Cur, N, Grid, DPPrev),
    iterate_layers(Cur + 1, MaxT, N, Grid, DPCurr).

%% Process a single layer t
process_layer(T, N, Grid, DPPrev) ->
    lists:foldl(
      fun(C1, AccC1) ->
          R1 = T - C1,
          if R1 < 0 orelse R1 >= N -> AccC1;
             true ->
                 lists:foldl(
                   fun(C2, AccC2) ->
                       R2 = T - C2,
                       if R2 < 0 orelse R2 >= N -> AccC2;
                          true ->
                              case get_cell(Grid, R1, C1) of
                                  -1 -> AccC2;
                                  V1 ->
                                      case get_cell(Grid, R2, C2) of
                                          -1 -> AccC2;
                                          V2 ->
                                              case best_prev(C1, C2, DPPrev) of
                                                  undefined -> AccC2;
                                                  BestPrev ->
                                                      Add = if C1 == C2 andalso R1 == R2 -> V1;
                                                               true -> V1 + V2 end,
                                                      maps:put({C1, C2}, BestPrev + Add, AccC2)
                                              end
                                      end
                              end
                       end
                   end, AccC1, lists:seq(0, N-1))
          end
      end, #{}, lists:seq(0, N-1)).

%% Find the best previous value among four possible moves
best_prev(C1, C2, DPPrev) ->
    Candidates = [
        maps:get({C1,   C2},   DPPrev, undefined),
        (if C1 > 0 -> maps:get({C1-1, C2},   DPPrev, undefined); true -> undefined end),
        (if C2 > 0 -> maps:get({C1,   C2-1}, DPPrev, undefined); true -> undefined end),
        (if C1 > 0 andalso C2 > 0 -> maps:get({C1-1, C2-1}, DPPrev, undefined); true -> undefined end)
    ],
    Valid = [V || V <- Candidates, V =/= undefined],
    case Valid of
        [] -> undefined;
        _  -> lists:max(Valid)
    end.

%% Retrieve cell value from grid (0‑based indices)
get_cell(Grid, R, C) ->
    Row = lists:nth(R + 1, Grid),
    lists:nth(C + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec cherry_pickup(grid :: [[integer]]) :: integer
  def cherry_pickup(grid) do
    n = length(grid)
    max_steps = 2 * (n - 1)

    start_val = cell(grid, 0, 0)
    dp_prev = %{{0, 0} => start_val}

    dp_final =
      Enum.reduce(1..max_steps, dp_prev, fn t, dp_acc ->
        c_min = max(0, t - (n - 1))
        c_max = min(n - 1, t)

        for c1 <- c_min..c_max,
            c2 <- c_min..c_max,
            reduce: %{} do
          acc ->
            r1 = t - c1
            r2 = t - c2

            val1 = cell(grid, r1, c1)
            val2 = cell(grid, r2, c2)

            if val1 == -1 or val2 == -1 do
              acc
            else
              max_prev =
                [
                  Map.get(dp_acc, {c1, c2}, -1_000_000),
                  Map.get(dp_acc, {c1 - 1, c2}, -1_000_000),
                  Map.get(dp_acc, {c1, c2 - 1}, -1_000_000),
                  Map.get(dp_acc, {c1 - 1, c2 - 1}, -1_000_000)
                ]
                |> Enum.max()

              if max_prev < 0 do
                acc
              else
                add = val1 + (if c1 != c2, do: val2, else: 0)
                Map.put(acc, {c1, c2}, max_prev + add)
              end
            end
        end
      end)

    result = Map.get(dp_final, {n - 1, n - 1}, 0)
    if result < 0, do: 0, else: result
  end

  defp cell(grid, r, c) do
    row = Enum.at(grid, r)
    Enum.at(row, c)
  end
end
```

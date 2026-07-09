# 3459. Length of Longest V-Shaped Diagonal Segment

## Cpp

```cpp
class Solution {
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = grid.size();
        if (n == 0) return 0;
        int m = grid[0].size();
        // The longest V-shaped diagonal segment in an empty grid is limited by the smaller dimension.
        return min(n, m);
    }
};
```

## Java

```java
class Solution {
    public int lenOfVDiagonal(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        // dp1[i][j]: length of diagonal (down-right) ending at (i,j)
        int[][] downRight = new int[n][m];
        // dp2[i][j]: length of diagonal (down-left) ending at (i,j)
        int[][] downLeft = new int[n][m];

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (i > 0 && j > 0) downRight[i][j] = downRight[i - 1][j - 1] + 1;
                else downRight[i][j] = 1;

                if (i > 0 && j + 1 < m) downLeft[i][j] = downLeft[i - 1][j + 1] + 1;
                else downLeft[i][j] = 1;
            }
        }

        int ans = 0;
        // For each possible apex (turn point), combine a diagonal coming from up-left
        // and a diagonal coming from up-right.
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int len = downRight[i][j] + downLeft[i][j] - 1;
                if (len > ans) ans = len;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dr = [[0]*m for _ in range(n)]  # down-right
        dl = [[0]*m for _ in range(n)]  # down-left
        ur = [[0]*m for _ in range(n)]  # up-right
        ul = [[0]*m for _ in range(n)]  # up-left

        # down-right
        for i in range(n-1, -1, -1):
            row_dr = dr[i]
            for j in range(m-1, -1, -1):
                if i+1 < n and j+1 < m:
                    row_dr[j] = dr[i+1][j+1] + 1
                else:
                    row_dr[j] = 1

        # down-left
        for i in range(n-1, -1, -1):
            row_dl = dl[i]
            for j in range(m):
                if i+1 < n and j-1 >= 0:
                    row_dl[j] = dl[i+1][j-1] + 1
                else:
                    row_dl[j] = 1

        # up-right
        for i in range(n):
            row_ur = ur[i]
            for j in range(m-1, -1, -1):
                if i-1 >= 0 and j+1 < m:
                    row_ur[j] = ur[i-1][j+1] + 1
                else:
                    row_ur[j] = 1

        # up-left
        for i in range(n):
            row_ul = ul[i]
            for j in range(m):
                if i-1 >= 0 and j-1 >= 0:
                    row_ul[j] = ul[i-1][j-1] + 1
                else:
                    row_ul[j] = 1

        ans = 0
        for i in range(n):
            for j in range(m):
                d_r = dr[i][j]
                d_l = dl[i][j]
                u_r = ur[i][j]
                u_l = ul[i][j]

                # straight diagonals
                if d_r > ans: ans = d_r
                if d_l > ans: ans = d_l
                if u_r > ans: ans = u_r
                if u_l > ans: ans = u_l

                # V-shaped (clockwise turn)
                v1 = d_r + d_l - 1
                if v1 > ans: ans = v1
                v2 = d_l + u_l - 1
                if v2 > ans: ans = v2
                v3 = u_l + u_r - 1
                if v3 > ans: ans = v3
                v4 = u_r + d_r - 1
                if v4 > ans: ans = v4

        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # up-left diagonal lengths ending at (i,j)
        ul = [[0] * m for _ in range(n)]
        # up-right diagonal lengths ending at (i,j)
        ur = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    ul[i][j] = ul[i-1][j-1] + 1
                else:
                    ul[i][j] = 1
                if i > 0 and j + 1 < m:
                    ur[i][j] = ur[i-1][j+1] + 1
                else:
                    ur[i][j] = 1

        # down-right diagonal lengths starting at (i,j)
        dr = [[0] * m for _ in range(n)]
        # down-left diagonal lengths starting at (i,j)
        dl = [[0] * m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i + 1 < n and j + 1 < m:
                    dr[i][j] = dr[i+1][j+1] + 1
                else:
                    dr[i][j] = 1
                if i + 1 < n and j - 1 >= 0:
                    dl[i][j] = dl[i+1][j-1] + 1
                else:
                    dl[i][j] = 1

        ans = 0
        for i in range(n):
            for j in range(m):
                # straight diagonals
                ans = max(ans, ul[i][j] + dr[i][j] - 1)
                ans = max(ans, ur[i][j] + dl[i][j] - 1)
                # V-shaped (clockwise turn)
                ans = max(ans, ul[i][j] + dl[i][j] - 1)
                ans = max(ans, ur[i][j] + dr[i][j] - 1)

        return ans
```

## C

```c
#include <stdlib.h>

int lenOfVDiagonal(int** grid, int gridSize, int* gridColSize) {
    (void)grid; // grid values are not needed for the computation
    int n = gridSize;
    int m = gridColSize[0];

    // Allocate DP arrays
    int **dr = (int**)malloc(n * sizeof(int*));
    int **dl = (int**)malloc(n * sizeof(int*));
    int **ul = (int**)malloc(n * sizeof(int*));
    int **ur = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        dr[i] = (int*)malloc(m * sizeof(int));
        dl[i] = (int*)malloc(m * sizeof(int));
        ul[i] = (int*)malloc(m * sizeof(int));
        ur[i] = (int*)malloc(m * sizeof(int));
    }

    // down-right
    for (int i = n - 1; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            dr[i][j] = 1;
            if (i + 1 < n && j + 1 < m)
                dr[i][j] = dr[i + 1][j + 1] + 1;
        }
    }

    // down-left
    for (int i = n - 1; i >= 0; --i) {
        for (int j = 0; j < m; ++j) {
            dl[i][j] = 1;
            if (i + 1 < n && j - 1 >= 0)
                dl[i][j] = dl[i + 1][j - 1] + 1;
        }
    }

    // up-left
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            ul[i][j] = 1;
            if (i - 1 >= 0 && j - 1 >= 0)
                ul[i][j] = ul[i - 1][j - 1] + 1;
        }
    }

    // up-right
    for (int i = 0; i < n; ++i) {
        for (int j = m - 1; j >= 0; --j) {
            ur[i][j] = 1;
            if (i - 1 >= 0 && j + 1 < m)
                ur[i][j] = ur[i - 1][j + 1] + 1;
        }
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int v;
            v = dr[i][j] + dl[i][j] - 1;
            if (v > ans) ans = v;
            v = dl[i][j] + ul[i][j] - 1;
            if (v > ans) ans = v;
            v = ul[i][j] + ur[i][j] - 1;
            if (v > ans) ans = v;
            v = ur[i][j] + dr[i][j] - 1;
            if (v > ans) ans = v;
        }
    }

    // Free memory
    for (int i = 0; i < n; ++i) {
        free(dr[i]);
        free(dl[i]);
        free(ul[i]);
        free(ur[i]);
    }
    free(dr);
    free(dl);
    free(ul);
    free(ur);

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LenOfVDiagonal(int[][] grid) {
        int n = grid.Length;
        int m = grid[0].Length;
        int[,] downRightEnd = new int[n, m];
        int[,] downLeftEnd = new int[n, m];
        int[,] downRightStart = new int[n, m];
        int[,] downLeftStart = new int[n, m];

        // DP for longest diagonal ending at (i,j)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                downRightEnd[i, j] = 1;
                if (i > 0 && j > 0 && grid[i][j] != grid[i - 1][j - 1]) {
                    downRightEnd[i, j] = downRightEnd[i - 1, j - 1] + 1;
                }

                downLeftEnd[i, j] = 1;
                if (i > 0 && j + 1 < m && grid[i][j] != grid[i - 1][j + 1]) {
                    downLeftEnd[i, j] = downLeftEnd[i - 1, j + 1] + 1;
                }
            }
        }

        // DP for longest diagonal starting at (i,j) and going downwards
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                downRightStart[i, j] = 1;
                if (i + 1 < n && j + 1 < m && grid[i][j] != grid[i + 1][j + 1]) {
                    downRightStart[i, j] = downRightStart[i + 1, j + 1] + 1;
                }

                downLeftStart[i, j] = 1;
                if (i + 1 < n && j - 1 >= 0 && grid[i][j] != grid[i + 1][j - 1]) {
                    downLeftStart[i, j] = downLeftStart[i + 1, j - 1] + 1;
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // straight diagonal segments
                if (downRightEnd[i, j] > ans) ans = downRightEnd[i, j];
                if (downLeftEnd[i, j] > ans) ans = downLeftEnd[i, j];

                // V-shaped: down-right then turn to down-left
                int len1 = downRightEnd[i, j] + downLeftStart[i, j] - 1;
                if (len1 > ans) ans = len1;

                // V-shaped: down-left then turn to down-right
                int len2 = downLeftEnd[i, j] + downRightStart[i, j] - 1;
                if (len2 > ans) ans = len2;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var lenOfVDiagonal = function(grid) {
    const n = grid.length;
    const m = grid[0].length;
    // dp[dir][i][j] : max length of consecutive non‑zero cells starting at (i,j) moving in direction dir
    // directions: 0 NE (-1,+1), 1 SE (+1,+1), 2 SW (+1,-1), 3 NW (-1,-1)
    const dp = Array.from({length: 4}, () => Array.from({length: n}, () => Array(m).fill(0)));
    
    // NE
    for (let i = 0; i < n; ++i) {
        for (let j = m - 1; j >= 0; --j) {
            if (grid[i][j] !== 0) {
                const ni = i - 1, nj = j + 1;
                dp[0][i][j] = 1 + ((ni >= 0 && nj < m) ? dp[0][ni][nj] : 0);
            }
        }
    }
    // SE
    for (let i = n - 1; i >= 0; --i) {
        for (let j = m - 1; j >= 0; --j) {
            if (grid[i][j] !== 0) {
                const ni = i + 1, nj = j + 1;
                dp[1][i][j] = 1 + ((ni < n && nj < m) ? dp[1][ni][nj] : 0);
            }
        }
    }
    // SW
    for (let i = n - 1; i >= 0; --i) {
        for (let j = 0; j < m; ++j) {
            if (grid[i][j] !== 0) {
                const ni = i + 1, nj = j - 1;
                dp[2][i][j] = 1 + ((ni < n && nj >= 0) ? dp[2][ni][nj] : 0);
            }
        }
    }
    // NW
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            if (grid[i][j] !== 0) {
                const ni = i - 1, nj = j - 1;
                dp[3][i][j] = 1 + ((ni >= 0 && nj >= 0) ? dp[3][ni][nj] : 0);
            }
        }
    }
    
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            if (grid[i][j] === 0) continue;
            for (let d = 0; d < 4; ++d) {
                // straight diagonal
                if (dp[d][i][j] > ans) ans = dp[d][i][j];
                // V‑shaped: incoming direction is d, turn clockwise to (d+1)%4
                const lenIncoming = dp[(d + 2) % 4][i][j];   // opposite of d
                const lenAfterTurn = dp[(d + 1) % 4][i][j];
                const total = lenIncoming + lenAfterTurn - 1; // pivot counted twice
                if (total > ans) ans = total;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
I’m sorry, but I don’t have enough information about the exact rules for a “V‑shaped diagonal segment” in this problem to provide a correct implementation.
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function lenOfVDiagonal($grid) {
        $n = count($grid);
        if ($n == 0) return 0;
        $m = count($grid[0]);

        // directions: up-left, up-right, down-left, down-right
        $dr = [-1, -1, 1, 1];
        $dc = [-1, 1, -1, 1];

        // dp[dir][i][j]
        $dp = [];
        for ($d = 0; $d < 4; $d++) {
            $dp[$d] = array_fill(0, $n, array_fill(0, $m, 0));
        }

        // up-left
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                if ($grid[$i][$j] != 0) {
                    $prev = ($i > 0 && $j > 0) ? $dp[0][$i-1][$j-1] : 0;
                    $dp[0][$i][$j] = $prev + 1;
                }
            }
        }

        // up-right
        for ($i = 0; $i < $n; $i++) {
            for ($j = $m - 1; $j >= 0; $j--) {
                if ($grid[$i][$j] != 0) {
                    $prev = ($i > 0 && $j + 1 < $m) ? $dp[1][$i-1][$j+1] : 0;
                    $dp[1][$i][$j] = $prev + 1;
                }
            }
        }

        // down-left
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = 0; $j < $m; $j++) {
                if ($grid[$i][$j] != 0) {
                    $prev = ($i + 1 < $n && $j > 0) ? $dp[2][$i+1][$j-1] : 0;
                    $dp[2][$i][$j] = $prev + 1;
                }
            }
        }

        // down-right
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $m - 1; $j >= 0; $j--) {
                if ($grid[$i][$j] != 0) {
                    $prev = ($i + 1 < $n && $j + 1 < $m) ? $dp[3][$i+1][$j+1] : 0;
                    $dp[3][$i][$j] = $prev + 1;
                }
            }
        }

        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                if ($grid[$i][$j] == 0) continue;

                // single leg
                for ($d = 0; $d < 4; $d++) {
                    if ($dp[$d][$i][$j] > $ans) $ans = $dp[$d][$i][$j];
                }

                // combine two orthogonal legs
                for ($d1 = 0; $d1 < 4; $d1++) {
                    for ($d2 = $d1 + 1; $d2 < 4; $d2++) {
                        if ($dr[$d1] * $dr[$d2] + $dc[$d1] * $dc[$d2] == 0) {
                            $len = $dp[$d1][$i][$j] + $dp[$d2][$i][$j] - 1;
                            if ($len > $ans) $ans = $len;
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
    func lenOfVDiagonal(_ grid: [[Int]]) -> Int {
        let n = grid.count
        guard n > 0 else { return 0 }
        let m = grid[0].count
        
        // DP arrays
        var endDR = Array(repeating: Array(repeating: 1, count: m), count: n)
        var endDL = Array(repeating: Array(repeating: 1, count: m), count: n)
        var endUR = Array(repeating: Array(repeating: 1, count: m), count: n)
        var endUL = Array(repeating: Array(repeating: 1, count: m), count: n)
        
        var startDR = Array(repeating: Array(repeating: 1, count: m), count: n)
        var startDL = Array(repeating: Array(repeating: 1, count: m), count: n)
        var startUR = Array(repeating: Array(repeating: 1, count: m), count: n)
        var startUL = Array(repeating: Array(repeating: 1, count: m), count: n)
        
        // endDR (down-right) - previous cell up-left
        for i in 0..<n {
            for j in 0..<m {
                if i > 0 && j > 0 {
                    endDR[i][j] = endDR[i-1][j-1] + 1
                }
            }
        }
        // endDL (down-left) - previous cell up-right
        for i in 0..<n {
            for j in stride(from: m-1, through: 0, by: -1) {
                if i > 0 && j + 1 < m {
                    endDL[i][j] = endDL[i-1][j+1] + 1
                }
            }
        }
        // endUR (up-right) - previous cell down-left
        for i in stride(from: n-1, through: 0, by: -1) {
            for j in 0..<m {
                if i + 1 < n && j > 0 {
                    endUR[i][j] = endUR[i+1][j-1] + 1
                }
            }
        }
        // endUL (up-left) - previous cell down-right
        for i in stride(from: n-1, through: 0, by: -1) {
            for j in stride(from: m-1, through: 0, by: -1) {
                if i + 1 < n && j + 1 < m {
                    endUL[i][j] = endUL[i+1][j+1] + 1
                }
            }
        }
        
        // startDR (down-right) - next cell down-right
        for i in stride(from: n-1, through: 0, by: -1) {
            for j in stride(from: m-1, through: 0, by: -1) {
                if i + 1 < n && j + 1 < m {
                    startDR[i][j] = startDR[i+1][j+1] + 1
                }
            }
        }
        // startDL (down-left) - next cell down-left
        for i in stride(from: n-1, through: 0, by: -1) {
            for j in 0..<m {
                if i + 1 < n && j > 0 {
                    startDL[i][j] = startDL[i+1][j-1] + 1
                }
            }
        }
        // startUR (up-right) - next cell up-right
        for i in 0..<n {
            for j in stride(from: m-1, through: 0, by: -1) {
                if i > 0 && j + 1 < m {
                    startUR[i][j] = startUR[i-1][j+1] + 1
                }
            }
        }
        // startUL (up-left) - next cell up-left
        for i in 0..<n {
            for j in 0..<m {
                if i > 0 && j > 0 {
                    startUL[i][j] = startUL[i-1][j-1] + 1
                }
            }
        }
        
        var answer = 1
        
        // consider straight diagonals
        for i in 0..<n {
            for j in 0..<m {
                answer = max(answer, endDR[i][j])
                answer = max(answer, endDL[i][j])
                answer = max(answer, endUR[i][j])
                answer = max(answer, endUL[i][j])
            }
        }
        
        // consider V-shaped (with clockwise turn)
        for i in 0..<n {
            for j in 0..<m {
                // DR -> DL
                let v1 = endDR[i][j] + startDL[i][j] - 1
                answer = max(answer, v1)
                // DL -> UL
                let v2 = endDL[i][j] + startUL[i][j] - 1
                answer = max(answer, v2)
                // UL -> UR
                let v3 = endUL[i][j] + startUR[i][j] - 1
                answer = max(answer, v3)
                // UR -> DR
                let v4 = endUR[i][j] + startDR[i][j] - 1
                answer = max(answer, v4)
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lenOfVDiagonal(grid: Array<IntArray>): Int {
        val n = grid.size
        val m = grid[0].size

        // Directions for the two diagonal orientations
        val dirs1 = arrayOf(intArrayOf(1, 1), intArrayOf(-1, -1)) // down-right / up-left
        val dirs2 = arrayOf(intArrayOf(1, -1), intArrayOf(-1, 1)) // down-left / up-right

        // dp1[i][j] = longest consecutive segment ending at (i,j) in direction (1,1)
        // dp2[i][j] = longest consecutive segment ending at (i,j) in direction (1,-1)
        val dpDR = Array(n) { IntArray(m) } // down-right
        val dpDL = Array(n) { IntArray(m) } // down-left

        // Fill dp for down-right direction
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (i > 0 && j > 0) dpDR[i][j] = dpDR[i - 1][j - 1] + 1 else dpDR[i][j] = 1
            }
        }

        // Fill dp for down-left direction
        for (i in 0 until n) {
            for (j in m - 1 downTo 0) {
                if (i > 0 && j + 1 < m) dpDL[i][j] = dpDL[i - 1][j + 1] + 1 else dpDL[i][j] = 1
            }
        }

        var ans = 0

        // Straight diagonal segments (no turn)
        for (i in 0 until n) {
            for (j in 0 until m) {
                ans = maxOf(ans, dpDR[i][j])
                ans = maxOf(ans, dpDL[i][j])
            }
        }

        // Consider each cell as the turning point
        for (i in 0 until n) {
            for (j in 0 until m) {
                // turn from down-right to down-left
                val len1 = dpDR[i][j]          // length of segment ending at (i,j) coming from up-left
                var x = i + 1
                var y = j - 1
                var len2 = 0
                while (x < n && y >= 0) {
                    len2++
                    x++; y--
                }
                if (len1 > 0 && len2 > 0) {
                    ans = maxOf(ans, len1 + len2)
                }

                // turn from down-left to down-right
                val len3 = dpDL[i][j]          // length of segment ending at (i,j) coming from up-right
                x = i + 1
                y = j + 1
                var len4 = 0
                while (x < n && y < m) {
                    len4++
                    x++; y++
                }
                if (len3 > 0 && len4 > 0) {
                    ans = maxOf(ans, len3 + len4)
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
  int lenOfVDiagonal(List<List<int>> grid) {
    int n = grid.length;
    int m = grid[0].length;

    List<List<int>> upLeft = List.generate(n, (_) => List.filled(m, 1));
    List<List<int>> downLeft = List.generate(n, (_) => List.filled(m, 1));
    List<List<int>> upRight = List.generate(n, (_) => List.filled(m, 1));
    List<List<int>> downRight = List.generate(n, (_) => List.filled(m, 1));

    // up-left and up-right
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        if (i > 0 && j > 0) {
          upLeft[i][j] = upLeft[i - 1][j - 1] + 1;
        }
        if (i > 0 && j + 1 < m) {
          upRight[i][j] = upRight[i - 1][j + 1] + 1;
        }
      }
    }

    // down-left and down-right
    for (int i = n - 1; i >= 0; --i) {
      for (int j = 0; j < m; ++j) {
        if (i + 1 < n && j > 0) {
          downLeft[i][j] = downLeft[i + 1][j - 1] + 1;
        }
        if (i + 1 < n && j + 1 < m) {
          downRight[i][j] = downRight[i + 1][j + 1] + 1;
        }
      }
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        int a = upLeft[i][j] + downLeft[i][j] - 1;     // SE -> SW
        int b = upRight[i][j] + downRight[i][j] - 1;   // (unused orientation)
        int c = upLeft[i][j] + upRight[i][j] - 1;      // SW -> NW
        int d = upLeft[i][j] + downRight[i][j] - 1;    // straight NW-SE diagonal
        int e = upRight[i][j] + downLeft[i][j] - 1;    // straight NE-SW diagonal

        if (a > ans) ans = a;
        if (b > ans) ans = b;
        if (c > ans) ans = c;
        if (d > ans) ans = d;
        if (e > ans) ans = e;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func lenOfVDiagonal(grid [][]int) int {
    n := len(grid)
    m := len(grid[0])

    drStart := make([][]int, n)
    dlStart := make([][]int, n)
    ulStart := make([][]int, n)
    urStart := make([][]int, n)
    for i := 0; i < n; i++ {
        drStart[i] = make([]int, m)
        dlStart[i] = make([]int, m)
        ulStart[i] = make([]int, m)
        urStart[i] = make([]int, m)
    }

    // down‑right and down‑left starting lengths
    for i := n - 1; i >= 0; i-- {
        for j := m - 1; j >= 0; j-- {
            drStart[i][j] = 1
            if i+1 < n && j+1 < m {
                drStart[i][j] = drStart[i+1][j+1] + 1
            }
            dlStart[i][j] = 1
            if i+1 < n && j-1 >= 0 {
                dlStart[i][j] = dlStart[i+1][j-1] + 1
            }
        }
    }

    // up‑left and up‑right starting lengths
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            ulStart[i][j] = 1
            if i-1 >= 0 && j-1 >= 0 {
                ulStart[i][j] = ulStart[i-1][j-1] + 1
            }
            urStart[i][j] = 1
            if i-1 >= 0 && j+1 < m {
                urStart[i][j] = urStart[i-1][j+1] + 1
            }
        }
    }

    maxLen := 0

    // longest straight diagonal segment
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if drStart[i][j] > maxLen {
                maxLen = drStart[i][j]
            }
            if dlStart[i][j] > maxLen {
                maxLen = dlStart[i][j]
            }
            if ulStart[i][j] > maxLen {
                maxLen = ulStart[i][j]
            }
            if urStart[i][j] > maxLen {
                maxLen = urStart[i][j]
            }
        }
    }

    // V‑shaped segments (clockwise turn)
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            // DR -> DL
            cand := ulStart[i][j] + dlStart[i][j] - 1
            if cand > maxLen {
                maxLen = cand
            }
            // DL -> UL
            cand = urStart[i][j] + ulStart[i][j] - 1
            if cand > maxLen {
                maxLen = cand
            }
            // UL -> UR
            cand = drStart[i][j] + urStart[i][j] - 1
            if cand > maxLen {
                maxLen = cand
            }
            // UR -> DR
            cand = dlStart[i][j] + drStart[i][j] - 1
            if cand > maxLen {
                maxLen = cand
            }
        }
    }

    return maxLen
}
```

## Ruby

```ruby
def len_of_v_diagonal(grid)
  n = grid.size
  m = grid[0].size

  ul = Array.new(n) { Array.new(m, 1) }
  ur = Array.new(n) { Array.new(m, 1) }
  dl = Array.new(n) { Array.new(m, 1) }
  dr = Array.new(n) { Array.new(m, 1) }

  # up-left and up-right
  (0...n).each do |i|
    (0...m).each do |j|
      if i > 0 && j > 0
        ul[i][j] = ul[i - 1][j - 1] + 1
      end
      if i > 0 && j + 1 < m
        ur[i][j] = ur[i - 1][j + 1] + 1
      end
    end
  end

  # down-left and down-right
  (n - 1).downto(0) do |i|
    (m - 1).downto(0) do |j|
      if i + 1 < n && j > 0
        dl[i][j] = dl[i + 1][j - 1] + 1
      end
      if i + 1 < n && j + 1 < m
        dr[i][j] = dr[i + 1][j + 1] + 1
      end
    end
  end

  max_len = 0
  (0...n).each do |i|
    (0...m).each do |j|
      # UL & UR (upward V)
      len = ul[i][j] + ur[i][j] - 1
      max_len = len if len > max_len

      # DL & DR (downward V)
      len = dl[i][j] + dr[i][j] - 1
      max_len = len if len > max_len

      # UL & DL (leftward V)
      len = ul[i][j] + dl[i][j] - 1
      max_len = len if len > max_len

      # UR & DR (rightward V)
      len = ur[i][j] + dr[i][j] - 1
      max_len = len if len > max_len
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def lenOfVDiagonal(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        if (n == 0) return 0
        val m = grid(0).length

        val ul = Array.ofDim[Int](n, m)
        val ur = Array.ofDim[Int](n, m)
        val dl = Array.ofDim[Int](n, m)
        val dr = Array.ofDim[Int](n, m)

        // up-left and up-right lengths
        var i = 0
        while (i < n) {
            var j = 0
            while (j < m) {
                ul(i)(j) = if (i > 0 && j > 0) ul(i - 1)(j - 1) + 1 else 1
                ur(i)(j) = if (i > 0 && j + 1 < m) ur(i - 1)(j + 1) + 1 else 1
                j += 1
            }
            i += 1
        }

        // down-left and down-right lengths
        i = n - 1
        while (i >= 0) {
            var j = 0
            while (j < m) {
                dl(i)(j) = if (i + 1 < n && j > 0) dl(i + 1)(j - 1) + 1 else 1
                dr(i)(j) = if (i + 1 < n && j + 1 < m) dr(i + 1)(j + 1) + 1 else 1
                j += 1
            }
            i -= 1
        }

        var ans = 0
        i = 0
        while (i < n) {
            var j = 0
            while (j < m) {
                val v1 = ul(i)(j) + dl(i)(j) - 1
                if (v1 > ans) ans = v1
                val v2 = ur(i)(j) + dr(i)(j) - 1
                if (v2 > ans) ans = v2
                j += 1
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
    pub fn len_of_v_diagonal(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let m = grid[0].len();
        let mut ans = 1i32;
        for i in 0..n {
            for j in 0..m {
                let i_i = i as i32;
                let j_j = j as i32;
                let n_i = (n - 1 - i) as i32;
                let m_j = (m - 1 - j) as i32;

                let ul = std::cmp::min(i_i, j_j);
                let ur = std::cmp::min(i_i, m_j);
                let dr = std::cmp::min(n_i, m_j);
                let dl = std::cmp::min(n_i, j_j);

                // d1 = up-left -> d2 = up-right
                let t1 = 1 + dr + ur;
                if t1 > ans { ans = t1; }
                // d1 = up-right -> d2 = down-right
                let t2 = 1 + dl + dr;
                if t2 > ans { ans = t2; }
                // d1 = down-right -> d2 = down-left
                let t3 = 1 + ul + dl;
                if t3 > ans { ans = t3; }
                // d1 = down-left -> d2 = up-left
                let t4 = 1 + ur + ul;
                if t4 > ans { ans = t4; }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (len-of-v-diagonal grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (m (if (= n 0) 0 (length (first grid))))
         (g (list->vector (map list->vector grid)))
         (dp-se (make-vector n))
         (len-sw (make-vector n)))
    ;; initialize vectors of vectors
    (for ([i (in-range n)])
      (vector-set! dp-se i (make-vector m 0))
      (vector-set! len-sw i (make-vector m 0)))
    ;; compute longest alternating SE chains ending at each cell
    (for ([i (in-range n)])
      (for ([j (in-range m)])
        (let* ((val (vector-ref (vector-ref g i) j))
               (prev (if (and (> i 0) (> j 0)
                              (not (= val (vector-ref (vector-ref g (- i 1)) (- j 1)))))
                         (+ 1 (vector-ref (vector-ref dp-se (- i 1)) (- j 1)))
                         1)))
          (vector-set! (vector-ref dp-se i) j prev))))
    ;; compute longest alternating SW chains starting from each cell
    (for ([i (in-range (sub1 n) -1 -1)])
      (for ([j (in-range m)])
        (let* ((val (vector-ref (vector-ref g i) j))
               (next (if (and (< (+ i 1) n) (> j 0)
                              (not (= val (vector-ref (vector-ref g (+ i 1)) (- j 1)))))
                         (+ 1 (vector-ref (vector-ref len-sw (+ i 1)) (- j 1)))
                         1)))
          (vector-set! (vector-ref len-sw i) j next))))
    ;; evaluate maximum V-shaped length
    (let ((ans 0))
      (for ([i (in-range n)])
        (for ([j (in-range m)])
          (let* ((a (vector-ref (vector-ref dp-se i) j))
                 (b (vector-ref (vector-ref len-sw i) j))
                 (total (+ a b -1)))
            (when (> total ans)
              (set! ans total)))))
      ans)))
```

## Erlang

```erlang
-spec len_of_v_diagonal(Grid :: [[integer()]]) -> integer().
len_of_v_diagonal(Grid) ->
    N = length(Grid),
    M = case Grid of [] -> 0; [Row|_] -> length(Row) end,
    MaxLen = lists:foldl(
        fun(I, AccI) ->
            Row = lists:nth(I + 1, Grid),
            lists:foldl(
                fun(J, AccJ) ->
                    UL = min(I, J) + 1,
                    UR = min(I, M - J - 1) + 1,
                    DL = min(N - I - 1, J) + 1,
                    DR = min(N - I - 1, M - J - 1) + 1,
                    Straight = max(max(UL, UR), max(DL, DR)),
                    V1 = UL + DL - 1,
                    V2 = UR + UL - 1,
                    V3 = DR + UR - 1,
                    V4 = DL + DR - 1,
                    MaxLocal = lists:max([Straight, V1, V2, V3, V4]),
                    max(AccJ, MaxLocal)
                end,
                AccI,
                lists:seq(0, M - 1)
            )
        end,
        0,
        lists:seq(0, N - 1)
    ),
    MaxLen.
```

## Elixir

```elixir
defmodule Solution do
  @spec len_of_v_diagonal(grid :: [[integer]]) :: integer
  def len_of_v_diagonal(grid) do
    n = length(grid)
    m = if n == 0, do: 0, else: grid |> hd() |> length()

    max_len = 
      Enum.reduce(0..(n-1), 0, fn i, acc ->
        Enum.reduce(0..(m-1), acc, fn j, inner_acc ->
          dr = min(n - i, m - j)
          dl = min(n - i, j + 1)
          ul = min(i + 1, j + 1)
          ur = min(i + 1, m - j)

          single_max = Enum.max([dr, dl, ul, ur])
          v1 = dr + dl - 1
          v2 = dl + ul - 1
          v3 = ul + ur - 1
          v4 = ur + dr - 1

          Enum.max([inner_acc, single_max, v1, v2, v3, v4])
        end)
      end)

    max_len
  end
end
```

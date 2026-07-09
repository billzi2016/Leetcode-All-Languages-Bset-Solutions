# 2132. Stamping the Grid

## Cpp

```cpp
class Solution {
public:
    bool possibleToStamp(vector<vector<int>>& grid, int stampHeight, int stampWidth) {
        int m = grid.size();
        int n = grid[0].size();
        // prefix sum of occupied cells
        vector<vector<int>> pref(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i < m; ++i) {
            int rowSum = 0;
            for (int j = 0; j < n; ++j) {
                rowSum += grid[i][j];
                pref[i + 1][j + 1] = pref[i][j + 1] + rowSum;
            }
        }
        auto getSum = [&](int r1, int c1, int r2, int c2) -> int {
            // sum over [r1, r2) x [c1, c2)
            return pref[r2][c2] - pref[r1][c2] - pref[r2][c1] + pref[r1][c1];
        };
        vector<vector<int>> diff(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i + stampHeight <= m; ++i) {
            for (int j = 0; j + stampWidth <= n; ++j) {
                if (getSum(i, j, i + stampHeight, j + stampWidth) == 0) {
                    diff[i][j] += 1;
                    diff[i + stampHeight][j] -= 1;
                    diff[i][j + stampWidth] -= 1;
                    diff[i + stampHeight][j + stampWidth] += 1;
                }
            }
        }
        // compute coverage and verify
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int val = diff[i][j];
                if (i > 0) val += diff[i - 1][j];
                if (j > 0) val += diff[i][j - 1];
                if (i > 0 && j > 0) val -= diff[i - 1][j - 1];
                diff[i][j] = val;
                if (grid[i][j] == 0 && diff[i][j] <= 0) return false;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean possibleToStamp(int[][] grid, int stampHeight, int stampWidth) {
        int m = grid.length;
        int n = grid[0].length;

        // Prefix sum of occupied cells
        int[][] pre = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            int rowSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += grid[i][j];
                pre[i + 1][j + 1] = pre[i][j + 1] + rowSum;
            }
        }

        // Difference array to mark stamp coverage
        int[][] diff = new int[m + 1][n + 1];

        for (int i = 0; i + stampHeight <= m; i++) {
            for (int j = 0; j + stampWidth <= n; j++) {
                int r2 = i + stampHeight;
                int c2 = j + stampWidth;
                int occupied = pre[r2][c2] - pre[i][c2] - pre[r2][j] + pre[i][j];
                if (occupied == 0) { // can place a stamp here
                    diff[i][j] += 1;
                    diff[r2][j] -= 1;
                    diff[i][c2] -= 1;
                    diff[r2][c2] += 1;
                }
            }
        }

        // Convert difference array to actual coverage counts via prefix sum
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = diff[i][j];
                if (i > 0) val += diff[i - 1][j];
                if (j > 0) val += diff[i][j - 1];
                if (i > 0 && j > 0) val -= diff[i - 1][j - 1];
                diff[i][j] = val;
            }
        }

        // Verify every empty cell is covered by at least one stamp
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && diff[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        if stampHeight > m or stampWidth > n:
            # cannot place any stamp, so any zero makes it impossible
            for row in grid:
                if 0 in row:
                    return False
            return True

        # prefix sum of occupied cells
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            gi = grid[i]
            psi = ps[i + 1]
            psi_prev = ps[i]
            for j in range(n):
                row_sum += gi[j]
                psi[j + 1] = psi_prev[j + 1] + row_sum

        # difference array for coverage counts
        diff = [[0] * (n + 1) for _ in range(m + 1)]

        max_i = m - stampHeight
        max_j = n - stampWidth
        for i in range(max_i + 1):
            pi = ps[i]
            pi_h = ps[i + stampHeight]
            for j in range(max_j + 1):
                # sum of rectangle (i,j) to (i+stampHeight-1, j+stampWidth-1)
                total = pi_h[j + stampWidth] - pi[j + stampWidth] - pi_h[j] + pi[j]
                if total == 0:
                    diff[i][j] += 1
                    diff[i + stampHeight][j] -= 1
                    diff[i][j + stampWidth] -= 1
                    diff[i + stampHeight][j + stampWidth] += 1

        # compute coverage from difference array
        for i in range(m):
            for j in range(n):
                val = diff[i][j]
                if i > 0:
                    val += diff[i - 1][j]
                if j > 0:
                    val += diff[i][j - 1]
                if i > 0 and j > 0:
                    val -= diff[i - 1][j - 1]
                diff[i][j] = val

        # verify every empty cell is covered
        for i in range(m):
            gi = grid[i]
            di = diff[i]
            for j in range(n):
                if gi[j] == 0 and di[j] <= 0:
                    return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        if stampHeight > m or stampWidth > n:
            # no stamp can be placed; all cells must already be occupied
            for row in grid:
                for val in row:
                    if val == 0:
                        return False
            return True

        # prefix sum of occupied cells
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                pref[i + 1][j + 1] = pref[i][j + 1] + row_sum

        # difference array for stamp coverage
        diff = [[0] * (n + 1) for _ in range(m + 1)]

        max_i = m - stampHeight
        max_j = n - stampWidth
        for i in range(max_i + 1):
            i2 = i + stampHeight
            pref_i = pref[i]
            pref_i2 = pref[i2]
            for j in range(max_j + 1):
                j2 = j + stampWidth
                # occupied cells in the candidate rectangle
                occ = pref_i2[j2] - pref_i[j2] - pref_i2[j] + pref_i[j]
                if occ == 0:
                    diff[i][j] += 1
                    diff[i2][j] -= 1
                    diff[i][j2] -= 1
                    diff[i2][j2] += 1

        # accumulate difference array and verify coverage
        for i in range(m):
            for j in range(n):
                val = diff[i][j]
                if i > 0:
                    val += diff[i - 1][j]
                if j > 0:
                    val += diff[i][j - 1]
                if i > 0 and j > 0:
                    val -= diff[i - 1][j - 1]
                diff[i][j] = val
                if grid[i][j] == 0 and val == 0:
                    return False
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

bool possibleToStamp(int** grid, int gridSize, int* gridColSize, int stampHeight, int stampWidth) {
    int m = gridSize;
    int n = gridColSize[0];
    int rows = m + 1;
    int cols = n + 1;

    // Prefix sum of the original grid
    int *pref = (int *)calloc(rows * cols, sizeof(int));
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            pref[i * cols + j] = grid[i - 1][j - 1]
                               + pref[(i - 1) * cols + j]
                               + pref[i * cols + (j - 1)]
                               - pref[(i - 1) * cols + (j - 1)];
        }
    }

    // Difference array for stamp coverage
    int *diff = (int *)calloc(rows * cols, sizeof(int));
    for (int i = 0; i + stampHeight <= m; ++i) {
        for (int j = 0; j + stampWidth <= n; ++j) {
            int sum = pref[(i + stampHeight) * cols + (j + stampWidth)]
                    - pref[i * cols + (j + stampWidth)]
                    - pref[(i + stampHeight) * cols + j]
                    + pref[i * cols + j];
            if (sum == 0) { // all cells are empty, we can place a stamp here
                diff[i * cols + j] += 1;
                diff[(i + stampHeight) * cols + j] -= 1;
                diff[i * cols + (j + stampWidth)] -= 1;
                diff[(i + stampHeight) * cols + (j + stampWidth)] += 1;
            }
        }
    }

    // Convert difference array to actual coverage counts
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int idx = i * cols + j;
            int val = diff[idx];
            if (i > 0) val += diff[(i - 1) * cols + j];
            if (j > 0) val += diff[i * cols + (j - 1)];
            if (i > 0 && j > 0) val -= diff[(i - 1) * cols + (j - 1)];
            diff[idx] = val;
        }
    }

    // Verify every empty cell is covered by at least one stamp
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 0 && diff[i * cols + j] <= 0) {
                free(pref);
                free(diff);
                return false;
            }
        }
    }

    free(pref);
    free(diff);
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool PossibleToStamp(int[][] grid, int stampHeight, int stampWidth) {
        int m = grid.Length;
        int n = grid[0].Length;

        // Prefix sum of occupied cells
        int[,] pref = new int[m + 1, n + 1];
        for (int i = 0; i < m; i++) {
            int rowSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += grid[i][j];
                pref[i + 1, j + 1] = pref[i, j + 1] + rowSum;
            }
        }

        // Difference array to mark stamp coverage
        int[,] diff = new int[m + 1, n + 1];

        for (int i = 0; i <= m - stampHeight; i++) {
            for (int j = 0; j <= n - stampWidth; j++) {
                int i2 = i + stampHeight;
                int j2 = j + stampWidth;
                int occupied = pref[i2, j2] - pref[i, j2] - pref[i2, j] + pref[i, j];
                if (occupied == 0) {
                    diff[i, j] += 1;
                    diff[i2, j] -= 1;
                    diff[i, j2] -= 1;
                    diff[i2, j2] += 1;
                }
            }
        }

        // Compute coverage and verify each empty cell is covered
        int[,] cover = new int[m, n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = diff[i, j];
                if (i > 0) val += cover[i - 1, j];
                if (j > 0) val += cover[i, j - 1];
                if (i > 0 && j > 0) val -= cover[i - 1, j - 1];
                cover[i, j] = val;
                if (grid[i][j] == 0 && val == 0) return false;
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} stampHeight
 * @param {number} stampWidth
 * @return {boolean}
 */
var possibleToStamp = function(grid, stampHeight, stampWidth) {
    const m = grid.length;
    const n = grid[0].length;

    // prefix sum of occupied cells
    const ps = Array.from({ length: m + 1 }, () => new Int32Array(n + 1));
    for (let i = 0; i < m; ++i) {
        let rowSum = 0;
        for (let j = 0; j < n; ++j) {
            rowSum += grid[i][j];
            ps[i + 1][j + 1] = ps[i][j + 1] + rowSum;
        }
    }

    // difference array for stamp coverage
    const diff = Array.from({ length: m + 1 }, () => new Int32Array(n + 1));

    const maxI = m - stampHeight;
    const maxJ = n - stampWidth;

    for (let i = 0; i <= maxI; ++i) {
        for (let j = 0; j <= maxJ; ++j) {
            const r2 = i + stampHeight;
            const c2 = j + stampWidth;
            const occupied = ps[r2][c2] - ps[i][c2] - ps[r2][j] + ps[i][j];
            if (occupied === 0) {
                diff[i][j] += 1;
                diff[i][c2] -= 1;
                diff[r2][j] -= 1;
                diff[r2][c2] += 1;
            }
        }
    }

    // convert diff to actual coverage counts via prefix sums
    for (let i = 0; i <= m; ++i) {
        for (let j = 1; j <= n; ++j) {
            diff[i][j] += diff[i][j - 1];
        }
    }
    for (let i = 1; i <= m; ++i) {
        for (let j = 0; j <= n; ++j) {
            diff[i][j] += diff[i - 1][j];
        }
    }

    // verify every empty cell is covered
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 0 && diff[i][j] <= 0) return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function possibleToStamp(grid: number[][], stampHeight: number, stampWidth: number): boolean {
    const m = grid.length;
    const n = grid[0].length;

    // Prefix sum of the original grid
    const ps: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; i++) {
        const row = grid[i];
        const cur = ps[i + 1];
        const prev = ps[i];
        for (let j = 0; j < n; j++) {
            cur[j + 1] = row[j] + prev[j + 1] + cur[j] - prev[j];
        }
    }

    // Difference array to mark coverage of all possible stamps
    const diff: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

    for (let i = 0; i <= m - stampHeight; i++) {
        for (let j = 0; j <= n - stampWidth; j++) {
            const total =
                ps[i + stampHeight][j + stampWidth] -
                ps[i][j + stampWidth] -
                ps[i + stampHeight][j] +
                ps[i][j];
            if (total === 0) {
                diff[i][j] += 1;
                diff[i + stampHeight][j] -= 1;
                diff[i][j + stampWidth] -= 1;
                diff[i + stampHeight][j + stampWidth] += 1;
            }
        }
    }

    // Reconstruct coverage from difference array and validate each empty cell
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let val = diff[i][j];
            if (i > 0) val += diff[i - 1][j];
            if (j > 0) val += diff[i][j - 1];
            if (i > 0 && j > 0) val -= diff[i - 1][j - 1];
            diff[i][j] = val;
            if (grid[i][j] === 0 && val === 0) {
                return false;
            }
        }
    }

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $stampHeight
     * @param Integer $stampWidth
     * @return Boolean
     */
    function possibleToStamp($grid, $stampHeight, $stampWidth) {
        $m = count($grid);
        $n = count($grid[0]);

        // prefix sum of occupied cells (1s)
        $pref = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $pref[$i + 1][$j + 1] = $grid[$i][$j]
                    + $pref[$i][$j + 1]
                    + $pref[$i + 1][$j]
                    - $pref[$i][$j];
            }
        }

        // difference array for coverage
        $diff = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));

        $maxI = $m - $stampHeight;
        $maxJ = $n - $stampWidth;
        if ($maxI >= 0 && $maxJ >= 0) {
            for ($i = 0; $i <= $maxI; ++$i) {
                $x2 = $i + $stampHeight;
                for ($j = 0; $j <= $maxJ; ++$j) {
                    $y2 = $j + $stampWidth;
                    // sum of occupied cells in the rectangle
                    $sum = $pref[$x2][$y2] - $pref[$i][$y2] - $pref[$x2][$j] + $pref[$i][$j];
                    if ($sum === 0) {
                        $diff[$i][$j] += 1;
                        $diff[$x2][$j] -= 1;
                        $diff[$i][$y2] -= 1;
                        $diff[$x2][$y2] += 1;
                    }
                }
            }
        }

        // compute coverage and validate
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($i > 0) $diff[$i][$j] += $diff[$i - 1][$j];
                if ($j > 0) $diff[$i][$j] += $diff[$i][$j - 1];
                if ($i > 0 && $j > 0) $diff[$i][$j] -= $diff[$i - 1][$j - 1];

                if ($grid[$i][$j] === 0 && $diff[$i][$j] <= 0) {
                    return false;
                }
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func possibleToStamp(_ grid: [[Int]], _ stampHeight: Int, _ stampWidth: Int) -> Bool {
        let m = grid.count
        guard m > 0 else { return true }
        let n = grid[0].count
        
        // If the stamp cannot fit at all, only succeed when there are no empty cells.
        if stampHeight > m || stampWidth > n {
            for row in grid {
                for cell in row where cell == 0 {
                    return false
                }
            }
            return true
        }
        
        // Prefix sum of occupied cells (1s)
        var pref = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for i in 0..<m {
            var rowSum = 0
            for j in 0..<n {
                rowSum += grid[i][j]
                pref[i + 1][j + 1] = pref[i][j + 1] + rowSum
            }
        }
        
        // Difference array to mark coverage of stamps
        var diff = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        let maxI = m - stampHeight
        let maxJ = n - stampWidth
        
        if maxI >= 0 && maxJ >= 0 {
            for i in 0...maxI {
                for j in 0...maxJ {
                    let ones = pref[i + stampHeight][j + stampWidth] - pref[i][j + stampWidth] -
                               pref[i + stampHeight][j] + pref[i][j]
                    if ones == 0 {
                        diff[i][j] += 1
                        diff[i + stampHeight][j] -= 1
                        diff[i][j + stampWidth] -= 1
                        diff[i + stampHeight][j + stampWidth] += 1
                    }
                }
            }
        }
        
        // Convert difference array to actual coverage counts (2D prefix sum)
        for i in 0..<m {
            var running = 0
            for j in 0..<n {
                running += diff[i][j]
                diff[i][j] = running
            }
        }
        for j in 0..<n {
            var running = 0
            for i in 0..<m {
                running += diff[i][j]
                diff[i][j] = running
            }
        }
        
        // Verify every empty cell is covered by at least one stamp
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 0 && diff[i][j] == 0 {
                    return false
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun possibleToStamp(grid: Array<IntArray>, stampHeight: Int, stampWidth: Int): Boolean {
        val m = grid.size
        val n = grid[0].size

        // Prefix sum of occupied cells
        val pref = Array(m + 1) { IntArray(n + 1) }
        for (i in 0 until m) {
            var rowSum = 0
            for (j in 0 until n) {
                rowSum += grid[i][j]
                pref[i + 1][j + 1] = pref[i][j + 1] + rowSum
            }
        }

        // Difference array for stamp coverage
        val diff = Array(m + 1) { IntArray(n + 1) }

        val maxI = m - stampHeight
        val maxJ = n - stampWidth
        if (maxI >= 0 && maxJ >= 0) {
            for (i in 0..maxI) {
                for (j in 0..maxJ) {
                    val occupied = pref[i + stampHeight][j + stampWidth] -
                                   pref[i][j + stampWidth] -
                                   pref[i + stampHeight][j] +
                                   pref[i][j]
                    if (occupied == 0) {
                        diff[i][j]++
                        diff[i + stampHeight][j]--
                        diff[i][j + stampWidth]--
                        diff[i + stampHeight][j + stampWidth]++
                    }
                }
            }
        }

        // Build coverage from difference array
        for (i in 0..m) {
            for (j in 0..n) {
                if (i > 0) diff[i][j] += diff[i - 1][j]
                if (j > 0) diff[i][j] += diff[i][j - 1]
                if (i > 0 && j > 0) diff[i][j] -= diff[i - 1][j - 1]
            }
        }

        // Verify every empty cell is covered
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 0 && diff[i][j] <= 0) return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool possibleToStamp(List<List<int>> grid, int stampHeight, int stampWidth) {
    int m = grid.length;
    if (m == 0) return true;
    int n = grid[0].length;

    // Prefix sum of original grid
    List<List<int>> pref = List.generate(m + 1, (_) => List.filled(n + 1, 0));
    for (int i = 0; i < m; ++i) {
      int rowSum = 0;
      for (int j = 0; j < n; ++j) {
        rowSum += grid[i][j];
        pref[i + 1][j + 1] = pref[i][j + 1] + rowSum;
      }
    }

    // Difference array for stamp coverage
    List<List<int>> diff = List.generate(m + 1, (_) => List.filled(n + 1, 0));

    for (int i = 0; i + stampHeight <= m; ++i) {
      for (int j = 0; j + stampWidth <= n; ++j) {
        int total = pref[i + stampHeight][j + stampWidth] -
            pref[i][j + stampWidth] -
            pref[i + stampHeight][j] +
            pref[i][j];
        if (total == 0) {
          diff[i][j] += 1;
          diff[i + stampHeight][j] -= 1;
          diff[i][j + stampWidth] -= 1;
          diff[i + stampHeight][j + stampWidth] += 1;
        }
      }
    }

    // Convert difference array to actual coverage counts
    for (int i = 0; i < m; ++i) {
      int rowAcc = 0;
      for (int j = 0; j < n; ++j) {
        rowAcc += diff[i][j];
        if (i > 0) {
          diff[i][j] = diff[i - 1][j] + rowAcc;
        } else {
          diff[i][j] = rowAcc;
        }
      }
    }

    // Verify every empty cell is covered
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 0 && diff[i][j] == 0) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func possibleToStamp(grid [][]int, stampHeight int, stampWidth int) bool {
    m := len(grid)
    n := len(grid[0])

    // Prefix sum of occupied cells
    ps := make([][]int, m+1)
    for i := 0; i <= m; i++ {
        ps[i] = make([]int, n+1)
    }
    for i := 0; i < m; i++ {
        rowSum := 0
        for j := 0; j < n; j++ {
            rowSum += grid[i][j]
            ps[i+1][j+1] = ps[i][j+1] + rowSum
        }
    }

    // Difference array for stamp coverage
    diff := make([][]int, m+1)
    for i := 0; i <= m; i++ {
        diff[i] = make([]int, n+1)
    }

    // Find all valid stamp placements and mark them in diff
    for i := 0; i+stampHeight <= m; i++ {
        for j := 0; j+stampWidth <= n; j++ {
            total := ps[i+stampHeight][j+stampWidth] - ps[i][j+stampWidth] -
                ps[i+stampHeight][j] + ps[i][j]
            if total == 0 { // no occupied cells in this rectangle
                diff[i][j]++
                diff[i+stampHeight][j]--
                diff[i][j+stampWidth]--
                diff[i+stampHeight][j+stampWidth]++
            }
        }
    }

    // Convert difference array to actual coverage using 2D prefix sum
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i > 0 {
                diff[i][j] += diff[i-1][j]
            }
            if j > 0 {
                diff[i][j] += diff[i][j-1]
            }
            if i > 0 && j > 0 {
                diff[i][j] -= diff[i-1][j-1]
            }
            // If a cell is empty and not covered by any stamp, impossible
            if grid[i][j] == 0 && diff[i][j] == 0 {
                return false
            }
        }
    }

    return true
}
```

## Ruby

```ruby
def possible_to_stamp(grid, stamp_height, stamp_width)
  m = grid.length
  n = grid[0].length

  # prefix sum of original ones
  ps = Array.new(m + 1) { Array.new(n + 1, 0) }
  (0...m).each do |i|
    row_sum = 0
    (0...n).each do |j|
      row_sum += grid[i][j]
      ps[i + 1][j + 1] = ps[i][j + 1] + row_sum
    end
  end

  # difference array for coverage counts
  diff = Array.new(m + 1) { Array.new(n + 1, 0) }

  max_i = m - stamp_height
  max_j = n - stamp_width
  if max_i >= 0 && max_j >= 0
    (0..max_i).each do |i|
      (0..max_j).each do |j|
        ones = ps[i + stamp_height][j + stamp_width] -
               ps[i][j + stamp_width] -
               ps[i + stamp_height][j] +
               ps[i][j]
        next unless ones == 0

        diff[i][j] += 1
        diff[i + stamp_height][j] -= 1 if i + stamp_height <= m
        diff[i][j + stamp_width] -= 1 if j + stamp_width <= n
        if i + stamp_height <= m && j + stamp_width <= n
          diff[i + stamp_height][j + stamp_width] += 1
        end
      end
    end
  end

  # accumulate difference array to get coverage per cell
  (0...m).each do |i|
    (0...n).each do |j|
      val = diff[i][j]
      val += diff[i - 1][j] if i > 0
      val += diff[i][j - 1] if j > 0
      val -= diff[i - 1][j - 1] if i > 0 && j > 0
      diff[i][j] = val
    end
  end

  # verify every empty cell is covered
  (0...m).each do |i|
    (0...n).each do |j|
      return false if grid[i][j] == 0 && diff[i][j] <= 0
    end
  end
  true
end
```

## Scala

```scala
object Solution {
  def possibleToStamp(grid: Array[Array[Int]], stampHeight: Int, stampWidth: Int): Boolean = {
    val m = grid.length
    if (m == 0) return true
    val n = grid(0).length

    // If stamp larger than grid, only possible when there are no empty cells
    if (stampHeight > m || stampWidth > n) {
      var i = 0
      while (i < m) {
        var j = 0
        while (j < n) {
          if (grid(i)(j) == 0) return false
          j += 1
        }
        i += 1
      }
      return true
    }

    // Prefix sum of original grid to query submatrix sums quickly
    val ps = Array.ofDim[Int](m + 1, n + 1)
    var i = 0
    while (i < m) {
      var rowSum = 0
      var j = 0
      while (j < n) {
        rowSum += grid(i)(j)
        ps(i + 1)(j + 1) = ps(i)(j + 1) + rowSum
        j += 1
      }
      i += 1
    }

    // Difference array for stamp coverage
    val diff = Array.ofDim[Int](m + 1, n + 1)

    var r = 0
    while (r <= m - stampHeight) {
      var c = 0
      while (c <= n - stampWidth) {
        val total = ps(r + stampHeight)(c + stampWidth) - ps(r)(c + stampWidth) -
          ps(r + stampHeight)(c) + ps(r)(c)
        if (total == 0) {
          diff(r)(c) += 1
          diff(r + stampHeight)(c) -= 1
          diff(r)(c + stampWidth) -= 1
          diff(r + stampHeight)(c + stampWidth) += 1
        }
        c += 1
      }
      r += 1
    }

    // Convert difference array to actual coverage counts via prefix sums
    var row = 0
    while (row < m) {
      var colSum = 0
      var col = 0
      while (col < n) {
        colSum += diff(row)(col)
        if (row > 0) diff(row)(col) = diff(row - 1)(col) + colSum
        else diff(row)(col) = colSum
        col += 1
      }
      row += 1
    }

    // Verify every empty cell is covered by at least one stamp
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 0 && diff(i)(j) <= 0) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn possible_to_stamp(grid: Vec<Vec<i32>>, stamp_height: i32, stamp_width: i32) -> bool {
        let m = grid.len();
        if m == 0 {
            return true;
        }
        let n = grid[0].len();

        let h = stamp_height as usize;
        let w = stamp_width as usize;

        // Prefix sum of the original grid
        let mut pref = vec![vec![0i32; n + 1]; m + 1];
        for i in 0..m {
            let mut row_sum = 0i32;
            for j in 0..n {
                row_sum += grid[i][j];
                pref[i + 1][j + 1] = pref[i][j + 1] + row_sum;
            }
        }

        // Difference array for stamp coverage
        let mut diff = vec![vec![0i32; n + 1]; m + 1];

        if h <= m && w <= n {
            for i in 0..=m - h {
                for j in 0..=n - w {
                    // Sum of rectangle (i, j) to (i+h-1, j+w-1)
                    let sum = pref[i + h][j + w] - pref[i][j + w] - pref[i + h][j] + pref[i][j];
                    if sum == 0 {
                        diff[i][j] += 1;
                        diff[i + h][j] -= 1;
                        diff[i][j + w] -= 1;
                        diff[i + h][j + w] += 1;
                    }
                }
            }
        }

        // Convert difference array to actual coverage counts
        for i in 0..=m {
            for j in 0..=n {
                if i > 0 {
                    diff[i][j] += diff[i - 1][j];
                }
                if j > 0 {
                    diff[i][j] += diff[i][j - 1];
                }
                if i > 0 && j > 0 {
                    diff[i][j] -= diff[i - 1][j - 1];
                }
            }
        }

        // Verify every empty cell is covered by at least one stamp
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 0 && diff[i][j] <= 0 {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (possible-to-stamp grid stampHeight stampWidth)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)
  (let* ([m (length grid)]
         [n (if (= m 0) 0 (length (first grid)))]
         [grid-vec (list->vector (map list->vector grid))]
         ;; prefix sum of original grid
         [ps (make-vector (+ m 1)
               (lambda () (make-vector (+ n 1) 0)))])
    ;; build prefix sums
    (for ([i (in-range 1 (+ m 1))])
      (let ([row-ps (vector-ref ps i)]
            [prev-row-ps (vector-ref ps (- i 1))]
            [grid-row (vector-ref grid-vec (- i 1))])
        (for ([j (in-range 1 (+ n 1))])
          (define val (vector-ref grid-row (- j 1)))
          (vector-set! row-ps j
            (+ val
               (vector-ref prev-row-ps j)
               (vector-ref row-ps (- j 1))
               (- (vector-ref prev-row-ps (- j 1))))))))
    ;; diff array for imos method
    (define diff (make-vector (+ m 1)
                  (lambda () (make-vector (+ n 1) 0))))
    (define (add-diff a b delta)
      (let ([row (vector-ref diff a)])
        (vector-set! row b (+ delta (vector-ref row b)))))
    ;; place stamps where possible
    (for* ([i (in-range 0 (- m stampHeight -1))]
           [j (in-range 0 (- n stampWidth -1))])
      (let* ([x1 i] [y1 j]
             [x2 (+ i stampHeight)] [y2 (+ j stampWidth)]
             [sum
              (- (+ (vector-ref (vector-ref ps x2) y2)
                    (vector-ref (vector-ref ps x1) y1))
                 (vector-ref (vector-ref ps x1) y2)
                 (vector-ref (vector-ref ps x2) y1))])
        (when (= sum 0)
          (add-diff i j 1)
          (add-diff (+ i stampHeight) j -1)
          (add-diff i (+ j stampWidth) -1)
          (add-diff (+ i stampHeight) (+ j stampWidth) 1))))
    ;; row-wise cumulative sum
    (for ([i (in-range (add1 m))])
      (let ([row (vector-ref diff i)])
        (for ([j (in-range 1 (add1 n))])
          (vector-set! row j (+ (vector-ref row j)
                                (vector-ref row (- j 1)))))))
    ;; column-wise cumulative sum
    (for ([i (in-range 1 (add1 m))])
      (let ([row (vector-ref diff i)]
            [prev-row (vector-ref diff (- i 1))])
        (for ([j (in-range (add1 n))])
          (vector-set! row j (+ (vector-ref row j)
                                (vector-ref prev-row j))))))
    ;; verify all zero cells are covered
    (let ([possible #t])
      (for ([i (in-range m)] #:break (not possible))
        (let ([grid-row (vector-ref grid-vec i)]
              [diff-row (vector-ref diff i)])
          (for ([j (in-range n)] #:break (not possible))
            (when (and (= (vector-ref grid-row j) 0)
                       (= (vector-ref diff-row j) 0))
              (set! possible #f)))))
      possible)))
```

## Erlang

```erlang
-spec possible_to_stamp(Grid :: [[integer()]], StampHeight :: integer(), StampWidth :: integer()) -> boolean().
possible_to_stamp(Grid, StampHeight, StampWidth) ->
    % Convert grid rows to tuples for O(1) access
    GridTuples = [list_to_tuple(Row) || Row <- Grid],
    case GridTuples of
        [] -> true;
        [_|_] ->
            M = length(GridTuples),
            N = tuple_size(hd(GridTuples)),
            % Build prefix sum matrix (tuple of tuples)
            PrefixTuple = build_prefix(GridTuples, M, N),

            % Initialize diff array for imos method
            Size = (M + 1) * (N + 1),
            Diff0 = array:new(Size, {default, 0}),
            Np1 = N + 1,

            % Apply stamp placements using prefix sums
            MaxI = M - StampHeight,
            MaxJ = N - StampWidth,
            Diff1 = if
                MaxI < 0 orelse MaxJ < 0 ->
                    Diff0;
                true ->
                    apply_stamps(0, MaxI, 0, MaxJ, PrefixTuple, StampHeight, StampWidth,
                                 Np1, Diff0)
            end,

            % Convert diff to coverage via 2‑D prefix sums
            Coverage = row_prefix(Diff1, M, N, Np1),
            Coverage2 = col_prefix(Coverage, M, N, Np1),

            % Verify every empty cell is covered
            verify_cells(GridTuples, Coverage2, M, N, Np1)
    end.

%% Build 2‑D prefix sum matrix (tuple of tuples) with leading zero row/col
build_prefix(GridTuples, M, N) ->
    ZeroRow = list_to_tuple(lists:duplicate(N + 1, 0)),
    {RowsRev, _} = lists:foldl(
        fun(RowTuple, {AccRows, PrevPref}) ->
            CurrRow = build_curr_row(RowTuple, PrevPref, N),
            {[CurrRow | AccRows], CurrRow}
        end,
        {[ZeroRow], ZeroRow},
        GridTuples),
    PrefixList = lists:reverse(RowsRev),          % includes zero row at front
    list_to_tuple(PrefixList).

%% Build a prefix row given current grid row tuple and previous prefix row tuple
build_curr_row(GridRow, PrevPref, N) ->
    CurrVals = build_curr_col(1, N, GridRow, PrevPref, 0, 0, []),
    RowList = [0 | lists:reverse(CurrVals)],
    list_to_tuple(RowList).

build_curr_col(J, N, _GridRow, _PrevPref, _Left, _UpLeft, Acc) when J > N ->
    Acc;
build_curr_col(J, N, GridRow, PrevPref, Left, UpLeft, Acc) ->
    G = element(J, GridRow),
    Up = element(J, PrevPref),
    Curr = G + Up + Left - UpLeft,
    build_curr_col(J + 1, N, GridRow, PrevPref, Curr, Up, [Curr | Acc]).

%% Apply all possible stamps and update diff array
apply_stamps(I, MaxI, JStart, MaxJ, PrefixTuple, H, W, Np1, Diff) when I =< MaxI ->
    DiffAfterRow = apply_row(I, JStart, MaxJ, PrefixTuple, H, W, Np1, Diff),
    apply_stamps(I + 1, MaxI, JStart, MaxJ, PrefixTuple, H, W, Np1, DiffAfterRow);
apply_stamps(_I, _MaxI, _JStart, _MaxJ, _PrefixTuple, _H, _W, _Np1, Diff) ->
    Diff.

apply_row(I, J, MaxJ, PrefixTuple, H, W, Np1, Diff) when J =< MaxJ ->
    Sum = rect_sum(PrefixTuple, I, J, H, W),
    NewDiff = if
        Sum == 0 ->
            R1 = I,
            C1 = J,
            R2 = I + H,
            C2 = J + W,
            Diff1 = add_diff(Diff, idx(R1, C1, Np1), 1),
            Diff2 = add_diff(Diff1, idx(R2, C1, Np1), -1),
            Diff3 = add_diff(Diff2, idx(R1, C2, Np1), -1),
            add_diff(Diff3, idx(R2, C2, Np1), 1);
        true ->
            Diff
    end,
    apply_row(I, J + 1, MaxJ, PrefixTuple, H, W, Np1, NewDiff);
apply_row(_I, _J, _MaxJ, _PrefixTuple, _H, _W, _Np1, Diff) ->
    Diff.

%% Rectangle sum using prefix matrix
rect_sum(PrefixTuple, I, J, H, W) ->
    R1 = I,
    C1 = J,
    R2 = I + H,
    C2 = J + W,
    RowR2 = element(R2 + 1, PrefixTuple),
    RowR1 = element(R1 + 1, PrefixTuple),
    A = element(C2 + 1, RowR2),
    B = element(C2 + 1, RowR1),
    C = element(C1 + 1, RowR2),
    D = element(C1 + 1, RowR1),
    A - B - C + D.

%% Index in flattened array
idx(R, C, Np1) -> R * Np1 + C.

add_diff(Diff, Idx, Delta) ->
    Old = array:get(Idx, Diff),
    array:set(Idx, Old + Delta, Diff).

%% Row‑wise prefix accumulation
row_prefix(Diff, M, N, Np1) ->
    row_prefix_loop(0, M, N, Np1, Diff).

row_prefix_loop(R, MaxR, _N, _Np1, Diff) when R > MaxR -> Diff;
row_prefix_loop(R, MaxR, N, Np1, Diff) ->
    Diff2 = row_accumulate_cols(R, 1, N, Np1, 0, Diff),
    row_prefix_loop(R + 1, MaxR, N, Np1, Diff2).

row_accumulate_cols(_R, C, N, _Np1, _Prev, Diff) when C > N -> Diff;
row_accumulate_cols(R, C, N, Np1, Prev, Diff) ->
    Idx = idx(R, C, Np1),
    Val = array:get(Idx, Diff) + Prev,
    NewDiff = array:set(Idx, Val, Diff),
    row_accumulate_cols(R, C + 1, N, Np1, Val, NewDiff).

%% Column‑wise prefix accumulation
col_prefix(Diff, M, N, Np1) ->
    col_prefix_loop(1, M, N, Np1, Diff).

col_prefix_loop(R, MaxR, _N, _Np1, Diff) when R > MaxR -> Diff;
col_prefix_loop(R, MaxR, N, Np1, Diff) ->
    Diff2 = col_accumulate_rows(R, 0, N, Np1, Diff),
    col_prefix_loop(R + 1, MaxR, N, Np1, Diff2).

col_accumulate_rows(_R, C, N, _Np1, Diff) when C > N -> Diff;
col_accumulate_rows(R, C, N, Np1, Diff) ->
    Idx = idx(R, C, Np1),
    UpIdx = idx(R - 1, C, Np1),
    Val = array:get(Idx, Diff) + array:get(UpIdx, Diff),
    NewDiff = array:set(Idx, Val, Diff),
    col_accumulate_rows(R, C + 1, N, Np1, NewDiff).

%% Verify every empty cell is covered
verify_cells([], _Coverage, _M, _N, _Np1) -> true;
verify_cells([RowTuple|RestRows], Coverage, RowIdx, N, Np1) ->
    case verify_row(RowTuple, Coverage, RowIdx, 0, N, Np1) of
        false -> false;
        true -> verify_cells(RestRows, Coverage, RowIdx + 1, N, Np1)
    end.

verify_row(_RowTuple, _Coverage, _R, C, N, _Np1) when C >= N ->
    true;
verify_row(RowTuple, Coverage, R, C, N, Np1) ->
    Cell = element(C + 1, RowTuple),
    case Cell of
        0 ->
            Idx = idx(R, C, Np1),
            Covered = array:get(Idx, Coverage) > 0,
            if Covered -> verify_row(RowTuple, Coverage, R, C + 1, N, Np1);
               true -> false
            end;
        _ ->
            verify_row(RowTuple, Coverage, R, C + 1, N, Np1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec possible_to_stamp(grid :: [[integer]], stamp_height :: integer, stamp_width :: integer) :: boolean
  def possible_to_stamp(grid, sh, sw) do
    m = length(grid)
    n = length(hd(grid))

    # convert grid rows to tuples for O(1) element access
    grid_rows = Enum.map(grid, &List.to_tuple/1)

    zero_row = :erlang.list_to_tuple(List.duplicate(0, n + 1))

    # build prefix sum matrix (tuple of rows, each row is a tuple)
    {ps_rev, _} =
      Enum.reduce(grid_rows, {[], zero_row}, fn grow, {rows_acc, prev_row} ->
        {rev_vals, _left} =
          Enum.reduce(0..(n - 1), {[], 0}, fn j, {rev, left} ->
            val = :erlang.element(j + 1, grow)
            up = :erlang.element(j + 1, prev_row)
            diag = :erlang.element(j, prev_row)
            cur = val + up + left - diag
            {[cur | rev], cur}
          end)

        cur_row = :erlang.list_to_tuple([0 | Enum.reverse(rev_vals)])
        {[cur_row | rows_acc], cur_row}
      end)

    ps_rows = Enum.reverse(ps_rev)
    ps_matrix = List.to_tuple([zero_row | ps_rows])

    # helper to get rectangle sum using prefix sums
    rect_sum = fn i, j ->
      a = :erlang.element(j, :erlang.element(i, ps_matrix))
      b = :erlang.element(j + sw, :erlang.element(i, ps_matrix))
      c = :erlang.element(j, :erlang.element(i + sh, ps_matrix))
      d = :erlang.element(j + sw, :erlang.element(i + sh, ps_matrix))
      d - b - c + a
    end

    max_i = m - sh
    max_j = n - sw

    diff =
      if max_i < 0 or max_j < 0 do
        %{}
      else
        Enum.reduce(0..max_i, %{}, fn i, acc ->
          Enum.reduce(0..max_j, acc, fn j, acc2 ->
            if rect_sum.(i, j) == 0 do
              acc2
              |> Map.update({i, j}, 1, &(&1 + 1))
              |> Map.update({i + sh, j}, -1, fn v -> v - 1 end)
              |> Map.update({i, j + sw}, -1, fn v -> v - 1 end)
              |> Map.update({i + sh, j + sw}, 1, &(&1 + 1))
            else
              acc2
            end
          end)
        end)
      end

    # verify each empty cell is covered
    prev_cover = List.duplicate(0, n)

    Enum.reduce_while(0..(m - 1), {diff, prev_cover}, fn i, {dmap, prev_row} ->
      {row_rev, _left, ok} =
        Enum.reduce(0..(n - 1), {[], 0, true}, fn j, {rev, left, acc_ok} ->
          base = Map.get(dmap, {i, j}, 0)
          up = Enum.at(prev_row, j)
          diag = if j > 0, do: Enum.at(prev_row, j - 1), else: 0
          cur = base + up + left - diag

          cell_val = :erlang.element(j + 1, Enum.at(grid_rows, i))
          acc_ok = acc_ok and (cell_val == 1 or cur > 0)

          {[cur | rev], cur, acc_ok}
        end)

      if not ok do
        {:halt, false}
      else
        current_row = Enum.reverse(row_rev)
        {:cont, {dmap, current_row}}
      end
    end)
    |> case do
      false -> false
      _ -> true
    end
  end
end
```

# 1895. Largest Magic Square

## Cpp

```cpp
class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<long long>> rowPref(m, vector<long long>(n + 1, 0));
        vector<vector<long long>> colPref(m + 1, vector<long long>(n, 0));
        vector<vector<long long>> diag1(m, vector<long long>(n, 0));
        vector<vector<long long>> diag2(m, vector<long long>(n, 0));

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rowPref[i][j + 1] = rowPref[i][j] + grid[i][j];
                colPref[i + 1][j] = colPref[i][j] + grid[i][j];
                diag1[i][j] = grid[i][j];
                if (i > 0 && j > 0) diag1[i][j] += diag1[i - 1][j - 1];
                diag2[i][j] = grid[i][j];
                if (i > 0 && j + 1 < n) diag2[i][j] += diag2[i - 1][j + 1];
            }
        }

        int maxK = min(m, n);
        for (int k = maxK; k >= 1; --k) {
            for (int i = 0; i + k <= m; ++i) {
                for (int j = 0; j + k <= n; ++j) {
                    long long target = rowPref[i][j + k] - rowPref[i][j];
                    bool ok = true;

                    // check rows
                    for (int r = i; r < i + k && ok; ++r) {
                        long long sum = rowPref[r][j + k] - rowPref[r][j];
                        if (sum != target) ok = false;
                    }
                    // check columns
                    for (int c = j; c < j + k && ok; ++c) {
                        long long sum = colPref[i + k][c] - colPref[i][c];
                        if (sum != target) ok = false;
                    }
                    // main diagonal
                    if (ok) {
                        long long d1 = diag1[i + k - 1][j + k - 1];
                        if (i > 0 && j > 0) d1 -= diag1[i - 1][j - 1];
                        if (d1 != target) ok = false;
                    }
                    // anti-diagonal
                    if (ok) {
                        long long d2 = diag2[i + k - 1][j];
                        if (i > 0 && j + k < n) d2 -= diag2[i - 1][j + k];
                        if (d2 != target) ok = false;
                    }

                    if (ok) return k;
                }
            }
        }
        return 1; // at least size 1 is always a magic square
    }
};
```

## Java

```java
class Solution {
    public int largestMagicSquare(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        // Row prefix sums
        int[][] rowPref = new int[m][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowPref[i][j + 1] = rowPref[i][j] + grid[i][j];
            }
        }
        // Column prefix sums
        int[][] colPref = new int[m + 1][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                colPref[i + 1][j] = colPref[i][j] + grid[i][j];
            }
        }
        // Main diagonal prefix sums (top-left to bottom-right)
        int[][] diag1 = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                diag1[i + 1][j + 1] = grid[i][j] + diag1[i][j];
            }
        }
        // Anti-diagonal prefix sums (top-right to bottom-left)
        int[][] diag2 = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = n - 1; j >= 0; j--) {
                diag2[i + 1][j] = grid[i][j] + diag2[i][j + 1];
            }
        }

        int maxSize = Math.min(m, n);
        for (int size = maxSize; size >= 1; --size) {
            for (int i = 0; i + size - 1 < m; ++i) {
                for (int j = 0; j + size - 1 < n; ++j) {
                    int target = rowPref[i][j + size] - rowPref[i][j];
                    boolean ok = true;
                    // Check rows
                    for (int r = i; r < i + size; ++r) {
                        if (rowPref[r][j + size] - rowPref[r][j] != target) {
                            ok = false;
                            break;
                        }
                    }
                    if (!ok) continue;
                    // Check columns
                    for (int c = j; c < j + size; ++c) {
                        if (colPref[i + size][c] - colPref[i][c] != target) {
                            ok = false;
                            break;
                        }
                    }
                    if (!ok) continue;
                    // Main diagonal
                    int d1 = diag1[i + size][j + size] - diag1[i][j];
                    if (d1 != target) continue;
                    // Anti-diagonal
                    int d2 = diag2[i + size][j] - diag2[i][j + size];
                    if (d2 != target) continue;
                    return size;
                }
            }
        }
        return 1; // at least a 1x1 magic square exists
    }
}
```

## Python

```python
class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # row prefix sums
        rowPref = []
        for i in range(m):
            rp = [0] * (n + 1)
            s = 0
            for j in range(n):
                s += grid[i][j]
                rp[j + 1] = s
            rowPref.append(rp)
        # column prefix sums
        colPref = [[0] * (m + 1) for _ in range(n)]
        for j in range(n):
            s = 0
            for i in range(m):
                s += grid[i][j]
                colPref[j][i + 1] = s
        # main diagonal prefix sums (top-left to bottom-right)
        diag1 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diag1[i][j] = grid[i][j]
                if i > 0 and j > 0:
                    diag1[i][j] += diag1[i - 1][j - 1]
        # anti-diagonal prefix sums (top-right to bottom-left)
        diag2 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                diag2[i][j] = grid[i][j]
                if i > 0 and j + 1 < n:
                    diag2[i][j] += diag2[i - 1][j + 1]

        maxK = min(m, n)
        for k in range(maxK, 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    target = rowPref[r][c + k] - rowPref[r][c]
                    ok = True
                    # check rows
                    for i in range(r, r + k):
                        if rowPref[i][c + k] - rowPref[i][c] != target:
                            ok = False
                            break
                    if not ok:
                        continue
                    # check columns
                    for j in range(c, c + k):
                        if colPref[j][r + k] - colPref[j][r] != target:
                            ok = False
                            break
                    if not ok:
                        continue
                    # main diagonal sum
                    br_i = r + k - 1
                    br_j = c + k - 1
                    diag_sum = diag1[br_i][br_j]
                    if r > 0 and c > 0:
                        diag_sum -= diag1[r - 1][c - 1]
                    if diag_sum != target:
                        continue
                    # anti-diagonal sum
                    bl_i = r + k - 1
                    bl_j = c
                    anti_sum = diag2[bl_i][bl_j]
                    if r > 0 and c + k < n:
                        anti_sum -= diag2[r - 1][c + k]
                    if anti_sum != target:
                        continue
                    return k
        return 1
```

## Python3

```python
class Solution:
    def largestMagicSquare(self, grid):
        from typing import List
        m, n = len(grid), len(grid[0])
        # row prefix sums
        row_ps = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            s = 0
            for j in range(n):
                s += grid[i][j]
                row_ps[i][j + 1] = s
        # column prefix sums
        col_ps = [[0] * (m + 1) for _ in range(n)]
        for j in range(n):
            s = 0
            for i in range(m):
                s += grid[i][j]
                col_ps[j][i + 1] = s
        # main diagonal prefix sums
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                diag1[i + 1][j + 1] = grid[i][j] + diag1[i][j]
        # anti-diagonal prefix sums
        anti = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                anti[i + 1][j] = grid[i][j] + anti[i][j + 1]

        max_k = min(m, n)
        for k in range(max_k, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row_ps[i][j + k] - row_ps[i][j]
                    ok = True
                    # check rows
                    for r in range(i, i + k):
                        if row_ps[r][j + k] - row_ps[r][j] != target:
                            ok = False
                            break
                    if not ok:
                        continue
                    # check columns
                    for c in range(j, j + k):
                        if col_ps[c][i + k] - col_ps[c][i] != target:
                            ok = False
                            break
                    if not ok:
                        continue
                    # main diagonal
                    d1 = diag1[i + k][j + k] - diag1[i][j]
                    if d1 != target:
                        continue
                    # anti-diagonal
                    d2 = anti[i + k][j] - anti[i][j + k]
                    if d2 != target:
                        continue
                    return k
        return 1
```

## C

```c
int largestMagicSquare(int** grid, int gridSize, int* gridColSize){
    int m = gridSize;
    int n = gridColSize[0];
    // Row prefix sums
    int **rowPref = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i) {
        rowPref[i] = (int*)malloc((n + 1) * sizeof(int));
        rowPref[i][0] = 0;
        for (int j = 0; j < n; ++j) {
            rowPref[i][j + 1] = rowPref[i][j] + grid[i][j];
        }
    }
    // Column prefix sums
    int **colPref = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; ++i) {
        colPref[i] = (int*)malloc(n * sizeof(int));
    }
    for (int j = 0; j < n; ++j) {
        colPref[0][j] = 0;
        for (int i = 0; i < m; ++i) {
            colPref[i + 1][j] = colPref[i][j] + grid[i][j];
        }
    }

    int maxK = (m < n ? m : n);
    for (int k = maxK; k >= 1; --k) {
        for (int i = 0; i + k <= m; ++i) {
            for (int j = 0; j + k <= n; ++j) {
                int target = rowPref[i][j + k] - rowPref[i][j];
                int ok = 1;
                // check rows
                for (int r = i; r < i + k && ok; ++r) {
                    if (rowPref[r][j + k] - rowPref[r][j] != target) ok = 0;
                }
                // check columns
                for (int c = j; c < j + k && ok; ++c) {
                    if (colPref[i + k][c] - colPref[i][c] != target) ok = 0;
                }
                // main diagonal
                int sumDiag = 0;
                for (int d = 0; d < k; ++d) sumDiag += grid[i + d][j + d];
                if (sumDiag != target) ok = 0;
                // anti-diagonal
                int sumAnti = 0;
                for (int d = 0; d < k; ++d) sumAnti += grid[i + d][j + k - 1 - d];
                if (sumAnti != target) ok = 0;

                if (ok) {
                    // free allocated memory before returning
                    for (int ii = 0; ii < m; ++ii) free(rowPref[ii]);
                    free(rowPref);
                    for (int ii = 0; ii <= m; ++ii) free(colPref[ii]);
                    free(colPref);
                    return k;
                }
            }
        }
    }

    // free allocated memory
    for (int i = 0; i < m; ++i) free(rowPref[i]);
    free(rowPref);
    for (int i = 0; i <= m; ++i) free(colPref[i]);
    free(colPref);
    return 1;
}
```

## Csharp

```csharp
public class Solution
{
    public int LargestMagicSquare(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;

        long[,] rowPref = new long[m, n + 1];
        long[,] colPref = new long[m + 1, n];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                rowPref[i, j + 1] = rowPref[i, j] + grid[i][j];
                colPref[i + 1, j] = colPref[i, j] + grid[i][j];
            }
        }

        long[,] diag1 = new long[m, n]; // top-left to bottom-right
        long[,] diag2 = new long[m, n]; // top-right to bottom-left
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                long val = grid[i][j];
                diag1[i, j] = val + ((i > 0 && j > 0) ? diag1[i - 1, j - 1] : 0);
                diag2[i, j] = val + ((i > 0 && j + 1 < n) ? diag2[i - 1, j + 1] : 0);
            }
        }

        int maxK = Math.Min(m, n);
        for (int k = maxK; k >= 1; k--)
        {
            for (int i = 0; i + k <= m; i++)
            {
                for (int j = 0; j + k <= n; j++)
                {
                    long target = rowPref[i, j + k] - rowPref[i, j];
                    bool ok = true;

                    // check rows
                    for (int r = i; r < i + k && ok; r++)
                    {
                        if (rowPref[r, j + k] - rowPref[r, j] != target)
                            ok = false;
                    }

                    // check columns
                    for (int c = j; c < j + k && ok; c++)
                    {
                        if (colPref[i + k, c] - colPref[i, c] != target)
                            ok = false;
                    }

                    // main diagonal
                    long d1 = diag1[i + k - 1, j + k - 1] -
                              ((i > 0 && j > 0) ? diag1[i - 1, j - 1] : 0);
                    if (d1 != target) ok = false;

                    // anti diagonal
                    long d2 = diag2[i + k - 1, j] -
                              ((i > 0 && j + k < n) ? diag2[i - 1, j + k] : 0);
                    if (d2 != target) ok = false;

                    if (ok)
                        return k;
                }
            }
        }

        return 1; // fallback, though loop will always return for k=1
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var largestMagicSquare = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    
    // row prefix sums
    const rowPref = Array.from({length: m}, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            rowPref[i][j + 1] = rowPref[i][j] + grid[i][j];
        }
    }
    
    // column prefix sums
    const colPref = Array.from({length: m + 1}, () => new Array(n).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            colPref[i + 1][j] = colPref[i][j] + grid[i][j];
        }
    }
    
    // main diagonal prefix sums (top-left to bottom-right)
    const diag1 = Array.from({length: m + 1}, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j];
        }
    }
    
    // anti-diagonal prefix sums (top-right to bottom-left)
    const diag2 = Array.from({length: m + 1}, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = n - 1; j >= 0; --j) {
            diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j];
        }
    }
    
    const maxSize = Math.min(m, n);
    for (let k = maxSize; k >= 1; --k) {
        for (let i = 0; i <= m - k; ++i) {
            for (let j = 0; j <= n - k; ++j) {
                const target = rowPref[i][j + k] - rowPref[i][j];
                let ok = true;
                
                // check rows
                for (let r = i; r < i + k; ++r) {
                    if (rowPref[r][j + k] - rowPref[r][j] !== target) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) continue;
                
                // check columns
                for (let c = j; c < j + k; ++c) {
                    if (colPref[i + k][c] - colPref[i][c] !== target) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) continue;
                
                // check diagonals
                const d1 = diag1[i + k][j + k] - diag1[i][j];
                const d2 = diag2[i + k][j] - diag2[i][j + k];
                if (d1 === target && d2 === target) {
                    return k;
                }
            }
        }
    }
    return 1; // fallback, though loop always returns for k=1
};
```

## Typescript

```typescript
function largestMagicSquare(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    // Row prefix sums
    const rowPref: number[][] = Array.from({ length: m }, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            rowPref[i][j + 1] = rowPref[i][j] + grid[i][j];
        }
    }

    // Column prefix sums
    const colPref: number[][] = Array.from({ length: m + 1 }, () => new Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            colPref[i + 1][j] = colPref[i][j] + grid[i][j];
        }
    }

    // Main diagonal prefix sums
    const diag1: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j];
        }
    }

    // Anti-diagonal prefix sums
    const antiDiag: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = n - 1; j >= 0; j--) {
            antiDiag[i + 1][j] = antiDiag[i][j + 1] + grid[i][j];
        }
    }

    const maxSize = Math.min(m, n);
    for (let k = maxSize; k >= 1; k--) {
        for (let i = 0; i <= m - k; i++) {
            for (let j = 0; j <= n - k; j++) {
                const target = rowPref[i][j + k] - rowPref[i][j];
                let ok = true;

                // Check rows
                for (let r = i; r < i + k && ok; r++) {
                    if (rowPref[r][j + k] - rowPref[r][j] !== target) ok = false;
                }

                // Check columns
                for (let c = j; c < j + k && ok; c++) {
                    if (colPref[i + k][c] - colPref[i][c] !== target) ok = false;
                }

                // Main diagonal
                if (ok) {
                    const d1 = diag1[i + k][j + k] - diag1[i][j];
                    if (d1 !== target) ok = false;
                }

                // Anti-diagonal
                if (ok) {
                    const d2 = antiDiag[i + k][j] - antiDiag[i][j + k];
                    if (d2 !== target) ok = false;
                }

                if (ok) return k;
            }
        }
    }
    return 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largestMagicSquare($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        // row prefix sums
        $rowPref = [];
        for ($i = 0; $i < $m; $i++) {
            $rowPref[$i] = array_fill(0, $n + 1, 0);
            for ($j = 0; $j < $n; $j++) {
                $rowPref[$i][$j + 1] = $rowPref[$i][$j] + $grid[$i][$j];
            }
        }

        // column prefix sums
        $colPref = [];
        for ($j = 0; $j < $n; $j++) {
            $colPref[$j] = array_fill(0, $m + 1, 0);
            for ($i = 0; $i < $m; $i++) {
                $colPref[$j][$i + 1] = $colPref[$j][$i] + $grid[$i][$j];
            }
        }

        // main diagonal prefix sums
        $diag1 = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $diag1[$i + 1][$j + 1] = $grid[$i][$j] + $diag1[$i][$j];
            }
        }

        // anti-diagonal prefix sums
        $diag2 = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = $n - 1; $j >= 0; $j--) {
                $diag2[$i + 1][$j] = $grid[$i][$j] + $diag2[$i][$j + 1];
            }
        }

        $maxSize = min($m, $n);
        for ($k = $maxSize; $k >= 1; $k--) {
            for ($i = 0; $i + $k <= $m; $i++) {
                for ($j = 0; $j + $k <= $n; $j++) {
                    // target sum from first row
                    $target = $rowPref[$i][$j + $k] - $rowPref[$i][$j];
                    $ok = true;

                    // check rows
                    for ($r = $i; $r < $i + $k && $ok; $r++) {
                        $sum = $rowPref[$r][$j + $k] - $rowPref[$r][$j];
                        if ($sum !== $target) {
                            $ok = false;
                        }
                    }
                    if (!$ok) continue;

                    // check columns
                    for ($c = $j; $c < $j + $k && $ok; $c++) {
                        $sum = $colPref[$c][$i + $k] - $colPref[$c][$i];
                        if ($sum !== $target) {
                            $ok = false;
                        }
                    }
                    if (!$ok) continue;

                    // main diagonal
                    $diagSum = $diag1[$i + $k][$j + $k] - $diag1[$i][$j];
                    if ($diagSum !== $target) continue;

                    // anti-diagonal
                    $antiSum = $diag2[$i + $k][$j] - $diag2[$i][$j + $k];
                    if ($antiSum !== $target) continue;

                    return $k;
                }
            }
        }

        return 1; // at least a 1x1 magic square exists
    }
}
```

## Swift

```swift
class Solution {
    func largestMagicSquare(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        
        // Prefix sums for rows
        var rowPrefix = Array(repeating: Array(repeating: 0, count: n + 1), count: m)
        // Prefix sums for columns
        var colPrefix = Array(repeating: Array(repeating: 0, count: n), count: m + 1)
        // Main diagonal prefix sums
        var diag1 = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        // Anti-diagonal prefix sums
        var antiDiag = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        
        for i in 0..<m {
            for j in 0..<n {
                let val = grid[i][j]
                rowPrefix[i][j + 1] = rowPrefix[i][j] + val
                colPrefix[i + 1][j] = colPrefix[i][j] + val
                diag1[i + 1][j + 1] = diag1[i][j] + val
                antiDiag[i + 1][j] = antiDiag[i][j + 1] + val
            }
        }
        
        let maxK = min(m, n)
        for k in stride(from: maxK, through: 1, by: -1) {
            let limitI = m - k
            let limitJ = n - k
            if limitI < 0 || limitJ < 0 { continue }
            for i in 0...limitI {
                for j in 0...limitJ {
                    let target = rowPrefix[i][j + k] - rowPrefix[i][j]
                    var ok = true
                    
                    // Check rows
                    var r = i
                    while r < i + k {
                        if rowPrefix[r][j + k] - rowPrefix[r][j] != target {
                            ok = false
                            break
                        }
                        r += 1
                    }
                    if !ok { continue }
                    
                    // Check columns
                    var c = j
                    while c < j + k {
                        if colPrefix[i + k][c] - colPrefix[i][c] != target {
                            ok = false
                            break
                        }
                        c += 1
                    }
                    if !ok { continue }
                    
                    // Main diagonal
                    let diagSum = diag1[i + k][j + k] - diag1[i][j]
                    if diagSum != target { continue }
                    
                    // Anti-diagonal
                    let antiDiagSum = antiDiag[i + k][j] - antiDiag[i][j + k]
                    if antiDiagSum != target { continue }
                    
                    return k
                }
            }
        }
        return 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestMagicSquare(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size

        // row prefix sums
        val rowPref = Array(m) { LongArray(n + 1) }
        for (i in 0 until m) {
            var sum = 0L
            for (j in 0 until n) {
                sum += grid[i][j].toLong()
                rowPref[i][j + 1] = sum
            }
        }

        // column prefix sums
        val colPref = Array(n) { LongArray(m + 1) }
        for (j in 0 until n) {
            var sum = 0L
            for (i in 0 until m) {
                sum += grid[i][j].toLong()
                colPref[j][i + 1] = sum
            }
        }

        // main diagonal prefix sums (top-left to bottom-right)
        val diag1 = Array(m + 1) { LongArray(n + 1) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j].toLong()
            }
        }

        // anti-diagonal prefix sums (top-right to bottom-left)
        val anti = Array(m + 1) { LongArray(n + 1) }
        for (i in 0 until m) {
            for (j in n - 1 downTo 0) {
                anti[i + 1][j] = anti[i][j + 1] + grid[i][j].toLong()
            }
        }

        val maxSize = minOf(m, n)
        for (k in maxSize downTo 1) {
            for (r in 0..m - k) {
                for (c in 0..n - k) {
                    // target sum from first row
                    val target = rowPref[r][c + k] - rowPref[r][c]

                    var ok = true

                    // check rows
                    for (i in r until r + k) {
                        val sumRow = rowPref[i][c + k] - rowPref[i][c]
                        if (sumRow != target) { ok = false; break }
                    }
                    if (!ok) continue

                    // check columns
                    for (j in c until c + k) {
                        val sumCol = colPref[j][r + k] - colPref[j][r]
                        if (sumCol != target) { ok = false; break }
                    }
                    if (!ok) continue

                    // main diagonal
                    val diagSum = diag1[r + k][c + k] - diag1[r][c]
                    if (diagSum != target) continue

                    // anti-diagonal
                    val antiSum = anti[r + k][c] - anti[r][c + k]
                    if (antiSum != target) continue

                    return k
                }
            }
        }
        return 0 // should never reach because size 1 always works
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int largestMagicSquare(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // Row prefix sums
    List<List<int>> rowPref = List.generate(m, (_) => List.filled(n + 1, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        rowPref[i][j + 1] = rowPref[i][j] + grid[i][j];
      }
    }

    // Column prefix sums
    List<List<int>> colPref = List.generate(n, (_) => List.filled(m + 1, 0));
    for (int j = 0; j < n; ++j) {
      for (int i = 0; i < m; ++i) {
        colPref[j][i + 1] = colPref[j][i] + grid[i][j];
      }
    }

    // Main diagonal prefix sums
    List<List<int>> diag1 = List.generate(m + 1, (_) => List.filled(n + 1, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        diag1[i + 1][j + 1] = grid[i][j] + diag1[i][j];
      }
    }

    // Anti-diagonal prefix sums
    List<List<int>> diag2 = List.generate(m + 1, (_) => List.filled(n + 1, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = n - 1; j >= 0; --j) {
        diag2[i + 1][j] = grid[i][j] + diag2[i][j + 1];
      }
    }

    int maxSize = min(m, n);
    for (int k = maxSize; k >= 1; --k) {
      for (int i = 0; i + k <= m; ++i) {
        for (int j = 0; j + k <= n; ++j) {
          int target = rowPref[i][j + k] - rowPref[i][j];
          bool ok = true;

          // Check rows
          for (int r = i; r < i + k && ok; ++r) {
            int sumRow = rowPref[r][j + k] - rowPref[r][j];
            if (sumRow != target) ok = false;
          }

          // Check columns
          for (int c = j; c < j + k && ok; ++c) {
            int sumCol = colPref[c][i + k] - colPref[c][i];
            if (sumCol != target) ok = false;
          }

          // Check main diagonal
          if (ok) {
            int d1 = diag1[i + k][j + k] - diag1[i][j];
            if (d1 != target) ok = false;
          }

          // Check anti-diagonal
          if (ok) {
            int d2 = diag2[i + k][j] - diag2[i][j + k];
            if (d2 != target) ok = false;
          }

          if (ok) return k;
        }
      }
    }
    return 1; // At least size 1 is always a magic square
  }
}
```

## Golang

```go
func largestMagicSquare(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	// Row prefix sums
	rowPref := make([][]int, m)
	for i := 0; i < m; i++ {
		rowPref[i] = make([]int, n+1)
		for j := 0; j < n; j++ {
			rowPref[i][j+1] = rowPref[i][j] + grid[i][j]
		}
	}
	// Column prefix sums
	colPref := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		colPref[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			colPref[i+1][j] = colPref[i][j] + grid[i][j]
		}
	}
	// Main diagonal prefix (down-right)
	diag1 := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		diag1[i] = make([]int, n+1)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			diag1[i+1][j+1] = grid[i][j] + diag1[i][j]
		}
	}
	// Anti-diagonal prefix (down-left)
	diag2 := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		diag2[i] = make([]int, n+1)
	}
	for i := 0; i < m; i++ {
		for j := n - 1; j >= 0; j-- {
			diag2[i+1][j] = grid[i][j] + diag2[i][j+1]
		}
	}

	minSide := m
	if n < minSide {
		minSide = n
	}
	for k := minSide; k >= 1; k-- {
		for r := 0; r <= m-k; r++ {
			for c := 0; c <= n-k; c++ {
				target := rowPref[r][c+k] - rowPref[r][c]
				ok := true
				// check rows
				for i := r; i < r+k && ok; i++ {
					if rowPref[i][c+k]-rowPref[i][c] != target {
						ok = false
					}
				}
				if !ok {
					continue
				}
				// check columns
				for j := c; j < c+k && ok; j++ {
					if colPref[r+k][j]-colPref[r][j] != target {
						ok = false
					}
				}
				if !ok {
					continue
				}
				// main diagonal
				if diag1[r+k][c+k]-diag1[r][c] != target {
					continue
				}
				// anti-diagonal
				if diag2[r+k][c]-diag2[r][c+k] != target {
					continue
				}
				return k
			}
		}
	}
	return 1
}
```

## Ruby

```ruby
def largest_magic_square(grid)
  m = grid.size
  n = grid[0].size
  # row prefix sums
  row_prefix = Array.new(m) { Array.new(n + 1, 0) }
  m.times do |i|
    n.times do |j|
      row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
    end
  end

  # column prefix sums
  col_prefix = Array.new(m + 1) { Array.new(n, 0) }
  m.times do |i|
    n.times do |j|
      col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]
    end
  end

  # main diagonal prefix sums
  diag1_prefix = Array.new(m + 1) { Array.new(n + 1, 0) }
  m.times do |i|
    n.times do |j|
      diag1_prefix[i + 1][j + 1] = diag1_prefix[i][j] + grid[i][j]
    end
  end

  # anti-diagonal prefix sums
  diag2_prefix = Array.new(m + 1) { Array.new(n + 1, 0) }
  m.times do |i|
    (n - 1).downto(0) do |j|
      diag2_prefix[i + 1][j] = diag2_prefix[i][j + 1] + grid[i][j]
    end
  end

  max_k = [m, n].min
  max_k.downto(1) do |k|
    (0..m - k).each do |r|
      (0..n - k).each do |c|
        target = row_prefix[r][c + k] - row_prefix[r][c]
        ok = true

        # check rows
        r.upto(r + k - 1) do |i|
          sum = row_prefix[i][c + k] - row_prefix[i][c]
          unless sum == target
            ok = false
            break
          end
        end
        next unless ok

        # check columns
        c.upto(c + k - 1) do |j|
          sum = col_prefix[r + k][j] - col_prefix[r][j]
          unless sum == target
            ok = false
            break
          end
        end
        next unless ok

        # main diagonal
        diag1 = diag1_prefix[r + k][c + k] - diag1_prefix[r][c]
        next unless diag1 == target

        # anti-diagonal
        diag2 = diag2_prefix[r + k][c] - diag2_prefix[r][c + k]
        next unless diag2 == target

        return k
      end
    end
  end
  1
end
```

## Scala

```scala
object Solution {
    def largestMagicSquare(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        // Prefix sums for rows
        val rowPref = Array.ofDim[Long](m, n + 1)
        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                rowPref(i)(j + 1) = rowPref(i)(j) + grid(i)(j).toLong
                j += 1
            }
            i += 1
        }
        // Prefix sums for columns
        val colPref = Array.ofDim[Long](m + 1, n)
        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                colPref(i + 1)(j) = colPref(i)(j) + grid(i)(j).toLong
                j += 1
            }
            i += 1
        }
        // Diagonal TL-BR prefix
        val diag1 = Array.ofDim[Long](m, n)
        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                val add = grid(i)(j).toLong
                diag1(i)(j) = add + (if (i > 0 && j > 0) diag1(i - 1)(j - 1) else 0L)
                j += 1
            }
            i += 1
        }
        // Diagonal TR-BL prefix
        val diag2 = Array.ofDim[Long](m, n)
        i = 0
        while (i < m) {
            var j = n - 1
            while (j >= 0) {
                val add = grid(i)(j).toLong
                diag2(i)(j) = add + (if (i > 0 && j + 1 < n) diag2(i - 1)(j + 1) else 0L)
                j -= 1
            }
            i += 1
        }

        var maxSize = 1
        val maxK = Math.min(m, n)

        var k = maxK
        while (k >= 2 && maxSize < k) {
            var found = false
            var r0 = 0
            while (r0 <= m - k && !found) {
                var c0 = 0
                while (c0 <= n - k && !found) {
                    val target = rowPref(r0)(c0 + k) - rowPref(r0)(c0)

                    // check rows
                    var ok = true
                    var r = r0 + 1
                    while (r < r0 + k && ok) {
                        val sum = rowPref(r)(c0 + k) - rowPref(r)(c0)
                        if (sum != target) ok = false
                        r += 1
                    }

                    // check columns
                    var c = c0
                    while (c < c0 + k && ok) {
                        val sum = colPref(r0 + k)(c) - colPref(r0)(c)
                        if (sum != target) ok = false
                        c += 1
                    }

                    // main diagonal
                    if (ok) {
                        val d1 = diag1(r0 + k - 1)(c0 + k - 1) -
                                 (if (r0 > 0 && c0 > 0) diag1(r0 - 1)(c0 - 1) else 0L)
                        if (d1 != target) ok = false
                    }

                    // anti diagonal
                    if (ok) {
                        val d2 = diag2(r0 + k - 1)(c0) -
                                 (if (r0 > 0 && c0 + k < n) diag2(r0 - 1)(c0 + k) else 0L)
                        if (d2 != target) ok = false
                    }

                    if (ok) {
                        maxSize = k
                        found = true
                    }
                    c0 += 1
                }
                r0 += 1
            }
            if (found) return maxSize
            k -= 1
        }
        maxSize
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        // Row prefix sums
        let mut row_ps = vec![vec![0i64; n + 1]; m];
        for i in 0..m {
            for j in 0..n {
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j] as i64;
            }
        }

        // Column prefix sums
        let mut col_ps = vec![vec![0i64; m + 1]; n];
        for j in 0..n {
            for i in 0..m {
                col_ps[j][i + 1] = col_ps[j][i] + grid[i][j] as i64;
            }
        }

        // Diagonal (top-left to bottom-right) prefix sums
        let mut diag1 = vec![vec![0i64; n + 1]; m + 1];
        for i in 0..m {
            for j in 0..n {
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j] as i64;
            }
        }

        // Anti-diagonal (top-right to bottom-left) prefix sums
        let mut diag2 = vec![vec![0i64; n + 1]; m + 1];
        for i in 0..m {
            for j in (0..n).rev() {
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j] as i64;
            }
        }

        let max_k = std::cmp::min(m, n);
        for k in (1..=max_k).rev() {
            for r in 0..=m - k {
                for c in 0..=n - k {
                    // Target sum from the first row of the square
                    let target = row_ps[r][c + k] - row_ps[r][c];
                    let mut ok = true;

                    // Check all rows
                    for i in r..r + k {
                        if row_ps[i][c + k] - row_ps[i][c] != target {
                            ok = false;
                            break;
                        }
                    }
                    if !ok {
                        continue;
                    }

                    // Check all columns
                    for j in c..c + k {
                        if col_ps[j][r + k] - col_ps[j][r] != target {
                            ok = false;
                            break;
                        }
                    }
                    if !ok {
                        continue;
                    }

                    // Main diagonal sum
                    let d1 = diag1[r + k][c + k] - diag1[r][c];
                    if d1 != target {
                        continue;
                    }

                    // Anti-diagonal sum
                    let d2 = diag2[r + k][c] - diag2[r][c + k];
                    if d2 != target {
                        continue;
                    }

                    return k as i32;
                }
            }
        }
        1
    }
}
```

## Racket

```racket
(define/contract (largest-magic-square grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows-list (map list->vector grid))
         (rows-vec (list->vector rows-list))
         (m (vector-length rows-vec))
         (n (if (= m 0) 0 (vector-length (vector-ref rows-vec 0))))
         ;; row prefix sums
         (row-pref
          (let ((v (make-vector m)))
            (for ([i (in-range m)])
              (let* ((row (vector-ref rows-vec i))
                     (pref (make-vector (+ n 1) 0)))
                (for ([j (in-range n)])
                  (vector-set! pref (add1 j)
                               (+ (vector-ref pref j)
                                  (vector-ref row j))))
                (vector-set! v i pref)))
            v))
         ;; column prefix sums
         (col-pref
          (let ((v (make-vector n)))
            (for ([j (in-range n)])
              (let ((pref (make-vector (+ m 1) 0)))
                (for ([i (in-range m)])
                  (vector-set! pref (add1 i)
                               (+ (vector-ref pref i)
                                  (vector-ref (vector-ref rows-vec i) j))))
                (vector-set! v j pref)))
            v))
         ;; main diagonal prefix
         (diag1
          (let ((v (make-vector (add1 m))))
            (for ([i (in-range (add1 m))])
              (vector-set! v i (make-vector (add1 n) 0)))
            (for ([i (in-range m)])
              (for ([j (in-range n)])
                (let* ((prev (vector-ref (vector-ref v i) j))
                       (val (vector-ref (vector-ref rows-vec i) j))
                       (new (+ prev val)))
                  (vector-set! (vector-ref v (add1 i)) (add1 j) new))))
            v))
         ;; anti-diagonal prefix
         (anti
          (let ((v (make-vector (add1 m))))
            (for ([i (in-range (add1 m))])
              (vector-set! v i (make-vector (add1 n) 0)))
            (for ([i (in-range m)])
              (for ([j (in-range (- n 1) -1 -1)]) ; from n-1 down to 0
                (let* ((next (vector-ref (vector-ref v i) (add1 j)))
                       (val (vector-ref (vector-ref rows-vec i) j))
                       (new (+ next val)))
                  (vector-set! (vector-ref v (add1 i)) j new))))
            v))
         ;; helper to test magic square at (i,j) size k
         (magic-at?
          (lambda (i j k)
            (let* ((target (- (vector-ref (vector-ref row-pref i) (+ j k))
                             (vector-ref (vector-ref row-pref i) j))))
              (and
               ;; rows
               (for/and ([r (in-range i (+ i k))])
                 (= (- (vector-ref (vector-ref row-pref r) (+ j k))
                       (vector-ref (vector-ref row-pref r) j))
                    target))
               ;; columns
               (for/and ([c (in-range j (+ j k))])
                 (= (- (vector-ref (vector-ref col-pref c) (+ i k))
                       (vector-ref (vector-ref col-pref c) i))
                    target))
               ;; main diagonal
               (= (- (vector-ref (vector-ref diag1 (+ i k)) (+ j k))
                     (vector-ref (vector-ref diag1 i) j))
                  target)
               ;; anti diagonal
               (= (- (vector-ref (vector-ref anti (+ i k)) j)
                     (vector-ref (vector-ref anti i) (+ j k)))
                  target))))))
    ;; search from largest size downwards
    (let loop ((k (min m n)))
      (if (= k 0)
          0
          (let* ((limit-i (+ 1 (- m k)))
                 (limit-j (+ 1 (- n k)))
                 (found (for*/first ([i (in-range limit-i)]
                                     [j (in-range limit-j)]
                                     #:when (magic-at? i j k))
                          k)))
            (if found
                found
                (loop (sub1 k))))))))
```

## Erlang

```erlang
-module(solution).
-export([largest_magic_square/1]).
-spec largest_magic_square(Grid :: [[integer()]]) -> integer().
largest_magic_square(Grid) ->
    RowsTuples = [list_to_tuple(Row) || Row <- Grid],
    GridT = list_to_tuple(RowsTuples),
    M = length(Grid),
    N = case Grid of [] -> 0; [First|_] -> length(First) end,
    MaxK = erlang:min(M, N),
    largest_magic_square_loop(MaxK, GridT, M, N).

largest_magic_square_loop(K, _GT, _M, _N) when K == 0 ->
    0;
largest_magic_square_loop(K, GT, M, N) ->
    case find_k(K, GT, M, N) of
        true -> K;
        false -> largest_magic_square_loop(K - 1, GT, M, N)
    end.

find_k(K, GT, M, N) ->
    MaxI = M - K,
    MaxJ = N - K,
    find_i(0, MaxI, K, GT, MaxJ).

find_i(I, MaxI, _K, _GT, _MaxJ) when I > MaxI ->
    false;
find_i(I, MaxI, K, GT, MaxJ) ->
    case find_j(I, 0, MaxJ, K, GT) of
        true -> true;
        false -> find_i(I + 1, MaxI, K, GT, MaxJ)
    end.

find_j(_I, J, MaxJ, _K, _GT) when J > MaxJ ->
    false;
find_j(I, J, MaxJ, K, GT) ->
    case is_magic(I, J, K, GT) of
        true -> true;
        false -> find_j(I, J + 1, MaxJ, K, GT)
    end.

is_magic(I, J, K, GT) ->
    Target = sum_row(GT, I, J, K),
    case check_rows(I, J, K, Target, GT) of
        false -> false;
        true ->
            case check_cols(I, J, K, Target, GT) of
                false -> false;
                true ->
                    D1 = sum_diag_main(GT, I, J, K),
                    D2 = sum_diag_anti(GT, I, J, K),
                    D1 =:= Target andalso D2 =:= Target
            end
    end.

check_rows(I, J, K, Target, GT) ->
    check_rows_loop(0, K, I, J, Target, GT).

check_rows_loop(R, K, _I, _J, _Target, _GT) when R == K ->
    true;
check_rows_loop(R, K, I, J, Target, GT) ->
    Sum = sum_row(GT, I + R, J, K),
    if
        Sum =:= Target -> check_rows_loop(R + 1, K, I, J, Target, GT);
        true -> false
    end.

check_cols(I, J, K, Target, GT) ->
    check_cols_loop(0, K, I, J, Target, GT).

check_cols_loop(C, K, _I, _J, _Target, _GT) when C == K ->
    true;
check_cols_loop(C, K, I, J, Target, GT) ->
    Sum = sum_col(GT, I, J + C, K),
    if
        Sum =:= Target -> check_cols_loop(C + 1, K, I, J, Target, GT);
        true -> false
    end.

sum_row(GT, I, J, K) ->
    Row = element(I + 1, GT),
    sum_row_loop(Row, J, K, 0).

sum_row_loop(_Row, _Pos, 0, Acc) ->
    Acc;
sum_row_loop(Row, Pos, Count, Acc) ->
    Val = element(Pos + 1, Row),
    sum_row_loop(Row, Pos + 1, Count - 1, Acc + Val).

sum_col(GT, I, J, K) ->
    sum_col_loop(I, J, K, 0, GT).

sum_col_loop(_I, _J, 0, Acc, _GT) ->
    Acc;
sum_col_loop(I, J, Count, Acc, GT) ->
    Row = element(I + 1, GT),
    Val = element(J + 1, Row),
    sum_col_loop(I + 1, J, Count - 1, Acc + Val, GT).

sum_diag_main(GT, I, J, K) ->
    sum_diag_main_loop(0, K, I, J, GT, 0).

sum_diag_main_loop(Off, K, _I, _J, _GT, Acc) when Off == K ->
    Acc;
sum_diag_main_loop(Off, K, I, J, GT, Acc) ->
    Val = get_elem(GT, I + Off, J + Off),
    sum_diag_main_loop(Off + 1, K, I, J, GT, Acc + Val).

sum_diag_anti(GT, I, J, K) ->
    sum_diag_anti_loop(0, K, I, J, GT, 0).

sum_diag_anti_loop(Off, K, _I, _J, _GT, Acc) when Off == K ->
    Acc;
sum_diag_anti_loop(Off, K, I, J, GT, Acc) ->
    Val = get_elem(GT, I + Off, J + K - 1 - Off),
    sum_diag_anti_loop(Off + 1, K, I, J, GT, Acc + Val).

get_elem(GT, I, J) ->
    Row = element(I + 1, GT),
    element(J + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_magic_square(grid :: [[integer]]) :: integer
  def largest_magic_square(grid) do
    m = length(grid)
    n = length(hd(grid))
    row_ps = build_row_prefix(grid)
    col_ps = build_col_prefix(grid)

    max_k = min(m, n)
    find_max(max_k, grid, row_ps, col_ps, m, n)
  end

  defp find_max(0, _grid, _row_ps, _col_ps, _m, _n), do: 1
  defp find_max(k, grid, row_ps, col_ps, m, n) do
    if exists_magic_of_size?(grid, row_ps, col_ps, m, n, k) do
      k
    else
      find_max(k - 1, grid, row_ps, col_ps, m, n)
    end
  end

  defp exists_magic_of_size?(grid, row_ps, col_ps, m, n, k) do
    max_r = m - k
    max_c = n - k

    Enum.any?(0..max_r, fn r ->
      Enum.any?(0..max_c, fn c ->
        magic_square_at?(grid, row_ps, col_ps, r, c, k)
      end)
    end)
  end

  defp magic_square_at?(grid, row_ps, col_ps, r, c, k) do
    target = get_row_sum(row_ps, r, c, c + k - 1)

    rows_ok =
      Enum.all?(0..(k - 1), fn i ->
        get_row_sum(row_ps, r + i, c, c + k - 1) == target
      end)

    if not rows_ok do
      false
    else
      cols_ok =
        Enum.all?(0..(k - 1), fn j ->
          get_col_sum(col_ps, c + j, r, r + k - 1) == target
        end)

      if not cols_ok do
        false
      else
        diag1 = diagonal_sum(grid, r, c, k, :main)
        diag2 = diagonal_sum(grid, r, c, k, :anti)
        diag1 == target and diag2 == target
      end
    end
  end

  defp get_row_sum(row_ps, row_idx, col_start, col_end) do
    ps = Enum.at(row_ps, row_idx)
    Enum.at(ps, col_end + 1) - Enum.at(ps, col_start)
  end

  defp get_col_sum(col_ps, col_idx, row_start, row_end) do
    cp = Enum.at(col_ps, col_idx)
    Enum.at(cp, row_end + 1) - Enum.at(cp, row_start)
  end

  defp diagonal_sum(grid, r, c, k, :main) do
    Enum.reduce(0..(k - 1), 0, fn offset, acc ->
      row = Enum.at(grid, r + offset)
      val = Enum.at(row, c + offset)
      acc + val
    end)
  end

  defp diagonal_sum(grid, r, c, k, :anti) do
    Enum.reduce(0..(k - 1), 0, fn offset, acc ->
      row = Enum.at(grid, r + offset)
      val = Enum.at(row, c + k - 1 - offset)
      acc + val
    end)
  end

  defp build_row_prefix(grid) do
    Enum.map(grid, fn row ->
      {list_rev, _} =
        Enum.reduce(row, {[0], 0}, fn val, {acc, sum} ->
          new_sum = sum + val
          {[new_sum | acc], new_sum}
        end)

      Enum.reverse(list_rev)
    end)
  end

  defp build_col_prefix(grid) do
    n = length(hd(grid))

    for j <- 0..(n - 1) do
      {list_rev, _} =
        Enum.reduce(grid, {[0], 0}, fn row, {acc, sum} ->
          val = Enum.at(row, j)
          new_sum = sum + val
          {[new_sum | acc], new_sum}
        end)

      Enum.reverse(list_rev)
    end
  end
end
```

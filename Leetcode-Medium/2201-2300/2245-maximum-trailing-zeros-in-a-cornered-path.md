# 2245. Maximum Trailing Zeros in a Cornered Path

## Cpp

```cpp
class Solution {
public:
    int maxTrailingZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> cnt2(m, vector<int>(n));
        vector<vector<int>> cnt5(m, vector<int>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int x = grid[i][j];
                while (x % 2 == 0) { cnt2[i][j]++; x /= 2; }
                while (x % 5 == 0) { cnt5[i][j]++; x /= 5; }
            }
        }
        // row prefix sums
        vector<vector<int>> preRow2(m, vector<int>(n + 1, 0));
        vector<vector<int>> preRow5(m, vector<int>(n + 1, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                preRow2[i][j + 1] = preRow2[i][j] + cnt2[i][j];
                preRow5[i][j + 1] = preRow5[i][j] + cnt5[i][j];
            }
        }
        // column prefix sums
        vector<vector<int>> preCol2(m + 1, vector<int>(n, 0));
        vector<vector<int>> preCol5(m + 1, vector<int>(n, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                preCol2[i + 1][j] = preCol2[i][j] + cnt2[i][j];
                preCol5[i + 1][j] = preCol5[i][j] + cnt5[i][j];
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int up2   = preCol2[i + 1][j];
                int down2 = preCol2[m][j] - preCol2[i][j];
                int left2 = preRow2[i][j + 1];
                int right2= preRow2[i][n] - preRow2[i][j];

                int up5   = preCol5[i + 1][j];
                int down5 = preCol5[m][j] - preCol5[i][j];
                int left5 = preRow5[i][j + 1];
                int right5= preRow5[i][n] - preRow5[i][j];

                // up + left
                {
                    int tot2 = up2 + left2 - cnt2[i][j];
                    int tot5 = up5 + left5 - cnt5[i][j];
                    ans = max(ans, min(tot2, tot5));
                }
                // up + right
                {
                    int tot2 = up2 + right2 - cnt2[i][j];
                    int tot5 = up5 + right5 - cnt5[i][j];
                    ans = max(ans, min(tot2, tot5));
                }
                // down + left
                {
                    int tot2 = down2 + left2 - cnt2[i][j];
                    int tot5 = down5 + left5 - cnt5[i][j];
                    ans = max(ans, min(tot2, tot5));
                }
                // down + right
                {
                    int tot2 = down2 + right2 - cnt2[i][j];
                    int tot5 = down5 + right5 - cnt5[i][j];
                    ans = max(ans, min(tot2, tot5));
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
    public int maxTrailingZeros(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int[][] cnt2 = new int[m][n];
        int[][] cnt5 = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                int c2 = 0, c5 = 0;
                while ((val & 1) == 0) { // faster check for even
                    c2++;
                    val >>= 1;
                }
                while (val % 5 == 0) {
                    c5++;
                    val /= 5;
                }
                cnt2[i][j] = c2;
                cnt5[i][j] = c5;
            }
        }

        int[][] rowPref2 = new int[m][n + 1];
        int[][] rowPref5 = new int[m][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowPref2[i][j + 1] = rowPref2[i][j] + cnt2[i][j];
                rowPref5[i][j + 1] = rowPref5[i][j] + cnt5[i][j];
            }
        }

        int[][] colPref2 = new int[m + 1][n];
        int[][] colPref5 = new int[m + 1][n];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                colPref2[i + 1][j] = colPref2[i][j] + cnt2[i][j];
                colPref5[i + 1][j] = colPref5[i][j] + cnt5[i][j];
            }
        }

        int best = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int up2 = colPref2[i + 1][j];
                int down2 = colPref2[m][j] - colPref2[i][j];
                int left2 = rowPref2[i][j + 1];
                int right2 = rowPref2[i][n] - rowPref2[i][j];

                int up5 = colPref5[i + 1][j];
                int down5 = colPref5[m][j] - colPref5[i][j];
                int left5 = rowPref5[i][j + 1];
                int right5 = rowPref5[i][n] - rowPref5[i][j];

                // up + left
                best = Math.max(best, Math.min(up2 + left2 - cnt2[i][j], up5 + left5 - cnt5[i][j]));
                // up + right
                best = Math.max(best, Math.min(up2 + right2 - cnt2[i][j], up5 + right5 - cnt5[i][j]));
                // down + left
                best = Math.max(best, Math.min(down2 + left2 - cnt2[i][j], down5 + left5 - cnt5[i][j]));
                // down + right
                best = Math.max(best, Math.min(down2 + right2 - cnt2[i][j], down5 + right5 - cnt5[i][j]));
            }
        }

        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        cnt2 = [[0]*n for _ in range(m)]
        cnt5 = [[0]*n for _ in range(m)]

        def factor_counts(x):
            c2 = c5 = 0
            while x % 2 == 0:
                c2 += 1
                x //= 2
            while x % 5 == 0:
                c5 += 1
                x //= 5
            return c2, c5

        for i in range(m):
            for j in range(n):
                cnt2[i][j], cnt5[i][j] = factor_counts(grid[i][j])

        # row prefix sums
        rowPref2 = [[0]*n for _ in range(m)]
        rowPref5 = [[0]*n for _ in range(m)]
        for i in range(m):
            s2 = s5 = 0
            for j in range(n):
                s2 += cnt2[i][j]
                s5 += cnt5[i][j]
                rowPref2[i][j] = s2
                rowPref5[i][j] = s5

        # column prefix sums
        colPref2 = [[0]*n for _ in range(m)]
        colPref5 = [[0]*n for _ in range(m)]
        for j in range(n):
            s2 = s5 = 0
            for i in range(m):
                s2 += cnt2[i][j]
                s5 += cnt5[i][j]
                colPref2[i][j] = s2
                colPref5[i][j] = s5

        ans = 0

        # straight rows
        for i in range(m):
            total2 = rowPref2[i][n-1]
            total5 = rowPref5[i][n-1]
            ans = max(ans, min(total2, total5))

        # straight columns
        for j in range(n):
            total2 = colPref2[m-1][j]
            total5 = colPref5[m-1][j]
            ans = max(ans, min(total2, total5))

        for i in range(m):
            for j in range(n):
                c2 = cnt2[i][j]
                c5 = cnt5[i][j]

                up2 = colPref2[i][j]
                up5 = colPref5[i][j]

                down2 = colPref2[m-1][j] - (colPref2[i-1][j] if i > 0 else 0)
                down5 = colPref5[m-1][j] - (colPref5[i-1][j] if i > 0 else 0)

                left2 = rowPref2[i][j]
                left5 = rowPref5[i][j]

                right2 = rowPref2[i][n-1] - (rowPref2[i][j-1] if j > 0 else 0)
                right5 = rowPref5[i][n-1] - (rowPref5[i][j-1] if j > 0 else 0)

                # up + left
                total2 = up2 + left2 - c2
                total5 = up5 + left5 - c5
                ans = max(ans, min(total2, total5))

                # up + right
                total2 = up2 + right2 - c2
                total5 = up5 + right5 - c5
                ans = max(ans, min(total2, total5))

                # down + left
                total2 = down2 + left2 - c2
                total5 = down5 + left5 - c5
                ans = max(ans, min(total2, total5))

                # down + right
                total2 = down2 + right2 - c2
                total5 = down5 + right5 - c5
                ans = max(ans, min(total2, total5))

        return ans
```

## Python3

```python
class Solution:
    def maxTrailingZeros(self, grid):
        from typing import List
        m, n = len(grid), len(grid[0])
        cnt2 = [[0]*n for _ in range(m)]
        cnt5 = [[0]*n for _ in range(m)]
        for i in range(m):
            row = grid[i]
            for j in range(n):
                v = row[j]
                c2 = c5 = 0
                while v % 2 == 0:
                    v //= 2
                    c2 += 1
                while v % 5 == 0:
                    v //= 5
                    c5 += 1
                cnt2[i][j] = c2
                cnt5[i][j] = c5

        up2 = [[0]*n for _ in range(m)]
        up5 = [[0]*n for _ in range(m)]
        left2 = [[0]*n for _ in range(m)]
        left5 = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                up2[i][j] = cnt2[i][j] + (up2[i-1][j] if i > 0 else 0)
                up5[i][j] = cnt5[i][j] + (up5[i-1][j] if i > 0 else 0)
                left2[i][j] = cnt2[i][j] + (left2[i][j-1] if j > 0 else 0)
                left5[i][j] = cnt5[i][j] + (left5[i][j-1] if j > 0 else 0)

        col_total2 = [up2[m-1][j] for j in range(n)]
        col_total5 = [up5[m-1][j] for j in range(n)]
        row_total2 = [left2[i][n-1] for i in range(m)]
        row_total5 = [left5[i][n-1] for i in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                c2 = cnt2[i][j]
                c5 = cnt5[i][j]

                up_sum2 = up2[i][j]
                up_sum5 = up5[i][j]
                down_sum2 = col_total2[j] - (up2[i-1][j] if i > 0 else 0)
                down_sum5 = col_total5[j] - (up5[i-1][j] if i > 0 else 0)

                left_sum2 = left2[i][j]
                left_sum5 = left5[i][j]
                right_sum2 = row_total2[i] - (left2[i][j-1] if j > 0 else 0)
                right_sum5 = row_total5[i] - (left5[i][j-1] if j > 0 else 0)

                # four L-shaped combos
                combos = [
                    (up_sum2, up_sum5, left_sum2, left_sum5),
                    (up_sum2, up_sum5, right_sum2, right_sum5),
                    (down_sum2, down_sum5, left_sum2, left_sum5),
                    (down_sum2, down_sum5, right_sum2, right_sum5)
                ]
                for a2, a5, b2, b5 in combos:
                    total2 = a2 + b2 - c2
                    total5 = a5 + b5 - c5
                    ans = max(ans, min(total2, total5))
        return ans
```

## C

```c
int maxTrailingZeros(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    if (m == 0) return 0;
    int n = gridColSize[0];
    int totalCells = m * n;

    // store exponents of 2 and 5 for each cell
    int *cnt2 = (int *)malloc(totalCells * sizeof(int));
    int *cnt5 = (int *)malloc(totalCells * sizeof(int));

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int val = grid[i][j];
            int c2 = 0, c5 = 0;
            while ((val & 1) == 0 && val % 2 == 0) { // faster even check
                ++c2;
                val >>= 1;
            }
            while (val % 5 == 0) {
                ++c5;
                val /= 5;
            }
            cnt2[i * n + j] = c2;
            cnt5[i * n + j] = c5;
        }
    }

    // row prefix sums
    int *row2 = (int *)malloc(m * (n + 1) * sizeof(int));
    int *row5 = (int *)malloc(m * (n + 1) * sizeof(int));
    for (int i = 0; i < m; ++i) {
        row2[i * (n + 1)] = 0;
        row5[i * (n + 1)] = 0;
        for (int j = 0; j < n; ++j) {
            int idx = i * n + j;
            row2[i * (n + 1) + j + 1] = row2[i * (n + 1) + j] + cnt2[idx];
            row5[i * (n + 1) + j + 1] = row5[i * (n + 1) + j] + cnt5[idx];
        }
    }

    // column prefix sums
    int *col2 = (int *)malloc((m + 1) * n * sizeof(int));
    int *col5 = (int *)malloc((m + 1) * n * sizeof(int));
    for (int j = 0; j < n; ++j) {
        col2[j] = 0;
        col5[j] = 0;
        for (int i = 0; i < m; ++i) {
            int idx = i * n + j;
            col2[(i + 1) * n + j] = col2[i * n + j] + cnt2[idx];
            col5[(i + 1) * n + j] = col5[i * n + j] + cnt5[idx];
        }
    }

    int answer = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int idx = i * n + j;
            int cur2 = cnt2[idx];
            int cur5 = cnt5[idx];

            // directional sums excluding current cell
            int up2   = col2[i * n + j];
            int up5   = col5[i * n + j];
            int down2 = col2[m * n + j] - col2[(i + 1) * n + j];
            int down5 = col5[m * n + j] - col5[(i + 1) * n + j];

            int left2   = row2[i * (n + 1) + j];
            int left5   = row5[i * (n + 1) + j];
            int right2  = row2[i * (n + 1) + n] - row2[i * (n + 1) + j + 1];
            int right5  = row5[i * (n + 1) + n] - row5[i * (n + 1) + j + 1];

            // straight lines
            int total2, total5, tz;
            total2 = cur2 + up2;   total5 = cur5 + up5;   tz = total2 < total5 ? total2 : total5; if (tz > answer) answer = tz;
            total2 = cur2 + down2; total5 = cur5 + down5; tz = total2 < total5 ? total2 : total5; if (tz > answer) answer = tz;
            total2 = cur2 + left2; total5 = cur5 + left5; tz = total2 < total5 ? total2 : total5; if (tz > answer) answer = tz;
            total2 = cur2 + right2;total5 = cur5 + right5;tz = total2 < total5 ? total2 : total5; if (tz > answer) answer = tz;

            // L-shaped paths
            // up + left
            total2 = cur2 + up2 + left2;
            total5 = cur5 + up5 + left5;
            tz = total2 < total5 ? total2 : total5;
            if (tz > answer) answer = tz;
            // up + right
            total2 = cur2 + up2 + right2;
            total5 = cur5 + up5 + right5;
            tz = total2 < total5 ? total2 : total5;
            if (tz > answer) answer = tz;
            // down + left
            total2 = cur2 + down2 + left2;
            total5 = cur5 + down5 + left5;
            tz = total2 < total5 ? total2 : total5;
            if (tz > answer) answer = tz;
            // down + right
            total2 = cur2 + down2 + right2;
            total5 = cur5 + down5 + right5;
            tz = total2 < total5 ? total2 : total5;
            if (tz > answer) answer = tz;
        }
    }

    free(cnt2);
    free(cnt5);
    free(row2);
    free(row5);
    free(col2);
    free(col5);

    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxTrailingZeros(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        int[,] cnt2 = new int[m, n];
        int[,] cnt5 = new int[m, n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                int c2 = 0, c5 = 0;
                while ((val & 1) == 0) { // faster check for even
                    c2++;
                    val >>= 1;
                }
                while (val % 5 == 0) {
                    c5++;
                    val /= 5;
                }
                cnt2[i, j] = c2;
                cnt5[i, j] = c5;
            }
        }

        // Row prefix sums
        int[,] rowPref2 = new int[m, n + 1];
        int[,] rowPref5 = new int[m, n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowPref2[i, j + 1] = rowPref2[i, j] + cnt2[i, j];
                rowPref5[i, j + 1] = rowPref5[i, j] + cnt5[i, j];
            }
        }

        // Column prefix sums
        int[,] colPref2 = new int[m + 1, n];
        int[,] colPref5 = new int[m + 1, n];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                colPref2[i + 1, j] = colPref2[i, j] + cnt2[i, j];
                colPref5[i + 1, j] = colPref5[i, j] + cnt5[i, j];
            }
        }

        int answer = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int c2 = cnt2[i, j];
                int c5 = cnt5[i, j];

                // sums in four directions including the current cell
                int up2 = colPref2[i + 1, j];
                int down2 = colPref2[m, j] - colPref2[i, j];
                int left2 = rowPref2[i, j + 1];
                int right2 = rowPref2[i, n] - rowPref2[i, j];

                int up5 = colPref5[i + 1, j];
                int down5 = colPref5[m, j] - colPref5[i, j];
                int left5 = rowPref5[i, j + 1];
                int right5 = rowPref5[i, n] - rowPref5[i, j];

                // up + left
                int total2 = up2 + left2 - c2;
                int total5 = up5 + left5 - c5;
                answer = Math.Max(answer, Math.Min(total2, total5));

                // up + right
                total2 = up2 + right2 - c2;
                total5 = up5 + right5 - c5;
                answer = Math.Max(answer, Math.Min(total2, total5));

                // down + left
                total2 = down2 + left2 - c2;
                total5 = down5 + left5 - c5;
                answer = Math.Max(answer, Math.Min(total2, total5));

                // down + right
                total2 = down2 + right2 - c2;
                total5 = down5 + right5 - c5;
                answer = Math.Max(answer, Math.Min(total2, total5));
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
var maxTrailingZeros = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    // helper to count factor 2 and 5
    const cnt2 = Array.from({ length: m }, () => new Array(n));
    const cnt5 = Array.from({ length: m }, () => new Array(n));

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            let val = grid[i][j];
            let c2 = 0, c5 = 0;
            while ((val & 1) === 0) { // faster check for factor 2
                c2++;
                val >>= 1;
            }
            while (val % 5 === 0) {
                c5++;
                val /= 5;
            }
            cnt2[i][j] = c2;
            cnt5[i][j] = c5;
        }
    }

    // row prefix sums
    const rowPref2 = Array.from({ length: m }, () => new Array(n));
    const rowPref5 = Array.from({ length: m }, () => new Array(n));
    for (let i = 0; i < m; ++i) {
        let sum2 = 0, sum5 = 0;
        for (let j = 0; j < n; ++j) {
            sum2 += cnt2[i][j];
            sum5 += cnt5[i][j];
            rowPref2[i][j] = sum2;
            rowPref5[i][j] = sum5;
        }
    }

    // column prefix sums
    const colPref2 = Array.from({ length: m }, () => new Array(n));
    const colPref5 = Array.from({ length: m }, () => new Array(n));
    for (let j = 0; j < n; ++j) {
        let sum2 = 0, sum5 = 0;
        for (let i = 0; i < m; ++i) {
            sum2 += cnt2[i][j];
            sum5 += cnt5[i][j];
            colPref2[i][j] = sum2;
            colPref5[i][j] = sum5;
        }
    }

    let ans = 0;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const c2 = cnt2[i][j];
            const c5 = cnt5[i][j];

            // up and down sums
            const up2 = colPref2[i][j];
            const up5 = colPref5[i][j];
            const down2 = colPref2[m - 1][j] - (i > 0 ? colPref2[i - 1][j] : 0);
            const down5 = colPref5[m - 1][j] - (i > 0 ? colPref5[i - 1][j] : 0);

            // left and right sums
            const left2 = rowPref2[i][j];
            const left5 = rowPref5[i][j];
            const right2 = rowPref2[i][n - 1] - (j > 0 ? rowPref2[i][j - 1] : 0);
            const right5 = rowPref5[i][n - 1] - (j > 0 ? rowPref5[i][j - 1] : 0);

            // four L-shaped possibilities
            let total2, total5;

            // up + left
            total2 = up2 + left2 - c2;
            total5 = up5 + left5 - c5;
            ans = Math.max(ans, Math.min(total2, total5));

            // up + right
            total2 = up2 + right2 - c2;
            total5 = up5 + right5 - c5;
            ans = Math.max(ans, Math.min(total2, total5));

            // down + left
            total2 = down2 + left2 - c2;
            total5 = down5 + left5 - c5;
            ans = Math.max(ans, Math.min(total2, total5));

            // down + right
            total2 = down2 + right2 - c2;
            total5 = down5 + right5 - c5;
            ans = Math.max(ans, Math.min(total2, total5));
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxTrailingZeros(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    const twos: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    const fives: number[][] = Array.from({ length: m }, () => Array(n).fill(0));

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let val = grid[i][j];
            let c2 = 0, c5 = 0;
            while (val % 2 === 0) { c2++; val /= 2; }
            while (val % 5 === 0) { c5++; val /= 5; }
            twos[i][j] = c2;
            fives[i][j] = c5;
        }
    }

    const rowTwo: number[][] = Array.from({ length: m }, () => Array(n + 1).fill(0));
    const rowFive: number[][] = Array.from({ length: m }, () => Array(n + 1).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            rowTwo[i][j + 1] = rowTwo[i][j] + twos[i][j];
            rowFive[i][j + 1] = rowFive[i][j] + fives[i][j];
        }
    }

    const colTwo: number[][] = Array.from({ length: m + 1 }, () => Array(n).fill(0));
    const colFive: number[][] = Array.from({ length: m + 1 }, () => Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            colTwo[i + 1][j] = colTwo[i][j] + twos[i][j];
            colFive[i + 1][j] = colFive[i][j] + fives[i][j];
        }
    }

    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const up2 = colTwo[i + 1][j];
            const up5 = colFive[i + 1][j];
            const down2 = colTwo[m][j] - colTwo[i][j];
            const down5 = colFive[m][j] - colFive[i][j];
            const left2 = rowTwo[i][j + 1];
            const left5 = rowFive[i][j + 1];
            const right2 = rowTwo[i][n] - rowTwo[i][j];
            const right5 = rowFive[i][n] - rowFive[i][j];

            const cell2 = twos[i][j];
            const cell5 = fives[i][j];

            // up + left
            let total2 = up2 + left2 - cell2;
            let total5 = up5 + left5 - cell5;
            ans = Math.max(ans, Math.min(total2, total5));

            // up + right
            total2 = up2 + right2 - cell2;
            total5 = up5 + right5 - cell5;
            ans = Math.max(ans, Math.min(total2, total5));

            // down + left
            total2 = down2 + left2 - cell2;
            total5 = down5 + left5 - cell5;
            ans = Math.max(ans, Math.min(total2, total5));

            // down + right
            total2 = down2 + right2 - cell2;
            total5 = down5 + right5 - cell5;
            ans = Math.max(ans, Math.min(total2, total5));
        }
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
    function maxTrailingZeros($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        // store exponents of 2 and 5 for each cell
        $cnt2 = array_fill(0, $m, []);
        $cnt5 = array_fill(0, $m, []);

        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $val = $grid[$i][$j];
                $c2 = 0;
                while (($val & 1) == 0) { // faster check for even
                    $c2++;
                    $val >>= 1;
                }
                // after removing all factors of 2, need original value for factor 5
                $val = $grid[$i][$j];
                $c5 = 0;
                while ($val % 5 == 0) {
                    $c5++;
                    $val /= 5;
                }
                $cnt2[$i][$j] = $c2;
                $cnt5[$i][$j] = $c5;
            }
        }

        // row prefix sums
        $rowPref2 = array_fill(0, $m, []);
        $rowPref5 = array_fill(0, $m, []);
        for ($i = 0; $i < $m; ++$i) {
            $pref2 = array_fill(0, $n + 1, 0);
            $pref5 = array_fill(0, $n + 1, 0);
            for ($j = 0; $j < $n; ++$j) {
                $pref2[$j + 1] = $pref2[$j] + $cnt2[$i][$j];
                $pref5[$j + 1] = $pref5[$j] + $cnt5[$i][$j];
            }
            $rowPref2[$i] = $pref2;
            $rowPref5[$i] = $pref5;
        }

        // column prefix sums
        $colPref2 = array_fill(0, $m + 1, array_fill(0, $n, 0));
        $colPref5 = array_fill(0, $m + 1, array_fill(0, $n, 0));
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $colPref2[$i + 1][$j] = $colPref2[$i][$j] + $cnt2[$i][$j];
                $colPref5[$i + 1][$j] = $colPref5[$i][$j] + $cnt5[$i][$j];
            }
        }

        $ans = 0;
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $c2 = $cnt2[$i][$j];
                $c5 = $cnt5[$i][$j];

                // up, down, left, right sums
                $up2   = $colPref2[$i + 1][$j];
                $down2 = $colPref2[$m][$j] - $colPref2[$i][$j];
                $left2 = $rowPref2[$i][$j + 1];
                $right2= $rowPref2[$i][$n] - $rowPref2[$i][$j];

                $up5   = $colPref5[$i + 1][$j];
                $down5 = $colPref5[$m][$j] - $colPref5[$i][$j];
                $left5 = $rowPref5[$i][$j + 1];
                $right5= $rowPref5[$i][$n] - $rowPref5[$i][$j];

                // four L-shaped possibilities
                $tot2 = $up2 + $left2 - $c2;
                $tot5 = $up5 + $left5 - $c5;
                $ans = max($ans, min($tot2, $tot5));

                $tot2 = $up2 + $right2 - $c2;
                $tot5 = $up5 + $right5 - $c5;
                $ans = max($ans, min($tot2, $tot5));

                $tot2 = $down2 + $left2 - $c2;
                $tot5 = $down5 + $left5 - $c5;
                $ans = max($ans, min($tot2, $tot5));

                $tot2 = $down2 + $right2 - $c2;
                $tot5 = $down5 + $right5 - $c5;
                $ans = max($ans, min($tot2, $tot5));
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxTrailingZeros(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var cnt2 = Array(repeating: Array(repeating: 0, count: n), count: m)
        var cnt5 = Array(repeating: Array(repeating: 0, count: n), count: m)
        for i in 0..<m {
            for j in 0..<n {
                var v = grid[i][j]
                var c2 = 0
                while v % 2 == 0 {
                    c2 += 1
                    v /= 2
                }
                var c5 = 0
                while v % 5 == 0 {
                    c5 += 1
                    v /= 5
                }
                cnt2[i][j] = c2
                cnt5[i][j] = c5
            }
        }
        var rowPref2 = Array(repeating: Array(repeating: 0, count: n), count: m)
        var rowPref5 = Array(repeating: Array(repeating: 0, count: n), count: m)
        for i in 0..<m {
            var sum2 = 0
            var sum5 = 0
            for j in 0..<n {
                sum2 += cnt2[i][j]
                sum5 += cnt5[i][j]
                rowPref2[i][j] = sum2
                rowPref5[i][j] = sum5
            }
        }
        var colPref2 = Array(repeating: Array(repeating: 0, count: n), count: m)
        var colPref5 = Array(repeating: Array(repeating: 0, count: n), count: m)
        for j in 0..<n {
            var sum2 = 0
            var sum5 = 0
            for i in 0..<m {
                sum2 += cnt2[i][j]
                sum5 += cnt5[i][j]
                colPref2[i][j] = sum2
                colPref5[i][j] = sum5
            }
        }
        var answer = 0
        for i in 0..<m {
            for j in 0..<n {
                let c2 = cnt2[i][j]
                let c5 = cnt5[i][j]
                // up direction sums (including current cell)
                let up2 = colPref2[i][j]
                let up5 = colPref5[i][j]
                // down direction sums
                let totalCol2 = colPref2[m - 1][j]
                let totalCol5 = colPref5[m - 1][j]
                let down2 = totalCol2 - (i > 0 ? colPref2[i - 1][j] : 0)
                let down5 = totalCol5 - (i > 0 ? colPref5[i - 1][j] : 0)
                // left direction sums
                let left2 = rowPref2[i][j]
                let left5 = rowPref5[i][j]
                // right direction sums
                let totalRow2 = rowPref2[i][n - 1]
                let totalRow5 = rowPref5[i][n - 1]
                let right2 = totalRow2 - (j > 0 ? rowPref2[i][j - 1] : 0)
                let right5 = totalRow5 - (j > 0 ? rowPref5[i][j - 1] : 0)
                
                var t2 = up2 + left2 - c2
                var t5 = up5 + left5 - c5
                answer = max(answer, min(t2, t5))
                
                t2 = up2 + right2 - c2
                t5 = up5 + right5 - c5
                answer = max(answer, min(t2, t5))
                
                t2 = down2 + left2 - c2
                t5 = down5 + left5 - c5
                answer = max(answer, min(t2, t5))
                
                t2 = down2 + right2 - c2
                t5 = down5 + right5 - c5
                answer = max(answer, min(t2, t5))
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTrailingZeros(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size

        // count of factor 2 and 5 for each cell
        val cnt2 = Array(m) { IntArray(n) }
        val cnt5 = Array(m) { IntArray(n) }

        fun factorCounts(v: Int): Pair<Int, Int> {
            var x = v
            var c2 = 0
            while (x % 2 == 0) {
                c2++
                x /= 2
            }
            var c5 = 0
            while (x % 5 == 0) {
                c5++
                x /= 5
            }
            return Pair(c2, c5)
        }

        // row prefix sums for 2 and 5
        val rowPref2 = Array(m) { IntArray(n) }
        val rowPref5 = Array(m) { IntArray(n) }
        // column prefix sums for 2 and 5
        val colPref2 = Array(m) { IntArray(n) }
        val colPref5 = Array(m) { IntArray(n) }

        // fill counts and row prefixes
        for (i in 0 until m) {
            var sum2 = 0
            var sum5 = 0
            for (j in 0 until n) {
                val (c2, c5) = factorCounts(grid[i][j])
                cnt2[i][j] = c2
                cnt5[i][j] = c5
                sum2 += c2
                sum5 += c5
                rowPref2[i][j] = sum2
                rowPref5[i][j] = sum5
            }
        }

        // fill column prefixes
        for (j in 0 until n) {
            var sum2 = 0
            var sum5 = 0
            for (i in 0 until m) {
                sum2 += cnt2[i][j]
                sum5 += cnt5[i][j]
                colPref2[i][j] = sum2
                colPref5[i][j] = sum5
            }
        }

        // total sums per row and column for quick access
        val rowTotal2 = IntArray(m) { rowPref2[it][n - 1] }
        val rowTotal5 = IntArray(m) { rowPref5[it][n - 1] }
        val colTotal2 = IntArray(n) { colPref2[m - 1][it] }
        val colTotal5 = IntArray(n) { colPref5[m - 1][it] }

        var answer = 0

        for (i in 0 until m) {
            for (j in 0 until n) {
                // up direction includes current cell
                val up2 = colPref2[i][j]
                val up5 = colPref5[i][j]

                // down direction includes current cell
                val down2 = colTotal2[j] - if (i > 0) colPref2[i - 1][j] else 0
                val down5 = colTotal5[j] - if (i > 0) colPref5[i - 1][j] else 0

                // left direction includes current cell
                val left2 = rowPref2[i][j]
                val left5 = rowPref5[i][j]

                // right direction includes current cell
                val right2 = rowTotal2[i] - if (j > 0) rowPref2[i][j - 1] else 0
                val right5 = rowTotal5[i] - if (j > 0) rowPref5[i][j - 1] else 0

                // four L-shaped combos (including straight lines)
                fun eval(a2: Int, a5: Int, b2: Int, b5: Int) {
                    val total2 = a2 + b2 - cnt2[i][j]
                    val total5 = a5 + b5 - cnt5[i][j]
                    answer = maxOf(answer, minOf(total2, total5))
                }

                eval(up2, up5, left2, left5)     // up + left
                eval(up2, up5, right2, right5)   // up + right
                eval(down2, down5, left2, left5) // down + left
                eval(down2, down5, right2, right5) // down + right
            }
        }

        return answer
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  int maxTrailingZeros(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // Count factors of 2 and 5 for each cell
    List<List<int>> cnt2 = List.generate(m, (_) => List.filled(n, 0));
    List<List<int>> cnt5 = List.generate(m, (_) => List.filled(n, 0));

    int countFactor(int x, int p) {
      int c = 0;
      while (x % p == 0) {
        c++;
        x ~/= p;
      }
      return c;
    }

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        int val = grid[i][j];
        cnt2[i][j] = countFactor(val, 2);
        cnt5[i][j] = countFactor(val, 5);
      }
    }

    // Row prefix sums
    List<List<int>> rowPref2 = List.generate(m, (_) => List.filled(n, 0));
    List<List<int>> rowPref5 = List.generate(m, (_) => List.filled(n, 0));
    List<int> rowTotal2 = List.filled(m, 0);
    List<int> rowTotal5 = List.filled(m, 0);

    for (int i = 0; i < m; ++i) {
      int sum2 = 0;
      int sum5 = 0;
      for (int j = 0; j < n; ++j) {
        sum2 += cnt2[i][j];
        sum5 += cnt5[i][j];
        rowPref2[i][j] = sum2;
        rowPref5[i][j] = sum5;
      }
      rowTotal2[i] = sum2;
      rowTotal5[i] = sum5;
    }

    // Column prefix sums
    List<List<int>> colPref2 = List.generate(m, (_) => List.filled(n, 0));
    List<List<int>> colPref5 = List.generate(m, (_) => List.filled(n, 0));
    List<int> colTotal2 = List.filled(n, 0);
    List<int> colTotal5 = List.filled(n, 0);

    for (int j = 0; j < n; ++j) {
      int sum2 = 0;
      int sum5 = 0;
      for (int i = 0; i < m; ++i) {
        sum2 += cnt2[i][j];
        sum5 += cnt5[i][j];
        colPref2[i][j] = sum2;
        colPref5[i][j] = sum5;
      }
      colTotal2[j] = sum2;
      colTotal5[j] = sum5;
    }

    int answer = 0;

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        int up2 = colPref2[i][j];
        int up5 = colPref5[i][j];
        int down2 = colTotal2[j] - (i > 0 ? colPref2[i - 1][j] : 0);
        int down5 = colTotal5[j] - (i > 0 ? colPref5[i - 1][j] : 0);

        int left2 = rowPref2[i][j];
        int left5 = rowPref5[i][j];
        int right2 = rowTotal2[i] - (j > 0 ? rowPref2[i][j - 1] : 0);
        int right5 = rowTotal5[i] - (j > 0 ? rowPref5[i][j - 1] : 0);

        // up + left
        int total2 = up2 + left2 - cnt2[i][j];
        int total5 = up5 + left5 - cnt5[i][j];
        answer = math.max(answer, math.min(total2, total5));

        // up + right
        total2 = up2 + right2 - cnt2[i][j];
        total5 = up5 + right5 - cnt5[i][j];
        answer = math.max(answer, math.min(total2, total5));

        // down + left
        total2 = down2 + left2 - cnt2[i][j];
        total5 = down5 + left5 - cnt5[i][j];
        answer = math.max(answer, math.min(total2, total5));

        // down + right
        total2 = down2 + right2 - cnt2[i][j];
        total5 = down5 + right5 - cnt5[i][j];
        answer = math.max(answer, math.min(total2, total5));
      }
    }

    return answer;
  }
}
```

## Golang

```go
func maxTrailingZeros(grid [][]int) int {
	m, n := len(grid), len(grid[0])

	// Count factors of 2 and 5 for each cell
	cnt2 := make([][]int, m)
	cnt5 := make([][]int, m)
	for i := 0; i < m; i++ {
		cnt2[i] = make([]int, n)
		cnt5[i] = make([]int, n)
		for j := 0; j < n; j++ {
			val := grid[i][j]
			c2, c5 := 0, 0
			for val%2 == 0 {
				c2++
				val /= 2
			}
			for val%5 == 0 {
				c5++
				val /= 5
			}
			cnt2[i][j] = c2
			cnt5[i][j] = c5
		}
	}

	// Prefix sums for rows and columns
	rowPref2 := make([][]int, m)
	rowPref5 := make([][]int, m)
	colPref2 := make([][]int, m)
	colPref5 := make([][]int, m)
	for i := 0; i < m; i++ {
		rowPref2[i] = make([]int, n)
		rowPref5[i] = make([]int, n)
		colPref2[i] = make([]int, n)
		colPref5[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if j == 0 {
				rowPref2[i][j] = cnt2[i][j]
				rowPref5[i][j] = cnt5[i][j]
			} else {
				rowPref2[i][j] = rowPref2[i][j-1] + cnt2[i][j]
				rowPref5[i][j] = rowPref5[i][j-1] + cnt5[i][j]
			}
			if i == 0 {
				colPref2[i][j] = cnt2[i][j]
				colPref5[i][j] = cnt5[i][j]
			} else {
				colPref2[i][j] = colPref2[i-1][j] + cnt2[i][j]
				colPref5[i][j] = colPref5[i-1][j] + cnt5[i][j]
			}
		}
	}

	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			up2, up5 := colPref2[i][j], colPref5[i][j]

			totalCol2, totalCol5 := colPref2[m-1][j], colPref5[m-1][j]
			down2, down5 := 0, 0
			if i > 0 {
				down2 = totalCol2 - colPref2[i-1][j]
				down5 = totalCol5 - colPref5[i-1][j]
			} else {
				down2 = totalCol2
				down5 = totalCol5
			}

			left2, left5 := rowPref2[i][j], rowPref5[i][j]

			totalRow2, totalRow5 := rowPref2[i][n-1], rowPref5[i][n-1]
			right2, right5 := 0, 0
			if j > 0 {
				right2 = totalRow2 - rowPref2[i][j-1]
				right5 = totalRow5 - rowPref5[i][j-1]
			} else {
				right2 = totalRow2
				right5 = totalRow5
			}

			// Four L-shaped paths
			t2 := up2 + left2 - cnt2[i][j]
			t5 := up5 + left5 - cnt5[i][j]
			if v := min(t2, t5); v > ans {
				ans = v
			}
			t2 = up2 + right2 - cnt2[i][j]
			t5 = up5 + right5 - cnt5[i][j]
			if v := min(t2, t5); v > ans {
				ans = v
			}
			t2 = down2 + left2 - cnt2[i][j]
			t5 = down5 + left5 - cnt5[i][j]
			if v := min(t2, t5); v > ans {
				ans = v
			}
			t2 = down2 + right2 - cnt2[i][j]
			t5 = down5 + right5 - cnt5[i][j]
			if v := min(t2, t5); v > ans {
				ans = v
			}

			// Straight lines (no turn)
			if v := min(up2, up5); v > ans {
				ans = v
			}
			if v := min(down2, down5); v > ans {
				ans = v
			}
			if v := min(left2, left5); v > ans {
				ans = v
			}
			if v := min(right2, right5); v > ans {
				ans = v
			}
		}
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def max_trailing_zeros(grid)
  m = grid.size
  n = grid[0].size

  cnt2 = Array.new(m) { Array.new(n, 0) }
  cnt5 = Array.new(m) { Array.new(n, 0) }

  # factor counts for each cell
  (0...m).each do |i|
    row = grid[i]
    (0...n).each do |j|
      v = row[j]
      c2 = 0
      while (v & 1) == 0
        c2 += 1
        v >>= 1
      end
      # after removing powers of 2, count factors of 5
      c5 = 0
      while v % 5 == 0
        c5 += 1
        v /= 5
      end
      cnt2[i][j] = c2
      cnt5[i][j] = c5
    end
  end

  up2 = Array.new(m) { Array.new(n, 0) }
  up5 = Array.new(m) { Array.new(n, 0) }
  down2 = Array.new(m) { Array.new(n, 0) }
  down5 = Array.new(m) { Array.new(n, 0) }
  left2 = Array.new(m) { Array.new(n, 0) }
  left5 = Array.new(m) { Array.new(n, 0) }
  right2 = Array.new(m) { Array.new(n, 0) }
  right5 = Array.new(m) { Array.new(n, 0) }

  # up
  (0...m).each do |i|
    (0...n).each do |j|
      if i == 0
        up2[i][j] = cnt2[i][j]
        up5[i][j] = cnt5[i][j]
      else
        up2[i][j] = up2[i-1][j] + cnt2[i][j]
        up5[i][j] = up5[i-1][j] + cnt5[i][j]
      end
    end
  end

  # down
  (m-1).downto(0) do |i|
    (0...n).each do |j|
      if i == m-1
        down2[i][j] = cnt2[i][j]
        down5[i][j] = cnt5[i][j]
      else
        down2[i][j] = down2[i+1][j] + cnt2[i][j]
        down5[i][j] = down5[i+1][j] + cnt5[i][j]
      end
    end
  end

  # left
  (0...m).each do |i|
    (0...n).each do |j|
      if j == 0
        left2[i][j] = cnt2[i][j]
        left5[i][j] = cnt5[i][j]
      else
        left2[i][j] = left2[i][j-1] + cnt2[i][j]
        left5[i][j] = left5[i][j-1] + cnt5[i][j]
      end
    end
  end

  # right
  (0...m).each do |i|
    (n-1).downto(0) do |j|
      if j == n-1
        right2[i][j] = cnt2[i][j]
        right5[i][j] = cnt5[i][j]
      else
        right2[i][j] = right2[i][j+1] + cnt2[i][j]
        right5[i][j] = right5[i][j+1] + cnt5[i][j]
      end
    end
  end

  ans = 0
  (0...m).each do |i|
    (0...n).each do |j|
      c2 = cnt2[i][j]
      c5 = cnt5[i][j]

      # up + left
      t2 = up2[i][j] + left2[i][j] - c2
      t5 = up5[i][j] + left5[i][j] - c5
      ans = [ans, [t2, t5].min].max

      # up + right
      t2 = up2[i][j] + right2[i][j] - c2
      t5 = up5[i][j] + right5[i][j] - c5
      ans = [ans, [t2, t5].min].max

      # down + left
      t2 = down2[i][j] + left2[i][j] - c2
      t5 = down5[i][j] + left5[i][j] - c5
      ans = [ans, [t2, t5].min].max

      # down + right
      t2 = down2[i][j] + right2[i][j] - c2
      t5 = down5[i][j] + right5[i][j] - c5
      ans = [ans, [t2, t5].min].max
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxTrailingZeros(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length

        val twos = Array.ofDim[Int](m, n)
        val fives = Array.ofDim[Int](m, n)

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                var v = grid(i)(j)
                var cnt2 = 0
                while ((v & 1) == 0) {
                    cnt2 += 1
                    v >>= 1
                }
                var vv = grid(i)(j)
                var cnt5 = 0
                while (vv % 5 == 0 && vv > 0) {
                    cnt5 += 1
                    vv /= 5
                }
                twos(i)(j) = cnt2
                fives(i)(j) = cnt5
            }
        }

        val rowPref2 = Array.ofDim[Int](m, n)
        val rowPref5 = Array.ofDim[Int](m, n)
        for (i <- 0 until m) {
            var sum2 = 0
            var sum5 = 0
            for (j <- 0 until n) {
                sum2 += twos(i)(j)
                sum5 += fives(i)(j)
                rowPref2(i)(j) = sum2
                rowPref5(i)(j) = sum5
            }
        }

        val colPref2 = Array.ofDim[Int](m, n)
        val colPref5 = Array.ofDim[Int](m, n)
        for (j <- 0 until n) {
            var sum2 = 0
            var sum5 = 0
            for (i <- 0 until m) {
                sum2 += twos(i)(j)
                sum5 += fives(i)(j)
                colPref2(i)(j) = sum2
                colPref5(i)(j) = sum5
            }
        }

        var ans = 0
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                val cell2 = twos(i)(j)
                val cell5 = fives(i)(j)

                val up2   = if (i > 0) colPref2(i - 1)(j) else 0
                val up5   = if (i > 0) colPref5(i - 1)(j) else 0
                val down2 = colPref2(m - 1)(j) - colPref2(i)(j)
                val down5 = colPref5(m - 1)(j) - colPref5(i)(j)

                val left2  = if (j > 0) rowPref2(i)(j - 1) else 0
                val left5  = if (j > 0) rowPref5(i)(j - 1) else 0
                val right2 = rowPref2(i)(n - 1) - rowPref2(i)(j)
                val right5 = rowPref5(i)(n - 1) - rowPref5(i)(j)

                var total2 = up2 + left2 + cell2
                var total5 = up5 + left5 + cell5
                ans = math.max(ans, math.min(total2, total5))

                total2 = up2 + right2 + cell2
                total5 = up5 + right5 + cell5
                ans = math.max(ans, math.min(total2, total5))

                total2 = down2 + left2 + cell2
                total5 = down5 + left5 + cell5
                ans = math.max(ans, math.min(total2, total5))

                total2 = down2 + right2 + cell2
                total5 = down5 + right5 + cell5
                ans = math.max(ans, math.min(total2, total5))
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_trailing_zeros(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        // count factors of 2 and 5 for each cell
        let mut cnt2 = vec![vec![0i32; n]; m];
        let mut cnt5 = vec![vec![0i32; n]; m];
        for i in 0..m {
            for j in 0..n {
                let mut v = grid[i][j];
                let mut c2 = 0;
                while v % 2 == 0 {
                    c2 += 1;
                    v /= 2;
                }
                let mut c5 = 0;
                while v % 5 == 0 {
                    c5 += 1;
                    v /= 5;
                }
                cnt2[i][j] = c2;
                cnt5[i][j] = c5;
            }
        }

        // row prefix sums
        let mut row_pre2 = vec![vec![0i32; n]; m];
        let mut row_pre5 = vec![vec![0i32; n]; m];
        for i in 0..m {
            let mut sum2 = 0;
            let mut sum5 = 0;
            for j in 0..n {
                sum2 += cnt2[i][j];
                sum5 += cnt5[i][j];
                row_pre2[i][j] = sum2;
                row_pre5[i][j] = sum5;
            }
        }

        // column prefix sums
        let mut col_pre2 = vec![vec![0i32; n]; m];
        let mut col_pre5 = vec![vec![0i32; n]; m];
        for j in 0..n {
            let mut sum2 = 0;
            let mut sum5 = 0;
            for i in 0..m {
                sum2 += cnt2[i][j];
                sum5 += cnt5[i][j];
                col_pre2[i][j] = sum2;
                col_pre5[i][j] = sum5;
            }
        }

        let mut ans = 0i32;

        for i in 0..m {
            for j in 0..n {
                // sums in four directions
                let up2 = if i > 0 { col_pre2[i - 1][j] } else { 0 };
                let down2 = col_pre2[m - 1][j] - col_pre2[i][j];
                let left2 = if j > 0 { row_pre2[i][j - 1] } else { 0 };
                let right2 = row_pre2[i][n - 1] - row_pre2[i][j];

                let up5 = if i > 0 { col_pre5[i - 1][j] } else { 0 };
                let down5 = col_pre5[m - 1][j] - col_pre5[i][j];
                let left5 = if j > 0 { row_pre5[i][j - 1] } else { 0 };
                let right5 = row_pre5[i][n - 1] - row_pre5[i][j];

                // up + left
                {
                    let total2 = up2 + left2 + cnt2[i][j];
                    let total5 = up5 + left5 + cnt5[i][j];
                    ans = ans.max(total2.min(total5));
                }
                // up + right
                {
                    let total2 = up2 + right2 + cnt2[i][j];
                    let total5 = up5 + right5 + cnt5[i][j];
                    ans = ans.max(total2.min(total5));
                }
                // down + left
                {
                    let total2 = down2 + left2 + cnt2[i][j];
                    let total5 = down5 + left5 + cnt5[i][j];
                    ans = ans.max(total2.min(total5));
                }
                // down + right
                {
                    let total2 = down2 + right2 + cnt2[i][j];
                    let total5 = down5 + right5 + cnt5[i][j];
                    ans = ans.max(total2.min(total5));
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-trailing-zeros grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (zero? rows) 0 (length (car grid))))
         ;; helper to count exponent of p in n
         (count-factor
          (lambda (n p)
            (let loop ((cnt 0) (x n))
              (if (= (remainder x p) 0)
                  (loop (+ cnt 1) (/ x p))
                  cnt))))
         ;; matrices for counts of 2 and 5
         (cnt2 (make-vector rows))
         (cnt5 (make-vector rows)))
    ;; fill cnt2 and cnt5
    (for ([i (in-range rows)])
      (let ((row2 (make-vector cols))
            (row5 (make-vector cols))
            (lst (list-ref grid i)))
        (for ([j (in-range cols)])
          (define val (list-ref lst j))
          (vector-set! row2 j (count-factor val 2))
          (vector-set! row5 j (count-factor val 5)))
        (vector-set! cnt2 i row2)
        (vector-set! cnt5 i row5)))
    ;; prefix sums for rows
    (define rowPref2 (make-vector rows))
    (define rowPref5 (make-vector rows))
    (for ([i (in-range rows)])
      (let ((pref2 (make-vector cols))
            (pref5 (make-vector cols)))
        (for ([j (in-range cols)])
          (define cur2 (vector-ref (vector-ref cnt2 i) j))
          (define cur5 (vector-ref (vector-ref cnt5 i) j))
          (vector-set! pref2 j (+ cur2 (if (> j 0) (vector-ref pref2 (sub1 j)) 0)))
          (vector-set! pref5 j (+ cur5 (if (> j 0) (vector-ref pref5 (sub1 j)) 0))))
        (vector-set! rowPref2 i pref2)
        (vector-set! rowPref5 i pref5)))
    ;; prefix sums for columns
    (define colPref2 (make-vector rows))
    (define colPref5 (make-vector rows))
    (for ([i (in-range rows)])
      (let ((pref2 (make-vector cols))
            (pref5 (make-vector cols)))
        (for ([j (in-range cols)])
          (define cur2 (vector-ref (vector-ref cnt2 i) j))
          (define cur5 (vector-ref (vector-ref cnt5 i) j))
          (vector-set! pref2 j (+ cur2 (if (> i 0) (vector-ref (vector-ref colPref2 (sub1 i)) j) 0)))
          (vector-set! pref5 j (+ cur5 (if (> i 0) (vector-ref (vector-ref colPref5 (sub1 i)) j) 0))))
        (vector-set! colPref2 i pref2)
        (vector-set! colPref5 i pref5)))
    ;; evaluate each elbow
    (let ((ans (make-parameter 0)))
      (for ([i (in-range rows)])
        (for ([j (in-range cols)])
          (define up2   (vector-ref (vector-ref colPref2 i) j))
          (define up5   (vector-ref (vector-ref colPref5 i) j))
          (define down2 (- (vector-ref (vector-ref colPref2 (sub1 rows)) j)
                           (if (> i 0) (vector-ref (vector-ref colPref2 (sub1 i)) j) 0)))
          (define down5 (- (vector-ref (vector-ref colPref5 (sub1 rows)) j)
                           (if (> i 0) (vector-ref (vector-ref colPref5 (sub1 i)) j) 0)))
          (define left2 (vector-ref (vector-ref rowPref2 i) j))
          (define left5 (vector-ref (vector-ref rowPref5 i) j))
          (define right2 (- (vector-ref (vector-ref rowPref2 i) (sub1 cols))
                            (if (> j 0) (vector-ref (vector-ref rowPref2 i) (sub1 j)) 0)))
          (define right5 (- (vector-ref (vector-ref rowPref5 i) (sub1 cols))
                            (if (> j 0) (vector-ref (vector-ref rowPref5 i) (sub1 j)) 0)))
          (define cell2 (vector-ref (vector-ref cnt2 i) j))
          (define cell5 (vector-ref (vector-ref cnt5 i) j))
          ;; four L shapes
          (for ([pair (list (list up2 left2)
                            (list up5 left5))
                 (list (list up2 right2)
                       (list up5 right5))
                 (list (list down2 left2)
                       (list down5 left5))
                 (list (list down2 right2)
                       (list down5 right5))])
            (define total2 (- (first (first pair)) cell2))
            (define total5 (- (first (second pair)) cell5))
            (ans (max (ans) (min total2 total5)))))
          ))
      (ans))))
```

## Erlang

```erlang
-export([max_trailing_zeros/1]).

-spec max_trailing_zeros(Grid :: [[integer()]]) -> integer().
max_trailing_zeros(Grid) ->
    % dimensions
    M = length(Grid),
    N = case Grid of [] -> 0; [Row|_] -> length(Row) end,

    % factor counts per cell
    {Cnt2Rows, Cnt5Rows} = build_cnt_rows(Grid),

    % row prefix sums
    RowPref2Rows = [row_prefix_tuple(R) || R <- Cnt2Rows],
    RowPref5Rows = [row_prefix_tuple(R) || R <- Cnt5Rows],

    % column prefix sums
    {ColPref2Rows, ColPref5Rows} = build_col_prefix(Cnt2Rows, Cnt5Rows),

    % row totals (last element of each row prefix)
    RowTotal2List = [element(tuple_size(R), R) || R <- RowPref2Rows],
    RowTotal5List = [element(tuple_size(R), R) || R <- RowPref5Rows],

    % column totals (last row of column prefixes)
    ColTotal2Tuple = case ColPref2Rows of [] -> list_to_tuple([]); [_|_] -> lists:last(ColPref2Rows) end,
    ColTotal5Tuple = case ColPref5Rows of [] -> list_to_tuple([]); [_|_] -> lists:last(ColPref5Rows) end,

    ZeroTuple = list_to_tuple(lists:duplicate(N, 0)),

    % process all cells
    process_rows(0,
                 Cnt2Rows, Cnt5Rows,
                 RowPref2Rows, RowPref5Rows,
                 ColPref2Rows, ColPref5Rows,
                 RowTotal2List, RowTotal5List,
                 ColTotal2Tuple, ColTotal5Tuple,
                 ZeroTuple, ZeroTuple,
                 0).

%% Build factor count rows
build_cnt_rows(Grid) ->
    {Cnt2Lists, Cnt5Lists} =
        lists:mapfoldl(fun(Row, Acc) ->
            {C2L, C5L} = lists:foldr(fun(Val,{L2,L5}) ->
                {C2,C5}=factor_counts(Val),
                {[C2|L2],[C5|L5]}
            end, {[],[]}, Row),
            {{list_to_tuple(C2L), list_to_tuple(C5L)}, Acc}
        end, ok, Grid),
    % extract tuples
    Cnt2Rows = [element(1,T) || T <- Cnt2Lists],
    Cnt5Rows = [element(2,T) || T <- Cnt5Lists],
    {Cnt2Rows, Cnt5Rows}.

%% Factor counts of 2 and 5
factor_counts(N) ->
    {count_factor(N,2), count_factor(N,5)}.

count_factor(N,F) when N rem F =:= 0 -> 1 + count_factor(N div F, F);
count_factor(_,_) -> 0.

%% Row prefix cumulative tuple
row_prefix_tuple(RowTuple) ->
    Size = tuple_size(RowTuple),
    row_prefix_acc(1, Size, RowTuple, 0, []).

row_prefix_acc(I, Size, RowTuple, Acc, Rev) when I > Size ->
    list_to_tuple(lists:reverse(Rev));
row_prefix_acc(I, Size, RowTuple, Acc, Rev) ->
    Val = element(I, RowTuple),
    NewAcc = Acc + Val,
    row_prefix_acc(I+1, Size, RowTuple, NewAcc, [NewAcc|Rev]).

%% Column prefix cumulative rows
build_col_prefix(Cnt2Rows, Cnt5Rows) ->
    build_col_prefix(Cnt2Rows, Cnt5Rows, [], []).

build_col_prefix([], [], Acc2, Acc5) ->
    {lists:reverse(Acc2), lists:reverse(Acc5)};
build_col_prefix([R2|Rest2], [R5|Rest5], Acc2, Acc5) ->
    case Acc2 of
        [] ->
            NewR2 = R2,
            NewR5 = R5;
        [Prev2|_] ->
            NewR2 = add_tuples(Prev2, R2),
            NewR5 = add_tuples(lists:nth(length(Acc5), Acc5), R5)
    end,
    build_col_prefix(Rest2, Rest5, [NewR2|Acc2], [NewR5|Acc5]).

add_tuples(T1,T2) ->
    Size = tuple_size(T1),
    add_tuples_acc(1, Size, T1, T2, []).

add_tuples_acc(I, Size, T1, T2, Rev) when I > Size ->
    list_to_tuple(lists:reverse(Rev));
add_tuples_acc(I, Size, T1, T2, Rev) ->
    Sum = element(I,T1) + element(I,T2),
    add_tuples_acc(I+1, Size, T1, T2, [Sum|Rev]).

%% Process rows recursively
process_rows(_, [], [], [], [], [], [], [], [], _, _, _, _, Max) -> Max;
process_rows(RowIdx,
             [Cnt2Row|RestCnt2],
             [Cnt5Row|RestCnt5],
             [RowPref2|RestRowPref2],
             [RowPref5|RestRowPref5],
             [ColPref2Curr|RestColPref2],
             [ColPref5Curr|RestColPref5],
             [RowTot2|RestRowTot2],
             [RowTot5|RestRowTot5],
             ColTotal2Tuple, ColTotal5Tuple,
             PrevColPref2, PrevColPref5,
             Max) ->

    NCols = tuple_size(Cnt2Row),
    NewMax = process_cols(0, NCols,
                          Cnt2Row, Cnt5Row,
                          RowPref2, RowPref5,
                          PrevColPref2, ColPref2Curr,
                          PrevColPref5, ColPref5Curr,
                          RowTot2, RowTot5,
                          ColTotal2Tuple, ColTotal5Tuple,
                          Max),

    process_rows(RowIdx+1,
                 RestCnt2, RestCnt5,
                 RestRowPref2, RestRowPref5,
                 RestColPref2, RestColPref5,
                 RestRowTot2, RestRowTot5,
                 ColTotal2Tuple, ColTotal5Tuple,
                 ColPref2Curr, ColPref5Curr,
                 NewMax).

%% Process columns within a row
process_cols(J, NCols,
            Cnt2Row, Cnt5Row,
            RowPref2, RowPref5,
            PrevColPref2, CurrColPref2,
            PrevColPref5, CurrColPref5,
            RowTot2, RowTot5,
            ColTotal2Tuple, ColTotal5Tuple,
            Max) when J == NCols -> Max;
process_cols(J, NCols,
            Cnt2Row, Cnt5Row,
            RowPref2, RowPref5,
            PrevColPref2, CurrColPref2,
            PrevColPref5, CurrColPref5,
            RowTot2, RowTot5,
            ColTotal2Tuple, ColTotal5Tuple,
            Max) ->

    C2 = element(J+1, Cnt2Row),
    C5 = element(J+1, Cnt5Row),

    Up2 = element(J+1, PrevColPref2),
    Up5 = element(J+1, PrevColPref5),

    Down2 = element(J+1, ColTotal2Tuple) - element(J+1, CurrColPref2),
    Down5 = element(J+1, ColTotal5Tuple) - element(J+1, CurrColPref5),

    Left2 = case J of 0 -> 0; _ -> element(J, RowPref2) end,
    Left5 = case J of 0 -> 0; _ -> element(J, RowPref5) end,

    Right2 = RowTot2 - element(J+1, RowPref2),
    Right5 = RowTot5 - element(J+1, RowPref5),

    Max1 = max_trailing(Up2 + Left2 + C2, Up5 + Left5 + C5, Max),
    Max2 = max_trailing(Up2 + Right2 + C2, Up5 + Right5 + C5, Max1),
    Max3 = max_trailing(Down2 + Left2 + C2, Down5 + Left5 + C5, Max2),
    Max4 = max_trailing(Down2 + Right2 + C2, Down5 + Right5 + C5, Max3),

    process_cols(J+1, NCols,
                 Cnt2Row, Cnt5Row,
                 RowPref2, RowPref5,
                 PrevColPref2, CurrColPref2,
                 PrevColPref5, CurrColPref5,
                 RowTot2, RowTot5,
                 ColTotal2Tuple, ColTotal5Tuple,
                 Max4).

%% Compute trailing zeros and keep maximum
max_trailing(TwoSum, FiveSum, CurMax) ->
    Z = if TwoSum < FiveSum -> TwoSum; true -> FiveSum end,
    case Z > CurMax of
        true -> Z;
        false -> CurMax
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_trailing_zeros(grid :: [[integer]]) :: integer
  def max_trailing_zeros(grid) do
    m = length(grid)
    n = grid |> List.first() |> length()

    cnt2_grid = Enum.map(grid, fn row -> Enum.map(row, &count_factor(&1, 2)) end)
    cnt5_grid = Enum.map(grid, fn row -> Enum.map(row, &count_factor(&1, 5)) end)

    up2 = compute_up(cnt2_grid)
    down2 = compute_down(cnt2_grid)
    left2 = compute_left(cnt2_grid)
    right2 = compute_right(cnt2_grid)

    up5 = compute_up(cnt5_grid)
    down5 = compute_down(cnt5_grid)
    left5 = compute_left(cnt5_grid)
    right5 = compute_right(cnt5_grid)

    Enum.reduce(0..(m - 1), 0, fn i, acc_max ->
      up2_row = Enum.at(up2, i)
      down2_row = Enum.at(down2, i)
      left2_row = Enum.at(left2, i)
      right2_row = Enum.at(right2, i)

      up5_row = Enum.at(up5, i)
      down5_row = Enum.at(down5, i)
      left5_row = Enum.at(left5, i)
      right5_row = Enum.at(right5, i)

      cnt2_row = Enum.at(cnt2_grid, i)
      cnt5_row = Enum.at(cnt5_grid, i)

      Enum.reduce(0..(n - 1), acc_max, fn j, inner_acc ->
        c2 = Enum.at(cnt2_row, j)
        c5 = Enum.at(cnt5_row, j)

        t1 =
          min(
            Enum.at(up2_row, j) + Enum.at(left2_row, j) - c2,
            Enum.at(up5_row, j) + Enum.at(left5_row, j) - c5
          )

        t2 =
          min(
            Enum.at(up2_row, j) + Enum.at(right2_row, j) - c2,
            Enum.at(up5_row, j) + Enum.at(right5_row, j) - c5
          )

        t3 =
          min(
            Enum.at(down2_row, j) + Enum.at(left2_row, j) - c2,
            Enum.at(down5_row, j) + Enum.at(left5_row, j) - c5
          )

        t4 =
          min(
            Enum.at(down2_row, j) + Enum.at(right2_row, j) - c2,
            Enum.at(down5_row, j) + Enum.at(right5_row, j) - c5
          )

        max_tz = Enum.max([t1, t2, t3, t4])
        if max_tz > inner_acc, do: max_tz, else: inner_acc
      end)
    end)
  end

  defp count_factor(num, p) do
    if rem(num, p) == 0 do
      1 + count_factor(div(num, p), p)
    else
      0
    end
  end

  defp compute_up(grid) do
    {rev_rows, _} =
      Enum.reduce(Enum.with_index(grid), {[], nil}, fn {row, i}, {acc, prev_row} ->
        new_row =
          Enum.map(Enum.with_index(row), fn {val, j} ->
            val + if i == 0, do: 0, else: Enum.at(prev_row, j)
          end)

        {[new_row | acc], new_row}
      end)

    Enum.reverse(rev_rows)
  end

  defp compute_down(grid) do
    grid |> Enum.reverse() |> compute_up() |> Enum.reverse()
  end

  defp compute_left(grid) do
    Enum.map(grid, fn row ->
      {rev, _} =
        Enum.reduce(row, {[], 0}, fn v, {list_rev, sum} ->
          new_sum = sum + v
          {[new_sum | list_rev], new_sum}
        end)

      Enum.reverse(rev)
    end)
  end

  defp compute_right(grid) do
    grid
    |> Enum.map(&Enum.reverse/1)
    |> compute_left()
    |> Enum.map(&Enum.reverse/1)
  end
end
```

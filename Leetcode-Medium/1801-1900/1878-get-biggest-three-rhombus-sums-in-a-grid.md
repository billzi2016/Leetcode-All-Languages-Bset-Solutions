# 1878. Get Biggest Three Rhombus Sums in a Grid

## Cpp

```cpp
class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<long long>> dr(m, vector<long long>(n));
        vector<vector<long long>> dl(m, vector<long long>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                dr[i][j] = grid[i][j];
                if (i > 0 && j > 0) dr[i][j] += dr[i-1][j-1];
                dl[i][j] = grid[i][j];
                if (i > 0 && j + 1 < n) dl[i][j] += dl[i-1][j+1];
            }
        }
        unordered_set<long long> uniq;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                uniq.insert(grid[i][j]); // size 0 rhombus
                int maxK = min({(m - 1 - i) / 2, j, n - 1 - j});
                for (int k = 1; k <= maxK; ++k) {
                    int ai = i, aj = j;
                    int bi = i + k, bj = j + k;
                    int ci = i + 2 * k, cj = j;
                    int di = i + k, dj = j - k;

                    long long sumAB = dr[bi][bj] - ((ai > 0 && aj > 0) ? dr[ai-1][aj-1] : 0);
                    long long sumBC = dl[ci][cj] - ((bi > 0 && bj + 1 < n) ? dl[bi-1][bj+1] : 0);
                    long long sumCD = dr[ci][cj] - ((di > 0 && dj > 0) ? dr[di-1][dj-1] : 0);
                    long long sumDA = dl[di][dj] - ((ai > 0 && aj + 1 < n) ? dl[ai-1][aj+1] : 0);

                    long long total = sumAB + sumBC + sumCD + sumDA
                                      - grid[ai][aj] - grid[bi][bj] - grid[ci][cj] - grid[di][dj];
                    uniq.insert(total);
                }
            }
        }
        vector<int> vals;
        vals.reserve(uniq.size());
        for (auto v : uniq) vals.push_back((int)v);
        sort(vals.begin(), vals.end(), greater<int>());
        if (vals.size() > 3) vals.resize(3);
        return vals;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] getBiggestThree(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // Prefix sums for main diagonal (top-left to bottom-right)
        int[][] d1 = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                d1[i + 1][j + 1] = grid[i][j] + d1[i][j];
            }
        }

        // Prefix sums for anti-diagonal (top-right to bottom-left)
        int[][] d2 = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = n - 1; j >= 0; j--) {
                d2[i + 1][j] = grid[i][j] + d2[i][j + 1];
            }
        }

        // Helper lambdas for diagonal sums
        java.util.function.BiFunction<int[], int[], Integer> getDiag = (start, end) -> {
            int r1 = start[0], c1 = start[1], r2 = end[0], c2 = end[1];
            return d1[r2 + 1][c2 + 1] - d1[r1][c1];
        };
        java.util.function.BiFunction<int[], int[], Integer> getAnti = (start, end) -> {
            int r1 = start[0], c1 = start[1], r2 = end[0], c2 = end[1];
            return d2[r2 + 1][c2] - d2[r1][c1 + 1];
        };

        Set<Integer> sums = new HashSet<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // radius 0 rhombus (single cell)
                sums.add(grid[i][j]);

                int maxK = Math.min(Math.min(i, m - 1 - i), Math.min(j, n - 1 - j));
                for (int k = 1; k <= maxK; k++) {
                    int topR = i - k, topC = j;
                    int rightR = i, rightC = j + k;
                    int bottomR = i + k, bottomC = j;
                    int leftR = i, leftC = j - k;

                    int sum = 0;
                    // top -> right (diag down-right)
                    sum += getDiag.apply(new int[]{topR, topC}, new int[]{rightR, rightC});
                    // right -> bottom (anti-diag down-left)
                    sum += getAnti.apply(new int[]{rightR, rightC}, new int[]{bottomR, bottomC});
                    // bottom -> left (diag down-right from left to bottom)
                    sum += getDiag.apply(new int[]{leftR, leftC}, new int[]{bottomR, bottomC});
                    // left -> top (anti-diag down-left)
                    sum += getAnti.apply(new int[]{topR, topC}, new int[]{leftR, leftC});

                    // subtract corners counted twice
                    sum -= grid[topR][topC] + grid[rightR][rightC] + grid[bottomR][bottomC] + grid[leftR][leftC];

                    sums.add(sum);
                }
            }
        }

        List<Integer> list = new ArrayList<>(sums);
        list.sort(Collections.reverseOrder());
        int size = Math.min(3, list.size());
        int[] ans = new int[size];
        for (int i = 0; i < size; i++) {
            ans[i] = list.get(i);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        sums = set()
        for i in range(m):
            for j in range(n):
                # rhombus of size 0 (single cell)
                sums.add(grid[i][j])
                max_k = min((m - 1 - i) // 2, j, n - 1 - j)
                for k in range(1, max_k + 1):
                    total = 0
                    # top -> left (exclude left corner)
                    for t in range(k):
                        total += grid[i + t][j - t]
                    # left -> bottom (exclude bottom)
                    for t in range(k):
                        total += grid[i + k + t][j - k + t]
                    # bottom -> right (exclude right)
                    for t in range(k):
                        total += grid[i + 2 * k - t][j + t]
                    # right -> top (exclude top)
                    for t in range(k):
                        total += grid[i + k - t][j + k - t]
                    sums.add(total)
        return sorted(sums, reverse=True)[:3]
```

## Python3

```python
class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()
        for i in range(m):
            for j in range(n):
                # rhombus of size 0 (single cell)
                sums.add(grid[i][j])
                max_k = min((m - 1 - i) // 2, j, n - 1 - j)
                k = 1
                while k <= max_k:
                    total = grid[i][j]  # top corner
                    r, c = i, j
                    # down-left side (including leftmost corner)
                    for _ in range(k):
                        r += 1
                        c -= 1
                        total += grid[r][c]
                    # down-right side (including bottom corner)
                    for _ in range(k):
                        r += 1
                        c += 1
                        total += grid[r][c]
                    # up-right side (including rightmost corner)
                    for _ in range(k):
                        r -= 1
                        c += 1
                        total += grid[r][c]
                    # up-left side (excluding the top corner already counted)
                    for _ in range(k - 1):
                        r -= 1
                        c -= 1
                        total += grid[r][c]
                    sums.add(total)
                    k += 1
        ans = sorted(sums, reverse=True)[:3]
        return ans
```

## C

```c
#include <stdlib.h>

static int m, n;
static int dr[55][55];
static int dl[55][55];

static inline int getDR(int x1, int y1, int x2, int y2) {
    int res = dr[x2][y2];
    if (x1 > 0 && y1 > 0) res -= dr[x1 - 1][y1 - 1];
    return res;
}

static inline int getDL(int x1, int y1, int x2, int y2) {
    int res = dl[x2][y2];
    if (x1 > 0 && y1 + 1 < n) res -= dl[x1 - 1][y1 + 1];
    return res;
}

static int cmpDesc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return vb - va;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getBiggestThree(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    m = gridSize;
    n = gridColSize[0];
    
    // Build diagonal prefix sums
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            dr[i][j] = grid[i][j];
            if (i > 0 && j > 0) dr[i][j] += dr[i - 1][j - 1];
            
            dl[i][j] = grid[i][j];
            if (i > 0 && j + 1 < n) dl[i][j] += dl[i - 1][j + 1];
        }
    }
    
    int maxPossible = m * n * ((m < n ? m : n) + 1);
    int *allSums = (int *)malloc(maxPossible * sizeof(int));
    int cnt = 0;
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            // size 0 rhombus
            allSums[cnt++] = grid[i][j];
            
            int maxK = (m - 1 - i) / 2;
            if (j < maxK) maxK = j;
            if (n - 1 - j < maxK) maxK = n - 1 - j;
            for (int k = 1; k <= maxK; ++k) {
                int top_i = i, top_j = j;
                int right_i = i + k, right_j = j + k;
                int bottom_i = i + 2 * k, bottom_j = j;
                int left_i = i + k, left_j = j - k;
                
                int s1 = getDR(top_i, top_j, right_i, right_j);
                int s2 = getDL(right_i, right_j, bottom_i, bottom_j);
                int s3 = getDR(left_i, left_j, bottom_i, bottom_j);
                int s4 = getDL(top_i, top_j, left_i, left_j);
                
                int total = s1 + s2 + s3 + s4
                            - grid[top_i][top_j]
                            - grid[right_i][right_j]
                            - grid[bottom_i][bottom_j]
                            - grid[left_i][left_j];
                allSums[cnt++] = total;
            }
        }
    }
    
    qsort(allSums, cnt, sizeof(int), cmpDesc);
    
    int *result = (int *)malloc(3 * sizeof(int));
    int resCnt = 0;
    for (int i = 0; i < cnt && resCnt < 3; ++i) {
        if (i == 0 || allSums[i] != allSums[i - 1]) {
            result[resCnt++] = allSums[i];
        }
    }
    
    free(allSums);
    *returnSize = resCnt;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] GetBiggestThree(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        var sums = new HashSet<int>();
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                // Rhombus of size 0 (single cell)
                sums.Add(grid[r][c]);
                int maxD = Math.Min((m - 1 - r) / 2, Math.Min(c, n - 1 - c));
                for (int d = 1; d <= maxD; ++d) {
                    int sum = grid[r][c];
                    // side 1: down-left
                    for (int step = 1; step <= d; ++step)
                        sum += grid[r + step][c - step];
                    // side 2: down-right
                    for (int step = 1; step <= d; ++step)
                        sum += grid[r + d + step][c - d + step];
                    // side 3: up-right
                    for (int step = 1; step <= d; ++step)
                        sum += grid[r + 2 * d - step][c + step];
                    // side 4: up-left (exclude top corner)
                    for (int step = 1; step < d; ++step)
                        sum += grid[r + d - step][c + d - step];
                    sums.Add(sum);
                }
            }
        }
        return sums.OrderByDescending(x => x).Take(3).ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var getBiggestThree = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const sums = new Set();

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            // rhombus of size 0 (single cell)
            sums.add(grid[i][j]);

            // maximum possible k for this top corner
            const maxK = Math.min(
                Math.floor((m - 1 - i) / 2),
                j,
                n - 1 - j
            );

            for (let k = 1; k <= maxK; ++k) {
                let sum = 0;

                // vertices
                const topR = i, topC = j;
                const rightR = i + k, rightC = j + k;
                const bottomR = i + 2 * k, bottomC = j;
                const leftR = i + k, leftC = j - k;

                // Edge: top -> right (down-right)
                for (let s = 0; s <= k; ++s) {
                    sum += grid[topR + s][topC + s];
                }
                // Edge: right -> bottom (down-left), skip the right corner already counted
                for (let s = 1; s <= k; ++s) {
                    sum += grid[rightR + s][rightC - s];
                }
                // Edge: bottom -> left (up-left), skip the bottom corner already counted
                for (let s = 1; s <= k; ++s) {
                    sum += grid[bottomR - s][bottomC - s];
                }
                // Edge: left -> top (up-right), skip both left and top corners
                for (let s = 1; s < k; ++s) {
                    sum += grid[leftR - s][leftC + s];
                }

                sums.add(sum);
            }
        }
    }

    const arr = Array.from(sums);
    arr.sort((a, b) => b - a);
    return arr.slice(0, 3);
};
```

## Typescript

```typescript
function getBiggestThree(grid: number[][]): number[] {
    const m = grid.length;
    const n = grid[0].length;

    // Prefix sums along the two diagonals
    const d1: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    const d2: number[][] = Array.from({ length: m }, () => Array(n).fill(0));

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            d1[i][j] = grid[i][j];
            if (i > 0 && j > 0) d1[i][j] += d1[i - 1][j - 1];

            d2[i][j] = grid[i][j];
            if (i > 0 && j + 1 < n) d2[i][j] += d2[i - 1][j + 1];
        }
    }

    const sums = new Set<number>();

    // helpers to get diagonal segment sums inclusive of both ends
    const diag1Sum = (r1: number, c1: number, r2: number, c2: number): number => {
        let res = d1[r2][c2];
        if (r1 > 0 && c1 > 0) res -= d1[r1 - 1][c1 - 1];
        return res;
    };
    const diag2Sum = (r1: number, c1: number, r2: number, c2: number): number => {
        let res = d2[r2][c2];
        if (r1 > 0 && c1 + 1 < n) res -= d2[r1 - 1][c1 + 1];
        return res;
    };

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            // rhombus of size 0 (single cell)
            sums.add(grid[r][c]);

            const maxK = Math.min(
                Math.floor((m - 1 - r) / 2),
                c,
                n - 1 - c
            );

            for (let k = 1; k <= maxK; k++) {
                // corners
                const top = grid[r][c];
                const right = grid[r + k][c + k];
                const bottom = grid[r + 2 * k][c];
                const left = grid[r + k][c - k];

                // four sides
                const s1 = diag1Sum(r, c, r + k, c + k);           // top -> right
                const s2 = diag2Sum(r + k, c + k, r + 2 * k, c);   // right -> bottom
                const s3 = diag1Sum(r + k, c - k, r + 2 * k, c);   // left -> bottom (down‑right)
                const s4 = diag2Sum(r, c, r + k, c - k);           // top -> left

                const total = s1 + s2 + s3 + s4 - (top + right + bottom + left);
                sums.add(total);
            }
        }
    }

    const result = Array.from(sums).sort((a, b) => b - a);
    return result.slice(0, 3);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function getBiggestThree($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $sums = [];

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                // rhombus of size 0 (single cell)
                $sums[$grid[$i][$j]] = true;

                // maximum possible k for this top vertex
                $maxK = min(intdiv($m - 1 - $i, 2), $j, $n - 1 - $j);
                for ($k = 1; $k <= $maxK; $k++) {
                    $sum = 0;

                    // top to left (down‑left)
                    for ($d = 0; $d <= $k; $d++) {
                        $r = $i + $d;
                        $c = $j - $d;
                        $sum += $grid[$r][$c];
                    }

                    // left to bottom (down‑right)
                    for ($d = 0; $d <= $k; $d++) {
                        $r = $i + $k + $d;
                        $c = $j - $k + $d;
                        $sum += $grid[$r][$c];
                    }

                    // bottom to right (up‑right)
                    for ($d = 0; $d <= $k; $d++) {
                        $r = $i + 2 * $k - $d;
                        $c = $j + $d;
                        $sum += $grid[$r][$c];
                    }

                    // right to top (up‑left)
                    for ($d = 0; $d <= $k; $d++) {
                        $r = $i + $k - $d;
                        $c = $j + $k - $d;
                        $sum += $grid[$r][$c];
                    }

                    // each corner counted twice, subtract once
                    $sum -= $grid[$i][$j];
                    $sum -= $grid[$i + $k][$j - $k];
                    $sum -= $grid[$i + 2 * $k][$j];
                    $sum -= $grid[$i + $k][$j + $k];

                    $sums[$sum] = true;
                }
            }
        }

        $unique = array_keys($sums);
        rsort($unique, SORT_NUMERIC);
        return array_slice($unique, 0, min(3, count($unique)));
    }
}
```

## Swift

```swift
class Solution {
    func getBiggestThree(_ grid: [[Int]]) -> [Int] {
        let m = grid.count
        let n = grid[0].count
        var sums = Set<Int>()
        
        for i in 0..<m {
            for j in 0..<n {
                // rhombus of size 0 (single cell)
                sums.insert(grid[i][j])
                
                let maxK = min((m - 1 - i) / 2, j, n - 1 - j)
                if maxK > 0 {
                    for k in 1...maxK {
                        var x = i
                        var y = j
                        var curSum = 0
                        
                        // edge: top to right (down-right)
                        for _ in 0..<k {
                            curSum += grid[x][y]
                            x += 1
                            y += 1
                        }
                        // edge: right to bottom (down-left)
                        for _ in 0..<k {
                            curSum += grid[x][y]
                            x += 1
                            y -= 1
                        }
                        // edge: bottom to left (up-left)
                        for _ in 0..<k {
                            curSum += grid[x][y]
                            x -= 1
                            y -= 1
                        }
                        // edge: left back to top (up-right)
                        for _ in 0..<k {
                            curSum += grid[x][y]
                            x -= 1
                            y += 1
                        }
                        
                        sums.insert(curSum)
                    }
                }
            }
        }
        
        let sorted = sums.sorted(by: >)
        return Array(sorted.prefix(3))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getBiggestThree(grid: Array<IntArray>): IntArray {
        val m = grid.size
        val n = grid[0].size
        // Prefix sums for two diagonal directions
        val d1 = Array(m) { LongArray(n) } // down-right
        val d2 = Array(m) { LongArray(n) } // down-left
        for (i in 0 until m) {
            for (j in 0 until n) {
                var sum1 = grid[i][j].toLong()
                if (i > 0 && j > 0) sum1 += d1[i - 1][j - 1]
                d1[i][j] = sum1
                var sum2 = grid[i][j].toLong()
                if (i > 0 && j + 1 < n) sum2 += d2[i - 1][j + 1]
                d2[i][j] = sum2
            }
        }

        fun diag1Sum(x1: Int, y1: Int, x2: Int, y2: Int): Long {
            var res = d1[x2][y2]
            if (x1 > 0 && y1 > 0) res -= d1[x1 - 1][y1 - 1]
            return res
        }

        fun diag2Sum(x1: Int, y1: Int, x2: Int, y2: Int): Long {
            var res = d2[x2][y2]
            if (x1 > 0 && y1 + 1 < n) res -= d2[x1 - 1][y1 + 1]
            return res
        }

        val sums = mutableSetOf<Int>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                // rhombus of size 0 (single cell)
                sums.add(grid[i][j])
                var maxK = minOf((m - 1 - i) / 2, j, n - 1 - j)
                var k = 1
                while (k <= maxK) {
                    val topRow = i
                    val leftRow = i + k
                    val leftCol = j - k
                    val bottomRow = i + 2 * k
                    val rightCol = j + k

                    var total = 0L
                    // four sides
                    total += diag2Sum(topRow, j, leftRow, leftCol)          // top -> left
                    total += diag1Sum(leftRow, leftCol, bottomRow, j)      // left -> bottom
                    total += diag2Sum(leftRow, rightCol, bottomRow, j)     // bottom -> right (reverse direction)
                    total += diag1Sum(topRow, j, leftRow, rightCol)        // top -> right

                    // subtract corners counted twice
                    total -= grid[topRow][j].toLong()
                    total -= grid[leftRow][leftCol].toLong()
                    total -= grid[bottomRow][j].toLong()
                    total -= grid[leftRow][rightCol].toLong()

                    sums.add(total.toInt())
                    k++
                }
            }
        }

        val result = sums.sortedDescending().take(3)
        return result.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> getBiggestThree(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // Prefix sums for two diagonal directions
    List<List<int>> dr = List.generate(m, (_) => List.filled(n, 0));
    List<List<int>> dl = List.generate(m, (_) => List.filled(n, 0));

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        dr[i][j] = grid[i][j];
        if (i > 0 && j > 0) dr[i][j] += dr[i - 1][j - 1];

        dl[i][j] = grid[i][j];
        if (i > 0 && j + 1 < n) dl[i][j] += dl[i - 1][j + 1];
      }
    }

    int getDR(int r1, int c1, int r2, int c2) {
      int res = dr[r2][c2];
      if (r1 > 0 && c1 > 0) res -= dr[r1 - 1][c1 - 1];
      return res;
    }

    int getDL(int r1, int c1, int r2, int c2) {
      int res = dl[r2][c2];
      if (r1 > 0 && c1 + 1 < n) res -= dl[r1 - 1][c1 + 1];
      return res;
    }

    Set<int> sums = {};

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        for (int k = 0;; k++) {
          if (i + 2 * k >= m || j - k < 0 || j + k >= n) break;
          if (k == 0) {
            sums.add(grid[i][j]);
          } else {
            int topRight = getDR(i, j, i + k, j + k);
            int rightBottom = getDL(i + k, j + k, i + 2 * k, j);
            int bottomLeft = getDR(i + k, j - k, i + 2 * k, j);
            int leftTop = getDL(i, j, i + k, j - k);

            int total = topRight +
                rightBottom +
                bottomLeft +
                leftTop -
                grid[i][j] -
                grid[i + k][j + k] -
                grid[i + 2 * k][j] -
                grid[i + k][j - k];

            sums.add(total);
          }
        }
      }
    }

    List<int> result = sums.toList();
    result.sort((a, b) => b.compareTo(a));
    if (result.length > 3) result = result.sublist(0, 3);
    return result;
  }
}
```

## Golang

```go
import "sort"

func getBiggestThree(grid [][]int) []int {
	m, n := len(grid), len(grid[0])

	// diagonal prefix sums
	dr := make([][]int, m)
	dl := make([][]int, m)
	for i := 0; i < m; i++ {
		dr[i] = make([]int, n)
		dl[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			val := grid[i][j]
			if i > 0 && j > 0 {
				dr[i][j] = val + dr[i-1][j-1]
			} else {
				dr[i][j] = val
			}
			if i > 0 && j+1 < n {
				dl[i][j] = val + dl[i-1][j+1]
			} else {
				dl[i][j] = val
			}
		}
	}

	drSum := func(x1, y1, x2, y2 int) int {
		res := dr[x2][y2]
		if x1 > 0 && y1 > 0 {
			res -= dr[x1-1][y1-1]
		}
		return res
	}
	dlSum := func(x1, y1, x2, y2 int) int {
		// (x1,y1) -> (x2,y2) moves down-left
		res := dl[x2][y2]
		if x1 > 0 && y1+1 < n {
			res -= dl[x1-1][y1+1]
		}
		return res
	}

	sumsMap := make(map[int]struct{})
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			// radius 0 rhombus (single cell)
			sumsMap[grid[i][j]] = struct{}{}

			maxK := i
			if j < maxK {
				maxK = j
			}
			if m-1-i < maxK {
				maxK = m - 1 - i
			}
			if n-1-j < maxK {
				maxK = n - 1 - j
			}

			for k := 1; k <= maxK; k++ {
				topX, topY := i-k, j
				rightX, rightY := i, j+k
				bottomX, bottomY := i+k, j
				leftX, leftY := i, j-k

				edge1 := drSum(topX, topY, rightX, rightY)               // top to right
				edge2 := dlSum(rightX, rightY, bottomX, bottomY)         // right to bottom
				edge3 := drSum(i, j-k, i+k, j)                           // bottom to left (dr segment)
				edge4 := dlSum(i-k, j, i, j-k)                           // left to top (dl segment)

				sum := edge1 + edge2 + edge3 + edge4
				sum -= grid[topX][topY]
				sum -= grid[rightX][rightY]
				sum -= grid[bottomX][bottomY]
				sum -= grid[leftX][leftY]

				sumsMap[sum] = struct{}{}
			}
		}
	}

	vals := make([]int, 0, len(sumsMap))
	for v := range sumsMap {
		vals = append(vals, v)
	}
	sort.Slice(vals, func(i, j int) bool { return vals[i] > vals[j] })
	if len(vals) > 3 {
		vals = vals[:3]
	}
	return vals
}
```

## Ruby

```ruby
def get_biggest_three(grid)
  m = grid.size
  n = grid[0].size
  diag1 = Array.new(m) { Array.new(n, 0) }
  diag2 = Array.new(m) { Array.new(n, 0) }

  (0...m).each do |i|
    (0...n).each do |j|
      diag1[i][j] = grid[i][j]
      diag1[i][j] += diag1[i - 1][j - 1] if i > 0 && j > 0
      diag2[i][j] = grid[i][j]
      diag2[i][j] += diag2[i - 1][j + 1] if i > 0 && j + 1 < n
    end
  end

  sums = {}

  (0...m).each do |i|
    (0...n).each do |j|
      max_k = [(m - i - 1) / 2, j, n - 1 - j].min
      k = 0
      while k <= max_k
        if k == 0
          sums[grid[i][j]] = true
        else
          top_i = i
          top_j = j
          right_i = i + k
          right_j = j + k
          bottom_i = i + 2 * k
          bottom_j = j
          left_i = i + k
          left_j = j - k

          s1 = diag1[right_i][right_j] - (top_i > 0 && top_j > 0 ? diag1[top_i - 1][top_j - 1] : 0)
          s2 = diag2[bottom_i][bottom_j] - (right_i > 0 && right_j + 1 < n ? diag2[right_i - 1][right_j + 1] : 0)
          s3 = diag1[bottom_i][bottom_j] - (left_i > 0 && left_j > 0 ? diag1[left_i - 1][left_j - 1] : 0)
          s4 = diag2[left_i][left_j] - (top_i > 0 && top_j + 1 < n ? diag2[top_i - 1][top_j + 1] : 0)

          total = s1 + s2 + s3 + s4
          total -= grid[top_i][top_j]
          total -= grid[right_i][right_j]
          total -= grid[bottom_i][bottom_j]
          total -= grid[left_i][left_j]

          sums[total] = true
        end
        k += 1
      end
    end
  end

  sums.keys.sort.reverse.first(3)
end
```

## Scala

```scala
object Solution {
    def getBiggestThree(grid: Array[Array[Int]]): Array[Int] = {
        val m = grid.length
        val n = grid(0).length
        val sums = scala.collection.mutable.HashSet[Int]()
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                // rhombus of size 0 (single cell)
                sums += grid(i)(j)
                var k = 1
                while (i + 2 * k < m && j - k >= 0 && j + k < n) {
                    var sum = 0
                    var x = i
                    var y = j
                    // side 1: top -> right (down-right), exclude right corner
                    for (_ <- 0 until k) {
                        sum += grid(x)(y)
                        x += 1
                        y += 1
                    }
                    // side 2: right -> bottom (down-left), include right corner, exclude bottom corner
                    for (_ <- 0 until k) {
                        sum += grid(x)(y)
                        x += 1
                        y -= 1
                    }
                    // side 3: bottom -> left (up-left), include bottom corner, exclude left corner
                    for (_ <- 0 until k) {
                        sum += grid(x)(y)
                        x -= 1
                        y -= 1
                    }
                    // side 4: left -> top (up-right), include left corner, exclude top (already counted)
                    for (_ <- 0 until k) {
                        sum += grid(x)(y)
                        x -= 1
                        y += 1
                    }
                    sums += sum
                    k += 1
                }
            }
        }
        sums.toArray.sorted(Ordering[Int].reverse).take(3)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_biggest_three(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len();

        // diagonal prefix sums
        let mut diag1 = vec![vec![0i64; n]; m];
        let mut diag2 = vec![vec![0i64; n]; m];

        for i in 0..m {
            for j in 0..n {
                let val = grid[i][j] as i64;
                diag1[i][j] = val + if i > 0 && j > 0 { diag1[i - 1][j - 1] } else { 0 };
                diag2[i][j] = val + if i > 0 && j + 1 < n { diag2[i - 1][j + 1] } else { 0 };
            }
        }

        use std::collections::HashSet;
        let mut sums: HashSet<i64> = HashSet::new();

        for i in 0..m {
            for j in 0..n {
                // maximum possible size k
                let max_k = ((m - i - 1) / 2).min(j.min(n - 1 - j));
                for k in 0..=max_k {
                    if k == 0 {
                        sums.insert(grid[i][j] as i64);
                    } else {
                        let x2 = i + k;
                        let y2 = j + k;
                        let x3 = i + 2 * k;
                        let y3 = j;
                        let x4 = i + k;
                        let y4 = j - k;

                        // side top -> right (down-right)
                        let mut s1 = diag1[x2][y2];
                        if i > 0 && j > 0 {
                            s1 -= diag1[i - 1][j - 1];
                        }

                        // side right -> bottom (down-left)
                        let mut s2 = diag2[x3][y3];
                        if x2 > 0 && y2 + 1 < n {
                            s2 -= diag2[x2 - 1][y2 + 1];
                        }

                        // side left -> bottom (down-right)
                        let mut s3 = diag1[x3][y3];
                        if x4 > 0 && y4 > 0 {
                            s3 -= diag1[x4 - 1][y4 - 1];
                        }

                        // side top -> left (down-left)
                        let mut s4 = diag2[x4][y4];
                        if i > 0 && j + 1 < n {
                            s4 -= diag2[i - 1][j + 1];
                        }

                        let total = s1
                            + s2
                            + s3
                            + s4
                            - (grid[i][j] as i64
                                + grid[x2][y2] as i64
                                + grid[x3][y3] as i64
                                + grid[x4][y4] as i64);
                        sums.insert(total);
                    }
                }
            }
        }

        let mut result: Vec<i32> = sums.into_iter().map(|v| v as i32).collect();
        result.sort_by(|a, b| b.cmp(a));
        if result.len() > 3 {
            result.truncate(3);
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(provide get-biggest-three)

(define/contract (get-biggest-three grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([m (length grid)]
         [n (if (= m 0) 0 (length (first grid)))]
         ;; convert to vectors for O(1) indexing
         [grid-v (list->vector (map list->vector grid))]
         ;; diagonal prefix sums
         [diagDR (make-vector m)]
         [diagDL (make-vector m)])
    ;; build diagonal prefix sums
    (for ([i (in-range m)])
      (let* ([row-dr (make-vector n)]
             [row-dl (make-vector n)])
        (for ([j (in-range n)])
          (define val (vector-ref (vector-ref grid-v i) j))
          (define dr (+ val
                        (if (and (> i 0) (> j 0))
                            (vector-ref (vector-ref diagDR (- i 1)) (- j 1))
                            0)))
          (define dl (+ val
                        (if (and (> i 0) (< (+ j 1) n))
                            (vector-ref (vector-ref diagDL (- i 1)) (+ j 1))
                            0)))
          (vector-set! row-dr j dr)
          (vector-set! row-dl j dl))
        (vector-set! diagDR i row-dr)
        (vector-set! diagDL i row-dl)))
    ;; helper to get sum on down‑right diagonal inclusive
    (define (dr-sum r1 c1 r2 c2)
      (let* ([total (vector-ref (vector-ref diagDR r2) c2)]
             [sub   (if (and (> r1 0) (> c1 0))
                        (vector-ref (vector-ref diagDR (- r1 1)) (- c1 1))
                        0)])
        (- total sub)))
    ;; helper to get sum on down‑left diagonal inclusive
    (define (dl-sum r1 c1 r2 c2)
      (let* ([total (vector-ref (vector-ref diagDL r2) c2)]
             [sub   (if (and (> r1 0) (< (+ c1 1) n))
                        (vector-ref (vector-ref diagDL (- r1 1)) (+ c1 1))
                        0)])
        (- total sub)))
    ;; collect distinct sums
    (define sums-hash (make-hash))
    (define (add-sum s)
      (hash-set! sums-hash s #t))
    ;; iterate all rhombuses
    (for ([i (in-range m)]
          [j (in-range n)])
      (let* ([val (vector-ref (vector-ref grid-v i) j)])
        (add-sum val))
      (define maxk-row (quotient (- m i 1) 2)) ; floor((m-i-1)/2)
      (define maxk-col-left j)
      (define maxk-col-right (- n j 1))
      (define maxk (min maxk-row (min maxk-col-left maxk-col-right)))
      (when (> maxk 0)
        (for ([k (in-range 1 (add1 maxk))])
          (let* ([iA i] [jA j]
                 [iB (+ i k)] [jB (- j k)]
                 [iC (+ i (* 2 k))] [jC j]
                 [iD (+ i k)] [jD (+ j k)])
            (define seg1 (dl-sum iA jA iB jB))
            (define seg2 (dr-sum iB jB iC jC))
            (define seg3 (dl-sum iD jD iC jC))
            (define seg4 (dr-sum iA jA iD jD))
            (define corner-sum (+ (vector-ref (vector-ref grid-v iA) jA)
                                  (vector-ref (vector-ref grid-v iB) jB)
                                  (vector-ref (vector-ref grid-v iC) jC)
                                  (vector-ref (vector-ref grid-v iD) jD)))
            (define total (- (+ seg1 seg2 seg3 seg4) corner-sum))
            (add-sum total))))))
    ;; extract, sort descending, take up to three
    (let* ([all (hash-keys sums-hash)]
           [sorted (sort all >)])
      (take sorted 3))))
```

## Erlang

```erlang
-module(solution).
-export([get_biggest_three/1]).

-spec get_biggest_three(Grid :: [[integer()]]) -> [integer()].
get_biggest_three(Grid) ->
    RowTuples = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    M = tuple_size(RowTuples),
    N = case M of
            0 -> 0;
            _ -> tuple_size(element(1, RowTuples))
        end,
    SumsMap = collect_sums(RowTuples, M, N, #{}),
    SumList = maps:keys(SumsMap),
    SortedDesc = lists:reverse(lists:sort(SumList)),
    case length(SortedDesc) of
        L when L >= 3 -> lists:sublist(SortedDesc, 3);
        _ -> SortedDesc
    end.

%% collect all distinct rhombus sums into a map
collect_sums(GridTuple, M, N, AccMap) ->
    collect_rows(0, M - 1, GridTuple, M, N, AccMap).

collect_rows(I, MaxI, GridTuple, M, N, AccMap) when I =< MaxI ->
    NewAcc = collect_cols(I, 0, N - 1, GridTuple, M, N, AccMap),
    collect_rows(I + 1, MaxI, GridTuple, M, N, NewAcc);
collect_rows(_, _, _, _, _, _, AccMap) -> AccMap.

collect_cols(I, J, MaxJ, GridTuple, M, N, AccMap) when J =< MaxJ ->
    MaxK = min(min(I, M - 1 - I), min(J, N - 1 - J)),
    NewAcc = collect_sizes(I, J, 0, MaxK, GridTuple, AccMap),
    collect_cols(I, J + 1, MaxJ, GridTuple, M, N, NewAcc);
collect_cols(_, _, _, _, _, _, AccMap) -> AccMap.

collect_sizes(_I, _J, K, MaxK, _GridTuple, AccMap) when K > MaxK ->
    AccMap;
collect_sizes(I, J, K, MaxK, GridTuple, AccMap) ->
    Sum = compute_sum(GridTuple, I, J, K),
    NewMap = maps:put(Sum, true, AccMap),
    collect_sizes(I, J, K + 1, MaxK, GridTuple, NewMap).

%% compute sum of border cells for rhombus centered at (I,J) with radius K
compute_sum(GridTuple, I, J, 0) ->
    get_elem(GridTuple, I, J);
compute_sum(GridTuple, I, J, K) ->
    lists:foldl(fun(Dx, Acc) ->
        AbsDx = abs(Dx),
        Dy = K - AbsDx,
        X = I + Dx,
        Y1 = J + Dy,
        Val1 = get_elem(GridTuple, X, Y1),
        Acc2 = Acc + Val1,
        case Dy > 0 of
            true ->
                Y2 = J - Dy,
                Val2 = get_elem(GridTuple, X, Y2),
                Acc2 + Val2;
            false -> Acc2
        end
    end, 0, lists:seq(-K, K)).

%% retrieve element at (I,J) where indices are zero‑based
get_elem(GridTuple, I, J) ->
    Row = element(I + 1, GridTuple),
    element(J + 1, Row).

min(A, B) when A =< B -> A;
min(_, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_biggest_three(grid :: [[integer]]) :: [integer]
  def get_biggest_three(grid) do
    m = length(grid)
    n = length(List.first(grid))

    dr = build_dr(grid, m, n)
    dl = build_dl(grid, m, n)

    single_sums =
      for i <- 0..(m - 1), j <- 0..(n - 1), do: get(grid, i, j)

    big_sums =
      for i <- 0..(m - 1),
          j <- 0..(n - 1),
          max_k = min(div(m - 1 - i, 2), j, n - 1 - j),
          k <- 1..max_k do
        top_i = i
        top_j = j
        right_i = i + k
        right_j = j + k
        bottom_i = i + 2 * k
        bottom_j = j
        left_i = i + k
        left_j = j - k

        sum1 = dr_sum(dr, top_i, top_j, right_i, right_j)
        sum2 = dl_sum(dl, right_i, right_j, bottom_i, bottom_j, n)
        sum3 = dr_sum(dr, left_i, left_j, bottom_i, bottom_j)
        sum4 = dl_sum(dl, top_i, top_j, left_i, left_j, n)

        total =
          sum1 + sum2 + sum3 + sum4 -
            get(grid, top_i, top_j) -
            get(grid, right_i, right_j) -
            get(grid, bottom_i, bottom_j) -
            get(grid, left_i, left_j)

        total
      end

    all = single_sums ++ big_sums
    distinct = MapSet.new(all) |> MapSet.to_list()
    sorted = Enum.sort(distinct, &>=/2)
    Enum.take(sorted, 3)
  end

  defp get(matrix, i, j), do: matrix |> Enum.at(i) |> Enum.at(j)

  defp build_dr(grid, m, n) do
    Enum.reduce(0..(m - 1), [], fn i, acc ->
      prev_row = if i == 0, do: nil, else: Enum.at(acc, i - 1)

      cur_row =
        Enum.map(0..(n - 1), fn j ->
          val = get(grid, i, j)
          add = if i > 0 and j > 0, do: get(prev_row, j - 1), else: 0
          val + add
        end)

      acc ++ [cur_row]
    end)
  end

  defp build_dl(grid, m, n) do
    Enum.reduce(0..(m - 1), [], fn i, acc ->
      prev_row = if i == 0, do: nil, else: Enum.at(acc, i - 1)

      cur_row =
        Enum.map(0..(n - 1), fn j ->
          val = get(grid, i, j)
          add = if i > 0 and j + 1 < n, do: get(prev_row, j + 1), else: 0
          val + add
        end)

      acc ++ [cur_row]
    end)
  end

  defp dr_sum(dr, i1, j1, i2, j2) do
    base = if i1 > 0 and j1 > 0, do: get(dr, i1 - 1, j1 - 1), else: 0
    get(dr, i2, j2) - base
  end

  defp dl_sum(dl, i1, j1, i2, j2, n) do
    base = if i1 > 0 and j1 + 1 < n, do: get(dl, i1 - 1, j1 + 1), else: 0
    get(dl, i2, j2) - base
  end
end
```

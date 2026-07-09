# 3548. Equal Sum Grid Partition II

## Cpp

```cpp
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long totalSum = 0;
        unordered_map<int,int> totalFreq;
        totalFreq.reserve(m * n * 2);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int v = grid[i][j];
                totalSum += v;
                ++totalFreq[v];
            }
        }

        // Horizontal cuts
        unordered_map<int,int> topFreq;
        topFreq.reserve(m * n);
        long long topSum = 0;
        for (int i = 0; i < m - 1; ++i) { // cut after row i
            for (int j = 0; j < n; ++j) {
                int v = grid[i][j];
                topSum += v;
                ++topFreq[v];
            }
            long long bottomSum = totalSum - topSum;
            if (topSum == bottomSum) return true;
            long long diffLL = llabs(topSum - bottomSum);
            if (diffLL > 100000) continue; // values are <=1e5
            int diff = (int)diffLL;

            if (topSum > bottomSum) {
                // need diff in top part
                if (i + 1 == 1) { // only one row on top
                    if (grid[0][0] == diff || grid[0][n-1] == diff) return true;
                } else {
                    if (topFreq.find(diff) != topFreq.end()) return true;
                }
            } else { // bottom larger
                int rowsBottom = m - (i + 1);
                if (rowsBottom == 1) { // only one row at bottom
                    int r = i + 1;
                    if (grid[r][0] == diff || grid[r][n-1] == diff) return true;
                } else {
                    int cntTotal = totalFreq.count(diff) ? totalFreq[diff] : 0;
                    int cntTop = topFreq.count(diff) ? topFreq[diff] : 0;
                    if (cntTotal - cntTop > 0) return true;
                }
            }
        }

        // Vertical cuts
        unordered_map<int,int> leftFreq;
        leftFreq.reserve(m * n);
        long long leftSum = 0;
        for (int j = 0; j < n - 1; ++j) { // cut after column j
            for (int i = 0; i < m; ++i) {
                int v = grid[i][j];
                leftSum += v;
                ++leftFreq[v];
            }
            long long rightSum = totalSum - leftSum;
            if (leftSum == rightSum) return true;
            long long diffLL = llabs(leftSum - rightSum);
            if (diffLL > 100000) continue;
            int diff = (int)diffLL;

            if (leftSum > rightSum) {
                // need diff in left part
                if (j + 1 == 1) { // only one column on left
                    if (grid[0][0] == diff || grid[m-1][0] == diff) return true;
                } else {
                    if (leftFreq.find(diff) != leftFreq.end()) return true;
                }
            } else { // right larger
                int colsRight = n - (j + 1);
                if (colsRight == 1) { // only one column on right
                    int c = j + 1;
                    if (grid[0][c] == diff || grid[m-1][c] == diff) return true;
                } else {
                    int cntTotal = totalFreq.count(diff) ? totalFreq[diff] : 0;
                    int cntLeft = leftFreq.count(diff) ? leftFreq[diff] : 0;
                    if (cntTotal - cntLeft > 0) return true;
                }
            }
        }

        return false;
    }
};
```

## Java

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long total = 0L;
        for (int[] row : grid) {
            for (int v : row) total += v;
        }
        final int MAX_VAL = 100000;

        // Horizontal cuts
        if (m > 1) {
            Map<Integer, Integer> topMap = new HashMap<>();
            Map<Integer, Integer> bottomMap = new HashMap<>();
            for (int[] row : grid) {
                for (int v : row) inc(bottomMap, v);
            }
            long topSum = 0L;
            for (int i = 0; i < m - 1; i++) { // cut after row i
                for (int j = 0; j < n; j++) {
                    int val = grid[i][j];
                    topSum += val;
                    inc(topMap, val);
                    dec(bottomMap, val);
                }
                long bottomSum = total - topSum;
                if (topSum == bottomSum) return true;
                long diffL = Math.abs(topSum - bottomSum);
                if (diffL > MAX_VAL) continue;
                int diff = (int) diffL;
                if (topSum > bottomSum) {
                    if (validRemovalTop(grid, i, n, diff, topMap)) return true;
                } else {
                    if (validRemovalBottom(grid, i + 1, m - 1, n, diff, bottomMap)) return true;
                }
            }
        }

        // Vertical cuts
        if (n > 1) {
            Map<Integer, Integer> leftMap = new HashMap<>();
            Map<Integer, Integer> rightMap = new HashMap<>();
            for (int[] row : grid) {
                for (int v : row) inc(rightMap, v);
            }
            long leftSum = 0L;
            for (int j = 0; j < n - 1; j++) { // cut after column j
                for (int i = 0; i < m; i++) {
                    int val = grid[i][j];
                    leftSum += val;
                    inc(leftMap, val);
                    dec(rightMap, val);
                }
                long rightSum = total - leftSum;
                if (leftSum == rightSum) return true;
                long diffL = Math.abs(leftSum - rightSum);
                if (diffL > MAX_VAL) continue;
                int diff = (int) diffL;
                if (leftSum > rightSum) {
                    if (validRemovalLeft(grid, j, m, diff, leftMap)) return true;
                } else {
                    if (validRemovalRight(grid, j + 1, n - 1, m, diff, rightMap)) return true;
                }
            }
        }

        return false;
    }

    private static void inc(Map<Integer, Integer> map, int v) {
        map.put(v, map.getOrDefault(v, 0) + 1);
    }

    private static void dec(Map<Integer, Integer> map, int v) {
        int cnt = map.getOrDefault(v, 0);
        if (cnt <= 1) map.remove(v);
        else map.put(v, cnt - 1);
    }

    // Horizontal side checks
    private boolean validRemovalTop(int[][] grid, int cutRowIdx, int n, int diff,
                                    Map<Integer, Integer> topMap) {
        int rows = cutRowIdx + 1;
        if (rows > 1 && n > 1) return topMap.containsKey(diff);
        if (rows == 1) { // single row
            return grid[0][0] == diff || grid[0][n - 1] == diff;
        }
        // n == 1 case (single column)
        return grid[0][0] == diff || grid[cutRowIdx][0] == diff;
    }

    private boolean validRemovalBottom(int[][] grid, int startRow, int endRow,
                                       int n, int diff, Map<Integer, Integer> bottomMap) {
        int rows = endRow - startRow + 1;
        if (rows > 1 && n > 1) return bottomMap.containsKey(diff);
        if (rows == 1) { // single row
            return grid[startRow][0] == diff || grid[startRow][n - 1] == diff;
        }
        // n == 1 case (single column)
        return grid[startRow][0] == diff || grid[endRow][0] == diff;
    }

    // Vertical side checks
    private boolean validRemovalLeft(int[][] grid, int cutColIdx, int m,
                                     int diff, Map<Integer, Integer> leftMap) {
        int cols = cutColIdx + 1;
        if (cols > 1 && m > 1) return leftMap.containsKey(diff);
        if (cols == 1) { // single column
            return grid[0][0] == diff || grid[m - 1][0] == diff;
        }
        // m == 1 case (single row)
        return grid[0][0] == diff || grid[0][cutColIdx] == diff;
    }

    private boolean validRemovalRight(int[][] grid, int startCol, int endCol,
                                      int m, int diff, Map<Integer, Integer> rightMap) {
        int cols = endCol - startCol + 1;
        if (cols > 1 && m > 1) return rightMap.containsKey(diff);
        if (cols == 1) { // single column
            return grid[0][startCol] == diff || grid[m - 1][startCol] == diff;
        }
        // m == 1 case (single row)
        return grid[0][startCol] == diff || grid[0][endCol] == diff;
    }
}
```

## Python

```python
class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        from collections import Counter

        m = len(grid)
        n = len(grid[0])

        total = 0
        for row in grid:
            total += sum(row)

        # vertical cuts
        right_counter = Counter()
        for row in grid:
            right_counter.update(row)
        left_counter = Counter()
        left_sum = 0

        for col in range(n - 1):
            for r in range(m):
                val = grid[r][col]
                left_sum += val
                left_counter[val] += 1
                # remove from right side
                cnt = right_counter[val] - 1
                if cnt:
                    right_counter[val] = cnt
                else:
                    del right_counter[val]

            right_sum = total - left_sum
            diff = left_sum - right_sum
            if diff == 0:
                return True
            if diff > 0:
                if left_counter.get(diff, 0) > 0:
                    return True
            else:
                if right_counter.get(-diff, 0) > 0:
                    return True

        # horizontal cuts
        bottom_counter = Counter()
        for row in grid:
            bottom_counter.update(row)
        top_counter = Counter()
        top_sum = 0

        for row_idx in range(m - 1):
            row = grid[row_idx]
            row_sum = sum(row)
            top_sum += row_sum
            top_counter.update(row)

            # remove this row from bottom side
            for val in row:
                cnt = bottom_counter[val] - 1
                if cnt:
                    bottom_counter[val] = cnt
                else:
                    del bottom_counter[val]

            bottom_sum = total - top_sum
            diff = top_sum - bottom_sum
            if diff == 0:
                return True
            if diff > 0:
                if top_counter.get(diff, 0) > 0:
                    return True
            else:
                if bottom_counter.get(-diff, 0) > 0:
                    return True

        return False
```

## Python3

```python
import collections
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = 0
        row_sums = [0] * m
        col_sums = [0] * n
        all_counter = collections.Counter()
        for i in range(m):
            rs = 0
            for j in range(n):
                v = grid[i][j]
                rs += v
                col_sums[j] += v
                all_counter[v] += 1
            row_sums[i] = rs
            total += rs

        # vertical cuts
        left_sum = 0
        left_counter = collections.Counter()
        right_counter = all_counter.copy()
        for i in range(n - 1):
            col_sum_i = col_sums[i]
            left_sum += col_sum_i
            for r in range(m):
                v = grid[r][i]
                left_counter[v] += 1
                cnt = right_counter[v] - 1
                if cnt:
                    right_counter[v] = cnt
                else:
                    del right_counter[v]

            right_sum = total - left_sum
            if left_sum == right_sum:
                return True

            # need removal from larger side
            if left_sum > right_sum:
                diff = left_sum - right_sum
                width_left = i + 1
                if m > 1 and width_left > 1:
                    if left_counter.get(diff, 0):
                        return True
                else:
                    # single row or single column case for left part
                    if m == 1:  # single row
                        if diff == grid[0][0] or diff == grid[0][i]:
                            return True
                    else:      # width_left == 1 (single column)
                        if diff == grid[0][i] or diff == grid[m - 1][i]:
                            return True
            else:
                diff = right_sum - left_sum
                width_right = n - i - 1
                if m > 1 and width_right > 1:
                    if right_counter.get(diff, 0):
                        return True
                else:
                    # single row or single column case for right part
                    col = i + 1
                    if m == 1:  # single row
                        if diff == grid[0][col] or diff == grid[0][n - 1]:
                            return True
                    else:      # width_right == 1 (single column)
                        if diff == grid[0][col] or diff == grid[m - 1][col]:
                            return True

        # horizontal cuts
        top_sum = 0
        top_counter = collections.Counter()
        bottom_counter = all_counter.copy()
        for r in range(m - 1):
            row_sum_r = row_sums[r]
            top_sum += row_sum_r
            for c in range(n):
                v = grid[r][c]
                top_counter[v] += 1
                cnt = bottom_counter[v] - 1
                if cnt:
                    bottom_counter[v] = cnt
                else:
                    del bottom_counter[v]

            bottom_sum = total - top_sum
            if top_sum == bottom_sum:
                return True

            if top_sum > bottom_sum:
                diff = top_sum - bottom_sum
                height_top = r + 1
                if n > 1 and height_top > 1:
                    if top_counter.get(diff, 0):
                        return True
                else:
                    # single column or single row case for top part
                    if n == 1:  # single column
                        if diff == grid[0][0] or diff == grid[r][0]:
                            return True
                    else:      # height_top == 1 (single row)
                        if diff == grid[0][0] or diff == grid[0][n - 1]:
                            return True
            else:
                diff = bottom_sum - top_sum
                height_bottom = m - r - 1
                if n > 1 and height_bottom > 1:
                    if bottom_counter.get(diff, 0):
                        return True
                else:
                    # single column or single row case for bottom part
                    row_idx = r + 1
                    if n == 1:  # single column
                        if diff == grid[row_idx][0] or diff == grid[m - 1][0]:
                            return True
                    else:      # height_bottom == 1 (single row)
                        if diff == grid[row_idx][0] or diff == grid[row_idx][n - 1]:
                            return True

        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

bool canPartitionGrid(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    if (m == 0) return false;
    int n = gridColSize[0];
    const int MAXV = 100000;   // max value of a cell

    long long total = 0;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            total += grid[i][j];

    if (m * n < 2) return false;   // need at least two cells to cut

    /* ---------- Horizontal cuts ---------- */
    int *cntUpper = (int*)calloc(MAXV + 1, sizeof(int));
    int *cntLower = (int*)calloc(MAXV + 1, sizeof(int));

    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            cntLower[grid[i][j]]++;

    long long sumUpper = 0, sumLower = total;
    int rowsUpper = 0;

    for (int cut = 0; cut < m - 1; ++cut) {
        // move row 'cut' to upper part
        rowsUpper++;
        for (int j = 0; j < n; ++j) {
            int val = grid[cut][j];
            sumUpper += val;
            sumLower -= val;
            cntUpper[val] ++;
            cntLower[val] --;
        }

        if (sumUpper == sumLower) {
            free(cntUpper);
            free(cntLower);
            return true;
        }

        long long diffLL = llabs(sumUpper - sumLower);
        if (diffLL > MAXV) continue;   // cannot match any cell value
        int diff = (int)diffLL;

        if (sumUpper > sumLower) {
            if (cntUpper[diff] == 0) continue;
            int rows = rowsUpper, cols = n;
            if (rows == 1 && cols == 1) continue; // removal would empty the part
            else if (rows == 1) {   // single row, need at ends
                int left = grid[0][0];
                int right = grid[0][n - 1];
                if (diff == left || diff == right) {
                    free(cntUpper);
                    free(cntLower);
                    return true;
                }
            } else if (cols == 1) { // single column, need top or bottom
                int top = grid[0][0];
                int bottom = grid[cut][0];
                if (diff == top || diff == bottom) {
                    free(cntUpper);
                    free(cntLower);
                    return true;
                }
            } else {
                free(cntUpper);
                free(cntLower);
                return true;
            }
        } else { // lower part larger
            if (cntLower[diff] == 0) continue;
            int rows = m - rowsUpper, cols = n;
            if (rows == 1 && cols == 1) continue;
            else if (rows == 1) {
                int rowIdx = cut + 1;
                int left = grid[rowIdx][0];
                int right = grid[rowIdx][n - 1];
                if (diff == left || diff == right) {
                    free(cntUpper);
                    free(cntLower);
                    return true;
                }
            } else if (cols == 1) {
                int top = grid[cut + 1][0];
                int bottom = grid[m - 1][0];
                if (diff == top || diff == bottom) {
                    free(cntUpper);
                    free(cntLower);
                    return true;
                }
            } else {
                free(cntUpper);
                free(cntLower);
                return true;
            }
        }
    }

    free(cntUpper);
    free(cntLower);

    /* ---------- Vertical cuts ---------- */
    int *cntLeft = (int*)calloc(MAXV + 1, sizeof(int));
    int *cntRight = (int*)calloc(MAXV + 1, sizeof(int));

    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            cntRight[grid[i][j]]++;

    long long sumLeft = 0, sumRight = total;
    int colsLeft = 0;

    for (int cut = 0; cut < n - 1; ++cut) {
        // move column 'cut' to left part
        colsLeft++;
        for (int i = 0; i < m; ++i) {
            int val = grid[i][cut];
            sumLeft += val;
            sumRight -= val;
            cntLeft[val] ++;
            cntRight[val] --;
        }

        if (sumLeft == sumRight) {
            free(cntLeft);
            free(cntRight);
            return true;
        }

        long long diffLL = llabs(sumLeft - sumRight);
        if (diffLL > MAXV) continue;
        int diff = (int)diffLL;

        if (sumLeft > sumRight) {
            if (cntLeft[diff] == 0) continue;
            int rows = m, cols = colsLeft;
            if (rows == 1 && cols == 1) continue;
            else if (rows == 1) { // single row
                int left = grid[0][0];
                int right = grid[0][cut];
                if (diff == left || diff == right) {
                    free(cntLeft);
                    free(cntRight);
                    return true;
                }
            } else if (cols == 1) { // single column
                int top = grid[0][0];
                int bottom = grid[m - 1][0];
                if (diff == top || diff == bottom) {
                    free(cntLeft);
                    free(cntRight);
                    return true;
                }
            } else {
                free(cntLeft);
                free(cntRight);
                return true;
            }
        } else { // right part larger
            if (cntRight[diff] == 0) continue;
            int rows = m, cols = n - colsLeft;
            if (rows == 1 && cols == 1) continue;
            else if (rows == 1) {
                int colStart = cut + 1;
                int left = grid[0][colStart];
                int right = grid[0][n - 1];
                if (diff == left || diff == right) {
                    free(cntLeft);
                    free(cntRight);
                    return true;
                }
            } else if (cols == 1) {
                int colIdx = cut + 1;
                int top = grid[0][colIdx];
                int bottom = grid[m - 1][colIdx];
                if (diff == top || diff == bottom) {
                    free(cntLeft);
                    free(cntRight);
                    return true;
                }
            } else {
                free(cntLeft);
                free(cntRight);
                return true;
            }
        }
    }

    free(cntLeft);
    free(cntRight);
    return false;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public bool CanPartitionGrid(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        long total = 0;
        var totalFreq = new Dictionary<int, int>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                total += val;
                if (totalFreq.ContainsKey(val)) totalFreq[val]++; else totalFreq[val] = 1;
            }
        }

        // Horizontal cuts
        if (m >= 2) {
            var prefixFreq = new Dictionary<int, int>();
            long topSum = 0;
            for (int i = 0; i < m - 1; i++) { // cut after row i
                for (int j = 0; j < n; j++) {
                    int val = grid[i][j];
                    topSum += val;
                    if (prefixFreq.ContainsKey(val)) prefixFreq[val]++; else prefixFreq[val] = 1;
                }
                long bottomSum = total - topSum;
                if (topSum == bottomSum) return true;

                long diffL = Math.Abs(topSum - bottomSum);
                if (diffL > int.MaxValue) continue;
                int diff = (int)diffL;

                if (topSum > bottomSum) {
                    // need diff in top side
                    bool ok = false;
                    int topRows = i + 1;
                    if (topRows == 1 || n == 1) {
                        if (topRows == 1) { // single row
                            if (grid[0][0] == diff || grid[0][n - 1] == diff) ok = true;
                        }
                        if (n == 1) { // single column
                            if (grid[0][0] == diff || grid[i][0] == diff) ok = true;
                        }
                    } else {
                        if (prefixFreq.TryGetValue(diff, out int cnt) && cnt > 0) ok = true;
                    }
                    if (ok) return true;
                } else { // bottom larger
                    bool ok = false;
                    int bottomRows = m - i - 1;
                    if (bottomRows == 1 || n == 1) {
                        if (bottomRows == 1) {
                            int rowIdx = i + 1;
                            if (grid[rowIdx][0] == diff || grid[rowIdx][n - 1] == diff) ok = true;
                        }
                        if (n == 1) {
                            if (grid[i + 1][0] == diff || grid[m - 1][0] == diff) ok = true;
                        }
                    } else {
                        int totalCnt = totalFreq.ContainsKey(diff) ? totalFreq[diff] : 0;
                        int leftCnt = prefixFreq.ContainsKey(diff) ? prefixFreq[diff] : 0;
                        if (totalCnt - leftCnt > 0) ok = true;
                    }
                    if (ok) return true;
                }
            }
        }

        // Vertical cuts
        if (n >= 2) {
            var leftFreq = new Dictionary<int, int>();
            long leftSum = 0;
            for (int j = 0; j < n - 1; j++) { // cut after column j
                for (int i = 0; i < m; i++) {
                    int val = grid[i][j];
                    leftSum += val;
                    if (leftFreq.ContainsKey(val)) leftFreq[val]++; else leftFreq[val] = 1;
                }
                long rightSum = total - leftSum;
                if (leftSum == rightSum) return true;

                long diffL = Math.Abs(leftSum - rightSum);
                if (diffL > int.MaxValue) continue;
                int diff = (int)diffL;

                if (leftSum > rightSum) {
                    // need diff in left side
                    bool ok = false;
                    int leftCols = j + 1;
                    if (leftCols == 1 || m == 1) {
                        if (leftCols == 1) { // single column
                            if (grid[0][0] == diff || grid[m - 1][0] == diff) ok = true;
                        }
                        if (m == 1) { // single row
                            if (grid[0][0] == diff || grid[0][j] == diff) ok = true;
                        }
                    } else {
                        if (leftFreq.TryGetValue(diff, out int cnt) && cnt > 0) ok = true;
                    }
                    if (ok) return true;
                } else { // right larger
                    bool ok = false;
                    int rightCols = n - j - 1;
                    if (rightCols == 1 || m == 1) {
                        if (rightCols == 1) { // single column at j+1
                            if (grid[0][j + 1] == diff || grid[m - 1][j + 1] == diff) ok = true;
                        }
                        if (m == 1) {
                            if (grid[0][j + 1] == diff || grid[0][n - 1] == diff) ok = true;
                        }
                    } else {
                        int totalCnt = totalFreq.ContainsKey(diff) ? totalFreq[diff] : 0;
                        int leftCnt = leftFreq.ContainsKey(diff) ? leftFreq[diff] : 0;
                        if (totalCnt - leftCnt > 0) ok = true;
                    }
                    if (ok) return true;
                }
            }
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var canPartitionGrid = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let total = 0;

    // ---------- Horizontal cut ----------
    const rowSums = new Array(m).fill(0);
    const bottomMapH = new Map(); // all cells initially
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const v = grid[i][j];
            total += v;
            rowSums[i] += v;
            bottomMapH.set(v, (bottomMapH.get(v) || 0) + 1);
        }
    }

    let topSum = 0;
    const topMapH = new Map();

    for (let i = 0; i < m - 1; ++i) { // cut after row i
        topSum += rowSums[i];
        for (let j = 0; j < n; ++j) {
            const v = grid[i][j];
            // move from bottom to top
            const cntB = bottomMapH.get(v);
            if (cntB === 1) bottomMapH.delete(v);
            else bottomMapH.set(v, cntB - 1);

            topMapH.set(v, (topMapH.get(v) || 0) + 1);
        }

        const bottomSum = total - topSum;
        if (topSum === bottomSum) return true;

        const diff = Math.abs(topSum - bottomSum);
        if (topSum > bottomSum) {
            if (topMapH.has(diff)) return true;
        } else {
            if (bottomMapH.has(diff)) return true;
        }
    }

    // ---------- Vertical cut ----------
    const colSums = new Array(n).fill(0);
    const rightMapV = new Map(); // all cells initially
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const v = grid[i][j];
            colSums[j] += v;
            rightMapV.set(v, (rightMapV.get(v) || 0) + 1);
        }
    }

    let leftSum = 0;
    const leftMapV = new Map();

    for (let j = 0; j < n - 1; ++j) { // cut after column j
        leftSum += colSums[j];
        for (let i = 0; i < m; ++i) {
            const v = grid[i][j];
            // move from right to left
            const cntR = rightMapV.get(v);
            if (cntR === 1) rightMapV.delete(v);
            else rightMapV.set(v, cntR - 1);

            leftMapV.set(v, (leftMapV.get(v) || 0) + 1);
        }

        const rightSum = total - leftSum;
        if (leftSum === rightSum) return true;

        const diff = Math.abs(leftSum - rightSum);
        if (leftSum > rightSum) {
            if (leftMapV.has(diff)) return true;
        } else {
            if (rightMapV.has(diff)) return true;
        }
    }

    return false;
};
```

## Typescript

```typescript
function canPartitionGrid(grid: number[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;

    let total = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) total += grid[i][j];
    }

    // ---------- Horizontal cuts ----------
    const freqBottom = new Map<number, number>();
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const v = grid[i][j];
            freqBottom.set(v, (freqBottom.get(v) ?? 0) + 1);
        }
    }

    let topSum = 0;
    const freqTop = new Map<number, number>();

    for (let i = 0; i < m - 1; ++i) {
        // move row i from bottom to top
        for (let j = 0; j < n; ++j) {
            const v = grid[i][j];
            topSum += v;

            const cntB = freqBottom.get(v)! - 1;
            if (cntB === 0) freqBottom.delete(v);
            else freqBottom.set(v, cntB);

            freqTop.set(v, (freqTop.get(v) ?? 0) + 1);
        }

        const diff = topSum - (total - topSum);
        if (diff === 0) return true;

        if (diff > 0) {
            // need a cell with value diff in the top part
            const rowsTop = i + 1;
            const cellsTop = rowsTop * n;
            if (cellsTop === 1) continue; // cannot remove the only cell

            if (rowsTop > 1 && n > 1) {
                if (freqTop.has(diff)) return true;
            } else {
                if (rowsTop === 1) { // single row
                    if (grid[0][0] === diff || grid[0][n - 1] === diff) return true;
                } else if (n === 1) { // single column
                    if (grid[0][0] === diff || grid[rowsTop - 1][0] === diff) return true;
                }
            }
        } else {
            const need = -diff; // positive
            const rowsBottom = m - i - 1;
            const cellsBottom = rowsBottom * n;
            if (cellsBottom === 1) continue;

            if (rowsBottom > 1 && n > 1) {
                if (freqBottom.has(need)) return true;
            } else {
                if (rowsBottom === 1) { // single row
                    const r = i + 1;
                    if (grid[r][0] === need || grid[r][n - 1] === need) return true;
                } else if (n === 1) { // single column
                    if (grid[i + 1][0] === need || grid[m - 1][0] === need) return true;
                }
            }
        }
    }

    // ---------- Vertical cuts ----------
    const freqRight = new Map<number, number>();
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const v = grid[i][j];
            freqRight.set(v, (freqRight.get(v) ?? 0) + 1);
        }
    }

    let leftSum = 0;
    const freqLeft = new Map<number, number>();

    for (let j = 0; j < n - 1; ++j) {
        // move column j from right to left
        for (let i = 0; i < m; ++i) {
            const v = grid[i][j];
            leftSum += v;

            const cntR = freqRight.get(v)! - 1;
            if (cntR === 0) freqRight.delete(v);
            else freqRight.set(v, cntR);

            freqLeft.set(v, (freqLeft.get(v) ?? 0) + 1);
        }

        const diff = leftSum - (total - leftSum);
        if (diff === 0) return true;

        if (diff > 0) {
            // need a cell with value diff in the left part
            const colsLeft = j + 1;
            const cellsLeft = m * colsLeft;
            if (cellsLeft === 1) continue;

            if (m > 1 && colsLeft > 1) {
                if (freqLeft.has(diff)) return true;
            } else {
                if (m === 1) { // single row
                    if (grid[0][0] === diff || grid[0][j] === diff) return true;
                } else if (colsLeft === 1) { // single column
                    if (grid[0][0] === diff || grid[m - 1][0] === diff) return true;
                }
            }
        } else {
            const need = -diff; // positive
            const colsRight = n - j - 1;
            const cellsRight = m * colsRight;
            if (cellsRight === 1) continue;

            if (m > 1 && colsRight > 1) {
                if (freqRight.has(need)) return true;
            } else {
                if (m === 1) { // single row
                    const cStart = j + 1;
                    if (grid[0][cStart] === need || grid[0][n - 1] === need) return true;
                } else if (colsRight === 1) { // single column
                    const colIdx = j + 1;
                    if (grid[0][colIdx] === need || grid[m - 1][colIdx] === need) return true;
                }
            }
        }
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function canPartitionGrid($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $totalSum = 0;
        $totalFreq = [];

        // compute total sum and frequency map
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $val = $grid[$i][$j];
                $totalSum += $val;
                $totalFreq[$val] = ($totalFreq[$val] ?? 0) + 1;
            }
        }

        // Horizontal cuts
        if ($m > 1) {
            $freqTop = [];
            $freqBottom = $totalFreq;
            $sumTop = 0;

            for ($i = 0; $i < $m - 1; $i++) {
                // add row i to top part
                for ($j = 0; $j < $n; $j++) {
                    $val = $grid[$i][$j];
                    $sumTop += $val;
                    $freqTop[$val] = ($freqTop[$val] ?? 0) + 1;
                    $freqBottom[$val]--;
                    if ($freqBottom[$val] == 0) {
                        unset($freqBottom[$val]);
                    }
                }

                $sumBottom = $totalSum - $sumTop;

                if ($sumTop == $sumBottom) {
                    return true;
                }

                $diff = abs($sumTop - $sumBottom);

                if ($sumTop > $sumBottom) { // top larger
                    if ($i + 1 >= 2) {
                        if (isset($freqTop[$diff])) {
                            return true;
                        }
                    } else { // single row on top
                        if ($grid[0][0] == $diff || $grid[0][$n - 1] == $diff) {
                            return true;
                        }
                    }
                } else { // bottom larger
                    $bottomRows = $m - ($i + 1);
                    if ($bottomRows >= 2) {
                        if (isset($freqBottom[$diff])) {
                            return true;
                        }
                    } else { // single row on bottom (last row)
                        if ($grid[$m - 1][0] == $diff || $grid[$m - 1][$n - 1] == $diff) {
                            return true;
                        }
                    }
                }
            }
        }

        // Vertical cuts
        if ($n > 1) {
            $freqLeft = [];
            $freqRight = $totalFreq;
            $sumLeft = 0;

            for ($j = 0; $j < $n - 1; $j++) {
                // add column j to left part
                for ($i = 0; $i < $m; $i++) {
                    $val = $grid[$i][$j];
                    $sumLeft += $val;
                    $freqLeft[$val] = ($freqLeft[$val] ?? 0) + 1;
                    $freqRight[$val]--;
                    if ($freqRight[$val] == 0) {
                        unset($freqRight[$val]);
                    }
                }

                $sumRight = $totalSum - $sumLeft;

                if ($sumLeft == $sumRight) {
                    return true;
                }

                $diff = abs($sumLeft - $sumRight);

                if ($sumLeft > $sumRight) { // left larger
                    if ($j + 1 >= 2) {
                        if (isset($freqLeft[$diff])) {
                            return true;
                        }
                    } else { // single column on left
                        if ($grid[0][0] == $diff || $grid[$m - 1][0] == $diff) {
                            return true;
                        }
                    }
                } else { // right larger
                    $rightCols = $n - ($j + 1);
                    if ($rightCols >= 2) {
                        if (isset($freqRight[$diff])) {
                            return true;
                        }
                    } else { // single column on right (last column)
                        if ($grid[0][$n - 1] == $diff || $grid[$m - 1][$n - 1] == $diff) {
                            return true;
                        }
                    }
                }
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func canPartitionGrid(_ grid: [[Int]]) -> Bool {
        let m = grid.count
        let n = grid[0].count
        var totalSum: Int64 = 0
        var totalFreq = [Int:Int]()
        for r in 0..<m {
            for c in 0..<n {
                let v = grid[r][c]
                totalSum += Int64(v)
                totalFreq[v, default: 0] += 1
            }
        }
        
        // Horizontal cuts
        var topSum: Int64 = 0
        var topFreq = [Int:Int]()
        if m > 1 {
            for i in 0..<(m-1) {
                // add row i to top side
                for c in 0..<n {
                    let v = grid[i][c]
                    topSum += Int64(v)
                    topFreq[v, default: 0] += 1
                }
                let bottomSum = totalSum - topSum
                if topSum == bottomSum { return true }
                let diff64 = abs(topSum - bottomSum)
                if diff64 == 0 || diff64 > Int.max { continue }
                let diff = Int(diff64)
                
                if topSum > bottomSum {
                    // need to remove from top side
                    if (topFreq[diff] ?? 0) > 0 {
                        let rowsTop = i + 1
                        let cols = n
                        if rowsTop > 1 && cols > 1 { return true }
                        else if rowsTop == 1 && cols >= 2 {
                            // single row, check ends of the row (global column 0 and n-1)
                            if grid[0][0] == diff || grid[0][n-1] == diff { return true }
                        } else if cols == 1 && rowsTop >= 2 {
                            // single column, check topmost or bottommost cell in this side
                            if grid[0][0] == diff || grid[rowsTop-1][0] == diff { return true }
                        }
                    }
                } else {
                    // need to remove from bottom side
                    let topCount = topFreq[diff] ?? 0
                    let totalCount = totalFreq[diff] ?? 0
                    let bottomCount = totalCount - topCount
                    if bottomCount > 0 {
                        let rowsBottom = m - i - 1
                        let cols = n
                        if rowsBottom > 1 && cols > 1 { return true }
                        else if rowsBottom == 1 && cols >= 2 {
                            // single row at index i+1
                            let r = i + 1
                            if grid[r][0] == diff || grid[r][n-1] == diff { return true }
                        } else if cols == 1 && rowsBottom >= 2 {
                            // single column, check first or last row of this side
                            let startRow = i + 1
                            if grid[startRow][0] == diff || grid[m-1][0] == diff { return true }
                        }
                    }
                }
            }
        }
        
        // Vertical cuts
        var leftSum: Int64 = 0
        var leftFreq = [Int:Int]()
        if n > 1 {
            for j in 0..<(n-1) {
                // add column j to left side
                for r in 0..<m {
                    let v = grid[r][j]
                    leftSum += Int64(v)
                    leftFreq[v, default: 0] += 1
                }
                let rightSum = totalSum - leftSum
                if leftSum == rightSum { return true }
                let diff64 = abs(leftSum - rightSum)
                if diff64 == 0 || diff64 > Int.max { continue }
                let diff = Int(diff64)
                
                if leftSum > rightSum {
                    // remove from left side
                    if (leftFreq[diff] ?? 0) > 0 {
                        let colsLeft = j + 1
                        let rows = m
                        if rows > 1 && colsLeft > 1 { return true }
                        else if rows == 1 && colsLeft >= 2 {
                            // single row, check ends of this segment (col 0 and col j)
                            if grid[0][0] == diff || grid[0][j] == diff { return true }
                        } else if colsLeft == 1 && rows >= 2 {
                            // single column, check topmost or bottommost cell in this side
                            if grid[0][j] == diff || grid[m-1][j] == diff { return true }
                        }
                    }
                } else {
                    // remove from right side
                    let leftCount = leftFreq[diff] ?? 0
                    let totalCount = totalFreq[diff] ?? 0
                    let rightCount = totalCount - leftCount
                    if rightCount > 0 {
                        let colsRight = n - j - 1
                        let rows = m
                        if rows > 1 && colsRight > 1 { return true }
                        else if rows == 1 && colsRight >= 2 {
                            // single row, segment starts at column j+1
                            let startCol = j + 1
                            if grid[0][startCol] == diff || grid[0][n-1] == diff { return true }
                        } else if colsRight == 1 && rows >= 2 {
                            // single column, column index j+1
                            let colIdx = j + 1
                            if grid[0][colIdx] == diff || grid[m-1][colIdx] == diff { return true }
                        }
                    }
                }
            }
        }
        
        return false
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap
import kotlin.math.abs

class Solution {
    fun canPartitionGrid(grid: Array<IntArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        var totalSum = 0L
        val totalFreq = HashMap<Int, Int>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                val v = grid[i][j]
                totalSum += v.toLong()
                totalFreq[v] = (totalFreq[v] ?: 0) + 1
            }
        }

        // Horizontal cuts
        if (m > 1) {
            var topSum = 0L
            val topFreq = HashMap<Int, Int>()
            for (i in 0 until m - 1) {
                // add row i to top part
                for (j in 0 until n) {
                    val v = grid[i][j]
                    topSum += v.toLong()
                    topFreq[v] = (topFreq[v] ?: 0) + 1
                }
                val bottomSum = totalSum - topSum
                if (topSum == bottomSum) return true

                val diffLong = abs(topSum - bottomSum)
                if (diffLong > 100000L) continue
                val diff = diffLong.toInt()
                if (topSum > bottomSum) {
                    // larger side is top
                    val rowsL = i + 1
                    val colsL = n
                    if (rowsL > 1 && colsL > 1) {
                        if ((topFreq[diff] ?: 0) > 0) return true
                    } else if (rowsL == 1) { // single row
                        if (grid[i][0] == diff || grid[i][n - 1] == diff) return true
                    } else if (colsL == 1) { // single column (n==1)
                        if (grid[0][0] == diff || grid[i][0] == diff) return true
                    }
                } else {
                    // larger side is bottom
                    val rowsL = m - i - 1
                    val colsL = n
                    val cntTotal = totalFreq[diff] ?: 0
                    val cntTop = topFreq[diff] ?: 0
                    val cntBottom = cntTotal - cntTop
                    if (rowsL > 1 && colsL > 1) {
                        if (cntBottom > 0) return true
                    } else if (rowsL == 1) { // single row
                        val rowIdx = i + 1
                        if (grid[rowIdx][0] == diff || grid[rowIdx][n - 1] == diff) return true
                    } else if (colsL == 1) { // single column (n==1)
                        if (grid[i + 1][0] == diff || grid[m - 1][0] == diff) return true
                    }
                }
            }
        }

        // Vertical cuts
        if (n > 1) {
            var leftSum = 0L
            val leftFreq = HashMap<Int, Int>()
            for (j in 0 until n - 1) {
                // add column j to left part
                for (i in 0 until m) {
                    val v = grid[i][j]
                    leftSum += v.toLong()
                    leftFreq[v] = (leftFreq[v] ?: 0) + 1
                }
                val rightSum = totalSum - leftSum
                if (leftSum == rightSum) return true

                val diffLong = abs(leftSum - rightSum)
                if (diffLong > 100000L) continue
                val diff = diffLong.toInt()
                if (leftSum > rightSum) {
                    // larger side is left
                    val rowsL = m
                    val colsL = j + 1
                    if (rowsL > 1 && colsL > 1) {
                        if ((leftFreq[diff] ?: 0) > 0) return true
                    } else if (colsL == 1) { // single column
                        if (grid[0][j] == diff || grid[m - 1][j] == diff) return true
                    } else if (rowsL == 1) { // single row (m==1)
                        if (grid[0][j] == diff || grid[0][j] == diff) return true
                    }
                } else {
                    // larger side is right
                    val rowsL = m
                    val colsL = n - j - 1
                    val cntTotal = totalFreq[diff] ?: 0
                    val cntLeft = leftFreq[diff] ?: 0
                    val cntRight = cntTotal - cntLeft
                    if (rowsL > 1 && colsL > 1) {
                        if (cntRight > 0) return true
                    } else if (colsL == 1) { // single column on right side
                        val colIdx = j + 1
                        if (grid[0][colIdx] == diff || grid[m - 1][colIdx] == diff) return true
                    } else if (rowsL == 1) { // single row (m==1)
                        if (grid[0][j + 1] == diff || grid[0][j + 1] == diff) return true
                    }
                }
            }
        }

        return false
    }
}
```

## Dart

```dart
class Solution {
  bool canPartitionGrid(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // Compute total sum and full frequency map
    int totalSum = 0;
    Map<int, int> fullFreq = {};
    for (var row in grid) {
      for (int v in row) {
        totalSum += v;
        fullFreq[v] = (fullFreq[v] ?? 0) + 1;
      }
    }

    // Helper to check cuts given orientation
    bool checkHorizontal() {
      int topSum = 0;
      Map<int, int> topFreq = {};
      Map<int, int> bottomFreq = Map.from(fullFreq);

      for (int i = 0; i < m - 1; ++i) {
        for (int v in grid[i]) {
          topSum += v;

          // move from bottom to top
          int cntBottom = bottomFreq[v]!;
          if (cntBottom == 1) {
            bottomFreq.remove(v);
          } else {
            bottomFreq[v] = cntBottom - 1;
          }
          topFreq[v] = (topFreq[v] ?? 0) + 1;
        }

        int bottomSum = totalSum - topSum;
        if (topSum == bottomSum) return true;

        int diff = (topSum - bottomSum).abs();
        if (diff == 0) return true; // already handled

        if (topSum > bottomSum) {
          if (topFreq.containsKey(diff)) return true;
        } else {
          if (bottomFreq.containsKey(diff)) return true;
        }
      }
      return false;
    }

    bool checkVertical() {
      int leftSum = 0;
      Map<int, int> leftFreq = {};
      Map<int, int> rightFreq = Map.from(fullFreq);

      for (int j = 0; j < n - 1; ++j) {
        for (int i = 0; i < m; ++i) {
          int v = grid[i][j];
          leftSum += v;

          // move from right to left
          int cntRight = rightFreq[v]!;
          if (cntRight == 1) {
            rightFreq.remove(v);
          } else {
            rightFreq[v] = cntRight - 1;
          }
          leftFreq[v] = (leftFreq[v] ?? 0) + 1;
        }

        int rightSum = totalSum - leftSum;
        if (leftSum == rightSum) return true;

        int diff = (leftSum - rightSum).abs();
        if (diff == 0) return true; // already handled

        if (leftSum > rightSum) {
          if (leftFreq.containsKey(diff)) return true;
        } else {
          if (rightFreq.containsKey(diff)) return true;
        }
      }
      return false;
    }

    // Try both orientations
    if (checkHorizontal()) return true;
    if (checkVertical()) return true;
    return false;
  }
}
```

## Golang

```go
func canPartitionGrid(grid [][]int) bool {
    m := len(grid)
    n := len(grid[0])
    // total sum and frequency map of all values
    totalSum := int64(0)
    totalFreq := make(map[int]int, m*n)
    for i := 0; i < m; i++ {
        row := grid[i]
        for j := 0; j < n; j++ {
            v := row[j]
            totalSum += int64(v)
            totalFreq[v]++
        }
    }

    // Horizontal cuts
    if m > 1 {
        // prefix sums of rows
        rowCum := make([]int64, m+1)
        for i := 0; i < m; i++ {
            var s int64
            for _, v := range grid[i] {
                s += int64(v)
            }
            rowCum[i+1] = rowCum[i] + s
        }

        topFreq := make(map[int]int)
        bottomFreq := make(map[int]int, len(totalFreq))
        for k, v := range totalFreq {
            bottomFreq[k] = v
        }

        for r := 0; r < m-1; r++ {
            // move row r from bottom to top
            for _, v := range grid[r] {
                topFreq[v]++
                cnt := bottomFreq[v] - 1
                if cnt == 0 {
                    delete(bottomFreq, v)
                } else {
                    bottomFreq[v] = cnt
                }
            }

            sumTop := rowCum[r+1]
            sumBottom := totalSum - sumTop
            if sumTop == sumBottom {
                return true
            }

            diff := sumTop - sumBottom
            largerIsTop := true
            if diff < 0 {
                diff = -diff
                largerIsTop = false
            }
            d := int(diff)

            var exists bool
            if largerIsTop {
                _, exists = topFreq[d]
            } else {
                _, exists = bottomFreq[d]
            }
            if !exists {
                continue
            }

            // connectivity check
            rowsCnt := r + 1
            if !largerIsTop {
                rowsCnt = m - (r + 1)
            }
            if rowsCnt == 1 {
                var rowIdx int
                if largerIsTop {
                    rowIdx = r
                } else {
                    rowIdx = r + 1
                }
                if grid[rowIdx][0] == d || grid[rowIdx][n-1] == d {
                    return true
                }
            } else {
                // at least 2 rows -> any cell works
                return true
            }
        }
    }

    // Vertical cuts
    if n > 1 {
        // column sums and prefix
        colSum := make([]int64, n)
        for i := 0; i < m; i++ {
            for j, v := range grid[i] {
                colSum[j] += int64(v)
            }
        }
        colCum := make([]int64, n+1)
        for j := 0; j < n; j++ {
            colCum[j+1] = colCum[j] + colSum[j]
        }

        leftFreq := make(map[int]int)
        rightFreq := make(map[int]int, len(totalFreq))
        for k, v := range totalFreq {
            rightFreq[k] = v
        }

        for c := 0; c < n-1; c++ {
            // move column c from right to left
            for i := 0; i < m; i++ {
                v := grid[i][c]
                leftFreq[v]++
                cnt := rightFreq[v] - 1
                if cnt == 0 {
                    delete(rightFreq, v)
                } else {
                    rightFreq[v] = cnt
                }
            }

            sumLeft := colCum[c+1]
            sumRight := totalSum - sumLeft
            if sumLeft == sumRight {
                return true
            }

            diff := sumLeft - sumRight
            largerIsLeft := true
            if diff < 0 {
                diff = -diff
                largerIsLeft = false
            }
            d := int(diff)

            var exists bool
            if largerIsLeft {
                _, exists = leftFreq[d]
            } else {
                _, exists = rightFreq[d]
            }
            if !exists {
                continue
            }

            // connectivity check
            colsCnt := c + 1
            if !largerIsLeft {
                colsCnt = n - (c + 1)
            }
            if colsCnt == 1 {
                var colIdx int
                if largerIsLeft {
                    colIdx = c
                } else {
                    colIdx = c + 1
                }
                if grid[0][colIdx] == d || grid[m-1][colIdx] == d {
                    return true
                }
            } else {
                // at least 2 columns -> any cell works
                return true
            }
        }
    }

    return false
}
```

## Ruby

```ruby
def can_partition_grid(grid)
  m = grid.length
  n = grid[0].length

  total_sum = 0
  total_freq = Hash.new(0)
  grid.each do |row|
    row.each do |v|
      total_sum += v
      total_freq[v] += 1
    end
  end

  # Horizontal cuts
  top_sum = 0
  top_freq = Hash.new(0)
  (0...m - 1).each do |i|
    grid[i].each do |v|
      top_sum += v
      top_freq[v] += 1
    end
    bottom_sum = total_sum - top_sum
    diff = top_sum - bottom_sum

    if diff == 0
      return true
    elsif diff > 0
      need = diff
      top_rows = i + 1
      if top_rows > 1 && n > 1
        return true if top_freq[need] > 0
      else
        # check boundary cells in the top part
        if top_rows == 1 && n == 1
          return true if grid[0][0] == need
        elsif top_rows == 1
          return true if grid[0][0] == need || grid[0][n - 1] == need
        else # n == 1
          return true if grid[0][0] == need || grid[i][0] == need
        end
      end
    else # diff < 0, bottom larger
      need = -diff
      bottom_rows = m - (i + 1)
      if bottom_rows > 1 && n > 1
        have_bottom = total_freq[need] - top_freq[need]
        return true if have_bottom > 0
      else
        start_row = i + 1
        if bottom_rows == 1 && n == 1
          return true if grid[start_row][0] == need
        elsif bottom_rows == 1
          return true if grid[start_row][0] == need || grid[start_row][n - 1] == need
        else # n == 1
          return true if grid[start_row][0] == need || grid[m - 1][0] == need
        end
      end
    end
  end

  # Vertical cuts
  left_sum = 0
  left_freq = Hash.new(0)
  (0...n - 1).each do |j|
    i = 0
    while i < m
      v = grid[i][j]
      left_sum += v
      left_freq[v] += 1
      i += 1
    end
    right_sum = total_sum - left_sum
    diff = left_sum - right_sum

    if diff == 0
      return true
    elsif diff > 0
      need = diff
      left_cols = j + 1
      if left_cols > 1 && m > 1
        return true if left_freq[need] > 0
      else
        # check boundary cells in the left part
        if left_cols == 1 && m == 1
          return true if grid[0][0] == need
        elsif left_cols == 1
          return true if grid[0][j] == need || grid[m - 1][j] == need
        else # m == 1
          return true if grid[0][0] == need || grid[0][j] == need
        end
      end
    else # diff < 0, right larger
      need = -diff
      right_cols = n - (j + 1)
      if right_cols > 1 && m > 1
        have_right = total_freq[need] - left_freq[need]
        return true if have_right > 0
      else
        start_col = j + 1
        if right_cols == 1 && m == 1
          return true if grid[0][start_col] == need
        elsif right_cols == 1
          return true if grid[0][start_col] == need || grid[m - 1][start_col] == need
        else # m == 1
          return true if grid[0][start_col] == need || grid[0][n - 1] == need
        end
      end
    end
  end

  false
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.{HashMap => MutableMap}

    def canPartitionGrid(grid: Array[Array[Int]]): Boolean = {
        val m = grid.length
        val n = grid(0).length

        var totalSum: Long = 0L
        val totalFreq = MutableMap[Int, Int]()
        for (i <- 0 until m) {
            val row = grid(i)
            for (j <- 0 until n) {
                val v = row(j)
                totalSum += v
                totalFreq(v) = totalFreq.getOrElse(v, 0) + 1
            }
        }

        // Horizontal cuts
        var topSum: Long = 0L
        val topFreq = MutableMap[Int, Int]()
        val bottomFreq = totalFreq.clone()
        for (r <- 0 until m - 1) {
            val row = grid(r)
            for (j <- 0 until n) {
                val v = row(j)
                topSum += v
                topFreq(v) = topFreq.getOrElse(v, 0) + 1
                val cnt = bottomFreq(v) - 1
                if (cnt == 0) bottomFreq -= v else bottomFreq(v) = cnt
            }
            val bottomSum = totalSum - topSum
            if (topSum == bottomSum) return true

            val diffLong = math.abs(topSum - bottomSum)
            if (diffLong > 0 && diffLong <= 100000) {
                val diff = diffLong.toInt
                if (topSum > bottomSum) { // need diff in top part
                    val topHeight = r + 1
                    if (topHeight == 1) {
                        if (grid(r)(0) == diff || grid(r)(n - 1) == diff) return true
                    } else {
                        if (topFreq.contains(diff)) return true
                    }
                } else { // need diff in bottom part
                    val bottomHeight = m - r - 1
                    if (bottomHeight == 1) {
                        val rowIdx = r + 1
                        if (grid(rowIdx)(0) == diff || grid(rowIdx)(n - 1) == diff) return true
                    } else {
                        if (bottomFreq.contains(diff)) return true
                    }
                }
            }
        }

        // Vertical cuts
        var leftSum: Long = 0L
        val leftFreq = MutableMap[Int, Int]()
        val rightFreq = totalFreq.clone()
        for (c <- 0 until n - 1) {
            for (i <- 0 until m) {
                val v = grid(i)(c)
                leftSum += v
                leftFreq(v) = leftFreq.getOrElse(v, 0) + 1
                val cnt = rightFreq(v) - 1
                if (cnt == 0) rightFreq -= v else rightFreq(v) = cnt
            }
            val rightSum = totalSum - leftSum
            if (leftSum == rightSum) return true

            val diffLong = math.abs(leftSum - rightSum)
            if (diffLong > 0 && diffLong <= 100000) {
                val diff = diffLong.toInt
                if (leftSum > rightSum) { // need diff in left part
                    val leftWidth = c + 1
                    if (leftWidth == 1) {
                        if (grid(0)(c) == diff || grid(m - 1)(c) == diff) return true
                    } else {
                        if (leftFreq.contains(diff)) return true
                    }
                } else { // need diff in right part
                    val rightWidth = n - c - 1
                    if (rightWidth == 1) {
                        val colIdx = c + 1
                        if (grid(0)(colIdx) == diff || grid(m - 1)(colIdx) == diff) return true
                    } else {
                        if (rightFreq.contains(diff)) return true
                    }
                }
            }
        }

        false
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn can_partition_grid(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();

        // total sum of all cells
        let mut total: i64 = 0;
        for row in &grid {
            for &v in row {
                total += v as i64;
            }
        }

        // ----- Horizontal cuts -----
        {
            let mut bottom_map: HashMap<i32, usize> = HashMap::new();
            for row in &grid {
                for &v in row {
                    *bottom_map.entry(v).or_insert(0) += 1;
                }
            }
            let mut top_map: HashMap<i32, usize> = HashMap::new();
            let mut top_sum: i64 = 0;
            let mut top_rows: usize = 0;

            for r in 0..m {
                // move row r to the top part
                for c in 0..n {
                    let v = grid[r][c];
                    top_sum += v as i64;
                    *top_map.entry(v).or_insert(0) += 1;
                    if let Some(cnt) = bottom_map.get_mut(&v) {
                        *cnt -= 1;
                        if *cnt == 0 {
                            bottom_map.remove(&v);
                        }
                    }
                }
                top_rows += 1;
                let bottom_rows = m - top_rows;
                if bottom_rows == 0 {
                    break; // no cut after the last row
                }

                let bottom_sum = total - top_sum;

                if top_sum == bottom_sum {
                    return true;
                }

                let diff_i64 = (top_sum - bottom_sum).abs();
                if diff_i64 > 100_000 {
                    continue;
                }
                let diff = diff_i64 as i32;

                if top_sum > bottom_sum {
                    // need to remove from the top part
                    if n == 1 {
                        // single column: only first or last row can be removed
                        let v1 = grid[0][0];
                        let v2 = grid[top_rows - 1][0];
                        if v1 == diff || v2 == diff {
                            return true;
                        }
                    } else if top_rows == 1 {
                        // single row: only first or last column can be removed
                        let v1 = grid[0][0];
                        let v2 = grid[0][n - 1];
                        if v1 == diff || v2 == diff {
                            return true;
                        }
                    } else {
                        if top_map.contains_key(&diff) {
                            return true;
                        }
                    }
                } else {
                    // need to remove from the bottom part
                    let start_bottom = top_rows; // first row index of bottom part
                    if n == 1 {
                        // single column
                        let v1 = grid[start_bottom][0];
                        let v2 = grid[m - 1][0];
                        if v1 == diff || v2 == diff {
                            return true;
                        }
                    } else if bottom_rows == 1 {
                        // single row
                        let v1 = grid[start_bottom][0];
                        let v2 = grid[start_bottom][n - 1];
                        if v1 == diff || v2 == diff {
                            return true;
                        }
                    } else {
                        if bottom_map.contains_key(&diff) {
                            return true;
                        }
                    }
                }
            }
        }

        // ----- Vertical cuts -----
        {
            let mut right_map: HashMap<i32, usize> = HashMap::new();
            for row in &grid {
                for &v in row {
                    *right_map.entry(v).or_insert(0) += 1;
                }
            }
            let mut left_map: HashMap<i32, usize> = HashMap::new();
            let mut left_sum: i64 = 0;
            let mut left_cols: usize = 0;

            for c in 0..n {
                // move column c to the left part
                for r in 0..m {
                    let v = grid[r][c];
                    left_sum += v as i64;
                    *left_map.entry(v).or_insert(0) += 1;
                    if let Some(cnt) = right_map.get_mut(&v) {
                        *cnt -= 1;
                        if *cnt == 0 {
                            right_map.remove(&v);
                        }
                    }
                }
                left_cols += 1;
                let right_cols = n - left_cols;
                if right_cols == 0 {
                    break; // no cut after the last column
                }

                let right_sum = total - left_sum;

                if left_sum == right_sum {
                    return true;
                }

                let diff_i64 = (left_sum - right_sum).abs();
                if diff_i64 > 100_000 {
                    continue;
                }
                let diff = diff_i64 as i32;

                if left_sum > right_sum {
                    // need to remove from the left part
                    if m == 1 {
                        // single row: only first or last column in this row can be removed
                        let v1 = grid[0][0];
                        let v2 = grid[0][left_cols - 1];
                        if v1 == diff || v2 == diff {
                            return true;
                        }
                    } else if left_cols == 1 {
                        // single column: only top or bottom cell can be removed
                        let v1 = grid[0][0];
                        let v2 = grid[m - 1][0];
                        if v1 == diff || v2 == diff {
                            return true;
                        }
                    } else {
                        if left_map.contains_key(&diff) {
                            return true;
                        }
                    }
                } else {
                    // need to remove from the right part
                    let start_col = left_cols; // first column index of right part
                    if m == 1 {
                        // single row
                        let v1 = grid[0][start_col];
                        let v2 = grid[0][n - 1];
                        if v1 == diff || v2 == diff {
                            return true;
                        }
                    } else if right_cols == 1 {
                        // single column
                        let v1 = grid[0][start_col];
                        let v2 = grid[m - 1][start_col];
                        if v1 == diff || v2 == diff {
                            return true;
                        }
                    } else {
                        if right_map.contains_key(&diff) {
                            return true;
                        }
                    }
                }
            }
        }

        false
    }
}
```

## Racket

```racket
(define/contract (can-partition-grid grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((grid-vec (list->vector (map list->vector grid)))
         (m (vector-length grid-vec))
         (n (if (= m 0) 0 (vector-length (vector-ref grid-vec 0))))
         (total-sum
          (let loop ((i 0) (acc 0))
            (if (= i m)
                acc
                (loop (+ i 1)
                      (+ acc (let inner ((j 0) (row-acc 0))
                               (if (= j n)
                                   row-acc
                                   (inner (+ j 1) (+ row-acc (vector-ref (vector-ref grid-vec i) j))))))))))
         (global-freq (make-hash)))
    ;; build global frequency map
    (let loop ((i 0))
      (when (< i m)
        (let inner ((j 0))
          (when (< j n)
            (let* ((val (vector-ref (vector-ref grid-vec i) j))
                   (cnt (+ (hash-ref global-freq val 0) 1)))
              (hash-set! global-freq val cnt))
            (inner (+ j 1))))
        (loop (+ i 1))))
    ;; helper to add value to a freq hash
    (define (add-to-hash! h v)
      (hash-set! h v (+ (hash-ref h v 0) 1)))
    ;; check horizontal cuts
    (let ((top-sum 0)
          (prefix-freq (make-hash))
          (found #f))
      (let loop-rows ((i 0))
        (when (and (< i m) (not found))
          ;; add row i to top side
          (let inner ((j 0))
            (when (< j n)
              (let* ((val (vector-ref (vector-ref grid-vec i) j)))
                (set! top-sum (+ top-sum val))
                (add-to-hash! prefix-freq val))
              (inner (+ j 1))))
          ;; if not the last row, evaluate cut after this row
          (when (< i (- m 1))
            (let* ((bottom-sum (- total-sum top-sum)))
              (cond
                [(= top-sum bottom-sum) (set! found #t)]
                [else
                 (let ((diff (abs (- top-sum bottom-sum))))
                   (when (> diff 0)
                     (if (> top-sum bottom-sum)
                         (when (> (hash-ref prefix-freq diff 0) 0) (set! found #t))
                         (let ((cnt (- (hash-ref global-freq diff 0)
                                       (hash-ref prefix-freq diff 0))))
                           (when (> cnt 0) (set! found #t))))))])))
          (loop-rows (+ i 1))))
      (if found
          #t
          ;; check vertical cuts
          (let ((left-sum 0)
                (left-freq (make-hash))
                (found-v #f))
            (let loop-cols ((j 0))
              (when (and (< j n) (not found-v))
                ;; add column j to left side
                (let inner ((i 0))
                  (when (< i m)
                    (let* ((val (vector-ref (vector-ref grid-vec i) j)))
                      (set! left-sum (+ left-sum val))
                      (add-to-hash! left-freq val))
                    (inner (+ i 1))))
                ;; if not the last column, evaluate cut after this column
                (when (< j (- n 1))
                  (let* ((right-sum (- total-sum left-sum)))
                    (cond
                      [(= left-sum right-sum) (set! found-v #t)]
                      [else
                       (let ((diff (abs (- left-sum right-sum))))
                         (when (> diff 0)
                           (if (> left-sum right-sum)
                               (when (> (hash-ref left-freq diff 0) 0) (set! found-v #t))
                               (let ((cnt (- (hash-ref global-freq diff 0)
                                             (hash-ref left-freq diff 0))))
                                 (when (> cnt 0) (set! found-v #t))))))])))
                (loop-cols (+ j 1))))
            found-v)))))
```

## Erlang

```erlang
-module(solution).
-export([can_partition_grid/1]).

-spec can_partition_grid(Grid :: [[integer()]]) -> boolean().
can_partition_grid(Grid) ->
    case check_horizontal(Grid) of
        true -> true;
        false -> check_horizontal(transpose(Grid))
    end.

%% Check horizontal cuts on the given grid.
check_horizontal(Grid) ->
    {Total, RowSums, AllMap} = preprocess(Grid),
    RowsCount = length(RowSums),
    if RowsCount < 2 -> false;
       true -> iterate_rows(Grid, RowSums, #{}, AllMap, 0, Total)
    end.

%% Preprocess grid to compute total sum, row sums and frequency map.
preprocess(Grid) ->
    preprocess(Grid, 0, [], #{}).

preprocess([], AccTotal, RevRowSums, Map) ->
    {AccTotal, lists:reverse(RevRowSums), Map};
preprocess([Row|Rest], AccTotal, RevRowSums, Map) ->
    RowSum = sum_list(Row),
    NewTotal = AccTotal + RowSum,
    NewMap = add_list_to_map(Row, Map),
    preprocess(Rest, NewTotal, [RowSum|RevRowSums], NewMap).

%% Iterate over rows to evaluate possible cuts.
iterate_rows(_, [], _, _, _, _) -> false;
iterate_rows([Row|RestRows]=AllRows, [RowSum|RestSums],
             TopMap, BottomMap, TopSum, Total) ->
    NewTopMap = add_list_to_map(Row, TopMap),
    NewBottomMap = remove_list_from_map(Row, BottomMap),
    NewTopSum = TopSum + RowSum,
    case RestRows of
        [] -> false; % no bottom part left
        _ ->
            BottomSum = Total - NewTopSum,
            case check_cut(NewTopSum, BottomSum, NewTopMap, NewBottomMap) of
                true -> true;
                false -> iterate_rows(RestRows, RestSums,
                                      NewTopMap, NewBottomMap,
                                      NewTopSum, Total)
            end
    end.

%% Check if a cut yields equal sums possibly after removing one element.
check_cut(SumA, SumB, MapA, MapB) ->
    case SumA == SumB of
        true -> true;
        false ->
            Diff = abs(SumA - SumB),
            LargerMap = if SumA > SumB -> MapA; true -> MapB end,
            maps:is_key(Diff, LargerMap)
    end.

%% Helpers for map frequency updates.
add_list_to_map(List, Map) ->
    lists:foldl(fun(V, M) -> inc(M, V) end, Map, List).

remove_list_from_map(List, Map) ->
    lists:foldl(fun(V, M) -> dec(M, V) end, Map, List).

inc(Map, Key) ->
    Count = maps:get(Key, Map, 0),
    maps:put(Key, Count + 1, Map).

dec(Map, Key) ->
    case maps:get(Key, Map, 0) of
        1 -> maps:remove(Key, Map);
        C when C > 1 -> maps:put(Key, C - 1, Map)
    end.

sum_list(List) ->
    lists:foldl(fun(V, Acc) -> V + Acc end, 0, List).

%% Transpose the grid (rows become columns).
transpose(Rows) ->
    case Rows of
        [] -> [];
        [First|_] ->
            N = length(First),
            EmptyCols = lists:duplicate(N, []),
            ColsRev = lists:foldl(fun(Row, Acc) -> add_row_to_cols(Row, Acc) end,
                                  EmptyCols, Rows),
            [lists:reverse(C) || C <- ColsRev]
    end.

add_row_to_cols(Row, ColsAcc) ->
    add_row_to_cols(Row, ColsAcc, []).

add_row_to_cols([], [], NewAcc) ->
    lists:reverse(NewAcc);
add_row_to_cols([V|Vs], [Col|Cols], NewAcc) ->
    UpdatedCol = [V|Col],
    add_row_to_cols(Vs, Cols, [UpdatedCol|NewAcc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_partition_grid(grid :: [[integer]]) :: boolean
  def can_partition_grid(grid) do
    m = length(grid)
    n = grid |> hd() |> length()

    # Compute total sum and frequency map of all values
    {total_sum, freq_total} =
      Enum.reduce(grid, {0, %{}}, fn row, {sum_acc, freq_acc} ->
        Enum.reduce(row, {sum_acc, freq_acc}, fn val, {s, f} ->
          {s + val, Map.update(f, val, 1, &(&1 + 1))}
        end)
      end)

    # Row sums for quick access
    row_sums = Enum.map(grid, &Enum.sum/1)

    # Horizontal cuts
    if m > 1 do
      horizontal_result =
        Enum.reduce_while(0..(m - 2), {0, %{}, freq_total}, fn i,
                                                            {top_sum, top_freq, bottom_freq} ->
          row = Enum.at(grid, i)
          sum_row = Enum.at(row_sums, i)

          top_sum2 = top_sum + sum_row

          {top_freq2, bottom_freq2} =
            Enum.reduce(row, {top_freq, bottom_freq}, fn val,
                                                          {tf, bf} ->
              tf = Map.update(tf, val, 1, &(&1 + 1))

              case Map.get(bf, val) do
                nil -> {tf, bf}
                1 -> {tf, Map.delete(bf, val)}
                cnt -> {tf, Map.put(bf, cnt - 1)}
              end
            end)

          bottom_sum = total_sum - top_sum2
          d = top_sum2 - bottom_sum

          cond do
            d == 0 ->
              {:halt, true}

            d > 0 and Map.has_key?(top_freq2, d) ->
              {:halt, true}

            d < 0 and Map.has_key?(bottom_freq2, -d) ->
              {:halt, true}

            true ->
              {:cont, {top_sum2, top_freq2, bottom_freq2}}
          end
        end)

      case horizontal_result do
        true -> true
        _ -> nil
      end
    else
      nil
    end
    |> case do
      true -> true
      _ ->
        # Prepare columns (transpose)
        col_tuples = List.zip(grid)
        cols = Enum.map(col_tuples, &Tuple.to_list/1)

        col_sums = Enum.map(cols, &Enum.sum/1)

        # Vertical cuts
        if n > 1 do
          vertical_result =
            Enum.reduce_while(0..(n - 2), {0, %{}, freq_total}, fn j,
                                                              {left_sum, left_freq,
                                                               right_freq} ->
              col = Enum.at(cols, j)
              col_sum = Enum.at(col_sums, j)

              left_sum2 = left_sum + col_sum

              {left_freq2, right_freq2} =
                Enum.reduce(col, {left_freq, right_freq}, fn val,
                                                             {lf, rf} ->
                  lf = Map.update(lf, val, 1, &(&1 + 1))

                  case Map.get(rf, val) do
                    nil -> {lf, rf}
                    1 -> {lf, Map.delete(rf, val)}
                    cnt -> {lf, Map.put(rf, cnt - 1)}
                  end
                end)

              right_sum = total_sum - left_sum2
              d = left_sum2 - right_sum

              cond do
                d == 0 ->
                  {:halt, true}

                d > 0 and Map.has_key?(left_freq2, d) ->
                  {:halt, true}

                d < 0 and Map.has_key?(right_freq2, -d) ->
                  {:halt, true}

                true ->
                  {:cont, {left_sum2, left_freq2, right_freq2}}
              end
            end)

          case vertical_result do
            true -> true
            _ -> false
          end
        else
          false
        end
    end
  end
end
```

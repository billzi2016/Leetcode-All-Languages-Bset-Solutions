# 3212. Count Submatrices With Equal Frequency of X and Y

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        int R = grid.size();
        int C = grid[0].size();

        // ---------- count all '.' submatrices ----------
        vector<int> height(C, 0);
        long long dotOnly = 0;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (grid[i][j] == '.') height[j]++; else height[j] = 0;
            }
            vector<pair<int,int>> st; // {height, count}
            long long cur = 0;
            for (int j = 0; j < C; ++j) {
                int cnt = 1;
                while (!st.empty() && st.back().first >= height[j]) {
                    cur -= 1LL * st.back().second * (st.back().first - height[j]);
                    cnt += st.back().second;
                    st.pop_back();
                }
                st.push_back({height[j], cnt});
                cur += height[j];
                dotOnly += cur;
            }
        }

        // ---------- prepare numeric matrix ----------
        vector<vector<int>> val(R, vector<int>(C));
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (grid[i][j] == 'X') val[i][j] = 1;
                else if (grid[i][j] == 'Y') val[i][j] = -1;
                else val[i][j] = 0;
            }
        }

        // Transpose if rows > cols to reduce complexity
        int n = R, m = C;
        vector<vector<int>> a = move(val);
        if (n > m) {
            vector<vector<int>> t(m, vector<int>(n));
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < m; ++j)
                    t[j][i] = a[i][j];
            a.swap(t);
            swap(n, m);
        }

        // ---------- count zero-sum submatrices ----------
        long long zeroSum = 0;
        vector<int> col(m);
        for (int top = 0; top < n; ++top) {
            fill(col.begin(), col.end(), 0);
            for (int bottom = top; bottom < n; ++bottom) {
                for (int j = 0; j < m; ++j) col[j] += a[bottom][j];
                unordered_map<long long,int> freq;
                freq.reserve(m * 2);
                freq.max_load_factor(0.7);
                long long pref = 0;
                freq[0] = 1;
                for (int j = 0; j < m; ++j) {
                    pref += col[j];
                    auto it = freq.find(pref);
                    if (it != freq.end()) {
                        zeroSum += it->second;
                        ++(it->second);
                    } else {
                        freq[pref] = 1;
                    }
                }
            }
        }

        long long result = zeroSum - dotOnly;
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int numberOfSubmatrices(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        // Count all-dot submatrices
        long dotRectangles = 0L;
        int[] height = new int[m];
        java.util.ArrayDeque<int[]> stack = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '.') {
                    height[j] += 1;
                } else {
                    height[j] = 0;
                }
            }
            stack.clear();
            long cur = 0L;
            for (int j = 0; j < m; j++) {
                int cnt = 1;
                while (!stack.isEmpty() && stack.peek()[0] >= height[j]) {
                    int[] top = stack.pop();
                    cnt += top[1];
                    cur -= (long) top[0] * top[1];
                }
                stack.push(new int[]{height[j], cnt});
                cur += (long) height[j] * cnt;
                dotRectangles += cur;
            }
        }

        // Transform grid to numeric values: X=1, Y=-1, .=0
        int rows = n, cols = m;
        int[][] val = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                char c = grid[i][j];
                if (c == 'X') val[i][j] = 1;
                else if (c == 'Y') val[i][j] = -1;
                else val[i][j] = 0;
            }
        }

        // If rows > cols, transpose to reduce complexity
        boolean transposed = false;
        if (rows > cols) {
            int[][] t = new int[cols][rows];
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    t[j][i] = val[i][j];
                }
            }
            val = t;
            int tmp = rows;
            rows = cols;
            cols = tmp;
            transposed = true;
        }

        // Count submatrices with sum zero
        long zeroSumRectangles = 0L;
        int[] colSums = new int[cols];
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        for (int top = 0; top < rows; top++) {
            java.util.Arrays.fill(colSums, 0);
            for (int bottom = top; bottom < rows; bottom++) {
                for (int c = 0; c < cols; c++) {
                    colSums[c] += val[bottom][c];
                }
                map.clear();
                map.put(0, 1);
                int prefix = 0;
                for (int c = 0; c < cols; c++) {
                    prefix += colSums[c];
                    zeroSumRectangles += map.getOrDefault(prefix, 0);
                    map.put(prefix, map.getOrDefault(prefix, 0) + 1);
                }
            }
        }

        long result = zeroSumRectangles - dotRectangles;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        # convert to numeric values: X=1, Y=-1, .=0
        val = [[1 if c == 'X' else -1 if c == 'Y' else 0 for c in row] for row in grid]

        # To reduce complexity, ensure rows <= cols by transposing the numeric matrix
        transposed = False
        if n > m:
            transposed = True
            val = [list(row) for row in zip(*val)]
            n, m = m, n  # swapped

        total_zero = 0
        from collections import defaultdict

        # Count submatrices whose sum (X-Y) is zero using the classic row‑pair + hashmap method
        for top in range(n):
            col_sum = [0] * m
            for bottom in range(top, n):
                row = val[bottom]
                for c in range(m):
                    col_sum[c] += row[c]

                cnt = defaultdict(int)
                cnt[0] = 1
                cur = 0
                for s in col_sum:
                    cur += s
                    total_zero += cnt[cur]
                    cnt[cur] += 1

        # Count submatrices consisting only of '.' (they have sum zero but must be excluded)
        rows, cols = len(grid), len(grid[0])
        height = [0] * cols
        dot_rect = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '.':
                    height[j] += 1
                else:
                    height[j] = 0

            stack = []
            sum_in_row = 0
            for j in range(cols):
                cnt = 1
                while stack and stack[-1][0] >= height[j]:
                    h, c = stack.pop()
                    sum_in_row -= h * c
                    cnt += c
                stack.append((height[j], cnt))
                sum_in_row += height[j] * cnt
                dot_rect += sum_in_row

        return total_zero - dot_rect
```

## Python3

```python
class Solution:
    def numberOfSubmatrices(self, grid):
        from collections import defaultdict
        n = len(grid)
        m = len(grid[0])
        # convert to numeric values: X=1, Y=-1, .=0
        vals = [[1 if c == 'X' else -1 if c == 'Y' else 0 for c in row] for row in grid]

        # ensure rows <= cols for O(rows^2 * cols)
        transposed = False
        if n > m:
            transposed = True
            vals = [list(row) for row in zip(*vals)]
            n, m = m, n  # swap dimensions

        total_zero = 0
        col_sums = [0] * m
        for top in range(n):
            col_sums = [0] * m
            for bottom in range(top, n):
                row = vals[bottom]
                for c in range(m):
                    col_sums[c] += row[c]

                freq = defaultdict(int)
                cur = 0
                freq[0] = 1
                for s in col_sums:
                    cur += s
                    total_zero += freq[cur]
                    freq[cur] += 1

        # count all-zero (only '.') submatrices using histogram method on original grid
        zero_rect = 0
        heights = [0] * m if not transposed else [0] * n
        rows, cols = (n, m) if not transposed else (m, n)
        for i in range(rows):
            for j in range(cols):
                cell = grid[i][j] if not transposed else grid[j][i]
                if cell == '.':
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            sum_in_row = 0
            for j in range(cols):
                cnt = 1
                while stack and stack[-1][0] >= heights[j]:
                    h, c = stack.pop()
                    sum_in_row -= h * c
                    cnt += c
                sum_in_row += heights[j] * cnt
                zero_rect += sum_in_row
                stack.append((heights[j], cnt))

        return total_zero - zero_rect
```

## C

```c
#include <stdlib.h>
#include <string.h>

int numberOfSubmatrices(char** grid, int gridSize, int* gridColSize) {
    int R = gridSize;
    int C = gridColSize[0];
    // Prefix sums per column for quick value access
    int **pref = (int**)malloc((R + 1) * sizeof(int*));
    for (int i = 0; i <= R; ++i) {
        pref[i] = (int*)calloc(C, sizeof(int));
    }
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            int v = 0;
            if (grid[i][j] == 'X') v = 1;
            else if (grid[i][j] == 'Y') v = -1;
            pref[i + 1][j] = pref[i][j] + v;
        }
    }

    const int MAX_SUM = 1000000;               // R*C max absolute sum
    const int OFFSET   = MAX_SUM;              // shift for negative indices
    static int cnt[2 * MAX_SUM + 5];
    static int vis[2 * MAX_SUM + 5];
    int curIter = 1;

    long long zeroSumCount = 0;
    int *colAccum = (int*)calloc(C, sizeof(int));

    for (int top = 0; top < R; ++top) {
        memset(colAccum, 0, C * sizeof(int));
        for (int bottom = top; bottom < R; ++bottom) {
            // update column accumulation between rows top..bottom
            for (int j = 0; j < C; ++j) {
                colAccum[j] += pref[bottom + 1][j] - pref[bottom][j];
            }

            curIter++;
            long long curAns = 0;
            int sum = 0;

            // initialize frequency of prefix sum 0
            int idx0 = OFFSET;
            vis[idx0] = curIter;
            cnt[idx0] = 1;

            for (int j = 0; j < C; ++j) {
                sum += colAccum[j];
                int idx = sum + OFFSET;
                if (vis[idx] != curIter) { vis[idx] = curIter; cnt[idx] = 0; }
                curAns += cnt[idx];
                cnt[idx]++;
            }
            zeroSumCount += curAns;
        }
    }

    // Count submatrices consisting only of '.'
    long long dotRect = 0;
    int *height = (int*)calloc(C, sizeof(int));
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (grid[i][j] == '.') height[j] += 1;
            else height[j] = 0;
        }
        // monotonic stack storing {height, count}
        struct Node { int h; int cnt; };
        struct Node *st = (struct Node*)malloc(C * sizeof(struct Node));
        int topSt = -1;
        long long sum = 0;
        for (int j = 0; j < C; ++j) {
            int cntSame = 1;
            while (topSt >= 0 && st[topSt].h >= height[j]) {
                sum -= (long long)st[topSt].h * st[topSt].cnt;
                cntSame += st[topSt].cnt;
                topSt--;
            }
            st[++topSt] = (struct Node){height[j], cntSame};
            sum += (long long)height[j] * cntSame;
            dotRect += sum;
        }
        free(st);
    }

    free(height);
    free(colAccum);
    for (int i = 0; i <= R; ++i) free(pref[i]);
    free(pref);

    return (int)(zeroSumCount - dotRect);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int NumberOfSubmatrices(char[][] grid) {
        int n = grid.Length;
        int m = grid[0].Length;

        // Convert to int values: X=1, Y=-1, .=0
        int[,] val = new int[n, m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char c = grid[i][j];
                if (c == 'X') val[i, j] = 1;
                else if (c == 'Y') val[i, j] = -1;
                else val[i, j] = 0;
            }
        }

        // Ensure rows <= cols for efficiency
        if (n > m) {
            int[,] trans = new int[m, n];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    trans[j, i] = val[i, j];
            val = trans;
            int tmp = n; n = m; m = tmp;
        }

        long totalZeroSum = 0;
        int[] colSums = new int[m];

        for (int top = 0; top < n; top++) {
            Array.Clear(colSums, 0, m);
            for (int bottom = top; bottom < n; bottom++) {
                for (int c = 0; c < m; c++) {
                    colSums[c] += val[bottom, c];
                }

                var dict = new Dictionary<int, int>();
                dict[0] = 1;
                int prefix = 0;
                foreach (int sum in colSums) {
                    prefix += sum;
                    if (dict.TryGetValue(prefix, out int cnt)) {
                        totalZeroSum += cnt;
                        dict[prefix] = cnt + 1;
                    } else {
                        dict[prefix] = 1;
                    }
                }
            }
        }

        // Count submatrices consisting only of '.'
        long allDot = CountAllDotRectangles(grid);

        long result = totalZeroSum - allDot;
        return (int)result;
    }

    private long CountAllDotRectangles(char[][] grid) {
        int n = grid.Length;
        int m = grid[0].Length;
        int[] height = new int[m];
        long total = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '.') height[j] += 1;
                else height[j] = 0;
            }

            // Monotonic stack storing pairs (height, count)
            int[] stackH = new int[m];
            int[] stackC = new int[m];
            int sp = 0; // stack pointer
            long rowSum = 0;

            for (int j = 0; j < m; j++) {
                int cnt = 1;
                while (sp > 0 && stackH[sp - 1] >= height[j]) {
                    sp--;
                    cnt += stackC[sp];
                    rowSum -= (long)stackH[sp] * stackC[sp];
                }
                stackH[sp] = height[j];
                stackC[sp] = cnt;
                sp++;
                rowSum += (long)height[j] * cnt;
                total += rowSum;
            }
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numberOfSubmatrices = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;

    // Convert to numeric values: X=1, Y=-1, .=0
    const val = new Array(rows);
    for (let i = 0; i < rows; ++i) {
        const row = new Int32Array(cols);
        for (let j = 0; j < cols; ++j) {
            const ch = grid[i][j];
            if (ch === 'X') row[j] = 1;
            else if (ch === 'Y') row[j] = -1;
            // '.' stays 0
        }
        val[i] = row;
    }

    // Count submatrices with total sum == 0
    let totalZeroSum = 0;
    for (let top = 0; top < rows; ++top) {
        const colSums = new Int32Array(cols);
        for (let bottom = top; bottom < rows; ++bottom) {
            const curRow = val[bottom];
            for (let c = 0; c < cols; ++c) {
                colSums[c] += curRow[c];
            }
            // Count zero‑sum subarrays in colSums
            const map = new Map();
            map.set(0, 1);
            let cum = 0;
            for (let c = 0; c < cols; ++c) {
                cum += colSums[c];
                const prev = map.get(cum) || 0;
                totalZeroSum += prev;
                map.set(cum, prev + 1);
            }
        }
    }

    // Count submatrices consisting only of '.' (all zeros)
    let zeroOnly = 0;
    const heights = new Int32Array(cols);
    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            if (grid[i][j] === '.') heights[j] += 1;
            else heights[j] = 0;
        }
        const stack = []; // each element: [height, count]
        let sum = 0;
        for (let j = 0; j < cols; ++j) {
            let cnt = 1;
            while (stack.length && stack[stack.length - 1][0] >= heights[j]) {
                const [h, c] = stack.pop();
                sum -= h * c;
                cnt += c;
            }
            stack.push([heights[j], cnt]);
            sum += heights[j] * cnt;
            zeroOnly += sum;
        }
    }

    // Submatrices with equal X and Y and at least one X
    return totalZeroSum - zeroOnly;
};
```

## Typescript

```typescript
function numberOfSubmatrices(grid: string[][]): number {
    const n = grid.length;
    const m = grid[0].length;

    // numeric values: X=1, Y=-1, .=0
    const val = Array.from({ length: n }, () => new Int32Array(m));
    // dot indicator
    const isDot = Array.from({ length: n }, () => new Uint8Array(m));

    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            const ch = grid[i][j];
            if (ch === 'X') val[i][j] = 1;
            else if (ch === 'Y') val[i][j] = -1;
            // '.' stays 0
            isDot[i][j] = ch === '.' ? 1 : 0;
        }
    }

    // Count submatrices with sum == 0
    let zeroSum = 0;
    const colSums = new Int32Array(m);
    for (let top = 0; top < n; ++top) {
        colSums.fill(0);
        for (let bottom = top; bottom < n; ++bottom) {
            for (let c = 0; c < m; ++c) {
                colSums[c] += val[bottom][c];
            }
            const prefixMap = new Map<number, number>();
            let pref = 0;
            prefixMap.set(0, 1);
            for (let c = 0; c < m; ++c) {
                pref += colSums[c];
                const cnt = prefixMap.get(pref) ?? 0;
                zeroSum += cnt;
                prefixMap.set(pref, cnt + 1);
            }
        }
    }

    // Count submatrices consisting only of '.'
    let dotOnly = 0;
    const heights = new Int32Array(m);
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            if (isDot[i][j]) heights[j] += 1;
            else heights[j] = 0;
        }
        const stack: number[] = [];
        const sumArr = new Array<number>(m).fill(0);
        for (let j = 0; j < m; ++j) {
            while (stack.length && heights[stack[stack.length - 1]] >= heights[j]) {
                stack.pop();
            }
            if (stack.length === 0) {
                sumArr[j] = heights[j] * (j + 1);
            } else {
                const prev = stack[stack.length - 1];
                sumArr[j] = sumArr[prev] + heights[j] * (j - prev);
            }
            dotOnly += sumArr[j];
            stack.push(j);
        }
    }

    return zeroSum - dotOnly;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function numberOfSubmatrices($grid) {
        $n = count($grid);
        if ($n == 0) return 0;
        $m = count($grid[0]);

        // map characters to numbers: X -> 1, Y -> -1, . -> 0
        $val = array_fill(0, $n, array_fill(0, $m, 0));
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $m; ++$j) {
                if ($grid[$i][$j] === 'X') {
                    $val[$i][$j] = 1;
                } elseif ($grid[$i][$j] === 'Y') {
                    $val[$i][$j] = -1;
                }
            }
        }

        // count submatrices with total sum == 0
        $totalZero = 0;
        for ($top = 0; $top < $n; ++$top) {
            $colSums = array_fill(0, $m, 0);
            for ($bottom = $top; $bottom < $n; ++$bottom) {
                for ($c = 0; $c < $m; ++$c) {
                    $colSums[$c] += $val[$bottom][$c];
                }
                // count zero‑sum subarrays in colSums
                $prefixMap = [0 => 1];
                $pref = 0;
                for ($c = 0; $c < $m; ++$c) {
                    $pref += $colSums[$c];
                    if (isset($prefixMap[$pref])) {
                        $totalZero += $prefixMap[$pref];
                        $prefixMap[$pref] += 1;
                    } else {
                        $prefixMap[$pref] = 1;
                    }
                }
            }
        }

        // count submatrices consisting only of '.'
        $totalDot = 0;
        $heights = array_fill(0, $m, 0);
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $m; ++$j) {
                if ($grid[$i][$j] === '.') {
                    $heights[$j] += 1;
                } else {
                    $heights[$j] = 0;
                }
            }

            // monotonic stack to count rectangles ending at current row
            $stack = [];
            $sum = 0;
            for ($j = 0; $j < $m; ++$j) {
                $cnt = 1;
                while (!empty($stack) && $stack[count($stack) - 1][0] >= $heights[$j]) {
                    $top = array_pop($stack);
                    $sum -= $top[0] * $top[1];
                    $cnt += $top[1];
                }
                $sum += $heights[$j] * $cnt;
                $totalDot += $sum;
                $stack[] = [$heights[$j], $cnt];
            }
        }

        // required submatrices have sum 0 and at least one X
        return (int)($totalZero - $totalDot);
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSubmatrices(_ grid: [[Character]]) -> Int {
        let r = grid.count
        guard r > 0 else { return 0 }
        let c = grid[0].count

        // Convert to numeric values: X=1, Y=-1, .=0
        var vals = Array(repeating: Array(repeating: 0, count: c), count: r)
        for i in 0..<r {
            for j in 0..<c {
                switch grid[i][j] {
                case "X":
                    vals[i][j] = 1
                case "Y":
                    vals[i][j] = -1
                default:
                    vals[i][j] = 0
                }
            }
        }

        // Ensure rows <= cols for efficiency (transpose if needed)
        var rows = r, cols = c
        var matrix = vals
        if rows > cols {
            rows = c
            cols = r
            matrix = Array(repeating: Array(repeating: 0, count: cols), count: rows)
            for i in 0..<r {
                for j in 0..<c {
                    matrix[j][i] = vals[i][j]
                }
            }
        }

        var totalZeroSum: Int64 = 0
        var colSums = Array(repeating: 0, count: cols)

        // Enumerate pairs of rows and count zero‑sum subarrays for each compressed column array
        for top in 0..<rows {
            colSums = Array(repeating: 0, count: cols)
            for bottom in top..<rows {
                for j in 0..<cols {
                    colSums[j] += matrix[bottom][j]
                }
                var prefixCount = [Int:Int]()
                prefixCount[0] = 1
                var cur = 0
                for v in colSums {
                    cur += v
                    if let cnt = prefixCount[cur] {
                        totalZeroSum += Int64(cnt)
                        prefixCount[cur] = cnt + 1
                    } else {
                        prefixCount[cur] = 1
                    }
                }
            }
        }

        // Count submatrices consisting only of '.' (all zeros) to subtract them later
        var height = Array(repeating: 0, count: c)
        var totalDotOnly: Int64 = 0
        for i in 0..<r {
            for j in 0..<c {
                if grid[i][j] == "." {
                    height[j] += 1
                } else {
                    height[j] = 0
                }
            }
            var stack: [(h: Int, cnt: Int)] = []
            var sum: Int64 = 0
            for j in 0..<c {
                var cnt = 1
                while let last = stack.last, last.h >= height[j] {
                    stack.removeLast()
                    sum -= Int64(last.h * last.cnt)
                    cnt += last.cnt
                }
                stack.append((h: height[j], cnt: cnt))
                sum += Int64(height[j] * cnt)
                totalDotOnly += sum
            }
        }

        let result = totalZeroSum - totalDotOnly
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSubmatrices(grid: Array<CharArray>): Int {
        val n = grid.size
        val m = grid[0].size

        // ---------- count submatrices consisting only of '.' ----------
        var dotOnlyCount = 0L
        val height = IntArray(m)
        val sumAt = LongArray(m)
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (grid[i][j] == '.') height[j] += 1 else height[j] = 0
            }
            val stackIdx = IntArray(m)
            var top = -1
            for (j in 0 until m) {
                while (top >= 0 && height[stackIdx[top]] >= height[j]) {
                    top--
                }
                if (top == -1) {
                    sumAt[j] = height[j].toLong() * (j + 1)
                } else {
                    val prev = stackIdx[top]
                    sumAt[j] = sumAt[prev] + height[j].toLong() * (j - prev)
                }
                dotOnlyCount += sumAt[j]
                top++
                stackIdx[top] = j
            }
        }

        // ---------- prepare matrix with values 1, -1, 0 ----------
        var rows = n
        var cols = m
        var mat = Array(rows) { IntArray(cols) }
        for (i in 0 until rows) {
            for (j in 0 until cols) {
                mat[i][j] = when (grid[i][j]) {
                    'X' -> 1
                    'Y' -> -1
                    else -> 0
                }
            }
        }

        // Transpose if rows > cols to reduce complexity
        if (rows > cols) {
            val trans = Array(cols) { IntArray(rows) }
            for (i in 0 until rows) {
                for (j in 0 until cols) {
                    trans[j][i] = mat[i][j]
                }
            }
            mat = trans
            val tmp = rows
            rows = cols
            cols = tmp
        }

        // ---------- count submatrices with sum == 0 ----------
        var zeroSumCount = 0L
        val colSums = IntArray(cols)
        for (topRow in 0 until rows) {
            java.util.Arrays.fill(colSums, 0)
            for (bottomRow in topRow until rows) {
                val rowArr = mat[bottomRow]
                for (c in 0 until cols) {
                    colSums[c] += rowArr[c]
                }
                val map = java.util.HashMap<Int, Int>()
                var prefix = 0
                map[prefix] = 1
                for (c in 0 until cols) {
                    prefix += colSums[c]
                    val cnt = map.getOrDefault(prefix, 0)
                    zeroSumCount += cnt.toLong()
                    map[prefix] = cnt + 1
                }
            }
        }

        // ---------- final answer ----------
        val result = (zeroSumCount - dotOnlyCount).coerceAtLeast(0L)
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSubmatrices(List<List<String>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;

    // Build value matrix (X=1, Y=-1, .=0) and dot boolean matrix
    List<List<int>> val = List.generate(rows, (_) => List.filled(cols, 0));
    List<List<bool>> isDot = List.generate(rows, (_) => List.filled(cols, false));

    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        String ch = grid[i][j];
        if (ch == 'X') {
          val[i][j] = 1;
        } else if (ch == 'Y') {
          val[i][j] = -1;
        } // '.' stays 0
        isDot[i][j] = ch == '.';
      }
    }

    // If rows > cols, transpose to make row count minimal for O(r^2*c)
    if (rows > cols) {
      List<List<int>> tVal = List.generate(cols, (_) => List.filled(rows, 0));
      List<List<bool>> tDot = List.generate(cols, (_) => List.filled(rows, false));
      for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
          tVal[j][i] = val[i][j];
          tDot[j][i] = isDot[i][j];
        }
      }
      val = tVal;
      isDot = tDot;
      int tmp = rows;
      rows = cols;
      cols = tmp;
    }

    int totalZeroSum = _countZeroSumSubmatrices(val, rows, cols);
    int totalAllDot = _countAllDotSubmatrices(isDot, rows, cols);
    return totalZeroSum - totalAllDot;
  }

  int _countZeroSumSubmatrices(List<List<int>> a, int rows, int cols) {
    int ans = 0;
    List<int> colSums = List.filled(cols, 0);
    for (int top = 0; top < rows; ++top) {
      // reset column sums
      for (int c = 0; c < cols; ++c) colSums[c] = 0;
      for (int bottom = top; bottom < rows; ++bottom) {
        for (int c = 0; c < cols; ++c) {
          colSums[c] += a[bottom][c];
        }
        // count subarrays with sum zero in colSums
        Map<int, int> freq = {0: 1};
        int prefix = 0;
        for (int v in colSums) {
          prefix += v;
          ans += freq[prefix] ?? 0;
          freq[prefix] = (freq[prefix] ?? 0) + 1;
        }
      }
    }
    return ans;
  }

  int _countAllDotSubmatrices(List<List<bool>> dot, int rows, int cols) {
    int ans = 0;
    List<int> heights = List.filled(cols, 0);
    for (int i = 0; i < rows; ++i) {
      // update histogram heights
      for (int j = 0; j < cols; ++j) {
        if (dot[i][j]) {
          heights[j] += 1;
        } else {
          heights[j] = 0;
        }
      }

      // monotonic stack to count rectangles ending at row i
      List<int> stackHeight = [];
      List<int> stackCount = [];
      int sum = 0;
      for (int j = 0; j < cols; ++j) {
        int cnt = 1;
        while (stackHeight.isNotEmpty && stackHeight.last >= heights[j]) {
          int h = stackHeight.removeLast();
          int c = stackCount.removeLast();
          sum -= h * c;
          cnt += c;
        }
        stackHeight.add(heights[j]);
        stackCount.add(cnt);
        sum += heights[j] * cnt;
        ans += sum;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func numberOfSubmatrices(grid [][]byte) int {
    rows := len(grid)
    cols := len(grid[0])

    // Convert grid to numeric values: X=1, Y=-1, .=0
    vals := make([][]int, rows)
    for i := 0; i < rows; i++ {
        vals[i] = make([]int, cols)
        for j := 0; j < cols; j++ {
            switch grid[i][j] {
            case 'X':
                vals[i][j] = 1
            case 'Y':
                vals[i][j] = -1
            default:
                vals[i][j] = 0
            }
        }
    }

    // Transpose if rows > cols to reduce the O(min^2 * max) factor
    r, c := rows, cols
    if r > c {
        transVals := make([][]int, c)
        for i := 0; i < c; i++ {
            transVals[i] = make([]int, r)
            for j := 0; j < r; j++ {
                transVals[i][j] = vals[j][i]
            }
        }
        vals = transVals
        r, c = c, r
    }

    // Count submatrices with sum zero (equal number of X and Y)
    zeroCount := 0
    colSum := make([]int, c)
    for top := 0; top < r; top++ {
        for i := 0; i < c; i++ {
            colSum[i] = 0
        }
        for bottom := top; bottom < r; bottom++ {
            for j := 0; j < c; j++ {
                colSum[j] += vals[bottom][j]
            }
            freq := map[int]int{0: 1}
            prefix := 0
            for _, v := range colSum {
                prefix += v
                if cnt, ok := freq[prefix]; ok {
                    zeroCount += cnt
                }
                freq[prefix]++
            }
        }
    }

    // Count submatrices consisting only of '.' (they were also counted above)
    dotCount := 0
    heights := make([]int, cols)
    type pair struct{ h, c int }
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == '.' {
                heights[j]++
            } else {
                heights[j] = 0
            }
        }
        stack := []pair{}
        sum := 0
        for j := 0; j < cols; j++ {
            cnt := 1
            for len(stack) > 0 && stack[len(stack)-1].h >= heights[j] {
                top := stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                sum -= top.h * top.c
                cnt += top.c
            }
            stack = append(stack, pair{heights[j], cnt})
            sum += heights[j] * cnt
            dotCount += sum
        }
    }

    return zeroCount - dotCount
}
```

## Ruby

```ruby
def number_of_submatrices(grid)
  n = grid.size
  m = grid[0].size

  # Convert characters to numbers: X=>1, Y=>-1, .=>0
  vals = Array.new(n) { Array.new(m) }
  has_x = false
  (0...n).each do |i|
    row = grid[i]
    (0...m).each do |j|
      case row[j]
      when 'X'
        vals[i][j] = 1
        has_x = true
      when 'Y'
        vals[i][j] = -1
      else
        vals[i][j] = 0
      end
    end
  end

  return 0 unless has_x

  # Ensure we iterate over the smaller dimension as rows
  if n > m
    transposed_vals = Array.new(m) { Array.new(n) }
    (0...n).each do |i|
      (0...m).each do |j|
        transposed_vals[j][i] = vals[i][j]
      end
    end
    vals = transposed_vals
    n, m = m, n
  end

  # Count submatrices whose sum is zero using row pair compression
  total_zero_sum = 0
  col_prefix = Array.new(m, 0)

  (0...n).each do |top|
    col_prefix.map! { 0 }
    (top...n).each do |bottom|
      rowb = vals[bottom]
      (0...m).each { |c| col_prefix[c] += rowb[c] }

      freq = Hash.new(0)
      sum = 0
      freq[0] = 1
      (0...m).each do |c|
        sum += col_prefix[c]
        total_zero_sum += freq[sum]
        freq[sum] += 1
      end
    end
  end

  # Count submatrices consisting only of '.' (all zeros)
  rows_orig = grid.size
  cols_orig = grid[0].size
  heights = Array.new(cols_orig, 0)
  zero_rect = 0

  (0...rows_orig).each do |i|
    row = grid[i]
    (0...cols_orig).each do |j|
      if row[j] == '.'
        heights[j] += 1
      else
        heights[j] = 0
      end
    end

    stack = []
    sum_in_row = 0
    (0...cols_orig).each do |j|
      cnt = 1
      while !stack.empty? && stack[-1][0] >= heights[j]
        h, c = stack.pop
        sum_in_row -= h * c
        cnt += c
      end
      sum_in_row += heights[j] * cnt
      zero_rect += sum_in_row
      stack << [heights[j], cnt]
    end
  end

  total_zero_sum - zero_rect
end
```

## Scala

```scala
object Solution {
  def numberOfSubmatrices(grid: Array[Array[Char]]): Int = {
    val n0 = grid.length
    val m0 = if (n0 == 0) 0 else grid(0).length

    // Ensure rows <= cols to minimize O(rows^2 * cols)
    var R = n0
    var C = m0
    var vals: Array[Array[Int]] = null
    var isX: Array[Array[Boolean]] = null

    if (n0 <= m0) {
      R = n0; C = m0
      vals = Array.ofDim[Int](R, C)
      isX = Array.ofDim[Boolean](R, C)
      var i = 0
      while (i < R) {
        var j = 0
        while (j < C) {
          grid(i)(j) match {
            case 'X' => { vals(i)(j) = 1; isX(i)(j) = true }
            case 'Y' => vals(i)(j) = -1
            case _   => // '.' stays 0
          }
          j += 1
        }
        i += 1
      }
    } else {
      // transpose
      R = m0; C = n0
      vals = Array.ofDim[Int](R, C)
      isX = Array.ofDim[Boolean](R, C)
      var i = 0
      while (i < n0) {
        var j = 0
        while (j < m0) {
          val ch = grid(i)(j)
          val ti = j
          val tj = i
          ch match {
            case 'X' => { vals(ti)(tj) = 1; isX(ti)(tj) = true }
            case 'Y' => vals(ti)(tj) = -1
            case _   => // '.'
          }
          j += 1
        }
        i += 1
      }
    }

    var ans: Long = 0L
    val colSum = new Array[Int](C)
    val colHasX = new Array[Boolean](C)

    var top = 0
    while (top < R) {
      java.util.Arrays.fill(colSum, 0)
      java.util.Arrays.fill(colHasX, false)
      var bottom = top
      while (bottom < R) {
        var c = 0
        while (c < C) {
          colSum(c) += vals(bottom)(c)
          if (!colHasX(c) && isX(bottom)(c)) colHasX(c) = true
          c += 1
        }

        // count zero‑sum subarrays for current row pair
        val map = scala.collection.mutable.HashMap[Int, Int]()
        var cur = 0
        map.put(0, 1)
        var totalZero: Long = 0L
        c = 0
        while (c < C) {
          cur += colSum(c)
          totalZero += map.getOrElse(cur, 0)
          map.put(cur, map.getOrElse(cur, 0) + 1)
          c += 1
        }

        // subtract subarrays that contain no 'X' (must be all '.')
        var run: Long = 0L
        var zeroOnly: Long = 0L
        c = 0
        while (c < C) {
          if (colSum(c) == 0 && !colHasX(c)) {
            run += 1
          } else {
            zeroOnly += run * (run + 1) / 2
            run = 0L
          }
          c += 1
        }
        zeroOnly += run * (run + 1) / 2

        ans += totalZero - zeroOnly
        bottom += 1
      }
      top += 1
    }

    ans.toInt
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
        let mut n = grid.len();
        if n == 0 {
            return 0;
        }
        let mut m = grid[0].len();

        // convert to numeric values and dot boolean matrix
        let mut vals = vec![vec![0i32; m]; n];
        let mut dots = vec![vec![false; m]; n];
        for i in 0..n {
            for j in 0..m {
                match grid[i][j] {
                    'X' => {
                        vals[i][j] = 1;
                        dots[i][j] = false;
                    }
                    'Y' => {
                        vals[i][j] = -1;
                        dots[i][j] = false;
                    }
                    _ => {
                        vals[i][j] = 0;
                        dots[i][j] = true;
                    }
                }
            }
        }

        // transpose if rows > cols to reduce complexity
        if n > m {
            let mut t_vals = vec![vec![0i32; n]; m];
            let mut t_dots = vec![vec![false; n]; m];
            for i in 0..n {
                for j in 0..m {
                    t_vals[j][i] = vals[i][j];
                    t_dots[j][i] = dots[i][j];
                }
            }
            std::mem::swap(&mut n, &mut m);
            vals = t_vals;
            dots = t_dots;
        }

        // 1) count all submatrices with sum == 0 (including all-dot ones)
        let mut total_zero: i64 = 0;
        let mut col_sums = vec![0i32; m];
        for top in 0..n {
            col_sums.fill(0);
            for bottom in top..n {
                for c in 0..m {
                    col_sums[c] += vals[bottom][c];
                }
                // count subarrays with sum zero
                let mut prefix: i32 = 0;
                let mut map: HashMap<i32, i32> = HashMap::new();
                map.insert(0, 1);
                for &v in col_sums.iter() {
                    prefix += v;
                    if let Some(cnt) = map.get(&prefix) {
                        total_zero += *cnt as i64;
                    }
                    *map.entry(prefix).or_insert(0) += 1;
                }
            }
        }

        // 2) count submatrices consisting only of '.' (all-dot)
        let mut total_dot: i64 = 0;
        let mut heights = vec![0i32; m];
        for i in 0..n {
            for j in 0..m {
                if dots[i][j] {
                    heights[j] += 1;
                } else {
                    heights[j] = 0;
                }
            }
            // monotonic stack to count rectangles ending at row i
            let mut stack: Vec<(i32, i64)> = Vec::new(); // (height, count)
            let mut sum: i64 = 0;
            for &h in heights.iter() {
                let mut cnt: i64 = 1;
                while let Some(&(prev_h, prev_cnt)) = stack.last() {
                    if prev_h >= h {
                        sum -= (prev_h as i64) * prev_cnt;
                        cnt += prev_cnt;
                        stack.pop();
                    } else {
                        break;
                    }
                }
                stack.push((h, cnt));
                sum += (h as i64) * cnt;
                total_dot += sum;
            }
        }

        let result = total_zero - total_dot;
        result as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-submatrices grid)
  (-> (listof (listof char?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (= rows 0) 0 (length (first grid))))
         ;; transformed values: X=1, Y=-1, .=0
         (trans (make-vector rows))
         ;; dot indicator: 1 if '.', else 0
         (dot (make-vector rows)))
    ;; fill trans and dot vectors
    (for ([i (in-range rows)])
      (let* ((row-list (list-ref grid i))
             (tvec (make-vector cols))
             (dvec (make-vector cols)))
        (for ([j (in-range cols)])
          (define ch (list-ref row-list j))
          (cond [(char=? ch #\X) (vector-set! tvec j 1) (vector-set! dvec j 0)]
                [(char=? ch #\Y) (vector-set! tvec j -1) (vector-set! dvec j 0)]
                [else (vector-set! tvec j 0) (vector-set! dvec j 1)]))
        (vector-set! trans i tvec)
        (vector-set! dot i dvec)))
    ;; column-wise prefix sums for trans and dot
    (define colCum (make-vector (+ rows 1)))
    (define colDotCum (make-vector (+ rows 1)))
    (for ([i (in-range (+ rows 1))])
      (vector-set! colCum i (make-vector cols 0))
      (vector-set! colDotCum i (make-vector cols 0)))
    (for ([r (in-range rows)])
      (let ((prev (vector-ref colCum r))
            (curr (vector-ref colCum (+ r 1)))
            (prevD (vector-ref colDotCum r))
            (currD (vector-ref colDotCum (+ r 1)))
            (trow (vector-ref trans r))
            (drow (vector-ref dot r)))
        (for ([c (in-range cols)])
          (vector-set! curr c (+ (vector-ref prev c) (vector-ref trow c)))
          (vector-set! currD c (+ (vector-ref prevD c) (vector-ref drow c))))))
    ;; main counting
    (define total-zero 0)
    (define total-all-dot 0)
    (for ([top (in-range rows)])
      (let ((colSum (make-vector cols 0))
            (colAllDot (make-vector cols #t)))
        (for ([bottom (in-range top rows)])
          (let ((height (+ 1 (- bottom top))))
            ;; update column sums and dot flags for current row pair
            (let ((trow (vector-ref trans bottom))
                  (drow (vector-ref dot bottom)))
              (for ([c (in-range cols)])
                (define new-sum (+ (vector-ref colSum c) (vector-ref trow c)))
                (vector-set! colSum c new-sum)
                (define dotCnt (- (vector-ref (vector-ref colDotCum (+ bottom 1)) c)
                                  (vector-ref (vector-ref colDotCum top) c)))
                (if (= dotCnt height)
                    (vector-set! colAllDot c #t)
                    (vector-set! colAllDot c #f))))
            ;; count zero‑sum subarrays using hashmap of prefix sums
            (define pref 0)
            (define h (make-hash))
            (hash-set! h 0 1)
            (for ([c (in-range cols)])
              (set! pref (+ pref (vector-ref colSum c)))
              (define cnt (hash-ref h pref 0))
              (set! total-zero (+ total-zero cnt))
              (hash-set! h pref (+ cnt 1)))
            ;; count all‑dot submatrices for this row pair
            (let ((run 0))
              (for ([c (in-range cols)])
                (if (vector-ref colAllDot c)
                    (set! run (+ run 1))
                    (begin
                      (when (> run 0)
                        (set! total-all-dot (+ total-all-dot (quotient (* run (+ run 1)) 2))))
                      (set! run 0))))
              (when (> run 0)
                (set! total-all-dot (+ total-all-dot (quotient (* run (+ run 1)) 2)))))))))
    (- total-zero total-all-dot)))
```

## Erlang

```erlang
-spec number_of_submatrices(Grid :: [[char()]]) -> integer().
number_of_submatrices(Grid) ->
    case Grid of
        [] -> 0;
        _ ->
            C = length(hd(Grid)),
            ValRows = [ [char_val(Ci) || Ci <- Row] || Row <- Grid ],
            DotRows = [ [dot_val(Ci)   || Ci <- Row] || Row <- Grid ],

            ZeroSum = count_zero_sum_submatrices(ValRows, C),
            DotOnly = count_all_dot_submatrices(DotRows, C),

            ZeroSum - DotOnly
    end.

char_val($X) -> 1;
char_val($Y) -> -1;
char_val(_)  -> 0.

dot_val($.) -> 1;
dot_val(_)  -> 0.

%% count submatrices whose sum (with X=1,Y=-1, .=0) equals zero
count_zero_sum_submatrices(Rows, C) ->
    count_top(0, Rows, length(Rows), C, 0).

count_top(_TopIdx, _Rows, Len, _C, Acc) when _TopIdx >= Len -> Acc;
count_top(TopIdx, Rows, Len, C, Acc) ->
    ZeroCol = lists:duplicate(C, 0),
    Acc1 = count_bottom(TopIdx, TopIdx, Rows, Len, C, ZeroCol, Acc),
    count_top(TopIdx + 1, Rows, Len, C, Acc1).

count_bottom(_TopIdx, BottomIdx, _Rows, Len, _C, _ColSum, Acc) when BottomIdx >= Len -> Acc;
count_bottom(TopIdx, BottomIdx, Rows, Len, C, ColSum, Acc) ->
    Row = lists:nth(BottomIdx + 1, Rows),
    NewColSum = lists:zipwith(fun(A,B) -> A + B end, ColSum, Row),
    Add = count_zero_subarrays(NewColSum),
    Acc1 = Acc + Add,
    count_bottom(TopIdx, BottomIdx + 1, Rows, Len, C, NewColSum, Acc1).

count_zero_subarrays(List) ->
    count_zero_subarrays(List, #{0 => 1}, 0, 0).

count_zero_subarrays([], _Map, _Pref, Count) -> Count;
count_zero_subarrays([H|T], Map, Pref, Count) ->
    NewPref = Pref + H,
    Prev = maps:get(NewPref, Map, 0),
    NewCount = Count + Prev,
    NewMap = maps:put(NewPref, Prev + 1, Map),
    count_zero_subarrays(T, NewMap, NewPref, NewCount).

%% count submatrices consisting only of '.' cells
count_all_dot_submatrices(DotRows, C) ->
    count_dot_rows(DotRows, lists:duplicate(C, 0), 0).

count_dot_rows([], _Heights, Acc) -> Acc;
count_dot_rows([Row|Rest], HeightsPrev, Acc) ->
    NewHeights = [ if Cell == 1 -> H + 1; true -> 0 end
                   || {Cell, H} <- lists:zip(Row, HeightsPrev) ],
    Add = count_histogram(NewHeights),
    count_dot_rows(Rest, NewHeights, Acc + Add).

count_histogram(Heights) ->
    {_, _, Total} = lists:foldl(fun(H, {Stack, Sum, Tot}) ->
        {NewStack, NewSum, Cnt} = pop_ge(Stack, Sum, 1, H),
        UpdatedSum = NewSum + H * Cnt,
        { [{H, Cnt}|NewStack], UpdatedSum, Tot + UpdatedSum }
    end, {[], 0, 0}, Heights),
    Total.

pop_ge([], Sum, CntAcc, _H) -> {[], Sum, CntAcc};
pop_ge([{PrevH, PrevCnt}|Rest], Sum, CntAcc, H) when PrevH >= H ->
    NewSum = Sum - PrevH * PrevCnt,
    pop_ge(Rest, NewSum, CntAcc + PrevCnt, H);
pop_ge(Stack, Sum, CntAcc, _H) -> {Stack, Sum, CntAcc}.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_submatrices(grid :: [[char]]) :: integer
  def number_of_submatrices(grid) do
    n = length(grid)
    m = grid |> List.first() |> length()

    # Precompute numeric values for each cell: X -> 1, Y -> -1, . -> 0
    vals =
      Enum.map(grid, fn row ->
        Enum.map(row, fn
          "X" -> 1
          "Y" -> -1
          "." -> 0
        end)
      end)

    total_zero = count_zero_sum_submatrices(vals, n, m)
    total_dot = count_all_dot_rectangles(grid, n, m)

    total_zero - total_dot
  end

  # Count submatrices whose sum is zero (X as +1, Y as -1, . as 0)
  defp count_zero_sum_submatrices(vals, n, m) do
    Enum.reduce(0..(n - 1), 0, fn top, acc_top ->
      col_sums = List.duplicate(0, m)

      acc_top + Enum.reduce(top..(n - 1), {col_sums, 0}, fn bottom, {sums, acc} ->
        row_vals = Enum.at(vals, bottom)

        new_sums =
          Enum.with_index(sums)
          |> Enum.map(fn {sum, idx} -> sum + Enum.at(row_vals, idx) end)

        zero_subarrays = count_zero_sum_subarrays(new_sums)
        {new_sums, acc + zero_subarrays}
      end)
      |> elem(1)
    end)
  end

  # Count subarrays in a 1‑D array whose sum is zero
  defp count_zero_sum_subarrays(arr) do
    {_cnt, _freq, _pref} =
      Enum.reduce(arr, {0, %{0 => 1}, 0}, fn v, {c, freq, pref} ->
        new_pref = pref + v
        add = Map.get(freq, new_pref, 0)
        new_freq = Map.update(freq, new_pref, 1, &(&1 + 1))
        {c + add, new_freq, new_pref}
      end)

    elem({_cnt, _freq, _pref}, 0)
  end

  # Count submatrices consisting only of '.'
  defp count_all_dot_rectangles(grid, n, m) do
    heights = List.duplicate(0, m)

    Enum.reduce(0..(n - 1), {heights, 0}, fn row_idx, {prev_heights, total} ->
      row = Enum.at(grid, row_idx)

      new_heights =
        Enum.with_index(prev_heights)
        |> Enum.map(fn {_h, j} ->
          if Enum.at(row, j) == "." do
            Enum.at(prev_heights, j) + 1
          else
            0
          end
        end)

      added = count_rectangles_in_histogram(new_heights)
      {new_heights, total + added}
    end)
    |> elem(1)
  end

  # Given histogram heights, count rectangles with bottom edge at current row
  defp count_rectangles_in_histogram(heights) do
    Enum.reduce(heights, {[], 0, 0}, fn h, {stack, cur, total} ->
      {new_stack, new_cur, cnt} = pop_higher(stack, cur, 1, h)
      new_cur = new_cur + h * cnt
      total = total + new_cur
      {[{h, cnt} | new_stack], new_cur, total}
    end)
    |> elem(2)
  end

  # Pop from stack while top height >= current height
  defp pop_higher([], cur, cnt, _h), do: {[], cur, cnt}

  defp pop_higher([{ph, pc} | rest], cur, cnt, h) when ph >= h do
    new_cur = cur - ph * pc
    new_cnt = cnt + pc
    pop_higher(rest, new_cur, new_cnt, h)
  end

  defp pop_higher(stack, cur, cnt, _h), do: {stack, cur, cnt}
end
```

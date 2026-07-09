# 3197. Find the Minimum Area to Cover All Ones II

## Cpp

```cpp
class Solution {
public:
    int minimumSum(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        const int INF = 1e9;
        auto areaInRegion = [&](int r1, int r2, int c1, int c2) -> int {
            int minR = n, maxR = -1, minC = m, maxC = -1;
            for (int i = r1; i <= r2; ++i) {
                for (int j = c1; j <= c2; ++j) {
                    if (grid[i][j] == 1) {
                        minR = min(minR, i);
                        maxR = max(maxR, i);
                        minC = min(minC, j);
                        maxC = max(maxC, j);
                    }
                }
            }
            if (maxR == -1) return INF; // no ones
            return (maxR - minR + 1) * (maxC - minC + 1);
        };
        
        int ans = INF;
        // three vertical strips
        for (int c1 = 0; c1 <= m - 3; ++c1) {
            for (int c2 = c1 + 1; c2 <= m - 2; ++c2) {
                int a1 = areaInRegion(0, n - 1, 0, c1);
                int a2 = areaInRegion(0, n - 1, c1 + 1, c2);
                int a3 = areaInRegion(0, n - 1, c2 + 1, m - 1);
                if (a1 == INF || a2 == INF || a3 == INF) continue;
                ans = min(ans, a1 + a2 + a3);
            }
        }
        // three horizontal strips
        for (int r1 = 0; r1 <= n - 3; ++r1) {
            for (int r2 = r1 + 1; r2 <= n - 2; ++r2) {
                int a1 = areaInRegion(0, r1, 0, m - 1);
                int a2 = areaInRegion(r1 + 1, r2, 0, m - 1);
                int a3 = areaInRegion(r2 + 1, n - 1, 0, m - 1);
                if (a1 == INF || a2 == INF || a3 == INF) continue;
                ans = min(ans, a1 + a2 + a3);
            }
        }
        // vertical cut then split right side horizontally
        for (int c = 0; c <= m - 2; ++c) {
            int leftA = areaInRegion(0, n - 1, 0, c);
            if (leftA == INF) continue;
            for (int r = 0; r <= n - 2; ++r) {
                int topR = areaInRegion(0, r, c + 1, m - 1);
                int botR = areaInRegion(r + 1, n - 1, c + 1, m - 1);
                if (topR == INF || botR == INF) continue;
                ans = min(ans, leftA + topR + botR);
            }
        }
        // vertical cut then split left side horizontally
        for (int c = 1; c <= m - 1; ++c) {
            int rightA = areaInRegion(0, n - 1, c, m - 1);
            if (rightA == INF) continue;
            for (int r = 0; r <= n - 2; ++r) {
                int topL = areaInRegion(0, r, 0, c - 1);
                int botL = areaInRegion(r + 1, n - 1, 0, c - 1);
                if (topL == INF || botL == INF) continue;
                ans = min(ans, rightA + topL + botL);
            }
        }
        // horizontal cut then split bottom side vertically
        for (int r = 0; r <= n - 2; ++r) {
            int topA = areaInRegion(0, r, 0, m - 1);
            if (topA == INF) continue;
            for (int c = 0; c <= m - 2; ++c) {
                int leftB = areaInRegion(r + 1, n - 1, 0, c);
                int rightB = areaInRegion(r + 1, n - 1, c + 1, m - 1);
                if (leftB == INF || rightB == INF) continue;
                ans = min(ans, topA + leftB + rightB);
            }
        }
        // horizontal cut then split top side vertically
        for (int r = 1; r <= n - 1; ++r) {
            int bottomA = areaInRegion(r, n - 1, 0, m - 1);
            if (bottomA == INF) continue;
            for (int c = 0; c <= m - 2; ++c) {
                int leftT = areaInRegion(0, r - 1, 0, c);
                int rightT = areaInRegion(0, r - 1, c + 1, m - 1);
                if (leftT == INF || rightT == INF) continue;
                ans = min(ans, bottomA + leftT + rightT);
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Point {
        int r, c;
        Point(int r, int c) { this.r = r; this.c = c; }
    }

    private List<Point> ones;

    // area of minimal bounding rectangle covering all 1's inside the submatrix.
    // returns 0 if there is no 1 in the region.
    private int areaInRegion(int r1, int r2, int c1, int c2) {
        int minR = Integer.MAX_VALUE, maxR = -1;
        int minC = Integer.MAX_VALUE, maxC = -1;
        for (Point p : ones) {
            if (p.r < r1 || p.r > r2 || p.c < c1 || p.c > c2) continue;
            if (p.r < minR) minR = p.r;
            if (p.r > maxR) maxR = p.r;
            if (p.c < minC) minC = p.c;
            if (p.c > maxC) maxC = p.c;
        }
        if (maxR == -1) return 0; // no ones
        return (maxR - minR + 1) * (maxC - minC + 1);
    }

    // minimal sum of areas using exactly two non‑overlapping rectangles,
    // each must contain at least one 1, inside the given region.
    private int twoRectExactArea(int r1, int r2, int c1, int c2) {
        final int INF = Integer.MAX_VALUE / 4;
        int best = INF;

        // vertical splits
        for (int cs = c1; cs < c2; ++cs) {
            int left = areaInRegion(r1, r2, c1, cs);
            int right = areaInRegion(r1, r2, cs + 1, c2);
            if (left > 0 && right > 0) {
                best = Math.min(best, left + right);
            }
        }

        // horizontal splits
        for (int rs = r1; rs < r2; ++rs) {
            int top = areaInRegion(r1, rs, c1, c2);
            int bottom = areaInRegion(rs + 1, r2, c1, c2);
            if (top > 0 && bottom > 0) {
                best = Math.min(best, top + bottom);
            }
        }

        return best;
    }

    public int minimumSum(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        ones = new ArrayList<>();
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 1) ones.add(new Point(i, j));

        final int INF = Integer.MAX_VALUE / 4;
        int answer = INF;

        // three vertical strips
        for (int c1 = 0; c1 <= m - 3; ++c1) {
            for (int c2 = c1 + 1; c2 <= m - 2; ++c2) {
                int a1 = areaInRegion(0, n - 1, 0, c1);
                int a2 = areaInRegion(0, n - 1, c1 + 1, c2);
                int a3 = areaInRegion(0, n - 1, c2 + 1, m - 1);
                if (a1 > 0 && a2 > 0 && a3 > 0) {
                    answer = Math.min(answer, a1 + a2 + a3);
                }
            }
        }

        // three horizontal strips
        for (int r1 = 0; r1 <= n - 3; ++r1) {
            for (int r2 = r1 + 1; r2 <= n - 2; ++r2) {
                int a1 = areaInRegion(0, r1, 0, m - 1);
                int a2 = areaInRegion(r1 + 1, r2, 0, m - 1);
                int a3 = areaInRegion(r2 + 1, n - 1, 0, m - 1);
                if (a1 > 0 && a2 > 0 && a3 > 0) {
                    answer = Math.min(answer, a1 + a2 + a3);
                }
            }
        }

        // vertical cut, left single rectangle, right split into two
        for (int c = 0; c < m - 1; ++c) {
            int leftArea = areaInRegion(0, n - 1, 0, c);
            if (leftArea == 0) continue;
            int rightTwo = twoRectExactArea(0, n - 1, c + 1, m - 1);
            if (rightTwo < INF) {
                answer = Math.min(answer, leftArea + rightTwo);
            }
        }

        // vertical cut, right single rectangle, left split into two
        for (int c = 0; c < m - 1; ++c) {
            int rightArea = areaInRegion(0, n - 1, c + 1, m - 1);
            if (rightArea == 0) continue;
            int leftTwo = twoRectExactArea(0, n - 1, 0, c);
            if (leftTwo < INF) {
                answer = Math.min(answer, rightArea + leftTwo);
            }
        }

        // horizontal cut, top single rectangle, bottom split into two
        for (int r = 0; r < n - 1; ++r) {
            int topArea = areaInRegion(0, r, 0, m - 1);
            if (topArea > 0) {
                int bottomTwo = twoRectExactArea(r + 1, n - 1, 0, m - 1);
                if (bottomTwo < INF) answer = Math.min(answer, topArea + bottomTwo);
            }
            int bottomArea = areaInRegion(r + 1, n - 1, 0, m - 1);
            if (bottomArea > 0) {
                int topTwo = twoRectExactArea(0, r, 0, m - 1);
                if (topTwo < INF) answer = Math.min(answer, bottomArea + topTwo);
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        INF = 10**9

        # helper to compute bounding box area of ones in submatrix [r1..r2][c1..c2]
        def bbox_area(r1, r2, c1, c2):
            min_r, max_r = n, -1
            min_c, max_c = m, -1
            for i in range(r1, r2 + 1):
                row = grid[i]
                for j in range(c1, c2 + 1):
                    if row[j]:
                        if i < min_r: min_r = i
                        if i > max_r: max_r = i
                        if j < min_c: min_c = j
                        if j > max_c: max_c = j
            if max_r == -1:   # no 1's
                return 0
            return (max_r - min_r + 1) * (max_c - min_c + 1)

        ans = INF

        # three vertical strips
        for c1 in range(m):
            for c2 in range(c1 + 1, m):
                a1 = bbox_area(0, n - 1, 0, c1)
                a2 = bbox_area(0, n - 1, c1 + 1, c2)
                a3 = bbox_area(0, n - 1, c2 + 1, m - 1)
                if a1 and a2 and a3:
                    ans = min(ans, a1 + a2 + a3)

        # three horizontal strips
        for r1 in range(n):
            for r2 in range(r1 + 1, n):
                a1 = bbox_area(0, r1, 0, m - 1)
                a2 = bbox_area(r1 + 1, r2, 0, m - 1)
                a3 = bbox_area(r2 + 1, n - 1, 0, m - 1)
                if a1 and a2 and a3:
                    ans = min(ans, a1 + a2 + a3)

        # vertical cut then horizontal split on the other side
        for c in range(m - 1):
            left_area = bbox_area(0, n - 1, 0, c)
            right_area = bbox_area(0, n - 1, c + 1, m - 1)

            if left_area:
                for r in range(n - 1):
                    top = bbox_area(0, r, c + 1, m - 1)
                    bot = bbox_area(r + 1, n - 1, c + 1, m - 1)
                    if top and bot:
                        ans = min(ans, left_area + top + bot)

            if right_area:
                for r in range(n - 1):
                    top = bbox_area(0, r, 0, c)
                    bot = bbox_area(r + 1, n - 1, 0, c)
                    if top and bot:
                        ans = min(ans, right_area + top + bot)

        # horizontal cut then vertical split on the other side
        for r in range(n - 1):
            top_area = bbox_area(0, r, 0, m - 1)
            bottom_area = bbox_area(r + 1, n - 1, 0, m - 1)

            if top_area:
                for c in range(m - 1):
                    left = bbox_area(r + 1, n - 1, 0, c)
                    right = bbox_area(r + 1, n - 1, c + 1, m - 1)
                    if left and right:
                        ans = min(ans, top_area + left + right)

            if bottom_area:
                for c in range(m - 1):
                    left = bbox_area(0, r, 0, c)
                    right = bbox_area(0, r, c + 1, m - 1)
                    if left and right:
                        ans = min(ans, bottom_area + left + right)

        return ans
```

## Python3

```python
class Solution:
    def minimumSum(self, grid):
        from math import inf

        n = len(grid)
        m = len(grid[0])
        ones = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]

        def area_cond(cond):
            min_r, max_r = n, -1
            min_c, max_c = m, -1
            for i, j in ones:
                if cond(i, j):
                    if i < min_r: min_r = i
                    if i > max_r: max_r = i
                    if j < min_c: min_c = j
                    if j > max_c: max_c = j
            if max_r == -1:
                return 0
            return (max_r - min_r + 1) * (max_c - min_c + 1)

        def min_two_area(base_cond):
            best = inf
            # vertical splits
            for c in range(m + 1):
                left = area_cond(lambda i, j, bc=base_cond, col=c: bc(i, j) and j < col)
                right = area_cond(lambda i, j, bc=base_cond, col=c: bc(i, j) and j >= col)
                if left > 0 and right > 0:
                    best = min(best, left + right)
            # horizontal splits
            for r in range(n + 1):
                top = area_cond(lambda i, j, bc=base_cond, row=r: bc(i, j) and i < row)
                bottom = area_cond(lambda i, j, bc=base_cond, row=r: bc(i, j) and i >= row)
                if top > 0 and bottom > 0:
                    best = min(best, top + bottom)
            return best

        ans = inf
        # vertical first cut
        for c in range(m + 1):
            # left side as first rectangle
            area_left = area_cond(lambda i, j, col=c: j < col)
            if area_left > 0:
                two = min_two_area(lambda i, j, col=c: j >= col)
                ans = min(ans, area_left + two)
            # right side as first rectangle
            area_right = area_cond(lambda i, j, col=c: j >= col)
            if area_right > 0:
                two = min_two_area(lambda i, j, col=c: j < col)
                ans = min(ans, area_right + two)

        # horizontal first cut
        for r in range(n + 1):
            # top side as first rectangle
            area_top = area_cond(lambda i, j, row=r: i < row)
            if area_top > 0:
                two = min_two_area(lambda i, j, row=r: i >= row)
                ans = min(ans, area_top + two)
            # bottom side as first rectangle
            area_bottom = area_cond(lambda i, j, row=r: i >= row)
            if area_bottom > 0:
                two = min_two_area(lambda i, j, row=r: i < row)
                ans = min(ans, area_bottom + two)

        return int(ans)
```

## C

```c
int areaRegion(int **grid, int m, int n, int r1, int r2, int c1, int c2) {
    int top = m, bottom = -1, left = n, right = -1;
    for (int i = r1; i <= r2; ++i) {
        for (int j = c1; j <= c2; ++j) {
            if (grid[i][j]) {
                if (i < top) top = i;
                if (i > bottom) bottom = i;
                if (j < left) left = j;
                if (j > right) right = j;
            }
        }
    }
    if (bottom == -1) return 0;               // no ones in this region
    return (bottom - top + 1) * (right - left + 1);
}

int minTwoRectArea(int **grid, int m, int n, int r1, int r2, int c1, int c2) {
    const int INF = 1e9;
    int best = INF;

    // vertical splits
    for (int cs = c1; cs < c2; ++cs) {
        int a = areaRegion(grid, m, n, r1, r2, c1, cs);
        int b = areaRegion(grid, m, n, r1, r2, cs + 1, c2);
        if (a && b && a + b < best) best = a + b;
    }
    // horizontal splits
    for (int rs = r1; rs < r2; ++rs) {
        int a = areaRegion(grid, m, n, r1, rs, c1, c2);
        int b = areaRegion(grid, m, n, rs + 1, r2, c1, c2);
        if (a && b && a + b < best) best = a + b;
    }
    return best;
}

int minimumSum(int** grid, int gridSize, int* gridColSize){
    int m = gridSize;
    int n = gridColSize[0];
    const int INF = 1e9;
    int ans = INF;

    // vertical first split: left single, right two
    for (int c = 0; c < n - 1; ++c) {
        int leftArea = areaRegion(grid, m, n, 0, m - 1, 0, c);
        if (!leftArea) continue;
        int rightTwo = minTwoRectArea(grid, m, n, 0, m - 1, c + 1, n - 1);
        if (rightTwo < INF && leftArea + rightTwo < ans) ans = leftArea + rightTwo;

        // left two, right single
        int rightArea = areaRegion(grid, m, n, 0, m - 1, c + 1, n - 1);
        if (!rightArea) continue;
        int leftTwo = minTwoRectArea(grid, m, n, 0, m - 1, 0, c);
        if (leftTwo < INF && rightArea + leftTwo < ans) ans = rightArea + leftTwo;
    }

    // horizontal first split: top single, bottom two
    for (int r = 0; r < m - 1; ++r) {
        int topArea = areaRegion(grid, m, n, 0, r, 0, n - 1);
        if (!topArea) continue;
        int bottomTwo = minTwoRectArea(grid, m, n, r + 1, m - 1, 0, n - 1);
        if (bottomTwo < INF && topArea + bottomTwo < ans) ans = topArea + bottomTwo;

        // top two, bottom single
        int bottomArea = areaRegion(grid, m, n, r + 1, m - 1, 0, n - 1);
        if (!bottomArea) continue;
        int topTwo = minTwoRectArea(grid, m, n, 0, r, 0, n - 1);
        if (topTwo < INF && bottomArea + topTwo < ans) ans = bottomArea + topTwo;
    }

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumSum(int[][] grid) {
        int n = grid.Length;
        int m = grid[0].Length;
        var ones = new List<(int r, int c)>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) ones.Add((i, j));
            }
        }

        int GetArea(int r1, int r2, int c1, int c2) {
            int minR = n, maxR = -1, minC = m, maxC = -1;
            foreach (var (r, c) in ones) {
                if (r >= r1 && r <= r2 && c >= c1 && c <= c2) {
                    if (r < minR) minR = r;
                    if (r > maxR) maxR = r;
                    if (c < minC) minC = c;
                    if (c > maxC) maxC = c;
                }
            }
            if (maxR == -1) return 0; // no ones
            return (maxR - minR + 1) * (maxC - minC + 1);
        }

        int ans = int.MaxValue;

        // First cut vertical, then split left or right horizontally
        for (int vc = 0; vc < m - 1; vc++) {
            // split left part horizontally
            for (int hr = 0; hr < n - 1; hr++) {
                int a = GetArea(0, hr, 0, vc);
                int b = GetArea(hr + 1, n - 1, 0, vc);
                int c = GetArea(0, n - 1, vc + 1, m - 1);
                if (a > 0 && b > 0 && c > 0) {
                    ans = Math.Min(ans, a + b + c);
                }
            }
            // split right part horizontally
            for (int hr = 0; hr < n - 1; hr++) {
                int a = GetArea(0, n - 1, 0, vc);
                int b = GetArea(0, hr, vc + 1, m - 1);
                int c = GetArea(hr + 1, n - 1, vc + 1, m - 1);
                if (a > 0 && b > 0 && c > 0) {
                    ans = Math.Min(ans, a + b + c);
                }
            }
        }

        // First cut horizontal, then split top or bottom vertically
        for (int hc = 0; hc < n - 1; hc++) {
            // split top part vertically
            for (int vc = 0; vc < m - 1; vc++) {
                int a = GetArea(0, hc, 0, vc);
                int b = GetArea(0, hc, vc + 1, m - 1);
                int c = GetArea(hc + 1, n - 1, 0, m - 1);
                if (a > 0 && b > 0 && c > 0) {
                    ans = Math.Min(ans, a + b + c);
                }
            }
            // split bottom part vertically
            for (int vc = 0; vc < m - 1; vc++) {
                int a = GetArea(0, hc, 0, m - 1);
                int b = GetArea(hc + 1, n - 1, 0, vc);
                int c = GetArea(hc + 1, n - 1, vc + 1, m - 1);
                if (a > 0 && b > 0 && c > 0) {
                    ans = Math.Min(ans, a + b + c);
                }
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number[][]} grid
 * @return {number}
 * /
var minimumSum = function(grid) {
    const R = grid.length;
    const C = grid[0].length;
    // collect positions of all ones
    const ones = [];
    for (let i = 0; i < R; ++i) {
        for (let j = 0; j < C; ++j) {
            if (grid[i][j] === 1) ones.push([i, j]);
        }
    }
    const K = ones.length;
    let answer = Infinity;

    // temporary arrays reused inside loops
    const colHas = new Array(C);
    const colMinRow = new Array(C);
    const colMaxRow = new Array(C);
    const rowHas = new Array(R);
    const rowMinCol = new Array(R);
    const rowMaxCol = new Array(R);

    for (let top = 0; top < R; ++top) {
        for (let bottom = top; bottom < R; ++bottom) {
            for (let left = 0; left < C; ++left) {
                for (let right = left; right < C; ++right) {
                    // area of first rectangle
                    const area1 = (bottom - top + 1) * (right - left + 1);

                    // reset stats
                    for (let c = 0; c < C; ++c) {
                        colHas[c] = false;
                        colMinRow[c] = R;      // large sentinel
                        colMaxRow[c] = -1;
                    }
                    for (let r = 0; r < R; ++r) {
                        rowHas[r] = false;
                        rowMinCol[r] = C;
                        rowMaxCol[r] = -1;
                    }

                    // gather remaining ones outside the first rectangle
                    for (let idx = 0; idx < K; ++idx) {
                        const [r, c] = ones[idx];
                        if (r >= top && r <= bottom && c >= left && c <= right) continue; // covered by rect1
                        // column stats
                        colHas[c] = true;
                        if (r < colMinRow[c]) colMinRow[c] = r;
                        if (r > colMaxRow[c]) colMaxRow[c] = r;
                        // row stats
                        rowHas[r] = true;
                        if (c < rowMinCol[r]) rowMinCol[r] = c;
                        if (c > rowMaxCol[r]) rowMaxCol[r] = c;
                    }

                    // prefix areas for columns (left side)
                    const leftArea = new Array(C).fill(0);
                    let any = false, curMinR = R, curMaxR = -1, curMinC = C, curMaxC = -1;
                    for (let c = 0; c < C; ++c) {
                        if (colHas[c]) {
                            any = true;
                            if (colMinRow[c] < curMinR) curMinR = colMinRow[c];
                            if (colMaxRow[c] > curMaxR) curMaxR = colMaxRow[c];
                            if (c < curMinC) curMinC = c;
                            if (c > curMaxC) curMaxC = c;
                        }
                        if (any) {
                            leftArea[c] = (curMaxR - curMinR + 1) * (curMaxC - curMinC + 1);
                        }
                    }

                    // suffix areas for columns (right side)
                    const rightArea = new Array(C).fill(0);
                    any = false; curMinR = R; curMaxR = -1; curMinC = C; curMaxC = -1;
                    for (let c = C - 1; c >= 0; --c) {
                        if (colHas[c]) {
                            any = true;
                            if (colMinRow[c] < curMinR) curMinR = colMinRow[c];
                            if (colMaxRow[c] > curMaxR) curMaxR = colMaxRow[c];
                            if (c < curMinC) curMinC = c;
                            if (c > curMaxC) curMaxC = c;
                        }
                        if (any) {
                            rightArea[c] = (curMaxR - curMinR + 1) * (curMaxC - curMinC + 1);
                        }
                    }

                    // evaluate vertical splits
                    for (let split = 0; split < C - 1; ++split) {
                        const aL = leftArea[split];
                        const aR = rightArea[split + 1];
                        if (aL > 0 && aR > 0) {
                            const total = area1 + aL + aR;
                            if (total < answer) answer = total;
                        }
                    }

                    // prefix areas for rows (top side)
                    const topArea = new Array(R).fill(0);
                    any = false; let curMinC2 = C, curMaxC2 = -1, curMinR2 = R, curMaxR2 = -1;
                    for (let r = 0; r < R; ++r) {
                        if (rowHas[r]) {
                            any = true;
                            if (rowMinCol[r] < curMinC2) curMinC2 = rowMinCol[r];
                            if (rowMaxCol[r] > curMaxC2) curMaxC2 = rowMaxCol[r];
                            if (r < curMinR2) curMinR2 = r;
                            if (r > curMaxR2) curMaxR2 = r;
                        }
                        if (any) {
                            topArea[r] = (curMaxR2 - curMinR2 + 1) * (curMaxC2 - curMinC2 + 1);
                        }
                    }

                    // suffix areas for rows (bottom side)
                    const bottomArea = new Array(R).fill(0);
                    any = false; curMinC2 = C; curMaxC2 = -1; curMinR2 = R; curMaxR2 = -1;
                    for (let r = R - 1; r >= 0; --r) {
                        if (rowHas[r]) {
                            any = true;
                            if (rowMinCol[r] < curMinC2) curMinC2 = rowMinCol[r];
                            if (rowMaxCol[r] > curMaxC2) curMaxC2 = rowMaxCol[r];
                            if (r < curMinR2) curMinR2 = r;
                            if (r > curMaxR2) curMaxR2 = r;
                        }
                        if (any) {
                            bottomArea[r] = (curMaxR2 - curMinR2 + 1) * (curMaxC2 - curMinC2 + 1);
                        }
                    }

                    // evaluate horizontal splits
                    for (let split = 0; split < R - 1; ++split) {
                        const aT = topArea[split];
                        const aB = bottomArea[split + 1];
                        if (aT > 0 && aB > 0) {
                            const total = area1 + aT + aB;
                            if (total < answer) answer = total;
                        }
                    }
                }
            }
        }
    }

    return answer;
};
```

## Typescript

```typescript
function minimumSum(grid: number[][]): number {
    const n = grid.length;
    const m = grid[0].length;

    const getArea = (r1: number, r2: number, c1: number, c2: number): number => {
        let minR = n, maxR = -1, minC = m, maxC = -1;
        for (let i = r1; i <= r2; i++) {
            for (let j = c1; j <= c2; j++) {
                if (grid[i][j] === 1) {
                    if (i < minR) minR = i;
                    if (i > maxR) maxR = i;
                    if (j < minC) minC = j;
                    if (j > maxC) maxC = j;
                }
            }
        }
        if (maxR === -1) return 0; // no ones
        return (maxR - minR + 1) * (maxC - minC + 1);
    };

    let ans = Number.MAX_SAFE_INTEGER;

    // three vertical strips
    for (let c1 = 0; c1 < m - 2; c1++) {
        for (let c2 = c1 + 1; c2 < m - 1; c2++) {
            const a = getArea(0, n - 1, 0, c1);
            const b = getArea(0, n - 1, c1 + 1, c2);
            const c = getArea(0, n - 1, c2 + 1, m - 1);
            if (a && b && c) {
                ans = Math.min(ans, a + b + c);
            }
        }
    }

    // three horizontal strips
    for (let r1 = 0; r1 < n - 2; r1++) {
        for (let r2 = r1 + 1; r2 < n - 1; r2++) {
            const a = getArea(0, r1, 0, m - 1);
            const b = getArea(r1 + 1, r2, 0, m - 1);
            const c = getArea(r2 + 1, n - 1, 0, m - 1);
            if (a && b && c) {
                ans = Math.min(ans, a + b + c);
            }
        }
    }

    // vertical split then split left or right horizontally
    for (let vc = 0; vc < m - 1; vc++) {
        // split left part horizontally
        for (let hr = 0; hr < n - 1; hr++) {
            const a = getArea(0, hr, 0, vc);
            const b = getArea(hr + 1, n - 1, 0, vc);
            const c = getArea(0, n - 1, vc + 1, m - 1);
            if (a && b && c) ans = Math.min(ans, a + b + c);
        }
        // split right part horizontally
        for (let hr = 0; hr < n - 1; hr++) {
            const a = getArea(0, hr, vc + 1, m - 1);
            const b = getArea(hr + 1, n - 1, vc + 1, m - 1);
            const c = getArea(0, n - 1, 0, vc);
            if (a && b && c) ans = Math.min(ans, a + b + c);
        }
    }

    // horizontal split then split top or bottom vertically
    for (let hr = 0; hr < n - 1; hr++) {
        // split top part vertically
        for (let vc = 0; vc < m - 1; vc++) {
            const a = getArea(0, hr, 0, vc);
            const b = getArea(0, hr, vc + 1, m - 1);
            const c = getArea(hr + 1, n - 1, 0, m - 1);
            if (a && b && c) ans = Math.min(ans, a + b + c);
        }
        // split bottom part vertically
        for (let vc = 0; vc < m - 1; vc++) {
            const a = getArea(hr + 1, n - 1, 0, vc);
            const b = getArea(hr + 1, n - 1, vc + 1, m - 1);
            const c = getArea(0, hr, 0, m - 1);
            if (a && b && c) ans = Math.min(ans, a + b + c);
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
    function minimumSum($grid) {
        $n = count($grid);
        $m = count($grid[0]);
        $INF = PHP_INT_MAX;

        // helper to compute minimal bounding rectangle area of 1's inside a submatrix.
        $area = function(int $r1, int $r2, int $c1, int $c2) use ($grid, $n, $m, $INF): int {
            $minR = $n; $maxR = -1;
            $minC = $m; $maxC = -1;
            for ($i = $r1; $i <= $r2; ++$i) {
                for ($j = $c1; $j <= $c2; ++$j) {
                    if ($grid[$i][$j] == 1) {
                        if ($i < $minR) $minR = $i;
                        if ($i > $maxR) $maxR = $i;
                        if ($j < $minC) $minC = $j;
                        if ($j > $maxC) $maxC = $j;
                    }
                }
            }
            if ($maxR == -1) return $INF; // no 1's
            return ($maxR - $minR + 1) * ($maxC - $minC + 1);
        };

        $ans = $INF;

        // three vertical strips
        for ($c1 = 0; $c1 < $m - 2; ++$c1) {
            for ($c2 = $c1 + 1; $c2 < $m - 1; ++$c2) {
                $a1 = $area(0, $n - 1, 0, $c1);
                $a2 = $area(0, $n - 1, $c1 + 1, $c2);
                $a3 = $area(0, $n - 1, $c2 + 1, $m - 1);
                if ($a1 == $INF || $a2 == $INF || $a3 == $INF) continue;
                $ans = min($ans, $a1 + $a2 + $a3);
            }
        }

        // three horizontal strips
        for ($r1 = 0; $r1 < $n - 2; ++$r1) {
            for ($r2 = $r1 + 1; $r2 < $n - 1; ++$r2) {
                $a1 = $area(0, $r1, 0, $m - 1);
                $a2 = $area($r1 + 1, $r2, 0, $m - 1);
                $a3 = $area($r2 + 1, $n - 1, 0, $m - 1);
                if ($a1 == $INF || $a2 == $INF || $a3 == $INF) continue;
                $ans = min($ans, $a1 + $a2 + $a3);
            }
        }

        // vertical cut then split left side horizontally
        for ($c = 0; $c < $m - 1; ++$c) {
            for ($r = 0; $r < $n - 1; ++$r) {
                $aLtop   = $area(0, $r, 0, $c);
                $aLbottom= $area($r + 1, $n - 1, 0, $c);
                $aR      = $area(0, $n - 1, $c + 1, $m - 1);
                if ($aLtop == $INF || $aLbottom == $INF || $aR == $INF) continue;
                $ans = min($ans, $aLtop + $aLbottom + $aR);
            }
        }

        // vertical cut then split right side horizontally
        for ($c = 0; $c < $m - 1; ++$c) {
            for ($r = 0; $r < $n - 1; ++$r) {
                $aL      = $area(0, $n - 1, 0, $c);
                $aRtop   = $area(0, $r, $c + 1, $m - 1);
                $aRbottom= $area($r + 1, $n - 1, $c + 1, $m - 1);
                if ($aL == $INF || $aRtop == $INF || $aRbottom == $INF) continue;
                $ans = min($ans, $aL + $aRtop + $aRbottom);
            }
        }

        // horizontal cut then split top side vertically
        for ($r = 0; $r < $n - 1; ++$r) {
            for ($c = 0; $c < $m - 1; ++$c) {
                $aTleft   = $area(0, $r, 0, $c);
                $aTright  = $area(0, $r, $c + 1, $m - 1);
                $aB       = $area($r + 1, $n - 1, 0, $m - 1);
                if ($aTleft == $INF || $aTright == $INF || $aB == $INF) continue;
                $ans = min($ans, $aTleft + $aTright + $aB);
            }
        }

        // horizontal cut then split bottom side vertically
        for ($r = 0; $r < $n - 1; ++$r) {
            for ($c = 0; $c < $m - 1; ++$c) {
                $aT       = $area(0, $r, 0, $m - 1);
                $aBleft   = $area($r + 1, $n - 1, 0, $c);
                $aBright  = $area($r + 1, $n - 1, $c + 1, $m - 1);
                if ($aT == $INF || $aBleft == $INF || $aBright == $INF) continue;
                $ans = min($ans, $aT + $aBleft + $aBright);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSum(_ grid: [[Int]]) -> Int {
        let n = grid.count
        let m = grid[0].count
        var answer = Int.max
        
        func area(_ r1: Int, _ r2: Int, _ c1: Int, _ c2: Int) -> Int {
            var minR = n, maxR = -1, minC = m, maxC = -1
            for i in r1...r2 {
                for j in c1...c2 {
                    if grid[i][j] == 1 {
                        if i < minR { minR = i }
                        if i > maxR { maxR = i }
                        if j < minC { minC = j }
                        if j > maxC { maxC = j }
                    }
                }
            }
            if maxR == -1 { return 0 } // no ones
            return (maxR - minR + 1) * (maxC - minC + 1)
        }
        
        // three vertical strips
        if m >= 3 {
            for c1 in 0..<(m - 2) {
                for c2 in (c1 + 1)..<(m - 1) {
                    let a1 = area(0, n - 1, 0, c1)
                    let a2 = area(0, n - 1, c1 + 1, c2)
                    let a3 = area(0, n - 1, c2 + 1, m - 1)
                    if a1 > 0 && a2 > 0 && a3 > 0 {
                        answer = min(answer, a1 + a2 + a3)
                    }
                }
            }
        }
        
        // three horizontal strips
        if n >= 3 {
            for r1 in 0..<(n - 2) {
                for r2 in (r1 + 1)..<(n - 1) {
                    let a1 = area(0, r1, 0, m - 1)
                    let a2 = area(r1 + 1, r2, 0, m - 1)
                    let a3 = area(r2 + 1, n - 1, 0, m - 1)
                    if a1 > 0 && a2 > 0 && a3 > 0 {
                        answer = min(answer, a1 + a2 + a3)
                    }
                }
            }
        }
        
        // vertical cut then horizontal split on the right side
        for c in 0..<(m - 1) {
            for r in 0..<(n - 1) {
                let left = area(0, n - 1, 0, c)
                let topRight = area(0, r, c + 1, m - 1)
                let bottomRight = area(r + 1, n - 1, c + 1, m - 1)
                if left > 0 && topRight > 0 && bottomRight > 0 {
                    answer = min(answer, left + topRight + bottomRight)
                }
            }
        }
        
        // horizontal cut then vertical split on the bottom side
        for r in 0..<(n - 1) {
            for c in 0..<(m - 1) {
                let top = area(0, r, 0, m - 1)
                let bottomLeft = area(r + 1, n - 1, 0, c)
                let bottomRight = area(r + 1, n - 1, c + 1, m - 1)
                if top > 0 && bottomLeft > 0 && bottomRight > 0 {
                    answer = min(answer, top + bottomLeft + bottomRight)
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSum(grid: Array<IntArray>): Int {
        val n = grid.size
        val m = grid[0].size

        fun bbox(r1: Int, r2: Int, c1: Int, c2: Int): Pair<Int, Boolean> {
            var minR = n
            var maxR = -1
            var minC = m
            var maxC = -1
            var cnt = 0
            for (i in r1..r2) {
                for (j in c1..c2) {
                    if (grid[i][j] == 1) {
                        cnt++
                        if (i < minR) minR = i
                        if (i > maxR) maxR = i
                        if (j < minC) minC = j
                        if (j > maxC) maxC = j
                    }
                }
            }
            return if (cnt == 0) Pair(0, false)
            else Pair((maxR - minR + 1) * (maxC - minC + 1), true)
        }

        var ans = Int.MAX_VALUE

        // three vertical groups
        for (c1 in 0 until m - 2) {
            for (c2 in c1 + 1 until m - 1) {
                val a = bbox(0, n - 1, 0, c1)
                if (!a.second) continue
                val b = bbox(0, n - 1, c1 + 1, c2)
                if (!b.second) continue
                val c = bbox(0, n - 1, c2 + 1, m - 1)
                if (!c.second) continue
                ans = minOf(ans, a.first + b.first + c.first)
            }
        }

        // three horizontal groups
        for (r1 in 0 until n - 2) {
            for (r2 in r1 + 1 until n - 1) {
                val a = bbox(0, r1, 0, m - 1); if (!a.second) continue
                val b = bbox(r1 + 1, r2, 0, m - 1); if (!b.second) continue
                val c = bbox(r2 + 1, n - 1, 0, m - 1); if (!c.second) continue
                ans = minOf(ans, a.first + b.first + c.first)
            }
        }

        // left vertical slice + right split horizontally
        for (c in 0 until m - 1) {
            val left = bbox(0, n - 1, 0, c); if (!left.second) continue
            for (r in 0 until n - 1) {
                val topRight = bbox(0, r, c + 1, m - 1); if (!topRight.second) continue
                val bottomRight = bbox(r + 1, n - 1, c + 1, m - 1); if (!bottomRight.second) continue
                ans = minOf(ans, left.first + topRight.first + bottomRight.first)
            }
        }

        // right vertical slice + left split horizontally
        for (c in 1 until m) {
            val right = bbox(0, n - 1, c, m - 1); if (!right.second) continue
            for (r in 0 until n - 1) {
                val topLeft = bbox(0, r, 0, c - 1); if (!topLeft.second) continue
                val bottomLeft = bbox(r + 1, n - 1, 0, c - 1); if (!bottomLeft.second) continue
                ans = minOf(ans, right.first + topLeft.first + bottomLeft.first)
            }
        }

        // top horizontal slice + bottom split vertically
        for (r in 0 until n - 1) {
            val top = bbox(0, r, 0, m - 1); if (!top.second) continue
            for (c in 0 until m - 1) {
                val bl = bbox(r + 1, n - 1, 0, c); if (!bl.second) continue
                val br = bbox(r + 1, n - 1, c + 1, m - 1); if (!br.second) continue
                ans = minOf(ans, top.first + bl.first + br.first)
            }
        }

        // bottom horizontal slice + top split vertically
        for (r in 1 until n) {
            val bottom = bbox(r, n - 1, 0, m - 1); if (!bottom.second) continue
            for (c in 0 until m - 1) {
                val tl = bbox(0, r - 1, 0, c); if (!tl.second) continue
                val tr = bbox(0, r - 1, c + 1, m - 1); if (!tr.second) continue
                ans = minOf(ans, bottom.first + tl.first + tr.first)
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumSum(List<List<int>> grid) {
    int n = grid.length;
    int m = grid[0].length;

    int getArea(int r0, int r1, int c0, int c1) {
      int minR = n, maxR = -1, minC = m, maxC = -1;
      for (int i = r0; i <= r1; ++i) {
        for (int j = c0; j <= c1; ++j) {
          if (grid[i][j] == 1) {
            if (i < minR) minR = i;
            if (i > maxR) maxR = i;
            if (j < minC) minC = j;
            if (j > maxC) maxC = j;
          }
        }
      }
      if (maxR == -1) return -1; // no ones
      return (maxR - minR + 1) * (maxC - minC + 1);
    }

    int ans = 1 << 30;

    // First cut vertical
    for (int c = 0; c < m - 1; ++c) {
      // left as single rectangle
      int areaL = getArea(0, n - 1, 0, c);
      if (areaL != -1) {
        // split right vertically
        for (int c2 = c + 1; c2 < m - 1; ++c2) {
          int a1 = getArea(0, n - 1, c + 1, c2);
          int a2 = getArea(0, n - 1, c2 + 1, m - 1);
          if (a1 != -1 && a2 != -1) {
            ans = ans < areaL + a1 + a2 ? ans : areaL + a1 + a2;
          }
        }
        // split right horizontally
        for (int r = 0; r < n - 1; ++r) {
          int a1 = getArea(0, r, c + 1, m - 1);
          int a2 = getArea(r + 1, n - 1, c + 1, m - 1);
          if (a1 != -1 && a2 != -1) {
            ans = ans < areaL + a1 + a2 ? ans : areaL + a1 + a2;
          }
        }
      }

      // right as single rectangle
      int areaR = getArea(0, n - 1, c + 1, m - 1);
      if (areaR != -1) {
        // split left vertically
        for (int c2 = 0; c2 < c; ++c2) {
          int a1 = getArea(0, n - 1, 0, c2);
          int a2 = getArea(0, n - 1, c2 + 1, c);
          if (a1 != -1 && a2 != -1) {
            ans = ans < areaR + a1 + a2 ? ans : areaR + a1 + a2;
          }
        }
        // split left horizontally
        for (int r = 0; r < n - 1; ++r) {
          int a1 = getArea(0, r, 0, c);
          int a2 = getArea(r + 1, n - 1, 0, c);
          if (a1 != -1 && a2 != -1) {
            ans = ans < areaR + a1 + a2 ? ans : areaR + a1 + a2;
          }
        }
      }
    }

    // First cut horizontal
    for (int r = 0; r < n - 1; ++r) {
      // top as single rectangle
      int areaTop = getArea(0, r, 0, m - 1);
      if (areaTop != -1) {
        // split bottom vertically
        for (int c = 0; c < m - 1; ++c) {
          int a1 = getArea(r + 1, n - 1, 0, c);
          int a2 = getArea(r + 1, n - 1, c + 1, m - 1);
          if (a1 != -1 && a2 != -1) {
            ans = ans < areaTop + a1 + a2 ? ans : areaTop + a1 + a2;
          }
        }
        // split bottom horizontally
        for (int r2 = r + 1; r2 < n - 1; ++r2) {
          int a1 = getArea(r + 1, r2, 0, m - 1);
          int a2 = getArea(r2 + 1, n - 1, 0, m - 1);
          if (a1 != -1 && a2 != -1) {
            ans = ans < areaTop + a1 + a2 ? ans : areaTop + a1 + a2;
          }
        }
      }

      // bottom as single rectangle
      int areaBottom = getArea(r + 1, n - 1, 0, m - 1);
      if (areaBottom != -1) {
        // split top vertically
        for (int c = 0; c < m - 1; ++c) {
          int a1 = getArea(0, r, 0, c);
          int a2 = getArea(0, r, c + 1, m - 1);
          if (a1 != -1 && a2 != -1) {
            ans = ans < areaBottom + a1 + a2 ? ans : areaBottom + a1 + a2;
          }
        }
        // split top horizontally
        for (int r2 = 0; r2 < r; ++r2) {
          int a1 = getArea(0, r2, 0, m - 1);
          int a2 = getArea(r2 + 1, r, 0, m - 1);
          if (a1 != -1 && a2 != -1) {
            ans = ans < areaBottom + a1 + a2 ? ans : areaBottom + a1 + a2;
          }
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func minimumSum(grid [][]int) int {
    n := len(grid)
    m := len(grid[0])

    area := func(r1, r2, c1, c2 int) int {
        minR, maxR := n, -1
        minC, maxC := m, -1
        for i := r1; i <= r2; i++ {
            for j := c1; j <= c2; j++ {
                if grid[i][j] == 1 {
                    if i < minR {
                        minR = i
                    }
                    if i > maxR {
                        maxR = i
                    }
                    if j < minC {
                        minC = j
                    }
                    if j > maxC {
                        maxC = j
                    }
                }
            }
        }
        if maxR == -1 {
            return 0
        }
        return (maxR-minR+1)*(maxC-minC+1)
    }

    const INF = int(1e9)
    ans := INF

    // two vertical cuts
    for c1 := 0; c1 < m-2; c1++ {
        for c2 := c1 + 1; c2 < m-1; c2++ {
            a := area(0, n-1, 0, c1)
            b := area(0, n-1, c1+1, c2)
            c := area(0, n-1, c2+1, m-1)
            if a > 0 && b > 0 && c > 0 {
                sum := a + b + c
                if sum < ans {
                    ans = sum
                }
            }
        }
    }

    // two horizontal cuts
    for r1 := 0; r1 < n-2; r1++ {
        for r2 := r1 + 1; r2 < n-1; r2++ {
            a := area(0, r1, 0, m-1)
            b := area(r1+1, r2, 0, m-1)
            c := area(r2+1, n-1, 0, m-1)
            if a > 0 && b > 0 && c > 0 {
                sum := a + b + c
                if sum < ans {
                    ans = sum
                }
            }
        }
    }

    // vertical cut then split left side horizontally / right side horizontally
    for c := 0; c < m-1; c++ {
        for r := 0; r < n-1; r++ {
            // split left side horizontally
            a := area(0, r, 0, c)
            b := area(r+1, n-1, 0, c)
            d := area(0, n-1, c+1, m-1)
            if a > 0 && b > 0 && d > 0 {
                sum := a + b + d
                if sum < ans {
                    ans = sum
                }
            }
            // split right side horizontally
            a2 := area(0, n-1, 0, c)
            b2 := area(0, r, c+1, m-1)
            c2 := area(r+1, n-1, c+1, m-1)
            if a2 > 0 && b2 > 0 && c2 > 0 {
                sum := a2 + b2 + c2
                if sum < ans {
                    ans = sum
                }
            }
        }
    }

    // horizontal cut then split top side vertically / bottom side vertically
    for r := 0; r < n-1; r++ {
        for c := 0; c < m-1; c++ {
            // split top side vertically
            a := area(0, r, 0, c)
            b := area(0, r, c+1, m-1)
            d := area(r+1, n-1, 0, m-1)
            if a > 0 && b > 0 && d > 0 {
                sum := a + b + d
                if sum < ans {
                    ans = sum
                }
            }
            // split bottom side vertically
            a2 := area(0, r, 0, m-1)
            b2 := area(r+1, n-1, 0, c)
            c2 := area(r+1, n-1, c+1, m-1)
            if a2 > 0 && b2 > 0 && c2 > 0 {
                sum := a2 + b2 + c2
                if sum < ans {
                    ans = sum
                }
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def minimum_sum(grid)
  n = grid.size
  m = grid[0].size
  # prefix sum of ones
  ps = Array.new(n + 1) { Array.new(m + 1, 0) }
  (0...n).each do |i|
    row_sum = 0
    (0...m).each do |j|
      row_sum += grid[i][j]
      ps[i + 1][j + 1] = ps[i][j + 1] + row_sum
    end
  end

  count = lambda do |r1, c1, r2, c2|
    ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
  end

  INF = 1 << 60
  dp = Array.new(4) { {} } # dp[rectangles][key] => min area

  (1..n).each do |h|
    (1..m).each do |w|
      (0..n - h).each do |r1|
        r2 = r1 + h - 1
        (0..m - w).each do |c1|
          c2 = c1 + w - 1
          key = [r1, c1, r2, c2]
          ones = count.call(r1, c1, r2, c2)
          if ones == 0
            dp[0][key] = 0
            dp[1][key] = 0
            dp[2][key] = 0
            dp[3][key] = 0
            next
          else
            dp[0][key] = INF
          end

          # find tight bounding box of ones inside this subgrid
          top = r1
          while top <= r2 && count.call(top, c1, top, c2) == 0
            top += 1
          end
          bottom = r2
          while bottom >= r1 && count.call(bottom, c1, bottom, c2) == 0
            bottom -= 1
          end
          left = c1
          while left <= c2 && count.call(r1, left, r2, left) == 0
            left += 1
          end
          right = c2
          while right >= c1 && count.call(r1, right, r2, right) == 0
            right -= 1
          end
          area_one = (bottom - top + 1) * (right - left + 1)

          (1..3).each do |k|
            best = INF
            # use a single rectangle for this subgrid
            best = area_one if k >= 1 && area_one < best

            # vertical splits
            (c1...c2).each do |col|
              left_key = [r1, c1, r2, col]
              right_key = [r1, col + 1, r2, c2]
              (0..k).each do |kl|
                kr = k - kl
                val = dp[kl][left_key] + dp[kr][right_key]
                best = val if val < best
              end
            end

            # horizontal splits
            (r1...r2).each do |row|
              top_key = [r1, c1, row, c2]
              bottom_key = [row + 1, c1, r2, c2]
              (0..k).each do |kt|
                kb = k - kt
                val = dp[kt][top_key] + dp[kb][bottom_key]
                best = val if val < best
              end
            end

            dp[k][key] = best
          end
        end
      end
    end
  end

  full_key = [0, 0, n - 1, m - 1]
  dp[3][full_key]
end
```

## Scala

```scala
object Solution {
    def minimumSum(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        val m = grid(0).length

        def boundingArea(r1: Int, r2: Int, c1: Int, c2: Int): Int = {
            var minR = Int.MaxValue
            var maxR = -1
            var minC = Int.MaxValue
            var maxC = -1
            var i = r1
            while (i <= r2) {
                val row = grid(i)
                var j = c1
                while (j <= c2) {
                    if (row(j) == 1) {
                        if (i < minR) minR = i
                        if (i > maxR) maxR = i
                        if (j < minC) minC = j
                        if (j > maxC) maxC = j
                    }
                    j += 1
                }
                i += 1
            }
            if (maxR == -1) 0 else (maxR - minR + 1) * (maxC - minC + 1)
        }

        var ans = Int.MaxValue

        // First cut vertical
        for (cv <- 0 until m - 1) {
            val leftR1 = 0; val leftR2 = n - 1; val leftC1 = 0; val leftC2 = cv
            val rightR1 = 0; val rightR2 = n - 1; val rightC1 = cv + 1; val rightC2 = m - 1

            // split left side further
            for (splitSide <- 0 to 1) {
                val (sr1, sr2, sc1, sc2) =
                    if (splitSide == 0) (leftR1, leftR2, leftC1, leftC2)
                    else (rightR1, rightR2, rightC1, rightC2)

                val otherArea = {
                    if (splitSide == 0) boundingArea(rightR1, rightR2, rightC1, rightC2)
                    else boundingArea(leftR1, leftR2, leftC1, leftC2)
                }

                // vertical second cut inside the selected side
                var cv2 = sc1
                while (cv2 < sc2) {
                    val a1 = boundingArea(sr1, sr2, sc1, cv2)
                    val a2 = boundingArea(sr1, sr2, cv2 + 1, sc2)
                    if (a1 > 0 && a2 > 0 && otherArea > 0) {
                        val sum = a1 + a2 + otherArea
                        if (sum < ans) ans = sum
                    }
                    cv2 += 1
                }

                // horizontal second cut inside the selected side
                var rh2 = sr1
                while (rh2 < sr2) {
                    val a1 = boundingArea(sr1, rh2, sc1, sc2)
                    val a2 = boundingArea(rh2 + 1, sr2, sc1, sc2)
                    if (a1 > 0 && a2 > 0 && otherArea > 0) {
                        val sum = a1 + a2 + otherArea
                        if (sum < ans) ans = sum
                    }
                    rh2 += 1
                }
            }
        }

        // First cut horizontal
        for (rh <- 0 until n - 1) {
            val topR1 = 0; val topR2 = rh; val topC1 = 0; val topC2 = m - 1
            val botR1 = rh + 1; val botR2 = n - 1; val botC1 = 0; val botC2 = m - 1

            for (splitSide <- 0 to 1) {
                val (sr1, sr2, sc1, sc2) =
                    if (splitSide == 0) (topR1, topR2, topC1, topC2)
                    else (botR1, botR2, botC1, botC2)

                val otherArea = {
                    if (splitSide == 0) boundingArea(botR1, botR2, botC1, botC2)
                    else boundingArea(topR1, topR2, topC1, topC2)
                }

                // vertical second cut inside the selected side
                var cv2 = sc1
                while (cv2 < sc2) {
                    val a1 = boundingArea(sr1, sr2, sc1, cv2)
                    val a2 = boundingArea(sr1, sr2, cv2 + 1, sc2)
                    if (a1 > 0 && a2 > 0 && otherArea > 0) {
                        val sum = a1 + a2 + otherArea
                        if (sum < ans) ans = sum
                    }
                    cv2 += 1
                }

                // horizontal second cut inside the selected side
                var rh2 = sr1
                while (rh2 < sr2) {
                    val a1 = boundingArea(sr1, rh2, sc1, sc2)
                    val a2 = boundingArea(rh2 + 1, sr2, sc1, sc2)
                    if (a1 > 0 && a2 > 0 && otherArea > 0) {
                        val sum = a1 + a2 + otherArea
                        if (sum < ans) ans = sum
                    }
                    rh2 += 1
                }
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_sum(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let m = grid[0].len();

        // helper to compute minimal bounding rectangle area and count of ones in a subgrid
        fn get_area(
            grid: &Vec<Vec<i32>>,
            r1: usize,
            r2: usize,
            c1: usize,
            c2: usize,
        ) -> (i32, i32) {
            let mut min_r = n as i32;
            let mut max_r = -1i32;
            let mut min_c = m as i32;
            let mut max_c = -1i32;
            let mut cnt = 0i32;
            for i in r1..=r2 {
                for j in c1..=c2 {
                    if grid[i][j] == 1 {
                        cnt += 1;
                        let ir = i as i32;
                        let jc = j as i32;
                        if ir < min_r { min_r = ir; }
                        if ir > max_r { max_r = ir; }
                        if jc < min_c { min_c = jc; }
                        if jc > max_c { max_c = jc; }
                    }
                }
            }
            if cnt == 0 {
                (0, 0)
            } else {
                let area = (max_r - min_r + 1) * (max_c - min_c + 1);
                (area, cnt)
            }
        }

        // helper to compute minimal sum of areas using exactly two rectangles inside a region
        fn min_two(
            grid: &Vec<Vec<i32>>,
            r1: usize,
            r2: usize,
            c1: usize,
            c2: usize,
        ) -> Option<i32> {
            let mut best = i32::MAX;
            // vertical splits
            if c1 < c2 {
                for col in c1..c2 {
                    let (area_l, cnt_l) = get_area(grid, r1, r2, c1, col);
                    let (area_r, cnt_r) = get_area(grid, r1, r2, col + 1, c2);
                    if cnt_l > 0 && cnt_r > 0 {
                        let sum = area_l + area_r;
                        if sum < best { best = sum; }
                    }
                }
            }
            // horizontal splits
            if r1 < r2 {
                for row in r1..r2 {
                    let (area_t, cnt_t) = get_area(grid, r1, row, c1, c2);
                    let (area_b, cnt_b) = get_area(grid, row + 1, r2, c1, c2);
                    if cnt_t > 0 && cnt_b > 0 {
                        let sum = area_t + area_b;
                        if sum < best { best = sum; }
                    }
                }
            }
            if best == i32::MAX { None } else { Some(best) }
        }

        let mut answer = i32::MAX;

        // first cut vertical
        for col in 0..m - 1 {
            // left region [0..n-1][0..col]
            let (area_l, cnt_l) = get_area(&grid, 0, n - 1, 0, col);
            // right region [0..n-1][col+1..m-1]
            let (area_r, cnt_r) = get_area(&grid, 0, n - 1, col + 1, m - 1);

            if cnt_l > 0 {
                if let Some(best_r) = min_two(&grid, 0, n - 1, col + 1, m - 1) {
                    answer = answer.min(area_l + best_r);
                }
            }
            if cnt_r > 0 {
                if let Some(best_l) = min_two(&grid, 0, n - 1, 0, col) {
                    answer = answer.min(area_r + best_l);
                }
            }
        }

        // first cut horizontal
        for row in 0..n - 1 {
            // top region [0..row][0..m-1]
            let (area_t, cnt_t) = get_area(&grid, 0, row, 0, m - 1);
            // bottom region [row+1..n-1][0..m-1]
            let (area_b, cnt_b) = get_area(&grid, row + 1, n - 1, 0, m - 1);

            if cnt_t > 0 {
                if let Some(best_b) = min_two(&grid, row + 1, n - 1, 0, m - 1) {
                    answer = answer.min(area_t + best_b);
                }
            }
            if cnt_b > 0 {
                if let Some(best_t) = min_two(&grid, 0, row, 0, m - 1) {
                    answer = answer.min(area_b + best_t);
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (minimum-sum grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (= rows 0) 0 (length (first grid))))
         (gvec (list->vector
                (map (lambda (row) (list->vector row)) grid)))
         (info-hash (make-hash))
         (dp-hash (make-hash))
         (INF 1000000000))

    ;; retrieve count and bounding box of ones in sub-rectangle [x1,x2)×[y1,y2)
    (define (get-info x1 y1 x2 y2)
      (let ((key (vector x1 y1 x2 y2)))
        (or (hash-ref info-hash key #f)
            (let ((cnt 0)
                  (minr rows) (maxr -1)
                  (minc cols) (maxc -1))
              (do ((i x1 (+ i 1))) ((= i x2))
                (do ((j y1 (+ j 1))) ((= j y2))
                  (when (= (vector-ref (vector-ref gvec i) j) 1)
                    (set! cnt (+ cnt 1))
                    (when (< i minr) (set! minr i))
                    (when (> i maxr) (set! maxr i))
                    (when (< j minc) (set! minc j))
                    (when (> j maxc) (set! maxc j)))))
              (let ((res (vector cnt minr maxr minc maxc)))
                (hash-set! info-hash key res)
                res)))))

    ;; dp(k, sub-rect) = minimal total area to cover all ones in sub-rect
    ;; using exactly k non‑empty rectangles.
    (define (dp k x1 y1 x2 y2)
      (let ((key (vector k x1 y1 x2 y2)))
        (or (hash-ref dp-hash key #f)
            (let* ((info (get-info x1 y1 x2 y2))
                   (cnt  (vector-ref info 0))
                   (result
                    (cond
                      [(= cnt 0) (if (= k 0) 0 INF)]
                      [(= k 0)   INF]
                      [(= k 1)
                       (* (+ (- (vector-ref info 2) (vector-ref info 1)) 1)
                          (+ (- (vector-ref info 4) (vector-ref info 3)) 1))]
                      [else
                       ;; try vertical splits
                       (let loop-vert ((c (+ y1 1)) (best INF))
                         (if (>= c y2)
                             best
                             (let ((best-after-k1
                                    (let loop-k1 ((k1 0) (b best))
                                      (if (> k1 k)
                                          b
                                          (let ((val (+ (dp k1 x1 y1 x2 c)
                                                        (dp (- k k1) x1 c x2 y2))))
                                            (loop-k1 (+ k1 1) (min b val)))))))
                               (loop-vert (+ c 1) (min best best-after-k1))))))
                       ;; try horizontal splits
                       (let loop-horiz ((r (+ x1 1)) (best INF))
                         (if (>= r x2)
                             best
                             (let ((best-after-k1
                                    (let loop-k1 ((k1 0) (b best))
                                      (if (> k1 k)
                                          b
                                          (let ((val (+ (dp k1 x1 y1 r y2)
                                                        (dp (- k k1) r y1 x2 y2))))
                                            (loop-k1 (+ k1 1) (min b val)))))))
                               (loop-horiz (+ r 1) (min best best-after-k1))))))]))
              (hash-set! dp-hash key result)
              result))))

    (dp 3 0 0 rows cols)))
```

## Erlang

```erlang
-spec minimum_sum(Grid :: [[integer()]]) -> integer().
minimum_sum(Grid) ->
    R = length(Grid),
    C = length(hd(Grid)),
    RowPs = build_row_prefixes(Grid, C),
    ColPs = build_col_prefixes(Grid, R, C),
    {Ans, _} = solve(0, R - 1, 0, C - 1, 3, RowPs, ColPs, #{}),
    Ans.

%% Build row prefix sums: map RowIdx -> tuple of size C+1
build_row_prefixes(Grid, C) ->
    lists:foldl(
      fun({RowIdx, Row}, Acc) ->
          Prefix = list_to_tuple(build_prefix_list(Row)),
          maps:put(RowIdx, Prefix, Acc)
      end,
      #{},
      enumerate_rows(Grid, 0)
    ).

%% Build column prefix sums: map ColIdx -> tuple of size R+1
build_col_prefixes(Grid, R, C) ->
    lists:foldl(
      fun(ColIdx, Acc) ->
          Column = [lists:nth(RowIdx + 1, Row) || {RowIdx, Row} <- enumerate_rows(Grid, 0)],
          Prefix = list_to_tuple(build_prefix_list(Column)),
          maps:put(ColIdx, Prefix, Acc)
      end,
      #{},
      lists:seq(0, C - 1)
    ).

%% Enumerate rows with index
enumerate_rows([], _) -> [];
enumerate_rows([H|T], Idx) ->
    [{Idx, H} | enumerate_rows(T, Idx + 1)].

%% Build prefix list (length N+1) where element i is sum of first i-1 elements
build_prefix_list(List) ->
    build_prefix_list(List, 0, []).

build_prefix_list([], Sum, Acc) ->
    lists:reverse([Sum | Acc]);
build_prefix_list([V|Rest], Sum, Acc) ->
    NewSum = Sum + V,
    build_prefix_list(Rest, NewSum, [Sum | Acc]).

%% Count ones in submatrix using row prefixes
count_ones(R1, R2, C1, C2, RowPs) ->
    lists:foldl(
      fun(RowIdx, Acc) ->
          Prefix = maps:get(RowIdx, RowPs),
          Upper = element(C2 + 2, Prefix),
          Lower = element(C1 + 1, Prefix),
          Acc + (Upper - Lower)
      end,
      0,
      lists:seq(R1, R2)
    ).

%% Check if a row segment contains any 1
row_has_one(RowIdx, C1, C2, RowPs) ->
    Prefix = maps:get(RowIdx, RowPs),
    Upper = element(C2 + 2, Prefix),
    Lower = element(C1 + 1, Prefix),
    (Upper - Lower) > 0.

%% Check if a column segment contains any 1
col_has_one(ColIdx, R1, R2, ColPs) ->
    Prefix = maps:get(ColIdx, ColPs),
    Upper = element(R2 + 2, Prefix),
    Lower = element(R1 + 1, Prefix),
    (Upper - Lower) > 0.

%% Bounding box area of ones in submatrix
bounding_box_area(R1, R2, C1, C2, RowPs, ColPs) ->
    case count_ones(R1, R2, C1, C2, RowPs) of
        0 -> 0;
        _Cnt ->
            MinRow = find_min_row(R1, R2, C1, C2, RowPs),
            MaxRow = find_max_row(R1, R2, C1, C2, RowPs),
            MinCol = find_min_col(C1, C2, R1, R2, ColPs),
            MaxCol = find_max_col(C1, C2, R1, R2, ColPs),
            (MaxRow - MinRow + 1) * (MaxCol - MinCol + 1)
    end.

find_min_row(R, EndR, C1, C2, RowPs) ->
    case lists:dropwhile(fun(I) -> not row_has_one(I, C1, C2, RowPs) end,
                         lists:seq(R, EndR)) of
        [] -> R;
        [First|_] -> First
    end.

find_max_row(R, EndR, C1, C2, RowPs) ->
    Rev = lists:reverse(lists:seq(R, EndR)),
    case lists:dropwhile(fun(I) -> not row_has_one(I, C1, C2, RowPs) end,
                         Rev) of
        [] -> EndR;
        [First|_] -> First
    end.

find_min_col(C, EndC, R1, R2, ColPs) ->
    case lists:dropwhile(fun(J) -> not col_has_one(J, R1, R2, ColPs) end,
                         lists:seq(C, EndC)) of
        [] -> C;
        [First|_] -> First
    end.

find_max_col(C, EndC, R1, R2, ColPs) ->
    Rev = lists:reverse(lists:seq(C, EndC)),
    case lists:dropwhile(fun(J) -> not col_has_one(J, R1, R2, ColPs) end,
                         Rev) of
        [] -> EndC;
        [First|_] -> First
    end.

%% DP solver with memoization
solve(R1, R2, C1, C2, K, RowPs, ColPs, Memo) ->
    Key = {R1, R2, C1, C2, K},
    case maps:find(Key, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            Inf = 1000000,
            Count = count_ones(R1, R2, C1, C2, RowPs),
            Result =
                if Count == 0 ->
                        if K == 0 -> 0; true -> Inf end;
                   K == 1 ->
                        bounding_box_area(R1, R2, C1, C2, RowPs, ColPs);
                   true ->
                        find_best_split(R1, R2, C1, C2, K, RowPs, ColPs, Memo, Inf)
                end,
            NewMemo = maps:put(Key, Result, Memo),
            {Result, NewMemo}
    end.

find_best_split(R1, R2, C1, C2, K, RowPs, ColPs, Memo, Inf) ->
    % Horizontal splits
    {BestH, MemH} =
        lists:foldl(
          fun(Mid, {BestAcc, MemAcc}) ->
              lists:foldl(
                fun(I, {B, M}) ->
                    {TopRes, M1} = solve(R1, Mid, C1, C2, I, RowPs, ColPs, M),
                    {BotRes, M2} = solve(Mid + 1, R2, C1, C2, K - I, RowPs, ColPs, M1),
                    NewBest = if TopRes < Inf, BotRes < Inf -> min(B, TopRes + BotRes);
                               true -> B end,
                    {NewBest, M2}
                end,
                {BestAcc, MemAcc},
                lists:seq(1, K - 1)
              )
          end,
          {Inf, Memo},
          lists:seq(R1, R2 - 1)
        ),
    % Vertical splits
    {BestV, MemV} =
        lists:foldl(
          fun(Mid, {BestAcc, MemAcc}) ->
              lists:foldl(
                fun(I, {B, M}) ->
                    {LeftRes, M1} = solve(R1, R2, C1, Mid, I, RowPs, ColPs, M),
                    {RightRes, M2} = solve(R1, R2, Mid + 1, C2, K - I, RowPs, ColPs, M1),
                    NewBest = if LeftRes < Inf, RightRes < Inf -> min(B, LeftRes + RightRes);
                               true -> B end,
                    {NewBest, M2}
                end,
                {BestAcc, MemAcc},
                lists:seq(1, K - 1)
              )
          end,
          {BestH, MemH},
          lists:seq(C1, C2 - 1)
        ),
    BestV.
```

## Elixir

```elixir
defmodule Solution do
  @inf 1_000_000_000

  @spec minimum_sum(grid :: [[integer]]) :: integer
  def minimum_sum(grid) do
    m = length(grid)
    n = length(hd(grid))

    # row prefix sums: rows x (n+1)
    row_ps =
      Enum.map(grid, fn row ->
        {_, pref} =
          Enum.reduce(row, {0, []}, fn val, {acc, lst} ->
            new = acc + val
            {new, lst ++ [new]}
          end)

        [0] ++ pref
      end)

    # column prefix sums: cols x (m+1)
    col_ps =
      for j <- 0..(n - 1) do
        col_vals = Enum.map(grid, fn row -> Enum.at(row, j) end)

        {_, pref} =
          Enum.reduce(col_vals, {0, []}, fn val, {acc, lst} ->
            new = acc + val
            {new, lst ++ [new]}
          end)

        [0] ++ pref
      end

    # 2D prefix sum (m+1) x (n+1)
    ps =
      for i <- 0..m do
        for j <- 0..n do
          cond do
            i == 0 or j == 0 ->
              0

            true ->
              grid_val = Enum.at(Enum.at(grid, i - 1), j - 1)
              top = Enum.at(Enum.at(ps, i - 1), j)
              left = Enum.at(Enum.at(ps, i), j - 1)
              diag = Enum.at(Enum.at(ps, i - 1), j - 1)
              grid_val + top + left - diag
          end
        end
      end

    :ets.new(:dp_cache, [:named_table, :public, read_concurrency: true])

    result = dp(3, 0, m - 1, 0, n - 1, ps, row_ps, col_ps)

    :ets.delete(:dp_cache)
    result
  end

  defp rect_sum(ps, r1, r2, c1, c2) do
    a = Enum.at(Enum.at(ps, r2 + 1), c2 + 1)
    b = Enum.at(Enum.at(ps, r1), c2 + 1)
    c = Enum.at(Enum.at(ps, r2 + 1), c1)
    d = Enum.at(Enum.at(ps, r1), c1)
    a - b - c + d
  end

  defp bounding_box_area(r1, r2, c1, c2, row_ps, col_ps) do
    # find minRow
    {min_row, _} =
      Enum.reduce_while(r1..r2, {nil, false}, fn i, acc ->
        cnt = Enum.at(row_ps, i) |> then(&Enum.at(&1, c2 + 1)) - Enum.at(row_ps, i) |> then(&Enum.at(&1, c1))
        if cnt > 0, do: {:halt, {i, true}}, else: {:cont, acc}
      end)

    # find maxRow
    {max_row, _} =
      Enum.reduce_while(Enum.reverse(r1..r2), {nil, false}, fn i, acc ->
        cnt = Enum.at(row_ps, i) |> then(&Enum.at(&1, c2 + 1)) - Enum.at(row_ps, i) |> then(&Enum.at(&1, c1))
        if cnt > 0, do: {:halt, {i, true}}, else: {:cont, acc}
      end)

    # find minCol
    {min_col, _} =
      Enum.reduce_while(c1..c2, {nil, false}, fn j, acc ->
        cnt = Enum.at(col_ps, j) |> then(&Enum.at(&1, max_row + 1)) - Enum.at(col_ps, j) |> then(&Enum.at(&1, min_row))
        if cnt > 0, do: {:halt, {j, true}}, else: {:cont, acc}
      end)

    # find maxCol
    {max_col, _} =
      Enum.reduce_while(Enum.reverse(c1..c2), {nil, false}, fn j, acc ->
        cnt = Enum.at(col_ps, j) |> then(&Enum.at(&1, max_row + 1)) - Enum.at(col_ps, j) |> then(&Enum.at(&1, min_row))
        if cnt > 0, do: {:halt, {j, true}}, else: {:cont, acc}
      end)

    (max_row - min_row + 1) * (max_col - min_col + 1)
  end

  defp dp(k, r1, r2, c1, c2, ps, row_ps, col_ps) do
    key = {k, r1, r2, c1, c2}
    case :ets.lookup(:dp_cache, key) do
      [{^key, val}] ->
        val

      [] ->
        cnt = rect_sum(ps, r1, r2, c1, c2)

        val =
          cond do
            cnt == 0 and k == 0 ->
              0

            cnt == 0 ->
              @inf

            k == 1 ->
              bounding_box_area(r1, r2, c1, c2, row_ps, col_ps)

            true ->
              candidates = []

              # vertical splits
              vert_candidates =
                for m <- c1..(c2 - 1), i <- 0..k do
                  left = dp(i, r1, r2, c1, m, ps, row_ps, col_ps)
                  right = dp(k - i, r1, r2, m + 1, c2, ps, row_ps, col_ps)
                  left + right
                end

              # horizontal splits
              horiz_candidates =
                for m <- r1..(r2 - 1), i <- 0..k do
                  top = dp(i, r1, m, c1, c2, ps, row_ps, col_ps)
                  bottom = dp(k - i, m + 1, r2, c1, c2, ps, row_ps, col_ps)
                  top + bottom
                end

              Enum.min(vert_candidates ++ horiz_candidates ++ [@inf])
          end

        :ets.insert(:dp_cache, {key, val})
        val
    end
  end
end
```

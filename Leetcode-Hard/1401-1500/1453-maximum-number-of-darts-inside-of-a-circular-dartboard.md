# 1453. Maximum Number of Darts Inside of a Circular Dartboard

## Cpp

```cpp
class Solution {
public:
    int numPoints(vector<vector<int>>& darts, int r) {
        const double R = (double)r;
        const double R2 = R * R;
        const double EPS = 1e-7;
        int n = darts.size();
        if (n == 0) return 0;
        int best = 1;
        auto countInside = [&](double cx, double cy) {
            int cnt = 0;
            for (int k = 0; k < n; ++k) {
                double dx = darts[k][0] - cx;
                double dy = darts[k][1] - cy;
                if (dx * dx + dy * dy <= R2 + EPS) ++cnt;
            }
            return cnt;
        };
        // centers at each point
        for (int i = 0; i < n; ++i) {
            best = max(best, countInside(darts[i][0], darts[i][1]));
        }
        // centers defined by pairs
        for (int i = 0; i < n; ++i) {
            double x1 = darts[i][0];
            double y1 = darts[i][1];
            for (int j = i + 1; j < n; ++j) {
                double x2 = darts[j][0];
                double y2 = darts[j][1];
                double dx = x2 - x1;
                double dy = y2 - y1;
                double d2 = dx * dx + dy * dy;
                double d = sqrt(d2);
                if (d > 2.0 * R + EPS) continue; // cannot fit both
                // midpoint
                double mx = (x1 + x2) / 2.0;
                double my = (y1 + y2) / 2.0;
                // distance from midpoint to centers
                double h = sqrt(max(0.0, R2 - (d / 2.0) * (d / 2.0)));
                // unit perpendicular vector
                double ux = -dy / d;
                double uy = dx / d;
                // two possible centers
                double cx1 = mx + ux * h;
                double cy1 = my + uy * h;
                best = max(best, countInside(cx1, cy1));
                double cx2 = mx - ux * h;
                double cy2 = my - uy * h;
                best = max(best, countInside(cx2, cy2));
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int numPoints(int[][] darts, int r) {
        int n = darts.length;
        double R = r;
        double R2 = R * R;
        int best = 1;
        double eps = 1e-7;

        // Centers at each dart point
        for (int i = 0; i < n; i++) {
            double cx = darts[i][0];
            double cy = darts[i][1];
            int cnt = 0;
            for (int k = 0; k < n; k++) {
                double dx = darts[k][0] - cx;
                double dy = darts[k][1] - cy;
                if (dx * dx + dy * dy <= R2 + eps) cnt++;
            }
            best = Math.max(best, cnt);
        }

        // Centers defined by pairs of points
        for (int i = 0; i < n; i++) {
            double x1 = darts[i][0];
            double y1 = darts[i][1];
            for (int j = i + 1; j < n; j++) {
                double x2 = darts[j][0];
                double y2 = darts[j][1];

                double dx = x2 - x1;
                double dy = y2 - y1;
                double d2 = dx * dx + dy * dy;
                double d = Math.sqrt(d2);
                if (d > 2 * R + eps) continue; // cannot be covered together

                // midpoint
                double mx = (x1 + x2) / 2.0;
                double my = (y1 + y2) / 2.0;

                // distance from midpoint to circle centers
                double hSq = R2 - (d / 2.0) * (d / 2.0);
                if (hSq < 0) hSq = 0; // guard against negative due to precision
                double h = Math.sqrt(hSq);

                // unit perpendicular vector
                double ux = -dy / d;
                double uy = dx / d;

                // first possible center
                double cx1 = mx + ux * h;
                double cy1 = my + uy * h;
                int cnt1 = 0;
                for (int k = 0; k < n; k++) {
                    double ddx = darts[k][0] - cx1;
                    double ddy = darts[k][1] - cy1;
                    if (ddx * ddx + ddy * ddy <= R2 + eps) cnt1++;
                }
                best = Math.max(best, cnt1);

                // second possible center
                double cx2 = mx - ux * h;
                double cy2 = my - uy * h;
                int cnt2 = 0;
                for (int k = 0; k < n; k++) {
                    double ddx = darts[k][0] - cx2;
                    double ddy = darts[k][1] - cy2;
                    if (ddx * ddx + ddy * ddy <= R2 + eps) cnt2++;
                }
                best = Math.max(best, cnt2);
            }
        }

        return best;
    }
}
```

## Python

```python
import math

class Solution(object):
    def numPoints(self, darts, r):
        """
        :type darts: List[List[int]]
        :type r: int
        :rtype: int
        """
        n = len(darts)
        if n == 0:
            return 0
        R = float(r)
        R2 = R * R
        eps = 1e-7
        ans = 1

        # circles centered at each dart
        for i in range(n):
            xi, yi = darts[i]
            cnt = 0
            for x, y in darts:
                if (x - xi) ** 2 + (y - yi) ** 2 <= R2 + eps:
                    cnt += 1
            ans = max(ans, cnt)

        # circles passing through each pair of darts
        for i in range(n):
            xi, yi = darts[i]
            for j in range(i + 1, n):
                xj, yj = darts[j]
                dx = xj - xi
                dy = yj - yi
                d2 = dx * dx + dy * dy
                d = math.sqrt(d2)
                if d > 2 * R + eps:
                    continue
                # midpoint
                mx = (xi + xj) / 2.0
                my = (yi + yj) / 2.0
                # distance from midpoint to circle centers
                h = math.sqrt(max(R2 - (d / 2.0) ** 2, 0.0))
                # unit perpendicular vector
                if d == 0:
                    continue
                ux = -dy / d
                uy = dx / d
                for sign in (1, -1):
                    cx = mx + sign * ux * h
                    cy = my + sign * uy * h
                    cnt = 0
                    for x, y in darts:
                        if (x - cx) ** 2 + (y - cy) ** 2 <= R2 + eps:
                            cnt += 1
                    ans = max(ans, cnt)

        return ans
```

## Python3

```python
import math
from typing import List

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        if n == 0:
            return 0
        points = [(float(x), float(y)) for x, y in darts]
        ans = 1
        rr = r * r
        eps = 1e-7

        def count_inside(cx: float, cy: float) -> int:
            cnt = 0
            for px, py in points:
                if (px - cx) ** 2 + (py - cy) ** 2 <= rr + eps:
                    cnt += 1
            return cnt

        # consider circles defined by each pair of points
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                d_sq = dx * dx + dy * dy
                d = math.sqrt(d_sq)
                if d > 2 * r + eps:
                    continue  # cannot be covered together
                # midpoint
                mx = (x1 + x2) / 2.0
                my = (y1 + y2) / 2.0
                # distance from midpoint to circle centers
                h = math.sqrt(max(rr - (d / 2.0) ** 2, 0.0))
                # unit perpendicular vector
                ux = -dy / d
                uy = dx / d
                cx1 = mx + ux * h
                cy1 = my + uy * h
                cx2 = mx - ux * h
                cy2 = my - uy * h
                ans = max(ans, count_inside(cx1, cy1), count_inside(cx2, cy2))

        return ans
```

## C

```c
#include <math.h>

int numPoints(int** darts, int dartsSize, int* dartsColSize, int r) {
    if (dartsSize == 0) return 0;
    double R = (double)r;
    const double eps = 1e-7;
    int maxCount = 1;

    double xs[100];
    double ys[100];
    for (int i = 0; i < dartsSize; ++i) {
        xs[i] = (double)darts[i][0];
        ys[i] = (double)darts[i][1];
    }

    // Centers at each point
    for (int i = 0; i < dartsSize; ++i) {
        int cnt = 0;
        for (int k = 0; k < dartsSize; ++k) {
            double dx = xs[k] - xs[i];
            double dy = ys[k] - ys[i];
            if (dx * dx + dy * dy <= R * R + eps) ++cnt;
        }
        if (cnt > maxCount) maxCount = cnt;
    }

    // Centers defined by pairs of points
    for (int i = 0; i < dartsSize; ++i) {
        for (int j = i + 1; j < dartsSize; ++j) {
            double dx = xs[j] - xs[i];
            double dy = ys[j] - ys[i];
            double d2 = dx * dx + dy * dy;
            double d = sqrt(d2);
            if (d > 2.0 * R + eps) continue;

            double mx = (xs[i] + xs[j]) / 2.0;
            double my = (ys[i] + ys[j]) / 2.0;
            double h = sqrt(R * R - (d / 2.0) * (d / 2.0));

            double ux = -dy / d; // unit perpendicular vector
            double uy = dx / d;

            // First possible center
            double cx1 = mx + ux * h;
            double cy1 = my + uy * h;
            int cnt1 = 0;
            for (int k = 0; k < dartsSize; ++k) {
                double ddx = xs[k] - cx1;
                double ddy = ys[k] - cy1;
                if (ddx * ddx + ddy * ddy <= R * R + eps) ++cnt1;
            }
            if (cnt1 > maxCount) maxCount = cnt1;

            // Second possible center
            double cx2 = mx - ux * h;
            double cy2 = my - uy * h;
            int cnt2 = 0;
            for (int k = 0; k < dartsSize; ++k) {
                double ddx = xs[k] - cx2;
                double ddy = ys[k] - cy2;
                if (ddx * ddx + ddy * ddy <= R * R + eps) ++cnt2;
            }
            if (cnt2 > maxCount) maxCount = cnt2;
        }
    }

    return maxCount;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int NumPoints(int[][] darts, int r) {
        int n = darts.Length;
        if (n == 0) return 0;
        double R = r;
        double eps = 1e-7;
        int best = 1;
        
        // Helper to count points within radius from a given center
        int Count(double cx, double cy) {
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                double dx = darts[i][0] - cx;
                double dy = darts[i][1] - cy;
                if (dx * dx + dy * dy <= R * R + eps) cnt++;
            }
            return cnt;
        }
        
        // Centers at each point
        for (int i = 0; i < n; i++) {
            best = Math.Max(best, Count(darts[i][0], darts[i][1]));
        }
        
        // Centers defined by pairs of points
        for (int i = 0; i < n; i++) {
            double x1 = darts[i][0];
            double y1 = darts[i][1];
            for (int j = i + 1; j < n; j++) {
                double x2 = darts[j][0];
                double y2 = darts[j][1];
                
                double dx = x2 - x1;
                double dy = y2 - y1;
                double d2 = dx * dx + dy * dy;
                double d = Math.Sqrt(d2);
                
                if (d > 2.0 * R + eps) continue; // cannot be covered together
                
                // midpoint
                double mx = (x1 + x2) / 2.0;
                double my = (y1 + y2) / 2.0;
                
                // distance from midpoint to circle centers
                double h = Math.Sqrt(R * R - (d / 2.0) * (d / 2.0));
                
                // unit perpendicular vector
                double ux = -dy / d;
                double uy = dx / d;
                
                // first center
                double cx1 = mx + ux * h;
                double cy1 = my + uy * h;
                best = Math.Max(best, Count(cx1, cy1));
                
                // second center (if distinct)
                if (h > eps) {
                    double cx2 = mx - ux * h;
                    double cy2 = my - uy * h;
                    best = Math.Max(best, Count(cx2, cy2));
                }
            }
        }
        
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} darts
 * @param {number} r
 * @return {number}
 */
var numPoints = function(darts, r) {
    const n = darts.length;
    if (n === 0) return 0;
    const R2 = r * r;
    const EPS = 1e-7;
    let best = 1;

    // helper to count points within radius of (cx, cy)
    const countInside = (cx, cy) => {
        let cnt = 0;
        for (let k = 0; k < n; ++k) {
            const dx = darts[k][0] - cx;
            const dy = darts[k][1] - cy;
            if (dx * dx + dy * dy <= R2 + EPS) cnt++;
        }
        return cnt;
    };

    // circles centered at each point (covers case when only one boundary point)
    for (let i = 0; i < n; ++i) {
        best = Math.max(best, countInside(darts[i][0], darts[i][1]));
    }

    for (let i = 0; i < n; ++i) {
        const [x1, y1] = darts[i];
        for (let j = i + 1; j < n; ++j) {
            const [x2, y2] = darts[j];
            const dx = x2 - x1;
            const dy = y2 - y1;
            const d2 = dx * dx + dy * dy;
            const d = Math.sqrt(d2);
            if (d > 2 * r + EPS) continue; // cannot be on same circle

            // midpoint
            const mx = (x1 + x2) / 2;
            const my = (y1 + y2) / 2;

            // distance from midpoint to centers
            const h = Math.sqrt(Math.max(0, r * r - (d / 2) * (d / 2)));

            // unit perpendicular vector
            const ux = -dy / d;
            const uy = dx / d;

            // two possible centers
            const c1x = mx + ux * h;
            const c1y = my + uy * h;
            const c2x = mx - ux * h;
            const c2y = my - uy * h;

            best = Math.max(best, countInside(c1x, c1y));
            best = Math.max(best, countInside(c2x, c2y));
        }
    }

    return best;
};
```

## Typescript

```typescript
function numPoints(darts: number[][], r: number): number {
    const n = darts.length;
    if (n === 0) return 0;
    const rr = r * r;
    let ans = 1;
    const eps = 1e-7;

    function countInside(cx: number, cy: number): number {
        let cnt = 0;
        for (let k = 0; k < n; ++k) {
            const dx = darts[k][0] - cx;
            const dy = darts[k][1] - cy;
            if (dx * dx + dy * dy <= rr + eps) cnt++;
        }
        return cnt;
    }

    // Centers at each dart
    for (let i = 0; i < n; ++i) {
        ans = Math.max(ans, countInside(darts[i][0], darts[i][1]));
    }

    // Centers defined by pairs of darts
    for (let i = 0; i < n; ++i) {
        const [x1, y1] = darts[i];
        for (let j = i + 1; j < n; ++j) {
            const [x2, y2] = darts[j];
            const dx = x2 - x1;
            const dy = y2 - y1;
            const d2 = dx * dx + dy * dy;
            const d = Math.sqrt(d2);
            if (d > 2 * r + eps) continue; // cannot be covered together

            const mx = (x1 + x2) / 2;
            const my = (y1 + y2) / 2;
            const half = d / 2;
            const h = Math.sqrt(Math.max(0, rr - half * half));

            const ux = -dy / d; // unit perpendicular vector
            const uy = dx / d;

            const cx1 = mx + ux * h;
            const cy1 = my + uy * h;
            const cx2 = mx - ux * h;
            const cy2 = my - uy * h;

            ans = Math.max(ans, countInside(cx1, cy1));
            ans = Math.max(ans, countInside(cx2, cy2));
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $darts
     * @param Integer $r
     * @return Integer
     */
    function numPoints($darts, $r) {
        $n = count($darts);
        if ($n == 0) return 0;
        $max = 1;
        $eps = 1e-7;
        $rr = $r * $r;

        // circles centered at each dart
        for ($i = 0; $i < $n; $i++) {
            $cx = $darts[$i][0];
            $cy = $darts[$i][1];
            $cnt = 0;
            for ($k = 0; $k < $n; $k++) {
                $dx = $darts[$k][0] - $cx;
                $dy = $darts[$k][1] - $cy;
                if ($dx * $dx + $dy * $dy <= $rr + $eps) {
                    $cnt++;
                }
            }
            if ($cnt > $max) $max = $cnt;
        }

        // circles defined by two points on the boundary
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $x1 = $darts[$i][0];
                $y1 = $darts[$i][1];
                $x2 = $darts[$j][0];
                $y2 = $darts[$j][1];

                $dx = $x2 - $x1;
                $dy = $y2 - $y1;
                $dist2 = $dx * $dx + $dy * $dy;
                $dist = sqrt($dist2);

                if ($dist > 2 * $r + $eps) continue; // cannot fit both points

                // midpoint
                $mx = ($x1 + $x2) / 2.0;
                $my = ($y1 + $y2) / 2.0;

                // distance from midpoint to circle centers
                $h = sqrt($r * $r - ($dist / 2.0) * ($dist / 2.0));

                if ($dist == 0) continue; // points are distinct per constraints

                // unit perpendicular vector
                $ux = -$dy / $dist;
                $uy = $dx / $dist;

                // two possible centers
                $c1x = $mx + $ux * $h;
                $c1y = $my + $uy * $h;
                $c2x = $mx - $ux * $h;
                $c2y = $my - $uy * $h;

                $cnt1 = 0;
                $cnt2 = 0;
                for ($k = 0; $k < $n; $k++) {
                    $dx1 = $darts[$k][0] - $c1x;
                    $dy1 = $darts[$k][1] - $c1y;
                    if ($dx1 * $dx1 + $dy1 * $dy1 <= $rr + $eps) $cnt1++;

                    $dx2 = $darts[$k][0] - $c2x;
                    $dy2 = $darts[$k][1] - $c2y;
                    if ($dx2 * $dx2 + $dy2 * $dy2 <= $rr + $eps) $cnt2++;
                }

                if ($cnt1 > $max) $max = $cnt1;
                if ($cnt2 > $max) $max = $cnt2;
            }
        }

        return $max;
    }
}
```

## Swift

```swift
import Foundation

struct Point {
    let x: Double
    let y: Double
}

class Solution {
    func numPoints(_ darts: [[Int]], _ r: Int) -> Int {
        let n = darts.count
        var points = [Point]()
        for d in darts {
            points.append(Point(x: Double(d[0]), y: Double(d[1])))
        }
        let radius = Double(r)
        let radiusSq = radius * radius
        let eps = 1e-7
        var best = 1
        
        func countInside(_ cx: Double, _ cy: Double) -> Int {
            var cnt = 0
            for p in points {
                let dx = p.x - cx
                let dy = p.y - cy
                if dx * dx + dy * dy <= radiusSq + eps {
                    cnt += 1
                }
            }
            return cnt
        }
        
        // Centers at each point
        for i in 0..<n {
            best = max(best, countInside(points[i].x, points[i].y))
        }
        
        if n == 1 { return best }
        
        // Centers defined by pairs of points
        for i in 0..<n {
            for j in i+1..<n {
                let p1 = points[i]
                let p2 = points[j]
                let dx = p2.x - p1.x
                let dy = p2.y - p1.y
                let dSq = dx * dx + dy * dy
                let d = sqrt(dSq)
                if d > 2.0 * radius + eps { continue }
                
                // Midpoint
                let mx = (p1.x + p2.x) / 2.0
                let my = (p1.y + p2.y) / 2.0
                
                // Distance from midpoint to circle centers
                var hSq = radiusSq - (d / 2.0) * (d / 2.0)
                if hSq < 0 { hSq = 0 }
                let h = sqrt(hSq)
                
                // Unit perpendicular vector
                let ux = -dy / d
                let uy = dx / d
                
                // First center
                let c1x = mx + ux * h
                let c1y = my + uy * h
                best = max(best, countInside(c1x, c1y))
                
                // Second center
                let c2x = mx - ux * h
                let c2y = my - uy * h
                best = max(best, countInside(c2x, c2y))
            }
        }
        
        return best
    }
}
```

## Kotlin

```kotlin
import kotlin.math.*

class Solution {
    fun numPoints(darts: Array<IntArray>, r: Int): Int {
        val n = darts.size
        if (n == 0) return 0
        val rr = r.toDouble()
        val rr2 = rr * rr
        var best = 1
        fun count(cx: Double, cy: Double): Int {
            var cnt = 0
            for (p in darts) {
                val dx = p[0] - cx
                val dy = p[1] - cy
                if (dx * dx + dy * dy <= rr2 + 1e-7) cnt++
            }
            return cnt
        }
        // centers at each point
        for (p in darts) {
            best = maxOf(best, count(p[0].toDouble(), p[1].toDouble()))
        }
        // centers defined by pairs of points
        for (i in 0 until n) {
            val x1 = darts[i][0].toDouble()
            val y1 = darts[i][1].toDouble()
            for (j in i + 1 until n) {
                val x2 = darts[j][0].toDouble()
                val y2 = darts[j][1].toDouble()
                val dx = x2 - x1
                val dy = y2 - y1
                val d2 = dx * dx + dy * dy
                val d = sqrt(d2)
                if (d > 2.0 * rr + 1e-7) continue
                // midpoint
                val mx = (x1 + x2) / 2.0
                val my = (y1 + y2) / 2.0
                // distance from midpoint to circle centers
                val h = sqrt(rr2 - (d / 2.0) * (d / 2.0))
                // unit perpendicular vector
                val ux = -dy / d
                val uy = dx / d
                // first center
                var cx = mx + ux * h
                var cy = my + uy * h
                best = maxOf(best, count(cx, cy))
                // second center
                cx = mx - ux * h
                cy = my - uy * h
                best = maxOf(best, count(cx, cy))
            }
        }
        return best
    }
}
```

## Dart

```dart
import 'dart:math' as Math;

class Solution {
  int numPoints(List<List<int>> darts, int r) {
    int n = darts.length;
    if (n == 0) return 0;
    double radius = r.toDouble();
    double radiusSq = radius * radius;
    const double eps = 1e-7;
    int best = 1;

    bool inside(double cx, double cy, List<int> p) {
      double dx = p[0] - cx;
      double dy = p[1] - cy;
      return dx * dx + dy * dy <= radiusSq + eps;
    }

    // Centers at each dart
    for (int i = 0; i < n; ++i) {
      double cx = darts[i][0].toDouble();
      double cy = darts[i][1].toDouble();
      int cnt = 0;
      for (var p in darts) {
        if (inside(cx, cy, p)) cnt++;
      }
      if (cnt > best) best = cnt;
    }

    // Centers defined by pairs of darts
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        double x1 = darts[i][0].toDouble();
        double y1 = darts[i][1].toDouble();
        double x2 = darts[j][0].toDouble();
        double y2 = darts[j][1].toDouble();

        double dx = x2 - x1;
        double dy = y2 - y1;
        double d = Math.sqrt(dx * dx + dy * dy);
        if (d > 2 * radius + eps) continue;

        // midpoint
        double mx = (x1 + x2) / 2.0;
        double my = (y1 + y2) / 2.0;

        double h = Math.sqrt(radius * radius - (d / 2) * (d / 2));
        // unit perpendicular vector
        double ux = -dy / d;
        double uy = dx / d;

        for (int sign = -1; sign <= 1; sign += 2) {
          double cx = mx + ux * h * sign;
          double cy = my + uy * h * sign;
          int cnt = 0;
          for (var p in darts) {
            if (inside(cx, cy, p)) cnt++;
          }
          if (cnt > best) best = cnt;
        }
      }
    }

    return best;
  }
}
```

## Golang

```go
package main

import "math"

func numPoints(darts [][]int, r int) int {
	n := len(darts)
	if n == 0 {
		return 0
	}
	rr := float64(r)
	rr2 := rr * rr
	maxCount := 1

	xs := make([]float64, n)
	ys := make([]float64, n)
	for i, p := range darts {
		xs[i] = float64(p[0])
		ys[i] = float64(p[1])
	}

	eps := 1e-7

	countAt := func(cx, cy float64) int {
		cnt := 0
		for i := 0; i < n; i++ {
			dx := xs[i] - cx
			dy := ys[i] - cy
			if dx*dx+dy*dy <= rr2+eps {
				cnt++
			}
		}
		return cnt
	}

	for i := 0; i < n; i++ {
		c := countAt(xs[i], ys[i])
		if c > maxCount {
			maxCount = c
		}
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			dx := xs[j] - xs[i]
			dy := ys[j] - ys[i]
			d2 := dx*dx + dy*dy
			d := math.Sqrt(d2)
			if d > 2*rr+eps {
				continue
			}
			mx := (xs[i] + xs[j]) / 2.0
			my := (ys[i] + ys[j]) / 2.0

			h := math.Sqrt(rr2 - (d/2)*(d/2))

			ux := -dy / d
			uy := dx / d

			cx1 := mx + ux*h
			cy1 := my + uy*h
			if cnt := countAt(cx1, cy1); cnt > maxCount {
				maxCount = cnt
			}

			cx2 := mx - ux*h
			cy2 := my - uy*h
			if cnt := countAt(cx2, cy2); cnt > maxCount {
				maxCount = cnt
			}
		}
	}

	return maxCount
}
```

## Ruby

```ruby
def num_points(darts, r)
  n = darts.length
  return 0 if n == 0
  radius = r.to_f
  rad_sq = radius * radius
  eps = 1e-7
  max_cnt = 1

  # Centers at each dart (optional safety)
  darts.each do |cx, cy|
    cnt = 0
    darts.each do |x, y|
      dx = x - cx
      dy = y - cy
      cnt += 1 if dx * dx + dy * dy <= rad_sq + eps
    end
    max_cnt = [max_cnt, cnt].max
  end

  (0...n).each do |i|
    xi, yi = darts[i]
    ((i + 1)...n).each do |j|
      xj, yj = darts[j]
      dx = xj - xi
      dy = yj - yi
      d_sq = dx * dx + dy * dy
      next if d_sq > (2 * radius) * (2 * radius) + eps

      d = Math.sqrt(d_sq)
      mx = (xi + xj) / 2.0
      my = (yi + yj) / 2.0
      h = Math.sqrt(rad_sq - (d / 2.0) * (d / 2.0))

      ux = -dy / d
      uy = dx / d

      [1, -1].each do |sign|
        cx = mx + sign * ux * h
        cy = my + sign * uy * h
        cnt = 0
        darts.each do |xk, yk|
          ddx = xk - cx
          ddy = yk - cy
          cnt += 1 if ddx * ddx + ddy * ddy <= rad_sq + eps
        end
        max_cnt = [max_cnt, cnt].max
      end
    end
  end

  max_cnt
end
```

## Scala

```scala
object Solution {
    def numPoints(darts: Array[Array[Int]], r: Int): Int = {
        val n = darts.length
        if (n == 0) return 0
        val points = darts.map { case Array(x, y) => (x.toDouble, y.toDouble) }
        val rr = r.toDouble * r
        var best = 1
        val eps = 1e-7

        def count(cx: Double, cy: Double): Int = {
            var cnt = 0
            var i = 0
            while (i < n) {
                val dx = points(i)._1 - cx
                val dy = points(i)._2 - cy
                if (dx * dx + dy * dy <= rr + eps) cnt += 1
                i += 1
            }
            cnt
        }

        // centers at each point
        var i = 0
        while (i < n) {
            val c = count(points(i)._1, points(i)._2)
            if (c > best) best = c
            i += 1
        }

        // centers defined by pairs of points
        i = 0
        while (i < n) {
            var j = i + 1
            while (j < n) {
                val x1 = points(i)._1
                val y1 = points(i)._2
                val x2 = points(j)._1
                val y2 = points(j)._2
                val dx = x2 - x1
                val dy = y2 - y1
                val d2 = dx * dx + dy * dy
                val d = Math.sqrt(d2)
                if (d <= 2.0 * r + eps) {
                    val mx = (x1 + x2) / 2.0
                    val my = (y1 + y2) / 2.0
                    val h = Math.sqrt(rr - (d / 2.0) * (d / 2.0))
                    val ux = -dy / d
                    val uy = dx / d

                    val cx1 = mx + ux * h
                    val cy1 = my + uy * h
                    val cnt1 = count(cx1, cy1)
                    if (cnt1 > best) best = cnt1

                    val cx2 = mx - ux * h
                    val cy2 = my - uy * h
                    val cnt2 = count(cx2, cy2)
                    if (cnt2 > best) best = cnt2
                }
                j += 1
            }
            i += 1
        }

        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_points(darts: Vec<Vec<i32>>, r: i32) -> i32 {
        let n = darts.len();
        if n == 0 {
            return 0;
        }
        let points: Vec<(f64, f64)> = darts.iter()
            .map(|v| (v[0] as f64, v[1] as f64))
            .collect();

        let r_f = r as f64;
        let r_sq = r_f * r_f;
        let eps = 1e-7_f64;
        let mut ans = 1i32;

        // Center at each point
        for i in 0..n {
            let (cx, cy) = points[i];
            let mut cnt = 0;
            for &(x, y) in &points {
                let dx = x - cx;
                let dy = y - cy;
                if dx * dx + dy * dy <= r_sq + eps {
                    cnt += 1;
                }
            }
            if cnt > ans {
                ans = cnt;
            }
        }

        // Centers defined by pairs of points
        for i in 0..n {
            for j in (i + 1)..n {
                let (x1, y1) = points[i];
                let (x2, y2) = points[j];
                let dx = x2 - x1;
                let dy = y2 - y1;
                let d_sq = dx * dx + dy * dy;
                let d = d_sq.sqrt();

                if d > 2.0 * r_f + eps {
                    continue;
                }

                // Midpoint
                let mx = (x1 + x2) / 2.0;
                let my = (y1 + y2) / 2.0;

                // Distance from midpoint to circle centers
                let half = d / 2.0;
                let h_sq = r_sq - half * half;
                if h_sq < -eps {
                    continue;
                }
                let h = if h_sq <= 0.0 { 0.0 } else { h_sq.sqrt() };

                // Unit perpendicular vector
                let ux = -dy / d;
                let uy = dx / d;

                for &sign in &[1.0_f64, -1.0_f64] {
                    let cx = mx + sign * ux * h;
                    let cy = my + sign * uy * h;
                    let mut cnt = 0;
                    for &(x, y) in &points {
                        let dxp = x - cx;
                        let dyp = y - cy;
                        if dxp * dxp + dyp * dyp <= r_sq + eps {
                            cnt += 1;
                        }
                    }
                    if cnt > ans {
                        ans = cnt;
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (num-points darts r)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((n (length darts))
         (eps 1e-7)
         (r-d (+ r eps))
         (r2 (* r-d r-d))
         (max-count 0))

    (define (dist-sq p q)
      (let ((dx (- (first p) (first q)))
            (dy (- (second p) (second q))))
        (+ (* dx dx) (* dy dy))))

    (define (count-inside cx cy)
      (for/sum ([pt darts]
                #:when (<= (dist-sq pt (list cx cy)) r2))
        1))

    ;; centers at each single point
    (for ([pt darts])
      (set! max-count (max max-count (count-inside (first pt) (second pt)))))

    ;; centers defined by pairs of points
    (for* ([i (in-range n)]
           [j (in-range (+ i 1) n)])
      (let* ((p1 (list-ref darts i))
             (p2 (list-ref darts j))
             (dx (- (first p2) (first p1)))
             (dy (- (second p2) (second p1)))
             (d2 (+ (* dx dx) (* dy dy))))
        (when (<= d2 (* 4 r2))               ; distance <= 2r
          (let* ((d (sqrt d2))
                 (mid-x (/ (+ (first p1) (first p2)) 2.0))
                 (mid-y (/ (+ (second p1) (second p2)) 2.0))
                 (h-sq (- (* r-d r-d) (* (/ d 2.0) (/ d 2.0))))
                 (h (sqrt (max 0.0 h-sq)))
                 (ux (/ dx d))
                 (uy (/ dy d))
                 (px (* -uy h))               ; perpendicular vector scaled by h
                 (py (* ux h))
                 (c1-x (+ mid-x px))
                 (c1-y (+ mid-y py))
                 (c2-x (- mid-x px))
                 (c2-y (- mid-y py)))
            (set! max-count (max max-count (count-inside c1-x c1-y)))
            (set! max-count (max max-count (count-inside c2-x c2-y))))))))

    max-count))
```

## Erlang

```erlang
-module(solution).
-export([num_points/2]).

-spec num_points(Darts :: [[integer()]], R :: integer()) -> integer().
num_points(Darts, R) ->
    RF = float(R),
    Points = [{float(X), float(Y)} || [X, Y] <- Darts],
    Max0 = max_single(Points, RF),
    pair_centers(Points, RF, Max0).

max_single(Points, R) ->
    lists:max([count_inside(P, Points, R) || P <- Points]).

pair_centers(Points, R, Max) ->
    N = length(Points),
    pair_loop(1, N, Points, R, Max).

pair_loop(I, N, _Points, _R, Max) when I > N -> Max;
pair_loop(I, N, Points, R, Max) ->
    Pi = lists:nth(I, Points),
    NewMax = pair_with_i(I + 1, N, Pi, Points, R, Max),
    pair_loop(I + 1, N, Points, R, NewMax).

pair_with_i(J, N, _Pi, _Points, _R, Max) when J > N -> Max;
pair_with_i(J, N, {X1, Y1}=Pi, Points, R, Max) ->
    {X2, Y2} = lists:nth(J, Points),
    Dx = X2 - X1,
    Dy = Y2 - Y1,
    D2 = Dx*Dx + Dy*Dy,
    TwoR = 2.0 * R,
    Eps = 1.0e-7,
    if
        D2 > (TwoR+Eps)*(TwoR+Eps) ->
            pair_with_i(J + 1, N, Pi, Points, R, Max);
        true ->
            D = math:sqrt(D2),
            Mx = (X1 + X2) / 2.0,
            My = (Y1 + Y2) / 2.0,
            H = math:sqrt(R*R - (D/2)*(D/2)),
            ux = -Dy / D,
            uy = Dx / D,
            C1x = Mx + ux * H,
            C1y = My + uy * H,
            C2x = Mx - ux * H,
            C2y = My - uy * H,
            Count1 = count_inside({C1x, C1y}, Points, R),
            Count2 = count_inside({C2x, C2y}, Points, R),
            NewMax = erlang:max(Max, erlang:max(Count1, Count2)),
            pair_with_i(J + 1, N, Pi, Points, R, NewMax)
    end.

count_inside({Cx, Cy}, Points, R) ->
    Eps = 1.0e-7,
    R2 = (R + Eps)*(R + Eps),
    length([1 || {X, Y} <- Points,
                 ((X - Cx)*(X - Cx) + (Y - Cy)*(Y - Cy)) =< R2]).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_points(darts :: [[integer]], r :: integer) :: integer
  def num_points(darts, r) do
    points = Enum.map(darts, fn [x, y] -> {x * 1.0, y * 1.0} end)
    n = length(points)

    if n == 0 do
      0
    else
      r_f = r * 1.0
      r2 = r_f * r_f
      eps = 1.0e-7

      Enum.reduce(0..(n - 1), 1, fn i, acc_max ->
        {xi, yi} = Enum.at(points, i)

        # center at point i
        cnt_center_i = count_inside(points, xi, yi, r2, eps)
        acc_max = max(acc_max, cnt_center_i)

        Enum.reduce((i + 1)..(n - 1), acc_max, fn j, inner_acc ->
          {xj, yj} = Enum.at(points, j)
          dx = xj - xi
          dy = yj - yi
          d2 = dx * dx + dy * dy
          limit = (2.0 * r_f) * (2.0 * r_f)

          if d2 > limit + eps do
            inner_acc
          else
            d = :math.sqrt(d2)
            mx = (xi + xj) / 2.0
            my = (yi + yj) / 2.0
            h = :math.sqrt(r2 - (d / 2.0) * (d / 2.0))
            ux = -dy / d
            uy = dx / d

            c1x = mx + ux * h
            c1y = my + uy * h
            cnt1 = count_inside(points, c1x, c1y, r2, eps)

            c2x = mx - ux * h
            c2y = my - uy * h
            cnt2 = count_inside(points, c2x, c2y, r2, eps)

            inner_acc |> max(cnt1) |> max(cnt2)
          end
        end)
      end)
    end
  end

  defp count_inside(points, cx, cy, r2, eps) do
    Enum.reduce(points, 0, fn {x, y}, acc ->
      dx = x - cx
      dy = y - cy
      if dx * dx + dy * dy <= r2 + eps, do: acc + 1, else: acc
    end)
  end
end
```

# 3380. Maximum Area Rectangle With Point Constraints I

## Cpp

```cpp
class Solution {
public:
    int maxRectangleArea(vector<vector<int>>& points) {
        int n = points.size();
        unordered_set<long long> pointSet;
        for (auto &p : points) {
            long long key = ((long long)p[0] << 32) | (unsigned int)p[1];
            pointSet.insert(key);
        }
        int best = -1;
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue; // not a proper rectangle
                long long key3 = ((long long)x1 << 32) | (unsigned int)y2;
                long long key4 = ((long long)x2 << 32) | (unsigned int)y1;
                if (!pointSet.count(key3) || !pointSet.count(key4)) continue; // missing corners
                int minX = min(x1, x2), maxX = max(x1, x2);
                int minY = min(y1, y2), maxY = max(y1, y2);
                bool ok = true;
                for (auto &p : points) {
                    int px = p[0], py = p[1];
                    // skip the four corners
                    if ((px == x1 && py == y1) || (px == x2 && py == y2) ||
                        (px == x1 && py == y2) || (px == x2 && py == y1))
                        continue;
                    if (px >= minX && px <= maxX && py >= minY && py <= maxY) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    int area = (maxX - minX) * (maxY - minY);
                    best = max(best, area);
                }
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maxRectangleArea(int[][] points) {
        int n = points.length;
        java.util.HashSet<Long> pointSet = new java.util.HashSet<>();
        for (int[] p : points) {
            pointSet.add(encode(p[0], p[1]));
        }
        int best = -1;
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                if (x1 == x2 || y1 == y2) continue; // not opposite corners
                long need1 = encode(x1, y2);
                long need2 = encode(x2, y1);
                if (!pointSet.contains(need1) || !pointSet.contains(need2)) continue;
                int minX = Math.min(x1, x2), maxX = Math.max(x1, x2);
                int minY = Math.min(y1, y2), maxY = Math.max(y1, y2);
                boolean ok = true;
                for (int[] p : points) {
                    int x = p[0], y = p[1];
                    // skip the four corners
                    if ((x == x1 && y == y1) || (x == x2 && y == y2) ||
                        (x == x1 && y == y2) || (x == x2 && y == y1)) {
                        continue;
                    }
                    if (x >= minX && x <= maxX && y >= minY && y <= maxY) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    int area = (maxX - minX) * (maxY - minY);
                    best = Math.max(best, area);
                }
            }
        }
        return best;
    }

    private long encode(int x, int y) {
        return ((long) x << 32) | (y & 0xffffffffL);
    }
}
```

## Python

```python
class Solution(object):
    def maxRectangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        point_set = set(map(tuple, points))
        n = len(points)
        best = -1

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                # need distinct x and y to form a rectangle
                if x1 == x2 or y1 == y2:
                    continue

                # the other two corners must exist
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    min_x, max_x = (x1, x2) if x1 < x2 else (x2, x1)
                    min_y, max_y = (y1, y2) if y1 < y2 else (y2, y1)

                    # verify no other point lies inside or on the border
                    valid = True
                    for px, py in point_set:
                        if (px, py) in {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}:
                            continue
                        if min_x <= px <= max_x and min_y <= py <= max_y:
                            valid = False
                            break

                    if valid:
                        area = (max_x - min_x) * (max_y - min_y)
                        if area > best:
                            best = area

        return best
```

## Python3

```python
class Solution:
    def maxRectangleArea(self, points):
        point_set = { (x, y) for x, y in points }
        n = len(points)
        best = -1
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue  # not opposite corners
                # other two corners must exist
                if (x1, y2) not in point_set or (x2, y1) not in point_set:
                    continue
                # check for any extra point inside or on border
                x_low, x_high = (x1, x2) if x1 < x2 else (x2, x1)
                y_low, y_high = (y1, y2) if y1 < y2 else (y2, y1)
                valid = True
                for px, py in points:
                    if (px, py) in ((x1, y1), (x2, y2), (x1, y2), (x2, y1)):
                        continue
                    if x_low <= px <= x_high and y_low <= py <= y_high:
                        valid = False
                        break
                if valid:
                    area = (x_high - x_low) * (y_high - y_low)
                    if area > best:
                        best = area
        return best
```

## C

```c
int maxRectangleArea(int** points, int pointsSize, int* pointsColSize) {
    int maxArea = -1;
    for (int i = 0; i < pointsSize; ++i) {
        int xi = points[i][0];
        int yi = points[i][1];
        for (int j = i + 1; j < pointsSize; ++j) {
            int xj = points[j][0];
            int yj = points[j][1];
            if (xi == xj || yi == yj) continue; // not opposite corners
            
            // check existence of the other two corners
            int have1 = 0, have2 = 0;
            for (int k = 0; k < pointsSize; ++k) {
                if (k == i || k == j) continue;
                int xk = points[k][0];
                int yk = points[k][1];
                if (xk == xi && yk == yj) have1 = 1;
                if (xk == xj && yk == yi) have2 = 1;
            }
            if (!have1 || !have2) continue;
            
            int minX = xi < xj ? xi : xj;
            int maxX = xi > xj ? xi : xj;
            int minY = yi < yj ? yi : yj;
            int maxY = yi > yj ? yi : yj;
            
            // verify no other point lies inside or on border
            int ok = 1;
            for (int p = 0; p < pointsSize; ++p) {
                int xp = points[p][0];
                int yp = points[p][1];
                if (xp >= minX && xp <= maxX && yp >= minY && yp <= maxY) {
                    if (!((xp == xi && yp == yi) ||
                          (xp == xi && yp == yj) ||
                          (xp == xj && yp == yi) ||
                          (xp == xj && yp == yj))) {
                        ok = 0;
                        break;
                    }
                }
            }
            if (ok) {
                int area = (maxX - minX) * (maxY - minY);
                if (area > maxArea) maxArea = area;
            }
        }
    }
    return maxArea;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxRectangleArea(int[][] points)
    {
        var pointSet = new HashSet<(int, int)>();
        foreach (var p in points)
            pointSet.Add((p[0], p[1]));

        int n = points.Length;
        int maxArea = -1;

        for (int i = 0; i < n; i++)
        {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; j++)
            {
                int x2 = points[j][0];
                int y2 = points[j][1];

                if (x1 == x2 || y1 == y2) continue; // not opposite corners

                var c3 = (x1, y2);
                var c4 = (x2, y1);
                if (!pointSet.Contains(c3) || !pointSet.Contains(c4)) continue;

                int minX = Math.Min(x1, x2);
                int maxX = Math.Max(x1, x2);
                int minY = Math.Min(y1, y2);
                int maxY = Math.Max(y1, y2);

                bool valid = true;
                foreach (var p in points)
                {
                    int px = p[0];
                    int py = p[1];

                    // skip the four corners
                    if ((px == x1 && py == y1) ||
                        (px == x2 && py == y2) ||
                        (px == c3.Item1 && py == c3.Item2) ||
                        (px == c4.Item1 && py == c4.Item2))
                        continue;

                    // point lies inside or on the border
                    if (px >= minX && px <= maxX && py >= minY && py <= maxY)
                    {
                        valid = false;
                        break;
                    }
                }

                if (valid)
                {
                    int area = (maxX - minX) * (maxY - minY);
                    if (area > maxArea) maxArea = area;
                }
            }
        }

        return maxArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxRectangleArea = function(points) {
    const pointSet = new Set();
    for (const [x, y] of points) {
        pointSet.add(`${x},${y}`);
    }
    let maxArea = -1;
    const n = points.length;
    for (let i = 0; i < n; i++) {
        const [x1, y1] = points[i];
        for (let j = i + 1; j < n; j++) {
            const [x2, y2] = points[j];
            if (x1 === x2 || y1 === y2) continue; // not opposite corners
            const c3 = `${x1},${y2}`;
            const c4 = `${x2},${y1}`;
            if (!pointSet.has(c3) || !pointSet.has(c4)) continue;
            const minX = Math.min(x1, x2), maxX = Math.max(x1, x2);
            const minY = Math.min(y1, y2), maxY = Math.max(y1, y2);
            let valid = true;
            for (let k = 0; k < n; k++) {
                if (k === i || k === j) continue;
                const [x, y] = points[k];
                // skip the other two corners
                if ((x === x1 && y === y2) || (x === x2 && y === y1)) continue;
                if (x >= minX && x <= maxX && y >= minY && y <= maxY) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                const area = (maxX - minX) * (maxY - minY);
                if (area > maxArea) maxArea = area;
            }
        }
    }
    return maxArea;
};
```

## Typescript

```typescript
function maxRectangleArea(points: number[][]): number {
    const pointSet = new Set<string>();
    for (const [x, y] of points) {
        pointSet.add(`${x},${y}`);
    }
    let maxArea = -1;
    const n = points.length;
    for (let i = 0; i < n; i++) {
        const [x1, y1] = points[i];
        for (let j = i + 1; j < n; j++) {
            const [x2, y2] = points[j];
            if (x1 === x2 || y1 === y2) continue; // not opposite corners
            const c3 = `${x1},${y2}`;
            const c4 = `${x2},${y1}`;
            if (!pointSet.has(c3) || !pointSet.has(c4)) continue;
            const minX = Math.min(x1, x2);
            const maxX = Math.max(x1, x2);
            const minY = Math.min(y1, y2);
            const maxY = Math.max(y1, y2);
            let ok = true;
            for (let k = 0; k < n; k++) {
                if (k === i || k === j) continue;
                const [x, y] = points[k];
                // skip the other two corners
                if ((x === x1 && y === y2) || (x === x2 && y === y1)) continue;
                if (x >= minX && x <= maxX && y >= minY && y <= maxY) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                const area = (maxX - minX) * (maxY - minY);
                if (area > maxArea) maxArea = area;
            }
        }
    }
    return maxArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxRectangleArea($points) {
        $n = count($points);
        // Build a set for O(1) existence checks
        $pointSet = [];
        foreach ($points as $p) {
            $key = $p[0] . ',' . $p[1];
            $pointSet[$key] = true;
        }

        $maxArea = -1;

        for ($i = 0; $i < $n; ++$i) {
            [$x1, $y1] = $points[$i];
            for ($j = $i + 1; $j < $n; ++$j) {
                [$x2, $y2] = $points[$j];

                // Need opposite corners: both coordinates differ
                if ($x1 == $x2 || $y1 == $y2) continue;

                // Check the other two required corners exist
                $c3Key = $x1 . ',' . $y2;
                $c4Key = $x2 . ',' . $y1;
                if (!isset($pointSet[$c3Key]) || !isset($pointSet[$c4Key])) continue;

                // Determine rectangle bounds
                $minX = min($x1, $x2);
                $maxX = max($x1, $x2);
                $minY = min($y1, $y2);
                $maxY = max($y1, $y2);

                // Verify no other point lies inside or on the border
                $valid = true;
                foreach ($points as $p) {
                    $px = $p[0];
                    $py = $p[1];
                    // Skip the four corner points
                    if (
                        ($px == $x1 && $py == $y1) ||
                        ($px == $x2 && $py == $y2) ||
                        ($px == $x1 && $py == $y2) ||
                        ($px == $x2 && $py == $y1)
                    ) {
                        continue;
                    }
                    if ($px >= $minX && $px <= $maxX && $py >= $minY && $py <= $maxY) {
                        $valid = false;
                        break;
                    }
                }

                if ($valid) {
                    $area = ($maxX - $minX) * ($maxY - $minY);
                    if ($area > $maxArea) {
                        $maxArea = $area;
                    }
                }
            }
        }

        return $maxArea;
    }
}
```

## Swift

```swift
class Solution {
    func maxRectangleArea(_ points: [[Int]]) -> Int {
        let n = points.count
        var pointSet = Set<Int>()
        for p in points {
            pointSet.insert(p[0] * 101 + p[1])
        }
        var best = -1
        for i in 0..<n {
            let x1 = points[i][0]
            let y1 = points[i][1]
            for j in i+1..<n {
                let x2 = points[j][0]
                let y2 = points[j][1]
                if x1 == x2 || y1 == y2 { continue }
                // opposite corners
                let keyA = x1 * 101 + y2
                let keyB = x2 * 101 + y1
                if !pointSet.contains(keyA) || !pointSet.contains(keyB) {
                    continue
                }
                let minX = min(x1, x2)
                let maxX = max(x1, x2)
                let minY = min(y1, y2)
                let maxY = max(y1, y2)
                var ok = true
                for p in points {
                    let px = p[0]
                    let py = p[1]
                    // skip the four corners
                    if (px == x1 && py == y1) ||
                       (px == x2 && py == y2) ||
                       (px == x1 && py == y2) ||
                       (px == x2 && py == y1) {
                        continue
                    }
                    if px >= minX && px <= maxX && py >= minY && py <= maxY {
                        ok = false
                        break
                    }
                }
                if ok {
                    let area = (maxX - minX) * (maxY - minY)
                    if area > best { best = area }
                }
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxRectangleArea(points: Array<IntArray>): Int {
        val pointSet = HashSet<Long>()
        for (p in points) {
            val key = (p[0].toLong() shl 32) xor (p[1].toLong() and 0xffffffffL)
            pointSet.add(key)
        }
        var maxArea = -1
        val n = points.size
        for (i in 0 until n) {
            val x1 = points[i][0]
            val y1 = points[i][1]
            for (j in i + 1 until n) {
                val x2 = points[j][0]
                val y2 = points[j][1]
                if (x1 == x2 || y1 == y2) continue
                val keyA = (x1.toLong() shl 32) xor (y2.toLong() and 0xffffffffL)
                val keyB = (x2.toLong() shl 32) xor (y1.toLong() and 0xffffffffL)
                if (!pointSet.contains(keyA) || !pointSet.contains(keyB)) continue

                val rectPoints = HashSet<Long>()
                rectPoints.add((x1.toLong() shl 32) xor (y1.toLong() and 0xffffffffL))
                rectPoints.add((x2.toLong() shl 32) xor (y2.toLong() and 0xffffffffL))
                rectPoints.add(keyA)
                rectPoints.add(keyB)

                val minX = kotlin.math.min(x1, x2)
                val maxX = kotlin.math.max(x1, x2)
                val minY = kotlin.math.min(y1, y2)
                val maxY = kotlin.math.max(y1, y2)

                var ok = true
                for (p in points) {
                    val key = (p[0].toLong() shl 32) xor (p[1].toLong() and 0xffffffffL)
                    if (rectPoints.contains(key)) continue
                    if (p[0] >= minX && p[0] <= maxX && p[1] >= minY && p[1] <= maxY) {
                        ok = false
                        break
                    }
                }
                if (ok) {
                    val area = (maxX - minX) * (maxY - minY)
                    if (area > maxArea) maxArea = area
                }
            }
        }
        return maxArea
    }
}
```

## Dart

```dart
class Solution {
  int maxRectangleArea(List<List<int>> points) {
    int n = points.length;
    // Encode each point as a unique integer for O(1) lookup.
    const int factor = 101; // since coordinates are <= 100
    Set<int> pointSet = {};
    for (var p in points) {
      pointSet.add(p[0] * factor + p[1]);
    }

    int best = -1;

    for (int i = 0; i < n; ++i) {
      var p1 = points[i];
      for (int j = i + 1; j < n; ++j) {
        var p2 = points[j];

        // Must be opposite corners: both x and y differ.
        if (p1[0] == p2[0] || p1[1] == p2[1]) continue;

        int x1 = p1[0], y1 = p1[1];
        int x2 = p2[0], y2 = p2[1];

        // Check existence of the other two corners.
        if (!pointSet.contains(x1 * factor + y2)) continue;
        if (!pointSet.contains(x2 * factor + y1)) continue;

        int minX = x1 < x2 ? x1 : x2;
        int maxX = x1 > x2 ? x1 : x2;
        int minY = y1 < y2 ? y1 : y2;
        int maxY = y1 > y2 ? y1 : y2;

        bool valid = true;
        for (var p in points) {
          int px = p[0], py = p[1];
          // Skip the four corners of this rectangle.
          if ((px == x1 && py == y1) ||
              (px == x2 && py == y2) ||
              (px == x1 && py == y2) ||
              (px == x2 && py == y1)) {
            continue;
          }
          // If any other point lies inside or on the border, invalidate.
          if (px >= minX && px <= maxX && py >= minY && py <= maxY) {
            valid = false;
            break;
          }
        }

        if (valid) {
          int area = (maxX - minX) * (maxY - minY);
          if (area > best) best = area;
        }
      }
    }

    return best;
  }
}
```

## Golang

```go
func maxRectangleArea(points [][]int) int {
	n := len(points)
	pointSet := make(map[int]bool, n)
	const mul = 101 // coordinates are in [0,100]
	for _, p := range points {
		key := p[0]*mul + p[1]
		pointSet[key] = true
	}
	maxArea := -1

	for i := 0; i < n; i++ {
		x1, y1 := points[i][0], points[i][1]
		for j := i + 1; j < n; j++ {
			x2, y2 := points[j][0], points[j][1]

			if x1 == x2 || y1 == y2 {
				continue // not opposite corners
			}

			// other two required corners
			if !pointSet[x1*mul+y2] || !pointSet[x2*mul+y1] {
				continue
			}

			minX, maxX := x1, x2
			if minX > maxX {
				minX, maxX = maxX, minX
			}
			minY, maxY := y1, y2
			if minY > maxY {
				minY, maxY = maxY, minY
			}

			valid := true
			for k := 0; k < n && valid; k++ {
				if k == i || k == j {
					continue
				}
				px, py := points[k][0], points[k][1]
				// skip the other two corners if they appear in iteration
				if (px == x1 && py == y2) || (px == x2 && py == y1) {
					continue
				}
				if px >= minX && px <= maxX && py >= minY && py <= maxY {
					valid = false
				}
			}

			if valid {
				area := (maxX - minX) * (maxY - minY)
				if area > maxArea {
					maxArea = area
				}
			}
		}
	}
	return maxArea
}
```

## Ruby

```ruby
def max_rectangle_area(points)
  point_set = {}
  points.each { |x, y| point_set[[x, y]] = true }
  n = points.length
  max_area = -1

  (0...n).each do |i|
    x1, y1 = points[i]
    ((i + 1)...n).each do |j|
      x2, y2 = points[j]
      next if x1 == x2 || y1 == y2
      next unless point_set[[x1, y2]] && point_set[[x2, y1]]

      min_x = [x1, x2].min
      max_x = [x1, x2].max
      min_y = [y1, y2].min
      max_y = [y1, y2].max

      valid = true
      points.each do |px, py|
        next if (px == x1 && py == y1) || (px == x2 && py == y2) ||
                (px == x1 && py == y2) || (px == x2 && py == y1)
        if px >= min_x && px <= max_x && py >= min_y && py <= max_y
          valid = false
          break
        end
      end

      if valid
        area = (max_x - min_x) * (max_y - min_y)
        max_area = [max_area, area].max
      end
    end
  end

  max_area
end
```

## Scala

```scala
object Solution {
    def maxRectangleArea(points: Array[Array[Int]]): Int = {
        val n = points.length
        if (n < 4) return -1
        val pts = points.map(p => (p(0), p(1)))
        val pointSet = pts.toSet
        var maxArea = -1

        for (i <- 0 until n) {
            val (x1, y1) = pts(i)
            for (j <- i + 1 until n) {
                val (x2, y2) = pts(j)
                if (x1 != x2 && y1 != y2) {
                    if (pointSet.contains((x1, y2)) && pointSet.contains((x2, y1))) {
                        val minX = math.min(x1, x2)
                        val maxX = math.max(x1, x2)
                        val minY = math.min(y1, y2)
                        val maxY = math.max(y1, y2)

                        val corners = Set((x1, y1), (x1, y2), (x2, y1), (x2, y2))
                        var ok = true
                        for (k <- 0 until n if ok) {
                            val p = pts(k)
                            if (!corners.contains(p)) {
                                val (px, py) = p
                                if (px >= minX && px <= maxX && py >= minY && py <= maxY) {
                                    ok = false
                                }
                            }
                        }

                        if (ok) {
                            val area = (maxX - minX) * (maxY - minY)
                            if (area > maxArea) maxArea = area
                        }
                    }
                }
            }
        }

        maxArea
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn max_rectangle_area(points: Vec<Vec<i32>>) -> i32 {
        let mut set = HashSet::new();
        for p in &points {
            set.insert((p[0], p[1]));
        }
        let n = points.len();
        let mut best = -1;
        for i in 0..n {
            let x1 = points[i][0];
            let y1 = points[i][1];
            for j in (i + 1)..n {
                let x2 = points[j][0];
                let y2 = points[j][1];
                if x1 == x2 || y1 == y2 {
                    continue;
                }
                // check existence of the other two corners
                if !set.contains(&(x1, y2)) || !set.contains(&(x2, y1)) {
                    continue;
                }
                let min_x = x1.min(x2);
                let max_x = x1.max(x2);
                let min_y = y1.min(y2);
                let max_y = y1.max(y2);
                // verify no other point lies inside or on the border
                let mut ok = true;
                for p in &points {
                    let px = p[0];
                    let py = p[1];
                    if (px == x1 && py == y1)
                        || (px == x2 && py == y2)
                        || (px == x1 && py == y2)
                        || (px == x2 && py == y1)
                    {
                        continue;
                    }
                    if px >= min_x && px <= max_x && py >= min_y && py <= max_y {
                        ok = false;
                        break;
                    }
                }
                if ok {
                    let area = (max_x - min_x) * (max_y - min_y);
                    if area > best {
                        best = area;
                    }
                }
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (max-rectangle-area points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length points))
         (pt-hash (make-hash)))
    ;; store all points for O(1) lookup
    (for-each (lambda (p)
                (hash-set! pt-hash (cons (first p) (second p)) #t))
              points)
    (define max-area -1)
    (for ([i (in-range n)])
      (let ((p1 (list-ref points i)))
        (for ([j (in-range (+ i 1) n)])
          (let ((p2 (list-ref points j)))
            (define x1 (first p1)) (define y1 (second p1))
            (define x2 (first p2)) (define y2 (second p2))
            (when (and (not (= x1 x2)) (not (= y1 y2))) ; opposite corners
              (define c1 (cons x1 y1))
              (define c2 (cons x1 y2))
              (define c3 (cons x2 y1))
              (define c4 (cons x2 y2))
              (when (and (hash-has-key? pt-hash c1)
                         (hash-has-key? pt-hash c2)
                         (hash-has-key? pt-hash c3)
                         (hash-has-key? pt-hash c4))
                ;; verify no other point lies inside or on the border
                (define minx (min x1 x2))
                (define maxx (max x1 x2))
                (define miny (min y1 y2))
                (define maxy (max y1 y2))
                (define valid #t)
                (for ([p points])
                  (let ((px (first p)) (py (second p)))
                    (unless (or (and (= px x1) (= py y1))
                                (and (= px x1) (= py y2))
                                (and (= px x2) (= py y1))
                                (and (= px x2) (= py y2)))
                      (when (and (>= px minx) (<= px maxx)
                                 (>= py miny) (<= py maxy))
                        (set! valid #f)))))
                (when valid
                  (define area (* (abs (- x1 x2)) (abs (- y1 y2))))
                  (when (> area max-area) (set! max-area area))))))))))
    max-area)))
```

## Erlang

```erlang
-spec max_rectangle_area(Points :: [[integer()]]) -> integer().
max_rectangle_area(Points) ->
    PointTuples = [list_to_tuple(P) || P <- Points],
    Set = maps:from_list([{Pt, true} || Pt <- PointTuples]),
    MaxArea = max_rect(PointTuples, Set),
    MaxArea.

%% Compute maximum rectangle area among all unordered point pairs
max_rect(Points, Set) ->
    N = length(Points),
    Indices = lists:seq(1, N),
    Pairs = [{lists:nth(I, Points), lists:nth(J, Points)} ||
                I <- Indices,
                J <- Indices,
                I < J],
    lists:foldl(fun({P1, P2}, Acc) ->
        case rectangle_area(P1, P2, Set, Points) of
            {ok, Area} when Area > Acc -> Area;
            _ -> Acc
        end
    end, -1, Pairs).

%% Determine if a valid rectangle exists for the two opposite corners and return its area
rectangle_area({X1, Y1}=P1, {X2, Y2}=P2, Set, AllPoints) ->
    case (X1 =:= X2) orelse (Y1 =:= Y2) of
        true -> invalid;
        false ->
            C3 = {X1, Y2},
            C4 = {X2, Y1},
            case maps:is_key(C3, Set) andalso maps:is_key(C4, Set) of
                false -> invalid;
                true ->
                    Area = erlang:abs(X1 - X2) * erlang:abs(Y1 - Y2),
                    MinX = min(X1, X2), MaxX = max(X1, X2),
                    MinY = min(Y1, Y2), MaxY = max(Y1, Y2),
                    CornerMap = maps:from_list([{P1, true}, {P2, true},
                                                {C3, true}, {C4, true}]),
                    case has_inside(AllPoints, CornerMap, MinX, MaxX, MinY, MaxY) of
                        true -> invalid;
                        false -> {ok, Area}
                    end
            end
    end.

%% Check whether any non‑corner point lies inside or on the border of the rectangle
has_inside([], _CornerMap, _, _, _, _) ->
    false;
has_inside([Pt | Rest], CornerMap, MinX, MaxX, MinY, MaxY) ->
    case maps:is_key(Pt, CornerMap) of
        true -> has_inside(Rest, CornerMap, MinX, MaxX, MinY, MaxY);
        false ->
            {X, Y} = Pt,
            if X >= MinX, X =< MaxX, Y >= MinY, Y =< MaxY ->
                    true;
               true ->
                    has_inside(Rest, CornerMap, MinX, MaxX, MinY, MaxY)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_rectangle_area(points :: [[integer]]) :: integer
  def max_rectangle_area(points) do
    pts = Enum.map(points, fn [x, y] -> {x, y} end)
    set = MapSet.new(pts)
    n = length(pts)

    Enum.reduce(0..(n - 2), -1, fn i, acc ->
      p1 = Enum.at(pts, i)

      Enum.reduce((i + 1)..(n - 1), acc, fn j, acc2 ->
        p2 = Enum.at(pts, j)
        {x1, y1} = p1
        {x2, y2} = p2

        if x1 == x2 or y1 == y2 do
          acc2
        else
          other1 = {x1, y2}
          other2 = {x2, y1}

          if MapSet.member?(set, other1) and MapSet.member?(set, other2) do
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)

            valid =
              Enum.all?(pts, fn {x, y} = pt ->
                if pt == p1 or pt == p2 or pt == other1 or pt == other2 do
                  true
                else
                  not (x >= min_x and x <= max_x and y >= min_y and y <= max_y)
                end
              end)

            if valid do
              area = (max_x - min_x) * (max_y - min_y)
              max(acc2, area)
            else
              acc2
            end
          else
            acc2
          end
        end
      end)
    end)
  end
end
```

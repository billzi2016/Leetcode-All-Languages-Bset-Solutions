# 0391. Perfect Rectangle

## Cpp

```cpp
class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        long long totalArea = 0;
        int minX = INT_MAX, minY = INT_MAX, maxX = INT_MIN, maxY = INT_MIN;
        unordered_set<long long> corners;
        
        auto encode = [&](int x, int y) -> long long {
            return (static_cast<long long>(x) << 32) | static_cast<unsigned int>(y);
        };
        auto toggle = [&](long long p) {
            if (!corners.erase(p)) corners.insert(p);
        };
        
        for (const auto& r : rectangles) {
            int x1 = r[0], y1 = r[1], x2 = r[2], y2 = r[3];
            totalArea += 1LL * (x2 - x1) * (y2 - y1);
            minX = min(minX, x1);
            minY = min(minY, y1);
            maxX = max(maxX, x2);
            maxY = max(maxY, y2);
            
            toggle(encode(x1, y1));
            toggle(encode(x1, y2));
            toggle(encode(x2, y1));
            toggle(encode(x2, y2));
        }
        
        long long expectedArea = 1LL * (maxX - minX) * (maxY - minY);
        if (totalArea != expectedArea) return false;
        if (corners.size() != 4) return false;
        
        return corners.count(encode(minX, minY)) &&
               corners.count(encode(minX, maxY)) &&
               corners.count(encode(maxX, minY)) &&
               corners.count(encode(maxX, maxY));
    }
};
```

## Java

```java
class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        if (rectangles == null || rectangles.length == 0) return false;
        long totalArea = 0;
        int minX = Integer.MAX_VALUE, minY = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE, maxY = Integer.MIN_VALUE;
        java.util.HashSet<String> points = new java.util.HashSet<>();
        for (int[] r : rectangles) {
            int x1 = r[0], y1 = r[1], x2 = r[2], y2 = r[3];
            if (x1 >= x2 || y1 >= y2) return false; // invalid rectangle, though constraints guarantee otherwise
            minX = Math.min(minX, x1);
            minY = Math.min(minY, y1);
            maxX = Math.max(maxX, x2);
            maxY = Math.max(maxY, y2);
            long area = (long) (x2 - x1) * (y2 - y1);
            totalArea += area;
            String[] corners = {
                x1 + " " + y1,
                x1 + " " + y2,
                x2 + " " + y1,
                x2 + " " + y2
            };
            for (String c : corners) {
                if (!points.add(c)) {
                    points.remove(c);
                }
            }
        }
        long expectedArea = (long) (maxX - minX) * (maxY - minY);
        if (totalArea != expectedArea) return false;
        if (points.size() != 4) return false;
        String[] finalCorners = {
            minX + " " + minY,
            minX + " " + maxY,
            maxX + " " + minY,
            maxX + " " + maxY
        };
        for (String c : finalCorners) {
            if (!points.contains(c)) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if not rectangles:
            return False

        point_set = set()
        area_sum = 0
        min_x = float('inf')
        min_y = float('inf')
        max_x = -float('inf')
        max_y = -float('inf')

        for x1, y1, x2, y2 in rectangles:
            # update bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # accumulate area
            area_sum += (x2 - x1) * (y2 - y1)

            # toggle corners in the set
            for p in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if p in point_set:
                    point_set.remove(p)
                else:
                    point_set.add(p)

        # after processing all rectangles, there must be exactly four corners
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        if point_set != expected_corners:
            return False

        # total area must match bounding rectangle area
        return area_sum == (max_x - min_x) * (max_y - min_y)
```

## Python3

```python
from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles:
            return False

        min_x = float('inf')
        min_y = float('inf')
        max_x = -float('inf')
        max_y = -float('inf')
        area_sum = 0
        corners = set()

        for x1, y1, x2, y2 in rectangles:
            # update bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # accumulate area
            area_sum += (x2 - x1) * (y2 - y1)

            # toggle corners
            for pt in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if pt in corners:
                    corners.remove(pt)
                else:
                    corners.add(pt)

        # The final set should contain exactly the four corners of the bounding rectangle
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        if corners != expected_corners:
            return False

        # Total area must match bounding rectangle area
        return area_sum == (max_x - min_x) * (max_y - min_y)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

static int cmp_ll(const void *a, const void *b) {
    long long va = *(const long long *)a;
    long long vb = *(const long long *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

bool isRectangleCover(int** rectangles, int rectanglesSize, int* rectanglesColSize){
    if (rectanglesSize == 0) return false;

    long long totalArea = 0;
    int minX = INT_MAX, minY = INT_MAX, maxX = INT_MIN, maxY = INT_MIN;

    long long *points = (long long *)malloc(sizeof(long long) * rectanglesSize * 4);
    if (!points) return false; // allocation failure

    int idx = 0;
    for (int i = 0; i < rectanglesSize; ++i) {
        int x1 = rectangles[i][0];
        int y1 = rectangles[i][1];
        int x2 = rectangles[i][2];
        int y2 = rectangles[i][3];

        if (x1 < minX) minX = x1;
        if (y1 < minY) minY = y1;
        if (x2 > maxX) maxX = x2;
        if (y2 > maxY) maxY = y2;

        long long area = (long long)(x2 - x1) * (long long)(y2 - y1);
        totalArea += area;

        points[idx++] = ((long long)x1 << 32) | (unsigned int)y1;
        points[idx++] = ((long long)x1 << 32) | (unsigned int)y2;
        points[idx++] = ((long long)x2 << 32) | (unsigned int)y1;
        points[idx++] = ((long long)x2 << 32) | (unsigned int)y2;
    }

    long long expectedArea = (long long)(maxX - minX) * (long long)(maxY - minY);
    if (totalArea != expectedArea) {
        free(points);
        return false;
    }

    qsort(points, idx, sizeof(long long), cmp_ll);

    int oddCount = 0;
    long long oddPoints[4];
    for (int i = 0; i < idx; ) {
        int j = i + 1;
        while (j < idx && points[j] == points[i]) ++j;
        int cnt = j - i;
        if (cnt % 2 == 1) {
            if (oddCount < 4) oddPoints[oddCount] = points[i];
            ++oddCount;
        }
        i = j;
    }

    free(points);

    if (oddCount != 4) return false;

    long long need[4];
    need[0] = ((long long)minX << 32) | (unsigned int)minY;
    need[1] = ((long long)minX << 32) | (unsigned int)maxY;
    need[2] = ((long long)maxX << 32) | (unsigned int)minY;
    need[3] = ((long long)maxX << 32) | (unsigned int)maxY;

    // sort both arrays to compare irrespective of order
    qsort(oddPoints, 4, sizeof(long long), cmp_ll);
    qsort(need, 4, sizeof(long long), cmp_ll);

    for (int i = 0; i < 4; ++i) {
        if (oddPoints[i] != need[i]) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsRectangleCover(int[][] rectangles)
    {
        long minX = long.MaxValue, minY = long.MaxValue;
        long maxX = long.MinValue, maxY = long.MinValue;
        long totalArea = 0;
        var corners = new HashSet<string>();

        foreach (var rect in rectangles)
        {
            long x1 = rect[0];
            long y1 = rect[1];
            long x2 = rect[2];
            long y2 = rect[3];

            minX = Math.Min(minX, x1);
            minY = Math.Min(minY, y1);
            maxX = Math.Max(maxX, x2);
            maxY = Math.Max(maxY, y2);

            totalArea += (x2 - x1) * (y2 - y1);

            string[] pts = {
                $"{x1}_{y1}",
                $"{x1}_{y2}",
                $"{x2}_{y1}",
                $"{x2}_{y2}"
            };

            foreach (var p in pts)
            {
                if (!corners.Add(p))
                    corners.Remove(p);
            }
        }

        long boundingArea = (maxX - minX) * (maxY - minY);
        if (totalArea != boundingArea) return false;
        if (corners.Count != 4) return false;

        string[] required = {
            $"{minX}_{minY}",
            $"{minX}_{maxY}",
            $"{maxX}_{minY}",
            $"{maxX}_{maxY}"
        };

        foreach (var p in required)
            if (!corners.Contains(p))
                return false;

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} rectangles
 * @return {boolean}
 */
var isRectangleCover = function(rectangles) {
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    let totalArea = 0;
    const points = new Set();

    for (const rect of rectangles) {
        const [x1, y1, x2, y2] = rect;
        // update bounding box
        if (x1 < minX) minX = x1;
        if (y1 < minY) minY = y1;
        if (x2 > maxX) maxX = x2;
        if (y2 > maxY) maxY = y2;

        totalArea += (x2 - x1) * (y2 - y1);

        const corners = [
            `${x1}_${y1}`,
            `${x1}_${y2}`,
            `${x2}_${y1}`,
            `${x2}_${y2}`
        ];

        for (const p of corners) {
            if (points.has(p)) {
                points.delete(p);
            } else {
                points.add(p);
            }
        }
    }

    const expectedArea = (maxX - minX) * (maxY - minY);
    if (totalArea !== expectedArea) return false;
    if (points.size !== 4) return false;

    const required = new Set([
        `${minX}_${minY}`,
        `${minX}_${maxY}`,
        `${maxX}_${minY}`,
        `${maxX}_${maxY}`
    ]);

    for (const p of points) {
        if (!required.has(p)) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isRectangleCover(rectangles: number[][]): boolean {
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    let totalArea = 0;
    const corners = new Set<string>();

    for (const rect of rectangles) {
        const [x1, y1, x2, y2] = rect;
        // update bounding box
        if (x1 < minX) minX = x1;
        if (y1 < minY) minY = y1;
        if (x2 > maxX) maxX = x2;
        if (y2 > maxY) maxY = y2;

        totalArea += (x2 - x1) * (y2 - y1);

        const pts: [number, number][] = [
            [x1, y1],
            [x1, y2],
            [x2, y1],
            [x2, y2]
        ];

        for (const [cx, cy] of pts) {
            const key = `${cx},${cy}`;
            if (corners.has(key)) {
                corners.delete(key);
            } else {
                corners.add(key);
            }
        }
    }

    const expectedArea = (maxX - minX) * (maxY - minY);
    if (totalArea !== expectedArea) return false;
    if (corners.size !== 4) return false;

    const required = [
        `${minX},${minY}`,
        `${minX},${maxY}`,
        `${maxX},${minY}`,
        `${maxX},${maxY}`
    ];
    for (const key of required) {
        if (!corners.has(key)) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @return Boolean
     */
    function isRectangleCover($rectangles) {
        $minX = PHP_INT_MAX;
        $minY = PHP_INT_MAX;
        $maxX = PHP_INT_MIN;
        $maxY = PHP_INT_MIN;
        $area = 0;
        $points = [];

        foreach ($rectangles as $rec) {
            list($x1, $y1, $x2, $y2) = $rec;

            if ($x1 < $minX) $minX = $x1;
            if ($y1 < $minY) $minY = $y1;
            if ($x2 > $maxX) $maxX = $x2;
            if ($y2 > $maxY) $maxY = $y2;

            $area += ($x2 - $x1) * ($y2 - $y1);

            $corners = [
                "$x1:$y1",
                "$x1:$y2",
                "$x2:$y1",
                "$x2:$y2"
            ];

            foreach ($corners as $c) {
                if (isset($points[$c])) {
                    unset($points[$c]);
                } else {
                    $points[$c] = true;
                }
            }
        }

        $expectedArea = ($maxX - $minX) * ($maxY - $minY);
        if ($area !== $expectedArea) return false;

        if (count($points) !== 4) return false;

        $required = [
            "$minX:$minY",
            "$minX:$maxY",
            "$maxX:$minY",
            "$maxX:$maxY"
        ];

        foreach ($required as $c) {
            if (!isset($points[$c])) return false;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isRectangleCover(_ rectangles: [[Int]]) -> Bool {
        var minX = Int.max, minY = Int.max, maxX = Int.min, maxY = Int.min
        var pointSet = Set<String>()
        var totalArea: Int64 = 0

        for rect in rectangles {
            let x1 = rect[0], y1 = rect[1], x2 = rect[2], y2 = rect[3]

            if x1 < minX { minX = x1 }
            if y1 < minY { minY = y1 }
            if x2 > maxX { maxX = x2 }
            if y2 > maxY { maxY = y2 }

            totalArea += Int64(x2 - x1) * Int64(y2 - y1)

            let corners = [
                "\(x1)#\(y1)",
                "\(x1)#\(y2)",
                "\(x2)#\(y1)",
                "\(x2)#\(y2)"
            ]

            for p in corners {
                if pointSet.contains(p) {
                    pointSet.remove(p)
                } else {
                    pointSet.insert(p)
                }
            }
        }

        let expectedArea = Int64(maxX - minX) * Int64(maxY - minY)
        if totalArea != expectedArea { return false }
        if pointSet.count != 4 { return false }

        let required: Set<String> = [
            "\(minX)#\(minY)",
            "\(minX)#\(maxY)",
            "\(maxX)#\(minY)",
            "\(maxX)#\(maxY)"
        ]

        return pointSet == required
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isRectangleCover(rectangles: Array<IntArray>): Boolean {
        var minX = Int.MAX_VALUE
        var minY = Int.MAX_VALUE
        var maxX = Int.MIN_VALUE
        var maxY = Int.MIN_VALUE
        var totalArea = 0L
        val points = HashSet<String>()

        for (rect in rectangles) {
            val x1 = rect[0]
            val y1 = rect[1]
            val x2 = rect[2]
            val y2 = rect[3]

            minX = kotlin.math.min(minX, x1)
            minY = kotlin.math.min(minY, y1)
            maxX = kotlin.math.max(maxX, x2)
            maxY = kotlin.math.max(maxY, y2)

            totalArea += (x2 - x1).toLong() * (y2 - y1).toLong()

            val corners = arrayOf(
                "$x1 $y1",
                "$x1 $y2",
                "$x2 $y1",
                "$x2 $y2"
            )
            for (c in corners) {
                if (!points.add(c)) {
                    points.remove(c)
                }
            }
        }

        val expectedArea = (maxX - minX).toLong() * (maxY - minY).toLong()
        if (totalArea != expectedArea) return false
        if (points.size != 4) return false

        val required = arrayOf(
            "$minX $minY",
            "$minX $maxY",
            "$maxX $minY",
            "$maxX $maxY"
        )
        for (c in required) {
            if (!points.contains(c)) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isRectangleCover(List<List<int>> rectangles) {
    int minX = rectangles[0][0];
    int minY = rectangles[0][1];
    int maxX = rectangles[0][2];
    int maxY = rectangles[0][3];
    int totalArea = 0;
    final Set<String> points = {};

    for (final rect in rectangles) {
      final int x1 = rect[0], y1 = rect[1], x2 = rect[2], y2 = rect[3];

      if (x1 < minX) minX = x1;
      if (y1 < minY) minY = y1;
      if (x2 > maxX) maxX = x2;
      if (y2 > maxY) maxY = y2;

      totalArea += (x2 - x1) * (y2 - y1);

      final List<String> corners = [
        '$x1,$y1',
        '$x1,$y2',
        '$x2,$y1',
        '$x2,$y2'
      ];
      for (final p in corners) {
        if (!points.remove(p)) {
          points.add(p);
        }
      }
    }

    final int boundingArea = (maxX - minX) * (maxY - minY);
    if (totalArea != boundingArea) return false;
    if (points.length != 4) return false;

    final Set<String> expected = {
      '$minX,$minY',
      '$minX,$maxY',
      '$maxX,$minY',
      '$maxX,$maxY'
    };
    for (final p in expected) {
      if (!points.contains(p)) return false;
    }
    return true;
  }
}
```

## Golang

```go
func isRectangleCover(rectangles [][]int) bool {
	type point struct{ x, y int }
	corners := make(map[point]bool)

	const INF = 1 << 30
	minX, minY := INF, INF
	maxX, maxY := -INF, -INF

	var totalArea int64 = 0

	for _, r := range rectangles {
		x1, y1, x2, y2 := r[0], r[1], r[2], r[3]

		if x1 < minX {
			minX = x1
		}
		if y1 < minY {
			minY = y1
		}
		if x2 > maxX {
			maxX = x2
		}
		if y2 > maxY {
			maxY = y2
		}

		totalArea += int64(x2-x1) * int64(y2-y1)

		ps := []point{{x1, y1}, {x1, y2}, {x2, y1}, {x2, y2}}
		for _, p := range ps {
			if corners[p] {
				delete(corners, p)
			} else {
				corners[p] = true
			}
		}
	}

	expectedArea := int64(maxX-minX) * int64(maxY-minY)
	if totalArea != expectedArea {
		return false
	}
	if len(corners) != 4 {
		return false
	}
	required := []point{{minX, minY}, {minX, maxY}, {maxX, minY}, {maxX, maxY}}
	for _, p := range required {
		if !corners[p] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_rectangle_cover(rectangles)
  require 'set'
  point_set = Set.new
  area = 0
  min_x = Float::INFINITY
  min_y = Float::INFINITY
  max_a = -Float::INFINITY
  max_b = -Float::INFINITY

  rectangles.each do |rect|
    x1, y1, x2, y2 = rect
    area += (x2 - x1) * (y2 - y1)
    min_x = [min_x, x1].min
    min_y = [min_y, y1].min
    max_a = [max_a, x2].max
    max_b = [max_b, y2].max

    [[x1, y1], [x1, y2], [x2, y1], [x2, y2]].each do |p|
      if point_set.include?(p)
        point_set.delete(p)
      else
        point_set.add(p)
      end
    end
  end

  return false unless area == (max_a - min_x) * (max_b - min_y)

  expected = Set.new([[min_x, min_y], [min_x, max_b], [max_a, min_y], [max_a, max_b]])
  point_set == expected
end
```

## Scala

```scala
object Solution {
    def isRectangleCover(rectangles: Array[Array[Int]]): Boolean = {
        import scala.collection.mutable
        var minX = Int.MaxValue
        var minY = Int.MaxValue
        var maxX = Int.MinValue
        var maxY = Int.MinValue
        var totalArea: Long = 0L
        val points = mutable.HashSet[(Int, Int)]()
        for (rect <- rectangles) {
            val x1 = rect(0)
            val y1 = rect(1)
            val x2 = rect(2)
            val y2 = rect(3)
            if (x1 < minX) minX = x1
            if (y1 < minY) minY = y1
            if (x2 > maxX) maxX = x2
            if (y2 > maxY) maxY = y2
            totalArea += (x2 - x1).toLong * (y2 - y1).toLong
            val corners = Array((x1, y1), (x1, y2), (x2, y1), (x2, y2))
            for (c <- corners) {
                if (!points.add(c)) points.remove(c)
            }
        }
        val expectedArea = (maxX - minX).toLong * (maxY - minY).toLong
        if (totalArea != expectedArea) return false
        if (points.size != 4) return false
        val expectedCorners = Set((minX, minY), (minX, maxY), (maxX, minY), (maxX, maxY))
        points == expectedCorners
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_rectangle_cover(rectangles: Vec<Vec<i32>>) -> bool {
        use std::collections::HashSet;
        if rectangles.is_empty() {
            return false;
        }
        let mut min_x = i32::MAX;
        let mut min_y = i32::MAX;
        let mut max_x = i32::MIN;
        let mut max_y = i32::MIN;
        let mut area: i64 = 0;
        let mut points: HashSet<(i32, i32)> = HashSet::new();

        for r in rectangles.iter() {
            let x1 = r[0];
            let y1 = r[1];
            let x2 = r[2];
            let y2 = r[3];

            if x1 < min_x { min_x = x1; }
            if y1 < min_y { min_y = y1; }
            if x2 > max_x { max_x = x2; }
            if y2 > max_y { max_y = y2; }

            area += (x2 - x1) as i64 * (y2 - y1) as i64;

            let corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)];
            for &c in &corners {
                if !points.insert(c) {
                    points.remove(&c);
                }
            }
        }

        let expected_area = (max_x - min_x) as i64 * (max_y - min_y) as i64;
        if area != expected_area {
            return false;
        }

        if points.len() != 4 {
            return false;
        }

        let required = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)];
        for &c in &required {
            if !points.contains(&c) {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-rectangle-cover rectangles)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((first (car rectangles))
         (min-x (list-ref first 0))
         (min-y (list-ref first 1))
         (max-x (list-ref first 2))
         (max-y (list-ref first 3))
         (area-sum 0)
         (corner-set (make-hash)))
    (for ([rect rectangles])
      (define x1 (list-ref rect 0))
      (define y1 (list-ref rect 1))
      (define x2 (list-ref rect 2))
      (define y2 (list-ref rect 3))
      (set! min-x (min min-x x1))
      (set! min-y (min min-y y1))
      (set! max-x (max max-x x2))
      (set! max-y (max max-y y2))
      (set! area-sum (+ area-sum (* (- x2 x1) (- y2 y1))))
      (for ([pt (list (cons x1 y1)
                      (cons x1 y2)
                      (cons x2 y1)
                      (cons x2 y2))])
        (if (hash-has-key? corner-set pt)
            (hash-remove! corner-set pt)
            (hash-set! corner-set pt #t))))
    (define expected-area (* (- max-x min-x) (- max-y min-y)))
    (and (= area-sum expected-area)
         (= (hash-count corner-set) 4)
         (let ((bl (cons min-x min-y))
               (tl (cons min-x max-y))
               (br (cons max-x min-y))
               (tr (cons max-x max-y)))
           (and (hash-has-key? corner-set bl)
                (hash-has-key? corner-set tl)
                (hash-has-key? corner-set br)
                (hash-has-key? corner-set tr))))))
```

## Erlang

```erlang
-module(solution).
-export([is_rectangle_cover/1]).

-spec is_rectangle_cover(Rectangles :: [[integer()]]) -> boolean().
is_rectangle_cover([]) ->
    false;
is_rectangle_cover(Rectangles) ->
    [First|Rest] = Rectangles,
    [X1,Y1,X2,Y2] = First,
    InitialArea = (X2 - X1)*(Y2 - Y1),
    InitialSet = toggle_corners(#{} , [{X1,Y1},{X1,Y2},{X2,Y1},{X2,Y2}]),
    FoldFun = fun([A,B,C,D], {MinX, MinY, MaxA, MaxB, AreaAcc, Set}) ->
        NewMinX = min(MinX, A),
        NewMinY = min(MinY, B),
        NewMaxA = max(MaxA, C),
        NewMaxB = max(MaxB, D),
        NewArea = AreaAcc + (C - A)*(D - B),
        NewSet = toggle_corners(Set, [{A,B},{A,D},{C,B},{C,D}]),
        {NewMinX, NewMinY, NewMaxA, NewMaxB, NewArea, NewSet}
    end,
    {MinX, MinY, MaxA, MaxB, TotalArea, FinalSet} =
        lists:foldl(FoldFun, {X1,Y1,X2,Y2,InitialArea, InitialSet}, Rest),
    ExpectedArea = (MaxA - MinX)*(MaxB - MinY),
    if
        TotalArea =:= ExpectedArea,
        map_size(FinalSet) =:= 4 ->
            Required = [{MinX,MinY},{MinX,MaxB},{MaxA,MinY},{MaxA,MaxB}],
            lists:all(fun(P) -> maps:is_key(P, FinalSet) end, Required);
        true -> false
    end.

toggle_corners(Set, Points) ->
    lists:foldl(
        fun(P, Acc) ->
            case maps:is_key(P, Acc) of
                true -> maps:remove(P, Acc);
                false -> maps:put(P, true, Acc)
            end
        end,
        Set,
        Points
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_rectangle_cover(rectangles :: [[integer]]) :: boolean
  def is_rectangle_cover(rectangles) do
    {min_x, min_y, max_a, max_b, total_area, corners} =
      Enum.reduce(rectangles, {nil, nil, nil, nil, 0, MapSet.new()}, fn [x, y, a, b],
                                                                      {mx, my, Mx, My, sum, set} ->
        mx = if mx == nil or x < mx, do: x, else: mx
        my = if my == nil or y < my, do: y, else: my
        Mx = if Mx == nil or a > Mx, do: a, else: Mx
        My = if My == nil or b > My, do: b, else: My

        sum = sum + (a - x) * (b - y)

        set =
          Enum.reduce([{x, y}, {x, b}, {a, y}, {a, b}], set, fn pt, acc ->
            if MapSet.member?(acc, pt), do: MapSet.delete(acc, pt), else: MapSet.put(acc, pt)
          end)

        {mx, my, Mx, My, sum, set}
      end)

    expected_area = (max_a - min_x) * (max_b - min_y)

    if total_area != expected_area do
      false
    else
      required_corners = MapSet.new([{min_x, min_y}, {min_x, max_b}, {max_a, min_y}, {max_a, max_b}])
      MapSet.size(corners) == 4 and MapSet.equal?(corners, required_corners)
    end
  end
end
```

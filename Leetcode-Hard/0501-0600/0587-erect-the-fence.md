# 0587. Erect the Fence

## Cpp

```cpp
class Solution {
public:
    static long long cross(const vector<int>& O, const vector<int>& A, const vector<int>& B) {
        return (long long)(A[0] - O[0]) * (B[1] - O[1]) -
               (long long)(A[1] - O[1]) * (B[0] - O[0]);
    }
    
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        int n = trees.size();
        if (n <= 1) return trees;
        
        sort(trees.begin(), trees.end());
        vector<vector<int>> lower, upper;
        
        for (const auto& p : trees) {
            while (lower.size() >= 2 && cross(lower[lower.size() - 2], lower.back(), p) < 0)
                lower.pop_back();
            lower.push_back(p);
        }
        
        for (int i = n - 1; i >= 0; --i) {
            const auto& p = trees[i];
            while (upper.size() >= 2 && cross(upper[upper.size() - 2], upper.back(), p) < 0)
                upper.pop_back();
            upper.push_back(p);
        }
        
        vector<vector<int>> hull = lower;
        for (size_t i = 1; i + 1 < upper.size(); ++i)
            hull.push_back(upper[i]);
        
        sort(hull.begin(), hull.end());
        hull.erase(unique(hull.begin(), hull.end()), hull.end());
        return hull;
    }
};
```

## Java

```java
class Solution {
    public int[][] outerTrees(int[][] trees) {
        int n = trees.length;
        if (n <= 1) {
            int[][] res = new int[n][];
            for (int i = 0; i < n; i++) {
                res[i] = new int[]{trees[i][0], trees[i][1]};
            }
            return res;
        }

        Arrays.sort(trees, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));

        List<int[]> lower = new ArrayList<>();
        for (int[] p : trees) {
            while (lower.size() >= 2 && cross(lower.get(lower.size() - 2), lower.get(lower.size() - 1), p) < 0) {
                lower.remove(lower.size() - 1);
            }
            lower.add(p);
        }

        List<int[]> upper = new ArrayList<>();
        for (int i = n - 1; i >= 0; --i) {
            int[] p = trees[i];
            while (upper.size() >= 2 && cross(upper.get(upper.size() - 2), upper.get(upper.size() - 1), p) < 0) {
                upper.remove(upper.size() - 1);
            }
            upper.add(p);
        }

        Set<String> seen = new HashSet<>();
        List<int[]> result = new ArrayList<>();

        for (int[] p : lower) {
            String key = p[0] + "," + p[1];
            if (seen.add(key)) {
                result.add(new int[]{p[0], p[1]});
            }
        }
        for (int[] p : upper) {
            String key = p[0] + "," + p[1];
            if (seen.add(key)) {
                result.add(new int[]{p[0], p[1]});
            }
        }

        return result.toArray(new int[result.size()][]);
    }

    private long cross(int[] o, int[] a, int[] b) {
        return (long) (a[0] - o[0]) * (b[1] - o[1]) - (long) (a[1] - o[1]) * (b[0] - o[0]);
    }
}
```

## Python

```python
class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(trees) <= 1:
            return trees

        # Convert to tuples for easier handling and sort lexicographically
        points = sorted(map(tuple, trees))

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Concatenate lower and upper to get full hull; omit last point of each because it repeats
        hull = lower[:-1] + upper[:-1]

        # Remove duplicates (possible when all points are collinear)
        unique_hull = list({(x, y) for x, y in hull})

        return [list(p) for p in unique_hull]
```

## Python3

```python
from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees[:]
        
        # Sort points lexicographically
        pts = sorted(trees)
        
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
        
        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
        
        # Use a set to avoid duplicates (handles collinear cases)
        hull_set = {tuple(point) for point in lower + upper}
        return [list(pt) for pt in hull_set]
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int x;
    int y;
} Point;

static long long cross(const Point *o, const Point *a, const Point *b) {
    return (long long)(a->x - o->x) * (b->y - o->y) -
           (long long)(a->y - o->y) * (b->x - o->x);
}

static int cmpPoint(const void *pa, const void *pb) {
    const Point *a = (const Point *)pa;
    const Point *b = (const Point *)pb;
    if (a->x != b->x) return a->x - b->x;
    return a->y - b->y;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** outerTrees(int** trees, int treesSize, int* treesColSize, int* returnSize, int*** returnColumnSizes) {
    if (treesSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    // Copy points
    Point *pts = (Point *)malloc(sizeof(Point) * treesSize);
    for (int i = 0; i < treesSize; ++i) {
        pts[i].x = trees[i][0];
        pts[i].y = trees[i][1];
    }

    qsort(pts, treesSize, sizeof(Point), cmpPoint);

    // Allocate hull arrays (max size = treesSize)
    Point *lower = (Point *)malloc(sizeof(Point) * treesSize);
    int lowerSize = 0;
    for (int i = 0; i < treesSize; ++i) {
        while (lowerSize >= 2 && cross(&lower[lowerSize-2], &lower[lowerSize-1], &pts[i]) < 0)
            lowerSize--;
        lower[lowerSize++] = pts[i];
    }

    Point *upper = (Point *)malloc(sizeof(Point) * treesSize);
    int upperSize = 0;
    for (int i = treesSize - 1; i >= 0; --i) {
        while (upperSize >= 2 && cross(&upper[upperSize-2], &upper[upperSize-1], &pts[i]) < 0)
            upperSize--;
        upper[upperSize++] = pts[i];
    }

    // Combine, using visited map to avoid duplicates
    char visited[101][101];
    memset(visited, 0, sizeof(visited));

    int capacity = treesSize * 2; // enough
    Point *hull = (Point *)malloc(sizeof(Point) * capacity);
    int hullCount = 0;

    for (int i = 0; i < lowerSize; ++i) {
        int x = lower[i].x, y = lower[i].y;
        if (!visited[x][y]) {
            visited[x][y] = 1;
            hull[hullCount++] = lower[i];
        }
    }
    for (int i = 0; i < upperSize; ++i) {
        int x = upper[i].x, y = upper[i].y;
        if (!visited[x][y]) {
            visited[x][y] = 1;
            hull[hullCount++] = upper[i];
        }
    }

    // Prepare return structures
    *returnSize = hullCount;
    int **result = (int **)malloc(sizeof(int *) * hullCount);
    int *colSizes = (int *)malloc(sizeof(int) * hullCount);
    for (int i = 0; i < hullCount; ++i) {
        result[i] = (int *)malloc(2 * sizeof(int));
        result[i][0] = hull[i].x;
        result[i][1] = hull[i].y;
        colSizes[i] = 2;
    }
    *returnColumnSizes = &colSizes;

    // Clean up
    free(pts);
    free(lower);
    free(upper);
    free(hull);

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[][] OuterTrees(int[][] trees) {
        if (trees.Length <= 1) return trees;
        
        var points = new List<Point>(trees.Length);
        foreach (var t in trees) points.Add(new Point(t[0], t[1]));
        points.Sort((a, b) => a.x == b.x ? a.y.CompareTo(b.y) : a.x.CompareTo(b.x));
        
        List<Point> lower = new List<Point>();
        foreach (var p in points) {
            while (lower.Count >= 2 && Cross(lower[lower.Count - 2], lower[lower.Count - 1], p) < 0)
                lower.RemoveAt(lower.Count - 1);
            lower.Add(p);
        }
        
        List<Point> upper = new List<Point>();
        for (int i = points.Count - 1; i >= 0; i--) {
            var p = points[i];
            while (upper.Count >= 2 && Cross(upper[upper.Count - 2], upper[upper.Count - 1], p) < 0)
                upper.RemoveAt(upper.Count - 1);
            upper.Add(p);
        }
        
        var seen = new HashSet<(int, int)>();
        var hull = new List<Point>();
        foreach (var p in lower) {
            if (seen.Add((p.x, p.y))) hull.Add(p);
        }
        foreach (var p in upper) {
            if (seen.Add((p.x, p.y))) hull.Add(p);
        }
        
        return hull.Select(p => new int[] { p.x, p.y }).ToArray();
    }
    
    private long Cross(Point a, Point b, Point c) {
        // (b - a) x (c - a)
        return ((long)(b.x - a.x)) * (c.y - a.y) - ((long)(b.y - a.y)) * (c.x - a.x);
    }
    
    private struct Point {
        public int x;
        public int y;
        public Point(int x, int y) { this.x = x; this.y = y; }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} trees
 * @return {number[][]}
 */
var outerTrees = function(trees) {
    if (trees.length <= 2) return trees.slice();
    
    const points = trees.map(p => ({x: p[0], y: p[1]}));
    points.sort((a, b) => a.x === b.x ? a.y - b.y : a.x - b.x);
    
    const cross = (o, a, b) => (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
    
    const lower = [];
    for (const p of points) {
        while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], p) < 0) {
            lower.pop();
        }
        lower.push(p);
    }
    
    const upper = [];
    for (let i = points.length - 1; i >= 0; --i) {
        const p = points[i];
        while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], p) < 0) {
            upper.pop();
        }
        upper.push(p);
    }
    
    // Combine lower and upper hulls, avoiding duplicate endpoints
    const hull = [];
    for (let i = 0; i < lower.length; ++i) hull.push(lower[i]);
    for (let i = 1; i < upper.length - 1; ++i) hull.push(upper[i]);
    
    // Remove possible duplicates while preserving any order
    const seen = new Set();
    const result = [];
    for (const p of hull) {
        const key = p.x + ',' + p.y;
        if (!seen.has(key)) {
            seen.add(key);
            result.push([p.x, p.y]);
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function outerTrees(trees: number[][]): number[][] {
    if (trees.length <= 1) return trees.slice();

    const points = trees.slice().sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);

    const cross = (o: number[], a: number[], b: number[]): number => {
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    };

    const lower: number[][] = [];
    for (const p of points) {
        while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], p) < 0) {
            lower.pop();
        }
        lower.push(p);
    }

    const upper: number[][] = [];
    for (let i = points.length - 1; i >= 0; --i) {
        const p = points[i];
        while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], p) < 0) {
            upper.pop();
        }
        upper.push(p);
    }

    // Combine lower and upper hulls, removing duplicate end points
    const combined = lower.concat(upper.slice(1, -1));

    const seen = new Set<string>();
    const result: number[][] = [];
    for (const p of combined) {
        const key = `${p[0]},${p[1]}`;
        if (!seen.has(key)) {
            seen.add(key);
            result.push(p);
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $trees
     * @return Integer[][]
     */
    function outerTrees($trees) {
        $n = count($trees);
        if ($n <= 2) {
            return $trees;
        }

        usort($trees, function($p1, $p2) {
            if ($p1[0] == $p2[0]) {
                return $p1[1] <=> $p2[1];
            }
            return $p1[0] <=> $p2[0];
        });

        $lower = [];
        foreach ($trees as $p) {
            while (count($lower) >= 2 && $this->cross(
                $lower[count($lower)-2],
                $lower[count($lower)-1],
                $p
            ) < 0) {
                array_pop($lower);
            }
            $lower[] = $p;
        }

        $upper = [];
        for ($i = $n - 1; $i >= 0; --$i) {
            $p = $trees[$i];
            while (count($upper) >= 2 && $this->cross(
                $upper[count($upper)-2],
                $upper[count($upper)-1],
                $p
            ) < 0) {
                array_pop($upper);
            }
            $upper[] = $p;
        }

        // Remove duplicate end points
        array_pop($lower);
        array_pop($upper);

        $combined = array_merge($lower, $upper);

        // Deduplicate (in case of collinear all points)
        $unique = [];
        foreach ($combined as $pt) {
            $key = $pt[0] . ',' . $pt[1];
            $unique[$key] = $pt;
        }

        return array_values($unique);
    }

    private function cross($o, $a, $b) {
        return ($a[0] - $o[0]) * ($b[1] - $o[1]) - ($a[1] - $o[1]) * ($b[0] - $o[0]);
    }
}
```

## Swift

```swift
struct Point: Hashable {
    let x: Int
    let y: Int
}

class Solution {
    func outerTrees(_ trees: [[Int]]) -> [[Int]] {
        if trees.count <= 1 { return trees }
        
        var points = trees.map { Point(x: $0[0], y: $0[1]) }
        points.sort {
            if $0.x == $1.x { return $0.y < $1.y }
            return $0.x < $1.x
        }
        
        func cross(_ o: Point, _ a: Point, _ b: Point) -> Int {
            return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
        }
        
        var lower = [Point]()
        for p in points {
            while lower.count >= 2 && cross(lower[lower.count - 2], lower[lower.count - 1], p) < 0 {
                lower.removeLast()
            }
            lower.append(p)
        }
        
        var upper = [Point]()
        for p in points.reversed() {
            while upper.count >= 2 && cross(upper[upper.count - 2], upper[upper.count - 1], p) < 0 {
                upper.removeLast()
            }
            upper.append(p)
        }
        
        var hull = lower
        if upper.count > 0 {
            hull.append(contentsOf: upper.dropFirst().dropLast())
        }
        
        let uniquePoints = Set(hull)
        return uniquePoints.map { [$0.x, $0.y] }
    }
}
```

## Kotlin

```kotlin
class Solution {
    data class Point(val x: Int, val y: Int)

    private fun cross(o: Point, a: Point, b: Point): Long {
        return (a.x - o.x).toLong() * (b.y - o.y) - (a.y - o.y).toLong() * (b.x - o.x)
    }

    fun outerTrees(trees: Array<IntArray>): Array<IntArray> {
        if (trees.size <= 1) return trees
        val points = trees.map { Point(it[0], it[1]) }
            .sortedWith(compareBy<Point> { it.x }.thenBy { it.y })

        val lower = mutableListOf<Point>()
        for (p in points) {
            while (lower.size >= 2 && cross(lower[lower.size - 2], lower[lower.size - 1], p) < 0) {
                lower.removeAt(lower.size - 1)
            }
            lower.add(p)
        }

        val upper = mutableListOf<Point>()
        for (i in points.indices.reversed()) {
            val p = points[i]
            while (upper.size >= 2 && cross(upper[upper.size - 2], upper[upper.size - 1], p) < 0) {
                upper.removeAt(upper.size - 1)
            }
            upper.add(p)
        }

        val hullSet = linkedSetOf<Point>()
        hullSet.addAll(lower)
        hullSet.addAll(upper)

        val result = Array(hullSet.size) { IntArray(2) }
        var idx = 0
        for (pt in hullSet) {
            result[idx][0] = pt.x
            result[idx][1] = pt.y
            idx++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> outerTrees(List<List<int>> trees) {
    if (trees.length <= 1) return List.from(trees);
    // Sort points lexicographically.
    trees.sort((a, b) {
      if (a[0] == b[0]) return a[1].compareTo(b[1]);
      return a[0].compareTo(b[0]);
    });

    List<List<int>> lower = [];
    for (var p in trees) {
      while (lower.length >= 2 &&
          _cross(lower[lower.length - 2], lower[lower.length - 1], p) < 0) {
        lower.removeLast();
      }
      lower.add(p);
    }

    List<List<int>> upper = [];
    for (int i = trees.length - 1; i >= 0; i--) {
      var p = trees[i];
      while (upper.length >= 2 &&
          _cross(upper[upper.length - 2], upper[upper.length - 1], p) < 0) {
        upper.removeLast();
      }
      upper.add(p);
    }

    // Combine lower and upper hulls, removing duplicates.
    Set<String> seen = {};
    List<List<int>> result = [];

    for (var pt in lower) {
      var key = '${pt[0]},${pt[1]}';
      if (!seen.contains(key)) {
        seen.add(key);
        result.add(pt);
      }
    }
    for (var pt in upper) {
      var key = '${pt[0]},${pt[1]}';
      if (!seen.contains(key)) {
        seen.add(key);
        result.add(pt);
      }
    }

    return result;
  }

  int _cross(List<int> o, List<int> a, List<int> b) {
    return (a[0] - o[0]) * (b[1] - o[1]) -
        (a[1] - o[1]) * (b[0] - o[0]);
  }
}
```

## Golang

```go
import "sort"

func outerTrees(trees [][]int) [][]int {
	n := len(trees)
	if n <= 1 {
		return trees
	}
	sort.Slice(trees, func(i, j int) bool {
		if trees[i][0] == trees[j][0] {
			return trees[i][1] < trees[j][1]
		}
		return trees[i][0] < trees[j][0]
	})

	cross := func(o, a, b []int) int {
		return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
	}

	lower := [][]int{}
	for _, p := range trees {
		for len(lower) >= 2 && cross(lower[len(lower)-2], lower[len(lower)-1], p) < 0 {
			lower = lower[:len(lower)-1]
		}
		lower = append(lower, p)
	}

	upper := [][]int{}
	for i := n - 1; i >= 0; i-- {
		p := trees[i]
		for len(upper) >= 2 && cross(upper[len(upper)-2], upper[len(upper)-1], p) < 0 {
			upper = upper[:len(upper)-1]
		}
		upper = append(upper, p)
	}

	hull := [][]int{}
	hull = append(hull, lower...)
	for i := 1; i < len(upper)-1; i++ {
		hull = append(hull, upper[i])
	}

	seen := make(map[[2]int]bool)
	res := [][]int{}
	for _, p := range hull {
		key := [2]int{p[0], p[1]}
		if !seen[key] {
			seen[key] = true
			res = append(res, []int{p[0], p[1]})
		}
	}
	return res
}
```

## Ruby

```ruby
def outer_trees(trees)
  return trees if trees.size <= 1

  pts = trees.sort_by { |x, y| [x, y] }

  cross = ->(o, a, b) {
    (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
  }

  lower = []
  pts.each do |p|
    while lower.size >= 2 && cross.call(lower[-2], lower[-1], p) < 0
      lower.pop
    end
    lower << p
  end

  upper = []
  pts.reverse_each do |p|
    while upper.size >= 2 && cross.call(upper[-2], upper[-1], p) < 0
      upper.pop
    end
    upper << p
  end

  hull_points = {}
  (lower + upper).each { |pt| hull_points[pt] = true }
  hull_points.keys
end
```

## Scala

```scala
object Solution {
  def outerTrees(trees: Array[Array[Int]]): Array[Array[Int]] = {
    import scala.collection.mutable.{ArrayBuffer, LinkedHashSet}
    case class Pt(x: Int, y: Int)

    val pts = trees.map(arr => Pt(arr(0), arr(1)))
    if (pts.length <= 1) return trees

    def cross(o: Pt, a: Pt, b: Pt): Long =
      (a.x - o.x).toLong * (b.y - o.y) - (a.y - o.y).toLong * (b.x - o.x)

    val sorted = pts.sortBy(p => (p.x, p.y))

    val lower = ArrayBuffer[Pt]()
    for (p <- sorted) {
      while (lower.size >= 2 && cross(lower(lower.size - 2), lower(lower.size - 1), p) < 0)
        lower.remove(lower.size - 1)
      lower.append(p)
    }

    val upper = ArrayBuffer[Pt]()
    for (p <- sorted.reverse) {
      while (upper.size >= 2 && cross(upper(upper.size - 2), upper(upper.size - 1), p) < 0)
        upper.remove(upper.size - 1)
      upper.append(p)
    }

    val hullSet = LinkedHashSet[(Int, Int)]()
    lower.foreach(p => hullSet.add((p.x, p.y)))
    upper.foreach(p => hullSet.add((p.x, p.y)))

    hullSet.map { case (x, y) => Array(x, y) }.toArray
  }
}
```

## Rust

```rust
use std::collections::HashSet;

#[derive(Clone, Copy)]
struct Point {
    x: i32,
    y: i32,
}

fn cross(o: &Point, a: &Point, b: &Point) -> i64 {
    let ax = (a.x - o.x) as i64;
    let ay = (a.y - o.y) as i64;
    let bx = (b.x - o.x) as i64;
    let by = (b.y - o.y) as i64;
    ax * by - ay * bx
}

impl Solution {
    pub fn outer_trees(trees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if trees.len() <= 1 {
            return trees;
        }

        // Convert to points and sort
        let mut pts: Vec<Point> = trees.iter()
            .map(|v| Point { x: v[0], y: v[1] })
            .collect();
        pts.sort_by(|a, b| {
            if a.x == b.x {
                a.y.cmp(&b.y)
            } else {
                a.x.cmp(&b.x)
            }
        });

        // Build lower hull
        let mut lower: Vec<Point> = Vec::new();
        for &p in &pts {
            while lower.len() >= 2 && cross(&lower[lower.len() - 2], &lower[lower.len() - 1], &p) < 0 {
                lower.pop();
            }
            lower.push(p);
        }

        // Build upper hull
        let mut upper: Vec<Point> = Vec::new();
        for &p in pts.iter().rev() {
            while upper.len() >= 2 && cross(&upper[upper.len() - 2], &upper[upper.len() - 1], &p) < 0 {
                upper.pop();
            }
            upper.push(p);
        }

        // Remove duplicate end points
        lower.pop();
        upper.pop();

        // Concatenate hull points
        let mut hull = lower;
        hull.extend(upper);

        // Deduplicate (in case of collinear all points)
        let mut seen: HashSet<(i32, i32)> = HashSet::new();
        let mut result: Vec<Vec<i32>> = Vec::new();
        for p in hull {
            if seen.insert((p.x, p.y)) {
                result.push(vec![p.x, p.y]);
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (outer-trees trees)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ([sorted
          (sort trees
                (lambda (a b)
                  (or (< (car a) (car b))
                      (and (= (car a) (car b))
                           (< (cadr a) (cadr b))))))]

         ;; cross product (o->a) x (o->b)
         [cross
          (lambda (o a b)
            (let* ([ox (car o)] [oy (cadr o)]
                   [ax (car a)] [ay (cadr a)]
                   [bx (car b)] [by (cadr b)])
              (- (* (- ax ox) (- by oy))
                 (* (- ay oy) (- bx ox)))))]

         ;; build hull with condition pop when turn is right (cross < 0)
         [build-hull
          (lambda (pts)
            (let loop ((h '()) (rem pts))
              (if (null? rem)
                  (reverse h)
                  (let* ([p (car rem)]
                         [new-h
                          (let recur ((hh h))
                            (if (or (< (length hh) 2)
                                    (>= (cross (list-ref hh (- (length hh) 2))
                                               (list-ref hh (- (length hh) 1))
                                               p)
                                        0))
                                (cons p hh)
                                (recur (cdr hh))))])
                    (loop new-h (cdr rem))))))]

         [lower (build-hull sorted)]
         [upper (build-hull (reverse sorted))]
         [hset (make-hash)])

    ;; insert all hull points into hash set to deduplicate
    (for ([p lower]) (hash-set! hset p #t))
    (for ([p upper]) (hash-set! hset p #t))

    (hash-keys hset)))
```

## Erlang

```erlang
-spec outer_trees(Trees :: [[integer()]]) -> [[integer()]].
outer_trees(Trees) ->
    Sorted = lists:sort(fun([X1, Y1], [X2, Y2]) ->
        case X1 < X2 of
            true -> true;
            false when X1 > X2 -> false;
            _ -> Y1 =< Y2
        end
    end, Trees),
    Lower = build_hull([], Sorted),
    Upper = build_hull([], lists:reverse(Sorted)),
    %% concatenate lower and upper without duplicate endpoints
    Combined = case Upper of
        [] -> Lower;
        [_] -> Lower;
        _ ->
            TrimmedUpper = lists:sublist(Upper, 2, length(Upper) - 2),
            Lower ++ TrimmedUpper
    end,
    lists:usort(Combined).

%% Build hull (monotone chain) keeping collinear points.
build_hull(Stack, []) ->
    lists:reverse(Stack);
build_hull([], [P | Rest]) ->
    build_hull([P], Rest);
build_hull([_]=Stack, [P | Rest]) ->
    build_hull([P | Stack], Rest);
build_hull([B, A | Tail] = Stack, [P | Rest]) when cross(A, B, P) < 0 ->
    %% right turn: remove B and reprocess P
    build_hull([A | Tail], [P | Rest]);
build_hull(Stack, [P | Rest]) ->
    build_hull([P | Stack], Rest).

%% Cross product (O,A,B)
cross([Ox, Oy], [Ax, Ay], [Bx, By]) ->
    (Ax - Ox) * (By - Oy) - (Ay - Oy) * (Bx - Ox).
```

## Elixir

```elixir
defmodule Solution do
  @spec outer_trees(trees :: [[integer]]) :: [[integer]]
  def outer_trees(trees) do
    sorted = Enum.sort_by(trees, fn [x, y] -> {x, y} end)

    lower_rev = Enum.reduce(sorted, [], fn p, acc -> push(acc, p) end)
    lower = Enum.reverse(lower_rev)

    upper_rev = Enum.reduce(Enum.reverse(sorted), [], fn p, acc -> push(acc, p) end)
    upper = Enum.reverse(upper_rev)

    hull =
      case upper do
        [] -> lower
        [_] -> lower ++ upper
        _ -> lower ++ Enum.slice(upper, 1..-2)
      end

    hull |> MapSet.new() |> MapSet.to_list()
  end

  defp push(stack, p) do
    stack = pop_while(stack, p)
    [p | stack]
  end

  defp pop_while([first, second | rest] = _stack, p) do
    if cross(second, first, p) < 0 do
      pop_while([second | rest], p)
    else
      _stack
    end
  end

  defp pop_while(stack, _p), do: stack

  defp cross([x1, y1], [x2, y2], [x3, y3]) do
    (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
  end
end
```

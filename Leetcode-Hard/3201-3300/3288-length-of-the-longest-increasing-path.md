# 3288. Length of the Longest Increasing Path

## Cpp

```cpp
class Solution {
public:
    int maxPathLength(std::vector<std::vector<int>>& coordinates, int k) {
        using pii = std::pair<int,int>;
        int tx = coordinates[k][0];
        int ty = coordinates[k][1];
        std::vector<pii> left, right;
        left.reserve(coordinates.size());
        right.reserve(coordinates.size());
        for (int i = 0; i < (int)coordinates.size(); ++i) {
            if (i == k) continue;
            int x = coordinates[i][0];
            int y = coordinates[i][1];
            if (x < tx && y < ty) left.emplace_back(x, y);
            else if (x > tx && y > ty) right.emplace_back(x, y);
        }
        auto lis = [&](std::vector<pii>& pts)->int{
            std::sort(pts.begin(), pts.end(),
                      [](const pii& a, const pii& b){
                          if (a.first != b.first) return a.first < b.first;
                          return a.second > b.second; // descending y for equal x
                      });
            std::vector<int> dp;
            dp.reserve(pts.size());
            for (auto &p : pts) {
                int y = p.second;
                auto it = std::lower_bound(dp.begin(), dp.end(), y);
                if (it == dp.end()) dp.push_back(y);
                else *it = y;
            }
            return (int)dp.size();
        };
        int leftLen = lis(left);
        int rightLen = lis(right);
        return leftLen + 1 + rightLen;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxPathLength(int[][] coordinates, int k) {
        int tx = coordinates[k][0];
        int ty = coordinates[k][1];
        List<int[]> left = new ArrayList<>();
        List<int[]> right = new ArrayList<>();

        for (int i = 0; i < coordinates.length; i++) {
            if (i == k) continue;
            int x = coordinates[i][0];
            int y = coordinates[i][1];
            if (x < tx && y < ty) {
                left.add(new int[]{x, y});
            } else if (x > tx && y > ty) {
                right.add(new int[]{x, y});
            }
        }

        int leftLen = lisLength(left);
        int rightLen = lisLength(right);
        return leftLen + 1 + rightLen;
    }

    private int lisLength(List<int[]> points) {
        points.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]); // y descending for equal x
        });

        int[] tails = new int[points.size()];
        int size = 0;
        for (int[] p : points) {
            int y = p[1];
            int l = 0, r = size;
            while (l < r) {
                int m = (l + r) >>> 1;
                if (tails[m] >= y) r = m;
                else l = m + 1;
            }
            tails[l] = y;
            if (l == size) size++;
        }
        return size;
    }
}
```

## Python

```python
class Solution(object):
    def maxPathLength(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect

        def lis(vals):
            dp = []
            for v in vals:
                i = bisect.bisect_left(dp, v)
                if i == len(dp):
                    dp.append(v)
                else:
                    dp[i] = v
            return len(dp)

        pkx, pky = coordinates[k]

        left = []
        right = []

        for i, (x, y) in enumerate(coordinates):
            if i == k:
                continue
            if x < pkx and y < pky:
                left.append((x, y))
            elif x > pkx and y > pky:
                right.append((x, y))

        # sort by x asc, y desc for LIS on y
        left.sort(key=lambda p: (p[0], -p[1]))
        right.sort(key=lambda p: (p[0], -p[1]))

        left_len = lis([y for _, y in left])
        right_len = lis([y for _, y in right])

        return 1 + left_len + right_len
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        tx, ty = coordinates[k]
        left_pts = []
        right_pts = []
        for x, y in coordinates:
            if x < tx and y < ty:
                left_pts.append((x, y))
            elif x > tx and y > ty:
                right_pts.append((x, y))

        def lis(points: List[tuple]) -> int:
            points.sort(key=lambda p: (p[0], -p[1]))
            dp = []
            for _, y in points:
                i = bisect.bisect_left(dp, y)
                if i == len(dp):
                    dp.append(y)
                else:
                    dp[i] = y
            return len(dp)

        left_len = lis(left_pts)
        right_len = lis(right_pts)
        return left_len + 1 + right_len
```

## C

```c
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Point;

static int cmpPoint(const void *a, const void *b) {
    const Point *pa = (const Point *)a;
    const Point *pb = (const Point *)b;
    if (pa->x != pb->x) return pa->x - pb->x;          // ascending x
    return pb->y - pa->y;                              // descending y for equal x
}

static int lis(int *arr, int n) {
    if (n == 0) return 0;
    int *tails = (int *)malloc(sizeof(int) * n);
    int len = 0;
    for (int i = 0; i < n; ++i) {
        int x = arr[i];
        int l = 0, r = len;
        while (l < r) {
            int m = (l + r) >> 1;
            if (tails[m] < x)
                l = m + 1;
            else
                r = m;
        }
        tails[l] = x;
        if (l == len) ++len;
    }
    free(tails);
    return len;
}

int maxPathLength(int** coordinates, int coordinatesSize, int* coordinatesColSize, int k) {
    int xk = coordinates[k][0];
    int yk = coordinates[k][1];

    Point *left = (Point *)malloc(sizeof(Point) * coordinatesSize);
    Point *right = (Point *)malloc(sizeof(Point) * coordinatesSize);
    int lcnt = 0, rcnt = 0;

    for (int i = 0; i < coordinatesSize; ++i) {
        if (i == k) continue;
        int x = coordinates[i][0];
        int y = coordinates[i][1];
        if (x < xk && y < yk) {
            left[lcnt].x = x;
            left[lcnt].y = y;
            ++lcnt;
        } else if (x > xk && y > yk) {
            right[rcnt].x = x;
            right[rcnt].y = y;
            ++rcnt;
        }
    }

    qsort(left, lcnt, sizeof(Point), cmpPoint);
    qsort(right, rcnt, sizeof(Point), cmpPoint);

    int *leftY = (int *)malloc(sizeof(int) * lcnt);
    for (int i = 0; i < lcnt; ++i) leftY[i] = left[i].y;
    int *rightY = (int *)malloc(sizeof(int) * rcnt);
    for (int i = 0; i < rcnt; ++i) rightY[i] = right[i].y;

    int leftLen = lis(leftY, lcnt);
    int rightLen = lis(rightY, rcnt);

    free(left);
    free(right);
    free(leftY);
    free(rightY);

    return leftLen + 1 + rightLen;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxPathLength(int[][] coordinates, int k) {
        int n = coordinates.Length;
        int tx = coordinates[k][0];
        int ty = coordinates[k][1];

        // Left side: points strictly smaller in both dimensions
        var leftList = new List<(int x, int y)>();
        // Right side: points strictly larger in both dimensions
        var rightList = new List<(int x, int y)>();

        for (int i = 0; i < n; i++) {
            if (i == k) continue;
            int x = coordinates[i][0];
            int y = coordinates[i][1];
            if (x < tx && y < ty) leftList.Add((x, y));
            else if (x > tx && y > ty) rightList.Add((x, y));
        }

        // Helper to compute LIS length on y after sorting by x asc, y desc
        int LisLength(List<(int x, int y)> points) {
            points.Sort((a, b) => {
                if (a.x != b.x) return a.x.CompareTo(b.x);
                // for equal x, sort y descending to avoid using same x twice
                return b.y.CompareTo(a.y);
            });

            var tails = new List<int>();
            foreach (var p in points) {
                int y = p.y;
                int idx = tails.BinarySearch(y);
                if (idx < 0) idx = ~idx; // lower_bound: first >= y
                if (idx == tails.Count) tails.Add(y);
                else tails[idx] = y;
            }
            return tails.Count;
        }

        int leftLen = LisLength(leftList);
        int rightLen = LisLength(rightList);

        return leftLen + 1 + rightLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} coordinates
 * @param {number} k
 * @return {number}
 */
var maxPathLength = function(coordinates, k) {
    const n = coordinates.length;
    const points = new Array(n);
    const ys = [];
    for (let i = 0; i < n; ++i) {
        const [x, y] = coordinates[i];
        points[i] = { x, y, idx: i };
        ys.push(y);
    }
    // compress y
    ys.sort((a, b) => a - b);
    const uniqY = [...new Set(ys)];
    const m = uniqY.length;
    const yToIdx = new Map();
    for (let i = 0; i < m; ++i) {
        yToIdx.set(uniqY[i], i + 1); // 1‑based
    }

    class BIT {
        constructor(size) {
            this.n = size;
            this.tree = new Int32Array(size + 2);
        }
        update(i, val) {
            const n = this.n;
            while (i <= n) {
                if (val > this.tree[i]) this.tree[i] = val;
                i += i & -i;
            }
        }
        query(i) {
            let res = 0;
            while (i > 0) {
                if (this.tree[i] > res) res = this.tree[i];
                i -= i & -i;
            }
            return res;
        }
    }

    const leftLen = new Int32Array(n);
    // sort by x asc, y desc
    points.sort((a, b) => {
        if (a.x !== b.x) return a.x - b.x;
        return b.y - a.y;
    });
    let bit = new BIT(m);
    for (const p of points) {
        const idx = yToIdx.get(p.y);
        const best = bit.query(idx - 1);
        const cur = best + 1;
        leftLen[p.idx] = cur;
        bit.update(idx, cur);
    }

    const rightLen = new Int32Array(n);
    // sort by x desc, y asc
    points.sort((a, b) => {
        if (a.x !== b.x) return b.x - a.x;
        return a.y - b.y;
    });
    bit = new BIT(m);
    for (const p of points) {
        const idx = yToIdx.get(p.y);
        const revIdx = m - idx + 1; // rank in descending order
        const best = bit.query(revIdx - 1); // larger original y have smaller revIdx
        const cur = best + 1;
        rightLen[p.idx] = cur;
        bit.update(revIdx, cur);
    }

    return leftLen[k] + rightLen[k] - 1;
};
```

## Typescript

```typescript
function maxPathLength(coordinates: number[][], k: number): number {
    const [tx, ty] = coordinates[k];

    const left: number[][] = [];
    const right: number[][] = [];

    for (let i = 0; i < coordinates.length; ++i) {
        if (i === k) continue;
        const [x, y] = coordinates[i];
        if (x < tx && y < ty) left.push([x, y]);
        else if (x > tx && y > ty) right.push([x, y]);
    }

    const lisLength = (points: number[][]): number => {
        points.sort((a, b) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            // same x -> descending y to avoid using both
            return b[1] - a[1];
        });
        const dp: number[] = [];
        for (const [, y] of points) {
            let l = 0, r = dp.length;
            while (l < r) {
                const m = (l + r) >> 1;
                if (dp[m] < y) l = m + 1;
                else r = m;
            }
            if (l === dp.length) dp.push(y);
            else dp[l] = y;
        }
        return dp.length;
    };

    const leftLen = lisLength(left);
    const rightLen = lisLength(right);

    return leftLen + 1 + rightLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $coordinates
     * @param Integer $k
     * @return Integer
     */
    function maxPathLength($coordinates, $k) {
        $tx = $coordinates[$k][0];
        $ty = $coordinates[$k][1];

        $lower = [];
        $higher = [];

        foreach ($coordinates as $i => $pt) {
            if ($i == $k) continue;
            $x = $pt[0];
            $y = $pt[1];
            if ($x < $tx && $y < $ty) {
                $lower[] = [$x, $y];
            } elseif ($x > $tx && $y > $ty) {
                $higher[] = [$x, $y];
            }
        }

        $left  = $this->lisLength($lower);
        $right = $this->lisLength($higher);

        return $left + 1 + $right;
    }

    private function lisLength($points) {
        if (empty($points)) return 0;

        usort($points, function ($a, $b) {
            if ($a[0] == $b[0]) {
                // y descending for equal x
                return $b[1] <=> $a[1];
            }
            return $a[0] <=> $b[0];
        });

        $tails = [];
        foreach ($points as $pt) {
            $y = $pt[1];
            $l = 0;
            $r = count($tails);
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($tails[$mid] < $y) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }
            if ($l == count($tails)) {
                $tails[] = $y;
            } else {
                $tails[$l] = $y;
            }
        }

        return count($tails);
    }
}
```

## Swift

```swift
class Solution {
    func maxPathLength(_ coordinates: [[Int]], _ k: Int) -> Int {
        let target = coordinates[k]
        let tx = target[0]
        let ty = target[1]
        
        var smaller = [(x: Int, y: Int)]()
        var larger = [(x: Int, y: Int)]()
        
        for i in 0..<coordinates.count where i != k {
            let x = coordinates[i][0]
            let y = coordinates[i][1]
            if x < tx && y < ty {
                smaller.append((x, y))
            } else if x > tx && y > ty {
                larger.append((x, y))
            }
        }
        
        func sortAndExtractY(_ points: inout [(x: Int, y: Int)]) -> [Int] {
            points.sort {
                if $0.x != $1.x { return $0.x < $1.x }
                return $0.y > $1.y   // descending y for equal x
            }
            return points.map { $0.y }
        }
        
        func lisLength(_ arr: [Int]) -> Int {
            var tails = [Int]()
            for v in arr {
                var l = 0, r = tails.count
                while l < r {
                    let m = (l + r) >> 1
                    if tails[m] < v {
                        l = m + 1
                    } else {
                        r = m
                    }
                }
                if l == tails.count {
                    tails.append(v)
                } else {
                    tails[l] = v
                }
            }
            return tails.count
        }
        
        let leftY = sortAndExtractY(&smaller)
        let rightY = sortAndExtractY(&larger)
        
        let leftLen = lisLength(leftY)
        let rightLen = lisLength(rightY)
        
        return leftLen + 1 + rightLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPathLength(coordinates: Array<IntArray>, k: Int): Int {
        val target = coordinates[k]
        val tx = target[0]
        val ty = target[1]

        val left = mutableListOf<Pair<Int, Int>>()
        val right = mutableListOf<Pair<Int, Int>>()

        for (i in coordinates.indices) {
            if (i == k) continue
            val x = coordinates[i][0]
            val y = coordinates[i][1]
            if (x < tx && y < ty) {
                left.add(Pair(x, y))
            } else if (x > tx && y > ty) {
                right.add(Pair(x, y))
            }
        }

        fun lis(points: List<Pair<Int, Int>>): Int {
            if (points.isEmpty()) return 0
            val sorted = points.sortedWith(
                compareBy<Pair<Int, Int>> { it.first }.thenByDescending { it.second }
            )
            val dp = mutableListOf<Int>()
            for ((_, y) in sorted) {
                var l = 0
                var r = dp.size
                while (l < r) {
                    val m = (l + r) ushr 1
                    if (dp[m] < y) {
                        l = m + 1
                    } else {
                        r = m
                    }
                }
                if (l == dp.size) dp.add(y) else dp[l] = y
            }
            return dp.size
        }

        val leftLen = lis(left)
        val rightLen = lis(right)

        return 1 + leftLen + rightLen
    }
}
```

## Dart

```dart
class Solution {
  int maxPathLength(List<List<int>> coordinates, int k) {
    int px = coordinates[k][0];
    int py = coordinates[k][1];

    // Points strictly smaller in both dimensions
    List<_Point> lower = [];
    for (int i = 0; i < coordinates.length; i++) {
      if (i == k) continue;
      int x = coordinates[i][0];
      int y = coordinates[i][1];
      if (x < px && y < py) lower.add(_Point(x, y));
    }

    // Points strictly larger in both dimensions
    List<_Point> higher = [];
    for (int i = 0; i < coordinates.length; i++) {
      if (i == k) continue;
      int x = coordinates[i][0];
      int y = coordinates[i][1];
      if (x > px && y > py) higher.add(_Point(x, y));
    }

    int bestBefore = _lisLength(lower, limitY: py);
    int bestAfter = _lisLength(higher);

    return bestBefore + 1 + bestAfter;
  }

  // Computes LIS length for points with strict increase in both x and y.
  // If limitY is provided, returns the maximum length of a sequence
  // whose last point has y < limitY (used for the lower side).
  int _lisLength(List<_Point> pts, {int? limitY}) {
    if (pts.isEmpty) return 0;
    // Sort by x asc, then y desc
    pts.sort((a, b) {
      int cmp = a.x.compareTo(b.x);
      if (cmp != 0) return cmp;
      return b.y.compareTo(a.y); // descending y for equal x
    });

    // Coordinate compression of y values
    List<int> ys = pts.map((p) => p.y).toList();
    if (limitY != null) ys.add(limitY);
    ys.sort();
    List<int> uniq = [];
    int prev = -1;
    for (int v in ys) {
      if (uniq.isEmpty || v != prev) {
        uniq.add(v);
        prev = v;
      }
    }
    Map<int, int> yToIdx = {};
    for (int i = 0; i < uniq.length; i++) {
      yToIdx[uniq[i]] = i + 1; // 1‑based index for BIT
    }

    Fenwick bit = Fenwick(uniq.length);
    int overallMax = 0;

    for (var p in pts) {
      int idx = yToIdx[p.y]!;
      int bestPrev = bit.query(idx - 1);
      int cur = bestPrev + 1;
      bit.update(idx, cur);
      if (cur > overallMax) overallMax = cur;
    }

    if (limitY != null) {
      int limitIdx = yToIdx[limitY]!;
      return bit.query(limitIdx - 1);
    }
    return overallMax;
  }
}

class _Point {
  final int x;
  final int y;
  _Point(this.x, this.y);
}

class Fenwick {
  final List<int> _tree;
  Fenwick(int n) : _tree = List.filled(n + 2, 0);

  void update(int i, int val) {
    for (int idx = i; idx < _tree.length; idx += idx & -idx) {
      if (val > _tree[idx]) _tree[idx] = val;
    }
  }

  int query(int i) {
    int res = 0;
    for (int idx = i; idx > 0; idx -= idx & -idx) {
      if (_tree[idx] > res) res = _tree[idx];
    }
    return res;
  }
}
```

## Golang

```go
import "sort"

func maxPathLength(coordinates [][]int, k int) int {
	xk, yk := coordinates[k][0], coordinates[k][1]

	left := make([][2]int, 0)
	right := make([][2]int, 0)

	for i, p := range coordinates {
		if i == k {
			continue
		}
		x, y := p[0], p[1]
		if x < xk && y < yk {
			left = append(left, [2]int{x, y})
		} else if x > xk && y > yk {
			right = append(right, [2]int{x, y})
		}
	}

	sort.Slice(left, func(i, j int) bool {
		if left[i][0] == left[j][0] {
			return left[i][1] > left[j][1]
		}
		return left[i][0] < left[j][0]
	})
	sort.Slice(right, func(i, j int) bool {
		if right[i][0] == right[j][0] {
			return right[i][1] > right[j][1]
		}
		return right[i][0] < right[j][0]
	})

	leftLen := lisLength(left)
	rightLen := lisLength(right)

	return leftLen + 1 + rightLen
}

func lisLength(points [][2]int) int {
	dp := make([]int, 0)
	for _, p := range points {
		y := p[1]
		idx := sort.Search(len(dp), func(i int) bool { return dp[i] >= y })
		if idx == len(dp) {
			dp = append(dp, y)
		} else {
			dp[idx] = y
		}
	}
	return len(dp)
}
```

## Ruby

```ruby
def max_path_length(coordinates, k)
  tx, ty = coordinates[k]

  left = []
  right = []

  coordinates.each_with_index do |(x, y), idx|
    next if idx == k
    if x < tx && y < ty
      left << [x, y]
    elsif x > tx && y > ty
      right << [x, y]
    end
  end

  lis = lambda do |points|
    sorted = points.sort_by { |p| [p[0], -p[1]] }
    tails = []
    sorted.each do |_, y|
      idx = tails.bsearch_index { |v| v >= y }
      if idx.nil?
        tails << y
      else
        tails[idx] = y
      end
    end
    tails.size
  end

  left_len = lis.call(left)
  right_len = lis.call(right)

  1 + left_len + right_len
end
```

## Scala

```scala
object Solution {
  class BIT(val size: Int) {
    private val tree = Array.fill(size + 2)(0)
    def update(i: Int, v: Int): Unit = {
      var idx = i
      while (idx <= size) {
        if (v > tree(idx)) tree(idx) = v
        idx += idx & -idx
      }
    }
    def query(i: Int): Int = {
      var idx = i
      var res = 0
      while (idx > 0) {
        if (tree(idx) > res) res = tree(idx)
        idx -= idx & -idx
      }
      res
    }
  }

  def maxPathLength(coordinates: Array[Array[Int]], k: Int): Int = {
    val n = coordinates.length
    val xs = new Array[Int](n)
    val ys = new Array[Int](n)
    var i = 0
    while (i < n) {
      xs(i) = coordinates(i)(0)
      ys(i) = coordinates(i)(1)
      i += 1
    }

    // compress y values
    val sortedY = ys.distinct.sorted
    val yToIdx = scala.collection.mutable.HashMap[Int, Int]()
    var idx = 1
    for (v <- sortedY) {
      yToIdx(v) = idx
      idx += 1
    }
    val m = sortedY.length

    case class Pt(x: Int, y: Int, idx: Int, yIdx: Int)
    val pts = new Array[Pt](n)
    i = 0
    while (i < n) {
      pts(i) = Pt(xs(i), ys(i), i, yToIdx(ys(i)))
      i += 1
    }

    // forward DP (points with smaller x and y)
    val forward = new Array[Int](n)
    val bitF = new BIT(m)
    val sortedF = pts.sortWith { (a, b) =>
      if (a.x != b.x) a.x < b.x else a.y > b.y
    }
    i = 0
    while (i < n) {
      var j = i
      while (j < n && sortedF(j).x == sortedF(i).x) j += 1
      var t = i
      while (t < j) {
        val p = sortedF(t)
        val best = if (p.yIdx > 1) bitF.query(p.yIdx - 1) else 0
        forward(p.idx) = best + 1
        t += 1
      }
      t = i
      while (t < j) {
        val p = sortedF(t)
        bitF.update(p.yIdx, forward(p.idx))
        t += 1
      }
      i = j
    }

    // backward DP (points with larger x and y)
    val backward = new Array[Int](n)
    val bitB = new BIT(m)
    val sortedB = pts.sortWith { (a, b) =>
      if (a.x != b.x) a.x > b.x else a.y < b.y
    }
    i = 0
    while (i < n) {
      var j = i
      while (j < n && sortedB(j).x == sortedB(i).x) j += 1
      var t = i
      while (t < j) {
        val p = sortedB(t)
        val revIdx = m - p.yIdx + 1
        val best = if (revIdx > 1) bitB.query(revIdx - 1) else 0
        backward(p.idx) = best + 1
        t += 1
      }
      t = i
      while (t < j) {
        val p = sortedB(t)
        val revIdx = m - p.yIdx + 1
        bitB.update(revIdx, backward(p.idx))
        t += 1
      }
      i = j
    }

    forward(k) + backward(k) - 1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_path_length(coordinates: Vec<Vec<i32>>, k: i32) -> i32 {
        let k_idx = k as usize;
        let target = &coordinates[k_idx];
        let tx = target[0];
        let ty = target[1];

        let mut left: Vec<(i32, i32)> = Vec::new();
        let mut right: Vec<(i32, i32)> = Vec::new();

        for (i, pt) in coordinates.iter().enumerate() {
            if i == k_idx {
                continue;
            }
            let x = pt[0];
            let y = pt[1];
            if x < tx && y < ty {
                left.push((x, y));
            } else if x > tx && y > ty {
                right.push((x, y));
            }
        }

        fn lis_len(points: &mut Vec<(i32, i32)>) -> i32 {
            points.sort_by(|a, b| {
                if a.0 != b.0 {
                    a.0.cmp(&b.0)
                } else {
                    b.1.cmp(&a.1) // y descending for equal x
                }
            });
            let mut tails: Vec<i32> = Vec::new();
            for &(_, y) in points.iter() {
                match tails.binary_search(&y) {
                    Ok(pos) => tails[pos] = y,
                    Err(pos) => {
                        if pos == tails.len() {
                            tails.push(y);
                        } else {
                            tails[pos] = y;
                        }
                    }
                }
            }
            tails.len() as i32
        }

        let left_len = lis_len(&mut left);
        let right_len = lis_len(&mut right);

        left_len + 1 + right_len
    }
}
```

## Racket

```racket
(define (lis-length seq)
  (let* ((n (length seq))
         (tails (make-vector n 0))
         (size 0))
    (for ([v seq])
      (let loop ((l 0) (r size))
        (if (= l r)
            (begin
              (vector-set! tails l v)
              (when (= l size) (set! size (+ size 1))))
            (let* ((mid (quotient (+ l r) 2))
                   (mid-val (vector-ref tails mid)))
              (if (< mid-val v)
                  (loop (+ mid 1) r)
                  (loop l mid))))))
    size))

(define/contract (max-path-length coordinates k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?
       exact-integer?)
  (let* ((target (list-ref coordinates k))
         (tx (first target))
         (ty (second target)))
    (define left-points
      (filter (lambda (pt)
                (and (< (first pt) tx) (< (second pt) ty))) coordinates))
    (define right-points
      (filter (lambda (pt)
                (and (> (first pt) tx) (> (second pt) ty))) coordinates))
    (define (sort-points pts)
      (sort pts
            (lambda (a b)
              (let ((ax (first a)) (ay (second a))
                    (bx (first b)) (by (second b)))
                (if (< ax bx) #t
                    (if (> ax bx) #f
                        (> ay by))))))) ; x equal → y descending
    (define left-sorted (sort-points left-points))
    (define right-sorted (sort-points right-points))
    (define left-ys (map second left-sorted))
    (define right-ys (map second right-sorted))
    (+ 1 (lis-length left-ys) (lis-length right-ys))))
```

## Erlang

```erlang
-spec max_path_length(Coordinates :: [[integer()]], K :: integer()) -> integer().
max_path_length(Coordinates, K) ->
    P = lists:nth(K + 1, Coordinates),
    Px = hd(P),
    Py = tl(P) |> hd(),
    Lower = [ {X, Y} || [X, Y] <- Coordinates, X < Px, Y < Py ],
    Upper = [ {X, Y} || [X, Y] <- Coordinates, X > Px, Y > Py ],
    LowerLen = lis_length(Lower),
    UpperLen = lis_length(Upper),
    LowerLen + 1 + UpperLen.

%% Compute LIS length for a list of points using the described sorting and patience algorithm.
-spec lis_length(list({integer(), integer()})) -> integer().
lis_length(PointList) ->
    Sorted = lists:sort(
        fun({X1, Y1}, {X2, Y2}) ->
            if
                X1 < X2 -> true;
                X1 > X2 -> false;
                true -> Y1 > Y2
            end
        end,
        PointList),
    Ys = [Y || {_X, Y} <- Sorted],
    lis_len(Ys).

%% Patience sorting LIS (strictly increasing) on a list of integers.
-spec lis_len([integer()]) -> integer().
lis_len(Ys) ->
    lis_len(Ys, array:new(), 0).

-spec lis_len([integer()], array:array(integer()), non_neg_integer()) -> non_neg_integer().
lis_len([], _Arr, Len) -> Len;
lis_len([Y | Rest], Arr, Len) ->
    case Len of
        0 ->
            NewArr = array:set(1, Y, Arr),
            lis_len(Rest, NewArr, 1);
        _ ->
            Pos = binary_search(Arr, 1, Len, Y),
            if
                Pos > Len ->
                    NewArr = array:set(Len + 1, Y, Arr),
                    lis_len(Rest, NewArr, Len + 1);
                true ->
                    NewArr = array:set(Pos, Y, Arr),
                    lis_len(Rest, NewArr, Len)
            end
    end.

%% Find first index in [Low..High] where stored value >= Target.
-spec binary_search(array:array(integer()), pos_integer(), pos_integer(), integer()) -> pos_integer().
binary_search(_Arr, Low, High, _Target) when Low > High ->
    Low;
binary_search(Arr, Low, High, Target) ->
    Mid = (Low + High) div 2,
    Val = array:get(Mid, Arr),
    if
        Val < Target -> binary_search(Arr, Mid + 1, High, Target);
        true -> binary_search(Arr, Low, Mid - 1, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_path_length(coordinates :: [[integer]], k :: integer) :: integer
  def max_path_length(coordinates, k) do
    {tx, ty} = List.to_tuple(Enum.at(coordinates, k))

    left =
      coordinates
      |> Enum.with_index()
      |> Enum.filter(fn {_pt, idx} -> idx != k end)
      |> Enum.filter(fn {[x, y], _idx} -> x < tx and y < ty end)
      |> Enum.map(fn {[x, y], _idx} -> {x, y} end)

    right =
      coordinates
      |> Enum.with_index()
      |> Enum.filter(fn {_pt, idx} -> idx != k end)
      |> Enum.filter(fn {[x, y], _idx} -> x > tx and y > ty end)
      |> Enum.map(fn {[x, y], _idx} -> {x, y} end)

    len_left = lis_length(sort_points(left))
    len_right = lis_length(sort_points(right))

    1 + len_left + len_right
  end

  # Sort by x ascending, then y descending
  defp sort_points(points) do
    points
    |> Enum.sort_by(fn {x, y} -> {x, -y} end)
    |> Enum.map(fn {_x, y} -> y end)
  end

  # Longest Increasing Subsequence length on a list of integers (strictly increasing)
  defp lis_length(ys) do
    {_, size} =
      Enum.reduce(ys, {:array.new(), 0}, fn y, {arr, sz} ->
        pos =
          if sz == 0 do
            0
          else
            binary_search(arr, 0, sz - 1, y)
          end

        arr = :array.set(pos, y, arr)
        new_sz = if pos == sz, do: sz + 1, else: sz
        {arr, new_sz}
      end)

    size
  end

  # Find first index in [l..r] where value >= target; if none, returns l (which will be r+1)
  defp binary_search(arr, l, r, target) do
    if l > r do
      l
    else
      mid = div(l + r, 2)
      val = :array.get(mid, arr)

      if val < target do
        binary_search(arr, mid + 1, r, target)
      else
        binary_search(arr, l, mid - 1, target)
      end
    end
  end
end
```

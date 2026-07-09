# 3464. Maximize the Distance Between Points on a Square

## Cpp

```cpp
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        long long L = 4LL * side;
        vector<long long> pos;
        pos.reserve(points.size());
        for (auto &p : points) {
            int x = p[0], y = p[1];
            long long d = 0;
            if (y == 0) {                 // bottom side, from (0,0) to (side,0)
                d = x;
            } else if (x == side) {       // right side, up
                d = (long long)side + y;
            } else if (y == side) {       // top side, leftwards
                d = 3LL * side - x;
            } else {                      // left side, downwards (x==0)
                d = L - y;
            }
            pos.push_back(d);
        }
        sort(pos.begin(), pos.end());
        int n = pos.size();
        vector<long long> dup(2 * n);
        for (int i = 0; i < n; ++i) {
            dup[i] = pos[i];
            dup[i + n] = pos[i] + L;
        }

        auto feasible = [&](long long D) -> bool {
            if (D == 0) return true;
            for (int start = 0; start < n; ++start) {
                int idx = start;
                long long cur = dup[idx];
                bool ok = true;
                for (int cnt = 1; cnt < k; ++cnt) {
                    long long target = cur + D;
                    // search within the next full circle range
                    int limit = start + n; // exclusive upper bound index
                    int nxt = lower_bound(dup.begin() + idx + 1, dup.begin() + limit + 1, target) - dup.begin();
                    if (nxt > limit) { ok = false; break; }
                    cur = dup[nxt];
                    idx = nxt;
                }
                if (!ok) continue;
                long long span = cur - dup[start];
                if (span <= L - D) return true;
            }
            return false;
        };

        long long low = 0, high = L / 2; // maximum possible minimum distance
        while (low < high) {
            long long mid = (low + high + 1) >> 1;
            if (feasible(mid)) low = mid;
            else high = mid - 1;
        }
        return (int)low;
    }
};
```

## Java

```java
class Solution {
    public int maxDistance(int side, int[][] points, int k) {
        int n = points.length;
        long s = side;
        long perimeter = 4L * s;
        long[] pos = new long[n];
        for (int i = 0; i < n; i++) {
            int x = points[i][0];
            int y = points[i][1];
            long t;
            if (y == 0) { // bottom edge
                t = x;
            } else if (x == side) { // right edge
                t = s + y;
            } else if (y == side) { // top edge
                t = 3L * s - x;
            } else { // left edge (x == 0)
                t = 4L * s - y;
            }
            pos[i] = t;
        }
        java.util.Arrays.sort(pos);
        long[] ext = new long[2 * n];
        for (int i = 0; i < n; i++) {
            ext[i] = pos[i];
            ext[i + n] = pos[i] + perimeter;
        }

        // binary search on answer
        long low = 0, high = perimeter / 2;
        while (low < high) {
            long mid = (low + high + 1) >>> 1;
            if (can(mid, k, n, perimeter, ext)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return (int) low;
    }

    private boolean can(long d, int k, int n, long L, long[] ext) {
        if (d == 0) return true;
        for (int start = 0; start < n; start++) {
            int idx = start;
            long curPos = ext[start];
            int cnt = 1;
            while (cnt < k) {
                long target = curPos + d;
                int nextIdx = lowerBound(ext, idx + 1, start + n, target);
                if (nextIdx == start + n) { // cannot find enough points
                    break;
                }
                curPos = ext[nextIdx];
                idx = nextIdx;
                cnt++;
            }
            if (cnt == k) {
                long firstPos = ext[start];
                long lastPos = curPos;
                if (L - (lastPos - firstPos) >= d) return true;
            }
        }
        return false;
    }

    private int lowerBound(long[] arr, int from, int to, long target) {
        int lo = from, hi = to;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        from bisect import bisect_left

        total = 4 * side

        def to_pos(p):
            x, y = p
            if x == 0:          # left edge, go up
                return y
            if y == side:       # top edge, go right
                return side + x
            if x == side:       # right edge, go down
                return 2 * side + (side - y)
            # bottom edge, go left
            return 3 * side + (side - x)

        pos = sorted(to_pos(p) for p in points)
        n = len(pos)
        pos_ext = pos + [p + total for p in pos]

        def can(dist):
            for start in range(n):
                cnt = 1
                last_idx = start
                last_val = pos_ext[start]
                # need to pick k-1 more points within the next n positions
                while cnt < k:
                    target = last_val + dist
                    nxt = bisect_left(pos_ext, target, lo=last_idx + 1, hi=start + n)
                    if nxt >= start + n:
                        break
                    cnt += 1
                    last_idx = nxt
                    last_val = pos_ext[nxt]
                if cnt == k:
                    return True
            return False

        low, high = 0, total
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        L = 4 * side  # perimeter length

        # convert each point to its clockwise distance from (0,0)
        pos = []
        for x, y in points:
            if x == 0:               # left edge, going up
                p = y
            elif y == side:          # top edge, going right
                p = side + x
            elif x == side:          # right edge, going down
                p = 2 * side + (side - y)
            else:                     # bottom edge, going left
                p = 3 * side + (side - x)
            pos.append(p)

        pos.sort()
        n = len(pos)
        ext = pos + [p + L for p in pos]   # duplicated list for wrap‑around

        def feasible(d: int) -> bool:
            if d == 0:
                return True
            for start in range(n):
                cnt = 1
                last = pos[start]
                idx = start
                while cnt < k:
                    target = last + d
                    lo = idx + 1
                    hi = start + n   # cannot go beyond one full loop
                    nxt = bisect.bisect_left(ext, target, lo, hi)
                    if nxt == hi:
                        break
                    last = ext[nxt]
                    idx = nxt
                    cnt += 1
                if cnt == k and L - (last - pos[start]) >= d:
                    return True
            return False

        low, high = 0, L // 2
        while low < high:
            mid = (low + high + 1) // 2
            if feasible(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## C

```c
#include <stdlib.h>

static int cmp_ll(const void *a, const void *b) {
    long long va = *(const long long *)a;
    long long vb = *(const long long *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

static int feasible(long long d, const long long *pos, const long long *dup, int n, long long L, int k) {
    for (int start = 0; start < n; ++start) {
        int cnt = 1;
        long long first = pos[start];
        long long last = first;
        int idx = start + 1;
        while (cnt < k && idx < start + n) {
            if (dup[idx] - last >= d) {
                ++cnt;
                last = dup[idx];
            }
            ++idx;
        }
        if (cnt == k && L - (last - first) >= d)
            return 1;
    }
    return 0;
}

int maxDistance(int side, int** points, int pointsSize, int* pointsColSize, int k) {
    int n = pointsSize;
    long long L = 4LL * side;
    long long *pos = (long long *)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; ++i) {
        int x = points[i][0];
        int y = points[i][1];
        long long p;
        if (y == 0) {
            p = x;
        } else if (x == side) {
            p = (long long)side + y;
        } else if (y == side) {
            p = 2LL * side + (side - x);
        } else { // x == 0
            p = 3LL * side + (side - y);
        }
        pos[i] = p;
    }

    qsort(pos, n, sizeof(long long), cmp_ll);

    long long *dup = (long long *)malloc(sizeof(long long) * (2 * n));
    for (int i = 0; i < n; ++i) {
        dup[i] = pos[i];
        dup[i + n] = pos[i] + L;
    }

    long long low = 0, high = L / 2;
    while (low < high) {
        long long mid = (low + high + 1) >> 1;
        if (feasible(mid, pos, dup, n, L, k))
            low = mid;
        else
            high = mid - 1;
    }

    free(pos);
    free(dup);
    return (int)low;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxDistance(int side, int[][] points, int k) {
        long L = 4L * side;
        List<long> posList = new List<long>(points.Length);
        foreach (var p in points) {
            int x = p[0], y = p[1];
            long pos;
            if (x == 0) {
                // left edge, going up
                pos = y;
            } else if (y == side) {
                // top edge, moving right
                pos = side + x;
            } else if (x == side) {
                // right edge, moving down
                pos = 2L * side + (side - y);
            } else { // y == 0
                // bottom edge, moving left
                pos = 3L * side + (side - x);
            }
            posList.Add(pos);
        }

        posList.Sort();
        int n = posList.Count;
        long[] pos = new long[2 * n];
        for (int i = 0; i < n; i++) {
            pos[i] = posList[i];
            pos[i + n] = posList[i] + L;
        }

        // binary search on answer
        int lo = 0, hi = side * 2; // maximum possible Manhattan distance between boundary points
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (CanPlace(pos, n, k, mid, L))
                lo = mid;
            else
                hi = mid - 1;
        }
        return lo;
    }

    private bool CanPlace(long[] posDup, int n, int k, int dist, long L) {
        // try each starting point among first n positions
        for (int start = 0; start < n; start++) {
            int count = 1;
            long last = posDup[start];
            int idx = start + 1;
            while (count < k && idx < start + n) {
                // find first position >= last + dist
                long target = last + dist;
                int lo = idx, hi = start + n; // exclusive upper bound
                while (lo < hi) {
                    int mid = lo + (hi - lo) / 2;
                    if (posDup[mid] >= target) hi = mid;
                    else lo = mid + 1;
                }
                if (lo == start + n) break; // cannot place further
                last = posDup[lo];
                idx = lo + 1;
                count++;
            }
            if (count == k) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} side
 * @param {number[][]} points
 * @param {number} k
 * @return {number}
 */
var maxDistance = function(side, points, k) {
    const perim = 4 * side;
    // map each point to its clockwise distance from (0,0)
    const coord = points.map(p => {
        const x = p[0], y = p[1];
        if (y === 0) return x;                     // bottom
        if (x === side) return side + y;           // right
        if (y === side) return 2 * side + (side - x); // top
        // left side (x===0)
        return 3 * side + (side - y);
    });
    coord.sort((a, b) => a - b);
    const n = coord.length;
    // duplicate for circular handling
    const dup = new Array(2 * n);
    for (let i = 0; i < n; ++i) {
        dup[i] = coord[i];
        dup[i + n] = coord[i] + perim;
    }

    function lowerBound(arr, target, start) {
        let l = start, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    }

    function can(d) {
        // try each start point
        for (let s = 0; s < n; ++s) {
            let cnt = 1;
            let idx = s;
            while (cnt < k) {
                const target = dup[idx] + d;
                const nextIdx = lowerBound(dup, target, idx + 1);
                if (nextIdx >= s + n) break; // out of circle range
                cnt++;
                idx = nextIdx;
            }
            if (cnt === k) {
                const span = dup[idx] - dup[s];
                if (span <= perim - d) return true;
            }
        }
        return false;
    }

    let low = 0, high = perim; // inclusive
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) low = mid;
        else high = mid - 1;
    }
    return low;
};
```

## Typescript

```typescript
function maxDistance(side: number, points: number[][], k: number): number {
    const L = 4 * side;

    // map each point to a position on the perimeter (clockwise from (0,0))
    const pos: number[] = [];
    for (const [x, y] of points) {
        if (y === 0) {                     // bottom edge
            pos.push(x);
        } else if (x === side) {           // right edge
            pos.push(side + y);
        } else if (y === side) {           // top edge
            pos.push(2 * side + (side - x));
        } else if (x === 0) {              // left edge
            pos.push(3 * side + (side - y));
        }
    }

    pos.sort((a, b) => a - b);
    const n = pos.length;

    // extended array to handle wrap‑around
    const ext: number[] = new Array(2 * n);
    for (let i = 0; i < n; ++i) {
        ext[i] = pos[i];
        ext[i + n] = pos[i] + L;
    }

    function lowerBound(arr: number[], target: number, start: number): number {
        let l = start, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    }

    function can(dist: number): boolean {
        for (let s = 0; s < n; ++s) {
            let cnt = 1;
            let last = pos[s];
            let idx = s;
            while (cnt < k) {
                const target = last + dist;
                const j = lowerBound(ext, target, idx + 1);
                if (j >= s + n) break; // exceeded one full loop
                cnt++;
                last = ext[j];
                idx = j;
            }
            if (cnt === k) return true;
        }
        return false;
    }

    let low = 0, high = Math.floor(L / 2);
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) low = mid;
        else high = mid - 1;
    }
    return low;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $side
     * @param Integer[][] $points
     * @param Integer $k
     * @return Integer
     */
    function maxDistance($side, $points, $k) {
        $n = count($points);
        $pos = [];
        foreach ($points as $p) {
            [$x, $y] = $p;
            if ($y == 0) {
                $pPos = $x; // bottom edge
            } elseif ($x == $side) {
                $pPos = $side + $y; // right edge
            } elseif ($y == $side) {
                $pPos = 2 * $side + ($side - $x); // top edge
            } else { // $x == 0
                $pPos = 3 * $side + ($side - $y); // left edge
            }
            $pos[] = $pPos;
        }
        sort($pos);
        $L = 4 * $side;

        $low = 0;
        $high = intdiv($L, 2); // maximum possible minimal distance

        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->canPlace($mid, $pos, $n, $k, $L)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }

    private function canPlace($d, $pos, $n, $k, $L) {
        // duplicate positions to handle wrap‑around
        $ext = array_merge($pos, array_map(function ($v) use ($L) { return $v + $L; }, $pos));
        $m = $n * 2;
        $next = array_fill(0, $m, -1);

        // two‑pointer to compute next index with distance >= d
        $j = 0;
        for ($i = 0; $i < $m; $i++) {
            if ($j < $i + 1) $j = $i + 1;
            while ($j < $m && $ext[$j] - $ext[$i] < $d) {
                $j++;
            }
            if ($j < $m) $next[$i] = $j;
        }

        // try each starting point among original positions
        for ($start = 0; $start < $n; $start++) {
            $cur = $start;
            $cnt = 1;
            while ($cnt < $k && $next[$cur] != -1 && $next[$cur] < $start + $n) {
                $cur = $next[$cur];
                $cnt++;
            }
            if ($cnt == $k) {
                $totalDist = $ext[$cur] - $ext[$start]; // clockwise span
                if ($L - $totalDist >= $d) {
                    return true;
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
    func maxDistance(_ side: Int, _ points: [[Int]], _ k: Int) -> Int {
        let n = points.count
        var pts: [(x: Int, y: Int, d: Int64)] = []
        pts.reserveCapacity(n)
        for p in points {
            let x = p[0]
            let y = p[1]
            var d: Int64 = 0
            if y == 0 {                 // bottom edge (0,0) -> (side,0)
                d = Int64(x)
            } else if x == side {       // right edge (side,0) -> (side,side)
                d = Int64(side) + Int64(y)
            } else if y == side {       // top edge (side,side) -> (0,side)
                d = Int64(2 * side) + Int64(side - x)
            } else {                    // left edge (0,side) -> (0,0)
                d = Int64(3 * side) + Int64(side - y)
            }
            pts.append((x, y, d))
        }
        pts.sort { $0.d < $1.d }
        var xs: [Int] = []
        var ys: [Int] = []
        xs.reserveCapacity(n)
        ys.reserveCapacity(n)
        for p in pts {
            xs.append(p.x)
            ys.append(p.y)
        }
        // duplicate to handle circular wrap
        let xs2 = xs + xs
        let ys2 = ys + ys
        
        func feasible(_ dist: Int64) -> Bool {
            for start in 0..<n {
                var count = 1
                var cur = start
                while count < k {
                    var nxt = cur + 1
                    while nxt < start + n {
                        let dval = Int64(abs(xs2[cur] - xs2[nxt])) + Int64(abs(ys2[cur] - ys2[nxt]))
                        if dval >= dist { break }
                        nxt += 1
                    }
                    if nxt == start + n { break } // cannot place more points starting here
                    cur = nxt
                    count += 1
                }
                if count == k { return true }
            }
            return false
        }
        
        var low: Int64 = 0
        var high: Int64 = Int64(2 * side)
        while low < high {
            let mid = (low + high + 1) >> 1
            if feasible(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return Int(low)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun maxDistance(side: Int, points: Array<IntArray>, k: Int): Int {
        val perim = 4L * side
        val tList = LongArray(points.size)
        for (i in points.indices) {
            val x = points[i][0].toLong()
            val y = points[i][1].toLong()
            val t = when {
                y == 0L -> x                         // bottom edge, left to right
                x == side.toLong() -> side.toLong() + y   // right edge, bottom to top
                y == side.toLong() -> 2L * side - x       // top edge, right to left
                else -> 3L * side + (side - y)            // left edge, top to bottom
            }
            tList[i] = t
        }
        Arrays.sort(tList)

        fun can(dist: Long): Boolean {
            val n = tList.size
            for (start in 0 until n) {
                var cnt = 1
                val first = tList[start]
                var last = first
                // iterate over next points in circular order
                var idx = start + 1
                while (cnt < k && idx < start + n) {
                    val curIdx = if (idx >= n) idx - n else idx
                    var curVal = tList[curIdx]
                    if (curIdx < start) curVal += perim
                    if (curVal - last >= dist) {
                        cnt++
                        last = curVal
                    }
                    idx++
                }
                if (cnt == k) {
                    // check wrap-around gap
                    if (perim - (last - first) >= dist) return true
                }
            }
            return false
        }

        var low = 0L
        var high = 2L * side.toLong()
        while (low < high) {
            val mid = (low + high + 1) ushr 1
            if (can(mid)) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxDistance(int side, List<List<int>> points, int k) {
    int L = 4 * side;
    // Map each point to its position along the perimeter in clockwise order.
    List<int> pos = [];
    for (var p in points) {
      int x = p[0], y = p[1];
      int s;
      if (y == 0) {
        // bottom edge, from (0,0) to (side,0)
        s = x;
      } else if (x == side) {
        // right edge, from (side,0) up to (side,side)
        s = side + y;
      } else if (y == side) {
        // top edge, from (side,side) leftwards to (0,side)
        s = 2 * side + (side - x);
      } else {
        // left edge, from (0,side) downwards to (0,0)
        s = 3 * side + (side - y);
      }
      pos.add(s);
    }

    pos.sort();
    int n = pos.length;
    List<int> ext = List.filled(n * 2, 0);
    for (int i = 0; i < n; ++i) {
      ext[i] = pos[i];
      ext[i + n] = pos[i] + L;
    }

    // lower bound: first index in [l, r) with value >= target
    int lowerBound(List<int> arr, int l, int r, int target) {
      while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m] >= target) {
          r = m;
        } else {
          l = m + 1;
        }
      }
      return l;
    }

    bool can(int d) {
      for (int start = 0; start < n; ++start) {
        int count = 1;
        int idx = start;
        int cur = ext[idx];
        bool ok = true;
        while (count < k) {
          int target = cur + d;
          int lo = idx + 1;
          int hi = start + n; // exclusive
          int nxt = lowerBound(ext, lo, hi, target);
          if (nxt >= start + n) {
            ok = false;
            break;
          }
          idx = nxt;
          cur = ext[idx];
          count++;
        }
        if (!ok) continue;
        // ensure circular distance between first and last is at least d
        if (cur <= ext[start] + L - d) return true;
      }
      return false;
    }

    int low = 0, high = L;
    while (low < high) {
      int mid = (low + high + 1) >> 1;
      if (can(mid)) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func maxDistance(side int, points [][]int, k int) int {
    n := len(points)
    p := int64(side)
    perim := 4 * p

    // Convert each point to its perimeter coordinate.
    coords := make([]int64, n)
    for i, pt := range points {
        x, y := int64(pt[0]), int64(pt[1])
        var c int64
        if y == 0 { // bottom edge
            c = x
        } else if x == p { // right edge
            c = p + y
        } else if y == p { // top edge
            c = 2*p + (p - x)
        } else { // left edge (x == 0)
            c = 3*p + (p - y)
        }
        coords[i] = c
    }

    sort.Slice(coords, func(i, j int) bool { return coords[i] < coords[j] })

    // Duplicate the array to handle wrap‑around.
    ext := make([]int64, 2*n)
    copy(ext[:n], coords)
    for i := 0; i < n; i++ {
        ext[n+i] = coords[i] + perim
    }

    feasible := func(dist int64) bool {
        for start := 0; start < n; start++ {
            pos := start
            cnt := 1
            for cnt < k {
                target := ext[pos] + dist
                idx := sort.Search(len(ext), func(i int) bool { return ext[i] >= target })
                if idx >= start+n { // exceeded one full circle
                    break
                }
                pos = idx
                cnt++
            }
            if cnt == k && ext[pos]-ext[start] <= perim-dist {
                return true
            }
        }
        return false
    }

    low, high := int64(0), perim
    for low < high {
        mid := (low + high + 1) / 2
        if feasible(mid) {
            low = mid
        } else {
            high = mid - 1
        }
    }
    return int(low)
}
```

## Ruby

```ruby
def max_distance(side, points, k)
  # Convert each point to its clockwise distance from (0,0)
  perim = 4 * side
  pos = points.map do |x, y|
    if y == 0
      x
    elsif x == side
      side + y
    elsif y == side
      2 * side + (side - x)
    else # x == 0
      3 * side + (side - y)
    end
  end

  pos.sort!
  n = pos.size
  dup = pos + pos.map { |p| p + perim }

  # binary search on answer
  low = 0
  high = perim / 2   # maximum possible minimum Manhattan distance
  while low < high
    mid = (low + high + 1) >> 1
    feasible = false

    n.times do |start|
      cnt = 1
      cur_idx = start
      cur_pos = dup[start]

      while cnt < k
        target = cur_pos + mid
        # binary search for the first index > cur_idx with value >= target
        l = cur_idx + 1
        r = start + n - 1
        idx = nil
        while l <= r
          m = (l + r) >> 1
          if dup[m] < target
            l = m + 1
          else
            idx = m
            r = m - 1
          end
        end
        break unless idx && idx <= start + n - 1
        cnt += 1
        cur_idx = idx
        cur_pos = dup[idx]
      end

      if cnt >= k
        feasible = true
        break
      end
    end

    if feasible
      low = mid
    else
      high = mid - 1
    end
  end

  low
end
```

## Scala

```scala
object Solution {
    def maxDistance(side: Int, points: Array[Array[Int]], k: Int): Int = {
        val n = points.length
        case class Pt(x: Int, y: Int, pos: Long)
        val pts = new Array[Pt](n)
        var idx = 0
        while (idx < n) {
            val x = points(idx)(0)
            val y = points(idx)(1)
            val pos: Long =
                if (y == 0) x.toLong
                else if (x == side) side.toLong + y
                else if (y == side) 2L * side + (side - x)
                else 3L * side + (side - y) // x == 0
            pts(idx) = Pt(x, y, pos)
            idx += 1
        }
        java.util.Arrays.sort(pts, new java.util.Comparator[Pt] {
            def compare(a: Pt, b: Pt): Int = java.lang.Long.compare(a.pos, b.pos)
        })
        val xs = new Array[Int](2 * n)
        val ys = new Array[Int](2 * n)
        var i = 0
        while (i < n) {
            xs(i) = pts(i).x
            ys(i) = pts(i).y
            xs(i + n) = xs(i)
            ys(i + n) = ys(i)
            i += 1
        }
        def manhattan(a: Int, b: Int): Int = {
            Math.abs(xs(a) - xs(b)) + Math.abs(ys(a) - ys(b))
        }

        var low = 0
        var high = 2 * side
        while (low < high) {
            val mid = (low + high + 1) / 2

            // compute next index for each position
            val nxt = new Array[Int](2 * n)
            var j = 0
            var ii = 0
            while (ii < 2 * n) {
                if (j < ii + 1) j = ii + 1
                while (j < ii + n && manhattan(ii, j) < mid) {
                    j += 1
                }
                nxt(ii) = if (j < ii + n) j else 2 * n // sentinel out of range
                ii += 1
            }

            var ok = false
            var start = 0
            while (!ok && start < n) {
                var cur = start
                var cnt = 1
                while (cnt < k && cur < start + n) {
                    val nextPos = nxt(cur)
                    if (nextPos >= start + n) {
                        cnt = -100 // break
                    } else {
                        cur = nextPos
                        cnt += 1
                    }
                }
                if (cnt == k) ok = true
                start += 1
            }

            if (ok) low = mid else high = mid - 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_distance(side: i32, points: Vec<Vec<i32>>, k: i32) -> i32 {
        let side_i64 = side as i64;
        let perim = 4 * side_i64;

        // map each point to its clockwise distance from (0,0)
        let mut pos: Vec<i64> = points
            .into_iter()
            .map(|p| {
                let x = p[0];
                let y = p[1];
                if y == 0 {
                    x as i64
                } else if x == side {
                    side_i64 + y as i64
                } else if y == side {
                    2 * side_i64 + (side_i64 - x as i64)
                } else {
                    // x == 0
                    3 * side_i64 + (side_i64 - y as i64)
                }
            })
            .collect();

        pos.sort_unstable();
        let n = pos.len();
        let mut ext: Vec<i64> = Vec::with_capacity(2 * n);
        for &v in &pos {
            ext.push(v);
        }
        for &v in &pos {
            ext.push(v + perim);
        }

        // helper lower_bound
        fn lower_bound(arr: &[i64], target: i64, start: usize) -> usize {
            let mut l = start;
            let mut r = arr.len();
            while l < r {
                let m = (l + r) / 2;
                if arr[m] < target {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            l
        }

        // feasibility check for a given distance x
        fn feasible(x: i64, k: usize, perim: i64, pos: &[i64], ext: &[i64]) -> bool {
            let n = pos.len();
            for start in 0..n {
                let mut cnt = 1usize;
                let mut cur_idx = start;
                let mut cur_pos = pos[start];
                while cnt < k {
                    let target = cur_pos + x;
                    // search in ext, must stay within one full circle (index < start + n)
                    let idx = lower_bound(ext, target, cur_idx + 1);
                    if idx >= start + n {
                        break;
                    }
                    cur_idx = idx;
                    cur_pos = ext[cur_idx];
                    cnt += 1;
                }
                if cnt == k {
                    let total_gap = cur_pos - pos[start]; // clockwise distance from first to last
                    if perim - total_gap >= x {
                        return true;
                    }
                }
            }
            false
        }

        let k_usize = k as usize;
        let mut lo: i64 = 0;
        let mut hi: i64 = perim / 2; // maximum possible minimal distance

        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if feasible(mid, k_usize, perim, &pos, &ext) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }

        lo as i32
    }
}
```

## Racket

```racket
(define/contract (max-distance side points k)
  (-> exact-integer?
      (listof (listof exact-integer?))
      exact-integer?
      exact-integer?)
  (let* ((L (* 4 side))
         ;; convert each point to its perimeter position
         (pos-list
          (map (lambda (pt)
                 (let ((x (first pt)) (y (second pt)))
                   (cond [(= y 0) x]                         ; bottom edge
                         [(= x side) (+ side y)]            ; right edge
                         [(= y side) (+ (* 2 side) (- side x))] ; top edge
                         [else        (+ (* 3 side) (- side y))]))) ; left edge
               points))
         (sorted-pos (sort pos-list <))
         (n (length sorted-pos))
         ;; vectors for fast indexing
         (pos-vec (list->vector sorted-pos))
         (ext-vec (let ((v (make-vector (* 2 n))))
                    (for ([i (in-range n)])
                      (vector-set! v i (vector-ref pos-vec i))
                      (vector-set! v (+ i n) (+ (vector-ref pos-vec i) L)))
                    v)))
    ;; binary search on answer
    (let loop ((low 0) (high L))
      (if (> low high)
          low
          (let* ((mid (quotient (+ low high 1) 2))) ; upper mid
            (define (feasible d)
              (let outer ((start-idx 0))
                (if (= start-idx n)
                    #f
                    (let* ((start-pos (vector-ref pos-vec start-idx))
                           (target-end (- L d)) ; maximal allowed span from start to last selected
                           (cnt 1)
                           (last-pos start-pos)
                           (cur-idx (+ start-idx 1)))
                      ;; inner loop to pick next points greedily
                      (let inner ((cnt cnt) (last last-pos) (cur cur-idx))
                        (if (= cnt k)
                            (if (<= (- last start-pos) target-end)
                                #t
                                (outer (+ start-idx 1))) ; try next start
                            (let* ((need (+ last d))
                                   ;; binary search in ext-vec between cur and start-idx + n
                                   (lo cur)
                                   (hi (+ start-idx n)))
                              (let find ((l lo) (r hi))
                                (if (= l r)
                                    #f ; cannot find enough points
                                    (let* ((midb (quotient (+ l r) 2))
                                           (val (vector-ref ext-vec midb)))
                                      (if (< val need)
                                          (find (+ midb 1) r)
                                          (find l midb))))))))
                      ))))
            (if (feasible mid)
                (loop mid (+ high 0)) ; keep low = mid
                (loop low (- mid 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_distance/3]).

-spec max_distance(Side :: integer(), Points :: [[integer()]], K :: integer()) -> integer().
max_distance(Side, Points, K) ->
    Total = 4 * Side,
    Positions = [point_to_pos(P, Side) || P <- Points],
    Sorted = lists:sort(Positions),
    N = length(Sorted),
    DupList = Sorted ++ [P + Total || P <- Sorted],
    PosTuple = list_to_tuple(DupList),
    binary_search(0, Total, N, K, Total, PosTuple).

point_to_pos([X, Y], Side) ->
    case X of
        0 -> Y;                                   % left side (including (0,0))
        _ when X == Side ->
            case Y of
                Side -> Side + X;                 % top side, right-top corner
                _ -> 2 * Side + (Side - Y)        % right side descending
            end;
        _ ->
            case Y of
                0 -> 3 * Side + (Side - X);       % bottom side moving leftwards
                Side -> Side + X                  % top side moving rightwards
            end
    end.

binary_search(Low, High, N, K, Total, PosTuple) when Low < High ->
    Mid = (Low + High + 1) div 2,
    case feasible(Mid, N, K, Total, PosTuple) of
        true -> binary_search(Mid, High, N, K, Total, PosTuple);
        false -> binary_search(Low, Mid - 1, N, K, Total, PosTuple)
    end;
binary_search(Low, _High, _N, _K, _Total, _PosTuple) ->
    Low.

feasible(Dist, N, K, Total, PosTuple) ->
    feasible_start(0, Dist, N, K, Total, PosTuple).

feasible_start(I, Dist, N, K, Total, PosTuple) when I < N ->
    case try_select(I, Dist, N, K, Total, PosTuple) of
        true -> true;
        false -> feasible_start(I + 1, Dist, N, K, Total, PosTuple)
    end;
feasible_start(_, _, _, _, _, _) ->
    false.

try_select(StartIdxZero, Dist, N, K, Total, PosTuple) ->
    FirstPos = element(StartIdxZero + 1, PosTuple),
    select(FirstPos, StartIdxZero, 1, FirstPos, StartIdxZero, Dist, N, K, Total, PosTuple).

select(_PrevPos, _PrevIdxZero, Count, _FirstPos, _StartIdxZero, _Dist, _N, K, _Total, _PosTuple) when Count == K ->
    false; % unreachable, handled in clause with PrevPos
select(PrevPos, PrevIdxZero, Count, FirstPos, StartIdxZero, Dist, N, K, Total, PosTuple) when Count == K ->
    ((FirstPos + Total) - PrevPos) >= Dist;
select(PrevPos, PrevIdxZero, Count, FirstPos, StartIdxZero, Dist, N, K, Total, PosTuple) ->
    Target = PrevPos + Dist,
    MaxIdxZero = StartIdxZero + N,
    case lower_bound(PosTuple, PrevIdxZero + 1, MaxIdxZero, Target) of
        undefined -> false;
        NextIdxZero ->
            NextPos = element(NextIdxZero + 1, PosTuple),
            select(NextPos, NextIdxZero, Count + 1, FirstPos, StartIdxZero, Dist, N, K, Total, PosTuple)
    end.

lower_bound(_Tuple, LowZero, HighZero, _Target) when LowZero > HighZero ->
    undefined;
lower_bound(Tuple, LowZero, HighZero, Target) ->
    MidZero = (LowZero + HighZero) div 2,
    Val = element(MidZero + 1, Tuple),
    if
        Val >= Target ->
            case lower_bound(Tuple, LowZero, MidZero - 1, Target) of
                undefined -> MidZero;
                Idx -> Idx
            end;
        true ->
            lower_bound(Tuple, MidZero + 1, HighZero, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_distance(side :: integer, points :: [[integer]], k :: integer) :: integer
  def max_distance(side, points, k) do
    perim = 4 * side

    positions =
      points
      |> Enum.map(fn [x, y] -> point_to_pos(x, y, side) end)
      |> Enum.sort()

    n = length(positions)

    dup_positions = positions ++ Enum.map(positions, fn v -> v + perim end)
    pos_tuple = List.to_tuple(dup_positions)

    binary_search(0, perim, pos_tuple, n, k)
  end

  defp point_to_pos(x, y, side) do
    cond do
      y == 0 -> x
      x == side -> side + y
      y == side -> 2 * side + (side - x)
      x == 0 -> 3 * side + (side - y)
    end
  end

  defp binary_search(low, high, tuple, n, k) do
    if low < high do
      mid = div(low + high + 1, 2)

      if feasible?(tuple, n, k, mid) do
        binary_search(mid, high, tuple, n, k)
      else
        binary_search(low, mid - 1, tuple, n, k)
      end
    else
      low
    end
  end

  defp feasible?(tuple, n, k, d) do
    do_feasible(0, n, tuple, k, d)
  end

  defp do_feasible(start, n, _tuple, _k, _d) when start >= n, do: false

  defp do_feasible(start, n, tuple, k, d) do
    if can_select?(tuple, n, k, d, start) do
      true
    else
      do_feasible(start + 1, n, tuple, k, d)
    end
  end

  defp can_select?(tuple, n, k, d, start) do
    limit = start + n - 1
    select_loop(1, elem(tuple, start), start, limit, tuple, k, d)
  end

  defp select_loop(count, _last, _idx, _limit, _tuple, k, _d) when count >= k, do: true

  defp select_loop(count, last, idx, limit, tuple, k, d) do
    target = last + d

    case first_ge(tuple, idx + 1, limit, target) do
      nil -> false
      pos ->
        new_last = elem(tuple, pos)
        select_loop(count + 1, new_last, pos, limit, tuple, k, d)
    end
  end

  defp first_ge(_tuple, lo, hi, _target) when lo > hi, do: nil

  defp first_ge(tuple, lo, hi, target) do
    mid = div(lo + hi, 2)
    val = elem(tuple, mid)

    if val >= target do
      case first_ge(tuple, lo, mid - 1, target) do
        nil -> mid
        res -> res
      end
    else
      first_ge(tuple, mid + 1, hi, target)
    end
  end
end
```

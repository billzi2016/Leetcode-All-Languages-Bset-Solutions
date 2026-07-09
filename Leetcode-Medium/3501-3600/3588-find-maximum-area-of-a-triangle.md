# 3588. Find Maximum Area of a Triangle

## Cpp

```cpp
class Solution {
public:
    long long maxArea(vector<vector<int>>& coords) {
        if (coords.size() < 3) return -1;
        unordered_map<int, pair<int,int>> yMap; // y -> {minX, maxX}
        unordered_map<int, pair<int,int>> xMap; // x -> {minY, maxY}
        int minX = INT_MAX, maxX = INT_MIN, minY = INT_MAX, maxY = INT_MIN;
        for (auto& p : coords) {
            int x = p[0], y = p[1];
            minX = min(minX, x);
            maxX = max(maxX, x);
            minY = min(minY, y);
            maxY = max(maxY, y);
            auto &ym = yMap[y];
            if (ym.first == 0 && ym.second == 0) { // first time, need sentinel
                ym.first = x;
                ym.second = x;
            } else {
                ym.first = min(ym.first, x);
                ym.second = max(ym.second, x);
            }
            auto &xm = xMap[x];
            if (xm.first == 0 && xm.second == 0) {
                xm.first = y;
                xm.second = y;
            } else {
                xm.first = min(xm.first, y);
                xm.second = max(xm.second, y);
            }
        }
        long long ans = 0;
        for (auto& kv : yMap) {
            int y = kv.first;
            int minx = kv.second.first;
            int maxx = kv.second.second;
            long long base = (long long)maxx - minx;
            if (base == 0) continue; // need two distinct points on this horizontal line
            long long height = max((long long)y - minY, (long long)maxY - y);
            if (height == 0) continue; // no point with different y
            ans = max(ans, base * height);
        }
        for (auto& kv : xMap) {
            int x = kv.first;
            int miny = kv.second.first;
            int maxy = kv.second.second;
            long long base = (long long)maxy - miny;
            if (base == 0) continue; // need two distinct points on this vertical line
            long long height = max((long long)x - minX, (long long)maxX - x);
            if (height == 0) continue; // no point with different x
            ans = max(ans, base * height);
        }
        return ans == 0 ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public long maxArea(int[][] coords) {
        int n = coords.length;
        if (n < 3) return -1L;

        java.util.HashMap<Integer, int[]> yMap = new java.util.HashMap<>();
        java.util.HashMap<Integer, int[]> xMap = new java.util.HashMap<>();

        int minX = Integer.MAX_VALUE, maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE, maxY = Integer.MIN_VALUE;

        for (int[] p : coords) {
            int x = p[0];
            int y = p[1];

            if (x < minX) minX = x;
            if (x > maxX) maxX = x;
            if (y < minY) minY = y;
            if (y > maxY) maxY = y;

            int[] arrY = yMap.get(y);
            if (arrY == null) {
                arrY = new int[]{x, x};
                yMap.put(y, arrY);
            } else {
                if (x < arrY[0]) arrY[0] = x;
                if (x > arrY[1]) arrY[1] = x;
            }

            int[] arrX = xMap.get(x);
            if (arrX == null) {
                arrX = new int[]{y, y};
                xMap.put(x, arrX);
            } else {
                if (y < arrX[0]) arrX[0] = y;
                if (y > arrX[1]) arrX[1] = y;
            }
        }

        long best = 0L;

        for (java.util.Map.Entry<Integer, int[]> e : yMap.entrySet()) {
            int y = e.getKey();
            int[] mnMx = e.getValue();
            long base = (long) mnMx[1] - mnMx[0];
            if (base == 0) continue;
            long height = Math.max((long) maxY - y, (long) y - minY);
            if (height == 0) continue;
            best = Math.max(best, base * height);
        }

        for (java.util.Map.Entry<Integer, int[]> e : xMap.entrySet()) {
            int x = e.getKey();
            int[] mnMx = e.getValue();
            long base = (long) mnMx[1] - mnMx[0];
            if (base == 0) continue;
            long height = Math.max((long) maxX - x, (long) x - minX);
            if (height == 0) continue;
            best = Math.max(best, base * height);
        }

        return best == 0L ? -1L : best;
    }
}
```

## Python

```python
class Solution(object):
    def maxArea(self, coords):
        """
        :type coords: List[List[int]]
        :rtype: int
        """
        if not coords:
            return -1

        # dictionaries to store min and max other coordinate for each fixed y or x
        min_x_at_y = {}
        max_x_at_y = {}
        min_y_at_x = {}
        max_y_at_x = {}

        global_min_y = float('inf')
        global_max_y = -float('inf')
        global_min_x = float('inf')
        global_max_x = -float('inf')

        for x, y in coords:
            # update per y
            if y not in min_x_at_y:
                min_x_at_y[y] = max_x_at_y[y] = x
            else:
                if x < min_x_at_y[y]:
                    min_x_at_y[y] = x
                if x > max_x_at_y[y]:
                    max_x_at_y[y] = x

            # update per x
            if x not in min_y_at_x:
                min_y_at_x[x] = max_y_at_x[x] = y
            else:
                if y < min_y_at_x[x]:
                    min_y_at_x[x] = y
                if y > max_y_at_x[x]:
                    max_y_at_x[x] = y

            # update globals
            if y < global_min_y:
                global_min_y = y
            if y > global_max_y:
                global_max_y = y
            if x < global_min_x:
                global_min_x = x
            if x > global_max_x:
                global_max_x = x

        best = 0

        # horizontal bases (same y)
        for y, minx in min_x_at_y.items():
            maxx = max_x_at_y[y]
            base = maxx - minx
            if base == 0:
                continue
            height = max(y - global_min_y, global_max_y - y)
            if height == 0:
                continue
            area2 = base * height
            if area2 > best:
                best = area2

        # vertical bases (same x)
        for x, miny in min_y_at_x.items():
            maxy = max_y_at_x[x]
            base = maxy - miny
            if base == 0:
                continue
            height = max(x - global_min_x, global_max_x - x)
            if height == 0:
                continue
            area2 = base * height
            if area2 > best:
                best = area2

        return best if best != 0 else -1
```

## Python3

```python
class Solution:
    def maxArea(self, coords):
        from collections import defaultdict

        min_x = float('inf')
        max_x = -float('inf')
        min_y = float('inf')
        max_y = -float('inf')

        y_map = {}
        x_map = {}

        for x, y in coords:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

            if y not in y_map:
                y_map[y] = [x, x]  # [min_x_at_y, max_x_at_y]
            else:
                if x < y_map[y][0]: y_map[y][0] = x
                if x > y_map[y][1]: y_map[y][1] = x

            if x not in x_map:
                x_map[x] = [y, y]  # [min_y_at_x, max_y_at_x]
            else:
                if y < x_map[x][0]: x_map[x][0] = y
                if y > x_map[x][1]: x_map[x][1] = y

        ans = 0

        # Horizontal bases (same y)
        for y, (minx, maxx) in y_map.items():
            base = maxx - minx
            if base == 0:
                continue
            height = max(abs(y - min_y), abs(y - max_y))
            if height == 0:
                continue
            area2 = base * height
            if area2 > ans:
                ans = area2

        # Vertical bases (same x)
        for x, (miny, maxy) in x_map.items():
            base = maxy - miny
            if base == 0:
                continue
            height = max(abs(x - min_x), abs(x - max_x))
            if height == 0:
                continue
            area2 = base * height
            if area2 > ans:
                ans = area2

        return -1 if ans == 0 else ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>
#include <stdint.h>

typedef struct {
    int min;
    int max;
} MinMax;

long long maxArea(int** coords, int coordsSize, int* coordsColSize) {
    if (coordsSize < 3) return -1;
    
    int globalMinX = INT_MAX, globalMaxX = INT_MIN;
    int globalMinY = INT_MAX, globalMaxY = INT_MIN;
    
    // Use simple hash tables with open addressing via unordered_map equivalent in C.
    // Since we cannot use C++ STL, implement using hashmap with chaining (simple).
    // For constraints up to 1e5, we can use arrays of size power of two and linear probing.
    // However for simplicity and given typical LeetCode C environment, we can use
    // a binary search tree via qsort after collecting points per coordinate.
    // We'll store all points then process groups by sorting.
    
    // Allocate arrays to hold points.
    int *xs = (int*)malloc(sizeof(int) * coordsSize);
    int *ys = (int*)malloc(sizeof(int) * coordsSize);
    for (int i = 0; i < coordsSize; ++i) {
        xs[i] = coords[i][0];
        ys[i] = coords[i][1];
        if (xs[i] < globalMinX) globalMinX = xs[i];
        if (xs[i] > globalMaxX) globalMaxX = xs[i];
        if (ys[i] < globalMinY) globalMinY = ys[i];
        if (ys[i] > globalMaxY) globalMaxY = ys[i];
    }
    
    // Helper struct for sorting by y then x.
    typedef struct {int key; int val;} Pair;
    
    // Process groups with same y (horizontal base)
    Pair *byY = (Pair*)malloc(sizeof(Pair) * coordsSize);
    for (int i = 0; i < coordsSize; ++i) {
        byY[i].key = ys[i];
        byY[i].val = xs[i];
    }
    // sort by key then val
    int cmpByKeyVal(const void *a, const void *b) {
        const Pair *pa = (const Pair*)a;
        const Pair *pb = (const Pair*)b;
        if (pa->key != pb->key) return pa->key - pb->key;
        return pa->val - pb->val;
    }
    qsort(byY, coordsSize, sizeof(Pair), cmpByKeyVal);
    
    long long answer = -1;
    for (int i = 0; i < coordsSize;) {
        int y = byY[i].key;
        int minX = byY[i].val;
        int maxX = byY[i].val;
        int j = i;
        while (j < coordsSize && byY[j].key == y) {
            if (byY[j].val < minX) minX = byY[j].val;
            if (byY[j].val > maxX) maxX = byY[j].val;
            ++j;
        }
        if (maxX > minX) {
            long long base = (long long)(maxX - minX);
            long long height = globalMaxY - y;
            long long h2 = y - globalMinY;
            if (h2 > height) height = h2;
            long long area2 = base * height;
            if (area2 > answer) answer = area2;
        }
        i = j;
    }
    
    // Process groups with same x (vertical base)
    Pair *byX = (Pair*)malloc(sizeof(Pair) * coordsSize);
    for (int i = 0; i < coordsSize; ++i) {
        byX[i].key = xs[i];
        byX[i].val = ys[i];
    }
    qsort(byX, coordsSize, sizeof(Pair), cmpByKeyVal);
    
    for (int i = 0; i < coordsSize;) {
        int x = byX[i].key;
        int minY = byX[i].val;
        int maxY = byX[i].val;
        int j = i;
        while (j < coordsSize && byX[j].key == x) {
            if (byX[j].val < minY) minY = byX[j].val;
            if (byX[j].val > maxY) maxY = byX[j].val;
            ++j;
        }
        if (maxY > minY) {
            long long base = (long long)(maxY - minY);
            long long height = globalMaxX - x;
            long long h2 = x - globalMinX;
            if (h2 > height) height = h2;
            long long area2 = base * height;
            if (area2 > answer) answer = area2;
        }
        i = j;
    }
    
    free(xs);
    free(ys);
    free(byY);
    free(byX);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxArea(int[][] coords) {
        int n = coords.Length;
        if (n < 3) return -1;

        var dictY = new Dictionary<int, (int minX, int maxX)>();
        var dictX = new Dictionary<int, (int minY, int maxY)>();

        int globalMinY = int.MaxValue, globalMaxY = int.MinValue;
        int globalMinX = int.MaxValue, globalMaxX = int.MinValue;

        foreach (var p in coords) {
            int x = p[0];
            int y = p[1];

            if (x < globalMinX) globalMinX = x;
            if (x > globalMaxX) globalMaxX = x;
            if (y < globalMinY) globalMinY = y;
            if (y > globalMaxY) globalMaxY = y;

            if (!dictY.TryGetValue(y, out var valY)) {
                dictY[y] = (x, x);
            } else {
                int minX = Math.Min(valY.minX, x);
                int maxX = Math.Max(valY.maxX, x);
                dictY[y] = (minX, maxX);
            }

            if (!dictX.TryGetValue(x, out var valX)) {
                dictX[x] = (y, y);
            } else {
                int minY = Math.Min(valX.minY, y);
                int maxY = Math.Max(valX.maxY, y);
                dictX[x] = (minY, maxY);
            }
        }

        long ans = -1;

        foreach (var kvp in dictY) {
            int y = kvp.Key;
            var (minX, maxX) = kvp.Value;
            int baseLen = maxX - minX;
            if (baseLen == 0) continue;
            int height = Math.Max(globalMaxY - y, y - globalMinY);
            if (height == 0) continue;
            long area2 = (long)baseLen * height;
            if (area2 > ans) ans = area2;
        }

        foreach (var kvp in dictX) {
            int x = kvp.Key;
            var (minY, maxY) = kvp.Value;
            int baseLen = maxY - minY;
            if (baseLen == 0) continue;
            int height = Math.Max(globalMaxX - x, x - globalMinX);
            if (height == 0) continue;
            long area2 = (long)baseLen * height;
            if (area2 > ans) ans = area2;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} coords
 * @return {number}
 */
var maxArea = function(coords) {
    let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
    const mapY = new Map(); // y -> [minX, maxX]
    const mapX = new Map(); // x -> [minY, maxY]

    for (const [x, y] of coords) {
        if (x < minX) minX = x;
        if (x > maxX) maxX = x;
        if (y < minY) minY = y;
        if (y > maxY) maxY = y;

        let arrY = mapY.get(y);
        if (!arrY) {
            mapY.set(y, [x, x]);
        } else {
            if (x < arrY[0]) arrY[0] = x;
            if (x > arrY[1]) arrY[1] = x;
        }

        let arrX = mapX.get(x);
        if (!arrX) {
            mapX.set(x, [y, y]);
        } else {
            if (y < arrX[0]) arrX[0] = y;
            if (y > arrX[1]) arrX[1] = y;
        }
    }

    let ans = 0;

    for (const [y, [minXy, maxXy]] of mapY.entries()) {
        const base = maxXy - minXy;
        if (base <= 0) continue; // need at least two distinct points on this horizontal line
        const height = Math.max(maxY - y, y - minY);
        if (height <= 0) continue;
        const area2 = base * height;
        if (area2 > ans) ans = area2;
    }

    for (const [x, [minYx, maxYx]] of mapX.entries()) {
        const base = maxYx - minYx;
        if (base <= 0) continue; // need at least two distinct points on this vertical line
        const height = Math.max(maxX - x, x - minX);
        if (height <= 0) continue;
        const area2 = base * height;
        if (area2 > ans) ans = area2;
    }

    return ans === 0 ? -1 : ans;
};
```

## Typescript

```typescript
function maxArea(coords: number[][]): number {
    const mapY = new Map<number, { min: number; max: number }>();
    const mapX = new Map<number, { min: number; max: number }>();
    let globalMinY = Infinity,
        globalMaxY = -Infinity;
    let globalMinX = Infinity,
        globalMaxX = -Infinity;

    for (const [x, y] of coords) {
        // update per y
        const yEntry = mapY.get(y);
        if (!yEntry) {
            mapY.set(y, { min: x, max: x });
        } else {
            if (x < yEntry.min) yEntry.min = x;
            if (x > yEntry.max) yEntry.max = x;
        }

        // update per x
        const xEntry = mapX.get(x);
        if (!xEntry) {
            mapX.set(x, { min: y, max: y });
        } else {
            if (y < xEntry.min) xEntry.min = y;
            if (y > xEntry.max) xEntry.max = y;
        }

        // global extremes
        if (x < globalMinX) globalMinX = x;
        if (x > globalMaxX) globalMaxX = x;
        if (y < globalMinY) globalMinY = y;
        if (y > globalMaxY) globalMaxY = y;
    }

    let ans = -1;

    // horizontal side (same y)
    for (const [y, { min, max }] of mapY.entries()) {
        const base = max - min;
        if (base === 0) continue; // need two distinct points
        const height = Math.max(Math.abs(globalMaxY - y), Math.abs(globalMinY - y));
        if (height === 0) continue;
        const area2 = base * height;
        if (area2 > ans) ans = area2;
    }

    // vertical side (same x)
    for (const [x, { min, max }] of mapX.entries()) {
        const base = max - min;
        if (base === 0) continue;
        const height = Math.max(Math.abs(globalMaxX - x), Math.abs(globalMinX - x));
        if (height === 0) continue;
        const area2 = base * height;
        if (area2 > ans) ans = area2;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $coords
     * @return Integer
     */
    function maxArea($coords) {
        $minXByY = [];
        $maxXByY = [];
        $minYByX = [];
        $maxYByX = [];

        $globalMinY = PHP_INT_MAX;
        $globalMaxY = PHP_INT_MIN;
        $globalMinX = PHP_INT_MAX;
        $globalMaxX = PHP_INT_MIN;

        foreach ($coords as $pt) {
            $x = $pt[0];
            $y = $pt[1];

            if (!isset($minXByY[$y])) {
                $minXByY[$y] = $maxXByY[$y] = $x;
            } else {
                if ($x < $minXByY[$y]) $minXByY[$y] = $x;
                if ($x > $maxXByY[$y]) $maxXByY[$y] = $x;
            }

            if (!isset($minYByX[$x])) {
                $minYByX[$x] = $maxYByX[$x] = $y;
            } else {
                if ($y < $minYByX[$x]) $minYByX[$x] = $y;
                if ($y > $maxYByX[$x]) $maxYByX[$x] = $y;
            }

            if ($y < $globalMinY) $globalMinY = $y;
            if ($y > $globalMaxY) $globalMaxY = $y;
            if ($x < $globalMinX) $globalMinX = $x;
            if ($x > $globalMaxX) $globalMaxX = $x;
        }

        $ans = -1;

        foreach ($minXByY as $y => $minX) {
            $maxX = $maxXByY[$y];
            $base = $maxX - $minX;
            if ($base <= 0) continue;
            $height = max($globalMaxY - $y, $y - $globalMinY);
            if ($height <= 0) continue;
            $area2 = $base * $height;
            if ($area2 > $ans) $ans = $area2;
        }

        foreach ($minYByX as $x => $minY) {
            $maxY = $maxYByX[$x];
            $base = $maxY - $minY;
            if ($base <= 0) continue;
            $height = max($globalMaxX - $x, $x - $globalMinX);
            if ($height <= 0) continue;
            $area2 = $base * $height;
            if ($area2 > $ans) $ans = $area2;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxArea(_ coords: [[Int]]) -> Int {
        var minXForY = [Int: Int]()
        var maxXForY = [Int: Int]()
        var minYForX = [Int: Int]()
        var maxYForX = [Int: Int]()
        
        var globalMinY = Int.max
        var globalMaxY = Int.min
        var globalMinX = Int.max
        var globalMaxX = Int.min
        
        for point in coords {
            let x = point[0]
            let y = point[1]
            
            // Update Y maps
            if let curMin = minXForY[y] {
                if x < curMin { minXForY[y] = x }
            } else {
                minXForY[y] = x
            }
            if let curMax = maxXForY[y] {
                if x > curMax { maxXForY[y] = x }
            } else {
                maxXForY[y] = x
            }
            
            // Update X maps
            if let curMin = minYForX[x] {
                if y < curMin { minYForX[x] = y }
            } else {
                minYForX[x] = y
            }
            if let curMax = maxYForX[x] {
                if y > curMax { maxYForX[x] = y }
            } else {
                maxYForX[x] = y
            }
            
            // Global extremes
            if y < globalMinY { globalMinY = y }
            if y > globalMaxY { globalMaxY = y }
            if x < globalMinX { globalMinX = x }
            if x > globalMaxX { globalMaxX = x }
        }
        
        var answer = -1
        
        // Horizontal bases (same y)
        for (y, minX) in minXForY {
            guard let maxX = maxXForY[y] else { continue }
            let base = maxX - minX
            if base <= 0 { continue }
            var height = 0
            if globalMinY < y { height = max(height, y - globalMinY) }
            if globalMaxY > y { height = max(height, globalMaxY - y) }
            if height == 0 { continue }
            let area2 = base * height
            if area2 > answer { answer = area2 }
        }
        
        // Vertical bases (same x)
        for (x, minY) in minYForX {
            guard let maxY = maxYForX[x] else { continue }
            let base = maxY - minY
            if base <= 0 { continue }
            var height = 0
            if globalMinX < x { height = max(height, x - globalMinX) }
            if globalMaxX > x { height = max(height, globalMaxX - x) }
            if height == 0 { continue }
            let area2 = base * height
            if area2 > answer { answer = area2 }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxArea(coords: Array<IntArray>): Long {
        var minY = Int.MAX_VALUE
        var maxY = Int.MIN_VALUE
        var minX = Int.MAX_VALUE
        var maxX = Int.MIN_VALUE

        val yMap = HashMap<Int, Pair<Int, Int>>() // y -> (minX, maxX)
        val xMap = HashMap<Int, Pair<Int, Int>>() // x -> (minY, maxY)

        for (pt in coords) {
            val x = pt[0]
            val y = pt[1]

            if (x < minX) minX = x
            if (x > maxX) maxX = x
            if (y < minY) minY = y
            if (y > maxY) maxY = y

            // update yMap
            val curY = yMap[y]
            if (curY == null) {
                yMap[y] = Pair(x, x)
            } else {
                var mn = curY.first
                var mx = curY.second
                if (x < mn) mn = x
                if (x > mx) mx = x
                yMap[y] = Pair(mn, mx)
            }

            // update xMap
            val curX = xMap[x]
            if (curX == null) {
                xMap[x] = Pair(y, y)
            } else {
                var mn = curX.first
                var mx = curX.second
                if (y < mn) mn = y
                if (y > mx) mx = y
                xMap[x] = Pair(mn, mx)
            }
        }

        var ans: Long = -1

        // Horizontal bases (same y)
        for ((y, pair) in yMap) {
            val minXy = pair.first
            val maxXy = pair.second
            if (maxXy > minXy) { // at least two points on this y
                val base = (maxXy - minXy).toLong()
                val height = kotlin.math.max(y - minY, maxY - y).toLong()
                if (height > 0) {
                    val area2 = base * height
                    if (area2 > ans) ans = area2
                }
            }
        }

        // Vertical bases (same x)
        for ((x, pair) in xMap) {
            val minYx = pair.first
            val maxYx = pair.second
            if (maxYx > minYx) { // at least two points on this x
                val base = (maxYx - minYx).toLong()
                val height = kotlin.math.max(x - minX, maxX - x).toLong()
                if (height > 0) {
                    val area2 = base * height
                    if (area2 > ans) ans = area2
                }
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxArea(List<List<int>> coords) {
    int globalMinX = 1 << 60;
    int globalMaxX = -1;
    int globalMinY = 1 << 60;
    int globalMaxY = -1;

    final Map<int, int> yMinX = {};
    final Map<int, int> yMaxX = {};

    final Map<int, int> xMinY = {};
    final Map<int, int> xMaxY = {};

    for (var p in coords) {
      int x = p[0];
      int y = p[1];

      if (x < globalMinX) globalMinX = x;
      if (x > globalMaxX) globalMaxX = x;
      if (y < globalMinY) globalMinY = y;
      if (y > globalMaxY) globalMaxY = y;

      // Update maps for same y (horizontal base)
      if (!yMinX.containsKey(y)) {
        yMinX[y] = x;
        yMaxX[y] = x;
      } else {
        if (x < yMinX[y]!) yMinX[y] = x;
        if (x > yMaxX[y]!) yMaxX[y] = x;
      }

      // Update maps for same x (vertical base)
      if (!xMinY.containsKey(x)) {
        xMinY[x] = y;
        xMaxY[x] = y;
      } else {
        if (y < xMinY[x]!) xMinY[x] = y;
        if (y > xMaxY[x]!) xMaxY[x] = y;
      }
    }

    int maxArea2 = 0;

    // Horizontal side (same y)
    for (var entry in yMinX.entries) {
      int y = entry.key;
      int minX = entry.value;
      int maxX = yMaxX[y]!;
      if (maxX > minX) {
        int base = maxX - minX;
        int height = globalMaxY - y;
        int altHeight = y - globalMinY;
        if (altHeight > height) height = altHeight;
        if (height > 0) {
          int area2 = base * height;
          if (area2 > maxArea2) maxArea2 = area2;
        }
      }
    }

    // Vertical side (same x)
    for (var entry in xMinY.entries) {
      int x = entry.key;
      int minY = entry.value;
      int maxY = xMaxY[x]!;
      if (maxY > minY) {
        int base = maxY - minY;
        int height = globalMaxX - x;
        int altHeight = x - globalMinX;
        if (altHeight > height) height = altHeight;
        if (height > 0) {
          int area2 = base * height;
          if (area2 > maxArea2) maxArea2 = area2;
        }
      }
    }

    return maxArea2 == 0 ? -1 : maxArea2;
  }
}
```

## Golang

```go
func maxArea(coords [][]int) int64 {
	type pair struct{ min, max int }
	yMap := make(map[int]*pair)
	xMap := make(map[int]*pair)

	if len(coords) == 0 {
		return -1
	}
	minY, maxY := coords[0][1], coords[0][1]
	minX, maxX := coords[0][0], coords[0][0]

	for _, p := range coords {
		x, y := p[0], p[1]

		if y < minY {
			minY = y
		}
		if y > maxY {
			maxY = y
		}
		if x < minX {
			minX = x
		}
		if x > maxX {
			maxX = x
		}

		if v, ok := yMap[y]; ok {
			if x < v.min {
				v.min = x
			}
			if x > v.max {
				v.max = x
			}
		} else {
			yMap[y] = &pair{min: x, max: x}
		}

		if v, ok := xMap[x]; ok {
			if y < v.min {
				v.min = y
			}
			if y > v.max {
				v.max = y
			}
		} else {
			xMap[x] = &pair{min: y, max: y}
		}
	}

	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}

	var ans int64

	for y, p := range yMap {
		if p.max > p.min { // at least two points sharing this y
			base := int64(p.max - p.min)
			h1 := abs(y - minY)
			h2 := abs(y - maxY)
			height := h1
			if h2 > height {
				height = h2
			}
			if height > 0 {
				area2 := base * int64(height)
				if area2 > ans {
					ans = area2
				}
			}
		}
	}

	for x, p := range xMap {
		if p.max > p.min { // at least two points sharing this x
			base := int64(p.max - p.min)
			h1 := abs(x - minX)
			h2 := abs(x - maxX)
			height := h1
			if h2 > height {
				height = h2
			}
			if height > 0 {
				area2 := base * int64(height)
				if area2 > ans {
					ans = area2
				}
			}
		}
	}

	if ans == 0 {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def max_area(coords)
  y_map = {}
  x_map = {}

  global_min_x = Float::INFINITY
  global_max_x = -Float::INFINITY
  global_min_y = Float::INFINITY
  global_max_y = -Float::INFINITY

  coords.each do |pt|
    x, y = pt[0], pt[1]

    if y_map.key?(y)
      min_x, max_x, cnt = y_map[y]
      min_x = x if x < min_x
      max_x = x if x > max_x
      cnt += 1
    else
      min_x = max_x = x
      cnt = 1
    end
    y_map[y] = [min_x, max_x, cnt]

    if x_map.key?(x)
      min_y, max_y, cnt2 = x_map[x]
      min_y = y if y < min_y
      max_y = y if y > max_y
      cnt2 += 1
    else
      min_y = max_y = y
      cnt2 = 1
    end
    x_map[x] = [min_y, max_y, cnt2]

    global_min_x = x if x < global_min_x
    global_max_x = x if x > global_max_x
    global_min_y = y if y < global_min_y
    global_max_y = y if y > global_max_y
  end

  max_twice_area = -1

  y_map.each do |y, (min_x, max_x, cnt)|
    next if cnt < 2
    base = max_x - min_x
    height = [global_max_y - y, y - global_min_y].max
    next if height == 0
    area2 = base * height
    max_twice_area = area2 if area2 > max_twice_area
  end

  x_map.each do |x, (min_y, max_y, cnt)|
    next if cnt < 2
    base = max_y - min_y
    height = [global_max_x - x, x - global_min_x].max
    next if height == 0
    area2 = base * height
    max_twice_area = area2 if area2 > max_twice_area
  end

  max_twice_area
end
```

## Scala

```scala
object Solution {
  def maxArea(coords: Array[Array[Int]]): Long = {
    import scala.collection.mutable

    var minXGlobal = Int.MaxValue
    var maxXGlobal = Int.MinValue
    var minYGlobal = Int.MaxValue
    var maxYGlobal = Int.MinValue

    val yMap = mutable.HashMap[Int, (Int, Int)]() // y -> (minX, maxX)
    val xMap = mutable.HashMap[Int, (Int, Int)]() // x -> (minY, maxY)

    for (pt <- coords) {
      val x = pt(0)
      val y = pt(1)

      if (x < minXGlobal) minXGlobal = x
      if (x > maxXGlobal) maxXGlobal = x
      if (y < minYGlobal) minYGlobal = y
      if (y > maxYGlobal) maxYGlobal = y

      yMap.get(y) match {
        case Some((minX, maxX)) =>
          val newMin = if (x < minX) x else minX
          val newMax = if (x > maxX) x else maxX
          if (newMin != minX || newMax != maxX) yMap.update(y, (newMin, newMax))
        case None =>
          yMap.put(y, (x, x))
      }

      xMap.get(x) match {
        case Some((minY, maxY)) =>
          val newMin = if (y < minY) y else minY
          val newMax = if (y > maxY) y else maxY
          if (newMin != minY || newMax != maxY) xMap.update(x, (newMin, newMax))
        case None =>
          xMap.put(x, (y, y))
      }
    }

    var best: Long = -1L

    // Horizontal base (same y)
    for ((y, (minX, maxX)) <- yMap) {
      if (maxX > minX) {
        val base = maxX.toLong - minX.toLong
        val height = math.max(y - minYGlobal, maxYGlobal - y).toLong
        if (height > 0) {
          val area2 = base * height
          if (area2 > best) best = area2
        }
      }
    }

    // Vertical base (same x)
    for ((x, (minY, maxY)) <- xMap) {
      if (maxY > minY) {
        val base = maxY.toLong - minY.toLong
        val height = math.max(x - minXGlobal, maxXGlobal - x).toLong
        if (height > 0) {
          val area2 = base * height
          if (area2 > best) best = area2
        }
      }
    }

    best
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn max_area(coords: Vec<Vec<i32>>) -> i64 {
        if coords.len() < 3 {
            return -1;
        }

        let mut y_map: HashMap<i32, (i32, i32)> = HashMap::new(); // y -> (min_x, max_x)
        let mut x_map: HashMap<i32, (i32, i32)> = HashMap::new(); // x -> (min_y, max_y)

        let mut min_x = i32::MAX;
        let mut max_x = i32::MIN;
        let mut min_y = i32::MAX;
        let mut max_y = i32::MIN;

        for p in &coords {
            let x = p[0];
            let y = p[1];

            if x < min_x { min_x = x; }
            if x > max_x { max_x = x; }
            if y < min_y { min_y = y; }
            if y > max_y { max_y = y; }

            y_map.entry(y).and_modify(|e| {
                if x < e.0 { e.0 = x; }
                if x > e.1 { e.1 = x; }
            }).or_insert((x, x));

            x_map.entry(x).and_modify(|e| {
                if y < e.0 { e.0 = y; }
                if y > e.1 { e.1 = y; }
            }).or_insert((y, y));
        }

        let mut best: i64 = -1;

        // Horizontal base (same y)
        for (&y, &(min_x_at_y, max_x_at_y)) in &y_map {
            if min_x_at_y < max_x_at_y {
                let base = (max_x_at_y - min_x_at_y) as i64;
                let height = std::cmp::max(y - min_y, max_y - y) as i64;
                if height > 0 {
                    best = best.max(base * height);
                }
            }
        }

        // Vertical base (same x)
        for (&x, &(min_y_at_x, max_y_at_x)) in &x_map {
            if min_y_at_x < max_y_at_x {
                let base = (max_y_at_x - min_y_at_x) as i64;
                let height = std::cmp::max(x - min_x, max_x - x) as i64;
                if height > 0 {
                    best = best.max(base * height);
                }
            }
        }

        best
    }
}
```

## Racket

```racket
(define/contract (max-area coords)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((global-minX #f)
         (global-maxX #f)
         (global-minY #f)
         (global-maxY #f)
         (y-map (make-hash))
         (x-map (make-hash)))
    ;; First pass: collect min/max per coordinate and global extremes
    (for ([pt coords])
      (define x (first pt))
      (define y (second pt))
      (when (or (not global-minX) (< x global-minX)) (set! global-minX x))
      (when (or (not global-maxX) (> x global-maxX)) (set! global-maxX x))
      (when (or (not global-minY) (< y global-minY)) (set! global-minY y))
      (when (or (not global-maxY) (> y global-maxY)) (set! global-maxY y))
      ;; Update map for same y (horizontal base)
      (let ([vec (hash-ref y-map y #f)])
        (if vec
            (begin
              (when (< x (vector-ref vec 0)) (vector-set! vec 0 x))
              (when (> x (vector-ref vec 1)) (vector-set! vec 1 x)))
            (hash-set! y-map y (vector x x))))
      ;; Update map for same x (vertical base)
      (let ([vec (hash-ref x-map x #f)])
        (if vec
            (begin
              (when (< y (vector-ref vec 0)) (vector-set! vec 0 y))
              (when (> y (vector-ref vec 1)) (vector-set! vec 1 y)))
            (hash-set! x-map x (vector y y)))))
    ;; Compute maximum doubled area
    (define ans -1)
    ;; Horizontal bases (same y)
    (for ([kv (in-hash y-map)])
      (define y (car kv))
      (define vec (cdr kv))
      (define minX (vector-ref vec 0))
      (define maxX (vector-ref vec 1))
      (when (> maxX minX) ; at least two points sharing this y
        (define base (- maxX minX))
        (define height (max (- y global-minY) (- global-maxY y)))
        (when (> height 0)
          (define area2 (* base height))
          (when (> area2 ans) (set! ans area2)))))
    ;; Vertical bases (same x)
    (for ([kv (in-hash x-map)])
      (define x (car kv))
      (define vec (cdr kv))
      (define minY (vector-ref vec 0))
      (define maxY (vector-ref vec 1))
      (when (> maxY minY) ; at least two points sharing this x
        (define base (- maxY minY))
        (define height (max (- x global-minX) (- global-maxX x)))
        (when (> height 0)
          (define area2 (* base height))
          (when (> area2 ans) (set! ans area2)))))
    ans))
```

## Erlang

```erlang
-spec max_area(Coords :: [[integer()]]) -> integer().
max_area(Coords) ->
    Init = #{min_x => 10000000, max_x => -1,
             min_y => 10000000, max_y => -1,
             y_map => #{}, x_map => #{}},
    State = lists:foldl(fun([X,Y], Acc) ->
                MinX0 = maps:get(min_x, Acc),
                MaxX0 = maps:get(max_x, Acc),
                MinY0 = maps:get(min_y, Acc),
                MaxY0 = maps:get(max_y, Acc),
                YMap0 = maps:get(y_map, Acc),
                XMap0 = maps:get(x_map, Acc),

                NewMinX = erlang:min(MinX0, X),
                NewMaxX = erlang:max(MaxX0, X),
                NewMinY = erlang:min(MinY0, Y),
                NewMaxY = erlang:max(MaxY0, Y),

                OldYVal = maps:get(Y, YMap0, undefined),
                NewYVal = case OldYVal of
                    undefined -> {X,X};
                    {MinXY, MaxXY} -> {erlang:min(MinXY, X), erlang:max(MaxXY, X)}
                end,
                NewYMap = maps:put(Y, NewYVal, YMap0),

                OldXVal = maps:get(X, XMap0, undefined),
                NewXVal = case OldXVal of
                    undefined -> {Y,Y};
                    {MinYX, MaxYX} -> {erlang:min(MinYX, Y), erlang:max(MaxYX, Y)}
                end,
                NewXMap = maps:put(X, NewXVal, XMap0),

                Acc#{min_x => NewMinX, max_x => NewMaxX,
                     min_y => NewMinY, max_y => NewMaxY,
                     y_map => NewYMap, x_map => NewXMap}
            end, Init, Coords),

    MinYGlobal = maps:get(min_y, State),
    MaxYGlobal = maps:get(max_y, State),
    MinXGlobal = maps:get(min_x, State),
    MaxXGlobal = maps:get(max_x, State),
    YMap = maps:get(y_map, State),
    XMap = maps:get(x_map, State),

    Ans0 = -1,
    Ans1 = maps:fold(fun(Y,{MinX,MaxX},Acc) ->
                Base = MaxX - MinX,
                if Base =< 0 -> Acc;
                   true ->
                       Height = erlang:max(erlang:abs(Y - MinYGlobal), erlang:abs(Y - MaxYGlobal)),
                       Prod = Base * Height,
                       erlang:max(Acc, Prod)
                end
            end, Ans0, YMap),

    Ans2 = maps:fold(fun(X,{MinY,MaxY},Acc) ->
                Base = MaxY - MinY,
                if Base =< 0 -> Acc;
                   true ->
                       Height = erlang:max(erlang:abs(X - MinXGlobal), erlang:abs(X - MaxXGlobal)),
                       Prod = Base * Height,
                       erlang:max(Acc, Prod)
                end
            end, Ans1, XMap),

    Ans2.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_area(coords :: [[integer]]) :: integer
  def max_area(coords) do
    {y_map, x_map, min_y, max_y, min_x, max_x} =
      Enum.reduce(coords, {%{}, %{}, nil, nil, nil, nil}, fn [x, y],
                                                            {ym, xm, miY, maY, miX, maX} ->
        ym = Map.update(ym, y, {x, x}, fn {minx, maxx} -> {min(minx, x), max(maxx, x)} end)
        xm = Map.update(xm, x, {y, y}, fn {miny, maxy} -> {min(miny, y), max(maxy, y)} end)

        miY = if miY == nil or y < miY, do: y, else: miY
        maY = if maY == nil or y > maY, do: y, else: maY
        miX = if miX == nil or x < miX, do: x, else: miX
        maX = if maX == nil or x > maX, do: x, else: maX

        {ym, xm, miY, maY, miX, maX}
      end)

    ans_y =
      Enum.reduce(y_map, 0, fn {y, {minx, maxx}}, acc ->
        base = maxx - minx
        if base > 0 do
          height = max(abs(max_y - y), abs(min_y - y))
          if height > 0, do: max(acc, base * height), else: acc
        else
          acc
        end
      end)

    ans =
      Enum.reduce(x_map, ans_y, fn {x, {miny, maxy}}, acc ->
        base = maxy - miny
        if base > 0 do
          height = max(abs(max_x - x), abs(min_x - x))
          if height > 0, do: max(acc, base * height), else: acc
        else
          acc
        end
      end)

    if ans == 0, do: -1, else: ans
  end
end
```

# 0963. Minimum Area Rectangle II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Key {
        int mx, my;
        long long d;
        bool operator==(const Key& other) const noexcept {
            return mx == other.mx && my == other.my && d == other.d;
        }
    };
    struct KeyHash {
        size_t operator()(const Key& k) const noexcept {
            size_t h1 = std::hash<int>()(k.mx);
            size_t h2 = std::hash<int>()(k.my);
            size_t h3 = std::hash<long long>()(k.d);
            size_t res = h1;
            res ^= h2 + 0x9e3779b97f4a7c15ULL + (res << 6) + (res >> 2);
            res ^= h3 + 0x9e3779b97f4a7c15ULL + (res << 6) + (res >> 2);
            return res;
        }
    };
    
    double minAreaFreeRect(vector<vector<int>>& points) {
        int n = points.size();
        unordered_map<Key, vector<pair<int,int>>, KeyHash> mp;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long long dx = (long long)points[i][0] - points[j][0];
                long long dy = (long long)points[i][1] - points[j][1];
                long long dist2 = dx * dx + dy * dy;
                int mx = points[i][0] + points[j][0]; // midpoint multiplied by 2
                int my = points[i][1] + points[j][1];
                Key key{mx, my, dist2};
                mp[key].push_back({i, j});
            }
        }
        double ans = numeric_limits<double>::infinity();
        for (auto& entry : mp) {
            const auto& vec = entry.second;
            int m = vec.size();
            for (int a = 0; a < m; ++a) {
                for (int b = a + 1; b < m; ++b) {
                    int i = vec[a].first, j = vec[a].second;
                    int k = vec[b].first, l = vec[b].second;
                    
                    long long x1 = points[i][0], y1 = points[i][1];
                    long long x2 = points[k][0], y2 = points[k][1];
                    long long x3 = points[l][0], y3 = points[l][1];
                    
                    long long cross = llabs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1));
                    if (cross > 0) {
                        ans = min(ans, static_cast<double>(cross));
                    }
                }
            }
        }
        return ans == numeric_limits<double>::infinity() ? 0.0 : ans;
    }
};
```

## Java

```java
class Solution {
    private static class Key {
        final int sumX;
        final int sumY;
        final long dist2;
        Key(int sumX, int sumY, long dist2) {
            this.sumX = sumX;
            this.sumY = sumY;
            this.dist2 = dist2;
        }
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Key)) return false;
            Key k = (Key) o;
            return sumX == k.sumX && sumY == k.sumY && dist2 == k.dist2;
        }
        @Override
        public int hashCode() {
            int h = Integer.hashCode(sumX);
            h = 31 * h + Integer.hashCode(sumY);
            h = 31 * h + Long.hashCode(dist2);
            return h;
        }
    }

    public double minAreaFreeRect(int[][] points) {
        int n = points.length;
        java.util.Map<Key, java.util.List<int[]>> map = new java.util.HashMap<>();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int sumX = points[i][0] + points[j][0];
                int sumY = points[i][1] + points[j][1];
                long dx = points[i][0] - points[j][0];
                long dy = points[i][1] - points[j][1];
                long dist2 = dx * dx + dy * dy;
                Key key = new Key(sumX, sumY, dist2);
                map.computeIfAbsent(key, k -> new java.util.ArrayList<>()).add(new int[]{i, j});
            }
        }

        double minArea = Double.MAX_VALUE;

        for (java.util.List<int[]> list : map.values()) {
            int m = list.size();
            if (m < 2) continue;
            for (int a = 0; a < m; ++a) {
                int[] p1 = list.get(a);
                for (int b = a + 1; b < m; ++b) {
                    int[] p2 = list.get(b);
                    // vertices: p1[0] opposite p1[1]; p2[0] and p2[1] are the other diagonal
                    int i1 = p1[0];
                    int j1 = p1[1];
                    int i2 = p2[0];
                    // compute area using points i1, i2, j1
                    long ax = points[i1][0];
                    long ay = points[i1][1];
                    long bx = points[i2][0];
                    long by = points[i2][1];
                    long cx = points[j1][0];
                    long cy = points[j1][1];

                    long cross = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
                    double area = Math.abs(cross);
                    if (area < minArea && area > 0) {
                        minArea = area;
                    }
                }
            }
        }

        return minArea == Double.MAX_VALUE ? 0.0 : minArea;
    }
}
```

## Python

```python
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        pts = [tuple(p) for p in points]
        from collections import defaultdict
        groups = defaultdict(list)

        # Build groups by midpoint (twice) and squared diagonal length
        for i in range(n):
            x1, y1 = pts[i]
            for j in range(i + 1, n):
                x2, y2 = pts[j]
                mx = x1 + x2          # twice the midpoint x
                my = y1 + y2          # twice the midpoint y
                dx = x1 - x2
                dy = y1 - y2
                dist2 = dx * dx + dy * dy
                groups[(mx, my, dist2)].append((i, j))

        min_area = float('inf')

        # For each group, try all pair combinations
        for lst in groups.values():
            m = len(lst)
            if m < 2:
                continue
            for a in range(m):
                i1, i2 = lst[a]
                ax, ay = pts[i1]
                for b in range(a + 1, m):
                    j1, j2 = lst[b]
                    # ensure four distinct points
                    if len({i1, i2, j1, j2}) < 4:
                        continue
                    bx, by = pts[j1]
                    dx_, dy_ = pts[j2]

                    # vectors from A to the two vertices of the other diagonal
                    vx = bx - ax
                    vy = by - ay
                    wx = dx_ - ax
                    wy = dy_ - ay

                    area = abs(vx * wy - vy * wx)
                    if area < min_area and area > 0:
                        min_area = area

        return 0.0 if min_area == float('inf') else float(min_area)
```

## Python3

```python
class Solution:
    def minAreaFreeRect(self, points):
        from collections import defaultdict
        n = len(points)
        pts = [tuple(p) for p in points]
        groups = defaultdict(list)
        min_area = float('inf')
        for i in range(n):
            x1, y1 = pts[i]
            for j in range(i + 1, n):
                x2, y2 = pts[j]
                mx = x1 + x2          # twice midpoint x
                my = y1 + y2          # twice midpoint y
                dx = x1 - x2
                dy = y1 - y2
                dist2 = dx * dx + dy * dy
                key = (mx, my, dist2)
                for a, b in groups[key]:
                    ax, ay = pts[a]
                    bx, by = pts[b]
                    # compute area using points: a,b,i,j where (i,j) is current pair
                    # a and i are opposite corners, b and j are opposite corners
                    # use vectors from a to b and a to j
                    cross = (bx - ax) * (y2 - ay) - (by - ay) * (x2 - ax)
                    area = abs(cross)
                    if area:
                        min_area = min(min_area, area)
                groups[key].append((i, j))
        return 0.0 if min_area == float('inf') else min_area / 1.0
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <math.h>

typedef struct {
    int midX;
    int midY;
    long long dist2;
    int dx;
    int dy;
} PairInfo;

static int cmpPair(const void *a, const void *b) {
    const PairInfo *p = (const PairInfo *)a;
    const PairInfo *q = (const PairInfo *)b;
    if (p->midX != q->midX) return p->midX - q->midX;
    if (p->midY != q->midY) return p->midY - q->midY;
    if (p->dist2 < q->dist2) return -1;
    if (p->dist2 > q->dist2) return 1;
    return 0;
}

double minAreaFreeRect(int** points, int pointsSize, int* pointsColSize){
    int n = pointsSize;
    int maxPairs = n * (n - 1) / 2;
    PairInfo *pairs = (PairInfo *)malloc(sizeof(PairInfo) * maxPairs);
    int idx = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[j][0];
            int y2 = points[j][1];
            int dx = x1 - x2;
            int dy = y1 - y2;
            pairs[idx].midX = x1 + x2;          // sum, not average
            pairs[idx].midY = y1 + y2;
            pairs[idx].dist2 = (long long)dx * dx + (long long)dy * dy;
            pairs[idx].dx = dx;
            pairs[idx].dy = dy;
            ++idx;
        }
    }

    qsort(pairs, idx, sizeof(PairInfo), cmpPair);

    double minArea = DBL_MAX;

    int start = 0;
    while (start < idx) {
        int end = start + 1;
        while (end < idx &&
               pairs[end].midX == pairs[start].midX &&
               pairs[end].midY == pairs[start].midY &&
               pairs[end].dist2 == pairs[start].dist2) {
            ++end;
        }
        // evaluate all combinations within [start, end)
        for (int i = start; i < end; ++i) {
            for (int j = i + 1; j < end; ++j) {
                long long cross = (long long)pairs[i].dx * pairs[j].dy -
                                  (long long)pairs[i].dy * pairs[j].dx;
                double area = fabs((double)cross) / 2.0;
                if (area > 0 && area < minArea) {
                    minArea = area;
                }
            }
        }
        start = end;
    }

    free(pairs);
    return (minArea == DBL_MAX) ? 0.0 : minArea;
}
```

## Csharp

```csharp
public class Solution {
    public double MinAreaFreeRect(int[][] points) {
        int n = points.Length;
        var dict = new Dictionary<(int sumX, int sumY, long dist2), List<(int i, int j)>>();
        double minArea = double.MaxValue;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int sumX = points[i][0] + points[j][0];
                int sumY = points[i][1] + points[j][1];
                long dx = (long)points[i][0] - points[j][0];
                long dy = (long)points[i][1] - points[j][1];
                long dist2 = dx * dx + dy * dy;
                var key = (sumX, sumY, dist2);

                if (!dict.TryGetValue(key, out var list)) {
                    list = new List<(int i, int j)>();
                    dict[key] = list;
                } else {
                    foreach (var pair in list) {
                        int a = pair.i;
                        int b = pair.j;

                        long cross = Math.Abs(
                            ((long)points[a][0] - points[i][0]) * ((long)points[b][1] - points[i][1]) -
                            ((long)points[a][1] - points[i][1]) * ((long)points[b][0] - points[i][0])
                        );

                        if (cross > 0 && cross < minArea) {
                            minArea = cross;
                        }
                    }
                }

                list.Add((i, j));
            }
        }

        return minArea == double.MaxValue ? 0.0 : minArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var minAreaFreeRect = function(points) {
    const n = points.length;
    const map = new Map(); // key -> array of pairs {i,j}
    
    for (let i = 0; i < n; ++i) {
        const [x1, y1] = points[i];
        for (let j = i + 1; j < n; ++j) {
            const [x2, y2] = points[j];
            const midX = x1 + x2; // use sum to avoid fractions
            const midY = y1 + y2;
            const dx = x1 - x2;
            const dy = y1 - y2;
            const dist2 = dx * dx + dy * dy;
            const key = `${midX},${midY},${dist2}`;
            if (!map.has(key)) map.set(key, []);
            map.get(key).push({i, j});
        }
    }
    
    let minArea = Infinity;
    
    for (const pairs of map.values()) {
        const m = pairs.length;
        if (m < 2) continue;
        for (let a = 0; a < m; ++a) {
            const p1 = pairs[a];
            for (let b = a + 1; b < m; ++b) {
                const p2 = pairs[b];
                // ensure four distinct points
                if (p1.i === p2.i || p1.i === p2.j ||
                    p1.j === p2.i || p1.j === p2.j) continue;
                
                const xA = points[p1.i][0];
                const yA = points[p1.i][1];
                
                const xC = points[p2.i][0];
                const yC = points[p2.i][1];
                
                const xD = points[p2.j][0];
                const yD = points[p2.j][1];
                
                const vx1 = xA - xC;
                const vy1 = yA - yC;
                const vx2 = xA - xD;
                const vy2 = yA - yD;
                
                const area = Math.abs(vx1 * vy2 - vy1 * vx2);
                if (area < minArea) minArea = area;
            }
        }
    }
    
    return minArea === Infinity ? 0 : minArea;
};
```

## Typescript

```typescript
function minAreaFreeRect(points: number[][]): number {
    const n = points.length;
    const map = new Map<string, [number, number][]>();

    for (let i = 0; i < n; i++) {
        const [x1, y1] = points[i];
        for (let j = i + 1; j < n; j++) {
            const [x2, y2] = points[j];
            const mx = x1 + x2; // twice midpoint x
            const my = y1 + y2; // twice midpoint y
            const dx = x1 - x2;
            const dy = y1 - y2;
            const distSq = dx * dx + dy * dy;
            const key = `${mx},${my},${distSq}`;
            if (!map.has(key)) map.set(key, []);
            map.get(key)!.push([i, j]);
        }
    }

    let minArea = Infinity;

    for (const pairs of map.values()) {
        const m = pairs.length;
        if (m < 2) continue;
        for (let a = 0; a < m; a++) {
            const [i1] = pairs[a];
            const p1 = points[i1];
            for (let b = a + 1; b < m; b++) {
                const [, j2] = pairs[b];
                const p3 = points[pairs[b][0]];
                const p4 = points[j2];

                const v13x = p3[0] - p1[0];
                const v13y = p3[1] - p1[1];
                const v14x = p4[0] - p1[0];
                const v14y = p4[1] - p1[1];

                const area = Math.abs(v13x * v14y - v13y * v14x);
                if (area > 0 && area < minArea) {
                    minArea = area;
                }
            }
        }
    }

    return minArea === Infinity ? 0 : minArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Float
     */
    function minAreaFreeRect($points) {
        $n = count($points);
        $map = [];
        $minArea = INF;

        for ($i = 0; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                $mx = $points[$i][0] + $points[$j][0];
                $my = $points[$i][1] + $points[$j][1];
                $dx = $points[$i][0] - $points[$j][0];
                $dy = $points[$i][1] - $points[$j][1];
                $dist = $dx * $dx + $dy * $dy;
                $key = $mx . ',' . $my . ',' . $dist;

                if (isset($map[$key])) {
                    foreach ($map[$key] as $pair) {
                        $a = $pair[0];
                        $b = $pair[1];

                        $p1 = $points[$i];
                        $q1 = $points[$a];
                        $q2 = $points[$b];

                        $area = abs(
                            ($p1[0] - $q1[0]) * ($p1[1] - $q2[1]) -
                            ($p1[1] - $q1[1]) * ($p1[0] - $q2[0])
                        );

                        if ($area > 0 && $area < $minArea) {
                            $minArea = $area;
                        }
                    }
                    $map[$key][] = [$i, $j];
                } else {
                    $map[$key] = [[$i, $j]];
                }
            }
        }

        return $minArea === INF ? 0.0 : (float)$minArea;
    }
}
```

## Swift

```swift
class Solution {
    func minAreaFreeRect(_ points: [[Int]]) -> Double {
        let n = points.count
        var pts = [(Int, Int)]()
        for p in points { pts.append((p[0], p[1])) }
        
        struct Key: Hashable {
            let sumX: Int
            let sumY: Int
            let dist: Int
        }
        
        var groups = [Key: [(Int, Int)]]()
        for i in 0..<n {
            for j in i+1..<n {
                let sumX = pts[i].0 + pts[j].0
                let sumY = pts[i].1 + pts[j].1
                let dx = pts[i].0 - pts[j].0
                let dy = pts[i].1 - pts[j].1
                let dist = dx * dx + dy * dy
                let key = Key(sumX: sumX, sumY: sumY, dist: dist)
                groups[key, default: []].append((i, j))
            }
        }
        
        var minArea = Double.greatestFiniteMagnitude
        
        for list in groups.values where list.count > 1 {
            let m = list.count
            for a in 0..<m {
                let (i1, _) = list[a]
                for b in a+1..<m {
                    let (i2, j2) = list[b]
                    // ensure four distinct points
                    var uniq = Set<Int>()
                    uniq.insert(i1)
                    uniq.insert(list[a].1)
                    uniq.insert(i2)
                    uniq.insert(j2)
                    if uniq.count < 4 { continue }
                    
                    let ax = pts[i1].0, ay = pts[i1].1
                    let cx = pts[i2].0, cy = pts[i2].1
                    let dx = pts[j2].0, dy = pts[j2].1
                    
                    let cross = (cx - ax) * (dy - ay) - (cy - ay) * (dx - ax)
                    let area = abs(cross)
                    if area > 0 {
                        minArea = min(minArea, Double(area))
                    }
                }
            }
        }
        
        return minArea == Double.greatestFiniteMagnitude ? 0.0 : minArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minAreaFreeRect(points: Array<IntArray>): Double {
        val n = points.size
        data class Key(val mx: Int, val my: Int, val dist: Long)
        val map = HashMap<Key, MutableList<Pair<Int, Int>>>()
        for (i in 0 until n) {
            val xi = points[i][0]
            val yi = points[i][1]
            for (j in i + 1 until n) {
                val xj = points[j][0]
                val yj = points[j][1]
                val mx = xi + xj
                val my = yi + yj
                val dx = xi - xj
                val dy = yi - yj
                val dist = dx.toLong() * dx + dy.toLong() * dy
                val key = Key(mx, my, dist)
                map.getOrPut(key) { mutableListOf() }.add(Pair(i, j))
            }
        }
        var minArea = Double.MAX_VALUE
        for (list in map.values) {
            if (list.size < 2) continue
            val size = list.size
            for (aIdx in 0 until size) {
                val p1 = list[aIdx]
                for (bIdx in aIdx + 1 until size) {
                    val p2 = list[bIdx]
                    // ensure four distinct points
                    if (p1.first == p2.first || p1.first == p2.second ||
                        p1.second == p2.first || p1.second == p2.second) continue
                    val ax = points[p1.first][0]
                    val ay = points[p1.first][1]
                    val bx = points[p2.first][0]
                    val by = points[p2.first][1]
                    val dx = points[p2.second][0]
                    val dy = points[p2.second][1]
                    val cross = (bx - ax).toLong() * (dy - ay) - (by - ay).toLong() * (dx - ax)
                    val area = kotlin.math.abs(cross).toDouble()
                    if (area < minArea && area > 0) {
                        minArea = area
                    }
                }
            }
        }
        return if (minArea == Double.MAX_VALUE) 0.0 else minArea
    }
}
```

## Dart

```dart
class Solution {
  double minAreaFreeRect(List<List<int>> points) {
    int n = points.length;
    const double INF = double.infinity;
    double minArea = INF;

    // Map key: "midX,midY,dist"
    final Map<String, List<List<int>>> map = {};

    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        int midX = points[i][0] + points[j][0];
        int midY = points[i][1] + points[j][1];
        int dx = points[i][0] - points[j][0];
        int dy = points[i][1] - points[j][1];
        int dist = dx * dx + dy * dy;
        String key = '$midX,$midY,$dist';

        if (map.containsKey(key)) {
          for (var pair in map[key]!) {
            int k = pair[0];
            int l = pair[1];

            int vx1 = points[i][0] - points[k][0];
            int vy1 = points[i][1] - points[k][1];
            int vx2 = points[i][0] - points[l][0];
            int vy2 = points[i][1] - points[l][1];

            int cross = vx1 * vy2 - vy1 * vx2;
            double area = cross.abs().toDouble();
            if (area > 0 && area < minArea) {
              minArea = area;
            }
          }
          map[key]!.add([i, j]);
        } else {
          map[key] = [
            [i, j]
          ];
        }
      }
    }

    return minArea == INF ? 0.0 : minArea;
  }
}
```

## Golang

```go
import "math"

type pair struct {
	i, j int
}

type key struct {
	sumX int
	sumY int
	dist int64
}

func minAreaFreeRect(points [][]int) float64 {
	n := len(points)
	groups := make(map[key][]pair)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			sumX := points[i][0] + points[j][0]
			sumY := points[i][1] + points[j][1]
			dx := points[i][0] - points[j][0]
			dy := points[i][1] - points[j][1]
			dist := int64(dx*dx + dy*dy)
			k := key{sumX, sumY, dist}
			groups[k] = append(groups[k], pair{i, j})
		}
	}

	minArea := math.MaxFloat64
	for _, list := range groups {
		if len(list) < 2 {
			continue
		}
		for a := 0; a < len(list); a++ {
			for b := a + 1; b < len(list); b++ {
				p1 := points[list[a].i]
				p3 := points[list[b].i]
				p4 := points[list[b].j]

				v1x := int64(p3[0] - p1[0])
				v1y := int64(p3[1] - p1[1])
				v2x := int64(p4[0] - p1[0])
				v2y := int64(p4[1] - p1[1])

				area2 := v1x*v2y - v1y*v2x
				if area2 < 0 {
					area2 = -area2
				}
				if area2 > 0 && float64(area2) < minArea {
					minArea = float64(area2)
				}
			}
		}
	}

	if minArea == math.MaxFloat64 {
		return 0.0
	}
	return minArea
}
```

## Ruby

```ruby
def min_area_free_rect(points)
  n = points.length
  groups = Hash.new { |h, k| h[k] = [] }
  min_area = Float::INFINITY

  (0...n).each do |i|
    xi, yi = points[i]
    ((i + 1)...n).each do |j|
      xj, yj = points[j]

      mx = xi + xj
      my = yi + yj
      dx = xi - xj
      dy = yi - yj
      d2 = dx * dx + dy * dy

      key = [mx, my, d2]
      groups[key].each do |p_idx, q_idx|
        xp, yp = points[p_idx]
        xq, yq = points[q_idx]

        v1x = xp - xi
        v1y = yp - yi
        v2x = xq - xi
        v2y = yq - yi

        cross = v1x * v2y - v1y * v2x
        area = cross.abs
        min_area = area if area > 0 && area < min_area
      end

      groups[key] << [i, j]
    end
  end

  min_area == Float::INFINITY ? 0.0 : min_area.to_f
end
```

## Scala

```scala
object Solution {
    def minAreaFreeRect(points: Array[Array[Int]]): Double = {
        val n = points.length
        val xs = new Array[Int](n)
        val ys = new Array[Int](n)
        for (i <- 0 until n) {
            xs(i) = points(i)(0)
            ys(i) = points(i)(1)
        }

        import scala.collection.mutable

        case class Key(midX2: Int, midY2: Int, distSq: Long)

        val map = mutable.HashMap[Key, mutable.ArrayBuffer[(Int, Int)]]()

        for (i <- 0 until n; j <- i + 1 until n) {
            val mx2 = xs(i) + xs(j)
            val my2 = ys(i) + ys(j)
            val dx = xs(i) - xs(j)
            val dy = ys(i) - ys(j)
            val distSq = dx.toLong * dx + dy.toLong * dy
            val key = Key(mx2, my2, distSq)
            map.getOrElseUpdate(key, mutable.ArrayBuffer()).append((i, j))
        }

        var minArea: Double = Double.MaxValue

        for ((_, list) <- map) {
            val size = list.size
            if (size > 1) {
                for (aIdx <- 0 until size - 1) {
                    val (i1, _) = list(aIdx)
                    val x0 = xs(i1)
                    val y0 = ys(i1)
                    for (bIdx <- aIdx + 1 until size) {
                        val (i2, j2) = list(bIdx)

                        var dx1 = xs(i2) - x0
                        var dy1 = ys(i2) - y0
                        var dx2 = xs(j2) - x0
                        var dy2 = ys(j2) - y0

                        val cross = math.abs(dx1.toLong * dy2 - dy1.toLong * dx2)
                        if (cross != 0 && cross.toDouble < minArea) {
                            minArea = cross.toDouble
                        }
                    }
                }
            }
        }

        if (minArea == Double.MaxValue) 0.0 else minArea
    }
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn min_area_free_rect(points: Vec<Vec<i32>>) -> f64 {
        let n = points.len();
        if n < 4 {
            return 0.0;
        }
        // Convert to i64 for safe arithmetic
        let pts: Vec<(i64, i64)> = points.iter().map(|p| (p[0] as i64, p[1] as i64)).collect();

        // key: (mid_x*2, mid_y*2, squared distance of diagonal)
        let mut map: HashMap<(i64, i64, i64), Vec<(usize, usize)>> = HashMap::new();
        let mut min_area: i64 = i64::MAX;

        for i in 0..n {
            for j in (i + 1)..n {
                let (x1, y1) = pts[i];
                let (x2, y2) = pts[j];
                let mid_x = x1 + x2; // twice the midpoint to keep integer
                let mid_y = y1 + y2;
                let dx = x1 - x2;
                let dy = y1 - y2;
                let dist2 = dx * dx + dy * dy;
                let key = (mid_x, mid_y, dist2);

                if let Some(vec) = map.get_mut(&key) {
                    for &(p, q) in vec.iter() {
                        // Use point i as one vertex of the rectangle
                        let (ax, ay) = pts[i];
                        let (bx, by) = pts[p];
                        let (dx_, dy_) = pts[q];

                        let cross = (bx - ax) * (dy_ - ay) - (by - ay) * (dx_ - ax);
                        let area = cross.abs();
                        if area > 0 && area < min_area {
                            min_area = area;
                        }
                    }
                    vec.push((i, j));
                } else {
                    map.insert(key, vec![(i, j)]);
                }
            }
        }

        if min_area == i64::MAX {
            0.0
        } else {
            min_area as f64
        }
    }
}
```

## Racket

```racket
(define/contract (min-area-free-rect points)
  (-> (listof (listof exact-integer?)) flonum?)
  (let* ([n (length points)]
         [ptvecs (list->vector (map list->vector points))]
         [hash (make-hash)])
    ;; group point pairs by midpoint (stored as sum) and squared distance
    (for ([i (in-range n)])
      (for ([j (in-range (+ i 1) n)])
        (define xi (vector-ref (vector-ref ptvecs i) 0))
        (define yi (vector-ref (vector-ref ptvecs i) 1))
        (define xj (vector-ref (vector-ref ptvecs j) 0))
        (define yj (vector-ref (vector-ref ptvecs j) 1))
        (define mx (+ xi xj))               ; twice midpoint x
        (define my (+ yi yj))               ; twice midpoint y
        (define dist2 (+ (* (- xi xj) (- xi xj))
                         (* (- yi yj) (- yi yj))))
        (define key (list mx my dist2))
        (hash-update! hash key (lambda (lst) (cons (list i j) lst)) '())))
    ;; evaluate minimal rectangle area
    (let ([min-area +inf.0])
      (for ([pair-list (in-hash-values hash)])
        (when (>= (length pair-list) 2)
          (define len (length pair-list))
          (for ([a (in-range (- len 1))])
            (define p1 (list-ref pair-list a))
            (define i1 (first p1))
            (for ([b (in-range (+ a 1) len)])
              (define p2 (list-ref pair-list b))
              (define i2 (first p2))
              (define j2 (second p2))
              ;; compute area using cross product of two adjacent sides
              (define x1 (vector-ref (vector-ref ptvecs i1) 0))
              (define y1 (vector-ref (vector-ref ptvecs i1) 1))
              (define x2 (vector-ref (vector-ref ptvecs i2) 0))
              (define y2 (vector-ref (vector-ref ptvecs i2) 1))
              (define x3 (vector-ref (vector-ref ptvecs j2) 0))
              (define y3 (vector-ref (vector-ref ptvecs j2) 1))
              (define cross (- (* (- x2 x1) (- y3 y1))
                               (* (- y2 y1) (- x3 x1))))
              (define area (abs cross))
              (when (< area min-area)
                (set! min-area area))))))
      (if (= min-area +inf.0)
          0.0
          (exact->inexact min-area)))))
```

## Erlang

```erlang
-spec min_area_free_rect(Points :: [[integer()]]) -> float().
min_area_free_rect(Points) ->
    PointsTuples = [ {X,Y} || [X,Y] <- Points ],
    Len = length(PointsTuples),
    Inf = 1.0e100,
    MinArea = process_i(0, Len, PointsTuples, #{}, Inf),
    case MinArea of
        A when A >= Inf/2 -> 0.0;
        _ -> MinArea * 1.0
    end.

process_i(I, Len, _Pts, Map, Min) when I >= Len-1 ->
    Min;
process_i(I, Len, Pts, Map, Min) ->
    {Xi,Yi} = lists:nth(I+1, Pts),
    {NewMap, NewMin} = process_j(I+1, Len-1, Xi, Yi, Pts, Map, Min),
    process_i(I+1, Len, Pts, NewMap, NewMin).

process_j(J, MaxJ, _Xi, _Yi, _Pts, Map, Min) when J > MaxJ ->
    {Map, Min};
process_j(J, MaxJ, Xi, Yi, Pts, Map, Min) ->
    {Xj,Yj} = lists:nth(J+1, Pts),
    SumX = Xi + Xj,
    SumY = Yi + Yj,
    Dx = Xi - Xj,
    Dy = Yi - Yj,
    Dist = Dx*Dx + Dy*Dy,
    Key = {SumX, SumY, Dist},
    Existing = maps:get(Key, Map, []),
    NewMin = compute_min_area(Existing, {Xi,Yi}, {Xj,Yj}, Min),
    UpdatedPairs = [{{Xi,Yi},{Xj,Yj}} | Existing],
    NewMap = maps:put(Key, UpdatedPairs, Map),
    process_j(J+1, MaxJ, Xi, Yi, Pts, NewMap, NewMin).

compute_min_area([], _A,_B, Min) -> Min;
compute_min_area([{{Xa,Ya},{_Xb,_Yb}} | Rest], {Xi,Yi}, {Xj,Yj}, Min) ->
    Area = abs((Xa - Xi)*(Ya - Yj) - (Ya - Yi)*(Xa - Xj)),
    NewMin = if Area < Min -> Area; true -> Min end,
    compute_min_area(Rest, {Xi,Yi}, {Xj,Yj}, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_area_free_rect(points :: [[integer]]) :: float
  def min_area_free_rect(points) do
    pts = Enum.map(points, fn [x, y] -> {x, y} end)
    n = length(pts)

    pair_map =
      Enum.reduce(0..(n - 2), %{}, fn i, acc ->
        {xi, yi} = Enum.at(pts, i)

        Enum.reduce((i + 1)..(n - 1), acc, fn j, acc2 ->
          {xj, yj} = Enum.at(pts, j)
          mid_x = xi + xj
          mid_y = yi + yj
          dx = xi - xj
          dy = yi - yj
          d2 = dx * dx + dy * dy
          key = {mid_x, mid_y, d2}
          Map.update(acc2, key, [{i, j}], fn list -> [{i, j} | list] end)
        end)
      end)

    min_area =
      Enum.reduce(pair_map, :infinity, fn {_key, pairs}, cur_min ->
        len = length(pairs)

        if len < 2 do
          cur_min
        else
          Enum.reduce(0..(len - 2), cur_min, fn idx1, acc1 ->
            {i1, j1} = Enum.at(pairs, idx1)
            {x1a, y1a} = Enum.at(pts, i1)
            {x1b, y1b} = Enum.at(pts, j1)
            dx1 = x1a - x1b
            dy1 = y1a - y1b

            Enum.reduce((idx1 + 1)..(len - 1), acc1, fn idx2, acc2 ->
              {i2, j2} = Enum.at(pairs, idx2)
              {x2a, y2a} = Enum.at(pts, i2)
              {x2b, y2b} = Enum.at(pts, j2)
              dx2 = x2a - x2b
              dy2 = y2a - y2b

              cross = dx1 * dy2 - dy1 * dx2
              area = :math.abs(cross) / 2.0

              if area < acc2, do: area, else: acc2
            end)
          end)
        end
      end)

    if min_area == :infinity, do: 0.0, else: min_area
  end
end
```

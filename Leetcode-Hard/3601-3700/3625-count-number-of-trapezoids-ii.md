# 3625. Count Number of Trapezoids II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Seg {
        int a, b;
        int dy, dx;          // reduced direction
        long long offset;    // dy*x - dx*y for point a (same for b)
        int midX, midY;      // sum of coordinates (midpoint *2)
    };
    
    static int gcd_int(int a, int b) {
        return std::gcd(a, b);
    }
    
    long long computeValid(const vector<int>& ids,
                           const vector<Seg>& segs,
                           bool useOffset) {
        long long k = ids.size();
        if (k < 2) return 0;
        long long totalPairs = k * (k - 1) / 2;
        
        unordered_map<int,int> degPoint;
        degPoint.reserve(k*2);
        for (int idx : ids) {
            const Seg& s = segs[idx];
            ++degPoint[s.a];
            ++degPoint[s.b];
        }
        long long shared = 0;
        for (auto &p : degPoint) {
            long long c = p.second;
            shared += c * (c - 1) / 2;
        }
        long long disjoint = totalPairs - shared;
        
        unordered_map<long long, vector<int>> groups;
        groups.reserve(ids.size()*2);
        for (int idx : ids) {
            const Seg& s = segs[idx];
            long long key = useOffset ? s.offset
                                      : ((static_cast<long long>(s.dy) << 32) ^ (static_cast<unsigned int>(s.dx)));
            groups[key].push_back(idx);
        }
        
        long long collinearDisjoint = 0;
        for (auto &g : groups) {
            const vector<int>& vec = g.second;
            long long cnt = vec.size();
            if (cnt < 2) continue;
            long long totalG = cnt * (cnt - 1) / 2;
            unordered_map<int,int> degP;
            degP.reserve(cnt*2);
            for (int idx : vec) {
                const Seg& s = segs[idx];
                ++degP[s.a];
                ++degP[s.b];
            }
            long long sharedG = 0;
            for (auto &p : degP) {
                long long c = p.second;
                sharedG += c * (c - 1) / 2;
            }
            collinearDisjoint += totalG - sharedG;
        }
        return disjoint - collinearDisjoint;
    }
    
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        vector<Seg> segs;
        segs.reserve(n * (n - 1) / 2);
        
        unordered_map<long long, vector<int>> slopeMap;
        unordered_map<long long, vector<int>> midMap;
        slopeMap.reserve(segs.capacity()*2);
        midMap.reserve(segs.capacity()*2);
        
        for (int i = 0; i < n; ++i) {
            int xi = points[i][0], yi = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int xj = points[j][0], yj = points[j][1];
                int dy = yj - yi;
                int dx = xj - xi;
                int g = gcd_int(abs(dy), abs(dx));
                dy /= g; dx /= g;
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dy = -dy; dx = -dx;
                }
                long long offset = static_cast<long long>(dy) * xi - static_cast<long long>(dx) * yi;
                int midX = xi + xj;
                int midY = yi + yj;
                
                Seg s{ i, j, dy, dx, offset, midX, midY };
                int idx = segs.size();
                segs.push_back(s);
                
                long long slopeKey = (static_cast<long long>(dy) << 32) ^ static_cast<unsigned int>(dx);
                slopeMap[slopeKey].push_back(idx);
                
                long long midKey = (static_cast<long long>(midX + 4000) << 32) ^ static_cast<unsigned int>(midY + 4000);
                midMap[midKey].push_back(idx);
            }
        }
        
        long long basePairs = 0;
        for (auto &kv : slopeMap) {
            basePairs += computeValid(kv.second, segs, true); // exclude same offset
        }
        
        long long parallelograms = 0;
        for (auto &kv : midMap) {
            parallelograms += computeValid(kv.second, segs, false); // exclude same slope
        }
        
        long long result = basePairs - parallelograms;
        return static_cast<int>(result);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Segment {
        int a, b;
        int lineKey;
        Segment(int a, int b, int lineKey) {
            this.a = a;
            this.b = b;
            this.lineKey = lineKey;
        }
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    }

    public int countTrapezoids(int[][] points) {
        int n = points.length;
        Map<Long, List<Segment>> slopeMap = new HashMap<>();
        Map<Long, Integer> midCount = new HashMap<>();

        // generate all point pairs
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0];
                int y2 = points[j][1];

                // slope normalization
                int dx = x2 - x1;
                int dy = y2 - y1;
                int g = gcd(Math.abs(dx), Math.abs(dy));
                dx /= g;
                dy /= g;
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }
                long slopeKey = ((long)dx << 32) ^ (dy & 0xffffffffL);

                // line identifier using normalized direction
                int lineKey = dy * x1 - dx * y1;

                slopeMap.computeIfAbsent(slopeKey, k -> new ArrayList<>())
                        .add(new Segment(i, j, lineKey));

                // midpoint key for parallelogram counting (using sum coordinates)
                int sumX = x1 + x2;
                int sumY = y1 + y2;
                long midKey = ((long)sumX << 32) ^ (sumY & 0xffffffffL);
                midCount.put(midKey, midCount.getOrDefault(midKey, 0) + 1);
            }
        }

        long totalValidPairs = 0L;

        // process each slope bucket
        for (List<Segment> segList : slopeMap.values()) {
            int k = segList.size();
            if (k < 2) continue;
            long totalPairs = (long) k * (k - 1) / 2;

            Map<Integer, Integer> pointDeg = new HashMap<>();
            Map<Integer, Integer> lineCnt = new HashMap<>();
            Map<Long, Integer> pointLineCnt = new HashMap<>();

            for (Segment seg : segList) {
                // degree per point
                pointDeg.put(seg.a, pointDeg.getOrDefault(seg.a, 0) + 1);
                pointDeg.put(seg.b, pointDeg.getOrDefault(seg.b, 0) + 1);

                // count per line
                lineCnt.put(seg.lineKey, lineCnt.getOrDefault(seg.lineKey, 0) + 1);

                // point-line combination
                long keyA = ((long) seg.a << 32) ^ (seg.lineKey & 0xffffffffL);
                long keyB = ((long) seg.b << 32) ^ (seg.lineKey & 0xffffffffL);
                pointLineCnt.put(keyA, pointLineCnt.getOrDefault(keyA, 0) + 1);
                pointLineCnt.put(keyB, pointLineCnt.getOrDefault(keyB, 0) + 1);
            }

            long shareEndpoint = 0;
            for (int cnt : pointDeg.values()) {
                if (cnt > 1) shareEndpoint += (long) cnt * (cnt - 1) / 2;
            }

            long collinear = 0;
            for (int cnt : lineCnt.values()) {
                if (cnt > 1) collinear += (long) cnt * (cnt - 1) / 2;
            }

            long intersection = 0;
            for (int cnt : pointLineCnt.values()) {
                if (cnt > 1) intersection += (long) cnt * (cnt - 1) / 2;
            }

            long validPairs = totalPairs - shareEndpoint - collinear + intersection;
            totalValidPairs += validPairs;
        }

        // count parallelograms
        long parallelogramCnt = 0L;
        for (int cnt : midCount.values()) {
            if (cnt > 1) parallelogramCnt += (long) cnt * (cnt - 1) / 2;
        }

        long result = totalValidPairs - parallelogramCnt;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from math import gcd
        from collections import defaultdict

        n = len(points)
        slope_buckets = dict()      # key -> list of (i,j,offset)
        midpoint_buckets = dict()   # key -> list of (i,j,slope)

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi
                g = gcd(dx, dy)
                if g:
                    dx //= g
                    dy //= g
                # normalize direction
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                slope = (dy, dx)

                offset = dy * xi - dx * yi   # invariant for the line

                slope_buckets.setdefault(slope, []).append((i, j, offset))

                mid_key = (xi + xj, yi + yj)
                midpoint_buckets.setdefault(mid_key, []).append((i, j, slope))

        total_parallel = 0
        for segs in slope_buckets.values():
            k = len(segs)
            if k < 2:
                continue
            total_pairs = k * (k - 1) // 2

            cnt_point = defaultdict(int)
            cnt_offset = defaultdict(int)
            cnt_pt_off = defaultdict(int)

            for i, j, off in segs:
                cnt_point[i] += 1
                cnt_point[j] += 1
                cnt_offset[off] += 1
                cnt_pt_off[(i, off)] += 1
                cnt_pt_off[(j, off)] += 1

            overlap_total = sum(c * (c - 1) // 2 for c in cnt_point.values())
            collinear_total = sum(c * (c - 1) // 2 for c in cnt_offset.values())
            overlap_collinear = sum(c * (c - 1) // 2 for c in cnt_pt_off.values())

            valid = total_pairs - overlap_total - (collinear_total - overlap_collinear)
            total_parallel += valid

        parallelogram = 0
        for segs in midpoint_buckets.values():
            m = len(segs)
            if m < 2:
                continue
            total_pairs = m * (m - 1) // 2

            cnt_point = defaultdict(int)
            cnt_slope = defaultdict(int)

            for i, j, slope in segs:
                cnt_point[i] += 1
                cnt_point[j] += 1
                cnt_slope[slope] += 1

            overlap_total = sum(c * (c - 1) // 2 for c in cnt_point.values())
            collinear_pairs = sum(c * (c - 1) // 2 for c in cnt_slope.values())

            valid = total_pairs - overlap_total - collinear_pairs
            parallelogram += valid

        return total_parallel - parallelogram
```

## Python3

```python
import math
from collections import defaultdict
class Solution:
    def countTrapezoids(self, points):
        n = len(points)
        slope_data = dict()  # (dy,dx) -> [total_cnt, {offset: cnt}]
        midpoint_counts = defaultdict(int)

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]

                dx = xj - xi
                dy = yj - yi

                # normalize slope
                if dx == 0:
                    ndy, ndx = 1, 0
                elif dy == 0:
                    ndy, ndx = 0, 1
                else:
                    g = math.gcd(abs(dy), abs(dx))
                    ndy = dy // g
                    ndx = dx // g
                    if ndx < 0:
                        ndy = -ndy
                        ndx = -ndx

                slope_key = (ndy, ndx)

                # line offset for this slope: dy*x - dx*y is constant on the line
                offset = ndy * xi - ndx * yi

                if slope_key not in slope_data:
                    slope_data[slope_key] = [0, defaultdict(int)]
                total_cnt, line_map = slope_data[slope_key]
                slope_data[slope_key][0] = total_cnt + 1
                line_map[offset] += 1

                # midpoint (use doubled coordinates to stay integer)
                mid_key = (xi + xj, yi + yj)
                midpoint_counts[mid_key] += 1

        def comb2(c):
            return c * (c - 1) // 2

        total_base_pairs = 0
        for total_cnt, line_map in slope_data.values():
            total_base_pairs += comb2(total_cnt)
            for cnt in line_map.values():
                total_base_pairs -= comb2(cnt)

        parallelograms = 0
        for cnt in midpoint_counts.values():
            parallelograms += comb2(cnt)

        return total_base_pairs - parallelograms
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int gcd_int(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a ? a : 1;
}

typedef struct {
    int dy, dx;      // normalized slope
    int sumX, sumY;  // midpoint sums
    short i, j;      // point indices
} Pair;

static int cmpSlope(const void *a, const void *b) {
    const Pair *p = (const Pair *)a;
    const Pair *q = (const Pair *)b;
    if (p->dy != q->dy) return p->dy - q->dy;
    return p->dx - q->dx;
}

static int cmpMid(const void *a, const void *b) {
    const Pair *p = (const Pair *)a;
    const Pair *q = (const Pair *)b;
    if (p->sumX != q->sumX) return p->sumX - q->sumX;
    return p->sumY - q->sumY;
}

int countTrapezoids(int** points, int pointsSize, int* pointsColSize){
    int n = pointsSize;
    int totalPairs = n * (n - 1) / 2;
    Pair *arr = (Pair *)malloc(sizeof(Pair) * totalPairs);
    int idx = 0;
    for (int i = 0; i < n; ++i) {
        int xi = points[i][0];
        int yi = points[i][1];
        for (int j = i + 1; j < n; ++j) {
            int xj = points[j][0];
            int yj = points[j][1];
            int dy = yj - yi;
            int dx = xj - xi;
            if (dx == 0) {
                dy = 1;
                dx = 0;
            } else if (dy == 0) {
                dy = 0;
                dx = 1;
            } else {
                int g = gcd_int(dy, dx);
                dy /= g;
                dx /= g;
                if (dx < 0) { dy = -dy; dx = -dx; }
            }
            arr[idx].dy = dy;
            arr[idx].dx = dx;
            arr[idx].sumX = xi + xj;
            arr[idx].sumY = yi + yj;
            arr[idx].i = (short)i;
            arr[idx].j = (short)j;
            ++idx;
        }
    }

    long long totalBases = 0;
    // sort by slope
    qsort(arr, totalPairs, sizeof(Pair), cmpSlope);
    int *cnt = (int *)calloc(n, sizeof(int));
    int *used = (int *)malloc(sizeof(int) * n);
    for (int s = 0; s < totalPairs;) {
        int e = s;
        while (e < totalPairs && arr[e].dy == arr[s].dy && arr[e].dx == arr[s].dx) ++e;
        long long k = e - s;
        totalBases += k * (k - 1) / 2;

        int usedCnt = 0;
        for (int t = s; t < e; ++t) {
            short a = arr[t].i, b = arr[t].j;
            if (cnt[a] == 0) used[usedCnt++] = a;
            if (cnt[b] == 0 && b != a) used[usedCnt++] = b;
            cnt[a]++;
            cnt[b]++;
        }
        for (int u = 0; u < usedCnt; ++u) {
            int p = used[u];
            long long c = cnt[p];
            if (c > 1) totalBases -= c * (c - 1) / 2;
            cnt[p] = 0;
        }
        s = e;
    }

    // count parallelograms via midpoints
    qsort(arr, totalPairs, sizeof(Pair), cmpMid);
    long long para = 0;
    for (int s = 0; s < totalPairs;) {
        int e = s;
        while (e < totalPairs && arr[e].sumX == arr[s].sumX && arr[e].sumY == arr[s].sumY) ++e;
        long long m = e - s;
        para += m * (m - 1) / 2;
        s = e;
    }

    free(arr);
    free(cnt);
    free(used);

    long long result = totalBases - para;
    return (int)result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private struct SlopeKey : IEquatable<SlopeKey> {
        public int Dy;
        public int Dx;
        public SlopeKey(int dy, int dx) { Dy = dy; Dx = dx; }
        public bool Equals(SlopeKey other) => Dy == other.Dy && Dx == other.Dx;
        public override bool Equals(object obj) => obj is SlopeKey other && Equals(other);
        public override int GetHashCode() => Dy * 31 + Dx;
    }

    private struct MidKey : IEquatable<MidKey> {
        public int SumX;
        public int SumY;
        public MidKey(int sx, int sy) { SumX = sx; SumY = sy; }
        public bool Equals(MidKey other) => SumX == other.SumX && SumY == other.SumY;
        public override bool Equals(object obj) => obj is MidKey other && Equals(other);
        public override int GetHashCode() => SumX * 31 + SumY;
    }

    private struct Segment {
        public int A;
        public int B;
        public Segment(int a, int b) { A = a; B = b; }
    }

    private static int Gcd(int a, int b) {
        a = Math.Abs(a);
        b = Math.Abs(b);
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a == 0 ? 1 : a;
    }

    public int CountTrapezoids(int[][] points) {
        int n = points.Length;
        var slopeMap = new Dictionary<SlopeKey, List<Segment>>();

        // Build segments grouped by normalized slope
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                if (dx == 0) { // vertical
                    dy = 1;
                } else if (dy == 0) { // horizontal
                    dx = 1;
                } else {
                    int g = Gcd(dx, dy);
                    dx /= g;
                    dy /= g;
                    if (dx < 0) { dx = -dx; dy = -dy; }
                }

                var key = new SlopeKey(dy, dx);
                if (!slopeMap.TryGetValue(key, out var list)) {
                    list = new List<Segment>();
                    slopeMap[key] = list;
                }
                list.Add(new Segment(i, j));
            }
        }

        long totalBasePairs = 0;

        // Process each slope bucket
        foreach (var kv in slopeMap) {
            var segs = kv.Value;
            int k = segs.Count;
            if (k < 2) continue;

            long totalPairs = (long)k * (k - 1) / 2;

            // degree per point within this bucket
            var deg = new Dictionary<int, int>();
            foreach (var s in segs) {
                if (!deg.TryGetValue(s.A, out int cnt)) cnt = 0;
                deg[s.A] = cnt + 1;
                if (!deg.TryGetValue(s.B, out cnt)) cnt = 0;
                deg[s.B] = cnt + 1;
            }
            long sharedEndpointPairs = 0;
            foreach (var d in deg.Values) {
                if (d > 1) sharedEndpointPairs += (long)d * (d - 1) / 2;
            }

            long disjointPairs = totalPairs - sharedEndpointPairs;

            // subtract collinear-disjoint pairs
            var lineMap = new Dictionary<long, List<Segment>>();
            foreach (var s in segs) {
                int dx = points[s.B][0] - points[s.A][0];
                int dy = points[s.B][1] - points[s.A][1];
                // use normalized direction from bucket key
                int ndx = kv.Key.Dx;
                int ndy = kv.Key.Dy;
                long offset = (long)ndy * points[s.A][0] - (long)ndx * points[s.A][1];
                if (!lineMap.TryGetValue(offset, out var lst)) {
                    lst = new List<Segment>();
                    lineMap[offset] = lst;
                }
                lst.Add(s);
            }

            long collinearDisjoint = 0;
            foreach (var entry in lineMap) {
                var list = entry.Value;
                int sz = list.Count;
                if (sz < 2) continue;
                long totalLinePairs = (long)sz * (sz - 1) / 2;

                var degLine = new Dictionary<int, int>();
                foreach (var s in list) {
                    if (!degLine.TryGetValue(s.A, out int cnt)) cnt = 0;
                    degLine[s.A] = cnt + 1;
                    if (!degLine.TryGetValue(s.B, out cnt)) cnt = 0;
                    degLine[s.B] = cnt + 1;
                }
                long sharedLinePairs = 0;
                foreach (var d in degLine.Values) {
                    if (d > 1) sharedLinePairs += (long)d * (d - 1) / 2;
                }

                long disjointLinePairs = totalLinePairs - sharedLinePairs;
                collinearDisjoint += disjointLinePairs;
            }

            disjointPairs -= collinearDisjoint;
            totalBasePairs += disjointPairs;
        }

        // Count parallelograms via midpoints
        var midMap = new Dictionary<MidKey, int>();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int sumX = points[i][0] + points[j][0];
                int sumY = points[i][1] + points[j][1];
                var mk = new MidKey(sumX, sumY);
                if (!midMap.TryGetValue(mk, out int cnt)) cnt = 0;
                midMap[mk] = cnt + 1;
            }
        }

        long parallelograms = 0;
        foreach (var cnt in midMap.Values) {
            if (cnt > 1) parallelograms += (long)cnt * (cnt - 1) / 2;
        }

        long result = totalBasePairs - parallelograms;
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var countTrapezoids = function(points) {
    const n = points.length;
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    // Map slope -> list of segments [i,j]
    const slopeMap = new Map();
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            let dy = points[j][1] - points[i][1];
            let dx = points[j][0] - points[i][0];
            if (dx === 0) { // vertical
                dy = 1;
                dx = 0;
            } else if (dy === 0) { // horizontal
                dy = 0;
                dx = 1;
            } else {
                const g = gcd(Math.abs(dy), Math.abs(dx));
                dy /= g;
                dx /= g;
                if (dx < 0) {
                    dy = -dy;
                    dx = -dx;
                }
            }
            const key = dy + '/' + dx;
            let arr = slopeMap.get(key);
            if (!arr) {
                arr = [];
                slopeMap.set(key, arr);
            }
            arr.push([i, j]);
        }
    }
    
    let totalBasePairs = 0;
    for (const segs of slopeMap.values()) {
        const k = segs.length;
        if (k < 2) continue;
        const totalPairs = k * (k - 1) / 2;
        const cntMap = new Map();
        for (const [a, b] of segs) {
            cntMap.set(a, (cntMap.get(a) || 0) + 1);
            cntMap.set(b, (cntMap.get(b) || 0) + 1);
        }
        let overlap = 0;
        for (const c of cntMap.values()) {
            overlap += c * (c - 1) / 2;
        }
        totalBasePairs += totalPairs - overlap;
    }
    
    // Count parallelograms via equal midpoints
    const midMap = new Map();
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            const sumX = points[i][0] + points[j][0];
            const sumY = points[i][1] + points[j][1];
            const key = sumX + ',' + sumY;
            let arr = midMap.get(key);
            if (!arr) {
                arr = [];
                midMap.set(key, arr);
            }
            arr.push([i, j]);
        }
    }
    
    let parallelogramCount = 0;
    for (const segs of midMap.values()) {
        const m = segs.length;
        if (m < 2) continue;
        const totalPairs = m * (m - 1) / 2;
        const cntMap = new Map();
        for (const [a, b] of segs) {
            cntMap.set(a, (cntMap.get(a) || 0) + 1);
            cntMap.set(b, (cntMap.get(b) || 0) + 1);
        }
        let overlap = 0;
        for (const c of cntMap.values()) {
            overlap += c * (c - 1) / 2;
        }
        parallelogramCount += totalPairs - overlap;
    }
    
    return totalBasePairs - parallelogramCount;
};
```

## Typescript

```typescript
function countTrapezoids(points: number[][]): number {
    const n = points.length;
    // helper gcd
    const gcd = (a: number, b: number): number => {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    // map slope -> list of segments {i,j,c}
    const slopeMap = new Map<string, { i: number; j: number; c: number }[]>();

    for (let i = 0; i < n; ++i) {
        const [xi, yi] = points[i];
        for (let j = i + 1; j < n; ++j) {
            const [xj, yj] = points[j];
            let dx = xj - xi;
            let dy = yj - yi;
            const g = gcd(dx, dy);
            dx /= g;
            dy /= g;
            // normalize direction to have unique representation
            if (dx < 0 || (dx === 0 && dy < 0)) {
                dx = -dx;
                dy = -dy;
            }
            const slopeKey = `${dx},${dy}`;
            const c = dy * xi - dx * yi; // line identifier for this direction
            let arr = slopeMap.get(slopeKey);
            if (!arr) {
                arr = [];
                slopeMap.set(slopeKey, arr);
            }
            arr.push({ i, j, c });
        }
    }

    let totalBases = 0;

    // process each slope bucket
    for (const segs of slopeMap.values()) {
        const k = segs.length;
        if (k < 2) continue;
        let pairs = (k * (k - 1)) >> 1; // C(k,2)

        const pointCnt = new Map<number, number>();
        const lineMap = new Map<number, { cnt: number; ptCnt: Map<number, number> }>();

        for (const seg of segs) {
            const { i, j, c } = seg;
            pointCnt.set(i, (pointCnt.get(i) || 0) + 1);
            pointCnt.set(j, (pointCnt.get(j) || 0) + 1);

            let lineEntry = lineMap.get(c);
            if (!lineEntry) {
                lineEntry = { cnt: 0, ptCnt: new Map<number, number>() };
                lineMap.set(c, lineEntry);
            }
            lineEntry.cnt++;
            lineEntry.ptCnt.set(i, (lineEntry.ptCnt.get(i) || 0) + 1);
            lineEntry.ptCnt.set(j, (lineEntry.ptCnt.get(j) || 0) + 1);
        }

        // subtract pairs sharing an endpoint
        for (const cnt of pointCnt.values()) {
            if (cnt > 1) pairs -= (cnt * (cnt - 1)) >> 1;
        }

        // subtract disjoint collinear pairs within each line
        for (const entry of lineMap.values()) {
            const lineCnt = entry.cnt;
            if (lineCnt < 2) continue;
            let shared = 0;
            for (const pc of entry.ptCnt.values()) {
                if (pc > 1) shared += (pc * (pc - 1)) >> 1;
            }
            const disjointCollinear = ((lineCnt * (lineCnt - 1)) >> 1) - shared;
            pairs -= disjointCollinear;
        }

        totalBases += pairs;
    }

    // count parallelograms via midpoints
    const midpointMap = new Map<string, number>();
    for (let i = 0; i < n; ++i) {
        const [xi, yi] = points[i];
        for (let j = i + 1; j < n; ++j) {
            const mx = xi + points[j][0];
            const my = yi + points[j][1];
            const key = `${mx},${my}`;
            midpointMap.set(key, (midpointMap.get(key) || 0) + 1);
        }
    }

    let parallelograms = 0;
    for (const cnt of midpointMap.values()) {
        if (cnt > 1) parallelograms += (cnt * (cnt - 1)) >> 1;
    }

    return totalBases - parallelograms;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function countTrapezoids($points) {
        $n = count($points);
        // map slope => list of [i,j,lineKey]
        $segmentsBySlope = [];
        // map midpoint => ['total'=>int, 'slopeCounts'=>[slope=>cnt]]
        $midpointMap = [];

        for ($i = 0; $i < $n; ++$i) {
            [$xi, $yi] = $points[$i];
            for ($j = $i + 1; $j < $n; ++$j) {
                [$xj, $yj] = $points[$j];
                $dx = $xj - $xi;
                $dy = $yj - $yi;

                // normalize direction
                if ($dx == 0) {
                    $dy = 1;
                    $dx = 0;
                } elseif ($dy == 0) {
                    $dx = 1;
                    $dy = 0;
                } else {
                    $g = $this->gcd(abs($dx), abs($dy));
                    $dx = intdiv($dx, $g);
                    $dy = intdiv($dy, $g);
                    if ($dx < 0) {
                        $dx = -$dx;
                        $dy = -$dy;
                    }
                }

                $slopeKey = $dy . ',' . $dx;

                // line identifier (constant for points on same line with this direction)
                $c = $dy * $xi - $dx * $yi;   // integer
                $segmentsBySlope[$slopeKey][] = [$i, $j, $c];

                // midpoint key (use sum to keep integers)
                $sx = $xi + $xj;
                $sy = $yi + $yj;
                $midKey = $sx . ',' . $sy;

                if (!isset($midpointMap[$midKey])) {
                    $midpointMap[$midKey] = ['total' => 0, 'slopeCounts' => []];
                }
                ++$midpointMap[$midKey]['total'];
                if (!isset($midpointMap[$midKey]['slopeCounts'][$slopeKey])) {
                    $midpointMap[$midKey]['slopeCounts'][$slopeKey] = 0;
                }
                ++$midpointMap[$midKey]['slopeCounts'][$slopeKey];
            }
        }

        // count valid base pairs (parallel, disjoint, non‑collinear)
        $totalValidBases = 0;
        foreach ($segmentsBySlope as $segList) {
            $k = count($segList);
            if ($k < 2) continue;

            $deg = array_fill(0, $n, 0);
            $linePoints = []; // lineKey => set of point indices

            foreach ($segList as $seg) {
                [$i, $j, $c] = $seg;
                ++$deg[$i];
                ++$deg[$j];

                if (!isset($linePoints[$c])) $linePoints[$c] = [];
                $linePoints[$c][$i] = true;
                $linePoints[$c][$j] = true;
            }

            $totalPairs = $k * ($k - 1) / 2;
            $shared = 0;
            foreach ($deg as $d) {
                if ($d > 1) $shared += $d * ($d - 1) / 2;
            }
            $disjoint = $totalPairs - $shared;

            // subtract pairs that are collinear (lie on the same line)
            $collinearDisjoint = 0;
            foreach ($linePoints as $pointSet) {
                $s = count($pointSet);
                if ($s < 4) continue; // need at least two disjoint segments
                $kLine = $s * ($s - 1) / 2;
                $totalPairsLine = $kLine * ($kLine - 1) / 2;
                $sharedInLine = $s * (($s - 1) * ($s - 2) / 2);
                $collinearDisjoint += $totalPairsLine - $sharedInLine;
            }

            $validBases = $disjoint - $collinearDisjoint;
            $totalValidBases += $validBases;
        }

        // count parallelograms (pairs of segments with same midpoint, non‑collinear)
        $parallelogramCount = 0;
        foreach ($midpointMap as $data) {
            $m = $data['total'];
            if ($m < 2) continue;
            $totalPairsMid = $m * ($m - 1) / 2;

            $collinearPairs = 0;
            foreach ($data['slopeCounts'] as $cnt) {
                if ($cnt > 1) $collinearPairs += $cnt * ($cnt - 1) / 2;
            }

            $parallelogramCount += $totalPairsMid - $collinearPairs;
        }

        return (int)($totalValidBases - $parallelogramCount);
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    struct SlopeKey: Hashable {
        let dy: Int
        let dx: Int
    }
    
    struct SlopeInfo {
        var segCount: Int = 0
        var pointCounts: [Int:Int] = [:]
        var lineCounts: [Int:Int] = [:]
    }
    
    struct MidKey: Hashable {
        let sumX: Int
        let sumY: Int
    }
    
    struct MidInfo {
        var segCount: Int = 0
        var slopeCounts: [SlopeKey:Int] = [:]
    }
    
    func gcd(_ a: Int, _ b: Int) -> Int {
        var x = abs(a)
        var y = abs(b)
        while y != 0 {
            let t = x % y
            x = y
            y = t
        }
        return x == 0 ? 1 : x
    }
    
    func countTrapezoids(_ points: [[Int]]) -> Int {
        let n = points.count
        var slopeMap = [SlopeKey:SlopeInfo]()
        var midMap = [MidKey:MidInfo]()
        
        for i in 0..<n {
            let xi = points[i][0]
            let yi = points[i][1]
            for j in (i+1)..<n {
                let xj = points[j][0]
                let yj = points[j][1]
                
                var dx = xj - xi
                var dy = yj - yi
                let g = gcd(dx, dy)
                dx /= g
                dy /= g
                if dx < 0 || (dx == 0 && dy < 0) {
                    dx = -dx
                    dy = -dy
                }
                let slopeKey = SlopeKey(dy: dy, dx: dx)
                
                // line offset key
                let c = -dy * xi + dx * yi   // Int
                
                var sInfo = slopeMap[slopeKey] ?? SlopeInfo()
                sInfo.segCount += 1
                sInfo.pointCounts[i, default: 0] += 1
                sInfo.pointCounts[j, default: 0] += 1
                sInfo.lineCounts[c, default: 0] += 1
                slopeMap[slopeKey] = sInfo
                
                // midpoint key (using sum to avoid fractions)
                let sumX = xi + xj
                let sumY = yi + yj
                let midKey = MidKey(sumX: sumX, sumY: sumY)
                
                var mInfo = midMap[midKey] ?? MidInfo()
                mInfo.segCount += 1
                mInfo.slopeCounts[slopeKey, default: 0] += 1
                midMap[midKey] = mInfo
            }
        }
        
        var totalBasePairs: Int64 = 0
        for (_, info) in slopeMap {
            let k = Int64(info.segCount)
            if k < 2 { continue }
            var pairs = k * (k - 1) / 2   // all unordered segment pairs with same slope
            
            // subtract pairs sharing an endpoint
            for cnt in info.pointCounts.values {
                let c = Int64(cnt)
                if c >= 2 {
                    pairs -= c * (c - 1) / 2
                }
            }
            // subtract collinear pairs (same line)
            for cnt in info.lineCounts.values {
                let c = Int64(cnt)
                if c >= 2 {
                    pairs -= c * (c - 1) / 2
                }
            }
            totalBasePairs += pairs
        }
        
        var parallelogramCount: Int64 = 0
        for (_, mInfo) in midMap {
            let m = Int64(mInfo.segCount)
            if m < 2 { continue }
            var pairs = m * (m - 1) / 2   // all unordered segment pairs sharing midpoint
            
            // subtract degenerate cases where the two segments are parallel (collinear diagonals)
            for cnt in mInfo.slopeCounts.values {
                let c = Int64(cnt)
                if c >= 2 {
                    pairs -= c * (c - 1) / 2
                }
            }
            parallelogramCount += pairs
        }
        
        let result = totalBasePairs - parallelogramCount
        return Int(result)
    }
}
```

## Kotlin

```kotlin
import kotlin.math.abs

class Solution {
    private fun gcd(a: Int, b: Int): Int {
        var x = abs(a)
        var y = abs(b)
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return if (x == 0) 1 else x
    }

    data class Slope(val dy: Int, val dx: Int)

    fun countTrapezoids(points: Array<IntArray>): Int {
        val n = points.size
        // Map slope -> list of point pairs having that slope
        val slopeMap = HashMap<Slope, MutableList<Pair<Int, Int>>>()

        for (i in 0 until n) {
            val xi = points[i][0]
            val yi = points[i][1]
            for (j in i + 1 until n) {
                val xj = points[j][0]
                val yj = points[j][1]
                var dy = yj - yi
                var dx = xj - xi

                if (dx == 0) { // vertical line
                    dy = 1
                    dx = 0
                } else {
                    val g = gcd(dy, dx)
                    dy /= g
                    dx /= g
                    if (dx < 0) {
                        dx = -dx
                        dy = -dy
                    }
                }

                val key = Slope(dy, dx)
                slopeMap.computeIfAbsent(key) { mutableListOf() }.add(Pair(i, j))
            }
        }

        var total: Long = 0

        // Count disjoint segment pairs with same slope
        for (list in slopeMap.values) {
            val k = list.size
            if (k < 2) continue
            var totalPairs = k.toLong() * (k - 1) / 2
            val cntMap = HashMap<Int, Int>()
            for (p in list) {
                cntMap[p.first] = (cntMap[p.first] ?: 0) + 1
                cntMap[p.second] = (cntMap[p.second] ?: 0) + 1
            }
            var shared: Long = 0
            for (c in cntMap.values) {
                if (c >= 2) shared += c.toLong() * (c - 1) / 2
            }
            total += totalPairs - shared
        }

        // Count parallelograms via equal midpoints (sum of coordinates)
        val midpointMap = HashMap<Pair<Int, Int>, Int>()
        for (i in 0 until n) {
            val xi = points[i][0]
            val yi = points[i][1]
            for (j in i + 1 until n) {
                val sx = xi + points[j][0]
                val sy = yi + points[j][1]
                val key = Pair(sx, sy)
                midpointMap[key] = (midpointMap[key] ?: 0) + 1
            }
        }

        var parallelograms: Long = 0
        for (cnt in midpointMap.values) {
            if (cnt >= 2) parallelograms += cnt.toLong() * (cnt - 1) / 2
        }

        val result = total - parallelograms
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countTrapezoids(List<List<int>> points) {
    int n = points.length;
    Map<String, int> slopeCnt = {};
    Map<String, Map<int, int>> slopePointCnt = {};
    Map<String, int> lineCnt = {};
    Map<String, Map<int, int>> linePointCnt = {};
    Map<String, int> midCnt = {};

    int gcd(int a, int b) {
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a.abs();
    }

    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        int dx = points[j][0] - points[i][0];
        int dy = points[j][1] - points[i][1];

        // normalize direction
        if (dx == 0) {
          dy = 1;
          dx = 0;
        } else if (dy == 0) {
          dy = 0;
          dx = 1;
        } else {
          int g = gcd(dx.abs(), dy.abs());
          dx ~/= g;
          dy ~/= g;
          if (dx < 0) {
            dx = -dx;
            dy = -dy;
          }
        }

        String slopeKey = '${dy}#${dx}';
        slopeCnt[slopeKey] = (slopeCnt[slopeKey] ?? 0) + 1;

        var spMap = slopePointCnt.putIfAbsent(slopeKey, () => <int, int>{});
        spMap[i] = (spMap[i] ?? 0) + 1;
        spMap[j] = (spMap[j] ?? 0) + 1;

        // line identifier using normal form: dy*x - dx*y = c
        int c = dy * points[i][0] - dx * points[i][1];
        String lineKey = '${dy}#${dx}#${c}';
        lineCnt[lineKey] = (lineCnt[lineKey] ?? 0) + 1;

        var lpMap = linePointCnt.putIfAbsent(lineKey, () => <int, int>{});
        lpMap[i] = (lpMap[i] ?? 0) + 1;
        lpMap[j] = (lpMap[j] ?? 0) + 1;

        // midpoint (using sums to avoid fractions)
        int sumX = points[i][0] + points[j][0];
        int sumY = points[i][1] + points[j][1];
        String midKey = '${sumX}#${sumY}';
        midCnt[midKey] = (midCnt[midKey] ?? 0) + 1;
      }
    }

    // total pairs of parallel segments
    int totalBasePairs = 0;
    for (var k in slopeCnt.values) {
      totalBasePairs += k * (k - 1) ~/ 2;
    }

    // subtract pairs sharing an endpoint
    int sharedEndpointPairs = 0;
    for (var pointMap in slopePointCnt.values) {
      for (var cnt in pointMap.values) {
        sharedEndpointPairs += cnt * (cnt - 1) ~/ 2;
      }
    }

    // subtract collinear disjoint segment pairs
    int collinearDisjoint = 0;
    for (var entry in lineCnt.entries) {
      int t = entry.value;
      int totalLinePairs = t * (t - 1) ~/ 2;
      var pointMap = linePointCnt[entry.key]!;
      int overlapInLine = 0;
      for (var cnt in pointMap.values) {
        overlapInLine += cnt * (cnt - 1) ~/ 2;
      }
      collinearDisjoint += totalLinePairs - overlapInLine;
    }

    // count parallelograms
    int parallelogramCnt = 0;
    for (var m in midCnt.values) {
      parallelogramCnt += m * (m - 1) ~/ 2;
    }

    int result = totalBasePairs - sharedEndpointPairs - collinearDisjoint - parallelogramCnt;
    return result;
  }
}
```

## Golang

```go
func countTrapezoids(points [][]int) int {
	type slopeKey struct{ dy, dx int }
	type segment struct{ i, j, line int }
	type midKey struct{ sx, sy int }

	n := len(points)
	slopes := make(map[slopeKey][]segment)
	midCnt := make(map[midKey]int)

	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}
	var gcd func(int, int) int
	gcd = func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		if a < 0 {
			return -a
		}
		return a
	}

	for i := 0; i < n; i++ {
		x1, y1 := points[i][0], points[i][1]
		for j := i + 1; j < n; j++ {
			x2, y2 := points[j][0], points[j][1]

			dx := x2 - x1
			dy := y2 - y1
			g := gcd(abs(dx), abs(dy))
			rdx := dx / g
			rdy := dy / g
			if rdx < 0 || (rdx == 0 && rdy < 0) {
				rdx = -rdx
				rdy = -rdy
			}
			sk := slopeKey{dy: rdy, dx: rdx}
			lineConst := rdy*x1 - rdx*y1
			slopes[sk] = append(slopes[sk], segment{i: i, j: j, line: lineConst})

			mk := midKey{sx: x1 + x2, sy: y1 + y2}
			midCnt[mk]++
		}
	}

	var totalValid int64
	for _, segs := range slopes {
		k := len(segs)
		if k < 2 {
			continue
		}
		totalPairs := int64(k) * int64(k-1) / 2

		deg := make(map[int]int, 8)
		lineCnt := make(map[int]int, 4)

		for _, s := range segs {
			deg[s.i]++
			deg[s.j]++
			lineCnt[s.line]++
		}

		var shared int64
		for _, d := range deg {
			if d >= 2 {
				shared += int64(d) * int64(d-1) / 2
			}
		}
		var collinear int64
		for _, c := range lineCnt {
			if c >= 2 {
				collinear += int64(c) * int64(c-1) / 2
			}
		}
		totalValid += totalPairs - shared - collinear
	}

	var parallelograms int64
	for _, cnt := range midCnt {
		if cnt >= 2 {
			parallelograms += int64(cnt) * int64(cnt-1) / 2
		}
	}

	ans := totalValid - parallelograms
	return int(ans)
}
```

## Ruby

```ruby
def count_trapezoids(points)
  n = points.length
  slopes = Hash.new { |h, k| h[k] = { cnt: 0, deg: Hash.new(0) } }
  mid_counts = Hash.new(0)

  (0...n).each do |i|
    xi, yi = points[i]
    (i + 1...n).each do |j|
      xj, yj = points[j]

      dy = yj - yi
      dx = xj - xi

      # normalize slope
      key =
        if dx == 0
          [1, 0]                     # vertical
        elsif dy == 0
          [0, 1]                     # horizontal
        else
          g = dy.gcd(dx)
          dy /= g
          dx /= g
          if dx < 0
            dy = -dy
            dx = -dx
          end
          [dy, dx]
        end

      entry = slopes[key]
      entry[:cnt] += 1
      entry[:deg][i] += 1
      entry[:deg][j] += 1

      # midpoint (use sum to keep integer)
      mid_key = [xi + xj, yi + yj]
      mid_counts[mid_key] += 1
    end
  end

  total = 0
  slopes.each_value do |e|
    k = e[:cnt]
    next if k < 2
    total += k * (k - 1) / 2
    e[:deg].each_value { |d| total -= d * (d - 1) / 2 }
  end

  parallelogram = 0
  mid_counts.each_value { |c| parallelogram += c * (c - 1) / 2 if c > 1 }

  total - parallelogram
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    private def gcd(a: Int, b: Int): Int = {
        var x = math.abs(a)
        var y = math.abs(b)
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        x
    }

    private class Bucket {
        var total: Int = 0
        val pointCounts: mutable.Map[Int, Int] = mutable.Map.empty
    }

    def countTrapezoids(points: Array[Array[Int]]): Int = {
        val n = points.length
        val slopeMap = mutable.Map[(Int, Int), Bucket]()

        // Build buckets of segments by normalized slope
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n) {
                var dy = points(j)(1) - points(i)(1)
                var dx = points(j)(0) - points(i)(0)

                val key: (Int, Int) =
                    if (dx == 0) {
                        // vertical line, unify direction
                        (1, 0)
                    } else {
                        val g = gcd(dy, dx)
                        dy /= g
                        dx /= g
                        if (dx < 0) {
                            dy = -dy
                            dx = -dx
                        }
                        (dy, dx)
                    }

                val bucket = slopeMap.getOrElseUpdate(key, new Bucket())
                bucket.total += 1
                bucket.pointCounts(i) = bucket.pointCounts.getOrElse(i, 0) + 1
                bucket.pointCounts(j) = bucket.pointCounts.getOrElse(j, 0) + 1

                j += 1
            }
            i += 1
        }

        // Count valid base pairs (parallel segments that do not share endpoints)
        var totalBasePairs: Long = 0L
        for ((_, bucket) <- slopeMap) {
            val k = bucket.total
            var pairs: Long = k.toLong * (k - 1) / 2
            var subtract: Long = 0L
            for (cnt <- bucket.pointCounts.values) {
                subtract += cnt.toLong * (cnt - 1) / 2
            }
            totalBasePairs += pairs - subtract
        }

        // Count parallelograms via equal midpoints of diagonals
        val midpointMap = mutable.Map[(Int, Int), Int]()
        i = 0
        while (i < n) {
            var j = i + 1
            while (j < n) {
                val mx = points(i)(0) + points(j)(0)
                val my = points(i)(1) + points(j)(1)
                val key = (mx, my)
                midpointMap(key) = midpointMap.getOrElse(key, 0) + 1
                j += 1
            }
            i += 1
        }

        var parallelograms: Long = 0L
        for (cnt <- midpointMap.values) {
            parallelograms += cnt.toLong * (cnt - 1) / 2
        }

        val result = totalBasePairs - parallelograms
        result.toInt
    }
}
```

## Rust

```rust
use std::collections::HashMap;

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a.abs()
}

impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut pts: Vec<(i32, i32)> = Vec::with_capacity(n);
        for p in &points {
            pts.push((p[0], p[1]));
        }

        // Map slope -> list of segments (i,j)
        let mut slope_map: HashMap<(i32, i32), Vec<(usize, usize)>> = HashMap::new();

        for i in 0..n {
            for j in (i + 1)..n {
                let (x1, y1) = pts[i];
                let (x2, y2) = pts[j];
                let mut dy = y2 - y1;
                let mut dx = x2 - x1;
                if dx == 0 {
                    dy = 1;
                    dx = 0;
                } else if dy == 0 {
                    dy = 0;
                    dx = 1;
                } else {
                    let g = gcd(dy.abs(), dx.abs());
                    dy /= g;
                    dx /= g;
                    if dx < 0 {
                        dy = -dy;
                        dx = -dx;
                    }
                }
                slope_map.entry((dy, dx)).or_default().push((i, j));
            }
        }

        let mut total_base_pairs: i64 = 0;

        for (&(dy, dx), segs) in &slope_map {
            let k = segs.len() as i64;
            if k < 2 {
                continue;
            }
            let total_pairs = k * (k - 1) / 2;

            // global point counts for overlapping endpoints
            let mut point_cnt: HashMap<usize, usize> = HashMap::new();
            // line offset -> list of segments on that line
            let mut line_map: HashMap<i64, Vec<(usize, usize)>> = HashMap::new();

            for &(a, b) in segs {
                *point_cnt.entry(a).or_insert(0) += 1;
                *point_cnt.entry(b).or_insert(0) += 1;

                // offset c = dy*x - dx*y (constant on the line)
                let (xa, ya) = pts[a];
                let c = (dy as i64) * (xa as i64) - (dx as i64) * (ya as i64);
                line_map.entry(c).or_default().push((a, b));
            }

            // overlapping pairs (share a point)
            let mut overlap_total: i64 = 0;
            for &cnt in point_cnt.values() {
                let c = cnt as i64;
                overlap_total += c * (c - 1) / 2;
            }

            // intra-line pairs and their internal overlaps
            let mut intra_line_pairs: i64 = 0;
            let mut overlap_intra: i64 = 0;

            for segs_on_line in line_map.values() {
                let cnt_line = segs_on_line.len() as i64;
                intra_line_pairs += cnt_line * (cnt_line - 1) / 2;

                // point counts within this line
                let mut pt_cnt: HashMap<usize, usize> = HashMap::new();
                for &(a, b) in segs_on_line {
                    *pt_cnt.entry(a).or_insert(0) += 1;
                    *pt_cnt.entry(b).or_insert(0) + = 1;
                }
                for &c in pt_cnt.values() {
                    let ci = c as i64;
                    overlap_intra += ci * (ci - 1) / 2;
                }
            }

            // valid base pairs: total - overlapping endpoints - intra-line non-overlapping
            let valid = total_pairs - overlap_total - intra_line_pairs + overlap_intra;
            total_base_pairs += valid;
        }

        // Count parallelograms via equal midpoints (using sum of coordinates)
        let mut midpoint_map: HashMap<(i32, i32), Vec<(usize, usize)>> = HashMap::new();
        for i in 0..n {
            for j in (i + 1)..n {
                let sx = pts[i].0 + pts[j].0;
                let sy = pts[i].1 + pts[j].1;
                midpoint_map.entry((sx, sy)).or_default().push((i, j));
            }
        }

        let mut parallelograms: i64 = 0;
        for segs in midpoint_map.values() {
            let m = segs.len() as i64;
            if m < 2 {
                continue;
            }
            let total_pairs = m * (m - 1) / 2;

            // overlapping endpoints (share a vertex)
            let mut point_cnt: HashMap<usize, usize> = HashMap::new();
            for &(a, b) in segs {
                *point_cnt.entry(a).or_insert(0) += 1;
                *point_cnt.entry(b).or_insert(0) += 1;
            }
            let mut overlap: i64 = 0;
            for &cnt in point_cnt.values() {
                let c = cnt as i64;
                overlap += c * (c - 1) / 2;
            }

            parallelograms += total_pairs - overlap;
        }

        let result = total_base_pairs - parallelograms;
        result as i32
    }
}
```

## Racket

```racket
(define (gcd a b)
  (let loop ((x (abs a)) (y (abs b)))
    (if (= y 0) x (loop y (remainder x y)))))

(define (ensure-bucket hm key init-fn)
  (hash-ref hm key
            (lambda ()
              (let ((b (init-fn)))
                (hash-set! hm key b)
                b))))

(define (count-trapezoids points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length points))
         (slope-map (make-hash))
         (mid-map   (make-hash)))
    ;; process all point pairs
    (for ([i (in-range n)])
      (let* ((pi (list-ref points i))
             (xi (first pi))
             (yi (second pi)))
        (for ([j (in-range (+ i 1) n)])
          (let* ((pj (list-ref points j))
                 (xj (first pj))
                 (yj (second pj))
                 ;; slope normalization
                 (dx (- xj xi))
                 (dy (- yj yi))
                 (g (gcd dx dy))
                 (dxr (if (= g 0) 0 (/ dx g)))
                 (dyr (if (= g 0) 0 (/ dy g)))
                 )
            ;; fix sign
            (when (or (< dxr 0) (and (= dxr 0) (< dyr 0)))
              (set! dxr (- dxr))
              (set! dyr (- dyr)))
            ;; slope bucket
            (define s-key (list dyr dxr))
            (define sb (ensure-bucket slope-map s-key
                                      (lambda ()
                                        (let ((b (make-hash)))
                                          (hash-set! b 'k 0)
                                          (hash-set! b 'pt (make-hash))
                                          (hash-set! b 'c (make-hash))
                                          b))))
            ;; update slope bucket counts
            (hash-set! sb 'k (+ (hash-ref sb 'k) 1))
            (define pt-h (hash-ref sb 'pt))
            (hash-set! pt-h i (+ (hash-ref pt-h i 0) 1))
            (hash-set! pt-h j (+ (hash-ref pt-h j 0) 1))
            (define c (- (* dyr xi) (* dxr yi))) ; line constant
            (define c-h (hash-ref sb 'c))
            (hash-set! c-h c (+ (hash-ref c-h c 0) 1))
            ;; midpoint bucket
            (define mx (+ xi xj))
            (define my (+ yi yj))
            (define m-key (list mx my))
            (define mb (ensure-bucket mid-map m-key
                                      (lambda ()
                                        (let ((b (make-hash)))
                                          (hash-set! b 'k 0)
                                          (hash-set! b 'pt (make-hash))
                                          b))))
            (hash-set! mb 'k (+ (hash-ref mb 'k) 1))
            (define ptm (hash-ref mb 'pt))
            (hash-set! ptm i (+ (hash-ref ptm i 0) 1))
            (hash-set! ptm j (+ (hash-ref ptm j 0) 1))))))
    ;; compute total base-pair contributions
    (let ((total-base 0)
          (parallelogram 0))
      (for ([bucket (in-hash-values slope-map)])
        (define k (hash-ref bucket 'k))
        (when (> k 1)
          (define total-pairs (/ (* k (- k 1)) 2))
          (define invalid-shared
            (let ((sum 0))
              (for ([cnt (in-hash-values (hash-ref bucket 'pt))])
                (when (> cnt 1)
                  (set! sum (+ sum (/ (* cnt (- cnt 1)) 2)))))
              sum))
          (define invalid-collinear
            (let ((sum 0))
              (for ([cnt (in-hash-values (hash-ref bucket 'c))])
                (when (> cnt 1)
                  (set! sum (+ sum (/ (* cnt (- cnt 1)) 2)))))
              sum))
          (set! total-base (+ total-base (- total-pairs invalid-shared invalid-collinear)))))
      ;; compute parallelogram count
      (for ([bucket (in-hash-values mid-map)])
        (define k (hash-ref bucket 'k))
        (when (> k 1)
          (define total-pairs (/ (* k (- k 1)) 2))
          (define invalid-shared
            (let ((sum 0))
              (for ([cnt (in-hash-values (hash-ref bucket 'pt))])
                (when (> cnt 1)
                  (set! sum (+ sum (/ (* cnt (- cnt 1)) 2)))))
              sum))
          (set! parallelogram (+ parallelogram (- total-pairs invalid-shared)))))
      (- total-base parallelogram))))
```

## Erlang

```erlang
-spec count_trapezoids(Points :: [[integer()]]) -> integer().
count_trapezoids(Points) ->
    N = length(Points),
    PtTuple = list_to_tuple(Points),
    {SlopeMap, MidMap} = build_maps(N, PtTuple, #{}, #{}),

    TotalBases = maps:fold(
        fun(_Slope, Segs, Acc) ->
            K = length(Segs),
            TotalPairs = K * (K - 1) div 2,
            Overlap = overlap_pairs(Segs),
            Acc + (TotalPairs - Overlap)
        end, 0, SlopeMap),

    Parallelograms = maps:fold(
        fun(_Mid, SlopesList, Acc) ->
            K = length(SlopesList),
            TotalPairs = K * (K - 1) div 2,
            Collinear = slope_pairs(SlopesList),
            Acc + (TotalPairs - Collinear)
        end, 0, MidMap),

    TotalBases - Parallelograms.

%% Build maps of slope -> list of segments and midpoint -> list of slopes
build_maps(N, PtTuple, SMap, MMap) ->
    build_i(0, N, PtTuple, SMap, MMap).

build_i(I, N, _PtTuple, SMap, MMap) when I >= N - 1 ->
    {SMap, MMap};
build_i(I, N, PtTuple, SMap, MMap) ->
    {Xi, Yi} = element(I + 1, PtTuple),
    {SMap2, MMap2} = build_j(I + 1, N, Xi, Yi, PtTuple, SMap, MMap),
    build_i(I + 1, N, PtTuple, SMap2, MMap2).

build_j(J, N, _Xi, _Yi, _PtTuple, SMap, MMap) when J >= N ->
    {SMap, MMap};
build_j(J, N, Xi, Yi, PtTuple, SMap, MMap) ->
    {Xj, Yj} = element(J + 1, PtTuple),
    Dx = Xj - Xi,
    Dy = Yj - Yi,
    Slope = normalize_slope(Dy, Dx),
    MidKey = {Xi + Xj, Yi + Yj},
    Seg = {I, J},
    SMap1 = maps:update_with(Slope,
            fun(L) -> [Seg | L] end,
            [Seg],
            SMap),
    MMap1 = maps:update_with(MidKey,
            fun(L) -> [Slope | L] end,
            [Slope],
            MMap),
    build_j(J + 1, N, Xi, Yi, PtTuple, SMap1, MMap1).

%% Normalize slope to reduced form with consistent sign
normalize_slope(0, 0) -> {0, 0}; % never occurs for distinct points
normalize_slope(Dy, 0) -> {1, 0};
normalize_slope(0, Dx) -> {0, 1};
normalize_slope(Dy, Dx) ->
    G = gcd(abs(Dy), abs(Dx)),
    Dy1 = Dy div G,
    Dx1 = Dx div G,
    case Dx1 of
        D when D < 0 -> {-Dy1, -Dx1};
        _ -> {Dy1, Dx1}
    end.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

%% Count overlapping endpoint pairs within a slope bucket
overlap_pairs(Segs) ->
    CountMap = lists:foldl(
        fun({A, B}, Acc) ->
            Acc1 = maps:update_with(A, fun(C) -> C + 1 end, 1, Acc),
            maps:update_with(B, fun(C) -> C + 1 end, 1, Acc1)
        end,
        #{},
        Segs),
    maps:fold(fun(_P, Cnt, Sum) -> Sum + Cnt * (Cnt - 1) div 2 end, 0, CountMap).

%% Count pairs of segments with the same slope inside a midpoint bucket
slope_pairs(SlopesList) ->
    SMap = lists:foldl(
        fun(S, Acc) -> maps:update_with(S, fun(C) -> C + 1 end, 1, Acc) end,
        #{},
        SlopesList),
    maps:fold(fun(_S, Cnt, Sum) -> Sum + Cnt * (Cnt - 1) div 2 end, 0, SMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_trapezoids(points :: [[integer]]) :: integer
  def count_trapezoids(points) do
    pts = Enum.map(points, fn [x, y] -> {x, y} end)
    n = length(pts)

    # Build maps: slope => list of segments, midpoint sum => count
    {slope_map, mid_map} =
      Enum.reduce(0..(n - 2), {%{}, %{}}, fn i, {sm, mm} ->
        {xi, yi} = Enum.at(pts, i)

        Enum.reduce((i + 1)..(n - 1), {sm, mm}, fn j, {sm_acc, mm_acc} ->
          {xj, yj} = Enum.at(pts, j)
          dy = yj - yi
          dx = xj - xi

          slope_key =
            cond do
              dx == 0 -> {1, 0}
              dy == 0 -> {0, 1}
              true ->
                g = Integer.gcd(abs(dy), abs(dx))
                ndy = div(dy, g)
                ndx = div(dx, g)

                if ndx < 0 do
                  {-ndy, -ndx}
                else
                  {ndy, ndx}
                end
            end

          sm_new =
            Map.update(sm_acc, slope_key, [{i, j}], fn list -> [{i, j} | list] end)

          sumx = xi + xj
          sumy = yi + yj
          mid_key = {sumx, sumy}
          mm_new = Map.update(mm_acc, mid_key, 1, &(&1 + 1))

          {sm_new, mm_new}
        end)
      end)

    # Count valid parallel base pairs (same slope, no shared endpoint)
    total_valid =
      Enum.reduce(slope_map, 0, fn {_key, segs}, acc ->
        m = length(segs)

        if m < 2 do
          acc
        else
          total_pairs = div(m * (m - 1), 2)

          deg_map =
            Enum.reduce(segs, %{}, fn {i, j}, dm ->
              dm = Map.update(dm, i, 1, &(&1 + 1))
              Map.update(dm, j, 1, &(&1 + 1))
            end)

          shared =
            Enum.reduce(deg_map, 0, fn {_p, d}, sacc ->
              if d >= 2, do: sacc + div(d * (d - 1), 2), else: sacc
            end)

          acc + total_pairs - shared
        end
      end)

    # Count parallelograms via equal midpoints of diagonals
    parallelogram_cnt =
      Enum.reduce(mid_map, 0, fn {_key, cnt}, acc ->
        if cnt < 2 do
          acc
        else
          acc + div(cnt * (cnt - 1), 2)
        end
      end)

    total_valid - parallelogram_cnt
  end
end
```

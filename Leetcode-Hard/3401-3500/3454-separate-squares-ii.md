# 3454. Separate Squares II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Event{
        long long y;
        int type; // +1 add, -1 remove
        int l,r;  // indices in x-segments [l,r)
        bool operator<(const Event& other) const{
            return y < other.y;
        }
    };
    
    struct SegTree{
        vector<int> cnt;
        vector<long long> len;
        const vector<long long>* xs;
        int n;
        SegTree(const vector<long long>& coord){
            xs = &coord;
            n = (int)coord.size() - 1; // number of elementary segments
            cnt.assign(4*n+5,0);
            len.assign(4*n+5,0);
        }
        void update(int node,int l,int r,int ql,int qr,int val){
            if(qr<=l || r<=ql) return;
            if(ql<=l && r<=qr){
                cnt[node] += val;
            }else{
                int mid = (l+r)/2;
                update(node<<1,l,mid,ql,qr,val);
                update(node<<1|1,mid,r,ql,qr,val);
            }
            if(cnt[node]>0){
                len[node] = (*xs)[r] - (*xs)[l];
            }else{
                if(l+1==r) len[node]=0;
                else len[node]=len[node<<1]+len[node<<1|1];
            }
        }
        void update(int l,int r,int val){ update(1,0,n,l,r,val); }
        long long totalLen() const { return len[1]; }
    };
    
    double separateSquares(vector<vector<int>>& squares) {
        int n = squares.size();
        vector<long long> xs;
        xs.reserve(2*n);
        for(auto &sq: squares){
            long long x = sq[0];
            long long l = sq[2];
            xs.push_back(x);
            xs.push_back(x+l);
        }
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        
        vector<Event> events;
        events.reserve(2*n);
        for(auto &sq: squares){
            long long x = sq[0];
            long long y = sq[1];
            long long l = sq[2];
            int li = lower_bound(xs.begin(), xs.end(), x) - xs.begin();
            int ri = lower_bound(xs.begin(), xs.end(), x+l) - xs.begin();
            events.push_back({y, +1, li, ri});
            events.push_back({y+l, -1, li, ri});
        }
        sort(events.begin(), events.end());
        
        // First pass: compute total union area
        SegTree seg(xs);
        size_t idx = 0;
        long long prevY = events[0].y;
        while(idx < events.size() && events[idx].y == prevY){
            seg.update(events[idx].l, events[idx].r, events[idx].type);
            ++idx;
        }
        long long curLen = seg.totalLen();
        __int128 totalAreaInt = 0;
        while(idx < events.size()){
            long long y = events[idx].y;
            long long delta = y - prevY;
            totalAreaInt += (__int128)curLen * delta;
            while(idx < events.size() && events[idx].y == y){
                seg.update(events[idx].l, events[idx].r, events[idx].type);
                ++idx;
            }
            curLen = seg.totalLen();
            prevY = y;
        }
        long double totalArea = (long double)totalAreaInt;
        long double target = totalArea / 2.0L;
        
        // Second pass: find split line
        SegTree seg2(xs);
        idx = 0;
        prevY = events[0].y;
        while(idx < events.size() && events[idx].y == prevY){
            seg2.update(events[idx].l, events[idx].r, events[idx].type);
            ++idx;
        }
        curLen = seg2.totalLen();
        long double acc = 0.0L;
        while(idx < events.size()){
            long long y = events[idx].y;
            long long delta = y - prevY;
            if(curLen > 0){
                __int128 incInt = (__int128)curLen * delta;
                long double inc = (long double)incInt;
                if(acc + inc >= target){
                    long double need = target - acc;
                    long double ansY = (long double)prevY + need / (long double)curLen;
                    return (double)ansY;
                }
                acc += inc;
            }
            while(idx < events.size() && events[idx].y == y){
                seg2.update(events[idx].l, events[idx].r, events[idx].type);
                ++idx;
            }
            curLen = seg2.totalLen();
            prevY = y;
        }
        // If not found within loop (shouldn't happen), return last processed y
        return (double)prevY;
    }
};
```

## Java

```java
class Solution {
    private int[][] squares;

    public double separateSquares(int[][] squares) {
        this.squares = squares;
        long minY = Long.MAX_VALUE;
        long maxY = Long.MIN_VALUE;
        for (int[] s : squares) {
            long y = s[1];
            long top = y + s[2];
            if (y < minY) minY = y;
            if (top > maxY) maxY = top;
        }
        double totalArea = unionArea((double) maxY);
        double target = totalArea / 2.0;
        double lo = minY, hi = maxY;
        for (int iter = 0; iter < 80; ++iter) {
            double mid = (lo + hi) * 0.5;
            double area = unionArea(mid);
            if (area < target) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        return hi;
    }

    private static class Event {
        double x;
        int type; // +1 add, -1 remove
        double y1, y2;
        Event(double x, int type, double y1, double y2) {
            this.x = x;
            this.type = type;
            this.y1 = y1;
            this.y2 = y2;
        }
    }

    private double unionArea(double lineY) {
        List<Event> events = new ArrayList<>(squares.length * 2);
        for (int[] s : squares) {
            double xi = s[0];
            double yi = s[1];
            double li = s[2];
            if (lineY <= yi) continue;
            double y1 = yi;
            double y2 = Math.min(yi + li, lineY);
            double x1 = xi;
            double x2 = xi + li;
            events.add(new Event(x1, 1, y1, y2));
            events.add(new Event(x2, -1, y1, y2));
        }
        if (events.isEmpty()) return 0.0;

        // collect y coordinates
        double[] ys = new double[events.size() * 2];
        int idx = 0;
        for (Event e : events) {
            ys[idx++] = e.y1;
            ys[idx++] = e.y2;
        }
        Arrays.sort(ys);
        int m = 1;
        for (int i = 1; i < ys.length; ++i) {
            if (ys[i] != ys[m - 1]) {
                ys[m++] = ys[i];
            }
        }
        double[] yVals = Arrays.copyOf(ys, m);

        // sort events by x
        events.sort((a, b) -> Double.compare(a.x, b.x));

        SegTree seg = new SegTree(yVals);
        double area = 0.0;
        double prevX = events.get(0).x;
        int i = 0;
        while (i < events.size()) {
            double curX = events.get(i).x;
            double dx = curX - prevX;
            if (dx > 0) {
                area += seg.totalLen() * dx;
            }
            // process all events at curX
            while (i < events.size() && events.get(i).x == curX) {
                Event e = events.get(i);
                int l = Arrays.binarySearch(yVals, e.y1);
                int r = Arrays.binarySearch(yVals, e.y2);
                seg.update(l, r, e.type);
                i++;
            }
            prevX = curX;
        }
        return area;
    }

    private static class SegTree {
        private final double[] ys;
        private final int n;
        private final int[] cnt;
        private final double[] len;

        SegTree(double[] ys) {
            this.ys = ys;
            this.n = ys.length - 1; // number of elementary intervals
            int size = Math.max(4, n * 4);
            cnt = new int[size];
            len = new double[size];
        }

        void update(int l, int r, int val) {
            update(1, 0, n, l, r, val);
        }

        private void update(int node, int nl, int nr, int ql, int qr, int val) {
            if (qr <= nl || nr <= ql) return;
            if (ql <= nl && nr <= qr) {
                cnt[node] += val;
            } else {
                int mid = (nl + nr) >>> 1;
                update(node << 1, nl, mid, ql, qr, val);
                update(node << 1 | 1, mid, nr, ql, qr, val);
            }
            if (cnt[node] > 0) {
                len[node] = ys[nr] - ys[nl];
            } else {
                if (nr - nl == 1) {
                    len[node] = 0.0;
                } else {
                    len[node] = len[node << 1] + len[node << 1 | 1];
                }
            }
        }

        double totalLen() {
            return len[1];
        }
    }
}
```

## Python

```python
class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # collect x coordinates for compression
        xs = []
        events = {}
        for xi, yi, li in squares:
            x1 = xi
            x2 = xi + li
            xs.append(x1)
            xs.append(x2)
            top = yi + li
            bottom = yi
            events.setdefault(top, []).append((1, x1, x2))
            events.setdefault(bottom, []).append((-1, x1, x2))

        xs = sorted(set(xs))
        xi_index = {x: i for i, x in enumerate(xs)}
        # convert event x to indices
        for y in list(events.keys()):
            lst = events[y]
            newlst = []
            for delta, x1, x2 in lst:
                l = xi_index[x1]
                r = xi_index[x2]
                newlst.append((delta, l, r))
            events[y] = newlst

        ys = sorted(events.keys(), reverse=True)
        if len(ys) < 2:
            return float(ys[0])  # degenerate case

        class SegTree:
            __slots__ = ('xs', 'cnt', 'len', 'n')
            def __init__(self, xs):
                self.xs = xs
                self.n = len(xs) - 1
                size = self.n * 4
                self.cnt = [0] * size
                self.len = [0] * size

            def _update(self, node, l, r, ql, qr, val):
                if ql >= r or qr <= l:
                    return
                if ql <= l and r <= qr:
                    self.cnt[node] += val
                else:
                    mid = (l + r) // 2
                    self._update(node * 2, l, mid, ql, qr, val)
                    self._update(node * 2 + 1, mid, r, ql, qr, val)
                if self.cnt[node] > 0:
                    self.len[node] = self.xs[r] - self.xs[l]
                else:
                    if l + 1 == r:
                        self.len[node] = 0
                    else:
                        self.len[node] = self.len[node * 2] + self.len[node * 2 + 1]

            def add(self, l, r, val):
                self._update(1, 0, self.n, l, r, val)

            def total_len(self):
                return self.len[1]

        # first pass: compute total union area
        seg = SegTree(xs)
        total_area = 0.0
        for i in range(len(ys) - 1):
            y = ys[i]
            for delta, l, r in events[y]:
                seg.add(l, r, delta)
            L = seg.total_len()
            dy = y - ys[i + 1]
            total_area += L * dy

        target = total_area / 2.0

        # second pass: find minimal y where area above equals target
        seg = SegTree(xs)
        acc = 0.0
        half_reached = False
        for i in range(len(ys) - 1):
            y = ys[i]
            for delta, l, r in events[y]:
                seg.add(l, r, delta)
            L = seg.total_len()
            dy = y - ys[i + 1]

            if not half_reached:
                if acc < target < acc + L * dy:
                    needed = target - acc
                    return y - needed / L
                elif acc + L * dy == target:
                    acc += L * dy
                    half_reached = True
                    continue
                else:
                    acc += L * dy
            else:
                if L > 0:
                    return float(y)
                # else stay in zero-length region, continue

        # If not returned inside loop, answer is the lowest y processed
        return float(ys[-1])
```

## Python3

```python
import sys
from typing import List

class SegTree:
    __slots__ = ("xs", "n", "cnt", "length")
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        size = self.n * 4 + 5
        self.cnt = [0] * size
        self.length = [0] * size

    def _update(self, idx: int, l: int, r: int, ql: int, qr: int, val: int):
        if ql >= r or qr <= l:
            return
        if ql <= l and r <= qr:
            self.cnt[idx] += val
        else:
            mid = (l + r) // 2
            self._update(idx * 2, l, mid, ql, qr, val)
            self._update(idx * 2 + 1, mid, r, ql, qr, val)
        if self.cnt[idx] > 0:
            self.length[idx] = self.xs[r] - self.xs[l]
        else:
            if r - l == 1:
                self.length[idx] = 0
            else:
                self.length[idx] = self.length[idx * 2] + self.length[idx * 2 + 1]

    def update(self, l: int, r: int, val: int):
        if l < r:
            self._update(1, 0, self.n, l, r, val)

    def total(self) -> int:
        return self.length[1] if self.n > 0 else 0


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = []
        events = []  # (y, type(+1/-1), x_l_idx, x_r_idx)
        for xi, yi, li in squares:
            x1 = xi
            x2 = xi + li
            y1 = yi
            y2 = yi + li
            xs.append(x1)
            xs.append(x2)
            # placeholders for indices; will fill after compression
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))

        xs = sorted(set(xs))
        x_id = {x: i for i, x in enumerate(xs)}
        # replace coordinates with indices in events
        comp_events = []
        for y, typ, xl, xr in events:
            comp_events.append((y, typ, x_id[xl], x_id[xr]))
        comp_events.sort(key=lambda e: e[0])

        # first sweep to compute total area
        seg = SegTree(xs)
        prev_y = comp_events[0][0]
        total_area = 0
        i = 0
        m = len(comp_events)
        while i < m:
            cur_y = comp_events[i][0]
            delta = cur_y - prev_y
            covered_len = seg.total()
            total_area += covered_len * delta
            # apply all events at cur_y
            while i < m and comp_events[i][0] == cur_y:
                _, typ, l_idx, r_idx = comp_events[i]
                seg.update(l_idx, r_idx, typ)
                i += 1
            prev_y = cur_y

        half = total_area / 2.0

        # second sweep to locate split line
        seg = SegTree(xs)
        prev_y = comp_events[0][0]
        area_below = 0.0
        i = 0
        while i < m:
            cur_y = comp_events[i][0]
            delta = cur_y - prev_y
            covered_len = seg.total()
            if covered_len > 0:
                potential = area_below + covered_len * delta
                if potential >= half - 1e-12:
                    needed = half - area_below
                    return prev_y + needed / covered_len
            area_below += covered_len * delta
            while i < m and comp_events[i][0] == cur_y:
                _, typ, l_idx, r_idx = comp_events[i]
                seg.update(l_idx, r_idx, typ)
                i += 1
            prev_y = cur_y

        # fallback (should not happen)
        return float(prev_y)
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    long long y;
    int type;      // +1 add, -1 remove
    int l, r;      // indices in xs (compressed), interval [l, r)
} Event;

static long long *xs;          // compressed x coordinates
static int xsSize;             // number of unique x's

static int *cntSeg;
static long long *lenSeg;

/* binary search for lower bound */
static int lower_bound(long long *arr, int n, long long val) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (arr[mid] < val) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

/* push up information for segment tree node */
static void pushup(int node, int l, int r) {
    if (cntSeg[node] > 0) {
        lenSeg[node] = xs[r + 1] - xs[l];
    } else {
        if (l == r) lenSeg[node] = 0;
        else lenSeg[node] = lenSeg[node << 1] + lenSeg[(node << 1) | 1];
    }
}

/* update segment tree on interval [ql, qr] inclusive */
static void update(int node, int l, int r, int ql, int qr, int delta) {
    if (qr < l || ql > r) return;
    if (ql <= l && r <= qr) {
        cntSeg[node] += delta;
        pushup(node, l, r);
        return;
    }
    int mid = (l + r) >> 1;
    update(node << 1, l, mid, ql, qr, delta);
    update((node << 1) | 1, mid + 1, r, ql, qr, delta);
    pushup(node, l, r);
}

/* comparator for qsort on events by y */
static int cmpEvent(const void *a, const void *b) {
    long long ya = ((const Event *)a)->y;
    long long yb = ((const Event *)b)->y;
    if (ya < yb) return -1;
    if (ya > yb) return 1;
    return 0;
}

double separateSquares(int** squares, int squaresSize, int* squaresColSize){
    int N = squaresSize;
    /* collect x coordinates */
    long long *tmpX = (long long *)malloc(sizeof(long long) * 2 * N);
    for (int i = 0; i < N; ++i) {
        long long xi = squares[i][0];
        long long li = squares[i][2];
        tmpX[2*i] = xi;
        tmpX[2*i+1] = xi + li;
    }
    qsort(tmpX, 2*N, sizeof(long long), (int (*)(const void*, const void*))cmpEvent);
    /* unique */
    xsSize = 0;
    xs = (long long *)malloc(sizeof(long long) * (2*N));
    for (int i = 0; i < 2*N; ++i) {
        if (i == 0 || tmpX[i] != tmpX[i-1]) {
            xs[xsSize++] = tmpX[i];
        }
    }
    free(tmpX);
    /* build events */
    Event *ev = (Event *)malloc(sizeof(Event) * 2 * N);
    int evCnt = 0;
    for (int i = 0; i < N; ++i) {
        long long xi = squares[i][0];
        long long yi = squares[i][1];
        long long li = squares[i][2];
        int lIdx = lower_bound(xs, xsSize, xi);
        int rIdx = lower_bound(xs, xsSize, xi + li);
        ev[evCnt++] = (Event){yi, 1, lIdx, rIdx};
        ev[evCnt++] = (Event){yi + li, -1, lIdx, rIdx};
    }
    qsort(ev, evCnt, sizeof(Event), cmpEvent);

    /* segment tree init */
    int segSize = xsSize * 4;
    cntSeg = (int *)calloc(segSize, sizeof(int));
    lenSeg = (long long *)calloc(segSize, sizeof(long long));

    /* sweep and store slabs */
    int M = xsSize - 1; // number of elementary x-intervals
    long long prevY = ev[0].y;
    long long curLen = 0;

    // allocate arrays for slabs (max possible slabs = evCnt)
    long long *slabStart = (long long *)malloc(sizeof(long long) * evCnt);
    long long *slabEnd   = (long long *)malloc(sizeof(long long) * evCnt);
    long long *slabLen   = (long long *)malloc(sizeof(long long) * evCnt);
    int slabCnt = 0;

    int idx = 0;
    while (idx < evCnt) {
        long long curY = ev[idx].y;
        if (curY > prevY && curLen > 0) {
            slabStart[slabCnt] = prevY;
            slabEnd[slabCnt]   = curY;
            slabLen[slabCnt]   = curLen;
            ++slabCnt;
        }
        // process all events at curY
        while (idx < evCnt && ev[idx].y == curY) {
            int l = ev[idx].l;
            int r = ev[idx].r - 1; // inclusive index for segment tree leaves
            if (l <= r)
                update(1, 0, M-1, l, r, ev[idx].type);
            ++idx;
        }
        curLen = lenSeg[1];
        prevY = curY;
    }

    /* compute total area */
    unsigned long long totalArea = 0ULL;
    for (int i = 0; i < slabCnt; ++i) {
        unsigned long long deltaY = (unsigned long long)(slabEnd[i] - slabStart[i]);
        unsigned long long area = (unsigned long long)slabLen[i] * deltaY;
        totalArea += area;
    }

    double target = (double)totalArea / 2.0;

    /* locate answer */
    double acc = 0.0;
    for (int i = 0; i < slabCnt; ++i) {
        if (slabLen[i] == 0) continue;
        double area = (double)slabLen[i] * (double)(slabEnd[i] - slabStart[i]);
        if (acc + area >= target) {
            double need = target - acc;
            double ans = (double)slabStart[i] + need / (double)slabLen[i];
            /* free allocated memory */
            free(xs);
            free(cntSeg);
            free(lenSeg);
            free(ev);
            free(slabStart);
            free(slabEnd);
            free(slabLen);
            return ans;
        }
        acc += area;
    }

    /* fallback (should not happen) */
    double ans = (double)slabEnd[slabCnt-1];
    free(xs);
    free(cntSeg);
    free(lenSeg);
    free(ev);
    free(slabStart);
    free(slabEnd);
    free(slabLen);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private long[] xs;
    private int[] cnt;
    private long[] len;

    private void PushUp(int node, int l, int r)
    {
        if (cnt[node] > 0)
        {
            len[node] = xs[r] - xs[l];
        }
        else if (l + 1 == r)
        {
            len[node] = 0;
        }
        else
        {
            len[node] = len[node << 1] + len[(node << 1) | 1];
        }
    }

    private void Update(int node, int l, int r, int ql, int qr, int val)
    {
        if (qr <= l || ql >= r) return;
        if (ql <= l && r <= qr)
        {
            cnt[node] += val;
            PushUp(node, l, r);
            return;
        }
        int mid = (l + r) >> 1;
        Update(node << 1, l, mid, ql, qr, val);
        Update((node << 1) | 1, mid, r, ql, qr, val);
        PushUp(node, l, r);
    }

    private long TotalCoveredLength()
    {
        return len[1];
    }

    public double SeparateSquares(int[][] squares)
    {
        int n = squares.Length;
        var xList = new List<long>(2 * n);
        for (int i = 0; i < n; i++)
        {
            long x = squares[i][0];
            long l = squares[i][2];
            xList.Add(x);
            xList.Add(x + l);
        }
        xList.Sort();
        var uniq = new List<long>();
        long prev = long.MinValue;
        foreach (var v in xList)
        {
            if (v != prev)
            {
                uniq.Add(v);
                prev = v;
            }
        }
        xs = uniq.ToArray();
        int m = xs.Length;

        var indexMap = new Dictionary<long, int>(m * 2);
        for (int i = 0; i < m; i++) indexMap[xs[i]] = i;

        // events
        var events = new List<(long y, int type, int l, int r)>();
        for (int i = 0; i < n; i++)
        {
            long x = squares[i][0];
            long y = squares[i][1];
            long l = squares[i][2];
            int li = indexMap[x];
            int ri = indexMap[x + l];
            events.Add((y, +1, li, ri));
            events.Add((y + l, -1, li, ri));
        }
        events.Sort((a, b) => a.y.CompareTo(b.y));

        // first sweep to compute total union area
        cnt = new int[4 * m];
        len = new long[4 * m];
        double totalArea = 0;
        long prevY = events[0].y;
        int idx = 0;
        while (idx < events.Count)
        {
            long curY = events[idx].y;
            long deltaY = curY - prevY;
            if (deltaY > 0)
            {
                totalArea += (double)TotalCoveredLength() * deltaY;
            }
            // process all events at curY
            while (idx < events.Count && events[idx].y == curY)
            {
                var e = events[idx];
                Update(1, 0, m - 1, e.l, e.r, e.type);
                idx++;
            }
            prevY = curY;
        }

        // second sweep to find median line
        cnt = new int[4 * m];
        len = new long[4 * m];
        double target = totalArea / 2.0;
        double cumArea = 0;
        prevY = events[0].y;
        idx = 0;
        while (idx < events.Count)
        {
            long curY = events[idx].y;
            long deltaY = curY - prevY;
            if (deltaY > 0)
            {
                double coveredLen = TotalCoveredLength();
                double areaInc = coveredLen * deltaY;
                if (cumArea + areaInc >= target && coveredLen > 0)
                {
                    double need = target - cumArea;
                    double ans = prevY + need / coveredLen;
                    return ans;
                }
                cumArea += areaInc;
            }
            while (idx < events.Count && events[idx].y == curY)
            {
                var e = events[idx];
                Update(1, 0, m - 1, e.l, e.r, e.type);
                idx++;
            }
            prevY = curY;
        }

        // If not found within loops (should not happen), return last y
        return prevY;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number[][]} squares
 * @return {number}
 * /
var separateSquares = function(squares) {
    // collect x-coordinates for compression
    const xs = [];
    const rects = squares.map(s => {
        const [x, y, l] = s;
        const xl = x, xr = x + l;
        xs.push(xl, xr);
        return {xl, xr, yb: y, yt: y + l};
    });
    xs.sort((a, b) => a - b);
    const uniq = [];
    for (let v of xs) {
        if (uniq.length === 0 || uniq[uniq.length - 1] !== v) uniq.push(v);
    }
    const idxMap = new Map();
    uniq.forEach((v, i) => idxMap.set(v, i));
    rects.forEach(r => {
        r.lIdx = idxMap.get(r.xl);
        r.rIdx = idxMap.get(r.xr);
    });

    // build events
    const events = [];
    for (let r of rects) {
        events.push({y: r.yb, type: 1, l: r.lIdx, r: r.rIdx});
        events.push({y: r.yt, type: -1, l: r.lIdx, r: r.rIdx});
    }
    events.sort((a, b) => a.y - b.y || a.type - b.type);

    const m = uniq.length - 1; // number of x-intervals
    const cnt = new Int32Array(4 * m);
    const len = new Float64Array(4 * m);

    function update(node, l, r, ql, qr, val) {
        if (ql >= r || qr <= l) return;
        if (ql <= l && r <= qr) {
            cnt[node] += val;
        } else {
            const mid = (l + r) >> 1;
            update(node << 1, l, mid, ql, qr, val);
            update((node << 1) | 1, mid, r, ql, qr, val);
        }
        if (cnt[node] > 0) {
            len[node] = uniq[r] - uniq[l];
        } else {
            if (l + 1 === r) len[node] = 0;
            else len[node] = len[node << 1] + len[(node << 1) | 1];
        }
    }

    // first pass: total union area
    let prevY = events[0].y;
    let covered = 0;
    let totalArea = 0;
    let i = 0;
    while (i < events.length) {
        const y = events[i].y;
        if (y > prevY) {
            totalArea += covered * (y - prevY);
        }
        while (i < events.length && events[i].y === y) {
            update(1, 0, m, events[i].l, events[i].r, events[i].type);
            i++;
        }
        covered = len[1];
        prevY = y;
    }

    const target = totalArea / 2;

    // second pass: find minimal y where area below reaches target
    cnt.fill(0);
    len.fill(0);
    let cum = 0;
    prevY = events[0].y;
    covered = 0;
    i = 0;
    while (i < events.length) {
        const y = events[i].y;
        if (y > prevY) {
            const delta = y - prevY;
            if (cum + covered * delta >= target - 1e-12) {
                if (covered === 0) {
                    return prevY; // any point in this gap works, minimal is lower bound
                } else {
                    const need = target - cum;
                    return prevY + need / covered;
                }
            }
            cum += covered * delta;
        }
        while (i < events.length && events[i].y === y) {
            update(1, 0, m, events[i].l, events[i].r, events[i].type);
            i++;
        }
        covered = len[1];
        prevY = y;
    }

    // fallback (should not happen)
    return events[events.length - 1].y;
};
```

## Typescript

```typescript
function separateSquares(squares: number[][]): number {
    // Collect all x coordinates for compression
    const xsSet = new Set<number>();
    const events: { y: number; type: number; l: number; r: number }[] = [];
    for (const [x, y, l] of squares) {
        xsSet.add(x);
        xsSet.add(x + l);
    }
    const xs = Array.from(xsSet).sort((a, b) => a - b);
    const xIdx = new Map<number, number>();
    for (let i = 0; i < xs.length; i++) xIdx.set(xs[i], i);

    // Build events
    for (const [x, y, l] of squares) {
        const left = xIdx.get(x)!;
        const right = xIdx.get(x + l)!;
        events.push({ y: y, type: 1, l: left, r: right });
        events.push({ y: y + l, type: -1, l: left, r: right });
    }
    events.sort((a, b) => a.y - b.y);

    // Segment tree for union length of x-intervals
    class SegTree {
        n: number;
        cnt: Int32Array;
        len: Float64Array;
        xs: number[];
        constructor(xs: number[]) {
            this.xs = xs;
            this.n = xs.length - 1; // number of elementary intervals
            const size = this.n * 4 + 5;
            this.cnt = new Int32Array(size);
            this.len = new Float64Array(size);
        }
        private pushUp(node: number, l: number, r: number): void {
            if (this.cnt[node] > 0) {
                this.len[node] = this.xs[r] - this.xs[l];
            } else if (r - l === 1) {
                this.len[node] = 0;
            } else {
                this.len[node] = this.len[node << 1] + this.len[(node << 1) | 1];
            }
        }
        private update(node: number, l: number, r: number, ql: number, qr: number, val: number): void {
            if (ql >= r || qr <= l) return;
            if (ql <= l && r <= qr) {
                this.cnt[node] += val;
                this.pushUp(node, l, r);
                return;
            }
            const mid = (l + r) >> 1;
            this.update(node << 1, l, mid, ql, qr, val);
            this.update((node << 1) | 1, mid, r, ql, qr, val);
            this.pushUp(node, l, r);
        }
        add(l: number, r: number, val: number): void {
            if (l < r) this.update(1, 0, this.n, l, r, val);
        }
        total(): number {
            return this.len[1];
        }
    }

    // First pass: compute total union area
    let seg = new SegTree(xs);
    let prevY = events.length ? events[0].y : 0;
    let totalArea = 0;
    let i = 0;
    while (i < events.length) {
        const curY = events[i].y;
        const deltaY = curY - prevY;
        if (deltaY > 0) {
            totalArea += seg.total() * deltaY;
        }
        while (i < events.length && events[i].y === curY) {
            const e = events[i];
            seg.add(e.l, e.r, e.type);
            i++;
        }
        prevY = curY;
    }

    // Second pass: locate split line
    const half = totalArea / 2;
    seg = new SegTree(xs);
    prevY = events.length ? events[0].y : 0;
    let acc = 0;
    i = 0;
    while (i < events.length) {
        const curY = events[i].y;
        const deltaY = curY - prevY;
        if (deltaY > 0) {
            const w = seg.total();
            if (w > 0) {
                const possible = acc + w * deltaY;
                if (possible >= half - 1e-12) {
                    return prevY + (half - acc) / w;
                }
                acc = possible;
            }
        }
        while (i < events.length && events[i].y === curY) {
            const e = events[i];
            seg.add(e.l, e.r, e.type);
            i++;
        }
        prevY = curY;
    }

    // Fallback (should not reach here)
    return xs[xs.length - 1];
}
```

## Php

```php
class SegmentTree {
    public array $cnt;
    public array $len;
    private array $xs;
    private int $n;

    public function __construct(array $xs) {
        $this->xs = $xs;
        $this->n = count($xs) - 1; // number of elementary intervals
        $size = $this->n * 4 + 5;
        $this->cnt = array_fill(0, $size, 0);
        $this->len = array_fill(0, $size, 0.0);
    }

    public function update(int $node, int $l, int $r, int $ql, int $qr, int $val): void {
        if ($qr <= $l || $r <= $ql) {
            return;
        }
        if ($ql <= $l && $r <= $qr) {
            $this->cnt[$node] += $val;
            $this->pushUp($node, $l, $r);
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->update($node * 2, $l, $mid, $ql, $qr, $val);
        $this->update($node * 2 + 1, $mid, $r, $ql, $qr, $val);
        $this->pushUp($node, $l, $r);
    }

    private function pushUp(int $node, int $l, int $r): void {
        if ($this->cnt[$node] > 0) {
            $this->len[$node] = $this->xs[$r] - $this->xs[$l];
        } else {
            if ($r - $l == 1) {
                $this->len[$node] = 0.0;
            } else {
                $this->len[$node] = $this->len[$node * 2] + $this->len[$node * 2 + 1];
            }
        }
    }
}

class Solution {

    /**
     * @param Integer[][] $squares
     * @return Float
     */
    function separateSquares($squares) {
        $xs = [];
        foreach ($squares as $sq) {
            $x = $sq[0];
            $l = $sq[2];
            $xs[] = $x;
            $xs[] = $x + $l;
        }
        sort($xs);
        $xs = array_values(array_unique($xs));
        $idxMap = [];
        foreach ($xs as $i => $val) {
            $idxMap[$val] = $i;
        }

        $events = []; // each event: ['y'=>..., 'type'=>1/-1, 'l'=>..., 'r'=>...]
        foreach ($squares as $sq) {
            [$x, $y, $l] = $sq;
            $xl = $idxMap[$x];
            $xr = $idxMap[$x + $l];
            $events[] = ['y' => $y, 'type' => 1, 'l' => $xl, 'r' => $xr];
            $events[] = ['y' => $y + $l, 'type' => -1, 'l' => $xl, 'r' => $xr];
        }

        usort($events, function ($a, $b) {
            if ($a['y'] == $b['y']) return 0;
            return ($a['y'] < $b['y']) ? -1 : 1;
        });

        $eventCount = count($events);
        if ($eventCount === 0) {
            return 0.0;
        }

        $m = count($xs) - 1; // number of elementary x-intervals

        // First sweep to compute total union area
        $seg = new SegmentTree($xs);
        $coveredLen = 0.0;
        $totalArea = 0.0;
        $prevY = $events[0]['y'];
        $i = 0;
        while ($i < $eventCount) {
            $curY = $events[$i]['y'];
            $dy = $curY - $prevY;
            if ($dy > 0 && $coveredLen > 0.0) {
                $totalArea += $coveredLen * $dy;
            }
            while ($i < $eventCount && $events[$i]['y'] == $curY) {
                $e = $events[$i];
                $seg->update(1, 0, $m, $e['l'], $e['r'], $e['type']);
                $i++;
            }
            $coveredLen = $seg->len[1];
            $prevY = $curY;
        }

        $half = $totalArea / 2.0;

        // Second sweep to find the split line
        $seg = new SegmentTree($xs);
        $coveredLen = 0.0;
        $cum = 0.0;
        $prevY = $events[0]['y'];
        $i = 0;
        while (true) {
            if ($i >= $eventCount) {
                // Should not happen, but return last y just in case
                return (float)$prevY;
            }
            $curY = $events[$i]['y'];
            $dy = $curY - $prevY;
            if ($dy > 0 && $coveredLen > 0.0) {
                $area = $coveredLen * $dy;
                if ($cum + $area >= $half) {
                    $need = $half - $cum;
                    $ans = $prevY + $need / $coveredLen;
                    return (float)$ans;
                }
                $cum += $area;
            }
            while ($i < $eventCount && $events[$i]['y'] == $curY) {
                $e = $events[$i];
                $seg->update(1, 0, $m, $e['l'], $e['r'], $e['type']);
                $i++;
            }
            $coveredLen = $seg->len[1];
            $prevY = $curY;
        }
    }
}
```

## Swift

```swift
class Solution {
    func separateSquares(_ squares: [[Int]]) -> Double {
        let n = squares.count
        var xVals = [Int64]()
        xVals.reserveCapacity(2 * n)
        struct RawSquare { var x: Int64; var y: Int64; var l: Int64 }
        var raw = [RawSquare]()
        raw.reserveCapacity(n)
        for sq in squares {
            let xi = Int64(sq[0])
            let yi = Int64(sq[1])
            let li = Int64(sq[2])
            raw.append(RawSquare(x: xi, y: yi, l: li))
            xVals.append(xi)
            xVals.append(xi + li)
        }
        // coordinate compression for x
        var xs = Array(Set(xVals)).sorted()
        var xIndex = [Int64: Int]()
        for (i, v) in xs.enumerated() {
            xIndex[v] = i
        }
        struct Event { var y: Int64; var type: Int; var lIdx: Int; var rIdx: Int }
        var events = [Event]()
        events.reserveCapacity(2 * n)
        for sq in raw {
            let lIdx = xIndex[sq.x]!
            let rIdx = xIndex[sq.x + sq.l]!
            events.append(Event(y: sq.y, type: 1, lIdx: lIdx, rIdx: rIdx))
            events.append(Event(y: sq.y + sq.l, type: -1, lIdx: lIdx, rIdx: rIdx))
        }
        events.sort { $0.y < $1.y }

        class SegmentTree {
            let xs: [Int64]
            var cnt: [Int]
            var len: [Int64]
            let n: Int
            init(_ xs: [Int64]) {
                self.xs = xs
                self.n = xs.count - 1
                let size = max(4 * n, 1)
                cnt = Array(repeating: 0, count: size)
                len = Array(repeating: 0, count: size)
            }
            private func pushUp(_ node: Int, _ l: Int, _ r: Int) {
                if cnt[node] > 0 {
                    len[node] = xs[r + 1] - xs[l]
                } else {
                    if l == r {
                        len[node] = 0
                    } else {
                        len[node] = len[node << 1] + len[(node << 1) | 1]
                    }
                }
            }
            private func update(_ node: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int, _ val: Int) {
                if ql > r || qr < l { return }
                if ql <= l && r <= qr {
                    cnt[node] += val
                    pushUp(node, l, r)
                    return
                }
                let mid = (l + r) >> 1
                update(node << 1, l, mid, ql, qr, val)
                update((node << 1) | 1, mid + 1, r, ql, qr, val)
                pushUp(node, l, r)
            }
            func update(l: Int, r: Int, val: Int) {
                if n <= 0 || l > r { return }
                update(1, 0, n - 1, l, r, val)
            }
            var totalLength: Int64 { len[1] }
        }

        // First pass to compute total union area
        let segTotal = SegmentTree(xs)
        var prevY = events.first?.y ?? 0
        var totalArea: Int64 = 0
        var idx = 0
        while idx < events.count {
            let curY = events[idx].y
            let dy = curY - prevY
            if dy > 0 {
                let covered = segTotal.totalLength
                totalArea += covered * dy
            }
            var j = idx
            while j < events.count && events[j].y == curY {
                let ev = events[j]
                segTotal.update(l: ev.lIdx, r: ev.rIdx - 1, val: ev.type)
                j += 1
            }
            prevY = curY
            idx = j
        }

        // Second pass to locate median line
        let target = Double(totalArea) / 2.0
        let seg = SegmentTree(xs)
        prevY = events.first?.y ?? 0
        var cumArea: Int64 = 0
        idx = 0
        while idx < events.count {
            let curY = events[idx].y
            let dy = curY - prevY
            if dy > 0 {
                let covered = seg.totalLength
                if covered > 0 {
                    let areaAdd = covered * dy
                    let newCum = cumArea + areaAdd
                    if Double(newCum) >= target {
                        let needed = target - Double(cumArea)
                        let yAns = Double(prevY) + needed / Double(covered)
                        return yAns
                    }
                    cumArea = newCum
                }
            }
            var j = idx
            while j < events.count && events[j].y == curY {
                let ev = events[j]
                seg.update(l: ev.lIdx, r: ev.rIdx - 1, val: ev.type)
                j += 1
            }
            prevY = curY
            idx = j
        }
        // Fallback (should not reach here)
        return Double(prevY)
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayList
import java.util.HashMap

class Solution {
    data class Event(val y: Long, val type: Int, val lIdx: Int, val rIdx: Int)

    class SegmentTree(private val xs: LongArray) {
        val n: Int = xs.size - 1
        private val cnt = IntArray(n * 4)
        private val len = LongArray(n * 4)

        fun update(node: Int, l: Int, r: Int, ql: Int, qr: Int, delta: Int) {
            if (qr <= l || r <= ql) return
            if (ql <= l && r <= qr) {
                cnt[node] += delta
            } else {
                val mid = (l + r) ushr 1
                update(node shl 1, l, mid, ql, qr, delta)
                update((node shl 1) + 1, mid, r, ql, qr, delta)
            }
            if (cnt[node] > 0) {
                len[node] = xs[r] - xs[l]
            } else {
                if (l + 1 == r) {
                    len[node] = 0L
                } else {
                    len[node] = len[node shl 1] + len[(node shl 1) + 1]
                }
            }
        }

        fun totalLength(): Long = len[1]
    }

    fun separateSquares(squares: Array<IntArray>): Double {
        val n = squares.size
        val xsTmp = LongArray(2 * n)
        var pos = 0
        for (sq in squares) {
            val x = sq[0].toLong()
            val l = sq[2].toLong()
            xsTmp[pos++] = x
            xsTmp[pos++] = x + l
        }
        val xsList = xsTmp.distinct().sorted()
        val xs = LongArray(xsList.size) { xsList[it] }

        val coordToIdx = HashMap<Long, Int>(xs.size * 2)
        for (i in xs.indices) {
            coordToIdx[xs[i]] = i
        }

        val events = ArrayList<Event>()
        for (sq in squares) {
            val x = sq[0].toLong()
            val y = sq[1].toLong()
            val l = sq[2].toLong()
            val left = coordToIdx[x]!!
            val right = coordToIdx[x + l]!!
            events.add(Event(y, 1, left, right))
            events.add(Event(y + l, -1, left, right))
        }
        events.sortWith(compareBy<Event> { it.y }.thenBy { it.type }) // removals (-1) before additions (+1)

        val seg = SegmentTree(xs)

        var prevY = events[0].y
        var totalArea = 0L
        var i = 0
        while (i < events.size) {
            val curY = events[i].y
            val deltaY = curY - prevY
            if (deltaY > 0) {
                totalArea += seg.totalLength() * deltaY
            }
            var j = i
            while (j < events.size && events[j].y == curY) {
                val e = events[j]
                seg.update(1, 0, seg.n, e.lIdx, e.rIdx, e.type)
                j++
            }
            prevY = curY
            i = j
        }

        val target = totalArea / 2.0

        // second sweep to locate the line
        val seg2 = SegmentTree(xs)
        var cum = 0.0
        prevY = events[0].y
        i = 0
        while (i < events.size) {
            val curY = events[i].y
            val deltaY = curY - prevY
            if (deltaY > 0) {
                val len = seg2.totalLength().toDouble()
                if (len > 0.0) {
                    val areaSeg = len * deltaY.toDouble()
                    if (cum + areaSeg >= target) {
                        val needed = (target - cum) / len
                        return prevY.toDouble() + needed
                    }
                    cum += areaSeg
                }
            }
            var j = i
            while (j < events.size && events[j].y == curY) {
                val e = events[j]
                seg2.update(1, 0, seg2.n, e.lIdx, e.rIdx, e.type)
                j++
            }
            prevY = curY
            i = j
        }

        return prevY.toDouble()
    }
}
```

## Dart

```dart
class _SegTree {
  List<int> cnt;
  List<int> len;
  List<int> xs;
  int n;
  _SegTree(this.xs) {
    n = xs.length - 1;
    cnt = List.filled(n * 4, 0);
    len = List.filled(n * 4, 0);
  }
  void _update(int node, int l, int r, int ql, int qr, int val) {
    if (ql >= r || qr <= l) return;
    if (ql <= l && r <= qr) {
      cnt[node] += val;
    } else {
      int mid = (l + r) >> 1;
      _update(node * 2, l, mid, ql, qr, val);
      _update(node * 2 + 1, mid, r, ql, qr, val);
    }
    if (cnt[node] > 0) {
      len[node] = xs[r] - xs[l];
    } else {
      if (l + 1 >= r) {
        len[node] = 0;
      } else {
        len[node] = len[node * 2] + len[node * 2 + 1];
      }
    }
  }

  void update(int lIdx, int rIdx, int val) {
    _update(1, 0, n, lIdx, rIdx, val);
  }

  int totalLen() => len[1];
}

class Solution {
  double separateSquares(List<List<int>> squares) {
    // coordinate compression for x
    List<int> xs = [];
    for (var s in squares) {
      xs.add(s[0]);
      xs.add(s[0] + s[2]);
    }
    xs.sort();
    List<int> uniq = [];
    for (int v in xs) {
      if (uniq.isEmpty || uniq.last != v) uniq.add(v);
    }
    xs = uniq;

    int lowerBound(int val) {
      int l = 0, r = xs.length;
      while (l < r) {
        int m = (l + r) >> 1;
        if (xs[m] < val)
          l = m + 1;
        else
          r = m;
      }
      return l;
    }

    // events: [y(double), type(int), leftIdx, rightIdx]
    List<List<dynamic>> events = [];
    for (var s in squares) {
      int x = s[0];
      int y = s[1];
      int l = s[2];
      int left = lowerBound(x);
      int right = lowerBound(x + l);
      events.add([y.toDouble(), 1, left, right]); // add
      events.add([(y + l).toDouble(), -1, left, right]); // remove
    }
    events.sort((a, b) => a[0].compareTo(b[0]));

    // First pass: total union area
    _SegTree seg = _SegTree(xs);
    double totalArea = 0.0;
    double prevY = events[0][0];
    int curLen = 0;
    int i = 0;
    while (i < events.length) {
      double y = events[i][0];
      double delta = y - prevY;
      if (delta > 0 && curLen > 0) {
        totalArea += curLen * delta;
      }
      while (i < events.length && events[i][0] == y) {
        int type = events[i][1];
        int lIdx = events[i][2];
        int rIdx = events[i][3];
        seg.update(lIdx, rIdx, type);
        i++;
      }
      curLen = seg.totalLen();
      prevY = y;
    }

    double half = totalArea / 2.0;

    // Second pass: find minimal y where area reaches half
    seg = _SegTree(xs);
    double cum = 0.0;
    prevY = events[0][0];
    curLen = 0;
    i = 0;
    while (i < events.length) {
      double y = events[i][0];
      double delta = y - prevY;
      if (delta > 0 && curLen > 0) {
        double possible = curLen * delta;
        if (cum + possible >= half) {
          double needed = half - cum;
          return prevY + needed / curLen;
        }
        cum += possible;
      }
      while (i < events.length && events[i][0] == y) {
        int type = events[i][1];
        int lIdx = events[i][2];
        int rIdx = events[i][3];
        seg.update(lIdx, rIdx, type);
        i++;
      }
      curLen = seg.totalLen();
      prevY = y;
    }

    // Fallback (should not happen)
    return prevY;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

type event struct {
	y   int64
	typ int // +1 add, -1 remove
	l   int
	r   int
}

type segTree struct {
	cnt    []int
	length []int64
	xs     []int64
	n      int
}

func newSegTree(n int, xs []int64) *segTree {
	return &segTree{
		cnt:    make([]int, 4*n),
		length: make([]int64, 4*n),
		xs:     xs,
		n:      n,
	}
}

func (st *segTree) Update(l, r, val int) {
	st.update(1, 0, st.n, l, r, val)
}

func (st *segTree) update(node, left, right, l, r, val int) {
	if l >= right || r <= left {
		return
	}
	if l <= left && right <= r {
		st.cnt[node] += val
	} else {
		mid := (left + right) >> 1
		st.update(node<<1, left, mid, l, r, val)
		st.update(node<<1|1, mid, right, l, r, val)
	}
	if st.cnt[node] > 0 {
		st.length[node] = st.xs[right] - st.xs[left]
	} else {
		if right-left == 1 {
			st.length[node] = 0
		} else {
			st.length[node] = st.length[node<<1] + st.length[node<<1|1]
		}
	}
}

func (st *segTree) Len() int64 {
	return st.length[1]
}

func separateSquares(squares [][]int) float64 {
	n := len(squares)
	if n == 0 {
		return 0.0
	}
	type sq struct{ x1, x2, y1, y2 int64 }
	tmp := make([]sq, n)
	xs := make([]int64, 0, 2*n)
	for i, s := range squares {
		x1 := int64(s[0])
		y1 := int64(s[1])
		l := int64(s[2])
		x2 := x1 + l
		y2 := y1 + l
		tmp[i] = sq{x1, x2, y1, y2}
		xs = append(xs, x1, x2)
	}
	sort.Slice(xs, func(i, j int) bool { return xs[i] < xs[j] })
	ux := make([]int64, 0, len(xs))
	for _, v := range xs {
		if len(ux) == 0 || ux[len(ux)-1] != v {
			ux = append(ux, v)
		}
	}
	getIdx := func(val int64) int {
		return sort.Search(len(ux), func(i int) bool { return ux[i] >= val })
	}
	events := make([]event, 0, 2*n)
	for _, s := range tmp {
		l := getIdx(s.x1)
		r := getIdx(s.x2)
		events = append(events, event{y: s.y1, typ: 1, l: l, r: r})
		events = append(events, event{y: s.y2, typ: -1, l: l, r: r})
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i].y == events[j].y {
			return events[i].typ > events[j].typ
		}
		return events[i].y < events[j].y
	})

	m := len(ux) - 1 // number of elementary x-intervals
	st := newSegTree(m, ux)

	// First sweep to compute total union area
	prevY := events[0].y
	var totalArea int64 = 0
	i := 0
	for i < len(events) {
		curY := events[i].y
		dy := curY - prevY
		if dy > 0 {
			covered := st.Len()
			totalArea += covered * dy
			prevY = curY
		}
		for i < len(events) && events[i].y == curY {
			st.Update(events[i].l, events[i].r, events[i].typ)
			i++
		}
	}

	half := float64(totalArea) / 2.0

	// Second sweep to locate split line
	st = newSegTree(m, ux)
	prevY = events[0].y
	var acc int64 = 0
	i = 0
	for i < len(events) {
		curY := events[i].y
		dy := curY - prevY
		if dy > 0 {
			covered := st.Len()
			if covered > 0 && float64(acc)+float64(covered)*float64(dy) >= half {
				need := half - float64(acc)
				return float64(prevY) + need/float64(covered)
			}
			acc += covered * dy
			prevY = curY
		}
		for i < len(events) && events[i].y == curY {
			st.Update(events[i].l, events[i].r, events[i].typ)
			i++
		}
	}
	return float64(prevY)
}
```

## Ruby

```ruby
def separate_squares(squares)
  xs = []
  raw_events = []

  squares.each do |x, y, l|
    xl = x
    xr = x + l
    xs << xl
    xs << xr
    bottom = y
    top = y + l
    raw_events << [bottom, 1, xl, xr]
    raw_events << [top, -1, xl, xr]
  end

  xs.uniq!
  xs.sort!
  index = {}
  xs.each_with_index { |v, i| index[v] = i }

  events = raw_events.map do |y, delta, xl, xr|
    [y, delta, index[xl], index[xr]]
  end
  events.sort_by! { |e| e[0] }

  # Segment tree for union length of x-intervals
  class SegTree
    def initialize(coords)
      @coords = coords
      @n = coords.length - 1
      size = @n * 4
      @cnt = Array.new(size, 0)
      @len = Array.new(size, 0)
    end

    def update(l, r, delta)
      _update(1, 0, @n, l, r, delta)
    end

    def total_len
      @len[1]
    end

    private

    def _push_up(node, l, r)
      if @cnt[node] > 0
        @len[node] = @coords[r] - @coords[l]
      else
        if l + 1 == r
          @len[node] = 0
        else
          @len[node] = @len[node * 2] + @len[node * 2 + 1]
        end
      end
    end

    def _update(node, l, r, ql, qr, delta)
      return if ql >= r || qr <= l
      if ql <= l && r <= qr
        @cnt[node] += delta
        _push_up(node, l, r)
        return
      end
      mid = (l + r) / 2
      _update(node * 2, l, mid, ql, qr, delta)
      _update(node * 2 + 1, mid, r, ql, qr, delta)
      _push_up(node, l, r)
    end
  end

  seg = SegTree.new(xs)

  cur_y = events[0][0]
  union_len = 0
  area = 0
  segments = [] # [y_start, y_end, length]

  i = 0
  while i < events.size
    y = events[i][0]
    dy = y - cur_y
    if dy > 0 && union_len > 0
      segments << [cur_y, y, union_len]
      area += union_len * dy
    end

    while i < events.size && events[i][0] == y
      _, delta, l_idx, r_idx = events[i]
      seg.update(l_idx, r_idx, delta)
      i += 1
    end

    union_len = seg.total_len
    cur_y = y
  end

  total_area = area.to_f
  half = total_area / 2.0

  cum = 0.0
  segments.each do |y_start, y_end, len|
    next if len == 0
    seg_area = len * (y_end - y_start)
    if cum + seg_area >= half
      needed = half - cum
      return y_start + needed / len.to_f
    else
      cum += seg_area
    end
  end

  cur_y.to_f
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.ArrayBuffer

  def separateSquares(squares: Array[Array[Int]]): Double = {
    val n = squares.length
    // Precompute min bottom and max top for bounds
    var minY = Long.MaxValue
    var maxY = Long.MinValue
    var i = 0
    while (i < n) {
      val y = squares(i)(1).toLong
      val l = squares(i)(2).toLong
      if (y < minY) minY = y
      if (y + l > maxY) maxY = y + l
      i += 1
    }

    // Segment tree class
    class SegTree(val ys: Array[Double]) {
      val segN: Int = ys.length - 1
      private val cnt = new Array[Int](segN * 4)
      private val len = new Array[Double](segN * 4)

      def update(node: Int, l: Int, r: Int, ql: Int, qr: Int, delta: Int): Unit = {
        if (ql >= r || qr <= l) return
        if (ql <= l && r <= qr) {
          cnt(node) += delta
        } else {
          val mid = (l + r) >>> 1
          update(node << 1, l, mid, ql, qr, delta)
          update(node << 1 | 1, mid, r, ql, qr, delta)
        }
        if (cnt(node) > 0) {
          len(node) = ys(r) - ys(l)
        } else if (l + 1 == r) {
          len(node) = 0.0
        } else {
          len(node) = len(node << 1) + len(node << 1 | 1)
        }
      }

      def totalLen: Double = if (segN > 0) len(1) else 0.0
    }

    case class Event(x: Long, typ: Int, l: Int, r: Int)

    // Compute union area of squares below given y
    def areaBelow(y: Double): Double = {
      val rects = new ArrayBuffer[(Long, Long, Double, Double)]()
      var idx = 0
      while (idx < n) {
        val xi = squares(idx)(0).toLong
        val yi = squares(idx)(1).toLong
        val li = squares(idx)(2).toLong
        if (y > yi) {
          val top = math.min(yi + li, y)
          rects += ((xi, xi + li, yi.toDouble, top))
        }
        idx += 1
      }
      if (rects.isEmpty) return 0.0

      // collect y-coordinates for compression
      val ysBuf = new ArrayBuffer[Double]()
      rects.foreach { r =>
        ysBuf += r._3
        ysBuf += r._4
      }
      val ysSorted = ysBuf.distinct.sorted.toArray
      if (ysSorted.length <= 1) return 0.0

      // build events
      val events = new ArrayBuffer[Event]()
      rects.foreach { r =>
        val lIdx = java.util.Arrays.binarySearch(ysSorted, r._3)
        val rIdx = java.util.Arrays.binarySearch(ysSorted, r._4)
        events += Event(r._1, 1, lIdx, rIdx)
        events += Event(r._2, -1, lIdx, rIdx)
      }
      events.sortInPlaceBy(_.x)

      val seg = new SegTree(ysSorted)
      var prevX = events(0).x
      var coveredY = 0.0
      var area = 0.0
      var eIdx = 0
      while (eIdx < events.length) {
        val curX = events(eIdx).x
        val dx = curX - prevX
        if (dx != 0 && coveredY > 0) {
          area += coveredY * dx.toDouble
        }
        // process all events at curX
        var j = eIdx
        while (j < events.length && events(j).x == curX) {
          val ev = events(j)
          seg.update(1, 0, seg.segN, ev.l, ev.r, ev.typ)
          j += 1
        }
        coveredY = seg.totalLen
        prevX = curX
        eIdx = j
      }
      area
    }

    // total union area
    val totalArea = areaBelow(maxY.toDouble)
    val target = totalArea / 2.0

    var lo = minY.toDouble
    var hi = maxY.toDouble
    var iter = 0
    while (iter < 60) {
      val mid = (lo + hi) * 0.5
      if (areaBelow(mid) >= target) hi = mid else lo = mid
      iter += 1
    }
    hi
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

#[derive(Clone)]
struct Event {
    y: i64,
    typ: i32, // +1 add, -1 remove
    l: usize,
    r: usize,
}

struct SegTree {
    n: usize,
    cnt: Vec<i32>,
    len: Vec<i64>,
    span: Vec<i64>,
}

impl SegTree {
    fn new(xs: &Vec<i64>) -> Self {
        let m = xs.len() - 1; // number of elementary intervals
        let size = 4 * m + 5;
        let mut st = SegTree {
            n: m,
            cnt: vec![0; size],
            len: vec![0; size],
            span: vec![0; size],
        };
        st.build(1, 0, m, xs);
        st
    }

    fn build(&mut self, node: usize, l: usize, r: usize, xs: &Vec<i64>) {
        if l + 1 == r {
            self.span[node] = xs[r] - xs[l];
            self.len[node] = 0;
            return;
        }
        let mid = (l + r) / 2;
        self.build(node * 2, l, mid, xs);
        self.build(node * 2 + 1, mid, r, xs);
        self.span[node] = self.span[node * 2] + self.span[node * 2 + 1];
        self.len[node] = 0;
    }

    fn push_up(&mut self, node: usize) {
        if self.cnt[node] > 0 {
            self.len[node] = self.span[node];
        } else {
            if node * 2 < self.cnt.len() {
                self.len[node] = self.len[node * 2] + self.len[node * 2 + 1];
            }
        }
    }

    fn update(&mut self, ql: usize, qr: usize, delta: i32) {
        self.update_rec(1, 0, self.n, ql, qr, delta);
    }

    fn update_rec(
        &mut self,
        node: usize,
        l: usize,
        r: usize,
        ql: usize,
        qr: usize,
        delta: i32,
    ) {
        if ql >= r || qr <= l {
            return;
        }
        if ql <= l && r <= qr {
            self.cnt[node] += delta;
            self.push_up(node);
            return;
        }
        let mid = (l + r) / 2;
        self.update_rec(node * 2, l, mid, ql, qr, delta);
        self.update_rec(node * 2 + 1, mid, r, ql, qr, delta);
        self.push_up(node);
    }

    fn total_len(&self) -> i64 {
        if self.cnt[1] > 0 {
            self.span[1]
        } else {
            self.len[1]
        }
    }
}

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let n = squares.len();
        let mut xs: Vec<i64> = Vec::with_capacity(2 * n);
        let mut raw_events: Vec<(i64, i32, i64, i64)> = Vec::with_capacity(2 * n);

        for sq in &squares {
            let xi = sq[0] as i64;
            let yi = sq[1] as i64;
            let li = sq[2] as i64;
            let xl = xi;
            let xr = xi + li;
            let yb = yi;
            let yt = yi + li;
            xs.push(xl);
            xs.push(xr);
            raw_events.push((yb, 1, xl, xr)); // add
            raw_events.push((yt, -1, xl, xr)); // remove
        }

        xs.sort_unstable();
        xs.dedup();

        let mut events: Vec<Event> = Vec::with_capacity(raw_events.len());
        for (y, typ, xl, xr) in raw_events {
            let l = xs.binary_search(&xl).unwrap();
            let r = xs.binary_search(&xr).unwrap();
            events.push(Event { y, typ, l, r });
        }

        events.sort_by(|a, b| a.y.cmp(&b.y));

        // First pass: compute total area
        let mut seg = SegTree::new(&xs);
        let mut prev_y = events[0].y;
        let mut total_area_f64: f64 = 0.0;

        let mut i = 0;
        while i < events.len() {
            let cur_y = events[i].y;
            let dy = cur_y - prev_y;
            if dy > 0 {
                let L = seg.total_len();
                total_area_f64 += (L as f64) * (dy as f64);
            }
            // apply all events at cur_y
            while i < events.len() && events[i].y == cur_y {
                let ev = &events[i];
                seg.update(ev.l, ev.r, ev.typ);
                i += 1;
            }
            prev_y = cur_y;
        }

        // No more intervals after last event (area zero)

        let half_target = total_area_f64 / 2.0;

        // Second pass: find y
        let mut seg2 = SegTree::new(&xs);
        let mut cum_f64: f64 = 0.0;
        prev_y = events[0].y;
        i = 0;
        while i < events.len() {
            let cur_y = events[i].y;
            let dy = cur_y - prev_y;
            if dy > 0 {
                let L = seg2.total_len();
                if L > 0 {
                    let area_add = (L as f64) * (dy as f64);
                    if cum_f64 + area_add >= half_target - 1e-12 {
                        let remaining = half_target - cum_f64;
                        let ans = (prev_y as f64) + remaining / (L as f64);
                        return ans;
                    }
                    cum_f64 += area_add;
                }
            }
            while i < events.len() && events[i].y == cur_y {
                let ev = &events[i];
                seg2.update(ev.l, ev.r, ev.typ);
                i += 1;
            }
            prev_y = cur_y;
        }

        // If not found inside intervals (should not happen), return last y
        prev_y as f64
    }
}
```

## Racket

```racket
(define (separate-squares squares)
  (let* ((xs-list
          (let loop ((lst squares) (acc '()))
            (if (null? lst)
                acc
                (let* ((sq (car lst))
                       (x (list-ref sq 0))
                       (l (list-ref sq 2)))
                  (loop (cdr lst)
                        (cons x (cons (+ x l) acc)))))))
         (xs-sorted (remove-duplicates (sort xs-list <)))
         (xs (list->vector xs-sorted))
         (m (vector-length xs))
         (x->idx
          (let ((h (make-hash)))
            (for ([i (in-range m)])
              (hash-set! h (vector-ref xs i) i))
            h))
         ;; events: vector of #[y type l r]
         (events
          (let loop ((lst squares) (ev '()))
            (if (null? lst)
                ev
                (let* ((sq (car lst))
                       (x (list-ref sq 0))
                       (y (list-ref sq 1))
                       (l (list-ref sq 2))
                       (x1 x)
                       (x2 (+ x l))
                       (y1 y)
                       (y2 (+ y l))
                       (lidx (hash-ref x->idx x1))
                       (ridx (hash-ref x->idx x2)))
                  (loop (cdr lst)
                        (cons (vector y1 1 lidx ridx)
                              (cons (vector y2 -1 lidx ridx) ev))))))))
         (sorted-events
          (list->vector (sort events (lambda (a b) (< (vector-ref a 0) (vector-ref b 0))))))
         (nevents (vector-length sorted-events))
         ;; segment tree
         (cnt (make-vector (* 4 m) 0))
         (len (make-vector (* 4 m) 0.0))
         (seg-update
          (letrec ((upd (lambda (node l r ql qr delta)
                          (when (and (< ql r) (> qr l)) ; overlap exists
                            (if (and (<= ql l) (>= qr r))
                                (vector-set! cnt node (+ (vector-ref cnt node) delta)))
                            (let ((mid (/ (+ l r) 2)))
                              (when (< (- r l) 2) ; not a leaf, recurse
                                (upd (* 2 node) l mid ql qr delta)
                                (upd (+ (* 2 node) 1) mid r ql qr delta))
                              (if (> (vector-ref cnt node) 0)
                                  (vector-set! len node (- (vector-ref xs r) (vector-ref xs l)))
                                  (if (< (- r l) 2)
                                      (vector-set! len node 0.0)
                                      (vector-set! len node (+ (vector-ref len (* 2 node))
                                                               (vector-ref len (+ (* 2 node) 1))))))))))
            (lambda (ql qr delta)
              (upd 1 0 m ql qr delta)))))
    ;; sweep line, collect slabs
    (let loop ((i 0) (prev-y (if (= nevents 0) 0 (vector-ref sorted-events 0 0)))
               (starts '()) (ends '()) (lens '()))
      (if (= i nevents)
          (let* ((start-vec (list->vector (reverse starts)))
                 (end-vec   (list->vector (reverse ends)))
                 (len-vec   (list->vector (reverse lens)))
                 (ns (vector-length start-vec))
                 (total-area
                  (let sum ((k 0) (acc 0.0))
                    (if (= k ns)
                        acc
                        (sum (+ k 1)
                             (+ acc (* (vector-ref len-vec k)
                                       (- (vector-ref end-vec k) (vector-ref start-vec k))))))))
                 (target (/ total-area 2.0)))
            ;; find from top down
            (let find ((k (- ns 1)) (rem total-area))
              (if (< k 0)
                  0.0
                  (let* ((h (- (vector-ref end-vec k) (vector-ref start-vec k)))
                         (L (vector-ref len-vec k))
                         (area (* L h)))
                    (if (<= (- rem area) target)
                        (let* ((need (- rem target))
                               (d (/ need L))
                               (ans (- (vector-ref end-vec k) d)))
                          ans)
                        (find (- k 1) (- rem area))))))))
          ;; process next group of events with same y
          (let* ((curr-y (vector-ref sorted-events i 0))
                 (delta   (- curr-y prev-y))
                 (cur-len (if (= i 0) 0.0 (vector-ref len 1))))
            (when (> delta 0)
              (set! starts (cons prev-y starts))
              (set! ends   (cons curr-y ends))
              (set! lens   (cons cur-len lens)))
            ;; apply all events at curr-y
            (let apply ((j i))
              (if (or (= j nevents) (not (= (vector-ref sorted-events j 0) curr-y)))
                  (loop j curr-y starts ends lens)
                  (let* ((ev   (vector-ref sorted-events j))
                         (type (vector-ref ev 1))
                         (lidx (vector-ref ev 2))
                         (ridx (vector-ref ev 3)))
                    (seg-update lidx ridx type)
                    (apply (+ j 1))))))))))
```

## Erlang

```erlang
-spec separate_squares(Squares :: [[integer()]]) -> float().
separate_squares(Squares) ->
    %% collect x coordinates for compression
    XsList = lists:foldl(fun([X, _Y, L], Acc) ->
                                 [X, X + L | Acc]
                         end, [], Squares),
    XsSorted = lists:usort(XsList),
    XsTuple = list_to_tuple(XsSorted),
    %% map x value to its index (1‑based)
    IndexMap = maps:from_list(
                 lists:zip(XsSorted,
                           lists:seq(1, length(XsSorted)))),
    %% build events {Y, Type (+1 add / -1 remove), LIdx, RIdx}
    Events0 = lists:foldl(fun([X, Y, L], Acc) ->
                                  X2 = X + L,
                                  IdxL = maps:get(X, IndexMap),
                                  IdxR = maps:get(X2, IndexMap) - 1,
                                  [{Y, 1, IdxL, IdxR},
                                   {Y + L, -1, IdxL, IdxR} | Acc]
                          end, [], Squares),
    EventsSorted = lists:keysort(1, Events0),

    %% sweep to collect segments and total area
    {SegmentsRev, TotalArea, _Map, CurLen, PrevY} =
        sweep_collect(EventsSorted, XsTuple, [], 0.0, #{}, 0, undefined),
    Segments = lists:reverse(SegmentsRev),

    Half = TotalArea / 2.0,
    find_answer(Segments, Half).

%% --------------------------------------------------------------------
%% Sweep to collect constant‑length segments.
%% Returns {SegmentsAcc, TotalArea, FinalMap, CurLen, PrevY}
sweep_collect([], _XsTuple, SegAcc, TotArea, Map, CurLen, PrevY) ->
    %% no more events
    {SegAcc, TotArea, Map, CurLen, PrevY};
sweep_collect(Events, XsTuple, SegAcc, TotArea, Map, CurLen, PrevY) ->
    [{Y, _, _, _} | _] = Events,
    case PrevY of
        undefined -> % first event, no area before it
            NewPrevY = Y,
            {NewMap, NewCurLen} = process_at_y(Events, XsTuple, Y, Map),
            sweep_collect(skip_same_y(Y, Events), XsTuple,
                         SegAcc, TotArea, NewMap, NewCurLen, NewPrevY);
        _ ->
            Delta = Y - PrevY,
            AreaAdd = CurLen * Delta,
            NewSegAcc = if Delta > 0 -> [{PrevY, Y, CurLen} | SegAcc];
                        true -> SegAcc
                       end,
            NewTotArea = TotArea + AreaAdd,
            {NewMap, NewCurLen} = process_at_y(Events, XsTuple, Y, Map),
            sweep_collect(skip_same_y(Y, Events), XsTuple,
                         NewSegAcc, NewTotArea, NewMap, NewCurLen, Y)
    end.

%% Process all events having the same Y, updating the segment tree.
process_at_y(Events, XsTuple, Y, Map) ->
    {Remaining, UpdatedMap} = process_events_same_y(Events, XsTuple, Y, Map),
    CurLen = get_len(UpdatedMap, 1, XsTuple),
    {UpdatedMap, CurLen},
    %% return remaining events for next iteration
    Remaining.

process_events_same_y([], _XsTuple, _Y, Map) ->
    {[], Map};
process_events_same_y([{Y, Type, LIdx, RIdx} = E | Rest], XsTuple, Y, Map) when Y == Y ->
    NewMap = seg_update(1, 1, size(XsTuple)-1, LIdx, RIdx, Type, XsTuple, Map),
    process_events_same_y(Rest, XsTuple, Y, NewMap);
process_events_same_y(Events, _XsTuple, _Y, Map) ->
    {Events, Map}.

skip_same_y(_Y, []) -> [];
skip_same_y(Y, [{Y2, _, _, _}=E | Rest]) when Y2 == Y ->
    skip_same_y(Y, Rest);
skip_same_y(_, Events) -> Events.

%% --------------------------------------------------------------------
%% Segment tree update (range add delta)
seg_update(Node, L, R, QL, QR, Delta, XsTuple, Map) ->
    if QL > R orelse QR < L ->
            Map;
       true ->
            case maps:get(Node, Map, {0,0}) of
                {Cnt, Len} when L == R ->
                    NewCnt = Cnt + Delta,
                    NewLen = if NewCnt > 0 -> element(L+1, XsTuple) - element(L, XsTuple);
                                true -> 0 end,
                    maps:put(Node, {NewCnt, NewLen}, Map);
                _ ->
                    Mid = (L + R) div 2,
                    Map1 = seg_update(Node*2, L, Mid, QL, QR, Delta, XsTuple, Map),
                    Map2 = seg_update(Node*2+1, Mid+1, R, QL, QR, Delta, XsTuple, Map1),
                    {Cnt0,_} = maps:get(Node, Map2, {0,0}),
                    LenLeft  = get_len(Map2, Node*2, XsTuple),
                    LenRight = get_len(Map2, Node*2+1, XsTuple),
                    NewLen = if Cnt0 > 0 -> element(R+1, XsTuple) - element(L, XsTuple);
                                true -> LenLeft + LenRight end,
                    maps:put(Node, {Cnt0, NewLen}, Map2)
            end
    end.

get_len(Map, Node, _XsTuple) ->
    case maps:get(Node, Map, undefined) of
        undefined -> 0;
        {_Cnt, Len} -> Len
    end.

%% --------------------------------------------------------------------
%% Find the answer y given segments and half area.
find_answer([], _Half) -> 0.0; % should not happen
find_answer([{Y1, Y2, Len} | Rest], Half) ->
    SegmentArea = Len * (Y2 - Y1),
    if Half =< SegmentArea ->
            Y1 + Half / Len;
       true ->
            find_answer(Rest, Half - SegmentArea)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec separate_squares(squares :: [[integer]]) :: float
  def separate_squares(squares) do
    # collect and compress x-coordinates
    xs =
      squares
      |> Enum.flat_map(fn [x, _y, l] -> [x, x + l] end)
      |> Enum.uniq()
      |> Enum.sort()

    xs_tuple = List.to_tuple(xs)

    coord_to_idx =
      xs
      |> Enum.with_index()
      |> Enum.into(%{}, fn {c, i} -> {c, i} end)

    seg_n = tuple_size(xs_tuple) - 1

    # build events: {y, delta, l_idx, r_idx}
    events =
      squares
      |> Enum.flat_map(fn [x, y, l] ->
        left = Map.fetch!(coord_to_idx, x)
        right_excl = Map.fetch!(coord_to_idx, x + l) - 1

        [
          {y, 1, left, right_excl},
          {y + l, -1, left, right_excl}
        ]
      end)
      |> Enum.sort_by(fn {y, _, _, _} -> y end)

    # group events by same y
    groups = Enum.chunk_by(events, fn {y, _, _, _} -> y end)

    # first sweep to get total union area
    total_area =
      sweep_total(groups, xs_tuple, seg_n)

    half = total_area / 2.0

    # second sweep to find answer
    find_answer(groups, xs_tuple, seg_n, half)
  end

  defp sweep_total(groups, xs_tuple, seg_n) do
    {cover_arr, len_arr} = build_arrays(seg_n)
    [{first_event | _}] = groups
    first_y = elem(first_event, 0)

    {_prev_y, total, _c, _l} =
      Enum.reduce(groups, {first_y, 0.0, cover_arr, len_arr}, fn group,
                                                               {prev_y, acc_area,
                                                                cov, ln} ->
        y = elem(hd(group), 0)
        width = :array.get(1, ln)
        delta_h = y - prev_y
        area_add = (width * delta_h) * 1.0
        new_acc = acc_area + area_add

        {new_cov, new_len} =
          Enum.reduce(group, {cov, ln}, fn {_y, delta, l_idx, r_idx},
                                            {c_acc, l_acc} ->
            update_range(c_acc, l_acc, 1, 0, seg_n - 1, l_idx, r_idx,
              delta, xs_tuple)
          end)

        {y, new_acc, new_cov, new_len}
      end)

    total
  end

  defp find_answer(groups, xs_tuple, seg_n, half) do
    {cover_arr, len_arr} = build_arrays(seg_n)
    [{first_event | _}] = groups
    first_y = elem(first_event, 0)

    Enum.reduce_while(groups, {first_y, 0.0, cover_arr, len_arr},
      fn group,
         {prev_y, acc_area, cov, ln} ->
        y = elem(hd(group), 0)
        width = :array.get(1, ln)
        delta_h = y - prev_y
        area_add = (width * delta_h) * 1.0

        if acc_area + area_add >= half do
          needed = half - acc_area
          ans = prev_y + needed / width
          {:halt, ans}
        else
          new_acc = acc_area + area_add

          {new_cov, new_len} =
            Enum.reduce(group, {cov, ln}, fn {_y, delta, l_idx, r_idx},
                                              {c_acc, l_acc} ->
              update_range(c_acc, l_acc, 1, 0, seg_n - 1, l_idx,
                r_idx, delta, xs_tuple)
            end)

          {:cont, {y, new_acc, new_cov, new_len}}
        end
      end)
  end

  defp build_arrays(seg_n) do
    size = seg_n * 4 + 5
    cover_arr = :array.new(size, default: 0)
    len_arr = :array.new(size, default: 0)
    {cover_arr, len_arr}
  end

  # updates segment tree for interval [ql, qr] (inclusive) with delta (+1 or -1)
  defp update_range(cover_arr, len_arr, idx, l, r, ql, qr, delta,
         xs_tuple) do
    cond do
      ql > r or qr < l ->
        {cover_arr, len_arr}

      ql <= l and r <= qr ->
        cur = :array.get(idx, cover_arr)
        new_cover = cur + delta
        cov2 = :array.set(idx, new_cover, cover_arr)

        len_val =
          if new_cover > 0 do
            elem(xs_tuple, r + 1) - elem(xs_tuple, l)
          else
            if l == r do
              0
            else
              left_len = :array.get(idx * 2, len_arr)
              right_len = :array.get(idx * 2 + 1, len_arr)
              left_len + right_len
            end
          end

        len2 = :array.set(idx, len_val, len_arr)
        {cov2, len2}

      true ->
        mid = div(l + r, 2)
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        {c1, l1} =
          update_range(cover_arr, len_arr, left_idx, l, mid,
            ql, qr, delta, xs_tuple)

        {c2, l2} =
          update_range(c1, l1, right_idx, mid + 1, r,
            ql, qr, delta, xs_tuple)

        cur_cover = :array.get(idx, c2)

        len_val =
          if cur_cover > 0 do
            elem(xs_tuple, r + 1) - elem(xs_tuple, l)
          else
            if l == r do
              0
            else
              left_len = :array.get(left_idx, l2)
              right_len = :array.get(right_idx, l2)
              left_len + right_len
            end
          end

        len3 = :array.set(idx, len_val, l2)
        {c2, len3}
    end
  end
end
```

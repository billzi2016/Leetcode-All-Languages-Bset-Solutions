# 0850. Rectangle Area II

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    struct Event{
        int y;
        int type; // +1 add, -1 remove
        int x1, x2;
        bool operator<(const Event& other) const{
            return y < other.y;
        }
    };
    
    vector<long long> xs;
    vector<int> cnt;
    vector<long long> segLen;
    
    void update(int node, int l, int r, int ql, int qr, int val){
        if (qr <= l || r <= ql) return;
        if (ql <= l && r <= qr){
            cnt[node] += val;
        } else {
            int mid = (l + r) >> 1;
            update(node<<1, l, mid, ql, qr, val);
            update(node<<1|1, mid, r, ql, qr, val);
        }
        if (cnt[node] > 0){
            segLen[node] = xs[r] - xs[l];
        } else {
            if (l + 1 == r) segLen[node] = 0;
            else segLen[node] = segLen[node<<1] + segLen[node<<1|1];
        }
    }
    
    int rectangleArea(vector<vector<int>>& rectangles) {
        vector<Event> events;
        xs.clear();
        for (auto &rec : rectangles){
            int x1 = rec[0], y1 = rec[1], x2 = rec[2], y2 = rec[3];
            events.push_back({y1, 1, x1, x2});
            events.push_back({y2, -1, x1, x2});
            xs.push_back(x1);
            xs.push_back(x2);
        }
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        int m = xs.size();
        cnt.assign(4*m, 0);
        segLen.assign(4*m, 0);
        
        sort(events.begin(), events.end());
        long long area = 0;
        int prevY = events[0].y;
        for (size_t i = 0; i < events.size(); ){
            int curY = events[i].y;
            long long dy = (long long)curY - prevY;
            if (dy){
                area = (area + segLen[1] % MOD * (dy % MOD)) % MOD;
                prevY = curY;
            }
            // process all events at curY
            while (i < events.size() && events[i].y == curY){
                int l = lower_bound(xs.begin(), xs.end(), events[i].x1) - xs.begin();
                int r = lower_bound(xs.begin(), xs.end(), events[i].x2) - xs.begin();
                update(1, 0, m-1, l, r, events[i].type);
                ++i;
            }
        }
        return (int)(area % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    private static class Event implements Comparable<Event> {
        int y;
        int x1Idx, x2Idx; // indices in compressed coordinates
        int type; // +1 add, -1 remove

        Event(int y, int x1Idx, int x2Idx, int type) {
            this.y = y;
            this.x1Idx = x1Idx;
            this.x2Idx = x2Idx;
            this.type = type;
        }

        @Override
        public int compareTo(Event o) {
            return Integer.compare(this.y, o.y);
        }
    }

    private static class SegTree {
        int[] count;
        long[] length;
        int n; // number of elementary intervals (xs.length - 1)
        int[] xs;

        SegTree(int[] xs) {
            this.xs = xs;
            this.n = xs.length - 1;
            this.count = new int[4 * n];
            this.length = new long[4 * n];
        }

        void update(int node, int l, int r, int ql, int qr, int val) {
            if (qr < l || r < ql) return;
            if (ql <= l && r <= qr) {
                count[node] += val;
            } else {
                int mid = (l + r) >>> 1;
                update(node << 1, l, mid, ql, qr, val);
                update(node << 1 | 1, mid + 1, r, ql, qr, val);
            }
            if (count[node] > 0) {
                length[node] = (long) xs[r + 1] - xs[l];
            } else {
                if (l == r) {
                    length[node] = 0;
                } else {
                    length[node] = length[node << 1] + length[node << 1 | 1];
                }
            }
        }

        long query() {
            return length[1];
        }
    }

    public int rectangleArea(int[][] rectangles) {
        int m = rectangles.length;
        // collect x coordinates
        java.util.List<Integer> xsList = new java.util.ArrayList<>(2 * m);
        for (int[] rec : rectangles) {
            xsList.add(rec[0]);
            xsList.add(rec[2]);
        }
        int[] xs = xsList.stream().distinct().sorted().mapToInt(Integer::intValue).toArray();

        // map x to index
        java.util.Map<Integer, Integer> xIndex = new java.util.HashMap<>();
        for (int i = 0; i < xs.length; ++i) {
            xIndex.put(xs[i], i);
        }

        // create events
        Event[] events = new Event[2 * m];
        int idx = 0;
        for (int[] rec : rectangles) {
            int y1 = rec[1];
            int y2 = rec[3];
            int x1Idx = xIndex.get(rec[0]);
            int x2Idx = xIndex.get(rec[2]);
            events[idx++] = new Event(y1, x1Idx, x2Idx, 1);   // add
            events[idx++] = new Event(y2, x1Idx, x2Idx, -1);  // remove
        }
        java.util.Arrays.sort(events);

        SegTree seg = new SegTree(xs);
        long area = 0;
        int prevY = events[0].y;

        for (Event e : events) {
            int curY = e.y;
            long coveredLen = seg.query();
            long deltaY = curY - prevY;
            area = (area + coveredLen % MOD * (deltaY % MOD)) % MOD;
            // update segment tree on interval [x1Idx, x2Idx-1]
            if (e.x1Idx < e.x2Idx) {
                seg.update(1, 0, seg.n - 1, e.x1Idx, e.x2Idx - 1, e.type);
            }
            prevY = curY;
        }

        return (int) (area % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        # collect and compress x-coordinates
        xs = sorted({x for rect in rectangles for x in (rect[0], rect[2])})
        xi = {v: i for i, v in enumerate(xs)}
        m = len(xs) - 1  # number of elementary segments

        # build events: (y, type, x1, x2)
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, 1, x1, x2))   # entering
            events.append((y2, -1, x1, x2))  # leaving
        events.sort()

        # segment tree arrays
        cnt = [0] * (4 * m)
        seg_len = [0] * (4 * m)

        def update(node, l, r, ql, qr, val):
            if ql >= r or qr <= l:
                return
            if ql <= l and r <= qr:
                cnt[node] += val
            else:
                mid = (l + r) // 2
                update(node * 2, l, mid, ql, qr, val)
                update(node * 2 + 1, mid, r, ql, qr, val)

            if cnt[node] > 0:
                seg_len[node] = xs[r] - xs[l]
            else:
                if l + 1 == r:   # leaf segment
                    seg_len[node] = 0
                else:
                    seg_len[node] = seg_len[node * 2] + seg_len[node * 2 + 1]

        prev_y = events[0][0]
        area = 0
        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy:
                area = (area + seg_len[1] * dy) % MOD
            update(1, 0, m, xi[x1], xi[x2], typ)
            prev_y = y

        return area % MOD
```

## Python3

```python
class Solution:
    def rectangleArea(self, rectangles):
        MOD = 10**9 + 7
        xs = set()
        events = []
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))
        xs = sorted(xs)
        xi = {x: i for i, x in enumerate(xs)}
        seg_len = [xs[i + 1] - xs[i] for i in range(len(xs) - 1)]
        n = len(seg_len)
        pref = [0]
        for v in seg_len:
            pref.append(pref[-1] + v)

        def range_sum(l, r):
            return pref[r] - pref[l]

        size = 4 * n
        cnt = [0] * size
        cov = [0] * size

        def update(node, l, r, ql, qr, val):
            if ql >= r or qr <= l:
                return
            if ql <= l and r <= qr:
                cnt[node] += val
            else:
                mid = (l + r) // 2
                update(node * 2, l, mid, ql, qr, val)
                update(node * 2 + 1, mid, r, ql, qr, val)
            if cnt[node] > 0:
                cov[node] = range_sum(l, r)
            else:
                if l + 1 == r:
                    cov[node] = 0
                else:
                    cov[node] = cov[node * 2] + cov[node * 2 + 1]

        events.sort()
        prev_y = events[0][0]
        area = 0
        for y, typ, x1, x2 in events:
            cur_len = cov[1]
            area = (area + cur_len * (y - prev_y)) % MOD
            l = xi[x1]
            r = xi[x2]
            update(1, 0, n, l, r, typ)
            prev_y = y
        return area % MOD
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

typedef struct {
    int y;
    int type;      // +1 for add, -1 for remove
    int x1Idx;
    int x2Idx;
} Event;

static int cmpLong(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

static int lowerBound(long long *arr, int n, long long target) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] < target)
            l = m + 1;
        else
            r = m;
    }
    return l;
}

/* Segment tree arrays are global within the function scope */
static void update(int node, int l, int r, int ql, int qr, int val,
                   long long *xs, int *cnt, long long *len) {
    if (qr <= l || r <= ql) return;
    if (ql <= l && r <= qr) {
        cnt[node] += val;
    } else {
        int mid = (l + r) >> 1;
        update(node << 1, l, mid, ql, qr, val, xs, cnt, len);
        update(node << 1 | 1, mid, r, ql, qr, val, xs, cnt, len);
    }
    if (cnt[node] > 0) {
        len[node] = xs[r] - xs[l];
    } else {
        if (l + 1 == r)
            len[node] = 0;
        else
            len[node] = len[node << 1] + len[node << 1 | 1];
    }
}

int rectangleArea(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    if (rectanglesSize == 0) return 0;

    /* Collect all x coordinates */
    long long *xs = (long long *)malloc(sizeof(long long) * rectanglesSize * 2);
    int xsCnt = 0;
    for (int i = 0; i < rectanglesSize; ++i) {
        xs[xsCnt++] = (long long)rectangles[i][0];
        xs[xsCnt++] = (long long)rectangles[i][2];
    }
    qsort(xs, xsCnt, sizeof(long long), cmpLong);
    /* Unique */
    int uniqCnt = 0;
    for (int i = 0; i < xsCnt; ++i) {
        if (i == 0 || xs[i] != xs[i - 1]) {
            xs[uniqCnt++] = xs[i];
        }
    }

    if (uniqCnt <= 1) {
        free(xs);
        return 0;
    }

    /* Build events */
    Event *events = (Event *)malloc(sizeof(Event) * rectanglesSize * 2);
    int evCnt = 0;
    for (int i = 0; i < rectanglesSize; ++i) {
        long long x1 = (long long)rectangles[i][0];
        long long y1 = (long long)rectangles[i][1];
        long long x2 = (long long)rectangles[i][2];
        long long y2 = (long long)rectangles[i][3];

        int l = lowerBound(xs, uniqCnt, x1);
        int r = lowerBound(xs, uniqCnt, x2);

        events[evCnt++] = (Event){(int)y1, +1, l, r};
        events[evCnt++] = (Event){(int)y2, -1, l, r};
    }

    /* Sort events by y */
    qsort(events, evCnt, sizeof(Event), cmpLong); // reuse cmpLong on y field via casting
    // Need proper comparator for Event based on y
    // We'll define a lambda-like static function
    // Since C doesn't support lambda, we create separate comparator

    /* Comparator for events */
    int (*cmpEvent)(const void *, const void *) = NULL;
    (void)cmpEvent; // placeholder to avoid unused warning

    /* Define comparator */
    int eventCmp(const void *a, const void *b) {
        const Event *ea = (const Event *)a;
        const Event *eb = (const Event *)b;
        if (ea->y < eb->y) return -1;
        if (ea->y > eb->y) return 1;
        return 0;
    }
    qsort(events, evCnt, sizeof(Event), eventCmp);

    int segCount = uniqCnt - 1; // number of elementary x-intervals
    int treeSize = segCount * 4 + 5;
    int *cnt = (int *)calloc(treeSize, sizeof(int));
    long long *len = (long long *)calloc(treeSize, sizeof(long long));

    long long area = 0;
    int prevY = events[0].y;

    for (int i = 0; i < evCnt; ++i) {
        int curY = events[i].y;
        long long coveredLen = len[1]; // total covered length at root
        long long dy = (long long)(curY - prevY);
        if (dy > 0 && coveredLen > 0) {
            area = (area + (coveredLen % MOD) * (dy % MOD)) % MOD;
        }
        update(1, 0, segCount, events[i].x1Idx, events[i].x2Idx,
               events[i].type, xs, cnt, len);
        prevY = curY;
    }

    free(xs);
    free(events);
    free(cnt);
    free(len);

    return (int)(area % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    private const int MOD = 1000000007;

    public int RectangleArea(int[][] rectangles) {
        var xs = new List<int>();
        var events = new List<(int y, int type, int x1Idx, int x2Idx)>();

        foreach (var rec in rectangles) {
            xs.Add(rec[0]);
            xs.Add(rec[2]);
        }

        xs = xs.Distinct().ToList();
        xs.Sort();

        var xIndex = new Dictionary<int, int>();
        for (int i = 0; i < xs.Count; i++) {
            xIndex[xs[i]] = i;
        }

        foreach (var rec in rectangles) {
            int x1 = rec[0], y1 = rec[1], x2 = rec[2], y2 = rec[3];
            int l = xIndex[x1];
            int r = xIndex[x2];
            events.Add((y1, 1, l, r));
            events.Add((y2, -1, l, r));
        }

        events.Sort((a, b) => a.y.CompareTo(b.y));

        var segTree = new SegmentTree(xs);
        long area = 0;
        int prevY = events[0].y;

        foreach (var ev in events) {
            int curY = ev.y;
            long coveredLen = segTree.TotalCoveredLength();
            area = (area + coveredLen * (curY - prevY)) % MOD;
            segTree.Update(ev.x1Idx, ev.x2Idx, ev.type);
            prevY = curY;
        }

        return (int)(area % MOD);
    }

    private class SegmentTree {
        private readonly int[] count;
        private readonly long[] length;
        private readonly List<int> xs;

        public SegmentTree(List<int> xs) {
            this.xs = xs;
            int n = xs.Count - 1; // number of elementary segments
            count = new int[n * 4];
            length = new long[n * 4];
        }

        public void Update(int l, int r, int val) {
            Update(1, 0, xs.Count - 1, l, r, val);
        }

        private void Update(int node, int left, int right, int ql, int qr, int val) {
            if (ql >= right || qr <= left) return;
            if (ql <= left && right <= qr) {
                count[node] += val;
            } else {
                int mid = (left + right) / 2;
                Update(node * 2, left, mid, ql, qr, val);
                Update(node * 2 + 1, mid, right, ql, qr, val);
            }

            if (count[node] > 0) {
                length[node] = (long)xs[right] - xs[left];
            } else {
                if (right - left == 1) {
                    length[node] = 0;
                } else {
                    length[node] = length[node * 2] + length[node * 2 + 1];
                }
            }
        }

        public long TotalCoveredLength() => length[1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var rectangleArea = function(rectangles) {
    const MOD = 1000000007n;
    let xs = [];
    let events = []; // {y, x1, x2, type}
    for (const [x1, y1, x2, y2] of rectangles) {
        xs.push(x1);
        xs.push(x2);
        events.push({ y: y1, x1, x2, type: 1 });
        events.push({ y: y2, x1, x2, type: -1 });
    }
    xs = Array.from(new Set(xs)).sort((a, b) => a - b);
    const xIndex = new Map();
    for (let i = 0; i < xs.length; i++) xIndex.set(xs[i], i);

    const n = xs.length;
    const segCount = new Array(4 * n).fill(0);
    const segLen = new Array(4 * n).fill(0n);

    function update(node, l, r, ql, qr, val) {
        if (qr <= l || r <= ql) return;
        if (ql <= l && r <= qr) {
            segCount[node] += val;
        } else {
            const mid = Math.floor((l + r) / 2);
            update(node * 2, l, mid, ql, qr, val);
            update(node * 2 + 1, mid, r, ql, qr, val);
        }
        if (segCount[node] > 0) {
            segLen[node] = BigInt(xs[r] - xs[l]);
        } else {
            if (r - l === 1) {
                segLen[node] = 0n;
            } else {
                segLen[node] = segLen[node * 2] + segLen[node * 2 + 1];
            }
        }
    }

    events.sort((a, b) => a.y - b.y);
    let prevY = events[0].y;
    let area = 0n;
    let i = 0;
    while (i < events.length) {
        const curY = events[i].y;
        const covered = segLen[1];
        area = (area + covered * BigInt(curY - prevY)) % MOD;

        while (i < events.length && events[i].y === curY) {
            const e = events[i];
            const l = xIndex.get(e.x1);
            const r = xIndex.get(e.x2);
            update(1, 0, n - 1, l, r, e.type);
            i++;
        }
        prevY = curY;
    }
    return Number((area + MOD) % MOD);
};
```

## Typescript

```typescript
function rectangleArea(rectangles: number[][]): number {
    const MOD = 1000000007n;

    // Collect all unique y-coordinates
    const yVals: number[] = [];
    for (const [ , y1, , y2] of rectangles) {
        yVals.push(y1, y2);
    }
    const ys = Array.from(new Set(yVals)).sort((a, b) => a - b);
    const yIndex = new Map<number, number>();
    for (let i = 0; i < ys.length; i++) {
        yIndex.set(ys[i], i);
    }

    interface Event { x: number; y1: number; y2: number; type: number; }
    const events: Event[] = [];

    for (const [x1, y1, x2, y2] of rectangles) {
        const iy1 = yIndex.get(y1)!;
        const iy2 = yIndex.get(y2)!;
        events.push({ x: x1, y1: iy1, y2: iy2, type: 1 });
        events.push({ x: x2, y1: iy1, y2: iy2, type: -1 });
    }

    events.sort((a, b) => a.x - b.x);

    class SegmentTree {
        cnt: number[];
        len: number[];
        ys: number[];
        n: number;
        constructor(ys: number[]) {
            this.ys = ys;
            this.n = ys.length - 1; // number of elementary intervals
            const size = this.n * 4 + 5;
            this.cnt = new Array(size).fill(0);
            this.len = new Array(size).fill(0);
        }
        update(l: number, r: number, val: number): void {
            this._update(1, 0, this.n, l, r, val);
        }
        private _update(node: number, left: number, right: number, ql: number, qr: number, val: number): void {
            if (ql >= right || qr <= left) return;
            if (ql <= left && right <= qr) {
                this.cnt[node] += val;
                this._pushUp(node, left, right);
                return;
            }
            const mid = (left + right) >> 1;
            this._update(node << 1, left, mid, ql, qr, val);
            this._update((node << 1) | 1, mid, right, ql, qr, val);
            this._pushUp(node, left, right);
        }
        private _pushUp(node: number, left: number, right: number): void {
            if (this.cnt[node] > 0) {
                this.len[node] = this.ys[right] - this.ys[left];
            } else if (right - left === 1) {
                this.len[node] = 0;
            } else {
                this.len[node] = this.len[node << 1] + this.len[(node << 1) | 1];
            }
        }
        query(): number {
            return this.len[1];
        }
    }

    const seg = new SegmentTree(ys);
    let prevX = events[0].x;
    let area = 0n;

    for (const e of events) {
        const curX = e.x;
        const dx = curX - prevX;
        if (dx !== 0) {
            const coveredY = seg.query(); // total y length currently covered
            area += BigInt(coveredY) * BigInt(dx);
            area %= MOD;
        }
        seg.update(e.y1, e.y2, e.type);
        prevX = curX;
    }

    return Number(area % MOD);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function rectangleArea($rectangles) {
        $MOD = 1000000007;
        $xs = [];
        $events = []; // each event: [y, type(+1/-1), x1, x2]

        foreach ($rectangles as $rec) {
            [$x1, $y1, $x2, $y2] = $rec;
            $xs[] = $x1;
            $xs[] = $x2;
            $events[] = [$y1, 1, $x1, $x2];   // add
            $events[] = [$y2, -1, $x1, $x2];  // remove
        }

        sort($xs);
        $xs = array_values(array_unique($xs));
        $m = count($xs);

        // map x coordinate to index
        $xIndex = [];
        foreach ($xs as $i => $val) {
            $xIndex[$val] = $i;
        }

        usort($events, function($a, $b) {
            if ($a[0] == $b[0]) return 0;
            return ($a[0] < $b[0]) ? -1 : 1;
        });

        // segment tree arrays
        $size = $m * 4;
        $cnt = array_fill(0, $size, 0);
        $len = array_fill(0, $size, 0);

        // recursive update function using closure
        $update = function($node, $l, $r, $ul, $ur, $val) use (&$update, &$cnt, &$len, $xs) {
            if ($ul >= $r || $ur <= $l) {
                return;
            }
            if ($ul <= $l && $r <= $ur) {
                $cnt[$node] += $val;
            } else {
                $mid = intdiv($l + $r, 2);
                $update($node * 2, $l, $mid, $ul, $ur, $val);
                $update($node * 2 + 1, $mid, $r, $ul, $ur, $val);
            }

            if ($cnt[$node] > 0) {
                $len[$node] = $xs[$r] - $xs[$l];
            } else {
                if ($r - $l == 1) {
                    $len[$node] = 0;
                } else {
                    $len[$node] = $len[$node * 2] + $len[$node * 2 + 1];
                }
            }
        };

        $prevY = $events[0][0];
        $curLen = 0;
        $area = 0;

        foreach ($events as $e) {
            [$y, $type, $x1, $x2] = $e;
            $dy = $y - $prevY;
            if ($dy != 0) {
                $area = ($area + ($curLen * $dy) % $MOD) % $MOD;
            }

            $lIdx = $xIndex[$x1];
            $rIdx = $xIndex[$x2];
            $update(1, 0, $m - 1, $lIdx, $rIdx, $type);
            $curLen = $len[1];

            $prevY = $y;
        }

        return ($area + $MOD) % $MOD;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func rectangleArea(_ rectangles: [[Int]]) -> Int {
        var xs = [Int]()
        for rect in rectangles {
            xs.append(rect[0])
            xs.append(rect[2])
        }
        xs.sort()
        var uniqXs = [Int]()
        var last: Int? = nil
        for x in xs {
            if x != last {
                uniqXs.append(x)
                last = x
            }
        }
        let xIndex: [Int:Int] = {
            var dict = [Int:Int]()
            for (i, v) in uniqXs.enumerated() {
                dict[v] = i
            }
            return dict
        }()

        struct Event {
            let y: Int
            let type: Int   // +1 add, -1 remove
            let l: Int      // index in compressed x
            let r: Int
        }

        var events = [Event]()
        for rect in rectangles {
            let x1 = rect[0], y1 = rect[1], x2 = rect[2], y2 = rect[3]
            let l = xIndex[x1]!
            let r = xIndex[x2]!
            events.append(Event(y: y1, type: 1, l: l, r: r))
            events.append(Event(y: y2, type: -1, l: l, r: r))
        }
        events.sort { $0.y < $1.y }

        let segTree = SegmentTree(xs: uniqXs)

        var prevY = events.first!.y
        var area: Int64 = 0

        for e in events {
            let curY = e.y
            let dy = curY - prevY
            if dy != 0 {
                let covered = segTree.total()
                area = (area + Int64(dy) * covered) % Int64(MOD)
            }
            segTree.update(e.l, e.r, e.type)
            prevY = curY
        }

        return Int(area)
    }
}

private class SegmentTree {
    private let xs: [Int]
    private var cnt: [Int]
    private var len: [Int64]
    private let n: Int

    init(xs: [Int]) {
        self.xs = xs
        self.n = xs.count - 1          // number of elementary intervals
        let size = max(4 * n, 4)
        self.cnt = Array(repeating: 0, count: size)
        self.len = Array(repeating: 0, count: size)
    }

    func update(_ l: Int, _ r: Int, _ val: Int) {
        // update range [l, r)
        update(1, 0, n, l, r, val)
    }

    private func update(_ node: Int, _ left: Int, _ right: Int,
                        _ ql: Int, _ qr: Int, _ val: Int) {
        if ql >= right || qr <= left { return }
        if ql <= left && right <= qr {
            cnt[node] += val
        } else {
            let mid = (left + right) >> 1
            update(node << 1, left, mid, ql, qr, val)
            update((node << 1) | 1, mid, right, ql, qr, val)
        }

        if cnt[node] > 0 {
            len[node] = Int64(xs[right] - xs[left])
        } else {
            if left + 1 == right {
                len[node] = 0
            } else {
                len[node] = len[node << 1] + len[(node << 1) | 1]
            }
        }
    }

    func total() -> Int64 {
        return len[1]
    }
}
```

## Kotlin

```kotlin
import java.util.*
 
class Solution {
    fun rectangleArea(rectangles: Array<IntArray>): Int {
        val MOD = 1_000_000_007L
        // collect all x coordinates
        val xsList = mutableListOf<Int>()
        for (rec in rectangles) {
            xsList.add(rec[0])
            xsList.add(rec[2])
        }
        val xsSorted = xsList.distinct().sorted()
        val n = xsSorted.size
        val xs = IntArray(n)
        for (i in 0 until n) xs[i] = xsSorted[i]
        // map x coordinate to index
        val xIndex = HashMap<Int, Int>()
        for (i in xs.indices) {
            xIndex[xs[i]] = i
        }
        // create events
        data class Event(val y: Int, val type: Int, val x1: Int, val x2: Int)
        val events = mutableListOf<Event>()
        for (rec in rectangles) {
            val x1 = rec[0]
            val y1 = rec[1]
            val x2 = rec[2]
            val y2 = rec[3]
            events.add(Event(y1, 1, x1, x2))
            events.add(Event(y2, -1, x1, x2))
        }
        events.sortBy { it.y }
 
        // segment tree arrays
        val cnt = IntArray(4 * n)
        val segLen = LongArray(4 * n)
 
        fun update(node: Int, l: Int, r: Int, ql: Int, qr: Int, delta: Int) {
            if (qr <= l || r <= ql) return
            if (ql <= l && r <= qr) {
                cnt[node] += delta
            } else {
                val mid = (l + r) / 2
                update(node * 2, l, mid, ql, qr, delta)
                update(node * 2 + 1, mid, r, ql, qr, delta)
            }
            if (cnt[node] > 0) {
                segLen[node] = xs[r].toLong() - xs[l].toLong()
            } else {
                if (r - l == 1) {
                    segLen[node] = 0L
                } else {
                    segLen[node] = segLen[node * 2] + segLen[node * 2 + 1]
                }
            }
        }
 
        var area = 0L
        var prevY = events[0].y
        for (e in events) {
            val curY = e.y
            val covered = segLen[1]
            val dy = (curY - prevY).toLong()
            area = (area + covered % MOD * (dy % MOD)) % MOD
            val lIdx = xIndex[e.x1]!!
            val rIdx = xIndex[e.x2]!!
            update(1, 0, n - 1, lIdx, rIdx, e.type)
            prevY = curY
        }
        return (area % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int rectangleArea(List<List<int>> rectangles) {
    // Collect all unique x coordinates.
    final Set<int> xSet = {};
    for (var rec in rectangles) {
      xSet.add(rec[0]);
      xSet.add(rec[2]);
    }
    final List<int> xs = xSet.toList()..sort();
    final Map<int, int> xIndex = {for (int i = 0; i < xs.length; i++) xs[i]: i};

    // Build events: [y, type(+1 add / -1 remove), x1, x2]
    final List<List<int>> events = [];
    for (var rec in rectangles) {
      int x1 = rec[0], y1 = rec[1], x2 = rec[2], y2 = rec[3];
      events.add([y1, 1, x1, x2]);
      events.add([y2, -1, x1, x2]);
    }
    events.sort((a, b) => a[0].compareTo(b[0]));

    // Segment tree over the intervals between xs.
    final _SegTree seg = _SegTree(xs);

    int i = 0;
    int area = 0;
    while (i < events.length) {
      int curY = events[i][0];
      // Process all events at curY
      while (i < events.length && events[i][0] == curY) {
        int type = events[i][1];
        int x1 = events[i][2];
        int x2 = events[i][3];
        int l = xIndex[x1]!;
        int r = xIndex[x2]! - 1;
        if (l <= r) {
          seg.update(1, 0, xs.length - 2, l, r, type);
        }
        i++;
      }
      if (i == events.length) break;
      int nextY = events[i][0];
      int coveredLen = seg.totalLength();
      int deltaY = nextY - curY;
      area = (area + ((coveredLen % _MOD) * (deltaY % _MOD)) % _MOD) % _MOD;
    }
    return area;
  }
}

class _SegTree {
  final List<int> xs;
  late final List<int> cnt;
  late final List<int> len;

  _SegTree(this.xs) {
    int n = xs.length;
    // tree size enough for intervals [0, n-2]
    cnt = List.filled(4 * n, 0);
    len = List.filled(4 * n, 0);
  }

  void update(int node, int l, int r, int ql, int qr, int val) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) {
      cnt[node] += val;
    } else {
      int mid = (l + r) >> 1;
      update(node << 1, l, mid, ql, qr, val);
      update((node << 1) | 1, mid + 1, r, ql, qr, val);
    }
    if (cnt[node] > 0) {
      len[node] = xs[r + 1] - xs[l];
    } else {
      if (l == r) {
        len[node] = 0;
      } else {
        len[node] = len[node << 1] + len[(node << 1) | 1];
      }
    }
  }

  int totalLength() => len[1];
}
```

## Golang

```go
func rectangleArea(rectangles [][]int) int {
	const MOD int64 = 1000000007

	type Event struct {
		y   int
		typ int // +1 add, -1 remove
		x1  int
		x2  int
	}

	var xs []int
	events := make([]Event, 0, len(rectangles)*2)
	for _, rec := range rectangles {
		x1, y1, x2, y2 := rec[0], rec[1], rec[2], rec[3]
		xs = append(xs, x1, x2)
		events = append(events, Event{y: y1, typ: 1, x1: x1, x2: x2})
		events = append(events, Event{y: y2, typ: -1, x1: x1, x2: x2})
	}
	sort.Ints(xs)
	// unique xs
	uniq := xs[:0]
	for _, v := range xs {
		if len(uniq) == 0 || v != uniq[len(uniq)-1] {
			uniq = append(uniq, v)
		}
	}
	xs = uniq

	sort.Slice(events, func(i, j int) bool { return events[i].y < events[j].y })

	m := len(xs)
	cnt := make([]int, 4*m)
	segLen := make([]int64, 4*m)

	var update func(node, l, r, ql, qr, val int)
	update = func(node, l, r, ql, qr, val int) {
		if ql >= r || qr <= l {
			return
		}
		if ql <= l && r <= qr {
			cnt[node] += val
		} else {
			mid := (l + r) / 2
			update(node*2, l, mid, ql, qr, val)
			update(node*2+1, mid, r, ql, qr, val)
		}
		if cnt[node] > 0 {
			segLen[node] = int64(xs[r] - xs[l])
		} else {
			if l+1 >= r { // leaf
				segLen[node] = 0
			} else {
				segLen[node] = segLen[node*2] + segLen[node*2+1]
			}
		}
	}

	var area int64
	prevY := events[0].y
	for _, e := range events {
		curY := e.y
		if curY != prevY {
			deltaY := curY - prevY
			coveredX := segLen[1] % MOD
			area = (area + coveredX*int64(deltaY)%MOD) % MOD
			prevY = curY
		}
		lIdx := sort.SearchInts(xs, e.x1)
		rIdx := sort.SearchInts(xs, e.x2)
		update(1, 0, m-1, lIdx, rIdx, e.typ)
	}

	return int(area % MOD)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def compute_union(intervals)
  sorted = intervals.sort_by { |a| a[0] }
  total = 0
  cur_start, cur_end = sorted[0]
  sorted[1..-1].each do |x1, x2|
    if x1 > cur_end
      total += cur_end - cur_start
      cur_start, cur_end = x1, x2
    else
      cur_end = [cur_end, x2].max
    end
  end
  total + (cur_end - cur_start)
end

def rectangle_area(rectangles)
  events = []
  rectangles.each do |x1, y1, x2, y2|
    events << [y1, 1, x1, x2]
    events << [y2, -1, x1, x2]
  end
  events.sort_by! { |e| e[0] }

  active = []
  prev_y = events[0][0]
  area = 0
  i = 0
  while i < events.length
    y = events[i][0]
    delta_y = y - prev_y
    unless active.empty?
      union_len = compute_union(active)
      area = (area + union_len * delta_y) % MOD
    end

    while i < events.length && events[i][0] == y
      _, typ, x1, x2 = events[i]
      if typ == 1
        active << [x1, x2]
      else
        idx = active.find_index { |a| a[0] == x1 && a[1] == x2 }
        active.delete_at(idx) if idx
      end
      i += 1
    end
    prev_y = y
  end

  area % MOD
end
```

## Scala

```scala
object Solution {
  def rectangleArea(rectangles: Array[Array[Int]]): Int = {
    val MOD = 1000000007L
    import scala.collection.mutable.ArrayBuffer

    val xsBuf = ArrayBuffer[Int]()
    val rawEvents = ArrayBuffer[(Int, Int, Int, Int)]() // (y, typ, x1, x2)

    for (rect <- rectangles) {
      val x1 = rect(0)
      val y1 = rect(1)
      val x2 = rect(2)
      val y2 = rect(3)
      xsBuf += x1
      xsBuf += x2
      rawEvents.append((y1, 1, x1, x2))
      rawEvents.append((y2, -1, x1, x2))
    }

    val xs = xsBuf.distinct.sorted
    val m = xs.length

    def idx(v: Int): Int = java.util.Arrays.binarySearch(xs, v)

    case class Event(y: Int, typ: Int, l: Int, r: Int)

    val events = rawEvents.map { case (y, t, x1, x2) =>
      Event(y, t, idx(x1), idx(x2))
    }.sortBy(_.y)

    if (events.isEmpty) return 0

    val cnt = new Array[Int](4 * m)
    val cover = new Array[Long](4 * m)

    def update(node: Int, l: Int, r: Int, ql: Int, qr: Int, delta: Int): Unit = {
      if (ql >= r || qr <= l) return
      if (ql <= l && r <= qr) {
        cnt(node) += delta
      } else {
        val mid = (l + r) / 2
        update(node * 2, l, mid, ql, qr, delta)
        update(node * 2 + 1, mid, r, ql, qr, delta)
      }
      if (cnt(node) > 0) {
        cover(node) = xs(r).toLong - xs(l).toLong
      } else {
        if (l + 1 >= r) {
          cover(node) = 0L
        } else {
          cover(node) = cover(node * 2) + cover(node * 2 + 1)
        }
      }
    }

    var prevY = events.head.y
    var area = 0L

    for (e <- events) {
      val curY = e.y
      val dy = curY - prevY
      if (dy != 0) {
        area = (area + cover(1) * dy) % MOD
      }
      update(1, 0, m - 1, e.l, e.r, e.typ)
      prevY = curY
    }

    ((area % MOD).toInt)
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

const MOD: i64 = 1_000_000_007;

#[derive(Clone)]
struct Event {
    y: i64,
    typ: i32, // +1 add, -1 remove
    x1: i64,
    x2: i64,
}

struct SegTree {
    cnt: Vec<i32>,
    len: Vec<i64>,
    xs: Vec<i64>,
}

impl SegTree {
    fn new(xs: Vec<i64>) -> Self {
        let m = xs.len() - 1; // number of intervals
        SegTree {
            cnt: vec![0; m * 4 + 5],
            len: vec![0; m * 4 + 5],
            xs,
        }
    }

    fn pull(&mut self, node: usize, l: usize, r: usize) {
        if self.cnt[node] > 0 {
            self.len[node] = self.xs[r] - self.xs[l];
        } else if l + 1 == r {
            self.len[node] = 0;
        } else {
            let left = node * 2;
            let right = left + 1;
            self.len[node] = self.len[left] + self.len[right];
        }
    }

    fn update(&mut self, node: usize, l: usize, r: usize, ql: usize, qr: usize, val: i32) {
        if ql >= r || qr <= l {
            return;
        }
        if ql <= l && r <= qr {
            self.cnt[node] += val;
            self.pull(node, l, r);
            return;
        }
        let mid = (l + r) / 2;
        self.update(node * 2, l, mid, ql, qr, val);
        self.update(node * 2 + 1, mid, r, ql, qr, val);
        self.pull(node, l, r);
    }

    fn total_covered(&self) -> i64 {
        self.len[1]
    }
}

impl Solution {
    pub fn rectangle_area(rectangles: Vec<Vec<i32>>) -> i32 {
        let mut xs: Vec<i64> = Vec::new();
        let mut events: Vec<Event> = Vec::new();

        for rec in rectangles.iter() {
            let x1 = rec[0] as i64;
            let y1 = rec[1] as i64;
            let x2 = rec[2] as i64;
            let y2 = rec[3] as i64;
            xs.push(x1);
            xs.push(x2);
            events.push(Event { y: y1, typ: 1, x1, x2 });
            events.push(Event { y: y2, typ: -1, x1, x2 });
        }

        xs.sort_unstable();
        xs.dedup();

        events.sort_by(|a, b| a.y.cmp(&b.y));

        let mut seg = SegTree::new(xs.clone());

        let mut prev_y = events[0].y;
        let mut area: i64 = 0;

        for e in events.iter() {
            let cur_y = e.y;
            let covered_len = seg.total_covered();
            let dy = (cur_y - prev_y) % MOD;
            area = (area + covered_len % MOD * dy) % MOD;

            // find indices
            let l = xs.binary_search(&e.x1).unwrap();
            let r = xs.binary_search(&e.x2).unwrap();
            seg.update(1, 0, xs.len() - 1, l, r, e.typ);

            prev_y = cur_y;
        }

        ((area % MOD + MOD) % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; return index of val in vector vec (val is guaranteed to exist)
(define (index-of vec val)
  (let ((len (vector-length vec)))
    (let loop ((i 0))
      (if (= i len)
          -1
          (if (= (vector-ref vec i) val)
              i
              (loop (add1 i)))))))

(define (rectangle-area rectangles)
  (let* ((xs (remove-duplicates
               (sort
                (apply append
                       (map (lambda (r) (list (list-ref r 0) (list-ref r 2))) rectangles))
                <)))
         (xvec (list->vector xs))
         (events
          (sort
           (apply append
                  (map (lambda (r)
                         (let ((x1 (list-ref r 0)) (y1 (list-ref r 1))
                               (x2 (list-ref r 2)) (y2 (list-ref r 3)))
                           (list (list y1 1 x1 x2)   ; add interval at y1
                                 (list y2 -1 x1 x2)))) ; remove interval at y2
                       rectangles))
           (lambda (a b) (< (first a) (first b)))))
         (cnt (make-vector (- (vector-length xvec) 1) 0)))
    (if (null? events)
        0
        (let loop ((i 0)
                   (prev-y (first (first events))) ; y of first event
                   (covered 0)
                   (area 0))
          (if (>= i (length events))
              area
              (let* ((cur-y (first (list-ref events i)))
                     (dy (- cur-y prev-y))
                     (area (+ area (modulo (* covered dy) MOD))))
                ;; process all events that have y == cur-y
                (let process ((j i))
                  (if (or (>= j (length events))
                          (not (= (first (list-ref events j)) cur-y)))
                      (begin
                        ;; recompute total covered length after updates
                        (let ((new-covered 0))
                          (for ([idx (in-range (- (vector-length xvec) 1))])
                            (when (> (vector-ref cnt idx) 0)
                              (set! new-covered (+ new-covered
                                                   (- (vector-ref xvec (add1 idx))
                                                      (vector-ref xvec idx))))))
                          (loop j cur-y new-covered (modulo area MOD))))
                      (let* ((ev (list-ref events j))
                             (typ (second ev))
                             (x1 (third ev))
                             (x2 (list-ref ev 3))
                             (l (index-of xvec x1))
                             (r (index-of xvec x2)))
                        (for ([idx (in-range l r)])
                          (vector-set! cnt idx (+ (vector-ref cnt idx) typ)))
                        (process (add1 j)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([rectangle_area/1]).

-define(MOD, 1000000007).

-spec rectangle_area(Rectangles :: [[integer()]]) -> integer().
rectangle_area(Rectangles) ->
    Events = build_events(Rectangles),
    SortedEvents = lists:sort(fun(E1, E2) -> element(1, E1) < element(1, E2) end, Events),
    process_events(SortedEvents, 0, 0, []).

build_events([]) -> [];
build_events([[X1, Y1, X2, Y2] | Rest]) ->
    [{Y1, 1, X1, X2}, {Y2, -1, X1, X2}] ++ build_events(Rest).

process_events([], _PrevY, Area, _Active) ->
    Area rem ?MOD;
process_events([Event | Rest], PrevY, Area, Active) ->
    {Y, Type, X1, X2} = Event,
    DeltaY = Y - PrevY,
    CoveredX = case DeltaY > 0 of
        true -> covered_length(Active);
        false -> 0
    end,
    NewArea = (Area + (CoveredX * DeltaY) rem ?MOD) rem ?MOD,
    NewActive = case Type of
        1 -> [{X1, X2} | Active];
        -1 -> lists:delete({X1, X2}, Active)
    end,
    process_events(Rest, Y, NewArea, NewActive).

covered_length([]) -> 0;
covered_length(Intervals) ->
    Sorted = lists:keysort(1, Intervals),
    merge_intervals(Sorted, 0, undefined, undefined).

merge_intervals([], Sum, undefined, _) -> Sum;
merge_intervals([], Sum, CurStart, CurEnd) ->
    Sum + (CurEnd - CurStart);
merge_intervals([{L, R} | Rest], Sum, undefined, _) ->
    merge_intervals(Rest, Sum, L, R);
merge_intervals([{L, R} | Rest], Sum, CurStart, CurEnd) when L > CurEnd ->
    NewSum = Sum + (CurEnd - CurStart),
    merge_intervals(Rest, NewSum, L, R);
merge_intervals([{L, R} | Rest], Sum, CurStart, CurEnd) ->
    NewEnd = erlang:max(CurEnd, R),
    merge_intervals(Rest, Sum, CurStart, NewEnd).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec rectangle_area(rectangles :: [[integer]]) :: integer
  def rectangle_area(rectangles) do
    mod = 1_000_000_007

    events =
      rectangles
      |> Enum.flat_map(fn [x1, y1, x2, y2] ->
        [{y1, 1, x1, x2}, {y2, -1, x1, x2}]
      end)
      |> Enum.sort_by(fn {y, _, _, _} -> y end)

    process_events(events, mod)
  end

  defp process_events(events, mod) do
    do_process(events, [], nil, 0, mod)
  end

  defp do_process([], _active, _prev_y, area, _mod), do: rem(area, _mod)

  defp do_process([{y, _, _, _} = first | rest], active, prev_y, area, mod) do
    # add contribution from previous y to current y
    area =
      if prev_y != nil do
        dy = y - prev_y

        if dy > 0 and length(active) > 0 do
          width = union_length(active)
          rem(area + rem(width * dy, mod), mod)
        else
          area
        end
      else
        area
      end

    # gather all events with the same y coordinate
    {same_y_events, remaining} =
      Enum.split_while([first | rest], fn {yy, _, _, _} -> yy == y end)

    # update active intervals according to these events
    new_active =
      Enum.reduce(same_y_events, active, fn {_y, type, x1, x2}, acc ->
        if type == 1 do
          [{x1, x2} | acc]
        else
          remove_one(acc, {x1, x2})
        end
      end)

    do_process(remaining, new_active, y, area, mod)
  end

  defp remove_one([], _target), do: []

  defp remove_one([h | t], target) do
    if h == target do
      t
    else
      [h | remove_one(t, target)]
    end
  end

  defp union_length(intervals) do
    intervals
    |> Enum.sort_by(fn {x1, _} -> x1 end)
    |> Enum.reduce({0, nil}, fn {l, r}, {total, cur} ->
      case cur do
        nil ->
          {total, {l, r}}

        {cl, cr} ->
          if l > cr do
            {total + (cr - cl), {l, r}}
          else
            {total, {cl, max(cr, r)}}
          end
      end
    end)
    |> then(fn {total, cur} ->
      case cur do
        nil -> total
        {cl, cr} -> total + (cr - cl)
      end
    end)
  end
end
```

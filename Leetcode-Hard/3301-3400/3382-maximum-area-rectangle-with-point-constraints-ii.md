# 3382. Maximum Area Rectangle With Point Constraints II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class SegTree {
    int n;
    vector<long long> seg;
public:
    SegTree(int sz) {
        n = 1;
        while (n < sz) n <<= 1;
        seg.assign(2 * n, LLONG_MIN);
    }
    void update(int pos, long long val) {
        pos += n;
        seg[pos] = val;
        for (pos >>= 1; pos; pos >>= 1)
            seg[pos] = max(seg[pos << 1], seg[(pos << 1) | 1]);
    }
    long long query(int l, int r) { // inclusive
        if (l > r) return LLONG_MIN;
        l += n; r += n;
        long long res = LLONG_MIN;
        while (l <= r) {
            if (l & 1) res = max(res, seg[l++]);
            if (!(r & 1)) res = max(res, seg[r--]);
            l >>= 1; r >>= 1;
        }
        return res;
    }
};

class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        vector<long long> allY(yCoord.begin(), yCoord.end());
        sort(allY.begin(), allY.end());
        allY.erase(unique(allY.begin(), allY.end()), allY.end());
        int m = allY.size();
        unordered_map<long long,int> yToIdx;
        yToIdx.reserve(m*2);
        for (int i=0;i<m;++i) yToIdx[allY[i]] = i;

        vector<pair<int,int>> pts(n);
        for (int i=0;i<n;++i){
            pts[i] = {xCoord[i], yToIdx[yCoord[i]]};
        }
        sort(pts.begin(), pts.end(), [](const auto& a, const auto& b){
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        });

        SegTree seg(m);
        unordered_map<unsigned long long,long long> intervalMap;
        intervalMap.reserve(n*2);

        long long best = -1;
        int i=0;
        while (i<n){
            int curX = pts[i].first;
            vector<pair<long long,int>> col; // (origY, idx)
            while (i<n && pts[i].first==curX){
                long long origY = allY[pts[i].second];
                col.emplace_back(origY, pts[i].second);
                ++i;
            }
            sort(col.begin(), col.end()); // by original y

            int sz = col.size();
            // first pass: evaluate possible rectangles
            for (int j=0;j+1<sz;++j){
                long long y1 = col[j].first, y2 = col[j+1].first;
                int idx1 = col[j].second, idx2 = col[j+1].second;
                if (idx1 > idx2) swap(idx1, idx2);
                long long maxLast = seg.query(idx1, idx2);
                if (maxLast==LLONG_MIN) continue;
                unsigned long long key = ((unsigned long long)idx1<<32) | (unsigned long long)idx2;
                auto it = intervalMap.find(key);
                if (it != intervalMap.end() && it->second == maxLast){
                    long long area = (long long)(curX - maxLast) * (y2 - y1);
                    if (area > best) best = area;
                }
            }
            // second pass: record intervals as consecutive at this column
            for (int j=0;j+1<sz;++j){
                int idx1 = col[j].second, idx2 = col[j+1].second;
                if (idx1 > idx2) swap(idx1, idx2);
                unsigned long long key = ((unsigned long long)idx1<<32) | (unsigned long long)idx2;
                intervalMap[key] = curX;
            }
            // update last occurrence for each y in this column
            for (auto &p: col){
                seg.update(p.second, curX);
            }
        }
        return best;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long maxRectangleArea(int[] xCoord, int[] yCoord) {
        int n = xCoord.length;
        // compress y coordinates
        int[] ys = Arrays.copyOf(yCoord, n);
        Arrays.sort(ys);
        int m = 0;
        for (int i = 0; i < n; ++i) {
            if (i == 0 || ys[i] != ys[i - 1]) {
                ys[m++] = ys[i];
            }
        }
        int[] yComp = new int[n];
        Map<Integer, Integer> yToIdx = new HashMap<>(m * 2);
        for (int i = 0; i < m; ++i) {
            yToIdx.put(ys[i], i);
        }
        for (int i = 0; i < n; ++i) {
            yComp[i] = yToIdx.get(yCoord[i]);
        }

        // group points by x
        int[] order = new int[n];
        for (int i = 0; i < n; ++i) order[i] = i;
        Arrays.sort(order, Comparator.comparingInt(i -> xCoord[i]));

        // segment tree for range max of lastX per y index
        SegTree seg = new SegTree(m);
        int[] lastX = new int[m];
        Arrays.fill(lastX, Integer.MIN_VALUE);

        // map from pair (y1Idx,y2Idx) to previous x where they were consecutive
        HashMap<Long, Integer> pairPrev = new HashMap<>(n * 2);

        long best = -1;
        int idx = 0;
        while (idx < n) {
            int curX = xCoord[order[idx]];
            // collect all y indices for this x
            List<Integer> colYs = new ArrayList<>();
            while (idx < n && xCoord[order[idx]] == curX) {
                colYs.add(yComp[order[idx]]);
                idx++;
            }
            Collections.sort(colYs);
            // process consecutive pairs
            for (int i = 0; i + 1 < colYs.size(); ++i) {
                int y1 = colYs.get(i);
                int y2 = colYs.get(i + 1);
                long key = ((long) y1 << 32) | (y2 & 0xffffffffL);
                Integer prevXObj = pairPrev.get(key);
                if (prevXObj != null) {
                    int prevX = prevXObj;
                    int maxInRange = seg.query(y1, y2);
                    if (maxInRange <= prevX) {
                        long area = (long) (curX - prevX) * (long) (ys[y2] - ys[y1]);
                        if (area > best) best = area;
                    }
                }
            }
            // after checking, update map and segment tree
            for (int i = 0; i + 1 < colYs.size(); ++i) {
                int y1 = colYs.get(i);
                int y2 = colYs.get(i + 1);
                long key = ((long) y1 << 32) | (y2 & 0xffffffffL);
                pairPrev.put(key, curX);
            }
            for (int yIdx : colYs) {
                lastX[yIdx] = curX;
                seg.update(yIdx, curX);
            }
        }
        return best;
    }

    // segment tree for range maximum query
    static class SegTree {
        int n;
        int[] tree;
        SegTree(int size) {
            n = 1;
            while (n < size) n <<= 1;
            tree = new int[2 * n];
            Arrays.fill(tree, Integer.MIN_VALUE);
        }
        void update(int pos, int val) {
            int i = pos + n;
            tree[i] = val;
            for (i >>= 1; i > 0; i >>= 1) {
                tree[i] = Math.max(tree[i << 1], tree[(i << 1) | 1]);
            }
        }
        // query inclusive [l, r]
        int query(int l, int r) {
            int res = Integer.MIN_VALUE;
            int left = l + n, right = r + n;
            while (left <= right) {
                if ((left & 1) == 1) res = Math.max(res, tree[left++]);
                if ((right & 1) == 0) res = Math.max(res, tree[right--]);
                left >>= 1;
                right >>= 1;
            }
            return res;
        }
    }
}
```

## Python

```python
class Solution(object):
    def maxRectangleArea(self, xCoord, yCoord):
        """
        :type xCoord: List[int]
        :type yCoord: List[int]
        :rtype: int
        """
        from collections import defaultdict

        n = len(xCoord)
        # group points by x
        xs = defaultdict(list)
        ys_set = set()
        for x, y in zip(xCoord, yCoord):
            xs[x].append(y)
            ys_set.add(y)

        # compress y coordinates
        sorted_ys = sorted(ys_set)
        y_to_idx = {y: i for i, y in enumerate(sorted_ys)}
        m = len(sorted_ys)

        # segment tree for range maximum of last x where a point with given y appeared
        size = 1
        while size < m:
            size <<= 1
        seg = [-1] * (2 * size)

        def point_update(pos, val):
            i = pos + size
            if seg[i] >= val:
                return
            seg[i] = val
            i >>= 1
            while i:
                new_val = seg[2 * i] if seg[2 * i] > seg[2 * i + 1] else seg[2 * i + 1]
                if seg[i] == new_val:
                    break
                seg[i] = new_val
                i >>= 1

        def range_query(l, r):
            l += size
            r += size
            res = -1
            while l <= r:
                if (l & 1):
                    if seg[l] > res:
                        res = seg[l]
                    l += 1
                if not (r & 1):
                    if seg[r] > res:
                        res = seg[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        # map segment (y_low_idx, y_high_idx) -> last x where this consecutive pair existed
        last_seg_x = {}

        ans = -1
        for x in sorted(xs.keys()):
            ys = xs[x]
            ys.sort()
            segs = []
            # generate consecutive y pairs as potential vertical edges
            for i in range(len(ys) - 1):
                y_low = ys[i]
                y_high = ys[i + 1]
                low_idx = y_to_idx[y_low]
                high_idx = y_to_idx[y_high]
                height = y_high - y_low
                segs.append(((low_idx, high_idx), height))

            # evaluate rectangles using current x as right side
            for (key, height) in segs:
                low_idx, high_idx = key
                max_last = range_query(low_idx, high_idx)
                if key in last_seg_x:
                    prev_x = last_seg_x[key]
                    if max_last <= prev_x:
                        area = (x - prev_x) * height
                        if area > ans:
                            ans = area

            # update point positions for this column
            for y in ys:
                point_update(y_to_idx[y], x)

            # store current x as last occurrence of each segment
            for (key, _) in segs:
                last_seg_x[key] = x

        return ans if ans != -1 else -1
```

## Python3

```python
import sys
from collections import defaultdict
from typing import List

class SegTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N <<= 1
        self.data = [-1] * (2 * self.N)

    def update(self, idx, val):
        i = idx + self.N
        self.data[i] = val
        i >>= 1
        while i:
            self.data[i] = self.data[i << 1]
            if self.data[(i << 1) | 1] > self.data[i]:
                self.data[i] = self.data[(i << 1) | 1]
            i >>= 1

    def query(self, l, r):
        res = -1
        l += self.N
        r += self.N
        while l <= r:
            if l & 1:
                if self.data[l] > res:
                    res = self.data[l]
                l += 1
            if not (r & 1):
                if self.data[r] > res:
                    res = self.data[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points_by_x = defaultdict(list)
        all_y = set()
        for x, y in zip(xCoord, yCoord):
            points_by_x[x].append(y)
            all_y.add(y)

        sorted_ys = sorted(all_y)
        y2idx = {y: i for i, y in enumerate(sorted_ys)}
        seg = SegTree(len(sorted_ys))

        pair_last = {}
        ans = -1

        for x in sorted(points_by_x.keys()):
            ys = points_by_x[x]
            ys.sort()
            k = len(ys)

            # evaluate possible rectangles using previous occurrence of each adjacent pair
            for i in range(k - 1):
                y1, y2 = ys[i], ys[i + 1]
                idx1, idx2 = y2idx[y1], y2idx[y2]
                max_last = seg.query(idx1, idx2)
                key = (idx1, idx2)
                if key in pair_last:
                    prev_x = pair_last[key]
                    if max_last == prev_x:
                        area = (x - prev_x) * (y2 - y1)
                        if area > ans:
                            ans = area

            # record current column as the latest occurrence for each adjacent pair
            for i in range(k - 1):
                key = (y2idx[ys[i]], y2idx[ys[i + 1]])
                pair_last[key] = x

            # update last seen x for all y's at this column
            for y in ys:
                seg.update(y2idx[y], x)

        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static inline long long pack(int x, int y) {
    return ( (long long)(unsigned int)x << 32 ) | (unsigned int)y;
}

long long maxRectangleArea(int* xCoord, int xCoordSize, int* yCoord, int yCoordSize) {
    int n = xCoordSize;
    unordered_map<int, vector<int>> rows; // y -> xs
    unordered_map<int, vector<int>> cols; // x -> ys
    rows.reserve(n * 2);
    cols.reserve(n * 2);
    unordered_set<long long> pointSet;
    pointSet.reserve(n * 2);

    for (int i = 0; i < n; ++i) {
        int x = xCoord[i];
        int y = yCoord[i];
        rows[y].push_back(x);
        cols[x].push_back(y);
        pointSet.insert(pack(x, y));
    }

    for (auto &kv : rows) {
        auto &vec = kv.second;
        sort(vec.begin(), vec.end());
    }
    for (auto &kv : cols) {
        auto &vec = kv.second;
        sort(vec.begin(), vec.end());
    }

    long long best = -1;

    for (int i = 0; i < n; ++i) {
        int x = xCoord[i];
        int y = yCoord[i];

        const vector<int> &rowVec = rows[y];
        auto itx = lower_bound(rowVec.begin(), rowVec.end(), x);
        if (itx == rowVec.end() || *itx != x) continue;
        size_t idxX = itx - rowVec.begin();
        if (idxX + 1 >= rowVec.size()) continue; // no right neighbor
        int xr = rowVec[idxX + 1];

        const vector<int> &colVec = cols[x];
        auto ity = lower_bound(colVec.begin(), colVec.end(), y);
        if (ity == colVec.end() || *ity != y) continue;
        size_t idxY = ity - colVec.begin();
        if (idxY + 1 >= colVec.size()) continue; // no top neighbor
        int yt = colVec[idxY + 1];

        // check opposite corner exists
        if (!pointSet.count(pack(xr, yt))) continue;

        // verify horizontal adjacency on top edge
        const vector<int> &topRow = rows[yt];
        auto itxrTop = lower_bound(topRow.begin(), topRow.end(), xr);
        if (itxrTop == topRow.end() || *itxrTop != xr) continue;
        size_t idxXRTop = itxrTop - topRow.begin();
        if (idxXRTop == 0) continue; // no left neighbor
        if (topRow[idxXRTop - 1] != x) continue; // not adjacent

        // verify vertical adjacency on right edge
        const vector<int> &rightCol = cols[xr];
        auto itytRight = lower_bound(rightCol.begin(), rightCol.end(), yt);
        if (itytRight == rightCol.end() || *itytRight != yt) continue;
        size_t idxYTRight = itytRight - rightCol.begin();
        if (idxYTRight == 0) continue; // no bottom neighbor
        if (rightCol[idxYTRight - 1] != y) continue; // not adjacent

        long long area = (long long)(xr - x) * (long long)(yt - y);
        if (area > best) best = area;
    }

    return best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaxRectangleArea(int[] xCoord, int[] yCoord) {
        int n = xCoord.Length;
        // Coordinate compression for y
        var ys = new int[n];
        Array.Copy(yCoord, ys, n);
        Array.Sort(ys);
        var uniqY = new List<int>();
        foreach (var v in ys) {
            if (uniqY.Count == 0 || uniqY[uniqY.Count - 1] != v) uniqY.Add(v);
        }
        int m = uniqY.Count;
        var yToIdx = new Dictionary<int, int>(m);
        for (int i = 0; i < m; i++) yToIdx[uniqY[i]] = i;

        // Group points by x
        var dictX = new SortedDictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            int x = xCoord[i];
            int yIdx = yToIdx[yCoord[i]];
            if (!dictX.TryGetValue(x, out var list)) {
                list = new List<int>();
                dictX[x] = list;
            }
            list.Add(yIdx);
        }

        // Segment tree for range max of last x where each y appeared
        int size = 1;
        while (size < m) size <<= 1;
        int[] seg = new int[2 * size];
        for (int i = 0; i < seg.Length; i++) seg[i] = -1;

        void SegUpdate(int pos, int val) {
            pos += size;
            seg[pos] = val;
            while (pos > 1) {
                pos >>= 1;
                seg[pos] = Math.Max(seg[pos << 1], seg[(pos << 1) | 1]);
            }
        }

        int SegQuery(int l, int r) { // inclusive
            l += size;
            r += size;
            int res = -1;
            while (l <= r) {
                if ((l & 1) == 1) res = Math.Max(res, seg[l++]);
                if ((r & 1) == 0) res = Math.Max(res, seg[r--]);
                l >>= 1;
                r >>= 1;
            }
            return res;
        }

        var gapLastX = new Dictionary<long, int>();
        long best = -1;

        foreach (var kv in dictX) {
            int curX = kv.Key;
            var yList = kv.Value;
            yList.Sort();

            // evaluate rectangles using existing gaps
            for (int i = 0; i + 1 < yList.Count; i++) {
                int low = yList[i];
                int high = yList[i + 1];
                long key = ((long)low << 32) | (uint)high;
                if (gapLastX.TryGetValue(key, out int leftX)) {
                    int maxLast = SegQuery(low, high);
                    if (maxLast == leftX) {
                        long area = (long)(curX - leftX) * (uniqY[high] - uniqY[low]);
                        if (area > best) best = area;
                    }
                }
            }

            // update last occurrence for each y in this column
            foreach (int yIdx in yList) {
                SegUpdate(yIdx, curX);
            }

            // store current gaps as potential left sides for future columns
            for (int i = 0; i + 1 < yList.Count; i++) {
                int low = yList[i];
                int high = yList[i + 1];
                long key = ((long)low << 32) | (uint)high;
                gapLastX[key] = curX;
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} xCoord
 * @param {number[]} yCoord
 * @return {number}
 */
var maxRectangleArea = function(xCoord, yCoord) {
    const n = xCoord.length;
    // collect unique xs and ys
    const xsSet = new Set();
    const ysSet = new Set();
    for (let i = 0; i < n; ++i) {
        xsSet.add(xCoord[i]);
        ysSet.add(yCoord[i]);
    }
    const xsList = Array.from(xsSet).sort((a, b) => a - b);
    const ysList = Array.from(ysSet).sort((a, b) => a - b);
    const mY = ysList.length;
    // maps
    const xToIdx = new Map();
    for (let i = 0; i < xsList.length; ++i) xToIdx.set(xsList[i], i);
    const yToIdx = new Map();
    for (let i = 0; i < ysList.length; ++i) yToIdx.set(ysList[i], i);
    // points per x (sorted y)
    const ptsByX = Array.from({length: xsList.length}, () => []);
    for (let i = 0; i < n; ++i) {
        const xi = xToIdx.get(xCoord[i]);
        ptsByX[xi].push(yCoord[i]);
    }
    for (let arr of ptsByX) arr.sort((a, b) => a - b);
    // xs per y (sorted)
    const xsByY = Array.from({length: mY}, () => []);
    for (let i = 0; i < n; ++i) {
        const yi = yToIdx.get(yCoord[i]);
        xsByY[yi].push(xCoord[i]);
    }
    for (let arr of xsByY) arr.sort((a, b) => a - b);
    // pointers per y
    const ptrs = new Int32Array(mY);
    // segment tree for next x per y
    const INF = Number.MAX_SAFE_INTEGER;
    let size = 1;
    while (size < mY) size <<= 1;
    const seg = new Float64Array(2 * size).fill(INF);
    for (let i = 0; i < mY; ++i) {
        const next = xsByY[i].length ? xsByY[i][0] : INF;
        seg[size + i] = next;
    }
    for (let i = size - 1; i >= 1; --i) seg[i] = Math.min(seg[2 * i], seg[2 * i + 1]);
    const update = (yIdx, val) => {
        let pos = size + yIdx;
        if (seg[pos] === val) return;
        seg[pos] = val;
        while (pos > 1) {
            pos >>= 1;
            const newVal = Math.min(seg[2 * pos], seg[2 * pos + 1]);
            if (seg[pos] === newVal) break;
            seg[pos] = newVal;
        }
    };
    const rangeMin = (lIdx, rIdx) => {
        let l = size + lIdx, r = size + rIdx;
        let res = INF;
        while (l <= r) {
            if ((l & 1) === 1) { if (seg[l] < res) res = seg[l]; l++; }
            if ((r & 1) === 0) { if (seg[r] < res) res = seg[r]; r--; }
            l >>= 1; r >>= 1;
        }
        return res;
    };
    const lowerBound = (arr, target) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < target) lo = mid + 1; else hi = mid;
        }
        return lo;
    };
    let best = -1;
    // sweep over xs
    for (let xi = 0; xi < xsList.length; ++xi) {
        const xVal = xsList[xi];
        const yArr = ptsByX[xi];
        // advance pointers for all ys at this x and update seg tree
        for (const y of yArr) {
            const yi = yToIdx.get(y);
            let p = ptrs[yi];
            while (p < xsByY[yi].length && xsByY[yi][p] <= xVal) ++p;
            ptrs[yi] = p;
            const nxt = (p < xsByY[yi].length) ? xsByY[yi][p] : INF;
            update(yi, nxt);
        }
        // evaluate consecutive y pairs at this column
        for (let i = 0; i + 1 < yArr.length; ++i) {
            const y1 = yArr[i];
            const y2 = yArr[i + 1];
            const idx1 = yToIdx.get(y1);
            const idx2 = yToIdx.get(y2);
            const minNextX = rangeMin(idx1, idx2);
            if (minNextX === INF) continue;
            const xr = minNextX;
            // verify right side has exactly these two ys consecutively
            const xrIdx = xToIdx.get(xr);
            if (xrIdx === undefined) continue;
            const yRightArr = ptsByX[xrIdx];
            const pos1 = lowerBound(yRightArr, y1);
            if (pos1 >= yRightArr.length || yRightArr[pos1] !== y1) continue;
            const pos2 = lowerBound(yRightArr, y2);
            if (pos2 >= yRightArr.length || yRightArr[pos2] !== y2) continue;
            if (pos2 - pos1 !== 1) continue; // not consecutive
            const area = (xr - xVal) * (y2 - y1);
            if (area > best) best = area;
        }
    }
    return best;
};
```

## Typescript

```typescript
function maxRectangleArea(xCoord: number[], yCoord: number[]): number {
    const n = xCoord.length;
    // compress y coordinates
    const uniqY = Array.from(new Set(yCoord)).sort((a, b) => a - b);
    const yToIdx = new Map<number, number>();
    for (let i = 0; i < uniqY.length; ++i) yToIdx.set(uniqY[i], i);
    const m = uniqY.length;

    // list of x's for each y index
    const yLists: number[][] = Array.from({ length: m }, () => []);
    // map from x to array of y indices present at that column
    const colMap = new Map<number, number[]>();

    for (let i = 0; i < n; ++i) {
        const x = xCoord[i];
        const yIdx = yToIdx.get(yCoord[i])!;
        yLists[yIdx].push(x);
        if (!colMap.has(x)) colMap.set(x, []);
        colMap.get(x)!.push(yIdx);
    }

    // sort per-y lists
    for (let i = 0; i < m; ++i) yLists[i].sort((a, b) => a - b);

    // sorted distinct x values
    const xsSorted = Array.from(colMap.keys()).sort((a, b) => a - b);
    // sort each column's y indices
    for (const x of xsSorted) {
        colMap.get(x)!.sort((a, b) => a - b);
    }

    const INF = Number.MAX_SAFE_INTEGER;

    // segment tree for range minimum of next x per y
    class SegTree {
        size: number;
        data: number[];
        INF: number;
        constructor(arr: number[]) {
            this.INF = INF;
            let n = arr.length;
            this.size = 1;
            while (this.size < n) this.size <<= 1;
            this.data = new Array(this.size * 2).fill(this.INF);
            for (let i = 0; i < n; ++i) this.data[this.size + i] = arr[i];
            for (let i = this.size - 1; i > 0; --i)
                this.data[i] = Math.min(this.data[i << 1], this.data[(i << 1) | 1]);
        }
        update(pos: number, val: number): void {
            let i = pos + this.size;
            this.data[i] = val;
            while (i > 1) {
                i >>= 1;
                this.data[i] = Math.min(this.data[i << 1], this.data[(i << 1) | 1]);
            }
        }
        query(l: number, r: number): number { // inclusive
            let res = this.INF;
            l += this.size;
            r += this.size;
            while (l <= r) {
                if ((l & 1) === 1) { res = Math.min(res, this.data[l]); ++l; }
                if ((r & 1) === 0) { res = Math.min(res, this.data[r]); --r; }
                l >>= 1;
                r >>= 1;
            }
            return res;
        }
    }

    // initial next-x for each y (first occurrence)
    const initArr: number[] = new Array(m);
    const ptr = new Uint32Array(m); // pointer to current position in yLists
    for (let i = 0; i < m; ++i) {
        initArr[i] = yLists[i].length ? yLists[i][0] : INF;
    }
    const seg = new SegTree(initArr);

    let best = -1;

    // helper binary search
    function lowerBound(arr: number[], target: number): number {
        let l = 0, r = arr.length;
        while (l < r) {
            const mid = (l + r) >> 1;
            if (arr[mid] < target) l = mid + 1; else r = mid;
        }
        return l;
    }

    // sweep columns as left side
    for (const x of xsSorted) {
        const yArr = colMap.get(x)!; // sorted list of y indices at this column

        // remove current column points from future consideration
        for (const yIdx of yArr) {
            ++ptr[yIdx];
            const nxt = ptr[yIdx] < yLists[yIdx].length ? yLists[yIdx][ptr[yIdx]] : INF;
            seg.update(yIdx, nxt);
        }

        // examine consecutive pairs in this column
        for (let i = 0; i + 1 < yArr.length; ++i) {
            const lowY = yArr[i];
            const highY = yArr[i + 1];
            const minX = seg.query(lowY, highY);
            if (minX === INF) continue;

            const rightCol = colMap.get(minX);
            if (!rightCol) continue;
            // verify both y's exist and are consecutive in the right column
            const posLow = lowerBound(rightCol, lowY);
            if (posLow >= rightCol.length || rightCol[posLow] !== lowY) continue;
            if (posLow + 1 >= rightCol.length || rightCol[posLow + 1] !== highY) continue;

            const area = (minX - x) * (uniqY[highY] - uniqY[lowY]);
            if (area > best) best = area;
        }
    }

    return best;
}
```

## Php

```php
class Solution {
    private array $tree = [];
    private int $size = 0;

    private function build(int $n): void {
        $this->size = 1;
        while ($this->size < $n) {
            $this->size <<= 1;
        }
        $this->tree = array_fill(0, $this->size * 2, -1);
    }

    private function updateSeg(int $pos, int $value): void {
        $i = $pos + $this->size;
        $this->tree[$i] = $value;
        $i >>= 1;
        while ($i > 0) {
            $left = $i << 1;
            $right = $left | 1;
            $this->tree[$i] = max($this->tree[$left], $this->tree[$right]);
            $i >>= 1;
        }
    }

    private function querySeg(int $l, int $r): int {
        $l += $this->size;
        $r += $this->size;
        $res = -1;
        while ($l <= $r) {
            if (($l & 1) == 1) {
                $res = max($res, $this->tree[$l]);
                $l++;
            }
            if (($r & 1) == 0) {
                $res = max($res, $this->tree[$r]);
                $r--;
            }
            $l >>= 1;
            $r >>= 1;
        }
        return $res;
    }

    /**
     * @param Integer[] $xCoord
     * @param Integer[] $yCoord
     * @return Integer
     */
    function maxRectangleArea($xCoord, $yCoord) {
        $n = count($xCoord);
        if ($n < 4) return -1;

        // compress y coordinates
        $ys = $yCoord;
        sort($ys);
        $uniqueYs = array_values(array_unique($ys));
        $m = count($uniqueYs);
        $yToIdx = [];
        foreach ($uniqueYs as $idx => $val) {
            $yToIdx[$val] = $idx;
        }

        // build points with compressed y
        $points = [];
        for ($i = 0; $i < $n; $i++) {
            $points[] = ['x' => $xCoord[$i], 'y' => $yToIdx[$yCoord[$i]]];
        }
        usort($points, function($a, $b) {
            if ($a['x'] == $b['x']) return 0;
            return ($a['x'] < $b['x']) ? -1 : 1;
        });

        // segment tree for last x of each y
        $this->build($m);
        $pairLastX = []; // key "y1#y2" => last common x
        $ans = -1;

        $i = 0;
        while ($i < $n) {
            $currX = $points[$i]['x'];
            $listY = [];
            while ($i < $n && $points[$i]['x'] == $currX) {
                $listY[] = $points[$i]['y'];
                $i++;
            }
            sort($listY);

            // update segment tree with current column points
            foreach ($listY as $yIdx) {
                $this->updateSeg($yIdx, $currX);
            }

            $cnt = count($listY);
            for ($j = 0; $j < $cnt - 1; $j++) {
                $a = $listY[$j];
                $b = $listY[$j + 1];
                $key = $a . '#' . $b;
                if (isset($pairLastX[$key])) {
                    $prevX = $pairLastX[$key];
                    if ($a + 1 <= $b - 1) {
                        $maxMid = $this->querySeg($a + 1, $b - 1);
                    } else {
                        $maxMid = -1;
                    }
                    if ($maxMid <= $prevX) {
                        $area = ($currX - $prevX) * ($uniqueYs[$b] - $uniqueYs[$a]);
                        if ($area > $ans) $ans = $area;
                    }
                }
            }

            // record this column as the latest common x for each consecutive pair
            for ($j = 0; $j < $cnt - 1; $j++) {
                $a = $listY[$j];
                $b = $listY[$j + 1];
                $pairLastX[$a . '#' . $b] = $currX;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxRectangleArea(_ xCoord: [Int], _ yCoord: [Int]) -> Int {
        let n = xCoord.count
        var columnMap = [Int: [Int]]()
        for i in 0..<n {
            columnMap[xCoord[i], default: []].append(yCoord[i])
        }
        // sort y lists for each column
        for (x, arr) in columnMap {
            columnMap[x] = arr.sorted()
        }
        // compress y coordinates
        var ySet = Set<Int>()
        for y in yCoord { ySet.insert(y) }
        let sortedY = Array(ySet).sorted()
        var yToIdx = [Int: Int]()
        for (i, y) in sortedY.enumerated() {
            yToIdx[y] = i
        }
        let m = sortedY.count
        // segment tree for range minimum x
        let INF = Int.max / 2
        var size = 1
        while size < m { size <<= 1 }
        var seg = Array(repeating: INF, count: 2 * size)
        func update(_ pos: Int, _ value: Int) {
            var i = pos + size
            seg[i] = value
            i >>= 1
            while i > 0 {
                seg[i] = min(seg[2 * i], seg[2 * i + 1])
                i >>= 1
            }
        }
        func query(_ l: Int, _ r: Int) -> Int {
            var res = INF
            var left = l + size
            var right = r + size
            while left <= right {
                if (left & 1) == 1 {
                    res = min(res, seg[left])
                    left += 1
                }
                if (right & 1) == 0 {
                    res = min(res, seg[right])
                    right -= 1
                }
                left >>= 1
                right >>= 1
            }
            return res
        }
        // process columns from rightmost to leftmost
        let xs = columnMap.keys.sorted()
        var maxArea = -1
        for x in xs.reversed() {
            guard let yList = columnMap[x] else { continue }
            if yList.count >= 2 {
                for i in 0..<(yList.count - 1) {
                    let y1 = yList[i]
                    let y2 = yList[i + 1]
                    let lIdx = yToIdx[y1]!
                    let rIdx = yToIdx[y2]!
                    let minX = query(lIdx, rIdx)
                    if minX != INF {
                        if let listR = columnMap[minX] {
                            // binary search for y1 in listR
                            var lo = 0
                            var hi = listR.count - 1
                            while lo <= hi {
                                let mid = (lo + hi) >> 1
                                if listR[mid] < y1 {
                                    lo = mid + 1
                                } else if listR[mid] > y1 {
                                    hi = mid - 1
                                } else {
                                    // found y1 at position mid, check next is y2
                                    if mid + 1 < listR.count && listR[mid + 1] == y2 {
                                        let area = (minX - x) * (y2 - y1)
                                        if area > maxArea { maxArea = area }
                                    }
                                    break
                                }
                            }
                        }
                    }
                }
            }
            // insert current column points into segment tree
            for y in yList {
                let idx = yToIdx[y]!
                update(idx, x)
            }
        }
        return maxArea
    }
}
```

## Kotlin

```kotlin
import java.util.*
import kotlin.math.min

class Solution {
    fun maxRectangleArea(xCoord: IntArray, yCoord: IntArray): Long {
        val n = xCoord.size
        // map x -> list of y's
        val xMap = HashMap<Int, MutableList<Int>>(n * 2)
        val allY = ArrayList<Int>(n)
        for (i in 0 until n) {
            val x = xCoord[i]
            val y = yCoord[i]
            xMap.computeIfAbsent(x) { ArrayList() }.add(y)
            allY.add(y)
        }
        // sort y lists per x
        for (list in xMap.values) {
            list.sort()
        }
        // compress y coordinates
        val sortedY = allY.distinct().sorted()
        val yToIdx = HashMap<Int, Int>(sortedY.size * 2)
        for (i in sortedY.indices) {
            yToIdx[sortedY[i]] = i
        }
        val m = sortedY.size
        // segment tree for range minimum x
        class SegTree(val size: Int) {
            private val INF = Int.MAX_VALUE
            private val tree = IntArray(size * 4) { INF }

            fun update(pos: Int, value: Int) {
                update(1, 0, size - 1, pos, value)
            }

            private fun update(node: Int, l: Int, r: Int, pos: Int, value: Int) {
                if (l == r) {
                    tree[node] = value
                    return
                }
                val mid = (l + r) ushr 1
                if (pos <= mid) update(node shl 1, l, mid, pos, value)
                else update(node shl 1 or 1, mid + 1, r, pos, value)
                tree[node] = min(tree[node shl 1], tree[node shl 1 or 1])
            }

            fun query(left: Int, right: Int): Int {
                return query(1, 0, size - 1, left, right)
            }

            private fun query(node: Int, l: Int, r: Int, ql: Int, qr: Int): Int {
                if (qr < l || r < ql) return INF
                if (ql <= l && r <= qr) return tree[node]
                val mid = (l + r) ushr 1
                val a = query(node shl 1, l, mid, ql, qr)
                val b = query(node shl 1 or 1, mid + 1, r, ql, qr)
                return min(a, b)
            }
        }

        val seg = SegTree(m)

        // sorted unique x's ascending
        val xs = xMap.keys.sorted()
        var maxArea = -1L

        for (idx in xs.size - 1 downTo 0) {
            val xl = xs[idx]
            val yList = xMap[xl]!!

            // evaluate each consecutive pair on this left side
            for (k in 0 until yList.size - 1) {
                val y1 = yList[k]
                val y2 = yList[k + 1]
                val i1 = yToIdx[y1]!!
                val i2 = yToIdx[y2]!!

                val xr = seg.query(i1, i2)
                if (xr == Int.MAX_VALUE) continue

                // verify right side has both y1 and y2 as consecutive points
                val rightYList = xMap[xr] ?: continue
                val pos1 = Collections.binarySearch(rightYList, y1)
                val pos2 = Collections.binarySearch(rightYList, y2)
                if (pos1 >= 0 && pos2 >= 0 && kotlin.math.abs(pos1 - pos2) == 1) {
                    val area = (xr - xl).toLong() * (y2 - y1).toLong()
                    if (area > maxArea) maxArea = area
                }
            }

            // insert current column points into segment tree
            for (y in yList) {
                seg.update(yToIdx[y]!!, xl)
            }
        }

        return maxArea
    }
}
```

## Dart

```dart
class Solution {
  int maxRectangleArea(List<int> xCoord, List<int> yCoord) {
    int n = xCoord.length;
    // Group points by their x-coordinate
    Map<int, List<int>> col = {};
    for (int i = 0; i < n; i++) {
      col.putIfAbsent(xCoord[i], () => []).add(yCoord[i]);
    }
    // Sort y-lists for each column
    for (var entry in col.entries) {
      entry.value.sort();
    }

    // Coordinate compression for y values
    List<int> allY = List.from(yCoord);
    allY.sort();
    List<int> uniqY = [];
    for (int v in allY) {
      if (uniqY.isEmpty || v != uniqY.last) uniqY.add(v);
    }
    Map<int, int> yToIdx = {};
    for (int i = 0; i < uniqY.length; i++) {
      yToIdx[uniqY[i]] = i;
    }
    int m = uniqY.length;

    const int INF = 1 << 60;
    SegmentTree seg = SegmentTree(m, INF);

    // Process columns from right to left
    List<int> xs = col.keys.toList()..sort();
    int maxArea = -1;

    for (int xi = xs.length - 1; xi >= 0; xi--) {
      int xL = xs[xi];
      List<int> yList = col[xL]!;

      // Examine each adjacent pair of points in this column
      for (int i = 0; i < yList.length - 1; i++) {
        int y1 = yList[i];
        int y2 = yList[i + 1];
        int idx1 = yToIdx[y1]!;
        int idx2 = yToIdx[y2]!;

        // Find the nearest column to the right that has any point with y in [y1, y2]
        int xR = seg.query(idx1, idx2);
        if (xR == INF) continue;

        // Verify that column xR contains exactly these two points and nothing between them
        List<int> rList = col[xR]!;
        int pos1 = _lowerBound(rList, y1);
        if (pos1 >= rList.length || rList[pos1] != y1) continue;
        int pos2 = _lowerBound(rList, y2);
        if (pos2 >= rList.length || rList[pos2] != y2) continue;
        if (pos2 - pos1 != 1) continue; // there is another point between them

        int area = (xR - xL) * (y2 - y1);
        if (area > maxArea) maxArea = area;
      }

      // Insert current column's points into the segment tree
      for (int y in yList) {
        int idx = yToIdx[y]!;
        seg.update(idx, xL);
      }
    }

    return maxArea;
  }

  int _lowerBound(List<int> arr, int target) {
    int l = 0, r = arr.length;
    while (l < r) {
      int mid = (l + r) >> 1;
      if (arr[mid] < target) {
        l = mid + 1;
      } else {
        r = mid;
      }
    }
    return l;
  }
}

class SegmentTree {
  late List<int> _tree;
  final int _n;
  final int _inf;

  SegmentTree(this._n, this._inf) {
    _tree = List.filled(4 * _n, _inf);
  }

  void update(int idx, int value) => _update(1, 0, _n - 1, idx, value);

  void _update(int node, int l, int r, int idx, int value) {
    if (l == r) {
      _tree[node] = value;
      return;
    }
    int mid = (l + r) >> 1;
    if (idx <= mid) {
      _update(node << 1, l, mid, idx, value);
    } else {
      _update((node << 1) | 1, mid + 1, r, idx, value);
    }
    _tree[node] = _tree[node << 1] < _tree[(node << 1) | 1]
        ? _tree[node << 1]
        : _tree[(node << 1) | 1];
  }

  int query(int left, int right) => _query(1, 0, _n - 1, left, right);

  int _query(int node, int l, int r, int ql, int qr) {
    if (qr < l || ql > r) return _inf;
    if (ql <= l && r <= qr) return _tree[node];
    int mid = (l + r) >> 1;
    int leftMin = _query(node << 1, l, mid, ql, qr);
    int rightMin = _query((node << 1) | 1, mid + 1, r, ql, qr);
    return leftMin < rightMin ? leftMin : rightMin;
  }
}
```

## Golang

```go
func maxRectangleArea(xCoord []int, yCoord []int) int64 {
	type point struct {
		x  int
		y  int
		yi int // compressed y index
	}
	n := len(xCoord)
	if n < 4 {
		return -1
	}
	points := make([]point, n)
	ys := make([]int, n)
	for i := 0; i < n; i++ {
		points[i] = point{x: xCoord[i], y: yCoord[i]}
		ys[i] = yCoord[i]
	}
	// compress y
	sortInts := func(a []int) {
		if len(a) <= 1 {
			return
		}
		quickSort(a, 0, len(a)-1)
	}
	sortInts(ys)
	uniq := make([]int, 0, n)
	for _, v := range ys {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}
	yToIdx := make(map[int]int, len(uniq))
	for i, v := range uniq {
		yToIdx[v] = i
	}
	for i := 0; i < n; i++ {
		points[i].yi = yToIdx[points[i].y]
	}
	// sort points by x then y
	sort.Slice(points, func(i, j int) bool {
		if points[i].x == points[j].x {
			return points[i].y < points[j].y
		}
		return points[i].x < points[j].x
	})
	// segment tree for max last seen x per y index
	type segTree struct {
		size int
		data []int
	}
	newSeg := func(m int) *segTree {
		sz := 1
		for sz < m {
			sz <<= 1
		}
		d := make([]int, 2*sz)
		for i := range d {
			d[i] = -1
		}
		return &segTree{size: sz, data: d}
	}
	update := func(st *segTree, pos int, val int) {
		pos += st.size
		if val > st.data[pos] {
			st.data[pos] = val
		}
		for pos > 1 {
			pos >>= 1
			left, right := st.data[pos<<1], st.data[(pos<<1)|1]
			if left > right {
				st.data[pos] = left
			} else {
				st.data[pos] = right
			}
		}
	}
	query := func(st *segTree, l, r int) int {
		if l > r {
			return -1
		}
		l += st.size
		r += st.size
		res := -1
		for l <= r {
			if (l & 1) == 1 {
				if st.data[l] > res {
					res = st.data[l]
				}
				l++
			}
			if (r & 1) == 0 {
				if st.data[r] > res {
					res = st.data[r]
				}
				r--
			}
			l >>= 1
			r >>= 1
		}
		return res
	}
	st := newSeg(len(uniq))
	pairMap := make(map[int64]int)
	var ans int64 = -1

	for i := 0; i < n; {
		j := i
		curX := points[i].x
		for j < n && points[j].x == curX {
			j++
		}
		// process pairs as right side
		for k := i; k+1 < j; k++ {
			y1, y2 := points[k].y, points[k+1].y
			if y1 == y2 {
				continue
			}
			key := (int64(y1) << 32) | int64(y2)
			if leftX, ok := pairMap[key]; ok {
				idx1, idx2 := points[k].yi, points[k+1].yi
				var interiorMax int
				if idx2-idx1 > 1 {
					interiorMax = query(st, idx1+1, idx2-1)
				} else {
					interiorMax = -1
				}
				if interiorMax <= leftX {
					area := int64(curX-leftX) * int64(y2-y1)
					if area > ans {
						ans = area
					}
				}
			}
		}
		// store current column as potential left side
		for k := i; k+1 < j; k++ {
			y1, y2 := points[k].y, points[k+1].y
			if y1 == y2 {
				continue
			}
			key := (int64(y1) << 32) | int64(y2)
			pairMap[key] = curX
		}
		// update segment tree with current column's y positions
		for k := i; k < j; k++ {
			update(st, points[k].yi, curX)
		}
		i = j
	}
	return ans
}
```

## Ruby

```ruby
def max_rectangle_area(x_coord, y_coord)
  n = x_coord.size
  return -1 if n < 4

  # Coordinate compression for y values
  ys_unique = y_coord.uniq.sort
  y_index = {}
  ys_unique.each_with_index { |v, i| y_index[v] = i }
  m = ys_unique.size

  # Group points by x and sort their y's
  x_to_ys = Hash.new { |h, k| h[k] = [] }
  n.times do |i|
    x_to_ys[x_coord[i]] << y_coord[i]
  end
  adj = {} # adjacency: for each x, map y -> next higher y at same x
  x_to_ys.each do |x, arr|
    arr.sort!
    if arr.size > 1
      inner = {}
      (0...arr.size - 1).each do |i|
        inner[arr[i]] = arr[i + 1]
      end
      adj[x] = inner
    else
      adj[x] = {}
    end
  end

  # Segment tree for range minimum query over x values
  INF = (1 << 60)
  size = 1
  size <<= 1 while size < m
  seg = Array.new(2 * size, INF)

  update = lambda do |pos, val|
    i = pos + size
    seg[i] = val
    i >>= 1
    while i > 0
      left = seg[i << 1]
      right = seg[(i << 1) | 1]
      seg[i] = left < right ? left : right
      i >>= 1
    end
  end

  query = lambda do |l, r|
    res = INF
    l += size
    r += size
    while l <= r
      if (l & 1) == 1
        v = seg[l]
        res = v < res ? v : res
        l += 1
      end
      if (r & 1) == 0
        v = seg[r]
        res = v < res ? v : res
        r -= 1
      end
      l >>= 1
      r >>= 1
    end
    res
  end

  max_area = -1
  xs_desc = x_to_ys.keys.sort.reverse

  xs_desc.each do |x|
    ys = x_to_ys[x]
    # evaluate rectangles using this x as left side
    (0...ys.size - 1).each do |i|
      y1 = ys[i]
      y2 = ys[i + 1]
      idx1 = y_index[y1]
      idx2 = y_index[y2]
      min_right_x = query.call(idx1, idx2)
      next if min_right_x == INF
      # verify that at min_right_x the two y's are consecutive (no other point on border)
      adj_map = adj[min_right_x]
      next unless adj_map && adj_map[y1] == y2
      area = (min_right_x - x) * (y2 - y1)
      max_area = area if area > max_area
    end
    # insert current column points into segment tree for future left sides
    ys.each do |y|
      update.call(y_index[y], x)
    end
  end

  max_area
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable
  def maxRectangleArea(xCoord: Array[Int], yCoord: Array[Int]): Long = {
    val n = xCoord.length
    // compress y coordinates
    val uniqY = yCoord.distinct.sorted
    val yToIdx = new mutable.HashMap[Int, Int]()
    for (i <- uniqY.indices) yToIdx(uniqY(i)) = i
    val m = uniqY.length

    // sort points by x
    val order = (0 until n).toArray.sortBy(xCoord(_))
    val xsList = new mutable.ArrayBuffer[Int]()
    val ysLists = new mutable.ArrayBuffer[Array[Int]]()
    var i = 0
    while (i < n) {
      val curX = xCoord(order(i))
      val buf = new mutable.ArrayBuffer[Int]()
      while (i < n && xCoord(order(i)) == curX) {
        buf += yToIdx(yCoord(order(i)))
        i += 1
      }
      buf.sortInPlace()
      xsList += curX
      ysLists += buf.toArray
    }

    // segment tree for range minimum of next X
    class SegTree(val size: Int) {
      val INF: Long = Long.MaxValue / 4
      private val n0: Int = {
        var p = 1
        while (p < size) p <<= 1
        p
      }
      private val tree = Array.fill(2 * n0)(INF)
      def update(pos: Int, value: Long): Unit = {
        var p = pos + n0
        tree(p) = value
        p >>= 1
        while (p > 0) {
          tree(p) = math.min(tree(p << 1), tree(p << 1 | 1))
          p >>= 1
        }
      }
      def query(l: Int, r: Int): Long = { // inclusive
        var left = l + n0
        var right = r + n0
        var res = INF
        while (left <= right) {
          if ((left & 1) == 1) {
            res = math.min(res, tree(left))
            left += 1
          }
          if ((right & 1) == 0) {
            res = math.min(res, tree(right))
            right -= 1
          }
          left >>= 1
          right >>= 1
        }
        res
      }
    }

    val seg = new SegTree(m)
    val INF: Long = Long.MaxValue / 4
    val nextX = Array.fill[Long](m)(INF)

    var answer: Long = -1L

    for (idx <- xsList.indices.reverse) {
      val xCurr = xsList(idx)
      val yArr = ysLists(idx)
      // evaluate rectangles with left side at xCurr
      var j = 0
      while (j + 1 < yArr.length) {
        val y1 = yArr(j)
        val y2 = yArr(j + 1)
        val nx1 = nextX(y1)
        val nx2 = nextX(y2)
        if (nx1 != INF && nx2 != INF) {
          val rightX = math.max(nx1, nx2)
          val minNext = seg.query(y1, y2)
          if (rightX == minNext && rightX != INF) {
            val area = (rightX - xCurr).toLong * (uniqY(y2) - uniqY(y1)).toLong
            if (area > answer) answer = area
          }
        }
        j += 1
      }
      // update structures with points at current column
      for (y <- yArr) {
        nextX(y) = xCurr.toLong
        seg.update(y, xCurr.toLong)
      }
    }

    answer
  }
}
```

## Rust

```rust
use std::cmp::min;
use std::collections::HashMap;

struct SegTree {
    n: usize,
    data: Vec<i32>,
}
impl SegTree {
    fn new(size: usize) -> Self {
        let mut n = 1usize;
        while n < size { n <<= 1; }
        SegTree { n, data: vec![i32::MAX; n * 2] }
    }
    fn update(&mut self, mut pos: usize, val: i32) {
        pos += self.n;
        self.data[pos] = val;
        while pos > 1 {
            pos >>= 1;
            self.data[pos] = min(self.data[pos << 1], self.data[(pos << 1) | 1]);
        }
    }
    // inclusive query
    fn query(&self, mut l: usize, mut r: usize) -> i32 {
        let mut res = i32::MAX;
        l += self.n;
        r += self.n;
        while l <= r {
            if (l & 1) == 1 {
                res = min(res, self.data[l]);
                l += 1;
            }
            if (r & 1) == 0 {
                res = min(res, self.data[r]);
                r -= 1;
            }
            l >>= 1;
            r >>= 1;
        }
        res
    }
}

impl Solution {
    pub fn max_rectangle_area(x_coord: Vec<i32>, y_coord: Vec<i32>) -> i64 {
        let n = x_coord.len();
        if n < 4 { return -1; }

        // compress y coordinates
        let mut uniq_y = y_coord.clone();
        uniq_y.sort_unstable();
        uniq_y.dedup();
        let m_y = uniq_y.len();

        let mut y_to_idx: HashMap<i32, usize> = HashMap::with_capacity(m_y * 2);
        for (i, &y) in uniq_y.iter().enumerate() {
            y_to_idx.insert(y, i);
        }

        // collect unique x coordinates
        let mut uniq_x = x_coord.clone();
        uniq_x.sort_unstable();
        uniq_x.dedup();
        let m_x = uniq_x.len();

        let mut x_to_idx: HashMap<i32, usize> = HashMap::with_capacity(m_x * 2);
        for (i, &x) in uniq_x.iter().enumerate() {
            x_to_idx.insert(x, i);
        }

        // column y lists
        let mut cols: Vec<Vec<usize>> = vec![Vec::new(); m_x];
        for i in 0..n {
            let xi = x_coord[i];
            let yi = y_coord[i];
            let col_idx = *x_to_idx.get(&xi).unwrap();
            let y_idx = *y_to_idx.get(&yi).unwrap();
            cols[col_idx].push(y_idx);
        }
        for v in cols.iter_mut() {
            v.sort_unstable();
        }

        // segment tree for nearest right x per y
        let mut seg = SegTree::new(m_y);

        let mut max_area: i64 = -1;

        // sweep from right to left
        for i_rev in (0..m_x).rev() {
            let cur_x = uniq_x[i_rev];
            let ys = &cols[i_rev];
            if ys.len() >= 2 {
                for j in 0..ys.len() - 1 {
                    let y1 = ys[j];
                    let y2 = ys[j + 1];
                    let min_right = seg.query(y1, y2);
                    if min_right != i32::MAX {
                        // check right column
                        if let Some(&r_idx) = x_to_idx.get(&min_right) {
                            let right_ys = &cols[r_idx];
                            if let Ok(pos) = right_ys.binary_search(&y1) {
                                if pos + 1 < right_ys.len() && right_ys[pos + 1] == y2 {
                                    let dy = (uniq_y[y2] - uniq_y[y1]) as i64;
                                    let dx = (min_right - cur_x) as i64;
                                    let area = dx * dy;
                                    if area > max_area { max_area = area; }
                                }
                            }
                        }
                    }
                }
            }
            // update segment tree with current column points
            for &y_idx in ys {
                seg.update(y_idx, cur_x);
            }
        }

        max_area
    }
}
```

## Racket

```racket
(define (max-rectangle-area xCoord yCoord)
  (let* ((n (length xCoord))
         ;; compress y coordinates
         (uniq-y (sort (remove-duplicates (copy-list yCoord)) <))
         (m (length uniq-y))
         (y->idx (make-hash))
         (idx->y (list->vector uniq-y)))
    (for ([i (in-range m)])
      (hash-set! y->idx (list-ref uniq-y i) i))
    ;; map x -> list of compressed y indices
    (define x->ys (make-hash))
    (for ([i (in-range n)])
      (let* ((x (list-ref xCoord i))
             (y (list-ref yCoord i))
             (yi (hash-ref y->idx y)))
        (hash-set! x->ys x (cons yi (hash-ref x->ys x '())))))
    ;; sort each y list
    (for ([k (in-hash-keys x->ys)])
      (hash-set! x->ys k (sort (hash-ref x->ys k) <)))
    ;; sorted distinct xs descending
    (define xs (sort (hash-keys x->ys) >))
    ;; segment tree for range minimum of nextX
    (define INF (expt 2 60))
    (define seg (make-vector (* 4 m) INF))
    (define nextX (make-vector m INF))
    (define (update node l r idx val)
      (if (= l r)
          (vector-set! seg node val)
          (let* ((mid (quotient (+ l r) 2)))
            (if (<= idx mid)
                (update (* node 2) l mid idx val)
                (update (+ (* node 2) 1) (+ mid 1) r idx val))
            (vector-set! seg node
                         (min (vector-ref seg (* node 2))
                              (vector-ref seg (+ (* node 2) 1)))))))
    (define (query node l r ql qr)
      (if (or (> ql r) (< qr l))
          INF
          (if (and (<= ql l) (>= qr r))
              (vector-ref seg node)
              (let* ((mid (quotient (+ l r) 2)))
                (min (query (* node 2) l mid ql qr)
                     (query (+ (* node 2) 1) (+ mid 1) r ql qr))))))
    (define ans -1)
    ;; sweep from right to left
    (for ([xl xs])
      (let ((ys-list (hash-ref x->ys xl)))
        (for ([i (in-range (- (length ys-list) 1))])
          (let* ((a (list-ref ys-list i))
                 (b (list-ref ys-list (+ i 1))))
            (when (< a b)
              (let ((minNext (query 1 0 (- m 1) a b)))
                (when (< minNext INF)
                  (when (and (= (vector-ref nextX a) minNext)
                             (= (vector-ref nextX b) minNext))
                    (let* ((area (* (- minNext xl)
                                    (- (vector-ref idx->y b)
                                       (vector-ref idx->y a)))))
                      (when (> area ans) (set! ans area))))))))))
      ;; insert current column points into structure
      (for ([yi (in-list (hash-ref x->ys xl))])
        (vector-set! nextX yi xl)
        (update 1 0 (- m 1) yi xl)))
    ans))
```

## Erlang

```erlang
-define(INF, 1000000000000000).

-spec max_rectangle_area(XCoord :: [integer()], YCoord :: [integer()]) -> integer().
max_rectangle_area(XCoord, YCoord) ->
    YsSorted = lists:usort(YCoord),
    M = length(YsSorted),
    YMap = maps:from_list(lists:zip(YsSorted, lists:seq(0, M - 1))),
    YValsArr0 = array:new(M, {default, 0}),
    YValsArr = fill_yvals(YsSorted, YValsArr0, 0),

    Points = lists:zip(XCoord, YCoord),
    Group = group_points(Points, YMap, #{}),

    XList = maps:keys(Group),
    XSorted = lists:sort(fun(A, B) -> A > B end, XList),

    Tree0 = seg_new(M),
    MaxArea = process_columns(XSorted, Group, YValsArr, M, -1, Tree0),
    MaxArea.

fill_yvals([], Arr, _) ->
    Arr;
fill_yvals([Val | Rest], Arr, Idx) ->
    NewArr = array:set(Idx + 1, Val, Arr),
    fill_yvals(Rest, NewArr, Idx + 1).

group_points([], _YMap, Acc) ->
    Acc;
group_points([{X, Y} | Rest], YMap, Acc) ->
    Idx = maps:get(Y, YMap),
    UpdatedAcc =
        case maps:is_key(X, Acc) of
            true -> maps:update_with(X, fun(L) -> [Idx | L] end, Acc);
            false -> maps:put(X, [Idx], Acc)
        end,
    group_points(Rest, YMap, UpdatedAcc).

process_columns([], _Group, _YValsArr, _M, MaxArea, _Tree) ->
    MaxArea;
process_columns([X | Rest], Group, YValsArr, M, MaxArea0, Tree0) ->
    YsIdx = maps:get(X, Group),
    SortedYs = lists:sort(YsIdx),
    {MaxArea1, TreeAfterPairs} = process_pairs(SortedYs, X, Tree0, YValsArr, M, MaxArea0),
    NewTree = lists:foldl(fun(Yi, T) -> seg_update(T, 1, 0, M - 1, Yi, X) end,
                          TreeAfterPairs, SortedYs),
    process_columns(Rest, Group, YValsArr, M, MaxArea1, NewTree).

process_pairs([], _X, Tree, _YValsArr, _M, MaxArea) ->
    {MaxArea, Tree};
process_pairs([_], _X, Tree, _YValsArr, _M, MaxArea) ->
    {MaxArea, Tree};
process_pairs(Ys, X, Tree, YValsArr, M, MaxArea0) ->
    Pairs = consecutive_pairs(Ys),
    lists:foldl(fun({Y1, Y2}, {CurMax, CurTree}) ->
        MinRight = seg_query(CurTree, 1, 0, M - 1, Y1, Y2),
        if MinRight =/= ?INF ->
            XR1 = seg_query(CurTree, 1, 0, M - 1, Y1, Y1),
            XR2 = seg_query(CurTree, 1, 0, M - 1, Y2, Y2),
            if XR1 == MinRight andalso XR2 == MinRight ->
                Height = array:get(Y2 + 1, YValsArr) - array:get(Y1 + 1, YValsArr),
                Area = (MinRight - X) * Height,
                NewMax = if Area > CurMax -> Area; true -> CurMax end,
                {NewMax, CurTree};
            true ->
                {CurMax, CurTree}
            end;
        true ->
            {CurMax, CurTree}
        end
    end, {MaxArea0, Tree}, Pairs).

consecutive_pairs([A, B | Rest]) ->
    [{A, B} | consecutive_pairs([B | Rest])];
consecutive_pairs(_) -> [].

seg_new(M) ->
    Size = 4 * M,
    array:new(Size, {default, ?INF}).

seg_update(Tree, Node, L, R, Idx, Val) ->
    if L == R ->
        array:set(Node, Val, Tree);
    true ->
        Mid = (L + R) div 2,
        UpdatedTree =
            if Idx =< Mid ->
                seg_update(Tree, Node * 2, L, Mid, Idx, Val);
            true ->
                seg_update(Tree, Node * 2 + 1, Mid + 1, R, Idx, Val)
            end,
        LeftMin = array:get(Node * 2, UpdatedTree),
        RightMin = array:get(Node * 2 + 1, UpdatedTree),
        Min = if LeftMin < RightMin -> LeftMin; true -> RightMin end,
        array:set(Node, Min, UpdatedTree)
    end.

seg_query(Tree, Node, L, R, QL, QR) ->
    if QL > R orelse QR < L ->
        ?INF;
    (QL =< L andalso R =< QR) ->
        array:get(Node, Tree);
    true ->
        Mid = (L + R) div 2,
        Min1 = seg_query(Tree, Node * 2, L, Mid, QL, QR),
        Min2 = seg_query(Tree, Node * 2 + 1, Mid + 1, R, QL, QR),
        if Min1 < Min2 -> Min1; true -> Min2 end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_rectangle_area(x_coord :: [integer], y_coord :: [integer]) :: integer
  def max_rectangle_area(x_coord, y_coord) do
    points = Enum.zip(x_coord, y_coord)

    # compress y coordinates
    ys =
      y_coord
      |> Enum.uniq()
      |> Enum.sort()

    y_to_idx =
      ys
      |> Enum.with_index()
      |> Map.new(fn {y, i} -> {y, i} end)

    m = length(ys)
    seg = build_seg(m)

    # group points by x and sort y indices
    points_by_x =
      points
      |> Enum.group_by(fn {x, _y} -> x end)
      |> Enum.map(fn {x, lst} ->
        ylist =
          lst
          |> Enum.map(fn {_x, y} -> Map.fetch!(y_to_idx, y) end)
          |> Enum.sort()

        {x, ylist}
      end)
      |> Enum.sort_by(fn {x, _} -> x end)

    y_vals_arr = :array.from_list(ys)

    {ans, _, _} =
      Enum.reduce(points_by_x, {-1, %{}, seg}, fn {x, ylist},
                                                {cur_ans, pair_map, cur_seg} ->
        # process consecutive pairs before updating segment tree
        {new_ans, new_pair_map} =
          if length(ylist) < 2 do
            {cur_ans, pair_map}
          else
            Enum.reduce(0..(length(ylist) - 2), {cur_ans, pair_map}, fn i,
                                                                    {a_acc,
                                                                     pmap_acc} ->
              y1 = Enum.at(ylist, i)
              y2 = Enum.at(ylist, i + 1)

              max_last = seg_query(cur_seg, y1, y2)

              key = {y1, y2}
              a_new =
                case Map.get(pmap_acc, key) do
                  nil ->
                    a_acc

                  prev_x when prev_x > max_last ->
                    area =
                      (x - prev_x) *
                        (:array.get(y2, y_vals_arr) -
                           :array.get(y1, y_vals_arr))

                    if area > a_acc, do: area, else: a_acc

                  _prev_x ->
                    a_acc
                end

              pmap_new = Map.put(pmap_acc, key, x)
              {a_new, pmap_new}
            end)
          end

        # update segment tree with current y's
        updated_seg =
          Enum.reduce(ylist, cur_seg, fn yidx, seg_acc ->
            seg_update(seg_acc, yidx, x)
          end)

        {new_ans, new_pair_map, updated_seg}
      end)

    ans
  end

  # Segment tree helpers
  defp build_seg(n) do
    size =
      1
      |> Stream.iterate(&(&1 * 2))
      |> Enum.find(fn s -> s >= n end)

    %{size: size, tree: :array.new(size * 2, default: -1)}
  end

  defp seg_update(%{size: size, tree: arr} = st, idx, val) do
    pos = idx + size
    arr = :array.set(pos, val, arr)
    arr = update_up(div(pos, 2), arr)
    %{st | tree: arr}
  end

  defp update_up(0, arr), do: arr

  defp update_up(p, arr) do
    left = :array.get(p * 2, arr)
    right = :array.get(p * 2 + 1, arr)
    maxv = if left > right, do: left, else: right
    arr = :array.set(p, maxv, arr)
    update_up(div(p, 2), arr)
  end

  defp seg_query(%{size: size, tree: arr}, l, r) do
    query_rec(l + size, r + size, -1, arr)
  end

  defp query_rec(l, r, acc, _arr) when l > r, do: acc

  defp query_rec(l, r, acc, arr) do
    {l1, acc1} =
      if rem(l, 2) == 1 do
        {l + 1, max(acc, :array.get(l, arr))}
      else
        {l, acc}
      end

    {r1, acc2} =
      if rem(r, 2) == 0 do
        {r - 1, max(acc1, :array.get(r, arr))}
      else
        {r, acc1}
      end

    query_rec(div(l1, 2), div(r1, 2), acc2, arr)
  end
end
```

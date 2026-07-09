# 2736. Maximum Sum Queries

## Cpp

```cpp
class Solution {
public:
    struct Fenwick {
        int n;
        vector<int> bit;
        Fenwick(int n): n(n), bit(n+1, INT_MIN) {}
        void update(int idx, int val){
            for(; idx<=n; idx+=idx&-idx)
                bit[idx] = max(bit[idx], val);
        }
        int query(int idx){
            int res = INT_MIN;
            for(; idx>0; idx-=idx&-idx)
                res = max(res, bit[idx]);
            return res;
        }
    };
    
    vector<int> maximumSumQueries(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        int n = nums1.size();
        vector<pair<int,int>> pts(n);
        for(int i=0;i<n;++i) pts[i] = {nums1[i], nums2[i]};
        sort(pts.begin(), pts.end(), [&](const auto& a, const auto& b){
            return a.first > b.first;
        });
        
        // unique descending ys from points
        vector<int> uniqY = nums2;
        sort(uniqY.begin(), uniqY.end());
        uniqY.erase(unique(uniqY.begin(), uniqY.end()), uniqY.end());
        reverse(uniqY.begin(), uniqY.end()); // now descending
        
        Fenwick fw((int)uniqY.size());
        
        struct Q {
            int x, y, idx;
        };
        vector<Q> qs;
        qs.reserve(queries.size());
        for(int i=0;i<(int)queries.size();++i){
            qs.push_back({queries[i][0], queries[i][1], i});
        }
        sort(qs.begin(), qs.end(), [&](const Q& a, const Q& b){
            return a.x > b.x;
        });
        
        vector<int> ans(queries.size(), -1);
        int p = 0;
        for(const auto& q: qs){
            while(p < n && pts[p].first >= q.x){
                int y = pts[p].second;
                int sum = pts[p].first + pts[p].second;
                // find index of y in descending uniqY
                int idx = lower_bound(uniqY.begin(), uniqY.end(), y, greater<int>()) - uniqY.begin() + 1;
                fw.update(idx, sum);
                ++p;
            }
            // query for y >= q.y
            auto it = lower_bound(uniqY.begin(), uniqY.end(), q.y, greater<int>());
            if(it == uniqY.end()){
                ans[q.idx] = -1;
            }else{
                int idx = (it - uniqY.begin()) + 1;
                int best = fw.query(idx);
                ans[q.idx] = (best==INT_MIN ? -1 : best);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] maximumSumQueries(int[] nums1, int[] nums2, int[][] queries) {
        int n = nums1.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        java.util.Arrays.sort(order, (a, b) -> Integer.compare(nums1[b], nums1[a])); // descending by nums1

        class Q {
            int x, y, idx;
            Q(int x, int y, int idx) { this.x = x; this.y = y; this.idx = idx; }
        }

        int m = queries.length;
        Q[] qs = new Q[m];
        for (int i = 0; i < m; i++) {
            qs[i] = new Q(queries[i][0], queries[i][1], i);
        }
        java.util.Arrays.sort(qs, (a, b) -> Integer.compare(b.x, a.x)); // descending by x

        int[] ans = new int[m];
        java.util.TreeMap<Integer, Integer> map = new java.util.TreeMap<>();

        int p = 0;
        for (Q q : qs) {
            while (p < n && nums1[order[p]] >= q.x) {
                int idx = order[p];
                int y = nums2[idx];
                int sum = nums1[idx] + nums2[idx];

                Integer higherKey = map.ceilingKey(y);
                if (higherKey != null && map.get(higherKey) >= sum) {
                    // dominated by a point with larger or equal y and better sum
                } else {
                    // remove lower keys that are now dominated
                    while (true) {
                        Integer lowerKey = map.lowerKey(y);
                        if (lowerKey == null) break;
                        if (map.get(lowerKey) <= sum) {
                            map.remove(lowerKey);
                        } else {
                            break;
                        }
                    }
                    map.put(y, sum);
                }
                p++;
            }

            Integer key = map.ceilingKey(q.y);
            ans[q.idx] = (key == null) ? -1 : map.get(key);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSumQueries(self, nums1, nums2, queries):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import bisect

        n = len(nums1)
        points = [(nums1[i], nums2[i]) for i in range(n)]
        points.sort(key=lambda x: -x[0])  # descending by nums1

        qlist = [(queries[i][0], queries[i][1], i) for i in range(len(queries))]
        qlist.sort(key=lambda x: -x[0])   # descending by xi

        # coordinate compression for nums2 and query yi
        all_y = set(nums2)
        for _, y, _ in qlist:
            all_y.add(y)
        sorted_y = sorted(all_y)
        N = len(sorted_y)

        # map exact y to rank (0-index)
        y_to_rank = {v: i for i, v in enumerate(sorted_y)}

        class BITMax:
            def __init__(self, size):
                self.N = size
                self.tree = [-10**18] * (size + 2)

            def update(self, idx, val):
                while idx <= self.N:
                    if val > self.tree[idx]:
                        self.tree[idx] = val
                    idx += idx & -idx

            def query(self, idx):
                res = -10**18
                while idx > 0:
                    if self.tree[idx] > res:
                        res = self.tree[idx]
                    idx -= idx & -idx
                return res

        bit = BITMax(N)

        ans = [-1] * len(queries)
        p = 0
        for xi, yi, qi in qlist:
            # add all points with nums1 >= xi
            while p < n and points[p][0] >= xi:
                x_val, y_val = points[p]
                sum_xy = x_val + y_val
                rank = y_to_rank[y_val]          # 0-index
                rev_idx = N - rank               # 1..N
                bit.update(rev_idx, sum_xy)
                p += 1

            pos = bisect.bisect_left(sorted_y, yi)   # first index with y >= yi
            if pos == N:
                ans[qi] = -1
            else:
                rev_q = N - pos
                best = bit.query(rev_q)
                ans[qi] = best if best > -10**17 else -1

        return ans
```

## Python3

```python
class Solution:
    def maximumSumQueries(self, nums1, nums2, queries):
        from bisect import bisect_left
        n = len(nums1)
        points = [(nums1[i], nums2[i]) for i in range(n)]
        points.sort(key=lambda x: -x[0])  # descending by nums1

        qlist = [(xi, yi, idx) for idx, (xi, yi) in enumerate(queries)]
        qlist.sort(key=lambda x: -x[0])   # descending by xi

        all_vals = set(nums2)
        for _, yi in queries:
            all_vals.add(yi)
        comp = sorted(all_vals)
        m = len(comp)

        size = 1
        while size < m:
            size <<= 1
        seg = [-1] * (2 * size)

        def update(pos, value):
            pos += size
            if seg[pos] >= value:
                return
            seg[pos] = value
            pos >>= 1
            while pos:
                new_val = seg[pos << 1]
                right = seg[(pos << 1) | 1]
                if right > new_val:
                    new_val = right
                if seg[pos] == new_val:
                    break
                seg[pos] = new_val
                pos >>= 1

        def query(l, r):
            l += size
            r += size
            res = -1
            while l < r:
                if l & 1:
                    if seg[l] > res:
                        res = seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    if seg[r] > res:
                        res = seg[r]
                l >>= 1
                r >>= 1
            return res

        ans = [-1] * len(queries)
        p = 0
        for xi, yi, idx in qlist:
            while p < n and points[p][0] >= xi:
                x_val, y_val = points[p]
                pos = bisect_left(comp, y_val)
                update(pos, x_val + y_val)
                p += 1
            l = bisect_left(comp, yi)
            if l < m:
                res = query(l, m)
                ans[idx] = res if res != -1 else -1
            else:
                ans[idx] = -1
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int x;
    int y;
    long long sum;
} Point;

typedef struct {
    int xi;
    int yi;
    int idx;
} Query;

/* binary search lower bound */
static int lower_bound(int *arr, int n, int target) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] < target) l = m + 1;
        else r = m;
    }
    return l;
}

/* BIT for prefix maximum */
typedef struct {
    int n;
    long long *tree;
} BIT;

static BIT* bit_create(int n) {
    BIT *b = (BIT*)malloc(sizeof(BIT));
    b->n = n;
    b->tree = (long long*)malloc((n + 2) * sizeof(long long));
    for (int i = 0; i <= n + 1; ++i) b->tree[i] = LLONG_MIN;
    return b;
}

static void bit_update(BIT *b, int idx, long long val) {
    while (idx <= b->n) {
        if (val > b->tree[idx]) b->tree[idx] = val;
        idx += idx & -idx;
    }
}

static long long bit_query(BIT *b, int idx) {
    long long res = LLONG_MIN;
    while (idx > 0) {
        if (b->tree[idx] > res) res = b->tree[idx];
        idx -= idx & -idx;
    }
    return res;
}

/* comparators for qsort */
static int cmp_point_desc(const void *a, const void *b) {
    const Point *pa = (const Point*)a;
    const Point *pb = (const Point*)b;
    if (pa->x != pb->x) return pb->x - pa->x;
    return pb->y - pa->y;
}

static int cmp_query_desc(const void *a, const void *b) {
    const Query *qa = (const Query*)a;
    const Query *qb = (const Query*)b;
    if (qa->xi != qb->xi) return qb->xi - qa->xi;
    return qb->yi - qa->yi;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumSumQueries(int* nums1, int nums1Size, int* nums2, int nums2Size,
                       int** queries, int queriesSize, int* queriesColSize,
                       int* returnSize) {
    int n = nums1Size;
    int q = queriesSize;

    /* collect points */
    Point *pts = (Point*)malloc(n * sizeof(Point));
    for (int i = 0; i < n; ++i) {
        pts[i].x = nums1[i];
        pts[i].y = nums2[i];
        pts[i].sum = (long long)nums1[i] + (long long)nums2[i];
    }
    qsort(pts, n, sizeof(Point), cmp_point_desc);

    /* collect queries */
    Query *qs = (Query*)malloc(q * sizeof(Query));
    for (int i = 0; i < q; ++i) {
        qs[i].xi = queries[i][0];
        qs[i].yi = queries[i][1];
        qs[i].idx = i;
    }
    qsort(qs, q, sizeof(Query), cmp_query_desc);

    /* coordinate compression for nums2 and query yi */
    int totalVals = n + q;
    int *vals = (int*)malloc(totalVals * sizeof(int));
    int pos = 0;
    for (int i = 0; i < n; ++i) vals[pos++] = nums2[i];
    for (int i = 0; i < q; ++i) vals[pos++] = queries[i][1];
    /* sort and dedup */
    qsort(vals, totalVals, sizeof(int), cmp_point_desc); // reuse comparator descending
    int m = 0;
    for (int i = 0; i < totalVals; ++i) {
        if (i == 0 || vals[i] != vals[i-1]) {
            vals[m++] = vals[i];
        }
    }
    /* now vals[0..m-1] is descending order, but we need ascending for lower_bound */
    /* reverse to ascending */
    for (int i = 0; i < m/2; ++i) {
        int tmp = vals[i];
        vals[i] = vals[m-1-i];
        vals[m-1-i] = tmp;
    }

    BIT *bit = bit_create(m);

    int *ans = (int*)malloc(q * sizeof(int));
    for (int i = 0; i < q; ++i) ans[i] = -1;

    int pIdx = 0;
    for (int i = 0; i < q; ++i) {
        Query cur = qs[i];
        while (pIdx < n && pts[pIdx].x >= cur.xi) {
            int yPos = lower_bound(vals, m, pts[pIdx].y); // ascending
            int revIdx = m - yPos;
            bit_update(bit, revIdx, pts[pIdx].sum);
            ++pIdx;
        }
        int qPos = lower_bound(vals, m, cur.yi);
        if (qPos == m) {
            ans[cur.idx] = -1;
        } else {
            int revIdx = m - qPos;
            long long best = bit_query(bit, revIdx);
            if (best == LLONG_MIN) ans[cur.idx] = -1;
            else ans[cur.idx] = (int)best;
        }
    }

    *returnSize = q;

    free(pts);
    free(qs);
    free(vals);
    free(bit->tree);
    free(bit);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    private class BIT
    {
        private readonly long[] tree;
        private readonly int n;
        private const long NEG = long.MinValue / 4;

        public BIT(int size)
        {
            n = size;
            tree = new long[n + 2];
            for (int i = 0; i < tree.Length; i++) tree[i] = NEG;
        }

        public void Update(int idx, long val)
        {
            while (idx <= n)
            {
                if (val > tree[idx]) tree[idx] = val;
                idx += idx & -idx;
            }
        }

        public long Query(int idx)
        {
            long res = NEG;
            while (idx > 0)
            {
                if (tree[idx] > res) res = tree[idx];
                idx -= idx & -idx;
            }
            return res;
        }
    }

    private struct Query
    {
        public int x;
        public int y;
        public int idx;
    }

    private static int LowerBound(int[] arr, int target)
    {
        int l = 0, r = arr.Length;
        while (l < r)
        {
            int m = (l + r) >> 1;
            if (arr[m] >= target) r = m;
            else l = m + 1;
        }
        return l; // may be arr.Length
    }

    public int[] MaximumSumQueries(int[] nums1, int[] nums2, int[][] queries)
    {
        int n = nums1.Length;
        var points = new (int x, int y, long sum)[n];
        for (int i = 0; i < n; i++)
            points[i] = (nums1[i], nums2[i], (long)nums1[i] + nums2[i]);
        Array.Sort(points, (a, b) => b.x.CompareTo(a.x)); // descending by x

        int q = queries.Length;
        var qs = new Query[q];
        for (int i = 0; i < q; i++)
            qs[i] = new Query { x = queries[i][0], y = queries[i][1], idx = i };
        Array.Sort(qs, (a, b) => b.x.CompareTo(a.x)); // descending by xi

        var allY = new List<int>(n + q);
        foreach (var p in points) allY.Add(p.y);
        foreach (var qu in qs) allY.Add(qu.y);
        int[] uniq = allY.Distinct().OrderBy(v => v).ToArray();
        int m = uniq.Length;
        var dict = new Dictionary<int, int>(m * 2);
        for (int i = 0; i < m; i++) dict[uniq[i]] = i + 1; // 1‑based index

        var bit = new BIT(m);
        const long NEG = long.MinValue / 4;

        int pIdx = 0;
        long[] ansLong = new long[q];

        foreach (var query in qs)
        {
            while (pIdx < n && points[pIdx].x >= query.x)
            {
                int yVal = points[pIdx].y;
                int idx = dict[yVal];
                int revIdx = m - idx + 1;
                bit.Update(revIdx, points[pIdx].sum);
                pIdx++;
            }

            int targetPos = LowerBound(uniq, query.y); // first index with y >= query.y
            if (targetPos == m)
            {
                ansLong[query.idx] = -1;
            }
            else
            {
                int revQueryIdx = m - (targetPos + 1) + 1; // convert to reversed prefix index
                long res = bit.Query(revQueryIdx);
                ansLong[query.idx] = res == NEG ? -1 : res;
            }
        }

        var result = new int[q];
        for (int i = 0; i < q; i++) result[i] = (int)ansLong[i];
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[][]} queries
 * @return {number[]}
 */
var maximumSumQueries = function(nums1, nums2, queries) {
    const n = nums1.length;
    // points with x, y, sum
    const points = new Array(n);
    for (let i = 0; i < n; ++i) {
        points[i] = {x: nums1[i], y: nums2[i], sum: nums1[i] + nums2[i]};
    }
    // sort points by x descending
    points.sort((a, b) => b.x - a.x);
    
    const qlen = queries.length;
    const qs = new Array(qlen);
    for (let i = 0; i < qlen; ++i) {
        qs[i] = {x: queries[i][0], y: queries[i][1], idx: i};
    }
    // sort queries by x descending
    qs.sort((a, b) => b.x - a.x);
    
    // coordinate compression for all y values (nums2 and query yi)
    const allY = [];
    for (let v of nums2) allY.push(v);
    for (let q of queries) allY.push(q[1]);
    allY.sort((a, b) => a - b);
    const uniqY = [];
    let prev = null;
    for (let v of allY) {
        if (v !== prev) {
            uniqY.push(v);
            prev = v;
        }
    }
    const m = uniqY.length;
    
    // segment tree for range maximum
    let size = 1;
    while (size < m) size <<= 1;
    const seg = new Array(size * 2).fill(Number.NEGATIVE_INFINITY);
    
    function lowerBound(arr, target) {
        let l = 0, r = arr.length;
        while (l < r) {
            const mid = (l + r) >> 1;
            if (arr[mid] < target) l = mid + 1;
            else r = mid;
        }
        return l;
    }
    
    function update(pos, val) {
        let idx = pos + size;
        if (seg[idx] >= val) return; // no need to update
        seg[idx] = Math.max(seg[idx], val);
        idx >>= 1;
        while (idx > 0) {
            const newVal = Math.max(seg[idx << 1], seg[(idx << 1) | 1]);
            if (seg[idx] === newVal) break;
            seg[idx] = newVal;
            idx >>= 1;
        }
    }
    
    function query(l, r) { // inclusive
        let res = Number.NEGATIVE_INFINITY;
        l += size;
        r += size;
        while (l <= r) {
            if ((l & 1) === 1) {
                res = Math.max(res, seg[l]);
                l++;
            }
            if ((r & 1) === 0) {
                res = Math.max(res, seg[r]);
                r--;
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    }
    
    const ans = new Array(qlen);
    let p = 0;
    for (const q of qs) {
        while (p < n && points[p].x >= q.x) {
            const yIdx = lowerBound(uniqY, points[p].y);
            update(yIdx, points[p].sum);
            ++p;
        }
        const startIdx = lowerBound(uniqY, q.y);
        if (startIdx === m) {
            ans[q.idx] = -1;
        } else {
            const best = query(startIdx, m - 1);
            ans[q.idx] = best === Number.NEGATIVE_INFINITY ? -1 : best;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maximumSumQueries(nums1: number[], nums2: number[], queries: number[][]): number[] {
    const n = nums1.length;
    const points: { x: number; y: number; sum: number }[] = [];
    for (let i = 0; i < n; i++) {
        points.push({ x: nums1[i], y: nums2[i], sum: nums1[i] + nums2[i] });
    }
    points.sort((a, b) => b.x - a.x); // descending by nums1

    const qlen = queries.length;
    const qs: { xi: number; yi: number; idx: number }[] = new Array(qlen);
    for (let i = 0; i < qlen; i++) {
        qs[i] = { xi: queries[i][0], yi: queries[i][1], idx: i };
    }
    qs.sort((a, b) => b.xi - a.xi); // descending by query xi

    // compress nums2 values from points
    const uniqY = Array.from(new Set(points.map(p => p.y))).sort((a, b) => a - b);
    const m = uniqY.length;
    const yToIdx = new Map<number, number>();
    for (let i = 0; i < m; i++) yToIdx.set(uniqY[i], i);

    class SegTree {
        size: number;
        data: number[];
        constructor(n: number) {
            this.size = 1;
            while (this.size < n) this.size <<= 1;
            this.data = new Array(this.size * 2).fill(-1);
        }
        update(pos: number, val: number): void {
            let i = pos + this.size;
            if (val <= this.data[i]) return;
            this.data[i] = val;
            i >>= 1;
            while (i) {
                const left = this.data[i << 1];
                const right = this.data[(i << 1) | 1];
                const best = left > right ? left : right;
                if (this.data[i] === best) break;
                this.data[i] = best;
                i >>= 1;
            }
        }
        query(l: number, r: number): number { // inclusive
            let res = -1;
            l += this.size;
            r += this.size;
            while (l <= r) {
                if ((l & 1) === 1) {
                    if (this.data[l] > res) res = this.data[l];
                    l++;
                }
                if ((r & 1) === 0) {
                    if (this.data[r] > res) res = this.data[r];
                    r--;
                }
                l >>= 1;
                r >>= 1;
            }
            return res;
        }
    }

    const seg = new SegTree(m);
    const ans = new Array(qlen).fill(-1);
    let pIdx = 0;

    for (const q of qs) {
        while (pIdx < n && points[pIdx].x >= q.xi) {
            const pos = yToIdx.get(points[pIdx].y)!;
            seg.update(pos, points[pIdx].sum);
            pIdx++;
        }
        // binary search first y >= yi
        let lo = 0, hi = m - 1, start = m;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (uniqY[mid] >= q.yi) {
                start = mid;
                hi = mid - 1;
            } else lo = mid + 1;
        }
        if (start === m) {
            ans[q.idx] = -1;
        } else {
            const res = seg.query(start, m - 1);
            ans[q.idx] = res;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maximumSumQueries($nums1, $nums2, $queries) {
        $n = count($nums1);
        // points with x, y, sum
        $points = [];
        for ($i = 0; $i < $n; ++$i) {
            $points[] = ['x' => $nums1[$i], 'y' => $nums2[$i], 'sum' => $nums1[$i] + $nums2[$i]];
        }
        usort($points, function($a, $b) {
            return $b['x'] <=> $a['x']; // descending by x
        });
        
        // prepare queries with original index
        $q = count($queries);
        $qs = [];
        for ($i = 0; $i < $q; ++$i) {
            $qs[] = ['xi' => $queries[$i][0], 'yi' => $queries[$i][1], 'idx' => $i];
        }
        usort($qs, function($a, $b) {
            return $b['xi'] <=> $a['xi']; // descending by xi
        });
        
        // coordinate compression for y values (nums2 and query yi)
        $allY = array_merge($nums2, array_column($queries, 1));
        sort($allY);
        $uniqueY = [];
        $prev = null;
        foreach ($allY as $v) {
            if ($v !== $prev) {
                $uniqueY[] = $v;
                $prev = $v;
            }
        }
        $m = count($uniqueY);
        
        // BIT for prefix maximum (we will use reversed index to query suffix)
        $bit = new class($m) {
            private $size;
            private $tree;
            public function __construct($n) {
                $this->size = $n;
                $this->tree = array_fill(0, $n + 2, 0);
            }
            public function update($idx, $val) {
                for ($i = $idx; $i <= $this->size; $i += $i & (-$i)) {
                    if ($val > $this->tree[$i]) $this->tree[$i] = $val;
                }
            }
            public function query($idx) {
                $res = 0;
                for ($i = $idx; $i > 0; $i -= $i & (-$i)) {
                    if ($this->tree[$i] > $res) $res = $this->tree[$i];
                }
                return $res;
            }
        };
        
        // helper lower bound
        $lowerBound = function($arr, $target) {
            $l = 0; $r = count($arr);
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($arr[$mid] < $target) $l = $mid + 1;
                else $r = $mid;
            }
            return $l; // may be count
        };
        
        $ans = array_fill(0, $q, -1);
        $pIdx = 0;
        foreach ($qs as $query) {
            $xi = $query['xi'];
            $yi = $query['yi'];
            // insert all points with x >= xi
            while ($pIdx < $n && $points[$pIdx]['x'] >= $xi) {
                $y = $points[$pIdx]['y'];
                $sum = $points[$pIdx]['sum'];
                $pos = $lowerBound($uniqueY, $y); // 0‑based
                // reversed index for suffix query
                $revIdx = $m - $pos;
                $bit->update($revIdx, $sum);
                ++$pIdx;
            }
            // answer query
            $posQ = $lowerBound($uniqueY, $yi);
            if ($posQ < $m) {
                $revIdxQ = $m - $posQ;
                $res = $bit->query($revIdxQ);
                if ($res > 0) $ans[$query['idx']] = $res;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSumQueries(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums1.count
        var points: [(x: Int, y: Int, sum: Int)] = []
        points.reserveCapacity(n)
        for i in 0..<n {
            points.append((nums1[i], nums2[i], nums1[i] + nums2[i]))
        }
        points.sort { $0.x > $1.x }   // descending by x
        
        var queryList: [(x: Int, y: Int, idx: Int)] = []
        queryList.reserveCapacity(queries.count)
        for (i, q) in queries.enumerated() {
            queryList.append((q[0], q[1], i))
        }
        queryList.sort { $0.x > $1.x }   // descending by x
        
        // coordinate compression of nums2 values
        var uniqY = nums2.sorted()
        var compressed: [Int] = []
        for v in uniqY {
            if compressed.isEmpty || compressed.last! != v {
                compressed.append(v)
            }
        }
        let m = compressed.count
        
        func lowerBound(_ arr: [Int], _ target: Int) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let mid = (l + r) >> 1
                if arr[mid] < target {
                    l = mid + 1
                } else {
                    r = mid
                }
            }
            return l
        }
        
        // Fenwick tree for prefix maximum
        final class BIT {
            var n: Int
            var tree: [Int]
            init(_ n: Int) {
                self.n = n
                self.tree = Array(repeating: Int.min, count: n + 2)
            }
            func update(_ index: Int, _ value: Int) {
                var i = index
                while i <= n {
                    if value > tree[i] { tree[i] = value }
                    i += i & -i
                }
            }
            func query(_ index: Int) -> Int {
                var res = Int.min
                var i = index
                while i > 0 {
                    if tree[i] > res { res = tree[i] }
                    i -= i & -i
                }
                return res
            }
        }
        
        let bit = BIT(m)
        var answers = Array(repeating: -1, count: queries.count)
        var pIdx = 0
        
        for q in queryList {
            while pIdx < n && points[pIdx].x >= q.x {
                let pt = points[pIdx]
                let pos = lowerBound(compressed, pt.y)          // 0‑based
                let rev = m - pos                               // 1‑based index for BIT prefix
                bit.update(rev, pt.sum)
                pIdx += 1
            }
            let posQ = lowerBound(compressed, q.y)
            if posQ == m {
                answers[q.idx] = -1
            } else {
                let revQ = m - posQ
                let res = bit.query(revQ)
                answers[q.idx] = (res == Int.min) ? -1 : res
            }
        }
        return answers
    }
}
```

## Kotlin

```kotlin
import java.util.*
 
class Solution {
    data class Point(val x: Int, val yIdx: Int, val sum: Int)
    data class Query(val x: Int, val y: Int, val idx: Int)
 
    private fun lowerBound(arr: List<Int>, target: Int): Int {
        var l = 0
        var r = arr.size
        while (l < r) {
            val m = (l + r) ushr 1
            if (arr[m] < target) l = m + 1 else r = m
        }
        return l
    }
 
    private class SegTree(n: Int) {
        private var size = 1
        init { while (size < n) size = size shl 1 }
        private val tree = IntArray(size * 2) { Int.MIN_VALUE }
 
        fun update(pos: Int, value: Int) {
            var p = pos + size
            if (value <= tree[p]) return
            tree[p] = value
            p = p shr 1
            while (p > 0) {
                val newVal = kotlin.math.max(tree[p shl 1], tree[(p shl 1) + 1])
                if (newVal == tree[p]) break
                tree[p] = newVal
                p = p shr 1
            }
        }
 
        fun query(l: Int, r: Int): Int {
            var left = l + size
            var right = r + size
            var res = Int.MIN_VALUE
            while (left <= right) {
                if ((left and 1) == 1) {
                    res = kotlin.math.max(res, tree[left])
                    left++
                }
                if ((right and 1) == 0) {
                    res = kotlin.math.max(res, tree[right])
                    right--
                }
                left = left shr 1
                right = right shr 1
            }
            return res
        }
    }
 
    fun maximumSumQueries(nums1: IntArray, nums2: IntArray, queries: Array<IntArray>): IntArray {
        val n = nums1.size
        val allYs = mutableListOf<Int>()
        for (v in nums2) allYs.add(v)
        for (q in queries) allYs.add(q[1])
        val sortedYs = allYs.distinct().sorted()
        val m = sortedYs.size
 
        val points = ArrayList<Point>(n)
        for (i in 0 until n) {
            val yIdx = lowerBound(sortedYs, nums2[i])
            points.add(Point(nums1[i], yIdx, nums1[i] + nums2[i]))
        }
        points.sortWith { a, b -> b.x - a.x } // descending by x
 
        val qList = ArrayList<Query>(queries.size)
        for (i in queries.indices) {
            val arr = queries[i]
            qList.add(Query(arr[0], arr[1], i))
        }
        qList.sortWith { a, b -> b.x - a.x } // descending by x
 
        val seg = SegTree(m)
        val ans = IntArray(queries.size) { -1 }
        var pIdx = 0
        for (q in qList) {
            while (pIdx < points.size && points[pIdx].x >= q.x) {
                val pt = points[pIdx]
                seg.update(pt.yIdx, pt.sum)
                pIdx++
            }
            val start = lowerBound(sortedYs, q.y)
            if (start == m) {
                ans[q.idx] = -1
            } else {
                val best = seg.query(start, m - 1)
                ans[q.idx] = if (best == Int.MIN_VALUE) -1 else best
            }
        }
        return ans
    }
}
```

## Dart

```dart
class SegTree {
  int _size;
  List<int> _tree;

  SegTree(int n) {
    _size = 1;
    while (_size < n) _size <<= 1;
    _tree = List.filled(_size << 1, -1);
  }

  void update(int pos, int value) {
    int idx = pos + _size;
    if (value <= _tree[idx]) return;
    _tree[idx] = value;
    idx >>= 1;
    while (idx > 0) {
      int newVal = _tree[idx << 1] > _tree[(idx << 1) | 1]
          ? _tree[idx << 1]
          : _tree[(idx << 1) | 1];
      if (newVal == _tree[idx]) break;
      _tree[idx] = newVal;
      idx >>= 1;
    }
  }

  int query(int l, int r) {
    int res = -1;
    int left = l + _size;
    int right = r + _size;
    while (left <= right) {
      if ((left & 1) == 1) {
        if (_tree[left] > res) res = _tree[left];
        left++;
      }
      if ((right & 1) == 0) {
        if (_tree[right] > res) res = _tree[right];
        right--;
      }
      left >>= 1;
      right >>= 1;
    }
    return res;
  }
}

int lowerBound(List<int> arr, int target) {
  int l = 0, r = arr.length;
  while (l < r) {
    int m = (l + r) >> 1;
    if (arr[m] < target)
      l = m + 1;
    else
      r = m;
  }
  return l;
}

class Solution {
  List<int> maximumSumQueries(
      List<int> nums1, List<int> nums2, List<List<int>> queries) {
    int n = nums1.length;

    // indices sorted by nums1 descending
    List<int> idxs = List.generate(n, (i) => i);
    idxs.sort((a, b) => nums2[b].compareTo(nums2[a])); // placeholder
    idxs.sort((a, b) => nums1[b].compareTo(nums1[a]));

    // compress nums2 values from points
    List<int> allY = List.from(nums2);
    allY.sort();
    allY = allY.toSet().toList()..sort();

    SegTree seg = SegTree(allY.length);

    // prepare queries with original index
    int qn = queries.length;
    List<_Query> qs = List.generate(qn, (i) {
      return _Query(queries[i][0], queries[i][1], i);
    });
    qs.sort((a, b) => b.x.compareTo(a.x)); // descending x

    List<int> ans = List.filled(qn, -1);
    int p = 0;
    for (var q in qs) {
      while (p < n && nums1[idxs[p]] >= q.x) {
        int i = idxs[p];
        int y = nums2[i];
        int pos = lowerBound(allY, y); // exact position
        seg.update(pos, nums1[i] + nums2[i]);
        p++;
      }
      int start = lowerBound(allY, q.y);
      if (start < allY.length) {
        ans[q.id] = seg.query(start, allY.length - 1);
      } else {
        ans[q.id] = -1;
      }
    }

    return ans;
  }
}

class _Query {
  int x;
  int y;
  int id;
  _Query(this.x, this.y, this.id);
}
```

## Golang

```go
package main

import (
	"sort"
)

type point struct {
	x   int
	y   int
	sum int
}

type query struct {
	x   int
	y   int
	idx int
}

// monotone map: y ascending, values strictly decreasing
type monoMap struct {
	ys   []int
	vals []int
}

func (m *monoMap) add(y, v int) {
	i := sort.Search(len(m.ys), func(i int) bool { return m.ys[i] >= y })
	if i < len(m.ys) && m.ys[i] == y {
		if m.vals[i] >= v {
			return
		}
		m.vals[i] = v
	} else {
		m.ys = append(m.ys, 0)
		m.vals = append(m.vals, 0)
		copy(m.ys[i+1:], m.ys[i:])
		copy(m.vals[i+1:], m.vals[i:])
		m.ys[i] = y
		m.vals[i] = v
	}
	// remove dominated entries on the left
	for i > 0 && m.vals[i-1] <= m.vals[i] {
		m.ys = append(m.ys[:i-1], m.ys[i:]...)
		m.vals = append(m.vals[:i-1], m.vals[i:]...)
		i--
	}
	// remove dominated entries on the right
	for i+1 < len(m.ys) && m.vals[i+1] <= m.vals[i] {
		m.ys = append(m.ys[:i+1], m.ys[i+2:]...)
		m.vals = append(m.vals[:i+1], m.vals[i+2:]...)
	}
}

func (m *monoMap) query(y int) int {
	i := sort.Search(len(m.ys), func(i int) bool { return m.ys[i] >= y })
	if i == len(m.ys) {
		return -1
	}
	return m.vals[i]
}

func maximumSumQueries(nums1 []int, nums2 []int, queries [][]int) []int {
	n := len(nums1)
	points := make([]point, n)
	for i := 0; i < n; i++ {
		points[i] = point{x: nums1[i], y: nums2[i], sum: nums1[i] + nums2[i]}
	}
	sort.Slice(points, func(i, j int) bool { return points[i].x > points[j].x })

	q := len(queries)
	qry := make([]query, q)
	for i := 0; i < q; i++ {
		qry[i] = query{x: queries[i][0], y: queries[i][1], idx: i}
	}
	sort.Slice(qry, func(i, j int) bool { return qry[i].x > qry[j].x })

	ans := make([]int, q)
	m := &monoMap{}
	pIdx := 0
	for _, qu := range qry {
		for pIdx < n && points[pIdx].x >= qu.x {
			m.add(points[pIdx].y, points[pIdx].sum)
			pIdx++
		}
		ans[qu.idx] = m.query(qu.y)
	}
	return ans
}
```

## Ruby

```ruby
class BIT
  def initialize(n)
    @n = n
    @tree = Array.new(n + 2, -1)
  end

  def update(i, val)
    while i <= @n
      @tree[i] = val if val > @tree[i]
      i += i & -i
    end
  end

  def query(i)
    res = -1
    while i > 0
      res = @tree[i] if @tree[i] > res
      i -= i & -i
    end
    res
  end
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_sum_queries(nums1, nums2, queries)
  n = nums1.length
  points = []
  n.times do |i|
    points << [nums1[i], nums2[i], nums1[i] + nums2[i]]
  end
  points.sort_by! { |p| -p[0] } # descending by nums1

  q_with_idx = queries.each_with_index.map { |(x, y), idx| [x, y, idx] }
  q_with_idx.sort_by! { |q| -q[0] }

  all_ys = nums2 + queries.map { |q| q[1] }
  sorted_ys = all_ys.uniq.sort
  rank = {}
  sorted_ys.each_with_index { |v, i| rank[v] = i }
  m = sorted_ys.length

  bit = BIT.new(m)
  ans = Array.new(queries.length, -1)

  p_idx = 0
  points_len = points.length

  q_with_idx.each do |x, y, idx|
    while p_idx < points_len && points[p_idx][0] >= x
      py = points[p_idx][1]
      sum = points[p_idx][2]
      r = rank[py]
      rev = m - r
      bit.update(rev, sum)
      p_idx += 1
    end

    # lower_bound for y in sorted_ys
    lo = 0
    hi = m
    while lo < hi
      mid = (lo + hi) / 2
      if sorted_ys[mid] < y
        lo = mid + 1
      else
        hi = mid
      end
    end

    if lo == m
      ans[idx] = -1
    else
      rev = m - lo
      res = bit.query(rev)
      ans[idx] = res
    end
  end

  ans
end
```

## Scala

```scala
import java.util.TreeMap

object Solution {
  def maximumSumQueries(nums1: Array[Int], nums2: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums1.length
    case class Point(x: Int, y: Int, sum: Int)
    val points = (0 until n).map(i => Point(nums1(i), nums2(i), nums1(i) + nums2(i)))
      .sortBy(p => -p.x)

    val qWithIdx = queries.zipWithIndex.map { case (arr, idx) =>
      (arr(0), arr(1), idx)
    }.sortBy(q => -q._1)

    val map = new TreeMap[Integer, Integer]()
    val ans = Array.fill[Int](queries.length)(-1)
    var pIdx = 0

    for ((qx, qy, qIdx) <- qWithIdx) {
      while (pIdx < points.length && points(pIdx).x >= qx) {
        val pt = points(pIdx)
        val higher = map.ceilingEntry(pt.y)
        if (higher == null || higher.getValue < pt.sum) {
          var lower = map.lowerEntry(pt.y)
          while (lower != null && lower.getValue <= pt.sum) {
            map.remove(lower.getKey)
            lower = map.lowerEntry(pt.y)
          }
          map.put(pt.y, pt.sum)
        }
        pIdx += 1
      }
      val entry = map.ceilingEntry(qy)
      if (entry != null) ans(qIdx) = entry.getValue else ans(qIdx) = -1
    }

    ans
  }
}
```

## Rust

```rust
use std::cmp::max;

struct Fenwick {
    n: usize,
    bit: Vec<i64>,
}
impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { n, bit: vec![i64::MIN; n + 2] }
    }
    fn update(&mut self, mut idx: usize, val: i64) {
        while idx <= self.n {
            if self.bit[idx] < val {
                self.bit[idx] = val;
            }
            idx += idx & (!idx + 1);
        }
    }
    fn query(&self, mut idx: usize) -> i64 {
        let mut res = i64::MIN;
        while idx > 0 {
            if self.bit[idx] > res {
                res = self.bit[idx];
            }
            idx &= idx - 1;
        }
        res
    }
}

pub struct Solution;

impl Solution {
    pub fn maximum_sum_queries(nums1: Vec<i32>, nums2: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums1.len();
        // collect unique sorted ys from nums2
        let mut uniq_y = nums2.clone();
        uniq_y.sort_unstable();
        uniq_y.dedup();
        let m = uniq_y.len();

        // points with (x, y_idx, sum)
        #[derive(Clone)]
        struct Point {
            x: i32,
            y_idx: usize,
            sum: i64,
        }
        let mut points: Vec<Point> = Vec::with_capacity(n);
        for i in 0..n {
            let y = nums2[i];
            let y_idx = uniq_y.binary_search(&y).unwrap();
            let sum = nums1[i] as i64 + nums2[i] as i64;
            points.push(Point { x: nums1[i], y_idx, sum });
        }
        // sort points by x descending
        points.sort_by(|a, b| b.x.cmp(&a.x));

        // queries with original index
        #[derive(Clone)]
        struct Query {
            xi: i32,
            yi: i32,
            idx: usize,
        }
        let q = queries.len();
        let mut qs: Vec<Query> = Vec::with_capacity(q);
        for (i, qu) in queries.iter().enumerate() {
            qs.push(Query { xi: qu[0], yi: qu[1], idx: i });
        }
        // sort queries by xi descending
        qs.sort_by(|a, b| b.xi.cmp(&a.xi));

        let mut fenwick = Fenwick::new(m);
        let mut ans = vec![-1i32; q];
        let mut p = 0usize;

        for query in qs.iter() {
            // add all points with x >= xi
            while p < points.len() && points[p].x >= query.xi {
                let y_idx = points[p].y_idx;
                // reversed index: larger original y -> smaller rev idx (1-based)
                let rev_idx = m - y_idx; // 0..m-1 => 1..m
                fenwick.update(rev_idx, points[p].sum);
                p += 1;
            }
            // find first y >= yi in uniq_y
            let pos = match uniq_y.binary_search(&query.yi) {
                Ok(v) => v,
                Err(v) => v,
            };
            if pos == m {
                ans[query.idx] = -1;
            } else {
                let rev_limit = m - pos; // prefix length in reversed order
                let res = fenwick.query(rev_limit);
                if res == i64::MIN {
                    ans[query.idx] = -1;
                } else {
                    ans[query.idx] = res as i32;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/vector)

(define (maximum-sum-queries nums1 nums2 queries)
  (let* ((n (length nums1))
         ;; points: list of (x y sum)
         (points
          (for/list ([i (in-range n)])
            (list (list-ref nums1 i)
                  (list-ref nums2 i)
                  (+ (list-ref nums1 i) (list-ref nums2 i)))))
         (sorted-points
          (sort points > #:key (lambda (p) (first p)))) ; descending by x
         (points-vec (list->vector sorted-points))
         (total-points (vector-length points-vec))

         (q (length queries))
         ;; queries with original index
         (queries-with-idx
          (for/list ([i (in-range q)])
            (let* ((pair (list-ref queries i))
                   (xi (first pair))
                   (yi (second pair)))
              (list xi yi i))))
         (sorted-queries
          (sort queries-with-idx > #:key (lambda (qq) (first qq)))) ; descending by xi

         ;; coordinate compression of all y values
         (all-ys (append nums2 (map second queries)))
         (uniq-ys (remove-duplicates (sort all-ys <)))
         (m (length uniq-ys))
         (ys-vec (list->vector uniq-ys))

         ;; Fenwick tree for maximum, 1‑based indexing
         (tree (make-vector (+ m 1) -1000000000000))

         ;; binary search: first index >= target in ys-vec (0‑based)
         (lower-bound
          (lambda (target)
            (let loop ((l 0) (r m))
              (if (= l r)
                  l
                  (let* ((mid (quotient (+ l r) 2))
                         (val (vector-ref ys-vec mid)))
                    (if (< val target)
                        (loop (+ mid 1) r)
                        (loop l mid)))))))

         ;; Fenwick update: set max at idx
         (update
          (lambda (idx val)
            (let loop ((i idx))
              (when (<= i m)
                (when (< (vector-ref tree i) val)
                  (vector-set! tree i val))
                (loop (+ i (bitwise-and (- i) i)))))))

         ;; Fenwick query: max over prefix [1..idx]
         (query
          (lambda (idx)
            (let loop ((i idx) (res -1000000000000))
              (if (= i 0)
                  res
                  (loop (bitwise-and i (- i)) (max res (vector-ref tree i)))))))

         (answers (make-vector q -1)))
    ;; process queries
    (let loop-queries ((qs sorted-queries) (pt-index 0))
      (if (null? qs)
          (vector->list answers)
          (let* ((qitem (car qs))
                 (xi (first qitem))
                 (yi (second qitem))
                 (orig-idx (third qitem)))

            ;; insert all points with x >= xi
            (define new-pt-index
              (let loop-points ((pi pt-index))
                (if (or (= pi total-points)
                        (< (first (vector-ref points-vec pi)) xi))
                    pi
                    (begin
                      (define point (vector-ref points-vec pi))
                      (define y (second point))
                      (define s (third point))
                      (define idx (+ 1 (lower-bound y)))          ; 1‑based index of exact y
                      (define rev-idx (- m idx + 1))              ; reversed for suffix query
                      (update rev-idx s)
                      (loop-points (+ pi 1))))))

            ;; answer current query
            (let* ((pos (lower-bound yi))                     ; first y >= yi, 0‑based
                   (ans
                    (if (= pos m)
                        -1
                        (let ((rev (- m pos)))               ; reversed index for suffix
                          (let ((res (query rev)))
                            (if (< res -500000000000) -1 res))))))
              (vector-set! answers orig-idx ans))

            ;; continue with next query
            (loop-queries (cdr qs) new-pt-index))))))
```

## Erlang

```erlang
-spec maximum_sum_queries(Nums1 :: [integer()], Nums2 :: [integer()], Queries :: [[integer()]]) -> [integer()].
maximum_sum_queries(Nums1, Nums2, Queries) ->
    Points = build_points(Nums1, Nums2),
    SortedPoints = lists:sort(fun({A,_,_},{B,_,_}) -> A > B end, Points),

    IndexedQueries = build_indexed_queries(Queries, 1, []),
    SortedQueries = lists:sort(fun({A,_,_},{B,_,_}) -> A > B end, IndexedQueries),

    UniqueYs = lists:usort(Nums2),
    YArr = array:from_list(UniqueYs),
    SizeY = length(UniqueYs),

    Tree0 = init_bit(SizeY, 0),

    AnswersMap = process_queries(SortedQueries, SortedPoints, YArr, SizeY, Tree0, #{}),

    [maps:get(I, AnswersMap, -1) || I <- lists:seq(1, length(Queries))].

%% Build list of points {Num1, Num2, Sum}
build_points([], [], Acc) -> lists:reverse(Acc);
build_points([A|As], [B|Bs], Acc) ->
    build_points(As, Bs, [{A,B,A+B}|Acc]).

%% Build indexed queries [{X,Y,Idx}]
build_indexed_queries([], _Idx, Acc) -> lists:reverse(Acc);
build_indexed_queries([[X,Y]|Rest], Idx, Acc) ->
    build_indexed_queries(Rest, Idx+1, [{X,Y,Idx}|Acc]).

%% Initialize BIT array with default value
init_bit(Size, InitVal) ->
    array:new(Size + 2, {default, InitVal}).

%% Process all queries recursively
process_queries([], _Points, _YArr, _SizeY, _Tree, AccMap) -> AccMap;
process_queries([{X,Y,QIdx}|RestQ], Points, YArr, SizeY, Tree, AccMap) ->
    {NewTree, NewPoints} = insert_while(Points, X, YArr, SizeY, Tree),
    Idx = lower_bound(YArr, SizeY, Y),
    Ans =
        if
            Idx > SizeY -> -1;
            true ->
                RevIdx = SizeY - Idx + 1,
                MaxVal = bit_query(NewTree, RevIdx),
                case MaxVal of
                    0 -> -1;
                    _ -> MaxVal
                end
        end,
    NewAccMap = maps:put(QIdx, Ans, AccMap),
    process_queries(RestQ, NewPoints, YArr, SizeY, NewTree, NewAccMap).

%% Insert points while Num1 >= Threshold
insert_while(Points, XThresh, YArr, SizeY, Tree) ->
    case Points of
        [] -> {Tree, []};
        [{Num1, Num2, Sum}|Rest] when Num1 >= XThresh ->
            Pos = lower_bound(YArr, SizeY, Num2),
            RevPos = SizeY - Pos + 1,
            UpdatedTree = bit_update(Tree, RevPos, Sum, SizeY),
            insert_while(Rest, XThresh, YArr, SizeY, UpdatedTree);
        _ -> {Tree, Points}
    end.

%% BIT point update (max)
bit_update(Tree, Index, Value, Size) when Index =< Size ->
    Cur = array:get(Index, Tree),
    NewVal = if Cur < Value -> Value; true -> Cur end,
    Tree1 = array:set(Index, NewVal, Tree),
    Next = Index + (Index band -Index),
    bit_update(Tree1, Next, Value, Size);
bit_update(Tree, _Index, _Value, _Size) ->
    Tree.

%% BIT prefix max query
bit_query(_Tree, 0) -> 0;
bit_query(Tree, Index) when Index > 0 ->
    Cur = array:get(Index, Tree),
    Rest = bit_query(Tree, Index - (Index band -Index)),
    if Cur > Rest -> Cur; true -> Rest end.

%% Lower bound: first index (1‑based) with value >= Target
lower_bound(Arr, N, Target) -> lower_bound(1, N + 1, Arr, Target).

lower_bound(Low, High, _Arr, _Target) when Low >= High -> Low;
lower_bound(Low, High, Arr, Target) ->
    Mid = (Low + High) div 2,
    MidVal = array:get(Mid, Arr),
    if
        MidVal < Target -> lower_bound(Mid + 1, High, Arr, Target);
        true -> lower_bound(Low, Mid, Arr, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  defmodule BIT do
    defstruct tree: nil, n: 0

    def new(n) do
      %BIT{tree: :array.new(n + 2, 0), n: n}
    end

    def update(%BIT{tree: t, n: n} = bit, idx, val) when idx > 0 and idx <= n do
      new_tree = upd(t, idx, val, n)
      %BIT{bit | tree: new_tree}
    end

    defp upd(arr, i, val, n) do
      if i <= n do
        cur = :array.get(i, arr)
        new_val = if val > cur, do: val, else: cur
        arr2 = :array.set(i, new_val, arr)
        nxt = i + (i &&& -i)
        upd(arr2, nxt, val, n)
      else
        arr
      end
    end

    def query(%BIT{tree: t}, idx) when idx > 0 do
      q(t, idx, 0)
    end

    defp q(_arr, 0, acc), do: acc

    defp q(arr, i, acc) do
      cur = :array.get(i, arr)
      new_acc = if cur > acc, do: cur, else: acc
      nxt = i &&& (i - 1)
      q(arr, nxt, new_acc)
    end
  end

  @spec maximum_sum_queries(nums1 :: [integer], nums2 :: [integer], queries :: [[integer]]) :: [integer]
  def maximum_sum_queries(nums1, nums2, queries) do
    n = length(nums1)

    points =
      Enum.zip([nums1, nums2])
      |> Enum.map(fn {x, y} -> {x, y, x + y} end)
      |> Enum.sort_by(fn {x, _, _} -> -x end)

    q_with_idx =
      queries
      |> Enum.with_index()
      |> Enum.map(fn {{xi, yi}, idx} -> {xi, yi, idx} end)
      |> Enum.sort_by(fn {xi, _, _} -> -xi end)

    # coordinate compression for y values
    all_ys = nums2 ++ Enum.map(queries, fn [_, yi] -> yi end)
    uniq_sorted_ys = all_ys |> Enum.uniq() |> Enum.sort()
    m = length(uniq_sorted_ys)

    y_to_idx =
      uniq_sorted_ys
      |> Enum.with_index(1)
      |> Enum.into(%{}, fn {v, i} -> {v, i} end)

    bit = BIT.new(m)
    answers = :array.new(length(queries), 0)

    {_, final_bit, final_ans} = process_queries(points, q_with_idx, y_to_idx, m, bit, answers)

    # extract answers in original order
    0..(length(queries) - 1)
    |> Enum.map(fn i -> :array.get(i, final_ans) end)
  end

  defp process_queries([], [], _y_to_idx, _m, bit, ans), do: {[], bit, ans}

  defp process_queries(points, [{xi, yi, qidx} | rest_q], y_to_idx, m, bit, ans) do
    {remaining_points, updated_bit} = insert_points(points, xi, y_to_idx, m, bit)

    idx_y = Map.fetch!(y_to_idx, yi)
    rev_idx = m - idx_y + 1
    res = BIT.query(updated_bit, rev_idx)
    answer = if res == 0, do: -1, else: res

    new_ans = :array.set(qidx, answer, ans)

    process_queries(remaining_points, rest_q, y_to_idx, m, updated_bit, new_ans)
  end

  defp insert_points([], _xi, _y_to_idx, _m, bit), do: {[], bit}

  defp insert_points([{x, y, sum} = head | tail], xi, y_to_idx, m, bit) when x >= xi do
    idx_y = Map.fetch!(y_to_idx, y)
    rev_idx = m - idx_y + 1
    new_bit = BIT.update(bit, rev_idx, sum)
    insert_points(tail, xi, y_to_idx, m, new_bit)
  end

  defp insert_points(remaining, _xi, _y_to_idx, _m, bit), do: {remaining, bit}
end
```

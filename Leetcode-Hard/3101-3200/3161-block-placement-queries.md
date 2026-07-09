# 3161. Block Placement Queries

## Cpp

```cpp
class Solution {
public:
    struct SegTree {
        int n;
        vector<long long> mx, lz;
        SegTree(int _n = 0) { init(_n); }
        void init(int _n) {
            n = 1;
            while (n < _n) n <<= 1;
            mx.assign(2 * n, 0);
            lz.assign(2 * n, 0);
        }
        void build(const vector<long long>& a) {
            for (int i = 0; i < (int)a.size(); ++i) mx[n + i] = a[i];
            for (int i = n - 1; i > 0; --i) mx[i] = max(mx[i << 1], mx[i << 1 | 1]);
        }
        void apply(int p, long long v) {
            mx[p] += v;
            if (p < n) lz[p] += v;
        }
        void push(int p) {
            if (lz[p]) {
                apply(p << 1, lz[p]);
                apply(p << 1 | 1, lz[p]);
                lz[p] = 0;
            }
        }
        void rangeAdd(int l, int r, long long v) { rangeAdd(l, r, v, 1, 0, n - 1); }
        void rangeAdd(int l, int r, long long v, int p, int nl, int nr) {
            if (l > nr || r < nl) return;
            if (l <= nl && nr <= r) { apply(p, v); return; }
            push(p);
            int mid = (nl + nr) >> 1;
            rangeAdd(l, r, v, p << 1, nl, mid);
            rangeAdd(l, r, v, p << 1 | 1, mid + 1, nr);
            mx[p] = max(mx[p << 1], mx[p << 1 | 1]);
        }
        long long queryMax(int l, int r) { return queryMax(l, r, 1, 0, n - 1); }
        long long queryMax(int l, int r, int p, int nl, int nr) {
            if (l > nr || r < nl) return LLONG_MIN;
            if (l <= nl && nr <= r) return mx[p];
            push(p);
            int mid = (nl + nr) >> 1;
            return max(queryMax(l, r, p << 1, nl, mid),
                       queryMax(l, r, p << 1 | 1, mid + 1, nr));
        }
    };
    
    vector<bool> getResults(vector<vector<int>>& queries) {
        const int INF = 1000000000;
        int maxCoord = 0;
        for (auto &q : queries) {
            if (q[0] == 1) maxCoord = max(maxCoord, q[1]);
            else {
                maxCoord = max(maxCoord, q[1]); // x
                // sz not needed for size bound
            }
        }
        int N = maxCoord + 5; // safety
        
        vector<long long> init(N);
        for (int i = 0; i < N; ++i) init[i] = (long long)INF - i;
        
        SegTree seg(N);
        seg.build(init);
        
        set<int> obs;
        vector<bool> ans;
        for (auto &q : queries) {
            if (q[0] == 1) {
                int p = q[1];
                // find right obstacle
                auto itR = obs.upper_bound(p);
                long long rightObs = (itR == obs.end()) ? INF : *itR;
                // find left bound of interval
                int leftBound = 0;
                if (!obs.empty()) {
                    auto itPrev = obs.lower_bound(p);
                    if (itPrev != obs.begin()) {
                        --itPrev;
                        leftBound = *itPrev + 1;
                    }
                }
                if (leftBound <= p - 1) {
                    long long delta = (long long)p - rightObs; // negative
                    seg.rangeAdd(leftBound, p - 1, delta);
                }
                obs.insert(p);
            } else { // type 2
                int x = q[1];
                int sz = q[2];
                int limit = x - sz;
                if (limit < 0) {
                    ans.push_back(false);
                } else {
                    long long mx = seg.queryMax(0, limit);
                    ans.push_back(mx > sz);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class SegTree {
        int n;
        int[] tree;
        SegTree(int size, int initVal) {
            n = size;
            tree = new int[4 * n];
            build(1, 0, n - 1, initVal);
        }
        private void build(int node, int l, int r, int val) {
            if (l == r) {
                tree[node] = val;
                return;
            }
            int mid = (l + r) >>> 1;
            build(node << 1, l, mid, val);
            build(node << 1 | 1, mid + 1, r, val);
            tree[node] = Math.max(tree[node << 1], tree[node << 1 | 1]);
        }
        void update(int idx, int value) {
            update(1, 0, n - 1, idx, value);
        }
        private void update(int node, int l, int r, int idx, int value) {
            if (l == r) {
                tree[node] = value;
                return;
            }
            int mid = (l + r) >>> 1;
            if (idx <= mid) update(node << 1, l, mid, idx, value);
            else update(node << 1 | 1, mid + 1, r, idx, value);
            tree[node] = Math.max(tree[node << 1], tree[node << 1 | 1]);
        }
        int query(int ql, int qr) {
            if (ql > qr) return Integer.MIN_VALUE;
            return query(1, 0, n - 1, ql, qr);
        }
        private int query(int node, int l, int r, int ql, int qr) {
            if (qr < l || r < ql) return Integer.MIN_VALUE;
            if (ql <= l && r <= qr) return tree[node];
            int mid = (l + r) >>> 1;
            return Math.max(query(node << 1, l, mid, ql, qr),
                            query(node << 1 | 1, mid + 1, r, ql, qr));
        }
    }

    public List<Boolean> getResults(int[][] queries) {
        int maxCoord = 0;
        for (int[] q : queries) {
            if (q[0] == 1) {
                maxCoord = Math.max(maxCoord, q[1]);
            } else {
                maxCoord = Math.max(maxCoord, Math.max(q[1], q[2]));
            }
        }
        int size = maxCoord + 5; // enough for all possible start positions
        final int INF = 1_000_000_000;
        SegTree seg = new SegTree(size, INF);
        TreeSet<Integer> obstacles = new TreeSet<>();
        obstacles.add(-1);                     // virtual obstacle before origin
        obstacles.add(Integer.MAX_VALUE);      // sentinel far right

        List<Boolean> ans = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) { // place obstacle
                int x = q[1];
                Integer prevObs = obstacles.lower(x);
                Integer nextObs = obstacles.higher(x);
                int leftStart = prevObs + 1;               // first free position after previous obstacle
                // update interval before the new obstacle
                if (leftStart <= x - 1) {
                    seg.update(leftStart, x - leftStart);
                } else {
                    if (leftStart < size) seg.update(leftStart, 0);
                }
                // update start right after the new obstacle
                int rightStart = x + 1;
                if (rightStart <= nextObs - 1 && rightStart < size) {
                    seg.update(rightStart, nextObs - rightStart);
                } else {
                    if (rightStart < size) seg.update(rightStart, 0);
                }
                // the position of the obstacle itself cannot be a start
                if (x < size) seg.update(x, 0);
                obstacles.add(x);
            } else { // query placement
                int x = q[1];
                int sz = q[2];
                int limit = x - sz;
                if (limit < 0) {
                    ans.add(false);
                    continue;
                }
                int maxLen = seg.query(0, Math.min(limit, size - 1));
                ans.add(maxLen > sz);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Determine maximum coordinate needed
        max_coord = 0
        for q in queries:
            if q[0] == 1:
                max_coord = max(max_coord, q[1])
            else:
                max_coord = max(max_coord, q[1])  # x value

        N = max_coord + 2  # include index max_coord
        INF_LEN = (max_coord + 5) * 2  # sufficiently large

        # ---------- Segment Tree for range maximum ----------
        size = 1
        while size < N:
            size <<= 1
        seg = [0] * (2 * size)

        # initialize leaves with INF_LEN
        for i in range(N):
            seg[size + i] = INF_LEN
        for i in range(size - 1, 0, -1):
            seg[i] = seg[i << 1] if seg[i << 1] > seg[(i << 1) | 1] else seg[(i << 1) | 1]

        def seg_set(pos, val):
            i = pos + size
            seg[i] = val
            i >>= 1
            while i:
                left = seg[i << 1]
                right = seg[(i << 1) | 1]
                seg[i] = left if left > right else right
                i >>= 1

        def seg_query(l, r):
            if l > r:
                return 0
            l += size
            r += size
            res = 0
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

        # ---------- Fenwick Tree for obstacle positions ----------
        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, idx, delta):
                i = idx + 1
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i

            def sum(self, idx):
                if idx < 0:
                    return 0
                i = idx + 1
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s

            # find smallest index such that prefix sum >= k (k>=1)
            def kth(self, k):
                idx = 0
                bitmask = 1 << (self.n.bit_length())
                while bitmask:
                    t = idx + bitmask
                    if t <= self.n and self.bit[t] < k:
                        idx = t
                        k -= self.bit[t]
                    bitmask >>= 1
                return idx  # zero‑based

        fenwick = Fenwick(N)

        # ---------- DSU for one‑time updates of d[i] ----------
        parent = list(range(N))

        def find(u):
            while u >= 0 and parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        results = []
        for q in queries:
            if q[0] == 1:          # place obstacle
                p = q[1]

                # find previous obstacle
                cnt_before = fenwick.sum(p - 1)
                prev = -1 if cnt_before == 0 else fenwick.kth(cnt_before)

                # update d[i] for i in [prev+1, p]
                left = prev + 1
                i = find(p)
                while i >= left:
                    seg_set(i, p - i)
                    parent[i] = i - 1   # mark as processed
                    i = find(i)

                fenwick.add(p, 1)    # record obstacle

            else:                   # query placement
                x, sz = q[1], q[2]
                limit = x - sz
                if limit < 0:
                    results.append(False)
                else:
                    max_val = seg_query(0, limit)
                    results.append(max_val > sz)

        return results
```

## Python3

```python
import sys
from bisect import bisect_left, bisect_right

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, val):
        i = idx + 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def sum(self, idx):
        # prefix sum [0..idx]
        i = idx + 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        # smallest index such that prefix >= k (k>=1)
        idx = 0
        bitmask = 1 << (self.n.bit_length())
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1
        return idx  # zero‑based

class SegTree:
    def __init__(self, size, INF):
        self.N = size
        self.INF = INF
        self.maxv = [0] * (4 * size)
        self.lz = [None] * (4 * size)
        self._build(1, 0, self.N - 1)

    def _apply(self, node, l, r, val):
        self.lz[node] = val
        self.maxv[node] = val - l

    def _push(self, node, l, r):
        if self.lz[node] is not None and l != r:
            mid = (l + r) // 2
            self._apply(node * 2, l, mid, self.lz[node])
            self._apply(node * 2 + 1, mid + 1, r, self.lz[node])
            self.lz[node] = None

    def _build(self, node, l, r):
        if l == r:
            self.maxv[node] = self.INF - l
            return
        mid = (l + r) // 2
        self._build(node * 2, l, mid)
        self._build(node * 2 + 1, mid + 1, r)
        self.maxv[node] = max(self.maxv[node * 2], self.maxv[node * 2 + 1])

    def update(self, ql, qr, val):
        if ql > qr:
            return
        self._update(1, 0, self.N - 1, ql, qr, val)

    def _update(self, node, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self._apply(node, l, r, val)
            return
        self._push(node, l, r)
        mid = (l + r) // 2
        self._update(node * 2, l, mid, ql, qr, val)
        self._update(node * 2 + 1, mid + 1, r, ql, qr, val)
        self.maxv[node] = max(self.maxv[node * 2], self.maxv[node * 2 + 1])

    def query(self, ql, qr):
        if ql > qr:
            return -self.INF
        return self._query(1, 0, self.N - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return -self.INF
        if ql <= l and r <= qr:
            return self.maxv[node]
        self._push(node, l, r)
        mid = (l + r) // 2
        left = self._query(node * 2, l, mid, ql, qr)
        right = self._query(node * 2 + 1, mid + 1, r, ql, qr)
        return max(left, right)

class Solution:
    def getResults(self, queries):
        MAX_POS = 50000 + 5
        INF = 10 ** 9

        bit = BIT(MAX_POS + 2)          # for obstacle positions
        seg = SegTree(MAX_POS + 1, INF)  # indices 0..MAX_POS

        results = []

        for q in queries:
            if q[0] == 1:   # place obstacle at x
                x = q[1]
                # find predecessor and successor obstacles
                cnt_le = bit.sum(x)
                total = bit.sum(MAX_POS + 1)

                prev_obs = -1
                if cnt_le > 0:
                    prev_obs = bit.kth(cnt_le)   # last obstacle <= x

                nxt_obs = INF
                if cnt_le < total:
                    nxt_obs = bit.kth(cnt_le + 1)   # first obstacle > x

                L = prev_obs + 1
                R = nxt_obs

                # update ranges according to new obstacle at x
                seg.update(L, x - 1, x)
                seg.update(x, x, x)          # obstacle itself (distance zero)
                if x + 1 <= R - 1:
                    seg.update(x + 1, R - 1, R)

                bit.add(x, 1)

            else:   # query type 2
                _, x, sz = q
                limit = x - sz
                if limit < 0:
                    results.append(False)
                    continue
                max_val = seg.query(0, limit)
                results.append(max_val > sz)

        return results
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

#define MAXV 50005   // enough for given constraints

/* ---------- BIT (Fenwick) ---------- */
static int bit[MAXV + 2];

static void bitAdd(int idx, int delta) {
    for (++idx; idx <= MAXV + 1; idx += idx & -idx)
        bit[idx] += delta;
}
static int bitSum(int idx) { // sum [0..idx]
    int res = 0;
    for (++idx; idx > 0; idx -= idx & -idx)
        res += bit[idx];
    return res;
}
/* find smallest index such that prefix sum >= k (1‑based k) */
static int bitFindKth(int k) {
    int idx = 0;
    int mask = 1 << 16;               // since MAXV < 2^17
    while (mask) {
        int next = idx + mask;
        if (next <= MAXV + 1 && bit[next] < k) {
            idx = next;
            k -= bit[next];
        }
        mask >>= 1;
    }
    return idx;   // zero‑based index
}
static int getPrev(int x) {           // largest obstacle < x, -1 if none
    int cnt = (x == 0) ? 0 : bitSum(x - 1);
    if (cnt == 0) return -1;
    return bitFindKth(cnt);
}
static int getNext(int x) {           // smallest obstacle > x, MAXV if none
    int total = bitSum(MAXV);
    int cnt = bitSum(x);
    if (cnt == total) return MAXV;   // sentinel for "no next"
    return bitFindKth(cnt + 1);
}

/* ---------- Segment Tree (range max) ---------- */
static int seg[4 * (MAXV + 5)];

static void segUpdate(int node, int l, int r, int pos, int val) {
    if (l == r) {
        seg[node] = val;
        return;
    }
    int mid = (l + r) >> 1;
    if (pos <= mid)
        segUpdate(node << 1, l, mid, pos, val);
    else
        segUpdate(node << 1 | 1, mid + 1, r, pos, val);
    seg[node] = seg[node << 1] > seg[node << 1 | 1] ? seg[node << 1] : seg[node << 1 | 1];
}
static int segQuery(int node, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return seg[node];
    int mid = (l + r) >> 1;
    int left = segQuery(node << 1, l, mid, ql, qr);
    int right = segQuery(node << 1 | 1, mid + 1, r, ql, qr);
    return left > right ? left : right;
}

/* ---------- Main function ---------- */
bool* getResults(int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    // initialize structures
    for (int i = 0; i <= MAXV + 1; ++i) bit[i] = 0;
    for (int i = 0; i < 4 * (MAXV + 5); ++i) seg[i] = 0;

    // initial gap starting at 0 with length MAXV
    segUpdate(1, 0, MAXV, 0, MAXV);

    // count type‑2 queries to allocate result array
    int cntType2 = 0;
    for (int i = 0; i < queriesSize; ++i)
        if (queries[i][0] == 2) ++cntType2;

    bool* ans = (bool*)malloc(sizeof(bool) * cntType2);
    int ansIdx = 0;

    for (int i = 0; i < queriesSize; ++i) {
        int type = queries[i][0];
        if (type == 1) {                     // place obstacle
            int x = queries[i][1];
            int prev = getPrev(x);
            int next = getNext(x);
            int leftStart = (prev == -1) ? 0 : prev;

            // update left part gap length
            segUpdate(1, 0, MAXV, leftStart, x - leftStart);
            // new right part gap starting at x
            segUpdate(1, 0, MAXV, x, next - x);

            // record obstacle in BIT
            bitAdd(x, 1);
        } else {                             // query placement
            int x = queries[i][1];
            int sz = queries[i][2];
            int L = x - sz;
            bool ok = false;
            if (L >= 0) {
                int maxLen = segQuery(1, 0, MAXV, 0, L);
                ok = (maxLen >= sz);
            }
            ans[ansIdx++] = ok;
        }
    }

    *returnSize = ansIdx;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    private const int MAX_POS = 50000 + 5; // enough for all coordinates
    private const int INF = MAX_POS;      // sentinel obstacle far right

    public IList<bool> GetResults(int[][] queries) {
        var results = new List<bool>();
        var obstacles = new SortedSet<int>();
        obstacles.Add(INF); // sentinel rightmost obstacle

        var seg = new SegmentTree(MAX_POS + 2);
        // initial gap from -1 to INF has length INF
        seg.Update(0, INF);

        foreach (var q in queries) {
            int type = q[0];
            if (type == 1) {
                int p = q[1];

                // predecessor a
                int a = -1;
                var leftView = obstacles.GetViewBetween(int.MinValue, p - 1);
                if (leftView.Count > 0) {
                    a = leftView.Max();
                }

                // successor b
                int b = obstacles.GetViewBetween(p + 1, int.MaxValue).Min();

                // remove old gap starting at a
                seg.Update(a + 1, 0);

                // add new gaps
                int len1 = p - a - 1;
                seg.Update(a + 1, len1);
                int len2 = b - p - 1;
                seg.Update(p + 1, len2);

                obstacles.Add(p);
            } else { // type == 2
                int x = q[1];
                int sz = q[2];
                int limit = x - sz - 1; // maximum allowed left obstacle position

                if (limit < -1) {
                    results.Add(false);
                    continue;
                }
                int rIdx = Math.Min(limit + 1, MAX_POS + 1);
                int maxLen = seg.Query(0, rIdx);
                results.Add(maxLen > sz);
            }
        }

        return results;
    }

    private class SegmentTree {
        private readonly int size;
        private readonly int[] tree;

        public SegmentTree(int n) {
            size = 1;
            while (size < n) size <<= 1;
            tree = new int[2 * size];
        }

        public void Update(int pos, int value) {
            int i = pos + size;
            tree[i] = value;
            for (i >>= 1; i > 0; i >>= 1) {
                tree[i] = Math.Max(tree[i << 1], tree[(i << 1) | 1]);
            }
        }

        public int Query(int l, int r) {
            if (l > r) return 0;
            l += size;
            r += size;
            int res = 0;
            while (l <= r) {
                if ((l & 1) == 1) {
                    res = Math.Max(res, tree[l]);
                    l++;
                }
                if ((r & 1) == 0) {
                    res = Math.Max(res, tree[r]);
                    r--;
                }
                l >>= 1;
                r >>= 1;
            }
            return res;
        }
    }
}
```

## Javascript

```javascript
/ **
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var getResults = function(queries) {
    // Determine maximum coordinate needed
    let maxCoord = 0;
    for (const q of queries) {
        if (q[0] === 1) {
            maxCoord = Math.max(maxCoord, q[1]);
        } else {
            maxCoord = Math.max(maxCoord, q[1]); // x
        }
    }
    const N = maxCoord + 5;               // safe margin
    const INF_GAP = 1000000000;           // larger than any possible sz

    // ---------- BIT ----------
    class BIT {
        constructor(n) {
            this.n = n;
            this.bit = new Int32Array(n + 2);
        }
        add(idx, delta) {                 // idx is zero‑based
            for (let i = idx + 1; i <= this.n + 1; i += i & -i) {
                this.bit[i] += delta;
            }
        }
        sum(idx) {                        // prefix sum [0..idx], idx zero‑based, idx<0 => 0
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.bit[i];
            }
            return res;
        }
        // smallest index such that prefix sum >= k (k>=1)
        kth(k) {
            let idx = 0;
            let bitMask = 1 << (Math.floor(Math.log2(this.n + 1)) + 1);
            for (let d = bitMask; d !== 0; d >>= 1) {
                const next = idx + d;
                if (next <= this.n && this.bit[next] < k) {
                    idx = next;
                    k -= this.bit[next];
                }
            }
            return idx; // zero‑based
        }
    }

    // ---------- Segment Tree ----------
    class SegTree {
        constructor(n, initVal) {
            this.N = 1;
            while (this.N < n) this.N <<= 1;
            this.tree = new Int32Array(this.N * 2);
            for (let i = 0; i < n; ++i) {
                this.tree[this.N + i] = initVal(i);
            }
            for (let i = this.N - 1; i > 0; --i) {
                this.tree[i] = Math.max(this.tree[i << 1], this.tree[(i << 1) | 1]);
            }
        }
        update(pos, val) {                 // zero‑based
            let idx = pos + this.N;
            this.tree[idx] = val;
            while (idx > 1) {
                idx >>= 1;
                const newVal = Math.max(this.tree[idx << 1], this.tree[(idx << 1) | 1]);
                if (this.tree[idx] === newVal) break;
                this.tree[idx] = newVal;
            }
        }
        query(l, r) {                      // inclusive, zero‑based
            let left = l + this.N, right = r + this.N;
            let res = 0;
            while (left <= right) {
                if ((left & 1) === 1) {
                    res = Math.max(res, this.tree[left]);
                    ++left;
                }
                if ((right & 1) === 0) {
                    res = Math.max(res, this.tree[right]);
                    --right;
                }
                left >>= 1;
                right >>= 1;
            }
            return res;
        }
    }

    const bit = new BIT(N);
    const seg = new SegTree(N + 1, (i) => (i === 0 ? INF_GAP : 0));

    const results = [];

    for (const q of queries) {
        if (q[0] === 1) {                     // place obstacle
            const p = q[1];

            // find predecessor
            let prev = null;
            const cntPrev = bit.sum(p - 1);
            if (cntPrev > 0) prev = bit.kth(cntPrev);

            // find successor
            const total = bit.sum(N);
            const cntBefore = bit.sum(p);
            let next = null;
            if (cntBefore < total) next = bit.kth(cntBefore + 1);

            // insert into BIT
            bit.add(p, 1);

            // update gap for predecessor (or start)
            if (prev !== null) {
                const valPrev = Math.max(0, p - prev - 1);
                seg.update(prev, valPrev);
            } else {
                // first obstacle: distance from position 0
                seg.update(0, p);
            }

            // update gap starting at new obstacle
            if (next !== null) {
                const valNew = Math.max(0, next - p - 1);
                seg.update(p, valNew);
            } else {
                seg.update(p, INF_GAP);
            }
        } else {                               // query placement
            const x = q[1];
            const sz = q[2];
            const limit = x - sz;
            if (limit < 0) {
                results.push(false);
                continue;
            }
            const r = Math.min(limit, N);
            const maxGap = seg.query(0, r);
            results.push(maxGap > sz);
        }
    }

    return results;
};
```

## Typescript

```typescript
function getResults(queries: number[][]): boolean[] {
    const INF = 1e9;
    // Determine maximum coordinate needed
    let maxCoord = 0;
    for (const q of queries) {
        if (q[0] === 1) {
            maxCoord = Math.max(maxCoord, q[1]);
        } else {
            maxCoord = Math.max(maxCoord, q[1]); // x can be up to coordinate
        }
    }
    const N = maxCoord + 5; // extra space for p+1 positions

    class Fenwick {
        n: number;
        bit: number[];
        constructor(n: number) {
            this.n = n;
            this.bit = new Array(n + 2).fill(0);
        }
        add(idx: number, delta: number): void {
            for (let i = idx; i <= this.n; i += i & -i) this.bit[i] += delta;
        }
        sum(idx: number): number {
            let res = 0;
            for (let i = idx; i > 0; i -= i & -i) res += this.bit[i];
            return res;
        }
        // smallest index such that prefix sum >= k (1‑based)
        kth(k: number): number {
            let idx = 0;
            let bitMask = 1 << (Math.floor(Math.log2(this.n)) + 1);
            while (bitMask !== 0) {
                const next = idx + bitMask;
                if (next <= this.n && this.bit[next] < k) {
                    idx = next;
                    k -= this.bit[next];
                }
                bitMask >>= 1;
            }
            return idx + 1;
        }
    }

    class SegTree {
        n: number;
        seg: number[];
        constructor(n: number) {
            this.n = n;
            this.seg = new Array(4 * n).fill(-Infinity);
        }
        update(pos: number, val: number, node: number = 1, l: number = 0, r: number = this.n - 1): void {
            if (l === r) {
                this.seg[node] = val;
                return;
            }
            const mid = (l + r) >> 1;
            if (pos <= mid) this.update(pos, val, node << 1, l, mid);
            else this.update(pos, val, node << 1 | 1, mid + 1, r);
            this.seg[node] = Math.max(this.seg[node << 1], this.seg[node << 1 | 1]);
        }
        query(qL: number, qR: number, node: number = 1, l: number = 0, r: number = this.n - 1): number {
            if (qL > r || qR < l) return -Infinity;
            if (qL <= l && r <= qR) return this.seg[node];
            const mid = (l + r) >> 1;
            return Math.max(
                this.query(qL, qR, node << 1, l, mid),
                this.query(qL, qR, node << 1 | 1, mid + 1, r)
            );
        }
    }

    const fenwick = new Fenwick(N);
    const seg = new SegTree(N);
    // initial infinite gap starting at 0
    seg.update(0, INF);

    const results: boolean[] = [];

    for (const q of queries) {
        if (q[0] === 1) { // place obstacle
            const p = q[1]; // position
            // find previous obstacle (< p)
            const cntPrev = fenwick.sum(p); // obstacles with index <= p-1
            let prevPos = -1;
            if (cntPrev > 0) {
                const idx = fenwick.kth(cntPrev);
                prevPos = idx - 1; // convert to coordinate
            }
            // find next obstacle (> p)
            const totalObs = fenwick.sum(N);
            const cntLeP = fenwick.sum(p + 1); // obstacles <= p
            let nextPos: number;
            if (cntLeP === totalObs) {
                nextPos = INF; // treat as infinite
            } else {
                const idx = fenwick.kth(cntLeP + 1);
                nextPos = idx - 1;
            }

            // left gap start
            const leftStart = prevPos + 1; // if prevPos==-1 => 0
            const leftLen = p - leftStart;
            seg.update(leftStart, leftLen);

            // right gap start
            const rightStart = p + 1;
            const rightLen = nextPos === INF ? INF : nextPos - rightStart;
            seg.update(rightStart, rightLen);

            // add obstacle to fenwick (store at index pos+1)
            fenwick.add(p + 1, 1);
        } else { // query placement
            const x = q[1];
            const sz = q[2];
            const R = x - sz;
            if (R < 0) {
                results.push(false);
            } else {
                const maxLen = seg.query(0, Math.min(R, N - 1));
                results.push(maxLen >= sz);
            }
        }
    }

    return results;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function getResults($queries) {
        // Determine maximum coordinate needed
        $maxCoord = 0;
        foreach ($queries as $q) {
            if ($q[0] == 1) {
                $maxCoord = max($maxCoord, $q[1]);
            } else {
                $maxCoord = max($maxCoord, $q[1]); // x
            }
        }
        // BIT for obstacle count (order statistics)
        $bit = new class($maxCoord + 2) {
            public $n;
            public $tree;
            function __construct($size) {
                $this->n = $size;
                $this->tree = array_fill(0, $size + 1, 0);
            }
            function add($idx, $delta) {
                for ($i = $idx; $i <= $this->n; $i += $i & -$i) {
                    $this->tree[$i] += $delta;
                }
            }
            function sum($idx) {
                $res = 0;
                for ($i = $idx; $i > 0; $i -= $i & -$i) {
                    $res += $this->tree[$i];
                }
                return $res;
            }
            // find smallest index such that prefix sum >= k (k is 1‑based)
            function findKth($k) {
                $idx = 0;
                $bitMask = 1;
                while ($bitMask << 1 <= $this->n) $bitMask <<= 1;
                for (; $bitMask > 0; $bitMask >>= 1) {
                    $next = $idx + $bitMask;
                    if ($next <= $this->n && $this->tree[$next] < $k) {
                        $idx = $next;
                        $k -= $this->tree[$next];
                    }
                }
                return $idx + 1;
            }
        };
        // Segment tree for gap lengths (point assign, range max)
        $segSize = 1;
        while ($segSize < $maxCoord + 2) $segSize <<= 1;
        $segTree = array_fill(0, $segSize * 2, 0);
        $update = function($pos, $val) use (&$segTree, $segSize) {
            $i = $pos + $segSize - 1;
            $segTree[$i] = $val;
            for ($i >>= 1; $i >= 1; $i >>= 1) {
                $segTree[$i] = max($segTree[$i << 1], $segTree[($i << 1) | 1]);
            }
        };
        $queryMax = function($l, $r) use (&$segTree, $segSize) {
            if ($l > $r) return 0;
            $l += $segSize - 1;
            $r += $segSize - 1;
            $res = 0;
            while ($l <= $r) {
                if (($l & 1) == 1) { $res = max($res, $segTree[$l]); $l++; }
                if (($r & 1) == 0) { $res = max($res, $segTree[$r]); $r--; }
                $l >>= 1;
                $r >>= 1;
            }
            return $res;
        };
        $results = [];
        foreach ($queries as $q) {
            if ($q[0] == 1) { // place obstacle
                $pos = $q[1];
                // predecessor
                $cntPrev = $bit->sum($pos - 1);
                $prev = 0;
                if ($cntPrev > 0) {
                    $prev = $bit->findKth($cntPrev);
                }
                // successor
                $total = $bit->sum($maxCoord + 1);
                $cntPos = $bit->sum($pos);
                $next = null;
                if ($cntPos < $total) {
                    $next = $bit->findKth($cntPos + 1);
                }
                // update gap ending at pos
                $update($pos, $pos - $prev);
                // update gap ending at next (if exists)
                if ($next !== null) {
                    $update($next, $next - $pos);
                }
                // add obstacle to BIT
                $bit->add($pos, 1);
            } else { // query placement
                $x = $q[1];
                $sz = $q[2];
                if ($sz > $x) {
                    $results[] = false;
                    continue;
                }
                // max full gap with right endpoint <= x
                $maxGap = $queryMax(1, $x);
                // partial gap that contains x (right endpoint > x)
                $cntPrev = $bit->sum($x - 1);
                $prev = 0;
                if ($cntPrev > 0) {
                    $prev = $bit->findKth($cntPrev);
                }
                $partial = $x - $prev;
                if ($partial > $maxGap) $maxGap = $partial;
                $results[] = ($maxGap >= $sz);
            }
        }
        return $results;
    }
}
```

## Swift

```swift
import Foundation

class SegmentTree {
    private var n: Int
    private var tree: [Int]
    init(_ size: Int) {
        var sz = 1
        while sz < size { sz <<= 1 }
        n = sz
        tree = Array(repeating: 0, count: 2 * n)
    }
    func update(_ index: Int, _ value: Int) {
        var i = index + n
        tree[i] = value
        i >>= 1
        while i > 0 {
            tree[i] = max(tree[i << 1], tree[(i << 1) | 1])
            i >>= 1
        }
    }
    func query(_ left: Int, _ right: Int) -> Int {
        if left > right { return 0 }
        var l = left + n
        var r = right + n
        var res = 0
        while l <= r {
            if (l & 1) == 1 {
                res = max(res, tree[l])
                l += 1
            }
            if (r & 1) == 0 {
                res = max(res, tree[r])
                r -= 1
            }
            l >>= 1
            r >>= 1
        }
        return res
    }
}

class BIT {
    private var n: Int
    private var bit: [Int]
    init(_ size: Int) {
        n = size
        bit = Array(repeating: 0, count: n + 2)
    }
    func add(_ idx: Int, _ delta: Int) {
        var i = idx + 1
        while i <= n + 1 {
            bit[i] += delta
            i += i & -i
        }
    }
    func sum(_ idx: Int) -> Int {
        if idx < 0 { return 0 }
        var i = idx + 1
        var res = 0
        while i > 0 {
            res += bit[i]
            i -= i & -i
        }
        return res
    }
    func total() -> Int {
        return sum(n - 1)
    }
    // returns smallest index (0‑based) such that prefix sum >= k, assuming 1 ≤ k ≤ total()
    func kth(_ k: Int) -> Int {
        var idx = 0
        var mask = 1
        while mask <= n + 1 { mask <<= 1 }
        var curMask = mask
        var curSum = 0
        while curMask > 0 {
            let next = idx + curMask
            if next <= n + 1 && curSum + bit[next] < k {
                idx = next
                curSum += bit[next]
            }
            curMask >>= 1
        }
        // idx is the largest position with prefix sum < k (in BIT's 1‑based indexing)
        return idx   // zero‑based index of the desired element
    }
}

class Solution {
    func getResults(_ queries: [[Int]]) -> [Bool] {
        var maxCoord = 0
        for q in queries {
            if q[0] == 1 {
                maxCoord = max(maxCoord, q[1])
            } else {
                maxCoord = max(maxCoord, q[1])
            }
        }
        let INF = maxCoord + 50000   // sufficiently large sentinel
        
        let size = maxCoord + 2       // indices 0 … maxCoord
        let seg = SegmentTree(size)
        let bit = BIT(size)
        
        // initial gap starting at 0 with huge length
        seg.update(0, INF)
        
        var results: [Bool] = []
        
        for q in queries {
            if q[0] == 1 {
                let p = q[1]
                
                // find predecessor obstacle
                let cntPrev = bit.sum(p - 1)          // obstacles with index <= p-1
                var prev = -1
                if cntPrev > 0 {
                    prev = bit.kth(cntPrev)
                }
                
                // find successor obstacle
                let totalObs = bit.total()
                let cntLeqP = bit.sum(p)              // obstacles <= p (p not yet inserted)
                var next = INF
                if cntLeqP < totalObs {
                    next = bit.kth(cntLeqP + 1)
                }
                
                // insert obstacle into BIT
                bit.add(p, 1)
                
                // update segment tree: remove old gap starting at prev+1
                let oldLeft = prev + 1
                if oldLeft < size {
                    seg.update(oldLeft, 0)
                }
                
                // left subgap [prev+1 , p-1]
                let leftLen = p - prev - 1
                if leftLen > 0 && (prev + 1) < size {
                    seg.update(prev + 1, leftLen)
                }
                
                // right subgap [p+1 , next-1]
                let rightStart = p + 1
                let rightLen = next - p - 1
                if rightLen > 0 && rightStart < size {
                    seg.update(rightStart, rightLen)
                }
            } else { // type 2 query
                let x = q[1]
                let sz = q[2]
                if sz > x {
                    results.append(false)
                    continue
                }
                let limit = x - sz
                if limit < 0 {
                    results.append(false)
                    continue
                }
                let maxLen = seg.query(0, min(limit, size - 1))
                results.append(maxLen >= sz)
            }
        }
        return results
    }
}
```

## Kotlin

```kotlin
import java.util.TreeSet

class Solution {
    private val INF = 1_000_000_007

    private class SegmentTree(n: Int, initVal: Int) {
        private var size = 1
        private val tree: IntArray

        init {
            while (size < n) size = size shl 1
            tree = IntArray(size * 2) { Int.MIN_VALUE }
            for (i in 0 until n) {
                tree[size + i] = initVal
            }
            for (i in size - 1 downTo 1) {
                tree[i] = kotlin.math.max(tree[i shl 1], tree[(i shl 1) + 1])
            }
        }

        fun update(pos: Int, value: Int) {
            var idx = pos + size
            if (tree[idx] == value) return
            tree[idx] = value
            idx = idx shr 1
            while (idx >= 1) {
                val newVal = kotlin.math.max(tree[idx shl 1], tree[(idx shl 1) + 1])
                if (tree[idx] == newVal) break
                tree[idx] = newVal
                idx = idx shr 1
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

    fun getResults(queries: Array<IntArray>): List<Boolean> {
        var maxPos = 0
        for (q in queries) {
            if (q[0] == 1) {
                maxPos = kotlin.math.max(maxPos, q[1])
            } else {
                maxPos = kotlin.math.max(maxPos, q[1])
            }
        }
        // positions are from 0 to maxPos inclusive
        val n = maxPos + 1
        val seg = SegmentTree(n, INF)
        val obstacles = TreeSet<Int>()
        val ans = ArrayList<Boolean>()

        for (q in queries) {
            if (q[0] == 1) {
                val p = q[1]
                val prev = obstacles.lower(p) ?: -1
                var start = prev + 1
                if (start < 0) start = 0
                for (pos in start..p) {
                    seg.update(pos, p - pos)
                }
                obstacles.add(p)
            } else {
                val x = q[1]
                val sz = q[2]
                if (x < sz) {
                    ans.add(false)
                } else {
                    val limit = x - sz
                    val maxDist = seg.query(0, limit)
                    ans.add(maxDist >= sz)
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Fenwick {
  final List<int> _bit;
  final int n;
  Fenwick(this.n) : _bit = List.filled(n + 2, 0);
  void add(int idx, int delta) {
    for (int i = idx; i <= n; i += i & -i) {
      _bit[i] += delta;
    }
  }

  int sum(int idx) {
    int res = 0;
    for (int i = idx; i > 0; i -= i & -i) {
      res += _bit[i];
    }
    return res;
  }

  // find smallest index such that prefix sum >= k (k >=1)
  int kth(int k) {
    int idx = 0;
    int bitMask = 1 << (log2(n).floor() + 1);
    while (bitMask != 0) {
      int next = idx + bitMask;
      if (next <= n && _bit[next] < k) {
        idx = next;
        k -= _bit[next];
      }
      bitMask >>= 1;
    }
    return idx + 1; // 1‑based index
  }

  int total() => sum(n);
}

class Solution {
  List<bool> getResults(List<List<int>> queries) {
    const int INF = 1 << 30;

    // Determine maximum coordinate needed
    int maxCoord = 0;
    for (var q in queries) {
      if (q[0] == 1) {
        maxCoord = max(maxCoord, q[1]);
      } else {
        maxCoord = max(maxCoord, q[1]); // x value
      }
    }
    // BIT works with 1‑based indices; store position+1
    int size = maxCoord + 5;
    Fenwick bit = Fenwick(size);

    List<bool> ans = [];

    for (var q in queries) {
      if (q[0] == 1) {
        int x = q[1];
        // add obstacle at x
        bit.add(x + 1, 1);
      } else {
        int x = q[1];
        int sz = q[2];
        if (x < sz) {
          ans.add(false);
          continue;
        }
        int limit = x - sz; // maximum allowed start position

        // number of obstacles with position <= limit
        int cntPrev = bit.sum(limit + 1);
        int total = bit.total();

        bool canPlace = false;

        if (cntPrev == 0) {
          // no predecessor obstacle
          if (total == 0) {
            canPlace = true; // no obstacles at all
          } else {
            // first obstacle position
            int idxFirst = bit.kth(1);
            int posFirst = idxFirst - 1;
            int gap = posFirst - 0;
            if (gap >= sz) canPlace = true;
          }
        } else {
          // predecessor exists
          int idxPrev = bit.kth(cntPrev);
          int posPrev = idxPrev - 1;

          if (cntPrev == total) {
            // no successor, infinite gap to the right
            canPlace = true;
          } else {
            int idxSucc = bit.kth(cntPrev + 1);
            int posSucc = idxSucc - 1;
            int gap = posSucc - posPrev;
            if (gap >= sz) canPlace = true;
          }
        }

        ans.add(canPlace);
      }
    }

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math/rand"
	"time"
)

type segTree struct {
	n    int
	tree []int
}

func newSegTree(n int) *segTree {
	st := &segTree{
		n:    n,
		tree: make([]int, 4*n),
	}
	return st
}

func (st *segTree) update(idx, val int) {
	var upd func(node, l, r int)
	upd = func(node, l, r int) {
		if l == r {
			st.tree[node] = val
			return
		}
		mid := (l + r) >> 1
		if idx <= mid {
			upd(node<<1, l, mid)
		} else {
			upd(node<<1|1, mid+1, r)
		}
		if st.tree[node<<1] > st.tree[node<<1|1] {
			st.tree[node] = st.tree[node<<1]
		} else {
			st.tree[node] = st.tree[node<<1|1]
		}
	}
	upd(1, 0, st.n-1)
}

func (st *segTree) query(qL, qR int) int {
	if qL > qR {
		return 0
	}
	var qry func(node, l, r int) int
	qry = func(node, l, r int) int {
		if qL <= l && r <= qR {
			return st.tree[node]
		}
		mid := (l + r) >> 1
		res := 0
		if qL <= mid {
			v := qry(node<<1, l, mid)
			if v > res {
				res = v
			}
		}
		if qR > mid {
			v := qry(node<<1|1, mid+1, r)
			if v > res {
				res = v
			}
		}
		return res
	}
	return qry(1, 0, st.n-1)
}

// treap for ordered set of obstacles
type node struct {
	key       int
	priority  uint32
	left      *node
	right     *node
}

func rotateRight(y *node) *node {
	x := y.left
	y.left = x.right
	x.right = y
	return x
}
func rotateLeft(x *node) *node {
	y := x.right
	x.right = y.left
	y.left = x
	return y
}
func treapInsert(root *node, key int) *node {
	if root == nil {
		return &node{key: key, priority: rand.Uint32()}
	}
	if key < root.key {
		root.left = treapInsert(root.left, key)
		if root.left.priority < root.priority {
			root = rotateRight(root)
		}
	} else {
		root.right = treapInsert(root.right, key)
		if root.right.priority < root.priority {
			root = rotateLeft(root)
		}
	}
	return root
}
func predecessor(root *node, key int) (int, bool) {
	found := false
	var pred int
	for root != nil {
		if key <= root.key {
			root = root.left
		} else {
			pred = root.key
			found = true
			root = root.right
		}
	}
	return pred, found
}
func successor(root *node, key int) (int, bool) {
	found := false
	var succ int
	for root != nil {
		if key >= root.key {
			root = root.right
		} else {
			succ = root.key
			found = true
			root = root.left
		}
	}
	return succ, found
}

func getResults(queries [][]int) []bool {
	rand.Seed(time.Now().UnixNano())

	maxCoord := 0
	for _, q := range queries {
		if len(q) >= 2 && q[1] > maxCoord {
			maxCoord = q[1]
		}
		if len(q) == 3 && q[2] > maxCoord {
			maxCoord = q[2]
		}
	}
	// sentinel larger than any possible coordinate
	sentinel := maxCoord + 5

	st := newSegTree(sentinel + 1)

	// initial gap starting at 0 stretches to sentinel
	st.update(0, sentinel)

	var root *node
	results := make([]bool, 0)

	for _, q := range queries {
		if q[0] == 1 { // place obstacle
			p := q[1]

			l, hasL := predecessor(root, p)
			if !hasL {
				l = 0
			}
			r, hasR := successor(root, p)
			if !hasR {
				r = sentinel
			}

			// update gaps
			st.update(l, p-l)   // gap [l, p]
			st.update(p, r-p)   // gap [p, r]

			root = treapInsert(root, p)
		} else { // query placement
			x := q[1]
			sz := q[2]
			limit := x - sz
			if limit < 0 {
				results = append(results, false)
				continue
			}
			maxLen := st.query(0, limit)
			if maxLen >= sz {
				results = append(results, true)
			} else {
				results = append(results, false)
			}
		}
	}
	return results
}
```

## Ruby

```ruby
def get_results(queries)
  # Determine maximum coordinate needed
  max_coord = 0
  queries.each do |q|
    if q[0] == 1
      max_coord = [max_coord, q[1]].max
    else
      max_coord = [max_coord, q[1], q[2]].max
    end
  end
  n = max_coord + 5

  INF = 1_000_000_000

  # Segment Tree for range assign of next obstacle and query max (next - index)
  class SegTree
    def initialize(n, inf)
      @n = n
      @inf = inf
      size = 4 * n
      @max = Array.new(size, inf)
      @lazy = Array.new(size, nil)
    end

    def push(node, l, r)
      if (val = @lazy[node])
        mid = (l + r) / 2
        left = node * 2
        right = left + 1
        @max[left] = val - l
        @max[right] = val - (mid + 1)
        @lazy[left] = val
        @lazy[right] = val
        @lazy[node] = nil
      end
    end

    def update(node, l, r, ql, qr, val)
      return if ql > r || qr < l
      if ql <= l && r <= qr
        @max[node] = val - l
        @lazy[node] = val
        return
      end
      push(node, l, r)
      mid = (l + r) / 2
      update(node * 2, l, mid, ql, qr, val)
      update(node * 2 + 1, mid + 1, r, ql, qr, val)
      @max[node] = [@max[node * 2], @max[node * 2 + 1]].max
    end

    def query(node, l, r, ql, qr)
      return -1 << 60 if ql > r || qr < l
      if ql <= l && r <= qr
        return @max[node]
      end
      push(node, l, r)
      mid = (l + r) / 2
      left = query(node * 2, l, mid, ql, qr)
      right = query(node * 2 + 1, mid + 1, r, ql, qr)
      left > right ? left : right
    end

    def range_update(l, r, val)
      update(1, 0, @n - 1, l, r, val) if l <= r
    end

    def range_query(l, r)
      return - (1 << 60) if l > r
      query(1, 0, @n - 1, l, r)
    end
  end

  # Binary Indexed Tree for predecessor queries
  class BIT
    def initialize(n)
      @n = n
      @bit = Array.new(n + 2, 0)
    end

    def add(idx, delta)
      i = idx + 1
      while i <= @n + 1
        @bit[i] += delta
        i += i & -i
      end
    end

    def sum(idx)
      return 0 if idx < 0
      i = idx + 1
      res = 0
      while i > 0
        res += @bit[i]
        i -= i & -i
      end
      res
    end

    # find index (0‑based) of k‑th one (k >= 1)
    def kth(k)
      idx = 0
      bitmask = 1 << (Math.log2(@n + 1).to_i + 1)
      while bitmask > 0
        t = idx + bitmask
        if t <= @n + 1 && @bit[t] < k
          idx = t
          k -= @bit[t]
        end
        bitmask >>= 1
      end
      idx
    end
  end

  def prev_obstacle(bit, pos)
    cnt = bit.sum(pos - 1)
    return -1 if cnt == 0
    bit.kth(cnt)
  end

  seg = SegTree.new(n, INF)
  bit = BIT.new(n)

  results = []

  queries.each do |q|
    if q[0] == 1
      p = q[1]
      prev = prev_obstacle(bit, p)
      l = (prev == -1 ? 0 : prev)
      r = p - 1
      seg.range_update(l, r, p) if l <= r
      bit.add(p, 1)
    else
      x = q[1]
      sz = q[2]
      if sz > x
        results << false
        next
      end
      limit = x - sz
      max_gap = seg.range_query(0, limit)
      results << (max_gap >= sz)
    end
  end

  results
end
```

## Scala

```scala
import java.util.TreeSet

object Solution {
  def getResults(queries: Array[Array[Int]]): List[Boolean] = {
    val obstacles = new TreeSet[Int]()
    val ans = scala.collection.mutable.ListBuffer[Boolean]()

    for (q <- queries) {
      q(0) match {
        case 1 =>
          obstacles.add(q(1))
        case 2 =>
          val x = q(1)
          val sz = q(2)
          val limit = x - sz
          var ok = false
          if (limit >= 0) {
            // previous obstacle <= limit, or -1 if none
            var prev = -1
            if (!obstacles.isEmpty) {
              val floorObj = obstacles.floor(limit)
              if (floorObj != null) prev = floorObj.intValue()
            }

            // next obstacle strictly greater than prev
            var nextObj: java.lang.Integer = null
            if (prev == -1) {
              if (!obstacles.isEmpty) nextObj = obstacles.first()
            } else {
              nextObj = obstacles.higher(prev)
            }

            val low = Math.max(prev, 0)
            if (nextObj == null) {
              // infinite gap after prev
              ok = low <= limit
            } else {
              val nextVal = nextObj.intValue()
              val high = Math.min(limit, nextVal - sz)
              ok = low <= high
            }
          }
          ans += ok
      }
    }

    ans.toList
  }
}
```

## Rust

```rust
use std::collections::BTreeSet;

struct SegTree {
    n: usize,
    data: Vec<i32>,
}

impl SegTree {
    fn new(size: usize) -> Self {
        let mut n = 1usize;
        while n < size {
            n <<= 1;
        }
        SegTree { n, data: vec![-1; 2 * n] }
    }
    fn update(&mut self, idx: usize, value: i32) {
        let mut i = idx + self.n;
        self.data[i] = value;
        i >>= 1;
        while i > 0 {
            self.data[i] = self.data[i << 1].max(self.data[(i << 1) | 1]);
            i >>= 1;
        }
    }
    // inclusive query [l, r]
    fn query(&self, l: usize, r: usize) -> i32 {
        if l > r {
            return -1;
        }
        let mut res = -1;
        let mut left = l + self.n;
        let mut right = r + self.n;
        while left <= right {
            if (left & 1) == 1 {
                res = res.max(self.data[left]);
                left += 1;
            }
            if (right & 1) == 0 {
                res = res.max(self.data[right]);
                right -= 1;
            }
            left >>= 1;
            right >>= 1;
        }
        res
    }
}

impl Solution {
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
        const INF_LEN: i32 = 1_000_000_000;
        // determine maximum coordinate we need to handle
        let mut max_coord: usize = 0;
        for q in &queries {
            if q[0] == 1 {
                max_coord = max_coord.max(q[1] as usize);
            } else {
                max_coord = max_coord.max(q[1] as usize);
            }
        }
        // allocate a bit extra
        let size = max_coord + 5;
        let mut seg = SegTree::new(size);
        // initially no obstacles: infinite gap starting at 0
        seg.update(0, INF_LEN);

        let mut obstacles: BTreeSet<i32> = BTreeSet::new();
        let mut ans: Vec<bool> = Vec::new();

        for q in queries {
            if q[0] == 1 {
                let x = q[1] as i32;
                // find predecessor and successor
                let pred_opt = obstacles.range(..x).next_back().cloned();
                let succ_opt = obstacles.range((x + 1)..).next().cloned();

                let pred = pred_opt.unwrap_or(-1);
                let succ = succ_opt.unwrap_or(i32::MAX); // treat as infinite

                // old gap start
                let l_old: usize = if pred == -1 { 0 } else { (pred + 1) as usize };
                seg.update(l_old, -1);

                // first new gap [l_old, x)
                if x > l_old as i32 {
                    let len1 = x - l_old as i32; // distance to obstacle at x
                    seg.update(l_old, len1);
                }

                // second new gap starting at x+1
                let l2 = (x + 1) as usize;
                if succ != i32::MAX {
                    if l2 < succ as usize {
                        let len2 = succ - (x + 1);
                        seg.update(l2, len2);
                    }
                } else {
                    // infinite tail
                    seg.update(l2, INF_LEN);
                }

                obstacles.insert(x);
            } else {
                let x = q[1] as usize;
                let sz = q[2];
                if x < sz as usize {
                    ans.push(false);
                    continue;
                }
                let limit = x - sz as usize;
                let max_len = seg.query(0, limit);
                ans.push(max_len > sz);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define (get-results queries)
  (let* ((inf 1000000) ; larger than any possible sz
         ;; determine needed size
         (max-pos
          (let loop ((qs queries) (m 0))
            (if (null? qs)
                m
                (let* ((q (car qs))
                       (t (car q)))
                  (cond [(= t 1)
                         (loop (cdr qs) (max m (cadr q)))]
                        [(= t 2)
                         (let ((x (cadr q))
                               (sz (caddr q)))
                           (loop (cdr qs) (max m (+ x sz))))] ; ensure enough room
                        [else (loop (cdr qs) m)])))))
         (nmax (+ max-pos 5)) ; safety margin
         ;; BIT for obstacles (1‑based internal)
         (bit (make-vector (+ nmax 2) 0))
         ;; segment tree for gap lengths (prefix max query)
         (size
          (let loop ((s 1))
            (if (< s nmax) (loop (* s 2)) s)))
         (seg (make-vector (* 2 size) -inf)))

    ;; helpers for BIT
    (define (bit-add! idx delta)
      (let ((i (+ idx 1))) ; convert to 1‑based
        (let loop ()
          (when (<= i (+ nmax 1))
            (vector-set! bit i (+ (vector-ref bit i) delta))
            (set! i (+ i (bitwise-and i (- i))))
            (loop)))))
    (define (bit-sum idx)
      (let ((i (+ idx 1)) (res 0))
        (let loop ()
          (if (= i 0)
              res
              (begin
                (set! res (+ res (vector-ref bit i)))
                (set! i (bitwise-and (sub1 i) i))
                (loop))))))
    ;; binary search helpers for predecessor / successor
    (define (find-prev x)
      (if (= x 0) -1
          (let ((low 0) (high (- x 1)) (ans -1))
            (let loop ()
              (when (<= low high)
                (let ((mid (quotient (+ low high) 2)))
                  (if (> (bit-sum mid) 0)
                      (begin (set! ans mid) (set! low (+ mid 1)))
                      (set! high (- mid 1)))))
              ans))))
    (define (find-next x)
      (let ((total (bit-sum (- nmax 1))))
        (if (= (bit-sum x) total)
            inf
            (let ((target (+ (bit-sum x) 1))
                  (low (+ x 1)) (high (- nmax 1)) (ans -1))
              (let loop ()
                (when (<= low high)
                  (let ((mid (quotient (+ low high) 2)))
                    (if (>= (bit-sum mid) target)
                        (begin (set! ans mid) (set! high (- mid 1)))
                        (set! low (+ mid 1)))))
                ans))))
    ;; segment tree point set
    (define (seg-set! pos val)
      (let ((i (+ pos size)))
        (vector-set! seg i val)
        (let loop ((i (quotient i 2)))
          (when (> i 0)
            (vector-set! seg i (max (vector-ref seg (* 2 i))
                                    (vector-ref seg (+ (* 2 i) 1))))
            (loop (quotient i 2))))))
    ;; segment tree range max query inclusive
    (define (seg-query l r)
      (let ((l (+ l size)) (r (+ r size)) (res -inf))
        (let loop ((l l) (r r) (res res))
          (if (> l r)
              res
              (begin
                (when (odd? l)
                  (set! res (max res (vector-ref seg l)))
                  (set! l (+ l 1)))
                (when (even? r)
                  (set! res (max res (vector-ref seg r)))
                  (set! r (- r 1)))
                (loop (quotient l 2) (quotient r 2) res))))))
    ;; initialise first gap starting at 0 with infinite length
    (seg-set! 0 inf)

    ;; process queries
    (let loop ((qs queries) (out '()))
      (if (null? qs)
          (reverse out)
          (let* ((q (car qs))
                 (t (car q)))
            (cond
              [(= t 1) ; add obstacle
               (let* ((x (cadr q))
                      (prev (find-prev x))
                      (next (find-next x)))
                 ;; mark obstacle in BIT
                 (bit-add! x 1)
                 ;; update left gap
                 (let ((left-start (if (= prev -1) 0 (+ prev 1))))
                   (seg-set! left-start (- x left-start)))
                 ;; update right gap if within bounds
                 (let ((right-start (+ x 1)))
                   (when (< right-start nmax)
                     (let ((len (if (= next inf) inf (- next right-start))))
                       (seg-set! right-start len)))))
               (loop (cdr qs) out)]
              [(= t 2) ; query placement
               (let* ((x (cadr q))
                      (sz (caddr q))
                      (r (- x sz)))
                 (if (< r 0)
                     (loop (cdr qs) (cons #f out))
                     (let ((mx (seg-query 0 (min r (- nmax 1)))))
                       (loop (cdr qs) (cons (> mx sz) out)))))])
              [else (loop (cdr qs) out)]))))))
```

## Erlang

```erlang
-module(solution).
-export([get_results/1]).

%% Public API
-spec get_results(Queries :: [[integer()]]) -> [boolean()].
get_results(Queries) ->
    MaxX = max_coordinate(Queries, 0),
    Size = MaxX + 5,
    BIT0 = array:new(Size, {default, 0}),
    process_queries(Queries, BIT0, Size, []).

%% Find maximum x appearing in type 1 or type 2 queries
max_coordinate([], Acc) -> Acc;
max_coordinate([[Type | Rest] | Tail], Acc) ->
    X = case Type of
            1 -> hd(Rest);
            2 -> hd(Rest)
        end,
    NewAcc = if X > Acc -> X; true -> Acc end,
    max_coordinate(Tail, NewAcc).

%% Process all queries sequentially
process_queries([], _BIT, _Size, ResRev) ->
    lists:reverse(ResRev);
process_queries([[1, X] | Rest], BIT, Size, ResRev) ->
    % add obstacle at position X (0‑based). BIT is 1‑based.
    NewBIT = bit_update(X + 1, 1, BIT, Size),
    process_queries(Rest, NewBIT, Size, ResRev);
process_queries([[2, X, Sz] | Rest], BIT, Size, ResRev) ->
    Limit = X - Sz,
    Answer =
        if
            Limit < 0 -> false;
            true ->
                Total = bit_query(Size, BIT),
                case Total of
                    0 -> true; % no obstacles at all
                    _ ->
                        IdxLimit = Limit + 1,
                        CntLe = bit_query(IdxLimit, BIT),   % obstacles <= Limit
                        if
                            CntLe == 0 ->
                                % no predecessor, check first obstacle
                                OIdx = find_kth(1, BIT, Size),
                                OPos = OIdx - 1,
                                OPos > Sz;
                            true ->
                                PIdx = find_kth(CntLe, BIT, Size),
                                PPos = PIdx - 1,
                                if
                                    CntLe == Total ->
                                        % no successor after predecessor
                                        true;
                                    true ->
                                        OIdx = find_kth(CntLe + 1, BIT, Size),
                                        OPos = OIdx - 1,
                                        (OPos - PPos) > Sz
                                end
                        end
                end
        end,
    process_queries(Rest, BIT, Size, [Answer | ResRev]).

%% Fenwick tree point update (add Delta at position Idx)
-spec bit_update(integer(), integer(), array:array(integer()), integer()) -> array:array(integer()).
bit_update(Idx, _Delta, BitArr, Size) when Idx > Size ->
    BitArr;
bit_update(Idx, Delta, BitArr, Size) ->
    Cur = array:get(Idx, BitArr),
    NewArr = array:set(Idx, Cur + Delta, BitArr),
    Next = Idx + (Idx band -Idx),
    bit_update(Next, Delta, NewArr, Size).

%% Fenwick tree prefix sum query up to Idx
-spec bit_query(integer(), array:array(integer())) -> integer().
bit_query(0, _BitArr) ->
    0;
bit_query(Idx, BitArr) ->
    Cur = array:get(Idx, BitArr),
    Cur + bit_query(Idx - (Idx band -Idx), BitArr).

%% Find the index of the K‑th one (1‑based indexing in BIT)
-spec find_kth(integer(), array:array(integer()), integer()) -> integer().
find_kth(K, BitArr, Size) ->
    Highest = highest_power_of_two(Size),
    find_kth_loop(0, K, Highest, BitArr, Size).

highest_power_of_two(N) ->
    highest_power_of_two(N, 1).
highest_power_of_two(N, Pow) when (Pow bsl 1) =< N ->
    highest_power_of_two(N, Pow bsl 1);
highest_power_of_two(_N, Pow) -> Pow.

find_kth_loop(Idx, K, Bit, _BitArr, _Size) when Bit =:= 0 ->
    Idx + 1;
find_kth_loop(Idx, K, Bit, BitArr, Size) ->
    Next = Idx + Bit,
    case (Next =< Size) andalso (array:get(Next, BitArr) < K) of
        true ->
            NewK = K - array:get(Next, BitArr),
            find_kth_loop(Next, NewK, Bit bsr 1, BitArr, Size);
        false ->
            find_kth_loop(Idx, K, Bit bsr 1, BitArr, Size)
    end.
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @inf 1_000_000_000
  @neg_inf -1_000_000_000

  @spec get_results(queries :: [[integer]]) :: [boolean]
  def get_results(queries) do
    max_coord =
      queries
      |> Enum.map(fn q ->
        case q do
          [1, x] -> x
          [2, x, _sz] -> x
        end
      end)
      |> Enum.max()

    n = max_coord + 1
    size = next_pow2(n)

    # segment tree stored as {size, array}
    seg =
      :array.new(size * 2, @neg_inf)
      |> :array.set(size + 0, @inf)

    seg_tree = {size, seg}
    obstacles = :ordsets.from_list([0])

    {_obs, _seg, results} =
      Enum.reduce(queries, {obstacles, seg_tree, []}, fn q, {obs_set, segt, acc} ->
        case q do
          [1, x] ->
            p = x

            {less, greater_or_equal} = :ordsets.split(p, obs_set)

            prev =
              case less do
                [] -> 0
                _ -> Enum.max(less)
              end

            succ =
              case greater_or_equal do
                [] -> @inf
                [h | _] -> h
              end

            segt = point_update(segt, prev, p - prev)

            new_len_p =
              if succ == @inf do
                @inf
              else
                succ - p
              end

            segt = point_update(segt, p, new_len_p)
            obs_set = :ordsets.add_element(p, obs_set)
            {obs_set, segt, acc}

          [2, x, sz] ->
            if sz > x do
              {obs_set, segt, [false | acc]}
            else
              limit = x - sz

              max_len =
                range_query(segt, 0, limit)

              ok = max_len >= sz
              {obs_set, segt, [ok | acc]}
            end
        end
      end)

    Enum.reverse(results)
  end

  # helper to compute smallest power of two >= n
  defp next_pow2(n), do: next_pow2(1, n)
  defp next_pow2(pow, n) when pow >= n, do: pow
  defp next_pow2(pow, n), do: next_pow2(pow * 2, n)

  # point update: set position pos to value val
  defp point_update({size, arr}, pos, val) do
    idx = size + pos
    arr1 = :array.set(idx, val, arr)
    propagate_up(size, idx >>> 1, arr1)
  end

  defp propagate_up(_size, 0, arr), do: {_size, arr}
  defp propagate_up(size, i, arr) do
    left = :array.get(i * 2, arr)
    right = :array.get(i * 2 + 1, arr)
    maxv = if left > right, do: left, else: right
    arr2 = :array.set(i, maxv, arr)
    propagate_up(size, i >>> 1, arr2)
  end

  # range maximum query on [l, r] inclusive
  defp range_query({size, arr}, l, r) when l <= r do
    l0 = l + size
    r0 = r + size
    do_range_query(l0, r0, @neg_inf, arr)
  end

  defp do_range_query(l, r, acc, arr) when l > r, do: acc

  defp do_range_query(l, r, acc, arr) do
    acc1 =
      if Bitwise.band(l, 1) == 1 do
        max(acc, :array.get(l, arr))
      else
        acc
      end

    acc2 =
      if Bitwise.band(r, 1) == 0 do
        max(acc1, :array.get(r, arr))
      else
        acc1
      end

    l_next = (l + 1) >>> 1
    r_next = (r - 1) >>> 1
    do_range_query(l_next, r_next, acc2, arr)
  end
end
```

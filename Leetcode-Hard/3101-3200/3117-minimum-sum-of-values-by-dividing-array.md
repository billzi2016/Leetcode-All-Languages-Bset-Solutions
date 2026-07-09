# 3117. Minimum Sum of Values by Dividing Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumValueSum(vector<int>& nums, vector<int>& andValues) {
        int n = nums.size();
        int m = andValues.size();
        const long long INF = (1LL<<60);
        vector<long long> dpPrev(n+1, INF), dpCurr(n+1, INF);
        dpPrev[0] = 0;
        
        for (int segIdx = 0; segIdx < m; ++segIdx) {
            int sz = n + 1;
            vector<long long> seg(4*sz, INF);
            
            function<void(int,int,int)> build = [&](int node, int l, int r){
                if(l == r){ seg[node] = dpPrev[l]; return; }
                int mid = (l+r)/2;
                build(node<<1, l, mid);
                build(node<<1|1, mid+1, r);
                seg[node] = min(seg[node<<1], seg[node<<1|1]);
            };
            function<long long(int,int,int,int,int)> query = [&](int node, int l, int r, int ql, int qr)->long long{
                if(ql > r || qr < l) return INF;
                if(ql <= l && r <= qr) return seg[node];
                int mid = (l+r)/2;
                return min(query(node<<1, l, mid, ql, qr),
                           query(node<<1|1, mid+1, r, ql, qr));
            };
            build(1, 0, sz-1);
            
            vector<pair<int,int>> cur; // (andValue, earliest start)
            for (int i = 0; i < n; ++i) {
                vector<pair<int,int>> nxt;
                nxt.reserve(cur.size() + 1);
                nxt.push_back({nums[i], i});
                for (auto &p : cur) {
                    int newVal = p.first & nums[i];
                    if (newVal == nxt.back().first) {
                        nxt.back().second = min(nxt.back().second, p.second);
                    } else {
                        nxt.push_back({newVal, p.second});
                    }
                }
                cur.swap(nxt);
                
                int target = andValues[segIdx];
                long long best = INF;
                for (size_t k = 0; k < cur.size(); ++k) {
                    if (cur[k].first == target) {
                        int L = cur[k].second;
                        int R = (k + 1 < cur.size()) ? cur[k+1].second - 1 : i;
                        if (L <= R) {
                            long long q = query(1, 0, sz-1, L, R);
                            if (q != INF) best = min(best, q + nums[i]);
                        }
                        break;
                    }
                }
                dpCurr[i+1] = best;
            }
            
            dpPrev.assign(n+1, INF);
            for (int i = 0; i <= n; ++i) dpPrev[i] = dpCurr[i];
            fill(dpCurr.begin(), dpCurr.end(), INF);
        }
        
        long long ans = dpPrev[n];
        return (ans >= INF/2) ? -1 : static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final long INF = Long.MAX_VALUE / 4;

    public int minimumValueSum(int[] nums, int[] andValues) {
        int n = nums.length;
        int m = andValues.length;
        long[] dpPrev = new long[n + 1];
        java.util.Arrays.fill(dpPrev, INF);
        dpPrev[0] = 0;

        for (int k = 1; k <= m; ++k) {
            int target = andValues[k - 1];
            long[] dpCurr = new long[n + 1];
            java.util.Arrays.fill(dpCurr, INF);

            SegTree seg = new SegTree(dpPrev);
            java.util.List<Pair> prevList = new java.util.ArrayList<>();

            for (int r = 0; r < n; ++r) {
                java.util.List<Pair> cur = new java.util.ArrayList<>();
                // subarray consisting only of nums[r]
                cur.add(new Pair(nums[r], r));

                for (Pair p : prevList) {
                    int v = p.val & nums[r];
                    if (cur.get(cur.size() - 1).val == v) {
                        // keep earliest start index
                        cur.get(cur.size() - 1).start = Math.min(cur.get(cur.size() - 1).start, p.start);
                    } else {
                        cur.add(new Pair(v, p.start));
                    }
                }

                for (int i = 0; i < cur.size(); ++i) {
                    Pair e = cur.get(i);
                    if (e.val == target) {
                        int left = e.start;
                        int right = (i == 0) ? r : cur.get(i - 1).start - 1;
                        long best = seg.query(left, right);
                        if (best != INF) {
                            dpCurr[r + 1] = Math.min(dpCurr[r + 1], best + nums[r]);
                        }
                    }
                }

                prevList = cur;
            }

            dpPrev = dpCurr;
        }

        long ans = dpPrev[n];
        return ans >= INF / 2 ? -1 : (int) ans;
    }

    private static class Pair {
        int val;
        int start; // earliest start index for this AND value ending at current r

        Pair(int v, int s) {
            this.val = v;
            this.start = s;
        }
    }

    private static class SegTree {
        private final int n;
        private final long[] tree;

        SegTree(long[] arr) {
            this.n = arr.length;
            this.tree = new long[4 * n];
            build(1, 0, n - 1, arr);
        }

        private void build(int node, int l, int r, long[] arr) {
            if (l == r) {
                tree[node] = arr[l];
                return;
            }
            int mid = (l + r) >>> 1;
            build(node << 1, l, mid, arr);
            build(node << 1 | 1, mid + 1, r, arr);
            tree[node] = Math.min(tree[node << 1], tree[node << 1 | 1]);
        }

        long query(int left, int right) {
            if (left > right) return INF;
            return query(1, 0, n - 1, left, right);
        }

        private long query(int node, int l, int r, int ql, int qr) {
            if (qr < l || r < ql) return INF;
            if (ql <= l && r <= qr) return tree[node];
            int mid = (l + r) >>> 1;
            long leftMin = query(node << 1, l, mid, ql, qr);
            long rightMin = query(node << 1 | 1, mid + 1, r, ql, qr);
            return Math.min(leftMin, rightMin);
        }
    }
}
```

## Python

```python
class Solution(object):
    def minimumValueSum(self, nums, andValues):
        """
        :type nums: List[int]
        :type andValues: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(andValues)
        INF = 10 ** 18

        # segment tree for range minimum query
        class SegTree:
            __slots__ = ('N', 'data')
            def __init__(self, size):
                N = 1
                while N < size:
                    N <<= 1
                self.N = N
                self.data = [INF] * (2 * N)

            def update(self, idx, val):
                i = idx + self.N
                self.data[i] = val
                i >>= 1
                while i:
                    left = self.data[i << 1]
                    right = self.data[(i << 1) | 1]
                    self.data[i] = left if left <= right else right
                    i >>= 1

            def query(self, l, r):
                if l > r:
                    return INF
                l += self.N
                r += self.N
                res = INF
                while l <= r:
                    if l & 1:
                        if self.data[l] < res:
                            res = self.data[l]
                        l += 1
                    if not (r & 1):
                        if self.data[r] < res:
                            res = self.data[r]
                        r -= 1
                    l >>= 1
                    r >>= 1
                return res

        # dp[i][j]: min sum for first i elements split into j parts
        dp = [[INF] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        segs = [SegTree(n + 1) for _ in range(m + 1)]
        segs[0].update(0, 0)

        prev = []  # list of (and_value, start_index)
        for i in range(1, n + 1):
            x = nums[i - 1]
            cur = [(x, i - 1)]
            for val, st in prev:
                new_val = val & x
                if cur[-1][0] == new_val:
                    # keep earlier (smaller) start index
                    cur[-1] = (new_val, st)
                else:
                    cur.append((new_val, st))

            intervals = {}
            for idx, (val, start_earliest) in enumerate(cur):
                if idx == 0:
                    max_start = i - 1
                else:
                    max_start = cur[idx - 1][1] - 1
                intervals[val] = (start_earliest, max_start)

            for j in range(1, m + 1):
                target = andValues[j - 1]
                if target in intervals:
                    l, r_range = intervals[target]
                    best = segs[j - 1].query(l, r_range)
                    if best < INF:
                        dp[i][j] = best + x

            for j in range(m + 1):
                val = dp[i][j]
                if val < INF:
                    segs[j].update(i, val)

            prev = cur

        ans = dp[n][m]
        return -1 if ans >= INF else ans
```

## Python3

```python
import sys
from typing import List

INF = 10**18

class SegTree:
    def __init__(self, data, func, default):
        n = len(data)
        size = 1
        while size < n:
            size <<= 1
        self.N = size
        self.func = func
        self.default = default
        self.tree = [default] * (2 * size)
        for i in range(n):
            self.tree[size + i] = data[i]
        for i in range(size - 1, 0, -1):
            self.tree[i] = func(self.tree[i << 1], self.tree[(i << 1) | 1])

    def query(self, l, r):  # inclusive
        if l > r:
            return self.default
        l += self.N
        r += self.N
        res_left = self.default
        res_right = self.default
        while l <= r:
            if l & 1:
                res_left = self.func(res_left, self.tree[l])
                l += 1
            if not (r & 1):
                res_right = self.func(self.tree[r], res_right)
                r -= 1
            l >>= 1
            r >>= 1
        return self.func(res_left, res_right)

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)

        # segment tree for range AND queries
        seg_and = SegTree(nums, lambda a, b: a & b, (1 << 30) - 1)

        dp_prev = [INF] * (n + 1)
        dp_prev[0] = 0

        for idx in range(m):
            target = andValues[idx]
            # segment tree for min over dp_prev
            seg_min = SegTree(dp_prev, min, INF)
            dp_cur = [INF] * (n + 1)

            for i in range(1, n + 1):
                r = i - 1

                # find leftmost L where AND(L..r) <= target
                lo, hi = 0, r
                while lo < hi:
                    mid = (lo + hi) // 2
                    if seg_and.query(mid, r) < target:
                        lo = mid + 1
                    else:
                        hi = mid
                L = lo
                if seg_and.query(L, r) != target:
                    continue

                # find first position P where AND(P..r) < target
                lo, hi = 0, r
                while lo < hi:
                    mid = (lo + hi) // 2
                    if seg_and.query(mid, r) < target:
                        hi = mid
                    else:
                        lo = mid + 1
                P = lo
                if P <= r and seg_and.query(P, r) < target:
                    R = P - 1
                else:
                    R = r

                # query minimum dp_prev over [L, R]
                best = seg_min.query(L, R)
                if best != INF:
                    dp_cur[i] = best + nums[r]

            dp_prev = dp_cur

        ans = dp_prev[n]
        return -1 if ans >= INF else ans
```

## C

```c
#include <limits.h>
#include <stddef.h>

#define MAXN 10005
#define MAXK 20
#define INFLL 1000000000000LL

static int cntArr[MAXN];
static int valArr[MAXN][MAXK];
static int leftArr[MAXN][MAXK];
static int rightArr[MAXN][MAXK];

static long long dpPrev[MAXN + 1];
static long long dpCurr[MAXN + 1];

static long long segTree[32768]; // enough for 2 * next power of two (<= 2*16384)
static int segSize;

/* build segment tree for array arr of length N */
static void buildSeg(long long *arr, int N) {
    segSize = 1;
    while (segSize < N) segSize <<= 1;
    for (int i = 0; i < 2 * segSize; ++i) segTree[i] = INFLL;
    for (int i = 0; i < N; ++i) segTree[segSize + i] = arr[i];
    for (int i = segSize - 1; i > 0; --i)
        segTree[i] = segTree[i << 1] < segTree[(i << 1) | 1] ? segTree[i << 1] : segTree[(i << 1) | 1];
}

/* query minimum on inclusive range [l, r] */
static long long querySeg(int l, int r) {
    if (l > r) return INFLL;
    l += segSize;
    r += segSize;
    long long res = INFLL;
    while (l <= r) {
        if (l & 1) {
            if (segTree[l] < res) res = segTree[l];
            ++l;
        }
        if (!(r & 1)) {
            if (segTree[r] < res) res = segTree[r];
            --r;
        }
        l >>= 1;
        r >>= 1;
    }
    return res;
}

int minimumValueSum(int* nums, int numsSize, int* andValues, int andValuesSize) {
    int n = numsSize;
    int m = andValuesSize;

    /* pre‑compute intervals of equal AND values for each ending position */
    int curVal[MAXK], curL[MAXK];
    int sz = 0;
    for (int i = 0; i < n; ++i) {
        int newVal[MAXK];
        int newL[MAXK];
        int ns = 0;

        newVal[ns] = nums[i];
        newL[ns] = i;
        ++ns;

        for (int p = 0; p < sz; ++p) {
            int v = curVal[p] & nums[i];
            int lpos = curL[p];
            if (ns > 0 && newVal[ns - 1] == v) {
                if (lpos < newL[ns - 1]) newL[ns - 1] = lpos;
            } else {
                newVal[ns] = v;
                newL[ns] = lpos;
                ++ns;
            }
        }

        cntArr[i] = ns;
        for (int k = 0; k < ns; ++k) {
            valArr[i][k] = newVal[k];
            leftArr[i][k] = newL[k];
            if (k == 0) rightArr[i][k] = i;
            else rightArr[i][k] = newL[k - 1] - 1;
        }

        sz = ns;
        for (int p = 0; p < sz; ++p) {
            curVal[p] = newVal[p];
            curL[p] = newL[p];
        }
    }

    /* DP initialization */
    for (int i = 0; i <= n; ++i) dpPrev[i] = INFLL;
    dpPrev[0] = 0;

    for (int j = 1; j <= m; ++j) {
        buildSeg(dpPrev, n + 1);

        for (int i = 0; i <= n; ++i) dpCurr[i] = INFLL;
        int target = andValues[j - 1];

        for (int i = 0; i < n; ++i) {
            long long bestPrev = INFLL;
            for (int k = 0; k < cntArr[i]; ++k) {
                if (valArr[i][k] == target) {
                    int l = leftArr[i][k];
                    int r = rightArr[i][k];
                    bestPrev = querySeg(l, r);
                    break;
                }
            }
            if (bestPrev != INFLL) dpCurr[i + 1] = bestPrev + nums[i];
        }

        for (int i = 0; i <= n; ++i) dpPrev[i] = dpCurr[i];
    }

    long long ans = dpPrev[n];
    return (ans >= INFLL / 2) ? -1 : (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long INF = (1L << 60);

    public int MinimumValueSum(int[] nums, int[] andValues) {
        int n = nums.Length;
        int m = andValues.Length;

        long[] dpPrev = new long[n + 1];
        for (int i = 0; i <= n; i++) dpPrev[i] = INF;
        dpPrev[0] = 0; // 0 elements with 0 segments

        for (int seg = 1; seg <= m; seg++) {
            long[] dpCurr = new long[n + 1];
            for (int i = 0; i <= n; i++) dpCurr[i] = INF;

            // Build segment tree over dpPrev
            SegTree st = new SegTree(dpPrev);

            List<(int val, int left)> cur = new List<(int, int)>();

            int target = andValues[seg - 1];

            for (int i = 1; i <= n; i++) {
                // update list of AND values for subarrays ending at i-1
                List<(int val, int left)> nxt = new List<(int, int)>();
                nxt.Add((nums[i - 1], i - 1)); // subarray of length 1

                foreach (var p in cur) {
                    int newVal = p.val & nums[i - 1];
                    var last = nxt[nxt.Count - 1];
                    if (last.val == newVal) {
                        // merge, keep earliest left index
                        nxt[nxt.Count - 1] = (last.val, Math.Min(last.left, p.left));
                    } else {
                        nxt.Add((newVal, p.left));
                    }
                }

                cur = nxt;

                // evaluate dpCurr[i]
                for (int idx = 0; idx < cur.Count; idx++) {
                    if (cur[idx].val != target) continue;
                    int l = cur[idx].left; // inclusive start index
                    int r = (idx == 0) ? i - 1 : cur[idx - 1].left - 1;
                    long bestPrev = st.Query(l, r);
                    if (bestPrev < INF) {
                        dpCurr[i] = Math.Min(dpCurr[i], bestPrev + nums[i - 1]);
                    }
                }
            }

            dpPrev = dpCurr;
        }

        long ans = dpPrev[n];
        return ans >= INF ? -1 : (int)ans;
    }

    // Simple iterative segment tree for range minimum query
    private class SegTree {
        private readonly int size;
        private readonly long[] tree;

        public SegTree(long[] data) {
            size = data.Length;
            tree = new long[2 * size];
            for (int i = 0; i < size; i++) tree[size + i] = data[i];
            for (int i = size - 1; i > 0; i--) tree[i] = Math.Min(tree[i << 1], tree[i << 1 | 1]);
        }

        // query minimum on inclusive range [l, r]
        public long Query(int l, int r) {
            if (l > r) return INF;
            long res = INF;
            for (l += size, r += size; l <= r; l >>= 1, r >>= 1) {
                if ((l & 1) == 1) {
                    res = Math.Min(res, tree[l]);
                    l++;
                }
                if ((r & 1) == 0) {
                    res = Math.Min(res, tree[r]);
                    r--;
                }
            }
            return res;
        }
    }
}
```

## Javascript

```javascript
/****
 * @param {number[]} nums
 * @param {number[]} andValues
 * @return {number}
 */
var minimumValueSum = function(nums, andValues) {
    const n = nums.length;
    const m = andValues.length;
    // precompute logs
    const log = new Array(n + 1);
    log[0] = 0;
    log[1] = 0;
    for (let i = 2; i <= n; ++i) {
        log[i] = log[(i >> 1)] + 1;
    }
    // build sparse table for range AND
    const K = log[n] + 1;
    const st = Array.from({ length: K }, () => new Array(n));
    for (let i = 0; i < n; ++i) st[0][i] = nums[i];
    for (let k = 1; k < K; ++k) {
        const len = 1 << k;
        const half = len >> 1;
        for (let i = 0; i + len <= n; ++i) {
            st[k][i] = st[k - 1][i] & st[k - 1][i + half];
        }
    }
    function rangeAnd(l, r) { // inclusive, 0‑based
        const len = r - l + 1;
        const k = log[len];
        return st[k][l] & st[k][r - (1 << k) + 1];
    }

    class SegTree {
        constructor(arr) {
            this.n = arr.length;
            let size = 1;
            while (size < this.n) size <<= 1;
            this.size = size;
            this.tree = new Array(2 * size).fill(Infinity);
            for (let i = 0; i < this.n; ++i) this.tree[size + i] = arr[i];
            for (let i = size - 1; i > 0; --i) {
                this.tree[i] = Math.min(this.tree[i << 1], this.tree[(i << 1) | 1]);
            }
        }
        query(l, r) { // inclusive
            if (l > r) return Infinity;
            l += this.size;
            r += this.size;
            let res = Infinity;
            while (l <= r) {
                if ((l & 1) === 1) {
                    res = Math.min(res, this.tree[l]);
                    ++l;
                }
                if ((r & 1) === 0) {
                    res = Math.min(res, this.tree[r]);
                    --r;
                }
                l >>= 1;
                r >>= 1;
            }
            return res;
        }
    }

    let dpPrev = new Array(n + 1).fill(Infinity);
    dpPrev[0] = 0;

    for (let segIdx = 0; segIdx < m; ++segIdx) {
        const target = andValues[segIdx];
        const dpCurr = new Array(n + 1).fill(Infinity);
        const segTree = new SegTree(dpPrev);

        for (let i = 1; i <= n; ++i) { // i is length of prefix, right endpoint = i-1
            const r = i - 1;

            // find leftmost start L0 (0‑based) where AND(L0..r) >= target
            let lo = 0, hi = r;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (rangeAnd(mid, r) < target) lo = mid + 1;
                else hi = mid;
            }
            const L0 = lo;
            if (rangeAnd(L0, r) !== target) continue; // no valid start

            // find first index > L0 where AND > target
            let low = L0, high = r + 1; // exclusive upper bound
            while (low < high) {
                const mid = (low + high) >> 1;
                if (mid === r + 1) { low = mid; break; }
                const val = rangeAnd(mid, r);
                if (val > target) high = mid;
                else low = mid + 1;
            }
            const R0 = low - 1; // last start where AND == target

            const leftPos = L0 + 1;   // convert to 1‑based start index
            const rightPos = R0 + 1;

            const minPrev = segTree.query(leftPos - 1, rightPos - 1);
            if (minPrev === Infinity) continue;
            dpCurr[i] = minPrev + nums[i - 1];
        }
        dpPrev = dpCurr;
    }

    const ans = dpPrev[n];
    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function minimumValueSum(nums: number[], andValues: number[]): number {
    const n = nums.length;
    const m = andValues.length;
    const INF = Number.MAX_SAFE_INTEGER;

    // Precompute distinct AND values for subarrays ending at each position
    interface Pair { val: number; left: number; }
    const allPairs: Pair[][] = new Array(n);
    let prev: Pair[] = [];
    for (let i = 0; i < n; i++) {
        const cur: Pair[] = [{ val: nums[i], left: i }];
        for (const p of prev) {
            const newVal = p.val & nums[i];
            if (cur[cur.length - 1].val === newVal) {
                // keep the earliest (minimum) left index
                cur[cur.length - 1].left = Math.min(cur[cur.length - 1].left, p.left);
            } else {
                cur.push({ val: newVal, left: p.left });
            }
        }
        allPairs[i] = cur;
        prev = cur;
    }

    // DP over segments
    let dpPrev = new Array(n + 1).fill(INF);
    dpPrev[0] = 0;

    for (let seg = 1; seg <= m; seg++) {
        const target = andValues[seg - 1];
        const dpCurr = new Array(n + 1).fill(INF);

        // monotonic queue for sliding window minimum
        const dqIdx: number[] = [];
        const dqVal: number[] = [];
        let head = 0;
        let nextToAdd = 0; // next index (prev) to insert into deque

        for (let i = 1; i <= n; i++) {
            const pairs = allPairs[i - 1];
            let L = -1, R = -2; // invalid defaults
            for (let k = 0; k < pairs.length; k++) {
                if (pairs[k].val === target) {
                    L = pairs[k].left;
                    R = (k === 0 ? i - 1 : pairs[k - 1].left - 1);
                    break;
                }
            }

            // add new candidates up to R
            while (nextToAdd <= R && nextToAdd < i) {
                const val = dpPrev[nextToAdd];
                if (val < INF) {
                    while (dqIdx.length > head && dqVal[dqVal.length - 1] >= val) {
                        dqIdx.pop();
                        dqVal.pop();
                    }
                    dqIdx.push(nextToAdd);
                    dqVal.push(val);
                }
                nextToAdd++;
            }

            // remove indices less than L
            while (dqIdx.length > head && dqIdx[head] < L) {
                head++;
            }

            if (L <= R && dqIdx.length > head) {
                dpCurr[i] = dqVal[head] + nums[i - 1];
            } else {
                dpCurr[i] = INF;
            }
        }

        dpPrev = dpCurr;
    }

    const ans = dpPrev[n];
    return ans >= INF ? -1 : ans;
}
```

## Php

```php
class SegmentTree {
    private int $size;
    private array $tree;

    public function __construct(array $arr) {
        $this->size = count($arr);
        $this->tree = array_fill(0, 4 * $this->size, PHP_INT_MAX);
        $this->build(1, 0, $this->size - 1, $arr);
    }

    private function build(int $node, int $l, int $r, array $arr): void {
        if ($l === $r) {
            $this->tree[$node] = $arr[$l];
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->build($node * 2, $l, $mid, $arr);
        $this->build($node * 2 + 1, $mid + 1, $r, $arr);
        $this->tree[$node] = min($this->tree[$node * 2], $this->tree[$node * 2 + 1]);
    }

    public function queryRange(int $l, int $r): int {
        if ($l > $r) return PHP_INT_MAX;
        return $this->query(1, 0, $this->size - 1, $l, $r);
    }

    private function query(int $node, int $nl, int $nr, int $l, int $r): int {
        if ($l <= $nl && $nr <= $r) return $this->tree[$node];
        if ($nr < $l || $nl > $r) return PHP_INT_MAX;
        $mid = intdiv($nl + $nr, 2);
        $left = $this->query($node * 2, $nl, $mid, $l, $r);
        $right = $this->query($node * 2 + 1, $mid + 1, $nr, $l, $r);
        return min($left, $right);
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $andValues
     * @return Integer
     */
    function minimumValueSum($nums, $andValues) {
        $n = count($nums);
        $m = count($andValues);
        $INF = 10 ** 18;

        // Preprocess intervals for each ending index i and each possible AND value.
        $intervals = array_fill(0, $n, []);
        $prevList = []; // list of [andValue, startPos] for subarrays ending at i-1

        for ($i = 0; $i < $n; ++$i) {
            $curr = [];
            // subarray consisting only of nums[i]
            $curr[] = [$nums[$i], $i];
            foreach ($prevList as $pair) {
                $newVal = $pair[0] & $nums[$i];
                if ($newVal == $curr[count($curr) - 1][0]) {
                    // merge, keep earlier start
                    if ($pair[1] < $curr[count($curr) - 1][1]) {
                        $curr[count($curr) - 1][1] = $pair[1];
                    }
                } else {
                    $curr[] = [$newVal, $pair[1]];
                }
            }

            $len = count($curr);
            for ($idx = 0; $idx < $len; ++$idx) {
                $val = $curr[$idx][0];
                $l = $curr[$idx][1];
                if ($idx + 1 < $len) {
                    $r = $curr[$idx + 1][1] - 1;
                } else {
                    $r = $i;
                }
                $intervals[$i][$val] = [$l, $r];
            }

            $prevList = $curr;
        }

        // DP initialization
        $dpPrev = array_fill(0, $n + 1, $INF);
        $dpPrev[0] = 0;

        for ($seg = 1; $seg <= $m; ++$seg) {
            $target = $andValues[$seg - 1];
            // Build segment tree over dpPrev
            $segTree = new SegmentTree($dpPrev);
            $dpCurr = array_fill(0, $n + 1, $INF);

            for ($i = 0; $i < $n; ++$i) {
                if (!isset($intervals[$i][$target])) continue;
                [$l, $r] = $intervals[$i][$target];
                // query minimum dpPrev over start positions [l, r]
                $minPrev = $segTree->queryRange($l, $r);
                if ($minPrev >= $INF) continue;
                $candidate = $minPrev + $nums[$i];
                if ($candidate < $dpCurr[$i + 1]) {
                    $dpCurr[$i + 1] = $candidate;
                }
            }

            $dpPrev = $dpCurr;
        }

        $ans = $dpPrev[$n];
        return ($ans >= $INF) ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    private let INF = Int.max / 4

    private class SegmentTree {
        private var size: Int
        private var tree: [Int]
        init(_ data: [Int], _ INF: Int) {
            var n = data.count
            size = 1
            while size < n { size <<= 1 }
            tree = Array(repeating: INF, count: 2 * size)
            for i in 0..<n {
                tree[size + i] = data[i]
            }
            if size > 0 {
                for i in stride(from: size - 1, through: 1, by: -1) {
                    tree[i] = min(tree[2 * i], tree[2 * i + 1])
                }
            }
        }
        func query(_ l: Int, _ r: Int) -> Int {
            var left = l + size
            var right = r + size
            var res = INF
            while left <= right {
                if (left & 1) == 1 {
                    res = min(res, tree[left])
                    left += 1
                }
                if (right & 1) == 0 {
                    res = min(res, tree[right])
                    right -= 1
                }
                left >>= 1
                right >>= 1
            }
            return res
        }
    }

    func minimumValueSum(_ nums: [Int], _ andValues: [Int]) -> Int {
        let n = nums.count
        let m = andValues.count
        if m > n { return -1 }

        var dpPrev = Array(repeating: INF, count: n + 1)
        dpPrev[0] = 0

        for k in 1...m {
            // build segment tree over dpPrev
            let seg = SegmentTree(dpPrev, INF)

            var dpCurr = Array(repeating: INF, count: n + 1)
            var curList: [(value: Int, start: Int)] = []

            for i in 1...n {
                // update list of AND values for subarrays ending at i-1
                var nxt: [(value: Int, start: Int)] = []
                nxt.append((nums[i - 1], i - 1))
                for pair in curList {
                    let newVal = pair.value & nums[i - 1]
                    if nxt[nxt.count - 1].value == newVal {
                        if pair.start < nxt[nxt.count - 1].start {
                            nxt[nxt.count - 1].start = pair.start
                        }
                    } else {
                        nxt.append((newVal, pair.start))
                    }
                }
                curList = nxt

                // find interval where AND equals target
                let target = andValues[k - 1]
                var L: Int? = nil
                var R: Int? = nil
                for idx in 0..<curList.count {
                    if curList[idx].value == target {
                        L = curList[idx].start
                        if idx + 1 < curList.count {
                            R = curList[idx + 1].start - 1
                        } else {
                            R = i - 1
                        }
                        break
                    }
                }

                if let l = L, let r = R {
                    let best = seg.query(l, r)
                    if best < INF {
                        dpCurr[i] = best + nums[i - 1]
                    }
                }
            }

            dpPrev = dpCurr
        }

        let ans = dpPrev[n]
        return ans >= INF ? -1 : ans
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import kotlin.math.min

class Solution {
    fun minimumValueSum(nums: IntArray, andValues: IntArray): Int {
        val n = nums.size
        val m = andValues.size
        val INF = 1_000_000_007
        var dpPrev = IntArray(n + 1) { INF }
        dpPrev[0] = 0

        for (k in 1..m) {
            val target = andValues[k - 1]
            val dpCurr = IntArray(n + 1) { INF }

            var curAndList = ArrayList<Pair<Int, Int>>() // pair of (andValue, earliestStart)
            val deque: ArrayDeque<Int> = ArrayDeque()
            var curRight = -1

            for (i in 1..n) {
                // update list of distinct AND values for subarrays ending at i
                val newList = ArrayList<Pair<Int, Int>>()
                newList.add(Pair(nums[i - 1], i))
                var lastVal = nums[i - 1]
                for (p in curAndList) {
                    val v = p.first and nums[i - 1]
                    if (v == lastVal) {
                        val prev = newList[newList.size - 1]
                        newList[newList.size - 1] = Pair(v, min(prev.second, p.second))
                    } else {
                        newList.add(Pair(v, p.second))
                        lastVal = v
                    }
                }
                curAndList = newList

                // find interval of start positions where AND equals target
                var L = -1
                var R = -1
                for (idx in curAndList.indices) {
                    if (curAndList[idx].first == target) {
                        L = curAndList[idx].second
                        R = if (idx + 1 < curAndList.size) curAndList[idx + 1].second - 1 else i
                        break
                    }
                }

                if (L != -1) {
                    val leftIdx = L - 1
                    val rightIdx = R - 1

                    // extend deque to include new right indices
                    while (curRight < rightIdx) {
                        curRight++
                        val value = dpPrev[curRight]
                        while (!deque.isEmpty() && dpPrev[deque.peekLast()] >= value) {
                            deque.pollLast()
                        }
                        deque.addLast(curRight)
                    }

                    // remove indices that are left of the window
                    while (!deque.isEmpty() && deque.peekFirst() < leftIdx) {
                        deque.pollFirst()
                    }

                    if (!deque.isEmpty()) {
                        val minPrev = dpPrev[deque.peekFirst()]
                        if (minPrev < INF) {
                            dpCurr[i] = minPrev + nums[i - 1]
                        }
                    }
                }
            }
            dpPrev = dpCurr
        }

        val ans = dpPrev[n]
        return if (ans >= INF) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  static const int _INF = 1 << 60;

  int minimumValueSum(List<int> nums, List<int> andValues) {
    final int n = nums.length;
    final int m = andValues.length;
    List<int> dpPrev = List.filled(n + 1, _INF);
    dpPrev[0] = 0;

    for (int seg = 1; seg <= m; seg++) {
      // segment tree over dpPrev
      final SegTree st = SegTree(dpPrev);
      List<int> dpCurr = List.filled(n + 1, _INF);

      List<_Pair> prevList = <_Pair>[];
      for (int i = 0; i < n; i++) {
        // build current list of distinct AND values for suffixes ending at i
        List<_Pair> cur = <_Pair>[];
        cur.add(_Pair(nums[i], i));
        for (final _Pair p in prevList) {
          final int v = p.val & nums[i];
          if (cur.last.val == v) {
            // keep the earliest start index (smaller)
            if (p.start < cur.last.start) cur.last.start = p.start;
          } else {
            cur.add(_Pair(v, p.start));
          }
        }

        final int target = andValues[seg - 1];
        int left = -1, right = -1;
        for (int k = 0; k < cur.length; k++) {
          if (cur[k].val == target) {
            left = cur[k].start;
            if (k == 0) {
              right = i;
            } else {
              right = cur[k - 1].start - 1;
            }
            break;
          }
        }

        if (left != -1 && left <= right) {
          final int minPrev = st.query(left, right);
          if (minPrev < _INF) {
            dpCurr[i + 1] = minPrev + nums[i];
          }
        }

        prevList = cur;
      }

      dpPrev = dpCurr;
    }

    final int ans = dpPrev[n];
    return ans >= _INF ? -1 : ans;
  }
}

class _Pair {
  int val;
  int start;
  _Pair(this.val, this.start);
}

class SegTree {
  late List<int> _tree;
  late int _size;

  SegTree(List<int> arr) {
    _size = arr.length;
    _tree = List.filled(_size * 2, Solution._INF);
    for (int i = 0; i < _size; i++) {
      _tree[_size + i] = arr[i];
    }
    for (int i = _size - 1; i > 0; i--) {
      _tree[i] = _tree[i << 1] < _tree[(i << 1) | 1]
          ? _tree[i << 1]
          : _tree[(i << 1) | 1];
    }
  }

  int query(int l, int r) {
    if (l > r) return Solution._INF;
    l += _size;
    r += _size;
    int res = Solution._INF;
    while (l <= r) {
      if ((l & 1) == 1) {
        if (_tree[l] < res) res = _tree[l];
        l++;
      }
      if ((r & 1) == 0) {
        if (_tree[r] < res) res = _tree[r];
        r--;
      }
      l >>= 1;
      r >>= 1;
    }
    return res;
  }
}
```

## Golang

```go
func minimumValueSum(nums []int, andValues []int) int {
	const INF = 1 << 60

	n := len(nums)
	m := len(andValues)

	// dpPrev[i] = min sum for first i elements using processed segments
	dpPrev := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dpPrev[i] = INF
	}
	dpPrev[0] = 0

	for segIdx := 0; segIdx < m; segIdx++ {
		target := andValues[segIdx]

		// segment tree for range minimum queries on dpPrev
		st := newSegTree(dpPrev)

		dpCurr := make([]int, n+1)
		for i := 0; i <= n; i++ {
			dpCurr[i] = INF
		}

		prevMap := make(map[int][2]int) // value -> [minStart, maxStart]

		for i := 0; i < n; i++ {
			curMap := make(map[int][2]int)

			v := nums[i]
			curMap[v] = [2]int{i, i}

			for val, mm := range prevMap {
				newVal := val & v
				if existing, ok := curMap[newVal]; ok {
					if mm[0] < existing[0] {
						existing[0] = mm[0]
					}
					if mm[1] > existing[1] {
						existing[1] = mm[1]
					}
					curMap[newVal] = existing
				} else {
					curMap[newVal] = [2]int{mm[0], mm[1]}
				}
			}

			if interval, ok := curMap[target]; ok {
				L, R := interval[0], interval[1]
				best := st.query(L, R)
				if best < INF {
					dpCurr[i+1] = best + v
				}
			}
			prevMap = curMap
		}
		dpPrev = dpCurr
	}

	ans := dpPrev[n]
	if ans >= INF/2 {
		return -1
	}
	return ans
}

// segment tree for range minimum query (inclusive)
type segTree struct {
	size int
	data []int
}

func newSegTree(arr []int) *segTree {
	n := len(arr)
	size := 1
	for size < n {
		size <<= 1
	}
	data := make([]int, 2*size)
	const INF = 1 << 60
	for i := range data {
		data[i] = INF
	}
	for i := 0; i < n; i++ {
		data[size+i] = arr[i]
	}
	for i := size - 1; i > 0; i-- {
		if data[2*i] < data[2*i+1] {
			data[i] = data[2*i]
		} else {
			data[i] = data[2*i+1]
		}
	}
	return &segTree{size: size, data: data}
}

// query minimum on [l,r] inclusive
func (st *segTree) query(l, r int) int {
	const INF = 1 << 60
	if l > r {
		return INF
	}
	l += st.size
	r += st.size
	res := INF
	for l <= r {
		if l&1 == 1 {
			if st.data[l] < res {
				res = st.data[l]
			}
			l++
		}
		if r&1 == 0 {
			if st.data[r] < res {
				res = st.data[r]
			}
			r--
		}
		l >>= 1
		r >>= 1
	}
	return res
}
```

## Ruby

```ruby
INF = 1 << 60

class SegTree
  def initialize(arr)
    @n = arr.size
    @size = 1
    @size <<= 1 while @size < @n
    @tree = Array.new(@size * 2, INF)
    @n.times { |i| @tree[@size + i] = arr[i] }
    (@size - 1).downto(1) { |i| @tree[i] = [@tree[i << 1], @tree[(i << 1) + 1]].min }
  end

  def query(l, r)
    l += @size
    r += @size
    res = INF
    while l <= r
      if (l & 1) == 1
        res = [res, @tree[l]].min
        l += 1
      end
      if (r & 1) == 0
        res = [res, @tree[r]].min
        r -= 1
      end
      l >>= 1
      r >>= 1
    end
    res
  end
end

# @param {Integer[]} nums
# @param {Integer[]} and_values
# @return {Integer}
def minimum_value_sum(nums, and_values)
  n = nums.length
  m = and_values.length

  left = Array.new(n + 1) { Array.new(m, -1) }
  right = Array.new(n + 1) { Array.new(m, -1) }

  cur = []
  (1..n).each do |i|
    x = nums[i - 1]
    nxt = [[x, i - 1]]
    cur.each do |val, st|
      new_val = val & x
      if nxt[-1][0] == new_val
        nxt[-1][1] = [nxt[-1][1], st].min
      else
        nxt << [new_val, st]
      end
    end
    cur = nxt

    (0...m).each do |t|
      target = and_values[t]
      idx = nil
      cur.each_with_index do |pair, ii|
        if pair[0] == target
          idx = ii
          break
        end
      end
      if idx
        l = cur[idx][1]
        r = (idx + 1 < cur.size) ? cur[idx + 1][1] - 1 : i - 1
        left[i][t] = l
        right[i][t] = r
      else
        left[i][t] = -1
      end
    end
  end

  dp = Array.new(n + 1) { Array.new(m + 1, INF) }
  dp[0][0] = 0

  (1..m).each do |j|
    arr = dp.map { |row| row[j - 1] }
    seg = SegTree.new(arr)
    (1..n).each do |i|
      l = left[i][j - 1]
      next if l < 0
      r = right[i][j - 1]
      best_prev = seg.query(l, r)
      dp[i][j] = best_prev + nums[i - 1] if best_prev < INF
    end
  end

  ans = dp[n][m]
  ans >= INF ? -1 : ans
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

object Solution {
  private val INF: Long = Long.MaxValue / 4

  class SegmentTree(arr: Array[Long]) {
    private val n: Int = arr.length
    private val size: Int = {
      var s = 1
      while (s < n) s <<= 1
      s
    }
    private val tree: Array[Long] = Array.fill(2 * size)(INF)

    init()

    private def init(): Unit = {
      for (i <- 0 until n) tree(size + i) = arr(i)
      for (i <- size - 1 to 1 by -1) tree(i) = math.min(tree(2 * i), tree(2 * i + 1))
    }

    def query(l: Int, r: Int): Long = {
      var left = l + size
      var right = r + size
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

  def minimumValueSum(nums: Array[Int], andValues: Array[Int]): Int = {
    val n = nums.length
    val m = andValues.length

    // Precompute AND intervals for each ending position
    val andInfo = new Array[Array[(Int, Int)]](n)
    var prevList = List.empty[(Int, Int)]

    for (i <- 0 until n) {
      val curBuf = ArrayBuffer[(Int, Int)]()
      // subarray consisting of only nums[i]
      curBuf.append((nums(i), i))
      for ((v, start) <- prevList) {
        val newV = v & nums(i)
        if (curBuf.last._1 == newV) {
          // keep the earliest start
          if (start < curBuf.last._2) {
            curBuf.update(curBuf.size - 1, (newV, start))
          }
        } else {
          curBuf.append((newV, start))
        }
      }
      andInfo(i) = curBuf.toArray
      prevList = curBuf.toList
    }

    var dpPrev: Array[Long] = Array.fill(n + 1)(INF)
    dpPrev(0) = 0L

    for (segIdx <- 0 until m) {
      val target = andValues(segIdx)
      val segTree = new SegmentTree(dpPrev)
      val dpCurr = Array.fill[Long](n + 1)(INF)

      for (i <- 1 to n) {
        val list = andInfo(i - 1)
        var found = false
        var L = 0
        var R = 0
        var idx = 0
        while (idx < list.length && !found) {
          if (list(idx)._1 == target) {
            L = list(idx)._2
            if (idx + 1 < list.length) R = list(idx + 1)._2 - 1 else R = i - 1
            found = true
          }
          idx += 1
        }
        if (found) {
          val minPrev = segTree.query(L, R)
          if (minPrev != INF) {
            dpCurr(i) = minPrev + nums(i - 1).toLong
          }
        }
      }

      dpPrev = dpCurr
    }

    val ans = dpPrev(n)
    if (ans >= INF / 2) -1 else ans.toInt
  }
}
```

## Rust

```rust
use std::cmp::min;

struct SegTree {
    size: usize,
    data: Vec<i64>,
}

impl SegTree {
    const INF: i64 = 1_i64 << 60;
    fn new(n: usize) -> Self {
        let mut size = 1usize;
        while size < n {
            size <<= 1;
        }
        SegTree {
            size,
            data: vec![Self::INF; 2 * size],
        }
    }
    fn update(&mut self, mut pos: usize, val: i64) {
        pos += self.size;
        self.data[pos] = val;
        while pos > 1 {
            pos >>= 1;
            self.data[pos] = min(self.data[pos << 1], self.data[(pos << 1) | 1]);
        }
    }
    fn query(&self, mut l: usize, mut r: usize) -> i64 {
        if l > r {
            return Self::INF;
        }
        let mut res = Self::INF;
        l += self.size;
        r += self.size;
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
    pub fn minimum_value_sum(nums: Vec<i32>, and_values: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = and_values.len();
        const INF: i64 = 1_i64 << 60;

        // dp[pos][k] = min sum for first pos elements split into k parts
        let mut dp = vec![vec![INF; m + 1]; n + 1];
        dp[0][0] = 0;

        // segment trees for each k (0..=m) over dp[*][k]
        let mut segs: Vec<SegTree> = (0..=m).map(|_| SegTree::new(n + 1)).collect();
        segs[0].update(0, 0);

        // previous AND list for subarrays ending at i-1
        let mut prev: Vec<(i32, usize)> = Vec::new(); // (and_value, start_index)

        for i in 0..n {
            // build current AND list for subarrays ending at i
            let mut cur: Vec<(i32, usize)> = Vec::new();
            cur.push((nums[i], i));
            for &(val, start) in &prev {
                let new_val = val & nums[i];
                if let Some(last) = cur.last_mut() {
                    if last.0 == new_val {
                        if start < last.1 {
                            last.1 = start;
                        }
                    } else {
                        cur.push((new_val, start));
                    }
                }
            }

            // compute dp for each k using current intervals
            for k in 1..=m {
                let target = and_values[k - 1];
                let mut found = false;
                let (mut l_idx, mut r_idx) = (0usize, 0usize);
                for idx in 0..cur.len() {
                    if cur[idx].0 == target {
                        l_idx = cur[idx].1;
                        r_idx = if idx == 0 { i } else { cur[idx - 1].1 - 1 };
                        found = true;
                        break;
                    }
                }
                if found && l_idx <= r_idx {
                    let best = segs[k - 1].query(l_idx, r_idx);
                    if best < INF {
                        dp[i + 1][k] = min(dp[i + 1][k], best + nums[i] as i64);
                    }
                }
            }

            // update segment trees with newly computed dp values
            for k in 0..=m {
                segs[k].update(i + 1, dp[i + 1][k]);
            }

            prev = cur;
        }

        let ans = dp[n][m];
        if ans >= INF / 2 {
            -1
        } else {
            ans as i32
        }
    }
}
```

## Racket

```racket
(define (minimum-value-sum nums andValues)
  (let* ((n (length nums))
         (m (length andValues))
         (INF 1000000000000) ; sufficiently large
         ;; build for each position the list of distinct AND values with earliest start
         (and-lists (make-vector n)))
    (let loop ((i 0) (prev '()))
      (when (< i n)
        (define num (list-ref nums i))
        (define cur
          (foldl (lambda (p acc)
                   (define v (car p))
                   (define s (cdr p))
                   (define newv (bitwise-and v num))
                   (if (= newv (caar acc))
                       (cons (cons newv (min s (cdar acc))) (cdr acc))
                       (cons (cons newv s) acc)))
                 (list (cons num i))
                 prev))
        (vector-set! and-lists i cur)
        (loop (+ i 1) cur)))
    ;; segment tree helpers
    (define (build-segtree arr)
      (let* ((len (vector-length arr))
             (seg (make-vector (* 4 len) INF)))
        (define (build node l r)
          (if (= l r)
              (vector-set! seg node (vector-ref arr l))
              (let ((mid (quotient (+ l r) 2)))
                (build (* node 2) l mid)
                (build (+ (* node 2) 1) (+ mid 1) r)
                (vector-set! seg node
                             (min (vector-ref seg (* node 2))
                                  (vector-ref seg (+ (* node 2) 1)))))))
        (build 1 0 (- len 1))
        seg))
    (define (query-segtree seg node l r ql qr)
      (if (or (> ql r) (< qr l))
          INF
          (if (and (<= ql l) (>= qr r))
              (vector-ref seg node)
              (let ((mid (quotient (+ l r) 2)))
                (min (query-segtree seg (* node 2) l mid ql qr)
                     (query-segtree seg (+ (* node 2) 1) (+ mid 1) r ql qr))))))
    ;; helper to find interval for a target at position idx
    (define (find-interval lst target idx)
      (let loop ((rest lst))
        (if (null? rest)
            #f
            (let* ((pair (car rest))
                   (val (car pair))
                   (s (cdr pair)))
              (if (= val target)
                  (let ((L s)
                        (R (if (null? (cdr rest)) idx (sub1 (cdr (car rest))))))
                    (list L R))
                  (loop (cdr rest)))))))
    ;; DP
    (define dp-prev (make-vector (+ n 1) INF))
    (vector-set! dp-prev 0 0)
    (for ([t andValues])
      (define dp-cur (make-vector (+ n 1) INF))
      (define seg (build-segtree dp-prev))
      (for ([i (in-range 1 (+ n 1))])
        (define idx (- i 1))
        (define lst (vector-ref and-lists idx))
        (define interval (find-interval lst t idx))
        (when interval
          (define L (list-ref interval 0))
          (define R (list-ref interval 1))
          (when (<= L R)
            (define best (query-segtree seg 1 0 (+ n) L R))
            (when (< best INF)
              (vector-set! dp-cur i (+ best (list-ref nums idx)))))))
      (set! dp-prev dp-cur))
    (let ((ans (vector-ref dp-prev n)))
      (if (>= ans INF) -1 ans))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_value_sum/2]).

-define(INF, (1 bsl 60)).

minimum_value_sum(Nums, AndValues) ->
    N = length(Nums),
    M = length(AndValues),

    DP0 = array:new(N + 1, {default, ?INF}),
    DPPrev = array:set(DP0, 0, 0),

    FinalDP = lists:foldl(
        fun(J, DPPrevAcc) ->
            Target = lists:nth(J, AndValues),
            {Tree, Size} = build_tree(DPPrevAcc),

            DPCurr0 = array:new(N + 1, {default, ?INF}),
            {DPCurrFinal, _} =
                lists:foldl(
                    fun({Num, Idx}, {DPAcc, PrevMap}) ->
                        BaseEntry = {Num, Idx, Idx},
                        EntriesFromPrev = [
                            {(V band Num), MinS, MaxS}
                         || {V, {MinS, MaxS}} <- maps:to_list(PrevMap)
                        ],
                        AllEntries = [BaseEntry | EntriesFromPrev],
                        NewMap = merge_entries(AllEntries, #{}),

                        case maps:get(Target, NewMap, undefined) of
                            undefined ->
                                {DPAcc, NewMap};
                            {MinStart, MaxStart} ->
                                LeftIdx = MinStart - 1,
                                RightIdx = MaxStart - 1,
                                MinPrev = query({Tree, Size}, LeftIdx, RightIdx),
                                if MinPrev < ?INF ->
                                    NewVal = MinPrev + Num,
                                    DPAcc2 = array:set(DPAcc, Idx, NewVal),
                                    {DPAcc2, NewMap};
                                   true ->
                                    {DPAcc, NewMap}
                                end
                        end
                    end,
                    {DPCurr0, #{}},
                    lists:zip(Nums, lists:seq(1, N))
                ),
            DPCurrFinal
        end,
        DPPrev,
        lists:seq(1, M)
    ),

    Answer = array:get(FinalDP, N),
    if Answer >= ?INF -> -1; true -> Answer end.

%% Merge list of entries {Val, MinStart, MaxStart} into map Val => {Min, Max}
merge_entries([], Acc) ->
    Acc;
merge_entries([{V, Smin, Smax} | Rest], Acc) ->
    case maps:get(V, Acc, undefined) of
        undefined ->
            NewAcc = maps:put(V, {Smin, Smax}, Acc);
        {OldMin, OldMax} ->
            Min = if Smin < OldMin -> Smin; true -> OldMin end,
            Max = if Smax > OldMax -> Smax; true -> OldMax end,
            NewAcc = maps:put(V, {Min, Max}, Acc)
    end,
    merge_entries(Rest, NewAcc).

%% Build segment tree for range minimum query
build_tree(DpArr) ->
    Nplus1 = array:size(DpArr),
    Size = next_pow2(Nplus1, 1),
    Tree0 = array:new(Size * 2, {default, ?INF}),
    TreeLeaves = fill_leaves(0, Nplus1 - 1, DpArr, Tree0, Size),
    TreeFull = build_internal(Size - 1, TreeLeaves),
    {TreeFull, Size}.

fill_leaves(I, MaxIdx, _DpArr, Tree, _Size) when I > MaxIdx ->
    Tree;
fill_leaves(I, MaxIdx, DpArr, Tree, Size) ->
    Val = array:get(DpArr, I),
    NewTree = array:set(Tree, Size + I, Val),
    fill_leaves(I + 1, MaxIdx, DpArr, NewTree, Size).

build_internal(0, Tree) -> Tree;
build_internal(I, Tree) ->
    Left = array:get(Tree, I * 2),
    Right = array:get(Tree, I * 2 + 1),
    Min = if Left < Right -> Left; true -> Right end,
    NewTree = array:set(Tree, I, Min),
    build_internal(I - 1, NewTree).

next_pow2(N, Pow) when Pow < N ->
    next_pow2(N, Pow * 2);
next_pow2(_N, Pow) ->
    Pow.

%% Range minimum query on segment tree
query({Tree, Size}, L, R) ->
    query_loop(L + Size, R + Size, Tree, ?INF).

query_loop(L, R, _Tree, MinAcc) when L > R ->
    MinAcc;
query_loop(L, R, Tree, MinAcc) ->
    Min1 = if (L band 1) == 1 ->
                Val = array:get(Tree, L),
                if Val < MinAcc -> Val; true -> MinAcc end;
           true -> MinAcc
          end,
    L1 = if (L band 1) == 1 -> L + 1; else L end,
    Min2 = if (R band 1) == 0 ->
                Val = array:get(Tree, R),
                if Val < Min1 -> Val; true -> Min1 end;
           true -> Min1
          end,
    R1 = if (R band 1) == 0 -> R - 1; else R end,
    query_loop(L1 bsr 1, R1 bsr 1, Tree, Min2).
```

## Elixir

```elixir
defmodule Solution do
  @inf 1_000_000_000

  def minimum_value_sum(nums, and_values) do
    n = length(nums)
    m = length(and_values)

    dp0 = :array.new(n + 1, default: @inf)
    dp0 = :array.set(0, 0, dp0)

    final_dp =
      Enum.reduce(1..m, dp0, fn j, dp_prev ->
        target = Enum.at(and_values, j - 1)

        # build segment tree over dp_prev[0..n-1]
        vals = for idx <- 0..(n - 1), do: :array.get(idx, dp_prev)
        seg = SegmentTree.new(vals, @inf)

        {dp_curr, _} =
          Enum.reduce(1..n, {%array_new(n + 1, default: @inf), []}, fn i,
                                                                      {dp_arr, prev_list} ->
            cur_num = Enum.at(nums, i - 1)
            and_list = build_and_list(prev_list, cur_num)

            {l, r} = find_interval(and_list, target, i)

            dp_arr =
              if l != nil do
                left_idx = l - 1
                right_idx = r - 1

                min_prev = SegmentTree.query(seg, left_idx, right_idx)

                val =
                  if min_prev >= @inf do
                    @inf
                  else
                    min_prev + cur_num
                  end

                :array.set(i, val, dp_arr)
              else
                dp_arr
              end

            {dp_arr, and_list}
          end)

        dp_curr
      end)

    res = :array.get(n, final_dp)

    if res >= @inf, do: -1, else: res
  end

  defp build_and_list(prev, cur) do
    # start with subarray of length 1
    list =
      Enum.reduce(prev, [{cur, nil}], fn {v, pos}, acc ->
        new_v = Bitwise.band(v, cur)

        case acc do
          [{prev_val, prev_pos} | rest] when prev_val == new_v ->
            # merge, keep earliest start (smaller index)
            [{prev_val, min(prev_pos || 0, pos)} | rest]

          _ ->
            [{new_v, pos} | acc]
        end
      end)

    # replace nil with actual position for length 1 subarray
    list =
      case list do
        [{val, nil} | rest] -> [{val, :undefined} | rest]
        _ -> list
      end

    # convert to proper start positions (i decreasing)
    {list, _} = Enum.map_reduce(list, [], fn {val, pos}, acc ->
      start =
        case pos do
          :undefined -> nil
          _ -> pos
        end

      {[{val, start} | acc], []}
    end)

    # reverse to have order from shortest (start near i) to longest
    Enum.reverse(list)
  end

  defp find_interval(list, target, i) do
    Enum.reduce_while(Enum.with_index(list), {nil, nil}, fn {{val, start}, idx},
                                                            _acc ->
      if val == target do
        ub =
          if idx == 0 do
            i
          else
            {_prev_val, prev_start} = Enum.at(list, idx - 1)
            prev_start - 1
          end

        {:halt, {start, ub}}
      else
        {:cont, {nil, nil}}
      end
    end)
  end
end

defmodule SegmentTree do
  defstruct size: 0, arr: nil

  def new(vals, inf) do
    n = length(vals)

    size =
      Enum.reduce_while(1, fn _ ->
        if size < n do
          {:cont, size * 2}
        else
          {:halt, size}
        end
      end)

    size = pow2_ge(n)
    arr = :array.new(2 * size, default: inf)

    arr =
      Enum.with_index(vals)
      |> Enum.reduce(arr, fn {v, i}, a -> :array.set(size + i, v, a) end)

    arr = build_internal(arr, size - 1, inf)

    %__MODULE__{size: size, arr: arr}
  end

  defp pow2_ge(n) do
    Enum.reduce_while(1, fn acc ->
      if acc < n, do: {:cont, acc * 2}, else: {:halt, acc}
    end)
  end

  defp build_internal(arr, 0, _inf), do: arr

  defp build_internal(arr, idx, inf) when idx > 0 do
    left = :array.get(idx * 2, arr)
    right = :array.get(idx * 2 + 1, arr)
    minv = if left < right, do: left, else: right
    arr = :array.set(idx, minv, arr)
    build_internal(arr, idx - 1, inf)
  end

  def query(%__MODULE__{size: size, arr: arr}, l, r) when l <= r do
    query_rec(l + size, r + size, arr, @inf)
  end

  defp query_rec(l, r, _arr, res) when l > r, do: res

  defp query_rec(l, r, arr, res) do
    {res, l, r} =
      if rem(l, 2) == 1 do
        val = :array.get(l, arr)
        {min(res, val), l + 1, r}
      else
        {res, l, r}
      end

    {res, l, r} =
      if rem(r, 2) == 0 do
        val = :array.get(r, arr)
        {min(res, val), l, r - 1}
      else
        {res, l, r}
      end

    query_rec(div(l, 2), div(r, 2), arr, res)
  end
end
```

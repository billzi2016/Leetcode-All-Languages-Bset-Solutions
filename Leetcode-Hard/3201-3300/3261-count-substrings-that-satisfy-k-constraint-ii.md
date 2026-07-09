# 3261. Count Substrings That Satisfy K-Constraint II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Fenwick {
    int n;
    vector<long long> bit;
public:
    Fenwick(int n=0): n(n), bit(n+1,0) {}
    void add(int idx,long long val){
        for(;idx<=n;idx+=idx&-idx) bit[idx]+=val;
    }
    long long sumPrefix(int idx) const{
        long long s=0;
        for(;idx>0;idx-=idx&-idx) s+=bit[idx];
        return s;
    }
    long long rangeSum(int l,int r) const{ // inclusive, 1-indexed
        return sumPrefix(r)-sumPrefix(l-1);
    }
};

class Solution {
public:
    vector<long long> countKConstraintSubstrings(string s, int k, vector<vector<int>>& queries) {
        int n = s.size();
        vector<int> B(n, n); // minimal right index where both counts > k
        int cnt0=0,cnt1=0;
        int r=0;
        for(int i=0;i<n;++i){
            while(r<n && !(cnt0>k && cnt1>k)){
                if(s[r]=='0') ++cnt0; else ++cnt1;
                ++r;
            }
            if(cnt0>k && cnt1>k) B[i]=r-1;
            // remove s[i] from window
            if(s[i]=='0') --cnt0; else --cnt1;
        }

        vector<vector<int>> bucket(n);
        for(int i=0;i<n;++i){
            if(B[i]<n) bucket[B[i]].push_back(i);
        }

        struct Q{int l,r,idx;};
        int m = queries.size();
        vector<Q> qs(m);
        for(int i=0;i<m;++i){
            qs[i]={queries[i][0], queries[i][1], i};
        }
        sort(qs.begin(), qs.end(), [](const Q& a,const Q& b){return a.r<b.r;});

        Fenwick bitCnt(n), bitSum(n);
        vector<long long> ans(m);
        int qptr=0;
        for(int curR=0;curR<n;++curR){
            for(int idx: bucket[curR]){
                int pos = idx+1; // 1-indexed
                bitCnt.add(pos,1);
                bitSum.add(pos,curR);
            }
            while(qptr<m && qs[qptr].r==curR){
                int l=qs[qptr].l;
                int rgt=qs[qptr].r;
                long long cnt = bitCnt.rangeSum(l+1, rgt+1);
                long long sumB = bitSum.rangeSum(l+1, rgt+1);
                long long len = (long long)(rgt - l + 1);
                long long total = len * (len + 1) / 2;
                long long invalid = cnt * (rgt + 1LL) - sumB;
                ans[qs[qptr].idx] = total - invalid;
                ++qptr;
            }
        }
        // queries with r beyond last processed (shouldn't happen)
        while(qptr<m){
            int l=qs[qptr].l;
            int rgt=qs[qptr].r;
            long long cnt = bitCnt.rangeSum(l+1, rgt+1);
            long long sumB = bitSum.rangeSum(l+1, rgt+1);
            long long len = (long long)(rgt - l + 1);
            long long total = len * (len + 1) / 2;
            long long invalid = cnt * (rgt + 1LL) - sumB;
            ans[qs[qptr].idx] = total - invalid;
            ++qptr;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long[] countKConstraintSubstrings(String s, int k, int[][] queries) {
        int n = s.length();
        int[] minR = new int[n];
        final int INF = n; // sentinel for no valid right endpoint
        int right = 0;
        int cnt0 = 0, cnt1 = 0;
        char[] ch = s.toCharArray();

        for (int left = 0; left < n; left++) {
            while (right < n && !(cnt0 > k && cnt1 > k)) {
                if (ch[right] == '0') cnt0++;
                else cnt1++;
                right++;
            }
            if (cnt0 > k && cnt1 > k) {
                minR[left] = right - 1; // minimal right index satisfying condition
            } else {
                minR[left] = INF;
            }
            // move left forward, remove its contribution
            if (ch[left] == '0') cnt0--;
            else cnt1--;
        }

        // collect positions with valid minR
        int m = 0;
        for (int i = 0; i < n; i++) {
            if (minR[i] != INF) m++;
        }
        int[][] arr = new int[m][2]; // {minR, index}
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (minR[i] != INF) {
                arr[idx][0] = minR[i];
                arr[idx][1] = i;
                idx++;
            }
        }
        java.util.Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));

        // prepare queries
        int q = queries.length;
        Query[] qs = new Query[q];
        for (int i = 0; i < q; i++) {
            qs[i] = new Query(queries[i][0], queries[i][1], i);
        }
        java.util.Arrays.sort(qs, (a, b) -> Integer.compare(a.r, b.r));

        Fenwick bitCnt = new Fenwick(n);
        Fenwick bitSum = new Fenwick(n);

        long[] ans = new long[q];
        int ptr = 0;
        for (Query qu : qs) {
            while (ptr < arr.length && arr[ptr][0] <= qu.r) {
                int pos = arr[ptr][1];
                int mr = arr[ptr][0];
                bitCnt.add(pos, 1);
                bitSum.add(pos, mr);
                ptr++;
            }
            long cnt = bitCnt.rangeSum(qu.l, qu.r);
            long sumMin = bitSum.rangeSum(qu.l, qu.r);
            long bad = ((long) qu.r + 1) * cnt - sumMin;
            long len = (long) qu.r - qu.l + 1;
            long total = len * (len + 1) / 2;
            ans[qu.idx] = total - bad;
        }
        return ans;
    }

    private static class Query {
        int l, r, idx;
        Query(int l, int r, int idx) {
            this.l = l;
            this.r = r;
            this.idx = idx;
        }
    }

    private static class Fenwick {
        long[] bit;
        int n;
        Fenwick(int n) {
            this.n = n;
            bit = new long[n + 1];
        }
        void add(int index, long delta) {
            // convert to 1-based
            for (int i = index + 1; i <= n; i += i & -i) {
                bit[i] += delta;
            }
        }
        long sumPrefix(int index) {
            long res = 0;
            for (int i = index + 1; i > 0; i -= i & -i) {
                res += bit[i];
            }
            return res;
        }
        long rangeSum(int l, int r) {
            if (l > r) return 0;
            return sumPrefix(r) - (l == 0 ? 0 : sumPrefix(l - 1));
        }
    }
}
```

## Python

```python
class Solution(object):
    def countKConstraintSubstrings(self, s, k, queries):
        """
        :type s: str
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        # compute minimal left index so that zeros count <= k
        Lz = [0] * n
        Lo = [0] * n

        zero_pos = []
        one_pos = []

        for i, ch in enumerate(s):
            if ch == '0':
                zero_pos.append(i)
            if len(zero_pos) > k:
                # (k+1)-th most recent zero is at index -(k+1)
                Lz[i] = zero_pos[-(k + 1)] + 1
            else:
                Lz[i] = 0

            if ch == '1':
                one_pos.append(i)
            if len(one_pos) > k:
                Lo[i] = one_pos[-(k + 1)] + 1
            else:
                Lo[i] = 0

        g = [min(Lz[i], Lo[i]) for i in range(n)]

        # Fenwick Tree implementation
        class BIT:
            __slots__ = ('n', 'tree')
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)
            def add(self, idx, delta):
                i = idx + 1
                while i <= self.n:
                    self.tree[i] += delta
                    i += i & -i
            def sum(self, idx):
                if idx < 0:
                    return 0
                i = idx + 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res

        # prepare positions sorted by g descending
        pos_by_g = sorted(((g[i], i) for i in range(n)), key=lambda x: -x[0])

        # sort queries by left descending
        qlist = [(l, r, idx) for idx, (l, r) in enumerate(queries)]
        qlist.sort(key=lambda x: -x[0])

        bit_cnt = BIT(n)
        bit_sum = BIT(n)

        ans = [0] * len(queries)
        p = 0
        m = len(pos_by_g)

        for l, r, idx in qlist:
            while p < m and pos_by_g[p][0] > l:
                gval, pos = pos_by_g[p]
                bit_cnt.add(pos, 1)
                bit_sum.add(pos, gval)
                p += 1

            total_len = r - l + 1
            total_sub = total_len * (total_len + 1) // 2

            cnt = bit_cnt.sum(r) - bit_cnt.sum(l - 1)
            sumg = bit_sum.sum(r) - bit_sum.sum(l - 1)

            bad = sumg - cnt * l
            ans[idx] = total_sub - bad

        return ans
```

## Python3

```python
import sys
from typing import List

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, val: int):
        i = idx + 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def sum(self, idx: int) -> int:
        res = 0
        i = idx + 1
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.sum(r) - (self.sum(l - 1) if l else 0)

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        zero_pos = []
        one_pos = []
        for i,ch in enumerate(s):
            if ch == '0':
                zero_pos.append(i)
            else:
                one_pos.append(i)

        bad_start = [-1] * n
        cnt0 = cnt1 = 0
        for i,ch in enumerate(s):
            if ch == '0':
                cnt0 += 1
            else:
                cnt1 += 1

            if cnt0 > k and cnt1 > k:
                left_zero = zero_pos[cnt0 - k - 1]
                left_one = one_pos[cnt1 - k - 1]
                bad_start[i] = min(left_zero, left_one)

        # prepare list of positions with valid bad_start
        bad_list = [(bad_start[i], i) for i in range(n) if bad_start[i] != -1]
        bad_list.sort(key=lambda x: x[0], reverse=True)  # descending by bad_start

        qinfo = [(l, r, idx) for idx,(l,r) in enumerate(queries)]
        qinfo.sort(key=lambda x: x[0], reverse=True)   # descending by l

        bit_cnt = BIT(n)
        bit_sum = BIT(n)

        ans = [0] * len(queries)
        ptr = 0
        m = len(bad_list)

        for l, r, idx in qinfo:
            while ptr < m and bad_list[ptr][0] >= l:
                bstart, pos = bad_list[ptr]
                bit_cnt.add(pos, 1)
                bit_sum.add(pos, bstart + 1)   # store (bad_start + 1)
                ptr += 1

            cnt = bit_cnt.range_sum(l, r)
            sum_vals = bit_sum.range_sum(l, r)
            contribution = sum_vals - l * cnt
            length = r - l + 1
            total = length * (length + 1) // 2
            ans[idx] = total - contribution

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int val;   // leftBad value
    int idx;   // position index (0‑based)
} Pair;

typedef struct {
    int l, r;
    int id;
} Query;

/* Fenwick Tree for counts and sums */
static void fenwickAdd(long long *tree, int n, int idx, long long delta) {
    while (idx <= n) {
        tree[idx] += delta;
        idx += idx & -idx;
    }
}
static long long fenwickSum(long long *tree, int idx) {
    long long res = 0;
    while (idx > 0) {
        res += tree[idx];
        idx -= idx & -idx;
    }
    return res;
}

/* Comparator for Pair descending by val */
static int cmpPairDesc(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    return pb->val - pa->val;
}
/* Comparator for Query descending by l */
static int cmpQueryDesc(const void *a, const void *b) {
    const Query *qa = (const Query *)a;
    const Query *qb = (const Query *)b;
    return qb->l - qa->l;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* countKConstraintSubstrings(char* s, int k, int** queries, int queriesSize,
                                     int* queriesColSize, int* returnSize) {
    int n = (int)strlen(s);
    int *leftBad = (int *)malloc(n * sizeof(int));
    int cnt0 = 0, cnt1 = 0;
    int left = 0;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '0') cnt0++; else cnt1++;
        if (cnt0 > k && cnt1 > k) {
            while (left <= i) {
                int dec0 = (s[left] == '0');
                int dec1 = (s[left] == '1');
                if (cnt0 - dec0 > k && cnt1 - dec1 > k) {
                    cnt0 -= dec0;
                    cnt1 -= dec1;
                    left++;
                } else break;
            }
            leftBad[i] = left;          // rightmost left index with both counts > k
        } else {
            leftBad[i] = -1;            // no violating substring ending at i
        }
    }

    /* Build list of positions with valid leftBad */
    int m = 0;
    for (int i = 0; i < n; ++i) if (leftBad[i] != -1) ++m;
    Pair *pairs = (Pair *)malloc(m * sizeof(Pair));
    int pidx = 0;
    for (int i = 0; i < n; ++i)
        if (leftBad[i] != -1) {
            pairs[pidx].val = leftBad[i];
            pairs[pidx].idx = i;
            ++pidx;
        }
    qsort(pairs, m, sizeof(Pair), cmpPairDesc);

    /* Prepare queries */
    Query *qs = (Query *)malloc(queriesSize * sizeof(Query));
    for (int i = 0; i < queriesSize; ++i) {
        qs[i].l = queries[i][0];
        qs[i].r = queries[i][1];
        qs[i].id = i;
    }
    qsort(qs, queriesSize, sizeof(Query), cmpQueryDesc);

    /* Fenwick trees: one for counts (as long long), one for sum of leftBad */
    long long *bitCnt = (long long *)calloc(n + 2, sizeof(long long));
    long long *bitSum = (long long *)calloc(n + 2, sizeof(long long));

    long long *ans = (long long *)malloc(queriesSize * sizeof(long long));
    int cur = 0;   // index in pairs

    for (int qi = 0; qi < queriesSize; ++qi) {
        int L = qs[qi].l;
        int R = qs[qi].r;

        while (cur < m && pairs[cur].val >= L) {
            int pos = pairs[cur].idx + 1;   // Fenwick is 1‑based
            fenwickAdd(bitCnt, n, pos, 1);
            fenwickAdd(bitSum, n, pos, (long long)pairs[cur].val);
            ++cur;
        }

        long long cnt = fenwickSum(bitCnt, R + 1) - fenwickSum(bitCnt, L);
        long long sumVals = fenwickSum(bitSum, R + 1) - fenwickSum(bitSum, L);

        long long offset = (long long)L - 1;   // (l-1)
        long long violating = sumVals - offset * cnt;

        long long len = (long long)(R - L + 1);
        long long totalSub = len * (len + 1) / 2;
        ans[qs[qi].id] = totalSub - violating;
    }

    free(leftBad);
    free(pairs);
    free(qs);
    free(bitCnt);
    free(bitSum);

    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long[] CountKConstraintSubstrings(string s, int k, int[][] queries) {
        int n = s.Length;
        int[] L = new int[n];
        int rPtr = 0;
        int cnt0 = 0, cnt1 = 0;
        for (int i = 0; i < n; i++) {
            while (rPtr < n && !(cnt0 > k && cnt1 > k)) {
                if (s[rPtr] == '0') cnt0++; else cnt1++;
                rPtr++;
            }
            if (cnt0 > k && cnt1 > k) L[i] = rPtr - 1;
            else L[i] = n; // never satisfies
            if (s[i] == '0') cnt0--; else cnt1--;
        }

        List<int>[] activate = new List<int>[n];
        for (int i = 0; i < n; i++) {
            int pos = L[i];
            if (pos < n) {
                if (activate[pos] == null) activate[pos] = new List<int>();
                activate[pos].Add(i);
            }
        }

        int q = queries.Length;
        Query[] qs = new Query[q];
        for (int i = 0; i < q; i++) {
            qs[i] = new Query { l = queries[i][0], r = queries[i][1], idx = i };
        }
        Array.Sort(qs, (a, b) => a.r.CompareTo(b.r));

        BIT bitCnt = new BIT(n);
        BIT bitSum = new BIT(n);
        long[] ans = new long[q];
        int qi = 0;
        for (int curR = 0; curR < n; curR++) {
            if (activate[curR] != null) {
                foreach (int i in activate[curR]) {
                    bitCnt.Add(i, 1);
                    bitSum.Add(i, L[i]);
                }
            }
            while (qi < q && qs[qi].r == curR) {
                var qu = qs[qi];
                long cnt = bitCnt.RangeSum(qu.l, qu.r);
                long sumF = bitSum.RangeSum(qu.l, qu.r);
                long bad = cnt * (curR + 1L) - sumF;
                long len = qu.r - qu.l + 1L;
                long total = len * (len + 1) / 2;
                ans[qu.idx] = total - bad;
                qi++;
            }
        }

        // Queries with r less than first processed index (if any) are already handled because loop starts at curR=0.
        return ans;
    }

    private struct Query {
        public int l, r, idx;
    }

    private class BIT {
        private readonly long[] tree;
        private readonly int n;
        public BIT(int size) {
            n = size;
            tree = new long[n + 1];
        }
        public void Add(int index, long delta) { // index is 0-based
            for (int i = index + 1; i <= n; i += i & -i)
                tree[i] += delta;
        }
        private long PrefixSum(int index) { // inclusive 0..index
            long res = 0;
            for (int i = index + 1; i > 0; i -= i & -i)
                res += tree[i];
            return res;
        }
        public long RangeSum(int left, int right) {
            if (left > right) return 0;
            long res = PrefixSum(right);
            if (left > 0) res -= PrefixSum(left - 1);
            return res;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @param {number[][]} queries
 * @return {number[]}
 */
var countKConstraintSubstrings = function(s, k, queries) {
    const n = s.length;
    // compute maxRight for each start index
    const maxR = new Array(n);
    let cnt0 = 0, cnt1 = 0;
    let r = -1;
    for (let l = 0; l < n; ++l) {
        while (r + 1 < n) {
            const ch = s.charAt(r + 1);
            const newCnt0 = cnt0 + (ch === '0' ? 1 : 0);
            const newCnt1 = cnt1 + (ch === '1' ? 1 : 0);
            if (newCnt0 <= k || newCnt1 <= k) {
                ++r;
                if (ch === '0') ++cnt0; else ++cnt1;
            } else break;
        }
        maxR[l] = r;
        const chL = s.charAt(l);
        if (chL === '0') --cnt0; else --cnt1;
        if (r < l) {
            // window became empty
            r = l;
        }
    }

    // prefix sum of indices
    const preIdx = new Array(n);
    for (let i = 0; i < n; ++i) {
        preIdx[i] = i + (i > 0 ? preIdx[i - 1] : 0);
    }

    // bucket positions by their maxR value
    const buckets = Array.from({ length: n }, () => []);
    for (let i = 0; i < n; ++i) {
        const mr = maxR[i];
        if (mr >= 0) buckets[mr].push(i);
    }

    // Fenwick Tree implementation
    class BIT {
        constructor(size) {
            this.n = size;
            this.bit = new Array(size + 2).fill(0);
        }
        add(idx, val) {
            for (let i = idx; i <= this.n; i += i & -i) {
                this.bit[i] += val;
            }
        }
        sum(idx) {
            let res = 0;
            for (let i = idx; i > 0; i -= i & -i) {
                res += this.bit[i];
            }
            return res;
        }
    }

    const bitCnt = new BIT(n);
    const bitSum = new BIT(n);

    // sort queries by right endpoint
    const qWithIdx = queries.map((qr, idx) => [qr[0], qr[1], idx]);
    qWithIdx.sort((a, b) => a[1] - b[1]);

    const ans = new Array(queries.length);
    let curR = -1;
    for (const [L, R, id] of qWithIdx) {
        while (curR < R) {
            ++curR;
            for (const pos of buckets[curR]) {
                const ftIdx = pos + 1; // 1-indexed
                bitCnt.add(ftIdx, 1);
                bitSum.add(ftIdx, curR);
            }
        }
        const total = R - L + 1;
        const sumCntLe = bitCnt.sum(R + 1) - bitCnt.sum(L);
        const sumA = bitSum.sum(R + 1) - bitSum.sum(L);
        const sumIndices = preIdx[R] - (L > 0 ? preIdx[L - 1] : 0);
        const sumMin = sumA + R * (total - sumCntLe);
        ans[id] = sumMin - sumIndices + total;
    }
    return ans;
};
```

## Typescript

```typescript
function countKConstraintSubstrings(s: string, k: number, queries: number[][]): number[] {
    const n = s.length;
    const prefZero = new Uint32Array(n + 1);
    const prefOne = new Uint32Array(n + 1);
    for (let i = 0; i < n; ++i) {
        prefZero[i + 1] = prefZero[i] + (s.charCodeAt(i) === 48 ? 1 : 0);
        prefOne[i + 1] = prefOne[i] + (s.charCodeAt(i) === 49 ? 1 : 0);
    }

    const goodLeft: number[] = new Array(n);
    for (let r = 0; r < n; ++r) {
        let lo = 0, hi = r, best = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            const zeros = prefZero[r + 1] - prefZero[mid];
            const ones = prefOne[r + 1] - prefOne[mid];
            if (zeros > k && ones > k) {
                best = mid;
                lo = mid + 1; // try to move left boundary rightwards (shorter window)
            } else {
                hi = mid - 1;
            }
        }
        goodLeft[r] = best + 1; // if best==-1 => 0
    }

    const prefGL = new Float64Array(n);
    for (let i = 0; i < n; ++i) {
        prefGL[i] = (i === 0 ? 0 : prefGL[i - 1]) + goodLeft[i];
    }

    // Fenwick Tree for count and sum of goodLeft where goodLeft <= current L
    class BIT {
        n: number;
        cnt: Float64Array;
        sum: Float64Array;
        constructor(n: number) {
            this.n = n;
            this.cnt = new Float64Array(n + 1);
            this.sum = new Float64Array(n + 1);
        }
        add(idx: number, deltaCnt: number, deltaSum: number): void {
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.cnt[i] += deltaCnt;
                this.sum[i] += deltaSum;
            }
        }
        prefix(idx: number): { cnt: number; sum: number } {
            let c = 0, s = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                c += this.cnt[i];
                s += this.sum[i];
            }
            return { cnt: c, sum: s };
        }
        range(l: number, r: number): { cnt: number; sum: number } {
            if (l > r) return { cnt: 0, sum: 0 };
            const preR = this.prefix(r);
            const preL = l ? this.prefix(l - 1) : { cnt: 0, sum: 0 };
            return { cnt: preR.cnt - preL.cnt, sum: preR.sum - preL.sum };
        }
    }

    // sort positions by goodLeft value
    const posByGL = Array.from({ length: n }, (_, i) => i).sort((a, b) => goodLeft[a] - goodLeft[b]);

    // prepare queries with original index
    const qObjs = queries.map((qr, idx) => ({ l: qr[0], r: qr[1], idx }));
    qObjs.sort((a, b) => a.l - b.l);

    const bit = new BIT(n);
    let ptr = 0;
    const ans = new Array(queries.length).fill(0);

    for (const q of qObjs) {
        while (ptr < n && goodLeft[posByGL[ptr]] <= q.l) {
            const pos = posByGL[ptr];
            bit.add(pos, 1, goodLeft[pos]);
            ++ptr;
        }
        const rangeInfo = bit.range(q.l, q.r);
        const cntLE = rangeInfo.cnt;
        const sumLE = rangeInfo.sum;

        const totalIdx = q.r - q.l + 1;
        const sumIPlusOne = ((q.l + 1) + (q.r + 1)) * totalIdx / 2;

        const totalGLRange = prefGL[q.r] - (q.l > 0 ? prefGL[q.l - 1] : 0);
        const sumGT = totalGLRange - sumLE;

        const res = sumIPlusOne - q.l * cntLE - sumGT;
        ans[q.idx] = Math.round(res); // result is integer
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function countKConstraintSubstrings($s, $k, $queries) {
        $n = strlen($s);
        // compute left bound for each right index
        $leftBound = array_fill(0, $n, 0);
        $cnt0 = 0;
        $cnt1 = 0;
        $L = 0;
        for ($r = 0; $r < $n; ++$r) {
            if ($s[$r] === '0') {
                $cnt0++;
            } else {
                $cnt1++;
            }
            while ($cnt0 > $k && $cnt1 > $k) {
                if ($s[$L] === '0') {
                    $cnt0--;
                } else {
                    $cnt1--;
                }
                $L++;
            }
            $leftBound[$r] = $L; // 0‑based
        }

        // prepare queries with original indices
        $qList = [];
        foreach ($queries as $idx => $qr) {
            $qList[] = [$qr[0], $qr[1], $idx];
        }
        usort($qList, function($a, $b) {
            return $a[1] <=> $b[1]; // sort by right endpoint
        });

        // Fenwick tree supporting range add & range sum
        $fenwick = new class($n) {
            public $size;
            public $bit1;
            public $bit2;
            function __construct($n) {
                $this->size = $n + 5; // extra space
                $this->bit1 = array_fill(0, $this->size, 0);
                $this->bit2 = array_fill(0, $this->size, 0);
            }
            private function update(&$bit, $idx, $delta) {
                $sz = $this->size;
                while ($idx < $sz) {
                    $bit[$idx] += $delta;
                    $idx += $idx & (-$idx);
                }
            }
            public function rangeAdd($l, $r, $val) { // 1‑based inclusive
                $this->update($this->bit1, $l, $val);
                $this->update($this->bit1, $r + 1, -$val);
                $this->update($this->bit2, $l, $val * ($l - 1));
                $this->update($this->bit2, $r + 1, -$val * $r);
            }
            private function query($bit, $idx) {
                $res = 0;
                while ($idx > 0) {
                    $res += $bit[$idx];
                    $idx -= $idx & (-$idx);
                }
                return $res;
            }
            public function prefixSum($idx) { // sum of array[1..idx]
                $sum1 = $this->query($this->bit1, $idx);
                $sum2 = $this->query($this->bit2, $idx);
                return $sum1 * $idx - $sum2;
            }
            public function rangeSum($l, $r) { // 1‑based inclusive
                if ($l > $r) return 0;
                return $this->prefixSum($r) - $this->prefixSum($l - 1);
            }
        };

        $answers = array_fill(0, count($queries), 0);
        $curR = -1;
        foreach ($qList as $qq) {
            [$ql, $qr, $origIdx] = $qq;
            while ($curR < $qr) {
                ++$curR;
                $Lbound = $leftBound[$curR]; // 0‑based
                $lIdx = $Lbound + 1;        // to 1‑based
                $rIdx = $curR + 1;
                $fenwick->rangeAdd($lIdx, $rIdx, 1);
            }
            $ans = $fenwick->rangeSum($ql + 1, $qr + 1);
            $answers[$origIdx] = $ans;
        }

        return $answers;
    }
}
```

## Swift

```swift
import Foundation

class Fenwick {
    private var n: Int
    private var tree: [Int64]
    init(_ size: Int) {
        self.n = size
        self.tree = Array(repeating: 0, count: size + 2)
    }
    func add(_ index: Int, _ delta: Int64) {
        var i = index
        while i <= n {
            tree[i] += delta
            i += i & -i
        }
    }
    func sum(_ index: Int) -> Int64 {
        var res: Int64 = 0
        var i = index
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }
}

class Solution {
    func countKConstraintSubstrings(_ s: String, _ k: Int, _ queries: [[Int]]) -> [Int] {
        let n = s.count
        let chars = Array(s.utf8)   // '0' = 48, '1' = 49
        
        var leftBound = Array(repeating: 0, count: n)
        var l = 0
        var zeros = 0
        var ones = 0
        for r in 0..<n {
            if chars[r] == 48 { zeros += 1 } else { ones += 1 }
            while zeros > k && ones > k {
                if chars[l] == 48 { zeros -= 1 } else { ones -= 1 }
                l += 1
            }
            leftBound[r] = l
        }
        
        // prefix sums of leftBound
        var prefA = Array(repeating: Int64(0), count: n + 1)
        for i in 0..<n {
            prefA[i + 1] = prefA[i] + Int64(leftBound[i])
        }
        
        // positions sorted by leftBound value
        var posList: [(value: Int, idx: Int)] = []
        posList.reserveCapacity(n)
        for i in 0..<n {
            posList.append((leftBound[i], i))
        }
        posList.sort { $0.value < $1.value }
        
        // queries with original index
        struct Query {
            let L: Int
            let R: Int
            let idx: Int
        }
        var qObjs: [Query] = []
        qObjs.reserveCapacity(queries.count)
        for (i, arr) in queries.enumerated() {
            qObjs.append(Query(L: arr[0], R: arr[1], idx: i))
        }
        qObjs.sort { $0.L < $1.L }
        
        let bitCount = Fenwick(n)
        let bitSum = Fenwick(n)
        var answers = Array(repeating: 0, count: queries.count)
        var p = 0
        
        for q in qObjs {
            while p < n && posList[p].value < q.L {
                let idx = posList[p].idx
                bitCount.add(idx + 1, 1)
                bitSum.add(idx + 1, Int64(posList[p].value))
                p += 1
            }
            // count and sum of leftBound values that are < L within [L,R]
            let cntLT = bitCount.sum(q.R + 1) - bitCount.sum(q.L)
            let sumLT = bitSum.sum(q.R + 1) - bitSum.sum(q.L)
            
            let sumA_range = prefA[q.R + 1] - prefA[q.L]
            let cnt = q.R - q.L + 1
            // total sum of (r+1) for r in [L,R]
            let totalSum = Int64((Int64(q.R) + 1 + Int64(q.L) + 1) * Int64(cnt) / 2)
            
            var ans = totalSum - sumA_range + sumLT - cntLT * Int64(q.L)
            answers[q.idx] = Int(ans)
        }
        
        return answers
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countKConstraintSubstrings(s: String, k: Int, queries: Array<IntArray>): LongArray {
        val n = s.length
        val lo = IntArray(n)
        var left = 0
        var zeros = 0
        var ones = 0
        for (i in 0 until n) {
            if (s[i] == '0') zeros++ else ones++
            while (zeros > k && ones > k) {
                if (s[left] == '0') zeros-- else ones--
                left++
            }
            lo[i] = left
        }

        val prefI = LongArray(n)
        val prefLo = LongArray(n)
        for (i in 0 until n) {
            val curI = (i + 1).toLong()
            prefI[i] = curI + if (i > 0) prefI[i - 1] else 0L
            prefLo[i] = lo[i].toLong() + if (i > 0) prefLo[i - 1] else 0L
        }

        fun sum(arr: LongArray, l: Int, r: Int): Long {
            if (l > r) return 0L
            var res = arr[r]
            if (l > 0) res -= arr[l - 1]
            return res
        }

        val ans = LongArray(queries.size)
        for ((idxQ, q) in queries.withIndex()) {
            val L = q[0]
            val R = q[1]

            // binary search first position >= L where lo[pos] >= L
            var low = L
            var high = R + 1 // exclusive
            while (low < high) {
                val mid = (low + high) ushr 1
                if (lo[mid] >= L) {
                    high = mid
                } else {
                    low = mid + 1
                }
            }
            val split = low // may be R+1

            var total: Long
            if (split > R) {
                // all lo[i] < L
                val cnt = (R - L + 1).toLong()
                val sumI = sum(prefI, L, R)
                total = sumI - cnt * L
            } else {
                // part1: [L, split-1] where lo < L
                val cnt1 = (split - L).toLong()
                val sumI1 = sum(prefI, L, split - 1)
                val part1 = sumI1 - cnt1 * L

                // part2: [split, R] where lo >= L
                val sumI2 = sum(prefI, split, R)
                val sumLo2 = sum(prefLo, split, R)
                val part2 = sumI2 - sumLo2

                total = part1 + part2
            }
            ans[idxQ] = total
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> countKConstraintSubstrings(String s, int k, List<List<int>> queries) {
    // Placeholder implementation
    return List.filled(queries.length, 0);
  }
}
```

## Golang

```go
package main

type query struct {
	l   int
	idx int
}

type fenwick struct {
	n  int
	b1 []int64
	b2 []int64
}

func newFenwick(n int) *fenwick {
	return &fenwick{
		n:  n + 2,
		b1: make([]int64, n+3),
		b2: make([]int64, n+3),
	}
}

func (f *fenwick) add(tree []int64, idx int, delta int64) {
	for i := idx; i < f.n; i += i & -i {
		tree[i] += delta
	}
}

// range add val to [l, r] (0-indexed)
func (f *fenwick) rangeAdd(l, r int, val int64) {
	if l > r {
		return
	}
	L := l + 1
	R := r + 1
	f.add(f.b1, L, val)
	f.add(f.b1, R+1, -val)
	f.add(f.b2, L, val*int64(L-1))
	f.add(f.b2, R+1, -val*int64(R))
}

// prefix sum of array after range adds (0-indexed inclusive)
func (f *fenwick) prefixSum(pos int) int64 {
	if pos < 0 {
		return 0
	}
	idx := pos + 1
	var s1, s2 int64
	for i := idx; i > 0; i -= i & -i {
		s1 += f.b1[i]
		s2 += f.b2[i]
	}
	return s1*int64(idx) - s2
}

func countKConstraintSubstrings(s string, k int, queries [][]int) []int64 {
	n := len(s)
	qByR := make([][]query, n)
	for i, qr := range queries {
		l, r := qr[0], qr[1]
		qByR[r] = append(qByR[r], query{l: l, idx: i})
	}
	ans := make([]int64, len(queries))

	bit := newFenwick(n)

	left, cnt0, cnt1 := 0, 0, 0
	for r := 0; r < n; r++ {
		if s[r] == '0' {
			cnt0++
		} else {
			cnt1++
		}
		// shrink left while both counts > k and removing left keeps them > k
		for left <= r && cnt0 > k && cnt1 > k {
			if s[left] == '0' && cnt0-1 > k && cnt1 > k {
				cnt0--
				left++
			} else if s[left] == '1' && cnt1-1 > k && cnt0 > k {
				cnt1--
				left++
			} else {
				break
			}
		}
		var low int
		if cnt0 > k && cnt1 > k {
			low = left + 1 // good starts start after left
		} else {
			low = 0
		}
		bit.rangeAdd(low, r, 1)

		// answer queries ending at r
		total := bit.prefixSum(n - 1)
		for _, qq := range qByR[r] {
			prefixBeforeL := bit.prefixSum(qq.l - 1)
			ans[qq.idx] = total - prefixBeforeL
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_k_constraint_substrings(s, k, queries)
  n = s.length
  bytes = s.bytes
  r = -1
  cnt0 = 0
  cnt1 = 0
  max_right = Array.new(n)

  (0...n).each do |l|
    while r + 1 < n
      ch = bytes[r + 1]
      new_cnt0 = cnt0 + (ch == 48 ? 1 : 0)
      new_cnt1 = cnt1 + (ch == 49 ? 1 : 0)
      break if new_cnt0 > k && new_cnt1 > k

      r += 1
      cnt0 = new_cnt0
      cnt1 = new_cnt1
    end

    max_right[l] = r

    ch_l = bytes[l]
    if ch_l == 48
      cnt0 -= 1
    else
      cnt1 -= 1
    end
  end

  pref = Array.new(n + 1, 0)
  (0...n).each do |i|
    val = max_right[i] - i + 1
    pref[i + 1] = pref[i] + val
  end

  answers = []
  queries.each do |lq, rq|
    lo = lq
    hi = rq
    idx = rq + 1
    while lo <= hi
      mid = (lo + hi) / 2
      if max_right[mid] > rq
        idx = mid
        hi = mid - 1
      else
        lo = mid + 1
      end
    end

    sum1 = pref[idx] - pref[lq]
    len2 = rq - idx + 1
    sum2 = len2 * (len2 + 1) / 2
    answers << sum1 + sum2
  end

  answers
end
```

## Scala

```scala
object Solution {
    def countKConstraintSubstrings(s: String, k: Int, queries: Array[Array[Int]]): Array[Long] = {
        val n = s.length
        val low = new Array[Int](n)
        var left = 0
        var cnt0 = 0
        var cnt1 = 0
        for (right <- 0 until n) {
            if (s.charAt(right) == '0') cnt0 += 1 else cnt1 += 1
            while (math.min(cnt0, cnt1) > k) {
                if (s.charAt(left) == '0') cnt0 -= 1 else cnt1 -= 1
                left += 1
            }
            low(right) = left
        }

        val base = new Array[Long](n)
        for (i <- 0 until n) base(i) = i - low(i) + 1L

        // bucket indices by their low value
        val buckets = Array.fill(n + 1)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (i <- 0 until n) buckets(low(i)) += i

        // prefix sum of (i+1)
        val prefIdx = new Array[Long](n)
        var acc: Long = 0L
        for (i <- 0 until n) {
            acc += (i + 1).toLong
            prefIdx(i) = acc
        }

        case class Query(l: Int, r: Int, idx: Int)
        val qObjs = new Array[Query](queries.length)
        for (i <- queries.indices) {
            val arr = queries(i)
            qObjs(i) = Query(arr(0), arr(1), i)
        }
        scala.util.Sorting.stableSort(qObjs)(Ordering.by((q: Query) => -q.l))

        class BIT(size: Int) {
            private val tree = new Array[Long](size + 2)
            def add(idx: Int, delta: Long): Unit = {
                var i = idx + 1
                while (i <= size) {
                    tree(i) += delta
                    i += i & -i
                }
            }
            private def sumIdx(idx: Int): Long = {
                var res = 0L
                var i = idx + 1
                while (i > 0) {
                    res += tree(i)
                    i -= i & -i
                }
                res
            }
            def rangeSum(l: Int, r: Int): Long = {
                if (l > r) 0L else sumIdx(r) - (if (l > 0) sumIdx(l - 1) else 0L)
            }
        }

        val bitBase = new BIT(n)
        val bitIdx = new BIT(n)
        val bitCnt = new BIT(n)

        var curL = n
        val ans = new Array[Long](queries.length)

        for (q <- qObjs) {
            while (curL > q.l) {
                curL -= 1
                for (idx <- buckets(curL)) {
                    bitBase.add(idx, base(idx))
                    bitIdx.add(idx, (idx + 1).toLong)
                    bitCnt.add(idx, 1L)
                }
            }
            val L = q.l
            val R = q.r
            val len = R - L + 1
            val totalIdxSumAll = prefIdx(R) - (if (L > 0) prefIdx(L - 1) else 0L)

            val sumBaseActive = bitBase.rangeSum(L, R)
            val sumIdxActive = bitIdx.rangeSum(L, R)
            val cntActive = bitCnt.rangeSum(L, R)

            val baseline = totalIdxSumAll - L.toLong * len
            val answer = baseline + (sumBaseActive - sumIdxActive + L.toLong * cntActive)
            ans(q.idx) = answer
        }

        ans
    }
}
```

## Rust

```rust
use std::cmp::Ordering;

struct Fenwick {
    tree: Vec<i64>,
}
impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { tree: vec![0; n + 2] }
    }
    fn add(&mut self, mut idx: usize, delta: i64) {
        let n = self.tree.len();
        while idx < n {
            self.tree[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }
    fn sum(&self, mut idx: usize) -> i64 {
        let mut res = 0i64;
        while idx > 0 {
            res += self.tree[idx];
            idx &= idx - 1;
        }
        res
    }
    fn range_sum(&self, l: usize, r: usize) -> i64 {
        if r < l {
            0
        } else {
            self.sum(r) - self.sum(l - 1)
        }
    }
}

impl Solution {
    pub fn count_k_constraint_substrings(s: String, k: i32, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let k_usize = k as usize;

        // compute max_len for each start using two pointers
        let mut max_len = vec![0usize; n];
        let (mut cnt0, mut cnt1) = (0usize, 0usize);
        let mut r = 0usize;
        for i in 0..n {
            while r < n {
                let add0 = if bytes[r] == b'0' { 1 } else { 0 };
                let add1 = if bytes[r] == b'1' { 1 } else { 0 };
                let new0 = cnt0 + add0;
                let new1 = cnt1 + add1;
                if new0 > k_usize && new1 > k_usize {
                    break;
                }
                cnt0 = new0;
                cnt1 = new1;
                r += 1;
            }
            max_len[i] = r - i;
            // move left pointer
            if bytes[i] == b'0' {
                cnt0 -= 1;
            } else {
                cnt1 -= 1;
            }
        }

        // prepare positions sorted by end index
        let mut pos: Vec<(usize, usize)> = (0..n)
            .map(|i| (i + max_len[i] - 1, i))
            .collect();
        pos.sort_by(|a, b| a.0.cmp(&b.0));

        // prepare queries sorted by right endpoint
        let mut qvec: Vec<(usize, usize, usize)> = queries
            .into_iter()
            .enumerate()
            .map(|(idx, v)| (v[0] as usize, v[1] as usize, idx))
            .collect();
        qvec.sort_by(|a, b| a.1.cmp(&b.1));

        let mut bit_cnt = Fenwick::new(n + 2);
        let mut bit_sum = Fenwick::new(n + 2);

        let mut ans = vec![0i64; qvec.len()];
        let mut p_idx = 0usize;

        for (l, r, qi) in qvec {
            while p_idx < n && pos[p_idx].0 <= r {
                let end_i = pos[p_idx].0;
                let i = pos[p_idx].1;
                bit_cnt.add(i + 1, 1);
                bit_sum.add(i + 1, end_i as i64);
                p_idx += 1;
            }
            let cnt = bit_cnt.range_sum(l + 1, r + 1) as i64;
            let sum_end = bit_sum.range_sum(l + 1, r + 1);
            let len = (r - l + 1) as i64;
            let total = len * (len + 1) / 2;
            let subtract = cnt * (r as i64) - sum_end;
            ans[qi] = total - subtract;
        }

        // reorder to original order
        let mut result = vec![0i64; ans.len()];
        for ((_, _, idx), &val) in qvec.iter().zip(ans.iter()) {
            result[idx] = val;
        }
        result
    }
}
```

## Racket

```racket
(define (count-k-constraint-substrings s k queries)
  (define n (string-length s))
  ;; compute minimal right index where both counts exceed k
  (define bad-start (make-vector n n))
  (let ((right 0) (cnt0 0) (cnt1 0))
    (for ([left (in-range n)])
      (let loop ()
        (when (and (< right n)
                   (not (and (> cnt0 k) (> cnt1 k))))
          (define ch (string-ref s right))
          (if (char=? ch #\0)
              (set! cnt0 (+ cnt0 1))
              (set! cnt1 (+ cnt1 1)))
          (set! right (+ right 1))
          (loop)))
      (when (and (> cnt0 k) (> cnt1 k))
        (vector-set! bad-start left (- right 1))) ; minimal R = right-1
      ;; move left forward
      (define ch-left (string-ref s left))
      (if (char=? ch-left #\0)
          (set! cnt0 (- cnt0 1))
          (set! cnt1 (- cnt1 1)))))
  ;; collect positions with a valid bad start
  (define pairs '())
  (for ([i (in-range n)])
    (let ((b (vector-ref bad-start i)))
      (when (< b n)
        (set! pairs (cons (list b i) pairs)))))
  (define sorted-pairs (sort pairs (lambda (a b) (< (first a) (first b)))))
  (define m (length sorted-pairs))
  (define bvec (make-vector m))
  (define ivec (make-vector m))
  (for ([idx (in-range m)])
    (vector-set! bvec idx (first (list-ref sorted-pairs idx)))
    (vector-set! ivec idx (second (list-ref sorted-pairs idx))))
  ;; prepare queries with original indices
  (define qlist '())
  (let loop ((i 0) (qs queries))
    (when (< i (length qs))
      (define qr (list-ref qs i))
      (define l (first qr))
      (define r (second qr))
      (set! qlist (cons (list r l i) qlist))
      (loop (+ i 1) qs)))
  (define sorted-queries (sort qlist (lambda (a b) (< (first a) (first b)))))
  ;; Fenwick trees
  (define (make-fenwick size)
    (make-vector (+ size 1) 0))
  (define bitCnt (make-fenwick n))
  (define bitSum (make-fenwick n))
  (define (fenwick-add! tree idx delta)
    (let ((i (+ idx 1)))
      (let loop ((j i))
        (when (<= j n)
          (vector-set! tree j (+ (vector-ref tree j) delta))
          (loop (+ j (bitwise-and (- j) j)))))))
  (define (fenwick-sum tree idx)
    (if (< idx 0)
        0
        (let ((i (+ idx 1)))
          (let loop ((j i) (acc 0))
            (if (= j 0)
                acc
                (loop (- j (bitwise-and (- j) j)) (+ acc (vector-ref tree j))))))))
  ;; process queries
  (define answers (make-vector (length queries) 0))
  (let ((ptr 0))
    (for ([q sorted-queries])
      (define r (first q))
      (define l (second q))
      (define qid (third q))
      ;; insert all positions whose bad start <= r
      (let add-pairs ()
        (when (and (< ptr m) (<= (vector-ref bvec ptr) r))
          (define pos (vector-ref ivec ptr))
          (fenwick-add! bitCnt pos 1)
          (fenwick-add! bitSum pos (vector-ref bvec ptr))
          (set! ptr (+ ptr 1))
          (add-pairs)))
      ;; query counts in [l, r]
      (define cnt (- (fenwick-sum bitCnt r) (fenwick-sum bitCnt (- l 1))))
      (define sumb (- (fenwick-sum bitSum r) (fenwick-sum bitSum (- l 1))))
      (define total-bad (- (* cnt (+ r 1)) sumb))
      (define len (+ (- r l) 1))
      (define total (/ (* len (+ len 1)) 2))
      (vector-set! answers qid (- total total-bad)))))
  (vector->list answers))
```

## Erlang

```erlang
-spec count_k_constraint_substrings(S :: unicode:unicode_binary(), K :: integer(), Queries :: [[integer()]]) -> [integer()].
count_k_constraint_substrings(S, K, Queries) ->
    N = byte_size(S),
    BList = compute_b_list(S, K, N),

    %% prefix sum of B values stored in a map for O(1) access
    PrefixMap = build_prefix_map(BList),

    %% pairs {BValue, Position} sorted by BValue
    Pairs = lists:keysort(1,
        [{BVal, Idx} || {BVal, Idx} <- lists:zip(BList, lists:seq(0, N - 1))]),

    Q = length(Queries),
    QueriesIdx = [{L, R, Idx}
                  || {{L, R}, Idx} <- lists:zip(Queries, lists:seq(0, Q - 1))],
    SortedQueries = lists:keysort(1, QueriesIdx),

    CntTab = ets:new(cnt_tab, [private]),
    SumTab = ets:new(sum_tab, [private]),

    AnswerMap = process_queries(N, Pairs, SortedQueries,
                                CntTab, SumTab, PrefixMap, #{}),

    [maps:get(I, AnswerMap) || I <- lists:seq(0, Q - 1)].

%% --------------------------------------------------------------------
%% Compute B list where B[i] is the minimal left index for substrings ending at i
%% that satisfy min(cnt0,cnt1) <= K.
%% --------------------------------------------------------------------
compute_b_list(S, K, N) ->
    compute_b_loop(S, K, N, 0, 0, 0, 0, []).

compute_b_loop(_S, _K, N, R, _Left, _C0, _C1, Acc) when R =:= N ->
    lists:reverse(Acc);
compute_b_loop(S, K, N, R, Left, C0, C1, Acc) ->
    Char = binary:at(S, R),
    {C0a, C1a} =
        case Char of
            $0 -> {C0 + 1, C1};
            $1 -> {C0, C1 + 1}
        end,
    {NewLeft, NewC0, NewC1} = shrink(Left, C0a, C1a, S, K),
    compute_b_loop(S, K, N, R + 1, NewLeft, NewC0, NewC1, [NewLeft | Acc]).

shrink(L, C0, C1, _S, K) when erlang:min(C0, C1) =< K ->
    {L, C0, C1};
shrink(L, C0, C1, S, K) ->
    CharL = binary:at(S, L),
    case CharL of
        $0 -> shrink(L + 1, C0 - 1, C1, S, K);
        $1 -> shrink(L + 1, C0, C1 - 1, S, K)
    end.

%% --------------------------------------------------------------------
%% Build map Index -> prefix sum of B up to that index.
%% --------------------------------------------------------------------
build_prefix_map(BList) ->
    build_prefix_map(lists:seq(0, length(BList) - 1), BList, 0, #{}).

build_prefix_map([], [], _Acc, Map) ->
    Map;
build_prefix_map([Idx | RestIdx], [Val | RestVals], Acc, Map) ->
    NewAcc = Acc + Val,
    NewMap = maps:put(Idx, NewAcc, Map),
    build_prefix_map(RestIdx, RestVals, NewAcc, NewMap).

%% --------------------------------------------------------------------
%% Process all queries offline.
%% --------------------------------------------------------------------
process_queries(N, Pairs, Queries, CntTab, SumTab, PrefixMap, AnsMap) ->
    process_queries_loop(Pairs, Queries, CntTab, SumTab,
                         N, PrefixMap, AnsMap).

process_queries_loop(_Pairs, [], _CntTab, _SumTab, _N, _PrefixMap, AnsMap) ->
    AnsMap;
process_queries_loop(Pairs, [{L, R, Idx} | RestQ],
                    CntTab, SumTab, N, PrefixMap, AnsMap) ->

    {NewPairs, CntTab1, SumTab1} = add_until(Pairs, L, CntTab, SumTab, N),

    Len = R - L + 1,
    TotalIdx = ((R + 1) * (R + 2) div 2) - (L * (L + 1) div 2),

    PrefixR = maps:get(R, PrefixMap),
    PrefixLm1 =
        case L of
            0 -> 0;
            _ -> maps:get(L - 1, PrefixMap)
        end,
    TotalBRange = PrefixR - PrefixLm1,

    CntRemoved = bit_range(CntTab1, N, L, R),
    SumRemoved = bit_range(SumTab1, N, L, R),

    Ans = TotalIdx - TotalBRange - L * CntRemoved + SumRemoved,
    NewAnsMap = maps:put(Idx, Ans, AnsMap),

    process_queries_loop(NewPairs, RestQ, CntTab1, SumTab1,
                         N, PrefixMap, NewAnsMap).

%% --------------------------------------------------------------------
%% Add all pairs with B <= Limit to the BITs.
%% --------------------------------------------------------------------
add_until(Pairs, Limit, CntTab, SumTab, N) ->
    add_until(Pairs, Limit, CntTab, SumTab, N, []).

add_until([], _Limit, CntTab, SumTab, _N, AccRemoved) ->
    {lists:reverse(AccRemoved), CntTab, SumTab};
add_until([{BVal, Pos} = Pair | Rest], Limit, CntTab, SumTab, N, AccRemoved)
        when BVal =< Limit ->
    bit_update(CntTab, N, Pos, 1),
    bit_update(SumTab, N, Pos, BVal),
    add_until(Rest, Limit, CntTab, SumTab, N, [Pair | AccRemoved]);
add_until(Pairs, _Limit, CntTab, SumTab, _N, AccRemoved) ->
    {Pairs ++ lists:reverse(AccRemoved), CntTab, SumTab}.

%% --------------------------------------------------------------------
%% Fenwick tree operations using ETS tables.
%% --------------------------------------------------------------------
bit_update(Tab, N, Pos, Delta) ->
    I0 = Pos + 1,
    bit_update_loop(Tab, N, I0, Delta).

bit_update_loop(_Tab, N, I, _Delta) when I > N ->
    ok;
bit_update_loop(Tab, N, I, Delta) ->
    ets:update_counter(Tab, I, {2, Delta}, {I, 0}),
    Next = I + (I band (-I)),
    bit_update_loop(Tab, N, Next, Delta).

bit_prefix(Tab, Pos) when Pos < 0 ->
    0;
bit_prefix(Tab, Pos) ->
    I0 = Pos + 1,
    bit_prefix_loop(Tab, I0, 0).

bit_prefix_loop(_Tab, 0, Acc) ->
    Acc;
bit_prefix_loop(Tab, I, Acc) ->
    Val =
        case ets:lookup(Tab, I) of
            [] -> 0;
            [{I, V}] -> V
        end,
    Next = I - (I band (-I)),
    bit_prefix_loop(Tab, Next, Acc + Val).

bit_range(Tab, N, L, R) ->
    PrefixR = bit_prefix(Tab, R),
    PrefixL1 =
        case L of
            0 -> 0;
            _ -> bit_prefix(Tab, L - 1)
        end,
    PrefixR - PrefixL1.
```

## Elixir

```elixir
defmodule BIT do
  def new(size), do: %{size: size, tree: %{}}

  def add(bit, idx, delta) do
    i = idx + 1
    new_tree = add_loop(bit.tree, i, delta, bit.size)
    %{bit | tree: new_tree}
  end

  defp add_loop(tree, i, delta, size) when i <= size do
    t = Map.update(tree, i, delta, &(&1 + delta))
    add_loop(t, i + (i &&& -i), delta, size)
  end

  defp add_loop(tree, _i, _delta, _size), do: tree

  def sum(bit, idx) when idx >= 0 do
    i = idx + 1
    sum_loop(bit.tree, i, 0)
  end

  defp sum_loop(_tree, i, acc) when i <= 0, do: acc

  defp sum_loop(tree, i, acc) do
    val = Map.get(tree, i, 0)
    sum_loop(tree, i - (i &&& -i), acc + val)
  end

  def range_sum(bit, l, r) when l <= r do
    s_r = sum(bit, r)
    s_l = if l > 0, do: sum(bit, l - 1), else: 0
    s_r - s_l
  end
end

defmodule Solution do
  @spec count_k_constraint_substrings(s :: String.t(), k :: integer(), queries :: [[integer]]) :: [integer]
  def count_k_constraint_substrings(s, k, queries) do
    n = String.length(s)

    chars =
      :binary.bin_to_list(s)
      |> Enum.map(fn c -> if c == ?0, do: 0, else: 1 end)

    # compute leftmost valid start for each right endpoint
    a_array = compute_lefts(chars, k, n)

    {pref_array, pairs} = build_prefix_and_pairs(a_array, n)

    sorted_pairs = Enum.sort_by(pairs, fn {left, _idx} -> left end)
    queries_with_idx =
      Enum.with_index(queries)
      |> Enum.map(fn {{l, r}, idx} -> %{l: l, r: r, idx: idx} end)
      |> Enum.sort_by(& &1.l)

    bit_cnt = BIT.new(n)
    bit_sum = BIT.new(n)

    {_, _, ans_map} =
      Enum.reduce(queries_with_idx, {0, bit_cnt, bit_sum, %{}}, fn q,
                                                                 {ptr, bc, bs, am} ->
        {new_ptr, new_bc, new_bs} = advance(ptr, sorted_pairs, q.l, bc, bs)

        cnt = BIT.range_sum(new_bc, q.l, q.r)
        sum_left = BIT.range_sum(new_bs, q.l, q.r)

        total_base =
          :array.get(q.r, pref_array) -
            (if q.l > 0, do: :array.get(q.l - 1, pref_array), else: 0)

        ans = total_base - (cnt * q.l - sum_left)
        {new_ptr, new_bc, new_bs, Map.put(am, q.idx, ans)}
      end)

    Enum.map(0..length(queries) - 1, fn i -> Map.fetch!(ans_map, i) end)
  end

  defp compute_lefts(chars, k, n) do
    a = :array.new(n)

    state = %{
      lz: 0,
      zc: 0,
      lo: 0,
      oc: 0,
      arr: a
    }

    Enum.reduce(0..n - 1, state, fn i, st ->
      c = Enum.at(chars, i)

      {zc, oc} =
        case c do
          0 -> {st.zc + 1, st.oc}
          1 -> {st.zc, st.oc + 1}
        end

      {lz, zc2} = adjust_zero(st.lz, zc, chars, k)
      {lo, oc2} = adjust_one(st.lo, oc, chars, k)

      min_left = if lz < lo, do: lz, else: lo
      arr2 = :array.set(i, min_left, st.arr)

      %{lz: lz, zc: zc2, lo: lo, oc: oc2, arr: arr2}
    end)
    |> Map.get(:arr)
  end

  defp adjust_zero(lz, zc, chars, k) when zc > k do
    c0 = Enum.at(chars, lz)

    zc2 =
      if c0 == 0, do: zc - 1, else: zc

    adjust_zero(lz + 1, zc2, chars, k)
  end

  defp adjust_zero(lz, zc, _chars, _k), do: {lz, zc}

  defp adjust_one(lo, oc, chars, k) when oc > k do
    c0 = Enum.at(chars, lo)

    oc2 =
      if c0 == 1, do: oc - 1, else: oc

    adjust_one(lo + 1, oc2, chars, k)
  end

  defp adjust_one(lo, oc, _chars, _k), do: {lo, oc}

  defp build_prefix_and_pairs(a_array, n) do
    pref = :array.new(n)

    {pref_arr, pairs} =
      Enum.reduce(0..n - 1, {%{sum: 0, arr: pref}, []}, fn i, acc ->
        left = :array.get(i, a_array)
        base = i - left + 1
        new_sum = acc.sum + base
        new_arr = :array.set(i, new_sum, acc.arr)
        { %{sum: new_sum, arr: new_arr}, [{left, i} | acc.pairs] }
      end)

    {pref_arr, Enum.reverse(pairs)}
  end

  defp advance(ptr, pairs, l, bc, bs) do
    if ptr < length(pairs) do
      {left, idx} = Enum.at(pairs, ptr)

      if left < l do
        new_bc = BIT.add(bc, idx, 1)
        new_bs = BIT.add(bs, idx, left)
        advance(ptr + 1, pairs, l, new_bc, new_bs)
      else
        {ptr, bc, bs}
      end
    else
      {ptr, bc, bs}
    end
  end
end
```

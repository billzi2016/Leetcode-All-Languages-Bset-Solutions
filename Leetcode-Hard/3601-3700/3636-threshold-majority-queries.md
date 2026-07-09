# 3636. Threshold Majority Queries

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class SegTree {
public:
    int n;
    vector<int> seg;
    SegTree(int _n = 0) { init(_n); }
    void init(int _n) {
        n = _n;
        seg.assign(4 * (n + 1), 0);
    }
    void setVal(int idx, int val) { update(1, 0, n, idx, val); }
    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            seg[node] = val;
            return;
        }
        int mid = (l + r) >> 1;
        if (idx <= mid) update(node << 1, l, mid, idx, val);
        else update(node << 1 | 1, mid + 1, r, idx, val);
        seg[node] = seg[node << 1] | seg[node << 1 | 1];
    }
    int queryMax(int ql, int qr) { return queryMaxRec(1, 0, n, ql, qr); }
    int queryMaxRec(int node, int l, int r, int ql, int qr) {
        if (r < ql || l > qr || seg[node] == 0) return -1;
        if (l == r) return l;
        int mid = (l + r) >> 1;
        int res = queryMaxRec(node << 1 | 1, mid + 1, r, ql, qr);
        if (res != -1) return res;
        return queryMaxRec(node << 1, l, mid, ql, qr);
    }
};

class Solution {
public:
    vector<int> subarrayMajority(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        struct Q {int l,r,thr,idx;};
        int m = queries.size();
        vector<Q> qs(m);
        for (int i=0;i<m;++i){
            qs[i]={queries[i][0],queries[i][1],queries[i][2],i};
        }
        int B = max(1,(int)sqrt(n));
        sort(qs.begin(),qs.end(),[&](const Q& a,const Q& b){
            int ba=a.l/B, bb=b.l/B;
            if (ba!=bb) return ba<bb;
            if (ba&1) return a.r>b.r;
            return a.r<b.r;
        });
        vector<int> ans(m,-1);
        unordered_map<int,int> cnt;
        vector<int> freqCnt(n+2,0);
        vector< set<int> > bucket(n+2);
        SegTree seg(n+1);
        auto add = [&](int pos){
            int x=nums[pos];
            int old = cnt[x];
            int nw = old+1;
            cnt[x]=nw;
            if(old>0){
                bucket[old].erase(x);
                freqCnt[old]--;
                if(freqCnt[old]==0) seg.setVal(old,0);
            }
            bucket[nw].insert(x);
            freqCnt[nw]++;
            if(freqCnt[nw]==1) seg.setVal(nw,1);
        };
        auto remove = [&](int pos){
            int x=nums[pos];
            int old = cnt[x];
            int nw = old-1;
            // old must be >0
            bucket[old].erase(x);
            freqCnt[old]--;
            if(freqCnt[old]==0) seg.setVal(old,0);
            if(nw>0){
                cnt[x]=nw;
                bucket[nw].insert(x);
                freqCnt[nw]++;
                if(freqCnt[nw]==1) seg.setVal(nw,1);
            }else{
                cnt.erase(x);
            }
        };
        int curL=0,curR=-1;
        for (auto &q: qs){
            while (curL>q.l) add(--curL);
            while (curR<q.r) add(++curR);
            while (curL<q.l) remove(curL++);
            while (curR>q.r) remove(curR--);
            int maxFreq = seg.queryMax(q.thr, n);
            if (maxFreq==-1){
                ans[q.idx]=-1;
            }else{
                ans[q.idx]=*bucket[maxFreq].begin();
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Query {
        int l, r, t, idx, block;
        Query(int l, int r, int t, int idx, int block) {
            this.l = l;
            this.r = r;
            this.t = t;
            this.idx = idx;
            this.block = block;
        }
    }

    public int[] subarrayMajority(int[] nums, int[][] queries) {
        int n = nums.length;
        int qn = queries.length;
        int B = (int) Math.sqrt(n) + 1;

        Query[] qs = new Query[qn];
        for (int i = 0; i < qn; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            int t = queries[i][2];
            qs[i] = new Query(l, r, t, i, l / B);
        }

        java.util.Arrays.sort(qs, (a, b) -> {
            if (a.block != b.block) return Integer.compare(a.block, b.block);
            return Integer.compare(a.r, b.r);
        });

        int[] ans = new int[qn];

        // frequency map
        java.util.HashMap<Integer, Integer> cnt = new java.util.HashMap<>();
        // bucket of values per frequency
        @SuppressWarnings("unchecked")
        java.util.TreeSet<Integer>[] bucket = new java.util.TreeSet[n + 2];
        for (int i = 0; i < bucket.length; i++) {
            bucket[i] = new java.util.TreeSet<>();
        }
        int maxF = 0;

        int curL = 0, curR = -1;
        for (Query qq : qs) {
            while (curL > qq.l) add(--curL);
            while (curR < qq.r) add(++curR);
            while (curL < qq.l) remove(curL++);
            while (curR > qq.r) remove(curR--);

            if (maxF >= qq.t && !bucket[maxF].isEmpty()) {
                ans[qq.idx] = bucket[maxF].first();
            } else {
                ans[qq.idx] = -1;
            }
        }

        return ans;

        // Helper methods capture outer variables
        void add(int pos) {
            int x = nums[pos];
            int old = cnt.getOrDefault(x, 0);
            int nw = old + 1;
            cnt.put(x, nw);
            if (old > 0) bucket[old].remove(x);
            bucket[nw].add(x);
            if (nw > maxF) maxF = nw;
        }

        void remove(int pos) {
            int x = nums[pos];
            int old = cnt.get(x); // must exist
            int nw = old - 1;
            bucket[old].remove(x);
            if (nw > 0) {
                bucket[nw].add(x);
                cnt.put(x, nw);
            } else {
                cnt.remove(x);
            }
            while (maxF > 0 && bucket[maxF].isEmpty()) maxF--;
        }
    }
}
```

## Python

```python
class Solution(object):
    def subarrayMajority(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import math
        n = len(nums)
        q = len(queries)
        block = int(math.sqrt(n)) + 1

        # augment queries with original index
        qs = [(l, r, t, i) for i, (l, r, t) in enumerate(queries)]
        qs.sort(key=lambda x: (x[0] // block, x[1]))

        # frequency of each value in current window
        cnt = {}
        maxFreqPossible = n
        bucket = [set() for _ in range(maxFreqPossible + 2)]   # bucket[f] = set of values with freq f
        freqCount = [0] * (maxFreqPossible + 2)                # number of values having frequency f

        # segment tree to query max frequency with non‑empty bucket
        size = 1
        while size < maxFreqPossible + 2:
            size <<= 1
        seg = [-1] * (2 * size)

        def seg_update(f):
            """set leaf f according to freqCount[f]"""
            pos = f + size
            seg[pos] = f if freqCount[f] > 0 else -1
            pos //= 2
            while pos:
                left, right = seg[2 * pos], seg[2 * pos + 1]
                seg[pos] = left if left >= right else right
                pos //= 2

        def seg_query(l, r):
            """max frequency in [l, r]; -1 if none"""
            l += size
            r += size
            res = -1
            while l <= r:
                if (l & 1) == 1:
                    if seg[l] > res:
                        res = seg[l]
                    l += 1
                if (r & 1) == 0:
                    if seg[r] > res:
                        res = seg[r]
                    r -= 1
                l //= 2
                r //= 2
            return res

        def add(pos):
            v = nums[pos]
            old = cnt.get(v, 0)
            new = old + 1
            cnt[v] = new

            if old > 0:
                bucket[old].remove(v)
                freqCount[old] -= 1
                seg_update(old)

            bucket[new].add(v)
            freqCount[new] += 1
            seg_update(new)

        def remove(pos):
            v = nums[pos]
            old = cnt[v]
            new = old - 1

            bucket[old].remove(v)
            freqCount[old] -= 1
            seg_update(old)

            if new == 0:
                del cnt[v]
            else:
                cnt[v] = new
                bucket[new].add(v)
                freqCount[new] += 1
                seg_update(new)

        ans = [-1] * q
        curL, curR = 0, -1

        for l, r, thr, idx in qs:
            while curL > l:
                curL -= 1
                add(curL)
            while curR < r:
                curR += 1
                add(curR)
            while curL < l:
                remove(curL)
                curL += 1
            while curR > r:
                remove(curR)
                curR -= 1

            f = seg_query(thr, maxFreqPossible)
            if f != -1:
                ans[idx] = min(bucket[f])
            else:
                ans[idx] = -1

        return ans
```

## Python3

```python
from typing import List
import math
import heapq

class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)
        block = int(math.sqrt(n)) + 1

        # Prepare queries with original index
        qs = [(l // block, r, l, r, t, i) for i, (l, r, t) in enumerate(queries)]
        qs.sort(key=lambda x: (x[0], x[1]))

        # Fenwick Tree for frequency counts
        class BIT:
            def __init__(self, size):
                self.n = size
                self.bit = [0] * (size + 2)

            def add(self, idx, delta):
                while idx <= self.n:
                    self.bit[idx] += delta
                    idx += idx & -idx

            def sum(self, idx):
                s = 0
                while idx > 0:
                    s += self.bit[idx]
                    idx -= idx & -idx
                return s

        maxFreqPossible = n
        bit = BIT(maxFreqPossible)

        cnt = {}                     # value -> current frequency in window
        heaps = [[] for _ in range(maxFreqPossible + 1)]   # heaps[f] holds values with freq f (lazy)

        def add_pos(pos):
            val = nums[pos]
            old = cnt.get(val, 0)
            new = old + 1
            cnt[val] = new
            if old > 0:
                bit.add(old, -1)
            bit.add(new, 1)
            heapq.heappush(heaps[new], val)

        def remove_pos(pos):
            val = nums[pos]
            old = cnt[val]
            new = old - 1
            if new == 0:
                del cnt[val]
            else:
                cnt[val] = new
                heapq.heappush(heaps[new], val)
            bit.add(old, -1)
            if new > 0:
                bit.add(new, 1)

        def query_threshold(t):
            total = bit.sum(maxFreqPossible)
            if total - bit.sum(t - 1) == 0:
                return -1
            low, high = t, maxFreqPossible
            while low < high:
                mid = (low + high + 1) // 2
                if total - bit.sum(mid - 1) > 0:
                    low = mid
                else:
                    high = mid - 1
            f = low
            heap = heaps[f]
            while heap and cnt.get(heap[0], 0) != f:
                heapq.heappop(heap)
            return heap[0] if heap else -1

        ans = [0] * q
        curL, curR = 0, -1
        for _, _, l, r, t, idx in qs:
            while curL > l:
                curL -= 1
                add_pos(curL)
            while curR < r:
                curR += 1
                add_pos(curR)
            while curL < l:
                remove_pos(curL)
                curL += 1
            while curR > r:
                remove_pos(curR)
                curR -= 1
            ans[idx] = query_threshold(t)

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

typedef struct {
    int l, r, thr, idx;
} Query;

static int blockSize;

/* integer compare for qsort */
static int cmpInt(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

/* query comparator for Mo's algorithm */
static int cmpQuery(const void *a, const void *b) {
    const Query *qa = (const Query *)a;
    const Query *qb = (const Query *)b;
    int block_a = qa->l / blockSize;
    int block_b = qb->l / blockSize;
    if (block_a != block_b) return block_a - block_b;
    if (block_a & 1)
        return qb->r - qa->r;   /* descending r for odd blocks */
    else
        return qa->r - qb->r;   /* ascending r for even blocks */
}

/* segment tree structures */
static int *cntTree;   /* counts */
static int *valTree;   /* smallest value achieving the count */
static int segSize;    /* leaf offset */

/* update a leaf (compressed index) with new count */
static void segUpdate(int idx, int newCnt) {
    int pos = segSize + idx;
    cntTree[pos] = newCnt;
    pos >>= 1;
    while (pos) {
        int left = pos << 1, right = left | 1;
        if (cntTree[left] > cntTree[right]) {
            cntTree[pos] = cntTree[left];
            valTree[pos] = valTree[left];
        } else if (cntTree[left] < cntTree[right]) {
            cntTree[pos] = cntTree[right];
            valTree[pos] = valTree[right];
        } else { /* equal counts, choose smaller value */
            cntTree[pos] = cntTree[left];
            valTree[pos] = (valTree[left] < valTree[right]) ? valTree[left] : valTree[right];
        }
        pos >>= 1;
    }
}

/* add element at position pos to current window */
static void addPos(int pos, int *comp, int *cntArr) {
    int idx = comp[pos];
    cntArr[idx]++;
    segUpdate(idx, cntArr[idx]);
}

/* remove element at position pos from current window */
static void removePos(int pos, int *comp, int *cntArr) {
    int idx = comp[pos];
    cntArr[idx]--;
    segUpdate(idx, cntArr[idx]);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* subarrayMajority(int* nums, int numsSize, int** queries, int queriesSize,
                      int* queriesColSize, int* returnSize) {
    *returnSize = queriesSize;
    int *answer = (int *)malloc(sizeof(int) * queriesSize);

    /* ----- coordinate compression ----- */
    int *tmp = (int *)malloc(sizeof(int) * numsSize);
    memcpy(tmp, nums, sizeof(int) * numsSize);
    qsort(tmp, numsSize, sizeof(int), cmpInt);
    int *uniqVals = (int *)malloc(sizeof(int) * numsSize);
    int m = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || tmp[i] != tmp[i - 1])
            uniqVals[m++] = tmp[i];
    }
    free(tmp);

    int *comp = (int *)malloc(sizeof(int) * numsSize);
    for (int i = 0; i < numsSize; ++i) {
        int lo = 0, hi = m - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            if (uniqVals[mid] == nums[i]) { comp[i] = mid; break; }
            else if (uniqVals[mid] < nums[i]) lo = mid + 1;
            else hi = mid - 1;
        }
    }

    /* ----- segment tree initialization ----- */
    segSize = 1;
    while (segSize < m) segSize <<= 1;
    cntTree = (int *)calloc(2 * segSize, sizeof(int));
    valTree = (int *)malloc(sizeof(int) * 2 * segSize);
    for (int i = 0; i < segSize; ++i) {
        if (i < m) valTree[segSize + i] = uniqVals[i];
        else valTree[segSize + i] = INT_MAX;
    }
    for (int i = segSize - 1; i > 0; --i) {
        int left = i << 1, right = left | 1;
        if (cntTree[left] > cntTree[right]) {
            cntTree[i] = cntTree[left];
            valTree[i] = valTree[left];
        } else if (cntTree[left] < cntTree[right]) {
            cntTree[i] = cntTree[right];
            valTree[i] = valTree[right];
        } else {
            cntTree[i] = cntTree[left];
            valTree[i] = (valTree[left] < valTree[right]) ? valTree[left] : valTree[right];
        }
    }

    /* ----- prepare queries for Mo's algorithm ----- */
    Query *qarr = (Query *)malloc(sizeof(Query) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        qarr[i].l = queries[i][0];
        qarr[i].r = queries[i][1];
        qarr[i].thr = queries[i][2];
        qarr[i].idx = i;
    }
    blockSize = (int)sqrt((double)numsSize) + 1;
    qsort(qarr, queriesSize, sizeof(Query), cmpQuery);

    /* ----- Mo's processing ----- */
    int *cntArr = (int *)calloc(m, sizeof(int));
    int curL = 0, curR = -1;
    for (int i = 0; i < queriesSize; ++i) {
        Query q = qarr[i];
        while (curL > q.l) addPos(--curL, comp, cntArr);
        while (curR < q.r) addPos(++curR, comp, cntArr);
        while (curL < q.l) removePos(curL++, comp, cntArr);
        while (curR > q.r) removePos(curR--, comp, cntArr);

        int maxCnt = cntTree[1];
        int bestVal = valTree[1];
        answer[q.idx] = (maxCnt >= q.thr) ? bestVal : -1;
    }

    /* ----- cleanup ----- */
    free(comp);
    free(uniqVals);
    free(cntArr);
    free(qarr);
    free(cntTree);
    free(valTree);

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private class ValComparer : IComparer<int>
    {
        private readonly int[] _vals;
        public ValComparer(int[] vals) => _vals = vals;
        public int Compare(int a, int b)
        {
            int ca = _vals[a];
            int cb = _vals[b];
            if (ca != cb) return ca.CompareTo(cb);
            return a.CompareTo(b);
        }
    }

    private struct Query
    {
        public int L, R, Thr, Id;
    }

    public int[] SubarrayMajority(int[] nums, int[][] queries)
    {
        int n = nums.Length;

        // coordinate compression
        var map = new Dictionary<int, int>();
        var uniqList = new List<int>();
        foreach (var v in nums)
        {
            if (!map.ContainsKey(v))
            {
                map[v] = uniqList.Count;
                uniqList.Add(v);
            }
        }
        int[] comp = new int[n];
        for (int i = 0; i < n; i++) comp[i] = map[nums[i]];
        int[] origVals = uniqList.ToArray();

        // prepare queries
        int qn = queries.Length;
        Query[] qs = new Query[qn];
        for (int i = 0; i < qn; i++)
        {
            qs[i].L = queries[i][0];
            qs[i].R = queries[i][1];
            qs[i].Thr = queries[i][2];
            qs[i].Id = i;
        }

        int blockSize = (int)Math.Sqrt(n) + 1;
        Array.Sort(qs, (a, b) =>
        {
            int blockA = a.L / blockSize;
            int blockB = b.L / blockSize;
            if (blockA != blockB) return blockA - blockB;
            // optional Hilbert order improvement
            return (blockA & 1) == 0 ? a.R - b.R : b.R - a.R;
        });

        int[] cnt = new int[uniqList.Count];
        var comparer = new ValComparer(origVals);
        SortedSet<int>[] buckets = new SortedSet<int>[n + 2]; // frequency up to n
        var freqSet = new SortedSet<int>();

        void Add(int pos)
        {
            int id = comp[pos];
            int old = cnt[id];
            if (old > 0)
            {
                var setOld = buckets[old];
                setOld.Remove(id);
                if (setOld.Count == 0) freqSet.Remove(old);
            }
            cnt[id]++;
            int nw = cnt[id];
            if (buckets[nw] == null) buckets[nw] = new SortedSet<int>(comparer);
            bool wasEmpty = buckets[nw].Count == 0;
            buckets[nw].Add(id);
            if (wasEmpty) freqSet.Add(nw);
        }

        void Remove(int pos)
        {
            int id = comp[pos];
            int old = cnt[id];
            var setOld = buckets[old];
            setOld.Remove(id);
            if (setOld.Count == 0) freqSet.Remove(old);
            cnt[id]--;
            int nw = cnt[id];
            if (nw > 0)
            {
                if (buckets[nw] == null) buckets[nw] = new SortedSet<int>(comparer);
                bool wasEmpty = buckets[nw].Count == 0;
                buckets[nw].Add(id);
                if (wasEmpty) freqSet.Add(nw);
            }
        }

        int[] answer = new int[qn];
        int curL = 0, curR = -1;

        foreach (var q in qs)
        {
            while (curL > q.L) { curL--; Add(curL); }
            while (curR < q.R) { curR++; Add(curR); }
            while (curL < q.L) { Remove(curL); curL++; }
            while (curR > q.R) { Remove(curR); curR--; }

            int ans = -1;
            var view = freqSet.GetViewBetween(q.Thr, n);
            if (view.Count > 0)
            {
                int bestFreq = view.Max;
                int id = buckets[bestFreq].Min; // smallest original value
                ans = origVals[id];
            }
            answer[q.Id] = ans;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var subarrayMajority = function(nums, queries) {
    const n = nums.length;
    // coordinate compression
    const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
    const m = uniq.length;
    const valToIdx = new Map();
    for (let i = 0; i < m; ++i) valToIdx.set(uniq[i], i);

    // segment tree arrays
    const maxSeg = new Int32Array(4 * m);
    const minSeg = new Float64Array(4 * m);
    for (let i = 0; i < minSeg.length; ++i) minSeg[i] = Infinity;

    function update(node, l, r, idx, cnt) {
        if (l === r) {
            maxSeg[node] = cnt;
            minSeg[node] = cnt > 0 ? uniq[idx] : Infinity;
            return;
        }
        const mid = (l + r) >> 1;
        if (idx <= mid) update(node << 1, l, mid, idx, cnt);
        else update((node << 1) | 1, mid + 1, r, idx, cnt);

        const leftNode = node << 1;
        const rightNode = leftNode | 1;
        const leftMax = maxSeg[leftNode];
        const rightMax = maxSeg[rightNode];
        if (leftMax > rightMax) {
            maxSeg[node] = leftMax;
            minSeg[node] = minSeg[leftNode];
        } else if (rightMax > leftMax) {
            maxSeg[node] = rightMax;
            minSeg[node] = minSeg[rightNode];
        } else {
            maxSeg[node] = leftMax; // equal
            const lm = minSeg[leftNode];
            const rm = minSeg[rightNode];
            minSeg[node] = Math.min(lm, rm);
        }
    }

    const freq = new Int32Array(m);

    function add(pos) {
        const idx = valToIdx.get(nums[pos]);
        freq[idx]++;
        update(1, 0, m - 1, idx, freq[idx]);
    }

    function remove(pos) {
        const idx = valToIdx.get(nums[pos]);
        freq[idx]--;
        update(1, 0, m - 1, idx, freq[idx]);
    }

    // Mo's algorithm
    const B = Math.floor(Math.sqrt(n));
    const qObjs = queries.map((q, i) => ({ l: q[0], r: q[1], t: q[2], id: i }));
    qObjs.sort((a, b) => {
        const blockA = (a.l / B) | 0;
        const blockB = (b.l / B) | 0;
        if (blockA !== blockB) return blockA - blockB;
        // zigzag ordering
        if (blockA & 1) return b.r - a.r;
        return a.r - b.r;
    });

    const ans = new Array(queries.length);
    let curL = 0, curR = -1;

    for (const q of qObjs) {
        while (curL > q.l) add(--curL);
        while (curR < q.r) add(++curR);
        while (curL < q.l) remove(curL++);
        while (curR > q.r) remove(curR--);

        const maxCnt = maxSeg[1];
        if (maxCnt >= q.t) ans[q.id] = minSeg[1];
        else ans[q.id] = -1;
    }

    return ans;
};
```

## Typescript

```typescript
function subarrayMajority(nums: number[], queries: number[][]): number[] {
    const n = nums.length;
    const q = queries.length;
    const blockSize = Math.floor(Math.sqrt(n)) || 1;

    type Query = { l: number; r: number; t: number; idx: number };
    const qs: Query[] = new Array(q);
    for (let i = 0; i < q; ++i) {
        const [l, r, t] = queries[i];
        qs[i] = { l, r, t, idx: i };
    }

    qs.sort((a, b) => {
        const blockA = Math.floor(a.l / blockSize);
        const blockB = Math.floor(b.l / blockSize);
        if (blockA !== blockB) return blockA - blockB;
        return a.r - b.r;
    });

    const cnt = new Map<number, number>();
    const buckets: Array<Set<number>> = new Array(n + 2);
    const minVal: number[] = new Array(n + 2).fill(Infinity);
    let maxFreq = 0;

    function add(pos: number): void {
        const v = nums[pos];
        const old = cnt.get(v) ?? 0;
        const nw = old + 1;
        cnt.set(v, nw);

        if (old > 0) {
            const setOld = buckets[old]!;
            setOld.delete(v);
            if (setOld.size === 0) {
                minVal[old] = Infinity;
            } else if (v === minVal[old]) {
                let m = Infinity;
                for (const x of setOld) if (x < m) m = x;
                minVal[old] = m;
            }
        }

        let setNew = buckets[nw];
        if (!setNew) {
            setNew = new Set<number>();
            buckets[nw] = setNew;
        }
        setNew.add(v);
        if (v < minVal[nw]) minVal[nw] = v;

        if (nw > maxFreq) maxFreq = nw;
    }

    function remove(pos: number): void {
        const v = nums[pos];
        const old = cnt.get(v)!;
        const nw = old - 1;

        const setOld = buckets[old]!;
        setOld.delete(v);
        if (setOld.size === 0) {
            minVal[old] = Infinity;
        } else if (v === minVal[old]) {
            let m = Infinity;
            for (const x of setOld) if (x < m) m = x;
            minVal[old] = m;
        }

        if (nw > 0) {
            let setNew = buckets[nw];
            if (!setNew) {
                setNew = new Set<number>();
                buckets[nw] = setNew;
            }
            setNew.add(v);
            if (v < minVal[nw]) minVal[nw] = v;
            cnt.set(v, nw);
        } else {
            cnt.delete(v);
        }

        while (maxFreq > 0 && (!buckets[maxFreq] || buckets[maxFreq]!.size === 0)) {
            maxFreq--;
        }
    }

    const ans: number[] = new Array(q);
    let curL = 0, curR = -1;

    for (const query of qs) {
        while (curL > query.l) add(--curL);
        while (curR < query.r) add(++curR);
        while (curL < query.l) remove(curL++);
        while (curR > query.r) remove(curR--);

        if (maxFreq < query.t) {
            ans[query.idx] = -1;
        } else {
            ans[query.idx] = minVal[maxFreq];
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function subarrayMajority($nums, $queries) {
        $n = count($nums);
        // coordinate compression
        $unique = array_values(array_unique($nums));
        sort($unique);
        $map = [];
        foreach ($unique as $i => $v) {
            $map[$v] = $i;
        }
        $m = count($unique);
        $compNums = [];
        foreach ($nums as $v) {
            $compNums[] = $map[$v];
        }
        $origVals = $unique; // id -> original value

        // prepare queries with index
        $qs = [];
        foreach ($queries as $idx => $q) {
            $qs[] = ['l' => $q[0], 'r' => $q[1], 't' => $q[2], 'i' => $idx];
        }

        $B = intval(sqrt($n)) + 1;
        usort($qs, function ($a, $b) use ($B) {
            $ba = intdiv($a['l'], $B);
            $bb = intdiv($b['l'], $B);
            if ($ba == $bb) {
                return $a['r'] <=> $b['r'];
            }
            return $ba <=> $bb;
        });

        // data structures
        $cnt = array_fill(0, $m, 0);          // count per value id
        $bucket = [];                         // freq => set of ids
        $minVal = [];                         // freq => smallest original value in that bucket
        $currentMaxFreq = 0;

        $add = function ($pos) use (&$compNums, &$cnt, &$bucket, &$minVal, &$origVals, &$currentMaxFreq) {
            $id = $compNums[$pos];
            $old = $cnt[$id];
            $new = $old + 1;
            $cnt[$id] = $new;

            if ($old > 0) {
                unset($bucket[$old][$id]);
                if (isset($minVal[$old])) {
                    $val = $origVals[$id];
                    if ($val == $minVal[$old]) {
                        if (!empty($bucket[$old])) {
                            $newMin = PHP_INT_MAX;
                            foreach ($bucket[$old] as $iid => $_) {
                                $v = $origVals[$iid];
                                if ($v < $newMin) $newMin = $v;
                            }
                            $minVal[$old] = $newMin;
                        } else {
                            unset($bucket[$old]);
                            unset($minVal[$old]);
                        }
                    } else {
                        if (empty($bucket[$old])) {
                            unset($bucket[$old]);
                            unset($minVal[$old]);
                        }
                    }
                }
            }

            $bucket[$new][$id] = true;
            $valNew = $origVals[$id];
            if (!isset($minVal[$new]) || $valNew < $minVal[$new]) {
                $minVal[$new] = $valNew;
            }
            if ($new > $currentMaxFreq) {
                $currentMaxFreq = $new;
            }
        };

        $remove = function ($pos) use (&$compNums, &$cnt, &$bucket, &$minVal, &$origVals, &$currentMaxFreq) {
            $id = $compNums[$pos];
            $old = $cnt[$id];
            $new = $old - 1;

            unset($bucket[$old][$id]);
            if (isset($minVal[$old])) {
                $val = $origVals[$id];
                if ($val == $minVal[$old]) {
                    if (!empty($bucket[$old])) {
                        $newMin = PHP_INT_MAX;
                        foreach ($bucket[$old] as $iid => $_) {
                            $v = $origVals[$iid];
                            if ($v < $newMin) $newMin = $v;
                        }
                        $minVal[$old] = $newMin;
                    } else {
                        unset($bucket[$old]);
                        unset($minVal[$old]);
                    }
                } else {
                    if (empty($bucket[$old])) {
                        unset($bucket[$old]);
                        unset($minVal[$old]);
                    }
                }
            }

            if ($new > 0) {
                $bucket[$new][$id] = true;
                $valNew = $origVals[$id];
                if (!isset($minVal[$new]) || $valNew < $minVal[$new]) {
                    $minVal[$new] = $valNew;
                }
            }

            $cnt[$id] = $new;

            while ($currentMaxFreq > 0 && !isset($bucket[$currentMaxFreq])) {
                $currentMaxFreq--;
            }
        };

        $answers = array_fill(0, count($queries), 0);
        $curL = 0;
        $curR = -1;

        foreach ($qs as $q) {
            $l = $q['l'];
            $r = $q['r'];
            $t = $q['t'];

            while ($curL > $l) { $curL--; $add($curL); }
            while ($curR < $r) { $curR++; $add($curR); }
            while ($curL < $l) { $remove($curL); $curL++; }
            while ($curR > $r) { $remove($curR); $curR--; }

            if ($currentMaxFreq >= $t && isset($minVal[$currentMaxFreq])) {
                $answers[$q['i']] = $minVal[$currentMaxFreq];
            } else {
                $answers[$q['i']] = -1;
            }
        }

        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    struct Query {
        let l: Int
        let r: Int
        let threshold: Int
        let idx: Int
    }
    
    func subarrayMajority(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        let blockSize = max(1, Int(Double(n).squareRoot()))
        var qs = [Query]()
        for (i, q) in queries.enumerated() {
            qs.append(Query(l: q[0], r: q[1], threshold: q[2], idx: i))
        }
        qs.sort { a, b in
            let blockA = a.l / blockSize
            let blockB = b.l / blockSize
            if blockA != blockB {
                return blockA < blockB
            } else {
                if blockA % 2 == 0 {
                    return a.r < b.r
                } else {
                    return a.r > b.r
                }
            }
        }
        
        var cnt = [Int: Int]()          // value -> frequency in current window
        var curL = 0
        var curR = -1
        var answer = Array(repeating: -1, count: queries.count)
        
        func add(_ x: Int) {
            cnt[x, default: 0] += 1
        }
        func remove(_ x: Int) {
            if let c = cnt[x] {
                if c == 1 {
                    cnt.removeValue(forKey: x)
                } else {
                    cnt[x] = c - 1
                }
            }
        }
        
        for q in qs {
            while curL > q.l {
                curL -= 1
                add(nums[curL])
            }
            while curR < q.r {
                curR += 1
                add(nums[curR])
            }
            while curL < q.l {
                remove(nums[curL])
                curL += 1
            }
            while curR > q.r {
                remove(nums[curR])
                curR -= 1
            }
            
            var bestVal = -1
            var bestCnt = -1
            for (val, c) in cnt where c >= q.threshold {
                if c > bestCnt || (c == bestCnt && val < bestVal) {
                    bestCnt = c
                    bestVal = val
                }
            }
            answer[q.idx] = bestVal
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.*
import kotlin.math.*

class Solution {
    private class SegmentTree(val maxFreq: Int) {
        private val size: Int
        private val tree: IntArray

        init {
            var s = 1
            while (s < maxFreq + 1) s = s shl 1
            size = s
            tree = IntArray(size * 2) { -1 }
        }

        fun update(pos: Int, present: Boolean) {
            var idx = pos + size
            tree[idx] = if (present) pos else -1
            idx = idx shr 1
            while (idx > 0) {
                tree[idx] = max(tree[idx shl 1], tree[(idx shl 1) + 1])
                idx = idx shr 1
            }
        }

        fun query(l: Int, r: Int): Int {
            var left = l + size
            var right = r + size
            var res = -1
            while (left <= right) {
                if ((left and 1) == 1) {
                    res = max(res, tree[left])
                    left++
                }
                if ((right and 1) == 0) {
                    res = max(res, tree[right])
                    right--
                }
                left = left shr 1
                right = right shr 1
            }
            return res
        }
    }

    data class Query(val l: Int, val r: Int, val t: Int, val idx: Int)

    fun subarrayMajority(nums: IntArray, queries: Array<IntArray>): IntArray {
        val n = nums.size
        // coordinate compression
        val uniqList = nums.toMutableSet().toMutableList()
        uniqList.sort()
        val valueToId = HashMap<Int, Int>(uniqList.size)
        for (i in uniqList.indices) valueToId[uniqList[i]] = i
        val comp = IntArray(n) { valueToId[nums[it]]!! }

        // prepare queries
        val qObjs = Array(queries.size) {
            Query(queries[it][0], queries[it][1], queries[it][2], it)
        }
        val blockSize = sqrt(n.toDouble()).toInt() + 1
        qObjs.sortWith { a, b ->
            val ba = a.l / blockSize
            val bb = b.l / blockSize
            if (ba != bb) ba - bb
            else {
                if ((ba and 1) == 0) a.r - b.r else b.r - a.r
            }
        }

        val maxFreq = n
        val cnt = IntArray(uniqList.size)
        val buckets = Array(maxFreq + 1) { TreeSet<Int>() }
        val seg = SegmentTree(maxFreq)

        fun add(pos: Int) {
            val id = comp[pos]
            val value = nums[pos]
            val oldCnt = cnt[id]
            if (oldCnt > 0) {
                buckets[oldCnt].remove(value)
                if (buckets[oldCnt].isEmpty()) seg.update(oldCnt, false)
            }
            val newCnt = oldCnt + 1
            cnt[id] = newCnt
            buckets[newCnt].add(value)
            if (buckets[newCnt].size == 1) seg.update(newCnt, true)
        }

        fun remove(pos: Int) {
            val id = comp[pos]
            val value = nums[pos]
            val oldCnt = cnt[id]
            buckets[oldCnt].remove(value)
            if (buckets[oldCnt].isEmpty()) seg.update(oldCnt, false)
            val newCnt = oldCnt - 1
            cnt[id] = newCnt
            if (newCnt > 0) {
                buckets[newCnt].add(value)
                if (buckets[newCnt].size == 1) seg.update(newCnt, true)
            }
        }

        fun answer(threshold: Int): Int {
            val freq = seg.query(threshold, maxFreq)
            return if (freq == -1) -1 else buckets[freq].first()
        }

        var curL = 0
        var curR = -1
        val ans = IntArray(queries.size)

        for (q in qObjs) {
            while (curL > q.l) add(--curL)
            while (curR < q.r) add(++curR)
            while (curL < q.l) remove(curL++)
            while (curR > q.r) remove(curR--)
            ans[q.idx] = answer(q.t)
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';
import 'dart:collection';

class Solution {
  List<int> subarrayMajority(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    int qLen = queries.length;
    int maxFreq = n;

    // Mo's algorithm block size
    int blockSize = sqrt(n).toInt();

    // Query structure
    class Q {
      int l, r, t, idx;
      Q(this.l, this.r, this.t, this.idx);
    }

    List<Q> qs = [];
    for (int i = 0; i < qLen; i++) {
      var arr = queries[i];
      qs.add(Q(arr[0], arr[1], arr[2], i));
    }

    qs.sort((a, b) {
      int blockA = a.l ~/ blockSize;
      int blockB = b.l ~/ blockSize;
      if (blockA != blockB) return blockA - blockB;
      return a.r - b.r;
    });

    // Frequency buckets with sorted values
    List<SplayTreeSet<int>> bucket =
        List.generate(maxFreq + 2, (_) => SplayTreeSet<int>());

    // Count of distinct numbers having exact frequency f
    List<int> freqCnt = List.filled(maxFreq + 2, 0);

    // Segment tree for max frequency with non‑empty bucket
    int size = 1;
    while (size < maxFreq + 2) size <<= 1;
    List<int> seg = List.filled(2 * size, -1);

    void segUpdate(int f, int val) {
      int pos = size + f;
      seg[pos] = val;
      for (pos >>= 1; pos > 0; pos >>= 1) {
        seg[pos] = seg[pos << 1] > seg[(pos << 1) | 1]
            ? seg[pos << 1]
            : seg[(pos << 1) | 1];
      }
    }

    int segQuery(int threshold) {
      int left = size + threshold;
      int right = size + maxFreq;
      int ans = -1;
      while (left <= right) {
        if ((left & 1) == 1) {
          if (seg[left] > ans) ans = seg[left];
          left++;
        }
        if ((right & 1) == 0) {
          if (seg[right] > ans) ans = seg[right];
          right--;
        }
        left >>= 1;
        right >>= 1;
      }
      return ans;
    }

    // Current counts of each value in the window
    Map<int, int> cnt = {};

    void add(int x) {
      int old = cnt[x] ?? 0;
      int nw = old + 1;
      cnt[x] = nw;

      if (old > 0) {
        bucket[old].remove(x);
        freqCnt[old]--;
        if (freqCnt[old] == 0) segUpdate(old, -1);
      }
      bucket[nw].add(x);
      freqCnt[nw]++;
      if (freqCnt[nw] == 1) segUpdate(nw, nw);
    }

    void remove(int x) {
      int old = cnt[x]!;
      int nw = old - 1;
      if (nw == 0) {
        cnt.remove(x);
      } else {
        cnt[x] = nw;
      }

      bucket[old].remove(x);
      freqCnt[old]--;
      if (freqCnt[old] == 0) segUpdate(old, -1);

      if (nw > 0) {
        bucket[nw].add(x);
        freqCnt[nw]++;
        if (freqCnt[nw] == 1) segUpdate(nw, nw);
      }
    }

    List<int> ans = List.filled(qLen, -1);
    int curL = 0;
    int curR = -1;

    for (var query in qs) {
      while (curR < query.r) add(nums[++curR]);
      while (curR > query.r) remove(nums[curR--]);
      while (curL < query.l) remove(nums[curL++]);
      while (curL > query.l) add(nums[--curL]);

      int f = segQuery(query.t);
      if (f != -1 && bucket[f].isNotEmpty) {
        ans[query.idx] = bucket[f].first;
      } else {
        ans[query.idx] = -1;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func subarrayMajority(nums []int, queries [][]int) []int {
	type Query struct {
		l, r   int
		thresh int
		idx    int
	}
	n := len(nums)
	// coordinate compression
	valToIdx := make(map[int]int)
	rev := []int{}
	comp := make([]int, n)
	for i, v := range nums {
		if id, ok := valToIdx[v]; ok {
			comp[i] = id
		} else {
			id := len(rev)
			valToIdx[v] = id
			rev = append(rev, v)
			comp[i] = id
		}
	}
	distinct := len(rev)

	// prepare queries with original index
	qList := make([]Query, len(queries))
	for i, q := range queries {
		qList[i] = Query{l: q[0], r: q[1], thresh: q[2], idx: i}
	}

	blockSize := int(float64(n)/float64(len(qList))*2.0) // heuristic
	if blockSize == 0 {
		blockSize = 1
	}
	sort.Slice(qList, func(i, j int) bool {
		bi := qList[i].l / blockSize
		bj := qList[j].l / blockSize
		if bi != bj {
			return bi < bj
		}
		return qList[i].r < qList[j].r
	})

	cnt := make([]int, distinct)
	bucket := make([]map[int]struct{}, n+1) // frequency -> set of value indices
	maxFreq := 0

	add := func(pos int) {
		idx := comp[pos]
		old := cnt[idx]
		newc := old + 1
		cnt[idx] = newc
		if old > 0 {
			delete(bucket[old], idx)
		}
		if bucket[newc] == nil {
			bucket[newc] = make(map[int]struct{})
		}
		bucket[newc][idx] = struct{}{}
		if newc > maxFreq {
			maxFreq = newc
		}
	}

	remove := func(pos int) {
		idx := comp[pos]
		old := cnt[idx]
		newc := old - 1
		cnt[idx] = newc
		delete(bucket[old], idx)
		if newc > 0 {
			if bucket[newc] == nil {
				bucket[newc] = make(map[int]struct{})
			}
			bucket[newc][idx] = struct{}{}
		}
		for maxFreq > 0 && (bucket[maxFreq] == nil || len(bucket[maxFreq]) == 0) {
			maxFreq--
		}
	}

	ans := make([]int, len(queries))
	curL, curR := 0, -1
	for _, q := range qList {
		for curL > q.l {
			curL--
			add(curL)
		}
		for curR < q.r {
			curR++
			add(curR)
		}
		for curL < q.l {
			remove(curL)
			curL++
		}
		for curR > q.r {
			remove(curR)
			curR--
		}

		res := -1
		for f := maxFreq; f >= q.thresh; f-- {
			if bucket[f] != nil && len(bucket[f]) > 0 {
				minVal := int(^uint(0) >> 1) // MaxInt
				for idx := range bucket[f] {
					val := rev[idx]
					if val < minVal {
						minVal = val
					}
				}
				res = minVal
				break
			}
		}
		ans[q.idx] = res
	}
	return ans
}
```

## Ruby

```ruby
require 'set'

def subarray_majority(nums, queries)
  n = nums.length
  block = Math.sqrt(n).to_i
  qinfo = queries.each_with_index.map { |(l, r, t), idx| [l, r, t, idx] }

  qinfo.sort! do |a, b|
    block_a = a[0] / block
    block_b = b[0] / block
    if block_a != block_b
      block_a <=> block_b
    else
      if block_a.even?
        a[1] <=> b[1]
      else
        b[1] <=> a[1]
      end
    end
  end

  cnt = Hash.new(0)
  bucket_sets = Array.new(n + 2) { SortedSet.new }
  present_set = SortedSet.new
  maxfreq = 0

  add = lambda do |val|
    old = cnt[val]
    newc = old + 1
    cnt[val] = newc
    if old > 0
      bucket_sets[old].delete(val)
    else
      present_set.add(val)
    end
    bucket_sets[newc].add(val)
    maxfreq = newc if newc > maxfreq
  end

  remove = lambda do |val|
    old = cnt[val]
    newc = old - 1
    cnt[val] = newc
    bucket_sets[old].delete(val)
    if newc > 0
      bucket_sets[newc].add(val)
    else
      present_set.delete(val)
    end
    while maxfreq > 0 && bucket_sets[maxfreq].empty?
      maxfreq -= 1
    end
  end

  ans = Array.new(queries.length)
  cur_l = 0
  cur_r = -1

  qinfo.each do |l, r, thr, idx|
    while cur_r < r
      cur_r += 1
      add.call(nums[cur_r])
    end
    while cur_r > r
      remove.call(nums[cur_r])
      cur_r -= 1
    end
    while cur_l < l
      remove.call(nums[cur_l])
      cur_l += 1
    end
    while cur_l > l
      cur_l -= 1
      add.call(nums[cur_l])
    end

    if maxfreq >= thr
      ans[idx] = bucket_sets[maxfreq].first
    else
      ans[idx] = -1
    end
  end

  ans
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def subarrayMajority(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    // coordinate compression
    val distinctVals = nums.distinct.sorted
    val valueToId = mutable.HashMap[Int, Int]()
    for ((v, i) <- distinctVals.zipWithIndex) valueToId(v) = i
    val m = distinctVals.length
    val origVals = distinctVals
    val a = nums.map(valueToId)

    // Mo's algorithm ordering
    val blockSize = Math.sqrt(n).toInt + 1
    case class Q(l: Int, r: Int, t: Int, idx: Int)
    val qs = queries.zipWithIndex.map { case (arr, i) => Q(arr(0), arr(1), arr(2), i) }
      .sortBy(q => (q.l / blockSize, q.r))

    // frequency structures
    val cnt = Array.fill(m)(0)

    // ordering for ids based on original value then id
    implicit val idOrdering: Ordering[Int] = new Ordering[Int] {
      def compare(a: Int, b: Int): Int = {
        val av = origVals(a)
        val bv = origVals(b)
        if (av != bv) av.compare(bv) else a.compare(b)
      }
    }

    // buckets per frequency
    val bucket = Array.ofDim[mutable.TreeSet[Int]](n + 2)
    for (i <- bucket.indices) bucket(i) = mutable.TreeSet.empty[Int]

    // segment tree to find max non‑empty frequency
    var sz = 1
    while (sz < n + 2) sz <<= 1
    val seg = Array.fill(2 * sz)(-1)
    val freqNonEmpty = Array.fill(n + 2)(false)

    def setFreq(f: Int, present: Boolean): Unit = {
      var i = f + sz
      seg(i) = if (present) f else -1
      i >>= 1
      while (i > 0) {
        val left = seg(i << 1)
        val right = seg((i << 1) | 1)
        seg(i) = if (left > right) left else right
        i >>= 1
      }
    }

    def queryFreq(l: Int, r: Int): Int = {
      var res = -1
      var left = l + sz
      var right = r + sz
      while (left <= right) {
        if ((left & 1) == 1) {
          val v = seg(left)
          if (v > res) res = v
          left += 1
        }
        if ((right & 1) == 0) {
          val v = seg(right)
          if (v > res) res = v
          right -= 1
        }
        left >>= 1
        right >>= 1
      }
      res
    }

    def addPos(pos: Int): Unit = {
      val id = a(pos)
      var c = cnt(id)
      if (c > 0) {
        bucket(c).remove(id)
        if (bucket(c).isEmpty && freqNonEmpty(c)) {
          freqNonEmpty(c) = false
          setFreq(c, false)
        }
      }
      c += 1
      cnt(id) = c
      if (!freqNonEmpty(c)) {
        freqNonEmpty(c) = true
        setFreq(c, true)
      }
      bucket(c).add(id)
    }

    def removePos(pos: Int): Unit = {
      val id = a(pos)
      var c = cnt(id)
      bucket(c).remove(id)
      if (bucket(c).isEmpty && freqNonEmpty(c)) {
        freqNonEmpty(c) = false
        setFreq(c, false)
      }
      c -= 1
      cnt(id) = c
      if (c > 0) {
        if (!freqNonEmpty(c)) {
          freqNonEmpty(c) = true
          setFreq(c, true)
        }
        bucket(c).add(id)
      }
    }

    def answer(threshold: Int): Int = {
      val f = queryFreq(threshold, n)
      if (f == -1) -1 else origVals(bucket(f).head)
    }

    val ans = Array.fill(queries.length)(-1)
    var curL = 0
    var curR = -1

    for (q <- qs) {
      while (curL > q.l) { curL -= 1; addPos(curL) }
      while (curR < q.r) { curR += 1; addPos(curR) }
      while (curL < q.l) { removePos(curL); curL += 1 }
      while (curR > q.r) { removePos(curR); curR -= 1 }

      ans(q.idx) = answer(q.t)
    }

    ans
  }
}
```

## Rust

```rust
use std::collections::{HashMap, BTreeSet};

struct SegTree {
    n: usize,
    data: Vec<i32>,
}
impl SegTree {
    fn new(size: usize) -> Self {
        let mut n = 1usize;
        while n < size { n <<= 1; }
        SegTree { n, data: vec![-1; 2 * n] }
    }
    fn update(&mut self, pos: usize, val: i32) {
        let mut idx = pos + self.n;
        self.data[idx] = val;
        idx >>= 1;
        while idx > 0 {
            self.data[idx] = std::cmp::max(self.data[2 * idx], self.data[2 * idx + 1]);
            idx >>= 1;
        }
    }
    fn query(&self, l: usize, r: usize) -> i32 { // inclusive
        if l > r { return -1; }
        let mut res = -1;
        let mut left = l + self.n;
        let mut right = r + self.n;
        while left <= right {
            if (left & 1) == 1 {
                res = std::cmp::max(res, self.data[left]);
                left += 1;
            }
            if (right & 1) == 0 {
                res = std::cmp::max(res, self.data[right]);
                if right == 0 { break; }
                right -= 1;
            }
            left >>= 1;
            right = (right >> 1);
        }
        res
    }
}

#[derive(Clone)]
struct Query {
    l: usize,
    r: usize,
    t: usize,
    idx: usize,
}
impl Solution {
    pub fn subarray_majority(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let q = queries.len();
        let block = (n as f64).sqrt() as usize + 1;
        let mut qs: Vec<Query> = queries.into_iter().enumerate().map(|(i, v)| {
            Query { l: v[0] as usize, r: v[1] as usize, t: v[2] as usize, idx: i }
        }).collect();
        qs.sort_by(|a, b| {
            let ba = a.l / block;
            let bb = b.l / block;
            if ba != bb { return ba.cmp(&bb); }
            if ba % 2 == 0 { a.r.cmp(&b.r) } else { b.r.cmp(&a.r) }
        });

        // data structures
        let mut cnt: HashMap<i32, usize> = HashMap::new();
        let mut bucket: Vec<BTreeSet<i32>> = vec![BTreeSet::new(); n + 2];
        let mut present: Vec<bool> = vec![false; n + 2];
        let mut seg = SegTree::new(n + 2);

        let mut add = |pos: usize,
                       cnt: &mut HashMap<i32, usize>,
                       bucket: &mut Vec<BTreeSet<i32>>,
                       present: &mut Vec<bool>,
                       seg: &mut SegTree| {
            let x = nums[pos];
            let c = *cnt.get(&x).unwrap_or(&0);
            if c > 0 {
                bucket[c].remove(&x);
                if bucket[c].is_empty() && present[c] {
                    present[c] = false;
                    seg.update(c, -1);
                }
            }
            let nc = c + 1;
            cnt.insert(x, nc);
            bucket[nc].insert(x);
            if !present[nc] {
                present[nc] = true;
                seg.update(nc, nc as i32);
            }
        };

        let mut remove = |pos: usize,
                          cnt: &mut HashMap<i32, usize>,
                          bucket: &mut Vec<BTreeSet<i32>>,
                          present: &mut Vec<bool>,
                          seg: &mut SegTree| {
            let x = nums[pos];
            let c = *cnt.get(&x).unwrap(); // must exist
            bucket[c].remove(&x);
            if bucket[c].is_empty() && present[c] {
                present[c] = false;
                seg.update(c, -1);
            }
            let nc = c - 1;
            if nc == 0 {
                cnt.remove(&x);
            } else {
                cnt.insert(x, nc);
                bucket[nc].insert(x);
                if !present[nc] {
                    present[nc] = true;
                    seg.update(nc, nc as i32);
                }
            }
        };

        let mut cur_l: isize = 0;
        let mut cur_r: isize = -1;
        let mut ans: Vec<i32> = vec![-1; q];

        for query in qs {
            let l = query.l as isize;
            let r = query.r as isize;

            while cur_l > l {
                cur_l -= 1;
                add(cur_l as usize, &mut cnt, &mut bucket, &mut present, &mut seg);
            }
            while cur_r < r {
                cur_r += 1;
                add(cur_r as usize, &mut cnt, &mut bucket, &mut present, &mut seg);
            }
            while cur_l < l {
                remove(cur_l as usize, &mut cnt, &mut bucket, &mut present, &mut seg);
                cur_l += 1;
            }
            while cur_r > r {
                remove(cur_r as usize, &mut cnt, &mut bucket, &mut present, &mut seg);
                cur_r -= 1;
            }

            let max_f = seg.query(query.t, n);
            if max_f == -1 {
                ans[query.idx] = -1;
            } else {
                let f = max_f as usize;
                // smallest value in bucket[f]
                if let Some(&val) = bucket[f].iter().next() {
                    ans[query.idx] = val;
                } else {
                    ans[query.idx] = -1; // should not happen
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
#lang racket

(struct query (l r t idx) #:transparent)

(define (subarray-majority nums queries)
  (let* ((n (length nums))
         (B (max 1 (exact-floor (sqrt n))))
         (nums-v (list->vector nums))

         ;; convert queries to structs with original index
         (qlist
          (let loop ((i 0) (qs queries) (acc '()))
            (if (null? qs)
                (reverse acc)
                (let* ((q (car qs))
                       (l (list-ref q 0))
                       (r (list-ref q 1))
                       (t (list-ref q 2)))
                  (loop (+ i 1) (cdr qs)
                        (cons (query l r t i) acc))))))

         ;; comparator for Mo's ordering
         (query-less?
          (lambda (a b)
            (let ((block-a (quotient (query-l a) B))
                  (block-b (quotient (query-l b) B)))
              (cond [(< block-a block-b) #t]
                    [(> block-a block-b) #f]
                    [else (< (query-r a) (query-r b))]))))

         (sorted-queries (sort qlist query-less?))

         ;; frequency structures
         (cnt (make-hash))
         (buckets (make-vector (+ n 1) #f))
         (_ (for ([i (in-range (add1 n))])
              (vector-set! buckets i (make-hash))))
         (maxFreq 0)

         ;; add element at position pos
         (add-pos
          (lambda (pos)
            (let* ((val (vector-ref nums-v pos))
                   (old (hash-ref cnt val 0))
                   (new (+ old 1)))
              (hash-set! cnt val new)
              (when (> old 0)
                (hash-remove! (vector-ref buckets old) val))
              (hash-set! (vector-ref buckets new) val #t)
              (when (> new maxFreq) (set! maxFreq new)))))

         ;; remove element at position pos
         (remove-pos
          (lambda (pos)
            (let* ((val (vector-ref nums-v pos))
                   (old (hash-ref cnt val))
                   (new (- old 1)))
              (if (= new 0)
                  (hash-remove! cnt val)
                  (hash-set! cnt val new))
              (hash-remove! (vector-ref buckets old) val)
              (when (> new 0)
                (hash-set! (vector-ref buckets new) val #t))
              (when (and (= old maxFreq)
                         (= (hash-count (vector-ref buckets maxFreq)) 0))
                (let loop ()
                  (set! maxFreq (- maxFreq 1))
                  (when (and (> maxFreq 0)
                             (= (hash-count (vector-ref buckets maxFreq)) 0))
                    (loop)))))))

         ;; answers vector
         (answers (make-vector (length queries) -1)))

    ;; process queries with Mo's algorithm
    (let ((L 0) (R -1))
      (for ([q sorted-queries])
        (define l (query-l q))
        (define r (query-r q))
        (define t (query-t q))

        (do () ((>= L l))
          (remove-pos L)
          (set! L (+ L 1)))
        (do () ((<= L l))
          (set! L (- L 1))
          (add-pos L))

        (do () ((>= R r))
          (remove-pos R)
          (set! R (- R 1)))
        (do () ((<= R r))
          (set! R (+ R 1))
          (add-pos R))

        (if (>= maxFreq t)
            (let* ((ht (vector-ref buckets maxFreq))
                   (min-val
                    (for/fold ([m most-positive-fixnum])
                              ([k (in-hash-keys ht)])
                      (if (< k m) k m))))
              (vector-set! answers (query-idx q) min-val))
            (vector-set! answers (query-idx q) -1))))

    (vector->list answers)))
```

## Erlang

```erlang
-module(solution).
-export([subarray_majority/2]).

-spec subarray_majority(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
subarray_majority(Nums, Queries) ->
    N = length(Nums),
    B = trunc(math:sqrt(N)) + 1,
    NumT = list_to_tuple(Nums),

    Indexed = lists:map(
        fun({Q, Idx}) ->
            [L,R,T] = Q,
            Block = L div B,
            {Block, R, Idx, L, T}
        end,
        lists:zip(Queries, lists:seq(0, length(Queries) - 1))
    ),

    Sorted = lists:sort(
        fun(A, B_) ->
            case element(1, A) =:= element(1, B_) of
                true -> element(2, A) < element(2, B_);
                false -> element(1, A) < element(1, B_)
            end
        end,
        Indexed
    ),

    AnswersKV = process_queries(Sorted, NumT, 0, -1, #{}, []),
    SortedAns = lists:keysort(1, AnswersKV),
    [Ans || {_Idx, Ans} <- SortedAns].

process_queries([], _NumT, _L, _R, _CntMap, Acc) ->
    Acc;
process_queries([Q|Rest], NumT, L, R, CntMap, Acc) ->
    {_, _, Idx, QL, QT} = Q,
    {NewL, NewR, NewCnt} = adjust_window(L, R, QL, Q.R, NumT, CntMap),
    Answer = find_answer(NewCnt, QT),
    process_queries(Rest, NumT, NewL, NewR, NewCnt, [{Idx, Answer}|Acc]).

adjust_window(L, R, LTarget, RTarget, NumT, Cnt) when L > LTarget ->
    NewL = L - 1,
    Val = element(NumT, NewL + 1),
    NewCnt = maps:update_with(Val, fun(C) -> C + 1 end, 1, Cnt),
    adjust_window(NewL, R, LTarget, RTarget, NumT, NewCnt);
adjust_window(L, R, LTarget, RTarget, NumT, Cnt) when R < RTarget ->
    NewR = R + 1,
    Val = element(NumT, NewR + 1),
    NewCnt = maps:update_with(Val, fun(C) -> C + 1 end, 1, Cnt),
    adjust_window(L, NewR, LTarget, RTarget, NumT, NewCnt);
adjust_window(L, R, LTarget, RTarget, NumT, Cnt) when L < LTarget ->
    Val = element(NumT, L + 1),
    NewCnt = case maps:get(Val, Cnt) of
                 1 -> maps:remove(Val, Cnt);
                 C -> maps:put(Val, C - 1, Cnt)
             end,
    NewL = L + 1,
    adjust_window(NewL, R, LTarget, RTarget, NumT, NewCnt);
adjust_window(L, R, LTarget, RTarget, NumT, Cnt) when R > RTarget ->
    Val = element(NumT, R + 1),
    NewCnt = case maps:get(Val, Cnt) of
                 1 -> maps:remove(Val, Cnt);
                 C -> maps:put(Val, C - 1, Cnt)
             end,
    NewR = R - 1,
    adjust_window(L, NewR, LTarget, RTarget, NumT, NewCnt);
adjust_window(L, R, _LTarget, _RTarget, _NumT, Cnt) ->
    {L, R, Cnt}.

find_answer(CntMap, Threshold) ->
    {BestFreq, BestVal} = maps:fold(
        fun(Val, C, {BF, BV}) ->
            if
                C >= Threshold,
                (C > BF orelse (C == BF andalso Val < BV)) ->
                    {C, Val};
                true ->
                    {BF, BV}
            end
        end,
        {0, 0},
        CntMap
    ),
    case BestFreq of
        0 -> -1;
        _ -> BestVal
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec subarray_majority(nums :: [integer], queries :: [[integer]]) :: [integer]
  def subarray_majority(nums, queries) do
    n = length(nums)
    block = trunc(:math.sqrt(n)) + 1

    nums_tuple = List.to_tuple(nums)

    indexed_queries =
      Enum.with_index(queries)
      |> Enum.map(fn {q, idx} ->
        %{l: Enum.at(q, 0), r: Enum.at(q, 1), t: Enum.at(q, 2), idx: idx}
      end)

    sorted_queries =
      Enum.sort_by(indexed_queries, fn q -> {div(q.l, block), q.r} end)

    # initial state
    init_state = %{
      l: 0,
      r: -1,
      cnt: %{},
      bucket: %{},
      max_freq: 0,
      answers: %{}
    }

    final_state =
      Enum.reduce(sorted_queries, init_state, fn q, state ->
        {state, _} = move_right(state, q.r, nums_tuple)
        {state, _} = move_left(state, q.l, nums_tuple)

        ans = query_answer(state.bucket, state.max_freq, q.t)
        %{state | answers: Map.put(state.answers, q.idx, ans)}
      end)

    # collect answers in original order
    0..(length(queries) - 1)
    |> Enum.map(fn i -> Map.fetch!(final_state.answers, i) end)
  end

  defp move_right(state, target_r, nums_tuple) do
    if state.r < target_r do
      new_r = state.r + 1
      val = :erlang.element(new_r + 1, nums_tuple)
      {new_state, _} = add(val, %{state | r: new_r}, nums_tuple)
      move_right(new_state, target_r, nums_tuple)
    else
      {state, nil}
    end
  end

  defp move_left(state, target_l, nums_tuple) do
    if state.l > target_l do
      new_l = state.l - 1
      val = :erlang.element(new_l + 1, nums_tuple)
      {new_state, _} = add(val, %{state | l: new_l}, nums_tuple)
      move_left(new_state, target_l, nums_tuple)
    else
      if state.l < target_l do
        # need to remove current left element and increment l
        val = :erlang.element(state.l + 1, nums_tuple)
        {new_state, _} = remove(val, %{state | l: state.l + 1}, nums_tuple)
        move_left(new_state, target_l, nums_tuple)
      else
        {state, nil}
      end
    end
  end

  defp add(x, state, _nums) do
    old_cnt = Map.get(state.cnt, x, 0)
    new_cnt = old_cnt + 1

    cnt = Map.put(state.cnt, x, new_cnt)

    bucket =
      if old_cnt > 0 do
        set_old = Map.get(state.bucket, old_cnt)
        set_old = MapSet.delete(set_old, x)

        if MapSet.size(set_old) == 0 do
          Map.delete(state.bucket, old_cnt)
        else
          Map.put(state.bucket, old_cnt, set_old)
        end
      else
        state.bucket
      end

    set_new = Map.get(bucket, new_cnt, MapSet.new())
    set_new = MapSet.put(set_new, x)
    bucket = Map.put(bucket, new_cnt, set_new)

    max_freq = if new_cnt > state.max_freq, do: new_cnt, else: state.max_freq

    {%{state | cnt: cnt, bucket: bucket, max_freq: max_freq}, nil}
  end

  defp remove(x, state, _nums) do
    old_cnt = Map.fetch!(state.cnt, x)
    new_cnt = old_cnt - 1

    # remove from old bucket
    set_old = Map.get(state.bucket, old_cnt)
    set_old = MapSet.delete(set_old, x)

    bucket =
      if MapSet.size(set_old) == 0 do
        Map.delete(state.bucket, old_cnt)
      else
        Map.put(state.bucket, old_cnt, set_old)
      end

    cnt =
      if new_cnt == 0 do
        Map.delete(state.cnt, x)
      else
        Map.put(state.cnt, x, new_cnt)
      end

    bucket =
      if new_cnt > 0 do
        set_new = Map.get(bucket, new_cnt, MapSet.new())
        set_new = MapSet.put(set_new, x)
        Map.put(bucket, new_cnt, set_new)
      else
        bucket
      end

    max_freq =
      cond do
        state.max_freq == old_cnt and not Map.has_key?(bucket, old_cnt) ->
          dec_max(state.max_freq - 1, bucket)

        true ->
          state.max_freq
      end

    {%{state | cnt: cnt, bucket: bucket, max_freq: max_freq}, nil}
  end

  defp dec_max(0, _bucket), do: 0

  defp dec_max(mf, bucket) do
    if Map.has_key?(bucket, mf) do
      mf
    else
      dec_max(mf - 1, bucket)
    end
  end

  defp query_answer(bucket, max_freq, threshold) do
    if max_freq < threshold do
      -1
    else
      find_freq(bucket, max_freq, threshold)
    end
  end

  defp find_freq(_bucket, freq, _threshold) when freq < 0, do: -1

  defp find_freq(bucket, freq, threshold) do
    if freq < threshold do
      -1
    else
      case Map.get(bucket, freq) do
        nil -> find_freq(bucket, freq - 1, threshold)
        set ->
          Enum.min(set)
      end
    end
  end
end
```

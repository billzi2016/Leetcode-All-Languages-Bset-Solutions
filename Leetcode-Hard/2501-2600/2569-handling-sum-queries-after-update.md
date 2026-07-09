# 2569. Handling Sum Queries After Update

## Cpp

```cpp
class Solution {
public:
    struct Node {
        long long cntOnes = 0;   // number of ones in nums1
        long long sumAll = 0;    // total sum of nums2 in this segment
        long long sumOnes = 0;   // sum of nums2 where corresponding nums1 is 1
        bool flip = false;       // lazy flip flag for nums1 bits
        long long addOnes = 0;   // lazy addition to positions where nums1 == 1
    };
    
    vector<Node> seg;
    vector<int> len;
    
    void build(int idx, int l, int r, const vector<int>& nums1, const vector<long long>& nums2) {
        len[idx] = r - l + 1;
        if (l == r) {
            seg[idx].cntOnes = nums1[l];
            seg[idx].sumAll = nums2[l];
            seg[idx].sumOnes = nums1[l] ? nums2[l] : 0;
            return;
        }
        int mid = (l + r) >> 1;
        build(idx<<1, l, mid, nums1, nums2);
        build(idx<<1|1, mid+1, r, nums1, nums2);
        pull(idx);
    }
    
    void applyFlip(int idx) {
        seg[idx].cntOnes = len[idx] - seg[idx].cntOnes;
        long long zeroSum = seg[idx].sumAll - seg[idx].sumOnes;
        seg[idx].sumOnes = zeroSum;
        seg[idx].flip ^= 1;
    }
    
    void applyAddOnes(int idx, long long val) {
        if (seg[idx].cntOnes == 0) {
            // nothing to add now, but keep lazy for children
            seg[idx].addOnes += val;
            return;
        }
        seg[idx].sumAll += val * seg[idx].cntOnes;
        seg[idx].sumOnes += val * seg[idx].cntOnes;
        seg[idx].addOnes += val;
    }
    
    void push(int idx) {
        if (seg[idx].flip) {
            applyFlip(idx<<1);
            applyFlip(idx<<1|1);
            seg[idx].flip = false;
        }
        if (seg[idx].addOnes != 0) {
            applyAddOnes(idx<<1, seg[idx].addOnes);
            applyAddOnes(idx<<1|1, seg[idx].addOnes);
            seg[idx].addOnes = 0;
        }
    }
    
    void pull(int idx) {
        seg[idx].cntOnes = seg[idx<<1].cntOnes + seg[idx<<1|1].cntOnes;
        seg[idx].sumAll = seg[idx<<1].sumAll + seg[idx<<1|1].sumAll;
        seg[idx].sumOnes = seg[idx<<1].sumOnes + seg[idx<<1|1].sumOnes;
    }
    
    void rangeFlip(int idx, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            applyFlip(idx);
            return;
        }
        push(idx);
        int mid = (l + r) >> 1;
        if (ql <= mid) rangeFlip(idx<<1, l, mid, ql, qr);
        if (qr > mid)  rangeFlip(idx<<1|1, mid+1, r, ql, qr);
        pull(idx);
    }
    
    vector<long long> handleQuery(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        int n = nums1.size();
        seg.assign(4*n + 5, Node());
        len.assign(4*n + 5, 0);
        vector<long long> nums2ll(nums2.begin(), nums2.end());
        build(1, 0, n-1, nums1, nums2ll);
        vector<long long> ans;
        for (auto &q : queries) {
            int type = q[0];
            if (type == 1) { // flip range
                int l = q[1], r = q[2];
                rangeFlip(1, 0, n-1, l, r);
            } else if (type == 2) { // add p to all positions where nums1[i]==1
                long long p = q[1];
                applyAddOnes(1, p); // whole array
            } else if (type == 3) { // total sum of nums2
                ans.push_back(seg[1].sumAll);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long[] handleQuery(int[] nums1, int[] nums2, int[][] queries) {
        int n = nums1.length;
        SegmentTree st = new SegmentTree(nums1, nums2);
        java.util.List<Long> resList = new java.util.ArrayList<>();
        for (int[] q : queries) {
            int type = q[0];
            if (type == 1) {                     // set range to 1 in nums1
                int l = q[1], r = q[2];
                st.setOnes(l, r);
            } else if (type == 2) {              // add p * nums1[i] to nums2[i] for all i
                long p = q[1];
                st.addRange(0, n - 1, p);
            } else {                             // type 3: sum query on nums2
                int l = q[1], r = q[2];
                resList.add(st.query(l, r));
            }
        }
        long[] ans = new long[resList.size()];
        for (int i = 0; i < ans.length; i++) ans[i] = resList.get(i);
        return ans;
    }

    private static class SegmentTree {
        int n;
        int[] cnt;          // number of ones in nums1 within segment
        long[] sum;         // sum of nums2 within segment
        long[] lazyAdd;     // pending addition value p for type‑2 updates
        boolean[] lazySet;  // pending set‑to‑one flag

        SegmentTree(int[] a1, int[] a2) {
            n = a1.length;
            cnt = new int[4 * n];
            sum = new long[4 * n];
            lazyAdd = new long[4 * n];
            lazySet = new boolean[4 * n];
            build(1, 0, n - 1, a1, a2);
        }

        private void build(int node, int l, int r, int[] a1, int[] a2) {
            if (l == r) {
                cnt[node] = a1[l];
                sum[node] = a2[l];
                return;
            }
            int mid = (l + r) >>> 1;
            build(node << 1, l, mid, a1, a2);
            build(node << 1 | 1, mid + 1, r, a1, a2);
            pull(node);
        }

        private void pull(int node) {
            cnt[node] = cnt[node << 1] + cnt[node << 1 | 1];
            sum[node] = sum[node << 1] + sum[node << 1 | 1];
        }

        private void applySet(int node, int l, int r) {
            cnt[node] = r - l + 1;
            lazySet[node] = true;
        }

        private void push(int node, int l, int r) {
            if (l == r) return;
            int mid = (l + r) >>> 1;
            int left = node << 1, right = node << 1 | 1;

            if (lazySet[node]) {
                applySet(left, l, mid);
                applySet(right, mid + 1, r);
                lazySet[node] = false;
            }
            if (lazyAdd[node] != 0) {
                long v = lazyAdd[node];
                sum[left] += v * cnt[left];
                lazyAdd[left] += v;
                sum[right] += v * cnt[right];
                lazyAdd[right] += v;
                lazyAdd[node] = 0;
            }
        }

        // public wrappers
        void setOnes(int L, int R) { setOnes(1, 0, n - 1, L, R); }
        void addRange(int L, int R, long p) { addRange(1, 0, n - 1, L, R, p); }
        long query(int L, int R) { return query(1, 0, n - 1, L, R); }

        // internal recursive methods
        private void setOnes(int node, int l, int r, int L, int R) {
            if (R < l || r < L) return;
            if (L <= l && r <= R) {
                applySet(node, l, r);
                return;
            }
            push(node, l, r);
            int mid = (l + r) >>> 1;
            setOnes(node << 1, l, mid, L, R);
            setOnes(node << 1 | 1, mid + 1, r, L, R);
            pull(node);
        }

        private void addRange(int node, int l, int r, int L, int R, long p) {
            if (R < l || r < L) return;
            if (L <= l && r <= R) {
                sum[node] += p * cnt[node];
                lazyAdd[node] += p;
                return;
            }
            push(node, l, r);
            int mid = (l + r) >>> 1;
            addRange(node << 1, l, mid, L, R, p);
            addRange(node << 1 | 1, mid + 1, r, L, R, p);
            pull(node);
        }

        private long query(int node, int l, int r, int L, int R) {
            if (R < l || r < L) return 0;
            if (L <= l && r <= R) return sum[node];
            push(node, l, r);
            int mid = (l + r) >>> 1;
            return query(node << 1, l, mid, L, R) +
                   query(node << 1 | 1, mid + 1, r, L, R);
        }
    }
}
```

## Python

```python
class Solution(object):
    def handleQuery(self, nums1, nums2, queries):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(1 << 25)

        n = len(nums1)
        size = 4 * n
        tree = [0] * size          # count of ones in the segment
        lazy = [0] * size          # pending flip flag (0 or 1)

        def build(node, l, r):
            if l == r:
                tree[node] = nums1[l]
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def apply_flip(node, l, r):
            tree[node] = (r - l + 1) - tree[node]
            lazy[node] ^= 1

        def push(node, l, r):
            if lazy[node]:
                mid = (l + r) // 2
                apply_flip(node * 2, l, mid)
                apply_flip(node * 2 + 1, mid + 1, r)
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply_flip(node, l, r)
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        build(1, 0, n - 1)

        total_sum2 = sum(nums2)
        ans = []

        for typ, a, b in queries:
            if typ == 1:          # flip nums1[l..r]
                l, r = a, b
                update(1, 0, n - 1, l, r)
            elif typ == 2:        # add p to nums2[i] where nums1[i]==1
                p = a
                cnt_one = tree[1]   # total number of ones in nums1
                total_sum2 += p * cnt_one
            else:                 # typ == 3, query sum of nums2
                ans.append(total_sum2)

        return ans
```

## Python3

```python
class Solution:
    def handleQuery(self, nums1, nums2, queries):
        n = len(nums1)
        size = 4 * n
        seg = [0] * size          # count of ones
        lazy = [0] * size         # pending flip flag (0/1)

        def build(idx, l, r):
            if l == r:
                seg[idx] = nums1[l]
                return
            mid = (l + r) // 2
            build(idx*2, l, mid)
            build(idx*2+1, mid+1, r)
            seg[idx] = seg[idx*2] + seg[idx*2+1]

        def apply_flip(idx, l, r):
            seg[idx] = (r - l + 1) - seg[idx]
            lazy[idx] ^= 1

        def push(idx, l, r):
            if lazy[idx]:
                mid = (l + r) // 2
                apply_flip(idx*2, l, mid)
                apply_flip(idx*2+1, mid+1, r)
                lazy[idx] = 0

        def update(idx, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply_flip(idx, l, r)
                return
            push(idx, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(idx*2, l, mid, ql, qr)
            if qr > mid:
                update(idx*2+1, mid+1, r, ql, qr)
            seg[idx] = seg[idx*2] + seg[idx*2+1]

        build(1, 0, n-1)

        total_sum = sum(nums2)
        ans = []

        for typ, a, b in queries:
            if typ == 1:
                l, r = a, b
                update(1, 0, n-1, l, r)
            elif typ == 2:
                p = a
                ones = seg[1]          # total number of 1s in nums1
                total_sum += p * ones
            else:   # typ == 3
                ans.append(total_sum)

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int cnt;   // number of ones in the segment
    char lazy; // 1 if this segment is fully set to 1
} Node;

static Node *seg;
static int N;

static void build(int idx, int l, int r, const int *arr) {
    seg[idx].lazy = 0;
    if (l == r) {
        seg[idx].cnt = arr[l];
        return;
    }
    int mid = (l + r) >> 1;
    build(idx << 1, l, mid, arr);
    build(idx << 1 | 1, mid + 1, r, arr);
    seg[idx].cnt = seg[idx << 1].cnt + seg[idx << 1 | 1].cnt;
}

static void pushDown(int idx, int l, int r) {
    if (!seg[idx].lazy) return;
    int mid = (l + r) >> 1;
    int left = idx << 1, right = idx << 1 | 1;

    seg[left].cnt = mid - l + 1;
    seg[left].lazy = 1;

    seg[right].cnt = r - mid;
    seg[right].lazy = 1;

    seg[idx].lazy = 0;
}

static int queryOnes(int idx, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) return seg[idx].cnt;
    pushDown(idx, l, r);
    int mid = (l + r) >> 1;
    int res = 0;
    if (ql <= mid) res += queryOnes(idx << 1, l, mid, ql, qr);
    if (qr > mid)  res += queryOnes(idx << 1 | 1, mid + 1, r, ql, qr);
    return res;
}

static void updateSetOne(int idx, int l, int r, int ul, int ur) {
    if (ul <= l && r <= ur) {
        seg[idx].cnt = r - l + 1;
        seg[idx].lazy = 1;
        return;
    }
    pushDown(idx, l, r);
    int mid = (l + r) >> 1;
    if (ul <= mid) updateSetOne(idx << 1, l, mid, ul, ur);
    if (ur > mid)  updateSetOne(idx << 1 | 1, mid + 1, r, ul, ur);
    seg[idx].cnt = seg[idx << 1].cnt + seg[idx << 1 | 1].cnt;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* handleQuery(int* nums1, int nums1Size, int* nums2, int nums2Size,
                       int** queries, int queriesSize, int* queriesColSize,
                       int* returnSize) {
    N = nums1Size;
    seg = (Node *)malloc(sizeof(Node) * 4 * N);
    build(1, 0, N - 1, nums1);

    long long totalSum = 0;
    for (int i = 0; i < nums2Size; ++i) totalSum += (long long)nums2[i];

    long long *ans = (long long *)malloc(sizeof(long long) * queriesSize);
    int ansCnt = 0;

    for (int i = 0; i < queriesSize; ++i) {
        int type = queries[i][0];
        if (type == 1) { // set range to 1
            int l = queries[i][1];
            int r = queries[i][2];
            int ones = queryOnes(1, 0, N - 1, l, r);
            int len = r - l + 1;
            if (ones < len) {
                updateSetOne(1, 0, N - 1, l, r);
            }
        } else if (type == 2) { // add p to nums2 where nums1[i]==1
            int p = queries[i][1];
            long long onesTotal = seg[1].cnt;
            totalSum += onesTotal * (long long)p;
        } else if (type == 3) { // query sum of nums2
            ans[ansCnt++] = totalSum;
        }
    }

    free(seg);
    *returnSize = ansCnt;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private class SegmentTree
    {
        private readonly int n;
        private readonly int[] cnt;
        private readonly bool[] lazy;

        public SegmentTree(int[] arr)
        {
            n = arr.Length;
            cnt = new int[4 * n];
            lazy = new bool[4 * n];
            Build(1, 0, n - 1, arr);
        }

        private void Build(int node, int l, int r, int[] arr)
        {
            if (l == r)
            {
                cnt[node] = arr[l];
                return;
            }
            int mid = (l + r) >> 1;
            Build(node << 1, l, mid, arr);
            Build(node << 1 | 1, mid + 1, r, arr);
            cnt[node] = cnt[node << 1] + cnt[node << 1 | 1];
        }

        private void ApplyFlip(int node, int l, int r)
        {
            cnt[node] = (r - l + 1) - cnt[node];
            lazy[node] ^= true;
        }

        private void Push(int node, int l, int r)
        {
            if (!lazy[node]) return;
            int mid = (l + r) >> 1;
            ApplyFlip(node << 1, l, mid);
            ApplyFlip(node << 1 | 1, mid + 1, r);
            lazy[node] = false;
        }

        public void Update(int L, int R)
        {
            Update(1, 0, n - 1, L, R);
        }

        private void Update(int node, int l, int r, int L, int R)
        {
            if (L > r || R < l) return;
            if (L <= l && r <= R)
            {
                ApplyFlip(node, l, r);
                return;
            }
            Push(node, l, r);
            int mid = (l + r) >> 1;
            Update(node << 1, l, mid, L, R);
            Update(node << 1 | 1, mid + 1, r, L, R);
            cnt[node] = cnt[node << 1] + cnt[node << 1 | 1];
        }

        public int QueryAll()
        {
            return cnt[1];
        }
    }

    public long[] HandleQuery(int[] nums1, int[] nums2, int[][] queries)
    {
        var seg = new SegmentTree(nums1);
        long sum = 0;
        foreach (var v in nums2) sum += v;

        var result = new List<long>();

        foreach (var q in queries)
        {
            int type = q[0];
            if (type == 1)
            {
                int l = q[1], r = q[2];
                seg.Update(l, r);
            }
            else if (type == 2)
            {
                int p = q[1];
                long ones = seg.QueryAll();
                sum += (long)p * ones;
            }
            else // type == 3
            {
                result.Add(sum);
            }
        }

        return result.ToArray();
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
var handleQuery = function(nums1, nums2, queries) {
    const n = nums1.length;
    const size = 4 * n;
    const cnt = new Array(size).fill(0);          // number of ones in segment (from nums1)
    const sum = new Array(size).fill(0);          // sum of nums2 values in segment
    const lazyFlip = new Uint8Array(size);        // pending flip flag
    const lazyAdd = new Array(size).fill(0);      // pending addition to nums2 where nums1==1

    function build(idx, l, r) {
        if (l === r) {
            cnt[idx] = nums1[l];
            sum[idx] = nums2[l];
            return;
        }
        const mid = (l + r) >> 1;
        build(idx << 1, l, mid);
        build(idx << 1 | 1, mid + 1, r);
        cnt[idx] = cnt[idx << 1] + cnt[idx << 1 | 1];
        sum[idx] = sum[idx << 1] + sum[idx << 1 | 1];
    }

    function applyAdd(idx, val) {
        if (val === 0) return;
        sum[idx] += val * cnt[idx];
        lazyAdd[idx] += val;
    }

    function applyFlip(idx, len) {
        cnt[idx] = len - cnt[idx];
        lazyFlip[idx] ^= 1;
    }

    function push(idx, l, r) {
        const mid = (l + r) >> 1;
        const left = idx << 1, right = idx << 1 | 1;

        if (lazyFlip[idx]) {
            applyFlip(left, mid - l + 1);
            applyFlip(right, r - mid);
            lazyFlip[idx] = 0;
        }
        if (lazyAdd[idx] !== 0) {
            const val = lazyAdd[idx];
            applyAdd(left, val);
            applyAdd(right, val);
            lazyAdd[idx] = 0;
        }
    }

    function rangeFlip(idx, l, r, ql, qr) {
        if (ql <= l && r <= qr) {
            applyFlip(idx, r - l + 1);
            return;
        }
        push(idx, l, r);
        const mid = (l + r) >> 1;
        if (ql <= mid) rangeFlip(idx << 1, l, mid, ql, qr);
        if (qr > mid) rangeFlip(idx << 1 | 1, mid + 1, r, ql, qr);
        cnt[idx] = cnt[idx << 1] + cnt[idx << 1 | 1];
        sum[idx] = sum[idx << 1] + sum[idx << 1 | 1];
    }

    function rangeAdd(idx, l, r, ql, qr, val) {
        if (ql <= l && r <= qr) {
            applyAdd(idx, val);
            return;
        }
        push(idx, l, r);
        const mid = (l + r) >> 1;
        if (ql <= mid) rangeAdd(idx << 1, l, mid, ql, qr, val);
        if (qr > mid) rangeAdd(idx << 1 | 1, mid + 1, r, ql, qr, val);
        sum[idx] = sum[idx << 1] + sum[idx << 1 | 1];
    }

    function querySum(idx, l, r, ql, qr) {
        if (ql <= l && r <= qr) return sum[idx];
        push(idx, l, r);
        const mid = (l + r) >> 1;
        let res = 0;
        if (ql <= mid) res += querySum(idx << 1, l, mid, ql, qr);
        if (qr > mid) res += querySum(idx << 1 | 1, mid + 1, r, ql, qr);
        return res;
    }

    build(1, 0, n - 1);
    const result = [];

    for (const [type, a, b] of queries) {
        if (type === 1) {               // flip nums1 in range [a,b]
            rangeFlip(1, 0, n - 1, a, b);
        } else if (type === 2) {        // add value a to nums2 where nums1 == 1
            const p = a;
            rangeAdd(1, 0, n - 1, 0, n - 1, p);
        } else {                        // type 3: sum query on nums2 in [a,b]
            result.push(querySum(1, 0, n - 1, a, b));
        }
    }

    return result;
};
```

## Typescript

```typescript
function handleQuery(nums1: number[], nums2: number[], queries: number[][]): number[] {
    const n = nums1.length;
    const size = 4 * n;
    const cnt1 = new Array<number>(size).fill(0);      // count of ones in nums1
    const sum2 = new Array<number>(size).fill(0);      // sum of nums2
    const lazyFlip = new Array<boolean>(size).fill(false);
    const lazyAdd = new Array<number>(size).fill(0);

    function build(node: number, l: number, r: number): void {
        if (l === r) {
            cnt1[node] = nums1[l];
            sum2[node] = nums2[l];
            return;
        }
        const mid = (l + r) >> 1;
        build(node << 1, l, mid);
        build((node << 1) | 1, mid + 1, r);
        cnt1[node] = cnt1[node << 1] + cnt1[(node << 1) | 1];
        sum2[node] = sum2[node << 1] + sum2[(node << 1) | 1];
    }

    function applyFlip(node: number, len: number): void {
        cnt1[node] = len - cnt1[node];
        lazyFlip[node] = !lazyFlip[node];
    }

    function applyAdd(node: number, p: number, len: number): void {
        sum2[node] += cnt1[node] * p;
        lazyAdd[node] += p;
    }

    function push(node: number, l: number, r: number): void {
        if (l === r) return;
        const mid = (l + r) >> 1;
        const left = node << 1;
        const right = left | 1;

        if (lazyFlip[node]) {
            applyFlip(left, mid - l + 1);
            applyFlip(right, r - mid);
            lazyFlip[node] = false;
        }
        if (lazyAdd[node] !== 0) {
            const addVal = lazyAdd[node];
            applyAdd(left, addVal, mid - l + 1);
            applyAdd(right, addVal, r - mid);
            lazyAdd[node] = 0;
        }
    }

    function updateFlip(node: number, l: number, r: number, ql: number, qr: number): void {
        if (ql <= l && r <= qr) {
            applyFlip(node, r - l + 1);
            return;
        }
        push(node, l, r);
        const mid = (l + r) >> 1;
        if (ql <= mid) updateFlip(node << 1, l, mid, ql, qr);
        if (qr > mid) updateFlip((node << 1) | 1, mid + 1, r, ql, qr);
        const left = node << 1, right = left | 1;
        cnt1[node] = cnt1[left] + cnt1[right];
        sum2[node] = sum2[left] + sum2[right];
    }

    function addOnes(node: number, l: number, r: number, p: number): void {
        // whole segment update
        applyAdd(node, p, r - l + 1);
    }

    function querySum(node: number, l: number, r: number, ql: number, qr: number): number {
        if (ql <= l && r <= qr) return sum2[node];
        push(node, l, r);
        const mid = (l + r) >> 1;
        let res = 0;
        if (ql <= mid) res += querySum(node << 1, l, mid, ql, qr);
        if (qr > mid) res += querySum((node << 1) | 1, mid + 1, r, ql, qr);
        return res;
    }

    build(1, 0, n - 1);
    const ans: number[] = [];

    for (const q of queries) {
        const type = q[0];
        if (type === 1) {
            const l = q[1], r = q[2];
            updateFlip(1, 0, n - 1, l, r);
        } else if (type === 2) {
            const p = q[1];
            addOnes(1, 0, n - 1, p);
        } else { // type === 3
            const l = q[1], r = q[2];
            ans.push(querySum(1, 0, n - 1, l, r));
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
    function handleQuery($nums1, $nums2, $queries) {
        $this->n = count($nums1);
        $size = 4 * $this->n + 5;
        $this->cnt = array_fill(0, $size, 0);       // number of ones in nums1
        $this->sum = array_fill(0, $size, 0);       // sum of nums2
        $this->len = array_fill(0, $size, 0);       // segment length
        $this->lazyFlip = array_fill(0, $size, 0);
        $this->lazyAdd = array_fill(0, $size, 0);
        $this->nums1 = $nums1;
        $this->nums2 = $nums2;
        $this->build(1, 0, $this->n - 1);

        $ans = [];
        foreach ($queries as $q) {
            $type = $q[0];
            $x = $q[1];
            $y = $q[2];
            if ($type == 1) {               // flip range [x, y] in nums1
                $this->rangeFlip(1, 0, $this->n - 1, $x, $y);
            } elseif ($type == 2) {         // add x to each nums2[i] where nums1[i]==1
                $p = $x;
                $this->addOnes(1, 0, $this->n - 1, $p);
            } else {                         // type 3: sum query on nums2 range [x, y]
                $res = $this->querySum(1, 0, $this->n - 1, $x, $y);
                $ans[] = $res;
            }
        }
        return $ans;
    }

    private function build($idx, $l, $r) {
        $this->len[$idx] = $r - $l + 1;
        if ($l == $r) {
            $this->cnt[$idx] = $this->nums1[$l];
            $this->sum[$idx] = $this->nums2[$l];
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->build($idx * 2, $l, $mid);
        $this->build($idx * 2 + 1, $mid + 1, $r);
        $this->pull($idx);
    }

    private function pull($idx) {
        $lc = $idx * 2;
        $rc = $idx * 2 + 1;
        $this->cnt[$idx] = $this->cnt[$lc] + $this->cnt[$rc];
        $this->sum[$idx] = $this->sum[$lc] + $this->sum[$rc];
    }

    private function push($idx) {
        $lc = $idx * 2;
        $rc = $idx * 2 + 1;

        // propagate flip
        if ($this->lazyFlip[$idx]) {
            // left child
            $this->cnt[$lc] = $this->len[$lc] - $this->cnt[$lc];
            $this->lazyFlip[$lc] ^= 1;
            // right child
            $this->cnt[$rc] = $this->len[$rc] - $this->cnt[$rc];
            $this->lazyFlip[$rc] ^= 1;

            $this->lazyFlip[$idx] = 0;
        }

        // propagate add-to-ones
        if ($this->lazyAdd[$idx] != 0) {
            $add = $this->lazyAdd[$idx];

            $this->sum[$lc] += $add * $this->cnt[$lc];
            $this->lazyAdd[$lc] += $add;

            $this->sum[$rc] += $add * $this->cnt[$rc];
            $this->lazyAdd[$rc] += $add;

            $this->lazyAdd[$idx] = 0;
        }
    }

    private function rangeFlip($idx, $l, $r, $ql, $qr) {
        if ($ql <= $l && $r <= $qr) {
            $this->cnt[$idx] = $this->len[$idx] - $this->cnt[$idx];
            $this->lazyFlip[$idx] ^= 1;
            return;
        }
        $this->push($idx);
        $mid = intdiv($l + $r, 2);
        if ($ql <= $mid) {
            $this->rangeFlip($idx * 2, $l, $mid, $ql, $qr);
        }
        if ($qr > $mid) {
            $this->rangeFlip($idx * 2 + 1, $mid + 1, $r, $ql, $qr);
        }
        $this->pull($idx);
    }

    private function addOnes($idx, $l, $r, $p) {
        // whole segment update
        $this->sum[$idx] += $p * $this->cnt[$idx];
        $this->lazyAdd[$idx] += $p;
    }

    private function querySum($idx, $l, $r, $ql, $qr) {
        if ($ql <= $l && $r <= $qr) {
            return $this->sum[$idx];
        }
        $this->push($idx);
        $mid = intdiv($l + $r, 2);
        $res = 0;
        if ($ql <= $mid) {
            $res += $this->querySum($idx * 2, $l, $mid, $ql, $qr);
        }
        if ($qr > $mid) {
            $res += $this->querySum($idx * 2 + 1, $mid + 1, $r, $ql, $qr);
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    struct Fenwick {
        var n: Int
        var bit: [Int64]
        init(_ n: Int) {
            self.n = n
            self.bit = Array(repeating: 0, count: n + 1)
        }
        mutating func add(_ idx: Int, _ delta: Int64) {
            var i = idx + 1
            while i <= n {
                bit[i] += delta
                i += i & -i
            }
        }
        func sum(_ idx: Int) -> Int64 {
            if idx < 0 { return 0 }
            var res: Int64 = 0
            var i = idx + 1
            while i > 0 {
                res += bit[i]
                i -= i & -i
            }
            return res
        }
        func rangeSum(_ l: Int, _ r: Int) -> Int64 {
            if l > r { return 0 }
            return sum(r) - sum(l - 1)
        }
    }

    func handleQuery(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums1.count
        var baseBIT = Fenwick(n)
        var onesBIT = Fenwick(n)
        var offsetBIT = Fenwick(n)

        for i in 0..<n {
            baseBIT.add(i, Int64(nums2[i]))
        }

        // DSU to skip already activated positions
        var parent = [Int](repeating: 0, count: n + 1)
        for i in 0...n { parent[i] = i }

        func find(_ x: Int) -> Int {
            if parent[x] == x { return x }
            parent[x] = find(parent[x])
            return parent[x]
        }

        // initialize active ones
        for i in 0..<n {
            if nums1[i] == 1 {
                onesBIT.add(i, 1)
                // offset is zero initially, no need to add
                parent[i] = find(i + 1)   // remove from zero set
            }
        }

        var curAdd: Int64 = 0
        var answer: [Int] = []

        for q in queries {
            let type = q[0]
            if type == 1 {
                let l = q[1], r = q[2]
                var idx = find(l)
                while idx <= r && idx < n {
                    onesBIT.add(idx, 1)
                    offsetBIT.add(idx, curAdd)
                    parent[idx] = find(idx + 1)   // mark as activated
                    idx = find(idx)               // next zero position
                }
            } else if type == 2 {
                let p = q[1]
                curAdd += Int64(p)
            } else { // type == 3
                // total sum of nums2 after all updates
                let baseSum = baseBIT.rangeSum(0, n - 1)
                let onesCount = onesBIT.rangeSum(0, n - 1)
                let offsetSum = offsetBIT.rangeSum(0, n - 1)
                let total = baseSum + curAdd * onesCount - offsetSum
                answer.append(Int(total))
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun handleQuery(nums1: IntArray, nums2: IntArray, queries: Array<IntArray>): LongArray {
        val n = nums1.size
        val seg = SegmentTree(nums1)
        var totalSum = 0L
        for (v in nums2) totalSum += v.toLong()
        val result = mutableListOf<Long>()
        for (q in queries) {
            when (q[0]) {
                1 -> { // flip range in nums1
                    seg.rangeFlip(q[1], q[2])
                }
                2 -> { // add p to each nums2[i] where nums1[i]==1
                    val p = q[1].toLong()
                    val ones = seg.totalOnes().toLong()
                    totalSum += p * ones
                }
                3 -> { // query total sum of nums2
                    result.add(totalSum)
                }
            }
        }
        return result.toLongArray()
    }

    private class SegmentTree(private val arr: IntArray) {
        private val n = arr.size
        private val sum = IntArray(n * 4)
        private val lazy = BooleanArray(n * 4)

        init { build(1, 0, n - 1) }

        private fun build(node: Int, l: Int, r: Int) {
            if (l == r) {
                sum[node] = arr[l]
                return
            }
            val mid = (l + r) ushr 1
            build(node shl 1, l, mid)
            build(node shl 1 or 1, mid + 1, r)
            pull(node)
        }

        private fun applyFlip(node: Int, l: Int, r: Int) {
            sum[node] = (r - l + 1) - sum[node]
            lazy[node] = !lazy[node]
        }

        private fun push(node: Int, l: Int, r: Int) {
            if (!lazy[node]) return
            val mid = (l + r) ushr 1
            applyFlip(node shl 1, l, mid)
            applyFlip(node shl 1 or 1, mid + 1, r)
            lazy[node] = false
        }

        private fun pull(node: Int) {
            sum[node] = sum[node shl 1] + sum[node shl 1 or 1]
        }

        private fun update(node: Int, l: Int, r: Int, ql: Int, qr: Int) {
            if (ql > r || qr < l) return
            if (ql <= l && r <= qr) {
                applyFlip(node, l, r)
                return
            }
            push(node, l, r)
            val mid = (l + r) ushr 1
            update(node shl 1, l, mid, ql, qr)
            update(node shl 1 or 1, mid + 1, r, ql, qr)
            pull(node)
        }

        fun rangeFlip(left: Int, right: Int) {
            update(1, 0, n - 1, left, right)
        }

        fun totalOnes(): Int = sum[1]
    }
}
```

## Dart

```dart
class SegmentTree {
  final int n;
  final List<int> _tree;
  final List<bool> _lazy;

  SegmentTree(List<int> arr)
      : n = arr.length,
        _tree = List.filled(arr.length * 4, 0),
        _lazy = List.filled(arr.length * 4, false) {
    _build(1, 0, n - 1, arr);
  }

  void _build(int node, int l, int r, List<int> arr) {
    if (l == r) {
      _tree[node] = arr[l];
      return;
    }
    final mid = (l + r) >> 1;
    _build(node << 1, l, mid, arr);
    _build((node << 1) | 1, mid + 1, r, arr);
    _tree[node] = _tree[node << 1] + _tree[(node << 1) | 1];
  }

  void _apply(int node, int l, int r) {
    _tree[node] = (r - l + 1) - _tree[node];
    _lazy[node] = !_lazy[node];
  }

  void _push(int node, int l, int r) {
    if (_lazy[node]) {
      final mid = (l + r) >> 1;
      _apply(node << 1, l, mid);
      _apply((node << 1) | 1, mid + 1, r);
      _lazy[node] = false;
    }
  }

  void updateFlip(int L, int R) => _update(1, 0, n - 1, L, R);

  void _update(int node, int l, int r, int L, int R) {
    if (L > r || R < l) return;
    if (L <= l && r <= R) {
      _apply(node, l, r);
      return;
    }
    _push(node, l, r);
    final mid = (l + r) >> 1;
    _update(node << 1, l, mid, L, R);
    _update((node << 1) | 1, mid + 1, r, L, R);
    _tree[node] = _tree[node << 1] + _tree[(node << 1) | 1];
  }

  int query(int L, int R) => _query(1, 0, n - 1, L, R);

  int _query(int node, int l, int r, int L, int R) {
    if (L > r || R < l) return 0;
    if (L <= l && r <= R) return _tree[node];
    _push(node, l, r);
    final mid = (l + r) >> 1;
    return _query(node << 1, l, mid, L, R) +
        _query((node << 1) | 1, mid + 1, r, L, R);
  }
}

class Solution {
  List<int> handleQuery(List<int> nums1, List<int> nums2, List<List<int>> queries) {
    final seg = SegmentTree(nums1);
    int cntOnes = 0;
    for (final v in nums1) cntOnes += v;
    int totalSum = 0;
    for (final v in nums2) totalSum += v;

    final List<int> ans = [];
    for (final q in queries) {
      final type = q[0];
      if (type == 1) {
        final l = q[1];
        final r = q[2];
        final onesInRange = seg.query(l, r);
        final len = r - l + 1;
        cntOnes += (len - 2 * onesInRange);
        seg.updateFlip(l, r);
      } else if (type == 2) {
        final p = q[1];
        totalSum += p * cntOnes;
      } else { // type == 3
        ans.add(totalSum);
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

func handleQuery(nums1 []int, nums2 []int, queries [][]int) []int64 {
	n := len(nums1)
	size := 4 * n
	cnt := make([]int, size)      // number of ones in nums1 for the segment
	sum := make([]int64, size)    // sum of nums2 for the segment
	lazySet := make([]bool, size) // lazy flag: whole segment set to 1

	var build func(node, l, r int)
	build = func(node, l, r int) {
		if l == r {
			cnt[node] = nums1[l]
			sum[node] = int64(nums2[l])
			return
		}
		mid := (l + r) >> 1
		build(node<<1, l, mid)
		build(node<<1|1, mid+1, r)
		cnt[node] = cnt[node<<1] + cnt[node<<1|1]
		sum[node] = sum[node<<1] + sum[node<<1|1]
	}
	build(1, 0, n-1)

	applySet := func(node, l, r int) {
		cnt[node] = r - l + 1
		lazySet[node] = true
	}

	var push func(node, l, r int)
	push = func(node, l, r int) {
		if !lazySet[node] || l == r {
			return
		}
		mid := (l + r) >> 1
		left, right := node<<1, node<<1|1
		applySet(left, l, mid)
		applySet(right, mid+1, r)
		lazySet[node] = false
	}

	var rangeSet func(node, l, r, ql, qr int)
	rangeSet = func(node, l, r, ql, qr int) {
		if ql <= l && r <= qr {
			applySet(node, l, r)
			return
		}
		push(node, l, r)
		mid := (l + r) >> 1
		if ql <= mid {
			rangeSet(node<<1, l, mid, ql, qr)
		}
		if qr > mid {
			rangeSet(node<<1|1, mid+1, r, ql, qr)
		}
		cnt[node] = cnt[node<<1] + cnt[node<<1|1]
		sum[node] = sum[node<<1] + sum[node<<1|1]
	}

	var addOnes func(val int) {
		if val == 0 {
			return
		}
		add := int64(cnt[1]) * int64(val)
		sum[1] += add
		// No need for lazy propagation because future set operations do not inherit past adds.
	}

	var querySum func(node, l, r, ql, qr int) int64
	querySum = func(node, l, r, ql, qr int) int64 {
		if ql <= l && r <= qr {
			return sum[node]
		}
		push(node, l, r)
		mid := (l + r) >> 1
		var res int64
		if ql <= mid {
			res += querySum(node<<1, l, mid, ql, qr)
		}
		if qr > mid {
			res += querySum(node<<1|1, mid+1, r, ql, qr)
		}
		return res
	}

	var ans []int64
	for _, q := range queries {
		switch q[0] {
		case 1:
			l, r := q[1], q[2]
			rangeSet(1, 0, n-1, l, r)
		case 2:
			val := q[1]
			addOnes(val)
		case 3:
			// According to problem examples, return total sum of nums2.
			ans = append(ans, sum[1])
		}
	}
	return ans
}
```

## Ruby

```ruby
class SegmentTree
  def initialize(arr)
    @n = arr.size
    @tree = Array.new(@n * 4, 0)
    @lazy = Array.new(@n * 4, false)
    build(1, 0, @n - 1, arr)
  end

  def flip(l, r)
    update(1, 0, @n - 1, l, r)
  end

  def count_ones
    @tree[1]
  end

  private

  def build(node, l, r, arr)
    if l == r
      @tree[node] = arr[l]
    else
      mid = (l + r) / 2
      build(node * 2, l, mid, arr)
      build(node * 2 + 1, mid + 1, r, arr)
      @tree[node] = @tree[node * 2] + @tree[node * 2 + 1]
    end
  end

  def push(node, l, r)
    if @lazy[node]
      @tree[node] = (r - l + 1) - @tree[node]
      if l != r
        @lazy[node * 2] ^= true
        @lazy[node * 2 + 1] ^= true
      end
      @lazy[node] = false
    end
  end

  def update(node, l, r, ql, qr)
    push(node, l, r)
    return if ql > r || qr < l
    if ql <= l && r <= qr
      @lazy[node] ^= true
      push(node, l, r)
      return
    end
    mid = (l + r) / 2
    update(node * 2, l, mid, ql, qr)
    update(node * 2 + 1, mid + 1, r, ql, qr)
    @tree[node] = @tree[node * 2] + @tree[node * 2 + 1]
  end
end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def handle_query(nums1, nums2, queries)
  seg = SegmentTree.new(nums1)
  total_sum = nums2.sum
  ans = []

  queries.each do |type, a, b|
    case type
    when 1
      seg.flip(a, b)
    when 2
      p_val = a
      total_sum += p_val * seg.count_ones
    when 3
      ans << total_sum
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def handleQuery(nums1: Array[Int], nums2: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
        val n = nums1.length
        val size = 4 * n
        val cnt1 = new Array[Int](size)
        val sum2 = new Array[Long](size)
        val lazySet = new Array[Boolean](size)
        val lazyAdd = new Array[Long](size)

        def build(idx: Int, l: Int, r: Int): Unit = {
            if (l == r) {
                cnt1(idx) = nums1(l)
                sum2(idx) = nums2(l).toLong
            } else {
                val mid = (l + r) >> 1
                val left = idx << 1
                val right = left | 1
                build(left, l, mid)
                build(right, mid + 1, r)
                pull(idx)
            }
        }

        def pull(idx: Int): Unit = {
            val left = idx << 1
            val right = left | 1
            cnt1(idx) = cnt1(left) + cnt1(right)
            sum2(idx) = sum2(left) + sum2(right)
        }

        def applySet(idx: Int, l: Int, r: Int): Unit = {
            cnt1(idx) = r - l + 1
            lazySet(idx) = true
            lazyAdd(idx) = 0L
        }

        def applyAdd(idx: Int, v: Long, l: Int, r: Int): Unit = {
            sum2(idx) += v * cnt1(idx).toLong
            lazyAdd(idx) += v
        }

        def push(idx: Int, l: Int, r: Int): Unit = {
            if (l == r) return
            val mid = (l + r) >> 1
            val left = idx << 1
            val right = left | 1
            if (lazySet(idx)) {
                applySet(left, l, mid)
                applySet(right, mid + 1, r)
                lazySet(idx) = false
            }
            if (lazyAdd(idx) != 0L) {
                val v = lazyAdd(idx)
                applyAdd(left, v, l, mid)
                applyAdd(right, v, mid + 1, r)
                lazyAdd(idx) = 0L
            }
        }

        def updateSet(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Unit = {
            if (ql <= l && r <= qr) {
                applySet(idx, l, r)
                return
            }
            push(idx, l, r)
            val mid = (l + r) >> 1
            if (ql <= mid) updateSet(idx << 1, l, mid, ql, qr)
            if (qr > mid) updateSet((idx << 1) | 1, mid + 1, r, ql, qr)
            pull(idx)
        }

        def querySum(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Long = {
            if (ql <= l && r <= qr) return sum2(idx)
            push(idx, l, r)
            val mid = (l + r) >> 1
            var res = 0L
            if (ql <= mid) res += querySum(idx << 1, l, mid, ql, qr)
            if (qr > mid) res += querySum((idx << 1) | 1, mid + 1, r, ql, qr)
            res
        }

        build(1, 0, n - 1)

        val ans = scala.collection.mutable.ArrayBuffer[Long]()
        for (q <- queries) {
            q(0) match {
                case 1 =>
                    val l = q(1)
                    val r = q(2)
                    updateSet(1, 0, n - 1, l, r)
                case 2 =>
                    val p = q(1).toLong
                    applyAdd(1, p, 0, n - 1) // global add to positions where nums1 == 1
                case 3 =>
                    val l = q(1)
                    val r = q(2)
                    ans += querySum(1, 0, n - 1, l, r)
            }
        }

        ans.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn handle_query(nums1: Vec<i32>, nums2: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        use std::collections::BTreeSet;
        let n = nums1.len();
        let mut zero_set: BTreeSet<usize> = BTreeSet::new();
        for (i, &v) in nums1.iter().enumerate() {
            if v == 0 {
                zero_set.insert(i);
            }
        }
        let mut ones_cnt = n - zero_set.len(); // number of 1s in nums1
        let mut total_sum: i64 = nums2.iter().map(|&x| x as i64).sum();
        let mut ans = Vec::new();

        for q in queries {
            match q[0] {
                1 => {
                    let l = q[1] as usize;
                    let r = q[2] as usize;
                    // collect zeros in [l, r] and turn them to 1
                    let to_remove: Vec<usize> = zero_set.range(l..=r).cloned().collect();
                    for idx in to_remove {
                        zero_set.remove(&idx);
                        ones_cnt += 1;
                    }
                }
                2 => {
                    let p = q[1] as i64;
                    total_sum += p * (ones_cnt as i64);
                }
                3 => {
                    ans.push(total_sum);
                }
                _ => {}
            }
        }

        ans
    }
}
```

## Racket

```racket
#lang racket
(require racket/vector)
(require racket/match)

(define (handle-query nums1 nums2 queries)
  (let* ((n (length nums1))
         (size (* 4 n))
         (cnt (make-vector size 0))
         (lazy (make-vector size #f))
         (v1 (list->vector nums1)))
    ;; build segment tree storing count of ones
    (define (build node l r)
      (if (= l r)
          (vector-set! cnt node (vector-ref v1 l))
          (let ((mid (quotient (+ l r) 2)))
            (build (* node 2) l mid)
            (build (+ node 1) (+ mid 1) r)
            (vector-set! cnt node
                         (+ (vector-ref cnt (* node 2))
                            (vector-ref cnt (+ node 1)))))))
    ;; flip count for a node of given length
    (define (apply-flip node len)
      (vector-set! cnt node (- len (vector-ref cnt node))))
    ;; propagate lazy flag to children
    (define (push node l r)
      (when (vector-ref lazy node)
        (let* ((mid (quotient (+ l r) 2))
               (left (* node 2))
               (right (+ node 1))
               (len-left (+ (- mid l) 1))
               (len-right (+ (- r mid) 1)))
          (apply-flip left len-left)
          (vector-set! lazy left (not (vector-ref lazy left)))
          (apply-flip right len-right)
          (vector-set! lazy right (not (vector-ref lazy right))))
        (vector-set! lazy node #f)))
    ;; range flip [ql,qr]
    (define (update node l r ql qr)
      (if (and (<= ql l) (>= qr r))
          (begin
            (apply-flip node (+ (- r l) 1))
            (vector-set! lazy node (not (vector-ref lazy node))))
          (begin
            (push node l r)
            (let ((mid (quotient (+ l r) 2)))
              (when (<= ql mid)
                (update (* node 2) l mid ql qr))
              (when (>= qr (+ mid 1))
                (update (+ node 1) (+ mid 1) r ql qr))
              (vector-set! cnt node
                           (+ (vector-ref cnt (* node 2))
                              (vector-ref cnt (+ node 1))))))))
    ;; initialize structures
    (build 1 0 (- n 1))
    (define total (apply + 0 nums2))
    ;; process queries
    (let loop ((qs queries) (ans total) (out '()))
      (if (null? qs)
          (reverse out)
          (match (car qs)
            [(list type x y)
             (cond
               [(= type 1) (begin (update 1 0 (- n 1) x y)
                                  (loop (cdr qs) ans out))]
               [(= type 2) (let ((new-ans (+ ans (* x (vector-ref cnt 1)))))
                             (loop (cdr qs) new-ans out))]
               [(= type 3) (loop (cdr qs) ans (cons ans out))])])))))
```

## Erlang

```erlang
-spec handle_query(Nums1 :: [integer()], Nums2 :: [integer()], Queries :: [[integer()]]) -> [integer()].
handle_query(Nums1, Nums2, Queries) ->
    N = length(Nums1),
    Tuple1 = list_to_tuple(Nums1),
    Tree0 = build_tree(Tuple1, 0, N - 1, 1, #{}),
    TotalOnes0 = lists:sum(Nums1),
    Sum2_0 = lists:sum(Nums2),
    {AnsRev, _Tree, _TotalOnes, _Sum2} = process_queries(Queries, Tree0, TotalOnes0, Sum2_0, [], N),
    lists:reverse(AnsRev).

%% Build segment tree storing count of ones in each node
build_tree(_Tuple, L, R, _Node, Map) when L > R ->
    Map;
build_tree(Tuple, L, R, Node, Map) ->
    if L == R ->
            Val = element(L + 1, Tuple),
            maps:put(Node, Val, Map);
       true ->
            Mid = (L + R) div 2,
            Map1 = build_tree(Tuple, L, Mid, Node * 2, Map),
            Map2 = build_tree(Tuple, Mid + 1, R, Node * 2 + 1, Map1),
            LeftCnt = maps:get(Node * 2, Map2),
            RightCnt = maps:get(Node * 2 + 1, Map2),
            maps:put(Node, LeftCnt + RightCnt, Map2)
    end.

%% Update range [QL,QR] to all ones; return new map and delta added ones
update(L, R, QL, QR, Node, Map) ->
    if QL > R orelse QR < L ->
            {Map, 0};
       QL =< L, R =< QR ->
            OldCnt = maps:get(Node, Map),
            Len = R - L + 1,
            if OldCnt == Len ->
                    {Map, 0};
               true ->
                    NewMap = maps:put(Node, Len, Map),
                    Delta = Len - OldCnt,
                    {NewMap, Delta}
            end;
       true ->
            Mid = (L + R) div 2,
            {Map1, D1} = update(L, Mid, QL, QR, Node * 2, Map),
            {Map2, D2} = update(Mid + 1, R, QL, QR, Node * 2 + 1, Map1),
            LeftCnt = maps:get(Node * 2, Map2),
            RightCnt = maps:get(Node * 2 + 1, Map2),
            NewCnt = LeftCnt + RightCnt,
            NewMap = maps:put(Node, NewCnt, Map2),
            {NewMap, D1 + D2}
    end.

process_queries([], Tree, TotalOnes, Sum2, Acc, _N) ->
    {Acc, Tree, TotalOnes, Sum2};
process_queries([Q | Rest], Tree, TotalOnes, Sum2, Acc, N) ->
    [Type | Params] = Q,
    case Type of
        1 ->
            [_ , L, R] = Q,
            {NewTree, Delta} = update(0, N - 1, L, R, 1, Tree),
            process_queries(Rest, NewTree, TotalOnes + Delta, Sum2, Acc, N);
        2 ->
            [_ , P, _] = Q,
            NewSum2 = Sum2 + P * TotalOnes,
            process_queries(Rest, Tree, TotalOnes, NewSum2, Acc, N);
        3 ->
            process_queries(Rest, Tree, TotalOnes, Sum2, [Sum2 | Acc], N)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec handle_query(nums1 :: [integer], nums2 :: [integer], queries :: [[integer]]) :: [integer]
  def handle_query(nums1, nums2, queries) do
    n = length(nums1)
    :ets.new(:seg, [:set, :private])

    build(1, 0, n - 1, nums1, nums2)

    ans_rev =
      Enum.reduce(queries, [], fn query, acc ->
        case query do
          [1, l, r] ->
            flip_range(1, 0, n - 1, l, r)
            acc

          [2, p, _] ->
            apply_add_global(p)
            acc

          [3, l, r] ->
            sum = range_sum(1, 0, n - 1, l, r)
            [sum | acc]
        end
      end)

    :ets.delete(:seg)
    Enum.reverse(ans_rev)
  end

  # Build segment tree
  defp build(node, l, r, nums1, nums2) do
    if l == r do
      cnt = Enum.at(nums1, l)
      sum = Enum.at(nums2, l)
      :ets.insert(:seg, {node, cnt, sum, 0})
    else
      mid = div(l + r, 2)
      left = node * 2
      right = node * 2 + 1

      build(left, l, mid, nums1, nums2)
      build(right, mid + 1, r, nums1, nums2)

      {cnt_l, sum_l, _} = get(left)
      {cnt_r, sum_r, _} = get(right)

      :ets.insert(:seg, {node, cnt_l + cnt_r, sum_l + sum_r, 0})
    end
  end

  # Retrieve node data
  defp get(node) do
    [{^node, cnt, sum, lazy}] = :ets.lookup(:seg, node)
    {cnt, sum, lazy}
  end

  # Store node data
  defp set_node(node, cnt, sum, lazy) do
    :ets.insert(:seg, {node, cnt, sum, lazy})
  end

  # Apply addition p to all positions where nums1 == 1 in this segment
  defp apply_add(node, p) do
    {cnt, sum, lazy} = get(node)
    new_sum = sum + cnt * p
    new_lazy = lazy + p
    set_node(node, cnt, new_sum, new_lazy)
  end

  # Push pending lazy addition to children
  defp push(node, l, r) do
    {_, _, lazy} = get(node)

    if lazy != 0 and l != r do
      left = node * 2
      right = node * 2 + 1

      apply_add(left, lazy)
      apply_add(right, lazy)

      {cnt, sum, _} = get(node)
      set_node(node, cnt, sum, 0)
    end
  end

  # Flip bits in nums1 over [ql, qr]
  defp flip_range(node, l, r, ql, qr) do
    if ql <= l and r <= qr do
      {cnt, sum, lazy} = get(node)
      len = r - l + 1
      new_cnt = len - cnt
      set_node(node, new_cnt, sum, lazy)
    else
      push(node, l, r)
      mid = div(l + r, 2)
      left = node * 2
      right = node * 2 + 1

      if ql <= mid do
        flip_range(left, l, mid, ql, qr)
      end

      if qr > mid do
        flip_range(right, mid + 1, r, ql, qr)
      end

      {cnt_l, sum_l, _} = get(left)
      {cnt_r, sum_r, _} = get(right)
      {_, _, lazy_cur} = get(node)

      set_node(node, cnt_l + cnt_r, sum_l + sum_r, lazy_cur)
    end
  end

  # Apply addition globally (type 2 query)
  defp apply_add_global(p) do
    apply_add(1, p)
  end

  # Range sum query on nums2
  defp range_sum(node, l, r, ql, qr) do
    if ql <= l and r <= qr do
      {_, sum, _} = get(node)
      sum
    else
      push(node, l, r)
      mid = div(l + r, 2)
      res = 0

      if ql <= mid do
        res = res + range_sum(node * 2, l, mid, ql, qr)
      end

      if qr > mid do
        res = res + range_sum(node * 2 + 1, mid + 1, r, ql, qr)
      end

      res
    end
  end
end
```

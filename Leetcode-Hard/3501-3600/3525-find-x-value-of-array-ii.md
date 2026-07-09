# 3525. Find X Value of Array II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    struct Node {
        int prod;
        int cnt[5][5];
        Node() { prod = 1; memset(cnt, 0, sizeof(cnt)); }
    };
    
    int n, K;
    vector<Node> seg;
    vector<int> arr;
    
    Node mergeNode(const Node& L, const Node& R) {
        if (K == 0) return Node();
        Node res;
        res.prod = (L.prod * R.prod) % K;
        for (int s = 0; s < K; ++s) {
            int enterR = (s * L.prod) % K;
            for (int x = 0; x < K; ++x) {
                res.cnt[s][x] = L.cnt[s][x] + R.cnt[enterR][x];
            }
        }
        return res;
    }
    
    void build(int idx, int l, int r) {
        if (l == r) {
            Node &node = seg[idx];
            node.prod = arr[l] % K;
            for (int s = 0; s < K; ++s) {
                int rem = (s * node.prod) % K;
                node.cnt[s][rem] = 1;
            }
            return;
        }
        int mid = (l + r) >> 1;
        build(idx<<1, l, mid);
        build(idx<<1|1, mid+1, r);
        seg[idx] = mergeNode(seg[idx<<1], seg[idx<<1|1]);
    }
    
    void pointUpdate(int idx, int l, int r, int pos, int valMod) {
        if (l == r) {
            Node &node = seg[idx];
            node.prod = valMod % K;
            for (int i = 0; i < K; ++i)
                for (int j = 0; j < K; ++j)
                    node.cnt[i][j] = 0;
            for (int s = 0; s < K; ++s) {
                int rem = (s * node.prod) % K;
                node.cnt[s][rem] = 1;
            }
            return;
        }
        int mid = (l + r) >> 1;
        if (pos <= mid) pointUpdate(idx<<1, l, mid, pos, valMod);
        else pointUpdate(idx<<1|1, mid+1, r, pos, valMod);
        seg[idx] = mergeNode(seg[idx<<1], seg[idx<<1|1]);
    }
    
    Node rangeQuery(int idx, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return Node(); // identity
        if (ql <= l && r <= qr) return seg[idx];
        int mid = (l + r) >> 1;
        Node left = rangeQuery(idx<<1, l, mid, ql, qr);
        Node right = rangeQuery(idx<<1|1, mid+1, r, ql, qr);
        return mergeNode(left, right);
    }
    
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        K = k;
        n = nums.size();
        arr.resize(n);
        for (int i = 0; i < n; ++i) arr[i] = nums[i] % K;
        seg.assign(4*n+5, Node());
        if (n) build(1, 0, n-1);
        
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &q : queries) {
            int idx = q[0];
            int val = q[1] % K;
            int start = q[2];
            int xi = q[3];
            
            pointUpdate(1, 0, n-1, idx, val);
            
            int remStart;
            if (start == 0) {
                remStart = 1 % K;
            } else {
                Node leftNode = rangeQuery(1, 0, n-1, 0, start-1);
                remStart = leftNode.prod;
            }
            Node rangeNode = rangeQuery(1, 0, n-1, start, n-1);
            ans.push_back(rangeNode.cnt[remStart][xi]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        int[] cnt;
        int prod;
        Node(int k) {
            cnt = new int[k];
            prod = 1 % k; // identity product
        }
    }

    private int n, K;
    private Node[] seg;

    public int[] resultArray(int[] nums, int k, int[][] queries) {
        this.K = k;
        this.n = nums.length;
        seg = new Node[4 * n];
        build(1, 0, n - 1, nums);
        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int idx = queries[i][0];
            int val = queries[i][1] % K;
            int start = queries[i][2];
            int xi = queries[i][3];
            update(1, 0, n - 1, idx, val);
            Node res = query(1, 0, n - 1, start, n - 1);
            ans[i] = (res == null) ? 0 : res.cnt[xi];
        }
        return ans;
    }

    private void build(int node, int l, int r, int[] arr) {
        if (l == r) {
            seg[node] = leaf(arr[l] % K);
            return;
        }
        int mid = (l + r) >>> 1;
        build(node << 1, l, mid, arr);
        build(node << 1 | 1, mid + 1, r, arr);
        seg[node] = merge(seg[node << 1], seg[node << 1 | 1]);
    }

    private Node leaf(int rem) {
        Node nd = new Node(K);
        nd.cnt[rem] = 1;
        nd.prod = rem;
        return nd;
    }

    private void update(int node, int l, int r, int idx, int valRem) {
        if (l == r) {
            seg[node] = leaf(valRem);
            return;
        }
        int mid = (l + r) >>> 1;
        if (idx <= mid) update(node << 1, l, mid, idx, valRem);
        else update(node << 1 | 1, mid + 1, r, idx, valRem);
        seg[node] = merge(seg[node << 1], seg[node << 1 | 1]);
    }

    private Node query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return null;
        if (ql <= l && r <= qr) return seg[node];
        int mid = (l + r) >>> 1;
        Node left = query(node << 1, l, mid, ql, qr);
        Node right = query(node << 1 | 1, mid + 1, r, ql, qr);
        return merge(left, right);
    }

    private Node merge(Node a, Node b) {
        if (a == null) return b;
        if (b == null) return a;
        Node res = new Node(K);
        // copy counts from left segment
        for (int i = 0; i < K; i++) {
            res.cnt[i] = a.cnt[i];
        }
        int prodL = a.prod;
        // shift right counts by product of left segment
        for (int j = 0; j < K; j++) {
            if (b.cnt[j] != 0) {
                int idx = (prodL * j) % K;
                res.cnt[idx] += b.cnt[j];
            }
        }
        res.prod = (a.prod * b.prod) % K;
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        # segment tree arrays
        prod = [0] * (size << 1)
        freq = [[0] * k for _ in range(size << 1)]

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                prod[node] = v
                f = freq[node]
                f[v] += 1
            else:
                mid = (l + r) // 2
                left = node << 1
                right = left | 1
                build(left, l, mid)
                build(right, mid + 1, r)
                self._pull(node, left, right, k, prod, freq)

        def update(node, l, r, idx, val):
            if l == r:
                # reset
                f = freq[node]
                for i in range(k):
                    f[i] = 0
                v = val % k
                prod[node] = v
                f[v] = 1
            else:
                mid = (l + r) // 2
                left = node << 1
                right = left | 1
                if idx <= mid:
                    update(left, l, mid, idx, val)
                else:
                    update(right, mid + 1, r, idx, val)
                self._pull(node, left, right, k, prod, freq)

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return freq[node], prod[node]
            if r < ql or l > qr:
                return None
            mid = (l + r) // 2
            left_res = query(node << 1, l, mid, ql, qr)
            right_res = query((node << 1) | 1, mid + 1, r, ql, qr)
            if left_res is None:
                return right_res
            if right_res is None:
                return left_res
            fL, pL = left_res
            fR, pR = right_res
            # combine
            new_f = [0] * k
            for i in range(k):
                new_f[i] = fL[i]
            for r_rem in range(k):
                if fR[r_rem]:
                    new_idx = (pL * r_rem) % k
                    new_f[new_idx] += fR[r_rem]
            new_p = (pL * pR) % k
            return new_f, new_p

        # helper to merge children into parent
        def pull(node, left, right):
            fL = freq[left]
            fR = freq[right]
            pL = prod[left]
            pR = prod[right]
            fP = freq[node]
            for i in range(k):
                fP[i] = fL[i]
            for r_rem in range(k):
                if fR[r_rem]:
                    new_idx = (pL * r_rem) % k
                    fP[new_idx] += fR[r_rem]
            prod[node] = (pL * pR) % k

        # bind pull to self for reuse
        self._pull = lambda node, left, right, k=k, prod=prod, freq=freq: (
            (lambda: (
                [freq[node].__setitem__(i, freq[left][i]) for i in range(k)],
                None,
                [(freq[node].__setitem__((prod[left] * r) % k, freq[node][(prod[left] * r) % k] + freq[right][r])) for r in range(k) if freq[right][r]],
                prod.__setitem__(node, (prod[left] * prod[right]) % k)
            ))()
        )
        # Actually use explicit pull defined above
        self._pull = lambda node, left, right, k=k, prod=prod, freq=freq: pull(node, left, right)

        build(1, 0, n - 1)

        res = []
        for idx, val, start, xi in queries:
            update(1, 0, n - 1, idx, val)
            f, _ = query(1, 0, n - 1, start, n - 1)
            res.append(f[xi])
        return res
```

## Python3

```python
class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 4 * n
        prod = [0] * size
        cnt = [[0] * k for _ in range(size)]

        def merge(lp, lc, rp, rc):
            new_cnt = [0] * k
            for i in range(k):
                new_cnt[i] += lc[i]
            for r in range(k):
                c = rc[r]
                if c:
                    nr = (lp * r) % k
                    new_cnt[nr] += c
            return (lp * rp) % k, new_cnt

        def build(node, l, r):
            if l == r:
                val = nums[l] % k
                prod[node] = val
                cnt[node][val] = 1
                return
            m = (l + r) // 2
            build(node * 2, l, m)
            build(node * 2 + 1, m + 1, r)
            prod[node], cnt[node] = merge(prod[node * 2], cnt[node * 2],
                                          prod[node * 2 + 1], cnt[node * 2 + 1])

        def update(node, l, r, idx, val_mod):
            if l == r:
                prod[node] = val_mod
                c = [0] * k
                c[val_mod] = 1
                cnt[node] = c
                return
            m = (l + r) // 2
            if idx <= m:
                update(node * 2, l, m, idx, val_mod)
            else:
                update(node * 2 + 1, m + 1, r, idx, val_mod)
            prod[node], cnt[node] = merge(prod[node * 2], cnt[node * 2],
                                          prod[node * 2 + 1], cnt[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return prod[node], cnt[node][:]
            if r < ql or l > qr:
                return (1 % k), [0] * k
            m = (l + r) // 2
            lp, lc = query(node * 2, l, m, ql, qr)
            rp, rc = query(node * 2 + 1, m + 1, r, ql, qr)
            return merge(lp, lc, rp, rc)

        build(1, 0, n - 1)
        ans = []
        for index, value, start, xi in queries:
            update(1, 0, n - 1, index, value % k)
            _, c = query(1, 0, n - 1, start, n - 1)
            ans.append(c[xi])
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int cnt[5];
    int prod;
} Node;

static Node *segTree;
static int N;
static int K;

/* Merge two nodes: left segment followed by right segment */
static Node mergeNode(Node left, Node right) {
    Node res;
    for (int i = 0; i < K; ++i) res.cnt[i] = left.cnt[i];
    int prodA = left.prod % K;
    for (int r = 0; r < K; ++r) {
        int target = (prodA * r) % K;
        res.cnt[target] += right.cnt[r];
    }
    res.prod = (left.prod * right.prod) % K;
    return res;
}

/* Build segment tree */
static void build(int idx, int l, int r, const int *arr) {
    if (l == r) {
        for (int i = 0; i < K; ++i) segTree[idx].cnt[i] = 0;
        int modv = arr[l] % K;
        segTree[idx].cnt[modv] = 1;
        segTree[idx].prod = modv;
        return;
    }
    int mid = (l + r) >> 1;
    build(idx << 1, l, mid, arr);
    build(idx << 1 | 1, mid + 1, r, arr);
    segTree[idx] = mergeNode(segTree[idx << 1], segTree[idx << 1 | 1]);
}

/* Point update */
static void update(int idx, int l, int r, int pos, int val) {
    if (l == r) {
        for (int i = 0; i < K; ++i) segTree[idx].cnt[i] = 0;
        int modv = val % K;
        segTree[idx].cnt[modv] = 1;
        segTree[idx].prod = modv;
        return;
    }
    int mid = (l + r) >> 1;
    if (pos <= mid) update(idx << 1, l, mid, pos, val);
    else update(idx << 1 | 1, mid + 1, r, pos, val);
    segTree[idx] = mergeNode(segTree[idx << 1], segTree[idx << 1 | 1]);
}

/* Query over [ql, qr] */
static Node query(int idx, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) {
        Node empty;
        for (int i = 0; i < K; ++i) empty.cnt[i] = 0;
        empty.prod = (K == 1 ? 0 : 1 % K);   // identity product
        return empty;
    }
    if (ql <= l && r <= qr) {
        return segTree[idx];
    }
    int mid = (l + r) >> 1;
    Node leftRes = query(idx << 1, l, mid, ql, qr);
    Node rightRes = query(idx << 1 | 1, mid + 1, r, ql, qr);
    return mergeNode(leftRes, rightRes);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultArray(int* nums, int numsSize, int k, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    K = k;
    N = numsSize;
    segTree = (Node *)malloc(sizeof(Node) * 4 * N);
    build(1, 0, N - 1, nums);

    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        int index = queries[i][0];
        int value = queries[i][1];
        int start = queries[i][2];
        int xi    = queries[i][3];

        update(1, 0, N - 1, index, value);
        Node res = query(1, 0, N - 1, start, N - 1);
        ans[i] = res.cnt[xi];
    }

    *returnSize = queriesSize;
    free(segTree);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    private int _k;
    private int _n;
    private int[] _prodTree;
    private int[,] _cntTree; // [node, remainder]

    public int[] ResultArray(int[] nums, int k, int[][] queries)
    {
        _k = k;
        _n = nums.Length;
        _prodTree = new int[4 * _n];
        _cntTree = new int[4 * _n, 5]; // k <= 5

        Build(1, 0, _n - 1, nums);

        int q = queries.Length;
        int[] answer = new int[q];

        for (int i = 0; i < q; i++)
        {
            int index = queries[i][0];
            int value = queries[i][1];
            int start = queries[i][2];
            int xi = queries[i][3];

            Update(1, 0, _n - 1, index, value % _k);
            Result res = Query(1, 0, _n - 1, start, _n - 1);
            answer[i] = res.Cnt[xi];
        }

        return answer;
    }

    private void Build(int node, int l, int r, int[] arr)
    {
        if (l == r)
        {
            int mod = arr[l] % _k;
            _prodTree[node] = mod;
            for (int i = 0; i < _k; i++) _cntTree[node, i] = 0;
            _cntTree[node, mod] = 1;
            return;
        }

        int mid = (l + r) >> 1;
        Build(node << 1, l, mid, arr);
        Build((node << 1) | 1, mid + 1, r, arr);
        Pull(node);
    }

    private void Update(int node, int l, int r, int pos, int valMod)
    {
        if (l == r)
        {
            _prodTree[node] = valMod;
            for (int i = 0; i < _k; i++) _cntTree[node, i] = 0;
            _cntTree[node, valMod] = 1;
            return;
        }

        int mid = (l + r) >> 1;
        if (pos <= mid)
            Update(node << 1, l, mid, pos, valMod);
        else
            Update((node << 1) | 1, mid + 1, r, pos, valMod);

        Pull(node);
    }

    private void Pull(int node)
    {
        int left = node << 1;
        int right = (node << 1) | 1;

        _prodTree[node] = (_prodTree[left] * _prodTree[right]) % _k;

        for (int i = 0; i < _k; i++) _cntTree[node, i] = _cntTree[left, i];

        int leftProd = _prodTree[left];
        for (int s = 0; s < _k; s++)
        {
            int target = (leftProd * s) % _k;
            _cntTree[node, target] += _cntTree[right, s];
        }
    }

    private struct Result
    {
        public int Prod;
        public int[] Cnt;
    }

    private Result Query(int node, int l, int r, int ql, int qr)
    {
        if (ql <= l && r <= qr)
        {
            var res = new Result { Prod = _prodTree[node], Cnt = new int[5] };
            for (int i = 0; i < _k; i++) res.Cnt[i] = _cntTree[node, i];
            return res;
        }

        int mid = (l + r) >> 1;
        if (qr <= mid)
            return Query(node << 1, l, mid, ql, qr);
        if (ql > mid)
            return Query((node << 1) | 1, mid + 1, r, ql, qr);

        Result leftRes = Query(node << 1, l, mid, ql, qr);
        Result rightRes = Query((node << 1) | 1, mid + 1, r, ql, qr);

        Result combined = new Result { Prod = (leftRes.Prod * rightRes.Prod) % _k, Cnt = new int[5] };
        for (int i = 0; i < _k; i++) combined.Cnt[i] = leftRes.Cnt[i];

        int leftProd = leftRes.Prod;
        for (int s = 0; s < _k; s++)
        {
            int target = (leftProd * s) % _k;
            combined.Cnt[target] += rightRes.Cnt[s];
        }

        return combined;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} queries
 * @return {number[]}
 */
var resultArray = function(nums, k, queries) {
    const n = nums.length;
    const size = 4 * n;
    const cnt = new Array(size);
    const prod = new Array(size);

    // helper to create zero-filled array of length k
    const zeroArr = () => new Array(k).fill(0);

    function build(node, l, r) {
        if (l === r) {
            const v = nums[l] % k;
            const arr = zeroArr();
            arr[v] = 1;
            cnt[node] = arr;
            prod[node] = v;
            return;
        }
        const mid = (l + r) >> 1;
        build(node << 1, l, mid);
        build((node << 1) | 1, mid + 1, r);
        mergeNode(node);
    }

    function mergeNode(node) {
        const left = node << 1;
        const right = (node << 1) | 1;
        const leftCnt = cnt[left];
        const rightCnt = cnt[right];
        const leftProd = prod[left];
        const rightProd = prod[right];

        const curCnt = zeroArr();
        for (let i = 0; i < k; ++i) {
            curCnt[i] = leftCnt[i];
        }
        for (let rRem = 0; rRem < k; ++rRem) {
            const c = rightCnt[rRem];
            if (c !== 0) {
                const t = (leftProd * rRem) % k;
                curCnt[t] += c;
            }
        }
        cnt[node] = curCnt;
        prod[node] = (leftProd * rightProd) % k;
    }

    function update(node, l, r, idx, valMod) {
        if (l === r) {
            const arr = zeroArr();
            arr[valMod] = 1;
            cnt[node] = arr;
            prod[node] = valMod;
            return;
        }
        const mid = (l + r) >> 1;
        if (idx <= mid) update(node << 1, l, mid, idx, valMod);
        else update((node << 1) | 1, mid + 1, r, idx, valMod);
        mergeNode(node);
    }

    function query(node, l, r, ql, qr) {
        if (qr < l || ql > r) return null;
        if (ql <= l && r <= qr) {
            // return a copy to avoid accidental mutation
            return { cnt: cnt[node].slice(), prod: prod[node] };
        }
        const mid = (l + r) >> 1;
        const leftRes = query(node << 1, l, mid, ql, qr);
        const rightRes = query((node << 1) | 1, mid + 1, r, ql, qr);
        if (!leftRes) return rightRes;
        if (!rightRes) return leftRes;

        // merge leftRes then rightRes
        const mergedCnt = zeroArr();
        for (let i = 0; i < k; ++i) {
            mergedCnt[i] = leftRes.cnt[i];
        }
        for (let rRem = 0; rRem < k; ++rRem) {
            const c = rightRes.cnt[rRem];
            if (c !== 0) {
                const t = (leftRes.prod * rRem) % k;
                mergedCnt[t] += c;
            }
        }
        const mergedProd = (leftRes.prod * rightRes.prod) % k;
        return { cnt: mergedCnt, prod: mergedProd };
    }

    build(1, 0, n - 1);
    const ans = [];

    for (const q of queries) {
        const [index, value, start, xi] = q;
        update(1, 0, n - 1, index, value % k);
        const resNode = query(1, 0, n - 1, start, n - 1);
        ans.push(resNode.cnt[xi] || 0);
    }

    return ans;
};
```

## Typescript

```typescript
function resultArray(nums: number[], k: number, queries: number[][]): number[] {
    const n = nums.length;
    class SegTree {
        n: number;
        cnt: number[][]; // each node stores array of size k
        prod: number[];
        constructor(arr: number[]) {
            this.n = arr.length;
            const size = 4 * this.n;
            this.cnt = new Array(size);
            this.prod = new Array(size).fill(0);
            this.build(1, 0, this.n - 1, arr);
        }
        private build(node: number, l: number, r: number, arr: number[]) {
            if (l === r) {
                const mod = ((arr[l] % k) + k) % k;
                const c = new Array(k).fill(0);
                c[mod] = 1;
                this.cnt[node] = c;
                this.prod[node] = mod;
                return;
            }
            const mid = (l + r) >> 1;
            this.build(node << 1, l, mid, arr);
            this.build((node << 1) | 1, mid + 1, r, arr);
            this.pull(node);
        }
        private pull(node: number) {
            const leftCnt = this.cnt[node << 1];
            const rightCnt = this.cnt[(node << 1) | 1];
            const leftProd = this.prod[node << 1];
            const rightProd = this.prod[(node << 1) | 1];
            const merged = new Array(k).fill(0);
            for (let i = 0; i < k; i++) {
                merged[i] += leftCnt[i];
            }
            for (let r = 0; r < k; r++) {
                const cntR = rightCnt[r];
                if (cntR === 0) continue;
                const combined = (leftProd * r) % k;
                merged[combined] += cntR;
            }
            this.cnt[node] = merged;
            this.prod[node] = (leftProd * rightProd) % k;
        }
        update(pos: number, valMod: number) {
            this._update(1, 0, this.n - 1, pos, ((valMod % k) + k) % k);
        }
        private _update(node: number, l: number, r: number, pos: number, modVal: number) {
            if (l === r) {
                const c = new Array(k).fill(0);
                c[modVal] = 1;
                this.cnt[node] = c;
                this.prod[node] = modVal;
                return;
            }
            const mid = (l + r) >> 1;
            if (pos <= mid) this._update(node << 1, l, mid, pos, modVal);
            else this._update((node << 1) | 1, mid + 1, r, pos, modVal);
            this.pull(node);
        }
        query(qL: number, qR: number): { cnt: number[]; prod: number } {
            return this._query(1, 0, this.n - 1, qL, qR);
        }
        private _query(node: number, l: number, r: number, qL: number, qR: number): { cnt: number[]; prod: number } {
            if (qL <= l && r <= qR) {
                // return a copy to avoid accidental mutation
                return { cnt: this.cnt[node].slice(), prod: this.prod[node] };
            }
            const mid = (l + r) >> 1;
            let leftRes: { cnt: number[]; prod: number } | null = null;
            let rightRes: { cnt: number[]; prod: number } | null = null;
            if (qL <= mid) leftRes = this._query(node << 1, l, mid, qL, qR);
            if (qR > mid) rightRes = this._query((node << 1) | 1, mid + 1, r, qL, qR);
            if (!leftRes) return rightRes!;
            if (!rightRes) return leftRes;
            // merge leftRes and rightRes
            const mergedCnt = new Array(k).fill(0);
            for (let i = 0; i < k; i++) {
                mergedCnt[i] += leftRes.cnt[i];
            }
            const leftProd = leftRes.prod;
            for (let rIdx = 0; rIdx < k; rIdx++) {
                const cntR = rightRes.cnt[rIdx];
                if (cntR === 0) continue;
                const combined = (leftProd * rIdx) % k;
                mergedCnt[combined] += cntR;
            }
            const mergedProd = (leftRes.prod * rightRes.prod) % k;
            return { cnt: mergedCnt, prod: mergedProd };
        }
    }

    const seg = new SegTree(nums);
    const ans: number[] = [];
    for (const q of queries) {
        const [index, value, start, xi] = q;
        seg.update(index, value % k);
        const nodeInfo = seg.query(start, n - 1);
        ans.push(nodeInfo.cnt[xi]);
    }
    return ans;
}
```

## Php

```php
class Solution {
    private $k;
    private $n;
    private $treeProd = [];
    private $treeCnt = [];

    private function merge($leftProd, $leftCnt, $rightProd, $rightCnt) {
        $k = $this->k;
        $newProd = ($leftProd * $rightProd) % $k;
        $newCnt = array_fill(0, $k, 0);
        for ($i = 0; $i < $k; $i++) {
            $newCnt[$i] += $leftCnt[$i];
        }
        for ($rb = 0; $rb < $k; $rb++) {
            $c = $rightCnt[$rb];
            if ($c == 0) continue;
            $r = ($leftProd * $rb) % $k;
            $newCnt[$r] += $c;
        }
        return [$newProd, $newCnt];
    }

    private function build($idx, $l, $r, $nums) {
        if ($l == $r) {
            $val = $nums[$l] % $this->k;
            $cnt = array_fill(0, $this->k, 0);
            $cnt[$val] = 1;
            $this->treeProd[$idx] = $val;
            $this->treeCnt[$idx] = $cnt;
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->build($idx * 2, $l, $mid, $nums);
        $this->build($idx * 2 + 1, $mid + 1, $r, $nums);
        [$prod, $cnt] = $this->merge(
            $this->treeProd[$idx * 2], $this->treeCnt[$idx * 2],
            $this->treeProd[$idx * 2 + 1], $this->treeCnt[$idx * 2 + 1]
        );
        $this->treeProd[$idx] = $prod;
        $this->treeCnt[$idx] = $cnt;
    }

    private function update($idx, $l, $r, $pos, $value) {
        if ($l == $r) {
            $val = $value % $this->k;
            $cnt = array_fill(0, $this->k, 0);
            $cnt[$val] = 1;
            $this->treeProd[$idx] = $val;
            $this->treeCnt[$idx] = $cnt;
            return;
        }
        $mid = intdiv($l + $r, 2);
        if ($pos <= $mid) {
            $this->update($idx * 2, $l, $mid, $pos, $value);
        } else {
            $this->update($idx * 2 + 1, $mid + 1, $r, $pos, $value);
        }
        [$prod, $cnt] = $this->merge(
            $this->treeProd[$idx * 2], $this->treeCnt[$idx * 2],
            $this->treeProd[$idx * 2 + 1], $this->treeCnt[$idx * 2 + 1]
        );
        $this->treeProd[$idx] = $prod;
        $this->treeCnt[$idx] = $cnt;
    }

    private function query($idx, $l, $r, $ql, $qr) {
        if ($ql <= $l && $r <= $qr) {
            return [$this->treeProd[$idx], $this->treeCnt[$idx]];
        }
        $mid = intdiv($l + $r, 2);
        if ($qr <= $mid) {
            return $this->query($idx * 2, $l, $mid, $ql, $qr);
        } elseif ($ql > $mid) {
            return $this->query($idx * 2 + 1, $mid + 1, $r, $ql, $qr);
        } else {
            [$prodL, $cntL] = $this->query($idx * 2, $l, $mid, $ql, $qr);
            [$prodR, $cntR] = $this->query($idx * 2 + 1, $mid + 1, $r, $ql, $qr);
            return $this->merge($prodL, $cntL, $prodR, $cntR);
        }
    }

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function resultArray($nums, $k, $queries) {
        $this->k = $k;
        $this->n = count($nums);
        if ($this->n == 0) return [];

        $this->build(1, 0, $this->n - 1, $nums);
        $ans = [];

        foreach ($queries as $q) {
            [$index, $value, $start, $xi] = $q;
            $this->update(1, 0, $this->n - 1, $index, $value);
            if ($start > $this->n - 1) {
                $ans[] = 0;
                continue;
            }
            [$prod, $cnt] = $this->query(1, 0, $this->n - 1, $start, $this->n - 1);
            $ans[] = $cnt[$xi];
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func resultArray(_ nums: [Int], _ k: Int, _ queries: [[Int]]) -> [Int] {
        let K = k
        let n = nums.count
        struct Node {
            var cnt: [Int]
            var prod: Int
        }
        var seg = Array(repeating: Node(cnt: Array(repeating: 0, count: K), prod: 1), count: 4 * n)
        
        func merge(_ left: Node, _ right: Node) -> Node {
            var resCnt = Array(repeating: 0, count: K)
            for i in 0..<K { resCnt[i] += left.cnt[i] }
            let lp = left.prod
            if K > 0 {
                for r in 0..<K {
                    let c = right.cnt[r]
                    if c != 0 {
                        let combined = (lp * r) % K
                        resCnt[combined] += c
                    }
                }
            }
            let prodAll = (left.prod * right.prod) % K
            return Node(cnt: resCnt, prod: prodAll)
        }
        
        func build(_ idx: Int, _ l: Int, _ r: Int) {
            if l == r {
                var cnt = Array(repeating: 0, count: K)
                let rem = nums[l] % K
                cnt[rem] = 1
                seg[idx] = Node(cnt: cnt, prod: rem)
            } else {
                let mid = (l + r) >> 1
                build(idx << 1, l, mid)
                build(idx << 1 | 1, mid + 1, r)
                seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1])
            }
        }
        
        func update(_ idx: Int, _ l: Int, _ r: Int, _ pos: Int, _ val: Int) {
            if l == r {
                var cnt = Array(repeating: 0, count: K)
                let rem = val % K
                cnt[rem] = 1
                seg[idx] = Node(cnt: cnt, prod: rem)
            } else {
                let mid = (l + r) >> 1
                if pos <= mid {
                    update(idx << 1, l, mid, pos, val)
                } else {
                    update(idx << 1 | 1, mid + 1, r, pos, val)
                }
                seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1])
            }
        }
        
        func query(_ idx: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Node {
            if ql <= l && r <= qr {
                return seg[idx]
            }
            let mid = (l + r) >> 1
            var leftNode = Node(cnt: Array(repeating: 0, count: K), prod: 1)
            var rightNode = Node(cnt: Array(repeating: 0, count: K), prod: 1)
            if ql <= mid {
                leftNode = query(idx << 1, l, mid, ql, qr)
            }
            if qr > mid {
                rightNode = query(idx << 1 | 1, mid + 1, r, ql, qr)
            }
            return merge(leftNode, rightNode)
        }
        
        build(1, 0, n - 1)
        var answer: [Int] = []
        for q in queries {
            let index = q[0]
            let value = q[1]
            let start = q[2]
            let xi = q[3] % K
            update(1, 0, n - 1, index, value)
            let node = query(1, 0, n - 1, start, n - 1)
            answer.append(node.cnt[xi])
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun resultArray(nums: IntArray, k: Int, queries: Array<IntArray>): IntArray {
        val n = nums.size
        val segCnt = Array(4 * n) { IntArray(k) }
        val segTot = IntArray(4 * n)

        fun build(idx: Int, l: Int, r: Int) {
            if (l == r) {
                val rem = ((nums[l] % k) + k) % k
                segCnt[idx][rem] = 1
                segTot[idx] = rem
                return
            }
            val mid = (l + r) / 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            pull(idx)
        }

        fun pull(idx: Int) {
            val left = idx * 2
            val right = left + 1
            for (i in 0 until k) segCnt[idx][i] = segCnt[left][i]
            val leftTot = segTot[left]
            for (r in 0 until k) {
                val c = segCnt[right][r]
                if (c != 0) {
                    val nr = (leftTot * r) % k
                    segCnt[idx][nr] += c
                }
            }
            segTot[idx] = (segTot[left] * segTot[right]) % k
        }

        fun update(idx: Int, l: Int, r: Int, pos: Int, value: Int) {
            if (l == r) {
                for (i in 0 until k) segCnt[idx][i] = 0
                val rem = ((value % k) + k) % k
                segCnt[idx][rem] = 1
                segTot[idx] = rem
                return
            }
            val mid = (l + r) / 2
            if (pos <= mid) update(idx * 2, l, mid, pos, value)
            else update(idx * 2 + 1, mid + 1, r, pos, value)
            pull(idx)
        }

        data class Node(val cnt: IntArray, val tot: Int)

        fun mergeNode(a: Node, b: Node): Node {
            val newCnt = IntArray(k)
            for (i in 0 until k) newCnt[i] = a.cnt[i]
            val leftTot = a.tot
            for (r in 0 until k) {
                val c = b.cnt[r]
                if (c != 0) {
                    val nr = (leftTot * r) % k
                    newCnt[nr] += c
                }
            }
            val newTot = (a.tot * b.tot) % k
            return Node(newCnt, newTot)
        }

        fun query(idx: Int, l: Int, r: Int, ql: Int, qr: Int): Node {
            if (ql <= l && r <= qr) {
                return Node(segCnt[idx].clone(), segTot[idx])
            }
            val mid = (l + r) / 2
            var leftNode: Node? = null
            var rightNode: Node? = null
            if (ql <= mid) leftNode = query(idx * 2, l, mid, ql, qr)
            if (qr > mid) rightNode = query(idx * 2 + 1, mid + 1, r, ql, qr)
            return when {
                leftNode == null -> rightNode!!
                rightNode == null -> leftNode
                else -> mergeNode(leftNode, rightNode)
            }
        }

        build(1, 0, n - 1)

        val m = queries.size
        val ans = IntArray(m)
        for (i in 0 until m) {
            val q = queries[i]
            val index = q[0]
            val value = q[1]
            val start = q[2]
            val xi = q[3]
            update(1, 0, n - 1, index, value)
            val node = query(1, 0, n - 1, start, n - 1)
            ans[i] = node.cnt[xi]
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> resultArray(List<int> nums, int k, List<List<int>> queries) {
    int n = nums.length;
    // segment tree arrays
    List<List<int>> cnts = List.generate(4 * n, (_) => List.filled(k, 0));
    List<int> prods = List.filled(4 * n, 1);

    void pull(int idx) {
      List<int> leftCnt = cnts[idx << 1];
      List<int> rightCnt = cnts[(idx << 1) | 1];
      int leftProd = prods[idx << 1];
      int rightProd = prods[(idx << 1) | 1];
      List<int> cur = List.filled(k, 0);
      for (int i = 0; i < k; ++i) {
        cur[i] += leftCnt[i];
      }
      for (int i = 0; i < k; ++i) {
        int shifted = (leftProd * i) % k;
        cur[shifted] += rightCnt[i];
      }
      cnts[idx] = cur;
      prods[idx] = (leftProd * rightProd) % k;
    }

    void build(int idx, int l, int r) {
      if (l == r) {
        int mod = nums[l] % k;
        List<int> arr = List.filled(k, 0);
        arr[mod] = 1;
        cnts[idx] = arr;
        prods[idx] = mod;
        return;
      }
      int mid = (l + r) >> 1;
      build(idx << 1, l, mid);
      build((idx << 1) | 1, mid + 1, r);
      pull(idx);
    }

    void update(int idx, int l, int r, int pos, int valMod) {
      if (l == r) {
        List<int> arr = List.filled(k, 0);
        arr[valMod] = 1;
        cnts[idx] = arr;
        prods[idx] = valMod;
        return;
      }
      int mid = (l + r) >> 1;
      if (pos <= mid) {
        update(idx << 1, l, mid, pos, valMod);
      } else {
        update((idx << 1) | 1, mid + 1, r, pos, valMod);
      }
      pull(idx);
    }

    class SegNode {
      List<int> cnt;
      int prod;
      SegNode(this.cnt, this.prod);
    }

    SegNode query(int idx, int l, int r, int ql, int qr) {
      if (ql <= l && r <= qr) {
        return SegNode(List<int>.from(cnts[idx]), prods[idx]);
      }
      int mid = (l + r) >> 1;
      if (qr <= mid) {
        return query(idx << 1, l, mid, ql, qr);
      } else if (ql > mid) {
        return query((idx << 1) | 1, mid + 1, r, ql, qr);
      } else {
        SegNode left = query(idx << 1, l, mid, ql, qr);
        SegNode right = query((idx << 1) | 1, mid + 1, r, ql, qr);
        List<int> cur = List.filled(k, 0);
        for (int i = 0; i < k; ++i) {
          cur[i] += left.cnt[i];
        }
        int leftProd = left.prod;
        for (int i = 0; i < k; ++i) {
          int shifted = (leftProd * i) % k;
          cur[shifted] += right.cnt[i];
        }
        int prod = (left.prod * right.prod) % k;
        return SegNode(cur, prod);
      }
    }

    build(1, 0, n - 1);
    List<int> ans = [];
    for (var q in queries) {
      int index = q[0];
      int value = q[1];
      int start = q[2];
      int xi = q[3];
      update(1, 0, n - 1, index, value % k);
      SegNode res = query(1, 0, n - 1, start, n - 1);
      ans.add(res.cnt[xi]);
    }
    return ans;
  }
}
```

## Golang

```go
package main

func resultArray(nums []int, k int, queries [][]int) []int {
	n := len(nums)
	seg := make([]Node, 4*n)

	var build func(idx, l, r int)
	build = func(idx, l, r int) {
		if l == r {
			val := nums[l] % k
			seg[idx].prod = val
			for i := 0; i < k; i++ {
				seg[idx].cnt[i] = 0
			}
			seg[idx].cnt[val] = 1
			return
		}
		mid := (l + r) >> 1
		build(idx<<1, l, mid)
		build(idx<<1|1, mid+1, r)
		seg[idx] = merge(seg[idx<<1], seg[idx<<1|1])
	}
	build(1, 0, n-1)

	var update func(idx, l, r, pos, value int)
	update = func(idx, l, r, pos, value int) {
		if l == r {
			val := value % k
			seg[idx].prod = val
			for i := 0; i < k; i++ {
				seg[idx].cnt[i] = 0
			}
			seg[idx].cnt[val] = 1
			return
		}
		mid := (l + r) >> 1
		if pos <= mid {
			update(idx<<1, l, mid, pos, value)
		} else {
			update(idx<<1|1, mid+1, r, pos, value)
		}
		seg[idx] = merge(seg[idx<<1], seg[idx<<1|1])
	}

	var query func(idx, l, r, ql, qr int) Node
	query = func(idx, l, r, ql, qr int) Node {
		if ql <= l && r <= qr {
			return seg[idx]
		}
		mid := (l + r) >> 1
		if qr <= mid {
			return query(idx<<1, l, mid, ql, qr)
		}
		if ql > mid {
			return query(idx<<1|1, mid+1, r, ql, qr)
		}
		left := query(idx<<1, l, mid, ql, qr)
		right := query(idx<<1|1, mid+1, r, ql, qr)
		return merge(left, right)
	}

	ans := make([]int, len(queries))
	for i, q := range queries {
		idx, val, start, xi := q[0], q[1], q[2], q[3]
		update(1, 0, n-1, idx, val)
		node := query(1, 0, n-1, start, n-1)
		ans[i] = node.cnt[xi]
	}
	return ans
}

type Node struct {
	cnt  [5]int
	prod int
}

func merge(a, b Node) Node {
	var res Node
	// copy left counts
	for i := 0; i < kGlobal; i++ {
		res.cnt[i] = a.cnt[i]
	}
	// shift right counts by left product
	for s := 0; s < kGlobal; s++ {
		if b.cnt[s] == 0 {
			continue
		}
		shifted := (a.prod * s) % kGlobal
		res.cnt[shifted] += b.cnt[s]
	}
	res.prod = (a.prod * b.prod) % kGlobal
	return res
}

// global variable for k to be used in merge
var kGlobal int

func init() {
	// placeholder; actual value will be set before first use.
	kGlobal = 1
}
```

## Ruby

```ruby
def result_array(nums, k, queries)
  class SegTree
    def initialize(arr, mod)
      @mod = mod
      @n = arr.size
      @size = 1
      @size <<= 1 while @size < @n
      @prod = Array.new(@size * 2, 1 % @mod)
      @cnt = Array.new(@size * 2) { Array.new(@mod, 0) }
      build(arr)
    end

    def build(arr)
      (0...@n).each do |i|
        idx = i + @size
        v = arr[i] % @mod
        @prod[idx] = v
        c = Array.new(@mod, 0)
        c[v] = 1
        @cnt[idx] = c
      end
      (@size - 1).downto(1) { |i| merge_children(i) }
    end

    def merge_children(i)
      l = i * 2
      r = l + 1
      a_prod = @prod[l]
      b_prod = @prod[r]
      prod = (a_prod * b_prod) % @mod
      cnt = Array.new(@mod, 0)
      0.upto(@mod - 1) { |x| cnt[x] = @cnt[l][x] }
      0.upto(@mod - 1) do |x|
        t = (a_prod * x) % @mod
        cnt[t] += @cnt[r][x]
      end
      @prod[i] = prod
      @cnt[i] = cnt
    end

    def update(pos, value)
      idx = pos + @size
      v = value % @mod
      @prod[idx] = v
      c = Array.new(@mod, 0)
      c[v] = 1
      @cnt[idx] = c
      idx >>= 1
      while idx >= 1
        merge_children(idx)
        idx >>= 1
      end
    end

    def query(l, r)
      l += @size
      r += @size
      left_node = nil
      right_node = nil
      while l <= r
        if (l & 1) == 1
          left_node = combine(left_node, node_at(l))
          l += 1
        end
        if (r & 1) == 0
          right_node = combine(node_at(r), right_node)
          r -= 1
        end
        l >>= 1
        r >>= 1
      end
      combine(left_node, right_node)
    end

    def node_at(idx)
      { prod: @prod[idx], cnt: @cnt[idx] }
    end

    def combine(a, b)
      return b if a.nil?
      return a if b.nil?
      prod = (a[:prod] * b[:prod]) % @mod
      cnt = Array.new(@mod, 0)
      0.upto(@mod - 1) { |x| cnt[x] = a[:cnt][x] }
      0.upto(@mod - 1) do |x|
        t = (a[:prod] * x) % @mod
        cnt[t] += b[:cnt][x]
      end
      { prod: prod, cnt: cnt }
    end
  end

  st = SegTree.new(nums, k)
  n = nums.length
  ans = []
  queries.each do |idx, val, starti, xi|
    st.update(idx, val)
    node = st.query(starti, n - 1)
    ans << node[:cnt][xi]
  end
  ans
end
```

## Scala

```scala
object Solution {
    def resultArray(nums: Array[Int], k: Int, queries: Array[Array[Int]]): Array[Int] = {
        val n = nums.length
        val size = 4 * n
        val prodTree = new Array[Int](size)
        val cntTree = Array.ofDim[Int](size, k)

        def build(node: Int, l: Int, r: Int): Unit = {
            if (l == r) {
                val p = ((nums(l) % k) + k) % k
                prodTree(node) = p
                java.util.Arrays.fill(cntTree(node), 0)
                cntTree(node)(p) = 1
            } else {
                val mid = (l + r) >>> 1
                build(node * 2, l, mid)
                build(node * 2 + 1, mid + 1, r)
                pull(node)
            }
        }

        def pull(node: Int): Unit = {
            val left = node * 2
            val right = node * 2 + 1
            val prodL = prodTree(left)
            val prodR = prodTree(right)
            prodTree(node) = (prodL * prodR) % k
            java.util.Arrays.fill(cntTree(node), 0)
            var i = 0
            while (i < k) {
                cntTree(node)(i) = cntTree(left)(i)
                i += 1
            }
            i = 0
            while (i < k) {
                val c = cntTree(right)(i)
                if (c != 0) {
                    val x = (prodL * i) % k
                    cntTree(node)(x) += c
                }
                i += 1
            }
        }

        def update(node: Int, l: Int, r: Int, idx: Int, value: Int): Unit = {
            if (l == r) {
                val p = ((value % k) + k) % k
                prodTree(node) = p
                java.util.Arrays.fill(cntTree(node), 0)
                cntTree(node)(p) = 1
            } else {
                val mid = (l + r) >>> 1
                if (idx <= mid) update(node * 2, l, mid, idx, value)
                else update(node * 2 + 1, mid + 1, r, idx, value)
                pull(node)
            }
        }

        case class Res(cnt: Array[Int], prod: Int)

        def combine(a: Res, b: Res): Res = {
            if (a == null) return b
            if (b == null) return a
            val newProd = (a.prod * b.prod) % k
            val newCnt = new Array[Int](k)
            var i = 0
            while (i < k) {
                newCnt(i) = a.cnt(i)
                i += 1
            }
            i = 0
            while (i < k) {
                val c = b.cnt(i)
                if (c != 0) {
                    val x = (a.prod * i) % k
                    newCnt(x) += c
                }
                i += 1
            }
            Res(newCnt, newProd)
        }

        def query(node: Int, l: Int, r: Int, ql: Int, qr: Int): Res = {
            if (ql <= l && r <= qr) {
                Res(cntTree(node).clone(), prodTree(node))
            } else {
                val mid = (l + r) >>> 1
                var leftRes: Res = null
                var rightRes: Res = null
                if (ql <= mid) leftRes = query(node * 2, l, mid, ql, qr)
                if (qr > mid) rightRes = query(node * 2 + 1, mid + 1, r, ql, qr)
                combine(leftRes, rightRes)
            }
        }

        build(1, 0, n - 1)

        val ans = new Array[Int](queries.length)
        var qi = 0
        while (qi < queries.length) {
            val q = queries(qi)
            val idx = q(0)
            val value = q(1)
            val start = q(2)
            val xi = q(3)
            update(1, 0, n - 1, idx, value)
            val res = query(1, 0, n - 1, start, n - 1)
            ans(qi) = if (xi < k) res.cnt(xi) else 0
            qi += 1
        }
        ans
    }
}
```

## Rust

```rust
use std::cmp::{max, min};

#[derive(Copy, Clone)]
struct Node {
    prod: usize,
    cnt: [i32; 5],
}

impl Node {
    fn identity(k: usize) -> Self {
        let mut cnt = [0i32; 5];
        Node { prod: 1 % k, cnt }
    }

    fn from_value(val: i32, k: usize) -> Self {
        let mut cnt = [0i32; 5];
        let v = ((val % k as i32 + k as i32) % k as i32) as usize;
        cnt[v] = 1;
        Node { prod: v, cnt }
    }

    fn merge(a: &Self, b: &Self, k: usize) -> Self {
        let mut res_cnt = [0i32; 5];
        for r in 0..k {
            res_cnt[r] += a.cnt[r];
        }
        let left_prod = a.prod % k;
        for t in 0..k {
            let shifted = (left_prod * t) % k;
            res_cnt[shifted] += b.cnt[t];
        }
        let prod = (a.prod * b.prod) % k;
        Node { prod, cnt: res_cnt }
    }
}

struct SegTree {
    n: usize,
    k: usize,
    tree: Vec<Node>,
}

impl SegTree {
    fn new(arr: &Vec<i32>, k: usize) -> Self {
        let n = arr.len();
        let mut seg = SegTree {
            n,
            k,
            tree: vec![Node::identity(k); 4 * n],
        };
        if n > 0 {
            seg.build(1, 0, n - 1, arr);
        }
        seg
    }

    fn build(&mut self, idx: usize, l: usize, r: usize, arr: &Vec<i32>) {
        if l == r {
            self.tree[idx] = Node::from_value(arr[l], self.k);
            return;
        }
        let mid = (l + r) / 2;
        self.build(idx * 2, l, mid, arr);
        self.build(idx * 2 + 1, mid + 1, r, arr);
        self.pull(idx);
    }

    fn pull(&mut self, idx: usize) {
        let left = self.tree[idx * 2];
        let right = self.tree[idx * 2 + 1];
        self.tree[idx] = Node::merge(&left, &right, self.k);
    }

    fn update(&mut self, pos: usize, val: i32) {
        self.update_rec(1, 0, self.n - 1, pos, val);
    }

    fn update_rec(&mut self, idx: usize, l: usize, r: usize, pos: usize, val: i32) {
        if l == r {
            self.tree[idx] = Node::from_value(val, self.k);
            return;
        }
        let mid = (l + r) / 2;
        if pos <= mid {
            self.update_rec(idx * 2, l, mid, pos, val);
        } else {
            self.update_rec(idx * 2 + 1, mid + 1, r, pos, val);
        }
        self.pull(idx);
    }

    fn query(&self, ql: usize, qr: usize) -> Node {
        self.query_rec(1, 0, self.n - 1, ql, qr)
    }

    fn query_rec(&self, idx: usize, l: usize, r: usize, ql: usize, qr: usize) -> Node {
        if ql <= l && r <= qr {
            return self.tree[idx];
        }
        if r < ql || l > qr {
            return Node::identity(self.k);
        }
        let mid = (l + r) / 2;
        let left = self.query_rec(idx * 2, l, mid, ql, qr);
        let right = self.query_rec(idx * 2 + 1, mid + 1, r, ql, qr);
        Node::merge(&left, &right, self.k)
    }
}

impl Solution {
    pub fn result_array(nums: Vec<i32>, k: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let k_usize = k as usize;
        let mut seg = SegTree::new(&nums, k_usize);
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let idx = q[0] as usize;
            let val = q[1];
            let start = q[2] as usize;
            let xi = q[3] as usize;

            seg.update(idx, val);
            let l = if start == 0 { 0 } else { start - 1 };
            let node = seg.query(l, n - 1);
            ans.push(node.cnt[xi]);
        }
        ans
    }
}
```

## Racket

```racket
(define (result-array nums k queries)
  (let* ((n (length nums))
         (size (* 4 n))
         (tree (make-vector size #f))
         
         ;; helper to create a node: [cnt-vector prod]
         (make-node
          (lambda (cnt prod) (vector cnt prod)))
         
         ;; identity node for empty segment
         (identity-node
          (let ((cnt (make-vector k 0))
                (prod (modulo 1 k))) ; multiplicative identity modulo k
            (make-node cnt prod)))
         
         ;; merge two nodes
         (merge-nodes
          (lambda (left right)
            (if (eq? left #f) right
                (if (eq? right #f) left
                    (let* ((cntL (vector-ref left 0))
                           (prodL (vector-ref left 1))
                           (cntR (vector-ref right 0))
                           (prodR (vector-ref right 1))
                           (new-cnt (make-vector k 0)))
                      ;; prefixes entirely in left
                      (for ([i (in-range k)])
                        (vector-set! new-cnt i (+ (vector-ref new-cnt i)
                                                  (vector-ref cntL i))))
                      ;; prefixes that extend into right
                      (for ([b (in-range k)])
                        (let* ((c (vector-ref cntR b))
                               (t (modulo (* prodL b) k)))
                          (when (> c 0)
                            (vector-set! new-cnt t (+ (vector-ref new-cnt t) c)))))
                      (make-node new-cnt (modulo (* prodL prodR) k))))))))
         
         ;; build segment tree
         (build
          (lambda (idx l r)
            (if (= l r)
                (let* ((val (modulo (list-ref nums l) k))
                       (cnt (make-vector k 0)))
                  (vector-set! cnt val 1)
                  (vector-set! tree idx (make-node cnt val)))
                (let ((mid (quotient (+ l r) 2)))
                  (build (* idx 2) l mid)
                  (build (+ (* idx 2) 1) (+ mid 1) r)
                  (vector-set! tree idx
                               (merge-nodes (vector-ref tree (* idx 2))
                                            (vector-ref tree (+ (* idx 2) 1))))))))
         
         ;; point update
         (update
          (lambda (idx l r pos newval)
            (if (= l r)
                (let* ((val (modulo newval k))
                       (cnt (make-vector k 0)))
                  (vector-set! cnt val 1)
                  (vector-set! tree idx (make-node cnt val)))
                (let ((mid (quotient (+ l r) 2)))
                  (if (<= pos mid)
                      (update (* idx 2) l mid pos newval)
                      (update (+ (* idx 2) 1) (+ mid 1) r pos newval))
                  (vector-set! tree idx
                               (merge-nodes (vector-ref tree (* idx 2))
                                            (vector-ref tree (+ (* idx 2) 1))))))))
         
         ;; range query [ql,qr]
         (query
          (lambda (idx l r ql qr)
            (cond [(> ql r) identity-node]
                  [(< qr l) identity-node]
                  [(and (<= ql l) (>= qr r)) (vector-ref tree idx)]
                  [else (let ((mid (quotient (+ l r) 2)))
                          (merge-nodes
                           (query (* idx 2) l mid ql qr)
                           (query (+ (* idx 2) 1) (+ mid 1) r ql qr)))]))))
    
    ;; build initial tree
    (build 1 0 (- n 1))
    
    ;; process queries, collect answers
    (let loop ((qs queries) (ans '()))
      (if (null? qs)
          (reverse ans)
          (let* ((q (car qs))
                 (index (list-ref q 0))
                 (value (list-ref q 1))
                 (start (list-ref q 2))
                 (xi    (list-ref q 3)))
            (update 1 0 (- n 1) index value)
            (let* ((node (query 1 0 (- n 1) start (- n 1)))
                   (cnt  (vector-ref node 0))
                   (res  (vector-ref cnt xi)))
              (loop (cdr qs) (cons res ans))))))))
```

## Erlang

```erlang
-spec result_array(Nums :: [integer()], K :: integer(), Queries :: [[integer()]]) -> [integer()].
result_array(Nums, K, Queries) ->
    {Tree, N} = build(Nums, K),
    process_queries(Tree, N, K, Queries).

%% Build segment tree
build(Nums, K) ->
    N = length(Nums),
    Tree0 = maps:new(),
    {Tree, _Node} = build_rec(1, 0, N - 1, Nums, K, Tree0),
    {Tree, N}.

build_rec(NodeIdx, L, R, Nums, K, Acc) when L == R ->
    Val = lists:nth(L + 1, Nums),
    Rem = Val rem K,
    Cnt = make_cnt(K, Rem),
    Node = #{cnt => Cnt, tot => Rem},
    {maps:put(NodeIdx, Node, Acc), Node};
build_rec(NodeIdx, L, R, Nums, K, Acc) ->
    Mid = (L + R) div 2,
    {Acc1, _} = build_rec(2 * NodeIdx, L, Mid, Nums, K, Acc),
    {Acc2, _} = build_rec(2 * NodeIdx + 1, Mid + 1, R, Nums, K, Acc1),
    LeftNode = maps:get(2 * NodeIdx, Acc2),
    RightNode = maps:get(2 * NodeIdx + 1, Acc2),
    Merged = merge_nodes(LeftNode, RightNode, K),
    {maps:put(NodeIdx, Merged, Acc2), Merged}.

%% Update a position
update(Tree, N, Idx, Val, K) ->
    update_rec(Tree, 1, 0, N - 1, Idx, Val, K).

update_rec(Map, NodeIdx, L, R, Idx, Val, K) when L == R ->
    Rem = Val rem K,
    Cnt = make_cnt(K, Rem),
    NewNode = #{cnt => Cnt, tot => Rem},
    maps:put(NodeIdx, NewNode, Map);
update_rec(Map, NodeIdx, L, R, Idx, Val, K) ->
    Mid = (L + R) div 2,
    Map1 =
        if Idx =< Mid ->
                update_rec(Map, 2 * NodeIdx, L, Mid, Idx, Val, K);
           true -> Map
        end,
    Map2 =
        if Idx > Mid ->
                update_rec(Map1, 2 * NodeIdx + 1, Mid + 1, R, Idx, Val, K);
           true -> Map1
        end,
    LeftNode = maps:get(2 * NodeIdx, Map2),
    RightNode = maps:get(2 * NodeIdx + 1, Map2),
    Merged = merge_nodes(LeftNode, RightNode, K),
    maps:put(NodeIdx, Merged, Map2).

%% Query range [QL, QR]
query(Tree, N, K, QL, QR) ->
    query_rec(Tree, 1, 0, N - 1, QL, QR, K).

query_rec(Map, NodeIdx, L, R, QL, QR, K) ->
    if QR < L orelse QL > R ->
            empty_node(K);
       QL =< L andalso R =< QR ->
            maps:get(NodeIdx, Map);
       true ->
            Mid = (L + R) div 2,
            LeftNode = query_rec(Map, 2 * NodeIdx, L, Mid, QL, QR, K),
            RightNode = query_rec(Map, 2 * NodeIdx + 1, Mid + 1, R, QL, QR, K),
            merge_nodes(LeftNode, RightNode, K)
    end.

%% Process all queries sequentially
process_queries(_Tree, _N, _K, []) -> [];
process_queries(Tree, N, K, [Q | Rest]) ->
    [Idx, Val, Start, Xi] = Q,
    NewTree = update(Tree, N, Idx, Val, K),
    Node = query(NewTree, N, K, Start, N - 1),
    CntList = maps:get(cnt, Node),
    Answer = lists:nth(Xi + 1, CntList),
    [Answer | process_queries(NewTree, N, K, Rest)].

%% Merge two segment nodes
merge_nodes(NodeA, NodeB, K) ->
    TotA = maps:get(tot, NodeA),
    TotB = maps:get(tot, NodeB),
    CntA = maps:get(cnt, NodeA),
    CntB = maps:get(cnt, NodeB),
    NewTot = (TotA * TotB) rem K,
    Base = CntA,
    MergedCnt = merge_cnts(Base, CntB, TotA, K),
    #{cnt => MergedCnt, tot => NewTot}.

merge_cnts(CntAcc, [], _ProdA, _K) -> CntAcc;
merge_cnts(CntAcc, [C | Rest], ProdA, K) ->
    Index = length(CntAcc) - length(Rest) - 1,
    case C of
        0 -> merge_cnts(CntAcc, Rest, ProdA, K);
        _ ->
            NewRem = (ProdA * Index) rem K,
            Updated = update_cnt(CntAcc, NewRem, C),
            merge_cnts(Updated, Rest, ProdA, K)
    end.

update_cnt(List, Index, Add) ->
    {Left, [Old | Right]} = lists:split(Index, List),
    NewVal = Old + Add,
    Left ++ [NewVal] ++ Right.

%% Helper to create count list with 1 at Rem
make_cnt(K, Rem) -> make_cnt(0, K, Rem, []).

make_cnt(I, K, _Rem, Acc) when I == K ->
    lists:reverse(Acc);
make_cnt(I, K, Rem, Acc) ->
    Val = if I == Rem -> 1; true -> 0 end,
    make_cnt(I + 1, K, Rem, [Val | Acc]).

%% Empty node for out-of-range queries
empty_node(K) -> #{cnt => zero_cnt(K), tot => 1}.

zero_cnt(K) -> zero_cnt(0, K, []).

zero_cnt(I, K, Acc) when I == K ->
    lists:reverse(Acc);
zero_cnt(I, K, Acc) ->
    zero_cnt(I + 1, K, [0 | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec result_array(nums :: [integer], k :: integer, queries :: [[integer]]) :: [integer]
  def result_array(nums, k, queries) do
    n = length(nums)
    tree = build(nums, k)

    {_, answers} =
      Enum.reduce(queries, {tree, []}, fn [index, value, start_idx, xi], {cur_tree, acc} ->
        {updated_tree, _} = update_rec(cur_tree, 1, 0, n - 1, index, value, k)
        node = query_range(updated_tree, 1, 0, n - 1, start_idx, n - 1, k)

        ans =
          if node == nil do
            0
          else
            cnts = elem(node, 0)
            Enum.at(cnts, xi)
          end

        {updated_tree, [ans | acc]}
      end)

    Enum.reverse(answers)
  end

  # Build segment tree
  defp build(nums, k) do
    n = length(nums)
    nums_arr = :array.from_list(nums)
    size = 4 * n
    empty_tree = :array.new(size, nil)
    {tree, _} = build_rec(empty_tree, nums_arr, k, 1, 0, n - 1)
    tree
  end

  defp build_rec(tree, nums_arr, k, idx, l, r) do
    if l == r do
      val = :array.get(l, nums_arr)
      rem = Integer.mod(val, k)

      cnt =
        List.duplicate(0, k)
        |> List.replace_at(rem, 1)

      node = {cnt, rem}
      { :array.set(idx, node, tree), node }
    else
      mid = div(l + r, 2)
      {tree1, left_node} = build_rec(tree, nums_arr, k, idx * 2, l, mid)
      {tree2, right_node} = build_rec(tree1, nums_arr, k, idx * 2 + 1, mid + 1, r)
      node = merge_nodes(left_node, right_node, k)
      { :array.set(idx, node, tree2), node }
    end
  end

  # Point update
  defp update_rec(tree, idx, l, r, pos, val, k) do
    if l == r do
      rem = Integer.mod(val, k)

      cnt =
        List.duplicate(0, k)
        |> List.replace_at(rem, 1)

      node = {cnt, rem}
      { :array.set(idx, node, tree), node }
    else
      mid = div(l + r, 2)

      if pos <= mid do
        {tree1, left_node} = update_rec(tree, idx * 2, l, mid, pos, val, k)
        right_node = :array.get(idx * 2 + 1, tree1)
        node = merge_nodes(left_node, right_node, k)
        { :array.set(idx, node, tree1), node }
      else
        {tree1, right_node} = update_rec(tree, idx * 2 + 1, mid + 1, r, pos, val, k)
        left_node = :array.get(idx * 2, tree1)
        node = merge_nodes(left_node, right_node, k)
        { :array.set(idx, node, tree1), node }
      end
    end
  end

  # Range query returning node for interval [ql, qr]
  defp query_range(tree, idx, l, r, ql, qr, k) do
    cond do
      ql <= l and r <= qr ->
        :array.get(idx, tree)

      r < ql or l > qr ->
        nil

      true ->
        mid = div(l + r, 2)
        left_node = query_range(tree, idx * 2, l, mid, ql, qr, k)
        right_node = query_range(tree, idx * 2 + 1, mid + 1, r, ql, qr, k)

        case {left_node, right_node} do
          {nil, nil} -> nil
          {nil, node_r} -> node_r
          {node_l, nil} -> node_l
          {node_l, node_r} -> merge_nodes(node_l, node_r, k)
        end
    end
  end

  # Merge two nodes (left then right)
  defp merge_nodes({cnt_l, tot_l}, {cnt_r, tot_r}, k) do
    new_tot = Integer.mod(tot_l * tot_r, k)

    # start with left counts
    base_cnt = Enum.map(cnt_l, fn x -> x end)

    merged_cnt =
      0..(k - 1)
      |> Enum.reduce(base_cnt, fn r, acc ->
        cr = Enum.at(cnt_r, r)

        if cr == 0 do
          acc
        else
          new_rem = Integer.mod(tot_l * r, k)
          List.update_at(acc, new_rem, &(&1 + cr))
        end
      end)

    {merged_cnt, new_tot}
  end
end
```

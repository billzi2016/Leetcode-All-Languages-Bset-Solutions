# 2916. Subarrays Distinct Element Sum of Squares II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    static const long long MOD = 1000000007LL;
    struct BIT {
        int n;
        vector<long long> bit;
        BIT(int n=0): n(n), bit(n+2,0) {}
        void add(int idx,long long val){
            for(; idx<=n; idx+=idx&-idx){
                bit[idx] += val;
                if(bit[idx]>=MOD) bit[idx]-=MOD;
                else if(bit[idx]<0) bit[idx]+=MOD;
            }
        }
        long long sumPrefix(int idx) const{
            long long res=0;
            for(; idx>0; idx-=idx&-idx){
                res += bit[idx];
                if(res>=MOD) res-=MOD;
            }
            return res;
        }
    };
public:
    int sumCounts(vector<int>& nums) {
        int n = nums.size();
        int maxVal = 0;
        for(int v:nums) if(v>maxVal) maxVal=v;
        vector<int> last(maxVal+1, -1);
        BIT b1(n), b2(n);
        auto rangeAdd = [&](int l,int r,long long val){
            if(l>r) return;
            int L=l+1, R=r+1;
            long long v = (val%MOD+MOD)%MOD;
            long long vL = v * (L-1) % MOD;
            long long vR = v * R % MOD;
            b1.add(L, v);
            b1.add(R+1, -v);
            b2.add(L, vL);
            b2.add(R+1, -vR);
        };
        auto prefixSumIdx = [&](int idx)->long long{
            int i=idx+1;
            long long s1 = b1.sumPrefix(i);
            long long s2 = b2.sumPrefix(i);
            long long res = (s1*i%MOD - s2) % MOD;
            if(res<0) res+=MOD;
            return res;
        };
        auto rangeSum = [&](int l,int r)->long long{
            if(l>r) return 0LL;
            long long res = prefixSumIdx(r);
            if(l>0){
                res -= prefixSumIdx(l-1);
                if(res<0) res+=MOD;
            }
            return res;
        };
        long long curSq = 0, ans = 0;
        for(int i=0;i<n;++i){
            int x = nums[i];
            int prev = last[x];
            long long addCnt = i - prev; // number of starts where x is absent (including new start)
            long long S = rangeSum(prev+1, i-1); // sum of distinct counts for those previous starts
            curSq = (curSq + 2LL * (S % MOD) + addCnt) % MOD;
            if(addCnt>0){
                rangeAdd(prev+1, i-1, 1);
            }
            rangeAdd(i,i,1); // set count of new subarray [i,i] to 1
            ans += curSq;
            if(ans>=MOD) ans-=MOD;
            last[x]=i;
        }
        return (int)(ans%MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int sumCounts(int[] nums) {
        int n = nums.length;
        // Determine max value for last occurrence array
        int maxVal = 0;
        for (int v : nums) if (v > maxVal) maxVal = v;
        int[] last = new int[maxVal + 1];
        java.util.Arrays.fill(last, -1);

        SegTree seg = new SegTree(n);
        long fPrev = 0; // f(i-1)
        long ans = 0;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int prevIdx = last[x];
            int l = prevIdx + 1;
            int r = i;
            long extra = 0;
            if (l <= r) {
                long sumD = seg.query(l, r);
                long len = r - l + 1L;
                extra = (2L * sumD % MOD + len) % MOD;
                seg.update(l, r, 1); // add 1 to D for this range
            }
            long fCurr = (fPrev + extra) % MOD;
            ans += fCurr;
            if (ans >= MOD) ans -= MOD;
            fPrev = fCurr;
            last[x] = i;
        }
        return (int) ans;
    }

    // Segment tree supporting range add and range sum modulo MOD
    private static class SegTree {
        int n;
        long[] sum;
        long[] lazy;

        SegTree(int size) {
            this.n = size;
            sum = new long[4 * n];
            lazy = new long[4 * n];
        }

        void apply(int node, int l, int r, long val) {
            sum[node] = (sum[node] + val * (r - l + 1)) % MOD;
            lazy[node] = (lazy[node] + val) % MOD;
        }

        void push(int node, int l, int r) {
            if (lazy[node] != 0) {
                int mid = (l + r) >>> 1;
                apply(node << 1, l, mid, lazy[node]);
                apply(node << 1 | 1, mid + 1, r, lazy[node]);
                lazy[node] = 0;
            }
        }

        void update(int ql, int qr, long val) {
            update(1, 0, n - 1, ql, qr, val);
        }

        private void update(int node, int l, int r, int ql, int qr, long val) {
            if (ql <= l && r <= qr) {
                apply(node, l, r, val);
                return;
            }
            push(node, l, r);
            int mid = (l + r) >>> 1;
            if (ql <= mid) update(node << 1, l, mid, ql, qr, val);
            if (qr > mid) update(node << 1 | 1, mid + 1, r, ql, qr, val);
            sum[node] = (sum[node << 1] + sum[node << 1 | 1]) % MOD;
        }

        long query(int ql, int qr) {
            return query(1, 0, n - 1, ql, qr);
        }

        private long query(int node, int l, int r, int ql, int qr) {
            if (ql <= l && r <= qr) {
                return sum[node];
            }
            push(node, l, r);
            int mid = (l + r) >>> 1;
            long res = 0;
            if (ql <= mid) res = (res + query(node << 1, l, mid, ql, qr)) % MOD;
            if (qr > mid) res = (res + query(node << 1 | 1, mid + 1, r, ql, qr)) % MOD;
            return res;
        }
    }
}
```

## Python

```python
class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        sumv = [0] * size          # sum of values in segment
        sumsq = [0] * size         # sum of squares in segment
        lazy = [0] * size

        def apply(node, l, r, v):
            length = r - l + 1
            old_sum = sumv[node]
            sumsq[node] = (sumsq[node] + 2 * v % MOD * old_sum + (v * v % MOD) * length) % MOD
            sumv[node] = (sumv[node] + v * length) % MOD
            lazy[node] = (lazy[node] + v) % MOD

        def push(node, l, r):
            if lazy[node]:
                mid = (l + r) // 2
                left = node * 2
                right = left + 1
                apply(left, l, mid, lazy[node])
                apply(right, mid + 1, r, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                apply(node, l, r, v)
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, v)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, v)
            sumv[node] = (sumv[node * 2] + sumv[node * 2 + 1]) % MOD
            sumsq[node] = (sumsq[node * 2] + sumsq[node * 2 + 1]) % MOD

        last = {}
        ans = 0
        for i, val in enumerate(nums):
            prev = last.get(val, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            ans = (ans + sumsq[1]) % MOD
            last[val] = i
        return ans
```

## Python3

```python
class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        seg_sum = [0] * size
        seg_sq = [0] * size
        lazy = [0] * size

        def apply(idx, v, l, r):
            length = r - l + 1
            old_sum = seg_sum[idx]
            seg_sq[idx] = (seg_sq[idx] + (2 * v % MOD) * old_sum + (v * v % MOD) * length) % MOD
            seg_sum[idx] = (old_sum + v * length) % MOD
            lazy[idx] = (lazy[idx] + v) % MOD

        def push(idx, l, r):
            if lazy[idx]:
                mid = (l + r) // 2
                apply(idx * 2, lazy[idx], l, mid)
                apply(idx * 2 + 1, lazy[idx], mid + 1, r)
                lazy[idx] = 0

        def range_add(idx, l, r, ql, qr, v):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                apply(idx, v, l, r)
                return
            push(idx, l, r)
            mid = (l + r) // 2
            range_add(idx * 2, l, mid, ql, qr, v)
            range_add(idx * 2 + 1, mid + 1, r, ql, qr, v)
            seg_sum[idx] = (seg_sum[idx * 2] + seg_sum[idx * 2 + 1]) % MOD
            seg_sq[idx] = (seg_sq[idx * 2] + seg_sq[idx * 2 + 1]) % MOD

        last = {}
        ans = 0
        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            range_add(1, 0, n - 1, prev + 1, i, 1)
            ans = (ans + seg_sq[1]) % MOD
            last[x] = i
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

struct SegNode {
    long long sum;   // sum of counts
    long long sq;    // sum of squares of counts
    int lazy;
    SegNode(): sum(0), sq(0), lazy(0) {}
};

class SegmentTree {
public:
    SegmentTree(int n): n(n) {
        tree.resize(4*n);
    }
    
    void rangeAdd(int l, int r, int val) { add(1, 0, n-1, l, r, val); }
    long long querySq(int l, int r) { return query(1, 0, n-1, l, r).sq; }

private:
    int n;
    vector<SegNode> tree;

    void apply(int idx, int len, int val) {
        SegNode &node = tree[idx];
        long long v = val;
        node.sq = (node.sq + 2LL * v % MOD * node.sum % MOD + (long long)len * v % MOD * v % MOD) % MOD;
        node.sum = (node.sum + v * len) % MOD;
        node.lazy = (node.lazy + val) % MOD;
    }

    void push(int idx, int l, int r) {
        int lazyVal = tree[idx].lazy;
        if (!lazyVal || l == r) return;
        int mid = (l + r) >> 1;
        apply(idx<<1, mid - l + 1, lazyVal);
        apply(idx<<1|1, r - mid, lazyVal);
        tree[idx].lazy = 0;
    }

    void add(int idx, int l, int r, int ql, int qr, int val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            apply(idx, r - l + 1, val);
            return;
        }
        push(idx, l, r);
        int mid = (l + r) >> 1;
        add(idx<<1, l, mid, ql, qr, val);
        add(idx<<1|1, mid+1, r, ql, qr, val);
        pull(idx);
    }

    SegNode query(int idx, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return SegNode();
        if (ql <= l && r <= qr) return tree[idx];
        push(idx, l, r);
        int mid = (l + r) >> 1;
        SegNode left = query(idx<<1, l, mid, ql, qr);
        SegNode right = query(idx<<1|1, mid+1, r, ql, qr);
        SegNode res;
        res.sum = (left.sum + right.sum) % MOD;
        res.sq  = (left.sq  + right.sq ) % MOD;
        return res;
    }

    void pull(int idx) {
        tree[idx].sum = (tree[idx<<1].sum + tree[idx<<1|1].sum) % MOD;
        tree[idx].sq  = (tree[idx<<1].sq  + tree[idx<<1|1].sq ) % MOD;
    }
};

int sumCounts(int* nums, int numsSize) {
    const int MAXV = 100000;
    vector<int> lastPos(MAXV + 5, -1);
    SegmentTree seg(numsSize);
    long long ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        int prev = lastPos[val];
        int l = prev + 1;
        if (l < 0) l = 0;
        seg.rangeAdd(l, i, 1);
        ans += seg.querySq(0, i);
        if (ans >= MOD) ans %= MOD;
        lastPos[val] = i;
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;
    
    private class SegTree {
        private readonly int n;
        private readonly long[] sum;
        private readonly long[] sq;
        private readonly long[] lazy;
        
        public SegTree(int size) {
            n = size;
            int m = 4 * n + 5;
            sum = new long[m];
            sq = new long[m];
            lazy = new long[m];
        }
        
        private void Apply(int node, int l, int r, long add) {
            long len = r - l + 1;
            long oldSum = sum[node];
            long oldSq = sq[node];
            long newSum = (oldSum + add * len) % MOD;
            long newSq = (oldSq + (2L * add % MOD) * oldSum % MOD + (add * add % MOD) * len % MOD) % MOD;
            sum[node] = newSum;
            sq[node] = newSq;
            lazy[node] = (lazy[node] + add) % MOD;
        }
        
        private void Push(int node, int l, int r) {
            if (lazy[node] != 0 && l != r) {
                int mid = (l + r) >> 1;
                Apply(node << 1, l, mid, lazy[node]);
                Apply(node << 1 | 1, mid + 1, r, lazy[node]);
                lazy[node] = 0;
            }
        }
        
        public void Update(int left, int right, long val) {
            Update(1, 0, n - 1, left, right, val);
        }
        
        private void Update(int node, int l, int r, int ql, int qr, long val) {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                Apply(node, l, r, val);
                return;
            }
            Push(node, l, r);
            int mid = (l + r) >> 1;
            Update(node << 1, l, mid, ql, qr, val);
            Update(node << 1 | 1, mid + 1, r, ql, qr, val);
            sum[node] = (sum[node << 1] + sum[node << 1 | 1]) % MOD;
            sq[node] = (sq[node << 1] + sq[node << 1 | 1]) % MOD;
        }
        
        public long QuerySq(int left, int right) {
            return QuerySq(1, 0, n - 1, left, right);
        }
        
        private long QuerySq(int node, int l, int r, int ql, int qr) {
            if (ql > r || qr < l) return 0;
            if (ql <= l && r <= qr) return sq[node];
            Push(node, l, r);
            int mid = (l + r) >> 1;
            long leftRes = QuerySq(node << 1, l, mid, ql, qr);
            long rightRes = QuerySq(node << 1 | 1, mid + 1, r, ql, qr);
            return (leftRes + rightRes) % MOD;
        }
    }
    
    public int SumCounts(int[] nums) {
        int n = nums.Length;
        var seg = new SegTree(n);
        var lastPos = new Dictionary<int, int>();
        long ans = 0;
        
        for (int i = 0; i < n; i++) {
            int prev = -1;
            if (lastPos.TryGetValue(nums[i], out int p)) prev = p;
            int l = prev + 1;
            seg.Update(l, i, 1);
            long cur = seg.QuerySq(0, i);
            ans += cur;
            if (ans >= MOD) ans -= MOD;
            lastPos[nums[i]] = i;
        }
        
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumCounts = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;
    const size = 4 * n + 5;
    const sum = new Array(size).fill(0);
    const sq = new Array(size).fill(0);
    const lazy = new Array(size).fill(0);

    function apply(idx, l, r, add) {
        const cnt = r - l + 1;
        // sq = oldSq + 2*add*oldSum + add^2 * cnt
        sq[idx] = (sq[idx] + (2 * add % MOD) * sum[idx] % MOD + (add * add % MOD) * cnt % MOD) % MOD;
        sum[idx] = (sum[idx] + add * cnt) % MOD;
        lazy[idx] = (lazy[idx] + add) % MOD;
    }

    function push(idx, l, r) {
        if (lazy[idx] !== 0 && l !== r) {
            const mid = (l + r) >> 1;
            apply(idx << 1, l, mid, lazy[idx]);
            apply(idx << 1 | 1, mid + 1, r, lazy[idx]);
            lazy[idx] = 0;
        }
    }

    function update(idx, l, r, ql, qr, add) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            apply(idx, l, r, add);
            return;
        }
        push(idx, l, r);
        const mid = (l + r) >> 1;
        update(idx << 1, l, mid, ql, qr, add);
        update(idx << 1 | 1, mid + 1, r, ql, qr, add);
        sum[idx] = (sum[idx << 1] + sum[idx << 1 | 1]) % MOD;
        sq[idx] = (sq[idx << 1] + sq[idx << 1 | 1]) % MOD;
    }

    function querySq(idx, l, r, ql, qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return sq[idx];
        push(idx, l, r);
        const mid = (l + r) >> 1;
        return (querySq(idx << 1, l, mid, ql, qr) + querySq(idx << 1 | 1, mid + 1, r, ql, qr)) % MOD;
    }

    const lastPos = new Map();
    let total = 0;

    for (let i = 0; i < n; ++i) {
        const val = nums[i];
        const prev = lastPos.has(val) ? lastPos.get(val) : -1;
        const L = prev + 1;
        const R = i;
        update(1, 0, n - 1, L, R, 1);
        const curSq = querySq(1, 0, n - 1, 0, i);
        total = (total + curSq) % MOD;
        lastPos.set(val, i);
    }

    return total;
};
```

## Typescript

```typescript
function sumCounts(nums: number[]): number {
    const MOD = 1_000_000_007;
    const n = nums.length;

    class SegmentTree {
        private n: number;
        private sum: number[];
        private lazy: number[];
        constructor(n: number) {
            this.n = n;
            const size = 4 * n;
            this.sum = new Array(size).fill(0);
            this.lazy = new Array(size).fill(0);
        }
        private push(node: number, l: number, r: number): void {
            const val = this.lazy[node];
            if (val !== 0 && l !== r) {
                const mid = (l + r) >> 1;
                const left = node << 1;
                const right = left | 1;

                this.sum[left] += (mid - l + 1) * val;
                this.lazy[left] += val;

                this.sum[right] += (r - mid) * val;
                this.lazy[right] += val;
            }
            this.lazy[node] = 0;
        }
        private rangeAdd(node: number, l: number, r: number, ql: number, qr: number, val: number): void {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                this.sum[node] += (r - l + 1) * val;
                this.lazy[node] += val;
                return;
            }
            this.push(node, l, r);
            const mid = (l + r) >> 1;
            this.rangeAdd(node << 1, l, mid, ql, qr, val);
            this.rangeAdd((node << 1) | 1, mid + 1, r, ql, qr, val);
            this.sum[node] = this.sum[node << 1] + this.sum[(node << 1) | 1];
        }
        private rangeSum(node: number, l: number, r: number, ql: number, qr: number): number {
            if (ql > r || qr < l) return 0;
            if (ql <= l && r <= qr) return this.sum[node];
            this.push(node, l, r);
            const mid = (l + r) >> 1;
            return (
                this.rangeSum(node << 1, l, mid, ql, qr) +
                this.rangeSum((node << 1) | 1, mid + 1, r, ql, qr)
            );
        }
        add(l: number, r: number, val: number): void {
            this.rangeAdd(1, 0, this.n - 1, l, r, val);
        }
        query(l: number, r: number): number {
            return this.rangeSum(1, 0, this.n - 1, l, r);
        }
    }

    const seg = new SegmentTree(n);
    const lastPos = new Map<number, number>();
    let prevF = 0; // f(i-1)
    let totalAns = 0;

    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        const prevIdx = lastPos.has(v) ? lastPos.get(v)! : -1;
        const left = prevIdx + 1;
        const right = i;

        const sumCnt = seg.query(left, right);
        const len = right - left + 1;

        let addition = (2 * (sumCnt % MOD)) % MOD;
        addition = (addition + (len % MOD)) % MOD;

        const currF = (prevF + addition) % MOD;
        totalAns = (totalAns + currF) % MOD;

        seg.add(left, right, 1);
        lastPos.set(v, i);
        prevF = currF;
    }

    return totalAns;
}
```

## Php

```php
class Fenwick {
    private int $n;
    private array $bit1;
    private array $bit2;

    public function __construct(int $size) {
        // 1-indexed BIT, allocate a bit larger for safety
        $this->n = $size + 5;
        $this->bit1 = array_fill(0, $this->n + 1, 0);
        $this->bit2 = array_fill(0, $this->n + 1, 0);
    }

    private function internalAdd(array &$bit, int $idx, int $val): void {
        while ($idx <= $this->n) {
            $bit[$idx] += $val;
            $idx += $idx & (-$idx);
        }
    }

    // add $val to range [l, r] (0‑based inclusive)
    public function rangeAdd(int $l, int $r, int $val): void {
        if ($l > $r) return;
        $l++; $r++;                     // convert to 1‑based
        $this->internalAdd($this->bit1, $l, $val);
        $this->internalAdd($this->bit1, $r + 1, -$val);
        $this->internalAdd($this->bit2, $l, $val * ($l - 1));
        $this->internalAdd($this->bit2, $r + 1, -$val * $r);
    }

    private function prefixSumIdx(int $idx): int {
        $sum1 = 0;
        $i = $idx;
        while ($i > 0) {
            $sum1 += $this->bit1[$i];
            $i -= $i & (-$i);
        }
        $sum2 = 0;
        $i = $idx;
        while ($i > 0) {
            $sum2 += $this->bit2[$i];
            $i -= $i & (-$i);
        }
        return $sum1 * $idx - $sum2;
    }

    // prefix sum of values up to position $pos (0‑based inclusive)
    public function prefixSum(int $pos): int {
        if ($pos < 0) return 0;
        $pos++;                         // to 1‑based
        return $this->prefixSumIdx($pos);
    }

    // sum over range [l, r] (0‑based inclusive)
    public function rangeSum(int $l, int $r): int {
        if ($l > $r) return 0;
        return $this->prefixSum($r) - $this->prefixSum($l - 1);
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumCounts($nums) {
        $MOD = 1000000007;
        $n = count($nums);
        $bit = new Fenwick($n);
        $lastPos = [];
        $gPrev = 0;   // sum of squares for subarrays ending at previous index
        $ans = 0;

        for ($i = 0; $i < $n; ++$i) {
            $x = $nums[$i];
            $prev = array_key_exists($x, $lastPos) ? $lastPos[$x] : -1;
            $cnt = $i - $prev;                     // number of starts where delta = 1

            if ($cnt > 0 && $i - 1 >= $prev + 1) {
                $sumD = $bit->rangeSum($prev + 1, $i - 1);
            } else {
                $sumD = 0;
            }

            $add = (2 * ($sumD % $MOD)) % $MOD;
            $gCurr = ($gPrev + $add + $cnt) % $MOD;

            $ans = ($ans + $gCurr) % $MOD;

            // update D values: add 1 to all starts > prev up to i
            $bit->rangeAdd($prev + 1, $i, 1);

            $lastPos[$x] = $i;
            $gPrev = $gCurr;
        }

        return $ans;
    }
}
```

## Swift

```swift
class SegmentTree {
    private let n: Int
    private var sum: [Int64]
    private var lazy: [Int64]

    init(_ n: Int) {
        self.n = n
        let size = 4 * n
        self.sum = Array(repeating: 0, count: size)
        self.lazy = Array(repeating: 0, count: size)
    }

    private func apply(_ node: Int, _ l: Int, _ r: Int, _ val: Int64) {
        sum[node] += val * Int64(r - l + 1)
        lazy[node] += val
    }

    private func push(_ node: Int, _ l: Int, _ r: Int) {
        if lazy[node] != 0 && l != r {
            let mid = (l + r) >> 1
            apply(node << 1, l, mid, lazy[node])
            apply((node << 1) | 1, mid + 1, r, lazy[node])
            lazy[node] = 0
        }
    }

    func rangeAdd(_ left: Int, _ right: Int, _ val: Int64) {
        rangeAdd(1, 0, n - 1, left, right, val)
    }

    private func rangeAdd(_ node: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int, _ val: Int64) {
        if ql > r || qr < l { return }
        if ql <= l && r <= qr {
            apply(node, l, r, val)
            return
        }
        push(node, l, r)
        let mid = (l + r) >> 1
        rangeAdd(node << 1, l, mid, ql, qr, val)
        rangeAdd((node << 1) | 1, mid + 1, r, ql, qr, val)
        sum[node] = sum[node << 1] + sum[(node << 1) | 1]
    }

    func querySum(_ left: Int, _ right: Int) -> Int64 {
        return querySum(1, 0, n - 1, left, right)
    }

    private func querySum(_ node: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Int64 {
        if ql > r || qr < l { return 0 }
        if ql <= l && r <= qr { return sum[node] }
        push(node, l, r)
        let mid = (l + r) >> 1
        return querySum(node << 1, l, mid, ql, qr) +
               querySum((node << 1) | 1, mid + 1, r, ql, qr)
    }
}

class Solution {
    func sumCounts(_ nums: [Int]) -> Int {
        let MOD = Int64(1_000_000_007)
        let n = nums.count
        if n == 0 { return 0 }

        let seg = SegmentTree(n)
        var lastPos = Array(repeating: -1, count: 100_001) // constraints max value

        var totalSquaresEnding: Int64 = 0
        var answer: Int64 = 0

        for i in 0..<n {
            let x = nums[i]
            let prev = lastPos[x]
            let l = prev + 1
            let r = i
            if l <= r {
                let sumD = seg.querySum(l, r)          // actual sum of distinct counts
                let len = Int64(r - l + 1)
                let extra = ( (2 * (sumD % MOD)) % MOD + len ) % MOD
                totalSquaresEnding = (totalSquaresEnding + extra) % MOD
                seg.rangeAdd(l, r, 1)
            }
            answer = (answer + totalSquaresEnding) % MOD
            lastPos[x] = i
        }

        return Int(answer)
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap

class Solution {
    private val MOD = 1_000_000_007L

    private class SegTree(private val n: Int) {
        private val sum = LongArray(4 * n)
        private val sumSq = LongArray(4 * n)
        private val lazy = LongArray(4 * n)

        private fun apply(node: Int, l: Int, r: Int, add: Long) {
            val len = (r - l + 1).toLong()
            // sumSq = sumSq + 2*add*sum + add^2 * len
            sumSq[node] = (sumSq[node] + 2L * add % MOD * sum[node] % MOD +
                    (add * add % MOD) * len % MOD) % MOD
            sum[node] = (sum[node] + add % MOD * len % MOD) % MOD
            lazy[node] = (lazy[node] + add) % MOD
        }

        private fun push(node: Int, l: Int, r: Int) {
            val add = lazy[node]
            if (add != 0L && l != r) {
                val mid = (l + r) / 2
                apply(node * 2, l, mid, add)
                apply(node * 2 + 1, mid + 1, r, add)
            }
            lazy[node] = 0L
        }

        private fun update(node: Int, l: Int, r: Int, ql: Int, qr: Int, add: Long) {
            if (ql > r || qr < l) return
            if (ql <= l && r <= qr) {
                apply(node, l, r, add)
                return
            }
            push(node, l, r)
            val mid = (l + r) / 2
            update(node * 2, l, mid, ql, qr, add)
            update(node * 2 + 1, mid + 1, r, ql, qr, add)
            sum[node] = (sum[node * 2] + sum[node * 2 + 1]) % MOD
            sumSq[node] = (sumSq[node * 2] + sumSq[node * 2 + 1]) % MOD
        }

        fun update(l: Int, r: Int, add: Long) {
            if (l > r) return
            update(1, 0, n - 1, l, r, add)
        }

        fun totalSumSq(): Long = sumSq[1]
    }

    fun sumCounts(nums: IntArray): Int {
        val n = nums.size
        val seg = SegTree(n)
        val lastPos = HashMap<Int, Int>()
        var ans = 0L

        for (i in 0 until n) {
            val v = nums[i]
            val prev = lastPos.getOrDefault(v, -1)
            seg.update(prev + 1, i, 1L)
            ans += seg.totalSumSq()
            if (ans >= MOD) ans -= MOD
            lastPos[v] = i
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class SegTree {
  static const int _mod = 1000000007;
  final int n;
  final List<int> _sum;
  final List<int> _sq;
  final List<int> _lazy;

  SegTree(this.n)
      : _sum = List.filled(4 * n, 0),
        _sq = List.filled(4 * n, 0),
        _lazy = List.filled(4 * n, 0);

  void _apply(int idx, int l, int r, int v) {
    final int len = r - l + 1;
    final int oldSum = _sum[idx];
    int addSq = ((2 * v) % _mod) * oldSum % _mod;
    addSq = (addSq + (v * v) % _mod * len % _mod) % _mod;
    _sq[idx] = (_sq[idx] + addSq) % _mod;
    _sum[idx] = (_sum[idx] + (v * len) % _mod) % _mod;
    _lazy[idx] = (_lazy[idx] + v) % _mod;
  }

  void _push(int idx, int l, int r) {
    final int v = _lazy[idx];
    if (v != 0 && l != r) {
      final int mid = (l + r) >> 1;
      _apply(idx << 1, l, mid, v);
      _apply(idx << 1 | 1, mid + 1, r, v);
      _lazy[idx] = 0;
    }
  }

  void update(int ql, int qr, int v) {
    _update(1, 0, n - 1, ql, qr, v);
  }

  void _update(int idx, int l, int r, int ql, int qr, int v) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) {
      _apply(idx, l, r, v);
      return;
    }
    _push(idx, l, r);
    final int mid = (l + r) >> 1;
    _update(idx << 1, l, mid, ql, qr, v);
    _update(idx << 1 | 1, mid + 1, r, ql, qr, v);
    _sum[idx] = (_sum[idx << 1] + _sum[idx << 1 | 1]) % _mod;
    _sq[idx] = (_sq[idx << 1] + _sq[idx << 1 | 1]) % _mod;
  }

  int querySq(int ql, int qr) {
    return _querySq(1, 0, n - 1, ql, qr);
  }

  int _querySq(int idx, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return _sq[idx];
    _push(idx, l, r);
    final int mid = (l + r) >> 1;
    final int left = _querySq(idx << 1, l, mid, ql, qr);
    final int right = _querySq(idx << 1 | 1, mid + 1, r, ql, qr);
    return (left + right) % _mod;
  }
}

class Solution {
  static const int _MOD = 1000000007;

  int sumCounts(List<int> nums) {
    final int n = nums.length;
    final seg = SegTree(n);
    final Map<int, int> lastPos = {};
    int ans = 0;

    for (int i = 0; i < n; ++i) {
      final int val = nums[i];
      final int prev = lastPos.containsKey(val) ? lastPos[val]! : -1;
      final int start = prev + 1;
      seg.update(start, i, 1);
      final int sqTotal = seg.querySq(0, i);
      ans += sqTotal;
      if (ans >= _MOD) ans -= _MOD;
      lastPos[val] = i;
    }
    return ans % _MOD;
  }
}
```

## Golang

```go
package main

import "math"

const MOD int64 = 1000000007

type Fenwick struct {
	n    int
	tree []int64
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{n: n, tree: make([]int64, n+2)}
}

func (f *Fenwick) add(idx int, delta int64) {
	if delta < 0 {
		delta = (delta%MOD + MOD) % MOD
	}
	for i := idx; i <= f.n; i += i & -i {
		f.tree[i] += delta
		if f.tree[i] >= MOD {
			f.tree[i] -= MOD
		}
	}
}

func (f *Fenwick) sum(idx int) int64 {
	var res int64 = 0
	for i := idx; i > 0; i -= i & -i {
		res += f.tree[i]
		if res >= MOD {
			res -= MOD
		}
	}
	return res
}

// range add val to [l, r] (0‑based inclusive)
func rangeAdd(b1, b2 *Fenwick, l, r int, val int64) {
	L := l + 1
	R := r + 1

	b1.add(L, val)
	if R+1 <= b1.n {
		b1.add(R+1, -val)
	}
	b2.add(L, (val*int64(L-1))%MOD)
	if R+1 <= b2.n {
		b2.add(R+1, -(val*int64(R))%MOD)
	}
}

// prefix sum up to x (1‑based)
func prefix(b1, b2 *Fenwick, x int) int64 {
	s1 := b1.sum(x)
	s2 := b2.sum(x)
	res := (s1*int64(x) - s2) % MOD
	if res < 0 {
		res += MOD
	}
	return res
}

// range sum over [l, r] (0‑based inclusive)
func rangeSum(b1, b2 *Fenwick, l, r int) int64 {
	if l > r {
		return 0
	}
	sumR := prefix(b1, b2, r+1)
	sumL := prefix(b1, b2, l)
	res := sumR - sumL
	if res < 0 {
		res += MOD
	}
	return res
}

func sumCounts(nums []int) int {
	n := len(nums)
	b1 := NewFenwick(n + 2)
	b2 := NewFenwick(n + 2)

	lastPos := make(map[int]int, n)
	var totalSq int64 = 0
	var ans int64 = 0

	for i, x := range nums {
		p, ok := lastPos[x]
		if !ok {
			p = -1
		}
		l := p + 1
		r := i
		length := r - l + 1 // equals i - p

		sumCntRange := rangeSum(b1, b2, l, r)

		totalSq = (totalSq + 2*sumCntRange%MOD + int64(length)%MOD) % MOD

		if length > 0 {
			rangeAdd(b1, b2, l, r, 1)
		}

		ans += totalSq
		if ans >= MOD {
			ans -= MOD
		}
		lastPos[x] = i
	}
	return int(ans % MOD)
}
```

## Ruby

```ruby
def sum_counts(nums)
  mod = 1_000_000_007
  n = nums.length
  seg = SegmentTree.new(n, mod)
  last = {}
  s_prev = 0
  ans = 0

  nums.each_with_index do |val, i|
    prev = last.key?(val) ? last[val] : -1

    sum_c = if prev + 1 <= i - 1
              seg.range_sum(prev + 1, i - 1)
            else
              0
            end

    length = i - prev
    extra = (2 * sum_c + length) % mod
    s_i = (s_prev + extra) % mod
    ans = (ans + s_i) % mod

    seg.range_add(prev + 1, i, 1)

    s_prev = s_i
    last[val] = i
  end

  ans % mod
end

class SegmentTree
  def initialize(n, mod)
    @n = n
    @mod = mod
    size = 4 * n
    @sum = Array.new(size, 0)
    @lazy = Array.new(size, 0)
  end

  def range_add(l, r, val)
    _add(1, 0, @n - 1, l, r, val % @mod) if l <= r
  end

  def range_sum(l, r)
    return 0 if l > r
    _sum(1, 0, @n - 1, l, r) % @mod
  end

  private

  def apply(node, l, r, val)
    @sum[node] = (@sum[node] + (r - l + 1) * val) % @mod
    @lazy[node] = (@lazy[node] + val) % @mod
  end

  def push(node, l, r)
    if @lazy[node] != 0 && l < r
      mid = (l + r) / 2
      left = node * 2
      right = left + 1
      apply(left, l, mid, @lazy[node])
      apply(right, mid + 1, r, @lazy[node])
      @lazy[node] = 0
    end
  end

  def _add(node, l, r, ql, qr, val)
    return if ql > r || qr < l
    if ql <= l && r <= qr
      apply(node, l, r, val)
      return
    end
    push(node, l, r)
    mid = (l + r) / 2
    _add(node * 2, l, mid, ql, qr, val)
    _add(node * 2 + 1, mid + 1, r, ql, qr, val)
    @sum[node] = (@sum[node * 2] + @sum[node * 2 + 1]) % @mod
  end

  def _sum(node, l, r, ql, qr)
    return 0 if ql > r || qr < l
    if ql <= l && r <= qr
      return @sum[node]
    end
    push(node, l, r)
    mid = (l + r) / 2
    left_sum = _sum(node * 2, l, mid, ql, qr)
    right_sum = _sum(node * 2 + 1, mid + 1, r, ql, qr)
    (left_sum + right_sum) % @mod
  end
end
```

## Scala

```scala
object Solution {
    def sumCounts(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        class BIT(n: Int) {
            private val size = n + 2
            private val bit1 = new Array[Long](size)
            private val bit2 = new Array[Long](size)

            private def add(bit: Array[Long], idx0: Int, delta: Long): Unit = {
                var i = idx0
                while (i < size) {
                    bit(i) += delta
                    i += i & -i
                }
            }

            def rangeAdd(l: Int, r: Int, delta: Long): Unit = {
                if (l > r) return
                val L = l + 1
                val R = r + 1
                add(bit1, L, delta)
                add(bit1, R + 1, -delta)
                add(bit2, L, delta * (L - 1))
                add(bit2, R + 1, -delta * R)
            }

            private def sum(bit: Array[Long], idx0: Int): Long = {
                var i = idx0
                var res = 0L
                while (i > 0) {
                    res += bit(i)
                    i -= i & -i
                }
                res
            }

            private def prefix(idx: Int): Long = {
                val i = idx + 1
                val s1 = sum(bit1, i)
                val s2 = sum(bit2, i)
                s1 * i - s2
            }

            def rangeSum(l: Int, r: Int): Long = {
                if (l > r) 0L else prefix(r) - (if (l == 0) 0L else prefix(l - 1))
            }
        }

        val n = nums.length
        val bit = new BIT(n)
        import scala.collection.mutable
        val last = mutable.Map[Int, Int]().withDefaultValue(-1)

        var fPrev = 0L
        var ans = 0L

        for (i <- 0 until n) {
            val prevIdx = last(nums(i))
            var sumIncD = 0L
            if (prevIdx + 1 <= i - 1) {
                sumIncD = bit.rangeSum(prevIdx + 1, i - 1) % MOD
            }
            val cntIncExisting = ((i - prevIdx - 1).toLong) % MOD

            var fCurr = (fPrev + 1) % MOD
            fCurr = (fCurr + (2L * sumIncD) % MOD) % MOD
            fCurr = (fCurr + cntIncExisting) % MOD

            ans = (ans + fCurr) % MOD

            bit.rangeAdd(prevIdx + 1, i, 1L)
            last(nums(i)) = i
            fPrev = fCurr
        }

        ans.toInt
    }
}
```

## Rust

```rust
use std::collections::HashMap;

const MOD: i64 = 1_000_000_007;

struct SegTree {
    n: usize,
    sum: Vec<i64>,
    sq: Vec<i64>,
    lazy: Vec<i64>,
}

impl SegTree {
    fn new(n: usize) -> Self {
        let size = 4 * n + 5;
        SegTree {
            n,
            sum: vec![0; size],
            sq: vec![0; size],
            lazy: vec![0; size],
        }
    }

    #[inline]
    fn apply(&mut self, idx: usize, l: usize, r: usize, v: i64) {
        let len = (r - l + 1) as i64 % MOD;
        let v_mod = v % MOD;
        // new_sq = sq + 2*v*sum + v^2 * len
        self.sq[idx] = (self.sq[idx]
            + 2 * v_mod % MOD * self.sum[idx] % MOD
            + v_mod * v_mod % MOD * len % MOD)
            % MOD;
        // new_sum = sum + v * len
        self.sum[idx] = (self.sum[idx] + v_mod * len % MOD) % MOD;
        self.lazy[idx] = (self.lazy[idx] + v_mod) % MOD;
    }

    #[inline]
    fn push(&mut self, idx: usize, l: usize, r: usize) {
        let lazy_val = self.lazy[idx];
        if lazy_val != 0 && l != r {
            let mid = (l + r) / 2;
            self.apply(idx * 2, l, mid, lazy_val);
            self.apply(idx * 2 + 1, mid + 1, r, lazy_val);
            self.lazy[idx] = 0;
        }
    }

    #[inline]
    fn pull(&mut self, idx: usize) {
        self.sum[idx] = (self.sum[idx * 2] + self.sum[idx * 2 + 1]) % MOD;
        self.sq[idx] = (self.sq[idx * 2] + self.sq[idx * 2 + 1]) % MOD;
    }

    fn range_add(&mut self, ql: usize, qr: usize, v: i64) {
        self._range_add(1, 0, self.n - 1, ql, qr, v);
    }

    fn _range_add(
        &mut self,
        idx: usize,
        l: usize,
        r: usize,
        ql: usize,
        qr: usize,
        v: i64,
    ) {
        if ql > r || qr < l {
            return;
        }
        if ql <= l && r <= qr {
            self.apply(idx, l, r, v);
            return;
        }
        self.push(idx, l, r);
        let mid = (l + r) / 2;
        self._range_add(idx * 2, l, mid, ql, qr, v);
        self._range_add(idx * 2 + 1, mid + 1, r, ql, qr, v);
        self.pull(idx);
    }

    fn total_sq(&self) -> i64 {
        self.sq[1]
    }
}

impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut seg = SegTree::new(n);
        let mut last: HashMap<i32, usize> = HashMap::new();
        let mut ans: i64 = 0;

        for (i, &x) in nums.iter().enumerate() {
            let l = match last.get(&x) {
                Some(&prev) => prev + 1,
                None => 0,
            };
            seg.range_add(l, i, 1);
            ans = (ans + seg.total_sq()) % MOD;
            last.insert(x, i);
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (sum-counts nums)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (size (* 4 n))
         (sumV (make-vector size 0))
         (sqV (make-vector size 0))
         (lazyV (make-vector size 0))
         (prev (make-hash)))
    (define (mod x) (remainder x MOD))
    (letrec
        ((apply
           (lambda (node l r v)
             (let* ((len (+ (- r l) 1))
                    (sum (vector-ref sumV node))
                    (sq (vector-ref sqV node))
                    (vmod (mod v))
                    (add-sq (mod (+ (* (mod (* 2 vmod)) sum)
                                    (* len (mod (* vmod vmod))))))
                    (new-sq (mod (+ sq add-sq)))
                    (new-sum (mod (+ sum (mod (* len vmod))))))
               (vector-set! sqV node new-sq)
               (vector-set! sumV node new-sum)
               (let ((lz (vector-ref lazyV node)))
                 (vector-set! lazyV node (mod (+ lz vmod)))))))
         (push
           (lambda (node l r)
             (let ((lz (vector-ref lazyV node)))
               (when (> lz 0)
                 (let ((mid (quotient (+ l r) 2))
                       (left (* node 2))
                       (right (+ (* node 2) 1)))
                   (apply left l mid lz)
                   (apply right (add1 mid) r lz)
                   (vector-set! lazyV node 0))))))
         (update
           (lambda (node l r ql qr v)
             (cond ((or (> ql r) (< qr l)) (void))
                   ((and (<= ql l) (>= qr r))
                    (apply node l r v))
                   (else
                    (push node l r)
                    (let ((mid (quotient (+ l r) 2)))
                      (update (* node 2) l mid ql qr v)
                      (update (+ (* node 2) 1) (add1 mid) r ql qr v)
                      (let ((sum-left (vector-ref sumV (* node 2)))
                            (sum-right (vector-ref sumV (+ (* node 2) 1)))
                            (sq-left (vector-ref sqV (* node 2)))
                            (sq-right (vector-ref sqV (+ (* node 2) 1))))
                        (vector-set! sumV node (mod (+ sum-left sum-right)))
                        (vector-set! sqV node (mod (+ sq-left sq-right)))))))))
         (querySq
           (lambda (node l r ql qr)
             (cond ((or (> ql r) (< qr l)) 0)
                   ((and (<= ql l) (>= qr r))
                    (vector-ref sqV node))
                   (else
                    (push node l r)
                    (let ((mid (quotient (+ l r) 2)))
                      (mod (+ (querySq (* node 2) l mid ql qr)
                              (querySq (+ (* node 2) 1) (add1 mid) r ql qr)))))))))
      (let ((ans 0))
        (for ([i (in-range n)])
          (let* ((a (vector-ref arr i))
                 (p (hash-ref prev a -1))
                 (l (+ p 1))
                 (r i))
            (when (<= l r)
              (update 1 0 (- n 1) l r 1))
            (set! ans (mod (+ ans (querySq 1 0 (- n 1) 0 i))))
            (hash-set! prev a i)))
        ans))))
```

## Erlang

```erlang
-module(solution).
-export([sum_counts/1]).

-define(MOD, 1000000007).

%% Public API
-spec sum_counts(Nums :: [integer()]) -> integer().
sum_counts(Nums) ->
    N = length(Nums),
    Size = N + 2,
    Empty = array:new(Size, {default,0}),
    process(0, Nums, #{}, Empty, Empty, 0, 0, N).

%% Recursive processing of each element
-spec process(Index :: integer(),
              Rest :: [integer()],
              LastMap :: map(),
              BIT1 :: tuple(),
              BIT2 :: tuple(),
              TotalSq :: integer(),
              Ans :: integer(),
              N :: integer()) -> integer().
process(_Idx, [], _LastMap, _B1, _B2, _TotalSq, Ans, _N) ->
    Ans rem ?MOD;
process(Idx, [Val | Rest], LastMap, B1, B2, TotalSq, Ans, N) ->
    Prev = maps:get(Val, LastMap, -1),
    L = Prev + 2,
    R = Idx + 1,
    {RangeSum, Len} =
        if
            L =< R ->
                SumR = prefix_sum(B1, B2, R),
                SumLMinus1 = prefix_sum(B1, B2, L - 1),
                RS = (SumR - SumLMinus1 + ?MOD) rem ?MOD,
                {RS, R - L + 1};
            true ->
                {0, 0}
        end,
    DeltaSq = ((2 * RangeSum) rem ?MOD + Len) rem ?MOD,
    NewTotalSq = (TotalSq + DeltaSq) rem ?MOD,
    {NewB1, NewB2} =
        if
            L =< R ->
                B1a = bit_update(B1, L, 1, N),
                B1b = if R + 1 =< N -> bit_update(B1a, R + 1, ?MOD - 1, N); true -> B1a end,
                B2a = bit_update(B2, L, (L - 1) rem ?MOD, N),
                NegR = (?MOD - (R rem ?MOD)) rem ?MOD,
                B2b = if R + 1 =< N -> bit_update(B2a, R + 1, NegR, N); true -> B2a end,
                {B1b, B2b};
            true ->
                {B1, B2}
        end,
    NewLastMap = maps:put(Val, Idx, LastMap),
    process(Idx + 1, Rest, NewLastMap, NewB1, NewB2,
            NewTotalSq, (Ans + NewTotalSq) rem ?MOD, N).

%% BIT point update with lazy propagation (range add handled externally)
-spec bit_update(BIT :: tuple(), Index :: integer(), Delta :: integer(),
                 Size :: integer()) -> tuple().
bit_update(BIT, Index, Delta, Size) when Index =< Size ->
    Old = array:get(Index, BIT),
    NewVal = (Old + Delta) rem ?MOD,
    Updated = array:set(Index, NewVal, BIT),
    Next = Index + (Index band -Index),
    bit_update(Updated, Next, Delta, Size);
bit_update(BIT, _Idx, _Delta, _Size) ->
    BIT.

%% BIT prefix sum query
-spec bit_query(BIT :: tuple(), Index :: integer()) -> integer().
bit_query(_BIT, 0) -> 0;
bit_query(BIT, Index) when Index > 0 ->
    Val = array:get(Index, BIT),
    (Val + bit_query(BIT, Index - (Index band -Index))) rem ?MOD.

%% Prefix sum of the underlying array represented by two BITs
-spec prefix_sum(B1 :: tuple(), B2 :: tuple(), X :: integer()) -> integer().
prefix_sum(B1, B2, X) ->
    S1 = bit_query(B1, X),
    S2 = bit_query(B2, X),
    ((S1 * X) rem ?MOD - S2 + ?MOD) rem ?MOD.
```

## Elixir

```elixir
defmodule BIT do
  @moduledoc false
  defstruct size: 0, b1: nil, b2: nil

  import Bitwise

  def new(n) do
    %BIT{
      size: n,
      b1: :array.new(n + 2, default: 0),
      b2: :array.new(n + 2, default: 0)
    }
  end

  # point update on array (functional), returns new array
  defp point_update(arr, idx, delta, limit) when idx <= limit do
    cur = :array.get(idx, arr)
    arr = :array.set(idx, cur + delta, arr)
    point_update(arr, idx + (idx &&& -idx), delta, limit)
  end

  defp point_update(arr, _idx, _delta, _limit), do: arr

  # prefix query on array
  defp prefix_query(arr, idx) when idx > 0 do
    do_prefix_query(arr, idx, 0)
  end

  defp prefix_query(_arr, 0), do: 0

  defp do_prefix_query(arr, idx, acc) when idx > 0 do
    cur = :array.get(idx, arr)
    do_prefix_query(arr, idx - (idx &&& -idx), acc + cur)
  end

  defp do_prefix_query(_arr, 0, acc), do: acc

  # add delta to range [l, r] (0-indexed inclusive)
  def add_range(bit, l, r, delta) do
    limit = bit.size + 1
    b1 = point_update(bit.b1, l + 1, delta, limit)
    b1 = point_update(b1, r + 2, -delta, limit)

    b2 = point_update(bit.b2, l + 1, delta * l, limit)
    b2 = point_update(b2, r + 2, -delta * (r + 1), limit)

    %BIT{bit | b1: b1, b2: b2}
  end

  # prefix sum for indices [0..idx] (0-indexed inclusive)
  def prefix_sum(bit, idx) do
    s1 = prefix_query(bit.b1, idx + 1)
    s2 = prefix_query(bit.b2, idx + 1)
    s1 * (idx + 1) - s2
  end

  # range sum for [l, r] inclusive
  def range_sum(bit, l, r) when l <= r do
    left = if l > 0, do: prefix_sum(bit, l - 1), else: 0
    prefix_sum(bit, r) - left
  end

  def range_sum(_bit, _l, _r), do: 0
end

defmodule Solution do
  @moduledoc false
  @spec sum_counts(nums :: [integer]) :: integer
  def sum_counts(nums) do
    mod = 1_000_000_007
    n = length(nums)
    bit = BIT.new(n)
    {ans, _sq_prev, _bit, _last} =
      Enum.reduce(Enum.with_index(nums), {0, 0, bit, %{}},
        fn {val, i}, {acc_ans, sq_prev, cur_bit, last_map} ->
          prev = Map.get(last_map, val, -1)
          l = prev + 1
          r = i
          len = r - l + 1

          sum_d = if l <= r, do: BIT.range_sum(cur_bit, l, r), else: 0

          sq_i = (sq_prev + 2 * sum_d + len) |> rem(mod)
          acc_ans = (acc_ans + sq_i) |> rem(mod)

          updated_bit = BIT.add_range(cur_bit, l, r, 1)
          updated_last = Map.put(last_map, val, i)

          {acc_ans, sq_i, updated_bit, updated_last}
        end)

    ans
  end
end
```

# 3605. Minimum Stability Factor of Array

## Cpp

```cpp
class Solution {
public:
    int n;
    vector<int> nums;
    vector<vector<int>> st;
    vector<int> lg;
    
    int queryGCD(int l, int r) {
        int len = r - l + 1;
        int j = lg[len];
        return std::gcd(st[l][j], st[r - (1 << j) + 1][j]);
    }
    
    bool can(int k, int maxC) {
        int L = k + 1;
        if (L > n) return true; // no window of this size
        int edits = 0;
        int lastEditedPos = -1;
        for (int i = 0; i + L - 1 < n; ++i) {
            if (queryGCD(i, i + L - 1) > 1) {
                // interval [i, i+L-1] needs to be hit
                if (i <= lastEditedPos) continue; // already covered
                edits++;
                lastEditedPos = i + L - 1;
                if (edits > maxC) return false;
            }
        }
        return true;
    }
    
    int minStable(vector<int>& nums_, int maxC) {
        nums = nums_;
        n = nums.size();
        // build log table
        lg.assign(n + 1, 0);
        for (int i = 2; i <= n; ++i) lg[i] = lg[i >> 1] + 1;
        int K = lg[n] + 1;
        st.assign(n, vector<int>(K));
        for (int i = 0; i < n; ++i) st[i][0] = nums[i];
        for (int j = 1; j < K; ++j) {
            for (int i = 0; i + (1 << j) <= n; ++i) {
                st[i][j] = std::gcd(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
            }
        }
        int low = 0, high = n;
        while (low < high) {
            int mid = (low + high) / 2;
            if (can(mid, maxC))
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    private static class SegTree {
        int n;
        long[] tree;
        SegTree(long[] arr) {
            n = arr.length;
            tree = new long[4 * n];
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
            tree[node] = gcd(tree[node << 1], tree[node << 1 | 1]);
        }
        long query(int L, int R) {
            return query(1, 0, n - 1, L, R);
        }
        private long query(int node, int l, int r, int L, int R) {
            if (L <= l && r <= R) return tree[node];
            int mid = (l + r) >>> 1;
            long res = 0;
            if (L <= mid) res = gcd(res, query(node << 1, l, mid, L, R));
            if (R > mid) res = gcd(res, query(node << 1 | 1, mid + 1, r, L, R));
            return res;
        }
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int minStable(int[] nums, int maxC) {
        int n = nums.length;
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) arr[i] = nums[i];
        SegTree seg = new SegTree(arr);

        int low = 0, high = n; // answer in [0, n]
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (canAchieve(mid, maxC, n, seg)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private boolean canAchieve(int k, int maxC, int n, SegTree seg) {
        int L = k + 1; // window size that must be broken
        if (L > n) return true; // no such windows
        int edits = 0;
        int editPos = -1; // last edited index
        for (int start = 0; start <= n - L; start++) {
            int end = start + L - 1;
            if (editPos >= start && editPos <= end) continue; // already covered
            long g = seg.query(start, end);
            if (g > 1) {
                edits++;
                if (edits > maxC) return false;
                editPos = end; // place edit at rightmost position
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def minStable(self, nums, maxC):
        """
        :type nums: List[int]
        :type maxC: int
        :rtype: int
        """
        import math

        n = len(nums)
        # build log table
        LOG = [0] * (n + 1)
        for i in range(2, n + 1):
            LOG[i] = LOG[i // 2] + 1

        K = LOG[n] + 1
        st = [[0] * n for _ in range(K)]
        st[0] = nums[:]
        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1
            prev = st[j - 1]
            cur = st[j]
            limit = n - length + 1
            for i in range(limit):
                cur[i] = math.gcd(prev[i], prev[i + half])
            j += 1

        def range_gcd(l, r):
            """inclusive indices"""
            k = LOG[r - l + 1]
            return math.gcd(st[k][l], st[k][r - (1 << k) + 1])

        # feasibility check for given max stable length L
        def feasible(L):
            w = L + 1
            if w > n:
                return True
            cnt = 0
            last_selected = -1
            i = 0
            while i + w <= n:
                if range_gcd(i, i + w - 1) > 1:
                    l, r = i, i + w - 1
                    if last_selected < l:
                        cnt += 1
                        if cnt > maxC:
                            return False
                        last_selected = r
                i += 1
            return True

        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
import math
from typing import List

class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.N = 1
        while self.N < n:
            self.N <<= 1
        self.seg = [0] * (2 * self.N)
        # build leaves
        for i in range(n):
            self.seg[self.N + i] = data[i]
        for i in range(self.N - 1, 0, -1):
            self.seg[i] = math.gcd(self.seg[2 * i], self.seg[2 * i + 1])

    def query(self, l, r):  # inclusive
        l += self.N
        r += self.N
        res = 0
        while l <= r:
            if (l & 1) == 1:
                res = math.gcd(res, self.seg[l])
                l += 1
            if (r & 1) == 0:
                res = math.gcd(res, self.seg[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        seg = SegmentTree(nums)

        def feasible(k):
            # ensure no stable subarray longer than k
            if k >= n:
                return True
            cnt = 0
            last_edit = -1
            win_len = k + 1
            for i in range(0, n - win_len + 1):
                if i <= last_edit:
                    continue
                g = seg.query(i, i + k)
                if g > 1:
                    cnt += 1
                    if cnt > maxC:
                        return False
                    last_edit = i + k
            return True

        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

static int *seg;
static int N;

static int gcdfunc(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static void build(int node, int l, int r, const int *arr) {
    if (l == r) {
        seg[node] = arr[l];
        return;
    }
    int mid = (l + r) >> 1;
    build(node << 1, l, mid, arr);
    build(node << 1 | 1, mid + 1, r, arr);
    seg[node] = gcdfunc(seg[node << 1], seg[node << 1 | 1]);
}

static int query(int node, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) return seg[node];
    int mid = (l + r) >> 1;
    int res = 0; // gcd(0,x)=x
    if (ql <= mid) res = gcdfunc(res, query(node << 1, l, mid, ql, qr));
    if (qr > mid)  res = gcdfunc(res, query(node << 1 | 1, mid + 1, r, ql, qr));
    return res;
}

static int feasible(int k, const int *nums, int maxC) {
    if (k >= N) return 1; // no window to check
    int edits = 0;
    int lastEdited = -1; // index of most recent edit
    int winLen = k + 1;
    for (int i = 0; i + winLen - 1 < N; ++i) {
        if (i <= lastEdited) continue; // already covered by previous edit
        int g = query(1, 0, N - 1, i, i + k);
        if (g > 1) {
            ++edits;
            if (edits > maxC) return 0;
            lastEdited = i + k; // place edit at right end of window
        }
    }
    return 1;
}

int minStable(int* nums, int numsSize, int maxC) {
    N = numsSize;
    seg = (int*)malloc(sizeof(int) * 4 * N);
    build(1, 0, N - 1, nums);

    int low = 0, high = N; // answer in [0,N]
    while (low < high) {
        int mid = (low + high) >> 1;
        if (feasible(mid, nums, maxC))
            high = mid;
        else
            low = mid + 1;
    }
    free(seg);
    return low;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinStable(int[] nums, int maxC) {
        int n = nums.Length;
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) arr[i] = nums[i];

        SegTree seg = new SegTree(arr);

        bool Feasible(int k) {
            int L = k + 1;
            if (L > n) return true;
            int edits = 0;
            int lastEdit = -1;
            for (int i = 0; i <= n - L; i++) {
                if (i <= lastEdit) continue;
                long g = seg.Query(i, i + L - 1);
                if (g > 1) {
                    edits++;
                    if (edits > maxC) return false;
                    lastEdit = i + L - 1;
                }
            }
            return true;
        }

        int low = 0, high = n;
        while (low < high) {
            int mid = (low + high) / 2;
            if (Feasible(mid)) high = mid;
            else low = mid + 1;
        }
        return low;
    }

    private static long Gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return Math.Abs(a);
    }

    private class SegTree {
        private readonly int n;
        private readonly long[] tree;

        public SegTree(long[] data) {
            n = data.Length;
            tree = new long[4 * n];
            Build(1, 0, n - 1, data);
        }

        private void Build(int node, int l, int r, long[] data) {
            if (l == r) {
                tree[node] = data[l];
                return;
            }
            int mid = (l + r) >> 1;
            Build(node << 1, l, mid, data);
            Build(node << 1 | 1, mid + 1, r, data);
            tree[node] = Gcd(tree[node << 1], tree[node << 1 | 1]);
        }

        public long Query(int left, int right) {
            return Query(1, 0, n - 1, left, right);
        }

        private long Query(int node, int nl, int nr, int ql, int qr) {
            if (ql > nr || qr < nl) return 0;
            if (ql <= nl && nr <= qr) return tree[node];
            int mid = (nl + nr) >> 1;
            long leftGcd = Query(node << 1, nl, mid, ql, qr);
            long rightGcd = Query(node << 1 | 1, mid + 1, nr, ql, qr);
            return Gcd(leftGcd, rightGcd);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} maxC
 * @return {number}
 */
var minStable = function(nums, maxC) {
    const n = nums.length;
    // build segment tree for range GCD queries
    let size = 1;
    while (size < n) size <<= 1;
    const seg = new Array(size << 1).fill(0);
    for (let i = 0; i < n; ++i) seg[size + i] = nums[i];
    for (let i = size - 1; i > 0; --i) seg[i] = gcd(seg[i << 1], seg[(i << 1) | 1]);

    const rangeGcd = (l, r) => {
        l += size;
        r += size;
        let res = 0;
        while (l <= r) {
            if ((l & 1) === 1) {
                res = gcd(res, seg[l]);
                ++l;
            }
            if ((r & 1) === 0) {
                res = gcd(res, seg[r]);
                --r;
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    };

    const canAchieve = (k) => {
        const len = k + 1;
        if (len > n) return true; // no window of this size
        let edits = 0;
        let lastEdited = -1;
        for (let i = 0; i <= n - len; ++i) {
            if (lastEdited >= i) continue; // already covered by previous edit
            const g = rangeGcd(i, i + len - 1);
            if (g > 1) {
                ++edits;
                if (edits > maxC) return false;
                lastEdited = i + len - 1; // place edit at rightmost position
            }
        }
        return true;
    };

    let lo = 0, hi = n;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (canAchieve(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;

    function gcd(a, b) {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
};
```

## Typescript

```typescript
function minStable(nums: number[], maxC: number): number {
    const n = nums.length;
    if (n === 0) return 0;

    // GCD helper
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    };

    // Build log table
    const lg = new Array(n + 1).fill(0);
    for (let i = 2; i <= n; ++i) lg[i] = lg[i >> 1] + 1;

    const K = lg[n] + 1;
    const st: number[][] = Array.from({ length: K }, () => new Array(n).fill(0));
    for (let i = 0; i < n; ++i) st[0][i] = nums[i];
    for (let k = 1; k < K; ++k) {
        const len = 1 << k;
        const half = len >> 1;
        for (let i = 0; i + len <= n; ++i) {
            st[k][i] = gcd(st[k - 1][i], st[k - 1][i + half]);
        }
    }

    const rangeGcd = (l: number, r: number): number => {
        const len = r - l + 1;
        const k = lg[len];
        return gcd(st[k][l], st[k][r - (1 << k) + 1]);
    };

    // Check if we can achieve stability factor <= limit with at most maxC edits
    const can = (limit: number): boolean => {
        if (limit >= n) return true; // no restriction needed
        const winSize = limit + 1;
        let edits = 0;
        let nextStart = 0; // earliest window start not yet covered by an edit

        for (let i = 0; i + winSize - 1 < n; ++i) {
            if (i < nextStart) continue; // already hit by previous edit
            const g = rangeGcd(i, i + winSize - 1);
            if (g > 1) {
                edits++;
                if (edits > maxC) return false;
                // place edit at the rightmost position of this window
                nextStart = i + winSize; // windows starting up to i+winSize-1 are now covered
            }
        }
        return true;
    };

    // Binary search minimal possible stability factor
    let lo = 0, hi = n;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (can(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

## Php

```php
class SegmentTree {
    private int $size;
    private array $tree;

    public function __construct(array $arr) {
        $n = count($arr);
        $this->size = 1;
        while ($this->size < $n) {
            $this->size <<= 1;
        }
        $this->tree = array_fill(0, $this->size * 2, 0);
        for ($i = 0; $i < $n; $i++) {
            $this->tree[$this->size + $i] = $arr[$i];
        }
        for ($i = $this->size - 1; $i > 0; $i--) {
            $this->tree[$i] = self::gcd($this->tree[$i << 1], $this->tree[($i << 1) | 1]);
        }
    }

    public function query(int $l, int $r): int {
        $l += $this->size;
        $r += $this->size;
        $res = 0;
        while ($l <= $r) {
            if (($l & 1) == 1) {
                $res = self::gcd($res, $this->tree[$l]);
                $l++;
            }
            if (($r & 1) == 0) {
                $res = self::gcd($res, $this->tree[$r]);
                $r--;
            }
            $l >>= 1;
            $r >>= 1;
        }
        return $res;
    }

    private static function gcd(int $a, int $b): int {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $maxC
     * @return Integer
     */
    function minStable($nums, $maxC) {
        $n = count($nums);
        if ($maxC >= $n) return 0;

        $st = new SegmentTree($nums);

        $low = 0;
        $high = $n; // answer lies in [0, n]

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canAchieve($mid, $st, $maxC, $n)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }

    private function canAchieve(int $k, SegmentTree $st, int $maxC, int $n): bool {
        $len = $k + 1;
        if ($len > $n) return true; // no window of this size
        $edits = 0;
        $lastEdited = -1;

        for ($i = 0; $i + $len - 1 < $n; $i++) {
            $g = $st->query($i, $i + $len - 1);
            if ($g > 1 && $i + $len - 1 > $lastEdited) {
                $edits++;
                $lastEdited = $i + $len - 1;
                if ($edits > $maxC) return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func minStable(_ nums: [Int], _ maxC: Int) -> Int {
        let n = nums.count
        var seg = SegmentTree(nums)
        
        func can(_ L: Int) -> Bool {
            let K = L + 1
            if K > n { return true }
            var edits = 0
            var lastEditedPos = -1
            var i = 0
            while i <= n - K {
                if lastEditedPos >= i && lastEditedPos <= i + K - 1 {
                    i += 1
                    continue
                }
                let g = seg.query(i, i + K - 1)
                if g > 1 {
                    edits += 1
                    if edits > maxC { return false }
                    lastEditedPos = i + K - 1
                }
                i += 1
            }
            return true
        }
        
        var low = 0
        var high = n
        while low < high {
            let mid = (low + high) >> 1
            if can(mid) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}

func gcd(_ a: Int, _ b: Int) -> Int {
    var x = a
    var y = b
    while y != 0 {
        let t = x % y
        x = y
        y = t
    }
    return abs(x)
}

struct SegmentTree {
    private var n: Int
    private var tree: [Int]
    
    init(_ arr: [Int]) {
        self.n = arr.count
        self.tree = Array(repeating: 0, count: 4 * n)
        build(arr, 1, 0, n - 1)
    }
    
    private mutating func build(_ arr: [Int], _ node: Int, _ l: Int, _ r: Int) {
        if l == r {
            tree[node] = arr[l]
        } else {
            let mid = (l + r) >> 1
            build(arr, node << 1, l, mid)
            build(arr, node << 1 | 1, mid + 1, r)
            tree[node] = gcd(tree[node << 1], tree[node << 1 | 1])
        }
    }
    
    func query(_ left: Int, _ right: Int) -> Int {
        return queryRec(1, 0, n - 1, left, right)
    }
    
    private func queryRec(_ node: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Int {
        if ql <= l && r <= qr {
            return tree[node]
        }
        let mid = (l + r) >> 1
        var res = 0
        if ql <= mid {
            res = gcd(res, queryRec(node << 1, l, mid, ql, min(qr, mid)))
        }
        if qr > mid {
            res = gcd(res, queryRec(node << 1 | 1, mid + 1, r, max(ql, mid + 1), qr))
        }
        return res
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minStable(nums: IntArray, maxC: Int): Int {
        val n = nums.size
        if (n == 0) return 0
        // precompute logs
        val log = IntArray(n + 1)
        for (i in 2..n) {
            log[i] = log[i shr 1] + 1
        }
        val K = log[n] + 1
        val st = Array(K) { IntArray(n) }
        // level 0
        for (i in 0 until n) st[0][i] = nums[i]
        var j = 1
        while ((1 shl j) <= n) {
            val len = 1 shl j
            val half = len shr 1
            for (i in 0..n - len) {
                st[j][i] = gcd(st[j - 1][i], st[j - 1][i + half])
            }
            j++
        }

        fun query(l: Int, r: Int): Int {
            val len = r - l + 1
            val p = log[len]
            val span = 1 shl p
            return gcd(st[p][l], st[p][r - span + 1])
        }

        fun canAchieve(k: Int): Boolean {
            if (k >= n) return true // no window of size k+1 exists
            var edits = 0
            var lastPick = -1
            val winSize = k + 1
            var i = 0
            while (i <= n - winSize) {
                if (query(i, i + k) > 1) {
                    if (i > lastPick) {
                        edits++
                        if (edits > maxC) return false
                        lastPick = i + k
                    }
                }
                i++
            }
            return true
        }

        var low = 0
        var high = n
        while (low < high) {
            val mid = (low + high) ushr 1
            if (canAchieve(mid)) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = kotlin.math.abs(a)
        var y = kotlin.math.abs(b)
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  late List<int> _tree;
  late List<int> _arr;
  late int _n;

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a.abs();
  }

  void _build(int node, int l, int r) {
    if (l == r) {
      _tree[node] = _arr[l];
    } else {
      int mid = (l + r) >> 1;
      _build(node << 1, l, mid);
      _build(node << 1 | 1, mid + 1, r);
      _tree[node] = _gcd(_tree[node << 1], _tree[node << 1 | 1]);
    }
  }

  int _query(int node, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) return _tree[node];
    int mid = (l + r) >> 1;
    int res = 0; // gcd(0,x)=x
    if (ql <= mid) res = _gcd(res, _query(node << 1, l, mid, ql, qr));
    if (qr > mid) res = _gcd(res, _query(node << 1 | 1, mid + 1, r, ql, qr));
    return res;
  }

  int minStable(List<int> nums, int maxC) {
    _arr = nums;
    _n = nums.length;
    _tree = List.filled(_n * 4, 0);
    _build(1, 0, _n - 1);

    bool can(int k) {
      int len = k + 1;
      if (len > _n) return true;
      int used = 0;
      int lastPos = -1; // last edited index
      for (int i = 0; i <= _n - len; ++i) {
        if (lastPos >= i) continue; // already covered by previous edit
        int g = _query(1, 0, _n - 1, i, i + len - 1);
        if (g > 1) {
          used++;
          if (used > maxC) return false;
          lastPos = i + len - 1; // edit at rightmost position of window
        }
      }
      return true;
    }

    int lo = -1, hi = _n;
    while (hi - lo > 1) {
      int mid = (lo + hi) >> 1;
      if (can(mid)) {
        hi = mid;
      } else {
        lo = mid;
      }
    }
    return hi;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func minStable(nums []int, maxC int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	st := buildSegTree(nums)

	// helper to check if we can achieve stability factor <= k
	can := func(k int) bool {
		if k >= n {
			return true
		}
		windowSize := k + 1
		lastEdited := -1
		used := 0
		for i := 0; i+windowSize-1 < n; i++ {
			if i <= lastEdited {
				continue
			}
			g := querySegTree(st, i, i+windowSize-1)
			if g > 1 {
				used++
				lastEdited = i + windowSize - 1
				if used > maxC {
					return false
				}
			}
		}
		return true
	}

	low, high := -1, n
	for high-low > 1 {
		mid := (low + high) / 2
		if can(mid) {
			high = mid
		} else {
			low = mid
		}
	}
	return high
}

// segment tree for range GCD
type segNode struct {
	l, r int
	val  int
}

func buildSegTree(arr []int) []*segNode {
	n := len(arr)
	size := 4 * n
	tree := make([]*segNode, size)

	var build func(idx, l, r int)
	build = func(idx, l, r int) {
		node := &segNode{l: l, r: r}
		if l == r {
			node.val = arr[l]
		} else {
			mid := (l + r) / 2
			build(idx*2, l, mid)
			build(idx*2+1, mid+1, r)
			left := tree[idx*2].val
			right := tree[idx*2+1].val
			node.val = gcd(left, right)
		}
		tree[idx] = node
	}
	build(1, 0, n-1)
	return tree
}

func querySegTree(tree []*segNode, l, r int) int {
	var query func(idx, ql, qr int) int
	query = func(idx, ql, qr int) int {
		node := tree[idx]
		if node.l > qr || node.r < ql {
			return 0 // gcd(0,x)=x
		}
		if ql <= node.l && node.r <= qr {
			return node.val
		}
		left := query(idx*2, ql, qr)
		right := query(idx*2+1, ql, qr)
		if left == 0 {
			return right
		}
		if right == 0 {
			return left
		}
		return gcd(left, right)
	}
	return query(1, l, r)
}

func gcd(a, b int) int {
	a = int(math.Abs(float64(a)))
	b = int(math.Abs(float64(b)))
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def min_stable(nums, max_c)
  n = nums.length
  # build sparse table for GCD queries
  log = Array.new(n + 1, 0)
  (2..n).each { |i| log[i] = log[i / 2] + 1 }
  kmax = log[n]
  st = Array.new(kmax + 1) { Array.new(n, 0) }
  st[0] = nums.clone
  j = 1
  while (1 << j) <= n
    len = 1 << j
    half = len >> 1
    limit = n - len + 1
    i = 0
    while i < limit
      st[j][i] = st[j - 1][i].gcd(st[j - 1][i + half])
      i += 1
    end
    j += 1
  end

  range_gcd = lambda do |l, r|
    len = r - l + 1
    k = log[len]
    a = st[k][l]
    b = st[k][r - (1 << k) + 1]
    a.gcd(b)
  end

  feasible = lambda do |k|
    window = k + 1
    return true if window == 0
    edits = 0
    last_edit = -1
    i = 0
    while i + window <= n
      if last_edit >= i
        # already covered by previous edit
      else
        g = range_gcd.call(i, i + window - 1)
        if g > 1
          edits += 1
          return false if edits > max_c
          last_edit = i + window - 1
        end
      end
      i += 1
    end
    true
  end

  low = 0
  high = n
  while low < high
    mid = (low + high) / 2
    if feasible.call(mid)
      high = mid
    else
      low = mid + 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
  def minStable(nums: Array[Int], maxC: Int): Int = {
    val n = nums.length
    // precompute logs
    val log = new Array[Int](n + 2)
    var i = 2
    while (i <= n + 1) {
      log(i) = log(i >> 1) + 1
      i += 1
    }
    val K = log(n) + 1
    val st = Array.ofDim[Int](K, n)
    // level 0
    System.arraycopy(nums, 0, st(0), 0, n)
    var k = 1
    while ((1 << k) <= n) {
      val half = 1 << (k - 1)
      i = 0
      while (i + (1 << k) <= n) {
        st(k)(i) = gcd(st(k - 1)(i), st(k - 1)(i + half))
        i += 1
      }
      k += 1
    }

    def rangeGcd(l: Int, r: Int): Int = {
      val len = r - l + 1
      val kk = log(len)
      gcd(st(kk)(l), st(kk)(r - (1 << kk) + 1))
    }

    def can(limit: Int): Boolean = {
      val w = limit + 1
      if (w > n) return true
      var lastMod = -1
      var used = 0
      i = 0
      while (i <= n - w) {
        if (i > lastMod) {
          if (rangeGcd(i, i + w - 1) > 1) {
            used += 1
            if (used > maxC) return false
            lastMod = i + w - 1
          }
        }
        i += 1
      }
      true
    }

    var lo = 0
    var hi = n
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (can(mid)) hi = mid else lo = mid + 1
    }
    lo
  }

  @annotation.tailrec
  private def gcd(a: Int, b: Int): Int =
    if (b == 0) math.abs(a) else gcd(b, a % b)
}
```

## Rust

```rust
use std::cmp::min;

pub struct Solution;

impl Solution {
    pub fn min_stable(nums: Vec<i32>, max_c: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // build logs
        let mut log = vec![0usize; n + 1];
        for i in 2..=n {
            log[i] = log[i / 2] + 1;
        }
        let max_log = log[n];
        // sparse table for GCD
        let mut st: Vec<Vec<i64>> = vec![vec![0; n]; max_log + 1];
        for i in 0..n {
            st[0][i] = nums[i] as i64;
        }
        for j in 1..=max_log {
            let len = 1usize << j;
            for i in 0..=n - len {
                st[j][i] = gcd(st[j - 1][i], st[j - 1][i + (len >> 1)]);
            }
        }

        // helper to query GCD on [l, r] inclusive
        let range_gcd = |l: usize, r: usize, st: &Vec<Vec<i64>>, log: &Vec<usize>| -> i64 {
            let len = r - l + 1;
            let k = log[len];
            gcd(st[k][l], st[k][r - (1 << k) + 1])
        };

        let max_c_usize = max_c as usize;

        // check if we can achieve stability factor <=k
        let can = |k: usize,
                   n: usize,
                   L: usize,
                   range_gcd: &dyn Fn(usize, usize, &Vec<Vec<i64>>, &Vec<usize>) -> i64,
                   st: &Vec<Vec<i64>>,
                   log: &Vec<usize>,
                   max_c_usize: usize|
         -> bool {
            if L > n {
                return true;
            }
            let mut edits = 0usize;
            let mut last_edit: isize = -1; // position of last edited element
            for start in 0..=n - L {
                let end = start + L - 1;
                if (last_edit as usize) >= start && (last_edit as usize) <= end {
                    continue;
                }
                let g = range_gcd(start, end, st, log);
                if g > 1 {
                    edits += 1;
                    if edits > max_c_usize {
                        return false;
                    }
                    last_edit = end as isize; // edit at rightmost position
                }
            }
            true
        };

        let mut lo: usize = 0;
        let mut hi: usize = n; // answer lies in [0, n]
        while lo < hi {
            let mid = (lo + hi) / 2;
            let L = mid + 1; // window size to forbid
            if can(
                mid,
                n,
                L,
                &range_gcd,
                &st,
                &log,
                max_c_usize,
            ) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a.abs()
}
```

## Racket

```racket
(define (min-stable nums maxC)
  (let* ((n (length nums))
         (arr (list->vector nums))
         ;; log table
         (logv (let ((v (make-vector (+ n 1) 0)))
                 (let loop ((i 2))
                   (when (<= i n)
                     (vector-set! v i (+ 1 (vector-ref v (quotient i 2))))
                     (loop (+ i 1))))
                 v))
         ;; build sparse table for GCD
         (K (let loop ((k 0) (p 1))
              (if (> p n) k
                  (loop (+ k 1) (* p 2)))))
         (table (let ((tbl (make-vector (+ K 1))))
                  (vector-set! tbl 0 arr)
                  (let loop-j ((j 1))
                    (when (<= j K)
                      (let* ((len (arithmetic-shift 1 j))
                             (half (arithmetic-shift 1 (- j 1)))
                             (prev (vector-ref tbl (- j 1)))
                             (cur (make-vector n 0)))
                        (let loop-i ((i 0))
                          (when (<= i (- n len))
                            (let* ((a (vector-ref prev i))
                                   (b (vector-ref prev (+ i half)))
                                   (g (gcd a b)))
                              (vector-set! cur i g)
                              (loop-i (+ i 1)))))
                        (vector-set! tbl j cur)
                        (loop-j (+ j 1))))
                  tbl))
         ;; GCD query on [l, r] inclusive
         (gcd-range
          (lambda (l r)
            (if (= l r)
                (vector-ref arr l)
                (let* ((len (+ (- r l) 1))
                       (j (vector-ref logv len))
                       (pow (arithmetic-shift 1 j))
                       (a (vector-ref (vector-ref table j) l))
                       (b (vector-ref (vector-ref table j) (- r (- pow) 1))))
                  (gcd a b))))))
    ;; feasibility test for given L
    (define (feasible? L)
      (let ((w (+ L 1)))
        (if (> w n)
            #t
            (let loop ((i 0) (last-edit -1) (cnt 0))
              (cond [(> i (- n w)) (<= cnt maxC)]
                    [else
                     (let ((g (gcd-range i (+ i w -1))))
                       (if (> g 1)
                           (if (>= last-edit i)
                               (loop (+ i 1) last-edit cnt)
                               (let ((pos (+ i w -1)))
                                 (if (> (+ cnt 1) maxC)
                                     #f
                                     (loop (+ i 1) pos (+ cnt 1)))))
                           (loop (+ i 1) last-edit cnt)))])))))
    ;; binary search for minimal feasible L
    (let loop ((lo 0) (hi n))
      (if (= lo hi)
          lo
          (let ((mid (quotient (+ lo hi) 2)))
            (if (feasible? mid)
                (loop lo mid)
                (loop (+ mid 1) hi)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_stable/2]).

%% Public API
-spec min_stable(Nums :: [integer()], MaxC :: integer()) -> integer().
min_stable(Nums, MaxC) ->
    N = length(Nums),
    LogT = build_log(N),
    Level0 = list_to_tuple(Nums),
    StL = build_sparse_levels(Level0, N),
    binary_search(0, N, MaxC, N, LogT, StL).

%% Binary search for minimal feasible K
binary_search(Low, High, MaxC, N, LogT, StL) when Low < High ->
    Mid = (Low + High) div 2,
    case feasible(Mid, MaxC, N, LogT, StL) of
        true -> binary_search(Low, Mid, MaxC, N, LogT, StL);
        false -> binary_search(Mid + 1, High, MaxC, N, LogT, StL)
    end;
binary_search(Low, _High, _MaxC, _N, _LogT, _StL) ->
    Low.

%% Check if stability factor K is achievable with at most MaxC modifications
feasible(K, MaxC, N, LogT, StL) when K >= N ->
    true;
feasible(K, MaxC, N, LogT, StL) ->
    Window = K + 1,
    Limit = N - Window,
    feasible_iter(0, -1, 0, Limit, Window, MaxC, LogT, StL).

feasible_iter(I, _LastMod, Count, Limit, _Window, MaxC, _LogT, _StL) when I > Limit ->
    Count =< MaxC;
feasible_iter(I, LastMod, Count, Limit, Window, MaxC, LogT, StL) ->
    if
        I =< LastMod ->
            feasible_iter(I + 1, LastMod, Count, Limit, Window, MaxC, LogT, StL);
        true ->
            G = range_gcd(I, I + Window - 1, LogT, StL),
            if
                G > 1 ->
                    NewCount = Count + 1,
                    if
                        NewCount > MaxC -> false;
                        true -> feasible_iter(I + 1, I + Window - 1, NewCount, Limit, Window, MaxC, LogT, StL)
                    end;
                true ->
                    feasible_iter(I + 1, LastMod, Count, Limit, Window, MaxC, LogT, StL)
            end
    end.

%% GCD of subarray [L,R] using sparse table
range_gcd(L, R, LogT, StL) ->
    Len = R - L + 1,
    K = element(Len + 1, LogT),
    TupleK = lists:nth(K + 1, StL),
    Shift = (1 bsl K) - 1,
    G1 = element(L + 1, TupleK),
    G2 = element(R - Shift + 1, TupleK),
    gcd(G1, G2).

%% Build logarithm table (floor of log2)
build_log(N) ->
    List = [if I == 0 -> 0; true -> trunc(math:log2(I)) end || I <- lists:seq(0, N)],
    list_to_tuple(List).

%% Build sparse table for GCD
build_sparse_levels(Level0, N) ->
    MaxJ = trunc(math:log2(N)),
    build_levels(1, MaxJ, N, [Level0]).

build_levels(J, MaxJ, _N, Acc) when J > MaxJ ->
    lists:reverse(Acc);
build_levels(J, MaxJ, N, Acc) ->
    Prev = hd(Acc),
    Shift = 1 bsl (J - 1),
    Len = N - (1 bsl J) + 1,
    NextList = [gcd(element(I + 1, Prev), element(I + Shift + 1, Prev)) || I <- lists:seq(0, Len - 1)],
    NextTuple = list_to_tuple(NextList),
    build_levels(J + 1, MaxJ, N, [NextTuple | Acc]).

%% Euclidean algorithm for GCD
gcd(0, B) -> B;
gcd(A, 0) -> A;
gcd(A, B) when A < B ->
    gcd(B, A);
gcd(A, B) ->
    gcd(B rem A, A).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec min_stable(nums :: [integer], max_c :: integer) :: integer
  def min_stable(nums, max_c) do
    {seg, size} = build_seg(nums)
    n = length(nums)
    binary_search(0, n, nums, max_c, seg, size)
  end

  # Build segment tree stored in a map for O(1) access
  defp build_seg(nums) do
    n = length(nums)

    size =
      (fn s ->
        if s >= n, do: s, else: s * 2 |> (&(&1)).()
      end).(1)
    # ensure power of two >= n
    size = 
      Enum.reduce_while(0..30, 1, fn _, acc ->
        if acc >= n, do: {:halt, acc}, else: {:cont, acc <<< 1}
      end)

    seg0 =
      Enum.with_index(nums)
      |> Enum.reduce(%{}, fn {val, i}, acc -> Map.put(acc, size + i, val) end)

    seg_filled =
      Enum.reduce((size + n)..(2 * size - 1), seg0, fn idx, acc ->
        Map.put(acc, idx, 0)
      end)

    seg_full =
      Enum.reduce(Enum.reverse(1..(size - 1)), seg_filled, fn i, acc ->
        left = Map.get(acc, i * 2, 0)
        right = Map.get(acc, i * 2 + 1, 0)
        Map.put(acc, i, Integer.gcd(left, right))
      end)

    {seg_full, size}
  end

  # Query GCD on interval [l, r] (0‑based inclusive)
  defp query(seg, size, l0, r0) do
    do_query(l0 + size, r0 + size, 0, seg)
  end

  defp do_query(l, r, acc, seg) do
    if l > r do
      acc
    else
      {acc1, l1} =
        if (l &&& 1) == 1 do
          {Integer.gcd(acc, Map.get(seg, l)), l + 1}
        else
          {acc, l}
        end

      {acc2, r1} =
        if (r &&& 1) == 0 do
          {Integer.gcd(acc1, Map.get(seg, r)), r - 1}
        else
          {acc1, r}
        end

      do_query(l1 >>> 1, r1 >>> 1, acc2, seg)
    end
  end

  # Check if stability factor <= L is achievable with at most max_c edits
  defp feasible?(nums, max_c, seg, size, l) do
    n = length(nums)
    w = l + 1

    if w > n do
      true
    else
      Enum.reduce_while(0..(n - w), {0, -1}, fn i, {need, last} ->
        g = query(seg, size, i, i + w - 1)

        cond do
          g <= 1 ->
            {:cont, {need, last}}

          i > last ->
            need2 = need + 1

            if need2 > max_c do
              {:halt, false}
            else
              {:cont, {need2, i + w - 1}}
            end

          true ->
            {:cont, {need, last}}
        end
      end)
      |> case do
        false -> false
        _ -> true
      end
    end
  end

  # Binary search for minimal feasible L
  defp binary_search(low, high, nums, max_c, seg, size) do
    if low < high do
      mid = div(low + high, 2)

      if feasible?(nums, max_c, seg, size, mid) do
        binary_search(low, mid, nums, max_c, seg, size)
      else
        binary_search(mid + 1, high, nums, max_c, seg, size)
      end
    else
      low
    end
  end
end
```

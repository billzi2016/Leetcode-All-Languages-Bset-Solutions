# 3413. Maximum Coins From K Consecutive Bags

## Cpp

```cpp
class Solution {
public:
    long long maximumCoins(std::vector<std::vector<int>>& coins, int k) {
        using ll = long long;
        int n = coins.size();
        std::vector<ll> L(n), R(n), C(n);
        for (int i = 0; i < n; ++i) {
            L[i] = coins[i][0];
            R[i] = coins[i][1];
            C[i] = coins[i][2];
        }
        // sort by left endpoint
        std::vector<int> idx(n);
        for (int i = 0; i < n; ++i) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b){ return L[a] < L[b]; });
        std::vector<ll> starts, ends, vals, pref;
        starts.reserve(n);
        ends.reserve(n);
        vals.reserve(n);
        pref.reserve(n);
        for (int id : idx) {
            starts.push_back(L[id]);
            ends.push_back(R[id]);
            vals.push_back(C[id]);
            ll contrib = (R[id] - L[id] + 1LL) * C[id];
            if (pref.empty()) pref.push_back(contrib);
            else pref.push_back(pref.back() + contrib);
        }
        int m = starts.size();
        auto getSum = [&](ll left, ll right)->ll{
            if (left > right) return 0;
            // first interval that may intersect
            int i = std::lower_bound(ends.begin(), ends.end(), left) - ends.begin();
            if (i == m) return 0;
            int j = std::upper_bound(starts.begin(), starts.end(), right) - starts.begin() - 1;
            if (j < i) return 0;
            ll sum = 0;
            // overlap with interval i
            ll l1 = std::max(left, starts[i]);
            ll r1 = std::min(right, ends[i]);
            if (l1 <= r1) sum += (r1 - l1 + 1) * vals[i];
            if (i == j) return sum;
            // overlap with interval j
            ll lj = std::max(left, starts[j]);
            ll rj = std::min(right, ends[j]);
            if (lj <= rj) sum += (rj - lj + 1) * vals[j];
            // full intervals between i+1 and j-1
            if (j > i + 1) {
                sum += pref[j-1] - pref[i];
            }
            return sum;
        };
        std::vector<ll> candidates;
        candidates.reserve(2*m);
        for (int i = 0; i < m; ++i) {
            candidates.push_back(starts[i]);
            ll s2 = ends[i] - (ll)k + 1;
            if (s2 >= 1) candidates.push_back(s2);
        }
        ll ans = 0;
        for (ll s : candidates) {
            ll cur = getSum(s, s + (ll)k - 1);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumCoins(int[][] coins, int k) {
        // Sort intervals by left coordinate
        java.util.Arrays.sort(coins, (a, b) -> Integer.compare(a[0], b[0]));
        int n = coins.length;
        long[] L = new long[n];
        long[] R = new long[n];
        long[] C = new long[n];
        for (int i = 0; i < n; i++) {
            L[i] = coins[i][0];
            R[i] = coins[i][1];
            C[i] = coins[i][2];
        }
        // Prefix sums of total coins per whole interval
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            long len = R[i] - L[i] + 1;
            pref[i + 1] = pref[i] + len * C[i];
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            // Candidate start at left bound
            ans = Math.max(ans, windowSum(L[i], k, L, R, C, pref));
            // Candidate start so that right end aligns with interval's right bound
            long s2 = R[i] - (long) k + 1;
            ans = Math.max(ans, windowSum(s2, k, L, R, C, pref));
        }
        return ans;
    }

    private long windowSum(long start, int k, long[] L, long[] R, long[] C, long[] pref) {
        long end = start + (long) k - 1;
        return getCoinsUpTo(end, L, R, C, pref) - getCoinsUpTo(start - 1, L, R, C, pref);
    }

    private long getCoinsUpTo(long pos, long[] L, long[] R, long[] C, long[] pref) {
        if (pos < L[0]) return 0;
        int idx = upperBound(L, pos) - 1; // index of interval with L <= pos
        long sum = pref[idx]; // total coins from intervals before idx
        if (pos >= R[idx]) {
            sum += (R[idx] - L[idx] + 1) * C[idx];
        } else {
            sum += (pos - L[idx] + 1) * C[idx];
        }
        return sum;
    }

    private int upperBound(long[] arr, long target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
class Solution(object):
    def maximumCoins(self, coins, k):
        """
        :type coins: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect

        # sort intervals by left endpoint
        coins.sort(key=lambda x: x[0])
        n = len(coins)
        L = [c[0] for c in coins]
        R = [c[1] for c in coins]
        C = [c[2] for c in coins]

        # prefix sum of total coins up to each interval's end
        cum = [0] * n
        s = 0
        for i in range(n):
            length = R[i] - L[i] + 1
            s += length * C[i]
            cum[i] = s

        def prefix(x):
            """total coins in bags with position <= x (inclusive)"""
            if x < L[0]:
                return 0
            # find last interval whose start <= x
            i = bisect.bisect_right(L, x) - 1
            if i >= 0 and R[i] >= x:
                before = cum[i - 1] if i > 0 else 0
                return before + (x - L[i] + 1) * C[i]
            # otherwise x lies after some intervals but not inside any
            j = bisect.bisect_right(R, x) - 1
            if j >= 0:
                return cum[j]
            return 0

        candidates = set()
        for li, ri in zip(L, R):
            candidates.add(li)
            candidates.add(ri - k + 1)

        best = 0
        for s_start in candidates:
            e_end = s_start + k - 1
            cur = prefix(e_end) - prefix(s_start - 1)
            if cur > best:
                best = cur

        return best
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # sort intervals by left endpoint
        coins.sort(key=lambda x: x[0])
        n = len(coins)
        L = [c[0] for c in coins]
        R = [c[1] for c in coins]
        C = [c[2] for c in coins]

        # prefix sum of total coins per interval
        pref = [0] * (n + 1)
        for i in range(n):
            length = R[i] - L[i] + 1
            pref[i + 1] = pref[i] + length * C[i]

        ends = R  # already sorted because intervals are non‑overlapping and sorted by L

        def window_sum(start: int) -> int:
            end = start + k - 1
            # first interval that may intersect (r >= start)
            left_idx = bisect.bisect_left(ends, start)
            if left_idx == n:
                return 0
            # last interval that may intersect (l <= end)
            right_idx = bisect.bisect_right(L, end) - 1
            if right_idx < 0 or left_idx > right_idx:
                return 0

            total = 0
            if left_idx == right_idx:
                overlap = min(R[left_idx], end) - max(L[left_idx], start) + 1
                total = overlap * C[left_idx]
                return total

            # left partial interval
            left_overlap = R[left_idx] - start + 1
            total += left_overlap * C[left_idx]

            # right partial interval
            right_overlap = end - L[right_idx] + 1
            total += right_overlap * C[right_idx]

            # fully covered intervals between them
            if left_idx + 1 <= right_idx - 1:
                total += pref[right_idx] - pref[left_idx + 1]

            return total

        candidates = set()
        for i in range(n):
            candidates.add(L[i])
            start2 = R[i] - k + 1
            if start2 >= 1:
                candidates.add(start2)

        ans = 0
        for s in candidates:
            cur = window_sum(s)
            if cur > ans:
                ans = cur
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    long long l;
    long long r;
    long long c;
} Interval;

static int cmpInterval(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->l < ib->l) return -1;
    if (ia->l > ib->l) return 1;
    return 0;
}

static int cmpLL(const void *a, const void *b) {
    long long va = *(const long long *)a;
    long long vb = *(const long long *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

/* total coins from position 1 up to x inclusive */
static long long getSum(long long x, Interval *arr, int n, long long *pref) {
    if (n == 0 || x < arr[0].l) return 0LL;
    int lo = 0, hi = n - 1, idx = -1;
    while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        if (arr[mid].l <= x) {
            idx = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    if (idx == -1) return 0LL;
    if (x >= arr[idx].r) {
        return pref[idx];
    } else {
        long long before = (idx > 0) ? pref[idx - 1] : 0LL;
        return before + (x - arr[idx].l + 1) * arr[idx].c;
    }
}

long long maximumCoins(int** coins, int coinsSize, int* coinsColSize, int k) {
    int n = coinsSize;
    if (n == 0) return 0LL;

    Interval *arr = (Interval *)malloc(sizeof(Interval) * n);
    for (int i = 0; i < n; ++i) {
        arr[i].l = (long long)coins[i][0];
        arr[i].r = (long long)coins[i][1];
        arr[i].c = (long long)coins[i][2];
    }
    qsort(arr, n, sizeof(Interval), cmpInterval);

    long long *pref = (long long *)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; ++i) {
        long long len = arr[i].r - arr[i].l + 1;
        long long total = len * arr[i].c;
        pref[i] = (i > 0 ? pref[i - 1] : 0LL) + total;
    }

    int candCap = 2 * n;
    long long *cand = (long long *)malloc(sizeof(long long) * candCap);
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        cand[cnt++] = arr[i].l;
        cand[cnt++] = arr[i].r - (long long)k + 1LL;
    }
    qsort(cand, cnt, sizeof(long long), cmpLL);

    long long ans = 0LL;
    for (int i = 0; i < cnt; ++i) {
        long long start = cand[i];
        long long end = start + (long long)k - 1LL;
        long long total = getSum(end, arr, n, pref) - getSum(start - 1LL, arr, n, pref);
        if (total > ans) ans = total;
    }

    free(arr);
    free(pref);
    free(cand);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MaximumCoins(int[][] coins, int k) {
        int n = coins.Length;
        var intervals = new (long l, long r, long c)[n];
        for (int i = 0; i < n; i++) {
            intervals[i] = (coins[i][0], coins[i][1], coins[i][2]);
        }
        Array.Sort(intervals, (a, b) => a.l.CompareTo(b.l));

        long[] L = new long[n];
        long[] R = new long[n];
        long[] C = new long[n];
        for (int i = 0; i < n; i++) {
            L[i] = intervals[i].l;
            R[i] = intervals[i].r;
            C[i] = intervals[i].c;
        }

        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + C[i] * (R[i] - L[i] + 1);
        }

        var candidates = new List<long>(2 * n);
        foreach (var iv in intervals) {
            candidates.Add(iv.l);
            candidates.Add(iv.r - k + 1);
        }

        long best = 0;
        foreach (long start in candidates) {
            long sum = GetSum(start, k, L, R, C, pref);
            if (sum > best) best = sum;
        }
        return best;
    }

    private long GetSum(long start, long k, long[] L, long[] R, long[] C, long[] pref) {
        long end = start + k - 1;
        int n = L.Length;

        int leftIdx = LowerBound(R, start);          // first interval with r >= start
        int rightIdx = UpperBound(L, end) - 1;       // last interval with l <= end

        if (leftIdx >= n || rightIdx < 0 || leftIdx > rightIdx) return 0L;

        long total = pref[rightIdx + 1] - pref[leftIdx];

        long leftExcess = Math.Max(0L, start - L[leftIdx]);
        total -= leftExcess * C[leftIdx];

        long rightExcess = Math.Max(0L, R[rightIdx] - end);
        total -= rightExcess * C[rightIdx];

        return total;
    }

    private int LowerBound(long[] arr, long target) {
        int lo = 0, hi = arr.Length;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (arr[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private int UpperBound(long[] arr, long target) {
        int lo = 0, hi = arr.Length;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (arr[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} coins
 * @param {number} k
 * @return {number}
 */
var maximumCoins = function(coins, k) {
    // sort intervals by left endpoint
    coins.sort((a, b) => a[0] - b[0]);
    const n = coins.length;
    const L = new Array(n);
    const R = new Array(n);
    const C = new Array(n);
    const pref = new Array(n); // total coins up to R[i]
    for (let i = 0; i < n; ++i) {
        L[i] = coins[i][0];
        R[i] = coins[i][1];
        C[i] = coins[i][2];
        const len = R[i] - L[i] + 1;
        const total = len * C[i];
        pref[i] = (i > 0 ? pref[i - 1] : 0) + total;
    }

    // helper: total coins from position 1 to x inclusive
    function getSum(x) {
        if (x < L[0]) return 0;
        // binary search last interval with L <= x
        let lo = 0, hi = n - 1, idx = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (L[mid] <= x) {
                idx = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        if (idx === -1) return 0;
        if (x <= R[idx]) {
            const before = idx > 0 ? pref[idx - 1] : 0;
            return before + (x - L[idx] + 1) * C[idx];
        } else {
            // x lies after this interval (maybe between intervals)
            return pref[idx];
        }
    }

    function windowSum(start) {
        const end = start + k - 1;
        return getSum(end) - getSum(start - 1);
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) {
        // candidate starting at left endpoint
        let s1 = L[i];
        if (s1 >= 1) {
            const val = windowSum(s1);
            if (val > ans) ans = val;
        }
        // candidate where right edge aligns with interval's end
        let s2 = R[i] - k + 1;
        if (s2 < 1) s2 = 1;
        const val2 = windowSum(s2);
        if (val2 > ans) ans = val2;
    }
    return ans;
};
```

## Typescript

```typescript
function maximumCoins(coins: number[][], k: number): number {
    const n = coins.length;
    const intervals = coins.map(c => ({ l: c[0], r: c[1], c: c[2] }));
    intervals.sort((a, b) => a.l - b.l);

    const L = new Array<number>(n);
    const R = new Array<number>(n);
    const C = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        L[i] = intervals[i].l;
        R[i] = intervals[i].r;
        C[i] = intervals[i].c;
    }

    const pref = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        const total = (R[i] - L[i] + 1) * C[i];
        pref[i] = total + (i > 0 ? pref[i - 1] : 0);
    }

    function findLeftIdx(pos: number): number {
        let lo = 0, hi = n - 1, ans = n;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (R[mid] >= pos) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }

    function findRightIdx(pos: number): number {
        let lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (L[mid] <= pos) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }

    function windowSum(start: number): number {
        const end = start + k - 1;
        const leftIdx = findLeftIdx(start);
        const rightIdx = findRightIdx(end);
        if (leftIdx > rightIdx || leftIdx === n || rightIdx === -1) return 0;

        let total = pref[rightIdx] - (leftIdx > 0 ? pref[leftIdx - 1] : 0);

        if (start > L[leftIdx]) {
            const cut = (start - L[leftIdx]) * C[leftIdx];
            total -= cut;
        }
        if (end < R[rightIdx]) {
            const cut = (R[rightIdx] - end) * C[rightIdx];
            total -= cut;
        }
        return total;
    }

    const candidates = new Set<number>();
    for (let i = 0; i < n; i++) {
        candidates.add(L[i]);
        const s = R[i] - k + 1;
        if (s >= 1) candidates.add(s);
    }

    let maxCoins = 0;
    for (const start of candidates) {
        const sum = windowSum(start);
        if (sum > maxCoins) maxCoins = sum;
    }
    return maxCoins;
}
```

## Php

```php
class Solution {
    private $L = [];
    private $R = [];
    private $C = [];
    private $pref = [];

    private function getPrefix($x) {
        if ($x < $this->L[0]) return 0;
        $n = count($this->R);
        $lo = 0;
        $hi = $n - 1;
        $idx = -1;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->R[$mid] <= $x) {
                $idx = $mid;
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        $sum = 0;
        if ($idx >= 0) $sum = $this->pref[$idx];
        $next = $idx + 1;
        if ($next < $n && $this->L[$next] <= $x) {
            $partialLen = $x - $this->L[$next] + 1;
            $sum += $partialLen * $this->C[$next];
        }
        return $sum;
    }

    /**
     * @param Integer[][] $coins
     * @param Integer $k
     * @return Integer
     */
    function maximumCoins($coins, $k) {
        usort($coins, function($a, $b) { return $a[0] <=> $b[0]; });
        $n = count($coins);
        $this->L = $this->R = $this->C = $this->pref = [];
        for ($i = 0; $i < $n; $i++) {
            [$l, $r, $c] = $coins[$i];
            $this->L[] = $l;
            $this->R[] = $r;
            $this->C[] = $c;
            $len = $r - $l + 1;
            $total = $len * $c;
            if ($i == 0) {
                $this->pref[] = $total;
            } else {
                $this->pref[] = $this->pref[$i - 1] + $total;
            }
        }

        $candidates = [];
        for ($i = 0; $i < $n; $i++) {
            $candidates[] = $this->L[$i];
            $cand2 = $this->R[$i] - $k + 1;
            if ($cand2 >= 1) $candidates[] = $cand2;
        }
        sort($candidates);
        $max = 0;
        foreach ($candidates as $s) {
            if ($s < 1) $s = 1;
            $end = $s + $k - 1;
            $sum = $this->getPrefix($end) - $this->getPrefix($s - 1);
            if ($sum > $max) $max = $sum;
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maximumCoins(_ coins: [[Int]], _ k: Int) -> Int {
        typealias LL = Int64
        let n = coins.count
        var intervals = [(l: LL, r: LL, c: LL)]()
        intervals.reserveCapacity(n)
        for arr in coins {
            let l = LL(arr[0])
            let r = LL(arr[1])
            let c = LL(arr[2])
            intervals.append((l, r, c))
        }
        intervals.sort { $0.l < $1.l }
        var L = [LL]()
        var R = [LL]()
        var C = [LL]()
        L.reserveCapacity(n)
        R.reserveCapacity(n)
        C.reserveCapacity(n)
        for iv in intervals {
            L.append(iv.l)
            R.append(iv.r)
            C.append(iv.c)
        }
        // prefix sum of total coins per interval
        var pref = [LL](repeating: 0, count: n)
        for i in 0..<n {
            let len = R[i] - L[i] + 1
            let total = len * C[i]
            pref[i] = total + (i > 0 ? pref[i-1] : 0)
        }
        func lowerBound(_ arr: [LL], _ target: LL) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let m = (l + r) >> 1
                if arr[m] < target {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }
        func upperBound(_ arr: [LL], _ target: LL) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let m = (l + r) >> 1
                if arr[m] <= target {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }
        func getSum(_ a: LL, _ b: LL) -> LL {
            if a > b { return 0 }
            let leftIdx = lowerBound(R, a)
            if leftIdx == n { return 0 }
            let rightIdxExclusive = upperBound(L, b)
            let rightIdx = rightIdxExclusive - 1
            if rightIdx < leftIdx { return 0 }
            if leftIdx == rightIdx {
                let overlapStart = max(L[leftIdx], a)
                let overlapEnd = min(R[leftIdx], b)
                let len = overlapEnd - overlapStart + 1
                return len * C[leftIdx]
            } else {
                var total: LL = pref[rightIdx] - pref[leftIdx]
                // left partial
                let leftOverlapStart = max(L[leftIdx], a)
                let leftOverlapEnd = min(R[leftIdx], b)
                let leftLen = leftOverlapEnd - leftOverlapStart + 1
                total += leftLen * C[leftIdx]
                // right partial
                let rightOverlapStart = max(L[rightIdx], a)
                let rightOverlapEnd = min(R[rightIdx], b)
                let rightLen = rightOverlapEnd - rightOverlapStart + 1
                total += rightLen * C[rightIdx]
                return total
            }
        }
        var candidateSet = Set<LL>()
        for i in 0..<n {
            candidateSet.insert(L[i])
            let s2 = R[i] - LL(k) + 1
            if s2 >= 1 {
                candidateSet.insert(s2)
            }
        }
        candidateSet.insert(1)
        var candidates = Array(candidateSet)
        candidates.sort()
        var maxCoins: LL = 0
        for start in candidates {
            let end = start + LL(k) - 1
            let sum = getSum(start, end)
            if sum > maxCoins { maxCoins = sum }
        }
        return Int(maxCoins)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumCoins(coins: Array<IntArray>, k: Int): Long {
        if (coins.isEmpty()) return 0L
        val sorted = coins.sortedBy { it[0] }
        val n = sorted.size
        val L = LongArray(n)
        val R = LongArray(n)
        val C = LongArray(n)
        for (i in 0 until n) {
            L[i] = sorted[i][0].toLong()
            R[i] = sorted[i][1].toLong()
            C[i] = sorted[i][2].toLong()
        }
        val pref = LongArray(n)
        for (i in 0 until n) {
            val len = R[i] - L[i] + 1
            val total = len * C[i]
            pref[i] = if (i == 0) total else pref[i - 1] + total
        }

        fun upperBound(arr: LongArray, target: Long): Int {
            var l = 0
            var r = arr.size
            while (l < r) {
                val m = (l + r) ushr 1
                if (arr[m] <= target) {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }

        fun getSum(pos: Long): Long {
            if (n == 0 || pos < L[0]) return 0L
            val idx = upperBound(R, pos) - 1
            var sum = if (idx >= 0) pref[idx] else 0L
            val nextIdx = idx + 1
            if (nextIdx < n && L[nextIdx] <= pos) {
                sum += (pos - L[nextIdx] + 1) * C[nextIdx]
            }
            return sum
        }

        var answer = 0L
        fun evaluate(start: Long) {
            val end = start + k.toLong() - 1
            val total = getSum(end) - getSum(start - 1)
            if (total > answer) answer = total
        }

        for (i in 0 until n) {
            evaluate(L[i])
            evaluate(R[i] - k.toLong() + 1)
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximumCoins(List<List<int>> coins, int k) {
    // Sort intervals by left endpoint
    coins.sort((a, b) => a[0].compareTo(b[0]));
    int n = coins.length;
    List<int> L = List.filled(n, 0);
    List<int> R = List.filled(n, 0);
    List<int> C = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      L[i] = coins[i][0];
      R[i] = coins[i][1];
      C[i] = coins[i][2];
    }

    // Prefix sums of ci * length_i
    List<int> pref = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int weight = C[i] * (R[i] - L[i] + 1);
      pref[i] = (i == 0 ? 0 : pref[i - 1]) + weight;
    }

    // Helper binary searches
    int lowerBound(List<int> arr, int target) {
      int lo = 0, hi = arr.length;
      while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (arr[mid] >= target) {
          hi = mid;
        } else {
          lo = mid + 1;
        }
      }
      return lo; // may be n
    }

    int upperBound(List<int> arr, int target) {
      int lo = 0, hi = arr.length;
      while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (arr[mid] <= target) {
          lo = mid + 1;
        } else {
          hi = mid;
        }
      }
      return lo; // first index > target
    }

    int getSum(int s) {
      int e = s + k - 1;
      int leftIdx = lowerBound(R, s);
      int rightPos = upperBound(L, e);
      int rightIdx = rightPos - 1;

      if (leftIdx >= n || rightIdx < 0 || leftIdx > rightIdx) return 0;

      int total = pref[rightIdx];
      if (leftIdx > 0) total -= pref[leftIdx - 1];

      // Adjust left interval partial overlap
      if (L[leftIdx] < s) {
        int cut = s - L[leftIdx];
        total -= C[leftIdx] * cut;
      }

      // Adjust right interval partial overlap
      if (rightIdx != leftIdx && R[rightIdx] > e) {
        int cut = R[rightIdx] - e;
        total -= C[rightIdx] * cut;
      } else if (rightIdx == leftIdx && R[leftIdx] > e) {
        int cut = R[leftIdx] - e;
        total -= C[leftIdx] * cut;
      }

      return total;
    }

    // Generate candidate start positions
    Set<int> candSet = {};
    for (int i = 0; i < n; i++) {
      candSet.add(L[i]);
      int s2 = R[i] - k + 1;
      candSet.add(s2);
    }
    List<int> candidates = candSet.toList();
    candidates.sort();

    int best = 0;
    for (int s in candidates) {
      int cur = getSum(s);
      if (cur > best) best = cur;
    }
    return best;
  }
}
```

## Golang

```go
package main

import "sort"

func maximumCoins(coins [][]int, k int) int64 {
	type interval struct{ l, r, c int64 }
	n := len(coins)
	intervals := make([]interval, n)
	for i, v := range coins {
		intervals[i] = interval{int64(v[0]), int64(v[1]), int64(v[2])}
	}
	sort.Slice(intervals, func(i, j int) bool { return intervals[i].l < intervals[j].l })

	L := make([]int64, n)
	R := make([]int64, n)
	C := make([]int64, n)
	prefix := make([]int64, n+1)
	for i := 0; i < n; i++ {
		L[i] = intervals[i].l
		R[i] = intervals[i].r
		C[i] = intervals[i].c
		total := (R[i] - L[i] + 1) * C[i]
		prefix[i+1] = prefix[i] + total
	}

	// prefix sum of coins up to position p (inclusive)
	pref := func(p int64) int64 {
		if n == 0 || p < L[0] {
			return 0
		}
		idx := sort.Search(len(R), func(i int) bool { return R[i] > p }) - 1 // last with R <= p
		var sum int64
		if idx >= 0 {
			sum = prefix[idx+1]
		}
		next := idx + 1
		if next < n && L[next] <= p {
			sum += (p - L[next] + 1) * C[next]
		}
		return sum
	}

	candMap := make(map[int64]struct{})
	candMap[1] = struct{}{}
	k64 := int64(k)
	for i := 0; i < n; i++ {
		s1 := L[i]
		if s1 < 1 {
			s1 = 1
		}
		candMap[s1] = struct{}{}

		s2 := R[i] - k64 + 1
		if s2 < 1 {
			s2 = 1
		}
		candMap[s2] = struct{}{}
	}

	candidates := make([]int64, 0, len(candMap))
	for v := range candMap {
		candidates = append(candidates, v)
	}
	sort.Slice(candidates, func(i, j int) bool { return candidates[i] < candidates[j] })

	var ans int64
	for _, s := range candidates {
		e := s + k64 - 1
		total := pref(e) - pref(s-1)
		if total > ans {
			ans = total
		}
	}
	return ans
}
```

## Ruby

```ruby
def lower_bound(arr, target)
  l = 0
  r = arr.length
  while l < r
    m = (l + r) / 2
    if arr[m] < target
      l = m + 1
    else
      r = m
    end
  end
  l
end

def upper_bound(arr, target)
  l = 0
  r = arr.length
  while l < r
    m = (l + r) / 2
    if arr[m] <= target
      l = m + 1
    else
      r = m
    end
  end
  l
end

# @param {Integer[][]} coins
# @param {Integer} k
# @return {Integer}
def maximum_coins(coins, k)
  # sort intervals by left endpoint
  coins.sort_by! { |a| a[0] }
  n = coins.length
  l_arr = Array.new(n)
  r_arr = Array.new(n)
  c_arr = Array.new(n)
  pref = Array.new(n)

  total = 0
  (0...n).each do |i|
    li, ri, ci = coins[i]
    l_arr[i] = li
    r_arr[i] = ri
    c_arr[i] = ci
    total += ci * (ri - li + 1)
    pref[i] = total
  end

  candidates = []
  (0...n).each do |i|
    candidates << l_arr[i]
    candidates << r_arr[i] - k + 1
  end
  candidates.sort!
  uniq_candidates = []
  prev = nil
  candidates.each do |v|
    if v != prev
      uniq_candidates << v
      prev = v
    end
  end

  max_sum = 0
  uniq_candidates.each do |s|
    e = s + k - 1

    left_idx = lower_bound(r_arr, s)
    right_idx = upper_bound(l_arr, e) - 1

    if left_idx > right_idx || left_idx >= n || right_idx < 0
      sum = 0
    else
      sum = pref[right_idx] - (left_idx > 0 ? pref[left_idx - 1] : 0)

      # adjust left interval
      overlap_start = [l_arr[left_idx], s].max
      extra_before = overlap_start - l_arr[left_idx]
      sum -= extra_before * c_arr[left_idx] if extra_before > 0

      # adjust right interval
      overlap_end = [r_arr[right_idx], e].min
      extra_after = r_arr[right_idx] - overlap_end
      sum -= extra_after * c_arr[right_idx] if extra_after > 0
    end

    max_sum = sum if sum > max_sum
  end

  max_sum
end
```

## Scala

```scala
object Solution {
    def maximumCoins(coins: Array[Array[Int]], k: Int): Long = {
        val n = coins.length
        // sort intervals by left endpoint
        val sorted = coins.sortBy(_(0))
        val L = new Array[Long](n)
        val R = new Array[Long](n)
        val C = new Array[Long](n)
        for (i <- 0 until n) {
            L(i) = sorted(i)(0).toLong
            R(i) = sorted(i)(1).toLong
            C(i) = sorted(i)(2).toLong
        }
        // prefix sums of total coins per interval
        val pref = new Array[Long](n + 1)
        for (i <- 0 until n) {
            val len = R(i) - L(i) + 1
            pref(i + 1) = pref(i) + C(i) * len
        }

        // binary search helpers
        def lowerBoundR(value: Long): Int = {
            var lo = 0
            var hi = n
            while (lo < hi) {
                val mid = (lo + hi) >>> 1
                if (R(mid) >= value) hi = mid else lo = mid + 1
            }
            lo // may be n
        }

        def upperBoundL(value: Long): Int = {
            var lo = 0
            var hi = n
            while (lo < hi) {
                val mid = (lo + hi) >>> 1
                if (L(mid) <= value) lo = mid + 1 else hi = mid
            }
            lo // first index > value
        }

        def windowSum(start: Long): Long = {
            val end = start + k.toLong - 1
            var idxL = lowerBoundR(start)
            if (idxL == n || L(idxL) > end) return 0L
            var idxR = upperBoundL(end) - 1
            if (idxL > idxR) return 0L

            var sum: Long = 0L
            // fully covered intervals between edges
            if (idxL < idxR) {
                sum += pref(idxR) - pref(idxL + 1)
            }
            // left edge interval contribution
            val leftStart = math.max(L(idxL), start)
            val leftEnd   = math.min(R(idxL), end)
            if (leftEnd >= leftStart) {
                sum += C(idxL) * (leftEnd - leftStart + 1)
            }
            // right edge if different from left
            if (idxR != idxL) {
                val rightStart = math.max(L(idxR), start)
                val rightEnd   = math.min(R(idxR), end)
                if (rightEnd >= rightStart) {
                    sum += C(idxR) * (rightEnd - rightStart + 1)
                }
            }
            sum
        }

        // generate candidate starting positions
        val candidates = new scala.collection.mutable.ArrayBuffer[Long]()
        for (i <- 0 until n) {
            candidates += L(i)
            candidates += R(i) - k.toLong + 1
        }

        var best: Long = 0L
        for (s <- candidates) {
            val cur = windowSum(s)
            if (cur > best) best = cur
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_coins(coins: Vec<Vec<i32>>, k: i32) -> i64 {
        // Helper to compute total coins in [1, pos]
        fn prefix_sum(pos: i64, l: &[i64], r: &[i64], c: &[i64], pref: &[i64]) -> i64 {
            if pos <= 0 {
                return 0;
            }
            // binary search for last interval with start <= pos
            let mut lo = 0usize;
            let mut hi = l.len();
            while lo < hi {
                let mid = (lo + hi) / 2;
                if l[mid] <= pos {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            if lo == 0 {
                return 0;
            }
            let idx = lo - 1;
            if pos >= r[idx] {
                pref[idx]
            } else {
                let before = if idx == 0 { 0 } else { pref[idx - 1] };
                before + (pos - l[idx] + 1) * c[idx]
            }
        }

        // Prepare sorted intervals
        let mut intervals: Vec<(i64, i64, i64)> = coins
            .into_iter()
            .map(|v| (v[0] as i64, v[1] as i64, v[2] as i64))
            .collect();
        intervals.sort_by_key(|x| x.0);

        let n = intervals.len();
        let mut l: Vec<i64> = Vec::with_capacity(n);
        let mut r: Vec<i64> = Vec::with_capacity(n);
        let mut c: Vec<i64> = Vec::with_capacity(n);
        let mut pref: Vec<i64> = Vec::with_capacity(n);

        for (i, &(li, ri, ci)) in intervals.iter().enumerate() {
            l.push(li);
            r.push(ri);
            c.push(ci);
            let len = ri - li + 1;
            let total = len * ci;
            if i == 0 {
                pref.push(total);
            } else {
                pref.push(pref[i - 1] + total);
            }
        }

        let k64 = k as i64;
        let mut ans: i64 = 0;

        for i in 0..n {
            // Candidate start at l_i
            let s = l[i];
            let e = s + k64 - 1;
            let cur = prefix_sum(e, &l, &r, &c, &pref) - prefix_sum(s - 1, &l, &r, &c, &pref);
            if cur > ans {
                ans = cur;
            }

            // Candidate start at r_i - k + 1 (clamped to >=1)
            let mut s2 = r[i] - k64 + 1;
            if s2 < 1 {
                s2 = 1;
            }
            let e2 = s2 + k64 - 1;
            let cur2 = prefix_sum(e2, &l, &r, &c, &pref) - prefix_sum(s2 - 1, &l, &r, &c, &pref);
            if cur2 > ans {
                ans = cur2;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-coins coins k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((sorted (sort coins (lambda (a b) (< (first a) (first b)))))
         (n (length sorted))
         (L (make-vector n))
         (R (make-vector n))
         (C (make-vector n))
         (pref (make-vector n)))
    ;; fill vectors and prefix sums
    (let loop ((i 0) (lst sorted))
      (when (< i n)
        (define li (first lst))
        (define ri (second lst))
        (define ci (third lst))
        (vector-set! L i li)
        (vector-set! R i ri)
        (vector-set! C i ci)
        (let ((len (+ 1 (- ri li))))
          (if (= i 0)
              (vector-set! pref i (* len ci))
              (vector-set! pref i (+ (vector-ref pref (- i 1)) (* len ci)))))
        (loop (+ i 1) (rest lst))))
    ;; binary search helpers
    (define (lower-bound vec target)
      (let loop ((lo 0) (hi n))
        (if (= lo hi)
            lo
            (let ((mid (quotient (+ lo hi) 2)))
              (if (>= (vector-ref vec mid) target)
                  (loop lo mid)
                  (loop (+ mid 1) hi))))))
    (define (upper-bound vec target)
      (let loop ((lo 0) (hi n))
        (if (= lo hi)
            lo
            (let ((mid (quotient (+ lo hi) 2)))
              (if (> (vector-ref vec mid) target)
                  (loop lo mid)
                  (loop (+ mid 1) hi))))))
    ;; sum of coins in window [s, e]
    (define (window-sum s e)
      (let* ((idxL (lower-bound R s))
             (idxRtemp (upper-bound L e))
             (idxR (- idxRtemp 1)))
        (if (or (>= idxL n) (< idxR 0) (> idxL idxR))
            0
            (let* ((total (- (vector-ref pref idxR)
                             (if (= idxL 0) 0 (vector-ref pref (- idxL 1)))))
                   (left-excess (max 0 (- s (vector-ref L idxL))))
                   (right-excess (max 0 (- (vector-ref R idxR) e)))
                   (left-sub (* left-excess (vector-ref C idxL)))
                   (right-sub (if (= idxL idxR)
                                  (* right-excess (vector-ref C idxL))
                                  (* right-excess (vector-ref C idxR)))))
              (- total left-sub right-sub)))))
    ;; evaluate candidates
    (define max-coins 0)
    (let loop ((i 0))
      (when (< i n)
        (define s1 (vector-ref L i))
        (define s2 (- (vector-ref R i) (- k 1))) ; r - k + 1
        (let ((cand (window-sum s1 (+ s1 (- k 1)))))
          (when (> cand max-coins) (set! max-coins cand)))
        (let ((cand (window-sum s2 (+ s2 (- k 1)))))
          (when (> cand max-coins) (set! max-coins cand)))
        (loop (+ i 1))))
    max-coins))
```

## Erlang

```erlang
-spec maximum_coins(Coins :: [[integer()]], K :: integer()) -> integer().
maximum_coins(Coins, K) ->
    Sorted = lists:keysort(1, Coins),
    N = length(Sorted),

    %% Build arrays for l, r, c and prefix sums of total coins per interval
    Ls0 = array:new(N, [{default, 0}]),
    Rs0 = array:new(N, [{default, 0}]),
    Cs0 = array:new(N, [{default, 0}]),
    Prefix0 = array:new(N, [{default, 0}]),

    {Ls, Rs, Cs, Prefix} =
        build_arrays(Sorted, 0, Ls0, Rs0, Cs0, Prefix0, 0),

    %% Candidate start positions: li and (ri - K + 1) when >= 1
    Starts = collect_starts(Sorted, K),
    SortedStarts = lists:usort(Starts),

    compute_max(SortedStarts, K, Ls, Rs, Cs, Prefix).

%% ------------------------------------------------------------------
%% Build arrays with interval data and prefix sums.
%% ------------------------------------------------------------------
build_arrays([], _Idx, Ls, Rs, Cs, Prefix, _Acc) ->
    {Ls, Rs, Cs, Prefix};
build_arrays([[L, R, C] | Rest], Idx, LsAcc, RsAcc, CsAcc, PrefixAcc, Acc) ->
    Total = (R - L + 1) * C,
    NewAcc = Acc + Total,
    Ls1 = array:set(Idx, L, LsAcc),
    Rs1 = array:set(Idx, R, RsAcc),
    Cs1 = array:set(Idx, C, CsAcc),
    Prefix1 = array:set(Idx, NewAcc, PrefixAcc),
    build_arrays(Rest, Idx + 1, Ls1, Rs1, Cs1, Prefix1, NewAcc).

%% ------------------------------------------------------------------
%% Collect candidate start positions.
%% ------------------------------------------------------------------
collect_starts(CoinsSorted, K) ->
    lists:foldl(
      fun([L, R, _C], Acc) ->
              Start2 = R - K + 1,
              case Start2 >= 1 of
                  true -> [Start2, L | Acc];
                  false -> [L | Acc]
              end
          end,
      [],
      CoinsSorted).

%% ------------------------------------------------------------------
%% Compute maximum coins over all candidate starts.
%% ------------------------------------------------------------------
compute_max(StartsList, K, Ls, Rs, Cs, Prefix) ->
    N = array:size(Ls),
    lists:foldl(
      fun(Start, MaxSoFar) ->
              Sum = window_sum(Start, K, Ls, Rs, Cs, Prefix, N),
              if Sum > MaxSoFar -> Sum; true -> MaxSoFar end
          end,
      0,
      StartsList).

%% ------------------------------------------------------------------
%% Compute coins collected for a window starting at S with length K.
%% ------------------------------------------------------------------
window_sum(S, K, Ls, Rs, Cs, Prefix, N) ->
    E = S + K - 1,
    LeftIdx = first_ge(Rs, S, 0, N - 1),
    RightIdx = last_le(Ls, E, 0, N - 1),

    if
        LeftIdx > RightIdx orelse LeftIdx == N orelse RightIdx == -1 ->
            0;
        true ->
            LiL = array:get(LeftIdx, Ls),
            RiL = array:get(LeftIdx, Rs),
            CiL = array:get(LeftIdx, Cs),
            OverlapL = erlang:min(RiL, E) - erlang:max(LiL, S) + 1,

            case LeftIdx == RightIdx of
                true ->
                    OverlapL * CiL;
                false ->
                    LiR = array:get(RightIdx, Ls),
                    RiR = array:get(RightIdx, Rs),
                    CiR = array:get(RightIdx, Cs),
                    OverlapR = E - LiR + 1,

                    MidSum =
                        if LeftIdx + 1 =< RightIdx - 1 ->
                               PrefixRight = array:get(RightIdx - 1, Prefix),
                               PrefixLeft = array:get(LeftIdx, Prefix),
                               PrefixRight - PrefixLeft;
                           true -> 0
                        end,
                    OverlapL * CiL + OverlapR * CiR + MidSum
            end
    end.

%% ------------------------------------------------------------------
%% Binary search: first index with value >= Target.
%% Returns N (array size) if not found.
%% ------------------------------------------------------------------
first_ge(Array, Target, Low, High) when Low > High ->
    array:size(Array);
first_ge(Array, Target, Low, High) ->
    Mid = (Low + High) div 2,
    Val = array:get(Mid, Array),
    if
        Val >= Target ->
            first_ge(Array, Target, Low, Mid - 1);
        true ->
            first_ge(Array, Target, Mid + 1, High)
    end.

%% ------------------------------------------------------------------
%% Binary search: last index with value <= Target.
%% Returns -1 if not found.
%% ------------------------------------------------------------------
last_le(Array, Target, Low, High) when Low > High ->
    -1;
last_le(Array, Target, Low, High) ->
    Mid = (Low + High) div 2,
    Val = array:get(Mid, Array),
    if
        Val =< Target ->
            case last_le(Array, Target, Mid + 1, High) of
                -1 -> Mid;
                Res -> Res
            end;
        true ->
            last_le(Array, Target, Low, Mid - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_coins(coins :: [[integer]], k :: integer) :: integer
  def maximum_coins(coins, k) do
    sorted = Enum.sort_by(coins, fn [l, _r, _c] -> l end)

    {ls, rs, cs} =
      Enum.reduce(sorted, {[], [], []}, fn [l, r, c], {acc_l, acc_r, acc_c} ->
        {[l | acc_l], [r | acc_r], [c | acc_c]}
      end)
      |> (fn {l_rev, r_rev, c_rev} -> {Enum.reverse(l_rev), Enum.reverse(r_rev), Enum.reverse(c_rev)} end).()

    l_tuple = List.to_tuple(ls)
    r_tuple = List.to_tuple(rs)
    c_tuple = List.to_tuple(cs)

    n = tuple_size(l_tuple)

    pref_vals =
      Enum.reduce(0..(n - 1), [], fn i, acc ->
        len = elem(r_tuple, i) - elem(l_tuple, i) + 1
        val = len * elem(c_tuple, i)
        total = if acc == [], do: val, else: val + hd(acc)
        [total | acc]
      end)
      |> Enum.reverse()

    pref_tuple = List.to_tuple(pref_vals)

    candidates =
      Enum.flat_map(0..(n - 1), fn i ->
        [
          elem(l_tuple, i),
          elem(r_tuple, i) - k + 1
        ]
      end)

    Enum.reduce(candidates, 0, fn start, best ->
      sum = window_sum(start, k, l_tuple, r_tuple, c_tuple, pref_tuple, n)
      if sum > best, do: sum, else: best
    end)
  end

  defp upper_bound(r_tuple, target, low, high) do
    if low >= high do
      low
    else
      mid = div(low + high, 2)

      if elem(r_tuple, mid) <= target do
        upper_bound(r_tuple, target, mid + 1, high)
      else
        upper_bound(r_tuple, target, low, mid)
      end
    end
  end

  defp sum_up_to(pos, l_tuple, r_tuple, c_tuple, pref_tuple, n) do
    idx = upper_bound(r_tuple, pos, 0, n) - 1

    cond do
      idx < 0 ->
        if n > 0 and elem(l_tuple, 0) <= pos do
          (pos - elem(l_tuple, 0) + 1) * elem(c_tuple, 0)
        else
          0
        end

      true ->
        total = elem(pref_tuple, idx)
        next_idx = idx + 1

        if next_idx < n and elem(l_tuple, next_idx) <= pos do
          extra_len = pos - elem(l_tuple, next_idx) + 1
          total + extra_len * elem(c_tuple, next_idx)
        else
          total
        end
    end
  end

  defp window_sum(start, k, l_tuple, r_tuple, c_tuple, pref_tuple, n) do
    end_pos = start + k - 1

    sum_up_to(end_pos, l_tuple, r_tuple, c_tuple, pref_tuple, n) -
      sum_up_to(start - 1, l_tuple, r_tuple, c_tuple, pref_tuple, n)
  end
end
```

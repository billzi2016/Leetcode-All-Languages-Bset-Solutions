# 2234. Maximum Total Beauty of the Gardens

## Cpp

```cpp
class Solution {
public:
    long long maximumBeauty(vector<int>& flowers, long long newFlowers, int target, int full, int partial) {
        int n = flowers.size();
        sort(flowers.begin(), flowers.end());
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + flowers[i];
        
        // needFull[i]: total flowers needed to bring all gardens from i..n-1 up to target
        vector<long long> needFull(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            long long add = max(0LL, (long long)target - flowers[i]);
            needFull[i] = needFull[i + 1] + add;
        }
        
        // number of gardens already full
        int firstFullIdx = lower_bound(flowers.begin(), flowers.end(), target) - flowers.begin();
        int initFull = n - firstFullIdx;
        
        long long ans = 0;
        for (int k = initFull; k <= n; ++k) { // k = total number of full gardens after planting
            int idx = n - k; // size of incomplete prefix
            long long costFull = needFull[idx];
            if (costFull > newFlowers) continue;
            long long remaining = newFlowers - costFull;
            
            long long curBeauty;
            if (idx == 0) {
                curBeauty = (long long)n * full; // all gardens are full
            } else {
                int lo = 0, hi = target - 1;
                while (lo < hi) {
                    int mid = lo + (hi - lo + 1) / 2;
                    int pos = lower_bound(flowers.begin(), flowers.begin() + idx, mid) - flowers.begin();
                    long long need = (long long)mid * pos - pref[pos];
                    if (need <= remaining) lo = mid;
                    else hi = mid - 1;
                }
                curBeauty = (long long)k * full + (long long)lo * partial;
            }
            ans = max(ans, curBeauty);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        int n = flowers.length;
        java.util.Arrays.sort(flowers);
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + flowers[i];
        }
        long[] suffNeed = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            long need = Math.max(0, target - flowers[i]);
            suffNeed[i] = suffNeed[i + 1] + need;
        }
        int idx = lowerBound(flowers, target); // first position with value >= target
        long best = 0L;
        for (int i = idx; i >= 0; i--) {
            long costFull = suffNeed[i];
            if (costFull > newFlowers) continue;
            long remaining = newFlowers - costFull;
            int fullCount = n - i;
            long curBeauty = (long) full * fullCount;
            if (i == 0) { // all gardens are complete
                best = Math.max(best, curBeauty);
                continue;
            }
            int low = flowers[0];
            int high = target - 1;
            int bestMin = low;
            while (low <= high) {
                int mid = low + ((high - low) >> 1);
                int pos = upperBound(flowers, i, mid); // number of elements < =mid among first i
                long need = (long) mid * pos - pref[pos];
                if (need <= remaining) {
                    bestMin = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            curBeauty += (long) partial * bestMin;
            best = Math.max(best, curBeauty);
        }
        return best;
    }

    private int lowerBound(int[] arr, int target) {
        int l = 0, r = arr.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (arr[m] >= target) r = m;
            else l = m + 1;
        }
        return l;
    }

    private int upperBound(int[] arr, int endExclusive, int value) {
        int l = 0, r = endExclusive;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (arr[m] <= value) l = m + 1;
            else r = m;
        }
        return l;
    }
}
```

## Python

```python
class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        :type flowers: List[int]
        :type newFlowers: int
        :type target: int
        :type full: int
        :type partial: int
        :rtype: int
        """
        import bisect

        n = len(flowers)
        flowers.sort()
        # prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + flowers[i]

        # need to bring each garden to target
        need = [max(0, target - f) for f in flowers]
        suff = [0] * (n + 1)   # suff[i]: total need from i..n-1
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] + need[i]

        ans = 0

        # iterate over number of full gardens k (0..n)
        for k in range(0, n + 1):
            # cost to make last k gardens full
            if k == 0:
                cost_full = 0
            else:
                cost_full = suff[n - k]
            if cost_full > newFlowers:
                continue
            remaining = newFlowers - cost_full

            if k == n:
                ans = max(ans, n * full)
                continue

            # binary search best minimum value for the rest (capped at target-1)
            lo, hi = 0, target - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                idx = bisect.bisect_left(flowers, mid, 0, n - k)  # first >=mid in the incomplete part
                cost_min = mid * idx - pref[idx]
                if cost_min <= remaining:
                    lo = mid
                else:
                    hi = mid - 1

            min_val = lo
            beauty = k * full + min_val * partial
            ans = max(ans, beauty)

        return ans
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        # Separate already complete gardens
        incomplete = [min(f, target - 1) for f in flowers if f < target]
        initial_full = len(flowers) - len(incomplete)

        if not incomplete:
            return (initial_full) * full

        incomplete.sort()
        m = len(incomplete)

        # Prefix sums of incomplete values
        prefix = [0] * (m + 1)
        for i in range(m):
            prefix[i + 1] = prefix[i] + incomplete[i]

        # Cost to make the largest k gardens full
        full_cost = [0] * (m + 1)   # full_cost[k]: cost for last k elements
        for k in range(1, m + 1):
            idx = m - k
            need = target - incomplete[idx]
            full_cost[k] = full_cost[k - 1] + need

        best = 0
        # Iterate over possible number of newly completed gardens
        for k in range(0, m + 1):
            cost_to_full = full_cost[k]
            if cost_to_full > newFlowers:
                break
            remaining = newFlowers - cost_to_full

            if k == m:
                # all incomplete become full
                total = (initial_full + k) * full
                best = max(best, total)
                continue

            # Binary search the maximal minimal value among the rest
            lo, hi = incomplete[0], target - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                cnt = bisect.bisect_left(incomplete, mid, 0, m - k)
                need = mid * cnt - prefix[cnt]
                if need <= remaining:
                    lo = mid
                else:
                    hi = mid - 1

            min_val = lo
            total = (initial_full + k) * full + min_val * partial
            best = max(best, total)

        return best
```

## C

```c
#include <stdlib.h>

static int cmp_ll(const void *p1, const void *p2) {
    long long a = *(const long long *)p1;
    long long b = *(const long long *)p2;
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
}

static int upperBound(const long long *a, int len, long long val) {
    int l = 0, r = len;
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (a[m] <= val)
            l = m + 1;
        else
            r = m;
    }
    return l;
}

long long maximumBeauty(int* flowers, int flowersSize, long long newFlowers, int target, int full, int partial) {
    int n = flowersSize;
    long long *arr = (long long *)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; ++i) arr[i] = flowers[i];
    qsort(arr, n, sizeof(long long), cmp_ll);

    long long *pref = (long long *)malloc(sizeof(long long) * (n + 1));
    pref[0] = 0;
    for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + arr[i];

    long long *suffB = (long long *)malloc(sizeof(long long) * (n + 1));
    suffB[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        long long capped = arr[i] < target ? arr[i] : target;
        suffB[i] = suffB[i + 1] + capped;
    }

    long long ans = 0;
    for (int k = 0; k <= n; ++k) {
        // cost to make last k gardens complete
        long long needComplete = (long long)k * target - suffB[n - k];
        if (needComplete > newFlowers) continue;

        long long remain = newFlowers - needComplete;
        int m = n - k;  // number of incomplete gardens

        if (m == 0) {
            long long cand = (long long)full * n;
            if (cand > ans) ans = cand;
            continue;
        }

        long long low = 0, high = target - 1, best = 0;
        while (low <= high) {
            long long mid = (low + high) >> 1;
            int pos = upperBound(arr, m, mid); // number of elements <= mid
            long long costRaise = mid * (long long)pos - pref[pos];
            if (costRaise <= remain) {
                best = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        long long cand = (long long)k * full + best * partial;
        if (cand > ans) ans = cand;
    }

    free(arr);
    free(pref);
    free(suffB);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MaximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        int n = flowers.Length;
        Array.Sort(flowers);
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + flowers[i];
        }

        // suffixCost[k]: cost to make last k gardens reach target
        long[] suffixCost = new long[n + 1];
        suffixCost[0] = 0;
        for (int k = 1; k <= n; k++) {
            int idx = n - k;
            long need = Math.Max(0L, (long)target - flowers[idx]);
            suffixCost[k] = suffixCost[k - 1] + need;
        }

        // first index where value >= target
        int posTarget = LowerBound(flowers, target);

        long answer = 0;

        for (int k = 0; k <= n; k++) {
            if (suffixCost[k] > newFlowers) continue;
            long remaining = newFlowers - suffixCost[k];
            int remainCount = n - k;

            // number of already complete gardens in the remaining prefix
            int extraFull = Math.Max(0, remainCount - posTarget);
            int incompleteCnt = Math.Min(remainCount, posTarget); // those < target

            if (incompleteCnt == 0) {
                // all gardens are complete
                answer = Math.Max(answer, (long)full * n);
                continue;
            }

            if (partial == 0) {
                long total = (long)full * (k + extraFull);
                answer = Math.Max(answer, total);
                continue;
            }

            int low = 0;
            int high = target - 1;
            int bestX = 0;

            while (low <= high) {
                int mid = low + ((high - low) >> 1);
                int idx = UpperBound(flowers, 0, incompleteCnt, mid); // first >mid
                long cost = (long)mid * idx - prefix[idx];
                if (cost <= remaining) {
                    bestX = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }

            long totalBeauty = (long)full * (k + extraFull) + (long)partial * bestX;
            answer = Math.Max(answer, totalBeauty);
        }

        return answer;
    }

    private int LowerBound(int[] arr, int value) {
        int l = 0, r = arr.Length;
        while (l < r) {
            int m = (l + r) >> 1;
            if (arr[m] < value) l = m + 1;
            else r = m;
        }
        return l;
    }

    private int UpperBound(int[] arr, int start, int length, int value) {
        int l = start, r = start + length;
        while (l < r) {
            int m = (l + r) >> 1;
            if (arr[m] <= value) l = m + 1;
            else r = m;
        }
        return l;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} flowers
 * @param {number} newFlowers
 * @param {number} target
 * @param {number} full
 * @param {number} partial
 * @return {number}
 */
var maximumBeauty = function(flowers, newFlowers, target, full, partial) {
    let initFull = 0;
    const arr = [];
    for (const f of flowers) {
        if (f >= target) initFull++;
        else arr.push(f);
    }
    const n = arr.length;
    if (n === 0) return initFull * full; // all already complete

    arr.sort((a, b) => a - b);

    const prefix = new Array(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }

    const need = new Array(n);
    for (let i = 0; i < n; i++) need[i] = target - arr[i]; // positive

    const suffixNeed = new Array(n + 1);
    suffixNeed[0] = 0;
    for (let k = 1; k <= n; k++) {
        suffixNeed[k] = suffixNeed[k - 1] + need[n - k];
    }

    let ans = 0;

    for (let k = 0; k <= n; k++) {
        const costComplete = suffixNeed[k];
        if (costComplete > newFlowers) continue;
        const remaining = newFlowers - costComplete;
        const totalFull = initFull + k;

        if (k === n) {
            ans = Math.max(ans, totalFull * full);
            continue;
        }

        const cnt = n - k; // number of gardens left incomplete
        let low = arr[0];
        let high = target - 1;
        let bestMin = low;

        while (low <= high) {
            const mid = Math.floor((low + high) / 2);
            // find how many of the first cnt elements are < mid
            let l = 0, r = cnt;
            while (l < r) {
                const m = (l + r) >> 1;
                if (arr[m] < mid) l = m + 1;
                else r = m;
            }
            const idx = l; // count of elements < mid
            const cost = mid * idx - prefix[idx];
            if (cost <= remaining) {
                bestMin = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        const beauty = totalFull * full + bestMin * partial;
        ans = Math.max(ans, beauty);
    }

    return ans;
};
```

## Typescript

```typescript
function maximumBeauty(flowers: number[], newFlowers: number, target: number, full: number, partial: number): number {
    const n = flowers.length;
    // Count already complete gardens
    let initialFull = 0;
    const incomplete: number[] = [];
    for (const f of flowers) {
        if (f >= target) {
            initialFull++;
        } else {
            incomplete.push(f);
        }
    }
    // If all are already full
    if (incomplete.length === 0) return n * full;

    incomplete.sort((a, b) => a - b);
    const m = incomplete.length;
    const pref = new Array(m + 1).fill(0);
    for (let i = 0; i < m; i++) pref[i + 1] = pref[i] + incomplete[i];

    // suffixCost[i]: cost to bring gardens i..m-1 up to target
    const suffixCost = new Array(m + 1).fill(0);
    for (let i = m - 1; i >= 0; i--) {
        const need = target - incomplete[i];
        suffixCost[i] = suffixCost[i + 1] + need;
    }

    let answer = initialFull * full; // at least this much

    for (let k = 0; k <= m; k++) { // make k additional gardens full
        const costFull = suffixCost[m - k];
        if (costFull > newFlowers) continue;
        const remaining = newFlowers - costFull;

        if (k === m) {
            // all become full
            answer = Math.max(answer, (initialFull + m) * full);
            continue;
        }

        const leftCount = m - k; // gardens that stay incomplete
        // binary search max minimal value (capped at target-1)
        let low = incomplete[0];
        let high = target - 1;
        if (low > high) {
            // all remaining already >= target, shouldn't happen here
            answer = Math.max(answer, (initialFull + k) * full);
            continue;
        }
        while (low < high) {
            const mid = Math.floor((low + high + 1) / 2);
            // find first index > mid in [0, leftCount)
            let l = 0, r = leftCount;
            while (l < r) {
                const md = (l + r) >> 1;
                if (incomplete[md] <= mid) l = md + 1; else r = md;
            }
            const idx = l; // number of elements <= mid
            const cost = mid * idx - pref[idx];
            if (cost <= remaining) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        const minVal = low;
        const totalBeauty = (initialFull + k) * full + minVal * partial;
        answer = Math.max(answer, totalBeauty);
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $flowers
     * @param Integer $newFlowers
     * @param Integer $target
     * @param Integer $full
     * @param Integer $partial
     * @return Integer
     */
    function maximumBeauty($flowers, $newFlowers, $target, $full, $partial) {
        $alreadyFull = 0;
        $filtered = [];
        foreach ($flowers as $f) {
            if ($f >= $target) {
                $alreadyFull++;
            } else {
                $filtered[] = $f;
            }
        }

        $n = count($filtered);
        if ($n == 0) {
            return $alreadyFull * $full;
        }

        sort($filtered); // ascending

        // prefix sums
        $pre = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pre[$i + 1] = $pre[$i] + $filtered[$i];
        }

        // suffix cost to make k gardens full (choose largest ones)
        $suff = array_fill(0, $n + 1, 0);
        for ($k = 1; $k <= $n; $k++) {
            $idx = $n - $k;
            $need = $target - $filtered[$idx];
            if ($need < 0) $need = 0;
            $suff[$k] = $suff[$k - 1] + $need;
        }

        $ans = 0;
        $limitMin = $target - 1;

        // helper to count elements less than value within first $len items
        $countLessThan = function($arr, $len, $value) {
            $l = 0; $r = $len;
            while ($l < $r) {
                $m = intdiv($l + $r, 2);
                if ($arr[$m] < $value) {
                    $l = $m + 1;
                } else {
                    $r = $m;
                }
            }
            return $l;
        };

        for ($k = 0; $k <= $n; $k++) {
            // cost to make $k largest gardens full
            if ($suff[$k] > $newFlowers) continue;
            $remain = $newFlowers - $suff[$k];

            if ($k == $n) { // all become full
                $beauty = ($alreadyFull + $n) * $full;
                if ($beauty > $ans) $ans = $beauty;
                continue;
            }

            // binary search best minimum for remaining (n - k) gardens
            $low = 0;
            $high = $limitMin;
            while ($low <= $high) {
                $mid = intdiv($low + $high, 2);
                $len = $n - $k; // number of gardens not forced full
                $cnt = $countLessThan($filtered, $len, $mid);
                $cost = $mid * $cnt - $pre[$cnt];
                if ($cost <= $remain) {
                    $low = $mid + 1;
                } else {
                    $high = $mid - 1;
                }
            }
            $bestMin = $high; // maximum feasible minimum
            $beauty = ($alreadyFull + $k) * $full + $bestMin * $partial;
            if ($beauty > $ans) $ans = $beauty;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumBeauty(_ flowers: [Int], _ newFlowers: Int, _ target: Int, _ full: Int, _ partial: Int) -> Int {
        let n = flowers.count
        var sorted = flowers.sorted()
        // Prefix sums as Int64
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(sorted[i])
        }
        // Suffix cost to make full
        var needFull = [Int64](repeating: 0, count: n + 1) // needFull[i]: cost for i..n-1
        for i in stride(from: n - 1, through: 0, by: -1) {
            let add = max(0, target - sorted[i])
            needFull[i] = needFull[i + 1] + Int64(add)
        }
        
        func lowerBound(_ arr: [Int], _ value: Int, _ hi: Int) -> Int {
            var l = 0
            var r = hi
            while l < r {
                let m = (l + r) >> 1
                if arr[m] < value {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }
        
        let newFlowers64 = Int64(newFlowers)
        var answer: Int64 = 0
        
        for k in 0...n { // k gardens become full (the largest k)
            let startIdx = n - k          // first index of incomplete part
            let costFull = needFull[startIdx]
            if costFull > newFlowers64 { continue }
            var remaining = newFlowers64 - costFull
            
            if startIdx == 0 {
                // all gardens are full
                let beauty = Int64(k) * Int64(full)
                answer = max(answer, beauty)
                continue
            }
            
            var low: Int64 = 0
            var high: Int64 = Int64(target - 1)
            while low < high {
                let mid = (low + high + 1) >> 1
                let pos = lowerBound(sorted, Int(mid), startIdx) // number of elements < mid
                let need = mid * Int64(pos) - prefix[pos]
                if need <= remaining {
                    low = mid
                } else {
                    high = mid - 1
                }
            }
            let minVal = low
            let beauty = Int64(k) * Int64(full) + minVal * Int64(partial)
            answer = max(answer, beauty)
        }
        
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumBeauty(flowers: IntArray, newFlowers: Long, target: Int, full: Int, partial: Int): Long {
        val n = flowers.size
        val arr = flowers.map { it.toLong() }.sorted()
        val pref = LongArray(n)
        for (i in 0 until n) {
            pref[i] = (if (i > 0) pref[i - 1] else 0L) + arr[i]
        }
        // needFull[i]: total flowers needed to make all gardens from i..n-1 full
        val needFull = LongArray(n + 1)
        for (i in n - 1 downTo 0) {
            val need = if (arr[i] >= target) 0L else (target - arr[i])
            needFull[i] = needFull[i + 1] + need
        }
        var answer = 0L
        for (k in 0..n) { // k gardens will be full (the largest ones)
            val idx = n - k // first index of incomplete part
            val costFull = needFull[idx]
            if (costFull > newFlowers) continue
            val remaining = newFlowers - costFull
            if (idx == 0) {
                // all gardens are full
                answer = maxOf(answer, k.toLong() * full)
                continue
            }
            var low = 0L
            var high = (target - 1).toLong()
            while (low <= high) {
                val mid = (low + high) ushr 1
                // find number of elements <= mid in arr[0..idx-1]
                var l = 0
                var r = idx
                while (l < r) {
                    val m = (l + r) ushr 1
                    if (arr[m] <= mid) {
                        l = m + 1
                    } else {
                        r = m
                    }
                }
                val pos = l // count of elements <= mid
                val cost = mid * pos - if (pos > 0) pref[pos - 1] else 0L
                if (cost <= remaining) {
                    low = mid + 1
                } else {
                    high = mid - 1
                }
            }
            val minVal = high
            val beauty = k.toLong() * full + minVal * partial
            answer = maxOf(answer, beauty)
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximumBeauty(List<int> flowers, int newFlowers, int target, int full, int partial) {
    int n = flowers.length;
    flowers.sort();
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + flowers[i];
    }

    // need to make each garden reach target
    List<int> need = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      need[i] = flowers[i] >= target ? 0 : target - flowers[i];
    }
    // suffix sum of needs
    List<int> suffNeed = List.filled(n + 1, 0); // suffNeed[i] = sum_{j=i}^{n-1} need[j]
    for (int i = n - 1; i >= 0; --i) {
      suffNeed[i] = suffNeed[i + 1] + need[i];
    }

    int ans = 0;
    // iterate over possible number of full gardens k
    for (int k = 0; k <= n; ++k) {
      int startIdx = n - k; // index where the suffix of size k begins
      int costFull = suffNeed[startIdx];
      if (costFull > newFlowers) continue;
      int remaining = newFlowers - costFull;

      if (k == n) {
        ans = _max(ans, n * full);
        continue;
      }

      // binary search best minimal value for the first n-k gardens
      int low = flowers[0];
      int high = target - 1;
      int best = low; // at least current minimum
      while (low <= high) {
        int mid = ((low + high) >> 1);
        int pos = _upperBound(flowers, mid, 0, startIdx); // first >mid in [0,startIdx)
        long cost = (mid * pos) - prefix[pos];
        if (cost <= remaining) {
          best = mid;
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }

      int beauty = k * full + best * partial;
      ans = _max(ans, beauty);
    }
    return ans;
  }

  int _upperBound(List<int> arr, int value, int left, int right) {
    // returns first index in [left,right) where arr[idx] > value
    while (left < right) {
      int mid = ((left + right) >> 1);
      if (arr[mid] <= value) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }

  int _max(int a, int b) => a > b ? a : b;
}
```

## Golang

```go
package main

import (
	"sort"
)

func maximumBeauty(flowers []int, newFlowers int64, target int, full int, partial int) int64 {
	sort.Ints(flowers)
	n := len(flowers)

	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(flowers[i])
	}

	suffCost := make([]int64, n+1) // suffCost[n]=0
	for i := n - 1; i >= 0; i-- {
		need := 0
		if flowers[i] < target {
			need = target - flowers[i]
		}
		suffCost[i] = suffCost[i+1] + int64(need)
	}

	var ans int64 = 0

	for i := n; i >= 0; i-- { // i is start index of suffix to be completed
		cntComplete := n - i
		costComplete := suffCost[i]
		if costComplete > newFlowers {
			continue
		}
		leftover := newFlowers - costComplete

		if i == 0 { // all gardens are complete
			total := int64(cntComplete) * int64(full)
			if total > ans {
				ans = total
			}
			continue
		}

		lo := flowers[0]
		hi := target - 1
		if lo > hi {
			lo = hi
		}
		for lo < hi {
			mid := (lo + hi + 1) / 2
			idx := sort.Search(i, func(j int) bool { return flowers[j] > mid })
			cntLow := idx
			costNeeded := int64(mid)*int64(cntLow) - pref[idx]
			if costNeeded <= leftover {
				lo = mid
			} else {
				hi = mid - 1
			}
		}
		minVal := lo
		total := int64(cntComplete)*int64(full) + int64(minVal)*int64(partial)
		if total > ans {
			ans = total
		}
	}

	return ans
}
```

## Ruby

```ruby
def maximum_beauty(flowers, new_flowers, target, full, partial)
  # Gardens already complete
  base_full = flowers.count { |v| v >= target }

  # Gardens that are not yet complete
  arr = flowers.select { |v| v < target }.sort
  n = arr.length
  return base_full * full if n == 0

  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + arr[i] }

  max_beauty = 0

  # Try making k additional gardens complete
  (0..n).each do |k|
    sum_last_k = k.zero? ? 0 : (prefix[n] - prefix[n - k])
    need_full = k * target - sum_last_k
    break if need_full > new_flowers && k > 0

    remaining = new_flowers - need_full
    m = n - k   # number of gardens still incomplete

    if m.zero?
      total = (base_full + k) * full
      max_beauty = [max_beauty, total].max
      next
    end

    low = arr[0]
    high = target - 1
    best = low

    while low <= high
      mid = (low + high) / 2

      # count of elements < mid among first m elements
      l = 0
      r = m
      while l < r
        mm = (l + r) / 2
        if arr[mm] < mid
          l = mm + 1
        else
          r = mm
        end
      end
      cnt = l
      cost = mid * cnt - prefix[cnt]

      if cost <= remaining
        best = mid
        low = mid + 1
      else
        high = mid - 1
      end
    end

    total = (base_full + k) * full + best * partial
    max_beauty = [max_beauty, total].max
  end

  max_beauty
end
```

## Scala

```scala
object Solution {
  def maximumBeauty(flowers: Array[Int], newFlowers: Long, target: Int, full: Int, partial: Int): Long = {
    val n = flowers.length
    val arr = flowers.map(_.toLong).sorted

    // prefix sums of sorted array
    val pref = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + arr(i)
      i += 1
    }

    // needFull(k): flowers needed to make the k largest gardens full
    val needFull = new Array[Long](n + 1)
    var sumNeed = 0L
    needFull(0) = 0L
    var k = 1
    while (k <= n) {
      val idx = n - k
      if (arr(idx) < target) sumNeed += target - arr(idx)
      needFull(k) = sumNeed
      k += 1
    }

    var ans = 0L
    var fullCnt = 0
    while (fullCnt <= n) {
      val costFull = needFull(fullCnt)
      if (costFull <= newFlowers) {
        val remaining = newFlowers - costFull
        if (fullCnt == n) {
          ans = math.max(ans, n.toLong * full)
        } else {
          var lo = 0L
          var hi = target - 1L
          while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            // count of elements < mid among the first n-fullCnt gardens
            var l = 0
            var r = n - fullCnt
            while (l < r) {
              val m = (l + r) >>> 1
              if (arr(m) < mid) l = m + 1 else r = m
            }
            val cnt = l
            val cost = mid * cnt - pref(cnt)
            if (cost <= remaining) lo = mid else hi = mid - 1
          }
          val totalBeauty = fullCnt.toLong * full + lo * partial
          ans = math.max(ans, totalBeauty)
        }
      }
      fullCnt += 1
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_beauty(
        flowers: Vec<i32>,
        new_flowers: i64,
        target: i32,
        full: i32,
        partial: i32,
    ) -> i64 {
        let n = flowers.len();
        if n == 0 {
            return 0;
        }
        let mut a: Vec<i64> = flowers.into_iter().map(|x| x as i64).collect();
        a.sort_unstable();

        // prefix sums
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + a[i];
        }

        let t = target as i64;
        // need to bring each garden up to target
        let mut need = vec![0i64; n];
        for i in 0..n {
            if a[i] < t {
                need[i] = t - a[i];
            }
        }
        // suffix sums of need
        let mut suff = vec![0i64; n + 1];
        for i in (0..n).rev() {
            suff[i] = suff[i + 1] + need[i];
        }

        let full_i = full as i64;
        let partial_i = partial as i64;
        let limit = t - 1; // maximum possible minimum among incomplete gardens
        let mut ans: i64 = 0;

        for k in 0..=n {
            let idx = n - k; // first index of the incomplete segment
            let cost_complete = suff[idx];
            if cost_complete > new_flowers {
                continue;
            }
            let remaining = new_flowers - cost_complete;
            if k == n {
                ans = ans.max(full_i * n as i64);
                continue;
            }

            // binary search the highest achievable minimum value (<= limit)
            let mut lo = 0i64;
            let mut hi = limit;
            while lo < hi {
                let mid = (lo + hi + 1) / 2;
                // count of elements <= mid in a[0..idx]
                let mut l = 0usize;
                let mut r = idx;
                while l < r {
                    let m = (l + r) / 2;
                    if a[m] <= mid {
                        l = m + 1;
                    } else {
                        r = m;
                    }
                }
                let pos = l; // number of elements that need to be raised
                let cost = mid * (pos as i64) - pref[pos];
                if cost <= remaining {
                    lo = mid;
                } else {
                    hi = mid - 1;
                }
            }

            let candidate = full_i * k as i64 + partial_i * lo;
            ans = ans.max(candidate);
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-beauty flowers newFlowers target full partial)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((sorted (list->vector (sort flowers <)))
         (n (vector-length sorted))
         ;; prefix sums
         (pref (make-vector (+ n 1) 0))
         ( _ (for ([i (in-range n)])
                (vector-set! pref (+ i 1)
                             (+ (vector-ref pref i) (vector-ref sorted i)))))
         ;; suffix cost: cost to make last k gardens reach target
         (suffix (make-vector (+ n 1) 0))
         (_ (let loop ((i (- n 1)) (k 1) (acc 0))
              (when (>= i 0)
                (let* ((need (max 0 (- target (vector-ref sorted i))))
                       (new-acc (+ acc need)))
                  (vector-set! suffix k new-acc)
                  (loop (- i 1) (+ k 1) new-acc)))))
         ;; upper-bound: first index >= x within first len elements
         (upper-bound
          (lambda (len x)
            (let loop ((l 0) (r len))
              (if (= l r)
                  l
                  (let ((mid (quotient (+ l r) 2)))
                    (if (< (vector-ref sorted mid) x)
                        (loop (+ mid 1) r)
                        (loop l mid))))))))
    (let ((ans (make-parameter 0)))
      (for ([k (in-range 0 (+ n 1))])
        (let ((costK (vector-ref suffix k)))
          (when (<= costK newFlowers)
            (define remaining (- newFlowers costK))
            (define full-beauty (* full k))
            (if (= k n)
                (ans (max (ans) (+ full-beauty 0))) ; all complete
                (let* ((m (- n k))
                       ;; binary search max minimal value (capped at target-1)
                       (best-min
                        (let loop ((l 0) (h (- target 1)) (best 0))
                          (if (> l h)
                              best
                              (let* ((mid (quotient (+ l h) 2))
                                     (idx (upper-bound m mid))
                                     (need (- (* mid idx) (vector-ref pref idx))))
                                (if (<= need remaining)
                                    (loop (+ mid 1) h mid)
                                    (loop l (- mid 1) best)))))))
                  (ans (max (ans) (+ full-beauty (* partial best-min)))))))))
      (ans))))
```

## Erlang

```erlang
-spec maximum_beauty(Flowers :: [integer()], NewFlowers :: integer(), Target :: integer(), Full :: integer(), Partial :: integer()) -> integer().
maximum_beauty(Flowers, NewFlowers, Target, Full, Partial) ->
    % Count already complete gardens and collect the rest
    FullCount = length([X || X <- Flowers, X >= Target]),
    RestList  = [X || X <- Flowers, X < Target],
    SortedRest = lists:sort(RestList),
    N = length(SortedRest),

    case N of
        0 ->
            Full * FullCount;
        _ ->
            SortedTuple = list_to_tuple(SortedRest),
            PrefTuple   = build_prefix_tuple(SortedRest),
            NeedList    = [Target - V || V <- SortedRest],
            SufTuple    = build_suffix_need_tuple(NeedList),

            MaxBeauty = max_beauty_loop(
                0,                     % k
                0,                     % current best
                FullCount,
                SortedTuple,
                PrefTuple,
                SufTuple,
                NewFlowers,
                Target,
                Full,
                Partial,
                N),

            MaxBeauty
    end.

%% Build prefix sums tuple: index i (0‑based) -> sum of first i elements, pref[0]=0
build_prefix_tuple(List) ->
    {RevPref,_} = lists:foldl(
        fun(V,{Acc,Sum}) ->
            NewSum = Sum + V,
            {[NewSum|Acc], NewSum}
        end,
        {[],0},
        List),
    PrefVals = lists:reverse(RevPref),          % sums for each element
    FullPref = [0 | PrefVals],
    list_to_tuple(FullPref).

%% Build suffix need tuple: index k (0‑based) -> sum of last k needs, suf[0]=0
build_suffix_need_tuple(NeedList) ->
    Rev = lists:reverse(NeedList),
    {_, RevAcc} = lists:foldl(
        fun(V,{Sum,Acc}) ->
            NewSum = Sum + V,
            {NewSum, [NewSum|Acc]}
        end,
        {0, []},
        Rev),
    SufList = [0 | lists:reverse(RevAcc)],
    list_to_tuple(SufList).

%% Main loop over k (number of gardens we turn into full)
max_beauty_loop(K, MaxBeauty, FullCount, SortedTuple, PrefTuple, SufTuple,
                NewFlowers, Target, Full, Partial, N) when K =< N ->
    CostComplete = element(K+1, SufTuple),
    if
        CostComplete > NewFlowers ->
            MaxBeauty;  % further k will only need more flowers
        true ->
            Remaining = NewFlowers - CostComplete,
            M = N - K,
            TotalFull = FullCount + K,
            Beauty =
                case M of
                    0 -> Full * TotalFull;
                    _ ->
                        BestMin = max_min(Remaining, SortedTuple, PrefTuple, M, Target-1),
                        Full * TotalFull + Partial * BestMin
                end,
            NewMax = if Beauty > MaxBeauty -> Beauty; true -> MaxBeauty end,
            max_beauty_loop(K+1, NewMax, FullCount, SortedTuple, PrefTuple,
                            SufTuple, NewFlowers, Target, Full, Partial, N)
    end;
max_beauty_loop(_, MaxBeauty, _, _, _, _, _, _, _, _, _) ->
    MaxBeauty.

%% Find maximal minimal value for incomplete gardens
max_min(Remaining, SortedTuple, PrefTuple, Len, MaxVal) ->
    bs_max_min(0, MaxVal, Remaining, SortedTuple, PrefTuple, Len).

bs_max_min(Low, High, Rem, Tuple, Pref, Len) when Low < High ->
    Mid = (Low + High + 1) div 2,
    Cost = cost_to_raise(Mid, Tuple, Pref, Len),
    if
        Cost =< Rem -> bs_max_min(Mid, High, Rem, Tuple, Pref, Len);
        true       -> bs_max_min(Low, Mid-1, Rem, Tuple, Pref, Len)
    end;
bs_max_min(Low, _High, _Rem, _Tuple, _Pref, _Len) ->
    Low.

%% Cost to raise first 'len' elements up to Val
cost_to_raise(Val, SortedTuple, PrefTuple, Len) ->
    Idx = upper_bound(SortedTuple, Len, Val),
    SumPref = element(Idx+1, PrefTuple),   % pref[Idx]
    Val * Idx - SumPref.

%% Upper bound: number of elements <= Val in first Len entries
upper_bound(Tuple, Len, Val) ->
    ub_loop(0, Len, Tuple, Val).

ub_loop(Low, High, _Tuple, _Val) when Low >= High ->
    Low;
ub_loop(Low, High, Tuple, Val) ->
    Mid = (Low + High) div 2,
    Elem = element(Mid+1, Tuple),
    if
        Elem =< Val -> ub_loop(Mid+1, High, Tuple, Val);
        true       -> ub_loop(Low, Mid, Tuple, Val)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_beauty(flowers :: [integer], new_flowers :: integer, target :: integer, full :: integer, partial :: integer) :: integer
  def maximum_beauty(flowers, new_flowers, target, full, partial) do
    # cap values at target and sort
    capped =
      flowers
      |> Enum.map(fn x -> if x > target, do: target, else: x end)
      |> Enum.sort()

    n = length(capped)
    arr = List.to_tuple(capped)

    # prefix sums
    {pref_rev, _} =
      0..(n - 1)
      |> Enum.reduce({[], 0}, fn idx, {list, sum} ->
        v = elem(arr, idx)
        new_sum = sum + v
        {[new_sum | list], new_sum}
      end)

    pref_list = [0 | Enum.reverse(pref_rev)]
    pref = List.to_tuple(pref_list)

    # suffix need to reach target
    {suffix_rev, _} =
      (n - 1)..0
      |> Enum.reduce({[], 0}, fn idx, {list, sum} ->
        need = target - elem(arr, idx)
        new_sum = sum + need
        {[new_sum | list], new_sum}
      end)

    suffix_list = suffix_rev ++ [0]
    suffix = List.to_tuple(suffix_list)

    # main iteration over possible number of complete gardens k
    0..n
    |> Enum.reduce(0, fn k, best_ans ->
      cost_complete = elem(suffix, n - k)

      if cost_complete > new_flowers do
        best_ans
      else
        remaining = new_flowers - cost_complete
        len = n - k

        total_beauty =
          if len == 0 do
            n * full
          else
            min_val = max_min(arr, pref, len, remaining, target)
            k * full + min_val * partial
          end

        if total_beauty > best_ans, do: total_beauty, else: best_ans
      end
    end)
  end

  # binary search for the highest achievable minimum value among first `len` gardens
  defp max_min(arr, pref, len, remaining, target) do
    do_max_min(arr, pref, len, remaining, 0, target - 1, 0)
  end

  defp do_max_min(_arr, _pref, _len, _remaining, low, high, best) when low > high,
    do: best

  defp do_max_min(arr, pref, len, remaining, low, high, _best) do
    mid = div(low + high, 2)
    cnt = upper_bound(arr, len, mid)
    cost = mid * cnt - elem(pref, cnt)

    if cost <= remaining do
      do_max_min(arr, pref, len, remaining, mid + 1, high, mid)
    else
      do_max_min(arr, pref, len, remaining, low, mid - 1, 0)
    end
  end

  # number of elements in arr[0..len-1] that are < val
  defp upper_bound(arr, len, val), do: ub(arr, 0, len, val)

  defp ub(_arr, lo, hi, _val) when lo >= hi, do: lo

  defp ub(arr, lo, hi, val) do
    mid = div(lo + hi, 2)

    if elem(arr, mid) < val do
      ub(arr, mid + 1, hi, val)
    else
      ub(arr, lo, mid, val)
    end
  end
end
```

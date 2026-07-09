# 1712. Ways to Split Array Into Three Subarrays

## Cpp

```cpp
class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        int n = nums.size();
        vector<long long> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) pre[i + 1] = pre[i] + nums[i];
        long long total = pre[n];
        long long ans = 0;
        int lo = 0, hi = 0;
        for (int k = 1; k <= n - 2; ++k) {
            // left bound: pre[lo] >= 2*pre[k] - total
            while (lo < k && pre[lo] < 2 * pre[k] - total) ++lo;
            // right bound: pre[hi] <= pre[k]/2, maximize hi
            while (hi + 1 < k && pre[hi + 1] <= pre[k] / 2) ++hi;
            if (hi >= lo) {
                ans += (hi - lo + 1);
                if (ans >= MOD) ans %= MOD;
            }
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    public int waysToSplit(int[] nums) {
        int n = nums.length;
        long[] pre = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pre[i + 1] = pre[i] + nums[i];
        }
        long total = pre[n];
        final long MOD = 1_000_000_007L;
        long ans = 0;
        int low = 2, high = 2; // pointers for the middle split position j
        for (int i = 1; i <= n - 2; i++) {
            if (low < i + 1) low = i + 1;
            if (high < i + 1) high = i + 1;
            while (low <= n - 1 && pre[low] - pre[i] < pre[i]) {
                low++;
            }
            while (high <= n - 1 && pre[high] - pre[i] <= total - pre[high]) {
                high++;
            }
            int leftBound = low;
            int rightBound = high - 1;
            if (rightBound >= leftBound) {
                ans += (rightBound - leftBound + 1);
                ans %= MOD;
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from itertools import accumulate
        from bisect import bisect_left, bisect_right

        MOD = 10**9 + 7
        n = len(nums)
        prefix = list(accumulate(nums))
        total = prefix[-1]
        ans = 0

        for i in range(n - 2):
            # first part ends at i, need j > i and j < n-1
            left = i + 1
            right_limit = n - 2  # maximum valid j index

            # condition sum2 >= sum1 -> prefix[j] >= 2*prefix[i]
            targetL = 2 * prefix[i]
            L = bisect_left(prefix, targetL, lo=left, hi=n-1)

            # condition sum2 <= sum3 -> 2*prefix[j] <= total + prefix[i]
            targetR = (total + prefix[i]) // 2
            R = bisect_right(prefix, targetR, lo=left, hi=n-1) - 1

            if L <= R and L <= right_limit:
                # clamp R to the allowed maximum index
                if R > right_limit:
                    R = right_limit
                ans += (R - L + 1)
                if ans >= MOD:
                    ans -= MOD

        return ans % MOD
```

## Python3

```python
class Solution:
    def waysToSplit(self, nums):
        from bisect import bisect_left, bisect_right
        MOD = 10**9 + 7
        n = len(nums)
        pref = [0] * n
        s = 0
        for i, v in enumerate(nums):
            s += v
            pref[i] = s
        total = s
        ans = 0
        for j in range(2, n):
            # middle subarray ends at j-1, third starts at j
            mid_sum = pref[j - 1]
            # lower bound for left sum: >= 2*mid_sum - total
            low_val = 2 * mid_sum - total
            if low_val < 0:
                low_val = 0
            left_idx = bisect_left(pref, low_val, 0, j - 1)
            # upper bound for left sum: <= mid_sum // 2
            high_val = mid_sum // 2
            right_idx = bisect_right(pref, high_val, 0, j - 1) - 1
            if left_idx <= right_idx:
                ans += (right_idx - left_idx + 1)
        return ans % MOD
```

## C

```c
#include <stdlib.h>

int waysToSplit(int* nums, int numsSize) {
    const int MOD = 1000000007;
    long long *pref = (long long*)malloc((numsSize + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < numsSize; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }
    long long total = pref[numsSize];
    long long ans = 0;

    for (int i = 1; i <= numsSize - 2; ++i) {
        long long leftSum = pref[i];

        // Find smallest j such that sum(mid) >= leftSum
        int lo = i + 1, hi = numsSize - 1, lPos = -1;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            long long midSum = pref[mid] - pref[i];
            if (midSum >= leftSum) {
                lPos = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        // Find largest j such that sum(right) >= sum(mid)
        lo = i + 1; hi = numsSize - 1;
        int rPos = -1;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            long long midSum = pref[mid] - pref[i];
            long long rightSum = total - pref[mid];
            if (rightSum >= midSum) {
                rPos = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        if (lPos != -1 && rPos != -1 && lPos <= rPos) {
            ans += (rPos - lPos + 1);
            if (ans >= MOD) ans %= MOD;
        }
    }

    free(pref);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int WaysToSplit(int[] nums) {
        int n = nums.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
        long total = pref[n];
        const int MOD = 1000000007;
        long ans = 0;
        int left = 1, right = 1;

        for (int j = 2; j < n; j++) {
            long lower = Math.Max(0L, 2 * pref[j] - total);
            long upper = pref[j] / 2;

            while (left < j && pref[left] < lower) left++;
            if (right < left) right = left;
            while (right < j && pref[right] <= upper) right++;

            ans += Math.Max(0, right - left);
            if (ans >= MOD) ans %= MOD;
        }

        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
var waysToSplit = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;
    const pref = new Array(n + 1);
    pref[0] = 0;
    for (let i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
    const total = pref[n];
    let ans = 0;

    const lowerBound = (arr, target, left, right) => {
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] >= target) right = mid;
            else left = mid + 1;
        }
        return left;
    };
    const upperBound = (arr, target, left, right) => {
        while (left < right) {
            const mid = Math.floor((left + right + 1) / 2);
            if (arr[mid] <= target) left = mid;
            else right = mid - 1;
        }
        return left;
    };

    for (let j = 2; j <= n - 1; ++j) {
        const low = Math.max(0, 2 * pref[j] - total);
        const high = Math.floor(pref[j] / 2);
        if (low > high) continue;
        const lIdx = lowerBound(pref, low, 1, j - 1);
        const rIdx = upperBound(pref, high, 1, j - 1);
        if (lIdx <= rIdx) {
            ans = (ans + (rIdx - lIdx + 1)) % MOD;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function waysToSplit(nums: number[]): number {
    const MOD = 1000000007;
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const total = prefix[n];
    let ans = 0;

    for (let i = 1; i <= n - 2; i++) {
        const leftSum = prefix[i];

        // Find the smallest j such that mid sum >= left sum
        let lo = i + 1, hi = n - 1;
        let lowIdx = n; // sentinel for "not found"
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (prefix[mid] - prefix[i] >= leftSum) {
                lowIdx = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        // Find the largest j such that mid sum <= right sum
        lo = i + 1; hi = n - 1;
        let highIdx = i; // sentinel for "no valid"
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (2 * prefix[mid] <= total + prefix[i]) {
                highIdx = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        if (lowIdx <= highIdx) {
            ans = (ans + (highIdx - lowIdx + 1)) % MOD;
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
     * @return Integer
     */
    function waysToSplit($nums) {
        $n = count($nums);
        $pref = [];
        $sum = 0;
        foreach ($nums as $v) {
            $sum += $v;
            $pref[] = $sum;
        }
        $mod = 1000000007;
        $ans = 0;

        for ($i = 0; $i <= $n - 3; $i++) {
            // Find leftmost j such that pref[j] >= 2 * pref[i]
            $leftTarget = 2 * $pref[$i];
            $l = $this->lowerBound($pref, $i + 1, $n - 2, $leftTarget);
            if ($l == -1) {
                continue;
            }

            // Find rightmost j such that pref[j] <= (total + pref[i]) / 2
            $rightTarget = intdiv($sum + $pref[$i], 2);
            $r = $this->upperBound($pref, $i + 1, $n - 2, $rightTarget);
            if ($r == -1) {
                continue;
            }

            if ($r >= $l) {
                $ans = ($ans + ($r - $l + 1)) % $mod;
            }
        }

        return $ans;
    }

    private function lowerBound($arr, $lo, $hi, $target) {
        $res = -1;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid] >= $target) {
                $res = $mid;
                $hi = $mid - 1;
            } else {
                $lo = $mid + 1;
            }
        }
        return $res;
    }

    private function upperBound($arr, $lo, $hi, $target) {
        $res = -1;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid] <= $target) {
                $res = $mid;
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func waysToSplit(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        if n < 3 { return 0 }
        
        var prefix = [Int](repeating: 0, count: n)
        var sum = 0
        for i in 0..<n {
            sum += nums[i]
            prefix[i] = sum
        }
        let total = sum
        var ans = 0
        
        for i in 0..<(n - 2) {
            let leftSum = prefix[i]
            let start = i + 1
            let end = n - 2
            
            // lower bound: first j where prefix[j] >= 2 * leftSum
            var l = start
            var r = end
            var lowIdx = end + 1
            let targetLow = leftSum * 2
            while l <= r {
                let m = (l + r) >> 1
                if prefix[m] >= targetLow {
                    lowIdx = m
                    r = m - 1
                } else {
                    l = m + 1
                }
            }
            
            // upper bound: last j where prefix[j] <= (total + leftSum) / 2
            l = start
            r = end
            var highIdx = start - 1
            let targetHigh = (total + leftSum) / 2
            while l <= r {
                let m = (l + r) >> 1
                if prefix[m] <= targetHigh {
                    highIdx = m
                    l = m + 1
                } else {
                    r = m - 1
                }
            }
            
            if lowIdx <= highIdx {
                ans += (highIdx - lowIdx + 1)
                if ans >= MOD { ans %= MOD }
            }
        }
        
        return ans % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun waysToSplit(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        val n = nums.size
        val prefix = LongArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + nums[i].toLong()
        }
        val total = prefix[n]
        var ans = 0L

        for (i in 1..n - 2) { // i is length of first part
            val leftSum = prefix[i]

            // Find smallest j such that prefix[j] >= 2 * leftSum
            var lo = i + 1
            var hi = n - 1
            var lower = -1
            while (lo <= hi) {
                val mid = (lo + hi) ushr 1
                if (prefix[mid] >= 2L * leftSum) {
                    lower = mid
                    hi = mid - 1
                } else {
                    lo = mid + 1
                }
            }

            // Find largest j such that prefix[j] <= (total + leftSum) / 2
            lo = i + 1
            hi = n - 1
            var upper = -1
            val maxVal = (total + leftSum) / 2L
            while (lo <= hi) {
                val mid = (lo + hi) ushr 1
                if (prefix[mid] <= maxVal) {
                    upper = mid
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }

            if (lower != -1 && upper != -1 && lower <= upper) {
                ans += (upper - lower + 1)
                if (ans >= MOD) ans %= MOD
            }
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int waysToSplit(List<int> nums) {
    const int MOD = 1000000007;
    int n = nums.length;
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      pref[i + 1] = pref[i] + nums[i];
    }
    int total = pref[n];
    int ans = 0;

    for (int i = 1; i <= n - 2; i++) {
      int leftSum = pref[i];

      // Find the smallest j such that sum(mid) >= sum(left)
      int lo = i + 1, hi = n - 1;
      int lowIdx = -1;
      while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        if (2 * leftSum <= pref[mid]) {
          lowIdx = mid;
          hi = mid - 1;
        } else {
          lo = mid + 1;
        }
      }
      if (lowIdx == -1) continue;

      // Find the largest j such that sum(mid) <= sum(right)
      lo = i + 1;
      hi = n - 1;
      int highIdx = -1;
      while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        if (2 * pref[mid] <= total + leftSum) {
          highIdx = mid;
          lo = mid + 1;
        } else {
          hi = mid - 1;
        }
      }
      if (highIdx == -1 || lowIdx > highIdx) continue;

      ans = (ans + (highIdx - lowIdx + 1)) % MOD;
    }

    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func waysToSplit(nums []int) int {
	const MOD int64 = 1000000007
	n := len(nums)
	prefix := make([]int64, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + int64(nums[i])
	}
	total := prefix[n]
	var ans int64

	for j := 1; j <= n-2; j++ { // j is the end index of the middle subarray
		midSumEnd := prefix[j+1]

		lower := 2*midSumEnd - total
		if lower < 0 {
			lower = 0
		}
		upper := midSumEnd / 2

		if lower > upper {
			continue
		}

		// search among k = i+1 where 1 <= k <= j
		lIdx := sort.Search(j, func(i int) bool { return prefix[i+1] >= lower })
		rIdx := sort.Search(j, func(i int) bool { return prefix[i+1] > upper })

		cnt := rIdx - lIdx
		if cnt > 0 {
			ans = (ans + int64(cnt)) % MOD
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
def ways_to_split(nums)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + nums[i] }
  mod = 1_000_000_007
  total = prefix[n]
  ans = 0

  lower_bound = lambda do |arr, left, right, target|
    while left < right
      mid = (left + right) / 2
      if arr[mid] < target
        left = mid + 1
      else
        right = mid
      end
    end
    left
  end

  upper_bound = lambda do |arr, left, right, target|
    while left < right
      mid = (left + right) / 2
      if arr[mid] <= target
        left = mid + 1
      else
        right = mid
      end
    end
    left
  end

  (0..n - 3).each do |i|
    left_sum = prefix[i + 1]
    l = lower_bound.call(prefix, i + 2, n, 2 * left_sum)
    r = upper_bound.call(prefix, i + 2, n, (total + left_sum) / 2) - 1
    if r >= l
      ans = (ans + (r - l + 1)) % mod
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def waysToSplit(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        val n = nums.length
        val prefix = new Array[Long](n + 1)
        var i = 0
        while (i < n) {
            prefix(i + 1) = prefix(i) + nums(i).toLong
            i += 1
        }
        val total = prefix(n)
        var ans = 0L

        var leftIdx = 0
        while (leftIdx <= n - 3) {
            val leftSum = prefix(leftIdx + 1)

            // find minimal t (j+1) such that prefix[t] >= 2 * leftSum
            var lo = leftIdx + 2
            var hi = n - 1
            var lowT = n // not found sentinel
            while (lo <= hi) {
                val mid = (lo + hi) >>> 1
                if (prefix(mid) >= leftSum * 2) {
                    lowT = mid
                    hi = mid - 1
                } else {
                    lo = mid + 1
                }
            }

            // find maximal t (j+1) such that prefix[t] <= (total + leftSum) / 2
            lo = leftIdx + 2
            hi = n - 1
            var highT = leftIdx + 1 // sentinel for not found
            val target = (total + leftSum) / 2
            while (lo <= hi) {
                val mid = (lo + hi) >>> 1
                if (prefix(mid) <= target) {
                    highT = mid
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }

            if (lowT <= highT && lowT < n && highT >= leftIdx + 2) {
                ans += (highT - lowT + 1)
                if (ans >= MOD) ans %= MOD
            }

            leftIdx += 1
        }

        (ans % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn ways_to_split(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pref = vec![0i64; n];
        for i in 0..n {
            pref[i] = nums[i] as i64 + if i > 0 { pref[i - 1] } else { 0 };
        }
        let total = pref[n - 1];
        const MOD: i64 = 1_000_000_007;
        let mut ans: i64 = 0;

        fn lower_bound(arr: &Vec<i64>, l: usize, r: usize, target: i64) -> usize {
            let (mut left, mut right) = (l, r);
            while left < right {
                let mid = (left + right) / 2;
                if arr[mid] < target {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            left
        }

        fn upper_bound(arr: &Vec<i64>, l: usize, r: usize, target: i64) -> usize {
            let (mut left, mut right) = (l, r);
            while left < right {
                let mid = (left + right) / 2;
                if arr[mid] <= target {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            left
        }

        for i in 0..n - 2 {
            let left_sum = pref[i];
            let low_target = 2 * left_sum;
            let start = i + 1;
            let end = n - 1; // exclusive, last possible j is n-2

            let low_idx = lower_bound(&pref, start, end, low_target);
            if low_idx >= n - 1 {
                continue;
            }

            let high_target = (total + left_sum) / 2;
            let high_excl = upper_bound(&pref, start, end, high_target);
            if high_excl == 0 {
                continue;
            }
            let high_idx = high_excl - 1;

            if low_idx > high_idx {
                continue;
            }

            ans += (high_idx - low_idx + 1) as i64;
            if ans >= MOD {
                ans %= MOD;
            }
        }

        (ans % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (ways-to-split nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (pref (make-vector n)))
    ;; prefix sums
    (for ([i (in-range n)])
      (if (= i 0)
          (vector-set! pref 0 (vector-ref vec 0))
          (vector-set! pref i (+ (vector-ref pref (- i 1)) (vector-ref vec i)))))
    (let ((total (vector-ref pref (- n 1))))
      ;; binary search helpers on pref vector
      (define (lower-bound lo hi target)
        (let loop ((l lo) (r (+ hi 1)))
          (if (= l r)
              l
              (let* ((mid (quotient (+ l r) 2))
                     (val (vector-ref pref mid)))
                (if (< val target)
                    (loop (+ mid 1) r)
                    (loop l mid))))))
      (define (upper-bound lo hi target)
        (let loop ((l lo) (r (+ hi 1)))
          (if (= l r)
              l
              (let* ((mid (quotient (+ l r) 2))
                     (val (vector-ref pref mid)))
                (if (<= val target)
                    (loop (+ mid 1) r)
                    (loop l mid))))))
      ;; main loop over first cut position i
      (let loop ((i 0) (ans 0))
        (if (> i (- n 3))
            ans
            (let* ((left-sum (vector-ref pref i))
                   (low-target (* 2 left-sum))
                   (high-target (quotient (+ total left-sum) 2)) ; floor
                   (low (lower-bound (+ i 1) (- n 2) low-target))
                   (up (upper-bound (+ i 1) (- n 2) high-target))
                   (high (- up 1)))
              (if (> low high)
                  (loop (+ i 1) ans)
                  (let ((add (modulo (- (+ high 1) low) MOD)))
                    (loop (+ i 1) (modulo (+ ans add) MOD)))))))))))
```

## Erlang

```erlang
-spec ways_to_split([integer()]) -> integer().
ways_to_split(Nums) ->
    Mod = 1000000007,
    Prefix = build_prefix_tuple(Nums),
    N = tuple_size(Prefix) - 1,
    Total = element(N + 1, Prefix),
    MaxI = N - 2,
    loop_i(1, MaxI, Prefix, Total, Mod, 0).

build_prefix_tuple(Nums) ->
    build_prefix_tuple(Nums, 0, [0]).

build_prefix_tuple([], _Sum, Acc) ->
    list_to_tuple(lists:reverse(Acc));
build_prefix_tuple([H | T], Sum, Acc) ->
    NewSum = Sum + H,
    build_prefix_tuple(T, NewSum, [NewSum | Acc]).

loop_i(I, MaxI, Prefix, Total, Mod, Acc) when I =< MaxI ->
    LeftSum = element(I, Prefix),
    TargetLow = 2 * LeftSum,
    TargetHigh = (Total + LeftSum) div 2,
    N = tuple_size(Prefix) - 1,
    LIdx = lower_bound(Prefix, I + 1, N - 1, TargetLow),
    HIdx = upper_bound(Prefix, I + 1, N - 1, TargetHigh),
    Count = if
        LIdx =< HIdx -> HIdx - LIdx + 1;
        true -> 0
    end,
    NewAcc = (Acc + Count) rem Mod,
    loop_i(I + 1, MaxI, Prefix, Total, Mod, NewAcc);
loop_i(_, _, _, _, _, Acc) ->
    Acc.

lower_bound(_Prefix, L, R, _Target) when L > R -> L;
lower_bound(Prefix, L, R, Target) ->
    Mid = (L + R) div 2,
    Val = element(Mid, Prefix),
    if
        Val >= Target -> lower_bound(Prefix, L, Mid - 1, Target);
        true -> lower_bound(Prefix, Mid + 1, R, Target)
    end.

upper_bound(_Prefix, L, R, _Target) when L > R -> R;
upper_bound(Prefix, L, R, Target) ->
    Mid = (L + R) div 2,
    Val = element(Mid, Prefix),
    if
        Val =< Target -> upper_bound(Prefix, Mid + 1, R, Target);
        true -> upper_bound(Prefix, L, Mid - 1, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec ways_to_split(nums :: [integer]) :: integer
  def ways_to_split(nums) do
    n = length(nums)
    total = Enum.sum(nums)

    # Build prefix sums list
    {_, rev_prefix} =
      Enum.reduce(nums, {0, []}, fn x, {sum, acc} ->
        new_sum = sum + x
        {new_sum, [new_sum | acc]}
      end)

    prefix_list = [0 | Enum.reverse(rev_prefix)]
    pre = List.to_tuple(prefix_list)
    mod = 1_000_000_007

    # Iterate over possible start index of the third subarray (j)
    {_left, _right, ans} =
      Enum.reduce(2..(n - 1), {0, 0, 0}, fn j, {left, right, acc} ->
        lower_needed = 2 * elem(pre, j) - total
        upper_needed = div(elem(pre, j), 2)

        limit = j - 1

        left = advance_left(left, limit, pre, lower_needed)
        right = advance_right(right, limit, pre, upper_needed)

        cnt = max(0, right - left)
        {left, right, rem(acc + cnt, mod)}
      end)

    ans
  end

  defp advance_left(l, limit, pre, target) do
    if l < limit && elem(pre, l + 1) < target do
      advance_left(l + 1, limit, pre, target)
    else
      l
    end
  end

  defp advance_right(r, limit, pre, target) do
    if r < limit && elem(pre, r + 1) <= target do
      advance_right(r + 1, limit, pre, target)
    else
      r
    end
  end
end
```

# 3251. Find the Count of Monotonic Pairs II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countOfPairs(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        const int MAXV = 1000; // given constraint
        vector<int> prev(MAXV + 1, 0), cur(MAXV + 1, 0), pref(MAXV + 1, 0);
        
        // initialization for first element
        for (int v = 0; v <= nums[0]; ++v) prev[v] = 1;
        
        for (size_t i = 1; i < nums.size(); ++i) {
            int inc = max(0, nums[i] - nums[i-1]); // required increase
            // build prefix sums of prev
            pref[0] = prev[0];
            for (int v = 1; v <= MAXV; ++v) {
                pref[v] = pref[v-1] + prev[v];
                if (pref[v] >= MOD) pref[v] -= MOD;
            }
            // compute cur
            fill(cur.begin(), cur.end(), 0);
            for (int v = 0; v <= nums[i]; ++v) {
                int limit = v - inc;
                if (limit < 0) continue;
                cur[v] = pref[limit];
            }
            prev.swap(cur);
        }
        
        long long ans = 0;
        for (int v = 0; v <= MAXV; ++v) {
            ans += prev[v];
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int countOfPairs(int[] nums) {
        int n = nums.length;
        int max = 0;
        for (int v : nums) if (v > max) max = v;
        long[] dp = new long[max + 1];
        // first position
        for (int v = 0; v <= nums[0]; v++) dp[v] = 1;
        for (int i = 1; i < n; i++) {
            long[] prefix = new long[max + 1];
            prefix[0] = dp[0];
            for (int v = 1; v <= max; v++) {
                prefix[v] = (prefix[v - 1] + dp[v]) % MOD;
            }
            long[] ndp = new long[max + 1];
            int limit = nums[i];
            for (int v = 0; v <= limit; v++) {
                ndp[v] = prefix[v];
            }
            dp = ndp;
        }
        long ans = 0;
        for (long val : dp) ans = (ans + val) % MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)
        dp = [0] * (max_val + 1)

        # initialize for first element
        for v in range(nums[0] + 1):
            dp[v] = 1

        # iterate over remaining positions
        for i in range(1, n):
            limit = nums[i]
            newdp = [0] * (max_val + 1)
            prefix = 0
            for w in range(limit + 1):
                prefix += dp[w]
                if prefix >= MOD:
                    prefix -= MOD
                newdp[w] = prefix
            dp = newdp

        # sum over possible ending values of the last position
        ans = sum(dp[:nums[-1] + 1]) % MOD
        return ans
```

## Python3

```python
import sys
from typing import List

MOD = 10 ** 9 + 7

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        max_val = max(nums)
        dp = [0] * (max_val + 1)

        # initialize for first element
        limit = nums[0]
        for v in range(limit + 1):
            dp[v] = 1

        for i in range(1, len(nums)):
            inc = nums[i] - nums[i - 1]
            if inc < 0:
                inc = 0
            # prefix sums of previous dp
            pref = [0] * (max_val + 1)
            cur_sum = 0
            for v in range(max_val + 1):
                cur_sum += dp[v]
                if cur_sum >= MOD:
                    cur_sum -= MOD
                pref[v] = cur_sum

            new_dp = [0] * (max_val + 1)
            limit = nums[i]
            for v in range(limit + 1):
                max_u = v - inc
                if max_u >= 0:
                    new_dp[v] = pref[max_u]
            dp = new_dp

        result = sum(dp[:nums[-1] + 1]) % MOD
        return result
```

## C

```c
#include <stddef.h>
#include <stdint.h>

int countOfPairs(int* nums, int numsSize) {
    const int MOD = 1000000007;
    if (numsSize == 0) return 0;

    int maxV = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxV) maxV = nums[i];

    // dp arrays
    static long long dpPrev[1001];
    static long long dpCurr[1001];
    static long long pref[1001];

    for (int v = 0; v <= maxV; ++v)
        dpPrev[v] = (v <= nums[0]) ? 1 : 0;

    for (int i = 1; i < numsSize; ++i) {
        // prefix sums of previous dp
        long long sum = 0;
        for (int v = 0; v <= maxV; ++v) {
            sum += dpPrev[v];
            if (sum >= MOD) sum -= MOD;
            pref[v] = sum;
        }
        // compute current dp
        int limit = nums[i];
        for (int v = 0; v <= maxV; ++v) {
            if (v <= limit)
                dpCurr[v] = pref[v];
            else
                dpCurr[v] = 0;
        }
        // swap dpPrev and dpCurr
        for (int v = 0; v <= maxV; ++v) dpPrev[v] = dpCurr[v];
    }

    long long ans = 0;
    for (int v = 0; v <= maxV; ++v) {
        ans += dpPrev[v];
        if (ans >= MOD) ans -= MOD;
    }
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    public int CountOfPairs(int[] nums) {
        int n = nums.Length;
        int maxVal = 0;
        foreach (int x in nums) if (x > maxVal) maxVal = x;
        long[] dp = new long[maxVal + 1];
        for (int v = 0; v <= nums[0]; v++) dp[v] = 1;

        for (int i = 0; i < n - 1; i++) {
            int curMax = nums[i];
            int nextMax = nums[i + 1];
            int diff = nums[i + 1] - nums[i];

            long[] pref = new long[curMax + 1];
            pref[0] = dp[0];
            for (int v = 1; v <= curMax; v++) {
                pref[v] = (pref[v - 1] + dp[v]) % MOD;
            }

            long[] ndp = new long[maxVal + 1];
            for (int vNext = 0; vNext <= nextMax; vNext++) {
                int lower = Math.Max(0, vNext - diff);
                int upper = Math.Min(vNext, curMax);
                if (lower > upper) continue;
                long sum = pref[upper];
                if (lower > 0) sum = (sum - pref[lower - 1] + MOD) % MOD;
                ndp[vNext] = sum;
            }
            dp = ndp;
        }

        long ans = 0;
        for (int v = 0; v <= nums[n - 1]; v++) {
            ans += dp[v];
            if (ans >= MOD) ans -= MOD;
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
var countOfPairs = function(nums) {
    const MOD = 1000000007n;
    const n = nums.length;
    const maxVal = Math.max(...nums);
    
    // dp[v] = number of ways ending with arr1[i]=v for current i
    let dp = new Array(maxVal + 1).fill(0n);
    for (let v = 0; v <= nums[0]; ++v) {
        dp[v] = 1n;
    }
    
    for (let i = 1; i < n; ++i) {
        const prevMax = nums[i - 1];
        const curMax = nums[i];
        // prefix sums of previous dp up to prevMax
        const pref = new Array(prevMax + 2).fill(0n); // pref[0]=0
        for (let p = 0; p <= prevMax; ++p) {
            pref[p + 1] = (pref[p] + dp[p]) % MOD;
        }
        const k = Math.max(0, nums[i] - nums[i - 1]); // required extra increase
        
        const newDp = new Array(maxVal + 1).fill(0n);
        for (let v = 0; v <= curMax; ++v) {
            const limit = v - k;
            if (limit < 0) continue;
            const idx = Math.min(limit, prevMax);
            // sum dp[0..idx] = pref[idx+1]
            newDp[v] = pref[idx + 1];
        }
        dp = newDp;
    }
    
    let ans = 0n;
    for (let v = 0; v <= nums[n - 1]; ++v) {
        ans = (ans + dp[v]) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function countOfPairs(nums: number[]): number {
    const MOD = 1_000_000_007;
    const n = nums.length;
    const maxVal = Math.max(...nums);
    // dp[a][b] - number of ways for processed prefix where last values are a (arr1) and b (arr2)
    // Since constraints are small (maxVal <= 1000), we can use O(n * maxVal^2) with optimization via prefix sums.
    let dp = Array.from({ length: maxVal + 1 }, () => new Uint32Array(maxVal + 1));
    // initialize for first position
    for (let a = 0; a <= nums[0]; ++a) {
        for (let b = a; b <= nums[0]; ++b) {
            dp[a][b] = 1;
        }
    }

    const prefix = Array.from({ length: maxVal + 2 }, () => new Uint32Array(maxVal + 2));

    for (let i = 1; i < n; ++i) {
        // build 2D prefix sums of dp
        for (let a = 0; a <= maxVal; ++a) {
            let rowSum = 0;
            for (let b = 0; b <= maxVal; ++b) {
                rowSum = (rowSum + dp[a][b]) % MOD;
                prefix[a + 1][b + 1] = (prefix[a][b + 1] + rowSum) % MOD;
            }
        }

        const newDp = Array.from({ length: maxVal + 1 }, () => new Uint32Array(maxVal + 1));

        for (let a = 0; a <= nums[i]; ++a) {
            for (let b = a; b <= nums[i]; ++b) {
                // sum over all previous (pa, pb) where pa <= a and pb <= b
                const total = prefix[a + 1][b + 1];
                newDp[a][b] = total;
            }
        }

        dp = newDp;
    }

    let ans = 0;
    for (let a = 0; a <= maxVal; ++a) {
        for (let b = a; b <= maxVal; ++b) {
            ans = (ans + dp[a][b]) % MOD;
        }
    }
    return ans;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countOfPairs($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $maxVal = max($nums);
        // dp[j] - number of ways for current position where the last value of the first array is j
        $dp = array_fill(0, $maxVal + 1, 0);
        // initialization for the first element
        for ($j = 0; $j <= $nums[0]; $j++) {
            $dp[$j] = 1;
        }
        for ($i = 1; $i < $n; $i++) {
            $new = array_fill(0, $maxVal + 1, 0);
            // prefix sums of dp for fast range sum
            $pref = array_fill(0, $maxVal + 2, 0);
            for ($j = 0; $j <= $maxVal; $j++) {
                $pref[$j + 1] = ($pref[$j] + $dp[$j]) % $mod;
            }
            // transition
            for ($j = 0; $j <= $nums[$i]; $j++) {
                // previous value k must satisfy:
                // k <= j (non-decreasing first array)
                // and nums[i-1]-k <= nums[i]-j (non-decreasing second array)
                // => k >= max(0, $j - ($nums[$i] - $nums[$i-1]))
                $low = 0;
                if ($nums[$i] - $nums[$i-1] < $j) {
                    $low = $j - ($nums[$i] - $nums[$i-1]);
                }
                $high = $j;
                if ($low > $high) continue;
                $new[$j] = ($pref[$high + 1] - $pref[$low] + $mod) % $mod;
            }
            $dp = $new;
        }
        $ans = 0;
        foreach ($dp as $v) {
            $ans = ($ans + $v) % $mod;
        }
        return $ans;
    }
}
?>
```

## Swift

```swift
class Solution {
    func countOfPairs(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        guard let first = nums.first else { return 0 }
        let maxVal = nums.max()!
        var dpPrev = Array(repeating: 0, count: maxVal + 1)
        for v in 0...first {
            dpPrev[v] = 1
        }
        if nums.count == 1 {
            var ans = 0
            for v in 0...first {
                ans += dpPrev[v]
                if ans >= MOD { ans -= MOD }
            }
            return ans
        }
        for i in 1..<nums.count {
            let cur = nums[i]
            let prevNum = nums[i - 1]
            let inc = max(0, cur - prevNum)
            var prefix = Array(repeating: 0, count: maxVal + 1)
            var running = 0
            for v in 0...maxVal {
                running += dpPrev[v]
                if running >= MOD { running -= MOD }
                prefix[v] = running
            }
            var dpNew = Array(repeating: 0, count: maxVal + 1)
            if inc == 0 {
                for val in 0...cur {
                    dpNew[val] = prefix[val]
                }
            } else {
                for val in 0...cur {
                    let idx = val - inc
                    if idx >= 0 {
                        dpNew[val] = prefix[idx]
                    }
                }
            }
            dpPrev = dpNew
        }
        var ans = 0
        let last = nums.last!
        for v in 0...last {
            ans += dpPrev[v]
            if ans >= MOD { ans -= MOD }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOfPairs(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        if (nums.isEmpty()) return 0
        val maxVal = nums.maxOrNull() ?: 0
        var prev = LongArray(maxVal + 1)
        for (v in 0..nums[0]) {
            prev[v] = 1L
        }
        for (i in 1 until nums.size) {
            val inc = if (nums[i] > nums[i - 1]) nums[i] - nums[i - 1] else 0
            val pref = LongArray(maxVal + 1)
            var sum = 0L
            for (v in 0..maxVal) {
                sum += prev[v]
                if (sum >= MOD) sum -= MOD
                pref[v] = sum
            }
            val curr = LongArray(maxVal + 1)
            for (v in 0..nums[i]) {
                val minPrev = v - inc
                if (minPrev >= 0) {
                    curr[v] = pref[minPrev]
                }
            }
            prev = curr
        }
        var ans = 0L
        for (v in 0..maxVal) {
            ans += prev[v]
            if (ans >= MOD) ans -= MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countOfPairs(List<int> nums) {
    int n = nums.length;
    int maxVal = nums.reduce((a, b) => a > b ? a : b);
    List<int> dpPrev = List.filled(maxVal + 1, 0);
    for (int v = 0; v <= nums[0]; ++v) {
      dpPrev[v] = 1;
    }

    for (int i = 1; i < n; ++i) {
      int need = nums[i] - nums[i - 1];
      if (need < 0) need = 0;

      // prefix sums of dpPrev
      List<int> pref = List.filled(maxVal + 1, 0);
      int running = 0;
      for (int v = 0; v <= maxVal; ++v) {
        running += dpPrev[v];
        if (running >= _mod) running -= _mod;
        pref[v] = running;
      }

      List<int> dpCurr = List.filled(maxVal + 1, 0);
      for (int v = 0; v <= nums[i]; ++v) {
        int limit = v - need;
        if (limit >= 0) {
          dpCurr[v] = pref[limit];
        }
      }
      dpPrev = dpCurr;
    }

    int ans = 0;
    for (int v = 0; v <= nums[n - 1]; ++v) {
      ans += dpPrev[v];
      if (ans >= _mod) ans -= _mod;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "math"

func countOfPairs(nums []int) int {
	const MOD = 1000000007
	if len(nums) == 0 {
		return 0
	}
	maxVal := 0
	for _, v := range nums {
		if v > maxVal {
			maxVal = v
		}
	}
	dpPrev := make([]int, maxVal+1)
	for v := 0; v <= nums[0]; v++ {
		dpPrev[v] = 1
	}
	for i := 1; i < len(nums); i++ {
		inc := nums[i] - nums[i-1]
		if inc < 0 {
			inc = 0
		}
		pref := make([]int, maxVal+1)
		sum := 0
		for v := 0; v <= maxVal; v++ {
			sum += dpPrev[v]
			if sum >= MOD {
				sum -= MOD
			}
			pref[v] = sum
		}
		dpCurr := make([]int, maxVal+1)
		limit := nums[i]
		for v := 0; v <= limit; v++ {
			idx := v - inc
			if idx >= 0 {
				dpCurr[v] = pref[idx]
			}
		}
		dpPrev = dpCurr
	}
	ans := 0
	for _, val := range dpPrev {
		ans += val
		if ans >= MOD {
			ans -= MOD
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_of_pairs(nums)
  mod = 1_000_000_007
  max_val = nums.max
  dp = Array.new(max_val + 1, 0)

  (0..nums[0]).each { |v| dp[v] = 1 }

  (1...nums.length).each do |i|
    new_dp = Array.new(max_val + 1, 0)
    prefix = 0
    (0..max_val).each do |v|
      prefix += dp[v]
      prefix -= mod if prefix >= mod
      if v <= nums[i]
        new_dp[v] = prefix
      end
    end
    dp = new_dp
  end

  result = 0
  dp.each { |val| result = (result + val) % mod }
  result
end
```

## Scala

```scala
object Solution {
    def countOfPairs(nums: Array[Int]): Int = {
        val MOD = 1000000007
        val maxVal = nums.max
        // dp[a][b] where a <= b, number of ways for current prefix ending with values (a,b)
        var dp = Array.ofDim[Int](maxVal + 1, maxVal + 1)
        // initialize for first element
        val cap0 = nums(0)
        for {
            a <- 0 to cap0
            b <- a to cap0
        } {
            dp(a)(b) = 1
        }
        var pref = Array.ofDim[Int](maxVal + 2, maxVal + 2)

        def buildPrefix(): Unit = {
            // reset prefix
            for (i <- 0 to maxVal + 1) java.util.Arrays.fill(pref(i), 0)
            for (i <- 0 to maxVal) {
                var rowSum = 0L
                for (j <- 0 to maxVal) {
                    rowSum += dp(i)(j)
                    if (rowSum >= MOD) rowSum -= MOD
                    pref(i + 1)(j + 1) = ((pref(i)(j + 1) + rowSum) % MOD).toInt
                }
            }
        }

        for (idx <- 1 until nums.length) {
            val cap = nums(idx)
            buildPrefix()
            // compute new dp using prefix sums
            val newDp = Array.ofDim[Int](maxVal + 1, maxVal + 1)
            for {
                a <- 0 to cap
                b <- a to cap
            } {
                // sum over all pa <= a and pb <= b
                val sum = pref(a + 1)(b + 1)
                newDp(a)(b) = sum
            }
            dp = newDp
        }

        // final answer: sum of all dp entries
        var ans = 0L
        for (i <- 0 to maxVal; j <- i to maxVal) {
            ans += dp(i)(j)
            if (ans >= MOD) ans -= MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
use std::cmp::max;

impl Solution {
    pub fn count_of_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // maximum possible value (nums[i] - 1)
        let max_val = *nums.iter().max().unwrap() as usize;
        // dp[v]: number of ways for current position ending with value v
        let mut dp = vec![0i64; max_val + 1];
        // initialize for first element
        let limit0 = nums[0] as usize;
        for v in 0..limit0 {
            dp[v] = 1;
        }
        // iterate over remaining positions
        for i in 1..n {
            // prefix sums of previous dp
            let mut pref = vec![0i64; max_val + 1];
            let mut acc: i64 = 0;
            for v in 0..=max_val {
                acc += dp[v];
                if acc >= MOD { acc -= MOD; }
                pref[v] = acc;
            }
            // compute new dp
            let limit = nums[i] as usize;
            let mut ndp = vec![0i64; max_val + 1];
            for v in 0..limit {
                ndp[v] = pref[v];
            }
            dp = ndp;
        }
        // sum all possibilities
        let mut ans: i64 = 0;
        for &val in dp.iter() {
            ans += val;
            if ans >= MOD { ans -= MOD; }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (count-of-pairs nums)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (maxV (apply max nums))
         (dp-prev (make-vector (+ maxV 1) 0))
         (dp-cur (make-vector (+ maxV 1) 0)))
    ;; initialize first position
    (let ((limit (vector-ref arr 0)))
      (for ([v (in-range (add1 limit))])
        (vector-set! dp-prev v 1)))
    ;; process remaining positions
    (for ([i (in-range 1 n)])
      (let* ((prev-val (vector-ref arr (- i 1)))
             (cur-val (vector-ref arr i))
             (delta (- cur-val prev-val))
             (L (if (> delta 0) delta 0)))
        ;; prefix sums of dp-prev
        (define prefix (make-vector (+ maxV 1) 0))
        (let loop ([v 0] [acc 0])
          (when (< v (vector-length dp-prev))
            (set! acc (modulo (+ acc (vector-ref dp-prev v)) MOD))
            (vector-set! prefix v acc)
            (loop (add1 v) acc)))
        ;; compute dp for current index
        (for ([v (in-range (add1 maxV))])
          (vector-set! dp-cur v 0))
        (for ([v (in-range (add1 cur-val))])
          (let ((max-u (- v L)))
            (if (< max-u 0)
                (vector-set! dp-cur v 0)
                (vector-set! dp-cur v (vector-ref prefix max-u)))))
        ;; swap buffers
        (let ((tmp dp-prev))
          (set! dp-prev dp-cur)
          (set! dp-cur tmp))))
    ;; sum up results for last position
    (let* ((last-val (vector-ref arr (- n 1)))
           (ans 0))
      (for ([v (in-range (add1 last-val))])
        (set! ans (modulo (+ ans (vector-ref dp-prev v)) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_of_pairs/1]).

-define(MOD, 1000000007).

count_of_pairs(Nums) ->
    Mod = ?MOD,
    case Nums of
        [] -> 0;
        [H|T] ->
            L0 = 0,
            U0 = H,
            Len0 = U0 - L0 + 1,
            DP0 = lists:duplicate(Len0, 1),
            process(T, H, 0, L0, U0, DP0, Mod)
    end.

process([], _PrevNum, _PAcc, _L, _U, DP, Mod) ->
    lists:foldl(fun(X, Acc) -> (X + Acc) rem Mod end, 0, DP);
process([Num|Rest], PrevNum, PAcc, PrevL, PrevU, PrevDP, Mod) ->
    Inc = max(0, Num - PrevNum),
    PNew = PAcc + Inc,
    L = -PNew,
    U = Num - PNew,
    if
        U < L -> 0;
        true ->
            {NewDP, _} = build_new_dp(L, U, PrevL, PrevDP, Mod),
            process(Rest, Num, PNew, L, U, NewDP, Mod)
    end.

build_new_dp(L, U, PrevL, PrevDP, Mod) ->
    build_loop(L, U, PrevL, PrevDP, 0, [], Mod).

build_loop(X, EndX, CurPrevVal, PrevRem, SumAcc, AccRev, Mod) when X =< EndX ->
    {NewSum, NewPrevRem, NewCurPrevVal} =
        consume_until(CurPrevVal, PrevRem, SumAcc, X, Mod),
    build_loop(X + 1, EndX, NewCurPrevVal, NewPrevRem,
               NewSum, [NewSum | AccRev], Mod);
build_loop(_X, _EndX, _CurPrevVal, _PrevRem, _SumAcc, AccRev, _Mod) ->
    {lists:reverse(AccRev), ok}.

consume_until(CurVal, [], Sum, _X, _Mod) ->
    {Sum, [], CurVal};
consume_until(CurVal, [H|T], Sum, X, Mod) when CurVal =< X ->
    NewSum = (Sum + H) rem Mod,
    consume_until(CurVal + 1, T, NewSum, X, Mod);
consume_until(CurVal, List, Sum, _X, _Mod) ->
    {Sum, List, CurVal}.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec count_of_pairs(nums :: [integer]) :: integer
  def count_of_pairs(nums) do
    mod = 1_000_000_007
    n = length(nums)
    max_val = Enum.max(nums)

    # initial dp for the first element
    first = hd(nums)

    dp =
      for v <- 0..max_val do
        if v <= first, do: 1, else: 0
      end

    final_dp =
      Enum.reduce(1..(n - 1), dp, fn idx, prev_dp ->
        cur = Enum.at(nums, idx)
        prev = Enum.at(nums, idx - 1)

        low_inc = max(0, cur - prev)

        # prefix sums of previous dp
        pref = Enum.scan(prev_dp, 0, fn x, acc -> rem(acc + x, mod) end)

        for v <- 0..max_val do
          if v <= cur do
            limit = v - low_inc

            if limit < 0 do
              0
            else
              # pref[limit] already modulo mod
              Enum.at(pref, limit)
            end
          else
            0
          end
        end
      end)

    last_val = List.last(nums)

    final_dp
    |> Enum.take(last_val + 1)
    |> Enum.reduce(0, fn x, acc -> rem(acc + x, mod) end)
  end
end
```

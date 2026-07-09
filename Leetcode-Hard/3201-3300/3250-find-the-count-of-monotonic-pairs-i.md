# 3250. Find the Count of Monotonic Pairs I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countOfPairs(vector<int>& nums) {
        const int MOD = 1000000007;
        int n = nums.size();
        int maxVal = 50; // given constraint
        
        vector<int> dp(maxVal + 1, 0), ndp(maxVal + 1, 0);
        for (int s = 0; s <= nums[0]; ++s) dp[s] = 1;
        
        for (int i = 1; i < n; ++i) {
            // prefix sums of previous dp
            vector<int> pref(maxVal + 1, 0);
            pref[0] = dp[0];
            for (int v = 1; v <= maxVal; ++v) {
                pref[v] = pref[v - 1] + dp[v];
                if (pref[v] >= MOD) pref[v] -= MOD;
            }
            
            fill(ndp.begin(), ndp.end(), 0);
            int diff = nums[i] - nums[i - 1];
            int limit = max(0, diff); // s - limit is the upper bound for previous t
            for (int s = 0; s <= nums[i]; ++s) {
                int ub = s - limit;
                if (ub < 0) continue;
                if (ub > maxVal) ub = maxVal;
                ndp[s] = pref[ub];
            }
            dp.swap(ndp);
        }
        
        long long ans = 0;
        for (int s = 0; s <= nums.back(); ++s) {
            ans += dp[s];
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
        int maxVal = 50; // given constraint
        long[] dpPrev = new long[maxVal + 1];
        for (int s = 0; s <= nums[0]; ++s) {
            dpPrev[s] = 1;
        }
        for (int i = 1; i < n; ++i) {
            int diff = nums[i] - nums[i - 1];
            int need = Math.max(diff, 0);
            long[] pref = new long[maxVal + 1];
            pref[0] = dpPrev[0];
            for (int v = 1; v <= maxVal; ++v) {
                pref[v] = (pref[v - 1] + dpPrev[v]) % MOD;
            }
            long[] dpCurr = new long[maxVal + 1];
            int limit = nums[i];
            for (int s = 0; s <= limit; ++s) {
                int upper = s - need;
                if (upper >= 0) {
                    dpCurr[s] = pref[upper];
                }
            }
            dpPrev = dpCurr;
        }
        long ans = 0;
        for (int s = 0; s <= nums[n - 1]; ++s) {
            ans += dpPrev[s];
            if (ans >= MOD) ans -= MOD;
        }
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
        max_val = max(nums)
        dp = [0] * (max_val + 1)
        for s in range(nums[0] + 1):
            dp[s] = 1

        for i in range(1, len(nums)):
            delta = nums[i] - nums[i - 1]
            if delta < 0:
                delta = 0
            pref = [0] * (max_val + 2)
            for s in range(max_val + 1):
                pref[s + 1] = (pref[s] + dp[s]) % MOD

            new_dp = [0] * (max_val + 1)
            upper = nums[i]
            for t in range(upper + 1):
                limit = t - delta
                if limit >= 0:
                    new_dp[t] = pref[limit + 1]
            dp = new_dp

        return sum(dp) % MOD
```

## Python3

```python
class Solution:
    def countOfPairs(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        maxV = max(nums)
        dp_prev = [0] * (maxV + 1)
        for s in range(nums[0] + 1):
            dp_prev[s] = 1

        for i in range(1, n):
            d = max(0, nums[i] - nums[i - 1])
            pref = [0] * (maxV + 1)
            cur = 0
            for v in range(maxV + 1):
                cur += dp_prev[v]
                if cur >= MOD:
                    cur -= MOD
                pref[v] = cur

            dp_curr = [0] * (maxV + 1)
            limit_prev = nums[i - 1]
            for s in range(nums[i] + 1):
                min_prev = s - d
                if min_prev < 0:
                    continue
                idx = min(limit_prev, min_prev)
                dp_curr[s] = pref[idx]
            dp_prev = dp_curr

        ans = sum(dp_prev[:nums[-1] + 1]) % MOD
        return ans
```

## C

```c
int countOfPairs(int* nums, int numsSize){
    const int MOD = 1000000007;
    int maxV = 50; // given constraint
    static int dpPrev[51];
    static int dpCurr[51];
    static int pref[51];
    for (int i=0;i<=maxV;++i) dpPrev[i]=0;
    for (int s=0;s<=nums[0];++s){
        dpPrev[s]=1;
    }
    for (int idx=1; idx<numsSize; ++idx){
        int curMax = nums[idx];
        int prevMax = nums[idx-1];
        int diff = nums[idx] - nums[idx-1];
        // prefix sums of dpPrev up to prevMax
        pref[0]=dpPrev[0];
        for (int i=1;i<=prevMax;++i){
            int v = pref[i-1] + dpPrev[i];
            if (v>=MOD) v-=MOD;
            pref[i]=v;
        }
        // compute current dp
        for (int s=0;s<=maxV;++s) dpCurr[s]=0;
        for (int s=0; s<=curMax; ++s){
            int upper = s < prevMax ? s : prevMax;
            if (diff>0){
                int limit = s - diff;
                if (limit < 0){
                    continue; // no valid previous state
                }
                if (limit < upper) upper = limit;
            }
            if (upper<0) continue;
            dpCurr[s] = pref[upper];
        }
        // swap dpPrev and dpCurr
        for (int i=0;i<=maxV;++i){
            dpPrev[i]=dpCurr[i];
        }
    }
    long long ans=0;
    int lastMax = nums[numsSize-1];
    for (int s=0; s<=lastMax; ++s){
        ans += dpPrev[s];
        if (ans>=MOD) ans-=MOD;
    }
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1_000_000_007;
    public int CountOfPairs(int[] nums) {
        int n = nums.Length;
        const int MAXV = 50;
        long[] prev = new long[MAXV + 1];
        long[] curr = new long[MAXV + 1];
        // initialization for first element
        for (int s = 0; s <= nums[0]; ++s) {
            prev[s] = 1;
        }
        // iterate over remaining positions
        for (int i = 1; i < n; ++i) {
            // prefix sums of prev
            long[] pref = new long[MAXV + 1];
            pref[0] = prev[0];
            for (int v = 1; v <= MAXV; ++v) {
                pref[v] = (pref[v - 1] + prev[v]) % MOD;
            }
            int diff = nums[i] - nums[i - 1];
            for (int s = 0; s <= nums[i]; ++s) {
                int limit;
                if (diff > 0) {
                    limit = s - diff;
                } else {
                    limit = s;
                }
                if (limit < 0) {
                    curr[s] = 0;
                } else {
                    int upper = Math.Min(limit, nums[i - 1]);
                    curr[s] = pref[upper];
                }
            }
            // reset prev for next iteration
            Array.Clear(prev, 0, prev.Length);
            var temp = prev;
            prev = curr;
            curr = temp;
        }
        long ans = 0;
        for (int s = 0; s <= nums[n - 1]; ++s) {
            ans += prev[s];
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
    const MOD = 1000000007;
    const MAXV = 50; // maximum possible value in nums
    
    const n = nums.length;
    let prev = new Array(MAXV + 1).fill(0);
    
    // base case: first position can take any value from 0..nums[0]
    for (let s = 0; s <= nums[0]; ++s) {
        prev[s] = 1;
    }
    
    for (let i = 1; i < n; ++i) {
        const cur = new Array(MAXV + 1).fill(0);
        const incPrev = Math.max(0, nums[i] - nums[i - 1]); // required minimal increase
        
        // prefix sums of prev for O(1) range sum queries
        const pref = new Array(MAXV + 2).fill(0);
        for (let v = 0; v <= MAXV; ++v) {
            pref[v + 1] = (pref[v] + prev[v]) % MOD;
        }
        
        const limitPrev = nums[i - 1];
        const limitCur = nums[i];
        for (let s = 0; s <= limitCur; ++s) {
            const maxP = Math.min(limitPrev, s - incPrev);
            if (maxP >= 0) {
                cur[s] = pref[maxP + 1]; // sum of prev[0..maxP]
            }
        }
        prev = cur;
    }
    
    let ans = 0;
    const lastLimit = nums[n - 1];
    for (let s = 0; s <= lastLimit; ++s) {
        ans = (ans + prev[s]) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function countOfPairs(nums: number[]): number {
    const MOD = 1000000007;
    const n = nums.length;
    const maxV = Math.max(...nums);
    let prev = new Array(maxV + 1).fill(0);
    for (let s = 0; s <= nums[0]; ++s) {
        prev[s] = 1;
    }
    for (let i = 1; i < n; ++i) {
        const cur = new Array(maxV + 1).fill(0);
        const diff = Math.max(0, nums[i] - nums[i - 1]);
        const pref = new Array(maxV + 1).fill(0);
        let acc = 0;
        for (let v = 0; v <= maxV; ++v) {
            acc += prev[v];
            if (acc >= MOD) acc -= MOD;
            pref[v] = acc;
        }
        for (let s = 0; s <= nums[i]; ++s) {
            const limit = s - diff;
            if (limit >= 0) {
                cur[s] = pref[limit];
            }
        }
        prev = cur;
    }
    let ans = 0;
    for (let v = 0; v <= maxV; ++v) {
        ans += prev[v];
        if (ans >= MOD) ans -= MOD;
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
    function countOfPairs($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $maxVal = 50; // given constraint

        // dp for previous position
        $dpPrev = array_fill(0, $maxVal + 1, 0);
        for ($s = 0; $s <= $nums[0]; $s++) {
            $dpPrev[$s] = 1;
        }

        for ($i = 1; $i < $n; $i++) {
            $prevMax = $nums[$i - 1];
            $currMax = $nums[$i];
            $diff = $currMax - $prevMax;

            // prefix sums of dpPrev
            $pref = array_fill(0, $maxVal + 1, 0);
            $pref[0] = $dpPrev[0];
            for ($j = 1; $j <= $maxVal; $j++) {
                $pref[$j] = ($pref[$j - 1] + $dpPrev[$j]) % $mod;
            }

            $dpCurr = array_fill(0, $maxVal + 1, 0);
            for ($s = 0; $s <= $currMax; $s++) {
                // allowed previous s range: max(0, s - diff) .. min(s, prevMax)
                $left = $s - $diff;
                if ($left < 0) $left = 0;
                $right = $s;
                if ($right > $prevMax) $right = $prevMax;

                if ($left > $right) {
                    continue;
                }

                $sum = $pref[$right];
                if ($left > 0) {
                    $sum = ($sum - $pref[$left - 1] + $mod) % $mod;
                }
                $dpCurr[$s] = $sum;
            }

            $dpPrev = $dpCurr;
        }

        // sum over last position
        $ans = 0;
        $lastMax = $nums[$n - 1];
        for ($s = 0; $s <= $lastMax; $s++) {
            $ans += $dpPrev[$s];
            if ($ans >= $mod) $ans -= $mod;
        }
        return $ans % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func countOfPairs(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let maxVal = 50
        var dpPrev = Array(repeating: 0, count: maxVal + 1)
        // initialize for first element
        for v in 0...nums[0] {
            dpPrev[v] = 1
        }
        if nums.count == 1 {
            var ans = 0
            for v in 0...nums[0] {
                ans += dpPrev[v]
                if ans >= MOD { ans -= MOD }
            }
            return ans
        }
        for i in 1..<nums.count {
            let diff = nums[i] - nums[i - 1]
            let extra = max(0, diff)
            // prefix sums of previous DP
            var pref = Array(repeating: 0, count: maxVal + 1)
            var running = 0
            for v in 0...maxVal {
                running += dpPrev[v]
                if running >= MOD { running -= MOD }
                pref[v] = running
            }
            var dpCurr = Array(repeating: 0, count: maxVal + 1)
            let prevMax = nums[i - 1]
            for w in 0...nums[i] {
                let limit = w - extra
                if limit < 0 { continue }
                let maxV = min(prevMax, limit)
                if maxV >= 0 {
                    dpCurr[w] = pref[maxV]
                }
            }
            dpPrev = dpCurr
        }
        var ans = 0
        for v in 0...nums.last! {
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
        val maxVal = 50
        var dpPrev = LongArray(maxVal + 1)
        for (s in 0..nums[0]) {
            dpPrev[s] = 1L
        }
        for (i in 1 until nums.size) {
            val inc = if (nums[i] > nums[i - 1]) nums[i] - nums[i - 1] else 0
            val pref = LongArray(maxVal + 1)
            var sum = 0L
            for (k in 0..maxVal) {
                sum += dpPrev[k]
                if (sum >= MOD) sum -= MOD
                pref[k] = sum
            }
            val dpNext = LongArray(maxVal + 1)
            for (t in 0..nums[i]) {
                val idx = t - inc
                if (idx >= 0) {
                    dpNext[t] = pref[idx]
                }
            }
            dpPrev = dpNext
        }
        var ans = 0L
        for (v in dpPrev) {
            ans += v
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
    // dpPrev[s] = number of ways ending with arr1 value s at previous position
    List<int> dpPrev = List.filled(51, 0);
    for (int s = 0; s <= nums[0]; ++s) {
      dpPrev[s] = 1;
    }

    for (int i = 1; i < n; ++i) {
      int need = nums[i] - nums[i - 1];
      if (need < 0) need = 0;

      // prefix sums of dpPrev
      List<int> pref = List.filled(51, 0);
      int acc = 0;
      for (int t = 0; t <= 50; ++t) {
        acc += dpPrev[t];
        if (acc >= _mod) acc -= _mod;
        pref[t] = acc;
      }

      List<int> dpCurr = List.filled(51, 0);
      int curMax = nums[i];
      for (int s = 0; s <= curMax; ++s) {
        int idx = s - need;
        if (idx >= 0) {
          dpCurr[s] = pref[idx];
        }
      }
      dpPrev = dpCurr;
    }

    int ans = 0;
    for (int s = 0; s <= nums[n - 1]; ++s) {
      ans += dpPrev[s];
      if (ans >= _mod) ans -= _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func countOfPairs(nums []int) int {
	const MOD = 1000000007
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
	limit := nums[len(nums)-1]
	for v := 0; v <= limit; v++ {
		ans += dpPrev[v]
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
  prev = Array.new(max_val + 1, 0)
  (0..nums[0]).each { |s| prev[s] = 1 }

  (1...nums.length).each do |i|
    inc = [nums[i] - nums[i - 1], 0].max
    cur = Array.new(max_val + 1, 0)

    prefix = Array.new(max_val + 1, 0)
    sum = 0
    (0..max_val).each do |v|
      sum += prev[v]
      sum -= mod if sum >= mod
      prefix[v] = sum
    end

    (0..nums[i]).each do |s|
      max_prev = s - inc
      cur[s] = max_prev >= 0 ? prefix[max_prev] : 0
    end

    prev = cur
  end

  ans = 0
  (0..nums[-1]).each do |s|
    ans += prev[s]
    ans -= mod if ans >= mod
  end
  ans % mod
end
```

## Scala

```scala
object Solution {
    def countOfPairs(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        val n = nums.length
        var dpPrev = Array.fill(51)(0L)
        for (s <- 0 to nums(0)) dpPrev(s) = 1L

        for (i <- 1 until n) {
            val curMax = nums(i)
            val prevMax = nums(i - 1)

            // suffix sums of dpPrev for fast range sum [k, prevMax]
            val suff = Array.fill(prevMax + 2)(0L)
            var acc = 0L
            for (k <- prevMax to 0 by -1) {
                acc = (acc + dpPrev(k)) % MOD
                suff(k) = acc
            }

            val diff = nums(i - 1) - nums(i)
            val dpCur = Array.fill(51)(0L)

            for (s <- 0 to curMax) {
                var L = s
                if (diff > 0) L = s + diff
                if (L <= prevMax) {
                    dpCur(s) = suff(L)
                } // else remains 0
            }
            dpPrev = dpCur
        }

        var ans = 0L
        for (s <- 0 to nums(n - 1)) {
            ans = (ans + dpPrev(s)) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_of_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut dp_prev = vec![0i64; max_val + 1];
        for s in 0..=nums[0] as usize {
            dp_prev[s] = 1;
        }
        let mut dp_cur = vec![0i64; max_val + 1];

        for i in 1..n {
            let offset = if nums[i] > nums[i - 1] {
                (nums[i] - nums[i - 1]) as usize
            } else {
                0
            };
            // prefix sums of dp_prev up to max_val
            let mut pref = vec![0i64; max_val + 1];
            let mut acc: i64 = 0;
            for j in 0..=nums[i - 1] as usize {
                acc += dp_prev[j];
                if acc >= MOD {
                    acc -= MOD;
                }
                pref[j] = acc;
            }
            // fill remaining positions with the same accumulated sum
            for j in (nums[i - 1] as usize + 1)..=max_val {
                pref[j] = acc;
            }

            for s in 0..=max_val {
                if s > nums[i] as usize {
                    dp_cur[s] = 0;
                    continue;
                }
                if s < offset {
                    dp_cur[s] = 0;
                    continue;
                }
                let limit = s - offset;
                let idx = std::cmp::min(limit, nums[i - 1] as usize);
                dp_cur[s] = pref[idx];
            }

            // move current to previous and reset current
            dp_prev.clone_from_slice(&dp_cur);
            for v in dp_cur.iter_mut() {
                *v = 0;
            }
        }

        let mut ans: i64 = 0;
        for s in 0..=nums[n - 1] as usize {
            ans += dp_prev[s];
            if ans >= MOD {
                ans -= MOD;
            }
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
         (arr (list->vector nums)))
    (if (= n 0)
        0
        (let loop ((i 1)
                   (dpPrev (let* ((first-val (vector-ref arr 0))
                                  (size (+ 1 first-val))
                                  (v (make-vector size 0)))
                             (for ([s (in-range size)])
                               (vector-set! v s 1))
                             v)))
          (if (= i n)
              (let ((total 0))
                (for ([val (in-vector dpPrev)])
                  (set! total (modulo (+ total val) MOD)))
                total)
              (let* ((cur-val (vector-ref arr i))
                     (prev-val (vector-ref arr (- i 1)))
                     (size-cur (+ 1 cur-val))
                     (newdp (make-vector size-cur 0))
                     (pref (make-vector (vector-length dpPrev) 0)))
                ;; prefix sums of dpPrev
                (let ((acc 0))
                  (for ([idx (in-range (vector-length dpPrev))])
                    (set! acc (modulo (+ acc (vector-ref dpPrev idx)) MOD))
                    (vector-set! pref idx acc)))
                ;; transition
                (for ([s (in-range size-cur)])
                  (let* ((lo-raw (- (+ prev-val s) cur-val)) ; nums[i-1] + s - nums[i]
                         (lo (max 0 lo-raw))
                         (hi (min s prev-val)))
                    (when (<= lo hi)
                      (define sum-range
                        (if (= lo 0)
                            (vector-ref pref hi)
                            (modulo (- (vector-ref pref hi) (vector-ref pref (sub1 lo))) MOD)))
                      (vector-set! newdp s sum-range))))
                (loop (+ i 1) newdp))))))))
```

## Erlang

```erlang
-define(MOD, 1000000007).

count_of_pairs(Nums) ->
    Max = 50,
    case Nums of
        [] -> 0;
        _ ->
            First = hd(Nums),
            DP0 = array:new(Max + 1, {default, 0}),
            DPInit = init_dp(0, First, DP0),
            process(lists:tl(Nums), First, DPInit, Max)
    end.

process([], _PrevNum, DP, Max) ->
    lists:foldl(
        fun(I, Acc) -> (Acc + array:get(I, DP)) rem ?MOD end,
        0,
        lists:seq(0, Max)
    );
process([Curr | Rest], PrevNum, DPPrev, Max) ->
    Diff = PrevNum - Curr,
    NewDP0 = array:new(Max + 1, {default, 0}),
    NewDP = transition(0, Max, Diff, Curr, DPPrev, NewDP0),
    process(Rest, Curr, NewDP, Max).

transition(S, Max, _Diff, _Curr, _DPPrev, Acc) when S > Max ->
    Acc;
transition(S, Max, Diff, Curr, DPPrev, Acc) ->
    Count = array:get(S, DPPrev),
    Acc1 =
        if
            Count =:= 0 -> Acc;
            true ->
                Low = S,
                HighTmp = S + Diff,
                High = erlang:min(Curr, HighTmp),
                if High >= Low ->
                    lists:foldl(
                        fun(T, A) ->
                            Old = array:get(T, A),
                            NewVal = (Old + Count) rem ?MOD,
                            array:set(T, NewVal, A)
                        end,
                        Acc,
                        lists:seq(Low, High)
                    );
                   true -> Acc
                end
        end,
    transition(S + 1, Max, Diff, Curr, DPPrev, Acc1).

init_dp(S, N0, Arr) when S > N0 ->
    Arr;
init_dp(S, N0, Arr) ->
    Arr2 = array:set(S, 1, Arr),
    init_dp(S + 1, N0, Arr2).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec count_of_pairs(nums :: [integer]) :: integer
  def count_of_pairs(nums) do
    mod = 1_000_000_007
    max_val = 50

    # initialize dp tuple for the first element
    first = hd(nums)
    init_dp =
      0..max_val
      |> Enum.map(fn i -> if i <= first, do: 1, else: 0 end)
      |> List.to_tuple()

    {final_dp, _} =
      nums
      |> Enum.slice(1, length(nums) - 1)
      |> Enum.reduce({init_dp, first}, fn cur, {prev_dp, prev_num} ->
        diff = cur - prev_num

        # create a tuple of zeros
        new_dp = List.duplicate(0, max_val + 1) |> List.to_tuple()

        new_dp =
          0..cur
          |> Enum.reduce(new_dp, fn s, acc_dp ->
            low = max(0, s - diff)
            high = s

            sum =
              low..high
              |> Enum.reduce(0, fn t, acc ->
                (acc + elem(prev_dp, t)) rem mod
              end)

            put_elem(acc_dp, s, sum)
          end)

        {new_dp, cur}
      end)

    # sum all possibilities for the last position
    0..max_val
    |> Enum.reduce(0, fn i, acc -> (acc + elem(final_dp, i)) rem mod end)
  end
end
```

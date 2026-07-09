# 3077. Maximum Strength of K Disjoint Subarrays

## Cpp

```cpp
class Solution {
public:
    long long maximumStrength(vector<int>& nums, int k) {
        const long long NEG_INF = LLONG_MIN / 4;
        auto getCoeff = [&](int j)->long long{
            return (j & 1) ? j : -j;
        };
        int n = nums.size();
        vector<long long> nxt0(k + 1, NEG_INF), nxt1(k + 1, NEG_INF);
        nxt0[0] = 0; // dp[n][0][0] = 0
        
        for (int i = n - 1; i >= 0; --i) {
            vector<long long> cur0(k + 1, NEG_INF), cur1(k + 1, NEG_INF);
            for (int j = 0; j <= k; ++j) {
                if (j > 0) {
                    long long opt = max(nxt0[j - 1], nxt1[j]);
                    if (opt > NEG_INF / 2) { // reachable state
                        cur1[j] = (long long)nums[i] * getCoeff(j) + opt;
                    }
                }
                cur0[j] = max(nxt0[j], cur1[j]);
            }
            nxt0.swap(cur0);
            nxt1.swap(cur1);
        }
        return nxt0[k];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long maximumStrength(int[] nums, int k) {
        int n = nums.length;
        long[] coeff = new long[k + 1]; // 1-indexed
        for (int t = 1; t <= k; ++t) {
            int sign = (t % 2 == 1) ? 1 : -1;
            coeff[t] = (long) (k - t + 1) * sign;
        }

        final long NEG = Long.MIN_VALUE / 4;
        long[] dp0 = new long[k + 1];
        long[] dp1 = new long[k + 1];
        Arrays.fill(dp0, NEG);
        Arrays.fill(dp1, NEG);
        dp0[0] = 0;

        for (int val : nums) {
            long[] ndp0 = new long[k + 1];
            long[] ndp1 = new long[k + 1];
            Arrays.fill(ndp0, NEG);
            Arrays.fill(ndp1, NEG);

            // Transitions that keep or end a subarray
            for (int j = 0; j <= k; ++j) {
                if (dp0[j] != NEG) {
                    ndp0[j] = Math.max(ndp0[j], dp0[j]); // skip current element
                }
                if (dp1[j] != NEG) {
                    ndp0[j] = Math.max(ndp0[j], dp1[j]); // close subarray before this element
                }
            }

            // Start new subarray or continue existing one
            for (int j = 1; j <= k; ++j) {
                long add = coeff[j] * (long) val;
                if (dp1[j] != NEG) {
                    ndp1[j] = Math.max(ndp1[j], dp1[j] + add); // continue current subarray
                }
                if (dp0[j - 1] != NEG) {
                    ndp1[j] = Math.max(ndp1[j], dp0[j - 1] + add); // start new subarray
                }
            }

            dp0 = ndp0;
            dp1 = ndp1;
        }

        return dp0[k];
    }
}
```

## Python

```python
class Solution(object):
    def maximumStrength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        INF = -10**30  # sufficiently small
        
        # dp for position i+1 (next)
        next0 = [INF] * (k + 1)   # not inside a subarray
        next1 = [INF] * (k + 1)   # inside a subarray
        next0[0] = 0              # base case: no elements left, need 0 subarrays
        
        for idx in range(n - 1, -1, -1):
            ndp0 = [INF] * (k + 1)
            ndp1 = [INF] * (k + 1)
            val = nums[idx]
            for j in range(k + 1):
                # compute state where we are inside a subarray
                if j > 0:
                    opt_end = next0[j - 1]   # finish current subarray here
                    opt_cont = next1[j]      # continue the subarray
                    best_next = opt_end if opt_end > opt_cont else opt_cont
                    if best_next != INF:
                        coeff = j if (j & 1) else -j
                        ndp1[j] = val * coeff + best_next
                # compute state where we are not inside a subarray
                skip = next0[j]               # skip current element
                start = ndp1[j]               # start a new subarray at idx
                ndp0[j] = skip if skip > start else start
            next0, next1 = ndp0, ndp1
        
        return next0[k]
```

## Python3

```python
from typing import List

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF_NEG = -10**30  # sufficiently small
        
        dp0 = [INF_NEG] * (k + 1)   # not inside a subarray
        dp1 = [INF_NEG] * (k + 1)   # inside a subarray
        dp0[0] = 0                  # base case: no elements left, no subarrays needed
        
        for i in range(n - 1, -1, -1):
            cur0 = [INF_NEG] * (k + 1)
            cur1 = [INF_NEG] * (k + 1)
            
            # compute states where we are inside a selected subarray
            for j in range(1, k + 1):
                coeff = j if (j & 1) else -j   # get(j)
                best_continue = dp1[j]          # keep the subarray open
                best_end = dp0[j - 1]           # close it after this element
                cur1[j] = nums[i] * coeff + max(best_continue, best_end)
            
            # compute states where we are not inside a selected subarray
            for j in range(k + 1):
                cur0[j] = max(dp0[j], cur1[j])
            
            dp0, dp1 = cur0, cur1
        
        return dp0[k]
```

## C

```c
#include <limits.h>
#include <stdlib.h>

long long maximumStrength(int* nums, int numsSize, int k) {
    const long long NEG_INF = LLONG_MIN / 4;
    
    long long *dp = (long long *)malloc((k + 1) * sizeof(long long));
    long long *best = (long long *)malloc((k + 1) * sizeof(long long));
    long long *coeff = (long long *)malloc((k + 1) * sizeof(long long));
    
    for (int i = 0; i <= k; ++i) {
        dp[i] = NEG_INF;
        best[i] = NEG_INF;
    }
    dp[0] = 0;
    
    for (int t = 1; t <= k; ++t) {
        long long mag = (long long)(k - t + 1);
        if (t % 2 == 0) mag = -mag;
        coeff[t] = mag;
    }
    
    long long pref = 0;
    for (int idx = 0; idx < numsSize; ++idx) {
        long long prefPrev = pref;
        
        // Update best values using positions before current index
        for (int t = 1; t <= k; ++t) {
            if (dp[t - 1] != NEG_INF) {
                long long val = dp[t - 1] - coeff[t] * prefPrev;
                if (val > best[t]) best[t] = val;
            }
        }
        
        // Include current element in prefix sum
        pref += nums[idx];
        
        // Compute candidates for subarrays ending at current index
        for (int t = 1; t <= k; ++t) {
            if (best[t] != NEG_INF) {
                long long cand = coeff[t] * pref + best[t];
                if (cand > dp[t]) dp[t] = cand;
            }
        }
    }
    
    long long ans = dp[k];
    free(dp);
    free(best);
    free(coeff);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumStrength(int[] nums, int k) {
        int n = nums.Length;
        const long NEG = long.MinValue / 4; // sufficiently small
        
        long[] nxt0 = new long[k + 1];
        long[] nxt1 = new long[k + 1];
        for (int j = 0; j <= k; ++j) {
            nxt0[j] = NEG;
            nxt1[j] = NEG;
        }
        nxt0[0] = 0; // base: no subarrays needed, strength 0
        
        for (int i = n - 1; i >= 0; --i) {
            long[] cur0 = new long[k + 1];
            long[] cur1 = new long[k + 1];
            for (int j = 0; j <= k; ++j) {
                cur0[j] = NEG;
                cur1[j] = NEG;
            }
            
            for (int j = 0; j <= k; ++j) {
                if (j > 0) {
                    long coeff = (j % 2 == 1) ? j : -j;
                    long continueVal = nxt1[j];
                    long endVal = (j - 1 >= 0) ? nxt0[j - 1] : NEG;
                    long bestNext = Math.Max(continueVal, endVal);
                    if (bestNext != NEG) {
                        cur1[j] = coeff * (long)nums[i] + bestNext;
                    }
                }
                
                // state where we are not currently inside a selected subarray
                long skip = nxt0[j];
                long start = cur1[j];
                cur0[j] = Math.Max(skip, start);
            }
            
            nxt0 = cur0;
            nxt1 = cur1;
        }
        
        return nxt0[k];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumStrength = function(nums, k) {
    const n = nums.length;
    const INF_NEG = Number.NEGATIVE_INFINITY;

    // dp for position i+1 (next)
    let next0 = new Array(k + 1).fill(INF_NEG);
    let next1 = new Array(k + 1).fill(INF_NEG);
    next0[0] = 0; // base: no elements left, need 0 subarrays, not inside a subarray

    for (let i = n - 1; i >= 0; --i) {
        const cur0 = new Array(k + 1).fill(INF_NEG);
        const cur1 = new Array(k + 1).fill(INF_NEG);
        for (let j = 0; j <= k; ++j) {
            // state 1: currently inside a subarray that will count as one of the remaining j subarrays
            if (j > 0) {
                const coeff = (j % 2 === 1) ? j : -j;
                const continueSub = next1[j];          // keep the subarray open
                const closeAndProceed = next0[j - 1];   // end current subarray here
                const bestNext = Math.max(continueSub, closeAndProceed);
                cur1[j] = nums[i] * coeff + bestNext;
            }
            // state 0: not inside a subarray at position i
            const skip = next0[j];
            const startHere = cur1[j]; // start a new subarray at i (state becomes 1)
            cur0[j] = Math.max(skip, startHere);
        }
        next0 = cur0;
        next1 = cur1;
    }

    return next0[k];
};
```

## Typescript

```typescript
function maximumStrength(nums: number[], k: number): number {
    const n = nums.length;
    const coeff = new Array(k + 1);
    for (let i = 1; i <= k; i++) {
        const sign = i % 2 === 1 ? 1 : -1;
        coeff[i] = sign * (k - i + 1);
    }
    const NEG = Number.NEGATIVE_INFINITY;
    let dp0 = new Array(k + 1).fill(NEG); // not inside a subarray
    let dp1 = new Array(k).fill(NEG);     // inside the (j+1)-th subarray, j completed before it
    dp0[0] = 0;

    for (let idx = 0; idx < n; idx++) {
        const val = nums[idx];
        const ndp0 = new Array(k + 1).fill(NEG);
        const ndp1 = new Array(k).fill(NEG);

        // transitions from state not inside a subarray
        for (let j = 0; j <= k; j++) {
            const cur = dp0[j];
            if (cur === NEG) continue;
            // skip current element
            if (cur > ndp0[j]) ndp0[j] = cur;
            // start a new subarray (the (j+1)-th)
            if (j < k) {
                const cand = cur + coeff[j + 1] * val;
                if (cand > ndp1[j]) ndp1[j] = cand;
            }
        }

        // transitions from state inside a subarray
        for (let j = 0; j < k; j++) {
            const cur = dp1[j];
            if (cur === NEG) continue;
            // continue the current subarray
            const cont = cur + coeff[j + 1] * val;
            if (cont > ndp1[j]) ndp1[j] = cont;
            // close the subarray before this element, moving to completed j+1 subarrays
            if (cur > ndp0[j + 1]) ndp0[j + 1] = cur;
        }

        dp0 = ndp0;
        dp1 = ndp1;
    }

    let ans = dp0[k];
    if (k >= 1 && dp1[k - 1] !== NEG) {
        // close the last ongoing subarray after processing all elements
        if (dp1[k - 1] > ans) ans = dp1[k - 1];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumStrength($nums, $k) {
        $n = count($nums);
        // prefix sums
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $pref[$i] = $pref[$i - 1] + $nums[$i - 1];
        }

        // dpPrev corresponds to selecting j-1 subarrays
        $dpPrev = array_fill(0, $n + 1, 0); // for j = 0

        for ($j = 1; $j <= $k; $j++) {
            $weight = ($k - $j + 1) * (($j % 2 == 1) ? 1 : -1);
            $dpCurr = array_fill(0, $n + 1, PHP_INT_MIN);
            $bestPrev = PHP_INT_MIN;

            for ($i = 1; $i <= $n; $i++) {
                // consider ending previous subarray at position i-1
                $candidate = $dpPrev[$i - 1] - $weight * $pref[$i - 1];
                if ($candidate > $bestPrev) {
                    $bestPrev = $candidate;
                }

                // value when the j-th subarray ends at i-1
                $val = $bestPrev + $weight * $pref[$i];

                // take max with not ending a subarray at i-1
                $dpCurr[$i] = ($dpCurr[$i - 1] > $val) ? $dpCurr[$i - 1] : $val;
            }

            $dpPrev = $dpCurr;
        }

        return $dpPrev[$n];
    }
}
```

## Swift

```swift
class Solution {
    func maximumStrength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let INF_NEG: Int64 = Int64.min / 4
        var next0 = Array(repeating: INF_NEG, count: k + 1)
        var next1 = Array(repeating: INF_NEG, count: k + 1)
        next0[0] = 0
        
        for idx in stride(from: n - 1, through: 0, by: -1) {
            var cur0 = Array(repeating: INF_NEG, count: k + 1)
            var cur1 = Array(repeating: INF_NEG, count: k + 1)
            let val = Int64(nums[idx])
            for j in 0...k {
                if j > 0 {
                    let coeff: Int64 = (j % 2 == 1) ? Int64(j) : -Int64(j)
                    let bestNext = max(next0[j - 1], next1[j])
                    if bestNext != INF_NEG {
                        cur1[j] = val * coeff + bestNext
                    }
                }
                // state 0: either skip current element or start a subarray here (cur1)
                cur0[j] = max(next0[j], cur1[j])
            }
            next0 = cur0
            next1 = cur1
        }
        return Int(next0[k])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumStrength(nums: IntArray, k: Int): Long {
        val coeff = LongArray(k + 1)
        for (t in 1..k) {
            val value = (k - t + 1).toLong()
            coeff[t] = if (t % 2 == 1) value else -value
        }
        val NEG_INF = Long.MIN_VALUE / 4
        var dp0 = LongArray(k + 1) { NEG_INF } // not inside a subarray
        var dp1 = LongArray(k + 1) { NEG_INF } // inside the current (j-th) subarray
        dp0[0] = 0L

        for (numInt in nums) {
            val x = numInt.toLong()
            val ndp0 = LongArray(k + 1) { NEG_INF }
            val ndp1 = LongArray(k + 1) { NEG_INF }

            for (j in 0..k) {
                // End previous subarray before current element or keep skipping
                var bestNotInside = dp0[j]
                if (dp1[j] > bestNotInside) bestNotInside = dp1[j]
                ndp0[j] = bestNotInside

                // Continue an open subarray
                var bestInside = NEG_INF
                if (dp1[j] != NEG_INF) {
                    val cand = dp1[j] + coeff[j] * x
                    if (cand > bestInside) bestInside = cand
                }
                // Start a new subarray as the j-th one
                if (j > 0 && dp0[j - 1] != NEG_INF) {
                    val cand = dp0[j - 1] + coeff[j] * x
                    if (cand > bestInside) bestInside = cand
                }
                ndp1[j] = bestInside
            }

            dp0 = ndp0
            dp1 = ndp1
        }

        var answer = dp0[k]
        if (dp1[k] > answer) answer = dp1[k]
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximumStrength(List<int> nums, int k) {
    const int NEG_INF = -0x7FFFFFFFFFFFFFFF; // sufficiently small negative
    List<int> dp0 = List.filled(k + 1, NEG_INF);
    List<int> dp1 = List.filled(k + 1, NEG_INF);
    dp0[0] = 0;

    for (int idx = nums.length - 1; idx >= 0; --idx) {
      int val = nums[idx];
      List<int> new0 = List.filled(k + 1, NEG_INF);
      List<int> new1 = List.filled(k + 1, NEG_INF);
      for (int j = 0; j <= k; ++j) {
        if (j >= 1) {
          int coeff = (j & 1) == 1 ? j : -j;
          int bestPrev = dp0[j - 1] > dp1[j] ? dp0[j - 1] : dp1[j];
          new1[j] = val * coeff + bestPrev;
        }
        int skip = dp0[j];
        int start = new1[j];
        new0[j] = skip > start ? skip : start;
      }
      dp0 = new0;
      dp1 = new1;
    }

    return dp0[k];
  }
}
```

## Golang

```go
func maximumStrength(nums []int, k int) int64 {
	const INF int64 = -1 << 60
	dpClosed := make([]int64, k+1)
	dpOpen := make([]int64, k+1)
	for i := 0; i <= k; i++ {
		dpClosed[i] = INF
		dpOpen[i] = INF
	}
	dpClosed[0] = 0

	coeff := make([]int64, k+1) // 1-indexed
	for t := 1; t <= k; t++ {
		c := int64(k - t + 1)
		if t%2 == 0 {
			c = -c
		}
		coeff[t] = c
	}

	for _, v := range nums {
		// Option to close any open subarray before processing current element
		for t := 1; t <= k; t++ {
			if dpOpen[t] > dpClosed[t] {
				dpClosed[t] = dpOpen[t]
			}
		}
		newOpen := make([]int64, k+1)
		for i := 0; i <= k; i++ {
			newOpen[i] = INF
		}
		// Start a new subarray
		for t := 0; t < k; t++ {
			if dpClosed[t] != INF {
				cand := dpClosed[t] + coeff[t+1]*int64(v)
				if cand > newOpen[t+1] {
					newOpen[t+1] = cand
				}
			}
		}
		// Extend an existing open subarray
		for t := 1; t <= k; t++ {
			if dpOpen[t] != INF {
				cand := dpOpen[t] + coeff[t]*int64(v)
				if cand > newOpen[t] {
					newOpen[t] = cand
				}
			}
		}
		dpOpen = newOpen
	}

	// Final closure of any remaining open subarray
	for t := 1; t <= k; t++ {
		if dpOpen[t] > dpClosed[t] {
			dpClosed[t] = dpOpen[t]
		}
	}
	return dpClosed[k]
}
```

## Ruby

```ruby
def maximum_strength(nums, k)
  n = nums.length
  neg_inf = -(10**30)

  # dp for suffix starting at i+1
  not_inside = Array.new(k + 1, neg_inf) # dp[i+1][j][0]
  inside = Array.new(k + 1, neg_inf)     # dp[i+1][j][1]
  not_inside[0] = 0

  (n - 1).downto(0) do |i|
    cur_not = Array.new(k + 1, neg_inf)
    cur_in = Array.new(k + 1, neg_inf)

    (0..k).each do |j|
      if j > 0
        coeff = j.odd? ? j : -j
        best_next = not_inside[j - 1] > inside[j] ? not_inside[j - 1] : inside[j]
        cur_in[j] = nums[i] * coeff + best_next
      end

      # dp[i][j][0] = max(skip, start subarray here)
      cur_not[j] = not_inside[j] > cur_in[j] ? not_inside[j] : cur_in[j]
    end

    not_inside = cur_not
    inside = cur_in
  end

  not_inside[k]
end
```

## Scala

```scala
object Solution {
  def maximumStrength(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val INF: Long = Long.MinValue / 4

    var next0 = Array.fill[Long](k + 1)(INF)
    var next1 = Array.fill[Long](k + 1)(INF)
    // base case: no elements left, zero subarrays selected, not inside a subarray
    next0(0) = 0L

    for (idx <- (n - 1) to 0 by -1) {
      val cur0 = Array.fill[Long](k + 1)(INF)
      val cur1 = Array.fill[Long](k + 1)(INF)
      val v = nums(idx).toLong

      var j = 1
      while (j <= k) {
        // coefficient depending on parity of remaining subarrays to select
        val coeff: Long = if ((j & 1) == 1) j.toLong else -j.toLong

        // either end the current subarray here or continue it
        var best = INF
        if (next0(j - 1) > best) best = next0(j - 1)
        if (next1(j) > best) best = next1(j)

        if (best != INF) {
          cur1(j) = v * coeff + best
        }
        j += 1
      }

      // dp[i][j][0] = max(skip i, start new subarray at i)
      j = 0
      while (j <= k) {
        var best = next0(j)
        if (cur1(j) > best) best = cur1(j)
        cur0(j) = best
        j += 1
      }

      next0 = cur0
      next1 = cur1
    }

    next0(k)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_strength(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k_usize = k as usize;
        const NEG_INF: i64 = i64::MIN / 4;

        // helper to get coefficient based on remaining subarrays j
        #[inline]
        fn coeff(j: usize) -> i64 {
            if j % 2 == 1 { j as i64 } else { -(j as i64) }
        }

        let mut next0 = vec![NEG_INF; k_usize + 1];
        let mut next1 = vec![NEG_INF; k_usize + 1];
        next0[0] = 0;

        for idx in (0..n).rev() {
            let val = nums[idx] as i64;
            let mut cur0 = vec![NEG_INF; k_usize + 1];
            let mut cur1 = vec![NEG_INF; k_usize + 1];

            for j in 0..=k_usize {
                if j > 0 {
                    let best_prev = if next0[j - 1] > next1[j] { next0[j - 1] } else { next1[j] };
                    cur1[j] = val * coeff(j) + best_prev;
                }
                // dp[i][j][0] = max(skip, start here)
                let skip = next0[j];
                let start = cur1[j];
                cur0[j] = if skip > start { skip } else { start };
            }

            next0 = cur0;
            next1 = cur1;
        }

        next0[k_usize]
    }
}
```

## Racket

```racket
(define/contract (maximum-strength nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (NEG-INF (- (expt 2 120))) ; sufficiently small sentinel
         (dp0-next (make-vector (add1 k) NEG-INF))
         (dp1-next (make-vector (add1 k) NEG-INF)))
    ;; base case: zero subarrays from empty suffix gives strength 0
    (vector-set! dp0-next 0 0)
    ;; iterate from the end towards the start
    (for ([i (in-range (sub1 n) -1 -1)])
      (let ((cur0 (make-vector (add1 k) NEG-INF))
            (cur1 (make-vector (add1 k) NEG-INF)))
        ;; compute dp[i][j][1]
        (for ([j (in-range (add1 k))])
          (if (= j 0)
              (vector-set! cur1 j NEG-INF)
              (let* ((coeff (if (odd? j) j (- j))) ; get(j)
                     (prev0 (vector-ref dp0-next (sub1 j)))
                     (prev1 (vector-ref dp1-next j))
                     (best-prev (max prev0 prev1))
                     (val (+ (* (vector-ref nums-vec i) coeff) best-prev)))
                (vector-set! cur1 j val))))
        ;; compute dp[i][j][0]
        (for ([j (in-range (add1 k))])
          (let ((candidate (max (vector-ref dp0-next j)
                                (vector-ref cur1 j))))
            (vector-set! cur0 j candidate)))
        ;; roll forward
        (set! dp0-next cur0)
        (set! dp1-next cur1)))
    (vector-ref dp0-next k)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_strength/2]).
-define(NEG_INF, -1000000000000000000).

-spec maximum_strength(Nums :: [integer()], K :: integer()) -> integer().
maximum_strength(Nums, K) ->
    NegInf = ?NEG_INF,
    DP0_0 = array:set(0, 0, array:new(K + 1, {default, NegInf})),
    DP1_0 = array:new(K + 1, {default, NegInf}),
    {FinalDP0, _} =
        lists:foldl(
          fun(X, {CurDP0, CurDP1}) ->
              NewDP1 = update_dp1(X, K, CurDP0, CurDP1, NegInf),
              NewDP0 = update_dp0(K, CurDP0, NewDP1),
              {NewDP0, NewDP1}
          end,
          {DP0_0, DP1_0},
          Nums
        ),
    array:get(K, FinalDP0).

update_dp1(X, K, DP0, DP1, NegInf) ->
    lists:foldl(
      fun(T, AccDP1) ->
          Coef = coeff(T, K),
          StartPrev = array:get(T - 1, DP0),
          StartVal = if StartPrev > NegInf -> StartPrev + X * Coef; true -> NegInf end,
          ContPrev = array:get(T, DP1),
          ContVal = if ContPrev > NegInf -> ContPrev + X * Coef; true -> NegInf end,
          NewVal = if StartVal > ContVal -> StartVal; true -> ContVal end,
          array:set(T, NewVal, AccDP1)
      end,
      DP1,
      lists:seq(K, 1, -1)
    ).

update_dp0(K, DP0, DP1) ->
    lists:foldl(
      fun(T, AccDP0) ->
          Old = array:get(T, DP0),
          Val = array:get(T, DP1),
          MaxV = if Val > Old -> Val; true -> Old end,
          array:set(T, MaxV, AccDP0)
      end,
      DP0,
      lists:seq(0, K)
    ).

coeff(T, K) ->
    Sign = case T rem 2 of
        1 -> 1;
        _ -> -1
    end,
    (K - T + 1) * Sign.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_strength(nums :: [integer], k :: integer) :: integer
  def maximum_strength(nums, k) do
    neg_inf = -10_000_000_000_000_000_000_000

    dp0 = List.duplicate(neg_inf, k + 1)
    dp0 = List.replace_at(dp0, 0, 0)
    dp1 = List.duplicate(neg_inf, k + 1)

    {final_dp0, _} =
      Enum.reduce(Enum.reverse(nums), {dp0, dp1}, fn num, {prev0, prev1} ->
        {rev0, rev1, _} = build(num, prev0, prev1, neg_inf, 0, nil, [], [])
        {Enum.reverse(rev0), Enum.reverse(rev1)}
      end)

    Enum.at(final_dp0, k)
  end

  defp build(_num, [], [], _neg_inf, _j, _prev0_prev, acc0, acc1) do
    {acc0, acc1, nil}
  end

  defp build(num, [cur0 | rest0], [cur1 | rest1], neg_inf, j, prev0_prev, acc0, acc1) do
    if j == 0 do
      ndp1 = neg_inf
      ndp0 = max(cur0, ndp1)
      build(num, rest0, rest1, neg_inf, j + 1, cur0, [ndp0 | acc0], [ndp1 | acc1])
    else
      coeff = if rem(j, 2) == 1, do: j, else: -j
      best_prev =
        cond do
          cur1 > prev0_prev -> cur1
          true -> prev0_prev
        end

      ndp1 = num * coeff + best_prev
      ndp0 = max(cur0, ndp1)
      build(num, rest0, rest1, neg_inf, j + 1, cur0, [ndp0 | acc0], [ndp1 | acc1])
    end
  end
end
```

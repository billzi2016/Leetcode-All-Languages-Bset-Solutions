# 3640. Trionic Array II

## Cpp

```cpp
class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        const long long NEG = -(1LL<<60);
        long long dp0 = NEG, dp1 = NEG, dp2 = NEG;
        long long ans = NEG;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (i == 0) {
                dp0 = nums[0];
                continue;
            }
            long long ndp0 = NEG, ndp1 = NEG, ndp2 = NEG;
            if (nums[i] > nums[i-1]) { // increasing step
                ndp0 = max(dp0 + nums[i], (long long)nums[i]);          // start/continue first increase
                ndp2 = max(dp2 + nums[i], dp1 + nums[i]);              // continue or start second increase
            } else if (nums[i] < nums[i-1]) { // decreasing step
                ndp1 = max(dp1 + nums[i], dp0 + nums[i]);              // continue or start decrease
            } else { // equal values break the strict pattern
                ndp0 = nums[i];                                        // can start new subarray here
            }
            dp0 = ndp0;
            dp1 = ndp1;
            dp2 = ndp2;
            ans = max(ans, dp2);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        final long NEG = Long.MIN_VALUE / 4;

        long dp0 = nums[0]; // first increasing segment sum
        long dp1 = NEG;     // after first increase, before decrease
        long dp2 = NEG;     // decreasing segment sum
        long dp3 = NEG;     // second increasing segment sum (complete trionic)
        long ans = NEG;

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) { // strictly increasing step
                long ndp3 = NEG;
                if (dp3 != NEG) ndp3 = dp3 + nums[i];
                if (dp2 != NEG) ndp3 = Math.max(ndp3, dp2 + nums[i]);
                dp3 = ndp3;

                long ndp1 = NEG;
                if (dp1 != NEG) ndp1 = dp1 + nums[i];
                if (dp0 != NEG) ndp1 = Math.max(ndp1, dp0 + nums[i]);
                dp1 = ndp1;

                // continue or start first increasing segment
                if (dp0 != NEG && nums[i] > nums[i - 1]) {
                    dp0 = dp0 + nums[i];
                } else {
                    dp0 = nums[i];
                }
            } else if (nums[i] < nums[i - 1]) { // strictly decreasing step
                long ndp2 = NEG;
                if (dp2 != NEG) ndp2 = dp2 + nums[i];
                if (dp1 != NEG) ndp2 = Math.max(ndp2, dp1 + nums[i]);
                dp2 = ndp2;

                // start a new possible first increasing segment later
                dp0 = nums[i];
            } else { // equal values break strictness
                dp0 = nums[i];
                dp1 = NEG;
                dp2 = NEG;
                dp3 = NEG;
            }
            ans = Math.max(ans, dp3);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INF_NEG = -10**18
        n = len(nums)
        # dp0: max sum of increasing segment ending at i (first inc)
        # dp1: max sum after first decreasing segment (inc->dec) ending at i
        # dp2: max sum after second increasing segment (inc->dec->inc) ending at i
        dp0 = nums[0]
        dp1 = INF_NEG
        dp2 = INF_NEG
        ans = INF_NEG

        for i in range(1, n):
            v = nums[i]
            prev = nums[i - 1]
            old_dp0, old_dp1, old_dp2 = dp0, dp1, dp2

            if v > prev:  # increasing step
                # continue first increasing segment or start new at v
                cand0 = old_dp0 + v if old_dp0 != INF_NEG else INF_NEG
                dp0 = max(cand0, v)

                # second increasing segment can come from previous decreasing segment
                cand2 = INF_NEG
                if old_dp1 != INF_NEG:
                    cand2 = old_dp1 + v
                if old_dp2 != INF_NEG:
                    cand2 = max(cand2, old_dp2 + v)
                dp2 = cand2 if cand2 != INF_NEG else INF_NEG

            elif v < prev:  # decreasing step
                # first decreasing segment can start from end of first increasing or continue
                cand1 = INF_NEG
                if old_dp0 != INF_NEG:
                    cand1 = old_dp0 + v
                if old_dp1 != INF_NEG:
                    cand1 = max(cand1, old_dp1 + v)
                dp1 = cand1 if cand1 != INF_NEG else INF_NEG

                # start a new first increasing segment at current element
                dp0 = v

            else:  # equal values break the strict pattern
                dp0 = v
                dp1 = INF_NEG
                dp2 = INF_NEG

            ans = max(ans, dp2)

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        NEG_INF = -10**18
        inc1 = NEG_INF   # first increasing phase (at least two elements)
        dec = NEG_INF    # decreasing phase after inc1
        inc2 = NEG_INF   # second increasing phase after dec
        ans = NEG_INF

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                new_inc1 = max(
                    inc1 + nums[i] if inc1 != NEG_INF else NEG_INF,
                    nums[i - 1] + nums[i]
                )
                new_inc2 = max(
                    inc2 + nums[i] if inc2 != NEG_INF else NEG_INF,
                    dec + nums[i] if dec != NEG_INF else NEG_INF
                )
            else:
                new_inc1 = NEG_INF
                new_inc2 = NEG_INF

            if nums[i] < nums[i - 1]:
                new_dec = max(
                    dec + nums[i] if dec != NEG_INF else NEG_INF,
                    inc1 + nums[i] if inc1 != NEG_INF else NEG_INF
                )
            else:
                new_dec = NEG_INF

            inc1, dec, inc2 = new_inc1, new_dec, new_inc2
            ans = max(ans, inc2)

        return ans
```

## C

```c
long long maxSumTrionic(int* nums, int numsSize) {
    const long long NEG = -(1LL << 60);
    long long inc = NEG;   // first increasing segment
    long long dec = NEG;   // decreasing segment after the peak
    long long inc2 = NEG;  // final increasing segment
    long long ans = NEG;

    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > nums[i - 1]) {                     // increase
            long long startInc = (long long)nums[i - 1] + nums[i];
            if (inc != NEG) {
                long long extend = inc + nums[i];
                inc = (extend > startInc) ? extend : startInc;
            } else {
                inc = startInc;
            }

            long long newInc2 = NEG;
            if (dec != NEG) newInc2 = dec + nums[i];
            if (inc2 != NEG) {
                long long ext = inc2 + nums[i];
                if (ext > newInc2) newInc2 = ext;
            }
            inc2 = newInc2;

            dec = NEG;   // reset decreasing part
        } else if (nums[i] < nums[i - 1]) {              // decrease
            long long startDec = (inc != NEG) ? inc + nums[i] : NEG;
            if (dec != NEG) {
                long long extend = dec + nums[i];
                dec = (startDec > extend) ? startDec : extend;
            } else {
                dec = startDec;
            }
            inc = NEG;   // reset first increasing part
        } else {                                         // equal values break pattern
            inc = dec = inc2 = NEG;
        }

        if (inc2 > ans) ans = inc2;
    }
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MaxSumTrionic(int[] nums) {
        int n = nums.Length;
        const long NEG = long.MinValue / 4;

        long dp0 = nums[0]; // first increasing segment (at least one element)
        long dp1 = NEG;     // after first increase phase
        long dp2 = NEG;     // decreasing phase
        long dp3 = NEG;     // final increasing phase
        long ans = NEG;

        for (int i = 1; i < n; i++) {
            long cur = nums[i];
            long prev = nums[i - 1];

            long o0 = dp0, o1 = dp1, o2 = dp2, o3 = dp3;
            if (cur > prev) {
                // continue/increase first segment
                dp0 = (o0 != NEG) ? o0 + cur : cur;

                long cand1 = NEG;
                if (o1 != NEG) cand1 = Math.Max(cand1, o1 + cur);
                if (o0 != NEG) cand1 = Math.Max(cand1, o0 + cur);
                dp1 = cand1;

                long cand3 = NEG;
                if (o3 != NEG) cand3 = Math.Max(cand3, o3 + cur);
                if (o2 != NEG) cand3 = Math.Max(cand3, o2 + cur);
                dp3 = cand3;
                // dp2 stays unchanged
            } else if (cur < prev) {
                // decreasing phase
                long cand2 = NEG;
                if (o2 != NEG) cand2 = Math.Max(cand2, o2 + cur);
                if (o1 != NEG) cand2 = Math.Max(cand2, o1 + cur);
                dp2 = cand2;

                // reset for possible new first increasing segment
                dp0 = prev;
                dp1 = NEG; // cannot stay in first increase after a decrease
                // dp3 unchanged
            } else {
                // equal values break strict monotonicity
                dp0 = cur;
                dp1 = dp2 = dp3 = NEG;
            }

            if (dp3 > ans) ans = dp3;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumTrionic = function(nums) {
    const n = nums.length;
    let dp0 = -Infinity, dp1 = -Infinity, dp2 = -Infinity, dp3 = -Infinity;
    let ans = -Infinity;

    for (let i = 0; i < n; ++i) {
        if (i === 0) {
            dp0 = nums[0];
            continue;
        }
        const a = nums[i];
        const b = nums[i - 1];

        let ndp0 = -Infinity, ndp1 = -Infinity, ndp2 = -Infinity, ndp3 = -Infinity;

        if (a > b) {
            // phase 0 can continue
            if (dp0 !== -Infinity) ndp0 = dp0 + a;
            ndp0 = Math.max(ndp0, a); // start new subarray at i

            // phase 1: increase after start
            if (dp1 !== -Infinity) ndp1 = Math.max(ndp1, dp1 + a);
            if (dp0 !== -Infinity) ndp1 = Math.max(ndp1, dp0 + a);

            // phase 3: final increase after decrease
            if (dp3 !== -Infinity) ndp3 = Math.max(ndp3, dp3 + a);
            if (dp2 !== -Infinity) ndp3 = Math.max(ndp3, dp2 + a);
        } else if (a < b) {
            // phase 2: decreasing after first increase
            if (dp2 !== -Infinity) ndp2 = Math.max(ndp2, dp2 + a);
            if (dp1 !== -Infinity) ndp2 = Math.max(ndp2, dp1 + a);
        }

        // If we didn't set ndp0 in this step (e.g., when a < b), we can still start new subarray
        if (ndp0 === -Infinity) ndp0 = a;

        ans = Math.max(ans, ndp3);

        dp0 = ndp0;
        dp1 = ndp1;
        dp2 = ndp2;
        dp3 = ndp3;
    }

    return ans;
};
```

## Typescript

```typescript
function maxSumTrionic(nums: number[]): number {
    const n = nums.length;
    let dp0 = nums[0];
    let dp1 = Number.NEGATIVE_INFINITY;
    let dp2 = Number.NEGATIVE_INFINITY;
    let dp3 = Number.NEGATIVE_INFINITY;
    let ans = Number.NEGATIVE_INFINITY;

    for (let i = 1; i < n; ++i) {
        const x = nums[i];
        const prev = nums[i - 1];

        let ndp0 = Number.NEGATIVE_INFINITY;
        let ndp1 = Number.NEGATIVE_INFINITY;
        let ndp2 = Number.NEGATIVE_INFINITY;
        let ndp3 = Number.NEGATIVE_INFINITY;

        if (x > prev) {
            if (dp0 !== Number.NEGATIVE_INFINITY) ndp0 = dp0 + x;
            ndp0 = Math.max(ndp0, x);

            const cand1 = dp1 !== Number.NEGATIVE_INFINITY ? dp1 + x : Number.NEGATIVE_INFINITY;
            const cand2 = dp0 !== Number.NEGATIVE_INFINITY ? dp0 + x : Number.NEGATIVE_INFINITY;
            ndp1 = Math.max(cand1, cand2);

            const cand3 = dp3 !== Number.NEGATIVE_INFINITY ? dp3 + x : Number.NEGATIVE_INFINITY;
            const cand4 = dp2 !== Number.NEGATIVE_INFINITY ? dp2 + x : Number.NEGATIVE_INFINITY;
            ndp3 = Math.max(cand3, cand4);
        } else if (x < prev) {
            const cand5 = dp2 !== Number.NEGATIVE_INFINITY ? dp2 + x : Number.NEGATIVE_INFINITY;
            const cand6 = dp1 !== Number.NEGATIVE_INFINITY ? dp1 + x : Number.NEGATIVE_INFINITY;
            ndp2 = Math.max(cand5, cand6);
        } else {
            ndp0 = x;
        }

        ndp0 = Math.max(ndp0, x);

        dp0 = ndp0;
        dp1 = ndp1;
        dp2 = ndp2;
        dp3 = ndp3;

        if (dp3 > ans) ans = dp3;
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
    function maxSumTrionic($nums) {
        $n = count($nums);
        if ($n < 4) return 0; // problem guarantees at least one trionic subarray

        $neg = -PHP_INT_MAX;
        $dp0 = array_fill(0, $n, $neg);
        $dp1 = array_fill(0, $n, $neg);
        $dp2 = array_fill(0, $n, $neg);
        $dp3 = array_fill(0, $n, $neg);

        $dp0[0] = $nums[0];
        $ans = $neg;

        for ($i = 1; $i < $n; ++$i) {
            if ($nums[$i] > $nums[$i - 1]) { // increasing
                // dp0: continue or start new at i
                $extend0 = ($dp0[$i - 1] != $neg) ? $dp0[$i - 1] + $nums[$i] : $neg;
                $dp0[$i] = max($extend0, $nums[$i]);

                // dp1: continue or transition from dp0
                $cand1a = ($dp1[$i - 1] != $neg) ? $dp1[$i - 1] + $nums[$i] : $neg;
                $cand1b = ($dp0[$i - 1] != $neg) ? $dp0[$i - 1] + $nums[$i] : $neg;
                $dp1[$i] = max($cand1a, $cand1b);

                // dp2 cannot be in decreasing phase while increasing
                $dp2[$i] = $neg;

                // dp3: continue or transition from dp2
                $cand3a = ($dp3[$i - 1] != $neg) ? $dp3[$i - 1] + $nums[$i] : $neg;
                $cand3b = ($dp2[$i - 1] != $neg) ? $dp2[$i - 1] + $nums[$i] : $neg;
                $dp3[$i] = max($cand3a, $cand3b);

            } elseif ($nums[$i] < $nums[$i - 1]) { // decreasing
                // dp0: start new at i (cannot continue increasing)
                $dp0[$i] = $nums[$i];

                // dp1 cannot be in increasing phase while decreasing
                $dp1[$i] = $neg;

                // dp2: continue or transition from dp1
                $cand2a = ($dp2[$i - 1] != $neg) ? $dp2[$i - 1] + $nums[$i] : $neg;
                $cand2b = ($dp1[$i - 1] != $neg) ? $dp1[$i - 1] + $nums[$i] : $neg;
                $dp2[$i] = max($cand2a, $cand2b);

                // dp3 cannot be in increasing phase while decreasing
                $dp3[$i] = $neg;

            } else { // equal values break strictness
                $dp0[$i] = $nums[$i];
                $dp1[$i] = $dp2[$i] = $dp3[$i] = $neg;
            }

            if ($dp3[$i] > $ans) {
                $ans = $dp3[$i];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxSumTrionic(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 4 { return 0 }
        let NEG = Int.min / 4   // sufficiently small sentinel
        
        var dp0 = nums[0]       // sum of current increasing segment (phase 1)
        var dp1 = NEG           // after first increase phase
        var dp2 = NEG           // after decrease phase
        var dp3 = NEG           // after final increase phase
        var ans = NEG
        
        for i in 1..<n {
            let cur = nums[i]
            let prev = nums[i - 1]
            
            var ndp0 = NEG
            var ndp1 = NEG
            var ndp2 = NEG
            var ndp3 = NEG
            
            if cur > prev {                     // increasing step
                // phase 0 (still in first increase)
                let ext0 = dp0 != NEG ? dp0 + cur : NEG
                ndp0 = max(ext0, cur)           // start new or extend
                
                // transition to / stay in phase 1
                var candA = NEG
                if dp1 != NEG { candA = dp1 + cur }
                var candB = NEG
                if dp0 != NEG { candB = dp0 + cur }
                ndp1 = max(candA, candB)
                
                // transition to / stay in phase 3 (final increase)
                var candC = NEG
                if dp3 != NEG { candC = dp3 + cur }
                var candD = NEG
                if dp2 != NEG { candD = dp2 + cur }
                ndp3 = max(candC, candD)
            } else if cur < prev {               // decreasing step
                // transition to / stay in phase 2 (decrease)
                var candA = NEG
                if dp2 != NEG { candA = dp2 + cur }
                var candB = NEG
                if dp1 != NEG { candB = dp1 + cur }
                ndp2 = max(candA, candB)
                
                // start a new possible first increase at current position
                ndp0 = cur
            } else {                             // equal values break strictness
                ndp0 = cur
            }
            
            dp0 = ndp0
            dp1 = ndp1
            dp2 = ndp2
            dp3 = ndp3
            
            if dp3 > ans {
                ans = dp3
            }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSumTrionic(nums: IntArray): Long {
        val n = nums.size
        if (n < 4) return 0L
        val NEG = Long.MIN_VALUE / 4
        var dp0 = nums[0].toLong()
        var dp1 = NEG
        var dp2 = NEG
        var dp3 = NEG
        var ans = NEG
        for (i in 1 until n) {
            val cur = nums[i].toLong()
            var ndp0 = maxOf(dp0 + cur, cur)
            var ndp1 = NEG
            var ndp2 = NEG
            var ndp3 = NEG
            if (nums[i] > nums[i - 1]) {
                ndp1 = maxOf(
                    if (dp1 != NEG) dp1 + cur else NEG,
                    dp0 + cur
                )
                ndp3 = maxOf(
                    if (dp3 != NEG) dp3 + cur else NEG,
                    if (dp2 != NEG) dp2 + cur else NEG
                )
            } else if (nums[i] < nums[i - 1]) {
                ndp2 = maxOf(
                    if (dp2 != NEG) dp2 + cur else NEG,
                    if (dp1 != NEG) dp1 + cur else NEG
                )
            }
            if (ndp3 > ans) ans = ndp3
            dp0 = ndp0
            dp1 = ndp1
            dp2 = ndp2
            dp3 = ndp3
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxSumTrionic(List<int> nums) {
    const int NEG = - (1 << 60);
    int n = nums.length;
    List<int> dp0 = List.filled(n, NEG);
    List<int> dp1 = List.filled(n, NEG);
    List<int> dp2 = List.filled(n, NEG);
    List<int> dp3 = List.filled(n, NEG);

    dp0[0] = nums[0];
    int ans = NEG;

    for (int i = 1; i < n; ++i) {
      if (nums[i] > nums[i - 1]) {
        // phase 0 continues
        if (dp0[i - 1] != NEG) dp0[i] = dp0[i - 1] + nums[i];

        // transition to / continue phase 1
        int candA = dp1[i - 1] != NEG ? dp1[i - 1] + nums[i] : NEG;
        int candB = dp0[i - 1] != NEG ? dp0[i - 1] + nums[i] : NEG;
        dp1[i] = max(candA, candB);

        // transition to / continue phase 3
        int candC = dp3[i - 1] != NEG ? dp3[i - 1] + nums[i] : NEG;
        int candD = dp2[i - 1] != NEG ? dp2[i - 1] + nums[i] : NEG;
        dp3[i] = max(candC, candD);
      } else if (nums[i] < nums[i - 1]) {
        // transition to / continue phase 2
        int candA = dp2[i - 1] != NEG ? dp2[i - 1] + nums[i] : NEG;
        int candB = dp1[i - 1] != NEG ? dp1[i - 1] + nums[i] : NEG;
        dp2[i] = max(candA, candB);
      } else {
        // equal elements break any ongoing phase; keep NEG (already set)
      }

      if (dp3[i] > ans) ans = dp3[i];
    }

    return ans;
  }
}
```

## Golang

```go
func maxSumTrionic(nums []int) int64 {
	const negInf = -1 << 60 // sufficiently small
	n := len(nums)
	if n < 4 {
		return 0
	}
	prev0 := int64(nums[0])
	prev1, prev2, prev3 := negInf, negInf, negInf
	ans := negInf

	for i := 1; i < n; i++ {
		cur0, cur1, cur2, cur3 := negInf, negInf, negInf, negInf
		val := int64(nums[i])

		// dp0: start a new subarray at i or extend previous increasing segment
		cur0 = val
		if nums[i] > nums[i-1] && prev0 != negInf {
			if tmp := prev0 + val; tmp > cur0 {
				cur0 = tmp
			}
		}

		// dp1: after first increase, still increasing (or just started)
		if nums[i] > nums[i-1] {
			if prev1 != negInf {
				if tmp := prev1 + val; tmp > cur1 {
					cur1 = tmp
				}
			}
			if prev0 != negInf {
				if tmp := prev0 + val; tmp > cur1 {
					cur1 = tmp
				}
			}
		}

		// dp2: decreasing phase after first increase
		if nums[i] < nums[i-1] {
			if prev2 != negInf {
				if tmp := prev2 + val; tmp > cur2 {
					cur2 = tmp
				}
			}
			if prev1 != negInf {
				if tmp := prev1 + val; tmp > cur2 {
					cur2 = tmp
				}
			}
		}

		// dp3: final increasing phase after decrease
		if nums[i] > nums[i-1] {
			if prev3 != negInf {
				if tmp := prev3 + val; tmp > cur3 {
					cur3 = tmp
				}
			}
			if prev2 != negInf {
				if tmp := prev2 + val; tmp > cur3 {
					cur3 = tmp
				}
			}
		}

		if cur3 > ans {
			ans = cur3
		}
		prev0, prev1, prev2, prev3 = cur0, cur1, cur2, cur3
	}
	return ans
}
```

## Ruby

```ruby
def max_sum_trionic(nums)
  neg_inf = -(1 << 60)
  inc = neg_inf      # first increasing segment
  dec = neg_inf      # after decreasing segment
  inc2 = neg_inf     # second increasing segment (complete trionic)
  ans = neg_inf

  (1...nums.length).each do |i|
    a = nums[i - 1]
    b = nums[i]

    new_inc = neg_inf
    new_dec = neg_inf
    new_inc2 = inc2

    if b > a
      start_inc = a + b
      extend_inc = inc != neg_inf ? inc + b : neg_inf
      new_inc = [extend_inc, start_inc].max

      extend_inc2 = inc2 != neg_inf ? inc2 + b : neg_inf
      from_dec = dec != neg_inf ? dec + b : neg_inf
      new_inc2 = [extend_inc2, from_dec].max
    end

    if b < a
      extend_dec = dec != neg_inf ? dec + b : neg_inf
      start_dec = inc != neg_inf ? inc + b : neg_inf
      new_dec = [extend_dec, start_dec].max
    end

    inc = new_inc
    dec = new_dec
    inc2 = new_inc2
    ans = inc2 if inc2 > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
  def maxSumTrionic(nums: Array[Int]): Long = {
    val n = nums.length
    val NEG = Long.MinValue / 4

    var dp0: Long = NEG // after first increasing phase
    var dp1: Long = NEG // after second phase (still increasing)
    var dp2: Long = NEG // after decreasing phase
    var dp3: Long = NEG // after final increasing phase
    var ans: Long = NEG

    for (i <- 1 until n) {
      val cur = nums(i).toLong
      if (nums(i) > nums(i - 1)) {
        // compute new states based on previous values
        val newDp0 = if (dp0 != NEG) dp0 + cur else nums(i - 1).toLong + cur

        var cand1 = NEG
        if (dp1 != NEG) cand1 = dp1 + cur
        var cand2 = NEG
        if (dp0 != NEG) cand2 = dp0 + cur
        val newDp1 = math.max(cand1, cand2)

        var cand31 = NEG
        if (dp3 != NEG) cand31 = dp3 + cur
        var cand32 = NEG
        if (dp2 != NEG) cand32 = dp2 + cur
        val newDp3 = math.max(cand31, cand32)

        dp0 = newDp0
        dp1 = newDp1
        dp3 = newDp3
      } else if (nums(i) < nums(i - 1)) {
        // a decreasing step breaks the first increasing phase
        dp0 = NEG

        var cand21 = NEG
        if (dp2 != NEG) cand21 = dp2 + cur
        var cand22 = NEG
        if (dp1 != NEG) cand22 = dp1 + cur
        val newDp2 = math.max(cand21, cand22)

        dp2 = newDp2
      } else {
        // equal values break strict monotonicity completely
        dp0 = NEG
        dp1 = NEG
        dp2 = NEG
        dp3 = NEG
      }

      if (dp3 > ans) ans = dp3
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum_trionic(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        const NEG: i64 = i64::MIN / 4;
        if n < 4 {
            return 0;
        }
        let mut inc1 = NEG; // up segment
        let mut dec = NEG;  // up-down segment
        let mut inc2 = NEG; // up-down-up (complete)
        let mut ans = NEG;

        for i in 1..n {
            let a = nums[i - 1] as i64;
            let b = nums[i] as i64;
            let (new_inc1, new_dec, new_inc2);
            if b > a {
                // extend or start first increasing segment
                let cand1 = if inc1 != NEG { inc1 + b } else { NEG };
                let cand2 = a + b; // start with two elements
                new_inc1 = std::cmp::max(cand1, cand2);
                // decreasing phase cannot continue on increase
                new_dec = NEG;
                // extend or start final increasing segment from dec
                let cand3 = if inc2 != NEG { inc2 + b } else { NEG };
                let cand4 = if dec != NEG { dec + b } else { NEG };
                new_inc2 = std::cmp::max(cand3, cand4);
            } else if b < a {
                // cannot be in first increasing segment
                new_inc1 = NEG;
                // extend or start decreasing segment
                let cand1 = if dec != NEG { dec + b } else { NEG };
                let cand2 = if inc1 != NEG { inc1 + b } else { NEG };
                new_dec = std::cmp::max(cand1, cand2);
                new_inc2 = NEG;
            } else {
                // equal breaks strictness
                new_inc1 = NEG;
                new_dec = NEG;
                new_inc2 = NEG;
            }
            if new_inc2 > ans {
                ans = new_inc2;
            }
            inc1 = new_inc1;
            dec = new_dec;
            inc2 = new_inc2;
        }

        ans
    }
}
```

## Racket

```racket
(define INF (expt 10 18))

(define/contract (max-sum-trionic nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (dp0 (make-vector n (- INF)))
         (dp1 (make-vector n (- INF)))
         (dp2 (make-vector n (- INF)))
         (dp3 (make-vector n (- INF))))
    (vector-set! dp0 0 (list-ref nums 0))
    (for ([i (in-range 1 n)])
      (define cur (list-ref nums i))
      (define prev (list-ref nums (- i 1)))
      (when (> cur prev)
        (define val0 (+ (vector-ref dp0 (- i 1)) cur))
        (vector-set! dp0 i val0)
        (define val1 (max (+ (vector-ref dp1 (- i 1)) cur)
                          (+ (vector-ref dp0 (- i 1)) cur)))
        (vector-set! dp1 i val1)
        (define val3 (max (+ (vector-ref dp3 (- i 1)) cur)
                          (+ (vector-ref dp2 (- i 1)) cur)))
        (vector-set! dp3 i val3))
      (when (< cur prev)
        (define val2 (max (+ (vector-ref dp2 (- i 1)) cur)
                          (+ (vector-ref dp1 (- i 1)) cur)))
        (vector-set! dp2 i val2))
      ;; start a new subarray at position i for the first increasing phase
      (when (> cur (vector-ref dp0 i))
        (vector-set! dp0 i cur)))
    (let ((ans (- INF)))
      (for ([i (in-range n)])
        (set! ans (max ans (vector-ref dp3 i))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([max_sum_trionic/1]).

max_sum_trionic(Nums) ->
    NegInf = -1000000000000000000,
    case Nums of
        [] -> 0;
        [First|Rest] ->
            loop(Rest, First, First, NegInf, NegInf, NegInf, NegInf)
    end.

loop([], _Prev, _Cur0, _Cur1, _Cur2, Cur3, MaxAns) ->
    max(Cur3, MaxAns);
loop([Curr|Rest], Prev, Cur0, Cur1, Cur2, Cur3, MaxAns) ->
    NegInf = -1000000000000000000,
    if
        Curr > Prev ->
            New0 = max(Cur0 + Curr, Curr),
            New1 = case Cur1 of
                NegInf -> Cur0 + Curr;
                _ -> max(Cur1 + Curr, Cur0 + Curr)
            end,
            CandFrom2 = case Cur2 of
                NegInf -> NegInf;
                _ -> Cur2 + Curr
            end,
            CandFrom3 = case Cur3 of
                NegInf -> NegInf;
                _ -> Cur3 + Curr
            end,
            New3 = max(CandFrom2, CandFrom3),
            MaxAns1 = max(MaxAns, New3),
            loop(Rest, Curr, New0, New1, NegInf, New3, MaxAns1);
        Curr < Prev ->
            New0 = Curr,
            New1 = NegInf,
            CandFrom1 = case Cur1 of
                NegInf -> NegInf;
                _ -> Cur1 + Curr
            end,
            CandFrom2 = case Cur2 of
                NegInf -> NegInf;
                _ -> Cur2 + Curr
            end,
            New2 = case {CandFrom1, CandFrom2} of
                {NegInf,_} -> NegInf;
                {_,NegInf} -> CandFrom1;
                _ -> max(CandFrom1, CandFrom2)
            end,
            loop(Rest, Curr, New0, New1, New2, NegInf, MaxAns);
        true ->
            % equal elements break the pattern
            loop(Rest, Curr, Curr, NegInf, NegInf, NegInf, MaxAns)
    end.

max(A,B) when A >= B -> A;
max(_,B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_trionic(nums :: [integer]) :: integer
  def max_sum_trionic(nums) do
    neg_inf = -10_000_000_000_000_000_000

    [first | rest] = nums

    {_, _, _, ans, _} =
      Enum.reduce(rest, {first, neg_inf, neg_inf, neg_inf, first}, fn cur,
                                                                      {dp0, dp1, dp2, dp3, prev} ->
        cond do
          cur > prev ->
            ndp1 = max(dp1 + cur, dp0 + cur)
            ndp3 = max(dp3 + cur, dp2 + cur)
            ndp0 = max(dp0 + cur, cur)
            nans = max(ans, ndp3)
            {ndp0, ndp1, dp2, ndp3, cur}

          cur < prev ->
            ndp2 = max(dp2 + cur, dp1 + cur)
            ndp0 = cur
            {ndp0, dp1, ndp2, dp3, cur}

          true ->
            {neg_inf, neg_inf, neg_inf, neg_inf, cur}
        end
      end)

    ans
  end
end
```

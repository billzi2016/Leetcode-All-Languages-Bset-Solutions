# 3139. Minimum Cost to Equalize Array

## Cpp

```cpp
class Solution {
public:
    int minCostToEqualizeArray(vector<int>& nums, int cost1, int cost2) {
        const long long MOD = 1000000007LL;
        int n = nums.size();
        long long sum = 0;
        int mx = nums[0], mn = nums[0];
        for (int v : nums) {
            sum += v;
            if (v > mx) mx = v;
            if (v < mn) mn = v;
        }
        long long D = 1LL * n * mx - sum; // total increments needed
        if (D == 0) return 0;
        long long c1 = cost1, c2 = cost2;
        if (c2 >= 2LL * c1) {
            long long ans = (D % MOD) * (c1 % MOD) % MOD;
            return (int)ans;
        }
        long long max_delta = mx - mn;
        long long pairs_by_other = D - max_delta; // increments available from other elements
        long long pairs_limit = min(D / 2, pairs_by_other);
        long long singles = D - 2 * pairs_limit;
        long long ans = (pairs_limit % MOD) * (c2 % MOD) % MOD;
        ans = (ans + (singles % MOD) * (c1 % MOD)) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int minCostToEqualizeArray(int[] nums, int cost1, int cost2) {
        int n = nums.length;
        long sum = 0;
        int maxVal = Integer.MIN_VALUE;
        int minVal = Integer.MAX_VALUE;
        for (int v : nums) {
            sum += v;
            if (v > maxVal) maxVal = v;
            if (v < minVal) minVal = v;
        }
        long c1 = cost1;
        long c2 = cost2;
        
        // If using pair operation is never cheaper
        if (c2 >= 2L * c1) {
            long diffSum = 0;
            for (int v : nums) diffSum += (long) maxVal - v;
            return (int) ((diffSum % MOD) * (c1 % MOD) % MOD);
        }
        
        // Special case n == 2
        if (n == 2) {
            long ans = (long) (maxVal - minVal) * c1 % MOD;
            return (int) ans;
        }
        
        // General case n >= 3 and pair operation may be useful
        long candidateT = maxVal; // at least the current maximum
        
        // Compute threshold where max delta <= sum of others
        long numerator = sum - 2L * maxVal;          // can be negative
        long denominator = n - 2L;
        if (numerator > 0) {
            long tThresh = ceilDiv(numerator, denominator);
            if (tThresh > candidateT) candidateT = tThresh;
        }
        
        long ans = Math.min(costAtTarget(maxVal, nums, sum, maxVal, c1, c2),
                            costAtTarget(candidateT, nums, sum, maxVal, c1, c2));
        return (int) (ans % MOD);
    }
    
    private long costAtTarget(long T, int[] nums, long totalSum, int maxVal,
                              long c1, long c2) {
        int n = nums.length;
        long mxDelta = T - maxVal;                 // delta of the original maximum element
        long D = (long) n * T - totalSum;          // total increments needed
        long S = D - mxDelta;                      // sum of deltas of other elements
        
        long pairs = Math.min(D / 2, S);
        long singles = D - 2L * pairs;
        
        long costPairs = (pairs % MOD) * (c2 % MOD) % MOD;
        long costSingles = (singles % MOD) * (c1 % MOD) % MOD;
        return (costPairs + costSingles) % MOD;
    }
    
    private static long ceilDiv(long a, long b) {
        // b > 0
        if (a >= 0) {
            return (a + b - 1) / b;
        } else {
            return a / b; // division truncates toward zero which is ceiling for negatives
        }
    }
}
```

## Python

```python
class Solution(object):
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        """
        :type nums: List[int]
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        mx = max(nums)
        mn = min(nums)

        # If using double operation is never cheaper than two singles
        if cost2 >= 2 * cost1:
            total_deficit = sum(mx - x for x in nums)
            return (total_deficit * cost1) % MOD

        # Special handling for n == 2 (already covered by above condition,
        # but keep for completeness)
        if n == 2:
            diff = mx - mn
            return (diff * cost1) % MOD

        S = sum(nums)

        # Compute candidate target values
        numerator = S - 2 * mn
        denom = n - 2
        if numerator <= 0:
            t_needed = 0
        else:
            t_needed = (numerator + denom - 1) // denom  # ceil division

        T0 = max(mx, t_needed)
        candidates = [T0]
        if T0 - 1 >= mx:
            candidates.append(T0 - 1)

        best = None
        for T in candidates:
            D = n * T - S                     # total deficit
            maxd = T - mn                     # largest individual deficit
            other = D - maxd                  # sum of deficits excluding the smallest element
            k = min(D // 2, other)            # number of double operations
            singles = D - 2 * k               # remaining single increments
            cost = k * cost2 + singles * cost1
            if best is None or cost < best:
                best = cost

        return best % MOD
```

## Python3

```python
import sys
from typing import List

MOD = 10**9 + 7

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        max_val = max(nums)
        total_sum = sum(nums)
        # If using two-element operation is not cheaper than two single operations
        if cost2 >= 2 * cost1:
            inc_total = n * max_val - total_sum
            return (inc_total % MOD) * (cost1 % MOD) % MOD

        # cost2 < 2*cost1, try to maximize paired increments
        if n == 2:
            # Only need to raise the smaller element up to the larger one
            inc = max_val - min(nums)
            return (inc % MOD) * (cost1 % MOD) % MOD

        m = min(nums)

        # Determine minimal target T such that all increments can be paired
        num = total_sum - 2 * m
        den = n - 2
        if num <= 0:
            T_needed = max_val
        else:
            T_needed = (num + den - 1) // den
            if T_needed < max_val:
                T_needed = max_val

        T = T_needed
        inc_total = n * T - total_sum          # S
        max_inc = T - m                        # largest individual increment
        pairs_limit1 = inc_total // 2
        pairs_limit2 = inc_total - max_inc
        pairs = min(pairs_limit1, pairs_limit2)

        cost = (pairs % MOD) * (cost2 % MOD)
        remaining = inc_total - 2 * pairs
        cost = (cost + (remaining % MOD) * (cost1 % MOD)) % MOD
        return cost
```

## C

```c
#include <limits.h>

int minCostToEqualizeArray(int* nums, int numsSize, int cost1, int cost2) {
    const long long MOD = 1000000007LL;
    if (numsSize == 0) return 0;
    
    int maxVal = INT_MIN;
    int minVal = INT_MAX;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > maxVal) maxVal = nums[i];
        if (nums[i] < minVal) minVal = nums[i];
    }
    
    long long totalInc = 0;
    for (int i = 0; i < numsSize; ++i) {
        totalInc += (long long)(maxVal - nums[i]);
    }
    
    long long maxDelta = (long long)(maxVal - minVal);
    
    long long ans;
    if ((long long)cost2 >= 2LL * cost1) {
        ans = (totalInc % MOD) * (cost1 % MOD) % MOD;
    } else {
        long long k = totalInc / 2;                     // max possible pairs by count
        long long limit = totalInc - maxDelta;          // limited by other elements
        if (limit < k) k = limit;
        long long remainingSingles = totalInc - 2 * k;
        ans = (remainingSingles % MOD) * (cost1 % MOD) % MOD;
        ans = (ans + (k % MOD) * (cost2 % MOD)) % MOD;
    }
    
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
public class Solution {
    private const int MOD = 1000000007;
    public int MinCostToEqualizeArray(int[] nums, int cost1, int cost2) {
        int n = nums.Length;
        if (n == 1) return 0;
        long sum = 0;
        int min = int.MaxValue;
        int max = int.MinValue;
        foreach (int v in nums) {
            sum += v;
            if (v < min) min = v;
            if (v > max) max = v;
        }
        // If using only single increments is cheaper or equal
        if ((long)cost2 >= 2L * cost1) {
            long totalInc = (long)n * max - sum;
            long ans = (totalInc % MOD) * cost1 % MOD;
            return (int)ans;
        }
        // n == 2 case: optimal target is max
        if (n == 2) {
            long totalInc = (long)n * max - sum; // equals max-min
            long ans = totalInc * cost1 % MOD;
            return (int)ans;
        }
        // Helper to compute cost for a given target T
        long ComputeCost(long T) {
            long S = (long)n * T - sum;          // total increments needed
            long M = T - min;                    // max delta
            long pairsLimit1 = S - M;            // limited by largest element
            long pairsLimit2 = S / 2;            // limited by total halves
            long pairs = Math.Min(pairsLimit1, pairsLimit2);
            if (pairs < 0) pairs = 0;
            long singles = S - 2 * pairs;
            return pairs * cost2 + singles * cost1;
        }
        long best = ComputeCost(max);
        // candidate where pairing becomes limited by total halves
        long numerator = sum - 2L * min; // may be negative
        long denominator = n - 2;
        long Tcand = max;
        if (denominator > 0) {
            long need = numerator <= 0 ? 0 : (numerator + denominator - 1) / denominator;
            if (need > Tcand) Tcand = need;
        }
        // evaluate around this candidate
        for (long T = Math.Max(max, Tcand); T <= Math.Max(max, Tcand) + 2; T++) {
            long cost = ComputeCost(T);
            if (cost < best) best = cost;
        }
        return (int)(best % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} cost1
 * @param {number} cost2
 * @return {number}
 */
var minCostToEqualizeArray = function(nums, cost1, cost2) {
    const MOD = 1000000007n;
    let maxVal = -Infinity;
    let minVal = Infinity;
    for (let v of nums) {
        if (v > maxVal) maxVal = v;
        if (v < minVal) minVal = v;
    }
    // total increments needed to raise all elements to current maximum
    let D = 0n;
    for (let v of nums) {
        D += BigInt(maxVal - v);
    }
    const c1 = BigInt(cost1);
    const c2 = BigInt(cost2);
    // If using two-element operation is not cheaper than two single operations
    if (c2 >= 2n * c1) {
        const ans = (D % MOD) * (c1 % MOD) % MOD;
        return Number(ans);
    }
    const maxDelta = BigInt(maxVal - minVal); // largest individual increment needed
    const halfFloor = D / 2n;
    const diff = D - maxDelta >= 0n ? D - maxDelta : 0n;
    const pairs = halfFloor < diff ? halfFloor : diff; // maximum number of double ops
    const remaining = D - 2n * pairs; // increments left for single ops
    let ans = (pairs % MOD) * (c2 % MOD) + (remaining % MOD) * (c1 % MOD);
    ans %= MOD;
    return Number(ans);
};
```

## Typescript

```typescript
function minCostToEqualizeArray(nums: number[], cost1: number, cost2: number): number {
    const MOD = 1000000007n;
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    let total = 0n;
    let maxDiff = 0n;
    for (const v of nums) {
        const diff = BigInt(maxVal - v);
        total += diff;
        if (diff > maxDiff) maxDiff = diff;
    }

    const c1 = BigInt(cost1);
    const c2 = BigInt(cost2);

    let ans: bigint;

    if (c2 >= 2n * c1) {
        // Only use single increments
        ans = (total % MOD) * (c1 % MOD) % MOD;
    } else {
        let pairs: bigint;
        if (maxDiff > total - maxDiff) {
            pairs = total - maxDiff; // limited by smaller elements
        } else {
            pairs = total / 2n; // can pair all possible increments
        }
        const singles = total - 2n * pairs;
        ans = ((pairs % MOD) * (c2 % MOD)) % MOD;
        ans = (ans + ((singles % MOD) * (c1 % MOD)) % MOD) % MOD;
    }

    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $cost1
     * @param Integer $cost2
     * @return Integer
     */
    function minCostToEqualizeArray($nums, $cost1, $cost2) {
        $mod = 1000000007;
        $maxVal = max($nums);
        $sumDelta = 0;
        $maxDeficit = 0;
        foreach ($nums as $v) {
            $def = $maxVal - $v;
            $sumDelta += $def;
            if ($def > $maxDeficit) {
                $maxDeficit = $def;
            }
        }

        // If using two-element operation is not cheaper than two single operations
        if ($cost2 >= 2 * $cost1) {
            $ans = ($sumDelta % $mod) * ($cost1 % $mod);
            return $ans % $mod;
        }

        // Maximum number of pair operations we can perform
        $pairsBySum = intdiv($sumDelta, 2);
        $pairsLimited = $sumDelta - $maxDeficit; // total deficit excluding the largest one
        if ($pairsLimited < 0) {
            $pairsLimited = 0;
        }
        $p = min($pairsBySum, $pairsLimited);

        $remaining = $sumDelta - 2 * $p; // single increments needed

        $ans = ( ($p % $mod) * ($cost2 % $mod) ) % $mod;
        $ans = ($ans + ( ($remaining % $mod) * ($cost1 % $mod) )) % $mod;

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minCostToEqualizeArray(_ nums: [Int], _ cost1: Int, _ cost2: Int) -> Int {
        let MOD: Int64 = 1_000_000_007
        let n = nums.count
        var sum: Int64 = 0
        var maxVal = 0
        for v in nums {
            sum += Int64(v)
            if v > maxVal { maxVal = v }
        }
        
        // If using two-element operation is not cheaper per unit, just use single increments.
        if Int64(cost2) >= 2 * Int64(cost1) {
            let delta = Int64(n) * Int64(maxVal) - sum   // total increments needed
            var ans = (delta % MOD) * Int64(cost1) % MOD
            if ans < 0 { ans += MOD }
            return Int(ans)
        }
        
        // Helper to compute cost for a given total increment delta.
        func costFor(_ delta: Int64) -> Int64 {
            let pairs = delta / 2
            let rem = delta % 2
            return (pairs * Int64(cost2) + rem * Int64(cost1)) % MOD
        }
        
        var delta0 = Int64(n) * Int64(maxVal) - sum   // using target = maxVal
        var answer = costFor(delta0)
        
        // When n is odd, checking target = maxVal + 1 may give lower cost.
        if n % 2 == 1 {
            let delta1 = delta0 + Int64(n)   // increase target by 1
            let cand = costFor(delta1)
            if cand < answer { answer = cand }
        }
        
        return Int(answer % MOD)
    }
}
```

## Kotlin

```kotlin
import java.util.*
import kotlin.math.*

class Solution {
    private val MOD = 1_000_000_007L

    fun minCostToEqualizeArray(nums: IntArray, cost1: Int, cost2: Int): Int {
        val n = nums.size
        if (n == 1) return 0
        var sum = 0L
        var maxVal = Int.MIN_VALUE
        var minVal = Int.MAX_VALUE
        for (v in nums) {
            sum += v.toLong()
            if (v > maxVal) maxVal = v
            if (v < minVal) minVal = v
        }
        val c1 = cost1.toLong()
        val c2 = cost2.toLong()

        // If using double operation is never cheaper than two singles
        if (c2 >= 2L * c1) {
            val need = maxVal.toLong() * n - sum
            return ((need % MOD) * (c1 % MOD) % MOD).toInt()
        }

        fun computeCost(target: Long): Long {
            val S = target * n - sum          // total increments needed
            val D = target - minVal           // max delta
            if (2L * D <= S) {
                val half = S / 2L
                val rem = S % 2L
                return half * c2 + rem * c1
            } else {
                val k = S - D                  // number of double ops we can use
                return k * c2 + (2L * D - S) * c1
            }
        }

        var best = computeCost(maxVal.toLong())

        if (n > 2) {
            // slope in region where 2D > S
            val slope = (n - 1).toLong() * c2 - (n - 2).toLong() * c1
            if (slope < 0L) {
                // find smallest T satisfying 2D <= S
                var numerator = sum - 2L * minVal
                var denominator = (n - 2).toLong()
                var tNeeded = if (numerator <= 0L) maxVal.toLong() else (numerator + denominator - 1) / denominator
                if (tNeeded < maxVal) tNeeded = maxVal.toLong()
                // evaluate at boundary and maybe next value
                best = min(best, computeCost(tNeeded))
                best = min(best, computeCost(tNeeded + 1))
            }
        }

        return ((best % MOD + MOD) % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;
  int minCostToEqualizeArray(List<int> nums, int cost1, int cost2) {
    int n = nums.length;
    if (n <= 1) return 0;

    int maxVal = nums[0];
    for (int v in nums) if (v > maxVal) maxVal = v;

    int sumDiff = 0;
    int maxDiff = 0;
    for (int v in nums) {
      int d = maxVal - v;
      sumDiff += d;
      if (d > maxDiff) maxDiff = d;
    }

    // If using only single increments is never worse.
    if (cost2 >= 2 * cost1) {
      return ((sumDiff % _MOD) * (cost1 % _MOD)) % _MOD;
    }

    // Cost when target equals current maximum.
    int k0 = sumDiff ~/ 2;
    int limit = sumDiff - maxDiff;
    if (k0 > limit) k0 = limit;
    int singles0 = sumDiff - 2 * k0;
    int cost0 = ((singles0 % _MOD) * (cost1 % _MOD) + (k0 % _MOD) * (cost2 % _MOD)) % _MOD;

    int answer = cost0;

    // Try increasing the target if it can improve pairing (only when n > 2).
    if (n > 2) {
      int need = 2 * maxDiff - sumDiff;
      if (need > 0) {
        int denom = n - 2;
        int x = (need + denom - 1) ~/ denom; // ceil division
        int total = sumDiff + n * x;
        int k1 = total ~/ 2;
        int singles1 = total - 2 * k1;
        int cost1calc = ((singles1 % _MOD) * (cost1 % _MOD) + (k1 % _MOD) * (cost2 % _MOD)) % _MOD;
        if (cost1calc < answer) answer = cost1calc;
      }
    }

    return answer;
  }
}
```

## Golang

```go
func minCostToEqualizeArray(nums []int, cost1 int, cost2 int) int {
	const MOD int64 = 1000000007
	n := len(nums)
	if n == 1 {
		return 0
	}
	var sum int64
	maxVal := nums[0]
	minVal := nums[0]
	for _, v := range nums {
		sum += int64(v)
		if v > maxVal {
			maxVal = v
		}
		if v < minVal {
			minVal = v
		}
	}
	c1 := int64(cost1)
	c2 := int64(cost2)

	// If using pair operation is not cheaper than two singles, never use it.
	if c2 >= 2*c1 {
		totalDef := int64(n)*int64(maxVal) - sum
		ans := (totalDef % MOD) * (c1 % MOD) % MOD
		return int(ans)
	}
	// Special case for n == 2: pair operation cannot change the difference.
	if n == 2 {
		diff := maxVal - minVal
		ans := (int64(diff) % MOD) * (c1 % MOD) % MOD
		return int(ans)
	}

	// Helper to compute cost for a given target T.
	computeCost := func(T int64) int64 {
		S := int64(n)*T - sum               // total deficit
		maxDef := T - int64(minVal)          // largest individual deficit
		excess := int64(0)
		if 2*maxDef > S {
			excess = 2*maxDef - S
		}
		b := excess                         // singles needed at least
		if (b%2) != (S%2) {                 // adjust parity so remaining is even
			b++
		}
		a := (S - b) / 2                     // number of pair operations
		return a*c2 + b*c1
	}

	candidates := []int64{int64(maxVal)}

	// Determine T where excess becomes zero.
	numer := sum - 2*int64(minVal)
	denom := int64(n - 2)
	var t0 int64
	if numer <= 0 {
		t0 = int64(maxVal)
	} else {
		t0 = (numer + denom - 1) / denom // ceil division
		if t0 < int64(maxVal) {
			t0 = int64(maxVal)
		}
	}
	candidates = append(candidates, t0, t0+1)

	minAns := int64(1<<63 - 1)
	for _, T := range candidates {
		if T < int64(maxVal) {
			continue
		}
		cost := computeCost(T)
		if cost < minAns {
			minAns = cost
		}
	}
	return int(minAns % MOD)
}
```

## Ruby

```ruby
def min_cost_to_equalize_array(nums, cost1, cost2)
  mod = 1_000_000_007
  n = nums.length
  max_val = nums.max
  sum = nums.sum
  total_deficit = max_val * n - sum
  return 0 if total_deficit == 0

  if cost2 >= 2 * cost1
    return (total_deficit % mod) * (cost1 % mod) % mod
  end

  min_val = nums.min
  max_deficit = max_val - min_val
  pairs = [total_deficit / 2, total_deficit - max_deficit].min
  singles = total_deficit - 2 * pairs

  ((pairs % mod) * (cost2 % mod) + (singles % mod) * (cost1 % mod)) % mod
end
```

## Scala

```scala
object Solution {
    def minCostToEqualizeArray(nums: Array[Int], cost1: Int, cost2: Int): Int = {
        val MOD = 1000000007L
        val n = nums.length
        if (n <= 1) return 0
        var sumLong = 0L
        var mn = Int.MaxValue
        var mx = Int.MinValue
        for (v <- nums) {
            sumLong += v
            if (v < mn) mn = v
            if (v > mx) mx = v
        }
        val c1 = cost1.toLong
        val c2 = cost2.toLong

        // If pair operation is not cheaper than two single operations
        if (c2 >= 2L * c1) {
            val target = mx.toLong
            val S = target * n - sumLong
            ((S % MOD) * (c1 % MOD) % MOD).toInt
        } else {
            // Helper to compute cost for a given target T
            def computeCost(T: Long): Long = {
                val S = T * n - sumLong          // total increments needed
                val maxd = T - mn                 // largest individual increment
                if (S >= 2L * maxd) {             // enough increments to pair all
                    val pairs = S / 2
                    val singles = S % 2
                    ((pairs % MOD) * (c2 % MOD) + (singles % MOD) * (c1 % MOD)) % MOD
                } else {
                    val pairs = S - maxd           // increments that can be paired
                    val singles = 2L * maxd - S    // remaining single increments
                    ((pairs % MOD) * (c2 % MOD) + (singles % MOD) * (c1 % MOD)) % MOD
                }
            }

            if (n == 2) {
                computeCost(mx.toLong).toInt
            } else {
                val targetM = mx.toLong
                var candidates = scala.collection.mutable.Set[Long]()
                candidates += targetM

                // Threshold where S >= 2*maxd becomes true
                val numerator = sumLong - 2L * mn
                val denom = n - 2
                var tThresh: Long =
                    if (numerator <= 0) targetM
                    else (numerator + denom - 1) / denom   // ceil division

                if (tThresh < targetM) tThresh = targetM

                candidates += tThresh
                candidates += tThresh + 1
                if (tThresh - 1 >= targetM) candidates += tThresh - 1

                var best = Long.MaxValue
                for (T <- candidates) {
                    val cost = computeCost(T)
                    if (cost < best) best = cost
                }
                (best % MOD).toInt
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost_to_equalize_array(nums: Vec<i32>, cost1: i32, cost2: i32) -> i32 {
        const MOD: i128 = 1_000_000_007;
        let n = nums.len() as i128;
        let mut sum: i128 = 0;
        let mut max_val: i128 = 0;
        for &v in &nums {
            let v = v as i128;
            sum += v;
            if v > max_val {
                max_val = v;
            }
        }
        let c1 = cost1 as i128;
        let c2 = cost2 as i128;

        let mut best: i128 = i128::MAX;
        // candidates: max and max+1 (the latter matters when n is odd)
        for &t in &[max_val, max_val + 1] {
            let need = n * t - sum; // total increments needed, non‑negative
            let cost = if c2 >= 2 * c1 {
                need * c1
            } else {
                let pairs = need / 2;
                let singles = need % 2;
                pairs * c2 + singles * c1
            };
            if cost < best {
                best = cost;
            }
        }

        (best % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (min-cost-to-equalize-array nums cost1 cost2)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((maxv (apply max nums))
         (minv (apply min nums))
         (total (foldl (lambda (x acc) (+ acc (- maxv x))) 0 nums))
         (max-delta (- maxv minv)))
    (if (>= cost2 (* 2 cost1))
        (modulo (* total cost1) MOD)
        (let* ((pairs (min (quotient total 2) (- total max-delta)))
               (cost (+ (* pairs cost2) (* (- total (* 2 pairs)) cost1))))
          (modulo cost MOD)))))
```

## Erlang

```erlang
-spec min_cost_to_equalize_array(Nums :: [integer()], Cost1 :: integer(), Cost2 :: integer()) -> integer().
min_cost_to_equalize_array(Nums, Cost1, Cost2) ->
    Mod = 1000000007,
    case length(Nums) of
        0 -> 0;
        1 -> 0;
        N ->
            Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
            MaxVal = lists:max(Nums),
            MinVal = lists:min(Nums),
            case Cost2 >= 2 * Cost1 of
                true ->
                    D = N * MaxVal - Sum,
                    ((D rem Mod) * (Cost1 rem Mod)) rem Mod;
                false ->
                    CostA = cost_for_t(N, Sum, MinVal, MaxVal, Cost1, Cost2),
                    TNeeded = case N of
                        2 -> MaxVal;
                        _ ->
                            Numer = Sum - 2 * MinVal,
                            Denom = N - 2,
                            Ceil = (Numer + Denom - 1) div Denom,
                            max(MaxVal, Ceil)
                    end,
                    CostB = cost_for_t(N, Sum, MinVal, TNeeded, Cost1, Cost2),
                    ((min(CostA, CostB)) rem Mod)
            end
    end.

cost_for_t(N, Sum, MinVal, T, C1, C2) ->
    D = N * T - Sum,
    MaxDelta = T - MinVal,
    PairMaxByTotal = D div 2,
    PairMaxByImbalance = D - MaxDelta,
    Pairs = if PairMaxByTotal =< PairMaxByImbalance -> PairMaxByTotal;
               true -> PairMaxByImbalance
            end,
    Pairs * C2 + (D - 2 * Pairs) * C1.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec min_cost_to_equalize_array(nums :: [integer], cost1 :: integer, cost2 :: integer) :: integer
  def min_cost_to_equalize_array(nums, cost1, cost2) do
    mod = 1_000_000_007
    max_val = Enum.max(nums)

    deficits =
      Enum.map(nums, fn x -> max_val - x end)

    total = Enum.sum(deficits)

    if total == 0 do
      0
    else
      maxd = Enum.max(deficits)

      if cost2 >= 2 * cost1 do
        rem(total * cost1, mod)
      else
        pair_ops = min(div(total, 2), total - maxd)
        singles = total - 2 * pair_ops
        ans = pair_ops * cost2 + singles * cost1
        rem(ans, mod)
      end
    end
  end
end
```

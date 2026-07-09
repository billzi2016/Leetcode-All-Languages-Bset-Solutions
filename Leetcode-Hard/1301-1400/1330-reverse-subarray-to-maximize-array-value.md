# 1330. Reverse Subarray To Maximize Array Value

## Cpp

```cpp
class Solution {
public:
    int maxValueAfterReverse(vector<int>& nums) {
        int n = nums.size();
        long long base = 0;
        for (int i = 0; i < n - 1; ++i) base += std::abs(nums[i] - nums[i + 1]);
        
        int bestGain = 0;
        // Case 1: reverse a prefix or suffix
        for (int i = 1; i <= n - 2; ++i) {
            bestGain = max(bestGain, std::abs(nums[i] - nums[0]) - std::abs(nums[i] - nums[i - 1]));
            bestGain = max(bestGain, std::abs(nums[i] - nums[n - 1]) - std::abs(nums[i + 1] - nums[i]));
        }
        
        // Case 2: reverse an internal subarray
        int maxLow = INT_MIN;   // maximum of min(a_i, a_{i+1})
        int minHigh = INT_MAX;  // minimum of max(a_i, a_{i+1})
        for (int i = 0; i < n - 1; ++i) {
            int low = std::min(nums[i], nums[i + 1]);
            int high = std::max(nums[i], nums[i + 1]);
            maxLow = std::max(maxLow, low);
            minHigh = std::min(minHigh, high);
        }
        bestGain = max(bestGain, 2 * (maxLow - minHigh));
        
        return static_cast<int>(base + bestGain);
    }
};
```

## Java

```java
class Solution {
    public int maxValueAfterReverse(int[] nums) {
        int n = nums.length;
        long base = 0;
        for (int i = 0; i < n - 1; i++) {
            base += Math.abs(nums[i] - nums[i + 1]);
        }

        // prefix min and max
        int[] prefMin = new int[n];
        int[] prefMax = new int[n];
        prefMin[0] = nums[0];
        prefMax[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefMin[i] = Math.min(prefMin[i - 1], nums[i]);
            prefMax[i] = Math.max(prefMax[i - 1], nums[i]);
        }

        // suffix min and max
        int[] suffMin = new int[n];
        int[] suffMax = new int[n];
        suffMin[n - 1] = nums[n - 1];
        suffMax[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.min(suffMin[i + 1], nums[i]);
            suffMax[i] = Math.max(suffMax[i + 1], nums[i]);
        }

        int bestGain = 0;

        // case where both ends improve simultaneously
        int mn = Integer.MAX_VALUE; // min of max pair
        int mx = Integer.MIN_VALUE; // max of min pair
        for (int i = 0; i < n - 1; i++) {
            int a = nums[i];
            int b = nums[i + 1];
            mn = Math.min(mn, Math.max(a, b));
            mx = Math.max(mx, Math.min(a, b));
        }
        bestGain = Math.max(bestGain, mx - mn);

        // improve one side using any earlier/later element
        for (int i = 0; i < n - 1; i++) {
            int cur = Math.abs(nums[i] - nums[i + 1]);

            // replace left edge with a later element
            int gainLeft = Math.max(suffMax[i + 1] - nums[i], nums[i] - suffMin[i + 1]) - cur;
            if (gainLeft > bestGain) bestGain = gainLeft;

            // replace right edge with an earlier element
            int gainRight = Math.max(nums[i + 1] - prefMin[i], prefMax[i] - nums[i + 1]) - cur;
            if (gainRight > bestGain) bestGain = gainRight;
        }

        return (int) (base + bestGain);
    }
}
```

## Python

```python
class Solution(object):
    def maxValueAfterReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        base = sum(abs(nums[i] - nums[i-1]) for i in range(1, n))
        best = 0

        # Cases where the reversed subarray touches an endpoint
        for i in range(1, n):
            best = max(best,
                       abs(nums[0] - nums[i]) - abs(nums[i] - nums[i-1]),
                       abs(nums[-1] - nums[i-1]) - abs(nums[i] - nums[i-1]))

        # Interior case: both ends are inside the array
        if n > 2:
            m = n - 1  # number of adjacent pairs
            r1 = [0] * m
            r2 = [0] * m
            r3 = [0] * m
            r4 = [0] * m

            for k in range(m):
                a, b = nums[k], nums[k+1]
                s = a + b               # sum of the pair
                d = a - b               # difference of the pair
                c = abs(d)              # original contribution of this edge
                r1[k] = s - c           # (a+b) - |a-b|
                r2[k] = -s - c          # -(a+b) - |a-b|
                r3[k] = d - c           # (a-b) - |a-b|
                r4[k] = -d - c          # -(a-b) - |a-b|

            # suffix maximums for each transformed array
            suff1 = [0] * m
            suff2 = [0] * m
            suff3 = [0] * m
            suff4 = [0] * m
            for k in range(m-1, -1, -1):
                if k == m-1:
                    suff1[k] = r1[k]
                    suff2[k] = r2[k]
                    suff3[k] = r3[k]
                    suff4[k] = r4[k]
                else:
                    suff1[k] = max(r1[k], suff1[k+1])
                    suff2[k] = max(r2[k], suff2[k+1])
                    suff3[k] = max(r3[k], suff3[k+1])
                    suff4[k] = max(r4[k], suff4[k+1])

            max_gain = 0
            for i in range(1, n-1):
                cL = abs(nums[i-1] - nums[i])          # original left edge contribution
                left_sum = nums[i-1] + nums[i]
                left_diff = nums[i-1] - nums[i]

                idx = i  # right edge index must be >= i
                gain1 = suff1[idx] - (left_sum + cL)            # both signs positive
                gain4 = suff2[idx] + (left_sum - cL)            # both signs negative
                gain3 = suff3[idx] - (left_diff + cL)           # first sign positive, second negative
                gain2 = suff4[idx] - (left_diff + cL)           # first sign negative, second positive

                max_gain = max(max_gain, gain1, gain2, gain3, gain4)

            best = max(best, max_gain)

        return base + best
```

## Python3

```python
class Solution:
    def maxValueAfterReverse(self, nums):
        n = len(nums)
        base = 0
        for i in range(1, n):
            base += abs(nums[i] - nums[i - 1])

        best_gain = 0

        # reverse a prefix or suffix
        first, last = nums[0], nums[-1]
        for i in range(1, n):
            cur = abs(nums[i] - nums[i - 1])
            best_gain = max(best_gain,
                            abs(first - nums[i]) - cur,
                            abs(last - nums[i - 1]) - cur)

        # reverse an internal subarray
        mn = float('inf')
        mx = -float('inf')
        for i in range(1, n):
            a, b = nums[i - 1], nums[i]
            mn = min(mn, max(a, b))
            mx = max(mx, min(a, b))

        best_gain = max(best_gain, mx - mn)

        return base + best_gain
```

## C

```c
int maxValueAfterReverse(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    long long base = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        int diff = nums[i] - nums[i + 1];
        if (diff < 0) diff = -diff;
        base += diff;
    }
    int best = 0;

    // Cases where the reversed subarray touches an endpoint
    for (int i = 0; i < numsSize - 1; ++i) {
        int cur = abs(nums[i] - nums[i + 1]) - abs(nums[0] - nums[i + 1]);
        if (cur > best) best = cur;
        cur = abs(nums[i] - nums[i + 1]) - abs(nums[numsSize - 1] - nums[i]);
        if (cur > best) best = cur;
    }

    // Cases where the reversed subarray is internal
    int mn = INT_MAX;   // minimum of the larger elements in each adjacent pair
    int mx = INT_MIN;   // maximum of the smaller elements in each adjacent pair
    for (int i = 0; i < numsSize - 1; ++i) {
        int a = nums[i];
        int b = nums[i + 1];
        int lo = a < b ? a : b;
        int hi = a > b ? a : b;
        if (hi < mn) mn = hi;
        if (lo > mx) mx = lo;
    }
    int internalGain = 2 * (mx - mn);
    if (internalGain > best) best = internalGain;

    return (int)(base + best);
}
```

## Csharp

```csharp
public class Solution {
    public int MaxValueAfterReverse(int[] nums) {
        int n = nums.Length;
        long baseSum = 0;
        for (int i = 0; i < n - 1; i++) {
            baseSum += Math.Abs(nums[i] - nums[i + 1]);
        }

        int bestGain = 0;

        // Case 1: reverse a prefix or suffix
        for (int i = 0; i < n - 1; i++) {
            int gainPrefix = Math.Abs(nums[i] - nums[0]) - Math.Abs(nums[i] - nums[i + 1]);
            if (gainPrefix > bestGain) bestGain = gainPrefix;

            int gainSuffix = Math.Abs(nums[n - 1] - nums[i + 1]) - Math.Abs(nums[i] - nums[i + 1]);
            if (gainSuffix > bestGain) bestGain = gainSuffix;
        }

        // Case 2: reverse a middle subarray
        int globalMin = int.MaxValue, globalMax = int.MinValue;
        foreach (int v in nums) {
            if (v < globalMin) globalMin = v;
            if (v > globalMax) globalMax = v;
        }

        for (int i = 0; i < n - 1; i++) {
            int diff = Math.Abs(nums[i] - nums[i + 1]);
            int candidate = Math.Max(Math.Abs(globalMin - nums[i]), Math.Abs(globalMax - nums[i + 1])) - diff;
            if (candidate > bestGain) bestGain = candidate;
        }

        return (int)(baseSum + bestGain);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxValueAfterReverse = function(nums) {
    const n = nums.length;
    let original = 0;
    for (let i = 1; i < n; ++i) {
        original += Math.abs(nums[i] - nums[i - 1]);
    }
    let bestGain = 0;
    let maxLow = -Infinity; // maximum of min(a[i], a[i-1])
    let minHigh = Infinity; // minimum of max(a[i], a[i-1])

    for (let i = 1; i < n; ++i) {
        const cur = Math.abs(nums[i] - nums[i - 1]);

        // reverse subarray that starts at index 0 and ends at i
        bestGain = Math.max(bestGain, Math.abs(nums[i] - nums[0]) - cur);
        // reverse subarray that starts at i-1 and ends at n-1
        bestGain = Math.max(bestGain, Math.abs(nums[i - 1] - nums[n - 1]) - cur);

        const low = Math.min(nums[i], nums[i - 1]);
        const high = Math.max(nums[i], nums[i - 1]);
        maxLow = Math.max(maxLow, low);
        minHigh = Math.min(minHigh, high);
    }

    // internal case: replace two edges simultaneously
    bestGain = Math.max(bestGain, 2 * (maxLow - minHigh));

    return original + bestGain;
};
```

## Typescript

```typescript
function maxValueAfterReverse(nums: number[]): number {
    const n = nums.length;
    let base = 0;
    for (let i = 1; i < n; ++i) {
        base += Math.abs(nums[i] - nums[i - 1]);
    }
    let minVal = Infinity, maxVal = -Infinity;
    for (const v of nums) {
        if (v < minVal) minVal = v;
        if (v > maxVal) maxVal = v;
    }
    const first = nums[0];
    const last = nums[n - 1];
    let bestGain = 0;
    for (let i = 0; i < n - 1; ++i) {
        const diff = Math.abs(nums[i] - nums[i + 1]);
        // bring an endpoint to the start
        bestGain = Math.max(bestGain, Math.abs(first - nums[i + 1]) - diff);
        // bring an endpoint to the end
        bestGain = Math.max(bestGain, Math.abs(last - nums[i]) - diff);
        if (i < n - 2) {
            const cand1 = Math.max(Math.abs(nums[i] - minVal), Math.abs(maxVal - nums[i + 1])) - diff;
            const cand2 = Math.max(Math.abs(nums[i] - maxVal), Math.abs(minVal - nums[i + 1])) - diff;
            bestGain = Math.max(bestGain, cand1, cand2);
        }
    }
    return base + bestGain;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxValueAfterReverse($nums) {
        $n = count($nums);
        $base = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $base += abs($nums[$i] - $nums[$i + 1]);
        }

        $maxGain = 0;

        // Case 1: reverse a prefix or suffix
        for ($i = 0; $i < $n - 1; $i++) {
            $cur = abs($nums[$i] - $nums[$i + 1]);

            $gain = abs($nums[0] - $nums[$i + 1]) - $cur;
            if ($gain > $maxGain) {
                $maxGain = $gain;
            }

            $gain = abs($nums[$n - 1] - $nums[$i]) - $cur;
            if ($gain > $maxGain) {
                $maxGain = $gain;
            }
        }

        // Case 2: reverse an internal subarray
        $maxMin = PHP_INT_MIN; // max of min(nums[i], nums[i+1])
        $minMax = PHP_INT_MAX; // min of max(nums[i], nums[i+1])

        for ($i = 0; $i < $n - 1; $i++) {
            $a = $nums[$i];
            $b = $nums[$i + 1];
            $mn = min($a, $b);
            $mx = max($a, $b);
            if ($mn > $maxMin) {
                $maxMin = $mn;
            }
            if ($mx < $minMax) {
                $minMax = $mx;
            }
        }

        $gain = 2 * ($maxMin - $minMax);
        if ($gain > $maxGain) {
            $maxGain = $gain;
        }

        return $base + $maxGain;
    }
}
```

## Swift

```swift
class Solution {
    func maxValueAfterReverse(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 1 { return 0 }
        var base = 0
        for i in 0..<(n - 1) {
            base += abs(nums[i] - nums[i + 1])
        }
        var bestImprove = 0
        
        // Edge improvements: reverse prefix or suffix
        for i in 0..<(n - 1) {
            let diff = abs(nums[i] - nums[i + 1])
            let cand1 = abs(nums[0] - nums[i + 1]) - diff
            if cand1 > bestImprove { bestImprove = cand1 }
            let cand2 = abs(nums[n - 1] - nums[i]) - diff
            if cand2 > bestImprove { bestImprove = cand2 }
        }
        
        // Internal improvements
        var curMin = Int.max
        var curMax = Int.min
        for i in 0..<(n - 1) {
            if nums[i] < curMin { curMin = nums[i] }
            if nums[i] > curMax { curMax = nums[i] }
            let diff = abs(nums[i] - nums[i + 1])
            let improve = max(abs(nums[i + 1] - curMin), abs(curMax - nums[i + 1])) - diff
            if improve > bestImprove { bestImprove = improve }
        }
        
        return base + bestImprove
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxValueAfterReverse(nums: IntArray): Int {
        val n = nums.size
        var base = 0L
        for (i in 1 until n) {
            base += kotlin.math.abs(nums[i] - nums[i - 1]).toLong()
        }
        var bestGain = 0L

        // Case 1: improve by moving an element to one of the ends
        var gainEnd = 0
        for (i in 1 until n) {
            val cur = kotlin.math.max(
                kotlin.math.abs(nums[i] - nums[0]),
                kotlin.math.abs(nums[i - 1] - nums[n - 1])
            ) - kotlin.math.abs(nums[i] - nums[i - 1])
            if (cur > gainEnd) gainEnd = cur
        }
        bestGain = kotlin.math.max(bestGain, gainEnd.toLong())

        // Case 2: internal improvement
        var minVal = nums[0]
        var maxVal = nums[0]
        for (i in 0 until n - 1) {
            val a = nums[i]
            val b = nums[i + 1]
            val cand1 = kotlin.math.abs(a - minVal) - kotlin.math.abs(b - a)
            if (cand1 > bestGain) bestGain = cand1.toLong()
            val cand2 = kotlin.math.abs(a - maxVal) - kotlin.math.abs(b - a)
            if (cand2 > bestGain) bestGain = cand2.toLong()
            // update extremes with b for future iterations
            if (b < minVal) minVal = b
            if (b > maxVal) maxVal = b
        }

        return (base + bestGain).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxValueAfterReverse(List<int> nums) {
    int n = nums.length;
    int total = 0;
    for (int i = 0; i < n - 1; ++i) {
      total += (nums[i] - nums[i + 1]).abs();
    }

    int bestGain = 0;

    // Case 1: reverse a subarray that touches one end
    for (int i = 0; i < n - 1; ++i) {
      int diff = (nums[i] - nums[i + 1]).abs();

      int gainStart = diff - (nums[0] - nums[i + 1]).abs();
      if (gainStart > bestGain) bestGain = gainStart;

      int gainEnd = diff - (nums[n - 1] - nums[i]).abs();
      if (gainEnd > bestGain) bestGain = gainEnd;
    }

    // Case 2: reverse a subarray that has both internal boundaries
    const int NEG_INF = -0x7fffffffffffffff; // sufficiently small
    int maxT1 = NEG_INF, maxT2 = NEG_INF, maxT3 = NEG_INF, maxT4 = NEG_INF;

    for (int i = 0; i < n - 1; ++i) {
      int a = nums[i];
      int b = nums[i + 1];
      int edge = (a - b).abs();

      if (i > 0) {
        int cand;
        cand = maxT1 + (a - b - edge);
        if (cand > bestGain) bestGain = cand;

        cand = maxT2 + (a + b - edge);
        if (cand > bestGain) bestGain = cand;

        cand = maxT3 + (-a - b - edge);
        if (cand > bestGain) bestGain = cand;

        cand = maxT4 + (-a + b - edge);
        if (cand > bestGain) bestGain = cand;
      }

      int t1 = -a + b - edge;
      if (t1 > maxT1) maxT1 = t1;

      int t2 = -a - b - edge;
      if (t2 > maxT2) maxT2 = t2;

      int t3 = a + b - edge;
      if (t3 > maxT3) maxT3 = t3;

      int t4 = a - b - edge;
      if (t4 > maxT4) maxT4 = t4;
    }

    return total + bestGain;
  }
}
```

## Golang

```go
package main

func maxValueAfterReverse(nums []int) int {
	n := len(nums)
	if n < 2 {
		return 0
	}
	var base int64
	for i := 1; i < n; i++ {
		diff := nums[i] - nums[i-1]
		if diff < 0 {
			diff = -diff
		}
		base += int64(diff)
	}

	best := int64(0)
	first, last := nums[0], nums[n-1]

	for i := 1; i < n; i++ {
		curDiff := nums[i] - nums[i-1]
		if curDiff < 0 {
			curDiff = -curDiff
		}
		cand := int64(abs(nums[i]-first) - curDiff)
		if cand > best {
			best = cand
		}
		cand2 := int64(abs(last-nums[i-1]) - curDiff)
		if cand2 > best {
			best = cand2
		}
	}

	mn := int(1 << 30) // sufficiently large
	mx := -mn

	for i := 1; i < n-1; i++ {
		if nums[i] < mn {
			mn = nums[i]
		}
		if nums[i] > mx {
			mx = nums[i]
		}
		curDiff := nums[i+1] - nums[i]
		if curDiff < 0 {
			curDiff = -curDiff
		}
		cand := int64(max(abs(nums[i+1]-mn), abs(mx-nums[i])) - curDiff)
		if cand > best {
			best = cand
		}
	}

	return int(base + best)
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def max_value_after_reverse(nums)
  n = nums.length
  total = 0
  (0...n - 1).each do |i|
    total += (nums[i] - nums[i + 1]).abs
  end

  best_gain = 0

  # Case A: bring an element to the front or back
  (0...n - 1).each do |i|
    cur = (nums[i] - nums[i + 1]).abs
    gain = (nums[i] - nums[0]).abs - cur
    best_gain = gain if gain > best_gain
    gain = (nums[i + 1] - nums[-1]).abs - cur
    best_gain = gain if gain > best_gain
  end

  # Case B: improve internal edges
  low_max = -10**18
  high_min = 10**18
  (0...n - 1).each do |i|
    a, b = nums[i], nums[i + 1]
    low = a < b ? a : b
    high = a > b ? a : b
    low_max = low if low > low_max
    high_min = high if high < high_min
  end
  gain2 = 2 * (low_max - high_min)
  best_gain = gain2 if gain2 > best_gain

  total + best_gain
end
```

## Scala

```scala
object Solution {
    def maxValueAfterReverse(nums: Array[Int]): Int = {
        val n = nums.length
        var base: Long = 0L
        for (i <- 0 until n - 1) {
            base += math.abs(nums(i) - nums(i + 1)).toLong
        }

        var best = 0

        // case 1: reverse a prefix or suffix
        for (i <- 0 until n - 1) {
            val curDiff = math.abs(nums(i) - nums(i + 1))
            best = math.max(best, math.abs(nums(0) - nums(i + 1)) - curDiff)
            best = math.max(best, math.abs(nums(n - 1) - nums(i)) - curDiff)
        }

        // case 2: internal subarray
        var minLow = Int.MaxValue
        var maxHigh = Int.MinValue
        for (i <- 0 until n - 1) {
            val low = math.min(nums(i), nums(i + 1))
            val high = math.max(nums(i), nums(i + 1))

            if (minLow != Int.MaxValue) best = math.max(best, high - minLow)
            if (maxHigh != Int.MinValue) best = math.max(best, maxHigh - low)

            minLow = math.min(minLow, low)
            maxHigh = math.max(maxHigh, high)
        }

        (base + 2L * best).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_value_after_reverse(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 2 {
            return 0;
        }
        // initial total value
        let mut base: i64 = 0;
        for i in 0..n - 1 {
            base += (nums[i] - nums[i + 1]).abs() as i64;
        }

        let mut best_gain: i64 = 0;

        // cases where one side of the changed subarray touches an endpoint
        for i in 0..n - 1 {
            let cur = (nums[i] - nums[i + 1]).abs() as i64;
            // reverse a prefix ending at i+1, new left edge uses nums[0]
            let gain1 = ((nums[0] - nums[i + 1]).abs() as i64) - cur;
            if gain1 > best_gain {
                best_gain = gain1;
            }
            // reverse a suffix starting at i, new right edge uses nums[n-1]
            let gain2 = ((nums[n - 1] - nums[i]).abs() as i64) - cur;
            if gain2 > best_gain {
                best_gain = gain2;
            }
        }

        // internal case: improve both sides simultaneously
        let mut mn = std::i32::MAX; // minimum of the larger elements in each adjacent pair
        let mut mx = std::i32::MIN; // maximum of the smaller elements in each adjacent pair
        for i in 0..n - 1 {
            let a = nums[i];
            let b = nums[i + 1];
            mn = mn.min(a.max(b));
            mx = mx.max(a.min(b));
        }
        let gain3 = (mx - mn) as i64;
        if gain3 > best_gain {
            best_gain = gain3;
        }

        (base + best_gain) as i32
    }
}
```

## Racket

```racket
(define/contract (max-value-after-reverse nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (if (< n 2)
        0
        (let ()
          ;; base value
          (define base
            (let loop ((i 0) (sum 0))
              (if (= i (- n 1))
                  sum
                  (loop (+ i 1)
                        (+ sum (abs (- (vector-ref v i) (vector-ref v (+ i 1)))))))))
          ;; global min and max
          (define global-min (apply min nums))
          (define global-max (apply max nums))
          ;; best gain from any reversal
          (define best-gain
            (let loop ((i 0) (best 0))
              (if (= i (- n 1))
                  best
                  (let* ((a-i   (vector-ref v i))
                         (a-ip1 (vector-ref v (+ i 1)))
                         (diff  (abs (- a-i a-ip1)))
                         ;; reverse prefix ending at i
                         (gain-prefix (- (abs (- (vector-ref v 0) a-ip1)) diff))
                         ;; reverse suffix starting at i+1
                         (gain-suffix (- (abs (- a-i (vector-ref v (- n 1)))) diff))
                         ;; internal reversal using extremes
                         (cand1 (- (max a-i a-ip1) global-min))
                         (cand2 (- global-max (min a-i a-ip1)))
                         (gain-internal (- (max cand1 cand2) diff))
                         (new-best (max best gain-prefix gain-suffix gain-internal)))
                    (loop (+ i 1) new-best)))))
          (+ base best-gain)))))
```

## Erlang

```erlang
-spec max_value_after_reverse(Nums :: [integer()]) -> integer().
max_value_after_reverse(Nums) ->
    case Nums of
        [] -> 0;
        [_] -> 0;
        [First|Rest] ->
            Last = lists:last(Nums),
            {BaseSum, MaxGainEnds, MaxMin, MinMax} =
                loop(Rest, First, Last, 1, First, 0, 0, undefined, undefined),
            GainMid = case (MaxMin - MinMax) > 0 of
                true -> 2 * (MaxMin - MinMax);
                false -> 0
            end,
            MaxGain = erlang:max(MaxGainEnds, GainMid),
            BaseSum + MaxGain
    end.

loop([], _First, _Last, _Idx, _Prev, BaseAcc, GainEndsAcc, MaxMinAcc, MinMaxAcc) ->
    {BaseAcc, GainEndsAcc, MaxMinAcc, MinMaxAcc};
loop([Curr|Rest], First, Last, Idx, Prev, BaseAcc, GainEndsAcc, MaxMinAcc, MinMaxAcc) ->
    Diff = erlang:abs(Curr - Prev),
    NewBase = BaseAcc + Diff,
    Gain1 = erlang:abs(Curr - First) - Diff,
    Gain2 = erlang:abs(Curr - Last) - Diff,
    NewGainEnds = erlang:max(GainEndsAcc, erlang:max(Gain1, Gain2)),
    PairMin = erlang:min(Prev, Curr),
    PairMax = erlang:max(Prev, Curr),
    NewMaxMin = case MaxMinAcc of
        undefined -> PairMin;
        _ -> erlang:max(MaxMinAcc, PairMin)
    end,
    NewMinMax = case MinMaxAcc of
        undefined -> PairMax;
        _ -> erlang:min(MinMaxAcc, PairMax)
    end,
    loop(Rest, First, Last, Idx+1, Curr, NewBase, NewGainEnds, NewMaxMin, NewMinMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_value_after_reverse(nums :: [integer]) :: integer
  def max_value_after_reverse(nums) do
    first = hd(nums)
    last = List.last(nums)

    pairs = Enum.zip(nums, tl(nums))

    base =
      Enum.reduce(pairs, 0, fn {a, b}, acc ->
        acc + abs(a - b)
      end)

    best_case1 =
      Enum.reduce(pairs, 0, fn {a, b}, best ->
        diff = abs(a - b)
        gain1 = abs(a - first) - diff
        gain2 = abs(b - last) - diff
        max(best, max(gain1, gain2))
      end)

    {mn, mx} =
      Enum.reduce(pairs, {1_000_000, -1}, fn {a, b}, {mn_acc, mx_acc} ->
        max_ab = if a > b, do: a, else: b
        min_ab = if a < b, do: a, else: b
        {min(mn_acc, max_ab), max(mx_acc, min_ab)}
      end)

    best_case2 = mx - mn
    best = Enum.max([best_case1, best_case2, 0])
    base + best
  end
end
```

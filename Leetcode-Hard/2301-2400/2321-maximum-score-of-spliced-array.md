# 2321. Maximum Score Of Spliced Array

## Cpp

```cpp
class Solution {
public:
    int maximumsSplicedArray(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        long long sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; ++i) {
            sum1 += nums1[i];
            sum2 += nums2[i];
        }
        long long maxPos = 0, cur = 0;
        for (int i = 0; i < n; ++i) {
            long long diff = (long long)nums2[i] - nums1[i];
            cur = max(0LL, cur + diff);
            maxPos = max(maxPos, cur);
        }
        long long maxNeg = 0;
        cur = 0;
        for (int i = 0; i < n; ++i) {
            long long diff = (long long)nums1[i] - nums2[i];
            cur = max(0LL, cur + diff);
            maxNeg = max(maxNeg, cur);
        }
        long long original = max(sum1, sum2);
        long long candidate1 = sum1 + maxPos;
        long long candidate2 = sum2 + maxNeg;
        long long ans = max({original, candidate1, candidate2});
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumsSplicedArray(int[] nums1, int[] nums2) {
        int n = nums1.length;
        long sum1 = 0, sum2 = 0;
        int[] diff = new int[n];
        for (int i = 0; i < n; i++) {
            sum1 += nums1[i];
            sum2 += nums2[i];
            diff[i] = nums2[i] - nums1[i];
        }
        long maxDelta = kadaneMax(diff);
        long minDelta = kadaneMin(diff);
        long ans = Math.max(Math.max(sum1, sum2), Math.max(sum1 + maxDelta, sum2 - minDelta));
        return (int) ans;
    }

    private long kadaneMax(int[] arr) {
        long best = arr[0];
        long cur = arr[0];
        for (int i = 1; i < arr.length; i++) {
            cur = Math.max(arr[i], cur + arr[i]);
            best = Math.max(best, cur);
        }
        return best;
    }

    private long kadaneMin(int[] arr) {
        long best = arr[0];
        long cur = arr[0];
        for (int i = 1; i < arr.length; i++) {
            cur = Math.min(arr[i], cur + arr[i]);
            best = Math.min(best, cur);
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        # Max increase for sum1 by swapping a subarray from nums2 into nums1
        best_inc_sum1 = 0
        cur = 0
        for a, b in zip(nums1, nums2):
            diff = b - a
            cur = max(diff, cur + diff)
            if cur > best_inc_sum1:
                best_inc_sum1 = cur

        # Max increase for sum2 by swapping a subarray from nums1 into nums2
        best_inc_sum2 = 0
        cur = 0
        for a, b in zip(nums1, nums2):
            diff = a - b
            cur = max(diff, cur + diff)
            if cur > best_inc_sum2:
                best_inc_sum2 = cur

        return max(sum1,
                   sum2,
                   sum1 + best_inc_sum1,
                   sum2 + best_inc_sum2)
```

## Python3

```python
from typing import List

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        total1 = sum(nums1)
        total2 = sum(nums2)

        # Gain for improving nums1
        cur = 0
        best_gain1 = 0
        for a, b in zip(nums1, nums2):
            diff = b - a
            cur = max(diff, cur + diff)
            best_gain1 = max(best_gain1, cur)
        candidate1 = total1 + max(0, best_gain1)

        # Gain for improving nums2 (equivalently loss for nums1)
        cur = 0
        best_gain2 = 0
        for a, b in zip(nums1, nums2):
            diff = a - b
            cur = max(diff, cur + diff)
            best_gain2 = max(best_gain2, cur)
        candidate2 = total2 + max(0, best_gain2)

        return max(total1, total2, candidate1, candidate2)
```

## C

```c
int maximumsSplicedArray(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    long long sum1 = 0, sum2 = 0;
    for (int i = 0; i < nums1Size; ++i) {
        sum1 += nums1[i];
        sum2 += nums2[i];
    }
    
    long long maxGain1 = 0, cur1 = 0; // gain for increasing sum1: nums2 - nums1
    long long maxGain2 = 0, cur2 = 0; // gain for increasing sum2: nums1 - nums2
    
    for (int i = 0; i < nums1Size; ++i) {
        long long diff1 = (long long)nums2[i] - nums1[i];
        cur1 = cur1 > 0 ? cur1 + diff1 : diff1;
        if (cur1 > maxGain1) maxGain1 = cur1;
        
        long long diff2 = (long long)nums1[i] - nums2[i];
        cur2 = cur2 > 0 ? cur2 + diff2 : diff2;
        if (cur2 > maxGain2) maxGain2 = cur2;
    }
    
    long long ans = sum1;
    if (sum2 > ans) ans = sum2;
    if (sum1 + maxGain1 > ans) ans = sum1 + maxGain1;
    if (sum2 + maxGain2 > ans) ans = sum2 + maxGain2;
    
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumsSplicedArray(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        long sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            sum1 += nums1[i];
            sum2 += nums2[i];
        }

        long maxInc1 = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            long diff = (long)nums2[i] - nums1[i];
            cur += diff;
            if (cur < 0) cur = 0;
            if (cur > maxInc1) maxInc1 = cur;
        }

        long maxInc2 = 0;
        cur = 0;
        for (int i = 0; i < n; i++) {
            long diff = (long)nums1[i] - nums2[i];
            cur += diff;
            if (cur < 0) cur = 0;
            if (cur > maxInc2) maxInc2 = cur;
        }

        long ans = Math.Max(Math.Max(sum1, sum2), Math.Max(sum1 + maxInc1, sum2 + maxInc2));
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maximumsSplicedArray = function(nums1, nums2) {
    const n = nums1.length;
    let sum1 = 0, sum2 = 0;
    for (let i = 0; i < n; ++i) {
        sum1 += nums1[i];
        sum2 += nums2[i];
    }
    let maxPos = 0, curPos = 0; // best increase for sum1
    let maxNeg = 0, curNeg = 0; // best increase for sum2
    for (let i = 0; i < n; ++i) {
        const diff = nums2[i] - nums1[i];      // contribution to sum1 if swapped
        curPos = Math.max(0, curPos + diff);
        maxPos = Math.max(maxPos, curPos);
        const ndiff = -diff;                   // contribution to sum2 if swapped
        curNeg = Math.max(0, curNeg + ndiff);
        maxNeg = Math.max(maxNeg, curNeg);
    }
    return Math.max(
        sum1,
        sum2,
        sum1 + maxPos,
        sum2 + maxNeg
    );
};
```

## Typescript

```typescript
function maximumsSplicedArray(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    let sum1 = 0, sum2 = 0;
    for (let i = 0; i < n; ++i) {
        sum1 += nums1[i];
        sum2 += nums2[i];
    }

    // max subarray sum of diff = nums2 - nums1
    let bestDiff = -Infinity;
    let cur = 0;
    for (let i = 0; i < n; ++i) {
        const d = nums2[i] - nums1[i];
        cur = Math.max(d, cur + d);
        if (cur > bestDiff) bestDiff = cur;
    }
    const gain1 = Math.max(0, bestDiff);

    // max subarray sum of diff = nums1 - nums2
    let bestDiff2 = -Infinity;
    cur = 0;
    for (let i = 0; i < n; ++i) {
        const d = nums1[i] - nums2[i];
        cur = Math.max(d, cur + d);
        if (cur > bestDiff2) bestDiff2 = cur;
    }
    const gain2 = Math.max(0, bestDiff2);

    const candidate1 = sum1 + gain1;
    const candidate2 = sum2 + gain2;

    return Math.max(sum1, sum2, candidate1, candidate2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maximumsSplicedArray($nums1, $nums2) {
        $n = count($nums1);
        $sum1 = 0;
        $sum2 = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum1 += $nums1[$i];
            $sum2 += $nums2[$i];
        }

        if ($sum1 < $sum2) {
            $maxDelta = 0;
            $cur = 0;
            for ($i = 0; $i < $n; $i++) {
                $diff = $nums2[$i] - $nums1[$i];
                $cur = max(0, $cur + $diff);
                if ($cur > $maxDelta) {
                    $maxDelta = $cur;
                }
            }
            return max($sum2, $sum1 + $maxDelta);
        } else {
            $maxDelta = 0;
            $cur = 0;
            for ($i = 0; $i < $n; $i++) {
                $diff = $nums1[$i] - $nums2[$i];
                $cur = max(0, $cur + $diff);
                if ($cur > $maxDelta) {
                    $maxDelta = $cur;
                }
            }
            return max($sum1, $sum2 + $maxDelta);
        }
    }
}
```

## Swift

```swift
class Solution {
    func maximumsSplicedArray(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var total1 = 0
        var total2 = 0
        for i in 0..<n {
            total1 += nums1[i]
            total2 += nums2[i]
        }
        
        // Max increase for nums1 by swapping a subarray (diff = nums2 - nums1)
        var maxInc1 = 0
        var cur = 0
        for i in 0..<n {
            let diff = nums2[i] - nums1[i]
            cur = max(diff, cur + diff)
            maxInc1 = max(maxInc1, cur)
        }
        
        // Max increase for nums2 by swapping a subarray (diff = nums1 - nums2)
        var maxInc2 = 0
        cur = 0
        for i in 0..<n {
            let diff = nums1[i] - nums2[i]
            cur = max(diff, cur + diff)
            maxInc2 = max(maxInc2, cur)
        }
        
        return max(total1 + maxInc1, total2 + maxInc2)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumsSplicedArray(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        var sum1 = 0L
        var sum2 = 0L
        for (i in 0 until n) {
            sum1 += nums1[i].toLong()
            sum2 += nums2[i].toLong()
        }
        var maxEnding = 0L
        var maxDiff = Long.MIN_VALUE
        var minEnding = 0L
        var minDiff = Long.MAX_VALUE
        for (i in 0 until n) {
            val d = nums2[i].toLong() - nums1[i].toLong()
            maxEnding = kotlin.math.max(d, maxEnding + d)
            maxDiff = kotlin.math.max(maxDiff, maxEnding)
            minEnding = kotlin.math.min(d, minEnding + d)
            minDiff = kotlin.math.min(minDiff, minEnding)
        }
        var ans = kotlin.math.max(sum1, sum2)
        ans = kotlin.math.max(ans, sum1 + maxDiff)
        ans = kotlin.math.max(ans, sum2 - minDiff)
        return ans.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maximumsSplicedArray(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    int sum1 = 0;
    int sum2 = 0;
    for (int i = 0; i < n; i++) {
      sum1 += nums1[i];
      sum2 += nums2[i];
    }

    const int INF = 1 << 60;

    int curMax = 0;
    int bestDelta = -INF;
    int curMin = 0;
    int worstDelta = INF;

    for (int i = 0; i < n; i++) {
      int diff = nums2[i] - nums1[i];

      // Max subarray sum (Kadane)
      if (curMax > 0) {
        curMax += diff;
      } else {
        curMax = diff;
      }
      if (curMax > bestDelta) bestDelta = curMax;

      // Min subarray sum (Kadane for minimum)
      if (curMin < 0) {
        curMin += diff;
      } else {
        curMin = diff;
      }
      if (curMin < worstDelta) worstDelta = curMin;
    }

    if (bestDelta < 0) bestDelta = 0;
    if (worstDelta > 0) worstDelta = 0;

    int ans = max(sum1, sum2);
    ans = max(ans, sum1 + bestDelta);
    ans = max(ans, sum2 - worstDelta); // worstDelta <= 0

    return ans;
  }
}
```

## Golang

```go
func maximumsSplicedArray(nums1 []int, nums2 []int) int {
    n := len(nums1)
    var sum1, sum2 int64
    diff := make([]int64, n)

    for i := 0; i < n; i++ {
        a := int64(nums1[i])
        b := int64(nums2[i])
        sum1 += a
        sum2 += b
        diff[i] = b - a
    }

    const infNeg int64 = -1 << 60
    const infPos int64 = 1 << 60

    // maximum subarray sum of diff
    var curMax, bestMax int64 = 0, infNeg
    for _, v := range diff {
        if curMax+v < v {
            curMax = v
        } else {
            curMax += v
        }
        if curMax > bestMax {
            bestMax = curMax
        }
    }

    // minimum subarray sum of diff
    var curMin, bestMin int64 = 0, infPos
    for _, v := range diff {
        if curMin+v > v {
            curMin = v
        } else {
            curMin += v
        }
        if curMin < bestMin {
            bestMin = curMin
        }
    }

    maxDelta := bestMax
    if maxDelta < 0 {
        maxDelta = 0
    }
    minDelta := bestMin
    if minDelta > 0 {
        minDelta = 0
    }

    ans1 := sum1 + maxDelta          // maximize sum of nums1
    ans2 := sum2 - minDelta          // maximize sum of nums2 (minDelta <= 0)
    if ans1 > ans2 {
        return int(ans1)
    }
    return int(ans2)
}
```

## Ruby

```ruby
def maximums_spliced_array(nums1, nums2)
  n = nums1.length
  sum1 = 0
  sum2 = 0
  diff = Array.new(n)

  n.times do |i|
    a = nums1[i]
    b = nums2[i]
    sum1 += a
    sum2 += b
    diff[i] = b - a
  end

  max_ending = diff[0]
  max_sum = diff[0]
  min_ending = diff[0]
  min_sum = diff[0]

  (1...n).each do |i|
    x = diff[i]

    max_ending = [x, max_ending + x].max
    max_sum = [max_sum, max_ending].max

    min_ending = [x, min_ending + x].min
    min_sum = [min_sum, min_ending].min
  end

  candidate1 = sum1 + [0, max_sum].max
  candidate2 = sum2 + [0, -min_sum].max

  [candidate1, candidate2, sum1, sum2].max
end
```

## Scala

```scala
object Solution {
    def maximumsSplicedArray(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length
        var sum1: Long = 0L
        var sum2: Long = 0L
        val diff = new Array[Long](n)
        var i = 0
        while (i < n) {
            sum1 += nums1(i).toLong
            sum2 += nums2(i).toLong
            diff(i) = nums2(i).toLong - nums1(i).toLong
            i += 1
        }

        // Max subarray sum for diff (increase sum1)
        var bestInc1: Long = 0L
        var cur: Long = 0L
        i = 0
        while (i < n) {
            cur = math.max(0L, cur + diff(i))
            if (cur > bestInc1) bestInc1 = cur
            i += 1
        }

        // Max subarray sum for -diff (increase sum2)
        var bestInc2: Long = 0L
        cur = 0L
        i = 0
        while (i < n) {
            cur = math.max(0L, cur - diff(i))
            if (cur > bestInc2) bestInc2 = cur
            i += 1
        }

        val result = math.max(sum1 + bestInc1, sum2 + bestInc2)
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximums_spliced_array(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let mut sum1: i64 = 0;
        let mut sum2: i64 = 0;
        let mut diffs: Vec<i64> = Vec::with_capacity(n);
        for i in 0..n {
            sum1 += nums1[i] as i64;
            sum2 += nums2[i] as i64;
            diffs.push(nums2[i] as i64 - nums1[i] as i64);
        }

        // Maximum subarray sum of diffs
        let mut cur_max: i64 = 0;
        let mut best_max: i64 = std::i64::MIN;
        for &d in &diffs {
            cur_max = (cur_max + d).max(d);
            best_max = best_max.max(cur_max);
        }

        // Minimum subarray sum of diffs
        let mut cur_min: i64 = 0;
        let mut best_min: i64 = std::i64::MAX;
        for &d in &diffs {
            cur_min = (cur_min + d).min(d);
            best_min = best_min.min(cur_min);
        }

        let mut ans = sum1.max(sum2);
        ans = ans.max(sum1 + best_max);
        ans = ans.max(sum2 - best_min);
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (maximums-spliced-array nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((sum1 (apply + nums1))
         (sum2 (apply + nums2))
         (diffs (map - nums2 nums1)))
    (letrec ((max-subarray
              (lambda (lst)
                (let ((first (car lst))
                      (rest (cdr lst)))
                  (let loop ((xs rest) (cur first) (best first))
                    (if (null? xs)
                        best
                        (let* ((x (car xs))
                               (new-cur (max x (+ cur x)))
                               (new-best (max best new-cur)))
                          (loop (cdr xs) new-cur new-best)))))))
             (min-subarray
              (lambda (lst)
                (let ((first (car lst))
                      (rest (cdr lst)))
                  (let loop ((xs rest) (cur first) (best first))
                    (if (null? xs)
                        best
                        (let* ((x (car xs))
                               (new-cur (min x (+ cur x)))
                               (new-best (min best new-cur)))
                          (loop (cdr xs) new-cur new-best))))))))
      (let* ((maxDelta (max-subarray diffs))
             (minDelta (min-subarray diffs))
             (score0 (max sum1 sum2))
             (score1 (max (+ sum1 maxDelta) (- sum2 maxDelta)))
             (score2 (max (+ sum1 minDelta) (- sum2 minDelta))))
        (max score0 score1 score2)))))
```

## Erlang

```erlang
-module(solution).
-export([maximums_spliced_array/2]).

-spec maximums_spliced_array(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
maximums_spliced_array(Nums1, Nums2) ->
    {Sum1, Sum2, BestGain1, BestGain2} = process(Nums1, Nums2, 0, 0, 0, 0, 0, 0),
    max(Sum1 + BestGain1, Sum2 + BestGain2).

process([], [], Sum1, Sum2, _Cur1, Best1, _Cur2, Best2) ->
    {Sum1, Sum2, Best1, Best2};
process([A|As], [B|Bs], Sum1, Sum2, Cur1, Best1, Cur2, Best2) ->
    NewSum1 = Sum1 + A,
    NewSum2 = Sum2 + B,
    Diff1 = B - A,
    NewCur1 = max(0, Cur1 + Diff1),
    NewBest1 = max(Best1, NewCur1),
    Diff2 = A - B,
    NewCur2 = max(0, Cur2 + Diff2),
    NewBest2 = max(Best2, NewCur2),
    process(As, Bs, NewSum1, NewSum2, NewCur1, NewBest1, NewCur2, NewBest2).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximums_spliced_array(nums1 :: [integer], nums2 :: [integer]) :: integer
  def maximums_spliced_array(nums1, nums2) do
    {sum1, sum2} =
      Enum.zip(nums1, nums2)
      |> Enum.reduce({0, 0}, fn {a, b}, {s1, s2} -> {s1 + a, s2 + b} end)

    diff = Enum.map(Enum.zip(nums1, nums2), fn {a, b} -> b - a end)

    gain1 = max_subarray_sum(diff)
    gain2 = max_subarray_sum(Enum.map(diff, &(&1 * -1)))

    Enum.max([sum1, sum2, sum1 + gain1, sum2 + gain2])
  end

  defp max_subarray_sum(list) do
    {best, cur} =
      Enum.reduce(list, {0, 0}, fn x, {best, cur} ->
        cur = max(0, cur + x)
        best = max(best, cur)
        {best, cur}
      end)

    best
  end
end
```

# 0918. Maximum Sum Circular Subarray

## Cpp

```cpp
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int total = 0;
        int maxEnding = 0, maxSum = INT_MIN;
        int minEnding = 0, minSum = INT_MAX;
        for (int x : nums) {
            total += x;
            maxEnding = std::max(maxEnding + x, x);
            maxSum = std::max(maxSum, maxEnding);
            minEnding = std::min(minEnding + x, x);
            minSum = std::min(minSum, minEnding);
        }
        if (maxSum < 0) return maxSum; // all numbers are negative
        return std::max(maxSum, total - minSum);
    }
};
```

## Java

```java
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int total = 0;
        int maxEnding = 0, maxSoFar = Integer.MIN_VALUE;
        int minEnding = 0, minSoFar = Integer.MAX_VALUE;
        for (int num : nums) {
            total += num;
            // Kadane for maximum subarray
            maxEnding = Math.max(num, maxEnding + num);
            maxSoFar = Math.max(maxSoFar, maxEnding);
            // Kadane for minimum subarray
            minEnding = Math.min(num, minEnding + num);
            minSoFar = Math.min(minSoFar, minEnding);
        }
        // If all numbers are negative, maxSoFar == total (min subarray is whole array)
        if (minSoFar == total) {
            return maxSoFar;
        }
        return Math.max(maxSoFar, total - minSoFar);
    }
}
```

## Python

```python
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]
        cur_max = max_sum = nums[0]
        cur_min = min_sum = nums[0]
        for x in nums[1:]:
            total += x
            cur_max = x if cur_max + x < x else cur_max + x
            max_sum = max(max_sum, cur_max)
            cur_min = x if cur_min + x > x else cur_min + x
            min_sum = min(min_sum, cur_min)
        if min_sum == total:
            return max_sum
        return max(max_sum, total - min_sum)
```

## Python3

```python
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        max_ending = min_ending = max_sum = min_sum = nums[0]

        for x in nums[1:]:
            total += x
            max_ending = max(x, max_ending + x)
            max_sum = max(max_sum, max_ending)

            min_ending = min(x, min_ending + x)
            min_sum = min(min_sum, min_ending)

        if min_sum == total:
            return max_sum
        return max(max_sum, total - min_sum)
```

## C

```c
int maxSubarraySumCircular(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int total = nums[0];
    int maxEnding = nums[0], maxSoFar = nums[0];
    int minEnding = nums[0], minSoFar = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        int x = nums[i];
        total += x;
        maxEnding = (maxEnding > 0) ? maxEnding + x : x;
        if (maxEnding > maxSoFar) maxSoFar = maxEnding;
        minEnding = (minEnding < 0) ? minEnding + x : x;
        if (minEnding < minSoFar) minSoFar = minEnding;
    }
    if (total == minSoFar) return maxSoFar; // all numbers are negative
    int circularMax = total - minSoFar;
    return (maxSoFar > circularMax) ? maxSoFar : circularMax;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxSubarraySumCircular(int[] nums)
    {
        int n = nums.Length;
        int total = nums[0];
        int maxEnding = nums[0], maxSoFar = nums[0];
        int minEnding = nums[0], minSoFar = nums[0];

        for (int i = 1; i < n; i++)
        {
            int x = nums[i];
            total += x;

            maxEnding = System.Math.Max(x, maxEnding + x);
            maxSoFar = System.Math.Max(maxSoFar, maxEnding);

            minEnding = System.Math.Min(x, minEnding + x);
            minSoFar = System.Math.Min(minSoFar, minEnding);
        }

        // If all numbers are negative, maxSoFar is the answer.
        if (maxSoFar < 0)
            return maxSoFar;

        // Otherwise, consider wrapping subarray.
        return System.Math.Max(maxSoFar, total - minSoFar);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubarraySumCircular = function(nums) {
    let total = 0;
    let maxCurr = 0, maxAns = -Infinity;
    let minCurr = 0, minAns = Infinity;
    
    for (let x of nums) {
        total += x;
        maxCurr = Math.max(x, maxCurr + x);
        maxAns = Math.max(maxAns, maxCurr);
        minCurr = Math.min(x, minCurr + x);
        minAns = Math.min(minAns, minCurr);
    }
    
    if (minAns === total) {
        return maxAns;
    }
    return Math.max(maxAns, total - minAns);
};
```

## Typescript

```typescript
function maxSubarraySumCircular(nums: number[]): number {
    let total = 0;
    let maxEnding = nums[0];
    let maxSoFar = nums[0];
    let minEnding = nums[0];
    let minSoFar = nums[0];

    for (const num of nums) {
        total += num;

        maxEnding = Math.max(num, maxEnding + num);
        maxSoFar = Math.max(maxSoFar, maxEnding);

        minEnding = Math.min(num, minEnding + num);
        minSoFar = Math.min(minSoFar, minEnding);
    }

    // If all numbers are negative, minSoFar == total, so we should return maxSoFar
    if (minSoFar === total) {
        return maxSoFar;
    }
    return Math.max(maxSoFar, total - minSoFar);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSubarraySumCircular($nums) {
        $n = count($nums);
        $total = $nums[0];
        $maxEnding = $nums[0];
        $maxSoFar = $nums[0];
        $minEnding = $nums[0];
        $minSoFar = $nums[0];

        for ($i = 1; $i < $n; $i++) {
            $x = $nums[$i];
            $total += $x;

            // Kadane for max subarray
            $maxEnding = max($x, $maxEnding + $x);
            $maxSoFar = max($maxSoFar, $maxEnding);

            // Kadane for min subarray
            $minEnding = min($x, $minEnding + $x);
            $minSoFar = min($minSoFar, $minEnding);
        }

        if ($minSoFar == $total) {
            return $maxSoFar;
        }

        $circularMax = $total - $minSoFar;
        return max($maxSoFar, $circularMax);
    }
}
```

## Swift

```swift
class Solution {
    func maxSubarraySumCircular(_ nums: [Int]) -> Int {
        var total = 0
        var maxEnding = nums[0]
        var maxSoFar = nums[0]
        var minEnding = nums[0]
        var minSoFar = nums[0]

        for i in 0..<nums.count {
            let x = nums[i]
            total += x
            if i > 0 {
                maxEnding = max(x, maxEnding + x)
                maxSoFar = max(maxSoFar, maxEnding)

                minEnding = min(x, minEnding + x)
                minSoFar = min(minSoFar, minEnding)
            }
        }

        if minSoFar == total {
            return maxSoFar
        } else {
            return max(maxSoFar, total - minSoFar)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSubarraySumCircular(nums: IntArray): Int {
        var total = nums[0].toLong()
        var maxEnding = nums[0]
        var maxSoFar = nums[0]
        var minEnding = nums[0]
        var minSoFar = nums[0]

        for (i in 1 until nums.size) {
            val v = nums[i]
            total += v

            maxEnding = if (maxEnding + v > v) maxEnding + v else v
            maxSoFar = kotlin.math.max(maxSoFar, maxEnding)

            minEnding = if (minEnding + v < v) minEnding + v else v
            minSoFar = kotlin.math.min(minSoFar, minEnding)
        }

        // If all numbers are negative, the minimum subarray is the whole array.
        if (minSoFar.toLong() == total) {
            return maxSoFar
        }
        val circularMax = (total - minSoFar).toInt()
        return kotlin.math.max(maxSoFar, circularMax)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxSubarraySumCircular(List<int> nums) {
    int total = 0;
    int maxEnding = nums[0];
    int maxSoFar = nums[0];
    int minEnding = nums[0];
    int minSoFar = nums[0];

    for (int i = 0; i < nums.length; i++) {
      int x = nums[i];
      total += x;

      if (i > 0) {
        maxEnding = max(maxEnding + x, x);
        maxSoFar = max(maxSoFar, maxEnding);

        minEnding = min(minEnding + x, x);
        minSoFar = min(minSoFar, minEnding);
      }
    }

    // If all numbers are negative, the maximum subarray is the largest (least negative) element.
    if (maxSoFar < 0) {
      return maxSoFar;
    }

    int circularMax = total - minSoFar;
    return max(maxSoFar, circularMax);
  }
}
```

## Golang

```go
func maxSubarraySumCircular(nums []int) int {
    total := 0
    maxEnding, maxSoFar := 0, nums[0]
    minEnding, minSoFar := 0, nums[0]

    for _, v := range nums {
        total += v

        // Kadane for maximum subarray sum
        if maxEnding > 0 {
            maxEnding += v
        } else {
            maxEnding = v
        }
        if maxEnding > maxSoFar {
            maxSoFar = maxEnding
        }

        // Kadane for minimum subarray sum
        if minEnding < 0 {
            minEnding += v
        } else {
            minEnding = v
        }
        if minEnding < minSoFar {
            minSoFar = minEnding
        }
    }

    if maxSoFar < 0 { // all numbers are negative
        return maxSoFar
    }
    circularMax := total - minSoFar
    if circularMax > maxSoFar {
        return circularMax
    }
    return maxSoFar
}
```

## Ruby

```ruby
def max_subarray_sum_circular(nums)
  n = nums.length
  return nums[0] if n == 1

  total = nums[0]
  max_ending = nums[0]
  max_sum = nums[0]
  min_ending = nums[0]
  min_sum = nums[0]

  (1...n).each do |i|
    x = nums[i]
    total += x

    max_ending = [x, max_ending + x].max
    max_sum = [max_sum, max_ending].max

    min_ending = [x, min_ending + x].min
    min_sum = [min_sum, min_ending].min
  end

  return max_sum if min_sum == total
  [max_sum, total - min_sum].max
end
```

## Scala

```scala
object Solution {
  def maxSubarraySumCircular(nums: Array[Int]): Int = {
    val n = nums.length
    var total = nums(0).toLong

    var maxEnding = nums(0).toLong
    var maxSoFar = nums(0).toLong

    var minEnding = nums(0).toLong
    var minSoFar = nums(0).toLong

    var i = 1
    while (i < n) {
      val v = nums(i).toLong
      total += v

      maxEnding = math.max(v, maxEnding + v)
      maxSoFar = math.max(maxSoFar, maxEnding)

      minEnding = math.min(v, minEnding + v)
      minSoFar = math.min(minSoFar, minEnding)

      i += 1
    }

    if (maxSoFar < 0) return maxSoFar.toInt

    val circularMax = total - minSoFar
    math.max(maxSoFar, circularMax).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_subarray_sum_circular(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        // At least one element guaranteed
        let mut total = 0i32;
        let mut cur_max = nums[0];
        let mut max_sum = nums[0];
        let mut cur_min = nums[0];
        let mut min_sum = nums[0];

        for &x in &nums {
            total += x;
        }

        // Kadane for max and min (skip first element already used)
        for i in 1..n {
            let x = nums[i];
            cur_max = (cur_max + x).max(x);
            max_sum = max_sum.max(cur_max);

            cur_min = (cur_min + x).min(x);
            min_sum = min_sum.min(cur_min);
        }

        // If all numbers are negative, min_sum == total
        if min_sum == total {
            max_sum
        } else {
            std::cmp::max(max_sum, total - min_sum)
        }
    }
}
```

## Racket

```racket
(define/contract (max-subarray-sum-circular nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? nums)
      0
      (let* ((first (car nums))
             (total first)
             (max-ending first)
             (max-sofar first)
             (min-ending first)
             (min-sofar first))
        (for ([x (cdr nums)])
          (set! total (+ total x))
          (set! max-ending (max x (+ max-ending x)))
          (set! max-sofar (max max-sofar max-ending))
          (set! min-ending (min x (+ min-ending x)))
          (set! min-sofar (min min-sofar min-ending)))
        (if (= min-sofar total)
            max-sofar
            (max max-sofar (- total min-sofar))))))
```

## Erlang

```erlang
-spec max_subarray_sum_circular(Nums :: [integer()]) -> integer().
max_subarray_sum_circular(Nums) ->
    {MaxSum, _} = lists:foldl(
        fun(X, {Cur, Global}) ->
            NewCur = erlang:max(X, Cur + X),
            {NewCur, erlang:max(Global, NewCur)}
        end,
        {hd(Nums), hd(Nums)},
        tl(Nums)
    ),
    {MinSum, _} = lists:foldl(
        fun(X, {Cur, Global}) ->
            NewCur = erlang:min(X, Cur + X),
            {NewCur, erlang:min(Global, NewCur)}
        end,
        {hd(Nums), hd(Nums)},
        tl(Nums)
    ),
    Total = lists:sum(Nums),
    if
        MinSum == Total -> MaxSum;
        true -> erlang:max(MaxSum, Total - MinSum)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_subarray_sum_circular(nums :: [integer]) :: integer
  def max_subarray_sum_circular([first | rest]) do
    init = %{
      cur_max: first,
      max_sum: first,
      cur_min: first,
      min_sum: first,
      total: first
    }

    final =
      Enum.reduce(rest, init, fn x, acc ->
        cur_max = max(x, acc.cur_max + x)
        max_sum = max(acc.max_sum, cur_max)

        cur_min = min(x, acc.cur_min + x)
        min_sum = min(acc.min_sum, cur_min)

        total = acc.total + x

        %{
          cur_max: cur_max,
          max_sum: max_sum,
          cur_min: cur_min,
          min_sum: min_sum,
          total: total
        }
      end)

    if final.min_sum == final.total do
      final.max_sum
    else
      max(final.max_sum, final.total - final.min_sum)
    end
  end
end
```

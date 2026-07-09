# 1749. Maximum Absolute Sum of Any Subarray

## Cpp

```cpp
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        long long maxEnding = 0, minEnding = 0;
        long long maxSoFar = LLONG_MIN, minSoFar = LLONG_MAX;
        for (int x : nums) {
            maxEnding = std::max<long long>(maxEnding + x, x);
            maxSoFar = std::max(maxSoFar, maxEnding);
            minEnding = std::min<long long>(minEnding + x, x);
            minSoFar = std::min(minSoFar, minEnding);
        }
        long long ans = std::max(std::llabs(maxSoFar), std::llabs(minSoFar));
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int maxAbsoluteSum(int[] nums) {
        int maxEnding = 0;
        int maxSoFar = Integer.MIN_VALUE;
        int minEnding = 0;
        int minSoFar = Integer.MAX_VALUE;
        
        for (int num : nums) {
            maxEnding = Math.max(num, maxEnding + num);
            maxSoFar = Math.max(maxSoFar, maxEnding);
            
            minEnding = Math.min(num, minEnding + num);
            minSoFar = Math.min(minSoFar, minEnding);
        }
        
        return Math.max(maxSoFar, -minSoFar);
    }
}
```

## Python

```python
class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending = max_sum = 0
        min_ending = min_sum = 0
        for x in nums:
            max_ending = max(0, max_ending + x)
            max_sum = max(max_sum, max_ending)
            min_ending = min(0, min_ending + x)
            min_sum = min(min_sum, min_ending)
        return max(abs(max_sum), abs(min_sum))
```

## Python3

```python
from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ending = max_sum = 0
        min_ending = min_sum = 0
        for x in nums:
            max_ending = max(x, max_ending + x)
            max_sum = max(max_sum, max_ending)
            min_ending = min(x, min_ending + x)
            min_sum = min(min_sum, min_ending)
        return max(abs(max_sum), abs(min_sum))
```

## C

```c
int maxAbsoluteSum(int* nums, int numsSize) {
    long curMax = 0, maxSum = 0;
    long curMin = 0, minSum = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        curMax = (curMax + x > x) ? curMax + x : x;
        if (curMax > maxSum) maxSum = curMax;
        curMin = (curMin + x < x) ? curMin + x : x;
        if (curMin < minSum) minSum = curMin;
    }
    long ans = maxSum;
    if (-minSum > ans) ans = -minSum;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxAbsoluteSum(int[] nums) {
        int maxEnding = 0, maxSoFar = int.MinValue;
        int minEnding = 0, minSoFar = int.MaxValue;

        foreach (int num in nums) {
            maxEnding = System.Math.Max(num, maxEnding + num);
            maxSoFar = System.Math.Max(maxSoFar, maxEnding);

            minEnding = System.Math.Min(num, minEnding + num);
            minSoFar = System.Math.Min(minSoFar, minEnding);
        }

        return System.Math.Max(maxSoFar, -minSoFar);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAbsoluteSum = function(nums) {
    let maxEnding = 0, maxOverall = Number.NEGATIVE_INFINITY;
    let minEnding = 0, minOverall = Number.POSITIVE_INFINITY;
    
    for (const num of nums) {
        // Kadane for maximum subarray sum
        maxEnding = Math.max(num, maxEnding + num);
        maxOverall = Math.max(maxOverall, maxEnding);
        
        // Kadane for minimum subarray sum
        minEnding = Math.min(num, minEnding + num);
        minOverall = Math.min(minOverall, minEnding);
    }
    
    return Math.max(maxOverall, -minOverall);
};
```

## Typescript

```typescript
function maxAbsoluteSum(nums: number[]): number {
    let maxEnding = 0;
    let maxSoFar = Number.NEGATIVE_INFINITY;
    let minEnding = 0;
    let minSoFar = Number.POSITIVE_INFINITY;

    for (const num of nums) {
        maxEnding = Math.max(num, maxEnding + num);
        maxSoFar = Math.max(maxSoFar, maxEnding);

        minEnding = Math.min(num, minEnding + num);
        minSoFar = Math.min(minSoFar, minEnding);
    }

    return Math.max(Math.abs(maxSoFar), Math.abs(minSoFar));
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAbsoluteSum($nums) {
        $maxEnding = 0;
        $maxSoFar = PHP_INT_MIN;
        $minEnding = 0;
        $minSoFar = PHP_INT_MAX;

        foreach ($nums as $num) {
            $maxEnding = max($num, $maxEnding + $num);
            $maxSoFar = max($maxSoFar, $maxEnding);

            $minEnding = min($num, $minEnding + $num);
            $minSoFar = min($minSoFar, $minEnding);
        }

        return max(abs($maxSoFar), abs($minSoFar));
    }
}
```

## Swift

```swift
class Solution {
    func maxAbsoluteSum(_ nums: [Int]) -> Int {
        var maxEnding = 0
        var maxSoFar = Int.min
        var minEnding = 0
        var minSoFar = Int.max
        
        for num in nums {
            maxEnding = max(num, maxEnding + num)
            maxSoFar = max(maxSoFar, maxEnding)
            
            minEnding = min(num, minEnding + num)
            minSoFar = min(minSoFar, minEnding)
        }
        
        return max(abs(maxSoFar), abs(minSoFar))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxAbsoluteSum(nums: IntArray): Int {
        var maxEnding = 0
        var maxSoFar = Int.MIN_VALUE
        var minEnding = 0
        var minSoFar = Int.MAX_VALUE

        for (num in nums) {
            maxEnding = kotlin.math.max(maxEnding + num, num)
            maxSoFar = kotlin.math.max(maxSoFar, maxEnding)

            minEnding = kotlin.math.min(minEnding + num, num)
            minSoFar = kotlin.math.min(minSoFar, minEnding)
        }

        return kotlin.math.max(kotlin.math.abs(maxSoFar), kotlin.math.abs(minSoFar))
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxAbsoluteSum(List<int> nums) {
    int curMax = nums[0];
    int bestMax = nums[0];
    int curMin = nums[0];
    int bestMin = nums[0];

    for (int i = 1; i < nums.length; ++i) {
      int x = nums[i];
      curMax = max(x, curMax + x);
      bestMax = max(bestMax, curMax);

      curMin = min(x, curMin + x);
      bestMin = min(bestMin, curMin);
    }

    return max(bestMax, -bestMin);
  }
}
```

## Golang

```go
func maxAbsoluteSum(nums []int) int {
	maxEnding, maxSoFar := 0, 0
	minEnding, minSoFar := 0, 0

	for _, v := range nums {
		if maxEnding+v > v {
			maxEnding = maxEnding + v
		} else {
			maxEnding = v
		}
		if maxEnding > maxSoFar {
			maxSoFar = maxEnding
		}

		if minEnding+v < v {
			minEnding = minEnding + v
		} else {
			minEnding = v
		}
		if minEnding < minSoFar {
			minSoFar = minEnding
		}
	}

	if maxSoFar >= -minSoFar {
		return maxSoFar
	}
	return -minSoFar
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_absolute_sum(nums)
  max_ending = 0
  max_sum = 0
  min_ending = 0
  min_sum = 0

  nums.each do |num|
    max_ending = [max_ending + num, 0].max
    max_sum = [max_sum, max_ending].max

    min_ending = [min_ending + num, 0].min
    min_sum = [min_sum, min_ending].min
  end

  [max_sum, -min_sum].max
end
```

## Scala

```scala
object Solution {
    def maxAbsoluteSum(nums: Array[Int]): Int = {
        var maxEnding = 0
        var maxSoFar = Int.MinValue
        var minEnding = 0
        var minSoFar = Int.MaxValue

        for (num <- nums) {
            maxEnding = math.max(num, maxEnding + num)
            maxSoFar = math.max(maxSoFar, maxEnding)

            minEnding = math.min(num, minEnding + num)
            minSoFar = math.min(minSoFar, minEnding)
        }

        math.max(maxSoFar, -minSoFar)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_absolute_sum(nums: Vec<i32>) -> i32 {
        let mut cur_max: i64 = 0;
        let mut best_max: i64 = 0;
        let mut cur_min: i64 = 0;
        let mut best_min: i64 = 0;

        for &v in nums.iter() {
            let val = v as i64;
            cur_max = (cur_max + val).max(0);
            best_max = best_max.max(cur_max);
            cur_min = (cur_min + val).min(0);
            best_min = best_min.min(cur_min);
        }

        let ans = best_max.max(-best_min);
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-absolute-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums)
             (max-end 0)
             (max-sofar 0)
             (min-end 0)
             (min-sofar 0))
    (if (null? lst)
        (max max-sofar (- min-sofar))
        (let* ((x (car lst))
               (new-max-end (max (+ max-end x) x))
               (new-max-sofar (max max-sofar new-max-end))
               (new-min-end (min (+ min-end x) x))
               (new-min-sofar (min min-sofar new-min-end)))
          (loop (cdr lst)
                new-max-end
                new-max-sofar
                new-min-end
                new-min-sofar)))))
```

## Erlang

```erlang
-spec max_absolute_sum(Nums :: [integer()]) -> integer().
max_absolute_sum(Nums) ->
    {_, MaxGlob, _, MinGlob} = lists:foldl(
        fun(N, {MaxEnd, MaxAcc, MinEnd, MinAcc}) ->
            NewMaxEnd = erlang:max(N, MaxEnd + N),
            NewMaxAcc = erlang:max(MaxAcc, NewMaxEnd),
            NewMinEnd = erlang:min(N, MinEnd + N),
            NewMinAcc = erlang:min(MinAcc, NewMinEnd),
            {NewMaxEnd, NewMaxAcc, NewMinEnd, NewMinAcc}
        end,
        {0, 0, 0, 0},
        Nums),
    MaxAbsPos = abs(MaxGlob),
    MaxAbsNeg = abs(MinGlob),
    erlang:max(MaxAbsPos, MaxAbsNeg).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_absolute_sum(nums :: [integer]) :: integer
  def max_absolute_sum(nums) do
    {max_sum, _, min_sum, _} =
      Enum.reduce(nums, {0, 0, 0, 0}, fn num, {max_sum, cur_max, min_sum, cur_min} ->
        new_cur_max = max(cur_max + num, num)
        new_max_sum = max(max_sum, new_cur_max)

        new_cur_min = min(cur_min + num, num)
        new_min_sum = min(min_sum, new_cur_min)

        {new_max_sum, new_cur_max, new_min_sum, new_cur_min}
      end)

    max(max_sum, -min_sum)
  end
end
```

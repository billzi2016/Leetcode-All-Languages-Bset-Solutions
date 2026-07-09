# 1838. Frequency of the Most Frequent Element

## Cpp

```cpp
class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        long long left = 0;
        long long windowSum = 0;
        int ans = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            windowSum += nums[right];
            while ((long long)(right - left + 1) * nums[right] - windowSum > k) {
                windowSum -= nums[left];
                ++left;
            }
            ans = std::max(ans, right - (int)left + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxFrequency(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        long windowSum = 0;
        int left = 0;
        int best = 1;
        for (int right = 0; right < nums.length; right++) {
            windowSum += nums[right];
            while ((long)(right - left + 1) * nums[right] - windowSum > k) {
                windowSum -= nums[left];
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        total = 0
        best = 1
        for right in range(len(nums)):
            total += nums[right]
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1
            best = max(best, right - left + 1)
        return best
```

## Python3

```python
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        best = 1
        for right, val in enumerate(nums):
            window_sum += val
            while (right - left + 1) * val - window_sum > k:
                window_sum -= nums[left]
                left += 1
            best = max(best, right - left + 1)
        return best
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int maxFrequency(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    
    long long sum = 0;
    int left = 0;
    int ans = 1;
    
    for (int right = 0; right < numsSize; ++right) {
        sum += nums[right];
        while ((long long)nums[right] * (right - left + 1) - sum > k) {
            sum -= nums[left];
            ++left;
        }
        int window = right - left + 1;
        if (window > ans) ans = window;
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxFrequency(int[] nums, int k)
    {
        Array.Sort(nums);
        long sum = 0;
        int left = 0;
        int best = 1;

        for (int right = 0; right < nums.Length; right++)
        {
            sum += nums[right];

            while ((long)(right - left + 1) * nums[right] - sum > k)
            {
                sum -= nums[left];
                left++;
            }

            int windowSize = right - left + 1;
            if (windowSize > best)
                best = windowSize;
        }

        return best;
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
var maxFrequency = function(nums, k) {
    nums.sort((a, b) => a - b);
    let left = 0;
    let sum = 0;
    let ans = 0;
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while ((right - left + 1) * nums[right] - sum > k) {
            sum -= nums[left];
            left++;
        }
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
};
```

## Typescript

```typescript
function maxFrequency(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let left = 0;
    let sum = 0;
    let ans = 1;

    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while ((right - left + 1) * nums[right] - sum > k) {
            sum -= nums[left];
            left++;
        }
        ans = Math.max(ans, right - left + 1);
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
    function maxFrequency($nums, $k) {
        sort($nums);
        $left = 0;
        $currSum = 0;
        $ans = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $currSum += $nums[$right];
            while (($right - $left + 1) * $nums[$right] - $currSum > $k) {
                $currSum -= $nums[$left];
                $left++;
            }
            $windowSize = $right - $left + 1;
            if ($windowSize > $ans) {
                $ans = $windowSize;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int) -> Int {
        let sortedNums = nums.sorted()
        var left = 0
        var windowSum: Int64 = 0
        var answer = 0
        let n = sortedNums.count
        for right in 0..<n {
            windowSum += Int64(sortedNums[right])
            while Int64(right - left + 1) * Int64(sortedNums[right]) - windowSum > Int64(k) {
                windowSum -= Int64(sortedNums[left])
                left += 1
            }
            answer = max(answer, right - left + 1)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFrequency(nums: IntArray, k: Int): Int {
        nums.sort()
        var left = 0
        var sum = 0L
        val kk = k.toLong()
        var answer = 0
        for (right in nums.indices) {
            sum += nums[right].toLong()
            while ((right - left + 1).toLong() * nums[right] - sum > kk) {
                sum -= nums[left].toLong()
                left++
            }
            val size = right - left + 1
            if (size > answer) answer = size
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxFrequency(List<int> nums, int k) {
    nums.sort();
    int left = 0;
    int ans = 0;
    int currSum = 0;

    for (int right = 0; right < nums.length; right++) {
      currSum += nums[right];
      while ((right - left + 1) * nums[right] - currSum > k) {
        currSum -= nums[left];
        left++;
      }
      int windowSize = right - left + 1;
      if (windowSize > ans) ans = windowSize;
    }

    return ans;
  }
}
```

## Golang

```go
import "sort"

func maxFrequency(nums []int, k int) int {
	if len(nums) == 0 {
		return 0
	}
	sort.Ints(nums)
	left := 0
	var sum int64 = 0
	ans := 1
	kk := int64(k)

	for right, v := range nums {
		sum += int64(v)
		// required operations to make all elements in [left,right] equal to v
		for int64(right-left+1)*int64(v)-sum > kk {
			sum -= int64(nums[left])
			left++
		}
		if curLen := right - left + 1; curLen > ans {
			ans = curLen
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_frequency(nums, k)
  nums.sort!
  left = 0
  total = 0
  ans = 0
  nums.each_with_index do |val, right|
    total += val
    while (right - left + 1) * val - total > k
      total -= nums[left]
      left += 1
    end
    ans = [ans, right - left + 1].max
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxFrequency(nums: Array[Int], k: Int): Int = {
        val sorted = nums.sorted
        var left = 0
        var sum: Long = 0L
        var ans = 0
        val kk = k.toLong

        for (right <- sorted.indices) {
            sum += sorted(right).toLong
            while ((right - left + 1).toLong * sorted(right) - sum > kk) {
                sum -= sorted(left).toLong
                left += 1
            }
            ans = math.max(ans, right - left + 1)
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let n = nums.len();
        let mut left = 0usize;
        let mut curr_sum: i64 = 0;
        let mut ans = 0usize;
        let k_i64 = k as i64;

        for right in 0..n {
            let target = nums[right] as i64;
            curr_sum += target;

            while (right - left + 1) as i64 * target - curr_sum > k_i64 {
                curr_sum -= nums[left] as i64;
                left += 1;
            }

            ans = ans.max(right - left + 1);
        }

        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (max-frequency nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted (sort nums <)]
         [v (list->vector sorted)]
         [n (vector-length v)])
    (if (= n 0)
        0
        (let ()
          (define left 0)
          (define curr 0)
          (define ans 0)
          (for ([right (in-range n)])
            (define target (vector-ref v right))
            (set! curr (+ curr target))
            ;; shrink window while operations exceed k
            (let shrink ((l left) (c curr))
              (if (> (- (* (- right l + 1) target) c) k)
                  (shrink (+ l 1) (- c (vector-ref v l)))
                  (begin
                    (set! left l)
                    (set! curr c))))
            (when (> (+ 1 (- right left)) ans)
              (set! ans (+ 1 (- right left)))))
          ans))))
```

## Erlang

```erlang
-module(solution).
-export([max_frequency/2]).

-spec max_frequency(Nums :: [integer()], K :: integer()) -> integer().
max_frequency(Nums, K) ->
    Sorted = lists:sort(Nums),
    NumArr = array:from_list(Sorted),      % 1‑based indexing
    N = length(Sorted),
    process(NumArr, N, K, 1, 1, 0, 0).

%% process(Array, N, K, RightIdx, LeftIdx, CurrSum, MaxAns) -> integer()
process(_Array, N, _K, Right, _Left, _CurrSum, MaxAns) when Right > N ->
    MaxAns;
process(Array, N, K, Right, Left, CurrSum, MaxAns) ->
    Val = array:get(Right, Array),
    NewSum = CurrSum + Val,
    {NewLeft, ShrunkSum} = shrink(Array, Right, Left, NewSum, K, Val),
    WindowSize = Right - NewLeft + 1,
    NewMax = case WindowSize > MaxAns of
                 true -> WindowSize;
                 false -> MaxAns
             end,
    process(Array, N, K, Right + 1, NewLeft, ShrunkSum, NewMax).

%% shrink(Array, RightIdx, LeftIdx, Sum, K, Target) -> {NewLeft, NewSum}
shrink(_Array, Right, Left, Sum, K, Target) ->
    Required = (Right - Left + 1) * Target - Sum,
    if
        Required > K ->
            LeftVal = array:get(Left, _Array),
            shrink(_Array, Right, Left + 1, Sum - LeftVal, K, Target);
        true ->
            {Left, Sum}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_frequency(nums :: [integer], k :: integer) :: integer
  def max_frequency(nums, k) do
    sorted = Enum.sort(nums)
    arr = List.to_tuple(sorted)
    n = tuple_size(arr)

    {ans, _left, _curr} =
      0..(n - 1)
      |> Enum.reduce({0, 0, 0}, fn right, {ans, left, curr_sum} ->
        target = elem(arr, right)
        curr_sum = curr_sum + target

        {new_left, new_curr} = shrink_window(left, curr_sum, right, target, k, arr)

        window_size = right - new_left + 1
        ans = if window_size > ans, do: window_size, else: ans

        {ans, new_left, new_curr}
      end)

    ans
  end

  defp shrink_window(left, curr_sum, right, target, k, arr) do
    needed = (right - left + 1) * target - curr_sum

    if needed > k do
      new_curr = curr_sum - elem(arr, left)
      shrink_window(left + 1, new_curr, right, target, k, arr)
    else
      {left, curr_sum}
    end
  end
end
```

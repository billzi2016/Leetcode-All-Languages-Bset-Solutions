# 0053. Maximum Subarray

## Cpp

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current = nums[0];
        int best = nums[0];
        for (size_t i = 1; i < nums.size(); ++i) {
            current = std::max(nums[i], current + nums[i]);
            best = std::max(best, current);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int current = nums[0];
        int best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            current = Math.max(nums[i], current + nums[i]);
            best = Math.max(best, current);
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global
```

## Python3

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
```

## C

```c
int maxSubArray(int* nums, int numsSize) {
    int max_current = nums[0];
    int max_global = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (max_current > 0)
            max_current += nums[i];
        else
            max_current = nums[i];
        if (max_current > max_global)
            max_global = max_current;
    }
    return max_global;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSubArray(int[] nums) {
        int maxSoFar = nums[0];
        int current = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            current = Math.Max(nums[i], current + nums[i]);
            maxSoFar = Math.Max(maxSoFar, current);
        }
        return maxSoFar;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let current = nums[0];
    let best = nums[0];
    for (let i = 1; i < nums.length; i++) {
        current = Math.max(nums[i], current + nums[i]);
        best = Math.max(best, current);
    }
    return best;
};
```

## Typescript

```typescript
function maxSubArray(nums: number[]): number {
    let maxSoFar = nums[0];
    let current = nums[0];
    for (let i = 1; i < nums.length; i++) {
        current = Math.max(nums[i], current + nums[i]);
        maxSoFar = Math.max(maxSoFar, current);
    }
    return maxSoFar;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSubArray($nums) {
        $maxSoFar = $nums[0];
        $currMax = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $currMax = max($nums[$i], $currMax + $nums[$i]);
            if ($currMax > $maxSoFar) {
                $maxSoFar = $currMax;
            }
        }
        return $maxSoFar;
    }
}
```

## Swift

```swift
class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        var current = nums[0]
        var best = nums[0]
        for i in 1..<nums.count {
            current = max(nums[i], current + nums[i])
            best = max(best, current)
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var maxEndingHere = nums[0]
        var maxSoFar = nums[0]
        for (i in 1 until nums.size) {
            val num = nums[i]
            maxEndingHere = if (maxEndingHere + num > num) maxEndingHere + num else num
            if (maxEndingHere > maxSoFar) {
                maxSoFar = maxEndingHere
            }
        }
        return maxSoFar
    }
}
```

## Dart

```dart
class Solution {
  int maxSubArray(List<int> nums) {
    int current = nums[0];
    int best = nums[0];
    for (int i = 1; i < nums.length; i++) {
      current = (current > 0) ? current + nums[i] : nums[i];
      if (current > best) best = current;
    }
    return best;
  }
}
```

## Golang

```go
func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	maxSoFar, cur := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		if cur < 0 {
			cur = nums[i]
		} else {
			cur += nums[i]
		}
		if cur > maxSoFar {
			maxSoFar = cur
		}
	}
	return maxSoFar
}
```

## Ruby

```ruby
def max_sub_array(nums)
  max_current = nums[0]
  max_global = nums[0]
  nums[1..-1].each do |x|
    max_current = [x, max_current + x].max
    max_global = [max_global, max_current].max
  end
  max_global
end
```

## Scala

```scala
object Solution {
    def maxSubArray(nums: Array[Int]): Int = {
        var maxEndingHere = nums(0)
        var maxSoFar = nums(0)
        var i = 1
        while (i < nums.length) {
            val x = nums(i)
            maxEndingHere = math.max(x, maxEndingHere + x)
            if (maxEndingHere > maxSoFar) maxSoFar = maxEndingHere
            i += 1
        }
        maxSoFar
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut current = nums[0];
        let mut best = nums[0];
        for &num in nums.iter().skip(1) {
            current = std::cmp::max(num, current + num);
            best = std::cmp::max(best, current);
        }
        best
    }
}
```

## Racket

```racket
(define/contract (max-sub-array nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((rest (cdr nums))
             (current (car nums))
             (best (car nums)))
    (if (null? rest)
        best
        (let* ((x (car rest))
               (new-current (max x (+ current x))))
          (loop (cdr rest) new-current (max best new-current))))))
```

## Erlang

```erlang
-spec max_sub_array(Nums :: [integer()]) -> integer().
max_sub_array([H|T]) ->
    {_, Global} = lists:foldl(
        fun (X, {Curr, Glob}) ->
            NewCurr = erlang:max(X, Curr + X),
            NewGlob = erlang:max(NewCurr, Glob),
            {NewCurr, NewGlob}
        end,
        {H, H},
        T
    ),
    Global.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sub_array(nums :: [integer]) :: integer
  def max_sub_array([head | tail]) do
    {_curr, best} =
      Enum.reduce(tail, {head, head}, fn x, {cur, best} ->
        new_cur = max(x, cur + x)
        new_best = max(best, new_cur)
        {new_cur, new_best}
      end)

    best
  end
end
```

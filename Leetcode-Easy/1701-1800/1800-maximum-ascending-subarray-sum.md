# 1800. Maximum Ascending Subarray Sum

## Cpp

```cpp
class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int maxSum = nums[0];
        int curSum = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1]) {
                curSum += nums[i];
            } else {
                maxSum = max(maxSum, curSum);
                curSum = nums[i];
            }
        }
        return max(maxSum, curSum);
    }
};
```

## Java

```java
class Solution {
    public int maxAscendingSum(int[] nums) {
        int maxSum = 0;
        int currentSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                currentSum += nums[i];
            } else {
                if (currentSum > maxSum) {
                    maxSum = currentSum;
                }
                currentSum = nums[i];
            }
        }
        return Math.max(maxSum, currentSum);
    }
}
```

## Python

```python
class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += nums[i]
            else:
                if cur > max_sum:
                    max_sum = cur
                cur = nums[i]
        return max(max_sum, cur)
```

## Python3

```python
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[i]
        return max(max_sum, cur_sum)
```

## C

```c
int maxAscendingSum(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int maxSum = nums[0];
    int curSum = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > nums[i - 1]) {
            curSum += nums[i];
        } else {
            if (curSum > maxSum) maxSum = curSum;
            curSum = nums[i];
        }
    }
    if (curSum > maxSum) maxSum = curSum;
    return maxSum;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxAscendingSum(int[] nums)
    {
        int maxSum = 0;
        int currentSum = nums[0];

        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] > nums[i - 1])
            {
                currentSum += nums[i];
            }
            else
            {
                if (currentSum > maxSum)
                    maxSum = currentSum;
                currentSum = nums[i];
            }
        }

        return currentSum > maxSum ? currentSum : maxSum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAscendingSum = function(nums) {
    let maxSum = 0;
    let curSum = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            curSum += nums[i];
        } else {
            if (curSum > maxSum) maxSum = curSum;
            curSum = nums[i];
        }
    }
    return Math.max(maxSum, curSum);
};
```

## Typescript

```typescript
function maxAscendingSum(nums: number[]): number {
    let maxSum = nums[0];
    let curSum = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            curSum += nums[i];
        } else {
            if (curSum > maxSum) maxSum = curSum;
            curSum = nums[i];
        }
    }
    return Math.max(maxSum, curSum);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAscendingSum($nums) {
        $max = 0;
        $curr = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] > $nums[$i - 1]) {
                $curr += $nums[$i];
            } else {
                if ($curr > $max) {
                    $max = $curr;
                }
                $curr = $nums[$i];
            }
        }
        return max($max, $curr);
    }
}
```

## Swift

```swift
class Solution {
    func maxAscendingSum(_ nums: [Int]) -> Int {
        var maxSum = nums[0]
        var currentSum = nums[0]
        for i in 1..<nums.count {
            if nums[i] > nums[i - 1] {
                currentSum += nums[i]
            } else {
                currentSum = nums[i]
            }
            if currentSum > maxSum {
                maxSum = currentSum
            }
        }
        return maxSum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxAscendingSum(nums: IntArray): Int {
        var maxSum = 0
        var currentSum = nums[0]
        for (i in 1 until nums.size) {
            if (nums[i] > nums[i - 1]) {
                currentSum += nums[i]
            } else {
                if (currentSum > maxSum) maxSum = currentSum
                currentSum = nums[i]
            }
        }
        if (currentSum > maxSum) maxSum = currentSum
        return maxSum
    }
}
```

## Dart

```dart
class Solution {
  int maxAscendingSum(List<int> nums) {
    int currentSum = nums[0];
    int maxSum = currentSum;
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] > nums[i - 1]) {
        currentSum += nums[i];
      } else {
        if (currentSum > maxSum) {
          maxSum = currentSum;
        }
        currentSum = nums[i];
      }
    }
    return currentSum > maxSum ? currentSum : maxSum;
  }
}
```

## Golang

```go
func maxAscendingSum(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	maxSum := nums[0]
	curSum := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			curSum += nums[i]
		} else {
			curSum = nums[i]
		}
		if curSum > maxSum {
			maxSum = curSum
		}
	}
	return maxSum
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_ascending_sum(nums)
  max_sum = 0
  cur_sum = nums[0]

  (1...nums.length).each do |i|
    if nums[i] > nums[i - 1]
      cur_sum += nums[i]
    else
      max_sum = [max_sum, cur_sum].max
      cur_sum = nums[i]
    end
  end

  [max_sum, cur_sum].max
end
```

## Scala

```scala
object Solution {
    def maxAscendingSum(nums: Array[Int]): Int = {
        var maxSum = 0
        var cur = 0
        for (i <- nums.indices) {
            if (i == 0 || nums(i) > nums(i - 1)) {
                cur += nums(i)
            } else {
                cur = nums(i)
            }
            if (cur > maxSum) maxSum = cur
        }
        maxSum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let mut max_sum = 0;
        let mut cur_sum = 0;
        let mut prev: Option<i32> = None;

        for &x in nums.iter() {
            match prev {
                Some(p) if x > p => {
                    cur_sum += x;
                }
                _ => {
                    max_sum = max_sum.max(cur_sum);
                    cur_sum = x;
                }
            }
            prev = Some(x);
        }

        max_sum.max(cur_sum)
    }
}
```

## Racket

```racket
(define/contract (max-ascending-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? nums)
      0
      (let loop ((prev (car nums))
                 (rest (cdr nums))
                 (cur-sum (car nums))
                 (max-sum (car nums)))
        (if (null? rest)
            (max cur-sum max-sum)
            (let* ((x (car rest))
                   (new-cur (if (> x prev) (+ cur-sum x) x))
                   (new-max (max max-sum new-cur)))
              (loop x (cdr rest) new-cur new-max))))))
```

## Erlang

```erlang
-spec max_ascending_sum(Nums :: [integer()]) -> integer().
max_ascending_sum([]) ->
    0;
max_ascending_sum([H|T]) ->
    helper(H, T, H, H).

helper(_Prev, [], CurSum, MaxSum) ->
    if CurSum > MaxSum -> CurSum; true -> MaxSum end;
helper(Prev, [X|Xs], CurSum, MaxSum) ->
    if X > Prev ->
            NewCur = CurSum + X,
            helper(X, Xs, NewCur, MaxSum);
       true ->
            NewMax = if CurSum > MaxSum -> CurSum; true -> MaxSum end,
            helper(X, Xs, X, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_ascending_sum(nums :: [integer]) :: integer
  def max_ascending_sum(nums) do
    {max_sum, cur_sum, _prev} =
      Enum.reduce(nums, {0, 0, nil}, fn val, {max_sum, cur_sum, prev} ->
        if prev != nil and val > prev do
          new_cur = cur_sum + val
          {max(max_sum, new_cur), new_cur, val}
        else
          {max(max_sum, cur_sum), val, val}
        end
      end)

    max(max_sum, cur_sum)
  end
end
```

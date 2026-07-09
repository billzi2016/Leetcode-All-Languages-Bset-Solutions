# 2574. Left and Right Sum Differences

## Cpp

```cpp
class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        long long total = prefix[n];
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            long long left = prefix[i];
            long long right = total - prefix[i + 1];
            ans[i] = static_cast<int>(llabs(left - right));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] leftRightDifference(int[] nums) {
        int n = nums.length;
        int total = 0;
        for (int num : nums) total += num;
        int left = 0;
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            int right = total - left - nums[i];
            answer[i] = Math.abs(left - right);
            left += nums[i];
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        left = 0
        ans = []
        for i, val in enumerate(nums):
            right = total - left - val
            ans.append(abs(left - right))
            left += val
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        result = []
        for num in nums:
            right_sum = total - left_sum - num
            result.append(abs(left_sum - right_sum))
            left_sum += num
        return result
```

## C

```c
#include <stdlib.h>
#include <stdio.h>

int* leftRightDifference(int* nums, int numsSize, int* returnSize) {
    long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    
    int *ans = (int*)malloc(numsSize * sizeof(int));
    long leftSum = 0;
    for (int i = 0; i < numsSize; ++i) {
        long rightSum = total - leftSum - nums[i];
        long diff = leftSum - rightSum;
        if (diff < 0) diff = -diff;
        ans[i] = (int)diff;
        leftSum += nums[i];
    }
    
    *returnSize = numsSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] LeftRightDifference(int[] nums) {
        int n = nums.Length;
        long total = 0;
        foreach (int v in nums) total += v;
        int[] answer = new int[n];
        long leftSum = 0;
        for (int i = 0; i < n; i++) {
            long rightSum = total - leftSum - nums[i];
            answer[i] = (int)Math.Abs(leftSum - rightSum);
            leftSum += nums[i];
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRightDifference = function(nums) {
    const n = nums.length;
    let total = 0;
    for (let v of nums) total += v;
    const result = new Array(n);
    let leftSum = 0;
    for (let i = 0; i < n; ++i) {
        const rightSum = total - leftSum - nums[i];
        result[i] = Math.abs(leftSum - rightSum);
        leftSum += nums[i];
    }
    return result;
};
```

## Typescript

```typescript
function leftRightDifference(nums: number[]): number[] {
    const n = nums.length;
    const total = nums.reduce((acc, val) => acc + val, 0);
    const result: number[] = new Array(n);
    let leftSum = 0;
    for (let i = 0; i < n; i++) {
        const rightSum = total - leftSum - nums[i];
        result[i] = Math.abs(leftSum - rightSum);
        leftSum += nums[i];
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function leftRightDifference($nums) {
        $n = count($nums);
        $total = array_sum($nums);
        $left = 0;
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $right = $total - $left - $nums[$i];
            $ans[] = abs($left - $right);
            $left += $nums[$i];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func leftRightDifference(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var total = 0
        for v in nums { total += v }
        var left = 0
        var result = Array(repeating: 0, count: n)
        for i in 0..<n {
            let right = total - left - nums[i]
            result[i] = abs(left - right)
            left += nums[i]
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun leftRightDifference(nums: IntArray): IntArray {
        val n = nums.size
        val total = nums.sum()
        var leftSum = 0
        val answer = IntArray(n)
        for (i in 0 until n) {
            val rightSum = total - leftSum - nums[i]
            answer[i] = kotlin.math.abs(leftSum - rightSum)
            leftSum += nums[i]
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> leftRightDifference(List<int> nums) {
    int total = 0;
    for (int v in nums) total += v;
    List<int> ans = List.filled(nums.length, 0);
    int leftSum = 0;
    for (int i = 0; i < nums.length; ++i) {
      int rightSum = total - leftSum - nums[i];
      ans[i] = (leftSum - rightSum).abs();
      leftSum += nums[i];
    }
    return ans;
  }
}
```

## Golang

```go
func leftRightDifference(nums []int) []int {
    n := len(nums)
    ans := make([]int, n)
    total := 0
    for _, v := range nums {
        total += v
    }
    left := 0
    for i, v := range nums {
        right := total - left - v
        diff := left - right
        if diff < 0 {
            diff = -diff
        }
        ans[i] = diff
        left += v
    }
    return ans
}
```

## Ruby

```ruby
def left_right_difference(nums)
  total = nums.sum
  left_sum = 0
  result = []
  nums.each do |num|
    right_sum = total - left_sum - num
    result << (left_sum - right_sum).abs
    left_sum += num
  end
  result
end
```

## Scala

```scala
object Solution {
    def leftRightDifference(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val total = nums.foldLeft(0L)(_ + _)
        var leftSum = 0L
        val result = new Array[Int](n)
        for (i <- 0 until n) {
            val rightSum = total - leftSum - nums(i).toLong
            result(i) = math.abs(leftSum - rightSum).toInt
            leftSum += nums(i).toLong
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut left_sum: i64 = 0;
        let mut answer = Vec::with_capacity(nums.len());
        for &v in &nums {
            let right_sum = total - left_sum - v as i64;
            let diff = (left_sum - right_sum).abs() as i32;
            answer.push(diff);
            left_sum += v as i64;
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (left-right-difference nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((total (apply + nums)))
    (let loop ((lst nums) (left 0) (acc '()))
      (if (null? lst)
          (reverse acc)
          (let* ((cur (car lst))
                 (right (- total left cur))
                 (diff (abs (- left right))))
            (loop (cdr lst) (+ left cur) (cons diff acc)))))))
```

## Erlang

```erlang
-spec left_right_difference(Nums :: [integer()]) -> [integer()].
left_right_difference(Nums) ->
    Total = lists:sum(Nums),
    {_, RevAns} = lists:foldl(
        fun(Elem, {Left, Acc}) ->
            Right = Total - Left - Elem,
            Diff = erlang:abs(Left - Right),
            {Left + Elem, [Diff | Acc]}
        end,
        {0, []},
        Nums
    ),
    lists:reverse(RevAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec left_right_difference(nums :: [integer]) :: [integer]
  def left_right_difference(nums) do
    total = Enum.sum(nums)

    {result, _} =
      Enum.map_reduce(nums, 0, fn num, left_sum ->
        right_sum = total - left_sum - num
        diff = abs(left_sum - right_sum)
        {diff, left_sum + num}
      end)

    result
  end
end
```

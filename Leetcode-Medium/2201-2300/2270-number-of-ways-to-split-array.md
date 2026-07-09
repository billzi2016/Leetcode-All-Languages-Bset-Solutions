# 2270. Number of Ways to Split Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        long long rightSum = 0;
        for (int v : nums) rightSum += v;
        long long leftSum = 0;
        int count = 0;
        for (size_t i = 0; i + 1 < nums.size(); ++i) {
            leftSum += nums[i];
            rightSum -= nums[i];
            if (leftSum >= rightSum) ++count;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int waysToSplitArray(int[] nums) {
        long total = 0;
        for (int num : nums) {
            total += num;
        }
        long leftSum = 0;
        int count = 0;
        // iterate up to the second last element as split point
        for (int i = 0; i < nums.length - 1; i++) {
            leftSum += nums[i];
            long rightSum = total - leftSum;
            if (leftSum >= rightSum) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum = sum(nums)
        left_sum = 0
        count = 0
        # iterate up to second last element as split point
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        count = 0
        # iterate up to second last element as split point must leave non‑empty right part
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            total -= nums[i]  # now total is the sum of the right part
            if left_sum >= total:
                count += 1
        return count
```

## C

```c
int waysToSplitArray(int* nums, int numsSize) {
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    long long leftSum = 0;
    int count = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        leftSum += nums[i];
        total -= nums[i]; // now total is right sum
        if (leftSum >= total) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int WaysToSplitArray(int[] nums)
    {
        long total = 0;
        foreach (int num in nums) total += num;

        long leftSum = 0;
        long rightSum = total;
        int count = 0;
        // split after index i, i from 0 to n-2
        for (int i = 0; i < nums.Length - 1; i++)
        {
            leftSum += nums[i];
            rightSum -= nums[i];
            if (leftSum >= rightSum) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToSplitArray = function(nums) {
    const n = nums.length;
    let total = 0;
    for (let i = 0; i < n; ++i) total += nums[i];
    
    let leftSum = 0;
    let rightSum = total;
    let count = 0;
    
    // split after index i, where i ranges from 0 to n-2
    for (let i = 0; i < n - 1; ++i) {
        leftSum += nums[i];
        rightSum -= nums[i];
        if (leftSum >= rightSum) count++;
    }
    
    return count;
};
```

## Typescript

```typescript
function waysToSplitArray(nums: number[]): number {
    let total = 0;
    for (const v of nums) total += v;
    let leftSum = 0;
    let count = 0;
    const n = nums.length;
    for (let i = 0; i < n - 1; ++i) {
        leftSum += nums[i];
        if (leftSum >= total - leftSum) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function waysToSplitArray($nums) {
        $n = count($nums);
        if ($n < 2) return 0;

        $rightSum = 0;
        foreach ($nums as $v) {
            $rightSum += $v;
        }

        $leftSum = 0;
        $count = 0;
        for ($i = 0; $i < $n - 1; ++$i) {
            $leftSum += $nums[$i];
            $rightSum -= $nums[$i];
            if ($leftSum >= $rightSum) {
                ++$count;
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func waysToSplitArray(_ nums: [Int]) -> Int {
        var total: Int64 = 0
        for v in nums {
            total += Int64(v)
        }
        var leftSum: Int64 = 0
        var count = 0
        // iterate up to the second last element as split point
        for i in 0..<(nums.count - 1) {
            leftSum += Int64(nums[i])
            let rightSum = total - leftSum
            if leftSum >= rightSum {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun waysToSplitArray(nums: IntArray): Int {
        var total = 0L
        for (v in nums) total += v.toLong()
        var leftSum = 0L
        var count = 0
        // iterate up to n-2 inclusive, because split must leave non‑empty right part
        for (i in 0 until nums.size - 1) {
            leftSum += nums[i].toLong()
            val rightSum = total - leftSum
            if (leftSum >= rightSum) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int waysToSplitArray(List<int> nums) {
    int total = 0;
    for (var v in nums) {
      total += v;
    }
    int leftSum = 0;
    int rightSum = total;
    int count = 0;
    for (int i = 0; i < nums.length - 1; ++i) {
      leftSum += nums[i];
      rightSum -= nums[i];
      if (leftSum >= rightSum) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func waysToSplitArray(nums []int) int {
    var total int64
    for _, v := range nums {
        total += int64(v)
    }
    var left int64
    count := 0
    // iterate up to len-2 because both parts must be non‑empty
    for i := 0; i < len(nums)-1; i++ {
        left += int64(nums[i])
        right := total - left
        if left >= right {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def ways_to_split_array(nums)
  total = nums.sum
  left = 0
  count = 0
  (0...nums.length - 1).each do |i|
    left += nums[i]
    right = total - left
    count += 1 if left >= right
  end
  count
end
```

## Scala

```scala
object Solution {
    def waysToSplitArray(nums: Array[Int]): Int = {
        var total: Long = 0L
        for (v <- nums) total += v.toLong

        var leftSum: Long = 0L
        var count = 0
        val n = nums.length
        var i = 0
        while (i < n - 1) {
            leftSum += nums(i).toLong
            val rightSum = total - leftSum
            if (leftSum >= rightSum) count += 1
            i += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn ways_to_split_array(nums: Vec<i32>) -> i32 {
        let mut right_sum: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut left_sum: i64 = 0;
        let mut count: i32 = 0;
        // iterate up to the second last element
        for i in 0..nums.len() - 1 {
            left_sum += nums[i] as i64;
            right_sum -= nums[i] as i64;
            if left_sum >= right_sum {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (ways-to-split-array nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((total (apply + nums)))
    (let loop ((lst nums) (left 0) (count 0))
      (if (null? (cdr lst))
          count
          (let* ((new-left (+ left (car lst)))
                 (right (- total new-left))
                 (new-count (if (>= new-left right) (+ count 1) count)))
            (loop (cdr lst) new-left new-count))))))
```

## Erlang

```erlang
-spec ways_to_split_array(Nums :: [integer()]) -> integer().
ways_to_split_array(Nums) ->
    Total = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
    count_splits(Nums, 0, Total, 0).

count_splits([], _Left, _Right, Count) ->
    Count;
count_splits([_], _Left, _Right, Count) ->
    Count;
count_splits([X|Rest], Left, Right, Count) ->
    NewLeft = Left + X,
    NewRight = Right - X,
    NewCount = if
        NewLeft >= NewRight -> Count + 1;
        true -> Count
    end,
    count_splits(Rest, NewLeft, NewRight, NewCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec ways_to_split_array(nums :: [integer]) :: integer
  def ways_to_split_array(nums) do
    n = length(nums)
    total = Enum.reduce(nums, 0, &+/2)

    {count, _} =
      Enum.with_index(nums)
      |> Enum.reduce({0, 0}, fn {val, idx}, {cnt, left_sum} ->
        if idx < n - 1 do
          new_left = left_sum + val
          right_sum = total - new_left

          new_cnt =
            if new_left >= right_sum do
              cnt + 1
            else
              cnt
            end

          {new_cnt, new_left}
        else
          {cnt, left_sum}
        end
      end)

    count
  end
end
```

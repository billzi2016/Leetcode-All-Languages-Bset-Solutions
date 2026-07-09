# 0724. Find Pivot Index

## Cpp

```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        long long total = 0;
        for (int num : nums) total += num;
        long long leftSum = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (leftSum == total - leftSum - nums[i]) return i;
            leftSum += nums[i];
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0;
        for (int num : nums) total += num;
        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (leftSum == total - leftSum - nums[i]) return i;
            leftSum += nums[i];
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1
```

## C

```c
int pivotIndex(int* nums, int numsSize) {
    long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    long left = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (left == total - left - nums[i]) {
            return i;
        }
        left += nums[i];
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int PivotIndex(int[] nums) {
        long total = 0;
        foreach (int num in nums) total += num;
        long leftSum = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (leftSum == total - leftSum - nums[i]) return i;
            leftSum += nums[i];
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let total = 0;
    for (let num of nums) total += num;
    let leftSum = 0;
    for (let i = 0; i < nums.length; i++) {
        if (leftSum === total - leftSum - nums[i]) return i;
        leftSum += nums[i];
    }
    return -1;
};
```

## Typescript

```typescript
function pivotIndex(nums: number[]): number {
    const total = nums.reduce((acc, val) => acc + val, 0);
    let leftSum = 0;
    for (let i = 0; i < nums.length; i++) {
        if (leftSum === total - leftSum - nums[i]) {
            return i;
        }
        leftSum += nums[i];
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function pivotIndex($nums) {
        $total = array_sum($nums);
        $leftSum = 0;
        foreach ($nums as $i => $num) {
            if ($leftSum == $total - $leftSum - $num) {
                return $i;
            }
            $leftSum += $num;
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func pivotIndex(_ nums: [Int]) -> Int {
        var total = 0
        for num in nums { total += num }
        var leftSum = 0
        for (i, num) in nums.enumerated() {
            if leftSum == total - leftSum - num {
                return i
            }
            leftSum += num
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pivotIndex(nums: IntArray): Int {
        var total = 0L
        for (num in nums) total += num
        var leftSum = 0L
        for (i in nums.indices) {
            if (leftSum == total - leftSum - nums[i]) return i
            leftSum += nums[i]
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int pivotIndex(List<int> nums) {
    int total = 0;
    for (var num in nums) total += num;
    int leftSum = 0;
    for (int i = 0; i < nums.length; i++) {
      if (leftSum == total - leftSum - nums[i]) return i;
      leftSum += nums[i];
    }
    return -1;
  }
}
```

## Golang

```go
func pivotIndex(nums []int) int {
    total := 0
    for _, v := range nums {
        total += v
    }
    left := 0
    for i, v := range nums {
        if left == total-left-v {
            return i
        }
        left += v
    }
    return -1
}
```

## Ruby

```ruby
def pivot_index(nums)
  total = nums.sum
  left = 0
  nums.each_with_index do |num, i|
    return i if left == total - left - num
    left += num
  end
  -1
end
```

## Scala

```scala
object Solution {
    def pivotIndex(nums: Array[Int]): Int = {
        var total: Long = 0L
        for (v <- nums) total += v
        var left: Long = 0L
        for (i <- nums.indices) {
            val right = total - left - nums(i)
            if (left == right) return i
            left += nums(i)
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut left_sum: i64 = 0;
        for (i, &num) in nums.iter().enumerate() {
            let right_sum = total - left_sum - num as i64;
            if left_sum == right_sum {
                return i as i32;
            }
            left_sum += num as i64;
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (pivot-index nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((total (foldl + 0 nums)))
    (let loop ((lst nums) (idx 0) (left 0))
      (if (null? lst)
          -1
          (let* ((right (- total (+ left (car lst)))))
            (if (= left right)
                idx
                (loop (cdr lst) (+ idx 1) (+ left (car lst)))))))))
```

## Erlang

```erlang
-spec pivot_index(Nums :: [integer()]) -> integer().
pivot_index(Nums) ->
    Total = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
    find_pivot(Nums, Total, 0, 0).

find_pivot([], _Total, _Idx, _Left) ->
    -1;
find_pivot([H|T], Total, Idx, Left) ->
    Right = Total - Left - H,
    case Left =:= Right of
        true -> Idx;
        false -> find_pivot(T, Total, Idx + 1, Left + H)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec pivot_index(nums :: [integer]) :: integer
  def pivot_index(nums) do
    total = Enum.sum(nums)

    {index, _} =
      Enum.reduce_while(Enum.with_index(nums), {-1, 0}, fn {num, idx},
                                                          {_prev_idx, left_sum} ->
        if left_sum == total - left_sum - num do
          {:halt, {idx, left_sum}}
        else
          {:cont, {-1, left_sum + num}}
        end
      end)

    index
  end
end
```

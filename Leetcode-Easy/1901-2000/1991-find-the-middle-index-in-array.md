# 1991. Find the Middle Index in Array

## Cpp

```cpp
class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
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
    public int findMiddleIndex(int[] nums) {
        int total = 0;
        for (int num : nums) total += num;
        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (leftSum == total - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for i, val in enumerate(nums):
            if left_sum == total - left_sum - val:
                return i
            left_sum += val
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, val in enumerate(nums):
            if left_sum == total - left_sum - val:
                return i
            left_sum += val
        return -1
```

## C

```c
int findMiddleIndex(int* nums, int numsSize) {
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    long long leftSum = 0;
    for (int i = 0; i < numsSize; ++i) {
        long long rightSum = total - leftSum - nums[i];
        if (leftSum == rightSum) {
            return i;
        }
        leftSum += nums[i];
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindMiddleIndex(int[] nums)
    {
        int total = 0;
        foreach (int num in nums) total += num;

        int leftSum = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (leftSum == total - leftSum - nums[i])
                return i;
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
var findMiddleIndex = function(nums) {
    let total = 0;
    for (let v of nums) total += v;
    let leftSum = 0;
    for (let i = 0; i < nums.length; ++i) {
        if (leftSum === total - leftSum - nums[i]) return i;
        leftSum += nums[i];
    }
    return -1;
};
```

## Typescript

```typescript
function findMiddleIndex(nums: number[]): number {
    let total = 0;
    for (const v of nums) total += v;
    let left = 0;
    for (let i = 0; i < nums.length; i++) {
        const right = total - left - nums[i];
        if (left === right) return i;
        left += nums[i];
    }
    return -1;
};
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMiddleIndex($nums) {
        $total = array_sum($nums);
        $leftSum = 0;
        foreach ($nums as $i => $val) {
            $rightSum = $total - $leftSum - $val;
            if ($leftSum === $rightSum) {
                return $i;
            }
            $leftSum += $val;
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func findMiddleIndex(_ nums: [Int]) -> Int {
        var total = 0
        for v in nums {
            total += v
        }
        var leftSum = 0
        for i in 0..<nums.count {
            let rightSum = total - leftSum - nums[i]
            if leftSum == rightSum {
                return i
            }
            leftSum += nums[i]
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMiddleIndex(nums: IntArray): Int {
        var total = 0
        for (num in nums) total += num
        var leftSum = 0
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
  int findMiddleIndex(List<int> nums) {
    int total = 0;
    for (int num in nums) {
      total += num;
    }
    int leftSum = 0;
    for (int i = 0; i < nums.length; i++) {
      int rightSum = total - leftSum - nums[i];
      if (leftSum == rightSum) {
        return i;
      }
      leftSum += nums[i];
    }
    return -1;
  }
}
```

## Golang

```go
func findMiddleIndex(nums []int) int {
    total := 0
    for _, v := range nums {
        total += v
    }
    leftSum := 0
    for i, v := range nums {
        if leftSum == total-leftSum-v {
            return i
        }
        leftSum += v
    }
    return -1
}
```

## Ruby

```ruby
def find_middle_index(nums)
  total = nums.sum
  left = 0
  nums.each_with_index do |val, i|
    right = total - left - val
    return i if left == right
    left += val
  end
  -1
end
```

## Scala

```scala
object Solution {
    def findMiddleIndex(nums: Array[Int]): Int = {
        var total = 0
        for (v <- nums) total += v
        var leftSum = 0
        for (i <- nums.indices) {
            val rightSum = total - leftSum - nums(i)
            if (leftSum == rightSum) return i
            leftSum += nums(i)
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_middle_index(nums: Vec<i32>) -> i32 {
        let total: i32 = nums.iter().sum();
        let mut left_sum = 0;
        for (i, &v) in nums.iter().enumerate() {
            if left_sum == total - left_sum - v {
                return i as i32;
            }
            left_sum += v;
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (find-middle-index nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((total (apply + nums)))
    (let loop ((idx 0) (left-sum 0) (rest nums))
      (cond
        [(null? rest) -1]
        [else
         (define cur (car rest))
         (define right (- total left-sum cur))
         (if (= left-sum right)
             idx
             (loop (+ idx 1) (+ left-sum cur) (cdr rest)))]))))
```

## Erlang

```erlang
-spec find_middle_index(Nums :: [integer()]) -> integer().
find_middle_index(Nums) ->
    Total = lists:sum(Nums),
    find_middle_index(Nums, 0, 0, Total).

find_middle_index([], _Idx, _Left, _Total) ->
    -1;
find_middle_index([H|T], Idx, Left, Total) ->
    Right = Total - Left - H,
    if
        Left == Right -> Idx;
        true -> find_middle_index(T, Idx + 1, Left + H, Total)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_middle_index(nums :: [integer]) :: integer
  def find_middle_index(nums) do
    total = Enum.sum(nums)

    {idx, _left} =
      Enum.reduce_while(Enum.with_index(nums), {-1, 0}, fn {val, i}, {_found, left_sum} ->
        right_sum = total - left_sum - val

        if left_sum == right_sum do
          {:halt, {i, left_sum}}
        else
          {:cont, {-1, left_sum + val}}
        end
      end)

    idx
  end
end
```

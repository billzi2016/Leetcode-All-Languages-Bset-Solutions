# 1480. Running Sum of 1d Array

## Cpp

```cpp
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> result(nums.size());
        long long sum = 0;
        for (size_t i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            result[i] = static_cast<int>(sum);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] runningSum(int[] nums) {
        int[] result = new int[nums.length];
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            result[i] = sum;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
```

## Python3

```python
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    if (returnSize) *returnSize = numsSize;
    int* result = (int*)malloc(numsSize * sizeof(int));
    if (!result) return NULL;
    long long sum = 0;
    for (int i = 0; i < numsSize; ++i) {
        sum += nums[i];
        result[i] = (int)sum;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] RunningSum(int[] nums) {
        int n = nums.Length;
        int[] result = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            result[i] = sum;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    const result = new Array(nums.length);
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        result[i] = sum;
    }
    return result;
};
```

## Typescript

```typescript
function runningSum(nums: number[]): number[] {
    const result: number[] = new Array(nums.length);
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        result[i] = sum;
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
    function runningSum($nums) {
        $sum = 0;
        foreach ($nums as $i => $val) {
            $sum += $val;
            $nums[$i] = $sum;
        }
        return $nums;
    }
}
```

## Swift

```swift
class Solution {
    func runningSum(_ nums: [Int]) -> [Int] {
        var result = nums
        for i in 1..<result.count {
            result[i] += result[i - 1]
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun runningSum(nums: IntArray): IntArray {
        val n = nums.size
        val result = IntArray(n)
        var sum = 0
        for (i in 0 until n) {
            sum += nums[i]
            result[i] = sum
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> runningSum(List<int> nums) {
    for (int i = 1; i < nums.length; ++i) {
      nums[i] += nums[i - 1];
    }
    return nums;
  }
}
```

## Golang

```go
func runningSum(nums []int) []int {
    res := make([]int, len(nums))
    sum := 0
    for i, v := range nums {
        sum += v
        res[i] = sum
    }
    return res
}
```

## Ruby

```ruby
def running_sum(nums)
  sum = 0
  nums.map { |x| sum += x }
end
```

## Scala

```scala
object Solution {
    def runningSum(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val result = new Array[Int](n)
        var sum = 0
        var i = 0
        while (i < n) {
            sum += nums(i)
            result(i) = sum
            i += 1
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut res = Vec::with_capacity(nums.len());
        let mut sum = 0i32;
        for v in nums {
            sum += v;
            res.push(sum);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (running-sum nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((xs nums) (acc 0) (res '()))
    (if (null? xs)
        (reverse res)
        (let ((new-acc (+ acc (car xs))))
          (loop (cdr xs) new-acc (cons new-acc res))))))
```

## Erlang

```erlang
-module(solution).
-export([running_sum/1]).

-spec running_sum(Nums :: [integer()]) -> [integer()].
running_sum(Nums) ->
    rev_prefix(Nums, 0, []).

rev_prefix([], _Sum, Acc) ->
    lists:reverse(Acc);
rev_prefix([H|T], Sum, Acc) ->
    NewSum = Sum + H,
    rev_prefix(T, NewSum, [NewSum | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec running_sum(nums :: [integer]) :: [integer]
  def running_sum(nums) do
    {result, _} = Enum.map_reduce(nums, 0, fn x, acc ->
      sum = acc + x
      {sum, sum}
    end)

    result
  end
end
```

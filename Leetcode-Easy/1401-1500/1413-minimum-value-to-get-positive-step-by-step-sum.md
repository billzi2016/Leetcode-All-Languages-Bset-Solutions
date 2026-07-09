# 1413. Minimum Value to Get Positive Step by Step Sum

## Cpp

```cpp
class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int cur = 0;
        int minPref = INT_MAX;
        for (int x : nums) {
            cur += x;
            minPref = min(minPref, cur);
        }
        // If the minimum prefix sum is >= 0, start value can be 1.
        // Otherwise we need to offset it so that the smallest cumulative sum becomes at least 1.
        return max(1 - minPref, 1);
    }
};
```

## Java

```java
class Solution {
    public int minStartValue(int[] nums) {
        int prefixSum = 0;
        int minPrefix = 0; // includes the empty prefix before any element
        for (int num : nums) {
            prefixSum += num;
            if (prefixSum < minPrefix) {
                minPrefix = prefixSum;
            }
        }
        return Math.max(1, 1 - minPrefix);
    }
}
```

## Python

```python
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        min_prefix = 0
        for x in nums:
            cur += x
            if cur < min_prefix:
                min_prefix = cur
        return max(1, 1 - min_prefix)
```

## Python3

```python
from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur = 0
        min_prefix = 0
        for x in nums:
            cur += x
            if cur < min_prefix:
                min_prefix = cur
        return max(1 - min_prefix, 1)
```

## C

```c
int minStartValue(int* nums, int numsSize) {
    int cum = 0;
    int minPrefix = 0; // minimum cumulative sum when starting from 0
    for (int i = 0; i < numsSize; ++i) {
        cum += nums[i];
        if (cum < minPrefix) {
            minPrefix = cum;
        }
    }
    return (minPrefix >= 0) ? 1 : 1 - minPrefix;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinStartValue(int[] nums)
    {
        int sum = 0;
        int minSum = 0;
        foreach (int num in nums)
        {
            sum += num;
            if (sum < minSum) minSum = sum;
        }
        return Math.Max(1 - minSum, 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function(nums) {
    let cum = 0;
    let minCum = 0;
    for (const n of nums) {
        cum += n;
        if (cum < minCum) minCum = cum;
    }
    return Math.max(1, 1 - minCum);
};
```

## Typescript

```typescript
function minStartValue(nums: number[]): number {
    let sum = 0;
    let minSum = 0;
    for (const num of nums) {
        sum += num;
        if (sum < minSum) minSum = sum;
    }
    return Math.max(1, 1 - minSum);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minStartValue($nums) {
        $cum = 0;
        $minCum = 0;
        foreach ($nums as $num) {
            $cum += $num;
            if ($cum < $minCum) {
                $minCum = $cum;
            }
        }
        return max(1, 1 - $minCum);
    }
}
```

## Swift

```swift
class Solution {
    func minStartValue(_ nums: [Int]) -> Int {
        var sum = 0
        var minSum = Int.max
        for num in nums {
            sum += num
            if sum < minSum { minSum = sum }
        }
        let required = 1 - minSum
        return required > 0 ? required : 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minStartValue(nums: IntArray): Int {
        var sum = 0
        var minPrefix = 0
        for (num in nums) {
            sum += num
            if (sum < minPrefix) {
                minPrefix = sum
            }
        }
        return if (minPrefix >= 0) 1 else 1 - minPrefix
    }
}
```

## Dart

```dart
class Solution {
  int minStartValue(List<int> nums) {
    int cur = 0;
    int minSum = 0;
    for (int x in nums) {
      cur += x;
      if (cur < minSum) minSum = cur;
    }
    return 1 - minSum;
  }
}
```

## Golang

```go
func minStartValue(nums []int) int {
    sum, minSum := 0, 0
    for _, v := range nums {
        sum += v
        if sum < minSum {
            minSum = sum
        }
    }
    if minSum >= 0 {
        return 1
    }
    return 1 - minSum
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_start_value(nums)
  sum = 0
  min_sum = Float::INFINITY
  nums.each do |num|
    sum += num
    min_sum = [min_sum, sum].min
  end
  required = 1 - min_sum
  required > 1 ? required : 1
end
```

## Scala

```scala
object Solution {
    def minStartValue(nums: Array[Int]): Int = {
        var sum = 0
        var minPrefix = 0
        for (num <- nums) {
            sum += num
            if (sum < minPrefix) minPrefix = sum
        }
        math.max(1 - minPrefix, 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_start_value(nums: Vec<i32>) -> i32 {
        let mut cur = 0;
        let mut min_cur = 0;
        for &v in nums.iter() {
            cur += v;
            if cur < min_cur {
                min_cur = cur;
            }
        }
        if min_cur >= 0 { 1 } else { 1 - min_cur }
    }
}
```

## Racket

```racket
(define/contract (min-start-value nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (curr 0) (min-sum 0))
    (if (null? lst)
        (max 1 (- 1 min-sum))
        (let* ((new (+ curr (car lst)))
               (new-min (if (< new min-sum) new min-sum)))
          (loop (cdr lst) new new-min)))))
```

## Erlang

```erlang
-spec min_start_value(Nums :: [integer()]) -> integer().
min_start_value(Nums) ->
    {_, MinPref} = lists:foldl(
        fun(N, {Sum, Min}) ->
            NewSum = Sum + N,
            NewMin = if NewSum < Min -> NewSum; true -> Min end,
            {NewSum, NewMin}
        end,
        {0, 0},
        Nums
    ),
    Needed = 1 - MinPref,
    case Needed > 0 of
        true -> Needed;
        false -> 1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_start_value(nums :: [integer]) :: integer
  def min_start_value(nums) do
    {_, min_prefix} =
      Enum.reduce(nums, {0, 0}, fn x, {curr, min_sofar} ->
        new_curr = curr + x
        new_min = if new_curr < min_sofar, do: new_curr, else: min_sofar
        {new_curr, new_min}
      end)

    max(1, 1 - min_prefix)
  end
end
```

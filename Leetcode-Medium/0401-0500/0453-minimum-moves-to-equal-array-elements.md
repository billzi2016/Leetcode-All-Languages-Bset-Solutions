# 0453. Minimum Moves to Equal Array Elements

## Cpp

```cpp
class Solution {
public:
    int minMoves(vector<int>& nums) {
        long long total = 0;
        int mn = nums[0];
        for (int x : nums) {
            total += x;
            if (x < mn) mn = x;
        }
        return static_cast<int>(total - static_cast<long long>(mn) * nums.size());
    }
};
```

## Java

```java
class Solution {
    public int minMoves(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int min = nums[0];
        long sum = 0L;
        for (int num : nums) {
            sum += num;
            if (num < min) min = num;
        }
        long moves = sum - (long) min * nums.length;
        return (int) moves;
    }
}
```

## Python

```python
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mn = min(nums)
        total = sum(nums)
        return total - mn * len(nums)
```

## Python3

```python
from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mn = min(nums)
        total = sum(nums)
        return total - mn * len(nums)
```

## C

```c
int minMoves(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    long long sum = 0;
    int mn = nums[0];
    for (int i = 0; i < numsSize; ++i) {
        sum += nums[i];
        if (nums[i] < mn) mn = nums[i];
    }
    return (int)(sum - (long long)mn * numsSize);
}
```

## Csharp

```csharp
public class Solution {
    public int MinMoves(int[] nums) {
        if (nums == null || nums.Length == 0) return 0;
        int min = nums[0];
        long sum = 0;
        foreach (int num in nums) {
            if (num < min) min = num;
            sum += num;
        }
        long moves = sum - (long)min * nums.Length;
        return (int)moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves = function(nums) {
    let minVal = Infinity;
    let sum = 0;
    for (const num of nums) {
        if (num < minVal) minVal = num;
        sum += num;
    }
    return sum - minVal * nums.length;
};
```

## Typescript

```typescript
function minMoves(nums: number[]): number {
    let minVal = nums[0];
    let total = 0;
    for (const num of nums) {
        if (num < minVal) minVal = num;
        total += num;
    }
    return total - minVal * nums.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minMoves($nums) {
        $min = PHP_INT_MAX;
        $sum = 0;
        foreach ($nums as $v) {
            if ($v < $min) {
                $min = $v;
            }
            $sum += $v;
        }
        return $sum - $min * count($nums);
    }
}
```

## Swift

```swift
class Solution {
    func minMoves(_ nums: [Int]) -> Int {
        var minVal = nums[0]
        var total: Int64 = 0
        for num in nums {
            if num < minVal { minVal = num }
            total += Int64(num)
        }
        let moves = total - Int64(nums.count) * Int64(minVal)
        return Int(moves)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMoves(nums: IntArray): Int {
        var minVal = nums[0]
        var sum: Long = 0
        for (num in nums) {
            if (num < minVal) minVal = num
            sum += num.toLong()
        }
        val moves = sum - minVal.toLong() * nums.size
        return moves.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minMoves(List<int> nums) {
    int minVal = nums[0];
    int sum = 0;
    for (int num in nums) {
      if (num < minVal) minVal = num;
      sum += num;
    }
    return sum - minVal * nums.length;
  }
}
```

## Golang

```go
func minMoves(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    minVal := nums[0]
    var sum int64 = 0
    for _, v := range nums {
        if v < minVal {
            minVal = v
        }
        sum += int64(v)
    }
    moves := sum - int64(minVal)*int64(len(nums))
    return int(moves)
}
```

## Ruby

```ruby
def min_moves(nums)
  min_val = nums.min
  sum = nums.sum
  sum - min_val * nums.length
end
```

## Scala

```scala
object Solution {
    def minMoves(nums: Array[Int]): Int = {
        var minVal = nums(0)
        var sum: Long = 0L
        for (v <- nums) {
            if (v < minVal) minVal = v
            sum += v.toLong
        }
        val moves = sum - nums.length.toLong * minVal.toLong
        moves.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves(nums: Vec<i32>) -> i32 {
        let mut min_val = nums[0];
        let mut sum: i64 = 0;
        for &x in &nums {
            if x < min_val {
                min_val = x;
            }
            sum += x as i64;
        }
        let n = nums.len() as i64;
        (sum - n * min_val as i64) as i32
    }
}
```

## Racket

```racket
(define/contract (min-moves nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((min-val (apply min nums))
         (total   (apply + nums))
         (n       (length nums)))
    (- total (* n min-val))))
```

## Erlang

```erlang
-spec min_moves([integer()]) -> integer().
min_moves([H|T]=Nums) ->
    {Sum, Min} = lists:foldl(
        fun(X, {S, M}) -> {S + X, erlang:min(M, X)} end,
        {H, H},
        T),
    Len = length(Nums),
    Sum - Len * Min.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves(nums :: [integer]) :: integer
  def min_moves(nums) do
    {min_val, sum} =
      Enum.reduce(nums, {nil, 0}, fn x, {cur_min, acc_sum} ->
        new_min = if cur_min == nil or x < cur_min, do: x, else: cur_min
        {new_min, acc_sum + x}
      end)

    sum - length(nums) * min_val
  end
end
```

# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

## Cpp

```cpp
class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int n = nums.size();
        int ans = std::abs(nums[0] - nums[n - 1]);
        for (int i = 1; i < n; ++i) {
            ans = std::max(ans, std::abs(nums[i] - nums[i - 1]));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int n = nums.length;
        int maxDiff = Math.abs(nums[0] - nums[n - 1]);
        for (int i = 1; i < n; i++) {
            int diff = Math.abs(nums[i] - nums[i - 1]);
            if (diff > maxDiff) {
                maxDiff = diff;
            }
        }
        return maxDiff;
    }
}
```

## Python

```python
class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_diff = abs(nums[0] - nums[-1])
        for i in range(1, n):
            diff = abs(nums[i] - nums[i-1])
            if diff > max_diff:
                max_diff = diff
        return max_diff
```

## Python3

```python
from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = abs(nums[0] - nums[-1])
        for i in range(1, n):
            diff = abs(nums[i] - nums[i - 1])
            if diff > max_diff:
                max_diff = diff
        return max_diff
```

## C

```c
int maxAdjacentDistance(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    int maxDiff = abs(nums[0] - nums[numsSize - 1]);
    for (int i = 1; i < numsSize; ++i) {
        int diff = abs(nums[i] - nums[i - 1]);
        if (diff > maxDiff) maxDiff = diff;
    }
    return maxDiff;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxAdjacentDistance(int[] nums) {
        int n = nums.Length;
        int maxDiff = Math.Abs(nums[0] - nums[n - 1]);
        for (int i = 1; i < n; i++) {
            int diff = Math.Abs(nums[i] - nums[i - 1]);
            if (diff > maxDiff) maxDiff = diff;
        }
        return maxDiff;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAdjacentDistance = function(nums) {
    const n = nums.length;
    let maxDiff = Math.abs(nums[0] - nums[n - 1]);
    for (let i = 1; i < n; ++i) {
        const diff = Math.abs(nums[i] - nums[i - 1]);
        if (diff > maxDiff) maxDiff = diff;
    }
    return maxDiff;
};
```

## Typescript

```typescript
function maxAdjacentDistance(nums: number[]): number {
    const n = nums.length;
    let maxDiff = Math.abs(nums[0] - nums[n - 1]);
    for (let i = 1; i < n; i++) {
        const diff = Math.abs(nums[i] - nums[i - 1]);
        if (diff > maxDiff) {
            maxDiff = diff;
        }
    }
    return maxDiff;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAdjacentDistance($nums) {
        $n = count($nums);
        $maxDiff = abs($nums[0] - $nums[$n - 1]);
        for ($i = 1; $i < $n; $i++) {
            $diff = abs($nums[$i] - $nums[$i - 1]);
            if ($diff > $maxDiff) {
                $maxDiff = $diff;
            }
        }
        return $maxDiff;
    }
}
```

## Swift

```swift
class Solution {
    func maxAdjacentDistance(_ nums: [Int]) -> Int {
        let n = nums.count
        var maxDiff = abs(nums[0] - nums[n - 1])
        for i in 1..<n {
            let diff = abs(nums[i] - nums[i - 1])
            if diff > maxDiff {
                maxDiff = diff
            }
        }
        return maxDiff
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxAdjacentDistance(nums: IntArray): Int {
        var maxDiff = kotlin.math.abs(nums[0] - nums[nums.lastIndex])
        for (i in 1 until nums.size) {
            val diff = kotlin.math.abs(nums[i] - nums[i - 1])
            if (diff > maxDiff) maxDiff = diff
        }
        return maxDiff
    }
}
```

## Dart

```dart
class Solution {
  int maxAdjacentDistance(List<int> nums) {
    int n = nums.length;
    int maxDiff = (nums[0] - nums[n - 1]).abs();
    for (int i = 1; i < n; ++i) {
      int diff = (nums[i] - nums[i - 1]).abs();
      if (diff > maxDiff) {
        maxDiff = diff;
      }
    }
    return maxDiff;
  }
}
```

## Golang

```go
func maxAdjacentDistance(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    maxDiff := abs(nums[0] - nums[n-1])
    for i := 1; i < n; i++ {
        diff := abs(nums[i] - nums[i-1])
        if diff > maxDiff {
            maxDiff = diff
        }
    }
    return maxDiff
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_adjacent_distance(nums)
  n = nums.length
  max_diff = (nums[0] - nums[-1]).abs
  (1...n).each do |i|
    diff = (nums[i] - nums[i - 1]).abs
    max_diff = diff if diff > max_diff
  end
  max_diff
end
```

## Scala

```scala
object Solution {
    def maxAdjacentDistance(nums: Array[Int]): Int = {
        var maxDiff = math.abs(nums(0) - nums(nums.length - 1))
        for (i <- 1 until nums.length) {
            val diff = math.abs(nums(i) - nums(i - 1))
            if (diff > maxDiff) maxDiff = diff
        }
        maxDiff
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_adjacent_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 2 {
            return 0;
        }
        let mut max_diff = (nums[0] - nums[n - 1]).abs();
        for i in 1..n {
            let diff = (nums[i] - nums[i - 1]).abs();
            if diff > max_diff {
                max_diff = diff;
            }
        }
        max_diff
    }
}
```

## Racket

```racket
(define/contract (max-adjacent-distance nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (first (car nums))
         (last (list-ref nums (- n 1)))
         (init (abs (- first last))))
    (let loop ((prev first) (rest (cdr nums)) (max-diff init))
      (if (null? rest)
          max-diff
          (let* ((curr (car rest))
                 (diff (abs (- curr prev)))
                 (new-max (if (> diff max-diff) diff max-diff)))
            (loop curr (cdr rest) new-max))))))
```

## Erlang

```erlang
-spec max_adjacent_distance(Nums :: [integer()]) -> integer().
max_adjacent_distance([H|T]) ->
    {MaxAdj, Last} = loop(T, H, 0),
    erlang:max(MaxAdj, abs(Last - H)).

loop([], Prev, Max) ->
    {Max, Prev};
loop([Curr|Rest], Prev, Max) ->
    Diff = abs(Curr - Prev),
    NewMax = erlang:max(Diff, Max),
    loop(Rest, Curr, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_adjacent_distance(nums :: [integer]) :: integer
  def max_adjacent_distance([head | _] = nums) when length(nums) >= 2 do
    init_diff = abs(head - List.last(nums))

    {_, max_diff} =
      Enum.reduce(tl(nums), {head, init_diff}, fn curr, {prev, cur_max} ->
        diff = abs(curr - prev)
        new_max = if diff > cur_max, do: diff, else: cur_max
        {curr, new_max}
      end)

    max_diff
  end

  def max_adjacent_distance(_), do: 0
end
```

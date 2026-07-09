# 0376. Wiggle Subsequence

## Cpp

```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.empty()) return 0;
        int up = 1, down = 1;
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1]) {
                up = down + 1;
            } else if (nums[i] < nums[i - 1]) {
                down = up + 1;
            }
        }
        return max(up, down);
    }
};
```

## Java

```java
class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length == 0) return 0;
        int up = 1, down = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                up = down + 1;
            } else if (nums[i] < nums[i - 1]) {
                down = up + 1;
            }
        }
        return Math.max(up, down);
    }
}
```

## Python

```python
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n

        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1

        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
            elif diff != 0:
                # update prev_diff to the latest non-zero diff when direction hasn't changed yet
                prev_diff = diff

        return count
```

## Python3

```python
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
```

## C

```c
int wiggleMaxLength(int* nums, int numsSize) {
    if (numsSize < 2) return numsSize;
    int up = 1, down = 1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > nums[i - 1]) {
            up = down + 1;
        } else if (nums[i] < nums[i - 1]) {
            down = up + 1;
        }
    }
    return up > down ? up : down;
}
```

## Csharp

```csharp
public class Solution {
    public int WiggleMaxLength(int[] nums) {
        if (nums.Length == 0) return 0;
        int up = 1, down = 1;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] > nums[i - 1]) {
                up = down + 1;
            } else if (nums[i] < nums[i - 1]) {
                down = up + 1;
            }
        }
        return Math.Max(up, down);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    const n = nums.length;
    if (n < 2) return n;

    let prevDiff = nums[1] - nums[0];
    let result = prevDiff !== 0 ? 2 : 1;

    for (let i = 2; i < n; ++i) {
        const diff = nums[i] - nums[i - 1];
        if ((diff > 0 && prevDiff <= 0) || (diff < 0 && prevDiff >= 0)) {
            result++;
            prevDiff = diff;
        }
    }

    return result;
};
```

## Typescript

```typescript
function wiggleMaxLength(nums: number[]): number {
    const n = nums.length;
    if (n < 2) return n;
    let up = 1, down = 1;
    for (let i = 1; i < n; i++) {
        if (nums[i] > nums[i - 1]) {
            up = down + 1;
        } else if (nums[i] < nums[i - 1]) {
            down = up + 1;
        }
    }
    return Math.max(up, down);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function wiggleMaxLength($nums) {
        $n = count($nums);
        if ($n < 2) {
            return $n;
        }
        $prevDiff = $nums[1] - $nums[0];
        $count = $prevDiff != 0 ? 2 : 1;
        for ($i = 2; $i < $n; $i++) {
            $diff = $nums[$i] - $nums[$i - 1];
            if (($diff > 0 && $prevDiff <= 0) || ($diff < 0 && $prevDiff >= 0)) {
                $count++;
                $prevDiff = $diff;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func wiggleMaxLength(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 2 { return n }
        var up = 1
        var down = 1
        for i in 1..<n {
            if nums[i] > nums[i - 1] {
                up = down + 1
            } else if nums[i] < nums[i - 1] {
                down = up + 1
            }
        }
        return max(up, down)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wiggleMaxLength(nums: IntArray): Int {
        if (nums.size < 2) return nums.size
        var up = 1
        var down = 1
        for (i in 1 until nums.size) {
            when {
                nums[i] > nums[i - 1] -> up = down + 1
                nums[i] < nums[i - 1] -> down = up + 1
                else -> {}
            }
        }
        return maxOf(up, down)
    }
}
```

## Dart

```dart
class Solution {
  int wiggleMaxLength(List<int> nums) {
    if (nums.length < 2) return nums.length;
    int up = 1, down = 1;
    for (int i = 1; i < nums.length; i++) {
      int diff = nums[i] - nums[i - 1];
      if (diff > 0) {
        up = down + 1;
      } else if (diff < 0) {
        down = up + 1;
      }
    }
    return up > down ? up : down;
  }
}
```

## Golang

```go
func wiggleMaxLength(nums []int) int {
    n := len(nums)
    if n < 2 {
        return n
    }
    up, down := 1, 1
    for i := 1; i < n; i++ {
        if nums[i] > nums[i-1] {
            up = down + 1
        } else if nums[i] < nums[i-1] {
            down = up + 1
        }
    }
    if up > down {
        return up
    }
    return down
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def wiggle_max_length(nums)
  return 0 if nums.empty?
  up = down = 1
  (1...nums.length).each do |i|
    if nums[i] > nums[i - 1]
      up = down + 1
    elsif nums[i] < nums[i - 1]
      down = up + 1
    end
  end
  [up, down].max
end
```

## Scala

```scala
object Solution {
    def wiggleMaxLength(nums: Array[Int]): Int = {
        val n = nums.length
        if (n < 2) return n
        var up = 1
        var down = 1
        var i = 1
        while (i < n) {
            val diff = nums(i) - nums(i - 1)
            if (diff > 0) {
                up = down + 1
            } else if (diff < 0) {
                down = up + 1
            }
            i += 1
        }
        math.max(up, down)
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 2 {
            return n as i32;
        }
        let mut up = 1;
        let mut down = 1;
        for i in 1..n {
            if nums[i] > nums[i - 1] {
                up = down + 1;
            } else if nums[i] < nums[i - 1] {
                down = up + 1;
            }
        }
        std::cmp::max(up, down) as i32
    }
}
```

## Racket

```racket
(define/contract (wiggle-max-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? nums)
      0
      (let loop ((prev (car nums))
                 (rest (cdr nums))
                 (up 1)
                 (down 1))
        (if (null? rest)
            (max up down)
            (let ((curr (car rest)))
              (cond [(> curr prev) (loop curr (cdr rest) (+ down 1) down)]
                    [(< curr prev) (loop curr (cdr rest) up (+ up 1))]
                    [else          (loop curr (cdr rest) up down)]))))))
```

## Erlang

```erlang
-spec wiggle_max_length([integer()]) -> integer().
wiggle_max_length([]) ->
    0;
wiggle_max_length([First|Rest]) ->
    {_, Up, Down} = lists:foldl(
        fun(Num, {Prev, UpAcc, DownAcc}) ->
            Diff = Num - Prev,
            if
                Diff > 0 -> {Num, DownAcc + 1, DownAcc};
                Diff < 0 -> {Num, UpAcc, UpAcc + 1};
                true      -> {Num, UpAcc, DownAcc}
            end
        end,
        {First, 1, 1},
        Rest),
    erlang:max(Up, Down).
```

## Elixir

```elixir
defmodule Solution do
  @spec wiggle_max_length(nums :: [integer]) :: integer
  def wiggle_max_length(nums) do
    case nums do
      [] -> 0
      [_] -> 1
      _ ->
        {up, down, _} =
          Enum.reduce(tl(nums), {1, 1, hd(nums)}, fn cur, {up, down, prev} ->
            diff = cur - prev

            cond do
              diff > 0 -> {down + 1, down, cur}
              diff < 0 -> {up, up + 1, cur}
              true -> {up, down, cur}
            end
          end)

        max(up, down)
    end
  end
end
```

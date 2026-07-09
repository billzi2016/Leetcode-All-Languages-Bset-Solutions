# 0413. Arithmetic Slices

## Cpp

```cpp
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return 0;
        long long total = 0;
        int cur = 0;
        for (int i = 2; i < n; ++i) {
            if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
                ++cur;
            } else {
                cur = 0;
            }
            total += cur;
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int total = 0, cur = 0;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                cur++;
                total += cur;
            } else {
                cur = 0;
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        cur = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                cur += 1
                total += cur
            else:
                cur = 0
        return total
```

## Python3

```python
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        cur = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                cur += 1
                total += cur
            else:
                cur = 0
        return total
```

## C

```c
int numberOfArithmeticSlices(int* nums, int numsSize) {
    if (numsSize < 3) return 0;
    int total = 0, cur = 0;
    for (int i = 2; i < numsSize; ++i) {
        if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
            cur++;
            total += cur;
        } else {
            cur = 0;
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfArithmeticSlices(int[] nums) {
        int n = nums.Length;
        if (n < 3) return 0;
        int total = 0;
        int cur = 0;
        for (int i = 2; i < n; i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                cur++;
                total += cur;
            } else {
                cur = 0;
            }
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function(nums) {
    let total = 0;
    let cur = 0;
    for (let i = 2; i < nums.length; i++) {
        if (nums[i] - nums[i - 1] === nums[i - 1] - nums[i - 2]) {
            cur += 1;
            total += cur;
        } else {
            cur = 0;
        }
    }
    return total;
};
```

## Typescript

```typescript
function numberOfArithmeticSlices(nums: number[]): number {
    const n = nums.length;
    if (n < 3) return 0;
    let total = 0;
    let cur = 0;
    for (let i = 2; i < n; ++i) {
        if (nums[i] - nums[i - 1] === nums[i - 1] - nums[i - 2]) {
            cur += 1;
            total += cur;
        } else {
            cur = 0;
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfArithmeticSlices($nums) {
        $n = count($nums);
        if ($n < 3) {
            return 0;
        }
        $ans = 0;
        $cur = 0;
        for ($i = 2; $i < $n; $i++) {
            if ($nums[$i] - $nums[$i - 1] === $nums[$i - 1] - $nums[$i - 2]) {
                $cur++;
                $ans += $cur;
            } else {
                $cur = 0;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfArithmeticSlices(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 3 { return 0 }
        var total = 0
        var curr = 0
        for i in 2..<n {
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2] {
                curr += 1
                total += curr
            } else {
                curr = 0
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfArithmeticSlices(nums: IntArray): Int {
        var total = 0
        var current = 0
        for (i in 2 until nums.size) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                current++
                total += current
            } else {
                current = 0
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int numberOfArithmeticSlices(List<int> nums) {
    int n = nums.length;
    if (n < 3) return 0;
    int total = 0;
    int curr = 0;
    for (int i = 2; i < n; ++i) {
      if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
        curr += 1;
        total += curr;
      } else {
        curr = 0;
      }
    }
    return total;
  }
}
```

## Golang

```go
func numberOfArithmeticSlices(nums []int) int {
    n := len(nums)
    if n < 3 {
        return 0
    }
    total, cur := 0, 0
    for i := 2; i < n; i++ {
        if nums[i]-nums[i-1] == nums[i-1]-nums[i-2] {
            cur++
            total += cur
        } else {
            cur = 0
        }
    }
    return total
}
```

## Ruby

```ruby
def number_of_arithmetic_slices(nums)
  n = nums.length
  return 0 if n < 3
  total = 0
  cur = 0
  (2...n).each do |i|
    if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]
      cur += 1
      total += cur
    else
      cur = 0
    end
  end
  total
end
```

## Scala

```scala
object Solution {
    def numberOfArithmeticSlices(nums: Array[Int]): Int = {
        var total = 0
        var cur = 0
        for (i <- 2 until nums.length) {
            if (nums(i) - nums(i - 1) == nums(i - 1) - nums(i - 2)) {
                cur += 1
                total += cur
            } else {
                cur = 0
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_arithmetic_slices(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }
        let mut total: i32 = 0;
        let mut cur: i32 = 0;
        for i in 2..n {
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] {
                cur += 1;
                total += cur;
            } else {
                cur = 0;
            }
        }
        total
    }
}
```

## Racket

```racket
(define/contract (number-of-arithmetic-slices nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((i 2) (cur 0) (ans 0))
      (if (>= i n)
          ans
          (let ((diff1 (- (vector-ref v i) (vector-ref v (- i 1))))
                (diff2 (- (vector-ref v (- i 1)) (vector-ref v (- i 2)))))
            (if (= diff1 diff2)
                (let ((newcur (+ cur 1)))
                  (loop (+ i 1) newcur (+ ans newcur)))
                (loop (+ i 1) 0 ans)))))))
```

## Erlang

```erlang
-spec number_of_arithmetic_slices(Nums :: [integer()]) -> integer().
number_of_arithmetic_slices(Nums) ->
    case Nums of
        [_ , _ , _ | Rest] = List ->
            [A, B, C | Tail] = List,
            Diff1 = B - A,
            Diff2 = C - B,
            Cur0 = if Diff1 == Diff2 -> 1; true -> 0 end,
            Total0 = Cur0,
            helper(C, Diff2, Tail, Cur0, Total0);
        _ ->
            0
    end.

helper(_Prev, _Diff, [], _Cur, Total) ->
    Total;
helper(Prev, Diff, [X | Rest], Cur, Total) ->
    NewDiff = X - Prev,
    if NewDiff == Diff ->
            NewCur = Cur + 1,
            NewTotal = Total + NewCur,
            helper(X, NewDiff, Rest, NewCur, NewTotal);
       true ->
            helper(X, NewDiff, Rest, 0, Total)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_arithmetic_slices(nums :: [integer]) :: integer
  def number_of_arithmetic_slices(nums) do
    case nums do
      [a, b, c | tail] ->
        helper(a, b, [c | tail], 0, 0)

      _ ->
        0
    end
  end

  defp helper(_prev2, _prev1, [], _cur_len, total), do: total

  defp helper(prev2, prev1, [curr | tail], cur_len, total) do
    if curr - prev1 == prev1 - prev2 do
      new_cur = cur_len + 1
      helper(prev1, curr, tail, new_cur, total + new_cur)
    else
      helper(prev1, curr, tail, 0, total)
    end
  end
end
```

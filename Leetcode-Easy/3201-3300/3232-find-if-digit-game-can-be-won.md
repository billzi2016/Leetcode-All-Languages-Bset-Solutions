# 3232. Find if Digit Game Can Be Won

## Cpp

```cpp
class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        long long total = 0, sumSingle = 0, sumDouble = 0;
        for (int x : nums) {
            total += x;
            if (x < 10) sumSingle += x;
            else sumDouble += x;
        }
        return (2 * sumSingle > total) || (2 * sumDouble > total);
    }
};
```

## Java

```java
class Solution {
    public boolean canAliceWin(int[] nums) {
        int total = 0;
        int singleSum = 0;
        int doubleSum = 0;
        for (int num : nums) {
            total += num;
            if (num < 10) {
                singleSum += num;
            } else {
                doubleSum += num;
            }
        }
        return (singleSum * 2 > total) || (doubleSum * 2 > total);
    }
}
```

## Python

```python
class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_single = 0
        for x in nums:
            if x < 10:
                sum_single += x
        total = sum(nums)
        sum_double = total - sum_single
        return sum_single != sum_double
```

## Python3

```python
from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = sum(x for x in nums if x < 10)
        total_sum = sum(nums)
        double_sum = total_sum - single_sum
        return single_sum != double_sum
```

## C

```c
#include <stdbool.h>

bool canAliceWin(int* nums, int numsSize) {
    int sumSingle = 0, sumDouble = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] < 10)
            sumSingle += nums[i];
        else
            sumDouble += nums[i];
    }
    int total = sumSingle + sumDouble;
    if (sumSingle > total - sumSingle) return true;
    if (sumDouble > total - sumDouble) return true;
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanAliceWin(int[] nums) {
        int total = 0;
        int singleSum = 0;
        foreach (int num in nums) {
            total += num;
            if (num < 10) singleSum += num;
        }
        int doubleSum = total - singleSum;
        return (2 * singleSum > total) || (2 * doubleSum > total);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canAliceWin = function(nums) {
    let singleSum = 0;
    for (const num of nums) {
        if (num < 10) singleSum += num;
    }
    const total = nums.reduce((a, b) => a + b, 0);
    const doubleSum = total - singleSum;
    return singleSum !== doubleSum;
};
```

## Typescript

```typescript
function canAliceWin(nums: number[]): boolean {
    let sumSingle = 0;
    for (const x of nums) {
        if (x < 10) sumSingle += x;
    }
    const total = nums.reduce((a, b) => a + b, 0);
    const sumDouble = total - sumSingle;
    return sumSingle !== sumDouble;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canAliceWin($nums) {
        $sumSingle = 0;
        $sumDouble = 0;
        foreach ($nums as $num) {
            if ($num < 10) {
                $sumSingle += $num;
            } else {
                $sumDouble += $num;
            }
        }
        $total = $sumSingle + $sumDouble;
        return (2 * $sumSingle > $total) || (2 * $sumDouble > $total);
    }
}
```

## Swift

```swift
class Solution {
    func canAliceWin(_ nums: [Int]) -> Bool {
        var total = 0
        var singleSum = 0
        var doubleSum = 0
        for num in nums {
            total += num
            if num < 10 {
                singleSum += num
            } else {
                doubleSum += num
            }
        }
        if singleSum > total - singleSum { return true }
        if doubleSum > total - doubleSum { return true }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canAliceWin(nums: IntArray): Boolean {
        var total = 0
        var singleSum = 0
        var doubleSum = 0
        for (num in nums) {
            total += num
            if (num < 10) {
                singleSum += num
            } else {
                doubleSum += num
            }
        }
        return singleSum > total - singleSum || doubleSum > total - doubleSum
    }
}
```

## Dart

```dart
class Solution {
  bool canAliceWin(List<int> nums) {
    int total = 0;
    int singleSum = 0;
    for (int num in nums) {
      total += num;
      if (num < 10) singleSum += num;
    }
    int doubleSum = total - singleSum;
    return (2 * singleSum > total) || (2 * doubleSum > total);
  }
}
```

## Golang

```go
func canAliceWin(nums []int) bool {
    sumSingle := 0
    for _, v := range nums {
        if v < 10 {
            sumSingle += v
        }
    }
    total := 0
    for _, v := range nums {
        total += v
    }
    sumDouble := total - sumSingle
    return sumSingle != sumDouble
}
```

## Ruby

```ruby
def can_alice_win(nums)
  total = nums.sum
  sum_single = 0
  sum_double = 0

  nums.each do |num|
    if num < 10
      sum_single += num
    else
      sum_double += num
    end
  end

  (2 * sum_single > total) || (2 * sum_double > total)
end
```

## Scala

```scala
object Solution {
    def canAliceWin(nums: Array[Int]): Boolean = {
        var sumSingle = 0
        var total = 0
        for (v <- nums) {
            total += v
            if (v < 10) sumSingle += v
        }
        val sumDouble = total - sumSingle
        sumSingle != sumDouble
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_alice_win(nums: Vec<i32>) -> bool {
        let mut sum_single = 0;
        let mut total = 0;
        for &v in nums.iter() {
            total += v;
            if v < 10 {
                sum_single += v;
            }
        }
        let sum_double = total - sum_single;
        (2 * sum_single > total) || (2 * sum_double > total)
    }
}
```

## Racket

```racket
(define/contract (can-alice-win nums)
  (-> (listof exact-integer?) boolean?)
  (define-values (sum-single sum-double)
    (for/fold ([single 0] [double 0]) ([x nums])
      (if (< x 10)
          (values (+ single x) double)
          (values single (+ double x)))))
  (let ((total (+ sum-single sum-double)))
    (or (> (* 2 sum-single) total)
        (> (* 2 sum-double) total))))
```

## Erlang

```erlang
-module(solution).
-export([can_alice_win/1]).

-spec can_alice_win(Nums :: [integer()]) -> boolean().
can_alice_win(Nums) ->
    SumSingle = lists:foldl(fun(N, Acc) ->
                                 if N < 10 -> Acc + N; true -> Acc end
                             end, 0, Nums),
    Total = lists:foldl(fun(N, Acc) -> Acc + N end, 0, Nums),
    SumDouble = Total - SumSingle,
    SumSingle =/= SumDouble.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_alice_win(nums :: [integer]) :: boolean
  def can_alice_win(nums) do
    {single_sum, double_sum} =
      Enum.reduce(nums, {0, 0}, fn n, {s, d} ->
        if n < 10, do: {s + n, d}, else: {s, d + n}
      end)

    total = single_sum + double_sum
    (2 * single_sum > total) or (2 * double_sum > total)
  end
end
```

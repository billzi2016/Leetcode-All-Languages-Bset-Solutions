# 0416. Partition Equal Subset Sum

## Cpp

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = 0;
        for (int num : nums) total += num;
        if (total % 2 != 0) return false;
        int target = total / 2;
        vector<char> dp(target + 1, 0);
        dp[0] = 1;
        for (int num : nums) {
            for (int j = target; j >= num; --j) {
                if (dp[j - num]) dp[j] = 1;
            }
        }
        return dp[target];
    }
};
```

## Java

```java
class Solution {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int num : nums) total += num;
        if ((total & 1) == 1) return false;
        int target = total / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : nums) {
            for (int j = target; j >= num; --j) {
                dp[j] = dp[j] || dp[j - num];
            }
        }
        return dp[target];
    }
}
```

## Python

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        bits = 1  # bit i set means subset sum i achievable
        for num in nums:
            bits |= bits << num
            # optional early stop to keep bits manageable
            if bits >> target & 1:
                return True
        return (bits >> target) & 1 == 1
```

## Python3

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = 1  # bitmask where bit i indicates sum i is achievable
        for num in nums:
            dp |= dp << num
        return (dp >> target) & 1 == 1
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool canPartition(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    if (total % 2 != 0) return false;
    int target = total / 2;

    bool *dp = (bool *)calloc(target + 1, sizeof(bool));
    dp[0] = true;

    for (int i = 0; i < numsSize; ++i) {
        int num = nums[i];
        for (int j = target; j >= num; --j) {
            if (!dp[j] && dp[j - num]) dp[j] = true;
        }
    }

    bool result = dp[target];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanPartition(int[] nums)
    {
        int total = 0;
        foreach (int n in nums) total += n;
        if ((total & 1) == 1) return false;

        int target = total / 2;
        bool[] dp = new bool[target + 1];
        dp[0] = true;

        foreach (int num in nums)
        {
            for (int i = target; i >= num; i--)
            {
                if (dp[i - num]) dp[i] = true;
            }
        }

        return dp[target];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    const total = nums.reduce((a, b) => a + b, 0);
    if (total % 2 !== 0) return false;
    const target = total / 2;
    const dp = new Uint8Array(target + 1);
    dp[0] = 1;
    for (const num of nums) {
        for (let j = target; j >= num; --j) {
            if (dp[j - num]) dp[j] = 1;
        }
        if (dp[target]) return true;
    }
    return !!dp[target];
};
```

## Typescript

```typescript
function canPartition(nums: number[]): boolean {
    const total = nums.reduce((a, b) => a + b, 0);
    if (total % 2 !== 0) return false;
    const target = total / 2;
    const dp = new Uint8Array(target + 1);
    dp[0] = 1;
    for (const num of nums) {
        for (let j = target; j >= num; --j) {
            if (dp[j - num]) dp[j] = 1;
        }
        if (dp[target]) return true;
    }
    return dp[target] === 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canPartition($nums) {
        $total = array_sum($nums);
        if ($total % 2 !== 0) {
            return false;
        }
        $target = intdiv($total, 2);
        $dp = array_fill(0, $target + 1, false);
        $dp[0] = true;

        foreach ($nums as $num) {
            for ($i = $target; $i >= $num; $i--) {
                if ($dp[$i - $num]) {
                    $dp[$i] = true;
                }
            }
        }

        return $dp[$target];
    }
}
```

## Swift

```swift
class Solution {
    func canPartition(_ nums: [Int]) -> Bool {
        let total = nums.reduce(0, +)
        if total % 2 != 0 { return false }
        let target = total / 2
        var dp = [Bool](repeating: false, count: target + 1)
        dp[0] = true
        
        for num in nums {
            if num > target { continue }
            var j = target
            while j >= num {
                if dp[j - num] {
                    dp[j] = true
                }
                j -= 1
            }
            if dp[target] { return true }
        }
        return dp[target]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canPartition(nums: IntArray): Boolean {
        val total = nums.sum()
        if (total % 2 != 0) return false
        val target = total / 2
        val dp = BooleanArray(target + 1)
        dp[0] = true
        for (num in nums) {
            var j = target
            while (j >= num) {
                if (dp[j - num]) dp[j] = true
                j--
            }
        }
        return dp[target]
    }
}
```

## Dart

```dart
class Solution {
  bool canPartition(List<int> nums) {
    int total = 0;
    for (int n in nums) total += n;
    if (total % 2 != 0) return false;
    int target = total ~/ 2;
    List<bool> dp = List.filled(target + 1, false);
    dp[0] = true;
    for (int num in nums) {
      for (int j = target; j >= num; --j) {
        if (dp[j - num]) dp[j] = true;
      }
    }
    return dp[target];
  }
}
```

## Golang

```go
func canPartition(nums []int) bool {
    total := 0
    for _, v := range nums {
        total += v
    }
    if total%2 != 0 {
        return false
    }
    target := total / 2
    dp := make([]bool, target+1)
    dp[0] = true
    for _, num := range nums {
        for j := target; j >= num; j-- {
            if dp[j-num] {
                dp[j] = true
            }
        }
    }
    return dp[target]
}
```

## Ruby

```ruby
def can_partition(nums)
  total = nums.sum
  return false if total.odd?
  target = total / 2
  dp = 1
  nums.each do |num|
    dp |= (dp << num)
  end
  ((dp >> target) & 1) == 1
end
```

## Scala

```scala
object Solution {
    def canPartition(nums: Array[Int]): Boolean = {
        val total = nums.sum
        if (total % 2 != 0) return false
        val target = total / 2
        val dp = new Array[Boolean](target + 1)
        dp(0) = true
        for (num <- nums) {
            var j = target
            while (j >= num) {
                if (dp(j - num)) dp(j) = true
                j -= 1
            }
        }
        dp(target)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let total: i32 = nums.iter().sum();
        if total % 2 != 0 {
            return false;
        }
        let target = (total / 2) as usize;
        let mut dp = vec![false; target + 1];
        dp[0] = true;
        for &num in nums.iter() {
            let v = num as usize;
            if v > target { continue; }
            for j in (v..=target).rev() {
                if dp[j - v] {
                    dp[j] = true;
                }
            }
        }
        dp[target]
    }
}
```

## Racket

```racket
(define/contract (can-partition nums)
  (-> (listof exact-integer?) boolean?)
  (let* ((total (apply + nums))
         (target (quotient total 2)))
    (if (odd? total)
        #f
        (let ([dp (make-vector (+ target 1) #f)])
          (vector-set! dp 0 #t)
          (for ([num nums])
            (for ([s (in-range (- target num) -1 -1)])
              (when (vector-ref dp s)
                (vector-set! dp (+ s num) #t))))
          (vector-ref dp target)))))
```

## Erlang

```erlang
-module(solution).
-export([can_partition/1]).

-spec can_partition(Nums :: [integer()]) -> boolean().
can_partition(Nums) ->
    Sum = lists:sum(Nums),
    case Sum rem 2 of
        1 -> false;
        0 ->
            Target = Sum div 2,
            Bits = compute_bits(Nums, Target, 1),
            ((Bits band (1 bsl Target)) =/= 0)
    end.

-spec compute_bits([integer()], integer(), integer()) -> integer().
compute_bits([], _Target, Bits) -> Bits;
compute_bits([H|T], Target, Bits) ->
    NewBits = Bits bor (Bits bsl H),
    Mask = (1 bsl (Target + 1)) - 1,
    compute_bits(T, Target, NewBits band Mask).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec can_partition(nums :: [integer]) :: boolean
  def can_partition(nums) do
    total = Enum.sum(nums)

    if rem(total, 2) != 0 do
      false
    else
      target = div(total, 2)
      mask = (1 <<< (target + 1)) - 1

      bits =
        Enum.reduce(nums, 1, fn x, acc ->
          ((acc <<< x) ||| acc) &&& mask
        end)

      ((bits >>> target) &&& 1) == 1
    end
  end
end
```

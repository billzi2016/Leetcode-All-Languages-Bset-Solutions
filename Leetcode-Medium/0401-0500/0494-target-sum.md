# 0494. Target Sum

## Cpp

```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        if (abs(target) > total) return 0;
        int sum = target + total;
        if (sum % 2 != 0) return 0;
        int subset = sum / 2;
        vector<int> dp(subset + 1, 0);
        dp[0] = 1;
        for (int num : nums) {
            for (int s = subset; s >= num; --s) {
                dp[s] += dp[s - num];
            }
        }
        return dp[subset];
    }
};
```

## Java

```java
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int total = 0;
        for (int num : nums) total += num;
        if (Math.abs(target) > total) return 0;
        int sumPlusTarget = total + target;
        if ((sumPlusTarget & 1) == 1) return 0; // not divisible by 2
        int subsetSum = sumPlusTarget / 2;
        int[] dp = new int[subsetSum + 1];
        dp[0] = 1;
        for (int num : nums) {
            for (int s = subsetSum; s >= num; --s) {
                dp[s] += dp[s - num];
            }
        }
        return dp[subsetSum];
    }
}
```

## Python

```python
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        # The required subset sum must be integer and non-negative
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        subset_sum = (total + target) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            # iterate backwards to avoid using the same element multiple times
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[subset_sum]
```

## Python3

```python
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # The required subset sum P must be integer and non-negative
        if (target + total) % 2 != 0 or target > total or target < -total:
            return 0
        P = (target + total) // 2
        if P < 0:
            return 0

        dp = [0] * (P + 1)
        dp[0] = 1
        for num in nums:
            # iterate backwards to avoid reuse within same iteration
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[P]
```

## C

```c
#include <stdlib.h>

int findTargetSumWays(int* nums, int numsSize, int target) {
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
    }
    
    // The required subset sum must be an integer and non‑negative
    int diff = total + target;
    if (diff < 0 || diff % 2 != 0) return 0;
    int subset = diff / 2;
    
    int *dp = (int *)calloc(subset + 1, sizeof(int));
    dp[0] = 1;  // one way to reach sum 0: choose nothing
    
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        for (int s = subset; s >= val; --s) {
            dp[s] += dp[s - val];
        }
    }
    
    int result = dp[subset];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindTargetSumWays(int[] nums, int target)
    {
        int total = 0;
        foreach (int n in nums) total += n;

        if (Math.Abs(target) > total) return 0;

        int sumPlus = target + total;
        if ((sumPlus & 1) == 1) return 0; // not divisible by 2

        int subsetSum = sumPlus / 2;
        int[] dp = new int[subsetSum + 1];
        dp[0] = 1;

        foreach (int num in nums)
        {
            for (int s = subsetSum; s >= num; s--)
            {
                dp[s] += dp[s - num];
            }
        }

        return dp[subsetSum];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function(nums, target) {
    const total = nums.reduce((a, b) => a + b, 0);
    if (Math.abs(target) > total) return 0;
    const sum = total + target;
    if (sum % 2 !== 0) return 0;
    const subset = sum / 2;
    const dp = new Array(subset + 1).fill(0);
    dp[0] = 1;
    for (const num of nums) {
        for (let s = subset; s >= num; s--) {
            dp[s] += dp[s - num];
        }
    }
    return dp[subset];
};
```

## Typescript

```typescript
function findTargetSumWays(nums: number[], target: number): number {
    const total = nums.reduce((acc, v) => acc + v, 0);
    if (Math.abs(target) > total) return 0;
    const sumPlusTarget = total + target;
    if (sumPlusTarget % 2 !== 0) return 0;
    const subsetSum = sumPlusTarget / 2;

    const dp: number[] = new Array(subsetSum + 1).fill(0);
    dp[0] = 1;

    for (const num of nums) {
        for (let s = subsetSum; s >= num; s--) {
            dp[s] += dp[s - num];
        }
    }

    return dp[subsetSum];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function findTargetSumWays($nums, $target) {
        $total = array_sum($nums);
        if (abs($target) > $total) {
            return 0;
        }
        $sumP = $target + $total;
        if ($sumP % 2 !== 0) {
            return 0;
        }
        $subset = intdiv($sumP, 2);
        $dp = array_fill(0, $subset + 1, 0);
        $dp[0] = 1;
        foreach ($nums as $num) {
            for ($s = $subset; $s >= $num; $s--) {
                $dp[$s] += $dp[$s - $num];
            }
        }
        return $dp[$subset];
    }
}
```

## Swift

```swift
class Solution {
    func findTargetSumWays(_ nums: [Int], _ target: Int) -> Int {
        let total = nums.reduce(0, +)
        if abs(target) > total { return 0 }
        let offset = total
        var dp = Array(repeating: 0, count: 2 * total + 1)
        
        // Initialize with the first number
        let first = nums[0]
        dp[first + offset] += 1
        dp[-first + offset] += 1
        
        if nums.count > 1 {
            for i in 1..<nums.count {
                var next = Array(repeating: 0, count: 2 * total + 1)
                let num = nums[i]
                for idx in 0..<(2 * total + 1) {
                    let cnt = dp[idx]
                    if cnt != 0 {
                        // Adding the current number
                        let plusIdx = idx + num
                        next[plusIdx] += cnt
                        // Subtracting the current number
                        let minusIdx = idx - num
                        next[minusIdx] += cnt
                    }
                }
                dp = next
            }
        }
        
        return dp[target + offset]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findTargetSumWays(nums: IntArray, target: Int): Int {
        val total = nums.sum()
        if (target > total || target < -total) return 0
        val diff = target + total
        if (diff % 2 != 0) return 0
        val subset = diff / 2
        val dp = IntArray(subset + 1)
        dp[0] = 1
        for (num in nums) {
            var s = subset
            while (s >= num) {
                dp[s] += dp[s - num]
                s--
            }
        }
        return dp[subset]
    }
}
```

## Dart

```dart
class Solution {
  int findTargetSumWays(List<int> nums, int target) {
    int total = nums.fold(0, (sum, n) => sum + n);
    if ((target).abs() > total) return 0;
    int sumPlus = target + total;
    if (sumPlus % 2 != 0) return 0;
    int subset = sumPlus ~/ 2;

    List<int> dp = List.filled(subset + 1, 0);
    dp[0] = 1;

    for (int num in nums) {
      for (int s = subset; s >= num; s--) {
        dp[s] += dp[s - num];
      }
    }

    return dp[subset];
  }
}
```

## Golang

```go
func findTargetSumWays(nums []int, target int) int {
    total := 0
    for _, v := range nums {
        total += v
    }
    // If target is out of possible sum range or (total+target) is odd, no solution.
    if abs(target) > total || (total+target)%2 != 0 {
        return 0
    }
    subsetSum := (total + target) / 2
    dp := make([]int, subsetSum+1)
    dp[0] = 1
    for _, num := range nums {
        for s := subsetSum; s >= num; s-- {
            dp[s] += dp[s-num]
        }
    }
    return dp[subsetSum]
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
# @param {Integer} target
# @return {Integer}
def find_target_sum_ways(nums, target)
  total = nums.sum
  return 0 if target.abs > total

  diff = total - target
  return 0 if diff < 0 || diff.odd?

  subset = diff / 2
  dp = Array.new(subset + 1, 0)
  dp[0] = 1

  nums.each do |num|
    (subset).downto(num) { |s| dp[s] += dp[s - num] }
  end

  dp[subset]
end
```

## Scala

```scala
object Solution {
    def findTargetSumWays(nums: Array[Int], target: Int): Int = {
        val total = nums.sum
        if ((total + target) % 2 != 0) return 0
        val subset = (total + target) / 2
        if (subset < 0) return 0
        val dp = new Array[Int](subset + 1)
        dp(0) = 1
        for (num <- nums) {
            var s = subset
            while (s >= num) {
                dp(s) += dp(s - num)
                s -= 1
            }
        }
        dp(subset)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        let total: i32 = nums.iter().sum();
        if target.abs() > total {
            return 0;
        }
        let sum_needed = target + total;
        if sum_needed % 2 != 0 {
            return 0;
        }
        let subset_sum = sum_needed / 2; // non‑negative
        let mut dp = vec![0i32; (subset_sum as usize) + 1];
        dp[0] = 1;
        for &num in nums.iter() {
            let n = num as usize;
            for s in (n..=subset_sum as usize).rev() {
                dp[s] += dp[s - n];
            }
        }
        dp[subset_sum as usize]
    }
}
```

## Racket

```racket
(define/contract (find-target-sum-ways nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((total (apply + nums))
         (offset total)
         (size (+ (* 2 total) 1)))
    (if (> (abs target) total)
        0
        (let loop ((idx 0)
                   (dp (let ((v (make-vector size 0)))
                         (vector-set! v offset 1)
                         v)))
          (if (= idx (length nums))
              (vector-ref dp (+ target offset))
              (let* ((num (list-ref nums idx))
                     (next (make-vector size 0)))
                (for ([s (in-range (- total) (+ total 1))])
                  (let ((cnt (vector-ref dp (+ s offset))))
                    (when (> cnt 0)
                      (let ((add-idx (+ s num offset))
                            (sub-idx (+ s (- num) offset)))
                        (vector-set! next add-idx (+ (vector-ref next add-idx) cnt))
                        (vector-set! next sub-idx (+ (vector-ref next sub-idx) cnt))))))
                (loop (+ idx 1) next)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_target_sum_ways/2]).

-spec find_target_sum_ways(Nums :: [integer()], Target :: integer()) -> integer().
find_target_sum_ways(Nums, Target) ->
    Total = lists:sum(Nums),
    case erlang:abs(Target) > Total of
        true -> 0;
        false ->
            Offset = Total,
            case Nums of
                [] ->
                    if Target == 0 -> 1 else 0 end;
                [First | Rest] ->
                    InitMap =
                        case First of
                            0 -> #{Offset => 2};
                            _ -> #{Offset + First => 1, Offset - First => 1}
                        end,
                    FinalMap = lists:foldl(
                        fun(N, Acc) ->
                            Next = maps:new(),
                            maps:fold(
                                fun(SumIdx, Count, M) ->
                                    PlusIdx = SumIdx + N,
                                    MinusIdx = SumIdx - N,
                                    M1 = maps:update_with(PlusIdx,
                                                          fun(V) -> V + Count end,
                                                          Count,
                                                          M),
                                    maps:update_with(MinusIdx,
                                                     fun(V) -> V + Count end,
                                                     Count,
                                                     M1)
                                end,
                                Next,
                                Acc)
                        end,
                        InitMap,
                        Rest),
                    maps:get(Target + Offset, FinalMap, 0)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_target_sum_ways(nums :: [integer], target :: integer) :: integer
  def find_target_sum_ways(nums, target) do
    total = Enum.sum(nums)

    if abs(target) > total do
      0
    else
      [first | rest] = nums

      dp_initial =
        %{}
        |> Map.update(first, 1, &(&1 + 1))
        |> Map.update(-first, 1, &(&1 + 1))

      final_dp =
        Enum.reduce(rest, dp_initial, fn num, acc ->
          Enum.reduce(acc, %{}, fn {sum, cnt}, new_acc ->
            s_add = sum + num
            s_sub = sum - num

            new_acc
            |> Map.update(s_add, cnt, &(&1 + cnt))
            |> Map.update(s_sub, cnt, &(&1 + cnt))
          end)
        end)

      Map.get(final_dp, target, 0)
    end
  end
end
```

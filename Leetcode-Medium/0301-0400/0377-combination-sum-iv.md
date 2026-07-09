# 0377. Combination Sum IV

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target + 1, 0);
        dp[0] = 1;
        sort(nums.begin(), nums.end());
        for (int t = 1; t <= target; ++t) {
            long long ways = 0;
            for (int num : nums) {
                if (num > t) break;
                ways += dp[t - num];
            }
            dp[t] = static_cast<int>(ways);
        }
        return dp[target];
    }
};
```

## Java

```java
class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        // Optional: sort to allow early break
        java.util.Arrays.sort(nums);
        for (int i = 1; i <= target; i++) {
            long sum = 0;
            for (int num : nums) {
                if (num > i) break;
                sum += dp[i - num];
            }
            dp[i] = (int) sum;
        }
        return dp[target];
    }
}
```

## Python

```python
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            total = 0
            for num in nums:
                if t >= num:
                    total += dp[t - num]
            dp[t] = total
        return dp[target]
```

## Python3

```python
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            total = 0
            for num in nums:
                if i >= num:
                    total += dp[i - num]
            dp[i] = total
        return dp[target]
```

## C

```c
#include <stdlib.h>

int combinationSum4(int* nums, int numsSize, int target) {
    int *dp = (int *)calloc(target + 1, sizeof(int));
    if (!dp) return 0;
    dp[0] = 1;
    for (int i = 1; i <= target; ++i) {
        long long cur = 0;
        for (int j = 0; j < numsSize; ++j) {
            if (i >= nums[j]) {
                cur += dp[i - nums[j]];
            }
        }
        dp[i] = (int)cur;
    }
    int result = dp[target];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int CombinationSum4(int[] nums, int target)
    {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int i = 1; i <= target; i++)
        {
            foreach (int num in nums)
            {
                if (num <= i)
                {
                    dp[i] += dp[i - num];
                }
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
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function(nums, target) {
    const dp = new Array(target + 1).fill(0);
    dp[0] = 1;
    for (let t = 1; t <= target; ++t) {
        let sum = 0;
        for (const num of nums) {
            if (t >= num) {
                sum += dp[t - num];
            }
        }
        dp[t] = sum;
    }
    return dp[target];
};
```

## Typescript

```typescript
function combinationSum4(nums: number[], target: number): number {
    const dp = new Array<number>(target + 1).fill(0);
    dp[0] = 1;
    // Optional sort to allow early break
    nums.sort((a, b) => a - b);
    for (let t = 1; t <= target; ++t) {
        let sum = 0;
        for (const num of nums) {
            if (num > t) break;
            sum += dp[t - num];
        }
        dp[t] = sum;
    }
    return dp[target];
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
    function combinationSum4($nums, $target) {
        $dp = array_fill(0, $target + 1, 0);
        $dp[0] = 1;
        for ($i = 1; $i <= $target; $i++) {
            foreach ($nums as $num) {
                if ($i >= $num) {
                    $dp[$i] += $dp[$i - $num];
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
    func combinationSum4(_ nums: [Int], _ target: Int) -> Int {
        var dp = Array(repeating: 0, count: target + 1)
        dp[0] = 1
        for i in 1...target {
            var sum = 0
            for num in nums where i >= num {
                sum += dp[i - num]
            }
            dp[i] = sum
        }
        return dp[target]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun combinationSum4(nums: IntArray, target: Int): Int {
        val dp = IntArray(target + 1)
        dp[0] = 1
        for (i in 1..target) {
            var ways = 0L
            for (num in nums) {
                if (i >= num) {
                    ways += dp[i - num]
                }
            }
            dp[i] = ways.toInt()
        }
        return dp[target]
    }
}
```

## Dart

```dart
class Solution {
  int combinationSum4(List<int> nums, int target) {
    List<int> dp = List.filled(target + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= target; ++i) {
      int count = 0;
      for (int num in nums) {
        if (num <= i) {
          count += dp[i - num];
        }
      }
      dp[i] = count;
    }
    return dp[target];
  }
}
```

## Golang

```go
func combinationSum4(nums []int, target int) int {
    dp := make([]int, target+1)
    dp[0] = 1
    for i := 1; i <= target; i++ {
        total := 0
        for _, num := range nums {
            if num <= i {
                total += dp[i-num]
            }
        }
        dp[i] = total
    }
    return dp[target]
}
```

## Ruby

```ruby
def combination_sum4(nums, target)
  dp = Array.new(target + 1, 0)
  dp[0] = 1
  (1..target).each do |t|
    nums.each do |num|
      dp[t] += dp[t - num] if num <= t
    end
  end
  dp[target]
end
```

## Scala

```scala
object Solution {
    def combinationSum4(nums: Array[Int], target: Int): Int = {
        val dp = new Array[Long](target + 1)
        dp(0) = 1L
        for (i <- 1 to target) {
            var total = 0L
            var idx = 0
            while (idx < nums.length) {
                val num = nums(idx)
                if (i >= num) total += dp(i - num)
                idx += 1
            }
            dp(i) = total
        }
        dp(target).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let t = target as usize;
        let mut dp = vec![0i64; t + 1];
        dp[0] = 1;
        for i in 1..=t {
            let mut count = 0i64;
            for &num in &nums {
                let n = num as usize;
                if n <= i {
                    count += dp[i - n];
                }
            }
            dp[i] = count;
        }
        dp[t] as i32
    }
}
```

## Racket

```racket
(define/contract (combination-sum4 nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((dp (make-vector (+ target 1) 0)))
    (vector-set! dp 0 1)
    (for ([i (in-range 1 (+ target 1))])
      (let ((cnt 0))
        (for ([num nums])
          (when (>= i num)
            (set! cnt (+ cnt (vector-ref dp (- i num))))))
        (vector-set! dp i cnt)))
    (vector-ref dp target)))
```

## Erlang

```erlang
-spec combination_sum4(Nums :: [integer()], Target :: integer()) -> integer().
combination_sum4(Nums, Target) ->
    DP0 = array:new(Target + 1, {default, 0}),
    DP1 = array:set(0, 1, DP0),
    DPFinal = fill_dp(lists:seq(1, Target), Nums, DP1),
    array:get(Target, DPFinal).

fill_dp([], _Nums, DP) -> DP;
fill_dp([T | Rest], Nums, DP) ->
    Sum = lists:foldl(
        fun(N, Acc) ->
            if
                N =< T -> Acc + array:get(T - N, DP);
                true   -> Acc
            end
        end,
        0,
        Nums),
    DP2 = array:set(T, Sum, DP),
    fill_dp(Rest, Nums, DP2).
```

## Elixir

```elixir
defmodule Solution do
  @spec combination_sum4(nums :: [integer], target :: integer) :: integer
  def combination_sum4(nums, target) do
    nums = Enum.sort(nums)
    dp = :array.new(target + 1, default: 0)
    dp = :array.set(0, 1, dp)

    dp =
      Enum.reduce(1..target, dp, fn i, acc ->
        sum =
          Enum.reduce(nums, 0, fn n, s ->
            if n <= i do
              s + :array.get(i - n, acc)
            else
              s
            end
          end)

        :array.set(i, sum, acc)
      end)

    :array.get(target, dp)
  end
end
```

# 2915. Length of the Longest Subsequence That Sums to Target

## Cpp

```cpp
class Solution {
public:
    int lengthOfLongestSubsequence(vector<int>& nums, int target) {
        const int NEG = -1e9;
        vector<int> dp(target + 1, NEG);
        dp[0] = 0; // empty subsequence has sum 0 and length 0
        for (int num : nums) {
            if (num > target) continue;
            for (int j = target; j >= num; --j) {
                if (dp[j - num] != NEG) {
                    dp[j] = max(dp[j], dp[j - num] + 1);
                }
            }
        }
        return dp[target] == NEG ? -1 : dp[target];
    }
};
```

## Java

```java
class Solution {
    public int lengthOfLongestSubsequence(java.util.List<Integer> nums, int target) {
        int[] dp = new int[target + 1];
        java.util.Arrays.fill(dp, -1);
        dp[0] = 0; // sum 0 achievable with length 0
        
        for (int num : nums) {
            if (num > target) continue;
            for (int j = target; j >= num; --j) {
                if (dp[j - num] != -1) {
                    dp[j] = Math.max(dp[j], dp[j - num] + 1);
                }
            }
        }
        
        return dp[target];
    }
}
```

## Python

```python
class Solution(object):
    def lengthOfLongestSubsequence(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        INF_NEG = -10**9
        dp = [INF_NEG] * (target + 1)
        dp[0] = 0  # empty subsequence has sum 0 and length 0

        for num in nums:
            if num > target:
                continue
            for s in range(target, num - 1, -1):
                if dp[s - num] != INF_NEG:
                    dp[s] = max(dp[s], dp[s - num] + 1)

        return dp[target] if dp[target] > 0 else -1
```

## Python3

```python
from typing import List

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        dp[0] = 0
        for num in nums:
            if num > target:
                continue
            for s in range(target, num - 1, -1):
                if dp[s - num] != -1:
                    cand = dp[s - num] + 1
                    if cand > dp[s]:
                        dp[s] = cand
        return dp[target] if dp[target] != -1 else -1
```

## C

```c
int lengthOfLongestSubsequence(int* nums, int numsSize, int target) {
    const int NEG = -1000000000;
    int *dp = (int *)malloc((target + 1) * sizeof(int));
    if (!dp) return -1; // allocation failure fallback
    for (int i = 0; i <= target; ++i) dp[i] = NEG;
    dp[0] = 0; // sum 0 with length 0

    for (int idx = 0; idx < numsSize; ++idx) {
        int val = nums[idx];
        if (val > target) continue;
        for (int s = target; s >= val; --s) {
            if (dp[s - val] != NEG) {
                int cand = dp[s - val] + 1;
                if (cand > dp[s]) dp[s] = cand;
            }
        }
    }

    int ans = dp[target];
    free(dp);
    return (ans == NEG) ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LengthOfLongestSubsequence(IList<int> nums, int target) {
        const int NEG = -1000000;
        int[] dp = new int[target + 1];
        for (int i = 0; i <= target; i++) dp[i] = NEG;
        dp[0] = 0;
        foreach (int num in nums) {
            if (num > target) continue;
            for (int j = target; j >= num; j--) {
                if (dp[j - num] != NEG) {
                    int cand = dp[j - num] + 1;
                    if (cand > dp[j]) dp[j] = cand;
                }
            }
        }
        return dp[target] < 0 ? -1 : dp[target];
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
var lengthOfLongestSubsequence = function(nums, target) {
    const dp = new Array(target + 1).fill(-1);
    dp[0] = 0; // empty subsequence has sum 0 and length 0
    
    for (const num of nums) {
        for (let s = target; s >= num; --s) {
            if (dp[s - num] !== -1) {
                dp[s] = Math.max(dp[s], dp[s - num] + 1);
            }
        }
    }
    
    return dp[target];
};
```

## Typescript

```typescript
function lengthOfLongestSubsequence(nums: number[], target: number): number {
    const dp = new Array(target + 1).fill(-1);
    dp[0] = 0;
    for (const num of nums) {
        for (let sum = target; sum >= num; --sum) {
            if (dp[sum - num] !== -1) {
                dp[sum] = Math.max(dp[sum], dp[sum - num] + 1);
            }
        }
    }
    return dp[target] === -1 ? -1 : dp[target];
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
    function lengthOfLongestSubsequence($nums, $target) {
        $dp = array_fill(0, $target + 1, -1);
        $dp[0] = 0;
        foreach ($nums as $num) {
            for ($j = $target; $j >= $num; --$j) {
                if ($dp[$j - $num] != -1) {
                    $cand = $dp[$j - $num] + 1;
                    if ($cand > $dp[$j]) {
                        $dp[$j] = $cand;
                    }
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
    func lengthOfLongestSubsequence(_ nums: [Int], _ target: Int) -> Int {
        let NEG = -1_000_000
        var dp = Array(repeating: NEG, count: target + 1)
        dp[0] = 0
        for num in nums {
            if num > target { continue }
            var j = target
            while j >= num {
                if dp[j - num] != NEG {
                    let cand = dp[j - num] + 1
                    if cand > dp[j] {
                        dp[j] = cand
                    }
                }
                j -= 1
            }
        }
        return dp[target] < 0 ? -1 : dp[target]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lengthOfLongestSubsequence(nums: List<Int>, target: Int): Int {
        val dp = IntArray(target + 1) { -1 }
        dp[0] = 0
        for (num in nums) {
            if (num > target) continue
            for (j in target downTo num) {
                if (dp[j - num] != -1) {
                    dp[j] = maxOf(dp[j], dp[j - num] + 1)
                }
            }
        }
        return if (dp[target] == -1) -1 else dp[target]
    }
}
```

## Dart

```dart
class Solution {
  int lengthOfLongestSubsequence(List<int> nums, int target) {
    const int NEG = -1000000;
    List<int> dp = List.filled(target + 1, NEG);
    dp[0] = 0;
    for (int num in nums) {
      for (int j = target; j >= num; --j) {
        if (dp[j - num] != NEG) {
          int cand = dp[j - num] + 1;
          if (cand > dp[j]) dp[j] = cand;
        }
      }
    }
    return dp[target] < 0 ? -1 : dp[target];
  }
}
```

## Golang

```go
func lengthOfLongestSubsequence(nums []int, target int) int {
    const unreachable = -1
    dp := make([]int, target+1)
    for i := range dp {
        dp[i] = unreachable
    }
    dp[0] = 0

    for _, v := range nums {
        for s := target; s >= v; s-- {
            if dp[s-v] != unreachable {
                cand := dp[s-v] + 1
                if cand > dp[s] {
                    dp[s] = cand
                }
            }
        }
    }

    if dp[target] == unreachable {
        return -1
    }
    return dp[target]
}
```

## Ruby

```ruby
def length_of_longest_subsequence(nums, target)
  dp = Array.new(target + 1, -1)
  dp[0] = 0
  nums.each do |num|
    target.downto(num) do |s|
      if dp[s - num] != -1
        cand = dp[s - num] + 1
        dp[s] = cand if cand > dp[s]
      end
    end
  end
  dp[target] == -1 ? -1 : dp[target]
end
```

## Scala

```scala
object Solution {
    def lengthOfLongestSubsequence(nums: List[Int], target: Int): Int = {
        val dp = Array.fill(target + 1)(-1)
        dp(0) = 0
        for (num <- nums) {
            var j = target
            while (j >= num) {
                if (dp(j - num) != -1) {
                    val cand = dp(j - num) + 1
                    if (cand > dp(j)) dp(j) = cand
                }
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
    pub fn length_of_longest_subsequence(nums: Vec<i32>, target: i32) -> i32 {
        let t = target as usize;
        let mut dp = vec![-1i32; t + 1];
        dp[0] = 0;
        for &val in nums.iter() {
            let v = val as usize;
            if v > t { continue; }
            for sum in (v..=t).rev() {
                if dp[sum - v] != -1 {
                    let cand = dp[sum - v] + 1;
                    if cand > dp[sum] {
                        dp[sum] = cand;
                    }
                }
            }
        }
        if dp[t] <= 0 { -1 } else { dp[t] }
    }
}
```

## Racket

```racket
(define/contract (length-of-longest-subsequence nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((dp (make-vector (+ target 1) -1)))
    (vector-set! dp 0 0)
    (for ([num nums])
      (when (<= num target)
        (for ([j (in-range target (- num 1) -1)])
          (let ((prev (vector-ref dp (- j num))))
            (when (>= prev 0)
              (define cand (+ prev 1))
              (when (> cand (vector-ref dp j))
                (vector-set! dp j cand)))))))
    (let ((ans (vector-ref dp target)))
      (if (= ans -1) -1 ans))))
```

## Erlang

```erlang
-spec length_of_longest_subsequence([integer()], integer()) -> integer().
length_of_longest_subsequence(Nums, Target) ->
    DP0 = #{0 => 0},
    FinalDP = process(Nums, Target, DP0),
    maps:get(Target, FinalDP, -1).

process([], _Target, DP) -> DP;
process([Num|Rest], Target, DP) ->
    NewDP = maps:fold(
        fun(Sum, Len, Acc) ->
            NewSum = Sum + Num,
            if
                NewSum =< Target ->
                    NewLen = Len + 1,
                    case maps:get(NewSum, Acc, -1) of
                        Prev when Prev >= NewLen -> Acc;
                        _ -> maps:put(NewSum, NewLen, Acc)
                    end;
                true -> Acc
            end
        end,
        DP,
        DP),
    process(Rest, Target, NewDP).
```

## Elixir

```elixir
defmodule Solution do
  @spec length_of_longest_subsequence(nums :: [integer], target :: integer) :: integer
  def length_of_longest_subsequence(nums, target) do
    # Initialize DP array with -1 (unreachable), dp[0] = 0 (empty subsequence)
    dp = :array.new(target + 1, default: -1)
    dp = :array.set(0, 0, dp)

    final_dp =
      Enum.reduce(nums, dp, fn num, acc ->
        # iterate sums from target down to num
        Enum.reduce(Enum.to_list(num..target) |> Enum.reverse(), acc, fn sum, a ->
          prev_len = :array.get(sum - num, a)
          if prev_len != -1 do
            cand = prev_len + 1
            cur = :array.get(sum, a)
            new_val = if cand > cur, do: cand, else: cur
            :array.set(sum, new_val, a)
          else
            a
          end
        end)
      end)

    case :array.get(target, final_dp) do
      -1 -> -1
      val -> val
    end
  end
end
```

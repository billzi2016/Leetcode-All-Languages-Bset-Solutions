# 1262. Greatest Sum Divisible by Three

## Cpp

```cpp
class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        const int INF_NEG = -1e9;
        vector<int> dp(3, INF_NEG);
        dp[0] = 0;
        for (int num : nums) {
            vector<int> ndp = dp;
            int mod = num % 3;
            for (int i = 0; i < 3; ++i) {
                if (dp[i] != INF_NEG) {
                    int newMod = (i + mod) % 3;
                    ndp[newMod] = max(ndp[newMod], dp[i] + num);
                }
            }
            dp.swap(ndp);
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public int maxSumDivThree(int[] nums) {
        int[] dp = new int[]{0, Integer.MIN_VALUE, Integer.MIN_VALUE};
        for (int num : nums) {
            int[] ndp = dp.clone();
            for (int r = 0; r < 3; ++r) {
                if (dp[r] != Integer.MIN_VALUE) {
                    int nr = (r + num) % 3;
                    ndp[nr] = Math.max(ndp[nr], dp[r] + num);
                }
            }
            dp = ndp;
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            ndp = dp[:]
            for r in range(3):
                if dp[r] != float('-inf'):
                    new_sum = dp[r] + num
                    new_mod = (r + num) % 3
                    if new_sum > ndp[new_mod]:
                        ndp[new_mod] = new_sum
            dp = ndp
        return dp[0]
```

## Python3

```python
from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -10**9, -10**9]  # dp[mod] = max sum with remainder mod
        for num in nums:
            ndp = dp[:]
            for r in range(3):
                new_mod = (r + num) % 3
                ndp[new_mod] = max(ndp[new_mod], dp[r] + num)
            dp = ndp
        return dp[0]
```

## C

```c
int maxSumDivThree(int* nums, int numsSize) {
    const int NEG = -1000000000;
    int dp[3] = {0, NEG, NEG};
    for (int i = 0; i < numsSize; ++i) {
        int ndp[3] = {dp[0], dp[1], dp[2]};
        int num = nums[i];
        for (int mod = 0; mod < 3; ++mod) {
            if (dp[mod] == NEG) continue;
            int newMod = (mod + num) % 3;
            int cand = dp[mod] + num;
            if (cand > ndp[newMod]) ndp[newMod] = cand;
        }
        dp[0] = ndp[0];
        dp[1] = ndp[1];
        dp[2] = ndp[2];
    }
    return dp[0];
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxSumDivThree(int[] nums)
    {
        const int INF_NEG = -1000000000;
        int[] dp = new int[3] { 0, INF_NEG, INF_NEG };
        foreach (int num in nums)
        {
            int[] ndp = new int[3];
            Array.Copy(dp, ndp, 3);
            for (int r = 0; r < 3; r++)
            {
                if (dp[r] == INF_NEG) continue;
                int nr = (r + num) % 3;
                ndp[nr] = Math.Max(ndp[nr], dp[r] + num);
            }
            dp = ndp;
        }
        return dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumDivThree = function(nums) {
    const dp = [0, -Infinity, -Infinity];
    for (const num of nums) {
        const next = dp.slice();
        for (let i = 0; i < 3; i++) {
            if (dp[i] !== -Infinity) {
                const sum = dp[i] + num;
                const mod = sum % 3;
                if (sum > next[mod]) next[mod] = sum;
            }
        }
        dp[0] = next[0];
        dp[1] = next[1];
        dp[2] = next[2];
    }
    return dp[0];
};
```

## Typescript

```typescript
function maxSumDivThree(nums: number[]): number {
    const dp: number[] = [0, Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY];
    for (const x of nums) {
        const ndp = dp.slice();
        for (let r = 0; r < 3; ++r) {
            if (dp[r] !== Number.NEGATIVE_INFINITY) {
                const nr = (r + x) % 3;
                ndp[nr] = Math.max(ndp[nr], dp[r] + x);
            }
        }
        dp[0] = ndp[0];
        dp[1] = ndp[1];
        dp[2] = ndp[2];
    }
    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumDivThree($nums) {
        $negInf = -PHP_INT_MAX;
        $dp = [0, $negInf, $negInf];
        foreach ($nums as $num) {
            $mod = $num % 3;
            $new = $dp;
            for ($i = 0; $i < 3; $i++) {
                if ($dp[$i] == $negInf) continue;
                $candidate = $dp[$i] + $num;
                $idx = ($i + $mod) % 3;
                if ($candidate > $new[$idx]) {
                    $new[$idx] = $candidate;
                }
            }
            $dp = $new;
        }
        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func maxSumDivThree(_ nums: [Int]) -> Int {
        let NEG = -1_000_000_000
        var dp = [0, NEG, NEG]  // dp[mod] = max sum with remainder mod
        
        for num in nums {
            var ndp = dp
            let mod = num % 3
            for r in 0..<3 {
                if dp[r] != NEG {
                    let newMod = (r + mod) % 3
                    ndp[newMod] = max(ndp[newMod], dp[r] + num)
                }
            }
            dp = ndp
        }
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSumDivThree(nums: IntArray): Int {
        val INF = -1_000_000_000
        val dp = IntArray(3) { INF }
        dp[0] = 0
        for (num in nums) {
            val prev = dp.clone()
            val mod = num % 3
            for (i in 0..2) {
                if (prev[i] != INF) {
                    val newMod = (i + mod) % 3
                    dp[newMod] = kotlin.math.max(dp[newMod], prev[i] + num)
                }
            }
        }
        return dp[0]
    }
}
```

## Dart

```dart
class Solution {
  int maxSumDivThree(List<int> nums) {
    const int NEG_INF = -1000000000;
    List<int> dp = [0, NEG_INF, NEG_INF];
    for (int num in nums) {
      List<int> ndp = List.from(dp);
      for (int i = 0; i < 3; ++i) {
        if (dp[i] != NEG_INF) {
          int newMod = (i + num) % 3;
          int candidate = dp[i] + num;
          if (candidate > ndp[newMod]) ndp[newMod] = candidate;
        }
      }
      dp = ndp;
    }
    return dp[0];
  }
}
```

## Golang

```go
func maxSumDivThree(nums []int) int {
	const INF = int(-1 << 60)
	dp := [3]int{0, INF, INF}
	for _, v := range nums {
		ndp := dp
		for r := 0; r < 3; r++ {
			if dp[r] == INF {
				continue
			}
			nr := (r + v) % 3
			sum := dp[r] + v
			if sum > ndp[nr] {
				ndp[nr] = sum
			}
		}
		dp = ndp
	}
	return dp[0]
}
```

## Ruby

```ruby
def max_sum_div_three(nums)
  neg_inf = -1 << 60
  dp = [0, neg_inf, neg_inf]
  nums.each do |num|
    ndp = dp.clone
    3.times do |r|
      sum = dp[r] + num
      nr = (r + num) % 3
      ndp[nr] = sum if sum > ndp[nr]
    end
    dp = ndp
  end
  dp[0]
end
```

## Scala

```scala
object Solution {
    def maxSumDivThree(nums: Array[Int]): Int = {
        val NEG = -1000000000
        val dp = Array(0, NEG, NEG)
        for (num <- nums) {
            val cur = dp.clone()
            val r = num % 3
            for (i <- 0 until 3) {
                val newMod = (i + r) % 3
                dp(newMod) = math.max(dp(newMod), cur(i) + num)
            }
        }
        dp(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {
        const NEG: i32 = -1_000_000_000;
        let mut dp = [0i32, NEG, NEG];
        for &num in nums.iter() {
            let mod_num = (num % 3) as usize;
            let prev = dp;
            let mut ndp = dp;
            for r in 0..3 {
                if prev[r] != NEG {
                    let nr = (r + mod_num) % 3;
                    ndp[nr] = ndp[nr].max(prev[r] + num);
                }
            }
            dp = ndp;
        }
        dp[0]
    }
}
```

## Racket

```racket
(define/contract (max-sum-div-three nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((neg -1000000000000)               ; sentinel for impossible states
         (dp (vector 0 neg neg)))          ; dp[mod] = max sum with given remainder
    (for ([x nums])
      (let* ((rem (modulo x 3))
             (new-dp (vector-copy dp)))
        (for ([r (in-range 3)])
          (define cur (vector-ref dp r))
          (when (> cur neg)                 ; reachable state
            (define nr (modulo (+ r rem) 3))
            (define cand (+ cur x))
            (when (> cand (vector-ref new-dp nr))
              (vector-set! new-dp nr cand))))
        (set! dp new-dp)))
    (max 0 (vector-ref dp 0))))
```

## Erlang

```erlang
-spec max_sum_div_three(Nums :: [integer()]) -> integer().
max_sum_div_three(Nums) ->
    Inf = 1 bsl 30,
    Init = #{sum => 0,
             min1_1 => Inf,
             min2_1 => Inf,
             min1_2 => Inf,
             min2_2 => Inf},
    Final = lists:foldl(fun(Num, Acc) ->
        Rem = Num rem 3,
        Sum1 = maps:get(sum, Acc) + Num,
        Acc1 = Acc#{sum => Sum1},
        case Rem of
            0 -> Acc1;
            1 ->
                Min1 = maps:get(min1_1, Acc1),
                Min2 = maps:get(min2_1, Acc1),
                if Num < Min1 ->
                        Acc1#{min1_1 => Num, min2_1 => Min1};
                   Num < Min2 ->
                        Acc1#{min2_1 => Num};
                   true -> Acc1
                end;
            2 ->
                Min1 = maps:get(min1_2, Acc1),
                Min2 = maps:get(min2_2, Acc1),
                if Num < Min1 ->
                        Acc1#{min1_2 => Num, min2_2 => Min1};
                   Num < Min2 ->
                        Acc1#{min2_2 => Num};
                   true -> Acc1
                end
        end
    end, Init, Nums),

    Sum = maps:get(sum, Final),
    case Sum rem 3 of
        0 -> Sum;
        1 ->
            MinMod1 = maps:get(min1_1, Final),
            OptionA = if MinMod1 < Inf -> MinMod1; true -> Inf end,
            Min2a = maps:get(min1_2, Final),
            Min2b = maps:get(min2_2, Final),
            OptionB = if (Min2a < Inf) andalso (Min2b < Inf) -> Min2a + Min2b; true -> Inf end,
            Removal = min(OptionA, OptionB),
            if Removal < Inf -> Sum - Removal; true -> 0 end;
        2 ->
            MinMod2 = maps:get(min1_2, Final),
            OptionA = if MinMod2 < Inf -> MinMod2; true -> Inf end,
            Min2a = maps:get(min1_1, Final),
            Min2b = maps:get(min2_1, Final),
            OptionB = if (Min2a < Inf) andalso (Min2b < Inf) -> Min2a + Min2b; true -> Inf end,
            Removal = min(OptionA, OptionB),
            if Removal < Inf -> Sum - Removal; true -> 0 end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_div_three(nums :: [integer]) :: integer
  def max_sum_div_three(nums) do
    init_dp = [0, -1_000_000_000, -1_000_000_000]

    final_dp =
      Enum.reduce(nums, init_dp, fn num, dp ->
        Enum.with_index(dp)
        |> Enum.reduce(dp, fn {val, _idx}, acc ->
          if val < 0 do
            acc
          else
            new_sum = val + num
            mod = rem(new_sum, 3)

            List.update_at(acc, mod, fn existing -> max(existing, new_sum) end)
          end
        end)
      end)

    Enum.at(final_dp, 0)
  end
end
```

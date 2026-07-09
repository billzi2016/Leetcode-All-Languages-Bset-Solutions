# 2770. Maximum Number of Jumps to Reach the Last Index

## Cpp

```cpp
class Solution {
public:
    int maximumJumps(vector<int>& nums, int target) {
        int n = nums.size();
        const int INF_NEG = -1e9;
        vector<int> dp(n, INF_NEG);
        dp[0] = 0;
        for (int j = 1; j < n; ++j) {
            for (int i = 0; i < j; ++i) {
                long long diff = (long long)nums[j] - (long long)nums[i];
                if (diff >= -target && diff <= target && dp[i] != INF_NEG) {
                    dp[j] = max(dp[j], dp[i] + 1);
                }
            }
        }
        return dp[n-1] < 0 ? -1 : dp[n-1];
    }
};
```

## Java

```java
class Solution {
    public int maximumJumps(int[] nums, int target) {
        int n = nums.length;
        int[] dp = new int[n];
        java.util.Arrays.fill(dp, -1);
        dp[0] = 0;
        long t = target;
        for (int j = 1; j < n; ++j) {
            for (int i = 0; i < j; ++i) {
                if (dp[i] == -1) continue;
                long diff = (long) nums[j] - (long) nums[i];
                if (-t <= diff && diff <= t) {
                    dp[j] = Math.max(dp[j], dp[i] + 1);
                }
            }
        }
        return dp[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        INF_NEG = -10**9
        dp = [INF_NEG] * n
        dp[0] = 0  # start at index 0 with zero jumps
        
        for j in range(1, n):
            best = INF_NEG
            for i in range(j):
                if abs(nums[j] - nums[i]) <= target and dp[i] != INF_NEG:
                    if dp[i] + 1 > best:
                        best = dp[i] + 1
            dp[j] = best
        
        return dp[-1] if dp[-1] != INF_NEG else -1
```

## Python3

```python
from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0  # start at index 0 with zero jumps
        
        for j in range(1, n):
            best = -1
            for i in range(j):
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                    cand = dp[i] + 1
                    if cand > best:
                        best = cand
            dp[j] = best
        
        return dp[-1]
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int maximumJumps(int* nums, int numsSize, int target) {
    if (numsSize == 0) return -1;
    int *dp = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) dp[i] = INT_MIN;
    dp[0] = 0;

    long long t = target; // promote to avoid overflow in comparisons
    for (int j = 1; j < numsSize; ++j) {
        for (int i = 0; i < j; ++i) {
            if (dp[i] == INT_MIN) continue;
            long long diff = (long long)nums[j] - (long long)nums[i];
            if (diff >= -t && diff <= t) {
                if (dp[i] + 1 > dp[j]) dp[j] = dp[i] + 1;
            }
        }
    }

    int ans = dp[numsSize - 1];
    free(dp);
    return (ans == INT_MIN) ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumJumps(int[] nums, int target) {
        int n = nums.Length;
        const int UNREACHABLE = -1;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) dp[i] = UNREACHABLE;
        dp[0] = 0;
        long t = target; // use long to avoid overflow
        for (int i = 0; i < n; i++) {
            if (dp[i] == UNREACHABLE) continue;
            for (int j = i + 1; j < n; j++) {
                long diff = (long)nums[j] - nums[i];
                if (diff >= -t && diff <= t) {
                    dp[j] = Math.Max(dp[j], dp[i] + 1);
                }
            }
        }
        return dp[n - 1];
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
var maximumJumps = function(nums, target) {
    const n = nums.length;
    const dp = new Array(n).fill(Number.NEGATIVE_INFINITY);
    dp[0] = 0; // zero jumps to stay at start
    
    for (let j = 1; j < n; ++j) {
        let best = Number.NEGATIVE_INFINITY;
        for (let i = 0; i < j; ++i) {
            if (dp[i] !== Number.NEGATIVE_INFINITY && Math.abs(nums[j] - nums[i]) <= target) {
                const cand = dp[i] + 1;
                if (cand > best) best = cand;
            }
        }
        dp[j] = best;
    }
    
    return dp[n - 1] === Number.NEGATIVE_INFINITY ? -1 : dp[n - 1];
};
```

## Typescript

```typescript
function maximumJumps(nums: number[], target: number): number {
    const n = nums.length;
    const dp = new Array<number>(n).fill(-1);
    dp[0] = 0;
    for (let j = 1; j < n; ++j) {
        let best = -1;
        for (let i = 0; i < j; ++i) {
            if (dp[i] !== -1 && Math.abs(nums[j] - nums[i]) <= target) {
                const cand = dp[i] + 1;
                if (cand > best) best = cand;
            }
        }
        dp[j] = best;
    }
    return dp[n - 1];
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
    function maximumJumps($nums, $target) {
        $n = count($nums);
        $dp = array_fill(0, $n, -1);
        $dp[0] = 0;
        for ($j = 1; $j < $n; ++$j) {
            $best = -1;
            for ($i = 0; $i < $j; ++$i) {
                if ($dp[$i] != -1 && abs($nums[$j] - $nums[$i]) <= $target) {
                    $cand = $dp[$i] + 1;
                    if ($cand > $best) {
                        $best = $cand;
                    }
                }
            }
            $dp[$j] = $best;
        }
        return $dp[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maximumJumps(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var dp = Array(repeating: -1, count: n)
        dp[0] = 0
        for j in 1..<n {
            for i in 0..<j {
                if dp[i] != -1 && abs(nums[j] - nums[i]) <= target {
                    dp[j] = max(dp[j], dp[i] + 1)
                }
            }
        }
        return dp[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumJumps(nums: IntArray, target: Int): Int {
        val n = nums.size
        val dp = IntArray(n) { -1 }
        dp[0] = 0
        for (j in 1 until n) {
            var best = -1
            for (i in 0 until j) {
                if (dp[i] != -1 && kotlin.math.abs(nums[j] - nums[i]) <= target) {
                    val cand = dp[i] + 1
                    if (cand > best) best = cand
                }
            }
            dp[j] = best
        }
        return dp[n - 1]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maximumJumps(List<int> nums, int target) {
    int n = nums.length;
    List<int> dp = List.filled(n, -1);
    dp[0] = 0;
    for (int j = 1; j < n; ++j) {
      for (int i = 0; i < j; ++i) {
        if ((nums[j] - nums[i]).abs() <= target && dp[i] != -1) {
          dp[j] = max(dp[j], dp[i] + 1);
        }
      }
    }
    return dp[n - 1];
  }
}
```

## Golang

```go
func maximumJumps(nums []int, target int) int {
    n := len(nums)
    dp := make([]int, n)
    for i := range dp {
        dp[i] = -1
    }
    dp[0] = 0

    for j := 1; j < n; j++ {
        for i := 0; i < j; i++ {
            if dp[i] == -1 {
                continue
            }
            diff := nums[j] - nums[i]
            if diff < -target || diff > target {
                continue
            }
            if dp[i]+1 > dp[j] {
                dp[j] = dp[i] + 1
            }
        }
    }

    if dp[n-1] == -1 {
        return -1
    }
    return dp[n-1]
}
```

## Ruby

```ruby
def maximum_jumps(nums, target)
  n = nums.length
  dp = Array.new(n, -1)
  dp[0] = 0

  (1...n).each do |j|
    (0...j).each do |i|
      next if dp[i] == -1
      diff = nums[j] - nums[i]
      if diff <= target && diff >= -target
        dp[j] = [dp[j], dp[i] + 1].max
      end
    end
  end

  dp[n - 1]
end
```

## Scala

```scala
object Solution {
    def maximumJumps(nums: Array[Int], target: Int): Int = {
        val n = nums.length
        val dp = Array.fill(n)(Int.MinValue)
        dp(0) = 0
        for (j <- 1 until n) {
            var best = Int.MinValue
            var i = 0
            while (i < j) {
                if (dp(i) != Int.MinValue && math.abs(nums(j).toLong - nums(i).toLong) <= target.toLong) {
                    val cand = dp(i) + 1
                    if (cand > best) best = cand
                }
                i += 1
            }
            dp(j) = best
        }
        if (dp(n - 1) < 0) -1 else dp(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_jumps(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        const NEG: i32 = -1_000_000_000;
        let mut dp = vec![NEG; n];
        dp[0] = 0;
        let t = target as i64;
        for j in 1..n {
            for i in 0..j {
                if dp[i] != NEG {
                    let diff = nums[j] as i64 - nums[i] as i64;
                    if -t <= diff && diff <= t {
                        dp[j] = dp[j].max(dp[i] + 1);
                    }
                }
            }
        }
        if dp[n - 1] < 0 { -1 } else { dp[n - 1] }
    }
}
```

## Racket

```racket
(define/contract (maximum-jumps nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (dp (make-vector n -10000))) ; sentinel for unreachable
    (vector-set! dp 0 0)
    (for ([j (in-range 1 n)])
      (for ([i (in-range 0 j)])
        (let ((diff (- (vector-ref arr j) (vector-ref arr i))))
          (when (and (<= (abs diff) target)
                     (> (vector-ref dp i) -10000))
            (let ((cand (+ 1 (vector-ref dp i))))
              (when (> cand (vector-ref dp j))
                (vector-set! dp j cand)))))))
    (let ((ans (vector-ref dp (- n 1))))
      (if (< ans 0) -1 ans))))
```

## Erlang

```erlang
-spec maximum_jumps(Nums :: [integer()], Target :: integer()) -> integer().
maximum_jumps(Nums, Target) ->
    N = length(Nums),
    DP0 = erlang:make_tuple(N, -1),
    DP1 = setelement(1, DP0, 0),               % start at index 0 with 0 jumps
    DPFinal = compute_dp(2, N, Nums, Target, DP1),
    element(N, DPFinal).

%% iterate over positions j from Cur to N, updating DP tuple
-spec compute_dp(integer(), integer(), [integer()], integer(), tuple()) -> tuple().
compute_dp(CurJ, N, _Nums, _Target, DP) when CurJ > N ->
    DP;
compute_dp(CurJ, N, Nums, Target, DP) ->
    NumJ = lists:nth(CurJ, Nums),
    MaxPrev = find_best(1, CurJ - 1, Nums, Target, NumJ, DP, -1),
    NewDP = case MaxPrev of
        -1 -> DP;                               % unreachable, keep -1
        _  -> setelement(CurJ, DP, MaxPrev)
    end,
    compute_dp(CurJ + 1, N, Nums, Target, NewDP).

%% find the best dp[i] + 1 for i in [CurI, End] satisfying jump condition
-spec find_best(integer(), integer(), [integer()], integer(), integer(), tuple(), integer()) -> integer().
find_best(CurI, End, _Nums, _Target, _NumJ, _DP, Best) when CurI > End ->
    Best;
find_best(CurI, End, Nums, Target, NumJ, DP, Best) ->
    Di = element(CurI, DP),
    case Di of
        -1 ->                                   % cannot reach i
            find_best(CurI + 1, End, Nums, Target, NumJ, DP, Best);
        _ ->
            NumI = lists:nth(CurI, Nums),
            Diff = NumJ - NumI,
            if
                Diff >= -Target, Diff =< Target ->
                    NewBest = erlang:max(Best, Di + 1),
                    find_best(CurI + 1, End, Nums, Target, NumJ, DP, NewBest);
                true ->
                    find_best(CurI + 1, End, Nums, Target, NumJ, DP, Best)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_jumps(nums :: [integer], target :: integer) :: integer
  def maximum_jumps(nums, target) do
    n = length(nums)
    arr = List.to_tuple(nums)

    # dp array initialized with -1 (unreachable), except dp[0] = 0
    dp =
      :array.new(n, default: -1)
      |> :array.set(0, 0)

    dp =
      Enum.reduce(1..(n - 1), dp, fn j, acc_dp ->
        max_jump =
          Enum.reduce(0..(j - 1), -1, fn i, cur_max ->
            diff = elem(arr, j) - elem(arr, i)

            if diff >= -target and diff <= target do
              prev = :array.get(i, acc_dp)

              if prev != -1 do
                cand = prev + 1
                if cand > cur_max, do: cand, else: cur_max
              else
                cur_max
              end
            else
              cur_max
            end
          end)

        if max_jump != -1 do
          :array.set(j, max_jump, acc_dp)
        else
          acc_dp
        end
      end)

    result = :array.get(n - 1, dp)
    if result == -1, do: -1, else: result
  end
end
```

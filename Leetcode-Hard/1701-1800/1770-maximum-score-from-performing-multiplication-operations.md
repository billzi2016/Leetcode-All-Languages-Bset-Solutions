# 1770. Maximum Score from Performing Multiplication Operations

## Cpp

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int n = nums.size();
        int m = multipliers.size();
        const long long NEG_INF = LLONG_MIN / 4;
        vector<long long> dp(m + 1, NEG_INF);
        dp[0] = 0;
        for (int i = 1; i <= m; ++i) {
            vector<long long> ndp(i + 1, NEG_INF);
            for (int l = 0; l <= i; ++l) {
                // take from start
                if (l > 0 && dp[l - 1] != NEG_INF) {
                    long long val = dp[l - 1] + (long long)nums[l - 1] * multipliers[i - 1];
                    ndp[l] = max(ndp[l], val);
                }
                // take from end
                if (l <= i - 1 && dp[l] != NEG_INF) {
                    int rIdx = n - (i - l);
                    long long val = dp[l] + (long long)nums[rIdx] * multipliers[i - 1];
                    ndp[l] = max(ndp[l], val);
                }
            }
            dp.swap(ndp);
        }
        long long ans = NEG_INF;
        for (int l = 0; l <= m; ++l) ans = max(ans, dp[l]);
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        int n = nums.length;
        int m = multipliers.length;
        long[][] dp = new long[m + 1][m + 1];
        for (int i = m - 1; i >= 0; --i) {
            for (int left = i; left >= 0; --left) {
                int rightIdx = n - 1 - (i - left);
                long takeLeft = (long) multipliers[i] * nums[left] + dp[i + 1][left + 1];
                long takeRight = (long) multipliers[i] * nums[rightIdx] + dp[i + 1][left];
                dp[i][left] = Math.max(takeLeft, takeRight);
            }
        }
        return (int) dp[0][0];
    }
}
```

## Python

```python
class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(multipliers)
        # dp[i][left] = max score after performing operations i..m-1,
        # having taken 'left' elements from the start so far.
        dp = [[float('-inf')] * (m + 1) for _ in range(m + 1)]
        for left in range(m + 1):
            dp[m][left] = 0  # base case: no operations left

        for i in range(m - 1, -1, -1):
            mult = multipliers[i]
            for left in range(i, -1, -1):
                right_idx = n - 1 - (i - left)
                take_left = mult * nums[left] + dp[i + 1][left + 1]
                take_right = mult * nums[right_idx] + dp[i + 1][left]
                dp[i][left] = max(take_left, take_right)

        return int(dp[0][0])
```

## Python3

```python
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [0] * (m + 1)  # base case: after using all multipliers score is 0
        for i in range(m - 1, -1, -1):
            mult = multipliers[i]
            new_dp = [0] * (m + 1)
            # left can be from 0 to i inclusive
            for left in range(i, -1, -1):
                right = n - 1 - (i - left)
                take_left = mult * nums[left] + dp[left + 1]
                take_right = mult * nums[right] + dp[left]
                new_dp[left] = max(take_left, take_right)
            dp = new_dp
        return dp[0]
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int maximumScore(int* nums, int numsSize, int* multipliers, int multipliersSize) {
    int m = multipliersSize;
    int n = numsSize;
    const long long NEG_INF = -(1LL << 60);

    long long *prev = (long long *)malloc((m + 1) * sizeof(long long));
    long long *cur  = (long long *)malloc((m + 1) * sizeof(long long));

    for (int i = 0; i <= m; ++i) prev[i] = NEG_INF;
    prev[0] = 0;

    for (int i = 1; i <= m; ++i) {
        int mult = multipliers[i - 1];
        for (int j = 0; j <= m; ++j) cur[j] = NEG_INF;

        for (int left = 0; left <= i; ++left) {
            // take from start
            if (left > 0 && prev[left - 1] != NEG_INF) {
                long long cand = prev[left - 1] + (long long)mult * nums[left - 1];
                if (cand > cur[left]) cur[left] = cand;
            }
            // take from end
            int rightTaken = i - left; // number taken from the end so far
            if (rightTaken > 0 && prev[left] != NEG_INF) {
                long long cand = prev[left] + (long long)mult * nums[n - rightTaken];
                if (cand > cur[left]) cur[left] = cand;
            }
        }
        long long *tmp = prev; prev = cur; cur = tmp;
    }

    long long ans = NEG_INF;
    for (int left = 0; left <= m; ++left) {
        if (prev[left] > ans) ans = prev[left];
    }

    free(prev);
    free(cur);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumScore(int[] nums, int[] multipliers) {
        int n = nums.Length;
        int m = multipliers.Length;
        long[,] dp = new long[m + 1, m + 1];

        for (int i = m - 1; i >= 0; --i) {
            for (int left = i; left >= 0; --left) {
                int right = n - 1 - (i - left);
                long takeLeft = multipliers[i] * (long)nums[left] + dp[i + 1, left + 1];
                long takeRight = multipliers[i] * (long)nums[right] + dp[i + 1, left];
                dp[i, left] = Math.Max(takeLeft, takeRight);
            }
        }

        return (int)dp[0, 0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} multipliers
 * @return {number}
 */
var maximumScore = function(nums, multipliers) {
    const n = nums.length;
    const m = multipliers.length;
    const dp = Array.from({ length: m + 1 }, () => Array(m + 1).fill(Number.NEGATIVE_INFINITY));
    dp[0][0] = 0;
    for (let i = 0; i < m; ++i) {
        const mult = multipliers[i];
        for (let left = 0; left <= i; ++left) {
            const cur = dp[i][left];
            if (cur === Number.NEGATIVE_INFINITY) continue;
            // take from start
            const valStart = cur + mult * nums[left];
            if (valStart > dp[i + 1][left + 1]) dp[i + 1][left + 1] = valStart;
            // take from end
            const rightIdx = n - 1 - (i - left);
            const valEnd = cur + mult * nums[rightIdx];
            if (valEnd > dp[i + 1][left]) dp[i + 1][left] = valEnd;
        }
    }
    let ans = Number.NEGATIVE_INFINITY;
    for (let left = 0; left <= m; ++left) {
        if (dp[m][left] > ans) ans = dp[m][left];
    }
    return ans;
};
```

## Typescript

```typescript
function maximumScore(nums: number[], multipliers: number[]): number {
    const n = nums.length;
    const m = multipliers.length;
    // dp[left] represents the best score for the next operation (i+1) when we have taken 'left' elements from the start
    let dp: number[] = new Array(m + 1).fill(0);
    
    for (let i = m - 1; i >= 0; i--) {
        const cur: number[] = new Array(m + 1).fill(0);
        for (let left = 0; left <= i; left++) {
            const rightIdx = n - 1 - (i - left);
            const takeLeft = multipliers[i] * nums[left] + dp[left + 1];
            const takeRight = multipliers[i] * nums[rightIdx] + dp[left];
            cur[left] = Math.max(takeLeft, takeRight);
        }
        dp = cur;
    }
    
    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $multipliers
     * @return Integer
     */
    function maximumScore($nums, $multipliers) {
        $n = count($nums);
        $m = count($multipliers);
        // dp[i][left] = max score from operation i with 'left' elements taken from start so far
        $dp = array_fill(0, $m + 1, array_fill(0, $m + 1, 0));

        for ($i = $m - 1; $i >= 0; $i--) {
            $mult = $multipliers[$i];
            for ($left = 0; $left <= $i; $left++) {
                // Take from the start
                $pickLeft = $mult * $nums[$left] + $dp[$i + 1][$left + 1];

                // Take from the end
                $rightIdx = $n - 1 - ($i - $left);
                $pickRight = $mult * $nums[$rightIdx] + $dp[$i + 1][$left];

                $dp[$i][$left] = max($pickLeft, $pickRight);
            }
        }

        return $dp[0][0];
    }
}
```

## Swift

```swift
class Solution {
    func maximumScore(_ nums: [Int], _ multipliers: [Int]) -> Int {
        let n = nums.count
        let m = multipliers.count
        var dp = Array(repeating: Array(repeating: 0, count: m + 1), count: m + 1)
        
        for i in stride(from: m - 1, through: 0, by: -1) {
            for left in 0...i {
                let right = n - 1 - (i - left)
                let mult = multipliers[i]
                let takeLeft = dp[i + 1][left + 1] + nums[left] * mult
                let takeRight = dp[i + 1][left] + nums[right] * mult
                dp[i][left] = max(takeLeft, takeRight)
            }
        }
        return dp[0][0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumScore(nums: IntArray, multipliers: IntArray): Int {
        val n = nums.size
        val m = multipliers.size
        var dp = LongArray(m + 1) { Long.MIN_VALUE }
        dp[0] = 0L
        for (i in 1..m) {
            val newDp = LongArray(m + 1) { Long.MIN_VALUE }
            val mult = multipliers[i - 1].toLong()
            for (left in 0..i) {
                // Take from the start
                if (left > 0 && dp[left - 1] != Long.MIN_VALUE) {
                    val score = dp[left - 1] + nums[left - 1].toLong() * mult
                    if (score > newDp[left]) newDp[left] = score
                }
                // Take from the end
                if (i - left > 0 && dp[left] != Long.MIN_VALUE) {
                    val rightIdx = n - (i - left)
                    val score = dp[left] + nums[rightIdx].toLong() * mult
                    if (score > newDp[left]) newDp[left] = score
                }
            }
            dp = newDp
        }
        var ans = Long.MIN_VALUE
        for (v in dp) {
            if (v > ans) ans = v
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maximumScore(List<int> nums, List<int> multipliers) {
    int n = nums.length;
    int m = multipliers.length;
    const int NEG_INF = -1 << 60; // sufficiently small

    List<int> dpPrev = List.filled(m + 1, NEG_INF);
    dpPrev[0] = 0;

    for (int i = 1; i <= m; ++i) {
      List<int> dpCurr = List.filled(m + 1, NEG_INF);
      int mult = multipliers[i - 1];
      for (int left = 0; left <= i; ++left) {
        // Take from the start
        if (left > 0 && dpPrev[left - 1] != NEG_INF) {
          int val = dpPrev[left - 1] + nums[left - 1] * mult;
          if (val > dpCurr[left]) dpCurr[left] = val;
        }
        // Take from the end
        if (left <= i - 1 && dpPrev[left] != NEG_INF) {
          int rightIdx = n - 1 - ((i - 1) - left);
          int val = dpPrev[left] + nums[rightIdx] * mult;
          if (val > dpCurr[left]) dpCurr[left] = val;
        }
      }
      dpPrev = dpCurr;
    }

    int ans = NEG_INF;
    for (int v in dpPrev) {
      if (v > ans) ans = v;
    }
    return ans;
  }
}
```

## Golang

```go
func maximumScore(nums []int, multipliers []int) int {
    n := len(nums)
    m := len(multipliers)

    // dp[i][l] = max score using operations i..m-1 when l numbers have been taken from the start
    dp := make([][]int, m+1)
    for i := 0; i <= m; i++ {
        dp[i] = make([]int, m+1)
    }

    // Fill DP bottom‑up
    for i := m - 1; i >= 0; i-- {
        mult := multipliers[i]
        // left can range from 0 to i (inclusive)
        for l := i; l >= 0; l-- {
            rIdx := n - 1 - (i - l) // index of the rightmost available element
            takeLeft := mult*nums[l] + dp[i+1][l+1]
            takeRight := mult*nums[rIdx] + dp[i+1][l]
            if takeLeft > takeRight {
                dp[i][l] = takeLeft
            } else {
                dp[i][l] = takeRight
            }
        }
    }

    return dp[0][0]
}
```

## Ruby

```ruby
def maximum_score(nums, multipliers)
  n = nums.length
  m = multipliers.length
  neg_inf = -(1 << 60)

  dp = Array.new(m + 1, neg_inf)
  dp[0] = 0

  (0...m).each do |i|
    ndp = Array.new(m + 1, neg_inf)
    mult = multipliers[i]
    (0..i).each do |left|
      cur = dp[left]
      next if cur == neg_inf

      # take from the start
      val_left = cur + mult * nums[left]
      ndp[left + 1] = val_left if val_left > ndp[left + 1]

      # take from the end
      right_idx = n - 1 - (i - left)
      val_right = cur + mult * nums[right_idx]
      ndp[left] = val_right if val_right > ndp[left]
    end
    dp = ndp
  end

  dp.max
end
```

## Scala

```scala
object Solution {
    def maximumScore(nums: Array[Int], multipliers: Array[Int]): Int = {
        val n = nums.length
        val m = multipliers.length
        var next = new Array[Long](m + 1)
        var cur = new Array[Long](m + 1)

        for (i <- (m - 1) to 0 by -1) {
            val mult = multipliers(i).toLong
            for (left <- i to 0 by -1) {
                val rightIdx = n - 1 - (i - left)
                val takeLeft = mult * nums(left) + next(left + 1)
                val takeRight = mult * nums(rightIdx) + next(left)
                cur(left) = if (takeLeft > takeRight) takeLeft else takeRight
            }
            val temp = next
            next = cur
            cur = temp
        }

        next(0).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_score(nums: Vec<i32>, multipliers: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = multipliers.len();

        // dp[left] = max score after processing current number of operations,
        // having taken 'left' elements from the start.
        let mut dp: Vec<i64> = vec![i64::MIN; m + 1];
        dp[0] = 0;

        for i in 1..=m {
            let mult = multipliers[i - 1] as i64;
            let mut ndp: Vec<i64> = vec![i64::MIN; i + 1];

            for left in 0..=i {
                // Take from the start
                if left > 0 && dp[left - 1] != i64::MIN {
                    let val = dp[left - 1] + mult * nums[left - 1] as i64;
                    ndp[left] = ndp[left].max(val);
                }
                // Take from the end
                if left < i && dp[left] != i64::MIN {
                    let right_taken = i - 1 - left;
                    let idx = n - 1 - right_taken;
                    let val = dp[left] + mult * nums[idx] as i64;
                    ndp[left] = ndp[left].max(val);
                }
            }

            dp = ndp;
        }

        dp.into_iter().max().unwrap() as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-score nums multipliers)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (m (length multipliers))
         (numsV (list->vector nums))
         (multV (list->vector multipliers))
         (memo (make-vector (add1 m) #f)))
    (for ([i (in-range (add1 m))])
      (vector-set! memo i (make-vector (add1 m) #f)))
    (letrec ((dp (lambda (i l)
                   (if (= i m)
                       0
                       (let* ((row (vector-ref memo i))
                              (cached (vector-ref row l)))
                         (if (not (eq? cached #f))
                             cached
                             (let* ((mult (vector-ref multV i))
                                    (left (* (vector-ref numsV l) mult))
                                    (score-left (+ left (dp (+ i 1) (+ l 1))))
                                    (right-index (- (- n 1) (- i l))) ; n-1-(i-l)
                                    (right (* (vector-ref numsV right-index) mult))
                                    (score-right (+ right (dp (+ i 1) l)))
                                    (best (if (> score-left score-right) score-left score-right)))
                               (vector-set! row l best)
                               best))))))))
      (dp 0 0))))
```

## Erlang

```erlang
-spec maximum_score(Nums :: [integer()], Multipliers :: [integer()]) -> integer().
maximum_score(Nums, Multipliers) ->
    NumsT = list_to_tuple(Nums),
    MultT = list_to_tuple(Multipliers),
    M = tuple_size(MultT),
    N = tuple_size(NumsT),
    DPZero = erlang:make_tuple(M + 1, 0),
    FinalDP = loop_i(M - 1, M, N, NumsT, MultT, DPZero),
    erlang:element(1, FinalDP).

loop_i(I, _M, _N, _NumsT, _MultT, DP) when I < 0 ->
    DP;
loop_i(I, M, N, NumsT, MultT, DPNext) ->
    DPCur = dp_compute(I, M, N, NumsT, MultT, DPNext),
    loop_i(I - 1, M, N, NumsT, MultT, DPCur).

dp_compute(I, M, N, NumsT, MultT, DPNext) ->
    DPCur0 = erlang:make_tuple(M + 1, 0),
    compute_l(0, I, N, NumsT, MultT, DPNext, DPCur0).

compute_l(L, I, _N, _NumsT, _MultT, _DPNext, DPCur) when L > I ->
    DPCur;
compute_l(L, I, N, NumsT, MultT, DPNext, DPCur) ->
    Mult = erlang:element(I + 1, MultT),
    NumL = erlang:element(L + 1, NumsT),
    RIdx = N - 1 - (I - L),
    NumR = erlang:element(RIdx + 1, NumsT),

    TakeLeft = Mult * NumL + erlang:element(L + 2, DPNext),
    TakeRight = Mult * NumR + erlang:element(L + 1, DPNext),

    Best = if TakeLeft > TakeRight -> TakeLeft; true -> TakeRight end,
    DPCur1 = erlang:setelement(L + 1, DPCur, Best),
    compute_l(L + 1, I, N, NumsT, MultT, DPNext, DPCur1).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_score(nums :: [integer], multipliers :: [integer]) :: integer
  def maximum_score(nums, multipliers) do
    n = length(nums)
    m = length(multipliers)

    nums_t = List.to_tuple(nums)
    mult_t = List.to_tuple(multiplers)

    # dp maps number of taken elements from the left to the best score so far
    initial_dp = %{0 => 0}

    final_dp =
      0..(m - 1)
      |> Enum.reduce(initial_dp, fn i, dp ->
        mult = elem(mult_t, i)

        Enum.reduce(dp, %{}, fn {left_taken, cur_score}, new_dp ->
          # Take from the left
          left_val = cur_score + elem(nums_t, left_taken) * mult

          new_dp =
            Map.update(new_dp, left_taken + 1, left_val, fn existing -> max(existing, left_val) end)

          # Take from the right
          right_idx = n - 1 - (i - left_taken)
          right_val = cur_score + elem(nums_t, right_idx) * mult

          Map.update(new_dp, left_taken, right_val, fn existing -> max(existing, right_val) end)
        end)
      end)

    final_dp
    |> Enum.max_by(fn {_k, v} -> v end)
    |> elem(1)
  end
end
```

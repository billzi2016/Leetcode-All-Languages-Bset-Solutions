# 2919. Minimum Increment Operations to Make Array Beautiful

## Cpp

```cpp
class Solution {
public:
    long long minIncrementOperations(std::vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<long long> dp(n, 0);
        auto cost = [&](int i)->long long{
            long long need = (long long)k - nums[i];
            return need > 0 ? need : 0;
        };
        for (int i = 0; i < n && i < 3; ++i) {
            dp[i] = cost(i);
        }
        for (int i = 3; i < n; ++i) {
            long long mn = std::min({dp[i-1], dp[i-2], dp[i-3]});
            dp[i] = cost(i) + mn;
        }
        long long ans = LLONG_MAX;
        for (int i = n-1; i >= std::max(0, n-3); --i) {
            ans = std::min(ans, dp[i]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minIncrementOperations(int[] nums, int k) {
        int n = nums.length;
        long[] dp = new long[n];
        long[] cost = new long[n];
        for (int i = 0; i < n; i++) {
            long diff = (long) k - nums[i];
            cost[i] = diff > 0 ? diff : 0L;
        }
        dp[0] = cost[0];
        if (n > 1) dp[1] = cost[1];
        if (n > 2) dp[2] = cost[2];
        for (int i = 3; i < n; i++) {
            long minPrev = Math.min(dp[i - 1], Math.min(dp[i - 2], dp[i - 3]));
            dp[i] = cost[i] + minPrev;
        }
        long ans = Math.min(dp[n - 1], Math.min(dp[n - 2], dp[n - 3]));
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minIncrementOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        cost = [max(0, k - x) for x in nums]

        # Base cases for first three positions
        dp = cost[:]  # dp[i] will hold min cost with i selected

        if n == 3:
            return min(dp[0], dp[1], dp[2])

        for i in range(3, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2], dp[i - 3])

        return min(dp[n - 1], dp[n - 2], dp[n - 3])
```

## Python3

```python
from typing import List

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cost = [max(0, k - x) for x in nums]
        INF = 10**18
        dp = [INF] * n

        # Base cases for first three positions
        for i in range(min(3, n)):
            dp[i] = cost[i]

        # DP transition for the rest
        for i in range(3, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2], dp[i - 3])

        # Answer is minimum among the last three positions (or fewer if n < 3)
        ans = INF
        for i in range(n - 3, n):
            if i >= 0:
                ans = min(ans, dp[i])
        return ans
```

## C

```c
long long minIncrementOperations(int* nums, int numsSize, int k) {
    if (numsSize < 3) return 0;
    long long *dp = (long long *)malloc(sizeof(long long) * numsSize);
    long long cost0 = k > nums[0] ? (long long)k - nums[0] : 0LL;
    dp[0] = cost0;
    if (numsSize > 1) {
        long long cost1 = k > nums[1] ? (long long)k - nums[1] : 0LL;
        dp[1] = cost1;
    }
    if (numsSize > 2) {
        long long cost2 = k > nums[2] ? (long long)k - nums[2] : 0LL;
        dp[2] = cost2;
    }
    for (int i = 3; i < numsSize; ++i) {
        long long cost = k > nums[i] ? (long long)k - nums[i] : 0LL;
        long long minPrev = dp[i-1];
        if (dp[i-2] < minPrev) minPrev = dp[i-2];
        if (dp[i-3] < minPrev) minPrev = dp[i-3];
        dp[i] = cost + minPrev;
    }
    long long ans = dp[numsSize-1];
    if (dp[numsSize-2] < ans) ans = dp[numsSize-2];
    if (dp[numsSize-3] < ans) ans = dp[numsSize-3];
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MinIncrementOperations(int[] nums, int k) {
        int n = nums.Length;
        long[] dp = new long[n];
        for (int i = 0; i < Math.Min(3, n); i++) {
            dp[i] = Math.Max(0L, (long)k - nums[i]);
        }
        for (int i = 3; i < n; i++) {
            long inc = Math.Max(0L, (long)k - nums[i]);
            long minPrev = Math.Min(dp[i - 1], Math.Min(dp[i - 2], dp[i - 3]));
            dp[i] = inc + minPrev;
        }
        long ans = dp[n - 1];
        if (n >= 2) ans = Math.Min(ans, dp[n - 2]);
        if (n >= 3) ans = Math.Min(ans, dp[n - 3]);
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minIncrementOperations = function(nums, k) {
    const n = nums.length;
    const cost = new Array(n);
    for (let i = 0; i < n; ++i) {
        const diff = k - nums[i];
        cost[i] = diff > 0 ? diff : 0;
    }
    const dp = new Array(n);
    dp[0] = cost[0];
    if (n > 1) dp[1] = cost[1];
    if (n > 2) dp[2] = cost[2];
    for (let i = 3; i < n; ++i) {
        const minPrev = Math.min(dp[i - 1], dp[i - 2], dp[i - 3]);
        dp[i] = cost[i] + minPrev;
    }
    return Math.min(dp[n - 1], dp[n - 2], dp[n - 3]);
};
```

## Typescript

```typescript
function minIncrementOperations(nums: number[], k: number): number {
    const n = nums.length;
    const cost = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        const diff = k - nums[i];
        cost[i] = diff > 0 ? diff : 0;
    }
    const dp = new Array<number>(n);
    dp[0] = cost[0];
    if (n > 1) dp[1] = cost[1];
    if (n > 2) dp[2] = cost[2];
    for (let i = 3; i < n; i++) {
        const minPrev = Math.min(dp[i - 1], dp[i - 2], dp[i - 3]);
        dp[i] = cost[i] + minPrev;
    }
    let ans = dp[n - 1];
    if (n >= 2) ans = Math.min(ans, dp[n - 2]);
    if (n >= 3) ans = Math.min(ans, dp[n - 3]);
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minIncrementOperations($nums, $k) {
        $n = count($nums);
        if ($n == 0) return 0;
        $dp = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; ++$i) {
            $need = $k - $nums[$i];
            if ($need < 0) $need = 0;
            if ($i < 3) {
                $dp[$i] = $need;
            } else {
                $minPrev = min($dp[$i-1], $dp[$i-2], $dp[$i-3]);
                $dp[$i] = $need + $minPrev;
            }
        }
        $ans = PHP_INT_MAX;
        for ($i = $n - 3; $i < $n; ++$i) {
            if ($i >= 0 && $dp[$i] < $ans) {
                $ans = $dp[$i];
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minIncrementOperations(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        var cost = [Int](repeating: 0, count: n)
        for i in 0..<n {
            let diff = k - nums[i]
            cost[i] = diff > 0 ? diff : 0
        }
        var dp = [Int](repeating: 0, count: n)
        for i in 0..<n {
            if i <= 2 {
                dp[i] = cost[i]
            } else {
                let minPrev = min(dp[i - 1], min(dp[i - 2], dp[i - 3]))
                dp[i] = cost[i] + minPrev
            }
        }
        var answer = Int.max
        let start = max(0, n - 3)
        for i in start..<n {
            answer = min(answer, dp[i])
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minIncrementOperations(nums: IntArray, k: Int): Long {
        val n = nums.size
        if (n == 0) return 0L
        val dp = LongArray(n)
        for (i in 0 until minOf(3, n)) {
            dp[i] = maxOf(0L, (k - nums[i]).toLong())
        }
        for (i in 3 until n) {
            val minPrev = minOf(dp[i - 1], dp[i - 2], dp[i - 3])
            dp[i] = maxOf(0L, (k - nums[i]).toLong()) + minPrev
        }
        return minOf(dp[n - 1], dp[n - 2], dp[n - 3])
    }
}
```

## Dart

```dart
class Solution {
  int minIncrementOperations(List<int> nums, int k) {
    int n = nums.length;
    List<int> dp = List.filled(n, 0);
    // Helper to compute required increment for position i
    int cost(int i) => (k - nums[i] > 0) ? k - nums[i] : 0;

    // Base cases for first three positions
    for (int i = 0; i < n && i < 3; ++i) {
      dp[i] = cost(i);
    }

    // DP transition for the rest
    for (int i = 3; i < n; ++i) {
      int minPrev = dp[i - 1];
      if (dp[i - 2] < minPrev) minPrev = dp[i - 2];
      if (dp[i - 3] < minPrev) minPrev = dp[i - 3];
      dp[i] = cost(i) + minPrev;
    }

    // Answer is the minimum among the last three dp values
    int ans = dp[n - 1];
    if (n >= 2 && dp[n - 2] < ans) ans = dp[n - 2];
    if (n >= 3 && dp[n - 3] < ans) ans = dp[n - 3];
    return ans;
  }
}
```

## Golang

```go
func minIncrementOperations(nums []int, k int) int64 {
    n := len(nums)
    if n == 0 {
        return 0
    }
    kk := int64(k)
    cost := make([]int64, n)
    for i, v := range nums {
        diff := kk - int64(v)
        if diff < 0 {
            diff = 0
        }
        cost[i] = diff
    }

    dp := make([]int64, n)
    dp[0] = cost[0]
    if n > 1 {
        dp[1] = cost[1]
    }
    if n > 2 {
        dp[2] = cost[2]
    }
    for i := 3; i < n; i++ {
        minPrev := dp[i-1]
        if dp[i-2] < minPrev {
            minPrev = dp[i-2]
        }
        if dp[i-3] < minPrev {
            minPrev = dp[i-3]
        }
        dp[i] = cost[i] + minPrev
    }

    ans := dp[n-1]
    if n >= 2 && dp[n-2] < ans {
        ans = dp[n-2]
    }
    if n >= 3 && dp[n-3] < ans {
        ans = dp[n-3]
    }
    return ans
}
```

## Ruby

```ruby
def min_increment_operations(nums, k)
  n = nums.length
  inc = ->(i) { [k - nums[i], 0].max }
  dp = Array.new(n, 0)

  dp[0] = inc.call(0)
  dp[1] = inc.call(1) if n > 1
  dp[2] = inc.call(2) if n > 2

  (3...n).each do |i|
    min_prev = dp[i - 1]
    min_prev = dp[i - 2] if dp[i - 2] < min_prev
    min_prev = dp[i - 3] if dp[i - 3] < min_prev
    dp[i] = inc.call(i) + min_prev
  end

  ans = dp[n - 1]
  ans = dp[n - 2] if n >= 2 && dp[n - 2] < ans
  ans = dp[n - 3] if n >= 3 && dp[n - 3] < ans
  ans
end
```

## Scala

```scala
object Solution {
    def minIncrementOperations(nums: Array[Int], k: Int): Long = {
        val n = nums.length
        val dp = new Array[Long](n)
        val kk = k.toLong

        // Initialize first up to three positions
        for (i <- 0 until math.min(3, n)) {
            dp(i) = math.max(0L, kk - nums(i).toLong)
        }

        // DP transition for the rest
        for (i <- 3 until n) {
            val cost = math.max(0L, kk - nums(i).toLong)
            var minPrev = dp(i - 1)
            if (dp(i - 2) < minPrev) minPrev = dp(i - 2)
            if (dp(i - 3) < minPrev) minPrev = dp(i - 3)
            dp(i) = cost + minPrev
        }

        // Answer is the minimum among the last three dp values
        var ans = dp(n - 1)
        if (n >= 2 && dp(n - 2) < ans) ans = dp(n - 2)
        if (n >= 3 && dp(n - 3) < ans) ans = dp(n - 3)

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_increment_operations(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k_i64 = k as i64;
        let mut dp = vec![0i64; n];
        // Base cases for first three positions
        for i in 0..n.min(3) {
            let cost = (k_i64 - nums[i] as i64).max(0);
            dp[i] = cost;
        }
        // DP transition for the rest
        if n > 3 {
            for i in 3..n {
                let cost = (k_i64 - nums[i] as i64).max(0);
                let min_prev = dp[i - 1].min(dp[i - 2]).min(dp[i - 3]);
                dp[i] = cost + min_prev;
            }
        }
        // Answer is the minimum among the last three dp values
        let mut ans = dp[n - 1];
        if n >= 2 {
            ans = ans.min(dp[n - 2]);
        }
        if n >= 3 {
            ans = ans.min(dp[n - 3]);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-increment-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (define (cost idx)
      (let ((diff (- k (vector-ref v idx))))
        (if (> diff 0) diff 0)))
    (if (= n 3)
        (min (cost 0) (cost 1) (cost 2))
        (let ([dp0 (cost 0)]
              [dp1 (cost 1)]
              [dp2 (cost 2)])
          (for ([i (in-range 3 n)])
            (let* ((ci (cost i))
                   (dpi (+ ci (min dp0 dp1 dp2))))
              (set! dp0 dp1)
              (set! dp1 dp2)
              (set! dp2 dpi)))
          (min dp0 dp1 dp2)))))
```

## Erlang

```erlang
-module(solution).
-export([min_increment_operations/2]).

-spec min_increment_operations(Nums :: [integer()], K :: integer()) -> integer().
min_increment_operations(Nums, K) ->
    Inc = fun(V) ->
        if V >= K -> 0;
           true -> K - V
        end
    end,
    case Nums of
        [A,B,C|Rest] ->
            D0 = Inc(A),
            D1 = Inc(B),
            D2 = Inc(C),
            {F0,F1,F2} = process(Rest, Inc, D0, D1, D2),
            min3(F0, F1, F2)
    end.

process([], _Inc, D0, D1, D2) ->
    {D0, D1, D2};
process([X|Xs], Inc, D0, D1, D2) ->
    CurNeed = Inc(X),
    MinPrev = min3(D0, D1, D2),
    CurDP = CurNeed + MinPrev,
    process(Xs, Inc, D1, D2, CurDP).

min3(A,B,C) when A =< B, A =< C -> A;
min3(_,B,C) when B =< C -> B;
min3(_,_,C) -> C.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_increment_operations(nums :: [integer], k :: integer) :: integer
  def min_increment_operations(nums, k) do
    # nums length is guaranteed to be at least 3
    [a, b, c | rest] = nums

    dp0 = max(0, k - a)
    dp1 = max(0, k - b)
    dp2 = max(0, k - c)

    {d3, d2, d1} =
      Enum.reduce(rest, {dp0, dp1, dp2}, fn x, {prev3, prev2, prev1} ->
        cost = max(0, k - x)
        new_dp = cost + Enum.min([prev1, prev2, prev3])
        {prev2, prev1, new_dp}
      end)

    Enum.min([d3, d2, d1])
  end
end
```

# 0746. Min Cost Climbing Stairs

## Cpp

```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        int dp_next = 0;      // dp[i+1]
        int dp_nextnext = 0;  // dp[i+2]
        for (int i = n - 1; i >= 0; --i) {
            int cur = cost[i] + min(dp_next, dp_nextnext);
            dp_nextnext = dp_next;
            dp_next = cur;
        }
        return min(dp_next, dp_nextnext);
    }
};
```

## Java

```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int dpNext = 0;      // dp[i+1]
        int dpNextNext = 0;  // dp[i+2]
        for (int i = n - 1; i >= 0; --i) {
            int cur = cost[i] + Math.min(dpNext, dpNextNext);
            dpNextNext = dpNext;
            dpNext = cur;
        }
        return Math.min(dpNext, dpNextNext);
    }
}
```

## Python

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        next1 = 0  # dp[i+1]
        next2 = 0  # dp[i+2]
        for i in range(n - 1, -1, -1):
            cur = cost[i] + (next1 if next1 < next2 else next2)
            next2 = next1
            next1 = cur
        return next1 if next1 < next2 else next2
```

## Python3

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] will hold the minimum cost to reach step i
        # We only need the last two values.
        prev2, prev1 = 0, 0  # dp[0] and dp[1] are both 0 (starting points)
        for i in range(2, n + 1):
            cur = min(prev2 + cost[i - 2], prev1 + cost[i - 1])
            prev2, prev1 = prev1, cur
        return prev1
```

## C

```c
int minCostClimbingStairs(int* cost, int costSize) {
    int next1 = 0; // dp[i+1]
    int next2 = 0; // dp[i+2]
    for (int i = costSize - 1; i >= 0; --i) {
        int cur = cost[i] + (next1 < next2 ? next1 : next2);
        next2 = next1;
        next1 = cur;
    }
    return next1 < next2 ? next1 : next2;
}
```

## Csharp

```csharp
public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        int n = cost.Length;
        int dpNext = 0;      // dp[i+1]
        int dpNextNext = 0;  // dp[i+2]

        for (int i = n - 1; i >= 0; i--) {
            int current = cost[i] + Math.Min(dpNext, dpNextNext);
            dpNextNext = dpNext;
            dpNext = current;
        }

        return Math.Min(dpNext, dpNextNext);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    const n = cost.length;
    let next = 0;      // dp[i+1]
    let nextNext = 0;  // dp[i+2]
    for (let i = n - 1; i >= 0; --i) {
        const cur = cost[i] + Math.min(next, nextNext);
        nextNext = next;
        next = cur;
    }
    return Math.min(next, nextNext);
};
```

## Typescript

```typescript
function minCostClimbingStairs(cost: number[]): number {
    const n = cost.length;
    let next1 = 0; // dp[i+1]
    let next2 = 0; // dp[i+2]
    for (let i = n - 1; i >= 0; i--) {
        const cur = cost[i] + Math.min(next1, next2);
        next2 = next1;
        next1 = cur;
    }
    return Math.min(next1, next2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @return Integer
     */
    function minCostClimbingStairs($cost) {
        $n = count($cost);
        // dp[i+1] and dp[i+2] for the next iteration, initialized as 0 for the top (dp[n]=0) and dp[n+1]=0
        $next1 = 0; // dp[i+1]
        $next2 = 0; // dp[i+2]

        for ($i = $n - 1; $i >= 0; --$i) {
            $current = $cost[$i] + min($next1, $next2);
            // shift for next iteration
            $next2 = $next1;
            $next1 = $current;
        }

        // After the loop, $next1 is dp[0], $next2 is dp[1]
        return min($next1, $next2);
    }
}
```

## Swift

```swift
class Solution {
    func minCostClimbingStairs(_ cost: [Int]) -> Int {
        var nextOne = 0   // dp[i+1]
        var nextTwo = 0   // dp[i+2]
        for i in stride(from: cost.count - 1, through: 0, by: -1) {
            let current = cost[i] + min(nextOne, nextTwo)
            nextTwo = nextOne
            nextOne = current
        }
        return min(nextOne, nextTwo)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCostClimbingStairs(cost: IntArray): Int {
        val n = cost.size
        if (n == 2) return kotlin.math.min(cost[0], cost[1])
        var twoStepsBack = cost[0]
        var oneStepBack = cost[1]
        for (i in 2 until n) {
            val current = cost[i] + kotlin.math.min(oneStepBack, twoStepsBack)
            twoStepsBack = oneStepBack
            oneStepBack = current
        }
        return kotlin.math.min(oneStepBack, twoStepsBack)
    }
}
```

## Dart

```dart
class Solution {
  int minCostClimbingStairs(List<int> cost) {
    int n = cost.length;
    int next1 = 0; // dp[i+1]
    int next2 = 0; // dp[i+2]

    for (int i = n - 1; i >= 0; i--) {
      int cur = cost[i] + (next1 < next2 ? next1 : next2);
      next2 = next1;
      next1 = cur;
    }

    return next1 < next2 ? next1 : next2;
  }
}
```

## Golang

```go
func minCostClimbingStairs(cost []int) int {
    n := len(cost)
    if n == 0 {
        return 0
    }
    dpNext1, dpNext2 := 0, 0 // dp[i+1], dp[i+2]
    var cur int
    for i := n - 1; i >= 0; i-- {
        cur = cost[i] + min(dpNext1, dpNext2)
        dpNext2 = dpNext1
        dpNext1 = cur
    }
    return min(dpNext1, dpNext2)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

## Ruby

```ruby
# @param {Integer[]} cost
# @return {Integer}
def min_cost_climbing_stairs(cost)
  dp_next = 0   # dp[i+1]
  dp_next_next = 0 # dp[i+2]

  (cost.length - 1).downto(0) do |i|
    current = cost[i] + [dp_next, dp_next_next].min
    dp_next_next = dp_next
    dp_next = current
  end

  [dp_next, dp_next_next].min
end
```

## Scala

```scala
object Solution {
    def minCostClimbingStairs(cost: Array[Int]): Int = {
        val n = cost.length
        val dp = new Array[Int](n + 1)
        dp(n) = 0
        for (i <- (n - 1) to 0 by -1) {
            val next1 = dp(i + 1)
            val next2 = if (i + 2 <= n) dp(i + 2) else Int.MaxValue
            dp(i) = cost(i) + math.min(next1, next2)
        }
        math.min(dp(0), dp(1))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let n = cost.len();
        let mut dp_next1: i32 = 0; // dp[i+1]
        let mut dp_next2: i32 = 0; // dp[i+2]
        for i in (0..n).rev() {
            let cur = cost[i] + std::cmp::min(dp_next1, dp_next2);
            dp_next2 = dp_next1;
            dp_next1 = cur;
        }
        std::cmp::min(dp_next1, dp_next2)
    }
}
```

## Racket

```racket
(define/contract (min-cost-climbing-stairs cost)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length cost))
         (next1 0)   ; dp[i+1]
         (next2 0))  ; dp[i+2]
    (for ([i (in-range (- n 1) -1 -1)])
      (let* ((c (list-ref cost i))
             (cur (+ c (min next1 next2))))
        (set! next2 next1)
        (set! next1 cur)))
    (min next1 next2)))
```

## Erlang

```erlang
-spec min_cost_climbing_stairs(Cost :: [integer()]) -> integer().
min_cost_climbing_stairs(Cost) ->
    {DP0, DP1} = lists:foldl(
        fun(C, {Prev1, Prev2}) ->
            Curr = C + erlang:min(Prev1, Prev2),
            {Curr, Prev1}
        end,
        {0, 0},
        lists:reverse(Cost)
    ),
    erlang:min(DP0, DP1).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost_climbing_stairs(cost :: [integer]) :: integer
  def min_cost_climbing_stairs(cost) do
    n = length(cost)
    indices = Enum.to_list(0..(n - 1)) |> Enum.reverse()

    {_, _, dp0, dp1} =
      Enum.reduce(indices, {0, 0, nil, nil}, fn i, {next1, next2, acc_dp0, acc_dp1} ->
        cur = Enum.at(cost, i) + min(next1, next2)
        new_dp0 = if i == 0, do: cur, else: acc_dp0
        new_dp1 = if i == 1, do: cur, else: acc_dp1
        {cur, next1, new_dp0, new_dp1}
      end)

    min(dp0, dp1)
  end
end
```

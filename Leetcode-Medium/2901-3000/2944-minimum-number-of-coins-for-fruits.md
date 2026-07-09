# 2944. Minimum Number of Coins for Fruits

## Cpp

```cpp
class Solution {
public:
    int minimumCoins(vector<int>& prices) {
        int n = prices.size();
        const long long INF = 4e18;
        vector<long long> dp(n + 1, INF);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            int maxj = min(n, 2 * i + 2); // inclusive upper bound
            long long best = INF;
            for (int j = i + 1; j <= maxj; ++j) {
                if (dp[j] < best) best = dp[j];
            }
            dp[i] = (long long)prices[i] + best;
        }
        return (int)dp[0];
    }
};
```

## Java

```java
class Solution {
    public int minimumCoins(int[] prices) {
        int n = prices.length;
        int[] dp = new int[n + 1];
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            int maxIdx = Math.min(n, 2 * i + 2);
            int minNext = Integer.MAX_VALUE;
            for (int j = i + 1; j <= maxIdx; ++j) {
                if (dp[j] < minNext) {
                    minNext = dp[j];
                }
            }
            dp[i] = prices[i] + minNext;
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            upper = min(n, 2 * i + 2)  # maximum index we can start next after using reward
            best = float('inf')
            for j in range(i + 1, upper + 1):
                if dp[j] < best:
                    best = dp[j]
            dp[i] = prices[i] + best
        return dp[0]
```

## Python3

```python
import sys
from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        INF = 10**18
        dp = [INF] * (n + 1)   # dp[i]: min coins to acquire fruits from i to end
        dp[n] = 0               # no fruit left
        
        # monotonic queue for sliding window minimum
        from collections import deque
        dq = deque()            # stores pairs (index, dp value)
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            # The furthest index we can jump to after buying fruit i
            max_jump = min(n, i + (i + 1) + 1)   # i is 0‑based, fruit number = i+1
            
            # Maintain deque: remove indices out of the new window [i+1, max_jump)
            while dq and dq[0][0] >= max_jump:
                dq.popleft()
            
            # Insert dp[i+1] into deque (it becomes candidate for future windows)
            val = dp[i + 1]
            idx = i + 1
            while dq and dq[-1][1] >= val:
                dq.pop()
            dq.append((idx, val))
            
            # Minimum in window is at front of deque
            best = dq[0][1] if dq else INF
            dp[i] = prices[i] + (best if i + (i + 1) + 1 < n else 0)
        
        return dp[0]
```

## C

```c
int minimumCoins(int* prices, int pricesSize) {
    if (pricesSize == 0) return 0;
    const long long INF = 1LL << 60;
    long long notBuyPrev = INF;                 // dp[i-1][0]
    long long buyPrev = prices[0];               // dp[i-1][1]
    for (int i = 1; i < pricesSize; ++i) {
        long long notBuyCurr = buyPrev;                              // dp[i][0] = dp[i-1][1]
        long long buyCurr = (long long)prices[i] + 
                           (notBuyPrev < buyPrev ? notBuyPrev : buyPrev); // dp[i][1]
        notBuyPrev = notBuyCurr;
        buyPrev = buyCurr;
    }
    long long ans = notBuyPrev < buyPrev ? notBuyPrev : buyPrev;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumCoins(int[] prices) {
        int n = prices.Length;
        int[] dp = new int[n + 1];
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            int left = i + 1;
            int right = Math.Min(n, i + i + 2);
            int best = int.MaxValue;
            for (int k = left; k <= right; ++k) {
                if (dp[k] < best) best = dp[k];
            }
            dp[i] = prices[i] + best;
        }
        return dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var minimumCoins = function(prices) {
    const n = prices.length;
    const dp = new Array(n + 1).fill(0); // dp[n] = 0
    
    for (let i = n - 1; i >= 0; --i) {
        let best = Infinity;
        const start = i + 1;
        const end = Math.min(n, i + 1 + (i + 1)); // can skip up to i+1 fruits
        for (let j = start; j <= end; ++j) {
            if (dp[j] < best) best = dp[j];
        }
        dp[i] = prices[i] + best;
    }
    
    return dp[0];
};
```

## Typescript

```typescript
function minimumCoins(prices: number[]): number {
    const n = prices.length;
    const dp = new Array<number>(n + 1).fill(0);
    // dp[n] is already 0 (no fruits left)
    for (let i = n - 1; i >= 0; i--) {
        let best = Number.MAX_SAFE_INTEGER;
        const maxJump = Math.min(n, i + i + 2); // i + (i+2) as derived
        for (let j = i + 1; j <= maxJump; j++) {
            if (dp[j] < best) best = dp[j];
        }
        dp[i] = prices[i] + best;
    }
    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function minimumCoins($prices) {
        $n = count($prices);
        // extra space to avoid bounds checking for i+1 and i+2
        $dp = array_fill(0, $n + 3, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            $costWithReward = $prices[$i] + $dp[$i + 2];   // take next fruit for free
            $costWithoutReward = $prices[$i] + $dp[$i + 1]; // do not use the reward now
            $dp[$i] = min($costWithReward, $costWithoutReward);
        }
        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func minimumCoins(_ prices: [Int]) -> Int {
        let n = prices.count
        var dp = Array(repeating: 0, count: n + 1)
        dp[n] = 0
        if n == 0 { return 0 }
        for i in stride(from: n - 1, through: 0, by: -1) {
            let maxIdx = min(n, 2 * i + 2)
            var best = Int.max
            if i + 1 <= maxIdx {
                for j in (i + 1)...maxIdx {
                    if dp[j] < best { best = dp[j] }
                }
            } else {
                best = 0
            }
            dp[i] = prices[i] + best
        }
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCoins(prices: IntArray): Int {
        val n = prices.size
        val dp = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            var best = Int.MAX_VALUE
            val maxIdx = kotlin.math.min(n, 2 * i + 2)
            var j = i + 1
            while (j <= maxIdx) {
                if (dp[j] < best) best = dp[j]
                j++
            }
            dp[i] = prices[i] + best
        }
        return dp[0]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minimumCoins(List<int> prices) {
    int n = prices.length;
    List<int> dp = List.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      int maxJ = min(n, 2 * i + 2);
      int best = dp[maxJ];
      for (int j = i + 1; j <= maxJ; ++j) {
        if (dp[j] < best) best = dp[j];
      }
      dp[i] = prices[i] + best;
    }
    return dp[0];
  }
}
```

## Golang

```go
func minimumCoins(prices []int) int {
    n := len(prices)
    dp := make([]int, n+2) // dp[n+1] = 0 by default
    const INF = int(1 << 60)

    for i := n; i >= 1; i-- {
        best := INF
        maxJ := i + 1 + i
        if maxJ > n+1 {
            maxJ = n + 1
        }
        for j := i + 1; j <= maxJ; j++ {
            if dp[j] < best {
                best = dp[j]
            }
        }
        dp[i] = prices[i-1] + best
    }
    return dp[1]
}
```

## Ruby

```ruby
def minimum_coins(prices)
  n = prices.length
  dp = Array.new(n, 0)

  (n - 1).downto(0) do |i|
    if 2 * i + 1 >= n - 1
      dp[i] = prices[i]
    else
      limit = [n - 1, 2 * i + 2].min
      best = Float::INFINITY
      (i + 1).upto(limit) do |j|
        val = dp[j]
        best = val if val < best
      end
      dp[i] = prices[i] + best
    end
  end

  dp[0]
end
```

## Scala

```scala
object Solution {
    def minimumCoins(prices: Array[Int]): Int = {
        val n = prices.length
        val dp = new Array[Int](n + 2) // dp[n] and dp[n+1] are 0 by default
        var i = n - 1
        while (i >= 0) {
            val buyNoReward = prices(i) + dp(i + 1)
            val buyUseReward = prices(i) + dp(i + 2)
            dp(i) = if (buyNoReward < buyUseReward) buyNoReward else buyUseReward
            i -= 1
        }
        dp(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_coins(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        // dp[i] = minimal coins to acquire fruits from i..n-1 assuming we buy fruit i
        // dp[n] = 0 (no fruits left)
        let mut dp: Vec<i64> = vec![0; n + 1];
        for i in (0..n).rev() {
            let max_j = std::cmp::min(n, i + 1 + i);
            let mut best = i64::MAX;
            // j ranges from i+1 to max_j inclusive
            for j in (i + 1)..=max_j {
                if dp[j] < best {
                    best = dp[j];
                }
            }
            dp[i] = prices[i] as i64 + best;
        }
        dp[0] as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-coins prices)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length prices))
         (dp (make-vector (+ n 1) 0))) ; dp[n] = 0
    (for ([i (in-range (- n 1) -1 -1)])
      (define price (list-ref prices i))
      (define max-k (min n (+ i price 1))) ; inclusive upper bound for k
      (define min-next
        (apply min
               (for/list ([k (in-range (+ i 1) (+ max-k 1))])
                 (vector-ref dp k))))
      (vector-set! dp i (+ price min-next)))
    (vector-ref dp 0)))
```

## Erlang

```erlang
-spec minimum_coins(Prices :: [integer()]) -> integer().
minimum_coins(Prices) ->
    N = length(Prices),
    % DPAcc holds dp values for indices > current i, starting with dp[N] = 0
    DPAcc = build_dp(lists:seq(N - 1, 0, -1), Prices, N, [0]),
    hd(DPAcc).

build_dp([], _Prices, _N, Acc) -> Acc;
build_dp([I | RestIdx], Prices, N, DPAcc) ->
    PriceI = lists:nth(I + 1, Prices),
    MaxJump = min(N, I + 1 + I),               % maximum j (inclusive)
    Count = MaxJump - I,                       % number of candidates j in [I+1 .. MaxJump]
    MinCost = min_cost(PriceI, DPAcc, Count, 1000000000),
    build_dp(RestIdx, Prices, N, [MinCost | DPAcc]).

min_cost(_Price, _DPAcc, 0, Min) -> Min;
min_cost(Price, [D | Rest], Cnt, Min) ->
    Cost = Price + D,
    NewMin = if Cost < Min -> Cost; true -> Min end,
    min_cost(Price, Rest, Cnt - 1, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_coins(prices :: [integer]) :: integer
  def minimum_coins(prices) do
    n = length(prices)
    base_dp = %{n => 0}
    indices = :lists.seq(n - 1, 0, -1)

    Enum.reduce(indices, base_dp, fn i, dp ->
      price = Enum.at(prices, i)
      limit = min(n, i + i + 2)

      best =
        (i + 1)..limit
        |> Enum.map(&Map.get(dp, &1))
        |> Enum.min()

      Map.put(dp, i, price + best)
    end)
    |> Map.get(0)
  end
end
```

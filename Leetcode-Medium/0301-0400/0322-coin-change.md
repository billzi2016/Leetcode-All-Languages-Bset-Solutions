# 0322. Coin Change

## Cpp

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        const int INF = amount + 1;
        vector<int> dp(amount + 1, INF);
        dp[0] = 0;
        for (int i = 1; i <= amount; ++i) {
            for (int c : coins) {
                if (i >= c && dp[i - c] != INF) {
                    dp[i] = min(dp[i], dp[i - c] + 1);
                }
            }
        }
        return dp[amount] == INF ? -1 : dp[amount];
    }
};
```

## Java

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        java.util.Arrays.fill(dp, max);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        return dp[amount] == max ? -1 : dp[amount];
    }
}
```

## Python

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        max_val = amount + 1
        dp = [max_val] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min_coins = max_val
            for coin in coins:
                if i >= coin:
                    cur = dp[i - coin] + 1
                    if cur < min_coins:
                        min_coins = cur
            dp[i] = min_coins
        return dp[amount] if dp[amount] != max_val else -1
```

## Python3

```python
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        max_val = amount + 1
        dp = [max_val] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min_coins = max_val
            for c in coins:
                if c <= i:
                    cur = dp[i - c] + 1
                    if cur < min_coins:
                        min_coins = cur
            dp[i] = min_coins
        return dp[amount] if dp[amount] != max_val else -1
```

## C

```c
#include <stdlib.h>

int coinChange(int* coins, int coinsSize, int amount) {
    if (amount == 0) return 0;
    int *dp = (int *)malloc((amount + 1) * sizeof(int));
    if (!dp) return -1; // allocation failure fallback
    for (int i = 0; i <= amount; ++i) dp[i] = amount + 1; // INF
    dp[0] = 0;
    for (int i = 0; i < coinsSize; ++i) {
        int c = coins[i];
        for (int j = c; j <= amount; ++j) {
            if (dp[j - c] + 1 < dp[j]) dp[j] = dp[j - c] + 1;
        }
    }
    int res = dp[amount];
    free(dp);
    return (res > amount) ? -1 : res;
}
```

## Csharp

```csharp
public class Solution
{
    public int CoinChange(int[] coins, int amount)
    {
        if (amount == 0) return 0;
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        for (int i = 1; i <= amount; i++) dp[i] = max;

        foreach (int coin in coins)
        {
            if (coin == 0) continue;
        }

        for (int i = 1; i <= amount; i++)
        {
            foreach (int coin in coins)
            {
                if (coin <= i && dp[i - coin] != max)
                {
                    int candidate = dp[i - coin] + 1;
                    if (candidate < dp[i]) dp[i] = candidate;
                }
            }
        }

        return dp[amount] == max ? -1 : dp[amount];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    if (amount === 0) return 0;
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (i >= coin && dp[i - coin] !== Infinity) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
};
```

## Typescript

```typescript
function coinChange(coins: number[], amount: number): number {
    const MAX = amount + 1;
    const dp = new Array<number>(amount + 1).fill(MAX);
    dp[0] = 0;
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (coin <= i) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[amount] === MAX ? -1 : dp[amount];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $coins
     * @param Integer $amount
     * @return Integer
     */
    function coinChange($coins, $amount) {
        if ($amount == 0) return 0;
        $max = $amount + 1;
        $dp = array_fill(0, $amount + 1, $max);
        $dp[0] = 0;
        for ($i = 1; $i <= $amount; $i++) {
            foreach ($coins as $coin) {
                if ($coin <= $i) {
                    $prev = $dp[$i - $coin];
                    if ($prev + 1 < $dp[$i]) {
                        $dp[$i] = $prev + 1;
                    }
                }
            }
        }
        return $dp[$amount] > $amount ? -1 : $dp[$amount];
    }
}
```

## Swift

```swift
class Solution {
    func coinChange(_ coins: [Int], _ amount: Int) -> Int {
        if amount == 0 { return 0 }
        var dp = Array(repeating: amount + 1, count: amount + 1)
        dp[0] = 0
        for i in 1...amount {
            for coin in coins where coin <= i {
                let prev = dp[i - coin]
                if prev != amount + 1 && prev + 1 < dp[i] {
                    dp[i] = prev + 1
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        val INF = amount + 1
        val dp = IntArray(amount + 1) { INF }
        dp[0] = 0
        for (i in 1..amount) {
            for (c in coins) {
                if (i >= c && dp[i - c] != INF) {
                    dp[i] = kotlin.math.min(dp[i], dp[i - c] + 1)
                }
            }
        }
        return if (dp[amount] == INF) -1 else dp[amount]
    }
}
```

## Dart

```dart
class Solution {
  int coinChange(List<int> coins, int amount) {
    List<int> dp = List.filled(amount + 1, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
      for (int coin in coins) {
        if (i - coin >= 0) {
          int candidate = dp[i - coin] + 1;
          if (candidate < dp[i]) dp[i] = candidate;
        }
      }
    }
    return dp[amount] > amount ? -1 : dp[amount];
  }
}
```

## Golang

```go
func coinChange(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	const inf = int(^uint(0) >> 1) // MaxInt
	dp := make([]int, amount+1)
	for i := 1; i <= amount; i++ {
		dp[i] = inf
	}
	dp[0] = 0

	for i := 1; i <= amount; i++ {
		for _, c := range coins {
			if i >= c && dp[i-c] != inf {
				if dp[i] > dp[i-c]+1 {
					dp[i] = dp[i-c] + 1
				}
			}
		}
	}

	if dp[amount] == inf {
		return -1
	}
	return dp[amount]
}
```

## Ruby

```ruby
# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}
def coin_change(coins, amount)
  return 0 if amount == 0
  max = amount + 1
  dp = Array.new(amount + 1, max)
  dp[0] = 0

  coins.each do |coin|
    next if coin > amount
    (coin..amount).each do |i|
      dp[i] = [dp[i], dp[i - coin] + 1].min
    end
  end

  dp[amount] > amount ? -1 : dp[amount]
end
```

## Scala

```scala
object Solution {
    def coinChange(coins: Array[Int], amount: Int): Int = {
        if (amount == 0) return 0
        val INF = amount + 1
        val dp = Array.fill(amount + 1)(INF)
        dp(0) = 0
        for (i <- 1 to amount) {
            var best = INF
            var idx = 0
            while (idx < coins.length) {
                val coin = coins(idx)
                if (coin <= i && dp(i - coin) + 1 < best) {
                    best = dp(i - coin) + 1
                }
                idx += 1
            }
            dp(i) = best
        }
        if (dp(amount) > amount) -1 else dp(amount)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let amt = amount as usize;
        let mut dp = vec![i32::MAX / 2; amt + 1];
        dp[0] = 0;
        for i in 1..=amt {
            for &c in &coins {
                if (c as usize) <= i {
                    let candidate = dp[i - c as usize] + 1;
                    if candidate < dp[i] {
                        dp[i] = candidate;
                    }
                }
            }
        }
        if dp[amt] >= i32::MAX / 2 { -1 } else { dp[amt] }
    }
}
```

## Racket

```racket
(define/contract (coin-change coins amount)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([inf (+ amount 1)]
         [dp (make-vector (+ amount 1) inf)])
    (vector-set! dp 0 0)
    (for ([i (in-range 1 (+ amount 1))])
      (for ([c coins])
        (when (>= i c)
          (let* ([prev (vector-ref dp (- i c))]
                 [cand (+ prev 1)])
            (when (< prev inf)
              (when (< cand (vector-ref dp i))
                (vector-set! dp i cand)))))))
    (let ([res (vector-ref dp amount)])
      (if (= res inf) -1 res))))
```

## Erlang

```erlang
-spec coin_change(Coins :: [integer()], Amount :: integer()) -> integer().
coin_change(_Coins, 0) ->
    0;
coin_change(Coins, Amount) when Amount > 0 ->
    Max = Amount + 1,
    InitArray = array:new(Amount + 1, {default, Max}),
    DP0 = array:set(0, 0, InitArray),
    DPFinal = lists:foldl(
        fun(A, DPAcc) ->
            MinCoins = lists:foldl(
                fun(Coin, CurMin) ->
                    if Coin =< A ->
                        Prev = array:get(A - Coin, DPAcc),
                        case Prev of
                            Max -> CurMin;
                            _ ->
                                New = Prev + 1,
                                erlang:min(CurMin, New)
                        end;
                       true -> CurMin
                    end
                end,
                Max,
                Coins),
            array:set(A, MinCoins, DPAcc)
        end,
        DP0,
        lists:seq(1, Amount)),
    Res = array:get(Amount, DPFinal),
    if Res == Max -> -1; true -> Res end.
```

## Elixir

```elixir
defmodule Solution do
  @spec coin_change(coins :: [integer], amount :: integer) :: integer
  def coin_change(coins, amount) do
    max = amount + 1
    dp = :array.new(amount + 1, default: max)
    dp = :array.set(0, 0, dp)

    dp =
      Enum.reduce(1..amount, dp, fn i, acc ->
        min_val =
          Enum.reduce(coins, max, fn coin, cur_min ->
            if coin <= i do
              prev = :array.get(i - coin, acc)
              cand = prev + 1
              if cand < cur_min, do: cand, else: cur_min
            else
              cur_min
            end
          end)

        :array.set(i, min_val, acc)
      end)

    result = :array.get(amount, dp)
    if result > amount, do: -1, else: result
  end
end
```

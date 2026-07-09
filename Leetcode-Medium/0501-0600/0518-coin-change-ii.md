# 0518. Coin Change II

## Cpp

```cpp
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<long long> dp(amount + 1, 0);
        dp[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i <= amount; ++i) {
                dp[i] += dp[i - coin];
            }
        }
        return static_cast<int>(dp[amount]);
    }
};
```

## Java

```java
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        return dp[amount];
    }
}
```

## Python

```python
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
```

## Python3

```python
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            if coin > amount:
                continue
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
```

## C

```c
#include <stdlib.h>

int change(int amount, int* coins, int coinsSize) {
    long long *dp = (long long *)calloc(amount + 1, sizeof(long long));
    if (!dp) return 0;
    dp[0] = 1;
    for (int i = 0; i < coinsSize; ++i) {
        int coin = coins[i];
        for (int j = coin; j <= amount; ++j) {
            dp[j] += dp[j - coin];
        }
    }
    int result = (int)dp[amount];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int Change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        foreach (int coin in coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        return dp[amount];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */
var change = function(amount, coins) {
    const dp = new Array(amount + 1).fill(0);
    dp[0] = 1;
    for (const coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] += dp[i - coin];
        }
    }
    return dp[amount];
};
```

## Typescript

```typescript
function change(amount: number, coins: number[]): number {
    const dp = new Array<number>(amount + 1).fill(0);
    dp[0] = 1;
    for (const coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] += dp[i - coin];
        }
    }
    return dp[amount];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $amount
     * @param Integer[] $coins
     * @return Integer
     */
    function change($amount, $coins) {
        $dp = array_fill(0, $amount + 1, 0);
        $dp[0] = 1;
        foreach ($coins as $coin) {
            for ($i = $coin; $i <= $amount; $i++) {
                $dp[$i] += $dp[$i - $coin];
            }
        }
        return $dp[$amount];
    }
}
```

## Swift

```swift
class Solution {
    func change(_ amount: Int, _ coins: [Int]) -> Int {
        var dp = Array(repeating: 0, count: amount + 1)
        dp[0] = 1
        for coin in coins {
            if coin > amount { continue }
            for i in coin...amount {
                dp[i] += dp[i - coin]
            }
        }
        return dp[amount]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun change(amount: Int, coins: IntArray): Int {
        val dp = LongArray(amount + 1)
        dp[0] = 1L
        for (coin in coins) {
            var i = coin
            while (i <= amount) {
                dp[i] += dp[i - coin]
                i++
            }
        }
        return dp[amount].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int change(int amount, List<int> coins) {
    List<int> dp = List.filled(amount + 1, 0);
    dp[0] = 1;
    for (int coin in coins) {
      for (int i = coin; i <= amount; ++i) {
        dp[i] += dp[i - coin];
      }
    }
    return dp[amount];
  }
}
```

## Golang

```go
func change(amount int, coins []int) int {
    dp := make([]int, amount+1)
    dp[0] = 1
    for _, coin := range coins {
        for i := coin; i <= amount; i++ {
            dp[i] += dp[i-coin]
        }
    }
    return dp[amount]
}
```

## Ruby

```ruby
def change(amount, coins)
  dp = Array.new(amount + 1, 0)
  dp[0] = 1
  coins.each do |coin|
    (coin..amount).each do |i|
      dp[i] += dp[i - coin]
    end
  end
  dp[amount]
end
```

## Scala

```scala
object Solution {
    def change(amount: Int, coins: Array[Int]): Int = {
        val dp = new Array[Long](amount + 1)
        dp(0) = 1
        for (coin <- coins) {
            var i = coin
            while (i <= amount) {
                dp(i) += dp(i - coin)
                i += 1
            }
        }
        dp(amount).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let amt = amount as usize;
        let mut dp = vec![0i32; amt + 1];
        dp[0] = 1;
        for &c in &coins {
            let coin = c as usize;
            if coin > amt { continue; }
            for j in coin..=amt {
                dp[j] += dp[j - coin];
            }
        }
        dp[amt]
    }
}
```

## Racket

```racket
(define/contract (change amount coins)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let ([dp (make-vector (+ amount 1) 0)])
    (vector-set! dp 0 1)
    (for ([coin coins])
      (when (<= coin amount)
        (for ([i (in-range coin (+ amount 1))])
          (let* ([prev (vector-ref dp (- i coin))]
                 [curr (vector-ref dp i)]
                 [new (+ curr prev)])
            (vector-set! dp i new)))))
    (vector-ref dp amount)))
```

## Erlang

```erlang
-spec change(integer(), [integer()]) -> integer().
change(Amount, Coins) ->
    DP0 = array:set(0, 1, array:new(Amount + 1, {default, 0})),
    FinalDP = lists:foldl(fun(Coin, DPAcc) -> update_coin(Coin, Amount, DPAcc) end,
                          DP0, Coins),
    array:get(Amount, FinalDP).

-spec update_coin(integer(), integer(), array:array()) -> array:array().
update_coin(Coin, Max, DP) ->
    update_coin_loop(Coin, Coin, Max, DP).

-spec update_coin_loop(integer(), integer(), integer(), array:array()) -> array:array().
update_coin_loop(_Coin, J, Max, DP) when J > Max ->
    DP;
update_coin_loop(Coin, J, Max, DP) ->
    Prev = array:get(J - Coin, DP),
    Cur = array:get(J, DP),
    NewDP = array:set(J, Cur + Prev, DP),
    update_coin_loop(Coin, J + 1, Max, NewDP).
```

## Elixir

```elixir
defmodule Solution do
  @spec change(amount :: integer, coins :: [integer]) :: integer
  def change(amount, coins) do
    dp0 = :array.new(amount + 1, 0)
    dp0 = :array.set(0, 1, dp0)

    final_dp =
      Enum.reduce(coins, dp0, fn coin, dp_acc ->
        Enum.reduce(coin..amount, dp_acc, fn sum, dp_inner ->
          prev = :array.get(sum - coin, dp_inner)
          cur = :array.get(sum, dp_inner)
          :array.set(sum, cur + prev, dp_inner)
        end)
      end)

    :array.get(amount, final_dp)
  end
end
```

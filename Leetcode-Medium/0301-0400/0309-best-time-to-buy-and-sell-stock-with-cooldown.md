# 0309. Best Time to Buy and Sell Stock with Cooldown

## Cpp

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        const int INF_NEG = -1e9;
        int hold = -prices[0];      // profit when holding a stock
        int sold = INF_NEG;         // profit just after selling (cooldown)
        int rest = 0;               // profit when in rest state
        
        for (size_t i = 1; i < prices.size(); ++i) {
            int prevHold = hold, prevSold = sold, prevRest = rest;
            hold = max(prevHold, prevRest - prices[i]);   // buy or keep holding
            sold = prevHold + prices[i];                  // sell today
            rest = max(prevRest, prevSold);               // stay/rest after cooldown
        }
        return max(rest, sold);
    }
};
```

## Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) return 0;
        int hold = -prices[0];
        int sold = 0; // profit after selling (cooldown state)
        int rest = 0; // profit when not holding and not in cooldown
        for (int i = 1; i < prices.length; i++) {
            int prevSold = sold;
            sold = hold + prices[i];                 // sell today
            hold = Math.max(hold, rest - prices[i]); // buy today or keep holding
            rest = Math.max(rest, prevSold);         // stay idle or come from cooldown
        }
        return Math.max(sold, rest);
    }
}
```

## Python

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy = -prices[0]   # profit when holding a stock
        sell = 0           # profit after selling today
        rest = 0           # profit when in cooldown or doing nothing
        for price in prices[1:]:
            prev_buy, prev_sell, prev_rest = buy, sell, rest
            buy = max(prev_buy, prev_rest - price)
            sell = prev_buy + price
            rest = max(prev_rest, prev_sell)
        return max(sell, rest)
```

## Python3

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = -prices[0]   # profit when holding a stock
        sell = 0           # profit after selling (in cooldown)
        rest = 0           # profit when free to buy
        
        for price in prices[1:]:
            new_buy = max(buy, rest - price)
            new_sell = buy + price
            new_rest = max(rest, sell)
            buy, sell, rest = new_buy, new_sell, new_rest
        
        return max(sell, rest)
```

## C

```c
int maxProfit(int* prices, int pricesSize){
    if (pricesSize == 0) return 0;
    const int NEG_INF = -1000000000;
    int hold = -prices[0];
    int sold = NEG_INF;
    int rest = 0;
    for (int i = 1; i < pricesSize; ++i){
        int price = prices[i];
        int prev_hold = hold, prev_sold = sold, prev_rest = rest;
        hold = (prev_hold > prev_rest - price) ? prev_hold : prev_rest - price;
        sold = prev_hold + price;
        rest = (prev_rest > prev_sold) ? prev_rest : prev_sold;
    }
    return (rest > sold) ? rest : sold;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices == null || prices.Length == 0) return 0;
        int hold = -prices[0];
        int rest = 0; // not holding, can buy
        int cooldown = int.MinValue / 2; // impossible state
        
        for (int i = 1; i < prices.Length; i++) {
            int prevHold = hold;
            int prevRest = rest;
            int prevCooldown = cooldown;
            
            rest = Math.Max(prevRest, prevCooldown);
            hold = Math.Max(prevHold, prevRest - prices[i]);
            cooldown = prevHold + prices[i];
        }
        
        return Math.Max(rest, cooldown);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    const n = prices.length;
    if (n === 0) return 0;
    
    let notHold = 0;               // dp[i-1][0]
    let hold = -prices[0];         // dp[i-1][1]
    let notHoldPrevPrev = 0;       // dp[i-2][0], initially dp[-1][0] = 0
    
    for (let i = 1; i < n; ++i) {
        const price = prices[i];
        const newNotHold = Math.max(notHold, hold + price);               // sell or stay idle
        const newHold = Math.max(hold, notHoldPrevPrev - price);          // buy after cooldown or keep holding
        
        notHoldPrevPrev = notHold;
        notHold = newNotHold;
        hold = newHold;
    }
    
    return notHold; // maximum profit when not holding any stock at the end
};
```

## Typescript

```typescript
function maxProfit(prices: number[]): number {
    if (prices.length === 0) return 0;
    let hold = -prices[0];
    let sold = 0;
    let rest = 0;

    for (let i = 1; i < prices.length; i++) {
        const price = prices[i];
        const prevHold = hold;
        const prevSold = sold;
        const prevRest = rest;

        hold = Math.max(prevHold, prevRest - price);
        sold = prevHold + price;
        rest = Math.max(prevRest, prevSold);
    }

    return Math.max(sold, rest);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $n = count($prices);
        if ($n == 0) return 0;
        $hold = -$prices[0];
        $sold = -1000000000; // impossible state
        $rest = 0;
        for ($i = 1; $i < $n; $i++) {
            $price = $prices[$i];
            $prevHold = $hold;
            $prevSold = $sold;
            $prevRest = $rest;

            $hold = max($prevHold, $prevRest - $price);
            $sold = $prevHold + $price;
            $rest = max($prevRest, $prevSold);
        }
        return max($sold, $rest);
    }
}
```

## Swift

```swift
class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        if prices.isEmpty { return 0 }
        var hold = -prices[0]
        var sold = 0
        var rest = 0
        for i in 1..<prices.count {
            let price = prices[i]
            let prevHold = hold
            let prevSold = sold
            let prevRest = rest
            hold = max(prevHold, prevRest - price)
            sold = prevHold + price
            rest = max(prevRest, prevSold)
        }
        return max(sold, rest)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(prices: IntArray): Int {
        if (prices.isEmpty()) return 0
        var held = -prices[0]
        var sold = 0
        var rest = 0
        for (i in 1 until prices.size) {
            val price = prices[i]
            val prevSold = sold
            sold = held + price
            held = maxOf(held, rest - price)
            rest = maxOf(rest, prevSold)
        }
        return maxOf(sold, rest)
    }
}
```

## Dart

```dart
class Solution {
  int maxProfit(List<int> prices) {
    if (prices.isEmpty) return 0;
    int hold = -prices[0];
    int rest = 0;
    int cooldown = -(1 << 60);
    for (int i = 1; i < prices.length; i++) {
      int price = prices[i];
      int prevHold = hold;
      int prevRest = rest;
      int prevCooldown = cooldown;

      int newRest = prevRest > prevCooldown ? prevRest : prevCooldown;
      int buyOption = prevRest - price;
      int newHold = prevHold > buyOption ? prevHold : buyOption;
      int newCooldown = prevHold + price;

      hold = newHold;
      rest = newRest;
      cooldown = newCooldown;
    }
    return rest > cooldown ? rest : cooldown;
  }
}
```

## Golang

```go
func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	hold := -prices[0] // profit when holding a stock
	cash := 0          // profit when not holding and can buy
	prevCash := 0      // cash from day i-2, needed for cooldown

	for i := 1; i < len(prices); i++ {
		newHold := hold
		if prevCash-prices[i] > hold {
			newHold = prevCash - prices[i]
		}
		newCash := cash
		if hold+prices[i] > cash {
			newCash = hold + prices[i]
		}
		prevCash = cash
		hold = newHold
		cash = newCash
	}
	return cash
}
```

## Ruby

```ruby
def max_profit(prices)
  return 0 if prices.empty?
  cash = 0
  hold = -prices[0]
  prev_cash = 0
  (1...prices.length).each do |i|
    temp = cash
    cash = [cash, hold + prices[i]].max
    hold = [hold, prev_cash - prices[i]].max
    prev_cash = temp
  end
  cash
end
```

## Scala

```scala
object Solution {
    def maxProfit(prices: Array[Int]): Int = {
        if (prices.isEmpty) return 0
        var rest = 0
        var hold = -prices(0)
        var sold = Int.MinValue
        for (i <- 1 until prices.length) {
            val price = prices(i)
            val prevRest = rest
            val prevHold = hold
            val prevSold = sold
            rest = Math.max(prevRest, prevSold)
            hold = Math.max(prevHold, prevRest - price)
            sold = prevHold + price
        }
        Math.max(rest, sold)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.is_empty() {
            return 0;
        }
        let mut hold = -prices[0];
        let mut sold = std::i32::MIN / 2; // impossible state
        let mut rest = 0;
        for &p in prices.iter().skip(1) {
            let prev_hold = hold;
            let prev_sold = sold;
            let prev_rest = rest;
            hold = std::cmp::max(prev_hold, prev_rest - p);
            sold = prev_hold + p;
            rest = std::cmp::max(prev_rest, prev_sold);
        }
        std::cmp::max(sold, rest)
    }
}
```

## Racket

```racket
(define/contract (max-profit prices)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? prices)
      0
      (let* ((first-price (car prices))
             (rest-prices (cdr prices))
             (init-hold (- first-price))   ; profit when holding after day 0
             (init-cash 0)                ; profit when not holding and can buy
             (init-prev-cash 0))          ; profit two days ago (for cooldown)
        (let loop ((ps rest-prices)
                   (hold init-hold)
                   (cash init-cash)
                   (prev-cash init-prev-cash))
          (if (null? ps)
              cash
              (let* ((price (car ps))
                     (new-hold (max hold (- prev-cash price)))   ; buy today after cooldown
                     (new-cash (max cash (+ hold price))))      ; sell today or stay idle
                (loop (cdr ps) new-hold new-cash cash)))))))
```

## Erlang

```erlang
-spec max_profit([integer()]) -> integer().
max_profit([]) ->
    0;
max_profit([Price | Rest]) ->
    S0 = 0,
    S1 = -Price,
    NegInf = -1000000000,
    loop(Rest, S0, S1, NegInf).

loop([], S0, _S1, S2) ->
    max(S0, S2);
loop([Price | Rest], S0, S1, S2) ->
    NewS0 = max(S0, S2),
    NewS1 = max(S1, S0 - Price),
    NewS2 = S1 + Price,
    loop(Rest, NewS0, NewS1, NewS2).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit([]), do: 0

  def max_profit([first | rest]) do
    s0 = 0
    s1 = -first
    s2 = -1_000_000_000

    {s0, _s1, s2} =
      Enum.reduce(rest, {s0, s1, s2}, fn price, {prev_s0, prev_s1, prev_s2} ->
        new_s0 = max(prev_s0, prev_s2)
        new_s1 = max(prev_s1, prev_s0 - price)
        new_s2 = prev_s1 + price
        {new_s0, new_s1, new_s2}
      end)

    max(s0, s2)
  end
end
```

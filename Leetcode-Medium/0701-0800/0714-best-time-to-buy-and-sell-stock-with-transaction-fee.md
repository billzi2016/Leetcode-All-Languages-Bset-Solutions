# 0714. Best Time to Buy and Sell Stock with Transaction Fee

## Cpp

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        if (prices.empty()) return 0;
        long cash = 0;                 // profit when not holding a stock
        long hold = -prices[0];        // profit when holding a stock
        for (size_t i = 1; i < prices.size(); ++i) {
            long price = prices[i];
            long newCash = max(cash, hold + price - fee);
            long newHold = max(hold, cash - price);
            cash = newCash;
            hold = newHold;
        }
        return (int)cash;
    }
};
```

## Java

```java
class Solution {
    public int maxProfit(int[] prices, int fee) {
        if (prices == null || prices.length == 0) return 0;
        int cash = 0;                 // profit when not holding a stock
        int hold = -prices[0];        // profit when holding a stock
        for (int i = 1; i < prices.length; i++) {
            int price = prices[i];
            int newCash = Math.max(cash, hold + price - fee);
            int newHold = Math.max(hold, cash - price);
            cash = newCash;
            hold = newHold;
        }
        return cash;
    }
}
```

## Python

```python
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        cash = 0               # profit with no stock in hand
        hold = -prices[0]      # profit with a stock in hand (bought at day 0)
        for price in prices[1:]:
            prev_cash = cash
            cash = max(cash, hold + price - fee)   # sell today
            hold = max(hold, prev_cash - price)    # buy today
        return cash
```

## Python3

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash
```

## C

```c
int maxProfit(int* prices, int pricesSize, int fee) {
    if (pricesSize == 0) return 0;
    long cash = 0;
    long hold = -prices[0];
    for (int i = 1; i < pricesSize; ++i) {
        long prevCash = cash;
        long sell = hold + prices[i] - fee;
        cash = (cash > sell) ? cash : sell;
        long buy = prevCash - prices[i];
        hold = (hold > buy) ? hold : buy;
    }
    return (int)cash;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProfit(int[] prices, int fee) {
        if (prices == null || prices.Length == 0) return 0;
        long cash = 0;               // profit when not holding a stock
        long hold = -prices[0];      // profit when holding a stock
        foreach (int price in prices) {
            long prevCash = cash;
            cash = Math.Max(cash, hold + price - fee);
            hold = Math.Max(hold, prevCash - price);
        }
        return (int)cash;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function(prices, fee) {
    if (!prices || prices.length === 0) return 0;
    let cash = 0;                 // profit with no stock in hand
    let hold = -prices[0];        // profit with a stock bought at day 0
    
    for (let i = 1; i < prices.length; i++) {
        const price = prices[i];
        const newCash = Math.max(cash, hold + price - fee);
        const newHold = Math.max(hold, cash - price);
        cash = newCash;
        hold = newHold;
    }
    
    return cash;
};
```

## Typescript

```typescript
function maxProfit(prices: number[], fee: number): number {
    if (prices.length === 0) return 0;
    let cash = 0;               // profit when not holding a stock
    let hold = -prices[0];      // profit when holding a stock
    for (let i = 1; i < prices.length; i++) {
        const price = prices[i];
        const prevCash = cash;
        cash = Math.max(cash, hold + price - fee);
        hold = Math.max(hold, prevCash - price);
    }
    return cash;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @param Integer $fee
     * @return Integer
     */
    function maxProfit($prices, $fee) {
        $cash = 0;
        $hold = -$prices[0];
        foreach ($prices as $i => $price) {
            if ($i == 0) continue;
            $prevCash = $cash;
            $cash = max($cash, $hold + $price - $fee);
            $hold = max($hold, $prevCash - $price);
        }
        return $cash;
    }
}
```

## Swift

```swift
class Solution {
    func maxProfit(_ prices: [Int], _ fee: Int) -> Int {
        guard !prices.isEmpty else { return 0 }
        var cash = 0
        var hold = -prices[0]
        for i in 1..<prices.count {
            let price = prices[i]
            let newCash = max(cash, hold + price - fee)
            let newHold = max(hold, cash - price)
            cash = newCash
            hold = newHold
        }
        return cash
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(prices: IntArray, fee: Int): Int {
        var cash = 0
        var hold = -prices[0]
        for (i in 1 until prices.size) {
            val price = prices[i]
            val newCash = kotlin.math.max(cash, hold + price - fee)
            val newHold = kotlin.math.max(hold, cash - price)
            cash = newCash
            hold = newHold
        }
        return cash
    }
}
```

## Dart

```dart
class Solution {
  int maxProfit(List<int> prices, int fee) {
    if (prices.isEmpty) return 0;
    int cash = 0;
    int hold = -prices[0];
    for (int i = 1; i < prices.length; i++) {
      int price = prices[i];
      int newCash = cash > (hold + price - fee) ? cash : (hold + price - fee);
      int newHold = hold > (cash - price) ? hold : (cash - price);
      cash = newCash;
      hold = newHold;
    }
    return cash;
  }
}
```

## Golang

```go
func maxProfit(prices []int, fee int) int {
	if len(prices) == 0 {
		return 0
	}
	cash, hold := 0, -prices[0]
	for i := 1; i < len(prices); i++ {
		price := prices[i]
		newCash := cash
		if hold+price-fee > newCash {
			newCash = hold + price - fee
		}
		newHold := hold
		if cash-price > newHold {
			newHold = cash - price
		}
		cash, hold = newCash, newHold
	}
	return cash
}
```

## Ruby

```ruby
def max_profit(prices, fee)
  return 0 if prices.empty?
  cash = 0
  hold = -prices[0]
  prices.each do |price|
    prev_cash = cash
    cash = [cash, hold + price - fee].max
    hold = [hold, prev_cash - price].max
  end
  cash
end
```

## Scala

```scala
object Solution {
    def maxProfit(prices: Array[Int], fee: Int): Int = {
        if (prices.isEmpty) return 0
        var cash = 0               // profit with no stock in hand
        var hold = -prices(0)      // profit with a stock bought
        for (i <- 1 until prices.length) {
            val price = prices(i)
            val newCash = math.max(cash, hold + price - fee)
            val newHold = math.max(hold, cash - price)
            cash = newCash
            hold = newHold
        }
        cash
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        if prices.is_empty() {
            return 0;
        }
        let mut cash = 0i32;
        let mut hold = -prices[0];
        for &price in prices.iter().skip(1) {
            let new_cash = std::cmp::max(cash, hold + price - fee);
            let new_hold = std::cmp::max(hold, cash - price);
            cash = new_cash;
            hold = new_hold;
        }
        cash
    }
}
```

## Racket

```racket
(define/contract (max-profit prices fee)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (if (null? prices)
      0
      (let* ((first-price (car prices))
             (rest-prices (cdr prices)))
        (let loop ((cash 0) (hold (- first-price)) (ps rest-prices))
          (if (null? ps)
              cash
              (let* ((p (car ps))
                     (new-cash (max cash (+ hold p (- fee))))
                     (new-hold (max hold (- cash p))))
                (loop new-cash new-hold (cdr ps))))))))
```

## Erlang

```erlang
-spec max_profit(Prices :: [integer()], Fee :: integer()) -> integer().
max_profit(Prices, Fee) ->
    case Prices of
        [] -> 0;
        [First|Rest] ->
            {Cash,_Hold} = lists:foldl(
                fun(P, {C, H}) ->
                    NewCash = erlang:max(C, H + P - Fee),
                    NewHold = erlang:max(H, C - P),
                    {NewCash, NewHold}
                end,
                {0, -First},
                Rest
            ),
            Cash
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_profit(prices :: [integer], fee :: integer) :: integer
  def max_profit([], _fee), do: 0

  def max_profit([first | rest], fee) do
    {cash, _hold} =
      Enum.reduce(rest, {0, -first}, fn price, {cash, hold} ->
        new_cash = max(cash, hold + price - fee)
        new_hold = max(hold, cash - price)
        {new_cash, new_hold}
      end)

    cash
  end
end
```

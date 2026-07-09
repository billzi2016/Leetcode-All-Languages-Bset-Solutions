# 0123. Best Time to Buy and Sell Stock III

## Cpp

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        long firstBuy = LLONG_MIN, secondBuy = LLONG_MIN;
        long firstSell = 0, secondSell = 0;
        for (int p : prices) {
            firstBuy = max(firstBuy, -static_cast<long>(p));
            firstSell = max(firstSell, firstBuy + p);
            secondBuy = max(secondBuy, firstSell - static_cast<long>(p));
            secondSell = max(secondSell, secondBuy + p);
        }
        return static_cast<int>(secondSell);
    }
};
```

## Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) return 0;
        int firstBuy = Integer.MIN_VALUE;
        int firstSell = 0;
        int secondBuy = Integer.MIN_VALUE;
        int secondSell = 0;
        for (int price : prices) {
            firstBuy = Math.max(firstBuy, -price);
            firstSell = Math.max(firstSell, firstBuy + price);
            secondBuy = Math.max(secondBuy, firstSell - price);
            secondSell = Math.max(secondSell, secondBuy + price);
        }
        return secondSell;
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
        first_buy = -prices[0]
        first_sell = 0
        second_buy = -prices[0]
        second_sell = 0
        for p in prices[1:]:
            first_buy = max(first_buy, -p)
            first_sell = max(first_sell, first_buy + p)
            second_buy = max(second_buy, first_sell - p)
            second_sell = max(second_sell, second_buy + p)
        return second_sell
```

## Python3

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy = float('-inf')
        first_sell = 0
        second_buy = float('-inf')
        second_sell = 0

        for p in prices:
            first_buy = max(first_buy, -p)
            first_sell = max(first_sell, first_buy + p)
            second_buy = max(second_buy, first_sell - p)
            second_sell = max(second_sell, second_buy + p)

        return second_sell
```

## C

```c
int maxProfit(int* prices, int pricesSize) {
    if (pricesSize == 0) return 0;
    int firstBuy = -prices[0];
    int firstSell = 0;
    int secondBuy = -prices[0];
    int secondSell = 0;
    for (int i = 1; i < pricesSize; ++i) {
        int p = prices[i];
        if (-p > firstBuy) firstBuy = -p;
        if (firstBuy + p > firstSell) firstSell = firstBuy + p;
        if (firstSell - p > secondBuy) secondBuy = firstSell - p;
        if (secondBuy + p > secondSell) secondSell = secondBuy + p;
    }
    return secondSell;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxProfit(int[] prices)
    {
        if (prices == null || prices.Length == 0) return 0;

        int firstBuy = -prices[0];
        int firstSell = 0;
        int secondBuy = -prices[0];
        int secondSell = 0;

        foreach (int price in prices)
        {
            firstBuy = Math.Max(firstBuy, -price);
            firstSell = Math.Max(firstSell, firstBuy + price);
            secondBuy = Math.Max(secondBuy, firstSell - price);
            secondSell = Math.Max(secondSell, secondBuy + price);
        }

        return secondSell;
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
    if (!prices || prices.length === 0) return 0;
    let firstBuy = -Infinity, firstSell = 0;
    let secondBuy = -Infinity, secondSell = 0;
    for (let price of prices) {
        firstBuy = Math.max(firstBuy, -price);
        firstSell = Math.max(firstSell, firstBuy + price);
        secondBuy = Math.max(secondBuy, firstSell - price);
        secondSell = Math.max(secondSell, secondBuy + price);
    }
    return secondSell;
};
```

## Typescript

```typescript
function maxProfit(prices: number[]): number {
    if (prices.length === 0) return 0;
    let firstBuy = -Infinity;
    let firstSell = 0;
    let secondBuy = -Infinity;
    let secondSell = 0;

    for (const price of prices) {
        firstBuy = Math.max(firstBuy, -price);
        firstSell = Math.max(firstSell, firstBuy + price);
        secondBuy = Math.max(secondBuy, firstSell - price);
        secondSell = Math.max(secondSell, secondBuy + price);
    }

    return secondSell;
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
        $firstBuy = PHP_INT_MIN;
        $firstSell = 0;
        $secondBuy = PHP_INT_MIN;
        $secondSell = 0;

        foreach ($prices as $price) {
            $firstBuy = max($firstBuy, -$price);
            $firstSell = max($firstSell, $firstBuy + $price);
            $secondBuy = max($secondBuy, $firstSell - $price);
            $secondSell = max($secondSell, $secondBuy + $price);
        }

        return $secondSell;
    }
}
```

## Swift

```swift
class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var firstBuy = Int.min
        var firstSell = 0
        var secondBuy = Int.min
        var secondSell = 0
        
        for price in prices {
            firstBuy = max(firstBuy, -price)
            firstSell = max(firstSell, firstBuy + price)
            secondBuy = max(secondBuy, firstSell - price)
            secondSell = max(secondSell, secondBuy + price)
        }
        
        return secondSell
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(prices: IntArray): Int {
        if (prices.isEmpty()) return 0
        var firstBuy = -prices[0]
        var firstSell = 0
        var secondBuy = -prices[0]
        var secondSell = 0
        for (i in 1 until prices.size) {
            val price = prices[i]
            firstBuy = maxOf(firstBuy, -price)
            firstSell = maxOf(firstSell, firstBuy + price)
            secondBuy = maxOf(secondBuy, firstSell - price)
            secondSell = maxOf(secondSell, secondBuy + price)
        }
        return secondSell
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxProfit(List<int> prices) {
    if (prices.isEmpty) return 0;
    int firstBuy = -prices[0];
    int firstSell = 0;
    int secondBuy = -prices[0];
    int secondSell = 0;

    for (var price in prices) {
      firstBuy = max(firstBuy, -price);
      firstSell = max(firstSell, firstBuy + price);
      secondBuy = max(secondBuy, firstSell - price);
      secondSell = max(secondSell, secondBuy + price);
    }

    return secondSell;
  }
}
```

## Golang

```go
func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	firstBuy := -prices[0]
	firstSell := 0
	secondBuy := -prices[0]
	secondSell := 0

	for i := 1; i < len(prices); i++ {
		p := prices[i]

		if -p > firstBuy {
			firstBuy = -p
		}
		if firstBuy+p > firstSell {
			firstSell = firstBuy + p
		}
		if firstSell-p > secondBuy {
			secondBuy = firstSell - p
		}
		if secondBuy+p > secondSell {
			secondSell = secondBuy + p
		}
	}
	return secondSell
}
```

## Ruby

```ruby
def max_profit(prices)
  return 0 if prices.empty?
  first_buy = -Float::INFINITY
  first_sell = 0
  second_buy = -Float::INFINITY
  second_sell = 0

  prices.each do |price|
    first_buy = [first_buy, -price].max
    first_sell = [first_sell, first_buy + price].max
    second_buy = [second_buy, first_sell - price].max
    second_sell = [second_sell, second_buy + price].max
  end

  second_sell
end
```

## Scala

```scala
object Solution {
    def maxProfit(prices: Array[Int]): Int = {
        if (prices.isEmpty) return 0
        var firstBuy = -prices(0)
        var firstSell = 0
        var secondBuy = -prices(0)
        var secondSell = 0

        for (i <- 1 until prices.length) {
            val p = prices(i)
            firstBuy = math.max(firstBuy, -p)
            firstSell = math.max(firstSell, firstBuy + p)
            secondBuy = math.max(secondBuy, firstSell - p)
            secondSell = math.max(secondSell, secondBuy + p)
        }
        secondSell
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut buy1 = i32::MIN;
        let mut sell1 = 0;
        let mut buy2 = i32::MIN;
        let mut sell2 = 0;

        for p in prices {
            // Max profit after first purchase (spend money)
            buy1 = buy1.max(-p);
            // Max profit after first sale
            sell1 = sell1.max(buy1 + p);
            // Max profit after second purchase (use profit from first sale)
            buy2 = buy2.max(sell1 - p);
            // Max profit after second sale
            sell2 = sell2.max(buy2 + p);
        }

        sell2
    }
}
```

## Racket

```racket
(define/contract (max-profit prices)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length prices))
         (vec (list->vector prices)))
    (if (< n 2)
        0
        (let* ((fwd (make-vector n 0))
               (bwd (make-vector n 0)))
          ;; forward pass: max profit up to each day
          (let ((min-price (vector-ref vec 0)))
            (for ([i (in-range n)])
              (let ((price (vector-ref vec i)))
                (when (< price min-price) (set! min-price price))
                (define profit (- price min-price))
                (if (= i 0)
                    (vector-set! fwd i profit)
                    (vector-set! fwd i (max (vector-ref fwd (sub1 i)) profit))))))
          ;; backward pass: max profit from each day to the end
          (let ((max-price (vector-ref vec (sub1 n))))
            (vector-set! bwd (sub1 n) 0)
            (for ([i (in-range (sub1 n) -1 -1)])
              (let ((price (vector-ref vec i)))
                (when (> price max-price) (set! max-price price))
                (define profit (- max-price price))
                (if (= i (sub1 n))
                    (vector-set! bwd i profit)
                    (vector-set! bwd i (max (vector-ref bwd (add1 i)) profit))))))
          ;; combine the two passes
          (let ((ans 0))
            (for ([i (in-range n)])
              (set! ans (max ans (+ (vector-ref fwd i) (vector-ref bwd i)))))
            ans)))) )
```

## Erlang

```erlang
-spec max_profit(Prices :: [integer()]) -> integer().
max_profit(Prices) ->
    case Prices of
        [] -> 0;
        _ ->
            Init = {-1000000000, 0, -1000000000, 0},
            {_, _, _, SecondSell} = lists:foldl(
                fun(Price, {FirstBuy, FirstSell, SecondBuy, SecondSell}) ->
                    NewFirstBuy = erlang:max(FirstBuy, -Price),
                    NewFirstSell = erlang:max(FirstSell, NewFirstBuy + Price),
                    NewSecondBuy = erlang:max(SecondBuy, NewFirstSell - Price),
                    NewSecondSell = erlang:max(SecondSell, NewSecondBuy + Price),
                    {NewFirstBuy, NewFirstSell, NewSecondBuy, NewSecondSell}
                end,
                Init,
                Prices
            ),
            SecondSell
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit([]), do: 0

  def max_profit(prices) do
    {_, _, _, second_sell} =
      Enum.reduce(prices, {-1_000_000_000, 0, -1_000_000_000, 0}, fn price,
          {first_buy, first_sell, second_buy, second_sell} ->
        first_buy = max(first_buy, -price)
        first_sell = max(first_sell, first_buy + price)
        second_buy = max(second_buy, first_sell - price)
        second_sell = max(second_sell, second_buy + price)
        {first_buy, first_sell, second_buy, second_sell}
      end)

    second_sell
  end
end
```

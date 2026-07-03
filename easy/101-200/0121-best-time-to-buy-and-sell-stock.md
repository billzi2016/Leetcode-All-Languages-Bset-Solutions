# 0121. Best Time to Buy and Sell Stock

## Cpp

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxProf = 0;
        for (int price : prices) {
            if (price < minPrice) minPrice = price;
            else if (price - minPrice > maxProf) maxProf = price - minPrice;
        }
        return maxProf;
    }
};
```

## Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                int profit = price - minPrice;
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
            }
        }
        return maxProfit;
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
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = p - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
```

## Python3

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
```

## C

```c
#include <limits.h>

int maxProfit(int* prices, int pricesSize) {
    int min_price = INT_MAX;
    int max_profit = 0;
    for (int i = 0; i < pricesSize; ++i) {
        if (prices[i] < min_price) {
            min_price = prices[i];
        } else {
            int profit = prices[i] - min_price;
            if (profit > max_profit) {
                max_profit = profit;
            }
        }
    }
    return max_profit;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProfit(int[] prices) {
        int minPrice = int.MaxValue;
        int maxProfit = 0;
        foreach (int price in prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                int profit = price - minPrice;
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
            }
        }
        return maxProfit;
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
    let minPrice = Infinity;
    let best = 0;
    for (let p of prices) {
        if (p < minPrice) {
            minPrice = p;
        } else {
            const profit = p - minPrice;
            if (profit > best) best = profit;
        }
    }
    return best;
};
```

## Typescript

```typescript
function maxProfit(prices: number[]): number {
    let minPrice = Number.MAX_SAFE_INTEGER;
    let profit = 0;
    for (const price of prices) {
        if (price < minPrice) {
            minPrice = price;
        } else {
            const diff = price - minPrice;
            if (diff > profit) profit = diff;
        }
    }
    return profit;
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
        $minPrice = PHP_INT_MAX;
        $maxProfit = 0;
        foreach ($prices as $price) {
            if ($price < $minPrice) {
                $minPrice = $price;
            } else {
                $profit = $price - $minPrice;
                if ($profit > $maxProfit) {
                    $maxProfit = $profit;
                }
            }
        }
        return $maxProfit;
    }
}
```

## Swift

```swift
class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var minPrice = Int.max
        var maxProfit = 0
        for price in prices {
            if price < minPrice {
                minPrice = price
            } else {
                let profit = price - minPrice
                if profit > maxProfit {
                    maxProfit = profit
                }
            }
        }
        return maxProfit
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(prices: IntArray): Int {
        var minPrice = Int.MAX_VALUE
        var maxProfit = 0
        for (price in prices) {
            if (price < minPrice) {
                minPrice = price
            } else {
                val profit = price - minPrice
                if (profit > maxProfit) {
                    maxProfit = profit
                }
            }
        }
        return maxProfit
    }
}
```

## Dart

```dart
class Solution {
  int maxProfit(List<int> prices) {
    if (prices.isEmpty) return 0;
    int minPrice = prices[0];
    int maxProf = 0;
    for (int i = 1; i < prices.length; i++) {
      int profit = prices[i] - minPrice;
      if (profit > maxProf) maxProf = profit;
      if (prices[i] < minPrice) minPrice = prices[i];
    }
    return maxProf;
  }
}
```

## Golang

```go
func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	minPrice := prices[0]
	maxProf := 0
	for _, p := range prices[1:] {
		if diff := p - minPrice; diff > maxProf {
			maxProf = diff
		}
		if p < minPrice {
			minPrice = p
		}
	}
	return maxProf
}
```

## Ruby

```ruby
def max_profit(prices)
  min_price = Float::INFINITY
  max_profit = 0
  prices.each do |price|
    if price < min_price
      min_price = price
    else
      profit = price - min_price
      max_profit = profit if profit > max_profit
    end
  end
  max_profit
end
```

## Scala

```scala
object Solution {
    def maxProfit(prices: Array[Int]): Int = {
        var minPrice = Int.MaxValue
        var maxProfit = 0
        for (price <- prices) {
            if (price < minPrice) {
                minPrice = price
            } else {
                val profit = price - minPrice
                if (profit > maxProfit) maxProfit = profit
            }
        }
        maxProfit
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_price = i32::MAX;
        let mut max_profit = 0;
        for price in prices {
            if price < min_price {
                min_price = price;
            } else {
                let profit = price - min_price;
                if profit > max_profit {
                    max_profit = profit;
                }
            }
        }
        max_profit
    }
}
```

## Racket

```racket
(define/contract (max-profit prices)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? prices)
      0
      (let loop ((rest (cdr prices))
                 (min-price (car prices))
                 (best 0))
        (if (null? rest)
            best
            (let* ((price (car rest))
                   (new-min (if (< price min-price) price min-price))
                   (profit (- price new-min))
                   (new-best (if (> profit best) profit best)))
              (loop (cdr rest) new-min new-best))))))
```

## Erlang

```erlang
-spec max_profit(Prices :: [integer()]) -> integer().
max_profit([]) ->
    0;
max_profit([First|Rest] = Prices) ->
    {_, MaxProfit} = lists:foldl(
        fun(P, {MinSoFar, MaxSoFar}) ->
            NewMin = erlang:min(MinSoFar, P),
            Profit = P - MinSoFar,
            NewMax = erlang:max(MaxSoFar, Profit),
            {NewMin, NewMax}
        end,
        {First, 0},
        Prices
    ),
    MaxProfit.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit([]), do: 0

  def max_profit([head | tail]) do
    {_min_price, profit} =
      Enum.reduce(tail, {head, 0}, fn price, {min_price, max_profit} ->
        new_min = min(min_price, price)
        new_max = max(max_profit, price - min_price)
        {new_min, new_max}
      end)

    profit
  end
end
```

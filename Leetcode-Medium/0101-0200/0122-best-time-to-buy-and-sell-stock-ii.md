# 0122. Best Time to Buy and Sell Stock II

## Cpp

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for (size_t i = 1; i < prices.size(); ++i) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
        }
        return profit;
    }
};
```

## Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            int diff = prices[i] - prices[i - 1];
            if (diff > 0) {
                profit += diff;
            }
        }
        return profit;
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
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        return profit
```

## Python3

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        return profit
```

## C

```c
int maxProfit(int* prices, int pricesSize) {
    int profit = 0;
    for (int i = 1; i < pricesSize; ++i) {
        if (prices[i] > prices[i - 1]) {
            profit += prices[i] - prices[i - 1];
        }
    }
    return profit;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxProfit(int[] prices)
    {
        if (prices == null || prices.Length < 2) return 0;
        int profit = 0;
        for (int i = 1; i < prices.Length; i++)
        {
            int diff = prices[i] - prices[i - 1];
            if (diff > 0) profit += diff;
        }
        return profit;
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
    let profit = 0;
    for (let i = 1; i < prices.length; i++) {
        const diff = prices[i] - prices[i - 1];
        if (diff > 0) profit += diff;
    }
    return profit;
};
```

## Typescript

```typescript
function maxProfit(prices: number[]): number {
    let profit = 0;
    for (let i = 1; i < prices.length; i++) {
        const diff = prices[i] - prices[i - 1];
        if (diff > 0) profit += diff;
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
        $profit = 0;
        $n = count($prices);
        for ($i = 1; $i < $n; $i++) {
            if ($prices[$i] > $prices[$i - 1]) {
                $profit += $prices[$i] - $prices[$i - 1];
            }
        }
        return $profit;
    }
}
```

## Swift

```swift
class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var profit = 0
        for i in 1..<prices.count {
            let diff = prices[i] - prices[i - 1]
            if diff > 0 {
                profit += diff
            }
        }
        return profit
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(prices: IntArray): Int {
        var profit = 0
        for (i in 1 until prices.size) {
            val diff = prices[i] - prices[i - 1]
            if (diff > 0) profit += diff
        }
        return profit
    }
}
```

## Dart

```dart
class Solution {
  int maxProfit(List<int> prices) {
    int profit = 0;
    for (int i = 1; i < prices.length; i++) {
      if (prices[i] > prices[i - 1]) {
        profit += prices[i] - prices[i - 1];
      }
    }
    return profit;
  }
}
```

## Golang

```go
func maxProfit(prices []int) int {
    profit := 0
    for i := 1; i < len(prices); i++ {
        if prices[i] > prices[i-1] {
            profit += prices[i] - prices[i-1]
        }
    }
    return profit
}
```

## Ruby

```ruby
def max_profit(prices)
  profit = 0
  (1...prices.length).each do |i|
    diff = prices[i] - prices[i - 1]
    profit += diff if diff > 0
  end
  profit
end
```

## Scala

```scala
object Solution {
    def maxProfit(prices: Array[Int]): Int = {
        var profit = 0
        for (i <- 1 until prices.length) {
            val diff = prices(i) - prices(i - 1)
            if (diff > 0) profit += diff
        }
        profit
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        for i in 1..prices.len() {
            if prices[i] > prices[i - 1] {
                profit += prices[i] - prices[i - 1];
            }
        }
        profit
    }
}
```

## Racket

```racket
(define/contract (max-profit prices)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst prices) (prev #f) (profit 0))
    (if (null? lst)
        profit
        (if prev
            (let* ((curr (car lst))
                   (diff (- curr prev)))
              (loop (cdr lst) curr (+ profit (if (> diff 0) diff 0))))
            (loop (cdr lst) (car lst) profit)))))
```

## Erlang

```erlang
-spec max_profit(Prices :: [integer()]) -> integer().
max_profit([]) ->
    0;
max_profit([_]) ->
    0;
max_profit([First | Rest]) ->
    {_Last, Profit} = lists:foldl(
        fun(Curr, {Prev, Acc}) ->
            if
                Curr > Prev -> {Curr, Acc + (Curr - Prev)};
                true       -> {Curr, Acc}
            end
        end,
        {First, 0},
        Rest),
    Profit.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit(prices) do
    {profit, _} =
      Enum.reduce(prices, {0, nil}, fn price, {acc, prev} ->
        case prev do
          nil -> {acc, price}
          _ ->
            diff = price - prev
            new_acc = if diff > 0, do: acc + diff, else: acc
            {new_acc, price}
        end
      end)

    profit
  end
end
```

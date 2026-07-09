# 2706. Buy Two Chocolates

## Cpp

```cpp
class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int min1 = INT_MAX, min2 = INT_MAX;
        for (int p : prices) {
            if (p < min1) {
                min2 = min1;
                min1 = p;
            } else if (p < min2) {
                min2 = p;
            }
        }
        int cost = min1 + min2;
        return (cost <= money) ? money - cost : money;
    }
};
```

## Java

```java
class Solution {
    public int buyChoco(int[] prices, int money) {
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;
        for (int price : prices) {
            if (price <= min1) {
                min2 = min1;
                min1 = price;
            } else if (price < min2) {
                min2 = price;
            }
        }
        int sum = min1 + min2;
        return sum <= money ? money - sum : money;
    }
}
```

## Python

```python
class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        cost = prices[0] + prices[1]
        return money - cost if cost <= money else money
```

## Python3

```python
from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Find the two cheapest chocolates
        if len(prices) < 2:
            return money
        # Sorting is fine given small constraints
        prices.sort()
        min_cost = prices[0] + prices[1]
        return money - min_cost if min_cost <= money else money
```

## C

```c
#include <limits.h>

int buyChoco(int* prices, int pricesSize, int money) {
    int min1 = INT_MAX, min2 = INT_MAX;
    for (int i = 0; i < pricesSize; ++i) {
        int p = prices[i];
        if (p <= min1) {
            min2 = min1;
            min1 = p;
        } else if (p < min2) {
            min2 = p;
        }
    }
    int sum = min1 + min2;
    return (sum <= money) ? (money - sum) : money;
}
```

## Csharp

```csharp
public class Solution {
    public int BuyChoco(int[] prices, int money) {
        System.Array.Sort(prices);
        int minCost = prices[0] + prices[1];
        return minCost <= money ? money - minCost : money;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}
 */
var buyChoco = function(prices, money) {
    prices.sort((a, b) => a - b);
    const minCost = prices[0] + prices[1];
    return minCost <= money ? money - minCost : money;
};
```

## Typescript

```typescript
function buyChoco(prices: number[], money: number): number {
    prices.sort((a, b) => a - b);
    const cost = prices[0] + prices[1];
    return cost <= money ? money - cost : money;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer[] $prices
     * @param Integer $money
     * @return Integer
     */
    function buyChoco($prices, $money) {
        sort($prices);
        $minCost = $prices[0] + $prices[1];
        if ($minCost <= $money) {
            return $money - $minCost;
        }
        return $money;
    }
}
?>
```

## Swift

```swift
class Solution {
    func buyChoco(_ prices: [Int], _ money: Int) -> Int {
        let sorted = prices.sorted()
        let cost = sorted[0] + sorted[1]
        return cost <= money ? money - cost : money
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun buyChoco(prices: IntArray, money: Int): Int {
        var min1 = Int.MAX_VALUE
        var min2 = Int.MAX_VALUE
        for (p in prices) {
            if (p < min1) {
                min2 = min1
                min1 = p
            } else if (p < min2) {
                min2 = p
            }
        }
        val cost = min1 + min2
        return if (cost <= money) money - cost else money
    }
}
```

## Dart

```dart
class Solution {
  int buyChoco(List<int> prices, int money) {
    prices.sort();
    int minCost = prices[0] + prices[1];
    return (minCost <= money) ? money - minCost : money;
  }
}
```

## Golang

```go
package main

import "sort"

func buyChoco(prices []int, money int) int {
	sort.Ints(prices)
	minCost := prices[0] + prices[1]
	if minCost <= money {
		return money - minCost
	}
	return money
}
```

## Ruby

```ruby
# @param {Integer[]} prices
# @param {Integer} money
# @return {Integer}
def buy_choco(prices, money)
  # Initialize the two smallest values using the first two elements
  if prices[0] <= prices[1]
    min1 = prices[0]
    min2 = prices[1]
  else
    min1 = prices[1]
    min2 = prices[0]
  end

  # Scan remaining elements to maintain the smallest and second smallest
  i = 2
  while i < prices.length
    p = prices[i]
    if p < min1
      min2 = min1
      min1 = p
    elsif p < min2
      min2 = p
    end
    i += 1
  end

  cost = min1 + min2
  cost <= money ? money - cost : money
end
```

## Scala

```scala
object Solution {
    def buyChoco(prices: Array[Int], money: Int): Int = {
        val sorted = prices.sorted
        val cost = sorted(0) + sorted(1)
        if (cost <= money) money - cost else money
    }
}
```

## Rust

```rust
impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        let mut sorted = prices;
        sorted.sort_unstable();
        let cost = sorted[0] + sorted[1];
        if cost <= money { money - cost } else { money }
    }
}
```

## Racket

```racket
(define/contract (buy-choco prices money)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort prices <))
         (min-sum (+ (list-ref sorted 0) (list-ref sorted 1))))
    (if (<= min-sum money)
        (- money min-sum)
        money)))
```

## Erlang

```erlang
-spec buy_choco(Prices :: [integer()], Money :: integer()) -> integer().
buy_choco(Prices, Money) ->
    Sorted = lists:sort(Prices),
    case Sorted of
        [A, B | _] ->
            Cost = A + B,
            if Cost =< Money -> Money - Cost;
               true -> Money
            end;
        _ -> Money
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec buy_choco(prices :: [integer], money :: integer) :: integer
  def buy_choco(prices, money) do
    [a, b | rest] = prices

    {min1, min2} =
      if a <= b do
        {a, b}
      else
        {b, a}
      end

    {min1, min2} =
      Enum.reduce(rest, {min1, min2}, fn price, {m1, m2} ->
        cond do
          price < m1 -> {price, m1}
          price < m2 -> {m1, price}
          true -> {m1, m2}
        end
      end)

    total = min1 + min2

    if total <= money, do: money - total, else: money
  end
end
```

# 1833. Maximum Ice Cream Bars

## Cpp

```cpp
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        const int MAXC = 100000;
        vector<int> freq(MAXC + 1, 0);
        for (int c : costs) ++freq[c];
        int bought = 0;
        for (int price = 1; price <= MAXC && coins >= price; ++price) {
            if (!freq[price]) continue;
            long long canBuy = min<long long>(freq[price], coins / price);
            bought += static_cast<int>(canBuy);
            coins -= static_cast<int>(canBuy * price);
        }
        return bought;
    }
};
```

## Java

```java
class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int max = 0;
        for (int c : costs) {
            if (c > max) max = c;
        }
        int[] count = new int[max + 1];
        for (int c : costs) {
            count[c]++;
        }
        int bought = 0;
        for (int price = 1; price <= max && coins >= price; price++) {
            if (count[price] == 0) continue;
            int canBuy = Math.min(count[price], coins / price);
            bought += canBuy;
            coins -= canBuy * price;
        }
        return bought;
    }
}
```

## Python

```python
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if not costs:
            return 0
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1

        bought = 0
        remaining = coins
        for price in range(1, max_cost + 1):
            if freq[price] == 0 or remaining < price:
                continue
            # maximum number we can afford at this price
            can_buy = min(freq[price], remaining // price)
            bought += can_buy
            remaining -= can_buy * price
            if remaining < price:
                break
        return bought
```

## Python3

```python
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1

        bought = 0
        remaining = coins
        for price in range(1, max_cost + 1):
            if freq[price] == 0 or remaining < price:
                continue
            can_buy = min(freq[price], remaining // price)
            bought += can_buy
            remaining -= can_buy * price
            if remaining < price:
                # No need to continue if we can't afford this price,
                # but cheaper prices have already been processed.
                break
        return bought
```

## C

```c
#include <string.h>

int maxIceCream(int* costs, int costsSize, int coins) {
    const int MAX_COST = 100000;
    static int freq[100001];
    memset(freq, 0, sizeof(freq));
    
    for (int i = 0; i < costsSize; ++i) {
        ++freq[costs[i]];
    }
    
    long long remaining = coins;
    int count = 0;
    
    for (int price = 1; price <= MAX_COST && remaining > 0; ++price) {
        if (freq[price] == 0) continue;
        long long canBuy = remaining / price;
        if (canBuy == 0) break;
        if ((long long)freq[price] <= canBuy) {
            count += freq[price];
            remaining -= (long long)freq[price] * price;
        } else {
            count += (int)canBuy;
            break;
        }
    }
    
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxIceCream(int[] costs, int coins) {
        const int MAX_COST = 100000;
        int[] freq = new int[MAX_COST + 1];
        foreach (int c in costs) {
            freq[c]++;
        }
        int bought = 0;
        for (int price = 1; price <= MAX_COST && coins >= price; price++) {
            if (freq[price] == 0) continue;
            int maxCanBuy = coins / price;
            int take = Math.Min(freq[price], maxCanBuy);
            bought += take;
            coins -= take * price;
        }
        return bought;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} costs
 * @param {number} coins
 * @return {number}
 */
var maxIceCream = function(costs, coins) {
    const MAX_COST = 100000;
    const freq = new Uint32Array(MAX_COST + 1);
    for (let c of costs) {
        freq[c]++;
    }
    let bought = 0;
    for (let price = 1; price <= MAX_COST && coins > 0; price++) {
        const cnt = freq[price];
        if (!cnt) continue;
        const canBuy = Math.min(cnt, Math.floor(coins / price));
        bought += canBuy;
        coins -= canBuy * price;
    }
    return bought;
};
```

## Typescript

```typescript
function maxIceCream(costs: number[], coins: number): number {
    const MAX_COST = 100000;
    const freq = new Uint32Array(MAX_COST + 1);
    for (const c of costs) {
        freq[c]++;
    }
    let bought = 0;
    for (let price = 1; price <= MAX_COST && coins >= price; price++) {
        const available = freq[price];
        if (!available) continue;
        const canBuy = Math.min(available, Math.floor(coins / price));
        bought += canBuy;
        coins -= canBuy * price;
    }
    return bought;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $costs
     * @param Integer $coins
     * @return Integer
     */
    function maxIceCream($costs, $coins) {
        $maxCost = 100000;
        $freq = array_fill(0, $maxCost + 1, 0);
        foreach ($costs as $c) {
            $freq[$c]++;
        }

        $count = 0;
        for ($price = 1; $price <= $maxCost && $coins > 0; $price++) {
            if ($freq[$price] == 0) continue;
            $canBuy = intdiv($coins, $price);
            if ($canBuy == 0) break;
            $take = min($freq[$price], $canBuy);
            $count += $take;
            $coins -= $take * $price;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func maxIceCream(_ costs: [Int], _ coins: Int) -> Int {
        var maxCost = 0
        for c in costs {
            if c > maxCost { maxCost = c }
        }
        var freq = [Int](repeating: 0, count: maxCost + 1)
        for c in costs {
            freq[c] += 1
        }
        var remaining = coins
        var bought = 0
        var price = 1
        while price <= maxCost && remaining >= price {
            let cnt = freq[price]
            if cnt > 0 {
                let canBuy = min(cnt, remaining / price)
                bought += canBuy
                remaining -= canBuy * price
            }
            price += 1
        }
        return bought
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxIceCream(costs: IntArray, coins: Int): Int {
        val maxCost = 100000
        val freq = IntArray(maxCost + 1)
        for (c in costs) {
            freq[c]++
        }
        var remaining = coins.toLong()
        var count = 0
        var price = 1
        while (price <= maxCost && remaining > 0) {
            val cnt = freq[price]
            if (cnt == 0) {
                price++
                continue
            }
            val canBuy = (remaining / price).toInt()
            if (canBuy >= cnt) {
                count += cnt
                remaining -= cnt.toLong() * price
            } else {
                count += canBuy
                break
            }
            price++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int maxIceCream(List<int> costs, int coins) {
    const int MAX_COST = 100000;
    List<int> freq = List.filled(MAX_COST + 1, 0);
    for (int c in costs) {
      freq[c]++;
    }
    int count = 0;
    for (int price = 1; price <= MAX_COST && coins > 0; price++) {
      int available = freq[price];
      if (available == 0) continue;
      int canBuy = coins ~/ price;
      int take = available < canBuy ? available : canBuy;
      count += take;
      coins -= take * price;
    }
    return count;
  }
}
```

## Golang

```go
func maxIceCream(costs []int, coins int) int {
	const maxCost = 100000
	freq := make([]int, maxCost+1)
	for _, c := range costs {
		freq[c]++
	}
	count := 0
	remaining := coins
	for price := 1; price <= maxCost && remaining > 0; price++ {
		if freq[price] == 0 {
			continue
		}
		maxBuy := remaining / price
		if maxBuy >= freq[price] {
			count += freq[price]
			remaining -= price * freq[price]
		} else {
			count += maxBuy
			break
		}
	}
	return count
}
```

## Ruby

```ruby
def max_ice_cream(costs, coins)
  max_price = costs.max
  freq = Array.new(max_price + 1, 0)
  costs.each { |c| freq[c] += 1 }

  count = 0
  price = 1
  while price <= max_price && coins > 0
    if freq[price] > 0
      can_buy = [freq[price], coins / price].min
      count += can_buy
      coins -= can_buy * price
    end
    price += 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def maxIceCream(costs: Array[Int], coins: Int): Int = {
        val maxCost = 100000
        val freq = new Array[Int](maxCost + 1)
        for (c <- costs) {
            freq(c) += 1
        }
        var remaining = coins
        var count = 0
        var price = 1
        while (price <= maxCost && remaining >= price) {
            val f = freq(price)
            if (f > 0) {
                val canBuy = Math.min(f, remaining / price)
                count += canBuy
                remaining -= canBuy * price
            }
            price += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_ice_cream(costs: Vec<i32>, coins: i32) -> i32 {
        const MAX_COST: usize = 100_000;
        let mut freq = vec![0usize; MAX_COST + 1];
        for c in costs {
            freq[c as usize] += 1;
        }
        let mut remaining = coins;
        let mut bought = 0i32;
        for price in 1..=MAX_COST {
            if remaining < price as i32 {
                break;
            }
            let available = freq[price];
            if available == 0 {
                continue;
            }
            let can_afford = (remaining / price as i32) as usize;
            let take = std::cmp::min(available, can_afford);
            bought += take as i32;
            remaining -= (take * price) as i32;
        }
        bought
    }
}
```

## Racket

```racket
(define/contract (max-ice-cream costs coins)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([max-cost 100000]
         [freq (make-vector (+ max-cost 1) 0)])
    ;; Count frequencies of each cost
    (for ([c costs])
      (vector-set! freq c (+ 1 (vector-ref freq c))))
    ;; Greedily buy from cheapest to most expensive
    (let loop ((price 1)
               (remaining coins)
               (cnt 0))
      (cond
        [(or (> price max-cost) (= remaining 0)) cnt]
        [else
         (define avail (vector-ref freq price))
         (if (and (> avail 0) (>= remaining price))
             (let* ([max-buy (quotient remaining price)]
                    [buy (min avail max-buy)])
               (loop (+ price 1)
                     (- remaining (* buy price))
                     (+ cnt buy)))
             (loop (+ price 1) remaining cnt))]))))
```

## Erlang

```erlang
-module(solution).
-export([max_ice_cream/2]).

-spec max_ice_cream(Costs :: [integer()], Coins :: integer()) -> integer().
max_ice_cream(Costs, Coins) ->
    MaxCost = 100000,
    FreqMap = build_freq(Costs, #{}),
    buy(FreqMap, 1, MaxCost, Coins, 0).

build_freq([], Map) -> Map;
build_freq([H|T], Map) ->
    NewMap = maps:update_with(H, fun(V) -> V + 1 end, 1, Map),
    build_freq(T, NewMap).

buy(_Map, _Cost, _MaxCost, Coins, Count) when Coins =< 0 ->
    Count;
buy(Map, Cost, MaxCost, Coins, Count) when Cost > MaxCost ->
    Count;
buy(Map, Cost, MaxCost, Coins, Count) ->
    case maps:get(Cost, Map, 0) of
        0 -> buy(Map, Cost + 1, MaxCost, Coins, Count);
        Cnt ->
            MaxCanBuy = erlang:min(Cnt, Coins div Cost),
            NewCoins = Coins - MaxCanBuy * Cost,
            NewCount = Count + MaxCanBuy,
            if NewCoins =:= 0 -> NewCount;
               true -> buy(Map, Cost + 1, MaxCost, NewCoins, NewCount)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_ice_cream(costs :: [integer], coins :: integer) :: integer
  def max_ice_cream(costs, coins) do
    max_cost = Enum.max(costs)

    counts =
      Enum.reduce(costs, :array.new(max_cost + 1, 0), fn cost, acc ->
        current = :array.get(cost, acc)
        :array.set(cost, current + 1, acc)
      end)

    {_remaining, total} =
      Enum.reduce_while(1..max_cost, {coins, 0}, fn price, {c, tot} ->
        if c < price do
          {:halt, {c, tot}}
        else
          cnt = :array.get(price, counts)

          if cnt == 0 do
            {:cont, {c, tot}}
          else
            max_can_buy = div(c, price)
            buy = if cnt < max_can_buy, do: cnt, else: max_can_buy
            new_c = c - buy * price
            {:cont, {new_c, tot + buy}}
          end
        end
      end)

    total
  end
end
```

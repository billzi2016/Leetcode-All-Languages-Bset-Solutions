# 2110. Number of Smooth Descent Periods of a Stock

## Cpp

```cpp
class Solution {
public:
    long long getDescentPeriods(std::vector<int>& prices) {
        long long ans = 0;
        long long curLen = 0;
        for (size_t i = 0; i < prices.size(); ++i) {
            if (i > 0 && prices[i - 1] - prices[i] == 1) {
                ++curLen;
            } else {
                curLen = 1;
            }
            ans += curLen;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long getDescentPeriods(int[] prices) {
        long total = 0;
        long curLen = 1; // length of current smooth descent period
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] == prices[i - 1] - 1) {
                curLen++;
            } else {
                total += curLen * (curLen + 1) / 2;
                curLen = 1;
            }
        }
        total += curLen * (curLen + 1) / 2; // add the last segment
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        cur_len = 0
        prev = None
        for price in prices:
            if prev is not None and prev - price == 1:
                cur_len += 1
            else:
                cur_len = 1
            total += cur_len
            prev = price
        return total
```

## Python3

```python
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 0
        cur_len = 0
        prev = None
        for p in prices:
            if prev is not None and prev - p == 1:
                cur_len += 1
            else:
                cur_len = 1
            total += cur_len
            prev = p
        return total
```

## C

```c
long long getDescentPeriods(int* prices, int pricesSize) {
    long long total = 0;
    long long curLen = 0;
    for (int i = 0; i < pricesSize; ++i) {
        if (i > 0 && prices[i] == prices[i - 1] - 1) {
            ++curLen;
        } else {
            curLen = 1;
        }
        total += curLen;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public long GetDescentPeriods(int[] prices) {
        long total = 0;
        long curLen = 1;
        for (int i = 1; i < prices.Length; i++) {
            if (prices[i] == prices[i - 1] - 1) {
                curLen++;
            } else {
                total += curLen * (curLen + 1) / 2;
                curLen = 1;
            }
        }
        total += curLen * (curLen + 1) / 2;
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var getDescentPeriods = function(prices) {
    let total = 0;
    let curLen = 0;
    for (let i = 0; i < prices.length; i++) {
        if (i > 0 && prices[i - 1] - prices[i] === 1) {
            curLen += 1;
        } else {
            curLen = 1;
        }
        total += curLen;
    }
    return total;
};
```

## Typescript

```typescript
function getDescentPeriods(prices: number[]): number {
    let total = 0;
    let curLen = 0;
    for (let i = 0; i < prices.length; ++i) {
        if (i > 0 && prices[i - 1] - prices[i] === 1) {
            curLen += 1;
        } else {
            curLen = 1;
        }
        total += curLen;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function getDescentPeriods($prices) {
        $n = count($prices);
        $ans = 0;
        $len = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i > 0 && $prices[$i - 1] - $prices[$i] == 1) {
                $len++;
            } else {
                $len = 1;
            }
            $ans += $len;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func getDescentPeriods(_ prices: [Int]) -> Int {
        var total = 0
        var currentLength = 0
        for i in 0..<prices.count {
            if i > 0 && prices[i - 1] - prices[i] == 1 {
                currentLength += 1
            } else {
                currentLength = 1
            }
            total += currentLength
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getDescentPeriods(prices: IntArray): Long {
        var total = 0L
        var length = 0L
        for (i in prices.indices) {
            if (i > 0 && prices[i - 1] - prices[i] == 1) {
                length += 1
            } else {
                length = 1
            }
            total += length
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int getDescentPeriods(List<int> prices) {
    int n = prices.length;
    int curLen = 1;
    int total = 0;
    for (int i = 1; i < n; ++i) {
      if (prices[i] == prices[i - 1] - 1) {
        curLen++;
      } else {
        total += curLen * (curLen + 1) ~/ 2;
        curLen = 1;
      }
    }
    total += curLen * (curLen + 1) ~/ 2;
    return total;
  }
}
```

## Golang

```go
func getDescentPeriods(prices []int) int64 {
    var total int64
    var cur int64 = 1
    n := len(prices)
    if n == 0 {
        return 0
    }
    total = 1 // first element
    for i := 1; i < n; i++ {
        if prices[i] == prices[i-1]-1 {
            cur++
        } else {
            cur = 1
        }
        total += cur
    }
    return total
}
```

## Ruby

```ruby
def get_descent_periods(prices)
  total = 0
  cur_len = 0
  prices.each_with_index do |price, i|
    if i > 0 && price == prices[i - 1] - 1
      cur_len += 1
    else
      cur_len = 1
    end
    total += cur_len
  end
  total
end
```

## Scala

```scala
object Solution {
    def getDescentPeriods(prices: Array[Int]): Long = {
        var total: Long = 0L
        var curLen: Long = 0L
        for (i <- prices.indices) {
            if (i > 0 && prices(i - 1) - prices(i) == 1) {
                curLen += 1
            } else {
                curLen = 1
            }
            total += curLen
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        let mut total: i64 = 0;
        let mut current_len: i64 = 0;
        let mut prev: Option<i32> = None;

        for price in prices {
            if let Some(p) = prev {
                if p - price == 1 {
                    current_len += 1;
                } else {
                    current_len = 1;
                }
            } else {
                current_len = 1;
            }
            total += current_len;
            prev = Some(price);
        }

        total
    }
}
```

## Racket

```racket
(define/contract (get-descent-periods prices)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? prices)
      0
      (let-values ([( _ _ total)]
                   (for/fold ([prev #f] [cur 0] [ans 0])
                             ([x prices])
                     (if (and prev (= (- prev x) 1))
                         (values x (+ cur 1) (+ ans (+ cur 1)))
                         (values x 1 (+ ans 1)))))
        total)))
```

## Erlang

```erlang
-module(solution).
-export([get_descent_periods/1]).

-spec get_descent_periods(Prices :: [integer()]) -> integer().
get_descent_periods([]) -> 
    0;
get_descent_periods([H|T]) ->
    go(T, H, 1, 1).

go([], _Prev, _CurLen, Acc) ->
    Acc;
go([X|Rest], Prev, CurLen, Acc) ->
    case X =:= Prev - 1 of
        true ->
            NewLen = CurLen + 1,
            go(Rest, X, NewLen, Acc + NewLen);
        false ->
            go(Rest, X, 1, Acc + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_descent_periods(prices :: [integer]) :: integer
  def get_descent_periods(prices) do
    case prices do
      [] -> 0
      [first | rest] ->
        {_, _, total} = Enum.reduce(rest, {first, 1, 1}, fn price, {prev, cur_len, acc} ->
          if prev - price == 1 do
            new_len = cur_len + 1
            {price, new_len, acc + new_len}
          else
            {price, 1, acc + 1}
          end
        end)

        total
    end
  end
end
```

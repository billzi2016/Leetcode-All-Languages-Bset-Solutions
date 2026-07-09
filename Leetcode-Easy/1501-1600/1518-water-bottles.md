# 1518. Water Bottles

## Cpp

```cpp
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int total = numBottles;
        int empties = numBottles;
        while (empties >= numExchange) {
            int newFull = empties / numExchange;
            total += newFull;
            empties = empties % numExchange + newFull;
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        // Using the mathematical shortcut:
        // Each exchange consumes (numExchange - 1) bottles net.
        // The total drinks = initial + extra obtained from exchanges.
        return numBottles + (numBottles - 1) / (numExchange - 1);
    }
}
```

## Python

```python
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # Using the derived formula:
        # total = initial bottles + extra bottles obtained from exchanges.
        # Each exchange consumes (numExchange - 1) net empty bottles because one bottle is returned as full.
        return numBottles + (numBottles - 1) // (numExchange - 1)
```

## Python3

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Using the derived formula: total = initial bottles + (initial - 1) // (exchange - 1)
        return numBottles + (numBottles - 1) // (numExchange - 1)
```

## C

```c
int numWaterBottles(int numBottles, int numExchange) {
    return numBottles + (numBottles - 1) / (numExchange - 1);
}
```

## Csharp

```csharp
public class Solution
{
    public int NumWaterBottles(int numBottles, int numExchange)
    {
        // Each exchange effectively consumes (numExchange - 1) bottles to gain one more drink.
        // The total drinks = initial bottles + extra drinks obtained from exchanges.
        return numBottles + (numBottles - 1) / (numExchange - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    // Using the derived formula: total = initial + floor((initial - 1) / (exchange - 1))
    return numBottles + Math.floor((numBottles - 1) / (numExchange - 1));
};
```

## Typescript

```typescript
function numWaterBottles(numBottles: number, numExchange: number): number {
    let total = 0;
    let empty = 0;
    while (numBottles > 0) {
        total += numBottles;
        empty += numBottles;
        numBottles = Math.floor(empty / numExchange);
        empty = empty % numExchange;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numBottles
     * @param Integer $numExchange
     * @return Integer
     */
    function numWaterBottles($numBottles, $numExchange) {
        $drank = 0;
        while ($numBottles >= $numExchange) {
            $exchange = intdiv($numBottles, $numExchange);
            $drank += $exchange * $numExchange;
            $numBottles = $numBottles % $numExchange + $exchange;
        }
        return $drank + $numBottles;
    }
}
```

## Swift

```swift
class Solution {
    func numWaterBottles(_ numBottles: Int, _ numExchange: Int) -> Int {
        var total = numBottles
        var empty = numBottles
        while empty >= numExchange {
            let newFull = empty / numExchange
            total += newFull
            empty = newFull + (empty % numExchange)
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numWaterBottles(numBottles: Int, numExchange: Int): Int {
        // Using the derived formula: total = initial + (initial - 1) / (exchange - 1)
        return numBottles + (numBottles - 1) / (numExchange - 1)
    }
}
```

## Dart

```dart
class Solution {
  int numWaterBottles(int numBottles, int numExchange) {
    return numBottles + (numBottles - 1) ~/ (numExchange - 1);
  }
}
```

## Golang

```go
func numWaterBottles(numBottles int, numExchange int) int {
	total := numBottles
	empty := numBottles
	for empty >= numExchange {
		exchange := empty / numExchange
		total += exchange
		empty = exchange + (empty % numExchange)
	}
	return total
}
```

## Ruby

```ruby
# @param {Integer} num_bottles
# @param {Integer} num_exchange
# @return {Integer}
def num_water_bottles(num_bottles, num_exchange)
  return num_bottles if num_exchange <= 1
  num_bottles + (num_bottles - 1) / (num_exchange - 1)
end
```

## Scala

```scala
object Solution {
    def numWaterBottles(numBottles: Int, numExchange: Int): Int = {
        var total = numBottles
        var empty = numBottles
        while (empty >= numExchange) {
            val exchange = empty / numExchange
            total += exchange
            empty = exchange + (empty % numExchange)
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut total = num_bottles;
        let mut empty = num_bottles;
        while empty >= num_exchange {
            let exchange = empty / num_exchange;
            total += exchange;
            empty = exchange + (empty % num_exchange);
        }
        total
    }
}
```

## Racket

```racket
#lang racket

(provide num-water-bottles)

(define/contract (num-water-bottles numBottles numExchange)
  (-> exact-integer? exact-integer? exact-integer?)
  (+ numBottles
     (quotient (- numBottles 1) (- numExchange 1))))
```

## Erlang

```erlang
-module(solution).
-export([num_water_bottles/2]).

-spec num_water_bottles(NumBottles :: integer(), NumExchange :: integer()) -> integer().
num_water_bottles(NumBottles, NumExchange) ->
    loop(NumBottles, NumBottles, NumExchange).

loop(Total, Empty, Exchange) when Empty >= Exchange ->
    NewFull = Empty div Exchange,
    NewTotal = Total + NewFull,
    NewEmpty = NewFull + (Empty rem Exchange),
    loop(NewTotal, NewEmpty, Exchange);
loop(Total, _Empty, _Exchange) ->
    Total.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_water_bottles(num_bottles :: integer, num_exchange :: integer) :: integer
  def num_water_bottles(num_bottles, num_exchange) do
    num_bottles + div(num_bottles - 1, num_exchange - 1)
  end
end
```

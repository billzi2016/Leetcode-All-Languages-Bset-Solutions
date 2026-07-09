# 3100. Water Bottles II

## Cpp

```cpp
class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        if (numExchange == 1) return numBottles; // edge case, avoid division by zero
        return numBottles + (numBottles - 1) / (numExchange - 1);
    }
};
```

## Java

```java
class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        if (numExchange == 1) {
            // With an exchange rate of 1, you can drink indefinitely.
            return Integer.MAX_VALUE;
        }
        return numBottles + (numBottles - 1) / (numExchange - 1);
    }
}
```

## Python

```python
class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles
        # If exchange rate is 1, the process would be infinite.
        if numExchange == 1:
            return float('inf')
        while empty >= numExchange:
            new_full = empty // numExchange
            total += new_full
            empty = empty % numExchange + new_full
        return total
```

## Python3

```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        if numExchange == 1:
            # With exchange rate 1, drinking can continue indefinitely.
            # Problem constraints avoid this case; return the initial count as a safe fallback.
            return numBottles
        return numBottles + (numBottles - 1) // (numExchange - 1)
```

## C

```c
#include <limits.h>

int maxBottlesDrunk(int numBottles, int numExchange) {
    if (numExchange == 1) {
        // With an exchange rate of 1, you can drink indefinitely.
        // Returning INT_MAX to indicate unbounded consumption.
        return INT_MAX;
    }
    int total = numBottles;
    int empty = numBottles;
    while (empty >= numExchange) {
        int newFull = empty / numExchange;
        total += newFull;
        empty = empty % numExchange + newFull;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxBottlesDrunk(int numBottles, int numExchange) {
        int total = 0;
        int full = numBottles;
        int empty = 0;
        while (full > 0) {
            total++;
            full--;
            empty++;
            if (empty == numExchange) {
                empty = 0;
                full++; // exchange empties for a new full bottle
            }
        }
        return total;
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
var maxBottlesDrunk = function(numBottles, numExchange) {
    if (numExchange === 1) {
        // With an exchange rate of 1, each empty bottle can be turned into a new full bottle indefinitely.
        // Return a very large number to represent infinity within JavaScript's numeric limits.
        return Number.MAX_SAFE_INTEGER;
    }
    // Each additional bottle effectively costs (numExchange - 1) empty bottles.
    // The total number of extra bottles obtainable is floor((numBottles - 1) / (numExchange - 1)).
    return numBottles + Math.floor((numBottles - 1) / (numExchange - 1));
};
```

## Typescript

```typescript
function maxBottlesDrunk(numBottles: number, numExchange: number): number {
    if (numExchange === 1) {
        // With an exchange rate of 1, you can drink indefinitely.
        return Number.MAX_SAFE_INTEGER;
    }
    let total = numBottles;
    let empty = numBottles;
    while (empty >= numExchange) {
        const newFull = Math.floor(empty / numExchange);
        total += newFull;
        empty = newFull + (empty % numExchange);
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
    function maxBottlesDrunk($numBottles, $numExchange) {
        if ($numExchange == 1) {
            return $numBottles;
        }
        return $numBottles + intdiv($numBottles - 1, $numExchange - 1);
    }
}
```

## Swift

```swift
class Solution {
    func maxBottlesDrunk(_ numBottles: Int, _ numExchange: Int) -> Int {
        var full = numBottles
        var empty = 0
        var drunk = 0
        
        while full > 0 {
            // Drink one bottle
            full -= 1
            empty += 1
            drunk += 1
            
            // Exchange if possible
            if empty >= numExchange {
                empty -= numExchange
                full += 1
            }
        }
        
        return drunk
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxBottlesDrunk(numBottles: Int, numExchange: Int): Int {
        if (numExchange == 1) return numBottles
        // Using the derived formula: total = initial + (initial - 1) / (exchange - 1)
        return numBottles + (numBottles - 1) / (numExchange - 1)
    }
}
```

## Dart

```dart
class Solution {
  int maxBottlesDrunk(int numBottles, int numExchange) {
    if (numExchange == 1) return numBottles;
    return numBottles + (numBottles - 1) ~/ (numExchange - 1);
  }
}
```

## Golang

```go
func maxBottlesDrunk(numBottles int, numExchange int) int {
	total := numBottles
	empty := numBottles

	if numExchange <= 1 {
		// Exchange rate of 1 would lead to infinite drinking;
		// problem constraints effectively avoid this case.
		return total
	}

	for empty >= numExchange {
		newFull := empty / numExchange
		total += newFull
		empty = newFull + (empty % numExchange)
	}
	return total
}
```

## Ruby

```ruby
def max_bottles_drunk(num_bottles, num_exchange)
  total = num_bottles
  empty = num_bottles
  while empty >= num_exchange
    empty -= num_exchange
    total += 1
  end
  total
end
```

## Scala

```scala
object Solution {
    def maxBottlesDrunk(numBottles: Int, numExchange: Int): Int = {
        if (numExchange == 1) numBottles * 2
        else numBottles + (numBottles - 1) / numExchange
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_bottles_drunk(num_bottles: i32, num_exchange: i32) -> i32 {
        if num_exchange == 1 {
            // According to problem constraints this case should not appear.
            return i32::MAX;
        }
        let mut total = num_bottles;
        let mut empty = num_bottles;
        while empty >= num_exchange {
            empty -= num_exchange; // exchange empties
            total += 1;            // drink the obtained bottle
            empty += 1;            // its empty after drinking
        }
        total
    }
}
```

## Racket

```racket
(define/contract (max-bottles-drunk numBottles numExchange)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((full numBottles) (drank 0))
    (if (>= full numExchange)
        (loop (+ (- full numExchange) 1) (+ drank numExchange))
        (+ drank full))))
```

## Erlang

```erlang
-spec max_bottles_drunk(NumBottles :: integer(), NumExchange :: integer()) -> integer().
max_bottles_drunk(NumBottles, NumExchange) ->
    case NumExchange of
        1 -> NumBottles;
        _ -> max_bottles_drunk_loop(NumBottles, 0, 0, NumExchange)
    end.

max_bottles_drunk_loop(Full, Empty, Total, Exchange) when Full > 0 ->
    max_bottles_drunk_loop(Full - 1, Empty + 1, Total + 1, Exchange);
max_bottles_drunk_loop(0, Empty, Total, Exchange) when Empty >= Exchange ->
    max_bottles_drunk_loop(1, Empty - Exchange, Total, Exchange);
max_bottles_drunk_loop(_, _, Total, _) -> Total.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_bottles_drunk(num_bottles :: integer, num_exchange :: integer) :: integer
  def max_bottles_drunk(num_bottles, num_exchange) do
    if num_exchange == 1 do
      # With an exchange rate of 1 the process would be infinite;
      # returning the initial count avoids non‑terminating behavior.
      num_bottles
    else
      num_bottles + div(num_bottles - 1, num_exchange - 1)
    end
  end
end
```

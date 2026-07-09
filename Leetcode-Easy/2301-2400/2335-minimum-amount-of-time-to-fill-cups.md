# 2335. Minimum Amount of Time to Fill Cups

## Cpp

```cpp
class Solution {
public:
    int fillCups(vector<int>& amount) {
        int total = amount[0] + amount[1] + amount[2];
        int mx = max({amount[0], amount[1], amount[2]});
        return max((total + 1) / 2, mx);
    }
};
```

## Java

```java
class Solution {
    public int fillCups(int[] amount) {
        int sum = amount[0] + amount[1] + amount[2];
        int max = Math.max(amount[0], Math.max(amount[1], amount[2]));
        return Math.max(max, (sum + 1) / 2);
    }
}
```

## Python

```python
class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        total = sum(amount)
        mx = max(amount)
        return max(mx, (total + 1) // 2)
```

## Python3

```python
from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        total = sum(amount)
        max_cup = max(amount)
        return max(max_cup, (total + 1) // 2)
```

## C

```c
int fillCups(int* amount, int amountSize) {
    int sum = 0, maxVal = 0;
    for (int i = 0; i < amountSize; ++i) {
        sum += amount[i];
        if (amount[i] > maxVal) maxVal = amount[i];
    }
    int half = (sum + 1) / 2;
    return maxVal > half ? maxVal : half;
}
```

## Csharp

```csharp
public class Solution {
    public int FillCups(int[] amount) {
        int sum = amount[0] + amount[1] + amount[2];
        int max = Math.Max(amount[0], Math.Max(amount[1], amount[2]));
        return Math.Max((sum + 1) / 2, max);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} amount
 * @return {number}
 */
var fillCups = function(amount) {
    const total = amount.reduce((sum, v) => sum + v, 0);
    const maxVal = Math.max(...amount);
    return Math.max(maxVal, Math.ceil(total / 2));
};
```

## Typescript

```typescript
function fillCups(amount: number[]): number {
    const total = amount[0] + amount[1] + amount[2];
    const maxVal = Math.max(amount[0], amount[1], amount[2]);
    return Math.max(maxVal, Math.ceil(total / 2));
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $amount
     * @return Integer
     */
    function fillCups($amount) {
        $max = max($amount);
        $sum = array_sum($amount);
        return max($max, intdiv($sum + 1, 2));
    }
}
```

## Swift

```swift
class Solution {
    func fillCups(_ amount: [Int]) -> Int {
        let total = amount.reduce(0, +)
        let maxVal = amount.max()!
        return max((total + 1) / 2, maxVal)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fillCups(amount: IntArray): Int {
        val total = amount.sum()
        val maxVal = amount.maxOrNull() ?: 0
        return kotlin.math.max(maxVal, (total + 1) / 2)
    }
}
```

## Dart

```dart
class Solution {
  int fillCups(List<int> amount) {
    int total = amount[0] + amount[1] + amount[2];
    int maxVal = amount.reduce((a, b) => a > b ? a : b);
    int halfCeil = (total + 1) ~/ 2;
    return maxVal > halfCeil ? maxVal : halfCeil;
  }
}
```

## Golang

```go
func fillCups(amount []int) int {
    sum := amount[0] + amount[1] + amount[2]
    maxVal := amount[0]
    if amount[1] > maxVal {
        maxVal = amount[1]
    }
    if amount[2] > maxVal {
        maxVal = amount[2]
    }
    half := (sum + 1) / 2
    if maxVal > half {
        return maxVal
    }
    return half
}
```

## Ruby

```ruby
def fill_cups(amount)
  total = amount.sum
  max_val = amount.max
  [(total + 1) / 2, max_val].max
end
```

## Scala

```scala
object Solution {
    def fillCups(amount: Array[Int]): Int = {
        val sum = amount(0) + amount(1) + amount(2)
        val maxVal = amount.max
        Math.max(maxVal, (sum + 1) / 2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn fill_cups(amount: Vec<i32>) -> i32 {
        let total: i32 = amount.iter().sum();
        let max_val = *amount.iter().max().unwrap();
        std::cmp::max(max_val, (total + 1) / 2)
    }
}
```

## Racket

```racket
(define/contract (fill-cups amount)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((a (first amount))
         (b (second amount))
         (c (third amount))
         (total (+ a b c))
         (maxVal (apply max amount))
         (half-ceil (quotient (+ total 1) 2)))
    (max half-ceil maxVal)))
```

## Erlang

```erlang
-module(solution).
-export([fill_cups/1]).

-spec fill_cups([integer()]) -> integer().
fill_cups(Amount) ->
    Sum = lists:sum(Amount),
    Max = lists:max(Amount),
    CeilHalf = (Sum + 1) div 2,
    if
        Max > CeilHalf -> Max;
        true -> CeilHalf
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec fill_cups(amount :: [integer]) :: integer
  def fill_cups(amount) do
    total = Enum.sum(amount)
    max_val = Enum.max(amount)
    max(max_val, div(total + 1, 2))
  end
end
```

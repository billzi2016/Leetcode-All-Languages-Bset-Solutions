# 2600. K Items With the Maximum Sum

## Cpp

```cpp
class Solution {
public:
    int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int takeOnes = std::min(k, numOnes);
        int sum = takeOnes; // each contributes +1
        int remaining = k - takeOnes;
        
        int takeZeros = std::min(remaining, numZeros);
        remaining -= takeZeros; // zeros add nothing
        
        // Remaining items must be -1s
        sum -= remaining; // each -1 reduces sum by 1
        return sum;
    }
};
```

## Java

```java
class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int takeOnes = Math.min(k, numOnes);
        int sum = takeOnes;
        int remaining = k - takeOnes;
        // zeros contribute nothing, just reduce remaining count
        int takeZeros = Math.min(remaining, numZeros);
        remaining -= takeZeros;
        // remaining items must be -1s
        sum -= remaining; // each -1 reduces sum by 1
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        take_ones = min(k, numOnes)
        remaining = k - take_ones

        # zeros contribute nothing, just reduce the remaining count
        take_zeros = min(remaining, numZeros)
        remaining -= take_zeros

        # whatever is left must be taken from -1 items
        take_neg = remaining  # each contributes -1

        return take_ones - take_neg
```

## Python3

```python
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        take_ones = min(k, numOnes)
        remaining = k - take_ones
        take_zeros = min(remaining, numZeros)
        remaining -= take_zeros  # these will be -1 items
        return take_ones - remaining
```

## C

```c
int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    int takeOnes = k < numOnes ? k : numOnes;
    int sum = takeOnes;  // each contributes +1
    int remaining = k - takeOnes;

    int takeZeros = remaining < numZeros ? remaining : numZeros;
    remaining -= takeZeros;  // zeros add nothing to sum

    // whatever remains must be taken from -1 items
    sum -= remaining;  // each -1 reduces sum by 1
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int KItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        // Take as many 1's as possible
        int takeOnes = Math.Min(k, numOnes);
        int sum = takeOnes;
        int remaining = k - takeOnes;

        // Take zeros (they don't affect the sum)
        int takeZeros = Math.Min(remaining, numZeros);
        remaining -= takeZeros; // sum unchanged

        // Remaining items must be -1's
        sum -= remaining; // each contributes -1
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numOnes
 * @param {number} numZeros
 * @param {number} numNegOnes
 * @param {number} k
 * @return {number}
 */
var kItemsWithMaximumSum = function(numOnes, numZeros, numNegOnes, k) {
    const takeOnes = Math.min(k, numOnes);
    let remaining = k - takeOnes;
    
    const takeZeros = Math.min(remaining, numZeros);
    remaining -= takeZeros; // zeros add nothing
    
    // remaining items must be -1s
    const sum = takeOnes - remaining; // each -1 reduces sum by 1
    return sum;
};
```

## Typescript

```typescript
function kItemsWithMaximumSum(numOnes: number, numZeros: number, numNegOnes: number, k: number): number {
    const takeOnes = Math.min(k, numOnes);
    let sum = takeOnes; // each contributes +1
    let remaining = k - takeOnes;

    const takeZeros = Math.min(remaining, numZeros);
    remaining -= takeZeros; // zeros add nothing

    // any remaining picks must be -1 items
    sum -= remaining; // each -1 reduces sum by 1

    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numOnes
     * @param Integer $numZeros
     * @param Integer $numNegOnes
     * @param Integer $k
     * @return Integer
     */
    function kItemsWithMaximumSum($numOnes, $numZeros, $numNegOnes, $k) {
        $takeOnes = min($k, $numOnes);
        $sum = $takeOnes;
        $remaining = $k - $takeOnes;

        // Take zeros (they don't affect the sum)
        $takeZeros = min($remaining, $numZeros);
        $remaining -= $takeZeros;

        // Remaining items must be -1s
        $sum -= $remaining; // each -1 reduces the sum by 1

        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func kItemsWithMaximumSum(_ numOnes: Int, _ numZeros: Int, _ numNegOnes: Int, _ k: Int) -> Int {
        var remaining = k
        let takeOnes = min(remaining, numOnes)
        var sum = takeOnes
        remaining -= takeOnes
        
        let takeZeros = min(remaining, numZeros)
        // zeros add nothing to sum
        remaining -= takeZeros
        
        // the rest are -1 items
        sum -= remaining  // each contributes -1
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kItemsWithMaximumSum(numOnes: Int, numZeros: Int, numNegOnes: Int, k: Int): Int {
        var remaining = k
        val takeOnes = minOf(remaining, numOnes)
        var sum = takeOnes // each contributes +1
        remaining -= takeOnes

        val takeZeros = minOf(remaining, numZeros)
        // zeros add nothing
        remaining -= takeZeros

        // any leftover must be -1 items
        sum -= remaining  // each -1 reduces sum by 1
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    int takeOnes = k < numOnes ? k : numOnes;
    int sum = takeOnes; // each contributes +1
    int remaining = k - takeOnes;

    int takeZeros = remaining < numZeros ? remaining : numZeros;
    remaining -= takeZeros; // zeros add nothing

    // Remaining items must be -1s
    sum -= remaining; // each -1 reduces sum by 1
    return sum;
  }
}
```

## Golang

```go
func kItemsWithMaximumSum(numOnes int, numZeros int, numNegOnes int, k int) int {
    // Take as many 1s as possible
    takeOnes := k
    if takeOnes > numOnes {
        takeOnes = numOnes
    }
    remaining := k - takeOnes

    // Take as many 0s as possible (they don't affect sum)
    takeZeros := remaining
    if takeZeros > numZeros {
        takeZeros = numZeros
    }
    remaining -= takeZeros

    // The rest must be -1s, each decreasing the sum by 1
    // remaining is the number of -1 items taken
    return takeOnes - remaining
}
```

## Ruby

```ruby
def k_items_with_maximum_sum(num_ones, num_zeros, num_neg_ones, k)
  take_one = [num_ones, k].min
  remaining = k - take_one
  take_zero = [num_zeros, remaining].min
  remaining -= take_zero
  take_one - remaining
end
```

## Scala

```scala
object Solution {
    def kItemsWithMaximumSum(numOnes: Int, numZeros: Int, numNegOnes: Int, k: Int): Int = {
        val takeOnes = math.min(k, numOnes)
        var sum = takeOnes
        val remainingAfterOnes = k - takeOnes

        val takeZeros = math.min(remainingAfterOnes, numZeros)
        val remainingAfterZeros = remainingAfterOnes - takeZeros

        // Remaining items must be -1s
        sum -= remainingAfterZeros
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn k_items_with_maximum_sum(num_ones: i32, num_zeros: i32, num_neg_ones: i32, k: i32) -> i32 {
        let take_ones = num_ones.min(k);
        let remaining_after_ones = k - take_ones;
        let take_zeros = num_zeros.min(remaining_after_ones);
        let remaining_after_zeros = remaining_after_ones - take_zeros; // these must be -1s
        take_ones - remaining_after_zeros
    }
}
```

## Racket

```racket
(define/contract (k-items-with-maximum-sum numOnes numZeros numNegOnes k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([take-ones (min k numOnes)]
         [remaining (- k take-ones)]
         [take-zeros (min remaining numZeros)]
         [remaining2 (- remaining take-zeros)])
    (+ (* take-ones 1) (* remaining2 -1))))
```

## Erlang

```erlang
-module(solution).
-export([k_items_with_maximum_sum/4]).

-spec k_items_with_maximum_sum(integer(), integer(), integer(), integer()) -> integer().
k_items_with_maximum_sum(NumOnes, NumZeros, _NumNegOnes, K) ->
    OnesTaken = erlang:min(NumOnes, K),
    Rem1 = K - OnesTaken,
    ZerosTaken = erlang:min(NumZeros, Rem1),
    Rem2 = Rem1 - ZerosTaken,
    OnesTaken - Rem2.
```

## Elixir

```elixir
defmodule Solution do
  @spec k_items_with_maximum_sum(num_ones :: integer, num_zeros :: integer, num_neg_ones :: integer, k :: integer) :: integer
  def k_items_with_maximum_sum(num_ones, num_zeros, _num_neg_ones, k) do
    ones_taken = min(num_ones, k)
    remaining = k - ones_taken
    zeros_taken = min(num_zeros, remaining)
    neg_needed = remaining - zeros_taken
    ones_taken - neg_needed
  end
end
```

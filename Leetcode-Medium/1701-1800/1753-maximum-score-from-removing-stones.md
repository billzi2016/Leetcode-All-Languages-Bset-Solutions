# 1753. Maximum Score From Removing Stones

## Cpp

```cpp
class Solution {
public:
    int maximumScore(int a, int b, int c) {
        long long total = (long long)a + b + c;
        int mx = std::max({a, b, c});
        return (int)std::min(total / 2, total - mx);
    }
};
```

## Java

```java
class Solution {
    public int maximumScore(int a, int b, int c) {
        int total = a + b + c;
        int max = Math.max(a, Math.max(b, c));
        return Math.min(total / 2, total - max);
    }
}
```

## Python

```python
class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        total = a + b + c
        mx = max(a, b, c)
        return min(total - mx, total // 2)
```

## Python3

```python
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        total = a + b + c
        max_pile = max(a, b, c)
        # The game can last at most the sum of the two smaller piles,
        # and also cannot exceed half of total stones (each move uses 2 stones).
        return min(total // 2, total - max_pile)
```

## C

```c
int maximumScore(int a, int b, int c) {
    int total = a + b + c;
    int mx = a;
    if (b > mx) mx = b;
    if (c > mx) mx = c;
    int limit1 = total / 2;
    int limit2 = total - mx;
    return limit1 < limit2 ? limit1 : limit2;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumScore(int a, int b, int c)
    {
        int total = a + b + c;
        int maxPile = Math.Max(a, Math.Max(b, c));
        return Math.Min(total / 2, total - maxPile);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var maximumScore = function(a, b, c) {
    const arr = [a, b, c].sort((x, y) => y - x); // descending
    return Math.min(arr[0], arr[1] + arr[2]);
};
```

## Typescript

```typescript
function maximumScore(a: number, b: number, c: number): number {
    const total = a + b + c;
    const maxPile = Math.max(a, b, c);
    return Math.min(Math.floor(total / 2), total - maxPile);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function maximumScore($a, $b, $c) {
        $total = $a + $b + $c;
        $maxPile = max($a, $b, $c);
        return min(intdiv($total, 2), $total - $maxPile);
    }
}
```

## Swift

```swift
class Solution {
    func maximumScore(_ a: Int, _ b: Int, _ c: Int) -> Int {
        let total = a + b + c
        let maxPile = max(a, max(b, c))
        return min(total / 2, total - maxPile)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumScore(a: Int, b: Int, c: Int): Int {
        val total = a + b + c
        val maxPile = maxOf(a, b, c)
        return kotlin.math.min(total / 2, total - maxPile)
    }
}
```

## Dart

```dart
class Solution {
  int maximumScore(int a, int b, int c) {
    int total = a + b + c;
    int maxPile = a;
    if (b > maxPile) maxPile = b;
    if (c > maxPile) maxPile = c;
    int limitByLargest = total - maxPile; // sum of two smaller piles
    int limitByTotal = total ~/ 2; // each move removes 2 stones
    return limitByLargest < limitByTotal ? limitByLargest : limitByTotal;
  }
}
```

## Golang

```go
func maximumScore(a int, b int, c int) int {
	total := a + b + c
	maxPile := a
	if b > maxPile {
		maxPile = b
	}
	if c > maxPile {
		maxPile = c
	}
	sumOtherTwo := total - maxPile
	if total/2 < sumOtherTwo {
		return total / 2
	}
	return sumOtherTwo
}
```

## Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer}
def maximum_score(a, b, c)
  total = a + b + c
  max_val = [a, b, c].max
  [total - max_val, total / 2].min
end
```

## Scala

```scala
object Solution {
    def maximumScore(a: Int, b: Int, c: Int): Int = {
        val total = a + b + c
        val maxPile = math.max(a, math.max(b, c))
        math.min(total / 2, total - maxPile)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_score(a: i32, b: i32, c: i32) -> i32 {
        let total = a + b + c;
        let max_val = *[a, b, c].iter().max().unwrap();
        std::cmp::min(total / 2, total - max_val)
    }
}
```

## Racket

```racket
(define/contract (maximum-score a b c)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([total (+ a b c)]
         [mx (max a b c)]
         [limit1 (quotient total 2)]
         [limit2 (- total mx)])
    (if (< limit1 limit2) limit1 limit2)))
```

## Erlang

```erlang
-spec maximum_score(A :: integer(), B :: integer(), C :: integer()) -> integer().
maximum_score(A, B, C) ->
    Sum = A + B + C,
    MaxAB = erlang:max(A, B),
    Max = erlang:max(MaxAB, C),
    SmallSum = Sum - Max,
    Half = Sum div 2,
    if
        SmallSum < Half -> SmallSum;
        true -> Half
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_score(a :: integer, b :: integer, c :: integer) :: integer
  def maximum_score(a, b, c) do
    [x, y, _z] = Enum.sort([a, b, c])
    total = a + b + c
    min(x + y, div(total, 2))
  end
end
```

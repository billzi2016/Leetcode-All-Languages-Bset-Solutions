# 0172. Factorial Trailing Zeroes

## Cpp

```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        while (n >= 5) {
            n /= 5;
            count += n;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int trailingZeroes(int n) {
        int count = 0;
        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n //= 5
            count += n
        return count
```

## Python3

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            n //= 5
            count += n
        return count
```

## C

```c
int trailingZeroes(int n) {
    int count = 0;
    while (n >= 5) {
        n /= 5;
        count += n;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int TrailingZeroes(int n) {
        int count = 0;
        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
    let count = 0;
    while (n > 0) {
        n = Math.floor(n / 5);
        count += n;
    }
    return count;
};
```

## Typescript

```typescript
function trailingZeroes(n: number): number {
    let count = 0;
    while (n >= 5) {
        n = Math.floor(n / 5);
        count += n;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function trailingZeroes($n) {
        $count = 0;
        while ($n > 0) {
            $n = intdiv($n, 5);
            $count += $n;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func trailingZeroes(_ n: Int) -> Int {
        var count = 0
        var divisor = n
        while divisor > 0 {
            divisor /= 5
            count += divisor
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun trailingZeroes(n: Int): Int {
        var count = 0
        var divisor = n
        while (divisor >= 5) {
            divisor /= 5
            count += divisor
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int trailingZeroes(int n) {
    int count = 0;
    while (n >= 5) {
      n ~/= 5;
      count += n;
    }
    return count;
  }
}
```

## Golang

```go
func trailingZeroes(n int) int {
    count := 0
    for n > 0 {
        n /= 5
        count += n
    }
    return count
}
```

## Ruby

```ruby
def trailing_zeroes(n)
  count = 0
  while n > 0
    n /= 5
    count += n
  end
  count
end
```

## Scala

```scala
object Solution {
    def trailingZeroes(n: Int): Int = {
        var count = 0
        var divisor = 5L
        while (divisor <= n) {
            count += (n / divisor).toInt
            divisor *= 5
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn trailing_zeroes(n: i32) -> i32 {
        let mut count = 0;
        let mut divisor = 5;
        while divisor <= n {
            count += n / divisor;
            if divisor > i32::MAX / 5 { break; }
            divisor *= 5;
        }
        count
    }
}
```

## Racket

```racket
(define/contract (trailing-zeroes n)
  (-> exact-integer? exact-integer?)
  (let loop ((k n) (sum 0))
    (if (< k 5)
        sum
        (let ((next (quotient k 5)))
          (loop next (+ sum next))))))
```

## Erlang

```erlang
-spec trailing_zeroes(N :: integer()) -> integer().
trailing_zeroes(N) when N >= 0 ->
    trailing_zeroes(N, 0).

trailing_zeroes(0, Acc) -> Acc;
trailing_zeroes(N, Acc) ->
    N1 = N div 5,
    trailing_zeroes(N1, Acc + N1).
```

## Elixir

```elixir
defmodule Solution do
  @spec trailing_zeroes(n :: integer) :: integer
  def trailing_zeroes(n) do
    count_zeros(n, 5, 0)
  end

  defp count_zeros(n, divisor, acc) when n < divisor, do: acc
  defp count_zeros(n, divisor, acc) do
    count_zeros(n, divisor * 5, acc + div(n, divisor))
  end
end
```

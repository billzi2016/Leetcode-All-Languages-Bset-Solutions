# 1837. Sum of Digits in Base K

## Cpp

```cpp
class Solution {
public:
    int sumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            sum += n % k;
            n /= k;
        }
        return sum;
    }
};
```

## Java

```java
class Solution {
    public int sumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            sum += n % k;
            n /= k;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        total = 0
        while n:
            total += n % k
            n //= k
        return total
```

## Python3

```python
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total = 0
        while n:
            total += n % k
            n //= k
        return total
```

## C

```c
int sumBase(int n, int k) {
    int sum = 0;
    while (n > 0) {
        sum += n % k;
        n /= k;
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int SumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            sum += n % k;
            n /= k;
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var sumBase = function(n, k) {
    let sum = 0;
    while (n > 0) {
        sum += n % k;
        n = Math.floor(n / k);
    }
    return sum;
};
```

## Typescript

```typescript
function sumBase(n: number, k: number): number {
    let sum = 0;
    while (n > 0) {
        sum += n % k;
        n = Math.floor(n / k);
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function sumBase($n, $k) {
        $sum = 0;
        while ($n > 0) {
            $sum += $n % $k;
            $n = intdiv($n, $k);
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func sumBase(_ n: Int, _ k: Int) -> Int {
        var num = n
        var result = 0
        while num > 0 {
            result += num % k
            num /= k
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumBase(n: Int, k: Int): Int {
        var num = n
        var sum = 0
        while (num > 0) {
            sum += num % k
            num /= k
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int sumBase(int n, int k) {
    int sum = 0;
    while (n > 0) {
      sum += n % k;
      n ~/= k;
    }
    return sum;
  }
}
```

## Golang

```go
func sumBase(n int, k int) int {
	sum := 0
	for n > 0 {
		sum += n % k
		n /= k
	}
	return sum
}
```

## Ruby

```ruby
def sum_base(n, k)
  sum = 0
  while n > 0
    sum += n % k
    n /= k
  end
  sum
end
```

## Scala

```scala
object Solution {
    def sumBase(n: Int, k: Int): Int = {
        var num = n
        var sum = 0
        while (num > 0) {
            sum += num % k
            num /= k
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_base(mut n: i32, k: i32) -> i32 {
        let mut sum = 0;
        while n > 0 {
            sum += n % k;
            n /= k;
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (sum-base n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((num n) (acc 0))
    (if (= num 0)
        acc
        (loop (quotient num k)
              (+ acc (remainder num k))))))
```

## Erlang

```erlang
-spec sum_base(N :: integer(), K :: integer()) -> integer().
sum_base(N, K) ->
    sum_base(N, K, 0).

sum_base(0, _K, Acc) -> 
    Acc;
sum_base(N, K, Acc) ->
    Digit = N rem K,
    sum_base(N div K, K, Acc + Digit).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_base(n :: integer, k :: integer) :: integer
  def sum_base(n, k), do: sum_digits(n, k, 0)

  defp sum_digits(0, _k, acc), do: acc
  defp sum_digits(num, k, acc) do
    digit = rem(num, k)
    sum_digits(div(num, k), k, acc + digit)
  end
end
```

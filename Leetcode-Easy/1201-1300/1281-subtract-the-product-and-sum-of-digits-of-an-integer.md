# 1281. Subtract the Product and Sum of Digits of an Integer

## Cpp

```cpp
class Solution {
public:
    int subtractProductAndSum(int n) {
        int sum = 0, prod = 1;
        while (n > 0) {
            int d = n % 10;
            sum += d;
            prod *= d;
            n /= 10;
        }
        return prod - sum;
    }
};
```

## Java

```java
class Solution {
    public int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            product *= digit;
            sum += digit;
            n /= 10;
        }
        return product - sum;
    }
}
```

## Python

```python
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        summ = 0
        while n:
            digit = n % 10
            prod *= digit
            summ += digit
            n //= 10
        return prod - summ
```

## Python3

```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10
        return product - total
```

## C

```c
int subtractProductAndSum(int n) {
    if (n == 0) return 0;
    int product = 1;
    int sum = 0;
    while (n > 0) {
        int digit = n % 10;
        product *= digit;
        sum += digit;
        n /= 10;
    }
    return product - sum;
}
```

## Csharp

```csharp
public class Solution {
    public int SubtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            product *= digit;
            sum += digit;
            n /= 10;
        }
        return product - sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let product = 1, sum = 0;
    while (n > 0) {
        const digit = n % 10;
        product *= digit;
        sum += digit;
        n = Math.floor(n / 10);
    }
    return product - sum;
};
```

## Typescript

```typescript
function subtractProductAndSum(n: number): number {
    if (n === 0) return 0;
    let sum = 0;
    let product = 1;
    while (n > 0) {
        const digit = n % 10;
        sum += digit;
        product *= digit;
        n = Math.floor(n / 10);
    }
    return product - sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function subtractProductAndSum($n) {
        if ($n == 0) {
            return 0;
        }
        $product = 1;
        $sum = 0;
        while ($n > 0) {
            $digit = $n % 10;
            $product *= $digit;
            $sum += $digit;
            $n = intdiv($n, 10);
        }
        return $product - $sum;
    }
}
```

## Swift

```swift
class Solution {
    func subtractProductAndSum(_ n: Int) -> Int {
        if n == 0 { return 0 }
        var num = n
        var sum = 0
        var product = 1
        while num > 0 {
            let digit = num % 10
            sum += digit
            product *= digit
            num /= 10
        }
        return product - sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subtractProductAndSum(n: Int): Int {
        var num = n
        var sum = 0
        var product = 1
        while (num > 0) {
            val digit = num % 10
            sum += digit
            product *= digit
            num /= 10
        }
        return product - sum
    }
}
```

## Dart

```dart
class Solution {
  int subtractProductAndSum(int n) {
    if (n == 0) return 0;
    int product = 1;
    int sum = 0;
    while (n > 0) {
      int digit = n % 10;
      product *= digit;
      sum += digit;
      n ~/= 10;
    }
    return product - sum;
  }
}
```

## Golang

```go
func subtractProductAndSum(n int) int {
    prod, sum := 1, 0
    for n > 0 {
        d := n % 10
        prod *= d
        sum += d
        n /= 10
    }
    return prod - sum
}
```

## Ruby

```ruby
def subtract_product_and_sum(n)
  prod = 1
  sum = 0
  while n > 0
    digit = n % 10
    prod *= digit
    sum += digit
    n /= 10
  end
  prod - sum
end
```

## Scala

```scala
object Solution {
    def subtractProductAndSum(n: Int): Int = {
        var num = n
        var prod = 1
        var sum = 0
        while (num > 0) {
            val digit = num % 10
            prod *= digit
            sum += digit
            num /= 10
        }
        prod - sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subtract_product_and_sum(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let mut num = n;
        let mut prod: i32 = 1;
        let mut sum: i32 = 0;
        while num > 0 {
            let digit = num % 10;
            prod *= digit;
            sum += digit;
            num /= 10;
        }
        prod - sum
    }
}
```

## Racket

```racket
(define/contract (subtract-product-and-sum n)
  (-> exact-integer? exact-integer?)
  (if (= n 0)
      0
      (let loop ((x n) (prod 1) (sum 0))
        (if (= x 0)
            (- prod sum)
            (let* ((digit (remainder x 10))
                   (new-prod (* prod digit))
                   (new-sum (+ sum digit)))
              (loop (quotient x 10) new-prod new-sum))))))
```

## Erlang

```erlang
-spec subtract_product_and_sum(N :: integer()) -> integer().
subtract_product_and_sum(N) ->
    subtract_product_and_sum(N, 1, 0).

subtract_product_and_sum(0, Prod, Sum) ->
    Prod - Sum;
subtract_product_and_sum(N, Prod, Sum) ->
    Digit = N rem 10,
    subtract_product_and_sum(N div 10, Prod * Digit, Sum + Digit).
```

## Elixir

```elixir
defmodule Solution do
  @spec subtract_product_and_sum(n :: integer) :: integer
  def subtract_product_and_sum(n) do
    {product, sum} = compute_digits(n, 1, 0)
    product - sum
  end

  defp compute_digits(0, prod, sum), do: {prod, sum}
  defp compute_digits(num, prod, sum) do
    digit = rem(num, 10)
    compute_digits(div(num, 10), prod * digit, sum + digit)
  end
end
```

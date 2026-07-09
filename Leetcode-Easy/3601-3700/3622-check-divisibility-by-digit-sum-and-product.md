# 3622. Check Divisibility by Digit Sum and Product

## Cpp

```cpp
class Solution {
public:
    bool checkDivisibility(int n) {
        int sum = 0;
        int prod = 1;
        int temp = n;
        while (temp > 0) {
            int d = temp % 10;
            sum += d;
            prod *= d;
            temp /= 10;
        }
        int divisor = sum + prod;
        return divisor != 0 && n % divisor == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean checkDivisibility(int n) {
        int sum = 0;
        int prod = 1;
        int temp = n;
        while (temp > 0) {
            int d = temp % 10;
            sum += d;
            prod *= d;
            temp /= 10;
        }
        int divisor = sum + prod;
        return n % divisor == 0;
    }
}
```

## Python

```python
class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total_sum = 0
        total_prod = 1
        temp = n
        while temp:
            digit = temp % 10
            total_sum += digit
            total_prod *= digit
            temp //= 10
        divisor = total_sum + total_prod
        return n % divisor == 0
```

## Python3

```python
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = n
        s = 0
        p = 1
        while total:
            d = total % 10
            s += d
            p *= d
            total //= 10
        divisor = s + p
        return n % divisor == 0
```

## C

```c
#include <stdbool.h>

bool checkDivisibility(int n) {
    int sum = 0, product = 1, temp = n;
    while (temp > 0) {
        int d = temp % 10;
        sum += d;
        product *= d;
        temp /= 10;
    }
    int divisor = sum + product;
    return divisor != 0 && n % divisor == 0;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckDivisibility(int n) {
        int sum = 0;
        int product = 1;
        int temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            sum += digit;
            product *= digit;
            temp /= 10;
        }
        int divisor = sum + product;
        return divisor != 0 && n % divisor == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var checkDivisibility = function(n) {
    let sum = 0;
    let product = 1;
    let temp = n;
    while (temp > 0) {
        const digit = temp % 10;
        sum += digit;
        product *= digit;
        temp = Math.floor(temp / 10);
    }
    const divisor = sum + product;
    return n % divisor === 0;
};
```

## Typescript

```typescript
function checkDivisibility(n: number): boolean {
    let sum = 0;
    let prod = 1;
    let x = n;
    while (x > 0) {
        const d = x % 10;
        sum += d;
        prod *= d;
        x = Math.floor(x / 10);
    }
    const divisor = sum + prod;
    return divisor !== 0 && n % divisor === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function checkDivisibility($n) {
        $sum = 0;
        $product = 1;
        $temp = $n;
        while ($temp > 0) {
            $digit = $temp % 10;
            $sum += $digit;
            $product *= $digit;
            $temp = intdiv($temp, 10);
        }
        $total = $sum + $product;
        return $n % $total == 0;
    }
}
```

## Swift

```swift
class Solution {
    func checkDivisibility(_ n: Int) -> Bool {
        var num = n
        var sum = 0
        var product = 1
        while num > 0 {
            let digit = num % 10
            sum += digit
            product *= digit
            num /= 10
        }
        let divisor = sum + product
        return n % divisor == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkDivisibility(n: Int): Boolean {
        var sum = 0
        var prod = 1
        var temp = n
        while (temp > 0) {
            val d = temp % 10
            sum += d
            prod *= d
            temp /= 10
        }
        val divisor = sum + prod
        return n % divisor == 0
    }
}
```

## Dart

```dart
class Solution {
  bool checkDivisibility(int n) {
    int sum = 0;
    int product = 1;
    int temp = n;
    while (temp > 0) {
      int digit = temp % 10;
      sum += digit;
      product *= digit;
      temp ~/= 10;
    }
    int divisor = sum + product;
    if (divisor == 0) return false;
    return n % divisor == 0;
  }
}
```

## Golang

```go
func checkDivisibility(n int) bool {
	sum, prod := 0, 1
	for x := n; x > 0; x /= 10 {
		d := x % 10
		sum += d
		prod *= d
	}
	total := sum + prod
	if total == 0 {
		return false
	}
	return n%total == 0
}
```

## Ruby

```ruby
def check_divisibility(n)
  sum = 0
  prod = 1
  temp = n
  while temp > 0
    d = temp % 10
    sum += d
    prod *= d
    temp /= 10
  end
  total = sum + prod
  n % total == 0
end
```

## Scala

```scala
object Solution {
    def checkDivisibility(n: Int): Boolean = {
        var temp = n
        var sum = 0
        var prod = 1
        while (temp > 0) {
            val d = temp % 10
            sum += d
            prod *= d
            temp /= 10
        }
        val divisor = sum + prod
        divisor != 0 && n % divisor == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_divisibility(n: i32) -> bool {
        let mut x = n;
        let mut sum = 0;
        let mut prod = 1;
        while x > 0 {
            let d = x % 10;
            sum += d;
            prod *= d;
            x /= 10;
        }
        let divisor = sum + prod;
        n % divisor == 0
    }
}
```

## Racket

```racket
(define/contract (check-divisibility n)
  (-> exact-integer? boolean?)
  (let loop ((x n) (sum 0) (prod 1))
    (if (= x 0)
        (let ((total (+ sum prod)))
          (= (remainder n total) 0))
        (let* ((digit (remainder x 10))
               (new-sum (+ sum digit))
               (new-prod (* prod digit)))
          (loop (quotient x 10) new-sum new-prod)))))
```

## Erlang

```erlang
-spec check_divisibility(N :: integer()) -> boolean().
check_divisibility(N) when N > 0 ->
    {Sum, Prod} = digits_sum_product(N, 0, 1),
    Divisor = Sum + Prod,
    N rem Divisor == 0.

digits_sum_product(0, Sum, Prod) ->
    {Sum, Prod};
digits_sum_product(N, SumAcc, ProdAcc) ->
    Digit = N rem 10,
    digits_sum_product(N div 10, SumAcc + Digit, ProdAcc * Digit).
```

## Elixir

```elixir
defmodule Solution do
  @spec check_divisibility(n :: integer) :: boolean
  def check_divisibility(n) do
    {sum, prod} =
      Integer.digits(n)
      |> Enum.reduce({0, 1}, fn d, {s, p} -> {s + d, p * d} end)

    divisor = sum + prod
    rem(n, divisor) == 0
  end
end
```

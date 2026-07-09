# 0050. Pow(x, n)

## Cpp

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1.0 / x;
            N = -N;
        }
        double result = 1.0;
        while (N > 0) {
            if (N & 1LL) result *= x;
            x *= x;
            N >>= 1;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public double myPow(double x, int n) {
        long exp = n;
        if (exp < 0) {
            x = 1 / x;
            exp = -exp;
        }
        double result = 1.0;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result *= x;
            }
            x *= x;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            x = 1.0 / x
            n = -n
        result = 1.0
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result
```

## Python3

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        negative = n < 0
        N = -n if negative else n
        result = 1.0
        current = x
        while N:
            if N & 1:
                result *= current
            current *= current
            N >>= 1
        return 1.0 / result if negative else result
```

## C

```c
double myPow(double x, int n) {
    long long exp = n;
    if (exp < 0) {
        x = 1.0 / x;
        exp = -exp;
    }
    double result = 1.0;
    while (exp) {
        if (exp & 1LL) result *= x;
        x *= x;
        exp >>= 1LL;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public double MyPow(double x, int n) {
        long exp = n;
        if (exp < 0) {
            x = 1 / x;
            exp = -exp;
        }
        double result = 1.0;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result *= x;
            }
            x *= x;
            exp >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    let N = BigInt(n);
    if (N < 0n) {
        x = 1 / x;
        N = -N;
    }
    let result = 1;
    while (N > 0n) {
        if ((N & 1n) === 1n) {
            result *= x;
        }
        x *= x;
        N >>= 1n;
    }
    return result;
};
```

## Typescript

```typescript
function myPow(x: number, n: number): number {
    if (n === 0) return 1;
    let exponent = Math.abs(n);
    let base = x;
    let result = 1;
    while (exponent > 0) {
        if (exponent % 2 === 1) {
            result *= base;
        }
        base *= base;
        exponent = Math.floor(exponent / 2);
    }
    return n < 0 ? 1 / result : result;
}
```

## Php

```php
class Solution {
    /**
     * @param Float $x
     * @param Integer $n
     * @return Float
     */
    function myPow($x, $n) {
        if ($n == 0) return 1.0;
        $N = $n;
        if ($n < 0) {
            $x = 1 / $x;
            $N = -$n;
        }
        $result = 1.0;
        while ($N > 0) {
            if ($N & 1) {
                $result *= $x;
            }
            $x *= $x;
            $N >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func myPow(_ x: Double, _ n: Int) -> Double {
        var base = x
        var exp = Int64(n)
        if exp < 0 {
            base = 1.0 / base
            exp = -exp
        }
        var result: Double = 1.0
        while exp > 0 {
            if (exp & 1) == 1 {
                result *= base
            }
            base *= base
            exp >>= 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun myPow(x: Double, n: Int): Double {
        var base = x
        var exp = n.toLong()
        if (exp < 0) {
            base = 1 / base
            exp = -exp
        }
        var result = 1.0
        while (exp > 0) {
            if ((exp and 1L) == 1L) {
                result *= base
            }
            base *= base
            exp = exp shr 1
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  double myPow(double x, int n) {
    if (n == 0) return 1.0;
    double base = x;
    int exponent = n;
    if (exponent < 0) {
      base = 1 / base;
      exponent = -exponent;
    }
    double result = 1.0;
    while (exponent > 0) {
      if ((exponent & 1) == 1) {
        result *= base;
      }
      base *= base;
      exponent >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
func myPow(x float64, n int) float64 {
    var exp int64 = int64(n)
    if exp < 0 {
        x = 1 / x
        exp = -exp
    }
    result := 1.0
    for exp > 0 {
        if exp&1 == 1 {
            result *= x
        }
        x *= x
        exp >>= 1
    }
    return result
}
```

## Ruby

```ruby
def my_pow(x, n)
  return 0.0 if x == 0 && n < 0
  result = 1.0
  base = x.to_f
  exp = n

  if exp < 0
    exp = -exp
    base = 1.0 / base
  end

  while exp > 0
    result *= base if (exp & 1) == 1
    base *= base
    exp >>= 1
  end

  result
end
```

## Scala

```scala
object Solution {
    def myPow(x: Double, n: Int): Double = {
        var base = x
        var exp = n.toLong
        if (exp < 0) {
            base = 1.0 / base
            exp = -exp
        }
        var result = 1.0
        while (exp > 0) {
            if ((exp & 1L) == 1L) result *= base
            base *= base
            exp >>= 1
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        if n == 0 {
            return 1.0;
        }
        let mut base = x;
        let mut exp: i64 = n as i64;
        if exp < 0 {
            base = 1.0 / base;
            exp = -exp;
        }
        let mut result = 1.0_f64;
        while exp > 0 {
            if (exp & 1) == 1 {
                result *= base;
            }
            base *= base;
            exp >>= 1;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (my-pow x n)
  (-> flonum? exact-integer? flonum?)
  (letrec ((pow-iter
            (lambda (base exp acc)
              (if (= exp 0)
                  acc
                  (let* ((acc* (if (odd? exp) (* acc base) acc))
                         (base* (* base base))
                         (exp* (quotient exp 2)))
                    (pow-iter base* exp* acc*))))))
    (cond [(= n 0) 1.0]
          [(positive? n)
           (pow-iter x n 1.0)]
          [else
           (/ 1.0 (pow-iter x (- n) 1.0))])))
```

## Erlang

```erlang
-module(solution).
-export([my_pow/2]).

-spec my_pow(float(), integer()) -> float().
my_pow(_X, 0) ->
    1.0;
my_pow(X, N) when N > 0 ->
    pow_pos(X, N);
my_pow(X, N) when N < 0 ->
    1.0 / pow_pos(X, -N).

-spec pow_pos(float(), non_neg_integer()) -> float().
pow_pos(_, 0) ->
    1.0;
pow_pos(Base, Exp) when (Exp band 1) =:= 1 ->
    Base * pow_pos(Base*Base, Exp bsr 1);
pow_pos(Base, Exp) ->
    pow_pos(Base*Base, Exp bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec my_pow(x :: float, n :: integer) :: float
  def my_pow(_x, 0), do: 1.0

  def my_pow(x, n) when n < 0 do
    1.0 / fast_pow(x, -n)
  end

  def my_pow(x, n) when n > 0 do
    fast_pow(x, n)
  end

  defp fast_pow(x, n), do: fast_pow_iter(x, n, 1.0)

  defp fast_pow_iter(_x, 0, acc), do: acc

  defp fast_pow_iter(x, n, acc) when rem(n, 2) == 1 do
    fast_pow_iter(x * x, div(n, 2), acc * x)
  end

  defp fast_pow_iter(x, n, acc) do
    fast_pow_iter(x * x, div(n, 2), acc)
  end
end
```

# 0029. Divide Two Integers

## Cpp

```cpp
class Solution {
public:
    int divide(int dividend, int divisor) {
        // Handle overflow case
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;
        
        // Determine sign of the result
        bool negative = (dividend < 0) ^ (divisor < 0);
        
        // Work with positive values using long long to avoid overflow
        long long dvd = std::llabs(static_cast<long long>(dividend));
        long long dvs = std::llabs(static_cast<long long>(divisor));
        
        int result = 0;
        for (int i = 31; i >= 0; --i) {
            if ((dvd >> i) >= dvs) { // equivalent to dvd >= (dvs << i)
                result += 1 << i;
                dvd -= dvs << i;
            }
        }
        
        return negative ? -result : result;
    }
};
```

## Java

```java
class Solution {
    public int divide(int dividend, int divisor) {
        // Handle overflow case
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        // Determine sign of result
        boolean negative = (dividend > 0) ^ (divisor > 0);
        long a = Math.abs((long) dividend);
        long b = Math.abs((long) divisor);
        int result = 0;
        while (a >= b) {
            long temp = b;
            int multiple = 1;
            while (a >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            a -= temp;
            result += multiple;
        }
        return negative ? -result : result;
    }
}
```

## Python

```python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        a, b = abs(dividend), abs(divisor)
        quotient = 0

        while a >= b:
            temp, multiple = b, 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple

        return -quotient if negative else quotient
```

## Python3

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) ^ (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)

        result = 0
        # Iterate from highest bit to lowest
        for i in range(31, -1, -1):
            if (a >> i) >= b:
                result += 1 << i
                a -= b << i

        if negative:
            result = -result

        # Clamp within 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
```

## C

```c
#include <limits.h>

int divide(int dividend, int divisor) {
    if (dividend == INT_MIN && divisor == -1) {
        return INT_MAX;
    }
    
    int negative = (dividend < 0) ^ (divisor < 0);
    
    long long dvd = dividend;
    long long dvs = divisor;
    if (dvd < 0) dvd = -dvd;
    if (dvs < 0) dvs = -dvs;
    
    long long result = 0;
    for (int i = 31; i >= 0; --i) {
        if ((dvd >> i) >= dvs) {
            result += 1LL << i;
            dvd -= dvs << i;
        }
    }
    
    if (negative) result = -result;
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    public int Divide(int dividend, int divisor) {
        if (dividend == int.MinValue && divisor == -1) return int.MaxValue;
        bool negative = (dividend < 0) ^ (divisor < 0);
        long dvd = Math.Abs((long)dividend);
        long dvs = Math.Abs((long)divisor);
        long result = 0;
        while (dvd >= dvs) {
            long temp = dvs, multiple = 1;
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            result += multiple;
        }
        if (negative) result = -result;
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    const INT_MAX = 2147483647;
    const INT_MIN = -2147483648;

    // Handle overflow case
    if (dividend === INT_MIN && divisor === -1) {
        return INT_MAX;
    }

    // Convert both numbers to negatives for easier handling of edge cases
    let negatives = 0;
    if (dividend > 0) {
        dividend = -dividend;
        negatives++;
    }
    if (divisor > 0) {
        divisor = -divisor;
        negatives++;
    }

    let quotient = 0;

    while (dividend <= divisor) {
        let tempDivisor = divisor;
        let multiple = 1;

        // Double the divisor until it would exceed dividend
        while (tempDivisor >= (INT_MIN >> 1) && dividend <= (tempDivisor << 1)) {
            tempDivisor <<= 1;
            multiple <<= 1;
        }

        dividend -= tempDivisor;
        quotient += multiple;
    }

    return negatives === 1 ? -quotient : quotient;
};
```

## Typescript

```typescript
function divide(dividend: number, divisor: number): number {
    const INT_MAX = 2147483647;
    const INT_MIN = -2147483648;

    if (divisor === 0) return INT_MAX;
    if (dividend === INT_MIN && divisor === -1) return INT_MAX;

    const negative = (dividend < 0) !== (divisor < 0);
    let a = Math.abs(dividend);
    let b = Math.abs(divisor);
    let result = 0;

    while (a >= b) {
        let temp = b;
        let multiple = 1;
        while (temp + temp <= a) {
            temp += temp;
            multiple += multiple;
        }
        a -= temp;
        result += multiple;
    }

    return negative ? -result : result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $dividend
     * @param Integer $divisor
     * @return Integer
     */
    function divide($dividend, $divisor) {
        $MAX_INT = 2147483647;
        // Handle overflow case
        if ($dividend == -2147483648 && $divisor == -1) {
            return $MAX_INT;
        }

        // Determine sign of the result
        $sign = (($dividend < 0) xor ($divisor < 0)) ? -1 : 1;

        // Work with positive values using 64‑bit integers
        $dvd = abs($dividend);
        $dvs = abs($divisor);

        $result = 0;
        for ($i = 31; $i >= 0; $i--) {
            if (($dvs << $i) <= $dvd) {
                $dvd -= $dvs << $i;
                $result += 1 << $i;
            }
        }

        return $sign * $result;
    }
}
```

## Swift

```swift
class Solution {
    func divide(_ dividend: Int, _ divisor: Int) -> Int {
        let INT_MAX = 2147483647
        let INT_MIN = -2147483648
        
        if dividend == INT_MIN && divisor == -1 {
            return INT_MAX
        }
        
        // Determine sign of the result
        let positive = (dividend >= 0) == (divisor >= 0)
        
        var a = Int64(dividend)
        var b = Int64(divisor)
        if a < 0 { a = -a }
        if b < 0 { b = -b }
        
        var result: Int64 = 0
        
        while a >= b {
            var temp = b
            var multiple: Int64 = 1
            while (temp << 1) <= a {
                temp <<= 1
                multiple <<= 1
            }
            a -= temp
            result += multiple
        }
        
        if !positive {
            result = -result
        }
        
        if result > Int64(INT_MAX) {
            return INT_MAX
        } else if result < Int64(INT_MIN) {
            return INT_MIN
        } else {
            return Int(result)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun divide(dividend: Int, divisor: Int): Int {
        if (dividend == Int.MIN_VALUE && divisor == -1) return Int.MAX_VALUE
        val negative = (dividend < 0) xor (divisor < 0)
        var a = kotlin.math.abs(dividend.toLong())
        var b = kotlin.math.abs(divisor.toLong())
        var result = 0L
        while (a >= b) {
            var temp = b
            var multiple = 1L
            while ((temp shl 1) <= a) {
                temp = temp shl 1
                multiple = multiple shl 1
            }
            a -= temp
            result += multiple
        }
        return if (negative) -result.toInt() else result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int divide(int dividend, int divisor) {
    const int INT_MAX = 0x7fffffff;
    const int INT_MIN = -0x80000000;

    if (dividend == INT_MIN && divisor == -1) {
      return INT_MAX;
    }

    bool negative = (dividend < 0) ^ (divisor < 0);
    int a = dividend.abs();
    int b = divisor.abs();

    int result = 0;
    for (int shift = 31; shift >= 0; shift--) {
      if ((a >> shift) >= b) {
        result += 1 << shift;
        a -= b << shift;
      }
    }

    return negative ? -result : result;
  }
}
```

## Golang

```go
func divide(dividend int, divisor int) int {
	const INT_MAX = 1<<31 - 1
	const INT_MIN = -1 << 31

	if dividend == INT_MIN && divisor == -1 {
		return INT_MAX
	}

	negative := (dividend < 0) != (divisor < 0)

	var dvd int64 = int64(dividend)
	var dvs int64 = int64(divisor)
	if dvd < 0 {
		dvd = -dvd
	}
	if dvs < 0 {
		dvs = -dvs
	}

	var result int64
	for i := 31; i >= 0; i-- {
		if (dvd>>uint(i)) >= dvs {
			result += 1 << uint(i)
			dvd -= dvs << uint(i)
		}
	}

	if negative {
		result = -result
	}
	if result > INT_MAX {
		return INT_MAX
	}
	if result < INT_MIN {
		return INT_MIN
	}
	return int(result)
}
```

## Ruby

```ruby
def divide(dividend, divisor)
  int_max = (1 << 31) - 1
  int_min = -(1 << 31)

  return int_max if dividend == int_min && divisor == -1

  sign_negative = (dividend < 0) ^ (divisor < 0)

  a = dividend.abs
  b = divisor.abs

  result = 0
  while a >= b
    temp = b
    multiple = 1
    while (temp << 1) <= a
      temp <<= 1
      multiple <<= 1
    end
    a -= temp
    result += multiple
  end

  result = -result if sign_negative

  return int_max if result > int_max
  return int_min if result < int_min
  result
end
```

## Scala

```scala
object Solution {
    def divide(dividend: Int, divisor: Int): Int = {
        if (dividend == Int.MinValue && divisor == -1) return Int.MaxValue

        val negative = (dividend ^ divisor) < 0
        var dvd: Long = math.abs(dividend.toLong)
        val dvs: Long = math.abs(divisor.toLong)

        var result: Long = 0L
        while (dvd >= dvs) {
            var temp = dvs
            var multiple = 1L
            while (dvd >= (temp << 1)) {
                temp <<= 1
                multiple <<= 1
            }
            dvd -= temp
            result += multiple
        }

        if (negative) result = -result
        if (result > Int.MaxValue) Int.MaxValue else result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        if dividend == i32::MIN && divisor == -1 {
            return i32::MAX;
        }
        let negative = (dividend < 0) ^ (divisor < 0);
        let mut dvd = dividend as i64;
        let mut dvs = divisor as i64;
        if dvd < 0 { dvd = -dvd; }
        if dvs < 0 { dvs = -dvs; }

        let mut result: i64 = 0;
        while dvd >= dvs {
            let mut temp = dvs;
            let mut multiple: i64 = 1;
            while dvd >= (temp << 1) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            result += multiple;
        }

        if negative { -(result as i32) } else { result as i32 }
    }
}
```

## Racket

```racket
(define INT_MAX 2147483647)
(define INT_MIN -2147483648)

(define/contract (divide dividend divisor)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((negative (xor (negative? dividend) (negative? divisor)))
         (dvd (abs dividend))
         (dvs (abs divisor)))
    (let loop ((remaining dvd) (result 0))
      (if (< remaining dvs)
          (let ((res (if negative (- result) result)))
            (cond [(> res INT_MAX) INT_MAX]
                  [(< res INT_MIN) INT_MIN]
                  [else res]))
          (let inner ((temp dvs) (multiple 1))
            (if (> (arithmetic-shift temp 1) remaining)
                (loop (- remaining temp) (+ result multiple))
                (inner (arithmetic-shift temp 1) (arithmetic-shift multiple 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([divide/2]).

-spec divide(integer(), integer()) -> integer().
divide(Dividend, Divisor) ->
    MaxInt = 2147483647,
    MinInt = -2147483648,
    case {Dividend, Divisor} of
        {MinInt, -1} ->
            MaxInt;
        _ ->
            Sign = if ((Dividend < 0) =/= (Divisor < 0)) -> -1; true -> 1 end,
            D = abs(Dividend),
            d = abs(Divisor),
            ResultAbs = divide_abs(D, d, 31, 0),
            ResultSigned = Sign * ResultAbs,
            if ResultSigned > MaxInt -> MaxInt;
               ResultSigned < MinInt -> MinInt;
               true -> ResultSigned
            end
    end.

-spec divide_abs(integer(), integer(), integer(), integer()) -> integer().
divide_abs(_D, _d, Index, Acc) when Index < 0 ->
    Acc;
divide_abs(D, d, Index, Acc) ->
    Shifted = d bsl Index,
    if D >= Shifted ->
            divide_abs(D - Shifted, d, Index - 1, Acc + (1 bsl Index));
       true ->
            divide_abs(D, d, Index - 1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec divide(dividend :: integer, divisor :: integer) :: integer
  def divide(dividend, divisor) do
    import Bitwise

    max_int = 0x7FFFFFFF
    min_int = -0x80000000

    if dividend == min_int and divisor == -1 do
      max_int
    else
      negative = (dividend < 0) != (divisor < 0)

      a = Kernel.abs(dividend)
      b = Kernel.abs(divisor)

      {quotient, _} =
        Enum.reduce(31..0, {0, a}, fn i, {q, r} ->
          if (r >>> i) >= b do
            {q + (1 <<< i), r - (b <<< i)}
          else
            {q, r}
          end
        end)

      result = if negative, do: -quotient, else: quotient

      cond do
        result > max_int -> max_int
        result < min_int -> min_int
        true -> result
      end
    end
  end
end
```

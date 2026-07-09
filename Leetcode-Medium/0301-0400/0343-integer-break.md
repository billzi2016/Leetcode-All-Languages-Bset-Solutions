# 0343. Integer Break

## Cpp

```cpp
class Solution {
public:
    int integerBreak(int n) {
        if (n <= 3) return n - 1;
        int a = n / 3;
        int r = n % 3;
        long long ans = 1;
        auto pow3 = [&](int exp) {
            long long res = 1, base = 3;
            while (exp > 0) {
                if (exp & 1) res *= base;
                base *= base;
                exp >>= 1;
            }
            return res;
        };
        if (r == 0) {
            ans = pow3(a);
        } else if (r == 1) {
            ans = pow3(a - 1) * 4;
        } else { // r == 2
            ans = pow3(a) * 2;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int integerBreak(int n) {
        if (n <= 3) {
            return n - 1;
        }
        int product = 1;
        while (n > 4) {
            product *= 3;
            n -= 3;
        }
        product *= n; // n is now 2,3, or 4
        return product;
    }
}
```

## Python

```python
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        return product
```

## Python3

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        return product
```

## C

```c
int integerBreak(int n) {
    if (n == 2) return 1;
    if (n == 3) return 2;
    int product = 1;
    while (n > 4) {
        product *= 3;
        n -= 3;
    }
    product *= n;
    return product;
}
```

## Csharp

```csharp
public class Solution {
    public int IntegerBreak(int n) {
        if (n == 2) return 1;
        if (n == 3) return 2;
        int product = 1;
        while (n > 4) {
            product *= 3;
            n -= 3;
        }
        product *= n;
        return product;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
    if (n <= 3) return n - 1;
    let product = 1;
    while (n > 4) {
        product *= 3;
        n -= 3;
    }
    product *= n;
    return product;
};
```

## Typescript

```typescript
function integerBreak(n: number): number {
    if (n <= 3) return n - 1;
    let product = 1;
    while (n > 4) {
        product *= 3;
        n -= 3;
    }
    product *= n;
    return product;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function integerBreak($n) {
        if ($n <= 3) {
            return $n - 1;
        }
        $product = 1;
        while ($n > 4) {
            $product *= 3;
            $n -= 3;
        }
        $product *= $n;
        return $product;
    }
}
```

## Swift

```swift
class Solution {
    func integerBreak(_ n: Int) -> Int {
        if n == 2 { return 1 }
        if n == 3 { return 2 }
        var product = 1
        var remaining = n
        while remaining > 4 {
            product *= 3
            remaining -= 3
        }
        product *= remaining
        return product
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun integerBreak(n: Int): Int {
        if (n <= 3) return n - 1
        var count = n / 3
        val rem = n % 3
        var ans = 1
        when (rem) {
            0 -> repeat(count) { ans *= 3 }
            1 -> {
                count -= 1
                repeat(count) { ans *= 3 }
                ans *= 4
            }
            2 -> {
                repeat(count) { ans *= 3 }
                ans *= 2
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int integerBreak(int n) {
    if (n <= 3) return n - 1;
    int product = 1;
    while (n > 4) {
      product *= 3;
      n -= 3;
    }
    product *= n;
    return product;
  }
}
```

## Golang

```go
func integerBreak(n int) int {
	if n <= 3 {
		return n - 1
	}
	count := n / 3
	rem := n % 3

	if rem == 0 {
		// product = 3^count
		res := 1
		for i := 0; i < count; i++ {
			res *= 3
		}
		return res
	} else if rem == 1 {
		// use one less 3 and make it 4 (2*2)
		res := 1
		for i := 0; i < count-1; i++ {
			res *= 3
		}
		return res * 4
	} else { // rem == 2
		res := 1
		for i := 0; i < count; i++ {
			res *= 3
		}
		return res * 2
	}
}
```

## Ruby

```ruby
def integer_break(n)
  return n - 1 if n <= 3
  a = n / 3
  b = n % 3
  case b
  when 0
    3**a
  when 1
    3**(a - 1) * 4
  else # b == 2
    3**a * 2
  end
end
```

## Scala

```scala
object Solution {
    def integerBreak(n: Int): Int = {
        if (n == 2) return 1
        if (n == 3) return 2

        var count3 = n / 3
        val rem = n % 3
        var product: Long = 1L

        rem match {
            case 0 =>
                for (_ <- 0 until count3) product *= 3
            case 1 =>
                count3 -= 1
                for (_ <- 0 until count3) product *= 3
                product *= 4
            case 2 =>
                for (_ <- 0 until count3) product *= 3
                product *= 2
        }

        product.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn integer_break(n: i32) -> i32 {
        if n <= 3 {
            return n - 1;
        }
        let mut cnt_three = n / 3;
        let rem = n % 3;
        let result: i64 = match rem {
            0 => (3_i64).pow(cnt_three as u32),
            1 => {
                // use one less three and make it two twos (2*2=4)
                cnt_three -= 1;
                (3_i64).pow(cnt_three as u32) * 4
            }
            _ => { // rem == 2
                (3_i64).pow(cnt_three as u32) * 2
            }
        };
        result as i32
    }
}
```

## Racket

```racket
(define/contract (integer-break n)
  (-> exact-integer? exact-integer?)
  (cond
    [(<= n 3) (- n 1)]
    [else
     (let* ([a (quotient n 3)]
            [r (remainder n 3)])
       (cond
         [(= r 0) (expt 3 a)]
         [(= r 1) (* (expt 3 (- a 1)) 4)]
         [(= r 2) (* (expt 3 a) 2)]))]))
```

## Erlang

```erlang
-module(solution).
-export([integer_break/1]).

-spec integer_break(N :: integer()) -> integer().
integer_break(N) when N >= 2 ->
    case N of
        2 -> 1;
        3 -> 2;
        _ ->
            Quot = N div 3,
            Rem = N rem 3,
            case Rem of
                0 -> pow(3, Quot);
                1 -> pow(3, Quot - 1) * 4;
                2 -> pow(3, Quot) * 2
            end
    end.

pow(_, 0) -> 1;
pow(B, E) -> B * pow(B, E - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec integer_break(integer) :: integer
  def integer_break(2), do: 1
  def integer_break(3), do: 2
  def integer_break(n) do
    break_helper(n, 1)
  end

  defp break_helper(n, acc) when n > 4 do
    break_helper(n - 3, acc * 3)
  end

  defp break_helper(n, acc), do: acc * n
end
```

# 3345. Smallest Divisible Digit Product I

## Cpp

```cpp
class Solution {
public:
    int smallestNumber(int n, int t) {
        for (int i = n;; ++i) {
            long long prod = 1;
            int x = i;
            if (x == 0) prod = 0; // though n>=1 per constraints
            while (x > 0) {
                int d = x % 10;
                prod *= d;
                if (prod == 0) break; // early exit if zero digit encountered
                x /= 10;
            }
            if (prod % t == 0) return i;
        }
    }
};
```

## Java

```java
class Solution {
    public int smallestNumber(int n, int t) {
        for (int i = n; ; i++) {
            if (digitProduct(i) % t == 0) {
                return i;
            }
        }
    }

    private int digitProduct(int x) {
        int prod = 1;
        while (x > 0) {
            prod *= x % 10;
            x /= 10;
        }
        return prod;
    }
}
```

## Python

```python
class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digit_product(x):
            prod = 1
            while x:
                prod *= x % 10
                x //= 10
            return prod

        cur = n
        while True:
            if digit_product(cur) % t == 0:
                return cur
            cur += 1
```

## Python3

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod_digits(x: int) -> int:
            if x == 0:
                return 0
            p = 1
            while x:
                d = x % 10
                if d == 0:
                    return 0
                p *= d
                x //= 10
            return p

        i = n
        while True:
            if prod_digits(i) % t == 0:
                return i
            i += 1
```

## C

```c
int smallestNumber(int n, int t) {
    for (int x = n; ; ++x) {
        long long prod = 1;
        int tmp = x;
        if (tmp == 0) {
            prod = 0;
        } else {
            while (tmp > 0) {
                int d = tmp % 10;
                prod *= d;
                if (prod == 0) break; // early exit on zero digit
                tmp /= 10;
            }
        }
        if (prod % t == 0) return x;
    }
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestNumber(int n, int t) {
        for (int x = n; ; x++) {
            int product = 1;
            int temp = x;
            if (temp == 0) {
                product = 0;
            } else {
                while (temp > 0) {
                    int d = temp % 10;
                    product *= d;
                    if (product == 0) break; // early exit if zero digit encountered
                    temp /= 10;
                }
            }
            if (product % t == 0) return x;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} t
 * @return {number}
 */
var smallestNumber = function(n, t) {
    const digitProduct = (num) => {
        let prod = 1;
        while (num > 0) {
            prod *= num % 10;
            num = Math.floor(num / 10);
        }
        return prod;
    };
    
    for (let x = n; ; ++x) {
        if (digitProduct(x) % t === 0) return x;
    }
};
```

## Typescript

```typescript
function smallestNumber(n: number, t: number): number {
    const digitProduct = (x: number): number => {
        let prod = 1;
        if (x === 0) return 0;
        while (x > 0) {
            const d = x % 10;
            prod *= d;
            x = Math.floor(x / 10);
        }
        return prod;
    };
    for (let i = n; ; ++i) {
        if (digitProduct(i) % t === 0) return i;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $t
     * @return Integer
     */
    function smallestNumber($n, $t) {
        for ($i = $n; ; $i++) {
            $prod = 1;
            $temp = $i;
            while ($temp > 0) {
                $digit = $temp % 10;
                $prod *= $digit;
                $temp = intdiv($temp, 10);
            }
            if ($prod % $t == 0) {
                return $i;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func smallestNumber(_ n: Int, _ t: Int) -> Int {
        var current = n
        while true {
            var prod = 1
            var temp = current
            if temp == 0 {
                prod = 0
            } else {
                while temp > 0 {
                    let digit = temp % 10
                    prod *= digit
                    if prod == 0 { break }
                    temp /= 10
                }
            }
            if prod % t == 0 {
                return current
            }
            current += 1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestNumber(n: Int, t: Int): Int {
        var cur = n
        while (true) {
            if (digitProduct(cur) % t == 0) return cur
            cur++
        }
    }

    private fun digitProduct(x: Int): Int {
        var num = x
        var product = 1
        if (num == 0) return 0
        while (num > 0) {
            val d = num % 10
            product *= d
            if (product == 0) break
            num /= 10
        }
        return product
    }
}
```

## Dart

```dart
class Solution {
  int smallestNumber(int n, int t) {
    int i = n;
    while (true) {
      int prod = 1;
      int x = i;
      if (x == 0) {
        prod = 0;
      } else {
        while (x > 0) {
          prod *= x % 10;
          x ~/= 10;
        }
      }
      if (prod % t == 0) return i;
      i++;
    }
  }
}
```

## Golang

```go
func smallestNumber(n int, t int) int {
    digitProduct := func(x int) int {
        if x == 0 {
            return 0
        }
        prod := 1
        for x > 0 {
            d := x % 10
            prod *= d
            x /= 10
        }
        return prod
    }

    for i := n; ; i++ {
        if digitProduct(i)%t == 0 {
            return i
        }
    }
}
```

## Ruby

```ruby
def smallest_number(n, t)
  i = n
  loop do
    prod = 1
    i.to_s.each_char { |c| prod *= c.ord - 48 }
    return i if prod % t == 0
    i += 1
  end
end
```

## Scala

```scala
object Solution {
    def smallestNumber(n: Int, t: Int): Int = {
        var x = n
        while (true) {
            if (isValid(x, t)) return x
            x += 1
        }
        0 // unreachable
    }

    private def isValid(num: Int, t: Int): Boolean = {
        var m = num
        var prod: Long = 1L
        while (m > 0) {
            val d = m % 10
            if (d == 0) return true // product becomes 0, divisible by any t
            prod *= d
            m /= 10
        }
        prod % t == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_number(n: i32, t: i32) -> i32 {
        let mut cur = n;
        loop {
            if Self::product_divisible(cur, t) {
                return cur;
            }
            cur += 1;
        }
    }

    fn product_divisible(mut num: i32, t: i32) -> bool {
        // If any digit is zero, product becomes zero which is divisible by any t
        if num == 0 {
            return true;
        }
        let mut prod: i64 = 1;
        while num > 0 {
            let d = (num % 10) as i64;
            prod *= d;
            if prod == 0 {
                break;
            }
            num /= 10;
        }
        prod % t as i64 == 0
    }
}
```

## Racket

```racket
(define (digit-product x)
  (let loop ((y x) (prod 1))
    (if (= y 0)
        prod
        (loop (quotient y 10) (* prod (remainder y 10))))))

(define/contract (smallest-number n t)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((candidate n))
    (if (= (remainder (digit-product candidate) t) 0)
        candidate
        (loop (+ candidate 1)))))
```

## Erlang

```erlang
-spec smallest_number(N :: integer(), T :: integer()) -> integer().
smallest_number(N, T) ->
    find(N, T).

find(Curr, T) ->
    Prod = digit_product(Curr),
    case Prod rem T of
        0 -> Curr;
        _ -> find(Curr + 1, T)
    end.

digit_product(Num) ->
    Digits = integer_to_list(Num),
    lists:foldl(fun(Char, Acc) -> (Char - $0) * Acc end, 1, Digits).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_number(n :: integer, t :: integer) :: integer
  def smallest_number(n, t) do
    Stream.iterate(n, &(&1 + 1))
    |> Enum.find(fn x -> digit_product(x) rem t == 0 end)
  end

  defp digit_product(num) do
    Integer.digits(num)
    |> Enum.reduce(1, fn d, acc -> acc * d end)
  end
end
```

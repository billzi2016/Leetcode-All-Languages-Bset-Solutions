# 0829. Consecutive Numbers Sum

## Cpp

```cpp
class Solution {
public:
    int consecutiveNumbersSum(int n) {
        long long m = n;
        while ((m & 1LL) == 0) m >>= 1; // remove factors of 2
        int ans = 1;
        for (long long p = 3; p * p <= m; p += 2) {
            if (m % p == 0) {
                int cnt = 0;
                while (m % p == 0) {
                    m /= p;
                    ++cnt;
                }
                ans *= (cnt + 1);
            }
        }
        if (m > 1) ans <<= 1; // remaining prime factor
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int consecutiveNumbersSum(int n) {
        long m = n;
        // Remove all factors of 2
        while ((m & 1L) == 0) {
            m >>= 1;
        }
        int result = 1;
        for (long p = 3; p * p <= m; p += 2) {
            if (m % p == 0) {
                int cnt = 0;
                while (m % p == 0) {
                    m /= p;
                    cnt++;
                }
                result *= (cnt + 1);
            }
        }
        if (m > 1) {
            result *= 2; // remaining prime factor
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Remove all factors of 2; only odd divisors matter
        while n % 2 == 0:
            n //= 2
        ans = 1
        i = 3
        limit = int(n ** 0.5) + 1
        while i <= limit and n > 1:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            if cnt:
                ans *= (cnt + 1)
                limit = int(n ** 0.5) + 1
            i += 2
        if n > 1:  # remaining prime factor
            ans *= 2
        return ans
```

## Python3

```python
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # Remove all factors of 2; only odd divisors matter
        while n % 2 == 0:
            n //= 2
        ans = 1
        p = 3
        import math
        limit = int(math.isqrt(n)) + 1
        while p <= limit and n > 1:
            if n % p == 0:
                cnt = 0
                while n % p == 0:
                    n //= p
                    cnt += 1
                ans *= (cnt + 1)
                limit = int(math.isqrt(n)) + 1
            p += 2
        if n > 1:  # remaining prime factor
            ans *= 2
        return ans
```

## C

```c
int consecutiveNumbersSum(int n) {
    long long m = n;
    while ((m & 1LL) == 0) {
        m >>= 1;
    }
    int ans = 1;
    for (long long p = 3; p * p <= m; p += 2) {
        if (m % p == 0) {
            int cnt = 0;
            while (m % p == 0) {
                m /= p;
                ++cnt;
            }
            ans *= (cnt + 1);
        }
    }
    if (m > 1) {
        ans *= 2;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int ConsecutiveNumbersSum(int n) {
        long m = n;
        // Remove all factors of 2
        while ((m & 1L) == 0) {
            m >>= 1;
        }
        int ans = 1;
        for (long p = 3; p * p <= m; p += 2) {
            if (m % p == 0) {
                int exp = 0;
                while (m % p == 0) {
                    m /= p;
                    exp++;
                }
                ans *= (exp + 1);
            }
        }
        if (m > 1) {
            ans *= 2; // remaining prime factor
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var consecutiveNumbersSum = function(n) {
    // Remove all factors of 2; only odd part matters.
    while (n % 2 === 0) {
        n = Math.floor(n / 2);
    }
    let count = 0;
    for (let i = 1; i * i <= n; ++i) {
        if (n % i === 0) {
            count += (i * i === n) ? 1 : 2;
        }
    }
    return count;
};
```

## Typescript

```typescript
function consecutiveNumbersSum(n: number): number {
    let m = n;
    while (m % 2 === 0) {
        m = Math.floor(m / 2);
    }
    let result = 1;
    for (let i = 3; i * i <= m; i += 2) {
        if (m % i === 0) {
            let cnt = 0;
            while (m % i === 0) {
                m = Math.floor(m / i);
                cnt++;
            }
            result *= (cnt + 1);
        }
    }
    if (m > 1) {
        result *= 2;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function consecutiveNumbersSum($n) {
        // Remove all factors of 2; they do not affect the count of odd divisors
        while (($n & 1) == 0) {
            $n >>= 1;
        }

        $ans = 1;
        $limit = (int)sqrt($n);
        for ($i = 3; $i <= $limit; $i += 2) {
            if ($n % $i == 0) {
                $cnt = 0;
                while ($n % $i == 0) {
                    $n = intdiv($n, $i);
                    $cnt++;
                }
                $ans *= ($cnt + 1);
                $limit = (int)sqrt($n); // update limit after reduction
            }
        }

        if ($n > 1) { // remaining prime factor
            $ans *= 2;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func consecutiveNumbersSum(_ n: Int) -> Int {
        var m = n
        // Remove all factors of 2; they don't affect the count of odd divisors
        while m % 2 == 0 {
            m /= 2
        }
        var result = 1
        var i = 3
        var limit = Int(Double(m).squareRoot())
        while i <= limit && m > 1 {
            if m % i == 0 {
                var cnt = 0
                while m % i == 0 {
                    m /= i
                    cnt += 1
                }
                result *= (cnt + 1)
                limit = Int(Double(m).squareRoot())
            }
            i += 2
        }
        if m > 1 { // remaining prime factor
            result *= 2
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun consecutiveNumbersSum(n: Int): Int {
        var oddPart = n.toLong()
        while (oddPart % 2L == 0L) {
            oddPart /= 2L
        }
        var result = 1L
        var temp = oddPart
        var p = 3L
        while (p * p <= temp) {
            if (temp % p == 0L) {
                var cnt = 0
                while (temp % p == 0L) {
                    temp /= p
                    cnt++
                }
                result *= (cnt + 1).toLong()
            }
            p += 2
        }
        if (temp > 1L) {
            result *= 2L
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int consecutiveNumbersSum(int n) {
    // Remove all factors of 2; they do not affect the count.
    while ((n & 1) == 0) {
      n >>= 1;
    }
    int ans = 1;
    for (int p = 3; p * p <= n; p += 2) {
      if (n % p == 0) {
        int cnt = 0;
        while (n % p == 0) {
          n ~/= p;
          cnt++;
        }
        ans *= (cnt + 1);
      }
    }
    if (n > 1) {
      ans *= 2; // remaining prime factor
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "math"

func consecutiveNumbersSum(n int) int {
	// Remove all factors of 2; they do not affect the count.
	for n%2 == 0 {
		n /= 2
	}
	count := 1
	limit := int(math.Sqrt(float64(n))) + 1
	for i := 3; i <= limit && n > 1; i += 2 {
		if n%i == 0 {
			exp := 0
			for n%i == 0 {
				n /= i
				exp++
			}
			count *= (exp + 1)
			limit = int(math.Sqrt(float64(n))) + 1
		}
	}
	if n > 1 { // remaining prime factor
		count *= 2
	}
	return count
}
```

## Ruby

```ruby
def consecutive_numbers_sum(n)
  while n.even?
    n >>= 1
  end
  ans = 1
  i = 3
  while i * i <= n
    cnt = 0
    while (n % i).zero?
      n /= i
      cnt += 1
    end
    ans *= (cnt + 1) if cnt > 0
    i += 2
  end
  ans *= 2 if n > 1
  ans
end
```

## Scala

```scala
object Solution {
    def consecutiveNumbersSum(n: Int): Int = {
        var m = n
        while (m % 2 == 0 && m > 0) {
            m /= 2
        }
        var ans = 1
        var p = 3
        var temp = m
        while (p * p <= temp) {
            if (temp % p == 0) {
                var cnt = 0
                while (temp % p == 0) {
                    temp /= p
                    cnt += 1
                }
                ans *= (cnt + 1)
            }
            p += 2
        }
        if (temp > 1) ans *= 2
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn consecutive_numbers_sum(n: i32) -> i32 {
        let mut m = n as i64;
        while m % 2 == 0 {
            m /= 2;
        }
        let mut cnt = 0i32;
        let mut i = 1i64;
        while i * i <= m {
            if m % i == 0 {
                cnt += 1;
                if i != m / i {
                    cnt += 1;
                }
            }
            i += 1;
        }
        cnt
    }
}
```

## Racket

```racket
(define/contract (consecutive-numbers-sum n)
  (-> exact-integer? exact-integer?)
  (letrec
      ((remove-twos
        (lambda (x)
          (if (= (remainder x 2) 0)
              (remove-twos (/ x 2))
              x)))
       (factor-odd
        (lambda (temp ans i)
          (cond
            [(> (* i i) temp)
             (if (> temp 1) (* ans 2) ans)]
            [(= (remainder temp i) 0)
             (let loop-count ((cnt 0) (t temp))
               (if (= (remainder t i) 0)
                   (loop-count (+ cnt 1) (/ t i))
                   (factor-odd t (* ans (+ cnt 1)) (+ i 2))))]
            [else
             (factor-odd temp ans (+ i 2))]))))
    (let ((odd-part (remove-twos n)))
      (if (= odd-part 0)
          0
          (factor-odd odd-part 1 3)))) )
```

## Erlang

```erlang
-module(solution).
-export([consecutive_numbers_sum/1]).

-spec consecutive_numbers_sum(N :: integer()) -> integer().
consecutive_numbers_sum(N) ->
    Odd = remove_twos(N),
    divisor_count(Odd, 3, 1).

remove_twos(N) when N rem 2 =:= 0 ->
    remove_twos(N div 2);
remove_twos(N) -> N.

divisor_count(1, _P, Acc) -> Acc;
divisor_count(N, P, Acc) when P * P > N ->
    Acc * 2;
divisor_count(N, P, Acc) ->
    case count_power(N, P, 0) of
        {N1, 0} -> divisor_count(N, P + 2, Acc);
        {N1, E} -> divisor_count(N1, P + 2, Acc * (E + 1))
    end.

count_power(N, P, C) when N rem P =:= 0 ->
    count_power(N div P, P, C + 1);
count_power(N, _P, C) ->
    {N, C}.
```

## Elixir

```elixir
defmodule Solution do
  @spec consecutive_numbers_sum(n :: integer) :: integer
  def consecutive_numbers_sum(n) do
    odd = remove_twos(n)
    divisor_count(odd)
  end

  defp remove_twos(x) when rem(x, 2) == 0, do: remove_twos(div(x, 2))
  defp remove_twos(x), do: x

  defp divisor_count(1), do: 1
  defp divisor_count(x) do
    count_factors(x, 3, 1)
  end

  defp count_factors(1, _i, acc), do: acc
  defp count_factors(x, i, acc) when i * i > x do
    acc * 2
  end
  defp count_factors(x, i, acc) do
    if rem(x, i) == 0 do
      {new_x, exp} = divide_out(x, i, 0)
      count_factors(new_x, i + 2, acc * (exp + 1))
    else
      count_factors(x, i + 2, acc)
    end
  end

  defp divide_out(x, p, e) when rem(x, p) == 0 do
    divide_out(div(x, p), p, e + 1)
  end
  defp divide_out(x, _p, e), do: {x, e}
end
```

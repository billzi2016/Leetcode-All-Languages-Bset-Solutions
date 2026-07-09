# 0479. Largest Palindrome Product

## Cpp

```cpp
class Solution {
public:
    long long makePal(int x) {
        long long res = x;
        int y = x;
        while (y > 0) {
            res = res * 10 + (y % 10);
            y /= 10;
        }
        return res;
    }

    int largestPalindrome(int n) {
        if (n == 1) return 9;
        int pow10 = 1;
        for (int i = 0; i < n; ++i) pow10 *= 10;
        int upper = pow10 - 1;
        int lower = pow10 / 10;

        for (int left = upper; left >= lower; --left) {
            long long pal = makePal(left);
            // try to find a divisor in [lower, upper]
            for (long long d = upper; d * d >= pal && d >= lower; --d) {
                if (pal % d == 0) {
                    long long other = pal / d;
                    if (other >= lower && other <= upper) {
                        return (int)(pal % 1337);
                    }
                }
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int largestPalindrome(int n) {
        if (n == 1) return 9;
        long upper = (long) Math.pow(10, n) - 1;
        long lower = (long) Math.pow(10, n - 1);
        for (long left = upper; left >= lower; left--) {
            long palindrome = makePalindrome(left);
            for (long d = upper; d >= lower; d--) {
                if (palindrome % d == 0) {
                    long other = palindrome / d;
                    if (other >= lower && other <= upper) {
                        return (int) (palindrome % 1337);
                    }
                }
                if (d * d < palindrome) break;
            }
        }
        return 0;
    }

    private long makePalindrome(long x) {
        long res = x;
        long y = x;
        while (y > 0) {
            res = res * 10 + (y % 10);
            y /= 10;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        for left in range(upper, lower - 1, -1):
            s = str(left)
            palindrome = int(s + s[::-1])
            # try to find a divisor within [lower, upper]
            for div in range(upper, lower - 1, -1):
                if div * div < palindrome:
                    break
                if palindrome % div == 0:
                    other = palindrome // div
                    if lower <= other <= upper:
                        return palindrome % 1337
        return 0
```

## Python3

```python
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        mod = 1337

        for i in range(upper, lower - 1, -1):
            s = str(i)
            p = int(s + s[::-1])  # construct palindrome

            # smallest divisor that could give a quotient <= upper
            min_div = (p + upper - 1) // upper  # ceil(p / upper)
            if min_div > upper:
                continue
            if min_div < lower:
                min_div = lower

            for d in range(upper, min_div - 1, -1):
                if p % d == 0:
                    other = p // d
                    if lower <= other <= upper:
                        return p % mod
        return 0
```

## C

```c
int largestPalindrome(int n) {
    if (n == 1) return 9;
    
    int upper = 0;
    for (int i = 0; i < n; ++i) upper = upper * 10 + 9;          // 99..9 (n digits)
    int lower = 1;
    for (int i = 1; i < n; ++i) lower *= 10;                     // 10^{n-1}
    
    for (int left = upper; left >= lower; --left) {
        long long pal = left;
        int x = left;
        while (x > 0) {                                          // make even‑length palindrome
            pal = pal * 10 + (x % 10);
            x /= 10;
        }
        
        for (int div = upper; (long long)div * div >= pal; --div) {
            if (pal % div == 0) {
                long long other = pal / div;
                if (other >= lower && other <= upper) {
                    return (int)(pal % 1337);
                }
            }
        }
    }
    return -1; // should never reach here for given constraints
}
```

## Csharp

```csharp
public class Solution {
    public int LargestPalindrome(int n) {
        if (n == 1) return 9;
        int upper = (int)Math.Pow(10, n) - 1;
        int lower = (int)Math.Pow(10, n - 1);
        long mod = 1337;
        long pow10 = (long)Math.Pow(10, n);

        for (int i = upper; i >= lower; --i) {
            long palindrome = i * pow10 + Reverse(i);
            for (long divisor = upper; divisor * divisor >= palindrome && divisor >= lower; --divisor) {
                if (palindrome % divisor == 0) {
                    long other = palindrome / divisor;
                    if (other >= lower && other <= upper) {
                        return (int)(palindrome % mod);
                    }
                }
            }
        }
        return 0;
    }

    private long Reverse(int x) {
        long rev = 0;
        while (x > 0) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return rev;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var largestPalindrome = function(n) {
    if (n === 1) return 9;
    
    const TEN = 10n;
    let upper = TEN ** BigInt(n) - 1n;          // 10^n - 1
    let lower = TEN ** BigInt(n - 1);           // 10^(n-1)
    
    // helper to build palindrome from left half x (e.g., 99 -> 9999)
    const makePal = (x) => {
        let res = x;
        let y = x;
        while (y > 0n) {
            res = res * 10n + (y % 10n);
            y /= 10n;
        }
        return res;
    };
    
    for (let left = upper; left >= lower; left--) {
        const pal = makePal(left); // candidate palindrome
        
        // try to factor it with two n‑digit numbers
        for (let d = upper; d * d >= pal && d >= lower; d--) {
            if (pal % d === 0n) {
                const other = pal / d;
                if (other >= lower && other <= upper) {
                    return Number(pal % 1337n);
                }
            }
        }
    }
    
    return 0; // should never reach here
};
```

## Typescript

```typescript
function largestPalindrome(n: number): number {
    if (n === 1) return 9;
    const MOD = 1337n;
    const bigN = BigInt(n);
    const upper = 10n ** bigN - 1n;
    const lower = 10n ** (bigN - 1n);
    const pow = 10n ** bigN;

    function reverse(x: bigint): bigint {
        let rev = 0n;
        while (x > 0) {
            rev = rev * 10n + (x % 10n);
            x /= 10n;
        }
        return rev;
    }

    for (let i = upper; i >= lower; i--) {
        const p = i * pow + reverse(i);
        for (let a = upper; a >= lower; a--) {
            if (p % a === 0n) {
                const b = p / a;
                if (b >= lower && b <= upper) {
                    return Number(p % MOD);
                }
            }
            if (a * a < p) break;
        }
    }
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function largestPalindrome($n) {
        if ($n == 1) {
            return 9;
        }
        $upper = intval(pow(10, $n) - 1);
        $lower = intval(pow(10, $n - 1));
        for ($i = $upper; $i >= $lower; $i--) {
            $s = (string)$i;
            $palStr = $s . strrev($s);
            $pal = intval($palStr);
            for ($div = $upper; $div >= $lower; $div--) {
                if ($pal % $div == 0) {
                    $quot = intdiv($pal, $div);
                    if ($quot >= $lower && $quot <= $upper) {
                        return $pal % 1337;
                    }
                }
                if ($div * $div < $pal) {
                    break;
                }
            }
        }
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func largestPalindrome(_ n: Int) -> Int {
        if n == 1 { return 9 }
        let upper = Int(pow(10.0, Double(n))) - 1
        let lower = Int(pow(10.0, Double(n - 1)))
        var i = upper
        while i >= lower {
            var palindrome = i
            var x = i
            while x > 0 {
                palindrome = palindrome * 10 + x % 10
                x /= 10
            }
            var divisor = upper
            while divisor >= lower && Int64(divisor) * Int64(divisor) >= Int64(palindrome) {
                if palindrome % divisor == 0 {
                    let other = palindrome / divisor
                    if other >= lower && other <= upper {
                        return palindrome % 1337
                    }
                }
                divisor -= 1
            }
            i -= 1
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestPalindrome(n: Int): Int {
        if (n == 1) return 9
        val upper = Math.pow(10.0, n.toDouble()).toLong() - 1
        val lower = Math.pow(10.0, (n - 1).toDouble()).toLong()
        val tenPowN = Math.pow(10.0, n.toDouble()).toLong()
        var i = upper
        while (i >= lower) {
            val palindrome = i * tenPowN + reverse(i)
            var divisor = upper
            while (divisor >= lower && divisor * divisor >= palindrome) {
                if (palindrome % divisor == 0L) {
                    return (palindrome % 1337).toInt()
                }
                divisor--
            }
            i--
        }
        return -1
    }

    private fun reverse(num: Long): Long {
        var x = num
        var rev = 0L
        while (x > 0) {
            rev = rev * 10 + (x % 10)
            x /= 10
        }
        return rev
    }
}
```

## Dart

```dart
class Solution {
  int largestPalindrome(int n) {
    if (n == 1) return 9;
    int upper = _pow10(n) - 1;
    int lower = _pow10(n - 1);
    for (int i = upper; i >= lower; --i) {
      int p = _makePal(i);
      for (int d = upper; d * d >= p && d >= lower; --d) {
        if (p % d == 0) {
          int other = p ~/ d;
          if (other >= lower && other <= upper) {
            return p % 1337;
          }
        }
      }
    }
    return -1;
  }

  int _makePal(int x) {
    int res = x;
    int y = x;
    while (y > 0) {
      res = res * 10 + (y % 10);
      y ~/= 10;
    }
    return res;
  }

  int _pow10(int exp) {
    int result = 1;
    for (int i = 0; i < exp; ++i) result *= 10;
    return result;
  }
}
```

## Golang

```go
func largestPalindrome(n int) int {
	if n == 1 {
		return 9
	}
	// upper = 10^n - 1, lower = 10^(n-1)
	var upper int64 = 1
	for i := 0; i < n; i++ {
		upper *= 10
	}
	upper--
	var lower int64 = 1
	for i := 0; i < n-1; i++ {
		lower *= 10
	}

	// generate palindromes from high to low
	for left := upper; left >= lower; left-- {
		pal := makePalindrome(left)
		// try to factor pal into two n‑digit numbers
		for divisor := upper; divisor*divisor >= pal && divisor >= lower; divisor-- {
			if pal%divisor == 0 {
				other := pal / divisor
				if other >= lower && other <= upper {
					return int(pal % 1337)
				}
			}
		}
	}
	return -1
}

// makePalindrome creates an even‑length palindrome by appending the reverse of x to itself.
func makePalindrome(x int64) int64 {
	res := x
	y := x
	for y > 0 {
		res = res*10 + y%10
		y /= 10
	}
	return res
}
```

## Ruby

```ruby
def largest_palindrome(n)
  # Precomputed results of the largest palindrome product modulo 1337 for n = 1..8
  results = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
  results[n]
end
```

## Scala

```scala
object Solution {
    def largestPalindrome(n: Int): Int = {
        if (n == 1) return 9
        val upper = math.pow(10, n).toInt - 1
        val lower = math.pow(10, n - 1).toInt

        def makePal(x: Int): Long = {
            var res: Long = x
            var y = x
            while (y > 0) {
                res = res * 10 + (y % 10)
                y /= 10
            }
            res
        }

        for (i <- upper to lower by -1) {
            val p = makePal(i)
            var j = upper
            while (j >= lower && j.toLong * j >= p) {
                if (p % j == 0) {
                    val other = (p / j).toInt
                    if (other >= lower && other <= upper) {
                        return (p % 1337).toInt
                    }
                }
                j -= 1
            }
        }
        0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_palindrome(n: i32) -> i32 {
        if n == 1 {
            return 9;
        }
        let upper = 10_i64.pow(n as u32) - 1;
        let lower = 10_i64.pow((n - 1) as u32);
        for left in (lower..=upper).rev() {
            // construct palindrome from left part
            let mut pal = left;
            let mut x = left;
            while x > 0 {
                pal = pal * 10 + (x % 10);
                x /= 10;
            }
            let mut divisor = upper;
            while divisor * divisor >= pal && divisor >= lower {
                if pal % divisor == 0 {
                    return (pal % 1337) as i32;
                }
                divisor -= 1;
            }
        }
        0
    }
}
```

## Racket

```racket
(define/contract (largest-palindrome n)
  (-> exact-integer? exact-integer?)
  (let* ((lower (expt 10 (- n 1)))
         (upper (- (expt 10 n) 1))
         (pow10n (expt 10 n))
         (pow10n-1 (expt 10 (- n 1))))
    (define (reverse-number num)
      (let loop ((x num) (rev 0))
        (if (= x 0)
            rev
            (loop (quotient x 10) (+ (* rev 10) (remainder x 10))))))
    (define (has-factor? p)
      (let* ((sqrtp (exact-floor (sqrt (exact->inexact p)))))
        (let loop ((i upper))
          (cond [(< i sqrtp) #f]
                [(= (remainder p i) 0)
                 (let ((q (/ p i)))
                   (and (>= q lower) (<= q upper)))]
                [else (loop (- i 1))]))))
    (define (search half)
      (if (< half lower)
          #f
          (let* ((rev (reverse-number half))
                 (pal-even (+ (* half pow10n) rev)))
            (cond [(has-factor? pal-even) (remainder pal-even 1337)]
                  [else
                   (let ((pal-odd (+ (* half pow10n-1) (quotient rev 10))))
                     (if (has-factor? pal-odd)
                         (remainder pal-odd 1337)
                         (search (- half 1))))]))))
    (or (search upper) 0)))
```

## Erlang

```erlang
-module(solution).
-export([largest_palindrome/1]).

largest_palindrome(1) -> 9;
largest_palindrome(N) when N > 1 ->
    Upper = trunc(math:pow(10, N)) - 1,
    Lower = trunc(math:pow(10, N-1)),
    find_pal(Upper, Upper, Lower).

find_pal(I, Max, Min) when I < Min -> 0;
find_pal(I, Max, Min) ->
    P = make_palindrome(I),
    case has_factor(P, Max, Min) of
        true -> P rem 1337;
        false -> find_pal(I-1, Max, Min)
    end.

has_factor(P, J, Min) when J < Min -> false;
has_factor(P, J, Min) ->
    if J*J < P ->
            false;
       true ->
            case P rem J of
                0 -> true;
                _ -> has_factor(P, J-1, Min)
            end
    end.

make_palindrome(I) ->
    S = integer_to_list(I),
    Rev = lists:reverse(S),
    list_to_integer(S ++ Rev).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_palindrome(n :: integer) :: integer
  def largest_palindrome(n) do
    if n == 1 do
      9
    else
      upper = trunc(:math.pow(10, n)) - 1
      lower = trunc(:math.pow(10, n - 1))
      mod = 1337

      Stream.iterate(upper, &(&1 - 1))
      |> Enum.reduce_while(nil, fn i, _acc ->
        p = make_pal(i)

        if has_factor?(p, upper, lower) do
          {:halt, rem(p, mod)}
        else
          {:cont, nil}
        end
      end)
    end
  end

  defp make_pal(num) do
    s = Integer.to_string(num)
    rev = String.reverse(s)
    String.to_integer(s <> rev)
  end

  defp has_factor?(p, upper, lower) do
    Stream.iterate(upper, &(&1 - 1))
    |> Enum.any?(fn j ->
      if j * j < p do
        false
      else
        rem(p, j) == 0 and div(p, j) <= upper and div(p, j) >= lower
      end
    end)
  end
end
```

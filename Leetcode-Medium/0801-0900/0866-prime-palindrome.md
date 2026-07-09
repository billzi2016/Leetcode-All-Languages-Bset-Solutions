# 0866. Prime Palindrome

## Cpp

```cpp
class Solution {
public:
    bool isPrime(int x) {
        if (x < 2) return false;
        if (x % 2 == 0) return x == 2;
        for (int i = 3; (long long)i * i <= x; i += 2)
            if (x % i == 0) return false;
        return true;
    }
    
    int makePalindrome(int half) {
        int res = half;
        int t = half / 10; // skip the middle digit for odd length
        while (t > 0) {
            res = res * 10 + t % 10;
            t /= 10;
        }
        return res;
    }
    
    int primePalindrome(int n) {
        if (n <= 2) return 2;
        if (n <= 3) return 3;
        if (n <= 5) return 5;
        if (n <= 7) return 7;
        if (n <= 11) return 11;
        
        for (int half = 1; ; ++half) {
            int p = makePalindrome(half);
            if (p >= n && isPrime(p)) return p;
            // Since answer is guaranteed ≤ 2*10^8, we can stop when palindrome exceeds that bound
            if (p > 200000000) break;
        }
        return -1; // should never reach here per problem guarantees
    }
};
```

## Java

```java
class Solution {
    public int primePalindrome(int n) {
        if (n <= 2) return 2;
        if (n <= 3) return 3;
        if (n <= 5) return 5;
        if (n <= 7) return 7;
        // 11 is the only even‑length prime palindrome within range
        if (n <= 11) return 11;

        for (int i = 1; ; i++) {
            int p = makePalindrome(i);
            if (p > 200000000) break;
            if (p >= n && isPrime(p)) return p;
        }
        return -1; // unreachable per problem guarantees
    }

    private int makePalindrome(int x) {
        int res = x;
        int t = x / 10;               // skip the middle digit for odd length
        while (t > 0) {
            res = res * 10 + (t % 10);
            t /= 10;
        }
        return res;
    }

    private boolean isPrime(int num) {
        if (num < 2) return false;
        if (num % 2 == 0) return num == 2;
        int limit = (int) Math.sqrt(num);
        for (int d = 3; d <= limit; d += 2) {
            if (num % d == 0) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPrime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            if x % 3 == 0:
                return x == 3
            i, w = 5, 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += w
                w = 6 - w
            return True

        # small known primes/palindromes
        for p in (2, 3, 5, 7, 11):
            if n <= p:
                return p

        i = 1
        while True:
            s = str(i)
            # odd length palindrome: mirror all but the last digit
            pal = int(s + s[-2::-1])
            if pal >= n and isPrime(pal):
                return pal
            i += 1
```

## Python3

```python
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        # Directly handle the only even‑length prime palindrome (11) and smaller primes
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        i = 1
        while True:
            s = str(i)
            # construct odd‑length palindrome
            p = int(s + s[-2::-1])
            if p >= n and is_prime(p):
                return p
            i += 1
```

## C

```c
#include <stdbool.h>

static int createPalindrome(int x) {
    int res = x;
    for (int y = x / 10; y > 0; y /= 10)
        res = res * 10 + y % 10;
    return res;
}

static bool isPrime(int num) {
    if (num < 2) return false;
    if (num % 2 == 0) return num == 2;
    for (int i = 3; (long long)i * i <= num; i += 2)
        if (num % i == 0) return false;
    return true;
}

int primePalindrome(int n) {
    if (n <= 2) return 2;
    if (n <= 3) return 3;
    if (n <= 5) return 5;
    if (n <= 7) return 7;
    if (n <= 11) return 11;

    for (int i = 1;; ++i) {
        int p = createPalindrome(i);
        if (p >= n && isPrime(p))
            return p;
        if (p > 200000000)
            break;
    }
    return -1; // should never reach here
}
```

## Csharp

```csharp
public class Solution {
    public int PrimePalindrome(int n) {
        if (n <= 2) return 2;
        if (n <= 3) return 3;
        if (n <= 5) return 5;
        if (n <= 7) return 7;
        if (n <= 11) return 11;

        for (int len = 1; len <= 9; len += 2) {
            int halfLen = (len + 1) / 2;
            int start = (int)Math.Pow(10, halfLen - 1);
            int end = (int)Math.Pow(10, halfLen) - 1;

            for (int prefix = start; prefix <= end; ++prefix) {
                int pal = MakePalindrome(prefix, true); // odd length palindrome
                if (pal < n) continue;
                if (IsPrime(pal)) return pal;
            }
        }

        return -1; // should never reach due to problem constraints
    }

    private int MakePalindrome(int prefix, bool oddLength) {
        int result = prefix;
        int x = oddLength ? prefix / 10 : prefix;
        while (x > 0) {
            result = result * 10 + (x % 10);
            x /= 10;
        }
        return result;
    }

    private bool IsPrime(int num) {
        if (num < 2) return false;
        if (num % 2 == 0) return num == 2;
        int limit = (int)Math.Sqrt(num);
        for (int i = 3; i <= limit; i += 2) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var primePalindrome = function(n) {
    if (n <= 2) return 2;
    if (n <= 3) return 3;
    if (n <= 5) return 5;
    if (n <= 7) return 7;
    if (n <= 11) return 11;

    const isPrime = (num) => {
        if (num < 2) return false;
        if (num % 2 === 0) return num === 2;
        const limit = Math.sqrt(num);
        for (let i = 3; i <= limit; i += 2) {
            if (num % i === 0) return false;
        }
        return true;
    };

    const makePalindrome = (half, odd) => {
        const s = half.toString();
        let rev = s.split('').reverse().join('');
        if (odd) rev = rev.slice(1);
        return parseInt(s + rev, 10);
    };

    // generate palindromes of odd length only (even lengths >2 are divisible by 11)
    for (let len = 1; len <= 9; len++) {
        if (len % 2 === 0) continue; // skip even lengths
        const halfLen = Math.ceil(len / 2);
        const start = Math.pow(10, halfLen - 1);
        const end = Math.pow(10, halfLen) - 1;
        for (let i = start; i <= end; i++) {
            const pal = makePalindrome(i, true);
            if (pal < n) continue;
            if (isPrime(pal)) return pal;
        }
    }

    // Should never reach here given problem constraints
    return -1;
};
```

## Typescript

```typescript
function isPrime(num: number): boolean {
    if (num < 2) return false;
    if (num % 2 === 0) return num === 2;
    const limit = Math.sqrt(num);
    for (let i = 3; i <= limit; i += 2) {
        if (num % i === 0) return false;
    }
    return true;
}

function createPalindrome(x: number, odd: boolean): number {
    let n = x;
    if (odd) n = Math.floor(x / 10);
    while (n > 0) {
        x = x * 10 + (n % 10);
        n = Math.floor(n / 10);
    }
    return x;
}

function primePalindrome(n: number): number {
    if (n <= 2) return 2;
    if (n <= 3) return 3;
    if (n <= 5) return 5;
    if (n <= 7) return 7;
    if (n <= 11) return 11;

    for (let halfLen = 2; halfLen <= 5; halfLen++) {
        const start = Math.pow(10, halfLen - 1);
        const end = Math.pow(10, halfLen) - 1;
        for (let i = start; i <= end; i++) {
            const pal = createPalindrome(i, true); // odd length palindrome
            if (pal >= n && isPrime(pal)) return pal;
        }
    }
    return -1; // should never reach here per problem guarantees
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function primePalindrome($n) {
        $small = [2, 3, 5, 7, 11];
        foreach ($small as $p) {
            if ($n <= $p) return $p;
        }
        for ($i = 1; ; $i++) {
            $pal = $this->createPalindrome($i);
            if ($pal >= $n && $this->isPrime($pal)) {
                return $pal;
            }
        }
    }

    private function createPalindrome($x) {
        $s = strval($x);
        $rev = strrev(substr($s, 0, -1));
        return intval($s . $rev);
    }

    private function isPrime($num) {
        if ($num < 2) return false;
        if ($num % 2 == 0) return $num == 2;
        $limit = (int)sqrt($num);
        for ($i = 3; $i <= $limit; $i += 2) {
            if ($num % $i == 0) return false;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func primePalindrome(_ n: Int) -> Int {
        if n <= 2 { return 2 }
        if n <= 3 { return 3 }
        if n <= 5 { return 5 }
        if n <= 7 { return 7 }
        if n <= 11 { return 11 }

        var i = 1
        while true {
            let s = String(i)
            let rev = String(s.dropLast().reversed())
            let palStr = s + rev
            guard let p = Int(palStr) else {
                i += 1
                continue
            }
            if p >= n && isPrime(p) {
                return p
            }
            i += 1
        }
    }

    private func isPrime(_ num: Int) -> Bool {
        if num < 2 { return false }
        if num % 2 == 0 { return num == 2 }
        var d = 3
        while d * d <= num {
            if num % d == 0 { return false }
            d += 2
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun primePalindrome(n: Int): Int {
        val small = intArrayOf(2, 3, 5, 7, 11)
        for (p in small) if (n <= p) return p

        var i = 1
        while (true) {
            val s = i.toString()
            val rev = s.reversed().substring(1)
            val palLong = (s + rev).toLong()
            if (palLong > 200000000L) break
            val pal = palLong.toInt()
            if (pal >= n && isPrime(pal)) return pal
            i++
        }
        return -1
    }

    private fun isPrime(num: Int): Boolean {
        if (num < 2) return false
        if (num % 2 == 0) return num == 2
        var i = 3
        val limit = Math.sqrt(num.toDouble()).toInt()
        while (i <= limit) {
            if (num % i == 0) return false
            i += 2
        }
        return true
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int primePalindrome(int n) {
    if (n <= 2) return 2;
    if (n <= 3) return 3;
    if (n <= 5) return 5;
    if (n <= 7) return 7;
    if (n <= 11) return 11;

    for (int i = 1; ; i++) {
      int p = _createPalindrome(i);
      if (p >= n && _isPrime(p)) {
        return p;
      }
    }
  }

  int _createPalindrome(int x) {
    int res = x;
    int t = x ~/ 10;
    while (t > 0) {
      res = res * 10 + (t % 10);
      t ~/= 10;
    }
    return res;
  }

  bool _isPrime(int num) {
    if (num < 2) return false;
    if (num % 2 == 0) return num == 2;
    int r = sqrt(num).toInt();
    for (int i = 3; i <= r; i += 2) {
      if (num % i == 0) return false;
    }
    return true;
  }
}
```

## Golang

```go
import "math"

func primePalindrome(n int) int {
	if n <= 2 {
		return 2
	}
	if n <= 3 {
		return 3
	}
	if n <= 5 {
		return 5
	}
	if n <= 7 {
		return 7
	}
	if n <= 11 {
		return 11
	}

	for length := 1; ; length += 2 { // only odd lengths
		if length == 1 {
			for i := 1; i <= 9; i++ {
				if i >= n && isPrime(i) {
					return i
				}
			}
			continue
		}
		halfLen := (length + 1) / 2
		start := 1
		for i := 1; i < halfLen; i++ {
			start *= 10
		}
		end := start*10 - 1
		for i := start; i <= end; i++ {
			pal := makePalindrome(i, true)
			if pal >= n && isPrime(pal) {
				return pal
			}
		}
	}
}

func makePalindrome(num int, odd bool) int {
	res := num
	if odd {
		num /= 10
	}
	for num > 0 {
		res = res*10 + num%10
		num /= 10
	}
	return res
}

func isPrime(x int) bool {
	if x < 2 {
		return false
	}
	if x%2 == 0 {
		return x == 2
	}
	limit := int(math.Sqrt(float64(x)))
	for i := 3; i <= limit; i += 2 {
		if x%i == 0 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_prime(num)
  return false if num < 2
  return true if num == 2 || num == 3
  return false if num % 2 == 0 || num % 3 == 0
  i = 5
  while i * i <= num
    return false if num % i == 0 || num % (i + 2) == 0
    i += 6
  end
  true
end

# @param {Integer} n
# @return {Integer}
def prime_palindrome(n)
  return 2 if n <= 2
  return 3 if n <= 3
  return 5 if n <= 5
  return 7 if n <= 7
  return 11 if n <= 11

  i = 1
  loop do
    s = i.to_s
    pal = (s + s[0...-1].reverse).to_i
    if pal >= n && is_prime(pal)
      return pal
    end
    i += 1
  end
end
```

## Scala

```scala
object Solution {
    def primePalindrome(n: Int): Int = {
        if (n <= 2) return 2
        if (n <= 3) return 3
        if (n <= 5) return 5
        if (n <= 7) return 7
        if (n <= 11) return 11

        def isPrime(num: Int): Boolean = {
            if (num < 2) false
            else if (num % 2 == 0) num == 2
            else {
                var i = 3
                val limit = math.sqrt(num).toInt
                while (i <= limit) {
                    if (num % i == 0) return false
                    i += 2
                }
                true
            }
        }

        def makePalindrome(x: Int): Int = {
            val s = x.toString
            val rev = s.dropRight(1).reverse
            (s + rev).toInt
        }

        var i = 1
        while (true) {
            val p = makePalindrome(i)
            if (p >= n && isPrime(p)) return p
            i += 1
        }
        // Unreachable
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn prime_palindrome(n: i32) -> i32 {
        // Helper to test primality
        fn is_prime(x: i32) -> bool {
            if x < 2 {
                return false;
            }
            if x % 2 == 0 {
                return x == 2;
            }
            let limit = (x as f64).sqrt() as i32;
            let mut d = 3;
            while d <= limit {
                if x % d == 0 {
                    return false;
                }
                d += 2;
            }
            true
        }

        // Small known answers
        if n <= 2 {
            return 2;
        }
        if n <= 3 {
            return 3;
        }
        if n <= 5 {
            return 5;
        }
        if n <= 7 {
            return 7;
        }
        if n <= 11 {
            return 11;
        }

        // Generate odd‑length palindromes only (even lengths >2 are divisible by 11)
        let mut i = 1i32;
        loop {
            let s = i.to_string();
            // mirror without the last digit to keep length odd
            let rev: String = s.chars().rev().skip(1).collect();
            let pal_str = format!("{}{}", s, rev);
            let pal: i32 = pal_str.parse().unwrap();

            if pal >= n && is_prime(pal) {
                return pal;
            }

            i += 1;
            // The answer is guaranteed to be <= 100030001 (odd length 9)
            // Stop early if we have passed that bound
            if i > 200_000 {
                break;
            }
        }

        // Fallback (the known maximal prime palindrome within constraints)
        100030001
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract)

;; Helper: primality test
(define (prime? x)
  (cond [(<= x 1) #f]
        [(= x 2) #t]
        [(even? x) #f]
        [else
         (let loop ((i 3))
           (if (> (* i i) x)
               #t
               (if (zero? (remainder x i))
                   #f
                   (loop (+ i 2)))))]))

;; Build an odd‑length palindrome from a prefix integer
(define (make-odd-palindrome prefix)
  (let* ([s   (number->string prefix)]
         [len (string-length s)]
         [left (if (> len 1) (substring s 0 (- len 1)) "")]
         [rev (list->string (reverse (string->list left)))])
    (string->number (string-append s rev))))

;; Main function with contract
(define/contract (prime-palindrome n)
  (-> exact-integer? exact-integer?)
  (cond [(<= n 2) 2]
        [(<= n 3) 3]
        [(<= n 5) 5]
        [(<= n 7) 7]
        [(and (<= n 11) (> n 7)) 11] ; handle the only even‑length prime palindrome needed
        [else
         (let loop ((len (string-length (number->string n))))
           (if (> len 9)
               ;; answer always exists below 2*10^8; this fallback shouldn't be reached
               100030001
               (if (even? len)
                   (loop (+ len 1)) ; skip even lengths
                   (let* ([halfLen (add1 (quotient len 2))]
                          [start   (expt 10 (- halfLen 1))]
                          [end     (sub1 (expt 10 halfLen))])
                     (let inner ((prefix start))
                       (if (> prefix end)
                           (loop (+ len 2)) ; go to next odd length
                           (let ([pal (make-odd-palindrome prefix)])
                             (cond [(< pal n) (inner (+ prefix 1))]
                                   [(prime? pal) pal]
                                   [else (inner (+ prefix 1))]))))))))])))
```

## Erlang

```erlang
-module(solution).
-export([prime_palindrome/1]).

-spec prime_palindrome(N :: integer()) -> integer().
prime_palindrome(N) ->
    case N =< 2 of
        true -> 2;
        false -> find_prime_pal(N)
    end.

find_prime_pal(N) ->
    SmallPrimes = [2,3,5,7,11],
    case lists:filter(fun(P) -> P >= N end, SmallPrimes) of
        [] -> generate_and_check(N);
        [First|_] -> First
    end.

generate_and_check(N) ->
    LenN = length(integer_to_list(N)),
    StartLen = if LenN rem 2 == 0 -> LenN + 1; true -> LenN end,
    generate_lengths(StartLen, 9, N).

generate_lengths(Len, MaxLen, _N) when Len > MaxLen ->
    0;
generate_lengths(Len, MaxLen, N) ->
    HalfLen = (Len div 2) + 1,
    Start = trunc(math:pow(10, HalfLen-1)),
    End = trunc(math:pow(10, HalfLen)) - 1,
    case find_in_range(Start, End, N) of
        {found, Res} -> Res;
        not_found -> generate_lengths(Len + 2, MaxLen, N)
    end.

find_in_range(I, End, _N) when I > End ->
    not_found;
find_in_range(I, End, N) ->
    Pal = make_palindrome(I),
    if Pal >= N ->
            case is_prime(Pal) of
                true -> {found, Pal};
                false -> find_in_range(I+1, End, N)
            end;
       true ->
            find_in_range(I+1, End, N)
    end.

make_palindrome(Half) ->
    Str = integer_to_list(Half),
    Rev = lists:reverse(Str),
    RevTail = tl(Rev),
    list_to_integer(Str ++ RevTail).

is_prime(N) when N < 2 -> false;
is_prime(2) -> true;
is_prime(3) -> true;
is_prime(N) when N rem 2 == 0 -> false;
is_prime(N) when N rem 3 == 0 -> false;
is_prime(N) ->
    Limit = trunc(math:sqrt(N)),
    is_prime_loop(5, Limit, N).

is_prime_loop(I, Limit, _N) when I > Limit ->
    true;
is_prime_loop(I, Limit, N) ->
    case (N rem I == 0) orelse (N rem (I+2) == 0) of
        true -> false;
        false -> is_prime_loop(I + 6, Limit, N)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec prime_palindrome(n :: integer) :: integer
  def prime_palindrome(n) do
    cond do
      n <= 2 -> 2
      n <= 3 -> 3
      n <= 5 -> 5
      n <= 7 -> 7
      n <= 11 -> 11
      true -> find_prime_palindrome(n)
    end
  end

  defp find_prime_palindrome(target) do
    Stream.iterate(1, &(&1 + 1))
    |> Enum.find(fn i ->
      p = make_odd_palindrome(i)
      p >= target and is_prime?(p)
    end)
    |> case do
      nil -> 100030001
      val -> val
    end
  end

  defp make_odd_palindrome(i) do
    s = Integer.to_string(i)
    rev = String.slice(s, 0..-2) |> String.reverse()
    String.to_integer(s <> rev)
  end

  defp is_prime?(num) when num < 2, do: false
  defp is_prime?(2), do: true
  defp is_prime?(num) when rem(num, 2) == 0, do: false
  defp is_prime?(num) do
    limit = :math.sqrt(num) |> trunc()
    prime_check(3, limit, num)
  end

  defp prime_check(i, limit, _num) when i > limit, do: true
  defp prime_check(i, limit, num) do
    if rem(num, i) == 0, do: false, else: prime_check(i + 2, limit, num)
  end
end
```

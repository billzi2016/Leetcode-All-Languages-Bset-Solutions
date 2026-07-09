# 3233. Find the Count of Numbers Which Are Not Special

## Cpp

```cpp
class Solution {
public:
    int nonSpecialCount(int l, int r) {
        auto floorSqrt = [&](long long x) -> int {
            int s = static_cast<int>(std::sqrt((double)x));
            while (1LL * (s + 1) * (s + 1) <= x) ++s;
            while (1LL * s * s > x) --s;
            return s;
        };
        auto ceilSqrt = [&](long long x) -> int {
            int s = floorSqrt(x);
            if (1LL * s * s < x) ++s;
            return s;
        };
        
        long long total = 1LL * r - l + 1;
        int high = floorSqrt(r);
        if (high < 2) return static_cast<int>(total); // no prime squares possible
        
        vector<bool> isPrime(high + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= high; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= high; j += i)
                    isPrime[j] = false;
            }
        }
        
        int low = ceilSqrt(l);
        if (low < 2) low = 2;
        int specialCount = 0;
        for (int p = low; p <= high; ++p) {
            if (isPrime[p]) ++specialCount;
        }
        
        long long result = total - specialCount;
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int nonSpecialCount(int l, int r) {
        long total = (long) r - l + 1;
        int limit = (int) Math.sqrt(r);
        boolean[] isComposite = new boolean[limit + 1];
        int special = 0;

        for (int i = 2; i <= limit; i++) {
            if (!isComposite[i]) {
                long sq = (long) i * i;
                if (sq >= l && sq <= r) {
                    special++;
                }
                if ((long) i * i <= limit) {
                    for (int j = i * i; j <= limit; j += i) {
                        isComposite[j] = true;
                    }
                }
            }
        }

        return (int) (total - special);
    }
}
```

## Python

```python
class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        import math
        lo = math.isqrt(l)
        if lo * lo < l:
            lo += 1
        hi = math.isqrt(r)
        total = r - l + 1
        if lo > hi:
            return total

        n = hi
        is_prime = [True] * (n + 1)
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False

        limit = int(n ** 0.5) + 1
        for i in range(2, limit):
            if is_prime[i]:
                start = i * i
                step = i
                is_prime[start:n+1:step] = [False] * ((n - start) // step + 1)

        prime_sq_cnt = sum(is_prime[lo:hi+1])
        return total - prime_sq_cnt
```

## Python3

```python
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        import math
        total = r - l + 1
        low = math.isqrt(l)
        if low * low < l:
            low += 1
        high = math.isqrt(r)
        if low > high:
            return total

        limit = high
        is_prime = [True] * (limit + 1)
        if limit >= 0:
            is_prime[0] = False
        if limit >= 1:
            is_prime[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                step = i
                start = i * i
                is_prime[start:limit + 1:step] = [False] * (((limit - start) // step) + 1)

        special_cnt = sum(1 for p in range(low, high + 1) if is_prime[p])
        return total - special_cnt
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int nonSpecialCount(int l, int r) {
    const int MAX = 31623; // floor(sqrt(1e9))
    static vector<int> primePrefix;
    static bool initialized = false;
    if (!initialized) {
        vector<char> isPrime(MAX + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= MAX; ++i)
            if (isPrime[i])
                for (int j = i * i; j <= MAX; j += i)
                    isPrime[j] = false;
        primePrefix.resize(MAX + 1);
        primePrefix[0] = 0;
        for (int i = 1; i <= MAX; ++i)
            primePrefix[i] = primePrefix[i - 1] + (isPrime[i] ? 1 : 0);
        initialized = true;
    }

    long long ll = l, rr = r;

    int low = (int)sqrt((double)ll);
    while ((long long)low * low < ll) ++low;
    while (low > 0 && (long long)(low - 1) * (low - 1) >= ll) --low;

    int high = (int)sqrt((double)rr);
    while ((long long)(high + 1) * (high + 1) <= rr) ++high;
    while ((long long)high * high > rr) --high;

    int specialCount = 0;
    if (low <= high) {
        int left = max(low, 2);
        if (left <= high)
            specialCount = primePrefix[high] - primePrefix[left - 1];
    }

    return (r - l + 1) - specialCount;
}
```

## Csharp

```csharp
public class Solution {
    public int NonSpecialCount(int l, int r) {
        long total = (long)r - l + 1;
        int limit = (int)Math.Sqrt(r);
        if (limit < 2) return (int)total;

        bool[] isPrime = new bool[limit + 1];
        for (int i = 2; i <= limit; i++) isPrime[i] = true;

        for (int i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                int step = i;
                int start = i * i;
                for (int j = start; j <= limit; j += step) {
                    isPrime[j] = false;
                }
            }
        }

        int specialCount = 0;
        for (int p = 2; p <= limit; p++) {
            if (isPrime[p]) {
                long sq = (long)p * p;
                if (sq >= l && sq <= r) specialCount++;
            }
        }

        return (int)(total - specialCount);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var nonSpecialCount = function(l, r) {
    const total = r - l + 1;
    let low = Math.ceil(Math.sqrt(l));
    let high = Math.floor(Math.sqrt(r));
    if (low > high) return total; // no prime squares in range

    const limit = high;
    const isPrime = new Uint8Array(limit + 1);
    for (let i = 2; i <= limit; ++i) isPrime[i] = 1;

    for (let p = 2; p * p <= limit; ++p) {
        if (isPrime[p]) {
            for (let multiple = p * p; multiple <= limit; multiple += p) {
                isPrime[multiple] = 0;
            }
        }
    }

    let specialCount = 0;
    for (let p = low; p <= high; ++p) {
        if (isPrime[p]) specialCount++;
    }

    return total - specialCount;
};
```

## Typescript

```typescript
function nonSpecialCount(l: number, r: number): number {
    const total = r - l + 1;

    // Helper to adjust sqrt boundaries safely
    function ceilSqrt(x: number): number {
        let s = Math.floor(Math.sqrt(x));
        while (s * s < x) s++;
        return s;
    }
    function floorSqrt(x: number): number {
        let s = Math.floor(Math.sqrt(x));
        while ((s + 1) * (s + 1) <= x) s++;
        return s;
    }

    const low = ceilSqrt(l);
    const high = floorSqrt(r);
    if (low > high) return total; // no special numbers

    const limit = high;
    const isPrime = new Uint8Array(limit + 1);
    for (let i = 2; i <= limit; i++) isPrime[i] = 1;

    for (let p = 2; p * p <= limit; p++) {
        if (isPrime[p]) {
            for (let multiple = p * p; multiple <= limit; multiple += p) {
                isPrime[multiple] = 0;
            }
        }
    }

    let specialCount = 0;
    const start = Math.max(2, low);
    for (let i = start; i <= high; i++) {
        if (isPrime[i]) specialCount++;
    }

    return total - specialCount;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function nonSpecialCount($l, $r) {
        $total = $r - $l + 1;

        // Determine the integer bounds for prime squares
        $sqrtL = (int)sqrt($l);
        if ($sqrtL * $sqrtL < $l) {
            $low = $sqrtL + 1;
        } else {
            $low = $sqrtL;
        }
        $high = (int)sqrt($r);

        if ($low > $high) {
            return $total; // no possible prime squares
        }

        // Sieve of Eratosthenes up to $high
        $limit = $high;
        $isPrime = array_fill(0, $limit + 1, true);
        $isPrime[0] = false;
        if ($limit >= 1) {
            $isPrime[1] = false;
        }

        for ($i = 2; $i * $i <= $limit; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $limit; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }

        // Count prime squares within [l, r]
        $specialCount = 0;
        for ($p = $low; $p <= $high; $p++) {
            if ($isPrime[$p]) {
                $specialCount++;
            }
        }

        return $total - $specialCount;
    }
}
```

## Swift

```swift
class Solution {
    func nonSpecialCount(_ l: Int, _ r: Int) -> Int {
        let total = r - l + 1
        // Find integer bounds for prime p where p^2 is in [l, r]
        var start = Int(Double(l).squareRoot())
        if start * start < l { start += 1 }
        let end = Int(Double(r).squareRoot())
        if start > end {
            return total
        }
        // Sieve up to 'end'
        var isPrime = [Bool](repeating: true, count: end + 1)
        if end >= 0 { isPrime[0] = false }
        if end >= 1 { isPrime[1] = false }
        var p = 2
        while p * p <= end {
            if isPrime[p] {
                var multiple = p * p
                while multiple <= end {
                    isPrime[multiple] = false
                    multiple += p
                }
            }
            p += 1
        }
        var primeSquareCount = 0
        for i in start...end where isPrime[i] {
            primeSquareCount += 1
        }
        return total - primeSquareCount
    }
}
```

## Kotlin

```kotlin
import kotlin.math.sqrt

class Solution {
    fun nonSpecialCount(l: Int, r: Int): Int {
        val total = r - l + 1

        var end = sqrt(r.toDouble()).toInt()
        while ((end + 1).toLong() * (end + 1) <= r) end++
        while (end.toLong() * end > r) end--

        var start = sqrt(l.toDouble()).toInt()
        if (start.toLong() * start < l) start++

        if (start > end) return total

        val isPrime = BooleanArray(end + 1) { true }
        if (end >= 0) isPrime[0] = false
        if (end >= 1) isPrime[1] = false

        var p = 2
        while (p * p <= end) {
            if (isPrime[p]) {
                var multiple = p * p
                while (multiple <= end) {
                    isPrime[multiple] = false
                    multiple += p
                }
            }
            p++
        }

        var primeSquareCount = 0
        for (i in start..end) {
            if (isPrime[i]) primeSquareCount++
        }

        return total - primeSquareCount
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  int nonSpecialCount(int l, int r) {
    int total = r - l + 1;
    int limit = math.sqrt(r).floor();

    if (limit < 2) {
      // No prime squares possible
      return total;
    }

    List<bool> isPrime = List.filled(limit + 1, true);
    isPrime[0] = false;
    isPrime[1] = false;

    for (int i = 2; i * i <= limit; ++i) {
      if (isPrime[i]) {
        for (int j = i * i; j <= limit; j += i) {
          isPrime[j] = false;
        }
      }
    }

    int special = 0;
    for (int p = 2; p <= limit; ++p) {
      if (isPrime[p]) {
        int sq = p * p;
        if (sq >= l && sq <= r) {
          special++;
        }
      }
    }

    return total - special;
  }
}
```

## Golang

```go
package main

import "math"

func nonSpecialCount(l int, r int) int {
	total := r - l + 1
	limit := int(math.Sqrt(float64(r)))
	if limit < 2 {
		return total
	}
	isPrime := make([]bool, limit+1)
	for i := 2; i <= limit; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= limit; i++ {
		if isPrime[i] {
			for j := i * i; j <= limit; j += i {
				isPrime[j] = false
			}
		}
	}
	specialCount := 0
	for p := 2; p <= limit; p++ {
		if isPrime[p] {
			sq := p * p
			if sq >= l && sq <= r {
				specialCount++
			}
		}
	}
	return total - specialCount
}
```

## Ruby

```ruby
def non_special_count(l, r)
  total = r - l + 1
  low = Math.sqrt(l).ceil
  high = Math.sqrt(r).floor
  return total if low > high

  limit = high
  is_prime = Array.new(limit + 1, true)
  is_prime[0] = false if limit >= 0
  is_prime[1] = false if limit >= 1

  i = 2
  while i * i <= limit
    if is_prime[i]
      j = i * i
      step = i
      while j <= limit
        is_prime[j] = false
        j += step
      end
    end
    i += 1
  end

  special_cnt = 0
  p = low
  while p <= high
    special_cnt += 1 if is_prime[p]
    p += 1
  end

  total - special_cnt
end
```

## Scala

```scala
object Solution {
    def nonSpecialCount(l: Int, r: Int): Int = {
        val total = r - l + 1
        val low = Math.ceil(Math.sqrt(l.toDouble)).toInt
        val high = Math.floor(Math.sqrt(r.toDouble)).toInt
        if (low > high) return total

        val limit = high
        if (limit < 2) return total

        val isPrime = Array.fill(limit + 1)(true)
        isPrime(0) = false
        if (limit >= 1) isPrime(1) = false

        val sqrtLimit = Math.sqrt(limit).toInt
        var i = 2
        while (i <= sqrtLimit) {
            if (isPrime(i)) {
                var j = i * i
                while (j <= limit) {
                    isPrime(j) = false
                    j += i
                }
            }
            i += 1
        }

        var cnt = 0
        var p = low
        while (p <= high) {
            if (p <= limit && isPrime(p)) cnt += 1
            p += 1
        }

        total - cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn non_special_count(l: i32, r: i32) -> i32 {
        let l64 = l as i64;
        let r64 = r as i64;

        // maximum possible prime whose square may be <= r
        let max_p = (r as f64).sqrt() as usize;
        if max_p < 2 {
            return r - l + 1; // no prime squares exist in this range
        }

        // Sieve of Eratosthenes up to max_p
        let mut is_prime = vec![true; max_p + 1];
        is_prime[0] = false;
        if max_p >= 1 {
            is_prime[1] = false;
        }
        let limit = (max_p as f64).sqrt() as usize;
        for i in 2..=limit {
            if is_prime[i] {
                let mut j = i * i;
                while j <= max_p {
                    is_prime[j] = false;
                    j += i;
                }
            }
        }

        // Count prime squares within [l, r]
        let mut special_cnt: i32 = 0;
        for p in 2..=max_p {
            if is_prime[p] {
                let sq = (p as i64) * (p as i64);
                if sq >= l64 && sq <= r64 {
                    special_cnt += 1;
                }
            }
        }

        let total = r - l + 1;
        total - special_cnt
    }
}
```

## Racket

```racket
(require racket/math)

(define/contract (non-special-count l r)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ([total (+ (- r l) 1)]
         [low-sqrt (integer-sqrt l)]
         [low (if (= (* low-sqrt low-sqrt) l) low-sqrt (+ low-sqrt 1))]
         [high (integer-sqrt r)])
    (if (> low high)
        total
        (let* ([limit high]
               [is-prime (make-vector (+ limit 1) #t)])
          (when (>= limit 0) (vector-set! is-prime 0 #f))
          (when (>= limit 1) (vector-set! is-prime 1 #f))
          (let ([sqrt-limit (integer-sqrt limit)])
            (for ([i (in-range 2 (add1 sqrt-limit))])
              (when (vector-ref is-prime i)
                (for ([j (in-range (* i i) (add1 limit) i)])
                  (vector-set! is-prime j #f)))))
          (let loop ([p low] [cnt 0])
            (if (> p high)
                (- total cnt)
                (loop (+ p 1) (if (vector-ref is-prime p) (+ cnt 1) cnt))))))))
```

## Erlang

```erlang
-module(solution).
-export([non_special_count/2]).

-spec non_special_count(L :: integer(), R :: integer()) -> integer().
non_special_count(L, R) ->
    Total = R - L + 1,
    LowRoot = ceil_sqrt(L),
    HighRoot = floor_sqrt(R),
    PrimeCount =
        if
            LowRoot > HighRoot -> 0;
            true ->
                SmallLimit = trunc(math:sqrt(HighRoot)) + 1,
                SmallPrimes = sieve_small(SmallLimit),
                count_primes_in_range(max(LowRoot, 2), HighRoot, SmallPrimes)
        end,
    Total - PrimeCount.

%% ceil(sqrt(N))
ceil_sqrt(N) ->
    S = trunc(math:sqrt(N)),
    if
        S * S < N -> S + 1;
        true -> S
    end.

%% floor(sqrt(N))
floor_sqrt(N) ->
    trunc(math:sqrt(N)).

%% simple sieve for numbers up to Limit (Limit is small, <= ~180)
sieve_small(Limit) when Limit < 2 -> [];
sieve_small(Limit) ->
    Numbers = lists:seq(2, Limit),
    sieve(Numbers).

sieve([]) -> [];
sieve([H|T]) ->
    [H | sieve([X || X <- T, X rem H =/= 0])].

%% count primes in [Low, High] using trial division with SmallPrimes
count_primes_in_range(Low, High, SmallPrimes) ->
    count_primes_in_range(Low, High, SmallPrimes, 0).

count_primes_in_range(Current, High, _SmallPrimes, Acc) when Current > High ->
    Acc;
count_primes_in_range(Current, High, SmallPrimes, Acc) ->
    NewAcc = if is_prime(Current, SmallPrimes) -> Acc + 1; true -> Acc end,
    count_primes_in_range(Current + 1, High, SmallPrimes, NewAcc).

%% primality test using list of small primes
is_prime(N, Primes) when N < 2 -> false;
is_prime(N, []) -> true;
is_prime(N, [P|Rest]) when P * P > N -> true;
is_prime(N, [P|Rest]) ->
    case N rem P of
        0 -> false;
        _ -> is_prime(N, Rest)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec non_special_count(l :: integer, r :: integer) :: integer
  def non_special_count(l, r) do
    total = r - l + 1

    low = ceil_sqrt(l)
    high = floor_sqrt(r)

    if low > high do
      total
    else
      prime_cnt =
        Enum.reduce(low..high, 0, fn p, acc ->
          if is_prime?(p), do: acc + 1, else: acc
        end)

      total - prime_cnt
    end
  end

  defp floor_sqrt(x) do
    :math.sqrt(x) |> trunc()
  end

  defp ceil_sqrt(x) do
    s = :math.sqrt(x)
    f = trunc(s)
    if s == f, do: f, else: f + 1
  end

  defp is_prime?(n) when n < 2, do: false
  defp is_prime?(2), do: true
  defp is_prime?(n) when rem(n, 2) == 0, do: false
  defp is_prime?(n) do
    limit = :math.sqrt(n) |> trunc()
    Enum.reduce_while(3..limit, true, fn i, _ ->
      if rem(n, i) == 0, do: {:halt, false}, else: {:cont, true}
    end)
  end
end
```

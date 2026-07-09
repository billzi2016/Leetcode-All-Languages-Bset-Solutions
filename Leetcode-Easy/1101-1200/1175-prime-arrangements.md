# 1175. Prime Arrangements

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    int numPrimeArrangements(int n) {
        vector<bool> isPrime(n + 1, true);
        if (n >= 0) isPrime[0] = false;
        if (n >= 1) isPrime[1] = false;
        for (int i = 2; i * i <= n; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i)
                    isPrime[j] = false;
            }
        }
        int primeCount = 0;
        for (int i = 2; i <= n; ++i)
            if (isPrime[i]) ++primeCount;
        long long ans = 1;
        for (int i = 2; i <= primeCount; ++i) {
            ans = ans * i % MOD;
        }
        for (int i = 2; i <= n - primeCount; ++i) {
            ans = ans * i % MOD;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    
    public int numPrimeArrangements(int n) {
        int primeCount = countPrimes(n);
        long ans = factorial(primeCount);
        ans = (ans * factorial(n - primeCount)) % MOD;
        return (int) ans;
    }
    
    private int countPrimes(int n) {
        if (n < 2) return 0;
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) isPrime[i] = true;
        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int multiple = p * p; multiple <= n; multiple += p) {
                    isPrime[multiple] = false;
                }
            }
        }
        int cnt = 0;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) cnt++;
        }
        return cnt;
    }
    
    private long factorial(int k) {
        long res = 1L;
        for (int i = 2; i <= k; i++) {
            res = (res * i) % MOD;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if n < 2:
            return 1
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        p = sum(is_prime)
        def fact(k):
            res = 1
            for i in range(2, k + 1):
                res = (res * i) % MOD
            return res
        return (fact(p) * fact(n - p)) % MOD
```

## Python3

```python
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        # Sieve to count primes up to n
        is_prime = [True] * (n + 1)
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False
        i = 2
        while i * i <= n:
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
            i += 1
        prime_cnt = sum(is_prime)

        # Compute factorials modulo MOD
        ans = 1
        for i in range(2, prime_cnt + 1):
            ans = (ans * i) % MOD
        for i in range(2, n - prime_cnt + 1):
            ans = (ans * i) % MOD
        return ans
```

## C

```c
#include <stdbool.h>

int numPrimeArrangements(int n) {
    const int MOD = 1000000007;
    bool isPrime[101];
    for (int i = 0; i <= n; ++i) isPrime[i] = true;
    if (n >= 0) isPrime[0] = false;
    if (n >= 1) isPrime[1] = false;
    for (int i = 2; i * i <= n; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i)
                isPrime[j] = false;
        }
    }
    int p = 0;
    for (int i = 2; i <= n; ++i)
        if (isPrime[i]) ++p;
    long long ans = 1;
    for (int i = 2; i <= p; ++i) ans = ans * i % MOD;
    for (int i = 2; i <= n - p; ++i) ans = ans * i % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    private const long MOD = 1000000007L;
    
    public int NumPrimeArrangements(int n) {
        int primeCount = CountPrimes(n);
        long result = Factorial(primeCount);
        result = (result * Factorial(n - primeCount)) % MOD;
        return (int)result;
    }
    
    private int CountPrimes(int n) {
        if (n < 2) return 0;
        bool[] isPrime = new bool[n + 1];
        for (int i = 2; i <= n; i++) isPrime[i] = true;
        for (int p = 2; p * p <= n; p++) {
            if (!isPrime[p]) continue;
            for (int multiple = p * p; multiple <= n; multiple += p) {
                isPrime[multiple] = false;
            }
        }
        int count = 0;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) count++;
        }
        return count;
    }
    
    private long Factorial(int k) {
        long res = 1L;
        for (int i = 2; i <= k; i++) {
            res = (res * i) % MOD;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numPrimeArrangements = function(n) {
    const MOD = 1000000007n;
    
    // Count primes up to n (1-indexed)
    let primeCount = 0;
    for (let i = 2; i <= n; ++i) {
        let isPrime = true;
        for (let d = 2; d * d <= i; ++d) {
            if (i % d === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) primeCount++;
    }
    
    const factorialMod = (k) => {
        let res = 1n;
        for (let i = 2; i <= k; ++i) {
            res = (res * BigInt(i)) % MOD;
        }
        return res;
    };
    
    const ans = (factorialMod(primeCount) * factorialMod(n - primeCount)) % MOD;
    return Number(ans);
};
```

## Typescript

```typescript
function numPrimeArrangements(n: number): number {
    const MOD = 1000000007n;

    let primeCount = 0;
    for (let i = 2; i <= n; i++) {
        let isPrime = true;
        for (let j = 2; j * j <= i; j++) {
            if (i % j === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) primeCount++;
    }

    const factorial = (k: number): bigint => {
        let res = 1n;
        for (let i = 2; i <= k; i++) {
            res = (res * BigInt(i)) % MOD;
        }
        return res;
    };

    const result = (factorial(primeCount) * factorial(n - primeCount)) % MOD;
    return Number(result);
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;

    /**
     * @param Integer $n
     * @return Integer
     */
    function numPrimeArrangements($n) {
        $primeCount = 0;
        for ($i = 2; $i <= $n; $i++) {
            if ($this->isPrime($i)) {
                $primeCount++;
            }
        }

        $res = 1;
        for ($i = 2; $i <= $primeCount; $i++) {
            $res = ($res * $i) % self::MOD;
        }
        for ($i = 2; $i <= $n - $primeCount; $i++) {
            $res = ($res * $i) % self::MOD;
        }

        return $res;
    }

    private function isPrime($x) {
        if ($x < 2) return false;
        for ($i = 2; $i * $i <= $x; $i++) {
            if ($x % $i == 0) return false;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func numPrimeArrangements(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        if n < 2 { return 1 }
        var isPrime = [Bool](repeating: true, count: n + 1)
        isPrime[0] = false
        isPrime[1] = false
        var i = 2
        while i * i <= n {
            if isPrime[i] {
                var j = i * i
                while j <= n {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        var primeCount = 0
        for k in 2...n {
            if isPrime[k] { primeCount += 1 }
        }
        func factorial(_ x: Int) -> Int64 {
            var result: Int64 = 1
            var v = 1
            while v <= x {
                result = (result * Int64(v)) % Int64(MOD)
                v += 1
            }
            return result
        }
        let part1 = factorial(primeCount)
        let part2 = factorial(n - primeCount)
        let ans = (part1 * part2) % Int64(MOD)
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numPrimeArrangements(n: Int): Int {
        val MOD = 1_000_000_007L

        fun isPrime(x: Int): Boolean {
            if (x < 2) return false
            var i = 2
            while (i * i <= x) {
                if (x % i == 0) return false
                i++
            }
            return true
        }

        var primeCount = 0
        for (i in 1..n) {
            if (isPrime(i)) primeCount++
        }

        fun fact(k: Int): Long {
            var res = 1L
            for (i in 2..k) {
                res = (res * i) % MOD
            }
            return res
        }

        val result = (fact(primeCount) * fact(n - primeCount)) % MOD
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numPrimeArrangements(int n) {
    int primeCount = 0;
    for (int i = 2; i <= n; ++i) {
      bool isPrime = true;
      for (int j = 2; j * j <= i; ++j) {
        if (i % j == 0) {
          isPrime = false;
          break;
        }
      }
      if (isPrime) primeCount++;
    }

    int nonPrime = n - primeCount;

    int fact(int k) {
      int res = 1;
      for (int i = 2; i <= k; ++i) {
        res = (res * i) % _mod;
      }
      return res;
    }

    int ans = fact(primeCount);
    ans = (ans * fact(nonPrime)) % _mod;
    return ans;
  }
}
```

## Golang

```go
package main

import "math"

const MOD int64 = 1000000007

func numPrimeArrangements(n int) int {
	primeCount := 0
	for i := 2; i <= n; i++ {
		if isPrime(i) {
			primeCount++
		}
	}
	fact := func(k int) int64 {
		res := int64(1)
		for i := 2; i <= k; i++ {
			res = res * int64(i) % MOD
		}
		return res
	}
	ans := fact(primeCount) * fact(n-primeCount) % MOD
	return int(ans)
}

func isPrime(x int) bool {
	if x < 2 {
		return false
	}
	limit := int(math.Sqrt(float64(x)))
	for i := 2; i <= limit; i++ {
		if x%i == 0 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def num_prime_arrangements(n)
  mod = 1_000_000_007
  prime_cnt = 0

  (2..n).each do |i|
    is_prime = true
    j = 2
    while j * j <= i
      if i % j == 0
        is_prime = false
        break
      end
      j += 1
    end
    prime_cnt += 1 if is_prime
  end

  fact = ->(k) {
    res = 1
    (2..k).each { |i| res = (res * i) % mod }
    res
  }

  (fact.call(prime_cnt) * fact.call(n - prime_cnt)) % mod
end
```

## Scala

```scala
object Solution {
    def numPrimeArrangements(n: Int): Int = {
        val MOD = 1000000007L
        // Sieve of Eratosthenes to count primes up to n
        val isPrime = Array.fill[Boolean](n + 1)(true)
        if (n >= 0) isPrime(0) = false
        if (n >= 1) isPrime(1) = false
        var p = 2
        while (p * p <= n) {
            if (isPrime(p)) {
                var multiple = p * p
                while (multiple <= n) {
                    isPrime(multiple) = false
                    multiple += p
                }
            }
            p += 1
        }
        var primeCount = 0
        for (i <- 2 to n) if (isPrime(i)) primeCount += 1

        def fact(k: Int): Long = {
            var res = 1L
            var i = 2
            while (i <= k) {
                res = (res * i) % MOD
                i += 1
            }
            res
        }

        val result = (fact(primeCount) * fact(n - primeCount)) % MOD
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_prime_arrangements(n: i32) -> i32 {
        const MOD: u64 = 1_000_000_007;
        let n_usize = n as usize;

        // Sieve of Eratosthenes to count primes up to n
        let mut is_prime = vec![true; n_usize + 1];
        if n_usize >= 0 { is_prime[0] = false; }
        if n_usize >= 1 { is_prime[1] = false; }

        let limit = (n_usize as f64).sqrt() as usize;
        for i in 2..=limit {
            if is_prime[i] {
                let mut j = i * i;
                while j <= n_usize {
                    is_prime[j] = false;
                    j += i;
                }
            }
        }

        let prime_cnt = (2..=n_usize).filter(|&i| is_prime[i]).count() as u64;
        let composite_cnt = n as u64 - prime_cnt;

        // factorial modulo MOD
        let mut fact_prime = 1u64;
        for i in 2..=prime_cnt {
            fact_prime = (fact_prime * i) % MOD;
        }
        let mut fact_composite = 1u64;
        for i in 2..=composite_cnt {
            fact_composite = (fact_composite * i) % MOD;
        }

        ((fact_prime * fact_composite) % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (prime? x)
  (if (< x 2)
      #false
      (let loop ((i 2))
        (cond [(> (* i i) x) #true]
              [(zero? (modulo x i)) #false]
              [else (loop (+ i 1))]))))

(define (count-primes n)
  (let loop ((i 2) (cnt 0))
    (if (> i n)
        cnt
        (loop (+ i 1) (if (prime? i) (+ cnt 1) cnt)))))

(define (factorial-mod k)
  (let loop ((i 1) (acc 1))
    (if (> i k)
        acc
        (loop (+ i 1) (mod (* acc i) MOD)))))

(define/contract (num-prime-arrangements n)
  (-> exact-integer? exact-integer?)
  (let* ((p (count-primes n))
         (non-p (- n p))
         (ans (mod (* (factorial-mod p) (factorial-mod non-p)) MOD)))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([num_prime_arrangements/1]).
-define(MOD, 1000000007).

-spec num_prime_arrangements(N :: integer()) -> integer().
num_prime_arrangements(N) when N >= 0 ->
    PrimeCount = count_primes(N),
    NonPrimeCount = N - PrimeCount,
    (factorial_mod(PrimeCount) * factorial_mod(NonPrimeCount)) rem ?MOD.

count_primes(N) ->
    count_primes(2, N, 0).

count_primes(I, N, Acc) when I > N -> Acc;
count_primes(I, N, Acc) ->
    NewAcc = if is_prime(I) -> Acc + 1; true -> Acc end,
    count_primes(I + 1, N, NewAcc).

is_prime(Num) when Num < 2 -> false;
is_prime(2) -> true;
is_prime(N) ->
    Max = trunc(math:sqrt(N)),
    is_prime_divisible(N, 2, Max).

is_prime_divisible(_, D, Max) when D > Max -> true;
is_prime_divisible(N, D, Max) ->
    case N rem D of
        0 -> false;
        _ -> is_prime_divisible(N, D + 1, Max)
    end.

factorial_mod(0) -> 1;
factorial_mod(K) -> factorial_mod(K, 1).

factorial_mod(0, Acc) -> Acc;
factorial_mod(N, Acc) ->
    NewAcc = (Acc * N) rem ?MOD,
    factorial_mod(N - 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_prime_arrangements(n :: integer) :: integer
  def num_prime_arrangements(n) do
    mod = 1_000_000_007
    p = count_primes(n)
    res = fact(p, mod)
    rem(res * fact(n - p, mod), mod)
  end

  defp count_primes(limit) do
    1..limit |> Enum.count(&prime?/1)
  end

  defp prime?(x) when x < 2, do: false
  defp prime?(x) do
    max = :math.sqrt(x) |> trunc()
    2..max |> Enum.all?(fn d -> rem(x, d) != 0 end)
  end

  defp fact(0, _mod), do: 1
  defp fact(k, mod) do
    Enum.reduce(1..k, 1, fn i, acc -> rem(acc * i, mod) end)
  end
end
```

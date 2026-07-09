# 3179. Find the N-th Value After K Seconds

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    
    long long modPow(long long a, long long e) {
        long long res = 1;
        while (e) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
    
    int valueAfterKSeconds(int n, int k) {
        int N = n + k - 1;          // total items for combination
        int R = k;                  // choose k (or n-1)
        int maxN = N;
        static std::vector<long long> fact, invFact;
        if ((int)fact.size() <= maxN) {
            int oldSize = fact.size();
            fact.resize(maxN + 1);
            invFact.resize(maxN + 1);
            if (oldSize == 0) {
                fact[0] = 1;
                oldSize = 1;
            }
            for (int i = oldSize; i <= maxN; ++i)
                fact[i] = fact[i - 1] * i % MOD;
            invFact[maxN] = modPow(fact[maxN], MOD - 2);
            for (int i = maxN; i > 0; --i)
                invFact[i - 1] = invFact[i] * i % MOD;
        }
        long long ans = fact[N];
        ans = ans * invFact[R] % MOD;
        ans = ans * invFact[N - R] % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int valueAfterKSeconds(int n, int k) {
        int max = n + k; // need up to (n-1)+k
        long[] fact = new long[max + 1];
        long[] invFact = new long[max + 1];
        fact[0] = 1;
        for (int i = 1; i <= max; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[max] = modPow(fact[max], MOD - 2);
        for (int i = max; i > 0; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
        int total = n - 1 + k;
        long res = fact[total];
        res = res * invFact[k] % MOD;
        res = res * invFact[n - 1] % MOD;
        return (int) res;
    }

    private long modPow(long base, long exp) {
        long result = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def valueAfterKSeconds(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = n + k - 1  # total for binomial coefficient C(m, k)
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (m + 1)
        inv_fact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        return fact[m] * inv_fact[k] % MOD * inv_fact[n - 1] % MOD
```

## Python3

```python
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        total = n - 1 + k
        fact = [1] * (total + 1)
        for i in range(1, total + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (total + 1)
        inv_fact[total] = pow(fact[total], MOD - 2, MOD)
        for i in range(total - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        return fact[total] * inv_fact[k] % MOD * inv_fact[n - 1] % MOD
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

long long modpow(long long a, long long e) {
    long long r = 1 % MOD;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

int valueAfterKSeconds(int n, int k) {
    int N = n + k;                     // maximum needed factorial index
    vector<long long> fact(N + 1), invFact(N + 1);
    fact[0] = 1;
    for (int i = 1; i <= N; ++i) fact[i] = fact[i - 1] * i % MOD;
    invFact[N] = modpow(fact[N], MOD - 2);
    for (int i = N; i >= 1; --i) invFact[i - 1] = invFact[i] * i % MOD;

    long long ans = fact[n - 1 + k];
    ans = ans * invFact[k] % MOD;
    ans = ans * invFact[n - 1] % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int ValueAfterKSeconds(int n, int k) {
        int max = n - 1 + k;
        long[] fact = new long[max + 1];
        long[] invFact = new long[max + 1];
        fact[0] = 1;
        for (int i = 1; i <= max; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[max] = ModPow(fact[max], MOD - 2);
        for (int i = max; i >= 1; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
        long res = fact[n - 1 + k];
        res = res * invFact[k] % MOD;
        res = res * invFact[n - 1] % MOD;
        return (int)res;
    }

    private long ModPow(long a, long e) {
        long result = 1;
        long baseVal = a % MOD;
        while (e > 0) {
            if ((e & 1) == 1) result = result * baseVal % MOD;
            baseVal = baseVal * baseVal % MOD;
            e >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var valueAfterKSeconds = function(n, k) {
    const MOD = 1000000007n;
    const max = n + k; // need up to (n-1)+k but allocate a bit more
    const fact = new Array(max + 1);
    const invFact = new Array(max + 1);
    fact[0] = 1n;
    for (let i = 1; i <= max; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    const modPow = (base, exp) => {
        let res = 1n;
        base %= MOD;
        while (exp > 0n) {
            if (exp & 1n) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return res;
    };
    invFact[max] = modPow(fact[max], MOD - 2n);
    for (let i = max; i > 0; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const total = n - 1 + k;
    let ans = fact[total];
    ans = (ans * invFact[k]) % MOD;
    ans = (ans * invFact[n - 1]) % MOD;
    return Number(ans);
};
```

## Typescript

```typescript
function valueAfterKSeconds(n: number, k: number): number {
    const MOD = 1000000007n;
    const N = n + k; // maximum needed factorial index
    const fact: bigint[] = new Array(N + 1);
    const invFact: bigint[] = new Array(N + 1);
    fact[0] = 1n;
    for (let i = 1; i <= N; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    function modPow(base: bigint, exp: bigint): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }
    invFact[N] = modPow(fact[N], MOD - 2n);
    for (let i = N; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const total = n - 1 + k;
    const r = k;
    let ans = fact[total];
    ans = (ans * invFact[r]) % MOD;
    ans = (ans * invFact[total - r]) % MOD;
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function valueAfterKSeconds($n, $k) {
        $MOD = 1000000007;
        $max = $n + $k; // enough for factorials up to n+k-1
        $fact = array_fill(0, $max + 1, 1);
        for ($i = 1; $i <= $max; $i++) {
            $fact[$i] = ($fact[$i - 1] * $i) % $MOD;
        }
        // modular exponentiation
        $modPow = function($base, $exp) use ($MOD) {
            $result = 1;
            $base %= $MOD;
            while ($exp > 0) {
                if ($exp & 1) {
                    $result = ($result * $base) % $MOD;
                }
                $base = ($base * $base) % $MOD;
                $exp >>= 1;
            }
            return $result;
        };
        $invFact = array_fill(0, $max + 1, 1);
        $invFact[$max] = $modPow($fact[$max], $MOD - 2);
        for ($i = $max; $i >= 1; $i--) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % $MOD;
        }
        // C((n-1)+k, k)
        $total = $n + $k - 1;
        $res = $fact[$total];
        $res = ($res * $invFact[$k]) % $MOD;
        $res = ($res * $invFact[$n - 1]) % $MOD;
        return (int)$res;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    private func modPow(_ base: Int, _ exp: Int) -> Int {
        var result = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if e & 1 == 1 {
                result = Int((Int64(result) * Int64(b)) % Int64(MOD))
            }
            b = Int((Int64(b) * Int64(b)) % Int64(MOD))
            e >>= 1
        }
        return result
    }

    func valueAfterKSeconds(_ n: Int, _ k: Int) -> Int {
        let total = n - 1 + k
        var fact = [Int](repeating: 0, count: total + 1)
        var invFact = [Int](repeating: 0, count: total + 1)

        fact[0] = 1
        if total > 0 {
            for i in 1...total {
                fact[i] = Int((Int64(fact[i - 1]) * Int64(i)) % Int64(MOD))
            }
        }

        invFact[total] = modPow(fact[total], MOD - 2)
        if total > 0 {
            for i in stride(from: total, to: 0, by: -1) {
                invFact[i - 1] = Int((Int64(invFact[i]) * Int64(i)) % Int64(MOD))
            }
        }

        var ans = fact[total]
        ans = Int((Int64(ans) * Int64(invFact[n - 1])) % Int64(MOD))
        ans = Int((Int64(ans) * Int64(invFact[k])) % Int64(MOD))
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    fun valueAfterKSeconds(n: Int, k: Int): Int {
        val max = n + k
        val fact = LongArray(max + 1)
        val invFact = LongArray(max + 1)
        fact[0] = 1L
        for (i in 1..max) {
            fact[i] = fact[i - 1] * i % MOD
        }
        invFact[max] = modPow(fact[max], MOD - 2)
        for (i in max downTo 1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }
        val res = fact[n + k - 1] * invFact[k] % MOD * invFact[n - 1] % MOD
        return res.toInt()
    }

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var result = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) result = result * b % MOD
            b = b * b % MOD
            e = e shr 1
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int valueAfterKSeconds(int n, int k) {
    int max = n + k; // need up to (n-1)+k
    List<int> fact = List.filled(max + 1, 1);
    for (int i = 1; i <= max; ++i) {
      fact[i] = (fact[i - 1] * i) % _mod;
    }
    List<int> invFact = List.filled(max + 1, 1);
    invFact[max] = _modPow(fact[max], _mod - 2);
    for (int i = max; i >= 1; --i) {
      invFact[i - 1] = (invFact[i] * i) % _mod;
    }
    int res = fact[n - 1 + k];
    res = (res * invFact[k]) % _mod;
    res = (res * invFact[n - 1]) % _mod;
    return res;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
const MOD int64 = 1000000007

func modPow(a, e int64) int64 {
	res := int64(1)
	a %= MOD
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD
		}
		a = a * a % MOD
		e >>= 1
	}
	return res
}

func valueAfterKSeconds(n int, k int) int {
	total := n - 1 + k
	fact := make([]int64, total+1)
	invFact := make([]int64, total+1)

	fact[0] = 1
	for i := 1; i <= total; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[total] = modPow(fact[total], MOD-2)
	for i := total; i >= 1; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}

	res := fact[total]
	res = res * invFact[k] % MOD
	res = res * invFact[n-1] % MOD

	return int(res)
}
```

## Ruby

```ruby
def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = result * b % mod if (e & 1) == 1
    b = b * b % mod
    e >>= 1
  end
  result
end

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def value_after_k_seconds(n, k)
  mod = 1_000_000_007
  max = n + k
  fact = Array.new(max + 1, 1)
  (1..max).each { |i| fact[i] = fact[i - 1] * i % mod }

  inv_fact = Array.new(max + 1, 1)
  inv_fact[max] = mod_pow(fact[max], mod - 2, mod)
  max.downto(1) do |i|
    inv_fact[i - 1] = inv_fact[i] * i % mod
  end

  res = fact[n + k - 1]
  res = res * inv_fact[k] % mod
  res = res * inv_fact[n - 1] % mod
  res
end
```

## Scala

```scala
object Solution {
    private val MOD: Long = 1000000007L

    private def modPow(base: Long, exp: Long): Long = {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e & 1L) == 1L) res = (res * b) % MOD
            b = (b * b) % MOD
            e >>= 1
        }
        res
    }

    def valueAfterKSeconds(n: Int, k: Int): Int = {
        val max = n + k // enough for factorial up to n+k-1
        val fact = new Array[Long](max + 1)
        val invFact = new Array[Long](max + 1)

        fact(0) = 1L
        var i = 1
        while (i <= max) {
            fact(i) = (fact(i - 1) * i) % MOD
            i += 1
        }

        invFact(max) = modPow(fact(max), MOD - 2)
        i = max
        while (i > 0) {
            invFact(i - 1) = (invFact(i) * i) % MOD
            i -= 1
        }

        val total = n + k - 1
        var ans = fact(total)
        ans = (ans * invFact(n - 1)) % MOD
        ans = (ans * invFact(k)) % MOD

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn value_after_k_seconds(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let k = k as usize;
        // we need factorials up to n + k - 1
        let limit = n + k;
        let mut fact = vec![1i64; limit + 1];
        for i in 1..=limit {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        fn mod_pow(mut base: i64, mut exp: i64, modu: i64) -> i64 {
            let mut res = 1i64;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = res * base % modu;
                }
                base = base * base % modu;
                exp >>= 1;
            }
            res
        }
        // C(n + k - 1, k) = fact[n+k-1] / (fact[k] * fact[n-1])
        let inv_fact_k = mod_pow(fact[k], MOD - 2, MOD);
        let inv_fact_n_1 = mod_pow(fact[n - 1], MOD - 2, MOD);
        let comb = fact[n + k - 1] * inv_fact_k % MOD * inv_fact_n_1 % MOD;
        comb as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (modpow base exp)
  (let loop ((b (remainder base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (remainder (* b b) MOD)
              (quotient e 2)
              (if (odd? e) (remainder (* res b) MOD) res)))))

(define (modinv a)
  (modpow a (- MOD 2)))

(define/contract (value-after-k-seconds n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((max (+ n k -1))
         (fact (make-vector (+ max 1) 0))
         (inv-fact (make-vector (+ max 1) 0)))
    ;; factorials
    (vector-set! fact 0 1)
    (for ([i (in-range 1 (+ max 1))])
      (vector-set! fact i (remainder (* (vector-ref fact (- i 1)) i) MOD)))
    ;; inverse factorials
    (vector-set! inv-fact max (modinv (vector-ref fact max)))
    (for ([i (in-range max 0 -1)])
      (vector-set! inv-fact i (remainder (* (vector-ref inv-fact (+ i 1)) (+ i 1)) MOD)))
    ;; binomial coefficient C(n+k-1, k)
    (let* ((numer (vector-ref fact max))
           (denom1 (vector-ref inv-fact k))
           (denom2 (vector-ref inv-fact (- max k))))
      (remainder (* numer (remainder (* denom1 denom2) MOD)) MOD))))
```

## Erlang

```erlang
-spec value_after_k_seconds(N :: integer(), K :: integer()) -> integer().
value_after_k_seconds(N, K) ->
    Mod = 1000000007,
    Total = N - 1 + K,
    R = if (N - 1) < K -> N - 1; true -> K end,
    combination(Total, R, Mod).

-spec combination(integer(), integer(), integer()) -> integer().
combination(_Total, 0, _Mod) ->
    1;
combination(Total, R, Mod) ->
    Start = Total - R + 1,
    combination_loop(1, Start, R, Mod, 1).

-spec combination_loop(integer(), integer(), integer(), integer(), integer()) -> integer().
combination_loop(I, _Start, R, _Mod, Acc) when I > R ->
    Acc;
combination_loop(I, Start, R, Mod, Acc) ->
    Num = (Acc * (Start + I - 1)) rem Mod,
    Inv = pow_mod(I, Mod - 2, Mod),
    NewAcc = (Num * Inv) rem Mod,
    combination_loop(I + 1, Start, R, Mod, NewAcc).

-spec pow_mod(integer(), integer(), integer()) -> integer().
pow_mod(Base, Exp, Mod) ->
    pow_mod_iter(Base rem Mod, Exp, Mod, 1).

-spec pow_mod_iter(integer(), integer(), integer(), integer()) -> integer().
pow_mod_iter(_Base, 0, _Mod, Acc) ->
    Acc;
pow_mod_iter(Base, Exp, Mod, Acc) when (Exp band 1) =:= 1 ->
    NewAcc = (Acc * Base) rem Mod,
    pow_mod_iter((Base * Base) rem Mod, Exp bsr 1, Mod, NewAcc);
pow_mod_iter(Base, Exp, Mod, Acc) ->
    pow_mod_iter((Base * Base) rem Mod, Exp bsr 1, Mod, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @modulus 1_000_000_007

  @spec value_after_k_seconds(n :: integer, k :: integer) :: integer
  def value_after_k_seconds(n, k) do
    limit = n + k
    {fact, inv_fact} = precompute(limit)
    comb(fact, inv_fact, n + k - 1, k)
  end

  # Pre‑compute factorials and inverse factorials up to `limit`
  defp precompute(limit) do
    fact = :array.new(limit + 1, default: 0)
    fact = :array.set(0, 1, fact)
    fact = compute_fact(1, limit, fact)

    inv_fact = :array.new(limit + 1, default: 0)
    inv_last = mod_pow(:array.get(limit, fact), @modulus - 2)
    inv_fact = :array.set(limit, inv_last, inv_fact)
    inv_fact = compute_inv(limit - 1, inv_fact)

    {fact, inv_fact}
  end

  defp compute_fact(i, limit, arr) when i > limit, do: arr
  defp compute_fact(i, limit, arr) do
    prev = :array.get(i - 1, arr)
    arr = :array.set(i, rem(prev * i, @modulus), arr)
    compute_fact(i + 1, limit, arr)
  end

  defp compute_inv(i, arr) when i < 0, do: arr
  defp compute_inv(i, arr) do
    next = :array.get(i + 1, arr)
    val = rem(next * (i + 1), @modulus)
    arr = :array.set(i, val, arr)
    compute_inv(i - 1, arr)
  end

  # nCr modulo MOD using pre‑computed factorials
  defp comb(fact, inv_fact, n, r) when r < 0 or r > n, do: 0
  defp comb(fact, inv_fact, n, r) do
    a = :array.get(n, fact)
    b = :array.get(r, inv_fact)
    c = :array.get(n - r, inv_fact)
    rem(rem(a * b, @modulus) * c, @modulus)
  end

  # Fast modular exponentiation
  defp mod_pow(base, exp), do: pow_mod(rem(base, @modulus), exp, 1)

  defp pow_mod(_base, 0, acc), do: acc
  defp pow_mod(base, exp, acc) do
    {base, exp, acc} =
      if rem(exp, 2) == 1 do
        {rem(base * base, @modulus), div(exp, 2), rem(acc * base, @modulus)}
      else
        {rem(base * base, @modulus), div(exp, 2), acc}
      end

    pow_mod(base, exp, acc)
  end
end
```

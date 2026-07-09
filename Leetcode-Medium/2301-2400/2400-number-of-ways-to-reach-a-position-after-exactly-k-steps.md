# 2400. Number of Ways to Reach a Position After Exactly k Steps

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
    
    int numberOfWays(int startPos, int endPos, int k) {
        long long d = (long long)endPos - startPos;
        if (abs(d) > k) return 0;
        if ((k + d) % 2 != 0) return 0; // parity mismatch
        
        int r = (int)((k + d) / 2); // number of right moves
        if (r < 0 || r > k) return 0;
        
        vector<long long> fact(k + 1), invFact(k + 1);
        fact[0] = 1;
        for (int i = 1; i <= k; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[k] = modPow(fact[k], MOD - 2);
        for (int i = k; i >= 1; --i) invFact[i - 1] = invFact[i] * i % MOD;
        
        long long ans = fact[k];
        ans = ans * invFact[r] % MOD;
        ans = ans * invFact[k - r] % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int numberOfWays(int startPos, int endPos, int k) {
        int d = endPos - startPos;
        if (((k + d) & 1) != 0) return 0;               // parity mismatch
        int right = (k + d) / 2;
        if (right < 0 || right > k) return 0;           // impossible counts

        long[] fact = new long[k + 1];
        long[] invFact = new long[k + 1];
        fact[0] = 1;
        for (int i = 1; i <= k; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[k] = modPow(fact[k], MOD - 2);
        for (int i = k; i >= 1; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }

        long ans = fact[k];
        ans = ans * invFact[right] % MOD;
        ans = ans * invFact[k - right] % MOD;
        return (int) ans;
    }

    private long modPow(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = res * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        diff = abs(endPos - startPos)
        if diff > k or (k - diff) % 2 != 0:
            return 0

        # number of steps in the direction that has more moves
        x = (k + diff) // 2  # choose positions for those steps

        # precompute factorials up to k
        fact = [1] * (k + 1)
        for i in range(1, k + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (k + 1)
        inv_fact[k] = pow(fact[k], MOD - 2, MOD)
        for i in range(k, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # nCk = fact[n] * inv_fact[k] * inv_fact[n-k] % MOD
        return fact[k] * inv_fact[x] % MOD * inv_fact[k - x] % MOD
```

## Python3

```python
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        d = endPos - startPos
        if abs(d) > k or (k + d) & 1:
            return 0
        r = (k + d) // 2

        fact = [1] * (k + 1)
        for i in range(1, k + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (k + 1)
        inv_fact[k] = pow(fact[k], MOD - 2, MOD)
        for i in range(k, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        return fact[k] * inv_fact[r] % MOD * inv_fact[k - r] % MOD
```

## C

```c
#include <stdlib.h>

static long long modPow(long long a, long long e) {
    const long long MOD = 1000000007LL;
    long long r = 1 % MOD;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

int numberOfWays(int startPos, int endPos, int k) {
    const long long MOD = 1000000007LL;
    int delta = endPos - startPos;

    if (abs(delta) > k) return 0;
    if ((k + delta) & 1) return 0;               // parity mismatch
    int r = (k + delta) / 2;                     // number of right moves
    if (r < 0 || r > k) return 0;

    long long fact[1001];
    long long invFact[1001];
    fact[0] = 1;
    for (int i = 1; i <= k; ++i) fact[i] = fact[i - 1] * i % MOD;

    invFact[k] = modPow(fact[k], MOD - 2);
    for (int i = k; i >= 1; --i) invFact[i - 1] = invFact[i] * i % MOD;

    long long ans = fact[k];
    ans = ans * invFact[r] % MOD;
    ans = ans * invFact[k - r] % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    private const long MOD = 1000000007L;

    public int NumberOfWays(int startPos, int endPos, int k)
    {
        long diff = (long)endPos - startPos;
        long sum = k + diff;
        if ((sum & 1L) != 0L) return 0; // parity mismatch
        long right = sum / 2;
        if (right < 0 || right > k) return 0;

        int n = k;
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++)
            fact[i] = fact[i - 1] * i % MOD;

        invFact[n] = ModPow(fact[n], MOD - 2);
        for (int i = n - 1; i >= 0; i--)
            invFact[i] = invFact[i + 1] * (i + 1) % MOD;

        long res = fact[n];
        res = res * invFact[(int)right] % MOD;
        res = res * invFact[n - (int)right] % MOD;
        return (int)res;
    }

    private static long ModPow(long baseVal, long exp)
    {
        long result = 1;
        long b = baseVal % MOD;
        while (exp > 0)
        {
            if ((exp & 1L) == 1L)
                result = result * b % MOD;
            b = b * b % MOD;
            exp >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} startPos
 * @param {number} endPos
 * @param {number} k
 * @return {number}
 */
var numberOfWays = function(startPos, endPos, k) {
    const MOD = 1000000007n;
    const delta = endPos - startPos;
    if (Math.abs(delta) > k) return 0;
    if ((k + delta) % 2 !== 0) return 0;
    const r = (k + delta) / 2; // number of right moves, integer guaranteed

    // factorials modulo MOD
    const fact = new Array(k + 1);
    fact[0] = 1n;
    for (let i = 1; i <= k; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    // fast exponentiation
    const modPow = (base, exp) => {
        let result = 1n;
        let b = base % MOD;
        let e = BigInt(exp);
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    };

    // inverse factorials
    const invFact = new Array(k + 1);
    invFact[k] = modPow(fact[k], MOD - 2n);
    for (let i = k; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    let ans = fact[k];
    ans = (ans * invFact[r]) % MOD;
    ans = (ans * invFact[k - r]) % MOD;

    return Number(ans);
};
```

## Typescript

```typescript
function numberOfWays(startPos: number, endPos: number, k: number): number {
    const MOD = 1000000007n;
    const diff = endPos - startPos;
    const d = Math.abs(diff);
    if (k < d) return 0;
    if ((k - d) % 2 !== 0) return 0;

    const r = (k + diff) / 2;
    if (r < 0 || r > k) return 0;
    const ri = Math.floor(r);

    function modPow(base: bigint, exp: bigint): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }

    const n = k;
    const fact: bigint[] = new Array(n + 1);
    const invFact: bigint[] = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i >= 1; i--) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    const res = (((fact[n] * invFact[ri]) % MOD) * invFact[n - ri]) % MOD;
    return Number(res);
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;
    private $fact = [];
    private $invFact = [];

    private function modPow(int $base, int $exp): int {
        $mod = self::MOD;
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = (int)(($result * $base) % $mod);
            }
            $base = (int)(($base * $base) % $mod);
            $exp >>= 1;
        }
        return $result;
    }

    private function prepare(int $n): void {
        if (!empty($this->fact) && count($this->fact) - 1 >= $n) {
            return; // already prepared up to at least n
        }
        $mod = self::MOD;
        $this->fact[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $this->fact[$i] = (int)(($this->fact[$i - 1] * $i) % $mod);
        }
        $this->invFact[$n] = $this->modPow($this->fact[$n], $mod - 2);
        for ($i = $n; $i > 0; $i--) {
            $this->invFact[$i - 1] = (int)(($this->invFact[$i] * $i) % $mod);
        }
    }

    /**
     * @param Integer $startPos
     * @param Integer $endPos
     * @param Integer $k
     * @return Integer
     */
    function numberOfWays($startPos, $endPos, $k) {
        $d = $endPos - $startPos;
        if (abs($d) > $k) return 0;
        if ((($k + $d) & 1) != 0) return 0; // parity mismatch
        $r = intdiv($k + $d, 2);
        if ($r < 0 || $r > $k) return 0;

        $this->prepare($k);

        $mod = self::MOD;
        $res = $this->fact[$k];
        $res = (int)(($res * $this->invFact[$r]) % $mod);
        $res = (int)(($res * $this->invFact[$k - $r]) % $mod);
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    private func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
        var result: Int64 = 1
        var b = base % Int64(MOD)
        var e = exp
        while e > 0 {
            if (e & 1) == 1 {
                result = (result * b) % Int64(MOD)
            }
            b = (b * b) % Int64(MOD)
            e >>= 1
        }
        return result
    }

    func numberOfWays(_ startPos: Int, _ endPos: Int, _ k: Int) -> Int {
        let distance = abs(endPos - startPos)
        if distance > k { return 0 }
        if (k - distance) % 2 != 0 { return 0 }

        let rightMoves = (k + distance) / 2

        var fact = [Int64](repeating: 1, count: k + 1)
        for i in 1...k {
            fact[i] = (fact[i - 1] * Int64(i)) % Int64(MOD)
        }

        let invFactRight = modPow(fact[rightMoves], Int64(MOD - 2))
        let invFactLeft = modPow(fact[k - rightMoves], Int64(MOD - 2))

        var ans = fact[k]
        ans = (ans * invFactRight) % Int64(MOD)
        ans = (ans * invFactLeft) % Int64(MOD)

        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    fun numberOfWays(startPos: Int, endPos: Int, k: Int): Int {
        val d = endPos - startPos
        val sum = k + d
        if (sum < 0 || sum % 2 != 0) return 0
        val r = sum / 2
        if (r < 0 || r > k) return 0

        val n = k
        val fact = LongArray(n + 1)
        val invFact = LongArray(n + 1)

        fact[0] = 1L
        for (i in 1..n) {
            fact[i] = fact[i - 1] * i % MOD
        }

        invFact[n] = modPow(fact[n], MOD - 2)
        for (i in n downTo 1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }

        val ans = fact[n] * invFact[r] % MOD * invFact[n - r] % MOD
        return ans.toInt()
    }

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) {
                res = res * b % MOD
            }
            b = b * b % MOD
            e = e shr 1
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numberOfWays(int startPos, int endPos, int k) {
    int d = endPos - startPos;
    // r = (k + d) / 2 must be integer and between 0 and k
    if ((k + d) % 2 != 0) return 0;
    int r = (k + d) ~/ 2;
    if (r < 0 || r > k) return 0;

    // precompute factorials up to k
    List<int> fact = List.filled(k + 1, 1);
    for (int i = 1; i <= k; ++i) {
      fact[i] = (fact[i - 1] * i) % _mod;
    }

    int invFactR = _modPow(fact[r], _mod - 2);
    int invFactKMinusR = _modPow(fact[k - r], _mod - 2);

    int res = fact[k];
    res = ((res * invFactR) % _mod * invFactKMinusR) % _mod;
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

func modPow(a int64, e int64) int64 {
	var res int64 = 1
	base := a % MOD
	for e > 0 {
		if e&1 == 1 {
			res = res * base % MOD
		}
		base = base * base % MOD
		e >>= 1
	}
	return res
}

func numberOfWays(startPos int, endPos int, k int) int {
	diff := endPos - startPos
	if (k+diff)%2 != 0 {
		return 0
	}
	R := (k + diff) / 2
	if R < 0 || R > k {
		return 0
	}

	fact := make([]int64, k+1)
	invFact := make([]int64, k+1)
	fact[0] = 1
	for i := 1; i <= k; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[k] = modPow(fact[k], MOD-2)
	for i := k; i >= 1; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}

	res := fact[k] * invFact[R] % MOD * invFact[k-R] % MOD
	return int(res)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e, mod)
  result = 1
  a %= mod
  while e > 0
    result = result * a % mod if (e & 1) == 1
    a = a * a % mod
    e >>= 1
  end
  result
end

def number_of_ways(start_pos, end_pos, k)
  d = end_pos - start_pos
  return 0 if ((k + d) & 1) == 1 || d.abs > k
  r = (k + d) / 2
  return 0 if r < 0 || r > k

  fact = Array.new(k + 1, 1)
  (1..k).each { |i| fact[i] = fact[i - 1] * i % MOD }

  inv_fact = Array.new(k + 1, 1)
  inv_fact[k] = mod_pow(fact[k], MOD - 2, MOD)
  (k - 1).downto(0) { |i| inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD }

  ans = fact[k] * inv_fact[r] % MOD
  ans = ans * inv_fact[k - r] % MOD
  ans
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L

    def numberOfWays(startPos: Int, endPos: Int, k: Int): Int = {
        val diff = endPos - startPos
        if (((k + diff) & 1) != 0) return 0
        val rLong = (k + diff) / 2
        if (rLong < 0 || rLong > k) return 0
        val r = rLong.toInt

        val fact = new Array[Long](k + 1)
        fact(0) = 1L
        var i = 1
        while (i <= k) {
            fact(i) = fact(i - 1) * i % MOD
            i += 1
        }

        val invFact = new Array[Long](k + 1)
        invFact(k) = modPow(fact(k), MOD - 2)
        i = k
        while (i > 0) {
            invFact(i - 1) = invFact(i) * i % MOD
            i -= 1
        }

        val res = fact(k) * invFact(r) % MOD * invFact(k - r) % MOD
        res.toInt
    }

    private def modPow(base: Long, exp: Long): Long = {
        var b = base % MOD
        var e = exp
        var result = 1L
        while (e > 0) {
            if ((e & 1L) == 1L) result = result * b % MOD
            b = b * b % MOD
            e >>= 1
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_ways(start_pos: i32, end_pos: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let delta = (end_pos - start_pos) as i64;
        let k_i64 = k as i64;

        // parity check
        if ((k_i64 + delta) & 1) != 0 {
            return 0;
        }

        let r = (k_i64 + delta) / 2;
        if r < 0 || r > k_i64 {
            return 0;
        }

        let n = k as usize;
        let r_usize = r as usize;

        // factorials
        let mut fac = vec![1i64; n + 1];
        for i in 1..=n {
            fac[i] = fac[i - 1] * (i as i64) % MOD;
        }

        fn mod_pow(mut a: i64, mut e: i64, m: i64) -> i64 {
            let mut res = 1i64;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % m;
                }
                a = a * a % m;
                e >>= 1;
            }
            res
        }

        // inverse factorials
        let mut inv_fac = vec![1i64; n + 1];
        inv_fac[n] = mod_pow(fac[n], MOD - 2, MOD);
        for i in (1..=n).rev() {
            inv_fac[i - 1] = inv_fac[i] * (i as i64) % MOD;
        }

        let ans = fac[n] * inv_fac[r_usize] % MOD * inv_fac[n - r_usize] % MOD;
        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(define MOD 1000000007)

(define (modexp base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (modulo (* b b) MOD)
              (quotient e 2)
              (if (= (modulo e 2) 1)
                  (modulo (* res b) MOD)
                  res)))))

(define/contract (number-of-ways startPos endPos k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((delta (- endPos startPos))
         (abs-delta (if (< delta 0) (- delta) delta)))
    (if (or (> abs-delta k)
            (not (= (modulo (+ k delta) 2) 0)))
        0
        (let* ((r (quotient (+ k delta) 2))
               (fact (make-vector (+ k 1) 1))
               (invFact (make-vector (+ k 1) 1)))
          ;; factorials
          (for ([i (in-range 1 (+ k 1))])
            (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
          ;; inverse factorial of k
          (vector-set! invFact k (modexp (vector-ref fact k) (- MOD 2)))
          ;; compute remaining inverse factorials
          (for ([i (in-range (- k 1) -1 -1)])
            (vector-set! invFact i (modulo (* (vector-ref invFact (+ i 1)) (+ i 1)) MOD)))
          (let ((ans (modulo (* (vector-ref fact k)
                                (modulo (* (vector-ref invFact r)
                                           (vector-ref invFact (- k r))) MOD))
                              MOD)))
            ans)))) )
```

## Erlang

```erlang
-module(solution).
-export([number_of_ways/3]).

-define(MOD, 1000000007).

-spec number_of_ways(StartPos :: integer(), EndPos :: integer(), K :: integer()) -> integer().
number_of_ways(StartPos, EndPos, K) ->
    Diff = EndPos - StartPos,
    Sum = K + Diff,
    case (Sum band 1) of
        1 -> 0;
        0 ->
            R = Sum div 2,
            if R < 0 orelse R > K -> 0;
               true -> binom(K, R)
            end
    end.

-spec binom(N :: integer(), R :: integer()) -> integer().
binom(N, R) when R < 0; R > N -> 0;
binom(N, R) ->
    SmallR = if R > N - R -> N - R; true -> R end,
    binom_iter(1, SmallR, N - SmallR + 1, 1).

-spec binom_iter(I :: integer(), MaxI :: integer(), Num :: integer(), Acc :: integer()) -> integer().
binom_iter(I, MaxI, Num, Acc) when I =< MaxI ->
    InvI = mod_pow(I, ?MOD-2, ?MOD),
    NewAcc = (Acc * (Num rem ?MOD)) rem ?MOD,
    NewAcc2 = (NewAcc * InvI) rem ?MOD,
    binom_iter(I + 1, MaxI, Num + 1, NewAcc2);
binom_iter(_, _, _, Acc) -> Acc.

-spec mod_pow(Base :: integer(), Exp :: integer(), Mod :: integer()) -> integer().
mod_pow(_Base, 0, _Mod) -> 1;
mod_pow(Base, Exp, Mod) when (Exp band 1) =:= 1 ->
    ((Base rem Mod) * mod_pow((Base * Base) rem Mod, Exp div 2, Mod)) rem Mod;
mod_pow(Base, Exp, Mod) ->
    mod_pow((Base * Base) rem Mod, Exp div 2, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @modulus 1_000_000_007

  @spec number_of_ways(start_pos :: integer, end_pos :: integer, k :: integer) :: integer
  def number_of_ways(start_pos, end_pos, k) do
    delta = end_pos - start_pos

    if (k + delta) < 0 or rem(k + delta, 2) != 0 do
      0
    else
      r = div(k + delta, 2)

      if r < 0 or r > k do
        0
      else
        fact = :array.new(k + 1, default: 0)
        fact = :array.set(0, 1, fact)

        fact =
          Enum.reduce(1..k, fact, fn i, arr ->
            prev = :array.get(i - 1, arr)
            :array.set(i, rem(prev * i, @modulus), arr)
          end)

        inv_r = mod_pow(:array.get(r, fact), @modulus - 2)
        inv_nr = mod_pow(:array.get(k - r, fact), @modulus - 2)

        ((:array.get(k, fact) * inv_r) |> rem(@modulus) *
           inv_nr) |> rem(@modulus)
      end
    end
  end

  defp mod_pow(_base, 0), do: 1

  defp mod_pow(base, exp) when exp > 0 do
    base = rem(base, @modulus)
    do_mod_pow(base, exp, 1)
  end

  defp do_mod_pow(_, 0, acc), do: acc

  defp do_mod_pow(b, e, acc) when rem(e, 2) == 1 do
    do_mod_pow(rem(b * b, @modulus), div(e, 2), rem(acc * b, @modulus))
  end

  defp do_mod_pow(b, e, acc) do
    do_mod_pow(rem(b * b, @modulus), div(e, 2), acc)
  end
end
```

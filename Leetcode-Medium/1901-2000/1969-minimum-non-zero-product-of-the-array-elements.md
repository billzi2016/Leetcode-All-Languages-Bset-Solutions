# 1969. Minimum Non-Zero Product of the Array Elements

## Cpp

```cpp
class Solution {
public:
    static const long long MOD = 1000000007LL;
    
    long long modPow(long long base, unsigned long long exp) {
        long long result = 1 % MOD;
        base %= MOD;
        while (exp) {
            if (exp & 1ULL) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1ULL;
        }
        return result;
    }
    
    int minNonZeroProduct(int p) {
        // a = 2^p - 1, b = a - 1 = 2^p - 2
        long long pow2_mod = modPow(2, (unsigned long long)p);
        long long a = (pow2_mod - 1 + MOD) % MOD;
        long long b = (a - 1 + MOD) % MOD;
        
        unsigned long long exp = 1ULL << (p - 1); // 2^{p-1}
        long long part1 = modPow(a, exp);
        long long part2 = modPow(b, exp - 1);
        long long ans = (part1 * part2) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    private static long modPow(long base, long exp, long mod) {
        long result = 1L % mod;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }

    public int minNonZeroProduct(int p) {
        long maxVal = (modPow(2L, p, MOD) - 1 + MOD) % MOD;          // 2^p - 1
        long secondMax = (maxVal - 1 + MOD) % MOD;                  // 2^p - 2
        long exp = (modPow(2L, p - 1, MOD - 1) - 1 + (MOD - 1)) % (MOD - 1); // 2^{p-1} - 1 modulo MOD-1
        long part = modPow(secondMax, exp, MOD);
        long ans = (maxVal * part) % MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # max value in the array: 2^p - 1
        max_val = (pow(2, p, MOD) - 1) % MOD
        # base for exponentiation: max_val - 1 (i.e., 2^p - 2)
        base = (max_val - 1) % MOD
        # exponent: (2^{p-1} - 1)
        exp = (1 << (p - 1)) - 1
        return (max_val * pow(base, exp, MOD)) % MOD
```

## Python3

```python
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        max_val = (pow(2, p, MOD) - 1) % MOD
        base = (pow(2, p, MOD) - 2) % MOD
        exp = (1 << (p - 1)) - 1
        return max_val * pow(base, exp, MOD) % MOD
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const long long MOD = 1000000007LL;

long long modPow(long long base, unsigned long long exp) {
    long long result = 1;
    base %= MOD;
    while (exp) {
        if (exp & 1ULL) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1ULL;
    }
    return result;
}

int minNonZeroProduct(int p) {
    long long pow2p_mod = modPow(2, static_cast<unsigned long long>(p));
    long long maxVal = (pow2p_mod - 1 + MOD) % MOD;          // 2^p - 1
    long long second = (pow2p_mod - 2 + MOD) % MOD;         // 2^p - 2
    unsigned long long exp = (1ULL << (p - 1)) - 1ULL;      // 2^{p-1} - 1
    long long part = modPow(second, exp);
    long long ans = (maxVal * part) % MOD;
    return static_cast<int>(ans);
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1_000_000_007;

    public int MinNonZeroProduct(int p)
    {
        long maxVal = (ModPow(2, p, MOD) - 1 + MOD) % MOD;          // 2^p - 1
        long second = (maxVal - 1 + MOD) % MOD;                    // 2^p - 2

        long exp = 1L << (p - 1);                                 // 2^{p-1}
        long part1 = ModPow(maxVal, exp, MOD);
        long part2 = ModPow(second, exp - 1, MOD);

        return (int)((part1 * part2) % MOD);
    }

    private long ModPow(long baseValue, long exponent, int mod)
    {
        long result = 1;
        baseValue %= mod;
        while (exponent > 0)
        {
            if ((exponent & 1) == 1)
                result = (result * baseValue) % mod;
            baseValue = (baseValue * baseValue) % mod;
            exponent >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} p
 * @return {number}
 */
var minNonZeroProduct = function(p) {
    const MOD = 1000000007n;
    const P = BigInt(p);
    
    // max value with p bits all set to 1: 2^p - 1
    const maxVal = (1n << P) - 1n;
    // base value for the repeated factor: maxVal - 1
    const base = maxVal - 1n;
    // exponent: number of times we use (maxVal-1), which is 2^{p-1} - 1
    const exp = (1n << (P - 1n)) - 1n;
    
    const modPow = (b, e, m) => {
        let res = 1n;
        while (e > 0n) {
            if (e & 1n) res = (res * b) % m;
            b = (b * b) % m;
            e >>= 1n;
        }
        return res;
    };
    
    const part = modPow(base % MOD, exp, MOD);
    const ans = (maxVal % MOD) * part % MOD;
    return Number(ans);
};
```

## Typescript

```typescript
function minNonZeroProduct(p: number): number {
    const MOD = 1000000007n;
    const bigP = BigInt(p);
    const maxVal = (1n << bigP) - 1n;               // 2^p - 1
    const base = maxVal - 1n;                       // 2^p - 2
    const exp = (1n << (bigP - 1n)) - 1n;           // 2^{p-1} - 1

    function modPow(b: bigint, e: bigint, m: bigint): bigint {
        let result = 1n;
        b %= m;
        while (e > 0) {
            if (e & 1n) result = (result * b) % m;
            b = (b * b) % m;
            e >>= 1n;
        }
        return result;
    }

    const part = modPow(base, exp, MOD);
    const ans = (maxVal % MOD) * part % MOD;
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $p
     * @return Integer
     */
    function minNonZeroProduct($p) {
        $mod = 1000000007;

        // compute (2^p) % mod
        $pow2pMod = $this->modPow(2, $p, $mod);
        $maxVal = ($pow2pMod - 1 + $mod) % $mod;          // (2^p - 1) % mod
        $base   = ($pow2pMod - 2 + $mod) % $mod;          // (2^p - 2) % mod

        // exponent = 2^{p-1} - 1, fits in 64-bit for p <= 60
        $exp = (1 << ($p - 1)) - 1;

        $part = $this->modPow($base, $exp, $mod);
        $result = ($part * $maxVal) % $mod;
        return $result;
    }

    private function modPow($a, $e, $mod) {
        $res = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) {
                $res = ($res * $a) % $mod;
            }
            $a = ($a * $a) % $mod;
            $e >>= 1;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func minNonZeroProduct(_ p: Int) -> Int {
        let MOD = 1_000_000_007
        func modPow(_ base: Int, _ exp: UInt64) -> Int {
            var result: Int64 = 1
            var b: Int64 = Int64(base % MOD)
            var e = exp
            let m = Int64(MOD)
            while e > 0 {
                if (e & 1) == 1 {
                    result = (result * b) % m
                }
                b = (b * b) % m
                e >>= 1
            }
            return Int(result)
        }
        
        // maxVal = 2^p - 1 (mod MOD)
        let twoPowPMod = modPow(2, UInt64(p))
        let maxValMod = (twoPowPMod - 1 + MOD) % MOD
        
        // exponent = 2^{p-1} - 1
        let exp: UInt64 = (UInt64(1) << (p - 1)) - 1
        
        // base = maxVal - 1 = 2^p - 2 (mod MOD)
        let baseMod = (maxValMod - 1 + MOD) % MOD
        
        let powPart = modPow(baseMod, exp)
        
        var ans = Int64(maxValMod)
        ans = (ans * Int64(powPart)) % Int64(MOD)
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    fun minNonZeroProduct(p: Int): Int {
        if (p == 1) return 1
        val maxVal = ((1L shl p) - 1) % MOD
        val secondMax = ((1L shl p) - 2) % MOD
        val exp = (1L shl (p - 1)) - 1
        val pow = modPow(secondMax, exp)
        val ans = maxVal * pow % MOD
        return ans.toInt()
    }
    private fun modPow(base: Long, exp: Long): Long {
        var result = 1L
        var b = base % MOD
        var e = exp
        while (e > 0) {
            if ((e and 1L) == 1L) {
                result = result * b % MOD
            }
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

  int minNonZeroProduct(int p) {
    int maxVal = ((1 << p) - 1) % _mod;
    int base = ((1 << p) - 2) % _mod;
    int exp = (1 << (p - 1)) - 1;
    int pow = _modPow(base, exp);
    return (maxVal * pow) % _mod;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _mod;
    int e = exp;
    while (e > 0) {
      if ((e & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      e >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
func minNonZeroProduct(p int) int {
	const MOD int64 = 1000000007
	if p == 1 {
		return 1
	}
	// Compute (2^p - 1) mod MOD
	maxValMod := int64(((uint64(1) << uint(p)) - 1) % uint64(MOD))
	// Compute (2^p - 2) mod MOD
	baseMod := int64(((uint64(1) << uint(p)) - 2) % uint64(MOD))

	// Exponent = 2^{p-1} - 1
	exp := (uint64(1) << uint(p-1)) - 1

	modPow := func(a int64, e uint64) int64 {
		res := int64(1)
		base := a % MOD
		for e > 0 {
			if e&1 == 1 {
				res = (res * base) % MOD
			}
			base = (base * base) % MOD
			e >>= 1
		}
		return res
	}

	power := modPow(baseMod, exp)
	ans := (maxValMod * power) % MOD
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e)
  res = 1
  a %= MOD
  while e > 0
    res = res * a % MOD if (e & 1) == 1
    a = a * a % MOD
    e >>= 1
  end
  res
end

# @param {Integer} p
# @return {Integer}
def min_non_zero_product(p)
  max_val = (1 << p) - 1
  base = max_val - 1
  exp = (1 << (p - 1)) - 1
  (max_val % MOD) * mod_pow(base, exp) % MOD
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L

    private def modPow(base: Long, exp: Long, mod: Long): Long = {
        var result = 1L
        var b = ((base % mod) + mod) % mod
        var e = exp
        while (e > 0) {
            if ((e & 1L) == 1L) result = (result * b) % mod
            b = (b * b) % mod
            e >>= 1
        }
        result
    }

    def minNonZeroProduct(p: Int): Int = {
        // max value = 2^p - 1
        val maxValMod = ((1L << p) - 1) % MOD
        // base = max - 1 = 2^p - 2
        val baseMod = ((1L << p) - 2) % MOD
        // exponent = 2^{p-1} - 1
        val exp = (1L << (p - 1)) - 1

        val powPart = modPow(baseMod, exp, MOD)
        val ans = (maxValMod * powPart) % MOD
        ans.toInt
    }
}
```

## Rust

```rust
use std::cmp::Ordering;

impl Solution {
    const MOD: i64 = 1_000_000_007;
    
    fn mod_pow(mut base: i64, mut exp: u128) -> i64 {
        let modulo = Self::MOD;
        let mut result: i64 = 1;
        base %= modulo;
        while exp > 0 {
            if (exp & 1) == 1 {
                result = ((result as i128 * base as i128) % modulo as i128) as i64;
            }
            base = ((base as i128 * base as i128) % modulo as i128) as i64;
            exp >>= 1;
        }
        result
    }

    pub fn min_non_zero_product(p: i32) -> i32 {
        // compute (2^p) mod MOD
        let two_pow_p_mod = Self::mod_pow(2, p as u128);
        // max element value (2^p - 1) modulo MOD
        let max_val = (two_pow_p_mod + Self::MOD - 1) % Self::MOD;
        // base for the repeated factor (2^p - 2) modulo MOD
        let base = (two_pow_p_mod + Self::MOD - 2) % Self::MOD;
        // exponent = 2^{p-1} - 1
        let exp: u128 = if p == 0 {
            0
        } else {
            (1u128 << (p as u32 - 1)) - 1
        };
        let pow_part = Self::mod_pow(base, exp);
        let ans = ((max_val as i128 * pow_part as i128) % Self::MOD as i128) as i64;
        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(define MOD 1000000007)

(define (modpow base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (let* ((res (if (odd? e) (modulo (* res b) MOD) res))
               (b   (modulo (* b b) MOD))
               (e   (arithmetic-shift e -1)))
          (loop b e res)))))

(define/contract (min-non-zero-product p)
  (-> exact-integer? exact-integer?)
  (let* ((pow2p (arithmetic-shift 1 p))
         (a (- pow2p 1))
         (b (- pow2p 2))
         (exp (- (arithmetic-shift 1 (- p 1)) 1)))
    (modulo (* (modulo a MOD) (modpow b exp)) MOD)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec min_non_zero_product(P :: integer()) -> integer().
min_non_zero_product(P) ->
    Max = (1 bsl P) - 1,
    Second = Max - 1,
    Exp = (1 bsl (P - 1)) - 1,
    Pow = mod_pow(Second rem ?MOD, Exp, ?MOD),
    (Max rem ?MOD * Pow) rem ?MOD.

mod_pow(_Base, 0, _Mod) -> 1;
mod_pow(Base, Exp, Mod) ->
    case Exp band 1 of
        1 ->
            ((Base * mod_pow((Base * Base) rem Mod, Exp bsr 1, Mod)) ) rem Mod;
        0 ->
            mod_pow((Base * Base) rem Mod, Exp bsr 1, Mod)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  require Bitwise

  @spec min_non_zero_product(p :: integer) :: integer
  def min_non_zero_product(p) do
    mod = 1_000_000_007

    max_val =
      (mod_pow(2, p, mod) - 1)
      |> rem(mod)
      |> adjust_mod(mod)

    base =
      (max_val - 1)
      |> rem(mod)
      |> adjust_mod(mod)

    exp = (1 <<< (p - 1)) - 1
    pow = mod_pow(base, exp, mod)
    rem(max_val * pow, mod)
  end

  defp adjust_mod(value, mod) when value < 0, do: value + mod
  defp adjust_mod(value, _mod), do: value

  defp mod_pow(base, exp, mod), do: mod_pow(base |> rem(mod), exp, mod, 1)

  defp mod_pow(_base, 0, _mod, acc), do: acc

  defp mod_pow(base, exp, mod, acc) do
    acc = if Bitwise.band(exp, 1) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    exp = Bitwise.bsr(exp, 1)
    mod_pow(base, exp, mod, acc)
  end
end
```

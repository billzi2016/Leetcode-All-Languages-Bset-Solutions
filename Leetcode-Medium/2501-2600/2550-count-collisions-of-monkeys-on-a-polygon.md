# 2550. Count Collisions of Monkeys on a Polygon

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    long long modpow(long long a, long long e) {
        long long res = 1;
        a %= MOD;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
    
    int monkeyMove(int n) {
        long long total = modpow(2, n);
        long long ans = (total - 2 + MOD) % MOD;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    
    public int monkeyMove(int n) {
        long total = modPow(2L, n, MOD);
        long ans = (total - 2 + MOD) % MOD;
        return (int) ans;
    }
    
    private long modPow(long base, long exp, long mod) {
        long result = 1L;
        long b = base % mod;
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                result = (result * b) % mod;
            }
            b = (b * b) % mod;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def monkeyMove(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        return (pow(2, n, MOD) - 2) % MOD
```

## Python3

```python
class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        total = pow(2, n, MOD)
        return (total - 2) % MOD
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int monkeyMove(int n) {
    const long long MOD = 1000000007LL;
    long long res = 1, base = 2, exp = n;
    while (exp) {
        if (exp & 1) res = res * base % MOD;
        base = base * base % MOD;
        exp >>= 1;
    }
    res = (res - 2 + MOD) % MOD;
    return (int)res;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const long MOD = 1000000007L;
    
    public int MonkeyMove(int n) {
        long total = ModPow(2L, n, MOD);
        long result = (total - 2 + MOD) % MOD;
        return (int)result;
    }
    
    private long ModPow(long baseVal, long exp, long mod) {
        long res = 1L;
        baseVal %= mod;
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                res = (res * baseVal) % mod;
            }
            baseVal = (baseVal * baseVal) % mod;
            exp >>= 1;
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
var monkeyMove = function(n) {
    const MOD = 1000000007n;
    let base = 2n;
    let exp = BigInt(n);
    let result = 1n;
    while (exp > 0n) {
        if (exp & 1n) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1n;
    }
    result = (result - 2n + MOD) % MOD; // subtract the two non‑collision cases
    return Number(result);
};
```

## Typescript

```typescript
function monkeyMove(n: number): number {
    const MOD = 1000000007n;
    function modPow(base: bigint, exp: bigint, mod: bigint): bigint {
        let result = 1n;
        let b = base % mod;
        let e = exp;
        while (e > 0) {
            if (e & 1n) result = (result * b) % mod;
            b = (b * b) % mod;
            e >>= 1n;
        }
        return result;
    }
    const total = modPow(2n, BigInt(n), MOD);
    let ans = (total - 2n) % MOD;
    if (ans < 0) ans += MOD;
    return Number(ans);
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
    function monkeyMove($n) {
        $mod = self::MOD;
        $result = 1;
        $base = 2 % $mod;
        $exp = $n;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        $ans = $result - 2;
        if ($ans < 0) {
            $ans += $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func monkeyMove(_ n: Int) -> Int {
        var total = modPow(2, n, MOD)
        total = (total - 2 + MOD) % MOD
        return total
    }

    private func modPow(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
        var result: Int64 = 1
        var b: Int64 = Int64(base % mod)
        var e = exp
        let m = Int64(mod)

        while e > 0 {
            if e & 1 == 1 {
                result = (result * b) % m
            }
            b = (b * b) % m
            e >>= 1
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    fun monkeyMove(n: Int): Int {
        var base = 2L
        var exp = n.toLong()
        var result = 1L
        while (exp > 0) {
            if ((exp and 1L) == 1L) {
                result = (result * base) % MOD
            }
            base = (base * base) % MOD
            exp = exp shr 1
        }
        result = (result - 2 + MOD) % MOD
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int monkeyMove(int n) {
    int result = 1;
    int base = 2 % _mod;
    int exp = n;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * base) % _mod;
      }
      base = (base * base) % _mod;
      exp >>= 1;
    }
    result = (result - 2) % _mod;
    if (result < 0) result += _mod;
    return result;
  }
}
```

## Golang

```go
func monkeyMove(n int) int {
	const MOD int64 = 1000000007
	exp := int64(n)
	base := int64(2)
	var res int64 = 1
	for exp > 0 {
		if exp&1 == 1 {
			res = (res * base) % MOD
		}
		base = (base * base) % MOD
		exp >>= 1
	}
	ans := (res - 2) % MOD
	if ans < 0 {
		ans += MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = (result * b) % mod if (e & 1) == 1
    b = (b * b) % mod
    e >>= 1
  end
  result
end

# @param {Integer} n
# @return {Integer}
def monkey_move(n)
  total = mod_pow(2, n, MOD)
  (total - 2) % MOD
end
```

## Scala

```scala
object Solution {
    def monkeyMove(n: Int): Int = {
        val MOD = 1000000007L
        var result = 1L
        var base = 2L
        var exp = n.toLong
        while (exp > 0) {
            if ((exp & 1L) == 1L) result = (result * base) % MOD
            base = (base * base) % MOD
            exp >>= 1
        }
        val ans = (result - 2 + MOD) % MOD
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn monkey_move(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut base: i64, mut exp: i64, modu: i64) -> i64 {
            let mut res = 1i64;
            base %= modu;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = res * base % modu;
                }
                base = base * base % modu;
                exp >>= 1;
            }
            res
        }
        let total = mod_pow(2, n as i64, MOD);
        let ans = (total - 2 + MOD) % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (pow-mod base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (modulo (* b b) MOD)
              (quotient e 2)
              (if (odd? e)
                  (modulo (* res b) MOD)
                  res)))))

(define/contract (monkey-move n)
  (-> exact-integer? exact-integer?)
  (let ((total (pow-mod 2 n)))
    (modulo (- total 2) MOD)))
```

## Erlang

```erlang
-module(solution).
-export([monkey_move/1]).
-define(MOD, 1000000007).

-spec monkey_move(N :: integer()) -> integer().
monkey_move(N) ->
    Mod = ?MOD,
    Pow = pow_mod(2, N, Mod),
    (Pow - 2 + Mod) rem Mod.

pow_mod(Base, Exp, Mod) ->
    pow_mod_iter(Base rem Mod, Exp, 1, Mod).

pow_mod_iter(_, 0, Acc, _Mod) ->
    Acc;
pow_mod_iter(Base, Exp, Acc, Mod) ->
    NewAcc = case (Exp band 1) of
        1 -> (Acc * Base) rem Mod;
        0 -> Acc
    end,
    pow_mod_iter((Base * Base) rem Mod, Exp bsr 1, NewAcc, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  use Bitwise

  @modulus 1_000_000_007

  @spec monkey_move(n :: integer) :: integer
  def monkey_move(n) do
    total = mod_pow(2, n, @modulus)
    rem(total - 2 + @modulus, @modulus)
  end

  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) do
    base = rem(base, mod)

    if (exp &&& 1) == 1 do
      (base * mod_pow(rem(base * base, mod), exp >>> 1, mod)) |> rem(mod)
    else
      mod_pow(rem(base * base, mod), exp >>> 1, mod)
    end
  end
end
```

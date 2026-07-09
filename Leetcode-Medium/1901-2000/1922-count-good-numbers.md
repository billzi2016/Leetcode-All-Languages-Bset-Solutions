# 1922. Count Good Numbers

## Cpp

```cpp
class Solution {
public:
    static const long long MOD = 1000000007LL;
    
    long long modPow(long long base, long long exp) {
        long long result = 1 % MOD;
        base %= MOD;
        while (exp > 0) {
            if (exp & 1) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }
    
    int countGoodNumbers(long long n) {
        long long evenCount = (n + 1) / 2; // positions 0,2,4,...
        long long oddCount = n / 2;       // positions 1,3,5,...
        long long ans = modPow(5, evenCount);
        ans = (ans * modPow(4, oddCount)) % MOD;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    public int countGoodNumbers(long n) {
        long evenCount = (n + 1) / 2;
        long oddCount = n / 2;
        long partEven = modPow(5, evenCount);
        long partOdd = modPow(4, oddCount);
        return (int) ((partEven * partOdd) % MOD);
    }

    private long modPow(long base, long exp) {
        long result = 1L;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        even_cnt = (n + 1) // 2  # positions with even index
        odd_cnt = n // 2         # positions with odd index
        return (pow(5, even_cnt, MOD) * pow(4, odd_cnt, MOD)) % MOD
```

## Python3

```python
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_cnt = (n + 1) // 2
        odd_cnt = n // 2
        return pow(5, even_cnt, MOD) * pow(4, odd_cnt, MOD) % MOD
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const long long MOD = 1000000007LL;

static long long modPow(long long base, long long exp) {
    long long result = 1 % MOD;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

int countGoodNumbers(long long n) {
    long long evenCnt = (n + 1) / 2; // positions with even index
    long long oddCnt  = n / 2;       // positions with odd index
    long long ans = modPow(5, evenCnt);
    ans = (ans * modPow(4, oddCnt)) % MOD;
    return static_cast<int>(ans);
}
```

## Csharp

```csharp
public class Solution
{
    private const long MOD = 1000000007L;
    
    public int CountGoodNumbers(long n)
    {
        long evenCount = (n + 1) / 2;
        long oddCount = n / 2;
        
        long pow5 = PowMod(5, evenCount);
        long pow4 = PowMod(4, oddCount);
        
        long result = (pow5 * pow4) % MOD;
        return (int)result;
    }
    
    private long PowMod(long baseVal, long exp)
    {
        long result = 1L;
        baseVal %= MOD;
        while (exp > 0)
        {
            if ((exp & 1L) == 1L)
                result = (result * baseVal) % MOD;
            baseVal = (baseVal * baseVal) % MOD;
            exp >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countGoodNumbers = function(n) {
    const MOD = 1000000007n;
    
    const evenCount = (BigInt(n) + 1n) / 2n; // positions 0,2,4,...
    const oddCount  = BigInt(n) / 2n;        // positions 1,3,5,...
    
    const modPow = (base, exp) => {
        let result = 1n;
        base %= MOD;
        while (exp > 0n) {
            if (exp & 1n) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return result;
    };
    
    const partEven = modPow(5n, evenCount);
    const partOdd  = modPow(4n, oddCount);
    const ans = (partEven * partOdd) % MOD;
    
    return Number(ans);
};
```

## Typescript

```typescript
function countGoodNumbers(n: number): number {
    const MOD = 1000000007n;

    const evenCount = Math.floor((n + 1) / 2);
    const oddCount = Math.floor(n / 2);

    function powMod(base: bigint, exp: number): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = BigInt(exp);
        while (e > 0n) {
            if ((e & 1n) === 1n) {
                result = (result * b) % MOD;
            }
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }

    const partEven = powMod(5n, evenCount);
    const partOdd = powMod(4n, oddCount);
    const ans = (partEven * partOdd) % MOD;
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countGoodNumbers($n) {
        $mod = 1000000007;
        $evenCnt = intdiv($n + 1, 2);
        $oddCnt  = intdiv($n, 2);

        $pow5 = $this->modPow(5, $evenCnt, $mod);
        $pow4 = $this->modPow(4, $oddCnt, $mod);

        return (int)(($pow5 * $pow4) % $mod);
    }

    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countGoodNumbers(_ n: Int) -> Int {
        let MOD: Int64 = 1_000_000_007
        let nn = Int64(n)
        let evenCount = (nn + 1) / 2
        let oddCount = nn / 2
        
        func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
            var result: Int64 = 1
            var b = base % MOD
            var e = exp
            while e > 0 {
                if e & 1 == 1 {
                    result = (result * b) % MOD
                }
                b = (b * b) % MOD
                e >>= 1
            }
            return result
        }
        
        let part1 = modPow(5, evenCount)
        let part2 = modPow(4, oddCount)
        let ans = (part1 * part2) % MOD
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    private fun modPow(base: Long, exp: Long): Long {
        var result = 1L
        var b = base % MOD
        var e = exp
        while (e > 0) {
            if ((e and 1L) == 1L) {
                result = (result * b) % MOD
            }
            b = (b * b) % MOD
            e = e shr 1
        }
        return result
    }

    fun countGoodNumbers(n: Long): Int {
        val evenCount = (n + 1) / 2
        val oddCount = n / 2
        val partEven = modPow(5L, evenCount)
        val partOdd = modPow(4L, oddCount)
        val ans = (partEven * partOdd) % MOD
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countGoodNumbers(int n) {
    int evenCount = (n + 1) ~/ 2;
    int oddCount = n ~/ 2;
    int partEven = _modPow(5, evenCount);
    int partOdd = _modPow(4, oddCount);
    return ((partEven * partOdd) % _mod).toInt();
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
const mod int64 = 1000000007

func powMod(base, exp int64) int64 {
    result := int64(1)
    b := base % mod
    for exp > 0 {
        if exp&1 == 1 {
            result = result * b % mod
        }
        b = b * b % mod
        exp >>= 1
    }
    return result
}

func countGoodNumbers(n int64) int {
    even := (n + 1) / 2
    odd := n / 2
    res := powMod(5, even)
    res = res * powMod(4, odd) % mod
    return int(res)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(base, exp, mod)
  result = 1
  base %= mod
  while exp > 0
    result = (result * base) % mod if (exp & 1) == 1
    base = (base * base) % mod
    exp >>= 1
  end
  result
end

# @param {Integer} n
# @return {Integer}
def count_good_numbers(n)
  even_cnt = (n + 1) / 2
  odd_cnt = n / 2
  (mod_pow(5, even_cnt, MOD) * mod_pow(4, odd_cnt, MOD)) % MOD
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L

  private def modPow(base: Long, exp: Long): Long = {
    var result = 1L
    var b = base % MOD
    var e = exp
    while (e > 0) {
      if ((e & 1L) == 1L) result = (result * b) % MOD
      b = (b * b) % MOD
      e >>= 1
    }
    result
  }

  def countGoodNumbers(n: Long): Int = {
    val evenCount = (n + 1) / 2
    val oddCount = n / 2
    val partEven = modPow(5, evenCount)
    val partOdd = modPow(4, oddCount)
    ((partEven * partOdd) % MOD).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_good_numbers(n: i64) -> i32 {
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
        let even_cnt = (n + 1) / 2;
        let odd_cnt = n / 2;
        let ans = mod_pow(5, even_cnt, MOD) * mod_pow(4, odd_cnt, MOD) % MOD;
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
              (if (odd? e) (modulo (* res b) MOD) res)))))

(define/contract (count-good-numbers n)
  (-> exact-integer? exact-integer?)
  (let* ((e1 (quotient (+ n 1) 2))
         (e2 (quotient n 2))
         (part1 (pow-mod 5 e1))
         (part2 (pow-mod 4 e2)))
    (modulo (* part1 part2) MOD)))
```

## Erlang

```erlang
-module(solution).
-export([count_good_numbers/1]).

-define(MOD, 1000000007).

-spec count_good_numbers(N :: integer()) -> integer().
count_good_numbers(N) ->
    EvenCnt = (N + 1) div 2,
    OddCnt = N div 2,
    Pow5 = pow_mod(5, EvenCnt),
    Pow4 = pow_mod(4, OddCnt),
    (Pow5 * Pow4) rem ?MOD.

-spec pow_mod(Base :: integer(), Exp :: integer()) -> integer().
pow_mod(_, 0) ->
    1;
pow_mod(Base, Exp) when Exp band 1 =:= 0 ->
    Half = pow_mod(Base, Exp div 2),
    (Half * Half) rem ?MOD;
pow_mod(Base, Exp) ->
    Half = pow_mod(Base, Exp div 2),
    ((Half * Half) rem ?MOD * (Base rem ?MOD)) rem ?MOD.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  @spec count_good_numbers(n :: integer) :: integer
  def count_good_numbers(n) do
    even_cnt = div(n + 1, 2)
    odd_cnt = div(n, 2)

    pow5 = mod_pow(5, even_cnt)
    pow4 = mod_pow(4, odd_cnt)

    rem(pow5 * pow4, @mod)
  end

  defp mod_pow(base, exp) do
    mod_pow(rem(base, @mod), exp, 1)
  end

  defp mod_pow(_base, 0, acc), do: acc

  defp mod_pow(base, exp, acc) do
    new_acc = if rem(exp, 2) == 1, do: rem(acc * base, @mod), else: acc
    new_base = rem(base * base, @mod)
    mod_pow(new_base, div(exp, 2), new_acc)
  end
end
```

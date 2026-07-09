# 0372. Super Pow

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1337;
    
    int superPow(int a, vector<int>& b) {
        return dfs(a % MOD, b);
    }
    
private:
    int powmod(long long x, int e) {
        long long res = 1;
        x %= MOD;
        while (e) {
            if (e & 1) res = (res * x) % MOD;
            x = (x * x) % MOD;
            e >>= 1;
        }
        return (int)res;
    }
    
    int dfs(int a, vector<int>& b) {
        if (b.empty()) return 1;
        int last = b.back();
        b.pop_back();
        int part = dfs(a, b);
        int part10 = powmod(part, 10);
        int partLast = powmod(a, last);
        return (int)((long long)part10 * partLast % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1337;

    public int superPow(int a, int[] b) {
        int aMod = a % MOD;
        int result = 1;
        for (int digit : b) {
            result = powMod(result, 10);
            result = (int) ((long) result * powMod(aMod, digit) % MOD);
        }
        return result;
    }

    private int powMod(int x, int n) {
        long res = 1;
        long base = x % MOD;
        while (n > 0) {
            if ((n & 1) == 1) {
                res = (res * base) % MOD;
            }
            base = (base * base) % MOD;
            n >>= 1;
        }
        return (int) res;
    }
}
```

## Python

```python
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337
        a %= MOD
        result = 1
        for digit in b:
            # raise current result to the power of 10 modulo MOD
            result = pow(result, 10, MOD)
            # multiply by a^digit modulo MOD
            result = (result * pow(a, digit, MOD)) % MOD
        return result
```

## Python3

```python
from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def powmod(x: int, n: int) -> int:
            x %= MOD
            res = 1
            while n:
                if n & 1:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                n >>= 1
            return res

        def helper(exp_digits: List[int]) -> int:
            if not exp_digits:
                return 1
            last = exp_digits.pop()
            part = helper(exp_digits)
            part = powmod(part, 10)
            part = (part * powmod(a, last)) % MOD
            return part

        return helper(b[:])
```

## C

```c
#include <stddef.h>

#define MOD 1337

static int powmod(int x, int n) {
    long long res = 1;
    long long base = x % MOD;
    while (n > 0) {
        if (n & 1)
            res = (res * base) % MOD;
        base = (base * base) % MOD;
        n >>= 1;
    }
    return (int)res;
}

int superPow(int a, int* b, int bSize) {
    int a_mod = a % MOD;
    long long result = 1;
    for (int i = 0; i < bSize; ++i) {
        result = powmod((int)result, 10);
        result = (result * powmod(a_mod, b[i])) % MOD;
    }
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1337;
    
    private int PowMod(int x, int n) {
        int result = 1;
        x %= MOD;
        while (n > 0) {
            if ((n & 1) == 1) result = (result * x) % MOD;
            x = (x * x) % MOD;
            n >>= 1;
        }
        return result;
    }

    public int SuperPow(int a, int[] b) {
        a %= MOD;
        int result = 1;
        foreach (int digit in b) {
            result = PowMod(result, 10);
            result = (result * PowMod(a, digit)) % MOD;
        }
        return result;
    }
}
```

## Javascript

```javascript
const MOD = 1337;

function modPow(base, exp) {
    base %= MOD;
    let result = 1;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

/**
 * @param {number} a
 * @param {number[]} b
 * @return {number}
 */
var superPow = function(a, b) {
    if (b.length === 0) return 1;
    const last = b.pop();
    const part1 = modPow(a, last);
    const part2 = modPow(superPow(a, b), 10);
    return (part1 * part2) % MOD;
};
```

## Typescript

```typescript
function superPow(a: number, b: number[]): number {
    const MOD = 1337;
    const modPow = (base: number, exp: number): number => {
        let result = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp & 1) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    };
    let ans = 1;
    for (const digit of b) {
        ans = modPow(ans, 10);
        ans = (ans * modPow(a, digit)) % MOD;
    }
    return ans;
};
```

## Php

```php
class Solution {
    const MOD = 1337;

    /**
     * @param Integer $a
     * @param Integer[] $b
     * @return Integer
     */
    function superPow($a, $b) {
        $a %= self::MOD;
        $result = 1;
        foreach ($b as $digit) {
            // result = (result^10) % MOD
            $result = $this->powmod($result, 10);
            // multiply by a^digit % MOD
            $result = ($result * $this->powmod($a, $digit)) % self::MOD;
        }
        return $result;
    }

    private function powmod($base, $exp) {
        $base %= self::MOD;
        $res = 1;
        while ($exp > 0) {
            if ($exp & 1) {
                $res = ($res * $base) % self::MOD;
            }
            $base = ($base * $base) % self::MOD;
            $exp >>= 1;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func superPow(_ a: Int, _ b: [Int]) -> Int {
        let mod = 1337
        let aMod = a % mod
        
        func powMod(_ base: Int, _ exp: Int) -> Int {
            var result = 1
            var b = base % mod
            var e = exp
            while e > 0 {
                if (e & 1) == 1 {
                    result = (result * b) % mod
                }
                b = (b * b) % mod
                e >>= 1
            }
            return result
        }
        
        var result = 1
        for digit in b {
            result = powMod(result, 10)
            let part = powMod(aMod, digit)
            result = (result * part) % mod
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1337
    fun superPow(a: Int, b: IntArray): Int {
        var result = 1
        val aMod = a % MOD
        for (digit in b) {
            result = (pow(result, 10) * pow(aMod, digit)) % MOD
        }
        return result
    }

    private fun pow(x: Int, y: Int): Int {
        var base = x.toLong()
        var exp = y
        var res = 1L
        while (exp > 0) {
            if ((exp and 1) == 1) {
                res = (res * base) % MOD
            }
            base = (base * base) % MOD
            exp = exp shr 1
        }
        return res.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1337;

  int superPow(int a, List<int> b) {
    int aMod = a % _mod;
    int result = 1;
    for (int digit in b) {
      result = _powMod(result, 10);
      result = (result * _powMod(aMod, digit)) % _mod;
    }
    return result;
  }

  int _powMod(int base, int exp) {
    int res = 1;
    int cur = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        res = (res * cur) % _mod;
      }
      cur = (cur * cur) % _mod;
      exp >>= 1;
    }
    return res;
  }
}
```

## Golang

```go
func superPow(a int, b []int) int {
	const MOD = 1337
	var modPow func(int, int) int
	modPow = func(base, exp int) int {
		res := 1 % MOD
		base %= MOD
		for exp > 0 {
			if exp&1 == 1 {
				res = (res * base) % MOD
			}
			base = (base * base) % MOD
			exp >>= 1
		}
		return res
	}

	result := 1
	for _, d := range b {
		result = modPow(result, 10)
		result = (result * modPow(a, d)) % MOD
	}
	return result
}
```

## Ruby

```ruby
def pow_mod(x, n, mod)
  res = 1
  x %= mod
  while n > 0
    res = (res * x) % mod if (n & 1) == 1
    x = (x * x) % mod
    n >>= 1
  end
  res
end

def super_pow(a, b)
  mod = 1337
  a %= mod
  result = 1
  b.each do |digit|
    result = (pow_mod(result, 10, mod) * pow_mod(a, digit, mod)) % mod
  end
  result
end
```

## Scala

```scala
object Solution {
    def superPow(a: Int, b: Array[Int]): Int = {
        val MOD = 1337

        def powMod(x: Int, n: Int): Int = {
            var result = 1L
            var base = (x % MOD).toLong
            var exp = n
            while (exp > 0) {
                if ((exp & 1) == 1) result = (result * base) % MOD
                base = (base * base) % MOD
                exp >>= 1
            }
            result.toInt
        }

        var ans = 1
        for (digit <- b) {
            ans = powMod(ans, 10)
            ans = (ans * powMod(a, digit)) % MOD
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn super_pow(a: i32, b: Vec<i32>) -> i32 {
        const MOD: i32 = 1337;
        fn pow_mod(mut x: i32, mut n: i32) -> i32 {
            const MOD: i32 = 1337;
            let mut result: i64 = 1;
            let mut base: i64 = (x % MOD) as i64;
            while n > 0 {
                if n & 1 == 1 {
                    result = result * base % MOD as i64;
                }
                base = base * base % MOD as i64;
                n >>= 1;
            }
            result as i32
        }

        let a_mod = a % MOD;
        let mut result = 1i32;
        for &digit in b.iter() {
            result = pow_mod(result, 10);
            let term = pow_mod(a_mod, digit);
            result = ((result as i64 * term as i64) % MOD as i64) as i32;
        }
        result
    }
}
```

## Racket

```racket
#lang racket

(define MOD 1337)

(define (pow-mod a e)
  (let loop ((base (modulo a MOD)) (exp e) (res 1))
    (if (= exp 0)
        res
        (let* ((res2 (if (odd? exp) (modulo (* res base) MOD) res))
               (base2 (modulo (* base base) MOD)))
          (loop base2 (quotient exp 2) res2)))))

(define/contract (super-pow a b)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let loop ((digits b) (result 1))
    (if (null? digits)
        result
        (let* ((d (car digits))
               (new-result (modulo (* (pow-mod result 10) (pow-mod a d)) MOD)))
          (loop (cdr digits) new-result)))))
```

## Erlang

```erlang
-module(solution).
-export([super_pow/2]).

-spec super_pow(integer(), [integer()]) -> integer().
super_pow(A, B) ->
    Mod = 1337,
    A1 = A rem Mod,
    lists:foldl(fun(Digit, Acc) ->
        (pow_mod(Acc, 10, Mod) * pow_mod(A1, Digit, Mod)) rem Mod
    end, 1, B).

-spec pow_mod(integer(), integer(), integer()) -> integer().
pow_mod(_, 0, _) -> 1;
pow_mod(Base, Exp, Mod) when Exp > 0 ->
    case Exp band 1 of
        1 ->
            (Base * pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod)) rem Mod;
        0 ->
            pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec super_pow(a :: integer, b :: [integer]) :: integer
  def super_pow(a, b) do
    a_mod = rem(a, 1337)

    Enum.reduce(b, 1, fn digit, acc ->
      part1 = powmod(acc, 10, 1337)
      part2 = powmod(a_mod, digit, 1337)
      rem(part1 * part2, 1337)
    end)
  end

  defp powmod(_base, 0, _mod), do: 1

  defp powmod(base, exp, mod) when exp > 0 do
    if rem(exp, 2) == 1 do
      tmp = powmod(rem(base * base, mod), div(exp - 1, 2), mod)
      rem(base * tmp, mod)
    else
      powmod(rem(base * base, mod), div(exp, 2), mod)
    end
  end
end
```

# 1808. Maximize Number of Nice Divisors

## Cpp

```cpp
class Solution {
public:
    int maxNiceDivisors(int primeFactors) {
        const long long MOD = 1000000007LL;
        if (primeFactors <= 4) return primeFactors % MOD;
        long long cnt3 = primeFactors / 3;
        int rem = primeFactors % 3;
        long long ans;
        if (rem == 0) {
            ans = modPow(3, cnt3, MOD);
        } else if (rem == 1) {
            cnt3 -= 1;
            ans = modPow(3, cnt3, MOD);
            ans = ans * 4 % MOD;
        } else { // rem == 2
            ans = modPow(3, cnt3, MOD);
            ans = ans * 2 % MOD;
        }
        return (int)ans;
    }
private:
    long long modPow(long long base, long long exp, long long mod) {
        long long res = 1 % mod;
        while (exp > 0) {
            if (exp & 1) res = res * base % mod;
            base = base * base % mod;
            exp >>= 1;
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    public int maxNiceDivisors(int primeFactors) {
        if (primeFactors <= 4) return primeFactors;
        long ans;
        int rem = primeFactors % 3;
        if (rem == 0) {
            ans = modPow(3, primeFactors / 3);
        } else if (rem == 1) {
            ans = modPow(3, (primeFactors - 4) / 3);
            ans = (ans * 4) % MOD;
        } else { // rem == 2
            ans = modPow(3, primeFactors / 3);
            ans = (ans * 2) % MOD;
        }
        return (int) ans;
    }

    private long modPow(long base, int exp) {
        long result = 1L;
        long b = base % MOD;
        long e = exp;
        while (e > 0) {
            if ((e & 1) == 1) {
                result = (result * b) % MOD;
            }
            b = (b * b) % MOD;
            e >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if primeFactors <= 3:
            return primeFactors % MOD

        rem = primeFactors % 3
        if rem == 0:
            return pow(3, primeFactors // 3, MOD)
        elif rem == 1:
            # use two 2's instead of one 3 and the remainder 1
            return (pow(3, (primeFactors - 4) // 3, MOD) * 4) % MOD
        else:  # rem == 2
            return (pow(3, primeFactors // 3, MOD) * 2) % MOD
```

## Python3

```python
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        if primeFactors <= 3:
            return primeFactors % MOD
        rem = primeFactors % 3
        if rem == 0:
            return pow(3, primeFactors // 3, MOD)
        if rem == 1:
            return (pow(3, primeFactors // 3 - 1, MOD) * 4) % MOD
        # rem == 2
        return (pow(3, primeFactors // 3, MOD) * 2) % MOD
```

## C

```c
#include <stdint.h>

#define MOD 1000000007LL

static long long modPow(long long base, long long exp) {
    long long result = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1)
            result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

int maxNiceDivisors(int primeFactors) {
    if (primeFactors <= 4)
        return primeFactors;

    long long cnt3 = primeFactors / 3;
    int rem = primeFactors % 3;
    long long ans;

    if (rem == 0) {
        ans = modPow(3, cnt3);
    } else if (rem == 1) {
        // use one less 3 and make a 4 (2*2)
        ans = modPow(3, cnt3 - 1);
        ans = (ans * 4) % MOD;
    } else { // rem == 2
        ans = modPow(3, cnt3);
        ans = (ans * 2) % MOD;
    }

    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    private const long MOD = 1000000007L;

    public int MaxNiceDivisors(int primeFactors)
    {
        if (primeFactors <= 3) return primeFactors;

        long count3 = primeFactors / 3;
        int remainder = primeFactors % 3;

        long result;
        if (remainder == 0)
        {
            result = ModPow(3, count3);
        }
        else if (remainder == 1)
        {
            // use one less 3 and two 2's (4)
            result = ModPow(3, count3 - 1) * 4 % MOD;
        }
        else // remainder == 2
        {
            result = ModPow(3, count3) * 2 % MOD;
        }

        return (int)result;
    }

    private long ModPow(long baseVal, long exp)
    {
        long res = 1L;
        long b = baseVal % MOD;
        while (exp > 0)
        {
            if ((exp & 1) == 1)
                res = (res * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} primeFactors
 * @return {number}
 */
var maxNiceDivisors = function(primeFactors) {
    const MOD = 1000000007n;
    
    const modPow = (base, exp) => {
        let result = 1n;
        let b = base % MOD;
        while (exp > 0) {
            if (exp & 1) {
                result = (result * b) % MOD;
            }
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return result;
    };
    
    if (primeFactors === 1) return 1;
    
    const rem = primeFactors % 3;
    let ans;
    
    if (rem === 0) {
        ans = modPow(3n, Math.floor(primeFactors / 3));
    } else if (rem === 1) {
        // use two 2's instead of a 3+1
        const exp = Math.floor((primeFactors - 4) / 3);
        ans = modPow(3n, exp);
        ans = (ans * 4n) % MOD;
    } else { // rem === 2
        const exp = Math.floor(primeFactors / 3);
        ans = modPow(3n, exp);
        ans = (ans * 2n) % MOD;
    }
    
    return Number(ans);
};
```

## Typescript

```typescript
function maxNiceDivisors(primeFactors: number): number {
    const MOD = 1000000007n;
    if (primeFactors <= 4) return primeFactors % Number(MOD);
    
    function modPow(base: bigint, exp: number): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if (e & 1) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>>= 1;
        }
        return result;
    }

    let cnt3 = Math.floor(primeFactors / 3);
    const rem = primeFactors % 3;
    let ans: bigint;

    if (rem === 0) {
        ans = modPow(3n, cnt3);
    } else if (rem === 1) {
        cnt3 -= 1;
        ans = (modPow(3n, cnt3) * 4n) % MOD;
    } else { // rem === 2
        ans = (modPow(3n, cnt3) * 2n) % MOD;
    }

    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $primeFactors
     * @return Integer
     */
    function maxNiceDivisors($primeFactors) {
        $MOD = 1000000007;
        if ($primeFactors <= 4) {
            return $primeFactors;
        }
        $a = intdiv($primeFactors, 3);
        $rem = $primeFactors % 3;

        if ($rem == 0) {
            return $this->modPow(3, $a, $MOD);
        } elseif ($rem == 1) {
            // replace one group of (3+1) with (2+2)
            $res = $this->modPow(3, $a - 1, $MOD);
            $res = ($res * 4) % $MOD;
            return $res;
        } else { // $rem == 2
            $res = $this->modPow(3, $a, $MOD);
            $res = ($res * 2) % $MOD;
            return $res;
        }
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
    func maxNiceDivisors(_ primeFactors: Int) -> Int {
        let mod: Int64 = 1_000_000_007
        if primeFactors <= 4 { return primeFactors }
        
        func powMod(_ base: Int64, _ exp: Int64) -> Int64 {
            var result: Int64 = 1
            var b = base % mod
            var e = exp
            while e > 0 {
                if e & 1 == 1 {
                    result = (result * b) % mod
                }
                b = (b * b) % mod
                e >>= 1
            }
            return result
        }
        
        let n = Int64(primeFactors)
        let count3 = n / 3
        let remainder = n % 3
        
        var ans: Int64 = 0
        if remainder == 0 {
            ans = powMod(3, count3)
        } else if remainder == 1 {
            ans = (powMod(3, count3 - 1) * 4) % mod
        } else { // remainder == 2
            ans = (powMod(3, count3) * 2) % mod
        }
        
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) {
                res = (res * b) % MOD
            }
            b = (b * b) % MOD
            e = e shr 1
        }
        return res
    }

    fun maxNiceDivisors(primeFactors: Int): Int {
        if (primeFactors <= 3) return primeFactors
        var cnt3 = primeFactors / 3
        val rem = primeFactors % 3
        val result = when (rem) {
            0 -> modPow(3L, cnt3.toLong())
            1 -> {
                cnt3 -= 1
                (modPow(3L, cnt3.toLong()) * 4) % MOD
            }
            else -> { // rem == 2
                (modPow(3L, cnt3.toLong()) * 2) % MOD
            }
        }
        return result.toInt()
    }
}
```

## Golang

```go
func maxNiceDivisors(primeFactors int) int {
	const MOD = 1000000007
	if primeFactors <= 4 {
		return primeFactors
	}
	cnt3 := primeFactors / 3
	rem := primeFactors % 3

	powMod := func(a, b int) int64 {
		res := int64(1)
		base := int64(a % MOD)
		exp := b
		for exp > 0 {
			if exp&1 == 1 {
				res = res * base % MOD
			}
			base = base * base % MOD
			exp >>= 1
		}
		return res
	}

	var result int64
	if rem == 0 {
		result = powMod(3, cnt3)
	} else if rem == 1 {
		result = powMod(3, cnt3-1) * 4 % MOD
	} else { // rem == 2
		result = powMod(3, cnt3) * 2 % MOD
	}
	return int(result)
}
```

## Ruby

```ruby
def max_nice_divisors(prime_factors)
  mod = 1_000_000_007
  return prime_factors if prime_factors <= 3

  a = prime_factors / 3
  b = prime_factors % 3

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

  if b == 0
    mod_pow(3, a, mod)
  elsif b == 1
    (mod_pow(3, a - 1, mod) * 4) % mod
  else # b == 2
    (mod_pow(3, a, mod) * 2) % mod
  end
end
```

## Scala

```scala
object Solution {
    private val MOD: Long = 1000000007L

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

    def maxNiceDivisors(primeFactors: Int): Int = {
        if (primeFactors <= 3) return primeFactors
        val cnt3 = primeFactors / 3
        val rem = primeFactors % 3
        val ans: Long = rem match {
            case 0 => modPow(3L, cnt3.toLong)
            case 1 => (modPow(3L, (cnt3 - 1).toLong) * 4L) % MOD
            case 2 => (modPow(3L, cnt3.toLong) * 2L) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_nice_divisors(prime_factors: i32) -> i32 {
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

        let n = prime_factors as i64;
        if n <= 4 {
            return n as i32;
        }
        let q = n / 3;
        let r = n % 3;
        let ans = match r {
            0 => mod_pow(3, q, MOD),
            1 => (mod_pow(3, q - 1, MOD) * 4) % MOD,
            _ => (mod_pow(3, q, MOD) * 2) % MOD,
        };
        ans as i32
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
              (if (odd? e)
                  (remainder (* res b) MOD)
                  res)))))

(define/contract (max-nice-divisors primeFactors)
  (-> exact-integer? exact-integer?)
  (cond
    [(<= primeFactors 3) primeFactors]
    [else
     (let* ([a (quotient primeFactors 3)]
            [r (remainder primeFactors 3)])
       (cond
         [(= r 0) (modpow 3 a)]
         [(= r 1)
          (remainder (* (modpow 3 (- a 1)) 4) MOD)]
         [else ; r == 2
          (remainder (* (modpow 3 a) 2) MOD)]))]))
```

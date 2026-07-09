# 3405. Count the Number of Arrays with K Matching Adjacent Elements

## Cpp

```cpp
class Solution {
public:
    int countGoodArrays(int n, int m, int k) {
        const long long MOD = 1000000007LL;
        // Precompute factorials up to n
        vector<long long> fact(n + 1), invFact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        auto modPow = [&](long long a, long long e) -> long long {
            long long res = 1 % MOD;
            a %= MOD;
            while (e) {
                if (e & 1) res = res * a % MOD;
                a = a * a % MOD;
                e >>= 1;
            }
            return res;
        };
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i >= 1; --i) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
        // Compute C(n-1, k)
        if (k < 0 || k > n - 1) return 0;
        long long comb = fact[n - 1] * invFact[k] % MOD * invFact[n - 1 - k] % MOD;
        long long powPart = modPow(m - 1LL, n - k - 1);
        long long ans = (static_cast<long long>(m) % MOD) * comb % MOD;
        ans = ans * powPart % MOD;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int countGoodArrays(int n, int m, int k) {
        if (m == 1) {
            return (k == n - 1) ? 1 : 0;
        }
        // precompute factorials up to n-1
        long[] fact = new long[n];
        long[] invFact = new long[n];
        fact[0] = 1;
        for (int i = 1; i < n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[n - 1] = modPow(fact[n - 1], MOD - 2);
        for (int i = n - 2; i >= 0; i--) {
            invFact[i] = invFact[i + 1] * (i + 1) % MOD;
        }

        long comb = fact[n - 1];
        comb = comb * invFact[k] % MOD;
        comb = comb * invFact[n - 1 - k] % MOD;

        long pow = modPow(m - 1L, n - k - 1);

        long ans = (m % MOD) * comb % MOD;
        ans = ans * pow % MOD;
        return (int) ans;
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
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Edge case when m == 1
        if m == 1:
            return 1 if k == n - 1 else 0

        # Precompute factorials up to n
        size = n
        fact = [1] * (size + 1)
        for i in range(1, size + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (size + 1)
        inv_fact[size] = pow(fact[size], MOD - 2, MOD)
        for i in range(size, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        ways_choose = comb(n - 1, k)
        ways_colors = pow(m - 1, n - k - 1, MOD)

        result = m % MOD
        result = result * ways_choose % MOD
        result = result * ways_colors % MOD
        return result
```

## Python3

```python
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        # Precompute factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a: int, b: int) -> int:
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        ways_choose = comb(n - 1, k)
        power = pow(m - 1, n - k - 1, MOD) if n - k - 1 >= 0 else 1
        ans = (m % MOD) * ways_choose % MOD * power % MOD
        return ans
```

## C

```c
#include <stdlib.h>

static const long long MOD = 1000000007LL;

static long long mod_pow(long long a, long long e) {
    long long res = 1 % MOD;
    a %= MOD;
    while (e > 0) {
        if (e & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return res;
}

int countGoodArrays(int n, int m, int k) {
    if (k < 0 || k > n - 1) return 0;

    long long *fact = (long long *)malloc((n + 1) * sizeof(long long));
    long long *invFact = (long long *)malloc((n + 1) * sizeof(long long));

    fact[0] = 1;
    for (int i = 1; i <= n; ++i)
        fact[i] = fact[i - 1] * i % MOD;

    invFact[n] = mod_pow(fact[n], MOD - 2);
    for (int i = n; i >= 1; --i)
        invFact[i - 1] = invFact[i] * i % MOD;

    long long comb = fact[n - 1];
    comb = comb * invFact[k] % MOD;
    comb = comb * invFact[(n - 1) - k] % MOD;

    long long powPart = mod_pow((long long)m - 1, (long long)n - k - 1);

    long long ans = ((long long)m % MOD) * comb % MOD;
    ans = ans * powPart % MOD;

    free(fact);
    free(invFact);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    private const long MOD = 1000000007L;
    
    public int CountGoodArrays(int n, int m, int k) {
        if (k > n - 1) return 0;

        int limit = n; // need factorials up to n
        long[] fact = new long[limit + 1];
        long[] invFact = new long[limit + 1];
        fact[0] = 1;
        for (int i = 1; i <= limit; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[limit] = ModPow(fact[limit], MOD - 2);
        for (int i = limit; i >= 1; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }

        long comb = fact[n - 1];
        comb = comb * invFact[k] % MOD;
        comb = comb * invFact[n - 1 - k] % MOD;

        long powPart = ModPow(m - 1L, n - k - 1);
        long result = (m % MOD) * comb % MOD * powPart % MOD;
        return (int)(result % MOD);
    }

    private long ModPow(long baseVal, long exp) {
        long res = 1;
        baseVal %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = res * baseVal % MOD;
            baseVal = baseVal * baseVal % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Javascript

```javascript
const MOD = 1000000007n;

function modPow(base, exp) {
    let result = 1n;
    base %= MOD;
    while (exp > 0n) {
        if (exp & 1n) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1n;
    }
    return result;
}

/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var countGoodArrays = function(n, m, k) {
    const fact = new Array(n + 1);
    const invFact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * BigInt(i + 1)) % MOD;
    }
    const comb = (a, b) => {
        if (b < 0 || b > a) return 0n;
        return (((fact[a] * invFact[b]) % MOD) * invFact[a - b]) % MOD;
    };
    let ans = BigInt(m) % MOD;
    ans = (ans * comb(n - 1, k)) % MOD;
    const exp = n - k - 1;
    if (exp > 0) {
        const pow = modPow(BigInt(m - 1), BigInt(exp));
        ans = (ans * pow) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function countGoodArrays(n: number, m: number, k: number): number {
    const MOD = 1000000007n;

    // fast exponentiation (base^exp % MOD)
    function modPow(base: bigint, exp: bigint): bigint {
        let result = 1n;
        let b = ((base % MOD) + MOD) % MOD;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }

    // precompute factorials up to n
    const size = n; // need up to n-1, but allocate n for simplicity
    const fact: bigint[] = new Array(size + 1);
    const invFact: bigint[] = new Array(size + 1);
    fact[0] = 1n;
    for (let i = 1; i <= size; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    invFact[size] = modPow(fact[size], MOD - 2n);
    for (let i = size; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    // combination C(n-1, k)
    const nn = n - 1;
    let comb = 0n;
    if (k >= 0 && k <= nn) {
        comb = fact[nn];
        comb = (comb * invFact[k]) % MOD;
        comb = (comb * invFact[nn - k]) % MOD;
    }

    const powPart = modPow(BigInt(m - 1), BigInt(n - k - 1));
    let ans = (BigInt(m) * comb) % MOD;
    ans = (ans * powPart) % MOD;

    return Number(ans);
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer $k
     * @return Integer
     */
    function countGoodArrays($n, $m, $k) {
        if ($k > $n - 1) return 0;
        // precompute factorials up to n
        $fact = array_fill(0, $n + 1, 0);
        $invFact = array_fill(0, $n + 1, 0);
        $mod = self::MOD;

        $fact[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $fact[$i] = ($fact[$i - 1] * $i) % $mod;
        }

        $invFact[$n] = $this->modPow($fact[$n], $mod - 2);
        for ($i = $n; $i >= 1; $i--) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % $mod;
        }

        // C(n-1, k)
        $comb = $this->nCr($n - 1, $k, $fact, $invFact);

        // (m-1)^(n-k-1)
        $pow = $this->modPow($m - 1, $n - $k - 1);

        $result = ($m % $mod);
        $result = ($result * $comb) % $mod;
        $result = ($result * $pow) % $mod;

        return (int)$result;
    }

    private function modPow($base, $exp) {
        $mod = self::MOD;
        $base %= $mod;
        $result = 1;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }

    private function nCr($n, $r, $fact, $invFact) {
        if ($r < 0 || $r > $n) return 0;
        $mod = self::MOD;
        $res = ($fact[$n] * $invFact[$r]) % $mod;
        $res = ($res * $invFact[$n - $r]) % $mod;
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func countGoodArrays(_ n: Int, _ m: Int, _ k: Int) -> Int {
        // Special case when only one possible value
        if m == 1 {
            return k == n - 1 ? 1 : 0
        }

        // Pre‑compute factorials and inverse factorials up to n
        var fact = [Int64](repeating: 0, count: n + 1)
        var invFact = [Int64](repeating: 0, count: n + 1)
        fact[0] = 1
        if n >= 1 {
            for i in 1...n {
                fact[i] = fact[i - 1] * Int64(i) % Int64(MOD)
            }
        }

        func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
            var result: Int64 = 1
            var b = base % Int64(MOD)
            var e = exp
            while e > 0 {
                if (e & 1) == 1 {
                    result = result * b % Int64(MOD)
                }
                b = b * b % Int64(MOD)
                e >>= 1
            }
            return result
        }

        invFact[n] = modPow(fact[n], Int64(MOD - 2))
        if n >= 1 {
            for i in stride(from: n, to: 0, by: -1) {
                invFact[i - 1] = invFact[i] * Int64(i) % Int64(MOD)
            }
        }

        func comb(_ N: Int, _ K: Int) -> Int64 {
            if K < 0 || K > N { return 0 }
            let res = fact[N] * invFact[K] % Int64(MOD) * invFact[N - K] % Int64(MOD)
            return res
        }

        // m * C(n-1, k) * (m-1)^(n-k-1)
        let choose = comb(n - 1, k)
        let power = modPow(Int64(m - 1), Int64(n - k - 1))
        var ans = Int64(m) % Int64(MOD)
        ans = ans * choose % Int64(MOD)
        ans = ans * power % Int64(MOD)

        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    fun countGoodArrays(n: Int, m: Int, k: Int): Int {
        if (k > n - 1) return 0
        val max = n
        val fact = LongArray(max + 1)
        val invFact = LongArray(max + 1)
        fact[0] = 1L
        for (i in 1..max) {
            fact[i] = fact[i - 1] * i % MOD
        }

        fun modPow(baseInput: Long, expInput: Long): Long {
            var base = baseInput % MOD
            var exp = expInput
            var res = 1L
            while (exp > 0) {
                if ((exp and 1L) == 1L) res = res * base % MOD
                base = base * base % MOD
                exp = exp shr 1
            }
            return res
        }

        invFact[max] = modPow(fact[max], MOD - 2)
        for (i in max downTo 1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }

        fun nCr(nn: Int, rr: Int): Long {
            if (rr < 0 || rr > nn) return 0L
            return fact[nn] * invFact[rr] % MOD * invFact[nn - rr] % MOD
        }

        val comb = nCr(n - 1, k)
        val powPart = modPow((m - 1).toLong(), (n - k - 1).toLong())
        var ans = m.toLong() % MOD
        ans = ans * comb % MOD
        ans = ans * powPart % MOD
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int countGoodArrays(int n, int m, int k) {
    if (k < 0 || k > n - 1) return 0;

    // factorials and inverse factorials up to n
    List<int> fact = List.filled(n + 1, 0);
    List<int> invFact = List.filled(n + 1, 0);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) {
      fact[i] = (fact[i - 1] * i) % _MOD;
    }
    invFact[n] = _modPow(fact[n], _MOD - 2);
    for (int i = n - 1; i >= 0; --i) {
      invFact[i] = (invFact[i + 1] * (i + 1)) % _MOD;
    }

    int comb(int N, int K) {
      if (K < 0 || K > N) return 0;
      return (((fact[N] * invFact[K]) % _MOD) * invFact[N - K]) % _MOD;
    }

    int ans = m % _MOD;
    ans = (ans * comb(n - 1, k)) % _MOD;
    ans = (ans * _modPow(m - 1, n - k - 1)) % _MOD;
    return ans;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = ((base % _MOD) + _MOD) % _MOD;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _MOD;
      }
      b = (b * b) % _MOD;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
package main

const mod int64 = 1000000007

func countGoodArrays(n int, m int, k int) int {
	maxN := n
	fact := make([]int64, maxN+1)
	invFact := make([]int64, maxN+1)

	fact[0] = 1
	for i := 1; i <= maxN; i++ {
		fact[i] = fact[i-1] * int64(i) % mod
	}
	invFact[maxN] = modPow(fact[maxN], mod-2)
	for i := maxN - 1; i >= 0; i-- {
		invFact[i] = invFact[i+1] * int64(i+1) % mod
	}

	comb := func(N, K int) int64 {
		if K < 0 || K > N {
			return 0
		}
		return fact[N] * invFact[K] % mod * invFact[N-K] % mod
	}

	c := comb(n-1, k)
	powPart := modPow(int64(m-1), int64(n-k-1))
	res := (int64(m) * c % mod) * powPart % mod
	return int(res)
}

func modPow(a, e int64) int64 {
	a %= mod
	var result int64 = 1
	for e > 0 {
		if e&1 == 1 {
			result = result * a % mod
		}
		a = a * a % mod
		e >>= 1
	}
	return result
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
    result = result * b % mod if (e & 1) == 1
    b = b * b % mod
    e >>= 1
  end
  result
end

def count_good_arrays(n, m, k)
  max = n
  fact = Array.new(max + 1, 1)
  (1..max).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact = Array.new(max + 1, 1)
  inv_fact[max] = mod_pow(fact[max], MOD - 2, MOD)
  (max - 1).downto(0) { |i| inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD }

  comb = fact[n - 1] * inv_fact[k] % MOD * inv_fact[n - 1 - k] % MOD
  pow_part = mod_pow(m - 1, n - k - 1, MOD)
  ans = m % MOD * comb % MOD * pow_part % MOD
  ans
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L

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

  def countGoodArrays(n: Int, m: Int, k: Int): Int = {
    val maxN = n
    val fact = new Array[Long](maxN + 1)
    val invFact = new Array[Long](maxN + 1)

    fact(0) = 1L
    var i = 1
    while (i <= maxN) {
      fact(i) = (fact(i - 1) * i) % MOD
      i += 1
    }

    invFact(maxN) = modPow(fact(maxN), MOD - 2)
    i = maxN
    while (i > 0) {
      invFact(i - 1) = (invFact(i) * i) % MOD
      i -= 1
    }

    def comb(a: Int, b: Int): Long = {
      if (b < 0 || b > a) return 0L
      ((fact(a) * invFact(b)) % MOD * invFact(a - b)) % MOD
    }

    val c = comb(n - 1, k)
    val powPart = modPow((m - 1).toLong, (n - k - 1).toLong)
    val ans = ((m.toLong % MOD) * c % MOD) * powPart % MOD
    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_good_arrays(n: i32, m: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
            let mut res: i64 = 1;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = res * base % MOD;
                }
                base = base * base % MOD;
                exp >>= 1;
            }
            res
        }
        fn comb(n: i32, k: i32, fact: &[i64], inv_fact: &[i64]) -> i64 {
            if k < 0 || k > n {
                return 0;
            }
            let n_us = n as usize;
            let k_us = k as usize;
            let res = fact[n_us] * inv_fact[k_us] % MOD * inv_fact[n_us - k_us] % MOD;
            res
        }

        if k < 0 || k > n - 1 {
            return 0;
        }
        let max_n = n as usize;
        let mut fact = vec![0i64; max_n + 1];
        fact[0] = 1;
        for i in 1..=max_n {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact = vec![0i64; max_n + 1];
        inv_fact[max_n] = mod_pow(fact[max_n], MOD - 2);
        for i in (1..=max_n).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }

        let choose = comb(n - 1, k, &fact, &inv_fact);
        let pow_part = if n - k - 1 >= 0 {
            mod_pow((m - 1) as i64, (n - k - 1) as i64)
        } else {
            1
        };
        let ans = ((m as i64 % MOD) * choose % MOD) * pow_part % MOD;
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
        (let ((res (if (odd? e) (modulo (* res b) MOD) res)))
          (loop (modulo (* b b) MOD) (quotient e 2) res)))))

(define (modinv a)
  (pow-mod a (- MOD 2)))

(define/contract (count-good-arrays n m k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((max-n n)
         (fact (make-vector (+ max-n 1) 1))
         (inv-fact (make-vector (+ max-n 1) 1)))
    ;; factorials
    (for ([i (in-range 1 (add1 max-n))])
      (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
    ;; inverse factorials
    (vector-set! inv-fact max-n (modinv (vector-ref fact max-n)))
    (for ([i (in-range (- max-n 1) -1 -1)])
      (vector-set! inv-fact i (modulo (* (vector-ref inv-fact (+ i 1)) (+ i 1)) MOD)))
    ;; combination
    (define (comb a b)
      (if (or (< b 0) (> b a))
          0
          (let* ((num (vector-ref fact a))
                 (den (modulo (* (vector-ref inv-fact b)
                                 (vector-ref inv-fact (- a b))) MOD)))
            (modulo (* num den) MOD))))
    (let* ((comb-val (comb (- n 1) k))
           (exp (- n k 1))
           (pow-val (if (< exp 0) 1 (pow-mod (- m 1) exp)))
           (ans (modulo (* (modulo (* m comb-val) MOD) pow-val) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_good_arrays/3]).

-define(MOD, 1000000007).

count_good_arrays(N, M, K) ->
    Mod = ?MOD,
    Binom = binom(N - 1, K, Mod),
    Pow = pow_mod(M - 1, N - K - 1, Mod),
    Res = ((M rem Mod) * (Binom rem Mod)) rem Mod,
    (Res * Pow) rem Mod.

binom(N, K, Mod) ->
    if
        K < 0 orelse K > N -> 0;
        true ->
            K1 = erlang:min(K, N - K),
            binom_loop(1, K1, 1, N, Mod)
    end.

binom_loop(I, K, Acc, N, Mod) when I =< K ->
    Num = (N - I + 1) rem Mod,
    InvI = pow_mod(I, Mod - 2, Mod),
    NewAcc = (((Acc * Num) rem Mod) * InvI) rem Mod,
    binom_loop(I + 1, K, NewAcc, N, Mod);
binom_loop(_, _, Acc, _, _) -> Acc.

pow_mod(Base, Exp, Mod) ->
    pow_mod(Base rem Mod, Exp, Mod, 1).

pow_mod(_Base, 0, _Mod, Acc) -> Acc;
pow_mod(Base, Exp, Mod, Acc) when (Exp band 1) =:= 1 ->
    NewAcc = (Acc * Base) rem Mod,
    pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod, NewAcc);
pow_mod(Base, Exp, Mod, Acc) ->
    pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  @spec count_good_arrays(n :: integer, m :: integer, k :: integer) :: integer
  def count_good_arrays(n, m, k) do
    cond do
      k > n - 1 -> 0
      true ->
        c = comb(n - 1, k)
        pow_part = pow_mod(m - 1, n - k - 1)
        res = rem(rem(m * c, @mod) * pow_part, @mod)
        res
    end
  end

  defp comb(_n, 0), do: 1
  defp comb(n, k) when k < 0 or k > n, do: 0
  defp comb(n, k) do
    k = min(k, n - k)
    {num, den} =
      Enum.reduce(1..k, {1, 1}, fn i, {num_acc, den_acc} ->
        num_acc = rem(num_acc * (n - k + i), @mod)
        den_acc = rem(den_acc * i, @mod)
        {num_acc, den_acc}
      end)

    inv_den = pow_mod(den, @mod - 2)
    rem(num * inv_den, @mod)
  end

  defp pow_mod(_base, 0), do: 1
  defp pow_mod(base, exp) when exp > 0 do
    pow_mod(rem(base, @mod), exp, 1)
  end

  defp pow_mod(_base, 0, acc), do: acc

  defp pow_mod(base, exp, acc) do
    case rem(exp, 2) do
      1 ->
        acc = rem(acc * base, @mod)
        base = rem(base * base, @mod)
        pow_mod(base, div(exp, 2), acc)

      0 ->
        base = rem(base * base, @mod)
        pow_mod(base, div(exp, 2), acc)
    end
  end
end
```

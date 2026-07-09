# 2338. Count the Number of Ideal Arrays

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1'000'000'007;
    
    long long modpow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    
    int idealArrays(int n, int maxValue) {
        // smallest prime factor sieve
        vector<int> spf(maxValue + 1);
        for (int i = 2; i <= maxValue; ++i) {
            if (!spf[i]) {
                spf[i] = i;
                if ((long long)i * i <= maxValue)
                    for (int j = i * i; j <= maxValue; j += i)
                        if (!spf[j]) spf[j] = i;
            }
        }
        // precompute factorials up to n + 20
        int limit = n + 20;
        vector<long long> fact(limit + 1), invFact(limit + 1);
        fact[0] = 1;
        for (int i = 1; i <= limit; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[limit] = modpow(fact[limit], MOD - 2);
        for (int i = limit; i >= 1; --i) invFact[i - 1] = invFact[i] * i % MOD;
        
        auto C = [&](int N, int K) -> long long {
            if (K < 0 || K > N) return 0;
            return fact[N] * invFact[K] % MOD * invFact[N - K] % MOD;
        };
        
        long long ans = 0;
        for (int v = 1; v <= maxValue; ++v) {
            int x = v;
            long long ways = 1;
            while (x > 1) {
                int p = spf[x];
                if (p == 0) p = x; // when x is prime and spf not set
                int cnt = 0;
                while (x % p == 0) {
                    x /= p;
                    ++cnt;
                }
                ways = ways * C(cnt + n - 1, cnt) % MOD;
            }
            ans += ways;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int idealArrays(int n, int maxValue) {
        // sieve for smallest prime factor
        int[] spf = new int[maxValue + 1];
        for (int i = 2; i <= maxValue; i++) {
            if (spf[i] == 0) {
                for (int j = i; j <= maxValue; j += i) {
                    if (spf[j] == 0) spf[j] = i;
                }
            }
        }

        // maximum exponent of any prime in numbers up to maxValue is at most log2(maxValue)
        int maxExp = 0;
        int temp = maxValue;
        while (temp > 1) {
            maxExp++;
            temp >>= 1;
        }
        int limit = n + maxExp + 5; // safety margin

        long[] fact = new long[limit + 1];
        long[] invFact = new long[limit + 1];
        fact[0] = 1;
        for (int i = 1; i <= limit; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[limit] = modPow(fact[limit], MOD - 2);
        for (int i = limit - 1; i >= 0; i--) {
            invFact[i] = invFact[i + 1] * (i + 1) % MOD;
        }

        long ans = 0;
        for (int x = 1; x <= maxValue; x++) {
            int val = x;
            long ways = 1;
            while (val > 1) {
                int p = spf[val];
                int cnt = 0;
                while (val % p == 0) {
                    val /= p;
                    cnt++;
                }
                ways = ways * nCr(cnt + n - 1, cnt, fact, invFact) % MOD;
            }
            ans += ways;
            if (ans >= MOD) ans -= MOD;
        }
        return (int) ans;
    }

    private long nCr(int N, int K, long[] fact, long[] invFact) {
        if (K < 0 || K > N) return 0;
        return fact[N] * invFact[K] % MOD * invFact[N - K] % MOD;
    }

    private long modPow(long a, long e) {
        long res = 1;
        long base = a % MOD;
        while (e > 0) {
            if ((e & 1) == 1) {
                res = res * base % MOD;
            }
            base = base * base % MOD;
            e >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # smallest prime factor sieve
        m = maxValue
        spf = [0] * (m + 1)
        for i in range(2, m + 1):
            if spf[i] == 0:
                spf[i] = i
                if i * i <= m:
                    step = i
                    start = i * i
                    for j in range(start, m + 1, step):
                        if spf[j] == 0:
                            spf[j] = i

        # factorials up to n + max possible exponent (<=14 for maxValue<=10^4)
        limit = n + 14
        fact = [1] * (limit + 1)
        inv_fact = [1] * (limit + 1)
        for i in range(1, limit + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
        for i in range(limit, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(N, K):
            if K < 0 or K > N:
                return 0
            return fact[N] * inv_fact[K] % MOD * inv_fact[N - K] % MOD

        ans = 0
        for x in range(1, m + 1):
            v = x
            ways = 1
            while v > 1:
                p = spf[v]
                cnt = 0
                while v % p == 0:
                    v //= p
                    cnt += 1
                ways = ways * comb(cnt + n - 1, cnt) % MOD
            ans = (ans + ways) % MOD

        return ans
```

## Python3

```python
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        # smallest prime factor sieve
        spf = list(range(maxValue + 1))
        for i in range(2, int(maxValue ** 0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, maxValue + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        # factorials up to n + max exponent (max exponent <= log2(maxValue) < 15)
        limit = n + 14
        fact = [1] * (limit + 1)
        for i in range(1, limit + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (limit + 1)
        inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
        for i in range(limit, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(N: int, K: int) -> int:
            if K < 0 or K > N:
                return 0
            return fact[N] * inv_fact[K] % MOD * inv_fact[N - K] % MOD

        ans = 0
        for x in range(1, maxValue + 1):
            val = x
            ways = 1
            while val > 1:
                p = spf[val]
                cnt = 0
                while val % p == 0:
                    val //= p
                    cnt += 1
                # distribute cnt identical prime factors among n positions
                ways = ways * comb(cnt + n - 1, cnt) % MOD
            ans = (ans + ways) % MOD

        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007LL

static long long modPow(long long a, long long e) {
    long long res = 1;
    while (e) {
        if (e & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return res;
}

int idealArrays(int n, int maxValue) {
    // smallest prime factor sieve
    int *spf = (int *)calloc(maxValue + 1, sizeof(int));
    for (int i = 2; i <= maxValue; ++i) {
        if (!spf[i]) {
            for (int j = i; j <= maxValue; j += i)
                if (!spf[j]) spf[j] = i;
        }
    }

    // factorials up to n + max possible exponent (<= 20 is safe)
    int limit = n + 20;
    long long *fact = (long long *)malloc((limit + 1) * sizeof(long long));
    long long *invFact = (long long *)malloc((limit + 1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= limit; ++i)
        fact[i] = fact[i - 1] * i % MOD;
    invFact[limit] = modPow(fact[limit], MOD - 2);
    for (int i = limit; i > 0; --i)
        invFact[i - 1] = invFact[i] * i % MOD;

    long long ans = 0;
    for (int x = 1; x <= maxValue; ++x) {
        int t = x;
        long long ways = 1;
        while (t > 1) {
            int p = spf[t];
            int cnt = 0;
            while (t % p == 0) {
                t /= p;
                ++cnt;
            }
            int N = cnt + n - 1;
            int K = cnt;
            long long comb = fact[N] * invFact[K] % MOD * invFact[N - K] % MOD;
            ways = ways * comb % MOD;
        }
        ans += ways;
        if (ans >= MOD) ans -= MOD;
    }

    free(spf);
    free(fact);
    free(invFact);
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1_000_000_007;
    
    public int IdealArrays(int n, int maxValue) {
        // smallest prime factor sieve
        int[] spf = new int[maxValue + 1];
        for (int i = 2; i <= maxValue; ++i) {
            if (spf[i] == 0) {
                for (int j = i; j <= maxValue; j += i) {
                    if (spf[j] == 0) spf[j] = i;
                }
            }
        }

        // precompute factorials up to n + maxExponent
        int limit = n + 20; // enough for all exponents (max exponent <= log2(maxValue) < 15)
        long[] fact = new long[limit + 1];
        long[] invFact = new long[limit + 1];
        fact[0] = 1;
        for (int i = 1; i <= limit; ++i) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[limit] = ModPow(fact[limit], MOD - 2);
        for (int i = limit; i >= 1; --i) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }

        long result = 0;
        for (int x = 1; x <= maxValue; ++x) {
            int temp = x;
            long ways = 1;
            while (temp > 1) {
                int p = spf[temp];
                int cnt = 0;
                while (temp % p == 0) {
                    temp /= p;
                    cnt++;
                }
                ways = ways * Comb(cnt + n - 1, cnt, fact, invFact) % MOD;
            }
            result += ways;
            if (result >= MOD) result -= MOD;
        }

        return (int)result;
    }

    private static long Comb(int a, int b, long[] fact, long[] invFact) {
        if (b < 0 || b > a) return 0;
        return fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
    }

    private static long ModPow(long baseVal, long exp) {
        long res = 1;
        long cur = baseVal % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = res * cur % MOD;
            }
            cur = cur * cur % MOD;
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
 * @param {number} maxValue
 * @return {number}
 */
var idealArrays = function(n, maxValue) {
    const MOD = 1000000007n;
    // maximum exponent for numbers up to 1e4 is less than 20
    const LIMIT = n + 30;   // safe upper bound for factorials

    // precompute factorials and inverse factorials modulo MOD
    const fact = new Array(LIMIT + 1);
    const invFact = new Array(LIMIT + 1);
    fact[0] = 1n;
    for (let i = 1; i <= LIMIT; ++i) {
        fact[i] = fact[i - 1] * BigInt(i) % MOD;
    }
    const modPow = (base, exp) => {
        let b = base % MOD;
        let e = exp;
        let res = 1n;
        while (e > 0n) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    };
    invFact[LIMIT] = modPow(fact[LIMIT], MOD - 2n);
    for (let i = LIMIT; i >= 1; --i) {
        invFact[i - 1] = invFact[i] * BigInt(i) % MOD;
    }
    const comb = (a, b) => {
        if (b < 0 || b > a) return 0n;
        return fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
    };

    // smallest prime factor sieve up to maxValue
    const spf = new Uint32Array(maxValue + 1);
    for (let i = 2; i <= maxValue; ++i) {
        if (spf[i] === 0) {
            for (let j = i; j <= maxValue; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }

    let ans = 0n;
    for (let x = 1; x <= maxValue; ++x) {
        let temp = x;
        let ways = 1n;
        while (temp > 1) {
            const p = spf[temp];
            let cnt = 0;
            while (temp % p === 0) {
                temp = Math.trunc(temp / p);
                ++cnt;
            }
            ways = ways * comb(cnt + n - 1, cnt) % MOD;
        }
        ans = (ans + ways) % MOD;
    }

    return Number(ans);
};
```

## Typescript

```typescript
function idealArrays(n: number, maxValue: number): number {
    const MOD = 1000000007n;

    // Sieve for smallest prime factor
    const spf = new Uint32Array(maxValue + 1);
    for (let i = 2; i <= maxValue; i++) {
        if (spf[i] === 0) {
            for (let j = i; j <= maxValue; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }
    spf[1] = 1;

    // Precompute factorials up to n + 20 (enough for all exponents)
    const limit = n + 20;
    const fact: bigint[] = new Array(limit + 1);
    const invFact: bigint[] = new Array(limit + 1);
    fact[0] = 1n;
    for (let i = 1; i <= limit; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    // fast exponentiation
    function modPow(base: bigint, exp: bigint): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if ((e & 1n) === 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }

    invFact[limit] = modPow(fact[limit], MOD - 2n);
    for (let i = limit; i > 0; i--) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    function comb(N: number, K: number): bigint {
        if (K < 0 || K > N) return 0n;
        return (((fact[N] * invFact[K]) % MOD) * invFact[N - K]) % MOD;
    }

    let ans = 0n;

    for (let x = 1; x <= maxValue; x++) {
        let temp = x;
        let ways = 1n;
        while (temp > 1) {
            const p = spf[temp];
            let cnt = 0;
            while (temp % p === 0) {
                temp = Math.floor(temp / p);
                cnt++;
            }
            // multiply by C(cnt + n - 1, cnt)
            ways = (ways * comb(cnt + n - 1, cnt)) % MOD;
        }
        ans = (ans + ways) % MOD;
    }

    return Number(ans);
}
```

## Php

```php
class Solution {
    private $MOD = 1000000007;
    private $fact = [];
    private $invFact = [];

    /**
     * @param Integer $n
     * @param Integer $maxValue
     * @return Integer
     */
    function idealArrays($n, $maxValue) {
        $mod = $this->MOD;

        // smallest prime factor sieve
        $spf = array_fill(0, $maxValue + 1, 0);
        for ($i = 2; $i * $i <= $maxValue; $i++) {
            if ($spf[$i] == 0) {
                for ($j = $i * $i; $j <= $maxValue; $j += $i) {
                    if ($spf[$j] == 0) $spf[$j] = $i;
                }
            }
        }
        for ($i = 2; $i <= $maxValue; $i++) {
            if ($spf[$i] == 0) $spf[$i] = $i;
        }

        // factorials up to n + max exponent (safe margin)
        $limit = $n + 30;
        $this->fact = array_fill(0, $limit + 1, 0);
        $this->invFact = array_fill(0, $limit + 1, 0);
        $this->fact[0] = 1;
        for ($i = 1; $i <= $limit; $i++) {
            $this->fact[$i] = ($this->fact[$i - 1] * $i) % $mod;
        }
        $this->invFact[$limit] = $this->modPow($this->fact[$limit], $mod - 2);
        for ($i = $limit; $i >= 1; $i--) {
            $this->invFact[$i - 1] = ($this->invFact[$i] * $i) % $mod;
        }

        $ans = 0;
        for ($x = 1; $x <= $maxValue; $x++) {
            $temp = $x;
            $ways = 1;
            while ($temp > 1) {
                $p = $spf[$temp];
                $cnt = 0;
                while ($temp % $p == 0) {
                    $temp = intdiv($temp, $p);
                    $cnt++;
                }
                // multiply by C(cnt + n - 1, cnt)
                $ways = ($ways * $this->comb($cnt + $n - 1, $cnt)) % $mod;
            }
            $ans = ($ans + $ways) % $mod;
        }

        return $ans;
    }

    private function comb($N, $K) {
        if ($K < 0 || $K > $N) return 0;
        $mod = $this->MOD;
        return ((($this->fact[$N] * $this->invFact[$K]) % $mod) * $this->invFact[$N - $K]) % $mod;
    }

    private function modPow($a, $e) {
        $mod = $this->MOD;
        $res = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) $res = ($res * $a) % $mod;
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
    let MOD = 1_000_000_007

    func idealArrays(_ n: Int, _ maxValue: Int) -> Int {
        // smallest prime factor sieve
        var spf = [Int](repeating: 0, count: maxValue + 1)
        if maxValue >= 2 {
            for i in 2...maxValue {
                if spf[i] == 0 {
                    var j = i
                    while j <= maxValue {
                        if spf[j] == 0 { spf[j] = i }
                        j += i
                    }
                }
            }
        }

        // factorials up to n + 20 (enough for all needed combinations)
        let limit = n + 20
        var fac = [Int](repeating: 1, count: limit + 1)
        for i in 1...limit {
            fac[i] = Int((Int64(fac[i - 1]) * Int64(i)) % Int64(MOD))
        }

        func modPow(_ base: Int, _ exp: Int) -> Int {
            var result = 1
            var b = base % MOD
            var e = exp
            while e > 0 {
                if (e & 1) == 1 {
                    result = Int((Int64(result) * Int64(b)) % Int64(MOD))
                }
                b = Int((Int64(b) * Int64(b)) % Int64(MOD))
                e >>= 1
            }
            return result
        }

        var invFac = [Int](repeating: 1, count: limit + 1)
        invFac[limit] = modPow(fac[limit], MOD - 2)
        if limit > 0 {
            for i in stride(from: limit - 1, through: 0, by: -1) {
                invFac[i] = Int((Int64(invFac[i + 1]) * Int64(i + 1)) % Int64(MOD))
            }
        }

        func comb(_ k: Int, _ n: Int) -> Int { // C(n, k)
            if k < 0 || k > n { return 0 }
            let res = Int(
                (Int64(fac[n]) * Int64(invFac[k]) % Int64(MOD)) *
                Int64(invFac[n - k]) % Int64(MOD)
            )
            return res
        }

        var answer = 0
        for x in 1...maxValue {
            var temp = x
            var ways = 1
            while temp > 1 {
                let p = spf[temp]
                var cnt = 0
                while temp % p == 0 {
                    cnt += 1
                    temp /= p
                }
                // multiply by C(cnt + n - 1, cnt)
                let c = comb(cnt, cnt + n - 1)
                ways = Int((Int64(ways) * Int64(c)) % Int64(MOD))
            }
            answer += ways
            if answer >= MOD { answer -= MOD }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun idealArrays(n: Int, maxValue: Int): Int {
        val MOD = 1_000_000_007L
        // maximum exponent of any prime in numbers up to maxValue (2^13=8192 <10000<2^14)
        val limit = n + 20
        val fact = LongArray(limit + 1)
        val invFact = LongArray(limit + 1)
        fact[0] = 1L
        for (i in 1..limit) {
            fact[i] = fact[i - 1] * i % MOD
        }
        fun modPow(a: Long, e: Long): Long {
            var base = a % MOD
            var exp = e
            var res = 1L
            while (exp > 0) {
                if ((exp and 1L) == 1L) res = res * base % MOD
                base = base * base % MOD
                exp = exp shr 1
            }
            return res
        }
        invFact[limit] = modPow(fact[limit], MOD - 2)
        for (i in limit downTo 1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }
        fun comb(N: Int, K: Int): Long {
            if (K < 0 || K > N) return 0L
            return fact[N] * invFact[K] % MOD * invFact[N - K] % MOD
        }

        // smallest prime factor sieve
        val spf = IntArray(maxValue + 1)
        for (i in 2..maxValue) {
            if (spf[i] == 0) {
                var j = i
                while (j <= maxValue) {
                    if (spf[j] == 0) spf[j] = i
                    j += i
                }
            }
        }

        var ans = 0L
        for (x in 1..maxValue) {
            var v = x
            var ways = 1L
            while (v > 1) {
                val p = spf[v]
                var cnt = 0
                while (v % p == 0) {
                    v /= p
                    cnt++
                }
                ways = ways * comb(cnt + n - 1, cnt) % MOD
            }
            ans += ways
            if (ans >= MOD) ans -= MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int idealArrays(int n, int maxValue) {
    // Smallest prime factor sieve
    List<int> spf = List.filled(maxValue + 1, 0);
    for (int i = 2; i <= maxValue; ++i) {
      if (spf[i] == 0) {
        spf[i] = i;
        if (i * i <= maxValue) {
          for (int j = i * i; j <= maxValue; j += i) {
            if (spf[j] == 0) spf[j] = i;
          }
        }
      }
    }

    // Precompute factorials up to n + 20 (enough for all needed combinations)
    int limit = n + 20;
    List<int> fact = List.filled(limit + 1, 1);
    for (int i = 1; i <= limit; ++i) {
      fact[i] = (fact[i - 1] * i) % _MOD;
    }
    List<int> invFact = List.filled(limit + 1, 1);
    invFact[limit] = _modPow(fact[limit], _MOD - 2);
    for (int i = limit - 1; i >= 0; --i) {
      invFact[i] = (invFact[i + 1] * (i + 1)) % _MOD;
    }

    int answer = 0;
    for (int v = 1; v <= maxValue; ++v) {
      int x = v;
      int ways = 1;
      while (x > 1) {
        int p = spf[x];
        int cnt = 0;
        while (x % p == 0) {
          x ~/= p;
          cnt++;
        }
        // C(cnt + n - 1, cnt)
        int comb = fact[cnt + n - 1];
        comb = (comb * invFact[cnt]) % _MOD;
        comb = (comb * invFact[n - 1]) % _MOD;
        ways = (ways * comb) % _MOD;
      }
      answer += ways;
      if (answer >= _MOD) answer -= _MOD;
    }

    return answer;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _MOD;
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

import (
	"math"
)

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

func idealArrays(n int, maxValue int) int {
	// smallest prime factor sieve
	spf := make([]int, maxValue+1)
	for i := 2; i <= maxValue; i++ {
		if spf[i] == 0 {
			for j := i; j <= maxValue; j += i {
				if spf[j] == 0 {
					spf[j] = i
				}
			}
		}
	}

	// factorials up to n + max exponent (max exponent for 10000 is < 14)
	limit := n + 20
	fact := make([]int64, limit+1)
	invFact := make([]int64, limit+1)
	fact[0] = 1
	for i := 1; i <= limit; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[limit] = modPow(fact[limit], MOD-2)
	for i := limit; i >= 1; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}

	comb := func(a, b int) int64 {
		if b < 0 || b > a {
			return 0
		}
		return fact[a] * invFact[b] % MOD * invFact[a-b] % MOD
	}

	var ans int64 = 0
	for x := 1; x <= maxValue; x++ {
		t := x
		ways := int64(1)
		for t > 1 {
			p := spf[t]
			if p == 0 { // t is prime
				p = t
			}
			cnt := 0
			for t%p == 0 {
				t /= p
				cnt++
			}
			ways = ways * comb(cnt+n-1, cnt) % MOD
		}
		ans = (ans + ways) % MOD
	}
	return int(ans)
}

// The following main function is only for local testing and will be ignored on LeetCode.
func main() {
	// Example tests
	println(idealArrays(2, 5)) // Expected: 10
	println(idealArrays(5, 3)) // Expected: 11

	// Additional test to ensure performance within constraints
	n := 10000
	maxV := 10000
	println(int(math.Log10(float64(idealArrays(n, maxV)))))
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e)
  res = 1
  base = a % MOD
  while e > 0
    res = res * base % MOD if (e & 1) == 1
    base = base * base % MOD
    e >>= 1
  end
  res
end

def comb(a, b, fact, inv_fact)
  return 0 if b < 0 || b > a
  fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
end

# @param {Integer} n
# @param {Integer} max_value
# @return {Integer}
def ideal_arrays(n, max_value)
  # smallest prime factor sieve
  spf = Array.new(max_value + 1) { |i| i }
  limit_i = Math.sqrt(max_value).to_i
  (2..limit_i).each do |i|
    if spf[i] == i
      (i * i).step(max_value, i) do |j|
        spf[j] = i if spf[j] == j
      end
    end
  end

  # factorials up to n + max possible exponent (13 for max_value <= 1e4)
  limit = n + 14
  fact = Array.new(limit + 1, 0)
  inv_fact = Array.new(limit + 1, 0)
  fact[0] = 1
  (1..limit).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact[limit] = mod_pow(fact[limit], MOD - 2)
  limit.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % MOD }

  ans = 0
  (1..max_value).each do |x|
    temp = x
    ways = 1
    while temp > 1
      p = spf[temp]
      cnt = 0
      while (temp % p).zero?
        temp /= p
        cnt += 1
      end
      ways = ways * comb(cnt + n - 1, cnt, fact, inv_fact) % MOD
    end
    ans += ways
    ans -= MOD if ans >= MOD
  end
  ans
end
```

## Scala

```scala
object Solution {
  def idealArrays(n: Int, maxValue: Int): Int = {
    val MOD = 1000000007L

    // Smallest prime factor sieve
    val spf = new Array[Int](maxValue + 1)
    var i = 2
    while (i <= maxValue) {
      if (spf(i) == 0) {
        var j = i
        while (j <= maxValue) {
          if (spf(j) == 0) spf(j) = i
          j += i
        }
      }
      i += 1
    }

    // factorials up to n + max exponent (max exponent for 10000 is <14)
    val limit = n + 14
    val fact = new Array[Long](limit + 1)
    val invFact = new Array[Long](limit + 1)
    fact(0) = 1L
    var idx = 1
    while (idx <= limit) {
      fact(idx) = fact(idx - 1) * idx % MOD
      idx += 1
    }

    def modPow(a: Long, e: Long): Long = {
      var base = a % MOD
      var exp = e
      var res = 1L
      while (exp > 0) {
        if ((exp & 1L) == 1L) res = res * base % MOD
        base = base * base % MOD
        exp >>= 1
      }
      res
    }

    invFact(limit) = modPow(fact(limit), MOD - 2)
    idx = limit - 1
    while (idx >= 0) {
      invFact(idx) = invFact(idx + 1) * (idx + 1) % MOD
      idx -= 1
    }

    def comb(nn: Int, kk: Int): Long = {
      if (kk < 0 || kk > nn) 0L
      else fact(nn) * invFact(kk) % MOD * invFact(nn - kk) % MOD
    }

    var ans = 0L
    var x = 1
    while (x <= maxValue) {
      var v = x
      var ways = 1L
      while (v > 1) {
        val p = spf(v)
        var cnt = 0
        while (v % p == 0) {
          cnt += 1
          v /= p
        }
        ways = ways * comb(cnt + n - 1, cnt) % MOD
      }
      ans = (ans + ways) % MOD
      x += 1
    }

    ans.toInt
  }
}
```

## Rust

```rust
use std::cmp::min;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut a: i64, mut e: i64) -> i64 {
    let mut res = 1i64;
    while e > 0 {
        if e & 1 == 1 {
            res = res * a % MOD;
        }
        a = a * a % MOD;
        e >>= 1;
    }
    res
}

impl Solution {
    pub fn ideal_arrays(n: i32, max_value: i32) -> i32 {
        let n_usize = n as usize;
        let max_v = max_value as usize;

        // smallest prime factor sieve
        let mut spf = vec![0usize; max_v + 1];
        for i in 2..=max_v {
            if spf[i] == 0 {
                spf[i] = i;
                let mut j = i * i;
                while j <= max_v {
                    if spf[j] == 0 {
                        spf[j] = i;
                    }
                    j += i;
                }
            }
        }
        // for 1, keep spf[1]=1 (unused)
        spf[1] = 1;

        // maximum exponent of any prime in numbers up to max_v
        let mut max_exp = 0usize;
        let mut temp = max_v;
        while temp > 1 {
            let p = spf[temp];
            let mut cnt = 0usize;
            while temp % p == 0 {
                temp /= p;
                cnt += 1;
            }
            max_exp = max_exp.max(cnt);
        }

        // precompute factorials up to n + max_exp
        let limit = n_usize + max_exp + 5; // safety margin
        let mut fact = vec![1i64; limit + 1];
        for i in 1..=limit {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact = vec![1i64; limit + 1];
        inv_fact[limit] = mod_pow(fact[limit], MOD - 2);
        for i in (0..limit).rev() {
            inv_fact[i] = inv_fact[i + 1] * ((i + 1) as i64) % MOD;
        }

        let comb = |nn: usize, kk: usize, fact: &Vec<i64>, inv_fact: &Vec<i64>| -> i64 {
            if kk > nn { return 0; }
            fact[nn] * inv_fact[kk] % MOD * inv_fact[nn - kk] % MOD
        };

        let mut answer = 0i64;
        for mut x in 1..=max_v {
            let mut ways = 1i64;
            while x > 1 {
                let p = spf[x];
                let mut cnt = 0usize;
                while x % p == 0 {
                    x /= p;
                    cnt += 1;
                }
                // multiply by C(cnt + n - 1, cnt)
                ways = ways * comb(cnt + n_usize - 1, cnt, &fact, &inv_fact) % MOD;
            }
            answer += ways;
            if answer >= MOD {
                answer -= MOD;
            }
        }

        answer as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (modpow base exp mod)
  (let loop ((b (modulo base mod)) (e exp) (res 1))
    (if (= e 0)
        res
        (let* ((res2 (if (odd? e) (modulo (* res b) mod) res))
               (b2   (modulo (* b b) mod)))
          (loop b2 (quotient e 2) res2)))))

(define/contract (ideal-arrays n maxValue)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((limit (+ n 20))
         (fact   (make-vector (+ limit 1) 0))
         (invFact (make-vector (+ limit 1) 0)))
    ;; factorials
    (vector-set! fact 0 1)
    (for ([i (in-range 1 (add1 limit))])
      (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
    ;; inverse factorials
    (vector-set! invFact limit (modpow (vector-ref fact limit) (- MOD 2) MOD))
    (for ([i (in-range (- limit 1) -1 -1)])
      (vector-set! invFact i (modulo (* (vector-ref invFact (+ i 1)) (+ i 1)) MOD)))
    ;; combination
    (define (comb a b)
      (if (or (< b 0) (> b a))
          0
          (let ((fa (vector-ref fact a))
                (fb (vector-ref invFact b))
                (fc (vector-ref invFact (- a b))))
            (modulo (* (* fa fb) fc) MOD))))
    ;; smallest prime factor sieve
    (define spf (make-vector (+ maxValue 1) 0))
    (for ([i (in-range 2 (add1 maxValue))])
      (when (= (vector-ref spf i) 0)
        (for ([j (in-range i (add1 maxValue) i)])
          (when (= (vector-ref spf j) 0)
            (vector-set! spf j i)))))
    ;; factor exponents of a number
    (define (factor-exponents x)
      (let recur ((v x) (acc '()))
        (if (= v 1)
            acc
            (let* ((p (vector-ref spf v))
                   (cnt 0)
                   (temp v))
              (let inner ((t temp) (c 0))
                (if (zero? (remainder t p))
                    (inner (/ t p) (+ c 1))
                    (begin
                      (set! cnt c)
                      (set! temp t))))
              (recur temp (cons cnt acc))))))
    ;; sum over all possible last values
    (let ((total 0))
      (for ([v (in-range 1 (add1 maxValue))])
        (let ((exps (factor-exponents v))
              (ways 1))
          (for ([e exps])
            (set! ways (modulo (* ways (comb (+ e n -1) e)) MOD)))
          (set! total (modulo (+ total ways) MOD))))
      total)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec ideal_arrays(integer(), integer()) -> integer().
ideal_arrays(N, MaxValue) ->
    Limit = N + 14,
    Fact = build_fact(Limit),
    InvFact = build_inv_fact(Fact, Limit),
    sum_ways(1, MaxValue, N, Fact, InvFact, 0).

build_fact(Limit) ->
    build_fact(0, Limit, array:new(Limit+1, {default,0})).

build_fact(I, Limit, Arr) when I =< Limit ->
    case I of
        0 ->
            NewArr = array:set(0, 1, Arr),
            build_fact(1, Limit, NewArr);
        _ ->
            Prev = array:get(I-1, Arr),
            Val = (Prev * I) rem ?MOD,
            NewArr = array:set(I, Val, Arr),
            if I == Limit -> NewArr; true -> build_fact(I+1, Limit, NewArr) end
    end.

build_inv_fact(FactArr, Limit) ->
    InvLast = pow_mod(array:get(Limit, FactArr), ?MOD-2),
    build_inv_desc(Limit, array:new(Limit+1,{default,0}), InvLast).

build_inv_desc(I, InvArr, CurrInv) when I >= 0 ->
    NewInvArr = array:set(I, CurrInv, InvArr),
    if I == 0 -> NewInvArr;
       true ->
           PrevInv = (CurrInv * I) rem ?MOD,
           build_inv_desc(I-1, NewInvArr, PrevInv)
    end.

comb(A,B,Fact,InvFact) when B < 0; B > A -> 0;
comb(A,B,Fact,InvFact) ->
    Fa = array:get(A, Fact),
    Fb = array:get(B, InvFact),
    Fab = array:get(A-B, InvFact),
    ((Fa * Fb) rem ?MOD * Fab) rem ?MOD.

sum_ways(Cur, MaxV, N, Fact, InvFact, Acc) when Cur > MaxV ->
    Acc;
sum_ways(Cur, MaxV, N, Fact, InvFact, Acc) ->
    Ways = ways_for_x(Cur, N, Fact, InvFact),
    NewAcc = (Acc + Ways) rem ?MOD,
    sum_ways(Cur+1, MaxV, N, Fact, InvFact, NewAcc).

ways_for_x(X, N, Fact, InvFact) ->
    Exps = factor_exponents(X),
    lists:foldl(fun(A, Prod) ->
        Comb = comb(A + N - 1, A, Fact, InvFact),
        (Prod * Comb) rem ?MOD
    end, 1, Exps).

factor_exponents(Num) -> factor_exponents(Num, 2, []).

factor_exponents(1, _I, Acc) ->
    lists:reverse(Acc);
factor_exponents(N, I, Acc) when I*I =< N ->
    case N rem I of
        0 ->
            {Cnt, Rest} = count_power(N, I, 0),
            factor_exponents(Rest, I+1, [Cnt|Acc]);
        _ ->
            factor_exponents(N, I+1, Acc)
    end;
factor_exponents(N, _I, Acc) when N > 1 ->
    lists:reverse([1|Acc]).

count_power(N, I, Cnt) when N rem I =:= 0 ->
    count_power(N div I, I, Cnt+1);
count_power(N, _I, Cnt) ->
    {Cnt, N}.

pow_mod(Base, Exp) -> pow_mod(Base rem ?MOD, Exp, 1).

pow_mod(_Base, 0, Acc) -> Acc;
pow_mod(Base, Exp, Acc) when (Exp band 1) =:= 1 ->
    NewAcc = (Acc * Base) rem ?MOD,
    pow_mod((Base*Base) rem ?MOD, Exp bsr 1, NewAcc);
pow_mod(Base, Exp, Acc) ->
    pow_mod((Base*Base) rem ?MOD, Exp bsr 1, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007
  import Bitwise

  @spec ideal_arrays(n :: integer, max_value :: integer) :: integer
  def ideal_arrays(n, max_value) do
    primes = gen_primes(max_value)

    Enum.reduce(1..max_value, 0, fn v, acc ->
      ways = count_ways(v, n, primes)
      rem(acc + ways, @mod)
    end)
  end

  # Count number of ideal arrays ending with value v
  defp count_ways(v, n, primes) do
    {rem_val, ways} = factor(v, n, primes)

    if rem_val > 1 do
      rem(ways * comb_small(1, n, @mod), @mod)
    else
      ways
    end
  end

  # Factorize v using the list of primes, accumulating combination product
  defp factor(value, n, primes) do
    Enum.reduce_while(primes, {value, 1}, fn p, {t, w} ->
      if p * p > t do
        {:halt, {t, w}}
      else
        {cnt, new_t} = extract_factor(t, p)

        if cnt > 0 do
          new_w = rem(w * comb_small(cnt, n, @mod), @mod)
          {:cont, {new_t, new_w}}
        else
          {:cont, {t, w}}
        end
      end
    end)
  end

  # Extract exponent of prime p from t, returning {count, remaining}
  defp extract_factor(t, p) do
    extract_factor(t, p, 0)
  end

  defp extract_factor(t, p, c) do
    if rem(t, p) == 0 do
      extract_factor(div(t, p), p, c + 1)
    else
      {c, t}
    end
  end

  # Combination C(n + k - 1, k) where k is small (exponent)
  defp comb_small(0, _n, _mod), do: 1

  defp comb_small(k, n, mod) do
    num =
      Enum.reduce(0..(k - 1), 1, fn i, acc ->
        rem(acc * (n + i), mod)
      end)

    denom =
      Enum.reduce(2..k, 1, fn i, acc ->
        rem(acc * i, mod)
      end)

    inv = mod_pow(denom, mod - 2, mod)
    rem(num * inv, mod)
  end

  # Fast modular exponentiation
  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) when (exp &&& 1) == 1 do
    half = mod_pow(rem(base * base, mod), div(exp, 2), mod)
    rem(half * base, mod)
  end

  defp mod_pow(base, exp, mod) do
    mod_pow(rem(base * base, mod), div(exp, 2), mod)
  end

  # Generate list of primes up to limit using incremental trial division
  defp gen_primes(limit) when limit < 2, do: []

  defp gen_primes(limit) do
    Enum.reduce(2..limit, [], fn i, primes ->
      if is_prime(i, primes), do: [i | primes], else: primes
    end)
    |> Enum.reverse()
  end

  defp is_prime(num, primes) do
    max = :math.sqrt(num) |> trunc()

    Enum.all?(primes, fn p ->
      p > max or rem(num, p) != 0
    end)
  end
end
```

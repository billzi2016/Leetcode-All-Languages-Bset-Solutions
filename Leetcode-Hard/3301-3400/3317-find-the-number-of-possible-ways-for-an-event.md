# 3317. Find the Number of Possible Ways for an Event

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    
    long long modPow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    
    int numberOfWays(int n, int x, int y) {
        int maxN = max(n, x);
        vector<long long> fact(maxN + 1), invFact(maxN + 1);
        fact[0] = 1;
        for (int i = 1; i <= maxN; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxN] = modPow(fact[maxN], MOD - 2);
        for (int i = maxN; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;
        
        // Stirling numbers of the second kind S[n][k]
        vector<vector<long long>> S(n + 1, vector<long long>(n + 1, 0));
        S[0][0] = 1;
        for (int i = 1; i <= n; ++i) {
            for (int k = 1; k <= i; ++k) {
                S[i][k] = (S[i - 1][k - 1] + S[i - 1][k] * k) % MOD;
            }
        }
        
        long long ans = 0;
        int limit = min(n, x);
        vector<long long> powY(limit + 1, 1);
        for (int i = 1; i <= limit; ++i) powY[i] = powY[i - 1] * y % MOD;
        
        for (int k = 1; k <= limit; ++k) {
            long long perm = fact[x] * invFact[x - k] % MOD; // P(x,k)
            long long term = perm * S[n][k] % MOD * powY[k] % MOD;
            ans += term;
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

    public int numberOfWays(int n, int x, int y) {
        int max = Math.max(n, x);
        long[] fact = new long[max + 1];
        long[] invFact = new long[max + 1];
        fact[0] = 1;
        for (int i = 1; i <= max; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[max] = modPow(fact[max], MOD - 2);
        for (int i = max - 1; i >= 0; i--) {
            invFact[i] = invFact[i + 1] * (i + 1) % MOD;
        }

        long[][] stirling = new long[n + 1][n + 1];
        stirling[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                stirling[i][j] = (stirling[i - 1][j - 1] + j * stirling[i - 1][j]) % MOD;
            }
        }

        long ans = 0;
        long powY = 1; // y^k
        int limit = Math.min(x, n);
        for (int k = 0; k <= limit; k++) {
            if (k > 0) {
                powY = powY * y % MOD;
            }
            if (stirling[n][k] == 0) continue;
            long perm = fact[x] * invFact[x - k] % MOD; // P(x, k)
            long term = perm * stirling[n][k] % MOD;
            term = term * powY % MOD;
            ans += term;
            if (ans >= MOD) ans -= MOD;
        }
        return (int) ans;
    }

    private long modPow(long base, long exp) {
        long res = 1;
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
    def numberOfWays(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: int
        """
        MOD = 10**9 + 7
        maxN = max(n, x)
        # factorials and inverse factorials
        fact = [1] * (maxN + 1)
        for i in range(1, maxN + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1] * (maxN + 1)
        inv_fact[maxN] = pow(fact[maxN], MOD - 2, MOD)
        for i in range(maxN, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD

        # Stirling numbers of the second kind S[n][k] for k<=x
        S = [[0] * (x + 1) for _ in range(n + 1)]
        S[0][0] = 1
        for i in range(1, n + 1):
            upper = min(i, x)
            for k in range(1, upper + 1):
                S[i][k] = (S[i-1][k-1] + k * S[i-1][k]) % MOD

        # precompute powers of y
        pow_y = [1] * (x + 1)
        for i in range(1, x + 1):
            pow_y[i] = pow_y[i-1] * y % MOD

        ans = 0
        limit = min(n, x)
        for k in range(1, limit + 1):
            # P(x,k) = x! / (x-k)!
            perm = fact[x] * inv_fact[x - k] % MOD
            term = perm * S[n][k] % MOD
            term = term * pow_y[k] % MOD
            ans = (ans + term) % MOD
        return ans
```

## Python3

```python
class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 10**9 + 7
        max_val = max(n, x)
        fact = [1] * (max_val + 1)
        for i in range(1, max_val + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1] * (max_val + 1)
        inv_fact[max_val] = pow(fact[max_val], MOD - 2, MOD)
        for i in range(max_val, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD

        # Stirling numbers of the second kind S[n][k]
        S = [[0] * (n + 1) for _ in range(n + 1)]
        S[0][0] = 1
        for i in range(1, n + 1):
            for k in range(1, i + 1):
                S[i][k] = (S[i-1][k-1] + k * S[i-1][k]) % MOD

        limit = min(n, x)
        ans = 0
        pow_y = [1] * (limit + 1)
        for i in range(1, limit + 1):
            pow_y[i] = pow_y[i-1] * y % MOD

        for m in range(1, limit + 1):
            # permutations P(x,m) = x! / (x-m)!
            perm = fact[x] * inv_fact[x - m] % MOD
            term = perm * S[n][m] % MOD
            term = term * pow_y[m] % MOD
            ans = (ans + term) % MOD

        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

long long modPow(long long a, long long e) {
    long long r = 1;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

int numberOfWays(int n, int x, int y) {
    int maxN = max(n, x);
    vector<long long> fact(maxN + 1), invFact(maxN + 1);
    fact[0] = 1;
    for (int i = 1; i <= maxN; ++i) fact[i] = fact[i - 1] * i % MOD;
    invFact[maxN] = modPow(fact[maxN], MOD - 2);
    for (int i = maxN; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;

    // Stirling numbers of the second kind S[n][k]
    vector<vector<int>> S(n + 1, vector<int>(n + 1, 0));
    S[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int k = 1; k <= i; ++k) {
            long long val = S[i - 1][k - 1];
            val += 1LL * k * S[i - 1][k] % MOD;
            if (val >= MOD) val -= MOD;
            S[i][k] = (int)val;
        }
    }

    long long ans = 0;
    int limit = min(n, x);
    vector<long long> powY(limit + 1, 1);
    for (int i = 1; i <= limit; ++i) powY[i] = powY[i - 1] * y % MOD;

    for (int k = 0; k <= limit; ++k) {
        if (S[n][k] == 0) continue;
        long long comb = fact[x] * invFact[k] % MOD * invFact[x - k] % MOD;
        long long term = comb;
        term = term * fact[k] % MOD;          // k!
        term = term * S[n][k] % MOD;
        term = term * powY[k] % MOD;
        ans += term;
        if (ans >= MOD) ans -= MOD;
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    const int MOD = 1000000007;
    public int NumberOfWays(int n, int x, int y) {
        int maxN = Math.Max(Math.Max(n, x), y);
        long[] fact = new long[maxN + 1];
        long[] invFact = new long[maxN + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxN; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxN] = ModPow(fact[maxN], MOD - 2);
        for (int i = maxN; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;

        long[,] stirling = new long[n + 1, n + 1];
        stirling[0, 0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                stirling[i, j] = (stirling[i - 1, j - 1] + j * stirling[i - 1, j]) % MOD;
            }
        }

        int limit = Math.Min(n, x);
        long[] powY = new long[limit + 2];
        powY[0] = 1;
        for (int i = 1; i < powY.Length; i++) {
            powY[i] = powY[i - 1] * y % MOD;
        }

        long ans = 0;
        for (int k = 1; k <= limit; k++) {
            long comb = fact[x] * invFact[k] % MOD * invFact[x - k] % MOD;
            long term = comb * stirling[n, k] % MOD;
            term = term * fact[k] % MOD;
            term = term * powY[k] % MOD;
            ans += term;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }

    private long ModPow(long a, long e) {
        long res = 1;
        long baseVal = a % MOD;
        while (e > 0) {
            if ((e & 1) == 1) res = res * baseVal % MOD;
            baseVal = baseVal * baseVal % MOD;
            e >>= 1;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var numberOfWays = function(n, x, y) {
    const MOD = 1000000007n;

    const maxN = Math.max(n, x);
    // factorials
    const fact = new Array(maxN + 1);
    const invFact = new Array(maxN + 1);
    fact[0] = 1n;
    for (let i = 1; i <= maxN; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    // fast power
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
    invFact[maxN] = modPow(fact[maxN], MOD - 2n);
    for (let i = maxN; i > 0; i--) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    // Stirling numbers of the second kind S[n][k]
    const S = new Array(n + 1);
    S[0] = [1n];
    for (let i = 1; i <= n; i++) {
        const limitK = Math.min(i, x);
        S[i] = new Array(limitK + 1).fill(0n);
        for (let k = 1; k <= limitK; k++) {
            const term1 = (BigInt(k) * (S[i - 1][k] || 0n)) % MOD;
            const term2 = S[i - 1][k - 1] || 0n;
            S[i][k] = (term1 + term2) % MOD;
        }
    }

    // powers of y
    const powY = new Array(x + 1);
    powY[0] = 1n;
    const bigY = BigInt(y);
    for (let i = 1; i <= x; i++) {
        powY[i] = (powY[i - 1] * bigY) % MOD;
    }

    let ans = 0n;
    const limit = Math.min(n, x);
    for (let k = 1; k <= limit; k++) {
        // P(x,k) = x! / (x-k)!
        const perm = (fact[x] * invFact[x - k]) % MOD;
        let term = (perm * S[n][k]) % MOD;
        term = (term * powY[k]) % MOD;
        ans = (ans + term) % MOD;
    }

    return Number(ans);
};
```

## Typescript

```typescript
function numberOfWays(n: number, x: number, y: number): number {
    const MOD = 1000000007n;
    const maxK = Math.min(n, x);

    // Stirling numbers of the second kind S[n][k]
    const S: bigint[][] = Array.from({ length: n + 1 }, () => new Array(maxK + 1).fill(0n));
    S[0][0] = 1n;
    for (let i = 1; i <= n; i++) {
        const limit = Math.min(i, maxK);
        for (let j = 1; j <= limit; j++) {
            S[i][j] = (S[i - 1][j - 1] + BigInt(j) * S[i - 1][j]) % MOD;
        }
    }

    // factorials and inverse factorials up to x
    const fact: bigint[] = new Array(x + 1).fill(0n);
    const invFact: bigint[] = new Array(x + 1).fill(0n);
    fact[0] = 1n;
    for (let i = 1; i <= x; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    const modPow = (base: bigint, exp: bigint): bigint => {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    };
    invFact[x] = modPow(fact[x], MOD - 2n);
    for (let i = x; i >= 1; i--) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    // powers of y
    const powY: bigint[] = new Array(maxK + 1).fill(0n);
    powY[0] = 1n;
    const bigY = BigInt(y) % MOD;
    for (let i = 1; i <= maxK; i++) {
        powY[i] = (powY[i - 1] * bigY) % MOD;
    }

    let ans = 0n;
    for (let k = 1; k <= maxK; k++) {
        const stir = S[n][k];
        if (stir === 0n) continue;
        // permutations P(x, k) = x! / (x - k)!
        const perm = (fact[x] * invFact[x - k]) % MOD;
        const term = (((stir * perm) % MOD) * powY[k]) % MOD;
        ans = (ans + term) % MOD;
    }

    return Number(ans);
}
```

## Php

```php
class Solution {

    const MOD = 1000000007;

    /**
     * @param Integer $n
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function numberOfWays($n, $x, $y) {
        $max = max($n, $x);
        // factorials
        $fact = array_fill(0, $max + 1, 1);
        for ($i = 1; $i <= $max; $i++) {
            $fact[$i] = ($fact[$i - 1] * $i) % self::MOD;
        }
        // inverse factorials
        $invFact = array_fill(0, $max + 1, 1);
        $invFact[$max] = $this->modPow($fact[$max], self::MOD - 2);
        for ($i = $max; $i >= 1; $i--) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % self::MOD;
        }

        // Stirling numbers of the second kind S[n][k]
        $S = array_fill(0, $n + 1, array_fill(0, $n + 1, 0));
        $S[0][0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 1; $j <= $i; $j++) {
                $val = ($j * $S[$i - 1][$j]) % self::MOD;
                $val = ($val + $S[$i - 1][$j - 1]) % self::MOD;
                $S[$i][$j] = $val;
            }
        }

        // powers of y
        $limit = min($x, $n);
        $powY = array_fill(0, $limit + 1, 1);
        for ($i = 1; $i <= $limit; $i++) {
            $powY[$i] = ($powY[$i - 1] * $y) % self::MOD;
        }

        $ans = 0;
        for ($k = 1; $k <= $limit; $k++) {
            // C(x, k)
            $comb = $fact[$x];
            $comb = ($comb * $invFact[$k]) % self::MOD;
            $comb = ($comb * $invFact[$x - $k]) % self::MOD;

            $term = $comb;                         // choose stages
            $term = ($term * $fact[$k]) % self::MOD;   // k!
            $term = ($term * $S[$n][$k]) % self::MOD;  // surjective assignments
            $term = ($term * $powY[$k]) % self::MOD;   // scores

            $ans = ($ans + $term) % self::MOD;
        }

        return $ans;
    }

    private function modPow($base, $exp) {
        $mod = self::MOD;
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
    let MOD = 1_000_000_007

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

    func numberOfWays(_ n: Int, _ x: Int, _ y: Int) -> Int {
        let maxVal = max(n, x)
        var fact = [Int](repeating: 0, count: maxVal + 1)
        var invFact = [Int](repeating: 0, count: maxVal + 1)

        fact[0] = 1
        if maxVal > 0 {
            for i in 1...maxVal {
                fact[i] = Int((Int64(fact[i - 1]) * Int64(i)) % Int64(MOD))
            }
        }

        invFact[maxVal] = modPow(fact[maxVal], MOD - 2)
        if maxVal > 0 {
            for i in stride(from: maxVal, to: 0, by: -1) {
                invFact[i - 1] = Int((Int64(invFact[i]) * Int64(i)) % Int64(MOD))
            }
        }

        func comb(_ n: Int, _ k: Int) -> Int {
            if k < 0 || k > n { return 0 }
            let res = Int(
                (Int64(fact[n]) *
                 Int64(invFact[k]) % Int64(MOD)) *
                 Int64(invFact[n - k]) % Int64(MOD)
            )
            return res
        }

        // Stirling numbers of the second kind S(n, k)
        var stir = Array(repeating: Array(repeating: 0, count: x + 1), count: n + 1)
        stir[0][0] = 1
        if n > 0 {
            for i in 1...n {
                let limit = min(i, x)
                if limit >= 1 {
                    for j in 1...limit {
                        let term1 = stir[i - 1][j - 1]
                        let term2 = Int((Int64(j) * Int64(stir[i - 1][j])) % Int64(MOD))
                        var val = term1 + term2
                        if val >= MOD { val -= MOD }
                        stir[i][j] = val
                    }
                }
            }
        }

        let maxK = min(n, x)
        var powY = [Int](repeating: 0, count: maxK + 1)
        powY[0] = 1
        if maxK >= 1 {
            for i in 1...maxK {
                powY[i] = Int((Int64(powY[i - 1]) * Int64(y)) % Int64(MOD))
            }
        }

        var ans = 0
        if maxK >= 1 {
            for k in 1...maxK {
                let c = comb(x, k)
                let termA = Int((Int64(c) * Int64(fact[k])) % Int64(MOD))
                let termB = Int((Int64(termA) * Int64(stir[n][k])) % Int64(MOD))
                let termC = Int((Int64(termB) * Int64(powY[k])) % Int64(MOD))
                ans += termC
                if ans >= MOD { ans -= MOD }
            }
        }

        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfWays(n: Int, x: Int, y: Int): Int {
        val MOD = 1_000_000_007L
        val maxK = kotlin.math.min(n, x)

        // Stirling numbers of the second kind S[i][j]
        val stirling = Array(n + 1) { LongArray(maxK + 1) }
        stirling[0][0] = 1L
        for (i in 1..n) {
            val limit = kotlin.math.min(i, maxK)
            for (j in 1..limit) {
                stirling[i][j] = (stirling[i - 1][j - 1] + j * stirling[i - 1][j]) % MOD
            }
        }

        // Powers of y
        val powY = LongArray(maxK + 1)
        powY[0] = 1L
        for (k in 1..maxK) {
            powY[k] = powY[k - 1] * y % MOD
        }

        var ans = 0L
        var perm = 1L // P(x,0) = 1
        for (k in 1..maxK) {
            perm = perm * (x - k + 1) % MOD   // P(x,k)
            val term = perm * stirling[n][k] % MOD * powY[k] % MOD
            ans += term
            if (ans >= MOD) ans -= MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  static const int MOD = 1000000007;

  int numberOfWays(int n, int x, int y) {
    int kMax = min(x, n);
    // factorials up to max(x, n)
    int limit = max(x, n);
    List<int> fact = List.filled(limit + 1, 1);
    for (int i = 1; i <= limit; ++i) {
      fact[i] = (fact[i - 1] * i) % MOD;
    }
    // inverse factorials
    List<int> invFact = List.filled(limit + 1, 1);
    invFact[limit] = _modPow(fact[limit], MOD - 2);
    for (int i = limit; i > 0; --i) {
      invFact[i - 1] = (invFact[i] * i) % MOD;
    }

    // Stirling numbers of the second kind S[n][k]
    List<List<int>> stir = List.generate(n + 1, (_) => List.filled(kMax + 1, 0));
    stir[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
      int up = min(i, kMax);
      for (int j = 1; j <= up; ++j) {
        int val = (stir[i - 1][j - 1] + (j * stir[i - 1][j]) % MOD) % MOD;
        stir[i][j] = val;
      }
    }

    // powers of y
    List<int> powY = List.filled(kMax + 1, 1);
    for (int i = 1; i <= kMax; ++i) {
      powY[i] = (powY[i - 1] * y) % MOD;
    }

    int ans = 0;
    for (int k = 1; k <= kMax; ++k) {
      // P(x, k) = x! / (x-k)!
      int perm = ((fact[x] * invFact[x - k]) % MOD);
      int term = perm;
      term = (term * stir[n][k]) % MOD;
      term = (term * powY[k]) % MOD;
      ans += term;
      if (ans >= MOD) ans -= MOD;
    }
    return ans;
  }

  int _modPow(int base, int exp) {
    long result = 1;
    long b = base.toLong();
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % MOD;
      }
      b = (b * b) % MOD;
      exp >>= 1;
    }
    return result.toInt();
  }
}

// Helper extensions for long arithmetic
extension on int {
  long toLong() => long(this);
}

class long {
  final int value;
  const long(this.value);
  operator *(long other) => long((value * other.value) % Solution.MOD);
  operator %(int mod) => long(value % mod);
  operator +(long other) => long((value + other.value) % Solution.MOD);
  operator -(long other) => long((value - other.value + Solution.MOD) % Solution.MOD);
  int toInt() => value;
}
```

## Golang

```go
func numberOfWays(n int, x int, y int) int {
	const MOD int64 = 1000000007

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	maxVal := max(x, n)
	fac := make([]int64, maxVal+1)
	invFac := make([]int64, maxVal+1)
	fac[0] = 1
	for i := 1; i <= maxVal; i++ {
		fac[i] = fac[i-1] * int64(i) % MOD
	}
	modPow := func(a, e int64) int64 {
		res := int64(1)
		base := a % MOD
		exp := e
		for exp > 0 {
			if exp&1 == 1 {
				res = res * base % MOD
			}
			base = base * base % MOD
			exp >>= 1
		}
		return res
	}
	invFac[maxVal] = modPow(fac[maxVal], MOD-2)
	for i := maxVal; i > 0; i-- {
		invFac[i-1] = invFac[i] * int64(i) % MOD
	}

	// Stirling numbers of the second kind S[n][k]
	S := make([][]int64, n+1)
	for i := range S {
		S[i] = make([]int64, x+1)
	}
	S[0][0] = 1
	for i := 1; i <= n; i++ {
		limit := min(i, x)
		for j := 1; j <= limit; j++ {
			S[i][j] = (S[i-1][j-1] + int64(j)*S[i-1][j]) % MOD
		}
	}

	// powers of y
	powY := make([]int64, x+1)
	powY[0] = 1
	for i := 1; i <= x; i++ {
		powY[i] = powY[i-1] * int64(y) % MOD
	}

	ans := int64(0)
	limitK := min(n, x)
	for k := 1; k <= limitK; k++ {
		comb := fac[x] * invFac[k] % MOD * invFac[x-k] % MOD // C(x,k)
		term := comb * fac[k] % MOD                         // *k!
		term = term * S[n][k] % MOD
		term = term * powY[k] % MOD
		ans = (ans + term) % MOD
	}
	return int(ans)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e)
  mod = MOD
  res = 1
  a %= mod
  while e > 0
    res = res * a % mod if (e & 1) == 1
    a = a * a % mod
    e >>= 1
  end
  res
end

def number_of_ways(n, x, y)
  max_n = [n, x].max
  fact = Array.new(max_n + 1, 1)
  (1..max_n).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact = Array.new(max_n + 1, 1)
  inv_fact[max_n] = mod_pow(fact[max_n], MOD - 2)
  max_n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % MOD }

  comb = lambda do |nn, kk|
    return 0 if kk < 0 || kk > nn
    fact[nn] * inv_fact[kk] % MOD * inv_fact[nn - kk] % MOD
  end

  # Stirling numbers of the second kind S(n,k)
  s = Array.new(n + 1) { Array.new(n + 1, 0) }
  s[0][0] = 1
  (1..n).each do |i|
    (1..i).each do |j|
      s[i][j] = (s[i - 1][j - 1] + j * s[i - 1][j]) % MOD
    end
  end

  ans = 0
  limit = [n, x].min
  (1..limit).each do |k|
    onto = fact[k] * s[n][k] % MOD          # number of onto assignments to k labeled stages
    ways = comb.call(x, k) * onto % MOD     # choose stages and assign performers
    ways = ways * mod_pow(y, k) % MOD       # score each band
    ans = (ans + ways) % MOD
  end
  ans
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L

  def numberOfWays(n: Int, x: Int, y: Int): Int = {
    val maxVal = math.max(n, x)
    // factorials
    val fact = new Array[Long](maxVal + 1)
    val invFact = new Array[Long](maxVal + 1)
    fact(0) = 1L
    for (i <- 1 to maxVal) {
      fact(i) = fact(i - 1) * i % MOD
    }
    // modular exponentiation
    def modPow(base: Long, exp: Long): Long = {
      var b = base % MOD
      var e = exp
      var res = 1L
      while (e > 0) {
        if ((e & 1L) == 1L) res = res * b % MOD
        b = b * b % MOD
        e >>= 1
      }
      res
    }
    invFact(maxVal) = modPow(fact(maxVal), MOD - 2)
    for (i <- maxVal - 1 to 0 by -1) {
      invFact(i) = invFact(i + 1) * (i + 1) % MOD
    }

    // Stirling numbers of the second kind S(n,k)
    val stir = Array.ofDim[Long](n + 1, n + 1)
    stir(0)(0) = 1L
    for (i <- 1 to n) {
      var j = 1
      while (j <= i) {
        stir(i)(j) = (stir(i - 1)(j - 1) + j.toLong * stir(i - 1)(j)) % MOD
        j += 1
      }
    }

    val limit = math.min(n, x)
    val yPow = new Array[Long](limit + 1)
    yPow(0) = 1L
    for (k <- 1 to limit) {
      yPow(k) = yPow(k - 1) * y % MOD
    }

    var ans = 0L
    for (k <- 1 to limit) {
      val s = stir(n)(k)
      if (s != 0) {
        val perm = fact(x) * invFact(x - k) % MOD // P(x, k)
        val term = ((s * perm) % MOD) * yPow(k) % MOD
        ans = (ans + term) % MOD
      }
    }
    ans.toInt
  }
}
```

## Rust

```rust
use std::cmp::min;

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

impl Solution {
    pub fn number_of_ways(n: i32, x: i32, y: i32) -> i32 {
        let n_usize = n as usize;
        let x_usize = x as usize;

        // factorials and inverse factorials up to max(x,n)
        let limit = max(n_usize, x_usize);
        let mut fact = vec![1i64; limit + 1];
        for i in 1..=limit {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact = vec![1i64; limit + 1];
        inv_fact[limit] = mod_pow(fact[limit], MOD - 2);
        for i in (1..=limit).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }

        // Stirling numbers of the second kind S(n,k)
        let mut stir = vec![vec![0i64; x_usize + 1]; n_usize + 1];
        stir[0][0] = 1;
        for i in 1..=n_usize {
            let max_k = min(i, x_usize);
            for k in 1..=max_k {
                let val = (stir[i - 1][k - 1] + (k as i64) * stir[i - 1][k]) % MOD;
                stir[i][k] = val;
            }
        }

        // precompute powers of y
        let mut pow_y = vec![1i64; x_usize + 1];
        let y_mod = (y as i64) % MOD;
        for k in 1..=x_usize {
            pow_y[k] = pow_y[k - 1] * y_mod % MOD;
        }

        // sum over k
        let mut ans: i64 = 0;
        let max_k = min(n_usize, x_usize);
        for k in 1..=max_k {
            // C(x,k)
            let comb = fact[x_usize] * inv_fact[k] % MOD * inv_fact[x_usize - k] % MOD;
            let term = comb
                * stir[n_usize][k] % MOD
                * pow_y[k] % MOD;
            ans += term;
            if ans >= MOD {
                ans -= MOD;
            }
        }

        ans as i32
    }
}

fn max(a: usize, b: usize) -> usize {
    if a > b { a } else { b }
}
```

## Racket

```racket
(define MOD 1000000007)

(: pow-mod : Integer Integer -> Integer)
(define (pow-mod a e)
  (let loop ((base (modulo a MOD)) (exp e) (res 1))
    (if (= exp 0)
        res
        (loop (modulo (* base base) MOD)
              (quotient exp 2)
              (if (odd? exp) (modulo (* res base) MOD) res)))))

(define/contract (number-of-ways n x y)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((maxK (min n x))
         ;; Stirling numbers of the second kind, rolling DP
         (prev (make-vector (+ x 1) 0)))
    (vector-set! prev 0 1)
    (for ([i (in-range 1 (add1 n))])
      (define cur (make-vector (+ x 1) 0))
      (for ([k (in-range 1 (add1 (min i x)))])
        (let* ((term1 (modulo (* k (vector-ref prev k)) MOD))
               (term2 (vector-ref prev (sub1 k)))
               (val   (modulo (+ term1 term2) MOD)))
          (vector-set! cur k val)))
      (set! prev cur))
    ;; factorials and inverse factorials up to x
    (define fact (make-vector (+ x 1) 0))
    (vector-set! fact 0 1)
    (for ([i (in-range 1 (add1 x))])
      (vector-set! fact i (modulo (* (vector-ref fact (sub1 i)) i) MOD)))
    (define inv-fact (make-vector (+ x 1) 0))
    (vector-set! inv-fact x (pow-mod (vector-ref fact x) (- MOD 2)))
    (for ([i (in-range (sub1 x) -1 -1)])
      (vector-set! inv-fact i
                   (modulo (* (vector-ref inv-fact (add1 i)) (add1 i)) MOD)))
    ;; accumulate answer
    (let loop ((k 1) (ypow 1) (ans 0))
      (if (> k maxK)
          ans
          (let* ((new-ypow (modulo (* ypow y) MOD))
                 (perm (modulo (* (vector-ref fact x)
                                 (vector-ref inv-fact (- x k))) MOD))
                 (term (modulo (* perm (vector-ref prev k)) MOD))
                 (add  (modulo (* term new-ypow) MOD)))
            (loop (add1 k) new-ypow (modulo (+ ans add) MOD)))))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_ways/3]).

-define(MOD, 1000000007).

-spec number_of_ways(N :: integer(), X :: integer(), Y :: integer()) -> integer().
number_of_ways(N, X, Y) ->
    Mod = ?MOD,
    MaxK = min(N, X),
    StirlingRow = stirling_last_row(N, MaxK, Mod),
    compute_sum(StirlingRow, X, Y, MaxK, Mod).

%% Compute the last row of Stirling numbers S(N,k) for k=0..MaxK
stirling_last_row(N, MaxK, Mod) ->
    Init = list_to_tuple(lists:duplicate(MaxK + 1, 0)),
    Init1 = setelement(1, Init, 1),               % S(0,0)=1
    stirling_loop(1, N, MaxK, Init1, Mod).

stirling_loop(I, N, _MaxK, Prev, _Mod) when I > N ->
    Prev;
stirling_loop(I, N, MaxK, Prev, Mod) ->
    Limit = min(I, MaxK),
    Curr0 = list_to_tuple(lists:duplicate(MaxK + 1, 0)),
    Curr = stirling_inner(1, Limit, Prev, Curr0, Mod),
    stirring_loop(I + 1, N, MaxK, Curr, Mod).

stirling_inner(J, Limit, _Prev, Curr, _Mod) when J > Limit ->
    Curr;
stirling_inner(J, Limit, Prev, Curr, Mod) ->
    SjPrev = element(J + 1, Prev),      % S(i-1, j)
    SjMinusPrev = element(J, Prev),    % S(i-1, j-1)
    Val = (J * SjPrev + SjMinusPrev) rem Mod,
    NewCurr = setelement(J + 1, Curr, Val),
    stirling_inner(J + 1, Limit, Prev, NewCurr, Mod).

%% Compute the final answer using the Stirling row
compute_sum(Row, X, Y, MaxK, Mod) ->
    compute_sum_loop(1, MaxK, Row, X, Y, 0, 1, 1, Mod).

compute_sum_loop(K, MaxK, _Row, _X, _Y, Ans, _Perm, _PowY, _Mod) when K > MaxK ->
    Ans;
compute_sum_loop(K, MaxK, Row, X, Y, Ans, Perm, PowY, Mod) ->
    NewPerm = (Perm * (X - K + 1)) rem Mod,
    NewPowY = (PowY * Y) rem Mod,
    S = element(K + 1, Row),
    Term = ((NewPerm * S) rem Mod * NewPowY) rem Mod,
    NewAns = (Ans + Term) rem Mod,
    compute_sum_loop(K + 1, MaxK, Row, X, Y, NewAns, NewPerm, NewPowY, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec number_of_ways(n :: integer, x :: integer, y :: integer) :: integer
  def number_of_ways(n, x, y) do
    kmax = min(n, x)

    s_arr = stirling_numbers(n, kmax)
    limit = max(n, x)
    fact = factorials(limit)
    inv_fact = inv_factorials(limit, fact)

    Enum.reduce(1..kmax, 0, fn k, acc ->
      perm = rem(:array.get(x, fact) * :array.get(x - k, inv_fact), @mod)
      s = :array.get(k, s_arr)
      yk = mod_pow(y, k)
      term = rem(rem(perm * s, @mod) * yk, @mod)
      rem(acc + term, @mod)
    end)
  end

  defp stirling_numbers(n, kmax) do
    prev = :array.new(kmax + 1, default: 0) |> :array.set(0, 1)

    Enum.reduce(1..n, prev, fn i, acc ->
      cur = :array.new(kmax + 1, default: 0)
      maxj = min(i, kmax)

      Enum.reduce(1..maxj, cur, fn j, cacc ->
        val =
          rem(
            :array.get(j - 1, acc) + j * :array.get(j, acc),
            @mod
          )

        :array.set(j, val, cacc)
      end)
    end)
  end

  defp factorials(limit) do
    Enum.reduce(0..limit, :array.new(limit + 1, default: 0), fn i, acc ->
      if i == 0 do
        :array.set(0, 1, acc)
      else
        prev = :array.get(i - 1, acc)
        :array.set(i, rem(prev * i, @mod), acc)
      end
    end)
  end

  defp inv_factorials(limit, fact) do
    inv_last = mod_pow(:array.get(limit, fact), @mod - 2)

    base = :array.new(limit + 1, default: 0) |> :array.set(limit, inv_last)

    Enum.reduce(Enum.reverse(0..(limit - 1)), base, fn i, acc ->
      val = rem(:array.get(i + 1, acc) * (i + 1), @mod)
      :array.set(i, val, acc)
    end)
  end

  defp mod_pow(_base, 0), do: 1

  defp mod_pow(base, exp) do
    pow_loop(rem(base, @mod), exp, 1)
  end

  defp pow_loop(_b, 0, acc), do: acc

  defp pow_loop(b, e, acc) do
    acc = if rem(e, 2) == 1, do: rem(acc * b, @mod), else: acc
    b = rem(b * b, @mod)
    pow_loop(b, div(e, 2), acc)
  end
end
```

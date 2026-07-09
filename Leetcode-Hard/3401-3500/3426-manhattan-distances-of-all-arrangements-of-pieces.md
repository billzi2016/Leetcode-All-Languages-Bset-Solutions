# 3426. Manhattan Distances of All Arrangements of Pieces

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    static const long long MOD = 1000000007LL;
    
    long long modpow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = (__int128)r * a % MOD;
            a = (__int128)a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    
    long long modInv(long long x) { return modpow(x, MOD - 2); }
    
public:
    int distanceSum(int m, int n, int k) {
        long long N = 1LL * m * n;
        // factorials
        vector<long long> fact(N + 1), invFact(N + 1);
        fact[0] = 1;
        for (long long i = 1; i <= N; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[N] = modInv(fact[N]);
        for (long long i = N; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;
        
        auto C = [&](long long nn, long long kk)->long long{
            if (kk < 0 || kk > nn) return 0;
            return fact[nn] * invFact[kk] % MOD * invFact[nn - kk] % MOD;
        };
        
        long long comb = C(N - 2, k - 2); // number of arrangements containing a fixed pair
        
        long long inv6 = modInv(6);
        auto sumDiff = [&](long long len)->long long{
            // len*(len-1)*(len+1)/6
            long long a = len % MOD;
            long long b = (len - 1) % MOD;
            long long c = (len + 1) % MOD;
            return (__int128)a * b % MOD * c % MOD * inv6 % MOD;
        };
        
        long long sumRow = sumDiff(m); // sum_{r1<r2} (r2-r1)
        long long sumCol = sumDiff(n);
        
        long long n2 = (long long)n % MOD * n % MOD;
        long long m2 = (long long)m % MOD * m % MOD;
        
        long long Sx = (__int128)n2 * sumRow % MOD; // column choices squared
        long long Sy = (__int128)m2 * sumCol % MOD;
        long long totalDistPairs = (Sx + Sy) % MOD;
        
        long long ans = (__int128)comb * totalDistPairs % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    private long[] fact;
    private long[] invFact;

    public int distanceSum(int m, int n, int k) {
        int N = (int) ((long) m * n);
        precomputeFactorials(N);
        long comb = nCr(N - 2, k - 2);
        long inv6 = modPow(6, MOD - 2);

        long mm = m % MOD;
        long nn = n % MOD;

        long termRow = (nn * nn) % MOD;
        termRow = termRow * ((mm * ((mm - 1 + MOD) % MOD)) % MOD) % MOD;
        termRow = termRow * ((mm + 1) % MOD) % MOD; // n^2 * m*(m-1)*(m+1)

        long termCol = (mm * mm) % MOD;
        termCol = termCol * ((nn * ((nn - 1 + MOD) % MOD)) % MOD) % MOD;
        termCol = termCol * ((nn + 1) % MOD) % MOD; // m^2 * n*(n-1)*(n+1)

        long sumDist = (termRow + termCol) % MOD;
        sumDist = sumDist * inv6 % MOD;

        long ans = comb * sumDist % MOD;
        return (int) ans;
    }

    private void precomputeFactorials(int n) {
        fact = new long[n + 1];
        invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
    }

    private long nCr(int N, int K) {
        if (K < 0 || K > N) return 0;
        return fact[N] * invFact[K] % MOD * invFact[N - K] % MOD;
    }

    private long modPow(long base, long exp) {
        long res = 1;
        long b = base % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = res * b % MOD;
            }
            b = b * b % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def distanceSum(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        N = m * n

        # factorials up to N
        fac = [1] * (N + 1)
        for i in range(1, N + 1):
            fac[i] = fac[i - 1] * i % MOD
        invfac = [1] * (N + 1)
        invfac[N] = pow(fac[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            invfac[i - 1] = invfac[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fac[a] * invfac[b] % MOD * invfac[a - b] % MOD

        # sum of |row_i - row_j| over all unordered pairs of rows
        row_sum = (m * m * m - m) // 6   # (m^3 - m)/6
        col_sum = (n * n * n - n) // 6   # (n^3 - n)/6

        S_mod = ((n * n) % MOD) * (row_sum % MOD) % MOD
        S_mod = (S_mod + ((m * m) % MOD) * (col_sum % MOD)) % MOD

        ways = comb(N - 2, k - 2)
        return ways * S_mod % MOD
```

## Python3

```python
class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MOD = 10**9 + 7
        N = m * n

        # factorials up to N
        fac = [1] * (N + 1)
        for i in range(1, N + 1):
            fac[i] = fac[i - 1] * i % MOD
        invfac = [1] * (N + 1)
        invfac[N] = pow(fac[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            invfac[i - 1] = invfac[i] * i % MOD

        def C(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            return fac[n] * invfac[r] % MOD * invfac[n - r] % MOD

        comb = C(N - 2, k - 2)

        inv6 = pow(6, MOD - 2, MOD)
        m_mod = m % MOD
        n_mod = n % MOD

        term1 = (n_mod * n_mod) % MOD
        term1 = term1 * ((m_mod * (m_mod - 1)) % MOD) % MOD
        term1 = term1 * ((m_mod + 1) % MOD) % MOD

        term2 = (m_mod * m_mod) % MOD
        term2 = term2 * ((n_mod * (n_mod - 1)) % MOD) % MOD
        term2 = term2 * ((n_mod + 1) % MOD) % MOD

        S = (term1 + term2) % MOD
        S = S * inv6 % MOD

        return comb * S % MOD
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int distanceSum(int m, int n, int k) {
    const long long MOD = 1000000007LL;
    long long N = 1LL * m * n;

    vector<long long> fac(N + 1), invfac(N + 1);
    fac[0] = 1;
    for (long long i = 1; i <= N; ++i) fac[i] = fac[i - 1] * i % MOD;

    auto modpow = [&](long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    };

    invfac[N] = modpow(fac[N], MOD - 2);
    for (long long i = N; i >= 1; --i) invfac[i - 1] = invfac[i] * i % MOD;

    auto C = [&](long long nn, long long kk) -> long long {
        if (kk < 0 || kk > nn) return 0;
        return fac[nn] * invfac[kk] % MOD * invfac[nn - kk] % MOD;
    };

    long long comb = C(N - 2, k - 2);
    long long inv6 = modpow(6, MOD - 2);

    long long mm = m % MOD;
    long long nn_mod = n % MOD;

    long long termRow = nn_mod * nn_mod % MOD *
                        ((mm * mm % MOD * mm % MOD - mm + MOD) % MOD) % MOD;
    long long termCol = mm * mm % MOD *
                        ((nn_mod * nn_mod % MOD * nn_mod % MOD - nn_mod + MOD) % MOD) % MOD;

    long long S = (termRow + termCol) % MOD * inv6 % MOD;
    long long ans = comb * S % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    const long MOD = 1000000007L;

    private static long ModPow(long a, long e)
    {
        long res = 1;
        a %= MOD;
        while (e > 0)
        {
            if ((e & 1) == 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }

    public int DistanceSum(int m, int n, int k)
    {
        long rows = m;
        long cols = n;
        long totalCellsLong = rows * cols;
        int totalCells = (int)totalCellsLong; // totalCells <= 1e5

        // factorials
        long[] fact = new long[totalCells + 1];
        long[] invFact = new long[totalCells + 1];
        fact[0] = 1;
        for (int i = 1; i <= totalCells; i++)
            fact[i] = fact[i - 1] * i % MOD;

        invFact[totalCells] = ModPow(fact[totalCells], MOD - 2);
        for (int i = totalCells; i >= 1; i--)
            invFact[i - 1] = invFact[i] * i % MOD;

        long comb = 0;
        if (k >= 2)
        {
            int nChoose = totalCells - 2;
            int kChoose = k - 2;
            if (kChoose <= nChoose && kChoose >= 0)
            {
                comb = fact[nChoose];
                comb = comb * invFact[kChoose] % MOD;
                comb = comb * invFact[nChoose - kChoose] % MOD;
            }
        }

        long mMod = rows % MOD;
        long nMod = cols % MOD;

        long mnMod = mMod * nMod % MOD;

        long mSq = mMod * mMod % MOD;
        long nSq = nMod * nMod % MOD;

        long partA = nMod * ((mSq - 1 + MOD) % MOD) % MOD; // n*(m^2-1)
        long partB = mMod * ((nSq - 1 + MOD) % MOD) % MOD; // m*(n^2-1)

        long sumPart = (partA + partB) % MOD;

        long inv6 = ModPow(6, MOD - 2);
        long S = mnMod * sumPart % MOD;
        S = S * inv6 % MOD; // total Manhattan distance over all unordered cell pairs

        long ans = comb * S % MOD;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var distanceSum = function(m, n, k) {
    const MOD = 1000000007n;
    const N = m * n; // total cells, fits in Number (<=1e5)

    // precompute factorials up to N
    const fact = new Array(N + 1);
    const invFact = new Array(N + 1);
    fact[0] = 1n;
    for (let i = 1; i <= N; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    // fast power
    const modPow = (base, exp) => {
        let res = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    };
    invFact[N] = modPow(fact[N], MOD - 2n);
    for (let i = N; i > 0; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    // C(N-2, k-2)
    const comb = (() => {
        if (k < 2) return 0n;
        const nn = N - 2;
        const kk = k - 2;
        if (kk > nn || kk < 0) return 0n;
        let res = fact[nn];
        res = (res * invFact[kk]) % MOD;
        res = (res * invFact[nn - kk]) % MOD;
        return res;
    })();

    // compute sum of Manhattan distances over all unordered pairs of cells
    const mBig = BigInt(m);
    const nBig = BigInt(n);

    const diffRows = (mBig * (mBig * mBig - 1n)) / 6n; // Σ |r1-r2|
    const diffCols = (nBig * (nBig * nBig - 1n)) / 6n; // Σ |c1-c2|

    const term1 = ((nBig * nBig) % MOD) * (diffRows % MOD) % MOD;
    const term2 = ((mBig * mBig) % MOD) * (diffCols % MOD) % MOD;

    const totalDistPairs = (term1 + term2) % MOD; // S

    const answer = (comb * totalDistPairs) % MOD;
    return Number(answer);
};
```

## Typescript

```typescript
function distanceSum(m: number, n: number, k: number): number {
    const MOD = 1000000007n;

    const N = m * n;
    // precompute factorials up to N
    const fact: bigint[] = new Array(N + 1);
    const invFact: bigint[] = new Array(N + 1);
    fact[0] = 1n;
    for (let i = 1; i <= N; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    const modPow = (base: bigint, exp: bigint): bigint => {
        let res = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    };
    invFact[N] = modPow(fact[N], MOD - 2n);
    for (let i = N; i > 0; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    const comb = (() => {
        // C(N-2, k-2)
        if (k < 2) return 0n;
        const a = N - 2;
        const b = k - 2;
        if (b < 0 || b > a) return 0n;
        let res = fact[a];
        res = (res * invFact[b]) % MOD;
        res = (res * invFact[a - b]) % MOD;
        return res;
    })();

    const bigM = BigInt(m);
    const bigN = BigInt(n);

    // rowSum = (m^3 - m) / 6
    const rowSum = ((bigM ** 3n) - bigM) / 6n;
    // colSum = (n^3 - n) / 6
    const colSum = ((bigN ** 3n) - bigN) / 6n;

    const term1 = ((bigN * bigN) % MOD) * (rowSum % MOD) % MOD;
    const term2 = ((bigM * bigM) % MOD) * (colSum % MOD) % MOD;
    const S = (term1 + term2) % MOD;

    const ans = (comb * S) % MOD;
    return Number(ans);
}
```

## Php

```php
class Solution {

    const MOD = 1000000007;

    private function modPow(int $base, int $exp): int {
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

    private function nCr(int $n, int $r, array $fact, array $invFact): int {
        if ($r < 0 || $r > $n) return 0;
        $mod = self::MOD;
        $res = $fact[$n];
        $res = ($res * $invFact[$r]) % $mod;
        $res = ($res * $invFact[$n - $r]) % $mod;
        return $res;
    }

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function distanceSum($m, $n, $k) {
        $mod = self::MOD;
        $N = $m * $n;

        // precompute factorials up to N
        $fact = array_fill(0, $N + 1, 0);
        $invFact = array_fill(0, $N + 1, 0);
        $fact[0] = 1;
        for ($i = 1; $i <= $N; ++$i) {
            $fact[$i] = ($fact[$i - 1] * $i) % $mod;
        }
        $invFact[$N] = $this->modPow($fact[$N], $mod - 2);
        for ($i = $N; $i >= 1; --$i) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % $mod;
        }

        // C(N-2, k-2)
        $comb = $this->nCr($N - 2, $k - 2, $fact, $invFact);

        // inverse of 6 modulo MOD
        $inv6 = $this->modPow(6, $mod - 2);

        $mMod = $m % $mod;
        $nMod = $n % $mod;

        // term1: n^2 * m(m-1)(m+1) / 6
        $term1 = ($nMod * $nMod) % $mod;
        $term1 = ($term1 * $mMod) % $mod;
        $term1 = ($term1 * (($m - 1) % $mod)) % $mod;
        $term1 = ($term1 * (($m + 1) % $mod)) % $mod;
        $term1 = ($term1 * $inv6) % $mod;

        // term2: m^2 * n(n-1)(n+1) / 6
        $term2 = ($mMod * $mMod) % $mod;
        $term2 = ($term2 * $nMod) % $mod;
        $term2 = ($term2 * (($n - 1) % $mod)) % $mod;
        $term2 = ($term2 * (($n + 1) % $mod)) % $mod;
        $term2 = ($term2 * $inv6) % $mod;

        $S = ($term1 + $term2) % $mod;

        $answer = ($comb * $S) % $mod;
        return $answer;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD: Int64 = 1_000_000_007
    
    func distanceSum(_ m: Int, _ n: Int, _ k: Int) -> Int {
        let M = Int64(m)
        let Ncol = Int64(n)
        let totalCells = m * n
        if k < 2 { return 0 }
        
        // Precompute factorials up to totalCells
        var fact = [Int64](repeating: 0, count: totalCells + 1)
        var invFact = [Int64](repeating: 0, count: totalCells + 1)
        fact[0] = 1
        for i in 1...totalCells {
            fact[i] = fact[i - 1] * Int64(i) % MOD
        }
        invFact[totalCells] = modPow(fact[totalCells], MOD - 2)
        if totalCells > 0 {
            for i in stride(from: totalCells, to: 0, by: -1) {
                invFact[i - 1] = invFact[i] * Int64(i) % MOD
            }
        }
        
        func comb(_ n: Int, _ r: Int) -> Int64 {
            if r < 0 || r > n { return 0 }
            let res = fact[n] * invFact[r] % MOD * invFact[n - r] % MOD
            return res
        }
        
        // Helper to compute (x / y) mod MOD using modular inverse
        func mulDiv(_ a: Int64, _ b: Int64, _ divisorInv: Int64) -> Int64 {
            return a % MOD * b % MOD * divisorInv % MOD
        }
        
        let inv6 = modPow(6, MOD - 2)
        
        // diff sum for rows and columns using formula (len-1)*len*(len+1)/6
        let diffRows = ((M - 1) % MOD + MOD) % MOD * (M % MOD) % MOD * ((M + 1) % MOD) % MOD * inv6 % MOD
        let diffCols = ((Ncol - 1) % MOD + MOD) % MOD * (Ncol % MOD) % MOD * ((Ncol + 1) % MOD) % MOD * inv6 % MOD
        
        let nSq = Ncol % MOD * Ncol % MOD
        let mSq = M % MOD * M % MOD
        
        let Sr = nSq * diffRows % MOD
        let Sc = mSq * diffCols % MOD
        let S = (Sr + Sc) % MOD
        
        let ways = comb(totalCells - 2, k - 2)
        let answer = ways * S % MOD
        return Int(answer)
    }
    
    private func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
        var result: Int64 = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if e & 1 == 1 {
                result = result * b % MOD
            }
            b = b * b % MOD
            e >>= 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    fun distanceSum(m: Int, n: Int, k: Int): Int {
        val totalCells = m.toLong() * n
        val max = totalCells.toInt()

        // factorials and inverse factorials
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

        fun comb(nn: Int, kk: Int): Long {
            if (kk < 0 || kk > nn) return 0L
            return fact[nn] * invFact[kk] % MOD * invFact[nn - kk] % MOD
        }

        val ways = comb((totalCells - 2).toInt(), k - 2)

        // sum of Manhattan distances over all unordered cell pairs
        val mL = m.toLong()
        val nL = n.toLong()

        val rowDiff = mL * (mL * mL - 1) / 6   // Σ_{i<j} (j-i) for rows
        val colDiff = nL * (nL * nL - 1) / 6   // Σ_{i<j} (j-i) for columns

        val nSqMod = (nL % MOD) * (nL % MOD) % MOD
        val mSqMod = (mL % MOD) * (mL % MOD) % MOD

        var sumDist = (nSqMod * (rowDiff % MOD)) % MOD
        sumDist = (sumDist + (mSqMod * (colDiff % MOD)) % MOD) % MOD

        val answer = ways * sumDist % MOD
        return answer.toInt()
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

  int distanceSum(int m, int n, int k) {
    int N = m * n;
    // Precompute factorials up to N
    List<int> fact = List.filled(N + 1, 0);
    List<int> invFact = List.filled(N + 1, 0);
    fact[0] = 1;
    for (int i = 1; i <= N; ++i) {
      fact[i] = (fact[i - 1] * i) % _mod;
    }
    invFact[N] = _modPow(fact[N], _mod - 2);
    for (int i = N; i > 0; --i) {
      invFact[i - 1] = (invFact[i] * i) % _mod;
    }

    int comb = _nCr(N - 2, k - 2, fact, invFact);

    // precompute inverse of 6
    const int inv6 = 166666668; // modular inverse of 6 modulo 1e9+7

    int mMod = m % _mod;
    int nMod = n % _mod;

    int rowDistSum = ((mMod *
                ((m - 1) % _mod) %
                _mod) *
            ((m + 1) % _mod) %
            _mod) *
        inv6 %
        _mod;
    int colDistSum = ((nMod *
                ((n - 1) % _mod) %
                _mod) *
            ((n + 1) % _mod) %
            _mod) *
        inv6 %
        _mod;

    int nSq = (nMod * nMod) % _mod;
    int mSq = (mMod * mMod) % _mod;

    int totalPairsDist = (nSq * rowDistSum + mSq * colDistSum) % _mod;

    return (comb * totalPairsDist) % _mod;
  }

  int _nCr(int n, int r, List<int> fact, List<int> invFact) {
    if (r < 0 || r > n) return 0;
    return (((fact[n] * invFact[r]) % _mod) * invFact[n - r]) % _mod;
  }

  int _modPow(int base, int exp) {
    long result = 1;
    long b = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      exp >>= 1;
    }
    return result.toInt();
  }
}
```

## Golang

```go
func distanceSum(m int, n int, k int) int {
	const MOD int64 = 1000000007
	N := m * n
	fact := make([]int64, N+1)
	invFact := make([]int64, N+1)

	fact[0] = 1
	for i := 1; i <= N; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[N] = modPow(fact[N], MOD-2, MOD)
	for i := N; i >= 1; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}

	comb := func(nn, rr int) int64 {
		if rr < 0 || rr > nn {
			return 0
		}
		return fact[nn] * invFact[rr] % MOD * invFact[nn-rr] % MOD
	}

	mm := int64(m)
	nn := int64(n)

	term1 := (nn * nn) % MOD
	term1 = term1 * (mm % MOD) % MOD
	term1 = term1 * ((mm - 1) % MOD) % MOD
	term1 = term1 * ((mm + 1) % MOD) % MOD

	term2 := (mm * mm) % MOD
	term2 = term2 * (nn % MOD) % MOD
	term2 = term2 * ((nn - 1) % MOD) % MOD
	term2 = term2 * ((nn + 1) % MOD) % MOD

	inv6 := modPow(6, MOD-2, MOD)
	S := (term1 + term2) % MOD
	S = S * inv6 % MOD

	ans := comb(N-2, k-2) * S % MOD
	return int(ans)
}

func modPow(a, e, mod int64) int64 {
	res := int64(1)
	a %= mod
	for e > 0 {
		if e&1 == 1 {
			res = res * a % mod
		}
		a = a * a % mod
		e >>= 1
	}
	return res
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, b, mod)
  res = 1
  a %= mod
  while b > 0
    res = res * a % mod if (b & 1) == 1
    a = a * a % mod
    b >>= 1
  end
  res
end

def distance_sum(m, n, k)
  total_cells = m * n
  max_n = total_cells

  fact = Array.new(max_n + 1, 1)
  (1..max_n).each { |i| fact[i] = fact[i - 1] * i % MOD }

  inv_fact = Array.new(max_n + 1, 1)
  inv_fact[max_n] = mod_pow(fact[max_n], MOD - 2, MOD)
  (max_n - 1).downto(0) { |i| inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD }

  comb = lambda do |nn, rr|
    return 0 if rr < 0 || rr > nn
    fact[nn] * inv_fact[rr] % MOD * inv_fact[nn - rr] % MOD
  end

  inv6 = mod_pow(6, MOD - 2, MOD)

  m_mod = m % MOD
  n_mod = n % MOD

  term_rows = m_mod * ((m - 1) % MOD) % MOD
  term_rows = term_rows * ((m + 1) % MOD) % MOD
  term_rows = term_rows * inv6 % MOD
  s_row = n_mod * n_mod % MOD * term_rows % MOD

  term_cols = n_mod * ((n - 1) % MOD) % MOD
  term_cols = term_cols * ((n + 1) % MOD) % MOD
  term_cols = term_cols * inv6 % MOD
  s_col = m_mod * m_mod % MOD * term_cols % MOD

  total_distance_sum = (s_row + s_col) % MOD

  factor = comb.call(total_cells - 2, k - 2)

  (factor * total_distance_sum) % MOD
end
```

## Scala

```scala
object Solution {
  private val MOD: Long = 1000000007L
  private def modPow(a: Long, e: Long): Long = {
    var base = a % MOD
    var exp = e
    var res = 1L
    while (exp > 0) {
      if ((exp & 1L) == 1L) res = (res * base) % MOD
      base = (base * base) % MOD
      exp >>= 1
    }
    res
  }

  def distanceSum(m: Int, n: Int, k: Int): Int = {
    val M = m.toLong
    val Ncol = n.toLong
    val totalCells = M * Ncol // up to 1e5

    // precompute factorials up to totalCells
    val maxN = totalCells.toInt
    val fact = new Array[Long](maxN + 1)
    val invFact = new Array[Long](maxN + 1)
    fact(0) = 1L
    var i = 1
    while (i <= maxN) {
      fact(i) = (fact(i - 1) * i) % MOD
      i += 1
    }
    invFact(maxN) = modPow(fact(maxN), MOD - 2)
    i = maxN - 1
    while (i >= 0) {
      invFact(i) = (invFact(i + 1) * (i + 1)) % MOD
      i -= 1
    }

    def comb(n: Long, r: Long): Long = {
      if (r < 0 || r > n) return 0L
      val nn = n.toInt
      val rr = r.toInt
      ((fact(nn) * invFact(rr)) % MOD * invFact(nn - rr)) % MOD
    }

    // sum of Manhattan distances over all unordered cell pairs
    val inv6 = modPow(6, MOD - 2)

    val nMod = Ncol % MOD
    val mMod = M % MOD

    var rowPart = (nMod * nMod) % MOD
    rowPart = (rowPart * ((mMod * ((M - 1) % MOD)) % MOD)) % MOD
    rowPart = (rowPart * ((M + 1) % MOD)) % MOD
    rowPart = (rowPart * inv6) % MOD

    var colPart = (mMod * mMod) % MOD
    colPart = (colPart * ((nMod * ((Ncol - 1) % MOD)) % MOD)) % MOD
    colPart = (colPart * ((Ncol + 1) % MOD)) % MOD
    colPart = (colPart * inv6) % MOD

    val sumDist = (rowPart + colPart) % MOD

    val ways = comb(totalCells - 2, k.toLong - 2)
    val ans = (ways * sumDist) % MOD
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
            res = (res * base) % MOD;
        }
        base = (base * base) % MOD;
        exp >>= 1;
    }
    res
}

pub struct Solution;

impl Solution {
    pub fn distance_sum(m: i32, n: i32, k: i32) -> i32 {
        let m = m as i64;
        let n = n as i64;
        let k = k as i64;
        let total_cells = m * n; // N

        // precompute factorials up to N
        let size = (total_cells + 1) as usize;
        let mut fact: Vec<i64> = vec![1; size];
        for i in 1..size {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        // inverse factorials
        let mut inv_fact: Vec<i64> = vec![1; size];
        inv_fact[size - 1] = mod_pow(fact[size - 1], MOD - 2);
        for i in (1..size).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }

        // C(N-2, k-2)
        let n_minus_2 = total_cells - 2;
        let k_minus_2 = k - 2;
        let comb = if k_minus_2 < 0 || k_minus_2 > n_minus_2 {
            0
        } else {
            fact[n_minus_2 as usize]
                * inv_fact[k_minus_2 as usize] % MOD
                * inv_fact[(n_minus_2 - k_minus_2) as usize] % MOD
        };

        // helper to compute x*(x-1)*(x+1)/6 mod MOD
        let inv6 = mod_pow(6, MOD - 2);
        let row_diff = ((m % MOD)
            * ((m - 1) % MOD) % MOD
            * ((m + 1) % MOD) % MOD
            * inv6 % MOD)
            % MOD;
        let col_diff = ((n % MOD)
            * ((n - 1) % MOD) % MOD
            * ((n + 1) % MOD) % MOD
            * inv6 % MOD)
            % MOD;

        let n_sq = (n % MOD) * (n % MOD) % MOD;
        let m_sq = (m % MOD) * (m % MOD) % MOD;

        let sum_dist = (n_sq * row_diff % MOD + m_sq * col_diff % MOD) % MOD;

        let ans = comb * sum_dist % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; fast modular exponentiation
(define (pow-mod a e)
  (let loop ((base (modulo a MOD)) (exp e) (res 1))
    (if (= exp 0)
        res
        (loop (modulo (* base base) MOD)
              (quotient exp 2)
              (if (odd? exp)
                  (modulo (* res base) MOD)
                  res)))))

;; precompute factorials and inverse factorials up to n
(define (precompute-fact n)
  (let ((fact (make-vector (+ n 1) 0))
        (invFact (make-vector (+ n 1) 0)))
    (vector-set! fact 0 1)
    (for ([i (in-range 1 (add1 n))])
      (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
    (vector-set! invFact n (pow-mod (vector-ref fact n) (- MOD 2)))
    (for ([i (in-range n 0 -1)])
      (when (> i 0)
        (vector-set! invFact (- i 1) (modulo (* (vector-ref invFact i) i) MOD))))
    (values fact invFact)))

;; combination n choose r modulo MOD
(define (comb n r fact invFact)
  (if (or (< r 0) (> r n))
      0
      (let* ((fn (vector-ref fact n))
             (fr (vector-ref invFact r))
             (fnr (vector-ref invFact (- n r)))
             (res (modulo (* fn (modulo (* fr fnr) MOD)) MOD)))
        res)))

(define/contract (distance-sum m n k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((N (* m n))
         (values (precompute-fact N))
         (fact (car values))
         (invFact (cadr values))
         (c (comb (- N 2) (- k 2) fact invFact))
         (inv6 (pow-mod 6 (- MOD 2)))
         ;; sum over row differences
         (n2 (modulo (* n n) MOD))
         (m_term (modulo (* (modulo (* m (- m 1)) MOD)
                           (modulo (+ m 1) MOD))
                        MOD))
         (sumx (modulo (* (modulo (* n2 m_term) MOD) inv6) MOD))
         ;; sum over column differences
         (m2 (modulo (* m m) MOD))
         (n_term (modulo (* (modulo (* n (- n 1)) MOD)
                           (modulo (+ n 1) MOD))
                        MOD))
         (sumy (modulo (* (modulo (* m2 n_term) MOD) inv6) MOD))
         (S (modulo (+ sumx sumy) MOD)))
    (modulo (* c S) MOD)))
```

## Erlang

```erlang
-module(solution).
-export([distance_sum/3]).

-define(MOD, 1000000007).

distance_sum(M, N, K) ->
    Mod = ?MOD,
    Total = M * N,
    % compute combination C(Total-2, K-2)
    Comb = comb_mod(Total - 2, K - 2, Mod),
    RowSum = sum_abs_diff(M, Mod),
    ColSum = sum_abs_diff(N, Mod),
    NSq = (N rem Mod) * (N rem Mod) rem Mod,
    MSq = (M rem Mod) * (M rem Mod) rem Mod,
    S = (NSq * RowSum + MSq * ColSum) rem Mod,
    (Comb * S) rem Mod.

comb_mod(N, R, Mod) when R < 0; R > N ->
    0;
comb_mod(N, R, Mod) ->
    FactN = fact_mod(N, Mod),
    InvFactR = inv_fact_mod(R, Mod),
    InvFactNR = inv_fact_mod(N - R, Mod),
    ((FactN * InvFactR) rem Mod * InvFactNR) rem Mod.

fact_mod(0, _) -> 1;
fact_mod(N, Mod) ->
    fact_loop(2, N, 1, Mod).

fact_loop(I, N, Acc, Mod) when I =< N ->
    NewAcc = (Acc * I) rem Mod,
    fact_loop(I + 1, N, NewAcc, Mod);
fact_loop(_, _, Acc, _) -> Acc.

inv_fact_mod(N, Mod) ->
    pow_mod(fact_mod(N, Mod), Mod - 2, Mod).

pow_mod(_Base, 0, _Mod) -> 1;
pow_mod(Base, Exp, Mod) when Exp band 1 =:= 1 ->
    ((Base rem Mod) * pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod)) rem Mod;
pow_mod(Base, Exp, Mod) ->
    pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod).

sum_abs_diff(Len, Mod) when Len =< 1 -> 0;
sum_abs_diff(Len, Mod) ->
    sum_loop(1, Len - 1, 0, Len, Mod).

sum_loop(D, MaxD, Acc, Len, Mod) when D =< MaxD ->
    Term = (D * (Len - D)) rem Mod,
    NewAcc = (Acc + Term) rem Mod,
    sum_loop(D + 1, MaxD, NewAcc, Len, Mod);
sum_loop(_, _, Acc, _, _) -> Acc.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec distance_sum(m :: integer, n :: integer, k :: integer) :: integer
  def distance_sum(m, n, k) do
    total = m * n
    comb_val = comb(total - 2, k - 2)

    sum_m = line_sum(m)
    sum_n = line_sum(n)

    n_sq = rem(rem(n, @mod) * n, @mod)
    m_sq = rem(rem(m, @mod) * m, @mod)

    row_part = rem(n_sq * sum_m, @mod)
    col_part = rem(m_sq * sum_n, @mod)

    s = rem(row_part + col_part, @mod)
    rem(comb_val * s, @mod)
  end

  defp line_sum(l) do
    a = rem(l, @mod)
    b = rem(l - 1, @mod)
    c = rem(l + 1, @mod)
    num = rem(rem(a * b, @mod) * c, @mod)
    inv6 = mod_pow(6, @mod - 2, @mod)
    rem(num * inv6, @mod)
  end

  defp comb(n, r) when r < 0 or r > n, do: 0
  defp comb(n, r) do
    r = min(r, n - r)

    {num, den} =
      Enum.reduce(1..r, {1, 1}, fn i, {a, b} ->
        a = rem(a * (n - r + i), @mod)
        b = rem(b * i, @mod)
        {a, b}
      end)

    inv_den = mod_pow(den, @mod - 2, @mod)
    rem(num * inv_den, @mod)
  end

  defp mod_pow(_base, 0, _mod), do: 1
  defp mod_pow(base, exp, mod) when rem(exp, 2) == 0 do
    half = mod_pow(rem(base * base, mod), div(exp, 2), mod)
    half
  end
  defp mod_pow(base, exp, mod) do
    rem(base * mod_pow(base, exp - 1, mod), mod)
  end
end
```

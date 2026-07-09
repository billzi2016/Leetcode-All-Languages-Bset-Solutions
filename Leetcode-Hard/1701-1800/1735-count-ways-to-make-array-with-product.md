# 1735. Count Ways to Make Array With Product

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    static const int MOD = 1'000'000'007;
public:
    vector<int> waysToFillArray(vector<vector<int>>& queries) {
        int maxN = 0, maxK = 0;
        for (auto &q : queries) {
            maxN = max(maxN, q[0]);
            maxK = max(maxK, q[1]);
        }
        // SPF sieve up to maxK
        vector<int> spf(maxK + 1);
        for (int i = 2; i <= maxK; ++i) {
            if (!spf[i]) {
                for (int j = i; j <= maxK; j += i)
                    if (!spf[j]) spf[j] = i;
            }
        }
        // factorials up to maxN + 30
        int limit = maxN + 30;
        vector<long long> fact(limit + 1), invFact(limit + 1);
        fact[0] = 1;
        for (int i = 1; i <= limit; ++i) fact[i] = fact[i - 1] * i % MOD;
        auto modpow = [&](long long a, long long e) {
            long long r = 1;
            while (e) {
                if (e & 1) r = r * a % MOD;
                a = a * a % MOD;
                e >>= 1;
            }
            return r;
        };
        invFact[limit] = modpow(fact[limit], MOD - 2);
        for (int i = limit; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;

        auto C = [&](int n, int k) -> long long {
            if (k < 0 || k > n) return 0;
            return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
        };

        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &q : queries) {
            int n = q[0];
            int k = q[1];
            long long ways = 1;
            while (k > 1) {
                int p = spf[k];
                int cnt = 0;
                while (k % p == 0) {
                    k /= p;
                    ++cnt;
                }
                ways = ways * C(cnt + n - 1, n - 1) % MOD;
            }
            ans.push_back((int)ways);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int[] spf;
    private long[] fact;
    private long[] invFact;

    public int[] waysToFillArray(int[][] queries) {
        int maxN = 0, maxK = 0;
        for (int[] q : queries) {
            maxN = Math.max(maxN, q[0]);
            maxK = Math.max(maxK, q[1]);
        }
        buildSpf(maxK);
        // exponent of any prime in k <= log2(10000) < 14
        int limit = maxN + 30; // safe upper bound for n + exponent
        precomputeFactorials(limit);

        int[] res = new int[queries.length];
        int idx = 0;
        for (int[] q : queries) {
            int n = q[0];
            int k = q[1];
            long ways = 1L;
            int x = k;
            while (x > 1) {
                int p = spf[x];
                int cnt = 0;
                while (x % p == 0) {
                    x /= p;
                    cnt++;
                }
                ways = ways * nCr(cnt + n - 1, n - 1) % MOD;
            }
            res[idx++] = (int) ways;
        }
        return res;
    }

    private void buildSpf(int max) {
        spf = new int[max + 1];
        for (int i = 2; i <= max; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long) i * i <= max) {
                    for (int j = i * i; j <= max; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }
    }

    private void precomputeFactorials(int n) {
        fact = new long[n + 1];
        invFact = new long[n + 1];
        fact[0] = 1L;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
    }

    private long nCr(int a, int b) {
        if (b < 0 || b > a) return 0L;
        return fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
    }

    private long modPow(long base, long exp) {
        long res = 1L;
        long cur = base % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = res * cur % MOD;
            cur = cur * cur % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        max_n = 0
        max_k = 0
        for n, k in queries:
            if n > max_n:
                max_n = n
            if k > max_k:
                max_k = k

        # sieve for smallest prime factor up to max_k
        limit_spf = max(2, max_k + 1)
        spf = list(range(limit_spf))
        for i in range(2, int(limit_spf ** 0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, limit_spf, step):
                    if spf[j] == j:
                        spf[j] = i

        # maximum exponent sum for any k <= max_k is small; set factorial limit safely
        max_exp_sum = 0
        temp = max_k
        while temp > 1:
            p = spf[temp]
            cnt = 0
            while temp % p == 0:
                temp //= p
                cnt += 1
            max_exp_sum += cnt
        fac_limit = max_n + max_exp_sum + 5

        fact = [1] * (fac_limit)
        for i in range(1, fac_limit):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (fac_limit)
        inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
        for i in range(fac_limit - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        res = []
        for n, k in queries:
            ans = 1
            x = k
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                ways = comb(cnt + n - 1, n - 1)
                ans = ans * ways % MOD
            res.append(ans)
        return res
```

## Python3

```python
class Solution:
    def waysToFillArray(self, queries):
        MOD = 10**9 + 7
        max_n = max(q[0] for q in queries)
        LIMIT = max_n + 15  # enough for n + exponent (exponent <= ~13 for k<=1e4)

        fact = [1] * (LIMIT + 1)
        for i in range(1, LIMIT + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (LIMIT + 1)
        inv_fact[LIMIT] = pow(fact[LIMIT], MOD - 2, MOD)
        for i in range(LIMIT, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        max_k = max(q[1] for q in queries)
        spf = list(range(max_k + 1))
        for i in range(2, int(max_k ** 0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, max_k + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        ans_list = []
        for n, k in queries:
            res = 1
            x = k
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                res = res * comb(cnt + n - 1, n - 1) % MOD
            ans_list.append(res)
        return ans_list
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007
#define MAXK 10000
#define MAXF 20005

static int spf[MAXK + 1];
static long long fact[MAXF];
static long long invFact[MAXF];

static long long modpow(long long a, long long e) {
    long long r = 1;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

static void init(void) {
    for (int i = 0; i <= MAXK; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXK; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXK; j += i)
                if (spf[j] == j) spf[j] = i;
        }
    }
    fact[0] = 1;
    for (int i = 1; i < MAXF; ++i) fact[i] = fact[i - 1] * i % MOD;
    invFact[MAXF - 1] = modpow(fact[MAXF - 1], MOD - 2);
    for (int i = MAXF - 1; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;
}

static long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* waysToFillArray(int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    static int initialized = 0;
    if (!initialized) { init(); initialized = 1; }

    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        int n = queries[i][0];
        int k = queries[i][1];
        long long res = 1;
        int temp = k;
        while (temp > 1) {
            int p = spf[temp];
            int cnt = 0;
            while (temp % p == 0) { temp /= p; ++cnt; }
            res = res * nCr(cnt + n - 1, n - 1) % MOD;
        }
        ans[i] = (int)res;
    }
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    private long[] _fac;
    private long[] _invFac;
    private int[] _spf;

    private void Init(int maxVal)
    {
        _fac = new long[maxVal + 1];
        _invFac = new long[maxVal + 1];
        _fac[0] = 1;
        for (int i = 1; i <= maxVal; i++)
            _fac[i] = _fac[i - 1] * i % MOD;

        _invFac[maxVal] = ModPow(_fac[maxVal], MOD - 2);
        for (int i = maxVal; i > 0; i--)
            _invFac[i - 1] = _invFac[i] * i % MOD;

        int limit = 10000;
        _spf = new int[limit + 1];
        for (int i = 2; i <= limit; i++)
            if (_spf[i] == 0)
                for (int j = i; j <= limit; j += i)
                    if (_spf[j] == 0) _spf[j] = i;
    }

    private long ModPow(long a, long e)
    {
        long res = 1;
        while (e > 0)
        {
            if ((e & 1) == 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }

    private long Comb(int n, int k)
    {
        if (k < 0 || k > n) return 0;
        return _fac[n] * _invFac[k] % MOD * _invFac[n - k] % MOD;
    }

    public int[] WaysToFillArray(int[][] queries)
    {
        int maxN = 0;
        foreach (var q in queries)
            if (q[0] > maxN) maxN = q[0];

        Init(maxN + 20); // enough for n + exponent

        int m = queries.Length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++)
        {
            int n = queries[i][0];
            int k = queries[i][1];
            long ways = 1;
            int temp = k;
            while (temp > 1)
            {
                int p = _spf[temp];
                int cnt = 0;
                while (temp % p == 0)
                {
                    temp /= p;
                    cnt++;
                }
                ways = ways * Comb(cnt + n - 1, n - 1) % MOD;
            }
            ans[i] = (int)ways;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} queries
 * @return {number[]}
 */
var waysToFillArray = function(queries) {
    const MOD = 1000000007n;

    // find max n and max k to size precomputations
    let maxN = 0, maxK = 0;
    for (const [n, k] of queries) {
        if (n > maxN) maxN = n;
        if (k > maxK) maxK = k;
    }

    // sieve smallest prime factor up to maxK
    const spf = new Uint32Array(maxK + 1);
    for (let i = 2; i <= maxK; ++i) {
        if (spf[i] === 0) {
            for (let j = i; j <= maxK; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }

    // factorials up to limit = maxN + max possible exponent (~30)
    const LIMIT = maxN + 30;
    const fact = new Array(LIMIT + 1);
    const invFact = new Array(LIMIT + 1);
    fact[0] = 1n;
    for (let i = 1; i <= LIMIT; ++i) {
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

    invFact[LIMIT] = modPow(fact[LIMIT], MOD - 2n);
    for (let i = LIMIT; i > 0; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    const comb = (a, b) => {
        if (b < 0 || b > a) return 0n;
        return (((fact[a] * invFact[b]) % MOD) * invFact[a - b]) % MOD;
    };

    const answers = [];

    for (const [n, kOrig] of queries) {
        let k = kOrig;
        let ans = 1n;

        while (k > 1) {
            const p = spf[k];
            let cnt = 0;
            while (k % p === 0) {
                k = Math.floor(k / p);
                ++cnt;
            }
            // multiply by C(cnt + n - 1, n - 1)
            ans = (ans * comb(cnt + n - 1, n - 1)) % MOD;
        }

        answers.push(Number(ans));
    }

    return answers;
};
```

## Typescript

```typescript
function waysToFillArray(queries: number[][]): number[] {
    const MOD = 1000000007n;

    // Find maximum n to know how far factorials are needed
    let maxN = 0;
    for (const [n] of queries) if (n > maxN) maxN = n;
    const limit = maxN + 20; // safe margin for exponent additions

    // Pre‑compute factorials and inverse factorials modulo MOD
    const fact: bigint[] = new Array(limit + 1);
    const invFact: bigint[] = new Array(limit + 1);
    fact[0] = 1n;
    for (let i = 1; i <= limit; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    const modPow = (base: bigint, exp: bigint): bigint => {
        let b = base % MOD;
        let e = exp;
        let res = 1n;
        while (e > 0) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    };
    invFact[limit] = modPow(fact[limit], MOD - 2n);
    for (let i = limit; i > 0; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const comb = (a: number, b: number): bigint => {
        if (b < 0 || b > a) return 0n;
        return (((fact[a] * invFact[b]) % MOD) * invFact[a - b]) % MOD;
    };

    // Smallest prime factor sieve up to max k
    let maxK = 0;
    for (const [, k] of queries) if (k > maxK) maxK = k;
    const spf = new Uint32Array(maxK + 1);
    for (let i = 2; i <= maxK; ++i) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= maxK) {
                for (let j = i * i; j <= maxK; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }

    const ans: number[] = [];
    for (const [nOrig, kOrig] of queries) {
        let n = nOrig;
        let k = kOrig;
        let ways = 1n;
        while (k > 1) {
            const p = spf[k];
            let cnt = 0;
            while (k % p === 0) {
                k = Math.floor(k / p);
                ++cnt;
            }
            const a = cnt + n - 1;
            const b = n - 1;
            ways = (ways * comb(a, b)) % MOD;
        }
        ans.push(Number(ways));
    }
    return ans;
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;

    private $fact = [];
    private $invFact = [];
    private $spf = [];

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

    private function comb(int $n, int $k): int {
        if ($k < 0 || $k > $n) return 0;
        $mod = self::MOD;
        $res = $this->fact[$n];
        $res = ($res * $this->invFact[$k]) % $mod;
        $res = ($res * $this->invFact[$n - $k]) % $mod;
        return $res;
    }

    /**
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function waysToFillArray($queries) {
        $maxN = 0;
        foreach ($queries as $q) {
            if ($q[0] > $maxN) $maxN = $q[0];
        }
        $limit = $maxN + 30; // enough for n + max exponent

        // factorials
        $this->fact = array_fill(0, $limit + 1, 1);
        for ($i = 1; $i <= $limit; $i++) {
            $this->fact[$i] = ($this->fact[$i - 1] * $i) % self::MOD;
        }
        // inverse factorials
        $this->invFact = array_fill(0, $limit + 1, 1);
        $this->invFact[$limit] = $this->modPow($this->fact[$limit], self::MOD - 2);
        for ($i = $limit; $i > 0; $i--) {
            $this->invFact[$i - 1] = ($this->invFact[$i] * $i) % self::MOD;
        }

        // smallest prime factor sieve up to 10000
        $maxK = 10000;
        $this->spf = array_fill(0, $maxK + 1, 0);
        for ($i = 2; $i <= $maxK; $i++) {
            if ($this->spf[$i] == 0) {
                $this->spf[$i] = $i;
                if ((int)($i * $i) <= $maxK) {
                    for ($j = $i * $i; $j <= $maxK; $j += $i) {
                        if ($this->spf[$j] == 0) $this->spf[$j] = $i;
                    }
                }
            }
        }

        $result = [];
        foreach ($queries as $q) {
            $n = $q[0];
            $k = $q[1];
            $ans = 1;
            while ($k > 1) {
                $p = $this->spf[$k];
                if ($p == 0) $p = $k; // should not happen, safety
                $cnt = 0;
                while ($k % $p == 0) {
                    $k = intdiv($k, $p);
                    $cnt++;
                }
                $ans = ($ans * $this->comb($cnt + $n - 1, $n - 1)) % self::MOD;
            }
            $result[] = $ans;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func waysToFillArray(_ queries: [[Int]]) -> [Int] {
        var maxN = 0
        var maxK = 0
        for q in queries {
            if q[0] > maxN { maxN = q[0] }
            if q[1] > maxK { maxK = q[1] }
        }

        // smallest prime factor sieve up to maxK
        var spf = [Int](repeating: 0, count: maxK + 1)
        if maxK >= 2 {
            for i in 2...maxK {
                if spf[i] == 0 {
                    spf[i] = i
                    if i * i <= maxK {
                        var j = i * i
                        while j <= maxK {
                            if spf[j] == 0 { spf[j] = i }
                            j += i
                        }
                    }
                }
            }
        }
        if maxK >= 1 { spf[1] = 1 }

        // factorials up to maxN + small buffer (max exponent <= log2(10000) < 14)
        let limit = maxN + 20
        var fact = [Int](repeating: 0, count: limit + 1)
        var invFact = [Int](repeating: 0, count: limit + 1)
        fact[0] = 1
        for i in 1...limit {
            fact[i] = modMul(fact[i - 1], i)
        }
        invFact[limit] = modPow(fact[limit], MOD - 2)
        if limit > 0 {
            for i in stride(from: limit, to: 0, by: -1) {
                invFact[i - 1] = modMul(invFact[i], i)
            }
        }

        func comb(_ n: Int, _ k: Int) -> Int {
            if k < 0 || k > n { return 0 }
            let res = modMul(fact[n], modMul(invFact[k], invFact[n - k]))
            return res
        }

        var results = [Int]()
        for q in queries {
            let n = q[0]
            var k = q[1]
            var ways = 1
            while k > 1 {
                let p = spf[k]
                var cnt = 0
                while k % p == 0 {
                    k /= p
                    cnt += 1
                }
                let add = comb(cnt + n - 1, n - 1)
                ways = modMul(ways, add)
            }
            results.append(ways)
        }
        return results
    }

    private func modMul(_ a: Int, _ b: Int) -> Int {
        return Int((Int64(a) * Int64(b)) % Int64(MOD))
    }

    private func modPow(_ base: Int, _ exp: Int) -> Int {
        var result = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if (e & 1) == 1 {
                result = modMul(result, b)
            }
            b = modMul(b, b)
            e >>= 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    companion object {
        private const val MOD = 1_000_000_007L
        private const val MAX_K = 10000
        private const val LIMIT = 20000

        private val spf = IntArray(MAX_K + 1) { it }
        private val fact = LongArray(LIMIT + 1)
        private val invFact = LongArray(LIMIT + 1)

        init {
            // smallest prime factor sieve
            for (i in 2..MAX_K) {
                if (spf[i] == i) {
                    var j = i * i
                    while (j <= MAX_K) {
                        if (spf[j] == j) spf[j] = i
                        j += i
                    }
                }
            }
            // factorials and inverse factorials
            fact[0] = 1L
            for (i in 1..LIMIT) {
                fact[i] = fact[i - 1] * i % MOD
            }
            invFact[LIMIT] = modPow(fact[LIMIT], MOD - 2)
            for (i in LIMIT downTo 1) {
                invFact[i - 1] = invFact[i] * i % MOD
            }
        }

        private fun modPow(base: Long, exp: Long): Long {
            var b = base % MOD
            var e = exp
            var res = 1L
            while (e > 0) {
                if ((e and 1L) == 1L) res = res * b % MOD
                b = b * b % MOD
                e = e shr 1
            }
            return res
        }

        private fun nCr(n: Int, r: Int): Long {
            if (r < 0 || r > n) return 0L
            return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD
        }
    }

    fun waysToFillArray(queries: Array<IntArray>): IntArray {
        val m = queries.size
        val answer = IntArray(m)
        for (idx in 0 until m) {
            val n = queries[idx][0]
            var k = queries[idx][1]
            var res = 1L
            while (k > 1) {
                val p = spf[k]
                var cnt = 0
                while (k % p == 0) {
                    k /= p
                    cnt++
                }
                // distribute cnt identical prime factors into n slots
                val comb = nCr(cnt + n - 1, n - 1)
                res = res * comb % MOD
            }
            answer[idx] = res.toInt()
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  static const int _MOD = 1000000007;

  List<int> waysToFillArray(List<List<int>> queries) {
    int maxN = 0;
    int maxK = 0;
    for (var q in queries) {
      if (q[0] > maxN) maxN = q[0];
      if (q[1] > maxK) maxK = q[1];
    }

    // Sieve for smallest prime factor up to maxK
    List<int> spf = List.filled(maxK + 1, 0);
    for (int i = 2; i <= maxK; ++i) {
      if (spf[i] == 0) {
        for (int j = i; j <= maxK; j += i) {
          if (spf[j] == 0) spf[j] = i;
        }
      }
    }

    // Determine limit for factorials
    int maxExp = maxK > 1 ? (math.log(maxK) / math.log(2)).floor() : 0;
    int limit = maxN + maxExp + 5;

    List<int> fact = List.filled(limit + 1, 1);
    for (int i = 1; i <= limit; ++i) {
      fact[i] = (fact[i - 1] * i) % _MOD;
    }

    List<int> invFact = List.filled(limit + 1, 1);
    invFact[limit] = _modPow(fact[limit], _MOD - 2);
    for (int i = limit; i > 0; --i) {
      invFact[i - 1] = (invFact[i] * i) % _MOD;
    }

    int comb(int n, int k) {
      if (k < 0 || k > n) return 0;
      return ((fact[n] * invFact[k]) % _MOD * invFact[n - k]) % _MOD;
    }

    List<int> ans = [];
    for (var q in queries) {
      int n = q[0];
      int k = q[1];
      if (k == 1) {
        ans.add(1);
        continue;
      }
      int res = 1;
      int x = k;
      while (x > 1) {
        int p = spf[x];
        int cnt = 0;
        while (x % p == 0) {
          x ~/= p;
          cnt++;
        }
        res = (res * comb(cnt + n - 1, n - 1)) % _MOD;
      }
      ans.add(res);
    }

    return ans;
  }

  int _modPow(int base, int exp) {
    long result = 1;
    long b = base.toLong();
    int e = exp;
    while (e > 0) {
      if ((e & 1) == 1) {
        result = (result * b) % _MOD;
      }
      b = (b * b) % _MOD;
      e >>= 1;
    }
    return result.toInt();
  }
}

// Helper extensions for performance
extension on int {
  long toLong() => this as long;
}
typedef long = int;
```

## Golang

```go
package main

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

func nCr(N, R int, fact, invFact []int64) int64 {
	if R < 0 || R > N {
		return 0
	}
	return fact[N] * invFact[R] % MOD * invFact[N-R] % MOD
}

func waysToFillArray(queries [][]int) []int {
	maxN := 0
	for _, q := range queries {
		if q[0] > maxN {
			maxN = q[0]
		}
	}
	limit := maxN + 30 // enough for exponent addition
	fact := make([]int64, limit+1)
	invFact := make([]int64, limit+1)
	fact[0] = 1
	for i := 1; i <= limit; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[limit] = modPow(fact[limit], MOD-2)
	for i := limit; i > 0; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}

	res := make([]int, len(queries))
	for idx, q := range queries {
		n := q[0]
		k := q[1]
		ans := int64(1)
		tmp := k
		for p := 2; p*p <= tmp; p++ {
			if tmp%p == 0 {
				cnt := 0
				for tmp%p == 0 {
					cnt++
					tmp /= p
				}
				comb := nCr(cnt+n-1, n-1, fact, invFact)
				ans = ans * comb % MOD
			}
		}
		if tmp > 1 { // remaining prime factor with exponent 1
			comb := nCr(1+n-1, n-1, fact, invFact)
			ans = ans * comb % MOD
		}
		res[idx] = int(ans)
	}
	return res
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e, mod)
  res = 1
  a %= mod
  while e > 0
    res = res * a % mod if (e & 1) == 1
    a = a * a % mod
    e >>= 1
  end
  res
end

# @param {Integer[][]} queries
# @return {Integer[]}
def ways_to_fill_array(queries)
  max_n = 0
  max_k = 0
  queries.each do |q|
    n, k = q[0], q[1]
    max_n = n if n > max_n
    max_k = k if k > max_k
  end

  # maximum exponent of any prime in max_k (worst case)
  max_exp = 0
  temp = max_k
  p = 2
  while p * p <= temp
    if temp % p == 0
      cnt = 0
      while temp % p == 0
        temp /= p
        cnt += 1
      end
      max_exp = cnt if cnt > max_exp
    end
    p += (p == 2 ? 1 : 2)
  end
  max_exp = [max_exp, 1].max if temp > 1

  limit = max_n + max_exp + 5

  fact = Array.new(limit + 1, 1)
  (1..limit).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact = Array.new(limit + 1, 1)
  inv_fact[limit] = mod_pow(fact[limit], MOD - 2, MOD)
  (limit - 1).downto(0) { |i| inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD }

  comb = lambda do |n, k|
    return 0 if k < 0 || k > n
    fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
  end

  answers = []
  queries.each do |q|
    n, k = q[0], q[1]
    ans = 1
    kk = k
    p = 2
    while p * p <= kk
      if kk % p == 0
        cnt = 0
        while kk % p == 0
          kk /= p
          cnt += 1
        end
        ans = ans * comb.call(cnt + n - 1, n - 1) % MOD
      end
      p += (p == 2 ? 1 : 2)
    end
    if kk > 1
      ans = ans * comb.call(1 + n - 1, n - 1) % MOD
    end
    answers << ans
  end
  answers
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L

    private def modPow(a: Long, e: Long): Long = {
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

    def waysToFillArray(queries: Array[Array[Int]]): Array[Int] = {
        val maxN = queries.map(_(0)).max
        val MAX = maxN + 20 // enough for exponent addition

        val fact = new Array[Long](MAX + 1)
        val invFact = new Array[Long](MAX + 1)
        fact(0) = 1L
        for (i <- 1 to MAX) fact(i) = fact(i - 1) * i % MOD
        invFact(MAX) = modPow(fact(MAX), MOD - 2)
        for (i <- MAX until 0 by -1) {
            if (i > 0) invFact(i - 1) = invFact(i) * i % MOD
        }

        // smallest prime factor up to 10000
        val limitK = 10000
        val spf = new Array[Int](limitK + 1)
        for (i <- 2 to limitK) {
            if (spf(i) == 0) {
                var j = i
                while (j <= limitK) {
                    if (spf(j) == 0) spf(j) = i
                    j += i
                }
            }
        }

        def comb(a: Int, b: Int): Long = {
            if (b < 0 || b > a) 0L
            else fact(a) * invFact(b) % MOD * invFact(a - b) % MOD
        }

        val ans = new Array[Int](queries.length)
        for (idx <- queries.indices) {
            val n = queries(idx)(0)
            var k = queries(idx)(1)
            var ways = 1L
            while (k > 1) {
                val p = spf(k)
                var cnt = 0
                while (k % p == 0) {
                    cnt += 1
                    k /= p
                }
                ways = ways * comb(cnt + n - 1, n - 1) % MOD
            }
            ans(idx) = ways.toInt
        }
        ans
    }
}
```

## Rust

```rust
use std::cmp::max;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res = 1i64;
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
    pub fn ways_to_fill_array(queries: Vec<Vec<i32>>) -> Vec<i32> {
        // find maximum n to size factorial tables
        let mut max_n = 0usize;
        for q in &queries {
            max_n = max(max_n, q[0] as usize);
        }
        // exponent of any prime factor of k (k <= 1e4) is at most ~14,
        // add some margin.
        let limit = max_n + 100;

        // precompute factorials and inverse factorials
        let mut fact: Vec<i64> = vec![1; limit + 1];
        for i in 1..=limit {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact: Vec<i64> = vec![1; limit + 1];
        inv_fact[limit] = mod_pow(fact[limit], MOD - 2);
        for i in (1..=limit).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }

        let mut answers: Vec<i32> = Vec::with_capacity(queries.len());

        for q in queries {
            let n = q[0] as usize;
            let mut k = q[1];
            let mut ans: i64 = 1;

            // factorize k
            let mut p = 2;
            while (p * p) <= k {
                if k % p == 0 {
                    let mut cnt = 0;
                    while k % p == 0 {
                        k /= p;
                        cnt += 1;
                    }
                    // combination C(cnt + n - 1, n - 1)
                    let a = cnt as usize + n - 1;
                    let b = n - 1;
                    let comb = fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD;
                    ans = ans * comb % MOD;
                }
                p += 1;
            }
            if k > 1 {
                // remaining prime factor with exponent 1
                let cnt = 1usize;
                let a = cnt + n - 1;
                let b = n - 1;
                let comb = fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD;
                ans = ans * comb % MOD;
            }

            answers.push(ans as i32);
        }

        answers
    }
}
```

## Racket

```racket
#lang racket

(define MOD 1000000007)

;; modular exponentiation
(define (pow-mod a b)
  (let loop ((base (modulo a MOD)) (exp b) (res 1))
    (if (= exp 0)
        res
        (loop (modulo (* base base) MOD)
              (arithmetic-shift exp -1)
              (if (odd? exp) (modulo (* res base) MOD) res)))))

;; prime factor exponents of n (n >= 2)
(define (prime-exponents n)
  (let ((exps '()))
    (let loop ((i 2) (num n))
      (cond
        [(> (* i i) num)
         (when (> num 1) (set! exps (cons 1 exps)))
         (reverse exps)]
        [else
         (if (= (remainder num i) 0)
             (let count ((cnt 0) (x num))
               (if (= (remainder x i) 0)
                   (count (+ cnt 1) (/ x i))
                   (begin
                     (set! exps (cons cnt exps))
                     (loop (+ i 1) x))))
             (loop (+ i 1) num))]))))

;; nCr modulo MOD using precomputed factorials
(define fact #f)
(define invfact #f)

(define (prepare-factorials limit)
  (set! fact (make-vector (+ limit 1) 0))
  (set! invfact (make-vector (+ limit 1) 0))
  (vector-set! fact 0 1)
  (for ([i (in-range 1 (+ limit 1))])
    (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
  (vector-set! invfact limit (pow-mod (vector-ref fact limit) (- MOD 2)))
  (for ([i (in-range (- limit 1) -1 -1)])
    (vector-set! invfact i
                 (modulo (* (vector-ref invfact (+ i 1)) (+ i 1)) MOD))))

(define (nCr a b)
  (if (or (< b 0) (> b a))
      0
      (let* ((fa (vector-ref fact a))
             (fb (vector-ref invfact b))
             (facb (vector-ref invfact (- a b)))
             (res (modulo (* fa (modulo (* fb facb) MOD)) MOD)))
        res)))

(define/contract (ways-to-fill-array queries)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((max-limit
          (let loop ((qs queries) (mx 0))
            (if (null? qs)
                mx
                (let* ((pair (car qs))
                       (n (first pair))
                       (k (second pair))
                       (exps (if (= k 1) '() (prime-exponents k))))
                  (for ([e exps])
                    (set! mx (max mx (+ n e -1))))
                  (loop (cdr qs) mx)))))
         )
    (prepare-factorials max-limit)
    (let process ((qs queries) (acc '()))
      (if (null? qs)
          (reverse acc)
          (let* ((pair (car qs))
                 (n (first pair))
                 (k (second pair))
                 (exps (if (= k 1) '() (prime-exponents k)))
                 (ans
                  (foldl (lambda (e cur)
                           (modulo (* cur (nCr (+ n e -1) (- n 1))) MOD))
                         1 exps)))
            (process (cdr qs) (cons ans acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([ways_to_fill_array/1]).

-define(MOD, 1000000007).

ways_to_fill_array(Queries) ->
    MaxN = max_n(Queries),
    MaxK = max_k(Queries),
    SPF = build_spf(MaxK),
    MaxExp = max_exponent(MaxK),
    Limit = MaxN + MaxExp,
    {FactTuple, InvFactTuple} = precompute_factorials(Limit),
    lists:map(fun([N, K]) ->
        Exps = factorize(K, SPF),
        compute_answer(N, Exps, FactTuple, InvFactTuple)
    end, Queries).

max_n(Queries) ->
    lists:max([N || [N,_] <- Queries]).

max_k(Queries) ->
    lists:max([K || [_ ,K] <- Queries]).

max_exponent(K) when K =< 1 -> 0;
max_exponent(K) ->
    max_exponent(K, 0).
max_exponent(1, Acc) -> Acc;
max_exponent(N, Acc) -> max_exponent(N div 2, Acc + 1).

build_spf(Max) ->
    SPFList = lists:duplicate(Max + 1, 0),
    SPFArray = list_to_tuple(SPFList),
    build_spf(2, Max, SPFArray).

build_spf(I, Max, SPF) when I > Max -> SPF;
build_spf(I, Max, SPF) ->
    case element(I+1, SPF) of
        0 ->
            NewSPF = set_elem(I+1, I, SPF),
            UpdatedSPF = mark_multiples(I*I, I, Max, NewSPF),
            build_spf(I + 1, Max, UpdatedSPF);
        _Other ->
            build_spf(I + 1, Max, SPF)
    end.

mark_multiples(J, Step, Max, SPF) when J > Max -> SPF;
mark_multiples(J, Step, Max, SPF) ->
    case element(J+1, SPF) of
        0 ->
            NewSPF = set_elem(J+1, Step, SPF),
            mark_multiples(J + Step, Step, Max, NewSPF);
        _ ->
            mark_multiples(J + Step, Step, Max, SPF)
    end.

set_elem(Index, Value, Tuple) ->
    erlang:setelement(Index, Tuple, Value).

factorize(1, _SPF) -> [];
factorize(K, SPF) ->
    factorize(K, SPF, []).

factorize(1, _SPF, Acc) -> lists:reverse(Acc);
factorize(N, SPF, Acc) ->
    P = element(N+1, SPF),
    {Cnt, Rest} = count_power(N, P, 0),
    factorize(Rest, SPF, [Cnt | Acc]).

count_power(N, P, Cnt) when N rem P =:= 0 ->
    count_power(N div P, P, Cnt + 1);
count_power(N, _P, Cnt) -> {Cnt, N}.

precompute_factorials(Limit) ->
    FactList = build_fact_list(Limit, []),
    FactTuple = list_to_tuple(FactList),
    InvFactLast = mod_pow(element(Limit+1, FactTuple), ?MOD-2),
    InvFactList = build_inv_fact_list(Limit, InvFactLast, []),
    InvFactTuple = list_to_tuple(InvFactList),
    {FactTuple, InvFactTuple}.

build_fact_list(-1, Acc) -> lists:reverse([1 | Acc]); % include 0!
build_fact_list(I, Acc) ->
    Prev = case Acc of
        [] -> 1;
        [PrevVal | _] -> PrevVal
    end,
    Cur = (Prev * (I+1)) rem ?MOD,
    build_fact_list(I-1, [Cur | Acc]).

build_inv_fact_list(-1, _, Acc) -> lists:reverse([1 | Acc]); % include 0!
build_inv_fact_list(I, NextInv, Acc) ->
    Cur = (NextInv * (I+1)) rem ?MOD,
    build_inv_fact_list(I-1, Cur, [NextInv | Acc]).

mod_pow(_Base, 0) -> 1;
mod_pow(Base, Exp) when Exp band 1 =:= 1 ->
    ((Base rem ?MOD) * mod_pow((Base*Base) rem ?MOD, Exp bsr 1)) rem ?MOD;
mod_pow(Base, Exp) ->
    mod_pow((Base*Base) rem ?MOD, Exp bsr 1).

compute_answer(N, Exps, FactTuple, InvFactTuple) ->
    compute_answer(Exps, N, FactTuple, InvFactTuple, 1).

compute_answer([], _N, _Fact, _InvFact, Acc) -> Acc;
compute_answer([E|Rest], N, Fact, InvFact, Acc) ->
    Comb = nCr(E + N - 1, N - 1, Fact, InvFact),
    NewAcc = (Acc * Comb) rem ?MOD,
    compute_answer(Rest, N, Fact, InvFact, NewAcc).

nCr(N, K, Fact, InvFact) when K < 0; K > N -> 0;
nCr(N, K, Fact, InvFact) ->
    F_N = element(N+1, Fact),
    F_K = element(K+1, InvFact),
    F_NK = element(N-K+1, InvFact),
    ((F_N * F_K) rem ?MOD * F_NK) rem ?MOD.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec ways_to_fill_array(queries :: [[integer]]) :: [integer]
  def ways_to_fill_array(queries) do
    mod = 1_000_000_007

    max_n =
      queries
      |> Enum.map(&hd/1)
      |> Enum.max()

    limit = max_n + 30

    fact = precompute_fact(limit, mod)
    inv_fact = precompute_inv_fact(fact, limit, mod)

    Enum.map(queries, fn [n, k] ->
      if k == 1 do
        1
      else
        factors = factorize(k)

        Enum.reduce(factors, 1, fn {_p, cnt}, acc ->
          comb_val = comb(cnt + n - 1, n - 1, fact, inv_fact, mod)
          rem(acc * comb_val, mod)
        end)
      end
    end)
  end

  # factorials as tuple for O(1) access
  defp precompute_fact(limit, mod) do
    fact_rev =
      Enum.reduce(0..limit, [], fn i, acc ->
        if i == 0 do
          [1 | acc]
        else
          prev = hd(acc)
          [rem(prev * i, mod) | acc]
        end
      end)

    List.to_tuple(Enum.reverse(fact_rev))
  end

  defp precompute_inv_fact(fact, limit, mod) do
    inv_list =
      Enum.map(0..limit, fn i ->
        mod_pow(elem(fact, i), mod - 2, mod)
      end)

    List.to_tuple(inv_list)
  end

  defp comb(n, k, fact, inv_fact, mod) when k < 0 or k > n do
    0
  end

  defp comb(n, k, fact, inv_fact, mod) do
    a = elem(fact, n)
    b = elem(inv_fact, k)
    c = elem(inv_fact, n - k)
    rem(rem(a * b, mod) * c, mod)
  end

  # fast modular exponentiation
  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) when exp > 0 do
    half = mod_pow(base, div(exp, 2), mod)
    res = rem(half * half, mod)

    if rem(exp, 2) == 1 do
      rem(res * base, mod)
    else
      res
    end
  end

  # factorization of k (k <= 10^4)
  defp factorize(k) when k > 1, do: do_factor(k, 2, %{})
  defp factorize(_), do: %{}

  defp do_factor(1, _d, acc), do: acc

  defp do_factor(n, d, acc) when d * d > n do
    Map.update(acc, n, 1, &(&1 + 1))
  end

  defp do_factor(n, d, acc) do
    if rem(n, d) == 0 do
      {cnt, rest} = count_divisions(n, d, 0)
      new_acc = Map.put(acc, d, cnt)
      do_factor(rest, d + 1, new_acc)
    else
      do_factor(n, d + 1, acc)
    end
  end

  defp count_divisions(n, d, cnt) do
    if rem(n, d) == 0 do
      count_divisions(div(n, d), d, cnt + 1)
    else
      {cnt, n}
    end
  end
end
```

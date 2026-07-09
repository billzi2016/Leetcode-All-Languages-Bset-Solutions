# 2842. Count K-Subsequences of a String With Maximum Beauty

## Cpp

```cpp
class Solution {
public:
    static const long long MOD = 1000000007LL;
    
    long long modPow(long long a, long long e) {
        long long r = 1 % MOD;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    
    int countKSubsequencesWithMaxBeauty(string s, int k) {
        vector<int> freq(26, 0);
        for (char ch : s) freq[ch - 'a']++;
        
        vector<int> f;
        for (int cnt : freq) if (cnt > 0) f.push_back(cnt);
        int m = f.size();
        if (k > m) return 0;
        
        sort(f.begin(), f.end(), greater<int>());
        int t = f[k - 1];                     // threshold frequency
        long long productHigher = 1;
        int cntHigher = 0;                    // number of chars with freq > t
        for (int val : f) {
            if (val > t) {
                productHigher = productHigher * val % MOD;
                ++cntHigher;
            }
        }
        int totalEqual = 0;                   // chars with freq == t
        for (int val : f) if (val == t) ++totalEqual;
        int need = k - cntHigher;             // how many of the equal-freq chars we must pick
        
        // precompute factorials up to needed size (max 200000 is safe)
        static vector<long long> fact, invFact;
        static bool prepared = false;
        if (!prepared) {
            int N = 200000;
            fact.resize(N + 1);
            invFact.resize(N + 1);
            fact[0] = 1;
            for (int i = 1; i <= N; ++i) fact[i] = fact[i - 1] * i % MOD;
            invFact[N] = modPow(fact[N], MOD - 2);
            for (int i = N; i >= 1; --i) invFact[i - 1] = invFact[i] * i % MOD;
            prepared = true;
        }
        auto C = [&](int n, int r) -> long long {
            if (r < 0 || r > n) return 0;
            return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
        };
        
        long long powT = modPow(t, need);
        long long ways = C(totalEqual, need);
        long long ans = ways * productHigher % MOD * powT % MOD;
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final int MAXN = 26; // at most 26 distinct letters

    private long modPow(long base, long exp) {
        long res = 1L;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    private long[] fact = new long[MAXN + 1];
    private long[] invFact = new long[MAXN + 1];

    private void initFactorials() {
        fact[0] = 1L;
        for (int i = 1; i <= MAXN; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }
        invFact[MAXN] = modPow(fact[MAXN], MOD - 2);
        for (int i = MAXN; i > 0; i--) {
            invFact[i - 1] = (invFact[i] * i) % MOD;
        }
    }

    private long nCr(int n, int r) {
        if (r < 0 || r > n) return 0L;
        return (((fact[n] * invFact[r]) % MOD) * invFact[n - r]) % MOD;
    }

    public int countKSubsequencesWithMaxBeauty(String s, int k) {
        initFactorials();

        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }

        // Count distinct characters
        int distinct = 0;
        TreeMap<Integer, Integer> map = new TreeMap<>(Collections.reverseOrder());
        for (int f : freq) {
            if (f > 0) {
                distinct++;
                map.put(f, map.getOrDefault(f, 0) + 1);
            }
        }

        if (k > distinct) return 0;

        long productHigher = 1L;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int val = entry.getKey();
            int cnt = entry.getValue();

            if (k > cnt) {
                // take all characters of this frequency
                productHigher = (productHigher * modPow(val, cnt)) % MOD;
                k -= cnt;
            } else {
                // final group where we select exactly k characters
                long ways = productHigher;
                long comb = nCr(cnt, k);
                long pow = modPow(val, k);
                ways = (ways * comb) % MOD;
                ways = (ways * pow) % MOD;
                return (int) ways;
            }
        }

        // Should never reach here because k <= distinct
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def countKSubsequencesWithMaxBeauty(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        from collections import Counter
        freq_counter = Counter(s)
        freqs = list(freq_counter.values())
        distinct = len(freqs)
        if k > distinct:
            return 0

        freqs.sort(reverse=True)
        threshold = freqs[k - 1]

        cnt_higher = sum(1 for f in freqs if f > threshold)
        cnt_equal = sum(1 for f in freqs if f == threshold)

        need = k - cnt_higher  # number to pick among those equal to threshold

        # product of frequencies strictly greater than threshold
        prod_higher = 1
        for f in freqs:
            if f > threshold:
                prod_higher = (prod_higher * f) % MOD

        # compute combination C(cnt_equal, need)
        max_n = cnt_equal
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
        for i in range(max_n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        comb = fact[cnt_equal] * inv_fact[need] % MOD * inv_fact[cnt_equal - need] % MOD

        ans = comb
        ans = ans * prod_higher % MOD
        ans = ans * pow(threshold, need, MOD) % MOD
        return ans
```

## Python3

```python
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        from collections import Counter

        freq_counter = Counter(s)
        distinct = len(freq_counter)
        if distinct < k:
            return 0

        freqs = sorted(freq_counter.values(), reverse=True)

        threshold = freqs[k - 1]
        # count how many have frequency > threshold and == threshold
        greater_cnt = sum(1 for f in freqs if f > threshold)
        equal_cnt = sum(1 for f in freqs if f == threshold)

        need = k - greater_cnt  # number to pick among those with freq == threshold

        # product of frequencies that are strictly greater than threshold
        prod = 1
        for f in freqs:
            if f > threshold:
                prod = (prod * f) % MOD
            else:
                break

        # precompute factorials up to distinct (max 26) but use length of s for safety
        max_n = len(s)
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        for i in range(2, max_n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
        for i in range(max_n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        comb = nCr(equal_cnt, need)
        prod = prod * pow(threshold, need, MOD) % MOD
        ans = prod * comb % MOD
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const long long MOD = 1000000007LL;

static long long modPow(long long a, long long e) {
    long long res = 1 % MOD;
    a %= MOD;
    while (e > 0) {
        if (e & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return res;
}

int countKSubsequencesWithMaxBeauty(char* s, int k) {
    int freq[26] = {0};
    for (char* p = s; *p; ++p) freq[*p - 'a']++;
    
    vector<int> fvec;
    for (int i = 0; i < 26; ++i) if (freq[i] > 0) fvec.push_back(freq[i]);
    int distinct = (int)fvec.size();
    if (k > distinct) return 0;
    
    sort(fvec.begin(), fvec.end(), greater<int>());
    int threshold = fvec[k - 1];
    
    int cntThresh = 0, higherCnt = 0;
    long long productHigh = 1;
    for (int v : fvec) {
        if (v > threshold) {
            ++higherCnt;
            productHigh = (productHigh * v) % MOD;
        } else if (v == threshold) {
            ++cntThresh;
        }
    }
    
    int needFromThresh = k - higherCnt; // r
    // precompute factorials up to 26
    static long long fact[27], invFact[27];
    fact[0] = 1;
    for (int i = 1; i <= 26; ++i) fact[i] = fact[i-1] * i % MOD;
    invFact[26] = modPow(fact[26], MOD - 2);
    for (int i = 26; i >= 1; --i) invFact[i-1] = invFact[i] * i % MOD;
    
    auto comb = [&](int n, int r)->long long{
        if (r < 0 || r > n) return 0LL;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    };
    
    long long waysThresh = comb(cntThresh, needFromThresh);
    long long powPart = modPow(threshold, needFromThresh);
    
    long long ans = productHigh;
    ans = ans * waysThresh % MOD;
    ans = ans * powPart % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1_000_000_007L;
    private static long ModPow(long a, long e) {
        long res = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) == 1) res = (res * a) % MOD;
            a = (a * a) % MOD;
            e >>= 1;
        }
        return res;
    }

    private static long[] fact;
    private static long[] invFact;

    private static void InitFactorials(int n) {
        fact = new long[n + 1];
        invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = ModPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
    }

    private static long NCr(int n, int r) {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    }

    public int CountKSubsequencesWithMaxBeauty(string s, int k) {
        int[] freq = new int[26];
        foreach (char ch in s) freq[ch - 'a']++;

        // Map frequency -> count of characters having that frequency
        var map = new SortedDictionary<int, int>(Comparer<int>.Create((x, y) => y.CompareTo(x)));
        int distinct = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                distinct++;
                if (!map.ContainsKey(freq[i])) map[freq[i]] = 0;
                map[freq[i]]++;
            }
        }

        if (k > distinct) return 0;

        InitFactorials(distinct); // at most 26, safe

        long ans = 1;
        int remaining = k;

        foreach (var kvp in map) {
            int f = kvp.Key;
            int cnt = kvp.Value;
            if (remaining == 0) break;

            if (remaining <= cnt) {
                // choose 'remaining' characters from this group
                long ways = NCr(cnt, remaining);
                ans = ans * ModPow(f, remaining) % MOD;
                ans = ans * ways % MOD;
                remaining = 0;
                break;
            } else {
                // take all characters of this frequency
                ans = ans * ModPow(f, cnt) % MOD;
                remaining -= cnt;
            }
        }

        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var countKSubsequencesWithMaxBeauty = function(s, k) {
    const MOD = 1000000007n;
    // frequency of each character
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        freq[s.charCodeAt(i) - 97]++;
    }
    let distinct = 0;
    for (const f of freq) if (f > 0) distinct++;
    if (k > distinct) return 0;

    // map frequency -> count of characters having that frequency
    const cntMap = new Map();
    for (const f of freq) {
        if (f === 0) continue;
        cntMap.set(f, (cntMap.get(f) || 0) + 1);
    }

    const freqsDesc = Array.from(cntMap.keys()).sort((a, b) => b - a);

    // modular exponentiation
    const modPow = (base, exp) => {
        let b = BigInt(base) % MOD;
        let e = BigInt(exp);
        let res = 1n;
        while (e > 0n) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    };

    // precompute factorials up to max count of characters sharing same frequency
    const maxCnt = Math.max(...cntMap.values());
    const fact = new Array(maxCnt + 1);
    const invFact = new Array(maxCnt + 1);
    fact[0] = 1n;
    for (let i = 1; i <= maxCnt; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    invFact[maxCnt] = modPow(fact[maxCnt], MOD - 2n);
    for (let i = maxCnt; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const comb = (n, r) => {
        if (r < 0 || r > n) return 0n;
        return (((fact[n] * invFact[r]) % MOD) * invFact[n - r]) % MOD;
    };

    let remaining = k;
    let ans = 1n;

    for (const f of freqsDesc) {
        const cnt = cntMap.get(f);
        if (remaining === 0) break;
        if (remaining >= cnt) {
            // take all characters with this frequency
            ans = (ans * modPow(f, cnt)) % MOD;
            remaining -= cnt;
        } else {
            // need only part of this group
            const r = remaining;
            ans = (ans * comb(cnt, r)) % MOD;
            ans = (ans * modPow(f, r)) % MOD;
            remaining = 0;
            break;
        }
    }

    return Number(ans);
};
```

## Typescript

```typescript
function countKSubsequencesWithMaxBeauty(s: string, k: number): number {
    const MOD = 1000000007n;

    // Count frequencies of each character
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    // Collect non‑zero frequencies
    const freqs: number[] = [];
    for (const f of freq) if (f > 0) freqs.push(f);

    const distinct = freqs.length;
    if (k > distinct) return 0;

    // Sort descending
    freqs.sort((a, b) => b - a);
    const threshold = freqs[k - 1];

    // Count frequencies greater than threshold and their product
    let cntHigher = 0;
    let prodHigher = 1n;
    for (const f of freqs) {
        if (f > threshold) {
            cntHigher++;
            prodHigher = (prodHigher * BigInt(f)) % MOD;
        } else break; // sorted, no more greater values
    }

    const cntEqual = freqs.filter(v => v === threshold).length;
    const needFromEqual = k - cntHigher; // r

    // Pre‑compute factorials up to cntEqual (max 26)
    const maxN = cntEqual;
    const fact: bigint[] = new Array(maxN + 1);
    const invFact: bigint[] = new Array(maxN + 1);
    fact[0] = 1n;
    for (let i = 1; i <= maxN; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    const modPow = (base: bigint | number, exp: bigint | number): bigint => {
        let b = BigInt(base) % MOD;
        let e = BigInt(exp);
        let res = 1n;
        while (e > 0) {
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

    const comb = ((fact[cntEqual] * invFact[needFromEqual]) % MOD * invFact[cntEqual - needFromEqual]) % MOD;
    const powThresh = modPow(threshold, needFromEqual);

    let ans = prodHigher;
    ans = (ans * comb) % MOD;
    ans = (ans * powThresh) % MOD;

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

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function countKSubsequencesWithMaxBeauty($s, $k) {
        $mod = self::MOD;
        $freq = array_fill(0, 26, 0);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }

        $freqList = [];
        foreach ($freq as $f) {
            if ($f > 0) {
                $freqList[] = $f;
            }
        }

        $distinct = count($freqList);
        if ($k > $distinct) {
            return 0;
        }

        rsort($freqList); // descending
        $threshold = $freqList[$k - 1];

        $cnt_eq = 0;
        $numHigher = 0;
        $productHigher = 1;

        foreach ($freqList as $f) {
            if ($f > $threshold) {
                $numHigher++;
                $productHigher = ($productHigher * $f) % $mod;
            } elseif ($f == $threshold) {
                $cnt_eq++;
            }
        }

        $need = $k - $numHigher; // number to pick from equal-frequency group

        // precompute factorials up to cnt_eq (max 26)
        $maxN = $cnt_eq;
        $fact = array_fill(0, $maxN + 1, 0);
        $invFact = array_fill(0, $maxN + 1, 0);
        $fact[0] = 1;
        for ($i = 1; $i <= $maxN; $i++) {
            $fact[$i] = ($fact[$i - 1] * $i) % $mod;
        }
        $invFact[$maxN] = $this->modPow($fact[$maxN], $mod - 2);
        for ($i = $maxN; $i >= 1; $i--) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % $mod;
        }

        if ($need < 0 || $need > $cnt_eq) {
            return 0;
        }
        // nCr
        $comb = (($fact[$cnt_eq] * $invFact[$need]) % $mod * $invFact[$cnt_eq - $need]) % $mod;

        $pow_f_t = $this->modPow($threshold, $need);
        $ans = $comb;
        $ans = ($ans * $productHigher) % $mod;
        $ans = ($ans * $pow_f_t) % $mod;

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

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

    func countKSubsequencesWithMaxBeauty(_ s: String, _ k: Int) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        for ch in s.utf8 {
            let idx = Int(ch - 97)   // 'a' ascii = 97
            freq[idx] += 1
        }

        var freqs: [Int] = []
        for f in freq where f > 0 {
            freqs.append(f)
        }

        if k > freqs.count { return 0 }

        freqs.sort(by: >)

        let threshold = freqs[k - 1]
        var cntHigher = 0
        var cntEqual = 0
        for f in freqs {
            if f > threshold {
                cntHigher += 1
            } else if f == threshold {
                cntEqual += 1
            }
        }

        let need = k - cntHigher

        // factorials up to s.count (max 2e5)
        let maxN = s.count
        var fact = [Int](repeating: 0, count: maxN + 1)
        var invFact = [Int](repeating: 0, count: maxN + 1)
        fact[0] = 1
        if maxN > 0 {
            for i in 1...maxN {
                fact[i] = Int((Int64(fact[i - 1]) * Int64(i)) % Int64(MOD))
            }
            invFact[maxN] = modPow(fact[maxN], MOD - 2)
            if maxN > 0 {
                var i = maxN
                while i > 0 {
                    invFact[i - 1] = Int((Int64(invFact[i]) * Int64(i)) % Int64(MOD))
                    i -= 1
                }
            }
        }

        func nCk(_ n: Int, _ k: Int) -> Int {
            if k < 0 || k > n { return 0 }
            let res = Int((Int64(fact[n]) * Int64(invFact[k]) % Int64(MOD)) *
                          Int64(invFact[n - k]) % Int64(MOD))
            return res
        }

        var productHigher = 1
        for i in 0..<cntHigher {
            productHigher = Int((Int64(productHigher) * Int64(freqs[i])) % Int64(MOD))
        }

        let powPart = modPow(threshold, need)
        let comb = nCk(cntEqual, need)

        var ans = Int((Int64(productHigher) * Int64(powPart)) % Int64(MOD))
        ans = Int((Int64(ans) * Int64(comb)) % Int64(MOD))

        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L

    fun countKSubsequencesWithMaxBeauty(s: String, k: Int): Int {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        val list = mutableListOf<Int>()
        for (f in freq) if (f > 0) list.add(f)

        val distinct = list.size
        if (k > distinct) return 0

        list.sortDescending()
        val threshold = list[k - 1]

        var higherCount = 0
        var productHigher = 1L
        for (v in list) {
            if (v > threshold) {
                higherCount++
                productHigher = productHigher * v % MOD
            } else break
        }

        val cntTotal = list.count { it == threshold }
        val need = k - higherCount

        val comb = nCr(cntTotal, need)
        val powThresh = modPow(threshold.toLong(), need.toLong())

        var ans = comb * productHigher % MOD
        ans = ans * powThresh % MOD
        return ans.toInt()
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
        val fact = LongArray(n + 1)
        val invFact = LongArray(n + 1)
        fact[0] = 1L
        for (i in 1..n) fact[i] = fact[i - 1] * i % MOD
        invFact[n] = modPow(fact[n], MOD - 2)
        for (i in n downTo 1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;

  int countKSubsequencesWithMaxBeauty(String s, int k) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; ++i) {
      freq[s.codeUnitAt(i) - 97]++;
    }
    List<int> freqs = [];
    for (int f in freq) if (f > 0) freqs.add(f);
    int distinct = freqs.length;
    if (k > distinct) return 0;

    freqs.sort((a, b) => b.compareTo(a)); // descending
    int X = freqs[k - 1];
    int cntHigher = 0;
    for (int f in freqs) {
      if (f > X) cntHigher++;
    }
    int need = k - cntHigher; // how many we must take from frequency == X
    int totX = 0;
    for (int f in freqs) if (f == X) totX++;

    int prodHigher = 1;
    for (int f in freqs) {
      if (f > X) prodHigher = (prodHigher * f) % MOD;
    }

    int comb = _nCr(totX, need);
    int powPart = _modPow(X, need);
    return ((prodHigher * comb) % MOD * powPart) % MOD;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % MOD;
    while (exp > 0) {
      if ((exp & 1) == 1) result = (result * b) % MOD;
      b = (b * b) % MOD;
      exp >>= 1;
    }
    return result;
  }

  int _nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    List<int> fac = List.filled(n + 1, 1);
    for (int i = 1; i <= n; ++i) fac[i] = (fac[i - 1] * i) % MOD;
    int invFacR = _modPow(fac[r], MOD - 2);
    int invFacNR = _modPow(fac[n - r], MOD - 2);
    return ((fac[n] * invFacR) % MOD * invFacNR) % MOD;
  }
}
```

## Golang

```go
package main

import (
	"sort"
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

func countKSubsequencesWithMaxBeauty(s string, k int) int {
	freq := make([]int, 26)
	for _, ch := range s {
		freq[ch-'a']++
	}
	var freqs []int
	for _, f := range freq {
		if f > 0 {
			freqs = append(freqs, f)
		}
	}
	m := len(freqs)
	if k > m {
		return 0
	}
	sort.Slice(freqs, func(i, j int) bool { return freqs[i] > freqs[j] })
	x := freqs[k-1]

	cntHigher := 0
	var productHigher int64 = 1
	for _, f := range freqs {
		if f > x {
			cntHigher++
			productHigher = productHigher * int64(f) % MOD
		} else {
			break
		}
	}
	r := k - cntHigher

	totalX := 0
	for _, f := range freq {
		if f == x {
			totalX++
		}
	}

	maxN := 26
	fact := make([]int64, maxN+1)
	invFact := make([]int64, maxN+1)
	fact[0] = 1
	for i := 1; i <= maxN; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[maxN] = modPow(fact[maxN], MOD-2)
	for i := maxN - 1; i >= 0; i-- {
		invFact[i] = invFact[i+1] * int64(i+1) % MOD
	}
	comb := func(n, k int) int64 {
		if k < 0 || k > n {
			return 0
		}
		return fact[n] * invFact[k] % MOD * invFact[n-k] % MOD
	}

	waysChoose := comb(totalX, r)
	powx := modPow(int64(x), int64(r))
	ans := productHigher * waysChoose % MOD * powx % MOD
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e, mod)
  res = 1
  a %= mod
  while e > 0
    res = (res * a) % mod if (e & 1) == 1
    a = (a * a) % mod
    e >>= 1
  end
  res
end

def count_k_subsequences_with_max_beauty(s, k)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  freqs = freq.select { |c| c > 0 }
  m = freqs.length
  return 0 if k > m

  sorted = freqs.sort.reverse
  x = sorted[k - 1]

  cnt_gt = 0
  total_eq = 0
  product_big = 1
  freqs.each do |f|
    if f > x
      cnt_gt += 1
      product_big = (product_big * f) % MOD
    elsif f == x
      total_eq += 1
    end
  end

  r = k - cnt_gt
  max_n = total_eq
  fact = Array.new(max_n + 1, 1)
  (1..max_n).each { |i| fact[i] = (fact[i - 1] * i) % MOD }
  inv_fact = Array.new(max_n + 1, 1)
  inv_fact[max_n] = mod_pow(fact[max_n], MOD - 2, MOD)
  (max_n - 1).downto(0) { |i| inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD }

  comb = fact[total_eq]
  comb = (comb * inv_fact[r]) % MOD
  comb = (comb * inv_fact[total_eq - r]) % MOD

  pow_x_r = mod_pow(x, r, MOD)
  ans = product_big
  ans = (ans * comb) % MOD
  ans = (ans * pow_x_r) % MOD
  ans
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

    def countKSubsequencesWithMaxBeauty(s: String, k: Int): Int = {
        val freq = new Array[Int](26)
        for (ch <- s) freq(ch - 'a') += 1

        val list = scala.collection.mutable.ArrayBuffer[Int]()
        for (f <- freq) if (f > 0) list += f

        val distinct = list.length
        if (k > distinct) return 0

        val sorted = list.sorted(Ordering[Int].reverse)
        val threshold = sorted(k - 1)

        var higher = 0
        var atThresh = 0
        for (f <- sorted) {
            if (f > threshold) higher += 1
            else if (f == threshold) atThresh += 1
        }

        val needFromThresh = k - higher // choose this many from the group with frequency == threshold

        // precompute factorials up to atThresh (max 26)
        val maxN = atThresh
        val fact = new Array[Long](maxN + 1)
        val invFact = new Array[Long](maxN + 1)
        fact(0) = 1L
        for (i <- 1 to maxN) fact(i) = fact(i - 1) * i % MOD
        invFact(maxN) = modPow(fact(maxN), MOD - 2)
        for (i <- maxN - 1 to 0 by -1) invFact(i) = invFact(i + 1) * (i + 1) % MOD

        def nCr(n: Int, r: Int): Long = {
            if (r < 0 || r > n) return 0L
            fact(n) * invFact(r) % MOD * invFact(n - r) % MOD
        }

        val ans = nCr(atThresh, needFromThresh)
        (ans % MOD).toInt
    }
}
```

## Rust

```rust
use std::cmp::Ordering;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res = 1i64;
    base %= MOD;
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
    pub fn count_k_subsequences_with_max_beauty(s: String, k: i32) -> i32 {
        let mut cnt = [0i64; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut freqs: Vec<i64> = cnt.iter().cloned().filter(|&x| x > 0).collect();
        let distinct = freqs.len();
        if (k as usize) > distinct {
            return 0;
        }

        // sort descending
        freqs.sort_by(|a, b| b.cmp(a));

        let k_usize = k as usize;
        let threshold = freqs[k_usize - 1];

        // count total_eq and higher
        let mut total_eq = 0usize;
        let mut higher = 0usize;
        for &v in &freqs {
            if v > threshold {
                higher += 1;
            } else if v == threshold {
                total_eq += 1;
            }
        }

        let need = k_usize - higher; // number of chars to pick among those equal to threshold

        // product of frequencies greater than threshold
        let mut prod_high = 1i64;
        for &v in &freqs {
            if v > threshold {
                prod_high = prod_high * (v % MOD) % MOD;
            }
        }

        // compute combination C(total_eq, need)
        let n = total_eq;
        let r = need;
        let mut fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let inv_fact_n = mod_pow(fact[n], MOD - 2);
        let mut inv_fact = vec![1i64; n + 1];
        inv_fact[n] = inv_fact_n;
        for i in (0..n).rev() {
            inv_fact[i] = inv_fact[i + 1] * ((i + 1) as i64) % MOD;
        }
        let comb = fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD;

        // x^need
        let pow_part = if need == 0 {
            1
        } else {
            mod_pow(threshold % MOD, need as i64)
        };

        let ans = comb * prod_high % MOD * pow_part % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-k-subsequences-with-max-beauty s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((MOD 1000000007)
         (freq (make-vector 26 0)))
    ;; count frequencies of each character
    (for ([i (in-range (string-length s))])
      (let* ((ch (char->integer (string-ref s i)))
             (idx (- ch (char->integer #\a))))
        (vector-set! freq idx (+ (vector-ref freq idx) 1))))
    ;; collect non‑zero frequencies
    (define freqs
      (for/list ([i (in-range 26)]
                 #:when (> (vector-ref freq i) 0))
        (vector-ref freq i)))
    (define distinct (length freqs))
    (if (> k distinct)
        0
        (let* ((sorted (sort freqs >))
               (target (list-ref sorted (- k 1))) ; kth largest frequency
               (total-target (for/sum ([f freqs] #:when (= f target)) 1))
               (greater (for/sum ([f freqs] #:when (> f target)) 1))
               (need (- k greater)))
          ;; pre‑compute factorials up to total-target
          (define max-n total-target)
          (define fact (make-vector (+ max-n 1) 1))
          (for ([i (in-range 1 (+ max-n 1))])
            (vector-set! fact i (remainder (* (vector-ref fact (- i 1)) i) MOD)))
          ;; modular exponentiation
          (define (modpow a e)
            (let loop ((base (remainder a MOD)) (exp e) (res 1))
              (if (= exp 0)
                  res
                  (loop (remainder (* base base) MOD)
                        (quotient exp 2)
                        (if (= (remainder exp 2) 1)
                            (remainder (* res base) MOD)
                            res)))))
          (define (modinv a) (modpow a (- MOD 2)))
          ;; inverse factorials
          (define invfact (make-vector (+ max-n 1) 1))
          (vector-set! invfact max-n (modinv (vector-ref fact max-n)))
          (for ([i (in-range (- max-n 1) -1 -1)])
            (vector-set! invfact i (remainder (* (vector-ref invfact (+ i 1)) (+ i 1)) MOD)))
          ;; combination modulo MOD
          (define (comb n k)
            (if (or (< k 0) (> k n))
                0
                (remainder (* (vector-ref fact n)
                              (remainder (* (vector-ref invfact k)
                                            (vector-ref invfact (- n k))) MOD))
                          MOD)))
          (comb total-target need))))))
```

## Erlang

```erlang
-module(solution).
-export([count_k_subsequences_with_max_beauty/2]).

-define(MOD, 1000000007).

count_k_subsequences_with_max_beauty(S, K) ->
    Freqs = freq_counts(S),
    Distinct = [F || F <- Freqs, F > 0],
    M = length(Distinct),
    case K > M of
        true -> 0;
        false ->
            Sorted = lists:reverse(lists:sort(Distinct)),
            Cutoff = nth_element(Sorted, K),
            TotalEq = count_eq(Distinct, Cutoff),
            HigherCount = count_higher(Distinct, Cutoff),
            NeedEq = K - HigherCount,
            Fact = factorials(26),
            InvFact = inv_factorials(Fact),
            Comb = comb(TotalEq, NeedEq, Fact, InvFact),
            PowCut = pow_mod(Cutoff, NeedEq, ?MOD),
            ProdHigher = prod_higher(Distinct, Cutoff, ?MOD),
            Ans0 = (Comb * PowCut) rem ?MOD,
            (Ans0 * ProdHigher) rem ?MOD
    end.

freq_counts(S) ->
    List = binary:bin_to_list(S),
    freq_counts(List, lists:duplicate(26, 0)).

freq_counts([], F) -> F;
freq_counts([C|Rest], F) ->
    Index = C - $a,
    Old = lists:nth(Index + 1, F),
    NewVal = Old + 1,
    NewF = set_nth(Index + 1, NewVal, F),
    freq_counts(Rest, NewF).

set_nth(1, Val, [_|Tail]) -> [Val | Tail];
set_nth(N, Val, [H|Tail]) -> [H | set_nth(N - 1, Val, Tail)].

nth_element(List, K) ->
    lists:nth(K, List).

count_eq(Distinct, Cutoff) ->
    length([F || F <- Distinct, F == Cutoff]).

count_higher(Distinct, Cutoff) ->
    length([F || F <- Distinct, F > Cutoff]).

prod_higher(Distinct, Cutoff, Mod) ->
    lists:foldl(fun(F, Acc) ->
        if
            F > Cutoff -> (Acc * (F rem Mod)) rem Mod;
            true -> Acc
        end
    end, 1, Distinct).

factorials(N) ->
    {_, Rev} = lists:foldl(
        fun(I, {Prev, Acc}) ->
            F = (Prev * I) rem ?MOD,
            {F, [F | Acc]}
        end,
        {1, [1]}, % fact(0)=1
        lists:seq(1, N)
    ),
    lists:reverse(Rev).

inv_factorials(Fact) ->
    N = length(Fact) - 1,
    LastFact = lists:nth(N + 1, Fact),
    InvLast = pow_mod(LastFact, ?MOD - 2, ?MOD),
    {InvList, _} = lists:foldl(
        fun(I, {Acc, PrevInv}) ->
            InvPrev = (PrevInv * I) rem ?MOD,
            {[InvPrev | Acc], InvPrev}
        end,
        {[InvLast], InvLast},
        lists:seq(N, 1, -1)
    ),
    InvList.

comb(N, R, Fact, InvFact) when R < 0; R > N -> 0;
comb(N, R, Fact, InvFact) ->
    F = lists:nth(N + 1, Fact),
    FR = lists:nth(R + 1, InvFact),
    FN_R = lists:nth(N - R + 1, InvFact),
    ((F * FR) rem ?MOD * FN_R) rem ?MOD.

pow_mod(_, 0, _) -> 1;
pow_mod(B, E, M) when (E band 1) =:= 1 ->
    (B * pow_mod((B * B) rem M, E bsr 1, M)) rem M;
pow_mod(B, E, M) ->
    pow_mod((B * B) rem M, E bsr 1, M).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_k_subsequences_with_max_beauty(String.t(), integer) :: integer
  def count_k_subsequences_with_max_beauty(s, k) do
    freq_map = Enum.frequencies(String.to_charlist(s))
    freqs = Map.values(freq_map)

    distinct = length(freqs)
    if k > distinct, do: 0, else: compute_answer(freqs, k)
  end

  defp compute_answer(freqs, k) do
    sorted = Enum.sort(freqs, &>=/2)

    val = Enum.at(sorted, k - 1)

    cnt_higher = Enum.count(sorted, fn x -> x > val end)
    total_equal = Enum.count(sorted, fn x -> x == val end)
    r = k - cnt_higher

    product_high =
      Enum.reduce(sorted, 1, fn f, acc ->
        if f > val do
          rem(acc * f, @mod)
        else
          acc
        end
      end)

    ans =
      product_high
      |> mul(mod_pow(val, r))
      |> mul(ncr(total_equal, r))

    ans
  end

  defp mod_pow(_base, 0), do: 1

  defp mod_pow(base, exp) when exp > 0 do
    base = rem(base, @mod)

    if rem(exp, 2) == 1 do
      mul(base, mod_pow(mul(base, base), div(exp - 1, 2)))
    else
      mod_pow(mul(base, base), div(exp, 2))
    end
  end

  defp ncr(n, r) when r < 0 or r > n, do: 0
  defp ncr(_n, 0), do: 1

  defp ncr(n, r) do
    fact_n = fact(n)
    inv_fact_r = mod_pow(fact(r), @mod - 2)
    inv_fact_nr = mod_pow(fact(n - r), @mod - 2)

    fact_n
    |> mul(inv_fact_r)
    |> mul(inv_fact_nr)
  end

  defp fact(0), do: 1

  defp fact(n) when n > 0 do
    Enum.reduce(1..n, 1, fn i, acc -> rem(acc * i, @mod) end)
  end

  defp mul(a, b), do: rem(a * b, @mod)
end
```

# 2851. String Transformation

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const long long MOD = 1000000007LL;
    
    // KMP prefix function
    vector<int> buildLPS(const string& pat) {
        int m = pat.size();
        vector<int> lps(m,0);
        for (int i=1,len=0;i<m;){
            if(pat[i]==pat[len]){
                lps[i++] = ++len;
            }else{
                if(len) len = lps[len-1];
                else lps[i++] = 0;
            }
        }
        return lps;
    }
    
    long long mulmod(long long a,long long b){
        return (a*b)%MOD;
    }
    
    array<array<long long,2>,2> matMul(const array<array<long long,2>,2>& A,
                                      const array<array<long long,2>,2>& B){
        array<array<long long,2>,2> C{};
        for(int i=0;i<2;i++)
            for(int j=0;j<2;j++){
                C[i][j]= (mulmod(A[i][0],B[0][j]) + mulmod(A[i][1],B[1][j]))%MOD;
            }
        return C;
    }
    
    array<array<long long,2>,2> matPow(array<array<long long,2>,2> base, long long exp){
        array<array<long long,2>,2> res{{{{1,0},{0,1}}}};
        while(exp){
            if(exp&1) res = matMul(res,base);
            base = matMul(base,base);
            exp >>= 1;
        }
        return res;
    }
    
    int numberOfWays(string s, string t, long long k) {
        int n = s.size();
        // find all rotations where s rotated by i equals t
        string ss = s + s;
        vector<int> lps = buildLPS(t);
        int i=0,j=0;
        long long cnt=0;
        bool zeroMatch=false;
        while(i < (int)ss.size()){
            if(ss[i]==t[j]){
                ++i; ++j;
                if(j==(int)t.size()){
                    int pos = i - j;
                    if(pos < n){
                        ++cnt;
                        if(pos==0) zeroMatch=true;
                    }
                    j = lps[j-1];
                }
            }else{
                if(j) j = lps[j-1];
                else ++i;
            }
        }
        if(cnt==0) return 0;
        
        // transition matrix
        array<array<long long,2>,2> M{{{{0, (n-1)%MOD},{1, (n-2)%MOD}}}};
        auto Mp = matPow(M,k);
        long long a_k = Mp[0][0]; // ways to be at start after k steps
        long long b_k = Mp[1][0]; // ways to be at any specific non-start node
        
        long long ans = 0;
        if(zeroMatch){
            ans = (ans + a_k) % MOD;
        }
        long long nonZeroCnt = cnt - (zeroMatch?1:0);
        ans = (ans + (nonZeroCnt%MOD) * b_k)%MOD;
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;

    public int numberOfWays(String s, String t, long k) {
        int n = s.length();
        if (k == 0) {
            return s.equals(t) ? 1 : 0;
        }

        // Find all rotation offsets where rotating s yields t
        List<Integer> matchPos = kmpMatches(s + s.substring(0, n - 1), t);
        int totalMatches = 0;
        boolean hasZero = false;
        for (int pos : matchPos) {
            if (pos < n) {
                totalMatches++;
                if (pos == 0) hasZero = true;
            }
        }
        if (totalMatches == 0) return 0;

        // Matrix exponentiation
        long[][] M = new long[2][2];
        M[0][0] = 0;
        M[0][1] = (n - 1) % MOD;
        M[1][0] = 1;
        M[1][1] = (n - 2) % MOD;

        long[][] Mp = matrixPower(M, k);
        long aK = Mp[0][0]; // ways to reach offset 0
        long bK = Mp[1][0]; // ways to reach any specific non-zero offset

        long ans = 0;
        if (hasZero) {
            ans = (ans + aK) % MOD;
        }
        int nonZeroMatches = totalMatches - (hasZero ? 1 : 0);
        ans = (ans + bK * nonZeroMatches) % MOD;

        return (int) ans;
    }

    private List<Integer> kmpMatches(String text, String pattern) {
        int n = pattern.length();
        int[] lps = new int[n];
        // build LPS array
        for (int i = 1, len = 0; i < n; ) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                lps[i++] = ++len;
            } else if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }

        List<Integer> res = new ArrayList<>();
        int i = 0, j = 0;
        int m = text.length();
        while (i < m) {
            if (text.charAt(i) == pattern.charAt(j)) {
                i++; j++;
                if (j == n) {
                    res.add(i - j);
                    j = lps[j - 1];
                }
            } else {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return res;
    }

    private long[][] matrixPower(long[][] base, long exp) {
        long[][] result = new long[2][2];
        result[0][0] = result[1][1] = 1; // identity
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                result = multiply(result, base);
            }
            base = multiply(base, base);
            exp >>= 1;
        }
        return result;
    }

    private long[][] multiply(long[][] A, long[][] B) {
        long[][] C = new long[2][2];
        for (int i = 0; i < 2; i++) {
            for (int k = 0; k < 2; k++) {
                if (A[i][k] == 0) continue;
                long aik = A[i][k];
                for (int j = 0; j < 2; j++) {
                    C[i][j] = (C[i][j] + aik * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfWays(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        if n != len(t):
            return 0

        # KMP prefix function to find all rotations where s becomes t
        pattern = t
        text = s + s[:-1]  # length 2n-1, enough for starts < n
        combined = pattern + "#" + text
        m = len(pattern)
        pi = [0] * len(combined)
        for i in range(1, len(combined)):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j

        offsets = []
        for i in range(m + 1, len(combined)):
            if pi[i] == m:
                offset = i - 2 * m
                if 0 <= offset < n:
                    offsets.append(offset)

        if not offsets:
            return 0

        cnt_zero = 1 if 0 in offsets else 0
        cnt_nonzero = len(offsets) - cnt_zero

        pow_n1 = pow(n - 1, k, MOD)
        sign = 1 if k % 2 == 0 else MOD - 1  # (-1)^k modulo MOD
        inv_n = pow(n, MOD - 2, MOD)

        ways_off = (pow_n1 - sign) % MOD
        ways_off = ways_off * inv_n % MOD

        ways_diag = (pow_n1 + (n - 1) * sign) % MOD
        ways_diag = ways_diag * inv_n % MOD

        ans = (cnt_zero * ways_diag + cnt_nonzero * ways_off) % MOD
        return ans
```

## Python3

```python
class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        # KMP prefix for pattern t
        m = n
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j and t[i] != t[j]:
                j = pi[j - 1]
            if t[i] == t[j]:
                j += 1
            pi[i] = j

        # search t in s+s (excluding the last character to avoid duplicate offset n)
        txt = s + s[:-1]
        matches = []
        j = 0
        for i, ch in enumerate(txt):
            while j and ch != t[j]:
                j = pi[j - 1]
            if ch == t[j]:
                j += 1
            if j == m:
                start = i - m + 1
                if start < n:  # valid rotation offset
                    matches.append(start)
                j = pi[j - 1]

        if not matches:
            return 0

        zero_present = 0 in matches
        cnt_nonzero = len(matches) - (1 if zero_present else 0)

        # matrix exponentiation for transformation
        def mat_mul(A, B):
            return [
                [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
                 (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
                [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
                 (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
            ]

        def mat_pow(M, power):
            # identity
            R = [[1, 0], [0, 1]]
            while power:
                if power & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                power >>= 1
            return R

        # transition matrix
        M = [[0, n - 1],
             [1, n - 2]]
        R = mat_pow(M, k)
        yk = R[0][0]   # ways to have total shift 0
        xk = R[1][0]   # ways for any non-zero shift

        ans = (yk if zero_present else 0) + cnt_nonzero * xk
        return ans % MOD
```

## C

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MOD 1000000007LL

typedef long long ll;

static ll mul_mod(ll a, ll b) {
    return (a * b) % MOD;
}

typedef struct {
    ll a00, a01, a10, a11;
} Mat;

static Mat mat_mul(const Mat* x, const Mat* y) {
    Mat r;
    r.a00 = (mul_mod(x->a00, y->a00) + mul_mod(x->a01, y->a10)) % MOD;
    r.a01 = (mul_mod(x->a00, y->a01) + mul_mod(x->a01, y->a11)) % MOD;
    r.a10 = (mul_mod(x->a10, y->a00) + mul_mod(x->a11, y->a10)) % MOD;
    r.a11 = (mul_mod(x->a10, y->a01) + mul_mod(x->a11, y->a11)) % MOD;
    return r;
}

static Mat mat_pow(Mat base, long long exp) {
    Mat res = {1, 0, 0, 1}; // identity
    while (exp > 0) {
        if (exp & 1LL) res = mat_mul(&res, &base);
        base = mat_mul(&base, &base);
        exp >>= 1LL;
    }
    return res;
}

int numberOfWays(char* s, char* t, long long k) {
    int n = strlen(s);
    if (n != (int)strlen(t)) return 0;

    // Build prefix function for pattern t
    int *pi = (int*)malloc(sizeof(int) * n);
    pi[0] = 0;
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && t[i] != t[j]) j = pi[j - 1];
        if (t[i] == t[j]) ++j;
        pi[i] = j;
    }

    // Build double string s+s
    char *ss = (char*)malloc(sizeof(char) * (2 * n));
    memcpy(ss, s, n);
    memcpy(ss + n, s, n);

    long long cnt0 = 0, cntNonZero = 0;
    int j = 0;
    // Scan up to position 2n-2 inclusive (length 2n-1)
    for (int i = 0; i < 2 * n - 1; ++i) {
        while (j > 0 && ss[i] != t[j]) j = pi[j - 1];
        if (ss[i] == t[j]) ++j;
        if (j == n) {
            int pos = i - n + 1; // starting index in ss
            if (pos < n) {
                if (pos == 0) cnt0 = 1;
                else cntNonZero++;
            }
            j = pi[j - 1];
        }
    }

    free(pi);
    free(ss);

    if (cnt0 + cntNonZero == 0) return 0; // t not a rotation of s

    // Build transition matrix
    Mat M;
    M.a00 = 0;
    M.a01 = n - 1;
    M.a10 = 1;
    M.a11 = n - 2;

    Mat R = mat_pow(M, k);
    ll a_k = R.a00 % MOD; // f_k[0]
    ll b_k = R.a10 % MOD; // f_k[x] for x!=0

    ll ans = (cnt0 * a_k) % MOD;
    ans = (ans + (cntNonZero % MOD) * b_k) % MOD;

    return (int)ans;
}
```

## Csharp

```csharp
using System;
public class Solution {
    private const int MOD = 1000000007;
    public int NumberOfWays(string s, string t, long k) {
        int n = s.Length;
        // Build combined string for Z-algorithm: t + "#" + s+s
        string ss = s + s;
        string combined = t + "#" + ss;
        int m = combined.Length;
        int[] z = new int[m];
        int l = 0, r = 0;
        for (int i = 1; i < m; i++) {
            if (i <= r) {
                z[i] = Math.Min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < m && combined[z[i]] == combined[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        long matchCount = 0;
        int offsetStart = n + 1; // position after t and '#'
        for (int i = offsetStart; i < m; i++) {
            if (z[i] >= n) {
                int pos = i - offsetStart; // rotation amount
                if (pos < n) matchCount++;
            }
        }
        if (matchCount == 0) return 0;
        long pow = ModPow(n, k - 1);
        long ans = (matchCount % MOD) * pow % MOD;
        return (int)ans;
    }
    private long ModPow(long baseVal, long exp) {
        long result = 1 % MOD;
        baseVal %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) result = (result * baseVal) % MOD;
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
 * @param {string} s
 * @param {string} t
 * @param {number} k
 * @return {number}
 */
var numberOfWays = function(s, t, k) {
    const MOD = 1000000007n;
    const n = s.length;
    if (n !== t.length) return 0;

    // KMP to find all rotations where s rotated left by d equals t
    const m = n;
    const lps = new Array(m).fill(0);
    for (let i = 1, len = 0; i < m; ) {
        if (t[i] === t[len]) {
            lps[i++] = ++len;
        } else if (len) {
            len = lps[len - 1];
        } else {
            lps[i++] = 0;
        }
    }

    const concat = s + s;
    let j = 0;
    let zeroShift = false;
    let totalShifts = 0; // number of d in [0,n-1] such that rotation matches
    for (let i = 0; i < concat.length; ++i) {
        while (j > 0 && concat[i] !== t[j]) j = lps[j - 1];
        if (concat[i] === t[j]) j++;
        if (j === m) {
            const start = i - m + 1;
            if (start < n) {
                totalShifts++;
                if (start === 0) zeroShift = true;
            }
            j = lps[j - 1];
        }
    }

    if (totalShifts === 0) return 0;

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

    const modInv = (a) => modPow(a, MOD - 2n);

    const invN = modInv(BigInt(n));
    const powNm1 = modPow(BigInt(n - 1), BigInt(k));
    const powNeg1 = (k % 2 === 0) ? 1n : MOD - 1n;

    // a_k for shift 0, b_k for non-zero shifts
    const aK = (invN * powNm1 % MOD + ((1n - invN + MOD) % MOD) * powNeg1 % MOD) % MOD;
    const bK = (invN * ((powNm1 - powNeg1 + MOD) % MOD)) % MOD;

    let ans = 0n;
    if (zeroShift) {
        ans = (ans + aK) % MOD;
    }
    const nonZeroCount = totalShifts - (zeroShift ? 1 : 0);
    ans = (ans + bK * BigInt(nonZeroCount)) % MOD;

    return Number(ans);
};
```

## Typescript

```typescript
function numberOfWays(s: string, t: string, k: number): number {
    const MOD = 1000000007n;
    const n = s.length;

    // KMP prefix function for pattern t
    const m = n;
    const lps = new Array(m).fill(0);
    for (let i = 1, len = 0; i < m;) {
        if (t[i] === t[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len !== 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }

    // Search t in s+s (excluding the last character to avoid duplicate full rotation)
    const ss = s + s.slice(0, n - 1);
    let totalMatches = 0;
    let zeroMatch = 0; // whether offset 0 is a match
    for (let i = 0, j = 0; i < ss.length;) {
        while (j > 0 && ss[i] !== t[j]) j = lps[j - 1];
        if (ss[i] === t[j]) j++;
        if (j === m) {
            const start = i - m + 1;
            if (start < n) {
                totalMatches++;
                if (start === 0) zeroMatch = 1;
            }
            j = lps[j - 1];
        }
        i++;
    }

    // modular exponentiation
    function modPow(base: bigint, exp: number): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if ((e & 1) === 1) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1;
        }
        return result;
    }

    const powBase = BigInt(n - 1);
    const powK = modPow(powBase, k); // (n-1)^k mod MOD
    const sign = (k % 2 === 0) ? 1n : MOD - 1n; // (-1)^k

    const invN = modPow(BigInt(n), Number(MOD - 2n)); // modular inverse of n

    // f0 for offset 0
    let f0 = (powK + powBase * sign) % MOD;
    f0 = (f0 * invN) % MOD;

    // f for non‑zero offsets
    let temp = powK - sign;
    if (temp < 0) temp += MOD;
    let fNonZero = (temp * invN) % MOD;

    const ansBig = (BigInt(zeroMatch) * f0 + BigInt(totalMatches - zeroMatch) * fNonZero) % MOD;
    return Number(ansBig);
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;

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

    private function computeLPS($pat) {
        $m = strlen($pat);
        $lps = array_fill(0, $m, 0);
        $len = 0;
        $i = 1;
        while ($i < $m) {
            if ($pat[$i] === $pat[$len]) {
                $len++;
                $lps[$i] = $len;
                $i++;
            } else {
                if ($len != 0) {
                    $len = $lps[$len - 1];
                } else {
                    $lps[$i] = 0;
                    $i++;
                }
            }
        }
        return $lps;
    }

    /**
     * @param String $s
     * @param String $t
     * @param Integer $k
     * @return Integer
     */
    function numberOfWays($s, $t, $k) {
        $n = strlen($s);
        if ($n != strlen($t)) return 0;

        // KMP to count occurrences of t in s+s with start index < n
        $pattern = $t;
        $text = $s . $s;
        $lps = $this->computeLPS($pattern);
        $cnt = 0;
        $i = 0; // index for text
        $j = 0; // index for pattern
        $limit = $n * 2 - 1; // last start position is n-1, so we need up to index limit-1
        $textLen = strlen($text);
        while ($i < $limit) {
            if ($text[$i] === $pattern[$j]) {
                $i++;
                $j++;
                if ($j == $n) {
                    // match ending at i-1, start = i - n
                    $cnt++;
                    $j = $lps[$j - 1];
                }
            } else {
                if ($j != 0) {
                    $j = $lps[$j - 1];
                } else {
                    $i++;
                }
            }
        }

        if ($cnt == 0) return 0;

        $cntZero = ($s === $t) ? 1 : 0;
        $cntNonZero = $cnt - $cntZero;

        $powAll = $this->modPow($n - 1, $k);
        $powNegOne = ($k % 2 == 0) ? 1 : (self::MOD - 1);

        $invN = $this->modPow($n, self::MOD - 2);

        // dp for residue 0
        $tempZero = ($powAll + ($powNegOne * ($n - 1)) % self::MOD) % self::MOD;
        $dpZero = ($tempZero * $invN) % self::MOD;

        // dp for non-zero residues
        $tempNonZero = ($powAll - $powNegOne) % self::MOD;
        if ($tempNonZero < 0) $tempNonZero += self::MOD;
        $dpNonZero = ($tempNonZero * $invN) % self::MOD;

        $ans = 0;
        if ($cntZero > 0) {
            $ans = ($ans + $dpZero) % self::MOD;
        }
        if ($cntNonZero > 0) {
            $ans = ($ans + ($cntNonZero * $dpNonZero) % self::MOD) % self::MOD;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfWays(_ s: String, _ t: String, _ k: Int) -> Int {
        // Placeholder implementation
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfWays(s: String, t: String, k: Long): Int {
        val MOD = 1_000_000_007L
        val n = s.length

        // KMP prefix function for pattern t
        val lps = IntArray(n)
        var len = 0
        var i = 1
        while (i < n) {
            if (t[i] == t[len]) {
                len++
                lps[i] = len
                i++
            } else {
                if (len != 0) {
                    len = lps[len - 1]
                } else {
                    lps[i] = 0
                    i++
                }
            }
        }

        // Search t in s+s, count valid rotations
        val text = (s + s).toCharArray()
        var j = 0
        var cntZero = 0L
        var cntNonZero = 0L
        for (idx in text.indices) {
            while (j > 0 && text[idx] != t[j]) {
                j = lps[j - 1]
            }
            if (text[idx] == t[j]) j++
            if (j == n) {
                val start = idx - n + 1
                if (start < n) {
                    if (start == 0) cntZero = 1L else cntNonZero++
                }
                j = lps[j - 1]
            }
        }

        if (cntZero + cntNonZero == 0L) return 0

        val base = ((n - 1).toLong()) % MOD
        val pow = modPow(base, k, MOD)
        val sign = if (k % 2L == 0L) 1L else MOD - 1L
        val invN = modInverse(n.toLong(), MOD)

        // f(k): ways to end at same rotation (d=0)
        val f = ((pow + ((n - 1).toLong() % MOD) * sign % MOD) % MOD) * invN % MOD
        // g(k): ways to end at a specific different rotation (d!=0)
        val g = ((pow - sign + MOD) % MOD) * invN % MOD

        var ans = (cntZero % MOD) * f % MOD
        ans = (ans + (cntNonZero % MOD) * g % MOD) % MOD
        return ans.toInt()
    }

    private fun modPow(base: Long, exp: Long, mod: Long): Long {
        var b = base % mod
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) res = (res * b) % mod
            b = (b * b) % mod
            e = e shr 1
        }
        return res
    }

    private fun modInverse(a: Long, mod: Long): Long {
        return modPow(a, mod - 2, mod)
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int numberOfWays(String s, String t, int k) {
    int n = s.length;
    if (n != t.length) return 0;

    // Find all rotation offsets where rotating s by offset equals t
    List<int> offsets = _findOffsets(s, t);
    if (offsets.isEmpty) return 0;

    int powA = _modPow(n - 1, k);
    int powB = (k % 2 == 0) ? 1 : (_MOD - 1);
    int invN = _modPow(n, _MOD - 2);

    // ways to reach residue 0
    int waysZero = ((powA + ((n - 1) % _MOD) * powB) % _MOD) *
        invN %
        _MOD;
    // ways to reach any non‑zero residue
    int waysNonZero =
        ((powA - powB + _MOD) % _MOD) * invN % _MOD;

    int ans = 0;
    for (int d in offsets) {
      if (d == 0) {
        ans += waysZero;
      } else {
        ans += waysNonZero;
      }
      if (ans >= _MOD) ans -= _MOD;
    }
    return ans % _MOD;
  }

  List<int> _findOffsets(String s, String t) {
    int n = s.length;
    String ss = s + s;
    // KMP prefix function for pattern t
    List<int> lps = List.filled(n, 0);
    int len = 0;
    for (int i = 1; i < n; i++) {
      while (len > 0 && t[i] != t[len]) {
        len = lps[len - 1];
      }
      if (t[i] == t[len]) {
        len++;
        lps[i] = len;
      }
    }

    List<int> offsets = [];
    int j = 0;
    int limit = 2 * n - 1; // we need start positions < n
    for (int i = 0; i < limit; i++) {
      while (j > 0 && ss[i] != t[j]) {
        j = lps[j - 1];
      }
      if (ss[i] == t[j]) {
        j++;
      }
      if (j == n) {
        int pos = i - n + 1;
        if (pos < n) offsets.add(pos);
        j = lps[j - 1];
      }
    }
    return offsets;
  }

  int _modPow(int base, int exp) {
    long result = 1;
    long b = base % _MOD;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _MOD;
      }
      b = (b * b) % _MOD;
      exp >>= 1;
    }
    return result.toInt();
  }
}
```

## Golang

```go
func numberOfWays(s string, t string, k int64) int {
	const MOD int64 = 1000000007
	n := len(s)
	// Build prefix function for pattern t
	m := n
	pi := make([]int, m)
	for i := 1; i < m; i++ {
		j := pi[i-1]
		for j > 0 && t[i] != t[j] {
			j = pi[j-1]
		}
		if t[i] == t[j] {
			j++
		}
		pi[i] = j
	}
	// Search in s+s (only need first n-1 chars of second copy)
	text := s + s[:n-1]
	cnt := 0
	goodZero := false
	j := 0
	for i := 0; i < len(text); i++ {
		for j > 0 && text[i] != t[j] {
			j = pi[j-1]
		}
		if text[i] == t[j] {
			j++
		}
		if j == m {
			start := i - m + 1
			if start < n { // valid rotation offset
				cnt++
				if start == 0 {
					goodZero = true
				}
			}
			j = pi[j-1]
		}
	}
	if cnt == 0 {
		return 0
	}

	type Mat [2][2]int64
	mul := func(a, b Mat) Mat {
		var c Mat
		for i := 0; i < 2; i++ {
			for j := 0; j < 2; j++ {
				var sum int64
				for l := 0; l < 2; l++ {
					sum = (sum + a[i][l]*b[l][j]) % MOD
				}
				c[i][j] = sum
			}
		}
		return c
	}

	// exponentiate matrix M = [[0, n-1],[1, n-2]]
	var res Mat = Mat{{1, 0}, {0, 1}}
	base := Mat{{0, int64(n - 1)}, {1, int64(n - 2)}}
	exp := k
	for exp > 0 {
		if exp&1 == 1 {
			res = mul(res, base)
		}
		base = mul(base, base)
		exp >>= 1
	}
	// V_k = res * V_0 where V_0 = [1,0]^T
	f := res[0][0] % MOD // ways to be at offset 0 after k steps
	g := res[1][0] % MOD // ways to be at a specific non‑zero offset after k steps

	ans := int64(0)
	if goodZero {
		ans = (ans + f) % MOD
	}
	nonZeroGood := cnt
	if goodZero {
		nonZeroGood--
	}
	ans = (ans + int64(nonZeroGood)*g%MOD) % MOD
	return int(ans)
}
```

## Ruby

```ruby
def number_of_ways(s, t, k)
  mod = 1_000_000_007
  n = s.length

  # ---------- find all rotation offsets where s rotated by d equals t ----------
  ss = s + s
  combined = t + "$" + ss[0, 2 * n - 1]  # only need positions < n
  m = combined.length
  z = Array.new(m, 0)
  l = r = 0
  (1...m).each do |i|
    if i <= r
      z[i] = [r - i + 1, z[i - l]].min
    end
    while i + z[i] < m && combined.getbyte(z[i]) == combined.getbyte(i + z[i])
      z[i] += 1
    end
    if i + z[i] - 1 > r
      l = i
      r = i + z[i] - 1
    end
  end

  valid_shifts = []
  offset = t.length + 1
  (0...n).each do |start|
    idx = offset + start
    if idx < m && z[idx] >= n
      valid_shifts << start
    end
  end

  return 0 if valid_shifts.empty?

  # ---------- precompute powers ----------
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

  pow_n1 = mod_pow(n - 1, k, mod)
  sign = k.even? ? 1 : mod - 1   # (-1)^k modulo mod
  inv_n = mod_pow(n, mod - 2, mod)

  total = 0
  valid_shifts.each do |d|
    if d == 0
      val = (pow_n1 + (n - 1) * sign) % mod
    else
      val = (pow_n1 - sign) % mod
      val += mod if val < 0
    end
    val = (val * inv_n) % mod
    total += val
    total -= mod if total >= mod
  end

  total
end
```

## Scala

```scala
object Solution {
    private val MOD: Long = 1000000007L

    def numberOfWays(s: String, t: String, k: Long): Int = {
        val n = s.length
        // Find all rotation offsets where rotating s left by offset equals t
        val concat = s + s
        val lps = new Array[Int](n)
        // build LPS for pattern t
        var len = 0
        var i = 1
        while (i < n) {
            if (t.charAt(i) == t.charAt(len)) {
                len += 1
                lps(i) = len
                i += 1
            } else {
                if (len != 0) {
                    len = lps(len - 1)
                } else {
                    lps(i) = 0
                    i += 1
                }
            }
        }

        var cnt = 0L
        var zeroMatch = false
        var j = 0 // index in pattern t
        val limit = 2 * n - 1 // we need positions < n
        for (idx <- 0 until limit) {
            while (j > 0 && concat.charAt(idx) != t.charAt(j)) {
                j = lps(j - 1)
            }
            if (concat.charAt(idx) == t.charAt(j)) {
                j += 1
                if (j == n) {
                    val pos = idx - n + 1 // start position of match
                    if (pos < n) {
                        cnt += 1
                        if (pos == 0) zeroMatch = true
                    }
                    j = lps(j - 1)
                }
            }
        }

        if (cnt == 0) return 0

        // Matrix exponentiation for transitions
        def mul(a: Array[Array[Long]], b: Array[Array[Long]]): Array[Array[Long]] = {
            val res = Array.ofDim[Long](2, 2)
            var r = 0
            while (r < 2) {
                var c = 0
                while (c < 2) {
                    var sum = 0L
                    var kk = 0
                    while (kk < 2) {
                        sum = (sum + a(r)(kk) * b(kk)(c)) % MOD
                        kk += 1
                    }
                    res(r)(c) = sum
                    c += 1
                }
                r += 1
            }
            res
        }

        var power = k
        var base = Array(
            Array(0L, (n - 1).toLong % MOD),
            Array(1L, (n - 2).toLong % MOD)
        )
        var result = Array(
            Array(1L, 0L),
            Array(0L, 1L)
        )

        while (power > 0) {
            if ((power & 1L) == 1L) result = mul(result, base)
            base = mul(base, base)
            power >>= 1
        }

        val f = result(0)(0) % MOD // ways to be at offset 0 after k ops
        val g = result(1)(0) % MOD // ways to be at any specific non-zero offset

        var ans = 0L
        if (zeroMatch) {
            ans = (ans + f) % MOD
        }
        val nonZeroCnt = cnt - (if (zeroMatch) 1 else 0)
        ans = (ans + g * (nonZeroCnt % MOD)) % MOD

        ans.toInt
    }
}
```

## Rust

```rust
use std::cmp::min;

const MOD: i64 = 1_000_000_007;

impl Solution {
    pub fn number_of_ways(s: String, t: String, k: i64) -> i32 {
        let n = s.len();
        if n != t.len() || n == 0 {
            return 0;
        }

        // KMP prefix function for pattern t
        let pat = t.as_bytes();
        let mut lps = vec![0usize; n];
        for i in 1..n {
            let mut len = lps[i - 1];
            while len > 0 && pat[i] != pat[len] {
                len = lps[len - 1];
            }
            if pat[i] == pat[len] {
                len += 1;
            }
            lps[i] = len;
        }

        // Search t in s+s
        let ss_bytes = {
            let mut v = Vec::with_capacity(2 * n);
            v.extend_from_slice(s.as_bytes());
            v.extend_from_slice(s.as_bytes());
            v
        };

        let mut cnt_zero: i64 = 0;
        let mut cnt_nonzero: i64 = 0;
        let mut j = 0usize;
        // we need positions < n, so iterate up to 2n-1 (last start index is n-1)
        for i in 0..(2 * n - 1) {
            while j > 0 && ss_bytes[i] != pat[j] {
                j = lps[j - 1];
            }
            if ss_bytes[i] == pat[j] {
                j += 1;
            }
            if j == n {
                let pos = i + 1 - n; // starting index
                if pos < n {
                    if pos == 0 {
                        cnt_zero = 1;
                    } else {
                        cnt_nonzero += 1;
                    }
                }
                j = lps[j - 1];
            }
        }

        if cnt_zero + cnt_nonzero == 0 {
            return 0;
        }

        // Matrix exponentiation for recurrence
        fn mul(a: [[i64; 2]; 2], b: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
            let mut res = [[0i64; 2]; 2];
            for i in 0..2 {
                for k in 0..2 {
                    if a[i][k] == 0 {
                        continue;
                    }
                    for j in 0..2 {
                        let val = (a[i][k] as i128 * b[k][j] as i128) % MOD as i128;
                        res[i][j] =
                            ((res[i][j] as i128 + val) % MOD as i128) as i64;
                    }
                }
            }
            res
        }

        let n_mod = n as i64 % MOD;
        let a01 = (n_mod - 1 + MOD) % MOD; // n-1
        let a11 = (n_mod - 2 + MOD) % MOD; // n-2

        let mut mat = [[0i64, a01], [1i64, a11]];
        let mut res = [[1i64, 0i64], [0i64, 1i64]];

        let mut exp = k as u64;
        while exp > 0 {
            if exp & 1 == 1 {
                res = mul(res, mat);
            }
            mat = mul(mat, mat);
            exp >>= 1;
        }

        // v_k = res * v_0 where v_0 = [1, 0]^T
        let xk = res[0][0] % MOD; // value for residue 0
        let yk = res[1][0] % MOD; // value for any non‑zero residue

        let ans = ((cnt_zero % MOD) * xk % MOD + (cnt_nonzero % MOD) * yk % MOD) % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; 2x2 matrix multiplication (row-major vector of length 4)
(define (mat-mul m1 m2)
  (let* ((a (vector-ref m1 0))
         (b (vector-ref m1 1))
         (c (vector-ref m1 2))
         (d (vector-ref m1 3))
         (e (vector-ref m2 0))
         (f (vector-ref m2 1))
         (g (vector-ref m2 2))
         (h (vector-ref m2 3)))
    (vector (modulo (+ (* a e) (* b g)) MOD)
            (modulo (+ (* a f) (* b h)) MOD)
            (modulo (+ (* c e) (* d g)) MOD)
            (modulo (+ (* c f) (* d h)) MOD))))

;; fast exponentiation of 2x2 matrix
(define (mat-pow m exp)
  (let loop ((res (vector 1 0 0 1))
             (base m)
             (e exp))
    (if (= e 0)
        res
        (let* ((new-res (if (odd? e) (mat-mul res base) res))
               (new-base (mat-mul base base)))
          (loop new-res new-base (quotient e 2))))))

;; prefix function for KMP
(define (compute-pi pat)
  (let* ((m (string-length pat))
         (pi (make-vector m 0)))
    (let loop ((i 1) (j 0))
      (when (< i m)
        (if (char=? (string-ref pat i) (string-ref pat j))
            (begin
              (set! j (+ j 1))
              (vector-set! pi i j)
              (loop (+ i 1) j))
            (if (> j 0)
                (begin
                  (set! j (vector-ref pi (- j 1)))
                  (loop i j))
                (begin
                  (vector-set! pi i 0)
                  (loop (+ i 1) 0))))))
    pi))

;; find all rotation offsets d (0 <= d < n) such that rotating s left by d yields t
(define (find-offsets s t)
  (let* ((n (string-length s))
         (ss (string-append s s))
         (m (string-length t))
         (pi (compute-pi t))
         (positions '()))
    (let loop ((i 0) (j 0))
      (when (< i (* 2 n))
        (if (char=? (string-ref ss i) (string-ref t j))
            (begin
              (set! i (+ i 1))
              (set! j (+ j 1))
              (when (= j m)
                (let ((pos (- i m)))
                  (when (< pos n)
                    (set! positions (cons pos positions))))
                (set! j (vector-ref pi (- j 1))))
              (loop i j))
            (if (> j 0)
                (begin
                  (set! j (vector-ref pi (- j 1)))
                  (loop i j))
                (begin
                  (set! i (+ i 1))
                  (loop i j))))))
    positions))

;; main function
(define/contract (number-of-ways s t k)
  (-> string? string? exact-integer? exact-integer?)
  (let* ((n (string-length s)))
    ;; compute DP values after k steps
    (let* ((trans (vector 0 (- n 1) 1 (- n 2))) ; matrix [[0,n-1],[1,n-2]]
           (powM (mat-pow trans k))
           (dp-same (vector-ref powM 0))   ; from state 0 to 0
           (dp-diff (vector-ref powM 2)))  ; from state 0 to any specific non‑zero state
      ;; find all valid offsets
      (let ((offsets (find-offsets s t)))
        (if (null? offsets)
            0
            (foldl (lambda (d acc)
                     (modulo (+ acc (if (= d 0) dp-same dp-diff)) MOD))
                   0
                   offsets))))))
```

## Erlang

```erlang
-spec number_of_ways(S :: unicode:unicode_binary(), T :: unicode:unicode_binary(), K :: integer()) -> integer().
number_of_ways(S, T, K) ->
    Mod = 1000000007,
    N = byte_size(S),
    case byte_size(T) of
        N2 when N2 =:= N ->
            ok;
        _ -> 
            0
    end,
    %% count rotations where rotate left by i gives T
    Pattern = T,
    Text = <<S/binary, S/binary>>,
    LpsTuple = build_lps_tuple(Pattern),
    Count = kmp_search(Text, N, Pattern, LpsTuple, 0, 0, 0),
    %% cnt0 : rotation offset 0 matches?
    Cnt0 = if S =:= T -> 1; true -> 0 end,
    %% modular exponentiations
    PowN1 = mod_pow(N - 1, K, Mod),
    Sign = case K rem 2 of 0 -> 1; _ -> Mod - 1 end,
    InvN = mod_pow(N, Mod - 2, Mod),
    Ways0 = ((PowN1 + ((N - 1) * Sign) rem Mod) rem Mod * InvN) rem Mod,
    TotalNonZero = ((PowN1 - Sign + Mod) rem Mod * InvN) rem Mod,
    Answer = (Cnt0 * Ways0 + (Count - Cnt0) * TotalNonZero) rem Mod,
    if Answer < 0 -> Answer + Mod; true -> Answer end.

%% Build LPS tuple for pattern (0‑based indexing)
build_lps_tuple(Pattern) ->
    N = byte_size(Pattern),
    build_lps(1, 0, N, Pattern, lists:duplicate(N, 0)).

build_lps(I, Len, N, Pattern, LpsList) when I < N ->
    CharI = binary:at(Pattern, I),
    CharLen = binary:at(Pattern, Len),
    if CharI =:= CharLen ->
            NewLen = Len + 1,
            Updated = set_elem(LpsList, I, NewLen),
            build_lps(I + 1, NewLen, N, Pattern, Updated);
       Len =/= 0 ->
            NewLen = get_elem(LpsList, Len - 1),
            build_lps(I, NewLen, N, Pattern, LpsList);
       true ->
            Updated = set_elem(LpsList, I, 0),
            build_lps(I + 1, 0, N, Pattern, Updated)
    end;
build_lps(_, _, _, _, LpsList) ->
    list_to_tuple(LpsList).

set_elem(List, Index, Value) ->
    lists:sublist(List, Index) ++ [Value] ++ lists:nthtail(Index + 1, List).

get_elem(List, Index) ->
    lists:nth(Index + 1, List).

%% KMP search over Text (length 2N‑1), counting matches with start < N
kmp_search(Text, N, Pattern, LpsTuple, I, J, Acc) ->
    MaxI = 2 * N - 1,
    if I >= MaxI -> Acc;
       true ->
            CharT = binary:at(Text, I),
            CharP = binary:at(Pattern, J),
            if CharT =:= CharP ->
                    J1 = J + 1,
                    I1 = I + 1,
                    if J1 == N ->
                            Start = I1 - N,
                            Acc1 = if Start < N -> Acc + 1; true -> Acc end,
                            J2 = element(N, LpsTuple), % lps[N‑1]
                            kmp_search(Text, N, Pattern, LpsTuple, I1, J2, Acc1);
                       true ->
                            kmp_search(Text, N, Pattern, LpsTuple, I1, J1, Acc)
                    end;
               true ->
                    if J =/= 0 ->
                            J2 = element(J, LpsTuple), % lps[J‑1]
                            kmp_search(Text, N, Pattern, LpsTuple, I, J2, Acc);
                       true ->
                            kmp_search(Text, N, Pattern, LpsTuple, I + 1, 0, Acc)
                    end
            end
    end.

%% Fast modular exponentiation
mod_pow(_, 0, Mod) -> 1 rem Mod;
mod_pow(Base, Exp, Mod) when Exp band 1 =:= 1 ->
    ((Base rem Mod) * mod_pow(Base rem Mod, Exp bsr 1, Mod)) rem Mod;
mod_pow(Base, Exp, Mod) ->
    Half = mod_pow(Base rem Mod, Exp bsr 1, Mod),
    (Half * Half) rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec number_of_ways(String.t(), String.t(), integer()) :: integer()
  def number_of_ways(s, t, k) do
    {g0, g1} = count_good_offsets(s, t)

    n = byte_size(s)
    # transition matrix M = [[0, n-1],[1, n-2]]
    m00 = 0
    m01 = rem(n - 1, @mod)
    m10 = 1
    m11 = rem(n - 2, @mod)

    {r00, r01, _r10, _r11} = mat_pow({m00, m01, m10, m11}, k, @mod)

    ans = rem(g0 * r00 + g1 * r01, @mod)
    ans
  end

  # count good rotation offsets where rotating s left by offset yields t
  defp count_good_offsets(s, t) do
    n = byte_size(s)

    s_tuple = :binary.bin_to_list(s) |> List.to_tuple()
    t_tuple = :binary.bin_to_list(t) |> List.to_tuple()

    text_bin = s <> s
    text_tuple = :binary.bin_to_list(text_bin) |> List.to_tuple()
    len_text = tuple_size(text_tuple)

    pi = build_pi(t_tuple, n)

    {g0, g1, _} =
      search_loop(0, 0, text_tuple, len_text, t_tuple, n, pi, 0, 0)

    {g0, g1}
  end

  # KMP prefix function
  defp build_pi(pat, m) do
    pi_array = :array.new(m, default: 0)
    {pi_array, _} = pi_loop(1, 0, pi_array, pat, m)
    List.to_tuple(Enum.map(0..m - 1, fn i -> :array.get(i, pi_array) end))
  end

  defp pi_loop(i, j, pi, pat, m) when i < m do
    if :erlang.element(i + 1, pat) == :erlang.element(j + 1, pat) do
      j2 = j + 1
      pi2 = :array.set(i, j2, pi)
      pi_loop(i + 1, j2, pi2, pat, m)
    else
      if j != 0 do
        j2 = :array.get(j - 1, pi)
        pi_loop(i, j2, pi, pat, m)
      else
        pi2 = :array.set(i, 0, pi)
        pi_loop(i + 1, 0, pi2, pat, m)
      end
    end
  end

  defp pi_loop(_, _, pi, _, _), do: {pi, nil}

  # KMP search over concatenated text, counting offsets < n
  defp search_loop(i, j, text, len, pat, n, pi, g0, g1) when i < len do
    ti = :erlang.element(i + 1, text)
    tj = :erlang.element(j + 1, pat)

    cond do
      ti == tj ->
        j2 = j + 1

        if j2 == n do
          pos = i - n + 1

          {ng0, ng1} =
            if pos < n do
              if pos == 0, do: {g0 + 1, g1}, else: {g0, g1 + 1}
            else
              {g0, g1}
            end

          # after full match, continue with pi[n-1]
          j_next = :erlang.element(n, pi)
          search_loop(i + 1, j_next, text, len, pat, n, pi, ng0, ng1)
        else
          search_loop(i + 1, j2, text, len, pat, n, pi, g0, g1)
        end

      j != 0 ->
        # fallback using prefix function
        j_fallback = :erlang.element(j, pi) # pi[j-1]
        search_loop(i, j_fallback, text, len, pat, n, pi, g0, g1)

      true ->
        search_loop(i + 1, 0, text, len, pat, n, pi, g0, g1)
    end
  end

  defp search_loop(_, _, _, _, _, _, _, g0, g1), do: {g0, g1, 0}

  # 2x2 matrix multiplication modulo mod
  defp mat_mul({a00, a01, a10, a11}, {b00, b01, b10, b11}, mod) do
    {
      rem(a00 * b00 + a01 * b10, mod),
      rem(a00 * b01 + a01 * b11, mod),
      rem(a10 * b00 + a11 * b10, mod),
      rem(a10 * b01 + a11 * b11, mod)
    }
  end

  # fast exponentiation of matrix
  defp mat_pow(_m, 0, _mod), do: {1, 0, 0, 1}

  defp mat_pow(m, exp, mod) when exp > 0 do
    pow_acc(m, exp, {1, 0, 0, 1}, mod)
  end

  defp pow_acc(_base, 0, acc, _mod), do: acc

  defp pow_acc(base, exp, acc, mod) do
    acc = if rem(exp, 2) == 1, do: mat_mul(acc, base, mod), else: acc
    base = mat_mul(base, base, mod)
    pow_acc(base, div(exp, 2), acc, mod)
  end
end
```

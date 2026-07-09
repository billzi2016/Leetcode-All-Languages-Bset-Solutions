# 3337. Total Characters in String After Transformations II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    static const long long MOD = 1000000007LL;
    using Matrix = array<array<long long,26>,26>;
    
    Matrix mul(const Matrix& A, const Matrix& B) {
        Matrix C{};
        for (int i = 0; i < 26; ++i)
            for (int k = 0; k < 26; ++k) if (A[i][k])
                for (int j = 0; j < 26; ++j) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
                }
        return C;
    }
    
    Matrix matPow(Matrix base, long long exp) {
        Matrix res{};
        for (int i = 0; i < 26; ++i) res[i][i] = 1;
        while (exp > 0) {
            if (exp & 1LL) res = mul(res, base);
            base = mul(base, base);
            exp >>= 1LL;
        }
        return res;
    }
    
public:
    int lengthAfterTransformations(string s, int t, vector<int>& nums) {
        // initial count vector
        array<long long,26> cnt{};
        for (char ch : s) cnt[ch - 'a']++;
        
        // build transformation matrix M where M[new][old] = occurrences
        Matrix M{};
        for (int old = 0; old < 26; ++old) {
            int len = nums[old];
            for (int k = 1; k <= len; ++k) {
                int nw = (old + k) % 26;
                M[nw][old] = (M[nw][old] + 1) % MOD;
            }
        }
        
        Matrix Mp = matPow(M, t);
        
        // multiply Mp with cnt vector
        array<long long,26> finalCnt{};
        for (int i = 0; i < 26; ++i) {
            long long sum = 0;
            for (int j = 0; j < 26; ++j) {
                sum = (sum + Mp[i][j] * cnt[j]) % MOD;
            }
            finalCnt[i] = sum;
        }
        
        long long ans = 0;
        for (int i = 0; i < 26; ++i) ans = (ans + finalCnt[i]) % MOD;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    public int lengthAfterTransformations(String s, int t, java.util.List<Integer> nums) {
        int n = 26;
        long[][] trans = new long[n][n];
        for (int j = 0; j < n; ++j) {
            int cnt = nums.get(j);
            for (int k = 1; k <= cnt; ++k) {
                int i = (j + k) % n;
                trans[i][j] = 1;
            }
        }

        long[][] matPow = matrixPower(trans, t);

        long[] init = new long[n];
        for (char ch : s.toCharArray()) {
            init[ch - 'a']++;
        }

        long[] after = new long[n];
        for (int i = 0; i < n; ++i) {
            long sum = 0;
            for (int j = 0; j < n; ++j) {
                if (init[j] == 0) continue;
                sum = (sum + matPow[i][j] * init[j]) % MOD;
            }
            after[i] = sum;
        }

        long ans = 0;
        for (long v : after) ans = (ans + v) % MOD;
        return (int) ans;
    }

    private long[][] matrixPower(long[][] base, int exp) {
        int n = base.length;
        long[][] result = new long[n][n];
        for (int i = 0; i < n; ++i) result[i][i] = 1;

        long[][] cur = copy(base);
        long e = exp;
        while (e > 0) {
            if ((e & 1L) == 1L) result = multiply(cur, result);
            cur = multiply(cur, cur);
            e >>= 1;
        }
        return result;
    }

    private long[][] multiply(long[][] A, long[][] B) {
        int n = A.length;
        long[][] C = new long[n][n];
        for (int i = 0; i < n; ++i) {
            for (int k = 0; k < n; ++k) {
                if (A[i][k] == 0) continue;
                long aik = A[i][k];
                for (int j = 0; j < n; ++j) {
                    if (B[k][j] == 0) continue;
                    C[i][j] = (C[i][j] + aik * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    private long[][] copy(long[][] M) {
        int n = M.length;
        long[][] cp = new long[n][n];
        for (int i = 0; i < n; ++i) System.arraycopy(M[i], 0, cp[i], 0, n);
        return cp;
    }
}
```

## Python

```python
class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = 26

        # initial count vector
        v0 = [0] * n
        for ch in s:
            v0[ord(ch) - 97] += 1

        if t == 0:
            return len(s) % MOD

        # build transformation matrix M (size 26x26)
        M = [[0] * n for _ in range(n)]
        for j in range(n):
            k = nums[j]
            for d in range(1, k + 1):
                i = (j + d) % n
                M[i][j] = (M[i][j] + 1) % MOD

        def mat_mul(A, B):
            """multiply two 26x26 matrices"""
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                Ai = A[i]
                Ci = C[i]
                for k in range(n):
                    aik = Ai[k]
                    if aik:
                        Bk = B[k]
                        mul = aik
                        for j in range(n):
                            Ci[j] = (Ci[j] + mul * Bk[j]) % MOD
            return C

        def mat_pow(mat, exp):
            """matrix exponentiation"""
            # identity matrix
            res = [[0] * n for _ in range(n)]
            for i in range(n):
                res[i][i] = 1
            base = mat
            while exp:
                if exp & 1:
                    res = mat_mul(res, base)
                base = mat_mul(base, base)
                exp >>= 1
            return res

        M_pow = mat_pow(M, t)

        # multiply matrix with initial vector
        vt = [0] * n
        for i in range(n):
            total = 0
            row = M_pow[i]
            for j in range(n):
                if v0[j]:
                    total = (total + row[j] * v0[j]) % MOD
            vt[i] = total

        ans = sum(vt) % MOD
        return ans
```

## Python3

```python
class Solution:
    def lengthAfterTransformations(self, s, t, nums):
        MOD = 10**9 + 7
        n = 26

        # initial count vector
        cnt = [0] * n
        for ch in s:
            cnt[ord(ch) - 97] += 1

        if t == 0:
            return len(s) % MOD

        # build transformation matrix M (n x n)
        M = [[0] * n for _ in range(n)]
        for i in range(n):
            step = nums[i]
            for k in range(1, step + 1):
                j = (i + k) % n
                M[j][i] = (M[j][i] + 1) % MOD

        def mat_mul(A, B):
            # multiply two n x n matrices
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                Ai = A[i]
                Ci = C[i]
                for k in range(n):
                    if Ai[k]:
                        aik = Ai[k]
                        Bk = B[k]
                        for j in range(n):
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        def mat_pow(mat, power):
            # identity matrix
            res = [[0] * n for _ in range(n)]
            for i in range(n):
                res[i][i] = 1
            while power:
                if power & 1:
                    res = mat_mul(res, mat)
                mat = mat_mul(mat, mat)
                power >>= 1
            return res

        # compute M^t
        Mt = mat_pow(M, t)

        # multiply Mt with cnt vector
        final_cnt = [0] * n
        for i in range(n):
            total = 0
            row = Mt[i]
            for j in range(n):
                if row[j]:
                    total = (total + row[j] * cnt[j]) % MOD
            final_cnt[i] = total

        return sum(final_cnt) % MOD
```

## C

```c
#include <stddef.h>
#include <string.h>

#define MOD 1000000007LL
#define SZ 26

static void matMul(long long A[SZ][SZ], long long B[SZ][SZ], long long C[SZ][SZ]) {
    long long tmp[SZ][SZ] = {0};
    for (int i = 0; i < SZ; ++i) {
        for (int k = 0; k < SZ; ++k) if (A[i][k]) {
            long long aik = A[i][k];
            for (int j = 0; j < SZ; ++j) if (B[k][j]) {
                tmp[i][j] = (tmp[i][j] + aik * B[k][j]) % MOD;
            }
        }
    }
    memcpy(C, tmp, sizeof(tmp));
}

static void matPow(long long base[SZ][SZ], long long exp, long long res[SZ][SZ]) {
    // initialize res as identity
    for (int i = 0; i < SZ; ++i)
        for (int j = 0; j < SZ; ++j)
            res[i][j] = (i == j);
    long long cur[SZ][SZ];
    memcpy(cur, base, sizeof(cur));
    while (exp) {
        if (exp & 1LL) {
            matMul(res, cur, res);
        }
        matMul(cur, cur, cur);
        exp >>= 1LL;
    }
}

int lengthAfterTransformations(char* s, int t, int* nums, int numsSize) {
    long long cnt[SZ] = {0};
    for (char *p = s; *p; ++p) {
        cnt[*p - 'a']++;
    }

    // Build transformation matrix M where M[j][i]=1 if i transforms to j
    long long M[SZ][SZ] = {{0}};
    for (int i = 0; i < SZ; ++i) {
        int k = nums[i];
        for (int step = 1; step <= k; ++step) {
            int j = (i + step) % SZ;
            M[j][i] = 1;
        }
    }

    long long P[SZ][SZ];
    matPow(M, (long long)t, P);

    // Multiply P with initial vector cnt
    long long finalCnt[SZ] = {0};
    for (int i = 0; i < SZ; ++i) {
        long long sum = 0;
        for (int j = 0; j < SZ; ++j) {
            if (P[i][j] && cnt[j]) {
                sum = (sum + P[i][j] * cnt[j]) % MOD;
            }
        }
        finalCnt[i] = sum;
    }

    long long ans = 0;
    for (int i = 0; i < SZ; ++i) {
        ans += finalCnt[i];
        if (ans >= MOD) ans -= MOD;
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;
    private const int SZ = 26;

    public int LengthAfterTransformations(string s, int t, IList<int> nums) {
        // Count initial characters
        long[] cnt = new long[SZ];
        foreach (char ch in s) {
            cnt[ch - 'a']++;
        }

        // Build transformation matrix T where T[new][old] = 1 if new appears in expansion of old
        long[,] baseMat = new long[SZ, SZ];
        for (int old = 0; old < SZ; old++) {
            int steps = nums[old];
            for (int k = 1; k <= steps; k++) {
                int nw = (old + k) % SZ;
                baseMat[nw, old] = (baseMat[nw, old] + 1) % MOD;
            }
        }

        // Compute T^t
        long[,] matPow = MatrixPower(baseMat, t);

        // Multiply matrix by initial vector
        long[] finalVec = new long[SZ];
        for (int i = 0; i < SZ; i++) {
            long sum = 0;
            for (int j = 0; j < SZ; j++) {
                if (matPow[i, j] == 0 || cnt[j] == 0) continue;
                sum += matPow[i, j] * cnt[j];
                if (sum >= (1L << 62)) sum %= MOD; // prevent overflow
            }
            finalVec[i] = sum % MOD;
        }

        long answer = 0;
        foreach (var v in finalVec) {
            answer += v;
            if (answer >= MOD) answer -= MOD;
        }
        return (int)(answer % MOD);
    }

    private static long[,] MatrixMultiply(long[,] A, long[,] B) {
        long[,] C = new long[SZ, SZ];
        for (int i = 0; i < SZ; i++) {
            for (int k = 0; k < SZ; k++) {
                if (A[i, k] == 0) continue;
                long aik = A[i, k];
                for (int j = 0; j < SZ; j++) {
                    if (B[k, j] == 0) continue;
                    C[i, j] = (C[i, j] + aik * B[k, j]) % MOD;
                }
            }
        }
        return C;
    }

    private static long[,] MatrixPower(long[,] baseMat, int exponent) {
        long[,] result = new long[SZ, SZ];
        for (int i = 0; i < SZ; i++) result[i, i] = 1;

        long[,] cur = baseMat;
        long exp = exponent;
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                result = MatrixMultiply(result, cur);
            }
            cur = MatrixMultiply(cur, cur);
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
 * @param {number} t
 * @param {number[]} nums
 * @return {number}
 */
var lengthAfterTransformations = function(s, t, nums) {
    const MOD = 1000000007n;
    const N = 26;

    // initial vector of counts
    const vec0 = Array(N).fill(0n);
    for (let ch of s) {
        const idx = ch.charCodeAt(0) - 97;
        vec0[idx] = (vec0[idx] + 1n) % MOD;
    }

    // build base transformation matrix M where M[i][j]=1 if char j expands to i
    const base = Array.from({length: N}, () => Array(N).fill(0n));
    for (let src = 0; src < N; ++src) {
        const cnt = nums[src];
        for (let k = 1; k <= cnt; ++k) {
            const tgt = (src + k) % N;
            base[tgt][src] = 1n;
        }
    }

    // matrix multiplication (A * B) % MOD
    function matMul(A, B) {
        const C = Array.from({length: N}, () => Array(N).fill(0n));
        for (let i = 0; i < N; ++i) {
            for (let k = 0; k < N; ++k) {
                if (A[i][k] === 0n) continue;
                const aik = A[i][k];
                for (let j = 0; j < N; ++j) {
                    if (B[k][j] === 0n) continue;
                    C[i][j] = (C[i][j] + aik * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    // matrix exponentiation by squaring
    function matPow(mat, exp) {
        let result = Array.from({length: N}, (_, i) =>
            Array.from({length: N}, (_, j) => (i === j ? 1n : 0n))
        );
        let baseMat = mat;
        while (exp > 0) {
            if (exp & 1) {
                result = matMul(baseMat, result);
            }
            exp = Math.floor(exp / 2);
            if (exp > 0) {
                baseMat = matMul(baseMat, baseMat);
            }
        }
        return result;
    }

    // multiply matrix with vector
    function matVecMul(M, vec) {
        const res = Array(N).fill(0n);
        for (let i = 0; i < N; ++i) {
            let sum = 0n;
            for (let j = 0; j < N; ++j) {
                if (M[i][j] !== 0n && vec[j] !== 0n) {
                    sum = (sum + M[i][j] * vec[j]) % MOD;
                }
            }
            res[i] = sum;
        }
        return res;
    }

    // compute M^t
    const Mt = matPow(base, t);

    // final vector after t transformations
    const vt = matVecMul(Mt, vec0);

    // total length is sum of all counts modulo MOD
    let ans = 0n;
    for (let i = 0; i < N; ++i) {
        ans = (ans + vt[i]) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function lengthAfterTransformations(s: string, t: number, nums: number[]): number {
    const MOD = 1000000007n;
    const N = 26;

    // Build transformation matrix M (N x N), M[row][col]
    const M: bigint[][] = Array.from({ length: N }, () => Array(N).fill(0n));
    for (let i = 0; i < N; i++) {
        const k = nums[i];
        for (let step = 1; step <= k; step++) {
            const j = (i + step) % N;
            M[j][i] = 1n;
        }
    }

    // Matrix multiplication
    function matMul(A: bigint[][], B: bigint[][]): bigint[][] {
        const C: bigint[][] = Array.from({ length: N }, () => Array(N).fill(0n));
        for (let i = 0; i < N; i++) {
            for (let k = 0; k < N; k++) {
                if (A[i][k] === 0n) continue;
                const aik = A[i][k];
                for (let j = 0; j < N; j++) {
                    if (B[k][j] === 0n) continue;
                    C[i][j] = (C[i][j] + aik * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    // Matrix exponentiation
    function matPow(base: bigint[][], exp: number): bigint[][] {
        let result: bigint[][] = Array.from({ length: N }, (_, i) => {
            const row = Array(N).fill(0n);
            row[i] = 1n; // identity
            return row;
        });
        let b = base;
        let e = exp;
        while (e > 0) {
            if (e & 1) result = matMul(result, b);
            b = matMul(b, b);
            e >>>= 1;
        }
        return result;
    }

    // Initial vector of character counts
    const vec: bigint[] = Array(N).fill(0n);
    for (let ch of s) {
        const idx = ch.charCodeAt(0) - 97;
        vec[idx] = (vec[idx] + 1n) % MOD;
    }

    // Compute M^t
    const Mt = matPow(M, t);

    // Multiply Mt by initial vector
    const finalVec: bigint[] = Array(N).fill(0n);
    for (let i = 0; i < N; i++) {
        let sum = 0n;
        for (let j = 0; j < N; j++) {
            if (Mt[i][j] !== 0n && vec[j] !== 0n) {
                sum = (sum + Mt[i][j] * vec[j]) % MOD;
            }
        }
        finalVec[i] = sum;
    }

    // Sum all counts
    let ans = 0n;
    for (let v of finalVec) {
        ans = (ans + v) % MOD;
    }
    return Number(ans);
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $t
     * @param Integer[] $nums
     * @return Integer
     */
    function lengthAfterTransformations($s, $t, $nums) {
        $mod = 1000000007;
        $n = 26;

        // initial count vector
        $cnt = array_fill(0, $n, 0);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx] = ($cnt[$idx] + 1) % $mod;
        }

        // build transformation matrix M (size 26x26)
        $M = array_fill(0, $n, array_fill(0, $n, 0));
        for ($old = 0; $old < $n; $old++) {
            $k = $nums[$old];
            for ($d = 1; $d <= $k; $d++) {
                $new = ($old + $d) % $n;
                $M[$new][$old] = ($M[$new][$old] + 1) % $mod;
            }
        }

        // identity matrix
        $res = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            $res[$i][$i] = 1;
        }

        // fast exponentiation of matrix M to power t
        while ($t > 0) {
            if ($t & 1) {
                $res = $this->matMul($res, $M, $mod);
            }
            $M = $this->matMul($M, $M, $mod);
            $t >>= 1;
        }

        // multiply resulting matrix with initial count vector
        $finalCnt = $this->matVecMul($res, $cnt, $mod);

        // sum all counts to get total length
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans = ($ans + $finalCnt[$i]) % $mod;
        }
        return $ans;
    }

    private function matMul($A, $B, $mod) {
        $n = 26;
        $C = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            for ($k = 0; $k < $n; $k++) {
                $aik = $A[$i][$k];
                if ($aik == 0) continue;
                for ($j = 0; $j < $n; $j++) {
                    $bkj = $B[$k][$j];
                    if ($bkj == 0) continue;
                    $C[$i][$j] = ($C[$i][$j] + $aik * $bkj) % $mod;
                }
            }
        }
        return $C;
    }

    private function matVecMul($M, $vec, $mod) {
        $n = 26;
        $res = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $sum = 0;
            for ($j = 0; $j < $n; $j++) {
                if ($M[$i][$j] == 0 || $vec[$j] == 0) continue;
                $sum = ($sum + $M[$i][$j] * $vec[$j]) % $mod;
            }
            $res[$i] = $sum;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    let MOD: Int64 = 1_000_000_007

    func lengthAfterTransformations(_ s: String, _ t: Int, _ nums: [Int]) -> Int {
        var cnt = Array(repeating: Int64(0), count: 26)
        for ch in s.utf8 {
            let idx = Int(ch - 97)   // 'a' ascii is 97
            cnt[idx] += 1
        }
        if t == 0 {
            var sum: Int64 = 0
            for v in cnt { sum = (sum + v) % MOD }
            return Int(sum)
        }

        let size = 26
        var base = Array(repeating: Array(repeating: Int64(0), count: size), count: size)
        for i in 0..<size {
            let steps = nums[i]
            if steps == 0 { continue }
            for k in 1...steps {
                let j = (i + k) % size
                base[j][i] = 1
            }
        }

        var result = identityMatrix(size)
        var power = base
        var exp = t
        while exp > 0 {
            if exp & 1 == 1 {
                result = matMul(result, power, size)
            }
            power = matMul(power, power, size)
            exp >>= 1
        }

        var finalCnt = Array(repeating: Int64(0), count: size)
        for i in 0..<size {
            var sum: Int64 = 0
            for j in 0..<size where result[i][j] != 0 && cnt[j] != 0 {
                sum = (sum + result[i][j] * cnt[j]) % MOD
            }
            finalCnt[i] = sum
        }

        var total: Int64 = 0
        for v in finalCnt { total = (total + v) % MOD }
        return Int(total)
    }

    private func identityMatrix(_ n: Int) -> [[Int64]] {
        var I = Array(repeating: Array(repeating: Int64(0), count: n), count: n)
        for i in 0..<n { I[i][i] = 1 }
        return I
    }

    private func matMul(_ A: [[Int64]], _ B: [[Int64]], _ n: Int) -> [[Int64]] {
        var C = Array(repeating: Array(repeating: Int64(0), count: n), count: n)
        let mod = MOD
        for i in 0..<n {
            for k in 0..<n where A[i][k] != 0 {
                let aik = A[i][k]
                for j in 0..<n where B[k][j] != 0 {
                    C[i][j] = (C[i][j] + aik * B[k][j]) % mod
                }
            }
        }
        return C
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L
    private val N = 26

    private fun multiply(a: Array<LongArray>, b: Array<LongArray>): Array<LongArray> {
        val res = Array(N) { LongArray(N) }
        for (i in 0 until N) {
            for (k in 0 until N) {
                val aik = a[i][k]
                if (aik == 0L) continue
                for (j in 0 until N) {
                    val bkj = b[k][j]
                    if (bkj == 0L) continue
                    res[i][j] = (res[i][j] + aik * bkj) % MOD
                }
            }
        }
        return res
    }

    private fun matrixPower(base: Array<LongArray>, expLong: Long): Array<LongArray> {
        var exp = expLong
        var result = Array(N) { i -> LongArray(N) { j -> if (i == j) 1L else 0L } }
        var cur = base
        while (exp > 0) {
            if ((exp and 1L) == 1L) {
                result = multiply(result, cur)
            }
            cur = multiply(cur, cur)
            exp = exp shr 1
        }
        return result
    }

    fun lengthAfterTransformations(s: String, t: Int, nums: List<Int>): Int {
        if (t == 0) return s.length % MOD.toInt()
        val cnt = LongArray(N)
        for (ch in s) {
            cnt[ch.code - 'a'.code]++
        }

        // build transformation matrix M where M[target][source] = 1 if target appears in replacement of source
        val mat = Array(N) { LongArray(N) }
        for (src in 0 until N) {
            val steps = nums[src]
            for (k in 1..steps) {
                val tgt = (src + k) % N
                mat[tgt][src] = 1L
            }
        }

        val powerMat = matrixPower(mat, t.toLong())

        // multiply powerMat with initial vector cnt
        var total = 0L
        for (i in 0 until N) {
            var sum = 0L
            for (j in 0 until N) {
                val mij = powerMat[i][j]
                if (mij == 0L) continue
                sum = (sum + mij * cnt[j]) % MOD
            }
            total = (total + sum) % MOD
        }

        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;
  List<List<int>> _multiply(List<List<int>> a, List<List<int>> b) {
    const int n = 26;
    final res = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) {
      for (int k = 0; k < n; ++k) {
        final aik = a[i][k];
        if (aik == 0) continue;
        for (int j = 0; j < n; ++j) {
          final bkj = b[k][j];
          if (bkj == 0) continue;
          res[i][j] = (res[i][j] + aik * bkj) % _MOD;
        }
      }
    }
    return res;
  }

  List<List<int>> _power(List<List<int>> base, int exp) {
    const int n = 26;
    final result = List.generate(n, (i) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) result[i][i] = 1;
    while (exp > 0) {
      if ((exp & 1) == 1) result = _multiply(result, base);
      base = _multiply(base, base);
      exp >>= 1;
    }
    return result;
  }

  int lengthAfterTransformations(String s, int t, List<int> nums) {
    const int n = 26;
    final cnt = List.filled(n, 0);
    for (final code in s.codeUnits) {
      final idx = code - 97; // 'a'
      cnt[idx] = (cnt[idx] + 1) % _MOD;
    }

    // Build transformation matrix M[dest][src]
    final mat = List.generate(n, (_) => List.filled(n, 0));
    for (int src = 0; src < n; ++src) {
      final steps = nums[src];
      for (int k = 1; k <= steps; ++k) {
        final dest = (src + k) % n;
        mat[dest][src] = (mat[dest][src] + 1) % _MOD;
      }
    }

    final powMat = _power(mat, t);

    // Multiply matrix with initial vector
    final finalVec = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int sum = 0;
      for (int j = 0; j < n; ++j) {
        if (powMat[i][j] == 0) continue;
        sum = (sum + powMat[i][j] * cnt[j]) % _MOD;
      }
      finalVec[i] = sum;
    }

    int ans = 0;
    for (final v in finalVec) {
      ans += v;
      if (ans >= _MOD) ans -= _MOD;
    }
    return ans;
  }
}
```

## Golang

```go
func lengthAfterTransformations(s string, t int, nums []int) int {
	const MOD int64 = 1000000007

	// Count initial frequencies
	var v0 [26]int64
	for _, ch := range s {
		v0[ch-'a']++
	}

	// Build transformation matrix M where M[i][j]=1 if i is within next nums[j] letters after j
	var M [26][26]int64
	for j := 0; j < 26; j++ {
		cnt := nums[j]
		for k := 1; k <= cnt; k++ {
			i := (j + k) % 26
			M[i][j] = 1
		}
	}

	// Matrix exponentiation: res = M^t
	var res [26][26]int64
	for i := 0; i < 26; i++ {
		res[i][i] = 1
	}
	cur := M
	power := int64(t)
	for power > 0 {
		if power&1 == 1 {
			res = mul(res, cur)
		}
		cur = mul(cur, cur)
		power >>= 1
	}

	// Multiply resulting matrix with initial vector
	var vt [26]int64
	for i := 0; i < 26; i++ {
		sum := int64(0)
		for j := 0; j < 26; j++ {
			if res[i][j] != 0 && v0[j] != 0 {
				sum = (sum + res[i][j]*v0[j]) % MOD
			}
		}
		vt[i] = sum
	}

	// Sum all counts to get final length
	ans := int64(0)
	for i := 0; i < 26; i++ {
		ans = (ans + vt[i]) % MOD
	}
	return int(ans)
}

// Helper: multiply two 26x26 matrices modulo MOD
func mul(a, b [26][26]int64) [26][26]int64 {
	const MOD int64 = 1000000007
	var c [26][26]int64
	for i := 0; i < 26; i++ {
		for k := 0; k < 26; k++ {
			if a[i][k] == 0 {
				continue
			}
			ak := a[i][k]
			for j := 0; j < 26; j++ {
				if b[k][j] == 0 {
					continue
				}
				c[i][j] = (c[i][j] + ak*b[k][j]) % MOD
			}
		}
	}
	return c
}
```

## Ruby

```ruby
def length_after_transformations(s, t, nums)
  mod = 1_000_000_007
  n = 26

  # Build transformation matrix M (size 26x26)
  m = Array.new(n) { Array.new(n, 0) }
  (0...n).each do |c|
    cnt = nums[c]
    (1..cnt).each do |off|
      new_c = (c + off) % n
      m[new_c][c] = (m[new_c][c] + 1) % mod
    end
  end

  # Matrix multiplication lambda
  mat_mul = lambda do |a, b|
    size = a.size
    res = Array.new(size) { Array.new(size, 0) }
    size.times do |i|
      size.times do |k|
        aik = a[i][k]
        next if aik == 0
        size.times do |j|
          res[i][j] = (res[i][j] + aik * b[k][j]) % mod
        end
      end
    end
    res
  end

  # Identity matrix
  result = Array.new(n) { |i| arr = Array.new(n, 0); arr[i] = 1; arr }
  base = m
  exp = t
  while exp > 0
    if (exp & 1) == 1
      result = mat_mul.call(result, base)
    end
    base = mat_mul.call(base, base)
    exp >>= 1
  end

  # Initial character counts vector
  vec = Array.new(n, 0)
  s.each_byte { |ch| vec[ch - 97] += 1 }

  # Multiply result matrix with initial vector
  final_vec = Array.new(n, 0)
  n.times do |i|
    sum = 0
    n.times do |j|
      sum = (sum + result[i][j] * vec[j]) % mod
    end
    final_vec[i] = sum
  end

  # Total length after t transformations
  total = final_vec.reduce(0) { |acc, v| (acc + v) % mod }
  total
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L
    private val SZ = 26

    private def multiply(A: Array[Array[Long]], B: Array[Array[Long]]): Array[Array[Long]] = {
        val C = Array.ofDim[Long](SZ, SZ)
        var i = 0
        while (i < SZ) {
            var k = 0
            while (k < SZ) {
                val aik = A(i)(k)
                if (aik != 0L) {
                    var j = 0
                    while (j < SZ) {
                        C(i)(j) = (C(i)(j) + aik * B(k)(j)) % MOD
                        j += 1
                    }
                }
                k += 1
            }
            i += 1
        }
        C
    }

    def lengthAfterTransformations(s: String, t: Int, nums: List[Int]): Int = {
        // Build transformation matrix M where M[row][col] = 1 if row char appears in replacement of col char
        val M = Array.ofDim[Long](SZ, SZ)
        var c = 0
        while (c < SZ) {
            val k = nums(c)
            var step = 1
            while (step <= k) {
                val target = (c + step) % SZ
                M(target)(c) = 1L
                step += 1
            }
            c += 1
        }

        // Initial vector counts of each character in s
        val vec0 = new Array[Long](SZ)
        var idx = 0
        while (idx < s.length) {
            val ch = s.charAt(idx) - 'a'
            vec0(ch) += 1L
            idx += 1
        }

        // Fast exponentiation of matrix M to the power t
        var resultMat = Array.ofDim[Long](SZ, SZ)
        var i = 0
        while (i < SZ) {
            resultMat(i)(i) = 1L
            i += 1
        }
        var base = M.map(_.clone())
        var exp = t.toLong
        while (exp > 0) {
            if ((exp & 1L) == 1L) resultMat = multiply(resultMat, base)
            base = multiply(base, base)
            exp >>= 1
        }

        // Multiply resulting matrix with initial vector
        val finalVec = new Array[Long](SZ)
        i = 0
        while (i < SZ) {
            var sum = 0L
            var j = 0
            while (j < SZ) {
                sum = (sum + resultMat(i)(j) * vec0(j)) % MOD
                j += 1
            }
            finalVec(i) = sum
            i += 1
        }

        // Sum all counts to get answer
        var ans = 0L
        i = 0
        while (i < SZ) {
            ans = (ans + finalVec(i)) % MOD
            i += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn length_after_transformations(s: String, t: i32, nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len() as i64 % MOD;
        if t == 0 {
            return n as i32;
        }
        // initial counts of each character
        let mut init = vec![0i64; 26];
        for b in s.bytes() {
            init[(b - b'a') as usize] += 1;
        }

        // build transformation matrix M (26 x 26)
        let mut m = vec![vec![0i64; 26]; 26];
        for old in 0..26 {
            let k = nums[old] as usize;
            for offset in 1..=k {
                let newc = (old + offset) % 26;
                m[newc][old] = 1;
            }
        }

        // matrix multiplication
        fn mat_mul(a: &Vec<Vec<i64>>, b: &Vec<Vec<i64>>) -> Vec<Vec<i64>> {
            const MOD: i64 = 1_000_000_007;
            let mut res = vec![vec![0i64; 26]; 26];
            for i in 0..26 {
                for k in 0..26 {
                    if a[i][k] == 0 { continue; }
                    let aik = a[i][k];
                    for j in 0..26 {
                        if b[k][j] == 0 { continue; }
                        res[i][j] = (res[i][j] + aik * b[k][j]) % MOD;
                    }
                }
            }
            res
        }

        // matrix exponentiation
        fn mat_pow(mut base: Vec<Vec<i64>>, mut exp: i64) -> Vec<Vec<i64>> {
            let mut result = vec![vec![0i64; 26]; 26];
            for i in 0..26 { result[i][i] = 1; }
            while exp > 0 {
                if exp & 1 == 1 {
                    result = mat_mul(&result, &base);
                }
                base = mat_mul(&base, &base);
                exp >>= 1;
            }
            result
        }

        let m_pow = mat_pow(m, t as i64);

        // multiply matrix with initial vector
        let mut final_counts = vec![0i64; 26];
        for i in 0..26 {
            let mut sum = 0i64;
            for j in 0..26 {
                if m_pow[i][j] == 0 || init[j] == 0 { continue; }
                sum = (sum + m_pow[i][j] * init[j]) % MOD;
            }
            final_counts[i] = sum;
        }

        let total: i64 = final_counts.iter().fold(0, |acc, &x| (acc + x) % MOD);
        total as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; create a 26x26 zero matrix
(define (make-zero-matrix)
  (let ((M (make-vector 26)))
    (for ([i (in-range 26)])
      (vector-set! M i (make-vector 26 0)))
    M))

;; identity matrix
(define (identity-matrix)
  (let ((I (make-zero-matrix)))
    (for ([i (in-range 26)])
      (vector-set! (vector-ref I i) i 1))
    I))

;; matrix multiplication (A * B) mod MOD
(define (mat-mul A B)
  (let ((C (make-zero-matrix)))
    (for ([i (in-range 26)])
      (for ([k (in-range 26)])
        (let ((aik (vector-ref (vector-ref A i) k)))
          (when (not (= aik 0))
            (for ([j (in-range 26)])
              (let* ((bkj (vector-ref (vector-ref B k) j))
                     (cij (vector-ref (vector-ref C i) j))
                     (new (+ cij (* aik bkj))))
                (vector-set! (vector-ref C i) j (modulo new MOD)))))))))
    C))

;; fast exponentiation of matrix M to power e
(define (mat-pow M e)
  (let loop ((result (identity-matrix)) (base M) (exp e))
    (if (= exp 0)
        result
        (let ((new-result (if (odd? exp) (mat-mul base result) result)))
          (loop new-result (mat-mul base base) (quotient exp 2))))))

;; matrix-vector multiplication (M * v) mod MOD
(define (mat-vec-mul M v)
  (let ((res (make-vector 26 0)))
    (for ([i (in-range 26)])
      (let ((sum 0))
        (for ([j (in-range 26)])
          (set! sum (+ sum (* (vector-ref (vector-ref M i) j)
                              (vector-ref v j)))))
        (vector-set! res i (modulo sum MOD))))
    res))

;; build transformation matrix from nums list
(define (build-matrix nums)
  (let ((M (make-zero-matrix)))
    (for ([old (in-range 26)])
      (let ((k (list-ref nums old))) ; nums[i] is exact integer
        (for ([offset (in-range 1 (+ k 1))])
          (let ((new (modulo (+ old offset) 26)))
            (vector-set! (vector-ref M new) old 1)))))
    M))

;; main function
(define/contract (length-after-transformations s t nums)
  (-> string? exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((cnt (make-vector 26 0))
         (n (string-length s)))
    ;; count initial characters
    (for ([i (in-range n)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! cnt idx (+ (vector-ref cnt idx) 1))))
    ;; build matrix and exponentiate
    (let* ((M (build-matrix nums))
           (Mp (mat-pow M t))
           (final-vec (mat-vec-mul Mp cnt)))
      ;; sum all counts modulo MOD
      (let ((total 0))
        (for ([i (in-range 26)])
          (set! total (+ total (vector-ref final-vec i))))
        (modulo total MOD)))))
```

## Erlang

```erlang
-module(solution).
-export([length_after_transformations/3]).

-define(MOD, 1000000007).

%% Public API
-spec length_after_transformations(S :: unicode:unicode_binary(), T :: integer(), Nums :: [integer()]) -> integer().
length_after_transformations(S, T, Nums) ->
    Vec0 = count_chars(S),
    Mat = build_matrix(Nums),
    MatT = mat_pow(Mat, T),
    Vt = mat_vec_mul(MatT, Vec0),
    sum_vector(Vt).

%% Count occurrences of each character in the string
count_chars(Bin) ->
    ZeroVec = list_to_tuple(lists:duplicate(26, 0)),
    count_chars_loop(Bin, ZeroVec).

count_chars_loop(<<>>, Vec) -> Vec;
count_chars_loop(<<Char:8, Rest/binary>>, Vec) ->
    Index = Char - $a,
    Old = element(Index + 1, Vec),
    NewVec = setelement(Index + 1, Vec, Old + 1),
    count_chars_loop(Rest, NewVec).

%% Build transformation matrix from nums
build_matrix(Nums) ->
    Size = 26,
    ZeroRow = list_to_tuple(lists:duplicate(Size, 0)),
    InitMat = list_to_tuple(lists:duplicate(Size, ZeroRow)),
    build_matrix_loop(InitMat, Nums, 0).

build_matrix_loop(Mat, _Nums, Src) when Src == 26 -> Mat;
build_matrix_loop(Mat, Nums, Src) ->
    Num = lists:nth(Src + 1, Nums),
    Mat2 = add_edges(Mat, Src, Num, 1),
    build_matrix_loop(Mat2, Nums, Src + 1).

add_edges(Mat, _Src, 0, _K) -> Mat;
add_edges(Mat, Src, Rem, K) ->
    Dest = (Src + K) rem 26,
    Row = element(Dest + 1, Mat),
    NewRow = setelement(Src + 1, Row, 1),
    NewMat = setelement(Dest + 1, Mat, NewRow),
    add_edges(NewMat, Src, Rem - 1, K + 1).

%% Matrix exponentiation by squaring (iterative)
mat_pow(Matrix, Exp) ->
    mat_pow_loop(Matrix, Exp, identity()).

mat_pow_loop(_M, 0, Acc) -> Acc;
mat_pow_loop(M, Exp, Acc) ->
    NewAcc = case (Exp band 1) of
        1 -> mul(Acc, M);
        _ -> Acc
    end,
    NewM = mul(M, M),
    mat_pow_loop(NewM, Exp bsr 1, NewAcc).

%% Identity matrix
identity() ->
    Rows = [list_to_tuple([if I == J -> 1; true -> 0 end || J <- lists:seq(0,25)]) ||
            I <- lists:seq(0,25)],
    list_to_tuple(Rows).

%% Matrix multiplication (26x26)
mul(A, B) ->
    Size = 26,
    Rows = [row_mul(I, A, B, Size) || I <- lists:seq(0, Size - 1)],
    list_to_tuple(Rows).

row_mul(I, A, B, Size) ->
    RowA = element(I + 1, A),
    ColVals = [col_val(RowA, B, J, Size) || J <- lists:seq(0, Size - 1)],
    list_to_tuple(ColVals).

col_val(RowA, B, J, Size) ->
    col_sum(0, RowA, B, J, Size, 0).

col_sum(K, _RowA, _B, _J, Size, Acc) when K == Size -> Acc;
col_sum(K, RowA, B, J, Size, Acc) ->
    Aik = element(K + 1, RowA),
    Bkj = element(J + 1, element(K + 1, B)),
    NewAcc = (Acc + (Aik * Bkj) rem ?MOD) rem ?MOD,
    col_sum(K + 1, RowA, B, J, Size, NewAcc).

%% Matrix-vector multiplication
mat_vec_mul(Mat, Vec) ->
    Size = 26,
    Rows = [row_vec_mul(I, Mat, Vec, Size) || I <- lists:seq(0, Size - 1)],
    list_to_tuple(Rows).

row_vec_mul(I, Mat, Vec, Size) ->
    Row = element(I + 1, Mat),
    vec_sum(0, Row, Vec, Size, 0).

vec_sum(K, _Row, _Vec, Size, Acc) when K == Size -> Acc;
vec_sum(K, Row, Vec, Size, Acc) ->
    Rik = element(K + 1, Row),
    Vk = element(K + 1, Vec),
    NewAcc = (Acc + (Rik * Vk) rem ?MOD) rem ?MOD,
    vec_sum(K + 1, Row, Vec, Size, NewAcc).

%% Sum all elements of a vector
sum_vector(Vec) ->
    sum_vec(0, Vec, 0).

sum_vec(Index, _Vec, Acc) when Index == 26 -> Acc;
sum_vec(Index, Vec, Acc) ->
    Val = element(Index + 1, Vec),
    NewAcc = (Acc + Val) rem ?MOD,
    sum_vec(Index + 1, Vec, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007
  @size 26

  @spec length_after_transformations(String.t(), integer(), [integer()]) :: integer()
  def length_after_transformations(s, t, nums) do
    base_mat = build_matrix(nums)
    mat_t = mat_pow(base_mat, t)

    cnt_tuple =
      :binary.bin_to_list(s)
      |> Enum.reduce(tuple_zeroes(), fn byte, acc ->
        idx = byte - ?a
        cur = elem(acc, idx)
        put_elem(acc, idx, cur + 1)
      end)

    total =
      Enum.reduce(0..@size - 1, 0, fn i, sum ->
        row = Enum.at(mat_t, i)

        val =
          Enum.reduce(0..@size - 1, 0, fn j, acc2 ->
            (acc2 + Enum.at(row, j) * elem(cnt_tuple, j)) |> rem(@mod)
          end)

        (sum + val) |> rem(@mod)
      end)

    total
  end

  defp tuple_zeroes do
    List.to_tuple(List.duplicate(0, @size))
  end

  defp build_matrix(nums) do
    for i <- 0..@size - 1 do
      # column i corresponds to original character i
      col = Enum.at(nums, i)
      row_vals =
        for j <- 0..@size - 1 do
          if in_range?(i, j, col), do: 1, else: 0
        end

      row_vals
    end
  end

  defp in_range?(orig, target, len) do
    # check if target is within the next `len` characters after orig (cyclic)
    diff = rem(target - orig + @size, @size)
    diff >= 1 and diff <= len
  end

  defp mat_pow(mat, exp) do
    ident = identity()
    pow_loop(mat, exp, ident)
  end

  defp pow_loop(_mat, 0, acc), do: acc

  defp pow_loop(mat, exp, acc) do
    {new_acc, new_mat, new_exp} =
      if rem(exp, 2) == 1 do
        {mul(acc, mat), mul(mat, mat), div(exp, 2)}
      else
        {acc, mul(mat, mat), div(exp, 2)}
      end

    pow_loop(new_mat, new_exp, new_acc)
  end

  defp identity do
    for i <- 0..@size - 1 do
      for j <- 0..@size - 1 do
        if i == j, do: 1, else: 0
      end
    end
  end

  defp mul(a, b) do
    for i <- 0..@size - 1 do
      row_a = Enum.at(a, i)

      for j <- 0..@size - 1 do
        sum =
          Enum.reduce(0..@size - 1, 0, fn k, acc ->
            (acc + Enum.at(row_a, k) * Enum.at(Enum.at(b, k), j)) |> rem(@mod)
          end)

        sum
      end
    end
  end
end
```

# 3145. Find Products of Elements of Big Array

## Cpp

```cpp
class Solution {
public:
    vector<int> findProductsOfElements(vector<vector<long long>>& queries) {
        vector<int> ans;
        for (auto& q : queries) {
            long long L = q[0];
            long long R = q[1];
            int mod = (int)q[2];
            long long exp = prefixExp(R) - prefixExp(L - 1);
            ans.push_back((int)modPow(2, exp, mod));
        }
        return ans;
    }

private:
    // total number of set bits in binary representations of numbers 1..n
    static unsigned long long countOnes(unsigned long long n) {
        if (n == 0) return 0;
        unsigned long long total = 0;
        for (int b = 0; (1ULL << b) <= n; ++b) {
            unsigned long long cycle = 1ULL << (b + 1);
            unsigned long long full = (n + 1) / cycle;
            total += full * (1ULL << b);
            unsigned long long rem = (n + 1) % cycle;
            if (rem > (1ULL << b)) total += rem - (1ULL << b);
        }
        return total;
    }

    // number of integers in [1,n] with bit b set
    static unsigned long long countSet(unsigned long long n, int b) {
        if (n == 0) return 0;
        unsigned long long cycle = 1ULL << (b + 1);
        unsigned long long full = (n + 1) / cycle;
        unsigned long long cnt = full * (1ULL << b);
        unsigned long long rem = (n + 1) % cycle;
        if (rem > (1ULL << b)) cnt += rem - (1ULL << b);
        return cnt;
    }

    // sum of exponents (bit positions) for all set bits in numbers 1..n
    static unsigned long long prefixSumExp(unsigned long long n) {
        if (n == 0) return 0;
        unsigned long long sum = 0;
        for (int b = 0; (1ULL << b) <= n; ++b) {
            unsigned long long cnt = countSet(n, b);
            sum += (unsigned long long)b * cnt;
        }
        return sum;
    }

    // find smallest i such that countOnes(i) > pos
    static unsigned long long findNumber(unsigned long long pos) {
        unsigned long long low = 1, high = 2;
        while (countOnes(high) <= pos) high <<= 1;
        while (low < high) {
            unsigned long long mid = low + ((high - low) >> 1);
            if (countOnes(mid) > pos)
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }

    // total exponent sum for elements with index <= pos (0‑based)
    static unsigned long long prefixExp(long long pos) {
        if (pos < 0) return 0;
        unsigned long long p = (unsigned long long)pos;
        unsigned long long num = findNumber(p);
        unsigned long long prevCnt = countOnes(num - 1);
        unsigned long long offset = p - prevCnt; // zero‑based within bits of num
        unsigned long long sumPrev = prefixSumExp(num - 1);

        // sum exponents of first (offset+1) set bits of num (low to high)
        unsigned long long need = offset + 1;
        unsigned long long taken = 0, partial = 0;
        for (int b = 0; taken < need; ++b) {
            if ((num >> b) & 1ULL) {
                partial += b;
                ++taken;
            }
        }
        return sumPrev + partial;
    }

    static long long modPow(long long base, unsigned long long exp, int mod) {
        if (mod == 1) return 0;
        long long res = 1 % mod;
        base %= mod;
        while (exp) {
            if (exp & 1ULL) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1ULL;
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[] findProductsOfElements(long[][] queries) {
        int q = queries.length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            long from = queries[i][0];
            long to = queries[i][1];
            int mod = (int) queries[i][2];
            long exp = prefix(to + 1) - prefix(from);
            ans[i] = (int) modPow(2L, exp, mod);
        }
        return ans;
    }

    // total exponent sum of first 'pos' elements (positions 0..pos-1)
    private long prefix(long pos) {
        if (pos == 0) return 0L;
        long low = 0, high = pos; // n cannot exceed pos
        while (low < high) {
            long mid = (low + high + 1) >>> 1;
            if (countBits(mid) <= pos) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        long fullNums = low; // numbers fully included
        long rem = pos - countBits(fullNums);
        long sum = sumBitPos(fullNums);
        if (rem > 0) {
            long val = fullNums + 1;
            for (int k = 0; rem > 0 && val != 0; k++) {
                if ((val & 1L) == 1L) {
                    sum += k;
                    rem--;
                }
                val >>>= 1;
            }
        }
        return sum;
    }

    // total number of set bits in binary representations of 1..n
    private long countBits(long n) {
        if (n <= 0) return 0L;
        long total = 0L;
        for (int k = 0; (1L << k) <= n; k++) {
            long cycle = 1L << (k + 1);
            long fullCycles = (n + 1) / cycle;
            long bits = fullCycles * (1L << k);
            long remainder = (n + 1) % cycle;
            long extra = Math.max(0L, remainder - (1L << k));
            total += bits + extra;
        }
        return total;
    }

    // sum of bit positions (exponents) for all set bits in 1..n
    private long sumBitPos(long n) {
        if (n <= 0) return 0L;
        long total = 0L;
        for (int k = 0; (1L << k) <= n; k++) {
            long cycle = 1L << (k + 1);
            long fullCycles = (n + 1) / cycle;
            long bits = fullCycles * (1L << k);
            long remainder = (n + 1) % cycle;
            long extra = Math.max(0L, remainder - (1L << k));
            long cnt = bits + extra; // number of set bits at position k
            total += (long) k * cnt;
        }
        return total;
    }

    private long modPow(long base, long exp, int mod) {
        if (mod == 1) return 0L;
        long result = 1 % mod;
        long b = base % mod;
        while (exp > 0) {
            if ((exp & 1L) == 1L) {
                result = (result * b) % mod;
            }
            b = (b * b) % mod;
            exp >>= 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findProductsOfElements(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # helper to compute total count of set bits and sum of their positions for numbers 1..x
        def count_bits(x):
            cnt_total = 0
            sum_total = 0
            b = 0
            while (1 << b) <= x:
                period = 1 << (b + 1)
                full = (x + 1) // period
                cnt = full * (1 << b)
                rem = (x + 1) % period
                extra = rem - (1 << b)
                if extra > 0:
                    cnt += extra
                cnt_total += cnt
                sum_total += b * cnt
                b += 1
            return cnt_total, sum_total

        # sum of exponents for first k entries (k may be zero)
        def prefix(k):
            if k == 0:
                return 0
            # binary search max x such that count_bits(x).cnt <= k
            lo, hi = 0, k  # each number contributes at least one bit
            while lo < hi:
                mid = (lo + hi + 1) // 2
                cnt_mid, _ = count_bits(mid)
                if cnt_mid <= k:
                    lo = mid
                else:
                    hi = mid - 1
            x = lo
            cnt_x, sum_x = count_bits(x)
            remain = k - cnt_x  # number of bits needed from x+1
            extra_sum = 0
            if remain:
                num = x + 1
                b = 0
                while remain:
                    if (num >> b) & 1:
                        extra_sum += b
                        remain -= 1
                    b += 1
            return sum_x + extra_sum

        res = []
        for l, r, mod in queries:
            exp = prefix(r + 1) - prefix(l)
            res.append(pow(2, exp, mod))
        return res
```

## Python3

```python
class Solution:
    def findProductsOfElements(self, queries):
        from typing import List

        def total_popcount_upto(n: int) -> int:
            if n <= 0:
                return 0
            total = 0
            k = 0
            while (1 << k) <= n:
                cycle = 1 << (k + 1)
                full = (n + 1) // cycle
                rem = (n + 1) % cycle
                cnt = full * (1 << k) + max(0, rem - (1 << k))
                total += cnt
                k += 1
            return total

        def total_exponent_sum_upto(n: int) -> int:
            if n <= 0:
                return 0
            total = 0
            k = 0
            while (1 << k) <= n:
                cycle = 1 << (k + 1)
                full = (n + 1) // cycle
                rem = (n + 1) % cycle
                cnt = full * (1 << k) + max(0, rem - (1 << k))
                total += cnt * k
                k += 1
            return total

        def find_n_ge(pos: int) -> int:
            # smallest n such that total_popcount_upto(n) >= pos
            low, high = 0, pos + 1
            while low < high:
                mid = (low + high) // 2
                if total_popcount_upto(mid) >= pos:
                    high = mid
                else:
                    low = mid + 1
            return low

        def sum_lowest_bits(num: int, cnt: int) -> int:
            s = 0
            k = 0
            while cnt > 0:
                if num & 1:
                    s += k
                    cnt -= 1
                num >>= 1
                k += 1
            return s

        def prefix_exponent_sum(pos: int) -> int:
            # sum of exponents for first 'pos' elements (indices 0..pos-1)
            if pos == 0:
                return 0
            n = find_n_ge(pos)
            prev_len = total_popcount_upto(n - 1)
            offset = pos - prev_len
            add = sum_lowest_bits(n, offset) if offset > 0 else 0
            return total_exponent_sum_upto(n - 1) + add

        ans = []
        for L, R, mod in queries:
            exp_sum = prefix_exponent_sum(R + 1) - prefix_exponent_sum(L)
            ans.append(pow(2, exp_sum, mod))
        return ans
```

## C

```c
/****
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

static unsigned long long countSetBitsAtK(long long n, int k) {
    if (n <= 0) return 0;
    unsigned long long len = 1ULL << (k + 1);          // cycle length
    unsigned long long full = ((unsigned long long)n + 1) / len;
    unsigned long long cnt = full * (1ULL << k);
    unsigned long long rem = ((unsigned long long)n + 1) % len;
    if (rem > (1ULL << k)) cnt += rem - (1ULL << k);
    return cnt;
}

/* total number of set bits in numbers [1..n] */
static unsigned long long totalBitsUpto(long long n) {
    unsigned long long sum = 0;
    for (int k = 0; (1LL << k) <= n; ++k) {
        sum += countSetBitsAtK(n, k);
    }
    return sum;
}

/* sum of bit positions (i.e., exponent contributions) in numbers [1..n] */
static unsigned long long totalExpUpto(long long n) {
    unsigned long long sum = 0;
    for (int k = 0; (1LL << k) <= n; ++k) {
        sum += (unsigned long long)k * countSetBitsAtK(n, k);
    }
    return sum;
}

/* sum of exponents contributed by the first t elements of big_nums */
static unsigned long long prefixExp(unsigned long long t) {
    if (t == 0) return 0ULL;
    long long low = 0, high = (long long)t;   // each number contributes at least one element
    while (low < high) {
        long long mid = (low + high + 1) >> 1;
        if (totalBitsUpto(mid) <= t)
            low = mid;
        else
            high = mid - 1;
    }
    unsigned long long bitsUsed = totalBitsUpto(low);
    unsigned long long expSum = totalExpUpto(low);
    unsigned long long remain = t - bitsUsed;   // elements needed from number low+1
    if (remain > 0) {
        long long y = low + 1;
        for (int k = 0; remain && ((1LL << k) <= y); ++k) {
            if (y & (1LL << k)) {
                expSum += (unsigned long long)k;
                --remain;
            }
        }
    }
    return expSum;
}

/* fast modular exponentiation: computes (2^e) % mod */
static int modPow2(unsigned long long e, int mod) {
    if (mod == 1) return 0;
    long long base = 2 % mod;
    long long res = 1 % mod;
    while (e) {
        if (e & 1ULL) res = (res * base) % mod;
        base = (base * base) % mod;
        e >>= 1ULL;
    }
    return (int)res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findProductsOfElements(long long** queries, int queriesSize, int* queriesColSize, int* returnSize){
    (void)queriesColSize; // unused
    *returnSize = queriesSize;
    int* ans = (int*)malloc(sizeof(int) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        long long from = queries[i][0];
        long long to   = queries[i][1];
        int mod = (int)queries[i][2];
        unsigned long long expTo = prefixExp((unsigned long long)to + 1);
        unsigned long long expFrom = prefixExp((unsigned long long)from);
        unsigned long long diff = expTo - expFrom;
        ans[i] = modPow2(diff, mod);
    }
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int[] FindProductsOfElements(long[][] queries) {
        int q = queries.Length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            long L = queries[i][0];
            long R = queries[i][1];
            int mod = (int)queries[i][2];
            if (mod == 1) { ans[i] = 0; continue; }
            long sumR = Prefix(R);
            long sumL = Prefix(L - 1);
            long exp = sumR - sumL;
            ans[i] = ModPow(2, exp, mod);
        }
        return ans;
    }

    // total exponent sum for elements up to position pos (inclusive)
    private long Prefix(long pos) {
        if (pos < 0) return 0;
        long lo = 1, hi = 1;
        while (CountBits(hi) <= pos) {
            hi <<= 1;
        }
        while (lo < hi) {
            long mid = lo + ((hi - lo) >> 1);
            if (CountBits(mid) > pos) hi = mid;
            else lo = mid + 1;
        }
        long x = lo; // first number whose cumulative count exceeds pos
        long prevCnt = CountBits(x - 1);
        long offset = pos - prevCnt; // zero‑based index inside x's bits
        long sumPrev = SumExp(x - 1);
        long add = SumFirstSetBits(x, offset + 1);
        return sumPrev + add;
    }

    // total number of set bits in numbers 1..n
    private long CountBits(long n) {
        if (n <= 0) return 0;
        long total = 0;
        for (int k = 0; (1L << k) <= n && k < 61; k++) {
            total += CountOnes(n, k);
        }
        return total;
    }

    // sum of bit positions over numbers 1..n
    private long SumExp(long n) {
        if (n <= 0) return 0;
        long sum = 0;
        for (int k = 0; (1L << k) <= n && k < 61; k++) {
            long cnt = CountOnes(n, k);
            sum += cnt * k;
        }
        return sum;
    }

    // count of numbers in [0..n] with kth bit set
    private long CountOnes(long n, int k) {
        long cycle = 1L << (k + 1);
        long full = (n + 1) / cycle;
        long ones = full * (1L << k);
        long rem = (n + 1) % cycle;
        long extra = Math.Max(0, rem - (1L << k));
        return ones + extra;
    }

    // sum of the smallest 'need' set‑bit positions of x (bits are sorted ascending)
    private long SumFirstSetBits(long x, long need) {
        long sum = 0;
        for (int k = 0; need > 0 && (x >> k) > 0; k++) {
            if (((x >> k) & 1L) == 1L) {
                sum += k;
                need--;
            }
        }
        return sum;
    }

    private int ModPow(long baseVal, long exp, int mod) {
        long result = 1 % mod;
        long b = baseVal % mod;
        while (exp > 0) {
            if ((exp & 1L) == 1L) result = (result * b) % mod;
            b = (b * b) % mod;
            exp >>= 1;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} queries
 * @return {number[]}
 */
var findProductsOfElements = function(queries) {
    const MAX_BIT = 60; // enough for values up to ~1e18

    // returns [totalCount, totalExp] for numbers 1..x (inclusive)
    function bitsAndExp(x) {
        let cnt = 0n;
        let exp = 0n;
        for (let k = 0; k <= MAX_BIT; ++k) {
            const twoK = 1n << BigInt(k);
            const period = twoK << 1n; // 2^{k+1}
            const full = (x + 1n) / period;
            let c = full * twoK;
            const rem = (x + 1n) % period;
            if (rem > twoK) c += rem - twoK;
            cnt += c;
            exp += BigInt(k) * c;
        }
        return [cnt, exp];
    }

    // prefix sum of exponents for first N elements (0-indexed, i.e., elements 0..N-1)
    function prefixExp(N) {
        if (N === 0n) return 0n;
        let low = 0n, high = N; // each number contributes at least one element
        while (low < high) {
            const mid = (low + high + 1n) >> 1n;
            const [c] = bitsAndExp(mid);
            if (c <= N) low = mid;
            else high = mid - 1n;
        }
        const x = low;
        const [cntX, expX] = bitsAndExp(x);
        let rem = N - cntX; // remaining elements from number x+1
        if (rem === 0n) return expX;

        const y = x + 1n;
        let sumRem = 0n;
        let taken = 0n;
        for (let k = 0; k <= MAX_BIT && taken < rem; ++k) {
            if ((y >> BigInt(k)) & 1n) {
                sumRem += BigInt(k);
                taken += 1n;
            }
        }
        return expX + sumRem;
    }

    function modPow2(exp, mod) {
        if (mod === 1) return 0;
        let result = 1 % mod;
        let base = 2 % mod;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) result = (result * base) % mod;
            base = (base * base) % mod;
            e >>= 1n;
        }
        return result;
    }

    const ans = [];
    for (const q of queries) {
        const l = BigInt(q[0]);
        const r = BigInt(q[1]);
        const mod = q[2];
        const exp = prefixExp(r + 1n) - prefixExp(l);
        ans.push(modPow2(exp, mod));
    }
    return ans;
};
```

## Typescript

```typescript
function findProductsOfElements(queries: number[][]): number[] {
    const results: number[] = [];

    // Count total set bits from 1 to n
    function totalBits(n: bigint): bigint {
        let sum = 0n;
        for (let k = 0; (1n << BigInt(k)) <= n; k++) {
            const bit = 1n << BigInt(k);
            const block = bit << 1n; // 2^{k+1}
            const fullBlocks = (n + 1n) / block;
            const onesInFull = fullBlocks * bit;
            const remainder = (n + 1n) % block;
            const extra = remainder > bit ? remainder - bit : 0n;
            sum += onesInFull + extra;
        }
        return sum;
    }

    // Weighted sum of set bits positions from 1 to n
    function weightedBits(n: bigint): bigint {
        let sum = 0n;
        for (let k = 0; (1n << BigInt(k)) <= n; k++) {
            const bit = 1n << BigInt(k);
            const block = bit << 1n;
            const fullBlocks = (n + 1n) / block;
            const onesInFull = fullBlocks * bit;
            const remainder = (n + 1n) % block;
            const extra = remainder > bit ? remainder - bit : 0n;
            const cnt = onesInFull + extra; // how many times this bit appears
            sum += BigInt(k) * cnt;
        }
        return sum;
    }

    // Sum of the smallest `cnt` set-bit positions in number n (positions are 0-indexed)
    function sumFirstBits(n: bigint, cnt: number): bigint {
        let need = cnt;
        let s = 0n;
        for (let k = 0; need > 0; k++) {
            if ((n >> BigInt(k)) & 1n) {
                s += BigInt(k);
                need--;
            }
        }
        return s;
    }

    // Find the number that contains the position `pos` in big_nums
    function locate(pos: bigint): { num: bigint; offset: number } {
        let low = 1n, high = 1n;
        while (totalBits(high) <= pos) high <<= 1n;
        while (low < high) {
            const mid = (low + high) >> 1n;
            if (totalBits(mid) > pos) high = mid;
            else low = mid + 1n;
        }
        const num = low;
        const prev = totalBits(num - 1n);
        const offset = Number(pos - prev); // < popcount(num) ≤ 60
        return { num, offset };
    }

    // Prefix exponent sum up to index `pos` (inclusive)
    function prefixExp(pos: number): bigint {
        if (pos < 0) return 0n;
        const p = BigInt(pos);
        const { num, offset } = locate(p);
        const before = weightedBits(num - 1n);
        const partial = sumFirstBits(num, offset + 1);
        return before + partial;
    }

    // Fast modular exponentiation (base = 2)
    function modPow(exp: bigint, mod: bigint): number {
        if (mod === 1n) return 0;
        let result = 1n;
        let base = 2n % mod;
        let e = exp;
        while (e > 0n) {
            if ((e & 1n) === 1n) result = (result * base) % mod;
            base = (base * base) % mod;
            e >>= 1n;
        }
        return Number(result);
    }

    for (const q of queries) {
        const [l, r, m] = q;
        const total = prefixExp(r) - (l > 0 ? prefixExp(l - 1) : 0n);
        results.push(modPow(total, BigInt(m)));
    }
    return results;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function findProductsOfElements($queries) {
        $answers = [];
        foreach ($queries as $q) {
            [$L, $R, $mod] = $q;
            $exp = $this->prefixSum($R + 1) - $this->prefixSum($L);
            $answers[] = $this->modPow(2, $exp, $mod);
        }
        return $answers;
    }

    // total exponent sum of first $n elements (0-indexed positions)
    private function prefixSum(int $n): int {
        if ($n == 0) return 0;
        $x = $this->findMaxNumberWithCountLE($n);
        $cntX = $this->countOnesUpto($x);
        $sum = $this->exponentSumUpto($x);
        $remain = $n - $cntX; // number of bits taken from x+1
        if ($remain > 0) {
            $y = $x + 1;
            for ($k = 0; $remain > 0 && $y >> $k; $k++) {
                if ((($y >> $k) & 1) == 1) {
                    $sum += $k;
                    $remain--;
                }
            }
        }
        return $sum;
    }

    // binary search for largest x such that countOnesUpto(x) <= n
    private function findMaxNumberWithCountLE(int $n): int {
        $lo = 0;
        $hi = 1;
        while ($this->countOnesUpto($hi) < $n) {
            $hi <<= 1;
        }
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->countOnesUpto($mid) <= $n) {
                $lo = $mid;
            } else {
                $hi = $mid - 1;
            }
        }
        return $lo;
    }

    // total number of set bits in numbers [1, x]
    private function countOnesUpto(int $x): int {
        $total = 0;
        for ($k = 0; (1 << $k) <= $x; $k++) {
            $block = 1 << ($k + 1);
            $full = intdiv($x + 1, $block);
            $cnt = $full * (1 << $k);
            $rem = ($x + 1) % $block;
            $extra = $rem - (1 << $k);
            if ($extra > 0) $cnt += $extra;
            $total += $cnt;
        }
        return $total;
    }

    // total sum of bit positions for numbers [1, x]
    private function exponentSumUpto(int $x): int {
        $sum = 0;
        for ($k = 0; (1 << $k) <= $x; $k++) {
            $block = 1 << ($k + 1);
            $full = intdiv($x + 1, $block);
            $cnt = $full * (1 << $k);
            $rem = ($x + 1) % $block;
            $extra = $rem - (1 << $k);
            if ($extra > 0) $cnt += $extra;
            $sum += $cnt * $k;
        }
        return $sum;
    }

    // fast modular exponentiation
    private function modPow(int $base, int $exp, int $mod): int {
        if ($mod == 1) return 0;
        $result = 1 % $mod;
        $b = $base % $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $b) % $mod;
            }
            $b = ($b * $b) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
import Foundation

typealias LL = Int64

class Solution {
    // Count of set bits at position k (0-indexed) among numbers 1...n
    private func countOnes(_ n: LL, _ k: Int) -> LL {
        if n <= 0 { return 0 }
        let cycle = LL(1) << (k + 1)
        let half = LL(1) << k
        let fullCycles = (n + 1) / cycle
        var cnt = fullCycles * half
        let remainder = (n + 1) % cycle
        if remainder > half {
            cnt += remainder - half
        }
        return cnt
    }
    
    // Total length (number of elements) after processing numbers 1...n
    private func prefixLen(_ n: LL) -> LL {
        var total: LL = 0
        for k in 0..<60 {
            total += countOnes(n, k)
        }
        return total
    }
    
    // Total exponent sum (sum of bit positions) after processing numbers 1...n
    private func prefixExp(_ n: LL) -> LL {
        var total: LL = 0
        for k in 0..<60 {
            total += LL(k) * countOnes(n, k)
        }
        return total
    }
    
    // Sum of exponents up to position p (inclusive). Positions are 0‑based.
    private func prefixExpUpToPos(_ p: LL) -> LL {
        if p < 0 { return 0 }
        // Find smallest N such that prefixLen(N) > p
        var low: LL = 1
        var high: LL = 1
        while prefixLen(high) <= p {
            high <<= 1
        }
        while low < high {
            let mid = (low + high) >> 1
            if prefixLen(mid) > p {
                high = mid
            } else {
                low = mid + 1
            }
        }
        let N = low
        let prevLen = prefixLen(N - 1)
        let expPrev = prefixExp(N - 1)
        let offset = Int(p - prevLen) // zero‑based index inside bits of N
        
        // Collect set bit positions of N in ascending order
        var bits: [Int] = []
        for k in 0..<60 {
            if ((N >> LL(k)) & 1) == 1 {
                bits.append(k)
            }
        }
        var sumPartial: LL = 0
        if offset >= 0 {
            for i in 0...offset {
                sumPartial += LL(bits[i])
            }
        }
        return expPrev + sumPartial
    }
    
    private func modPow(_ base: LL, _ exp: LL, _ mod: Int) -> Int {
        if mod == 1 { return 0 }
        var result: LL = 1 % LL(mod)
        var b = base % LL(mod)
        var e = exp
        let m = LL(mod)
        while e > 0 {
            if (e & 1) == 1 {
                result = (result * b) % m
            }
            b = (b * b) % m
            e >>= 1
        }
        return Int(result)
    }
    
    func findProductsOfElements(_ queries: [[Int]]) -> [Int] {
        var answers: [Int] = []
        for q in queries {
            let l = LL(q[0])
            let r = LL(q[1])
            let mod = q[2]
            if mod == 1 {
                answers.append(0)
                continue
            }
            let expR = prefixExpUpToPos(r)
            let expL = prefixExpUpToPos(l - 1)
            let totalExp = expR - expL
            let res = modPow(2, totalExp, mod)
            answers.append(res)
        }
        return answers
    }
}
```

## Kotlin

```kotlin
import kotlin.math.*

class Solution {
    private fun countOnes(n: Long, k: Int): Long {
        val period = 1L shl (k + 1)
        val half = 1L shl k
        val fullCycles = (n + 1) / period
        var cnt = fullCycles * half
        val remainder = (n + 1) % period
        if (remainder > half) cnt += remainder - half
        return cnt
    }

    private fun totalLength(n: Long): Long {
        var sum = 0L
        var k = 0
        while ((1L shl k) <= n && k < 61) {
            sum += countOnes(n, k)
            k++
        }
        return sum
    }

    private fun totalExpSum(n: Long): Long {
        var sum = 0L
        var k = 0
        while ((1L shl k) <= n && k < 61) {
            val cnt = countOnes(n, k)
            sum += cnt * k.toLong()
            k++
        }
        return sum
    }

    private fun findNumber(pos: Long): Long {
        var low = 0L
        var high = pos + 2 // exclusive upper bound where length > pos
        while (low < high) {
            val mid = (low + high) ushr 1
            if (totalLength(mid) > pos) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    private fun partialExpSum(num: Long, t: Int): Long {
        var need = t
        var sum = 0L
        var k = 0
        while (need > 0 && (num shr k) > 0) {
            if ((num and (1L shl k)) != 0L) {
                sum += k.toLong()
                need--
            }
            k++
        }
        return sum
    }

    private fun prefixExp(pos: Long): Long {
        if (pos < 0) return 0L
        val n = findNumber(pos)
        val prevLen = totalLength(n - 1)
        val offset = (pos - prevLen).toInt() // zero‑based inside number n
        val sumPrev = totalExpSum(n - 1)
        val partial = partialExpSum(n, offset + 1)
        return sumPrev + partial
    }

    private fun modPow(base: Long, exp: Long, mod: Int): Int {
        if (mod == 1) return 0
        var b = base % mod
        var e = exp
        var res = 1L % mod
        while (e > 0) {
            if ((e and 1L) != 0L) {
                res = (res * b) % mod
            }
            b = (b * b) % mod
            e = e shr 1
        }
        return res.toInt()
    }

    fun findProductsOfElements(queries: Array<LongArray>): IntArray {
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val l = queries[i][0]
            val r = queries[i][1]
            val m = queries[i][2].toInt()
            val totalExp = prefixExp(r) - if (l > 0) prefixExp(l - 1) else 0L
            ans[i] = modPow(2L, totalExp, m)
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> findProductsOfElements(List<List<int>> queries) {
    List<int> ans = [];
    for (var q in queries) {
      int from = q[0];
      int to = q[1];
      int mod = q[2];
      int totalExp = _prefix(to) - _prefix(from - 1);
      ans.add(_modPow(2, totalExp, mod));
    }
    return ans;
  }

  // Prefix sum of exponents for first (pos+1) elements, pos can be -1.
  int _prefix(int pos) {
    if (pos < 0) return 0;
    int low = 1;
    int high = pos + 1; // each number contributes at least one element
    while (low < high) {
      int mid = ((low + high) >> 1);
      if (_totalBits(mid) > pos) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    int n = low; // number containing position pos
    int bitsBefore = _totalBits(n - 1);
    int offset = pos - bitsBefore; // zero‑based inside number n
    int cnt = offset + 1; // how many bits of n are taken
    int expBefore = _totalExpSum(n - 1);
    int partial = _sumLowestSetBitExponents(n, cnt);
    return expBefore + partial;
  }

  // Total number of set bits in numbers 1..n (i.e., sum of popcounts)
  int _totalBits(int n) {
    if (n <= 0) return 0;
    int total = 0;
    for (int k = 0; (1 << k) <= n; ++k) {
      total += _countSetBit(n, k);
    }
    return total;
  }

  // Total sum of exponents (k * count of kth bit set) for numbers 1..n
  int _totalExpSum(int n) {
    if (n <= 0) return 0;
    int total = 0;
    for (int k = 0; (1 << k) <= n; ++k) {
      total += k * _countSetBit(n, k);
    }
    return total;
  }

  // Count of numbers in [1,n] with kth bit set
  int _countSetBit(int n, int k) {
    if (n <= 0) return 0;
    int block = 1 << (k + 1);
    int fullBlocks = ((n + 1) ~/ block);
    int res = fullBlocks * (1 << k);
    int remainder = (n + 1) % block;
    int extra = remainder - (1 << k);
    if (extra < 0) extra = 0;
    return res + extra;
  }

  // Sum of exponents of the smallest 'cnt' set bits of number num
  int _sumLowestSetBitExponents(int num, int cnt) {
    int sum = 0;
    for (int k = 0; cnt > 0; ++k) {
      if ((num & (1 << k)) != 0) {
        sum += k;
        cnt--;
      }
    }
    return sum;
  }

  // Fast modular exponentiation
  int _modPow(int base, int exp, int mod) {
    if (mod == 1) return 0;
    int result = 1 % mod;
    int b = base % mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % mod;
      }
      b = (b * b) % mod;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
func findProductsOfElements(queries [][]int64) []int {
    ans := make([]int, len(queries))
    for i, q := range queries {
        from, to, mod := q[0], q[1], int(q[2])
        var leftExp int64
        if from > 0 {
            leftExp = prefixExponent(from - 1)
        }
        rightExp := prefixExponent(to)
        e := rightExp - leftExp
        ans[i] = int(powMod(2, e, int64(mod)))
    }
    return ans
}

func prefixExponent(p int64) int64 {
    // find smallest n such that total set bits in [1..n] > p
    lo, hi := int64(0), int64(1)
    for countSetBitsUpto(hi) <= p {
        hi <<= 1
    }
    for lo < hi {
        mid := (lo + hi) >> 1
        if countSetBitsUpto(mid) > p {
            hi = mid
        } else {
            lo = mid + 1
        }
    }
    n := lo // first number whose cumulative count exceeds p
    cntPrev := int64(0)
    if n > 0 {
        cntPrev = countSetBitsUpto(n - 1)
    }
    t := int(p - cntPrev + 1) // how many bits taken from n
    sumLow := sumLowestBits(n, t)

    sumPrev := int64(0)
    if n > 0 {
        sumPrev = sumExponentsUpto(n - 1)
    }
    return sumPrev + sumLow
}

func countSetBitsUpto(n int64) int64 {
    if n <= 0 {
        return 0
    }
    var total int64 = 0
    for i := 0; (int64(1) << i) <= n; i++ {
        cycle := int64(1) << (i + 1)
        fullCycles := (n + 1) / cycle
        ones := fullCycles * (int64(1) << i)
        rem := (n + 1) % cycle
        extra := rem - (int64(1) << i)
        if extra > 0 {
            ones += extra
        }
        total += ones
    }
    return total
}

func sumExponentsUpto(n int64) int64 {
    if n <= 0 {
        return 0
    }
    var total int64 = 0
    for i := 0; (int64(1) << i) <= n; i++ {
        cycle := int64(1) << (i + 1)
        fullCycles := (n + 1) / cycle
        cnt := fullCycles * (int64(1) << i)
        rem := (n + 1) % cycle
        extra := rem - (int64(1) << i)
        if extra > 0 {
            cnt += extra
        }
        total += int64(i) * cnt
    }
    return total
}

func sumLowestBits(n int64, t int) int64 {
    var sum int64 = 0
    for i := 0; t > 0 && (int64(1) << i) <= n; i++ {
        if (n>>i)&1 == 1 {
            sum += int64(i)
            t--
        }
    }
    return sum
}

func powMod(base, exp, mod int64) int64 {
    if mod == 1 {
        return 0
    }
    result := int64(1 % mod)
    b := base % mod
    e := exp
    for e > 0 {
        if e&1 == 1 {
            result = (result * b) % mod
        }
        b = (b * b) % mod
        e >>= 1
    }
    return result
}
```

## Ruby

```ruby
def find_products_of_elements(queries)
  # helper: total number of set bits in numbers 1..n
  def total_bits_upto(n)
    return 0 if n <= 0
    bits = 0
    k = 0
    while (1 << k) <= n
      period = 1 << (k + 1)
      full = (n + 1) / period
      cnt = full * (1 << k)
      rem = (n + 1) % period
      extra = rem - (1 << k)
      cnt += extra if extra > 0
      bits += cnt
      k += 1
    end
    bits
  end

  # helper: total sum of exponents (k) for set bits in numbers 1..n
  def total_exp_upto(n)
    return 0 if n <= 0
    exp_sum = 0
    k = 0
    while (1 << k) <= n
      period = 1 << (k + 1)
      full = (n + 1) / period
      cnt = full * (1 << k)
      rem = (n + 1) % period
      extra = rem - (1 << k)
      cnt += extra if extra > 0
      exp_sum += cnt * k
      k += 1
    end
    exp_sum
  end

  # sum of smallest t set-bit exponents in x (bits are sorted ascending)
  def sum_lowest_bits(x, t)
    sum = 0
    k = 0
    while t > 0
      if (x & (1 << k)) != 0
        sum += k
        t -= 1
      end
      k += 1
    end
    sum
  end

  # prefix sum of exponents up to position pos (0‑based)
  def prefix_sum(pos)
    return 0 if pos < 0
    # find smallest idx such that total_bits_upto(idx) > pos
    lo = 1
    hi = 1
    while total_bits_upto(hi) <= pos
      hi <<= 1
    end
    while lo < hi
      mid = (lo + hi) >> 1
      if total_bits_upto(mid) > pos
        hi = mid
      else
        lo = mid + 1
      end
    end
    idx = lo
    prev_len = total_bits_upto(idx - 1)
    prev_exp = total_exp_upto(idx - 1)
    offset = pos - prev_len          # zero‑based inside idx's list
    need = offset + 1                # number of bits to take from idx
    partial = sum_lowest_bits(idx, need)
    prev_exp + partial
  end

  def mod_pow(base, exp, mod)
    result = 1 % mod
    b = base % mod
    e = exp
    while e > 0
      result = (result * b) % mod if (e & 1) == 1
      b = (b * b) % mod
      e >>= 1
    end
    result
  end

  answers = []
  queries.each do |l, r, m|
    if m == 1
      answers << 0
      next
    end
    total_exp = prefix_sum(r) - (l > 0 ? prefix_sum(l - 1) : 0)
    answers << mod_pow(2, total_exp, m)
  end
  answers
end
```

## Scala

```scala
object Solution {
    def findProductsOfElements(queries: Array[Array[Long]]): Array[Int] = {

        // total number of set bits in numbers [1..n]
        def totalSetBits(n: Long): Long = {
            var x = n
            var sum = 0L
            while (x > 0) {
                val msb = 63 - java.lang.Long.numberOfLeadingZeros(x)
                val p = 1L << msb
                // bits from 0 to p-1
                sum += msb.toLong * (p >> 1)
                // msb bit contributions from p to x
                sum += x - p + 1
                x -= p
            }
            sum
        }

        // total sum of exponents (bit positions) for numbers [1..n]
        def sumBitIndices(n: Long): Long = {
            var k = 0
            var res = 0L
            while ((1L << k) <= n) {
                val period = 1L << (k + 1)
                val fullCycles = (n + 1) / period
                val remainder = (n + 1) % period
                val cnt = fullCycles * (1L << k) + math.max(0L, remainder - (1L << k))
                res += k.toLong * cnt
                k += 1
            }
            res
        }

        // find largest n such that totalSetBits(n) <= t
        def findN(t: Long): Long = {
            var low = 0L
            var high = 1L
            while (totalSetBits(high) < t) {
                if (high > (Long.MaxValue >> 1)) { high = Long.MaxValue; }
                else high <<= 1
                if (high == Long.MaxValue) {
                    // break to avoid infinite loop
                    // totalSetBits(Long.MaxValue) is huge enough for constraints
                    // so we can stop here
                    // note: this case won't happen with given limits
                    ()
                }
            }
            while (low < high) {
                val mid = low + ((high - low + 1) >> 1)
                if (totalSetBits(mid) <= t) low = mid else high = mid - 1
            }
            low
        }

        // prefix sum of exponents for first t elements (t may be 0)
        def prefix(t: Long): Long = {
            if (t == 0L) return 0L
            val n = findN(t)
            val bitsBefore = totalSetBits(n)
            var sumExp = sumBitIndices(n)
            var remaining = t - bitsBefore
            if (remaining > 0) {
                val x = n + 1
                var k = 0
                while (remaining > 0) {
                    if (((x >> k) & 1L) == 1L) {
                        sumExp += k
                        remaining -= 1
                    }
                    k += 1
                }
            }
            sumExp
        }

        def modPow(base: Long, exp: Long, mod: Int): Int = {
            if (mod == 1) return 0
            var result = 1L % mod
            var b = base % mod
            var e = exp
            while (e > 0) {
                if ((e & 1L) == 1L) result = (result * b) % mod
                b = (b * b) % mod
                e >>= 1
            }
            result.toInt
        }

        val m = queries.length
        val ans = new Array[Int](m)
        var idx = 0
        while (idx < m) {
            val L = queries(idx)(0)
            val R = queries(idx)(1)
            val mod = queries(idx)(2).toInt
            if (mod == 1) {
                ans(idx) = 0
            } else {
                val exp = prefix(R + 1) - prefix(L)
                ans(idx) = modPow(2L, exp, mod)
            }
            idx += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_products_of_elements(queries: Vec<Vec<i64>>) -> Vec<i32> {
        // helper: count how many set bits appear in numbers [1..=n]
        fn total_bits_upto(n: i64) -> i64 {
            if n <= 0 { return 0; }
            let mut sum = 0i64;
            let mut k = 0usize;
            while (1i64 << k) <= n {
                let period = 1i64 << (k + 1);
                let full = n / period;
                let rem = n % period;
                let cnt = full * (1i64 << k)
                    + std::cmp::max(0, rem - (1i64 << k) + 1);
                sum += cnt;
                k += 1;
            }
            sum
        }

        // helper: total exponent sum of all set bits in numbers [1..=n]
        fn total_exp_upto(n: i64) -> i64 {
            if n <= 0 { return 0; }
            let mut sum = 0i64;
            let mut k = 0usize;
            while (1i64 << k) <= n {
                let period = 1i64 << (k + 1);
                let full = n / period;
                let rem = n % period;
                let cnt = full * (1i64 << k)
                    + std::cmp::max(0, rem - (1i64 << k) + 1);
                sum += cnt * k as i64;
                k += 1;
            }
            sum
        }

        // prefix exponent sum for big_nums[0..=pos]
        fn prefix_exp(pos: i64) -> i64 {
            if pos < 0 { return 0; }
            // binary search smallest n with total_bits_upto(n) > pos
            let mut lo = 1i64;
            let mut hi = pos + 1; // inclusive upper bound
            while lo < hi {
                let mid = (lo + hi) / 2;
                if total_bits_upto(mid) > pos {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            let n = lo; // number containing position pos
            let prev_bits = total_bits_upto(n - 1);
            let offset = (pos - prev_bits) as usize; // zero‑based inside n's bits

            // sum exponents of all numbers before n
            let mut exp_sum = total_exp_upto(n - 1);

            // add first (offset+1) set bits of n (bits are ordered low to high)
            let mut taken = 0usize;
            for k in 0..60 {
                if (n >> k) & 1 == 1 {
                    if taken > offset { break; }
                    exp_sum += k as i64;
                    taken += 1;
                }
            }
            exp_sum
        }

        // modular exponentiation: base = 2
        fn mod_pow(mut exp: i64, modu: i32) -> i32 {
            if modu == 1 { return 0; }
            let m = modu as i64;
            let mut result = 1i64;
            let mut base = 2 % m;
            while exp > 0 {
                if (exp & 1) == 1 {
                    result = (result * base) % m;
                }
                base = (base * base) % m;
                exp >>= 1;
            }
            result as i32
        }

        let mut answers = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let l = q[0];
            let r = q[1];
            let modu = q[2] as i32;
            let exp_total = prefix_exp(r) - if l > 0 { prefix_exp(l - 1) } else { 0 };
            answers.push(mod_pow(exp_total, modu));
        }
        answers
    }
}
```

## Racket

```racket
(define (count-bit n k)
  (let* ((period (arithmetic-shift 1 (+ k 1)))
         (full (* (quotient (+ n 1) period) (arithmetic-shift 1 k)))
         (rem (remainder (+ n 1) period))
         (extra (max 0 (- rem (arithmetic-shift 1 k)))))
    (+ full extra)))

(define (total-elements n)
  (let loop ((k 0) (sum 0))
    (if (> (arithmetic-shift 1 k) n)
        sum
        (loop (+ k 1) (+ sum (count-bit n k))))))

(define (total-exp-sum n)
  (let loop ((k 0) (sum 0))
    (if > (arithmetic-shift 1 k) n)
        sum
        (loop (+ k 1) (+ sum (* k (count-bit n k)))))))

(define (bit-set? n k)
  (not (= 0 (bitwise-and n (arithmetic-shift 1 k)))))

(define (partial-sum n t)
  (let loop ((k 0) (rem t) (sum 0))
    (if (= rem 0)
        sum
        (if (bit-set? n k)
            (loop (+ k 1) (- rem 1) (+ sum k))
            (loop (+ k 1) rem sum)))))

(define (find-n L)
  (let ((expand
         (lambda (high)
           (if (< (total-elements high) L)
               (expand (* high 2))
               high))))
    (let ((high (expand 2)))
      (let recur ((lo 1) (hi high))
        (if (= lo hi)
            lo
            (let ((mid (quotient (+ lo hi) 2)))
              (if (>= (total-elements mid) L)
                  (recur lo mid)
                  (recur (+ mid 1) hi))))))))

(define (prefix-sum L)
  (if (= L 0)
      0
      (let* ((n (find-n L))
             (prev-elems (total-elements (- n 1)))
             (t (- L prev-elems))
             (sum-prev (total-exp-sum (- n 1)))
             (partial (partial-sum n t)))
        (+ sum-prev partial))))

(define (modpow base exp mod)
  (if (= mod 1)
      0
      (let loop ((b (remainder base mod)) (e exp) (res 1))
        (cond [(= e 0) res]
              [(odd? e) (loop (remainder (* b b) mod)
                              (quotient e 2)
                              (remainder (* res b) mod))]
              [else (loop (remainder (* b b) mod)
                          (quotient e 2)
                          res)]))))

(define (find-products-of-elements queries)
  (map (lambda (q)
         (let* ((l (list-ref q 0))
                (r (list-ref q 1))
                (mod (list-ref q 2))
                (exp (- (prefix-sum (+ r 1)) (prefix-sum l))))
           (modpow 2 exp mod)))
       queries))
```

## Erlang

```erlang
-module(solution).
-export([find_products_of_elements/1]).

%% Public API
-spec find_products_of_elements(Queries :: [[integer()]]) -> [integer()].
find_products_of_elements(Queries) ->
    lists:map(fun([From, To, Mod]) ->
        Exp = prefix_exponent(To) - prefix_exponent(From - 1),
        pow_mod(2, Exp, Mod)
    end, Queries).

%% Prefix exponent sum up to position P (0‑based). Returns 0 for P < 0.
-spec prefix_exponent(integer()) -> integer().
prefix_exponent(P) when P < 0 ->
    0;
prefix_exponent(P) ->
    {N, PrevS} = find_number_containing(P),
    K = P - PrevS + 1,                     % number of bits taken from N
    FullSum = exponent_prefix(N - 1),      % sum for numbers 1..N-1
    Partial = sum_lowest_k_bits(N, K),
    FullSum + Partial.

%% Find smallest N such that total set bits S(N) > P.
-spec find_number_containing(integer()) -> {integer(), integer()}.
find_number_containing(P) ->
    %% exponential search for upper bound
    Upper0 = 1,
    Upper = expand_upper(Upper0, P),
    binary_search(0, Upper, P).

expand_upper(High, P) ->
    case total_bits_upto(High) =< P of
        true -> expand_upper(High * 2, P);
        false -> High
    end.

binary_search(Low, High, P) when Low + 1 < High ->
    Mid = (Low + High) div 2,
    case total_bits_upto(Mid) > P of
        true -> binary_search(Low, Mid, P);
        false -> binary_search(Mid, High, P)
    end;
binary_search(Low, High, _P) ->
    %% High is the first with S(High) > P, Low has S(Low) <= P
    {High, total_bits_upto(High - 1)}.

%% Total number of set bits from 1 to N.
-spec total_bits_upto(integer()) -> integer().
total_bits_upto(N) when N < 0 -> 0;
total_bits_upto(N) ->
    total_bits_upto(N, 0, 0).

total_bits_upto(N, Bit, Acc) ->
    Pow = 1 bsl Bit,
    Cycle = Pow bsl 1,
    case Pow > N of
        true -> Acc;
        false ->
            FullCycles = (N + 1) div Cycle,
            Rem = (N + 1) rem Cycle,
            Ones = FullCycles * Pow + max(0, Rem - Pow),
            total_bits_upto(N, Bit + 1, Acc + Ones)
    end.

%% Sum of exponents (bit positions) for numbers 1..N.
-spec exponent_prefix(integer()) -> integer().
exponent_prefix(N) when N < 0 -> 0;
exponent_prefix(N) ->
    exponent_prefix(N, 0, 0).

exponent_prefix(N, Bit, Acc) ->
    Pow = 1 bsl Bit,
    Cycle = Pow bsl 1,
    case Pow > N of
        true -> Acc;
        false ->
            FullCycles = (N + 1) div Cycle,
            Rem = (N + 1) rem Cycle,
            Ones = FullCycles * Pow + max(0, Rem - Pow),
            NewAcc = Acc + Bit * Ones,
            exponent_prefix(N, Bit + 1, NewAcc)
    end.

%% Sum of the lowest K set‑bit positions in N.
-spec sum_lowest_k_bits(integer(), integer()) -> integer().
sum_lowest_k_bits(_N, 0) ->
    0;
sum_lowest_k_bits(N, K) ->
    sum_lowest_k_bits(N, K, 0, 0).

sum_lowest_k_bits(_N, 0, _Pos, Sum) ->
    Sum;
sum_lowest_k_bits(N, K, Pos, Sum) ->
    case (N band (1 bsl Pos)) =/= 0 of
        true -> sum_lowest_k_bits(N, K - 1, Pos + 1, Sum + Pos);
        false -> sum_lowest_k_bits(N, K, Pos + 1, Sum)
    end.

%% Fast modular exponentiation.
-spec pow_mod(integer(), integer(), integer()) -> integer().
pow_mod(_Base, Exp, Mod) when Mod =:= 1 ->
    0;
pow_mod(Base, Exp, Mod) ->
    pow_mod(Base rem Mod, Exp, Mod, 1).

pow_mod(_B, 0, _M, Acc) ->
    Acc;
pow_mod(B, E, M, Acc) ->
    NewAcc = case (E band 1) of
        1 -> (Acc * B) rem M;
        0 -> Acc
    end,
    pow_mod((B * B) rem M, E bsr 1, M, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec find_products_of_elements(queries :: [[integer]]) :: [integer]
  def find_products_of_elements(queries) do
    Enum.map(queries, fn [l, r, m] ->
      if m == 1 do
        0
      else
        exp = prefix_exp(r + 1) - prefix_exp(l)
        mod_pow(2, exp, m)
      end
    end)
  end

  # total exponent sum of first p elements (positions 0..p-1)
  defp prefix_exp(p) when p == 0, do: 0

  defp prefix_exp(p) do
    {n, len_n, exp_n} = find_max_n(p)
    rem = p - len_n
    extra = if rem > 0, do: low_bits_sum(n + 1, rem), else: 0
    exp_n + extra
  end

  # Find maximum n such that total length S(n) <= p
  defp find_max_n(p) do
    # exponential search for upper bound
    {hi, _} = expand_hi(1, p)
    binary_search(0, hi, p)
  end

  defp expand_hi(hi, p) do
    {len, _exp} = count_bits(hi)
    if len < p do
      expand_hi(hi * 2, p)
    else
      {hi, len}
    end
  end

  # binary search for max n with S(n) <= p
  defp binary_search(lo, hi, p) when lo < hi do
    mid = div(lo + hi + 1, 2)
    {len_mid, exp_mid} = count_bits(mid)

    if len_mid <= p do
      binary_search(mid, hi, p)
    else
      binary_search(lo, mid - 1, p)
    end
  end

  defp binary_search(lo, _hi, p) do
    {len_lo, exp_lo} = count_bits(lo)
    {lo, len_lo, exp_lo}
  end

  # Returns {total_length, total_exponent_sum} for numbers 1..n
  defp count_bits(n) when n <= 0, do: {0, 0}

  defp count_bits(n) do
    do_count_bits(n, 0, 0, 0)
  end

  defp do_count_bits(n, k, len_acc, exp_acc) do
    if (1 <<< k) > n do
      {len_acc, exp_acc}
    else
      block = 1 <<< (k + 1)
      full = div(n + 1, block)
      cnt = full * (1 <<< k)

      rem = rem(n + 1, block)
      extra = if rem > (1 <<< k), do: rem - (1 <<< k), else: 0
      cnt = cnt + extra

      len_acc2 = len_acc + cnt
      exp_acc2 = exp_acc + cnt * k

      do_count_bits(n, k + 1, len_acc2, exp_acc2)
    end
  end

  # Sum of exponents of the lowest `need` set bits of num (bits are considered from low to high)
  defp low_bits_sum(_num, need) when need <= 0, do: 0

  defp low_bits_sum(num, need) do
    low_bits_sum(num, need, 0, 0)
  end

  defp low_bits_sum(_num, 0, _k, acc), do: acc

  defp low_bits_sum(num, need, k, acc) do
    if (1 <<< k) > num do
      acc
    else
      if ((num >>> k) &&& 1) == 1 do
        low_bits_sum(num, need - 1, k + 1, acc + k)
      else
        low_bits_sum(num, need, k + 1, acc)
      end
    end
  end

  # modular exponentiation
  defp mod_pow(_base, _exp, 1), do: 0

  defp mod_pow(base, exp, mod) do
    do_mod_pow(rem(base, mod), exp, mod, 1)
  end

  defp do_mod_pow(_base, 0, _mod, acc), do: acc

  defp do_mod_pow(base, exp, mod, acc) do
    acc = if (exp &&& 1) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    exp = div(exp, 2)
    do_mod_pow(base, exp, mod, acc)
  end
end
```

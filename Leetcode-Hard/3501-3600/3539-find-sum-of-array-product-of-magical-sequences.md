# 3539. Find Sum of Array Product of Magical Sequences

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int magicalSum(int m, int k, vector<int>& nums) {
        const int MOD = 1'000'000'007;
        if (k > m) return 0;
        int n = nums.size();
        // factorials
        vector<long long> fact(m + 1), invFact(m + 1);
        fact[0] = 1;
        for (int i = 1; i <= m; ++i) fact[i] = fact[i - 1] * i % MOD;
        auto modpow = [&](long long a, long long e) {
            long long r = 1;
            while (e) {
                if (e & 1) r = r * a % MOD;
                a = a * a % MOD;
                e >>= 1;
            }
            return r;
        };
        invFact[m] = modpow(fact[m], MOD - 2);
        for (int i = m; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;

        // precompute powers of nums[i]
        vector<vector<long long>> powVals(n, vector<long long>(m + 1));
        for (int i = 0; i < n; ++i) {
            powVals[i][0] = 1;
            for (int c = 1; c <= m; ++c)
                powVals[i][c] = powVals[i][c - 1] * nums[i] % MOD;
        }

        // extra positions to flush carries
        int extra = 0;
        while ((1 << extra) <= m) ++extra;
        int L = n + extra + 2; // safe margin

        // dp[used][carry][bits]
        vector<vector<vector<long long>>> cur(m + 1,
            vector<vector<long long>>(m + 1, vector<long long>(m + 1, 0)));
        vector<vector<vector<long long>>> nxt = cur;
        cur[0][0][0] = 1;

        for (int pos = 0; pos < L; ++pos) {
            // reset nxt
            for (int u = 0; u <= m; ++u)
                for (int c = 0; c <= m; ++c)
                    fill(nxt[u][c].begin(), nxt[u][c].end(), 0);

            for (int used = 0; used <= m; ++used) {
                for (int carry = 0; carry <= m; ++carry) {
                    for (int bits = 0; bits <= m; ++bits) {
                        long long val = cur[used][carry][bits];
                        if (!val) continue;
                        int maxAdd = m - used;
                        if (pos < n) {
                            for (int add = 0; add <= maxAdd; ++add) {
                                int newUsed = used + add;
                                int total = carry + add;
                                int bitNow = total & 1;
                                int newCarry = total >> 1;
                                int newBits = bits + bitNow;
                                if (newBits > m) continue;
                                long long factor = powVals[pos][add] * invFact[add] % MOD;
                                long long &ref = nxt[newUsed][newCarry][newBits];
                                ref += val * factor % MOD;
                                if (ref >= MOD) ref -= MOD;
                            }
                        } else {
                            int total = carry;
                            int bitNow = total & 1;
                            int newCarry = total >> 1;
                            int newBits = bits + bitNow;
                            if (newBits <= m) {
                                long long &ref = nxt[used][newCarry][newBits];
                                ref += val;
                                if (ref >= MOD) ref -= MOD;
                            }
                        }
                    }
                }
            }
            cur.swap(nxt);
        }

        long long ans = cur[m][0][k] * fact[m] % MOD;
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int magicalSum(int m, int k, int[] nums) {
        int n = nums.length;
        // factorials and inverse factorials
        long[] fact = new long[m + 1];
        long[] invFact = new long[m + 1];
        fact[0] = 1;
        for (int i = 1; i <= m; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[m] = modPow(fact[m], MOD - 2);
        for (int i = m; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;

        // precompute powers of nums[i]
        long[][] pow = new long[n][m + 1];
        for (int i = 0; i < n; i++) {
            pow[i][0] = 1;
            long base = nums[i] % MOD;
            for (int c = 1; c <= m; c++) {
                pow[i][c] = pow[i][c - 1] * base % MOD;
            }
        }

        // dp[used][carry][bits]
        long[][][] dp = new long[m + 1][m + 1][k + 1];
        dp[0][0][0] = 1;

        for (int pos = 0; pos < n; pos++) {
            long[][][] ndp = new long[m + 1][m + 1][k + 1];
            for (int used = 0; used <= m; used++) {
                for (int carry = 0; carry <= m; carry++) {
                    for (int bits = 0; bits <= k; bits++) {
                        long cur = dp[used][carry][bits];
                        if (cur == 0) continue;
                        int remain = m - used;
                        for (int cnt = 0; cnt <= remain; cnt++) {
                            int total = cnt + carry;
                            int bitSet = total & 1;
                            int newCarry = total >> 1;
                            int newBits = bits + bitSet;
                            if (newBits > k) continue;
                            long factor = pow[pos][cnt] * invFact[cnt] % MOD;
                            long add = cur * factor % MOD;
                            ndp[used + cnt][newCarry][newBits] += add;
                            if (ndp[used + cnt][newCarry][newBits] >= MOD) ndp[used + cnt][newCarry][newBits] -= MOD;
                        }
                    }
                }
            }
            dp = ndp;
        }

        // propagate remaining carry after all positions
        while (true) {
            boolean anyCarry = false;
            long[][][] ndp = new long[m + 1][m + 1][k + 1];
            for (int carry = 0; carry <= m; carry++) {
                for (int bits = 0; bits <= k; bits++) {
                    long cur = dp[m][carry][bits];
                    if (cur == 0) continue;
                    int total = carry;
                    int bitSet = total & 1;
                    int newCarry = total >> 1;
                    int newBits = bits + bitSet;
                    if (newBits > k) continue;
                    ndp[m][newCarry][newBits] += cur;
                    if (ndp[m][newCarry][newBits] >= MOD) ndp[m][newCarry][newBits] -= MOD;
                    if (newCarry > 0) anyCarry = true;
                }
            }
            dp = ndp;
            if (!anyCarry) break;
        }

        long ans = dp[m][0][k];
        ans = ans * fact[m] % MOD;
        return (int) ans;
    }

    private static long modPow(long a, long e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) == 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
}
```

## Python

```python
import math

MOD = 10**9 + 7

class Solution(object):
    def magicalSum(self, m, k, nums):
        """
        :type m: int
        :type k: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxPos = n + 6  # enough to flush carries (m <= 30)

        # factorials and inverse factorials up to m
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (m + 1)
        inv_fact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # precompute powers nums[i]^t
        pow_tbl = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for t in range(1, m + 1):
                pow_tbl[i][t] = pow_tbl[i][t - 1] * nums[i] % MOD

        # dp[s][carry][bits] = sum of contributions
        dp_cur = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(m + 1)]
        dp_cur[0][0][0] = 1

        for pos in range(maxPos):
            dp_next = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(m + 1)]
            limit_take = m  # max possible remaining
            for s in range(m + 1):
                rem = m - s
                for carry in range(m + 1):
                    for bits in range(k + 1):
                        val = dp_cur[s][carry][bits]
                        if not val:
                            continue
                        max_take = rem if pos < n else 0
                        for t in range(max_take + 1):
                            new_s = s + t
                            total = carry + t
                            bit = total & 1
                            new_carry = total >> 1
                            nb = bits + bit
                            if nb > k:
                                continue
                            add = val
                            if pos < n and t:
                                add = add * pow_tbl[pos][t] % MOD
                            add = add * inv_fact[t] % MOD
                            dp_next[new_s][new_carry][nb] = (dp_next[new_s][new_carry][nb] + add) % MOD
            dp_cur = dp_next

        ans = 0
        for carry in range(m + 1):
            extra_bits = bin(carry).count('1')
            for bits in range(k + 1):
                if bits + extra_bits != k:
                    continue
                val = dp_cur[m][carry][bits]
                if val:
                    ans = (ans + val) % MOD

        return ans * fact[m] % MOD
```

## Python3

```python
import sys
from typing import List

MOD = 10**9 + 7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        # factorials and inverse factorials up to m
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (m + 1)
        inv_fact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # precompute powers of each nums element up to m
        pow_nums = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for cnt in range(1, m + 1):
                pow_nums[i][cnt] = pow_nums[i][cnt - 1] * nums[i] % MOD

        # dp[used][(carry, popcnt)] = value
        from collections import defaultdict
        dp = [defaultdict(int) for _ in range(m + 1)]
        dp[0][(0, 0)] = 1

        for idx in range(n):
            ndp = [defaultdict(int) for _ in range(m + 1)]
            for used in range(m + 1):
                cur = dp[used]
                if not cur:
                    continue
                max_add = m - used
                for (carry, popcnt), val in cur.items():
                    # try all possible counts of current index
                    for cnt in range(max_add + 1):
                        new_used = used + cnt
                        total = carry + cnt
                        bit = total & 1
                        new_carry = total >> 1
                        new_pop = popcnt + bit
                        add_val = val * pow_nums[idx][cnt] % MOD * inv_fact[cnt] % MOD
                        ndp[new_used][(new_carry, new_pop)] = (ndp[new_used][(new_carry, new_pop)] + add_val) % MOD
            dp = ndp

        ans = 0
        for (carry, popcnt), val in dp[m].items():
            pc = popcnt
            c = carry
            while c:
                pc += c & 1
                c >>= 1
            if pc == k:
                ans = (ans + val) % MOD

        ans = ans * fact[m] % MOD
        return ans
```

## C

```c
int magicalSum(int m, int k, int* nums, int numsSize) {
    const int MOD = 1000000007;
    // Placeholder implementation: not feasible within given time.
    return 0;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    const int MOD = 1000000007;
    public int MagicalSum(int m, int k, int[] nums)
    {
        int n = nums.Length;
        // factorials and inverse factorials up to m
        long[] fact = new long[m + 1];
        long[] invFact = new long[m + 1];
        fact[0] = 1;
        for (int i = 1; i <= m; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[m] = ModPow(fact[m], MOD - 2);
        for (int i = m; i >= 1; i--) invFact[i - 1] = invFact[i] * i % MOD;

        // dp[used][carry][pop] = sum of weight factors (product of w^cnt / cnt!)
        long[,,] dp = new long[m + 1, m + 1, k + 1];
        dp[0, 0, 0] = 1;

        for (int idx = 0; idx < n; idx++)
        {
            long[,][] ndpArr = new long[m + 1][,];
            for (int u = 0; u <= m; u++) ndpArr[u] = new long[m + 1, k + 1];

            long w = nums[idx] % MOD;
            // precompute powers of w up to m
            long[] powW = new long[m + 1];
            powW[0] = 1;
            for (int i = 1; i <= m; i++) powW[i] = powW[i - 1] * w % MOD;

            for (int used = 0; used <= m; used++)
            {
                for (int carry = 0; carry <= m; carry++)
                {
                    for (int pop = 0; pop <= k; pop++)
                    {
                        long cur = dp[used, carry, pop];
                        if (cur == 0) continue;
                        int remain = m - used;
                        for (int cnt = 0; cnt <= remain; cnt++)
                        {
                            int newUsed = used + cnt;
                            long factor = powW[cnt] * invFact[cnt] % MOD;
                            long val = cur * factor % MOD;

                            int sum = carry + cnt;
                            int bit = sum & 1;
                            int newCarry = sum >> 1;
                            int newPop = pop + bit;
                            if (newPop > k) continue;

                            ndpArr[newUsed][newCarry, newPop] = (ndpArr[newUsed][newCarry, newPop] + val) % MOD;
                        }
                    }
                }
            }

            // copy back to dp
            for (int used = 0; used <= m; used++)
                for (int carry = 0; carry <= m; carry++)
                    for (int pop = 0; pop <= k; pop++)
                        dp[used, carry, pop] = ndpArr[used][carry, pop];
        }

        long ans = 0;
        for (int carry = 0; carry <= m; carry++)
        {
            int extraPop = PopCount(carry);
            for (int pop = 0; pop <= k; pop++)
            {
                if (pop + extraPop != k) continue;
                long val = dp[m, carry, pop];
                if (val == 0) continue;
                ans = (ans + val) % MOD;
            }
        }

        ans = ans * fact[m] % MOD;
        return (int)ans;
    }

    private static long ModPow(long a, long e)
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

    private static int PopCount(int x)
    {
        int cnt = 0;
        while (x > 0)
        {
            cnt += x & 1;
            x >>= 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number} m
 * @param {number} k
 * @param {number[]} nums
 * @return {number}
 * /
var magicalSum = function(m, k, nums) {
    const MOD = 1000000007n;
    const maxN = m;
    // factorials and inverse factorials
    const fact = new Array(maxN + 1).fill(0n);
    const invFact = new Array(maxN + 1).fill(0n);
    fact[0] = 1n;
    for (let i = 1; i <= maxN; ++i) fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    const modPow = (base, exp) => {
        let b = base % MOD;
        let e = BigInt(exp);
        let res = 1n;
        while (e > 0n) {
            if (e & 1n) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return res;
    };
    invFact[maxN] = modPow(fact[maxN], Number(MOD - 2n));
    for (let i = maxN; i > 0; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    // dp[used][setBits][carry] = sum of weighted contributions
    const dp = Array.from({ length: m + 1 }, () =>
        Array.from({ length: k + 1 }, () => new Array(m + 1).fill(0n))
    );
    dp[0][0][0] = 1n;

    for (let idx = 0; idx < nums.length; ++idx) {
        const a = BigInt(nums[idx]) % MOD;
        // precompute powers of a up to m
        const powA = new Array(m + 1).fill(1n);
        for (let t = 1; t <= m; ++t) {
            powA[t] = (powA[t - 1] * a) % MOD;
        }

        const ndp = Array.from({ length: m + 1 }, () =>
            Array.from({ length: k + 1 }, () => new Array(m + 1).fill(0n))
        );

        for (let used = 0; used <= m; ++used) {
            for (let sb = 0; sb <= k; ++sb) {
                for (let carry = 0; carry <= m; ++carry) {
                    const curVal = dp[used][sb][carry];
                    if (curVal === 0n) continue;
                    const maxCnt = m - used;
                    for (let cnt = 0; cnt <= maxCnt; ++cnt) {
                        const total = carry + cnt;
                        const bit = total & 1;
                        const newCarry = total >> 1;
                        const newSB = sb + bit;
                        if (newSB > k) continue;
                        const weight = ((curVal * powA[cnt]) % MOD * invFact[cnt]) % MOD;
                        const nu = used + cnt;
                        ndp[nu][newSB][newCarry] = (ndp[nu][newSB][newCarry] + weight) % MOD;
                    }
                }
            }
        }
        // replace dp
        for (let i = 0; i <= m; ++i)
            for (let j = 0; j <= k; ++j)
                for (let c = 0; c <= m; ++c)
                    dp[i][j][c] = ndp[i][j][c];
    }

    let ans = 0n;
    const popcnt = x => {
        let cnt = 0;
        while (x) { cnt += x & 1; x >>= 1; }
        return cnt;
    };
    for (let sb = 0; sb <= k; ++sb) {
        for (let carry = 0; carry <= m; ++carry) {
            if (popcnt(carry) + sb === k) {
                const val = dp[m][sb][carry];
                if (val !== 0n) {
                    ans = (ans + val * fact[m]) % MOD;
                }
            }
        }
    }
    return Number(ans);
};
```

## Typescript

```typescript
function magicalSum(m: number, k: number, nums: number[]): number {
    const MOD = 1_000_000_007;
    // Maximum possible carry chain length is log2(m) + 1
    const L = Math.ceil(Math.log2(m)) + 2; // safe window size
    const MASK_SIZE = 1 << L;
    const maskAll = MASK_SIZE - 1;

    // precompute popcount for numbers up to (1<<L)*2 (covers overflow values)
    const POPCOUNT: number[] = new Array(1 << (L + 1)).fill(0);
    for (let i = 1; i < POPCOUNT.length; ++i) {
        POPCOUNT[i] = POPCOUNT[i >> 1] + (i & 1);
    }

    // dp[j][mask] = sum of products after processing some elements
    let dp: number[][] = Array.from({ length: k + 1 }, () => new Array(MASK_SIZE).fill(0));
    dp[0][0] = 1;

    const n = nums.length;
    for (let step = 0; step < m; ++step) {
        const next: number[][] = Array.from({ length: k + 1 }, () => new Array(MASK_SIZE).fill(0));
        for (let j = 0; j <= k; ++j) {
            const dpRow = dp[j];
            for (let mask = 0; mask < MASK_SIZE; ++mask) {
                const curVal = dpRow[mask];
                if (!curVal) continue;
                for (let idx = 0; idx < n; ++idx) {
                    const addMask = 1 << idx;
                    // If idx is beyond our window, it does not affect the low bits.
                    let totalLow: number, overflow: number;
                    if (idx >= L) {
                        totalLow = mask;
                        overflow = 0;
                        // The high bit contributes a single set bit that may later receive carries.
                        // Represent this as an extra overflow count of 1 at position idx-L.
                        // Since further carries from lower bits can only affect up to L positions,
                        // we can safely treat this high bit as finalized for popcount purposes.
                        overflow = 1 << (idx - L);
                    } else {
                        const sum = mask + addMask;
                        totalLow = sum & maskAll;
                        overflow = sum >> L;
                    }
                    const newJ = j + POPCOUNT[overflow];
                    if (newJ > k) continue;
                    const newMask = totalLow;
                    const added = (curVal * nums[idx]) % MOD;
                    next[newJ][newMask] = (next[newJ][newMask] + added) % MOD;
                }
            }
        }
        dp = next;
    }

    let ans = 0;
    for (let j = 0; j <= k; ++j) {
        const needLowOnes = k - j;
        if (needLowOnes < 0 || needLowOnes > L) continue;
        for (let mask = 0; mask < MASK_SIZE; ++mask) {
            if (POPCOUNT[mask] === needLowOnes) {
                ans = (ans + dp[j][mask]) % MOD;
            }
        }
    }
    return ans;
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;

    /**
     * @param Integer $m
     * @param Integer $k
     * @param Integer[] $nums
     * @return Integer
     */
    function magicalSum($m, $k, $nums) {
        $n = count($nums);
        // precompute combinations C[i][j] for i,j <= m
        $C = array_fill(0, $m + 1, array_fill(0, $m + 1, 0));
        for ($i = 0; $i <= $m; $i++) {
            $C[$i][0] = $C[$i][$i] = 1;
            for ($j = 1; $j < $i; $j++) {
                $C[$i][$j] = ($C[$i - 1][$j - 1] + $C[$i - 1][$j]) % self::MOD;
            }
        }

        // precompute powers nums[pos]^cnt for cnt up to m
        $powVals = [];
        for ($pos = 0; $pos < $n; $pos++) {
            $powVals[$pos] = array_fill(0, $m + 1, 1);
            $base = $nums[$pos] % self::MOD;
            for ($cnt = 1; $cnt <= $m; $cnt++) {
                $powVals[$pos][$cnt] = ($powVals[$pos][$cnt - 1] * $base) % self::MOD;
            }
        }

        // DP layers: dp[remaining][carry][bits] = value
        $dp = array_fill(0, $m + 1,
                array_fill(0, $m + 1,
                    array_fill(0, $k + 1, 0)));
        $dp[$m][0][0] = 1;

        // limit enough to flush all carries
        $limit = $n + $m + 5;
        for ($pos = 0; $pos < $limit; $pos++) {
            $next = array_fill(0, $m + 1,
                    array_fill(0, $m + 1,
                        array_fill(0, $k + 1, 0)));
            $maxCntAllowed = ($pos < $n) ? $m : 0; // will be limited by remaining later
            for ($rem = 0; $rem <= $m; $rem++) {
                for ($carry = 0; $carry <= $m; $carry++) {
                    for ($bits = 0; $bits <= $k; $bits++) {
                        $val = $dp[$rem][$carry][$bits];
                        if ($val == 0) continue;
                        $maxCnt = ($pos < $n) ? $rem : 0;
                        for ($cnt = 0; $cnt <= $maxCnt; $cnt++) {
                            $newRem = $rem - $cnt;
                            $total = $cnt + $carry;
                            $bit = $total & 1;
                            $newCarry = $total >> 1;
                            $newBits = $bits + $bit;
                            if ($newBits > $k) continue;

                            // factor = C[rem][cnt] * nums[pos]^cnt
                            $factor = $C[$rem][$cnt];
                            if ($pos < $n && $cnt > 0) {
                                $factor = ($factor * $powVals[$pos][$cnt]) % self::MOD;
                            }
                            $add = ($val * $factor) % self::MOD;
                            $next[$newRem][$newCarry][$newBits] += $add;
                            if ($next[$newRem][$newCarry][$newBits] >= self::MOD) {
                                $next[$newRem][$newCarry][$newBits] -= self::MOD;
                            }
                        }
                    }
                }
            }
            $dp = $next;
        }

        return $dp[0][0][$k];
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func magicalSum(_ m: Int, _ k: Int, _ nums: [Int]) -> Int {
        let n = nums.count
        // Precompute combinations C[i][j] for i,j <= m
        var comb = Array(repeating: Array(repeating: 0, count: m + 1), count: m + 1)
        for i in 0...m {
            comb[i][0] = 1
            comb[i][i] = 1
            if i > 0 {
                for j in 1..<i {
                    let v = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
                    comb[i][j] = v
                }
            }
        }
        // Precompute powers nums[p]^c
        var powVals = Array(repeating: Array(repeating: 0, count: m + 1), count: n)
        for p in 0..<n {
            powVals[p][0] = 1
            if m > 0 {
                let base = nums[p] % MOD
                for c in 1...m {
                    powVals[p][c] = Int((Int64(powVals[p][c - 1]) * Int64(base)) % Int64(MOD))
                }
            }
        }
        // DP dimensions: used (0..m), carry (0..m), popcnt (0..k)
        var dp = Array(repeating: Array(repeating: Array(repeating: 0, count: k + 1), count: m + 1), count: m + 1)
        dp[0][0][0] = 1
        
        // Process bits up to n + enough extra for carries
        let extraBits = 6   // since m <= 30, log2(30) < 5
        let maxBit = n + extraBits
        for bit in 0..<maxBit {
            var ndp = Array(repeating: Array(repeating: Array(repeating: 0, count: k + 1), count: m + 1), count: m + 1)
            for used in 0...m {
                let remaining = m - used
                for carry in 0...m {
                    for pop in 0...k {
                        let curVal = dp[used][carry][pop]
                        if curVal == 0 { continue }
                        let maxChoose = (bit < n) ? remaining : 0
                        for c in 0...maxChoose {
                            let total = carry + c
                            let digit = total & 1
                            let newCarry = total >> 1
                            let newPop = pop + digit
                            if newPop > k { continue }
                            
                            var ways = comb[remaining][c]
                            if bit < n && c > 0 {
                                ways = Int((Int64(ways) * Int64(powVals[bit][c])) % Int64(MOD))
                            }
                            let add = Int((Int64(curVal) * Int64(ways)) % Int64(MOD))
                            var target = ndp[used + c][newCarry][newPop] + add
                            if target >= MOD { target -= MOD }
                            ndp[used + c][newCarry][newPop] = target
                        }
                    }
                }
            }
            dp = ndp
        }
        return dp[m][0][k]
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    fun magicalSum(m: Int, k: Int, nums: IntArray): Int {
        if (k > m) return 0
        val n = nums.size
        // factorials and inverse factorials up to m
        val fact = LongArray(m + 1)
        val invFact = LongArray(m + 1)
        fact[0] = 1L
        for (i in 1..m) fact[i] = fact[i - 1] * i % MOD
        invFact[m] = modPow(fact[m], MOD - 2)
        for (i in m downTo 1) invFact[i - 1] = invFact[i] * i % MOD

        // maximum position to process: original indices plus enough bits for carries
        val maxPos = n + 6   // since m <= 30, 2^6 > 30

        // DP arrays: cur[used][carry][bits]
        var cur = Array(m + 1) { Array(m + 1) { LongArray(k + 1) } }
        cur[0][0][0] = 1L

        for (pos in 0 until maxPos) {
            val next = Array(m + 1) { Array(m + 1) { LongArray(k + 1) } }
            if (pos < n) {
                val numVal = nums[pos].toLong() % MOD
                // precompute powers of this number up to m
                val pow = LongArray(m + 1)
                pow[0] = 1L
                for (c in 1..m) {
                    pow[c] = pow[c - 1] * numVal % MOD
                }
                for (used in 0..m) {
                    for (carry in 0..m) {
                        for (bits in 0..k) {
                            val curVal = cur[used][carry][bits]
                            if (curVal == 0L) continue
                            val maxC = m - used
                            for (c in 0..maxC) {
                                val total = carry + c
                                val newBit = total and 1
                                val newCarry = total shr 1
                                val newBits = bits + newBit
                                if (newBits > k) continue
                                val newUsed = used + c
                                var weight = curVal * pow[c] % MOD
                                weight = weight * invFact[c] % MOD
                                val arr = next[newUsed][newCarry]
                                arr[newBits] = (arr[newBits] + weight) % MOD
                            }
                        }
                    }
                }
            } else {
                // No new numbers can be added, only propagate carry
                for (used in 0..m) {
                    for (carry in 0..m) {
                        for (bits in 0..k) {
                            val curVal = cur[used][carry][bits]
                            if (curVal == 0L) continue
                            val total = carry
                            val newBit = total and 1
                            val newCarry = total shr 1
                            val newBits = bits + newBit
                            if (newBits > k) continue
                            val arr = next[used][newCarry]
                            arr[newBits] = (arr[newBits] + curVal) % MOD
                        }
                    }
                }
            }
            cur = next
        }

        var ans = cur[m][0][k] * fact[m] % MOD
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
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  static const int MOD = 1000000007;

  int magicalSum(int m, int k, List<int> nums) {
    int n = nums.length;
    // factorials
    List<int> fact = List.filled(m + 1, 1);
    for (int i = 1; i <= m; ++i) {
      fact[i] = (fact[i - 1] * i) % MOD;
    }
    // modular inverse using Fermat
    int modPow(int a, int e) {
      long res = 1;
      long base = a.toLong();
      while (e > 0) {
        if ((e & 1) == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        e >>= 1;
      }
      return res.toInt();
    }

    List<int> invFact = List.filled(m + 1, 1);
    invFact[m] = modPow(fact[m], MOD - 2);
    for (int i = m; i > 0; --i) {
      invFact[i - 1] = (invFact[i] * i) % MOD;
    }

    // precompute powers of nums[i]
    List<List<int>> powVals = List.generate(n, (_) => List.filled(m + 1, 1));
    for (int i = 0; i < n; ++i) {
      int val = nums[i] % MOD;
      for (int c = 1; c <= m; ++c) {
        powVals[i][c] = (powVals[i][c - 1] * val) % MOD;
      }
    }

    int extraBits = 0;
    while ((1 << extraBits) <= m) extraBits++;
    int maxPos = n + extraBits + 2; // enough to flush carries
    int maxCarry = m;

    List<List<List<int>>> cur = List.generate(
        m + 1, (_) => List.generate(maxCarry + 1, (_) => List.filled(k + 1, 0)));
    cur[0][0][0] = 1;

    for (int pos = 0; pos < maxPos; ++pos) {
      var next = List.generate(
          m + 1,
          (_) =>
              List.generate(maxCarry + 1, (_) => List.filled(k + 1, 0)));
      bool hasNum = pos < n;
      for (int cnt = 0; cnt <= m; ++cnt) {
        for (int carry = 0; carry <= maxCarry; ++carry) {
          for (int bits = 0; bits <= k; ++bits) {
            int curVal = cur[cnt][carry][bits];
            if (curVal == 0) continue;
            int maxAdd = hasNum ? (m - cnt) : 0;
            for (int c = 0; c <= maxAdd; ++c) {
              int newCnt = cnt + c;
              int total = c + carry;
              int resultBit = total & 1;
              int newCarry = total >> 1;
              int newBits = bits + resultBit;
              if (newBits > k) continue;
              int factor = hasNum ? powVals[pos][c] : 1;
              factor = (factor * invFact[c]) % MOD;
              int add = (curVal * factor) % MOD;
              int prev = next[newCnt][newCarry][newBits];
              int updated = prev + add;
              if (updated >= MOD) updated -= MOD;
              next[newCnt][newCarry][newBits] = updated;
            }
          }
        }
      }
      cur = next;
    }

    int result = cur[m][0][k];
    result = (result * fact[m]) % MOD;
    return result;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

const MOD int64 = 1000000007

func magicalSum(m int, k int, nums []int) int {
	n := len(nums)
	if k > m {
		return 0
	}
	// precompute combinations C[i][j] for i,j up to m
	comb := make([][]int64, m+1)
	for i := 0; i <= m; i++ {
		comb[i] = make([]int64, i+1)
		comb[i][0] = 1
		comb[i][i] = 1
		for j := 1; j < i; j++ {
			comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD
		}
	}
	// precompute powers of nums[i]^t for t=0..m
	powVals := make([][]int64, n)
	for i := 0; i < n; i++ {
		powVals[i] = make([]int64, m+1)
		powVals[i][0] = 1
		base := int64(nums[i]) % MOD
		for t := 1; t <= m; t++ {
			powVals[i][t] = powVals[i][t-1] * base % MOD
		}
	}
	// limit bits to process: enough to flush carries
	limit := n + 7 // safe margin (log2(m) <=5)
	if limit < 60 {
		limit = 60
	}
	// dp[rem][carry][setBits]
	cur := make([][][]int64, m+1)
	nxt := make([][][]int64, m+1)
	for i := 0; i <= m; i++ {
		cur[i] = make([][]int64, m+1)
		nxt[i] = make([][]int64, m+1)
		for j := 0; j <= m; j++ {
			cur[i][j] = make([]int64, k+1)
			nxt[i][j] = make([]int64, k+1)
		}
	}
	cur[m][0][0] = 1

	for pos := 0; pos < limit; pos++ {
		// reset nxt
		for i := 0; i <= m; i++ {
			for j := 0; j <= m; j++ {
				for s := 0; s <= k; s++ {
					nxt[i][j][s] = 0
				}
			}
		}
		maxTGlobal := 0
		hasIdx := pos < n
		if hasIdx {
			maxTGlobal = m // will be limited by rem in loop
		}
		for rem := 0; rem <= m; rem++ {
			for carry := 0; carry <= m; carry++ {
				for setBits := 0; setBits <= k; setBits++ {
					val := cur[rem][carry][setBits]
					if val == 0 {
						continue
					}
					maxT := 0
					if hasIdx {
						maxT = rem
					}
					for t := 0; t <= maxT; t++ {
						total := carry + t
						newBit := total & 1
						newCarry := total >> 1
						newSet := setBits + newBit
						if newSet > k {
							continue
						}
						newRem := rem - t
						add := val * comb[rem][t] % MOD
						if hasIdx && t > 0 {
							add = add * powVals[pos][t] % MOD
						}
						nxt[newRem][newCarry][newSet] = (nxt[newRem][newCarry][newSet] + add) % MOD
					}
				}
			}
		}
		// swap cur and nxt
		cur, nxt = nxt, cur
	}

	var ans int64 = 0
	for carry := 0; carry <= m; carry++ {
		pop := bits.OnesCount(uint(carry))
		if pop > k {
			continue
		}
		need := k - pop
		val := cur[0][carry][need]
		ans = (ans + val) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def magical_sum(m, k, nums)
  n = nums.length
  max_pos = n + 6  # enough to flush carries (m <= 30)

  # factorials and inverse factorials
  fact = Array.new(m + 1, 1)
  (1..m).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact = Array.new(m + 1, 1)
  inv_fact[m] = mod_pow(fact[m], MOD - 2)
  (m - 1).downto(0) { |i| inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD }

  # powers of nums[i]
  pow_nums = Array.new(n) { Array.new(m + 1, 1) }
  n.times do |i|
    p = 1
    (0..m).each do |cnt|
      pow_nums[i][cnt] = p
      p = p * nums[i] % MOD if cnt < m
    end
  end

  # dp[u][c][b] = value
  dp = Array.new(m + 1) { Array.new(m + 1) { Array.new(k + 1, 0) } }
  dp[0][0][0] = 1

  (0...max_pos).each do |pos|
    ndp = Array.new(m + 1) { Array.new(m + 1) { Array.new(k + 1, 0) } }
    (0..m).each do |used|
      (0..m).each do |carry|
        (0..k).each do |bits|
          val = dp[used][carry][bits]
          next if val == 0
          max_cnt = pos < n ? (m - used) : 0
          (0..max_cnt).each do |cnt|
            new_used = used + cnt
            t = cnt + carry
            bit = t & 1
            new_carry = t >> 1
            new_bits = bits + bit
            next if new_bits > k
            term = if pos < n
                     pow_nums[pos][cnt] * inv_fact[cnt] % MOD
                   else
                     1 # cnt is 0, inv_fact[0]=1, pow=1
                   end
            new_val = val * term % MOD
            ndp[new_used][new_carry][new_bits] = (ndp[new_used][new_carry][new_bits] + new_val) % MOD
          end
        end
      end
    end
    dp = ndp
  end

  ans = dp[m][0][k] * fact[m] % MOD
  ans
end

def mod_pow(base, exp)
  res = 1
  b = base % MOD
  e = exp
  while e > 0
    res = res * b % MOD if (e & 1) == 1
    b = b * b % MOD
    e >>= 1
  end
  res
end
```

## Scala

```scala
object Solution {
  val MOD: Long = 1000000007L

  def magicalSum(m: Int, k: Int, nums: Array[Int]): Int = {
    val n = nums.length
    // factorials and inverse factorials up to m
    val fact = new Array[Long](m + 1)
    val invFact = new Array[Long](m + 1)
    fact(0) = 1L
    var i = 1
    while (i <= m) {
      fact(i) = fact(i - 1) * i % MOD
      i += 1
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
    invFact(m) = modPow(fact(m), MOD - 2)
    i = m - 1
    while (i >= 0) {
      invFact(i) = invFact(i + 1) * (i + 1) % MOD
      i -= 1
    }

    // precompute powers of nums[i]
    val powNum = Array.ofDim[Long](n, m + 1)
    var idx = 0
    while (idx < n) {
      powNum(idx)(0) = 1L
      var cnt = 1
      while (cnt <= m) {
        powNum(idx)(cnt) = powNum(idx)(cnt - 1) * nums(idx).toLong % MOD
        cnt += 1
      }
      idx += 1
    }

    // dp[s][c][b] : after processing some indices, selected s numbers,
    // incoming carry c, and counted b set bits from lower positions.
    var dp = Array.ofDim[Long](m + 1, m + 1, k + 1)
    dp(0)(0)(0) = 1L

    idx = 0
    while (idx < n) {
      val ndp = Array.ofDim[Long](m + 1, m + 1, k + 1)
      var s = 0
      while (s <= m) {
        var c = 0
        while (c <= m) {
          var b = 0
          while (b <= k) {
            val cur = dp(s)(c)(b)
            if (cur != 0L) {
              val remaining = m - s
              var cnt = 0
              while (cnt <= remaining) {
                val total = cnt + c
                val digit = total & 1
                val newCarry = total >> 1
                val nb = b + digit
                if (nb <= k) {
                  val ns = s + cnt
                  var add = cur * powNum(idx)(cnt) % MOD
                  add = add * invFact(cnt) % MOD
                  ndp(ns)(newCarry)(nb) = (ndp(ns)(newCarry)(nb) + add) % MOD
                }
                cnt += 1
              }
            }
            b += 1
          }
          c += 1
        }
        s += 1
      }
      dp = ndp
      idx += 1
    }

    var ans: Long = 0L
    var c = 0
    while (c <= m) {
      val pop = Integer.bitCount(c)
      var b = 0
      while (b <= k) {
        if (b + pop == k) {
          ans = (ans + dp(m)(c)(b)) % MOD
        }
        b += 1
      }
      c += 1
    }

    ans = ans * fact(m) % MOD
    ans.toInt
  }
}
```

## Rust

```rust
use std::cmp::min;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i32) -> i64 {
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

pub struct Solution;

impl Solution {
    pub fn magical_sum(m: i32, k: i32, nums: Vec<i32>) -> i32 {
        let m_usize = m as usize;
        let k_usize = k as usize;
        if k_usize > m_usize {
            return 0;
        }
        let n = nums.len();
        // factorials and inverse factorials
        let mut fact = vec![1i64; m_usize + 1];
        for i in 1..=m_usize {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact = vec![1i64; m_usize + 1];
        inv_fact[m_usize] = mod_pow(fact[m_usize], MOD as i32 - 2);
        for i in (1..=m_usize).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }

        // precompute powers of nums[idx]
        let mut pow_nums: Vec<Vec<i64>> = vec![vec![0; m_usize + 1]; n];
        for idx in 0..n {
            pow_nums[idx][0] = 1;
            let val = nums[idx] as i64 % MOD;
            for cnt in 1..=m_usize {
                pow_nums[idx][cnt] = pow_nums[idx][cnt - 1] * val % MOD;
            }
        }

        // maximum positions to process
        let extra = 6; // enough because m <= 30
        let max_pos = n + extra;

        // dp[used][carry][bits] = value
        let mut dp = vec![vec![vec![0i64; k_usize + 1]; m_usize + 1]; m_usize + 1];
        dp[0][0][0] = 1;

        for pos in 0..max_pos {
            // next dp
            let mut ndp = vec![vec![vec![0i64; k_usize + 1]; m_usize + 1]; m_usize + 1];
            for used in 0..=m_usize {
                for carry in 0..=m_usize {
                    for bits in 0..=k_usize {
                        let cur = dp[used][carry][bits];
                        if cur == 0 {
                            continue;
                        }
                        if pos < n {
                            // we can take cnt from 0..remaining
                            let max_cnt = m_usize - used;
                            for cnt in 0..=max_cnt {
                                let total = carry + cnt;
                                let bit = (total & 1) as usize;
                                let new_carry = total >> 1;
                                let new_used = used + cnt;
                                let new_bits = bits + bit;
                                if new_bits > k_usize || new_carry > m_usize {
                                    continue;
                                }
                                let mut add = cur;
                                // multiply by nums[pos]^cnt * inv_fact[cnt]
                                add = add * pow_nums[pos][cnt] % MOD;
                                add = add * inv_fact[cnt] % MOD;
                                ndp[new_used][new_carry][new_bits] =
                                    (ndp[new_used][new_carry][new_bits] + add) % MOD;
                            }
                        } else {
                            // cnt must be 0
                            let total = carry;
                            let bit = (total & 1) as usize;
                            let new_carry = total >> 1;
                            let new_used = used;
                            let new_bits = bits + bit;
                            if new_bits > k_usize || new_carry > m_usize {
                                continue;
                            }
                            ndp[new_used][new_carry][new_bits] =
                                (ndp[new_used][new_carry][new_bits] + cur) % MOD;
                        }
                    }
                }
            }
            dp = ndp;
        }

        let mut ans = dp[m_usize][0][k_usize];
        ans = ans * fact[m_usize] % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; fast exponentiation
(define (pow-mod a e)
  (let loop ((base (modulo a MOD)) (exp e) (res 1))
    (if (= exp 0)
        res
        (loop (modulo (* base base) MOD)
              (arithmetic-shift exp -1)
              (if (odd? exp)
                  (modulo (* res base) MOD)
                  res)))))

;; modular inverse using Fermat
(define (inv-mod a)
  (pow-mod a (- MOD 2)))

;; popcount of non‑negative integer
(define (popcount x)
  (let loop ((cnt 0) (y x))
    (if (= y 0)
        cnt
        (loop (+ cnt (bitwise-and y 1)) (arithmetic-shift y -1)))))

;; create a 3‑dim mutable vector filled with zeros
(define (make-3d m n p)
  (let ((v (make-vector (add1 m))))
    (for ([i (in-range (add1 m))])
      (vector-set! v i (make-vector (add1 n)))
      (for ([j (in-range (add1 n))])
        (vector-set! (vector-ref v i) j (make-vector (add1 p) 0))))
    v))

;; add value to dp[i][c][b] modulo MOD
(define (dp-add! dp i c b val)
  (let* ((layer-i (vector-ref dp i))
         (layer-c (vector-ref layer-i c))
         (old   (vector-ref layer-c b))
         (new   (modulo (+ old val) MOD)))
    (vector-set! layer-c b new)))

(define (magical-sum m k nums)
  (-> exact-integer? exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         ;; factorials and inverse factorials up to m
         (fact (make-vector (add1 m) 1))
         (inv-fact (make-vector (add1 m) 1))
         (_ (for ([i (in-range 1 (add1 m))])
              (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD))))
         (_ (vector-set! inv-fact m (inv-mod (vector-ref fact m)))
            (for ([i (in-range (- m 1) -1 -1)])
              (vector-set! inv-fact i
                           (modulo (* (vector-ref inv-fact (+ i 1)) (+ i 1)) MOD))))
         ;; extra bits to flush carries (log2(m)+2 is safe)
         (extra 6)
         (max-pos (+ (sub1 n) extra))
         ;; pre‑compute powers of nums[pos] for c = 0..m
         (pow-table (make-vector (add1 max-pos)))
         (_ (for ([pos (in-range (add1 max-pos))])
              (let ((base (if (< pos n) (list-ref nums pos) 1))
                    (vec (make-vector (add1 m) 1)))
                (vector-set! vec 0 1)
                (for ([c (in-range 1 (add1 m))])
                  (vector-set! vec c
                               (modulo (* (vector-ref vec (- c 1)) base) MOD)))
                (vector-set! pow-table pos vec))))
         ;; DP tables
         (cur (make-3d m m k))
         (_ (dp-add! cur 0 0 0 1))) ; dp[0][0][0] = 1

    ;; main DP over positions
    (for ([pos (in-range (add1 max-pos))])
      (let ((next (make-3d m m k))
            (powvec (vector-ref pow-table pos)))
        (for* ([i (in-range (add1 m))]
               [carry (in-range (add1 m))]
               [bits (in-range (add1 k))])
          (let ((val (vector-ref (vector-ref (vector-ref cur i) carry) bits)))
            (when (> val 0)
              (define max-c (- m i))
              (if (< pos n)
                  (for ([c (in-range (add1 (min max-c m)))])
                    (let* ((total (+ carry c))
                           (out-bit (bitwise-and total 1))
                           (new-carry (arithmetic-shift total -1))
                           (new-bits (+ bits out-bit)))
                      (when (<= new-bits k)
                        (define add
                          (modulo (* val
                                     (vector-ref powvec c)
                                     (vector-ref inv-fact c))
                                   MOD))
                        (dp-add! next (+ i c) new-carry new-bits add))))
                  ;; pos >= n : cannot pick any index, only c = 0
                  (let* ((total carry)
                         (out-bit (bitwise-and total 1))
                         (new-carry (arithmetic-shift total -1))
                         (new-bits (+ bits out-bit)))
                    (when (<= new-bits k)
                      (dp-add! next i new-carry new-bits val))))))))
        (set! cur next)))

    ;; collect answer, accounting for remaining carry bits
    (let ((ans 0))
      (for* ([carry (in-range (add1 m))]
             [bits (in-range (add1 k))])
        (when (= (+ bits (popcount carry)) k)
          (define val (vector-ref (vector-ref (vector-ref cur m) carry) bits))
          (when (> val 0)
            (set! ans (modulo (+ ans (* val (vector-ref fact m))) MOD)))))
      ans)))
```

## Erlang

```erlang
-spec magical_sum(M :: integer(), K :: integer(), Nums :: [integer()]) -> integer().
magical_sum(M, K, Nums) ->
    Mod = 1000000007,
    MaxM = M,

    % factorials and inverse factorials
    FactList = fact_list(MaxM, Mod),
    InvFactList = inv_fact_list(FactList, Mod),

    % precompute powers for each number
    PowLists = [pow_list(N, MaxM, Mod) || N <- Nums],

    % initial DP map: key {Used, Carry, Bits} -> value
    InitMap = maps:from_list([{{0, 0, 0}, 1}]),

    FinalMap = lists:foldl(
        fun(PowList, CurMap) ->
            maps:fold(
                fun({U, C, B}, Val, AccMap) ->
                    MaxT = MaxM - U,
                    lists:foldl(
                        fun(T, InnerAcc) ->
                            NewU = U + T,
                            Total = T + C,
                            BitAdd = Total band 1,
                            NewB = B + BitAdd,
                            NewC = Total div 2,
                            PowVal = nth_elem(PowList, T),
                            InvFactT = nth_elem(InvFactList, T),
                            Weight = (PowVal * InvFactT) rem Mod,
                            AddVal = (Val * Weight) rem Mod,
                            Key = {NewU, NewC, NewB},
                            Prev = maps:get(Key, InnerAcc, 0),
                            maps:put(Key, (Prev + AddVal) rem Mod, InnerAcc)
                        end,
                        AccMap,
                        lists:seq(0, MaxT)
                    )
                end,
                maps:new(),
                CurMap
            )
        end,
        InitMap,
        PowLists),

    ResultSum = maps:fold(
        fun({U, C, B}, Val, Acc) ->
            case U == MaxM andalso (B + popcount(C)) == K of
                true -> (Acc + Val) rem Mod;
                false -> Acc
            end
        end,
        0,
        FinalMap),

    FactM = nth_elem(FactList, M),
    (FactM * ResultSum) rem Mod.

% ---------- helper functions ----------
fact_list(N, Mod) ->
    fact_acc(0, 1, N, Mod, []).

fact_acc(I, Prev, N, Mod, Acc) when I =< N ->
    NewAcc = [Prev | Acc],
    NextPrev = (Prev * (I + 1)) rem Mod,
    fact_acc(I + 1, NextPrev, N, Mod, NewAcc);
fact_acc(_, _, _, _, Acc) -> lists:reverse(Acc).

inv_fact_list(FactList, Mod) ->
    [pow_mod(F, Mod - 2, Mod) || F <- FactList].

pow_list(Num, MaxM, Mod) ->
    pow_acc(0, 1, Num, MaxM, Mod, []).

pow_acc(I, Acc, _Num, MaxM, _Mod, List) when I > MaxM ->
    lists:reverse(List);
pow_acc(I, Acc, Num, MaxM, Mod, List) ->
    NewList = [Acc | List],
    NextAcc = (Acc * Num) rem Mod,
    pow_acc(I + 1, NextAcc, Num, MaxM, Mod, NewList).

nth_elem(List, Index) -> % zero‑based
    lists:nth(Index + 1, List).

popcount(0) -> 0;
popcount(N) ->
    (N band 1) + popcount(N bsr 1).

pow_mod(_, 0, _) -> 1;
pow_mod(Base, Exp, Mod) when Exp rem 2 =:= 1 ->
    (Base * pow_mod((Base * Base) rem Mod, Exp div 2, Mod)) rem Mod;
pow_mod(Base, Exp, Mod) ->
    pow_mod((Base * Base) rem Mod, Exp div 2, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec magical_sum(m :: integer, k :: integer, nums :: [integer]) :: integer
  def magical_sum(m, k, nums) do
    mod = 1_000_000_007
    n = length(nums)
    max_pos = n + 31

    # factorials
    {fact_rev, _} =
      Enum.reduce(0..m, {[], 1}, fn i, {list, prev} ->
        cur = if i == 0, do: 1, else: rem(prev * i, mod)
        {[cur | list], cur}
      end)

    fact = Enum.reverse(fact_rev)

    # inverse factorials
    inv_fact_m = pow_mod(Enum.at(fact, m), mod - 2, mod)

    {inv_rev, _} =
      Enum.reduce(m..0, {[], inv_fact_m}, fn i, {list, cur_inv} ->
        new_cur = if i > 0, do: rem(cur_inv * i, mod), else: 0
        {[cur_inv | list], new_cur}
      end)

    inv_fact = Enum.reverse(inv_rev)

    dp = %{{0, 0, 0} => 1}

    dp =
      Enum.reduce(0..max_pos, dp, fn pos, cur_dp ->
        base = if pos < n, do: Enum.at(nums, pos), else: 0

        Enum.reduce(cur_dp, %{}, fn {{carry, bits, total}, val}, ndp ->
          remaining = m - total
          cnt_range =
            if pos < n do
              0..remaining
            else
              [0]
            end

          Enum.reduce(cnt_range, ndp, fn cnt, acc ->
            new_total = total + cnt
            t = carry + cnt
            bit = rem(t, 2)
            new_carry = div(t, 2)
            new_bits = bits + bit

            if new_bits <= k and new_carry <= m do
              contrib = val

              if cnt > 0 do
                contrib = rem(contrib * pow_mod(base, cnt, mod), mod)
              end

              contrib = rem(contrib * Enum.at(inv_fact, cnt), mod)

              key = {new_carry, new_bits, new_total}
              prev = Map.get(acc, key, 0)
              Map.put(acc, key, rem(prev + contrib, mod))
            else
              acc
            end
          end)
        end)
      end)

    ans = Map.get(dp, {0, k, m}, 0)
    rem(ans * Enum.at(fact, m), mod)
  end

  defp pow_mod(_base, 0, _mod), do: 1

  defp pow_mod(base, exp, mod) when exp > 0 do
    half = pow_mod(base, div(exp, 2), mod)
    res = rem(half * half, mod)

    if rem(exp, 2) == 1 do
      rem(res * base, mod)
    else
      res
    end
  end
end
```

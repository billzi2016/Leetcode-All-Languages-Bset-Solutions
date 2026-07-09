# 1994. The Number of Good Subsets

## Cpp

```cpp
class Solution {
public:
    int numberOfGoodSubsets(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        vector<int> cnt(31, 0);
        for (int x : nums) cnt[x]++;
        int ones = cnt[1];
        
        // primes up to 30
        vector<int> primes = {2,3,5,7,11,13,17,19,23,29};
        const int P = primes.size();
        const int FULL = 1 << P;
        
        // mask for each number (2..30), -1 if invalid (has squared prime factor)
        vector<int> masks(31, -1);
        for (int v = 2; v <= 30; ++v) {
            if (cnt[v] == 0) continue;
            int x = v;
            int mask = 0;
            bool ok = true;
            for (int i = 0; i < P; ++i) {
                int p = primes[i];
                if (x % p == 0) {
                    x /= p;
                    if (x % p == 0) { // squared factor
                        ok = false;
                        break;
                    }
                    mask |= (1 << i);
                }
            }
            if (ok && x == 1) masks[v] = mask; // valid square‑free number
        }
        
        vector<long long> dp(FULL, 0);
        dp[0] = 1;
        for (int v = 2; v <= 30; ++v) {
            int c = cnt[v];
            if (c == 0) continue;
            int m = masks[v];
            if (m == -1) continue; // invalid number
            for (int mask = FULL - 1; mask >= 0; --mask) {
                if ((mask & m) == 0) {
                    dp[mask | m] = (dp[mask | m] + dp[mask] * c) % MOD;
                }
            }
        }
        
        long long ans = 0;
        for (int mask = 1; mask < FULL; ++mask) {
            ans = (ans + dp[mask]) % MOD;
        }
        // incorporate ones
        long long pow2 = 1;
        long long base = 2;
        int exp = ones;
        while (exp > 0) {
            if (exp & 1) pow2 = pow2 * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        ans = ans * pow2 % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int numberOfGoodSubsets(int[] nums) {
        int[] freq = new int[31];
        for (int v : nums) freq[v]++;
        int[] primes = {2,3,5,7,11,13,17,19,23,29};
        int[] numMask = new int[31];
        for (int i = 2; i <= 30; i++) {
            int x = i;
            int mask = 0;
            boolean ok = true;
            for (int j = 0; j < primes.length; j++) {
                int p = primes[j];
                if (x % p == 0) {
                    int cnt = 0;
                    while (x % p == 0) {
                        x /= p;
                        cnt++;
                    }
                    if (cnt > 1) { // not square‑free
                        ok = false;
                        break;
                    }
                    mask |= 1 << j;
                }
            }
            if (ok && x == 1) numMask[i] = mask; // valid
            else numMask[i] = -1; // invalid
        }

        long[] dp = new long[1 << primes.length];
        dp[0] = 1;
        for (int i = 2; i <= 30; i++) {
            int cnt = freq[i];
            if (cnt == 0) continue;
            int m = numMask[i];
            if (m == -1) continue; // cannot be used
            for (int mask = dp.length - 1; mask >= 0; mask--) {
                if ((mask & m) == 0) {
                    dp[mask | m] = (dp[mask | m] + dp[mask] * cnt) % MOD;
                }
            }
        }

        long sum = 0;
        for (int mask = 1; mask < dp.length; mask++) {
            sum = (sum + dp[mask]) % MOD;
        }

        int ones = freq[1];
        long pow2 = modPow(2, ones);
        long ans = sum * pow2 % MOD;
        return (int) ans;
    }

    private long modPow(long base, long exp) {
        long res = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) res = res * base % MOD;
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
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        primes = [2,3,5,7,11,13,17,19,23,29]
        prime_to_bit = {p:i for i,p in enumerate(primes)}
        
        # count frequencies
        freq = [0]*31
        for x in nums:
            freq[x] += 1
        
        cnt_one = freq[1]
        
        # precompute mask for numbers 2..30, -1 if invalid (has squared prime factor)
        masks = [-1]*31
        for num in range(2,31):
            n = num
            mask = 0
            valid = True
            for p in primes:
                if p*p > n:
                    break
                cnt = 0
                while n % p == 0:
                    n //= p
                    cnt += 1
                if cnt > 1:
                    valid = False
                    break
                if cnt == 1:
                    mask |= (1 << prime_to_bit[p])
            if not valid:
                masks[num] = -1
                continue
            # remaining factor could be a prime > sqrt(num)
            if n > 1:
                # n is prime and <=30
                if n in prime_to_bit:
                    mask |= (1 << prime_to_bit[n])
                else:
                    # should not happen for given constraints
                    valid = False
            masks[num] = mask if valid else -1
        
        dp = [0]* (1<<10)
        dp[0] = 1
        
        for num in range(2,31):
            c = freq[num]
            if c == 0:
                continue
            m = masks[num]
            if m == -1:
                continue
            # iterate masks descending to avoid reuse within same number
            for mask in range((1<<10)-1, -1, -1):
                if dp[mask] and (mask & m) == 0:
                    new_mask = mask | m
                    dp[new_mask] = (dp[new_mask] + dp[mask]*c) % MOD
        
        total = sum(dp[1:]) % MOD   # exclude empty subset
        if cnt_one:
            total = total * pow(2, cnt_one, MOD) % MOD
        return total
```

## Python3

```python
import sys
from typing import List
from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        prime_list = [2,3,5,7,11,13,17,19,23,29]
        prime_to_bit = {p:i for i,p in enumerate(prime_list)}
        
        # precompute mask for numbers 2..30, -1 if invalid (has squared prime factor)
        num_mask = {}
        for x in range(2,31):
            orig = x
            mask = 0
            valid = True
            for p in prime_list:
                if p*p > x:
                    break
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                if cnt > 1:
                    valid = False
                    break
                if cnt == 1:
                    mask |= 1 << prime_to_bit[p]
            if not valid:
                continue
            # after loop, x may be a remaining prime > sqrt(orig)
            if x > 1:
                # x is prime
                if x in prime_to_bit:
                    mask |= 1 << prime_to_bit[x]
                else:
                    # prime >30 not possible given constraints
                    valid = False
            if valid and mask != 0:
                num_mask[orig] = mask
        
        freq = Counter(nums)
        cnt_one = freq.get(1,0)
        
        dp = [0]* (1<<10)
        dp[0] = 1
        
        for val, m in num_mask.items():
            c = freq.get(val,0)
            if c == 0:
                continue
            # update dp in reverse to avoid reuse within same iteration
            for mask in range((1<<10)-1, -1, -1):
                if dp[mask] == 0 or (mask & m):
                    continue
                new_mask = mask | m
                dp[new_mask] = (dp[new_mask] + dp[mask]*c) % MOD
        
        ans = sum(dp[mask] for mask in range(1, 1<<10)) % MOD
        if cnt_one:
            ans = ans * pow(2, cnt_one, MOD) % MOD
        return ans
```

## C

```c
#include <stddef.h>

#define MOD 1000000007

static long long modpow(long long a, long long e) {
    long long res = 1;
    while (e) {
        if (e & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return res;
}

int numberOfGoodSubsets(int* nums, int numsSize) {
    const int primes[10] = {2,3,5,7,11,13,17,19,23,29};
    int primeBit[31];
    for (int i = 0; i <= 30; ++i) primeBit[i] = -1;
    for (int i = 0; i < 10; ++i) primeBit[primes[i]] = i;

    int cnt[31] = {0};
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] >= 1 && nums[i] <= 30)
            cnt[nums[i]]++;
    }

    int masks[31];
    for (int i = 0; i <= 30; ++i) masks[i] = -1;
    for (int val = 2; val <= 30; ++val) {
        if (cnt[val] == 0) continue;
        int v = val, mask = 0;
        int ok = 1;
        for (int i = 0; i < 10; ++i) {
            int p = primes[i];
            if (v % p == 0) {
                v /= p;
                if (v % p == 0) { // repeated prime factor
                    ok = 0;
                    break;
                }
                mask |= (1 << i);
            }
        }
        if (ok && v == 1) masks[val] = mask; // valid square‑free number
    }

    const int MAXMASK = 1 << 10;
    long long dp[MAXMASK];
    for (int i = 0; i < MAXMASK; ++i) dp[i] = 0;
    dp[0] = 1;

    for (int val = 2; val <= 30; ++val) {
        if (cnt[val] == 0) continue;
        int mask = masks[val];
        if (mask == -1) continue; // invalid number
        long long ways = cnt[val];
        for (int m = MAXMASK - 1; m >= 0; --m) {
            if ((m & mask) == 0 && dp[m]) {
                int nm = m | mask;
                dp[nm] = (dp[nm] + dp[m] * ways) % MOD;
            }
        }
    }

    long long ans = 0;
    for (int m = 1; m < MAXMASK; ++m) {
        ans = (ans + dp[m]) % MOD;
    }

    int ones = cnt[1];
    if (ones > 0) {
        ans = (ans * modpow(2, ones)) % MOD;
    }
    return (int)ans;
}
```

## Csharp

```csharp
using System;
public class Solution {
    private const int MOD = 1_000_000_007;
    public int NumberOfGoodSubsets(int[] nums) {
        int[] cnt = new int[31];
        foreach (int x in nums) cnt[x]++;
        // primes up to 30
        int[] primes = {2,3,5,7,11,13,17,19,23,29};
        int primeCount = primes.Length;
        int[] numMask = new int[31];
        for (int i = 2; i <= 30; i++) {
            int x = i;
            int mask = 0;
            bool valid = true;
            foreach (int p in primes) {
                if (p * p > x) break;
                int exp = 0;
                while (x % p == 0) {
                    x /= p;
                    exp++;
                }
                if (exp > 1) { valid = false; break; }
                if (exp == 1) mask |= 1 << Array.IndexOf(primes, p);
            }
            if (!valid) { numMask[i] = -1; continue; }
            // x may be a prime greater than sqrt(original)
            if (x > 1) {
                int idx = Array.IndexOf(primes, x);
                if (idx == -1) { // should not happen for numbers <=30
                    valid = false;
                } else {
                    mask |= 1 << idx;
                }
            }
            numMask[i] = valid ? mask : -1;
        }

        int fullMask = 1 << primeCount;
        long[] dp = new long[fullMask];
        dp[0] = 1;

        for (int i = 2; i <= 30; i++) {
            if (cnt[i] == 0) continue;
            int mask = numMask[i];
            if (mask == -1) continue; // contains squared prime factor
            long ways = cnt[i]; // choose one occurrence among identical numbers
            for (int m = fullMask - 1; m >= 0; m--) {
                if ((m & mask) != 0) continue;
                dp[m | mask] = (dp[m | mask] + dp[m] * ways) % MOD;
            }
        }

        long total = 0;
        for (int m = 1; m < fullMask; m++) {
            total = (total + dp[m]) % MOD;
        }

        // account for ones
        if (cnt[1] > 0) {
            long pow2 = ModPow(2, cnt[1], MOD);
            total = total * pow2 % MOD;
        }
        return (int)total;
    }

    private long ModPow(long baseVal, int exp, int mod) {
        long result = 1;
        long b = baseVal % mod;
        while (exp > 0) {
            if ((exp & 1) == 1) result = result * b % mod;
            b = b * b % mod;
            exp >>= 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodSubsets = function(nums) {
    const MOD = 1_000_000_007;
    const primes = [2,3,5,7,11,13,17,19,23,29];
    const primeCount = primes.length; //10
    const maxMask = 1 << primeCount; //1024

    // frequency of each number (1..30)
    const freq = new Array(31).fill(0);
    for (const v of nums) freq[v]++;

    // precompute mask for numbers 2..30, -1 if invalid (has squared prime factor)
    const masks = new Array(31).fill(-1);
    for (let num = 2; num <= 30; ++num) {
        let x = num;
        let mask = 0;
        let valid = true;
        for (let i = 0; i < primeCount; ++i) {
            const p = primes[i];
            if (x % p === 0) {
                let cnt = 0;
                while (x % p === 0) {
                    x /= p;
                    cnt++;
                }
                if (cnt > 1) { // squared factor
                    valid = false;
                    break;
                }
                mask |= (1 << i);
            }
        }
        if (valid && x === 1) masks[num] = mask; // else stays -1
    }

    const dp = new Array(maxMask).fill(0);
    dp[0] = 1;

    for (let num = 2; num <= 30; ++num) {
        const cnt = freq[num];
        if (cnt === 0) continue;
        const m = masks[num];
        if (m === -1) continue; // cannot be used
        // iterate masks in descending order to avoid using the same number multiple times
        for (let s = maxMask - 1; s >= 0; --s) {
            if ((s & m) === 0) {
                const ns = s | m;
                dp[ns] = (dp[ns] + dp[s] * cnt) % MOD;
            }
        }
    }

    // sum all non-empty masks
    let ans = 0;
    for (let i = 1; i < maxMask; ++i) {
        ans = (ans + dp[i]) % MOD;
    }

    // account for ones: each good subset can be combined with any subset of the ones
    const cntOnes = freq[1];
    if (cntOnes > 0 && ans > 0) {
        let pow2 = 1;
        let base = 2;
        let exp = cntOnes;
        while (exp > 0) {
            if (exp & 1) pow2 = (pow2 * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        ans = (ans * pow2) % MOD;
    }

    return ans;
};
```

## Typescript

```typescript
function numberOfGoodSubsets(nums: number[]): number {
    const MOD = 1_000_000_007;
    const primeList = [2,3,5,7,11,13,17,19,23,29];
    const primeIndex = new Map<number, number>();
    for (let i = 0; i < primeList.length; ++i) primeIndex.set(primeList[i], i);
    
    // frequency of each number (1..30)
    const freq = new Array(31).fill(0);
    for (const v of nums) freq[v]++;
    
    // mask for each valid square‑free number, -1 if invalid
    const masks = new Array(31).fill(-1);
    for (let num = 2; num <= 30; ++num) {
        let x = num;
        let mask = 0;
        let ok = true;
        for (const p of primeList) {
            if (p * p > x) break;
            if (x % p === 0) {
                let cnt = 0;
                while (x % p === 0) {
                    x /= p;
                    cnt++;
                }
                if (cnt > 1) { ok = false; break; } // repeated prime factor
                mask |= 1 << (primeIndex.get(p)!);
            }
        }
        if (!ok) continue;
        if (x > 1) { // remaining prime factor
            if (!primeIndex.has(x)) { ok = false; }
            else {
                const idx = primeIndex.get(x)!;
                mask |= 1 << idx;
            }
        }
        if (ok) masks[num] = mask;
    }
    
    const dpSize = 1 << primeList.length; // 1024
    const dp = new Array(dpSize).fill(0);
    dp[0] = 1;
    
    for (let num = 2; num <= 30; ++num) {
        const cnt = freq[num];
        if (cnt === 0) continue;
        const mask = masks[num];
        if (mask === -1) continue; // invalid number
        for (let m = dpSize - 1; m >= 0; --m) {
            if ((m & mask) !== 0) continue;
            const cur = dp[m];
            if (cur === 0) continue;
            const nm = m | mask;
            dp[nm] = (dp[nm] + cur * cnt) % MOD;
        }
    }
    
    let ans = 0;
    for (let m = 1; m < dpSize; ++m) {
        ans = (ans + dp[m]) % MOD;
    }
    
    // incorporate ones
    const ones = freq[1];
    if (ones > 0) {
        let pow2 = 1;
        let base = 2;
        let exp = ones;
        while (exp > 0) {
            if (exp & 1) pow2 = (pow2 * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        ans = (ans * pow2) % MOD;
    }
    
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfGoodSubsets($nums) {
        $MOD = 1000000007;
        // Count frequencies
        $freq = array_fill(0, 31, 0);
        foreach ($nums as $v) {
            $freq[$v]++;
        }

        // Primes up to 30
        $primes = [2,3,5,7,11,13,17,19,23,29];
        $primeIndex = [];
        foreach ($primes as $i => $p) {
            $primeIndex[$p] = $i;
        }

        // Precompute mask for each number (2..30)
        $numMask = array_fill(0, 31, -1);
        for ($i = 2; $i <= 30; $i++) {
            $x = $i;
            $mask = 0;
            $valid = true;
            foreach ($primes as $p) {
                if ($x % $p == 0) {
                    $cnt = 0;
                    while ($x % $p == 0) {
                        $x /= $p;
                        $cnt++;
                    }
                    if ($cnt > 1) { // square factor
                        $valid = false;
                        break;
                    }
                    $mask |= (1 << $primeIndex[$p]);
                }
            }
            if ($x != 1) $valid = false; // leftover prime >30 not possible but keep safety
            if ($valid) {
                $numMask[$i] = $mask;
            }
        }

        $dpSize = 1 << count($primes); // 1024
        $dp = array_fill(0, $dpSize, 0);
        $dp[0] = 1;

        for ($val = 2; $val <= 30; $val++) {
            $cnt = $freq[$val];
            if ($cnt == 0) continue;
            $mask = $numMask[$val];
            if ($mask == -1) continue; // cannot be used
            // iterate masks descending to avoid reuse within same number
            for ($m = $dpSize - 1; $m >= 0; $m--) {
                if (($m & $mask) == 0) {
                    $newMask = $m | $mask;
                    $add = ($dp[$m] * $cnt) % $MOD;
                    $dp[$newMask] = ($dp[$newMask] + $add) % $MOD;
                }
            }
        }

        // Sum all non-empty masks
        $ans = 0;
        for ($mask = 1; $mask < $dpSize; $mask++) {
            $ans = ($ans + $dp[$mask]) % $MOD;
        }

        // Account for ones (they can be added arbitrarily)
        $ones = $freq[1];
        if ($ones > 0 && $ans > 0) {
            $pow2 = $this->modPow(2, $ones, $MOD);
            $ans = ($ans * $pow2) % $MOD;
        }

        return $ans;
    }

    private function modPow($base, $exp, $mod) {
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
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    private let primes = [2,3,5,7,11,13,17,19,23,29]
    
    func numberOfGoodSubsets(_ nums: [Int]) -> Int {
        var freq = [Int](repeating: 0, count: 31)
        for v in nums { freq[v] += 1 }
        
        let cntOne = freq[1]
        
        // precompute masks for numbers 2..30
        var masks = [Int](repeating: -1, count: 31)
        for num in 2...30 {
            var x = num
            var mask = 0
            var valid = true
            for (i, p) in primes.enumerated() {
                if x % p == 0 {
                    var cnt = 0
                    while x % p == 0 {
                        x /= p
                        cnt += 1
                    }
                    if cnt > 1 { // square factor
                        valid = false
                        break
                    }
                    mask |= (1 << i)
                }
            }
            if valid && x == 1 {
                masks[num] = mask
            }
        }
        
        var dp = [Int](repeating: 0, count: 1 << primes.count)
        dp[0] = 1
        
        for val in 2...30 {
            let f = freq[val]
            if f == 0 { continue }
            let m = masks[val]
            if m == -1 { continue } // invalid number
            // iterate states backwards to avoid reuse within same iteration
            for s in stride(from: dp.count - 1, through: 0, by: -1) {
                let cur = dp[s]
                if cur == 0 { continue }
                if (s & m) == 0 {
                    let ns = s | m
                    let add = Int((Int64(cur) * Int64(f)) % Int64(MOD))
                    dp[ns] += add
                    if dp[ns] >= MOD { dp[ns] -= MOD }
                }
            }
        }
        
        var sum = 0
        for i in 1..<dp.count {
            sum += dp[i]
            if sum >= MOD { sum -= MOD }
        }
        
        let pow2cntOne = modPow(2, cntOne)
        let result = Int((Int64(sum) * Int64(pow2cntOne)) % Int64(MOD))
        return result
    }
    
    private func modPow(_ base: Int, _ exp: Int) -> Int {
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
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfGoodSubsets(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        val primes = intArrayOf(2,3,5,7,11,13,17,19,23,29)
        val primeToBit = HashMap<Int,Int>()
        for (i in primes.indices) primeToBit[primes[i]] = i

        // count frequencies
        val cnt = IntArray(31)
        var ones = 0
        for (v in nums) {
            if (v == 1) ones++ else cnt[v]++
        }

        // precompute mask for each number, -1 means invalid (has squared prime factor)
        fun getMask(num: Int): Int {
            var x = num
            var mask = 0
            for (p in primes) {
                if (p * p > x) break
                var c = 0
                while (x % p == 0) {
                    x /= p
                    c++
                }
                if (c > 1) return -1          // squared prime factor
                if (c == 1) mask = mask or (1 shl (primeToBit[p]!!))
            }
            if (x > 1) { // remaining prime factor
                mask = mask or (1 shl (primeToBit[x]!!))
            }
            return mask
        }

        val masks = IntArray(31) { -1 }
        for (num in 2..30) {
            masks[num] = getMask(num)
        }

        val dp = LongArray(1 shl 10)
        dp[0] = 1L

        // DP over numbers
        for (num in 2..30) {
            val freq = cnt[num]
            if (freq == 0) continue
            val m = masks[num]
            if (m == -1) continue   // invalid number
            for (mask in dp.indices.reversed()) {
                val cur = dp[mask]
                if (cur == 0L) continue
                if ((mask and m) == 0) {
                    val newMask = mask or m
                    dp[newMask] = (dp[newMask] + cur * freq) % MOD
                }
            }
        }

        var ans = 0L
        for (mask in 1 until dp.size) {
            ans = (ans + dp[mask]) % MOD
        }

        // multiply by any subset of ones
        if (ones > 0) {
            var pow = 1L
            var base = 2L
            var e = ones
            while (e > 0) {
                if ((e and 1) == 1) pow = (pow * base) % MOD
                base = (base * base) % MOD
                e = e shr 1
            }
            ans = (ans * pow) % MOD
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;
  int numberOfGoodSubsets(List<int> nums) {
    // Frequency count
    List<int> freq = List.filled(31, 0);
    for (int v in nums) {
      freq[v]++;
    }
    int ones = freq[1];

    // Primes up to 30
    const List<int> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
    Map<int, int> primeToBit = {};
    for (int i = 0; i < primes.length; ++i) {
      primeToBit[primes[i]] = i;
    }

    // Precompute masks for numbers 2..30
    List<int> numMask = List.filled(31, -1);
    for (int val = 2; val <= 30; ++val) {
      int x = val;
      int mask = 0;
      bool ok = true;
      for (int p in primes) {
        if (p * p > x) break;
        if (x % p == 0) {
          int cnt = 0;
          while (x % p == 0) {
            x ~/= p;
            cnt++;
          }
          if (cnt > 1) {
            ok = false;
            break;
          }
          mask |= (1 << primeToBit[p]!);
        }
      }
      if (!ok) continue;
      if (x > 1) {
        // x is a remaining prime factor
        if (!primeToBit.containsKey(x)) {
          ok = false;
        } else {
          mask |= (1 << primeToBit[x]!);
        }
      }
      if (ok) numMask[val] = mask;
    }

    int maxMask = 1 << primes.length; // 1024
    List<int> dp = List.filled(maxMask, 0);
    dp[0] = 1;

    for (int val = 2; val <= 30; ++val) {
      int cnt = freq[val];
      if (cnt == 0) continue;
      int mask = numMask[val];
      if (mask == -1) continue; // invalid number
      for (int m = maxMask - 1; m >= 0; --m) {
        int cur = dp[m];
        if (cur == 0) continue;
        if ((m & mask) != 0) continue;
        int newMask = m | mask;
        dp[newMask] = (dp[newMask] + (cur * cnt) % _MOD) % _MOD;
      }
    }

    int ans = 0;
    for (int m = 1; m < maxMask; ++m) {
      ans += dp[m];
      if (ans >= _MOD) ans -= _MOD;
    }

    if (ones > 0 && ans > 0) {
      ans = (ans * _modPow(2, ones)) % _MOD;
    }
    return ans;
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
package main

import "math"

const MOD int64 = 1000000007
const PRIME_COUNT = 10

func numberOfGoodSubsets(nums []int) int {
	// Count frequencies
	freq := make([]int, 31)
	for _, v := range nums {
		freq[v]++
	}
	ones := freq[1]

	// Primes up to 30
	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

	// Precompute mask for each number (square‑free numbers only)
	masks := make([]int, 31)
	for i := range masks {
		masks[i] = -1
	}
	for num := 2; num <= 30; num++ {
		x := num
		mask := 0
		valid := true
		for idx, p := range primes {
			if x%p == 0 {
				cnt := 0
				for x%p == 0 {
					x /= p
					cnt++
				}
				if cnt > 1 { // square factor
					valid = false
					break
				}
				mask |= 1 << idx
			}
		}
		if valid && x == 1 {
			masks[num] = mask
		}
	}

	dp := make([]int64, 1<<PRIME_COUNT)
	dp[0] = 1

	for num := 2; num <= 30; num++ {
		if freq[num] == 0 || masks[num] == -1 {
			continue
		}
		mask := masks[num]
		cnt := int64(freq[num])
		// iterate masks in reverse to avoid reuse within same number
		for m := (1 << PRIME_COUNT) - 1; m >= 0; m-- {
			if dp[m] == 0 {
				continue
			}
			if m&mask != 0 {
				continue
			}
			newMask := m | mask
			dp[newMask] = (dp[newMask] + dp[m]*cnt) % MOD
		}
	}

	var ans int64 = 0
	for m := 1; m < (1 << PRIME_COUNT); m++ {
		ans = (ans + dp[m]) % MOD
	}
	if ones > 0 && ans > 0 {
		pow2 := fastPow(2, int64(ones))
		ans = ans * pow2 % MOD
	}
	return int(ans)
}

func fastPow(base, exp int64) int64 {
	result := int64(1)
	b := base % MOD
	e := exp
	for e > 0 {
		if e&1 == 1 {
			result = result * b % MOD
		}
		b = b * b % MOD
		e >>= 1
	}
	return result
}
```

## Ruby

```ruby
def number_of_good_subsets(nums)
  mod = 1_000_000_007
  cnt = Array.new(31, 0)
  nums.each { |x| cnt[x] += 1 }

  primes = [2,3,5,7,11,13,17,19,23,29]
  prime_bit = {}
  primes.each_with_index { |p, i| prime_bit[p] = i }

  masks = Array.new(31, 0)
  (2..30).each do |v|
    temp = v
    mask = 0
    ok = true
    primes.each do |p|
      next unless temp % p == 0
      exp = 0
      while temp % p == 0
        temp /= p
        exp += 1
      end
      if exp > 1
        ok = false
        break
      else
        mask |= (1 << prime_bit[p])
      end
    end
    masks[v] = mask if ok && v != 1
  end

  dp = Array.new(1 << primes.size, 0)
  dp[0] = 1

  (2..30).each do |v|
    c = cnt[v]
    next if c == 0 || masks[v] == 0
    m = masks[v]
    (dp.size - 1).downto(0) do |mask|
      next if dp[mask] == 0
      if (mask & m).zero?
        new_mask = mask | m
        dp[new_mask] = (dp[new_mask] + dp[mask] * c) % mod
      end
    end
  end

  total = 0
  (1...dp.size).each { |mask| total = (total + dp[mask]) % mod }

  cnt1 = cnt[1]
  if cnt1 > 0
    pow2 = 1
    base = 2
    exp = cnt1
    while exp > 0
      pow2 = (pow2 * base) % mod if (exp & 1) == 1
      base = (base * base) % mod
      exp >>= 1
    end
    total = (total * pow2) % mod
  end

  total
end
```

## Scala

```scala
object Solution {
    def numberOfGoodSubsets(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        val primes = Array(2,3,5,7,11,13,17,19,23,29)
        val numMask = new Array[Int](31)

        for (i <- 2 to 30) {
            var x = i
            var mask = 0
            var ok = true
            for (j <- primes.indices) {
                val p = primes(j)
                if (x % p == 0) {
                    var cnt = 0
                    while (x % p == 0) {
                        x /= p
                        cnt += 1
                    }
                    if (cnt > 1) ok = false
                    else mask |= (1 << j)
                }
            }
            if (ok && x == 1) numMask(i) = mask else numMask(i) = 0
        }

        val cnt = new Array[Int](31)
        for (v <- nums) cnt(v) += 1

        var dp = new Array[Long](1 << primes.length)
        dp(0) = 1L

        for (i <- 2 to 30) {
            val c = cnt(i)
            if (c > 0 && numMask(i) != 0) {
                val m = numMask(i)
                for (mask <- (dp.length - 1) to 0 by -1) {
                    if ((mask & m) == 0) {
                        val newMask = mask | m
                        dp(newMask) = (dp(newMask) + dp(mask) * c) % MOD
                    }
                }
            }
        }

        var ans: Long = 0L
        for (mask <- 1 until dp.length) {
            ans = (ans + dp(mask)) % MOD
        }

        var pow2: Long = 1L
        var cnt1 = cnt(1)
        var base = 2L
        while (cnt1 > 0) {
            if ((cnt1 & 1) == 1) pow2 = (pow2 * base) % MOD
            base = (base * base) % MOD
            cnt1 >>= 1
        }

        ans = (ans * pow2) % MOD
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_good_subsets(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        const PRIMES: [i32; 10] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        // count occurrences
        let mut cnt = vec![0usize; 31];
        for v in nums {
            cnt[v as usize] += 1;
        }
        // precompute mask for each value (square‑free numbers only)
        let mut masks = vec![-1i32; 31];
        for val in 2..=30 {
            let mut x = val;
            let mut m: i32 = 0;
            let mut ok = true;
            for (i, &p) in PRIMES.iter().enumerate() {
                if p * p > x { break; }
                if x % p == 0 {
                    let mut c = 0;
                    while x % p == 0 {
                        x /= p;
                        c += 1;
                    }
                    if c > 1 {
                        ok = false;
                        break;
                    }
                    m |= 1 << i;
                }
            }
            if ok && x > 1 {
                // x is a remaining prime factor
                let idx = PRIMES.iter().position(|&prime| prime == x as i32).unwrap();
                m |= 1 << idx;
            }
            if ok {
                masks[val] = m;
            }
        }

        let size = 1usize << PRIMES.len(); // 1024
        let mut dp = vec![0i64; size];
        dp[0] = 1;

        for val in 2..=30 {
            let c = cnt[val];
            if c == 0 { continue; }
            let mask_i32 = masks[val];
            if mask_i32 == -1 { continue; } // not square‑free
            let mask = mask_i32 as usize;
            // iterate masks in reverse to avoid reuse within same iteration
            for existing in (0..size).rev() {
                if dp[existing] == 0 { continue; }
                if (existing & mask) == 0 {
                    let new_mask = existing | mask;
                    dp[new_mask] = (dp[new_mask] + dp[existing] * c as i64) % MOD;
                }
            }
        }

        // sum all non‑empty masks
        let mut ans: i64 = 0;
        for (i, &val) in dp.iter().enumerate() {
            if i != 0 {
                ans += val;
                if ans >= MOD { ans -= MOD; }
            }
        }

        // account for ones
        let ones = cnt[1];
        let mut pow2: i64 = 1;
        let mut base: i64 = 2;
        let mut exp = ones;
        while exp > 0 {
            if exp & 1 == 1 {
                pow2 = pow2 * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }

        ans = ans * pow2 % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define primes '(2 3 5 7 11 13 17 19 23 29))

;; compute mask of prime factors for n; return -1 if n has a squared prime factor or leftover >1
(define (get-mask n)
  (let ([mask 0] [valid #t])
    (for ([p primes] [idx (in-naturals)])
      (when (and valid (> n 1))
        (if (= (remainder n p) 0)
            (begin
              (set! n (/ n p))
              (when (= (remainder n p) 0)
                (set! valid #f))
              (set! mask (bitwise-ior mask (arithmetic-shift 1 idx)))))))
    (if (and valid (= n 1)) mask -1))

;; fast modular exponentiation
(define (pow-mod base exp mod)
  (let loop ((b (modulo base mod)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (modulo (* b b) mod)
              (quotient e 2)
              (if (= (remainder e 1) 0) res (modulo (* res b) mod))))))

(define/contract (number-of-good-subsets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([freq (make-vector 31 0)]
         [_   (for ([x nums]) (vector-set! freq x (+ (vector-ref freq x) 1)))]
         [cnt1 (vector-ref freq 1)]
         [prime-count (length primes)]
         [maxMask (expt 2 prime-count)]
         [dp (make-vector maxMask 0)])
    (vector-set! dp 0 1)
    ;; process numbers from 2 to 30
    (for ([num (in-range 2 31)])
      (let ([c (vector-ref freq num)])
        (when (> c 0)
          (let ([mask (get-mask num)])
            (when (>= mask 0) ; valid number
              ;; iterate masks descending to avoid reuse within same iteration
              (for ([old-mask (in-range (sub1 maxMask) -1 -1)])
                (let ([val (vector-ref dp old-mask)])
                  (when (> val 0)
                    (when (= (bitwise-and old-mask mask) 0)
                      (let* ([new-mask (bitwise-ior old-mask mask)]
                             [add (modulo (* val c) MOD)]
                             [cur (vector-ref dp new-mask)])
                        (vector-set! dp new-mask (modulo (+ cur add) MOD))))))))))))
    ;; sum all non‑empty masks
    (let ([sum (let loop ((m 1) (acc 0))
                 (if (= m maxMask)
                     acc
                     (loop (+ m 1) (modulo (+ acc (vector-ref dp m)) MOD))))])
      (modulo (* sum (pow-mod 2 cnt1 MOD)) MOD))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_good_subsets/1]).

-define(MOD, 1000000007).

number_of_good_subsets(Nums) ->
    Freq = count_freq(Nums, #{}),
    Cnt1 = maps:get(1, Freq, 0),

    MaskMap = build_mask_map(),
    DP0 = #{0 => 1},
    DP = maps:fold(fun(Num, Mask, AccDP) ->
                case maps:get(Num, Freq, undefined) of
                    undefined -> AccDP;
                    F when F > 0 ->
                        update_dp(AccDP, Mask, F)
                end
            end, DP0, MaskMap),

    Sum = maps:fold(fun(Mask, Val, Acc) ->
                if Mask =/= 0 -> (Acc + Val) rem ?MOD; true -> Acc end
            end, 0, DP),
    Pow2Cnt1 = pow_mod(2, Cnt1, ?MOD),
    (Sum * Pow2Cnt1) rem ?MOD.

%% count frequencies of numbers in the list
count_freq([], Map) -> Map;
count_freq([H|T], Map) ->
    NewMap = maps:update_with(H,
                fun(V) -> V + 1 end,
                1,
                Map),
    count_freq(T, NewMap).

%% build map Num -> Mask for square‑free numbers (2..30)
build_mask_map() ->
    Primes = [2,3,5,7,11,13,17,19,23,29],
    lists:foldl(fun(N, Acc) ->
                case get_mask(N, Primes) of
                    -1 -> Acc;
                    Mask -> maps:put(N, Mask, Acc)
                end
            end, #{}, lists:seq(2,30)).

%% compute bitmask of distinct prime factors; return -1 if any square factor exists
get_mask(N, Primes) ->
    get_mask(N, Primes, 0, 0).

get_mask(1, [], _Idx, Mask) -> Mask;
get_mask(_, [], _, _) -> -1;
get_mask(Num, [P|Rest], Idx, Mask) ->
    case Num rem P of
        0 ->
            Num1 = Num div P,
            case Num1 rem P of
                0 -> -1;                     % square factor
                _ ->
                    NewMask = Mask bor (1 bsl Idx),
                    get_mask(Num1, Rest, Idx+1, NewMask)
            end;
        _ ->
            get_mask(Num, Rest, Idx+1, Mask)
    end.

%% update DP with a new number having mask NumMask and frequency Freq
update_dp(DPMap, NumMask, Freq) ->
    maps:fold(fun(PrevMask, PrevCnt, Acc) ->
                if (PrevMask band NumMask) =:= 0 ->
                        NewMask = PrevMask bor NumMask,
                        Add = (PrevCnt * Freq) rem ?MOD,
                        Old = maps:get(NewMask, Acc, 0),
                        maps:put(NewMask, (Old + Add) rem ?MOD, Acc);
                   true -> Acc
                end
            end, DPMap, DPMap).

%% fast modular exponentiation
pow_mod(_Base, 0, _Mod) -> 1;
pow_mod(Base, Exp, Mod) ->
    pow_mod(Base rem Mod, Exp, Mod, 1).

pow_mod(_, 0, _, Acc) -> Acc;
pow_mod(B, E, M, Acc) when (E band 1) =:= 1 ->
    pow_mod((B * B) rem M, E bsr 1, M, (Acc * B) rem M);
pow_mod(B, E, M, Acc) ->
    pow_mod((B * B) rem M, E bsr 1, M, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007
  @mask_map %{
    2 => 1,
    3 => 2,
    5 => 4,
    6 => 3,
    7 => 8,
    10 => 5,
    11 => 16,
    13 => 32,
    14 => 9,
    15 => 6,
    17 => 64,
    19 => 128,
    21 => 10,
    22 => 17,
    23 => 256,
    26 => 33,
    29 => 512,
    30 => 7
  }

  @spec number_of_good_subsets(nums :: [integer]) :: integer
  def number_of_good_subsets(nums) do
    freq = Enum.frequencies(nums)
    cnt_one = Map.get(freq, 1, 0)

    dp =
      Enum.reduce(@mask_map, %{0 => 1}, fn {num, mask}, dp_acc ->
        cnt = Map.get(freq, num, 0)

        if cnt == 0 do
          dp_acc
        else
          snapshot = dp_acc

          Enum.reduce(snapshot, dp_acc, fn {state_mask, ways}, inner_dp ->
            if Bitwise.band(state_mask, mask) == 0 do
              new_mask = Bitwise.bor(state_mask, mask)
              add = rem(ways * cnt, @mod)

              Map.update(inner_dp, new_mask, add, fn existing ->
                rem(existing + add, @mod)
              end)
            else
              inner_dp
            end
          end)
        end
      end)

    total =
      dp
      |> Enum.reduce(0, fn {mask, cnt}, acc ->
        if mask != 0 do
          rem(acc + cnt, @mod)
        else
          acc
        end
      end)

    pow2 = mod_pow(2, cnt_one, @mod)
    rem(total * pow2, @mod)
  end

  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) do
    base = rem(base, mod)
    do_mod_pow(base, exp, mod, 1)
  end

  defp do_mod_pow(_base, 0, _mod, acc), do: acc

  defp do_mod_pow(base, exp, mod, acc) do
    acc =
      if Bitwise.band(exp, 1) == 1 do
        rem(acc * base, mod)
      else
        acc
      end

    base = rem(base * base, mod)
    do_mod_pow(base, div(exp, 2), mod, acc)
  end
end
```

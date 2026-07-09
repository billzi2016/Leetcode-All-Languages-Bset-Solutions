# 2572. Count the Number of Square-Free Subsets

## Cpp

```cpp
class Solution {
public:
    int squareFreeSubsets(vector<int>& nums) {
        const int MOD = 1000000007;
        vector<int> primes = {2,3,5,7,11,13,17,19,23,29};
        // precompute mask for numbers 1..30, -1 if not square-free
        vector<int> numMask(31, -1);
        numMask[1] = 0;
        for (int v = 2; v <= 30; ++v) {
            int x = v;
            int mask = 0;
            bool ok = true;
            for (int i = 0; i < (int)primes.size(); ++i) {
                int p = primes[i];
                if (x % p == 0) {
                    int cnt = 0;
                    while (x % p == 0) {
                        x /= p;
                        ++cnt;
                    }
                    if (cnt > 1) { // square factor
                        ok = false;
                        break;
                    }
                    mask |= (1 << i);
                }
            }
            if (ok && x == 1) numMask[v] = mask; // x should be 1 after factoring primes <=30
        }

        int SZ = 1 << primes.size(); // 1024
        vector<int> dp(SZ, 0), ndp;
        dp[0] = 1;

        for (int val : nums) {
            if (val == 1) {
                for (int i = 0; i < SZ; ++i) {
                    dp[i] = (dp[i] * 2LL) % MOD;
                }
                continue;
            }
            int m = numMask[val];
            if (m == -1) continue; // cannot be used
            ndp = dp;
            for (int mask = 0; mask < SZ; ++mask) {
                if ((mask & m) == 0) {
                    int nmask = mask | m;
                    ndp[nmask] += dp[mask];
                    if (ndp[nmask] >= MOD) ndp[nmask] -= MOD;
                }
            }
            dp.swap(ndp);
        }

        long long total = 0;
        for (int v : dp) {
            total += v;
            if (total >= MOD) total -= MOD;
        }
        // exclude empty subset
        total = (total - 1 + MOD) % MOD;
        return (int)total;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int squareFreeSubsets(int[] nums) {
        int[] primes = {2,3,5,7,11,13,17,19,23,29};
        int fullMask = (1 << primes.length) - 1;
        long[] dp = new long[1 << primes.length];
        dp[0] = 1; // empty subset
        for (int val : nums) {
            int x = val;
            int mask = 0;
            boolean ok = true;
            for (int i = 0; i < primes.length; i++) {
                int p = primes[i];
                if (x % p == 0) {
                    int cnt = 0;
                    while (x % p == 0) {
                        x /= p;
                        cnt++;
                    }
                    if (cnt > 1) { // contains a square factor
                        ok = false;
                        break;
                    }
                    mask |= (1 << i);
                }
            }
            if (!ok) continue; // cannot be part of any square‑free subset
            for (int m = fullMask; m >= 0; --m) {
                if ((m & mask) == 0) {
                    int newMask = m | mask;
                    dp[newMask] = (dp[newMask] + dp[m]) % MOD;
                }
            }
        }
        long ans = 0;
        for (long v : dp) ans = (ans + v) % MOD;
        ans = (ans - 1 + MOD) % MOD; // exclude empty subset
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def squareFreeSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        primes = [2,3,5,7,11,13,17,19,23,29]
        # precompute mask for numbers 1..30, -1 if not square-free
        num_mask = [-1] * 31
        for x in range(1,31):
            m = 0
            ok = True
            y = x
            for i,p in enumerate(primes):
                cnt = 0
                while y % p == 0:
                    y //= p
                    cnt += 1
                if cnt > 1:   # square factor
                    ok = False
                    break
                if cnt == 1:
                    m |= (1 << i)
            if ok and y == 1:   # fully factored by primes <=30
                num_mask[x] = m
        cnt_one = sum(1 for v in nums if v == 1)

        dp = [0]*1024
        dp[0] = 1
        for v in nums:
            if v == 1:
                continue
            mask = num_mask[v]
            if mask == -1:
                continue
            old = dp[:]   # snapshot before using current number
            for m in range(1024):
                if old[m] and (m & mask) == 0:
                    dp[m | mask] = (dp[m | mask] + old[m]) % MOD

        total = sum(dp) % MOD
        pow2_one = pow(2, cnt_one, MOD)
        ans = (total * pow2_one - 1) % MOD   # exclude empty subset
        return ans
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2,3,5,7,11,13,17,19,23,29]
        prime_to_bit = {p:i for i,p in enumerate(primes)}
        
        # precompute mask for numbers 2..30 that are square-free
        num_mask = {}
        for x in range(2,31):
            y = x
            mask = 0
            ok = True
            for p in primes:
                if p*p > y:
                    break
                cnt = 0
                while y % p == 0:
                    y //= p
                    cnt += 1
                if cnt > 1:
                    ok = False
                    break
                if cnt == 1:
                    mask |= 1 << prime_to_bit[p]
            if not ok:
                continue
            if y > 1:  # remaining prime factor
                # y is a prime <=30, exponent is 1
                mask |= 1 << prime_to_bit[y]
            num_mask[x] = mask
        
        freq = Counter(nums)
        dp = [0]* (1<<10)
        dp[0] = 1
        
        for val, cnt in freq.items():
            if val == 1 or cnt == 0:
                continue
            if val not in num_mask:
                continue  # contains a squared prime factor, cannot be used
            m = num_mask[val]
            newdp = dp[:]
            for mask in range(1<<10):
                if dp[mask] == 0:
                    continue
                if mask & m == 0:
                    nmask = mask | m
                    newdp[nmask] = (newdp[nmask] + dp[mask] * cnt) % MOD
            dp = newdp
        
        total = sum(dp) % MOD
        ones = freq.get(1,0)
        total = (total * pow(2, ones, MOD) - 1) % MOD
        return total
```

## C

```c
#include <stddef.h>
#include <stdint.h>

#define MOD 1000000007

static int modPow(int base, int exp) {
    int64_t result = 1;
    int64_t b = base;
    while (exp > 0) {
        if (exp & 1) result = (result * b) % MOD;
        b = (b * b) % MOD;
        exp >>= 1;
    }
    return (int)result;
}

int squareFreeSubsets(int* nums, int numsSize) {
    // primes up to 30
    const int primes[10] = {2,3,5,7,11,13,17,19,23,29};
    int maskMap[31];
    for (int i = 0; i <= 30; ++i) maskMap[i] = -1;
    maskMap[1] = 0;
    // precompute masks for square‑free numbers
    for (int v = 2; v <= 30; ++v) {
        int x = v;
        int curMask = 0;
        int ok = 1;
        for (int j = 0; j < 10; ++j) {
            if (x % primes[j] == 0) {
                int cnt = 0;
                while (x % primes[j] == 0) {
                    x /= primes[j];
                    ++cnt;
                }
                if (cnt > 1) { ok = 0; break; }
                curMask |= (1 << j);
            }
        }
        if (ok && x == 1) maskMap[v] = curMask;
    }

    int64_t dp[1 << 10] = {0};
    dp[0] = 1;
    int cntOne = 0;

    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        if (val == 1) {
            ++cntOne;
            continue;
        }
        int curMask = maskMap[val];
        if (curMask == -1) continue; // not square‑free, skip
        for (int m = (1 << 10) - 1; m >= 0; --m) {
            if ((m & curMask) == 0) {
                dp[m | curMask] += dp[m];
                if (dp[m | curMask] >= MOD) dp[m | curMask] -= MOD;
            }
        }
    }

    int64_t total = 0;
    for (int m = 0; m < (1 << 10); ++m) {
        total += dp[m];
        if (total >= MOD) total -= MOD;
    }

    int powOnes = modPow(2, cntOne);
    int64_t ans = (total * powOnes) % MOD;
    ans = (ans - 1 + MOD) % MOD; // exclude empty subset

    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1_000_000_007;
    public int SquareFreeSubsets(int[] nums) {
        // primes up to 30
        int[] primes = new int[] {2,3,5,7,11,13,17,19,23,29};
        int primeCount = primes.Length;
        int maxMask = 1 << primeCount;

        // precompute mask for each number 2..30, -1 if not square‑free
        int[] numMask = new int[31];
        for (int v = 2; v <= 30; v++) {
            int x = v;
            int mask = 0;
            bool ok = true;
            for (int i = 0; i < primeCount; i++) {
                int p = primes[i];
                if (p * p > x) break;
                int cnt = 0;
                while (x % p == 0) {
                    cnt++;
                    x /= p;
                }
                if (cnt > 1) { ok = false; break; }
                if (cnt == 1) mask |= 1 << i;
            }
            if (!ok) {
                numMask[v] = -1;
                continue;
            }
            // x may be a prime larger than sqrt(v)
            if (x > 1) {
                // find its index
                int idx = Array.IndexOf(primes, x);
                if (idx == -1) { // should not happen for v<=30
                    numMask[v] = -1;
                    continue;
                }
                mask |= 1 << idx;
            }
            numMask[v] = mask;
        }

        long pow2Ones = 1; // 2^{count of ones}
        int[] dp = new int[maxMask];
        dp[0] = 1;

        foreach (int val in nums) {
            if (val == 1) {
                pow2Ones = (pow2Ones * 2) % MOD;
                continue;
            }
            int m = numMask[val];
            if (m == -1) continue; // not square‑free, cannot be used
            for (int mask = maxMask - 1; mask >= 0; mask--) {
                int cur = dp[mask];
                if (cur == 0) continue;
                if ((mask & m) != 0) continue;
                int newMask = mask | m;
                dp[newMask] = (int)((dp[newMask] + cur) % MOD);
            }
        }

        long total = 0;
        for (int mask = 1; mask < maxMask; mask++) {
            total += dp[mask];
        }
        total %= MOD;

        // combine with subsets of ones
        total = (total * pow2Ones) % MOD;
        // add subsets consisting only of ones (non‑empty)
        long onlyOnes = (pow2Ones - 1 + MOD) % MOD;
        total = (total + onlyOnes) % MOD;

        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var squareFreeSubsets = function(nums) {
    const MOD = 1000000007n;
    const primes = [2,3,5,7,11,13,17,19,23,29];
    const primeIdx = {};
    for (let i = 0; i < primes.length; ++i) primeIdx[primes[i]] = i;

    // precompute mask for numbers 2..30, -1 means not square‑free
    const masks = new Array(31).fill(-1);
    for (let num = 2; num <= 30; ++num) {
        let x = num;
        let m = 0;
        let ok = true;
        for (const p of primes) {
            if (p * p > x) break;
            let cnt = 0;
            while (x % p === 0) {
                x /= p;
                ++cnt;
            }
            if (cnt > 1) { ok = false; break; }
            if (cnt === 1) m |= (1 << primeIdx[p]);
        }
        if (!ok) continue;
        if (x > 1) { // remaining prime factor
            const idx = primeIdx[x];
            if (idx === undefined) { ok = false; }
            else m |= (1 << idx);
        }
        if (ok) masks[num] = m;
    }

    let cntOne = 0;
    const dpSize = 1 << primes.length; // 1024
    const dp = new Array(dpSize).fill(0n);
    dp[0] = 1n;

    for (const v of nums) {
        if (v === 1) { ++cntOne; continue; }
        const m = masks[v];
        if (m === -1) continue; // not square‑free, skip
        for (let mask = dpSize - 1; mask >= 0; --mask) {
            if ((mask & m) === 0) {
                dp[mask | m] = (dp[mask | m] + dp[mask]) % MOD;
            }
        }
    }

    let total = 0n;
    for (let i = 0; i < dpSize; ++i) {
        total = (total + dp[i]) % MOD;
    }

    // multiply by ways to choose ones
    const pow2 = (exp) => {
        let base = 2n, res = 1n, e = BigInt(exp);
        while (e > 0n) {
            if (e & 1n) res = (res * base) % MOD;
            base = (base * base) % MOD;
            e >>= 1n;
        }
        return res;
    };
    total = (total * pow2(cntOne)) % MOD;

    // exclude empty subset
    total = (total - 1n + MOD) % MOD;

    return Number(total);
};
```

## Typescript

```typescript
function squareFreeSubsets(nums: number[]): number {
    const MOD = 1000000007;
    const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
    const primeIdx = new Map<number, number>();
    for (let i = 0; i < primes.length; i++) primeIdx.set(primes[i], i);

    // maskArr[n] = bitmask of distinct prime factors if n is square‑free, else -1
    const maskArr = new Array<number>(31).fill(-1);
    for (let n = 2; n <= 30; n++) {
        let x = n;
        let mask = 0;
        let ok = true;
        for (const p of primes) {
            if (p * p > x) break;
            if (x % p === 0) {
                let cnt = 0;
                while (x % p === 0) {
                    x /= p;
                    cnt++;
                }
                if (cnt > 1) {
                    ok = false;
                    break;
                }
                mask |= 1 << primeIdx.get(p)!;
            }
        }
        if (!ok) continue;
        if (x > 1) { // remaining prime factor
            const idx = primeIdx.get(x);
            if (idx === undefined) continue; // should not happen for n<=30
            mask |= 1 << idx;
        }
        maskArr[n] = mask;
    }

    let cntOne = 0;
    const masks: number[] = [];
    for (const v of nums) {
        if (v === 1) {
            cntOne++;
        } else {
            const m = maskArr[v];
            if (m !== -1) masks.push(m);
        }
    }

    const SZ = 1 << primes.length; // 1024
    let dp = new Array<number>(SZ).fill(0);
    dp[0] = 1;

    for (const m of masks) {
        const ndp = dp.slice();
        for (let s = 0; s < SZ; s++) {
            if ((s & m) === 0) {
                ndp[s | m] = (ndp[s | m] + dp[s]) % MOD;
            }
        }
        dp = ndp;
    }

    let sumAll = 0;
    for (const val of dp) {
        sumAll = (sumAll + val) % MOD;
    }

    const modPow2 = (exp: number): number => {
        let res = 1, base = 2, e = exp;
        while (e > 0) {
            if (e & 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            e >>= 1;
        }
        return res;
    };

    const total = (sumAll * modPow2(cntOne)) % MOD;
    const ans = (total - 1 + MOD) % MOD; // exclude empty subset
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
    function squareFreeSubsets($nums) {
        $MOD = 1000000007;
        $primes = [2,3,5,7,11,13,17,19,23,29];
        $primeCount = count($primes);
        $maxMask = 1 << $primeCount; // 1024
        $dp = array_fill(0, $maxMask, 0);
        $dp[0] = 1;
        $cntOnes = 0;

        foreach ($nums as $num) {
            if ($num == 1) {
                $cntOnes++;
                continue;
            }

            // compute mask for the number; -1 if it contains a squared prime factor
            $mask = 0;
            $tmp = $num;
            $invalid = false;
            foreach ($primes as $i => $p) {
                if ($tmp % $p == 0) {
                    $cnt = 0;
                    while ($tmp % $p == 0) {
                        $tmp /= $p;
                        $cnt++;
                    }
                    if ($cnt > 1) { // squared prime factor
                        $invalid = true;
                        break;
                    }
                    $mask |= (1 << $i);
                }
            }
            if ($invalid) continue; // cannot be used

            // DP transition using a snapshot of previous dp values
            $prev = $dp;
            for ($m = 0; $m < $maxMask; $m++) {
                if (($m & $mask) == 0) {
                    $newMask = $m | $mask;
                    $dp[$newMask] = ($dp[$newMask] + $prev[$m]) % $MOD;
                }
            }
        }

        // sum all non‑empty subsets formed without ones
        $total = 0;
        for ($m = 1; $m < $maxMask; $m++) {
            $total = ($total + $dp[$m]) % $MOD;
        }

        // compute 2^cntOnes modulo MOD
        $powTwo = 1;
        $base = 2;
        $exp = $cntOnes;
        while ($exp > 0) {
            if ($exp & 1) {
                $powTwo = ($powTwo * $base) % $MOD;
            }
            $base = ($base * $base) % $MOD;
            $exp >>= 1;
        }

        // combine subsets with ones and add subsets consisting only of ones
        $answer = ( ($total * $powTwo) % $MOD + ($powTwo - 1 + $MOD) % $MOD ) % $MOD;
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func squareFreeSubsets(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        var count = [Int](repeating: 0, count: 31)
        for v in nums { count[v] += 1 }
        
        let primes = [2,3,5,7,11,13,17,19,23,29]
        var masks = [Int](repeating: -1, count: 31)   // -1 means invalid (contains squared prime)
        for val in 2...30 {
            var x = val
            var mask = 0
            var ok = true
            for (i, p) in primes.enumerated() {
                if p * p > x { break }
                var exp = 0
                while x % p == 0 {
                    x /= p
                    exp += 1
                }
                if exp > 1 {
                    ok = false
                    break
                } else if exp == 1 {
                    mask |= (1 << i)
                }
            }
            if ok && x > 1 {
                if let idx = primes.firstIndex(of: x) {
                    mask |= (1 << idx)
                } else {
                    ok = false
                }
            }
            masks[val] = ok ? mask : -1
        }
        
        var dp = [Int](repeating: 0, count: 1 << 10)
        dp[0] = 1
        
        for val in 2...30 {
            let freq = count[val]
            if freq == 0 { continue }
            let m = masks[val]
            if m == -1 { continue }   // cannot be used
            var newDP = dp
            for mask in 0..<(1 << 10) {
                let cur = dp[mask]
                if cur == 0 { continue }
                if (mask & m) != 0 { continue }
                let combined = mask | m
                let add = Int((Int64(cur) * Int64(freq)) % Int64(MOD))
                newDP[combined] = (newDP[combined] + add) % MOD
            }
            dp = newDP
        }
        
        var sumAll = 0
        for v in dp {
            sumAll = (sumAll + v) % MOD
        }
        
        let cnt1 = count[1]
        var pow2 = 1
        if cnt1 > 0 {
            var base = 2
            var exp = cnt1
            var result = 1
            while exp > 0 {
                if (exp & 1) == 1 {
                    result = Int((Int64(result) * Int64(base)) % Int64(MOD))
                }
                base = Int((Int64(base) * Int64(base)) % Int64(MOD))
                exp >>= 1
            }
            pow2 = result
        }
        
        var ans = Int((Int64(sumAll) * Int64(pow2)) % Int64(MOD))
        ans = (ans - 1 + MOD) % MOD   // exclude empty subset
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) {
                res = (res * b) % MOD
            }
            b = (b * b) % MOD
            e = e shr 1
        }
        return res
    }

    fun squareFreeSubsets(nums: IntArray): Int {
        val primes = intArrayOf(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        var onesCount = 0
        val dp = LongArray(1 shl 10)
        dp[0] = 1L

        for (num in nums) {
            if (num == 1) {
                onesCount++
                continue
            }
            var x = num
            var mask = 0
            var ok = true
            for (i in primes.indices) {
                val p = primes[i]
                if (x % p == 0) {
                    var cnt = 0
                    while (x % p == 0) {
                        x /= p
                        cnt++
                    }
                    if (cnt > 1) { // contains a square factor
                        ok = false
                        break
                    }
                    mask = mask or (1 shl i)
                }
            }
            if (!ok) continue
            // update dp in reverse to avoid reuse within same iteration
            for (s in dp.indices.reversed()) {
                if ((s and mask) == 0) {
                    val ns = s or mask
                    dp[ns] = (dp[ns] + dp[s]) % MOD
                }
            }
        }

        var total = 0L
        for (v in dp) {
            total = (total + v) % MOD
        }
        total = total * modPow(2L, onesCount.toLong()) % MOD
        total = (total - 1 + MOD) % MOD // exclude empty subset
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;

  int squareFreeSubsets(List<int> nums) {
    const List<int> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
    int cnt1 = 0;
    List<int> masks = [];

    for (int num in nums) {
      if (num == 1) {
        cnt1++;
        continue;
      }
      int x = num;
      int mask = 0;
      bool ok = true;

      for (int i = 0; i < primes.length && primes[i] * primes[i] <= x; i++) {
        int p = primes[i];
        int cnt = 0;
        while (x % p == 0) {
          x ~/= p;
          cnt++;
        }
        if (cnt > 1) {
          ok = false;
          break;
        }
        if (cnt == 1) mask |= (1 << i);
      }

      if (!ok) continue;

      if (x > 1) {
        int idx = primes.indexOf(x);
        if (idx == -1) {
          // x is a prime larger than 29, which cannot happen for nums[i] <= 30
          ok = false;
        } else {
          mask |= (1 << idx);
        }
      }

      if (!ok) continue;
      masks.add(mask);
    }

    int maxMask = 1 << primes.length; // 1024
    List<int> dp = List.filled(maxMask, 0);
    dp[0] = 1;

    for (int m in masks) {
      for (int mask = maxMask - 1; mask >= 0; mask--) {
        if (dp[mask] == 0) continue;
        if ((mask & m) != 0) continue;
        int newMask = mask | m;
        dp[newMask] = (dp[newMask] + dp[mask]) % MOD;
      }
    }

    int sum = 0;
    for (int mask = 1; mask < maxMask; mask++) {
      sum = (sum + dp[mask]) % MOD;
    }

    int pow2cnt = _modPow(2, cnt1);
    int ans = (sum * pow2cnt) % MOD;
    ans = (ans + (pow2cnt - 1 + MOD) % MOD) % MOD;
    return ans;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % MOD;
    int e = exp;
    while (e > 0) {
      if ((e & 1) == 1) result = (result * b) % MOD;
      b = (b * b) % MOD;
      e >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
func squareFreeSubsets(nums []int) int {
	const MOD int = 1000000007
	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
	primeIdx := map[int]int{}
	for i, p := range primes {
		primeIdx[p] = i
	}

	cnt1 := 0
	masks := []int{}

	for _, num := range nums {
		if num == 1 {
			cnt1++
			continue
		}
		mask := 0
		x := num
		valid := true

		for _, p := range primes {
			if p*p > x {
				break
			}
			exp := 0
			for x%p == 0 {
				x /= p
				exp++
				if exp > 1 {
					valid = false
					break
				}
			}
			if !valid {
				break
			}
			if exp == 1 {
				mask |= 1 << primeIdx[p]
			}
		}
		if valid && x > 1 {
			if idx, ok := primeIdx[x]; ok {
				mask |= 1 << idx
			} else {
				valid = false
			}
		}
		if valid {
			masks = append(masks, mask)
		}
	}

	dp := make([]int, 1<<10)
	dp[0] = 1

	for _, m := range masks {
		newDP := make([]int, len(dp))
		copy(newDP, dp)
		for mask := 0; mask < len(dp); mask++ {
			if dp[mask] == 0 {
				continue
			}
			if (mask & m) == 0 {
				nm := mask | m
				newDP[nm] = (newDP[nm] + dp[mask]) % MOD
			}
		}
		dp = newDP
	}

	total := 0
	for _, v := range dp {
		total = (total + v) % MOD
	}

	// pow2cnt1 = 2^cnt1 mod MOD
	pow2cnt1 := 1
	base := 2
	k := cnt1
	for k > 0 {
		if k&1 == 1 {
			pow2cnt1 = int(int64(pow2cnt1) * int64(base) % int64(MOD))
		}
		base = int(int64(base) * int64(base) % int64(MOD))
		k >>= 1
	}

	ans := (int(int64(total)*int64(pow2cnt1)%int64(MOD)) - 1) % MOD
	if ans < 0 {
		ans += MOD
	}
	return ans
}
```

## Ruby

```ruby
MOD = 1_000_000_007
PRIMES = [2,3,5,7,11,13,17,19,23,29]

def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = result * b % mod if (e & 1) == 1
    b = b * b % mod
    e >>= 1
  end
  result
end

def prime_mask(num)
  mask = 0
  n = num
  PRIMES.each_with_index do |p, idx|
    cnt = 0
    while (n % p).zero?
      n /= p
      cnt += 1
      break if cnt > 1
    end
    return nil if cnt > 1
    mask |= (1 << idx) if cnt == 1
  end
  return nil unless n == 1
  mask
end

def square_free_subsets(nums)
  mod = MOD
  cnt_one = 0
  freq = Hash.new(0)

  nums.each do |num|
    if num == 1
      cnt_one += 1
    else
      m = prime_mask(num)
      next if m.nil?
      freq[m] += 1
    end
  end

  max_mask = 1 << PRIMES.size
  dp = Array.new(max_mask, 0)
  dp[0] = 1

  freq.each do |mask, c|
    ndp = dp.clone
    (0...max_mask).each do |existing|
      next if dp[existing].zero?
      if (existing & mask) == 0
        new_mask = existing | mask
        ndp[new_mask] = (ndp[new_mask] + dp[existing] * c) % mod
      end
    end
    dp = ndp
  end

  total = dp.sum % mod
  pow2_ones = mod_pow(2, cnt_one, mod)
  ans = (total * pow2_ones - 1) % mod
  ans += mod if ans < 0
  ans
end
```

## Scala

```scala
object Solution {
  private val MOD: Long = 1000000007L
  private val primes: Array[Int] = Array(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
  private val primeCount: Int = primes.length
  private val maxMask: Int = 1 << primeCount

  def squareFreeSubsets(nums: Array[Int]): Int = {
    val cnt = new Array[Int](31)
    for (v <- nums) cnt(v) += 1

    // precompute mask for each value 2..30, -1 if not square‑free
    val masks = new Array[Int](31)
    for (v <- 2 to 30) {
      var n = v
      var mask = 0
      var ok = true
      var i = 0
      while (i < primeCount && n > 1 && ok) {
        val p = primes(i)
        if (n % p == 0) {
          var c = 0
          while (n % p == 0) {
            n /= p
            c += 1
            if (c > 1) ok = false // square factor found
          }
          if (ok) mask |= (1 << i)
        }
        i += 1
      }
      if (n > 1) { // remaining prime larger than sqrt(v), exponent is 1
        val idx = primes.indexOf(n)
        if (idx >= 0) mask |= (1 << idx) else ok = false
      }
      masks(v) = if (ok) mask else -1
    }

    val dp = new Array[Long](maxMask)
    dp(0) = 1L

    for (v <- 2 to 30) {
      val c = cnt(v)
      if (c > 0 && masks(v) != -1) {
        val m = masks(v)
        val ways = c.toLong
        var mask = maxMask - 1
        while (mask >= 0) {
          if ((mask & m) == 0 && dp(mask) != 0) {
            val newMask = mask | m
            dp(newMask) = (dp(newMask) + dp(mask) * ways) % MOD
          }
          mask -= 1
        }
      }
    }

    var sumNonZero: Long = 0L
    var i = 1
    while (i < maxMask) {
      sumNonZero += dp(i)
      if (sumNonZero >= MOD) sumNonZero -= MOD
      i += 1
    }

    val ones = cnt(1)
    val powOnes: Long = modPow(2L, ones, MOD)

    var ans = (sumNonZero * powOnes) % MOD
    if (ones > 0) {
      ans = (ans + (powOnes - 1 + MOD) % MOD) % MOD
    }
    ans.toInt
  }

  private def modPow(base: Long, exp: Int, mod: Long): Long = {
    var result = 1L
    var b = base % mod
    var e = exp
    while (e > 0) {
      if ((e & 1) == 1) result = (result * b) % mod
      b = (b * b) % mod
      e >>= 1
    }
    result
  }
}
```

## Rust

```rust
impl Solution {
    pub fn square_free_subsets(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        // frequency of each number (1..=30)
        let mut freq = vec![0usize; 31];
        for &v in &nums {
            freq[v as usize] += 1;
        }
        let cnt_one = freq[1];
        // dp over prime masks
        let size = 1 << primes.len(); // 1024
        let mut dp = vec![0i64; size];
        dp[0] = 1;
        for val in 2..=30 {
            let f = freq[val as usize];
            if f == 0 {
                continue;
            }
            // compute mask, skip if not square‑free
            let mut x = val;
            let mut mask = 0usize;
            let mut ok = true;
            for (i, &p) in primes.iter().enumerate() {
                if x % p == 0 {
                    x /= p;
                    if x % p == 0 {
                        ok = false; // squared prime factor
                        break;
                    }
                    mask |= 1 << i;
                }
            }
            if !ok || x > 1 {
                continue; // not usable
            }
            let ways = f as i64; // choose exactly one occurrence among f copies
            for m in (0..size).rev() {
                if dp[m] == 0 {
                    continue;
                }
                if m & mask == 0 {
                    let nm = m | mask;
                    dp[nm] = (dp[nm] + dp[m] * ways) % MOD;
                }
            }
        }
        // sum of non‑empty subsets that use at least one number >1
        let mut sum_non_empty = 0i64;
        for i in 1..size {
            sum_non_empty = (sum_non_empty + dp[i]) % MOD;
        }
        // power of two for ones
        fn mod_pow(mut base: i64, mut exp: usize, modu: i64) -> i64 {
            let mut res = 1i64;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = res * base % modu;
                }
                base = base * base % modu;
                exp >>= 1;
            }
            res
        }
        let pow2_one = mod_pow(2, cnt_one, MOD);
        // total answer
        let ans = (sum_non_empty * pow2_one % MOD + (pow2_one - 1 + MOD) % MOD) % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define primes '(2 3 5 7 11 13 17 19 23 29))

;; returns two values: mask and a boolean indicating whether the number is square‑free
(define (mask-and-valid n)
  (if (= n 1)
      (values 0 #t)
      (let ((mask 0) (valid #t) (temp n))
        (for ([p primes] [i (in-naturals)])
          (when (> temp 1)
            (let loop ((cnt 0) (rem temp))
              (if (= (remainder rem p) 0)
                  (loop (+ cnt 1) (/ rem p))
                  (begin
                    (cond [(> cnt 1) (set! valid #f)]
                          [(= cnt 1) (set! mask (bitwise-ior mask (arithmetic-shift 1 i)))])
                    (set! temp rem))))))
        (values mask valid))))

(define (square-free-subsets nums)
  (let* ((maxMask (arithmetic-shift 1 10))
         (dp (make-vector maxMask 0)))
    (vector-set! dp 0 1)
    (define cnt1 0)
    (for ([num nums])
      (cond [(= num 1) (set! cnt1 (+ cnt1 1))]
            [else
             (define-values (mask valid) (mask-and-valid num))
             (when (and valid (> mask 0))
               (for ([m (in-range (- maxMask 1) -1 -1)])
                 (let ((cur (vector-ref dp m)))
                   (when (and (> cur 0) (= (bitwise-and m mask) 0))
                     (define newMask (bitwise-ior m mask))
                     (vector-set! dp newMask
                                  (modulo (+ (vector-ref dp newMask) cur) MOD))))))]))
    ;; sum all dp entries
    (define total 0)
    (for ([val (in-vector dp)])
      (set! total (modulo (+ total val) MOD)))
    ;; pow2 = 2^cnt1 mod MOD
    (define (pow2 exp)
      (let loop ((e exp) (res 1))
        (if (= e 0)
            res
            (loop (- e 1) (modulo (* res 2) MOD)))))
    (define ans (modulo (- (modulo (* total (pow2 cnt1)) MOD) 1) MOD))
    ans))

;; contract
(define/contract (square-free-subsets nums)
  (-> (listof exact-integer?) exact-integer?)
  square-free-subsets)
```

## Erlang

```erlang
-module(solution).
-export([square_free_subsets/1]).

-define(MOD, 1000000007).

square_free_subsets(Nums) ->
    {Masks, Ones} = lists:foldl(fun(N, {Mlist, C1}) ->
        case N of
            1 -> {Mlist, C1 + 1};
            _ ->
                {Mask, Valid} = factor_mask(N),
                if Valid -> {[Mask | Mlist], C1};
                   true -> {Mlist, C1}
                end
        end
    end, {[], 0}, Nums),

    DP0 = maps:from_list([{0, 1}]),
    DP = lists:foldl(fun(Mask, DPPrev) ->
            maps:fold(
                fun(PrevMask, Cnt, Acc) ->
                    case (PrevMask band Mask) of
                        0 ->
                            NewMask = PrevMask bor Mask,
                            Old = maps:get(NewMask, Acc, 0),
                            Updated = (Old + Cnt) rem ?MOD,
                            maps:put(NewMask, Updated, Acc);
                        _ -> Acc
                    end
                end,
                DPPrev,
                DPPrev)
        end, DP0, Masks),

    SumAll = maps:fold(fun(_M, C, A) -> (A + C) rem ?MOD end, 0, DP),
    Pow2 = pow_mod(2, Ones, ?MOD),
    ResTmp = ((SumAll * Pow2) rem ?MOD - 1) rem ?MOD,
    if ResTmp < 0 -> ResTmp + ?MOD; true -> ResTmp end.

factor_mask(N) ->
    PrimeList = [2,3,5,7,11,13,17,19,23,29],
    factor_mask(N, PrimeList, 0, 0).

factor_mask(Num, [], _Idx, Mask) ->
    {Mask, true};
factor_mask(Num, [P | Rest], Idx, Mask) ->
    case Num rem P of
        0 ->
            {Exp, NewNum} = count_exp(Num, P, 0),
            if Exp > 1 -> {0, false};
               Exp == 1 -> factor_mask(NewNum, Rest, Idx + 1,
                                      Mask bor (1 bsl Idx));
               true -> factor_mask(NewNum, Rest, Idx + 1, Mask)
            end;
        _ ->
            factor_mask(Num, Rest, Idx + 1, Mask)
    end.

count_exp(N, P, Cnt) when N rem P =:= 0 ->
    count_exp(N div P, P, Cnt + 1);
count_exp(N, _P, Cnt) ->
    {Cnt, N}.

pow_mod(_Base, 0, _Mod) -> 1;
pow_mod(Base, Exp, Mod) when (Exp band 1) =:= 1 ->
    (Base * pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod)) rem Mod;
pow_mod(Base, Exp, Mod) ->
    pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @mod 1_000_000_007
  @primes [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

  @spec square_free_subsets(nums :: [integer]) :: integer
  def square_free_subsets(nums) do
    cnt1 = Enum.count(nums, fn x -> x == 1 end)

    max_mask = 1 <<< length(@primes)
    dp = :array.from_list(List.duplicate(0, max_mask)) |> :array.set(0, 1)

    dp =
      Enum.reduce(nums, dp, fn num, acc_dp ->
        cond do
          num == 1 ->
            acc_dp

          true ->
            {mask_num, valid} = get_mask(num)

            if not valid do
              acc_dp
            else
              new_dp = acc_dp

              for m <- 0..(max_mask - 1) do
                val = :array.get(m, acc_dp)

                if val != 0 and (band(m, mask_num) == 0) do
                  idx = bor(m, mask_num)
                  cur = :array.get(idx, new_dp)
                  updated = rem(cur + val, @mod)
                  new_dp = :array.set(idx, updated, new_dp)
                end
              end

              new_dp
            end
        end
      end)

    total =
      Enum.reduce(0..(max_mask - 1), 0, fn m, sum ->
        rem(sum + :array.get(m, dp), @mod)
      end)

    pow2 = mod_pow(2, cnt1)
    ans = rem(total * pow2 - 1, @mod)
    if ans < 0, do: ans + @mod, else: ans
  end

  defp get_mask(num) do
    {mask, ok, rest} =
      Enum.reduce_while(Enum.with_index(@primes), {0, true, num}, fn {p, i},
                                                                   {m, _ok, cur} ->
        if cur == 1 do
          {:cont, {m, true, cur}}
        else
          {cnt, rem_val} = count_factor(cur, p)

          if cnt > 1 do
            {:halt, {m, false, rem_val}}
          else
            new_mask = if cnt == 1, do: bor(m, 1 <<< i), else: m
            {:cont, {new_mask, true, rem_val}}
          end
        end
      end)

    {mask, ok and rest == 1}
  end

  defp count_factor(num, p) do
    if rem(num, p) == 0 do
      {cnt, rest} = count_factor(div(num, p), p)
      {cnt + 1, rest}
    else
      {0, num}
    end
  end

  defp mod_pow(base, exp) when exp >= 0 do
    mod_pow(base, exp, 1)
  end

  defp mod_pow(_base, 0, acc), do: acc

  defp mod_pow(base, exp, acc) do
    if exp == 0 do
      acc
    else
      acc = if band(exp, 1) == 1, do: rem(acc * base, @mod), else: acc
      mod_pow(rem(base * base, @mod), div(exp, 2), acc)
    end
  end
end
```

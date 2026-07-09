# 3428. Maximum and Minimum Sums of at Most Size K Subsequences

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    long long modpow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    int minMaxSums(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<long long> fact(n + 1), invFact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = modpow(fact[n], MOD - 2);
        for (int i = n; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;

        auto C = [&](int N, int R) -> long long {
            if (R < 0 || R > N) return 0;
            return fact[N] * invFact[R] % MOD * invFact[N - R] % MOD;
        };

        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long cntMax = 0, cntMin = 0;
            int limitLeft = min(k - 1, i);
            for (int t = 0; t <= limitLeft; ++t) {
                cntMax += C(i, t);
                if (cntMax >= MOD) cntMax -= MOD;
            }
            int right = n - 1 - i;
            int limitRight = min(k - 1, right);
            for (int t = 0; t <= limitRight; ++t) {
                cntMin += C(right, t);
                if (cntMin >= MOD) cntMin -= MOD;
            }
            long long totalCnt = cntMax + cntMin;
            if (totalCnt >= MOD) totalCnt -= MOD;
            ans = (ans + (long long)nums[i] % MOD * totalCnt) % MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    public int minMaxSums(int[] nums, int k) {
        int n = nums.length;
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }

        long ans = 0;
        int limitK = k - 1;

        for (int i = 0; i < n; i++) {
            // count as maximum
            long cntMax = 0;
            int maxT = Math.min(limitK, i);
            for (int t = 0; t <= maxT; t++) {
                cntMax += nCr(i, t, fact, invFact);
                if (cntMax >= MOD) cntMax -= MOD;
            }

            // count as minimum
            int right = n - 1 - i;
            long cntMin = 0;
            int minT = Math.min(limitK, right);
            for (int t = 0; t <= minT; t++) {
                cntMin += nCr(right, t, fact, invFact);
                if (cntMin >= MOD) cntMin -= MOD;
            }

            long totalCnt = cntMax + cntMin;
            if (totalCnt >= MOD) totalCnt -= MOD;

            long contrib = totalCnt * (nums[i] % MOD) % MOD;
            ans += contrib;
            if (ans >= MOD) ans -= MOD;
        }
        return (int) ans;
    }

    private static long nCr(int n, int r, long[] fact, long[] invFact) {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    }

    private static long modPow(long base, long exp) {
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
    def minMaxSums(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        # factorials and inverse factorials
        fac = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = fac[i - 1] * i % MOD
        invfac = [1] * (n + 1)
        invfac[n] = pow(fac[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfac[i - 1] = invfac[i] * i % MOD

        def comb(N, R):
            if R < 0 or R > N:
                return 0
            return fac[N] * invfac[R] % MOD * invfac[N - R] % MOD

        max_choose = k - 1
        total = 0
        for i, val in enumerate(nums):
            # count subsets where nums[i] is the maximum
            cnt_max = 0
            limit = min(max_choose, i)
            for t in range(limit + 1):
                cnt_max += comb(i, t)
            # count subsets where nums[i] is the minimum
            right = n - 1 - i
            cnt_min = 0
            limit2 = min(max_choose, right)
            for t in range(limit2 + 1):
                cnt_min += comb(right, t)

            contrib = (cnt_max + cnt_min) % MOD
            total = (total + (val % MOD) * contrib) % MOD

        return total
```

## Python3

```python
import sys
from typing import List

MOD = 10**9 + 7

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        # precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(nn: int, r: int) -> int:
            if r < 0 or r > nn:
                return 0
            return fact[nn] * inv_fact[r] % MOD * inv_fact[nn - r] % MOD

        ans = 0
        max_choose = k - 1
        for i, val in enumerate(nums):
            cnt_max = 0
            limit = min(max_choose, i)
            for s in range(limit + 1):
                cnt_max += comb(i, s)
            cnt_max %= MOD

            cnt_min = 0
            right = n - 1 - i
            limit = min(max_choose, right)
            for s in range(limit + 1):
                cnt_min += comb(right, s)
            cnt_min %= MOD

            total_cnt = (cnt_max + cnt_min) % MOD
            ans = (ans + (val % MOD) * total_cnt) % MOD

        return ans
```

## C

```c
#include <stdlib.h>
#include <stdint.h>

static const int MOD = 1000000007;

static long long modpow(long long a, long long e) {
    long long res = 1;
    while (e) {
        if (e & 1) res = res * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return res;
}

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int minMaxSums(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);

    int n = numsSize;
    long long *fact = (long long *)malloc((n + 1) * sizeof(long long));
    long long *invFact = (long long *)malloc((n + 1) * sizeof(long long));

    fact[0] = 1;
    for (int i = 1; i <= n; ++i)
        fact[i] = fact[i - 1] * i % MOD;

    invFact[n] = modpow(fact[n], MOD - 2);
    for (int i = n; i > 0; --i)
        invFact[i - 1] = invFact[i] * i % MOD;

    auto C = [&](int N, int R) -> long long {
        if (R < 0 || R > N) return 0;
        return fact[N] * invFact[R] % MOD * invFact[N - R] % MOD;
    };

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        long long sumMax = 0, sumMin = 0;
        int limitLeft = k - 1;
        if (limitLeft > i) limitLeft = i;
        for (int t = 0; t <= limitLeft; ++t) {
            sumMax += C(i, t);
            if (sumMax >= MOD) sumMax -= MOD;
        }
        int rightCnt = n - 1 - i;
        int limitRight = k - 1;
        if (limitRight > rightCnt) limitRight = rightCnt;
        for (int t = 0; t <= limitRight; ++t) {
            sumMin += C(rightCnt, t);
            if (sumMin >= MOD) sumMin -= MOD;
        }
        long long totalCnt = (sumMax + sumMin) % MOD;
        ans = (ans + totalCnt * (nums[i] % MOD)) % MOD;
    }

    free(fact);
    free(invFact);
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    public int MinMaxSums(int[] nums, int k) {
        int n = nums.Length;
        Array.Sort(nums);
        // comb[i][r] = C(i, r) for i up to n and r up to k
        long[,] comb = new long[n + 1, k + 1];
        for (int i = 0; i <= n; i++) {
            comb[i, 0] = 1;
        }
        for (int i = 1; i <= n; i++) {
            int up = Math.Min(i, k);
            for (int r = 1; r <= up; r++) {
                comb[i, r] = (comb[i - 1, r] + comb[i - 1, r - 1]) % MOD;
            }
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            // ways where nums[i] is the maximum
            int limitMax = Math.Min(i, k - 1);
            long maxWays = 0;
            for (int t = 0; t <= limitMax; t++) {
                maxWays += comb[i, t];
            }
            maxWays %= MOD;

            // ways where nums[i] is the minimum
            int remaining = n - i - 1;
            int limitMin = Math.Min(remaining, k - 1);
            long minWays = 0;
            for (int t = 0; t <= limitMin; t++) {
                minWays += comb[remaining, t];
            }
            minWays %= MOD;

            long totalWays = (maxWays + minWays) % MOD;
            ans = (ans + ((long)nums[i] % MOD) * totalWays) % MOD;
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minMaxSums = function(nums, k) {
    const MOD = 1000000007n;
    const n = nums.length;
    nums.sort((a, b) => a - b);
    
    // factorials and inverse factorials
    const fact = new Array(n + 1);
    const invFact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    const modPow = (base, exp) => {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    };
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const comb = (nn, rr) => {
        if (rr < 0 || rr > nn) return 0n;
        return (((fact[nn] * invFact[rr]) % MOD) * invFact[nn - rr]) % MOD;
    };
    
    let ans = 0n;
    const maxT = k - 1;
    for (let i = 0; i < n; ++i) {
        let maxSum = 0n;
        const limitMax = Math.min(maxT, i);
        for (let t = 0; t <= limitMax; ++t) {
            maxSum += comb(i, t);
        }
        maxSum %= MOD;
        
        let minSum = 0n;
        const right = n - 1 - i;
        const limitMin = Math.min(maxT, right);
        for (let t = 0; t <= limitMin; ++t) {
            minSum += comb(right, t);
        }
        minSum %= MOD;
        
        const totalCnt = (maxSum + minSum) % MOD;
        ans = (ans + (BigInt(nums[i]) % MOD) * totalCnt) % MOD;
    }
    
    return Number(ans);
};
```

## Typescript

```typescript
function minMaxSums(nums: number[], k: number): number {
    const MOD = 1000000007n;
    const n = nums.length;

    // precompute factorials and inverse factorials
    const fact: bigint[] = new Array(n + 1);
    const invFact: bigint[] = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; ++i) {
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
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i > 0; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const comb = (nn: number, rr: number): bigint => {
        if (rr < 0 || rr > nn) return 0n;
        return (((fact[nn] * invFact[rr]) % MOD) * invFact[nn - rr]) % MOD;
    };

    let total = 0n;
    const limit = k - 1; // max number of other elements besides the chosen one
    for (let i = 0; i < n; ++i) {
        let cntMax = 0n;
        const maxT = Math.min(limit, i);
        for (let t = 0; t <= maxT; ++t) {
            cntMax += comb(i, t);
        }
        let cntMin = 0n;
        const right = n - 1 - i;
        const minT = Math.min(limit, right);
        for (let t = 0; t <= minT; ++t) {
            cntMin += comb(right, t);
        }
        const contrib = (BigInt(nums[i]) % MOD) * ((cntMax + cntMin) % MOD) % MOD;
        total = (total + contrib) % MOD;
    }

    return Number(total);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minMaxSums($nums, $k) {
        $mod = 1000000007;
        $n = count($nums);
        sort($nums, SORT_NUMERIC);

        // factorials
        $fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) {
            $fact[$i] = ($fact[$i - 1] * $i) % $mod;
        }

        // inverse factorials
        $invFact = array_fill(0, $n + 1, 1);
        $invFact[$n] = $this->powMod($fact[$n], $mod - 2, $mod);
        for ($i = $n; $i > 0; $i--) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % $mod;
        }

        // combination function using closures to capture arrays
        $comb = function($nn, $rr) use (&$fact, &$invFact, $mod) {
            if ($rr < 0 || $rr > $nn) return 0;
            $res = $fact[$nn];
            $res = ($res * $invFact[$rr]) % $mod;
            $res = ($res * $invFact[$nn - $rr]) % $mod;
            return $res;
        };

        $total = 0;
        for ($i = 0; $i < $n; $i++) {
            // count as maximum
            $maxCnt = 0;
            $limitMax = min($k - 1, $i);
            for ($t = 0; $t <= $limitMax; $t++) {
                $maxCnt += $comb($i, $t);
                if ($maxCnt >= $mod) $maxCnt -= $mod;
            }

            // count as minimum
            $right = $n - 1 - $i;
            $minCnt = 0;
            $limitMin = min($k - 1, $right);
            for ($t = 0; $t <= $limitMin; $t++) {
                $minCnt += $comb($right, $t);
                if ($minCnt >= $mod) $minCnt -= $mod;
            }

            $cnt = $maxCnt + $minCnt;
            if ($cnt >= $mod) $cnt -= $mod;

            $valMod = $nums[$i] % $mod;
            $total = ($total + ($cnt * $valMod) % $mod) % $mod;
        }

        return (int)$total;
    }

    private function powMod($base, $exp, $mod) {
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
    private let MOD = 1_000_000_007

    func minMaxSums(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        let sorted = nums.sorted()
        // factorials
        var fact = [Int](repeating: 0, count: n + 1)
        var invFact = [Int](repeating: 0, count: n + 1)
        fact[0] = 1
        for i in 1...n {
            fact[i] = Int((Int64(fact[i - 1]) * Int64(i)) % Int64(MOD))
        }
        invFact[n] = modPow(fact[n], MOD - 2)
        if n > 0 {
            for i in stride(from: n, to: 0, by: -1) {
                invFact[i - 1] = Int((Int64(invFact[i]) * Int64(i)) % Int64(MOD))
            }
        }

        func comb(_ nn: Int, _ r: Int) -> Int {
            if r < 0 || r > nn { return 0 }
            let res = Int64(fact[nn])
                * Int64(invFact[r]) % Int64(MOD)
                * Int64(invFact[nn - r]) % Int64(MOD)
            return Int(res)
        }

        var answer: Int64 = 0
        for i in 0..<n {
            let v = Int64(sorted[i])
            // count as maximum
            var cntMax = 0
            let limitMax = min(k - 1, i)
            if limitMax >= 0 {
                for t in 0...limitMax {
                    cntMax += comb(i, t)
                    if cntMax >= MOD { cntMax -= MOD }
                }
            }
            // count as minimum
            var cntMin = 0
            let right = n - 1 - i
            let limitMin = min(k - 1, right)
            if limitMin >= 0 {
                for t in 0...limitMin {
                    cntMin += comb(right, t)
                    if cntMin >= MOD { cntMin -= MOD }
                }
            }
            var totalCnt = cntMax + cntMin
            if totalCnt >= MOD { totalCnt -= MOD }
            answer = (answer + v * Int64(totalCnt)) % Int64(MOD)
        }
        return Int(answer)
    }

    private func modPow(_ base: Int, _ exp: Int) -> Int {
        var result: Int64 = 1
        var b: Int64 = Int64(base % MOD)
        var e = exp
        let m = Int64(MOD)
        while e > 0 {
            if e & 1 == 1 {
                result = (result * b) % m
            }
            b = (b * b) % m
            e >>= 1
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
import java.util.Arrays
import kotlin.math.min

class Solution {
    fun minMaxSums(nums: IntArray, k: Int): Int {
        val MOD = 1_000_000_007L
        val n = nums.size
        val sorted = nums.clone()
        Arrays.sort(sorted)

        // sumComb[i] = sum_{t=0}^{min(k-1,i)} C(i, t) mod MOD
        val sumComb = LongArray(n + 1)
        var prev = LongArray(k) { 0L }
        var cur = LongArray(k) { 0L }

        prev[0] = 1L
        sumComb[0] = 1L

        for (i in 1..n) {
            Arrays.fill(cur, 0L)
            cur[0] = 1L
            val upto = min(i, k - 1)
            for (j in 1..upto) {
                var v = prev[j - 1]
                if (j <= i - 1) {
                    v += prev[j]
                }
                cur[j] = v % MOD
            }
            var s = 0L
            for (j in 0..upto) {
                s += cur[j]
                if (s >= MOD) s -= MOD
            }
            sumComb[i] = s
            val tmp = prev
            prev = cur
            cur = tmp
        }

        var ans = 0L
        for (i in 0 until n) {
            val left = i
            val right = n - 1 - i
            val cnt = (sumComb[left] + sumComb[right]) % MOD
            ans = (ans + cnt * (sorted[i].toLong() % MOD)) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int minMaxSums(List<int> nums, int k) {
    nums.sort();
    int n = nums.length;
    if (k == 1) {
      int ans = 0;
      for (int v in nums) {
        int val = v % _mod;
        ans = (ans + (val * 2) % _mod) % _mod;
      }
      return ans;
    }

    int maxT = k - 2; // maximum t in C(d, t)
    int lenF = n > 1 ? n - 1 : 0; // we need f[0..n-2]
    List<int> f = List.filled(lenF, 0);
    List<int> binom = List.filled(maxT + 1, 0);
    binom[0] = 1;

    for (int d = 0; d <= n - 2; ++d) {
      int sum = 0;
      for (int t = 0; t <= maxT; ++t) {
        sum += binom[t];
        if (sum >= _mod) sum -= _mod;
      }
      f[d] = sum;

      // update binom for next d+1
      int limit = d + 1;
      if (limit > maxT) limit = maxT;
      for (int t = limit; t >= 1; --t) {
        binom[t] = (binom[t] + binom[t - 1]) % _mod;
      }
    }

    List<int> pref = List.filled(lenF, 0);
    if (lenF > 0) {
      pref[0] = f[0];
      for (int i = 1; i < lenF; ++i) {
        pref[i] = (pref[i - 1] + f[i]) % _mod;
      }
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int cntMin = 1;
      int remaining = n - i - 2;
      if (remaining >= 0) {
        cntMin = (cntMin + pref[remaining]) % _mod;
      }

      int cntMax = 1;
      int left = i - 1;
      if (left >= 0) {
        cntMax = (cntMax + pref[left]) % _mod;
      }

      int totalCnt = cntMin + cntMax;
      if (totalCnt >= _mod) totalCnt -= _mod;

      int val = nums[i] % _mod;
      ans = (ans + (val * totalCnt) % _mod) % _mod;
    }
    return ans;
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
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD
		}
		a = a * a % MOD
		e >>= 1
	}
	return res
}

func minMaxSums(nums []int, k int) int {
	n := len(nums)
	sort.Ints(nums)

	fact := make([]int64, n+1)
	invFact := make([]int64, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[n] = modPow(fact[n], MOD-2)
	for i := n - 1; i >= 0; i-- {
		invFact[i] = invFact[i+1] * int64(i+1) % MOD
	}

	comb := func(nn, rr int) int64 {
		if rr < 0 || rr > nn {
			return 0
		}
		return fact[nn] * invFact[rr] % MOD * invFact[nn-rr] % MOD
	}

	var ans int64 = 0
	km1 := k - 1
	for i := 0; i < n; i++ {
		limitMax := km1
		if limitMax > i {
			limitMax = i
		}
		var cntMax int64 = 0
		for t := 0; t <= limitMax; t++ {
			cntMax += comb(i, t)
		}
		right := n - 1 - i
		limitMin := km1
		if limitMin > right {
			limitMin = right
		}
		var cntMin int64 = 0
		for t := 0; t <= limitMin; t++ {
			cntMin += comb(right, t)
		}
		totalCnt := (cntMax + cntMin) % MOD
		ans = (ans + int64(nums[i])%MOD*totalCnt) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def min_max_sums(nums, k)
  mod = 1_000_000_007
  n = nums.length
  nums.sort!
  return 0 if n == 0

  # precompute factorials and inverse factorials
  fact = Array.new(n + 1, 1)
  (1..n).each { |i| fact[i] = fact[i - 1] * i % mod }
  inv_fact = Array.new(n + 1, 1)
  pow = ->(a, e) {
    res = 1
    while e > 0
      res = res * a % mod if (e & 1) == 1
      a = a * a % mod
      e >>= 1
    end
    res
  }
  inv_fact[n] = pow.call(fact[n], mod - 2)
  n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % mod }

  comb = ->(m, r) {
    return 0 if r < 0 || r > m
    fact[m] * inv_fact[r] % mod * inv_fact[m - r] % mod
  }

  k_limit = k - 2
  f = []
  if n >= 2 && k_limit >= 0
    (0..n - 2).each do |m|
      limit = m < k_limit ? m : k_limit
      sum = 0
      (0..limit).each { |t| sum = (sum + comb.call(m, t)) % mod }
      f[m] = sum
    end
  else
    # all zeros when k <= 1
    f = Array.new(n - 1, 0) if n >= 2
  end

  pref = []
  if n >= 2
    pref[0] = f[0]
    (1..n - 2).each { |i| pref[i] = (pref[i - 1] + f[i]) % mod }
  end

  total = 0
  (0...n).each do |i|
    len_right = n - 1 - i
    a_cnt = if len_right == 0
              1
            else
              (1 + pref[len_right - 1]) % mod
            end
    b_cnt = if i == 0
              1
            else
              (1 + pref[i - 1]) % mod
            end
    cnt_sum = (a_cnt + b_cnt) % mod
    total = (total + nums[i] % mod * cnt_sum) % mod
  end

  total % mod
end
```

## Scala

```scala
object Solution {
    def minMaxSums(nums: Array[Int], k: Int): Int = {
        val MOD = 1000000007L
        val n = nums.length
        val arr = nums.sorted.map(_.toLong)

        // factorials and inverse factorials
        val fact = new Array[Long](n + 1)
        val invFact = new Array[Long](n + 1)
        fact(0) = 1L
        var i = 1
        while (i <= n) {
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
        invFact(n) = modPow(fact(n), MOD - 2)
        i = n
        while (i >= 1) {
            invFact(i - 1) = invFact(i) * i % MOD
            i -= 1
        }

        def C(nn: Int, rr: Int): Long = {
            if (rr < 0 || rr > nn) 0L
            else fact(nn) * invFact(rr) % MOD * invFact(nn - rr) % MOD
        }

        var ans = 0L
        i = 0
        while (i < n) {
            var cntMax = 0L
            val limitMax = math.min(k - 1, i)
            var t = 0
            while (t <= limitMax) {
                cntMax += C(i, t)
                if (cntMax >= MOD) cntMax -= MOD
                t += 1
            }

            var cntMin = 0L
            val after = n - 1 - i
            val limitMin = math.min(k - 1, after)
            t = 0
            while (t <= limitMin) {
                cntMin += C(after, t)
                if (cntMin >= MOD) cntMin -= MOD
                t += 1
            }

            val totalCnt = (cntMax + cntMin) % MOD
            ans = (ans + arr(i) % MOD * totalCnt) % MOD

            i += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_max_sums(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut a: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        a.sort_unstable();

        // factorials
        let mut fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        // inverse factorials
        fn mod_pow(mut base: i64, mut exp: i64, m: i64) -> i64 {
            let mut res = 1i64;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = res * base % m;
                }
                base = base * base % m;
                exp >>= 1;
            }
            res
        }
        let mut inv_fact = vec![1i64; n + 1];
        inv_fact[n] = mod_pow(fact[n], MOD - 2, MOD);
        for i in (1..=n).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }
        let comb = |nn: usize, rr: usize, fact: &Vec<i64>, inv_fact: &Vec<i64>| -> i64 {
            if rr > nn {
                0
            } else {
                fact[nn] * inv_fact[rr] % MOD * inv_fact[nn - rr] % MOD
            }
        };

        let kk = k as usize;
        let mut ans: i64 = 0;
        for i in 0..n {
            // count as minimum
            let mut cnt_min: i64 = 0;
            let right = n - 1 - i;
            for t in 0..kk {
                if t <= right {
                    cnt_min += comb(right, t, &fact, &inv_fact);
                    if cnt_min >= MOD {
                        cnt_min -= MOD;
                    }
                } else {
                    break;
                }
            }
            // count as maximum
            let mut cnt_max: i64 = 0;
            for t in 0..kk {
                if t <= i {
                    cnt_max += comb(i, t, &fact, &inv_fact);
                    if cnt_max >= MOD {
                        cnt_max -= MOD;
                    }
                } else {
                    break;
                }
            }
            let total_cnt = (cnt_min + cnt_max) % MOD;
            ans = (ans + a[i] % MOD * total_cnt) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (min-max-sums nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (sorted-vec (list->vector (sort nums <)))
         (K (- k 1))) ; maximum t = k-1
    ;; precompute binomial coefficients C(i, r) for i up to n and r up to K
    (define comb (make-vector (+ n 1) #f))
    (for ([i (in-range (+ n 1))])
      (let ((row (make-vector (+ K 1) 0)))
        (vector-set! row 0 1)
        (when (> i 0)
          (let ((prev (vector-ref comb (- i 1))))
            (for ([r (in-range 1 (add1 (min i K)))])
              (let* ((val (+ (vector-ref prev r)
                             (vector-ref prev (- r 1)))))
                (vector-set! row r (modulo val MOD))))))
        (vector-set! comb i row)))
    ;; accumulate answer
    (let ((ans 0))
      (for ([idx (in-range n)])
        (let* ((v (vector-ref sorted-vec idx))
               (left idx)                     ; number of smaller elements
               (right (- n idx 1))            ; number of larger elements
               (row-left (vector-ref comb left))
               (row-right (vector-ref comb right))
               (sum-min 0)
               (sum-max 0))
          ;; sum_{t=0}^{K} C(right, t)
          (for ([t (in-range (add1 K))])
            (when (<= t right)
              (set! sum-min (+ sum-min (vector-ref row-right t)))))
          ;; sum_{t=0}^{K} C(left, t)
          (for ([t (in-range (add1 K))])
            (when (<= t left)
              (set! sum-max (+ sum-max (vector-ref row-left t)))))
          (set! ans (modulo (+ ans (* v (+ sum-min sum-max))) MOD))))
      ans)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec min_max_sums(Nums :: [integer()], K :: integer()) -> integer().
min_max_sums(Nums, K) ->
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    Prefs = build_prefs(N, K),
    compute_total(Sorted, Prefs, N).

%% Build list Prefs where Prefs[M] = sum_{t=0}^{K-1} C(M,t) mod MOD
build_prefs(N, K) ->
    EmptyPrev = erlang:make_tuple(K + 1, 0),
    build_loop(0, N, EmptyPrev, [], K).

build_loop(I, N, Prev, Acc, K) when I =< N ->
    Curr = compute_curr(Prev, K),
    Sum = sum_first_k(Curr, K - 1),
    build_loop(I + 1, N, Curr, [Sum | Acc], K);
build_loop(_, _, _, Acc, _) ->
    lists:reverse(Acc).

%% Compute current row of binomial coefficients C(i, t) for t=0..K
compute_curr(Prev, K) ->
    List = [if T == 0 -> 1;
               true -> (element(T, Prev) + element(T - 1, Prev)) rem ?MOD
            end || T <- lists:seq(0, K)],
    erlang:list_to_tuple(List).

%% Sum C(i,t) for t=0..MaxIdx
sum_first_k(_Tuple, MaxIdx) when MaxIdx < 0 -> 0;
sum_first_k(Tuple, MaxIdx) ->
    sum_first_k(Tuple, MaxIdx, 0, 0).

sum_first_k(_Tuple, MaxIdx, Idx, Acc) when Idx > MaxIdx ->
    Acc rem ?MOD;
sum_first_k(Tuple, MaxIdx, Idx, Acc) ->
    Val = element(Idx + 1, Tuple),
    sum_first_k(Tuple, MaxIdx, Idx + 1, (Acc + Val) rem ?MOD).

%% Compute final answer using Prefs
compute_total(List, Prefs, N) ->
    compute_total(List, Prefs, 0, N, 0).

compute_total([], _Prefs, _Idx, _N, Acc) ->
    Acc rem ?MOD;
compute_total([H | T], Prefs, Idx, N, Acc) ->
    After = N - Idx - 1,
    CntMin = nth_elem(After, Prefs),
    CntMax = nth_elem(Idx, Prefs),
    TotalCnt = (CntMin + CntMax) rem ?MOD,
    Contribution = ((H rem ?MOD) * TotalCnt) rem ?MOD,
    NewAcc = (Acc + Contribution) rem ?MOD,
    compute_total(T, Prefs, Idx + 1, N, NewAcc).

nth_elem(I, List) ->
    lists:nth(I + 1, List).
```

## Elixir

```elixir
defmodule Solution do
  @modulus 1_000_000_007
  require Bitwise

  @spec min_max_sums(nums :: [integer], k :: integer) :: integer
  def min_max_sums(nums, k) do
    sorted = Enum.sort(nums)
    n = length(sorted)

    inv = precompute_inverses(k, @modulus)

    Enum.with_index(sorted)
    |> Enum.reduce(0, fn {val, i}, acc ->
      max_cnt = count_subsets(i, k - 1, inv)
      min_cnt = count_subsets(n - 1 - i, k - 1, inv)
      contrib = rem(val * (max_cnt + min_cnt), @modulus)
      rem(acc + contrib, @modulus)
    end)
  end

  defp precompute_inverses(k, mod) do
    Enum.reduce(1..k, [0], fn i, acc ->
      inv_i = mod_pow(i, mod - 2, mod)
      acc ++ [inv_i]
    end)
  end

  defp count_subsets(m, limit, inv) do
    max_s = min(limit, m)

    if max_s < 0 do
      0
    else
      {sum, _c} =
        Enum.reduce(0..max_s, {0, 1}, fn s, {sum_acc, c} ->
          new_sum = rem(sum_acc + c, @modulus)

          if s == max_s do
            {new_sum, c}
          else
            numerator = m - s
            denom_inv = Enum.at(inv, s + 1)
            new_c = rem(rem(c * numerator, @modulus) * denom_inv, @modulus)
            {new_sum, new_c}
          end
        end)

      sum
    end
  end

  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) do
    rec_mod_pow(rem(base, mod), exp, mod, 1)
  end

  defp rec_mod_pow(_base, 0, _mod, acc), do: acc

  defp rec_mod_pow(base, exp, mod, acc) do
    acc = if (exp &&& 1) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    rec_mod_pow(base, exp >>> 1, mod, acc)
  end
end
```

# 3444. Minimum Increments for Target Multiples in an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long lcm_ll(long long a, long long b) {
        if (a == 0 || b == 0) return 0;
        long long g = std::gcd(a, b);
        __int128 mul = (__int128)(a / g) * b;
        if (mul > (long long)4e18) return (long long)4e18; // cap to avoid overflow
        return (long long)mul;
    }
    
    int minimumIncrements(vector<int>& nums, vector<int>& target) {
        int n = nums.size();
        int m = target.size();
        int fullMask = (1 << m) - 1;
        const long long INF = (1LL<<60);
        
        // precompute lcm for each subset of targets
        vector<long long> lcmMask(1 << m, 0);
        for (int mask = 1; mask <= fullMask; ++mask) {
            int b = __builtin_ctz(mask); // least set bit index
            int prev = mask ^ (1 << b);
            if (prev == 0) {
                lcmMask[mask] = target[b];
            } else {
                lcmMask[mask] = lcm_ll(lcmMask[prev], target[b]);
            }
        }
        
        vector<long long> dp(1 << m, INF), ndp;
        dp[0] = 0;
        for (int x : nums) {
            long long val = x;
            // compute cost for each subset
            vector<long long> cost(1 << m, 0);
            for (int mask = 1; mask <= fullMask; ++mask) {
                long long L = lcmMask[mask];
                long long rem = val % L;
                cost[mask] = (rem == 0) ? 0 : (L - rem);
            }
            ndp = dp; // copy for using each element at most once
            for (int prevMask = 0; prevMask <= fullMask; ++prevMask) {
                if (dp[prevMask] == INF) continue;
                for (int sub = 1; sub <= fullMask; ++sub) {
                    int newMask = prevMask | sub;
                    long long cand = dp[prevMask] + cost[sub];
                    if (cand < ndp[newMask]) ndp[newMask] = cand;
                }
            }
            dp.swap(ndp);
        }
        return (int)dp[fullMask];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private long lcm(long a, long b) {
        if (a == 0 || b == 0) return 0;
        return a / gcd(a, b) * b;
    }

    public int minimumIncrements(int[] nums, int[] target) {
        int k = target.length;
        int fullMask = (1 << k) - 1;

        long[] lcmMask = new long[fullMask + 1];
        for (int mask = 1; mask <= fullMask; ++mask) {
            long cur = 1;
            for (int i = 0; i < k; ++i) {
                if ((mask >> i & 1) == 1) {
                    cur = lcm(cur, target[i]);
                }
            }
            lcmMask[mask] = cur;
        }

        long INF = Long.MAX_VALUE / 4;
        long[] dp = new long[fullMask + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int num : nums) {
            long[] cost = new long[fullMask + 1];
            for (int mask = 1; mask <= fullMask; ++mask) {
                long L = lcmMask[mask];
                long n = num;
                long q = (n + L - 1) / L;
                long y = q * L;
                cost[mask] = y - n;
            }

            long[] ndp = dp.clone();
            for (int prev = 0; prev <= fullMask; ++prev) {
                if (dp[prev] == INF) continue;
                for (int sub = 1; sub <= fullMask; ++sub) {
                    int newMask = prev | sub;
                    long val = dp[prev] + cost[sub];
                    if (val < ndp[newMask]) ndp[newMask] = val;
                }
            }
            dp = ndp;
        }

        return (int) dp[fullMask];
    }
}
```

## Python

```python
import math

class Solution(object):
    def minimumIncrements(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        k = len(target)
        full = 1 << k

        # precompute lcm for each subset mask
        lcm_mask = [0] * full
        lcm_mask[0] = 1
        for mask in range(1, full):
            low_bit = mask & -mask
            idx = (low_bit.bit_length() - 1)          # index of the lowest set bit
            prev = mask ^ low_bit
            if prev == 0:
                lcm_mask[mask] = target[idx]
            else:
                a = lcm_mask[prev]
                b = target[idx]
                g = math.gcd(a, b)
                lcm_mask[mask] = a // g * b

        INF = 10 ** 18
        dp = [INF] * full
        dp[0] = 0

        for x in nums:
            # cost to make this number cover each subset
            cost = [0] * full
            for mask in range(1, full):
                L = lcm_mask[mask]
                inc = ((x + L - 1) // L) * L - x
                cost[mask] = inc

            newdp = dp[:]
            for mask in range(full):
                if dp[mask] == INF:
                    continue
                base = dp[mask]
                for sub in range(1, full):
                    nmask = mask | sub
                    val = base + cost[sub]
                    if val < newdp[nmask]:
                        newdp[nmask] = val
            dp = newdp

        return dp[full - 1]
```

## Python3

```python
import math
from typing import List

class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        m = len(target)
        full_mask = (1 << m) - 1

        # precompute lcm for each non-empty subset mask
        lcm_mask = [0] * (1 << m)
        for mask in range(1, 1 << m):
            cur_lcm = 1
            for i in range(m):
                if mask >> i & 1:
                    t = target[i]
                    cur_lcm = cur_lcm // math.gcd(cur_lcm, t) * t
            lcm_mask[mask] = cur_lcm

        INF = 10**20
        dp = [INF] * (1 << m)
        dp[0] = 0

        for num in nums:
            # cost to make this number cover each subset
            cost = [0] * (1 << m)
            for mask in range(1, 1 << m):
                L = lcm_mask[mask]
                r = num % L
                cost[mask] = (L - r) % L

            newdp = dp[:]  # we may also skip this element
            for cur in range(1 << m):
                if dp[cur] == INF:
                    continue
                base = dp[cur]
                for mask in range(1, 1 << m):
                    nxt = cur | mask
                    val = base + cost[mask]
                    if val < newdp[nxt]:
                        newdp[nxt] = val
            dp = newdp

        return dp[full_mask]
```

## C

```c
#include <limits.h>

static long long gcd_ll(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int minimumIncrements(int* nums, int numsSize, int* target, int targetSize) {
    int fullMask = (1 << targetSize) - 1;
    const long long INF = (1LL << 60);
    long long dp[1 << 4];
    for (int m = 0; m <= fullMask; ++m) dp[m] = INF;
    dp[0] = 0;

    /* pre‑compute lcm for every subset of target */
    long long lcmMask[1 << 4];
    lcmMask[0] = 1;
    for (int mask = 1; mask <= fullMask; ++mask) {
        long long cur = 1;
        for (int j = 0; j < targetSize; ++j) {
            if (mask & (1 << j)) {
                long long a = cur;
                long long b = target[j];
                long long g = gcd_ll(a, b);
                cur = a / g * b;
            }
        }
        lcmMask[mask] = cur;
    }

    for (int i = 0; i < numsSize; ++i) {
        long long cost[1 << 4];
        cost[0] = 0;
        long long orig = nums[i];
        for (int mask = 1; mask <= fullMask; ++mask) {
            long long l = lcmMask[mask];
            long long mult = ((orig + l - 1) / l) * l;
            cost[mask] = mult - orig;
        }

        long long newdp[1 << 4];
        for (int m = 0; m <= fullMask; ++m) newdp[m] = dp[m];

        for (int mask = 0; mask <= fullMask; ++mask) {
            if (dp[mask] == INF) continue;
            for (int sub = 1; sub <= fullMask; ++sub) {
                int nmask = mask | sub;
                long long val = dp[mask] + cost[sub];
                if (val < newdp[nmask]) newdp[nmask] = val;
            }
        }

        for (int m = 0; m <= fullMask; ++m) dp[m] = newdp[m];
    }

    return (int)dp[fullMask];
}
```

## Csharp

```csharp
using System;
using System.Numerics;

public class Solution {
    private static long Gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int MinimumIncrements(int[] nums, int[] target) {
        int n = nums.Length;
        int k = target.Length;
        int fullMask = (1 << k) - 1;

        // Precompute LCM for every subset of target
        long[] lcm = new long[1 << k];
        lcm[0] = 1;
        for (int mask = 1; mask <= fullMask; mask++) {
            int bit = BitOperations.TrailingZeroCount(mask);
            int prev = mask ^ (1 << bit);
            long a = lcm[prev];
            long b = target[bit];
            long g = Gcd(a, b);
            lcm[mask] = a / g * b;
        }

        // Cost[i, subMask]: increments needed for nums[i] to become multiple of LCM(subMask)
        long[,] cost = new long[n, fullMask + 1];
        for (int i = 0; i < n; i++) {
            long cur = nums[i];
            for (int mask = 1; mask <= fullMask; mask++) {
                long L = lcm[mask];
                long inc = ((cur + L - 1) / L) * L - cur;
                cost[i, mask] = inc;
            }
        }

        const long INF = (long)4e18;
        long[] dp = new long[1 << k];
        for (int i = 0; i < dp.Length; i++) dp[i] = INF;
        dp[0] = 0;

        // DP over elements, each used at most once
        for (int i = 0; i < n; i++) {
            long[] ndp = new long[1 << k];
            Array.Copy(dp, ndp, dp.Length);
            for (int maskPrev = 0; maskPrev <= fullMask; maskPrev++) {
                if (dp[maskPrev] == INF) continue;
                int remaining = fullMask ^ maskPrev;
                // iterate over non‑empty subsets of remaining bits
                for (int sub = remaining; sub > 0; sub = (sub - 1) & remaining) {
                    long newCost = dp[maskPrev] + cost[i, sub];
                    int newMask = maskPrev | sub;
                    if (newCost < ndp[newMask]) ndp[newMask] = newCost;
                }
            }
            dp = ndp;
        }

        return (int)dp[fullMask];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} target
 * @return {number}
 */
var minimumIncrements = function(nums, target) {
    const m = target.length;
    const fullMask = (1 << m) - 1;

    // gcd and lcm helpers
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const lcm = (a, b) => a / gcd(a, b) * b;

    // precompute lcm for each mask
    const lcmMask = new Array(1 << m).fill(1);
    for (let mask = 1; mask <= fullMask; ++mask) {
        const lowBit = mask & -mask;
        const idx = Math.log2(lowBit) | 0; // index of the target element
        const prev = mask ^ lowBit;
        if (prev === 0) {
            lcmMask[mask] = target[idx];
        } else {
            lcmMask[mask] = lcm(lcmMask[prev], target[idx]);
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    let dp = new Array(1 << m).fill(INF);
    dp[0] = 0;

    for (const num of nums) {
        // cost to make this number a multiple of each mask's lcm
        const cost = new Array(1 << m);
        cost[0] = 0;
        for (let mask = 1; mask <= fullMask; ++mask) {
            const L = lcmMask[mask];
            const inc = Math.floor((num + L - 1) / L) * L - num;
            cost[mask] = inc;
        }

        const prevDP = dp.slice();
        for (let pm = 0; pm <= fullMask; ++pm) {
            if (prevDP[pm] === INF) continue;
            for (let sm = 1; sm <= fullMask; ++sm) {
                const newMask = pm | sm;
                const val = prevDP[pm] + cost[sm];
                if (val < dp[newMask]) dp[newMask] = val;
            }
        }
    }

    return dp[fullMask];
};
```

## Typescript

```typescript
function minimumIncrements(nums: number[], target: number[]): number {
    const m = target.length;
    const fullMask = 1 << m;

    function gcd(a: bigint, b: bigint): bigint {
        while (b !== 0n) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    // pre‑compute lcm for every non‑empty subset of target
    const lcmArr = new Array(fullMask).fill(0n);
    for (let mask = 1; mask < fullMask; ++mask) {
        let cur = 1n;
        for (let i = 0; i < m; ++i) {
            if ((mask >> i) & 1) {
                const t = BigInt(target[i]);
                const g = gcd(cur, t);
                cur = (cur / g) * t;
            }
        }
        lcmArr[mask] = cur;
    }

    const INF = 1n << 200n; // sufficiently large
    let dp: bigint[] = new Array(fullMask).fill(INF);
    dp[0] = 0n;

    for (const num of nums) {
        const x = BigInt(num);
        const cost = new Array(fullMask).fill(0n);
        for (let mask = 1; mask < fullMask; ++mask) {
            const L = lcmArr[mask];
            const rem = x % L;
            cost[mask] = (L - rem) % L;
        }

        const ndp = dp.slice();
        for (let curMask = 0; curMask < fullMask; ++curMask) {
            if (dp[curMask] === INF) continue;
            const remaining = (~curMask) & (fullMask - 1);
            // iterate over all non‑empty submasks of remaining
            for (let sub = remaining; sub > 0; sub = (sub - 1) & remaining) {
                const newMask = curMask | sub;
                const newCost = dp[curMask] + cost[sub];
                if (newCost < ndp[newMask]) ndp[newMask] = newCost;
            }
        }
        dp = ndp;
    }

    return Number(dp[fullMask - 1]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $target
     * @return Integer
     */
    function minimumIncrements($nums, $target) {
        $m = count($target);
        $full = (1 << $m) - 1;

        // precompute lcm for each subset mask
        $lcmMask = array_fill(0, $full + 1, 1);
        for ($mask = 1; $mask <= $full; $mask++) {
            $l = 1;
            for ($i = 0; $i < $m; $i++) {
                if (($mask >> $i) & 1) {
                    $l = $this->lcm($l, $target[$i]);
                }
            }
            $lcmMask[$mask] = $l;
        }

        $INF = PHP_INT_MAX;
        $dp = array_fill(0, $full + 1, $INF);
        $dp[0] = 0;

        foreach ($nums as $x) {
            // cost to make this number a multiple of each subset
            $costs = [];
            for ($sub = 1; $sub <= $full; $sub++) {
                $L = $lcmMask[$sub];
                $k = intdiv($x + $L - 1, $L);
                $costs[$sub] = $k * $L - $x;
            }

            $newdp = $dp; // copy current dp
            for ($mask = 0; $mask <= $full; $mask++) {
                if ($dp[$mask] === $INF) continue;
                foreach ($costs as $sub => $c) {
                    $newMask = $mask | $sub;
                    $val = $dp[$mask] + $c;
                    if ($val < $newdp[$newMask]) {
                        $newdp[$newMask] = $val;
                    }
                }
            }
            $dp = $newdp;
        }

        return $dp[$full];
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }

    private function lcm($a, $b) {
        if ($a == 0 || $b == 0) return 0;
        return intdiv($a, $this->gcd($a, $b)) * $b;
    }
}
```

## Swift

```swift
class Solution {
    func minimumIncrements(_ nums: [Int], _ target: [Int]) -> Int {
        let m = target.count
        let fullMask = 1 << m
        // Precompute LCM for each subset mask
        var lcmMask = [Int64](repeating: 1, count: fullMask)
        func gcd(_ a: Int64, _ b: Int64) -> Int64 {
            var x = a, y = b
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }
        func lcm(_ a: Int64, _ b: Int64) -> Int64 {
            if a == 0 || b == 0 { return 0 }
            return a / gcd(a, b) * b
        }
        for mask in 1..<fullMask {
            var cur: Int64 = 1
            for i in 0..<m where (mask >> i) & 1 == 1 {
                cur = lcm(cur, Int64(target[i]))
            }
            lcmMask[mask] = cur
        }
        let INF = Int64.max / 4
        var dp = [Int64](repeating: INF, count: fullMask)
        dp[0] = 0
        for num in nums {
            let nVal = Int64(num)
            // cost to make this number a multiple of each subset's LCM
            var costForMask = [Int64](repeating: 0, count: fullMask)
            for mask in 1..<fullMask {
                let l = lcmMask[mask]
                let rem = nVal % l
                costForMask[mask] = rem == 0 ? 0 : (l - rem)
            }
            var newDP = dp
            for mask in 0..<fullMask where dp[mask] < INF {
                let base = dp[mask]
                for sub in 1..<fullMask {
                    let newMask = mask | sub
                    let cand = base + costForMask[sub]
                    if cand < newDP[newMask] {
                        newDP[newMask] = cand
                    }
                }
            }
            dp = newDP
        }
        return Int(dp[fullMask - 1])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumIncrements(nums: IntArray, target: IntArray): Int {
        val m = target.size
        val maxMask = 1 shl m
        // Precompute lcm for each subset mask
        val lcmArr = LongArray(maxMask)
        for (mask in 1 until maxMask) {
            var l = 1L
            for (i in 0 until m) {
                if ((mask and (1 shl i)) != 0) {
                    l = lcm(l, target[i].toLong())
                }
            }
            lcmArr[mask] = l
        }

        val INF = Long.MAX_VALUE / 4
        var dp = LongArray(maxMask) { INF }
        dp[0] = 0L

        for (num in nums) {
            val x = num.toLong()
            // cost to make this number cover each subset
            val cost = LongArray(maxMask)
            for (mask in 1 until maxMask) {
                val L = lcmArr[mask]
                val mult = ((x + L - 1) / L) * L
                cost[mask] = mult - x
            }
            val newDp = dp.clone()
            for (prev in 0 until maxMask) {
                val prevCost = dp[prev]
                if (prevCost == INF) continue
                for (sub in 1 until maxMask) {
                    val newMask = prev or sub
                    val cand = prevCost + cost[sub]
                    if (cand < newDp[newMask]) {
                        newDp[newMask] = cand
                    }
                }
            }
            dp = newDp
        }

        return dp[maxMask - 1].toInt()
    }

    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }

    private fun lcm(a: Long, b: Long): Long {
        if (a == 0L || b == 0L) return 0L
        return a / gcd(a, b) * b
    }
}
```

## Dart

```dart
class Solution {
  int minimumIncrements(List<int> nums, List<int> target) {
    int m = target.length;
    int fullMask = (1 << m) - 1;

    // Precompute LCM for each subset mask
    List<int> lcmMask = List.filled(1 << m, 1);
    for (int mask = 1; mask <= fullMask; ++mask) {
      int curLcm = 1;
      for (int i = 0; i < m; ++i) {
        if ((mask & (1 << i)) != 0) {
          curLcm = _lcm(curLcm, target[i]);
        }
      }
      lcmMask[mask] = curLcm;
    }

    const int INF = 1 << 60;
    List<int> dp = List.filled(1 << m, INF);
    dp[0] = 0;

    for (int num in nums) {
      // Cost to make this number a multiple of each subset's LCM
      List<int> costMask = List.filled(1 << m, 0);
      for (int mask = 1; mask <= fullMask; ++mask) {
        int L = lcmMask[mask];
        int inc = (( (num + L - 1) ~/ L) * L) - num;
        costMask[mask] = inc;
      }

      List<int> ndp = List.from(dp);
      for (int prev = 0; prev <= fullMask; ++prev) {
        if (dp[prev] == INF) continue;
        int remaining = fullMask ^ prev;
        for (int sub = remaining; sub > 0; sub = (sub - 1) & remaining) {
          int newMask = prev | sub;
          int newCost = dp[prev] + costMask[sub];
          if (newCost < ndp[newMask]) ndp[newMask] = newCost;
        }
      }
      dp = ndp;
    }

    return dp[fullMask];
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }

  int _lcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return a ~/ _gcd(a, b) * b;
  }
}
```

## Golang

```go
func minimumIncrements(nums []int, target []int) int {
    m := len(target)
    fullMask := (1 << m) - 1

    // precompute lcm for each subset mask
    lcmMask := make([]int64, 1<<m)
    for mask := 1; mask < (1 << m); mask++ {
        var cur int64 = 1
        for i := 0; i < m; i++ {
            if mask>>i&1 == 1 {
                t := int64(target[i])
                g := gcd(cur, t)
                cur = cur / g * t
            }
        }
        lcmMask[mask] = cur
    }

    const INF int64 = 1 << 60
    dp := make([]int64, 1<<m)
    for i := range dp {
        dp[i] = INF
    }
    dp[0] = 0

    for _, v := range nums {
        // cost to turn current number into a multiple of each subset's lcm
        cost := make([]int64, 1<<m)
        val := int64(v)
        for mask := 1; mask < (1 << m); mask++ {
            L := lcmMask[mask]
            mult := ((val + L - 1) / L) * L
            cost[mask] = mult - val
        }

        newdp := make([]int64, 1<<m)
        copy(newdp, dp) // option of not using this number

        for prev := 0; prev < (1 << m); prev++ {
            if dp[prev] == INF {
                continue
            }
            for mask := 1; mask < (1 << m); mask++ {
                newMask := prev | mask
                cand := dp[prev] + cost[mask]
                if cand < newdp[newMask] {
                    newdp[newMask] = cand
                }
            }
        }
        dp = newdp
    }

    return int(dp[fullMask])
}

func gcd(a, b int64) int64 {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}
```

## Ruby

```ruby
def minimum_increments(nums, target)
  m = target.size
  full_mask = (1 << m) - 1

  # lcm for each subset mask
  lcm_mask = Array.new(1 << m, 0)
  (1..full_mask).each do |mask|
    l = 1
    i = 0
    while i < m
      if (mask & (1 << i)) != 0
        t = target[i]
        g = l.gcd(t)
        l = l / g * t
      end
      i += 1
    end
    lcm_mask[mask] = l
  end

  inf = 1 << 60
  best_cost = Array.new(1 << m, inf)

  nums.each do |a|
    (1..full_mask).each do |mask|
      l = lcm_mask[mask]
      inc = (l - a % l) % l
      best_cost[mask] = inc if inc < best_cost[mask]
    end
  end

  dp = Array.new(1 << m, inf)
  dp[0] = 0
  (1..full_mask).each do |mask|
    sub = mask
    while sub > 0
      cost = best_cost[sub]
      if dp[mask ^ sub] + cost < dp[mask]
        dp[mask] = dp[mask ^ sub] + cost
      end
      sub = (sub - 1) & mask
    end
  end

  dp[full_mask]
end
```

## Scala

```scala
object Solution {
  def minimumIncrements(nums: Array[Int], target: Array[Int]): Int = {
    val k = target.length
    val fullMask = (1 << k) - 1

    // precompute lcm for each subset mask
    val lcms = new Array[Long](1 << k)
    var mask = 1
    while (mask <= fullMask) {
      var l: Long = 1L
      var i = 0
      while (i < k) {
        if ((mask & (1 << i)) != 0) {
          val t = target(i).toLong
          val g = gcd(l, t)
          l = (l / g) * t
        }
        i += 1
      }
      lcms(mask) = l
      mask += 1
    }

    val INF: Long = Long.MaxValue / 4
    var dp = Array.fill[Long](fullMask + 1)(INF)
    dp(0) = 0L

    for (numInt <- nums) {
      val num = numInt.toLong
      // cost to make this number a multiple of each subset's lcm
      val cost = new Array[Long](fullMask + 1)
      var s = 1
      while (s <= fullMask) {
        val l = lcms(s)
        val r = num % l
        cost(s) = if (r == 0L) 0L else l - r
        s += 1
      }

      // 0-1 knapsack style transition: each number can be used at most once
      val newDp = dp.clone()
      var oldMask = 0
      while (oldMask <= fullMask) {
        val cur = dp(oldMask)
        if (cur < INF) {
          var sub = 1
          while (sub <= fullMask) {
            val combined = oldMask | sub
            val cand = cur + cost(sub)
            if (cand < newDp(combined)) newDp(combined) = cand
            sub += 1
          }
        }
        oldMask += 1
      }
      dp = newDp
    }

    dp(fullMask).toInt
  }

  private def gcd(a: Long, b: Long): Long = {
    var x = a
    var y = b
    while (y != 0) {
      val t = x % y
      x = y
      y = t
    }
    x
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_increments(nums: Vec<i32>, target: Vec<i32>) -> i32 {
        use std::cmp::min;
        // helper functions
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        fn lcm(a: i64, b: i64) -> i64 {
            a / gcd(a, b) * b
        }

        let m = target.len();
        let full_mask = (1usize << m) - 1;

        // precompute lcm for each subset mask
        let mut lcm_mask = vec![0i64; full_mask + 1];
        for mask in 1..=full_mask {
            // isolate lowest set bit
            let low_bit = mask & (!mask + 1);
            let idx = low_bit.trailing_zeros() as usize;
            let prev = mask ^ low_bit;
            if prev == 0 {
                lcm_mask[mask] = target[idx] as i64;
            } else {
                lcm_mask[mask] = lcm(lcm_mask[prev], target[idx] as i64);
            }
        }

        const INF: i64 = i64::MAX / 4;
        let mut dp = vec![INF; full_mask + 1];
        dp[0] = 0;

        for &num in nums.iter() {
            // compute cost for each non‑empty subset using this number
            let mut cost = vec![INF; full_mask + 1];
            let x = num as i64;
            for mask in 1..=full_mask {
                let l = lcm_mask[mask];
                let need_mul = (x + l - 1) / l; // ceil division
                let y = need_mul * l;
                cost[mask] = y - x;
            }

            // DP transition
            let mut new_dp = dp.clone();
            for prev in 0..=full_mask {
                if dp[prev] == INF {
                    continue;
                }
                for sub in 1..=full_mask {
                    let nxt = prev | sub;
                    let cand = dp[prev] + cost[sub];
                    if cand < new_dp[nxt] {
                        new_dp[nxt] = cand;
                    }
                }
            }
            dp = new_dp;
        }

        dp[full_mask] as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-increments nums target)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([m (length target)]
         [maxMask (arithmetic-shift 1 m)]
         ;; compute lcm for each non‑empty subset of targets
         (define (lcm a b) (/ (* a b) (gcd a b)))
         (define lcms (let ([vec (make-vector maxMask 0)])
                        (for ([mask (in-range 1 maxMask)])
                          (define cur-lcm 1)
                          (for ([i (in-range m)])
                            (when (not (= (bitwise-and mask (arithmetic-shift 1 i)) 0))
                              (set! cur-lcm (lcm cur-lcm (list-ref target i)))))
                          (vector-set! vec mask cur-lcm))
                        vec))
         (define INF (expt 2 60))
         ;; dp[mask] = minimal cost to cover targets represented by mask
         (define dp (let ([vec (make-vector maxMask INF)])
                      (vector-set! vec 0 0)
                      vec)))
    (for ([num nums])
      (define ndp (vector-copy dp))
      (for ([mask (in-range maxMask)])
        (define cur (vector-ref dp mask))
        (when (< cur INF)
          (for ([s (in-range 1 maxMask)])
            (when (= (bitwise-and mask s) 0) ; only add uncovered targets
              (let* ([L (vector-ref lcms s)]
                     [q (quotient num L)]
                     [r (remainder num L)]
                     [next-multiple (* (if (= r 0) q (add1 q)) L)]
                     [cost (- next-multiple num)]
                     [newmask (bitwise-ior mask s)])
                (when (< (+ cur cost) (vector-ref ndp newmask))
                  (vector-set! ndp newmask (+ cur cost)))))))))
      (set! dp ndp))
    (vector-ref dp (sub1 maxMask))))
```

## Erlang

```erlang
-spec minimum_increments(Nums :: [integer()], Target :: [integer()]) -> integer().
minimum_increments(Nums, Target) ->
    M = length(Target),
    FullMask = (1 bsl M) - 1,
    Lcms = compute_lcms(FullMask, Target),
    INF = 1 bsl 60,
    DP0 = init_dp(FullMask, INF),
    FinalDP = lists:foldl(
        fun(X, DP) ->
            Costs = [{Mask, cost_to_multiple(X, maps:get(Mask, Lcms))} ||
                     Mask <- masks(FullMask)],
            update_dp(DP, Costs, FullMask, INF)
        end,
        DP0,
        Nums),
    element(FullMask + 1, FinalDP).

%% helper functions

compute_lcms(FullMask, Target) ->
    maps:from_list(
        [{Mask, lcm_of_mask(Mask, Target)} ||
         Mask <- masks(FullMask)]).

masks(FM) -> lists:seq(0, FM).

lcm_of_mask(0, _) -> 1;
lcm_of_mask(Mask, Targets) ->
    lcm_of_mask(Mask, Targets, 1, 0).

lcm_of_mask(_, [], Acc, _Idx) -> Acc;
lcm_of_mask(Mask, [T|Rest], Acc, Idx) ->
    NewAcc = case (Mask bsr Idx) band 1 of
                1 -> lcm(Acc, T);
                0 -> Acc
            end,
    lcm_of_mask(Mask, Rest, NewAcc, Idx + 1).

lcm(A, B) when A == 0; B == 0 -> 0;
lcm(A, B) ->
    G = gcd(A, B),
    (A div G) * B.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

cost_to_multiple(X, L) when L =:= 1 -> 0;
cost_to_multiple(X, L) ->
    Rem = X rem L,
    if Rem == 0 -> 0; true -> L - Rem end.

init_dp(FullMask, INF) ->
    Tuple = erlang:make_tuple(FullMask + 1, INF),
    setelement(1, Tuple, 0).

update_dp(OldDP, Costs, FullMask, INF) ->
    lists:foldl(
        fun({MaskS, CostS}, DPAcc) ->
            lists:foldl(
                fun(PrevMask, AccDP) ->
                    PrevCost = element(PrevMask + 1, OldDP),
                    if PrevCost < INF ->
                        NewMask = PrevMask bor MaskS,
                        OldVal = element(NewMask + 1, AccDP),
                        NewCost = PrevCost + CostS,
                        if NewCost < OldVal ->
                            setelement(NewMask + 1, AccDP, NewCost);
                           true -> AccDP
                        end;
                       true -> AccDP
                    end
                end,
                DPAcc,
                masks(FullMask)
            )
        end,
        OldDP,
        Costs).
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @spec minimum_increments(nums :: [integer], target :: [integer]) :: integer
  def minimum_increments(nums, target) do
    m = length(target)
    max_mask = 1 <<< m

    # precompute lcm for every mask (0..max_mask-1)
    lcms =
      Enum.map(0..max_mask - 1, fn mask ->
        if mask == 0 do
          1
        else
          selected =
            for i <- 0..m - 1,
                Bitwise.band(mask, 1 <<< i) != 0,
                do: Enum.at(target, i)

          Enum.reduce(selected, 1, fn a, acc -> lcm(acc, a) end)
        end
      end)

    inf = 1_000_000_000_000_000_000

    dp =
      :array.from_list(List.duplicate(inf, max_mask))
      |> :array.set(0, 0)

    final_dp =
      Enum.reduce(nums, dp, fn a, old_dp ->
        new_dp = :array.from_list(:array.to_list(old_dp))

        for prev <- 0..max_mask - 1 do
          base = :array.get(prev, old_dp)

          if base < inf do
            for sub <- 1..max_mask - 1 do
              l = Enum.at(lcms, sub)
              inc = ((a + l - 1) div l) * l - a
              new_mask = Bitwise.bor(prev, sub)
              cand = base + inc
              cur = :array.get(new_mask, new_dp)

              if cand < cur do
                new_dp = :array.set(new_mask, cand, new_dp)
              end
            end
          end
        end

        new_dp
      end)

    :array.get(max_mask - 1, final_dp)
  end

  defp lcm(a, b) do
    div(a, Integer.gcd(a, b)) * b
  end
end
```

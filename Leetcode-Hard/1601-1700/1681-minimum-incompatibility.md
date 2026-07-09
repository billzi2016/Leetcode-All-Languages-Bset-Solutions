# 1681. Minimum Incompatibility

## Cpp

```cpp
class Solution {
public:
    int minimumIncompatibility(vector<int>& nums, int k) {
        int n = nums.size();
        int sz = n / k;
        // early impossibility check
        vector<int> freq(17, 0);
        for (int v : nums) {
            if (++freq[v] > k) return -1;
        }
        const int FULL = (1 << n) - 1;
        const int INF = 1e9;
        // precompute valid subsets of size sz and their incompatibility
        vector<int> incompat(1 << n, -1);
        vector<int> validMasks;
        for (int mask = 0; mask <= FULL; ++mask) {
            if (__builtin_popcount(mask) != sz) continue;
            bool seen[17] = {false};
            int mn = INT_MAX, mx = INT_MIN;
            bool ok = true;
            for (int i = 0; i < n; ++i) if (mask & (1 << i)) {
                int v = nums[i];
                if (seen[v]) { ok = false; break; }
                seen[v] = true;
                mn = min(mn, v);
                mx = max(mx, v);
            }
            if (ok) {
                incompat[mask] = mx - mn;
                validMasks.push_back(mask);
            }
        }
        vector<int> dp(1 << n, INF);
        dp[0] = 0;
        for (int mask = 0; mask <= FULL; ++mask) {
            if (dp[mask] == INF) continue;
            // try to add a new group
            for (int sub : validMasks) {
                if ((sub & mask) != 0) continue;
                int nmask = mask | sub;
                dp[nmask] = min(dp[nmask], dp[mask] + incompat[sub]);
            }
        }
        return dp[FULL] == INF ? -1 : dp[FULL];
    }
};
```

## Java

```java
class Solution {
    public int minimumIncompatibility(int[] nums, int k) {
        int n = nums.length;
        int m = n / k; // size of each subset
        // quick impossibility check: any number appears more than k times
        int[] freq = new int[n + 1];
        for (int v : nums) {
            if (++freq[v] > k) return -1;
        }

        int fullMask = (1 << n) - 1;
        int[] groupCost = new int[1 << n];
        java.util.ArrayList<Integer> groups = new java.util.ArrayList<>();

        // precompute valid groups of size m with distinct elements
        for (int mask = 0; mask <= fullMask; ++mask) {
            if (Integer.bitCount(mask) != m) continue;
            int seen = 0;
            int minVal = Integer.MAX_VALUE;
            int maxVal = Integer.MIN_VALUE;
            boolean ok = true;
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) {
                    int v = nums[i];
                    int bit = 1 << v;
                    if ((seen & bit) != 0) { // duplicate value in this subset
                        ok = false;
                        break;
                    }
                    seen |= bit;
                    if (v < minVal) minVal = v;
                    if (v > maxVal) maxVal = v;
                }
            }
            if (ok) {
                int cost = maxVal - minVal;
                groupCost[mask] = cost;
                groups.add(mask);
            } else {
                groupCost[mask] = -1;
            }
        }

        int INF = 1_000_000_0;
        int[] dp = new int[1 << n];
        java.util.Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int mask = 0; mask <= fullMask; ++mask) {
            if (dp[mask] == INF) continue;
            // try to add a valid group that doesn't intersect with current mask
            for (int g : groups) {
                if ((mask & g) != 0) continue;
                int newMask = mask | g;
                int newCost = dp[mask] + groupCost[g];
                if (newCost < dp[newMask]) {
                    dp[newMask] = newCost;
                }
            }
        }

        return dp[fullMask] == INF ? -1 : dp[fullMask];
    }
}
```

## Python

```python
class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        m = n // k  # size of each subset

        # If any number appears more than k times, impossible
        from collections import Counter
        cnt = Counter(nums)
        if any(v > k for v in cnt.values()):
            return -1

        full_mask = (1 << n) - 1
        INF = float('inf')

        # Precompute incompatibility for all valid subsets of size m
        group_incompat = {}
        for mask in range(1 << n):
            if mask.bit_count() != m:
                continue
            seen = set()
            min_v = 17  # nums[i] <= n <=16
            max_v = 0
            ok = True
            mm = mask
            idx = 0
            while mm:
                if mm & 1:
                    val = nums[idx]
                    if val in seen:
                        ok = False
                        break
                    seen.add(val)
                    if val < min_v:
                        min_v = val
                    if val > max_v:
                        max_v = val
                idx += 1
                mm >>= 1
            if ok:
                group_incompat[mask] = max_v - min_v

        dp = [INF] * (1 << n)
        dp[0] = 0

        # Iterate over all masks whose bit count is multiple of m
        for mask in range(1, full_mask + 1):
            bits = mask.bit_count()
            if bits % m != 0:
                continue
            sub = mask
            while sub:
                if sub.bit_count() == m and sub in group_incompat:
                    prev = mask ^ sub
                    val = dp[prev] + group_incompat[sub]
                    if val < dp[mask]:
                        dp[mask] = val
                sub = (sub - 1) & mask

        return dp[full_mask] if dp[full_mask] != INF else -1
```

## Python3

```python
import sys
from typing import List

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = n // k
        # pigeonhole check
        from collections import Counter
        cnt = Counter(nums)
        if any(v > k for v in cnt.values()):
            return -1
        if m == 1:
            return 0

        full = (1 << n) - 1
        valid = {}
        # precompute all subsets of size m with distinct values
        for mask in range(1 << n):
            if mask.bit_count() != m:
                continue
            seen_vals = 0
            ok = True
            min_v = 17
            max_v = 0
            bits = mask
            while bits:
                lsb = bits & -bits
                i = (lsb.bit_length() - 1)
                v = nums[i]
                if (seen_vals >> v) & 1:
                    ok = False
                    break
                seen_vals |= 1 << v
                if v < min_v:
                    min_v = v
                if v > max_v:
                    max_v = v
                bits ^= lsb
            if ok:
                valid[mask] = max_v - min_v

        INF = sys.maxsize
        dp = [INF] * (1 << n)
        dp[0] = 0

        # iterate over masks that are reachable (bits count multiple of m)
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            # number of already used elements must be multiple of m
            if mask.bit_count() % m != 0:
                continue
            for sub, inc in valid.items():
                if (sub & mask) == 0:
                    new_mask = mask | sub
                    if dp[new_mask] > dp[mask] + inc:
                        dp[new_mask] = dp[mask] + inc

        return -1 if dp[full] == INF else dp[full]
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int minimumIncompatibility(int* nums, int numsSize, int k) {
    int n = numsSize;
    if (n % k != 0) return -1;
    int groupSize = n / k;

    // Early impossibility check: any number appears more than k times
    int freq[17] = {0};
    for (int i = 0; i < n; ++i) {
        if (++freq[nums[i]] > k) return -1;
    }

    int totalMask = (1 << n) - 1;
    int *inc = (int *)malloc((totalMask + 1) * sizeof(int));
    for (int i = 0; i <= totalMask; ++i) inc[i] = -1;

    // Store all valid subsets of size groupSize
    int *validSubs = (int *)malloc((totalMask + 1) * sizeof(int));
    int vcnt = 0;

    for (int mask = 0; mask <= totalMask; ++mask) {
        if (__builtin_popcount(mask) != groupSize) continue;
        int seenVals = 0;
        int mn = INT_MAX, mx = INT_MIN;
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                int val = nums[i];
                if (seenVals & (1 << val)) { ok = false; break; }
                seenVals |= (1 << val);
                if (val < mn) mn = val;
                if (val > mx) mx = val;
            }
        }
        if (!ok) continue;
        inc[mask] = mx - mn;
        validSubs[vcnt++] = mask;
    }

    const int INF = INT_MAX / 2;
    int *dp = (int *)malloc((totalMask + 1) * sizeof(int));
    for (int i = 0; i <= totalMask; ++i) dp[i] = INF;
    dp[0] = 0;

    for (int mask = 0; mask <= totalMask; ++mask) {
        if (dp[mask] == INF) continue;
        for (int idx = 0; idx < vcnt; ++idx) {
            int sub = validSubs[idx];
            if ((mask & sub) != 0) continue;
            int newMask = mask | sub;
            int cand = dp[mask] + inc[sub];
            if (cand < dp[newMask]) dp[newMask] = cand;
        }
    }

    int ans = dp[totalMask];
    free(inc);
    free(validSubs);
    free(dp);
    return (ans == INF) ? -1 : ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public int MinimumIncompatibility(int[] nums, int k) {
        int n = nums.Length;
        if (n % k != 0) return -1;
        int m = n / k; // size of each subset

        // Early impossibility check: any number appears more than k times
        var cnt = new int[n + 1];
        foreach (var v in nums) {
            cnt[v]++;
            if (cnt[v] > k) return -1;
        }

        int fullMask = (1 << n) - 1;

        // Precompute all valid groups of size m with distinct elements
        var groups = new List<(int mask, int incompat)>[n];
        for (int i = 0; i < n; i++) groups[i] = new List<(int, int)>();

        for (int mask = 0; mask <= fullMask; mask++) {
            if (BitOperations.PopCount((uint)mask) != m) continue;

            bool[] seen = new bool[n + 1];
            int minVal = int.MaxValue;
            int maxVal = int.MinValue;
            bool ok = true;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) continue;
                int val = nums[i];
                if (seen[val]) { ok = false; break; }
                seen[val] = true;
                if (val < minVal) minVal = val;
                if (val > maxVal) maxVal = val;
            }
            if (!ok) continue;

            int incompat = maxVal - minVal;
            int lowBitIdx = BitOperations.TrailingZeroCount((uint)mask);
            groups[lowBitIdx].Add((mask, incompat));
        }

        const int INF = int.MaxValue / 2;
        int[] dp = new int[1 << n];
        Array.Fill(dp, INF);
        dp[0] = 0;

        for (int mask = 0; mask <= fullMask; mask++) {
            if (dp[mask] == INF) continue;
            if (mask == fullMask) break;

            // find first unused element
            int first = 0;
            while (((mask >> first) & 1) == 1) first++;

            foreach (var (gMask, inc) in groups[first]) {
                if ((gMask & mask) != 0) continue; // overlap, cannot use
                int newMask = mask | gMask;
                int newVal = dp[mask] + inc;
                if (newVal < dp[newMask]) dp[newMask] = newVal;
            }
        }

        return dp[fullMask] == INF ? -1 : dp[fullMask];
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
var minimumIncompatibility = function(nums, k) {
    const n = nums.length;
    const m = n / k; // size of each subset

    // early impossibility check: any value appears more than k times
    const freq = new Map();
    for (const v of nums) {
        freq.set(v, (freq.get(v) || 0) + 1);
    }
    for (const cnt of freq.values()) {
        if (cnt > k) return -1;
    }

    const totalMask = 1 << n;

    // helper: popcount
    const popcnt = (x) => {
        let c = 0;
        while (x) {
            x &= x - 1;
            c++;
        }
        return c;
    };

    // precompute valid group masks and their incompatibility cost
    const groupCost = new Map();               // mask -> cost
    const groupsByFirst = Array.from({length: n}, () => []); // first (lowest) element index -> list of masks

    for (let mask = 0; mask < totalMask; ++mask) {
        if (popcnt(mask) !== m) continue;
        const seen = new Set();
        let minV = Infinity, maxV = -Infinity;
        let ok = true;
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                const val = nums[i];
                if (seen.has(val)) { ok = false; break; }
                seen.add(val);
                if (val < minV) minV = val;
                if (val > maxV) maxV = val;
            }
        }
        if (!ok) continue;
        const cost = maxV - minV;
        groupCost.set(mask, cost);
        // store by lowest set bit index
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                groupsByFirst[i].push(mask);
                break;
            }
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    const dp = new Array(totalMask).fill(INF);
    dp[0] = 0;

    for (let mask = 0; mask < totalMask; ++mask) {
        if (dp[mask] === INF) continue;
        const used = popcnt(mask);
        if (used === n) continue; // already full
        // find first unset bit to anchor next group
        let i = 0;
        while ((mask >> i) & 1) i++;
        for (const gMask of groupsByFirst[i]) {
            if ((gMask & mask) !== 0) continue; // overlap, cannot use
            const newMask = mask | gMask;
            const newCost = dp[mask] + groupCost.get(gMask);
            if (newCost < dp[newMask]) dp[newMask] = newCost;
        }
    }

    const ans = dp[totalMask - 1];
    return ans === INF ? -1 : ans;
};
```

## Typescript

```typescript
function minimumIncompatibility(nums: number[], k: number): number {
    const n = nums.length;
    const groupSize = n / k;

    // early impossibility check
    const freq = new Map<number, number>();
    for (const v of nums) {
        freq.set(v, (freq.get(v) ?? 0) + 1);
        if ((freq.get(v) ?? 0) > k) return -1;
    }

    const totalMask = 1 << n;
    const incompat = new Int32Array(totalMask).fill(-1);

    // precompute incompatibility for all subsets of size groupSize with distinct values
    const groups: number[] = [];
    for (let mask = 0; mask < totalMask; mask++) {
        if (popcnt(mask) !== groupSize) continue;
        let valMask = 0;
        let minV = 17; // nums[i] <= n <=16
        let maxV = -1;
        let dup = false;
        for (let i = 0; i < n; i++) {
            if ((mask >> i) & 1) {
                const v = nums[i];
                if ((valMask >> v) & 1) { dup = true; break; }
                valMask |= 1 << v;
                if (v < minV) minV = v;
                if (v > maxV) maxV = v;
            }
        }
        if (!dup) {
            incompat[mask] = maxV - minV;
            groups.push(mask);
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    const dp = new Array<number>(totalMask).fill(INF);
    dp[0] = 0;

    for (let mask = 0; mask < totalMask; mask++) {
        if (dp[mask] === INF) continue;
        for (const g of groups) {
            if ((mask & g) !== 0) continue;
            const newMask = mask | g;
            const val = dp[mask] + incompat[g];
            if (val < dp[newMask]) dp[newMask] = val;
        }
    }

    const ans = dp[totalMask - 1];
    return ans === INF ? -1 : ans;

    function popcnt(x: number): number {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    }
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
    function minimumIncompatibility($nums, $k) {
        $n = count($nums);
        $groupSize = intdiv($n, $k);

        // If any number appears more than k times, impossible.
        $freq = array_fill(0, $n + 1, 0);
        foreach ($nums as $v) {
            $freq[$v]++;
            if ($freq[$v] > $k) {
                return -1;
            }
        }

        $totalMask = (1 << $n) - 1;
        $subsetCost = array_fill(0, $totalMask + 1, -1);
        $validMasks = [];

        // Precompute cost for each subset of size groupSize with distinct values.
        for ($mask = 0; $mask <= $totalMask; ++$mask) {
            if ($this->popcnt($mask) != $groupSize) continue;

            $seen = [];
            $minVal = PHP_INT_MAX;
            $maxVal = PHP_INT_MIN;
            $ok = true;

            for ($i = 0; $i < $n; ++$i) {
                if (($mask >> $i) & 1) {
                    $val = $nums[$i];
                    if (isset($seen[$val])) {
                        $ok = false;
                        break;
                    }
                    $seen[$val] = true;
                    if ($val < $minVal) $minVal = $val;
                    if ($val > $maxVal) $maxVal = $val;
                }
            }

            if ($ok) {
                $cost = $maxVal - $minVal;
                $subsetCost[$mask] = $cost;
                $validMasks[] = $mask;
            }
        }

        $INF = PHP_INT_MAX;
        $dp = array_fill(0, $totalMask + 1, $INF);
        $dp[0] = 0;

        // DP over masks.
        for ($mask = 0; $mask <= $totalMask; ++$mask) {
            if ($dp[$mask] === $INF) continue;
            if ($this->popcnt($mask) % $groupSize !== 0) continue;

            foreach ($validMasks as $sub) {
                if (($mask & $sub) === 0) {
                    $newMask = $mask | $sub;
                    $newVal = $dp[$mask] + $subsetCost[$sub];
                    if ($newVal < $dp[$newMask]) {
                        $dp[$newMask] = $newVal;
                    }
                }
            }
        }

        $ans = $dp[$totalMask];
        return $ans === $INF ? -1 : $ans;
    }

    private function popcnt(int $x): int {
        $c = 0;
        while ($x) {
            $x &= $x - 1;
            $c++;
        }
        return $c;
    }
}
```

## Swift

```swift
class Solution {
    func minimumIncompatibility(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let m = n / k
        // Early impossibility check: any number appears more than k times
        var freq = [Int:Int]()
        for v in nums {
            freq[v, default: 0] += 1
            if freq[v]! > k { return -1 }
        }
        let fullMask = (1 << n) - 1
        // Precompute incompatibility cost for each subset of size m with distinct values
        var cost = [Int](repeating: -1, count: 1 << n)
        for mask in 0..<(1 << n) {
            if mask.nonzeroBitCount != m { continue }
            var seen = Set<Int>()
            var minV = Int.max
            var maxV = Int.min
            var ok = true
            var idx = 0
            var tempMask = mask
            while tempMask > 0 {
                if (tempMask & 1) == 1 {
                    let v = nums[idx]
                    if seen.contains(v) { ok = false; break }
                    seen.insert(v)
                    if v < minV { minV = v }
                    if v > maxV { maxV = v }
                }
                idx += 1
                tempMask >>= 1
            }
            if ok {
                cost[mask] = maxV - minV
            }
        }
        let INF = Int.max / 2
        var dp = [Int](repeating: INF, count: 1 << n)
        dp[0] = 0
        for mask in 0...fullMask {
            if dp[mask] == INF { continue }
            // remaining elements to assign
            let remaining = fullMask ^ mask
            var sub = remaining
            while sub > 0 {
                if cost[sub] != -1 {
                    let newMask = mask | sub
                    let val = dp[mask] + cost[sub]
                    if val < dp[newMask] {
                        dp[newMask] = val
                    }
                }
                sub = (sub - 1) & remaining
            }
        }
        return dp[fullMask] == INF ? -1 : dp[fullMask]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumIncompatibility(nums: IntArray, k: Int): Int {
        val n = nums.size
        val groupSize = n / k

        // If any number appears more than k times, impossible.
        val freq = IntArray(n + 1)
        for (v in nums) {
            freq[v]++
            if (freq[v] > k) return -1
        }

        val fullMask = (1 shl n) - 1
        val incompat = IntArray(1 shl n) { -1 }

        // Pre‑compute incompatibility for every subset of size groupSize with distinct values.
        for (mask in 0..fullMask) {
            if (Integer.bitCount(mask) != groupSize) continue
            var m = mask
            var minV = Int.MAX_VALUE
            var maxV = Int.MIN_VALUE
            var valMask = 0
            var ok = true
            while (m != 0 && ok) {
                val lsb = m and -m
                val idx = Integer.numberOfTrailingZeros(lsb)
                val v = nums[idx]
                if ((valMask shr v) and 1 == 1) {
                    ok = false
                    break
                }
                valMask = valMask or (1 shl v)
                if (v < minV) minV = v
                if (v > maxV) maxV = v
                m -= lsb
            }
            if (ok) incompat[mask] = maxV - minV
        }

        // Collect all valid group masks.
        val groups = mutableListOf<Int>()
        for (mask in 0..fullMask) {
            if (incompat[mask] != -1) groups.add(mask)
        }

        val INF = 1_000_000_000
        val dp = IntArray(1 shl n) { INF }
        dp[0] = 0

        for (mask in 0..fullMask) {
            val cur = dp[mask]
            if (cur == INF) continue
            for (g in groups) {
                if ((mask and g) != 0) continue
                val newMask = mask or g
                val cand = cur + incompat[g]
                if (cand < dp[newMask]) dp[newMask] = cand
            }
        }

        val ans = dp[fullMask]
        return if (ans == INF) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumIncompatibility(List<int> nums, int k) {
    int n = nums.length;
    int m = n ~/ k;

    // Early impossibility check: any number appears more than k times.
    List<int> freq = List.filled(n + 1, 0);
    for (int v in nums) {
      freq[v]++;
      if (freq[v] > k) return -1;
    }

    int fullMask = (1 << n) - 1;

    // Precompute all valid groups of size m and their incompatibility.
    Map<int, int> costMap = {};
    for (int mask = 0; mask <= fullMask; mask++) {
      if (_popCount(mask) != m) continue;
      List<bool> seen = List.filled(n + 1, false);
      int minV = n + 1;
      int maxV = 0;
      bool ok = true;
      for (int i = 0; i < n; i++) {
        if ((mask >> i) & 1 == 1) {
          int val = nums[i];
          if (seen[val]) {
            ok = false;
            break;
          }
          seen[val] = true;
          if (val < minV) minV = val;
          if (val > maxV) maxV = val;
        }
      }
      if (ok) costMap[mask] = maxV - minV;
    }

    const int INF = 1 << 30;
    List<int> dp = List.filled(1 << n, INF);
    dp[0] = 0;

    List<int> groups = costMap.keys.toList();

    for (int mask = 0; mask <= fullMask; mask++) {
      if (dp[mask] == INF) continue;
      for (int g in groups) {
        if ((g & mask) != 0) continue; // overlap, cannot use
        int newMask = mask | g;
        int newCost = dp[mask] + costMap[g]!;
        if (newCost < dp[newMask]) dp[newMask] = newCost;
      }
    }

    int ans = dp[fullMask];
    return ans == INF ? -1 : ans;
  }

  int _popCount(int x) {
    int cnt = 0;
    while (x > 0) {
      cnt += x & 1;
      x >>= 1;
    }
    return cnt;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func minimumIncompatibility(nums []int, k int) int {
	n := len(nums)
	sz := n / k

	// Early impossibility check: any number appears more than k times
	freq := make([]int, n+1)
	for _, v := range nums {
		freq[v]++
		if freq[v] > k {
			return -1
		}
	}

	totalMask := 1 << n
	incompat := make([]int, totalMask)
	const INF = int(1e9)

	for i := 0; i < totalMask; i++ {
		incompat[i] = -1
	}
	groups := []int{}

	// Precompute valid subsets of size sz with unique elements and their incompatibility
	for mask := 0; mask < totalMask; mask++ {
		if bits.OnesCount(uint(mask)) != sz {
			continue
		}
		valSeen := 0
		minV, maxV := int(1<<30), -int(1<<30)
		ok := true
		for i := 0; i < n; i++ {
			if (mask>>i)&1 == 1 {
				v := nums[i]
				bit := 1 << v
				if valSeen&bit != 0 {
					ok = false
					break
				}
				valSeen |= bit
				if v < minV {
					minV = v
				}
				if v > maxV {
					maxV = v
				}
			}
		}
		if ok {
			incompat[mask] = maxV - minV
			groups = append(groups, mask)
		}
	}

	dp := make([]int, totalMask)
	for i := 0; i < totalMask; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	fullMask := totalMask - 1
	for mask := 0; mask <= fullMask; mask++ {
		if dp[mask] == INF {
			continue
		}
		if bits.OnesCount(uint(mask))%sz != 0 {
			continue
		}
		for _, g := range groups {
			if mask&g == 0 {
				newMask := mask | g
				if dp[newMask] > dp[mask]+incompat[g] {
					dp[newMask] = dp[mask] + incompat[g]
				}
			}
		}
	}

	if dp[fullMask] >= INF {
		return -1
	}
	return dp[fullMask]
}
```

## Ruby

```ruby
def minimum_incompatibility(nums, k)
  n = nums.length
  m = n / k

  # feasibility check: any number appears more than k times -> impossible
  cnt_num = Hash.new(0)
  nums.each { |v| cnt_num[v] += 1 }
  return -1 if cnt_num.values.any? { |c| c > k }

  full_mask = (1 << n) - 1

  # popcount for all masks
  popcnt = Array.new(1 << n, 0)
  (1...(1 << n)).each do |i|
    popcnt[i] = popcnt[i >> 1] + (i & 1)
  end

  # precompute valid subsets of size m with unique elements and their incompatibility
  cost = Array.new(1 << n, nil)
  valid_masks = []
  (0..full_mask).each do |mask|
    next unless popcnt[mask] == m
    seen = {}
    min_v = 1000
    max_v = -1000
    ok = true
    n.times do |i|
      if ((mask >> i) & 1) == 1
        v = nums[i]
        if seen[v]
          ok = false
          break
        end
        seen[v] = true
        min_v = v if v < min_v
        max_v = v if v > max_v
      end
    end
    next unless ok
    cost[mask] = max_v - min_v
    valid_masks << mask
  end

  INF = (1 << 60)
  dp = Array.new(1 << n, INF)
  dp[0] = 0

  (0..full_mask).each do |mask|
    next if dp[mask] == INF
    # if already full, continue
    next if mask == full_mask
    valid_masks.each do |sub|
      next unless (sub & mask) == 0
      new_mask = mask | sub
      val = dp[mask] + cost[sub]
      dp[new_mask] = val if val < dp[new_mask]
    end
  end

  ans = dp[full_mask]
  ans == INF ? -1 : ans
end
```

## Scala

```scala
object Solution {
  def minimumIncompatibility(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val sz = n / k

    // Early impossibility check: any number appears more than k times
    val freq = new Array[Int](n + 1)
    for (v <- nums) {
      freq(v) += 1
      if (freq(v) > k) return -1
    }

    val totalMask = (1 << n) - 1
    val incompat = Array.fill[Int](1 << n)(-1)

    // Precompute incompatibility for all subsets of size sz with distinct elements
    var mask = 0
    while (mask <= totalMask) {
      if (Integer.bitCount(mask) == sz) {
        val seen = new Array[Boolean](n + 1)
        var minV = Int.MaxValue
        var maxV = Int.MinValue
        var ok = true
        var i = 0
        while (i < n && ok) {
          if ((mask & (1 << i)) != 0) {
            val v = nums(i)
            if (seen(v)) ok = false
            else {
              seen(v) = true
              if (v < minV) minV = v
              if (v > maxV) maxV = v
            }
          }
          i += 1
        }
        if (ok) incompat(mask) = maxV - minV
      }
      mask += 1
    }

    val validMasks = {
      val buf = scala.collection.mutable.ArrayBuffer[Int]()
      var m = 0
      while (m <= totalMask) {
        if (incompat(m) != -1) buf += m
        m += 1
      }
      buf.toArray
    }

    val INF = Int.MaxValue / 2
    val dp = Array.fill[Int](1 << n)(INF)
    dp(0) = 0

    var curMask = 0
    while (curMask <= totalMask) {
      if (dp(curMask) != INF && (Integer.bitCount(curMask) % sz == 0)) {
        for (s <- validMasks) {
          if ((curMask & s) == 0) {
            val newMask = curMask | s
            val newVal = dp(curMask) + incompat(s)
            if (newVal < dp(newMask)) dp(newMask) = newVal
          }
        }
      }
      curMask += 1
    }

    val ans = dp(totalMask)
    if (ans >= INF) -1 else ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_incompatibility(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_usize = k as usize;
        if n % k_usize != 0 {
            return -1;
        }
        let sz = n / k_usize; // size of each subset

        // quick impossibility check: any number appears more than k times
        {
            let mut cnt = vec![0usize; n + 1];
            for &v in &nums {
                cnt[v as usize] += 1;
                if cnt[v as usize] > k_usize {
                    return -1;
                }
            }
        }

        let total_masks = 1usize << n;
        // incompatibility of each valid subset, -1 means invalid
        let mut incompat = vec![-1i32; total_masks];

        for mask in 0..total_masks {
            if mask.count_ones() as usize != sz {
                continue;
            }
            let mut seen = [false; 17]; // nums[i] <= n <= 16
            let mut min_v = i32::MAX;
            let mut max_v = i32::MIN;
            let mut ok = true;
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    let val = nums[i] as usize;
                    if seen[val] {
                        ok = false;
                        break;
                    }
                    seen[val] = true;
                    let v = nums[i];
                    if v < min_v { min_v = v; }
                    if v > max_v { max_v = v; }
                }
            }
            if ok {
                incompat[mask] = max_v - min_v;
            }
        }

        let inf = i32::MAX / 2;
        let mut dp = vec![inf; total_masks];
        dp[0] = 0;

        for mask in 1..total_masks {
            let pc = mask.count_ones() as usize;
            if pc % sz != 0 {
                continue;
            }
            // enumerate submasks of mask
            let mut sub = mask;
            while sub > 0 {
                if incompat[sub] != -1 {
                    let prev = dp[mask ^ sub];
                    if prev + incompat[sub] < dp[mask] {
                        dp[mask] = prev + incompat[sub];
                    }
                }
                sub = (sub - 1) & mask;
            }
        }

        let ans = dp[total_masks - 1];
        if ans >= inf { -1 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (minimum-incompatibility nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (group-size (/ n k))
         (full-mask (sub1 (arithmetic-shift 1 n))) ; 2^n - 1
         (INF 1000000000)
         (num-vec (list->vector nums))
         (compat (make-vector (arithmetic-shift 1 n) -1))
         (valid-groups '()))
    ;; pre‑compute incompatibility for every subset of size group-size
    (for ([mask (in-range (arithmetic-shift 1 n))])
      (when (= (bitwise-bit-count mask) group-size)
        (let-values ([(val-mask minv maxv dup)
                      (for/fold ([val-mask 0] [minv n] [maxv -1] [dup #f])
                                ([i (in-range n)])
                        (if (= (bitwise-and mask (arithmetic-shift 1 i)) 0)
                            (values val-mask minv maxv dup)
                            (let* ((v (vector-ref num-vec i))
                                   (bit (arithmetic-shift 1 v)))
                              (if (zero? (bitwise-and val-mask bit))
                                  (values (bitwise-ior val-mask bit) (min minv v) (max maxv v) dup)
                                  (values val-mask minv maxv #t)))))])
          (unless dup
            (vector-set! compat mask (- maxv minv))
            (set! valid-groups (cons mask valid-groups)))))))
    ;; DP over masks
    (let ((dp (make-vector (arithmetic-shift 1 n) INF)))
      (vector-set! dp 0 0)
      (for ([mask (in-range (arithmetic-shift 1 n))])
        (let ((cur (vector-ref dp mask)))
          (when (< cur INF)
            (for ([g valid-groups])
              (when (= (bitwise-and mask g) 0)
                (let* ((new-mask (bitwise-ior mask g))
                       (new-val (+ cur (vector-ref compat g))))
                  (when (< new-val (vector-ref dp new-mask))
                    (vector-set! dp new-mask new-val)))))))))
      (let ((ans (vector-ref dp full-mask)))
        (if (>= ans INF) -1 ans)))))
```

## Erlang

```erlang
-spec minimum_incompatibility(Nums :: [integer()], K :: integer()) -> integer().
minimum_incompatibility(Nums, K) ->
    N = length(Nums),
    GroupSize = N div K,
    case impossible_by_freq(Nums, K) of
        true -> -1;
        false ->
            ValidGroups = generate_valid_groups(N, GroupSize, Nums),
            FullMask = (1 bsl N) - 1,
            Inf = 1 bsl 60,
            DP0 = #{0 => 0},
            DPF = dp_loop(0, FullMask, ValidGroups, DP0, Inf),
            case maps:get(FullMask, DPF, Inf) of
                V when V >= Inf -> -1;
                V -> V
            end
    end.

impossible_by_freq(Nums, K) ->
    Freq = lists:foldl(
        fun(X, Acc) ->
            maps:update_with(
                X,
                fun(C) -> C + 1 end,
                1,
                Acc)
        end,
        #{},
        Nums),
    maps:fold(
        fun(_Key, Count, Acc) ->
            if Count > K -> true;
               true -> Acc
            end
        end,
        false,
        Freq).

generate_valid_groups(N, GSize, Nums) ->
    Full = (1 bsl N) - 1,
    lists:foldl(
        fun(Mask, Acc) ->
            case popcnt(Mask) of
                GSize ->
                    Values = values_from_mask(Mask, Nums),
                    case length(lists:usort(Values)) == GSize of
                        true ->
                            MaxV = lists:max(Values),
                            MinV = lists:min(Values),
                            [{Mask, MaxV - MinV} | Acc];
                        false -> Acc
                    end;
                _ -> Acc
            end
        end,
        [],
        lists:seq(0, Full)).

popcnt(0) -> 0;
popcnt(N) -> 1 + popcnt(N band (N - 1)).

values_from_mask(Mask, Nums) ->
    values_from_mask(0, Mask, Nums, []).

values_from_mask(I, Mask, Nums, Acc) when I < length(Nums) ->
    Bit = 1 bsl I,
    case (Mask band Bit) of
        0 -> values_from_mask(I + 1, Mask, Nums, Acc);
        _ ->
            Num = lists:nth(I + 1, Nums),
            values_from_mask(I + 1, Mask, Nums, [Num | Acc])
    end;
values_from_mask(_, _, _, Acc) -> lists:reverse(Acc).

dp_loop(Mask, FullMask, ValidGroups, DP, Inf) when Mask =< FullMask ->
    Cur = maps:get(Mask, DP, Inf),
    DP1 = if
        Cur == Inf ->
            DP;
        true ->
            Rem = FullMask bxor Mask,
            lists:foldl(
                fun({GMask, Inc}, AccDP) ->
                    case (Rem band GMask) of
                        GMask ->
                            NewMask = Mask bor GMask,
                            Old = maps:get(NewMask, AccDP, Inf),
                            NewVal = Cur + Inc,
                            if NewVal < Old -> maps:put(NewMask, NewVal, AccDP);
                               true -> AccDP
                            end;
                        _ -> AccDP
                    end
                end,
                DP,
                ValidGroups)
          end,
    dp_loop(Mask + 1, FullMask, ValidGroups, DP1, Inf);
dp_loop(_, _, _, DP, _) -> DP.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_incompatibility(nums :: [integer], k :: integer) :: integer
  def minimum_incompatibility(nums, k) do
    n = length(nums)
    m = div(n, k)

    freq =
      Enum.reduce(nums, %{}, fn v, acc ->
        Map.update(acc, v, 1, &(&1 + 1))
      end)

    if Enum.any?(freq, fn {_v, c} -> c > k end) do
      -1
    else
      import Bitwise

      full_mask = (1 <<< n) - 1

      groups =
        0..full_mask
        |> Enum.filter(fn mask -> Integer.popcnt(mask) == m end)
        |> Enum.reduce(%{}, fn mask, acc ->
          vals =
            for i <- 0..(n - 1), ((mask >>> i) &&& 1) == 1 do
              Enum.at(nums, i)
            end

          if length(Enum.uniq(vals)) == m do
            min_v = Enum.min(vals)
            max_v = Enum.max(vals)
            Map.put(acc, mask, max_v - min_v)
          else
            acc
          end
        end)

      dp =
        Enum.reduce(0..full_mask, %{0 => 0}, fn mask, dp_acc ->
          case Map.get(dp_acc, mask) do
            nil ->
              dp_acc

            cur ->
              Enum.reduce(groups, dp_acc, fn {gmask, cost}, dp2 ->
                if (gmask &&& mask) == 0 do
                  new_mask = gmask ||| mask
                  prev = Map.get(dp2, new_mask, :infinity)
                  new_val = cur + cost

                  if new_val < prev do
                    Map.put(dp2, new_mask, new_val)
                  else
                    dp2
                  end
                else
                  dp2
                end
              end)
          end
        end)

      Map.get(dp, full_mask, -1)
    end
  end
end
```

# 3098. Find the Sum of Subsequence Powers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sumOfPowers(vector<int>& nums, int k) {
        const long long MOD = 1000000007LL;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        
        // collect all distinct differences
        vector<long long> diffs;
        diffs.reserve(n * (n - 1) / 2);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                diffs.push_back((long long)nums[j] - nums[i]);
            }
        }
        sort(diffs.begin(), diffs.end());
        diffs.erase(unique(diffs.begin(), diffs.end()), diffs.end());
        int m = diffs.size();
        
        vector<long long> f(m, 0); // number of subsequences with min diff >= d
        
        for (int idx = 0; idx < m; ++idx) {
            long long d = diffs[idx];
            vector<vector<long long>> dp(k + 1, vector<long long>(n, 0));
            for (int i = 0; i < n; ++i) dp[1][i] = 1;
            for (int len = 2; len <= k; ++len) {
                for (int i = 0; i < n; ++i) {
                    long long sum = 0;
                    for (int p = 0; p < i; ++p) {
                        if ((long long)nums[i] - nums[p] >= d) {
                            sum += dp[len - 1][p];
                            if (sum >= MOD) sum -= MOD;
                        }
                    }
                    dp[len][i] = sum % MOD;
                }
            }
            long long total = 0;
            for (int i = 0; i < n; ++i) {
                total += dp[k][i];
                if (total >= MOD) total -= MOD;
            }
            f[idx] = total;
        }
        
        long long ans = 0;
        for (int idx = 0; idx < m; ++idx) {
            long long cnt = f[idx];
            if (idx + 1 < m) {
                cnt = (cnt - f[idx + 1] + MOD) % MOD;
            }
            long long contrib = (diffs[idx] % MOD) * cnt % MOD;
            ans += contrib;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    public int sumOfPowers(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);
        // collect all distinct differences including 0
        TreeSet<Long> diffSet = new TreeSet<>();
        diffSet.add(0L);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                diffSet.add((long) nums[j] - (long) nums[i]);
            }
        }
        Long[] diffs = diffSet.toArray(new Long[0]);
        int m = diffs.length;
        long[] countAtLeast = new long[m]; // C(diff)
        for (int idx = 0; idx < m; ++idx) {
            long D = diffs[idx];
            long[][] dp = new long[n][k + 1];
            for (int i = 0; i < n; ++i) {
                dp[i][1] = 1;
            }
            for (int len = 2; len <= k; ++len) {
                for (int i = 0; i < n; ++i) {
                    long sum = 0;
                    for (int j = 0; j < i; ++j) {
                        if ((long) nums[i] - (long) nums[j] >= D) {
                            sum += dp[j][len - 1];
                            if (sum >= MOD) sum -= MOD;
                        }
                    }
                    dp[i][len] = sum;
                }
            }
            long total = 0;
            for (int i = 0; i < n; ++i) {
                total += dp[i][k];
                if (total >= MOD) total -= MOD;
            }
            countAtLeast[idx] = total;
        }

        long answer = 0;
        for (int i = 0; i < m; ++i) {
            long higher = (i + 1 < m) ? countAtLeast[i + 1] : 0L;
            long cntExact = countAtLeast[i] - higher;
            if (cntExact < 0) cntExact += MOD;
            long contrib = (diffs[i] % MOD) * cntExact % MOD;
            answer += contrib;
            if (answer >= MOD) answer -= MOD;
        }
        return (int) (answer % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def sumOfPowers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        # collect all distinct gaps
        gaps_set = set()
        for i in range(n):
            for j in range(i+1, n):
                gaps_set.add(nums[j] - nums[i])
        gaps = sorted(gaps_set)

        def count_subsets(min_gap):
            # dp_len[l][i]: number of ways to pick l elements ending at i
            dp = [1] * n  # length 1
            for length in range(2, k+1):
                new_dp = [0] * n
                j = 0
                prefix = 0
                for i in range(n):
                    while j < i and nums[i] - nums[j] >= min_gap:
                        prefix = (prefix + dp[j]) % MOD
                        j += 1
                    new_dp[i] = prefix
                dp = new_dp
            return sum(dp) % MOD

        f_vals = {}
        for d in gaps:
            f_vals[d] = count_subsets(d)

        ans = 0
        m = len(gaps)
        for idx, cur in enumerate(gaps):
            nxt_val = f_vals[gaps[idx+1]] if idx + 1 < m else 0
            cnt_exact = (f_vals[cur] - nxt_val) % MOD
            ans = (ans + (cur % MOD) * cnt_exact) % MOD

        return ans
```

## Python3

```python
import sys
from typing import List

MOD = 10**9 + 7

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        n = len(a)

        # collect all possible positive differences
        diffs_set = set()
        for i in range(n):
            for j in range(i + 1, n):
                diffs_set.add(a[j] - a[i])
        diffs = [0] + sorted(diffs_set)  # include 0 as smallest threshold

        def count_ge(D: int) -> int:
            # dp_prev[c][i]: number of ways to pick c elements ending at i
            dp_prev = [1] * n  # for c = 1
            if k == 1:
                return n % MOD
            for cnt in range(2, k + 1):
                # prefix sums of dp_prev
                pref = [0] * n
                running = 0
                for i in range(n):
                    running += dp_prev[i]
                    if running >= MOD:
                        running -= MOD
                    pref[i] = running

                dp_curr = [0] * n
                left = 0
                for i in range(n):
                    while left < i and a[i] - a[left] >= D:
                        left += 1
                    limit = left - 1
                    if limit >= 0:
                        dp_curr[i] = pref[limit]
                dp_prev = dp_curr
            total = sum(dp_prev) % MOD
            return total

        counts = [count_ge(D) for D in diffs]

        ans = 0
        for i in range(len(diffs)):
            cur = counts[i]
            nxt = counts[i + 1] if i + 1 < len(counts) else 0
            diff_cnt = (cur - nxt) % MOD
            ans = (ans + (diffs[i] % MOD) * diff_cnt) % MOD

        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007LL

static long long count_subsets(long long *a, int n, int k, long long D) {
    static long long dp[55][55];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j <= k; ++j)
            dp[i][j] = 0;
    for (int i = 0; i < n; ++i) dp[i][1] = 1;
    for (int len = 2; len <= k; ++len) {
        for (int i = 0; i < n; ++i) {
            long long sum = 0;
            for (int j = 0; j < i; ++j) {
                if (a[i] - a[j] >= D) {
                    sum += dp[j][len-1];
                    if (sum >= MOD) sum -= MOD;
                }
            }
            dp[i][len] = sum % MOD;
        }
    }
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += dp[i][k];
        if (total >= MOD) total -= MOD;
    }
    return total % MOD;
}

int sumOfPowers(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long *a = (long long*)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; ++i) a[i] = nums[i];
    // sort
    for (int i = 1; i < n; ++i) {
        long long key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j+1] = a[j];
            --j;
        }
        a[j+1] = key;
    }

    // collect all distinct positive differences
    long long *diffs = (long long*)malloc(sizeof(long long) * n * n);
    int diffCnt = 0;
    for (int i = 0; i < n; ++i)
        for (int j = i+1; j < n; ++j)
            diffs[diffCnt++] = a[j] - a[i];
    // sort diffs
    for (int i = 1; i < diffCnt; ++i) {
        long long key = diffs[i];
        int j = i - 1;
        while (j >= 0 && diffs[j] > key) {
            diffs[j+1] = diffs[j];
            --j;
        }
        diffs[j+1] = key;
    }
    // unique
    int uniqCnt = 0;
    for (int i = 0; i < diffCnt; ++i) {
        if (i == 0 || diffs[i] != diffs[i-1]) {
            diffs[uniqCnt++] = diffs[i];
        }
    }

    long long ans = 0;
    long long prev = 0;
    for (int idx = 0; idx < uniqCnt; ++idx) {
        long long d = diffs[idx];
        long long f = count_subsets(a, n, k, d);
        long long diff = (d - prev) % MOD;
        if (diff < 0) diff += MOD;
        ans = (ans + f * diff) % MOD;
        prev = d;
    }

    free(a);
    free(diffs);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;
    
    public int SumOfPowers(int[] nums, int k) {
        int n = nums.Length;
        Array.Sort(nums);
        // collect distinct differences
        var diffSet = new HashSet<long>();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                diffSet.Add((long)nums[j] - nums[i]);
            }
        }
        var diffs = new List<long>(diffSet);
        diffs.Sort(); // ascending
        
        // DP counting function
        long CountWithMinGap(long D) {
            long[,] dp = new long[k + 1, n];
            for (int i = 0; i < n; ++i) dp[1, i] = 1;
            for (int len = 2; len <= k; ++len) {
                for (int i = 0; i < n; ++i) {
                    long sum = 0;
                    for (int j = 0; j < i; ++j) {
                        if ((long)nums[i] - nums[j] >= D) {
                            sum += dp[len - 1, j];
                            if (sum >= MOD) sum -= MOD;
                        }
                    }
                    dp[len, i] = sum;
                }
            }
            long total = 0;
            for (int i = 0; i < n; ++i) {
                total += dp[k, i];
                if (total >= MOD) total -= MOD;
            }
            return total;
        }
        
        // compute f(D) for each diff
        var fMap = new Dictionary<long, long>();
        foreach (var d in diffs) {
            fMap[d] = CountWithMinGap(d);
        }
        
        long ans = 0;
        long prevF = 0; // f of larger D already processed
        for (int idx = diffs.Count - 1; idx >= 0; --idx) {
            long d = diffs[idx];
            long curF = fMap[d];
            long cntExact = curF - prevF;
            if (cntExact < 0) cntExact += MOD;
            ans = (ans + (d % MOD) * cntExact) % MOD;
            prevF = curF;
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
var sumOfPowers = function(nums, k) {
    const MOD = 1000000007n;
    const n = nums.length;
    // sort numbers
    const a = nums.slice().sort((x, y) => x - y);
    // collect distinct differences including 0
    const diffSet = new Set();
    diffSet.add(0);
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            diffSet.add(a[j] - a[i]);
        }
    }
    const diffs = Array.from(diffSet).sort((x, y) => x - y);
    const m = diffs.length;
    // compute f(d) for each diff
    const fVals = new Array(m).fill(0n);
    for (let idx = 0; idx < m; ++idx) {
        const d = diffs[idx];
        // dp[c][i]: ways to pick c elements ending at i
        const dp = Array.from({ length: k + 1 }, () => new Array(n).fill(0n));
        for (let i = 0; i < n; ++i) dp[1][i] = 1n;
        for (let c = 2; c <= k; ++c) {
            for (let i = 0; i < n; ++i) {
                let sum = 0n;
                for (let p = 0; p < i; ++p) {
                    if (a[i] - a[p] >= d) {
                        sum += dp[c - 1][p];
                        if (sum >= MOD) sum -= MOD;
                    }
                }
                dp[c][i] = sum;
            }
        }
        let total = 0n;
        for (let i = 0; i < n; ++i) {
            total += dp[k][i];
            if (total >= MOD) total -= MOD;
        }
        fVals[idx] = total;
    }
    // compute answer using differences of consecutive f values
    let ans = 0n;
    for (let i = 0; i < m; ++i) {
        const next = i + 1 < m ? fVals[i + 1] : 0n;
        let exact = fVals[i] - next;
        if (exact < 0) exact += MOD;
        const diffBig = BigInt(diffs[i]) % MOD;
        ans = (ans + diffBig * exact) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function sumOfPowers(nums: number[], k: number): number {
    const MOD = 1000000007n;
    const arr = nums.slice().sort((a, b) => a - b);
    const n = arr.length;

    // collect all distinct absolute differences
    const diffSet = new Set<number>();
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            diffSet.add(arr[j] - arr[i]);
        }
    }
    const diffs = Array.from(diffSet).sort((a, b) => a - b);
    const m = diffs.length;

    function countAtLeast(D: number): bigint {
        const dp: bigint[][] = Array.from({ length: n }, () => Array(k + 1).fill(0n));
        for (let i = 0; i < n; ++i) dp[i][1] = 1n;
        for (let len = 2; len <= k; ++len) {
            for (let i = 0; i < n; ++i) {
                let sum = 0n;
                for (let prev = 0; prev < i; ++prev) {
                    if (arr[i] - arr[prev] >= D) {
                        sum += dp[prev][len - 1];
                    }
                }
                dp[i][len] = sum % MOD;
            }
        }
        let total = 0n;
        for (let i = 0; i < n; ++i) total = (total + dp[i][k]) % MOD;
        return total;
    }

    const fVals: bigint[] = new Array(m);
    for (let idx = 0; idx < m; ++idx) {
        fVals[idx] = countAtLeast(diffs[idx]);
    }

    let ans = 0n;
    for (let i = 0; i < m; ++i) {
        const next = i + 1 < m ? fVals[i + 1] : 0n;
        let cntExact = (fVals[i] - next) % MOD;
        if (cntExact < 0) cntExact += MOD;
        ans = (ans + cntExact * BigInt(diffs[i])) % MOD;
    }
    return Number(ans);
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
    function sumOfPowers($nums, $k) {
        $MOD = 1000000007;
        sort($nums);
        $n = count($nums);

        // collect all distinct differences
        $diffSet = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $d = $nums[$j] - $nums[$i];
                $diffSet[$d] = true;
            }
        }
        $diffs = array_keys($diffSet);
        sort($diffs); // ascending

        $cntGe = []; // diff => count of subsequences with min diff >= diff (mod MOD)

        foreach ($diffs as $D) {
            // dp[i][len]: number of ways ending at i with length len
            $dp = array_fill(0, $n, array_fill(0, $k + 1, 0));
            for ($i = 0; $i < $n; $i++) {
                $dp[$i][1] = 1;
            }
            for ($len = 2; $len <= $k; $len++) {
                for ($i = 0; $i < $n; $i++) {
                    $sum = 0;
                    for ($p = 0; $p < $i; $p++) {
                        if ($nums[$i] - $nums[$p] >= $D) {
                            $sum += $dp[$p][$len - 1];
                            if ($sum >= $MOD) $sum -= $MOD;
                        }
                    }
                    $dp[$i][$len] = $sum;
                }
            }
            $total = 0;
            for ($i = 0; $i < $n; $i++) {
                $total += $dp[$i][$k];
                if ($total >= $MOD) $total -= $MOD;
            }
            $cntGe[$D] = $total;
        }

        // compute exact counts and sum
        $ans = 0;
        $prevCount = 0; // count for larger diff
        for ($idx = count($diffs) - 1; $idx >= 0; $idx--) {
            $d = $diffs[$idx];
            $cnt = $cntGe[$d];
            $exact = $cnt - $prevCount;
            if ($exact < 0) $exact += $MOD;
            $ans = ($ans + ($exact * ($d % $MOD)) ) % $MOD;
            $prevCount = $cnt;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    let MOD = 1_000_000_007
    func sumOfPowers(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var a = nums.sorted()
        var diffSet = Set<Int>()
        for i in 0..<n {
            for j in i+1..<n {
                diffSet.insert(a[j] - a[i])
            }
        }
        var diffs = Array(diffSet)
        diffs.sort()
        func countAtLeast(_ minDiff: Int) -> Int {
            var nxt = [Int](repeating: n, count: n)
            var j = 0
            for i in 0..<n {
                if j <= i { j = i + 1 }
                while j < n && a[j] - a[i] < minDiff {
                    j += 1
                }
                nxt[i] = j
            }
            var dp = Array(repeating: Array(repeating: 0, count: k + 1), count: n + 1)
            for pos in stride(from: n, through: 0, by: -1) {
                dp[pos][0] = 1
                if pos == n { continue }
                for left in 1...k {
                    var ways = dp[pos + 1][left]
                    let nextIdx = nxt[pos]
                    if nextIdx <= n {
                        ways += dp[nextIdx][left - 1]
                        if ways >= MOD { ways -= MOD }
                    }
                    dp[pos][left] = ways % MOD
                }
            }
            return dp[0][k]
        }
        var counts = [Int]()
        for d in diffs {
            counts.append(countAtLeast(d))
        }
        var ans: Int64 = 0
        let m = diffs.count
        for i in 0..<m {
            let curDiff = diffs[i]
            let cntCur = counts[i]
            let cntNext = (i + 1 < m) ? counts[i + 1] : 0
            var exact = cntCur - cntNext
            if exact < 0 { exact += MOD }
            ans = (ans + Int64(curDiff % MOD) * Int64(exact)) % Int64(MOD)
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    fun sumOfPowers(nums: IntArray, k: Int): Int {
        val n = nums.size
        val sorted = nums.clone()
        Arrays.sort(sorted)

        // collect all distinct differences
        val diffSet = HashSet<Long>()
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                diffSet.add((sorted[j].toLong() - sorted[i]))
            }
        }
        val diffs = diffSet.toLongArray()
        Arrays.sort(diffs)

        // compute g(d) for each difference
        val gVals = LongArray(diffs.size)
        for (idx in diffs.indices) {
            gVals[idx] = countAtLeast(sorted, k, diffs[idx])
        }

        var ans = 0L
        for (i in diffs.indices) {
            val next = if (i + 1 < diffs.size) gVals[i + 1] else 0L
            var cntExact = gVals[i] - next
            if (cntExact < 0) cntExact += MOD
            ans = (ans + (cntExact % MOD) * (diffs[i] % MOD)) % MOD
        }
        return ans.toInt()
    }

    private fun countAtLeast(arr: IntArray, k: Int, d: Long): Long {
        val n = arr.size
        var dpPrev = LongArray(n) { 1L } // length 1 subsequences

        if (k == 1) return n.toLong() % MOD

        for (len in 2..k) {
            // prefix sums of dpPrev
            val prefix = LongArray(n)
            var sum = 0L
            for (i in 0 until n) {
                sum += dpPrev[i]
                if (sum >= MOD) sum -= MOD
                prefix[i] = sum
            }

            val dpCurr = LongArray(n)
            var lo = -1
            for (i in 0 until n) {
                while (lo + 1 < i && arr[i].toLong() - arr[lo + 1] >= d) {
                    lo++
                }
                if (lo >= 0) {
                    dpCurr[i] = prefix[lo]
                }
            }
            dpPrev = dpCurr
        }

        var total = 0L
        for (v in dpPrev) {
            total += v
            if (total >= MOD) total -= MOD
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int sumOfPowers(List<int> nums, int k) {
    nums.sort();
    int n = nums.length;
    // Collect all distinct differences
    Set<int> diffSet = {};
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        diffSet.add(nums[j] - nums[i]);
      }
    }
    List<int> diffs = diffSet.toList()..sort();

    // Map each difference to f(d): number of subsequences of length k with min gap >= d
    Map<int, int> fMap = {};
    for (int d in diffs) {
      fMap[d] = _countWithMinGapAtLeast(d, nums, k);
    }

    int prev = 0; // f value for larger difference (initially 0)
    int ans = 0;
    for (int idx = diffs.length - 1; idx >= 0; --idx) {
      int d = diffs[idx];
      int cur = fMap[d]!;
      int exact = cur - prev;
      if (exact < 0) exact += _mod;
      ans = (ans + (exact * (d % _mod)) % _mod) % _mod;
      prev = cur;
    }
    return ans;
  }

  int _countWithMinGapAtLeast(int d, List<int> a, int k) {
    int n = a.length;
    // dp[len][i]: ways to pick len elements ending at index i
    List<List<int>> dp = List.generate(k + 1, (_) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) dp[1][i] = 1;
    for (int len = 2; len <= k; ++len) {
      for (int i = 0; i < n; ++i) {
        int sum = 0;
        for (int prev = 0; prev < i; ++prev) {
          if (a[i] - a[prev] >= d) {
            sum += dp[len - 1][prev];
            if (sum >= _mod) sum -= _mod;
          }
        }
        dp[len][i] = sum;
      }
    }
    int total = 0;
    for (int i = 0; i < n; ++i) {
      total += dp[k][i];
      if (total >= _mod) total -= _mod;
    }
    return total;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

const MOD int = 1000000007

func sumOfPowers(nums []int, k int) int {
	n := len(nums)
	if k == 1 {
		return 0
	}
	sort.Ints(nums)
	a := make([]int64, n)
	for i, v := range nums {
		a[i] = int64(v)
	}

	// collect distinct differences
	diffMap := make(map[int64]struct{})
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			d := a[j] - a[i]
			diffMap[d] = struct{}{}
		}
	}
	diffs := make([]int64, 0, len(diffMap))
	for d := range diffMap {
		diffs = append(diffs, d)
	}
	sort.Slice(diffs, func(i, j int) bool { return diffs[i] < diffs[j] })

	// helper to count subsets of size k where all adjacent gaps >= D
	countGe := func(D int64) int {
		dp := make([][]int, n)
		for i := 0; i < n; i++ {
			row := make([]int, k+1)
			row[1] = 1
			dp[i] = row
		}
		for cnt := 2; cnt <= k; cnt++ {
			for i := 0; i < n; i++ {
				sum := 0
				for p := 0; p < i; p++ {
					if a[i]-a[p] >= D {
						sum += dp[p][cnt-1]
						if sum >= MOD {
							sum -= MOD
						}
					}
				}
				dp[i][cnt] = sum
			}
		}
		total := 0
		for i := 0; i < n; i++ {
			total += dp[i][k]
			if total >= MOD {
				total -= MOD
			}
		}
		return total
	}

	ans := int64(0)
	prevCount := 0 // count for larger D (already processed)

	for i := len(diffs) - 1; i >= 0; i-- {
		d := diffs[i]
		cnt := countGe(d)
		exact := cnt - prevCount
		if exact < 0 {
			exact += MOD
		}
		ans = (ans + (d%int64(MOD))*int64(exact)) % int64(MOD)
		prevCount = cnt
	}

	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e)
  res = 1
  a %= MOD
  while e > 0
    res = (res * a) % MOD if (e & 1) == 1
    a = (a * a) % MOD
    e >>= 1
  end
  res
end

def comb(n, k, fact, inv_fact)
  return 0 if k < 0 || k > n
  ((fact[n] * inv_fact[k]) % MOD) * inv_fact[n - k] % MOD
end

def count_gt(limit, arr, n, k)
  dp = Array.new(n) { Array.new(k + 1, 0) }
  (0...n).each do |i|
    dp[i][1] = 1
    (2..k).each do |c|
      sum = 0
      (0...i).each do |j|
        if arr[i] - arr[j] > limit
          sum += dp[j][c - 1]
        end
      end
      dp[i][c] = sum % MOD
    end
  end
  total = 0
  (0...n).each { |i| total = (total + dp[i][k]) % MOD }
  total
end

def sum_of_powers(nums, k)
  arr = nums.sort
  n = arr.length

  # precompute factorials for combinations
  fact = Array.new(n + 1, 1)
  (1..n).each { |i| fact[i] = (fact[i - 1] * i) % MOD }
  inv_fact = Array.new(n + 1, 1)
  inv_fact[n] = mod_pow(fact[n], MOD - 2)
  (n - 1).downto(0) { |i| inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD }

  total_subsets = comb(n, k, fact, inv_fact)

  diffs = []
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      diffs << arr[j] - arr[i]
    end
  end
  diffs.uniq!
  diffs.sort!

  prev_cnt = total_subsets
  ans = 0

  diffs.each do |d|
    cnt = count_gt(d, arr, n, k)
    ways_eq = (prev_cnt - cnt) % MOD
    ans = (ans + (d % MOD) * ways_eq) % MOD
    prev_cnt = cnt
  end

  ans % MOD
end
```

## Scala

```scala
object Solution {
  val MOD = 1000000007L

  def sumOfPowers(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val a = nums.sorted.map(_.toLong)

    // collect distinct differences
    val diffSet = scala.collection.mutable.HashSet[Long]()
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        diffSet += a(j) - a(i)
        j += 1
      }
      i += 1
    }
    val diffs = diffSet.toArray.sorted

    // count subsequences of length k with all adjacent gaps >= d
    def countAtLeast(d: Long): Long = {
      if (k == 1) return n % MOD
      var prev = Array.fill[Long](n)(1L) // len = 1
      var curr = new Array[Long](n)
      var len = 2
      while (len <= k) {
        // prefix sums of prev
        val pref = new Array[Long](n)
        var sum = 0L
        var idx = 0
        while (idx < n) {
          sum += prev(idx)
          if (sum >= MOD) sum -= MOD
          pref(idx) = sum
          idx += 1
        }
        java.util.Arrays.fill(curr, 0L)

        var jIdx = 0
        while (jIdx < n) {
          val target = a(jIdx) - d
          // binary search for largest index <= target among [0, jIdx-1]
          var lo = 0
          var hi = jIdx - 1
          var pos = -1
          while (lo <= hi) {
            val mid = (lo + hi) >>> 1
            if (a(mid) <= target) {
              pos = mid
              lo = mid + 1
            } else {
              hi = mid - 1
            }
          }
          if (pos >= 0) curr(jIdx) = pref(pos)
          jIdx += 1
        }

        // swap prev and curr for next length
        val tmp = prev
        prev = curr
        curr = tmp
        len += 1
      }

      var total = 0L
      var idx2 = 0
      while (idx2 < n) {
        total += prev(idx2)
        if (total >= MOD) total -= MOD
        idx2 += 1
      }
      total % MOD
    }

    // compute f(d) for each distinct difference
    val fVals = new Array[Long](diffs.length)
    var di = 0
    while (di < diffs.length) {
      fVals(di) = countAtLeast(diffs(di))
      di += 1
    }

    // sum contributions where min diff equals exactly d
    var ans = 0L
    var prevCount = 0L
    var idxDesc = diffs.length - 1
    while (idxDesc >= 0) {
      val cur = fVals(idxDesc)
      var exact = cur - prevCount
      if (exact < 0) exact += MOD
      ans = (ans + exact * (diffs(idxDesc) % MOD)) % MOD
      prevCount = cur
      idxDesc -= 1
    }
    ans.toInt
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res: i64 = 1;
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
    pub fn sum_of_powers(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_usize = k as usize;
        if k_usize == 0 || n < k_usize {
            return 0;
        }

        // sort numbers
        let mut a: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        a.sort_unstable();

        // precompute factorials for total combinations (optional, not directly used)
        let mut fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        let mut inv_fact = vec![1i64; n + 1];
        inv_fact[n] = mod_pow(fact[n], MOD - 2);
        for i in (0..n).rev() {
            inv_fact[i] = inv_fact[i + 1] * ((i + 1) as i64) % MOD;
        }

        // total subsequences of length k (used only for verification)
        let _total_subseq = fact[n] * inv_fact[k_usize] % MOD * inv_fact[n - k_usize] % MOD;

        // collect all distinct positive differences
        let mut diffs: Vec<i64> = Vec::new();
        for i in 0..n {
            for j in (i + 1)..n {
                diffs.push(a[j] - a[i]);
            }
        }
        diffs.sort_unstable();
        diffs.dedup();

        // function to count subsequences of length k with adjacent gaps >= diff
        let mut count_cache: std::collections::HashMap<i64, i64> = std::collections::HashMap::new();
        let count_subseq = |diff: i64,
                            a: &Vec<i64>,
                            n: usize,
                            k_usize: usize,
                            cache: &mut std::collections::HashMap<i64, i64>| -> i64 {
            if let Some(&v) = cache.get(&diff) {
                return v;
            }
            // dp for length 1
            let mut dp_prev = vec![1i64; n];
            for len in 2..=k_usize {
                let mut dp_cur = vec![0i64; n];
                for i in 0..n {
                    let mut sum = 0i64;
                    for j in 0..i {
                        if a[i] - a[j] >= diff {
                            sum += dp_prev[j];
                            if sum >= MOD {
                                sum -= MOD;
                            }
                        }
                    }
                    dp_cur[i] = sum;
                }
                dp_prev = dp_cur;
            }
            let mut total = 0i64;
            for &v in &dp_prev {
                total += v;
                if total >= MOD {
                    total -= MOD;
                }
            }
            cache.insert(diff, total);
            total
        };

        // compute answer using telescoping sum
        let mut ans: i64 = 0;
        let mut prev_diff: i64 = 0;
        for &cur_diff in diffs.iter() {
            let g_cur = count_subseq(cur_diff, &a, n, k_usize, &mut count_cache);
            let range = (cur_diff - prev_diff) % MOD;
            ans = (ans + range * g_cur % MOD) % MOD;
            prev_diff = cur_diff;
        }

        // result modulo MOD fits in i32
        ((ans % MOD + MOD) % MOD) as i32
    }
}
```

## Racket

```racket
(define (sum-of-powers nums k)
  (let* ((mod 1000000007)
         (sorted (list->vector (sort nums <)))
         (n (vector-length sorted))
         ;; collect all pairwise differences
         (diffs
          (let loop ((i 0) (j 1) (acc '()))
            (if (>= i n)
                acc
                (if (< j n)
                    (loop i (+ j 1)
                          (cons (- (vector-ref sorted j) (vector-ref sorted i)) acc))
                    (loop (+ i 1) (+ i 2) acc)))))
         (unique-diffs (remove-duplicates (sort diffs <)))
         ;; sentinel for values larger than any possible difference
         (max-diff (if (null? unique-diffs) 0 (car (reverse unique-diffs))))
         (thresholds (append unique-diffs (list (+ max-diff 1)))))
    ;; DP to count subsets of size k with adjacent gaps >= min-gap
    (define (count-with-min-gap min-gap)
      (let ((dp (make-vector n)))
        (for ([i (in-range n)])
          (vector-set! dp i (make-vector (+ k 1) 0))
          (vector-set! (vector-ref dp i) 1 1)) ; length‑1 subsets
        (for ([len (in-range 2 (+ k 1))])
          (for ([i (in-range n)])
            (let ((sum 0))
              (for ([p (in-range i)])
                (when (>= (- (vector-ref sorted i) (vector-ref sorted p)) min-gap)
                  (set! sum (+ sum (vector-ref (vector-ref dp p) (- len 1))))))
              (vector-set! (vector-ref dp i) len (modulo sum mod)))))
        (let ((total 0))
          (for ([i (in-range n)])
            (set! total (modulo (+ total (vector-ref (vector-ref dp i) k)) mod)))
          total)))
    ;; compute counts for each threshold
    (define g-values (map count-with-min-gap thresholds))
    ;; accumulate answer using differences between successive counts
    (let loop ((idx 0) (ans 0))
      (if (>= idx (sub1 (length thresholds))) ; reached sentinel
          ans
          (let* ((v (list-ref unique-diffs idx))
                 (cnt (- (list-ref g-values idx) (list-ref g-values (+ idx 1))))
                 (cnt-mod (modulo cnt mod))
                 (ans2 (modulo (+ ans (modulo (* (modulo v mod) cnt-mod) mod)) mod)))
            (loop (+ idx 1) ans2))))))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec sum_of_powers(Nums :: [integer()], K :: integer()) -> integer().
sum_of_powers(Nums, K) ->
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    DiffList = [
        (lists:nth(J, Sorted) - lists:nth(I, Sorted))
        || I <- lists:seq(1, N-1), J <- lists:seq(I+1, N)
    ],
    Diffs = ordsets:to_list(ordsets:from_list(DiffList)),
    {Ans, _} =
        lists:foldl(
            fun(Diff, {AccAns, PrevGe}) ->
                Ge = count_ge(Diff, Sorted, K),
                Exact = (Ge - PrevGe + ?MOD) rem ?MOD,
                DiffMod = ((Diff rem ?MOD) + ?MOD) rem ?MOD,
                NewAns = (AccAns + DiffMod * Exact) rem ?MOD,
                {NewAns, Ge}
            end,
            {0, 0},
            lists:reverse(Diffs)
        ),
    Ans.

%% count of subsequences of length K where every consecutive gap >= Diff
-spec count_ge(integer(), [integer()], integer()) -> integer().
count_ge(Diff, Sorted, K) ->
    N = length(Sorted),
    {Total, _DPAcc} =
        lists:foldl(
            fun(Idx, {Tot, DPAcc}) ->
                Val = lists:nth(Idx, Sorted),
                CurrMap = make_curr(Idx, Val, Sorted, Diff, K, DPAcc),
                NewTot = (Tot + maps:get(K, CurrMap, 0)) rem ?MOD,
                {NewTot, DPAcc ++ [CurrMap]}
            end,
            {0, []},
            lists:seq(1, N)
        ),
    Total.

%% build map for position Idx (1‑based) containing counts for each length
-spec make_curr(integer(), integer(), [integer()], integer(), integer(),
                [map()]) -> map().
make_curr(Idx, Val, Sorted, Diff, K, DPAcc) ->
    BaseMap = maps:from_list([{1, 1}]),
    lists:foldl(
        fun(Len, AccMap) ->
            Sum = sum_prev(Idx, Val, Diff, Len - 1, Sorted, DPAcc),
            maps:put(Len, Sum rem ?MOD, AccMap)
        end,
        BaseMap,
        lists:seq(2, K)
    ).

%% sum over previous positions satisfying the gap condition
-spec sum_prev(integer(), integer(), integer(), integer(),
              [integer()], [map()]) -> integer().
sum_prev(CurIdx, CurVal, Diff, PrevLen, Sorted, DPAcc) ->
    lists:foldl(
        fun(J, Acc) ->
            PrevVal = lists:nth(J, Sorted),
            case CurVal - PrevVal >= Diff of
                true ->
                    PrevMap = lists:nth(J, DPAcc),
                    (Acc + maps:get(PrevLen, PrevMap, 0)) rem ?MOD;
                false -> Acc
            end
        end,
        0,
        lists:seq(1, CurIdx - 1)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec sum_of_powers(nums :: [integer], k :: integer) :: integer
  def sum_of_powers(nums, k) do
    a = Enum.sort(nums)
    n = length(a)

    # total subsets C(n,k)
    fac = factorials(n)
    inv_fac = inv_factorials(fac, n)
    total_subsets = comb(fac, inv_fac, n, k)

    # collect all distinct differences including 0
    diffs_set =
      Enum.reduce(0..(n - 1), MapSet.new([0]), fn i, set ->
        Enum.reduce((i + 1)..(n - 1), set, fn j, s ->
          MapSet.put(s, Enum.at(a, j) - Enum.at(a, i))
        end)
      end)

    diffs = diffs_set |> MapSet.to_list() |> Enum.sort()

    f_vals =
      Enum.map(diffs, fn d ->
        compute_f(a, n, k, d)
      end)

    # calculate exact counts and sum
    {ans, _} =
      Enum.reduce(Enum.with_index(diffs), {0, nil}, fn {d, idx}, {acc, _prev_exact} ->
        f_cur = Enum.at(f_vals, idx)
        f_next = if idx + 1 < length(f_vals), do: Enum.at(f_vals, idx + 1), else: 0
        exact = (f_cur - f_next) |> mod()
        new_acc = (acc + d * exact) |> mod()
        {new_acc, exact}
      end)

    ans
  end

  # compute number of k-length subsequences with all adjacent gaps >= d
  defp compute_f(a, n, k, d) do
    # pre[cnt][i] = cumulative sum of dp values for count cnt up to index i (inclusive)
    pre =
      for _ <- 0..k do
        List.duplicate(0, n)
      end

    pre =
      Enum.reduce(0..(n - 1), pre, fn i, pre_acc ->
        # position of the rightmost element <= a[i] - d among indices < i
        limit = Enum.at(a, i) - d
        pos = find_pos(a, i, limit)

        dp_i =
          List.duplicate(0, k + 1)
          |> List.replace_at(1, 1)
          |> Enum.reduce(2..k, fn cnt, dp_acc ->
            val = if pos >= 0, do: Enum.at(Enum.at(pre_acc, cnt - 1), pos), else: 0
            List.replace_at(dp_acc, cnt, val)
          end)

        # update pre arrays with new cumulative sums
        Enum.reduce(1..k, pre_acc, fn cnt, pre2 ->
          prev = if i == 0, do: 0, else: Enum.at(Enum.at(pre2, cnt), i - 1)
          new_val = (prev + Enum.at(dp_i, cnt)) |> mod()
          updated_cnt_list = List.replace_at(Enum.at(pre2, cnt), i, new_val)
          List.replace_at(pre2, cnt, updated_cnt_list)
        end)
      end)

    # total ways is the last element of pre[k]
    Enum.at(Enum.at(pre, k), n - 1) |> mod()
  end

  # binary search: largest index < hi with a[idx] <= limit
  defp find_pos(a, hi, limit) do
    find_pos_rec(a, 0, hi - 1, limit, -1)
  end

  defp find_pos_rec(_a, low, high, _limit, res) when low > high, do: res

  defp find_pos_rec(a, low, high, limit, _res) do
    mid = div(low + high, 2)
    val = Enum.at(a, mid)

    if val <= limit do
      find_pos_rec(a, mid + 1, high, limit, mid)
    else
      find_pos_rec(a, low, mid - 1, limit, -1)
    end
  end

  # factorials up to n
  defp factorials(n) do
    Enum.reduce(0..n, [1], fn i, acc ->
      [Enum.at(acc, -1) * i |> mod() | acc]
    end)
    |> Enum.reverse()
  end

  # inverse factorials using Fermat's little theorem
  defp inv_factorials(fac, n) do
    inv_n = pow_mod(Enum.at(fac, n), @mod - 2)
    {inv_list, _} =
      Enum.reduce((n)..0, {[inv_n], inv_n}, fn i, {list, prev_inv} ->
        if i == 0 do
          {[prev_inv | list], prev_inv}
        else
          cur = (prev_inv * i) |> mod()
          {[cur | list], cur}
        end
      end)

    Enum.reverse(inv_list)
  end

  defp comb(fac, inv_fac, n, k) when k < 0 or k > n, do: 0

  defp comb(fac, inv_fac, _n, k) do
    ((Enum.at(fac, length(fac) - 1) *
        Enum.at(inv_fac, k) |> mod()) *
       Enum.at(inv_fac, length(fac) - 1 - k)) |> mod()
  end

  defp pow_mod(_base, 0), do: 1

  defp pow_mod(base, exp) when rem(exp, 2) == 1 do
    (base * pow_mod(base, exp - 1)) |> mod()
  end

  defp pow_mod(base, exp) do
    half = pow_mod(base, div(exp, 2))
    (half * half) |> mod()
  end

  defp mod(x), do: rem(rem(x, @mod) + @mod, @mod)
end
```

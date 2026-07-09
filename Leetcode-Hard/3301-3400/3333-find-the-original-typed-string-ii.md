# 3333. Find the Original Typed String II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int possibleStringCount(string word, int k) {
        const int MOD = 1'000'000'007;
        // compute run lengths
        vector<int> freq;
        for (int i = 0, n = word.size(); i < n; ) {
            int j = i;
            while (j < n && word[j] == word[i]) ++j;
            freq.push_back(j - i);
            i = j;
        }
        int m = freq.size();
        long long totalAll = 1;
        for (int p : freq) totalAll = totalAll * p % MOD;

        // if minimal length already >= k, all strings are valid
        if (m >= k) return (int)totalAll;
        // if maximal possible length < k, answer is 0
        if ((int)word.size() < k) return 0;

        // DP for lengths up to k-1
        vector<int> dp(k, 0), ndp(k, 0);
        dp[0] = 1; // empty before processing any runs

        for (int p : freq) {
            // prefix sums of previous dp
            vector<int> pref(k, 0);
            pref[0] = dp[0];
            for (int i = 1; i < k; ++i) {
                int val = dp[i];
                pref[i] = pref[i-1] + val;
                if (pref[i] >= MOD) pref[i] -= MOD;
            }
            // compute ndp
            fill(ndp.begin(), ndp.end(), 0);
            for (int len = 1; len < k; ++len) {
                long long ways = pref[len-1];
                int leftIdx = len - p - 1;
                if (leftIdx >= 0) {
                    ways -= pref[leftIdx];
                    if (ways < 0) ways += MOD;
                }
                ndp[len] = (int)ways;
            }
            dp.swap(ndp);
        }

        long long sumLess = 0;
        for (int len = 1; len < k; ++len) {
            sumLess += dp[len];
            if (sumLess >= MOD) sumLess -= MOD;
        }

        long long ans = totalAll - sumLess;
        ans %= MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    public int possibleStringCount(String word, int k) {
        // collect run lengths
        List<Integer> runs = new ArrayList<>();
        int n = word.length();
        int i = 0;
        while (i < n) {
            char c = word.charAt(i);
            int j = i;
            while (j < n && word.charAt(j) == c) j++;
            runs.add(j - i);
            i = j;
        }
        int m = runs.size();
        long totalWays = 1L;
        for (int len : runs) {
            totalWays = (totalWays * len) % MOD;
        }
        if (m >= k) {
            return (int) totalWays;
        }
        // DP for lengths up to k-1
        int[] dp = new int[k];
        dp[0] = 1; // empty before processing any run
        for (int len : runs) {
            int[] pref = new int[k];
            pref[0] = dp[0];
            for (int t = 1; t < k; ++t) {
                int sum = pref[t - 1] + dp[t];
                if (sum >= MOD) sum -= MOD;
                pref[t] = sum;
            }
            int[] ndp = new int[k];
            // ndp[0] stays 0 because each run contributes at least one character
            for (int t = 1; t < k; ++t) {
                long val = pref[t - 1];
                int leftIdx = t - len - 1;
                if (leftIdx >= 0) {
                    val -= pref[leftIdx];
                }
                val %= MOD;
                if (val < 0) val += MOD;
                ndp[t] = (int) val;
            }
            dp = ndp;
        }
        long sumLessK = 0;
        for (int t = 1; t < k; ++t) {
            sumLessK += dp[t];
            if (sumLessK >= MOD) sumLessK -= MOD;
        }
        long ans = totalWays - sumLessK;
        ans %= MOD;
        if (ans < 0) ans += MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def possibleStringCount(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # compute run lengths
        freq = []
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            freq.append(j - i)
            i = j

        m = len(freq)

        # total number of possible original strings (any length)
        total = 1
        for p in freq:
            total = (total * p) % MOD

        # if minimal possible length already >= k, all are valid
        if m >= k:
            return total

        limit = k - 1  # we need counts for lengths <= limit
        dp_prev = [0] * (limit + 1)
        dp_prev[0] = 1  # empty string using zero runs

        for p in freq:
            # prefix sums of previous dp
            pref = [0] * (limit + 1)
            cur_sum = 0
            for idx in range(limit + 1):
                cur_sum += dp_prev[idx]
                if cur_sum >= MOD:
                    cur_sum -= MOD
                pref[idx] = cur_sum

            dp_curr = [0] * (limit + 1)
            # compute new dp using prefix sums
            for length in range(1, limit + 1):
                left = length - 1
                right = length - p - 1
                val = pref[left]
                if right >= 0:
                    val -= pref[right]
                dp_curr[length] = val % MOD
            dp_prev = dp_curr

        # sum ways with total length <= limit (and at least 1)
        small_sum = sum(dp_prev[1:]) % MOD

        ans = (total - small_sum) % MOD
        return ans
```

## Python3

```python
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        # compute run lengths
        runs = []
        cnt = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                cnt += 1
            else:
                runs.append(cnt)
                cnt = 1
        runs.append(cnt)

        m = len(runs)

        # total number of possible strings (any length)
        total = 1
        for p in runs:
            total = (total * p) % MOD

        # if minimal possible length already >= k, all are valid
        if m >= k:
            return total

        max_len = k - 1  # we need counts for lengths <= k-1
        dp = [0] * (max_len + 1)
        dp[0] = 1  # empty prefix before processing any run

        for p in runs:
            # prefix sums of current dp
            pref = [0] * (max_len + 1)
            s = 0
            for i in range(max_len + 1):
                s += dp[i]
                if s >= MOD:
                    s -= MOD
                pref[i] = s

            newdp = [0] * (max_len + 1)
            # length must be at least 1 after using this run, so start from j=1
            for j in range(1, max_len + 1):
                left = j - p
                if left <= 0:
                    total_sum = pref[j-1]
                else:
                    total_sum = pref[j-1] - pref[left-1]
                newdp[j] = total_sum % MOD
            dp = newdp

        small = sum(dp) % MOD  # ways with length <= k-1
        ans = (total - small) % MOD
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int possibleStringCount(char* word, int k) {
    const int MOD = 1000000007;
    int n = strlen(word);
    int *runs = (int*)malloc(n * sizeof(int));
    int m = 0;
    for (int i = 0; i < n; ) {
        char c = word[i];
        int j = i;
        while (j < n && word[j] == c) ++j;
        runs[m++] = j - i;
        i = j;
    }

    long long totalWays = 1;
    for (int i = 0; i < m; ++i) {
        totalWays = (totalWays * runs[i]) % MOD;
    }

    if (m >= k) {
        free(runs);
        return (int)totalWays;
    }

    int limitRuns = m;
    if (limitRuns > k - 1) limitRuns = k - 1;

    int K = k; // we need indices 0..k-1
    int *dp = (int*)calloc(K, sizeof(int));
    int *newdp = (int*)calloc(K, sizeof(int));
    int *pref = (int*)malloc(K * sizeof(int));

    dp[0] = 1;
    for (int idx = 0; idx < limitRuns; ++idx) {
        pref[0] = dp[0];
        for (int j = 1; j < K; ++j) {
            int sum = pref[j - 1] + dp[j];
            if (sum >= MOD) sum -= MOD;
            pref[j] = sum;
        }
        memset(newdp, 0, K * sizeof(int));
        int p = runs[idx];
        for (int t = 1; t < K; ++t) {
            int left = t - p;
            if (left < 0) left = 0;
            long long val = pref[t - 1];
            if (left - 1 >= 0) {
                val -= pref[left - 1];
                if (val < 0) val += MOD;
            }
            newdp[t] = (int)val;
        }
        int *tmp = dp; dp = newdp; newdp = tmp;
    }

    long long smallWays = 0;
    for (int j = 0; j < K; ++j) {
        smallWays += dp[j];
        if (smallWays >= MOD) smallWays -= MOD;
    }

    long long ans = totalWays - smallWays;
    ans %= MOD;
    if (ans < 0) ans += MOD;

    free(runs);
    free(dp);
    free(newdp);
    free(pref);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1_000_000_007;
    public int PossibleStringCount(string word, int k) {
        // Compute run lengths
        List<int> freq = new List<int>();
        int n = word.Length;
        int i = 0;
        while (i < n) {
            char c = word[i];
            int cnt = 0;
            while (i < n && word[i] == c) {
                cnt++;
                i++;
            }
            freq.Add(cnt);
        }

        // Total number of possible original strings
        long totalWays = 1;
        foreach (int p in freq) {
            totalWays = (totalWays * p) % MOD;
        }

        int m = freq.Count;
        if (m >= k) {
            return (int)totalWays;
        }

        int limit = k - 1; // we need counts for lengths <= k-1
        int[] dp = new int[limit + 1];
        dp[0] = 1;

        foreach (int p in freq) {
            int[] pref = new int[limit + 1];
            pref[0] = dp[0];
            for (int j = 1; j <= limit; ++j) {
                int sum = pref[j - 1] + dp[j];
                if (sum >= MOD) sum -= MOD;
                pref[j] = sum;
            }

            int[] ndp = new int[limit + 1];
            for (int len = 1; len <= limit; ++len) {
                long val = pref[len - 1];
                int idx = len - p - 1;
                if (idx >= 0) {
                    val -= pref[idx];
                }
                val %= MOD;
                if (val < 0) val += MOD;
                ndp[len] = (int)val;
            }
            dp = ndp;
        }

        long smallSum = 0;
        for (int len = 1; len <= limit; ++len) {
            smallSum += dp[len];
            if (smallSum >= MOD) smallSum -= MOD;
        }

        long ans = totalWays - smallSum;
        ans %= MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var possibleStringCount = function(word, k) {
    const MOD_BIG = 1000000007n;
    const MOD = 1000000007;

    // Compute run lengths
    const runs = [];
    let i = 0;
    const n = word.length;
    while (i < n) {
        let j = i + 1;
        while (j < n && word[j] === word[i]) j++;
        runs.push(j - i);
        i = j;
    }
    const m = runs.length;

    // Total number of possible strings (product of run lengths) modulo MOD
    let totalBig = 1n;
    for (const len of runs) {
        totalBig = (totalBig * BigInt(len)) % MOD_BIG;
    }
    const totalWays = Number(totalBig); // now < MOD, safe as Number

    // If minimal length already >= k, all strings satisfy condition
    if (m >= k) return totalWays;

    // DP for lengths up to k-1
    const limit = k; // we need indices 0..k-1
    let dpPrev = new Array(limit).fill(0);
    dpPrev[0] = 1; // empty prefix before any runs

    for (const p of runs) {
        // Prefix sums of previous DP row
        const pref = new Array(limit).fill(0);
        pref[0] = dpPrev[0];
        for (let idx = 1; idx < limit; ++idx) {
            let val = pref[idx - 1] + dpPrev[idx];
            if (val >= MOD) val -= MOD;
            pref[idx] = val;
        }

        const dpCurr = new Array(limit).fill(0);
        for (let len = 0; len < limit; ++len) {
            // Need at least one character from this run
            const left = len - 1;
            if (left < 0) continue; // cannot achieve length len with this run yet
            let total = pref[left];
            const rightIdx = len - p - 1;
            if (rightIdx >= 0) {
                total -= pref[rightIdx];
                if (total < 0) total += MOD;
            }
            dpCurr[len] = total;
        }
        dpPrev = dpCurr;
    }

    // Sum ways with length < k
    let sumLessK = 0;
    for (let len = 0; len < limit; ++len) {
        sumLessK += dpPrev[len];
        if (sumLessK >= MOD) sumLessK -= MOD;
    }

    let ans = totalWays - sumLessK;
    ans %= MOD;
    if (ans < 0) ans += MOD;
    return ans;
};
```

## Typescript

```typescript
function possibleStringCount(word: string, k: number): number {
    const MOD = 1000000007;
    // Compute run lengths
    const freq: number[] = [];
    let i = 0;
    while (i < word.length) {
        let j = i;
        while (j < word.length && word[j] === word[i]) j++;
        freq.push(j - i);
        i = j;
    }
    const m = freq.length;

    // Total number of possible original strings
    let total = 1;
    for (const p of freq) {
        total = (total * p) % MOD;
    }

    // If minimal length already >= k, all strings are valid
    if (m >= k) return total;

    const limit = k - 1; // we need lengths up to k-1
    let dp = new Array(limit + 1).fill(0);
    dp[0] = 1; // empty prefix

    for (const p of freq) {
        const pref = new Array(limit + 1).fill(0);
        pref[0] = dp[0];
        for (let t = 1; t <= limit; ++t) {
            pref[t] = (pref[t - 1] + dp[t]) % MOD;
        }
        const ndp = new Array(limit + 1).fill(0);
        for (let t = 1; t <= limit; ++t) {
            let low = t - p;
            if (low < 0) low = 0;
            let val = pref[t - 1];
            if (low - 1 >= 0) {
                val -= pref[low - 1];
                if (val < 0) val += MOD;
            }
            ndp[t] = val;
        }
        dp = ndp;
    }

    // Sum ways with length <= k-1
    let small = 0;
    for (let t = 1; t <= limit; ++t) {
        small = (small + dp[t]) % MOD;
    }

    let ans = total - small;
    ans %= MOD;
    if (ans < 0) ans += MOD;
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function possibleStringCount($word, $k) {
        $MOD = 1000000007;
        $n = strlen($word);
        if ($n == 0) return 0;

        // Build run lengths
        $freq = [];
        $cnt = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($word[$i] === $word[$i - 1]) {
                $cnt++;
            } else {
                $freq[] = $cnt;
                $cnt = 1;
            }
        }
        $freq[] = $cnt;

        // Total number of possible original strings
        $totalProd = 1;
        foreach ($freq as $p) {
            $totalProd = ($totalProd * $p) % $MOD;
        }

        $m = count($freq);
        if ($m >= $k) {
            return (int)$totalProd;
        }

        // DP for lengths <= k-1
        $limit = $k - 1; // maximum length we care about
        $dp = array_fill(0, $limit + 1, 0);
        $dp[0] = 1; // empty prefix before processing any run

        foreach ($freq as $p) {
            // Prefix sums of previous dp
            $prefix = array_fill(0, $limit + 1, 0);
            $sum = 0;
            for ($j = 0; $j <= $limit; $j++) {
                $sum += $dp[$j];
                if ($sum >= $MOD) $sum -= $MOD;
                $prefix[$j] = $sum;
            }

            // New dp after including this run
            $new = array_fill(0, $limit + 1, 0);
            for ($j = 1; $j <= $limit; $j++) {
                $leftIdx = $j - 1;
                $rightIdx = $j - $p - 1;

                $val = $prefix[$leftIdx];
                if ($rightIdx >= 0) {
                    $val -= $prefix[$rightIdx];
                    if ($val < 0) $val += $MOD;
                }
                $new[$j] = $val;
            }
            // After processing at least one run, length 0 is impossible
            $dp = $new;
        }

        // Sum ways with total length <= k-1
        $shortWays = 0;
        for ($j = 0; $j <= $limit; $j++) {
            $shortWays += $dp[$j];
            if ($shortWays >= $MOD) $shortWays -= $MOD;
        }

        $ans = $totalProd - $shortWays;
        $ans %= $MOD;
        if ($ans < 0) $ans += $MOD;

        return (int)$ans;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func possibleStringCount(_ word: String, _ k: Int) -> Int {
        // Build run lengths
        var freq = [Int]()
        var prev: UInt8? = nil
        var cnt = 0
        for c in word.utf8 {
            if let p = prev {
                if c == p {
                    cnt += 1
                } else {
                    freq.append(cnt)
                    cnt = 1
                    prev = c
                }
            } else {
                prev = c
                cnt = 1
            }
        }
        if cnt > 0 { freq.append(cnt) }

        // Total number of possible strings (product of run lengths)
        var totalWays = 1
        for p in freq {
            totalWays = Int((Int64(totalWays) * Int64(p)) % Int64(MOD))
        }

        let m = freq.count
        if k <= 0 { return totalWays } // not needed per constraints
        if m >= k {
            return totalWays
        }

        let maxLen = k - 1
        var dp = [Int](repeating: 0, count: maxLen + 1)
        dp[0] = 1

        for p in freq {
            // prefix sums of previous dp
            var prefix = [Int](repeating: 0, count: maxLen + 1)
            var sum = 0
            for i in 0...maxLen {
                sum += dp[i]
                if sum >= MOD { sum -= MOD }
                prefix[i] = sum
            }

            var newdp = [Int](repeating: 0, count: maxLen + 1)

            if p > maxLen {
                // left bound always <= 0
                for j in 1...maxLen {
                    newdp[j] = prefix[j - 1]
                }
            } else {
                for j in 1...maxLen {
                    let left = j - p
                    var val = prefix[j - 1]
                    if left > 0 {
                        val -= prefix[left - 1]
                        if val < 0 { val += MOD }
                    }
                    newdp[j] = val
                }
            }

            dp = newdp
        }

        // Sum ways with length <= k-1
        var smallWays = 0
        for v in dp {
            smallWays += v
            if smallWays >= MOD { smallWays -= MOD }
        }

        var ans = totalWays - smallWays
        if ans < 0 { ans += MOD }
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L

    fun possibleStringCount(word: String, k: Int): Int {
        // compute run lengths
        val runs = ArrayList<Int>()
        var i = 0
        val n = word.length
        while (i < n) {
            var j = i
            while (j < n && word[j] == word[i]) j++
            runs.add(j - i)
            i = j
        }

        // total number of possible original strings (any length)
        var total = 1L
        for (len in runs) {
            total = (total * len) % MOD
        }

        if (runs.size >= k) {
            return total.toInt()
        }

        val limit = k - 1 // we need counts for lengths < k
        var dp = LongArray(limit + 1)
        dp[0] = 1L

        for (p in runs) {
            // prefix sums of previous dp
            val pref = LongArray(limit + 1)
            var sum = 0L
            for (idx in 0..limit) {
                sum += dp[idx]
                if (sum >= MOD) sum -= MOD
                pref[idx] = sum
            }
            val ndp = LongArray(limit + 1)
            // compute new dp values for lengths 1..limit
            for (t in 1..limit) {
                var totalWays = pref[t - 1]
                val leftIdx = t - p - 1
                if (leftIdx >= 0) {
                    totalWays -= pref[leftIdx]
                    if (totalWays < 0) totalWays += MOD
                }
                ndp[t] = totalWays
            }
            dp = ndp
        }

        var smallSum = 0L
        for (t in 1..limit) {
            smallSum += dp[t]
            if (smallSum >= MOD) smallSum -= MOD
        }

        var ans = total - smallSum
        ans %= MOD
        if (ans < 0) ans += MOD
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;
  int possibleStringCount(String word, int k) {
    // Compute run lengths
    List<int> runs = [];
    int n = word.length;
    int i = 0;
    while (i < n) {
      int j = i;
      while (j < n && word[j] == word[i]) j++;
      runs.add(j - i);
      i = j;
    }
    int m = runs.length;

    // Total number of possible original strings
    int total = 1;
    for (int p in runs) {
      total = (total * p) % MOD;
    }

    // If minimal length (number of runs) already >= k, all are valid
    if (m >= k) return total;

    int limit = k - 1; // we need to count strings with length <= limit
    List<int> dp = List.filled(limit + 1, 0);
    dp[0] = 1; // empty prefix

    for (int p in runs) {
      // Prefix sums of previous dp
      List<int> pref = List.filled(limit + 1, 0);
      int acc = 0;
      for (int idx = 0; idx <= limit; ++idx) {
        acc += dp[idx];
        if (acc >= MOD) acc -= MOD;
        pref[idx] = acc;
      }

      // Compute new dp using the prefix sums
      List<int> ndp = List.filled(limit + 1, 0);
      for (int j = 1; j <= limit; ++j) {
        int left = j - 1;
        int right = j - p - 1;
        int val = pref[left];
        if (right >= 0) {
          val -= pref[right];
          if (val < 0) val += MOD;
        }
        ndp[j] = val;
      }
      dp = ndp;
    }

    // Sum ways with length <= limit
    int sumWays = 0;
    for (int v in dp) {
      sumWays += v;
      if (sumWays >= MOD) sumWays -= MOD;
    }

    int ans = total - sumWays;
    ans %= MOD;
    if (ans < 0) ans += MOD;
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"unicode/utf8"
)

const MOD int64 = 1000000007

func possibleStringCount(word string, k int) int {
	// Compute run lengths
	freq := make([]int, 0)
	n := len(word)
	if n == 0 {
		return 0
	}
	i := 0
	for i < n {
		j := i + 1
		for j < n && word[j] == word[i] {
			j++
		}
		freq = append(freq, j-i)
		i = j
	}

	// Total number of possible strings (any length)
	totalWays := int64(1)
	for _, p := range freq {
		totalWays = totalWays * int64(p) % MOD
	}

	m := len(freq)
	if m >= k {
		return int(totalWays)
	}

	// DP for lengths up to k-1
	dpPrev := make([]int64, k)
	dpPrev[0] = 1 // empty before processing any run

	for _, p := range freq {
		// prefix sums of dpPrev
		prefix := make([]int64, k)
		var acc int64 = 0
		for j := 0; j < k; j++ {
			acc += dpPrev[j]
			if acc >= MOD {
				acc -= MOD
			}
			prefix[j] = acc
		}
		dpCurr := make([]int64, k)
		for total := 1; total < k; total++ {
			left := total - p
			if left < 0 {
				left = 0
			}
			val := prefix[total-1]
			if left-1 >= 0 {
				val -= prefix[left-1]
				if val < 0 {
					val += MOD
				}
			}
			dpCurr[total] = val
		}
		dpPrev = dpCurr
	}

	// Sum ways with total length <= k-1
	var smallWays int64 = 0
	for j := 0; j < k; j++ {
		smallWays += dpPrev[j]
		if smallWays >= MOD {
			smallWays -= MOD
		}
	}

	ans := totalWays - smallWays
	if ans < 0 {
		ans += MOD
	}
	return int(ans)
}

// The following is only to avoid "imported and not used" error for utf8 in some environments.
var _ = utf8.RuneError
```

## Ruby

```ruby
MOD = 1_000_000_007

def possible_string_count(word, k)
  # compute run lengths
  freq = []
  cnt = 1
  (1...word.length).each do |i|
    if word[i] == word[i - 1]
      cnt += 1
    else
      freq << cnt
      cnt = 1
    end
  end
  freq << cnt

  # total number of possible strings (any length)
  total_all = 1
  freq.each { |p| total_all = (total_all * p) % MOD }

  # if minimal length >= k, all are valid
  return total_all if freq.size >= k

  limit = k # we need lengths 0..k-1
  dp = Array.new(limit, 0)
  dp[0] = 1

  freq.each do |p|
    prefix = Array.new(limit, 0)
    sum = 0
    limit.times do |j|
      sum += dp[j]
      sum -= MOD if sum >= MOD
      prefix[j] = sum
    end

    newdp = Array.new(limit, 0)
    (1...limit).each do |j|
      val = prefix[j - 1]
      left = j - p - 1
      if left >= 0
        val -= prefix[left]
        val += MOD if val < 0
      end
      newdp[j] = val % MOD
    end
    dp = newdp
  end

  sum_len = 0
  (1...limit).each do |j|
    sum_len += dp[j]
    sum_len -= MOD if sum_len >= MOD
  end

  ans = total_all - sum_len
  ans %= MOD
  ans += MOD if ans < 0
  ans
end
```

## Scala

```scala
object Solution {
    def possibleStringCount(word: String, k: Int): Int = {
        val MOD = 1000000007L
        // Compute run lengths
        val n = word.length
        val runs = scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n && word.charAt(j) == word.charAt(i)) j += 1
            runs += (j - i)
            i = j
        }
        val m = runs.length

        // Total number of possible strings (any length)
        var total = 1L
        for (p <- runs) {
            total = (total * p) % MOD
        }

        // If minimal possible length >= k, all strings are valid
        if (m >= k) return total.toInt

        val limit = k // we need dp indices 0..k-1
        var dpPrev = new Array[Long](limit)
        dpPrev(0) = 1L

        for (p <- runs) {
            // Prefix sums of previous DP row
            val prefix = new Array[Long](limit)
            var sum = 0L
            var idx = 0
            while (idx < limit) {
                sum += dpPrev(idx)
                if (sum >= MOD) sum -= MOD
                prefix(idx) = sum
                idx += 1
            }
            val dpCurr = new Array[Long](limit)
            var j = 1
            while (j < limit) {
                var res = prefix(j - 1)
                val rightIdx = j - p - 1
                if (rightIdx >= 0) {
                    res -= prefix(rightIdx)
                    if (res < 0) res += MOD
                }
                dpCurr(j) = res
                j += 1
            }
            dpPrev = dpCurr
        }

        // Count strings with length <= k-1
        var sumSmall = 0L
        var idx2 = 1
        while (idx2 < limit) {
            sumSmall += dpPrev(idx2)
            if (sumSmall >= MOD) sumSmall -= MOD
            idx2 += 1
        }

        var ans = total - sumSmall
        ans %= MOD
        if (ans < 0) ans += MOD
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn possible_string_count(word: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        // collect run lengths
        let bytes = word.as_bytes();
        let n = bytes.len();
        let mut freq: Vec<usize> = Vec::new();
        let mut i = 0;
        while i < n {
            let ch = bytes[i];
            let mut j = i;
            while j < n && bytes[j] == ch {
                j += 1;
            }
            freq.push(j - i);
            i = j;
        }

        // total number of possible strings (any length)
        let mut total: i64 = 1;
        for &p in &freq {
            total = total * (p as i64 % MOD) % MOD;
        }

        let m = freq.len();
        if m >= k as usize {
            return total as i32;
        }

        let max_len = (k - 1) as usize; // we need lengths < k
        let mut dp = vec![0i64; max_len + 1];
        dp[0] = 1;

        for &p in &freq {
            // prefix sums of previous dp
            let mut pref = vec![0i64; max_len + 1];
            let mut acc: i64 = 0;
            for idx in 0..=max_len {
                acc += dp[idx];
                if acc >= MOD {
                    acc -= MOD;
                }
                pref[idx] = acc;
            }

            let mut ndp = vec![0i64; max_len + 1];
            for j in 1..=max_len {
                // sum of dp[j-1] .. dp[j-p]
                let left = pref[j - 1];
                let sub = if j >= p + 1 {
                    pref[j - p - 1]
                } else {
                    0
                };
                let mut val = left + MOD - sub;
                if val >= MOD {
                    val -= MOD;
                }
                ndp[j] = val;
            }
            dp = ndp;
        }

        // count strings with length < k
        let mut small: i64 = 0;
        for &v in &dp {
            small += v;
            if small >= MOD {
                small -= MOD;
            }
        }

        let mut ans = total - small;
        ans %= MOD;
        if ans < 0 {
            ans += MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (possible-string-count word k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length word))
         ;; compute run lengths
         (freq
          (let loop ((i 0) (runs '()))
            (if (= i n)
                (reverse runs)
                (let ((c (string-ref word i)))
                  (let inner ((j i))
                    (if (and (< j n) (char=? (string-ref word j) c))
                        (inner (+ j 1))
                        (loop j (cons (- j i) runs)))))))))
         (m (length freq))
         ;; total number of possible strings (product of run lengths)
         (total-prod
          (let prod-loop ((lst freq) (acc 1))
            (if (null? lst)
                acc
                (prod-loop (cdr lst) (modulo (* acc (car lst)) MOD))))))
    (if (>= m k)
        total-prod
        (let* ((limit (- k 1))                     ; maximum length to count as "small"
               (dp-prev (make-vector (+ limit 1) 0)))
          (vector-set! dp-prev 0 1)                ; empty selection before any runs
          ;; process each run
          (for ([p freq])
            ;; prefix sums of previous DP row
            (define prefix (make-vector (+ limit 1) 0))
            (let loop ((j 0) (sum 0))
              (when (< j (+ limit 1))
                (set! sum (modulo (+ sum (vector-ref dp-prev j)) MOD))
                (vector-set! prefix j sum)
                (loop (+ j 1) sum)))
            ;; compute current DP row
            (define dp-curr (make-vector (+ limit 1) 0))
            (let loop2 ((j 0))
              (when (< j (+ limit 1))
                (if (= j 0)
                    (vector-set! dp-curr j 0)
                    (let* ((hi (- j 1))
                           (lo (- j p 1))
                           (val (vector-ref prefix hi)))
                      (when (>= lo 0)
                        (set! val (- val (vector-ref prefix lo))))
                      (set! val (modulo (+ val MOD) MOD))
                      (vector-set! dp-curr j val)))
                (loop2 (+ j 1))))
            (set! dp-prev dp-curr))
          ;; sum of ways with total length <= limit
          (let ((sum-small 0))
            (for ([j (in-range (+ limit 1))])
              (set! sum-small (modulo (+ sum-small (vector-ref dp-prev j)) MOD)))
            (let ((ans (- total-prod sum-small)))
              (if (< ans 0) (modulo (+ ans MOD) MOD) (modulo ans MOD))))))))
```

## Erlang

```erlang
-module(solution).
-export([possible_string_count/2]).

-define(MOD, 1000000007).

possible_string_count(Word, K) ->
    Freq = run_lengths(Word),
    Total = total_product(Freq),
    M = length(Freq),
    if
        M >= K ->
            Total;
        true ->
            Limit = K - 1,
            DP0 = array:new({size, Limit + 1}, {default, 0}),
            DPPrev = array:set(0, 1, DP0),
            DPEnd = lists:foldl(fun(P, Prev) -> dp_step(P, Prev, Limit) end, DPPrev, Freq),
            Small = sum_array(DPEnd, Limit),
            AnsTmp = (Total - Small) rem ?MOD,
            if
                AnsTmp < 0 -> AnsTmp + ?MOD;
                true -> AnsTmp
            end
    end.

run_lengths(Word) ->
    run_lengths(binary_to_list(Word), undefined, 0, []).

run_lengths([], _PrevChar, _Count, Acc) ->
    lists:reverse(Acc);
run_lengths([C|Rest], PrevChar, Count, Acc) when PrevChar =:= C ->
    run_lengths(Rest, PrevChar, Count + 1, Acc);
run_lengths([C|Rest], PrevChar, Count, Acc) when PrevChar =/= C, PrevChar =/= undefined ->
    run_lengths(Rest, C, 1, [Count | Acc]);
run_lengths([C|Rest], undefined, _Count, Acc) ->
    run_lengths(Rest, C, 1, Acc).

total_product(Freq) ->
    lists:foldl(fun(P, Acc) -> (Acc * P) rem ?MOD end, 1, Freq).

dp_step(P, PrevArr, Limit) ->
    % build prefix sums of PrevArr
    Pref0 = array:get(0, PrevArr),
    PrefInit = array:set(0, Pref0, array:new({size, Limit + 1}, {default, 0})),
    PrefArr = pref_build(1, Limit, PrevArr, PrefInit),
    % compute current DP using prefix sums
    CurInit = array:new({size, Limit + 1}, {default, 0}),
    dp_cur_build(0, Limit, P, PrefArr, CurInit).

pref_build(J, Limit, PrevArr, PrefArr) when J > Limit ->
    PrefArr;
pref_build(J, Limit, PrevArr, PrefArr) ->
    SumPrev = array:get(J - 1, PrefArr),
    CurVal = (SumPrev + array:get(J, PrevArr)) rem ?MOD,
    NewPref = array:set(J, CurVal, PrefArr),
    pref_build(J + 1, Limit, PrevArr, NewPref).

dp_cur_build(J, Limit, _P, _PrefArr, CurArr) when J > Limit ->
    CurArr;
dp_cur_build(0, Limit, P, PrefArr, CurArr) ->
    % length 0 cannot be formed after using at least one character from this run
    NewCur = array:set(0, 0, CurArr),
    dp_cur_build(1, Limit, P, PrefArr, NewCur);
dp_cur_build(J, Limit, P, PrefArr, CurArr) ->
    Upper = array:get(J - 1, PrefArr),
    LeftIdx = J - P - 1,
    Sub = if
        LeftIdx >= 0 -> array:get(LeftIdx, PrefArr);
        true -> 0
    end,
    Val = (Upper - Sub + ?MOD) rem ?MOD,
    NewCur = array:set(J, Val, CurArr),
    dp_cur_build(J + 1, Limit, P, PrefArr, NewCur).

sum_array(Arr, Limit) ->
    sum_array(0, Limit, Arr, 0).

sum_array(I, Limit, _Arr, Acc) when I > Limit ->
    Acc;
sum_array(I, Limit, Arr, Acc) ->
    NewAcc = (Acc + array:get(I, Arr)) rem ?MOD,
    sum_array(I + 1, Limit, Arr, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec possible_string_count(word :: String.t(), k :: integer) :: integer
  def possible_string_count(word, k) do
    mod = 1_000_000_007

    # obtain run lengths
    runs = run_lengths(word)
    m = length(runs)

    total_all =
      Enum.reduce(runs, 1, fn p, acc ->
        rem(acc * p, mod)
      end)

    if m >= k do
      total_all
    else
      max_len = k - 1

      # dp as Erlang array: dp[i] = ways to get length i using processed runs
      dp = :array.new(max_len + 1, default: 0) |> :array.set(0, 1)

      dp =
        Enum.reduce(runs, dp, fn p, cur_dp ->
          new_dp = :array.new(max_len + 1, default: 0)

          {final_arr, _} =
            Enum.reduce(1..max_len, {new_dp, 0}, fn j, {arr, sum} ->
              sum = rem(sum + :array.get(j - 1, cur_dp), mod)

              if j - p - 1 >= 0 do
                sub = :array.get(j - p - 1, cur_dp)
                sum = sum - sub
                if sum < 0, do: sum = sum + mod
              end

              arr = :array.set(j, sum, arr)
              {arr, sum}
            end)

          final_arr
        end)

      small_sum =
        Enum.reduce(1..max_len, 0, fn i, acc ->
          rem(acc + :array.get(i, dp), mod)
        end)

      ans = total_all - small_sum
      rem(ans + mod, mod)
    end
  end

  # helper to compute run lengths of consecutive identical characters
  defp run_lengths(word) do
    bytes = :binary.bin_to_list(word)

    {rev_runs, _prev, cur_cnt} =
      Enum.reduce(bytes, {[], nil, 0}, fn b, {acc, prev, cnt} ->
        cond do
          prev == nil ->
            {acc, b, 1}

          b == prev ->
            {acc, prev, cnt + 1}

          true ->
            {[cnt | acc], b, 1}
        end
      end)

    # prepend the last count and reverse to get correct order
    [cur_cnt | rev_runs] |> Enum.reverse()
  end
end
```

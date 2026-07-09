# 3176. Find the Maximum Length of a Good Subsequence I

## Cpp

```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n = nums.size();
        // compress values
        unordered_map<int,int> mp;
        vector<int> a(n);
        int idx = 0;
        for (int v : nums) {
            if (!mp.count(v)) mp[v] = idx++;
            a[&v - &nums[0]] = mp[v]; // placeholder, will overwrite below
        }
        for (int i = 0; i < n; ++i) a[i] = mp[nums[i]];
        int m = idx;
        const int NEG = -1e9;
        vector<vector<int>> dp(k+1, vector<int>(m, NEG));
        for (int pos = 0; pos < n; ++pos) {
            int x = a[pos];
            auto prev = dp; // snapshot before using current element
            // start new subsequence with this element
            dp[0][x] = max(dp[0][x], 1);
            for (int c = 0; c <= k; ++c) {
                // extend same value without extra change
                if (prev[c][x] != NEG) {
                    dp[c][x] = max(dp[c][x], prev[c][x] + 1);
                }
                // switch from a different value, consuming one change
                if (c > 0) {
                    int best = NEG;
                    for (int y = 0; y < m; ++y) {
                        if (y == x) continue;
                        best = max(best, prev[c-1][y]);
                    }
                    if (best != NEG) dp[c][x] = max(dp[c][x], best + 1);
                }
            }
        }
        int ans = 0;
        for (int c = 0; c <= k; ++c)
            for (int v = 0; v < m; ++v)
                ans = max(ans, dp[c][v]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        // compress values
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        int idx = 0;
        for (int num : nums) {
            if (!map.containsKey(num)) {
                map.put(num, idx++);
            }
        }
        int m = idx; // number of distinct values
        final int NEG = -1_000_000_0;
        int[][] dp = new int[k + 1][m];
        for (int i = 0; i <= k; i++) {
            java.util.Arrays.fill(dp[i], NEG);
        }

        for (int num : nums) {
            int x = map.get(num);

            // compute top two values for each transition count
            int[] maxVal = new int[k + 1];
            int[] maxIdx = new int[k + 1];
            int[] secondMax = new int[k + 1];
            java.util.Arrays.fill(maxVal, NEG);
            java.util.Arrays.fill(secondMax, NEG);
            java.util.Arrays.fill(maxIdx, -1);

            for (int t = 0; t <= k; t++) {
                for (int v = 0; v < m; v++) {
                    int val = dp[t][v];
                    if (val > maxVal[t]) {
                        secondMax[t] = maxVal[t];
                        maxVal[t] = val;
                        maxIdx[t] = v;
                    } else if (val > secondMax[t]) {
                        secondMax[t] = val;
                    }
                }
            }

            // store old values for current value x
            int[] oldVals = new int[k + 1];
            for (int t = 0; t <= k; t++) {
                oldVals[t] = dp[t][x];
            }

            for (int t = 0; t <= k; t++) {
                int best = oldVals[t];
                if (oldVals[t] > NEG) {
                    best = Math.max(best, oldVals[t] + 1); // extend same value
                }
                if (t == 0) {
                    best = Math.max(best, 1); // start new subsequence
                } else {
                    int candidate = (maxIdx[t - 1] != x) ? maxVal[t - 1] : secondMax[t - 1];
                    if (candidate > NEG) {
                        best = Math.max(best, candidate + 1); // transition from different value
                    }
                }
                dp[t][x] = best;
            }
        }

        int ans = 0;
        for (int t = 0; t <= k; t++) {
            for (int v = 0; v < m; v++) {
                if (dp[t][v] > ans) ans = dp[t][v];
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # compress values to 0..m-1
        mapping = {}
        comp = []
        for x in nums:
            if x not in mapping:
                mapping[x] = len(mapping)
            comp.append(mapping[x])
        m = len(mapping)

        INF_NEG = -10**9
        dp = [[INF_NEG] * m for _ in range(k + 1)]
        ans = 0

        for v in comp:
            # snapshot of previous state
            old = [row[:] for row in dp]

            # start a new subsequence with this element alone (0 changes)
            if dp[0][v] < 1:
                dp[0][v] = 1

            for c in range(k + 1):
                # extend same value without extra change
                if old[c][v] != INF_NEG:
                    cand = old[c][v] + 1
                    if cand > dp[c][v]:
                        dp[c][v] = cand

                # transition from a different value, consuming one change
                if c > 0:
                    best = INF_NEG
                    prev_row = old[c - 1]
                    for y in range(m):
                        if y == v:
                            continue
                        val = prev_row[y]
                        if val > best:
                            best = val
                    if best != INF_NEG:
                        cand = best + 1
                        if cand > dp[c][v]:
                            dp[c][v] = cand

                if dp[c][v] > ans:
                    ans = dp[c][v]

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # compress values to 0..m-1
        idx = {}
        comp = []
        for x in nums:
            if x not in idx:
                idx[x] = len(idx)
            comp.append(idx[x])
        m = len(idx)

        dp = [[0] * m for _ in range(k + 1)]  # dp[c][v] = best length ending with value v using c changes

        for val in comp:
            ndp = [row[:] for row in dp]

            # start a new subsequence with this element
            if ndp[0][val] < 1:
                ndp[0][val] = 1

            for c in range(k + 1):
                cur = dp[c][val]
                if cur:
                    # extend same value, no extra change
                    if ndp[c][val] < cur + 1:
                        ndp[c][val] = cur + 1

                if c < k:
                    best = 0
                    row = dp[c]
                    for y in range(m):
                        if y == val:
                            continue
                        v = row[y]
                        if v > best:
                            best = v
                    if best:
                        # switch from a different value, consumes one change
                        if ndp[c + 1][val] < best + 1:
                            ndp[c + 1][val] = best + 1

            dp = ndp

        ans = 0
        for c in range(k + 1):
            ans = max(ans, max(dp[c]))
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

int maximumLength(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;

    /* compress values to [0, m-1] */
    int *sorted = (int *)malloc(numsSize * sizeof(int));
    memcpy(sorted, nums, numsSize * sizeof(int));
    qsort(sorted, numsSize, sizeof(int), cmp_int);

    int *uniq = (int *)malloc(numsSize * sizeof(int));
    int m = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || sorted[i] != sorted[i - 1]) {
            uniq[m++] = sorted[i];
        }
    }
    free(sorted);

    int *comp = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        int lo = 0, hi = m - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            if (uniq[mid] == nums[i]) { comp[i] = mid; break; }
            else if (uniq[mid] < nums[i]) lo = mid + 1;
            else hi = mid - 1;
        }
    }

    const int NEG = -1000000;
    static int dp[26][500];
    static int prevdp[26][500];

    for (int t = 0; t <= k; ++t)
        for (int v = 0; v < m; ++v)
            dp[t][v] = NEG;

    for (int idx = 0; idx < numsSize; ++idx) {
        int x = comp[idx];
        memcpy(prevdp, dp, sizeof(dp));

        /* start a new subsequence with this element */
        if (dp[0][x] < 1) dp[0][x] = 1;

        for (int t = 0; t <= k; ++t) {
            /* extend same value without adding transition */
            if (prevdp[t][x] != NEG) {
                int cand = prevdp[t][x] + 1;
                if (cand > dp[t][x]) dp[t][x] = cand;
            }
            /* start a new run from a different previous value */
            if (t >= 1) {
                int best = NEG;
                for (int y = 0; y < m; ++y) {
                    if (y == x) continue;
                    if (prevdp[t - 1][y] > best) best = prevdp[t - 1][y];
                }
                if (best != NEG) {
                    int cand = best + 1;
                    if (cand > dp[t][x]) dp[t][x] = cand;
                }
            }
        }
    }

    int ans = 0;
    for (int t = 0; t <= k; ++t)
        for (int v = 0; v < m; ++v)
            if (dp[t][v] > ans) ans = dp[t][v];

    free(uniq);
    free(comp);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumLength(int[] nums, int k) {
        int n = nums.Length;
        // Compress values to [0, m-1]
        var map = new Dictionary<int, int>();
        int idx = 0;
        int[] comp = new int[n];
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            if (!map.ContainsKey(v)) {
                map[v] = idx++;
            }
            comp[i] = map[v];
        }
        int m = idx;
        const int NEG = -1000000;
        int[,] dp = new int[k + 1, m];
        for (int t = 0; t <= k; t++) {
            for (int v = 0; v < m; v++) dp[t, v] = NEG;
        }

        foreach (int x in comp) {
            int[,] ndp = (int[,])dp.Clone();
            // start new subsequence with this element alone
            ndp[0, x] = Math.Max(ndp[0, x], 1);
            for (int t = 0; t <= k; t++) {
                // extend same value without extra transition
                if (dp[t, x] != NEG) {
                    ndp[t, x] = Math.Max(ndp[t, x], dp[t, x] + 1);
                }
                // transition from a different value
                if (t > 0) {
                    for (int y = 0; y < m; y++) {
                        if (y == x) continue;
                        if (dp[t - 1, y] != NEG) {
                            ndp[t, x] = Math.Max(ndp[t, x], dp[t - 1, y] + 1);
                        }
                    }
                }
            }
            dp = ndp;
        }

        int ans = 0;
        for (int t = 0; t <= k; t++) {
            for (int v = 0; v < m; v++) {
                if (dp[t, v] > ans) ans = dp[t, v];
            }
        }
        return ans;
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
var maximumLength = function(nums, k) {
    const n = nums.length;
    // compress values to 0..m-1
    const map = new Map();
    let idx = 0;
    const comp = new Array(n);
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        if (!map.has(v)) {
            map.set(v, idx++);
        }
        comp[i] = map.get(v);
    }
    const m = idx;
    const NEG = -1e9;

    // dp[t][value] = max length ending with this value using exactly t transitions
    const dp = Array.from({length: k + 1}, () => new Array(m).fill(NEG));
    const best = new Array(k + 1).fill(NEG); // max over values for each t

    for (let pos = 0; pos < n; ++pos) {
        const v = comp[pos];
        const prevBest = best.slice(); // snapshot before this element
        for (let t = 0; t <= k; ++t) {
            let cur = dp[t][v];
            // start new subsequence with this single element
            let cand = 1;
            // extend same value without extra transition
            if (cur > NEG) {
                cand = Math.max(cand, cur + 1);
            }
            // transition from a different value (adds one transition)
            if (t > 0 && prevBest[t - 1] > NEG) {
                cand = Math.max(cand, prevBest[t - 1] + 1);
            }
            dp[t][v] = Math.max(dp[t][v], cand);
            if (dp[t][v] > best[t]) best[t] = dp[t][v];
        }
    }

    let ans = 0;
    for (let t = 0; t <= k; ++t) {
        if (best[t] > ans) ans = best[t];
    }
    return ans;
};
```

## Typescript

```typescript
function maximumLength(nums: number[], k: number): number {
    const n = nums.length;
    // compress values to 0..m-1
    const map = new Map<number, number>();
    let curIdx = 0;
    const comp = new Array(n);
    for (let i = 0; i < n; i++) {
        const v = nums[i];
        if (!map.has(v)) {
            map.set(v, curIdx++);
        }
        comp[i] = map.get(v)!;
    }
    const m = curIdx;
    const NEG = -1e9;

    // dp[t][v] = max length ending with value v using exactly t changes
    let dp: number[][] = Array.from({ length: k + 1 }, () => Array(m).fill(NEG));

    for (let i = 0; i < n; i++) {
        const x = comp[i];
        // copy current dp to ndp (we may improve it)
        const ndp: number[][] = dp.map(row => row.slice());

        // start a new subsequence with this element alone
        if (ndp[0][x] < 1) ndp[0][x] = 1;

        for (let t = 0; t <= k; t++) {
            // extend a subsequence that already ends with x (no extra change)
            if (dp[t][x] > NEG) {
                const cand = dp[t][x] + 1;
                if (cand > ndp[t][x]) ndp[t][x] = cand;
            }

            // transition from a different value, incurring one more change
            if (t < k) {
                let best = NEG;
                for (let y = 0; y < m; y++) {
                    if (y === x) continue;
                    const val = dp[t][y];
                    if (val > best) best = val;
                }
                if (best > NEG) {
                    const cand = best + 1;
                    if (cand > ndp[t + 1][x]) ndp[t + 1][x] = cand;
                }
            }
        }

        dp = ndp;
    }

    let ans = 0;
    for (let t = 0; t <= k; t++) {
        for (let v = 0; v < m; v++) {
            if (dp[t][v] > ans) ans = dp[t][v];
        }
    }
    return ans;
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
    function maximumLength($nums, $k) {
        $n = count($nums);
        // compress values
        $unique = array_values(array_unique($nums));
        $m = count($unique);
        $map = [];
        foreach ($unique as $idx => $val) {
            $map[$val] = $idx;
        }

        $NEG_INF = -1000000; // sufficiently small

        // dp[c][v] = max length ending with value v using exactly c transitions
        $dp = array_fill(0, $k + 1, array_fill(0, $m, $NEG_INF));

        foreach ($nums as $num) {
            $idx = $map[$num];

            // compute best and second best for each transition count before this element
            $bestLen = $secondBestLen = $argMax = [];
            for ($c = 0; $c <= $k; $c++) {
                $best = $NEG_INF;
                $second = $NEG_INF;
                $bestIdx = -1;
                for ($v = 0; $v < $m; $v++) {
                    $val = $dp[$c][$v];
                    if ($val > $best) {
                        $second = $best;
                        $best = $val;
                        $bestIdx = $v;
                    } elseif ($val > $second) {
                        $second = $val;
                    }
                }
                $bestLen[$c] = $best;
                $secondBestLen[$c] = $second;
                $argMax[$c] = $bestIdx;
            }

            // snapshot of dp for same-value extension
            $old = $dp;

            for ($c = 0; $c <= $k; $c++) {
                // start a new subsequence with this element (zero transitions)
                if ($c == 0 && $dp[0][$idx] < 1) {
                    $dp[0][$idx] = 1;
                }

                // extend same value without adding transition
                if ($old[$c][$idx] != $NEG_INF) {
                    $cand = $old[$c][$idx] + 1;
                    if ($cand > $dp[$c][$idx]) {
                        $dp[$c][$idx] = $cand;
                    }
                }

                // start a new block from a different value, consuming one transition
                if ($c > 0) {
                    if ($argMax[$c - 1] != $idx && $bestLen[$c - 1] != $NEG_INF) {
                        $cand = $bestLen[$c - 1] + 1;
                        if ($cand > $dp[$c][$idx]) {
                            $dp[$c][$idx] = $cand;
                        }
                    } elseif ($secondBestLen[$c - 1] != $NEG_INF) {
                        $cand = $secondBestLen[$c - 1] + 1;
                        if ($cand > $dp[$c][$idx]) {
                            $dp[$c][$idx] = $cand;
                        }
                    }
                }
            }
        }

        // answer is the maximum over all states with at most k transitions
        $ans = 0;
        for ($c = 0; $c <= $k; $c++) {
            for ($v = 0; $v < $m; $v++) {
                if ($dp[$c][$v] > $ans) {
                    $ans = $dp[$c][$v];
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int], _ k: Int) -> Int {
        // Compress values to 0..m-1
        var valueToIndex = [Int:Int]()
        var nextIdx = 0
        for num in nums {
            if valueToIndex[num] == nil {
                valueToIndex[num] = nextIdx
                nextIdx += 1
            }
        }
        let m = nextIdx
        let INF = -1_000_000_000
        
        // dp[t][v] = max length of subsequence ending with value v using at most t transitions
        var dp = Array(repeating: Array(repeating: INF, count: m), repeatCount: k + 1)
        
        for num in nums {
            guard let v = valueToIndex[num] else { continue }
            // copy previous state
            let prev = dp
            
            // start a new subsequence with this element alone (0 transitions)
            if dp[0][v] < 1 {
                dp[0][v] = 1
            }
            
            for t in 0...k {
                // extend from same value without adding a transition
                let samePrev = prev[t][v]
                if samePrev != INF {
                    let cand = samePrev + 1
                    if cand > dp[t][v] { dp[t][v] = cand }
                }
                
                // change from a different value, consuming one transition
                if t > 0 {
                    var bestPrev = INF
                    for y in 0..<m where y != v {
                        let val = prev[t - 1][y]
                        if val > bestPrev { bestPrev = val }
                    }
                    if bestPrev != INF {
                        let cand = bestPrev + 1
                        if cand > dp[t][v] { dp[t][v] = cand }
                    }
                }
            }
        }
        
        var answer = 0
        for t in 0...k {
            for v in 0..<m {
                if dp[t][v] > answer {
                    answer = dp[t][v]
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray, k: Int): Int {
        val n = nums.size
        // compress values to 0..m-1
        val distinct = nums.distinct()
        val map = HashMap<Int, Int>()
        for (i in distinct.indices) {
            map[distinct[i]] = i
        }
        val m = distinct.size
        val comp = IntArray(n) { map[nums[it]]!! }

        val NEG = -1_000_000
        val dp = Array(k + 1) { IntArray(m) { NEG } }
        var answer = 0

        for (value in comp) {
            // copy current dp to old
            val old = Array(k + 1) { dp[it].clone() }

            // start new subsequence with this element alone
            dp[0][value] = maxOf(dp[0][value], 1)

            for (c in 0..k) {
                // extend same value without extra change
                if (old[c][value] > NEG) {
                    dp[c][value] = maxOf(dp[c][value], old[c][value] + 1)
                }
                // start new block from a different value, consuming one change
                if (c > 0) {
                    var bestOther = NEG
                    for (v in 0 until m) {
                        if (v == value) continue
                        if (old[c - 1][v] > bestOther) bestOther = old[c - 1][v]
                    }
                    if (bestOther > NEG) {
                        dp[c][value] = maxOf(dp[c][value], bestOther + 1)
                    }
                }
                // update answer
                if (dp[c][value] > answer) answer = dp[c][value]
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maximumLength(List<int> nums, int k) {
    // Compress values to range [0, m-1]
    Map<int, int> comp = {};
    int idx = 0;
    for (int v in nums) {
      if (!comp.containsKey(v)) {
        comp[v] = idx++;
      }
    }
    int m = idx;
    List<List<int>> dp = List.generate(k + 1, (_) => List.filled(m, -1));

    for (int num in nums) {
      int x = comp[num]!;

      // snapshot of previous state
      List<List<int>> prev = List.generate(
          k + 1, (i) => List.from(dp[i])
      );

      // start a new subsequence with this element alone
      if (dp[0][x] < 1) dp[0][x] = 1;

      for (int c = 0; c <= k; ++c) {
        int same = prev[c][x];
        if (same != -1) {
          int cand = same + 1;
          if (cand > dp[c][x]) dp[c][x] = cand;
        }
        if (c < k) {
          for (int y = 0; y < m; ++y) {
            if (y == x) continue;
            int val = prev[c][y];
            if (val != -1) {
              int cand2 = val + 1;
              if (cand2 > dp[c + 1][x]) dp[c + 1][x] = cand2;
            }
          }
        }
      }
    }

    int ans = 0;
    for (int c = 0; c <= k; ++c) {
      for (int v = 0; v < m; ++v) {
        if (dp[c][v] > ans) ans = dp[c][v];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maximumLength(nums []int, k int) int {
    n := len(nums)
    // compress values to 0..m-1
    mp := make(map[int]int)
    comp := make([]int, n)
    idx := 0
    for i, v := range nums {
        if _, ok := mp[v]; !ok {
            mp[v] = idx
            idx++
        }
        comp[i] = mp[v]
    }
    m := idx

    // dp[c][v] = max length ending with value v using exactly c changes
    dp := make([][]int, k+1)
    for c := 0; c <= k; c++ {
        row := make([]int, m)
        for i := range row {
            row[i] = -1
        }
        dp[c] = row
    }

    best1Len := make([]int, k+1)
    best2Len := make([]int, k+1)
    best1Val := make([]int, k+1)

    for _, aIdx := range comp {
        // compute top two lengths for each change count before processing this element
        for c := 0; c <= k; c++ {
            b1, b2, v1 := -1, -1, -1
            for v := 0; v < m; v++ {
                val := dp[c][v]
                if val > b1 {
                    b2 = b1
                    b1 = val
                    v1 = v
                } else if val > b2 && v != v1 {
                    b2 = val
                }
            }
            best1Len[c] = b1
            best2Len[c] = b2
            best1Val[c] = v1
        }

        // update dp using current element
        for c := k; c >= 0; c-- {
            old := dp[c][aIdx]

            // start new subsequence (zero changes)
            if c == 0 && old < 1 {
                dp[c][aIdx] = 1
            }

            // extend same value without extra change
            if old != -1 {
                cand := old + 1
                if cand > dp[c][aIdx] {
                    dp[c][aIdx] = cand
                }
            }

            // switch from a different value, adding one change
            if c > 0 {
                var bestPrev int
                if best1Val[c-1] != aIdx {
                    bestPrev = best1Len[c-1]
                } else {
                    bestPrev = best2Len[c-1]
                }
                if bestPrev != -1 {
                    cand := bestPrev + 1
                    if cand > dp[c][aIdx] {
                        dp[c][aIdx] = cand
                    }
                }
            }
        }
    }

    ans := 0
    for c := 0; c <= k; c++ {
        for v := 0; v < m; v++ {
            if dp[c][v] > ans {
                ans = dp[c][v]
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_length(nums, k)
  # Coordinate compression of values
  uniq_vals = nums.uniq
  idx_map = {}
  uniq_vals.each_with_index { |v, i| idx_map[v] = i }
  m = uniq_vals.size

  neg_inf = -1_000_000
  dp = Array.new(k + 1) { Array.new(m, neg_inf) }

  nums.each do |num|
    x = idx_map[num]

    # start a new subsequence with this element
    dp[0][x] = [dp[0][x], 1].max

    k.downto(0) do |t|
      cur = dp[t][x]
      if cur > neg_inf / 2
        dp[t][x] = [cur + 1, dp[t][x]].max
      end

      next if t == k

      best = neg_inf
      (0...m).each do |y|
        next if y == x
        val = dp[t][y]
        best = val if val > best
      end
      if best > neg_inf / 2
        dp[t + 1][x] = [dp[t + 1][x], best + 1].max
      end
    end
  end

  dp.flatten.max
end
```

## Scala

```scala
object Solution {
    def maximumLength(nums: Array[Int], k: Int): Int = {
        val distinct = nums.distinct
        val idxMap = scala.collection.mutable.HashMap[Int, Int]()
        for (i <- distinct.indices) idxMap(distinct(i)) = i
        val m = distinct.length
        val NEG = -1000000
        var dp = Array.fill(k + 1, m)(NEG)

        for (num <- nums) {
            val x = idxMap(num)
            // copy previous state
            val prev = Array.ofDim[Int](k + 1, m)
            for (t <- 0 to k) {
                System.arraycopy(dp(t), 0, prev(t), 0, m)
            }
            // start new subsequence with this element alone
            if (dp(0)(x) < 1) dp(0)(x) = 1

            for (t <- 0 to k) {
                // extend same value without adding a transition
                val samePrev = prev(t)(x)
                if (samePrev > NEG) {
                    val cand = samePrev + 1
                    if (cand > dp(t)(x)) dp(t)(x) = cand
                }
                // transition from a different value
                if (t > 0) {
                    var maxOther = NEG
                    for (y <- 0 until m if y != x) {
                        val v = prev(t - 1)(y)
                        if (v > maxOther) maxOther = v
                    }
                    if (maxOther > NEG) {
                        val cand = maxOther + 1
                        if (cand > dp(t)(x)) dp(t)(x) = cand
                    }
                }
            }
        }

        var ans = 0
        for (t <- 0 to k; v <- 0 until m) {
            if (dp(t)(v) > ans) ans = dp(t)(v)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        // Coordinate compression
        let mut uniq = nums.clone();
        uniq.sort_unstable();
        uniq.dedup();
        let m = uniq.len();
        let comp: Vec<usize> = nums
            .iter()
            .map(|&v| uniq.binary_search(&v).unwrap())
            .collect();

        let k_usize = k as usize;
        // dp[c][value] = max length of a subsequence ending with `value` using at most c changes
        let mut dp = vec![vec![-1i32; m]; k_usize + 1];

        for &x in comp.iter() {
            let prev = dp.clone(); // snapshot before processing this element
            for c in 0..=k_usize {
                // start a new subsequence with this element
                let mut best = 1;
                // extend a subsequence that already ends with the same value (no extra change)
                if prev[c][x] != -1 {
                    best = best.max(prev[c][x] + 1);
                }
                // switch from a different value, consuming one change
                if c > 0 {
                    let mut mx = -1i32;
                    for y in 0..m {
                        if y == x { continue; }
                        if prev[c - 1][y] > mx {
                            mx = prev[c - 1][y];
                        }
                    }
                    if mx != -1 {
                        best = best.max(mx + 1);
                    }
                }
                if dp[c][x] < best {
                    dp[c][x] = best;
                }
            }
        }

        let mut ans = 0i32;
        for c in 0..=k_usize {
            for v in 0..m {
                if dp[c][v] > ans {
                    ans = dp[c][v];
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define (maximum-length nums k)
  (let* ((neg-inf -1000000)
         (hash (make-hash))
         (next-index 0)
         (compressed
           (map (lambda (v)
                  (if (hash-has-key? hash v)
                      (hash-ref hash v)
                      (begin
                        (hash-set! hash v next-index)
                        (set! next-index (+ next-index 1))
                        (- next-index 1))))
                nums))
         (m next-index)
         (dp (make-vector (+ k 1) #f)))
    ;; initialize dp vectors
    (for ([t (in-range (+ k 1))])
      (vector-set! dp t (make-vector m neg-inf)))
    (define best1 (make-vector (+ k 1) neg-inf))
    (define idx1 (make-vector (+ k 1) -1))
    (define best2 (make-vector (+ k 1) neg-inf))
    (define answer 0)
    ;; process each element
    (for ([x compressed])
      (define newvals (make-vector (+ k 1) neg-inf))
      (for ([t (in-range (+ k 1))])
        (let* ((vec (vector-ref dp t))
               (old (vector-ref vec x))
               (newlen old))
          ;; extend same value
          (when (> old neg-inf)
            (set! newlen (max newlen (+ old 1))))
          ;; start new subsequence
          (when (= t 0)
            (set! newlen (max newlen 1)))
          ;; transition from different value
          (when (> t 0)
            (let* ((prev-t (- t 1))
                   (best-ex (if (= (vector-ref idx1 prev-t) x)
                                (vector-ref best2 prev-t)
                                (vector-ref best1 prev-t))))
              (when (> best-ex neg-inf)
                (set! newlen (max newlen (+ best-ex 1))))))
          (vector-set! newvals t newlen)))
      ;; update dp and answer
      (for ([t (in-range (+ k 1))])
        (let* ((vec (vector-ref dp t))
               (newlen (vector-ref newvals t)))
          (when (> newlen (vector-ref vec x))
            (vector-set! vec x newlen))
          (when (> newlen answer)
            (set! answer newlen))))
      ;; recompute bests for each t
      (for ([t (in-range (+ k 1))])
        (let ((vec (vector-ref dp t)))
          (let loop ((i 0) (b1 neg-inf) (i1 -1) (b2 neg-inf))
            (if (= i m)
                (begin
                  (vector-set! best1 t b1)
                  (vector-set! idx1 t i1)
                  (vector-set! best2 t b2))
                (let ((val (vector-ref vec i)))
                  (cond
                    [(> val b1) (loop (+ i 1) val i b1)]
                    [(and (> val b2) (not (= i i1))) (loop (+ i 1) b1 i1 val)]
                    [else (loop (+ i 1) b1 i1 b2)])))))))
    answer))
```

## Erlang

```erlang
-module(solution).
-export([maximum_length/2]).

-define(NEG_INF, -1000000).

maximum_length(Nums, K) ->
    Unique = lists:usort(Nums),
    IndexMap = maps:from_list(lists:zip(Unique, lists:seq(0, length(Unique) - 1))),
    Compressed = [maps:get(N, IndexMap) || N <- Nums],
    M = length(Unique),
    InitRow = lists:duplicate(M, ?NEG_INF),
    DP0 = [InitRow || _ <- lists:seq(0, K)],
    FinalDP = lists:foldl(fun(Id, DPPrev) -> update_dp(DPPrev, Id, K, M) end,
                          DP0, Compressed),
    max_in_dp(FinalDP).

update_dp(DPPrev, Idx, K, _M) ->
    lists:foldl(
      fun(T, AccDP) ->
          PrevRow = nth_row(DPPrev, T),
          CurrRow = nth_row(AccDP, T),

          SamePrevLen = nth_elem(PrevRow, Idx),
          CandSame = if SamePrevLen > ?NEG_INF -> SamePrevLen + 1; true -> ?NEG_INF end,
          CandStart = case T of
                         0 -> max(CandSame, 1);
                         _ -> CandSame
                     end,

          CandTrans = case T of
                        0 -> ?NEG_INF;
                        _ ->
                            PrevRowPrevT = nth_row(DPPrev, T - 1),
                            MaxOther = max_except(PrevRowPrevT, Idx),
                            if MaxOther > ?NEG_INF -> MaxOther + 1; true -> ?NEG_INF end
                     end,

          OldVal = nth_elem(CurrRow, Idx),
          NewVal = max_of_three(OldVal, CandStart, CandTrans),

          UpdatedCurrRow = set_nth(CurrRow, Idx, NewVal),
          replace_row(AccDP, T, UpdatedCurrRow)
      end,
      DPPrev,
      lists:seq(0, K)).

nth_row(DP, Index) -> lists:nth(Index + 1, DP).
nth_elem(Row, Idx) -> lists:nth(Idx + 1, Row).

set_nth([_ | Tail], 0, Val) -> [Val | Tail];
set_nth([H | Tail], I, Val) when I > 0 -> [H | set_nth(Tail, I - 1, Val)].

replace_row(DP, Index, NewRow) -> set_nth(DP, Index, NewRow).

max_except(Row, ExIdx) ->
    max_except(Row, ExIdx, 0, ?NEG_INF).

max_except([], _, _, Acc) -> Acc;
max_except([H | T], ExIdx, CurIdx, Acc) ->
    NewAcc = if CurIdx =:= ExIdx -> Acc; H > Acc -> H; true -> Acc end,
    max_except(T, ExIdx, CurIdx + 1, NewAcc).

max_of_three(A, B, C) ->
    MaxAB = if A > B -> A; true -> B end,
    if MaxAB > C -> MaxAB; true -> C end.

max_in_dp(DP) ->
    lists:foldl(
      fun(Row, Acc) ->
          RowMax = max_list(Row),
          if RowMax > Acc -> RowMax; true -> Acc end
      end,
      ?NEG_INF,
      DP).

max_list([H | T]) ->
    lists:foldl(fun(X, Acc) -> if X > Acc -> X; true -> Acc end end, H, T).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer], k :: integer) :: integer
  def maximum_length(nums, k) do
    # Compress values to a small range
    uniq = Enum.uniq(nums)
    idx_map = uniq |> Enum.with_index() |> Map.new(fn {v, i} -> {v, i} end)
    comp = Enum.map(nums, fn v -> Map.get(idx_map, v) end)

    # Initialize dp: list of maps for each allowed number of changes (0..k)
    dp_initial = for _ <- 0..k, do: %{}

    dp_final =
      Enum.reduce(comp, dp_initial, fn x, dp_acc ->
        Enum.map(0..k, fn t ->
          row = Enum.at(dp_acc, t)

          # Extend subsequence ending with same value (no additional change)
          cur_len = Map.get(row, x, 0)
          row =
            if cur_len > 0 do
              put_max(row, x, cur_len + 1)
            else
              row
            end

          # Start a new subsequence of length 1 (only for t == 0)
          row =
            if t == 0 do
              put_max(row, x, 1)
            else
              row
            end

          # Extend from a different value, consuming one change
          row =
            if t > 0 do
              prev = Enum.at(dp_acc, t - 1)

              max_other =
                prev
                |> Enum.reject(fn {k, _v} -> k == x end)
                |> Enum.map(fn {_k, v} -> v end)
                |> Enum.max(fn -> 0 end)

              if max_other > 0 do
                put_max(row, x, max_other + 1)
              else
                row
              end
            else
              row
            end

          row
        end)
      end)

    dp_final
    |> Enum.flat_map(&Map.values/1)
    |> Enum.max(fn -> 0 end)
  end

  # Helper: store the larger of existing and new value for a key in a map
  defp put_max(map, key, val) do
    case Map.get(map, key, 0) do
      existing when existing >= val -> map
      _ -> Map.put(map, key, val)
    end
  end
end
```

# 3177. Find the Maximum Length of a Good Subsequence II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n = nums.size();
        // coordinate compression
        unordered_map<int,int> mp;
        vector<int> compVals;
        for (int x: nums) if (!mp.count(x)) {
            mp[x] = compVals.size();
            compVals.push_back(x);
        }
        int m = compVals.size();
        const int NEG = -1e9;
        vector<vector<int>> dp(m, vector<int>(k+1, NEG));
        
        // global top two per change count
        vector<int> max1(k+1, NEG), max2(k+1, NEG), val1(k+1, -1);
        
        int answer = 0;
        for (int num : nums) {
            int idx = mp[num];
            vector<int> oldRow = dp[idx];          // state before using this element
            vector<int> newRow(k+1, NEG);
            
            for (int c = 0; c <= k; ++c) {
                int cand = oldRow[c];
                if (oldRow[c] != NEG) cand = max(cand, oldRow[c] + 1); // extend same value
                if (c == 0) cand = max(cand, 1);                       // start new subsequence
                
                if (c > 0) {
                    int otherBest = (val1[c-1] != idx) ? max1[c-1] : max2[c-1];
                    if (otherBest != NEG) cand = max(cand, otherBest + 1);
                }
                newRow[c] = cand;
                answer = max(answer, cand);
            }
            
            // write back and update global maxima
            for (int c = 0; c <= k; ++c) {
                dp[idx][c] = newRow[c];
                int val = newRow[c];
                if (val > max1[c]) {
                    if (val1[c] != idx) {
                        max2[c] = max1[c];
                    }
                    max1[c] = val;
                    val1[c] = idx;
                } else if (idx != val1[c] && val > max2[c]) {
                    max2[c] = val;
                }
            }
        }
        return answer;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        // compress values
        Map<Integer, Integer> map = new HashMap<>();
        int idx = 0;
        int[] comp = new int[n];
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            if (!map.containsKey(v)) {
                map.put(v, idx++);
            }
            comp[i] = map.get(v);
        }
        int m = idx;
        final int NEG = -1_000_000_000;

        int[][] dp = new int[k + 1][m];
        for (int i = 0; i <= k; i++) {
            Arrays.fill(dp[i], NEG);
        }

        int[] bestVal = new int[k + 1];
        int[] bestIdx = new int[k + 1];
        int[] secondBest = new int[k + 1];
        Arrays.fill(bestVal, NEG);
        Arrays.fill(secondBest, NEG);
        Arrays.fill(bestIdx, -1);

        int answer = 0;
        int[] prevBestVal = new int[k + 1];
        int[] prevBestIdx = new int[k + 1];
        int[] prevSecondBest = new int[k + 1];
        int[] newLen = new int[k + 1];

        for (int x : comp) {
            // snapshot current bests
            for (int c = 0; c <= k; c++) {
                prevBestVal[c] = bestVal[c];
                prevBestIdx[c] = bestIdx[c];
                prevSecondBest[c] = secondBest[c];
            }

            for (int c = 0; c <= k; c++) {
                int same = dp[c][x] == NEG ? NEG : dp[c][x] + 1;
                int sw = NEG;
                if (c > 0) {
                    int best = prevBestVal[c - 1];
                    if (prevBestIdx[c - 1] == x) {
                        best = prevSecondBest[c - 1];
                    }
                    if (best != NEG) sw = best + 1;
                }
                int start = (c == 0) ? 1 : NEG;
                int cur = same;
                if (sw > cur) cur = sw;
                if (start > cur) cur = start;
                newLen[c] = cur;
            }

            for (int c = 0; c <= k; c++) {
                if (newLen[c] > dp[c][x]) {
                    dp[c][x] = newLen[c];
                    // update best structures
                    if (newLen[c] > bestVal[c]) {
                        if (bestIdx[c] == x) {
                            bestVal[c] = newLen[c];
                        } else {
                            secondBest[c] = bestVal[c];
                            bestVal[c] = newLen[c];
                            bestIdx[c] = x;
                        }
                    } else if (x != bestIdx[c] && newLen[c] > secondBest[c]) {
                        secondBest[c] = newLen[c];
                    }
                }
                if (dp[c][x] > answer) answer = dp[c][x];
            }
        }

        return answer;
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
        n = len(nums)
        # compress values
        comp = {}
        idx = 0
        arr = []
        for v in nums:
            if v not in comp:
                comp[v] = idx
                idx += 1
            arr.append(comp[v])
        m = idx

        NEG = -10**9
        dp = [[NEG] * m for _ in range(k + 1)]

        best_len = [NEG] * (k + 1)   # max length for each change count
        best_val = [-1] * (k + 1)    # value achieving that max
        sec_len = [NEG] * (k + 1)    # second max length (different value)

        for x in arr:
            prev_vals = [dp[t][x] for t in range(k + 1)]

            for t in range(k, -1, -1):
                cur = prev_vals[t]

                # extend same value
                cand_extend = cur + 1 if cur > NEG // 2 else NEG

                # switch from different value (increase change count)
                cand_switch = NEG
                if t > 0:
                    max_len = best_len[t - 1]
                    max_val = best_val[t - 1]
                    if max_len > NEG // 2:
                        if max_val != x:
                            cand_switch = max_len + 1
                        else:
                            sec = sec_len[t - 1]
                            if sec > NEG // 2:
                                cand_switch = sec + 1

                # start new subsequence (only when no changes used yet)
                cand_start = 1 if t == 0 else NEG

                new_len = cur
                if cand_extend > new_len:
                    new_len = cand_extend
                if cand_switch > new_len:
                    new_len = cand_switch
                if cand_start > new_len:
                    new_len = cand_start

                dp[t][x] = new_len

            # update best and second best for each t
            for t in range(k + 1):
                val = dp[t][x]
                if val > best_len[t]:
                    if best_val[t] != x:
                        sec_len[t] = best_len[t]
                    best_len[t] = val
                    best_val[t] = x
                elif x != best_val[t] and val > sec_len[t]:
                    sec_len[t] = val

        return max(best_len)
```

## Python3

```python
import sys
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # compress values
        uniq = {}
        comp = []
        for v in nums:
            if v not in uniq:
                uniq[v] = len(uniq)
                comp.append(v)
        a = [uniq[v] for v in nums]
        m = len(uniq)

        dp = [[0] * m for _ in range(k + 1)]          # dp[c][value] = max length with at most c changes
        best_val = [-1] * (k + 1)                     # value achieving best_len
        best_len = [0] * (k + 1)                      # longest length for each c
        second_len = [0] * (k + 1)                    # second longest length for each c

        for x in a:
            for c in range(k, -1, -1):
                cur = dp[c][x]

                # extend same value (no extra change)
                cand_same = cur + 1 if cur > 0 else (1 if c == 0 else 0)

                best_candidate = cur
                if cand_same > best_candidate:
                    best_candidate = cand_same

                # change from a different value, consuming one change
                if c > 0:
                    if best_val[c - 1] != x:
                        other_best = best_len[c - 1]
                    else:
                        other_best = second_len[c - 1]

                    if other_best > 0:
                        cand_change = other_best + 1
                        if cand_change > best_candidate:
                            best_candidate = cand_change

                new_len = best_candidate
                if new_len > cur:
                    dp[c][x] = new_len
                    # update top two for this c
                    if best_val[c] == x:
                        best_len[c] = new_len
                    else:
                        if new_len > best_len[c]:
                            second_len[c] = best_len[c]
                            best_len[c] = new_len
                            best_val[c] = x
                        elif new_len > second_len[c]:
                            second_len[c] = new_len

        return max(best_len)
```

## C

```c
#include <stdlib.h>
#include <string.h>

int maximumLength(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    /* coordinate compression */
    int *vals = (int *)malloc(numsSize * sizeof(int));
    memcpy(vals, nums, numsSize * sizeof(int));
    qsort(vals, numsSize, sizeof(int), (int (*)(const void *, const void *))strcmp);
    int m = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || vals[i] != vals[i - 1]) {
            vals[m++] = vals[i];
        }
    }
    /* map original numbers to compressed indices */
    int *comp = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        int lo = 0, hi = m - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            if (vals[mid] == nums[i]) { comp[i] = mid; break; }
            else if (vals[mid] < nums[i]) lo = mid + 1;
            else hi = mid - 1;
        }
    }

    const int NEG_INF = -1000000000;
    int *dp = (int *)malloc((k + 1) * m * sizeof(int));
    for (int i = 0; i < (k + 1) * m; ++i) dp[i] = NEG_INF;

    int best1[51], best2[51], idx1[51];
    for (int t = 0; t <= k; ++t) {
        best1[t] = best2[t] = NEG_INF;
        idx1[t] = -1;
    }

    for (int i = 0; i < numsSize; ++i) {
        int x = comp[i];
        /* compute new dp values using previous state */
        for (int t = k; t >= 0; --t) {
            int old = dp[t * m + x];
            int cand = old;
            if (old > NEG_INF / 2) {
                if (old + 1 > cand) cand = old + 1;
            }
            if (t == 0) {
                if (cand < 1) cand = 1;          // start new subsequence
            } else {
                int best_not_x = (idx1[t - 1] != x) ? best1[t - 1] : best2[t - 1];
                if (best_not_x > NEG_INF / 2) {
                    if (best_not_x + 1 > cand) cand = best_not_x + 1;
                }
            }
            dp[t * m + x] = cand;
        }
        /* update top two maxima for each t */
        for (int t = 0; t <= k; ++t) {
            int val = dp[t * m + x];
            if (val > best1[t]) {
                if (idx1[t] != x) {
                    best2[t] = best1[t];
                }
                best1[t] = val;
                idx1[t] = x;
            } else if (val > best2[t] && idx1[t] != x) {
                best2[t] = val;
            }
        }
    }

    int ans = 0;
    for (int t = 0; t <= k; ++t) {
        if (best1[t] > ans) ans = best1[t];
    }

    free(vals);
    free(comp);
    free(dp);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumLength(int[] nums, int k) {
        const int NEG = -1000000000;
        // Compress values
        var map = new Dictionary<int, int>();
        int idCounter = 0;
        int n = nums.Length;
        int[] ids = new int[n];
        foreach (var v in nums) {
            if (!map.ContainsKey(v)) {
                map[v] = idCounter++;
            }
        }
        for (int i = 0; i < n; i++) {
            ids[i] = map[nums[i]];
        }
        int m = idCounter;
        // dp[value][c] = max length ending with this value using exactly c changes
        int[][] dp = new int[m][];
        for (int i = 0; i < m; i++) {
            dp[i] = new int[k + 1];
            for (int j = 0; j <= k; j++) dp[i][j] = NEG;
        }
        // best1[c], best2[c], bestVal1[c]
        int[] best1 = new int[k + 1];
        int[] best2 = new int[k + 1];
        int[] bestVal1 = new int[k + 1];
        for (int c = 0; c <= k; c++) {
            best1[c] = NEG;
            best2[c] = NEG;
            bestVal1[c] = -1;
        }
        int answer = 0;
        // Process each element
        for (int idx = 0; idx < n; idx++) {
            int x = ids[idx];
            // snapshot of dp[x][*]
            int[] old = new int[k + 1];
            for (int c = 0; c <= k; c++) old[c] = dp[x][c];
            // snapshot of best arrays before this element
            int[] prevBest1 = (int[])best1.Clone();
            int[] prevBest2 = (int[])best2.Clone();
            int[] prevVal1 = (int[])bestVal1.Clone();

            // start new subsequence with this single element
            if (dp[x][0] < 1) {
                dp[x][0] = 1;
                answer = Math.Max(answer, 1);
            }

            for (int c = 0; c <= k; c++) {
                // extend same value without adding a change
                if (old[c] != NEG) {
                    int cand = old[c] + 1;
                    if (cand > dp[x][c]) {
                        dp[x][c] = cand;
                        answer = Math.Max(answer, cand);
                    }
                }
                // transition from different value, adding a change
                if (c > 0) {
                    int bestDiff = prevVal1[c - 1] != x ? prevBest1[c - 1] : prevBest2[c - 1];
                    if (bestDiff != NEG) {
                        int cand = bestDiff + 1;
                        if (cand > dp[x][c]) {
                            dp[x][c] = cand;
                            answer = Math.Max(answer, cand);
                        }
                    }
                }
            }

            // Update best arrays with the possibly increased dp[x][*]
            for (int c = 0; c <= k; c++) {
                int val = dp[x][c];
                if (val > best1[c]) {
                    if (bestVal1[c] != x) {
                        best2[c] = best1[c];
                    }
                    best1[c] = val;
                    bestVal1[c] = x;
                } else if (val > best2[c] && bestVal1[c] != x) {
                    best2[c] = val;
                }
            }
        }
        return answer;
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
    const m = idx; // number of distinct values

    // dp[c][v] = max length ending with value v using exactly c changes
    const dp = Array.from({length: k + 1}, () => new Array(m).fill(-Infinity));

    // best and second best for each change count
    const bestVal = new Array(k + 1).fill(-Infinity);
    const bestIdx = new Array(k + 1).fill(-1);
    const secondBestVal = new Array(k + 1).fill(-Infinity);

    const updateBest = (c, valIdx, val) => {
        if (bestIdx[c] === -1) { // first entry
            bestIdx[c] = valIdx;
            bestVal[c] = val;
            return;
        }
        if (valIdx === bestIdx[c]) {
            bestVal[c] = val; // improve the current best
        } else {
            if (val > bestVal[c]) {
                secondBestVal[c] = bestVal[c];
                bestVal[c] = val;
                bestIdx[c] = valIdx;
            } else if (val > secondBestVal[c]) {
                secondBestVal[c] = val;
            }
        }
    };

    for (let pos = 0; pos < n; ++pos) {
        const x = comp[pos];
        const newVals = new Array(k + 1).fill(-Infinity);

        for (let c = 0; c <= k; ++c) {
            // extend same value without extra change
            let cand = dp[c][x] === -Infinity ? -Infinity : dp[c][x] + 1;

            if (c === 0) {
                // start new subsequence with this element
                cand = Math.max(cand, 1);
            } else {
                // transition from a different value, increasing change count
                let bestNotX;
                if (bestIdx[c - 1] !== x) {
                    bestNotX = bestVal[c - 1];
                } else {
                    bestNotX = secondBestVal[c - 1];
                }
                if (bestNotX !== -Infinity) {
                    cand = Math.max(cand, bestNotX + 1);
                }
            }
            newVals[c] = cand;
        }

        // apply updates and maintain best/second best
        for (let c = 0; c <= k; ++c) {
            if (newVals[c] > dp[c][x]) {
                dp[c][x] = newVals[c];
                updateBest(c, x, dp[c][x]);
            }
        }
    }

    let answer = 0;
    for (let c = 0; c <= k; ++c) {
        if (bestVal[c] > answer) answer = bestVal[c];
    }
    return answer;
};
```

## Typescript

```typescript
function maximumLength(nums: number[], k: number): number {
    const n = nums.length;
    // coordinate compression
    const map = new Map<number, number>();
    let id = 0;
    const comp = new Array(n);
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        if (!map.has(v)) map.set(v, id++);
        comp[i] = map.get(v)!;
    }
    const m = id;

    // dp[c][value] = longest length ending with this value using at most c changes
    const dp: number[][] = Array.from({ length: k + 1 }, () => new Array(m).fill(0));

    // best structures for each c
    const bestIdx = new Array(k + 1).fill(-1);
    const bestVal = new Array(k + 1).fill(0);
    const secondVal = new Array(k + 1).fill(0);

    for (let pos = 0; pos < n; ++pos) {
        const x = comp[pos];
        // snapshot of best info before processing this element
        const prevBestIdx = bestIdx.slice();
        const prevBestVal = bestVal.slice();
        const prevSecondVal = secondVal.slice();

        for (let c = 0; c <= k; ++c) {
            const prevLen = dp[c][x];
            const extLen = prevLen > 0 ? prevLen + 1 : 0;

            let changeLen = 0;
            if (c > 0) {
                if (prevBestIdx[c - 1] !== x) {
                    changeLen = prevBestVal[c - 1] + 1;
                } else {
                    changeLen = prevSecondVal[c - 1] + 1;
                }
            }

            const base = 1; // start new subsequence
            let newLen = Math.max(prevLen, extLen, changeLen, base);
            dp[c][x] = newLen;

            // update best structures for this c
            if (newLen > bestVal[c]) {
                if (bestIdx[c] === x) {
                    bestVal[c] = newLen;
                } else {
                    secondVal[c] = bestVal[c];
                    bestVal[c] = newLen;
                    bestIdx[c] = x;
                }
            } else if (x !== bestIdx[c] && newLen > secondVal[c]) {
                secondVal[c] = newLen;
            }
        }
    }

    return bestVal[k];
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
        // compress values to 0..m-1
        $map = [];
        $compressed = [];
        $idx = 0;
        foreach ($nums as $v) {
            if (!isset($map[$v])) {
                $map[$v] = $idx++;
            }
            $compressed[] = $map[$v];
        }
        $m = $idx; // number of distinct values

        // dp[c][value] = max length ending with value using exactly c changes
        $dp = [];
        for ($c = 0; $c <= $k; $c++) {
            $dp[$c] = array_fill(0, $m, 0);
        }

        // best1Len[c], best1Val[c]: max length and its value for change count c
        // best2Len[c]: second max length (value different from best1Val)
        $best1Len = array_fill(0, $k + 1, 0);
        $best1Val = array_fill(0, $k + 1, -1);
        $best2Len = array_fill(0, $k + 1, 0);

        foreach ($compressed as $x) {
            // snapshot of best arrays before this element
            $prevBest1Len = $best1Len;
            $prevBest1Val = $best1Val;
            $prevBest2Len = $best2Len;

            for ($c = 0; $c <= $k; $c++) {
                $old = $dp[$c][$x];
                $new = $old;

                // start new subsequence with this element
                if ($new < 1) $new = 1;

                // extend same value without extra change
                if ($old > 0 && $old + 1 > $new) {
                    $new = $old + 1;
                }

                // transition from a different value using one more change
                if ($c > 0) {
                    if ($prevBest1Val[$c - 1] != $x) {
                        $cand = $prevBest1Len[$c - 1] + 1;
                    } else {
                        $cand = $prevBest2Len[$c - 1] + 1;
                    }
                    if ($cand > $new) {
                        $new = $cand;
                    }
                }

                // update dp
                $dp[$c][$x] = $new;

                // maintain best1 and best2 for this c
                if ($new > $best1Len[$c]) {
                    $best2Len[$c] = $best1Len[$c];
                    $best1Len[$c] = $new;
                    $best1Val[$c] = $x;
                } elseif ($best1Val[$c] != $x && $new > $best2Len[$c]) {
                    $best2Len[$c] = $new;
                }
            }
        }

        // answer is max over at most k changes
        $ans = 0;
        for ($c = 0; $c <= $k; $c++) {
            if ($best1Len[$c] > $ans) $ans = $best1Len[$c];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int], _ k: Int) -> Int {
        // Coordinate compression
        var comp = [Int:Int]()
        var idx = 0
        for v in nums {
            if comp[v] == nil {
                comp[v] = idx
                idx += 1
            }
        }
        let m = comp.count
        // DP arrays
        var bestSame = Array(repeating: Array(repeating: 0, count: m), count: k + 1)
        var maxAll = Array(repeating: 0, count: k + 1)
        var secondMax = Array(repeating: 0, count: k + 1)
        var argMax = Array(repeating: -1, count: k + 1)

        for num in nums {
            guard let curIdx = comp[num] else { continue }
            // snapshot of global maxima before processing this element
            let prevMaxAll = maxAll
            let prevSecondMax = secondMax
            let prevArgMax = argMax

            for c in 0...k {
                var newLen = 0
                if c == 0 {
                    newLen = 1   // start a new subsequence
                }
                // extend with same value, no extra change
                let samePrev = bestSame[c][curIdx]
                if samePrev > 0 {
                    newLen = max(newLen, samePrev + 1)
                }
                // transition from different value, consumes one change
                if c > 0 && prevMaxAll[c - 1] > 0 {
                    let cand: Int
                    if prevArgMax[c - 1] != curIdx {
                        cand = prevMaxAll[c - 1] + 1
                    } else {
                        cand = prevSecondMax[c - 1] + 1
                    }
                    newLen = max(newLen, cand)
                }

                // update structures if we improved length for this value and change count
                if newLen > bestSame[c][curIdx] {
                    bestSame[c][curIdx] = newLen
                    if newLen > maxAll[c] {
                        secondMax[c] = maxAll[c]
                        maxAll[c] = newLen
                        argMax[c] = curIdx
                    } else if curIdx != argMax[c] && newLen > secondMax[c] {
                        secondMax[c] = newLen
                    }
                }
            }
        }

        return maxAll.max() ?? 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray, k: Int): Int {
        val n = nums.size
        // Coordinate compression
        val map = HashMap<Int, Int>()
        var idx = 0
        val comp = IntArray(n)
        for (i in 0 until n) {
            val v = nums[i]
            var id = map[v]
            if (id == null) {
                id = idx
                map[v] = idx++
            }
            comp[i] = id
        }
        val m = idx
        val dp = Array(k + 1) { IntArray(m) }
        val best = IntArray(k + 1)

        for (value in comp) {
            // snapshot of best before this element updates
            val prevBest = best.clone()
            // store previous dp values for this value
            val oldVals = IntArray(k + 1)
            for (c in 0..k) {
                oldVals[c] = dp[c][value]
            }
            for (c in 0..k) {
                var cur = oldVals[c] // not taking current element yet
                if (c == 0) {
                    if (cur < 1) cur = 1   // start new subsequence
                }
                if (oldVals[c] > 0) {
                    val cand = oldVals[c] + 1   // extend same value, no extra change
                    if (cand > cur) cur = cand
                }
                if (c > 0 && prevBest[c - 1] > 0) {
                    val cand = prevBest[c - 1] + 1   // change from different value
                    if (cand > cur) cur = cand
                }
                dp[c][value] = cur
            }
            // update global bests for each change count
            for (c in 0..k) {
                if (dp[c][value] > best[c]) best[c] = dp[c][value]
            }
        }

        var ans = 0
        for (c in 0..k) {
            if (best[c] > ans) ans = best[c]
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumLength(List<int> nums, int k) {
    // Coordinate compression
    final Map<int, int> comp = {};
    int idx = 0;
    final List<int> a = List.filled(nums.length, 0);
    for (int i = 0; i < nums.length; ++i) {
      final v = nums[i];
      if (!comp.containsKey(v)) {
        comp[v] = idx++;
      }
      a[i] = comp[v]!;
    }
    final int m = idx;
    // dp[t][value] = max length ending with value using exactly t changes
    final List<List<int>> dp =
        List.generate(k + 1, (_) => List.filled(m, -1));
    // best structures for each t
    final List<int> bestVal = List.filled(k + 1, -1);
    final List<int> bestIdx = List.filled(k + 1, -1);
    final List<int> secondBest = List.filled(k + 1, -1);

    for (final x in a) {
      // compute candidate new lengths based on previous state
      final List<int> newVals = List.filled(k + 1, -1);
      for (int t = 0; t <= k; ++t) {
        int cur = dp[t][x];
        int candLen = -1;
        if (cur != -1) candLen = cur + 1; // extend same value
        if (t == 0) {
          if (candLen < 1) candLen = 1; // start new subsequence
        }
        if (t > 0) {
          int candidate =
              bestIdx[t - 1] != x ? bestVal[t - 1] : secondBest[t - 1];
          if (candidate != -1) {
            final val = candidate + 1;
            if (val > candLen) candLen = val;
          }
        }
        newVals[t] = candLen;
      }

      // apply updates and maintain best structures
      for (int t = 0; t <= k; ++t) {
        final int nv = newVals[t];
        if (nv > dp[t][x]) {
          dp[t][x] = nv;
          if (bestIdx[t] == -1) {
            bestIdx[t] = x;
            bestVal[t] = nv;
          } else if (x == bestIdx[t]) {
            bestVal[t] = nv;
          } else {
            if (nv > bestVal[t]) {
              secondBest[t] = bestVal[t];
              bestVal[t] = nv;
              bestIdx[t] = x;
            } else if (nv > secondBest[t]) {
              secondBest[t] = nv;
            }
          }
        }
      }
    }

    int ans = 0;
    for (int t = 0; t <= k; ++t) {
      if (bestVal[t] > ans) ans = bestVal[t];
    }
    return ans;
  }
}
```

## Golang

```go
func maximumLength(nums []int, k int) int {
    n := len(nums)
    // compress values to [0, m-1]
    comp := make(map[int]int)
    idx := 0
    a := make([]int, n)
    for i, v := range nums {
        if _, ok := comp[v]; !ok {
            comp[v] = idx
            idx++
        }
        a[i] = comp[v]
    }
    m := idx

    const NEG = -1 << 60
    dp := make([][]int, k+1)
    for i := 0; i <= k; i++ {
        row := make([]int, m)
        for j := 0; j < m; j++ {
            row[j] = NEG
        }
        dp[i] = row
    }

    top1Val := make([]int, k+1) // best value for each change count
    top2Val := make([]int, k+1) // second best (different value)
    topIdx := make([]int, k+1)  // value index achieving top1
    for i := 0; i <= k; i++ {
        top1Val[i] = NEG
        top2Val[i] = NEG
        topIdx[i] = -1
    }

    for _, x := range a {
        // compute updates using tops from previous elements only
        for c := 0; c <= k; c++ {
            oldSame := dp[c][x]
            bestPrevExceptX := NEG
            if c > 0 {
                if topIdx[c-1] != x {
                    bestPrevExceptX = top1Val[c-1]
                } else {
                    bestPrevExceptX = top2Val[c-1]
                }
            }

            cand := NEG
            if c == 0 && cand < 1 {
                cand = 1 // start new subsequence
            }
            if oldSame > NEG/2 && oldSame+1 > cand {
                cand = oldSame + 1 // extend same value
            }
            if c > 0 && bestPrevExceptX > NEG/2 && bestPrevExceptX+1 > cand {
                cand = bestPrevExceptX + 1 // change from different value
            }

            if cand > dp[c][x] {
                dp[c][x] = cand
            }
        }

        // update top structures with the new dp values for this x
        for c := 0; c <= k; c++ {
            val := dp[c][x]
            if val > top1Val[c] {
                if topIdx[c] != x {
                    top2Val[c] = top1Val[c]
                }
                top1Val[c] = val
                topIdx[c] = x
            } else if x != topIdx[c] && val > top2Val[c] {
                top2Val[c] = val
            }
        }
    }

    ans := 0
    for c := 0; c <= k; c++ {
        if top1Val[c] > ans {
            ans = top1Val[c]
        }
    }
    return ans
}
```

## Ruby

```ruby
def maximum_length(nums, k)
  # Coordinate compression
  uniq_vals = nums.uniq
  idx_map = {}
  uniq_vals.each_with_index { |v, i| idx_map[v] = i }
  m = uniq_vals.size
  comp = nums.map { |v| idx_map[v] }

  dp = Array.new(k + 1) { Array.new(m, 0) }
  best = Array.new(k + 1, 0)

  comp.each do |x|
    prev_best = best.clone
    (0..k).each do |t|
      cur = dp[t][x]
      cand = cur + 1
      if t == 0
        cand = [cand, 1].max
      else
        cand = [cand, prev_best[t - 1] + 1].max
      end
      if cand > dp[t][x]
        dp[t][x] = cand
        best[t] = cand if cand > best[t]
      end
    end
  end

  best[k]
end
```

## Scala

```scala
object Solution {
  def maximumLength(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    // compress values to [0, m)
    val distinctVals = nums.distinct
    val idxMap = scala.collection.mutable.HashMap[Int, Int]()
    distinctVals.zipWithIndex.foreach { case (v, i) => idxMap(v) = i }
    val comp = nums.map(idxMap)

    val m = distinctVals.length
    val NEG = -1_000_000_000

    // dp[c][value] = longest subsequence ending with this value using exactly c changes
    val dp = Array.ofDim[Int](k + 1, m)
    var i = 0
    while (i <= k) {
      java.util.Arrays.fill(dp(i), NEG)
      i += 1
    }

    // best and second best lengths for each change count
    val bestVal = Array.fill(k + 1)(NEG)
    val bestIdx = Array.fill(k + 1)(-1)
    val secondBestVal = Array.fill(k + 1)(NEG)

    for (v <- comp) {
      // snapshot of best information before this element is processed
      val curBestVal = bestVal.clone()
      val curBestIdx = bestIdx.clone()
      val curSecondBestVal = secondBestVal.clone()

      var c = 0
      while (c <= k) {
        var newLen = dp(c)(v)

        // extend same value without extra change
        if (dp(c)(v) > NEG / 2) {
          newLen = math.max(newLen, dp(c)(v) + 1)
        }

        // start a new subsequence with this element alone (only for c == 0)
        if (c == 0) {
          newLen = math.max(newLen, 1)
        }

        // change from another value
        if (c > 0) {
          var maxOther = curBestVal(c - 1)
          if (curBestIdx(c - 1) == v) {
            maxOther = curSecondBestVal(c - 1)
          }
          if (maxOther > NEG / 2) {
            newLen = math.max(newLen, maxOther + 1)
          }
        }

        // update dp and best structures if improved
        if (newLen > dp(c)(v)) {
          dp(c)(v) = newLen
          val len = newLen
          if (len > bestVal(c)) {
            secondBestVal(c) = bestVal(c)
            bestVal(c) = len
            bestIdx(c) = v
          } else if (v != bestIdx(c) && len > secondBestVal(c)) {
            secondBestVal(c) = len
          }
        }

        c += 1
      }
    }

    var answer = 0
    var c = 0
    while (c <= k) {
      if (bestVal(c) > answer) answer = bestVal(c)
      c += 1
    }
    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // compress values to 0..m-1
        let mut uniq = nums.clone();
        uniq.sort_unstable();
        uniq.dedup();
        let m = uniq.len();
        use std::collections::HashMap;
        let mut id_map: HashMap<i32, usize> = HashMap::with_capacity(m);
        for (i, &v) in uniq.iter().enumerate() {
            id_map.insert(v, i);
        }
        let ks = k as usize;
        const NEG_INF: i32 = -1_000_000_000;

        // dp[t][value] = max length ending with this value using exactly t changes
        let mut dp = vec![vec![NEG_INF; m]; ks + 1];

        // best and second best for each t
        let mut best_len = vec![NEG_INF; ks + 1];
        let mut best_val = vec![usize::MAX; ks + 1];
        let mut second_best_len = vec![NEG_INF; ks + 1];
        let mut second_best_val = vec![usize::MAX; ks + 1];

        for &num in nums.iter() {
            let cur = *id_map.get(&num).unwrap();

            // compute new dp values for this element
            for t in 0..=ks {
                let old = dp[t][cur];
                let mut new_val = old;

                // extend same value block
                if old > NEG_INF / 2 {
                    new_val = (old + 1).max(new_val);
                }

                if t == 0 {
                    // start a fresh subsequence with this element
                    new_val = new_val.max(1);
                } else {
                    // transition from a different value, consuming one change
                    let mut best_prev = NEG_INF;
                    if best_val[t - 1] != cur {
                        best_prev = best_len[t - 1];
                    } else {
                        best_prev = second_best_len[t - 1];
                    }
                    if best_prev > NEG_INF / 2 {
                        new_val = (best_prev + 1).max(new_val);
                    }
                }

                dp[t][cur] = new_val;
            }

            // update best and second best for each t
            for t in 0..=ks {
                let val_dp = dp[t][cur];
                if val_dp > best_len[t] {
                    second_best_len[t] = best_len[t];
                    second_best_val[t] = best_val[t];
                    best_len[t] = val_dp;
                    best_val[t] = cur;
                } else if val_dp > second_best_len[t] && cur != best_val[t] {
                    second_best_len[t] = val_dp;
                    second_best_val[t] = cur;
                }
            }
        }

        *best_len.iter().max().unwrap()
    }
}
```

## Racket

```racket
(define/contract (maximum-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         ;; compress values to 0..V-1
         (unique (remove-duplicates nums))
         (mapping (make-hash))
         (cnt 0))
    (for ([v unique])
      (hash-set! mapping v cnt)
      (set! cnt (+ cnt 1)))
    (define V cnt)
    (define comp (map (lambda (v) (hash-ref mapping v)) nums))
    ;; dp[t][value] = longest subsequence ending with value using exactly t changes
    (define dp (make-vector (+ k 1) #f))
    (for ([t (in-range (+ k 1))])
      (vector-set! dp t (make-vector V 0)))
    ;; best and second best lengths for each t, together with index of best
    (define best_len   (make-vector (+ k 1) 0))
    (define best_idx   (make-vector (+ k 1) -1))
    (define second_len (make-vector (+ k 1) 0))
    ;; process each element
    (for ([x comp])
      (for ([t (in-range k -1 -1)]) ; descending t = k .. 0
        (let* ((row (vector-ref dp t))
               (old (vector-ref row x))
               ;; extend same value without extra change
               (cand-same (if (> old 0) (+ old 1) 1))
               ;; start new run, increasing changes by 1
               (cand-new (if (> t 0)
                             (let ((bestv (if (= (vector-ref best_idx (- t 1)) x)
                                             (vector-ref second_len (- t 1))
                                             (vector-ref best_len (- t 1)))))
                               (+ bestv 1))
                             -1000000))
               (new-val (max old cand-same cand-new)))
          ;; update dp[t][x] if improved
          (when (> new-val old)
            (vector-set! row x new-val))
          ;; maintain best / second best for this t
          (let ((cur-best   (vector-ref best_len t))
                (cur-idx    (vector-ref best_idx t))
                (cur-second (vector-ref second_len t)))
            (cond [(> new-val cur-best)
                   (vector-set! second_len t cur-best)
                   (vector-set! best_len   t new-val)
                   (vector-set! best_idx   t x)]
                  [(and (> new-val cur-second) (not (= x cur-idx)))
                   (vector-set! second_len t new-val)])))))
    ;; answer is the maximum length achievable with at most k changes
    (let loop ((t 0) (ans 0))
      (if (> t (+ k 0))
          ans
          (loop (+ t 1) (max ans (vector-ref best_len t)))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_length/2]).
-spec maximum_length(Nums :: [integer()], K :: integer()) -> integer().
maximum_length(Nums, K) ->
    DPMaps0 = erlang:make_tuple(K + 1, #{}),
    BestVals0 = erlang:make_tuple(K + 1, -1),
    BestLens0 = erlang:make_tuple(K + 1, 0),
    SecondBest0 = erlang:make_tuple(K + 1, 0),

    {_, _, FinalBestLens, _} =
        lists:foldl(
          fun(X, {DPMaps, BVals, BLens, SB}) ->
              OldBVals = BVals,
              OldBLens = BLens,
              OldSB = SB,

              FoldFun = fun(I, {AccDP, AccBV, AccBL, AccSB}) ->
                  Index = I + 1,
                  OldMap = element(Index, AccDP),
                  OldLenSame = maps:get(X, OldMap, 0),

                  CandSame = OldLenSame + 1,

                  CandDiff =
                      case I of
                          0 -> 0;
                          _ ->
                              PrevIdx = I,
                              BestValPrev = element(PrevIdx, OldBVals),
                              BestLenPrev = element(PrevIdx, OldBLens),
                              SecondBestPrev = element(PrevIdx, OldSB),
                              DiffBase =
                                  if BestValPrev == X -> SecondBestPrev;
                                     true -> BestLenPrev
                                  end,
                              DiffBase + 1
                      end,

                  NewLen = erlang:max(CandSame, CandDiff),

                  UpdatedMap =
                      case NewLen > OldLenSame of
                          true -> maps:put(X, NewLen, OldMap);
                          false -> OldMap
                      end,
                  AccDP1 = setelement(Index, AccDP, UpdatedMap),

                  BestValI = element(Index, AccBV),
                  BestLenI = element(Index, AccBL),
                  SecondBestI = element(Index, AccSB),

                  {AccBV1, AccBL1, AccSB1} =
                      if NewLen > OldLenSame ->
                              if X == BestValI ->
                                      {AccBV,
                                       setelement(Index, AccBL, NewLen),
                                       AccSB};
                                 NewLen > BestLenI ->
                                      {setelement(Index, AccBV, X),
                                       setelement(Index, AccBL, NewLen),
                                       setelement(Index, AccSB, BestLenI)};
                                 NewLen > SecondBestI ->
                                      {AccBV,
                                       AccBL,
                                       setelement(Index, AccSB, NewLen)};
                                 true ->
                                      {AccBV, AccBL, AccSB}
                              end;
                         true -> {AccBV, AccBL, AccSB}
                      end,

                  {AccDP1, AccBV1, AccBL1, AccSB1}
              end,
              Indices = lists:seq(0, K),
              lists:foldl(FoldFun, {DPMaps, BVals, BLens, SB}, Indices)
          end,
          {DPMaps0, BestVals0, BestLens0, SecondBest0},
          Nums),

    MaxLen = lists:max(tuple_to_list(FinalBestLens)),
    MaxLen.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer], k :: integer) :: integer
  def maximum_length(nums, k) do
    # Coordinate compression
    uniq_vals = Enum.uniq(nums)
    val_to_idx =
      uniq_vals
      |> Enum.with_index()
      |> Enum.into(%{}, fn {v, i} -> {v, i} end)

    comp_nums = Enum.map(nums, &Map.get(val_to_idx, &1))
    m = length(uniq_vals)

    # Initialize DP structures
    dp = for _ <- 0..k, do: %{}
    max_len_arr = :array.new(k + 1, default: 0)
    max_val_arr = :array.new(k + 1, default: -1)
    second_max_arr = :array.new(k + 1, default: 0)

    state = %{dp: dp, max_len: max_len_arr, max_val: max_val_arr, second_max: second_max_arr}

    # Process each element
    final_state =
      Enum.reduce(comp_nums, state, fn x, st ->
        {new_dp, new_ml, new_mv, new_sm} =
          Enum.reduce(Enum.reverse(0..k), {st.dp, st.max_len, st.max_val, st.second_max},
            fn t,
               {dp_acc, ml_arr, mv_arr, sm_arr} = acc ->

              dp_t = Enum.at(dp_acc, t)
              old = Map.get(dp_t, x, 0)

              cand_same =
                if old > 0 do
                  old + 1
                else
                  if t == 0, do: 1, else: 0
                end

              best = max(old, cand_same)

              if t >= 1 do
                mv_prev = :array.get(t - 1, mv_arr)
                ml_prev = :array.get(t - 1, ml_arr)
                sm_prev = :array.get(t - 1, sm_arr)

                other_best =
                  if mv_prev != x do
                    ml_prev
                  else
                    sm_prev
                  end

                best =
                  if other_best > 0 do
                    max(best, other_best + 1)
                  else
                    best
                  end
              end

              new_val = best

              if new_val > old do
                dp_t2 = Map.put(dp_t, x, new_val)
                dp_acc = List.replace_at(dp_acc, t, dp_t2)

                ml = :array.get(t, ml_arr)
                mv = :array.get(t, mv_arr)
                sm = :array.get(t, sm_arr)

                cond do
                  new_val > ml ->
                    ml_arr = :array.set(t, new_val, ml_arr)
                    sm_arr = :array.set(t, ml, sm_arr)
                    mv_arr = :array.set(t, x, mv_arr)
                    {dp_acc, ml_arr, mv_arr, sm_arr}

                  x == mv ->
                    ml_arr = :array.set(t, new_val, ml_arr)
                    {dp_acc, ml_arr, mv_arr, sm_arr}

                  new_val > sm ->
                    sm_arr = :array.set(t, new_val, sm_arr)
                    {dp_acc, ml_arr, mv_arr, sm_arr}

                  true ->
                    {dp_acc, ml_arr, mv_arr, sm_arr}
                end
              else
                acc
              end
            end)

        %{dp: new_dp, max_len: new_ml, max_val: new_mv, second_max: new_sm}
      end)

    # Compute answer
    Enum.reduce(0..k, 0, fn t, acc ->
      max(acc, :array.get(t, final_state.max_len))
    end)
  end
end
```

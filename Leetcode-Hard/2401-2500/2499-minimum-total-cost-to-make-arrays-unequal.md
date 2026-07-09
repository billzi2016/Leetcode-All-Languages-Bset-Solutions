# 2499. Minimum Total Cost to Make Arrays Unequal

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minimumTotalCost(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        // feasibility check
        vector<int> cnt1(n + 1, 0), cnt2(n + 1, 0);
        for (int x : nums1) ++cnt1[x];
        for (int x : nums2) ++cnt2[x];
        for (int v = 1; v <= n; ++v) {
            if (cnt1[v] > n - cnt2[v]) return -1;
        }

        long long sumBad = 0;
        vector<int> badIdx;
        unordered_map<int,int> badValCnt;
        for (int i = 0; i < n; ++i) {
            if (nums1[i] == nums2[i]) {
                sumBad += i;
                badIdx.push_back(i);
                ++badValCnt[nums1[i]];
            }
        }

        int m = badIdx.size();
        if (m == 0) return 0;

        // if number of bad positions is even, we can pair them without extra cost
        if (m % 2 == 0) return sumBad;

        // compute cmax and minBadDiffIdx
        int cmax = 0;
        for (auto &p : badValCnt) cmax = max(cmax, p.second);

        int minBadDiffIdx = INT_MAX;
        if ((int)badValCnt.size() > 1) {
            // there exists at least two distinct values among bads
            for (int idx : badIdx) {
                if (badValCnt[nums1[idx]] < m) { // its value not covering all bads
                    minBadDiffIdx = min(minBadDiffIdx, idx);
                }
            }
        }

        // compute minimal good index that can serve as buffer
        int minGoodIdx = INT_MAX;
        for (int i = 0; i < n; ++i) {
            if (nums1[i] != nums2[i]) { // good position
                // need a bad value different from nums1[i]
                if ((int)badValCnt.size() == 0) continue;
                if (badValCnt[nums1[i]] < m) { // there exists some bad with different value
                    minGoodIdx = min(minGoodIdx, i);
                }
            }
        }

        long long extra = LLONG_MAX;
        // candidate using good index
        if (minGoodIdx != INT_MAX) extra = min(extra, (long long)minGoodIdx);
        // candidate using bad index as buffer: possible only when after removing a pair we still have another distinct value left
        // This is feasible when the most frequent bad value count <= m-2
        if ((int)badValCnt.size() > 1 && cmax <= m - 2 && minBadDiffIdx != INT_MAX) {
            extra = min(extra, (long long)minBadDiffIdx);
        }

        if (extra == LLONG_MAX) return -1;
        return sumBad + extra;
    }
};
```

## Java

```java
class Solution {
    public long minimumTotalCost(int[] nums1, int[] nums2) {
        int n = nums1.length;
        boolean[] isBad = new boolean[n];
        long sumBad = 0L;
        int[] freq = new int[n + 2]; // values are in [1, n]
        int m = 0;
        for (int i = 0; i < n; i++) {
            if (nums1[i] == nums2[i]) {
                isBad[i] = true;
                sumBad += i;
                freq[nums1[i]]++;
                m++;
            }
        }
        if (m == 0) return 0L;

        int maxFreq = 0, dominantVal = 0;
        for (int v = 1; v <= n; v++) {
            if (freq[v] > maxFreq) {
                maxFreq = freq[v];
                dominantVal = v;
            }
        }

        // If we can derange using only bad positions
        if (maxFreq * 2 <= m) {
            return sumBad;
        }

        int excess = maxFreq * 2 - m; // number of good indices needed
        long sumGood = 0L;
        int taken = 0;
        for (int i = 0; i < n && taken < excess; i++) {
            if (!isBad[i] && nums1[i] != nums2[i]
                    && nums1[i] != dominantVal && dominantVal != nums2[i]) {
                sumGood += i;
                taken++;
            }
        }

        if (taken < excess) return -1L;
        return sumBad + sumGood;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTotalCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        max_val = n  # values are in [1, n]
        occ1 = [0] * (max_val + 1)   # count of each value in nums1 within selected set
        occ2 = [0] * (max_val + 1)   # count of each value in nums2 within selected set

        bad_indices = []
        good = []  # list of (index, val1, val2)

        for i in range(n):
            if nums1[i] == nums2[i]:
                bad_indices.append(i)
                v = nums1[i]
                occ1[v] += 1
                occ2[v] += 1
            else:
                good.append((i, nums1[i], nums2[i]))

        total_size = len(bad_indices)
        total_cost = sum(bad_indices)

        cur_max = 0
        for v in range(1, max_val + 1):
            s = occ1[v] + occ2[v]
            if s > cur_max:
                cur_max = s

        good.sort(key=lambda x: x[0])
        ptr = 0
        min_idx_in_set = min(bad_indices) if bad_indices else float('inf')

        while True:
            if cur_max <= total_size:
                # feasible, compute final cost considering parity
                extra = 0
                if total_size % 2 == 1:
                    extra = min_idx_in_set if min_idx_in_set != float('inf') else 0
                return total_cost + extra

            if ptr >= len(good):
                return -1

            i, a, b = good[ptr]
            ptr += 1

            total_size += 1
            total_cost += i
            if i < min_idx_in_set:
                min_idx_in_set = i

            occ1[a] += 1
            occ2[b] += 1

            s = occ1[a] + occ2[a]
            if s > cur_max:
                cur_max = s
            s = occ1[b] + occ2[b]
            if s > cur_max:
                cur_max = s
```

## Python3

```python
class Solution:
    def minimumTotalCost(self, nums1, nums2):
        n = len(nums1)
        same_cnt = {}
        forced_sum = 0
        forced_cnt = 0
        for i in range(n):
            if nums1[i] == nums2[i]:
                forced_sum += i
                forced_cnt += 1
                same_cnt[nums1[i]] = same_cnt.get(nums1[i], 0) + 1

        # feasibility check
        from collections import Counter
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        for v, c in cnt1.items():
            if c > n - cnt2.get(v, 0):
                return -1

        max_need = 0
        for v, sc in same_cnt.items():
            need = 2 * sc - forced_cnt
            if need > max_need:
                max_need = need
        extra_needed = max(0, max_need)

        if extra_needed == 0:
            return forced_sum

        # values that cannot appear in chosen extra indices
        critical_vals = {v for v, sc in same_cnt.items() if 2 * sc - forced_cnt == extra_needed}

        candidates = []
        for i in range(n):
            if nums1[i] != nums2[i]:
                if nums1[i] not in critical_vals and nums2[i] not in critical_vals:
                    candidates.append(i)

        if len(candidates) < extra_needed:
            return -1

        candidates.sort()
        extra_sum = sum(candidates[:extra_needed])
        return forced_sum + extra_sum
```

## C

```c
#include <stddef.h>

long long minimumTotalCost(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size;
    // frequencies up to n (values are 1..n)
    int *freq1 = (int*)calloc(n + 1, sizeof(int));
    int *freq2 = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i < n; ++i) {
        freq1[nums1[i]]++;
        freq2[nums2[i]]++;
    }
    // feasibility check
    for (int v = 1; v <= n; ++v) {
        if (freq1[v] > n - freq2[v]) {
            free(freq1);
            free(freq2);
            return -1;
        }
    }

    // collect bad indices and count their values
    int *badIdx = (int*)malloc(n * sizeof(int));
    int badCnt = 0;
    int *cntBadVal = (int*)calloc(n + 1, sizeof(int));

    for (int i = 0; i < n; ++i) {
        if (nums1[i] == nums2[i]) {
            badIdx[badCnt++] = i;
            cntBadVal[nums1[i]]++;
        }
    }

    if (badCnt == 0) {
        free(freq1);
        free(freq2);
        free(badIdx);
        free(cntBadVal);
        return 0;
    }

    // find value with max frequency among bad positions
    int maxVal = -1, maxFreq = 0;
    for (int v = 1; v <= n; ++v) {
        if (cntBadVal[v] > maxFreq) {
            maxFreq = cntBadVal[v];
            maxVal = v;
        }
    }

    // minimal cost starts with sum of all bad indices
    long long totalCost = 0;
    for (int i = 0; i < badCnt; ++i) totalCost += badIdx[i];

    // number of good positions that must be used as partners
    int needGood = 2 * maxFreq - badCnt;
    if (needGood < 0) needGood = 0;

    if (needGood > 0) {
        // collect eligible good indices: nums1!=nums2, and both values differ from maxVal
        int collected = 0;
        for (int i = 0; i < n && collected < needGood; ++i) {
            if (nums1[i] != nums2[i] && nums1[i] != maxVal && nums2[i] != maxVal) {
                totalCost += i;
                ++collected;
            }
        }
        if (collected < needGood) { // should not happen due to feasibility
            free(freq1);
            free(freq2);
            free(badIdx);
            free(cntBadVal);
            return -1;
        }
    }

    free(freq1);
    free(freq2);
    free(badIdx);
    free(cntBadVal);
    return totalCost;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MinimumTotalCost(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        List<int> badIndices = new List<int>();
        long sumBad = 0;
        Dictionary<int, int> freq = new Dictionary<int, int>();
        
        for (int i = 0; i < n; i++) {
            if (nums1[i] == nums2[i]) {
                badIndices.Add(i);
                sumBad += i;
                if (!freq.ContainsKey(nums1[i])) freq[nums1[i]] = 0;
                freq[nums1[i]]++;
            }
        }
        
        int m = badIndices.Count;
        if (m == 0) return 0L;
        
        // find dominant value and its count
        int domVal = -1, maxCount = 0;
        foreach (var kv in freq) {
            if (kv.Value > maxCount) {
                maxCount = kv.Value;
                domVal = kv.Key;
            }
        }
        
        // If dominant appears more than half of bad positions, need an extra good index
        if (maxCount > m / 2) {
            int minGoodIdx = int.MaxValue;
            for (int i = 0; i < n; i++) {
                if (nums1[i] != nums2[i]) { // good position
                    if (nums1[i] != domVal && nums2[i] != domVal) {
                        if (i < minGoodIdx) minGoodIdx = i;
                    }
                }
            }
            if (minGoodIdx == int.MaxValue) return -1L;
            return sumBad + minGoodIdx;
        } else {
            return sumBad;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minimumTotalCost = function(nums1, nums2) {
    const n = nums1.length;
    const bad = [];
    const good = [];
    for (let i = 0; i < n; ++i) {
        if (nums1[i] === nums2[i]) bad.push(i);
        else good.push(i);
    }
    const m = bad.length;
    if (m === 0) return 0;

    let sumBad = 0;
    for (const idx of bad) sumBad += idx;

    // frequency of values at bad positions
    const freq = new Map();
    for (const idx of bad) {
        const val = nums1[idx]; // same as nums2[idx]
        freq.set(val, (freq.get(val) || 0) + 1);
    }

    let maxFreq = 0;
    let vMax = null;
    for (const [val, cnt] of freq.entries()) {
        if (cnt > maxFreq) {
            maxFreq = cnt;
            vMax = val;
        }
    }

    // If we can derange within bad positions
    if (maxFreq <= Math.floor(m / 2)) {
        return sumBad;
    }

    const need = 2 * maxFreq - m; // number of bad positions that must swap with good ones

    const compatible = [];
    for (const idx of good) {
        if (nums1[idx] !== vMax && nums2[idx] !== vMax) {
            compatible.push(idx);
        }
    }

    if (need > compatible.length) return -1;

    compatible.sort((a, b) => a - b);
    let extra = 0;
    for (let i = 0; i < need; ++i) {
        extra += compatible[i];
    }

    return sumBad + extra;
};
```

## Typescript

```typescript
function minimumTotalCost(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    // Global feasibility check
    const cnt1 = new Map<number, number>();
    const cnt2 = new Map<number, number>();
    for (let v of nums1) cnt1.set(v, (cnt1.get(v) ?? 0) + 1);
    for (let v of nums2) cnt2.set(v, (cnt2.get(v) ?? 0) + 1);
    for (let [v, c1] of cnt1.entries()) {
        const c2 = cnt2.get(v) ?? 0;
        if (c1 > n - c2) return -1;
    }

    const badIndices: number[] = [];
    const goodUsefulIndices: number[] = []; // good indices with value != vMax
    const freqBad = new Map<number, number>();
    for (let i = 0; i < n; ++i) {
        if (nums1[i] === nums2[i]) {
            badIndices.push(i);
            freqBad.set(nums1[i], (freqBad.get(nums1[i]) ?? 0) + 1);
        }
    }

    if (badIndices.length === 0) return 0;

    // Find value with maximum frequency among bad positions
    let vMax = -1;
    let maxBad = 0;
    for (let [v, cnt] of freqBad.entries()) {
        if (cnt > maxBad) {
            maxBad = cnt;
            vMax = v;
        }
    }

    // Collect good indices that can serve as partners (value != vMax)
    for (let i = 0; i < n; ++i) {
        if (nums1[i] !== nums2[i] && nums1[i] !== vMax) {
            goodUsefulIndices.push(i);
        }
    }

    const B = badIndices.length;
    const extraNeeded = Math.max(0, 2 * maxBad - B);
    if (extraNeeded > goodUsefulIndices.length) return -1;

    // Compute total cost: sum of all bad indices + smallest extraNeeded useful good indices
    let totalCost = 0;
    for (let idx of badIndices) totalCost += idx;
    for (let i = 0; i < extraNeeded; ++i) {
        totalCost += goodUsefulIndices[i];
    }
    return totalCost;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minimumTotalCost($nums1, $nums2) {
        $n = count($nums1);
        // Frequency check for feasibility
        $freq1 = array_fill(0, $n + 1, 0);
        $freq2 = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $freq1[$nums1[$i]]++;
            $freq2[$nums2[$i]]++;
        }
        for ($v = 1; $v <= $n; ++$v) {
            if ($freq1[$v] > $n - $freq2[$v]) {
                return -1;
            }
        }

        // Collect bad (equal) and good (different) indices
        $bad = [];
        $good = [];
        for ($i = 0; $i < $n; ++$i) {
            if ($nums1[$i] == $nums2[$i]) {
                $bad[] = $i;
            } else {
                $good[] = $i;
            }
        }

        if (empty($bad)) return 0;

        sort($bad);
        sort($good);

        // Map from value to queue of bad indices having that value
        $badMap = [];
        foreach ($bad as $idx) {
            $v = $nums1[$idx]; // same as nums2[idx]
            if (!isset($badMap[$v])) $badMap[$v] = new SplQueue();
            $badMap[$v]->enqueue($idx);
        }

        $usedGood = [];
        $extraCost = 0;
        foreach ($good as $gIdx) {
            // Try to match this good index with any pending bad whose value differs from both nums1[gIdx] and nums2[gIdx]
            $matched = false;
            foreach ($badMap as $val => $queue) {
                if ($queue->isEmpty()) continue;
                if ($nums1[$gIdx] != $val && $nums2[$gIdx] != $val) {
                    // match
                    $queue->dequeue();
                    $extraCost += $gIdx;
                    $matched = true;
                    break;
                }
            }
            if ($matched) {
                $usedGood[] = $gIdx;
            }
        }

        // Remaining bad indices (could not be matched with good ones)
        $remainingBad = [];
        foreach ($badMap as $queue) {
            while (!$queue->isEmpty()) {
                $remainingBad[] = $queue->dequeue();
            }
        }

        // Pair remaining bads among themselves
        // Since feasibility guarantees we can resolve them, the minimal extra cost is sum of their indices
        foreach ($remainingBad as $idx) {
            $extraCost += $idx;
        }

        // Total cost is sum of all involved indices (each swap adds both indices)
        $total = 0;
        foreach ($bad as $bIdx) $total += $bIdx;
        $total += $extraCost;

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTotalCost(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        // Feasibility check
        var cnt1 = [Int:Int]()
        var cnt2 = [Int:Int]()
        for v in nums1 { cnt1[v, default: 0] += 1 }
        for v in nums2 { cnt2[v, default: 0] += 1 }
        for (v, c1) in cnt1 {
            let c2 = cnt2[v] ?? 0
            if c1 > n - c2 { return -1 }
        }
        
        var badIndices = [Int]()
        var freqInBad = [Int:Int]()   // value -> count among bad positions
        var goodMinIndexForDom: Int? = nil   // will be set later after dom known
        
        for i in 0..<n {
            if nums1[i] == nums2[i] {
                badIndices.append(i)
                let v = nums1[i]
                freqInBad[v, default: 0] += 1
            }
        }
        
        if badIndices.isEmpty { return 0 }
        
        // find dominant value in bad positions
        var domValue = -1
        var maxFreq = 0
        for (v, c) in freqInBad {
            if c > maxFreq {
                maxFreq = c
                domValue = v
            }
        }
        
        // sum of bad indices
        var sumBad: Int64 = 0
        for idx in badIndices { sumBad += Int64(idx) }
        
        let totalBad = badIndices.count
        if maxFreq * 2 <= totalBad {
            return Int(sumBad)
        }
        
        // need extra swaps using a good position whose value != domValue
        var gMin: Int? = nil
        for i in 0..<n {
            if nums1[i] != nums2[i] && nums1[i] != domValue {
                if let cur = gMin {
                    if i < cur { gMin = i }
                } else {
                    gMin = i
                }
            }
        }
        guard let hub = gMin else { return -1 }
        
        let excess = 2 * maxFreq - totalBad   // number of bad positions that must use the hub
        let answer = sumBad + Int64(excess) * Int64(hub)
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTotalCost(nums1: IntArray, nums2: IntArray): Long {
        val n = nums1.size
        var sumBad = 0L
        var totalBad = 0
        val freq = IntArray(n + 1)
        for (i in 0 until n) {
            if (nums1[i] == nums2[i]) {
                sumBad += i.toLong()
                totalBad++
                freq[nums1[i]]++
            }
        }
        if (totalBad == 0) return 0L

        var maxFreq = 0
        var dominantVal = 0
        for (v in 1..n) {
            if (freq[v] > maxFreq) {
                maxFreq = freq[v]
                dominantVal = v
            }
        }

        // Need an extra helper index when a value dominates the bad positions
        return if (maxFreq > totalBad - maxFreq) {
            var minHelperIdx = Int.MAX_VALUE
            for (i in 0 until n) {
                if (nums1[i] != nums2[i] && nums1[i] != dominantVal) {
                    if (i < minHelperIdx) minHelperIdx = i
                }
            }
            if (minHelperIdx == Int.MAX_VALUE) -1L else sumBad + minHelperIdx.toLong()
        } else {
            sumBad
        }
    }
}
```

## Dart

```dart
class Solution {
  int minimumTotalCost(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    List<int> badIndices = [];
    Map<int, int> freq = {};
    for (int i = 0; i < n; ++i) {
      if (nums1[i] == nums2[i]) {
        badIndices.add(i);
        freq[nums1[i]] = (freq[nums1[i]] ?? 0) + 1;
      }
    }

    int totalBad = badIndices.length;
    if (totalBad == 0) return 0;

    int maxFreq = 0;
    int vMax = 0;
    freq.forEach((key, value) {
      if (value > maxFreq) {
        maxFreq = value;
        vMax = key;
      }
    });

    int leftover = 2 * maxFreq - totalBad;
    if (leftover < 0) leftover = 0;

    int sumB = 0;
    for (int idx in badIndices) sumB += idx;

    if (leftover == 0) return sumB;

    List<int> candidates = [];
    for (int i = 0; i < n; ++i) {
      if (nums1[i] != nums2[i]) {
        if (nums1[i] != vMax && nums2[i] != vMax) {
          candidates.add(i);
        }
      }
    }

    if (candidates.length < leftover) return -1;

    int extra = 0;
    for (int i = 0; i < leftover; ++i) {
      extra += candidates[i];
    }

    return sumB + extra;
  }
}
```

## Golang

```go
func minimumTotalCost(nums1 []int, nums2 []int) int64 {
    n := len(nums1)
    cnt1 := make([]int, n+2)
    cnt2 := make([]int, n+2)
    for i := 0; i < n; i++ {
        cnt1[nums1[i]]++
        cnt2[nums2[i]]++
    }
    for v := 1; v <= n; v++ {
        if cnt1[v]+cnt2[v] > n {
            return -1
        }
    }

    badIdx := make([]int, 0)
    freqBad := make([]int, n+2)
    var sumBad int64 = 0
    for i := 0; i < n; i++ {
        if nums1[i] == nums2[i] {
            badIdx = append(badIdx, i)
            sumBad += int64(i)
            freqBad[nums1[i]]++
        }
    }

    m := len(badIdx)
    if m == 0 {
        return 0
    }

    // find value with maximum frequency among bad positions
    maxFreq := 0
    dominantVal := -1
    for v := 1; v <= n; v++ {
        if freqBad[v] > maxFreq {
            maxFreq = freqBad[v]
            dominantVal = v
        }
    }

    // number of bad positions that cannot be paired internally
    leftover := 2*maxFreq - m
    if leftover < 0 {
        leftover = 0
    }

    var extra int64 = 0
    if leftover > 0 {
        eligible := make([]int, 0)
        for i := 0; i < n; i++ {
            if nums1[i] != dominantVal && nums2[i] != dominantVal {
                eligible = append(eligible, i)
            }
        }
        if len(eligible) < leftover {
            return -1
        }
        for k := 0; k < leftover; k++ {
            extra += int64(eligible[k])
        }
    }

    return sumBad + extra
}
```

## Ruby

```ruby
def minimum_total_cost(nums1, nums2)
  n = nums1.length
  cnt2 = Hash.new(0)
  cnt1 = Hash.new(0)
  bad_sum = 0
  bad_cnt = 0
  freq_bad = Hash.new(0)

  (0...n).each do |i|
    v1 = nums1[i]
    v2 = nums2[i]
    cnt1[v1] += 1
    cnt2[v2] += 1
    if v1 == v2
      bad_sum += i
      bad_cnt += 1
      freq_bad[v1] += 1
    end
  end

  # overall feasibility check
  cnt1.each do |val, c|
    return -1 if c > n - cnt2[val]
  end

  max_cnt = 0
  v_max = nil
  freq_bad.each do |val, c|
    if c > max_cnt
      max_cnt = c
      v_max = val
    end
  end

  needed = [0, 2 * max_cnt - bad_cnt].max
  return bad_sum if needed == 0

  candidates = []
  (0...n).each do |i|
    next if nums1[i] == v_max || nums2[i] == v_max
    candidates << i
  end
  candidates.sort!
  return -1 if candidates.size < needed

  extra = candidates[0, needed].sum
  bad_sum + extra
end
```

## Scala

```scala
object Solution {
    def minimumTotalCost(nums1: Array[Int], nums2: Array[Int]): Long = {
        val n = nums1.length
        // overall feasibility check
        val cnt1 = new Array[Int](n + 1)
        val cnt2 = new Array[Int](n + 1)
        var i = 0
        while (i < n) {
            cnt1(nums1(i)) += 1
            cnt2(nums2(i)) += 1
            i += 1
        }
        var v = 1
        while (v <= n) {
            if (cnt1(v) + cnt2(v) > n) return -1L
            v += 1
        }

        // collect bad positions where nums1[i] == nums2[i]
        val badIndices = new scala.collection.mutable.ArrayBuffer[Int]()
        var sumBad: Long = 0L
        i = 0
        while (i < n) {
            if (nums1(i) == nums2(i)) {
                badIndices += i
                sumBad += i.toLong
            }
            i += 1
        }

        val totalBad = badIndices.size
        if (totalBad == 0) return 0L

        // frequency of values among bad positions
        val freqBad = new Array[Int](n + 1)
        var maxFreq = 0
        var dominantVal = -1
        for (idx <- badIndices) {
            val value = nums1(idx)
            freqBad(value) += 1
            if (freqBad(value) > maxFreq) {
                maxFreq = freqBad(value)
                dominantVal = value
            }
        }

        // if we can rearrange within bad positions alone
        if (maxFreq <= totalBad - maxFreq) return sumBad

        // need external good indices
        val need = maxFreq - (totalBad - maxFreq) // positive
        // collect eligible good indices (where nums1[i] != dominantVal)
        val goodIndices = new scala.collection.mutable.ArrayBuffer[Int]()
        i = 0
        while (i < n) {
            if (nums1(i) != nums2(i) && nums1(i) != dominantVal) {
                goodIndices += i
            }
            i += 1
        }
        // sort to get smallest indices
        scala.util.Sorting.quickSort(goodIndices.toArray)
        var extraSum: Long = 0L
        var taken = 0
        while (taken < need && taken < goodIndices.size) {
            extraSum += goodIndices(taken).toLong
            taken += 1
        }
        // In theory feasibility guarantees enough indices; otherwise impossible
        if (taken < need) return -1L

        sumBad + extraSum
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn minimum_total_cost(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let n = nums1.len();
        // collect bad indices where values are equal
        let mut bad: Vec<usize> = Vec::new();
        for i in 0..n {
            if nums1[i] == nums2[i] {
                bad.push(i);
            }
        }
        if bad.is_empty() {
            return 0;
        }

        // frequency of values among bad positions
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for &i in &bad {
            *freq.entry(nums1[i]).or_insert(0) += 1;
        }
        // dominant value and its count
        let (mut dom, mut maxcnt) = (0i32, 0usize);
        for (&val, &cnt) in freq.iter() {
            if cnt > maxcnt {
                maxcnt = cnt;
                dom = val;
            }
        }

        // helper to compute minimal cost for a given set of bad indices
        fn cost_for_set(bad_set: &[usize], is_bad_mask: &[bool]) -> i64 {
            if bad_set.is_empty() {
                return 0;
            }
            let m = bad_set.len();
            let sum: i64 = bad_set.iter().map(|&x| x as i64).sum();
            let min_b = *bad_set.iter().min().unwrap() as i64;

            // internal method (cycle inside the set)
            let mut best = sum + ((m as i64) - 2) * min_b;

            // external helper: smallest index not in the current bad set
            if let Some(g) = is_bad_mask.iter().position(|&b| !b) {
                let external = sum + min_b + ((m as i64) + 1) * (g as i64);
                if external < best {
                    best = external;
                }
            }
            best
        }

        // mask for current bad positions
        let mut is_bad_mask = vec![false; n];
        for &i in &bad {
            is_bad_mask[i] = true;
        }

        if maxcnt <= bad.len() / 2 {
            // derangement possible within the bad set alone
            return cost_for_set(&bad, &is_bad_mask);
        }

        // need to swap some dominant-value positions with good positions
        let excess = 2 * maxcnt - bad.len(); // number of swaps needed with good indices

        // candidate good indices that can be used (value and forbidden both differ from dom)
        let mut candidates: Vec<usize> = Vec::new();
        for i in 0..n {
            if nums1[i] != nums2[i] && nums1[i] != dom && nums2[i] != dom {
                candidates.push(i);
            }
        }
        if candidates.len() < excess {
            return -1;
        }

        // select smallest 'excess' candidate good indices
        let selected_good: Vec<usize> = candidates.iter().cloned().take(excess).collect();

        // bad indices that contain the dominant value
        let mut bad_dom: Vec<usize> = Vec::new();
        for &i in &bad {
            if nums1[i] == dom {
                bad_dom.push(i);
            }
        }
        // select smallest 'excess' of them
        let selected_bad: Vec<usize> = bad_dom.iter().cloned().take(excess).collect();

        // cost contributed by these direct swaps
        let mut extra_cost: i64 = 0;
        for &i in &selected_good {
            extra_cost += i as i64;
        }
        for &i in &selected_bad {
            extra_cost += i as i64;
        }

        // update masks: remove selected bad indices from the bad set
        for &i in &selected_bad {
            is_bad_mask[i] = false;
        }

        // build remaining bad list
        let mut remaining_bad: Vec<usize> = Vec::new();
        for i in 0..n {
            if is_bad_mask[i] {
                remaining_bad.push(i);
            }
        }

        // compute minimal cost for the remaining bad positions (now feasible)
        let rem_cost = cost_for_set(&remaining_bad, &is_bad_mask);
        extra_cost + rem_cost
    }
}
```

## Racket

```racket
(define/contract (minimum-total-cost nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([n (length nums1)]
         [v1 (list->vector nums1)]
         [v2 (list->vector nums2)]
         ;; frequency vectors (size n+1, indices 0..n)
         [cnt1 (make-vector (+ n 1) 0)]
         [cnt2 (make-vector (+ n 1) 0)]
         ;; containers for bad/good info
         [bad-idxs '()]
         [good-idxs '()] ; list of (index a b)
         [sum-bad 0]
         [vbad-set (make-hash)])
    ;; first pass: count frequencies and classify indices
    (for ([i (in-range n)])
      (let* ([a (vector-ref v1 i)]
             [b (vector-ref v2 i)])
        (vector-set! cnt1 a (+ 1 (vector-ref cnt1 a)))
        (vector-set! cnt2 b (+ 1 (vector-ref cnt2 b)))
        (if (= a b)
            (begin
              (set! sum-bad (+ sum-bad i))
              (set! bad-idxs (cons i bad-idxs))
              (hash-set! vbad-set a #t))
            (set! good-idxs (cons (list i a b) good-idxs)))))
    ;; feasibility check
    (let loop ([val 1] [possible? #t])
      (if (or (> val n) (not possible?))
          possible?
          (let* ([c1 (vector-ref cnt1 val)]
                 [c2 (vector-ref cnt2 val)]
                 [max-allowed (- n c2)])
            (loop (+ val 1) (and possible? (<= c1 max-allowed))))))
    (if (not (let loop ([val 1]) (or (> val n) (and (<= (vector-ref cnt1 val) (- n (vector-ref cnt2 val))) (loop (+ val 1))))) )
        -1
        (let* ([m (length bad-idxs)]
               [ans-even sum-bad])
          (if (even? m)
              ans-even
              ;; odd case: need extra good index
              (let* ([vbad-values (hash-keys vbad-set)]
                     [sizeV (length vbad-values)])
                (cond
                  [(= (length good-idxs) 0) -1] ; no good positions to help
                  [(> sizeV 2)
                   ;; any good index works; pick smallest index
                   (let ([minj (apply min (map (lambda (lst) (first lst)) good-idxs))])
                     (+ sum-bad minj))]
                  [(= sizeV 1)
                   (define v (first vbad-values))
                   (let loop ((rest good-idxs) (best #f))
                     (if (null? rest)
                         (if best (+ sum-bad best) -1)
                         (let* ([i (first (first rest))]
                                [a (second (first rest))]
                                [b (third (first rest))])
                           (if (and (not (= a v)) (not (= b v)))
                               (loop (cdr rest) (if best (min best i) i))
                               (loop (cdr rest) best))))))]
                  [(= sizeV 2)
                   (define a1 (first vbad-values))
                   (define a2 (second vbad-values))
                   (let loop ((rest good-idxs) (best #f))
                     (if (null? rest)
                         (if best (+ sum-bad best) -1)
                         (let* ([i (first (first rest))]
                                [a (second (first rest))]
                                [b (third (first rest))])
                           (if (or (and (= a a1) (= b a2))
                                   (and (= a a2) (= b a1)))
                               (loop (cdr rest) best)
                               (loop (cdr rest) (if best (min best i) i))))))]
                  [else -1])))))))
```

## Erlang

```erlang
-spec minimum_total_cost(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
minimum_total_cost(Nums1, Nums2) ->
    Len = length(Nums1),
    {SumBad, BadCount, BadFreqMap, Cnt1Map, Cnt2Map, GoodList} =
        loop(Nums1, Nums2, 0, 0, 0, #{}, #{}, []),

    %% feasibility check
    Feasible = maps:fold(
        fun(Key, C1, Acc) ->
            C2 = maps:get(Key, Cnt2Map, 0),
            if C1 =< Len - C2 -> Acc; true -> false end
        end,
        true,
        Cnt1Map),

    if not Feasible -> -1;
       BadCount =:= 0 -> 0;
       true ->
            {MaxFreq, Vmax} = max_freq(BadFreqMap),
            if MaxFreq =< BadCount div 2 ->
                    SumBad;
               true ->
                    Leftovers = 2 * MaxFreq - BadCount,
                    case extra_sum(GoodList, Vmax, Leftovers) of
                        {ok, Extra} -> SumBad + Extra;
                        not_enough -> -1
                    end
            end
    end.

%% ------------------------------------------------------------------
loop([], [], _Idx, SumBad, BadCount, BadFreqMap, Cnt1Map, Cnt2Map, GoodAcc) ->
    {SumBad, BadCount, BadFreqMap, Cnt1Map, Cnt2Map,
     lists:reverse(GoodAcc)};
loop([A|RestA], [B|RestB], Idx, SumBad, BadCount, BadFreqMap, Cnt1Map, Cnt2Map, GoodAcc) ->
    Cnt1Map1 = inc_map(Cnt1Map, A),
    Cnt2Map1 = inc_map(Cnt2Map, B),
    if A == B ->
            SumBad1 = SumBad + Idx,
            BadCount1 = BadCount + 1,
            BadFreqMap1 = inc_map(BadFreqMap, B),
            loop(RestA, RestB, Idx+1, SumBad1, BadCount1,
                 BadFreqMap1, Cnt1Map1, Cnt2Map1, GoodAcc);
       true ->
            NewGood = [{Idx, A, B} | GoodAcc],
            loop(RestA, RestB, Idx+1, SumBad, BadCount,
                 BadFreqMap, Cnt1Map1, Cnt2Map1, NewGood)
    end.

inc_map(Map, Key) ->
    case maps:is_key(Key, Map) of
        true -> maps:update(Key, maps:get(Key, Map) + 1, Map);
        false -> maps:put(Key, 1, Map)
    end.

max_freq(BadFreqMap) ->
    maps:fold(
        fun(_Key, Count, {CurMax, CurVal}) ->
            if Count > CurMax -> {Count, _Key};
               true -> {CurMax, CurVal}
            end
        end,
        {0, undefined},
        BadFreqMap).

extra_sum(GoodList, Vmax, Needed) ->
    extra_sum(GoodList, Vmax, Needed, 0).

extra_sum(_, _, 0, Acc) ->
    {ok, Acc};
extra_sum([], _Vmax, _Needed, _Acc) ->
    not_enough;
extra_sum([{Idx, A, B} | Rest], Vmax, Needed, Acc) ->
    if A =/= Vmax andalso B =/= Vmax ->
            extra_sum(Rest, Vmax, Needed - 1, Acc + Idx);
       true ->
            extra_sum(Rest, Vmax, Needed, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_total_cost(nums1 :: [integer], nums2 :: [integer]) :: integer
  def minimum_total_cost(nums1, nums2) do
    n = length(nums1)

    # Count occurrences in both arrays
    {cnt1, cnt2} =
      Enum.reduce(Enum.with_index(Enum.zip(nums1, nums2)), {%{}, %{}}, fn {{v1, v2}, _i},
                                                                        {c1, c2} ->
        c1 = Map.update(c1, v1, 1, &(&1 + 1))
        c2 = Map.update(c2, v2, 1, &(&1 + 1))
        {c1, c2}
      end)

    # Feasibility check
    feasible =
      Enum.all?(Map.keys(cnt1), fn v ->
        a = Map.get(cnt1, v, 0)
        b = Map.get(cnt2, v, 0)
        a <= n - b
      end)

    if not feasible do
      -1
    else
      # Gather same positions and diff indices
      {same_sum, cnt_same, diff_indices} =
        Enum.reduce(Enum.with_index(Enum.zip(nums1, nums2)), {0, %{}, []},
          fn {{v1, v2}, i}, {s_sum, c_same, diffs} ->
            if v1 == v2 do
              {s_sum + i,
               Map.update(c_same, v1, 1, &(&1 + 1)),
               diffs}
            else
              {s_sum, c_same, [i | diffs]}
            end
          end)

      diff_indices = Enum.reverse(diff_indices) # maintain ascending order

      pending_set = MapSet.new(Map.keys(cnt_same))
      cnt_same = cnt_same
      sum_diff = 0

      {cnt_same, pending_set, sum_diff} =
        Enum.reduce_while(diff_indices, {cnt_same, pending_set, sum_diff},
          fn j, {c_same, p_set, acc} ->
            if MapSet.size(p_set) == 0 do
              {:halt, {c_same, p_set, acc}}
            else
              a = Enum.at(nums1, j)
              b = Enum.at(nums2, j)

              candidate =
                cond do
                  MapSet.size(p_set) == 1 ->
                    [v] = MapSet.to_list(p_set)
                    if v != a and v != b, do: v, else: nil

                  true ->
                    Enum.find(p_set, fn v -> v != a and v != b end)
                end

              if candidate == nil do
                {:cont, {c_same, p_set, acc}}
              else
                new_acc = acc + j
                cnt = Map.get(c_same, candidate) - 1

                {new_c_same, new_p_set} =
                  if cnt == 0 do
                    {Map.delete(c_same, candidate), MapSet.delete(p_set, candidate)}
                  else
                    {Map.put(c_same, candidate, cnt), p_set}
                  end

                {:cont, {new_c_same, new_p_set, new_acc}}
              end
            end
          end)

      if MapSet.size(pending_set) == 0 do
        same_sum + sum_diff
      else
        -1
      end
    end
  end
end
```

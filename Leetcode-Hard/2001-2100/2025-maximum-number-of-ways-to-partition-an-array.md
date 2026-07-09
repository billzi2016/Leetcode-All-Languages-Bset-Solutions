# 2025. Maximum Number of Ways to Partition an Array

## Cpp

```cpp
class Solution {
public:
    int waysToPartition(vector<int>& nums, int k) {
        int n = nums.size();
        using ll = long long;
        vector<ll> pref(n);
        pref[0] = nums[0];
        for (int i = 1; i < n; ++i) pref[i] = pref[i-1] + nums[i];
        ll total = pref.back();

        vector<ll> diff;
        diff.reserve(n-1);
        int original = 0;
        for (int p = 1; p < n; ++p) {
            ll d = total - 2 * pref[p-1];
            diff.push_back(d);
            if (d == 0) ++original;
        }

        unordered_map<ll,int> suffix, prefix;
        suffix.reserve(diff.size()*2+1);
        for (ll d : diff) ++suffix[d];

        int maxGain = 0;
        for (int i = 0; i < n; ++i) {
            ll needLeft = (ll)nums[i] - k;   // diff needed when pivot <= i
            ll needRight = (ll)k - nums[i];  // diff needed when pivot > i

            int cntLeft = 0, cntRight = 0;
            auto itL = prefix.find(needLeft);
            if (itL != prefix.end()) cntLeft = itL->second;
            auto itR = suffix.find(needRight);
            if (itR != suffix.end()) cntRight = itR->second;

            maxGain = max(maxGain, cntLeft + cntRight);

            if (i < n-1) {
                ll d = diff[i];
                // move d from suffix to prefix
                auto its = suffix.find(d);
                if (its != suffix.end()) {
                    if (--its->second == 0) suffix.erase(its);
                }
                ++prefix[d];
            }
        }

        return max(original, maxGain);
    }
};
```

## Java

```java
class Solution {
    public int waysToPartition(int[] nums, int k) {
        int n = nums.length;
        long[] pref = new long[n];
        pref[0] = nums[0];
        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + nums[i];
        }
        long total = pref[n - 1];

        long[] needL = new long[n]; // index is pivot position
        long[] needR = new long[n];
        int baseWays = 0;
        for (int p = 1; p < n; p++) {
            long leftSum = pref[p - 1];
            if (2 * leftSum == total) {
                baseWays++;
            }
            needL[p] = total - 2 * leftSum;
            needR[p] = 2 * leftSum - total;
        }

        int[] leftCnt = new int[n];
        java.util.HashMap<Long, Integer> map = new java.util.HashMap<>();
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1) { // pivot p = i+1 becomes > i
                long val = needL[i + 1];
                map.put(val, map.getOrDefault(val, 0) + 1);
            }
            long delta = (long) k - nums[i];
            leftCnt[i] = map.getOrDefault(delta, 0);
        }

        int[] rightCnt = new int[n];
        map.clear();
        for (int i = 0; i < n; i++) {
            if (i >= 1) { // pivot p = i is <= i
                long val = needR[i];
                map.put(val, map.getOrDefault(val, 0) + 1);
            }
            long delta = (long) k - nums[i];
            rightCnt[i] = map.getOrDefault(delta, 0);
        }

        int maxWays = baseWays;
        for (int i = 0; i < n; i++) {
            int totalWays = leftCnt[i] + rightCnt[i];
            if (totalWays > maxWays) {
                maxWays = totalWays;
            }
        }
        return maxWays;
    }
}
```

## Python

```python
class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        n = len(nums)
        total = sum(nums)

        # compute diff for each possible pivot (p = 1 .. n-1)
        diffs = []
        pref = 0
        right_counts = defaultdict(int)
        for p in range(1, n):
            pref += nums[p - 1]
            d = total - 2 * pref
            diffs.append(d)
            right_counts[d] += 1

        # original number of good pivots (no change)
        ans = right_counts.get(0, 0)

        left_counts = defaultdict(int)

        for i in range(n):
            delta = k - nums[i]
            candidate = left_counts.get(-delta, 0) + right_counts.get(delta, 0)
            if candidate > ans:
                ans = candidate

            # move pivot p = i+1 from right side to left side
            if i < n - 1:
                d = diffs[i]  # diff corresponding to pivot after index i
                cnt = right_counts[d]
                if cnt == 1:
                    del right_counts[d]
                else:
                    right_counts[d] = cnt - 1
                left_counts[d] += 1

        return ans
```

## Python3

```python
import collections
from typing import List

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = sum(nums)

        left_needed = [0] * n   # index by pivot position p (1..n-1)
        right_needed = [0] * n

        cnt_left = collections.Counter()
        pref = 0
        original = 0

        for p in range(1, n):
            pref += nums[p - 1]
            if pref * 2 == total:
                original += 1
            d_left = total - 2 * pref
            left_needed[p] = d_left
            right_needed[p] = -d_left
            cnt_left[d_left] += 1

        cnt_right = collections.Counter()
        best = 0

        for i in range(n):
            delta = k - nums[i]
            cur = cnt_left.get(delta, 0) + cnt_right.get(delta, 0)
            if cur > best:
                best = cur

            p = i + 1
            if p < n:
                d_left = left_needed[p]
                d_right = right_needed[p]

                cnt_left[d_left] -= 1
                if cnt_left[d_left] == 0:
                    del cnt_left[d_left]

                cnt_right[d_right] += 1

        return max(original, best)
```

## C

```c
#include <stddef.h>
#include <stdint.h>

typedef struct {
    long long key;
    int cnt;
    char used;
} Entry;

static inline uint64_t hash_key(long long x) {
    uint64_t h = (uint64_t)x;
    h ^= h >> 33;
    h *= 0xff51afd7ed558ccdULL;
    h ^= h >> 33;
    h *= 0xc4ceb9fe1a85ec53ULL;
    h ^= h >> 33;
    return h;
}

static void ht_init(Entry *tbl, int size) {
    for (int i = 0; i < size; ++i) tbl[i].used = 0;
}

static int *ht_find_slot(Entry *tbl, int size, long long key) {
    uint64_t idx = hash_key(key) & (size - 1);
    while (tbl[idx].used && tbl[idx].key != key) {
        idx = (idx + 1) & (size - 1);
    }
    return &tbl[idx].cnt;
}

static int ht_get(Entry *tbl, int size, long long key) {
    uint64_t idx = hash_key(key) & (size - 1);
    while (tbl[idx].used) {
        if (tbl[idx].key == key) return tbl[idx].cnt;
        idx = (idx + 1) & (size - 1);
    }
    return 0;
}

static void ht_add(Entry *tbl, int size, long long key, int delta) {
    uint64_t idx = hash_key(key) & (size - 1);
    while (tbl[idx].used && tbl[idx].key != key) {
        idx = (idx + 1) & (size - 1);
    }
    if (!tbl[idx].used) {
        tbl[idx].used = 1;
        tbl[idx].key = key;
        tbl[idx].cnt = delta;
    } else {
        tbl[idx].cnt += delta;
    }
}

/* LeetCode entry point */
int waysToPartition(int* nums, int numsSize, int k) {
    if (numsSize < 2) return 0;

    const int CAP = 1 << 20;               // > 4 * 10^5, power of two
    static Entry leftTbl[CAP];
    static Entry rightTbl[CAP];

    ht_init(leftTbl, CAP);
    ht_init(rightTbl, CAP);

    long long total = 0;
    for (int i = 0; i < numsSize; ++i) total += nums[i];

    // prefix sums up to index i (inclusive)
    long long *pref = (long long *)malloc(sizeof(long long) * (numsSize - 1));
    long long cur = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        cur += nums[i];
        pref[i] = cur;
        ht_add(rightTbl, CAP, pref[i], 1);
    }

    int baseWays = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        if (2 * pref[i] == total) ++baseWays;
    }
    int answer = baseWays;

    for (int i = 0; i < numsSize; ++i) {
        long long diff = (long long)k - (long long)nums[i];
        long long targetL = total + diff;
        long long targetR = total - diff;

        int cntL = 0, cntR = 0;
        if ((targetL & 1LL) == 0) {
            cntL = ht_get(leftTbl, CAP, targetL / 2);
        }
        if ((targetR & 1LL) == 0) {
            cntR = ht_get(rightTbl, CAP, targetR / 2);
        }

        int ways = cntL + cntR;
        if (ways > answer) answer = ways;

        // move pivot pref[i] from right to left for next iteration
        if (i <= numsSize - 2) {
            long long val = pref[i];
            ht_add(rightTbl, CAP, val, -1);
            ht_add(leftTbl, CAP, val, 1);
        }
    }

    free(pref);
    return answer;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int WaysToPartition(int[] nums, int k) {
        int n = nums.Length;
        long total = 0;
        foreach (int v in nums) total += v;

        // diffs for each pivot position (split after index p)
        long[] diffs = new long[n - 1];
        var leftMap = new Dictionary<long, int>();
        var rightMap = new Dictionary<long, int>();

        long prefix = 0;
        int baseWays = 0;
        for (int p = 0; p < n - 1; ++p) {
            prefix += nums[p];
            long diff = total - 2 * prefix; // needed delta if changed element is on the left side
            diffs[p] = diff;
            if (diff == 0) baseWays++;

            long rightKey = -diff; // needed delta if changed element is on the right side
            if (rightMap.ContainsKey(rightKey))
                rightMap[rightKey]++;
            else
                rightMap[rightKey] = 1;
        }

        int maxAns = baseWays;

        for (int i = 0; i < n; ++i) {
            long delta = (long)k - nums[i];
            int ways = 0;
            if (leftMap.TryGetValue(delta, out int cntL)) ways += cntL;
            if (rightMap.TryGetValue(delta, out int cntR)) ways += cntR;

            if (ways > maxAns) maxAns = ways;

            // move pivot p=i from right side to left side for future indices
            if (i <= n - 2) {
                long diff = diffs[i];
                long rightKey = -diff;
                // remove from rightMap
                if (rightMap.TryGetValue(rightKey, out int rc)) {
                    if (rc == 1) rightMap.Remove(rightKey);
                    else rightMap[rightKey] = rc - 1;
                }
                // add to leftMap
                if (leftMap.ContainsKey(diff))
                    leftMap[diff]++;
                else
                    leftMap[diff] = 1;
            }
        }

        return maxAns;
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
var waysToPartition = function(nums, k) {
    const n = nums.length;
    let total = 0;
    for (let v of nums) total += v;

    // map of prefix sums for all possible split points (left side ends at idx i)
    const rightMap = new Map();
    let pref = 0;
    for (let i = 0; i < n - 1; ++i) {
        pref += nums[i];
        rightMap.set(pref, (rightMap.get(pref) || 0) + 1);
    }

    // original answer without any change
    let ans = 0;
    if (total % 2 === 0) {
        const target = total / 2;
        ans = rightMap.get(target) || 0;
    }

    const leftMap = new Map();
    pref = 0; // will be prefix sum up to current index i

    for (let i = 0; i < n; ++i) {
        const delta = k - nums[i];

        if (delta !== 0) {
            // pivots before i: left side includes changed element
            const needBeforeSum = total - delta;
            if (needBeforeSum % 2 === 0) {
                const target = needBeforeSum / 2;
                const cnt = leftMap.get(target) || 0;
                if (cnt > ans) ans = cnt;
            }
            // pivots after i: left side unchanged
            const needAfterSum = total + delta;
            if (needAfterSum % 2 === 0) {
                const target = needAfterSum / 2;
                const cnt = rightMap.get(target) || 0;
                if (cnt > ans) ans = cnt;
            }
        }

        // move split point that ends at i from rightMap to leftMap
        if (i < n - 1) {
            pref += nums[i];
            // remove from rightMap
            const curCnt = rightMap.get(pref);
            if (curCnt === 1) rightMap.delete(pref);
            else rightMap.set(pref, curCnt - 1);
            // add to leftMap
            leftMap.set(pref, (leftMap.get(pref) || 0) + 1);
        }
    }

    return ans;
};
```

## Typescript

```typescript
function waysToPartition(nums: number[], k: number): number {
    const n = nums.length;
    const pref: number[] = new Array(n);
    let total = 0;
    for (let i = 0; i < n; i++) {
        total += nums[i];
        pref[i] = total;
    }

    const leftMap = new Map<number, number>();
    const rightMap = new Map<number, number>();

    // Initialize rightMap with all possible pivot prefix sums (indices 0 .. n-2)
    for (let i = 0; i < n - 1; i++) {
        const v = pref[i];
        rightMap.set(v, (rightMap.get(v) ?? 0) + 1);
    }

    let answer = 0;
    if (total % 2 === 0) {
        answer = rightMap.get(total / 2) ?? 0; // baseline without any change
    }

    for (let i = 0; i < n; i++) {
        // Move pivot at index i-1 from right side to left side
        if (i > 0) {
            const v = pref[i - 1];
            const cntR = rightMap.get(v)!;
            if (cntR === 1) rightMap.delete(v);
            else rightMap.set(v, cntR - 1);
            leftMap.set(v, (leftMap.get(v) ?? 0) + 1);
        }

        const delta = k - nums[i];
        // Count pivots where condition holds after changing nums[i] to k
        let cur = 0;

        // Pivots with left side not containing index i (j < i)
        if ((total + delta) % 2 === 0) {
            const targetLeft = (total + delta) / 2;
            cur += leftMap.get(targetLeft) ?? 0;
        }

        // Pivots with left side containing index i (j >= i)
        if ((total - delta) % 2 === 0) {
            const targetRight = (total - delta) / 2;
            cur += rightMap.get(targetRight) ?? 0;
        }

        if (cur > answer) answer = cur;
    }

    return answer;
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
    function waysToPartition($nums, $k) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $v) {
            $total += $v;
        }

        // prefix sums
        $pref = [];
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum += $nums[$i];
            $pref[$i] = $sum;
        }

        // right map contains counts of 2*prefix for pivots where p-1 >= current index
        $right = [];
        for ($j = 0; $j < $n - 1; $j++) {
            $key = 2 * $pref[$j];
            if (!isset($right[$key])) $right[$key] = 0;
            $right[$key]++;
        }

        $left = [];

        // base answer without any change
        $maxWays = $right[$total] ?? 0;

        for ($i = 0; $i < $n; $i++) {
            $delta = $k - $nums[$i];
            $targetRight = $total + $delta;   // condition when changed element is in right part
            $targetLeft  = $total - $delta;   // condition when changed element is in left part

            $cntRight = $left[$targetRight] ?? 0;
            $cntLeft  = $right[$targetLeft] ?? 0;

            $curr = $cntRight + $cntLeft;
            if ($curr > $maxWays) {
                $maxWays = $curr;
            }

            // move pivot index i from right map to left map for next iteration
            if ($i < $n - 1) {
                $key = 2 * $pref[$i];
                $right[$key]--;
                if ($right[$key] == 0) {
                    unset($right[$key]);
                }
                if (!isset($left[$key])) $left[$key] = 0;
                $left[$key]++;
            }
        }

        return $maxWays;
    }
}
```

## Swift

```swift
class Solution {
    func waysToPartition(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + nums[i]
        }
        let total = prefix[n]
        
        // frequency of left sums for pivots (positions) 1..n-1
        var rightCount = [Int: Int]()
        var baseAns = 0
        if n > 1 {
            for p in 1..<(n) {
                let val = prefix[p]
                rightCount[val, default: 0] += 1
                if val * 2 == total {
                    baseAns += 1
                }
            }
        }
        
        var leftCount = [Int: Int]()
        var answer = baseAns
        
        for j in 0..<n {
            let delta = k - nums[j]
            
            var cur = 0
            // pivots where split position <= j (left side does NOT include changed element)
            if ((total + delta) & 1) == 0 {
                let need = (total + delta) / 2
                cur += leftCount[need] ?? 0
            }
            // pivots where split position > j (left side includes changed element)
            if ((total - delta) & 1) == 0 {
                let need = (total - delta) / 2
                cur += rightCount[need] ?? 0
            }
            answer = max(answer, cur)
            
            // move pivot at position j+1 from right to left for next iteration
            let splitPos = j + 1
            if splitPos <= n - 1 {
                let val = prefix[splitPos]
                if let cnt = rightCount[val] {
                    if cnt == 1 {
                        rightCount.removeValue(forKey: val)
                    } else {
                        rightCount[val] = cnt - 1
                    }
                }
                leftCount[val, default: 0] += 1
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap

class Solution {
    fun waysToPartition(nums: IntArray, k: Int): Int {
        val n = nums.size
        var totalSum = 0L
        for (v in nums) totalSum += v.toLong()

        // need arrays for pivots 1..n-1
        val needL = LongArray(n)
        val needR = LongArray(n)

        var original = 0
        val totalNeedL = HashMap<Long, Int>()
        val totalNeedR = HashMap<Long, Int>()

        var prefix = 0L
        for (p in 1 until n) {
            prefix += nums[p - 1].toLong()
            val nl = totalSum - 2 * prefix   // delta needed if changed element is on the left side
            val nr = 2 * prefix - totalSum   // delta needed if changed element is on the right side
            needL[p] = nl
            needR[p] = nr
            if (nl == 0L) {
                original++
            } else {
                totalNeedL[nl] = (totalNeedL[nl] ?: 0) + 1
            }
            if (nr != 0L) { // when nl==0, nr also 0; skip to avoid double counting originals
                totalNeedR[nr] = (totalNeedR[nr] ?: 0) + 1
            }
        }

        val prefNeedL = HashMap<Long, Int>()
        val prefNeedR = HashMap<Long, Int>()
        var bestAdd = 0

        for (i in 0 until n) {
            val delta = (k - nums[i]).toLong()
            var cnt = 0
            // pivots where i is on the right side (p <= i)
            cnt += prefNeedR[delta] ?: 0
            // pivots where i is on the left side (p > i)
            val totalL = totalNeedL[delta] ?: 0
            val seenL = prefNeedL[delta] ?: 0
            cnt += totalL - seenL

            if (cnt > bestAdd) bestAdd = cnt

            // add pivot p = i+1 to prefix maps for next iterations
            val p = i + 1
            if (p < n) {
                val nl = needL[p]
                if (nl != 0L) {
                    prefNeedL[nl] = (prefNeedL[nl] ?: 0) + 1
                }
                val nr = needR[p]
                if (nr != 0L) {
                    prefNeedR[nr] = (prefNeedR[nr] ?: 0) + 1
                }
            }
        }

        return original + bestAdd
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int waysToPartition(List<int> nums, int k) {
    int n = nums.length;
    int total = 0;
    for (int v in nums) total += v;

    // suffix map stores counts of a = total - 2*L for pivots p > current index
    Map<int, int> suffix = {};
    int baseAns = 0;
    int prefixSum = 0;
    for (int i = 0; i < n - 1; i++) {
      prefixSum += nums[i];
      int a = total - 2 * prefixSum;
      suffix[a] = (suffix[a] ?? 0) + 1;
      if (a == 0) baseAns++;
    }

    Map<int, int> prefix = {};
    int ans = baseAns;
    int leftSum = 0;

    for (int i = 0; i < n; i++) {
      int delta = k - nums[i];
      int cntRight = suffix[delta] ?? 0; // pivots where i < p
      int cntLeft = prefix[delta] ?? 0;   // pivots where i >= p
      ans = max(ans, cntRight + cntLeft);

      leftSum += nums[i];
      if (i + 1 < n) {
        int L = leftSum;
        int a = total - 2 * L;
        int b = -a; // 2*L - total

        // move pivot p = i+1 from suffix to prefix
        int curCnt = suffix[a] ?? 0;
        if (curCnt <= 1) {
          suffix.remove(a);
        } else {
          suffix[a] = curCnt - 1;
        }
        prefix[b] = (prefix[b] ?? 0) + 1;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func waysToPartition(nums []int, k int) int {
    n := len(nums)
    pref := make([]int64, n)
    var sum int64
    for i, v := range nums {
        sum += int64(v)
        pref[i] = sum
    }

    base := 0
    needLeft := make([]int64, n)  // indexed by pivot position (1..n-1)
    needRight := make([]int64, n)

    leftMap := make(map[int64]int)
    rightMap := make(map[int64]int)

    for p := 1; p < n; p++ {
        L := pref[p-1]
        if 2*L == sum {
            base++
        }
        nl := sum - 2*L          // delta needed when changing an element on the left side
        nr := -nl                // delta needed when changing an element on the right side
        needLeft[p] = nl
        needRight[p] = nr
        leftMap[nl]++
    }

    ans := base

    for i, v := range nums {
        delta := int64(k - v)
        total := base + leftMap[delta] + rightMap[delta]
        if total > ans {
            ans = total
        }
        p := i + 1
        if p < n {
            nl := needLeft[p]
            cnt := leftMap[nl]
            if cnt == 1 {
                delete(leftMap, nl)
            } else {
                leftMap[nl] = cnt - 1
            }
            nr := needRight[p]
            rightMap[nr]++
        }
    }

    return ans
}
```

## Ruby

```ruby
def ways_to_partition(nums, k)
  n = nums.length
  pref = Array.new(n)
  sum = 0
  nums.each_with_index do |v, i|
    sum += v
    pref[i] = sum
  end
  total = sum

  left_map = Hash.new(0)
  right_map = Hash.new(0)

  need_left_arr = Array.new(n, 0)
  need_right_arr = Array.new(n, 0)

  original = 0
  (1...n).each do |p|
    l = pref[p - 1]
    need_left = total - 2 * l
    need_right = 2 * l - total
    left_map[need_left] += 1
    need_left_arr[p] = need_left
    need_right_arr[p] = need_right
    original += 1 if need_left == 0
  end

  ans = original

  (0...n).each do |i|
    delta = k - nums[i]
    cur = left_map[delta] + right_map[delta]
    ans = cur if cur > ans

    p = i + 1
    if p < n
      nl = need_left_arr[p]
      nr = need_right_arr[p]

      cnt = left_map[nl]
      if cnt == 1
        left_map.delete(nl)
      else
        left_map[nl] = cnt - 1
      end

      right_map[nr] += 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def waysToPartition(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        val pref = new Array[Long](n + 1)
        for (i <- 0 until n) {
            pref(i + 1) = pref(i) + nums(i).toLong
        }
        val total = pref(n)

        var base = 0
        for (p <- 1 until n) {
            if (pref(p) * 2 == total) base += 1
        }

        import scala.collection.mutable.{HashMap => MutableMap}
        val right = MutableMap[Long, Int]()
        for (p <- 1 until n) {
            val v = pref(p)
            right(v) = right.getOrElse(v, 0) + 1
        }
        val left = MutableMap[Long, Int]()

        var ans = base

        for (i <- 0 until n) {
            val delta = k.toLong - nums(i).toLong
            var cnt = 0

            val sumPlus = total + delta
            if (sumPlus % 2 == 0) {
                val target = sumPlus / 2
                cnt += left.getOrElse(target, 0)
            }

            val sumMinus = total - delta
            if (sumMinus % 2 == 0) {
                val target = sumMinus / 2
                cnt += right.getOrElse(target, 0)
            }

            if (cnt > ans) ans = cnt

            // move pivot p = i + 1 from right to left for next iteration
            if (i + 1 < n) {
                val v = pref(i + 1)
                val cur = right(v)
                if (cur == 1) right -= v else right(v) = cur - 1
                left(v) = left.getOrElse(v, 0) + 1
            }
        }

        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn ways_to_partition(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        // total sum as i64
        let mut total: i64 = 0;
        for &v in &nums {
            total += v as i64;
        }

        // diffs for each pivot (split after index i)
        let mut diffs: Vec<i64> = Vec::with_capacity(n - 1);
        let mut prefix: i64 = 0;
        for i in 0..n - 1 {
            prefix += nums[i] as i64;
            diffs.push(2 * prefix - total);
        }

        // count base ways (diff == 0)
        let base_ways = diffs.iter().filter(|&&d| d == 0).count() as i32;

        // maps for left and right side diffs
        let mut left: HashMap<i64, i32> = HashMap::new();
        let mut right: HashMap<i64, i32> = HashMap::new();
        for &d in &diffs {
            *right.entry(d).or_insert(0) += 1;
        }

        let mut best: i32 = 0;

        for i in 0..n {
            if i > 0 {
                // move pivot i-1 from right to left
                let d = diffs[i - 1];
                if let Some(cnt) = right.get_mut(&d) {
                    *cnt -= 1;
                    if *cnt == 0 {
                        right.remove(&d);
                    }
                }
                *left.entry(d).or_insert(0) += 1;
            }

            let delta = (k - nums[i]) as i64;
            let cnt_left = left.get(&delta).cloned().unwrap_or(0);
            let cnt_right = right.get(&(-delta)).cloned().unwrap_or(0);
            let cur = cnt_left + cnt_right;
            if cur > best {
                best = cur;
            }
        }

        std::cmp::max(base_ways, best)
    }
}
```

## Racket

```racket
(define/contract (ways-to-partition nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  (define (inc-hash! ht key delta)
    (hash-set! ht key (+ (hash-ref ht key 0) delta)))

  (let* ((n (length nums))
         (pref (make-vector n))
         ;; build prefix sums
         (build-pref
          (let loop ((i 0) (sum 0))
            (when (< i n)
              (set! sum (+ sum (list-ref nums i)))
              (vector-set! pref i sum)
              (loop (+ i 1) sum))))
         (total (if (= n 0) 0 (vector-ref pref (- n 1)))))
    ;; maps for needed delta on left/right side of a pivot
    (define left (make-hash))
    (define right (make-hash))
    (define base 0)
    ;; initialize left map with need_left for all pivots i = 0 .. n-2
    (for ([i (in-range (- n 1))])
      (let* ((need (- total (* 2 (vector-ref pref i)))))
        (inc-hash! left need 1)
        (when (= need 0) (set! base (+ base 1)))))
    (define ans base)

    ;; sweep possible changed index
    (for ([idx (in-range n)])
      (let ((delta (- k (list-ref nums idx))))
        (define ways (+ (hash-ref left delta 0)
                        (hash-ref right delta 0)))
        (when (> ways ans) (set! ans ways)))

      ;; move pivot i = idx from left side to right side for next iteration
      (when (< idx (- n 1))
        (let* ((need (- total (* 2 (vector-ref pref idx))))
               (cnt-left (hash-ref left need 0)))
          (if (= cnt-left 1)
              (hash-remove! left need)
              (hash-set! left need (- cnt-left 1)))
          ;; need_right is the opposite sign
          (inc-hash! right (- need) 1))))

    ans))
```

## Erlang

```erlang
-spec ways_to_partition(Nums :: [integer()], K :: integer()) -> integer().
ways_to_partition(Nums, K) ->
    {PrefList, Total} = prefix_sums(Nums),
    N = length(PrefList),
    RightMap0 = build_right_map(lists:sublist(PrefList, N - 1), #{}),
    BaseAns = count_base(lists:sublist(PrefList, N - 1), Total, 0),
    loop_change(lists:zip(Nums, PrefList), K, Total, RightMap0, #{}, BaseAns).

prefix_sums(L) ->
    {Total, RevPref} =
        lists:foldl(
            fun(X, {AccSum, AccRev}) ->
                NewSum = AccSum + X,
                {NewSum, [NewSum | AccRev]}
            end,
            {0, []},
            L),
    Pref = lists:reverse(RevPref),
    {Pref, Total}.

build_right_map([], Map) -> Map;
build_right_map([H|T], Map) ->
    NewMap = add_count(Map, H),
    build_right_map(T, NewMap).

count_base([], _Total, Acc) -> Acc;
count_base([H|T], Total, Acc) ->
    case 2 * H =:= Total of
        true -> count_base(T, Total, Acc + 1);
        false -> count_base(T, Total, Acc)
    end.

loop_change([], _K, _Total, _RightMap, _LeftMap, Max) -> Max;
loop_change([{Num, Pref}|Rest], K, Total, RightMap, LeftMap, Max) ->
    Delta = K - Num,
    Ways1 =
        case (Total + Delta) rem 2 of
            0 ->
                TargetL = (Total + Delta) div 2,
                maps:get(TargetL, LeftMap, 0);
            _ -> 0
        end,
    Ways2 =
        case (Total - Delta) rem 2 of
            0 ->
                TargetR = (Total - Delta) div 2,
                maps:get(TargetR, RightMap, 0);
            _ -> 0
        end,
    TotalWays = Ways1 + Ways2,
    NewMax = erlang:max(Max, TotalWays),
    {NewRightMap, NewLeftMap} =
        case maps:is_key(Pref, RightMap) of
            true ->
                UpdatedRight = remove_count(RightMap, Pref),
                UpdatedLeft = add_count(LeftMap, Pref),
                {UpdatedRight, UpdatedLeft};
            false -> {RightMap, LeftMap}
        end,
    loop_change(Rest, K, Total, NewRightMap, NewLeftMap, NewMax).

add_count(Map, Key) ->
    case maps:is_key(Key, Map) of
        true -> maps:update(Key, fun(V) -> V + 1 end, 1, Map);
        false -> maps:put(Key, 1, Map)
    end.

remove_count(Map, Key) ->
    case maps:get(Key, Map) of
        1 -> maps:remove(Key, Map);
        N when N > 1 -> maps:put(Key, N - 1, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec ways_to_partition(nums :: [integer], k :: integer) :: integer
  def ways_to_partition(nums, k) do
    n = length(nums)
    total = Enum.sum(nums)

    # Build needs map and count base partitions
    {needs_map, base, _} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({%{}, 0, 0}, fn {val, idx}, {map, base_acc, cur_sum} ->
        if idx < n - 1 do
          new_cur = cur_sum + val
          need_left = total - 2 * new_cur
          need_right = 2 * new_cur - total
          map = Map.put(map, idx, {need_left, need_right})
          base_acc = if 2 * new_cur == total, do: base_acc + 1, else: base_acc
          {map, base_acc, new_cur}
        else
          {map, base_acc, cur_sum}
        end
      end)

    # Frequency map of need_left for all pivots (initially all are on the left side)
    left_map =
      needs_map
      |> Enum.reduce(%{}, fn {_idx, {need_left, _need_right}}, acc ->
        Map.update(acc, need_left, 1, &(&1 + 1))
      end)

    right_map = %{}
    max_ways = base

    # Iterate over each index as the possible changed element
    {_, _, result} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({left_map, right_map, max_ways}, fn {val, idx},
                                                          {lmap, rmap, cur_max} ->
        delta = k - val

        extra =
          Map.get(lmap, delta, 0) + Map.get(rmap, delta, 0)

        total_ways = base + extra
        new_max = if total_ways > cur_max, do: total_ways, else: cur_max

        # Move pivot idx+1 from left side to right side for next iteration
        {new_lmap, new_rmap} =
          if idx < n - 1 do
            {need_left, need_right} = Map.get(needs_map, idx)

            lcnt = Map.get(lmap, need_left)
            updated_lmap =
              cond do
                lcnt == nil -> lmap
                lcnt == 1 -> Map.delete(lmap, need_left)
                true -> Map.put(lmap, need_left, lcnt - 1)
              end

            updated_rmap = Map.update(rmap, need_right, 1, &(&1 + 1))
            {updated_lmap, updated_rmap}
          else
            {lmap, rmap}
          end

        {new_lmap, new_rmap, new_max}
      end)

    result
  end
end
```

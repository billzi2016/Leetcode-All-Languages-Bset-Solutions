# 2035. Partition Array Into Two Arrays to Minimize Sum Difference

## Cpp

```cpp
class Solution {
public:
    int minimumDifference(vector<int>& nums) {
        int totalLen = nums.size();
        int n = totalLen / 2;
        long long totalSum = 0;
        for (int v : nums) totalSum += v;

        vector<int> left(nums.begin(), nums.begin() + n);
        vector<int> right(nums.begin() + n, nums.end());

        vector<vector<long long>> leftSums(n + 1), rightSums(n + 1);

        // enumerate subsets of left half
        int leftMaskLimit = 1 << n;
        for (int mask = 0; mask < leftMaskLimit; ++mask) {
            int cnt = __builtin_popcount(mask);
            long long sum = 0;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) sum += left[i];
            }
            leftSums[cnt].push_back(sum);
        }

        // enumerate subsets of right half
        int rightMaskLimit = 1 << n;
        for (int mask = 0; mask < rightMaskLimit; ++mask) {
            int cnt = __builtin_popcount(mask);
            long long sum = 0;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) sum += right[i];
            }
            rightSums[cnt].push_back(sum);
        }

        for (auto& vec : rightSums) {
            sort(vec.begin(), vec.end());
        }

        long long bestDiff = LLONG_MAX;
        // target is totalSum / 2, but we work with integers directly
        for (int k = 0; k <= n; ++k) {
            const vector<long long>& leftVec = leftSums[k];
            const vector<long long>& rightVec = rightSums[n - k];
            if (rightVec.empty()) continue;
            for (long long sumL : leftVec) {
                // we want total subset sum close to totalSum/2
                double needD = (double)totalSum / 2.0 - sumL;
                long long need = llround(needD); // approximate, binary search will handle exactness
                auto it = lower_bound(rightVec.begin(), rightVec.end(), need);
                if (it != rightVec.end()) {
                    long long totalSubset = sumL + *it;
                    long long diff = llabs(totalSum - 2 * totalSubset);
                    if (diff < bestDiff) bestDiff = diff;
                }
                if (it != rightVec.begin()) {
                    --it;
                    long long totalSubset = sumL + *it;
                    long long diff = llabs(totalSum - 2 * totalSubset);
                    if (diff < bestDiff) bestDiff = diff;
                }
            }
        }

        return (int)bestDiff;
    }
};
```

## Java

```java
class Solution {
    public int minimumDifference(int[] nums) {
        int n = nums.length / 2;
        long total = 0;
        for (int v : nums) total += v;

        int[] left = java.util.Arrays.copyOfRange(nums, 0, n);
        int[] right = java.util.Arrays.copyOfRange(nums, n, 2 * n);

        @SuppressWarnings("unchecked")
        java.util.List<Long>[] leftSums = new java.util.ArrayList[n + 1];
        @SuppressWarnings("unchecked")
        java.util.List<Long>[] rightSums = new java.util.ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            leftSums[i] = new java.util.ArrayList<>();
            rightSums[i] = new java.util.ArrayList<>();
        }

        int limit = 1 << n;
        for (int mask = 0; mask < limit; mask++) {
            long sum = 0;
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    sum += left[i];
                    cnt++;
                }
            }
            leftSums[cnt].add(sum);
        }

        for (int mask = 0; mask < limit; mask++) {
            long sum = 0;
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    sum += right[i];
                    cnt++;
                }
            }
            rightSums[cnt].add(sum);
        }

        for (int k = 0; k <= n; k++) {
            java.util.Collections.sort(rightSums[k]);
        }

        long best = Long.MAX_VALUE;
        long target = total / 2;

        for (int k = 0; k <= n; k++) {
            java.util.List<Long> leftList = leftSums[k];
            java.util.List<Long> rightList = rightSums[n - k];
            if (rightList.isEmpty()) continue;
            for (long sumL : leftList) {
                long need = target - sumL;
                int idx = java.util.Collections.binarySearch(rightList, need);
                if (idx >= 0) {
                    long totalA = sumL + rightList.get(idx);
                    long diff = Math.abs(total - 2 * totalA);
                    if (diff < best) best = diff;
                } else {
                    int insertPoint = -idx - 1;
                    if (insertPoint < rightList.size()) {
                        long sumR = rightList.get(insertPoint);
                        long totalA = sumL + sumR;
                        long diff = Math.abs(total - 2 * totalA);
                        if (diff < best) best = diff;
                    }
                    if (insertPoint > 0) {
                        long sumR = rightList.get(insertPoint - 1);
                        long totalA = sumL + sumR;
                        long diff = Math.abs(total - 2 * totalA);
                        if (diff < best) best = diff;
                    }
                }
            }
        }

        return (int) best;
    }
}
```

## Python

```python
import bisect

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        half = len(nums) // 2
        left = nums[:half]
        right = nums[half:]

        # sums_by_cnt[k] = list of subset sums using exactly k elements
        left_sums = [[] for _ in range(half + 1)]
        right_sums = [[] for _ in range(half + 1)]

        # enumerate subsets of left half
        for mask in range(1 << half):
            cnt = 0
            s = 0
            for i in range(half):
                if (mask >> i) & 1:
                    cnt += 1
                    s += left[i]
            left_sums[cnt].append(s)

        # enumerate subsets of right half
        for mask in range(1 << half):
            cnt = 0
            s = 0
            for i in range(half):
                if (mask >> i) & 1:
                    cnt += 1
                    s += right[i]
            right_sums[cnt].append(s)

        # sort each list of the right side for binary search
        for lst in right_sums:
            lst.sort()

        target = total / 2.0
        ans = abs(total)  # worst possible difference

        for k in range(half + 1):
            rlist = right_sums[half - k]
            if not rlist:
                continue
            for s_left in left_sums[k]:
                need = target - s_left
                idx = bisect.bisect_left(rlist, need)
                # candidate at idx
                if idx < len(rlist):
                    cur_sum = s_left + rlist[idx]
                    diff = abs(total - 2 * cur_sum)
                    if diff < ans:
                        ans = diff
                # candidate at idx-1
                if idx > 0:
                    cur_sum = s_left + rlist[idx - 1]
                    diff = abs(total - 2 * cur_sum)
                    if diff < ans:
                        ans = diff

        return int(ans)
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums) // 2
        left = nums[:n]
        right = nums[n:]

        # sums_by_cnt[i] = list of subset sums using exactly i elements from the half
        left_sums = [[] for _ in range(n + 1)]
        right_sums = [[] for _ in range(n + 1)]

        # enumerate subsets of left half
        for mask in range(1 << n):
            cnt = mask.bit_count()
            s = 0
            m = mask
            idx = 0
            while m:
                if m & 1:
                    s += left[idx]
                idx += 1
                m >>= 1
            left_sums[cnt].append(s)

        # enumerate subsets of right half
        for mask in range(1 << n):
            cnt = mask.bit_count()
            s = 0
            m = mask
            idx = 0
            while m:
                if m & 1:
                    s += right[idx]
                idx += 1
                m >>= 1
            right_sums[cnt].append(s)

        for lst in right_sums:
            lst.sort()

        best = abs(total)  # worst possible difference

        half_target = total / 2.0
        for k in range(n + 1):
            need = n - k
            r_list = right_sums[need]
            if not r_list:
                continue
            for l_sum in left_sums[k]:
                target = half_target - l_sum
                idx = bisect.bisect_left(r_list, target)
                # check candidate at idx
                if idx < len(r_list):
                    cur = l_sum + r_list[idx]
                    diff = abs(total - 2 * cur)
                    if diff < best:
                        best = diff
                        if best == 0:
                            return 0
                # check candidate at idx-1
                if idx > 0:
                    cur = l_sum + r_list[idx - 1]
                    diff = abs(total - 2 * cur)
                    if diff < best:
                        best = diff
                        if best == 0:
                            return 0

        return best
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long *data;
    int size;
    int capacity;
} Vec;

static void vecInit(Vec *v) {
    v->data = NULL;
    v->size = 0;
    v->capacity = 0;
}

static void vecPush(Vec *v, long long val) {
    if (v->size == v->capacity) {
        int newCap = v->capacity ? v->capacity * 2 : 4;
        v->data = (long long *)realloc(v->data, newCap * sizeof(long long));
        v->capacity = newCap;
    }
    v->data[v->size++] = val;
}

static int cmpLL(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

int minimumDifference(int* nums, int numsSize) {
    int n = numsSize / 2;                 // each part size
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) total += nums[i];

    Vec left[16], right[16];
    for (int k = 0; k <= n; ++k) {
        vecInit(&left[k]);
        vecInit(&right[k]);
    }

    // subsets of first half
    int maskLimit = 1 << n;
    for (int mask = 0; mask < maskLimit; ++mask) {
        long long sum = 0;
        int bits = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                sum += nums[i];
                ++bits;
            }
        }
        vecPush(&left[bits], sum);
    }

    // subsets of second half
    for (int mask = 0; mask < maskLimit; ++mask) {
        long long sum = 0;
        int bits = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                sum += nums[n + i];
                ++bits;
            }
        }
        vecPush(&right[bits], sum);
    }

    // sort right vectors for binary search
    for (int k = 0; k <= n; ++k) {
        if (right[k].size > 1)
            qsort(right[k].data, right[k].size, sizeof(long long), cmpLL);
    }

    long long best = LLONG_MAX;
    long long halfTotal = total / 2; // integer division

    for (int k = 0; k <= n; ++k) {
        int need = n - k;
        if (right[need].size == 0) continue;

        Vec *vL = &left[k];
        Vec *vR = &right[need];

        for (int i = 0; i < vL->size; ++i) {
            long long sL = vL->data[i];
            long long target = halfTotal - sL;

            // lower_bound in vR
            int lo = 0, hi = vR->size;
            while (lo < hi) {
                int mid = (lo + hi) >> 1;
                if (vR->data[mid] < target)
                    lo = mid + 1;
                else
                    hi = mid;
            }

            // check candidate at lo
            if (lo < vR->size) {
                long long sR = vR->data[lo];
                long long curSum = sL + sR;
                long long diff = llabs(total - 2 * curSum);
                if (diff < best) best = diff;
                if (best == 0) return 0;
            }
            // check candidate at lo-1
            if (lo > 0) {
                long long sR = vR->data[lo - 1];
                long long curSum = sL + sR;
                long long diff = llabs(total - 2 * curSum);
                if (diff < best) best = diff;
                if (best == 0) return 0;
            }
        }
    }

    return (int)best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public int MinimumDifference(int[] nums) {
        int total = 0;
        foreach (int v in nums) total += v;
        int len = nums.Length;
        int n = len / 2;

        int[] left = new int[n];
        int[] right = new int[n];
        Array.Copy(nums, 0, left, 0, n);
        Array.Copy(nums, n, right, 0, n);

        List<long>[] leftSums = new List<long>[n + 1];
        List<long>[] rightSums = new List<long>[n + 1];
        for (int i = 0; i <= n; i++) {
            leftSums[i] = new List<long>();
            rightSums[i] = new List<long>();
        }

        int limit = 1 << n;
        for (int mask = 0; mask < limit; mask++) {
            int cnt = BitOperations.PopCount((uint)mask);
            long sum = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) sum += left[i];
            }
            leftSums[cnt].Add(sum);
        }

        for (int mask = 0; mask < limit; mask++) {
            int cnt = BitOperations.PopCount((uint)mask);
            long sum = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) sum += right[i];
            }
            rightSums[cnt].Add(sum);
        }

        for (int i = 0; i <= n; i++) {
            rightSums[i].Sort();
        }

        long best = long.MaxValue;
        foreach (var leftList in leftSums) { } // placeholder to avoid unused warning

        for (int k = 0; k <= n; k++) {
            var Llist = leftSums[k];
            var Rlist = rightSums[n - k];
            if (Rlist.Count == 0) continue;

            foreach (long sumL in Llist) {
                long need = ((long)total) / 2 - sumL;
                int idx = Rlist.BinarySearch(need);
                if (idx >= 0) {
                    long totalSum = sumL + Rlist[idx];
                    long diff = Math.Abs((long)total - 2 * totalSum);
                    if (diff < best) best = diff;
                } else {
                    int insertPos = ~idx;
                    if (insertPos < Rlist.Count) {
                        long totalSum = sumL + Rlist[insertPos];
                        long diff = Math.Abs((long)total - 2 * totalSum);
                        if (diff < best) best = diff;
                    }
                    if (insertPos > 0) {
                        long totalSum = sumL + Rlist[insertPos - 1];
                        long diff = Math.Abs((long)total - 2 * totalSum);
                        if (diff < best) best = diff;
                    }
                }

                if (best == 0) return 0; // early exit
            }
        }

        return (int)best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDifference = function(nums) {
    const totalLen = nums.length;
    const n = totalLen >> 1; // half size
    const totalSum = nums.reduce((a, b) => a + b, 0);
    const target = totalSum / 2;

    const mid = totalLen >> 1;
    const left = nums.slice(0, mid);
    const right = nums.slice(mid);

    const a = left.length;
    const b = right.length;

    // generate subset sums grouped by count for left part
    const sumsLeft = Array.from({ length: a + 1 }, () => []);
    const limitA = 1 << a;
    for (let mask = 0; mask < limitA; ++mask) {
        let cnt = 0, sum = 0;
        for (let i = 0; i < a; ++i) {
            if ((mask >> i) & 1) {
                cnt++;
                sum += left[i];
            }
        }
        sumsLeft[cnt].push(sum);
    }

    // generate subset sums grouped by count for right part
    const sumsRight = Array.from({ length: b + 1 }, () => []);
    const limitB = 1 << b;
    for (let mask = 0; mask < limitB; ++mask) {
        let cnt = 0, sum = 0;
        for (let i = 0; i < b; ++i) {
            if ((mask >> i) & 1) {
                cnt++;
                sum += right[i];
            }
        }
        sumsRight[cnt].push(sum);
    }

    // sort each list in right part for binary search
    for (let i = 0; i <= b; ++i) {
        sumsRight[i].sort((x, y) => x - y);
    }

    let best = Infinity;

    // combine subsets to get exactly n elements total
    for (let k = 0; k <= a; ++k) {
        const need = n - k;
        if (need < 0 || need > b) continue;
        const rightList = sumsRight[need];
        if (!rightList.length) continue;

        for (const sumL of sumsLeft[k]) {
            const desired = target - sumL;
            // binary search lower bound in rightList
            let lo = 0, hi = rightList.length - 1;
            while (lo <= hi) {
                const midIdx = (lo + hi) >> 1;
                if (rightList[midIdx] < desired) lo = midIdx + 1;
                else hi = midIdx - 1;
            }
            // check candidate at lo
            if (lo < rightList.length) {
                const total = sumL + rightList[lo];
                const diff = Math.abs(total * 2 - totalSum);
                if (diff < best) best = diff;
            }
            // check candidate at lo-1
            if (lo > 0) {
                const total = sumL + rightList[lo - 1];
                const diff = Math.abs(total * 2 - totalSum);
                if (diff < best) best = diff;
            }
        }
    }

    return best;
};
```

## Typescript

```typescript
function minimumDifference(nums: number[]): number {
    const m = nums.length;
    const n = m / 2;
    const total = nums.reduce((a, b) => a + b, 0);
    const target = total / 2;

    const left = nums.slice(0, n);
    const right = nums.slice(n);

    const leftSums: number[][] = Array.from({ length: n + 1 }, () => []);
    const rightSums: number[][] = Array.from({ length: n + 1 }, () => []);

    const lLen = left.length;
    for (let mask = 0; mask < (1 << lLen); ++mask) {
        let cnt = 0, sum = 0;
        for (let i = 0; i < lLen; ++i) {
            if ((mask >> i) & 1) {
                cnt++;
                sum += left[i];
            }
        }
        leftSums[cnt].push(sum);
    }

    const rLen = right.length;
    for (let mask = 0; mask < (1 << rLen); ++mask) {
        let cnt = 0, sum = 0;
        for (let i = 0; i < rLen; ++i) {
            if ((mask >> i) & 1) {
                cnt++;
                sum += right[i];
            }
        }
        rightSums[cnt].push(sum);
    }

    for (let k = 0; k <= n; ++k) rightSums[k].sort((a, b) => a - b);

    let ans = Number.MAX_SAFE_INTEGER;

    function lowerBound(arr: number[], val: number): number {
        let l = 0, r = arr.length;
        while (l < r) {
            const mid = (l + r) >> 1;
            if (arr[mid] < val) l = mid + 1;
            else r = mid;
        }
        return l;
    }

    for (let k = 0; k <= n; ++k) {
        const listL = leftSums[k];
        const listR = rightSums[n - k];
        if (!listR.length) continue;
        for (const sumL of listL) {
            const need = target - sumL;
            const idx = lowerBound(listR, need);
            const candidates: number[] = [];
            if (idx < listR.length) candidates.push(listR[idx]);
            if (idx > 0) candidates.push(listR[idx - 1]);
            for (const sumR of candidates) {
                const curSum = sumL + sumR;
                const diff = Math.abs(2 * curSum - total);
                if (diff < ans) ans = diff;
            }
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
     * @return Integer
     */
    function minimumDifference($nums) {
        $len = count($nums);
        $n = intdiv($len, 2);
        $left = array_slice($nums, 0, $n);
        $right = array_slice($nums, $n);

        $leftSums = $this->getSumsByCount($left);
        $rightSums = $this->getSumsByCount($right);

        foreach ($leftSums as &$list) {
            sort($list);
        }
        unset($list);
        foreach ($rightSums as &$list) {
            sort($list);
        }
        unset($list);

        $total = array_sum($nums);
        $target = $total / 2.0;
        $ans = PHP_INT_MAX;

        for ($k = 0; $k <= $n; $k++) {
            $listL = $leftSums[$k];
            $listR = $rightSums[$n - $k];
            if (empty($listL) || empty($listR)) continue;
            foreach ($listL as $sL) {
                $need = $target - $sL;
                $idx = $this->lowerBound($listR, $need);
                // candidate idx
                if ($idx < count($listR)) {
                    $combined = $sL + $listR[$idx];
                    $diff = abs($total - 2 * $combined);
                    if ($diff < $ans) $ans = $diff;
                }
                // candidate idx-1
                if ($idx > 0) {
                    $combined = $sL + $listR[$idx - 1];
                    $diff = abs($total - 2 * $combined);
                    if ($diff < $ans) $ans = $diff;
                }
            }
        }

        return $ans;
    }

    private function getSumsByCount($arr) {
        $size = count($arr);
        $totalMasks = 1 << $size;
        $result = array_fill(0, $size + 1, []);
        for ($mask = 0; $mask < $totalMasks; $mask++) {
            $sum = 0;
            $cnt = 0;
            for ($i = 0; $i < $size; $i++) {
                if ($mask & (1 << $i)) {
                    $sum += $arr[$i];
                    $cnt++;
                }
            }
            $result[$cnt][] = $sum;
        }
        return $result;
    }

    private function lowerBound($arr, $target) {
        $low = 0;
        $high = count($arr);
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($arr[$mid] < $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func minimumDifference(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        let n = nums.count / 2
        let left = Array(nums[0..<n])
        let right = Array(nums[n..<nums.count])
        
        var leftSums = Array(repeating: [Int](), count: n + 1)
        var rightSums = Array(repeating: [Int](), count: n + 1)
        
        // subsets for left half
        let limit = 1 << n
        for mask in 0..<limit {
            var sum = 0
            var cnt = 0
            for i in 0..<n {
                if (mask & (1 << i)) != 0 {
                    sum += left[i]
                    cnt += 1
                }
            }
            leftSums[cnt].append(sum)
        }
        
        // subsets for right half
        for mask in 0..<limit {
            var sum = 0
            var cnt = 0
            for i in 0..<n {
                if (mask & (1 << i)) != 0 {
                    sum += right[i]
                    cnt += 1
                }
            }
            rightSums[cnt].append(sum)
        }
        
        // sort right sums for binary search
        for i in 0...n {
            rightSums[i].sort()
        }
        
        var answer = Int.max
        let target = total / 2
        
        for k in 0...n {
            let lList = leftSums[k]
            let rList = rightSums[n - k]
            if rList.isEmpty { continue }
            for sumL in lList {
                let desired = target - sumL
                // lower bound binary search
                var lo = 0, hi = rList.count
                while lo < hi {
                    let mid = (lo + hi) >> 1
                    if rList[mid] < desired {
                        lo = mid + 1
                    } else {
                        hi = mid
                    }
                }
                // check candidate at lo
                if lo < rList.count {
                    let s = sumL + rList[lo]
                    let diff = abs(total - 2 * s)
                    if diff < answer { answer = diff }
                }
                // check candidate before lo
                if lo > 0 {
                    let s = sumL + rList[lo - 1]
                    let diff = abs(total - 2 * s)
                    if diff < answer { answer = diff }
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
import kotlin.math.abs

class Solution {
    fun minimumDifference(nums: IntArray): Int {
        val n = nums.size / 2
        val totalSum = nums.fold(0L) { acc, v -> acc + v }
        val half = totalSum / 2

        // left half subsets
        val leftSums = Array(n + 1) { mutableListOf<Long>() }
        for (mask in 0 until (1 shl n)) {
            var cnt = 0
            var sum = 0L
            var m = mask
            var idx = 0
            while (m != 0) {
                if ((m and 1) == 1) {
                    cnt++
                    sum += nums[idx].toLong()
                }
                idx++
                m = m shr 1
            }
            // handle remaining bits where mask may have zeros, need to add contributions for zero bits? No.
            // For bits not set, nothing added.
            leftSums[cnt].add(sum)
        }

        // right half subsets
        val rightSums = Array(n + 1) { mutableListOf<Long>() }
        for (mask in 0 until (1 shl n)) {
            var cnt = 0
            var sum = 0L
            var m = mask
            var idx = 0
            while (m != 0) {
                if ((m and 1) == 1) {
                    cnt++
                    sum += nums[n + idx].toLong()
                }
                idx++
                m = m shr 1
            }
            rightSums[cnt].add(sum)
        }

        for (list in rightSums) {
            list.sort()
        }

        var minDiff = Long.MAX_VALUE

        for (k in 0..n) {
            val leftList = leftSums[k]
            val rightList = rightSums[n - k]
            if (rightList.isEmpty()) continue
            for (sumL in leftList) {
                val need = half - sumL
                var idx = java.util.Collections.binarySearch(rightList, need)
                if (idx >= 0) {
                    val totalA = sumL + rightList[idx]
                    val diff = abs(2 * totalA - totalSum)
                    if (diff < minDiff) minDiff = diff
                } else {
                    idx = -(idx + 1)
                    if (idx < rightList.size) {
                        val totalA = sumL + rightList[idx]
                        val diff = abs(2 * totalA - totalSum)
                        if (diff < minDiff) minDiff = diff
                    }
                    if (idx > 0) {
                        val totalA = sumL + rightList[idx - 1]
                        val diff = abs(2 * totalA - totalSum)
                        if (diff < minDiff) minDiff = diff
                    }
                }
            }
        }

        return minDiff.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumDifference(List<int> nums) {
    int len = nums.length;
    int n = len ~/ 2;
    int total = 0;
    for (int v in nums) total += v;

    List<int> left = nums.sublist(0, n);
    List<int> right = nums.sublist(n);

    List<List<int>> genSums(List<int> arr) {
      int m = arr.length;
      List<List<int>> byCnt = List.generate(m + 1, (_) => []);
      int totalMasks = 1 << m;
      for (int mask = 0; mask < totalMasks; ++mask) {
        int cnt = 0;
        int sum = 0;
        for (int i = 0; i < m; ++i) {
          if ((mask & (1 << i)) != 0) {
            cnt++;
            sum += arr[i];
          }
        }
        byCnt[cnt].add(sum);
      }
      return byCnt;
    }

    List<List<int>> leftSums = genSums(left);
    List<List<int>> rightSums = genSums(right);
    for (var lst in rightSums) {
      lst.sort();
    }

    int targetHalf = total ~/ 2;
    int minDiff = (total).abs(); // worst case

    int lowerBound(List<int> list, int value) {
      int l = 0, r = list.length;
      while (l < r) {
        int mid = (l + r) >> 1;
        if (list[mid] < value) {
          l = mid + 1;
        } else {
          r = mid;
        }
      }
      return l;
    }

    for (int k = 0; k <= n; ++k) {
      List<int> leftList = leftSums[k];
      List<int> rightList = rightSums[n - k];
      if (rightList.isEmpty) continue;
      for (int sL in leftList) {
        int need = targetHalf - sL;
        int idx = lowerBound(rightList, need);
        if (idx < rightList.length) {
          int sR = rightList[idx];
          int diff = (total - 2 * (sL + sR)).abs();
          if (diff < minDiff) minDiff = diff;
        }
        if (idx > 0) {
          int sR = rightList[idx - 1];
          int diff = (total - 2 * (sL + sR)).abs();
          if (diff < minDiff) minDiff = diff;
        }
      }
    }

    return minDiff;
  }
}
```

## Golang

```go
package main

import (
	"sort"
	"math/bits"
)

func minimumDifference(nums []int) int {
	totalLen := len(nums)
	half := totalLen / 2
	left := nums[:half]
	right := nums[half:]

	// generate subset sums grouped by count for left half
	leftSums := make([][]int, len(left)+1)
	for mask := 0; mask < (1 << uint(len(left))); mask++ {
		cnt := bits.OnesCount(uint(mask))
		sum := 0
		for i := 0; i < len(left); i++ {
			if mask&(1<<uint(i)) != 0 {
				sum += left[i]
			}
		}
		leftSums[cnt] = append(leftSums[cnt], sum)
	}

	// generate subset sums grouped by count for right half
	rightSums := make([][]int, len(right)+1)
	for mask := 0; mask < (1 << uint(len(right))); mask++ {
		cnt := bits.OnesCount(uint(mask))
		sum := 0
		for i := 0; i < len(right); i++ {
			if mask&(1<<uint(i)) != 0 {
				sum += right[i]
			}
		}
		rightSums[cnt] = append(rightSums[cnt], sum)
	}

	// sort each list in right half for binary search
	for _, lst := range rightSums {
		sort.Ints(lst)
	}

	totalSum := 0
	for _, v := range nums {
		totalSum += v
	}
	target := totalSum / 2

	n := totalLen / 2 // size of each partition
	best := int(^uint(0) >> 1) // max int

	for k := 0; k <= len(left); k++ {
		if k > n || n-k > len(right) {
			continue
		}
		leftList := leftSums[k]
		rightList := rightSums[n-k]

		for _, sl := range leftList {
			need := target - sl
			idx := sort.SearchInts(rightList, need)

			if idx < len(rightList) {
				sumA := sl + rightList[idx]
				diff := abs(2*sumA - totalSum)
				if diff < best {
					best = diff
				}
			}
			if idx > 0 {
				sumA := sl + rightList[idx-1]
				diff := abs(2*sumA - totalSum)
				if diff < best {
					best = diff
				}
			}
		}
	}

	return best
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def minimum_difference(nums)
  total = nums.sum
  n = nums.length / 2
  m = n # split into two halves of size n

  left = nums[0...m]
  right = nums[m..-1]

  sums_left = Array.new(m + 1) { [] }
  (0...(1 << m)).each do |mask|
    sum = 0
    cnt = 0
    i = 0
    while i < m
      if (mask & (1 << i)) != 0
        sum += left[i]
        cnt += 1
      end
      i += 1
    end
    sums_left[cnt] << sum
  end

  r_len = right.length
  sums_right = Array.new(r_len + 1) { [] }
  (0...(1 << r_len)).each do |mask|
    sum = 0
    cnt = 0
    i = 0
    while i < r_len
      if (mask & (1 << i)) != 0
        sum += right[i]
        cnt += 1
      end
      i += 1
    end
    sums_right[cnt] << sum
  end

  sums_right.each { |arr| arr.sort! }

  best = total.abs
  (0..m).each do |k|
    t = n - k
    next if t < 0 || t > r_len
    left_arr = sums_left[k]
    right_arr = sums_right[t]
    next if left_arr.empty? || right_arr.empty?
    left_arr.each do |sum_l|
      # binary search in right_arr for value closest to (total/2 - sum_l)
      desired = total / 2.0 - sum_l
      idx = right_arr.bsearch_index { |x| x >= desired }
      if idx
        sum_total = sum_l + right_arr[idx]
        diff = (total - 2 * sum_total).abs
        best = diff if diff < best
        if idx > 0
          sum_total = sum_l + right_arr[idx - 1]
          diff = (total - 2 * sum_total).abs
          best = diff if diff < best
        end
      else
        # all elements less than desired, take the largest
        sum_total = sum_l + right_arr[-1]
        diff = (total - 2 * sum_total).abs
        best = diff if diff < best
      end
    end
  end

  best
end
```

## Scala

```scala
object Solution {
    def minimumDifference(nums: Array[Int]): Int = {
        val total: Long = nums.map(_.toLong).sum
        val nHalf: Int = nums.length / 2
        val left = nums.take(nHalf)
        val right = nums.drop(nHalf)

        import scala.collection.mutable.ArrayBuffer

        val leftSums = Array.fill(nHalf + 1)(ArrayBuffer[Long]())
        val rightSums = Array.fill(nHalf + 1)(ArrayBuffer[Long]())

        // enumerate subsets for left half
        val limitL = 1 << left.length
        var mask = 0
        while (mask < limitL) {
            var sum: Long = 0L
            var cnt = 0
            var i = 0
            while (i < left.length) {
                if ((mask & (1 << i)) != 0) {
                    sum += left(i).toLong
                    cnt += 1
                }
                i += 1
            }
            leftSums(cnt) += sum
            mask += 1
        }

        // enumerate subsets for right half
        val limitR = 1 << right.length
        mask = 0
        while (mask < limitR) {
            var sum: Long = 0L
            var cnt = 0
            var i = 0
            while (i < right.length) {
                if ((mask & (1 << i)) != 0) {
                    sum += right(i).toLong
                    cnt += 1
                }
                i += 1
            }
            rightSums(cnt) += sum
            mask += 1
        }

        // sort each right list for binary search
        val rightArr: Array[Array[Long]] = rightSums.map { buf =>
            val arr = buf.toArray
            java.util.Arrays.sort(arr)
            arr
        }

        var answer: Long = Long.MaxValue
        val target: Long = total / 2

        var k = 0
        while (k <= nHalf) {
            val leftList = leftSums(k)
            val rArr = rightArr(nHalf - k)
            if (rArr.nonEmpty) {
                var idxL = 0
                while (idxL < leftList.length) {
                    val sumL = leftList(idxL)
                    val need = target - sumL
                    var pos = java.util.Arrays.binarySearch(rArr, need)
                    if (pos >= 0) {
                        val totalSel = sumL + rArr(pos)
                        val diff = math.abs(total - 2 * totalSel)
                        if (diff < answer) answer = diff
                    } else {
                        pos = -pos - 1 // insertion point
                        if (pos < rArr.length) {
                            val totalSel = sumL + rArr(pos)
                            val diff = math.abs(total - 2 * totalSel)
                            if (diff < answer) answer = diff
                        }
                        if (pos > 0) {
                            val totalSel = sumL + rArr(pos - 1)
                            val diff = math.abs(total - 2 * totalSel)
                            if (diff < answer) answer = diff
                        }
                    }
                    idxL += 1
                }
            }
            k += 1
        }

        answer.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_difference(nums: Vec<i32>) -> i32 {
        let total_len = nums.len();
        let n = total_len / 2;
        let left = &nums[..n];
        let right = &nums[n..];

        // generate all subset sums grouped by count of elements
        fn gen_sums(arr: &[i32]) -> Vec<Vec<i64>> {
            let m = arr.len();
            let mut res: Vec<Vec<i64>> = vec![Vec::new(); m + 1];
            for mask in 0usize..(1usize << m) {
                let mut cnt = 0usize;
                let mut sum: i64 = 0;
                for i in 0..m {
                    if (mask >> i) & 1 == 1 {
                        cnt += 1;
                        sum += arr[i] as i64;
                    }
                }
                res[cnt].push(sum);
            }
            for v in res.iter_mut() {
                v.sort_unstable();
            }
            res
        }

        let left_sums = gen_sums(left);
        let right_sums = gen_sums(right);

        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        let target = total / 2; // we aim for sum close to this

        let mut best: i64 = i64::MAX;

        for k in 0..=n {
            let left_vec = &left_sums[k];
            let right_vec = &right_sums[n - k];
            if left_vec.is_empty() || right_vec.is_empty() {
                continue;
            }
            for &s_left in left_vec.iter() {
                let need = target - s_left;
                // binary search in right_vec for value closest to `need`
                match right_vec.binary_search(&need) {
                    Ok(idx) => {
                        let s_right = right_vec[idx];
                        let selected = s_left + s_right;
                        let diff = (total - 2 * selected).abs();
                        if diff < best {
                            best = diff;
                        }
                    }
                    Err(pos) => {
                        // candidate at pos
                        if pos < right_vec.len() {
                            let s_right = right_vec[pos];
                            let selected = s_left + s_right;
                            let diff = (total - 2 * selected).abs();
                            if diff < best {
                                best = diff;
                            }
                        }
                        // candidate at pos-1
                        if pos > 0 {
                            let s_right = right_vec[pos - 1];
                            let selected = s_left + s_right;
                            let diff = (total - 2 * selected).abs();
                            if diff < best {
                                best = diff;
                            }
                        }
                    }
                }
            }
        }

        best as i32
    }
}
```

## Racket

```racket
(require racket/list)

(define (lower-bound vec target)
  (let loop ((l 0) (r (vector-length vec)))
    (if (= l r)
        l
        (let* ((mid (quotient (+ l r) 2))
               (val (vector-ref vec mid)))
          (if (< val target)
              (loop (+ mid 1) r)
              (loop l mid))))))

(define (gen-sums arr)
  (let* ((m (length arr))
         (sums (make-vector (add1 m) '())))
    (let recur ((idx 0) (cur 0) (cnt 0))
      (if (= idx m)
          (let ([lst (vector-ref sums cnt)])
            (vector-set! sums cnt (cons cur lst)))
          (begin
            (recur (+ idx 1) cur cnt)
            (recur (+ idx 1) (+ cur (list-ref arr idx)) (+ cnt 1)))))
    (for ([i (in-range (add1 m))])
      (let* ((lst (vector-ref sums i))
             (sorted (sort lst <)))
        (vector-set! sums i (list->vector sorted))))
    sums))

(define/contract (minimum-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((len (length nums))
         (n (/ len 2))
         (left (take nums n))
         (right (drop nums n))
         (total (apply + nums))
         (left-sums (gen-sums left))
         (right-sums (gen-sums right)))
    (define best (expt 2 60))
    (for ([k (in-range (add1 n))])
      (let* ((ls (vector-ref left-sums k))
             (rs (vector-ref right-sums (- n k))))
        (when (and (> (vector-length ls) 0) (> (vector-length rs) 0))
          (for ([i (in-range (vector-length ls))])
            (define sumL (vector-ref ls i))
            (define targetR (- (/ total 2) sumL))
            (define idx (lower-bound rs targetR))
            (for ([j (in-list (list idx (- idx 1)))])
              (when (and (>= j 0) (< j (vector-length rs)))
                (define sumR (vector-ref rs j))
                (define combined (+ sumL sumR))
                (define diff (abs (- total (* 2 combined))))
                (when (< diff best)
                  (set! best diff)))))))))
    best))
```

## Erlang

```erlang
-spec minimum_difference(Nums :: [integer()]) -> integer().
minimum_difference(Nums) ->
    Total = lists:sum(Nums),
    Len = length(Nums),
    N = Len div 2,
    {Left, Right} = split_half(Nums, N),
    LeftMap = subset_sums(Left),
    RightMap = subset_sums(Right),
    Target = Total div 2,
    InitialMin = 1 bsl 60,
    MinDiff = find_min(N, Total, Target, LeftMap, RightMap, InitialMin),
    MinDiff.

split_half(List, N) ->
    {lists:sublist(List, N), lists:nthtail(N, List)}.

%% Build map from count -> list of subset sums
subset_sums(Arr) ->
    Len = length(Arr),
    MaxMask = (1 bsl Len) - 1,
    subset_sums_loop(0, MaxMask, Arr, maps:new()).

subset_sums_loop(Mask, MaxMask, _Arr, Acc) when Mask > MaxMask ->
    Acc;
subset_sums_loop(Mask, MaxMask, Arr, Acc) ->
    {Sum, Count} = compute_sum_count(Mask, Arr, 0, 0, 0),
    UpdatedAcc = maps:update_with(
        Count,
        fun(List) -> [Sum | List] end,
        [Sum],
        Acc),
    subset_sums_loop(Mask + 1, MaxMask, Arr, UpdatedAcc).

compute_sum_count(_Mask, [], _Idx, Sum, Count) ->
    {Sum, Count};
compute_sum_count(Mask, [H|T], Idx, Sum, Count) ->
    if (Mask band (1 bsl Idx)) =/= 0 ->
            compute_sum_count(Mask, T, Idx + 1, Sum + H, Count + 1);
       true ->
            compute_sum_count(Mask, T, Idx + 1, Sum, Count)
    end.

find_min(N, Total, Target, LMap, RMap, CurrentMin) ->
    lists:foldl(
        fun(K, Acc) ->
            LeftSums = maps:get(K, LMap, []),
            RightSums = maps:get(N - K, RMap, []),
            case RightSums of
                [] -> Acc;
                _ ->
                    SortedRight = lists:sort(RightSums),
                    RightTuple = list_to_tuple(SortedRight),
                    SizeR = tuple_size(RightTuple),
                    fold_left_sums(LeftSums, Target, Total, RightTuple, SizeR, Acc)
            end
        end,
        CurrentMin,
        lists:seq(0, N)
    ).

fold_left_sums([], _Target, _Total, _RightTuple, _SizeR, MinAcc) ->
    MinAcc;
fold_left_sums([Lsum|Rest], Target, Total, RightTuple, SizeR, MinAcc) ->
    Desired = Target - Lsum,
    BestRight = binary_closest(RightTuple, SizeR, Desired),
    Diff = erlang:abs(Total - 2 * (Lsum + BestRight)),
    NewMin = if Diff < MinAcc -> Diff; true -> MinAcc end,
    fold_left_sums(Rest, Target, Total, RightTuple, SizeR, NewMin).

binary_closest(_Tuple, _Size, Target) when is_integer(Target) ->
    % placeholder for exact match case handled in binary_search
    ok.

binary_closest(Tuple, Size, Target) ->
    binary_search(Tuple, Size, Target, 1, Size).

binary_search(_Tuple, _Size, Target, Low, High) when Low > High ->
    % No exact match; pick nearest neighbor using low/high indices
    Cand = [],
    Cand1 = if High >= 1 -> [element(High, _Tuple)] else [] end,
    Cand2 = if Low =< _Size -> [element(Low, _Tuple)] else [] end,
    AllCand = Cand1 ++ Cand2,
    {BestVal,_} = lists:min(
        [{erlang:abs(Target - V), V} || V <- AllCand]),
    BestVal;
binary_search(Tuple, Size, Target, Low, High) ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid, Tuple),
    if MidVal == Target ->
            Target;
       MidVal < Target ->
            binary_search(Tuple, Size, Target, Mid + 1, High);
       true ->
            binary_search(Tuple, Size, Target, Low, Mid - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec minimum_difference(nums :: [integer]) :: integer
  def minimum_difference(nums) do
    n = div(length(nums), 2)
    total = Enum.sum(nums)
    target_half = div(total, 2)

    left = Enum.take(nums, n)
    right = Enum.drop(nums, n)

    left_map = gen(left)
    right_map = gen(right)

    right_tuples =
      for {k, list} <- right_map, into: %{} do
        {k, List.to_tuple(Enum.sort(list))}
      end

    Enum.reduce(0..n, :math.pow(2, 63) |> trunc(), fn k, acc ->
      list1 = Map.get(left_map, k)
      tuple2 = Map.get(right_tuples, n - k)
      len2 = tuple_size(tuple2)

      Enum.reduce(list1, acc, fn s1, cur_min ->
        need = target_half - s1
        idx = lower_bound_tuple(tuple2, need)

        cur_min =
          if idx < len2 do
            s2 = elem(tuple2, idx)
            sum_a = s1 + s2
            diff = abs(total - 2 * sum_a)
            min(cur_min, diff)
          else
            cur_min
          end

        if idx > 0 do
          s2 = elem(tuple2, idx - 1)
          sum_a = s1 + s2
          diff = abs(total - 2 * sum_a)
          min(cur_min, diff)
        else
          cur_min
        end
      end)
    end)
  end

  defp gen(arr) do
    m = length(arr)
    total_masks = 1 <<< m
    init_map = for k <- 0..m, into: %{}, do: {k, []}

    Enum.reduce(0..total_masks - 1, init_map, fn mask, mp ->
      {cnt, sum} = calc(mask, arr)
      Map.update!(mp, cnt, &[sum | &1])
    end)
  end

  defp calc(mask, arr) do
    Enum.reduce(Enum.with_index(arr), {0, 0}, fn {val, i}, {c, s} ->
      if (mask &&& (1 <<< i)) != 0 do
        {c + 1, s + val}
      else
        {c, s}
      end
    end)
  end

  defp lower_bound_tuple(tuple, target) do
    size = tuple_size(tuple)
    lb(0, size, tuple, target)
  end

  defp lb(low, high, _tuple, _target) when low >= high, do: low

  defp lb(low, high, tuple, target) do
    mid = div(low + high, 2)

    if elem(tuple, mid) < target do
      lb(mid + 1, high, tuple, target)
    else
      lb(low, mid, tuple, target)
    end
  end
end
```

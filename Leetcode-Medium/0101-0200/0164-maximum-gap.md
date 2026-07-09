# 0164. Maximum Gap

## Cpp

```cpp
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;
        int mn = *min_element(nums.begin(), nums.end());
        int mx = *max_element(nums.begin(), nums.end());
        if (mn == mx) return 0;
        
        // bucket size at least 1
        long long bucketSize = max(1LL, (long long)(mx - mn) / (n - 1));
        int bucketCount = (int)((mx - mn) / bucketSize) + 1;
        
        vector<int> bucketMin(bucketCount, INT_MAX);
        vector<int> bucketMax(bucketCount, INT_MIN);
        vector<bool> used(bucketCount, false);
        
        for (int v : nums) {
            int idx = (int)((v - mn) / bucketSize);
            bucketMin[idx] = min(bucketMin[idx], v);
            bucketMax[idx] = max(bucketMax[idx], v);
            used[idx] = true;
        }
        
        int prevMax = mx; // placeholder
        bool first = true;
        int ans = 0;
        for (int i = 0; i < bucketCount; ++i) {
            if (!used[i]) continue;
            if (first) {
                prevMax = bucketMax[i];
                first = false;
            } else {
                ans = max(ans, bucketMin[i] - prevMax);
                prevMax = bucketMax[i];
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximumGap(int[] nums) {
        if (nums == null || nums.length < 2) return 0;
        int n = nums.length;
        int min = nums[0];
        int max = nums[0];
        for (int v : nums) {
            if (v < min) min = v;
            if (v > max) max = v;
        }
        if (min == max) return 0;

        int bucketSize = Math.max(1, (max - min) / (n - 1));
        int bucketCount = (max - min) / bucketSize + 1;

        int[] bucketMin = new int[bucketCount];
        int[] bucketMax = new int[bucketCount];
        boolean[] used = new boolean[bucketCount];
        Arrays.fill(bucketMin, Integer.MAX_VALUE);
        Arrays.fill(bucketMax, Integer.MIN_VALUE);

        for (int v : nums) {
            int idx = (v - min) / bucketSize;
            if (!used[idx]) {
                used[idx] = true;
                bucketMin[idx] = v;
                bucketMax[idx] = v;
            } else {
                if (v < bucketMin[idx]) bucketMin[idx] = v;
                if (v > bucketMax[idx]) bucketMax[idx] = v;
            }
        }

        int prevMax = min;
        int maxGap = 0;
        for (int i = 0; i < bucketCount; i++) {
            if (!used[i]) continue;
            maxGap = Math.max(maxGap, bucketMin[i] - prevMax);
            prevMax = bucketMax[i];
        }
        return maxGap;
    }
}
```

## Python

```python
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0

        # bucket size and count
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = ((max_val - min_val) // bucket_size) + 1

        bucket_min = [None] * bucket_count
        bucket_max = [None] * bucket_count

        for num in nums:
            idx = (num - min_val) // bucket_size
            if bucket_min[idx] is None:
                bucket_min[idx] = bucket_max[idx] = num
            else:
                if num < bucket_min[idx]:
                    bucket_min[idx] = num
                if num > bucket_max[idx]:
                    bucket_max[idx] = num

        max_gap = 0
        prev_max = min_val
        for i in range(bucket_count):
            if bucket_min[i] is None:
                continue
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return max_gap
```

## Python3

```python
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0

        # bucket size and count
        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_cnt = ((mx - mn) // bucket_size) + 1

        bucket_min = [None] * bucket_cnt
        bucket_max = [None] * bucket_cnt

        for v in nums:
            idx = (v - mn) // bucket_size
            if bucket_min[idx] is None:
                bucket_min[idx] = bucket_max[idx] = v
            else:
                if v < bucket_min[idx]:
                    bucket_min[idx] = v
                if v > bucket_max[idx]:
                    bucket_max[idx] = v

        max_gap = 0
        prev_max = mn
        for i in range(bucket_cnt):
            if bucket_min[i] is None:
                continue
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return max_gap
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int maximumGap(int* nums, int numsSize) {
    if (numsSize < 2) return 0;

    int i;
    int minVal = nums[0], maxVal = nums[0];
    for (i = 1; i < numsSize; ++i) {
        if (nums[i] < minVal) minVal = nums[i];
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    if (minVal == maxVal) return 0;

    int bucketSize = (maxVal - minVal) / (numsSize - 1);
    if (bucketSize == 0) bucketSize = 1;
    int bucketCount = (maxVal - minVal) / bucketSize + 1;

    int *bMin = (int *)malloc(bucketCount * sizeof(int));
    int *bMax = (int *)malloc(bucketCount * sizeof(int));
    char *used = (char *)calloc(bucketCount, sizeof(char));

    for (i = 0; i < bucketCount; ++i) {
        bMin[i] = INT_MAX;
        bMax[i] = INT_MIN;
    }

    for (i = 0; i < numsSize; ++i) {
        int idx = (nums[i] - minVal) / bucketSize;
        if (!used[idx]) {
            used[idx] = 1;
            bMin[idx] = bMax[idx] = nums[i];
        } else {
            if (nums[i] < bMin[idx]) bMin[idx] = nums[i];
            if (nums[i] > bMax[idx]) bMax[idx] = nums[i];
        }
    }

    int prevMax = minVal;
    int maxGap = 0;
    for (i = 0; i < bucketCount; ++i) {
        if (!used[i]) continue;
        int gap = bMin[i] - prevMax;
        if (gap > maxGap) maxGap = gap;
        prevMax = bMax[i];
    }

    free(bMin);
    free(bMax);
    free(used);
    return maxGap;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumGap(int[] nums) {
        int n = nums.Length;
        if (n < 2) return 0;

        int min = nums[0], max = nums[0];
        foreach (int x in nums) {
            if (x < min) min = x;
            if (x > max) max = x;
        }
        if (min == max) return 0;

        // bucket size = ceil((max - min) / (n - 1))
        int bucketSize = Math.Max(1, (int)Math.Ceiling((double)(max - min) / (n - 1)));
        int bucketCount = ((max - min) / bucketSize) + 1;

        int[] bucketMin = new int[bucketCount];
        int[] bucketMax = new int[bucketCount];
        bool[] used = new bool[bucketCount];

        for (int i = 0; i < bucketCount; i++) {
            bucketMin[i] = int.MaxValue;
            bucketMax[i] = int.MinValue;
        }

        foreach (int x in nums) {
            int idx = (x - min) / bucketSize;
            if (!used[idx]) {
                used[idx] = true;
                bucketMin[idx] = x;
                bucketMax[idx] = x;
            } else {
                if (x < bucketMin[idx]) bucketMin[idx] = x;
                if (x > bucketMax[idx]) bucketMax[idx] = x;
            }
        }

        int prevMax = min;
        int maxGap = 0;
        for (int i = 0; i < bucketCount; i++) {
            if (!used[i]) continue;
            maxGap = Math.Max(maxGap, bucketMin[i] - prevMax);
            prevMax = bucketMax[i];
        }

        return maxGap;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumGap = function(nums) {
    const n = nums.length;
    if (n < 2) return 0;

    // Find global min and max
    let minVal = nums[0], maxVal = nums[0];
    for (let i = 1; i < n; ++i) {
        const v = nums[i];
        if (v < minVal) minVal = v;
        else if (v > maxVal) maxVal = v;
    }
    if (minVal === maxVal) return 0;

    // Determine bucket size and count
    const bucketSize = Math.max(1, Math.floor((maxVal - minVal) / (n - 1)));
    const bucketCount = Math.floor((maxVal - minVal) / bucketSize) + 1;

    const bucketMin = new Array(bucketCount).fill(Infinity);
    const bucketMax = new Array(bucketCount).fill(-Infinity);

    // Distribute numbers into buckets
    for (let i = 0; i < n; ++i) {
        const idx = Math.floor((nums[i] - minVal) / bucketSize);
        if (nums[i] < bucketMin[idx]) bucketMin[idx] = nums[i];
        if (nums[i] > bucketMax[idx]) bucketMax[idx] = nums[i];
    }

    // Scan buckets to find maximum gap
    let maxGap = 0;
    let prevMax = minVal;
    for (let i = 0; i < bucketCount; ++i) {
        if (bucketMin[i] === Infinity) continue; // empty bucket
        maxGap = Math.max(maxGap, bucketMin[i] - prevMax);
        prevMax = bucketMax[i];
    }

    return maxGap;
};
```

## Typescript

```typescript
function maximumGap(nums: number[]): number {
    const n = nums.length;
    if (n < 2) return 0;

    let minVal = nums[0];
    let maxVal = nums[0];
    for (let i = 1; i < n; i++) {
        const v = nums[i];
        if (v < minVal) minVal = v;
        else if (v > maxVal) maxVal = v;
    }
    if (minVal === maxVal) return 0;

    const bucketSize = Math.max(1, Math.floor((maxVal - minVal) / (n - 1)));
    const bucketCount = Math.floor((maxVal - minVal) / bucketSize) + 1;

    const bucketMin: number[] = new Array(bucketCount).fill(Infinity);
    const bucketMax: number[] = new Array(bucketCount).fill(-Infinity);

    for (let i = 0; i < n; i++) {
        const v = nums[i];
        const idx = Math.floor((v - minVal) / bucketSize);
        if (v < bucketMin[idx]) bucketMin[idx] = v;
        if (v > bucketMax[idx]) bucketMax[idx] = v;
    }

    let prevMax = minVal;
    let maxGap = 0;
    for (let i = 0; i < bucketCount; i++) {
        if (bucketMin[i] === Infinity) continue; // empty bucket
        const gap = bucketMin[i] - prevMax;
        if (gap > maxGap) maxGap = gap;
        prevMax = bucketMax[i];
    }

    return maxGap;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumGap($nums) {
        $n = count($nums);
        if ($n < 2) {
            return 0;
        }

        $minVal = PHP_INT_MAX;
        $maxVal = PHP_INT_MIN;
        foreach ($nums as $v) {
            if ($v < $minVal) $minVal = $v;
            if ($v > $maxVal) $maxVal = $v;
        }

        if ($minVal == $maxVal) {
            return 0;
        }

        $bucketSize = max(1, intdiv($maxVal - $minVal, $n - 1));
        $bucketCount = intdiv($maxVal - $minVal, $bucketSize) + 1;

        $bucketMin = array_fill(0, $bucketCount, PHP_INT_MAX);
        $bucketMax = array_fill(0, $bucketCount, PHP_INT_MIN);
        $bucketUsed = array_fill(0, $bucketCount, false);

        foreach ($nums as $v) {
            $idx = intdiv($v - $minVal, $bucketSize);
            if (!$bucketUsed[$idx]) {
                $bucketMin[$idx] = $v;
                $bucketMax[$idx] = $v;
                $bucketUsed[$idx] = true;
            } else {
                if ($v < $bucketMin[$idx]) $bucketMin[$idx] = $v;
                if ($v > $bucketMax[$idx]) $bucketMax[$idx] = $v;
            }
        }

        $prevMax = $minVal;
        $maxGap = 0;
        for ($i = 0; $i < $bucketCount; $i++) {
            if (!$bucketUsed[$i]) continue;
            $gap = $bucketMin[$i] - $prevMax;
            if ($gap > $maxGap) $maxGap = $gap;
            $prevMax = $bucketMax[$i];
        }

        return $maxGap;
    }
}
```

## Swift

```swift
class Solution {
    func maximumGap(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 2 { return 0 }
        
        var minVal = nums[0]
        var maxVal = nums[0]
        for v in nums {
            if v < minVal { minVal = v }
            if v > maxVal { maxVal = v }
        }
        if minVal == maxVal { return 0 }
        
        // Minimum possible maximum gap (ceil division)
        let gap = max(1, (maxVal - minVal + n - 2) / (n - 1))
        let bucketCount = (maxVal - minVal) / gap + 1
        
        var bucketMin = Array(repeating: Int.max, count: bucketCount)
        var bucketMax = Array(repeating: Int.min, count: bucketCount)
        
        for v in nums {
            let idx = (v - minVal) / gap
            if v < bucketMin[idx] { bucketMin[idx] = v }
            if v > bucketMax[idx] { bucketMax[idx] = v }
        }
        
        var prevMax = minVal
        var maxGap = 0
        
        for i in 0..<bucketCount {
            if bucketMin[i] == Int.max && bucketMax[i] == Int.min {
                continue // empty bucket
            }
            let currentGap = bucketMin[i] - prevMax
            if currentGap > maxGap { maxGap = currentGap }
            prevMax = bucketMax[i]
        }
        
        return maxGap
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumGap(nums: IntArray): Int {
        val n = nums.size
        if (n < 2) return 0
        var minVal = Int.MAX_VALUE
        var maxVal = Int.MIN_VALUE
        for (v in nums) {
            if (v < minVal) minVal = v
            if (v > maxVal) maxVal = v
        }
        if (minVal == maxVal) return 0
        val bucketSize = kotlin.math.max(1, ((maxVal - minVal) + n - 2) / (n - 1))
        val bucketCount = (maxVal - minVal) / bucketSize + 1
        val bucketMin = IntArray(bucketCount) { Int.MAX_VALUE }
        val bucketMax = IntArray(bucketCount) { Int.MIN_VALUE }
        val used = BooleanArray(bucketCount)
        for (v in nums) {
            val idx = (v - minVal) / bucketSize
            if (!used[idx]) {
                used[idx] = true
                bucketMin[idx] = v
                bucketMax[idx] = v
            } else {
                if (v < bucketMin[idx]) bucketMin[idx] = v
                if (v > bucketMax[idx]) bucketMax[idx] = v
            }
        }
        var prevMax = minVal
        var maxGap = 0
        for (i in 0 until bucketCount) {
            if (!used[i]) continue
            val curMin = bucketMin[i]
            maxGap = kotlin.math.max(maxGap, curMin - prevMax)
            prevMax = bucketMax[i]
        }
        return maxGap
    }
}
```

## Dart

```dart
class Solution {
  int maximumGap(List<int> nums) {
    int n = nums.length;
    if (n < 2) return 0;

    int minVal = nums[0];
    int maxVal = nums[0];
    for (int num in nums) {
      if (num < minVal) minVal = num;
      if (num > maxVal) maxVal = num;
    }
    if (minVal == maxVal) return 0;

    int bucketSize = ((maxVal - minVal) ~/ (n - 1));
    if (bucketSize == 0) bucketSize = 1;
    int bucketCount = ((maxVal - minVal) ~/ bucketSize) + 1;

    List<int> bucketMin = List.filled(bucketCount, 0);
    List<int> bucketMax = List.filled(bucketCount, 0);
    List<bool> used = List.filled(bucketCount, false);

    for (int num in nums) {
      int idx = ((num - minVal) ~/ bucketSize);
      if (!used[idx]) {
        bucketMin[idx] = num;
        bucketMax[idx] = num;
        used[idx] = true;
      } else {
        if (num < bucketMin[idx]) bucketMin[idx] = num;
        if (num > bucketMax[idx]) bucketMax[idx] = num;
      }
    }

    int prevMax = minVal;
    int maxGap = 0;
    for (int i = 0; i < bucketCount; ++i) {
      if (!used[i]) continue;
      int curMin = bucketMin[i];
      int gap = curMin - prevMax;
      if (gap > maxGap) maxGap = gap;
      prevMax = bucketMax[i];
    }
    return maxGap;
  }
}
```

## Golang

```go
func maximumGap(nums []int) int {
    n := len(nums)
    if n < 2 {
        return 0
    }
    minVal, maxVal := nums[0], nums[0]
    for _, v := range nums[1:] {
        if v < minVal {
            minVal = v
        }
        if v > maxVal {
            maxVal = v
        }
    }
    if minVal == maxVal {
        return 0
    }

    bucketSize := (maxVal - minVal) / (n - 1)
    if bucketSize == 0 {
        bucketSize = 1
    }
    bucketCount := (maxVal-minVal)/bucketSize + 1

    type bucket struct {
        used bool
        min  int
        max  int
    }
    buckets := make([]bucket, bucketCount)

    for _, v := range nums {
        idx := (v - minVal) / bucketSize
        b := &buckets[idx]
        if !b.used {
            b.used = true
            b.min = v
            b.max = v
        } else {
            if v < b.min {
                b.min = v
            }
            if v > b.max {
                b.max = v
            }
        }
    }

    maxGap := 0
    prevMaxSet := false
    var prevMax int

    for _, b := range buckets {
        if !b.used {
            continue
        }
        if !prevMaxSet {
            prevMax = b.max
            prevMaxSet = true
            continue
        }
        gap := b.min - prevMax
        if gap > maxGap {
            maxGap = gap
        }
        prevMax = b.max
    }

    return maxGap
}
```

## Ruby

```ruby
def maximum_gap(nums)
  n = nums.length
  return 0 if n < 2

  min_val = nums.min
  max_val = nums.max
  return 0 if min_val == max_val

  bucket_size = [(max_val - min_val) / (n - 1), 1].max
  bucket_count = ((max_val - min_val) / bucket_size) + 1

  bucket_min = Array.new(bucket_count)
  bucket_max = Array.new(bucket_count)

  nums.each do |num|
    idx = (num - min_val) / bucket_size
    if bucket_min[idx].nil?
      bucket_min[idx] = num
      bucket_max[idx] = num
    else
      bucket_min[idx] = [bucket_min[idx], num].min
      bucket_max[idx] = [bucket_max[idx], num].max
    end
  end

  prev_max = nil
  max_gap = 0
  bucket_min.each_with_index do |bmin, i|
    next if bmin.nil?
    unless prev_max.nil?
      gap = bmin - prev_max
      max_gap = [max_gap, gap].max
    end
    prev_max = bucket_max[i]
  end

  max_gap
end
```

## Scala

```scala
object Solution {
    def maximumGap(nums: Array[Int]): Int = {
        val n = nums.length
        if (n < 2) return 0

        var minVal = Int.MaxValue
        var maxVal = Int.MinValue
        for (v <- nums) {
            if (v < minVal) minVal = v
            if (v > maxVal) maxVal = v
        }
        if (minVal == maxVal) return 0

        val bucketSize = Math.max(1, ((maxVal - minVal).toLong / (n - 1)).toInt)
        val bucketCount = ((maxVal - minVal).toLong / bucketSize + 1).toInt

        val bucketMin = Array.fill(bucketCount)(Int.MaxValue)
        val bucketMax = Array.fill(bucketCount)(Int.MinValue)
        val used = Array.fill(bucketCount)(false)

        for (v <- nums) {
            val idx = ((v - minVal).toLong / bucketSize).toInt
            if (!used(idx)) {
                bucketMin(idx) = v
                bucketMax(idx) = v
                used(idx) = true
            } else {
                if (v < bucketMin(idx)) bucketMin(idx) = v
                if (v > bucketMax(idx)) bucketMax(idx) = v
            }
        }

        var prevMax = minVal
        var maxGap = 0
        for (i <- 0 until bucketCount) {
            if (used(i)) {
                val gap = bucketMin(i) - prevMax
                if (gap > maxGap) maxGap = gap
                prevMax = bucketMax(i)
            }
        }
        maxGap
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_gap(nums: Vec<i32>) -> i32 {
        let len = nums.len();
        if len < 2 {
            return 0;
        }
        // Find global min and max
        let mut min_val = nums[0];
        let mut max_val = nums[0];
        for &v in &nums[1..] {
            if v < min_val {
                min_val = v;
            }
            if v > max_val {
                max_val = v;
            }
        }
        if min_val == max_val {
            return 0;
        }

        let n = len as i64;
        // Bucket size (ceil division)
        let mut bucket_size = ((max_val - min_val) as i64 + n - 2) / (n - 1);
        if bucket_size == 0 {
            bucket_size = 1;
        }
        // Number of buckets
        let bucket_count = ((max_val - min_val) as i64 / bucket_size) + 1;
        let bucket_count = bucket_count as usize;

        let mut bucket_min: Vec<i32> = vec![i32::MAX; bucket_count];
        let mut bucket_max: Vec<i32> = vec![i32::MIN; bucket_count];
        let mut used: Vec<bool> = vec![false; bucket_count];

        // Distribute numbers into buckets
        for &v in &nums {
            let idx = ((v - min_val) as i64 / bucket_size) as usize;
            if !used[idx] {
                bucket_min[idx] = v;
                bucket_max[idx] = v;
                used[idx] = true;
            } else {
                if v < bucket_min[idx] {
                    bucket_min[idx] = v;
                }
                if v > bucket_max[idx] {
                    bucket_max[idx] = v;
                }
            }
        }

        // Scan buckets to find maximum gap
        let mut prev_max = min_val;
        let mut max_gap = 0i32;
        for i in 0..bucket_count {
            if !used[i] {
                continue;
            }
            let gap = bucket_min[i] - prev_max;
            if gap > max_gap {
                max_gap = gap;
            }
            prev_max = bucket_max[i];
        }

        max_gap
    }
}
```

## Racket

```racket
(define (ceil-div a b)
  (quotient (+ a (- b 1)) b))

(define/contract (maximum-gap nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((n (length nums)))
    (if (< n 2)
        0
        (let* ((min-val (apply min nums))
               (max-val (apply max nums)))
          (if (= min-val max-val)
              0
              (let* ((diff (- max-val min-val))
                     (bucket-size (max 1 (ceil-div diff (- n 1))))
                     (bucket-count (+ (quotient diff bucket-size) 1))
                     (mins (make-vector bucket-count #f))
                     (maxs (make-vector bucket-count #f)))
                ;; distribute numbers into buckets
                (for ([x nums])
                  (let* ((idx (quotient (- x min-val) bucket-size))
                         (cur-min (vector-ref mins idx))
                         (cur-max (vector-ref maxs idx)))
                    (if cur-min
                        (begin
                          (when (< x cur-min) (vector-set! mins idx x))
                          (when (> x cur-max) (vector-set! maxs idx x)))
                        (begin
                          (vector-set! mins idx x)
                          (vector-set! maxs idx x)))))
                ;; compute maximum gap
                (let loop ((i 0) (prev min-val) (ans 0))
                  (if (= i bucket-count)
                      ans
                      (let ((bmin (vector-ref mins i))
                            (bmax (vector-ref maxs i)))
                        (if bmin
                            (loop (+ i 1) bmax (max ans (- bmin prev)))
                            (loop (+ i 1) prev ans)))))))))))
```

## Erlang

```erlang
-spec maximum_gap(Nums :: [integer()]) -> integer().
maximum_gap(Nums) ->
    case length(Nums) of
        N when N < 2 -> 0;
        N ->
            {Min, Max} = find_min_max(Nums),
            if Min == Max -> 0;
               true ->
                BucketSizeFloat = (Max - Min) / (N - 1),
                BucketSize0 = trunc(math:ceil(BucketSizeFloat)),
                BucketSize = erlang:max(1, BucketSize0),
                BucketCount = N - 1,
                Buckets = fill_buckets(Nums, Min, Max, BucketSize, BucketCount, #{}),
                compute_max_gap(Buckets, Min, Max, BucketCount)
            end
    end.

find_min_max([H|T]) ->
    lists:foldl(fun(X,{Mi,Ma}) -> {erlang:min(Mi,X), erlang:max(Ma,X)} end,
                {H,H}, T).

fill_buckets([], _Min, _Max, _Size, _Count, Buckets) ->
    Buckets;
fill_buckets([X|Rest], Min, Max, Size, Count, Buckets) ->
    if X =:= Min; X =:= Max ->
            fill_buckets(Rest, Min, Max, Size, Count, Buckets);
       true ->
            Idx0 = (X - Min) div Size,
            Idx = if Idx0 >= Count -> Count-1; true -> Idx0 end,
            case maps:find(Idx, Buckets) of
                {ok,{BMin,BMax}} ->
                    NewMin = erlang:min(BMin,X),
                    NewMax = erlang:max(BMax,X),
                    NewBuckets = maps:put(Idx,{NewMin,NewMax},Buckets);
                error ->
                    NewBuckets = maps:put(Idx,{X,X},Buckets)
            end,
            fill_buckets(Rest, Min, Max, Size, Count, NewBuckets)
    end.

compute_max_gap(Buckets, Min, Max, Count) ->
    compute_max_gap_loop(0, Count, Buckets, Min, 0, Max).

compute_max_gap_loop(Index, Count, _Buckets, PrevMax, MaxGap, Max) when Index >= Count ->
    erlang:max(MaxGap, Max - PrevMax);
compute_max_gap_loop(Index, Count, Buckets, PrevMax, MaxGap, Max) ->
    case maps:find(Index, Buckets) of
        {ok,{BMin,BMax}} ->
            Gap = BMin - PrevMax,
            NewMaxGap = erlang:max(MaxGap, Gap),
            compute_max_gap_loop(Index+1, Count, Buckets, BMax, NewMaxGap, Max);
        error ->
            compute_max_gap_loop(Index+1, Count, Buckets, PrevMax, MaxGap, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_gap(nums :: [integer]) :: integer
  def maximum_gap(nums) do
    n = length(nums)

    if n < 2 do
      0
    else
      min_val = Enum.min(nums)
      max_val = Enum.max(nums)

      if min_val == max_val do
        0
      else
        bucket_size =
          max(1, div(max_val - min_val + n - 2, n - 1))

        bucket_count = div(max_val - min_val, bucket_size) + 1

        mins = :array.new(bucket_count, default: nil)
        maxs = :array.new(bucket_count, default: nil)

        {mins, maxs} =
          Enum.reduce(nums, {mins, maxs}, fn num, {mins_acc, maxs_acc} ->
            idx = div(num - min_val, bucket_size)

            cur_min = :array.get(idx, mins_acc)
            mins_acc =
              if cur_min == nil or num < cur_min do
                :array.set(idx, num, mins_acc)
              else
                mins_acc
              end

            cur_max = :array.get(idx, maxs_acc)
            maxs_acc =
              if cur_max == nil or num > cur_max do
                :array.set(idx, num, maxs_acc)
              else
                maxs_acc
              end

            {mins_acc, maxs_acc}
          end)

        {max_gap, _} =
          Enum.reduce(0..(bucket_count - 1), {0, nil}, fn i, {gap, prev_max} ->
            cur_min = :array.get(i, mins)

            if cur_min == nil do
              {gap, prev_max}
            else
              cur_max = :array.get(i, maxs)
              new_gap =
                case prev_max do
                  nil -> 0
                  _ -> cur_min - prev_max
                end

              {if new_gap > gap, do: new_gap, else: gap}, cur_max
            end
          end)

        max_gap
      end
    end
  end
end
```

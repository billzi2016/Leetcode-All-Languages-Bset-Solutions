# 0327. Count of Range Sum

## Cpp

```cpp
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        function<long long(int,int)> sortCount = [&](int left, int right) -> long long {
            if (right - left <= 1) return 0;
            int mid = left + (right - left) / 2;
            long long cnt = sortCount(left, mid) + sortCount(mid, right);
            int j = mid, k = mid;
            for (int i = left; i < mid; ++i) {
                while (j < right && prefix[j] - prefix[i] < lower) ++j;
                while (k < right && prefix[k] - prefix[i] <= upper) ++k;
                cnt += k - j;
            }
            vector<long long> merged;
            merged.reserve(right - left);
            int p = left, q = mid;
            while (p < mid && q < right) {
                if (prefix[p] <= prefix[q]) merged.push_back(prefix[p++]);
                else merged.push_back(prefix[q++]);
            }
            while (p < mid) merged.push_back(prefix[p++]);
            while (q < right) merged.push_back(prefix[q++]);
            copy(merged.begin(), merged.end(), prefix.begin() + left);
            return cnt;
        };
        long long result = sortCount(0, n + 1);
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        int n = nums.length;
        long[] sums = new long[n + 1];
        for (int i = 0; i < n; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
        long[] temp = new long[n + 1];
        long count = mergeSort(sums, temp, 0, n + 1, lower, upper);
        return (int) count;
    }

    private long mergeSort(long[] sums, long[] temp, int left, int right, int lower, int upper) {
        if (right - left <= 1) {
            return 0L;
        }
        int mid = (left + right) >>> 1;
        long count = mergeSort(sums, temp, left, mid, lower, upper)
                   + mergeSort(sums, temp, mid, right, lower, upper);

        int j = mid, k = mid;
        for (int i = left; i < mid; i++) {
            while (k < right && sums[k] - sums[i] < lower) {
                k++;
            }
            while (j < right && sums[j] - sums[i] <= upper) {
                j++;
            }
            count += j - k;
        }

        int p = left, q = mid, t = left;
        while (p < mid && q < right) {
            if (sums[p] <= sums[q]) {
                temp[t++] = sums[p++];
            } else {
                temp[t++] = sums[q++];
            }
        }
        while (p < mid) {
            temp[t++] = sums[p++];
        }
        while (q < right) {
            temp[t++] = sums[q++];
        }
        System.arraycopy(temp, left, sums, left, right - left);
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # Prefix sums
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def sort_count(sums, left, right):
            if right - left <= 1:
                return 0
            mid = (left + right) // 2
            count = sort_count(sums, left, mid) + sort_count(sums, mid, right)

            # Count valid ranges across the two halves
            j = k = mid
            for i in range(left, mid):
                while k < right and sums[k] - sums[i] < lower:
                    k += 1
                while j < right and sums[j] - sums[i] <= upper:
                    j += 1
                count += j - k

            # Merge step
            merged = []
            p, q = left, mid
            while p < mid or q < right:
                if q >= right or (p < mid and sums[p] <= sums[q]):
                    merged.append(sums[p])
                    p += 1
                else:
                    merged.append(sums[q])
                    q += 1
            sums[left:right] = merged
            return count

        return sort_count(prefix, 0, len(prefix))
```

## Python3

```python
from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pref = [0]
        for x in nums:
            pref.append(pref[-1] + x)

        def sort(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            cnt = sort(lo, mid) + sort(mid, hi)
            j = k = mid
            for i in range(lo, mid):
                while j < hi and pref[j] - pref[i] < lower:
                    j += 1
                while k < hi and pref[k] - pref[i] <= upper:
                    k += 1
                cnt += k - j
            # merge step
            merged = []
            p, q = lo, mid
            while p < mid and q < hi:
                if pref[p] <= pref[q]:
                    merged.append(pref[p])
                    p += 1
                else:
                    merged.append(pref[q])
                    q += 1
            if p < mid:
                merged.extend(pref[p:mid])
            if q < hi:
                merged.extend(pref[q:hi])
            pref[lo:hi] = merged
            return cnt

        return sort(0, len(pref))
```

## C

```c
#include <stdlib.h>

static long long mergeCount(long long *sum, int left, int right,
                            long long lower, long long upper, long long *temp) {
    if (left >= right) return 0;
    int mid = left + (right - left) / 2;
    long long cnt = 0;
    cnt += mergeCount(sum, left, mid, lower, upper, temp);
    cnt += mergeCount(sum, mid + 1, right, lower, upper, temp);

    int j = mid + 1, k = mid + 1;
    for (int i = left; i <= mid; ++i) {
        while (j <= right && sum[j] - sum[i] < lower) ++j;
        while (k <= right && sum[k] - sum[i] <= upper) ++k;
        cnt += (long long)(k - j);
    }

    int p = left, q = mid + 1, r = left;
    while (p <= mid && q <= right) {
        if (sum[p] <= sum[q]) temp[r++] = sum[p++];
        else temp[r++] = sum[q++];
    }
    while (p <= mid) temp[r++] = sum[p++];
    while (q <= right) temp[r++] = sum[q++];

    for (int i = left; i <= right; ++i) sum[i] = temp[i];
    return cnt;
}

int countRangeSum(int* nums, int numsSize, int lower, int upper) {
    int n = numsSize;
    long long *prefix = (long long *)malloc((n + 1) * sizeof(long long));
    if (!prefix) return 0;
    prefix[0] = 0;
    for (int i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + (long long)nums[i];
    }

    long long *temp = (long long *)malloc((n + 1) * sizeof(long long));
    if (!temp) {
        free(prefix);
        return 0;
    }

    long long result = mergeCount(prefix, 0, n, (long long)lower, (long long)upper, temp);

    free(prefix);
    free(temp);
    return (int)result;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountRangeSum(int[] nums, int lower, int upper)
    {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++)
            prefix[i + 1] = prefix[i] + nums[i];

        long[] temp = new long[prefix.Length];
        long result = MergeSort(prefix, 0, prefix.Length, lower, upper, temp);
        return (int)result;
    }

    private long MergeSort(long[] sum, int left, int right, int lower, int upper, long[] temp)
    {
        if (right - left <= 1) return 0;

        int mid = (left + right) >> 1;
        long count = MergeSort(sum, left, mid, lower, upper, temp) +
                     MergeSort(sum, mid, right, lower, upper, temp);

        int l = mid, r = mid;
        for (int i = left; i < mid; i++)
        {
            while (l < right && sum[l] - sum[i] < lower) l++;
            while (r < right && sum[r] - sum[i] <= upper) r++;
            count += r - l;
        }

        int p = left, q = mid, idx = left;
        while (p < mid && q < right)
        {
            if (sum[p] <= sum[q])
                temp[idx++] = sum[p++];
            else
                temp[idx++] = sum[q++];
        }
        while (p < mid) temp[idx++] = sum[p++];
        while (q < right) temp[idx++] = sum[q++];

        for (int i = left; i < right; i++)
            sum[i] = temp[i];

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var countRangeSum = function(nums, lower, upper) {
    const n = nums.length;
    const pref = new Array(n + 1);
    pref[0] = 0;
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }

    function sort(lo, hi) { // [lo, hi)
        if (hi - lo <= 1) return 0;
        const mid = Math.floor((lo + hi) / 2);
        let count = sort(lo, mid) + sort(mid, hi);

        let jLow = mid, jHigh = mid;
        for (let i = lo; i < mid; ++i) {
            while (jLow < hi && pref[jLow] - pref[i] < lower) jLow++;
            while (jHigh < hi && pref[jHigh] - pref[i] <= upper) jHigh++;
            count += jHigh - jLow;
        }

        // merge step
        const temp = [];
        let i = lo, k = mid;
        while (i < mid && k < hi) {
            if (pref[i] <= pref[k]) {
                temp.push(pref[i++]);
            } else {
                temp.push(pref[k++]);
            }
        }
        while (i < mid) temp.push(pref[i++]);
        while (k < hi) temp.push(pref[k++]);

        for (let idx = 0; idx < temp.length; ++idx) {
            pref[lo + idx] = temp[idx];
        }

        return count;
    }

    return sort(0, n + 1);
};
```

## Typescript

```typescript
function countRangeSum(nums: number[], lower: number, upper: number): number {
    const n = nums.length;
    const prefix = new Array<number>(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const temp = new Array<number>(n + 1);

    function sort(lo: number, hi: number): number {
        if (hi - lo <= 1) return 0;
        const mid = Math.floor((lo + hi) / 2);
        let count = sort(lo, mid) + sort(mid, hi);

        // Count cross sums
        let j = mid, k = mid;
        for (let i = lo; i < mid; i++) {
            const leftVal = prefix[i];
            while (j < hi && prefix[j] - leftVal < lower) j++;
            while (k < hi && prefix[k] - leftVal <= upper) k++;
            count += k - j;
        }

        // Merge step
        let p = lo, q = mid, t = lo;
        while (p < mid && q < hi) {
            if (prefix[p] <= prefix[q]) {
                temp[t++] = prefix[p++];
            } else {
                temp[t++] = prefix[q++];
            }
        }
        while (p < mid) temp[t++] = prefix[p++];
        while (q < hi) temp[t++] = prefix[q++];

        for (let i = lo; i < hi; i++) {
            prefix[i] = temp[i];
        }

        return count;
    }

    return sort(0, n + 1);
}
```

## Php

```php
class Solution {
    private $lower;
    private $upper;

    /**
     * @param Integer[] $nums
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function countRangeSum($nums, $lower, $upper) {
        $this->lower = $lower;
        $this->upper = $upper;
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        }
        return $this->sortCount($prefix, 0, $n);
    }

    private function sortCount(&$sums, $left, $right) {
        if ($right - $left <= 0) {
            return 0;
        }
        $mid = intdiv($left + $right, 2);
        $count = $this->sortCount($sums, $left, $mid) + $this->sortCount($sums, $mid + 1, $right);

        // count cross sums
        $j = $mid + 1;
        $k = $mid + 1;
        for ($i = $left; $i <= $mid; $i++) {
            while ($j <= $right && $sums[$j] - $sums[$i] < $this->lower) {
                $j++;
            }
            while ($k <= $right && $sums[$k] - $sums[$i] <= $this->upper) {
                $k++;
            }
            $count += $k - $j;
        }

        // merge step
        $temp = [];
        $p = $left;
        $q = $mid + 1;
        while ($p <= $mid && $q <= $right) {
            if ($sums[$p] <= $sums[$q]) {
                $temp[] = $sums[$p];
                $p++;
            } else {
                $temp[] = $sums[$q];
                $q++;
            }
        }
        while ($p <= $mid) {
            $temp[] = $sums[$p];
            $p++;
        }
        while ($q <= $right) {
            $temp[] = $sums[$q];
            $q++;
        }

        // copy back
        $len = count($temp);
        for ($i = 0; $i < $len; $i++) {
            $sums[$left + $i] = $temp[$i];
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countRangeSum(_ nums: [Int], _ lower: Int, _ upper: Int) -> Int {
        let n = nums.count
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(nums[i])
        }
        var sums = prefix
        let low = Int64(lower)
        let high = Int64(upper)

        func sortAndCount(_ start: Int, _ end: Int) -> Int {
            if end - start <= 1 { return 0 }
            let mid = (start + end) / 2
            var count = sortAndCount(start, mid)
            count += sortAndCount(mid, end)

            var j = mid, k = mid
            for i in start..<mid {
                while k < end && sums[k] - sums[i] < low { k += 1 }
                while j < end && sums[j] - sums[i] <= high { j += 1 }
                count += j - k
            }

            var merged = [Int64]()
            var p = start, q = mid
            while p < mid && q < end {
                if sums[p] <= sums[q] {
                    merged.append(sums[p])
                    p += 1
                } else {
                    merged.append(sums[q])
                    q += 1
                }
            }
            while p < mid { merged.append(sums[p]); p += 1 }
            while q < end { merged.append(sums[q]); q += 1 }

            for i in 0..<merged.count {
                sums[start + i] = merged[i]
            }
            return count
        }

        return sortAndCount(0, sums.count)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countRangeSum(nums: IntArray, lower: Int, upper: Int): Int {
        val n = nums.size
        val prefix = LongArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + nums[i].toLong()
        }
        val temp = LongArray(n + 1)
        val count = sortAndCount(prefix, temp, 0, n + 1, lower.toLong(), upper.toLong())
        return count.toInt()
    }

    private fun sortAndCount(arr: LongArray, temp: LongArray, left: Int, right: Int, lower: Long, upper: Long): Long {
        if (right - left <= 1) return 0L
        val mid = (left + right) ushr 1
        var count = sortAndCount(arr, temp, left, mid, lower, upper) +
                    sortAndCount(arr, temp, mid, right, lower, upper)

        var l = mid
        var r = mid
        for (i in left until mid) {
            while (l < right && arr[l] - arr[i] < lower) l++
            while (r < right && arr[r] - arr[i] <= upper) r++
            count += (r - l).toLong()
        }

        var i = left
        var j = mid
        var k = left
        while (i < mid && j < right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++]
            } else {
                temp[k++] = arr[j++]
            }
        }
        while (i < mid) temp[k++] = arr[i++]
        while (j < right) temp[k++] = arr[j++]

        for (p in left until right) {
            arr[p] = temp[p]
        }

        return count
    }
}
```

## Dart

```dart
class Solution {
  int countRangeSum(List<int> nums, int lower, int upper) {
    int n = nums.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + nums[i];
    }
    return _countWhileMergeSort(prefix, 0, n + 1, lower, upper);
  }

  int _countWhileMergeSort(List<int> sums, int left, int right, int lower, int upper) {
    if (right - left <= 1) return 0;
    int mid = (left + right) >> 1;
    int count = _countWhileMergeSort(sums, left, mid, lower, upper) +
                _countWhileMergeSort(sums, mid, right, lower, upper);

    int jLow = mid, jHigh = mid;
    for (int i = left; i < mid; ++i) {
      while (jLow < right && sums[jLow] - sums[i] < lower) jLow++;
      while (jHigh < right && sums[jHigh] - sums[i] <= upper) jHigh++;
      count += jHigh - jLow;
    }

    List<int> merged = [];
    int p = left, q = mid;
    while (p < mid && q < right) {
      if (sums[p] <= sums[q]) {
        merged.add(sums[p++]);
      } else {
        merged.add(sums[q++]);
      }
    }
    while (p < mid) merged.add(sums[p++]);
    while (q < right) merged.add(sums[q++]);

    for (int i = 0; i < merged.length; ++i) {
      sums[left + i] = merged[i];
    }

    return count;
  }
}
```

## Golang

```go
func countRangeSum(nums []int, lower int, upper int) int {
    n := len(nums)
    prefix := make([]int64, n+1)
    for i := 0; i < n; i++ {
        prefix[i+1] = prefix[i] + int64(nums[i])
    }
    loVal := int64(lower)
    hiVal := int64(upper)

    var sortAndCount func(lo, hi int) int64
    sortAndCount = func(lo, hi int) int64 {
        if hi-lo <= 1 {
            return 0
        }
        mid := (lo + hi) / 2
        cnt := sortAndCount(lo, mid) + sortAndCount(mid, hi)

        j, k := mid, mid
        for i := lo; i < mid; i++ {
            for j < hi && prefix[j]-prefix[i] < loVal {
                j++
            }
            for k < hi && prefix[k]-prefix[i] <= hiVal {
                k++
            }
            cnt += int64(k - j)
        }

        // merge step
        temp := make([]int64, 0, hi-lo)
        i, p := lo, mid
        for i < mid && p < hi {
            if prefix[i] < prefix[p] {
                temp = append(temp, prefix[i])
                i++
            } else {
                temp = append(temp, prefix[p])
                p++
            }
        }
        for i < mid {
            temp = append(temp, prefix[i])
            i++
        }
        for p < hi {
            temp = append(temp, prefix[p])
            p++
        }
        copy(prefix[lo:hi], temp)
        return cnt
    }

    result := sortAndCount(0, len(prefix))
    return int(result)
}
```

## Ruby

```ruby
def sort_and_count(pref, lo, hi, lower, upper)
  return 0 if hi - lo <= 1
  mid = (lo + hi) / 2
  cnt = sort_and_count(pref, lo, mid, lower, upper) + sort_and_count(pref, mid, hi, lower, upper)

  j = k = mid
  (lo...mid).each do |i|
    while k < hi && pref[k] - pref[i] < lower
      k += 1
    end
    while j < hi && pref[j] - pref[i] <= upper
      j += 1
    end
    cnt += j - k
  end

  temp = []
  i = lo
  r = mid
  while i < mid && r < hi
    if pref[i] <= pref[r]
      temp << pref[i]
      i += 1
    else
      temp << pref[r]
      r += 1
    end
  end
  while i < mid
    temp << pref[i]
    i += 1
  end
  while r < hi
    temp << pref[r]
    r += 1
  end

  pref[lo...hi] = temp
  cnt
end

# @param {Integer[]} nums
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def count_range_sum(nums, lower, upper)
  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each do |i|
    pref[i + 1] = pref[i] + nums[i]
  end
  sort_and_count(pref, 0, pref.size, lower, upper)
end
```

## Scala

```scala
object Solution {
    def countRangeSum(nums: Array[Int], lower: Int, upper: Int): Int = {
        val n = nums.length
        val prefix = new Array[Long](n + 1)
        var sum: Long = 0L
        for (i <- 0 until n) {
            sum += nums(i).toLong
            prefix(i + 1) = sum
        }
        val lowerL = lower.toLong
        val upperL = upper.toLong

        def sortCount(sums: Array[Long], left: Int, right: Int): Long = {
            if (right - left <= 1) return 0L
            val mid = (left + right) >>> 1
            var count = sortCount(sums, left, mid) + sortCount(sums, mid, right)

            var j = mid
            var k = mid
            for (i <- left until mid) {
                while (k < right && sums(k) - sums(i) < lowerL) k += 1
                while (j < right && sums(j) - sums(i) <= upperL) j += 1
                count += (j - k)
            }

            // merge step
            val temp = new Array[Long](right - left)
            var p = left
            var q = mid
            var t = 0
            while (p < mid && q < right) {
                if (sums(p) <= sums(q)) {
                    temp(t) = sums(p)
                    p += 1
                } else {
                    temp(t) = sums(q)
                    q += 1
                }
                t += 1
            }
            while (p < mid) {
                temp(t) = sums(p)
                p += 1
                t += 1
            }
            while (q < right) {
                temp(t) = sums(q)
                q += 1
                t += 1
            }
            System.arraycopy(temp, 0, sums, left, right - left)

            count
        }

        val result = sortCount(prefix, 0, prefix.length)
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_range_sum(nums: Vec<i32>, lower: i32, upper: i32) -> i32 {
        let mut prefix = Vec::with_capacity(nums.len() + 1);
        prefix.push(0i64);
        for &num in nums.iter() {
            let last = *prefix.last().unwrap();
            prefix.push(last + num as i64);
        }
        let cnt = Self::sort_and_count(&mut prefix[..], lower as i64, upper as i64);
        cnt as i32
    }

    fn sort_and_count(sums: &mut [i64], lower: i64, upper: i64) -> i64 {
        let n = sums.len();
        if n <= 1 {
            return 0;
        }
        let mid = n / 2;
        let (left, right) = sums.split_at_mut(mid);
        let mut count = Self::sort_and_count(left, lower, upper)
            + Self::sort_and_count(right, lower, upper);

        // Count cross pairs
        let mut j = 0usize;
        let mut k = 0usize;
        for &l in left.iter() {
            while k < right.len() && right[k] - l < lower {
                k += 1;
            }
            while j < right.len() && right[j] - l <= upper {
                j += 1;
            }
            count += (j - k) as i64;
        }

        // Merge left and right into a sorted slice
        let mut merged = Vec::with_capacity(n);
        let (mut i, mut p) = (0usize, 0usize);
        while i < left.len() && p < right.len() {
            if left[i] <= right[p] {
                merged.push(left[i]);
                i += 1;
            } else {
                merged.push(right[p]);
                p += 1;
            }
        }
        if i < left.len() {
            merged.extend_from_slice(&left[i..]);
        }
        if p < right.len() {
            merged.extend_from_slice(&right[p..]);
        }

        sums.copy_from_slice(&merged);
        count
    }
}
```

## Racket

```racket
(define/contract (count-range-sum nums lower upper)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length nums))
         ;; prefix sums vector of length n+1
         (pref (make-vector (+ n 1) 0)))
    (let loop ((i 0) (lst nums) (s 0))
      (if (null? lst)
          (void)
          (let ((new-s (+ s (car lst))))
            (vector-set! pref (add1 i) new-s)
            (loop (add1 i) (cdr lst) new-s))))
    ;; collect all prefix sums
    (define all-values
      (for/list ([i (in-range 0 (+ n 1))])
        (vector-ref pref i)))
    ;; sort and deduplicate
    (define sorted-vals
      (let* ((sorted (sort all-values <)))
        (let loop ((lst sorted) (prev #f) (out '()))
          (cond [(null? lst) (reverse out)]
                [else (let ((x (car lst)))
                        (if (and prev (= x prev))
                            (loop (cdr lst) prev out)
                            (loop (cdr lst) x (cons x out))))]))))
    (define vals-vec (list->vector sorted-vals))
    (define size (vector-length vals-vec))
    ;; Fenwick tree
    (define bit (make-vector (+ size 1) 0))
    (define (lowbit x) (bitwise-and x (- x)))
    (define (bit-add! idx val)
      (let loop ((i idx))
        (when (< i (vector-length bit))
          (vector-set! bit i (+ (vector-ref bit i) val))
          (loop (+ i (lowbit i))))))
    (define (bit-sum idx)
      (let loop ((i idx) (res 0))
        (if (= i 0)
            res
            (loop (bitwise-and i (- i)) (+ res (vector-ref bit i))))))
    ;; binary searches on vals-vec
    (define (lower-bound target)
      (let loop ((lo 0) (hi size))
        (if (= lo hi)
            lo
            (let* ((mid (+ lo (quotient (- hi lo) 2))))
              (if (< (vector-ref vals-vec mid) target)
                  (loop (add1 mid) hi)
                  (loop lo mid))))))
    (define (upper-bound target)
      (let loop ((lo 0) (hi size))
        (if (= lo hi)
            (- lo 1)
            (let* ((mid (+ lo (quotient (- hi lo) 2))))
              (if (<= (vector-ref vals-vec mid) target)
                  (loop (add1 mid) hi)
                  (loop lo mid))))))
    ;; main iteration
    (let loop ((i 0) (cnt 0))
      (if (= i (+ n 1))
          cnt
          (let* ((cur (vector-ref pref i))
                 (left (- cur upper))
                 (right (- cur lower))
                 (lIdx (lower-bound left))
                 (rIdx (upper-bound right))
                 (add-count (if (<= lIdx rIdx)
                                (- (bit-sum (+ rIdx 1)) (bit-sum lIdx))
                                0)))
            ;; insert current prefix sum into BIT
            (let ((pos (lower-bound cur))) ; exact position exists
              (bit-add! (+ pos 1) 1)
              (loop (add1 i) (+ cnt add-count))))))))
```

## Erlang

```erlang
-spec count_range_sum([integer()], integer(), integer()) -> integer().
count_range_sum(Nums, Lower, Upper) ->
    Prefix = prefix_sums(Nums),
    AllVals = Prefix ++ [P - Lower || P <- Prefix] ++ [P - Upper || P <- Prefix],
    Sorted = lists:usort(AllVals),
    Map = maps:from_list(lists:zip(Sorted, lists:seq(1, length(Sorted)))),
    Size = length(Sorted),
    Tree0 = array:new(Size + 1, {default, 0}),
    {Ans, _} =
        lists:foldl(
            fun(P, {Acc, Tree}) ->
                IdxLow = maps:get(P - Upper, Map),
                IdxHigh = maps:get(P - Lower, Map),
                CountInRange =
                    bit_query(IdxHigh, Tree) -
                        (if IdxLow > 1 -> bit_query(IdxLow - 1, Tree); true -> 0 end),
                IdxCur = maps:get(P, Map),
                NewTree = bit_add(IdxCur, 1, Size, Tree),
                {Acc + CountInRange, NewTree}
            end,
            {0, Tree0},
            Prefix
        ),
    Ans.

%% Helper to compute prefix sums including initial 0.
prefix_sums(Nums) ->
    prefix_sums(Nums, 0, [0]).

prefix_sums([], _Sum, Acc) -> lists:reverse(Acc);
prefix_sums([H | T], Sum, Acc) ->
    NewSum = Sum + H,
    prefix_sums(T, NewSum, [NewSum | Acc]).

%% BIT add operation.
bit_add(Index, Delta, Size, Tree) when Index =< Size ->
    Old = array:get(Index, Tree),
    NewTree = array:set(Index, Old + Delta, Tree),
    Next = Index + (Index band -Index),
    bit_add(Next, Delta, Size, NewTree);
bit_add(_, _, _, Tree) -> Tree.

%% BIT prefix sum query.
bit_query(0, _) -> 0;
bit_query(Index, Tree) ->
    Val = array:get(Index, Tree),
    Prev = Index - (Index band -Index),
    bit_query(Prev, Tree) + Val.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_range_sum(nums :: [integer], lower :: integer, upper :: integer) :: integer
  def count_range_sum(nums, lower, upper) do
    pref = build_prefix(nums)

    all_vals =
      Enum.flat_map(pref, fn s ->
        [s, s - lower, s - upper]
      end)

    uniq_sorted = all_vals |> Enum.uniq() |> Enum.sort()
    idx_map = Map.new(Enum.with_index(uniq_sorted, 1), fn {v, i} -> {v, i} end)
    size = map_size(idx_map) + 2
    bit = :array.new(size, default: 0)

    {_final_bit, result} =
      Enum.reduce(pref, {bit, 0}, fn s, {bit_acc, cnt} ->
        left_idx = Map.get(idx_map, s - upper)
        right_idx = Map.get(idx_map, s - lower)

        sum_right = bit_sum(bit_acc, right_idx)
        sum_left = if left_idx > 1, do: bit_sum(bit_acc, left_idx - 1), else: 0

        cnt2 = cnt + (sum_right - sum_left)

        idx_s = Map.get(idx_map, s)
        bit_new = bit_add(bit_acc, idx_s, 1)

        {bit_new, cnt2}
      end)

    result
  end

  defp build_prefix(nums) do
    {list_rev, _} =
      Enum.reduce(nums, {[0], 0}, fn x, {lst, cur} ->
        new = cur + x
        {[new | lst], new}
      end)

    Enum.reverse(list_rev)
  end

  defp bit_add(bit, idx, delta) do
    size = :array.size(bit)

    if idx < size do
      current = :array.get(idx, bit)
      bit = :array.set(idx, current + delta, bit)
      next_idx = idx + (idx &&& -idx)
      bit_add(bit, next_idx, delta)
    else
      bit
    end
  end

  defp bit_sum(bit, idx) when idx > 0 do
    current = :array.get(idx, bit)
    current + bit_sum(bit, idx - (idx &&& -idx))
  end

  defp bit_sum(_bit, _idx), do: 0
end
```

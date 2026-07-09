# 3134. Find the Median of the Uniqueness Array

## Cpp

```cpp
class Solution {
public:
    int medianOfUniquenessArray(std::vector<int>& nums) {
        int n = nums.size();
        long long totalSub = 1LL * n * (n + 1) / 2;
        long long need = totalSub / 2 + 1; // we need at least this many subarrays <= answer
        
        int maxVal = 0;
        for (int v : nums) if (v > maxVal) maxVal = v;
        
        // count distinct elements in whole array to set upper bound
        std::vector<int> seen(maxVal + 1, 0);
        int overallDistinct = 0;
        for (int v : nums) {
            if (!seen[v]) {
                seen[v] = 1;
                ++overallDistinct;
            }
        }
        
        auto countLE = [&](int limit) -> long long {
            std::vector<int> freq(maxVal + 1, 0);
            int distinct = 0;
            long long cnt = 0;
            int left = 0;
            for (int right = 0; right < n; ++right) {
                if (++freq[nums[right]] == 1) ++distinct;
                while (distinct > limit) {
                    if (--freq[nums[left]] == 0) --distinct;
                    ++left;
                }
                cnt += (right - left + 1);
            }
            return cnt;
        };
        
        int lo = 1, hi = overallDistinct; // answer lies between 1 and total distinct elements
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (countLE(mid) >= need)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int medianOfUniquenessArray(int[] nums) {
        int n = nums.length;
        long totalSubarrays = (long) n * (n + 1) / 2;
        long need = (totalSubarrays + 1) / 2; // rank of the median (lower middle)

        int maxVal = 0;
        for (int v : nums) {
            if (v > maxVal) maxVal = v;
        }

        int low = 1, high = n;
        while (low < high) {
            int mid = (low + high) >>> 1;
            long cnt = countAtMost(nums, mid, maxVal);
            if (cnt >= need) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private static long countAtMost(int[] nums, int k, int maxVal) {
        int n = nums.length;
        int[] freq = new int[maxVal + 1];
        int distinct = 0;
        long cnt = 0;
        int r = 0;

        for (int l = 0; l < n; ++l) {
            while (r < n && distinct + (freq[nums[r]] == 0 ? 1 : 0) <= k) {
                if (freq[nums[r]] == 0) distinct++;
                freq[nums[r]]++;
                r++;
            }
            cnt += r - l;

            // move left pointer
            freq[nums[l]]--;
            if (freq[nums[l]] == 0) distinct--;
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def medianOfUniquenessArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) // 2
        need = (total + 1) // 2  # number of subarrays needed to reach median position

        def count_at_most(k):
            freq = {}
            distinct = 0
            res = 0
            r = 0
            for l in range(n):
                while r < n:
                    val = nums[r]
                    inc = 1 if freq.get(val, 0) == 0 else 0
                    if distinct + inc > k:
                        break
                    freq[val] = freq.get(val, 0) + 1
                    distinct += inc
                    r += 1
                res += r - l
                left_val = nums[l]
                freq[left_val] -= 1
                if freq[left_val] == 0:
                    distinct -= 1
            return res

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if count_at_most(mid) >= need:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
from typing import List

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_subarrays = n * (n + 1) // 2
        need = (total_subarrays + 1) // 2  # kth smallest where k = need

        def count_at_most(limit: int) -> int:
            if limit == 0:
                return 0
            freq = {}
            left = 0
            distinct = 0
            cnt = 0
            for right, val in enumerate(nums):
                cur = freq.get(val, 0)
                if cur == 0:
                    distinct += 1
                freq[val] = cur + 1

                while distinct > limit:
                    v = nums[left]
                    freq[v] -= 1
                    if freq[v] == 0:
                        distinct -= 1
                        del freq[v]
                    left += 1

                cnt += right - left + 1
            return cnt

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if count_at_most(mid) >= need:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int *freq = NULL;
static int freqSize = 0;

static long long countLE(int *nums, int n, int limit) {
    memset(freq, 0, freqSize * sizeof(int));
    int distinct = 0;
    long long total = 0;
    int left = 0;
    for (int right = 0; right < n; ++right) {
        if (++freq[nums[right]] == 1) distinct++;
        while (distinct > limit) {
            if (--freq[nums[left]] == 0) distinct--;
            ++left;
        }
        total += (right - left + 1);
    }
    return total;
}

int medianOfUniquenessArray(int* nums, int numsSize) {
    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];
    freqSize = maxVal + 1;
    freq = (int *)malloc(freqSize * sizeof(int));

    long long totalSub = (long long)numsSize * (numsSize + 1) / 2;
    long long target = (totalSub + 1) / 2; // position of median (1‑based)

    int low = 1, high = numsSize, ans = numsSize;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        long long cnt = countLE(nums, numsSize, mid);
        if (cnt >= target) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    free(freq);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MedianOfUniquenessArray(int[] nums)
    {
        int n = nums.Length;
        long totalSubarrays = (long)n * (n + 1) / 2;
        long targetIdx = (totalSubarrays - 1) / 2; // zero‑based index of median
        long need = targetIdx + 1;                 // we need at least this many subarrays ≤ answer

        var distinctSet = new System.Collections.Generic.HashSet<int>(nums);
        int low = 1;
        int high = distinctSet.Count; // maximum possible distinct count in any subarray

        while (low < high)
        {
            int mid = low + (high - low) / 2;
            long cnt = CountAtMost(nums, mid);
            if (cnt >= need)
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }

    private long CountAtMost(int[] nums, int k)
    {
        if (k == 0) return 0;

        var freq = new System.Collections.Generic.Dictionary<int, int>();
        int distinct = 0;
        long res = 0;
        int left = 0;

        for (int right = 0; right < nums.Length; ++right)
        {
            int val = nums[right];
            if (!freq.TryGetValue(val, out int cur))
                cur = 0;
            if (cur == 0) distinct++;
            freq[val] = cur + 1;

            while (distinct > k)
            {
                int lval = nums[left++];
                int cntL = freq[lval];
                if (cntL == 1)
                {
                    distinct--;
                    freq.Remove(lval);
                }
                else
                {
                    freq[lval] = cntL - 1;
                }
            }

            res += right - left + 1;
        }

        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var medianOfUniquenessArray = function(nums) {
    const n = nums.length;
    const totalSubarrays = n * (n + 1) / 2;
    const need = Math.floor((totalSubarrays + 1) / 2); // kth smallest (1-indexed)

    const countLeq = (limit) => {
        let freq = new Map();
        let distinct = 0;
        let left = 0;
        let cnt = 0;
        for (let right = 0; right < n; ++right) {
            const val = nums[right];
            const cur = freq.get(val) || 0;
            if (cur === 0) distinct++;
            freq.set(val, cur + 1);
            while (distinct > limit) {
                const lv = nums[left];
                const lc = freq.get(lv);
                if (lc === 1) {
                    freq.delete(lv);
                    distinct--;
                } else {
                    freq.set(lv, lc - 1);
                }
                left++;
            }
            cnt += right - left + 1;
        }
        return cnt;
    };

    let low = 1, high = n;
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (countLeq(mid) >= need) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function medianOfUniquenessArray(nums: number[]): number {
    const n = nums.length;
    const totalSubarrays = (n * (n + 1)) >> 1; // n*(n+1)/2
    const need = Math.floor((totalSubarrays + 1) / 2); // ceil(total/2)

    const maxVal = Math.max(...nums);
    function countLe(limit: number): number {
        const freq = new Uint32Array(maxVal + 1);
        let distinct = 0;
        let right = 0;
        let cnt = 0;
        for (let left = 0; left < n; left++) {
            while (right < n) {
                const v = nums[right];
                if (freq[v] === 0 && distinct + 1 > limit) break;
                if (freq[v] === 0) distinct++;
                freq[v]++;
                right++;
            }
            cnt += right - left;
            const lv = nums[left];
            freq[lv]--;
            if (freq[lv] === 0) distinct--;
        }
        return cnt;
    }

    let lo = 1, hi = n;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (countLe(mid) >= need) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function medianOfUniquenessArray($nums) {
        $n = count($nums);
        $total = intdiv($n * ($n + 1), 2); // total subarrays
        $need = intdiv($total + 1, 2);    // required count for median

        $low = 1;
        $high = $n; // maximum possible distinct count

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->countLE($nums, $mid) >= $need) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }

    /**
     * Count subarrays with distinct elements <= $limit
     *
     * @param Integer[] $arr
     * @param int $limit
     * @return int
     */
    private function countLE($arr, $limit) {
        $n = count($arr);
        $freq = [];
        $distinct = 0;
        $r = 0;
        $cnt = 0;

        for ($l = 0; $l < $n; $l++) {
            while ($r < $n) {
                $val = $arr[$r];
                $addDistinct = isset($freq[$val]) ? 0 : 1;
                if ($distinct + $addDistinct > $limit) {
                    break;
                }
                $freq[$val] = ($freq[$val] ?? 0) + 1;
                if ($freq[$val] == 1) {
                    $distinct++;
                }
                $r++;
            }

            $cnt += $r - $l;

            // remove left element
            $leftVal = $arr[$l];
            $freq[$leftVal]--;
            if ($freq[$leftVal] == 0) {
                $distinct--;
                unset($freq[$leftVal]);
            }
        }

        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func medianOfUniquenessArray(_ nums: [Int]) -> Int {
        let n = nums.count
        let total = Int64(n) * Int64(n + 1) / 2
        let target = (total - 1) / 2   // zero‑based index of the median
        
        let maxVal = nums.max() ?? 0
        
        var lo = 1
        var hi = n
        while lo < hi {
            let mid = (lo + hi) / 2
            let cnt = countAtMost(nums, mid, maxVal)
            if cnt >= target + 1 {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }
    
    private func countAtMost(_ nums: [Int], _ k: Int, _ maxVal: Int) -> Int64 {
        var freq = [Int](repeating: 0, count: maxVal + 1)
        var left = 0
        var distinct = 0
        var res: Int64 = 0
        
        for right in 0..<nums.count {
            let v = nums[right]
            if freq[v] == 0 { distinct += 1 }
            freq[v] += 1
            
            while distinct > k {
                let lv = nums[left]
                freq[lv] -= 1
                if freq[lv] == 0 { distinct -= 1 }
                left += 1
            }
            
            res += Int64(right - left + 1)
        }
        return res
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun medianOfUniquenessArray(nums: IntArray): Int {
        val n = nums.size
        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v

        val total = n.toLong() * (n + 1L) / 2L
        val need = (total + 1) / 2   // position of lower median

        var lo = 1
        var hi = n
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (countSubarrays(nums, mid, maxVal) >= need) {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }

    private fun countSubarrays(arr: IntArray, limit: Int, maxVal: Int): Long {
        val freq = IntArray(maxVal + 1)
        var distinct = 0
        var r = 0
        var cnt = 0L
        val n = arr.size

        for (l in 0 until n) {
            while (r < n) {
                val v = arr[r]
                val add = if (freq[v] == 0) 1 else 0
                if (distinct + add > limit) break
                if (add == 1) distinct++
                freq[v]++
                r++
            }
            cnt += (r - l).toLong()
            val vL = arr[l]
            freq[vL]--
            if (freq[vL] == 0) distinct--
        }
        return cnt
    }
}
```

## Dart

```dart
class Solution {
  int medianOfUniquenessArray(List<int> nums) {
    int n = nums.length;
    int maxVal = 0;
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }

    int totalSubarrays = n * (n + 1) ~/ 2;
    int rank = (totalSubarrays + 1) >> 1; // median position (lower middle)

    int countLE(int limit) {
      List<int> cnt = List.filled(maxVal + 1, 0);
      int distinct = 0;
      int r = 0;
      int total = 0;

      for (int l = 0; l < n; ++l) {
        while (r < n &&
            distinct + (cnt[nums[r]] == 0 ? 1 : 0) <= limit) {
          int v = nums[r];
          if (cnt[v] == 0) distinct++;
          cnt[v]++;
          r++;
        }
        total += (r - l);
        int leftVal = nums[l];
        cnt[leftVal]--;
        if (cnt[leftVal] == 0) distinct--;
      }
      return total;
    }

    int low = 1, high = n;
    while (low < high) {
      int mid = (low + high) >> 1;
      if (countLE(mid) >= rank) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func medianOfUniquenessArray(nums []int) int {
    n := len(nums)
    // maximum possible distinct count in any subarray is the number of unique elements overall
    uniqSet := make(map[int]struct{})
    maxVal := 0
    for _, v := range nums {
        uniqSet[v] = struct{}{}
        if v > maxVal {
            maxVal = v
        }
    }
    low, high := 1, len(uniqSet)

    total := int64(n) * (int64(n) + 1) / 2
    target := (total + 1) / 2 // position of the median (lower middle)

    for low < high {
        mid := (low + high) / 2
        if countSubarraysWithDistinctLE(nums, mid) >= target {
            high = mid
        } else {
            low = mid + 1
        }
    }
    return low
}

// counts subarrays whose number of distinct elements is <= limit
func countSubarraysWithDistinctLE(nums []int, limit int) int64 {
    freq := make(map[int]int)
    distinct := 0
    var cnt int64
    left := 0
    for right, v := range nums {
        if freq[v] == 0 {
            distinct++
        }
        freq[v]++

        for distinct > limit {
            lv := nums[left]
            freq[lv]--
            if freq[lv] == 0 {
                distinct--
                delete(freq, lv)
            }
            left++
        }
        cnt += int64(right - left + 1)
    }
    return cnt
}
```

## Ruby

```ruby
def median_of_uniqueness_array(nums)
  n = nums.length
  total = n * (n + 1) / 2
  k = (total + 1) / 2

  low = 1
  high = n
  ans = n
  while low <= high
    mid = (low + high) / 2
    cnt = count_subarrays_at_most(nums, mid)
    if cnt >= k
      ans = mid
      high = mid - 1
    else
      low = mid + 1
    end
  end
  ans
end

def count_subarrays_at_most(arr, limit)
  n = arr.length
  freq = Hash.new(0)
  distinct = 0
  right = 0
  cnt = 0
  (0...n).each do |left|
    while right < n && (distinct + (freq[arr[right]] == 0 ? 1 : 0)) <= limit
      if freq[arr[right]] == 0
        distinct += 1
      end
      freq[arr[right]] += 1
      right += 1
    end
    cnt += right - left
    freq[arr[left]] -= 1
    distinct -= 1 if freq[arr[left]] == 0
  end
  cnt
end
```

## Scala

```scala
object Solution {
    def medianOfUniquenessArray(nums: Array[Int]): Int = {
        val n = nums.length
        val totalSub = n.toLong * (n + 1) / 2
        val need = (totalSub + 1) / 2

        // number of distinct values in the whole array -> upper bound for answer
        var maxDistinct = 0
        {
            val seen = scala.collection.mutable.HashSet[Int]()
            for (v <- nums) {
                if (!seen.contains(v)) {
                    seen += v
                    maxDistinct += 1
                }
            }
        }

        val maxVal = nums.max

        // count subarrays whose distinct count <= limit
        def countLE(limit: Int): Long = {
            val freq = new Array[Int](maxVal + 1)
            var distinct = 0
            var left = 0
            var total: Long = 0L
            var right = 0
            while (right < n) {
                val v = nums(right)
                if (freq(v) == 0) distinct += 1
                freq(v) += 1
                while (distinct > limit) {
                    val lv = nums(left)
                    freq(lv) -= 1
                    if (freq(lv) == 0) distinct -= 1
                    left += 1
                }
                total += (right - left + 1).toLong
                right += 1
            }
            total
        }

        var lo = 1
        var hi = maxDistinct
        while (lo < hi) {
            val mid = (lo + hi) >>> 1
            if (countLE(mid) >= need) hi = mid else lo = mid + 1
        }
        lo
    }
}
```

## Rust

```rust
impl Solution {
    pub fn median_of_uniqueness_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let total_subarrays = (n as i64) * (n as i64 + 1) / 2;
        let target = (total_subarrays + 1) / 2; // rank of median (lower median)

        // maximum value in nums to size frequency array
        let mut max_val = 0i32;
        for &v in &nums {
            if v > max_val {
                max_val = v;
            }
        }
        let max_usize = max_val as usize;

        fn count_subarrays(nums: &[i32], limit: usize, max_usize: usize) -> i64 {
            let n = nums.len();
            let mut freq = vec![0usize; max_usize + 1];
            let mut distinct = 0usize;
            let mut r = 0usize;
            let mut cnt: i64 = 0;

            for l in 0..n {
                while r < n {
                    let val = nums[r] as usize;
                    let add = if freq[val] == 0 { 1 } else { 0 };
                    if distinct + add > limit {
                        break;
                    }
                    if freq[val] == 0 {
                        distinct += 1;
                    }
                    freq[val] += 1;
                    r += 1;
                }
                cnt += (r - l) as i64;

                // move left pointer
                let val_l = nums[l] as usize;
                freq[val_l] -= 1;
                if freq[val_l] == 0 {
                    distinct -= 1;
                }
            }
            cnt
        }

        let mut low = 1usize;
        let mut high = n; // maximum possible distinct count

        while low < high {
            let mid = (low + high) / 2;
            if count_subarrays(&nums, mid, max_usize) >= target {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        low as i32
    }
}
```

## Racket

```racket
(define/contract (median-of-uniqueness-array nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((nums-v (list->vector nums))
         (n (vector-length nums-v))
         (total (/ (* n (+ n 1)) 2))
         (k (quotient (+ total 1) 2))
         (maxv
          (let loop ((i 0) (mx 0))
            (if (= i n)
                mx
                (loop (+ i 1) (max mx (vector-ref nums-v i)))))))
    (define (count-at-most x)
      (let* ((freq (make-vector (+ maxv 1) 0))
             (distinct 0)
             (right -1)
             (total 0))
        (for ([left (in-range n)])
          ;; expand right while distinct <= x
          (let loop ()
            (when (< (+ right 1) n)
              (define val (vector-ref nums-v (+ right 1)))
              (define cnt (vector-ref freq val))
              (define new-distinct (+ distinct (if (= cnt 0) 1 0)))
              (when (<= new-distinct x)
                (set! right (+ right 1))
                (vector-set! freq val (+ cnt 1))
                (set! distinct new-distinct)
                (loop))))
          ;; add subarrays starting at left with distinct <= x
          (when (>= right left)
            (set! total (+ total (+ 1 (- right left)))))
          ;; shrink window from the left
          (when (<= left right)
            (define val (vector-ref nums-v left))
            (define cnt (vector-ref freq val))
            (vector-set! freq val (- cnt 1))
            (when (= cnt 1)
              (set! distinct (- distinct 1)))))
        total))
    ;; binary search for smallest x with count >= k
    (let loop ((lo 1) (hi n) (ans n))
      (if (> lo hi)
          ans
          (let* ((mid (quotient (+ lo hi) 2))
                 (cnt (count-at-most mid)))
            (if (>= cnt k)
                (loop lo (- mid 1) mid)
                (loop (+ mid 1) hi ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([median_of_uniqueness_array/1]).

-spec median_of_uniqueness_array(Nums :: [integer()]) -> integer().
median_of_uniqueness_array(Nums) ->
    N = length(Nums),
    K = ((N * (N + 1)) div 2 + 1) div 2,
    Tuple = list_to_tuple(Nums),
    binary_search(Tuple, N, K, 1, N).

binary_search(_Tuple, _N, _K, Lo, Hi) when Lo >= Hi ->
    Lo;
binary_search(Tuple, N, K, Lo, Hi) ->
    Mid = (Lo + Hi) div 2,
    Cnt = count_at_most(Tuple, N, Mid),
    if
        Cnt >= K -> binary_search(Tuple, N, K, Lo, Mid);
        true      -> binary_search(Tuple, N, K, Mid + 1, Hi)
    end.

count_at_most(Tuple, N, X) ->
    count_loop(Tuple, N, X, 0, 0, #{}, 0, 0).

%% count_loop(L,R,FreqMap,Distinct,Acc)
count_loop(_Tuple, N, _X, L, _R, _Freq, _Dist, Acc) when L >= N ->
    Acc;
count_loop(Tuple, N, X, L, R, Freq, Dist, Acc) ->
    {NewR, NewFreq, NewDist} = expand(R, Freq, Dist, Tuple, N, X),
    SubCnt = NewR - L,
    NewAcc = Acc + SubCnt,
    ValL = element(L + 1, Tuple),
    {FreqAfterRem, DistAfterRem} = decrement(ValL, NewFreq, NewDist),
    count_loop(Tuple, N, X, L + 1, NewR, FreqAfterRem, DistAfterRem, NewAcc).

%% expand right pointer while distinct <= X
expand(R, Freq, Dist, Tuple, N, X) when R < N ->
    Val = element(R + 1, Tuple),
    case maps:is_key(Val, Freq) of
        true ->
            UpdatedFreq = maps:update_with(Val, fun(C) -> C + 1 end, Freq),
            expand(R + 1, UpdatedFreq, Dist, Tuple, N, X);
        false ->
            if Dist + 1 =< X ->
                UpdatedFreq = maps:put(Val, 1, Freq),
                expand(R + 1, UpdatedFreq, Dist + 1, Tuple, N, X);
               true ->
                {R, Freq, Dist}
            end
    end;
expand(R, Freq, Dist, _Tuple, _N, _X) ->
    {R, Freq, Dist}.

decrement(Val, Freq, Dist) ->
    case maps:get(Val, Freq) of
        1 -> {maps:remove(Val, Freq), Dist - 1};
        C when C > 1 -> {maps:update_with(Val, fun(C0) -> C0 - 1 end, Freq), Dist}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec median_of_uniqueness_array(nums :: [integer]) :: integer
  def median_of_uniqueness_array(nums) do
    n = length(nums)
    arr = :array.from_list(nums)

    total = div(n * (n + 1), 2)
    k = div(total - 1, 2)

    binary_search(arr, n, k, 1, n)
  end

  defp binary_search(_arr, _n, _k, low, high) when low == high, do: low

  defp binary_search(arr, n, k, low, high) do
    mid = div(low + high, 2)
    cnt = count_at_most(arr, n, mid)

    if cnt > k do
      binary_search(arr, n, k, low, mid)
    else
      binary_search(arr, n, k, mid + 1, high)
    end
  end

  defp count_at_most(arr, n, limit) do
    {_, _, _, total} =
      Enum.reduce(0..(n - 1), {%{}, 0, 0, 0}, fn right, {freq, distinct, left, total} ->
        val = :array.get(right, arr)

        {freq1, distinct1} =
          case Map.get(freq, val) do
            nil -> {Map.put(freq, val, 1), distinct + 1}
            cnt -> {Map.put(freq, val, cnt + 1), distinct}
          end

        {freq2, distinct2, left2} = shrink_left(left, freq1, distinct1, limit, arr)
        total2 = total + (right - left2 + 1)

        {freq2, distinct2, left2, total2}
      end)

    total
  end

  defp shrink_left(left, freq, distinct, limit, arr) do
    if distinct <= limit do
      {freq, distinct, left}
    else
      val = :array.get(left, arr)
      cnt = Map.get(freq, val)

      freq2 =
        if cnt == 1 do
          Map.delete(freq, val)
        else
          Map.put(freq, val, cnt - 1)
        end

      distinct2 = if cnt == 1, do: distinct - 1, else: distinct
      shrink_left(left + 1, freq2, distinct2, limit, arr)
    end
  end
end
```

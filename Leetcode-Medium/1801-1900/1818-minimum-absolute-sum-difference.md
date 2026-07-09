# 1818. Minimum Absolute Sum Difference

## Cpp

```cpp
class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        const long long MOD = 1000000007LL;
        int n = nums1.size();
        vector<int> sorted = nums1;
        sort(sorted.begin(), sorted.end());
        
        long long total = 0;
        long long maxImprove = 0;
        for (int i = 0; i < n; ++i) {
            long long diff = llabs((long long)nums1[i] - nums2[i]);
            total += diff;
            // find best possible replacement for nums1[i]
            int target = nums2[i];
            auto it = lower_bound(sorted.begin(), sorted.end(), target);
            long long best = diff; // at least current diff
            if (it != sorted.end()) {
                best = min(best, llabs((long long)*it - target));
            }
            if (it != sorted.begin()) {
                --it;
                best = min(best, llabs((long long)*it - target));
            }
            long long improve = diff - best;
            if (improve > maxImprove) maxImprove = improve;
        }
        long long ans = (total - maxImprove) % MOD;
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int minAbsoluteSumDiff(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] sorted = nums1.clone();
        java.util.Arrays.sort(sorted);
        long total = 0;
        long maxGain = 0;
        for (int i = 0; i < n; i++) {
            int a = nums1[i];
            int b = nums2[i];
            long diff = Math.abs((long) a - b);
            total += diff;
            int idx = java.util.Arrays.binarySearch(sorted, b);
            if (idx < 0) idx = -idx - 1; // insertion point
            if (idx < n) {
                long newDiff = Math.abs((long) sorted[idx] - b);
                maxGain = Math.max(maxGain, diff - newDiff);
            }
            if (idx > 0) {
                long newDiff = Math.abs((long) sorted[idx - 1] - b);
                maxGain = Math.max(maxGain, diff - newDiff);
            }
        }
        long result = (total - maxGain) % MOD;
        if (result < 0) result += MOD;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        import bisect
        MOD = 10**9 + 7

        sorted_nums1 = sorted(nums1)
        total = 0
        max_gain = 0

        for a, b in zip(nums1, nums2):
            cur_diff = abs(a - b)
            total += cur_diff

            # find best possible diff using any element from nums1
            idx = bisect.bisect_left(sorted_nums1, b)

            best = cur_diff  # initialize with current diff
            if idx < len(sorted_nums1):
                best = min(best, abs(sorted_nums1[idx] - b))
            if idx > 0:
                best = min(best, abs(sorted_nums1[idx - 1] - b))

            gain = cur_diff - best
            if gain > max_gain:
                max_gain = gain

        result = (total - max_gain) % MOD
        return result
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        sorted_nums1 = sorted(nums1)
        total = 0
        max_gain = 0
        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            total += diff
            idx = bisect.bisect_left(sorted_nums1, b)
            if idx < len(sorted_nums1):
                new_diff = abs(sorted_nums1[idx] - b)
                gain = diff - new_diff
                if gain > max_gain:
                    max_gain = gain
            if idx > 0:
                new_diff = abs(sorted_nums1[idx - 1] - b)
                gain = diff - new_diff
                if gain > max_gain:
                    max_gain = gain
        return (total - max_gain) % MOD
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int minAbsoluteSumDiff(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    const int MOD = 1000000007;
    long long total = 0;
    long long maxReduce = 0;

    int *sorted = (int *)malloc(nums1Size * sizeof(int));
    for (int i = 0; i < nums1Size; ++i) sorted[i] = nums1[i];
    qsort(sorted, nums1Size, sizeof(int), cmp_int);

    for (int i = 0; i < nums1Size; ++i) {
        long long diff = nums1[i] > nums2[i] ? (long long)nums1[i] - nums2[i]
                                            : (long long)nums2[i] - nums1[i];
        total += diff;

        int target = nums2[i];
        int l = 0, r = nums1Size;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (sorted[m] >= target)
                r = m;
            else
                l = m + 1;
        }

        if (l < nums1Size) {
            long long newDiff = sorted[l] > target ? (long long)sorted[l] - target
                                                   : (long long)target - sorted[l];
            if (diff - newDiff > maxReduce) maxReduce = diff - newDiff;
        }
        if (l > 0) {
            int idx = l - 1;
            long long newDiff = sorted[idx] > target ? (long long)sorted[idx] - target
                                                     : (long long)target - sorted[idx];
            if (diff - newDiff > maxReduce) maxReduce = diff - newDiff;
        }
    }

    total %= MOD;
    long long result = (total - maxReduce) % MOD;
    if (result < 0) result += MOD;

    free(sorted);
    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    public int MinAbsoluteSumDiff(int[] nums1, int[] nums2) {
        const int MOD = 1000000007;
        int n = nums1.Length;
        long total = 0;
        var sorted = new List<int>(nums1);
        sorted.Sort();
        long maxImprove = 0;
        for (int i = 0; i < n; i++) {
            long diff = Math.Abs((long)nums1[i] - nums2[i]);
            total += diff;

            int target = nums2[i];
            int idx = sorted.BinarySearch(target);
            if (idx < 0) idx = ~idx;

            if (idx < n) {
                long newDiff = Math.Abs((long)sorted[idx] - target);
                maxImprove = Math.Max(maxImprove, diff - newDiff);
            }
            if (idx > 0) {
                long newDiff = Math.Abs((long)sorted[idx - 1] - target);
                maxImprove = Math.Max(maxImprove, diff - newDiff);
            }
        }

        long result = (total - maxImprove) % MOD;
        if (result < 0) result += MOD;
        return (int)result;
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
var minAbsoluteSumDiff = function(nums1, nums2) {
    const MOD = 1000000007;
    const n = nums1.length;
    // original sum and sorted copy of nums1 for binary search
    let total = 0;
    const sorted = Array.from(new Set(nums1)).sort((a,b)=>a-b); // dedup not required but fine
    // helper: lower bound index
    function lowerBound(arr, target) {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    }
    let maxImprove = 0;
    for (let i = 0; i < n; ++i) {
        const a = nums1[i];
        const b = nums2[i];
        const curDiff = Math.abs(a - b);
        total = (total + curDiff) % MOD;
        // find best possible diff using any element from nums1
        let idx = lowerBound(sorted, b);
        let bestDiff = curDiff; // at worst keep original
        if (idx < sorted.length) {
            bestDiff = Math.min(bestDiff, Math.abs(sorted[idx] - b));
        }
        if (idx > 0) {
            bestDiff = Math.min(bestDiff, Math.abs(sorted[idx-1] - b));
        }
        const improve = curDiff - bestDiff;
        if (improve > maxImprove) maxImprove = improve;
    }
    let result = (total - maxImprove) % MOD;
    if (result < 0) result += MOD;
    return result;
};
```

## Typescript

```typescript
function minAbsoluteSumDiff(nums1: number[], nums2: number[]): number {
    const MOD = 1_000_000_007;
    const n = nums1.length;
    const sorted = [...nums1].sort((a, b) => a - b);
    let total = 0;
    let maxReduce = 0;

    for (let i = 0; i < n; i++) {
        const a = nums1[i];
        const b = nums2[i];
        const diff = Math.abs(a - b);
        total += diff;

        // binary search lower bound for b in sorted
        let l = 0, r = sorted.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (sorted[m] < b) l = m + 1;
            else r = m;
        }

        let bestDiff = Infinity;
        if (l < sorted.length) bestDiff = Math.min(bestDiff, Math.abs(sorted[l] - b));
        if (l > 0) bestDiff = Math.min(bestDiff, Math.abs(sorted[l - 1] - b));

        const reduce = diff - bestDiff;
        if (reduce > maxReduce) maxReduce = reduce;
    }

    let result = total - maxReduce;
    result %= MOD;
    if (result < 0) result += MOD;
    return result;
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
    function minAbsoluteSumDiff($nums1, $nums2) {
        $mod = 1000000007;
        $n = count($nums1);
        $sorted = $nums1;
        sort($sorted); // ascending

        $origSum = 0;
        $maxReduction = 0;

        for ($i = 0; $i < $n; ++$i) {
            $a = $nums1[$i];
            $b = $nums2[$i];
            $diff = abs($a - $b);
            $origSum = ($origSum + $diff) % $mod;

            // binary search for closest value to $b in $sorted
            $l = 0;
            $r = $n - 1;
            while ($l <= $r) {
                $mid = intdiv($l + $r, 2);
                if ($sorted[$mid] == $b) {
                    $bestDiff = 0;
                    break;
                } elseif ($sorted[$mid] < $b) {
                    $l = $mid + 1;
                } else {
                    $r = $mid - 1;
                }
            }

            // after loop, $l is first index > b, $r is last index < b
            $bestDiff = $diff; // start with original diff

            if (isset($sorted[$l])) {
                $cand = abs($sorted[$l] - $b);
                if ($cand < $bestDiff) $bestDiff = $cand;
            }
            if (isset($sorted[$r])) {
                $cand = abs($sorted[$r] - $b);
                if ($cand < $bestDiff) $bestDiff = $cand;
            }

            $reduction = $diff - $bestDiff;
            if ($reduction > $maxReduction) {
                $maxReduction = $reduction;
            }
        }

        $result = ($origSum - $maxReduction) % $mod;
        if ($result < 0) $result += $mod;
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minAbsoluteSumDiff(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let MOD = 1_000_000_007
        let n = nums1.count
        var sortedNums = nums1.sorted()
        var total: Int64 = 0
        var maxGain: Int64 = 0
        
        for i in 0..<n {
            let a = nums1[i]
            let b = nums2[i]
            let diff = abs(a - b)
            total += Int64(diff)
            
            // lower bound binary search for b
            var l = 0
            var r = sortedNums.count
            while l < r {
                let m = (l + r) >> 1
                if sortedNums[m] < b {
                    l = m + 1
                } else {
                    r = m
                }
            }
            
            var best = diff
            if l < sortedNums.count {
                best = min(best, abs(sortedNums[l] - b))
            }
            if l > 0 {
                best = min(best, abs(sortedNums[l - 1] - b))
            }
            
            let gain = diff - best
            if gain > maxGain {
                maxGain = Int64(gain)
            }
        }
        
        let result = (total - maxGain) % Int64(MOD)
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minAbsoluteSumDiff(nums1: IntArray, nums2: IntArray): Int {
        val MOD = 1_000_000_007L
        val sorted = nums1.clone()
        java.util.Arrays.sort(sorted)
        var total = 0L
        var maxGain = 0L
        for (i in nums1.indices) {
            val a = nums1[i]
            val b = nums2[i]
            val diff = kotlin.math.abs(a - b).toLong()
            total += diff

            var idx = java.util.Arrays.binarySearch(sorted, b)
            if (idx < 0) idx = -(idx + 1)

            var best = Long.MAX_VALUE
            if (idx < sorted.size) {
                best = kotlin.math.abs(sorted[idx] - b).toLong()
            }
            if (idx > 0) {
                val cand = kotlin.math.abs(sorted[idx - 1] - b).toLong()
                if (cand < best) best = cand
            }

            val gain = diff - best
            if (gain > maxGain) maxGain = gain
        }
        val result = ((total - maxGain) % MOD + MOD) % MOD
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int minAbsoluteSumDiff(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    List<int> sorted = List.from(nums1);
    sorted.sort();

    int maxReduction = 0;
    int total = 0;

    for (int i = 0; i < n; ++i) {
      int a = nums1[i];
      int b = nums2[i];
      int diff = (a - b).abs();
      total += diff;

      int idx = _lowerBound(sorted, b);

      if (idx < n) {
        int cand = (sorted[idx] - b).abs();
        int reduction = diff - cand;
        if (reduction > maxReduction) maxReduction = reduction;
      }
      if (idx > 0) {
        int cand = (sorted[idx - 1] - b).abs();
        int reduction = diff - cand;
        if (reduction > maxReduction) maxReduction = reduction;
      }
    }

    int result = (total - maxReduction) % _mod;
    if (result < 0) result += _mod;
    return result;
  }

  int _lowerBound(List<int> arr, int target) {
    int left = 0, right = arr.length;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

const mod int64 = 1000000007

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func minAbsoluteSumDiff(nums1 []int, nums2 []int) int {
	n := len(nums1)
	sorted := make([]int, n)
	copy(sorted, nums1)
	sort.Ints(sorted)

	var total int64
	var maxReduce int64

	for i := 0; i < n; i++ {
		a := nums1[i]
		b := nums2[i]
		curDiff := abs(a - b)
		total += int64(curDiff)

		idx := sort.Search(len(sorted), func(j int) bool { return sorted[j] >= b })
		bestDiff := curDiff

		if idx < n {
			cand := abs(sorted[idx] - b)
			if cand < bestDiff {
				bestDiff = cand
			}
		}
		if idx > 0 {
			cand := abs(sorted[idx-1] - b)
			if cand < bestDiff {
				bestDiff = cand
			}
		}

		reduction := curDiff - bestDiff
		if reduction > int(maxReduce) {
			maxReduce = int64(reduction)
		}
	}

	ans := (total - maxReduce) % mod
	if ans < 0 {
		ans += mod
	}
	return int(ans)
}
```

## Ruby

```ruby
def min_absolute_sum_diff(nums1, nums2)
  mod = 1_000_000_007
  sorted = nums1.sort
  total = 0
  max_reduction = 0

  nums1.each_with_index do |a, i|
    b = nums2[i]
    diff = (a - b).abs
    total += diff

    # binary search lower bound for b in sorted array
    l = 0
    r = sorted.length
    while l < r
      m = (l + r) / 2
      if sorted[m] < b
        l = m + 1
      else
        r = m
      end
    end

    # candidate at position l
    if l < sorted.length
      cand = (sorted[l] - b).abs
      reduction = diff - cand
      max_reduction = reduction if reduction > max_reduction
    end

    # candidate at position l-1
    if l > 0
      cand = (sorted[l - 1] - b).abs
      reduction = diff - cand
      max_reduction = reduction if reduction > max_reduction
    end
  end

  ((total % mod) - max_reduction) % mod
end
```

## Scala

```scala
object Solution {
    def minAbsoluteSumDiff(nums1: Array[Int], nums2: Array[Int]): Int = {
        val mod = 1000000007L
        val sorted = nums1.sorted
        var total = 0L
        var maxImprove = 0L

        for (i <- nums1.indices) {
            val a = nums1(i)
            val b = nums2(i)
            val diff = math.abs(a - b).toLong
            total += diff

            var idx = java.util.Arrays.binarySearch(sorted, b)
            if (idx < 0) idx = -idx - 1

            if (idx < sorted.length) {
                val newDiff = math.abs(sorted(idx) - b).toLong
                val improve = diff - newDiff
                if (improve > maxImprove) maxImprove = improve
            }
            if (idx > 0) {
                val newDiff = math.abs(sorted(idx - 1) - b).toLong
                val improve = diff - newDiff
                if (improve > maxImprove) maxImprove = improve
            }
        }

        ((total - maxImprove) % mod + mod).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_absolute_sum_diff(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums1.len();
        let mut sorted = nums1.clone();
        sorted.sort_unstable();

        let mut total: i64 = 0;
        let mut max_reduction: i64 = 0;

        for i in 0..n {
            let a = nums1[i] as i64;
            let b = nums2[i] as i64;
            let diff = (a - b).abs();
            total += diff;

            match sorted.binary_search(&nums2[i]) {
                Ok(_) => {
                    // can make this term zero
                    if diff > max_reduction {
                        max_reduction = diff;
                    }
                }
                Err(pos) => {
                    let mut best = i64::MAX;
                    if pos < sorted.len() {
                        best = (sorted[pos] as i64 - b).abs();
                    }
                    if pos > 0 {
                        let cand = (sorted[pos - 1] as i64 - b).abs();
                        if cand < best {
                            best = cand;
                        }
                    }
                    let reduction = diff - best;
                    if reduction > max_reduction {
                        max_reduction = reduction;
                    }
                }
            }
        }

        let ans = ((total - max_reduction) % MOD + MOD) % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (lower-bound vec target)
  (let loop ([l 0] [r (vector-length vec)])
    (if (= l r)
        l
        (let* ([mid (quotient (+ l r) 2)]
               [mid-val (vector-ref vec mid)])
          (if (< mid-val target)
              (loop (+ mid 1) r)
              (loop l mid))))))

(define/contract (min-absolute-sum-diff nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([n (length nums1)]
         [sorted (list->vector (sort nums1 <))])
    (let loop ((i 0) (sum 0) (best 0))
      (if (= i n)
          (modulo (- sum best) MOD)
          (let* ([a (list-ref nums1 i)]
                 [b (list-ref nums2 i)]
                 [cur-diff (abs (- a b))]
                 [lb (lower-bound sorted b)]
                 [diff1 (if (< lb n) (abs (- (vector-ref sorted lb) b)) cur-diff)]
                 [diff2 (if (> lb 0) (abs (- (vector-ref sorted (- lb 1)) b)) cur-diff)]
                 [best-new-diff (min diff1 diff2)]
                 [reduction (- cur-diff best-new-diff)])
            (loop (+ i 1)
                  (+ sum cur-diff)
                  (max best reduction)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_absolute_sum_diff/2]).

-spec min_absolute_sum_diff(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_absolute_sum_diff(Nums1, Nums2) ->
    Mod = 1000000007,
    SortedTuple = list_to_tuple(lists:sort(Nums1)),
    Len = tuple_size(SortedTuple),
    {TotalSum, MaxRed} = lists:foldl(
        fun({A,B}, {AccSum, AccRed}) ->
            Diff = abs(A - B),
            NewDiff = find_closest(SortedTuple, Len, B),
            Red = Diff - NewDiff,
            {AccSum + Diff, max(AccRed, Red)}
        end,
        {0, 0},
        lists:zip(Nums1, Nums2)
    ),
    Result = (TotalSum - MaxRed) rem Mod,
    if Result < 0 -> Result + Mod; true -> Result end.

find_closest(Tuple, Len, Target) ->
    find_insert(Tuple, Len, 0, Len-1, Target).

find_insert(_Tuple, _Len, Low, High, _Target) when Low > High ->
    DiffList1 = if Low < _Len -> [abs(_Target - element(Low+1, _Tuple))] else [] end,
    DiffList2 = if Low-1 >= 0 -> [abs(_Target - element(Low, _Tuple))] else [] end,
    lists:min(DiffList1 ++ DiffList2);
find_insert(Tuple, Len, Low, High, Target) ->
    Mid = (Low + High) div 2,
    Val = element(Mid+1, Tuple),
    case Val of
        V when V == Target -> 0;
        V when V < Target -> find_insert(Tuple, Len, Mid+1, High, Target);
        _ -> find_insert(Tuple, Len, Low, Mid-1, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @modulo 1_000_000_007

  @spec min_absolute_sum_diff(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_absolute_sum_diff(nums1, nums2) do
    n = length(nums1)
    sorted_arr = :array.from_list(Enum.sort(nums1))
    arr1 = :array.from_list(nums1)
    arr2 = :array.from_list(nums2)

    {total, max_red} =
      Enum.reduce(0..(n - 1), {0, 0}, fn i, {tot, maxr} ->
        a = :array.get(i, arr1)
        b = :array.get(i, arr2)
        diff = abs(a - b)

        new_tot = rem(tot + diff, @modulo)

        idx = lower_bound(sorted_arr, n, b)

        best_diff = diff

        best_diff =
          if idx < n do
            cand = abs(:array.get(idx, sorted_arr) - b)
            if cand < best_diff, do: cand, else: best_diff
          else
            best_diff
          end

        best_diff =
          if idx > 0 do
            cand = abs(:array.get(idx - 1, sorted_arr) - b)
            if cand < best_diff, do: cand, else: best_diff
          else
            best_diff
          end

        reduction = diff - best_diff
        new_maxr = if reduction > maxr, do: reduction, else: maxr

        {new_tot, new_maxr}
      end)

    rem(total - max_red + @modulo, @modulo)
  end

  defp lower_bound(arr, n, target) do
    lower_bound(arr, n, target, 0, n)
  end

  defp lower_bound(_arr, _n, _target, low, high) when low >= high, do: low

  defp lower_bound(arr, n, target, low, high) do
    mid = div(low + high, 2)
    val = :array.get(mid, arr)

    if val < target do
      lower_bound(arr, n, target, mid + 1, high)
    else
      lower_bound(arr, n, target, low, mid)
    end
  end
end
```

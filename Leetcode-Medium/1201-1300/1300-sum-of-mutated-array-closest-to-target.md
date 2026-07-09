# 1300. Sum of Mutated Array Closest to Target

## Cpp

```cpp
class Solution {
public:
    int findBestValue(vector<int>& arr, int target) {
        sort(arr.begin(), arr.end());
        int n = arr.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + arr[i];
        
        auto getSum = [&](int v) -> long long {
            int idx = upper_bound(arr.begin(), arr.end(), v) - arr.begin();
            return pref[idx] + (long long)(n - idx) * v;
        };
        
        int low = 0, high = arr.back();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (getSum(mid) < target)
                low = mid + 1;
            else
                high = mid;
        }
        
        int best = low;
        long long bestDiff = llabs(getSum(low) - target);
        if (low > 0) {
            long long diffPrev = llabs(getSum(low - 1) - target);
            if (diffPrev <= bestDiff) {
                best = low - 1;
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int findBestValue(int[] arr, int target) {
        java.util.Arrays.sort(arr);
        int n = arr.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + arr[i];
        }
        int low = 0, high = arr[n - 1];
        while (low < high) {
            int mid = low + (high - low) / 2;
            long sum = cappedSum(arr, prefix, mid);
            if (sum < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        int v1 = low;
        int v0 = low - 1;

        long diff1 = Math.abs(cappedSum(arr, prefix, v1) - target);
        long diff0 = Long.MAX_VALUE;
        if (v0 >= 0) {
            diff0 = Math.abs(cappedSum(arr, prefix, v0) - target);
        }
        return diff0 <= diff1 ? v0 : v1;
    }

    private long cappedSum(int[] arr, long[] prefix, int value) {
        int idx = upperBound(arr, value); // first index > value
        return prefix[idx] + (long) (arr.length - idx) * value;
    }

    private int upperBound(int[] arr, int target) {
        int left = 0, right = arr.length; // [left, right)
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        arr.sort()
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        def capped_sum(val):
            # index of first element greater than val
            idx = bisect.bisect_right(arr, val)
            return prefix[idx] + (n - idx) * val

        lo, hi = 0, arr[-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if capped_sum(mid) < target:
                lo = mid + 1
            else:
                hi = mid

        # lo is the smallest value where sum >= target (or max possible)
        best_val = lo
        best_diff = abs(capped_sum(lo) - target)

        if lo > 0:
            diff_prev = abs(capped_sum(lo - 1) - target)
            if diff_prev < best_diff or (diff_prev == best_diff and lo - 1 < best_val):
                best_val = lo - 1
                best_diff = diff_prev

        return best_val
```

## Python3

```python
from bisect import bisect_right
from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        def capped_sum(v: int) -> int:
            idx = bisect_right(arr, v)
            return prefix[idx] + (n - idx) * v

        lo, hi = 0, arr[-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if capped_sum(mid) < target:
                lo = mid + 1
            else:
                hi = mid

        best_val = lo
        best_diff = abs(capped_sum(best_val) - target)

        if lo > 0:
            prev_val = lo - 1
            prev_diff = abs(capped_sum(prev_val) - target)
            if prev_diff <= best_diff:
                best_val = prev_val
                best_diff = prev_diff

        return best_val
```

## C

```c
#include <stdlib.h>
#include <math.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

static long long sumWithCap(int *arr, int n, long long *pref, int v) {
    int l = 0, r = n;
    while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m] <= v)
            l = m + 1;
        else
            r = m;
    }
    int idx = l; // number of elements <= v
    long long sum = pref[idx] + (long long)(n - idx) * v;
    return sum;
}

int findBestValue(int* arr, int arrSize, int target) {
    qsort(arr, arrSize, sizeof(int), cmp_int);
    long long *pref = (long long *)malloc((arrSize + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < arrSize; ++i)
        pref[i + 1] = pref[i] + arr[i];

    int low = 0, high = arr[arrSize - 1];
    while (low < high) {
        int mid = (low + high) >> 1;
        long long s = sumWithCap(arr, arrSize, pref, mid);
        if (s < target)
            low = mid + 1;
        else
            high = mid;
    }

    int best = low;
    long long bestDiff = llabs(sumWithCap(arr, arrSize, pref, low) - (long long)target);

    if (low > 0) {
        int cand = low - 1;
        long long diffCand = llabs(sumWithCap(arr, arrSize, pref, cand) - (long long)target);
        if (diffCand < bestDiff || (diffCand == bestDiff && cand < best)) {
            best = cand;
            bestDiff = diffCand;
        }
    }

    free(pref);
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindBestValue(int[] arr, int target)
    {
        Array.Sort(arr);
        int n = arr.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++)
            pref[i + 1] = pref[i] + arr[i];

        int low = 0, high = arr[n - 1];
        while (low < high)
        {
            int mid = (low + high) / 2;
            long sum = GetSum(arr, pref, mid);
            if (sum < target)
                low = mid + 1;
            else
                high = mid;
        }

        int best = low;
        long bestDiff = Math.Abs(GetSum(arr, pref, best) - target);

        if (low > 0)
        {
            long diffPrev = Math.Abs(GetSum(arr, pref, low - 1) - target);
            if (diffPrev <= bestDiff)
            {
                best = low - 1;
                bestDiff = diffPrev;
            }
        }

        return best;
    }

    private static long GetSum(int[] arr, long[] pref, int v)
    {
        int idx = UpperBound(arr, v);
        return pref[idx] + (long)(arr.Length - idx) * v;
    }

    private static int UpperBound(int[] arr, int target)
    {
        int l = 0, r = arr.Length;
        while (l < r)
        {
            int m = (l + r) / 2;
            if (arr[m] <= target)
                l = m + 1;
            else
                r = m;
        }
        return l;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var findBestValue = function(arr, target) {
    const maxVal = Math.max(...arr);
    
    const calcSum = (v) => {
        let sum = 0;
        for (let num of arr) {
            sum += num < v ? num : v;
        }
        return sum;
    };
    
    // binary search for smallest v such that sum(v) >= target
    let low = 0, high = maxVal;
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (calcSum(mid) < target) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    
    // candidates: low and low-1 (if low > 0)
    let bestV = low;
    let bestDiff = Math.abs(calcSum(low) - target);
    
    if (low > 0) {
        const vPrev = low - 1;
        const diffPrev = Math.abs(calcSum(vPrev) - target);
        if (diffPrev < bestDiff || (diffPrev === bestDiff && vPrev < bestV)) {
            bestV = vPrev;
            bestDiff = diffPrev;
        }
    }
    
    return bestV;
};
```

## Typescript

```typescript
function findBestValue(arr: number[], target: number): number {
    const n = arr.length;
    arr.sort((a, b) => a - b);
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }
    const maxVal = arr[n - 1];

    const getSum = (v: number): number => {
        // first index where arr[idx] > v
        let l = 0, r = n;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] <= v) l = m + 1;
            else r = m;
        }
        const idx = l; // count of elements <= v
        return prefix[idx] + (n - idx) * v;
    };

    let low = 0, high = maxVal;
    while (low < high) {
        const mid = (low + high) >> 1;
        if (getSum(mid) < target) low = mid + 1;
        else high = mid;
    }

    let bestV = low;
    let bestDiff = Math.abs(getSum(low) - target);
    if (low > 0) {
        const prevDiff = Math.abs(getSum(low - 1) - target);
        if (prevDiff < bestDiff || (prevDiff === bestDiff && low - 1 < bestV)) {
            bestV = low - 1;
            bestDiff = prevDiff;
        }
    }
    return bestV;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function findBestValue($arr, $target) {
        sort($arr);
        $n = count($arr);
        $prefix = [];
        $sum = 0;
        foreach ($arr as $v) {
            $sum += $v;
            $prefix[] = $sum;
        }
        // If target is larger than or equal to total sum, no capping needed
        if ($target >= $sum) {
            return $arr[$n - 1];
        }

        // Helper to compute capped sum for a given value
        $calcSum = function($val) use (&$arr, &$prefix, $n) {
            $l = 0;
            $r = $n; // exclusive
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($arr[$mid] <= $val) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }
            // $l is first index with arr[i] > val
            $idx = $l;
            $sumLessOrEqual = $idx > 0 ? $prefix[$idx - 1] : 0;
            $cntGreater = $n - $idx;
            return $sumLessOrEqual + $cntGreater * $val;
        };

        // Binary search for smallest value where capped sum >= target
        $low = 0;
        $high = $arr[$n - 1];
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($calcSum($mid) < $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }

        // Compare low and low-1 to find the closest
        $bestVal = $low;
        $bestDiff = abs($calcSum($low) - $target);
        if ($low > 0) {
            $prevDiff = abs($calcSum($low - 1) - $target);
            if ($prevDiff <= $bestDiff) { // tie -> smaller value
                $bestVal = $low - 1;
                $bestDiff = $prevDiff;
            }
        }

        return $bestVal;
    }
}
```

## Swift

```swift
class Solution {
    func findBestValue(_ arr: [Int], _ target: Int) -> Int {
        let sortedArr = arr.sorted()
        let n = sortedArr.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + sortedArr[i]
        }
        
        func getSum(_ v: Int) -> Int {
            var l = 0
            var r = n
            while l < r {
                let m = (l + r) >> 1
                if sortedArr[m] <= v {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return prefix[l] + (n - l) * v
        }
        
        var low = 0
        var high = sortedArr.last!
        while low < high {
            let mid = (low + high) >> 1
            if getSum(mid) < target {
                low = mid + 1
            } else {
                high = mid
            }
        }
        
        var bestV = low
        var bestDiff = abs(getSum(bestV) - target)
        if low > 0 {
            let prevDiff = abs(getSum(low - 1) - target)
            if prevDiff < bestDiff || (prevDiff == bestDiff && low - 1 < bestV) {
                bestV = low - 1
                bestDiff = prevDiff
            }
        }
        return bestV
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findBestValue(arr: IntArray, target: Int): Int {
        val sorted = arr.clone()
        java.util.Arrays.sort(sorted)
        var left = 0
        var right = sorted.maxOrNull()!!

        while (left < right) {
            val mid = (left + right + 1) / 2
            if (mutatedSum(sorted, mid) <= target.toLong()) {
                left = mid
            } else {
                right = mid - 1
            }
        }

        var bestVal = left
        var bestDiff = kotlin.math.abs(mutatedSum(sorted, left) - target.toLong())

        if (left < sorted.maxOrNull()!!) {
            val diffNext = kotlin.math.abs(mutatedSum(sorted, left + 1) - target.toLong())
            if (diffNext < bestDiff || (diffNext == bestDiff && left + 1 < bestVal)) {
                bestVal = left + 1
            }
        }

        return bestVal
    }

    private fun mutatedSum(arr: IntArray, cap: Int): Long {
        var sum = 0L
        for (v in arr) {
            sum += if (v > cap) cap else v
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int findBestValue(List<int> arr, int target) {
    arr.sort();
    int n = arr.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] + arr[i];
    }
    int maxVal = arr[n - 1];
    int low = 0;
    int high = maxVal;
    while (low < high) {
      int mid = (low + high) >> 1;
      int sumMid = _calcSum(arr, prefix, mid);
      if (sumMid < target) {
        low = mid + 1;
      } else {
        high = mid;
      }
    }
    int best = low;
    int sumLow = _calcSum(arr, prefix, low);
    int diffLow = (sumLow - target).abs();
    if (low > 0) {
      int sumPrev = _calcSum(arr, prefix, low - 1);
      int diffPrev = (sumPrev - target).abs();
      if (diffPrev <= diffLow) {
        best = low - 1;
      }
    }
    return best;
  }

  int _calcSum(List<int> arr, List<int> prefix, int v) {
    int left = 0;
    int right = arr.length;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (arr[mid] <= v) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    int idx = left; // number of elements <= v
    return prefix[idx] + (arr.length - idx) * v;
  }
}
```

## Golang

```go
import "sort"

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func findBestValue(arr []int, target int) int {
	sort.Ints(arr)
	n := len(arr)

	prefix := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + arr[i]
	}
	maxVal := arr[n-1]

	sumFunc := func(v int) int {
		idx := sort.Search(n, func(i int) bool { return arr[i] > v })
		return prefix[idx] + (n-idx)*v
	}

	low, high := 0, maxVal
	for low < high {
		mid := (low + high) / 2
		if sumFunc(mid) < target {
			low = mid + 1
		} else {
			high = mid
		}
	}

	bestV := low
	bestDiff := abs(sumFunc(low) - target)
	if low > 0 {
		prevDiff := abs(sumFunc(low-1) - target)
		if prevDiff < bestDiff || (prevDiff == bestDiff && low-1 < bestV) {
			bestV = low - 1
			bestDiff = prevDiff
		}
	}
	_ = bestDiff // silence unused warning if any

	return bestV
}
```

## Ruby

```ruby
def find_best_value(arr, target)
  n = arr.length
  arr.sort!
  pref = Array.new(n + 1, 0)
  (1..n).each { |i| pref[i] = pref[i - 1] + arr[i - 1] }

  # helper to compute sum after capping at v
  capped_sum = lambda do |v|
    idx = arr.bsearch_index { |x| x > v } || n
    pref[idx] + (n - idx) * v
  end

  low = 0
  high = arr.max
  while low < high
    mid = (low + high) / 2
    if capped_sum.call(mid) < target
      low = mid + 1
    else
      high = mid
    end
  end

  best_val = low
  best_diff = (capped_sum.call(best_val) - target).abs

  if best_val > 0
    v2 = best_val - 1
    diff2 = (capped_sum.call(v2) - target).abs
    if diff2 < best_diff || (diff2 == best_diff && v2 < best_val)
      best_val = v2
      best_diff = diff2
    end
  end

  best_val
end
```

## Scala

```scala
object Solution {
    def findBestValue(arr: Array[Int], target: Int): Int = {
        val sorted = arr.sorted
        val n = sorted.length
        val prefix = new Array[Long](n + 1)
        for (i <- 0 until n) {
            prefix(i + 1) = prefix(i) + sorted(i).toLong
        }

        def sumAt(v: Int): Long = {
            var l = 0
            var r = n
            while (l < r) {
                val m = (l + r) >>> 1
                if (sorted(m) <= v) l = m + 1 else r = m
            }
            val cntLe = l
            val sumLe = prefix(cntLe)
            val cntGt = n - cntLe
            sumLe + cntGt.toLong * v
        }

        var low = 0
        var high = sorted.max
        while (low < high) {
            val mid = (low + high) >>> 1
            if (sumAt(mid) < target) low = mid + 1 else high = mid
        }

        var bestV = low
        var bestDiff = math.abs(sumAt(bestV) - target)
        if (low > 0) {
            val v2 = low - 1
            val diff2 = math.abs(sumAt(v2) - target)
            if (diff2 < bestDiff || (diff2 == bestDiff && v2 < bestV)) {
                bestV = v2
                bestDiff = diff2
            }
        }
        bestV
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_best_value(mut arr: Vec<i32>, target: i32) -> i32 {
        arr.sort_unstable();
        let n = arr.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + arr[i] as i64;
        }
        let max_val = *arr.last().unwrap();

        fn sum_at(v: i32, arr: &Vec<i32>, prefix: &Vec<i64>) -> i64 {
            let idx = arr.partition_point(|&x| x <= v);
            let small_sum = prefix[idx];
            let cnt_big = (arr.len() - idx) as i64;
            small_sum + cnt_big * v as i64
        }

        let mut lo: i32 = 0;
        let mut hi: i32 = max_val;
        while lo <= hi {
            let mid = lo + ((hi - lo) >> 1);
            let s = sum_at(mid, &arr, &prefix);
            if s < target as i64 {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        // lo is the smallest value with sum >= target
        let mut best_v = lo;
        let mut best_diff = (sum_at(best_v, &arr, &prefix) - target as i64).abs();

        if lo > 0 {
            let v2 = lo - 1;
            let diff2 = (sum_at(v2, &arr, &prefix) - target as i64).abs();
            if diff2 < best_diff || (diff2 == best_diff && v2 < best_v) {
                best_v = v2;
                best_diff = diff2;
            }
        }

        best_v
    }
}
```

## Racket

```racket
(define/contract (find-best-value arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((maxv (apply max arr)))
    ;; sum of array after capping each element to v
    (define (capped-sum v)
      (let loop ((lst arr) (acc 0))
        (if (null? lst)
            acc
            (let ((a (car lst)))
              (loop (cdr lst)
                    (+ acc (if (> a v) v a)))))))
    ;; binary search for the smallest v such that capped-sum(v) >= target
    (define (search lo hi)
      (if (= lo hi)
          lo
          (let* ((mid (quotient (+ lo hi) 2))
                 (s   (capped-sum mid)))
            (if (< s target)
                (search (+ mid 1) hi)
                (search lo mid)))))
    (define best-candidate (search 0 maxv))
    (define (diff v) (abs (- (capped-sum v) target)))
    (let* ((cand1 best-candidate)
           (cand2 (if (> best-candidate 0) (- best-candidate 1) best-candidate))
           (d1 (diff cand1))
           (d2 (diff cand2)))
      (cond [(< d2 d1) cand2]
            [(> d2 d1) cand1]
            [else (min cand1 cand2)]))))
```

## Erlang

```erlang
-module(solution).
-export([find_best_value/2]).

-spec find_best_value(Arr :: [integer()], Target :: integer()) -> integer().
find_best_value(Arr, Target) ->
    Max = lists:max(Arr),
    V = bin_search(Arr, Target, 0, Max),
    case V of
        0 -> 0;
        _ ->
            SumV = sum_min(Arr, V),
            DiffV = abs(SumV - Target),
            Prev = V - 1,
            SumPrev = sum_min(Arr, Prev),
            DiffPrev = abs(SumPrev - Target),
            if DiffPrev =< DiffV -> Prev;
               true -> V
            end
    end.

-spec bin_search([integer()], integer(), integer(), integer()) -> integer().
bin_search(_Arr, _Target, Low, High) when Low >= High ->
    Low;
bin_search(Arr, Target, Low, High) ->
    Mid = (Low + High) div 2,
    SumMid = sum_min(Arr, Mid),
    if SumMid < Target ->
            bin_search(Arr, Target, Mid + 1, High);
       true ->
            bin_search(Arr, Target, Low, Mid)
    end.

-spec sum_min([integer()], integer()) -> integer().
sum_min(Arr, V) ->
    lists:foldl(fun(A, Acc) -> Acc + erlang:min(A, V) end, 0, Arr).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_best_value(arr :: [integer], target :: integer) :: integer
  def find_best_value(arr, target) do
    max_val = Enum.max(arr)
    v1 = bin_search(arr, target, 0, max_val)
    v0 = if v1 > 0, do: v1 - 1, else: 0

    sum_v1 = sum_capped(arr, v1)
    sum_v0 = sum_capped(arr, v0)

    diff1 = abs(sum_v1 - target)
    diff0 = abs(sum_v0 - target)

    if diff0 <= diff1, do: v0, else: v1
  end

  defp bin_search(_arr, _target, lo, hi) when lo >= hi, do: lo

  defp bin_search(arr, target, lo, hi) do
    mid = div(lo + hi, 2)
    s = sum_capped(arr, mid)

    if s < target do
      bin_search(arr, target, mid + 1, hi)
    else
      bin_search(arr, target, lo, mid)
    end
  end

  defp sum_capped(arr, cap) do
    Enum.reduce(arr, 0, fn x, acc -> acc + min(x, cap) end)
  end
end
```

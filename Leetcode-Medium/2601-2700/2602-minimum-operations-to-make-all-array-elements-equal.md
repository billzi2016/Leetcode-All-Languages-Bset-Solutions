# 2602. Minimum Operations to Make All Array Elements Equal

## Cpp

```cpp
class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + nums[i];
        }
        long long totalSum = pref[n];
        vector<long long> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            int idx = lower_bound(nums.begin(), nums.end(), q) - nums.begin();
            long long leftCount = idx;
            long long rightCount = n - idx;
            long long leftSum = pref[idx];
            long long rightSum = totalSum - leftSum;
            long long opsLeft = (long long)q * leftCount - leftSum;
            long long opsRight = rightSum - (long long)q * rightCount;
            ans.push_back(opsLeft + opsRight);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Long> minOperations(int[] nums, int[] queries) {
        int n = nums.length;
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + sorted[i];
        }
        List<Long> result = new ArrayList<>(queries.length);
        for (int q : queries) {
            int idx = upperBound(sorted, q);
            long left = (long) q * idx - prefix[idx];
            long right = (prefix[n] - prefix[idx]) - (long) q * (n - idx);
            result.add(left + right);
        }
        return result;
    }

    private int upperBound(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        import bisect
        res = []
        total_sum = prefix[n]
        for q in queries:
            idx = bisect.bisect_left(nums, q)  # count of elements < q
            left_ops = q * idx - prefix[idx]
            right_ops = (total_sum - prefix[idx]) - q * (n - idx)
            res.append(left_ops + right_ops)
        return res
```

## Python3

```python
class Solution:
    def minOperations(self, nums, queries):
        from bisect import bisect_left
        n = len(nums)
        nums.sort()
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        total = pref[n]
        res = []
        for q in queries:
            idx = bisect_left(nums, q)
            left_sum = pref[idx]
            right_sum = total - left_sum
            left_ops = q * idx - left_sum
            right_ops = right_sum - q * (n - idx)
            res.append(left_ops + right_ops)
        return res
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return (ai > bi) - (ai < bi);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* minOperations(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    *returnSize = queriesSize;
    if (queriesSize == 0) return NULL;

    qsort(nums, numsSize, sizeof(int), cmp_int);

    long long *pref = (long long *)malloc((numsSize + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < numsSize; ++i)
        pref[i + 1] = pref[i] + (long long)nums[i];

    long long *ans = (long long *)malloc(queriesSize * sizeof(long long));

    for (int i = 0; i < queriesSize; ++i) {
        int q = queries[i];
        int l = 0, r = numsSize;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] < q)
                l = m + 1;
            else
                r = m;
        }
        int idx = l; // first index with nums[idx] >= q

        long long leftCnt = idx;
        long long rightCnt = numsSize - idx;

        long long leftSum = pref[idx];
        long long rightSum = pref[numsSize] - pref[idx];

        ans[i] = (long long)q * leftCnt - leftSum + rightSum - (long long)q * rightCnt;
    }

    free(pref);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<long> MinOperations(int[] nums, int[] queries) {
        int n = nums.Length;
        Array.Sort(nums);
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        List<long> result = new List<long>(queries.Length);
        foreach (int q in queries) {
            int idx = LowerBound(nums, q);
            long leftCount = idx;
            long rightCount = n - idx;

            long leftSum = prefix[idx];
            long rightSum = prefix[n] - prefix[idx];

            long x = q;
            long ops = x * leftCount - leftSum + (rightSum - x * rightCount);
            result.Add(ops);
        }
        return result;
    }

    private int LowerBound(int[] arr, int target) {
        int lo = 0, hi = arr.Length;
        while (lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
var minOperations = function(nums, queries) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const prefix = new Array(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const total = prefix[n];
    const result = [];
    for (const q of queries) {
        // lower bound: first index with value >= q
        let l = 0, r = n;
        while (l < r) {
            const m = (l + r) >> 1;
            if (nums[m] < q) l = m + 1;
            else r = m;
        }
        const idx = l; // count of elements < q
        const leftCount = idx;
        const rightCount = n - idx;
        const sumLeft = prefix[idx];
        const sumRight = total - sumLeft;
        const ops = (q * leftCount - sumLeft) + (sumRight - q * rightCount);
        result.push(ops);
    }
    return result;
};
```

## Typescript

```typescript
function minOperations(nums: number[], queries: number[]): number[] {
    const n = nums.length;
    const sorted = [...nums].sort((a, b) => a - b);
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + sorted[i];
    }

    const result: number[] = [];

    for (const q of queries) {
        // lower bound: first index with value >= q
        let lo = 0, hi = n;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (sorted[mid] < q) lo = mid + 1;
            else hi = mid;
        }
        const idx = lo; // count of elements < q
        const left = q * idx - prefix[idx];
        const right = (prefix[n] - prefix[idx]) - q * (n - idx);
        result.push(left + right);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @return Integer[]
     */
    function minOperations($nums, $queries) {
        sort($nums);
        $n = count($nums);
        $prefix = [];
        $sum = 0;
        foreach ($nums as $val) {
            $sum += $val;
            $prefix[] = $sum;
        }
        $total = $sum;
        $result = [];

        foreach ($queries as $q) {
            // binary search: first index with value > q
            $l = 0;
            $r = $n; // exclusive
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($nums[$mid] <= $q) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }
            $k = $l; // number of elements <= q

            $sumLeft = $k > 0 ? $prefix[$k - 1] : 0;
            $sumRight = $total - $sumLeft;

            $leftOps = $q * $k - $sumLeft;
            $rightOps = $sumRight - $q * ($n - $k);

            $result[] = $leftOps + $rightOps;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let n = nums.count
        let sortedNums = nums.sorted()
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(sortedNums[i])
        }
        let totalSum = prefix[n]
        
        func lowerBound(_ arr: [Int], _ target: Int) -> Int {
            var l = 0
            var r = arr.count
            while l < r {
                let mid = (l + r) >> 1
                if arr[mid] < target {
                    l = mid + 1
                } else {
                    r = mid
                }
            }
            return l
        }
        
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let idx = lowerBound(sortedNums, q)
            let leftSum = prefix[idx]
            let rightSum = totalSum - leftSum
            let leftOps = Int64(q) * Int64(idx) - leftSum
            let rightOps = rightSum - Int64(q) * Int64(n - idx)
            let ans = leftOps + rightOps
            result.append(Int(ans))
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, queries: IntArray): List<Long> {
        val n = nums.size
        val sorted = nums.clone()
        java.util.Arrays.sort(sorted)
        val prefix = LongArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + sorted[i].toLong()
        }
        val totalSum = prefix[n]
        val result = ArrayList<Long>(queries.size)
        for (q in queries) {
            var l = 0
            var r = n
            while (l < r) {
                val mid = (l + r) ushr 1
                if (sorted[mid] <= q) {
                    l = mid + 1
                } else {
                    r = mid
                }
            }
            val leftCount = l
            val sumLeft = prefix[leftCount]
            val rightCount = n - leftCount
            val sumRight = totalSum - sumLeft
            val leftDiff = q.toLong() * leftCount - sumLeft
            val rightDiff = sumRight - q.toLong() * rightCount
            result.add(leftDiff + rightDiff)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> minOperations(List<int> nums, List<int> queries) {
    int n = nums.length;
    List<int> sorted = List.from(nums);
    sorted.sort();
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] + sorted[i];
    }
    int totalSum = prefix[n];

    int lowerBound(List<int> arr, int target) {
      int l = 0, r = arr.length;
      while (l < r) {
        int mid = (l + r) >> 1;
        if (arr[mid] < target) {
          l = mid + 1;
        } else {
          r = mid;
        }
      }
      return l;
    }

    List<int> ans = [];
    for (int q in queries) {
      int idx = lowerBound(sorted, q);
      int leftCount = idx;
      int rightCount = n - idx;

      int sumLeft = prefix[idx];
      int sumRight = totalSum - sumLeft;

      int leftOps = q * leftCount - sumLeft;
      int rightOps = sumRight - q * rightCount;

      ans.add(leftOps + rightOps);
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func minOperations(nums []int, queries []int) []int64 {
	n := len(nums)
	sort.Ints(nums)

	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(nums[i])
	}
	total := pref[n]

	ans := make([]int64, len(queries))
	for i, q := range queries {
		idx := sort.Search(n, func(j int) bool { return nums[j] >= q })
		leftCnt := int64(idx)
		sumLeft := pref[idx]
		rightCnt := int64(n - idx)
		sumRight := total - sumLeft
		q64 := int64(q)

		ans[i] = q64*leftCnt - sumLeft + sumRight - q64*rightCnt
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def min_operations(nums, queries)
  sorted = nums.sort
  n = sorted.size
  prefix = Array.new(n + 1, 0)
  (0...n).each do |i|
    prefix[i + 1] = prefix[i] + sorted[i]
  end

  total_sum = prefix[n]
  result = []

  queries.each do |x|
    idx = sorted.bsearch_index { |v| v >= x } || n
    left_ops = x * idx - prefix[idx]
    right_ops = (total_sum - prefix[idx]) - x * (n - idx)
    result << left_ops + right_ops
  end

  result
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], queries: Array[Int]): List[Long] = {
        val n = nums.length
        val sorted = nums.map(_.toLong).sorted
        val prefix = new Array[Long](n + 1)
        var i = 0
        while (i < n) {
            prefix(i + 1) = prefix(i) + sorted(i)
            i += 1
        }
        val totalSum = prefix(n)

        def lowerBound(arr: Array[Long], target: Long): Int = {
            var l = 0
            var r = arr.length
            while (l < r) {
                val mid = (l + r) >>> 1
                if (arr(mid) < target) l = mid + 1 else r = mid
            }
            l
        }

        val res = new scala.collection.mutable.ListBuffer[Long]()
        for (q <- queries) {
            val t = q.toLong
            val idx = lowerBound(sorted, t)
            val leftCount = idx
            val leftSum = prefix(idx)
            val rightCount = n - idx
            val rightSum = totalSum - leftSum
            val ops = t * leftCount - leftSum + rightSum - t * rightCount
            res += ops
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut sorted = nums.clone();
        sorted.sort_unstable();

        // prefix sums, pref[i] = sum of first i elements (i from 0..=n)
        let mut pref: Vec<i64> = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + sorted[i] as i64;
        }

        let total_sum = pref[n];
        let mut answer: Vec<i64> = Vec::with_capacity(queries.len());

        for &q in queries.iter() {
            // number of elements <= q
            let idx = sorted.partition_point(|&x| x <= q);
            let left_cnt = idx as i64;
            let right_cnt = (n - idx) as i64;

            let left_sum = pref[idx];
            let right_sum = total_sum - left_sum;

            let t = q as i64;
            let ops_left = t * left_cnt - left_sum;
            let ops_right = right_sum - t * right_cnt;

            answer.push(ops_left + ops_right);
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (min-operations nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((sorted (sort nums <))
         (v (list->vector sorted))
         (n (vector-length v))
         (pref (make-vector (+ n 1) 0)))
    (for ([i (in-range n)])
      (vector-set! pref (+ i 1) (+ (vector-ref pref i) (vector-ref v i))))
    (define (upper-bound vec target)
      (let loop ((lo 0) (hi (vector-length vec)))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (mid-val (vector-ref vec mid)))
              (if (> mid-val target)
                  (loop lo mid)
                  (loop (+ mid 1) hi))))))
    (let loop-queries ((qs queries) (acc '()))
      (if (null? qs)
          (reverse acc)
          (let* ((q (car qs))
                 (idx (upper-bound v q))
                 (leftCount idx)
                 (rightCount (- n idx))
                 (sumLeft (vector-ref pref leftCount))
                 (sumRight (- (vector-ref pref n) sumLeft))
                 (ans (+ (- (* q leftCount) sumLeft)
                         (- sumRight (* q rightCount)))))
            (loop-queries (cdr qs) (cons ans acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/2]).

-spec min_operations(Nums :: [integer()], Queries :: [integer()]) -> [integer()].
min_operations(Nums, Queries) ->
    SortedList = lists:sort(Nums),
    N = length(SortedList),
    SortedTuple = list_to_tuple(SortedList),

    {_, RevPref} = lists:foldl(
        fun(X, {Sum, Acc}) ->
            NewSum = Sum + X,
            {NewSum, [NewSum | Acc]}
        end,
        {0, []},
        SortedList),
    PrefixList = lists:reverse(RevPref),
    FullPrefixList = [0 | PrefixList],
    PrefixTuple = list_to_tuple(FullPrefixList),

    TotalSum = element(N + 1, PrefixTuple),

    lists:map(
        fun(Q) ->
            Idx = upper_bound(SortedTuple, N, Q),   % number of elements <= Q
            L = Idx,
            R = N - Idx,
            SumLeft = element(L + 1, PrefixTuple),
            SumRight = TotalSum - SumLeft,
            (Q * L - SumLeft) + (SumRight - Q * R)
        end,
        Queries).

% binary search: returns count of elements <= Q
upper_bound(Tuple, N, Q) -> ub(0, N, Tuple, Q).

ub(Low, High, _Tuple, _Q) when Low >= High ->
    Low;
ub(Low, High, Tuple, Q) ->
    Mid = (Low + High + 1) div 2,
    case element(Mid, Tuple) =< Q of
        true -> ub(Mid, High, Tuple, Q);
        false -> ub(Low, Mid - 1, Tuple, Q)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], queries :: [integer]) :: [integer]
  def min_operations(nums, queries) do
    sorted = Enum.sort(nums)
    arr = List.to_tuple(sorted)
    pref_list = build_prefix(sorted)
    pref = List.to_tuple(pref_list)
    total_sum = elem(pref, tuple_size(pref) - 1)
    n = length(sorted)

    Enum.map(queries, fn q ->
      idx = lower_bound(arr, q)
      left_sum = elem(pref, idx)
      right_sum = total_sum - left_sum
      left_cnt = idx
      right_cnt = n - idx

      (q * left_cnt - left_sum) + (right_sum - q * right_cnt)
    end)
  end

  defp build_prefix(arr) do
    Enum.reduce(arr, [0], fn x, acc ->
      [hd(acc) + x | acc]
    end)
    |> Enum.reverse()
  end

  defp lower_bound(arr, target) do
    len = tuple_size(arr)
    lower_bound_rec(arr, target, 0, len)
  end

  defp lower_bound_rec(_arr, _target, lo, hi) when lo >= hi, do: lo

  defp lower_bound_rec(arr, target, lo, hi) do
    mid = div(lo + hi, 2)
    val = elem(arr, mid)

    if val < target do
      lower_bound_rec(arr, target, mid + 1, hi)
    else
      lower_bound_rec(arr, target, lo, mid)
    end
  end
end
```

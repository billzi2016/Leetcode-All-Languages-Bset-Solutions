# 3424. Minimum Cost to Make Arrays Identical

## Cpp

```cpp
class Solution {
public:
    long long minCost(vector<int>& arr, vector<int>& brr, long long k) {
        int n = arr.size();
        long long original = 0;
        for (int i = 0; i < n; ++i) {
            original += llabs((long long)arr[i] - (long long)brr[i]);
        }
        vector<int> aSorted = arr, bSorted = brr;
        sort(aSorted.begin(), aSorted.end());
        sort(bSorted.begin(), bSorted.end());
        long long sortedCost = 0;
        for (int i = 0; i < n; ++i) {
            sortedCost += llabs((long long)aSorted[i] - (long long)bSorted[i]);
        }
        long long withOp = sortedCost + k;
        return min(original, withOp);
    }
};
```

## Java

```java
class Solution {
    public long minCost(int[] arr, int[] brr, long k) {
        int n = arr.length;
        long costNoRearr = 0L;
        for (int i = 0; i < n; i++) {
            costNoRearr += Math.abs((long)arr[i] - (long)brr[i]);
        }

        int[] sortedArr = arr.clone();
        int[] sortedBrr = brr.clone();
        java.util.Arrays.sort(sortedArr);
        java.util.Arrays.sort(sortedBrr);

        long costWithRearr = k;
        for (int i = 0; i < n; i++) {
            costWithRearr += Math.abs((long)sortedArr[i] - (long)sortedBrr[i]);
        }

        return Math.min(costNoRearr, costWithRearr);
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, arr, brr, k):
        """
        :type arr: List[int]
        :type brr: List[int]
        :type k: int
        :rtype: int
        """
        # Cost without using the rearrangement operation
        cost_original = 0
        for a, b in zip(arr, brr):
            cost_original += abs(a - b)

        # Cost after sorting both arrays (optimal matching) plus the operation cost k
        arr_sorted = sorted(arr)
        brr_sorted = sorted(brr)
        cost_sorted = 0
        for a, b in zip(arr_sorted, brr_sorted):
            cost_sorted += abs(a - b)
        cost_with_op = cost_sorted + k

        return min(cost_original, cost_with_op)
```

## Python3

```python
from typing import List

class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        # Cost without using the special operation
        cost_no_op = sum(abs(a - b) for a, b in zip(arr, brr))
        
        # Cost when we can reorder arr (and implicitly brr) once at cost k
        sorted_arr = sorted(arr)
        sorted_brr = sorted(brr)
        cost_with_op = k + sum(abs(a - b) for a, b in zip(sorted_arr, sorted_brr))
        
        return min(cost_no_op, cost_with_op)
```

## C

```c
#include <stdlib.h>
#include <stddef.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

long long minCost(int* arr, int arrSize, int* brr, int brrSize, long long k) {
    (void)brrSize; // unused, sizes are equal
    long long original = 0;
    for (int i = 0; i < arrSize; ++i) {
        long long diff = (long long)arr[i] - (long long)brr[i];
        if (diff < 0) diff = -diff;
        original += diff;
    }

    int *aCopy = (int *)malloc(arrSize * sizeof(int));
    int *bCopy = (int *)malloc(arrSize * sizeof(int));
    if (!aCopy || !bCopy) {
        free(aCopy);
        free(bCopy);
        return 0; // allocation failure, shouldn't happen in LeetCode
    }

    for (int i = 0; i < arrSize; ++i) {
        aCopy[i] = arr[i];
        bCopy[i] = brr[i];
    }

    qsort(aCopy, arrSize, sizeof(int), cmp_int);
    qsort(bCopy, arrSize, sizeof(int), cmp_int);

    long long sortedDiff = 0;
    for (int i = 0; i < arrSize; ++i) {
        long long diff = (long long)aCopy[i] - (long long)bCopy[i];
        if (diff < 0) diff = -diff;
        sortedDiff += diff;
    }

    free(aCopy);
    free(bCopy);

    long long withRearrange = k + sortedDiff;
    return original < withRearrange ? original : withRearrange;
}
```

## Csharp

```csharp
public class Solution {
    public long MinCost(int[] arr, int[] brr, long k) {
        int n = arr.Length;
        long originalDiff = 0;
        for (int i = 0; i < n; i++) {
            originalDiff += Math.Abs((long)arr[i] - (long)brr[i]);
        }

        int[] sortedArr = (int[])arr.Clone();
        int[] sortedBrr = (int[])brr.Clone();
        Array.Sort(sortedArr);
        Array.Sort(sortedBrr);

        long sortedDiff = 0;
        for (int i = 0; i < n; i++) {
            sortedDiff += Math.Abs((long)sortedArr[i] - (long)sortedBrr[i]);
        }

        long withOperation = k + sortedDiff;
        return Math.Min(originalDiff, withOperation);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number[]} brr
 * @param {number} k
 * @return {number}
 */
var minCost = function(arr, brr, k) {
    const n = arr.length;
    let direct = 0;
    for (let i = 0; i < n; ++i) {
        direct += Math.abs(arr[i] - brr[i]);
    }
    
    const aSorted = arr.slice().sort((x, y) => x - y);
    const bSorted = brr.slice().sort((x, y) => x - y);
    let sortedDiff = 0;
    for (let i = 0; i < n; ++i) {
        sortedDiff += Math.abs(aSorted[i] - bSorted[i]);
    }
    
    return Math.min(direct, k + sortedDiff);
};
```

## Typescript

```typescript
function minCost(arr: number[], brr: number[], k: number): number {
    const n = arr.length;
    let direct = 0;
    for (let i = 0; i < n; i++) {
        direct += Math.abs(arr[i] - brr[i]);
    }
    const sortedArr = [...arr].sort((a, b) => a - b);
    const sortedBrr = [...brr].sort((a, b) => a - b);
    let rearranged = 0;
    for (let i = 0; i < n; i++) {
        rearranged += Math.abs(sortedArr[i] - sortedBrr[i]);
    }
    return Math.min(direct, rearranged + k);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[] $brr
     * @param Integer $k
     * @return Integer
     */
    function minCost($arr, $brr, $k) {
        $n = count($arr);
        $sumOriginal = 0;
        for ($i = 0; $i < $n; ++$i) {
            $sumOriginal += abs($arr[$i] - $brr[$i]);
        }

        $sortedArr = $arr;
        $sortedBrr = $brr;
        sort($sortedArr, SORT_NUMERIC);
        sort($sortedBrr, SORT_NUMERIC);

        $sumSorted = 0;
        for ($i = 0; $i < $n; ++$i) {
            $sumSorted += abs($sortedArr[$i] - $sortedBrr[$i]);
        }

        $costWithOperation = $sumSorted + $k;

        return min($sumOriginal, $costWithOperation);
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ arr: [Int], _ brr: [Int], _ k: Int) -> Int {
        let n = arr.count
        var direct: Int64 = 0
        for i in 0..<n {
            direct += Int64(abs(arr[i] - brr[i]))
        }
        
        let sortedArr = arr.sorted()
        let sortedBrr = brr.sorted()
        var sortedDiff: Int64 = 0
        for i in 0..<n {
            sortedDiff += Int64(abs(sortedArr[i] - sortedBrr[i]))
        }
        
        let totalWithOp = sortedDiff + Int64(k)
        let result = min(direct, totalWithOp)
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(arr: IntArray, brr: IntArray, k: Long): Long {
        val n = arr.size
        var originalSum = 0L
        for (i in 0 until n) {
            originalSum += kotlin.math.abs(arr[i] - brr[i]).toLong()
        }
        val sortedArr = arr.clone()
        val sortedBrr = brr.clone()
        java.util.Arrays.sort(sortedArr)
        java.util.Arrays.sort(sortedBrr)
        var sortedSum = 0L
        for (i in 0 until n) {
            sortedSum += kotlin.math.abs(sortedArr[i] - sortedBrr[i]).toLong()
        }
        val costWithRearrange = k + sortedSum
        return if (originalSum < costWithRearrange) originalSum else costWithRearrange
    }
}
```

## Dart

```dart
class Solution {
  int minCost(List<int> arr, List<int> brr, int k) {
    int n = arr.length;
    int original = 0;
    for (int i = 0; i < n; i++) {
      original += (arr[i] - brr[i]).abs();
    }
    List<int> aSorted = List.from(arr);
    List<int> bSorted = List.from(brr);
    aSorted.sort();
    bSorted.sort();
    int sortedCost = 0;
    for (int i = 0; i < n; i++) {
      sortedCost += (aSorted[i] - bSorted[i]).abs();
    }
    int withOperation = sortedCost + k;
    return original < withOperation ? original : withOperation;
  }
}
```

## Golang

```go
func minCost(arr []int, brr []int, k int64) int64 {
	n := len(arr)
	var sumOrig int64
	for i := 0; i < n; i++ {
		diff := int64(arr[i]) - int64(brr[i])
		if diff < 0 {
			diff = -diff
		}
		sumOrig += diff
	}

	a := make([]int, n)
	b := make([]int, n)
	copy(a, arr)
	copy(b, brr)
	sort.Ints(a)
	sort.Ints(b)

	var sumSorted int64
	for i := 0; i < n; i++ {
		diff := int64(a[i]) - int64(b[i])
		if diff < 0 {
			diff = -diff
		}
		sumSorted += diff
	}

	totalWithOp := k + sumSorted
	if sumOrig < totalWithOp {
		return sumOrig
	}
	return totalWithOp
}
```

## Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer[]} brr
# @param {Integer} k
# @return {Integer}
def min_cost(arr, brr, k)
  direct = 0
  n = arr.length
  i = 0
  while i < n
    direct += (arr[i] - brr[i]).abs
    i += 1
  end

  sorted_arr = arr.sort
  sorted_brr = brr.sort
  sorted_sum = 0
  i = 0
  while i < n
    sorted_sum += (sorted_arr[i] - sorted_brr[i]).abs
    i += 1
  end

  [direct, k + sorted_sum].min
end
```

## Scala

```scala
object Solution {
  def minCost(arr: Array[Int], brr: Array[Int], k: Long): Long = {
    val n = arr.length
    var sumOrig: Long = 0L
    var i = 0
    while (i < n) {
      sumOrig += math.abs(arr(i).toLong - brr(i).toLong)
      i += 1
    }

    val sortedArr = arr.clone()
    val sortedBrr = brr.clone()
    java.util.Arrays.sort(sortedArr)
    java.util.Arrays.sort(sortedBrr)

    var sumSorted: Long = 0L
    i = 0
    while (i < n) {
      sumSorted += math.abs(sortedArr(i).toLong - sortedBrr(i).toLong)
      i += 1
    }

    Math.min(sumOrig, k + sumSorted)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(arr: Vec<i32>, brr: Vec<i32>, k: i64) -> i64 {
        let n = arr.len();
        // Cost without using the rearrangement operation
        let mut cost_no_op: i64 = 0;
        for i in 0..n {
            cost_no_op += (arr[i] as i64 - brr[i] as i64).abs();
        }

        // Cost when we use the rearrangement operation once (cost k)
        let mut a = arr.clone();
        let mut b = brr.clone();
        a.sort_unstable();
        b.sort_unstable();

        let mut cost_with_op: i64 = 0;
        for i in 0..n {
            cost_with_op += (a[i] as i64 - b[i] as i64).abs();
        }
        cost_with_op += k;

        std::cmp::min(cost_no_op, cost_with_op)
    }
}
```

## Racket

```racket
(define/contract (min-cost arr brr k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sum1 (apply + (map (lambda (a b) (abs (- a b))) arr brr)))
         (sarr (sort arr <))
         (sbrr (sort brr <))
         (sum2 (+ k (apply + (map (lambda (a b) (abs (- a b))) sarr sbrr)))))
    (if (< sum1 sum2) sum1 sum2)))
```

## Erlang

```erlang
-spec min_cost(Arr :: [integer()], Brr :: [integer()], K :: integer()) -> integer().
min_cost(Arr, Brr, K) ->
    Original = sum_abs_diff(Arr, Brr),
    SortedArr = lists:sort(Arr),
    SortedBrr = lists:sort(Brr),
    SortedDiff = sum_abs_diff(SortedArr, SortedBrr),
    min(Original, SortedDiff + K).

sum_abs_diff([], []) -> 0;
sum_abs_diff([H|T], [H2|T2]) ->
    erlang:abs(H - H2) + sum_abs_diff(T, T2).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(arr :: [integer], brr :: [integer], k :: integer) :: integer
  def min_cost(arr, brr, k) do
    cost_no =
      Enum.zip(arr, brr)
      |> Enum.reduce(0, fn {a, b}, acc -> acc + abs(a - b) end)

    sorted_arr = Enum.sort(arr)
    sorted_brr = Enum.sort(brr)

    cost_sort =
      Enum.zip(sorted_arr, sorted_brr)
      |> Enum.reduce(0, fn {a, b}, acc -> acc + abs(a - b) end)

    min(cost_no, k + cost_sort)
  end
end
```

# 2009. Minimum Number of Operations to Make Array Continuous

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        nums.erase(unique(nums.begin(), nums.end()), nums.end()); // remove duplicates
        int m = nums.size();
        int ans = n;
        int j = 0;
        for (int i = 0; i < m; ++i) {
            while (j < m && nums[j] < nums[i] + n) {
                ++j;
            }
            int cnt = j - i; // elements already in the desired range
            ans = min(ans, n - cnt);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int num : nums) set.add(num);
        int m = set.size();
        int[] uniq = new int[m];
        int idx = 0;
        for (int val : set) {
            uniq[idx++] = val;
        }
        java.util.Arrays.sort(uniq);
        int ans = n;
        int j = 0;
        for (int i = 0; i < m; i++) {
            while (j < m && uniq[j] - uniq[i] < n) {
                j++;
            }
            int count = j - i;
            ans = Math.min(ans, n - count);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr = sorted(set(nums))
        m = len(arr)
        ans = n  # worst case: replace all elements
        j = 0
        for i in range(m):
            while j < m and arr[j] < arr[i] + n:
                j += 1
            count = j - i
            ops = n - count
            if ops < ans:
                ans = ops
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(set(nums))
        m = len(arr)
        ans = n
        j = 0
        for i in range(m):
            while j < m and arr[j] - arr[i] <= n - 1:
                j += 1
            count = j - i
            ops = n - count
            if ops < ans:
                ans = ops
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int minOperations(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    /* Copy and sort the array */
    int *sorted = (int *)malloc(numsSize * sizeof(int));
    memcpy(sorted, nums, numsSize * sizeof(int));
    qsort(sorted, numsSize, sizeof(int), cmp_int);

    /* Remove duplicates */
    int *uniq = (int *)malloc(numsSize * sizeof(int));
    int uniqCount = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || sorted[i] != sorted[i - 1]) {
            uniq[uniqCount++] = sorted[i];
        }
    }
    free(sorted);

    /* Sliding window to find maximum keepable elements */
    int maxKeep = 0;
    int j = 0;
    for (int i = 0; i < uniqCount; ++i) {
        while (j < uniqCount && (long long)uniq[j] < (long long)uniq[i] + numsSize) {
            ++j;
        }
        int cnt = j - i;
        if (cnt > maxKeep) maxKeep = cnt;
    }

    free(uniq);
    return numsSize - maxKeep;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        // Remove duplicates
        var uniqueList = new List<int>(new HashSet<int>(nums));
        uniqueList.Sort();
        int m = uniqueList.Count;
        int ans = n; // worst case: replace all elements
        
        int j = 0;
        for (int i = 0; i < m; i++) {
            while (j < m && uniqueList[j] < uniqueList[i] + n) {
                j++;
            }
            int countInRange = j - i; // number of distinct numbers already fitting the window
            ans = Math.Min(ans, n - countInRange);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;
    // Remove duplicates and sort
    const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
    
    let ans = n; // worst case: replace all elements
    let j = 0;
    
    for (let i = 0; i < uniq.length; i++) {
        while (j < uniq.length && uniq[j] < uniq[i] + n) {
            j++;
        }
        const countInRange = j - i; // elements already fitting the window
        ans = Math.min(ans, n - countInRange);
    }
    
    return ans;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    const n = nums.length;
    const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
    let ans = n;
    let j = 0;
    const m = uniq.length;
    for (let i = 0; i < m; i++) {
        while (j < m && uniq[j] < uniq[i] + n) {
            j++;
        }
        const count = j - i;
        ans = Math.min(ans, n - count);
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
    function minOperations($nums) {
        $n = count($nums);
        // Remove duplicates and sort
        $unique = array_values(array_unique($nums));
        sort($unique, SORT_NUMERIC);
        $m = count($unique);
        $ans = $n;
        $j = 0;
        for ($i = 0; $i < $m; $i++) {
            while ($j < $m && $unique[$j] < $unique[$i] + $n) {
                $j++;
            }
            $count = $j - $i; // elements already in the desired range
            $ops = $n - $count;
            if ($ops < $ans) {
                $ans = $ops;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        var unique = Array(Set(nums))
        unique.sort()
        var ans = n
        var j = 0
        for i in 0..<unique.count {
            while j < unique.count && unique[j] - unique[i] < n {
                j += 1
            }
            let count = j - i
            ans = min(ans, n - count)
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray): Int {
        val n = nums.size
        // Remove duplicates and sort
        val uniq = nums.toSet().toIntArray()
        uniq.sort()
        var ans = n
        var j = 0
        val m = uniq.size
        for (i in 0 until m) {
            while (j < m && uniq[j] < uniq[i] + n) {
                j++
            }
            val countInRange = j - i
            val opsNeeded = n - countInRange
            if (opsNeeded < ans) ans = opsNeeded
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    int n = nums.length;
    // Remove duplicates
    var uniqueSet = <int>{};
    for (var v in nums) {
      uniqueSet.add(v);
    }
    var uniq = uniqueSet.toList();
    uniq.sort();

    int ans = n; // worst case: replace all elements
    int j = 0;
    for (int i = 0; i < uniq.length; ++i) {
      while (j < uniq.length && uniq[j] - uniq[i] < n) {
        j++;
      }
      int countInRange = j - i;
      int opsNeeded = n - countInRange;
      if (opsNeeded < ans) ans = opsNeeded;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func minOperations(nums []int) int {
    n := len(nums)
    // Remove duplicates
    seen := make(map[int]struct{}, n)
    uniq := make([]int, 0, n)
    for _, v := range nums {
        if _, ok := seen[v]; !ok {
            seen[v] = struct{}{}
            uniq = append(uniq, v)
        }
    }
    sort.Ints(uniq)

    ans := n
    m := len(uniq)
    j := 0
    for i := 0; i < m; i++ {
        // expand window to include numbers less than left + n
        limit := uniq[i] + n
        for j < m && uniq[j] < limit {
            j++
        }
        count := j - i
        ops := n - count
        if ops < ans {
            ans = ops
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_operations(nums)
  n = nums.length
  uniq_sorted = nums.uniq.sort
  m = uniq_sorted.length
  ans = n
  j = 0

  (0...m).each do |i|
    while j < m && uniq_sorted[j] < uniq_sorted[i] + n
      j += 1
    end
    count_in_range = j - i
    ops_needed = n - count_in_range
    ans = ops_needed if ops_needed < ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        val n = nums.length
        val sorted = nums.distinct.sorted
        var ans = n
        var j = 0
        val m = sorted.length
        for (i <- 0 until m) {
            while (j < m && sorted(j).toLong < sorted(i).toLong + n) {
                j += 1
            }
            val count = j - i
            ans = math.min(ans, n - count)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        use std::collections::HashSet;
        // Deduplicate and convert to i64 for safe arithmetic
        let mut set = HashSet::with_capacity(n);
        for &x in &nums {
            set.insert(x as i64);
        }
        let mut uniq: Vec<i64> = set.into_iter().collect();
        uniq.sort_unstable();

        let m = uniq.len();
        let mut ans = n as i32;
        let mut j = 0usize;
        let window_len = n as i64; // length of the continuous range

        for i in 0..m {
            while j < m && uniq[j] < uniq[i] + window_len {
                j += 1;
            }
            let count = j - i; // number of distinct elements already fitting
            let ops = n - count;
            if (ops as i32) < ans {
                ans = ops as i32;
            }
        }
        ans
    }
}
```

## Racket

```racket
#lang racket
(require racket/set)

(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (uniq (sort (set->list (list->set nums)) <)))
    (let* ((arr (list->vector uniq))
           (m (vector-length arr)))
      (let ([ans n]
            [j 0])
        (for ([i (in-range m)])
          (when (< j i) (set! j i))
          ;; advance j while within the window of size n
          (let loop ((jj j))
            (if (and (< jj m)
                     (< (vector-ref arr jj) (+ (vector-ref arr i) n)))
                (begin
                  (set! j (add1 jj))
                  (loop (add1 jj)))
                (void)))
          (let ([cnt (- j i)])
            (when (< (- n cnt) ans)
              (set! ans (- n cnt)))))
        ans))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    N = length(Nums),
    SortedUnique = lists:usort(Nums),
    Tuple = list_to_tuple(SortedUnique),
    L = tuple_size(Tuple),
    loop(0, 0, N, L, Tuple, N).

loop(I, J, _N, L, _Tuple, Ans) when I >= L ->
    Ans;
loop(I, J, N, L, Tuple, Ans) ->
    NewJ = expand(J, I, N, L, Tuple),
    Count = NewJ - I,
    Ops = N - Count,
    NewAns = if Ops < Ans -> Ops; true -> Ans end,
    loop(I + 1, NewJ, N, L, Tuple, NewAns).

expand(J, I, N, L, Tuple) ->
    case J < L of
        true ->
            ValI = element(I + 1, Tuple),
            ValJ = element(J + 1, Tuple),
            if ValJ < ValI + N ->
                    expand(J + 1, I, N, L, Tuple);
               true -> J
            end;
        false -> J
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    n = length(nums)

    uniq_sorted =
      nums
      |> Enum.uniq()
      |> Enum.sort()

    arr = List.to_tuple(uniq_sorted)
    len = tuple_size(arr)

    {ans, _} =
      0..(len - 1)
      |> Enum.reduce({n, 0}, fn i, {best, j_start} ->
        j = if j_start < i, do: i, else: j_start
        j = advance_j(arr, len, i, j, n)
        count = j - i
        new_best = min(best, n - count)
        {new_best, j}
      end)

    ans
  end

  defp advance_j(arr, len, i, j, n) do
    if j < len and elem(arr, j) < elem(arr, i) + n do
      advance_j(arr, len, i, j + 1, n)
    else
      j
    end
  end
end
```

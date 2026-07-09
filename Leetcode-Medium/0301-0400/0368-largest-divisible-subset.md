# 0368. Largest Divisible Subset

## Cpp

```cpp
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        if (nums.empty()) return {};
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> dp(n, 1), parent(n, -1);
        int maxSize = 1, maxIdx = 0;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            }
            if (dp[i] > maxSize) {
                maxSize = dp[i];
                maxIdx = i;
            }
        }
        vector<int> result;
        for (int i = maxIdx; i != -1; i = parent[i]) {
            result.push_back(nums[i]);
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> largestDivisibleSubset(int[] nums) {
        int n = nums.length;
        java.util.Arrays.sort(nums);
        int[] dp = new int[n];
        int[] parent = new int[n];
        int maxSize = 0, maxIdx = -1;
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            parent[i] = -1;
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            }
            if (dp[i] > maxSize) {
                maxSize = dp[i];
                maxIdx = i;
            }
        }
        java.util.LinkedList<Integer> result = new java.util.LinkedList<>();
        while (maxIdx != -1) {
            result.addFirst(nums[maxIdx]);
            maxIdx = parent[maxIdx];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        max_len = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = parent[max_idx]
        return res[::-1]
```

## Python3

```python
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_idx = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]
        return res[::-1]
```

## C

```c
#include <stdlib.h>

/* Comparison function for qsort */
static int cmp_int(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* largestDivisibleSubset(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    /* Sort the numbers to ensure divisibility checks only need to look backwards */
    qsort(nums, numsSize, sizeof(int), cmp_int);

    int *dp = (int *)malloc(numsSize * sizeof(int));
    int *parent = (int *)malloc(numsSize * sizeof(int));

    int maxSize = 1;
    int maxIndex = 0;

    for (int i = 0; i < numsSize; ++i) {
        dp[i] = 1;
        parent[i] = -1;
        for (int j = 0; j < i; ++j) {
            if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                parent[i] = j;
            }
        }
        if (dp[i] > maxSize) {
            maxSize = dp[i];
            maxIndex = i;
        }
    }

    int *result = (int *)malloc(maxSize * sizeof(int));
    int pos = maxSize - 1;
    int idx = maxIndex;
    while (idx != -1) {
        result[pos--] = nums[idx];
        idx = parent[idx];
    }

    free(dp);
    free(parent);

    *returnSize = maxSize;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> LargestDivisibleSubset(int[] nums) {
        if (nums == null || nums.Length == 0) return new List<int>();
        Array.Sort(nums);
        int n = nums.Length;
        int[] dp = new int[n];
        int[] parent = new int[n];
        int maxLen = 0, maxIdx = 0;

        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            parent[i] = -1;
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            }
            if (dp[i] > maxLen) {
                maxLen = dp[i];
                maxIdx = i;
            }
        }

        List<int> result = new List<int>();
        int cur = maxIdx;
        while (cur != -1) {
            result.Add(nums[cur]);
            cur = parent[cur];
        }
        result.Reverse();
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var largestDivisibleSubset = function(nums) {
    if (!nums || nums.length === 0) return [];
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const dp = new Array(n).fill(1);
    const parent = new Array(n).fill(-1);
    let maxSize = 1, maxIndex = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] % nums[j] === 0 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                parent[i] = j;
            }
        }
        if (dp[i] > maxSize) {
            maxSize = dp[i];
            maxIndex = i;
        }
    }

    const result = [];
    let k = maxIndex;
    while (k !== -1) {
        result.push(nums[k]);
        k = parent[k];
    }
    return result.reverse();
};
```

## Typescript

```typescript
function largestDivisibleSubset(nums: number[]): number[] {
    const n = nums.length;
    if (n === 0) return [];
    const sorted = [...nums].sort((a, b) => a - b);
    const dp = new Array(n).fill(1);
    const parent = new Array(n).fill(-1);
    let maxSize = 1;
    let maxIdx = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (sorted[i] % sorted[j] === 0 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                parent[i] = j;
            }
        }
        if (dp[i] > maxSize) {
            maxSize = dp[i];
            maxIdx = i;
        }
    }

    const result: number[] = [];
    while (maxIdx !== -1) {
        result.push(sorted[maxIdx]);
        maxIdx = parent[maxIdx];
    }
    result.reverse();
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function largestDivisibleSubset($nums) {
        $n = count($nums);
        if ($n == 0) {
            return [];
        }
        sort($nums, SORT_NUMERIC);
        $dp = array_fill(0, $n, 1);
        $prev = array_fill(0, $n, -1);
        $maxSize = 1;
        $maxIdx = 0;

        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ($nums[$i] % $nums[$j] == 0 && $dp[$j] + 1 > $dp[$i]) {
                    $dp[$i] = $dp[$j] + 1;
                    $prev[$i] = $j;
                }
            }
            if ($dp[$i] > $maxSize) {
                $maxSize = $dp[$i];
                $maxIdx = $i;
            }
        }

        $result = [];
        while ($maxIdx != -1) {
            $result[] = $nums[$maxIdx];
            $maxIdx = $prev[$maxIdx];
        }
        return array_reverse($result);
    }
}
```

## Swift

```swift
class Solution {
    func largestDivisibleSubset(_ nums: [Int]) -> [Int] {
        if nums.isEmpty { return [] }
        let sorted = nums.sorted()
        let n = sorted.count
        var dp = Array(repeating: 1, count: n)
        var prev = Array(repeating: -1, count: n)
        var maxIdx = 0
        
        for i in 0..<n {
            for j in 0..<i {
                if sorted[i] % sorted[j] == 0 && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1
                    prev[i] = j
                }
            }
            if dp[i] > dp[maxIdx] {
                maxIdx = i
            }
        }
        
        var result: [Int] = []
        var idx = maxIdx
        while idx != -1 {
            result.append(sorted[idx])
            idx = prev[idx]
        }
        return result.reversed()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestDivisibleSubset(nums: IntArray): List<Int> {
        if (nums.isEmpty()) return emptyList()
        val sorted = nums.sorted()
        val n = sorted.size
        val dp = IntArray(n) { 1 }
        val parent = IntArray(n) { -1 }
        var maxIdx = 0
        for (i in 0 until n) {
            for (j in 0 until i) {
                if (sorted[i] % sorted[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1
                    parent[i] = j
                }
            }
            if (dp[i] > dp[maxIdx]) {
                maxIdx = i
            }
        }
        val result = mutableListOf<Int>()
        var cur = maxIdx
        while (cur != -1) {
            result.add(sorted[cur])
            cur = parent[cur]
        }
        result.reverse()
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> largestDivisibleSubset(List<int> nums) {
    if (nums.isEmpty) return [];
    nums.sort();
    int n = nums.length;
    List<int> dp = List.filled(n, 1);
    List<int> parent = List.filled(n, -1);
    int maxSize = 1;
    int maxIdx = 0;

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < i; ++j) {
        if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
          dp[i] = dp[j] + 1;
          parent[i] = j;
        }
      }
      if (dp[i] > maxSize) {
        maxSize = dp[i];
        maxIdx = i;
      }
    }

    List<int> result = [];
    int k = maxIdx;
    while (k != -1) {
      result.add(nums[k]);
      k = parent[k];
    }
    return result.reversed.toList();
  }
}
```

## Golang

```go
package main

import "sort"

func largestDivisibleSubset(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	sort.Ints(nums)
	n := len(nums)
	dp := make([]int, n)      // length of subset ending at i
	prev := make([]int, n)    // previous index in subset
	for i := range dp {
		dp[i] = 1
		prev[i] = -1
	}
	maxIdx := 0
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if nums[i]%nums[j] == 0 && dp[j]+1 > dp[i] {
				dp[i] = dp[j] + 1
				prev[i] = j
			}
		}
		if dp[i] > dp[maxIdx] {
			maxIdx = i
		}
	}
	// reconstruct subset
	res := []int{}
	for idx := maxIdx; idx != -1; idx = prev[idx] {
		res = append(res, nums[idx])
	}
	// reverse to get ascending order
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return res
}
```

## Ruby

```ruby
def largest_divisible_subset(nums)
  return [] if nums.empty?
  nums.sort!
  n = nums.length
  dp = Array.new(n, 1)
  parent = Array.new(n, -1)

  max_len = 1
  max_idx = 0

  (0...n).each do |i|
    (0...i).each do |j|
      if nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]
        dp[i] = dp[j] + 1
        parent[i] = j
      end
    end
    if dp[i] > max_len
      max_len = dp[i]
      max_idx = i
    end
  end

  result = []
  while max_idx != -1
    result << nums[max_idx]
    max_idx = parent[max_idx]
  end
  result.reverse
end
```

## Scala

```scala
object Solution {
    def largestDivisibleSubset(nums: Array[Int]): List[Int] = {
        if (nums.isEmpty) return Nil
        val sorted = nums.sorted
        val n = sorted.length
        val dp = Array.fill(n)(1)
        val parent = Array.fill(n)(-1)

        var maxSize = 1
        var maxIdx = 0

        for (i <- 0 until n) {
            for (j <- 0 until i) {
                if (sorted(i) % sorted(j) == 0 && dp(j) + 1 > dp(i)) {
                    dp(i) = dp(j) + 1
                    parent(i) = j
                }
            }
            if (dp(i) > maxSize) {
                maxSize = dp(i)
                maxIdx = i
            }
        }

        var result: List[Int] = Nil
        var cur = maxIdx
        while (cur != -1) {
            result = sorted(cur) :: result
            cur = parent(cur)
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_divisible_subset(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![];
        }
        let mut sorted = nums.clone();
        sorted.sort();

        let mut dp = vec![1usize; n];
        let mut parent: Vec<Option<usize>> = vec![None; n];

        for i in 0..n {
            for j in 0..i {
                if sorted[i] % sorted[j] == 0 && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1;
                    parent[i] = Some(j);
                }
            }
        }

        let mut max_idx = 0usize;
        for i in 1..n {
            if dp[i] > dp[max_idx] {
                max_idx = i;
            }
        }

        let mut res: Vec<i32> = Vec::new();
        let mut cur = Some(max_idx);
        while let Some(idx) = cur {
            res.push(sorted[idx]);
            cur = parent[idx];
        }
        res.reverse();
        res
    }
}
```

## Racket

```racket
(define/contract (largest-divisible-subset nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([sorted (sort nums <)]
         [n (length sorted)])
    (if (= n 0)
        '()
        (let* ([arr (list->vector sorted)]
               [dp (make-vector n 1)]
               [parent (make-vector n -1)]
               [max-idx
                (let loop ((i 0) (best 0))
                  (if (>= i n)
                      best
                      (begin
                        (for ([j (in-range i)])
                          (when (= (remainder (vector-ref arr i) (vector-ref arr j)) 0)
                            (when (> (+ (vector-ref dp j) 1) (vector-ref dp i))
                              (vector-set! dp i (+ (vector-ref dp j) 1))
                              (vector-set! parent i j))))
                        (let ([best (if (> (vector-ref dp i) (vector-ref dp best)) i best)])
                          (loop (+ i 1) best)))))]
               [result
                (let loop ((idx max-idx) (acc '()))
                  (if (= idx -1)
                      acc
                      (loop (vector-ref parent idx) (cons (vector-ref arr idx) acc))))])
          result))))
```

## Erlang

```erlang
-module(solution).
-export([largest_divisible_subset/1]).

-spec largest_divisible_subset(Nums :: [integer()]) -> [integer()].
largest_divisible_subset(Nums) ->
    Sorted = lists:sort(Nums),
    SortedT = list_to_tuple(Sorted),
    N = length(Sorted),
    DP0 = erlang:make_tuple(N, 1),
    Parent0 = erlang:make_tuple(N, 0),
    {_, ParentFinal, MaxIdx} = loop_i(2, N, SortedT, DP0, Parent0),
    reconstruct(MaxIdx, SortedT, ParentFinal, []).

loop_i(I, N, _SortedT, DP, Parent) when I > N ->
    MaxIdx = find_max(DP, N, 1, 1, element(1, DP)),
    {DP, Parent, MaxIdx};
loop_i(I, N, SortedT, DP, Parent) ->
    Ai = element(I, SortedT),
    {MaxLen, MaxPrev} = loop_j(1, I - 1, SortedT, DP, 1, 0, Ai),
    DP2 = setelement(I, DP, MaxLen),
    Parent2 = setelement(I, Parent, MaxPrev),
    loop_i(I + 1, N, SortedT, DP2, Parent2).

loop_j(J, End, _SortedT, _DP, CurMaxLen, CurPrev, _Ai) when J > End ->
    {CurMaxLen, CurPrev};
loop_j(J, End, SortedT, DP, CurMaxLen, CurPrev, Ai) ->
    Aj = element(J, SortedT),
    LenJ = element(J, DP),
    if (Ai rem Aj == 0) andalso (LenJ + 1 > CurMaxLen) ->
            loop_j(J + 1, End, SortedT, DP, LenJ + 1, J, Ai);
       true ->
            loop_j(J + 1, End, SortedT, DP, CurMaxLen, CurPrev, Ai)
    end.

find_max(_DP, N, I, BestIdx, _BestLen) when I > N ->
    BestIdx;
find_max(DP, N, I, BestIdx, BestLen) ->
    Len = element(I, DP),
    if Len > BestLen ->
            find_max(DP, N, I + 1, I, Len);
       true ->
            find_max(DP, N, I + 1, BestIdx, BestLen)
    end.

reconstruct(0, _SortedT, _Parent, Acc) ->
    lists:reverse(Acc);
reconstruct(Index, SortedT, Parent, Acc) ->
    Val = element(Index, SortedT),
    Prev = element(Index, Parent),
    reconstruct(Prev, SortedT, Parent, [Val | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_divisible_subset(nums :: [integer]) :: [integer]
  def largest_divisible_subset(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)

    {_, prev, best_idx, _} =
      Enum.reduce(0..(n - 1), {%{}, %{}, -1, 0}, fn i,
                                                   {dp_acc, prev_acc, b_idx, b_len} ->
        max_len = 1
        prev_i = -1

        {max_len, prev_i} =
          Enum.reduce(0..(i - 1), {max_len, prev_i}, fn j,
                                                       {cur_max, cur_prev} ->
            if rem(Enum.at(sorted, i), Enum.at(sorted, j)) == 0 do
              len_j = Map.get(dp_acc, j)
              if len_j + 1 > cur_max do
                {len_j + 1, j}
              else
                {cur_max, cur_prev}
              end
            else
              {cur_max, cur_prev}
            end
          end)

        dp_new = Map.put(dp_acc, i, max_len)
        prev_new = Map.put(prev_acc, i, prev_i)

        if max_len > b_len do
          {dp_new, prev_new, i, max_len}
        else
          {dp_new, prev_new, b_idx, b_len}
        end
      end)

    build_result(sorted, prev, best_idx, [])
  end

  defp build_result(_sorted, _prev, -1, acc), do: acc

  defp build_result(sorted, prev, idx, acc) do
    val = Enum.at(sorted, idx)
    next_idx = Map.get(prev, idx, -1)
    build_result(sorted, prev, next_idx, [val | acc])
  end
end
```

# 2670. Find the Distinct Difference Array

## Cpp

```cpp
class Solution {
public:
    vector<int> distinctDifferenceArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> suffDist(n);
        unordered_set<int> s;
        for (int i = n - 1; i >= 0; --i) {
            s.insert(nums[i]);
            suffDist[i] = s.size();
        }
        vector<int> ans(n);
        unordered_set<int> prefSet;
        for (int i = 0; i < n; ++i) {
            prefSet.insert(nums[i]);
            int prefixCnt = prefSet.size();
            int suffixCnt = (i + 1 < n) ? suffDist[i + 1] : 0;
            ans[i] = prefixCnt - suffixCnt;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] distinctDifferenceArray(int[] nums) {
        int n = nums.length;
        int[] prefixDistinct = new int[n];
        java.util.HashSet<Integer> prefSet = new java.util.HashSet<>();
        for (int i = 0; i < n; i++) {
            prefSet.add(nums[i]);
            prefixDistinct[i] = prefSet.size();
        }
        int[] suffixAfterDistinct = new int[n];
        java.util.HashSet<Integer> suffSet = new java.util.HashSet<>();
        for (int i = n - 1; i >= 0; i--) {
            suffixAfterDistinct[i] = suffSet.size(); // distinct elements after index i
            suffSet.add(nums[i]);
        }
        int[] diff = new int[n];
        for (int i = 0; i < n; i++) {
            diff[i] = prefixDistinct[i] - suffixAfterDistinct[i];
        }
        return diff;
    }
}
```

## Python

```python
class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pref_counts = [0] * n
        suff_counts = [0] * n

        seen = set()
        for i in range(n):
            seen.add(nums[i])
            pref_counts[i] = len(seen)

        seen.clear()
        for i in range(n - 1, -1, -1):
            suff_counts[i] = len(seen)
            seen.add(nums[i])

        return [pref_counts[i] - suff_counts[i] for i in range(n)]
```

## Python3

```python
from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_distinct = [0] * n
        seen_suffix = set()
        # compute number of distinct elements in suffix after each index
        for i in range(n - 1, -1, -1):
            suffix_distinct[i] = len(seen_suffix)
            seen_suffix.add(nums[i])
        
        result = []
        seen_prefix = set()
        for i in range(n):
            seen_prefix.add(nums[i])
            diff = len(seen_prefix) - suffix_distinct[i]
            result.append(diff)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* distinctDifferenceArray(int* nums, int numsSize, int* returnSize) {
    int *result = (int *)malloc(numsSize * sizeof(int));
    if (!result) return NULL;

    int *suffixDistinct = (int *)malloc(numsSize * sizeof(int));
    bool seen[51] = {false};
    int cnt = 0;
    for (int i = numsSize - 1; i >= 0; --i) {
        suffixDistinct[i] = cnt;
        if (!seen[nums[i]]) {
            seen[nums[i]] = true;
            ++cnt;
        }
    }

    memset(seen, 0, sizeof(seen));
    int prefCnt = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (!seen[nums[i]]) {
            seen[nums[i]] = true;
            ++prefCnt;
        }
        result[i] = prefCnt - suffixDistinct[i];
    }

    free(suffixDistinct);
    *returnSize = numsSize;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] DistinctDifferenceArray(int[] nums) {
        int n = nums.Length;
        int[] prefixDistinct = new int[n];
        var seenPrefix = new HashSet<int>();
        for (int i = 0; i < n; i++) {
            seenPrefix.Add(nums[i]);
            prefixDistinct[i] = seenPrefix.Count;
        }

        int[] suffixDistinct = new int[n];
        var seenSuffix = new HashSet<int>();
        for (int i = n - 1; i >= 0; i--) {
            seenSuffix.Add(nums[i]);
            suffixDistinct[i] = seenSuffix.Count;
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int suffixCount = (i + 1 < n) ? suffixDistinct[i + 1] : 0;
            result[i] = prefixDistinct[i] - suffixCount;
        }
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
var distinctDifferenceArray = function(nums) {
    const n = nums.length;
    const prefix = new Array(n);
    const seenPref = new Set();
    for (let i = 0; i < n; i++) {
        seenPref.add(nums[i]);
        prefix[i] = seenPref.size;
    }
    const suffix = new Array(n);
    const seenSuf = new Set();
    for (let i = n - 1; i >= 0; i--) {
        seenSuf.add(nums[i]);
        suffix[i] = seenSuf.size;
    }
    const diff = new Array(n);
    for (let i = 0; i < n; i++) {
        const pre = prefix[i];
        const suf = i + 1 < n ? suffix[i + 1] : 0;
        diff[i] = pre - suf;
    }
    return diff;
};
```

## Typescript

```typescript
function distinctDifferenceArray(nums: number[]): number[] {
    const n = nums.length;
    const prefixDistinct: number[] = new Array(n);
    const seenPrefix = new Set<number>();
    for (let i = 0; i < n; i++) {
        seenPrefix.add(nums[i]);
        prefixDistinct[i] = seenPrefix.size;
    }

    const suffixAfterDistinct: number[] = new Array(n);
    const seenSuffix = new Set<number>();
    for (let i = n - 1; i >= 0; i--) {
        // distinct elements strictly after index i
        suffixAfterDistinct[i] = seenSuffix.size;
        seenSuffix.add(nums[i]);
    }

    const result: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        result[i] = prefixDistinct[i] - suffixAfterDistinct[i];
    }
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
    function distinctDifferenceArray($nums) {
        $n = count($nums);
        $prefixCounts = array_fill(0, $n, 0);
        $suffixCounts = array_fill(0, $n, 0);

        // Prefix distinct counts
        $seen = [];
        for ($i = 0; $i < $n; $i++) {
            $seen[$nums[$i]] = true;
            $prefixCounts[$i] = count($seen);
        }

        // Suffix distinct counts (including current index)
        $seen = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            $seen[$nums[$i]] = true;
            $suffixCounts[$i] = count($seen);
        }

        // Build result: prefix[i] - suffix[i+1]
        $result = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $suffix = ($i + 1 < $n) ? $suffixCounts[$i + 1] : 0;
            $result[$i] = $prefixCounts[$i] - $suffix;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func distinctDifferenceArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var prefixDistinct = Array(repeating: 0, count: n)
        var seen = Set<Int>()
        for i in 0..<n {
            seen.insert(nums[i])
            prefixDistinct[i] = seen.count
        }
        
        var suffixDistinct = Array(repeating: 0, count: n + 1) // extra slot for empty suffix
        seen.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            seen.insert(nums[i])
            suffixDistinct[i] = seen.count
        }
        
        var result = [Int]()
        result.reserveCapacity(n)
        for i in 0..<n {
            let suffixAfter = (i + 1 < n) ? suffixDistinct[i + 1] : 0
            result.append(prefixDistinct[i] - suffixAfter)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distinctDifferenceArray(nums: IntArray): IntArray {
        val n = nums.size
        val suffixDist = IntArray(n)
        val seenSuffix = HashSet<Int>()
        for (i in n - 1 downTo 0) {
            seenSuffix.add(nums[i])
            suffixDist[i] = seenSuffix.size
        }
        val result = IntArray(n)
        val seenPrefix = HashSet<Int>()
        for (i in 0 until n) {
            seenPrefix.add(nums[i])
            val prefixCount = seenPrefix.size
            val suffixAfter = if (i + 1 < n) suffixDist[i + 1] else 0
            result[i] = prefixCount - suffixAfter
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> distinctDifferenceArray(List<int> nums) {
    int n = nums.length;
    List<int> prefixDistinct = List.filled(n, 0);
    Set<int> seenPrefix = {};
    for (int i = 0; i < n; i++) {
      seenPrefix.add(nums[i]);
      prefixDistinct[i] = seenPrefix.length;
    }

    List<int> suffixAfterDistinct = List.filled(n, 0);
    Set<int> seenSuffix = {};
    for (int i = n - 1; i >= 0; i--) {
      suffixAfterDistinct[i] = seenSuffix.length;
      seenSuffix.add(nums[i]);
    }

    List<int> result = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      result[i] = prefixDistinct[i] - suffixAfterDistinct[i];
    }
    return result;
  }
}
```

## Golang

```go
func distinctDifferenceArray(nums []int) []int {
    n := len(nums)
    suffix := make([]int, n)
    seen := make(map[int]struct{})
    for i := n - 1; i >= 0; i-- {
        suffix[i] = len(seen)
        seen[nums[i]] = struct{}{}
    }
    result := make([]int, n)
    seen = make(map[int]struct{})
    for i := 0; i < n; i++ {
        seen[nums[i]] = struct{}{}
        result[i] = len(seen) - suffix[i]
    }
    return result
}
```

## Ruby

```ruby
def distinct_difference_array(nums)
  n = nums.length
  prefix = Array.new(n, 0)
  seen_prefix = {}
  cnt = 0
  nums.each_with_index do |v, i|
    unless seen_prefix[v]
      seen_prefix[v] = true
      cnt += 1
    end
    prefix[i] = cnt
  end

  suffix = Array.new(n, 0)
  seen_suffix = {}
  cnt = 0
  (n - 1).downto(0) do |i|
    v = nums[i]
    unless seen_suffix[v]
      seen_suffix[v] = true
      cnt += 1
    end
    suffix[i] = cnt
  end

  result = Array.new(n)
  n.times do |i|
    suf_distinct = i + 1 < n ? suffix[i + 1] : 0
    result[i] = prefix[i] - suf_distinct
  end
  result
end
```

## Scala

```scala
object Solution {
    def distinctDifferenceArray(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val suffixCount = new Array[Int](n)
        val suffixSet = scala.collection.mutable.HashSet[Int]()
        for (i <- (n - 1) to 0 by -1) {
            suffixSet.add(nums(i))
            suffixCount(i) = suffixSet.size
        }
        val result = new Array[Int](n)
        val prefixSet = scala.collection.mutable.HashSet[Int]()
        for (i <- 0 until n) {
            prefixSet.add(nums(i))
            val prefixDistinct = prefixSet.size
            val suffixAfter = if (i + 1 < n) suffixCount(i + 1) else 0
            result(i) = prefixDistinct - suffixAfter
        }
        result
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn distinct_difference_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut pref = vec![0i32; n];
        let mut seen = HashSet::new();
        for i in 0..n {
            seen.insert(nums[i]);
            pref[i] = seen.len() as i32;
        }
        let mut suff = vec![0i32; n];
        seen.clear();
        for i in (0..n).rev() {
            suff[i] = seen.len() as i32;
            seen.insert(nums[i]);
        }
        let mut diff = Vec::with_capacity(n);
        for i in 0..n {
            diff.push(pref[i] - suff[i]);
        }
        diff
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (distinct-difference-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((i 0) (n (length nums)) (acc '()))
    (if (= i n)
        (reverse acc)
        (let* ((prefix (take nums (add1 i)))
               (suffix (drop nums (add1 i)))
               (pref-dist (length (remove-duplicates prefix)))
               (suf-dist (length (remove-duplicates suffix))))
          (loop (+ i 1) n (cons (- pref-dist suf-dist) acc))))))
```

## Erlang

```erlang
-module(solution).
-export([distinct_difference_array/1]).

-spec distinct_difference_array(Nums :: [integer()]) -> [integer()].
distinct_difference_array(Nums) ->
    SuffixCounts = suffix_counts(Nums),
    DiffRev = diff_list(Nums, SuffixCounts, #{}, []),
    lists:reverse(DiffRev).

suffix_counts(Nums) ->
    suffix_counts_rev(lists:reverse(Nums), #{}, []).

suffix_counts_rev([], _Set, Acc) ->
    lists:reverse(Acc);
suffix_counts_rev([H|T], Set, Acc) ->
    Count = maps:size(Set),
    NewSet = maps:put(H, true, Set),
    suffix_counts_rev(T, NewSet, [Count|Acc]).

diff_list([], [], _PrefixSet, Acc) -> Acc;
diff_list([H|T], [SC|SCTail], PrefixSet, Acc) ->
    NewSet = maps:put(H, true, PrefixSet),
    PC = maps:size(NewSet),
    D = PC - SC,
    diff_list(T, SCTail, NewSet, [D|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec distinct_difference_array(nums :: [integer]) :: [integer]
  def distinct_difference_array(nums) do
    # suffix distinct counts for each index i (elements after i)
    suffix_counts =
      nums
      |> Enum.with_index()
      |> Enum.reverse()
      |> Enum.reduce({MapSet.new(), []}, fn {val, _idx}, {set, acc} ->
        count = MapSet.size(set)
        {MapSet.put(set, val), [count | acc]}
      end)
      |> elem(1)

    suffix_tuple = List.to_tuple(suffix_counts)

    {_prefix_set, rev_res} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({MapSet.new(), []}, fn {val, idx}, {p_set, res_rev} ->
        p_set2 = MapSet.put(p_set, val)
        diff = MapSet.size(p_set2) - elem(suffix_tuple, idx)
        {p_set2, [diff | res_rev]}
      end)

    Enum.reverse(rev_res)
  end
end
```

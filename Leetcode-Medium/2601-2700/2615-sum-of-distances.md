# 2615. Sum of Distances

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, vector<int>> pos;
        pos.reserve(n * 2);
        for (int i = 0; i < n; ++i) {
            pos[nums[i]].push_back(i);
        }
        vector<long long> ans(n, 0);
        for (auto& kv : pos) {
            const vector<int>& idx = kv.second;
            int m = idx.size();
            if (m <= 1) continue;
            vector<long long> pref(m);
            pref[0] = idx[0];
            for (int i = 1; i < m; ++i) pref[i] = pref[i - 1] + idx[i];
            long long total = pref.back();
            for (int k = 0; k < m; ++k) {
                long long leftCnt = k;
                long long rightCnt = m - 1 - k;
                long long sumLeft = leftCnt == 0 ? 0 : (long long)idx[k] * leftCnt - pref[k - 1];
                long long sumRight = rightCnt == 0 ? 0 : (total - pref[k]) - (long long)idx[k] * rightCnt;
                ans[idx[k]] = sumLeft + sumRight;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        java.util.HashMap<Integer, java.util.ArrayList<Integer>> map = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new java.util.ArrayList<>()).add(i);
        }
        long[] ans = new long[n];
        for (java.util.Map.Entry<Integer, java.util.ArrayList<Integer>> entry : map.entrySet()) {
            java.util.ArrayList<Integer> idxs = entry.getValue();
            int m = idxs.size();
            if (m <= 1) continue;
            long[] prefix = new long[m];
            for (int i = 0; i < m; i++) {
                prefix[i] = idxs.get(i) + (i > 0 ? prefix[i - 1] : 0);
            }
            long total = prefix[m - 1];
            for (int k = 0; k < m; k++) {
                int pos = idxs.get(k);
                long leftSum = k > 0 ? prefix[k - 1] : 0;
                long rightSum = total - prefix[k];
                long leftCount = k;
                long rightCount = m - 1 - k;
                ans[pos] = (long) pos * leftCount - leftSum + (rightSum - (long) pos * rightCount);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)

        ans = [0] * len(nums)

        for idx_list in groups.values():
            m = len(idx_list)
            if m == 1:
                continue

            pref = [0] * m
            s = 0
            for i, pos in enumerate(idx_list):
                s += pos
                pref[i] = s
            total = pref[-1]

            for r, pos in enumerate(idx_list):
                left = pos * r - (pref[r - 1] if r > 0 else 0)
                right = (total - pref[r]) - pos * (m - r - 1)
                ans[pos] = left + right

        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)

        res = [0] * len(nums)
        for idxs in groups.values():
            m = len(idxs)
            if m == 1:
                continue
            prefix = [0] * m
            s = 0
            for i, pos in enumerate(idxs):
                s += pos
                prefix[i] = s
            total = prefix[-1]
            for k, pos in enumerate(idxs):
                left_cnt = k
                right_cnt = m - 1 - k
                left_sum = prefix[k - 1] if k > 0 else 0
                right_sum = total - prefix[k]
                res[pos] = pos * left_cnt - left_sum + (right_sum - pos * right_cnt)
        return res
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int idx;
} Pair;

/* Comparator for qsort: first by value, then by index */
static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->val != pb->val)
        return pa->val - pb->val;
    return pa->idx - pb->idx;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* distance(int* nums, int numsSize, int* returnSize) {
    Pair *arr = (Pair *)malloc(numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; ++i) {
        arr[i].val = nums[i];
        arr[i].idx = i;
    }
    qsort(arr, numsSize, sizeof(Pair), cmpPair);

    long long *ans = (long long *)calloc(numsSize, sizeof(long long));
    long long *prefix = (long long *)malloc((numsSize + 1) * sizeof(long long));

    int i = 0;
    while (i < numsSize) {
        int start = i;
        while (i + 1 < numsSize && arr[i + 1].val == arr[start].val)
            ++i;
        int end = i;                     // inclusive
        int m = end - start + 1;         // group size

        if (m > 1) {
            prefix[0] = 0;
            for (int t = 0; t < m; ++t) {
                prefix[t + 1] = prefix[t] + arr[start + t].idx;
            }
            long long totalSum = prefix[m];
            for (int t = 0; t < m; ++t) {
                int idx = arr[start + t].idx;
                long long left = (long long)idx * t - prefix[t];
                long long right = (totalSum - prefix[t + 1]) - (long long)idx * (m - t - 1);
                ans[idx] = left + right;
            }
        } else {
            ans[arr[start].idx] = 0; // already zero, kept for clarity
        }
        ++i;
    }

    free(arr);
    free(prefix);
    *returnSize = numsSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long[] Distance(int[] nums) {
        int n = nums.Length;
        var dict = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!dict.TryGetValue(nums[i], out var list)) {
                list = new List<int>();
                dict[nums[i]] = list;
            }
            list.Add(i);
        }

        long[] ans = new long[n];
        foreach (var kvp in dict) {
            var indices = kvp.Value;
            int m = indices.Count;
            if (m <= 1) continue;

            long[] pref = new long[m];
            pref[0] = indices[0];
            for (int i = 1; i < m; i++) {
                pref[i] = pref[i - 1] + indices[i];
            }

            for (int i = 0; i < m; i++) {
                int idx = indices[i];
                long leftCount = i;
                long rightCount = m - 1 - i;

                long sumLeft = leftCount == 0 ? 0 : (long)idx * leftCount - pref[i - 1];
                long sumRight = rightCount == 0 ? 0 : (pref[m - 1] - pref[i]) - (long)idx * rightCount;

                ans[idx] = sumLeft + sumRight;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var distance = function(nums) {
    const n = nums.length;
    const ans = new Array(n).fill(0);
    const groups = new Map();
    
    for (let i = 0; i < n; i++) {
        const v = nums[i];
        if (!groups.has(v)) groups.set(v, []);
        groups.get(v).push(i);
    }
    
    for (const indices of groups.values()) {
        const m = indices.length;
        if (m === 1) continue;
        
        const prefix = new Array(m);
        let sum = 0;
        for (let i = 0; i < m; i++) {
            sum += indices[i];
            prefix[i] = sum;
        }
        const total = prefix[m - 1];
        
        for (let i = 0; i < m; i++) {
            const idx = indices[i];
            
            // left side contribution
            const leftCount = i;
            const leftSum = leftCount > 0 ? prefix[i - 1] : 0;
            const leftDist = idx * leftCount - leftSum;
            
            // right side contribution
            const rightCount = m - 1 - i;
            const rightSum = total - prefix[i];
            const rightDist = rightSum - idx * rightCount;
            
            ans[idx] = leftDist + rightDist;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function distance(nums: number[]): number[] {
    const n = nums.length;
    const result = new Array<number>(n).fill(0);
    const groups = new Map<number, number[]>();
    
    for (let i = 0; i < n; i++) {
        const v = nums[i];
        if (!groups.has(v)) groups.set(v, []);
        groups.get(v)!.push(i);
    }
    
    for (const indices of groups.values()) {
        const m = indices.length;
        if (m <= 1) continue;
        
        const prefix = new Array<number>(m);
        prefix[0] = indices[0];
        for (let i = 1; i < m; i++) {
            prefix[i] = prefix[i - 1] + indices[i];
        }
        const totalSum = prefix[m - 1];
        
        for (let k = 0; k < m; k++) {
            const idx = indices[k];
            const leftCount = k;
            const rightCount = m - k - 1;
            
            let leftSum = 0;
            if (leftCount > 0) {
                leftSum = idx * leftCount - prefix[leftCount - 1];
            }
            
            let rightSum = 0;
            if (rightCount > 0) {
                const sumRightIndices = totalSum - prefix[k];
                rightSum = sumRightIndices - idx * rightCount;
            }
            
            result[idx] = leftSum + rightSum;
        }
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
    function distance($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $map = [];

        for ($i = 0; $i < $n; $i++) {
            $val = $nums[$i];
            if (!isset($map[$val])) {
                $map[$val] = [];
            }
            $map[$val][] = $i;
        }

        foreach ($map as $indices) {
            $len = count($indices);
            if ($len <= 1) continue;

            // prefix sums of indices
            $prefix = array_fill(0, $len, 0);
            $sum = 0;
            for ($k = 0; $k < $len; $k++) {
                $sum += $indices[$k];
                $prefix[$k] = $sum;
            }
            $total = $sum;

            for ($k = 0; $k < $len; $k++) {
                $idx = $indices[$k];

                // left side
                if ($k > 0) {
                    $leftSum = $prefix[$k - 1];
                    $leftCnt = $k;
                } else {
                    $leftSum = 0;
                    $leftCnt = 0;
                }

                // right side
                $rightSum = $total - $prefix[$k];
                $rightCnt = $len - $k - 1;

                $ans[$idx] = $idx * $leftCnt - $leftSum + $rightSum - $idx * $rightCnt;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func distance(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var groups = [Int: [Int]]()
        for (i, v) in nums.enumerated() {
            groups[v, default: []].append(i)
        }
        var ans = Array(repeating: 0, count: n)
        for (_, indices) in groups {
            let m = indices.count
            if m <= 1 { continue }
            var prefix = [Int64](repeating: 0, count: m + 1)
            for i in 0..<m {
                prefix[i + 1] = prefix[i] + Int64(indices[i])
            }
            let total = prefix[m]
            for k in 0..<m {
                let pos = Int64(indices[k])
                let leftCount = Int64(k)
                let rightCount = Int64(m - k - 1)
                let sumLeft = pos * leftCount - prefix[k]
                let sumRight = (total - prefix[k + 1]) - pos * rightCount
                ans[indices[k]] = Int(sumLeft + sumRight)
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distance(nums: IntArray): LongArray {
        val n = nums.size
        val map = HashMap<Int, MutableList<Int>>(n)
        for (i in 0 until n) {
            val list = map.getOrPut(nums[i]) { mutableListOf() }
            list.add(i)
        }
        val ans = LongArray(n)
        for (list in map.values) {
            val m = list.size
            if (m <= 1) continue
            val pref = LongArray(m + 1)
            for (i in 0 until m) {
                pref[i + 1] = pref[i] + list[i].toLong()
            }
            val total = pref[m]
            for (k in 0 until m) {
                val idx = list[k]
                val leftCount = k
                val rightCount = m - k - 1
                val leftSum = idx.toLong() * leftCount - pref[k]
                val rightSum = (total - pref[k + 1]) - idx.toLong() * rightCount
                ans[idx] = leftSum + rightSum
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> distance(List<int> nums) {
    int n = nums.length;
    Map<int, List<int>> groups = {};
    for (int i = 0; i < n; i++) {
      groups.putIfAbsent(nums[i], () => []).add(i);
    }

    List<int> ans = List.filled(n, 0);
    for (var entry in groups.entries) {
      List<int> pos = entry.value;
      int m = pos.length;
      if (m <= 1) continue;

      List<int> pref = List.filled(m, 0);
      pref[0] = pos[0];
      for (int i = 1; i < m; i++) {
        pref[i] = pref[i - 1] + pos[i];
      }
      int totalSum = pref[m - 1];

      for (int k = 0; k < m; k++) {
        int idx = pos[k];
        int leftCount = k;
        int rightCount = m - k - 1;

        int sumLeft = 0;
        if (leftCount > 0) {
          sumLeft = idx * leftCount - pref[leftCount - 1];
        }

        int sumRight = 0;
        if (rightCount > 0) {
          int rightSum = totalSum - pref[k];
          sumRight = rightSum - idx * rightCount;
        }

        ans[idx] = sumLeft + sumRight;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func distance(nums []int) []int64 {
    n := len(nums)
    res := make([]int64, n)

    // Map each value to its list of indices
    groups := make(map[int][]int)
    for i, v := range nums {
        groups[v] = append(groups[v], i)
    }

    // Process each group independently
    for _, idxs := range groups {
        m := len(idxs)
        if m == 1 {
            continue
        }
        // Prefix sums of indices (as int64)
        pref := make([]int64, m+1)
        for i, pos := range idxs {
            pref[i+1] = pref[i] + int64(pos)
        }

        total := pref[m]
        for j, pos := range idxs {
            leftCount := int64(j)
            rightCount := int64(m - j - 1)

            leftSum := pref[j]               // sum of indices to the left
            rightSum := total - pref[j+1]    // sum of indices to the right

            contribution := int64(pos)*leftCount - leftSum + (rightSum - int64(pos)*rightCount)
            res[pos] = contribution
        }
    }

    return res
}
```

## Ruby

```ruby
def distance(nums)
  n = nums.length
  result = Array.new(n, 0)
  groups = Hash.new { |h, k| h[k] = [] }

  nums.each_with_index do |val, idx|
    groups[val] << idx
  end

  groups.each_value do |indices|
    m = indices.size
    next if m <= 1

    prefix = Array.new(m + 1, 0)
    (0...m).each do |i|
      prefix[i + 1] = prefix[i] + indices[i]
    end
    total = prefix[m]

    (0...m).each do |i|
      pos = indices[i]
      left_cnt = i
      right_cnt = m - i - 1
      left_sum = prefix[i]
      right_sum = total - prefix[i + 1]
      result[pos] = pos * left_cnt - left_sum + right_sum - pos * right_cnt
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def distance(nums: Array[Int]): Array[Long] = {
        val n = nums.length
        val result = new Array[Long](n)
        import scala.collection.mutable

        val groups = mutable.HashMap[Int, mutable.ArrayBuffer[Int]]()
        for (i <- 0 until n) {
            val v = nums(i)
            groups.getOrElseUpdate(v, mutable.ArrayBuffer[Int]()) += i
        }

        for ((_, indices) <- groups) {
            val k = indices.length
            if (k > 1) {
                val prefix = new Array[Long](k)
                var sum: Long = 0L
                var idxPos = 0
                while (idxPos < k) {
                    sum += indices(idxPos).toLong
                    prefix(idxPos) = sum
                    idxPos += 1
                }
                var p = 0
                while (p < k) {
                    val idx = indices(p).toLong
                    val left = if (p > 0) idx * p - prefix(p - 1) else 0L
                    val right = if (p < k - 1) (prefix(k - 1) - prefix(p)) - idx * (k - p - 1) else 0L
                    result(indices(p)) = left + right
                    p += 1
                }
            }
        }

        result
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn distance(nums: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut groups: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            groups.entry(v).or_default().push(i);
        }

        let mut ans = vec![0_i64; n];

        for indices in groups.values() {
            let m = indices.len();
            if m <= 1 {
                continue;
            }
            // prefix sums of positions
            let mut pref: Vec<i64> = vec![0; m];
            for (i, &idx) in indices.iter().enumerate() {
                let val = idx as i64;
                pref[i] = val + if i > 0 { pref[i - 1] } else { 0 };
            }
            let total = *pref.last().unwrap();

            for (j, &idx) in indices.iter().enumerate() {
                let pos = idx as i64;
                let left_cnt = j as i64;
                let right_cnt = (m - j - 1) as i64;
                let sum_left = if j > 0 { pref[j - 1] } else { 0 };
                let sum_right = total - pref[j];
                let contribution = pos * left_cnt - sum_left + sum_right - pos * right_cnt;
                ans[idx] = contribution;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (distance nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (ht (make-hash)))
    ;; Build hash: value -> list of indices (in reverse order)
    (for ([val (in-list nums)] [i (in-naturals)])
      (hash-set! ht val (cons i (hash-ref ht val '()))))
    (define result (make-vector n 0))
    ;; Process each group of equal values
    (for ([key (in-hash-keys ht)])
      (let* ((idxs-rev (hash-ref ht key))
             (idxs (reverse idxs-rev))
             (len (length idxs))
             (vec (list->vector idxs)))
        ;; Prefix sums of indices
        (define pref (make-vector (+ len 1) 0))
        (for ([i (in-range len)])
          (vector-set! pref (+ i 1)
                       (+ (vector-ref pref i) (vector-ref vec i))))
        ;; Compute answer for each occurrence
        (for ([j (in-range len)])
          (let* ((p (vector-ref vec j))
                 (left j)
                 (right (- len 1 j))
                 (sum-left (- (* p left) (vector-ref pref left)))
                 (sum-right (- (- (vector-ref pref len)
                                 (vector-ref pref (+ j 1)))
                               (* p right)))
                 (total (+ sum-left sum-right)))
            (vector-set! result p total)))))
    (vector->list result)))
```

## Erlang

```erlang
-module(solution).
-export([distance/1]).

-spec distance(Nums :: [integer()]) -> [integer()].
distance(Nums) ->
    PositionsMap = build_positions(Nums, 0, #{}),
    ResultMap = maps:fold(fun(_Val, RevPosList, Acc) ->
        PosList = lists:reverse(RevPosList),
        process_group(PosList, Acc)
    end, #{}, PositionsMap),
    N = length(Nums),
    [maps:get(I, ResultMap, 0) || I <- lists:seq(0, N-1)].

build_positions([], _Idx, Map) -> Map;
build_positions([H|T], Idx, Map) ->
    UpdatedMap = maps:update_with(H,
        fun(L) -> [Idx | L] end,
        [Idx],
        Map),
    build_positions(T, Idx + 1, UpdatedMap).

process_group(PosList, AccMap) ->
    Len = length(PosList),
    Prefix = lists:scanl(fun(A, Acc) -> A + Acc end, 0, PosList),
    Total = lists:last(Prefix),
    process_positions(PosList, Prefix, Len, Total, 0, AccMap).

process_positions([], _Prefix, _Len, _Total, _Idx, Acc) ->
    Acc;
process_positions([Pos|Rest], Prefix, Len, Total, Idx, Acc) ->
    LeftCount = Idx,
    RightCount = Len - 1 - Idx,
    LeftSum = lists:nth(Idx + 1, Prefix),
    RightSum = Total - lists:nth(Idx + 2, Prefix),
    Contribution = Pos * LeftCount - LeftSum + RightSum - Pos * RightCount,
    NewAcc = maps:put(Pos, Contribution, Acc),
    process_positions(Rest, Prefix, Len, Total, Idx + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec distance(nums :: [integer]) :: [integer]
  def distance(nums) do
    n = length(nums)

    groups_rev =
      Enum.with_index(nums)
      |> Enum.reduce(%{}, fn {val, idx}, acc ->
        Map.update(acc, val, [idx], fn lst -> [idx | lst] end)
      end)

    result_map =
      Enum.reduce(groups_rev, %{}, fn {_val, rev_list}, res_acc ->
        indices = Enum.reverse(rev_list)
        k = length(indices)

        if k == 1 do
          Map.put(res_acc, hd(indices), 0)
        else
          sum_all = Enum.sum(indices)

          {_, updated_map} =
            Enum.with_index(indices)
            |> Enum.reduce({0, res_acc}, fn {p, i}, {left_sum, map_acc} ->
              left_contrib = i * p - left_sum
              right_contrib = (sum_all - left_sum - p) - (k - 1 - i) * p
              total = left_contrib + right_contrib
              new_map = Map.put(map_acc, p, total)
              {left_sum + p, new_map}
            end)

          updated_map
        end
      end)

    Enum.map(0..n - 1, fn i -> Map.get(result_map, i, 0) end)
  end
end
```

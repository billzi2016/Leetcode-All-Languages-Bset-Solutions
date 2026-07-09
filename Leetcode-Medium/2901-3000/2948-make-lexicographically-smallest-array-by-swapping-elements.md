# 2948. Make Lexicographically Smallest Array by Swapping Elements

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        
        unordered_map<long long,int> comp;
        vector<vector<int>> groups;
        int gid = -1;
        for (int i = 0; i < n; ++i) {
            if (i == 0 || (long long)sorted[i] - sorted[i-1] > limit) {
                ++gid;
                groups.emplace_back();
            }
            comp[sorted[i]] = gid;
            groups[gid].push_back(sorted[i]);
        }
        
        vector<int> pos(groups.size(), 0);
        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            int g = comp[nums[i]];
            res[i] = groups[g][pos[g]++];
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        
        Map<Integer, Integer> valToGroup = new HashMap<>();
        List<List<Integer>> groups = new ArrayList<>();
        int groupId = 0;
        groups.add(new ArrayList<>());
        
        for (int i = 0; i < n; i++) {
            if (i > 0 && (long)sorted[i] - sorted[i - 1] > limit) {
                groupId++;
                groups.add(new ArrayList<>());
            }
            int val = sorted[i];
            valToGroup.putIfAbsent(val, groupId);
            groups.get(groupId).add(val);
        }
        
        int[] ptr = new int[groups.size()];
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int g = valToGroup.get(nums[i]);
            result[i] = groups.get(g).get(ptr[g]++);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        # Sort a copy to determine connected components based on value differences.
        sorted_nums = sorted(nums)
        val_to_group = {}
        groups = []          # list of lists, each group holds its values in ascending order
        curr_group = 0
        groups.append([])

        prev = None
        for v in sorted_nums:
            if prev is not None and v - prev > limit:
                # start a new component
                curr_group += 1
                groups.append([])
            val_to_group[v] = curr_group
            groups[curr_group].append(v)
            prev = v

        # Pointers to the next unused element in each group.
        ptr = [0] * len(groups)

        result = []
        for v in nums:
            g = val_to_group[v]
            idx = ptr[g]
            result.append(groups[g][idx])
            ptr[g] += 1

        return result
```

## Python3

```python
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        if not nums:
            return []
        sorted_vals = sorted(nums)
        comp_id_map = {}
        components = []
        cur_id = -1
        prev_val = None
        for v in sorted_vals:
            if cur_id == -1 or (prev_val is not None and v - prev_val > limit):
                cur_id += 1
                components.append([])
            components[cur_id].append(v)
            comp_id_map[v] = cur_id
            prev_val = v

        # pointers for each component to retrieve next smallest element
        ptrs = [0] * len(components)

        result = []
        for v in nums:
            cid = comp_id_map[v]
            idx = ptrs[cid]
            result.append(components[cid][idx])
            ptrs[cid] += 1

        return result
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

/* lower bound: first index with value >= target */
static int lower_bound(int *arr, int n, int target) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] < target)
            l = m + 1;
        else
            r = m;
    }
    return l;   // assumes target exists in arr
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* lexicographicallySmallestArray(int* nums, int numsSize, int limit, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    /* copy and sort the array */
    int *sorted = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) sorted[i] = nums[i];
    qsort(sorted, numsSize, sizeof(int), cmp_int);

    /* assign group ids to each position in the sorted array */
    int *groupIdx = (int *)malloc(numsSize * sizeof(int));
    int curGroup = 0;
    groupIdx[0] = 0;
    for (int i = 1; i < numsSize; ++i) {
        long long diff = (long long)sorted[i] - (long long)sorted[i - 1];
        if (diff > limit) ++curGroup;
        groupIdx[i] = curGroup;
    }
    int groups = curGroup + 1;

    /* determine start index of each group in the sorted array */
    int *startIdx = (int *)malloc(groups * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || groupIdx[i] != groupIdx[i - 1]) {
            startIdx[groupIdx[i]] = i;
        }
    }

    /* pointer to next unused element inside each group */
    int *ptr = (int *)malloc(groups * sizeof(int));
    for (int g = 0; g < groups; ++g) ptr[g] = startIdx[g];

    /* build result */
    int *res = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        int pos = lower_bound(sorted, numsSize, val);   // first occurrence
        int gid = groupIdx[pos];
        res[i] = sorted[ptr[gid]];
        ++ptr[gid];
    }

    free(sorted);
    free(groupIdx);
    free(startIdx);
    free(ptr);

    *returnSize = numsSize;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] LexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.Length;
        int[] sorted = (int[])nums.Clone();
        Array.Sort(sorted);

        var valToGroup = new Dictionary<int, int>(n);
        var groups = new List<List<int>>();

        int groupId = -1;
        int prev = 0;

        for (int i = 0; i < n; i++) {
            if (i == 0 || sorted[i] - prev > limit) {
                groupId++;
                groups.Add(new List<int>());
            }
            groups[groupId].Add(sorted[i]);
            valToGroup[sorted[i]] = groupId;
            prev = sorted[i];
        }

        int[] ptr = new int[groups.Count];
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            int gid = valToGroup[nums[i]];
            result[i] = groups[gid][ptr[gid]++];
        }

        return result;
    }
}
```

## Javascript

```javascript
var lexicographicallySmallestArray = function(nums, limit) {
    const n = nums.length;
    const sorted = new Array(n);
    for (let i = 0; i < n; i++) {
        sorted[i] = { val: nums[i], idx: i };
    }
    sorted.sort((a, b) => a.val - b.val);

    const compId = new Array(n);
    const groups = [];
    let cur = 0;
    groups.push([]);
    compId[sorted[0].idx] = 0;
    groups[0].push(sorted[0].val);

    for (let i = 1; i < n; i++) {
        if (sorted[i].val - sorted[i - 1].val > limit) {
            cur++;
            groups.push([]);
        }
        compId[sorted[i].idx] = cur;
        groups[cur].push(sorted[i].val);
    }

    const ptr = new Array(groups.length).fill(0);
    const res = new Array(n);
    for (let i = 0; i < n; i++) {
        const id = compId[i];
        res[i] = groups[id][ptr[id]];
        ptr[id]++;
    }
    return res;
};
```

## Typescript

```typescript
function lexicographicallySmallestArray(nums: number[], limit: number): number[] {
    const sorted = [...nums].sort((a, b) => a - b);
    const groups: number[][] = [];
    const valueToGroup = new Map<number, number>();
    let curGroup = -1;
    for (let i = 0; i < sorted.length; i++) {
        if (i === 0 || sorted[i] - sorted[i - 1] > limit) {
            groups.push([]);
            curGroup = groups.length - 1;
        }
        groups[curGroup].push(sorted[i]);
        valueToGroup.set(sorted[i], curGroup);
    }

    const ptr = new Array(groups.length).fill(0);
    const result = new Array<number>(nums.length);
    for (let i = 0; i < nums.length; i++) {
        const g = valueToGroup.get(nums[i])!;
        result[i] = groups[g][ptr[g]];
        ptr[g]++;
    }
    return result;
}
```

## Php

```php
<?php
class DSU {
    public array $parent;
    public array $rank;

    public function __construct(int $n) {
        $this->parent = range(0, $n - 1);
        $this->rank   = array_fill(0, $n, 0);
    }

    public function find(int $x): int {
        if ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }

    public function union(int $x, int $y): void {
        $rx = $this->find($x);
        $ry = $this->find($y);
        if ($rx === $ry) {
            return;
        }
        if ($this->rank[$rx] < $this->rank[$ry]) {
            $this->parent[$rx] = $ry;
        } elseif ($this->rank[$rx] > $this->rank[$ry]) {
            $this->parent[$ry] = $rx;
        } else {
            $this->parent[$ry] = $rx;
            $this->rank[$rx]++;
        }
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @return Integer[]
     */
    function lexicographicallySmallestArray($nums, $limit) {
        $n = count($nums);
        if ($n <= 1) return $nums;

        // Pair each value with its original index.
        $pairs = [];
        for ($i = 0; $i < $n; $i++) {
            $pairs[] = [$nums[$i], $i];
        }

        // Sort by value.
        usort($pairs, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        // Build DSU based on adjacency condition in sorted order.
        $dsu = new DSU($n);
        for ($i = 1; $i < $n; $i++) {
            if ($pairs[$i][0] - $pairs[$i - 1][0] <= $limit) {
                $dsu->union($pairs[$i][1], $pairs[$i - 1][1]);
            }
        }

        // Group indices and values by component root.
        $components = [];
        for ($i = 0; $i < $n; $i++) {
            $root = $dsu->find($i);
            if (!isset($components[$root])) {
                $components[$root] = ['indices' => [], 'values' => []];
            }
            $components[$root]['indices'][] = $i;
            $components[$root]['values'][]  = $nums[$i];
        }

        // For each component, sort indices and values, then assign smallest values to smallest positions.
        foreach ($components as $comp) {
            sort($comp['indices']);
            sort($comp['values']);
            $cnt = count($comp['indices']);
            for ($k = 0; $k < $cnt; $k++) {
                $idx = $comp['indices'][$k];
                $nums[$idx] = $comp['values'][$k];
            }
        }

        return $nums;
    }
}
?>
```

## Swift

```swift
class Solution {
    func lexicographicallySmallestArray(_ nums: [Int], _ limit: Int) -> [Int] {
        let sorted = nums.sorted()
        var groups = [[Int]]()
        var currentGroup = [Int]()
        
        for (i, val) in sorted.enumerated() {
            if i == 0 {
                currentGroup.append(val)
            } else {
                if val - sorted[i - 1] <= limit {
                    currentGroup.append(val)
                } else {
                    groups.append(currentGroup)
                    currentGroup = [val]
                }
            }
        }
        groups.append(currentGroup)
        
        var valueToGroup = [Int: Int]()
        for (gIdx, grp) in groups.enumerated() {
            for v in grp {
                valueToGroup[v] = gIdx
            }
        }
        
        var groupPos = Array(repeating: 0, count: groups.count)
        var result = [Int]()
        result.reserveCapacity(nums.count)
        
        for num in nums {
            let g = valueToGroup[num]!   // each number belongs to a group
            let idx = groupPos[g]
            result.append(groups[g][idx])
            groupPos[g] = idx + 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lexicographicallySmallestArray(nums: IntArray, limit: Int): IntArray {
        val n = nums.size
        if (n == 0) return intArrayOf()
        // indices sorted by their values
        val idx = (0 until n).toMutableList()
        idx.sortWith { a, b ->
            when {
                nums[a] < nums[b] -> -1
                nums[a] > nums[b] -> 1
                else -> 0
            }
        }

        val comp = IntArray(n)
        val groups = mutableListOf<MutableList<Int>>()
        var curComp = 0
        var lastVal = nums[idx[0]]
        comp[idx[0]] = curComp
        groups.add(mutableListOf())
        groups[curComp].add(lastVal)

        for (k in 1 until n) {
            val i = idx[k]
            val v = nums[i]
            if (v - lastVal > limit) {
                curComp++
                groups.add(mutableListOf())
            }
            comp[i] = curComp
            groups[curComp].add(v)
            lastVal = v
        }

        val pointers = IntArray(groups.size)
        val res = IntArray(n)
        for (i in 0 until n) {
            val g = comp[i]
            res[i] = groups[g][pointers[g]]
            pointers[g]++
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> lexicographicallySmallestArray(List<int> nums, int limit) {
    int n = nums.length;
    // Order indices by their corresponding values
    List<int> order = List<int>.generate(n, (i) => i);
    order.sort((a, b) => nums[a].compareTo(nums[b]));

    // Determine component id for each index
    List<int> compId = List<int>.filled(n, 0);
    int comp = 0;
    compId[order[0]] = comp;
    for (int i = 1; i < n; ++i) {
      if (nums[order[i]] - nums[order[i - 1]] > limit) {
        comp++;
      }
      compId[order[i]] = comp;
    }

    int totalComp = comp + 1;
    // Collect sorted values for each component
    List<List<int>> groups = List<List<int>>.generate(totalComp, (_) => []);
    for (int idx in order) {
      groups[compId[idx]].add(nums[idx]);
    }

    // Pointers to the next unused element in each group
    List<int> ptr = List<int>.filled(totalComp, 0);
    List<int> result = List<int>.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int cid = compId[i];
      result[i] = groups[cid][ptr[cid]];
      ptr[cid]++;
    }
    return result;
  }
}
```

## Golang

```go
package main

import "sort"

func lexicographicallySmallestArray(nums []int, limit int) []int {
	n := len(nums)
	sortedVals := make([]int, n)
	copy(sortedVals, nums)
	sort.Ints(sortedVals)

	valToGroup := make(map[int]int, n)
	groups := [][]int{}
	groupID := -1
	var prev int

	for i, v := range sortedVals {
		if i == 0 || v-prev > limit {
			groupID++
			groups = append(groups, []int{})
		}
		groups[groupID] = append(groups[groupID], v)
		valToGroup[v] = groupID
		prev = v
	}

	ptr := make([]int, len(groups))
	res := make([]int, n)
	for i, v := range nums {
		g := valToGroup[v]
		idx := ptr[g]
		res[i] = groups[g][idx]
		ptr[g]++
	}
	return res
}
```

## Ruby

```ruby
def lexicographically_smallest_array(nums, limit)
  n = nums.length
  indexed = []
  nums.each_with_index { |v, i| indexed << [v, i] }
  indexed.sort_by! { |pair| pair[0] }

  groups = Array.new(n)
  group_vals = []

  prev_val = nil
  cur_group = 0

  indexed.each do |val, idx|
    if !prev_val.nil? && (val - prev_val) > limit
      cur_group += 1
    end
    groups[idx] = cur_group
    (group_vals[cur_group] ||= []) << val
    prev_val = val
  end

  ptrs = Array.new(group_vals.size, 0)
  result = Array.new(n)

  n.times do |i|
    g = groups[i]
    result[i] = group_vals[g][ptrs[g]]
    ptrs[g] += 1
  end

  result
end
```

## Scala

```scala
object Solution {
  def lexicographicallySmallestArray(nums: Array[Int], limit: Int): Array[Int] = {
    val n = nums.length
    if (n == 0) return nums

    class DSU(val size: Int) {
      private val parent = (0 until size).toArray
      private val rank   = new Array[Int](size)

      def find(x: Int): Int = {
        var p = x
        while (parent(p) != p) p = parent(p)
        var cur = x
        while (parent(cur) != cur) {
          val nxt = parent(cur)
          parent(cur) = p
          cur = nxt
        }
        p
      }

      def union(x: Int, y: Int): Unit = {
        var rx = find(x)
        var ry = find(y)
        if (rx == ry) return
        if (rank(rx) < rank(ry)) parent(rx) = ry
        else if (rank(rx) > rank(ry)) parent(ry) = rx
        else {
          parent(ry) = rx
          rank(rx) += 1
        }
      }
    }

    val dsu = new DSU(n)

    // sort values with their original indices
    val sorted = nums.zipWithIndex.sortBy(_._1)
    var i = 1
    while (i < n) {
      if (sorted(i)._1.toLong - sorted(i - 1)._1.toLong <= limit.toLong) {
        dsu.union(sorted(i)._2, sorted(i - 1)._2)
      }
      i += 1
    }

    import scala.collection.mutable.{ArrayBuffer, Queue, Map => MutableMap}
    val comp = MutableMap[Int, ArrayBuffer[Int]]()
    var idx = 0
    while (idx < n) {
      val root = dsu.find(idx)
      val buf = comp.getOrElseUpdate(root, ArrayBuffer())
      buf += nums(idx)
      idx += 1
    }

    // sort each component and store in a queue for fast dequeue
    val compQueue = MutableMap[Int, Queue[Int]]()
    for ((root, buf) <- comp) {
      val sortedVals = buf.sorted
      compQueue(root) = Queue(sortedVals: _*)
    }

    val res = new Array[Int](n)
    var pos = 0
    while (pos < n) {
      val root = dsu.find(pos)
      val q = compQueue(root)
      res(pos) = q.dequeue()
      pos += 1
    }
    res
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![];
        }
        let mut sorted = nums.clone();
        sorted.sort();

        let mut val_to_group: HashMap<i32, usize> = HashMap::with_capacity(n);
        let mut groups: Vec<Vec<i32>> = Vec::new();

        let mut cur_group: usize = 0;
        for (i, &val) in sorted.iter().enumerate() {
            if i > 0 && ((val as i64 - sorted[i - 1] as i64).abs() > limit as i64) {
                cur_group += 1;
            }
            if groups.len() == cur_group {
                groups.push(Vec::new());
            }
            groups[cur_group].push(val);
            val_to_group.entry(val).or_insert(cur_group);
        }

        let mut ptr = vec![0usize; groups.len()];
        let mut result: Vec<i32> = Vec::with_capacity(n);
        for &orig in nums.iter() {
            let g = *val_to_group.get(&orig).unwrap();
            let idx = ptr[g];
            result.push(groups[g][idx]);
            ptr[g] += 1;
        }
        result
    }
}
```

## Racket

```racket
#lang racket

(define/contract (lexicographically-smallest-array nums limit)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((sorted (sort (copy-list nums) <))
         (value->group (make-hash)))
    ;; Build groups and map each value to its group id
    (define groups '())
    (define current-group '())
    (define gid -1)
    (define prev #f)
    (for ([v sorted])
      (if (and prev (<= (abs (- v prev)) limit))
          (set! current-group (cons v current-group))
          (begin
            (when (not (null? current-group))
              (set! groups (cons (reverse current-group) groups)))
            (set! gid (+ gid 1))
            (set! current-group (list v))))
      (hash-set! value->group v gid)
      (set! prev v))
    (when (not (null? current-group))
      (set! groups (cons (reverse current-group) groups)))
    (set! groups (reverse groups))
    ;; Convert groups to vectors for O(1) indexing
    (define group-vec (list->vector (map list->vector groups)))
    (define pos-vec (make-vector (vector-length group-vec) 0))
    ;; Construct the result array
    (let loop ((remaining nums) (acc '()))
      (if (null? remaining)
          (reverse acc)
          (let* ((val (car remaining))
                 (g (hash-ref value->group val))
                 (idx (vector-ref pos-vec g))
                 (chosen (vector-ref (vector-ref group-vec g) idx)))
            (vector-set! pos-vec g (+ idx 1))
            (loop (cdr remaining) (cons chosen acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([lexicographically_smallest_array/2]).

lexicographically_smallest_array(Nums, Limit) ->
    Indexed = enumerate(Nums, 0),
    Sorted = lists:keysort(1, Indexed),
    {CompIdxMap, ValuesMap} = process_sorted(Sorted, Limit, undefined, 0, #{}, #{}),
    RevValuesMap = maps:map(fun(_K, L) -> lists:reverse(L) end, ValuesMap),
    N = length(Nums),
    Indices = lists:seq(0, N - 1),
    {Result, _} = build_result(Indices, CompIdxMap, RevValuesMap, []),
    Result.

enumerate([], _) ->
    [];
enumerate([H | T], I) ->
    [{H, I} | enumerate(T, I + 1)].

process_sorted([], _Limit, _PrevVal, _Comp, CompIdxMap, ValuesMap) ->
    {CompIdxMap, ValuesMap};
process_sorted([{Val, Idx} | Rest], Limit, PrevVal, Comp, CompIdxMap, ValuesMap) ->
    NewComp = case PrevVal of
        undefined -> 0;
        _ when Val - PrevVal > Limit -> Comp + 1;
        _ -> Comp
    end,
    CompIdxMap2 = maps:put(Idx, NewComp, CompIdxMap),
    ValuesMap2 = maps:update_with(
        NewComp,
        fun(L) -> [Val | L] end,
        [Val],
        ValuesMap
    ),
    process_sorted(Rest, Limit, Val, NewComp, CompIdxMap2, ValuesMap2).

build_result([], _CompIdxMap, ValuesMap, Acc) ->
    {lists:reverse(Acc), ValuesMap};
build_result([Idx | Rest], CompIdxMap, ValuesMap, Acc) ->
    Comp = maps:get(Idx, CompIdxMap),
    List = maps:get(Comp, ValuesMap),
    [Val | Tail] = List,
    ValuesMap2 = maps:put(Comp, Tail, ValuesMap),
    build_result(Rest, CompIdxMap, ValuesMap2, [Val | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec lexicographically_smallest_array(nums :: [integer], limit :: integer) :: [integer]
  def lexicographically_smallest_array(nums, limit) do
    sorted = Enum.sort(nums)

    {_, _, num_to_group, group_queues} =
      Enum.reduce(sorted, {nil, 0, %{}, %{}}, fn val, {prev, grp, ntg, gq} ->
        new_grp =
          case prev do
            nil -> grp
            _ when val - prev > limit -> grp + 1
            _ -> grp
          end

        ntg2 = Map.put(ntg, val, new_grp)
        q = Map.get(gq, new_grp, :queue.new())
        gq2 = Map.put(gq, new_grp, :queue.in(val, q))
        {val, new_grp, ntg2, gq2}
      end)

    {result_rev, _final_queues} =
      Enum.reduce(nums, {[], group_queues}, fn val, {acc, queues} ->
        grp = Map.fetch!(num_to_group, val)
        {{:value, smallest}, new_q} = :queue.out(Map.fetch!(queues, grp))
        {[smallest | acc], Map.put(queues, grp, new_q)}
      end)

    Enum.reverse(result_rev)
  end
end
```

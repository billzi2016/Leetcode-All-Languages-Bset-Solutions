# 2099. Find Subsequence of Length K With the Largest Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        vector<pair<int,int>> vp;
        vp.reserve(nums.size());
        for (int i = 0; i < (int)nums.size(); ++i) {
            vp.emplace_back(nums[i], i);
        }
        sort(vp.begin(), vp.end(), [](const pair<int,int>& a, const pair<int,int>& b){
            return a.first > b.first;
        });
        vp.resize(k);
        sort(vp.begin(), vp.end(), [](const pair<int,int>& a, const pair<int,int>& b){
            return a.second < b.second;
        });
        vector<int> ans;
        ans.reserve(k);
        for (auto &p : vp) ans.push_back(p.first);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        int n = nums.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) {
            idx[i] = i;
        }
        java.util.Arrays.sort(idx, (a, b) -> Integer.compare(nums[b], nums[a]));
        int[] selected = new int[k];
        System.arraycopy(idx, 0, selected, 0, k);
        java.util.Arrays.sort(selected);
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = nums[selected[i]];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Get indices of the k largest values
        top_k = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)[:k]
        # Preserve original order
        top_k.sort(key=lambda x: x[0])
        return [value for _, value in top_k]
```

## Python3

```python
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each number with its original index
        indexed = [(i, val) for i, val in enumerate(nums)]
        # Select the k largest values (by value descending)
        top_k = sorted(indexed, key=lambda x: x[1], reverse=True)[:k]
        # Restore original order by sorting indices ascending
        top_k.sort(key=lambda x: x[0])
        # Extract the values in order
        return [val for _, val in top_k]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int idx;
} Pair;

static int cmp_desc(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    return pb->val - pa->val;  // descending by value
}

static int cmp_asc(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    return pa->idx - pb->idx;  // ascending by index
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxSubsequence(int* nums, int numsSize, int k, int* returnSize) {
    Pair *pairs = (Pair *)malloc(numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; ++i) {
        pairs[i].val = nums[i];
        pairs[i].idx = i;
    }

    qsort(pairs, numsSize, sizeof(Pair), cmp_desc);

    Pair *selected = (Pair *)malloc(k * sizeof(Pair));
    for (int i = 0; i < k; ++i) {
        selected[i] = pairs[i];
    }
    free(pairs);

    qsort(selected, k, sizeof(Pair), cmp_asc);

    int *result = (int *)malloc(k * sizeof(int));
    for (int i = 0; i < k; ++i) {
        result[i] = selected[i].val;
    }

    free(selected);
    *returnSize = k;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] MaxSubsequence(int[] nums, int k) {
        var pairs = new List<(int val, int idx)>(nums.Length);
        for (int i = 0; i < nums.Length; i++) {
            pairs.Add((nums[i], i));
        }
        // Sort by value descending
        pairs.Sort((a, b) => b.val.CompareTo(a.val));
        var selected = pairs.GetRange(0, k);
        // Sort selected by original index to preserve order
        selected.Sort((a, b) => a.idx.CompareTo(b.idx));
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = selected[i].val;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSubsequence = function(nums, k) {
    const pairs = nums.map((value, index) => ({ value, index }));
    pairs.sort((a, b) => b.value - a.value);
    const chosen = pairs.slice(0, k);
    chosen.sort((a, b) => a.index - b.index);
    return chosen.map(p => p.value);
};
```

## Typescript

```typescript
function maxSubsequence(nums: number[], k: number): number[] {
    const indexed = nums.map((val, idx) => ({ val, idx }));
    indexed.sort((a, b) => b.val - a.val);
    const selected = indexed.slice(0, k);
    selected.sort((a, b) => a.idx - b.idx);
    return selected.map(item => item.val);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function maxSubsequence($nums, $k) {
        $pairs = [];
        foreach ($nums as $i => $v) {
            $pairs[] = ['idx' => $i, 'val' => $v];
        }
        usort($pairs, function($a, $b) {
            return $b['val'] <=> $a['val']; // descending by value
        });
        $selected = array_slice($pairs, 0, $k);
        usort($selected, function($a, $b) {
            return $a['idx'] <=> $b['idx']; // ascending by original index
        });
        $result = [];
        foreach ($selected as $p) {
            $result[] = $p['val'];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maxSubsequence(_ nums: [Int], _ k: Int) -> [Int] {
        // Pair each element with its original index
        let indexed = nums.enumerated().map { ($0.offset, $0.element) }
        // Sort by value descending to get the largest k elements
        let topK = indexed.sorted { $0.1 > $1.1 }.prefix(k)
        // Preserve original order by sorting selected pairs by index ascending
        let ordered = topK.sorted { $0.0 < $1.0 }
        // Extract values
        return ordered.map { $0.1 }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSubsequence(nums: IntArray, k: Int): IntArray {
        val indexed = nums.mapIndexed { idx, value -> idx to value }
        val selected = indexed
            .sortedByDescending { it.second }
            .take(k)
            .sortedBy { it.first }
        return selected.map { it.second }.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> maxSubsequence(List<int> nums, int k) {
    List<int> indices = List.generate(nums.length, (i) => i);
    indices.sort((a, b) {
      int cmp = nums[b].compareTo(nums[a]); // descending by value
      if (cmp != 0) return cmp;
      return a.compareTo(b); // tie‑break by index
    });
    List<int> chosen = indices.sublist(0, k);
    chosen.sort(); // restore original order
    return chosen.map((i) => nums[i]).toList();
  }
}
```

## Golang

```go
import "sort"

type pair struct {
	val int
	idx int
}

func maxSubsequence(nums []int, k int) []int {
	n := len(nums)
	pairs := make([]pair, n)
	for i, v := range nums {
		pairs[i] = pair{val: v, idx: i}
	}
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].val == pairs[j].val {
			return pairs[i].idx < pairs[j].idx
		}
		return pairs[i].val > pairs[j].val
	})
	selected := make([]pair, k)
	copy(selected, pairs[:k])
	sort.Slice(selected, func(i, j int) bool {
		return selected[i].idx < selected[j].idx
	})
	res := make([]int, k)
	for i, p := range selected {
		res[i] = p.val
	}
	return res
}
```

## Ruby

```ruby
def max_subsequence(nums, k)
  pairs = nums.each_with_index.map { |val, idx| [val, idx] }
  top_k = pairs.sort_by { |val, _| -val }[0, k]
  top_k.sort_by! { |_, idx| idx }
  top_k.map { |val, _| val }
end
```

## Scala

```scala
object Solution {
    def maxSubsequence(nums: Array[Int], k: Int): Array[Int] = {
        // Pair each number with its original index
        val paired = nums.zipWithIndex.map { case (value, idx) => (value, idx) }
        // Sort by value descending and take the first k elements
        val topK = paired.sortBy(-_._1).take(k)
        // Restore original order by sorting indices ascending
        val ordered = topK.sortBy(_._2)
        // Extract values
        ordered.map(_._1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_subsequence(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut pairs: Vec<(i32, usize)> = nums.iter().cloned().enumerate()
            .map(|(i, v)| (v, i))
            .collect();
        // Sort by value descending
        pairs.sort_by(|a, b| b.0.cmp(&a.0));
        let k_usize = k as usize;
        // Take the top k elements and keep their original indices
        let mut selected: Vec<(usize, i32)> = pairs.iter().take(k_usize)
            .map(|&(v, idx)| (idx, v))
            .collect();
        // Restore original order
        selected.sort_by_key(|&(idx, _)| idx);
        selected.into_iter().map(|(_, v)| v).collect()
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (max-subsequence nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ([pairs (for/list ([v nums] [i (in-naturals)]) (cons i v))]
         [sorted-by-val (sort pairs (lambda (a b) (> (cdr a) (cdr b))))]
         [topk (take sorted-by-val k)]
         [sorted-by-idx (sort topk (lambda (a b) (< (car a) (car b))))]
         [result (map cdr sorted-by-idx)])
    result))
```

## Erlang

```erlang
-spec max_subsequence(Nums :: [integer()], K :: integer()) -> [integer()].
max_subsequence(Nums, K) ->
    Indexed = lists:zip(lists:seq(0, length(Nums) - 1), Nums),
    DescSorted = lists:sort(fun({_, V1}, {_, V2}) -> V1 > V2 end, Indexed),
    TopK = lists:sublist(DescSorted, K),
    AscSorted = lists:sort(fun({I1, _}, {I2, _}) -> I1 < I2 end, TopK),
    [Val || {_, Val} <- AscSorted].
```

## Elixir

```elixir
defmodule Solution do
  @spec max_subsequence(nums :: [integer], k :: integer) :: [integer]
  def max_subsequence(nums, k) do
    nums
    |> Enum.with_index()
    |> Enum.sort_by(fn {val, _idx} -> -val end)
    |> Enum.take(k)
    |> Enum.sort_by(fn {_val, idx} -> idx end)
    |> Enum.map(fn {val, _idx} -> val end)
  end
end
```

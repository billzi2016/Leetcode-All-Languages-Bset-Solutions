# 2831. Find the Longest Equal Subarray

## Cpp

```cpp
class Solution {
public:
    int longestEqualSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> pos(n + 1);
        for (int i = 0; i < n; ++i) {
            pos[nums[i]].push_back(i);
        }
        int ans = 0;
        for (auto& v : pos) {
            if (v.empty()) continue;
            int l = 0;
            for (int r = 0; r < (int)v.size(); ++r) {
                while (l <= r && (v[r] - v[l]) - (r - l) > k) {
                    ++l;
                }
                ans = max(ans, r - l + 1);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestEqualSubarray(List<Integer> nums, int k) {
        int n = nums.size();
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int v = nums.get(i);
            map.computeIfAbsent(v, x -> new ArrayList<>()).add(i);
        }
        int best = 0;
        for (List<Integer> pos : map.values()) {
            int left = 0;
            for (int right = 0; right < pos.size(); right++) {
                while (left <= right && (pos.get(right) - pos.get(left) - (right - left)) > k) {
                    left++;
                }
                int len = right - left + 1;
                if (len > best) best = len;
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def longestEqualSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = 0
        for lst in pos.values():
            left = 0
            for right in range(len(lst)):
                # deletions needed to make the segment [lst[left], lst[right]] all equal to current value
                while lst[right] - lst[left] + 1 - (right - left + 1) > k:
                    left += 1
                cur_len = right - left + 1
                if cur_len > ans:
                    ans = cur_len
        return ans
```

## Python3

```python
from collections import defaultdict
from typing import List

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = 0
        for indices in pos.values():
            l = 0
            for r in range(len(indices)):
                while indices[r] - indices[l] - (r - l) > k:
                    l += 1
                cur = r - l + 1
                if cur > ans:
                    ans = cur
        return ans
```

## C

```c
#include <stdlib.h>

int longestEqualSubarray(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    int maxVal = numsSize;  // per constraints: 1 <= nums[i] <= nums.length

    struct Vec {
        int *data;
        int sz;
        int cap;
    };
    struct Vec *vecs = calloc(maxVal + 1, sizeof(struct Vec));

    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        struct Vec *vct = &vecs[v];
        if (vct->sz == vct->cap) {
            int newCap = vct->cap ? vct->cap * 2 : 1;
            vct->data = realloc(vct->data, newCap * sizeof(int));
            vct->cap = newCap;
        }
        vct->data[vct->sz++] = i;
    }

    int ans = 0;
    for (int val = 1; val <= maxVal; ++val) {
        struct Vec *vct = &vecs[val];
        int sz = vct->sz;
        if (sz == 0) continue;

        int left = 0;
        for (int right = 0; right < sz; ++right) {
            while (left <= right &&
                   ((vct->data[right] - vct->data[left] + 1) -
                    (right - left + 1)) > k) {
                ++left;
            }
            int len = right - left + 1;
            if (len > ans) ans = len;
        }
    }

    for (int val = 1; val <= maxVal; ++val) {
        free(vecs[val].data);
    }
    free(vecs);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int LongestEqualSubarray(IList<int> nums, int k) {
        var positions = new Dictionary<int, List<int>>();
        for (int i = 0; i < nums.Count; i++) {
            int val = nums[i];
            if (!positions.ContainsKey(val)) positions[val] = new List<int>();
            positions[val].Add(i);
        }

        int best = 0;
        foreach (var kvp in positions) {
            var list = kvp.Value;
            int left = 0;
            for (int right = 0; right < list.Count; right++) {
                // deletions needed to make elements between list[left] and list[right] all equal
                while ((list[right] - list[left] + 1) - (right - left + 1) > k) {
                    left++;
                }
                int len = right - left + 1;
                if (len > best) best = len;
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestEqualSubarray = function(nums, k) {
    const posMap = new Map();
    for (let i = 0; i < nums.length; ++i) {
        const v = nums[i];
        if (!posMap.has(v)) posMap.set(v, []);
        posMap.get(v).push(i);
    }
    let best = 0;
    for (const arr of posMap.values()) {
        let left = 0;
        for (let right = 0; right < arr.length; ++right) {
            // deletions needed to make segment [arr[left], arr[right]] all equal
            while ((arr[right] - arr[left] + 1) - (right - left + 1) > k) {
                ++left;
            }
            const len = right - left + 1;
            if (len > best) best = len;
        }
    }
    return best;
};
```

## Typescript

```typescript
function longestEqualSubarray(nums: number[], k: number): number {
    const indexMap = new Map<number, number[]>();
    for (let i = 0; i < nums.length; i++) {
        const v = nums[i];
        if (!indexMap.has(v)) indexMap.set(v, []);
        indexMap.get(v)!.push(i);
    }

    let best = 0;
    for (const positions of indexMap.values()) {
        let left = 0;
        for (let right = 0; right < positions.length; right++) {
            while (
                left <= right &&
                (positions[right] - positions[left] + 1) - (right - left + 1) > k
            ) {
                left++;
            }
            const len = right - left + 1;
            if (len > best) best = len;
        }
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function longestEqualSubarray($nums, $k) {
        $pos = [];
        foreach ($nums as $i => $v) {
            if (!isset($pos[$v])) {
                $pos[$v] = [];
            }
            $pos[$v][] = $i;
        }

        $ans = 0;
        foreach ($pos as $indices) {
            $l = 0;
            $len = count($indices);
            for ($r = 0; $r < $len; $r++) {
                while (true) {
                    $deletions = ($indices[$r] - $indices[$l] + 1) - ($r - $l + 1);
                    if ($deletions <= $k) {
                        break;
                    }
                    $l++;
                }
                $curr = $r - $l + 1;
                if ($curr > $ans) {
                    $ans = $curr;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestEqualSubarray(_ nums: [Int], _ k: Int) -> Int {
        var positions = [Int: [Int]]()
        for (idx, val) in nums.enumerated() {
            positions[val, default: []].append(idx)
        }
        var best = 0
        for arr in positions.values {
            var left = 0
            let m = arr.count
            for right in 0..<m {
                while left <= right && (arr[right] - arr[left]) - (right - left) > k {
                    left += 1
                }
                let len = right - left + 1
                if len > best { best = len }
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestEqualSubarray(nums: List<Int>, k: Int): Int {
        val indexMap = HashMap<Int, MutableList<Int>>()
        for (i in nums.indices) {
            val v = nums[i]
            indexMap.getOrPut(v) { mutableListOf() }.add(i)
        }
        var answer = 0
        for (list in indexMap.values) {
            var left = 0
            for (right in list.indices) {
                while (left <= right && (list[right] - list[left] + 1 - (right - left + 1)) > k) {
                    left++
                }
                val cnt = right - left + 1
                if (cnt > answer) answer = cnt
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int longestEqualSubarray(List<int> nums, int k) {
    final Map<int, List<int>> positions = {};
    for (int i = 0; i < nums.length; i++) {
      positions.putIfAbsent(nums[i], () => []).add(i);
    }

    int best = 0;
    for (var posList in positions.values) {
      int left = 0;
      for (int right = 0; right < posList.length; right++) {
        while (left <= right &&
            (posList[right] - posList[left] - (right - left)) > k) {
          left++;
        }
        int length = right - left + 1;
        if (length > best) best = length;
      }
    }

    return best;
  }
}
```

## Golang

```go
func longestEqualSubarray(nums []int, k int) int {
    posMap := make(map[int][]int)
    for i, v := range nums {
        posMap[v] = append(posMap[v], i)
    }
    ans := 0
    for _, positions := range posMap {
        l := 0
        for r := 0; r < len(positions); r++ {
            // deletions needed to make subarray equal to the current value
            for l <= r && (positions[r]-positions[l]+1)-(r-l+1) > k {
                l++
            }
            if cur := r - l + 1; cur > ans {
                ans = cur
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def longest_equal_subarray(nums, k)
  positions = Hash.new { |h, key| h[key] = [] }
  nums.each_with_index do |val, idx|
    positions[val] << idx
  end

  best = 0
  positions.each_value do |arr|
    l = 0
    arr.each_with_index do |right_idx, r|
      while l <= r && (right_idx - arr[l] - (r - l)) > k
        l += 1
      end
      len = r - l + 1
      best = len if len > best
    end
  end

  best
end
```

## Scala

```scala
object Solution {
    def longestEqualSubarray(nums: List[Int], k: Int): Int = {
        import scala.collection.mutable.{Map, ArrayBuffer}
        val posMap = Map[Int, ArrayBuffer[Int]]()
        for ((v, idx) <- nums.zipWithIndex) {
            posMap.getOrElseUpdate(v, ArrayBuffer()).append(idx)
        }
        var answer = 0
        for ((_, positions) <- posMap) {
            var left = 0
            val m = positions.length
            for (right <- 0 until m) {
                while (left <= right && (positions(right) - positions(left)) - (right - left) > k) {
                    left += 1
                }
                val len = right - left + 1
                if (len > answer) answer = len
            }
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_equal_subarray(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut positions: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
        for (i, &v) in nums.iter().enumerate() {
            positions[v as usize].push(i);
        }
        let k_usize = k as usize;
        let mut best = 0usize;

        for idxs in positions.iter() {
            if idxs.is_empty() {
                continue;
            }
            let mut left = 0usize;
            for right in 0..idxs.len() {
                while left <= right && (idxs[right] - idxs[left]) - (right - left) > k_usize {
                    left += 1;
                }
                let len = right - left + 1;
                if len > best {
                    best = len;
                }
            }
        }

        best as i32
    }
}
```

## Racket

```racket
(define/contract (longest‑equal‑subarray nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([ht (make-hash)])
    ;; build hash: value -> list of indices (in reverse order)
    (let loop ((lst nums) (idx 0))
      (cond [(null? lst) (void)]
            [else
             (let* ((val (car lst))
                    (prev (hash-ref ht val '())))
               (hash-set! ht val (cons idx prev)))
             (loop (cdr lst) (+ idx 1))]))
    (define maxlen 0)
    ;; process each value's index list
    (for ([idx-list (in-hash-values ht)])
      (let* ((vec (list->vector (reverse idx‑list)))
             (m   (vector-length vec))
             (l   0))
        (for ([r (in-range m)])
          (let loop ()
            (when (and (< l r)
                       (> (- (- (vector-ref vec r) (vector-ref vec l))
                             (- r l))
                          k))
              (set! l (+ l 1))
              (loop)))
          (set! maxlen (max maxlen (+ 1 (- r l)))))))
    maxlen))
```

## Erlang

```erlang
-module(solution).
-export([longest_equal_subarray/2]).

-spec longest_equal_subarray(Nums :: [integer()], K :: integer()) -> integer().
longest_equal_subarray(Nums, K) ->
    Map = build_map(Nums, 0, #{}),
    maps:fold(fun(_Key, RevIndices, Acc) ->
        Indices = lists:reverse(RevIndices),
        Len = max_len_for_indices(Indices, K),
        if Len > Acc -> Len; true -> Acc end
    end, 0, Map).

build_map([], _Idx, Map) -> Map;
build_map([H|T], Idx, Map) ->
    RevList = maps:get(H, Map, []),
    NewMap = maps:put(H, [Idx|RevList], Map),
    build_map(T, Idx + 1, NewMap).

max_len_for_indices([], _K) -> 0;
max_len_for_indices(Indices, K) ->
    Tuple = list_to_tuple(Indices),
    N = tuple_size(Tuple),
    slide(0, 0, 0, Tuple, N, K).

slide(L, R, Max, _Tuple, N, _K) when R =:= N -> Max;
slide(L, R, Max, Tuple, N, K) ->
    LeftIdx = element(L + 1, Tuple),
    RightIdx = element(R + 1, Tuple),
    Deletions = (RightIdx - LeftIdx) - (R - L),
    if
        Deletions =< K ->
            NewMax = case R - L + 1 > Max of true -> R - L + 1; false -> Max end,
            slide(L, R + 1, NewMax, Tuple, N, K);
        true ->
            slide(L + 1, R, Max, Tuple, N, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_equal_subarray(nums :: [integer], k :: integer) :: integer
  def longest_equal_subarray(nums, k) do
    # Build map from value to list of its indices (ascending order)
    indices_map =
      Enum.with_index(nums)
      |> Enum.reduce(%{}, fn {val, idx}, acc ->
        Map.update(acc, val, [idx], &[idx | &1])
      end)
      |> Enum.map(fn {key, rev_list} -> {key, Enum.reverse(rev_list)} end)
      |> Enum.into(%{})

    # Process each value independently with sliding window
    Enum.reduce(indices_map, 0, fn {_val, idxs}, global_max ->
      n = length(idxs)
      tup = List.to_tuple(idxs)

      {_, best} =
        Enum.reduce(0..(n - 1), {0, global_max}, fn r, {l, cur_max} ->
          l = adjust_left(l, r, tup, k)

          cur_len = r - l + 1
          new_max = if cur_len > cur_max, do: cur_len, else: cur_max
          {l, new_max}
        end)

      best
    end)
  end

  defp adjust_left(l, r, tup, k) do
    if l <= r and (elem(tup, r) - elem(tup, l)) - (r - l) > k do
      adjust_left(l + 1, r, tup, k)
    else
      l
    end
  end
end
```

# 2593. Find Score of an Array After Marking All Elements

## Cpp

```cpp
class Solution {
public:
    long long findScore(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<std::pair<int,int>> order;
        order.reserve(n);
        for (int i = 0; i < n; ++i) order.emplace_back(nums[i], i);
        std::sort(order.begin(), order.end(),
                  [](const auto& a, const auto& b){
                      if (a.first != b.first) return a.first < b.first;
                      return a.second < b.second;
                  });
        std::vector<char> marked(n, 0);
        long long ans = 0;
        for (auto [val, idx] : order) {
            if (!marked[idx]) {
                ans += val;
                marked[idx] = 1;
                if (idx > 0) marked[idx - 1] = 1;
                if (idx + 1 < n) marked[idx + 1] = 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long findScore(int[] nums) {
        int n = nums.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> {
            if (nums[a] != nums[b]) return Integer.compare(nums[a], nums[b]);
            return Integer.compare(a, b);
        });
        boolean[] marked = new boolean[n];
        long score = 0L;
        for (int idx : order) {
            if (!marked[idx]) {
                score += nums[idx];
                marked[idx] = true;
                if (idx - 1 >= 0) marked[idx - 1] = true;
                if (idx + 1 < n) marked[idx + 1] = true;
            }
        }
        return score;
    }
}
```

## Python

```python
class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        marked = [False] * n
        # pair each number with its index and sort by value then index
        order = sorted(((val, idx) for idx, val in enumerate(nums)), key=lambda x: (x[0], x[1]))
        score = 0
        for val, idx in order:
            if not marked[idx]:
                score += val
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx + 1 < n:
                    marked[idx + 1] = True
        return score
```

## Python3

```python
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        order = [(nums[i], i) for i in range(n)]
        order.sort(key=lambda x: (x[0], x[1]))
        score = 0
        for val, idx in order:
            if not marked[idx]:
                score += val
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx + 1 < n:
                    marked[idx + 1] = True
        return score
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int idx;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->val != pb->val)
        return pa->val - pb->val;          // ascending by value
    return pa->idx - pb->idx;              // tie‑break by index (leftmost first)
}

long long findScore(int* nums, int numsSize) {
    if (numsSize == 0) return 0LL;

    Pair *arr = (Pair *)malloc(numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; ++i) {
        arr[i].val = nums[i];
        arr[i].idx = i;
    }

    qsort(arr, numsSize, sizeof(Pair), cmpPair);

    char *marked = (char *)calloc(numsSize, sizeof(char));
    long long score = 0LL;

    for (int i = 0; i < numsSize; ++i) {
        int idx = arr[i].idx;
        if (!marked[idx]) {
            score += arr[i].val;
            marked[idx] = 1;
            if (idx > 0)     marked[idx - 1] = 1;
            if (idx + 1 < numsSize) marked[idx + 1] = 1;
        }
    }

    free(arr);
    free(marked);
    return score;
}
```

## Csharp

```csharp
public class Solution
{
    public long FindScore(int[] nums)
    {
        int n = nums.Length;
        var pairs = new (int val, int idx)[n];
        for (int i = 0; i < n; i++)
            pairs[i] = (nums[i], i);

        Array.Sort(pairs, (a, b) =>
        {
            int cmp = a.val.CompareTo(b.val);
            return cmp != 0 ? cmp : a.idx.CompareTo(b.idx);
        });

        bool[] marked = new bool[n];
        long ans = 0;

        foreach (var p in pairs)
        {
            int i = p.idx;
            if (!marked[i])
            {
                ans += p.val;
                marked[i] = true;
                if (i > 0) marked[i - 1] = true;
                if (i + 1 < n) marked[i + 1] = true;
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
 * @return {number}
 */
var findScore = function(nums) {
    const n = nums.length;
    const pairs = nums.map((v, i) => [v, i]);
    pairs.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);

    const marked = new Array(n).fill(false);
    let score = 0;

    for (const [val, idx] of pairs) {
        if (!marked[idx]) {
            score += val;
            marked[idx] = true;
            if (idx > 0) marked[idx - 1] = true;
            if (idx + 1 < n) marked[idx + 1] = true;
        }
    }

    return score;
};
```

## Typescript

```typescript
function findScore(nums: number[]): number {
    const n = nums.length;
    const pairs: [number, number][] = new Array(n);
    for (let i = 0; i < n; i++) {
        pairs[i] = [nums[i], i];
    }
    pairs.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
    const marked = new Array(n).fill(false);
    let ans = 0;
    for (const [val, idx] of pairs) {
        if (!marked[idx]) {
            ans += val;
            marked[idx] = true;
            if (idx > 0) marked[idx - 1] = true;
            if (idx + 1 < n) marked[idx + 1] = true;
        }
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
    function findScore($nums) {
        $n = count($nums);
        $pairs = [];
        for ($i = 0; $i < $n; $i++) {
            $pairs[] = [$nums[$i], $i];
        }
        usort($pairs, function ($a, $b) {
            if ($a[0] == $b[0]) {
                return $a[1] <=> $b[1];
            }
            return $a[0] <=> $b[0];
        });
        $marked = array_fill(0, $n, false);
        $ans = 0;
        foreach ($pairs as $p) {
            [$val, $idx] = $p;
            if (!$marked[$idx]) {
                $ans += $val;
                $marked[$idx] = true;
                if ($idx > 0) {
                    $marked[$idx - 1] = true;
                }
                if ($idx < $n - 1) {
                    $marked[$idx + 1] = true;
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
    func findScore(_ nums: [Int]) -> Int {
        let n = nums.count
        var indexed = [(value: Int, index: Int)]()
        indexed.reserveCapacity(n)
        for (i, v) in nums.enumerated() {
            indexed.append((v, i))
        }
        indexed.sort { a, b in
            if a.value == b.value {
                return a.index < b.index
            }
            return a.value < b.value
        }
        
        var marked = [Bool](repeating: false, count: n)
        var score = 0
        
        for pair in indexed {
            let idx = pair.index
            if !marked[idx] {
                score += pair.value
                marked[idx] = true
                if idx > 0 { marked[idx - 1] = true }
                if idx + 1 < n { marked[idx + 1] = true }
            }
        }
        
        return score
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findScore(nums: IntArray): Long {
        val n = nums.size
        val pairs = Array(n) { i -> Pair(nums[i], i) }
        pairs.sortBy { it.first }
        val marked = BooleanArray(n)
        var ans = 0L
        for ((value, idx) in pairs) {
            if (!marked[idx]) {
                ans += value.toLong()
                marked[idx] = true
                if (idx > 0) marked[idx - 1] = true
                if (idx + 1 < n) marked[idx + 1] = true
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findScore(List<int> nums) {
    int n = nums.length;
    List<int> order = List.generate(n, (i) => i);
    order.sort((a, b) {
      if (nums[a] != nums[b]) return nums[a] - nums[b];
      return a - b;
    });
    List<bool> marked = List.filled(n, false);
    int ans = 0;
    for (int idx in order) {
      if (!marked[idx]) {
        ans += nums[idx];
        marked[idx] = true;
        if (idx > 0) marked[idx - 1] = true;
        if (idx + 1 < n) marked[idx + 1] = true;
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func findScore(nums []int) int64 {
	type pair struct {
		val int
		idx int
	}
	n := len(nums)
	pairs := make([]pair, n)
	for i, v := range nums {
		pairs[i] = pair{val: v, idx: i}
	}
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].val == pairs[j].val {
			return pairs[i].idx < pairs[j].idx
		}
		return pairs[i].val < pairs[j].val
	})
	marked := make([]bool, n)
	var ans int64
	for _, p := range pairs {
		if !marked[p.idx] {
			ans += int64(p.val)
			marked[p.idx] = true
			if p.idx > 0 {
				marked[p.idx-1] = true
			}
			if p.idx+1 < n {
				marked[p.idx+1] = true
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_score(nums)
  n = nums.length
  pairs = []
  nums.each_with_index { |v, i| pairs << [v, i] }
  pairs.sort_by! { |v, i| [v, i] }

  marked = Array.new(n, false)
  score = 0

  pairs.each do |value, idx|
    next if marked[idx]

    score += value
    marked[idx] = true
    marked[idx - 1] = true if idx > 0
    marked[idx + 1] = true if idx + 1 < n
  end

  score
end
```

## Scala

```scala
object Solution {
    def findScore(nums: Array[Int]): Long = {
        val n = nums.length
        val indexed = nums.zipWithIndex.map { case (v, i) => (v, i) }
        val sorted = indexed.sortBy(p => (p._1, p._2))
        val marked = new Array[Boolean](n)
        var ans: Long = 0L

        for ((value, idx) <- sorted) {
            if (!marked(idx)) {
                ans += value.toLong
                marked(idx) = true
                if (idx > 0) marked(idx - 1) = true
                if (idx + 1 < n) marked(idx + 1) = true
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_score(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut indexed: Vec<(i32, usize)> = nums.iter().enumerate().map(|(i, &v)| (v, i)).collect();
        indexed.sort_by(|a, b| a.0.cmp(&b.0).then(a.1.cmp(&b.1)));
        let mut marked = vec![false; n];
        let mut ans: i64 = 0;
        for &(val, idx) in &indexed {
            if !marked[idx] {
                ans += val as i64;
                marked[idx] = true;
                if idx > 0 {
                    marked[idx - 1] = true;
                }
                if idx + 1 < n {
                    marked[idx + 1] = true;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-score nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (pairs (for/list ([i (in-range n)])
                  (cons (vector-ref vec i) i)))
         (sorted-pairs
          (sort pairs
                (lambda (a b)
                  (let ((va (car a)) (vb (car b)))
                    (if (= va vb)
                        (< (cdr a) (cdr b))
                        (< va vb)))))))
    (define marked (make-vector n #f))
    (define ans 0)
    (for ([p sorted-pairs])
      (define idx (cdr p))
      (unless (vector-ref marked idx)
        (set! ans (+ ans (car p)))
        (vector-set! marked idx #t)
        (when (> idx 0) (vector-set! marked (- idx 1) #t))
        (when (< idx (- n 1)) (vector-set! marked (+ idx 1) #t))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([find_score/1]).

-spec find_score(Nums :: [integer()]) -> integer().
find_score(Nums) ->
    Len = length(Nums),
    Indexed = lists:zip(Nums, lists:seq(0, Len - 1)),
    Sorted = lists:keysort(1, Indexed),
    compute(Sorted, #{}, 0, Len).

compute([], _Marked, Acc, _Len) -> Acc;
compute([{Val, Idx} | Rest], Marked, Acc, Len) ->
    case maps:is_key(Idx, Marked) of
        true ->
            compute(Rest, Marked, Acc, Len);
        false ->
            NewAcc = Acc + Val,
            M1 = maps:put(Idx, true, Marked),
            M2 = if Idx > 0 -> maps:put(Idx - 1, true, M1); true -> M1 end,
            M3 = if Idx < Len - 1 -> maps:put(Idx + 1, true, M2); true -> M2 end,
            compute(Rest, M3, NewAcc, Len)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_score(nums :: [integer]) :: integer
  def find_score(nums) do
    n = length(nums)

    sorted =
      nums
      |> Enum.with_index()
      |> Enum.sort_by(fn {v, i} -> {v, i} end)

    marked = :array.new(n, default: false)
    process(sorted, marked, 0, n)
  end

  defp process([], _marked, acc, _n), do: acc

  defp process([{val, idx} | rest], marked, acc, n) do
    if :array.get(idx, marked) do
      process(rest, marked, acc, n)
    else
      marked = :array.set(idx, true, marked)

      marked =
        if idx > 0 do
          :array.set(idx - 1, true, marked)
        else
          marked
        end

      marked =
        if idx + 1 < n do
          :array.set(idx + 1, true, marked)
        else
          marked
        end

      process(rest, marked, acc + val, n)
    end
  end
end
```

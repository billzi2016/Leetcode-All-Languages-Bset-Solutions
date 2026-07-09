# 0315. Count of Smaller Numbers After Self

## Cpp

```cpp
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> sorted(nums);
        sort(sorted.begin(), sorted.end());
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
        int m = sorted.size();
        vector<int> bit(m + 2, 0);
        auto add = [&](int idx, int val) {
            for (int i = idx; i <= m; i += i & -i) bit[i] += val;
        };
        auto sum = [&](int idx) {
            int res = 0;
            for (int i = idx; i > 0; i -= i & -i) res += bit[i];
            return res;
        };
        vector<int> result(n);
        for (int i = n - 1; i >= 0; --i) {
            int rank = lower_bound(sorted.begin(), sorted.end(), nums[i]) - sorted.begin() + 1;
            result[i] = sum(rank - 1);
            add(rank, 1);
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        List<Integer> result = new ArrayList<>(n);
        if (n == 0) return result;

        // Coordinate compression
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        Map<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;
        for (int v : sorted) {
            if (!rankMap.containsKey(v)) {
                rankMap.put(v, rank++);
            }
        }

        FenwickTree bit = new FenwickTree(rank);
        for (int i = n - 1; i >= 0; --i) {
            int r = rankMap.get(nums[i]);
            result.add(bit.query(r - 1));
            bit.update(r, 1);
        }
        Collections.reverse(result);
        return result;
    }

    private static class FenwickTree {
        private final int[] tree;

        FenwickTree(int size) {
            tree = new int[size + 2];
        }

        void update(int index, int delta) {
            while (index < tree.length) {
                tree[index] += delta;
                index += index & -index;
            }
        }

        int query(int index) {
            int sum = 0;
            while (index > 0) {
                sum += tree[index];
                index -= index & -index;
            }
            return sum;
        }
    }
}
```

## Python

```python
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        # Coordinate compression
        sorted_unique = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}  # 1-indexed ranks

        class Fenwick:
            __slots__ = ('n', 'bit')
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)
            def update(self, i, delta):
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def query(self, i):
                s = 0
                while i:
                    s += self.bit[i]
                    i -= i & -i
                return s

        ft = Fenwick(len(sorted_unique))
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            r = rank[nums[i]]
            res[i] = ft.query(r - 1)
            ft.update(r, 1)
        return res
```

## Python3

```python
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        ans = [0] * n
        enum = list(enumerate(nums))

        def sort(enum_list):
            half = len(enum_list) // 2
            if half:
                left = sort(enum_list[:half])
                right = sort(enum_list[half:])
                i = j = 0
                while i < len(left) or j < len(right):
                    if j == len(right) or (i < len(left) and left[i][1] <= right[j][1]):
                        ans[left[i][0]] += j
                        enum_list[i + j] = left[i]
                        i += 1
                    else:
                        enum_list[i + j] = right[j]
                        j += 1
            return enum_list

        sort(enum)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

static void bit_update(int *bit, int n, int idx, int delta) {
    while (idx <= n) {
        bit[idx] += delta;
        idx += idx & -idx;
    }
}

static int bit_query(int *bit, int idx) {
    int sum = 0;
    while (idx > 0) {
        sum += bit[idx];
        idx -= idx & -idx;
    }
    return sum;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countSmaller(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    // Copy and sort for coordinate compression
    int *sorted = (int *)malloc(numsSize * sizeof(int));
    memcpy(sorted, nums, numsSize * sizeof(int));
    qsort(sorted, numsSize, sizeof(int), cmp_int);

    // Deduplicate
    int *uniq = (int *)malloc(numsSize * sizeof(int));
    int uniqSize = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || sorted[i] != sorted[i - 1]) {
            uniq[uniqSize++] = sorted[i];
        }
    }
    free(sorted);

    // Map each number to its rank (1‑based)
    int *ranks = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        int l = 0, r = uniqSize - 1;
        while (l <= r) {
            int m = (l + r) >> 1;
            if (uniq[m] == nums[i]) {
                ranks[i] = m + 1; // BIT is 1‑based
                break;
            } else if (uniq[m] < nums[i]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
    }

    // Fenwick tree
    int *bit = (int *)calloc(uniqSize + 2, sizeof(int));
    int *result = (int *)malloc(numsSize * sizeof(int));

    for (int i = numsSize - 1; i >= 0; --i) {
        int idx = ranks[i];
        result[i] = bit_query(bit, idx - 1);
        bit_update(bit, uniqSize, idx, 1);
    }

    free(uniq);
    free(ranks);
    free(bit);

    *returnSize = numsSize;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> CountSmaller(int[] nums) {
        int n = nums.Length;
        var result = new List<int>(new int[n]);
        if (n == 0) return result;
        
        int[] counts = new int[n];
        int[] indexes = new int[n];
        for (int i = 0; i < n; i++) indexes[i] = i;

        void MergeSort(int left, int right) {
            if (right - left <= 1) return;
            int mid = (left + right) >> 1;
            MergeSort(left, mid);
            MergeSort(mid, right);

            int[] temp = new int[right - left];
            int i = left, j = mid, k = 0;
            int rightCount = 0;

            while (i < mid && j < right) {
                if (nums[indexes[j]] < nums[indexes[i]]) {
                    temp[k++] = indexes[j++];
                    rightCount++;
                } else {
                    counts[indexes[i]] += rightCount;
                    temp[k++] = indexes[i++];
                }
            }

            while (i < mid) {
                counts[indexes[i]] += rightCount;
                temp[k++] = indexes[i++];
            }

            while (j < right) {
                temp[k++] = indexes[j++];
            }

            for (int p = 0; p < temp.Length; p++) {
                indexes[left + p] = temp[p];
            }
        }

        MergeSort(0, n);
        for (int i = 0; i < n; i++) result[i] = counts[i];
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
var countSmaller = function(nums) {
    const n = nums.length;
    const result = new Array(n);
    
    // Coordinate compression
    const uniq = Array.from(new Set(nums)).sort((a, b) => a - b);
    const rankMap = new Map();
    for (let i = 0; i < uniq.length; i++) {
        rankMap.set(uniq[i], i + 1); // 1-indexed for BIT
    }
    
    const size = uniq.length + 2;
    const bit = new Array(size).fill(0);
    
    const update = (i, delta) => {
        while (i < size) {
            bit[i] += delta;
            i += i & -i;
        }
    };
    
    const query = (i) => {
        let sum = 0;
        while (i > 0) {
            sum += bit[i];
            i -= i & -i;
        }
        return sum;
    };
    
    for (let i = n - 1; i >= 0; --i) {
        const idx = rankMap.get(nums[i]);
        result[i] = query(idx - 1);
        update(idx, 1);
    }
    
    return result;
};
```

## Typescript

```typescript
function countSmaller(nums: number[]): number[] {
    const n = nums.length;
    if (n === 0) return [];

    // Coordinate compression
    const sorted = Array.from(new Set(nums)).sort((a, b) => a - b);
    const rankMap = new Map<number, number>();
    for (let i = 0; i < sorted.length; i++) {
        rankMap.set(sorted[i], i + 1); // 1-indexed ranks
    }

    class BIT {
        private tree: number[];
        private size: number;
        constructor(size: number) {
            this.size = size;
            this.tree = new Array(size + 1).fill(0);
        }
        update(index: number, delta: number): void {
            while (index <= this.size) {
                this.tree[index] += delta;
                index += index & -index;
            }
        }
        query(index: number): number {
            let sum = 0;
            while (index > 0) {
                sum += this.tree[index];
                index -= index & -index;
            }
            return sum;
        }
    }

    const bit = new BIT(sorted.length);
    const result = new Array<number>(n);

    for (let i = n - 1; i >= 0; i--) {
        const rank = rankMap.get(nums[i])!;
        result[i] = bit.query(rank - 1); // count of smaller elements to the right
        bit.update(rank, 1);
    }

    return result;
}
```

## Php

```php
class BIT {
    private int $size;
    private array $tree;

    public function __construct(int $n) {
        $this->size = $n;
        $this->tree = array_fill(0, $n + 2, 0);
    }

    public function update(int $index, int $delta): void {
        while ($index <= $this->size) {
            $this->tree[$index] += $delta;
            $index += $index & (-$index);
        }
    }

    public function query(int $index): int {
        $sum = 0;
        while ($index > 0) {
            $sum += $this->tree[$index];
            $index -= $index & (-$index);
        }
        return $sum;
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function countSmaller($nums) {
        $n = count($nums);
        if ($n === 0) {
            return [];
        }

        // Coordinate compression
        $sorted = $nums;
        sort($sorted, SORT_NUMERIC);
        $unique = array_values(array_unique($sorted));
        $rankMap = [];
        foreach ($unique as $i => $val) {
            $rankMap[$val] = $i + 1; // 1-indexed ranks
        }

        $bit = new BIT(count($unique) + 2);
        $result = array_fill(0, $n, 0);

        for ($i = $n - 1; $i >= 0; --$i) {
            $rank = $rankMap[$nums[$i]];
            $result[$i] = $bit->query($rank - 1);
            $bit->update($rank, 1);
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countSmaller(_ nums: [Int]) -> [Int] {
        guard !nums.isEmpty else { return [] }
        
        // Coordinate compression
        let sortedUnique = Array(Set(nums)).sorted()
        var indexMap = [Int:Int]()
        for (i, v) in sortedUnique.enumerated() {
            indexMap[v] = i + 1   // BIT is 1-indexed
        }
        
        // Fenwick Tree (Binary Indexed Tree)
        class BIT {
            private var tree: [Int]
            init(_ size: Int) {
                tree = Array(repeating: 0, count: size + 2)
            }
            func update(_ idx: Int, _ delta: Int) {
                var i = idx
                while i < tree.count {
                    tree[i] += delta
                    i += i & -i
                }
            }
            func query(_ idx: Int) -> Int {
                var i = idx
                var sum = 0
                while i > 0 {
                    sum += tree[i]
                    i -= i & -i
                }
                return sum
            }
        }
        
        let bit = BIT(sortedUnique.count)
        var result = Array(repeating: 0, count: nums.count)
        
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            let idx = indexMap[nums[i]]!
            // Count of numbers smaller than current
            result[i] = bit.query(idx - 1)
            // Insert current number into BIT
            bit.update(idx, 1)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSmaller(nums: IntArray): List<Int> {
        if (nums.isEmpty()) return emptyList()
        // Coordinate compression
        val sorted = nums.distinct().sorted()
        val rankMap = HashMap<Int, Int>(sorted.size)
        for ((i, v) in sorted.withIndex()) {
            rankMap[v] = i + 1 // 1-based index for BIT
        }
        val bit = FenwickTree(sorted.size)
        val result = IntArray(nums.size)
        for (i in nums.indices.reversed()) {
            val r = rankMap[nums[i]]!!
            result[i] = bit.query(r - 1)
            bit.update(r, 1)
        }
        return result.toList()
    }

    private class FenwickTree(private val n: Int) {
        private val tree = IntArray(n + 1)

        fun update(index: Int, delta: Int) {
            var i = index
            while (i <= n) {
                tree[i] += delta
                i += i and -i
            }
        }

        fun query(index: Int): Int {
            var sum = 0
            var i = index
            while (i > 0) {
                sum += tree[i]
                i -= i and -i
            }
            return sum
        }
    }
}
```

## Dart

```dart
class Solution {
  List<int> countSmaller(List<int> nums) {
    int n = nums.length;
    if (n == 0) return [];

    // Coordinate compression
    List<int> sorted = List.from(nums);
    sorted.sort();
    List<int> uniq = [];
    int? prev;
    for (int v in sorted) {
      if (prev == null || v != prev) {
        uniq.add(v);
        prev = v;
      }
    }

    Map<int, int> rank = {};
    for (int i = 0; i < uniq.length; i++) {
      // BIT is 1-indexed
      rank[uniq[i]] = i + 1;
    }

    // Fenwick Tree
    List<int> bit = List.filled(uniq.length + 2, 0);
    void update(int idx) {
      while (idx < bit.length) {
        bit[idx] += 1;
        idx += idx & -idx;
      }
    }

    int query(int idx) {
      int sum = 0;
      while (idx > 0) {
        sum += bit[idx];
        idx -= idx & -idx;
      }
      return sum;
    }

    List<int> result = List.filled(n, 0);
    for (int i = n - 1; i >= 0; i--) {
      int r = rank[nums[i]]!;
      result[i] = query(r - 1);
      update(r);
    }
    return result;
  }
}
```

## Golang

```go
package main

import "sort"

type BIT struct {
	tree []int
}

func NewBIT(n int) *BIT {
	return &BIT{make([]int, n)}
}

func (b *BIT) Update(i, delta int) {
	for i < len(b.tree) {
		b.tree[i] += delta
		i += i & -i
	}
}

func (b *BIT) Query(i int) int {
	sum := 0
	for i > 0 {
		sum += b.tree[i]
		i -= i & -i
	}
	return sum
}

func countSmaller(nums []int) []int {
	n := len(nums)
	if n == 0 {
		return []int{}
	}
	vals := make([]int, n)
	copy(vals, nums)
	sort.Ints(vals)

	uniq := make([]int, 0, n)
	for _, v := range vals {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}

	idxMap := make(map[int]int, len(uniq))
	for i, v := range uniq {
		idxMap[v] = i + 1 // 1‑based index for BIT
	}

	bit := NewBIT(len(uniq) + 2)

	res := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		idx := idxMap[nums[i]]
		res[i] = bit.Query(idx - 1)
		bit.Update(idx, 1)
	}
	return res
}
```

## Ruby

```ruby
def count_smaller(nums)
  return [] if nums.empty?
  sorted = nums.uniq.sort
  rank = {}
  sorted.each_with_index { |v, i| rank[v] = i + 1 }
  size = sorted.size
  bit = Array.new(size + 2, 0)

  add = lambda do |i, delta|
    while i <= size
      bit[i] += delta
      i += i & -i
    end
  end

  prefix_sum = lambda do |i|
    s = 0
    while i > 0
      s += bit[i]
      i -= i & -i
    end
    s
  end

  res = Array.new(nums.size)
  (nums.size - 1).downto(0) do |i|
    idx = rank[nums[i]]
    res[i] = prefix_sum.call(idx - 1)
    add.call(idx, 1)
  end
  res
end
```

## Scala

```scala
object Solution {
  def countSmaller(nums: Array[Int]): List[Int] = {
    val n = nums.length
    if (n == 0) return Nil

    // Coordinate compression
    val sorted = nums.distinct.sorted
    val idxMap = scala.collection.mutable.Map[Int, Int]()
    for (i <- sorted.indices) {
      idxMap(sorted(i)) = i + 1 // BIT is 1-indexed
    }

    val bit = new BIT(sorted.length)
    val res = new Array[Int](n)

    var i = n - 1
    while (i >= 0) {
      val idx = idxMap(nums(i))
      res(i) = bit.query(idx - 1)
      bit.update(idx, 1)
      i -= 1
    }

    res.toList
  }

  private class BIT(val size: Int) {
    private val tree = new Array[Int](size + 1)

    def update(i0: Int, delta: Int): Unit = {
      var i = i0
      while (i <= size) {
        tree(i) += delta
        i += i & -i
      }
    }

    def query(i0: Int): Int = {
      var i = i0
      var sum = 0
      while (i > 0) {
        sum += tree(i)
        i -= i & -i
      }
      sum
    }
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

struct Fenwick {
    tree: Vec<i32>,
    n: usize,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { tree: vec![0; n + 1], n }
    }

    fn update(&mut self, mut idx: usize, delta: i32) {
        while idx <= self.n {
            self.tree[idx] += delta;
            let lsb = idx & (!idx + 1);
            idx += lsb;
        }
    }

    fn query(&self, mut idx: usize) -> i32 {
        let mut sum = 0;
        while idx > 0 {
            sum += self.tree[idx];
            let lsb = idx & (!idx + 1);
            idx -= lsb;
        }
        sum
    }
}

impl Solution {
    pub fn count_smaller(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![];
        }

        // Coordinate compression
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        sorted.dedup();

        let mut bit = Fenwick::new(sorted.len());
        let mut res: Vec<i32> = Vec::with_capacity(n);

        for &num in nums.iter().rev() {
            // Find 1‑based index of num in the compressed array
            let idx = match sorted.binary_search(&num) {
                Ok(pos) => pos + 1,
                Err(_) => unreachable!(),
            };
            // Count of numbers smaller than current
            let cnt = bit.query(idx - 1);
            res.push(cnt);
            // Insert current number into BIT
            bit.update(idx, 1);
        }

        res.reverse();
        res
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/bitwise)

(define/contract (count-smaller nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((sorted (sort (remove-duplicates nums) <))
         (size (+ (length sorted) 2))
         (bit (make-vector size 0))
         (idx-map (let ((h (make-hash)))
                    (for ([v sorted] [i (in-naturals 1)])
                      (hash-set! h v i))
                    h)))
    (define (add! idx)
      (let loop ((i idx))
        (when (< i size)
          (vector-set! bit i (+ (vector-ref bit i) 1))
          (loop (+ i (bitwise-and i (- i)))))))
    (define (sum idx)
      (let loop ((i idx) (acc 0))
        (if (= i 0)
            acc
            (loop (- i (bitwise-and i (- i))) (+ acc (vector-ref bit i))))))
    (let loop ((xs (reverse nums)) (res '()))
      (if (null? xs)
          (reverse res)
          (let* ((x (car xs))
                 (idx (hash-ref idx-map x))
                 (cnt (sum (- idx 1))))
            (add! idx)
            (loop (cdr xs) (cons cnt res)))))))
```

## Erlang

```erlang
-spec count_smaller([integer()]) -> [integer()].
count_smaller(Nums) ->
    Unique = lists:usort(Nums),
    Size = length(Unique),
    IndexMap = maps:from_list(lists:zip(Unique, lists:seq(1, Size))),
    Rev = lists:reverse(Nums),
    {_, ResRev} = lists:foldl(
        fun(Num, {BIT, Acc}) ->
            Idx = maps:get(Num, IndexMap),
            Smaller = bit_query(BIT, Idx - 1),
            NewBIT = bit_update(BIT, Size, Idx, 1),
            {NewBIT, [Smaller | Acc]}
        end,
        {maps:new(), []},
        Rev
    ),
    lists:reverse(ResRev).

bit_query(BIT, Index) when Index =< 0 -> 0;
bit_query(BIT, Index) ->
    bit_query_loop(BIT, Index, 0).

bit_query_loop(_BIT, 0, Sum) -> Sum;
bit_query_loop(BIT, I, Sum) ->
    Val = maps:get(I, BIT, 0),
    NextI = I band (I - 1),
    bit_query_loop(BIT, NextI, Sum + Val).

bit_update(BIT, Size, Index, Delta) when Index > Size -> BIT;
bit_update(BIT, Size, Index, Delta) ->
    Old = maps:get(Index, BIT, 0),
    NewBIT = maps:put(Index, Old + Delta, BIT),
    NextI = Index + (Index band -Index),
    bit_update(NewBIT, Size, NextI, Delta).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_smaller(nums :: [integer]) :: [integer]
  def count_smaller(nums) do
    # coordinate compression
    ranks = nums |> Enum.uniq() |> Enum.sort()
    rank_map = for {v, i} <- Enum.with_index(ranks, 1), into: %{}, do: {v, i}
    size = map_size(rank_map)

    ft = Fenwick.new(size)

    {result, _ft} =
      Enum.reduce(Enum.reverse(nums), {[], ft}, fn num, {acc, ft_acc} ->
        r = Map.fetch!(rank_map, num)
        cnt = Fenwick.query(ft_acc, r - 1)
        :ok = Fenwick.update(ft_acc, r, 1)
        {[cnt | acc], ft_acc}
      end)

    result
  end
end

defmodule Fenwick do
  import Bitwise

  @spec new(pos_integer) :: {reference, pos_integer}
  def new(size) do
    tid = :ets.new(:fenwick_table, [:private])
    for i <- 1..size, do: :ets.insert(tid, {i, 0})
    {tid, size}
  end

  @spec update({reference, pos_integer}, pos_integer, integer) :: :ok
  def update({tid, size}, idx, delta) when idx <= size do
    update_loop(tid, size, idx, delta)
  end

  defp update_loop(_tid, _size, idx, _delta) when idx > _size, do: :ok

  defp update_loop(tid, size, idx, delta) do
    case :ets.lookup(tid, idx) do
      [] -> :ets.insert(tid, {idx, delta})
      [{^idx, val}] -> :ets.insert(tid, {idx, val + delta})
    end

    next = idx + (idx &&& -idx)
    update_loop(tid, size, next, delta)
  end

  @spec query({reference, pos_integer}, pos_integer) :: integer
  def query(_ft, 0), do: 0
  def query({tid, _size}, idx) when idx > 0 do
    query_loop(tid, idx, 0)
  end

  defp query_loop(_tid, 0, acc), do: acc

  defp query_loop(tid, idx, acc) do
    val =
      case :ets.lookup(tid, idx) do
        [] -> 0
        [{^idx, v}] -> v
      end

    next = idx - (idx &&& -idx)
    query_loop(tid, next, acc + val)
  end
end
```

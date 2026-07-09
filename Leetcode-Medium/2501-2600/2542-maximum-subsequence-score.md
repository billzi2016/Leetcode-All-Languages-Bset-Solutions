# 2542. Maximum Subsequence Score

## Cpp

```cpp
class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<pair<int,int>> v;
        v.reserve(n);
        for (int i = 0; i < n; ++i) v.emplace_back(nums2[i], nums1[i]);
        sort(v.begin(), v.end(), [](const auto& a, const auto& b){
            return a.first > b.first; // descending by nums2
        });
        
        priority_queue<long long, vector<long long>, greater<long long>> minHeap;
        long long sum = 0, ans = 0;
        for (auto& p : v) {
            long long curNum1 = p.second;
            sum += curNum1;
            minHeap.push(curNum1);
            if ((int)minHeap.size() > k) {
                sum -= minHeap.top();
                minHeap.pop();
            }
            if ((int)minHeap.size() == k) {
                ans = max(ans, sum * (long long)p.first);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; ++i) idx[i] = i;
        java.util.Arrays.sort(idx, (a, b) -> Integer.compare(nums2[b], nums2[a]));
        java.util.PriorityQueue<Integer> minHeap = new java.util.PriorityQueue<>();
        long sum = 0, ans = 0;
        for (int i : idx) {
            sum += nums1[i];
            minHeap.offer(nums1[i]);
            if (minHeap.size() > k) {
                sum -= minHeap.poll();
            }
            if (minHeap.size() == k) {
                long score = sum * (long) nums2[i];
                if (score > ans) ans = score;
            }
        }
        return ans;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # Sort indices by nums2 descending while keeping corresponding nums1 values
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []          # min-heap for selected nums1 values
        cur_sum = 0
        best = 0

        for b, a in pairs:
            heapq.heappush(heap, a)
            cur_sum += a
            if len(heap) > k:
                cur_sum -= heapq.heappop(heap)
            if len(heap) == k:
                score = cur_sum * b
                if score > best:
                    best = score
        return best
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair each element and sort by nums2 descending
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []          # min-heap for selected nums1 values
        cur_sum = 0
        best = 0

        for b, a in pairs:   # b is nums2 (potential minimum), a is nums1
            heapq.heappush(heap, a)
            cur_sum += a
            if len(heap) > k:
                cur_sum -= heapq.heappop(heap)
            if len(heap) == k:
                best = max(best, cur_sum * b)

        return best
```

## C

```c
#include <stdlib.h>

typedef struct {
    int a;
    int b;
} Pair;

static int cmpPair(const void *p1, const void *p2) {
    const Pair *x = (const Pair *)p1;
    const Pair *y = (const Pair *)p2;
    return y->b - x->b;  // descending by nums2
}

long long maxScore(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    int n = nums1Size;
    Pair *arr = (Pair *)malloc(sizeof(Pair) * n);
    for (int i = 0; i < n; ++i) {
        arr[i].a = nums1[i];
        arr[i].b = nums2[i];
    }
    qsort(arr, n, sizeof(Pair), cmpPair);

    int *heap = (int *)malloc(sizeof(int) * (k + 1)); // min-heap of size up to k
    int heapSize = 0;
    long long sum = 0;
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        int val = arr[i].a;

        /* push into min-heap */
        int idx = ++heapSize;
        while (idx > 1 && heap[idx / 2] > val) {
            heap[idx] = heap[idx / 2];
            idx /= 2;
        }
        heap[idx] = val;
        sum += val;

        if (heapSize > k) {
            /* pop smallest */
            int minVal = heap[1];
            int last = heap[heapSize];
            --heapSize;
            int j = 1;
            while (j * 2 <= heapSize) {
                int child = j * 2;
                if (child + 1 <= heapSize && heap[child + 1] < heap[child])
                    ++child;
                if (heap[child] >= last)
                    break;
                heap[j] = heap[child];
                j = child;
            }
            heap[j] = last;
            sum -= minVal;
        }

        if (heapSize == k) {
            long long candidate = sum * (long long)arr[i].b;
            if (candidate > ans)
                ans = candidate;
        }
    }

    free(arr);
    free(heap);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => nums2[b].CompareTo(nums2[a])); // descending by nums2

        MinHeap heap = new MinHeap();
        long sum = 0;
        long best = 0;

        foreach (int i in idx) {
            long val = nums1[i];
            heap.Add(val);
            sum += val;

            if (heap.Count > k) {
                sum -= heap.Pop(); // remove smallest
            }

            if (heap.Count == k) {
                long score = sum * (long)nums2[i];
                if (score > best) best = score;
            }
        }

        return best;
    }

    private class MinHeap {
        private List<long> data = new List<long>();
        public int Count => data.Count;

        public void Add(long x) {
            data.Add(x);
            SiftUp(data.Count - 1);
        }

        public long Pop() {
            long root = data[0];
            long last = data[data.Count - 1];
            data.RemoveAt(data.Count - 1);
            if (data.Count > 0) {
                data[0] = last;
                SiftDown(0);
            }
            return root;
        }

        private void SiftUp(int i) {
            while (i > 0) {
                int p = (i - 1) >> 1;
                if (data[p] <= data[i]) break;
                Swap(p, i);
                i = p;
            }
        }

        private void SiftDown(int i) {
            int n = data.Count;
            while (true) {
                int left = (i << 1) + 1;
                int right = left + 1;
                int smallest = i;

                if (left < n && data[left] < data[smallest]) smallest = left;
                if (right < n && data[right] < data[smallest]) smallest = right;

                if (smallest == i) break;
                Swap(i, smallest);
                i = smallest;
            }
        }

        private void Swap(int i, int j) {
            long tmp = data[i];
            data[i] = data[j];
            data[j] = tmp;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var maxScore = function(nums1, nums2, k) {
    const n = nums1.length;
    const pairs = new Array(n);
    for (let i = 0; i < n; ++i) {
        pairs[i] = [nums2[i], nums1[i]]; // sort by nums2 descending
    }
    pairs.sort((a, b) => b[0] - a[0]);

    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p] <= h[i]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            const root = h[0];
            const last = h.pop();
            if (h.length) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, smallest = i;
                    if (l < h.length && h[l] < h[smallest]) smallest = l;
                    if (r < h.length && h[r] < h[smallest]) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return root;
        }
    }

    const heap = new MinHeap();
    let sum = 0;
    let best = 0;

    for (const [b, a] of pairs) {
        heap.push(a);
        sum += a;
        if (heap.size() > k) {
            sum -= heap.pop(); // remove smallest nums1
        }
        if (heap.size() === k) {
            const score = sum * b;
            if (score > best) best = score;
        }
    }

    return best;
};
```

## Typescript

```typescript
function maxScore(nums1: number[], nums2: number[], k: number): number {
    const n = nums1.length;
    const pairs: [number, number][] = new Array(n);
    for (let i = 0; i < n; ++i) {
        pairs[i] = [nums1[i], nums2[i]];
    }
    // Sort by nums2 descending
    pairs.sort((a, b) => b[1] - a[1]);

    class MinHeap {
        private data: number[] = [];
        size(): number { return this.data.length; }
        push(val: number): void {
            let idx = this.data.length;
            this.data.push(val);
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.data[parent] <= this.data[idx]) break;
                [this.data[parent], this.data[idx]] = [this.data[idx], this.data[parent]];
                idx = parent;
            }
        }
        pop(): number {
            const root = this.data[0];
            const last = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = last;
                let idx = 0;
                while (true) {
                    let left = idx * 2 + 1;
                    let right = idx * 2 + 2;
                    let smallest = idx;
                    if (left < this.data.length && this.data[left] < this.data[smallest]) smallest = left;
                    if (right < this.data.length && this.data[right] < this.data[smallest]) smallest = right;
                    if (smallest === idx) break;
                    [this.data[idx], this.data[smallest]] = [this.data[smallest], this.data[idx]];
                    idx = smallest;
                }
            }
            return root;
        }
    }

    const heap = new MinHeap();
    let sum = 0;
    let best = 0;

    for (const [a, b] of pairs) {
        heap.push(a);
        sum += a;
        if (heap.size() > k) {
            sum -= heap.pop(); // remove smallest nums1
        }
        if (heap.size() === k) {
            const score = sum * b; // current b is the minimum among selected
            if (score > best) best = score;
        }
    }

    return best;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function maxScore($nums1, $nums2, $k) {
        $n = count($nums1);
        $pairs = [];
        for ($i = 0; $i < $n; $i++) {
            $pairs[] = ['a' => $nums1[$i], 'b' => $nums2[$i]];
        }
        usort($pairs, function ($x, $y) {
            if ($x['b'] == $y['b']) return 0;
            return ($x['b'] < $y['b']) ? 1 : -1; // descending by b
        });
        $heap = new SplMinHeap(); // min-heap for nums1 values
        $sum = 0;
        $ans = 0;
        foreach ($pairs as $p) {
            $heap->insert($p['a']);
            $sum += $p['a'];
            if ($heap->count() > $k) {
                $removed = $heap->extract();
                $sum -= $removed;
            }
            if ($heap->count() == $k) {
                $score = $sum * $p['b'];
                if ($score > $ans) {
                    $ans = $score;
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
    struct MinHeap {
        private var data: [Int] = []
        var count: Int { data.count }
        
        mutating func push(_ value: Int) {
            data.append(value)
            siftUp(data.count - 1)
        }
        
        mutating func pop() -> Int? {
            guard !data.isEmpty else { return nil }
            if data.count == 1 {
                return data.removeLast()
            }
            let root = data[0]
            data[0] = data.removeLast()
            siftDown(0)
            return root
        }
        
        private mutating func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) / 2
                if data[parent] <= data[child] { break }
                data.swapAt(parent, child)
                child = parent
            }
        }
        
        private mutating func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < data.count && data[left] < data[smallest] {
                    smallest = left
                }
                if right < data.count && data[right] < data[smallest] {
                    smallest = right
                }
                if smallest == parent { break }
                data.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }
    
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        let n = nums1.count
        var pairs = [(num1: Int, num2: Int)]()
        pairs.reserveCapacity(n)
        for i in 0..<n {
            pairs.append((nums1[i], nums2[i]))
        }
        // Sort by nums2 descending
        pairs.sort { $0.num2 > $1.num2 }
        
        var heap = MinHeap()
        var sum: Int64 = 0
        var best: Int64 = 0
        
        for pair in pairs {
            heap.push(pair.num1)
            sum += Int64(pair.num1)
            
            if heap.count > k {
                if let removed = heap.pop() {
                    sum -= Int64(removed)
                }
            }
            
            if heap.count == k {
                let candidate = sum * Int64(pair.num2)
                if candidate > best {
                    best = candidate
                }
            }
        }
        return Int(best)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(nums1: IntArray, nums2: IntArray, k: Int): Long {
        val n = nums1.size
        val indices = (0 until n).toMutableList()
        indices.sortWith { i, j -> nums2[j] - nums2[i] } // descending by nums2
        val minHeap = java.util.PriorityQueue<Int>()
        var sum = 0L
        var best = 0L
        for (idx in indices) {
            val a = nums1[idx]
            val b = nums2[idx].toLong()
            minHeap.add(a)
            sum += a.toLong()
            if (minHeap.size > k) {
                sum -= minHeap.poll().toLong()
            }
            if (minHeap.size == k) {
                val score = sum * b
                if (score > best) best = score
            }
        }
        return best
    }
}
```

## Dart

```dart
import 'dart:math';

class MinHeap {
  final List<int> _data = [];

  void push(int value) {
    _data.add(value);
    _siftUp(_data.length - 1);
  }

  int pop() {
    final int result = _data[0];
    final int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return result;
  }

  int size() => _data.length;

  void _siftUp(int idx) {
    while (idx > 0) {
      final int parent = (idx - 1) >> 1;
      if (_data[parent] <= _data[idx]) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final int n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _data[left] < _data[smallest]) smallest = left;
      if (right < n && _data[right] < _data[smallest]) smallest = right;

      if (smallest == idx) break;
      _swap(idx, smallest);
      idx = smallest;
    }
  }

  void _swap(int i, int j) {
    final int tmp = _data[i];
    _data[i] = _data[j];
    _data[j] = tmp;
  }
}

class Solution {
  int maxScore(List<int> nums1, List<int> nums2, int k) {
    final int n = nums1.length;
    final List<List<int>> pairs = List.generate(
        n, (i) => [nums2[i], nums1[i]]); // [minCandidate, valueFromNums1]
    pairs.sort((a, b) => b[0].compareTo(a[0])); // descending by nums2

    final MinHeap heap = MinHeap();
    int sum = 0;
    int best = 0;

    for (final pair in pairs) {
      int curNum2 = pair[0];
      int curNum1 = pair[1];

      heap.push(curNum1);
      sum += curNum1;

      if (heap.size() > k) {
        sum -= heap.pop();
      }

      if (heap.size() == k) {
        best = max(best, sum * curNum2);
      }
    }

    return best;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
	"sort"
)

type pair struct {
	a int
	b int
}

type minHeap []int

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] } // min-heap
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxScore(nums1 []int, nums2 []int, k int) int64 {
	n := len(nums1)
	pairs := make([]pair, n)
	for i := 0; i < n; i++ {
		pairs[i] = pair{a: nums1[i], b: nums2[i]}
	}
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].b > pairs[j].b // descending by nums2
	})

	h := &minHeap{}
	heap.Init(h)
	var sum int64
	var ans int64

	for _, p := range pairs {
		heap.Push(h, p.a)
		sum += int64(p.a)

		if h.Len() > k {
			removed := heap.Pop(h).(int)
			sum -= int64(removed)
		}
		if h.Len() == k {
			candidate := sum * int64(p.b)
			if candidate > ans {
				ans = candidate
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(val)
    i = @data.size
    @data << val
    while i > 0
      p = (i - 1) / 2
      break if @data[p] <= @data[i]
      @data[p], @data[i] = @data[i], @data[p]
      i = p
    end
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      size = @data.size
      loop do
        l = i * 2 + 1
        r = i * 2 + 2
        break if l >= size
        child = (r < size && @data[r] < @data[l]) ? r : l
        break if @data[i] <= @data[child]
        @data[i], @data[child] = @data[child], @data[i]
        i = child
      end
    end
    min
  end

  def size
    @data.size
  end
end

def max_score(nums1, nums2, k)
  n = nums1.length
  pairs = Array.new(n) { |i| [nums1[i], nums2[i]] }
  pairs.sort_by! { |_, b| -b }

  heap = MinHeap.new
  sum = 0
  ans = 0

  pairs.each do |a, b|
    heap.push(a)
    sum += a
    if heap.size > k
      removed = heap.pop
      sum -= removed
    end
    if heap.size == k
      score = sum * b
      ans = score if score > ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def maxScore(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
    val n = nums1.length
    // Pair each element with its counterpart in nums2
    val pairs = (0 until n).map(i => (nums2(i), nums1(i)))
    // Sort by nums2 descending so current nums2 acts as the minimum of chosen subsequence
    val sorted = pairs.sortBy(-_._1)

    // Min-heap to keep the k largest nums1 values (by removing smallest when size > k)
    implicit val minOrdering: Ordering[Int] = Ordering[Int].reverse
    val heap = scala.collection.mutable.PriorityQueue.empty[Int]

    var sum: Long = 0L
    var best: Long = 0L

    for ((b, a) <- sorted) {
      heap.enqueue(a)
      sum += a
      if (heap.size > k) {
        val removed = heap.dequeue()
        sum -= removed
      }
      if (heap.size == k) {
        val score = sum * b.toLong
        if (score > best) best = score
      }
    }

    best
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let n = nums1.len();
        let mut pairs: Vec<(i32, i32)> = (0..n).map(|i| (nums2[i], nums1[i])).collect();
        // Sort by nums2 descending
        pairs.sort_by(|a, b| b.0.cmp(&a.0));

        use std::collections::BinaryHeap;
        use std::cmp::Reverse;

        let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new(); // min-heap for selected nums1
        let mut sum: i64 = 0;
        let mut ans: i64 = 0;
        let k_usize = k as usize;

        for (b, a) in pairs {
            heap.push(Reverse(a));
            sum += a as i64;

            if heap.len() > k_usize {
                if let Some(Reverse(rem)) = heap.pop() {
                    sum -= rem as i64;
                }
            }

            if heap.len() == k_usize {
                let score = sum * b as i64;
                if score > ans {
                    ans = score;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(require racket/priority-queue)

(define/contract (max-score nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((pairs (map list nums2 nums1))
         (sorted (sort pairs > #:key first)))
    (define heap (make-pqueue <)) ; min‑heap for smallest nums1
    (define sum 0)
    (define ans 0)
    (define target (- k 1))
    (for ([pair sorted])
      (define b (first pair))
      (define a (second pair))
      (when (= (pqueue-size heap) target)
        (define candidate (* (+ sum a) b))
        (when (> candidate ans)
          (set! ans candidate)))
      (pqueue-put! heap a)
      (set! sum (+ sum a))
      (when (> (pqueue-size heap) target)
        (define smallest (pqueue-get! heap))
        (set! sum (- sum smallest))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([max_score/3]).

-spec max_score(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
max_score(Nums1, Nums2, K) ->
    Pairs = lists:zip(Nums2, Nums1),
    Sorted = lists:sort(fun({A,_},{B,_}) -> A > B end, Pairs),
    loop(Sorted, K, 0, gb_trees:empty(), 0, 0).

loop([], _K, _Sum, _Tree, _Size, Max) ->
    Max;
loop([{Num2, Num1}|Rest], K, Sum, Tree, Size, Max) ->
    {NewTree, NewSize, NewSum} =
        if Size < K ->
                {insert_val(Num1, Tree), Size + 1, Sum + Num1};
           true ->
                case gb_trees:smallest(Tree) of
                    {MinKey,_} when Num1 > MinKey ->
                        T1 = delete_one(MinKey, Tree),
                        T2 = insert_val(Num1, T1),
                        {T2, Size, Sum - MinKey + Num1};
                    _ ->
                        {Tree, Size, Sum}
                end
        end,
    NewMax =
        if NewSize == K ->
                Score = NewSum * Num2,
                case Score > Max of
                    true -> Score;
                    false -> Max
                end;
           true -> Max
        end,
    loop(Rest, K, NewSum, NewTree, NewSize, NewMax).

insert_val(V, Tree) ->
    case gb_trees:lookup(V, Tree) of
        {value, Count} ->
            gb_trees:update(V, Count + 1, Tree);
        none ->
            gb_trees:insert(V, 1, Tree)
    end.

delete_one(V, Tree) ->
    case gb_trees:lookup(V, Tree) of
        {value, Count} when Count > 1 ->
            gb_trees:update(V, Count - 1, Tree);
        {value, 1} ->
            gb_trees:delete(V, Tree)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def max_score(nums1, nums2, k) do
    pairs = Enum.zip(nums1, nums2)
    sorted = Enum.sort_by(pairs, fn {_a, b} -> -b end)

    {_, _, _, answer} =
      Enum.reduce(sorted, {:gb_trees.empty(), 0, 0, 0}, fn {a, b},
                                                      {tree, size, sum, best} ->
        # insert a into multiset (min‑heap via gb_tree)
        tree1 = insert(tree, a)
        sum1 = sum + a
        size1 = size + 1

        {tree2, size2, sum2} =
          if size1 > k do
            {min_key, cnt} = :gb_trees.smallest(tree1)

            tree_removed =
              if cnt == 1,
                do: :gb_trees.delete(min_key, tree1),
                else: :gb_trees.update(min_key, cnt - 1, tree1)

            {tree_removed, size1 - 1, sum1 - min_key}
          else
            {tree1, size1, sum1}
          end

        best1 =
          if size2 == k do
            max(best, sum2 * b)
          else
            best
          end

        {tree2, size2, sum2, best1}
      end)

    answer
  end

  defp insert(tree, val) do
    case :gb_trees.lookup(val, tree) do
      :none -> :gb_trees.insert(val, 1, tree)
      {_k, cnt} -> :gb_trees.update(val, cnt + 1, tree)
    end
  end
end
```

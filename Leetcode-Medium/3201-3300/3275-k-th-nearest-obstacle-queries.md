# 3275. K-th Nearest Obstacle Queries

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> resultsArray(vector<vector<int>>& queries, int k) {
        priority_queue<long long> maxHeap; // stores up to k smallest distances
        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            long long d = llabs((long long)q[0]) + llabs((long long)q[1]);
            if ((int)maxHeap.size() < k) {
                maxHeap.push(d);
            } else if (k > 0 && d < maxHeap.top()) {
                maxHeap.pop();
                maxHeap.push(d);
            }
            if ((int)maxHeap.size() < k) ans.push_back(-1);
            else ans.push_back((int)maxHeap.top());
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] resultsArray(int[][] queries, int k) {
        int n = queries.length;
        int[] res = new int[n];
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            long x = queries[i][0];
            long y = queries[i][1];
            int d = (int) (Math.abs(x) + Math.abs(y));
            if (maxHeap.size() < k) {
                maxHeap.offer(d);
            } else if (d < maxHeap.peek()) {
                maxHeap.poll();
                maxHeap.offer(d);
            }
            res[i] = (maxHeap.size() < k) ? -1 : maxHeap.peek();
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def resultsArray(self, queries, k):
        """
        :type queries: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        max_heap = []  # store negative distances to simulate a max-heap
        res = []
        for x, y in queries:
            d = abs(x) + abs(y)
            if len(max_heap) < k:
                heapq.heappush(max_heap, -d)
                if len(max_heap) == k:
                    res.append(-max_heap[0])
                else:
                    res.append(-1)
            else:
                # heap already has k elements
                if d < -max_heap[0]:
                    heapq.heapreplace(max_heap, -d)
                res.append(-max_heap[0])
        return res
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        max_heap = []  # store negative distances to simulate a max-heap
        ans = []
        for x, y in queries:
            d = abs(x) + abs(y)
            if len(max_heap) < k:
                heapq.heappush(max_heap, -d)
            else:
                if -max_heap[0] > d:
                    heapq.heapreplace(max_heap, -d)
            if len(max_heap) < k:
                ans.append(-1)
            else:
                ans.append(-max_heap[0])
        return ans
```

## C

```c
#include <stdlib.h>
#include <stddef.h>
#include <limits.h>

/* Max‑heap helpers */
static void heap_push(long long *heap, int *size, long long val) {
    (*size)++;
    int idx = *size;
    heap[idx] = val;
    while (idx > 1 && heap[idx / 2] < heap[idx]) {
        long long tmp = heap[idx];
        heap[idx] = heap[idx / 2];
        heap[idx / 2] = tmp;
        idx >>= 1;
    }
}

static void heapify_down(long long *heap, int size) {
    int idx = 1;
    while (1) {
        int left = idx << 1;
        int right = left + 1;
        int largest = idx;
        if (left <= size && heap[left] > heap[largest]) largest = left;
        if (right <= size && heap[right] > heap[largest]) largest = right;
        if (largest != idx) {
            long long tmp = heap[idx];
            heap[idx] = heap[largest];
            heap[largest] = tmp;
            idx = largest;
        } else break;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultsArray(int** queries, int queriesSize, int* queriesColSize, int k, int* returnSize) {
    (void)queriesColSize;  // unused
    *returnSize = queriesSize;
    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    if (!ans) return NULL;

    long long *heap = (long long *)malloc(sizeof(long long) * (k + 1)); // 1‑based
    if (!heap) {
        free(ans);
        return NULL;
    }
    int heapSize = 0;

    for (int i = 0; i < queriesSize; ++i) {
        long long x = (long long)queries[i][0];
        long long y = (long long)queries[i][1];
        long long d = llabs(x) + llabs(y);

        if (heapSize < k) {
            heap_push(heap, &heapSize, d);
        } else if (d < heap[1]) {
            heap[1] = d;
            heapify_down(heap, heapSize);
        }

        ans[i] = (heapSize < k) ? -1 : (int)heap[1];
    }

    free(heap);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] ResultsArray(int[][] queries, int k) {
        int n = queries.Length;
        int[] res = new int[n];
        MaxHeap heap = new MaxHeap();
        for (int i = 0; i < n; i++) {
            long dLong = Math.Abs((long)queries[i][0]) + Math.Abs((long)queries[i][1]);
            int d = (int)dLong; // fits in int per constraints
            if (heap.Count < k) {
                heap.Push(d);
                res[i] = heap.Count == k ? heap.Peek() : -1;
            } else {
                if (d < heap.Peek()) {
                    heap.Pop();
                    heap.Push(d);
                }
                res[i] = heap.Peek();
            }
        }
        return res;
    }

    private class MaxHeap {
        private List<int> data = new List<int>();
        public int Count => data.Count;

        public void Push(int val) {
            data.Add(val);
            SiftUp(data.Count - 1);
        }

        public int Peek() {
            return data[0];
        }

        public int Pop() {
            int top = data[0];
            int last = data[data.Count - 1];
            data.RemoveAt(data.Count - 1);
            if (data.Count > 0) {
                data[0] = last;
                SiftDown(0);
            }
            return top;
        }

        private void SiftUp(int i) {
            while (i > 0) {
                int p = (i - 1) / 2;
                if (data[p] >= data[i]) break;
                int tmp = data[p];
                data[p] = data[i];
                data[i] = tmp;
                i = p;
            }
        }

        private void SiftDown(int i) {
            int n = data.Count;
            while (true) {
                int l = i * 2 + 1;
                int r = l + 1;
                int largest = i;
                if (l < n && data[l] > data[largest]) largest = l;
                if (r < n && data[r] > data[largest]) largest = r;
                if (largest == i) break;
                int tmp = data[i];
                data[i] = data[largest];
                data[largest] = tmp;
                i = largest;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} queries
 * @param {number} k
 * @return {number[]}
 */
var resultsArray = function(queries, k) {
    class MaxHeap {
        constructor() {
            this.heap = [];
        }
        size() {
            return this.heap.length;
        }
        peek() {
            return this.heap[0];
        }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p] >= h[i]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const max = h[0];
            const end = h.pop();
            if (h.length > 0) {
                h[0] = end;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        largest = i;
                    if (l < h.length && h[l] > h[largest]) largest = l;
                    if (r < h.length && h[r] > h[largest]) largest = r;
                    if (largest === i) break;
                    [h[i], h[largest]] = [h[largest], h[i]];
                    i = largest;
                }
            }
            return max;
        }
    }

    const heap = new MaxHeap();
    const res = [];

    for (const [x, y] of queries) {
        const d = Math.abs(x) + Math.abs(y);
        if (heap.size() < k) {
            heap.push(d);
        } else if (d < heap.peek()) {
            heap.pop();
            heap.push(d);
        }
        res.push(heap.size() === k ? heap.peek() : -1);
    }

    return res;
};
```

## Typescript

```typescript
function resultsArray(queries: number[][], k: number): number[] {
    class MaxHeap {
        private arr: number[] = [];
        size(): number { return this.arr.length; }
        peek(): number { return this.arr[0]; }
        push(val: number): void {
            const a = this.arr;
            a.push(val);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (a[p] >= a[i]) break;
                [a[p], a[i]] = [a[i], a[p]];
                i = p;
            }
        }
        pop(): number {
            const a = this.arr;
            const n = a.length - 1;
            if (n < 0) return undefined as any;
            const top = a[0];
            const last = a.pop()!;
            if (n > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let left = i * 2 + 1;
                    let right = left + 1;
                    let largest = i;
                    if (left < a.length && a[left] > a[largest]) largest = left;
                    if (right < a.length && a[right] > a[largest]) largest = right;
                    if (largest === i) break;
                    [a[i], a[largest]] = [a[largest], a[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    const heap = new MaxHeap();
    const res: number[] = [];

    for (const q of queries) {
        const d = Math.abs(q[0]) + Math.abs(q[1]);
        if (heap.size() < k) {
            heap.push(d);
        } else if (d < heap.peek()) {
            heap.pop();
            heap.push(d);
        }
        res.push(heap.size() === k ? heap.peek() : -1);
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $queries
     * @param Integer $k
     * @return Integer[]
     */
    function resultsArray($queries, $k) {
        $heap = new SplMaxHeap();
        $result = [];
        foreach ($queries as $q) {
            $d = abs($q[0]) + abs($q[1]);
            if ($heap->count() < $k) {
                $heap->insert($d);
            } else {
                if ($d < $heap->top()) {
                    $heap->extract();
                    $heap->insert($d);
                }
            }
            if ($heap->count() < $k) {
                $result[] = -1;
            } else {
                $result[] = $heap->top();
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class MaxHeap {
    private var heap = [Int]()
    var count: Int { heap.count }
    var peek: Int? { heap.first }

    func push(_ val: Int) {
        heap.append(val)
        siftUp(heap.count - 1)
    }

    @discardableResult
    func pop() -> Int? {
        guard !heap.isEmpty else { return nil }
        let top = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            siftDown(0)
        }
        return top
    }

    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if heap[child] > heap[parent] {
                heap.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }

    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var largest = parent
            if left < heap.count && heap[left] > heap[largest] { largest = left }
            if right < heap.count && heap[right] > heap[largest] { largest = right }
            if largest == parent { break }
            heap.swapAt(parent, largest)
            parent = largest
        }
    }
}

class Solution {
    func resultsArray(_ queries: [[Int]], _ k: Int) -> [Int] {
        var heap = MaxHeap()
        var ans = [Int]()
        for q in queries {
            let d = abs(q[0]) + abs(q[1])
            if heap.count < k {
                heap.push(d)
            } else if let top = heap.peek, d < top {
                _ = heap.pop()
                heap.push(d)
            }
            if heap.count == k {
                ans.append(heap.peek!)
            } else {
                ans.append(-1)
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue
import kotlin.math.abs

class Solution {
    fun resultsArray(queries: Array<IntArray>, k: Int): IntArray {
        val n = queries.size
        val ans = IntArray(n)
        val maxHeap = PriorityQueue<Int>(k, Comparator { a, b -> b.compareTo(a) })
        for (i in 0 until n) {
            val d = abs(queries[i][0]) + abs(queries[i][1])
            if (maxHeap.size < k) {
                maxHeap.add(d)
            } else if (d < maxHeap.peek()) {
                maxHeap.poll()
                maxHeap.add(d)
            }
            ans[i] = if (maxHeap.size < k) -1 else maxHeap.peek()
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> resultsArray(List<List<int>> queries, int k) {
    // Max-heap to keep the k smallest distances.
    final heap = HeapPriorityQueue<int>((a, b) => b.compareTo(a));
    final List<int> result = [];

    for (final q in queries) {
      final dist = q[0].abs() + q[1].abs();
      heap.add(dist);
      if (heap.length > k) {
        // Remove the largest distance among stored ones.
        heap.removeFirst();
      }
      if (heap.length < k) {
        result.add(-1);
      } else {
        // The root holds the kth nearest distance.
        result.add(heap.first);
      }
    }

    return result;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func resultsArray(queries [][]int, k int) []int {
	res := make([]int, len(queries))
	h := &MaxHeap{}
	heap.Init(h)

	for i, q := range queries {
		d := abs(q[0]) + abs(q[1])

		if h.Len() < k {
			heap.Push(h, d)
			if h.Len() == k {
				res[i] = (*h)[0]
			} else {
				res[i] = -1
			}
		} else { // heap size == k
			if d < (*h)[0] {
				heap.Pop(h)
				heap.Push(h, d)
			}
			res[i] = (*h)[0]
		}
	}
	return res
}
```

## Ruby

```ruby
class MaxHeap
  def initialize
    @a = []
  end

  def size
    @a.size
  end

  def top
    @a[0]
  end

  def push(val)
    a = @a
    i = a.size
    a << val
    while i > 0
      p = (i - 1) / 2
      break if a[p] >= a[i]
      a[p], a[i] = a[i], a[p]
      i = p
    end
  end

  def pop
    a = @a
    return nil if a.empty?
    max = a[0]
    last = a.pop
    unless a.empty?
      a[0] = last
      i = 0
      n = a.size
      loop do
        l = i * 2 + 1
        r = l + 1
        break if l >= n
        larger = l
        larger = r if r < n && a[r] > a[l]
        break if a[i] >= a[larger]
        a[i], a[larger] = a[larger], a[i]
        i = larger
      end
    end
    max
  end
end

# @param {Integer[][]} queries
# @param {Integer} k
# @return {Integer[]}
def results_array(queries, k)
  heap = MaxHeap.new
  res = []
  queries.each do |x, y|
    d = x.abs + y.abs
    heap.push(d)
    heap.pop if heap.size > k
    if heap.size == k
      res << heap.top
    else
      res << -1
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def resultsArray(queries: Array[Array[Int]], k: Int): Array[Int] = {
        import scala.collection.mutable.PriorityQueue
        val pq = PriorityQueue.empty[Long] // max-heap (largest distance on top)
        val n = queries.length
        val ans = new Array[Int](n)
        var i = 0
        while (i < n) {
            val q = queries(i)
            val d = math.abs(q(0).toLong) + math.abs(q(1).toLong)
            if (pq.size < k) {
                pq.enqueue(d)
            } else if (d < pq.head) {
                pq.dequeue()
                pq.enqueue(d)
            }
            ans(i) = if (pq.size == k) pq.head.toInt else -1
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn results_array(queries: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        use std::collections::BinaryHeap;
        let k_usize = k as usize;
        let mut heap: BinaryHeap<i64> = BinaryHeap::new();
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let x = q[0] as i64;
            let y = q[1] as i64;
            let d = x.abs() + y.abs();
            if heap.len() < k_usize {
                heap.push(d);
            } else if let Some(&top) = heap.peek() {
                if d < top {
                    heap.pop();
                    heap.push(d);
                }
            }
            if heap.len() == k_usize {
                ans.push(*heap.peek().unwrap() as i32);
            } else {
                ans.push(-1);
            }
        }
        ans
    }
}
```

## Racket

```racket
(struct heap (data count) #:mutable)

(define (heap-push! h val)
  (let* ((cnt (+ (heap-count h) 1))
         (vec (heap-data h)))
    (set-heap-count! h cnt)
    (let loop ((i cnt))
      (if (= i 1)
          (vector-set! vec i val)
          (let ((parent (quotient i 2)))
            (if (< (vector-ref vec parent) val)
                (begin
                  (vector-set! vec i (vector-ref vec parent))
                  (loop parent))
                (vector-set! vec i val)))))))

(define (heap-top h)
  (if (> (heap-count h) 0)
      (vector-ref (heap-data h) 1)
      #f))

(define (heapify-down! h i)
  (let ((vec (heap-data h))
        (cnt (heap-count h)))
    (let loop ((idx i))
      (let* ((left (* idx 2))
             (right (+ left 1))
             (largest idx))
        (when (and (<= left cnt) (> (vector-ref vec left) (vector-ref vec largest)))
          (set! largest left))
        (when (and (<= right cnt) (> (vector-ref vec right) (vector-ref vec largest)))
          (set! largest right))
        (if (= largest idx)
            (void)
            (begin
              (let ((tmp (vector-ref vec idx)))
                (vector-set! vec idx (vector-ref vec largest))
                (vector-set! vec largest tmp))
              (loop largest)))))))

(define (heap-replace-top! h val)
  (vector-set! (heap-data h) 1 val)
  (heapify-down! h 1))

(define/contract (results-array queries k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  (let* ((h (make-heap (make-vector (+ k 1)) 0))
         (ans '()))
    (for ([p queries])
      (define x (first p))
      (define y (second p))
      (define d (+ (abs x) (abs y)))
      (cond
        [(< (heap-count h) k)
         (heap-push! h d)]
        [(and (> (heap-count h) 0) (< d (heap-top h)))
         (heap-replace-top! h d)])
      (set! ans (cons (if (= (heap-count h) k) (heap-top h) -1) ans)))
    (reverse ans)))
```

## Erlang

```erlang
-module(solution).
-export([results_array/2]).

-spec results_array(Queries :: [[integer()]], K :: integer()) -> [integer()].
results_array(Queries, K) ->
    EmptyTree = gb_trees:empty(),
    {_, _, RevRes} = lists:foldl(fun(Q, {Tree, Size, Acc}) ->
        [X, Y] = Q,
        Dist = abs(X) + abs(Y),
        case Size < K of
            true ->
                {NewTree, NewSize} = inc_insert(Dist, Tree, Size),
                Answer = if NewSize == K -> element(1, gb_trees:largest(NewTree));
                            true       -> -1
                         end,
                {NewTree, NewSize, [Answer | Acc]};
            false ->
                {LargestKey, _} = gb_trees:largest(Tree),
                if Dist < LargestKey ->
                        Tree1 = dec_remove(LargestKey, Tree),
                        Size1 = Size - 1,
                        {Tree2, Size2} = inc_insert(Dist, Tree1, Size1),
                        Answer = element(1, gb_trees:largest(Tree2)),
                        {Tree2, Size2, [Answer | Acc]};
                   true ->
                        Answer = LargestKey,
                        {Tree, Size, [Answer | Acc]}
                end
        end
    end, {EmptyTree, 0, []}, Queries),
    lists:reverse(RevRes).

-spec inc_insert(integer(), gb_trees:tree(), integer()) -> {gb_trees:tree(), integer()}.
inc_insert(Dist, Tree, Size) ->
    case gb_trees:lookup(Dist, Tree) of
        {value, C} ->
            NewTree = gb_trees:update(Dist, C + 1, Tree),
            {NewTree, Size + 1};
        none ->
            NewTree = gb_trees:insert(Dist, 1, Tree),
            {NewTree, Size + 1}
    end.

-spec dec_remove(integer(), gb_trees:tree()) -> gb_trees:tree().
dec_remove(Key, Tree) ->
    case gb_trees:lookup(Key, Tree) of
        {value, C} when C > 1 ->
            gb_trees:update(Key, C - 1, Tree);
        {value, _C} ->
            gb_trees:delete(Key, Tree)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec results_array(queries :: [[integer]], k :: integer) :: [integer]
  def results_array(queries, k) do
    {answers_rev, _heap} =
      Enum.reduce(queries, {[], MaxHeap.new()}, fn [x, y], {acc, heap} ->
        d = abs(x) + abs(y)

        heap =
          cond do
            heap.size < k ->
              MaxHeap.push(heap, d)

            true ->
              max_in_heap = MaxHeap.peek(heap)

              if d < max_in_heap do
                {_popped, heap2} = MaxHeap.pop_max(heap)
                MaxHeap.push(heap2, d)
              else
                heap
              end
          end

        ans = if heap.size == k, do: MaxHeap.peek(heap), else: -1
        {[ans | acc], heap}
      end)

    Enum.reverse(answers_rev)
  end

  defmodule MaxHeap do
    defstruct size: 0, data: :array.new(0)

    @spec new() :: %MaxHeap{}
    def new(), do: %MaxHeap{}

    @spec push(%MaxHeap{}, integer) :: %MaxHeap{}
    def push(%MaxHeap{size: s, data: d} = heap, val) do
      idx = s + 1
      d1 = :array.set(idx, val, d)
      heap = %{heap | size: idx, data: d1}
      bubble_up(heap, idx)
    end

    @spec peek(%MaxHeap{}) :: integer
    def peek(%MaxHeap{size: s, data: d}) when s > 0 do
      :array.get(1, d)
    end

    @spec pop_max(%MaxHeap{}) :: {integer, %MaxHeap{}}
    def pop_max(%MaxHeap{size: 0} = heap), do: {nil, heap}

    def pop_max(%MaxHeap{size: 1, data: d}) do
      max = :array.get(1, d)
      {max, %MaxHeap{size: 0, data: :array.new(0)}}
    end

    def pop_max(%MaxHeap{size: s, data: d} = heap) when s > 1 do
      max = :array.get(1, d)
      last = :array.get(s, d)

      d1 = :array.set(1, last, d)
      d2 = :array.set(s, nil, d1)

      new_heap = %MaxHeap{size: s - 1, data: d2}
      {max, bubble_down(new_heap, 1)}
    end

    defp bubble_up(%MaxHeap{size: _s, data: d} = heap, idx) when idx > 1 do
      parent = div(idx, 2)
      val = :array.get(idx, d)
      pval = :array.get(parent, d)

      if val > pval do
        d1 = :array.set(idx, pval, d)
        d2 = :array.set(parent, val, d1)
        heap = %{heap | data: d2}
        bubble_up(heap, parent)
      else
        heap
      end
    end

    defp bubble_up(heap, _), do: heap

    defp bubble_down(%MaxHeap{size: s, data: d} = heap, idx) do
      left = idx * 2
      right = left + 1
      largest = idx
      largest_val = :array.get(idx, d)

      if left <= s do
        lval = :array.get(left, d)
        if lval > largest_val do
          largest = left
          largest_val = lval
        end
      end

      if right <= s do
        rval = :array.get(right, d)
        if rval > largest_val do
          largest = right
        end
      end

      if largest != idx do
        val_idx = :array.get(idx, d)
        val_largest = :array.get(largest, d)

        d1 = :array.set(idx, val_largest, d)
        d2 = :array.set(largest, val_idx, d1)

        heap = %{heap | data: d2}
        bubble_down(heap, largest)
      else
        heap
      end
    end
  end
end
```

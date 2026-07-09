# 3066. Minimum Operations to Exceed Threshold Value II

## Cpp

```cpp
class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        using ll = long long;
        std::priority_queue<ll, std::vector<ll>, std::greater<ll>> pq;
        for (int x : nums) pq.push(static_cast<ll>(x));
        int ops = 0;
        while (!pq.empty() && pq.top() < k) {
            ll a = pq.top(); pq.pop();
            ll b = pq.top(); pq.pop();
            // a is the smallest, so new value is a*2 + b
            ll newVal = a * 2 + b;
            pq.push(newVal);
            ++ops;
        }
        return ops;
    }
};
```

## Java

```java
import java.util.PriorityQueue;

class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for (int num : nums) {
            pq.offer((long) num);
        }
        long target = k;
        int operations = 0;
        while (!pq.isEmpty() && pq.peek() < target) {
            long a = pq.poll(); // smallest
            long b = pq.poll(); // second smallest
            long newVal = a * 2 + b; // since a <= b, min*2 + max = a*2 + b
            pq.offer(newVal);
            operations++;
        }
        return operations;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapq.heapify(nums)
        ops = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_val = 2 * (x if x < y else y) + (y if x < y else x)
            heapq.heappush(nums, new_val)
            ops += 1
        return ops
```

## Python3

```python
class Solution:
    def minOperations(self, nums, k):
        import heapq
        heapq.heapify(nums)
        ops = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, 2 * min(x, y) + max(x, y))
            ops += 1
        return ops
```

## C

```c
#include <stdlib.h>

static void heapSwap(long long *a, long long *b) {
    long long tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(long long *heap, int *size, long long val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p] <= heap[i]) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static long long heapPop(long long *heap, int *size) {
    long long minVal = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= *size) break;
        int smallest = l;
        if (r < *size && heap[r] < heap[l]) smallest = r;
        if (heap[i] <= heap[smallest]) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return minVal;
}

int minOperations(int* nums, int numsSize, int k) {
    long long *heap = (long long *)malloc(sizeof(long long) * numsSize);
    int heapSize = 0;
    for (int i = 0; i < numsSize; ++i) {
        heapPush(heap, &heapSize, (long long)nums[i]);
    }

    int ops = 0;
    while (heapSize > 0 && heap[0] < k) {
        if (heapSize == 1) break; // should not happen per problem guarantee
        long long a = heapPop(heap, &heapSize);
        long long b = heapPop(heap, &heapSize);
        long long newVal = a * 2 + b;
        heapPush(heap, &heapSize, newVal);
        ++ops;
    }

    free(heap);
    return ops;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums, int k) {
        var heap = new PriorityQueue<long, long>();
        foreach (var num in nums) {
            long val = num;
            heap.Enqueue(val, val);
        }

        int operations = 0;
        long target = k;

        while (heap.Count > 0 && heap.Peek() < target) {
            // Since we always have at least two elements when needed (guaranteed by problem)
            long x = heap.Dequeue(); // smallest
            long y = heap.Dequeue(); // second smallest, x <= y
            long newVal = x * 2 + y;
            heap.Enqueue(newVal, newVal);
            operations++;
        }

        return operations;
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
var minOperations = function(nums, k) {
    class MinHeap {
        constructor(arr) {
            this.heap = arr ? arr.slice() : [];
            if (arr) this._heapify();
        }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
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
            if (h.length === 0) return undefined;
            const root = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                this._siftDown(0);
            }
            return root;
        }
        _siftDown(i) {
            const h = this.heap;
            const n = h.length;
            while (true) {
                let smallest = i;
                const l = i * 2 + 1;
                const r = l + 1;
                if (l < n && h[l] < h[smallest]) smallest = l;
                if (r < n && h[r] < h[smallest]) smallest = r;
                if (smallest === i) break;
                [h[i], h[smallest]] = [h[smallest], h[i]];
                i = smallest;
            }
        }
        _heapify() {
            for (let i = Math.floor(this.heap.length / 2) - 1; i >= 0; --i) {
                this._siftDown(i);
            }
        }
    }

    const heap = new MinHeap(nums);
    let ops = 0;
    while (heap.size() > 0 && heap.peek() < k) {
        // need at least two elements, guaranteed by problem constraints
        const x = heap.pop();
        const y = heap.pop();
        const newVal = x * 2 + y; // x <= y because they are the two smallest
        heap.push(newVal);
        ops++;
    }
    return ops;
};
```

## Typescript

```typescript
function minOperations(nums: number[], k: number): number {
    class MinHeap {
        private heap: number[];
        constructor(arr?: number[]) {
            this.heap = arr ? arr.slice() : [];
            if (arr) this.buildHeap();
        }
        size(): number {
            return this.heap.length;
        }
        peek(): number {
            return this.heap[0];
        }
        push(val: number): void {
            this.heap.push(val);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): number {
            const n = this.heap.length;
            if (n === 0) throw new Error("Heap is empty");
            const min = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.sinkDown(0);
            }
            return min;
        }
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent] <= this.heap[idx]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        private sinkDown(idx: number): void {
            const n = this.heap.length;
            while (true) {
                let smallest = idx;
                const left = idx * 2 + 1;
                const right = left + 1;
                if (left < n && this.heap[left] < this.heap[smallest]) smallest = left;
                if (right < n && this.heap[right] < this.heap[smallest]) smallest = right;
                if (smallest === idx) break;
                [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
                idx = smallest;
            }
        }
        private buildHeap(): void {
            for (let i = Math.floor(this.heap.length / 2) - 1; i >= 0; i--) {
                this.sinkDown(i);
            }
        }
    }

    const heap = new MinHeap(nums);
    let ops = 0;
    while (heap.size() > 0 && heap.peek() < k) {
        const x = heap.pop();
        const y = heap.pop();
        const newVal = Math.min(x, y) * 2 + Math.max(x, y);
        heap.push(newVal);
        ops++;
    }
    return ops;
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
    function minOperations($nums, $k) {
        $heap = new SplMinHeap();
        foreach ($nums as $num) {
            $heap->insert($num);
        }
        $ops = 0;
        while ($heap->count() > 0 && $heap->current() < $k) {
            if ($heap->count() == 1) {
                break; // guaranteed not to happen
            }
            $x = $heap->extract(); // smallest
            $y = $heap->extract(); // second smallest
            $new = $x * 2 + $y;
            $heap->insert($new);
            $ops++;
        }
        return $ops;
    }
}
```

## Swift

```swift
class MinHeap {
    private var data: [Int64]

    init(_ array: [Int64]) {
        self.data = array
        buildHeap()
    }

    var isEmpty: Bool { data.isEmpty }
    var count: Int { data.count }
    var peek: Int64? { data.first }

    func push(_ value: Int64) {
        data.append(value)
        heapifyUp(from: data.count - 1)
    }

    func pop() -> Int64 {
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            heapifyDown(from: 0)
        }
        return result
    }

    private func buildHeap() {
        guard !data.isEmpty else { return }
        for i in stride(from: (data.count / 2) - 1, through: 0, by: -1) {
            heapifyDown(from: i)
        }
    }

    private func heapifyUp(from index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && data[child] < data[parent] {
            data.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }

    private func heapifyDown(from index: Int) {
        var i = index
        while true {
            let left = 2 * i + 1
            let right = left + 1
            var smallest = i

            if left < data.count && data[left] < data[smallest] {
                smallest = left
            }
            if right < data.count && data[right] < data[smallest] {
                smallest = right
            }
            if smallest == i { break }
            data.swapAt(i, smallest)
            i = smallest
        }
    }
}

class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var heap = MinHeap(nums.map { Int64($0) })
        let target = Int64(k)
        var operations = 0

        while let minVal = heap.peek, minVal < target, heap.count >= 2 {
            let a = heap.pop()
            let b = heap.pop()
            let newVal = a * 2 + b
            heap.push(newVal)
            operations += 1
        }

        return operations
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        val heap = PriorityQueue<Long>()
        for (num in nums) {
            heap.add(num.toLong())
        }
        var ops = 0
        val target = k.toLong()
        while (heap.peek() < target) {
            // Since answer always exists, there will be at least two elements here
            val x = heap.poll()
            val y = heap.poll()
            val newVal = 2L * kotlin.math.min(x, y) + kotlin.math.max(x, y)
            heap.add(newVal)
            ops++
        }
        return ops
    }
}
```

## Dart

```dart
class MinHeap {
  final List<int> _data = [];

  bool get isEmpty => _data.isEmpty;

  int peek() => _data[0];

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

  void _siftUp(int idx) {
    while (idx > 0) {
      final int parent = (idx - 1) >> 1;
      if (_data[parent] <= _data[idx]) break;
      final int tmp = _data[parent];
      _data[parent] = _data[idx];
      _data[idx] = tmp;
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
      final int tmp = _data[idx];
      _data[idx] = _data[smallest];
      _data[smallest] = tmp;
      idx = smallest;
    }
  }
}

class Solution {
  int minOperations(List<int> nums, int k) {
    final MinHeap heap = MinHeap();
    for (final v in nums) {
      heap.push(v);
    }

    int operations = 0;
    while (heap.peek() < k) {
      int x = heap.pop();
      int y = heap.pop();

      int a = x < y ? x : y;
      int b = x < y ? y : x;
      int newVal = a * 2 + b;

      heap.push(newVal);
      operations++;
    }
    return operations;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type IntHeap []int64

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int64)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minOperations(nums []int, k int) int {
	h := make(IntHeap, len(nums))
	for i, v := range nums {
		h[i] = int64(v)
	}
	heap.Init(&h)

	k64 := int64(k)
	ops := 0

	for h.Len() > 1 && h[0] < k64 {
		x := heap.Pop(&h).(int64) // smallest
		y := heap.Pop(&h).(int64) // second smallest
		newVal := 2*x + y
		heap.Push(&h, newVal)
		ops++
	}
	return ops
}
```

## Ruby

```ruby
def min_operations(nums, k)
  heap = []

  push = lambda do |val|
    i = heap.size
    heap << val
    while i > 0
      parent = (i - 1) / 2
      break if heap[parent] <= heap[i]
      heap[parent], heap[i] = heap[i], heap[parent]
      i = parent
    end
  end

  pop = lambda do
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      i = 0
      size = heap.size
      loop do
        left = i * 2 + 1
        right = left + 1
        smallest = i
        smallest = left if left < size && heap[left] < heap[smallest]
        smallest = right if right < size && heap[right] < heap[smallest]
        break if smallest == i
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
      end
    end
    top
  end

  nums.each { |v| push.call(v) }

  ops = 0
  while !heap.empty? && heap[0] < k
    x = pop.call
    y = pop.call
    new_val = [x, y].min * 2 + [x, y].max
    push.call(new_val)
    ops += 1
  end

  ops
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], k: Int): Int = {
        val pq = new java.util.PriorityQueue[Long]()
        for (v <- nums) {
            pq.add(v.toLong)
        }
        var ops = 0
        while (!pq.isEmpty && pq.peek() < k) {
            val a = pq.poll()
            val b = pq.poll()
            val newVal = a * 2 + b // a is the smaller (or equal) element
            pq.add(newVal)
            ops += 1
        }
        ops
    }
}
```

## Rust

```rust
use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::with_capacity(nums.len());
        for v in nums {
            heap.push(Reverse(v as i64));
        }
        let target = k as i64;
        let mut ops: i32 = 0;
        while let Some(&Reverse(min_val)) = heap.peek() {
            if min_val >= target {
                break;
            }
            // It's guaranteed that we have at least two elements when needed
            let Reverse(x) = heap.pop().unwrap();
            let Reverse(y) = heap.pop().unwrap(); // x <= y because they are the two smallest
            let new_val = x * 2 + y;
            heap.push(Reverse(new_val));
            ops += 1;
        }
        ops
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (min-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([h (make-heap <)]
         [_ (for-each (lambda (v) (heap-add! h v)) nums)])
    (let loop ((ops 0))
      (if (< (heap-min h) k)
          (begin
            (define x (heap-remove-min! h))
            (define y (heap-remove-min! h))
            (heap-add! h (+ (* 2 x) y))
            (loop (add1 ops)))
          ops))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/2]).

-spec min_operations(Nums :: [integer()], K :: integer()) -> integer().
min_operations(Nums, K) ->
    Tree0 = build_tree(Nums),
    loop(Tree0, K, 0).

build_tree([]) -> gb_trees:empty();
build_tree([H|T]) ->
    insert_or_increment(H, build_tree(T)).

insert_or_increment(Key, Tree) ->
    case gb_trees:lookup(Key, Tree) of
        {value, Count} ->
            gb_trees:update(Key, Count + 1, Tree);
        none ->
            gb_trees:insert(Key, 1, Tree)
    end.

pop_min(Tree) ->
    {Key, Count} = gb_trees:smallest(Tree),
    NewTree =
        case Count > 1 of
            true -> gb_trees:update(Key, Count - 1, Tree);
            false -> gb_trees:delete(Key, Tree)
        end,
    {Key, NewTree}.

loop(Tree, K, Ops) ->
    {Min, _} = gb_trees:smallest(Tree),
    if
        Min >= K -> Ops;
        true ->
            {X, T1} = pop_min(Tree),
            {Y, T2} = pop_min(T1),
            NewVal = X * 2 + Y,
            Tree3 = insert_or_increment(NewVal, T2),
            loop(Tree3, K, Ops + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    tree =
      Enum.reduce(nums, :gb_trees.empty(), fn v, acc ->
        case :gb_trees.lookup(v, acc) do
          :none -> :gb_trees.insert(v, 1, acc)
          {_key, cnt} -> :gb_trees.update(v, cnt + 1, acc)
        end
      end)

    loop(tree, k, 0)
  end

  defp loop(tree, k, ops) do
    case :gb_trees.is_empty(tree) do
      true ->
        ops

      false ->
        {min_val, _cnt} = :gb_trees.smallest(tree)

        if min_val >= k do
          ops
        else
          {x, tree1} = pop_min(tree)
          {y, tree2} = pop_min(tree1)
          new_val = x * 2 + y
          tree3 = inc(tree2, new_val)
          loop(tree3, k, ops + 1)
        end
    end
  end

  defp pop_min(tree) do
    {key, cnt} = :gb_trees.smallest(tree)

    new_tree =
      if cnt == 1 do
        :gb_trees.delete(key, tree)
      else
        :gb_trees.update(key, cnt - 1, tree)
      end

    {key, new_tree}
  end

  defp inc(tree, val) do
    case :gb_trees.lookup(val, tree) do
      :none -> :gb_trees.insert(val, 1, tree)
      {_key, cnt} -> :gb_trees.update(val, cnt + 1, tree)
    end
  end
end
```

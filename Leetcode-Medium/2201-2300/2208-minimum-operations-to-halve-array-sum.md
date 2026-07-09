# 2208. Minimum Operations to Halve Array Sum

## Cpp

```cpp
class Solution {
public:
    int halveArray(vector<int>& nums) {
        priority_queue<double> pq;
        double total = 0.0;
        for (int x : nums) {
            total += x;
            pq.push(x);
        }
        double target = total / 2.0;
        int ops = 0;
        while (total > target) {
            double cur = pq.top();
            pq.pop();
            double half = cur / 2.0;
            total -= (cur - half); // reduce sum by half of cur
            pq.push(half);
            ++ops;
        }
        return ops;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int halveArray(int[] nums) {
        PriorityQueue<Double> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        double sum = 0.0;
        for (int num : nums) {
            sum += num;
            maxHeap.offer((double) num);
        }
        double target = sum / 2.0;
        int operations = 0;
        while (sum > target) {
            double largest = maxHeap.poll();
            double half = largest / 2.0;
            sum -= half; // reduction achieved
            maxHeap.offer(half);
            operations++;
        }
        return operations;
    }
}
```

## Python

```python
class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq

        # max-heap using negative values
        max_heap = [-float(x) for x in nums]
        heapq.heapify(max_heap)

        total = sum(nums)
        target = total / 2.0
        cur_sum = total
        ops = 0

        while cur_sum > target:
            # get largest element
            largest = -heapq.heappop(max_heap)   # positive value
            reduced = largest / 2.0
            cur_sum -= (largest - reduced)
            heapq.heappush(max_heap, -reduced)
            ops += 1

        return ops
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        target = total / 2.0
        # max-heap using negative values
        max_heap = [-float(x) for x in nums]
        heapq.heapify(max_heap)

        reduced = 0.0
        ops = 0

        while reduced < target:
            largest = -heapq.heappop(max_heap)
            half = largest / 2.0
            reduced += half
            heapq.heappush(max_heap, -half)
            ops += 1

        return ops
```

## C

```c
#include <stdlib.h>

static void swap(double *a, double *b) {
    double tmp = *a;
    *a = *b;
    *b = tmp;
}

static void siftDown(double *heap, int size, int idx) {
    while (1) {
        int left = 2 * idx + 1;
        int right = left + 1;
        if (left >= size) break;
        int largest = left;
        if (right < size && heap[right] > heap[left]) {
            largest = right;
        }
        if (heap[largest] > heap[idx]) {
            swap(&heap[largest], &heap[idx]);
            idx = largest;
        } else {
            break;
        }
    }
}

static void buildHeap(double *heap, int size) {
    for (int i = (size - 2) / 2; i >= 0; --i) {
        siftDown(heap, size, i);
    }
}

int halveArray(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    
    double *heap = (double *)malloc(numsSize * sizeof(double));
    double total = 0.0;
    for (int i = 0; i < numsSize; ++i) {
        heap[i] = (double)nums[i];
        total += heap[i];
    }
    
    buildHeap(heap, numsSize);
    
    double need = total / 2.0;
    double reduced = 0.0;
    int ops = 0;
    
    while (reduced < need) {
        double cur = heap[0];
        double half = cur / 2.0;
        reduced += cur - half;
        heap[0] = half;
        siftDown(heap, numsSize, 0);
        ++ops;
    }
    
    free(heap);
    return ops;
}
```

## Csharp

```csharp
public class Solution
{
    public int HalveArray(int[] nums)
    {
        double total = 0;
        var pq = new PriorityQueue<double, double>();
        foreach (int num in nums)
        {
            double d = num;
            total += d;
            pq.Enqueue(d, -d); // use negative priority for max‑heap behavior
        }

        double need = total / 2.0;
        double reduced = 0.0;
        int ops = 0;

        while (reduced < need)
        {
            double cur = pq.Dequeue();
            double half = cur / 2.0;
            reduced += cur - half; // which equals cur/2
            pq.Enqueue(half, -half);
            ops++;
        }

        return ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var halveArray = function(nums) {
    class MaxHeap {
        constructor() {
            this.heap = [];
        }
        size() {
            return this.heap.length;
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
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
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
            return top;
        }
    }

    const heap = new MaxHeap();
    let total = 0;
    for (const v of nums) {
        total += v;
        heap.push(v);
    }
    const target = total / 2;
    let ops = 0;
    while (total > target) {
        const maxVal = heap.pop();
        const reduced = maxVal / 2;
        total -= (maxVal - reduced); // net reduction
        heap.push(reduced);
        ops++;
    }
    return ops;
};
```

## Typescript

```typescript
function halveArray(nums: number[]): number {
    class MaxHeap {
        private data: number[] = [];
        push(val: number): void {
            let i = this.data.length;
            this.data.push(val);
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.data[p] >= this.data[i]) break;
                [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
                i = p;
            }
        }
        pop(): number {
            const top = this.data[0];
            const last = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = last;
                let i = 0;
                while (true) {
                    const left = i * 2 + 1;
                    const right = i * 2 + 2;
                    let largest = i;
                    if (left < this.data.length && this.data[left] > this.data[largest]) largest = left;
                    if (right < this.data.length && this.data[right] > this.data[largest]) largest = right;
                    if (largest === i) break;
                    [this.data[i], this.data[largest]] = [this.data[largest], this.data[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    let total = 0;
    for (const v of nums) total += v;
    const target = total / 2;

    const heap = new MaxHeap();
    for (const v of nums) heap.push(v);

    let reduced = 0;
    let ops = 0;
    while (reduced < target) {
        const maxVal = heap.pop();
        const half = maxVal / 2;
        reduced += maxVal - half;
        heap.push(half);
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
     * @return Integer
     */
    function halveArray($nums) {
        $sum = 0.0;
        foreach ($nums as $v) {
            $sum += $v;
        }
        $target = $sum / 2.0;

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        foreach ($nums as $v) {
            $pq->insert($v, $v);
        }

        $ops = 0;
        while ($sum > $target) {
            $maxVal = $pq->extract();
            $half = $maxVal / 2.0;
            $sum -= ($maxVal - $half);
            $pq->insert($half, $half);
            $ops++;
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func halveArray(_ nums: [Int]) -> Int {
        var totalSum = 0.0
        var heap = MaxHeap()
        for num in nums {
            let val = Double(num)
            totalSum += val
            heap.push(val)
        }
        let target = totalSum / 2.0
        var currentSum = totalSum
        var operations = 0
        
        while currentSum > target {
            let maxVal = heap.pop()
            let reduced = maxVal / 2.0
            currentSum -= (maxVal - reduced)
            heap.push(reduced)
            operations += 1
        }
        return operations
    }
}

struct MaxHeap {
    private var data: [Double] = []
    
    mutating func push(_ value: Double) {
        data.append(value)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Double {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }
    
    private mutating func siftUp(_ index: Int) {
        var childIdx = index
        while childIdx > 0 {
            let parentIdx = (childIdx - 1) / 2
            if data[parentIdx] < data[childIdx] {
                data.swapAt(parentIdx, childIdx)
                childIdx = parentIdx
            } else {
                break
            }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parentIdx = index
        while true {
            let leftIdx = 2 * parentIdx + 1
            let rightIdx = leftIdx + 1
            var largestIdx = parentIdx
            
            if leftIdx < data.count && data[leftIdx] > data[largestIdx] {
                largestIdx = leftIdx
            }
            if rightIdx < data.count && data[rightIdx] > data[largestIdx] {
                largestIdx = rightIdx
            }
            if largestIdx == parentIdx { break }
            data.swapAt(parentIdx, largestIdx)
            parentIdx = largestIdx
        }
    }
}
```

## Kotlin

```kotlin
import java.util.Collections
import java.util.PriorityQueue

class Solution {
    fun halveArray(nums: IntArray): Int {
        var total = 0.0
        val maxHeap = PriorityQueue<Double>(Collections.reverseOrder())
        for (num in nums) {
            val v = num.toDouble()
            total += v
            maxHeap.add(v)
        }
        var reduced = 0.0
        var ops = 0
        val target = total / 2.0
        while (reduced < target) {
            val largest = maxHeap.poll()
            val half = largest / 2.0
            reduced += half
            maxHeap.add(half)
            ops++
        }
        return ops
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int halveArray(List<int> nums) {
    double total = 0;
    for (var v in nums) total += v;

    double target = total / 2.0;
    var maxHeap = PriorityQueue<double>((a, b) => b.compareTo(a));
    for (var v in nums) maxHeap.add(v.toDouble());

    int operations = 0;
    while (total > target) {
      double largest = maxHeap.removeFirst();
      double half = largest / 2.0;
      total -= (largest - half);
      maxHeap.add(half);
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

type MaxHeap []float64

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // max‑heap
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(float64))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func halveArray(nums []int) int {
	total := 0.0
	h := &MaxHeap{}
	for _, v := range nums {
		fv := float64(v)
		total += fv
		*h = append(*h, fv)
	}
	heap.Init(h)

	target := total / 2.0
	reduced := 0.0
	ops := 0

	for reduced < target {
		maxVal := heap.Pop(h).(float64)
		half := maxVal / 2.0
		reduced += half
		heap.Push(h, half)
		ops++
	}
	return ops
}
```

## Ruby

```ruby
class MaxHeap
  def initialize
    @data = []
  end

  def push(val)
    i = @data.length
    while i > 0
      parent = (i - 1) / 2
      break if @data[parent] >= val
      @data[i] = @data[parent]
      i = parent
    end
    @data[i] = val
  end

  def pop
    return nil if @data.empty?
    max = @data[0]
    last = @data.pop
    unless @data.empty?
      i = 0
      while (child = 2 * i + 1) < @data.length
        right = child + 1
        child = right if right < @data.length && @data[right] > @data[child]
        break if last >= @data[child]
        @data[i] = @data[child]
        i = child
      end
      @data[i] = last
    end
    max
  end

  def empty?
    @data.empty?
  end
end

# @param {Integer[]} nums
# @return {Integer}
def halve_array(nums)
  total = nums.sum.to_f
  target = total / 2.0
  reduced = 0.0
  heap = MaxHeap.new
  nums.each { |v| heap.push(v.to_f) }

  ops = 0
  while reduced < target
    max_val = heap.pop
    half = max_val / 2.0
    reduced += half
    heap.push(half)
    ops += 1
  end
  ops
end
```

## Scala

```scala
object Solution {
    def halveArray(nums: Array[Int]): Int = {
        import scala.collection.mutable.PriorityQueue
        val pq = PriorityQueue.empty[Double] // max-heap by default
        var total = 0.0
        for (v <- nums) {
            val d = v.toDouble
            total += d
            pq.enqueue(d)
        }
        val target = total / 2.0
        var reduced = 0.0
        var ops = 0
        while (reduced < target) {
            val maxVal = pq.dequeue()
            val half = maxVal / 2.0
            reduced += half          // we saved half of maxVal
            pq.enqueue(half)
            ops += 1
        }
        ops
    }
}
```

## Rust

```rust
use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Clone, Copy)]
struct FloatOrd(f64);

impl PartialEq for FloatOrd {
    fn eq(&self, other: &Self) -> bool {
        self.0 == other.0
    }
}
impl Eq for FloatOrd {}

impl PartialOrd for FloatOrd {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        self.0.partial_cmp(&other.0)
    }
}
impl Ord for FloatOrd {
    fn cmp(&self, other: &Self) -> Ordering {
        // SAFETY: values are never NaN in this problem
        self.partial_cmp(other).unwrap()
    }
}

impl Solution {
    pub fn halve_array(nums: Vec<i32>) -> i32 {
        let mut total: f64 = 0.0;
        let mut heap: BinaryHeap<FloatOrd> = BinaryHeap::new();
        for &x in &nums {
            let v = x as f64;
            total += v;
            heap.push(FloatOrd(v));
        }
        let target = total / 2.0;
        let mut cur_sum = total;
        let mut ops = 0i32;
        while cur_sum > target + 1e-9 {
            if let Some(FloatOrd(val)) = heap.pop() {
                let reduced = val / 2.0;
                cur_sum -= val - reduced;
                heap.push(FloatOrd(reduced));
                ops += 1;
            }
        }
        ops
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define/contract (halve-array nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((total (apply + nums))
         (target (/ total 2))
         (h (make-heap >)))
    (for ([x nums])
      (heap-add! h x))
    (let loop ((curr-sum total) (ops 0))
      (if (<= curr-sum target)
          ops
          (let* ((max-val (heap-pop! h))
                 (new-val (/ max-val 2))
                 (reduction new-val)) ; reduction = max-val - new-val = max-val/2
            (heap-add! h new-val)
            (loop (- curr-sum reduction) (+ ops 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([halve_array/1]).

-spec halve_array(Nums :: [integer()]) -> integer().
halve_array(Nums) ->
    Sum = lists:foldl(fun(X, Acc) -> Acc + X end, 0, Nums),
    Target = Sum / 2,
    Tree0 = build_tree(Nums, gb_trees:empty()),
    loop(Tree0, 0.0, Target, 0).

build_tree([], Tree) ->
    Tree;
build_tree([H | T], Tree) ->
    Tree1 = insert_value(H, Tree),
    build_tree(T, Tree1).

insert_value(V, Tree) ->
    case gb_trees:lookup(V, Tree) of
        {value, C} -> gb_trees:update(V, C + 1, Tree);
        none -> gb_trees:insert(V, 1, Tree)
    end.

loop(_Tree, Reduced, Target, Ops) when Reduced >= Target ->
    Ops;
loop(Tree, Reduced, Target, Ops) ->
    {Max, _Count} = gb_trees:largest(Tree),
    Tree1 =
        case gb_trees:lookup(Max, Tree) of
            {value, 1} -> gb_trees:delete(Max, Tree);
            {value, C} when C > 1 -> gb_trees:update(Max, C - 1, Tree)
        end,
    NewVal = Max / 2,
    Reduced1 = Reduced + (Max - NewVal),
    Tree2 = insert_value(NewVal, Tree1),
    loop(Tree2, Reduced1, Target, Ops + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec halve_array(nums :: [integer]) :: integer
  def halve_array(nums) do
    # Convert numbers to floats for precise halving
    float_nums = Enum.map(nums, &(&1 * 1.0))
    total = Enum.reduce(float_nums, 0.0, &+/2)
    target = total / 2.0

    heap = Heap.from_list(float_nums)

    do_reduce(heap, total, target, 0)
  end

  defp do_reduce(_heap, sum, target, ops) when sum <= target, do: ops

  defp do_reduce(heap, sum, target, ops) do
    {max_val, heap1} = Heap.pop(heap)
    new_sum = sum - max_val / 2.0
    new_heap = Heap.push(heap1, max_val / 2.0)
    do_reduce(new_heap, new_sum, target, ops + 1)
  end

  # Simple binary max-heap implementation using Erlang :array
  defmodule Heap do
    defstruct arr: nil, size: 0

    @spec from_list([float]) :: %Heap{}
    def from_list(list) do
      empty = %Heap{arr: :array.new(0), size: 0}
      Enum.reduce(list, empty, fn v, h -> push(h, v) end)
    end

    @spec push(%Heap{}, float) :: %Heap{}
    def push(%Heap{arr: arr, size: sz} = heap, val) do
      new_arr = :array.set(sz, val, arr)
      heap = %{heap | arr: new_arr, size: sz + 1}
      bubble_up(heap, sz)
    end

    @spec pop(%Heap{}) :: {float, %Heap{}}
    def pop(%Heap{size: 0}) do
      raise "pop from empty heap"
    end

    def pop(%Heap{arr: arr, size: sz} = heap) do
      max_val = :array.get(0, arr)
      last_idx = sz - 1
      last_val = :array.get(last_idx, arr)

      new_arr =
        if last_idx == 0 do
          arr
        else
          :array.set(0, last_val, arr)
        end

      heap = %{heap | arr: new_arr, size: last_idx}
      heap = bubble_down(heap, 0)
      {max_val, heap}
    end

    defp parent(idx), do: div(idx - 1, 2)

    defp left_child(idx), do: idx * 2 + 1
    defp right_child(idx), do: idx * 2 + 2

    defp bubble_up(%Heap{size: sz} = heap, idx) when idx <= 0, do: heap

    defp bubble_up(heap, idx) do
      p_idx = parent(idx)

      if :array.get(idx, heap.arr) > :array.get(p_idx, heap.arr) do
        heap = swap(heap, idx, p_idx)
        bubble_up(heap, p_idx)
      else
        heap
      end
    end

    defp bubble_down(%Heap{size: sz} = heap, idx) do
      l = left_child(idx)
      r = right_child(idx)

      largest =
        cond do
          l < sz and :array.get(l, heap.arr) > :array.get(idx, heap.arr) -> l
          true -> idx
        end

      largest =
        if r < sz and :array.get(r, heap.arr) > :array.get(largest, heap.arr) do
          r
        else
          largest
        end

      if largest != idx do
        heap = swap(heap, idx, largest)
        bubble_down(heap, largest)
      else
        heap
      end
    end

    defp swap(%Heap{arr: arr} = heap, i, j) do
      vi = :array.get(i, arr)
      vj = :array.get(j, arr)

      new_arr =
        arr
        |> :array.set(i, vj)
        |> :array.set(j, vi)

      %{heap | arr: new_arr}
    end
  end
end
```

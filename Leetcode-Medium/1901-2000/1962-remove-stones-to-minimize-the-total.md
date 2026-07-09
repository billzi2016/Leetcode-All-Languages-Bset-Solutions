# 1962. Remove Stones to Minimize the Total

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> pq;
        long long total = 0;
        for (int x : piles) {
            pq.push(x);
            total += x;
        }
        while (k-- && !pq.empty()) {
            int cur = pq.top(); pq.pop();
            int removed = cur / 2;          // floor(cur/2)
            int nxt = cur - removed;        // ceil(cur/2)
            total -= removed;
            pq.push(nxt);
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int minStoneSum(int[] piles, int k) {
        java.util.PriorityQueue<Integer> maxHeap = new java.util.PriorityQueue<>((a, b) -> b - a);
        long sum = 0;
        for (int p : piles) {
            maxHeap.offer(p);
            sum += p;
        }
        for (int i = 0; i < k && !maxHeap.isEmpty(); i++) {
            int cur = maxHeap.poll();
            int reduced = cur / 2;
            sum -= (cur - reduced);
            maxHeap.offer(reduced);
        }
        return (int) sum;
    }
}
```

## Python

```python
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        # Use a max-heap by storing negative values
        max_heap = [-p for p in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            reduced = largest - largest // 2  # remove floor(largest/2) stones
            heapq.heappush(max_heap, -reduced)

        return -sum(max_heap)
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Use a max-heap by storing negative values
        max_heap = [-p for p in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            reduced = largest // 2  # floor division gives floor(largest/2)
            heapq.heappush(max_heap, -reduced)

        return -sum(max_heap)
```

## C

```c
int minStoneSum(int* piles, int pilesSize, int k) {
    long long sum = 0;
    for (int i = 0; i < pilesSize; ++i) sum += piles[i];
    
    // Build max-heap in-place
    for (int i = pilesSize / 2 - 1; i >= 0; --i) {
        int idx = i;
        while (1) {
            int left = 2 * idx + 1;
            int right = left + 1;
            int largest = idx;
            if (left < pilesSize && piles[left] > piles[largest]) largest = left;
            if (right < pilesSize && piles[right] > piles[largest]) largest = right;
            if (largest != idx) {
                int tmp = piles[idx];
                piles[idx] = piles[largest];
                piles[largest] = tmp;
                idx = largest;
            } else break;
        }
    }
    
    for (int i = 0; i < k; ++i) {
        int top = piles[0];
        int newVal = top - top / 2; // ceil(top/2)
        sum -= (top - newVal);
        piles[0] = newVal;
        
        // Heapify down from root
        int idx = 0;
        while (1) {
            int left = 2 * idx + 1;
            int right = left + 1;
            int largest = idx;
            if (left < pilesSize && piles[left] > piles[largest]) largest = left;
            if (right < pilesSize && piles[right] > piles[largest]) largest = right;
            if (largest != idx) {
                int tmp = piles[idx];
                piles[idx] = piles[largest];
                piles[largest] = tmp;
                idx = largest;
            } else break;
        }
    }
    
    return (int)sum;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int MinStoneSum(int[] piles, int k) {
        var pq = new PriorityQueue<int, int>();
        foreach (int p in piles) {
            pq.Enqueue(p, -p); // use negative priority for max-heap behavior
        }

        for (int i = 0; i < k && pq.Count > 0; i++) {
            int x = pq.Dequeue();          // largest element
            int y = x - x / 2;              // remove floor(x/2) stones
            pq.Enqueue(y, -y);
        }

        long total = 0;
        while (pq.Count > 0) {
            total += pq.Dequeue();
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} piles
 * @param {number} k
 * @return {number}
 */
var minStoneSum = function(piles, k) {
    class MaxHeap {
        constructor(arr) {
            this.heap = [];
            for (const v of arr) this.push(v);
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

    const heap = new MaxHeap(piles);
    for (let i = 0; i < k; ++i) {
        const x = heap.pop();
        if (x === undefined) break;
        heap.push(Math.floor(x / 2));
    }
    let sum = 0;
    while (heap.size() > 0) {
        sum += heap.pop();
    }
    return sum;
};
```

## Typescript

```typescript
function minStoneSum(piles: number[], k: number): number {
    class MaxHeap {
        private data: number[] = [];
        size(): number { return this.data.length; }
        push(val: number): void {
            const a = this.data;
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
            const a = this.data;
            if (a.length === 0) return 0;
            const max = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let left = i * 2 + 1,
                        right = i * 2 + 2,
                        largest = i;
                    if (left < a.length && a[left] > a[largest]) largest = left;
                    if (right < a.length && a[right] > a[largest]) largest = right;
                    if (largest === i) break;
                    [a[i], a[largest]] = [a[largest], a[i]];
                    i = largest;
                }
            }
            return max;
        }
    }

    const heap = new MaxHeap();
    for (const p of piles) heap.push(p);

    for (let i = 0; i < k; ++i) {
        const cur = heap.pop();
        const removed = Math.floor(cur / 2);
        heap.push(cur - removed);
    }

    let total = 0;
    while (heap.size() > 0) total += heap.pop();
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $piles
     * @param Integer $k
     * @return Integer
     */
    function minStoneSum($piles, $k) {
        $heap = new SplMaxHeap();
        $total = 0;
        foreach ($piles as $v) {
            $heap->insert($v);
            $total += $v;
        }

        for ($i = 0; $i < $k && !$heap->isEmpty(); $i++) {
            $x = $heap->extract();
            $removed = intdiv($x, 2); // floor(x/2)
            $total -= $removed;
            $newVal = $x - $removed; // ceil(x/2)
            $heap->insert($newVal);
        }

        return $total;
    }
}
```

## Swift

```swift
struct MaxHeap {
    private var data: [Int] = []
    
    init(_ elements: [Int]) {
        data = elements
        if !data.isEmpty {
            for i in stride(from: (data.count / 2) - 1, through: 0, by: -1) {
                siftDown(i)
            }
        }
    }
    
    mutating func insert(_ value: Int) {
        data.append(value)
        siftUp(data.count - 1)
    }
    
    mutating func popMax() -> Int? {
        guard !data.isEmpty else { return nil }
        let maxVal = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return maxVal
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[parent] < data[child] {
                data.swapAt(parent, child)
                child = parent
            } else { break }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var largest = parent
            if left < data.count && data[left] > data[largest] { largest = left }
            if right < data.count && data[right] > data[largest] { largest = right }
            if largest == parent { break }
            data.swapAt(parent, largest)
            parent = largest
        }
    }
}

class Solution {
    func minStoneSum(_ piles: [Int], _ k: Int) -> Int {
        var heap = MaxHeap(piles)
        for _ in 0..<k {
            guard let maxVal = heap.popMax() else { break }
            let reduced = maxVal / 2
            heap.insert(reduced)
        }
        var total = 0
        while let val = heap.popMax() {
            total += val
        }
        return total
    }
}
```

## Kotlin

```kotlin
import java.util.Collections
import java.util.PriorityQueue

class Solution {
    fun minStoneSum(piles: IntArray, k: Int): Int {
        var total = 0L
        val pq = PriorityQueue<Int>(Collections.reverseOrder())
        for (p in piles) {
            total += p
            pq.offer(p)
        }
        repeat(k) {
            val max = pq.poll()
            val removed = max / 2
            total -= removed
            val newVal = max - removed
            pq.offer(newVal)
        }
        return total.toInt()
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int minStoneSum(List<int> piles, int k) {
    var maxHeap = HeapPriorityQueue<int>((a, b) => b.compareTo(a));
    for (var p in piles) {
      maxHeap.add(p);
    }
    for (int i = 0; i < k; i++) {
      int largest = maxHeap.removeFirst();
      int reduced = largest - largest ~/ 2;
      maxHeap.add(reduced);
    }
    int total = 0;
    while (maxHeap.isNotEmpty) {
      total += maxHeap.removeFirst();
    }
    return total;
  }
}
```

## Golang

```go
package main

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minStoneSum(piles []int, k int) int {
	h := &IntHeap{}
	total := 0
	for _, v := range piles {
		total += v
		*h = append(*h, v)
	}
	heap.Init(h)

	for i := 0; i < k; i++ {
		maxVal := heap.Pop(h).(int)
		newVal := maxVal / 2
		total -= maxVal - newVal
		heap.Push(h, newVal)
	}
	return total
}
```

## Ruby

```ruby
class MaxHeap
  def initialize(arr = [])
    @data = arr
    heapify
  end

  def push(val)
    @data << val
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    max = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    max
  end

  def to_a
    @data
  end

  private

  def heapify
    ((@data.size / 2) - 1).downto(0) { |i| sift_down(i) }
  end

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent] >= @data[idx]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      largest = idx
      if left < size && @data[left] > @data[largest]
        largest = left
      end
      if right < size && @data[right] > @data[largest]
        largest = right
      end
      break if largest == idx
      @data[idx], @data[largest] = @data[largest], @data[idx]
      idx = largest
    end
  end
end

# @param {Integer[]} piles
# @param {Integer} k
# @return {Integer}
def min_stone_sum(piles, k)
  heap = MaxHeap.new(piles)
  k.times do
    max_val = heap.pop
    reduced = max_val / 2
    heap.push(reduced)
  end
  heap.to_a.sum
end
```

## Scala

```scala
import scala.collection.mutable.PriorityQueue

object Solution {
  def minStoneSum(piles: Array[Int], k: Int): Int = {
    val pq = PriorityQueue.empty[Int]
    var total = 0
    for (p <- piles) {
      total += p
      pq.enqueue(p)
    }
    var ops = k
    while (ops > 0 && pq.nonEmpty) {
      val x = pq.dequeue()
      val removed = x / 2
      total -= removed
      pq.enqueue(x - removed)
      ops -= 1
    }
    total
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_stone_sum(piles: Vec<i32>, k: i32) -> i32 {
        use std::collections::BinaryHeap;
        let mut heap = BinaryHeap::from(piles);
        for _ in 0..k {
            if let Some(max) = heap.pop() {
                let new_val = max - max / 2; // ceil(max/2)
                heap.push(new_val);
            }
        }
        let sum: i64 = heap.iter().map(|&x| x as i64).sum();
        sum as i32
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (min-stone-sum piles k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([total (apply + piles)]
         [h (make-heap >)])
    (for ([p piles])
      (heap-add! h p))
    (for ([i (in-range k)])
      (when (not (heap-empty? h))
        (define top (heap-min h))
        (heap-remove-min! h)
        (set! total (- total top))
        (define new-pile (quotient (+ top 1) 2)) ; ceil(top/2)
        (set! total (+ total new-pile))
        (heap-add! h new-pile)))
    total))
```

## Erlang

```erlang
-module(solution).
-export([min_stone_sum/2]).

-spec min_stone_sum(Piles :: [integer()], K :: integer()) -> integer().
min_stone_sum(Piles, K) ->
    Tree0 = lists:foldl(fun(V, Acc) -> add_val(Acc, V) end,
                        gb_trees:empty(),
                        Piles),
    TreeFinal = do_k(Tree0, K),
    total_sum(TreeFinal).

%% Insert a value into the multiset tree (increase count)
add_val(Tree, V) ->
    case gb_trees:lookup(V, Tree) of
        {value, C} -> gb_trees:update(V, C + 1, Tree);
        none       -> gb_trees:insert(V, 1, Tree)
    end.

%% Remove one occurrence of a value from the tree
remove_one(Tree, V) ->
    case gb_trees:lookup(V, Tree) of
        {value, 1} -> gb_trees:delete(V, Tree);
        {value, C} -> gb_trees:update(V, C - 1, Tree)
    end.

%% Perform K operations using tail recursion
do_k(Tree, 0) ->
    Tree;
do_k(Tree, K) ->
    {MaxVal, _Count} = gb_trees:largest(Tree),
    Tree1 = remove_one(Tree, MaxVal),
    NewPile = (MaxVal + 1) div 2,
    Tree2 = add_val(Tree1, NewPile),
    do_k(Tree2, K - 1).

%% Compute total sum from the tree
total_sum(Tree) ->
    total_sum(gb_trees:iterator(Tree), 0).

total_sum(Iter, Acc) ->
    case gb_trees:next(Iter) of
        none -> Acc;
        {Key, Count, NextIter} ->
            total_sum(NextIter, Acc + Key * Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_stone_sum(piles :: [integer], k :: integer) :: integer
  def min_stone_sum(piles, k) do
    tree =
      Enum.reduce(piles, :gb_trees.empty(), fn x, t ->
        case :gb_trees.lookup(x, t) do
          :none -> :gb_trees.insert(x, 1, t)
          {:value, cnt} -> :gb_trees.update(x, cnt + 1, t)
        end
      end)

    total = Enum.sum(piles)

    {_final_tree, final_total} =
      Enum.reduce(1..k, {tree, total}, fn _, {t, sum} ->
        {max_val, cnt} = :gb_trees.largest(t)

        t =
          if cnt == 1 do
            :gb_trees.delete(max_val, t)
          else
            :gb_trees.update(max_val, cnt - 1, t)
          end

        removed = div(max_val, 2)
        new_val = max_val - removed
        sum = sum - removed

        t =
          case :gb_trees.lookup(new_val, t) do
            :none -> :gb_trees.insert(new_val, 1, t)
            {:value, c} -> :gb_trees.update(new_val, c + 1, t)
          end

        {t, sum}
      end)

    final_total
  end
end
```

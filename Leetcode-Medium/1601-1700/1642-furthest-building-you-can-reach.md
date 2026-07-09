# 1642. Furthest Building You Can Reach

## Cpp

```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        int n = heights.size();
        for (int i = 0; i < n - 1; ++i) {
            int diff = heights[i + 1] - heights[i];
            if (diff <= 0) continue;
            minHeap.push(diff);
            if ((int)minHeap.size() > ladders) {
                bricks -= minHeap.top();
                minHeap.pop();
                if (bricks < 0) return i;
            }
        }
        return n - 1;
    }
};
```

## Java

```java
class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        java.util.PriorityQueue<Integer> minHeap = new java.util.PriorityQueue<>();
        long remainingBricks = bricks;
        for (int i = 0; i < heights.length - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            if (diff <= 0) continue;
            minHeap.offer(diff);
            if (minHeap.size() > ladders) {
                remainingBricks -= minHeap.poll();
            }
            if (remainingBricks < 0) {
                return i;
            }
        }
        return heights.length - 1;
    }
}
```

## Python

```python
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        import heapq
        min_heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(min_heap, diff)
            # If we have used more ladders than available,
            # convert the smallest climb to bricks.
            if len(min_heap) > ladders:
                bricks -= heapq.heappop(min_heap)
                if bricks < 0:
                    return i
        return len(heights) - 1
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(min_heap, diff)
            if len(min_heap) > ladders:
                smallest = heapq.heappop(min_heap)
                bricks -= smallest
                if bricks < 0:
                    return i
        return len(heights) - 1
```

## C

```c
int furthestBuilding(int* heights, int heightsSize, int bricks, int ladders) {
    long long b = bricks;
    int *heap = (int*)malloc(sizeof(int) * heightsSize);
    int heapSize = 0;

    for (int i = 0; i < heightsSize - 1; ++i) {
        int diff = heights[i + 1] - heights[i];
        if (diff <= 0) continue;

        // push diff into min-heap
        int idx = heapSize;
        heap[heapSize++] = diff;
        while (idx > 0) {
            int parent = (idx - 1) / 2;
            if (heap[parent] <= heap[idx]) break;
            int tmp = heap[parent];
            heap[parent] = heap[idx];
            heap[idx] = tmp;
            idx = parent;
        }

        // if we have used more ladders than available, replace smallest climb with bricks
        if (heapSize > ladders) {
            int minVal = heap[0];
            heapSize--;
            if (heapSize > 0) {
                heap[0] = heap[heapSize];
                int cur = 0;
                while (1) {
                    int left = 2 * cur + 1;
                    int right = 2 * cur + 2;
                    int smallest = cur;
                    if (left < heapSize && heap[left] < heap[smallest]) smallest = left;
                    if (right < heapSize && heap[right] < heap[smallest]) smallest = right;
                    if (smallest == cur) break;
                    int tmp = heap[cur];
                    heap[cur] = heap[smallest];
                    heap[smallest] = tmp;
                    cur = smallest;
                }
            }
            b -= minVal;
            if (b < 0) {
                free(heap);
                return i;
            }
        }
    }

    free(heap);
    return heightsSize - 1;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int FurthestBuilding(int[] heights, int bricks, int ladders) {
        var minHeap = new PriorityQueue<int, int>();
        for (int i = 0; i < heights.Length - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            if (diff <= 0) continue;
            minHeap.Enqueue(diff, diff);
            if (minHeap.Count > ladders) {
                bricks -= minHeap.Dequeue();
                if (bricks < 0) return i;
            }
        }
        return heights.Length - 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */
var furthestBuilding = function(heights, bricks, ladders) {
    class MinHeap {
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
                if (h[p] <= h[i]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const min = h[0];
            const end = h.pop();
            if (h.length > 0) {
                h[0] = end;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = i * 2 + 2;
                    let smallest = i;
                    if (l < h.length && h[l] < h[smallest]) smallest = l;
                    if (r < h.length && h[r] < h[smallest]) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return min;
        }
    }

    const heap = new MinHeap();
    for (let i = 0; i < heights.length - 1; i++) {
        const diff = heights[i + 1] - heights[i];
        if (diff <= 0) continue;
        heap.push(diff);
        if (heap.size() > ladders) {
            bricks -= heap.pop();
            if (bricks < 0) return i;
        }
    }
    return heights.length - 1;
};
```

## Typescript

```typescript
function furthestBuilding(heights: number[], bricks: number, ladders: number): number {
    class MinHeap {
        private data: number[] = [];
        size(): number { return this.data.length; }
        push(val: number): void {
            this.data.push(val);
            let idx = this.data.length - 1;
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.data[parent] <= this.data[idx]) break;
                [this.data[parent], this.data[idx]] = [this.data[idx], this.data[parent]];
                idx = parent;
            }
        }
        pop(): number | undefined {
            if (this.data.length === 0) return undefined;
            const min = this.data[0];
            const end = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = end;
                let idx = 0;
                const length = this.data.length;
                while (true) {
                    let left = idx * 2 + 1;
                    let right = idx * 2 + 2;
                    let smallest = idx;
                    if (left < length && this.data[left] < this.data[smallest]) smallest = left;
                    if (right < length && this.data[right] < this.data[smallest]) smallest = right;
                    if (smallest === idx) break;
                    [this.data[idx], this.data[smallest]] = [this.data[smallest], this.data[idx]];
                    idx = smallest;
                }
            }
            return min;
        }
    }

    const heap = new MinHeap();

    for (let i = 0; i < heights.length - 1; i++) {
        const diff = heights[i + 1] - heights[i];
        if (diff <= 0) continue;

        heap.push(diff);
        if (heap.size() > ladders) {
            const smallest = heap.pop()!;
            bricks -= smallest;
        }
        if (bricks < 0) return i;
    }

    return heights.length - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @param Integer $bricks
     * @param Integer $ladders
     * @return Integer
     */
    function furthestBuilding($heights, $bricks, $ladders) {
        $heap = new SplMinHeap();
        $n = count($heights);
        for ($i = 0; $i < $n - 1; $i++) {
            $diff = $heights[$i + 1] - $heights[$i];
            if ($diff <= 0) {
                continue;
            }
            $heap->insert($diff);
            if ($heap->count() > $ladders) {
                $bricks -= $heap->extract(); // use bricks for the smallest jump
                if ($bricks < 0) {
                    return $i;
                }
            }
        }
        return $n - 1;
    }
}
```

## Swift

```swift
class Solution {
    func furthestBuilding(_ heights: [Int], _ bricks: Int, _ ladders: Int) -> Int {
        var heap = MinHeap()
        var remainingBricks = bricks
        let n = heights.count
        for i in 0..<(n - 1) {
            let diff = heights[i + 1] - heights[i]
            if diff <= 0 { continue }
            heap.push(diff)
            if heap.count > ladders {
                if let smallest = heap.pop() {
                    remainingBricks -= smallest
                    if remainingBricks < 0 {
                        return i
                    }
                }
            }
        }
        return n - 1
    }
}

struct MinHeap {
    private var elements: [Int] = []
    
    var count: Int { elements.count }
    
    mutating func push(_ value: Int) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    mutating func pop() -> Int? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let root = elements[0]
            elements[0] = elements.removeLast()
            siftDown(from: 0)
            return root
        }
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if elements[child] < elements[parent] {
                elements.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < elements.count && elements[left] < elements[smallest] {
                smallest = left
            }
            if right < elements.count && elements[right] < elements[smallest] {
                smallest = right
            }
            if smallest == parent { break }
            elements.swapAt(parent, smallest)
            parent = smallest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun furthestBuilding(heights: IntArray, bricks: Int, ladders: Int): Int {
        var remainingBricks = bricks.toLong()
        val minHeap = java.util.PriorityQueue<Int>()
        for (i in 0 until heights.size - 1) {
            val diff = heights[i + 1] - heights[i]
            if (diff <= 0) continue
            minHeap.add(diff)
            if (minHeap.size > ladders) {
                remainingBricks -= minHeap.poll().toLong()
                if (remainingBricks < 0) return i
            }
        }
        return heights.size - 1
    }
}
```

## Dart

```dart
class MinHeap {
  final List<int> _data = [];

  void add(int val) {
    _data.add(val);
    int i = _data.length - 1;
    while (i > 0) {
      int parent = (i - 1) >> 1;
      if (_data[parent] <= _data[i]) break;
      int tmp = _data[parent];
      _data[parent] = _data[i];
      _data[i] = tmp;
      i = parent;
    }
  }

  int removeMin() {
    if (_data.isEmpty) throw StateError('Heap is empty');
    int min = _data[0];
    int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      int i = 0;
      while (true) {
        int left = i * 2 + 1;
        int right = left + 1;
        int smallest = i;
        if (left < _data.length && _data[left] < _data[smallest]) smallest = left;
        if (right < _data.length && _data[right] < _data[smallest]) smallest = right;
        if (smallest == i) break;
        int tmp = _data[i];
        _data[i] = _data[smallest];
        _data[smallest] = tmp;
        i = smallest;
      }
    }
    return min;
  }

  int get size => _data.length;
}

class Solution {
  int furthestBuilding(List<int> heights, int bricks, int ladders) {
    final heap = MinHeap();
    for (int i = 0; i < heights.length - 1; ++i) {
      int diff = heights[i + 1] - heights[i];
      if (diff <= 0) continue;
      heap.add(diff);
      if (heap.size > ladders) {
        bricks -= heap.removeMin();
      }
      if (bricks < 0) return i;
    }
    return heights.length - 1;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type intMinHeap []int

func (h intMinHeap) Len() int           { return len(h) }
func (h intMinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h intMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *intMinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *intMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func furthestBuilding(heights []int, bricks int, ladders int) int {
	h := &intMinHeap{}
	heap.Init(h)

	for i := 0; i < len(heights)-1; i++ {
		diff := heights[i+1] - heights[i]
		if diff <= 0 {
			continue
		}
		heap.Push(h, diff)
		if h.Len() > ladders {
			smallest := heap.Pop(h).(int)
			bricks -= smallest
			if bricks < 0 {
				return i
			}
		}
	}
	return len(heights) - 1
}
```

## Ruby

```ruby
# @param {Integer[]} heights
# @param {Integer} bricks
# @param {Integer} ladders
# @return {Integer}
def furthest_building(heights, bricks, ladders)
  heap = []

  # push value onto min-heap
  push = lambda do |val|
    heap << val
    idx = heap.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      break if heap[parent] <= heap[idx]
      heap[parent], heap[idx] = heap[idx], heap[parent]
      idx = parent
    end
  end

  # pop smallest value from min-heap
  pop_min = lambda do
    return nil if heap.empty?
    min = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      idx = 0
      size = heap.size
      loop do
        left = idx * 2 + 1
        right = left + 1
        break if left >= size
        smallest = left
        smallest = right if right < size && heap[right] < heap[left]
        break if heap[idx] <= heap[smallest]
        heap[idx], heap[smallest] = heap[smallest], heap[idx]
        idx = smallest
      end
    end
    min
  end

  heights.each_cons(2).with_index do |(h1, h2), i|
    diff = h2 - h1
    next if diff <= 0
    push.call(diff)
    if heap.size > ladders
      smallest = pop_min.call
      bricks -= smallest
      return i if bricks < 0
    end
  end

  heights.length - 1
end
```

## Scala

```scala
object Solution {
    def furthestBuilding(heights: Array[Int], bricks: Int, ladders: Int): Int = {
        import java.util.PriorityQueue
        val pq = new PriorityQueue[Int]()
        var remainingBricks = bricks.toLong
        for (i <- 0 until heights.length - 1) {
            val diff = heights(i + 1) - heights(i)
            if (diff > 0) {
                pq.add(diff)
                if (pq.size() > ladders) {
                    val smallest = pq.poll()
                    remainingBricks -= smallest
                }
                if (remainingBricks < 0) return i
            }
        }
        heights.length - 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn furthest_building(heights: Vec<i32>, bricks: i32, ladders: i32) -> i32 {
        use std::collections::BinaryHeap;
        use std::cmp::Reverse;

        let n = heights.len();
        if n == 0 {
            return 0;
        }
        let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut remaining_bricks = bricks as i64;
        let ladders_usize = ladders as usize;

        for i in 0..n - 1 {
            let diff = heights[i + 1] - heights[i];
            if diff > 0 {
                heap.push(Reverse(diff));
                if heap.len() > ladders_usize {
                    if let Some(Reverse(smallest)) = heap.pop() {
                        remaining_bricks -= smallest as i64;
                        if remaining_bricks < 0 {
                            return i as i32;
                        }
                    }
                }
            }
        }
        (n - 1) as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define/contract (furthest-building heights bricks ladders)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ([n (length heights)]
         [hvec (list->vector heights)]
         [heap (make-heap <)])
    (let loop ([i 0] [bricks-left bricks])
      (if (>= i (- n 1))
          (- n 1)
          (let* ([diff (- (vector-ref hvec (+ i 1)) (vector-ref hvec i))]
                 [new-bricks bricks-left])
            (when (> diff 0)
              (heap-push! heap diff)
              (when (> (heap-count heap) ladders)
                (set! new-bricks (- new-bricks (heap-pop! heap)))))
            (if (< new-bricks 0)
                i
                (loop (+ i 1) new-bricks)))))))
```

## Erlang

```erlang
-module(solution).
-export([furthest_building/3]).

-spec furthest_building(Heights :: [integer()], Bricks :: integer(), Ladders :: integer()) -> integer().
furthest_building(Heights, Bricks, Ladders) ->
    case Heights of
        [] -> -1;
        [_] -> 0;
        _ -> go(Heights, Bricks, Ladders, gb_trees:empty(), 0, 0)
    end.

go([_Prev], _Bricks, _Ladders, _Tree, _LadderCnt, Index) ->
    Index;
go([Prev, Next | Rest], Bricks, Ladders, Tree, LadderCnt, Index) ->
    Diff = Next - Prev,
    if
        Diff =< 0 ->
            go([Next | Rest], Bricks, Ladders, Tree, LadderCnt, Index + 1);
        true ->
            NewTree = inc(Tree, Diff),
            NewLadderCnt = LadderCnt + 1,
            case maybe_use_bricks(NewTree, NewLadderCnt, Ladders, Bricks) of
                {ok, UpdatedTree, UpdatedLadderCnt, UpdatedBricks} ->
                    go([Next | Rest], UpdatedBricks, Ladders, UpdatedTree, UpdatedLadderCnt, Index + 1);
                {fail, _} ->
                    Index
            end
    end.

maybe_use_bricks(Tree, LadderCnt, Ladders, Bricks) when LadderCnt =< Ladders ->
    {ok, Tree, LadderCnt, Bricks};
maybe_use_bricks(Tree, LadderCnt, Ladders, Bricks) ->
    {MinDiff, Count} = gb_trees:smallest(Tree),
    NewBricks = Bricks - MinDiff,
    if
        NewBricks < 0 ->
            {fail, nil};
        true ->
            UpdatedTree = case Count of
                1 -> gb_trees:delete(MinDiff, Tree);
                _ -> gb_trees:update(MinDiff, Count - 1, Tree)
            end,
            {ok, UpdatedTree, LadderCnt - 1, NewBricks}
    end.

inc(Tree, Key) ->
    case gb_trees:lookup(Key, Tree) of
        {value, Count} -> gb_trees:update(Key, Count + 1, Tree);
        none -> gb_trees:insert(Key, 1, Tree)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec furthest_building(heights :: [integer], bricks :: integer, ladders :: integer) :: integer
  def furthest_building(heights, bricks, ladders) do
    go(heights, bricks, ladders, :gb_trees.empty(), 0, 0)
  end

  # Reached the last building
  defp go([_single], _bricks, _ladders, _tree, _size, idx), do: idx

  # Process next jump
  defp go([cur, nxt | rest] = _list, bricks, ladders, tree, size, idx) do
    diff = nxt - cur

    if diff <= 0 do
      # No resources needed for this move
      go([nxt | rest], bricks, ladders, tree, size, idx + 1)
    else
      # Record the climb
      tree2 = insert(tree, diff)
      size2 = size + 1

      {tree3, size3, bricks2} =
        if size2 > ladders do
          {:value, min_diff} = :gb_trees.smallest(tree2)
          bricks_new = bricks - min_diff
          tree_new = delete_one(tree2, min_diff)
          {tree_new, size2 - 1, bricks_new}
        else
          {tree2, size2, bricks}
        end

      if bricks2 < 0 do
        idx
      else
        go([nxt | rest], bricks2, ladders, tree3, size3, idx + 1)
      end
    end
  end

  # Insert a value into the multiset (as a gb_tree with counts)
  defp insert(tree, key) do
    case :gb_trees.lookup(key, tree) do
      :none -> :gb_trees.insert(key, 1, tree)
      {:value, cnt} -> :gb_trees.update(key, cnt + 1, tree)
    end
  end

  # Delete one occurrence of a key from the multiset
  defp delete_one(tree, key) do
    case :gb_trees.lookup(key, tree) do
      {:value, 1} -> :gb_trees.delete(key, tree)
      {:value, cnt} -> :gb_trees.update(key, cnt - 1, tree)
      :none -> tree
    end
  end
end
```

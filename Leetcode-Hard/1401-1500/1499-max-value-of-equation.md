# 1499. Max Value of Equation

## Cpp

```cpp
class Solution {
public:
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        using P = pair<long long,int>;
        priority_queue<P> pq; // max-heap by first (yi - xi)
        long long ans = LLONG_MIN;
        for (const auto& pt : points) {
            long long x = pt[0];
            long long y = pt[1];
            while (!pq.empty() && x - pq.top().second > k) {
                pq.pop();
            }
            if (!pq.empty()) {
                ans = max(ans, pq.top().first + y + x);
            }
            pq.emplace(y - x, (int)x);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static class Pair {
        int value; // yi - xi
        int x;
        Pair(int value, int x) {
            this.value = value;
            this.x = x;
        }
    }

    public int findMaxValueOfEquation(int[][] points, int k) {
        java.util.PriorityQueue<Pair> maxHeap = new java.util.PriorityQueue<>(
                (a, b) -> Integer.compare(b.value, a.value));
        int answer = Integer.MIN_VALUE;

        for (int[] p : points) {
            int xj = p[0];
            int yj = p[1];

            // Remove points that are out of the allowed distance
            while (!maxHeap.isEmpty() && xj - maxHeap.peek().x > k) {
                maxHeap.poll();
            }

            if (!maxHeap.isEmpty()) {
                int candidate = maxHeap.peek().value + yj + xj;
                if (candidate > answer) {
                    answer = candidate;
                }
            }

            // Add current point as a potential i for future j
            maxHeap.offer(new Pair(yj - xj, xj));
        }

        return answer;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        max_heap = []  # stores (-(yi - xi), xi)
        ans = float('-inf')
        for x, y in points:
            while max_heap and x - max_heap[0][1] > k:
                heapq.heappop(max_heap)
            if max_heap:
                best = -max_heap[0][0] + y + x  # (yi - xi) + yj + xj
                if best > ans:
                    ans = best
            heapq.heappush(max_heap, (-(y - x), x))
        return int(ans)
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_heap = []  # stores (- (yi - xi), xi)
        ans = -10**18  # sufficiently small
        
        for x, y in points:
            # Remove points that are farther than k
            while max_heap and x - max_heap[0][1] > k:
                heapq.heappop(max_heap)
            
            if max_heap:
                best_val = -max_heap[0][0]  # yi - xi
                ans = max(ans, best_val + y + x)
            
            # Push current point as potential i for future j
            heapq.heappush(max_heap, (-(y - x), x))
        
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int findMaxValueOfEquation(int** points, int pointsSize, int* pointsColSize, int k) {
    int *heapVal = (int *)malloc(sizeof(int) * pointsSize);
    int *heapX   = (int *)malloc(sizeof(int) * pointsSize);
    int heapSize = 0;
    long long ans = LLONG_MIN;

    for (int idx = 0; idx < pointsSize; ++idx) {
        int x = points[idx][0];
        int y = points[idx][1];

        while (heapSize > 0 && x - heapX[0] > k) {
            // pop top
            heapVal[0] = heapVal[heapSize - 1];
            heapX[0]   = heapX[heapSize - 1];
            --heapSize;

            int i = 0;
            while (1) {
                int left = i * 2 + 1;
                int right = i * 2 + 2;
                if (left >= heapSize) break;
                int largest = left;
                if (right < heapSize && heapVal[right] > heapVal[left])
                    largest = right;
                if (heapVal[i] >= heapVal[largest]) break;
                // swap
                int tmpV = heapVal[i]; heapVal[i] = heapVal[largest]; heapVal[largest] = tmpV;
                int tmpX = heapX[i];   heapX[i]   = heapX[largest];   heapX[largest]   = tmpX;
                i = largest;
            }
        }

        if (heapSize > 0) {
            long long candidate = (long long)heapVal[0] + y + x;
            if (candidate > ans) ans = candidate;
        }

        // push current point
        int curVal = y - x;
        int i = heapSize;
        heapVal[i] = curVal;
        heapX[i]   = x;
        ++heapSize;

        while (i > 0) {
            int parent = (i - 1) / 2;
            if (heapVal[parent] >= heapVal[i]) break;
            // swap
            int tmpV = heapVal[parent]; heapVal[parent] = heapVal[i]; heapVal[i] = tmpV;
            int tmpX = heapX[parent];   heapX[parent]   = heapX[i];   heapX[i]   = tmpX;
            i = parent;
        }
    }

    free(heapVal);
    free(heapX);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int FindMaxValueOfEquation(int[][] points, int k) {
        var deque = new LinkedList<(int val, int x)>();
        int ans = int.MinValue;
        foreach (var p in points) {
            int x = p[0];
            int y = p[1];

            while (deque.Count > 0 && x - deque.First.Value.x > k) {
                deque.RemoveFirst();
            }

            if (deque.Count > 0) {
                ans = Math.Max(ans, deque.First.Value.val + y + x);
            }

            int curVal = y - x;
            while (deque.Count > 0 && deque.Last.Value.val <= curVal) {
                deque.RemoveLast();
            }
            deque.AddLast((curVal, x));
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number}
 */
var findMaxValueOfEquation = function(points, k) {
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
        push(node) {
            const h = this.heap;
            h.push(node);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p].value >= h[i].value) break;
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
                    if (l < h.length && h[l].value > h[largest].value) largest = l;
                    if (r < h.length && h[r].value > h[largest].value) largest = r;
                    if (largest === i) break;
                    [h[i], h[largest]] = [h[largest], h[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    const heap = new MaxHeap();
    let ans = -Infinity;

    for (const [xj, yj] of points) {
        // Remove points that are farther than k
        while (heap.size() > 0 && xj - heap.peek().x > k) {
            heap.pop();
        }
        if (heap.size() > 0) {
            const candidate = heap.peek().value + yj + xj; // (yi - xi) + (yj + xj)
            if (candidate > ans) ans = candidate;
        }
        // Insert current point as potential i for future j
        heap.push({ value: yj - xj, x: xj });
    }

    return ans;
};
```

## Typescript

```typescript
function findMaxValueOfEquation(points: number[][], k: number): number {
    class MaxHeap<T> {
        private data: T[] = [];
        private compare: (a: T, b: T) => number;
        constructor(compare: (a: T, b: T) => number) {
            this.compare = compare;
        }
        size(): number { return this.data.length; }
        peek(): T { return this.data[0]; }
        push(item: T): void {
            this.data.push(item);
            this.bubbleUp(this.data.length - 1);
        }
        pop(): T | undefined {
            if (this.data.length === 0) return undefined;
            const top = this.data[0];
            const end = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(idx: number): void {
            let parent = Math.floor((idx - 1) / 2);
            while (idx > 0 && this.compare(this.data[idx], this.data[parent]) > 0) {
                [this.data[idx], this.data[parent]] = [this.data[parent], this.data[idx]];
                idx = parent;
                parent = Math.floor((idx - 1) / 2);
            }
        }
        private bubbleDown(idx: number): void {
            const n = this.data.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let largest = idx;
                if (left < n && this.compare(this.data[left], this.data[largest]) > 0) largest = left;
                if (right < n && this.compare(this.data[right], this.data[largest]) > 0) largest = right;
                if (largest === idx) break;
                [this.data[idx], this.data[largest]] = [this.data[largest], this.data[idx]];
                idx = largest;
            }
        }
    }

    const heap = new MaxHeap<[number, number]>((a, b) => a[0] - b[0]); // compare by (yi - xi)
    let ans = -Infinity;

    for (const [xj, yj] of points) {
        while (heap.size() && xj - heap.peek()[1] > k) {
            heap.pop();
        }
        if (heap.size()) {
            const candidate = heap.peek()[0] + yj + xj;
            if (candidate > ans) ans = candidate;
        }
        heap.push([yj - xj, xj]);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer $k
     * @return Integer
     */
    function findMaxValueOfEquation($points, $k) {
        $heap = new SplPriorityQueue();
        // We need both data (xi) and priority (yi - xi)
        $heap->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        
        $ans = PHP_INT_MIN;
        
        foreach ($points as $pt) {
            [$x, $y] = $pt;
            
            // Remove points that are out of the allowed window
            while (!$heap->isEmpty()) {
                $top = $heap->current(); // peek without removing
                $xi = $top['data'][0];
                if ($x - $xi > $k) {
                    $heap->extract();
                } else {
                    break;
                }
            }
            
            // If there is a valid previous point, compute candidate answer
            if (!$heap->isEmpty()) {
                $top = $heap->current();
                $candidate = $top['priority'] + $y + $x; // (yi - xi) + yj + xj
                if ($candidate > $ans) {
                    $ans = $candidate;
                }
            }
            
            // Insert current point for future calculations
            $heap->insert([$x], $y - $x);
        }
        
        return $ans;
    }
}
```

## Swift

```swift
import Foundation

struct HeapNode {
    var value: Int
    var x: Int
}

struct MaxHeap {
    private var heap = [HeapNode]()
    var isEmpty: Bool { heap.isEmpty }
    func peek() -> HeapNode? { heap.first }
    
    mutating func push(_ node: HeapNode) {
        heap.append(node)
        siftUp(heap.count - 1)
    }
    
    mutating func pop() -> HeapNode? {
        guard !heap.isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeLast()
        } else {
            let top = heap[0]
            heap[0] = heap.removeLast()
            siftDown(0)
            return top
        }
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if heap[child].value > heap[parent].value {
                heap.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = 2 * parent + 1
            let right = left + 1
            var largest = parent
            if left < heap.count && heap[left].value > heap[largest].value {
                largest = left
            }
            if right < heap.count && heap[right].value > heap[largest].value {
                largest = right
            }
            if largest == parent { break }
            heap.swapAt(parent, largest)
            parent = largest
        }
    }
}

class Solution {
    func findMaxValueOfEquation(_ points: [[Int]], _ k: Int) -> Int {
        var maxHeap = MaxHeap()
        var answer = Int.min
        
        for point in points {
            let x = point[0]
            let y = point[1]
            
            while let top = maxHeap.peek(), x - top.x > k {
                _ = maxHeap.pop()
            }
            
            if let top = maxHeap.peek() {
                let candidate = top.value + y + x
                if candidate > answer { answer = candidate }
            }
            
            let node = HeapNode(value: y - x, x: x)
            maxHeap.push(node)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaxValueOfEquation(points: Array<IntArray>, k: Int): Int {
        val n = points.size
        var answer = Int.MIN_VALUE
        val deque: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        for (j in 0 until n) {
            // Remove indices that are out of the allowed distance window
            while (!deque.isEmpty() && points[j][0] - points[deque.peekFirst()] > k) {
                deque.pollFirst()
            }
            // Compute candidate using the best i within window
            if (!deque.isEmpty()) {
                val i = deque.peekFirst()
                val candidate = (points[i][1] - points[i][0]) + (points[j][1] + points[j][0])
                if (candidate > answer) answer = candidate
            }
            // Maintain deque in decreasing order of (yi - xi)
            val curVal = points[j][1] - points[j][0]
            while (!deque.isEmpty() && (points[deque.peekLast()][1] - points[deque.peekLast()][0]) <= curVal) {
                deque.pollLast()
            }
            deque.addLast(j)
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:collection';

class _Entry {
  final int val; // yi - xi
  final int x;
  _Entry(this.val, this.x);
}

class Solution {
  int findMaxValueOfEquation(List<List<int>> points, int k) {
    final Queue<_Entry> deque = Queue<_Entry>();
    int ans = -(1 << 60); // sufficiently small

    for (final p in points) {
      final int x = p[0];
      final int y = p[1];

      // Remove entries that are farther than k
      while (deque.isNotEmpty && x - deque.first.x > k) {
        deque.removeFirst();
      }

      // Update answer using the best candidate so far
      if (deque.isNotEmpty) {
        ans = _max(ans, deque.first.val + y + x);
      }

      // Insert current point maintaining decreasing order of (yi - xi)
      final int curVal = y - x;
      while (deque.isNotEmpty && deque.last.val <= curVal) {
        deque.removeLast();
      }
      deque.addLast(_Entry(curVal, x));
    }

    return ans;
  }

  int _max(int a, int b) => a > b ? a : b;
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type item struct {
	val int // yi - xi
	x   int // xi
}

// max-heap based on val
type maxHeap []item

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i].val > h[j].val } // reverse for max
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(item))
}

func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func findMaxValueOfEquation(points [][]int, k int) int {
	h := &maxHeap{}
	heap.Init(h)

	const infNeg = -1 << 63
	ans := infNeg

	for _, p := range points {
		xj, yj := p[0], p[1]

		// discard points out of the allowed window
		for h.Len() > 0 && (*h)[0].x < xj-k {
			heap.Pop(h)
		}

		if h.Len() > 0 {
			candidate := (*h)[0].val + yj + xj // (yi - xi) + (yj + xj)
			if candidate > ans {
				ans = candidate
			}
		}

		// current point can serve as i for future j
		heap.Push(h, item{val: yj - xj, x: xj})
	}

	return ans
}
```

## Ruby

```ruby
def find_max_value_of_equation(points, k)
  deque = [] # each element is [value = yi - xi, xi]
  max_ans = -Float::INFINITY

  points.each do |x, y|
    while !deque.empty? && x - deque[0][1] > k
      deque.shift
    end

    unless deque.empty?
      candidate = deque[0][0] + y + x
      max_ans = candidate if candidate > max_ans
    end

    cur_val = y - x
    while !deque.empty? && deque[-1][0] <= cur_val
      deque.pop
    end
    deque << [cur_val, x]
  end

  max_ans.to_i
end
```

## Scala

```scala
object Solution {
    def findMaxValueOfEquation(points: Array[Array[Int]], k: Int): Int = {
        import scala.collection.mutable.PriorityQueue
        case class Node(value: Int, x: Int)
        implicit val ord: Ordering[Node] = Ordering.by[Node, Int](_.value)
        val pq = PriorityQueue.empty[Node]
        var ans = Int.MinValue

        for (p <- points) {
            val x = p(0)
            val y = p(1)

            while (pq.nonEmpty && x - pq.head.x > k) {
                pq.dequeue()
            }

            if (pq.nonEmpty) {
                val candidate = pq.head.value + y + x
                if (candidate > ans) ans = candidate
            }

            pq.enqueue(Node(y - x, x))
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_max_value_of_equation(points: Vec<Vec<i32>>, k: i32) -> i32 {
        use std::collections::BinaryHeap;
        let mut heap: BinaryHeap<(i64, i64)> = BinaryHeap::new(); // (yi - xi, xi)
        let k = k as i64;
        let mut ans = i64::MIN;

        for p in points.iter() {
            let x = p[0] as i64;
            let y = p[1] as i64;

            while let Some(&(_, xi)) = heap.peek() {
                if x - xi > k {
                    heap.pop();
                } else {
                    break;
                }
            }

            if let Some(&(val, _)) = heap.peek() {
                let candidate = val + y + x;
                if candidate > ans {
                    ans = candidate;
                }
            }

            heap.push((y - x, x));
        }

        ans as i32
    }
}
```

## Racket

```racket
(require racket/heap)

(define (max-comp a b)
  (> (first a) (first b))) ; larger value has higher priority

(define/contract (find-max-value-of-equation points k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([h (make-heap max-comp)]
         [ans (let ([init (- (expt 10 18))]) init)])
    (for ([pt points])
      (define x (first pt))
      (define y (second pt))
      ;; discard points whose x is too far from current x
      (let loop ()
        (when (and (not (heap-empty? h))
                   (> (- x (second (heap-peek h))) k))
          (heap-remove-min! h)
          (loop)))
      ;; compute candidate using best previous point
      (unless (heap-empty? h)
        (define cand (+ y x (first (heap-peek h)))) ; yi - xi + yj + xj
        (set! ans (max ans cand)))
      ;; insert current point's value for future candidates
      (heap-insert! h (list (- y x) x)))
    ans))
```

## Erlang

```erlang
-spec find_max_value_of_equation(Points :: [[integer()]], K :: integer()) -> integer().
find_max_value_of_equation(Points, K) ->
    find_max_value_of_equation(Points, K, gb_trees:empty(), 0, -1000000000).

find_max_value_of_equation([], _K, _Tree, _Idx, Max) -> Max;
find_max_value_of_equation([[Xj, Yj] | Rest], K, Tree0, Idx, Max0) ->
    Tree1 = clean_tree(Tree0, Xj, K),
    Max1 = case gb_trees:is_empty(Tree1) of
        true -> Max0;
        false ->
            {{Val, _Id}, Xi} = gb_trees:largest(Tree1),
            Candidate = Val + (Yj + Xj),
            if Candidate > Max0 -> Candidate; true -> Max0 end
    end,
    Value = Yj - Xj,
    Key = {Value, Idx},
    Tree2 = gb_trees:insert(Key, Xj, Tree1),
    find_max_value_of_equation(Rest, K, Tree2, Idx + 1, Max1).

clean_tree(Tree, Xj, K) ->
    case gb_trees:is_empty(Tree) of
        true -> Tree;
        false ->
            {{Val, Id}, Xi} = gb_trees:largest(Tree),
            if Xj - Xi > K ->
                    clean_tree(gb_trees:delete({Val, Id}, Tree), Xj, K);
               true -> Tree
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_value_of_equation(points :: [[integer]], k :: integer) :: integer
  def find_max_value_of_equation(points, k) do
    tree = :gb_trees.empty()

    {ans, _} =
      Enum.reduce(points, {-1_000_000_000_000, tree}, fn [x, y], {cur_ans, t} ->
        bound = x - k

        t = clean_top(t, bound)

        cur_ans =
          if not :gb_trees.is_empty(t) do
            {max_val, _q} = :gb_trees.largest(t)
            cand = max_val + y + x
            if cand > cur_ans, do: cand, else: cur_ans
          else
            cur_ans
          end

        key = y - x

        t =
          case :gb_trees.lookup(key, t) do
            :none ->
              q = :queue.in(x, :queue.new())
              :gb_trees.insert(key, q, t)

            {:value, q} ->
              q2 = :queue.in(x, q)
              :gb_trees.update(key, q2, t)
          end

        {cur_ans, t}
      end)

    ans
  end

  defp clean_top(tree, bound) do
    cond do
      :gb_trees.is_empty(tree) ->
        tree

      true ->
        {max_val, q} = :gb_trees.largest(tree)

        case :queue.out(q) do
          {:empty, _} ->
            new_tree = :gb_trees.delete(max_val, tree)
            clean_top(new_tree, bound)

          {{:value, old_x}, rest_q} ->
            if old_x < bound do
              new_tree =
                if :queue.is_empty(rest_q) do
                  :gb_trees.delete(max_val, tree)
                else
                  :gb_trees.update(max_val, rest_q, tree)
                end

              clean_top(new_tree, bound)
            else
              tree
            end
        end
    end
  end
end
```

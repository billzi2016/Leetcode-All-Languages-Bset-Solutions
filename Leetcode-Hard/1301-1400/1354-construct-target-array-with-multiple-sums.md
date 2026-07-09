# 1354. Construct Target Array With Multiple Sums

## Cpp

```cpp
class Solution {
public:
    bool isPossible(vector<int>& target) {
        int n = target.size();
        if (n == 1) return target[0] == 1;
        
        priority_queue<long long> pq;
        long long total = 0;
        for (int x : target) {
            pq.push(x);
            total += x;
        }
        
        while (true) {
            long long cur = pq.top(); pq.pop();
            long long rest = total - cur;
            
            if (cur == 1 || rest == 1) return true;
            if (rest == 0 || cur < rest) return false;
            
            long long prev = cur % rest;
            if (prev == 0) prev = rest;
            if (prev < 1) return false;
            
            total = rest + prev;
            pq.push(prev);
        }
    }
};
```

## Java

```java
class Solution {
    public boolean isPossible(int[] target) {
        if (target.length == 1) {
            return target[0] == 1;
        }
        java.util.PriorityQueue<Long> maxHeap = new java.util.PriorityQueue<>(java.util.Collections.reverseOrder());
        long totalSum = 0L;
        for (int v : target) {
            totalSum += v;
            maxHeap.add((long) v);
        }
        while (true) {
            long max = maxHeap.poll();
            long rest = totalSum - max;
            if (max == 1 || rest == 1) {
                return true;
            }
            if (rest == 0 || max < rest) {
                return false;
            }
            long prev = max % rest;
            if (prev == 0) {
                return false;
            }
            totalSum = rest + prev;
            maxHeap.add(prev);
        }
    }
}
```

## Python

```python
class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        import heapq

        n = len(target)
        if n == 1:
            return target[0] == 1

        total = sum(target)
        # max-heap using negative values
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest

            # If the largest element is already 1 or the rest sums to 1,
            # we can always reduce it to 1.
            if largest == 1 or rest == 1:
                return True

            # Invalid cases
            if rest == 0 or largest < rest:
                return False

            # Compute previous value of the largest element
            new_val = largest % rest
            if new_val == 0:
                new_val = rest

            # If no progress is made, it's impossible
            if new_val == largest:
                return False

            total = rest + new_val
            heapq.heappush(heap, -new_val)
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        total = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while True:
            a = -heapq.heappop(max_heap)
            rest = total - a

            if a == 1 or rest == 1:
                return True
            if rest == 0 or a < rest:
                return False

            prev = a % rest
            if prev == 0:
                prev = rest

            if prev == a:
                return False

            total = rest + prev
            heapq.heappush(max_heap, -prev)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static void swap(long long *a, long long *b) {
    long long tmp = *a;
    *a = *b;
    *b = tmp;
}

/* heapify down from index i for a max-heap */
static void heapify_down(long long *heap, int size, int i) {
    while (1) {
        int left = 2 * i + 1;
        int right = left + 1;
        int largest = i;

        if (left < size && heap[left] > heap[largest])
            largest = left;
        if (right < size && heap[right] > heap[largest])
            largest = right;

        if (largest == i)
            break;

        swap(&heap[i], &heap[largest]);
        i = largest;
    }
}

/* build max-heap */
static void build_max_heap(long long *heap, int size) {
    for (int i = (size - 2) / 2; i >= 0; --i)
        heapify_down(heap, size, i);
}

bool isPossible(int* target, int targetSize) {
    if (targetSize == 1)
        return target[0] == 1;

    long long *heap = (long long *)malloc(sizeof(long long) * targetSize);
    if (!heap) return false; // allocation failure, treat as impossible

    long long total = 0;
    for (int i = 0; i < targetSize; ++i) {
        heap[i] = target[i];
        total += heap[i];
    }

    build_max_heap(heap, targetSize);

    while (true) {
        long long maxVal = heap[0];
        long long rest = total - maxVal;

        if (maxVal == 1 || rest == 1)
            break; // can reduce everything to ones

        if (rest == 0 || maxVal <= rest)
            { free(heap); return false; }

        long long prev = maxVal % rest;
        if (prev == 0)
            prev = rest;

        if (prev < 1)
            { free(heap); return false; }

        total = rest + prev;
        heap[0] = prev;
        heapify_down(heap, targetSize, 0);
    }

    free(heap);
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsPossible(int[] target)
    {
        int n = target.Length;
        if (n == 1) return target[0] == 1;

        long total = 0;
        MaxHeap heap = new MaxHeap(n);
        foreach (int v in target)
        {
            total += v;
            heap.Push(v);
        }

        while (true)
        {
            int max = heap.Pop();
            long rest = total - max;

            if (max == 1 || rest == 1) return true;
            if (rest == 0 || max <= rest) return false;

            int newVal = (int)(max % rest);
            if (newVal == 0) newVal = (int)rest; // when rest divides max

            total = rest + newVal;
            heap.Push(newVal);
        }
    }

    private class MaxHeap
    {
        private readonly int[] _heap;
        private int _size;

        public MaxHeap(int capacity)
        {
            _heap = new int[capacity + 1]; // 1-indexed
            _size = 0;
        }

        public void Push(int val)
        {
            _heap[++_size] = val;
            int i = _size;
            while (i > 1 && _heap[i / 2] < _heap[i])
            {
                Swap(i, i / 2);
                i /= 2;
            }
        }

        public int Pop()
        {
            int top = _heap[1];
            _heap[1] = _heap[_size--];
            Heapify(1);
            return top;
        }

        private void Heapify(int i)
        {
            while (true)
            {
                int left = i * 2;
                int right = left + 1;
                int largest = i;

                if (left <= _size && _heap[left] > _heap[largest]) largest = left;
                if (right <= _size && _heap[right] > _heap[largest]) largest = right;

                if (largest == i) break;

                Swap(i, largest);
                i = largest;
            }
        }

        private void Swap(int i, int j)
        {
            int tmp = _heap[i];
            _heap[i] = _heap[j];
            _heap[j] = tmp;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} target
 * @return {boolean}
 */
var isPossible = function(target) {
    const n = target.length;
    if (n === 1) return target[0] === 1;

    class MaxHeap {
        constructor() {
            this.heap = [];
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
            if (h.length === 1) return h.pop();
            const max = h[0];
            const end = h.pop();
            h[0] = end;
            this._down(0);
            return max;
        }
        _down(i) {
            const h = this.heap;
            const n = h.length;
            while (true) {
                let l = i * 2 + 1;
                let r = l + 1;
                let largest = i;
                if (l < n && h[l] > h[largest]) largest = l;
                if (r < n && h[r] > h[largest]) largest = r;
                if (largest === i) break;
                [h[i], h[largest]] = [h[largest], h[i]];
                i = largest;
            }
        }
    }

    const heap = new MaxHeap();
    let total = 0;
    for (const v of target) {
        heap.push(v);
        total += v;
    }

    while (true) {
        const max = heap.pop();
        const rest = total - max;

        if (max === 1 || rest === 1) return true;
        if (rest === 0 || max < rest) return false;

        let prev = max % rest;
        if (prev === 0) prev = rest; // must have been at least one subtraction

        if (prev === max) return false; // no progress

        total = rest + prev;
        heap.push(prev);
    }
};
```

## Typescript

```typescript
function isPossible(target: number[]): boolean {
    const n = target.length;
    if (n === 1) return target[0] === 1;

    class MaxHeap {
        private heap: number[] = [];
        constructor(arr?: number[]) {
            if (arr) {
                for (const v of arr) this.push(v);
            }
        }
        size(): number { return this.heap.length; }
        push(val: number): void {
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
        pop(): number {
            const h = this.heap;
            const top = h[0];
            const last = h.pop()!;
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let left = i * 2 + 1;
                    let right = left + 1;
                    let largest = i;
                    if (left < h.length && h[left] > h[largest]) largest = left;
                    if (right < h.length && h[right] > h[largest]) largest = right;
                    if (largest === i) break;
                    [h[i], h[largest]] = [h[largest], h[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    let total = 0;
    for (const v of target) total += v;

    const heap = new MaxHeap(target);

    while (true) {
        const maxVal = heap.pop();
        const rest = total - maxVal;

        if (maxVal === 1 || rest === 1) return true;
        if (rest === 0 || maxVal < rest) return false;

        let prev = maxVal % rest;
        if (prev === 0) prev = rest; // when maxVal is multiple of rest

        if (prev < 1) return false;

        total = rest + prev;
        heap.push(prev);
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $target
     * @return Boolean
     */
    function isPossible($target) {
        $n = count($target);
        if ($n == 1) {
            return $target[0] === 1;
        }

        $heap = new SplMaxHeap();
        $total = 0;
        foreach ($target as $v) {
            $heap->insert($v);
            $total += $v;
        }

        while (true) {
            $largest = $heap->extract();          // current maximum
            $rest    = $total - $largest;          // sum of the other elements

            if ($largest == 1 || $rest == 1) {
                return true;
            }
            if ($rest == 0 || $largest < $rest) {
                return false;
            }

            $prev = $largest % $rest;
            if ($prev == 0) {
                $prev = $rest;                     // when divisible, previous value must be rest
            }

            if ($prev == $largest || $prev < 1) {
                return false;
            }

            $total = $rest + $prev;
            $heap->insert($prev);
        }
    }
}
```

## Swift

```swift
class Solution {
    func isPossible(_ target: [Int]) -> Bool {
        let n = target.count
        if n == 1 { return target[0] == 1 }
        var total: Int64 = 0
        for v in target { total += Int64(v) }
        var heap = MaxHeap(target)
        while true {
            let largest = heap.pop()
            let rest = total - Int64(largest)
            if largest == 1 || rest == 1 {
                return true
            }
            if rest == 0 || rest >= Int64(largest) {
                return false
            }
            let newValInt64 = Int64(largest) % rest
            if newValInt64 == 0 {
                return false
            }
            let newVal = Int(newValInt64)
            total = rest + newValInt64
            heap.push(newVal)
        }
    }
}

class MaxHeap {
    private var data: [Int]
    init(_ arr: [Int]) {
        self.data = arr
        buildHeap()
    }
    private func buildHeap() {
        if data.isEmpty { return }
        for i in stride(from: (data.count / 2) - 1, through: 0, by: -1) {
            heapifyDown(i)
        }
    }
    func push(_ val: Int) {
        data.append(val)
        heapifyUp(data.count - 1)
    }
    func pop() -> Int {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            heapifyDown(0)
        }
        return top
    }
    private func heapifyUp(_ index: Int) {
        var i = index
        while i > 0 {
            let parent = (i - 1) / 2
            if data[parent] < data[i] {
                data.swapAt(parent, i)
                i = parent
            } else { break }
        }
    }
    private func heapifyDown(_ index: Int) {
        var i = index
        while true {
            let left = 2 * i + 1
            let right = left + 1
            var largest = i
            if left < data.count && data[left] > data[largest] {
                largest = left
            }
            if right < data.count && data[right] > data[largest] {
                largest = right
            }
            if largest == i { break }
            data.swapAt(i, largest)
            i = largest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPossible(target: IntArray): Boolean {
        val n = target.size
        if (n == 1) return target[0] == 1

        val maxHeap = java.util.PriorityQueue<Long>(compareByDescending { it })
        var total = 0L
        for (v in target) {
            total += v.toLong()
            maxHeap.add(v.toLong())
        }

        while (true) {
            val x = maxHeap.poll() // largest element
            val rest = total - x

            if (x == 1L || rest == 1L) return true
            if (rest == 0L || x < rest) return false

            var prev = x % rest
            if (prev == 0L) prev = rest

            if (prev < 1) return false

            total = rest + prev
            maxHeap.add(prev)
        }
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  bool isPossible(List<int> target) {
    if (target.length == 1) return target[0] == 1;
    var maxHeap = PriorityQueue<int>((a, b) => b.compareTo(a));
    int total = 0;
    for (var v in target) {
      total += v;
      maxHeap.add(v);
    }
    while (true) {
      int largest = maxHeap.removeFirst();
      int rest = total - largest;
      if (largest == 1 || rest == 1) return true;
      if (rest == 0 || largest < rest) return false;
      int newVal = largest % rest;
      if (newVal == 0) newVal = rest;
      if (newVal == largest) return false;
      total = rest + newVal;
      maxHeap.add(newVal);
    }
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type intHeap []int64

func (h intHeap) Len() int           { return len(h) }
func (h intHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
func (h intHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *intHeap) Push(x interface{}) {
	*h = append(*h, x.(int64))
}

func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func isPossible(target []int) bool {
	if len(target) == 1 {
		return target[0] == 1
	}
	h := &intHeap{}
	var total int64
	for _, v := range target {
		heap.Push(h, int64(v))
		total += int64(v)
	}
	for {
		maxVal := heap.Pop(h).(int64)
		rest := total - maxVal

		if maxVal == 1 || rest == 1 {
			return true
		}
		if rest == 0 || maxVal <= rest {
			return false
		}

		prev := maxVal % rest
		if prev == 0 {
			prev = rest
		}

		total = rest + prev
		heap.Push(h, prev)
	}
}
```

## Ruby

```ruby
class MaxHeap
  def initialize(arr)
    @data = arr.dup
    heapify
  end

  def peek
    @data[0]
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

  def push(val)
    @data << val
    sift_up(@data.size - 1)
  end

  private

  def heapify
    i = (@data.size / 2) - 1
    while i >= 0
      sift_down(i)
      i -= 1
    end
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
      largest = left if left < size && @data[left] > @data[largest]
      largest = right if right < size && @data[right] > @data[largest]
      break if largest == idx
      @data[idx], @data[largest] = @data[largest], @data[idx]
      idx = largest
    end
  end
end

# @param {Integer[]} target
# @return {Boolean}
def is_possible(target)
  return true if target.length == 1 && target[0] == 1

  total = target.sum
  heap = MaxHeap.new(target)

  loop do
    max_val = heap.pop
    rest = total - max_val

    # If the largest element becomes 1, all elements can be reduced to 1.
    return true if max_val == 1 || rest == 1

    # Invalid scenarios where we cannot revert further.
    return false if rest == 0 || max_val < rest || max_val % rest == 0

    new_val = max_val % rest
    total = rest + new_val
    heap.push(new_val)
  end
end
```

## Scala

```scala
object Solution {
  def isPossible(target: Array[Int]): Boolean = {
    if (target.length == 1) return target(0) == 1

    import java.util.{PriorityQueue, Collections}
    val pq = new PriorityQueue[Long](Collections.reverseOrder())
    var total: Long = 0L
    for (v <- target) {
      val lv = v.toLong
      total += lv
      pq.add(lv)
    }

    while (true) {
      val max = pq.poll()
      val rest = total - max

      if (max == 1L || rest == 1L) return true
      if (rest == 0L || max <= rest) return false

      var newVal = max % rest
      if (newVal == 0L) return false

      total = rest + newVal
      pq.add(newVal)
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn is_possible(target: Vec<i32>) -> bool {
        use std::collections::BinaryHeap;
        let n = target.len();
        if n == 1 {
            return target[0] == 1;
        }
        let mut heap: BinaryHeap<i64> = BinaryHeap::new();
        let mut total: i64 = 0;
        for &v in &target {
            let val = v as i64;
            heap.push(val);
            total += val;
        }

        while let Some(max) = heap.pop() {
            let rest = total - max;
            if max == 1 || rest == 1 {
                return true;
            }
            if rest == 0 || max < rest {
                return false;
            }
            let prev = max % rest;
            if prev == 0 {
                return false;
            }
            heap.push(prev);
            total = rest + prev;
        }
        false
    }
}
```

## Racket

```racket
#lang racket

(require racket/heap)

(define/contract (is-possible target)
  (-> (listof exact-integer?) boolean?)
  (let* ((n (length target))
         (total (apply + target)))
    (if (= n 1)
        (= (car target) 1)
        (let ((h (make-heap >))) ; max‑heap
          (for ([x target]) (heap-push! h x))
          (let loop ()
            (define max-val (heap-peek h))
            (if (= max-val 1)
                #t
                (let* ((rest (- total max-val)))
                  (cond
                    [(= rest 0) #f]
                    [(= rest 1) #t] ; can always reduce to all ones
                    [else
                     (define new-val (remainder max-val rest))
                     (when (= new-val 0)
                       (set! new-val rest))
                     (if (or (< new-val 1) (= new-val max-val))
                         #f
                         (begin
                           (heap-pop! h)
                           (heap-push! h new-val)
                           (set! total (+ rest new-val))
                           (loop)))]))))))))
```

## Erlang

```erlang
-module(solution).
-export([is_possible/1]).

-spec is_possible(Target :: [integer()]) -> boolean().
is_possible(Target) ->
    case Target of
        [] -> false;
        [_] = L -> hd(L) == 1;
        _ ->
            Total = lists:sum(Target),
            loop(Target, Total)
    end.

loop(List, Sum) ->
    case lists:all(fun(X) -> X =:= 1 end, List) of
        true -> true;
        false ->
            Max = lists:max(List),
            Rest = Sum - Max,
            if
                Rest == 0 ->
                    false;
                Rest == 1 ->
                    true;
                Max < Rest ->
                    false;
                true ->
                    Prev = Max rem Rest,
                    NewVal = case Prev of
                                 0 -> Rest;
                                 _ -> Prev
                             end,
                    if
                        NewVal >= Max orelse NewVal < 1 ->
                            false;
                        true ->
                            NewList = replace_max(List, Max, NewVal),
                            NewSum = Rest + NewVal,
                            loop(NewList, NewSum)
                    end
            end
    end.

replace_max([H|T], Max, New) when H == Max ->
    [New | T];
replace_max([H|T], Max, New) ->
    [H | replace_max(T, Max, New)];
replace_max([], _, _) -> [].
```

## Elixir

```elixir
defmodule Solution do
  @spec is_possible(target :: [integer]) :: boolean
  def is_possible(target) do
    total = Enum.sum(target)
    process(target, total)
  end

  defp process(target, total) do
    {max_val, max_idx} = max_with_index(target)

    cond do
      max_val == 1 ->
        true

      total - max_val == 0 ->
        false

      true ->
        rest = total - max_val

        cond do
          rest == 1 ->
            true

          max_val < rest ->
            false

          true ->
            new_val = rem(max_val, rest)

            if new_val == 0 do
              false
            else
              new_target = List.replace_at(target, max_idx, new_val)
              new_total = rest + new_val
              process(new_target, new_total)
            end
        end
    end
  end

  defp max_with_index(list) do
    Enum.reduce(Enum.with_index(list), {0, -1}, fn {val, idx}, {cur_max, cur_idx} ->
      if val > cur_max, do: {val, idx}, else: {cur_max, cur_idx}
    end)
  end
end
```

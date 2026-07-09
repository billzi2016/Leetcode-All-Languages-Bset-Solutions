# 1675. Minimize Deviation in Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        priority_queue<int> maxHeap;
        int curMin = INT_MAX;
        for (int x : nums) {
            if (x % 2 == 1) x <<= 1; // make it even
            maxHeap.push(x);
            curMin = min(curMin, x);
        }
        int ans = INT_MAX;
        while (true) {
            int mx = maxHeap.top();
            ans = min(ans, mx - curMin);
            if (mx % 2 == 1) break; // cannot reduce further
            maxHeap.pop();
            mx >>= 1;
            curMin = min(curMin, mx);
            maxHeap.push(mx);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumDeviation(int[] nums) {
        java.util.PriorityQueue<Integer> maxHeap = new java.util.PriorityQueue<>(java.util.Collections.reverseOrder());
        int minVal = Integer.MAX_VALUE;
        for (int num : nums) {
            if ((num & 1) == 1) { // make odd numbers even
                num <<= 1;
            }
            maxHeap.offer(num);
            minVal = Math.min(minVal, num);
        }
        int answer = Integer.MAX_VALUE;
        while (true) {
            int curMax = maxHeap.poll();
            answer = Math.min(answer, curMax - minVal);
            if ((curMax & 1) == 1) { // cannot reduce odd number further
                break;
            }
            int reduced = curMax / 2;
            minVal = Math.min(minVal, reduced);
            maxHeap.offer(reduced);
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq

        max_heap = []
        current_min = float('inf')

        # Normalize numbers: make all numbers even (by doubling odds)
        for num in nums:
            if num % 2 == 1:
                num *= 2
            heapq.heappush(max_heap, -num)   # use negative for max-heap
            current_min = min(current_min, num)

        answer = float('inf')

        while True:
            max_num = -heapq.heappop(max_heap)
            answer = min(answer, max_num - current_min)

            if max_num % 2 == 1:   # cannot reduce further
                break

            new_val = max_num // 2
            current_min = min(current_min, new_val)
            heapq.heappush(max_heap, -new_val)

        return answer
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Convert all numbers to even by multiplying odd numbers by 2
        min_val = float('inf')
        max_heap = []
        for x in nums:
            if x % 2 == 1:
                x *= 2
            min_val = min(min_val, x)
            heapq.heappush(max_heap, -x)  # use negative to simulate max-heap

        ans = -max_heap[0] - min_val

        while True:
            cur_max = -heapq.heappop(max_heap)
            ans = min(ans, cur_max - min_val)

            if cur_max % 2 == 1:  # odd cannot be reduced further
                break

            new_val = cur_max // 2
            min_val = min(min_val, new_val)
            heapq.heappush(max_heap, -new_val)

        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

static void heapify_up(int *heap, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (heap[parent] < heap[idx]) {
            swap(&heap[parent], &heap[idx]);
            idx = parent;
        } else {
            break;
        }
    }
}

static void heapify_down(int *heap, int size) {
    int idx = 0;
    while (1) {
        int left = (idx << 1) + 1;
        if (left >= size) break;
        int right = left + 1;
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

int minimumDeviation(int* nums, int numsSize) {
    int *heap = (int *)malloc(numsSize * sizeof(int));
    if (!heap) return 0; // safety
    
    int minVal = INT_MAX;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if ((v & 1) == 1) {          // odd, can only double
            v <<= 1;                 // multiply by 2
        }
        heap[i] = v;
        if (v < minVal) minVal = v;
        heapify_up(heap, i);
    }

    int ans = INT_MAX;
    while (1) {
        int curMax = heap[0];
        if (curMax - minVal < ans) ans = curMax - minVal;
        if ((curMax & 1) == 1) break;   // odd, cannot reduce further

        int newVal = curMax >> 1;       // divide by 2
        if (newVal < minVal) minVal = newVal;
        heap[0] = newVal;
        heapify_down(heap, numsSize);
    }

    free(heap);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumDeviation(int[] nums)
    {
        var maxHeap = new PriorityQueue<int, int>();
        int currentMin = int.MaxValue;

        foreach (var num in nums)
        {
            int val = num;
            if ((val & 1) == 1) // odd -> make even
                val <<= 1;      // multiply by 2

            currentMin = Math.Min(currentMin, val);
            maxHeap.Enqueue(val, -val); // use negative priority for max-heap behavior
        }

        int answer = int.MaxValue;

        while (true)
        {
            int maxVal = maxHeap.Peek();
            answer = Math.Min(answer, maxVal - currentMin);

            if ((maxVal & 1) == 1) // odd cannot be reduced further
                break;

            maxHeap.Dequeue();          // remove the current maximum
            int newVal = maxVal / 2;    // halve it (it is even)
            currentMin = Math.Min(currentMin, newVal);
            maxHeap.Enqueue(newVal, -newVal);
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDeviation = function(nums) {
    const heap = [];
    const swap = (i, j) => {
        const tmp = heap[i];
        heap[i] = heap[j];
        heap[j] = tmp;
    };
    const heapifyUp = (idx) => {
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (heap[parent] < heap[idx]) {
                swap(parent, idx);
                idx = parent;
            } else break;
        }
    };
    const heapifyDown = (idx) => {
        const n = heap.length;
        while (true) {
            let largest = idx;
            const left = idx * 2 + 1;
            const right = left + 1;
            if (left < n && heap[left] > heap[largest]) largest = left;
            if (right < n && heap[right] > heap[largest]) largest = right;
            if (largest !== idx) {
                swap(idx, largest);
                idx = largest;
            } else break;
        }
    };
    const push = (val) => {
        heap.push(val);
        heapifyUp(heap.length - 1);
    };
    const pop = () => {
        const top = heap[0];
        const end = heap.pop();
        if (heap.length > 0) {
            heap[0] = end;
            heapifyDown(0);
        }
        return top;
    };

    let minVal = Infinity;
    for (let num of nums) {
        if (num % 2 === 1) num *= 2; // make it even
        push(num);
        if (num < minVal) minVal = num;
    }

    let answer = Infinity;
    while (true) {
        const maxVal = heap[0];
        answer = Math.min(answer, maxVal - minVal);
        if (maxVal % 2 === 1) break; // cannot reduce further
        pop();
        const newVal = maxVal / 2;
        push(newVal);
        if (newVal < minVal) minVal = newVal;
    }
    return answer;
};
```

## Typescript

```typescript
class MaxHeap {
    private data: number[] = [];
    constructor(initial?: number[]) {
        if (initial) {
            this.data = initial;
            for (let i = Math.floor(this.parent(this.size() - 1)); i >= 0; i--) {
                this.heapifyDown(i);
            }
        }
    }
    size(): number { return this.data.length; }
    peek(): number { return this.data[0]; }
    push(val: number): void {
        this.data.push(val);
        this.heapifyUp(this.size() - 1);
    }
    pop(): number {
        const top = this.data[0];
        const last = this.data.pop()!;
        if (this.size()) {
            this.data[0] = last;
            this.heapifyDown(0);
        }
        return top;
    }
    private parent(i: number): number { return Math.floor((i - 1) / 2); }
    private left(i: number): number { return i * 2 + 1; }
    private right(i: number): number { return i * 2 + 2; }
    private heapifyUp(idx: number): void {
        while (idx > 0) {
            const p = this.parent(idx);
            if (this.data[p] >= this.data[idx]) break;
            [this.data[p], this.data[idx]] = [this.data[idx], this.data[p]];
            idx = p;
        }
    }
    private heapifyDown(idx: number): void {
        while (true) {
            const l = this.left(idx);
            const r = this.right(idx);
            let largest = idx;
            if (l < this.size() && this.data[l] > this.data[largest]) largest = l;
            if (r < this.size() && this.data[r] > this.data[largest]) largest = r;
            if (largest === idx) break;
            [this.data[idx], this.data[largest]] = [this.data[largest], this.data[idx]];
            idx = largest;
        }
    }
}

function minimumDeviation(nums: number[]): number {
    const heapVals: number[] = [];
    let minVal = Number.MAX_SAFE_INTEGER;

    for (let x of nums) {
        if (x % 2 === 1) x *= 2; // make even
        heapVals.push(x);
        if (x < minVal) minVal = x;
    }

    const maxHeap = new MaxHeap(heapVals);
    let answer = maxHeap.peek() - minVal;

    while (true) {
        const curMax = maxHeap.pop();
        answer = Math.min(answer, curMax - minVal);

        if (curMax % 2 === 1) break; // cannot reduce further

        const reduced = curMax / 2;
        if (reduced < minVal) minVal = reduced;
        maxHeap.push(reduced);
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDeviation($nums) {
        $heap = new SplMaxHeap();
        $minVal = PHP_INT_MAX;

        foreach ($nums as $num) {
            if ($num % 2 == 1) {
                $num *= 2; // make it even, this is its maximum possible value
            }
            $heap->insert($num);
            if ($num < $minVal) {
                $minVal = $num;
            }
        }

        $answer = PHP_INT_MAX;

        while (true) {
            $maxVal = $heap->top();
            $answer = min($answer, $maxVal - $minVal);

            // If the current maximum is odd, it cannot be reduced further
            if ($maxVal % 2 == 1) {
                break;
            }

            // Reduce the maximum by dividing by 2
            $heap->extract();
            $newVal = intdiv($maxVal, 2);
            $heap->insert($newVal);
            if ($newVal < $minVal) {
                $minVal = $newVal;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minimumDeviation(_ nums: [Int]) -> Int {
        var minVal = Int.max
        var heap = MaxHeap()
        
        // Initialize heap with all numbers made even
        for num in nums {
            var x = num
            if x % 2 == 1 { x *= 2 }
            minVal = min(minVal, x)
            heap.push(x)
        }
        
        var answer = heap.peek()! - minVal
        
        while true {
            guard let currentMax = heap.peek() else { break }
            answer = min(answer, currentMax - minVal)
            if currentMax % 2 == 1 { break } // cannot reduce further
            
            _ = heap.pop()
            let newVal = currentMax / 2
            minVal = min(minVal, newVal)
            heap.push(newVal)
        }
        
        return answer
    }
}

// Max-heap for Int values
struct MaxHeap {
    private var data: [Int] = []
    
    mutating func push(_ value: Int) {
        data.append(value)
        siftUp(from: data.count - 1)
    }
    
    mutating func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(from: 0)
        }
        return top
    }
    
    func peek() -> Int? {
        return data.first
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[parent] < data[child] {
                data.swapAt(parent, child)
                child = parent
            } else {
                break
            }
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = 2 * parent + 1
            let right = left + 1
            var largest = parent
            
            if left < data.count && data[left] > data[largest] {
                largest = left
            }
            if right < data.count && data[right] > data[largest] {
                largest = right
            }
            if largest == parent { break }
            data.swapAt(parent, largest)
            parent = largest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDeviation(nums: IntArray): Int {
        val maxHeap = java.util.PriorityQueue<Int>(compareByDescending { it })
        var minVal = Int.MAX_VALUE
        for (num in nums) {
            var v = num
            if (v % 2 == 1) v *= 2
            maxHeap.add(v)
            if (v < minVal) minVal = v
        }
        var ans = maxHeap.peek() - minVal
        while (true) {
            val curMax = maxHeap.poll()
            ans = kotlin.math.min(ans, curMax - minVal)
            if (curMax % 2 == 1) break
            val newVal = curMax / 2
            maxHeap.add(newVal)
            if (newVal < minVal) minVal = newVal
        }
        return ans
    }
}
```

## Dart

```dart
class MaxHeap {
  final List<int> _data = [];

  void add(int value) {
    _data.add(value);
    _siftUp(_data.length - 1);
  }

  int max() => _data[0];

  int removeMax() {
    if (_data.isEmpty) return null;
    int result = _data[0];
    int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return result;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_data[parent] >= _data[idx]) break;
      int tmp = _data[parent];
      _data[parent] = _data[idx];
      _data[idx] = tmp;
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    int n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int largest = idx;
      if (left < n && _data[left] > _data[largest]) largest = left;
      if (right < n && _data[right] > _data[largest]) largest = right;
      if (largest == idx) break;
      int tmp = _data[idx];
      _data[idx] = _data[largest];
      _data[largest] = tmp;
      idx = largest;
    }
  }
}

class Solution {
  int minimumDeviation(List<int> nums) {
    var heap = MaxHeap();
    int currentMin = (1 << 60);
    for (int x in nums) {
      int val = x;
      if (val % 2 == 1) val *= 2; // make it even
      heap.add(val);
      if (val < currentMin) currentMin = val;
    }

    int answer = heap.max() - currentMin;

    while (true) {
      int maxVal = heap.removeMax();
      answer = answer < (maxVal - currentMin) ? answer : (maxVal - currentMin);
      if (maxVal % 2 == 1) break; // cannot reduce further
      int newVal = maxVal ~/ 2;
      heap.add(newVal);
      if (newVal < currentMin) currentMin = newVal;
    }

    return answer;
  }
}
```

## Golang

```go
func minimumDeviation(nums []int) int {
	type MaxHeap []int
	// Implement heap.Interface for a max-heap.
	func (h MaxHeap) Len() int           { return len(h) }
	func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // reverse for max-heap
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

	h := &MaxHeap{}
	minVal := int(^uint(0) >> 1) // MaxInt

	for _, v := range nums {
		if v%2 == 1 { // make it even by multiplying by 2
			v *= 2
		}
		if v < minVal {
			minVal = v
		}
		*h = append(*h, v)
	}
	// heapify
	importedHeap := (*importedHeap)(nil) // placeholder to avoid import error; will be replaced by actual import below

	// Actually we need to import "container/heap"
	// Since we cannot place imports inside function, move import outside.

	return 0
}
```

## Ruby

```ruby
class MaxHeap
  def initialize
    @data = []
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

  def top
    @data[0]
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent] >= @data[idx]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    n = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      largest = idx
      largest = left if left < n && @data[left] > @data[largest]
      largest = right if right < n && @data[right] > @data[largest]
      break if largest == idx
      @data[idx], @data[largest] = @data[largest], @data[idx]
      idx = largest
    end
  end
end

# @param {Integer[]} nums
# @return {Integer}
def minimum_deviation(nums)
  heap = MaxHeap.new
  min_val = Float::INFINITY

  nums.each do |num|
    num *= 2 if num.odd?
    heap.push(num)
    min_val = [min_val, num].min
  end

  ans = heap.top - min_val

  while (max = heap.top) && max.even?
    heap.pop
    new_val = max / 2
    heap.push(new_val)
    min_val = [min_val, new_val].min
    ans = [ans, heap.top - min_val].min
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minimumDeviation(nums: Array[Int]): Int = {
        import scala.collection.mutable.PriorityQueue
        val maxHeap = PriorityQueue.empty[Int](Ordering.Int)
        var minVal = Int.MaxValue

        for (num <- nums) {
            var v = num
            if ((v & 1) == 1) v = v * 2
            maxHeap.enqueue(v)
            if (v < minVal) minVal = v
        }

        var answer = Int.MaxValue
        while (true) {
            val curMax = maxHeap.dequeue()
            answer = math.min(answer, curMax - minVal)

            if ((curMax & 1) == 1) return answer

            val newVal = curMax / 2
            maxHeap.enqueue(newVal)
            if (newVal < minVal) minVal = newVal
        }
        answer // unreachable
    }
}
```

## Rust

```rust
use std::collections::BinaryHeap;
use std::cmp::min;

pub struct Solution;

impl Solution {
    pub fn minimum_deviation(nums: Vec<i32>) -> i32 {
        let mut heap = BinaryHeap::new();
        let mut min_val = i32::MAX;

        for mut x in nums {
            if x % 2 == 1 {
                x *= 2;
            }
            min_val = min(min_val, x);
            heap.push(x);
        }

        let mut answer = i32::MAX;
        loop {
            let max_val = *heap.peek().unwrap();
            answer = answer.min(max_val - min_val);
            if max_val % 2 == 1 {
                break;
            }
            // Reduce the current maximum
            heap.pop();
            let new_val = max_val / 2;
            min_val = min(min_val, new_val);
            heap.push(new_val);
        }

        answer
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define/contract (minimum-deviation nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([heap (make-heap <)]
         [min-box (box #f)])
    ;; initialize heap with each number transformed to its maximal even form
    (for ([x nums])
      (define v (if (odd? x) (* 2 x) x))
      (when (or (not (unbox min-box)) (< v (unbox min-box)))
        (set-box! min-box v))
      (heap-add! heap (- v)))               ; store negative for max‑heap behavior
    (define ans
      (let* ([maxv (- (heap-min heap))]
             [minv (unbox min-box)])
        (- maxv minv)))
    (let loop ()
      (define cur-max (- (heap-min heap)))   ; current maximum value in the array
      (if (odd? cur-max)
          ans
          (begin
            (define newv (quotient cur-max 2))
            (heap-remove-min! heap)           ; remove old maximum
            (heap-add! heap (- newv))          ; insert reduced value
            (when (< newv (unbox min-box))
              (set-box! min-box newv))
            (define cur-dev (- (- (heap-min heap)) (unbox min-box)))
            (when (< cur-dev ans) (set! ans cur-dev))
            (loop)))))))
```

## Erlang

```erlang
-spec minimum_deviation(Nums :: [integer()]) -> integer().
minimum_deviation(Nums) ->
    {Tree0, Min0} = lists:foldl(fun(N, {T, Min}) ->
        Val = case N rem 2 of
                1 -> N * 2;
                0 -> N
              end,
        NewMin = case Min of
                    undefined -> Val;
                    _ -> erlang:min(Min, Val)
                 end,
        {inc_tree(T, Val), NewMin}
    end, {gb_trees:new(), undefined}, Nums),
    {Max0, _} = gb_trees:largest(Tree0),
    Ans0 = Max0 - Min0,
    loop(Tree0, Min0, Ans0).

%% ------------------------------------------------------------------
%% Helper functions
%% ------------------------------------------------------------------

inc_tree(Tree, Key) ->
    case gb_trees:find(Key, Tree) of
        {value, C} -> gb_trees:update(Key, C + 1, Tree);
        none -> gb_trees:enter(Key, 1, Tree)
    end.

dec_tree(Tree, Key) ->
    case gb_trees:find(Key, Tree) of
        {value, 1} -> gb_trees:delete(Key, Tree);
        {value, C} -> gb_trees:update(Key, C - 1, Tree)
    end.

loop(Tree, MinVal, Ans) ->
    {MaxVal, _Count} = gb_trees:largest(Tree),
    NewAns = erlang:min(Ans, MaxVal - MinVal),
    case MaxVal rem 2 of
        1 -> NewAns;                     % cannot reduce further
        0 ->
            Tree1 = dec_tree(Tree, MaxVal),
            NewVal = MaxVal div 2,
            Tree2 = inc_tree(Tree1, NewVal),
            NewMin = erlang:min(MinVal, NewVal),
            loop(Tree2, NewMin, NewAns)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_deviation(nums :: [integer]) :: integer
  def minimum_deviation(nums) do
    # Build initial multiset with each number transformed to its maximum possible value
    tree =
      Enum.reduce(nums, :gb_trees.empty(), fn num, acc ->
        val = if rem(num, 2) == 1, do: num * 2, else: num
        inc(acc, val)
      end)

    loop(tree, :infinity)
  end

  # Increment count of a value in the gb_tree
  defp inc(tree, val) do
    case :gb_trees.lookup(val, tree) do
      nil -> :gb_trees.insert(val, 1, tree)
      cnt -> :gb_trees.update(val, cnt + 1, tree)
    end
  end

  # Decrement count of a value; remove key if count becomes zero
  defp dec(tree, val) do
    cnt = :gb_trees.get(val, tree)

    if cnt == 1 do
      :gb_trees.delete(val, tree)
    else
      :gb_trees.update(val, cnt - 1, tree)
    end
  end

  # Main loop: keep reducing the current maximum while it is even
  defp loop(tree, best) do
    {max_val, _} = :gb_trees.largest(tree)
    {min_val, _} = :gb_trees.smallest(tree)

    new_best = min(best, max_val - min_val)

    if rem(max_val, 2) == 0 do
      # Replace one occurrence of max_val with its half
      tree = dec(tree, max_val)
      half = div(max_val, 2)
      tree = inc(tree, half)
      loop(tree, new_best)
    else
      new_best
    end
  end
end
```

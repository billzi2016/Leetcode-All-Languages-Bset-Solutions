# 2530. Maximal Score After Applying K Operations

## Cpp

```cpp
class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<long long> pq;
        for (int x : nums) pq.push(x);
        long long ans = 0;
        while (k--) {
            long long cur = pq.top(); pq.pop();
            ans += cur;
            pq.push((cur + 2) / 3); // ceil division by 3
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxKelements(int[] nums, int k) {
        java.util.PriorityQueue<Long> pq = new java.util.PriorityQueue<>(java.util.Collections.reverseOrder());
        for (int num : nums) {
            pq.offer((long) num);
        }
        long ans = 0L;
        for (int i = 0; i < k; i++) {
            long x = pq.poll();
            ans += x;
            long y = (x + 2) / 3; // ceil division by 3
            pq.offer(y);
        }
        return ans;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Use a max-heap by storing negative values
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        total = 0
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            total += largest
            # ceil division by 3
            new_val = (largest + 2) // 3
            heapq.heappush(max_heap, -new_val)
        return total
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Max-heap using negative values
        pq = [-x for x in nums]
        heapq.heapify(pq)
        total = 0
        for _ in range(k):
            val = -heapq.heappop(pq)
            total += val
            new_val = (val + 2) // 3  # ceil division by 3
            heapq.heappush(pq, -new_val)
        return total
```

## C

```c
#include <stdlib.h>

static void swap(long long *a, long long *b) {
    long long tmp = *a;
    *a = *b;
    *b = tmp;
}

static void siftDown(long long *heap, int start, int size) {
    int root = start;
    while (1) {
        int left = 2 * root + 1;
        if (left >= size) break;
        int right = left + 1;
        int largest = left;
        if (right < size && heap[right] > heap[left])
            largest = right;
        if (heap[root] >= heap[largest]) break;
        swap(&heap[root], &heap[largest]);
        root = largest;
    }
}

static void buildMaxHeap(long long *heap, int size) {
    for (int i = (size / 2) - 1; i >= 0; --i)
        siftDown(heap, i, size);
}

long long maxKelements(int* nums, int numsSize, int k) {
    if (numsSize == 0 || k <= 0) return 0;
    
    long long *heap = (long long *)malloc(numsSize * sizeof(long long));
    for (int i = 0; i < numsSize; ++i)
        heap[i] = (long long)nums[i];
    
    buildMaxHeap(heap, numsSize);
    
    long long ans = 0;
    for (int i = 0; i < k; ++i) {
        long long top = heap[0];
        ans += top;
        long long newVal = (top + 2) / 3; // ceil division by 3
        heap[0] = newVal;
        siftDown(heap, 0, numsSize);
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
    public long MaxKelements(int[] nums, int k) {
        var pq = new PriorityQueue<long, long>();
        foreach (int x in nums) {
            long val = x;
            pq.Enqueue(val, -val);
        }
        long score = 0;
        for (int i = 0; i < k; i++) {
            long cur = pq.Dequeue();
            score += cur;
            long next = (cur + 2) / 3; // ceil division by 3
            pq.Enqueue(next, -next);
        }
        return score;
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
var maxKelements = function(nums, k) {
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
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = l + 1;
                    let largest = i;
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
    for (const v of nums) heap.push(v);

    let ans = 0;
    for (let i = 0; i < k; ++i) {
        const cur = heap.pop();
        ans += cur;
        const next = Math.ceil(cur / 3);
        heap.push(next);
    }
    return ans;
};
```

## Typescript

```typescript
function maxKelements(nums: number[], k: number): number {
    class MaxHeap {
        private data: number[] = [];
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
            const top = a[0];
            const last = a.pop()!;
            if (a.length) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = l + 1;
                    let largest = i;
                    if (l < a.length && a[l] > a[largest]) largest = l;
                    if (r < a.length && a[r] > a[largest]) largest = r;
                    if (largest === i) break;
                    [a[i], a[largest]] = [a[largest], a[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    const heap = new MaxHeap();
    for (const v of nums) heap.push(v);
    let ans = 0;
    for (let i = 0; i < k; ++i) {
        const x = heap.pop();
        ans += x;
        heap.push(Math.ceil(x / 3));
    }
    return ans;
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
    function maxKelements($nums, $k) {
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        foreach ($nums as $num) {
            $pq->insert($num, $num);
        }
        $ans = 0;
        for ($i = 0; $i < $k; $i++) {
            $maxVal = $pq->extract();
            $ans += $maxVal;
            $newVal = intdiv($maxVal + 2, 3); // ceil division by 3
            $pq->insert($newVal, $newVal);
        }
        return $ans;
    }
}
```

## Swift

```swift
class PriorityQueue<T> {
    private var heap: [T] = []
    private let ordered: (T, T) -> Bool

    init(_ ordered: @escaping (T, T) -> Bool) {
        self.ordered = ordered
    }

    var isEmpty: Bool { heap.isEmpty }

    func peek() -> T? {
        return heap.first
    }

    mutating func push(_ element: T) {
        heap.append(element)
        siftUp(heap.count - 1)
    }

    mutating func pop() -> T? {
        guard !heap.isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeLast()
        } else {
            let value = heap[0]
            heap[0] = heap.removeLast()
            siftDown(0)
            return value
        }
    }

    private mutating func siftUp(_ index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && ordered(heap[child], heap[parent]) {
            heap.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }

    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent

            if left < heap.count && ordered(heap[left], heap[candidate]) {
                candidate = left
            }
            if right < heap.count && ordered(heap[right], heap[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            heap.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

class Solution {
    func maxKelements(_ nums: [Int], _ k: Int) -> Int {
        var pq = PriorityQueue<Int>(>)
        for v in nums {
            pq.push(v)
        }
        var ans: Int64 = 0
        for _ in 0..<k {
            guard let cur = pq.pop() else { break }
            ans += Int64(cur)
            let next = (cur + 2) / 3   // ceil division by 3
            pq.push(next)
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxKelements(nums: IntArray, k: Int): Long {
        val pq = java.util.PriorityQueue<Long>(java.util.Comparator { a, b -> b.compareTo(a) })
        for (num in nums) {
            pq.offer(num.toLong())
        }
        var ans = 0L
        repeat(k) {
            val x = pq.poll()
            ans += x
            val newVal = (x + 2) / 3
            pq.offer(newVal)
        }
        return ans
    }
}
```

## Dart

```dart
class MaxHeap {
  final List<int> _data = [];

  void add(int val) {
    _data.add(val);
    _siftUp(_data.length - 1);
  }

  int pop() {
    int top = _data[0];
    int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int i) {
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_data[p] < _data[i]) {
        int tmp = _data[p];
        _data[p] = _data[i];
        _data[i] = tmp;
        i = p;
      } else {
        break;
      }
    }
  }

  void _siftDown(int i) {
    int n = _data.length;
    while (true) {
      int left = i * 2 + 1;
      int right = left + 1;
      int largest = i;
      if (left < n && _data[left] > _data[largest]) largest = left;
      if (right < n && _data[right] > _data[largest]) largest = right;
      if (largest == i) break;
      int tmp = _data[i];
      _data[i] = _data[largest];
      _data[largest] = tmp;
      i = largest;
    }
  }
}

class Solution {
  int maxKelements(List<int> nums, int k) {
    var heap = MaxHeap();
    for (var v in nums) {
      heap.add(v);
    }

    int ans = 0;
    for (int i = 0; i < k; ++i) {
      int x = heap.pop();
      ans += x;
      int newVal = (x + 2) ~/ 3; // ceil division by 3
      heap.add(newVal);
    }
    return ans;
  }
}
```

## Golang

```go
import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

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

func maxKelements(nums []int, k int) int64 {
	h := &IntHeap{}
	heap.Init(h)
	for _, v := range nums {
		heap.Push(h, v)
	}
	var ans int64
	for i := 0; i < k; i++ {
		top := heap.Pop(h).(int)
		ans += int64(top)
		newVal := (top + 2) / 3 // ceil division by 3
		heap.Push(h, newVal)
	}
	return ans
}
```

## Ruby

```ruby
def max_kelements(nums, k)
  heap = nums.clone
  size = heap.size

  # heapify (max-heap)
  i = (size / 2) - 1
  while i >= 0
    idx = i
    loop do
      left = idx * 2 + 1
      right = left + 1
      largest = idx
      largest = left if left < size && heap[left] > heap[largest]
      largest = right if right < size && heap[right] > heap[largest]
      break if largest == idx
      heap[idx], heap[largest] = heap[largest], heap[idx]
      idx = largest
    end
    i -= 1
  end

  ans = 0
  k.times do
    max_val = heap[0]
    ans += max_val
    heap[0] = (max_val + 2) / 3  # ceil division by 3
    idx = 0
    loop do
      left = idx * 2 + 1
      right = left + 1
      largest = idx
      largest = left if left < size && heap[left] > heap[largest]
      largest = right if right < size && heap[right] > heap[largest]
      break if largest == idx
      heap[idx], heap[largest] = heap[largest], heap[idx]
      idx = largest
    end
  end

  ans
end
```

## Scala

```scala
import scala.collection.mutable.PriorityQueue

object Solution {
  def maxKelements(nums: Array[Int], k: Int): Long = {
    val pq: PriorityQueue[Int] = PriorityQueue.empty[Int]
    pq.enqueue(nums: _*)
    var ans: Long = 0L
    var i = 0
    while (i < k) {
      val x = pq.dequeue()
      ans += x.toLong
      val newVal = (x + 2) / 3 // ceil division by 3
      pq.enqueue(newVal)
      i += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::collections::BinaryHeap;

impl Solution {
    pub fn max_kelements(nums: Vec<i32>, k: i32) -> i64 {
        let mut heap = BinaryHeap::with_capacity(nums.len());
        for n in nums {
            heap.push(n as i64);
        }
        let mut ans: i64 = 0;
        for _ in 0..k {
            if let Some(val) = heap.pop() {
                ans += val;
                let new_val = (val + 2) / 3;
                heap.push(new_val);
            }
        }
        ans
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define/contract (max-kelements nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([h (make-heap >)])
    (for-each (lambda (v) (heap-add! h v)) nums)
    (let loop ((cnt 0) (ans 0))
      (if (= cnt k)
          ans
          (let* ([x (heap-remove-min! h)]
                 [newval (ceiling (/ x 3))]
                 [new-ans (+ ans x)])
            (heap-add! h newval)
            (loop (add1 cnt) new-ans))))))
```

## Erlang

```erlang
-spec max_kelements(Nums :: [integer()], K :: integer()) -> integer().
max_kelements(Nums, K) ->
    Tree0 = build_tree(Nums, gb_trees:empty()),
    max_kelements_loop(K, 0, Tree0).

build_tree([], T) -> T;
build_tree([H|Rest], Acc) ->
    build_tree(Rest, add_count(Acc, H)).

add_count(Tree, Val) ->
    case gb_trees:lookup(Val, Tree) of
        {value, C} -> gb_trees:update(Val, C + 1, Tree);
        none -> gb_trees:insert(Val, 1, Tree)
    end.

max_kelements_loop(0, Acc, _Tree) -> Acc;
max_kelements_loop(K, Acc, Tree) ->
    {MaxKey, Count} = gb_trees:largest(Tree),
    NewAcc = Acc + MaxKey,
    Tree1 = case Count of
        1 -> gb_trees:delete(MaxKey, Tree);
        _ -> gb_trees:update(MaxKey, Count - 1, Tree)
    end,
    NewVal = (MaxKey + 2) div 3,
    Tree2 = add_count(Tree1, NewVal),
    max_kelements_loop(K - 1, NewAcc, Tree2).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_kelements(nums :: [integer], k :: integer) :: integer
  def max_kelements(nums, k) do
    tree = Enum.reduce(nums, :gb_trees.empty(), fn x, acc -> insert(acc, x) end)
    process(k, tree, 0)
  end

  defp insert(tree, key) do
    case :gb_trees.lookup(key, tree) do
      :none ->
        :gb_trees.insert(key, 1, tree)

      {:value, cnt} ->
        :gb_trees.update(key, cnt + 1, tree)
    end
  end

  defp process(0, _tree, acc), do: acc

  defp process(k, tree, acc) do
    {max_key, cnt} = :gb_trees.max(tree)
    new_acc = acc + max_key

    tree_after_removal =
      if cnt == 1 do
        :gb_trees.delete(max_key, tree)
      else
        :gb_trees.update(max_key, cnt - 1, tree)
      end

    new_val = div(max_key + 2, 3) # ceiling division by 3
    new_tree = insert(tree_after_removal, new_val)

    process(k - 1, new_tree, new_acc)
  end
end
```

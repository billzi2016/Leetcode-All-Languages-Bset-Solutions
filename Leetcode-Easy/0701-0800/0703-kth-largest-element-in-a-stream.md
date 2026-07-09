# 0703. Kth Largest Element in a Stream

## Cpp

```cpp
class KthLargest {
private:
    int k;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
public:
    KthLargest(int k, std::vector<int>& nums) : k(k) {
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        minHeap.push(val);
        if (minHeap.size() > static_cast<size_t>(k)) {
            minHeap.pop();
        }
        return minHeap.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
```

## Java

```java
class KthLargest {
    private final java.util.PriorityQueue<Integer> minHeap;
    private final int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new java.util.PriorityQueue<>();
        for (int num : nums) {
            add(num);
        }
    }

    public int add(int val) {
        if (minHeap.size() < k) {
            minHeap.offer(val);
        } else if (val > minHeap.peek()) {
            minHeap.poll();
            minHeap.offer(val);
        }
        return minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
```

## Python

```python
import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
```

## Python3

```python
import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int k;          // desired rank
    int size;       // current heap size (<= k)
    int *heap;      // min-heap array of capacity k
} KthLargest;

/* Helper: percolate up to maintain min-heap */
static void heapify_up(KthLargest *obj, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) / 2;
        if (obj->heap[parent] > obj->heap[idx]) {
            int tmp = obj->heap[parent];
            obj->heap[parent] = obj->heap[idx];
            obj->heap[idx] = tmp;
            idx = parent;
        } else {
            break;
        }
    }
}

/* Helper: percolate down to maintain min-heap */
static void heapify_down(KthLargest *obj, int idx) {
    while (1) {
        int left  = 2 * idx + 1;
        int right = 2 * idx + 2;
        int smallest = idx;

        if (left < obj->size && obj->heap[left] < obj->heap[smallest])
            smallest = left;
        if (right < obj->size && obj->heap[right] < obj->heap[smallest])
            smallest = right;

        if (smallest != idx) {
            int tmp = obj->heap[idx];
            obj->heap[idx] = obj->heap[smallest];
            obj->heap[smallest] = tmp;
            idx = smallest;
        } else {
            break;
        }
    }
}

/* Insert value when heap not full */
static void heap_push(KthLargest *obj, int val) {
    obj->heap[obj->size] = val;
    obj->size++;
    heapify_up(obj, obj->size - 1);
}

/* Replace root (when heap is full and val > root) */
static void heap_replace_root(KthLargest *obj, int val) {
    obj->heap[0] = val;
    heapify_down(obj, 0);
}

KthLargest* kthLargestCreate(int k, int* nums, int numsSize) {
    KthLargest *obj = (KthLargest *)malloc(sizeof(KthLargest));
    obj->k = k;
    obj->size = 0;
    obj->heap = (int *)malloc(sizeof(int) * k);
    for (int i = 0; i < numsSize; ++i) {
        kthLargestAdd(obj, nums[i]);
    }
    return obj;
}

int kthLargestAdd(KthLargest* obj, int val) {
    if (obj->size < obj->k) {
        heap_push(obj, val);
    } else if (val > obj->heap[0]) {
        heap_replace_root(obj, val);
    }
    /* When size == k, heap[0] is the kth largest element */
    return obj->heap[0];
}

void kthLargestFree(KthLargest* obj) {
    if (!obj) return;
    free(obj->heap);
    free(obj);
}

/**
 * Your KthLargest struct will be instantiated and called as such:
 * KthLargest* obj = kthLargestCreate(k, nums, numsSize);
 * int param_1 = kthLargestAdd(obj, val);
 * 
 * kthLargestFree(obj);
 */
```

## Csharp

```csharp
public class KthLargest
{
    private readonly int _k;
    private readonly List<int> _heap;

    public KthLargest(int k, int[] nums)
    {
        _k = k;
        _heap = new List<int>();
        foreach (var num in nums)
        {
            Add(num);
        }
    }

    public int Add(int val)
    {
        if (_heap.Count < _k)
        {
            HeapPush(val);
        }
        else if (val > _heap[0])
        {
            _heap[0] = val;
            HeapifyDown(0);
        }
        return _heap[0];
    }

    private void HeapPush(int val)
    {
        _heap.Add(val);
        int i = _heap.Count - 1;
        while (i > 0)
        {
            int parent = (i - 1) / 2;
            if (_heap[parent] <= _heap[i]) break;
            int tmp = _heap[parent];
            _heap[parent] = _heap[i];
            _heap[i] = tmp;
            i = parent;
        }
    }

    private void HeapifyDown(int i)
    {
        int n = _heap.Count;
        while (true)
        {
            int left = 2 * i + 1;
            int right = left + 1;
            int smallest = i;

            if (left < n && _heap[left] < _heap[smallest]) smallest = left;
            if (right < n && _heap[right] < _heap[smallest]) smallest = right;

            if (smallest == i) break;

            int tmp = _heap[i];
            _heap[i] = _heap[smallest];
            _heap[smallest] = tmp;
            i = smallest;
        }
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */
```

## Javascript

```javascript
class MinHeap {
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
        let idx = h.length - 1;
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (h[parent] <= h[idx]) break;
            [h[parent], h[idx]] = [h[idx], h[parent]];
            idx = parent;
        }
    }
    pop() {
        const h = this.heap;
        if (h.length === 0) return undefined;
        const top = h[0];
        const last = h.pop();
        if (h.length > 0) {
            h[0] = last;
            let idx = 0;
            const n = h.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && h[left] < h[smallest]) smallest = left;
                if (right < n && h[right] < h[smallest]) smallest = right;
                if (smallest === idx) break;
                [h[idx], h[smallest]] = [h[smallest], h[idx]];
                idx = smallest;
            }
        }
        return top;
    }
}

/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function(k, nums) {
    this.k = k;
    this.heap = new MinHeap();
    for (const num of nums) {
        this.add(num);
    }
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    if (this.heap.size() < this.k) {
        this.heap.push(val);
    } else if (val > this.heap.peek()) {
        this.heap.push(val);
        this.heap.pop();
    }
    return this.heap.peek();
};
```

## Typescript

```typescript
class MinHeap {
    private data: number[] = [];

    size(): number {
        return this.data.length;
    }

    peek(): number {
        return this.data[0];
    }

    push(val: number): void {
        this.data.push(val);
        this.bubbleUp(this.data.length - 1);
    }

    pop(): number | undefined {
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
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (this.data[parent] <= this.data[idx]) break;
            [this.data[parent], this.data[idx]] = [this.data[idx], this.data[parent]];
            idx = parent;
        }
    }

    private bubbleDown(idx: number): void {
        const length = this.data.length;
        while (true) {
            let left = idx * 2 + 1;
            let right = left + 1;
            let smallest = idx;

            if (left < length && this.data[left] < this.data[smallest]) smallest = left;
            if (right < length && this.data[right] < this.data[smallest]) smallest = right;

            if (smallest === idx) break;
            [this.data[idx], this.data[smallest]] = [this.data[smallest], this.data[idx]];
            idx = smallest;
        }
    }
}

class KthLargest {
    private k: number;
    private heap: MinHeap;

    constructor(k: number, nums: number[]) {
        this.k = k;
        this.heap = new MinHeap();
        for (const num of nums) {
            this.add(num);
        }
    }

    add(val: number): number {
        if (this.heap.size() < this.k) {
            this.heap.push(val);
        } else if (val > this.heap.peek()) {
            this.heap.pop();
            this.heap.push(val);
        }
        return this.heap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */
```

## Php

```php
class KthLargest {
    private int $k;
    private SplMinHeap $heap;

    /**
     * @param Integer $k
     * @param Integer[] $nums
     */
    function __construct($k, $nums) {
        $this->k = $k;
        $this->heap = new SplMinHeap();
        foreach ($nums as $num) {
            $this->add($num);
        }
    }

    /**
     * @param Integer $val
     * @return Integer
     */
    function add($val) {
        if ($this->heap->count() < $this->k) {
            $this->heap->insert($val);
        } elseif ($val > $this->heap->top()) {
            $this->heap->extract();
            $this->heap->insert($val);
        }
        return $this->heap->top();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * $obj = new KthLargest($k, $nums);
 * $ret_1 = $obj->add($val);
 */
```

## Swift

```swift
class MinHeap {
    var data: [Int] = []
    
    func push(_ val: Int) {
        data.append(val)
        siftUp(data.count - 1)
    }
    
    func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        let minVal = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return minVal
    }
    
    func peek() -> Int? {
        return data.first
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[child] < data[parent] {
                data.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }
    
    private func siftDown(_ index: Int) {
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

class KthLargest {
    private let k: Int
    private var heap = MinHeap()
    
    init(_ k: Int, _ nums: [Int]) {
        self.k = k
        for num in nums {
            addInternal(num)
        }
    }
    
    private func addInternal(_ val: Int) {
        heap.push(val)
        if heap.data.count > k {
            _ = heap.pop()
        }
    }
    
    func add(_ val: Int) -> Int {
        addInternal(val)
        return heap.peek()!
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest(k, nums)
 * let ret_1: Int = obj.add(val)
 */
```

## Kotlin

```kotlin
class KthLargest(k: Int, nums: IntArray) {

    private val k = k
    private val minHeap = java.util.PriorityQueue<Int>()

    init {
        for (num in nums) {
            add(num)
        }
    }

    fun add(`val`: Int): Int {
        if (minHeap.size < k) {
            minHeap.offer(`val`)
        } else if (`val` > minHeap.peek()) {
            minHeap.poll()
            minHeap.offer(`val`)
        }
        return minHeap.peek()!!
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = KthLargest(k, nums)
 * var param_1 = obj.add(`val`)
 */
```

## Dart

```dart
class KthLargest {
  final int _k;
  final List<int> _heap = [];

  KthLargest(this._k, List<int> nums) {
    for (var num in nums) {
      _addInternal(num);
    }
  }

  int add(int val) {
    _addInternal(val);
    return _heap[0];
  }

  void _addInternal(int val) {
    if (_heap.length < _k) {
      _push(val);
    } else if (val > _heap[0]) {
      _push(val);
      _pop();
    }
  }

  void _push(int val) {
    _heap.add(val);
    int i = _heap.length - 1;
    while (i > 0) {
      int parent = (i - 1) >> 1;
      if (_heap[parent] <= _heap[i]) break;
      var tmp = _heap[parent];
      _heap[parent] = _heap[i];
      _heap[i] = tmp;
      i = parent;
    }
  }

  int _pop() {
    int lastIdx = _heap.length - 1;
    var top = _heap[0];
    var last = _heap.removeAt(lastIdx);
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _heapify(0);
    }
    return top;
  }

  void _heapify(int i) {
    int n = _heap.length;
    while (true) {
      int left = i * 2 + 1;
      int right = left + 1;
      int smallest = i;
      if (left < n && _heap[left] < _heap[smallest]) smallest = left;
      if (right < n && _heap[right] < _heap[smallest]) smallest = right;
      if (smallest == i) break;
      var tmp = _heap[i];
      _heap[i] = _heap[smallest];
      _heap[smallest] = tmp;
      i = smallest;
    }
  }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = KthLargest(k, nums);
 * int param1 = obj.add(val);
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type KthLargest struct {
	k    int
	heap MinHeap
}

func Constructor(k int, nums []int) KthLargest {
	kl := KthLargest{k: k}
	for _, v := range nums {
		kl.Add(v)
	}
	return kl
}

func (this *KthLargest) Add(val int) int {
	if len(this.heap) < this.k {
		heap.Push(&this.heap, val)
	} else if val > this.heap[0] {
		heap.Pop(&this.heap)
		heap.Push(&this.heap, val)
	}
	return this.heap[0]
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */
```

## Ruby

```ruby
class KthLargest
  def initialize(k, nums)
    @k = k
    @heap = []
    nums.each { |num| add(num) }
  end

  def add(val)
    if @heap.size < @k
      heap_push(val)
    elsif val > heap_top
      heap_push(val)
      heap_pop
    end
    heap_top
  end

  private

  def heap_push(val)
    @heap << val
    i = @heap.size - 1
    while i > 0
      parent = (i - 1) / 2
      break if @heap[parent] <= @heap[i]
      @heap[parent], @heap[i] = @heap[i], @heap[parent]
      i = parent
    end
  end

  def heap_pop
    return nil if @heap.empty?
    top = @heap[0]
    last = @heap.pop
    unless @heap.empty?
      @heap[0] = last
      size = @heap.size
      i = 0
      loop do
        left = i * 2 + 1
        right = left + 1
        smallest = i
        smallest = left if left < size && @heap[left] < @heap[smallest]
        smallest = right if right < size && @heap[right] < @heap[smallest]
        break if smallest == i
        @heap[i], @heap[smallest] = @heap[smallest], @heap[i]
        i = smallest
      end
    end
    top
  end

  def heap_top
    @heap[0]
  end
end
```

## Scala

```scala
import java.util.PriorityQueue

class KthLargest(_k: Int, _nums: Array[Int]) {
  private val k: Int = _k
  private val minHeap: PriorityQueue[Int] = new PriorityQueue[Int]()

  // Initialize the heap with the given numbers
  for (num <- _nums) {
    add(num)
  }

  def add(`val`: Int): Int = {
    if (minHeap.size() < k) {
      minHeap.offer(`val`)
    } else if (`val` > minHeap.peek()) {
      minHeap.poll()
      minHeap.offer(`val`)
    }
    minHeap.peek()
  }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * val obj = new KthLargest(k, nums)
 * val param_1 = obj.add(`val`)
 */
```

## Rust

```rust
use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct KthLargest {
    k: usize,
    heap: BinaryHeap<Reverse<i32>>,
}

impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut heap = BinaryHeap::new();
        let kk = k as usize;
        for num in nums {
            heap.push(Reverse(num));
            if heap.len() > kk {
                heap.pop();
            }
        }
        KthLargest { k: kk, heap }
    }

    fn add(&mut self, val: i32) -> i32 {
        self.heap.push(Reverse(val));
        if self.heap.len() > self.k {
            self.heap.pop();
        }
        self.heap.peek().unwrap().0
    }
}
```

## Racket

```racket
#lang racket
(require racket/priority-queue)

(define kth-largest%
  (class object%
    (init-field k nums)
    
    ;; private fields
    (define heap (make-pq <))
    (define size 0)
    
    ;; initialize heap with initial numbers
    (for ([n nums])
      (pq-add! heap n)
      (set! size (+ size 1))
      (when (> size k)
        (pq-pop! heap)
        (set! size (- size 1))))
    
    ;; public method to add a value and return the kth largest
    (define/public (add val)
      (pq-add! heap val)
      (set! size (+ size 1))
      (when (> size k)
        (pq-pop! heap)
        (set! size (- size 1)))
      (pq-min heap))
    
    (super-new)))
```

## Erlang

```erlang
-module(kth_largest).
-export([kth_largest_init_/2, kth_largest_add/1]).

-define(K_KEY, kth_largest_k).
-define(LIST_KEY, kth_largest_list).

-spec kth_largest_init_(K :: integer(), Nums :: [integer()]) -> any().
kth_largest_init_(K, Nums) ->
    put(?K_KEY, K),
    List = lists:foldl(fun(Num, Acc) -> insert_and_trim(Acc, Num, K) end,
                       [], Nums),
    put(?LIST_KEY, List).

-spec kth_largest_add(Val :: integer()) -> integer().
kth_largest_add(Val) ->
    K = get(?K_KEY),
    List = get(?LIST_KEY),
    NewList0 = insert_sorted(List, Val),
    Trimmed = case length(NewList0) > K of
                  true -> tl(NewList0);
                  false -> NewList0
              end,
    put(?LIST_KEY, Trimmed),
    hd(Trimmed).

%% Helper: insert value into ascending sorted list
-spec insert_sorted([integer()], integer()) -> [integer()].
insert_sorted([], Val) ->
    [Val];
insert_sorted([H|T]=L, Val) when Val =< H ->
    [Val | L];
insert_sorted([H|T], Val) ->
    [H | insert_sorted(T, Val)].

%% Helper: insert and keep size <= K
-spec insert_and_trim([integer()], integer(), integer()) -> [integer()].
insert_and_trim(List, Val, K) ->
    NewList = insert_sorted(List, Val),
    case length(NewList) > K of
        true -> tl(NewList);
        false -> NewList
    end.
```

## Elixir

```elixir
defmodule KthLargest do
  @spec init_(k :: integer, nums :: [integer]) :: any
  def init_(k, nums) do
    Process.put(:k, k)
    heap = :gb_sets.empty()
    counter = 0

    {heap, counter} =
      Enum.reduce(nums, {heap, counter}, fn val, {h, c} ->
        add_internal(h, c, val, k)
      end)

    Process.put(:heap, heap)
    Process.put(:counter, counter)
    :ok
  end

  @spec add(val :: integer) :: integer
  def add(val) do
    k = Process.get(:k)
    heap = Process.get(:heap)
    counter = Process.get(:counter)

    {new_heap, new_counter} = add_internal(heap, counter, val, k)

    Process.put(:heap, new_heap)
    Process.put(:counter, new_counter)

    # the smallest element in the heap is the kth largest overall
    {{min_val, _id}, _} = :gb_sets.take_smallest(new_heap)
    min_val
  end

  defp add_internal(heap, counter, val, k) do
    new_counter = counter + 1
    elem = {val, new_counter}
    heap2 = :gb_sets.add(elem, heap)

    if :gb_sets.size(heap2) > k do
      smallest = :gb_sets.smallest(heap2)
      heap3 = :gb_sets.delete_any(smallest, heap2)
      {heap3, new_counter}
    else
      {heap2, new_counter}
    end
  end
end
```

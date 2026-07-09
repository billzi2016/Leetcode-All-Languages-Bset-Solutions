# 2336. Smallest Number in Infinite Set

## Cpp

```cpp
class SmallestInfiniteSet {
public:
    SmallestInfiniteSet() : cur(1) {}
    
    int popSmallest() {
        if (!pq.empty()) {
            int x = pq.top();
            pq.pop();
            inHeap.erase(x);
            return x;
        }
        return cur++;
    }
    
    void addBack(int num) {
        if (num < cur && !inHeap.count(num)) {
            pq.push(num);
            inHeap.insert(num);
        }
    }

private:
    int cur;
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    std::unordered_set<int> inHeap;
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */
```

## Java

```java
class SmallestInfiniteSet {
    private java.util.PriorityQueue<Integer> pq;
    private java.util.HashSet<Integer> inHeap;
    private int cur;

    public SmallestInfiniteSet() {
        pq = new java.util.PriorityQueue<>();
        inHeap = new java.util.HashSet<>();
        cur = 1;
    }

    public int popSmallest() {
        if (!pq.isEmpty()) {
            int val = pq.poll();
            inHeap.remove(val);
            return val;
        }
        return cur++;
    }

    public void addBack(int num) {
        if (num >= cur) {
            // already present in the infinite set, no need to add
            return;
        }
        if (!inHeap.contains(num)) {
            pq.offer(num);
            inHeap.add(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */
```

## Python

```python
import heapq

class SmallestInfiniteSet(object):
    def __init__(self):
        self.cur = 1
        self.heap = []
        self.inheap = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.heap:
            val = heapq.heappop(self.heap)
            self.inheap.remove(val)
            return val
        else:
            val = self.cur
            self.cur += 1
            return val

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.cur and num not in self.inheap:
            heapq.heappush(self.heap, num)
            self.inheap.add(num)
```

## Python3

```python
import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1
        self.heap = []
        self.inheap = set()

    def popSmallest(self) -> int:
        if self.heap and self.heap[0] < self.cur:
            val = heapq.heappop(self.heap)
            self.inheap.remove(val)
            return val
        else:
            val = self.cur
            self.cur += 1
            return val

    def addBack(self, num: int) -> None:
        if num < self.cur and num not in self.inheap:
            heapq.heappush(self.heap, num)
            self.inheap.add(num)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int cur;                // next smallest number not yet popped
    int *heap;              // min-heap for numbers added back
    int heapSize;
    int capacity;
    bool inHeap[1001];      // presence flag for numbers <= 1000
} SmallestInfiniteSet;

static void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

static void heapifyUp(SmallestInfiniteSet *obj, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (obj->heap[parent] <= obj->heap[idx]) break;
        swap(&obj->heap[parent], &obj->heap[idx]);
        idx = parent;
    }
}

static void heapifyDown(SmallestInfiniteSet *obj, int idx) {
    while (true) {
        int left = (idx << 1) + 1;
        int right = left + 1;
        int smallest = idx;

        if (left < obj->heapSize && obj->heap[left] < obj->heap[smallest])
            smallest = left;
        if (right < obj->heapSize && obj->heap[right] < obj->heap[smallest])
            smallest = right;

        if (smallest == idx) break;
        swap(&obj->heap[idx], &obj->heap[smallest]);
        idx = smallest;
    }
}

static void heapPush(SmallestInfiniteSet *obj, int val) {
    if (obj->heapSize == obj->capacity) {
        obj->capacity = obj->capacity ? obj->capacity * 2 : 4;
        obj->heap = realloc(obj->heap, obj->capacity * sizeof(int));
    }
    obj->heap[obj->heapSize] = val;
    heapifyUp(obj, obj->heapSize);
    obj->heapSize++;
}

static int heapPop(SmallestInfiniteSet *obj) {
    int top = obj->heap[0];
    obj->heapSize--;
    if (obj->heapSize > 0) {
        obj->heap[0] = obj->heap[obj->heapSize];
        heapifyDown(obj, 0);
    }
    return top;
}

/** Initialize your data structure here. */
SmallestInfiniteSet* smallestInfiniteSetCreate() {
    SmallestInfiniteSet *obj = malloc(sizeof(SmallestInfiniteSet));
    obj->cur = 1;
    obj->heap = NULL;
    obj->heapSize = 0;
    obj->capacity = 0;
    for (int i = 0; i <= 1000; ++i) obj->inHeap[i] = false;
    return obj;
}

/** Remove and return the smallest integer in the set. */
int smallestInfiniteSetPopSmallest(SmallestInfiniteSet* obj) {
    if (obj->heapSize > 0) {
        int val = heapPop(obj);
        obj->inHeap[val] = false;
        return val;
    } else {
        return obj->cur++;
    }
}

/** Add a positive integer back to the set. */
void smallestInfiniteSetAddBack(SmallestInfiniteSet* obj, int num) {
    if (num < obj->cur && !obj->inHeap[num]) {
        heapPush(obj, num);
        obj->inHeap[num] = true;
    }
}

/** Deallocate memory. */
void smallestInfiniteSetFree(SmallestInfiniteSet* obj) {
    free(obj->heap);
    free(obj);
}
```

## Csharp

```csharp
public class SmallestInfiniteSet
{
    private readonly SortedSet<int> _addedBack;
    private int _next;

    public SmallestInfiniteSet()
    {
        _addedBack = new SortedSet<int>();
        _next = 1;
    }

    public int PopSmallest()
    {
        if (_addedBack.Count > 0)
        {
            int val = _addedBack.Min;
            _addedBack.Remove(val);
            return val;
        }
        else
        {
            return _next++;
        }
    }

    public void AddBack(int num)
    {
        if (num < _next && !_addedBack.Contains(num))
        {
            _addedBack.Add(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.PopSmallest();
 * obj.AddBack(num);
 */
```

## Javascript

```javascript
var SmallestInfiniteSet = function() {
    this.cur = 1;
    this.heap = [];
    this.inHeap = new Set();
};

SmallestInfiniteSet.prototype._heapPush = function(val) {
    const h = this.heap;
    h.push(val);
    let i = h.length - 1;
    while (i > 0) {
        const p = Math.floor((i - 1) / 2);
        if (h[p] <= h[i]) break;
        [h[p], h[i]] = [h[i], h[p]];
        i = p;
    }
};

SmallestInfiniteSet.prototype._heapPop = function() {
    const h = this.heap;
    const min = h[0];
    const last = h.pop();
    if (h.length > 0) {
        h[0] = last;
        let i = 0;
        while (true) {
            let l = i * 2 + 1,
                r = l + 1,
                smallest = i;
            if (l < h.length && h[l] < h[smallest]) smallest = l;
            if (r < h.length && h[r] < h[smallest]) smallest = r;
            if (smallest === i) break;
            [h[i], h[smallest]] = [h[smallest], h[i]];
            i = smallest;
        }
    }
    return min;
};

SmallestInfiniteSet.prototype.popSmallest = function() {
    if (this.heap.length > 0) {
        const val = this._heapPop();
        this.inHeap.delete(val);
        return val;
    } else {
        const val = this.cur;
        this.cur++;
        return val;
    }
};

SmallestInfiniteSet.prototype.addBack = function(num) {
    if (num >= this.cur) return;
    if (this.inHeap.has(num)) return;
    this._heapPush(num);
    this.inHeap.add(num);
};
```

## Typescript

```typescript
class SmallestInfiniteSet {
    private cur: number;
    private added: Set<number>;
    private heap: number[];

    constructor() {
        this.cur = 1;
        this.added = new Set();
        this.heap = [];
    }

    popSmallest(): number {
        if (this.heap.length > 0) {
            const min = this.heap[0];
            const last = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = last;
                this.heapifyDown(0);
            }
            this.added.delete(min);
            return min;
        } else {
            const result = this.cur;
            this.cur++;
            return result;
        }
    }

    addBack(num: number): void {
        if (num < this.cur && !this.added.has(num)) {
            this.added.add(num);
            this.heapPush(num);
        }
    }

    private heapPush(val: number): void {
        this.heap.push(val);
        this.heapifyUp(this.heap.length - 1);
    }

    private heapifyUp(idx: number): void {
        while (idx > 0) {
            const parent = Math.floor((idx - 1) / 2);
            if (this.heap[parent] <= this.heap[idx]) break;
            this.swap(parent, idx);
            idx = parent;
        }
    }

    private heapifyDown(idx: number): void {
        const n = this.heap.length;
        while (true) {
            let smallest = idx;
            const left = idx * 2 + 1;
            const right = idx * 2 + 2;
            if (left < n && this.heap[left] < this.heap[smallest]) smallest = left;
            if (right < n && this.heap[right] < this.heap[smallest]) smallest = right;
            if (smallest === idx) break;
            this.swap(idx, smallest);
            idx = smallest;
        }
    }

    private swap(i: number, j: number): void {
        const tmp = this.heap[i];
        this.heap[i] = this.heap[j];
        this.heap[j] = tmp;
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * var obj = new SmallestInfiniteSet()
 * var param_1 = obj.popSmallest()
 * obj.addBack(num)
 */
```

## Php

```php
class SmallestInfiniteSet {
    private $cur;
    private $heap;
    private $inHeap;

    /**
     * Initialize your data structure here.
     */
    function __construct() {
        $this->cur = 1;
        $this->heap = new SplMinHeap();
        $this->inHeap = [];
    }

    /**
     * @return Integer
     */
    function popSmallest() {
        if (!$this->heap->isEmpty()) {
            $val = $this->heap->extract();
            unset($this->inHeap[$val]);
            return $val;
        } else {
            $val = $this->cur;
            $this->cur++;
            return $val;
        }
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function addBack($num) {
        if ($num < $this->cur && !isset($this->inHeap[$num])) {
            $this->heap->insert($num);
            $this->inHeap[$num] = true;
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * $obj = new SmallestInfiniteSet();
 * $ret_1 = $obj->popSmallest();
 * $obj->addBack($num);
 */
```

## Swift

```swift
class SmallestInfiniteSet {
    private var next: Int
    private var heap: [Int]
    private var present: Set<Int>
    
    init() {
        self.next = 1
        self.heap = []
        self.present = Set()
    }
    
    func popSmallest() -> Int {
        if !heap.isEmpty {
            let val = removeMin()
            present.remove(val)
            return val
        } else {
            let val = next
            next += 1
            return val
        }
    }
    
    func addBack(_ num: Int) {
        if num < next && !present.contains(num) {
            insert(num)
            present.insert(num)
        }
    }
    
    // MARK: - Min Heap Operations
    
    private func insert(_ value: Int) {
        heap.append(value)
        var idx = heap.count - 1
        while idx > 0 {
            let parent = (idx - 1) / 2
            if heap[parent] <= heap[idx] { break }
            heap.swapAt(parent, idx)
            idx = parent
        }
    }
    
    private func removeMin() -> Int {
        let minVal = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            var idx = 0
            while true {
                let left = idx * 2 + 1
                let right = left + 1
                var smallest = idx
                if left < heap.count && heap[left] < heap[smallest] { smallest = left }
                if right < heap.count && heap[right] < heap[smallest] { smallest = right }
                if smallest == idx { break }
                heap.swapAt(idx, smallest)
                idx = smallest
            }
        }
        return minVal
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * let obj = SmallestInfiniteSet()
 * let ret_1: Int = obj.popSmallest()
 * obj.addBack(num)
 */
```

## Kotlin

```kotlin
class SmallestInfiniteSet() {

    private var next = 1
    private val heap = java.util.PriorityQueue<Int>()
    private val inHeap = java.util.HashSet<Int>()

    fun popSmallest(): Int {
        return if (heap.isNotEmpty()) {
            val v = heap.poll()
            inHeap.remove(v)
            v
        } else {
            val v = next
            next++
            v
        }
    }

    fun addBack(num: Int) {
        if (num < next && !inHeap.contains(num)) {
            heap.offer(num)
            inHeap.add(num)
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * var obj = SmallestInfiniteSet()
 * var param_1 = obj.popSmallest()
 * obj.addBack(num)
 */
```

## Dart

```dart
import 'dart:collection';

class SmallestInfiniteSet {
  int _next = 1;
  final SplayTreeSet<int> _addedBack = SplayTreeSet<int>();

  SmallestInfiniteSet();

  int popSmallest() {
    if (_addedBack.isNotEmpty && _addedBack.first < _next) {
      int val = _addedBack.first;
      _addedBack.remove(val);
      return val;
    }
    return _next++;
  }

  void addBack(int num) {
    if (num < _next) {
      _addedBack.add(num);
    }
  }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = SmallestInfiniteSet();
 * int param1 = obj.popSmallest();
 * obj.addBack(num);
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type SmallestInfiniteSet struct {
	cur  int
	h    IntHeap
	in   map[int]bool
}

func Constructor() SmallestInfiniteSet {
	s := SmallestInfiniteSet{
		cur: 1,
		h:   make(IntHeap, 0),
		in:  make(map[int]bool),
	}
	heap.Init(&s.h)
	return s
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	if this.h.Len() > 0 {
		val := heap.Pop(&this.h).(int)
		delete(this.in, val)
		return val
	}
	val := this.cur
	this.cur++
	return val
}

func (this *SmallestInfiniteSet) AddBack(num int) {
	if num < this.cur && !this.in[num] {
		heap.Push(&this.h, num)
		this.in[num] = true
	}
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.PopSmallest();
 * obj.AddBack(num);
 */
```

## Ruby

```ruby
class SmallestInfiniteSet
  def initialize()
    @cur = 1
    @heap = []
    @in_heap = {}
  end

=begin
    :rtype: Integer
=end
  def pop_smallest()
    if !@heap.empty? && @heap[0] < @cur
      val = heap_pop
      @in_heap.delete(val)
      return val
    else
      val = @cur
      @cur += 1
      return val
    end
  end

=begin
    :type num: Integer
    :rtype: Void
=end
  def add_back(num)
    if num < @cur && !@in_heap.key?(num)
      heap_push(num)
      @in_heap[num] = true
    end
  end

  private

  def heap_push(val)
    @heap << val
    idx = @heap.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      break if @heap[parent] <= @heap[idx]
      @heap[parent], @heap[idx] = @heap[idx], @heap[parent]
      idx = parent
    end
  end

  def heap_pop
    min = @heap[0]
    last = @heap.pop
    unless @heap.empty?
      @heap[0] = last
      sift_down(0)
    end
    min
  end

  def sift_down(idx)
    n = @heap.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < n && @heap[left] < @heap[smallest]
        smallest = left
      end
      if right < n && @heap[right] < @heap[smallest]
        smallest = right
      end
      break if smallest == idx
      @heap[idx], @heap[smallest] = @heap[smallest], @heap[idx]
      idx = smallest
    end
  end
end
```

## Scala

```scala
import java.util.PriorityQueue
import scala.collection.mutable

class SmallestInfiniteSet() {
  private var next = 1
  private val heap = new PriorityQueue[Int]()
  private val inHeap = mutable.HashSet[Int]()

  def popSmallest(): Int = {
    if (!heap.isEmpty) {
      val v = heap.poll()
      inHeap.remove(v)
      v
    } else {
      val v = next
      next += 1
      v
    }
  }

  def addBack(num: Int): Unit = {
    if (num < next && !inHeap.contains(num)) {
      heap.offer(num)
      inHeap.add(num)
    }
  }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * val obj = new SmallestInfiniteSet()
 * val param_1 = obj.popSmallest()
 * obj.addBack(num)
 */
```

## Rust

```rust
use std::collections::{BinaryHeap, HashSet};
use std::cmp::Reverse;

struct SmallestInfiniteSet {
    next: i32,
    heap: BinaryHeap<Reverse<i32>>,
    present: HashSet<i32>,
}

impl SmallestInfiniteSet {
    fn new() -> Self {
        SmallestInfiniteSet {
            next: 1,
            heap: BinaryHeap::new(),
            present: HashSet::new(),
        }
    }

    fn pop_smallest(&mut self) -> i32 {
        if let Some(Reverse(val)) = self.heap.pop() {
            self.present.remove(&val);
            val
        } else {
            let cur = self.next;
            self.next += 1;
            cur
        }
    }

    fn add_back(&mut self, num: i32) {
        if num < self.next && !self.present.contains(&num) {
            self.heap.push(Reverse(num));
            self.present.insert(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * let mut obj = SmallestInfiniteSet::new();
 * let ret_1: i32 = obj.pop_smallest();
 * obj.add_back(num);
 */
```

## Racket

```racket
(require racket/heap)

(define smallest-infinite-set%
  (class object%
    (super-new)
    
    (define cur 1)
    (define h (make-heap <))
    (define present (make-hash)) ; numbers currently stored in heap
    
    ;; pop-smallest : -> exact-integer?
    (define/public (pop-smallest)
      (if (zero? (heap-count h))
          (let ([res cur])
            (set! cur (+ cur 1))
            res)
          (let* ([val (heap-min h)])
            (heap-remove-min! h)
            (hash-remove! present val)
            val)))
    
    ;; add-back : exact-integer? -> void?
    (define/public (add-back num)
      (when (and (< num cur) (not (hash-has-key? present num)))
        (heap-insert! h num)
        (hash-set! present num))))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_infinite_set_init_/0,
         smallest_infinite_set_pop_smallest/0,
         smallest_infinite_set_add_back/1]).

-spec smallest_infinite_set_init_() -> any().
smallest_infinite_set_init_() ->
    put(state, #{next => 1, added => [], present => sets:new()}),
    ok.

-spec smallest_infinite_set_pop_smallest() -> integer().
smallest_infinite_set_pop_smallest() ->
    State = get(state),
    Next = maps:get(next, State),
    Added = maps:get(added, State),
    case Added of
        [] ->
            Result = Next,
            NewState = State#{next => Next + 1},
            put(state, NewState),
            Result;
        [H|T] ->
            Result = H,
            Present = maps:get(present, State),
            NewPresent = sets:del_element(H, Present),
            NewState = State#{added => T, present => NewPresent},
            put(state, NewState),
            Result
    end.

-spec smallest_infinite_set_add_back(Num :: integer()) -> any().
smallest_infinite_set_add_back(Num) ->
    State = get(state),
    Next = maps:get(next, State),
    Present = maps:get(present, State),
    if Num < Next,
       not sets:is_element(Num, Present) ->
            Added = maps:get(added, State),
            NewAdded = insert_sorted(Num, Added),
            NewPresent = sets:add_element(Num, Present),
            put(state, State#{added => NewAdded, present => NewPresent});
       true -> ok
    end,
    ok.

%% Insert Num into a sorted list (ascending) without duplicates.
insert_sorted(Num, []) ->
    [Num];
insert_sorted(Num, [H|T]) when Num =< H ->
    [Num, H | T];
insert_sorted(Num, [H|T]) ->
    [H | insert_sorted(Num, T)].
```

## Elixir

```elixir
defmodule SmallestInfiniteSet do
  @spec init_() :: :ok
  def init_() do
    Process.put(:sis_state, {1, MapSet.new()})
    :ok
  end

  defp get_state do
    Process.get(:sis_state)
  end

  defp put_state(state) do
    Process.put(:sis_state, state)
  end

  @spec pop_smallest() :: integer
  def pop_smallest() do
    {cur, set} = get_state()
    if MapSet.size(set) > 0 do
      min = Enum.min(set)
      new_set = MapSet.delete(set, min)
      put_state({cur, new_set})
      min
    else
      put_state({cur + 1, set})
      cur
    end
  end

  @spec add_back(num :: integer) :: :ok
  def add_back(num) do
    {cur, set} = get_state()
    if num < cur and not MapSet.member?(set, num) do
      new_set = MapSet.put(set, num)
      put_state({cur, new_set})
    else
      :ok
    end
  end
end
```

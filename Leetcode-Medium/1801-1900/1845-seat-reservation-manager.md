# 1845. Seat Reservation Manager

## Cpp

```cpp
class SeatManager {
public:
    SeatManager(int n) : nextSeat(1) {}
    
    int reserve() {
        if (!available.empty()) {
            int seat = available.top();
            available.pop();
            return seat;
        }
        return nextSeat++;
    }
    
    void unreserve(int seatNumber) {
        available.push(seatNumber);
    }
private:
    std::priority_queue<int, std::vector<int>, std::greater<int>> available;
    int nextSeat;
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
```

## Java

```java
class SeatManager {
    private java.util.PriorityQueue<Integer> available;
    private int nextSeat;

    public SeatManager(int n) {
        this.available = new java.util.PriorityQueue<>();
        this.nextSeat = 1;
    }

    public int reserve() {
        if (!available.isEmpty()) {
            return available.poll();
        }
        return nextSeat++;
    }

    public void unreserve(int seatNumber) {
        available.offer(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */
```

## Python

```python
import heapq

class SeatManager(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.next_seat = 1
        self.available = []
        # No need to store n explicitly for logic, but keep if needed
        self.n = n

    def reserve(self):
        """
        :rtype: int
        """
        if self.available:
            return heapq.heappop(self.available)
        seat = self.next_seat
        self.next_seat += 1
        return seat

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.available, seatNumber)
```

## Python3

```python
import heapq

class SeatManager:
    def __init__(self, n: int):
        self.heap = []
        self.next_seat = 1
        self.n = n

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        seat = self.next_seat
        self.next_seat += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *heap;
    int size;
    int capacity;
    int next;
} SeatManager;

SeatManager* seatManagerCreate(int n) {
    SeatManager *obj = (SeatManager *)malloc(sizeof(SeatManager));
    obj->capacity = n + 1;               // extra space for safety
    obj->heap = (int *)malloc(obj->capacity * sizeof(int));
    obj->size = 0;
    obj->next = 1;
    return obj;
}

static void heapify_up(SeatManager *obj, int idx) {
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

static void heapify_down(SeatManager *obj, int idx) {
    while (1) {
        int left = idx * 2 + 1;
        int right = left + 1;
        if (left >= obj->size) break;
        int smallest = left;
        if (right < obj->size && obj->heap[right] < obj->heap[left])
            smallest = right;
        if (obj->heap[smallest] < obj->heap[idx]) {
            int tmp = obj->heap[smallest];
            obj->heap[smallest] = obj->heap[idx];
            obj->heap[idx] = tmp;
            idx = smallest;
        } else {
            break;
        }
    }
}

int seatManagerReserve(SeatManager* obj) {
    if (obj->size > 0) {
        int res = obj->heap[0];
        int last = obj->heap[--obj->size];
        if (obj->size > 0) {
            obj->heap[0] = last;
            heapify_down(obj, 0);
        }
        return res;
    } else {
        return obj->next++;
    }
}

void seatManagerUnreserve(SeatManager* obj, int seatNumber) {
    int idx = obj->size++;
    obj->heap[idx] = seatNumber;
    heapify_up(obj, idx);
}

void seatManagerFree(SeatManager* obj) {
    if (obj) {
        free(obj->heap);
        free(obj);
    }
}

/**
 * Your SeatManager struct will be instantiated and called as such:
 * SeatManager* obj = seatManagerCreate(n);
 * int param_1 = seatManagerReserve(obj);
 * seatManagerUnreserve(obj, seatNumber);
 * seatManagerFree(obj);
 */
```

## Csharp

```csharp
using System.Collections.Generic;

public class SeatManager
{
    private int _nextSeat;
    private readonly PriorityQueue<int, int> _availableSeats;

    public SeatManager(int n)
    {
        _nextSeat = 1;
        _availableSeats = new PriorityQueue<int, int>();
    }

    public int Reserve()
    {
        if (_availableSeats.Count > 0)
            return _availableSeats.Dequeue();

        return _nextSeat++;
    }

    public void Unreserve(int seatNumber)
    {
        _availableSeats.Enqueue(seatNumber, seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
```

## Javascript

```javascript
/**
 * Min-heap implementation for numbers.
 */
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
        const root = h[0];
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
        return root;
    }
}

/**
 * @param {number} n
 */
var SeatManager = function(n) {
    this.heap = new MinHeap(); // stores unreserved seats smaller than current marker
    this.next = 1; // next seat number that has never been reserved
};

/**
 * @return {number}
 */
SeatManager.prototype.reserve = function() {
    if (this.heap.size() > 0) {
        return this.heap.pop();
    }
    const seat = this.next;
    this.next += 1;
    return seat;
};

/** 
 * @param {number} seatNumber
 * @return {void}
 */
SeatManager.prototype.unreserve = function(seatNumber) {
    this.heap.push(seatNumber);
};
```

## Typescript

```typescript
class MinHeap {
    private data: number[] = [];

    size(): number {
        return this.data.length;
    }

    push(val: number): void {
        const arr = this.data;
        arr.push(val);
        let idx = arr.length - 1;
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (arr[parent] <= arr[idx]) break;
            [arr[parent], arr[idx]] = [arr[idx], arr[parent]];
            idx = parent;
        }
    }

    pop(): number {
        const arr = this.data;
        if (arr.length === 0) throw new Error("Heap is empty");
        const min = arr[0];
        const last = arr.pop()!;
        if (arr.length > 0) {
            arr[0] = last;
            let idx = 0;
            const n = arr.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;

                if (left < n && arr[left] < arr[smallest]) smallest = left;
                if (right < n && arr[right] < arr[smallest]) smallest = right;
                if (smallest === idx) break;
                [arr[idx], arr[smallest]] = [arr[smallest], arr[idx]];
                idx = smallest;
            }
        }
        return min;
    }
}

class SeatManager {
    private heap: MinHeap;
    private nextSeat: number;

    constructor(n: number) {
        this.heap = new MinHeap();
        this.nextSeat = 1;
    }

    reserve(): number {
        if (this.heap.size() > 0) {
            return this.heap.pop();
        } else {
            const seat = this.nextSeat;
            this.nextSeat++;
            return seat;
        }
    }

    unreserve(seatNumber: number): void {
        this.heap.push(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

## Php

```php
class SeatManager {
    /**
     * @param Integer $n
     */
    private $available;
    private $next;

    function __construct($n) {
        $this->available = new SplMinHeap();
        $this->next = 1;
    }

    /**
     * @return Integer
     */
    function reserve() {
        if (!$this->available->isEmpty()) {
            return $this->available->extract();
        }
        $seat = $this->next;
        $this->next++;
        return $seat;
    }

    /**
     * @param Integer $seatNumber
     * @return NULL
     */
    function unreserve($seatNumber) {
        $this->available->insert($seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * $obj = new SeatManager($n);
 * $ret_1 = $obj->reserve();
 * $obj->unreserve($seatNumber);
 */
```

## Swift

```swift
class SeatManager {
    private var nextSeat: Int
    private var heap: [Int]

    init(_ n: Int) {
        self.nextSeat = 1
        self.heap = []
    }

    func reserve() -> Int {
        if let seat = popMin() {
            return seat
        } else {
            let seat = nextSeat
            nextSeat += 1
            return seat
        }
    }

    func unreserve(_ seatNumber: Int) {
        push(seatNumber)
    }

    private func push(_ val: Int) {
        heap.append(val)
        var idx = heap.count - 1
        while idx > 0 {
            let parent = (idx - 1) / 2
            if heap[idx] < heap[parent] {
                heap.swapAt(idx, parent)
                idx = parent
            } else { break }
        }
    }

    private func popMin() -> Int? {
        guard !heap.isEmpty else { return nil }
        let minVal = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            var idx = 0
            while true {
                let left = idx * 2 + 1
                let right = left + 1
                var smallest = idx
                if left < heap.count && heap[left] < heap[smallest] {
                    smallest = left
                }
                if right < heap.count && heap[right] < heap[smallest] {
                    smallest = right
                }
                if smallest == idx { break }
                heap.swapAt(idx, smallest)
                idx = smallest
            }
        }
        return minVal
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * let obj = SeatManager(n)
 * let ret_1: Int = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class SeatManager(n: Int) {
    private val pq = PriorityQueue<Int>()
    private var nextSeat = 1

    fun reserve(): Int {
        return if (pq.isEmpty()) {
            val seat = nextSeat
            nextSeat++
            seat
        } else {
            pq.poll()
        }
    }

    fun unreserve(seatNumber: Int) {
        pq.offer(seatNumber)
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * var obj = SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

## Dart

```dart
class MinHeap {
  final List<int> _data = [];

  bool get isEmpty => _data.isEmpty;

  void add(int value) {
    _data.add(value);
    _siftUp(_data.length - 1);
  }

  int poll() {
    if (_data.isEmpty) throw StateError('Heap is empty');
    final min = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return min;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_data[parent] <= _data[idx]) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _data[left] < _data[smallest]) smallest = left;
      if (right < n && _data[right] < _data[smallest]) smallest = right;

      if (smallest == idx) break;
      _swap(idx, smallest);
      idx = smallest;
    }
  }

  void _swap(int i, int j) {
    final tmp = _data[i];
    _data[i] = _data[j];
    _data[j] = tmp;
  }
}

class SeatManager {
  final MinHeap _heap = MinHeap();
  int _next = 1;

  SeatManager(int n) {
    // No need to pre‑fill the heap; we use a marker for sequential seats.
  }

  int reserve() {
    if (_heap.isEmpty) {
      return _next++;
    } else {
      return _heap.poll();
    }
  }

  void unreserve(int seatNumber) {
    _heap.add(seatNumber);
  }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = SeatManager(n);
 * int param1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */
```

## Golang

```go
package main

import "container/heap"

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

type SeatManager struct {
	available IntHeap
	next      int
}

func Constructor(n int) SeatManager {
	sm := SeatManager{
		available: make(IntHeap, 0),
		next:      1,
	}
	heap.Init(&sm.available)
	return sm
}

func (this *SeatManager) Reserve() int {
	if this.available.Len() > 0 {
		return heap.Pop(&this.available).(int)
	}
	seat := this.next
	this.next++
	return seat
}

func (this *SeatManager) Unreserve(seatNumber int) {
	heap.Push(&this.available, seatNumber)
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
```

## Ruby

```ruby
class SeatManager
  # Initialize the SeatManager with n seats.
  #
  # @param n [Integer] total number of seats (not directly used in this implementation)
  def initialize(n)
    @next_seat = 1          # The smallest seat number that has never been reserved yet
    @heap = []              # Min-heap to store seats that have been unreserved
  end

  # Reserve the lowest-numbered available seat and return it.
  #
  # @return [Integer] the seat number reserved
  def reserve
    if @heap.empty?
      seat = @next_seat
      @next_seat += 1
      seat
    else
      seat = @heap[0]
      last = @heap.pop
      unless @heap.empty?
        @heap[0] = last
        sift_down(0)
      end
      seat
    end
  end

  # Unreserve a previously reserved seat, making it available again.
  #
  # @param seat_number [Integer] the seat number to unreserve
  # @return [void]
  def unreserve(seat_number)
    push_heap(seat_number)
  end

  private

  # Push a value onto the min-heap.
  #
  # @param val [Integer] value to insert
  def push_heap(val)
    @heap << val
    idx = @heap.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      break if @heap[parent] <= @heap[idx]
      @heap[parent], @heap[idx] = @heap[idx], @heap[parent]
      idx = parent
    end
  end

  # Restore heap property by sifting the element at index downwards.
  #
  # @param idx [Integer] starting index
  def sift_down(idx)
    size = @heap.size
    loop do
      left = idx * 2 + 1
      break if left >= size
      right = left + 1
      smallest = left
      smallest = right if right < size && @heap[right] < @heap[left]
      break if @heap[idx] <= @heap[smallest]
      @heap[idx], @heap[smallest] = @heap[smallest], @heap[idx]
      idx = smallest
    end
  end
end
```

## Scala

```scala
import java.util.PriorityQueue

class SeatManager(_n: Int) {
  private val pq = new PriorityQueue[Int]()
  private var nextSeat = 1

  def reserve(): Int = {
    if (!pq.isEmpty) {
      pq.poll()
    } else {
      val seat = nextSeat
      nextSeat += 1
      seat
    }
  }

  def unreserve(seatNumber: Int): Unit = {
    pq.offer(seatNumber)
  }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * val obj = new SeatManager(n)
 * val param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

## Rust

```rust
use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct SeatManager {
    heap: BinaryHeap<Reverse<i32>>,
    next: i32,
}

impl SeatManager {
    fn new(_n: i32) -> Self {
        SeatManager {
            heap: BinaryHeap::new(),
            next: 1,
        }
    }

    fn reserve(&mut self) -> i32 {
        if let Some(Reverse(seat)) = self.heap.pop() {
            seat
        } else {
            let seat = self.next;
            self.next += 1;
            seat
        }
    }

    fn unreserve(&mut self, seat_number: i32) {
        self.heap.push(Reverse(seat_number));
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * let mut obj = SeatManager::new(n);
 * let ret_1: i32 = obj.reserve();
 * obj.unreserve(seatNumber);
 */
```

## Racket

```racket
#lang racket
(require data/heap)

(define seat-manager%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    (init-field n)
    
    ; internal state
    (define marker 1)                ; next never‑reserved seat number
    (define pq (make-heap <))        ; min‑heap for seats returned by unreserve
    
    ; reserve : -> exact-integer?
    (define/public (reserve)
      (if (heap-empty? pq)
          (let ([res marker])
            (set! marker (+ marker 1))
            res)
          (heap-pop! pq)))
    
    ; unreserve : exact-integer? -> void?
    (define/public (unreserve seat-number)
      (heap-push! pq seat-number))))
```

## Erlang

```erlang
-module(seat_manager).
-export([seat_manager_init_/1,
         seat_manager_reserve/0,
         seat_manager_unreserve/1]).

%% Initialize the manager with n seats.
-spec seat_manager_init_(N :: integer()) -> any().
seat_manager_init_(_N) ->
    %% Marker points to the smallest never‑reserved seat.
    put(seat_manager_state, {1, gb_sets:new()}),
    ok.

%% Reserve and return the smallest available seat number.
-spec seat_manager_reserve() -> integer().
seat_manager_reserve() ->
    {Marker, Set} = get(seat_manager_state),
    case gb_sets:is_empty(Set) of
        true ->
            Seat = Marker,
            put(seat_manager_state, {Marker + 1, Set}),
            Seat;
        false ->
            {Seat, NewSet} = gb_sets:take_smallest(Set),
            put(seat_manager_state, {Marker, NewSet}),
            Seat
    end.

%% Unreserve a previously reserved seat.
-spec seat_manager_unreserve(SeatNumber :: integer()) -> any().
seat_manager_unreserve(SeatNumber) ->
    {Marker, Set} = get(seat_manager_state),
    NewSet = gb_sets:add_element(SeatNumber, Set),
    put(seat_manager_state, {Marker, NewSet}),
    ok.
```

## Elixir

```elixir
defmodule SeatManager do
  use Agent

  @spec init_(n :: integer) :: any
  def init_(n) do
    # Stop existing agent if present (LeetCode calls init_ before each test case)
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    # Start a new agent with initial marker = 1 and empty ordered set
    {:ok, _pid} = Agent.start_link(fn -> {1, :gb_trees.empty()} end, name: __MODULE__)
    :ok
  end

  @spec reserve() :: integer
  def reserve() do
    Agent.get_and_update(__MODULE__, fn
      {marker, tree} ->
        if :gb_trees.is_empty(tree) do
          # No previously unreserved seats, take the current marker
          new_state = {marker + 1, tree}
          {marker, new_state}
        else
          # Take the smallest seat from the ordered set
          {{seat, _value}, new_tree} = :gb_trees.take_smallest(tree)
          new_state = {marker, new_tree}
          {seat, new_state}
        end
    end)
  end

  @spec unreserve(seat_number :: integer) :: any
  def unreserve(seat_number) do
    Agent.update(__MODULE__, fn {marker, tree} ->
      # Insert the seat back into the ordered set
      new_tree = :gb_trees.insert(seat_number, true, tree)
      {marker, new_tree}
    end)
  end
end
```

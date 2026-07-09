# 2349. Design a Number Container System

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class NumberContainers {
    unordered_map<int, int> idx2num;
    unordered_map<int, set<int>> num2idxs;
public:
    NumberContainers() {}
    
    void change(int index, int number) {
        auto it = idx2num.find(index);
        if (it != idx2num.end()) {
            int oldNum = it->second;
            auto sit = num2idxs.find(oldNum);
            if (sit != num2idxs.end()) {
                sit->second.erase(index);
                if (sit->second.empty())
                    num2idxs.erase(sit);
            }
        }
        idx2num[index] = number;
        num2idxs[number].insert(index);
    }
    
    int find(int number) {
        auto it = num2idxs.find(number);
        if (it == num2idxs.end() || it->second.empty())
            return -1;
        return *it->second.begin();
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
```

## Java

```java
import java.util.*;

class NumberContainers {
    private Map<Integer, Integer> indexToNumber;
    private Map<Integer, TreeSet<Integer>> numberToIndices;

    public NumberContainers() {
        indexToNumber = new HashMap<>();
        numberToIndices = new HashMap<>();
    }

    public void change(int index, int number) {
        Integer oldNumber = indexToNumber.get(index);
        if (oldNumber != null) {
            TreeSet<Integer> oldSet = numberToIndices.get(oldNumber);
            if (oldSet != null) {
                oldSet.remove(index);
                if (oldSet.isEmpty()) {
                    numberToIndices.remove(oldNumber);
                }
            }
        }
        indexToNumber.put(index, number);
        TreeSet<Integer> set = numberToIndices.computeIfAbsent(number, k -> new TreeSet<>());
        set.add(index);
    }

    public int find(int number) {
        TreeSet<Integer> set = numberToIndices.get(number);
        if (set == null || set.isEmpty()) {
            return -1;
        }
        return set.first();
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */
```

## Python

```python
import heapq
from collections import defaultdict

class NumberContainers(object):
    def __init__(self):
        self.idx_to_num = {}
        self.num_to_heap = defaultdict(list)

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        # Update mapping; old entries will be lazily cleaned up in find
        self.idx_to_num[index] = number
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.num_to_heap:
            return -1
        heap = self.num_to_heap[number]
        while heap:
            idx = heap[0]
            # Verify that this index still holds the desired number
            if self.idx_to_num.get(idx) == number:
                return idx
            heapq.heappop(heap)  # discard stale entry
        return -1
```

## Python3

```python
import heapq

class NumberContainers:
    def __init__(self):
        self.idx2num = {}
        self.num2heap = {}

    def change(self, index: int, number: int) -> None:
        self.idx2num[index] = number
        if number not in self.num2heap:
            self.num2heap[number] = []
        heapq.heappush(self.num2heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.num2heap:
            return -1
        heap = self.num2heap[number]
        while heap:
            idx = heap[0]
            if self.idx2num.get(idx) == number:
                return idx
            heapq.heappop(heap)
        return -1
```

## C

```c
#include <stdlib.h>
#include "uthash.h"

typedef struct {
    int index;          // key
    int number;
    UT_hash_handle hh;
} IndexMap;

typedef struct {
    int number;         // key
    int *data;          // min-heap of indices
    int size;
    int capacity;
    UT_hash_handle hh;
} NumberHeap;

typedef struct {
    IndexMap *idx_map;
    NumberHeap *num_map;
} NumberContainers;

/* Heap helper functions */
static void heap_push(NumberHeap *h, int val) {
    if (h->size == h->capacity) {
        h->capacity = h->capacity ? h->capacity * 2 : 4;
        h->data = (int *)realloc(h->data, h->capacity * sizeof(int));
    }
    int i = h->size++;
    h->data[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (h->data[p] <= h->data[i]) break;
        int tmp = h->data[p];
        h->data[p] = h->data[i];
        h->data[i] = tmp;
        i = p;
    }
}

static void heap_pop(NumberHeap *h) {
    if (h->size == 0) return;
    h->data[0] = h->data[h->size - 1];
    h->size--;
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= h->size) break;
        int smallest = l;
        if (r < h->size && h->data[r] < h->data[l]) smallest = r;
        if (h->data[i] <= h->data[smallest]) break;
        int tmp = h->data[i];
        h->data[i] = h->data[smallest];
        h->data[smallest] = tmp;
        i = smallest;
    }
}

/* API implementation */
NumberContainers* numberContainersCreate() {
    NumberContainers *obj = (NumberContainers *)malloc(sizeof(NumberContainers));
    obj->idx_map = NULL;
    obj->num_map = NULL;
    return obj;
}

void numberContainersChange(NumberContainers* obj, int index, int number) {
    IndexMap *im = NULL;
    HASH_FIND_INT(obj->idx_map, &index, im);
    if (im) {
        im->number = number;
    } else {
        im = (IndexMap *)malloc(sizeof(IndexMap));
        im->index = index;
        im->number = number;
        HASH_ADD_INT(obj->idx_map, index, im);
    }

    NumberHeap *nh = NULL;
    HASH_FIND_INT(obj->num_map, &number, nh);
    if (!nh) {
        nh = (NumberHeap *)malloc(sizeof(NumberHeap));
        nh->number = number;
        nh->size = 0;
        nh->capacity = 0;
        nh->data = NULL;
        HASH_ADD_INT(obj->num_map, number, nh);
    }
    heap_push(nh, index);
}

int numberContainersFind(NumberContainers* obj, int number) {
    NumberHeap *nh = NULL;
    HASH_FIND_INT(obj->num_map, &number, nh);
    if (!nh) return -1;

    while (nh->size > 0) {
        int idx = nh->data[0];
        IndexMap *im = NULL;
        HASH_FIND_INT(obj->idx_map, &idx, im);
        if (im && im->number == number) {
            return idx;
        }
        heap_pop(nh);
    }

    /* Heap empty: clean up entry */
    HASH_DEL(obj->num_map, nh);
    free(nh->data);
    free(nh);
    return -1;
}

void numberContainersFree(NumberContainers* obj) {
    IndexMap *cur_i, *tmp_i;
    HASH_ITER(hh, obj->idx_map, cur_i, tmp_i) {
        HASH_DEL(obj->idx_map, cur_i);
        free(cur_i);
    }
    NumberHeap *cur_n, *tmp_n;
    HASH_ITER(hh, obj->num_map, cur_n, tmp_n) {
        HASH_DEL(obj->num_map, cur_n);
        free(cur_n->data);
        free(cur_n);
    }
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class NumberContainers
{
    private readonly Dictionary<int, int> indexToNumber;
    private readonly Dictionary<int, SortedSet<int>> numberToIndices;

    public NumberContainers()
    {
        indexToNumber = new Dictionary<int, int>();
        numberToIndices = new Dictionary<int, SortedSet<int>>();
    }

    public void Change(int index, int number)
    {
        if (indexToNumber.TryGetValue(index, out int oldNumber))
        {
            // Remove the index from the old number's set
            var oldSet = numberToIndices[oldNumber];
            oldSet.Remove(index);
            if (oldSet.Count == 0)
                numberToIndices.Remove(oldNumber);
        }

        // Update mapping for the new number
        indexToNumber[index] = number;

        if (!numberToIndices.TryGetValue(number, out var set))
        {
            set = new SortedSet<int>();
            numberToIndices[number] = set;
        }
        set.Add(index);
    }

    public int Find(int number)
    {
        if (numberToIndices.TryGetValue(number, out var set) && set.Count > 0)
            return set.Min;
        return -1;
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.Change(index,number);
 * int param_2 = obj.Find(number);
 */
```

## Javascript

```javascript
var NumberContainers = function () {
    // Map from index to its current number
    this.idxToNum = new Map();
    // Map from number to a min-heap of indices containing that number
    this.numToHeap = new Map();
};

function MinHeap() {
    this.heap = [];
}
MinHeap.prototype.size = function () {
    return this.heap.length;
};
MinHeap.prototype.peek = function () {
    return this.heap[0];
};
MinHeap.prototype.push = function (val) {
    const h = this.heap;
    h.push(val);
    let i = h.length - 1;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (h[p] <= h[i]) break;
        [h[p], h[i]] = [h[i], h[p]];
        i = p;
    }
};
MinHeap.prototype.pop = function () {
    const h = this.heap;
    if (h.length === 0) return undefined;
    const top = h[0];
    const last = h.pop();
    if (h.length > 0) {
        h[0] = last;
        let i = 0;
        while (true) {
            let left = i * 2 + 1;
            let right = left + 1;
            let smallest = i;
            if (left < h.length && h[left] < h[smallest]) smallest = left;
            if (right < h.length && h[right] < h[smallest]) smallest = right;
            if (smallest === i) break;
            [h[i], h[smallest]] = [h[smallest], h[i]];
            i = smallest;
        }
    }
    return top;
};

NumberContainers.prototype.change = function (index, number) {
    const oldNum = this.idxToNum.get(index);
    if (oldNum !== undefined && oldNum === number) {
        // No effective change; still ensure the index is present in heap
        // (optional, can skip)
    }
    // Update mapping
    this.idxToNum.set(index, number);
    // Push index into the heap for the new number
    let heap = this.numToHeap.get(number);
    if (!heap) {
        heap = new MinHeap();
        this.numToHeap.set(number, heap);
    }
    heap.push(index);
};

NumberContainers.prototype.find = function (number) {
    const heap = this.numToHeap.get(number);
    if (!heap) return -1;
    while (heap.size() > 0) {
        const idx = heap.peek();
        // Verify that this index still maps to the requested number
        if (this.idxToNum.get(idx) === number) {
            return idx;
        }
        // Stale entry, discard it
        heap.pop();
    }
    return -1;
};
```

## Typescript

```typescript
class MinHeap {
    private data: number[];
    constructor() {
        this.data = [];
    }
    peek(): number | undefined {
        return this.data[0];
    }
    push(val: number): void {
        const a = this.data;
        a.push(val);
        let i = a.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (a[p] <= a[i]) break;
            [a[p], a[i]] = [a[i], a[p]];
            i = p;
        }
    }
    pop(): number | undefined {
        const a = this.data;
        if (a.length === 0) return undefined;
        const root = a[0];
        const last = a.pop()!;
        if (a.length > 0) {
            a[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1;
                let r = i * 2 + 2;
                let smallest = i;
                if (l < a.length && a[l] < a[smallest]) smallest = l;
                if (r < a.length && a[r] < a[smallest]) smallest = r;
                if (smallest === i) break;
                [a[i], a[smallest]] = [a[smallest], a[i]];
                i = smallest;
            }
        }
        return root;
    }
}

class NumberContainers {
    private idxToNum: Map<number, number>;
    private numToHeap: Map<number, MinHeap>;

    constructor() {
        this.idxToNum = new Map();
        this.numToHeap = new Map();
    }

    change(index: number, number: number): void {
        // Update index mapping
        this.idxToNum.set(index, number);
        // Push index into the heap for this number
        let heap = this.numToHeap.get(number);
        if (!heap) {
            heap = new MinHeap();
            this.numToHeap.set(number, heap);
        }
        heap.push(index);
    }

    find(number: number): number {
        const heap = this.numToHeap.get(number);
        if (!heap) return -1;
        while (true) {
            const top = heap.peek();
            if (top === undefined) {
                this.numToHeap.delete(number);
                return -1;
            }
            const curNum = this.idxToNum.get(top);
            if (curNum === number) {
                return top;
            } else {
                heap.pop(); // discard stale index
            }
        }
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = new NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */
```

## Php

```php
class NumberContainers {
    private $indexToNumber;
    private $numToHeap;

    function __construct() {
        $this->indexToNumber = [];
        $this->numToHeap = [];
    }

    /**
     * @param Integer $index
     * @param Integer $number
     * @return NULL
     */
    function change($index, $number) {
        // Record the new number at this index (overwrites if exists)
        $this->indexToNumber[$index] = $number;
        // Ensure a heap exists for this number and push the index
        if (!isset($this->numToHeap[$number])) {
            $this->numToHeap[$number] = new SplMinHeap();
        }
        $this->numToHeap[$number]->insert($index);
    }

    /**
     * @param Integer $number
     * @return Integer
     */
    function find($number) {
        if (!isset($this->numToHeap[$number])) {
            return -1;
        }
        $heap = $this->numToHeap[$number];
        while (!$heap->isEmpty()) {
            $top = $heap->top();
            // Verify that this index still holds the desired number
            if (isset($this->indexToNumber[$top]) && $this->indexToNumber[$top] === $number) {
                return $top;
            }
            // Stale entry, remove it
            $heap->extract();
        }
        // No valid indices left for this number
        unset($this->numToHeap[$number]);
        return -1;
    }
}
```

## Swift

```swift
import Foundation

class MinHeap {
    private var data: [Int] = []
    
    func push(_ value: Int) {
        data.append(value)
        siftUp(data.count - 1)
    }
    
    func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
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

class NumberContainers {
    private var indexToNumber: [Int: Int] = [:]
    private var numberToHeap: [Int: MinHeap] = [:]
    
    init() {}
    
    func change(_ index: Int, _ number: Int) {
        // Update mapping; old entry will be lazily cleaned later
        indexToNumber[index] = number
        if numberToHeap[number] == nil {
            numberToHeap[number] = MinHeap()
        }
        numberToHeap[number]?.push(index)
    }
    
    func find(_ number: Int) -> Int {
        guard let heap = numberToHeap[number] else { return -1 }
        while true {
            guard let top = heap.peek() else { return -1 }
            if indexToNumber[top] == number {
                return top
            } else {
                _ = heap.pop()
            }
        }
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * let obj = NumberContainers()
 * obj.change(index, number)
 * let ret_2: Int = obj.find(number)
 */
```

## Kotlin

```kotlin
class NumberContainers() {
    private val indexToNumber = HashMap<Int, Int>()
    private val numberToIndices = HashMap<Int, java.util.TreeSet<Int>>()

    fun change(index: Int, number: Int) {
        val oldNumber = indexToNumber.put(index, number)
        if (oldNumber != null) {
            val oldSet = numberToIndices[oldNumber]
            oldSet?.remove(index)
            if (oldSet != null && oldSet.isEmpty()) {
                numberToIndices.remove(oldNumber)
            }
        }
        var set = numberToIndices[number]
        if (set == null) {
            set = java.util.TreeSet()
            numberToIndices[number] = set
        }
        set.add(index)
    }

    fun find(number: Int): Int {
        val set = numberToIndices[number] ?: return -1
        return if (set.isEmpty()) -1 else set.first()
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */
```

## Dart

```dart
import 'dart:collection';

class NumberContainers {
  final Map<int, int> _indexToNumber = {};
  final Map<int, SplayTreeSet<int>> _numToIndices = {};

  NumberContainers();

  void change(int index, int number) {
    if (_indexToNumber.containsKey(index)) {
      int oldNum = _indexToNumber[index]!;
      var oldSet = _numToIndices[oldNum];
      if (oldSet != null) {
        oldSet.remove(index);
        if (oldSet.isEmpty) {
          _numToIndices.remove(oldNum);
        }
      }
    }
    _indexToNumber[index] = number;
    var set = _numToIndices.putIfAbsent(number, () => SplayTreeSet<int>());
    set.add(index);
  }

  int find(int number) {
    var set = _numToIndices[number];
    if (set == null || set.isEmpty) return -1;
    return set.first;
  }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = NumberContainers();
 * obj.change(index,number);
 * int param2 = obj.find(number);
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

type NumberContainers struct {
	idxToNum map[int]int
	numToH   map[int]*IntHeap
}

/** Initialize your data structure here. */
func Constructor() NumberContainers {
	return NumberContainers{
		idxToNum: make(map[int]int),
		numToH:   make(map[int]*IntHeap),
	}
}

func (this *NumberContainers) Change(index int, number int) {
	if _, ok := this.idxToNum[index]; ok {
		// old entry will be lazily removed from heap later
	}
	this.idxToNum[index] = number

	h, ok := this.numToH[number]
	if !ok {
		newH := &IntHeap{}
		heap.Init(newH)
		this.numToH[number] = newH
		h = newH
	}
	heap.Push(h, index)
}

func (this *NumberContainers) Find(number int) int {
	h, ok := this.numToH[number]
	if !ok {
		return -1
	}
	for h.Len() > 0 {
		top := (*h)[0]
		if curNum, exists := this.idxToNum[top]; exists && curNum == number {
			return top
		}
		heap.Pop(h) // discard stale index
	}
	return -1
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Change(index,number);
 * param_2 := obj.Find(number);
 */
```

## Ruby

```ruby
class NumberContainers
  def initialize()
    @idx_to_num = {}
    @num_to_heap = Hash.new { |h, k| h[k] = [] }
  end

  def change(index, number)
    @idx_to_num[index] = number
    heap_push(@num_to_heap[number], index)
  end

  def find(number)
    heap = @num_to_heap[number]
    return -1 if heap.empty?
    while !heap.empty?
      idx = heap[0]
      if @idx_to_num[idx] == number
        return idx
      else
        heap_pop(heap)
      end
    end
    -1
  end

  private

  def heap_push(heap, val)
    heap << val
    i = heap.size - 1
    while i > 0
      parent = (i - 1) / 2
      break if heap[parent] <= heap[i]
      heap[parent], heap[i] = heap[i], heap[parent]
      i = parent
    end
  end

  def heap_pop(heap)
    return nil if heap.empty?
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      i = 0
      size = heap.size
      loop do
        left = i * 2 + 1
        right = left + 1
        smallest = i
        smallest = left if left < size && heap[left] < heap[smallest]
        smallest = right if right < size && heap[right] < heap[smallest]
        break if smallest == i
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
      end
    end
    top
  end
end
```

## Scala

```scala
import scala.collection.mutable
import java.util.{TreeSet => JTreeSet}

class NumberContainers() {
  private val idxToNum = mutable.HashMap[Int, Int]()
  private val numToIdxSet = mutable.HashMap[Int, JTreeSet[Int]]()

  def change(index: Int, number: Int): Unit = {
    idxToNum.get(index).foreach { oldNum =>
      val setOld = numToIdxSet(oldNum)
      setOld.remove(index)
      if (setOld.isEmpty) numToIdxSet.remove(oldNum)
    }
    idxToNum.put(index, number)
    val setNew = numToIdxSet.getOrElseUpdate(number, new JTreeSet[Int]())
    setNew.add(index)
  }

  def find(number: Int): Int = {
    numToIdxSet.get(number) match {
      case Some(set) if !set.isEmpty => set.first()
      case _ => -1
    }
  }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * val obj = new NumberContainers()
 * obj.change(index,number)
 * val param_2 = obj.find(number)
 */
```

## Rust

```rust
use std::collections::{HashMap, BTreeSet};
use std::cell::RefCell;

struct NumberContainers {
    idx_to_num: RefCell<HashMap<i32, i32>>,
    num_to_idxs: RefCell<HashMap<i32, BTreeSet<i32>>>,
}

impl NumberContainers {
    fn new() -> Self {
        NumberContainers {
            idx_to_num: RefCell::new(HashMap::new()),
            num_to_idxs: RefCell::new(HashMap::new()),
        }
    }

    fn change(&self, index: i32, number: i32) {
        // Remove old association if it exists
        let mut idx_map = self.idx_to_num.borrow_mut();
        if let Some(&old_number) = idx_map.get(&index) {
            let mut map = self.num_to_idxs.borrow_mut();
            if let Some(set) = map.get_mut(&old_number) {
                set.remove(&index);
                if set.is_empty() {
                    map.remove(&old_number);
                }
            }
        }
        // Update index mapping
        idx_map.insert(index, number);
        drop(idx_map);

        // Insert into the new number's set
        let mut map = self.num_to_idxs.borrow_mut();
        map.entry(number).or_insert_with(BTreeSet::new).insert(index);
    }

    fn find(&self, number: i32) -> i32 {
        let map = self.num_to_idxs.borrow();
        if let Some(set) = map.get(&number) {
            if let Some(&idx) = set.iter().next() {
                return idx;
            }
        }
        -1
    }
}
```

## Racket

```racket
#lang racket
(require data/heap)

(define number-containers%
  (class object%
    (super-new)
    (define index->number (make-hash))
    (define number->heap (make-hash))

    ;; change : exact-integer? exact-integer? -> void?
    (define/public (change index number)
      (hash-set! index->number index number)
      (define h
        (hash-ref number->heap number
                  (lambda ()
                    (let ((newh (make-heap <)))
                      (hash-set! number->heap number newh)
                      newh))))
      (heap-push! h index))

    ;; find : exact-integer? -> exact-integer?
    (define/public (find number)
      (let ((h (hash-ref number->heap number #f)))
        (if (not h)
            -1
            (let loop ()
              (cond
                [(heap-empty? h) -1]
                [else
                 (define idx (heap-peek h))
                 (if (equal? (hash-ref index->number idx #f) number)
                     idx
                     (begin (heap-pop! h) (loop)))])))))))
```

## Erlang

```erlang
-spec number_containers_init_() -> any().
number_containers_init_() ->
    put(index_to_number, #{}),
    put(number_to_indices, #{}),
    ok.

-spec number_containers_change(Index :: integer(), Number :: integer()) -> any().
number_containers_change(Index, Number) ->
    IndexMap = get(index_to_number),
    NumMap   = get(number_to_indices),

    %% Remove old association if it exists
    {UpdatedIndexMap, UpdatedNumMap0} =
        case maps:find(Index, IndexMap) of
            error ->
                {maps:put(Index, Number, IndexMap), NumMap};
            {ok, OldNumber} ->
                OldSet = maps:get(OldNumber, NumMap),
                NewOldSet = ordsets:del_element(Index, OldSet),
                NewNumMap =
                    if ordsets:is_empty(NewOldSet) ->
                           maps:remove(OldNumber, NumMap);
                       true ->
                           maps:put(OldNumber, NewOldSet, NumMap)
                    end,
                {maps:put(Index, Number, IndexMap), NewNumMap}
        end,

    %% Add new association
    CurSet = maps:get(Number, UpdatedNumMap0, []),
    NewSet = ordsets:add_element(Index, CurSet),
    UpdatedNumMap = maps:put(Number, NewSet, UpdatedNumMap0),

    put(index_to_number, UpdatedIndexMap),
    put(number_to_indices, UpdatedNumMap),
    ok.

-spec number_containers_find(Number :: integer()) -> integer().
number_containers_find(Number) ->
    NumMap = get(number_to_indices),
    case maps:find(Number, NumMap) of
        error -> -1;
        {ok, Set} ->
            case Set of
                [] -> -1;
                [Smallest | _] -> Smallest
            end
    end.
```

## Elixir

```elixir
defmodule NumberContainers do
  @spec init_() :: any
  def init_() do
    Process.put(:idx2num, %{})
    Process.put(:num2set, %{})
  end

  @spec change(index :: integer, number :: integer) :: any
  def change(index, number) do
    idx2num = Process.get(:idx2num)
    num2set = Process.get(:num2set)

    # Remove index from previous number's set if it exists
    case Map.fetch(idx2num, index) do
      {:ok, old_num} ->
        old_set = Map.get(num2set, old_num, :gb_sets.empty())
        new_old_set = :gb_sets.delete_any(index, old_set)

        num2set =
          if :gb_sets.is_empty(new_old_set) do
            Map.delete(num2set, old_num)
          else
            Map.put(num2set, old_num, new_old_set)
          end

        # continue with updated num2set
        num2set = num2set

      :error ->
        num2set = num2set
    end

    # Add index to the new number's set
    cur_set = Map.get(num2set, number, :gb_sets.empty())
    new_cur_set = :gb_sets.add_element(index, cur_set)
    num2set = Map.put(num2set, number, new_cur_set)

    # Update index mapping
    idx2num = Map.put(idx2num, index, number)

    Process.put(:idx2num, idx2num)
    Process.put(:num2set, num2set)
  end

  @spec find(number :: integer) :: integer
  def find(number) do
    num2set = Process.get(:num2set)

    case Map.get(num2set, number) do
      nil -> -1
      set ->
        if :gb_sets.is_empty(set) do
          -1
        else
          :gb_sets.smallest(set)
        end
    end
  end
end
```

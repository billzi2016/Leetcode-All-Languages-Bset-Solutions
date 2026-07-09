# 3362. Zero Array Transformation III

## Cpp

```cpp
class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int m = queries.size();
        vector<pair<int,int>> qs;
        qs.reserve(m);
        for (auto &qr : queries) qs.emplace_back(qr[0], qr[1]);
        sort(qs.begin(), qs.end()); // sort by left
        
        priority_queue<int> pq; // max-heap of right endpoints
        vector<long long> delta(n + 2, 0); // changes to active count
        long long active = 0;
        int idx = 0;
        int used = 0;
        
        for (int i = 0; i < n; ++i) {
            active += delta[i];
            while (idx < m && qs[idx].first == i) {
                pq.push(qs[idx].second);
                ++idx;
            }
            while (active < nums[i]) {
                if (pq.empty()) return -1;
                int r = pq.top(); pq.pop();
                ++used;
                ++active;
                if (r + 1 <= n) delta[r + 1]--;
            }
        }
        // after processing all positions, any remaining queries are unnecessary
        return m - used;
    }
};
```

## Java

```java
class Solution {
    public int maxRemoval(int[] nums, int[][] queries) {
        int n = nums.length;
        int m = queries.length;
        java.util.Arrays.sort(queries, (a, b) -> Integer.compare(a[0], b[0]));
        java.util.PriorityQueue<Integer> maxHeap = new java.util.PriorityQueue<>(java.util.Collections.reverseOrder());
        java.util.PriorityQueue<Integer> minHeap = new java.util.PriorityQueue<>();
        int ptr = 0;
        int used = 0;
        int active = 0;
        for (int i = 0; i < n; i++) {
            while (ptr < m && queries[ptr][0] == i) {
                maxHeap.offer(queries[ptr][1]);
                ptr++;
            }
            while (active < nums[i]) {
                if (maxHeap.isEmpty()) return -1;
                int r = maxHeap.poll();
                used++;
                active++;
                minHeap.offer(r);
            }
            while (!minHeap.isEmpty() && minHeap.peek() == i) {
                minHeap.poll();
                active--;
            }
        }
        return m - used;
    }
}
```

## Python

```python
class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        import heapq

        n = len(nums)
        m = len(queries)

        # sort queries by left endpoint
        queries.sort(key=lambda x: x[0])

        heap = []  # max-heap of right endpoints (store as negative)
        diff = [0] * (n + 1)  # difference array for coverage count
        cur_cov = 0          # current coverage at position i
        used = 0             # number of queries we actually need
        q_idx = 0

        for i in range(n):
            # add all queries whose left <= i to the heap
            while q_idx < m and queries[q_idx][0] <= i:
                heapq.heappush(heap, -queries[q_idx][1])
                q_idx += 1

            cur_cov += diff[i]

            need = nums[i] - cur_cov
            while need > 0:
                # discard intervals that cannot cover position i
                while heap and -heap[0] < i:
                    heapq.heappop(heap)
                if not heap:
                    return -1
                r = -heapq.heappop(heap)   # select interval with farthest right end
                used += 1
                cur_cov += 1               # this interval covers current position i
                diff[r + 1] -= 1           # after r, its contribution ends
                need -= 1

        return m - used
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        # sort queries by left endpoint
        queries.sort(key=lambda x: x[0])
        idx = 0
        heap = []  # max-heap of right endpoints (store negative)
        endCount = [0] * n  # number of selected intervals ending at each position
        cur = 0          # current active selected intervals covering i
        selected = 0

        for i in range(n):
            if i > 0:
                cur -= endCount[i - 1]

            while idx < m and queries[idx][0] == i:
                heapq.heappush(heap, -queries[idx][1])
                idx += 1

            while cur < nums[i]:
                if not heap:
                    return -1
                r = -heapq.heappop(heap)
                selected += 1
                cur += 1
                endCount[r] += 1

        return m - selected
```

## C

```c
#include <stdlib.h>

typedef struct {
    int l;
    int r;
} Query;

static int cmpQuery(const void *a, const void *b) {
    const Query *qa = (const Query *)a;
    const Query *qb = (const Query *)b;
    return qa->l - qb->l;
}

/* max-heap for integers */
typedef struct {
    int *data;
    int size;
} MaxHeap;

static MaxHeap* heapCreate(int capacity) {
    MaxHeap *h = (MaxHeap*)malloc(sizeof(MaxHeap));
    h->data = (int*)malloc(sizeof(int) * capacity);
    h->size = 0;
    return h;
}

static void heapPush(MaxHeap *h, int val) {
    int i = h->size++;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (h->data[p] >= val) break;
        h->data[i] = h->data[p];
        i = p;
    }
    h->data[i] = val;
}

static int heapPop(MaxHeap *h) {
    int ret = h->data[0];
    int x = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        if (l >= h->size) break;
        int r = l + 1;
        int child = (r < h->size && h->data[r] > h->data[l]) ? r : l;
        if (h->data[child] <= x) break;
        h->data[i] = h->data[child];
        i = child;
    }
    h->data[i] = x;
    return ret;
}

int maxRemoval(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize){
    if (queriesSize == 0) return 0;

    Query *qs = (Query*)malloc(sizeof(Query) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        qs[i].l = queries[i][0];
        qs[i].r = queries[i][1];
    }
    qsort(qs, queriesSize, sizeof(Query), cmpQuery);

    int *diff = (int*)calloc(numsSize + 1, sizeof(int));
    MaxHeap *heap = heapCreate(queriesSize);
    long long active = 0;
    int used = 0;
    int idx = 0;

    for (int i = 0; i < numsSize; ++i) {
        while (idx < queriesSize && qs[idx].l == i) {
            heapPush(heap, qs[idx].r);
            ++idx;
        }
        active += diff[i];
        while (active < nums[i]) {
            if (heap->size == 0) {
                free(qs);
                free(diff);
                free(heap->data);
                free(heap);
                return -1;
            }
            int r = heapPop(heap);
            ++used;
            ++active;
            if (r + 1 <= numsSize) diff[r + 1]--;
        }
    }

    int result = queriesSize - used;

    free(qs);
    free(diff);
    free(heap->data);
    free(heap);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxRemoval(int[] nums, int[][] queries) {
        int n = nums.Length;
        int m = queries.Length;
        // Sort queries by left endpoint
        Array.Sort(queries, (a, b) => a[0].CompareTo(b[0]));
        // Max-heap using PriorityQueue with negative priority
        var heap = new PriorityQueue<int, int>();
        int idx = 0;
        int[] diff = new int[n + 2]; // extra space for safety
        long cur = 0; // current coverage count at position i
        int used = 0; // number of queries selected

        for (int i = 0; i < n; i++) {
            cur += diff[i];
            // add all queries whose left endpoint == i
            while (idx < m && queries[idx][0] == i) {
                int r = queries[idx][1];
                heap.Enqueue(r, -r); // max-heap by using negative priority
                idx++;
            }
            // need enough coverage for nums[i]
            while (cur < nums[i]) {
                if (heap.Count == 0) return -1;
                int r = heap.Dequeue(); // interval with farthest right endpoint
                used++;
                cur++; // this interval starts covering from i
                if (r + 1 <= n) diff[r + 1]--;
            }
        }
        // All positions satisfied
        return m - used;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var maxRemoval = function(nums, queries) {
    const n = nums.length;
    const m = queries.length;

    // sort queries by left endpoint
    queries.sort((a, b) => a[0] - b[0]);

    // Max-heap implementation for right endpoints
    class MaxHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
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
                    let l = i * 2 + 1, r = l + 1, largest = i;
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
    const diff = new Array(n + 2).fill(0);
    let cur = 0;      // current number of active selected queries covering position i
    let used = 0;     // number of queries we actually keep
    let idx = 0;      // pointer in sorted queries

    for (let i = 0; i < n; ++i) {
        cur += diff[i];

        while (idx < m && queries[idx][0] === i) {
            heap.push(queries[idx][1]);
            idx++;
        }

        while (cur < nums[i]) {
            if (heap.size() === 0) return -1;
            const r = heap.pop();
            used++;
            cur++;
            if (r + 1 <= n) diff[r + 1]--;
        }
    }

    // remaining queries in heap can be removed
    return m - used;
};
```

## Typescript

```typescript
function maxRemoval(nums: number[], queries: number[][]): number {
    const n = nums.length;
    const m = queries.length;

    // Sort queries by left endpoint
    queries.sort((a, b) => a[0] - b[0]);

    // Max-heap implementation for right endpoints
    class MaxHeap {
        private data: number[] = [];
        size(): number { return this.data.length; }
        push(val: number): void {
            const d = this.data;
            d.push(val);
            let i = d.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (d[p] >= d[i]) break;
                [d[p], d[i]] = [d[i], d[p]];
                i = p;
            }
        }
        pop(): number | undefined {
            const d = this.data;
            if (d.length === 0) return undefined;
            const top = d[0];
            const last = d.pop()!;
            if (d.length > 0) {
                d[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = l + 1;
                    if (l >= d.length) break;
                    let largest = l;
                    if (r < d.length && d[r] > d[l]) largest = r;
                    if (d[i] >= d[largest]) break;
                    [d[i], d[largest]] = [d[largest], d[i]];
                    i = largest;
                }
            }
            return top;
        }
        peek(): number | undefined {
            return this.data.length ? this.data[0] : undefined;
        }
    }

    const heap = new MaxHeap();
    const endAt: number[] = new Array(n).fill(0);
    let curCover = 0; // current number of selected intervals covering position i
    let idx = 0; // index in sorted queries

    for (let i = 0; i < n; ++i) {
        // add all queries whose left <= i
        while (idx < m && queries[idx][0] <= i) {
            heap.push(queries[idx][1]);
            idx++;
        }

        // ensure enough coverage at position i
        while (curCover < nums[i]) {
            // discard intervals that cannot cover i
            while (heap.size() > 0 && (heap.peek() as number) < i) {
                heap.pop();
            }
            const r = heap.pop();
            if (r === undefined) return -1; // impossible
            curCover++;
            endAt[r]++; // this interval will stop contributing after position r
        }

        // move to next index: remove intervals ending at i
        curCover -= endAt[i];
    }

    const selected = endAt.reduce((a, b) => a + b, 0);
    return m - selected;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer
     */
    function maxRemoval($nums, $queries) {
        $n = count($nums);
        $m = count($queries);
        // sort queries by left endpoint
        usort($queries, function($a, $b) {
            if ($a[0] == $b[0]) return $a[1] <=> $b[1];
            return $a[0] <=> $b[0];
        });
        // difference array for ending of selected intervals
        $delta = array_fill(0, $n + 1, 0);
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA); // extract the value (right endpoint)
        $idx = 0;
        $active = 0;      // number of selected intervals currently covering i
        $used = 0;        // total selected intervals
        for ($i = 0; $i < $n; ++$i) {
            // add all queries whose left <= i
            while ($idx < $m && $queries[$idx][0] <= $i) {
                $r = $queries[$idx][1];
                $pq->insert($r, $r); // priority = right endpoint (max-heap)
                $idx++;
            }
            // apply endings at position i
            $active += $delta[$i];
            // need enough intervals to satisfy nums[i]
            while ($active < $nums[$i]) {
                if ($pq->isEmpty()) {
                    return -1;
                }
                $r = $pq->extract(); // choose interval with farthest right end
                $used++;
                $active++;
                if ($r + 1 < $n) {
                    $delta[$r + 1]--;
                }
            }
        }
        return $m - $used;
    }
}
```

## Swift

```swift
class MaxHeap {
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
            let parent = (child - 1) >> 1
            if data[parent] < data[child] {
                data.swapAt(parent, child)
                child = parent
            } else {
                break
            }
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = (parent << 1) + 1
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

class Solution {
    func maxRemoval(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let n = nums.count
        let m = queries.count
        var sorted = queries.map { ($0[0], $0[1]) }.sorted { $0.0 < $1.0 }
        
        var diff = [Int](repeating: 0, count: n + 2)
        var heap = MaxHeap()
        var idx = 0
        var active = 0
        var used = 0
        
        for i in 0..<n {
            active += diff[i]
            
            while idx < m && sorted[idx].0 == i {
                heap.push(sorted[idx].1)
                idx += 1
            }
            
            if nums[i] > 0 {
                while active < nums[i] {
                    // discard intervals that cannot cover current index
                    while let top = heap.peek(), top < i {
                        _ = heap.pop()
                    }
                    guard let r = heap.pop() else {
                        return -1
                    }
                    used += 1
                    active += 1
                    if r + 1 <= n {
                        diff[r + 1] -= 1
                    }
                }
            }
        }
        
        return m - used
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxRemoval(nums: IntArray, queries: Array<IntArray>): Int {
        val n = nums.size
        val m = queries.size
        // Sort queries by left endpoint
        val sorted = queries.sortedWith(compareBy<IntArray> { it[0] }.thenBy { it[1] })
        var ptr = 0
        val heap = java.util.PriorityQueue<Int>(java.util.Collections.reverseOrder())
        val delta = IntArray(n + 2) // for scheduling coverage decrement
        var curCoverage = 0
        var used = 0

        for (i in 0 until n) {
            curCoverage += delta[i]

            while (ptr < m && sorted[ptr][0] <= i) {
                heap.add(sorted[ptr][1])
                ptr++
            }

            while (curCoverage < nums[i]) {
                var r = -1
                while (!heap.isEmpty()) {
                    val cand = heap.poll()
                    if (cand >= i) {
                        r = cand
                        break
                    }
                }
                if (r == -1) return -1  // cannot satisfy requirement

                used++
                curCoverage++               // this interval covers position i
                if (r + 1 <= n) delta[r + 1]--   // schedule its end
            }
        }

        return m - used
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int maxRemoval(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    int m = queries.length;
    queries.sort((a, b) => a[0].compareTo(b[0]));
    List<int> diff = List.filled(n + 1, 0);
    var heap = HeapPriorityQueue<int>((a, b) => b.compareTo(a));
    int idx = 0, selected = 0, cur = 0;
    for (int i = 0; i < n; ++i) {
      while (idx < m && queries[idx][0] == i) {
        heap.add(queries[idx][1]);
        idx++;
      }
      cur += diff[i];
      int need = nums[i];
      while (cur < need) {
        if (heap.isEmpty) return -1;
        int r = heap.removeFirst();
        selected++;
        cur++;
        if (r + 1 <= n) diff[r + 1]--;
      }
    }
    return m - selected;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
	"sort"
)

type MaxHeap []int

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Less(i, j int) bool  { return h[i] > h[j] } // max-heap
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxRemoval(nums []int, queries [][]int) int {
	n := len(nums)
	m := len(queries)

	// sort queries by left endpoint
	sort.Slice(queries, func(i, j int) bool {
		if queries[i][0] == queries[j][0] {
			return queries[i][1] < queries[j][1]
		}
		return queries[i][0] < queries[j][0]
	})

	diff := make([]int, n+1)
	cur := 0
	selected := 0
	idx := 0

	h := &MaxHeap{}
	heap.Init(h)

	for i := 0; i < n; i++ {
		// add all queries whose left <= i
		for idx < m && queries[idx][0] <= i {
			heap.Push(h, queries[idx][1])
			idx++
		}
		cur += diff[i]

		need := nums[i]
		for cur < need {
			if h.Len() == 0 {
				return -1
			}
			r := heap.Pop(h).(int)
			if r < i { // cannot help current position
				continue
			}
			selected++
			cur++
			if r+1 <= n {
				diff[r+1]--
			}
		}
	}

	return m - selected
}
```

## Ruby

```ruby
class MaxHeap
  def initialize
    @data = []
  end

  def push(val)
    i = @data.size
    @data << val
    while i > 0
      p = (i - 1) / 2
      break if @data[p] >= @data[i]
      @data[p], @data[i] = @data[i], @data[p]
      i = p
    end
  end

  def pop
    return nil if @data.empty?
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      size = @data.size
      loop do
        l = i * 2 + 1
        r = i * 2 + 2
        break if l >= size
        child = (r < size && @data[r] > @data[l]) ? r : l
        break if @data[i] >= @data[child]
        @data[i], @data[child] = @data[child], @data[i]
        i = child
      end
    end
    top
  end

  def empty?
    @data.empty?
  end
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def max_removal(nums, queries)
  n = nums.length
  m = queries.length
  sorted = queries.sort_by { |q| q[0] }

  remove_at = Array.new(n + 2, 0) # extra space for r+1 index
  active = 0
  selected = 0
  heap = MaxHeap.new
  idx = 0

  (0...n).each do |i|
    active -= remove_at[i] if i < remove_at.size
    while idx < m && sorted[idx][0] <= i
      heap.push(sorted[idx][1])
      idx += 1
    end
    need = nums[i]
    while active < need
      r = heap.pop
      return -1 if r.nil?
      selected += 1
      active += 1
      remove_at[r + 1] += 1 if r + 1 <= n
    end
  end

  m - selected
end
```

## Scala

```scala
object Solution {
    def maxRemoval(nums: Array[Int], queries: Array[Array[Int]]): Int = {
        val n = nums.length
        val m = queries.length
        val sorted = queries.sortBy(_(0))
        var idx = 0
        import scala.collection.mutable.PriorityQueue
        val heap = PriorityQueue.empty[Int] // max-heap of right endpoints
        val delta = new Array[Int](n + 1) // schedule decrement when interval ends
        var cur = 0
        var selected = 0

        for (i <- 0 until n) {
            while (idx < m && sorted(idx)(0) == i) {
                heap.enqueue(sorted(idx)(1))
                idx += 1
            }
            cur += delta(i)
            while (cur < nums(i)) {
                if (heap.isEmpty) return -1
                val r = heap.dequeue()
                selected += 1
                cur += 1
                if (r + 1 <= n) {
                    delta(r + 1) -= 1
                }
            }
        }
        m - selected
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_removal(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let m = queries.len() as i32;

        // bucket queries by their left endpoint
        let mut buckets: Vec<Vec<i32>> = vec![Vec::new(); n];
        for q in queries.iter() {
            let l = q[0] as usize;
            let r = q[1];
            if l < n {
                buckets[l].push(r);
            }
        }

        use std::collections::BinaryHeap;
        let mut heap: BinaryHeap<i32> = BinaryHeap::new(); // max-heap of right endpoints
        let mut delta: Vec<i32> = vec![0; n + 2]; // schedule decrement when interval ends
        let mut cur: i32 = 0;      // current number of active selected queries covering position i
        let mut selected: i32 = 0;

        for i in 0..n {
            cur += delta[i];
            // add all queries that start at i
            for &r in buckets[i].iter() {
                heap.push(r);
            }
            // ensure enough coverage for nums[i]
            while cur < nums[i] {
                if let Some(r) = heap.pop() {
                    selected += 1;
                    cur += 1;
                    let idx = (r as usize) + 1;
                    if idx <= n {
                        delta[idx] -= 1; // interval stops contributing after r
                    }
                } else {
                    return -1;
                }
            }
        }

        m - selected
    }
}
```

## Racket

```racket
#lang racket
(require data/heap)

(define/contract (max-removal nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length nums)]
         [m (length queries)]
         [sorted-queries (sort queries (lambda (a b) (< (first a) (first b))))]
         [delta (make-vector (+ n 1) 0)]
         [heap (make-heap <)] ; min‑heap storing negative right endpoints
         [nums-vec (list->vector nums)])
    (let loop ((i 0)
               (idx 0)
               (curCover 0)
               (selected 0))
      (if (= i n)
          (- m selected)                         ; all positions satisfied
          (begin
            ;; apply pending delta at position i
            (set! curCover (+ curCover (vector-ref delta i)))
            ;; insert queries whose left endpoint ≤ i
            (let recur-left ((j idx))
              (if (and (< j m)
                       (<= (first (list-ref sorted-queries j)) i))
                  (begin
                    (heap-insert! heap (- (second (list-ref sorted-queries j))))
                    (recur-left (+ j 1)))
                  (set! idx j)))                ; update idx to first unused query
            ;; ensure enough coverage for nums[i]
            (let recur-cover ((c curCover) (s selected))
              (if (>= c (vector-ref nums-vec i))
                  (loop (+ i 1) idx c s)
                  (if (heap-empty? heap)
                      -1                         ; impossible
                      (begin
                        (define r (- (heap-extract! heap))) ; original right endpoint
                        ;; schedule removal of its contribution after r
                        (when (< (+ r 1) (+ n 1))
                          (vector-set! delta (+ r 1)
                                       (- (vector-ref delta (+ r 1)) 1)))
                        (recur-cover (+ c 1) (+ s 1))))))))))))
```

## Erlang

```erlang
-spec max_removal(Nums :: [integer()], Queries :: [[integer()]]) -> integer().
max_removal(Nums, Queries) ->
    TotalQueries = length(Queries),
    % sort queries by left endpoint
    SortedQ = lists:keysort(1,
                [{L, R} || [L, R] <- Queries]),
    N = length(Nums),
    process(0, 0, SortedQ, Nums, gb_trees:empty(), #{}, 0, 0, TotalQueries).

% process(Index, QIdx, SortedQ, Nums, Tree, EndMap,
%         Active, SelectedCnt, TotalQueries) -> Result
process(I, _QIdx, _SortedQ, _Nums, _Tree, _EndMap, _Active, _Sel, _Tot) when I >= length(_Nums) ->
    % all positions satisfied
    _Tot - _Sel;
process(Index, QIdx, SortedQ, Nums, Tree0, EndMap0, Active0, SelCnt0, Tot) ->
    % add all queries whose left == Index
    {Tree1, QIdx1} = add_queries(Index, QIdx, SortedQ, Tree0),
    NumVal = lists:nth(Index + 1, Nums), % Erlang list is 1‑based
    Needed = NumVal - Active0,
    case Needed > 0 of
        true ->
            case select_intervals(Needed, Tree1, EndMap0, Active0, SelCnt0) of
                {error, _} -> -1;
                {Tree2, EndMap2, NewActive, NewSel} ->
                    % remove intervals ending at current index after covering this position
                    {FinalActive, FinalEndMap} = remove_ended(Index, NewActive, EndMap2),
                    process(Index + 1, QIdx1, SortedQ, Nums, Tree2, FinalEndMap,
                            FinalActive, NewSel, Tot)
            end;
        false ->
            % already enough coverage
            {FinalActive, FinalEndMap} = remove_ended(Index, Active0, EndMap0),
            process(Index + 1, QIdx1, SortedQ, Nums, Tree1, FinalEndMap,
                    FinalActive, SelCnt0, Tot)
    end.

% Insert all queries with left == Index into the tree
add_queries(Index, QIdx, SortedQ, Tree) ->
    add_queries_loop(Index, QIdx, SortedQ, Tree).

add_queries_loop(_Index, QIdx, SortedQ, Tree) when QIdx >= length(SortedQ) ->
    {Tree, QIdx};
add_queries_loop(Index, QIdx, SortedQ, Tree) ->
    {L,R} = lists:nth(QIdx + 1, SortedQ),
    case L == Index of
        true ->
            NewTree = tree_insert(R, Tree),
            add_queries_loop(Index, QIdx + 1, SortedQ, NewTree);
        false ->
            {Tree, QIdx}
    end.

% Insert a right endpoint into the multiset tree
tree_insert(R, Tree) ->
    case gb_trees:lookup(R, Tree) of
        {value, C} -> gb_trees:update(R, C + 1, Tree);
        error      -> gb_trees:insert(R, 1, Tree)
    end.

% Select Needed intervals with largest right endpoints
select_intervals(0, Tree, EndMap, Active, Sel) ->
    {Tree, EndMap, Active, Sel};
select_intervals(Needed, Tree, EndMap, Active, Sel) ->
    case gb_trees:is_empty(Tree) of
        true -> {error, not_enough};
        false ->
            {R, C} = gb_trees:largest(Tree),
            NewTree = if C == 1 -> gb_trees:delete(R, Tree);
                         true   -> gb_trees:update(R, C - 1, Tree)
                      end,
            NewActive = Active + 1,
            NewSel = Sel + 1,
            NewEndMap = maps:update_with(R,
                                         fun(V) -> V + 1 end,
                                         1,
                                         EndMap),
            select_intervals(Needed - 1, NewTree, NewEndMap, NewActive, NewSel)
    end.

% Remove intervals that end at current index from active count
remove_ended(Index, Active, EndMap) ->
    case maps:find(Index, EndMap) of
        {ok, C} -> {Active - C, maps:remove(Index, EndMap)};
        error   -> {Active, EndMap}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_removal(nums :: [integer], queries :: [[integer]]) :: integer
  def max_removal(nums, queries) do
    m = length(queries)
    total = m

    sorted = Enum.sort_by(queries, fn [l, _] -> l end)

    n = length(nums)

    num_arr = :array.from_list(nums)
    sorted_arr = :array.from_list(sorted)

    delta = :array.new(n + 1, default: 0)

    case go(0, n, num_arr, sorted_arr, m, total, delta, 0, 0, 0, :gb_trees.empty()) do
      {:ok, ans} -> ans
      :error -> -1
    end
  end

  defp go(i, n, _num_arr, _sorted_arr, _m, total, _delta, _cur, used, _q_idx, _tree) when i == n,
    do: {:ok, total - used}

  defp go(i, n, num_arr, sorted_arr, m, total, delta, cur, used, q_idx, tree) do
    cur = cur + :array.get(i, delta)

    {tree, q_idx} = add_queries(i, sorted_arr, m, q_idx, tree)

    need = :array.get(i, num_arr) - cur

    if need < 0 do
      :error
    else
      case select_need(need, tree, delta, cur, used) do
        :error -> :error
        {new_tree, new_delta, new_cur, new_used} ->
          go(i + 1, n, num_arr, sorted_arr, m, total, new_delta, new_cur, new_used, q_idx, new_tree)
      end
    end
  end

  defp add_queries(i, sorted_arr, m, q_idx, tree) do
    if q_idx < m do
      [l, r] = :array.get(q_idx, sorted_arr)

      if l <= i do
        tree =
          case :gb_trees.lookup(r, tree) do
            :none -> :gb_trees.insert(r, 1, tree)
            {:value, cnt} -> :gb_trees.update(r, cnt + 1, tree)
          end

        add_queries(i, sorted_arr, m, q_idx + 1, tree)
      else
        {tree, q_idx}
      end
    else
      {tree, q_idx}
    end
  end

  defp select_need(0, tree, delta, cur, used), do: {tree, delta, cur, used}

  defp select_need(k, tree, delta, cur, used) when k > 0 do
    if :gb_trees.is_empty(tree) do
      :error
    else
      {r, cnt} = :gb_trees.max(tree)

      tree =
        if cnt == 1,
          do: :gb_trees.delete(r, tree),
          else: :gb_trees.update(r, cnt - 1, tree)

      cur = cur + 1
      used = used + 1

      delta =
        if r + 1 <= :array.size(delta) - 1 do
          prev = :array.get(r + 1, delta)
          :array.set(r + 1, prev - 1, delta)
        else
          delta
        end

      select_need(k - 1, tree, delta, cur, used)
    end
  end
end
```

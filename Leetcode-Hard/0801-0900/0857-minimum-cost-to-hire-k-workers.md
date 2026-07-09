# 0857. Minimum Cost to Hire K Workers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        int n = quality.size();
        vector<pair<double,int>> workers;
        workers.reserve(n);
        for (int i = 0; i < n; ++i) {
            workers.emplace_back(static_cast<double>(wage[i]) / quality[i], quality[i]);
        }
        sort(workers.begin(), workers.end(),
             [](const pair<double,int>& a, const pair<double,int>& b){
                 return a.first < b.first;
             });
        
        priority_queue<int> maxHeap; // stores qualities, largest on top
        long long sumQual = 0;
        double best = numeric_limits<double>::max();
        
        for (auto& wq : workers) {
            double ratio = wq.first;
            int q = wq.second;
            maxHeap.push(q);
            sumQual += q;
            
            if ((int)maxHeap.size() > k) {
                sumQual -= maxHeap.top();
                maxHeap.pop();
            }
            if ((int)maxHeap.size() == k) {
                double cost = sumQual * ratio;
                if (cost < best) best = cost;
            }
        }
        return best;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n = quality.length;
        Worker[] workers = new Worker[n];
        for (int i = 0; i < n; i++) {
            workers[i] = new Worker(quality[i], (double) wage[i] / quality[i]);
        }
        Arrays.sort(workers, Comparator.comparingDouble(w -> w.ratio));

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        long sumQuality = 0;
        double best = Double.MAX_VALUE;

        for (Worker w : workers) {
            maxHeap.offer(w.quality);
            sumQuality += w.quality;

            if (maxHeap.size() > k) {
                sumQuality -= maxHeap.poll();
            }

            if (maxHeap.size() == k) {
                double cost = sumQuality * w.ratio;
                if (cost < best) {
                    best = cost;
                }
            }
        }
        return best;
    }

    private static class Worker {
        int quality;
        double ratio;

        Worker(int q, double r) {
            this.quality = q;
            this.ratio = r;
        }
    }
}
```

## Python

```python
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        workers = []
        for q, w in zip(quality, wage):
            workers.append((w / q, q))
        workers.sort(key=lambda x: x[0])  # sort by ratio

        import heapq
        max_heap = []  # store negative qualities to simulate max-heap
        sum_quality = 0.0
        best = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            sum_quality += q

            if len(max_heap) > k:
                removed_q = -heapq.heappop(max_heap)
                sum_quality -= removed_q

            if len(max_heap) == k:
                cost = sum_quality * ratio
                if cost < best:
                    best = cost

        return best
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = [(w / q, q) for q, w in zip(quality, wage)]
        workers.sort(key=lambda x: x[0])
        max_heap = []
        sum_quality = 0
        best = float('inf')
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            sum_quality += q
            if len(max_heap) > k:
                removed = -heapq.heappop(max_heap)
                sum_quality -= removed
            if len(max_heap) == k:
                cost = sum_quality * ratio
                if cost < best:
                    best = cost
        return best
```

## C

```c
#include <stdlib.h>
#include <float.h>

typedef struct {
    double ratio;
    int   q;
} Worker;

static int cmpWorker(const void *a, const void *b) {
    double diff = ((Worker *)a)->ratio - ((Worker *)b)->ratio;
    if (diff < 0) return -1;
    if (diff > 0) return 1;
    return 0;
}

/* max‑heap for qualities */
static void heapPush(int *heap, int *size, int val) {
    (*size)++;
    int i = *size;
    heap[i] = val;
    while (i > 1 && heap[i / 2] < heap[i]) {
        int tmp = heap[i];
        heap[i] = heap[i / 2];
        heap[i / 2] = tmp;
        i /= 2;
    }
}

static int heapPop(int *heap, int *size) {
    int top = heap[1];
    heap[1] = heap[*size];
    (*size)--;
    int i = 1;
    while (1) {
        int l = i * 2, r = i * 2 + 1, largest = i;
        if (l <= *size && heap[l] > heap[largest]) largest = l;
        if (r <= *size && heap[r] > heap[largest]) largest = r;
        if (largest == i) break;
        int tmp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = tmp;
        i = largest;
    }
    return top;
}

double mincostToHireWorkers(int* quality, int qualitySize, int* wage, int wageSize, int k) {
    (void)wageSize;  // unused, sizes are equal
    Worker *workers = (Worker *)malloc(qualitySize * sizeof(Worker));
    for (int i = 0; i < qualitySize; ++i) {
        workers[i].q = quality[i];
        workers[i].ratio = (double)wage[i] / (double)quality[i];
    }
    qsort(workers, qualitySize, sizeof(Worker), cmpWorker);

    int *heap = (int *)malloc((qualitySize + 1) * sizeof(int)); // 1‑based indexing
    int heapSize = 0;
    long long sumQ = 0;
    double best = DBL_MAX;

    for (int i = 0; i < qualitySize; ++i) {
        heapPush(heap, &heapSize, workers[i].q);
        sumQ += workers[i].q;

        if (heapSize > k) {
            int removed = heapPop(heap, &heapSize);
            sumQ -= removed;
        }

        if (heapSize == k) {
            double cost = sumQ * workers[i].ratio;
            if (cost < best) best = cost;
        }
    }

    free(workers);
    free(heap);
    return best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public double MincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n = quality.Length;
        var workers = new List<(double ratio, int qual)>(n);
        for (int i = 0; i < n; i++) {
            double r = (double)wage[i] / quality[i];
            workers.Add((r, quality[i]));
        }
        workers.Sort((a, b) => a.ratio.CompareTo(b.ratio));

        var pq = new PriorityQueue<int, double>(); // max-heap via negative priority
        double sumQual = 0;
        double best = double.MaxValue;

        foreach (var w in workers) {
            pq.Enqueue(w.qual, -w.qual);
            sumQual += w.qual;

            if (pq.Count > k) {
                int removed = pq.Dequeue(); // removes highest quality
                sumQual -= removed;
            }

            if (pq.Count == k) {
                double cost = sumQual * w.ratio;
                if (cost < best) best = cost;
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} quality
 * @param {number[]} wage
 * @param {number} k
 * @return {number}
 */
var mincostToHireWorkers = function(quality, wage, k) {
    const n = quality.length;
    const workers = new Array(n);
    for (let i = 0; i < n; ++i) {
        workers[i] = { ratio: wage[i] / quality[i], q: quality[i] };
    }
    workers.sort((a, b) => a.ratio - b.ratio);

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
            if (h.length === 0) return undefined;
            const max = h[0];
            const end = h.pop();
            if (h.length > 0) {
                h[0] = end;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        largest = i;
                    if (l < h.length && h[l] > h[largest]) largest = l;
                    if (r < h.length && h[r] > h[largest]) largest = r;
                    if (largest === i) break;
                    [h[i], h[largest]] = [h[largest], h[i]];
                    i = largest;
                }
            }
            return max;
        }
    }

    const heap = new MaxHeap();
    let sumQ = 0;
    let ans = Infinity;

    for (const w of workers) {
        heap.push(w.q);
        sumQ += w.q;
        if (heap.size() > k) {
            sumQ -= heap.pop(); // remove largest quality
        }
        if (heap.size() === k) {
            const cost = sumQ * w.ratio;
            if (cost < ans) ans = cost;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function mincostToHireWorkers(quality: number[], wage: number[], k: number): number {
    const n = quality.length;
    const workers: { ratio: number; q: number }[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        workers[i] = { ratio: wage[i] / quality[i], q: quality[i] };
    }
    workers.sort((a, b) => a.ratio - b.ratio);

    class MaxHeap {
        private heap: number[] = [];
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
        pop(): number | undefined {
            const h = this.heap;
            if (h.length === 0) return undefined;
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

    const heap = new MaxHeap();
    let sumQ = 0;
    let answer = Number.MAX_VALUE;

    for (const w of workers) {
        heap.push(w.q);
        sumQ += w.q;
        if (heap.size() > k) {
            const removed = heap.pop()!;
            sumQ -= removed;
        }
        if (heap.size() === k) {
            const cost = sumQ * w.ratio;
            if (cost < answer) answer = cost;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $quality
     * @param Integer[] $wage
     * @param Integer $k
     * @return Float
     */
    function mincostToHireWorkers($quality, $wage, $k) {
        $n = count($quality);
        $workers = [];
        for ($i = 0; $i < $n; $i++) {
            $ratio = $wage[$i] / $quality[$i];
            $workers[] = ['ratio' => $ratio, 'quality' => $quality[$i]];
        }

        usort($workers, function($a, $b) {
            if ($a['ratio'] == $b['ratio']) return 0;
            return ($a['ratio'] < $b['ratio']) ? -1 : 1;
        });

        $heap = new SplMaxHeap(); // stores qualities, max at top
        $sumQuality = 0.0;
        $minCost = INF;

        foreach ($workers as $w) {
            $q = $w['quality'];
            $ratio = $w['ratio'];

            $heap->insert($q);
            $sumQuality += $q;

            if ($heap->count() > $k) {
                $removed = $heap->extract(); // largest quality removed
                $sumQuality -= $removed;
            }

            if ($heap->count() == $k) {
                $cost = $sumQuality * $ratio;
                if ($cost < $minCost) {
                    $minCost = $cost;
                }
            }
        }

        return $minCost;
    }
}
```

## Swift

```swift
import Foundation

struct MaxHeap {
    private var data: [Int] = []
    
    var count: Int { data.count }
    
    mutating func push(_ value: Int) {
        data.append(value)
        siftUp(from: data.count - 1)
    }
    
    mutating func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        if data.count == 1 {
            return data.removeLast()
        }
        let top = data[0]
        data[0] = data.removeLast()
        siftDown(from: 0)
        return top
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
            let left = parent * 2 + 1
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
    func mincostToHireWorkers(_ quality: [Int], _ wage: [Int], _ k: Int) -> Double {
        let n = quality.count
        var workers: [(ratio: Double, q: Int)] = []
        workers.reserveCapacity(n)
        for i in 0..<n {
            let ratio = Double(wage[i]) / Double(quality[i])
            workers.append((ratio, quality[i]))
        }
        workers.sort { $0.ratio < $1.ratio }
        
        var heap = MaxHeap()
        var sumQuality = 0
        var answer = Double.greatestFiniteMagnitude
        
        for w in workers {
            heap.push(w.q)
            sumQuality += w.q
            
            if heap.count > k {
                if let removed = heap.pop() {
                    sumQuality -= removed
                }
            }
            
            if heap.count == k {
                let cost = Double(sumQuality) * w.ratio
                if cost < answer {
                    answer = cost
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mincostToHireWorkers(quality: IntArray, wage: IntArray, k: Int): Double {
        data class Worker(val ratio: Double, val qual: Int)
        val workers = ArrayList<Worker>(quality.size)
        for (i in quality.indices) {
            workers.add(Worker(wage[i].toDouble() / quality[i], quality[i]))
        }
        workers.sortBy { it.ratio }

        val maxHeap = java.util.PriorityQueue<Int>(compareByDescending { it })
        var sumQual: Long = 0
        var result = Double.MAX_VALUE

        for (w in workers) {
            maxHeap.add(w.qual)
            sumQual += w.qual.toLong()
            if (maxHeap.size > k) {
                val removed = maxHeap.poll()
                sumQual -= removed.toLong()
            }
            if (maxHeap.size == k) {
                val cost = sumQual * w.ratio
                if (cost < result) result = cost
            }
        }
        return result
    }
}
```

## Dart

```dart
class Worker {
  int quality;
  double ratio;
  Worker(this.quality, this.ratio);
}

class MaxHeap {
  final List<int> _data = [];

  int get size => _data.length;

  void push(int value) {
    _data.add(value);
    _siftUp(_data.length - 1);
  }

  int pop() {
    if (_data.isEmpty) throw StateError('pop from empty heap');
    int top = _data[0];
    int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return top;
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
  double mincostToHireWorkers(List<int> quality, List<int> wage, int k) {
    int n = quality.length;
    List<Worker> workers = List.generate(
        n,
        (i) => Worker(quality[i],
            wage[i] / quality[i].toDouble()));
    workers.sort((a, b) => a.ratio.compareTo(b.ratio));

    MaxHeap heap = MaxHeap();
    int sumQuality = 0;
    double result = double.infinity;

    for (var w in workers) {
      heap.push(w.quality);
      sumQuality += w.quality;

      if (heap.size > k) {
        sumQuality -= heap.pop(); // remove largest quality
      }

      if (heap.size == k) {
        double cost = sumQuality * w.ratio;
        if (cost < result) result = cost;
      }
    }

    return result;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
	"math"
	"sort"
)

type worker struct {
	ratio   float64
	quality int
}

// max-heap for qualities
type maxHeap []int

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] } // larger first
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func mincostToHireWorkers(quality []int, wage []int, k int) float64 {
	n := len(quality)
	workers := make([]worker, n)
	for i := 0; i < n; i++ {
		workers[i] = worker{
			ratio:   float64(wage[i]) / float64(quality[i]),
			quality: quality[i],
		}
	}
	sort.Slice(workers, func(i, j int) bool {
		return workers[i].ratio < workers[j].ratio
	})

	h := &maxHeap{}
	heap.Init(h)
	var sumQual int64 = 0
	ans := math.MaxFloat64

	for _, w := range workers {
		heap.Push(h, w.quality)
		sumQual += int64(w.quality)

		if h.Len() > k {
			removed := heap.Pop(h).(int)
			sumQual -= int64(removed)
		}
		if h.Len() == k {
			cost := float64(sumQual) * w.ratio
			if cost < ans {
				ans = cost
			}
		}
	}
	return ans
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
      parent = (i - 1) / 2
      break if @data[parent] >= @data[i]
      @data[parent], @data[i] = @data[i], @data[parent]
      i = parent
    end
  end

  def pop
    return nil if @data.empty?
    max = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      size = @data.size
      loop do
        left = i * 2 + 1
        right = left + 1
        break if left >= size
        larger = left
        larger = right if right < size && @data[right] > @data[left]
        break if @data[i] >= @data[larger]
        @data[i], @data[larger] = @data[larger], @data[i]
        i = larger
      end
    end
    max
  end

  def size
    @data.size
  end
end

# @param {Integer[]} quality
# @param {Integer[]} wage
# @param {Integer} k
# @return {Float}
def mincost_to_hire_workers(quality, wage, k)
  workers = quality.each_index.map do |i|
    [wage[i].to_f / quality[i], quality[i]]
  end
  workers.sort_by! { |ratio, _q| ratio }

  heap = MaxHeap.new
  sum_q = 0.0
  best = Float::INFINITY

  workers.each do |ratio, q|
    heap.push(q)
    sum_q += q

    if heap.size > k
      removed = heap.pop
      sum_q -= removed
    end

    if heap.size == k
      total = sum_q * ratio
      best = total if total < best
    end
  end

  best
end
```

## Scala

```scala
object Solution {
  def mincostToHireWorkers(quality: Array[Int], wage: Array[Int], k: Int): Double = {
    val n = quality.length
    // (ratio, quality)
    val workers = (0 until n).map { i =>
      (wage(i).toDouble / quality(i), quality(i))
    }.toArray

    import scala.util.Sorting
    import scala.math.Ordering
    Sorting.stableSort(workers)(Ordering.by[(Double, Int), Double](_._1))

    import scala.collection.mutable.PriorityQueue
    implicit val maxHeapOrd: Ordering[Int] = Ordering.Int.reverse
    val pq = PriorityQueue.empty[Int]

    var sumQ: Long = 0L
    var minCost = Double.MaxValue

    for ((ratio, q) <- workers) {
      pq.enqueue(q)
      sumQ += q
      if (pq.size > k) {
        val removed = pq.dequeue()
        sumQ -= removed
      }
      if (pq.size == k) {
        val cost = sumQ.toDouble * ratio
        if (cost < minCost) minCost = cost
      }
    }

    minCost
  }
}
```

## Rust

```rust
use std::collections::BinaryHeap;

impl Solution {
    pub fn mincost_to_hire_workers(quality: Vec<i32>, wage: Vec<i32>, k: i32) -> f64 {
        let n = quality.len();
        let mut workers: Vec<(f64, i32)> = (0..n)
            .map(|i| (wage[i] as f64 / quality[i] as f64, quality[i]))
            .collect();

        workers.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

        let mut heap: BinaryHeap<i32> = BinaryHeap::new(); // max-heap of qualities
        let mut sum_quality: i64 = 0;
        let k_usize = k as usize;
        let mut answer = std::f64::MAX;

        for (ratio, q) in workers {
            heap.push(q);
            sum_quality += q as i64;

            if heap.len() > k_usize {
                if let Some(removed) = heap.pop() {
                    sum_quality -= removed as i64;
                }
            }

            if heap.len() == k_usize {
                let cost = (sum_quality as f64) * ratio;
                if cost < answer {
                    answer = cost;
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (mincost-to-hire-workers quality wage k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? flonum?)
  (let* ((workers
          (map (lambda (q w)
                 (cons (/ (exact->inexact w) (exact->inexact q))
                       (exact->inexact q)))
               quality wage))
         (sorted (sort workers (lambda (a b) (< (car a) (car b)))))
         (heap (make-heap <))) ; min‑heap storing negative qualities
    (let loop ((lst sorted)
               (sum 0.0)
               (best +inf.0))
      (if (null? lst)
          best
          (let* ((ratio (car (car lst)))
                 (q (cdr (car lst)))
                 (neg-q (- q))) ; negative for max‑heap behavior
            (heap-add! heap neg-q)
            (set! sum (+ sum q))
            (when (> (heap-size heap) k)
              (let ([removed (heap-remove-min! heap)])
                (set! sum (- sum (- removed))))) ; subtract largest quality
            (if (= (heap-size heap) k)
                (let ((cost (* sum ratio)))
                  (loop (cdr lst) sum (min best cost)))
                (loop (cdr lst) sum best)))))))
```

## Erlang

```erlang
-spec mincost_to_hire_workers(Quality :: [integer()], Wage :: [integer()], K :: integer()) -> float().
mincost_to_hire_workers(Quality, Wage, K) ->
    Workers = lists:zipwith(fun(Q, W) -> {W / Q, Q} end, Quality, Wage),
    Sorted = lists:sort(fun({R1,_}, {R2,_}) -> R1 < R2 end, Workers),
    loop(Sorted, K, gb_trees:empty(), 0, 0, 1.0e100).

loop([], _K, _Tree, _SumQual, _Size, Best) ->
    Best;
loop([{Ratio, Q}|Rest], K, Tree, SumQual, Size, Best) ->
    % insert current worker's quality
    Tree1 = case gb_trees:lookup(Q, Tree) of
                none -> gb_trees:insert(Q, 1, Tree);
                {value, C} -> gb_trees:update(Q, C + 1, Tree)
            end,
    SumQual1 = SumQual + Q,
    Size1 = Size + 1,

    % keep only K smallest qualities (remove the largest if needed)
    {Tree2, SumQual2, Size2} =
        if Size1 > K ->
                {MaxQ, Count} = gb_trees:largest(Tree1),
                NewTree = case Count of
                            1 -> gb_trees:delete(MaxQ, Tree1);
                            _ -> gb_trees:update(MaxQ, Count - 1, Tree1)
                          end,
                {NewTree, SumQual1 - MaxQ, Size1 - 1};
           true ->
                {Tree1, SumQual1, Size1}
        end,

    % compute cost when we have exactly K workers
    Best1 = if Size2 == K ->
                Cost = Ratio * SumQual2,
                case Cost < Best of
                    true -> Cost;
                    false -> Best
                end;
            true -> Best
            end,

    loop(Rest, K, Tree2, SumQual2, Size2, Best1).
```

## Elixir

```elixir
defmodule Solution do
  @spec mincost_to_hire_workers(quality :: [integer], wage :: [integer], k :: integer) :: float
  def mincost_to_hire_workers(quality, wage, k) do
    workers =
      Enum.map(Enum.with_index(quality), fn {q, i} ->
        w = Enum.at(wage, i)
        {w / q, q}
      end)

    sorted = Enum.sort_by(workers, fn {ratio, _q} -> ratio end)

    init_tree = :gb_trees.empty()
    init_sum = 0.0
    init_sz = 0
    init_ans = :math.pow(10, 18)

    {_tree, _sum, _sz, ans} =
      Enum.reduce(sorted, {init_tree, init_sum, init_sz, init_ans}, fn {ratio, q},
                                                                     {tree, sum, sz, best} ->
        tree = insert(tree, q)
        sum = sum + q
        sz = sz + 1

        if sz > k do
          {max_q, tree} = remove_max_one(tree)
          sum = sum - max_q
          sz = sz - 1
        end

        best =
          if sz == k do
            cost = sum * ratio
            if cost < best, do: cost, else: best
          else
            best
          end

        {tree, sum, sz, best}
      end)

    ans
  end

  defp insert(tree, q) do
    case :gb_trees.lookup(q, tree) do
      :none -> :gb_trees.insert(q, 1, tree)
      {:value, cnt} -> :gb_trees.update(q, cnt + 1, tree)
    end
  end

  defp remove_max_one(tree) do
    {max_q, cnt} = :gb_trees.largest(tree)

    new_tree =
      if cnt == 1 do
        :gb_trees.delete(max_q, tree)
      else
        :gb_trees.update(max_q, cnt - 1, tree)
      end

    {max_q, new_tree}
  end
end
```

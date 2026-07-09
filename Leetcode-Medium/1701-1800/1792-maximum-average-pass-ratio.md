# 1792. Maximum Average Pass Ratio

## Cpp

```cpp
class Solution {
public:
    double maxAverageRatio(std::vector<std::vector<int>>& classes, int extraStudents) {
        auto gain = [](int p, int t) -> double {
            return static_cast<double>(p + 1) / (t + 1) - static_cast<double>(p) / t;
        };
        
        using Node = std::pair<double, std::pair<int,int>>; // {gain,{pass,total}}
        auto cmp = [](const Node& a, const Node& b) {
            return a.first < b.first; // max-heap by gain
        };
        std::priority_queue<Node, std::vector<Node>, decltype(cmp)> pq(cmp);
        
        for (auto &cls : classes) {
            int p = cls[0], t = cls[1];
            pq.emplace(gain(p, t), std::make_pair(p, t));
        }
        
        while (extraStudents-- > 0) {
            auto cur = pq.top(); pq.pop();
            int p = cur.second.first;
            int t = cur.second.second;
            ++p; ++t;
            pq.emplace(gain(p, t), std::make_pair(p, t));
        }
        
        double sum = 0.0;
        while (!pq.empty()) {
            auto cur = pq.top(); pq.pop();
            int p = cur.second.first;
            int t = cur.second.second;
            sum += static_cast<double>(p) / t;
        }
        return sum / classes.size();
    }
};
```

## Java

```java
import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    private static class Node {
        int pass;
        int total;
        Node(int p, int t) {
            this.pass = p;
            this.total = t;
        }
        double gain() {
            return ((double)(pass + 1) / (total + 1)) - ((double)pass / total);
        }
    }

    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<Node> pq = new PriorityQueue<>(new Comparator<Node>() {
            @Override
            public int compare(Node a, Node b) {
                return Double.compare(b.gain(), a.gain()); // max-heap based on gain
            }
        });

        for (int[] cls : classes) {
            pq.offer(new Node(cls[0], cls[1]));
        }

        while (extraStudents-- > 0) {
            Node cur = pq.poll();
            cur.pass++;
            cur.total++;
            pq.offer(cur);
        }

        double sum = 0.0;
        int n = classes.length;
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            sum += (double) node.pass / node.total;
        }
        return sum / n;
    }
}
```

## Python

```python
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq

        # Build a max-heap based on the gain of adding one student
        heap = []
        for p, t in classes:
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-gain, p, t))

        # Distribute extra students greedily
        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            new_gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-new_gain, p, t))

        # Compute final average ratio
        total_ratio = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total_ratio += p / t

        return total_ratio / len(classes)
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for p, t in classes:
            gain = (p + 1) / (t + 1) - p / t
            heap.append((-gain, p, t))
        heapq.heapify(heap)

        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-gain, p, t))

        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t

        return total / len(classes)
```

## C

```c
#include <stdlib.h>

static double calcGain(int p, int t) {
    return ((double)(p + 1) / (t + 1)) - ((double)p / t);
}

typedef struct {
    int pass;
    int total;
    double gain;
} Node;

static void heapifyDown(Node *heap, int n, int i) {
    while (1) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && heap[l].gain > heap[largest].gain) largest = l;
        if (r < n && heap[r].gain > heap[largest].gain) largest = r;
        if (largest != i) {
            Node tmp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = tmp;
            i = largest;
        } else {
            break;
        }
    }
}

double maxAverageRatio(int** classes, int classesSize, int* classesColSize, int extraStudents) {
    int n = classesSize;
    Node *heap = (Node *)malloc(sizeof(Node) * n);
    for (int i = 0; i < n; ++i) {
        int p = classes[i][0];
        int t = classes[i][1];
        heap[i].pass = p;
        heap[i].total = t;
        heap[i].gain = calcGain(p, t);
    }
    for (int i = n / 2 - 1; i >= 0; --i) {
        heapifyDown(heap, n, i);
    }

    for (int k = 0; k < extraStudents; ++k) {
        heap[0].pass += 1;
        heap[0].total += 1;
        heap[0].gain = calcGain(heap[0].pass, heap[0].total);
        heapifyDown(heap, n, 0);
    }

    double sum = 0.0;
    for (int i = 0; i < n; ++i) {
        sum += (double)heap[i].pass / heap[i].total;
    }
    free(heap);
    return sum / n;
}
```

## Csharp

```csharp
public class Solution
{
    public double MaxAverageRatio(int[][] classes, int extraStudents)
    {
        var pq = new PriorityQueue<Node, double>();
        foreach (var c in classes)
        {
            var node = new Node(c[0], c[1]);
            double gain = ((double)(node.Passes + 1) / (node.Total + 1)) - ((double)node.Passes / node.Total);
            pq.Enqueue(node, -gain); // negative for max-heap behavior
        }

        for (int i = 0; i < extraStudents; i++)
        {
            var node = pq.Dequeue();
            node.Passes++;
            node.Total++;
            double gain = ((double)(node.Passes + 1) / (node.Total + 1)) - ((double)node.Passes / node.Total);
            pq.Enqueue(node, -gain);
        }

        double sum = 0;
        while (pq.Count > 0)
        {
            var node = pq.Dequeue();
            sum += (double)node.Passes / node.Total;
        }

        return sum / classes.Length;
    }

    private class Node
    {
        public int Passes;
        public int Total;

        public Node(int passes, int total)
        {
            Passes = passes;
            Total = total;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} classes
 * @param {number} extraStudents
 * @return {number}
 */
var maxAverageRatio = function(classes, extraStudents) {
    // Max heap implementation based on gain
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
                if (h[p].gain >= h[i].gain) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return null;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let left = i * 2 + 1;
                    let right = i * 2 + 2;
                    let largest = i;
                    if (left < h.length && h[left].gain > h[largest].gain) largest = left;
                    if (right < h.length && h[right].gain > h[largest].gain) largest = right;
                    if (largest === i) break;
                    [h[i], h[largest]] = [h[largest], h[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    const gain = (p, t) => {
        return (p + 1) / (t + 1) - p / t;
    };

    const heap = new MaxHeap();
    for (const [p, t] of classes) {
        heap.push({ p, t, gain: gain(p, t) });
    }

    while (extraStudents > 0) {
        const node = heap.pop();
        node.p += 1;
        node.t += 1;
        node.gain = gain(node.p, node.t);
        heap.push(node);
        extraStudents--;
    }

    let total = 0;
    for (const node of heap.heap) {
        total += node.p / node.t;
    }
    return total / classes.length;
};
```

## Typescript

```typescript
function maxAverageRatio(classes: number[][], extraStudents: number): number {
    class MaxHeap {
        data: { p: number; t: number; gain: number }[] = [];
        private swap(i: number, j: number) {
            const tmp = this.data[i];
            this.data[i] = this.data[j];
            this.data[j] = tmp;
        }
        private parent(i: number): number {
            return (i - 1) >> 1;
        }
        private left(i: number): number {
            return i * 2 + 1;
        }
        private right(i: number): number {
            return i * 2 + 2;
        }
        push(item: { p: number; t: number; gain: number }) {
            this.data.push(item);
            this.bubbleUp(this.data.length - 1);
        }
        bubbleUp(idx: number) {
            while (idx > 0) {
                const p = this.parent(idx);
                if (this.data[p].gain < this.data[idx].gain) {
                    this.swap(p, idx);
                    idx = p;
                } else break;
            }
        }
        pop(): { p: number; t: number; gain: number } | null {
            if (this.data.length === 0) return null;
            const top = this.data[0];
            const last = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        bubbleDown(idx: number) {
            const n = this.data.length;
            while (true) {
                let largest = idx;
                const l = this.left(idx);
                const r = this.right(idx);
                if (l < n && this.data[l].gain > this.data[largest].gain) largest = l;
                if (r < n && this.data[r].gain > this.data[largest].gain) largest = r;
                if (largest !== idx) {
                    this.swap(largest, idx);
                    idx = largest;
                } else break;
            }
        }
    }

    const heap = new MaxHeap();

    for (const [p0, t0] of classes) {
        const p = p0;
        const t = t0;
        const gain = (p + 1) / (t + 1) - p / t;
        heap.push({ p, t, gain });
    }

    for (let i = 0; i < extraStudents; ++i) {
        const cur = heap.pop()!;
        cur.p += 1;
        cur.t += 1;
        cur.gain = (cur.p + 1) / (cur.t + 1) - cur.p / cur.t;
        heap.push(cur);
    }

    let sum = 0;
    for (const item of heap.data) {
        sum += item.p / item.t;
    }
    return sum / classes.length;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $classes
     * @param Integer $extraStudents
     * @return Float
     */
    function maxAverageRatio($classes, $extraStudents) {
        $pq = new SplPriorityQueue();
        // Ensure the queue returns only the data (the class info)
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        
        foreach ($classes as $c) {
            $p = $c[0];
            $t = $c[1];
            $gain = ($p + 1) / ($t + 1) - $p / $t;
            $pq->insert([$p, $t], $gain);
        }
        
        for ($i = 0; $i < $extraStudents; $i++) {
            $top = $pq->extract(); // [$p, $t]
            $p = $top[0] + 1;
            $t = $top[1] + 1;
            $newGain = ($p + 1) / ($t + 1) - $p / $t;
            $pq->insert([$p, $t], $newGain);
        }
        
        $sum = 0.0;
        while (!$pq->isEmpty()) {
            $item = $pq->extract(); // [$p, $t]
            $sum += $item[0] / $item[1];
        }
        
        return $sum / count($classes);
    }
}
```

## Swift

```swift
import Foundation

struct Node {
    var pass: Int
    var total: Int
    var gain: Double
}

struct MaxHeap {
    private(set) var data: [Node] = []
    
    mutating func push(_ node: Node) {
        data.append(node)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Node? {
        guard !data.isEmpty else { return nil }
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[child].gain <= data[parent].gain { break }
            data.swapAt(child, parent)
            child = parent
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parentIdx = index
        while true {
            let left = parentIdx * 2 + 1
            let right = left + 1
            var largest = parentIdx
            
            if left < data.count && data[left].gain > data[largest].gain {
                largest = left
            }
            if right < data.count && data[right].gain > data[largest].gain {
                largest = right
            }
            if largest == parentIdx { break }
            data.swapAt(parentIdx, largest)
            parentIdx = largest
        }
    }
}

class Solution {
    func maxAverageRatio(_ classes: [[Int]], _ extraStudents: Int) -> Double {
        func calcGain(pass: Int, total: Int) -> Double {
            return Double(pass + 1) / Double(total + 1) - Double(pass) / Double(total)
        }
        
        var heap = MaxHeap()
        for cls in classes {
            let p = cls[0]
            let t = cls[1]
            let g = calcGain(pass: p, total: t)
            heap.push(Node(pass: p, total: t, gain: g))
        }
        
        var extra = extraStudents
        while extra > 0 {
            guard var node = heap.pop() else { break }
            node.pass += 1
            node.total += 1
            node.gain = calcGain(pass: node.pass, total: node.total)
            heap.push(node)
            extra -= 1
        }
        
        var sum: Double = 0.0
        for n in heap.data {
            sum += Double(n.pass) / Double(n.total)
        }
        return sum / Double(classes.count)
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    fun maxAverageRatio(classes: Array<IntArray>, extraStudents: Int): Double {
        val pq = PriorityQueue<Node> { a, b ->
            when {
                a.gain < b.gain -> 1
                a.gain > b.gain -> -1
                else -> 0
            }
        }

        for (c in classes) {
            val p = c[0]
            val t = c[1]
            val gain = ((p + 1).toDouble() / (t + 1)) - (p.toDouble() / t)
            pq.add(Node(p, t, gain))
        }

        repeat(extraStudents) {
            val node = pq.poll()
            node.pass += 1
            node.total += 1
            node.gain = ((node.pass + 1).toDouble() / (node.total + 1)) - (node.pass.toDouble() / node.total)
            pq.offer(node)
        }

        var sum = 0.0
        for (node in pq) {
            sum += node.pass.toDouble() / node.total
        }
        return sum / classes.size
    }

    private data class Node(var pass: Int, var total: Int, var gain: Double)
}
```

## Dart

```dart
class Solution {
  double maxAverageRatio(List<List<int>> classes, int extraStudents) {
    // Node representing a class with current passes, total students and its gain.
    class Node {
      int pass;
      int total;
      double gain;
      Node(this.pass, this.total)
          : gain = ((pass + 1) / (total + 1)) - (pass / total);
      void updateGain() {
        gain = ((pass + 1) / (total + 1)) - (pass / total);
      }
    }

    // Max-heap based on the gain.
    class MaxHeap {
      List<Node> data;
      MaxHeap(this.data) {
        for (int i = (data.length >> 1) - 1; i >= 0; i--) {
          _siftDown(i);
        }
      }

      bool get isEmpty => data.isEmpty;

      Node pop() {
        final top = data[0];
        final last = data.removeLast();
        if (data.isNotEmpty) {
          data[0] = last;
          _siftDown(0);
        }
        return top;
      }

      void push(Node node) {
        data.add(node);
        _siftUp(data.length - 1);
      }

      void _swap(int i, int j) {
        final tmp = data[i];
        data[i] = data[j];
        data[j] = tmp;
      }

      void _siftUp(int idx) {
        while (idx > 0) {
          final parent = (idx - 1) >> 1;
          if (data[idx].gain <= data[parent].gain) break;
          _swap(idx, parent);
          idx = parent;
        }
      }

      void _siftDown(int idx) {
        final n = data.length;
        while (true) {
          int largest = idx;
          final left = idx * 2 + 1;
          final right = left + 1;
          if (left < n && data[left].gain > data[largest].gain) {
            largest = left;
          }
          if (right < n && data[right].gain > data[largest].gain) {
            largest = right;
          }
          if (largest == idx) break;
          _swap(idx, largest);
          idx = largest;
        }
      }
    }

    // Initialize heap with all classes.
    final nodes = <Node>[];
    for (var c in classes) {
      nodes.add(Node(c[0], c[1]));
    }
    final heap = MaxHeap(nodes);

    // Distribute extra students greedily.
    for (int i = 0; i < extraStudents; ++i) {
      final top = heap.pop();
      top.pass += 1;
      top.total += 1;
      top.updateGain();
      heap.push(top);
    }

    // Compute the final average pass ratio.
    double sum = 0.0;
    for (var node in heap.data) {
      sum += node.pass / node.total;
    }
    return sum / classes.length;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type Class struct {
	p, t int
	gain float64
}

type ClassHeap []*Class

func (h ClassHeap) Len() int { return len(h) }
func (h ClassHeap) Less(i, j int) bool { return h[i].gain > h[j].gain } // max-heap
func (h ClassHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *ClassHeap) Push(x interface{}) {
	*h = append(*h, x.(*Class))
}
func (h *ClassHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

func calcGain(p, t int) float64 {
	return float64(p+1)/float64(t+1) - float64(p)/float64(t)
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	h := make(ClassHeap, 0, len(classes))
	for _, c := range classes {
		p, t := c[0], c[1]
		h = append(h, &Class{p: p, t: t, gain: calcGain(p, t)})
	}
	heap.Init(&h)

	for i := 0; i < extraStudents; i++ {
		top := heap.Pop(&h).(*Class)
		top.p++
		top.t++
		top.gain = calcGain(top.p, top.t)
		heap.Push(&h, top)
	}

	total := 0.0
	for _, c := range h {
		total += float64(c.p) / float64(c.t)
	}
	return total / float64(len(classes))
}
```

## Ruby

```ruby
def max_average_ratio(classes, extra_students)
  heap = []
  classes.each do |p, t|
    gain = ((p + 1).to_f / (t + 1)) - (p.to_f / t)
    heap << [gain, p, t]
  end

  (heap.size / 2 - 1).downto(0) { |i| sift_down(heap, i) }

  extra_students.times do
    gain, p, t = heap_pop(heap)
    p += 1
    t += 1
    new_gain = ((p + 1).to_f / (t + 1)) - (p.to_f / t)
    heap_push(heap, [new_gain, p, t])
  end

  total = 0.0
  heap.each { |_, p, t| total += p.to_f / t }
  total / classes.size
end

def heap_push(heap, item)
  heap << item
  i = heap.size - 1
  while i > 0
    parent = (i - 1) / 2
    break if heap[parent][0] >= heap[i][0]
    heap[parent], heap[i] = heap[i], heap[parent]
    i = parent
  end
end

def heap_pop(heap)
  top = heap[0]
  last = heap.pop
  unless heap.empty?
    heap[0] = last
    sift_down(heap, 0)
  end
  top
end

def sift_down(heap, i)
  size = heap.size
  loop do
    left = i * 2 + 1
    right = left + 1
    largest = i
    largest = left if left < size && heap[left][0] > heap[largest][0]
    largest = right if right < size && heap[right][0] > heap[largest][0]
    break if largest == i
    heap[i], heap[largest] = heap[largest], heap[i]
    i = largest
  end
end
```

## Scala

```scala
object Solution {
    def maxAverageRatio(classes: Array[Array[Int]], extraStudents: Int): Double = {
        import java.util.PriorityQueue

        case class ClassInfo(var pass: Int, var total: Int)

        def gain(c: ClassInfo): Double = {
            (c.pass + 1).toDouble / (c.total + 1) - c.pass.toDouble / c.total
        }

        val pq = new PriorityQueue[ClassInfo](
            (a: ClassInfo, b: ClassInfo) => java.lang.Double.compare(gain(b), gain(a))
        )

        for (cls <- classes) {
            pq.offer(ClassInfo(cls(0), cls(1)))
        }

        var remaining = extraStudents
        while (remaining > 0) {
            val top = pq.poll()
            top.pass += 1
            top.total += 1
            pq.offer(top)
            remaining -= 1
        }

        var sum = 0.0
        while (!pq.isEmpty) {
            val c = pq.poll()
            sum += c.pass.toDouble / c.total
        }

        sum / classes.length
    }
}
```

## Rust

```rust
use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Clone)]
struct Item {
    gain: f64,
    p: i32,
    t: i32,
}

impl PartialEq for Item {
    fn eq(&self, other: &Self) -> bool {
        self.gain == other.gain
    }
}
impl Eq for Item {}

impl PartialOrd for Item {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        self.gain.partial_cmp(&other.gain)
    }
}

impl Ord for Item {
    fn cmp(&self, other: &Self) -> Ordering {
        // BinaryHeap is a max-heap; we want larger gain on top.
        self.partial_cmp(other).unwrap()
    }
}

pub struct Solution;

impl Solution {
    pub fn max_average_ratio(classes: Vec<Vec<i32>>, extra_students: i32) -> f64 {
        let mut heap = BinaryHeap::with_capacity(classes.len());
        for cls in classes.iter() {
            let p = cls[0];
            let t = cls[1];
            let gain = ((p + 1) as f64 / (t + 1) as f64) - (p as f64 / t as f64);
            heap.push(Item { gain, p, t });
        }

        let mut extra = extra_students;
        while extra > 0 {
            if let Some(mut top) = heap.pop() {
                top.p += 1;
                top.t += 1;
                top.gain = ((top.p + 1) as f64 / (top.t + 1) as f64) - (top.p as f64 / top.t as f64);
                heap.push(top);
            }
            extra -= 1;
        }

        let mut sum = 0.0_f64;
        while let Some(item) = heap.pop() {
            sum += item.p as f64 / item.t as f64;
        }

        sum / (classes.len() as f64)
    }
}
```

## Racket

```racket
(define/contract (max-average-ratio classes extraStudents)
  (-> (listof (listof exact-integer?)) exact-integer? flonum?)
  (let* ((n (length classes))
         (passes (make-vector n))
         (totals (make-vector n)))
    ;; initialize passes and totals vectors
    (for ([i (in-range n)] [cls classes])
      (vector-set! passes i (first cls))
      (vector-set! totals i (second cls)))
    ;; heap stores indices of classes
    (define heap (make-vector n))
    (for ([i (in-range n)])
      (vector-set! heap i i))
    ;; gain for a class index
    (define (gain-at idx)
      (let* ((p (vector-ref passes idx))
             (t (vector-ref totals idx)))
        (- (/ (+ p 1) (+ t 1)) (/ p t))))
    ;; sift‑down from position pos within heap size sz
    (define (sift-down pos sz)
      (let loop ()
        (let* ((left (+ (* 2 pos) 1))
               (right (+ left 1))
               (largest pos))
          (when (and (< left sz)
                     (> (gain-at (vector-ref heap left))
                        (gain-at (vector-ref heap largest))))
            (set! largest left))
          (when (and (< right sz)
                     (> (gain-at (vector-ref heap right))
                        (gain-at (vector-ref heap largest))))
            (set! largest right))
          (if (= largest pos)
              (void)
              (begin
                (let ((tmp (vector-ref heap pos)))
                  (vector-set! heap pos (vector-ref heap largest))
                  (vector-set! heap largest tmp))
                (set! pos largest)
                (loop))))))
    ;; sift‑up from position pos
    (define (sift-up pos)
      (let loop ()
        (if (= pos 0)
            (void)
            (let ((parent (quotient (- pos 1) 2)))
              (if (> (gain-at (vector-ref heap pos))
                     (gain-at (vector-ref heap parent)))
                  (begin
                    (let ((tmp (vector-ref heap pos)))
                      (vector-set! heap pos (vector-ref heap parent))
                      (vector-set! heap parent tmp))
                    (set! pos parent)
                    (loop))
                  (void))))))
    ;; build max‑heap
    (let ((start (sub1 (quotient n 2))))
      (let loop ((i start))
        (when (>= i 0)
          (sift-down i n)
          (loop (sub1 i)))))
    ;; distribute extra students
    (let loop ((k extraStudents))
      (when (> k 0)
        (let ((top-idx (vector-ref heap 0)))
          (vector-set! passes top-idx (+ (vector-ref passes top-idx) 1))
          (vector-set! totals top-idx (+ (vector-ref totals top-idx) 1))
          (sift-down 0 n)
          (loop (- k 1)))))
    ;; compute average pass ratio
    (let ((sum 0.0))
      (for ([i (in-range n)])
        (set! sum (+ sum (/ (vector-ref passes i) (vector-ref totals i)))))
      (/ sum n))))
```

## Erlang

```erlang
-spec max_average_ratio(Classes :: [[integer()]], ExtraStudents :: integer()) -> float().
max_average_ratio(Classes, ExtraStudents) ->
    Tree0 = build_tree(Classes, 0, gb_trees:empty()),
    FinalTree = assign_students(Tree0, ExtraStudents),
    SumRatio = gb_trees:fold(fun(_Key, {P,T}, Acc) -> Acc + P / T end, 0.0, FinalTree),
    SumRatio / length(Classes).

build_tree([], _Id, Tree) ->
    Tree;
build_tree([[P,T]|Rest], Id, Tree) ->
    Gain = ((P + 1) / (T + 1)) - (P / T),
    NewTree = gb_trees:insert({Gain, Id}, {P, T}, Tree),
    build_tree(Rest, Id + 1, NewTree).

assign_students(Tree, 0) ->
    Tree;
assign_students(Tree, K) ->
    {{Gain, Id}, {P,T}} = gb_trees:largest(Tree),
    Tree1 = gb_trees:delete({Gain, Id}, Tree),
    NewP = P + 1,
    NewT = T + 1,
    NewGain = ((NewP + 1) / (NewT + 1)) - (NewP / NewT),
    Tree2 = gb_trees:insert({NewGain, Id}, {NewP, NewT}, Tree1),
    assign_students(Tree2, K - 1).
```

## Elixir

```elixir
defmodule MaxHeap do
  @moduledoc false

  # Heap stored as {array, size}
  def new do
    {:array.new(0), 0}
  end

  def push({arr, size}, elem) do
    arr = :array.set(size, elem, arr)
    heap = {arr, size + 1}
    bubble_up(heap, size)
  end

  def pop_max({arr, size}) when size > 0 do
    max_elem = :array.get(0, arr)

    last_elem =
      if size - 1 == 0 do
        nil
      else
        :array.get(size - 1, arr)
      end

    arr = :array.set(0, last_elem, arr)
    heap = {arr, size - 1}
    heap = bubble_down(heap, 0)

    {max_elem, heap}
  end

  def size({_arr, size}), do: size

  # ----- internal helpers -----
  defp elem_greater({g1, _, _}, {g2, _, _}), do: g1 > g2

  defp bubble_up(heap = {_arr, _size}, idx) when idx > 0 do
    parent = div(idx - 1, 2)

    {arr, size} = heap
    cur = :array.get(idx, arr)
    par = :array.get(parent, arr)

    if elem_greater(cur, par) do
      arr = :array.set(idx, par, arr)
      arr = :array.set(parent, cur, arr)
      bubble_up({arr, size}, parent)
    else
      heap
    end
  end

  defp bubble_up(heap, _idx), do: heap

  defp bubble_down(heap = {arr, size}, idx) do
    left = idx * 2 + 1
    right = idx * 2 + 2
    largest = idx

    largest =
      if left < size do
        cur = :array.get(largest, arr)
        lval = :array.get(left, arr)

        if elem_greater(lval, cur), do: left, else: largest
      else
        largest
      end

    largest =
      if right < size do
        cur = :array.get(largest, arr)
        rval = :array.get(right, arr)

        if elem_greater(rval, cur), do: right, else: largest
      else
        largest
      end

    if largest != idx do
      a = :array.get(idx, arr)
      b = :array.get(largest, arr)
      arr = :array.set(idx, b, arr)
      arr = :array.set(largest, a, arr)
      bubble_down({arr, size}, largest)
    else
      heap
    end
  end
end

defmodule Solution do
  @spec max_average_ratio(classes :: [[integer]], extra_students :: integer) :: float
  def max_average_ratio(classes, extra_students) do
    # Build initial heap
    heap =
      Enum.reduce(classes, MaxHeap.new(), fn [p, t], acc ->
        gain = ((p + 1) / (t + 1)) - (p / t)
        MaxHeap.push(acc, {gain, p, t})
      end)

    # Distribute extra students
    final_heap =
      Enum.reduce(1..extra_students, heap, fn _, h ->
        {{_gain, p, t}, h_rest} = MaxHeap.pop_max(h)
        p_new = p + 1
        t_new = t + 1
        new_gain = ((p_new + 1) / (t_new + 1)) - (p_new / t_new)
        MaxHeap.push(h_rest, {new_gain, p_new, t_new})
      end)

    # Sum final ratios
    total_ratio =
      collect_ratios(final_heap, 0.0)

    total_ratio / length(classes)
  end

  defp collect_ratios(heap, acc) do
    case MaxHeap.size(heap) do
      0 -> acc
      _ ->
        {{_gain, p, t}, rest} = MaxHeap.pop_max(heap)
        collect_ratios(rest, acc + p / t)
    end
  end
end
```

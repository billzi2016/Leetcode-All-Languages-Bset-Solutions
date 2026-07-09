# 2558. Take Gifts From the Richest Pile

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<long long> pq;
        for (int g : gifts) pq.push(g);
        while (k--) {
            long long mx = pq.top();
            pq.pop();
            long long nxt = static_cast<long long>(sqrt((double)mx));
            pq.push(nxt);
        }
        long long ans = 0;
        while (!pq.empty()) {
            ans += pq.top();
            pq.pop();
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long pickGifts(int[] gifts, int k) {
        java.util.PriorityQueue<Integer> maxHeap = new java.util.PriorityQueue<>(java.util.Collections.reverseOrder());
        for (int g : gifts) {
            maxHeap.offer(g);
        }
        for (int i = 0; i < k; i++) {
            int top = maxHeap.poll();
            int reduced = (int) Math.sqrt(top);
            maxHeap.offer(reduced);
        }
        long total = 0L;
        while (!maxHeap.isEmpty()) {
            total += maxHeap.poll();
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        import heapq, math
        # max-heap using negative values
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            new_val = math.isqrt(largest)  # floor of sqrt
            heapq.heappush(max_heap, -new_val)
        return -sum(max_heap)
```

## Python3

```python
import math
import heapq
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # max-heap using negative values
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            reduced = math.isqrt(largest)  # floor of sqrt
            heapq.heappush(max_heap, -reduced)

        return -sum(max_heap)
```

## C

```c
#include <math.h>

static void maxHeapify(int *heap, int n, int i) {
    while (1) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && heap[l] > heap[largest]) largest = l;
        if (r < n && heap[r] > heap[largest]) largest = r;
        if (largest != i) {
            int tmp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = tmp;
            i = largest;
        } else {
            break;
        }
    }
}

static void buildMaxHeap(int *heap, int n) {
    for (int i = n / 2 - 1; i >= 0; --i) {
        maxHeapify(heap, n, i);
    }
}

long long pickGifts(int* gifts, int giftsSize, int k) {
    if (giftsSize == 0) return 0;
    buildMaxHeap(gifts, giftsSize);
    for (int step = 0; step < k; ++step) {
        int top = gifts[0];
        int newVal = (int)sqrt((double)top);
        gifts[0] = newVal;
        maxHeapify(gifts, giftsSize, 0);
    }
    long long sum = 0;
    for (int i = 0; i < giftsSize; ++i) {
        sum += (long long)gifts[i];
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public long PickGifts(int[] gifts, int k) {
        var pq = new System.Collections.Generic.PriorityQueue<int, int>();
        foreach (var g in gifts) {
            pq.Enqueue(g, -g); // use negative priority for max-heap behavior
        }

        for (int i = 0; i < k; i++) {
            int max = pq.Dequeue();
            int reduced = (int)Math.Floor(Math.Sqrt(max));
            pq.Enqueue(reduced, -reduced);
        }

        long total = 0;
        while (pq.Count > 0) {
            total += pq.Dequeue();
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} gifts
 * @param {number} k
 * @return {number}
 */
var pickGifts = function(gifts, k) {
    class MaxHeap {
        constructor(arr = []) {
            this.data = arr.slice();
            if (this.data.length > 0) this.heapify();
        }
        heapify() {
            for (let i = Math.floor((this.data.length - 2) / 2); i >= 0; i--) {
                this.siftDown(i);
            }
        }
        push(val) {
            this.data.push(val);
            this.siftUp(this.data.length - 1);
        }
        pop() {
            if (this.data.length === 0) return undefined;
            const root = this.data[0];
            const last = this.data.pop();
            if (this.data.length > 0) {
                this.data[0] = last;
                this.siftDown(0);
            }
            return root;
        }
        siftUp(idx) {
            while (idx > 0) {
                const parent = Math.floor((idx - 1) / 2);
                if (this.data[parent] >= this.data[idx]) break;
                [this.data[parent], this.data[idx]] = [this.data[idx], this.data[parent]];
                idx = parent;
            }
        }
        siftDown(idx) {
            const n = this.data.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let largest = idx;
                if (left < n && this.data[left] > this.data[largest]) largest = left;
                if (right < n && this.data[right] > this.data[largest]) largest = right;
                if (largest === idx) break;
                [this.data[idx], this.data[largest]] = [this.data[largest], this.data[idx]];
                idx = largest;
            }
        }
    }

    const heap = new MaxHeap(gifts);
    for (let i = 0; i < k; ++i) {
        const maxVal = heap.pop();
        const reduced = Math.floor(Math.sqrt(maxVal));
        heap.push(reduced);
    }
    let total = 0;
    for (const v of heap.data) total += v;
    return total;
};
```

## Typescript

```typescript
function pickGifts(gifts: number[], k: number): number {
    class MaxHeap {
        data: number[] = [];
        constructor(arr?: number[]) {
            if (arr) {
                for (const v of arr) this.push(v);
            }
        }
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
            if (a.length === 0) return 0;
            const top = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        largest = i;
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

    const heap = new MaxHeap(gifts);
    for (let i = 0; i < k; ++i) {
        const maxVal = heap.pop();
        heap.push(Math.floor(Math.sqrt(maxVal)));
    }
    let sum = 0;
    for (const v of heap.data) sum += v;
    return sum;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $gifts
     * @param Integer $k
     * @return Integer
     */
    function pickGifts($gifts, $k) {
        $heap = new SplMaxHeap();
        foreach ($gifts as $gift) {
            $heap->insert($gift);
        }
        for ($i = 0; $i < $k; $i++) {
            if ($heap->isEmpty()) break;
            $max = $heap->extract();
            $new = (int) floor(sqrt($max));
            $heap->insert($new);
        }
        $sum = 0;
        while (!$heap->isEmpty()) {
            $sum += $heap->extract();
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func pickGifts(_ gifts: [Int], _ k: Int) -> Int {
        var heap = MaxHeap(gifts)
        for _ in 0..<k {
            guard let maxVal = heap.pop() else { break }
            let newVal = Int(Double(maxVal).squareRoot())
            heap.push(newVal)
        }
        var total = 0
        while let val = heap.pop() {
            total += val
        }
        return total
    }
}

struct MaxHeap {
    private var data: [Int] = []
    
    init(_ elements: [Int]) {
        data = elements
        if !data.isEmpty {
            for i in stride(from: (data.count / 2) - 1, through: 0, by: -1) {
                siftDown(i)
            }
        }
    }
    
    mutating func push(_ value: Int) {
        data.append(value)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Int? {
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
        var parent = (child - 1) / 2
        while child > 0 && data[child] > data[parent] {
            data.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private mutating func siftDown(_ index: Int) {
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
```

## Kotlin

```kotlin
class Solution {
    fun pickGifts(gifts: IntArray, k: Int): Long {
        val maxHeap = java.util.PriorityQueue<Int>(compareByDescending { it })
        for (g in gifts) {
            maxHeap.add(g)
        }
        repeat(k) {
            val cur = maxHeap.poll()
            val reduced = kotlin.math.sqrt(cur.toDouble()).toInt()
            maxHeap.offer(reduced)
        }
        var total = 0L
        while (maxHeap.isNotEmpty()) {
            total += maxHeap.poll().toLong()
        }
        return total
    }
}
```

## Dart

```dart
import 'dart:math';
import 'dart:collection';

class Solution {
  int pickGifts(List<int> gifts, int k) {
    var maxHeap = HeapPriorityQueue<int>((a, b) => b.compareTo(a));
    for (var g in gifts) {
      maxHeap.add(g);
    }
    for (int i = 0; i < k; i++) {
      int largest = maxHeap.removeFirst();
      maxHeap.add(sqrt(largest).floor());
    }
    int total = 0;
    while (maxHeap.isNotEmpty) {
      total += maxHeap.removeFirst();
    }
    return total;
  }
}
```

## Golang

```go
import (
	"container/heap"
	"math"
)

type maxHeap []int

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i] > h[j] } // max‑heap
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func pickGifts(gifts []int, k int) int64 {
	h := maxHeap(gifts)
	heap.Init(&h)

	for i := 0; i < k; i++ {
		maxVal := heap.Pop(&h).(int)
		newVal := int(math.Sqrt(float64(maxVal)))
		heap.Push(&h, newVal)
	}

	var sum int64
	for _, v := range h {
		sum += int64(v)
	}
	return sum
}
```

## Ruby

```ruby
def pick_gifts(gifts, k)
  k.times do
    max_val = -1
    max_idx = 0
    gifts.each_with_index do |v, i|
      if v > max_val
        max_val = v
        max_idx = i
      end
    end
    gifts[max_idx] = Math.sqrt(max_val).floor
  end
  gifts.sum
end
```

## Scala

```scala
object Solution {
    def pickGifts(gifts: Array[Int], k: Int): Long = {
        val pq = scala.collection.mutable.PriorityQueue.empty[Int]
        pq.enqueue(gifts: _*)
        var steps = 0
        while (steps < k) {
            val maxVal = pq.dequeue()
            val reduced = Math.sqrt(maxVal.toDouble).toInt
            pq.enqueue(reduced)
            steps += 1
        }
        var total: Long = 0L
        while (pq.nonEmpty) {
            total += pq.dequeue().toLong
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn pick_gifts(gifts: Vec<i32>, k: i32) -> i64 {
        use std::collections::BinaryHeap;
        let mut heap = BinaryHeap::from(gifts);
        for _ in 0..k {
            if let Some(max_val) = heap.pop() {
                let new_val = (max_val as f64).sqrt().floor() as i32;
                heap.push(new_val);
            }
        }
        let mut sum: i64 = 0;
        while let Some(v) = heap.pop() {
            sum += v as i64;
        }
        sum
    }
}
```

## Racket

```racket
(define/contract (pick-gifts gifts k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length gifts)]
         [v (list->vector gifts)])
    (for ([iter (in-range k)])
      (define max-idx 0)
      (for ([i (in-range n)])
        (when (> (vector-ref v i) (vector-ref v max-idx))
          (set! max-idx i)))
      (define val (vector-ref v max-idx))
      (define new-val (inexact->exact (floor (sqrt val))))
      (vector-set! v max-idx new-val))
    (for/sum ([i (in-range n)]) (vector-ref v i))))
```

## Erlang

```erlang
-spec pick_gifts(Gifts :: [integer()], K :: integer()) -> integer().
pick_gifts(Gifts, K) ->
    Updated = do_k_times(Gifts, K),
    lists:sum(Updated).

do_k_times(Gifts, 0) -> Gifts;
do_k_times(Gifts, K) when K > 0 ->
    NewGifts = replace_max(Gifts),
    do_k_times(NewGifts, K - 1).

replace_max(Gifts) ->
    Max = lists:max(Gifts),
    NewVal = trunc(math:sqrt(Max)),
    replace_first(Gifts, Max, NewVal).

replace_first([H|T], Old, New) when H == Old -> [New|T];
replace_first([H|T], Old, New) -> [H|replace_first(T, Old, New)].
```

## Elixir

```elixir
defmodule Solution do
  @spec pick_gifts(gifts :: [integer], k :: integer) :: integer
  def pick_gifts(gifts, k) do
    do_pick(gifts, k)
  end

  defp do_pick(gifts, 0), do: Enum.sum(gifts)

  defp do_pick(gifts, k) when k > 0 do
    {max_val, idx} =
      gifts
      |> Enum.with_index()
      |> Enum.max_by(fn {v, _i} -> v end)

    new_val = :math.sqrt(max_val) |> trunc()
    new_gifts = List.replace_at(gifts, idx, new_val)
    do_pick(new_gifts, k - 1)
  end
end
```

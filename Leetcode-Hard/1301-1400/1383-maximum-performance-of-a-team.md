# 1383. Maximum Performance of a Team

## Cpp

```cpp
class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        const long long MOD = 1'000'000'007LL;
        vector<pair<int,int>> eng(n);
        for (int i = 0; i < n; ++i) eng[i] = {efficiency[i], speed[i]};
        sort(eng.begin(), eng.end(), [](const auto& a, const auto& b){
            return a.first > b.first; // descending efficiency
        });
        
        priority_queue<int, vector<int>, greater<int>> minHeap;
        long long sumSpeed = 0;
        long long best = 0;
        
        for (auto& e : eng) {
            int eff = e.first;
            int spd = e.second;
            
            if ((int)minHeap.size() == k) {
                // heap already full, will replace smallest if current speed is larger
                if (!minHeap.empty() && spd > minHeap.top()) {
                    sumSpeed -= minHeap.top();
                    minHeap.pop();
                    minHeap.push(spd);
                    sumSpeed += spd;
                }
            } else {
                minHeap.push(spd);
                sumSpeed += spd;
            }
            
            long long perf = sumSpeed * (long long)eff;
            if (perf > best) best = perf;
        }
        
        return (int)(best % MOD);
    }
};
```

## Java

```java
class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        int MOD = 1_000_000_007;
        // Pair of efficiency and speed
        int[][] engineers = new int[n][2];
        for (int i = 0; i < n; i++) {
            engineers[i][0] = efficiency[i];
            engineers[i][1] = speed[i];
        }
        // Sort by decreasing efficiency
        java.util.Arrays.sort(engineers, (a, b) -> b[0] - a[0]);
        
        java.util.PriorityQueue<Integer> minSpeedHeap = new java.util.PriorityQueue<>();
        long sumSpeeds = 0;
        long maxPerf = 0;
        
        for (int[] eng : engineers) {
            int eff = eng[0];
            int spd = eng[1];
            
            // Add current speed
            sumSpeeds += spd;
            minSpeedHeap.offer(spd);
            
            // If we exceed k, remove smallest speed
            if (minSpeedHeap.size() > k) {
                sumSpeeds -= minSpeedHeap.poll();
            }
            
            long perf = sumSpeeds * eff;
            if (perf > maxPerf) {
                maxPerf = perf;
            }
        }
        
        return (int)(maxPerf % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True)  # sort by decreasing efficiency

        import heapq
        speed_heap = []          # min-heap to keep the smallest speeds
        speed_sum = 0
        max_perf = 0

        for eff, spd in engineers:
            if len(speed_heap) == k:
                # remove the engineer with the smallest speed to make room
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, spd)
            speed_sum += spd
            max_perf = max(max_perf, speed_sum * eff)

        return max_perf % MOD
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        sum_speed = 0
        best = 0

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            sum_speed += spd
            if len(speed_heap) > k:
                removed = heapq.heappop(speed_heap)
                sum_speed -= removed
            performance = sum_speed * eff
            if performance > best:
                best = performance

        return best % MOD
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

struct Engineer {
    int speed;
    int eff;
};

static int cmpEng(const void *a, const void *b) {
    const struct Engineer *ea = (const struct Engineer *)a;
    const struct Engineer *eb = (const struct Engineer *)b;
    return eb->eff - ea->eff;  // descending efficiency
}

static void heapPush(int *heap, int *size, int val) {
    (*size)++;
    int i = *size;
    heap[i] = val;
    while (i > 1 && heap[i / 2] > heap[i]) {
        int tmp = heap[i];
        heap[i] = heap[i / 2];
        heap[i / 2] = tmp;
        i /= 2;
    }
}

static int heapPop(int *heap, int *size) {
    int root = heap[1];
    heap[1] = heap[*size];
    (*size)--;
    int i = 1;
    while (1) {
        int left = i * 2, right = i * 2 + 1, smallest = i;
        if (left <= *size && heap[left] < heap[smallest]) smallest = left;
        if (right <= *size && heap[right] < heap[smallest]) smallest = right;
        if (smallest == i) break;
        int tmp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = tmp;
        i = smallest;
    }
    return root;
}

int maxPerformance(int n, int* speed, int speedSize, int* efficiency, int efficiencySize, int k) {
    struct Engineer *eng = (struct Engineer *)malloc(n * sizeof(struct Engineer));
    for (int i = 0; i < n; ++i) {
        eng[i].speed = speed[i];
        eng[i].eff = efficiency[i];
    }
    qsort(eng, n, sizeof(struct Engineer), cmpEng);

    int *heap = (int *)malloc((n + 1) * sizeof(int)); // 1-indexed min-heap
    int heapSize = 0;
    long long sumSpeeds = 0;
    long long maxPerf = 0;

    for (int i = 0; i < n; ++i) {
        heapPush(heap, &heapSize, eng[i].speed);
        sumSpeeds += eng[i].speed;

        if (heapSize > k) {
            int removed = heapPop(heap, &heapSize);
            sumSpeeds -= removed;
        }

        long long perf = sumSpeeds * (long long)eng[i].eff;
        if (perf > maxPerf) maxPerf = perf;
    }

    free(eng);
    free(heap);
    return (int)(maxPerf % MOD);
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxPerformance(int n, int[] speed, int[] efficiency, int k)
    {
        const long MOD = 1_000_000_007L;
        var engineers = new (int eff, int sp)[n];
        for (int i = 0; i < n; i++)
            engineers[i] = (efficiency[i], speed[i]);

        Array.Sort(engineers, (a, b) => b.eff.CompareTo(a.eff)); // descending efficiency

        long sumSpeed = 0;
        long maxPerf = 0;
        var pq = new PriorityQueue<int, int>(); // min-heap based on speed as priority

        foreach (var eng in engineers)
        {
            pq.Enqueue(eng.sp, eng.sp);
            sumSpeed += eng.sp;

            if (pq.Count > k)
                sumSpeed -= pq.Dequeue(); // remove smallest speed

            long perf = sumSpeed * eng.eff;
            if (perf > maxPerf)
                maxPerf = perf;
        }

        return (int)(maxPerf % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} speed
 * @param {number[]} efficiency
 * @param {number} k
 * @return {number}
 */
var maxPerformance = function(n, speed, efficiency, k) {
    const MOD = 1000000007n;

    // Pair each engineer's efficiency with speed
    const engineers = [];
    for (let i = 0; i < n; ++i) {
        engineers.push({eff: efficiency[i], sp: speed[i]});
    }
    // Sort by decreasing efficiency
    engineers.sort((a, b) => b.eff - a.eff);

    // Min-heap for speeds
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
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
                    let l = i * 2 + 1, r = l + 1, smallest = i;
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

    const heap = new MinHeap();
    let sumSpeed = 0;          // Number, safe up to 1e10
    let maxPerf = 0n;          // BigInt

    for (const eng of engineers) {
        sumSpeed += eng.sp;
        heap.push(eng.sp);
        if (heap.size() > k) {
            const removed = heap.pop();
            sumSpeed -= removed;
        }
        const perf = (BigInt(sumSpeed) * BigInt(eng.eff)) % MOD;
        if (perf > maxPerf) maxPerf = perf;
    }

    return Number(maxPerf);
};
```

## Typescript

```typescript
function maxPerformance(n: number, speed: number[], efficiency: number[], k: number): number {
    const MOD = 1000000007n;
    
    // Pair each engineer's efficiency with speed
    const engineers: {eff: number, spd: number}[] = [];
    for (let i = 0; i < n; ++i) {
        engineers.push({eff: efficiency[i], spd: speed[i]});
    }
    // Sort by decreasing efficiency
    engineers.sort((a, b) => b.eff - a.eff);
    
    class MinHeap {
        private heap: number[] = [];
        size(): number { return this.heap.length; }
        push(val: number): void {
            let i = this.heap.length;
            this.heap.push(val);
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.heap[p] <= this.heap[i]) break;
                [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
                i = p;
            }
        }
        pop(): number | undefined {
            if (this.heap.length === 0) return undefined;
            const root = this.heap[0];
            const last = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = last;
                let i = 0;
                while (true) {
                    const left = i * 2 + 1;
                    const right = i * 2 + 2;
                    let smallest = i;
                    if (left < this.heap.length && this.heap[left] < this.heap[smallest]) smallest = left;
                    if (right < this.heap.length && this.heap[right] < this.heap[smallest]) smallest = right;
                    if (smallest === i) break;
                    [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
                    i = smallest;
                }
            }
            return root;
        }
    }
    
    const heap = new MinHeap();
    let sumSpeed = 0; // safe within Number range
    let maxPerf = 0n;
    
    for (const eng of engineers) {
        heap.push(eng.spd);
        sumSpeed += eng.spd;
        if (heap.size() > k) {
            const removed = heap.pop()!;
            sumSpeed -= removed;
        }
        const perf = BigInt(sumSpeed) * BigInt(eng.eff);
        if (perf > maxPerf) maxPerf = perf;
    }
    
    return Number(maxPerf % MOD);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $speed
     * @param Integer[] $efficiency
     * @param Integer $k
     * @return Integer
     */
    function maxPerformance($n, $speed, $efficiency, $k) {
        $MOD = 1000000007;
        $engineers = [];
        for ($i = 0; $i < $n; $i++) {
            $engineers[] = [$efficiency[$i], $speed[$i]];
        }
        usort($engineers, function($a, $b) {
            return $b[0] <=> $a[0]; // descending efficiency
        });

        $heap = new SplMinHeap(); // min-heap for speeds
        $sumSpeed = 0;
        $maxPerf = 0;

        foreach ($engineers as $e) {
            [$eff, $spd] = $e;
            $heap->insert($spd);
            $sumSpeed += $spd;

            if ($heap->count() > $k) {
                $removed = $heap->extract(); // remove smallest speed
                $sumSpeed -= $removed;
            }

            $perf = ($sumSpeed * $eff) % $MOD;
            if ($perf > $maxPerf) {
                $maxPerf = $perf;
            }
        }

        return $maxPerf % $MOD;
    }
}
```

## Swift

```swift
import Foundation

struct MinHeap<T> {
    private var elements: [T] = []
    private let areInIncreasingOrder: (T, T) -> Bool
    
    init(sort: @escaping (T, T) -> Bool) {
        self.areInIncreasingOrder = sort
    }
    
    var count: Int { elements.count }
    
    mutating func push(_ value: T) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    mutating func pop() -> T? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let value = elements[0]
            elements[0] = elements.removeLast()
            siftDown(from: 0)
            return value
        }
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && areInIncreasingOrder(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            
            if left < elements.count && areInIncreasingOrder(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && areInIncreasingOrder(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

class Solution {
    private let MOD: Int64 = 1_000_000_007
    
    func maxPerformance(_ n: Int, _ speed: [Int], _ efficiency: [Int], _ k: Int) -> Int {
        var engineers: [(eff: Int, spd: Int)] = []
        engineers.reserveCapacity(n)
        for i in 0..<n {
            engineers.append((efficiency[i], speed[i]))
        }
        // Sort by decreasing efficiency
        engineers.sort { $0.eff > $1.eff }
        
        var heap = MinHeap<Int>(sort: <) // min-heap based on speed
        var sumSpeed: Int64 = 0
        var best: Int64 = 0
        
        for eng in engineers {
            heap.push(eng.spd)
            sumSpeed += Int64(eng.spd)
            
            if heap.count > k, let removed = heap.pop() {
                sumSpeed -= Int64(removed)
            }
            
            let performance = sumSpeed * Int64(eng.eff)
            if performance > best {
                best = performance
            }
        }
        
        return Int(best % MOD)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPerformance(n: Int, speed: IntArray, efficiency: IntArray, k: Int): Int {
        val engineers = ArrayList<Pair<Int, Int>>(n)
        for (i in 0 until n) {
            engineers.add(Pair(speed[i], efficiency[i]))
        }
        engineers.sortWith { a, b -> b.second - a.second } // sort by efficiency descending

        val minHeap = java.util.PriorityQueue<Int>() // speeds
        var speedSum = 0L
        var maxPerf = 0L
        val MOD = 1_000_000_007L

        for ((sp, ef) in engineers) {
            minHeap.add(sp)
            speedSum += sp.toLong()
            if (minHeap.size > k) {
                speedSum -= minHeap.poll().toLong()
            }
            val curPerf = speedSum * ef.toLong()
            if (curPerf > maxPerf) {
                maxPerf = curPerf
            }
        }
        return (maxPerf % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int maxPerformance(int n, List<int> speed, List<int> efficiency, int k) {
    // Pair each engineer's efficiency with its speed.
    List<List<int>> engineers = List.generate(
        n, (i) => [efficiency[i], speed[i]],
        growable: false);
    // Sort by decreasing efficiency.
    engineers.sort((a, b) => b[0].compareTo(a[0]));

    final _MinHeap heap = _MinHeap();
    int sumSpeed = 0;
    int best = 0;

    for (var eng in engineers) {
      int eff = eng[0];
      int spd = eng[1];

      heap.add(spd);
      sumSpeed += spd;

      if (heap.size > k) {
        sumSpeed -= heap.pop();
      }

      int perf = ((sumSpeed * eff) % _mod).toInt();
      if (perf > best) best = perf;
    }
    return best;
  }
}

class _MinHeap {
  final List<int> _data = [];

  int get size => _data.length;

  void add(int value) {
    _data.add(value);
    _siftUp(_data.length - 1);
  }

  int pop() {
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
      if (_data[parent] <= _data[idx]) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    int n = _data.length;
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
    int tmp = _data[i];
    _data[i] = _data[j];
    _data[j] = tmp;
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

type engineer struct {
	speed     int
	efficiency int
}

type minHeap []int

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i] < h[j] } // min-heap
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxPerformance(n int, speed []int, efficiency []int, k int) int {
	const mod int64 = 1_000_000_007

	eng := make([]engineer, n)
	for i := 0; i < n; i++ {
		eng[i] = engineer{speed: speed[i], efficiency: efficiency[i]}
	}
	sort.Slice(eng, func(i, j int) bool {
		return eng[i].efficiency > eng[j].efficiency
	})

	h := &minHeap{}
	heap.Init(h)
	var sumSpeeds int64
	var best int64

	for _, e := range eng {
		heap.Push(h, e.speed)
		sumSpeeds += int64(e.speed)

		if h.Len() > k {
			removed := heap.Pop(h).(int)
			sumSpeeds -= int64(removed)
		}

		perf := sumSpeeds * int64(e.efficiency)
		if perf > best {
			best = perf
		}
	}

	return int(best % mod)
}
```

## Ruby

```ruby
def max_performance(n, speed, efficiency, k)
  engineers = []
  n.times do |i|
    engineers << [efficiency[i], speed[i]]
  end
  engineers.sort_by! { |e| -e[0] }

  heap = []            # min‑heap of speeds
  sum_speed = 0
  max_perf = 0
  mod = 1_000_000_007

  engineers.each do |eff, sp|
    # push speed into min‑heap
    heap << sp
    idx = heap.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      break if heap[parent] <= heap[idx]
      heap[parent], heap[idx] = heap[idx], heap[parent]
      idx = parent
    end
    sum_speed += sp

    # keep at most k speeds
    if heap.size > k
      min_val = heap[0]
      last = heap.pop
      unless heap.empty?
        heap[0] = last
        i = 0
        size = heap.size
        loop do
          left = i * 2 + 1
          right = left + 1
          break if left >= size
          smallest = left
          smallest = right if right < size && heap[right] < heap[left]
          break if heap[i] <= heap[smallest]
          heap[i], heap[smallest] = heap[smallest], heap[i]
          i = smallest
        end
      end
      sum_speed -= min_val
    end

    perf = sum_speed * eff
    max_perf = perf if perf > max_perf
  end

  max_perf % mod
end
```

## Scala

```scala
object Solution {
  def maxPerformance(n: Int, speed: Array[Int], efficiency: Array[Int], k: Int): Int = {
    val engineers = (0 until n).map(i => (efficiency(i), speed(i))).sortBy(-_._1)
    val pq = new java.util.PriorityQueue[Int]()
    var sumSpeed: Long = 0L
    var maxPerf: Long = 0L
    val mod = 1000000007L

    for ((eff, sp) <- engineers) {
      sumSpeed += sp
      pq.add(sp)
      if (pq.size() > k) {
        sumSpeed -= pq.poll()
      }
      val perf = sumSpeed * eff
      if (perf > maxPerf) maxPerf = perf
    }

    (maxPerf % mod).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_performance(n: i32, speed: Vec<i32>, efficiency: Vec<i32>, k: i32) -> i32 {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let mod_val: i64 = 1_000_000_007;
        let mut engineers: Vec<(i32, i32)> = (0..n as usize)
            .map(|i| (efficiency[i], speed[i]))
            .collect();
        // Sort by decreasing efficiency
        engineers.sort_by(|a, b| b.0.cmp(&a.0));

        let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new(); // min-heap for speeds
        let mut sum_speed: i64 = 0;
        let mut max_perf: i64 = 0;
        let limit = k as usize;

        for (eff, spd) in engineers {
            let spd_i64 = spd as i64;
            heap.push(Reverse(spd_i64));
            sum_speed += spd_i64;

            if heap.len() > limit {
                if let Some(Reverse(rem)) = heap.pop() {
                    sum_speed -= rem;
                }
            }

            let perf = sum_speed * (eff as i64);
            if perf > max_perf {
                max_perf = perf;
            }
        }

        (max_perf % mod_val) as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define/contract (max-performance n speed efficiency k)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([MOD 1000000007]
         [engineers (for/list ([e (in-list efficiency)] [s (in-list speed)]) (cons e s))]
         [sorted (sort engineers > #:key car)])
    (define sum 0)
    (define best 0)
    (define heap (make-heap <))
    (for ([eng sorted])
      (define eff (car eng))
      (define spd (cdr eng))
      (heap-push! heap spd)
      (set! sum (+ sum spd))
      (when (> (heap-size heap) k)
        (define removed (heap-pop! heap))
        (set! sum (- sum removed)))
      (define perf (* sum eff))
      (when (> perf best) (set! best perf)))
    (modulo best MOD)))
```

## Erlang

```erlang
-spec max_performance(N :: integer(), Speed :: [integer()], Efficiency :: [integer()], K :: integer()) -> integer().
max_performance(_N, Speed, Efficiency, K) ->
    Mod = 1000000007,
    Engineers = lists:map(
        fun({Sp, Ef}) -> {Ef, Sp} end,
        lists:zip(Speed, Efficiency)
    ),
    Sorted = lists:sort(fun({E1,_}, {E2,_}) -> E1 > E2 end, Engineers),
    {MaxPerf, _Sum, _Size, _Tree, _Id} =
        lists:foldl(
            fun({Eff, Sp},
                {CurMax, Sum, Size, Tree, Id}) ->
                NewId = Id + 1,
                NewTree0 = gb_trees:insert({Sp, NewId}, true, Tree),
                NewSum0 = Sum + Sp,
                NewSize0 = Size + 1,
                {NewTree, NewSum, NewSize} =
                    if
                        NewSize0 > K ->
                            Iter = gb_trees:iterator(NewTree0),
                            {MinKey, _} = gb_trees:next(Iter),
                            {MinSp, _MinId} = MinKey,
                            Tree2 = gb_trees:delete(MinKey, NewTree0),
                            {Tree2, NewSum0 - MinSp, NewSize0 - 1};
                        true ->
                            {NewTree0, NewSum0, NewSize0}
                    end,
                Perf = NewSum * Eff,
                MaxVal = if Perf > CurMax -> Perf; true -> CurMax end,
                {MaxVal, NewSum, NewSize, NewTree, NewId}
            end,
            {0, 0, 0, gb_trees:empty(), 0},
            Sorted),
    MaxPerf rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  defmodule MinHeap do
    defstruct size: 0, data: nil

    def new() do
      %MinHeap{size: 0, data: :array.new()}
    end

    def push(%MinHeap{size: sz, data: arr} = heap, val) do
      new_sz = sz + 1
      arr2 = :array.set(new_sz, val, arr)
      heap2 = %MinHeap{heap | size: new_sz, data: arr2}
      bubble_up(heap2, new_sz)
    end

    defp bubble_up(%MinHeap{size: _sz, data: arr} = heap, i) when i > 1 do
      parent = div(i, 2)

      cur = :array.get(i, arr)
      par_val = :array.get(parent, arr)

      if cur < par_val do
        arr_swapped =
          arr
          |> :array.set(i, par_val)
          |> :array.set(parent, cur)

        heap_swapped = %MinHeap{heap | data: arr_swapped}
        bubble_up(heap_swapped, parent)
      else
        heap
      end
    end

    defp bubble_up(heap, _i), do: heap

    def pop_min(%MinHeap{size: sz, data: arr} = heap) when sz > 0 do
      min = :array.get(1, arr)

      if sz == 1 do
        {%MinHeap{heap | size: 0}, min}
      else
        last_val = :array.get(sz, arr)
        arr2 = :array.set(1, last_val, arr)
        heap2 = %MinHeap{heap | size: sz - 1, data: arr2}
        {bubble_down(heap2, 1), min}
      end
    end

    defp bubble_down(%MinHeap{size: sz, data: arr} = heap, i) do
      left = i * 2
      right = left + 1

      smallest =
        cond do
          left <= sz and :array.get(left, arr) < :array.get(i, arr) -> left
          true -> i
        end

      smallest =
        if right <= sz and :array.get(right, arr) < :array.get(smallest, arr) do
          right
        else
          smallest
        end

      if smallest != i do
        val_i = :array.get(i, arr)
        val_s = :array.get(smallest, arr)

        arr2 =
          arr
          |> :array.set(i, val_s)
          |> :array.set(smallest, val_i)

        heap2 = %MinHeap{heap | data: arr2}
        bubble_down(heap2, smallest)
      else
        heap
      end
    end
  end

  @spec max_performance(n :: integer, speed :: [integer], efficiency :: [integer], k :: integer) :: integer
  def max_performance(_n, speed, efficiency, k) do
    mod = 1_000_000_007

    engineers =
      Enum.zip(efficiency, speed)
      |> Enum.sort_by(fn {e, _} -> -e end)

    {_, _, best} =
      Enum.reduce(engineers, {MinHeap.new(), 0, 0}, fn {eff, sp},
                                                    {heap, sum_sp, cur_best} ->
        heap1 = MinHeap.push(heap, sp)
        sum1 = sum_sp + sp

        {heap2, sum2} =
          if heap1.size > k do
            {new_heap, removed} = MinHeap.pop_min(heap1)
            {new_heap, sum1 - removed}
          else
            {heap1, sum1}
          end

        perf = sum2 * eff
        new_best = if perf > cur_best, do: perf, else: cur_best
        {heap2, sum2, new_best}
      end)

    rem(best, mod)
  end
end
```

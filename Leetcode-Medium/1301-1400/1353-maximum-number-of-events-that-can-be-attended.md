# 1353. Maximum Number of Events That Can Be Attended

## Cpp

```cpp
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        if (events.empty()) return 0;
        sort(events.begin(), events.end()); // sort by start day, then end day
        int n = events.size();
        int idx = 0;
        int maxDay = 0;
        for (auto& e : events) maxDay = max(maxDay, e[1]);
        
        priority_queue<int, vector<int>, greater<int>> minHeap; // stores end days
        int attended = 0;
        
        for (int day = 1; day <= maxDay; ++day) {
            while (idx < n && events[idx][0] <= day) {
                minHeap.push(events[idx][1]);
                ++idx;
            }
            while (!minHeap.empty() && minHeap.top() < day) {
                minHeap.pop(); // event already expired
            }
            if (!minHeap.empty()) {
                minHeap.pop(); // attend the event with earliest end day
                ++attended;
            }
        }
        return attended;
    }
};
```

## Java

```java
class Solution {
    public int maxEvents(int[][] events) {
        int n = events.length;
        // Find the maximum ending day
        int maxDay = 0;
        for (int[] e : events) {
            if (e[1] > maxDay) maxDay = e[1];
        }
        // Sort events by start day
        java.util.Arrays.sort(events, (a, b) -> a[0] - b[0]);
        java.util.PriorityQueue<Integer> pq = new java.util.PriorityQueue<>();
        int idx = 0, attended = 0;
        for (int day = 1; day <= maxDay; day++) {
            // Add all events that start on or before current day
            while (idx < n && events[idx][0] <= day) {
                pq.offer(events[idx][1]);
                idx++;
            }
            // Remove events that have already ended
            while (!pq.isEmpty() && pq.peek() < day) {
                pq.poll();
            }
            // Attend the event that ends earliest
            if (!pq.isEmpty()) {
                pq.poll();
                attended++;
            }
        }
        return attended;
    }
}
```

## Python

```python
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        import heapq
        events.sort(key=lambda x: x[0])
        i, n = 0, len(events)
        day = 0
        attended = 0
        minheap = []
        while i < n or minheap:
            if not minheap:
                day = max(day, events[i][0])
            while i < n and events[i][0] <= day:
                heapq.heappush(minheap, events[i][1])
                i += 1
            while minheap and minheap[0] < day:
                heapq.heappop(minheap)
            if minheap:
                heapq.heappop(minheap)
                attended += 1
                day += 1
        return attended
```

## Python3

```python
class Solution:
    def maxEvents(self, events):
        import heapq
        events.sort(key=lambda x: x[0])
        n = len(events)
        i = 0
        res = 0
        day = 1
        if not events:
            return 0
        max_day = max(e[1] for e in events)
        min_heap = []
        while day <= max_day:
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                res += 1
            day += 1
        return res
```

## C

```c
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Event;

static int cmpEvent(const void *a, const void *b) {
    const Event *ea = (const Event *)a;
    const Event *eb = (const Event *)b;
    if (ea->start != eb->start)
        return ea->start - eb->start;
    return ea->end - eb->end;
}

/* min-heap for end days */
static void heapPush(int *heap, int *size, int val) {
    int i = (*size)++;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p] <= val) break;
        heap[i] = heap[p];
        i = p;
    }
    heap[i] = val;
}

static int heapTop(int *heap, int size) {
    return heap[0];
}

static void heapPop(int *heap, int *size) {
    int n = --(*size);
    if (n == 0) return;
    int last = heap[n];
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        if (l >= n) break;
        int r = l + 1;
        int child = (r < n && heap[r] < heap[l]) ? r : l;
        if (heap[child] >= last) break;
        heap[i] = heap[child];
        i = child;
    }
    heap[i] = last;
}

int maxEvents(int** events, int eventsSize, int* eventsColSize){
    if (eventsSize == 0) return 0;

    Event *ev = (Event *)malloc(sizeof(Event) * eventsSize);
    for (int i = 0; i < eventsSize; ++i) {
        ev[i].start = events[i][0];
        ev[i].end   = events[i][1];
    }
    qsort(ev, eventsSize, sizeof(Event), cmpEvent);

    int *heap = (int *)malloc(sizeof(int) * (eventsSize + 5));
    int heapSize = 0;
    int i = 0;               // index in sorted events
    int day = 1;
    int attended = 0;

    while (i < eventsSize || heapSize > 0) {
        if (heapSize == 0 && i < eventsSize && day < ev[i].start)
            day = ev[i].start;   // jump to next start day

        while (i < eventsSize && ev[i].start <= day) {
            heapPush(heap, &heapSize, ev[i].end);
            ++i;
        }

        while (heapSize > 0 && heapTop(heap, heapSize) < day)
            heapPop(heap, &heapSize);

        if (heapSize > 0) {
            /* attend event with earliest end */
            heapPop(heap, &heapSize);
            ++attended;
            ++day;
        }
    }

    free(ev);
    free(heap);
    return attended;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxEvents(int[][] events) {
        Array.Sort(events, (a, b) => {
            if (a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        });

        var pq = new PriorityQueue<int, int>();
        int i = 0, day = 0, attended = 0;
        int n = events.Length;

        while (i < n || pq.Count > 0) {
            if (pq.Count == 0) {
                day = events[i][0];
            }

            while (i < n && events[i][0] <= day) {
                pq.Enqueue(events[i][1], events[i][1]);
                i++;
            }

            while (pq.Count > 0 && pq.Peek() < day) {
                pq.Dequeue();
            }

            if (pq.Count > 0) {
                pq.Dequeue(); // attend the event with earliest end day
                attended++;
                day++;
            }
        }

        return attended;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} events
 * @return {number}
 */
var maxEvents = function(events) {
    // sort by start day, then by end day
    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    
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
    
    const heap = new MinHeap();
    let i = 0; // index in events
    const n = events.length;
    let day = 0;
    let attended = 0;
    
    while (i < n || heap.size() > 0) {
        if (heap.size() === 0 && i < n) {
            day = Math.max(day, events[i][0]); // jump to next start day
        }
        // add all events that start on or before current day
        while (i < n && events[i][0] <= day) {
            heap.push(events[i][1]);
            i++;
        }
        // discard events that already ended before today
        while (heap.size() > 0 && heap.peek() < day) {
            heap.pop();
        }
        if (heap.size() > 0) {
            // attend the event with earliest end day
            heap.pop();
            attended++;
            day++; // move to next day
        } else {
            // no available events today, loop will jump day forward
        }
    }
    
    return attended;
};
```

## Typescript

```typescript
function maxEvents(events: number[][]): number {
    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    class MinHeap {
        private heap: number[] = [];
        size(): number { return this.heap.length; }
        isEmpty(): boolean { return this.heap.length === 0; }
        peek(): number { return this.heap[0]; }
        push(val: number): void {
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
        pop(): number | undefined {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const top = h[0];
            const last = h.pop()!;
            if (h.length > 0) {
                h[0] = last;
                let idx = 0;
                while (true) {
                    let left = idx * 2 + 1;
                    let right = left + 1;
                    let smallest = idx;
                    if (left < h.length && h[left] < h[smallest]) smallest = left;
                    if (right < h.length && h[right] < h[smallest]) smallest = right;
                    if (smallest === idx) break;
                    [h[idx], h[smallest]] = [h[smallest], h[idx]];
                    idx = smallest;
                }
            }
            return top;
        }
    }

    const heap = new MinHeap();
    let i = 0, day = 0, attended = 0;
    const n = events.length;

    while (i < n || !heap.isEmpty()) {
        if (heap.isEmpty() && i < n) {
            day = events[i][0];
        }
        while (i < n && events[i][0] <= day) {
            heap.push(events[i][1]);
            i++;
        }
        while (!heap.isEmpty() && heap.peek() < day) {
            heap.pop();
        }
        if (!heap.isEmpty()) {
            heap.pop(); // attend event with earliest end
            attended++;
            day++;
        }
    }

    return attended;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function maxEvents($events) {
        // Sort events by start day, then by end day
        usort($events, function($a, $b) {
            if ($a[0] == $b[0]) {
                return $a[1] <=> $b[1];
            }
            return $a[0] <=> $b[0];
        });

        $n = count($events);
        $maxDay = 0;
        foreach ($events as $e) {
            if ($e[1] > $maxDay) {
                $maxDay = $e[1];
            }
        }

        $heap = new SplMinHeap(); // stores end days
        $i = 0;      // index in sorted events
        $attended = 0;

        for ($day = 1; $day <= $maxDay; $day++) {
            // Add all events that start on or before current day
            while ($i < $n && $events[$i][0] <= $day) {
                $heap->insert($events[$i][1]);
                $i++;
            }

            // Remove events that have already ended before today
            while (!$heap->isEmpty() && $heap->top() < $day) {
                $heap->extract();
            }

            // Attend the event that ends earliest
            if (!$heap->isEmpty()) {
                $heap->extract();
                $attended++;
            }
        }

        return $attended;
    }
}
```

## Swift

```swift
class Solution {
    func maxEvents(_ events: [[Int]]) -> Int {
        let sorted = events.sorted { (a, b) -> Bool in
            if a[0] == b[0] {
                return a[1] < b[1]
            }
            return a[0] < b[0]
        }
        var heap = MinHeap()
        var i = 0
        let n = sorted.count
        var day = 0
        var attended = 0
        
        while i < n || !heap.isEmpty {
            if heap.isEmpty {
                day = sorted[i][0]
            }
            while i < n && sorted[i][0] <= day {
                heap.push(sorted[i][1])
                i += 1
            }
            while let top = heap.peek(), top < day {
                _ = heap.pop()
            }
            if !heap.isEmpty {
                _ = heap.pop()
                attended += 1
                day += 1
            }
        }
        return attended
    }
}

struct MinHeap {
    private var data: [Int] = []
    
    var isEmpty: Bool { data.isEmpty }
    
    func peek() -> Int? {
        return data.first
    }
    
    mutating func push(_ value: Int) {
        data.append(value)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        if data.count == 1 {
            return data.removeLast()
        }
        let result = data[0]
        data[0] = data.removeLast()
        siftDown(0)
        return result
    }
    
    private mutating func siftUp(_ index: Int) {
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
    
    private mutating func siftDown(_ index: Int) {
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
```

## Kotlin

```kotlin
class Solution {
    fun maxEvents(events: Array<IntArray>): Int {
        val sorted = events.sortedWith(compareBy<IntArray> { it[0] }.thenBy { it[1] })
        var day = 0
        var i = 0
        var attended = 0
        val pq = java.util.PriorityQueue<Int>()
        while (i < sorted.size || pq.isNotEmpty()) {
            if (pq.isEmpty() && i < sorted.size) {
                day = sorted[i][0]
            }
            while (i < sorted.size && sorted[i][0] <= day) {
                pq.add(sorted[i][1])
                i++
            }
            while (pq.isNotEmpty() && pq.peek() < day) {
                pq.poll()
            }
            if (pq.isNotEmpty()) {
                pq.poll()
                attended++
                day++
            } else {
                // No events can be attended today, move to next start day in next iteration
            }
        }
        return attended
    }
}
```

## Dart

```dart
class MinHeap {
  final List<int> _data = [];

  bool get isEmpty => _data.isEmpty;

  int peek() => _data[0];

  void push(int value) {
    _data.add(value);
    _siftUp(_data.length - 1);
  }

  int pop() {
    final int result = _data[0];
    final int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return result;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final int parent = (idx - 1) >> 1;
      if (_data[parent] <= _data[idx]) break;
      final int tmp = _data[parent];
      _data[parent] = _data[idx];
      _data[idx] = tmp;
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final int n = _data.length;
    while (true) {
      int smallest = idx;
      final int left = idx * 2 + 1;
      final int right = left + 1;
      if (left < n && _data[left] < _data[smallest]) smallest = left;
      if (right < n && _data[right] < _data[smallest]) smallest = right;
      if (smallest == idx) break;
      final int tmp = _data[idx];
      _data[idx] = _data[smallest];
      _data[smallest] = tmp;
      idx = smallest;
    }
  }
}

class Solution {
  int maxEvents(List<List<int>> events) {
    if (events.isEmpty) return 0;

    // Sort by start day, then by end day.
    events.sort((a, b) {
      if (a[0] == b[0]) return a[1] - b[1];
      return a[0] - b[0];
    });

    int maxEnd = 0;
    for (var e in events) {
      if (e[1] > maxEnd) maxEnd = e[1];
    }

    final MinHeap heap = MinHeap();
    int i = 0, attended = 0;
    final int n = events.length;

    for (int day = 1; day <= maxEnd; day++) {
      // Add all events that start on or before this day.
      while (i < n && events[i][0] <= day) {
        heap.push(events[i][1]);
        i++;
      }

      // Remove events that have already ended.
      while (!heap.isEmpty && heap.peek() < day) {
        heap.pop();
      }

      // Attend the event that ends earliest.
      if (!heap.isEmpty) {
        heap.pop();
        attended++;
      }
    }

    return attended;
  }
}
```

## Golang

```go
import (
	"container/heap"
	"sort"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

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

func maxEvents(events [][]int) int {
	if len(events) == 0 {
		return 0
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i][0] == events[j][0] {
			return events[i][1] < events[j][1]
		}
		return events[i][0] < events[j][0]
	})

	maxDay := 0
	for _, e := range events {
		if e[1] > maxDay {
			maxDay = e[1]
		}
	}

	h := &IntHeap{}
	heap.Init(h)

	ans, idx, n := 0, 0, len(events)
	for day := 1; day <= maxDay; day++ {
		for idx < n && events[idx][0] <= day {
			heap.Push(h, events[idx][1])
			idx++
		}
		for h.Len() > 0 && (*h)[0] < day {
			heap.Pop(h)
		}
		if h.Len() > 0 {
			heap.Pop(h)
			ans++
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_events(events)
  events.sort_by! { |s, e| [s, e] }
  n = events.length
  i = 0
  max_day = events.map { |_, e| e }.max || 0
  heap = []
  attended = 0

  (1..max_day).each do |day|
    while i < n && events[i][0] <= day
      val = events[i][1]
      heap << val
      idx = heap.size - 1
      while idx > 0
        parent = (idx - 1) / 2
        break if heap[parent] <= heap[idx]
        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent
      end
      i += 1
    end

    while !heap.empty? && heap[0] < day
      # pop min
      last = heap.pop
      if !heap.empty?
        heap[0] = last
        idx = 0
        size = heap.size
        loop do
          left = idx * 2 + 1
          right = left + 1
          break if left >= size
          smallest = left
          smallest = right if right < size && heap[right] < heap[left]
          break if heap[idx] <= heap[smallest]
          heap[idx], heap[smallest] = heap[smallest], heap[idx]
          idx = smallest
        end
      end
    end

    unless heap.empty?
      # attend event with earliest ending day
      last = heap.pop
      if !heap.empty?
        heap[0] = last
        idx = 0
        size = heap.size
        loop do
          left = idx * 2 + 1
          right = left + 1
          break if left >= size
          smallest = left
          smallest = right if right < size && heap[right] < heap[left]
          break if heap[idx] <= heap[smallest]
          heap[idx], heap[smallest] = heap[smallest], heap[idx]
          idx = smallest
        end
      end
      attended += 1
    end
  end

  attended
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.PriorityQueue

  def maxEvents(events: Array[Array[Int]]): Int = {
    val n = events.length
    if (n == 0) return 0

    // Sort events by start day
    val sorted = events.sortBy(_(0))
    var idx = 0

    // Find the latest ending day
    var maxDay = 0
    for (e <- events) {
      if (e(1) > maxDay) maxDay = e(1)
    }

    // Min-heap for event end days
    val pq = PriorityQueue.empty[Int](Ordering[Int].reverse)

    var attended = 0
    var day = 1

    while (day <= maxDay) {
      // Add all events that start on or before current day
      while (idx < n && sorted(idx)(0) <= day) {
        pq.enqueue(sorted(idx)(1))
        idx += 1
      }

      // Remove events that have already ended
      while (pq.nonEmpty && pq.head < day) {
        pq.dequeue()
      }

      // Attend the event with earliest end day, if any
      if (pq.nonEmpty) {
        pq.dequeue()
        attended += 1
      }

      day += 1
    }

    attended
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_events(events: Vec<Vec<i32>>) -> i32 {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        if events.is_empty() {
            return 0;
        }

        // Convert to (start, end) tuples and sort by start then end
        let mut ev: Vec<(i32, i32)> = events.into_iter().map(|v| (v[0], v[1])).collect();
        ev.sort_by_key(|&(s, e)| (s, e));

        // Maximum possible day we need to consider
        let max_day = ev.iter().map(|&(_, e)| e).max().unwrap();

        let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new(); // min-heap of end days
        let mut idx = 0usize;
        let mut attended = 0i32;

        for day in 1..=max_day {
            // Add all events that start on or before current day
            while idx < ev.len() && ev[idx].0 <= day {
                heap.push(Reverse(ev[idx].1));
                idx += 1;
            }

            // Remove events that have already ended before today
            while let Some(&Reverse(end)) = heap.peek() {
                if end < day {
                    heap.pop();
                } else {
                    break;
                }
            }

            // Attend the event with the earliest ending day, if any
            if heap.pop().is_some() {
                attended += 1;
            }
        }

        attended
    }
}
```

## Racket

```racket
(require racket/priority-queue)

(define/contract (max-events events)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted-list (sort events
                            (lambda (a b) (< (first a) (first b)))))
         (sorted (list->vector sorted-list))
         (n (vector-length sorted))
         (pq (make-pq <)))
    (let loop ((day 1) (idx 0) (attended 0))
      (if (and (= idx n) (pq-empty? pq))
          attended
          (let ((new-idx
                 (let add ((i idx))
                   (if (and (< i n)
                            (<= (first (vector-ref sorted i)) day))
                       (begin
                         (pq-add! pq (second (vector-ref sorted i)))
                         (add (+ i 1)))
                       i))))
            ;; Remove events that have already ended before current day
            (let clean ()
              (when (and (not (pq-empty? pq))
                         (< (pq-min pq) day))
                (pq-pop! pq)
                (clean)))
            (if (pq-empty? pq)
                (loop (+ day 1) new-idx attended)
                (begin
                  (pq-pop! pq) ; attend the event with earliest end day
                  (loop (+ day 1) new-idx (+ attended 1)))))))))
```

## Erlang

```erlang
-spec max_events(Events :: [[integer()]]) -> integer().
max_events(Events) ->
    EventsTuples = [ {Start, End} || [Start, End] <- Events ],
    Sorted = lists:keysort(1, EventsTuples),
    MaxDay = max_end(Sorted, 0),
    loop(1, Sorted, gb_trees:empty(), 0, MaxDay).

max_end([], Acc) -> Acc;
max_end([{_, End} | Rest], Acc) ->
    NewAcc = if End > Acc -> End; true -> Acc end,
    max_end(Rest, NewAcc).

loop(Day, EventsRem, Tree, Attended, MaxDay) when Day =< MaxDay ->
    {NewEventsRem, NewTree} = add_events(Day, EventsRem, Tree),
    CleanTree = clean_tree(Day, NewTree),
    case gb_trees:is_empty(CleanTree) of
        true ->
            loop(Day + 1, NewEventsRem, CleanTree, Attended, MaxDay);
        false ->
            {MinKey, Count} = gb_trees:smallest(CleanTree),
            UpdatedTree =
                if Count > 1 ->
                       gb_trees:update(MinKey, Count - 1, CleanTree);
                   true ->
                       gb_trees:delete(MinKey, CleanTree)
                end,
            loop(Day + 1, NewEventsRem, UpdatedTree, Attended + 1, MaxDay)
    end;
loop(_, _, _, Attended, _) -> Attended.

add_events(_Day, [], Tree) -> {[], Tree};
add_events(Day, [{Start, End} = _Evt | Rest], Tree) when Start =< Day ->
    NewTree =
        case gb_trees:lookup(End, Tree) of
            {value, C} -> gb_trees:update(End, C + 1, Tree);
            none -> gb_trees:insert(End, 1, Tree)
        end,
    add_events(Day, Rest, NewTree);
add_events(_Day, EventsRem, Tree) ->
    {EventsRem, Tree}.

clean_tree(Day, Tree) ->
    case gb_trees:is_empty(Tree) of
        true -> Tree;
        false ->
            {MinKey, _} = gb_trees:smallest(Tree),
            if MinKey < Day ->
                   clean_tree(Day, gb_trees:delete(MinKey, Tree));
               true -> Tree
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_events(events :: [[integer]]) :: integer
  def max_events(events) do
    sorted = Enum.sort_by(events, fn [s, _] -> s end)
    max_day = Enum.max_by(events, fn [_s, e] -> e end) |> elem(1)

    loop(1, max_day, sorted, :gb_trees.empty(), 0)
  end

  defp loop(day, max_day, remaining_events, tree, attended) when day > max_day do
    attended
  end

  defp loop(day, max_day, remaining_events, tree, attended) do
    {rem_after_add, tree1} = add_available(day, remaining_events, tree)
    tree2 = remove_expired(day, tree1)

    if get_min_key(tree2) != nil do
      {_min, new_tree} = pop_min(tree2)
      loop(day + 1, max_day, rem_after_add, new_tree, attended + 1)
    else
      loop(day + 1, max_day, rem_after_add, tree2, attended)
    end
  end

  defp add_available(day, [{s, e} | rest], tree) when s <= day do
    new_tree = add_end(tree, e)
    add_available(day, rest, new_tree)
  end

  defp add_available(_day, remaining, tree), do: {remaining, tree}

  defp remove_expired(day, tree) do
    case get_min_key(tree) do
      nil -> tree
      min when min < day ->
        {_min, new_tree} = pop_min(tree)
        remove_expired(day, new_tree)

      _ -> tree
    end
  end

  defp add_end(tree, e) do
    case :gb_trees.lookup(e, tree) do
      {:value, cnt} -> :gb_trees.update(e, cnt + 1, tree)
      :none -> :gb_trees.insert(e, 1, tree)
    end
  end

  defp get_min_key(tree) do
    case :gb_trees.iterator(tree) do
      it ->
        case :gb_trees.next(it) do
          {key, _val, _it2} -> key
          :none -> nil
        end
    end
  end

  defp pop_min(tree) do
    iterator = :gb_trees.iterator(tree)

    case :gb_trees.next(iterator) do
      {key, cnt, _it2} ->
        new_tree =
          if cnt == 1 do
            :gb_trees.delete(key, tree)
          else
            :gb_trees.update(key, cnt - 1, tree)
          end

        {key, new_tree}

      :none ->
        {:none, tree}
    end
  end
end
```

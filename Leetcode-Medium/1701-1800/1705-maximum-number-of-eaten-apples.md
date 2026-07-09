# 1705. Maximum Number of Eaten Apples

## Cpp

```cpp
class Solution {
public:
    int eatenApples(vector<int>& apples, vector<int>& days) {
        using P = pair<long long,long long>; // {expire_day, remaining_apples}
        priority_queue<P, vector<P>, greater<P>> pq;
        long long ans = 0;
        int n = apples.size();
        int day = 0;
        while (day < n || !pq.empty()) {
            if (day < n && apples[day] > 0) {
                long long expire = (long long)day + days[day];
                pq.emplace(expire, apples[day]);
            }
            while (!pq.empty() && pq.top().first <= day) {
                pq.pop(); // discard rotten batches
            }
            if (!pq.empty()) {
                auto cur = pq.top();
                pq.pop();
                cur.second--;          // eat one apple
                ++ans;
                if (cur.second > 0) {   // still have apples left in this batch
                    pq.emplace(cur.first, cur.second);
                }
            }
            ++day;
        }
        return (int)ans;
    }
};
```

## Java

```java
import java.util.PriorityQueue;

class Solution {
    public int eatenApples(int[] apples, int[] days) {
        int n = apples.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int day = 0, eaten = 0;
        while (day < n || !pq.isEmpty()) {
            if (day < n && apples[day] > 0) {
                int expireDay = day + days[day];
                pq.offer(new int[]{expireDay, apples[day]});
            }
            while (!pq.isEmpty() && pq.peek()[0] <= day) {
                pq.poll();
            }
            if (!pq.isEmpty()) {
                int[] batch = pq.poll();
                batch[1]--;
                eaten++;
                if (batch[1] > 0) {
                    pq.offer(batch);
                }
            }
            day++;
        }
        return eaten;
    }
}
```

## Python

```python
class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        import heapq
        heap = []  # each element is (expire_day, remaining_apples)
        n = len(apples)
        day = 0
        eaten = 0

        while day < n or heap:
            if day < n and apples[day] > 0:
                expire = day + days[day]
                heapq.heappush(heap, [expire, apples[day]])

            # remove rotten batches
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            if heap:
                # eat one apple from the batch that expires soonest
                heap[0][1] -= 1
                eaten += 1
                if heap[0][1] == 0:
                    heapq.heappop(heap)
            day += 1

        return eaten
```

## Python3

```python
class Solution:
    def eatenApples(self, apples, days):
        import heapq
        heap = []  # (expire_day, remaining)
        n = len(apples)
        day = 0
        ans = 0

        while day < n or heap:
            if day < n and apples[day] > 0:
                expire = day + days[day]
                heapq.heappush(heap, [expire, apples[day]])

            # remove rotten batches
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            if heap:
                heap[0][1] -= 1
                ans += 1
                if heap[0][1] == 0:
                    heapq.heappop(heap)
                else:
                    # need to re-heapify because the count changed but key unchanged
                    # heap property still holds as only value changed, no need to push/pop
                    pass

            day += 1

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int expire;
    int count;
} Node;

static void swap(Node *a, Node *b) {
    Node tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapifyUp(Node *heap, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (heap[parent].expire <= heap[idx].expire) break;
        swap(&heap[parent], &heap[idx]);
        idx = parent;
    }
}

static void heapifyDown(Node *heap, int size, int idx) {
    while (1) {
        int left = (idx << 1) + 1;
        int right = left + 1;
        int smallest = idx;
        if (left < size && heap[left].expire < heap[smallest].expire)
            smallest = left;
        if (right < size && heap[right].expire < heap[smallest].expire)
            smallest = right;
        if (smallest == idx) break;
        swap(&heap[idx], &heap[smallest]);
        idx = smallest;
    }
}

static void push(Node *heap, int *size, Node node) {
    heap[*size] = node;
    (*size)++;
    heapifyUp(heap, *size - 1);
}

static Node pop(Node *heap, int *size) {
    Node top = heap[0];
    heap[0] = heap[*size - 1];
    (*size)--;
    if (*size > 0)
        heapifyDown(heap, *size, 0);
    return top;
}

int eatenApples(int* apples, int applesSize, int* days, int daysSize){
    (void)daysSize; // unused parameter
    Node *heap = (Node*)malloc(sizeof(Node) * (applesSize + 5));
    int heapSize = 0;
    int day = 0;
    int ans = 0;

    while (day < applesSize || heapSize > 0) {
        if (day < applesSize && apples[day] > 0) {
            Node node;
            node.expire = day + days[day];
            node.count = apples[day];
            push(heap, &heapSize, node);
        }
        while (heapSize > 0 && (heap[0].expire <= day || heap[0].count == 0)) {
            pop(heap, &heapSize);
        }
        if (heapSize > 0) {
            heap[0].count--;
            ans++;
            if (heap[0].count == 0) {
                pop(heap, &heapSize);
            }
        }
        day++;
    }

    free(heap);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private class MinHeap
    {
        private readonly List<(int expire, int count)> _data = new List<(int, int)>();
        public int Count => _data.Count;

        public void Push((int expire, int count) item)
        {
            _data.Add(item);
            int i = _data.Count - 1;
            while (i > 0)
            {
                int p = (i - 1) / 2;
                if (_data[p].expire <= _data[i].expire) break;
                var tmp = _data[p];
                _data[p] = _data[i];
                _data[i] = tmp;
                i = p;
            }
        }

        public (int expire, int count) Pop()
        {
            var root = _data[0];
            var last = _data[_data.Count - 1];
            _data.RemoveAt(_data.Count - 1);
            if (_data.Count > 0)
            {
                _data[0] = last;
                int i = 0;
                while (true)
                {
                    int l = i * 2 + 1, r = l + 1, smallest = i;
                    if (l < _data.Count && _data[l].expire < _data[smallest].expire) smallest = l;
                    if (r < _data.Count && _data[r].expire < _data[smallest].expire) smallest = r;
                    if (smallest == i) break;
                    var tmp = _data[i];
                    _data[i] = _data[smallest];
                    _data[smallest] = tmp;
                    i = smallest;
                }
            }
            return root;
        }

        public (int expire, int count) Peek() => _data[0];
    }

    public int EatenApples(int[] apples, int[] days)
    {
        int n = apples.Length;
        var heap = new MinHeap();
        long eaten = 0;
        int day = 0;

        while (day < n || heap.Count > 0)
        {
            if (day < n && apples[day] > 0)
            {
                int expire = day + days[day];
                heap.Push((expire, apples[day]));
            }

            while (heap.Count > 0 && heap.Peek().expire <= day)
            {
                heap.Pop();
            }

            if (heap.Count > 0)
            {
                var top = heap.Pop();
                top.count--;
                eaten++;
                if (top.count > 0)
                {
                    heap.Push(top);
                }
            }

            day++;
        }

        return (int)eaten;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} apples
 * @param {number[]} days
 * @return {number}
 */
var eatenApples = function(apples, days) {
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
        push(item) {
            const h = this.heap;
            h.push(item);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p][0] <= h[i][0]) break;
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
                    let l = i * 2 + 1,
                        r = l + 1,
                        smallest = i;
                    if (l < h.length && h[l][0] < h[smallest][0]) smallest = l;
                    if (r < h.length && h[r][0] < h[smallest][0]) smallest = r;
                    if (smallest === i) break;
                    [h[i], h[smallest]] = [h[smallest], h[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const heap = new MinHeap();
    let day = 0;
    let eaten = 0;
    const n = apples.length;

    while (day < n || heap.size() > 0) {
        // add today's apples
        if (day < n && apples[day] > 0) {
            heap.push([day + days[day], apples[day]]); // [expireDay, remainingCount]
        }
        // remove rotten batches
        while (heap.size() > 0 && heap.peek()[0] <= day) {
            heap.pop();
        }
        // eat one apple from the batch that expires soonest
        if (heap.size() > 0) {
            const top = heap.peek();
            top[1]--; // consume one
            eaten++;
            if (top[1] === 0) heap.pop(); // remove empty batch
        }
        day++;
    }

    return eaten;
};
```

## Typescript

```typescript
function eatenApples(apples: number[], days: number[]): number {
    class MinHeap {
        private heap: [number, number][] = [];
        size(): number { return this.heap.length; }
        peek(): [number, number] | undefined { return this.heap[0]; }
        push(item: [number, number]): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = Math.floor((idx - 1) / 2);
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        private bubbleDown(idx: number): void {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let smallest = idx;
                if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const heap = new MinHeap();
    let day = 0;
    let eaten = 0;
    const n = apples.length;

    while (day < n || heap.size() > 0) {
        if (day < n && apples[day] > 0) {
            const expire = day + days[day];
            heap.push([expire, apples[day]]);
        }
        while (heap.size() > 0 && heap.peek()![0] <= day) {
            heap.pop();
        }
        if (heap.size() > 0) {
            let [exp, cnt] = heap.pop()!;
            cnt--;
            eaten++;
            if (cnt > 0) {
                heap.push([exp, cnt]);
            }
        }
        day++;
    }

    return eaten;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $apples
     * @param Integer[] $days
     * @return Integer
     */
    function eatenApples($apples, $days) {
        $n = count($apples);
        $heap = new SplPriorityQueue();
        // we only need the data part when extracting
        $heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        $day = 0;
        $eaten = 0;

        while ($day < $n || !$heap->isEmpty()) {
            // add new apples grown today
            if ($day < $n && $apples[$day] > 0) {
                $expire = $day + $days[$day];
                $cnt = $apples[$day];
                // priority is negative expire to simulate min-heap
                $heap->insert(['expire' => $expire, 'count' => $cnt], -$expire);
            }

            // discard rotten apples
            while (!$heap->isEmpty()) {
                $top = $heap->top(); // peek without removing
                if ($top['expire'] <= $day) {
                    $heap->extract();
                } else {
                    break;
                }
            }

            // eat one apple from the batch that expires soonest
            if (!$heap->isEmpty()) {
                $node = $heap->extract();
                $node['count']--;
                $eaten++;
                if ($node['count'] > 0 && $node['expire'] > $day) {
                    $heap->insert($node, -$node['expire']);
                }
            }

            $day++;
        }

        return $eaten;
    }
}
```

## Swift

```swift
struct AppleBatch {
    var expire: Int
    var count: Int
}

final class MinHeap {
    private var data: [AppleBatch] = []
    
    var isEmpty: Bool { data.isEmpty }
    
    func peek() -> AppleBatch? {
        return data.first
    }
    
    func push(_ batch: AppleBatch) {
        data.append(batch)
        siftUp(from: data.count - 1)
    }
    
    func pop() -> AppleBatch? {
        guard !data.isEmpty else { return nil }
        if data.count == 1 {
            return data.removeLast()
        } else {
            let root = data[0]
            data[0] = data.removeLast()
            siftDown(from: 0)
            return root
        }
    }
    
    private func siftUp(from index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[child].expire < data[parent].expire {
                data.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }
    
    private func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = 2 * parent + 1
            let right = left + 1
            var smallest = parent
            
            if left < data.count && data[left].expire < data[smallest].expire {
                smallest = left
            }
            if right < data.count && data[right].expire < data[smallest].expire {
                smallest = right
            }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}

class Solution {
    func eatenApples(_ apples: [Int], _ days: [Int]) -> Int {
        let n = apples.count
        var day = 0
        var eaten = 0
        let heap = MinHeap()
        
        while day < n || !heap.isEmpty {
            if day < n && apples[day] > 0 {
                let expireDay = day + days[day]
                heap.push(AppleBatch(expire: expireDay, count: apples[day]))
            }
            
            // Remove batches that have already rotted
            while let top = heap.peek(), top.expire <= day {
                _ = heap.pop()
            }
            
            if !heap.isEmpty {
                var batch = heap.pop()!
                batch.count -= 1
                eaten += 1
                if batch.count > 0 {
                    heap.push(batch)
                }
            }
            
            day += 1
        }
        
        return eaten
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun eatenApples(apples: IntArray, days: IntArray): Int {
        val n = apples.size
        val pq = java.util.PriorityQueue<Node>(compareBy { it.expire })
        var day = 0
        var eaten = 0
        while (day < n || pq.isNotEmpty()) {
            if (day < n && apples[day] > 0) {
                val expireDay = day + days[day]
                if (expireDay > day) {
                    pq.offer(Node(expireDay, apples[day]))
                }
            }
            while (pq.isNotEmpty() && (pq.peek().expire <= day || pq.peek().count == 0)) {
                pq.poll()
            }
            if (pq.isNotEmpty()) {
                val cur = pq.peek()
                cur.count--
                eaten++
                if (cur.count == 0) pq.poll()
            }
            day++
        }
        return eaten
    }

    private data class Node(var expire: Int, var count: Int)
}
```

## Dart

```dart
class Solution {
  int eatenApples(List<int> apples, List<int> days) {
    int n = apples.length;
    var heap = _MinHeap();
    int day = 0;
    int ans = 0;

    while (day < n || !heap.isEmpty()) {
      if (day < n && apples[day] > 0) {
        heap.push(_Apple(day + days[day], apples[day]));
      }

      while (!heap.isEmpty() && heap.peek().expire <= day) {
        heap.pop();
      }

      if (!heap.isEmpty()) {
        var top = heap.peek();
        top.count--;
        ans++;
        if (top.count == 0) {
          heap.pop();
        }
      }

      day++;
    }

    return ans;
  }
}

class _Apple {
  int expire;
  int count;
  _Apple(this.expire, this.count);
}

class _MinHeap {
  final List<_Apple> _data = [];

  bool isEmpty() => _data.isEmpty;

  _Apple peek() => _data[0];

  void push(_Apple a) {
    _data.add(a);
    _siftUp(_data.length - 1);
  }

  _Apple pop() {
    var root = _data[0];
    var last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return root;
  }

  void _siftUp(int i) {
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_data[p].expire <= _data[i].expire) break;
      var tmp = _data[p];
      _data[p] = _data[i];
      _data[i] = tmp;
      i = p;
    }
  }

  void _siftDown(int i) {
    int n = _data.length;
    while (true) {
      int l = i * 2 + 1;
      int r = l + 1;
      int smallest = i;
      if (l < n && _data[l].expire < _data[smallest].expire) smallest = l;
      if (r < n && _data[r].expire < _data[smallest].expire) smallest = r;
      if (smallest == i) break;
      var tmp = _data[i];
      _data[i] = _data[smallest];
      _data[smallest] = tmp;
      i = smallest;
    }
  }
}
```

## Golang

```go
import (
	"container/heap"
)

type apple struct {
	expire int
	cnt    int
}

type appleHeap []apple

func (h appleHeap) Len() int { return len(h) }
func (h appleHeap) Less(i, j int) bool {
	return h[i].expire < h[j].expire
}
func (h appleHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *appleHeap) Push(x interface{}) {
	*h = append(*h, x.(apple))
}

func (h *appleHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func eatenApples(apples []int, days []int) int {
	h := &appleHeap{}
	heap.Init(h)
	ans := 0
	n := len(apples)

	for day := 0; day < n || h.Len() > 0; day++ {
		if day < n && apples[day] > 0 {
			heap.Push(h, apple{expire: day + days[day], cnt: apples[day]})
		}
		// discard rotten batches
		for h.Len() > 0 && (*h)[0].expire <= day {
			heap.Pop(h)
		}
		if h.Len() > 0 {
			top := &(*h)[0]
			top.cnt--
			ans++
			if top.cnt == 0 {
				heap.Pop(h)
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def heap_push(heap, item)
  heap << item
  i = heap.size - 1
  while i > 0
    p = (i - 1) / 2
    break if heap[p][0] <= heap[i][0]
    heap[i], heap[p] = heap[p], heap[i]
    i = p
  end
end

def heap_pop(heap)
  return nil if heap.empty?
  min = heap[0]
  last = heap.pop
  unless heap.empty?
    heap[0] = last
    i = 0
    size = heap.size
    loop do
      l = i * 2 + 1
      r = i * 2 + 2
      smallest = i
      smallest = l if l < size && heap[l][0] < heap[smallest][0]
      smallest = r if r < size && heap[r][0] < heap[smallest][0]
      break if smallest == i
      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
  end
  min
end

# @param {Integer[]} apples
# @param {Integer[]} days
# @return {Integer}
def eaten_apples(apples, days)
  n = apples.size
  heap = []
  day = 0
  ans = 0

  while day < n || !heap.empty?
    if day < n && apples[day] > 0
      expire = day + days[day]
      heap_push(heap, [expire, apples[day]])
    end

    while !heap.empty? && heap[0][0] <= day
      heap_pop(heap)
    end

    unless heap.empty?
      expire, cnt = heap_pop(heap)
      cnt -= 1
      ans += 1
      if cnt > 0 && expire > day + 1
        heap_push(heap, [expire, cnt])
      end
    end

    day += 1
  end

  ans
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.PriorityQueue

    def eatenApples(apples: Array[Int], days: Array[Int]): Int = {
        // Min-heap based on expiration day
        val pq: PriorityQueue[(Int, Int)] = PriorityQueue.empty(
            Ordering.by[(Int, Int), Int](_._1).reverse
        )
        var day = 0
        var eaten = 0
        val n = apples.length

        while (day < n || pq.nonEmpty) {
            // Add new apples grown today
            if (day < n && apples(day) > 0) {
                val expireDay = day + days(day)
                pq.enqueue((expireDay, apples(day)))
            }

            // Remove rotten batches
            while (pq.nonEmpty && pq.head._1 <= day) {
                pq.dequeue()
            }

            // Eat one apple from the batch that expires soonest
            if (pq.nonEmpty) {
                val (exp, cnt) = pq.dequeue()
                eaten += 1
                if (cnt > 1) {
                    pq.enqueue((exp, cnt - 1))
                }
            }

            day += 1
        }

        eaten
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn eaten_apples(apples: Vec<i32>, days: Vec<i32>) -> i32 {
        let n = apples.len();
        let mut heap: BinaryHeap<(Reverse<i32>, i32)> = BinaryHeap::new();
        let mut day: i32 = 0;
        let mut ans: i32 = 0;

        while (day as usize) < n || !heap.is_empty() {
            if (day as usize) < n && apples[day as usize] > 0 {
                let expire = day + days[day as usize];
                heap.push((Reverse(expire), apples[day as usize]));
            }

            // Discard rotten batches
            while let Some(&(Reverse(expire), _)) = heap.peek() {
                if expire <= day {
                    heap.pop();
                } else {
                    break;
                }
            }

            if let Some((Reverse(expire), mut cnt)) = heap.pop() {
                ans += 1;          // eat one apple
                cnt -= 1;
                if cnt > 0 && expire > day + 1 {
                    heap.push((Reverse(expire), cnt));
                } else if cnt > 0 {
                    // still push back; it will be removed on the next iteration due to expiration
                    heap.push((Reverse(expire), cnt));
                }
            }

            day += 1;
        }

        ans
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define (eaten-apples apples days)
  (let* ([n (length apples)]
         [h (make-heap (lambda (a b) (< (car a) (car b))))] ; compare by expiration day
         [day 0]
         [ans 0])
    (let loop ()
      (when (or (< day n) (not (heap-empty? h)))
        ;; add apples that grow on this day
        (when (< day n)
          (define a (list-ref apples day))
          (define d (list-ref days day))
          (when (> a 0)
            (heap-add! h (cons (+ day d) a))))
        ;; discard all batches that have already expired
        (let remove-expired ()
          (when (and (not (heap-empty? h))
                     (<= (car (heap-min h)) day))
            (heap-remove-min! h)
            (remove-expired)))
        ;; eat one apple from the batch that expires soonest
        (unless (heap-empty? h)
          (define top (heap-remove-min! h)) ; top = (expire . count)
          (set! ans (+ ans 1))
          (define expire (car top))
          (define remaining (- (cdr top) 1))
          (when (> remaining 0)
            (heap-add! h (cons expire remaining))))
        (set! day (+ day 1))
        (loop)))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([eaten_apples/2]).

-spec eaten_apples(Apples :: [integer()], Days :: [integer()]) -> integer().
eaten_apples(Apples, Days) ->
    loop(0, Apples, Days, gb_trees:empty(), 0).

%% main recursion
loop(Day, [A|As], [D|Ds], Tree, Count) ->
    %% add new apples if any
    NewTree = case A > 0 of
        true ->
            Expire = Day + D,
            Existing = case gb_trees:lookup(Expire, Tree) of
                {value, V} -> V;
                none -> 0
            end,
            gb_trees:insert(Expire, Existing + A, Tree);
        false ->
            Tree
    end,
    CleanTree = remove_expired(Day, NewTree),
    case gb_trees:is_empty(CleanTree) of
        true ->
            loop(Day + 1, As, Ds, CleanTree, Count);
        false ->
            {ExpireDay, Val} = gb_trees:smallest(CleanTree),
            NewVal = Val - 1,
            UpdatedTree = if NewVal == 0 ->
                              gb_trees:delete(ExpireDay, CleanTree);
                          true ->
                              gb_trees:update(ExpireDay, NewVal, CleanTree)
                          end,
            loop(Day + 1, As, Ds, UpdatedTree, Count + 1)
    end;
loop(Day, [], [], Tree, Count) ->
    case gb_trees:is_empty(Tree) of
        true -> Count;
        false ->
            CleanTree = remove_expired(Day, Tree),
            case gb_trees:is_empty(CleanTree) of
                true -> Count;
                false ->
                    {ExpireDay, Val} = gb_trees:smallest(CleanTree),
                    NewVal = Val - 1,
                    UpdatedTree = if NewVal == 0 ->
                                      gb_trees:delete(ExpireDay, CleanTree);
                                  true ->
                                      gb_trees:update(ExpireDay, NewVal, CleanTree)
                                  end,
                    loop(Day + 1, [], [], UpdatedTree, Count + 1)
            end
    end.

%% remove all batches that have already rotted (expire <= Day)
remove_expired(Day, Tree) ->
    case gb_trees:is_empty(Tree) of
        true -> Tree;
        false ->
            {Key, _} = gb_trees:smallest(Tree),
            if Key =< Day ->
                    NewTree = gb_trees:delete(Key, Tree),
                    remove_expired(Day, NewTree);
               true ->
                    Tree
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec eaten_apples(apples :: [integer], days :: [integer]) :: integer
  def eaten_apples(apples, days) do
    n = length(apples)
    ap_arr = :array.from_list(apples)
    day_arr = :array.from_list(days)

    loop(0, n, ap_arr, day_arr, :gb_trees.empty(), 0)
  end

  defp loop(day, n, ap_arr, day_arr, tree, eaten) do
    cond do
      day >= n and :gb_trees.is_empty(tree) ->
        eaten

      true ->
        # add new batch if within original days
        tree =
          if day < n do
            a = :array.get(day, ap_arr)
            d = :array.get(day, day_arr)

            if a > 0 do
              expire = day + d

              case :gb_trees.lookup(expire, tree) do
                {:value, v} -> :gb_trees.update(expire, v + a, tree)
                :none -> :gb_trees.insert(expire, a, tree)
              end
            else
              tree
            end
          else
            tree
          end

        # remove all expired batches
        tree = clean_expired(tree, day)

        # eat one apple from the batch that expires soonest
        {tree, eaten} =
          if :gb_trees.is_empty(tree) do
            {tree, eaten}
          else
            {expire, cnt} = :gb_trees.smallest(tree)
            new_cnt = cnt - 1

            tree =
              if new_cnt == 0 do
                :gb_trees.delete(expire, tree)
              else
                :gb_trees.update(expire, new_cnt, tree)
              end

            {tree, eaten + 1}
          end

        loop(day + 1, n, ap_arr, day_arr, tree, eaten)
    end
  end

  defp clean_expired(tree, day) do
    if :gb_trees.is_empty(tree) do
      tree
    else
      {key, _} = :gb_trees.smallest(tree)

      if key <= day do
        clean_expired(:gb_trees.delete(key, tree), day)
      else
        tree
      end
    end
  end
end
```

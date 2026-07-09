# 1942. The Number of the Smallest Unoccupied Chair

## Cpp

```cpp
class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        int n = times.size();
        struct Friend {int arrival; int leave; int idx;};
        vector<Friend> friends;
        friends.reserve(n);
        for (int i = 0; i < n; ++i) {
            friends.push_back({times[i][0], times[i][1], i});
        }
        sort(friends.begin(), friends.end(),
             [](const Friend& a, const Friend& b){ return a.arrival < b.arrival; });
        
        using pii = pair<int,int>; // (leave time, chair)
        priority_queue<pii, vector<pii>, greater<pii>> occupied;
        priority_queue<int, vector<int>, greater<int>> freeChairs;
        int nextChair = 0;
        
        for (const auto& f : friends) {
            while (!occupied.empty() && occupied.top().first <= f.arrival) {
                freeChairs.push(occupied.top().second);
                occupied.pop();
            }
            int chair;
            if (!freeChairs.empty()) {
                chair = freeChairs.top();
                freeChairs.pop();
            } else {
                chair = nextChair++;
            }
            if (f.idx == targetFriend) return chair;
            occupied.emplace(f.leave, chair);
        }
        return -1; // should never reach here
    }
};
```

## Java

```java
class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        int n = times.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        java.util.Arrays.sort(order, (a, b) -> Integer.compare(times[a][0], times[b][0]));
        
        java.util.PriorityQueue<Integer> freeChairs = new java.util.PriorityQueue<>();
        java.util.PriorityQueue<int[]> occupied = new java.util.PriorityQueue<>(
            (a, b) -> Integer.compare(a[0], b[0]) // compare by leave time
        );
        
        int nextChair = 0;
        for (int idx : order) {
            int arrival = times[idx][0];
            int leaving = times[idx][1];
            
            while (!occupied.isEmpty() && occupied.peek()[0] <= arrival) {
                freeChairs.offer(occupied.poll()[1]);
            }
            
            int chair;
            if (!freeChairs.isEmpty()) {
                chair = freeChairs.poll();
            } else {
                chair = nextChair++;
            }
            
            if (idx == targetFriend) {
                return chair;
            }
            
            occupied.offer(new int[]{leaving, chair});
        }
        return -1; // should never reach here
    }
}
```

## Python

```python
class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        import heapq

        # Pair each friend with their arrival, leaving time and original index
        friends = [(arr, leave, i) for i, (arr, leave) in enumerate(times)]
        # Process friends in order of arrival
        friends.sort(key=lambda x: x[0])

        available = []          # min-heap of free chair numbers
        occupied = []           # min-heap of (leaving_time, chair_number)
        next_chair = 0

        for arr, leave, idx in friends:
            # Release chairs whose owners have left by current arrival time
            while occupied and occupied[0][0] <= arr:
                _, freed_chair = heapq.heappop(occupied)
                heapq.heappush(available, freed_chair)

            # Assign the smallest available chair
            if available:
                chair = heapq.heappop(available)
            else:
                chair = next_chair
                next_chair += 1

            # If this is the target friend, return the assigned chair
            if idx == targetFriend:
                return chair

            # Mark this chair as occupied until 'leave' time
            heapq.heappush(occupied, (leave, chair))

        return -1
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Pair each friend with their arrival, leaving times and original index
        friends = [(arr, leave, idx) for idx, (arr, leave) in enumerate(times)]
        friends.sort(key=lambda x: x[0])  # sort by arrival time

        available = []          # min-heap of free chair numbers
        occupied = []           # min-heap of (leaving_time, chair_number)
        next_chair = 0

        for arr, leave, idx in friends:
            # Release chairs whose owners have left at or before current arrival
            while occupied and occupied[0][0] <= arr:
                _, freed_chair = heapq.heappop(occupied)
                heapq.heappush(available, freed_chair)

            # Assign the smallest available chair
            if available:
                chair = heapq.heappop(available)
            else:
                chair = next_chair
                next_chair += 1

            if idx == targetFriend:
                return chair

            # Mark this chair as occupied until 'leave' time
            heapq.heappush(occupied, (leave, chair))

        # Should never reach here with valid input
        return -1
```

## C

```c
#include <stdlib.h>

typedef struct {
    int arr;
    int leave;
    int idx;
} Friend;

static int cmpFriend(const void *a, const void *b) {
    const Friend *fa = (const Friend *)a;
    const Friend *fb = (const Friend *)b;
    return fa->arr - fb->arr;
}

/* Min-heap for available chairs (ints) */
static void availPush(int *heap, int *size, int val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p] <= heap[i]) break;
        int tmp = heap[p];
        heap[p] = heap[i];
        heap[i] = tmp;
        i = p;
    }
}
static int availPop(int *heap, int *size) {
    int top = heap[0];
    (*size)--;
    if (*size > 0) {
        heap[0] = heap[*size];
        int i = 0;
        while (1) {
            int l = i * 2 + 1;
            int r = l + 1;
            if (l >= *size) break;
            int smallest = l;
            if (r < *size && heap[r] < heap[l]) smallest = r;
            if (heap[i] <= heap[smallest]) break;
            int tmp = heap[i];
            heap[i] = heap[smallest];
            heap[smallest] = tmp;
            i = smallest;
        }
    }
    return top;
}

/* Min-heap for occupied chairs */
typedef struct {
    int leave;
    int chair;
} Occupied;

static void occPush(Occupied *heap, int *size, int leave, int chair) {
    int i = (*size)++;
    heap[i].leave = leave;
    heap[i].chair = chair;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].leave <= heap[i].leave) break;
        Occupied tmp = heap[p];
        heap[p] = heap[i];
        heap[i] = tmp;
        i = p;
    }
}
static Occupied occTop(Occupied *heap) {
    return heap[0];
}
static void occPop(Occupied *heap, int *size) {
    (*size)--;
    if (*size > 0) {
        heap[0] = heap[*size];
        int i = 0;
        while (1) {
            int l = i * 2 + 1;
            int r = l + 1;
            if (l >= *size) break;
            int smallest = l;
            if (r < *size && heap[r].leave < heap[l].leave) smallest = r;
            if (heap[i].leave <= heap[smallest].leave) break;
            Occupied tmp = heap[i];
            heap[i] = heap[smallest];
            heap[smallest] = tmp;
            i = smallest;
        }
    }
}

int smallestChair(int** times, int timesSize, int* timesColSize, int targetFriend) {
    if (timesSize == 0) return -1;

    Friend *friends = (Friend *)malloc(timesSize * sizeof(Friend));
    for (int i = 0; i < timesSize; ++i) {
        friends[i].arr   = times[i][0];
        friends[i].leave = times[i][1];
        friends[i].idx   = i;
    }
    qsort(friends, timesSize, sizeof(Friend), cmpFriend);

    int *availHeap = (int *)malloc(timesSize * sizeof(int));
    int availSize = 0;
    for (int i = 0; i < timesSize; ++i) {
        availPush(availHeap, &availSize, i);
    }

    Occupied *occHeap = (Occupied *)malloc(timesSize * sizeof(Occupied));
    int occSize = 0;

    int answer = -1;
    for (int i = 0; i < timesSize; ++i) {
        int curArr   = friends[i].arr;
        int curLeave = friends[i].leave;
        int curIdx   = friends[i].idx;

        while (occSize > 0 && occTop(occHeap).leave <= curArr) {
            int freedChair = occTop(occHeap).chair;
            occPop(occHeap, &occSize);
            availPush(availHeap, &availSize, freedChair);
        }

        int chair = availPop(availHeap, &availSize);
        if (curIdx == targetFriend) {
            answer = chair;
            break;
        }
        occPush(occHeap, &occSize, curLeave, chair);
    }

    free(friends);
    free(availHeap);
    free(occHeap);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestChair(int[][] times, int targetFriend) {
        int n = times.Length;
        var friends = new (int arrival, int leave, int idx)[n];
        for (int i = 0; i < n; i++) {
            friends[i] = (times[i][0], times[i][1], i);
        }
        Array.Sort(friends, (a, b) => a.arrival.CompareTo(b.arrival));

        var available = new PriorityQueue<int, int>();
        for (int i = 0; i < n; i++) {
            available.Enqueue(i, i); // chair number as priority
        }

        var occupied = new PriorityQueue<(int leave, int chair), int>();

        foreach (var f in friends) {
            while (occupied.Count > 0 && occupied.TryPeek(out var top, out _) && top.leave <= f.arrival) {
                var freed = occupied.Dequeue();
                available.Enqueue(freed.chair, freed.chair);
            }

            int chair = available.Dequeue();
            if (f.idx == targetFriend) return chair;

            occupied.Enqueue((f.leave, chair), f.leave);
        }

        return -1; // should never reach here
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} times
 * @param {number} targetFriend
 * @return {number}
 */
var smallestChair = function(times, targetFriend) {
    class MinHeap {
        constructor(compare) {
            this.data = [];
            this.compare = compare;
        }
        size() {
            return this.data.length;
        }
        peek() {
            return this.data[0];
        }
        push(item) {
            const a = this.data;
            a.push(item);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.compare(a[i], a[p])) {
                    [a[i], a[p]] = [a[p], a[i]];
                    i = p;
                } else break;
            }
        }
        pop() {
            const a = this.data;
            if (a.length === 0) return undefined;
            const top = a[0];
            const last = a.pop();
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = i * 2 + 2;
                    let smallest = i;
                    if (l < a.length && this.compare(a[l], a[smallest])) smallest = l;
                    if (r < a.length && this.compare(a[r], a[smallest])) smallest = r;
                    if (smallest !== i) {
                        [a[i], a[smallest]] = [a[smallest], a[i]];
                        i = smallest;
                    } else break;
                }
            }
            return top;
        }
    }

    // Prepare friends with index
    const friends = times.map((t, idx) => ({arr: t[0], leave: t[1], idx}));
    friends.sort((a, b) => a.arr - b.arr);

    const occupied = new MinHeap((a, b) => a[0] < b[0]); // [leaveTime, chair]
    const available = new MinHeap((a, b) => a < b); // chair numbers
    let nextChair = 0;

    for (const f of friends) {
        // free chairs whose owners have left
        while (occupied.size() && occupied.peek()[0] <= f.arr) {
            const [, chair] = occupied.pop();
            available.push(chair);
        }

        let chair;
        if (available.size()) {
            chair = available.pop();
        } else {
            chair = nextChair++;
        }

        if (f.idx === targetFriend) return chair;

        occupied.push([f.leave, chair]);
    }
    return -1; // should never reach here
};
```

## Typescript

```typescript
function smallestChair(times: number[][], targetFriend: number): number {
    class MinHeap<T> {
        private data: T[] = [];
        private cmp: (a: T, b: T) => boolean;
        constructor(cmp: (a: T, b: T) => boolean) {
            this.cmp = cmp;
        }
        size(): number { return this.data.length; }
        peek(): T | undefined { return this.data[0]; }
        push(item: T): void {
            this.data.push(item);
            this.bubbleUp(this.data.length - 1);
        }
        pop(): T | undefined {
            if (this.data.length === 0) return undefined;
            const top = this.data[0];
            const last = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.cmp(this.data[idx], this.data[parent])) {
                    [this.data[idx], this.data[parent]] = [this.data[parent], this.data[idx]];
                    idx = parent;
                } else break;
            }
        }
        private bubbleDown(idx: number): void {
            const n = this.data.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && this.cmp(this.data[left], this.data[smallest])) smallest = left;
                if (right < n && this.cmp(this.data[right], this.data[smallest])) smallest = right;
                if (smallest !== idx) {
                    [this.data[idx], this.data[smallest]] = [this.data[smallest], this.data[idx]];
                    idx = smallest;
                } else break;
            }
        }
    }

    const friends = times.map((t, i) => ({ arrival: t[0], leave: t[1], idx: i }));
    friends.sort((a, b) => a.arrival - b.arrival);

    const occupied = new MinHeap<[number, number]>((a, b) => a[0] < b[0]); // [leaveTime, chair]
    const available = new MinHeap<number>((a, b) => a < b); // chair numbers
    let nextChair = 0;

    for (const f of friends) {
        while (occupied.size() > 0 && occupied.peek()![0] <= f.arrival) {
            const [, chair] = occupied.pop()!;
            available.push(chair);
        }

        let chair: number;
        if (available.size() > 0) {
            chair = available.pop()!;
        } else {
            chair = nextChair++;
        }

        if (f.idx === targetFriend) return chair;

        occupied.push([f.leave, chair]);
    }

    return -1; // should never reach here
}
```

## Php

```php
class MinLeaveHeap extends SplHeap {
    protected function compare($a, $b) {
        // $a and $b are arrays [leaveTime, chair]
        if ($a[0] === $b[0]) return 0;
        // smaller leave time should be extracted first -> higher priority
        return ($a[0] < $b[0]) ? 1 : -1;
    }
}

class Solution {
    /**
     * @param Integer[][] $times
     * @param Integer $targetFriend
     * @return Integer
     */
    function smallestChair($times, $targetFriend) {
        $n = count($times);
        // attach original index to each friend
        $friends = [];
        for ($i = 0; $i < $n; $i++) {
            $friends[] = [$times[$i][0], $times[$i][1], $i];
        }
        usort($friends, function($a, $b) {
            return $a[0] <=> $b[0]; // sort by arrival time
        });

        $available = new SplMinHeap();
        for ($i = 0; $i < $n; $i++) {
            $available->insert($i);
        }

        $occupied = new MinLeaveHeap(); // stores [leaveTime, chair]

        foreach ($friends as $f) {
            [$arr, $lev, $idx] = $f;

            // free chairs whose owners have left by current arrival time
            while (!$occupied->isEmpty()) {
                $occupied->top();
                $top = $occupied->current(); // [leaveTime, chair]
                if ($top[0] <= $arr) {
                    $occupied->extract();
                    $available->insert($top[1]);
                } else {
                    break;
                }
            }

            // assign smallest available chair
            $chair = $available->extract();

            if ($idx === $targetFriend) {
                return $chair;
            }

            // mark this chair as occupied until leaving time
            $occupied->insert([$lev, $chair]);
        }

        return -1; // should never reach here with valid input
    }
}
```

## Swift

```swift
class Solution {
    func smallestChair(_ times: [[Int]], _ targetFriend: Int) -> Int {
        let n = times.count
        var friends: [(arrival: Int, leave: Int, idx: Int)] = []
        for i in 0..<n {
            friends.append((times[i][0], times[i][1], i))
        }
        friends.sort { $0.arrival < $1.arrival }

        var available = Heap<Int>(sort: <)                 // smallest free chair
        var occupied = Heap<(Int, Int)>(sort: { $0.0 < $1.0 }) // (leaveTime, chair)

        var nextChair = 0

        for f in friends {
            let arrival = f.arrival
            while let top = occupied.peek(), top.0 <= arrival {
                if let freed = occupied.pop() {
                    available.push(freed.1)
                }
            }

            let chair: Int
            if !available.isEmpty {
                chair = available.pop()!
            } else {
                chair = nextChair
                nextChair += 1
            }

            if f.idx == targetFriend {
                return chair
            }

            occupied.push((f.leave, chair))
        }
        return -1
    }
}

// Generic min-heap implementation
struct Heap<Element> {
    private var elements: [Element] = []
    private let priorityFunction: (Element, Element) -> Bool

    init(sort: @escaping (Element, Element) -> Bool) {
        self.priorityFunction = sort
    }

    var isEmpty: Bool { elements.isEmpty }
    func peek() -> Element? { elements.first }

    mutating func push(_ value: Element) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }

    mutating func pop() -> Element? {
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
        while child > 0 && priorityFunction(elements[child], elements[parent]) {
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

            if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestChair(times: Array<IntArray>, targetFriend: Int): Int {
        val n = times.size
        // Order friends by arrival time
        val order = (0 until n).sortedBy { times[it][0] }

        val occupied = java.util.PriorityQueue<Pair<Int, Int>>(compareBy { it.first }) // (leaveTime, chair)
        val available = java.util.PriorityQueue<Int>() // free chairs
        var nextChair = 0

        for (idx in order) {
            val arrival = times[idx][0]
            val leave = times[idx][1]

            // Release chairs of friends who have left by now
            while (occupied.isNotEmpty() && occupied.peek().first <= arrival) {
                val freed = occupied.poll()
                available.offer(freed.second)
            }

            // Assign the smallest free chair
            val chair = if (available.isNotEmpty()) {
                available.poll()
            } else {
                val c = nextChair
                nextChair++
                c
            }

            if (idx == targetFriend) return chair

            occupied.offer(Pair(leave, chair))
        }
        // Should never reach here with valid input
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Occupied implements Comparable<Occupied> {
  final int leave;
  final int chair;
  Occupied(this.leave, this.chair);
  @override
  int compareTo(Occupied other) {
    if (leave != other.leave) return leave - other.leave;
    return chair - other.chair;
  }
}

class Solution {
  int smallestChair(List<List<int>> times, int targetFriend) {
    int n = times.length;
    List<List<int>> friends = [];
    for (int i = 0; i < n; i++) {
      friends.add([times[i][0], times[i][1], i]); // arrival, leave, index
    }
    friends.sort((a, b) => a[0] - b[0]);

    SplayTreeSet<int> freeChairs = SplayTreeSet<int>();
    SplayTreeSet<Occupied> occupied = SplayTreeSet<Occupied>();
    int nextChair = 0;

    for (var f in friends) {
      int arrival = f[0];
      int leave = f[1];
      int idx = f[2];

      // Release chairs whose owners have left
      while (occupied.isNotEmpty && occupied.first.leave <= arrival) {
        freeChairs.add(occupied.first.chair);
        occupied.remove(occupied.first);
      }

      int chair;
      if (freeChairs.isNotEmpty) {
        chair = freeChairs.first;
        freeChairs.remove(chair);
      } else {
        chair = nextChair;
        nextChair++;
      }

      occupied.add(Occupied(leave, chair));

      if (idx == targetFriend) return chair;
    }
    return -1; // should never reach here
  }
}
```

## Golang

```go
import (
	"container/heap"
	"sort"
)

type intHeap []int

func (h intHeap) Len() int           { return len(h) }
func (h intHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h intHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *intHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type occ struct {
	leave int
	chair int
}

type occHeap []occ

func (h occHeap) Len() int           { return len(h) }
func (h occHeap) Less(i, j int) bool { return h[i].leave < h[j].leave }
func (h occHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *occHeap) Push(x interface{}) {
	*h = append(*h, x.(occ))
}

func (h *occHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type friend struct {
	arrival int
	leave   int
	idx     int
}

func smallestChair(times [][]int, targetFriend int) int {
	n := len(times)
	friends := make([]friend, n)
	for i, t := range times {
		friends[i] = friend{arrival: t[0], leave: t[1], idx: i}
	}
	sort.Slice(friends, func(i, j int) bool { return friends[i].arrival < friends[j].arrival })

	available := &intHeap{}
	heap.Init(available)
	occupied := &occHeap{}
	heap.Init(occupied)

	nextChair := 0

	for _, f := range friends {
		// free chairs whose owners have left
		for occupied.Len() > 0 && (*occupied)[0].leave <= f.arrival {
			ch := heap.Pop(occupied).(occ).chair
			heap.Push(available, ch)
		}
		var chair int
		if available.Len() > 0 {
			chair = heap.Pop(available).(int)
		} else {
			chair = nextChair
			nextChair++
		}
		if f.idx == targetFriend {
			return chair
		}
		heap.Push(occupied, occ{leave: f.leave, chair: chair})
	}
	return -1
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(val)
    @data << val
    i = @data.size - 1
    while i > 0
      p = (i - 1) / 2
      break if @data[p] <= @data[i]
      @data[p], @data[i] = @data[i], @data[p]
      i = p
    end
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      n = @data.size
      loop do
        l = 2 * i + 1
        r = l + 1
        smallest = i
        smallest = l if l < n && @data[l] < @data[smallest]
        smallest = r if r < n && @data[r] < @data[smallest]
        break if smallest == i
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
    min
  end

  def peek
    @data[0]
  end

  def empty?
    @data.empty?
  end
end

def smallest_chair(times, target_friend)
  friends = []
  times.each_with_index { |(a, l), i| friends << [a, l, i] }
  friends.sort_by! { |f| f[0] }

  occupied = MinHeap.new   # [leave_time, chair]
  freed = MinHeap.new      # chair numbers
  next_chair = 0

  friends.each do |arr, leave, idx|
    while !occupied.empty? && occupied.peek[0] <= arr
      _, chair = occupied.pop
      freed.push(chair)
    end

    chair = if !freed.empty?
              freed.pop
            else
              c = next_chair
              next_chair += 1
              c
            end

    return chair if idx == target_friend
    occupied.push([leave, chair])
  end
  -1
end
```

## Scala

```scala
object Solution {
    import java.util.PriorityQueue

    def smallestChair(times: Array[Array[Int]], targetFriend: Int): Int = {
        val n = times.length
        // Build array of (arrival, leave, index)
        val friends = new Array[(Int, Int, Int)](n)
        var i = 0
        while (i < n) {
            friends(i) = (times(i)(0), times(i)(1), i)
            i += 1
        }
        // Sort by arrival time
        val sortedFriends = friends.sortBy(_._1)

        val available = new PriorityQueue[Int]() // smallest free chair
        val occupied = new PriorityQueue[(Int, Int)](
            (a: (Int, Int), b: (Int, Int)) => Integer.compare(a._1, b._1)
        ) // (leaveTime, chair)

        var nextChair = 0

        for ((arr, leave, idx) <- sortedFriends) {
            // Free chairs of friends who have left by current arrival time
            while (!occupied.isEmpty && occupied.peek()._1 <= arr) {
                val freed = occupied.poll()
                available.add(freed._2)
            }

            // Assign smallest available chair
            val chair =
                if (available.isEmpty) {
                    val c = nextChair
                    nextChair += 1
                    c
                } else {
                    available.poll()
                }

            if (idx == targetFriend) return chair

            occupied.add((leave, chair))
        }
        -1 // should never reach here with valid input
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn smallest_chair(times: Vec<Vec<i32>>, target_friend: i32) -> i32 {
        let n = times.len();
        // (arrival, leaving, original index)
        let mut friends: Vec<(i32, i32, usize)> = (0..n)
            .map(|i| (times[i][0], times[i][1], i))
            .collect();
        friends.sort_by_key(|k| k.0);

        // occupied chairs: (leaving time, chair index)
        let mut occupied: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        // available chairs indices
        let mut available: BinaryHeap<Reverse<i32>> = BinaryHeap::new();

        let mut next_chair: i32 = 0;

        for (arr, leave, idx) in friends {
            // free chairs whose owners have left by current arrival time
            while let Some(&Reverse((lt, ch))) = occupied.peek() {
                if lt <= arr {
                    let Reverse((_lt2, ch2)) = occupied.pop().unwrap();
                    available.push(Reverse(ch2));
                } else {
                    break;
                }
            }

            // assign smallest available chair
            let chair: i32 = if let Some(Reverse(ch)) = available.pop() {
                ch
            } else {
                let ch = next_chair;
                next_chair += 1;
                ch
            };

            if idx as i32 == target_friend {
                return chair;
            }

            occupied.push(Reverse((leave, chair)));
        }

        -1 // should never reach here with valid input
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/heap)

(define (smallest-chair times targetFriend)
  (let* ((n (length times))
         (indexed
           (for/list ([i (in-range n)]
                      [pair (in-list times)])
             (list (first pair) (second pair) i)))
         (sorted (sort indexed (lambda (a b) (< (first a) (first b)))))
         (available (make-heap <))
         (occupied (make-heap
                    (lambda (x y)
                      (< (first x) (first y))))))
    ;; initialize available chairs 0..n-1
    (for ([i (in-range n)])
      (heap-add! available i))
    (let recur ((lst sorted))
      (if (null? lst)
          -1 ; should not happen
          (let* ((entry (car lst))
                 (arrival (first entry))
                 (leave   (second entry))
                 (idx     (third entry)))
            ;; free chairs whose leave time <= current arrival
            (let loop-free ()
              (when (and (not (heap-empty? occupied))
                         (<= (first (heap-min occupied)) arrival))
                (define minpair (heap-remove-min! occupied))
                (heap-add! available (second minpair))
                (loop-free)))
            (define chair (heap-remove-min! available))
            (if (= idx targetFriend)
                chair
                (begin
                  (heap-add! occupied (list leave chair))
                  (recur (cdr lst)))))))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_chair/2]).

-spec smallest_chair(Times :: [[integer()]], TargetFriend :: integer()) -> integer().
smallest_chair(Times, TargetFriend) ->
    Indexed = lists:zipwith(
                fun(Index, [A, L]) -> {A, L, Index} end,
                lists:seq(0, length(Times) - 1),
                Times),
    Sorted = lists:keysort(1, Indexed),
    process(Sorted, TargetFriend, gb_trees:empty(), gb_trees:empty(), 0).

process([], _Target, _Occupied, _Avail, _Next) ->
    -1; % should never happen
process([{Arr, Leave, Id} | Rest], Target, Occupied, Avail, Next) ->
    {OccAfterFree, AvailAfterFree} = free_until(Occupied, Arr, Avail),
    Assign =
        case gb_trees:is_empty(AvailAfterFree) of
            true  -> {Next, AvailAfterFree, Next + 1};
            false ->
                {C, _} = gb_trees:smallest(AvailAfterFree),
                {C, gb_trees:delete(C, AvailAfterFree), Next}
        end,
    {Chair, NewAvail, Next2} = Assign,
    case Id of
        Target -> Chair;
        _ ->
            Occupied2 =
                case gb_trees:lookup(Leave, OccAfterFree) of
                    none -> gb_trees:insert(Leave, [Chair], OccAfterFree);
                    {value, List} -> gb_trees:update(Leave, [Chair | List], OccAfterFree)
                end,
            process(Rest, Target, Occupied2, NewAvail, Next2)
    end.

free_until(Occupied, Time, Avail) ->
    case gb_trees:is_empty(Occupied) of
        true -> {Occupied, Avail};
        false ->
            {LeaveTime, ChairsList} = gb_trees:smallest(Occupied),
            if LeaveTime =< Time ->
                    {_Key, _Val, RestOcc} = gb_trees:take_smallest(Occupied),
                    NewAvail = lists:foldl(
                                 fun(C, Acc) -> gb_trees:insert(C, true, Acc) end,
                                 Avail, ChairsList),
                    free_until(RestOcc, Time, NewAvail);
               true ->
                    {Occupied, Avail}
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_chair(times :: [[integer]], target_friend :: integer) :: integer
  def smallest_chair(times, target_friend) do
    sorted =
      times
      |> Enum.with_index()
      |> Enum.map(fn {{a, l}, i} -> {a, l, i} end)
      |> Enum.sort_by(fn {a, _, _} -> a end)

    process(sorted, :gb_trees.empty(), :gb_sets.empty(), 0, target_friend)
  end

  defp process([], _occ, _avail, _next, _target), do: -1

  defp process([{arr, leave, idx} | rest], occ, avail, next_chair, target) do
    {occ2, avail2} = free_up(arr, occ, avail)

    if not :gb_sets.is_empty(avail2) do
      chair = :gb_sets.smallest(avail2)
      avail3 = :gb_sets.delete(chair, avail2)
      next_chair3 = next_chair

      if idx == target do
        chair
      else
        occ3 = insert_occupied(occ2, leave, chair)
        process(rest, occ3, avail3, next_chair3, target)
      end
    else
      chair = next_chair
      avail3 = avail2
      next_chair3 = next_chair + 1

      if idx == target do
        chair
      else
        occ3 = insert_occupied(occ2, leave, chair)
        process(rest, occ3, avail3, next_chair3, target)
      end
    end
  end

  defp free_up(arrival, occ, avail) do
    if :gb_trees.is_empty(occ) do
      {occ, avail}
    else
      {{leave, chairs}, rest_occ} = :gb_trees.take_smallest(occ)

      if leave <= arrival do
        [chair | remaining] = chairs
        new_avail = :gb_sets.add(chair, avail)

        new_occ =
          if remaining == [] do
            rest_occ
          else
            :gb_trees.insert(leave, remaining, rest_occ)
          end

        free_up(arrival, new_occ, new_avail)
      else
        # put the node back since it's not ready to be freed
        occ_back = :gb_trees.insert(leave, chairs, rest_occ)
        {occ_back, avail}
      end
    end
  end

  defp insert_occupied(occ, leave, chair) do
    case :gb_trees.lookup(leave, occ) do
      :none -> :gb_trees.insert(leave, [chair], occ)
      {:value, list} -> :gb_trees.update(leave, [chair | list], occ)
    end
  end
end
```

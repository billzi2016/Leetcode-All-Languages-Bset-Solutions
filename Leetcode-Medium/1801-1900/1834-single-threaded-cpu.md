# 1834. Single-Threaded CPU

## Cpp

```cpp
class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        struct Task {int enq; int proc; int idx;};
        int n = tasks.size();
        vector<Task> arr;
        arr.reserve(n);
        for (int i = 0; i < n; ++i)
            arr.push_back({tasks[i][0], tasks[i][1], i});
        sort(arr.begin(), arr.end(), [](const Task& a, const Task& b) {
            return a.enq < b.enq;
        });
        
        auto cmp = [](const Task& a, const Task& b) {
            if (a.proc != b.proc) return a.proc > b.proc; // smaller processing time first
            return a.idx > b.idx;                         // then smaller index
        };
        priority_queue<Task, vector<Task>, decltype(cmp)> pq(cmp);
        
        vector<int> order;
        order.reserve(n);
        long long curTime = 0;
        int i = 0;
        while (i < n || !pq.empty()) {
            if (pq.empty() && curTime < arr[i].enq)
                curTime = arr[i].enq;
            while (i < n && arr[i].enq <= curTime) {
                pq.push(arr[i]);
                ++i;
            }
            Task t = pq.top(); pq.pop();
            order.push_back(t.idx);
            curTime += t.proc;
        }
        return order;
    }
};
```

## Java

```java
class Solution {
    private static class Task {
        int enqueue;
        int process;
        int index;
        Task(int e, int p, int i) {
            this.enqueue = e;
            this.process = p;
            this.index = i;
        }
    }

    public int[] getOrder(int[][] tasks) {
        int n = tasks.length;
        Task[] arr = new Task[n];
        for (int i = 0; i < n; i++) {
            arr[i] = new Task(tasks[i][0], tasks[i][1], i);
        }
        java.util.Arrays.sort(arr, (a, b) -> Integer.compare(a.enqueue, b.enqueue));

        java.util.PriorityQueue<Task> pq = new java.util.PriorityQueue<>(
                (a, b) -> a.process != b.process ? Integer.compare(a.process, b.process)
                                                : Integer.compare(a.index, b.index));

        int[] order = new int[n];
        int pos = 0;
        long time = 0;
        int i = 0;

        while (pos < n) {
            // enqueue all tasks that have become available by current time
            while (i < n && arr[i].enqueue <= time) {
                pq.offer(arr[i]);
                i++;
            }
            if (pq.isEmpty()) {
                // no task is ready, jump to next task's enqueue time
                time = arr[i].enqueue;
                continue;
            }
            Task cur = pq.poll();
            order[pos++] = cur.index;
            time += cur.process;
        }

        return order;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        n = len(tasks)
        # attach original indices
        indexed_tasks = [(enq, proc, i) for i, (enq, proc) in enumerate(tasks)]
        indexed_tasks.sort(key=lambda x: x[0])  # sort by enqueue time
        
        result = []
        heap = []  # (processingTime, index)
        time = 0
        i = 0  # pointer in indexed_tasks
        
        while i < n or heap:
            # load all tasks that have arrived by current time
            while i < n and indexed_tasks[i][0] <= time:
                enq, proc, idx = indexed_tasks[i]
                heapq.heappush(heap, (proc, idx))
                i += 1
            
            if not heap:
                # no available tasks, jump to next enqueue time
                time = indexed_tasks[i][0]
                continue
            
            proc, idx = heapq.heappop(heap)
            result.append(idx)
            time += proc
        
        return result
```

## Python3

```python
class Solution:
    def getOrder(self, tasks):
        # Attach original indices
        indexed = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        indexed.sort(key=lambda x: x[0])  # sort by enqueue time

        result = []
        heap = []  # will store (processingTime, index)
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            # Load all tasks that have arrived by current time
            while i < n and indexed[i][0] <= time:
                et, pt, idx = indexed[i]
                heap.append((pt, idx))
                i += 1
            if not heap:
                # No available tasks, jump to next enqueue time
                time = indexed[i][0]
                continue
            # Use a heap for efficient min extraction
            import heapq
            heapq.heapify(heap) if len(heap) == 1 else None  # ensure heap property when first element added
            pt, idx = heapq.heappop(heap)
            result.append(idx)
            time += pt

        return result
```

## C

```c
#include <stdlib.h>

typedef struct {
    int enq;
    int proc;
    int idx;
} Task;

/* Comparator for sorting tasks by enqueue time */
static int cmpTask(const void *a, const void *b) {
    const Task *t1 = (const Task *)a;
    const Task *t2 = (const Task *)b;
    if (t1->enq != t2->enq)
        return t1->enq - t2->enq;
    return t1->idx - t2->idx;
}

/* Min‑heap based on processing time then index */
typedef struct {
    Task *data;
    int size;
    int capacity;
} Heap;

/* Create a heap with given capacity */
static Heap* heapCreate(int cap) {
    Heap *h = (Heap *)malloc(sizeof(Heap));
    h->data = (Task *)malloc(sizeof(Task) * cap);
    h->size = 0;
    h->capacity = cap;
    return h;
}

/* Free heap memory */
static void heapFree(Heap *h) {
    if (!h) return;
    free(h->data);
    free(h);
}

/* Return true if a has higher priority than b */
static int taskLess(const Task *a, const Task *b) {
    if (a->proc != b->proc)
        return a->proc < b->proc;
    return a->idx < b->idx;
}

/* Sift up element at position i */
static void heapSiftUp(Heap *h, int i) {
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (!taskLess(&h->data[i], &h->data[p]))
            break;
        Task tmp = h->data[i];
        h->data[i] = h->data[p];
        h->data[p] = tmp;
        i = p;
    }
}

/* Sift down element at position i */
static void heapSiftDown(Heap *h, int i) {
    while (1) {
        int l = (i << 1) + 1;
        int r = l + 1;
        int smallest = i;

        if (l < h->size && taskLess(&h->data[l], &h->data[smallest]))
            smallest = l;
        if (r < h->size && taskLess(&h->data[r], &h->data[smallest]))
            smallest = r;

        if (smallest == i)
            break;

        Task tmp = h->data[i];
        h->data[i] = h->data[smallest];
        h->data[smallest] = tmp;
        i = smallest;
    }
}

/* Push a task into the heap */
static void heapPush(Heap *h, Task t) {
    if (h->size == h->capacity) {
        h->capacity <<= 1;
        h->data = (Task *)realloc(h->data, sizeof(Task) * h->capacity);
    }
    h->data[h->size] = t;
    heapSiftUp(h, h->size);
    h->size++;
}

/* Pop the top task from the heap */
static Task heapPop(Heap *h) {
    Task top = h->data[0];
    h->size--;
    if (h->size > 0) {
        h->data[0] = h->data[h->size];
        heapSiftDown(h, 0);
    }
    return top;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getOrder(int** tasks, int tasksSize, int* tasksColSize, int* returnSize) {
    if (tasksSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    Task *arr = (Task *)malloc(sizeof(Task) * tasksSize);
    for (int i = 0; i < tasksSize; ++i) {
        arr[i].enq = tasks[i][0];
        arr[i].proc = tasks[i][1];
        arr[i].idx = i;
    }

    qsort(arr, tasksSize, sizeof(Task), cmpTask);

    Heap *heap = heapCreate(tasksSize);
    int *order = (int *)malloc(sizeof(int) * tasksSize);
    int outPos = 0;

    long long time = 0;
    int idx = 0;   // index in sorted array

    while (outPos < tasksSize) {
        /* Enqueue all tasks that have arrived by current time */
        while (idx < tasksSize && arr[idx].enq <= time) {
            heapPush(heap, arr[idx]);
            ++idx;
        }

        if (heap->size > 0) {
            Task cur = heapPop(heap);
            order[outPos++] = cur.idx;
            time += cur.proc;
        } else {
            /* No available tasks; jump to next enqueue time */
            time = arr[idx].enq;
        }
    }

    heapFree(heap);
    free(arr);

    *returnSize = tasksSize;
    return order;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] GetOrder(int[][] tasks) {
        int n = tasks.Length;
        var taskArr = new (int enq, int proc, int idx)[n];
        for (int i = 0; i < n; i++) {
            taskArr[i] = (tasks[i][0], tasks[i][1], i);
        }
        Array.Sort(taskArr, (a, b) => a.enq.CompareTo(b.enq));

        var pq = new PriorityQueue<(int proc, int idx), long>();
        var order = new List<int>(n);
        long time = 0;
        int ptr = 0;

        while (order.Count < n) {
            while (ptr < n && taskArr[ptr].enq <= time) {
                var t = taskArr[ptr];
                long priority = ((long)t.proc << 32) | (uint)t.idx;
                pq.Enqueue((t.proc, t.idx), priority);
                ptr++;
            }

            if (pq.Count > 0) {
                var cur = pq.Dequeue();
                order.Add(cur.idx);
                time += cur.proc;
            } else {
                time = taskArr[ptr].enq;
            }
        }

        return order.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} tasks
 * @return {number[]}
 */
var getOrder = function(tasks) {
    const n = tasks.length;
    const indexed = tasks.map((t, i) => [t[0], t[1], i]); // enqueueTime, processingTime, index
    indexed.sort((a, b) => a[0] === b[0] ? a[2] - b[2] : a[0] - b[0]);

    class MinHeap {
        constructor(comp) {
            this.heap = [];
            this.comp = comp;
        }
        isEmpty() { return this.heap.length === 0; }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.comp(h[i], h[p]) < 0) {
                    [h[i], h[p]] = [h[p], h[i]];
                    i = p;
                } else break;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const top = h[0];
            const end = h.pop();
            if (h.length > 0) {
                h[0] = end;
                let i = 0;
                while (true) {
                    const l = i * 2 + 1;
                    const r = l + 1;
                    let smallest = i;
                    if (l < h.length && this.comp(h[l], h[smallest]) < 0) smallest = l;
                    if (r < h.length && this.comp(h[r], h[smallest]) < 0) smallest = r;
                    if (smallest !== i) {
                        [h[i], h[smallest]] = [h[smallest], h[i]];
                        i = smallest;
                    } else break;
                }
            }
            return top;
        }
    }

    const heap = new MinHeap((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]); // [processingTime, index]
    const result = [];
    let time = 0;
    let i = 0;

    while (result.length < n) {
        while (i < n && indexed[i][0] <= time) {
            heap.push([indexed[i][1], indexed[i][2]]);
            i++;
        }
        if (heap.isEmpty()) {
            time = indexed[i][0];
            continue;
        }
        const [proc, idx] = heap.pop();
        time += proc;
        result.push(idx);
    }

    return result;
};
```

## Typescript

```typescript
function getOrder(tasks: number[][]): number[] {
    const n = tasks.length;
    const indexed = tasks.map((t, i) => ({ enq: t[0], proc: t[1], idx: i }));
    indexed.sort((a, b) => a.enq - b.enq);

    class MinHeap {
        private data: { enq: number; proc: number; idx: number }[] = [];
        isEmpty(): boolean { return this.data.length === 0; }
        push(item: { enq: number; proc: number; idx: number }): void {
            this.data.push(item);
            this.bubbleUp(this.data.length - 1);
        }
        pop(): { enq: number; proc: number; idx: number } | undefined {
            if (this.isEmpty()) return undefined;
            const top = this.data[0];
            const last = this.data.pop()!;
            if (!this.isEmpty()) {
                this.data[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.compare(this.data[idx], this.data[parent]) < 0) {
                    [this.data[idx], this.data[parent]] = [this.data[parent], this.data[idx]];
                    idx = parent;
                } else break;
            }
        }
        private bubbleDown(idx: number): void {
            const n = this.data.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let smallest = idx;
                if (left < n && this.compare(this.data[left], this.data[smallest]) < 0) smallest = left;
                if (right < n && this.compare(this.data[right], this.data[smallest]) < 0) smallest = right;
                if (smallest !== idx) {
                    [this.data[idx], this.data[smallest]] = [this.data[smallest], this.data[idx]];
                    idx = smallest;
                } else break;
            }
        }
        private compare(a: { proc: number; idx: number }, b: { proc: number; idx: number }): number {
            if (a.proc !== b.proc) return a.proc - b.proc;
            return a.idx - b.idx;
        }
    }

    const heap = new MinHeap();
    let time = 0;
    let i = 0;
    const result: number[] = [];

    while (result.length < n) {
        while (i < n && indexed[i].enq <= time) {
            heap.push(indexed[i]);
            i++;
        }
        if (heap.isEmpty()) {
            time = indexed[i].enq;
            continue;
        }
        const task = heap.pop()!;
        result.push(task.idx);
        time += task.proc;
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $tasks
     * @return Integer[]
     */
    function getOrder($tasks) {
        $n = count($tasks);
        $arr = [];
        for ($i = 0; $i < $n; $i++) {
            $arr[] = [$tasks[$i][0], $tasks[$i][1], $i]; // [enqueue, processing, index]
        }
        usort($arr, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        $time = 0;
        $i = 0;
        $result = [];

        while ($i < $n || !$pq->isEmpty()) {
            if ($pq->isEmpty() && $time < $arr[$i][0]) {
                $time = $arr[$i][0];
            }

            while ($i < $n && $arr[$i][0] <= $time) {
                $proc = $arr[$i][1];
                $idx  = $arr[$i][2];
                // priority: smaller processing time, then smaller index
                $priority = [-$proc, -$idx];
                $pq->insert([$proc, $idx], $priority);
                $i++;
            }

            if (!$pq->isEmpty()) {
                $task = $pq->extract(); // [$proc, $idx]
                $result[] = $task[1];
                $time += $task[0];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    struct Task {
        let start: Int
        let duration: Int
        let idx: Int
    }

    class MinHeap {
        private var data: [Task] = []

        private func less(_ a: Task, _ b: Task) -> Bool {
            if a.duration != b.duration {
                return a.duration < b.duration
            }
            return a.idx < b.idx
        }

        var isEmpty: Bool { data.isEmpty }

        func push(_ task: Task) {
            data.append(task)
            siftUp(data.count - 1)
        }

        func pop() -> Task {
            let top = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                siftDown(0)
            }
            return top
        }

        private func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) / 2
                if less(data[child], data[parent]) {
                    data.swapAt(child, parent)
                    child = parent
                } else { break }
            }
        }

        private func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent

                if left < data.count && less(data[left], data[smallest]) {
                    smallest = left
                }
                if right < data.count && less(data[right], data[smallest]) {
                    smallest = right
                }
                if smallest == parent { break }
                data.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }

    func getOrder(_ tasks: [[Int]]) -> [Int] {
        let n = tasks.count
        var taskList: [Task] = []
        taskList.reserveCapacity(n)
        for (i, t) in tasks.enumerated() {
            taskList.append(Task(start: t[0], duration: t[1], idx: i))
        }
        taskList.sort { $0.start < $1.start }

        var result: [Int] = []
        result.reserveCapacity(n)

        let heap = MinHeap()
        var time = 0
        var i = 0

        while i < n || !heap.isEmpty {
            if heap.isEmpty && time < taskList[i].start {
                time = taskList[i].start
            }
            while i < n && taskList[i].start <= time {
                heap.push(taskList[i])
                i += 1
            }
            let cur = heap.pop()
            result.append(cur.idx)
            time += cur.duration
        }

        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    data class Task(val enqueueTime: Int, val processingTime: Int, val index: Int)

    fun getOrder(tasks: Array<IntArray>): IntArray {
        val n = tasks.size
        val taskList = ArrayList<Task>(n)
        for (i in 0 until n) {
            taskList.add(Task(tasks[i][0], tasks[i][1], i))
        }
        taskList.sortBy { it.enqueueTime }

        val pq = java.util.PriorityQueue<Task> { a, b ->
            if (a.processingTime != b.processingTime) {
                a.processingTime - b.processingTime
            } else {
                a.index - b.index
            }
        }

        var time = 0L
        var i = 0
        val result = IntArray(n)
        var pos = 0

        while (pos < n) {
            // enqueue all tasks that have arrived by current time
            while (i < n && taskList[i].enqueueTime.toLong() <= time) {
                pq.add(taskList[i])
                i++
            }

            if (pq.isNotEmpty()) {
                val cur = pq.poll()
                result[pos++] = cur.index
                time += cur.processingTime.toLong()
            } else {
                // no tasks available, jump to next task's enqueue time
                if (i < n) {
                    time = taskList[i].enqueueTime.toLong()
                }
            }
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> getOrder(List<List<int>> tasks) {
    int n = tasks.length;
    List<List<int>> sorted = [];
    for (int i = 0; i < n; i++) {
      sorted.add([tasks[i][0], tasks[i][1], i]); // [enqueue, processing, index]
    }
    sorted.sort((a, b) {
      if (a[0] != b[0]) return a[0] - b[0];
      return a[2] - b[2];
    });

    var heap = _MinHeap();
    List<int> result = [];
    int time = 0;
    int i = 0;

    while (result.length < n) {
      // add all tasks that have arrived by current time
      while (i < n && sorted[i][0] <= time) {
        heap.push([sorted[i][1], sorted[i][2]]); // [processing, index]
        i++;
      }

      if (!heap.isEmpty) {
        var cur = heap.pop();
        int proc = cur[0];
        int idx = cur[1];
        result.add(idx);
        time += proc;
      } else {
        // no available tasks, jump to next enqueue time
        time = sorted[i][0];
      }
    }

    return result;
  }
}

class _MinHeap {
  final List<List<int>> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void push(List<int> val) {
    _heap.add(val);
    _siftUp(_heap.length - 1);
  }

  List<int> pop() {
    var top = _heap[0];
    var last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return top;
  }

  int _compare(List<int> a, List<int> b) {
    if (a[0] != b[0]) return a[0] - b[0];
    return a[1] - b[1];
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_compare(_heap[idx], _heap[parent]) < 0) {
        var tmp = _heap[idx];
        _heap[idx] = _heap[parent];
        _heap[parent] = tmp;
        idx = parent;
      } else {
        break;
      }
    }
  }

  void _siftDown(int idx) {
    int n = _heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _compare(_heap[left], _heap[smallest]) < 0) {
        smallest = left;
      }
      if (right < n && _compare(_heap[right], _heap[smallest]) < 0) {
        smallest = right;
      }

      if (smallest != idx) {
        var tmp = _heap[idx];
        _heap[idx] = _heap[smallest];
        _heap[smallest] = tmp;
        idx = smallest;
      } else {
        break;
      }
    }
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

type task struct {
	enqueue int
	process int
	idx     int
}

// min-heap based on processing time, then index
type taskHeap []task

func (h taskHeap) Len() int { return len(h) }
func (h taskHeap) Less(i, j int) bool {
	if h[i].process == h[j].process {
		return h[i].idx < h[j].idx
	}
	return h[i].process < h[j].process
}
func (h taskHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *taskHeap) Push(x interface{}) {
	*h = append(*h, x.(task))
}

func (h *taskHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func getOrder(tasks [][]int) []int {
	n := len(tasks)
	if n == 0 {
		return nil
	}
	// attach original indices and sort by enqueue time
	ts := make([]task, n)
	for i, t := range tasks {
		ts[i] = task{enqueue: t[0], process: t[1], idx: i}
	}
	sort.Slice(ts, func(i, j int) bool {
		return ts[i].enqueue < ts[j].enqueue
	})

	h := &taskHeap{}
	heap.Init(h)

	result := make([]int, 0, n)
	time := 0
	i := 0 // pointer in sorted tasks

	for len(result) < n {
		// enqueue all tasks that have become available by current time
		for i < n && ts[i].enqueue <= time {
			heap.Push(h, ts[i])
			i++
		}
		if h.Len() > 0 {
			cur := heap.Pop(h).(task)
			result = append(result, cur.idx)
			time += cur.process
		} else {
			// no tasks available, jump to next enqueue time
			if i < n {
				time = ts[i].enqueue
			}
		}
	}
	return result
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(item)
    @data << item
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    min
  end

  def empty?
    @data.empty?
  end

  private

  # item format: [processing_time, index]
  def compare(a, b)
    if a[0] != b[0]
      a[0] < b[0]
    else
      a[1] < b[1]
    end
  end

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break unless compare(@data[idx], @data[parent])
      @data[idx], @data[parent] = @data[parent], @data[idx]
      idx = parent
    end
  end

  def sift_down(idx)
    n = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < n && compare(@data[left], @data[smallest])
        smallest = left
      end
      if right < n && compare(@data[right], @data[smallest])
        smallest = right
      end
      break if smallest == idx
      @data[idx], @data[smallest] = @data[smallest], @data[idx]
      idx = smallest
    end
  end
end

# @param {Integer[][]} tasks
# @return {Integer[]}
def get_order(tasks)
  n = tasks.length
  indexed_tasks = tasks.each_with_index.map { |(et, pt), i| [et, pt, i] }
  indexed_tasks.sort_by! { |et, _pt, _i| et }

  heap = MinHeap.new
  result = []
  time = 0
  idx = 0

  while result.size < n
    # enqueue all tasks that have become available by current time
    while idx < n && indexed_tasks[idx][0] <= time
      _, pt, i = indexed_tasks[idx]
      heap.push([pt, i])
      idx += 1
    end

    if heap.empty?
      # jump to next task's enqueue time
      time = indexed_tasks[idx][0]
      next
    else
      pt, i = heap.pop
      result << i
      time += pt
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  case class Task(enqueue: Int, proc: Int, idx: Int)

  def getOrder(tasks: Array[Array[Int]]): Array[Int] = {
    val n = tasks.length
    val taskObjs = new Array[Task](n)
    var i = 0
    while (i < n) {
      taskObjs(i) = Task(tasks(i)(0), tasks(i)(1), i)
      i += 1
    }
    val sorted = taskObjs.sortBy(_.enqueue)

    implicit val ordering: Ordering[Task] =
      Ordering.by[Task, (Int, Int)](t => (t.proc, t.idx)).reverse

    val pq = mutable.PriorityQueue.empty[Task]

    var time: Long = 0L
    var idx = 0          // pointer in sorted array
    var resPos = 0       // position in result
    val result = new Array[Int](n)

    while (resPos < n) {
      while (idx < n && sorted(idx).enqueue <= time) {
        pq.enqueue(sorted(idx))
        idx += 1
      }
      if (pq.isEmpty) {
        time = sorted(idx).enqueue
      } else {
        val cur = pq.dequeue()
        result(resPos) = cur.idx
        resPos += 1
        time += cur.proc
      }
    }

    result
  }
}
```

## Rust

```rust
impl Solution {
    pub fn get_order(tasks: Vec<Vec<i32>>) -> Vec<i32> {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let n = tasks.len();
        // (enqueue_time, processing_time, original_index)
        let mut sorted_tasks: Vec<(i64, i64, i32)> = tasks
            .into_iter()
            .enumerate()
            .map(|(idx, v)| (v[0] as i64, v[1] as i64, idx as i32))
            .collect();

        // sort by enqueue time
        sorted_tasks.sort_unstable_by_key(|t| t.0);

        let mut heap: BinaryHeap<Reverse<(i64, i32)>> = BinaryHeap::new();
        let mut result: Vec<i32> = Vec::with_capacity(n);
        let mut i = 0usize;
        let mut time: i64 = 0;

        while result.len() < n {
            // enqueue all tasks that have become available by current time
            while i < n && sorted_tasks[i].0 <= time {
                heap.push(Reverse((sorted_tasks[i].1, sorted_tasks[i].2)));
                i += 1;
            }

            if let Some(Reverse((proc, idx))) = heap.pop() {
                result.push(idx);
                time += proc;
            } else {
                // no tasks available, jump to next enqueue time
                if i < n {
                    time = sorted_tasks[i].0;
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (get-order tasks)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (length tasks)]
         [indexed
          (for/list ([t tasks] [i (in-naturals)])
            (list (first t) (second t) i))]
         [sorted (sort indexed (lambda (a b) (< (first a) (first b))))]
         [heap (make-heap
                (lambda (x y)
                  (let ([px (first x)] [ix (second x)]
                        [py (first y)] [iy (second y)])
                    (or (< px py)
                        (and (= px py) (< ix iy))))))])
    (define (add-tasks i time)
      (let loop ((j i))
        (if (and (< j n) (<= (first (list-ref sorted j)) time))
            (begin
              (heap-add! heap (list (second (list-ref sorted j))
                                    (third (list-ref sorted j))))
              (loop (+ j 1)))
            j)))
    (let rec ((i 0) (time 0) (result '()))
      (if (= (length result) n)
          (reverse result)
          (let ((new-i (add-tasks i time)))
            (if (not (heap-empty? heap))
                (let* ([top (heap-min heap)]
                       [proc (first top)]
                       [idx (second top)])
                  (heap-remove-min! heap)
                  (rec new-i (+ time proc) (cons idx result)))
                (if (< new-i n)
                    (rec new-i (first (list-ref sorted new-i)) result)
                    (reverse result))))))))
```

## Erlang

```erlang
-module(solution).
-export([get_order/1]).

-spec get_order(Tasks :: [[integer()]]) -> [integer()].
get_order(Tasks) ->
    N = length(Tasks),
    Indexed = lists:zipwith(
                fun({Enq, Proc}, Idx) -> {Enq, Proc, Idx} end,
                Tasks,
                lists:seq(0, N - 1)),
    Sorted = lists:keysort(1, Indexed), % sort by enqueue time
    process(N, Sorted, 0, gb_trees:empty(), []).

process(N, RemTasks, Time, Tree, Acc) when length(Acc) == N ->
    lists:reverse(Acc);
process(N, RemTasks, Time, Tree, Acc) ->
    {Rem2, Tree1} = add_available(RemTasks, Time, Tree),
    case gb_trees:is_empty(Tree1) of
        false ->
            {{Proc, Idx}, _Val} = gb_trees:smallest(Tree1),
            NewTree = gb_trees:delete({Proc, Idx}, Tree1),
            process(N, Rem2, Time + Proc, NewTree, [Idx | Acc]);
        true ->
            case Rem2 of
                [] -> lists:reverse(Acc);
                [{NextEnq, _P, _I} | _] ->
                    process(N, Rem2, NextEnq, Tree1, Acc)
            end
    end.

add_available([], _Time, Tree) ->
    {[], Tree};
add_available([{Enq, Proc, Idx}=Task | Rest], Time, Tree) when Enq =< Time ->
    NewTree = gb_trees:insert({Proc, Idx}, true, Tree),
    add_available(Rest, Time, NewTree);
add_available(Remaining, _Time, Tree) ->
    {Remaining, Tree}.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_order(tasks :: [[integer]]) :: [integer]
  def get_order(tasks) do
    sorted =
      tasks
      |> Enum.with_index()
      |> Enum.map(fn {[enq, proc], idx} -> {enq, proc, idx} end)
      |> Enum.sort_by(fn {enq, _, _} -> enq end)

    loop(sorted, 0, :gb_trees.empty(), [])
  end

  defp loop(remaining, time, heap, acc) do
    {rem2, heap2} = add_available(remaining, time, heap)

    cond do
      not :gb_trees.is_empty(heap2) ->
        {{proc, idx}, _, new_heap} = :gb_trees.take_smallest(heap2)
        loop(rem2, time + proc, new_heap, [idx | acc])

      rem2 != [] ->
        [{next_enq, _, _} | _] = rem2
        loop(rem2, next_enq, heap2, acc)

      true ->
        Enum.reverse(acc)
    end
  end

  defp add_available([ {enq, proc, idx} | rest ], time, heap) when enq <= time do
    new_heap = :gb_trees.insert({proc, idx}, nil, heap)
    add_available(rest, time, new_heap)
  end

  defp add_available(remaining, _time, heap), do: {remaining, heap}
end
```

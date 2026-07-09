# 0630. Course Schedule III

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        sort(courses.begin(), courses.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });
        long long total = 0;
        priority_queue<int> maxDur;
        for (auto& c : courses) {
            int dur = c[0], deadline = c[1];
            total += dur;
            maxDur.push(dur);
            if (total > deadline) {
                total -= maxDur.top();
                maxDur.pop();
            }
        }
        return static_cast<int>(maxDur.size());
    }
};
```

## Java

```java
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> Integer.compare(a[1], b[1]));
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int totalTime = 0;
        for (int[] course : courses) {
            int duration = course[0];
            int lastDay = course[1];
            totalTime += duration;
            maxHeap.offer(duration);
            if (totalTime > lastDay) {
                totalTime -= maxHeap.poll();
            }
        }
        return maxHeap.size();
    }
}
```

## Python

```python
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        import heapq
        # Sort by deadline (lastDay)
        courses.sort(key=lambda x: x[1])
        total_time = 0
        max_heap = []  # store negative durations to simulate max-heap

        for duration, last_day in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)

            if total_time > last_day:
                longest = -heapq.heappop(max_heap)
                total_time -= longest

        return len(max_heap)
```

## Python3

```python
class Solution:
    def scheduleCourse(self, courses):
        import heapq
        # Sort by lastDay to ensure we consider earlier deadlines first
        courses.sort(key=lambda x: x[1])
        total_time = 0
        max_heap = []  # store durations as negative values for a max-heap behavior
        
        for duration, last_day in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)
            if total_time > last_day:
                # Remove the course with the longest duration taken so far
                longest = -heapq.heappop(max_heap)
                total_time -= longest
        return len(max_heap)
```

## C

```c
#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    const int *ca = *(const int **)a;
    const int *cb = *(const int **)b;
    return ca[1] - cb[1];
}

static void heapPush(int *heap, int *size, int val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p] >= heap[i]) break;
        int tmp = heap[p];
        heap[p] = heap[i];
        heap[i] = tmp;
        i = p;
    }
}

static int heapPopMax(int *heap, int *size) {
    int maxVal = heap[0];
    int last = heap[--(*size)];
    if (*size > 0) {
        heap[0] = last;
        int i = 0;
        while (1) {
            int l = i * 2 + 1, r = l + 1, largest = i;
            if (l < *size && heap[l] > heap[largest]) largest = l;
            if (r < *size && heap[r] > heap[largest]) largest = r;
            if (largest == i) break;
            int tmp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = tmp;
            i = largest;
        }
    }
    return maxVal;
}

int scheduleCourse(int** courses, int coursesSize, int* coursesColSize){
    if (coursesSize == 0) return 0;
    qsort(courses, coursesSize, sizeof(int*), cmp);
    
    int *heap = (int *)malloc(sizeof(int) * coursesSize);
    int heapSize = 0;
    int totalTime = 0;
    int count = 0;
    
    for (int i = 0; i < coursesSize; ++i) {
        int dur = courses[i][0];
        int last = courses[i][1];
        if (totalTime + dur <= last) {
            heapPush(heap, &heapSize, dur);
            totalTime += dur;
            ++count;
        } else if (heapSize > 0 && heap[0] > dur) {
            int removed = heapPopMax(heap, &heapSize);
            totalTime -= removed;
            heapPush(heap, &heapSize, dur);
            totalTime += dur;
            // count unchanged
        }
    }
    
    free(heap);
    return count;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int ScheduleCourse(int[][] courses) {
        Array.Sort(courses, (a, b) => a[1].CompareTo(b[1]));
        long total = 0;
        var maxHeap = new PriorityQueue<int, int>();
        foreach (var course in courses) {
            int duration = course[0];
            int lastDay = course[1];
            total += duration;
            maxHeap.Enqueue(duration, -duration); // use negative priority for max-heap
            if (total > lastDay) {
                int longest = maxHeap.Dequeue();
                total -= longest;
            }
        }
        return maxHeap.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} courses
 * @return {number}
 */
var scheduleCourse = function(courses) {
    // Sort by deadline (lastDay)
    courses.sort((a, b) => a[1] - b[1]);

    const maxHeap = new MaxHeap();
    let totalTime = 0;

    for (const [duration, lastDay] of courses) {
        totalTime += duration;
        maxHeap.push(duration);

        if (totalTime > lastDay) {
            // Remove the longest course taken so far
            const longest = maxHeap.pop();
            totalTime -= longest;
        }
    }

    return maxHeap.size();
};

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
        return max;
    }
}
```

## Typescript

```typescript
function scheduleCourse(courses: number[][]): number {
    courses.sort((a, b) => a[1] - b[1]);

    class MaxHeap {
        private heap: number[] = [];

        size(): number {
            return this.heap.length;
        }

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

        pop(): number {
            const h = this.heap;
            const top = h[0];
            const last = h.pop()!;
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let left = i * 2 + 1,
                        right = i * 2 + 2,
                        largest = i;
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

    const maxHeap = new MaxHeap();
    let total = 0;

    for (const [duration, lastDay] of courses) {
        total += duration;
        maxHeap.push(duration);
        if (total > lastDay) {
            total -= maxHeap.pop();
        }
    }

    return maxHeap.size();
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $courses
     * @return Integer
     */
    function scheduleCourse($courses) {
        usort($courses, function ($a, $b) {
            return $a[1] <=> $b[1];
        });

        $total = 0;
        $maxHeap = new SplMaxHeap();

        foreach ($courses as $course) {
            $duration = $course[0];
            $lastDay = $course[1];

            $total += $duration;
            $maxHeap->insert($duration);

            if ($total > $lastDay) {
                $removed = $maxHeap->extract(); // remove longest duration
                $total -= $removed;
            }
        }

        return $maxHeap->count();
    }
}
```

## Swift

```swift
class MaxHeap {
    private var heap: [Int] = []
    
    var count: Int { heap.count }
    
    func push(_ value: Int) {
        heap.append(value)
        siftUp(heap.count - 1)
    }
    
    func pop() -> Int? {
        guard !heap.isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeLast()
        }
        let top = heap[0]
        heap[0] = heap.removeLast()
        siftDown(0)
        return top
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if heap[parent] >= heap[child] { break }
            heap.swapAt(parent, child)
            child = parent
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var largest = parent
            if left < heap.count && heap[left] > heap[largest] { largest = left }
            if right < heap.count && heap[right] > heap[largest] { largest = right }
            if largest == parent { break }
            heap.swapAt(parent, largest)
            parent = largest
        }
    }
}

class Solution {
    func scheduleCourse(_ courses: [[Int]]) -> Int {
        let sortedCourses = courses.sorted { $0[1] < $1[1] }
        var totalTime = 0
        let maxHeap = MaxHeap()
        
        for course in sortedCourses {
            let duration = course[0]
            let lastDay = course[1]
            totalTime += duration
            maxHeap.push(duration)
            
            if totalTime > lastDay {
                if let longest = maxHeap.pop() {
                    totalTime -= longest
                }
            }
        }
        
        return maxHeap.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun scheduleCourse(courses: Array<IntArray>): Int {
        val sorted = courses.sortedWith(compareBy<IntArray> { it[1] })
        var total = 0
        val maxHeap = java.util.PriorityQueue<Int>(java.util.Collections.reverseOrder())
        for (c in sorted) {
            val duration = c[0]
            val lastDay = c[1]
            total += duration
            maxHeap.add(duration)
            if (total > lastDay) {
                val removed = maxHeap.poll()
                total -= removed
            }
        }
        return maxHeap.size
    }
}
```

## Dart

```dart
class MaxHeap {
  final List<int> _data = [];

  void push(int value) {
    _data.add(value);
    int i = _data.length - 1;
    while (i > 0) {
      int parent = (i - 1) >> 1;
      if (_data[parent] >= _data[i]) break;
      int tmp = _data[parent];
      _data[parent] = _data[i];
      _data[i] = tmp;
      i = parent;
    }
  }

  int pop() {
    if (_data.isEmpty) throw StateError('Heap is empty');
    int result = _data[0];
    int last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _heapify(0);
    }
    return result;
  }

  int peek() => _data.isEmpty ? null : _data[0];

  int get length => _data.length;

  void _heapify(int i) {
    int n = _data.length;
    while (true) {
      int left = 2 * i + 1;
      int right = left + 1;
      int largest = i;
      if (left < n && _data[left] > _data[largest]) largest = left;
      if (right < n && _data[right] > _data[largest]) largest = right;
      if (largest == i) break;
      int tmp = _data[i];
      _data[i] = _data[largest];
      _data[largest] = tmp;
      i = largest;
    }
  }
}

class Solution {
  int scheduleCourse(List<List<int>> courses) {
    courses.sort((a, b) => a[1].compareTo(b[1]));
    var heap = MaxHeap();
    int totalTime = 0;

    for (var course in courses) {
      int duration = course[0];
      int lastDay = course[1];

      if (totalTime + duration <= lastDay) {
        totalTime += duration;
        heap.push(duration);
      } else if (heap.length > 0 && heap.peek() > duration) {
        totalTime += duration - heap.pop();
        heap.push(duration);
      }
    }

    return heap.length;
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

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
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

func scheduleCourse(courses [][]int) int {
	sort.Slice(courses, func(i, j int) bool {
		return courses[i][1] < courses[j][1]
	})
	h := &IntHeap{}
	heap.Init(h)
	total := 0
	for _, c := range courses {
		dur, last := c[0], c[1]
		total += dur
		heap.Push(h, dur)
		if total > last {
			maxDur := heap.Pop(h).(int)
			total -= maxDur
		}
	}
	return h.Len()
}
```

## Ruby

```ruby
class MaxHeap
  def initialize
    @data = []
  end

  def <<(val)
    @data << val
    sift_up(@data.size - 1)
    self
  end

  def pop
    return nil if @data.empty?
    max = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    max
  end

  def peek
    @data[0]
  end

  def size
    @data.size
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent] >= @data[idx]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    n = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      largest = idx
      largest = left if left < n && @data[left] > @data[largest]
      largest = right if right < n && @data[right] > @data[largest]
      break if largest == idx
      @data[idx], @data[largest] = @data[largest], @data[idx]
      idx = largest
    end
  end
end

# @param {Integer[][]} courses
# @return {Integer}
def schedule_course(courses)
  courses.sort_by! { |c| c[1] }
  total = 0
  heap = MaxHeap.new

  courses.each do |duration, last_day|
    if total + duration <= last_day
      total += duration
      heap << duration
    elsif heap.peek && heap.peek > duration
      removed = heap.pop
      total = total - removed + duration
      heap << duration
    end
  end

  heap.size
end
```

## Scala

```scala
object Solution {
    def scheduleCourse(courses: Array[Array[Int]]): Int = {
        val sorted = courses.sortBy(_(1))
        import scala.collection.mutable.PriorityQueue
        val maxHeap = PriorityQueue.empty[Int] // max-heap by default
        var total = 0L
        for (c <- sorted) {
            val d = c(0)
            val l = c(1)
            if (total + d <= l) {
                total += d
                maxHeap.enqueue(d)
            } else if (maxHeap.nonEmpty && maxHeap.head > d) {
                total -= maxHeap.dequeue()
                total += d
                maxHeap.enqueue(d)
            }
        }
        maxHeap.size
    }
}
```

## Rust

```rust
use std::collections::BinaryHeap;

impl Solution {
    pub fn schedule_course(courses: Vec<Vec<i32>>) -> i32 {
        let mut courses = courses;
        // Sort by deadline (lastDay)
        courses.sort_by_key(|c| c[1]);
        
        let mut total_time: i64 = 0;
        let mut max_heap: BinaryHeap<i32> = BinaryHeap::new();
        
        for course in courses.iter() {
            let duration = course[0] as i64;
            let deadline = course[1] as i64;
            
            if total_time + duration <= deadline {
                // Take the course
                total_time += duration;
                max_heap.push(course[0]);
            } else if let Some(&longest) = max_heap.peek() {
                // If we have taken a longer course before, replace it
                if longest > course[0] {
                    max_heap.pop();
                    total_time -= longest as i64;
                    total_time += duration;
                    max_heap.push(course[0]);
                }
            }
        }
        
        max_heap.len() as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/heap)

(define/contract (schedule-course courses)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([sorted (sort courses
                       (lambda (a b) (< (second a) (second b))))])
    (let ([h (make-heap >)]
          [total 0]
          [count 0])
      (for ([c sorted])
        (define dur (first c))
        (define dead (second c))
        (set! total (+ total dur))
        (heap-insert! h dur)
        (set! count (+ count 1))
        (when (> total dead)
          (define longest (heap-extract! h))
          (set! total (- total longest))
          (set! count (- count 1))))
      count)))
```

## Erlang

```erlang
-module(solution).
-export([schedule_course/1]).

-spec schedule_course(Courses :: [[integer()]]) -> integer().
schedule_course(Courses) ->
    Sorted = lists:sort(fun(A, B) ->
        element(2, A) =< element(2, B)
    end, Courses),
    process(Sorted, 0, 0, gb_trees:empty()).

%% Process the list of courses.
-spec process([[integer()]], integer(), integer(), gb_tree()) -> integer().
process([], _TotalTime, Count, _Tree) ->
    Count;
process([[Dur, Deadline] | Rest], TotalTime, Count, Tree) ->
    NewTotal = TotalTime + Dur,
    NewTree  = insert_duration(Tree, Dur),
    NewCount = Count + 1,
    {AdjTotal, AdjCount, AdjTree} = adjust(NewTotal, NewCount, NewTree, Deadline),
    process(Rest, AdjTotal, AdjCount, AdjTree).

%% Insert a duration into the multiset tree.
-spec insert_duration(gb_tree(), integer()) -> gb_tree().
insert_duration(Tree, Dur) ->
    case gb_trees:lookup(Dur, Tree) of
        none ->
            gb_trees:insert(Dur, 1, Tree);
        {value, C} ->
            gb_trees:update(Dur, C + 1, Tree)
    end.

%% Remove one occurrence of a duration from the tree.
-spec delete_one(gb_tree(), integer()) -> gb_tree().
delete_one(Tree, Dur) ->
    case gb_trees:lookup(Dur, Tree) of
        {value, 1} ->
            gb_trees:delete(Dur, Tree);
        {value, C} when C > 1 ->
            gb_trees:update(Dur, C - 1, Tree)
    end.

%% Adjust total time and count while exceeding the deadline.
-spec adjust(integer(), integer(), gb_tree(), integer()) -> {integer(), integer(), gb_tree()}.
adjust(Total, Count, Tree, Deadline) when Total =< Deadline ->
    {Total, Count, Tree};
adjust(Total, Count, Tree, Deadline) ->
    {MaxDur, _} = gb_trees:largest(Tree),
    NewTree = delete_one(Tree, MaxDur),
    adjust(Total - MaxDur, Count - 1, NewTree, Deadline).

%% Type alias for readability.
-type gb_tree() :: gb_trees:tree().
```

## Elixir

```elixir
defmodule Solution do
  @spec schedule_course(courses :: [[integer]]) :: integer
  def schedule_course(courses) do
    sorted = Enum.sort_by(courses, fn [_dur, last] -> last end)

    {_, selected} =
      Enum.reduce(sorted, {0, []}, fn [dur, last], {total, sel} ->
        new_total = total + dur
        new_sel = [dur | sel]

        if new_total > last do
          max_dur = Enum.max(new_sel)
          {new_total - max_dur, List.delete(new_sel, max_dur)}
        else
          {new_total, new_sel}
        end
      end)

    length(selected)
  end
end
```

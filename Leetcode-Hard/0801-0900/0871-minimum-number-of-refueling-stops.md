# 0871. Minimum Number of Refueling Stops

## Cpp

```cpp
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        priority_queue<int> maxHeap;
        long long tank = startFuel;
        int stops = 0;
        int i = 0;
        int n = stations.size();
        while (tank < target) {
            // add all reachable stations' fuel to heap
            while (i < n && stations[i][0] <= tank) {
                maxHeap.push(stations[i][1]);
                ++i;
            }
            if (maxHeap.empty()) return -1; // cannot reach further
            tank += maxHeap.top();
            maxHeap.pop();
            ++stops;
        }
        return stops;
    }
};
```

## Java

```java
import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int fuel = startFuel;
        int prev = 0;
        int stops = 0;
        for (int[] station : stations) {
            int distance = station[0] - prev;
            while (fuel < distance) {
                if (maxHeap.isEmpty()) return -1;
                fuel += maxHeap.poll();
                stops++;
            }
            fuel -= distance;
            prev = station[0];
            maxHeap.offer(station[1]);
        }
        int remaining = target - prev;
        while (fuel < remaining) {
            if (maxHeap.isEmpty()) return -1;
            fuel += maxHeap.poll();
            stops++;
        }
        return stops;
    }
}
```

## Python

```python
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        import heapq

        # Max-heap using negative values
        max_heap = []
        fuel = startFuel
        prev = 0
        stops = 0

        # Append the target as a station with 0 fuel to simplify loop
        stations.append([target, 0])

        for position, capacity in stations:
            distance = position - prev
            # Refuel from past stations if needed
            while fuel < distance:
                if not max_heap:
                    return -1
                fuel += -heapq.heappop(max_heap)
                stops += 1
            fuel -= distance
            heapq.heappush(max_heap, -capacity)
            prev = position

        return stops
```

## Python3

```python
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations):
        import heapq
        # Max-heap using negative values
        max_heap = []
        tank = startFuel
        stops = 0
        # Append destination as a station with 0 fuel to simplify loop
        stations.append([target, 0])
        for position, fuel in stations:
            # Need enough fuel to reach this station
            while tank < position:
                if not max_heap:
                    return -1
                tank += -heapq.heappop(max_heap)
                stops += 1
            # Arrived at the station; add its fuel to heap for possible future use
            heapq.heappush(max_heap, -fuel)
        return stops
```

## C

```c
#include <stdlib.h>

static void heapPush(int *heap, int *size, int val) {
    int i = ++(*size);
    while (i > 1 && heap[i / 2] < val) {
        heap[i] = heap[i / 2];
        i /= 2;
    }
    heap[i] = val;
}

static int heapPop(int *heap, int *size) {
    int top = heap[1];
    int last = heap[(*size)--];
    int i = 1, child;
    while ((child = i * 2) <= *size) {
        if (child + 1 <= *size && heap[child] < heap[child + 1])
            child++;
        if (heap[child] <= last)
            break;
        heap[i] = heap[child];
        i = child;
    }
    if (*size >= 1)
        heap[i] = last;
    return top;
}

int minRefuelStops(int target, int startFuel, int** stations, int stationsSize, int* stationsColSize) {
    if (startFuel >= target) return 0;

    int *heap = (int *)malloc((stationsSize + 2) * sizeof(int));
    int heapSize = 0;
    int i = 0;          // index over stations
    int fuel = startFuel;
    int stops = 0;

    while (fuel < target) {
        while (i < stationsSize && stations[i][0] <= fuel) {
            heapPush(heap, &heapSize, stations[i][1]);
            i++;
        }
        if (heapSize == 0) {
            free(heap);
            return -1;
        }
        fuel += heapPop(heap, &heapSize);
        stops++;
    }

    free(heap);
    return stops;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinRefuelStops(int target, int startFuel, int[][] stations)
    {
        var maxHeap = new PriorityQueue<int, int>();
        long tank = startFuel;
        int stops = 0;
        int n = stations.Length;

        for (int i = 0; i <= n; i++)
        {
            int loc = (i == n) ? target : stations[i][0];

            while (tank < loc)
            {
                if (maxHeap.Count == 0)
                    return -1;
                tank += maxHeap.Dequeue(); // largest fuel added
                stops++;
            }

            if (i < n)
            {
                int fuel = stations[i][1];
                maxHeap.Enqueue(fuel, -fuel); // negative priority makes it a max-heap
            }
        }

        return stops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} target
 * @param {number} startFuel
 * @param {number[][]} stations
 * @return {number}
 */
var minRefuelStops = function(target, startFuel, stations) {
    class MaxHeap {
        constructor() {
            this.heap = [];
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
                    let right = i * 2 + 2;
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
        isEmpty() {
            return this.heap.length === 0;
        }
    }

    const heap = new MaxHeap();
    let fuel = startFuel;
    let prevPos = 0;
    let stops = 0;

    // Append target as a station with 0 fuel to simplify loop
    stations.push([target, 0]);

    for (const [pos, cap] of stations) {
        fuel -= (pos - prevPos);
        while (fuel < 0 && !heap.isEmpty()) {
            fuel += heap.pop();
            stops++;
        }
        if (fuel < 0) return -1;
        heap.push(cap);
        prevPos = pos;
    }

    // The last station is the target with 0 fuel, we don't need to refuel there
    return stops;
};
```

## Typescript

```typescript
function minRefuelStops(target: number, startFuel: number, stations: number[][]): number {
    class MaxHeap {
        private heap: number[] = [];
        size(): number { return this.heap.length; }
        isEmpty(): boolean { return this.heap.length === 0; }
        push(val: number): void {
            this.heap.push(val);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): number {
            if (this.heap.length === 0) throw new Error("Heap is empty");
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(index: number): void {
            while (index > 0) {
                const parent = Math.floor((index - 1) / 2);
                if (this.heap[parent] >= this.heap[index]) break;
                [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]];
                index = parent;
            }
        }
        private bubbleDown(index: number): void {
            const length = this.heap.length;
            while (true) {
                let left = 2 * index + 1;
                let right = 2 * index + 2;
                let largest = index;

                if (left < length && this.heap[left] > this.heap[largest]) largest = left;
                if (right < length && this.heap[right] > this.heap[largest]) largest = right;

                if (largest === index) break;
                [this.heap[index], this.heap[largest]] = [this.heap[largest], this.heap[index]];
                index = largest;
            }
        }
    }

    const maxHeap = new MaxHeap();
    let fuel = startFuel;
    let prevPos = 0;
    let stops = 0;

    for (const [pos, cap] of stations) {
        const need = pos - prevPos;
        while (fuel < need) {
            if (maxHeap.isEmpty()) return -1;
            fuel += maxHeap.pop();
            stops++;
        }
        fuel -= need;
        prevPos = pos;
        maxHeap.push(cap);
    }

    // Reach target
    const need = target - prevPos;
    while (fuel < need) {
        if (maxHeap.isEmpty()) return -1;
        fuel += maxHeap.pop();
        stops++;
    }

    return stops;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer $startFuel
     * @param Integer[][] $stations
     * @return Integer
     */
    function minRefuelStops($target, $startFuel, $stations) {
        $pq = new SplMaxHeap();
        $fuel = $startFuel;
        $prev = 0;
        $stops = 0;

        // Append the target as a final station with 0 fuel
        $stations[] = [$target, 0];

        foreach ($stations as $station) {
            $pos = $station[0];
            $cap = $station[1];
            $dist = $pos - $prev;

            while ($fuel < $dist && !$pq->isEmpty()) {
                $fuel += $pq->extract();
                $stops++;
            }

            if ($fuel < $dist) {
                return -1;
            }

            $fuel -= $dist;
            $prev = $pos;
            $pq->insert($cap);
        }

        return $stops;
    }
}
```

## Swift

```swift
class Solution {
    func minRefuelStops(_ target: Int, _ startFuel: Int, _ stations: [[Int]]) -> Int {
        var maxHeap = MaxHeap()
        var fuel = startFuel
        var prevPos = 0
        var stops = 0
        
        // Append the destination as a station with 0 fuel to simplify loop
        let allStations = stations + [[target, 0]]
        
        for station in allStations {
            let position = station[0]
            let capacity = station[1]
            
            fuel -= (position - prevPos)
            
            while fuel < 0 && !maxHeap.isEmpty {
                fuel += maxHeap.pop()
                stops += 1
            }
            
            if fuel < 0 {
                return -1
            }
            
            maxHeap.push(capacity)
            prevPos = position
        }
        
        return stops
    }
}

struct MaxHeap {
    private var heap: [Int] = []
    
    var isEmpty: Bool { heap.isEmpty }
    
    mutating func push(_ value: Int) {
        heap.append(value)
        siftUp(heap.count - 1)
    }
    
    mutating func pop() -> Int {
        let top = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            siftDown(0)
        }
        return top
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if heap[child] > heap[parent] {
                heap.swapAt(child, parent)
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
            var largest = parent
            
            if left < heap.count && heap[left] > heap[largest] {
                largest = left
            }
            if right < heap.count && heap[right] > heap[largest] {
                largest = right
            }
            if largest == parent { break }
            heap.swapAt(parent, largest)
            parent = largest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minRefuelStops(target: Int, startFuel: Int, stations: Array<IntArray>): Int {
        val maxHeap = java.util.PriorityQueue<Int>(compareByDescending { it })
        var tank = startFuel
        var prev = 0
        var stops = 0

        for (station in stations) {
            val pos = station[0]
            val fuel = station[1]
            val distance = pos - prev
            while (tank < distance) {
                if (maxHeap.isEmpty()) return -1
                tank += maxHeap.poll()
                stops++
            }
            tank -= distance
            maxHeap.offer(fuel)
            prev = pos
        }

        val finalDist = target - prev
        while (tank < finalDist) {
            if (maxHeap.isEmpty()) return -1
            tank += maxHeap.poll()
            stops++
        }
        return stops
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int minRefuelStops(int target, int startFuel, List<List<int>> stations) {
    // Max-heap to store fuels of passed stations
    final maxHeap = HeapPriorityQueue<int>((a, b) => b.compareTo(a));
    int stops = 0;
    int prevPos = 0;
    int fuel = startFuel;

    for (int i = 0; i <= stations.length; ++i) {
      int curPos = i < stations.length ? stations[i][0] : target;
      int distance = curPos - prevPos;

      // Refuel from the largest past stations until we can reach curPos
      while (fuel < distance && maxHeap.isNotEmpty) {
        fuel += maxHeap.removeFirst();
        stops++;
      }

      if (fuel < distance) return -1; // cannot reach this station/target

      fuel -= distance;
      prevPos = curPos;

      // Add current station's fuel to heap for future use
      if (i < stations.length) {
        maxHeap.add(stations[i][1]);
      }
    }

    return stops;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
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

func minRefuelStops(target int, startFuel int, stations [][]int) int {
	pq := &IntHeap{}
	heap.Init(pq)

	tank := startFuel
	prevPos := 0
	stops := 0

	for _, st := range stations {
		pos, fuel := st[0], st[1]
		tank -= pos - prevPos
		for tank < 0 && pq.Len() > 0 {
			tank += heap.Pop(pq).(int)
			stops++
		}
		if tank < 0 {
			return -1
		}
		heap.Push(pq, fuel)
		prevPos = pos
	}

	tank -= target - prevPos
	for tank < 0 && pq.Len() > 0 {
		tank += heap.Pop(pq).(int)
		stops++
	}
	if tank < 0 {
		return -1
	}
	return stops
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
        r = l + 1
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

# @param {Integer} target
# @param {Integer} start_fuel
# @param {Integer[][]} stations
# @return {Integer}
def min_refuel_stops(target, start_fuel, stations)
  heap = MaxHeap.new
  tank = start_fuel
  prev = 0
  stops = 0

  stations.each do |pos, fuel|
    tank -= (pos - prev)
    while tank < 0 && !heap.empty?
      tank += heap.pop
      stops += 1
    end
    return -1 if tank < 0
    heap.push(fuel)
    prev = pos
  end

  tank -= (target - prev)
  while tank < 0 && !heap.empty?
    tank += heap.pop
    stops += 1
  end

  tank >= 0 ? stops : -1
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.PriorityQueue

  def minRefuelStops(target: Int, startFuel: Int, stations: Array[Array[Int]]): Int = {
    val maxHeap = PriorityQueue.empty[Int](Ordering.Int)
    var tank = startFuel
    var prevPos = 0
    var stops = 0

    for (i <- 0 to stations.length) {
      val curPos = if (i < stations.length) stations(i)(0) else target
      tank -= (curPos - prevPos)

      while (tank < 0 && maxHeap.nonEmpty) {
        tank += maxHeap.dequeue()
        stops += 1
      }

      if (tank < 0) return -1

      if (i < stations.length) {
        maxHeap.enqueue(stations(i)(1))
      }
      prevPos = curPos
    }

    stops
  }
}
```

## Rust

```rust
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_refuel_stops(target: i32, start_fuel: i32, stations: Vec<Vec<i32>>) -> i32 {
        let mut heap = BinaryHeap::<i64>::new();
        let mut fuel: i64 = start_fuel as i64;
        let mut prev: i64 = 0;
        let mut stops: i32 = 0;

        for station in stations.iter() {
            let pos = station[0] as i64;
            let cap = station[1] as i64;
            let dist = pos - prev;

            while fuel < dist {
                if let Some(max_cap) = heap.pop() {
                    fuel += max_cap;
                    stops += 1;
                } else {
                    return -1;
                }
            }

            fuel -= dist;
            heap.push(cap);
            prev = pos;
        }

        let remaining = target as i64 - prev;
        while fuel < remaining {
            if let Some(max_cap) = heap.pop() {
                fuel += max_cap;
                stops += 1;
            } else {
                return -1;
            }
        }

        stops
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (min-refuel-stops target startFuel stations)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([h (make-heap >)]
         [stations-with-target (append stations (list (list target 0)))])
    (define (process sts fuel prev-pos stops)
      (if (null? sts)
          stops
          (let* ((pos (car (car sts)))
                 (cap (cadr (car sts)))
                 (dist (- pos prev-pos)))
            (let loop ((fuel fuel) (stops stops))
              (if (>= fuel dist)
                  (let ((new-fuel (- fuel dist)))
                    (heap-insert! h cap)
                    (process (cdr sts) new-fuel pos stops))
                  (if (heap-empty? h)
                      -1
                      (loop (+ fuel (heap-extract-max! h)) (+ stops 1))))))))
    (process stations-with-target startFuel 0 0)))
```

## Erlang

```erlang
-module(solution).
-export([min_refuel_stops/3]).

-spec min_refuel_stops(Target :: integer(), StartFuel :: integer(), Stations :: [[integer()]]) -> integer().
min_refuel_stops(Target, StartFuel, Stations) ->
    N = length(Stations),
    InitList = lists:duplicate(N + 1, -1),
    Dp0 = list_to_tuple(InitList),
    Dp1 = setelement(1, Dp0, StartFuel), % dp[0] = start fuel
    DpFinal = process_stations(Stations, Dp1, N),
    find_min_stops(DpFinal, Target, 0, N).

%% Process each station updating the DP tuple
process_stations([], Dp, _N) ->
    Dp;
process_stations([Station | Rest], Dp, N) ->
    [Pos, Fuel] = Station,
    UpdatedDp = update_dp(Dp, Pos, Fuel, N),
    process_stations(Rest, UpdatedDp, N).

%% Update DP for a single station (iterate stops backwards)
update_dp(Dp, Pos, Fuel, N) ->
    update_dp(N - 1, Dp, Pos, Fuel).

update_dp(-1, Dp, _Pos, _Fuel) ->
    Dp;
update_dp(I, Dp, Pos, Fuel) ->
    Dist = element(I + 1, Dp),
    NewDp =
        if
            Dist >= Pos ->
                NewDist = Dist + Fuel,
                Old = element(I + 2, Dp),
                MaxDist = max(Old, NewDist),
                setelement(I + 2, Dp, MaxDist);
            true ->
                Dp
        end,
    update_dp(I - 1, NewDp, Pos, Fuel).

%% Find the smallest number of stops achieving at least Target distance
find_min_stops(Dp, Target, I, N) when I =< N ->
    if
        element(I + 1, Dp) >= Target -> I;
        true -> find_min_stops(Dp, Target, I + 1, N)
    end;
find_min_stops(_Dp, _Target, _I, _N) ->
    -1.

%% Helper max function (since erlang: max/2 is available but we define for clarity)
max(A, B) when A >= B -> A;
max(_, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_refuel_stops(target :: integer, start_fuel :: integer, stations :: [[integer]]) :: integer
  def min_refuel_stops(target, start_fuel, stations) do
    n = length(stations)
    dp_initial = List.duplicate(-1, n + 1) |> List.replace_at(0, start_fuel)

    {dp_final, _} =
      Enum.reduce(stations, {dp_initial, 0}, fn [pos, fuel], {dp, idx} ->
        dp_updated =
          Enum.reduce(idx..0//-1, dp, fn i, acc ->
            if Enum.at(acc, i) >= pos do
              cur = Enum.at(acc, i) + fuel
              prev = Enum.at(acc, i + 1)
              max_val = if cur > prev, do: cur, else: prev
              List.replace_at(acc, i + 1, max_val)
            else
              acc
            end
          end)

        {dp_updated, idx + 1}
      end)

    case Enum.find_index(dp_final, fn d -> d >= target end) do
      nil -> -1
      idx -> idx
    end
  end
end
```

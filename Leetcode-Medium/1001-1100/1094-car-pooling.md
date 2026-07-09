# 1094. Car Pooling

## Cpp

```cpp
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        const int MAX_POS = 1000;
        vector<int> diff(MAX_POS + 2, 0);
        for (const auto& t : trips) {
            int num = t[0], start = t[1], end = t[2];
            diff[start] += num;
            diff[end] -= num;
        }
        int cur = 0;
        for (int i = 0; i <= MAX_POS; ++i) {
            cur += diff[i];
            if (cur > capacity) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] diff = new int[1001];
        for (int[] trip : trips) {
            int num = trip[0];
            int from = trip[1];
            int to = trip[2];
            diff[from] += num;
            diff[to] -= num;
        }
        int current = 0;
        for (int i = 0; i < diff.length; i++) {
            current += diff[i];
            if (current > capacity) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        max_loc = 0
        for p, f, t in trips:
            if t > max_loc:
                max_loc = t
        diff = [0] * (max_loc + 2)  # extra slot to avoid index error at t
        
        for p, f, t in trips:
            diff[f] += p
            diff[t] -= p
        
        cur = 0
        for delta in diff:
            cur += delta
            if cur > capacity:
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Since locations are in range [0, 1000], we can use a difference array.
        max_location = 0
        for _, start, end in trips:
            if end > max_location:
                max_location = end
        diff = [0] * (max_location + 2)  # extra slot for the last drop-off
        
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        
        current = 0
        for i in range(max_location + 1):
            current += diff[i]
            if current > capacity:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool carPooling(int** trips, int tripsSize, int* tripsColSize, int capacity) {
    // Maximum possible location is 1000 according to constraints
    const int MAX_LOC = 1000;
    int *diff = (int *)calloc(MAX_LOC + 2, sizeof(int));
    if (!diff) return false; // allocation failure, treat as impossible

    int maxLoc = 0;
    for (int i = 0; i < tripsSize; ++i) {
        int num = trips[i][0];
        int from = trips[i][1];
        int to   = trips[i][2];
        diff[from] += num;
        diff[to]   -= num;
        if (to > maxLoc) maxLoc = to;
    }

    int cur = 0;
    for (int loc = 0; loc <= maxLoc; ++loc) {
        cur += diff[loc];
        if (cur > capacity) {
            free(diff);
            return false;
        }
    }

    free(diff);
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CarPooling(int[][] trips, int capacity) {
        // Maximum possible location value based on constraints
        const int maxLocation = 1000;
        int[] diff = new int[maxLocation + 2]; // extra slot for the end point
        
        foreach (var trip in trips) {
            int passengers = trip[0];
            int from = trip[1];
            int to = trip[2];
            diff[from] += passengers;
            diff[to] -= passengers;
        }
        
        int current = 0;
        for (int i = 0; i <= maxLocation + 1; i++) {
            current += diff[i];
            if (current > capacity) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function(trips, capacity) {
    const MAX_POS = 1000;
    const diff = new Array(MAX_POS + 1).fill(0);
    
    for (const [num, from, to] of trips) {
        diff[from] += num;
        diff[to] -= num;
    }
    
    let cur = 0;
    for (let i = 0; i <= MAX_POS; i++) {
        cur += diff[i];
        if (cur > capacity) return false;
    }
    return true;
};
```

## Typescript

```typescript
function carPooling(trips: number[][], capacity: number): boolean {
    const maxLoc = 1000;
    const diff = new Array(maxLoc + 2).fill(0);
    for (const [num, from, to] of trips) {
        diff[from] += num;
        diff[to] -= num;
    }
    let cur = 0;
    for (let i = 0; i <= maxLoc; i++) {
        cur += diff[i];
        if (cur > capacity) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $trips
     * @param Integer $capacity
     * @return Boolean
     */
    function carPooling($trips, $capacity) {
        // Maximum possible location is 1000 according to constraints
        $maxLocation = 1000;
        $diff = array_fill(0, $maxLocation + 1, 0);
        
        foreach ($trips as $trip) {
            [$numPassengers, $from, $to] = $trip;
            $diff[$from] += $numPassengers;
            $diff[$to] -= $numPassengers;
        }
        
        $current = 0;
        for ($i = 0; $i <= $maxLocation; $i++) {
            $current += $diff[$i];
            if ($current > $capacity) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func carPooling(_ trips: [[Int]], _ capacity: Int) -> Bool {
        var maxLoc = 0
        for t in trips {
            if t[2] > maxLoc { maxLoc = t[2] }
        }
        var diff = [Int](repeating: 0, count: maxLoc + 1)
        for t in trips {
            let num = t[0]
            let start = t[1]
            let end = t[2]
            diff[start] += num
            if end < diff.count { diff[end] -= num }
        }
        var current = 0
        for delta in diff {
            current += delta
            if current > capacity { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun carPooling(trips: Array<IntArray>, capacity: Int): Boolean {
        var maxLocation = 0
        for (trip in trips) {
            if (trip[2] > maxLocation) maxLocation = trip[2]
        }
        val diff = IntArray(maxLocation + 1)
        for (trip in trips) {
            val num = trip[0]
            val from = trip[1]
            val to = trip[2]
            diff[from] += num
            if (to < diff.size) diff[to] -= num
        }
        var current = 0
        for (i in diff.indices) {
            current += diff[i]
            if (current > capacity) return false
        }
        return true
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  bool carPooling(List<List<int>> trips, int capacity) {
    // Determine the maximum location to size the difference array.
    int maxLocation = 0;
    for (var trip in trips) {
      maxLocation = max(maxLocation, trip[2]);
    }

    // Difference array to track passenger changes at each point.
    List<int> diff = List.filled(maxLocation + 1, 0);

    for (var trip in trips) {
      int numPassengers = trip[0];
      int from = trip[1];
      int to = trip[2];
      diff[from] += numPassengers;
      // Ensure the array can accommodate 'to' index.
      if (to <= maxLocation) {
        diff[to] -= numPassengers;
      }
    }

    int current = 0;
    for (int i = 0; i <= maxLocation; ++i) {
      current += diff[i];
      if (current > capacity) return false;
    }
    return true;
  }
}
```

## Golang

```go
func carPooling(trips [][]int, capacity int) bool {
	const maxLocation = 1000
	diff := make([]int, maxLocation+1)
	for _, t := range trips {
		num, start, end := t[0], t[1], t[2]
		diff[start] += num
		if end <= maxLocation {
			diff[end] -= num
		}
	}
	cur := 0
	for i := 0; i <= maxLocation; i++ {
		cur += diff[i]
		if cur > capacity {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def car_pooling(trips, capacity)
  max_location = 1000
  diff = Array.new(max_location + 1, 0)

  trips.each do |num, from, to|
    diff[from] += num
    diff[to] -= num
  end

  current = 0
  (0..max_location).each do |i|
    current += diff[i]
    return false if current > capacity
  end
  true
end
```

## Scala

```scala
object Solution {
    def carPooling(trips: Array[Array[Int]], capacity: Int): Boolean = {
        var maxLoc = 0
        for (t <- trips) {
            if (t(2) > maxLoc) maxLoc = t(2)
        }
        val diff = new Array[Int](maxLoc + 2) // extra slot to avoid OOB
        for (t <- trips) {
            val num = t(0)
            val from = t(1)
            val to = t(2)
            diff(from) += num
            diff(to) -= num
        }
        var cur = 0
        for (i <- 0 until diff.length) {
            cur += diff(i)
            if (cur > capacity) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn car_pooling(trips: Vec<Vec<i32>>, capacity: i32) -> bool {
        let mut diff = vec![0i32; 1002];
        for trip in trips.iter() {
            let num = trip[0];
            let from = trip[1] as usize;
            let to = trip[2] as usize;
            diff[from] += num;
            diff[to] -= num;
        }
        let mut cur = 0i32;
        for delta in diff.iter() {
            cur += *delta;
            if cur > capacity {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define/contract (car-pooling trips capacity)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  (let* ((events
          (apply append
                 (map (lambda (trip)
                        (let ((num   (first trip))
                              (start (second trip))
                              (end   (third trip)))
                          (list (list start num)      ; pickup
                                (list end (- num)))))  ; dropoff
                      trips))))
    (define sorted-events
      (sort events
            (lambda (a b)
              (let ((loc-a   (first a))
                    (loc-b   (first b))
                    (delta-a (second a))
                    (delta-b (second b)))
                (if (= loc-a loc-b)
                    (< delta-a delta-b)          ; dropoffs before pickups at same spot
                    (< loc-a loc-b))))))
    (let loop ((evs sorted-events) (curr 0))
      (cond [(null? evs) #t]
            [else
             (let* ((delta (second (car evs)))
                    (new   (+ curr delta)))
               (if (> new capacity)
                   #f
                   (loop (cdr evs) new)))]))))
```

## Erlang

```erlang
-module(solution).
-export([car_pooling/2]).
-spec car_pooling(Trips :: [[integer()]], Capacity :: integer()) -> boolean().
car_pooling(Trips, Capacity) ->
    Events = build_events(Trips, []),
    Sorted = sort_events(Events),
    check_capacity(Sorted, Capacity, 0).

build_events([], Acc) ->
    Acc;
build_events([[P,F,T]|Rest], Acc) ->
    Pickup   = {F, 1, P},
    Dropoff  = {T, 0, -P},
    build_events(Rest, [Pickup, Dropoff | Acc]).

sort_events(Events) ->
    ByType = lists:keysort(2, Events),
    lists:keysort(1, ByType).

check_capacity([], _Cap, _Occ) ->
    true;
check_capacity([{_Loc,_Type,Delta}|Rest], Cap, Occ) ->
    NewOcc = Occ + Delta,
    if
        NewOcc > Cap -> false;
        true -> check_capacity(Rest, Cap, NewOcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec car_pooling(trips :: [[integer]], capacity :: integer) :: boolean
  def car_pooling(trips, capacity) do
    events =
      Enum.flat_map(trips, fn [p, from, to] ->
        [{from, p}, {to, -p}]
      end)

    sorted =
      Enum.sort_by(events, fn {loc, delta} ->
        {loc, if(delta < 0, do: 0, else: 1)}
      end)

    case Enum.reduce_while(sorted, 0, fn {_loc, delta}, cur_passengers ->
           new_total = cur_passengers + delta

           if new_total > capacity do
             {:halt, false}
           else
             {:cont, new_total}
           end
         end) do
      false -> false
      _ -> true
    end
  end
end
```

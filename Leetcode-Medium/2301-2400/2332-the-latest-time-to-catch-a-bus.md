# 2332. The Latest Time to Catch a Bus

## Cpp

```cpp
class Solution {
public:
    int latestTimeCatchTheBus(vector<int>& buses, vector<int>& passengers, int capacity) {
        sort(buses.begin(), buses.end());
        sort(passengers.begin(), passengers.end());
        unordered_set<int> passengerSet(passengers.begin(), passengers.end());
        
        int idx = 0;
        int m = passengers.size();
        vector<int> lastBoarded;
        int n = buses.size();
        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            vector<int> curBoarded;
            while (idx < m && passengers[idx] <= buses[i] && cnt < capacity) {
                curBoarded.push_back(passengers[idx]);
                ++idx;
                ++cnt;
            }
            if (i == n - 1) {
                lastBoarded = move(curBoarded);
            }
        }
        
        int limit;
        if ((int)lastBoarded.size() < capacity) {
            limit = buses.back();
        } else {
            limit = lastBoarded.back() - 1;
        }
        while (passengerSet.count(limit)) {
            --limit;
        }
        return limit;
    }
};
```

## Java

```java
class Solution {
    public int latestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        java.util.Arrays.sort(buses);
        java.util.Arrays.sort(passengers);
        java.util.HashSet<Integer> passengerSet = new java.util.HashSet<>();
        for (int p : passengers) passengerSet.add(p);

        int i = 0;
        int lastBoarded = -1;
        int answer = 0;

        for (int idx = 0; idx < buses.length; idx++) {
            int busTime = buses[idx];
            int cnt = 0;
            while (i < passengers.length && passengers[i] <= busTime && cnt < capacity) {
                lastBoarded = passengers[i];
                i++;
                cnt++;
            }
            if (idx == buses.length - 1) { // last bus
                if (cnt < capacity) {
                    answer = busTime;
                } else {
                    answer = lastBoarded - 1;
                }
                break;
            }
        }

        while (passengerSet.contains(answer)) {
            answer--;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)
        p = 0
        n = len(buses)
        m = len(passengers)

        for idx, b in enumerate(buses):
            cnt = 0
            last_boarded = -1
            while p < m and passengers[p] <= b and cnt < capacity:
                last_boarded = passengers[p]
                p += 1
                cnt += 1
            # if this is the last bus, determine answer
            if idx == n - 1:
                if cnt < capacity:          # bus not full
                    ans = b
                else:                       # bus full
                    ans = last_boarded - 1
                while ans in passenger_set:
                    ans -= 1
                return ans
        # Should never reach here because we always return on the last bus
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)
        
        i = 0  # index in passengers
        last_boarded_time = -1
        last_bus_count = 0
        
        for idx, bus_time in enumerate(buses):
            cnt = 0
            while i < len(passengers) and passengers[i] <= bus_time and cnt < capacity:
                last_boarded_time = passengers[i]
                i += 1
                cnt += 1
            if idx == len(buses) - 1:  # last bus
                last_bus_count = cnt
        
        if last_bus_count < capacity:
            ans = buses[-1]
        else:
            ans = last_boarded_time - 1
        
        while ans in passenger_set:
            ans -= 1
        
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

static int exists(int *arr, int size, int val) {
    int l = 0, r = size - 1;
    while (l <= r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] == val) return 1;
        if (arr[m] < val) l = m + 1;
        else r = m - 1;
    }
    return 0;
}

int latestTimeCatchTheBus(int* buses, int busesSize, int* passengers, int passengersSize, int capacity) {
    int *b = (int *)malloc(busesSize * sizeof(int));
    memcpy(b, buses, busesSize * sizeof(int));
    qsort(b, busesSize, sizeof(int), cmp_int);

    int *p = (int *)malloc(passengersSize * sizeof(int));
    memcpy(p, passengers, passengersSize * sizeof(int));
    qsort(p, passengersSize, sizeof(int), cmp_int);

    int idx = 0;
    int lastBusCnt = 0;
    int lastBoarded = -1;

    for (int i = 0; i < busesSize; ++i) {
        int cnt = 0;
        while (idx < passengersSize && p[idx] <= b[i] && cnt < capacity) {
            lastBoarded = p[idx];
            ++idx;
            ++cnt;
        }
        if (i == busesSize - 1) {
            lastBusCnt = cnt;
        }
    }

    int ans;
    if (lastBusCnt < capacity) {
        ans = b[busesSize - 1];
    } else {
        ans = lastBoarded - 1;
    }

    while (exists(p, passengersSize, ans)) {
        --ans;
    }

    free(b);
    free(p);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LatestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        Array.Sort(buses);
        Array.Sort(passengers);
        var passengerSet = new HashSet<int>(passengers);
        int p = 0;
        int n = buses.Length;
        int m = passengers.Length;

        // Process all buses except the last one
        for (int i = 0; i < n - 1; i++) {
            int busTime = buses[i];
            int cnt = 0;
            while (p < m && passengers[p] <= busTime && cnt < capacity) {
                cnt++;
                p++;
            }
        }

        // Process the last bus
        int lastBus = buses[n - 1];
        int cntLast = 0;
        int lastBoarded = -1;
        while (p < m && passengers[p] <= lastBus && cntLast < capacity) {
            lastBoarded = passengers[p];
            cntLast++;
            p++;
        }

        if (cntLast < capacity) {
            // There is at least one empty seat
            int ans = lastBus;
            while (passengerSet.Contains(ans)) {
                ans--;
            }
            return ans;
        } else {
            // Bus is full, need to arrive before the last boarded passenger
            int ans = lastBoarded - 1;
            while (ans >= 0 && passengerSet.Contains(ans)) {
                ans--;
            }
            return ans;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} buses
 * @param {number[]} passengers
 * @param {number} capacity
 * @return {number}
 */
var latestTimeCatchTheBus = function(buses, passengers, capacity) {
    buses.sort((a, b) => a - b);
    passengers.sort((a, b) => a - b);
    const passengerSet = new Set(passengers);
    
    let i = 0;
    let lastBoardedLast = -1;
    let countLast = 0;
    
    for (let bi = 0; bi < buses.length; bi++) {
        const busTime = buses[bi];
        let cnt = 0;
        while (i < passengers.length && passengers[i] <= busTime && cnt < capacity) {
            lastBoardedLast = passengers[i];
            i++;
            cnt++;
        }
        if (bi === buses.length - 1) {
            countLast = cnt;
        }
    }
    
    const lastBus = buses[buses.length - 1];
    let ans;
    if (countLast < capacity) {
        ans = lastBus;
    } else {
        ans = lastBoardedLast - 1;
    }
    while (passengerSet.has(ans)) {
        ans--;
    }
    return ans;
};
```

## Typescript

```typescript
function latestTimeCatchTheBus(buses: number[], passengers: number[], capacity: number): number {
    buses.sort((a, b) => a - b);
    passengers.sort((a, b) => a - b);
    const passengerSet = new Set<number>(passengers);
    let p = 0;
    const m = passengers.length;

    for (let i = 0; i < buses.length; i++) {
        const busTime = buses[i];
        let cnt = 0;
        let lastBoarded = -1;

        while (p < m && passengers[p] <= busTime && cnt < capacity) {
            lastBoarded = passengers[p];
            p++;
            cnt++;
        }

        if (i === buses.length - 1) {
            let ans: number;
            if (cnt < capacity) {
                ans = busTime;
            } else {
                ans = lastBoarded - 1;
            }
            while (passengerSet.has(ans)) {
                ans--;
            }
            return ans;
        }
    }

    return -1; // fallback, should never reach here
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $buses
     * @param Integer[] $passengers
     * @param Integer $capacity
     * @return Integer
     */
    function latestTimeCatchTheBus($buses, $passengers, $capacity) {
        sort($buses);
        sort($passengers);
        $passSet = array_flip($passengers);

        $n = count($buses);
        $m = count($passengers);
        $pIdx = 0;          // index in passengers
        $lastBoarded = -1;   // last passenger that boarded the current bus

        for ($i = 0; $i < $n; $i++) {
            $busTime = $buses[$i];
            $cnt = 0;
            while ($pIdx < $m && $passengers[$pIdx] <= $busTime && $cnt < $capacity) {
                $lastBoarded = $passengers[$pIdx];
                $pIdx++;
                $cnt++;
            }

            // If this is the last bus, determine the answer
            if ($i == $n - 1) {
                if ($cnt < $capacity) {
                    $candidate = $busTime;          // empty seat, can arrive at departure time
                } else {
                    $candidate = $lastBoarded - 1;   // bus full, must be before the last boarded passenger
                }
                while (isset($passSet[$candidate])) {
                    $candidate--;
                }
                return $candidate;
            }
        }

        return 0; // fallback, should never reach here with valid input
    }
}
```

## Swift

```swift
class Solution {
    func latestTimeCatchTheBus(_ buses: [Int], _ passengers: [Int], _ capacity: Int) -> Int {
        let sortedBuses = buses.sorted()
        let sortedPassengers = passengers.sorted()
        var passengerIndex = 0
        let lastBusTime = sortedBuses.last!
        var countOnLastBus = 0
        var lastBoardedOnLastBus = -1
        
        for bus in sortedBuses {
            var boarded = 0
            while boarded < capacity && passengerIndex < sortedPassengers.count && sortedPassengers[passengerIndex] <= bus {
                if bus == lastBusTime {
                    lastBoardedOnLastBus = sortedPassengers[passengerIndex]
                }
                passengerIndex += 1
                boarded += 1
            }
            if bus == lastBusTime {
                countOnLastBus = boarded
            }
        }
        
        let passengerSet = Set(passengers)
        if countOnLastBus < capacity {
            var time = lastBusTime
            while passengerSet.contains(time) {
                time -= 1
            }
            return time
        } else {
            var time = lastBoardedOnLastBus - 1
            while passengerSet.contains(time) {
                time -= 1
            }
            return time
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun latestTimeCatchTheBus(buses: IntArray, passengers: IntArray, capacity: Int): Int {
        val sortedBuses = buses.sorted()
        val sortedPassengers = passengers.sorted()
        val passengerSet = passengers.toHashSet()
        var pIdx = 0
        var answer = 0

        for (i in sortedBuses.indices) {
            val busTime = sortedBuses[i]
            var boarded = 0
            var lastBoarded = -1
            while (boarded < capacity && pIdx < sortedPassengers.size && sortedPassengers[pIdx] <= busTime) {
                lastBoarded = sortedPassengers[pIdx]
                pIdx++
                boarded++
            }
            if (i == sortedBuses.lastIndex) {
                answer = if (boarded < capacity) {
                    busTime
                } else {
                    lastBoarded - 1
                }
            }
        }

        while (passengerSet.contains(answer)) {
            answer--
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int latestTimeCatchTheBus(List<int> buses, List<int> passengers, int capacity) {
    buses.sort();
    passengers.sort();
    Set<int> passengerSet = passengers.toSet();

    int i = 0;
    int lastBoarded = -1;
    int cntLastBus = 0;
    int nBuses = buses.length;

    for (int idx = 0; idx < nBuses; idx++) {
      int busTime = buses[idx];
      int cnt = 0;
      while (i < passengers.length && passengers[i] <= busTime && cnt < capacity) {
        lastBoarded = passengers[i];
        i++;
        cnt++;
      }
      if (idx == nBuses - 1) {
        cntLastBus = cnt;
      }
    }

    int answer;
    int lastBusTime = buses.last;
    if (cntLastBus < capacity) {
      answer = lastBusTime;
    } else {
      answer = lastBoarded - 1;
    }

    while (passengerSet.contains(answer)) {
      answer--;
    }
    return answer;
  }
}
```

## Golang

```go
package main

import "sort"

func latestTimeCatchTheBus(buses []int, passengers []int, capacity int) int {
	sort.Ints(buses)
	sort.Ints(passengers)

	passSet := make(map[int]struct{}, len(passengers))
	for _, p := range passengers {
		passSet[p] = struct{}{}
	}

	idx := 0
	var lastBus int
	var lastCount int
	lastBoarded := -1

	n := len(buses)
	for i, b := range buses {
		cnt := 0
		boardLast := -1
		for idx < len(passengers) && passengers[idx] <= b && cnt < capacity {
			boardLast = passengers[idx]
			idx++
			cnt++
		}
		if i == n-1 {
			lastBus = b
			lastCount = cnt
			lastBoarded = boardLast
		}
	}

	var ans int
	if lastCount < capacity {
		ans = lastBus
	} else {
		ans = lastBoarded - 1
	}
	for {
		if _, ok := passSet[ans]; !ok {
			break
		}
		ans--
	}
	return ans
}
```

## Ruby

```ruby
def latest_time_catch_the_bus(buses, passengers, capacity)
  buses.sort!
  passengers.sort!
  occupied = {}
  passengers.each { |t| occupied[t] = true }

  p_idx = 0
  m = passengers.length
  last_bus_time = buses[-1]
  last_filled = 0
  last_boarded_time = nil

  buses.each_with_index do |b, i|
    cnt = 0
    while cnt < capacity && p_idx < m && passengers[p_idx] <= b
      cnt += 1
      last_boarded_time = passengers[p_idx] if i == buses.length - 1
      p_idx += 1
    end
    if i == buses.length - 1
      last_filled = cnt
    end
  end

  candidate = if last_filled < capacity
                last_bus_time
              else
                last_boarded_time - 1
              end

  while occupied.key?(candidate)
    candidate -= 1
  end
  candidate
end
```

## Scala

```scala
object Solution {
    def latestTimeCatchTheBus(buses: Array[Int], passengers: Array[Int], capacity: Int): Int = {
        val sortedBuses = buses.sorted
        val sortedPassengers = passengers.sorted
        val passengerSet = passengers.toSet

        var i = 0
        val m = sortedPassengers.length
        var answer = 0

        for (idx <- sortedBuses.indices) {
            val busTime = sortedBuses(idx)
            var cnt = 0
            var lastPassenger = -1
            while (cnt < capacity && i < m && sortedPassengers(i) <= busTime) {
                lastPassenger = sortedPassengers(i)
                i += 1
                cnt += 1
            }
            if (idx == sortedBuses.length - 1) { // last bus
                if (cnt < capacity) {
                    answer = busTime
                } else {
                    answer = lastPassenger - 1
                }
            }
        }

        var ans = answer
        while (passengerSet.contains(ans)) {
            ans -= 1
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn latest_time_catch_the_bus(buses: Vec<i32>, passengers: Vec<i32>, capacity: i32) -> i32 {
        let mut buses = buses;
        buses.sort_unstable();
        let mut passengers = passengers;
        passengers.sort_unstable();

        let passenger_set: HashSet<i32> = passengers.iter().cloned().collect();

        let cap = capacity as usize;
        let mut p_idx = 0usize;
        let m = passengers.len();

        let mut answer = 0i32;

        for (bus_i, &b) in buses.iter().enumerate() {
            let mut cnt = 0usize;
            let mut last_boarded = -1i32;
            while p_idx < m && passengers[p_idx] <= b && cnt < cap {
                last_boarded = passengers[p_idx];
                p_idx += 1;
                cnt += 1;
            }
            if bus_i == buses.len() - 1 {
                let mut candidate = if cnt < cap { b } else { last_boarded - 1 };
                while passenger_set.contains(&candidate) {
                    candidate -= 1;
                }
                answer = candidate;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (latest-time-catch-the-bus buses passengers capacity)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((buses-sorted (sort (copy-list buses) <))
         (passengers-sorted (sort (copy-list passengers) <))
         (p-set (make-hash))
         (p-vec (list->vector passengers-sorted)))
    (for ([p passengers])
      (hash-set! p-set p #t))
    (define n (vector-length p-vec))
    (define i 0)
    (define ans -1)
    (define bus-count (length buses-sorted))
    (for ([b (in-list buses-sorted)] [idx (in-naturals)])
      (define cnt 0)
      (define last-boarded #f)
      (while (and (< i n) (<= (vector-ref p-vec i) b) (< cnt capacity))
        (set! last-boarded (vector-ref p-vec i))
        (set! i (+ i 1))
        (set! cnt (+ cnt 1)))
      (when (= idx (- bus-count 1))
        (if (< cnt capacity)
            (set! ans b)
            (set! ans (- last-boarded 1)))))
    (let loop ((t ans))
      (if (hash-has-key? p-set t)
          (loop (- t 1))
          t))))
```

## Erlang

```erlang
-module(solution).
-export([latest_time_catch_the_bus/3]).

-spec latest_time_catch_the_bus([integer()], [integer()], integer()) -> integer().
latest_time_catch_the_bus(Buses, Passengers, Capacity) ->
    SortedB = lists:sort(Buses),
    SortedP = lists:sort(Passengers),
    PassengerMap = maps:from_list([{P, true} || P <- Passengers]),
    {BoardedCount, LastBoardedTime, LastBusTime} = process_last_bus(SortedB, SortedP, Capacity),
    Candidate0 =
        case BoardedCount < Capacity of
            true -> LastBusTime;
            false -> LastBoardedTime - 1
        end,
    find_free(Candidate0, PassengerMap).

%% Process all buses except the last one; for the last bus return boarding info.
process_last_bus([LastBus], Passengers, Capacity) ->
    {_, Count, LastBoarded} = board(LastBus, Passengers, Capacity),
    {Count, LastBoarded, LastBus};
process_last_bus([Bus | Rest], Passengers, Capacity) ->
    {Remaining, _, _} = board(Bus, Passengers, Capacity),
    process_last_bus(Rest, Remaining, Capacity).

%% Board passengers onto a bus up to Seats capacity.
board(BusTime, Passengers, Seats) ->
    board_loop(BusTime, Passengers, Seats, 0, undefined).

board_loop(_BusTime, Passengers, 0, Count, Last) ->
    {Passengers, Count, Last};
board_loop(_BusTime, [], _Seats, Count, Last) ->
    {[], Count, Last};
board_loop(BusTime, [P | Rest] = All, Seats, Count, _Last) when P =< BusTime ->
    board_loop(BusTime, Rest, Seats - 1, Count + 1, P);
board_loop(_BusTime, Passengers, _Seats, Count, Last) ->
    {Passengers, Count, Last}.

%% Find the largest time not occupied by any passenger.
find_free(Time, Map) ->
    case maps:is_key(Time, Map) of
        true -> find_free(Time - 1, Map);
        false -> Time
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec latest_time_catch_the_bus(buses :: [integer], passengers :: [integer], capacity :: integer) :: integer
  def latest_time_catch_the_bus(buses, passengers, capacity) do
    sorted_buses = Enum.sort(buses)
    sorted_passengers = Enum.sort(passengers)
    passenger_set = MapSet.new(passengers)

    process(sorted_buses, sorted_passengers, 0, capacity, passenger_set)
  end

  defp process([bus], passengers, idx, capacity, set) do
    {new_idx, count, last_boarded} = board(passengers, idx, bus, capacity)

    candidate =
      if count < capacity do
        bus
      else
        last_boarded - 1
      end

    adjust_candidate(candidate, set)
  end

  defp process([bus | rest], passengers, idx, capacity, set) do
    {new_idx, _count, _last} = board(passengers, idx, bus, capacity)
    process(rest, passengers, new_idx, capacity, set)
  end

  defp board(passengers, idx, bus_time, capacity) do
    len = length(passengers)
    board_loop(passengers, idx, len, bus_time, capacity, 0, nil)
  end

  defp board_loop(_passengers, idx, len, _bus_time, _capacity, count, last_boarded)
       when idx >= len or count == _capacity do
    {idx, count, last_boarded}
  end

  defp board_loop(passengers, idx, len, bus_time, capacity, count, _last) do
    p = Enum.at(passengers, idx)

    if p <= bus_time do
      board_loop(passengers, idx + 1, len, bus_time, capacity, count + 1, p)
    else
      {idx, count, nil}
    end
  end

  defp adjust_candidate(candidate, set) do
    if MapSet.member?(set, candidate) do
      adjust_candidate(candidate - 1, set)
    else
      candidate
    end
  end
end
```

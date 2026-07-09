# 0732. My Calendar III

## Cpp

```cpp
class MyCalendarThree {
public:
    MyCalendarThree() {}
    
    int book(int startTime, int endTime) {
        timeline[startTime] += 1;
        timeline[endTime] -= 1;
        int cur = 0, mx = 0;
        for (const auto& kv : timeline) {
            cur += kv.second;
            if (cur > mx) mx = cur;
        }
        return mx;
    }
private:
    std::map<int, int> timeline;
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime,endTime);
 */
```

## Java

```java
class MyCalendarThree {

    private final java.util.TreeMap<Integer, Integer> timeline;

    public MyCalendarThree() {
        timeline = new java.util.TreeMap<>();
    }

    public int book(int startTime, int endTime) {
        timeline.put(startTime, timeline.getOrDefault(startTime, 0) + 1);
        timeline.put(endTime, timeline.getOrDefault(endTime, 0) - 1);

        int ongoing = 0;
        int maxOverlap = 0;
        for (int delta : timeline.values()) {
            ongoing += delta;
            if (ongoing > maxOverlap) {
                maxOverlap = ongoing;
            }
        }
        return maxOverlap;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(startTime,endTime);
 */
```

## Python

```python
class MyCalendarThree(object):
    def __init__(self):
        self.delta = {}

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        self.delta[startTime] = self.delta.get(startTime, 0) + 1
        self.delta[endTime] = self.delta.get(endTime, 0) - 1

        ongoing = 0
        max_overlap = 0
        for time in sorted(self.delta):
            ongoing += self.delta[time]
            if ongoing > max_overlap:
                max_overlap = ongoing
        return max_overlap
```

## Python3

```python
class MyCalendarThree:
    def __init__(self):
        self.events = []          # stores (time, delta)
        self.max_overlap = 0

    def book(self, startTime: int, endTime: int) -> int:
        self.events.append((startTime, 1))
        self.events.append((endTime, -1))

        cur = 0
        for _, delta in sorted(self.events):
            cur += delta
            if cur > self.max_overlap:
                self.max_overlap = cur
        return self.max_overlap

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int time;
    int delta;
} Node;

typedef struct {
    Node *arr;
    int size;
    int capacity;
} MyCalendarThree;

/* Ensure enough capacity */
static void ensureCapacity(MyCalendarThree *obj) {
    if (obj->size >= obj->capacity) {
        int newCap = obj->capacity ? obj->capacity * 2 : 128;
        Node *newArr = (Node *)realloc(obj->arr, newCap * sizeof(Node));
        if (!newArr) exit(EXIT_FAILURE);
        obj->arr = newArr;
        obj->capacity = newCap;
    }
}

/* Add delta to a specific time point */
static void addDelta(MyCalendarThree *obj, int time, int delta) {
    int l = 0, r = obj->size;
    while (l < r) {
        int m = (l + r) >> 1;
        if (obj->arr[m].time < time)
            l = m + 1;
        else
            r = m;
    }
    if (l < obj->size && obj->arr[l].time == time) {
        obj->arr[l].delta += delta;
    } else {
        ensureCapacity(obj);
        memmove(&obj->arr[l + 1], &obj->arr[l],
                (obj->size - l) * sizeof(Node));
        obj->arr[l].time = time;
        obj->arr[l].delta = delta;
        obj->size++;
    }
}

/* Create a new MyCalendarThree object */
MyCalendarThree* myCalendarThreeCreate() {
    MyCalendarThree *obj = (MyCalendarThree *)malloc(sizeof(MyCalendarThree));
    if (!obj) exit(EXIT_FAILURE);
    obj->arr = NULL;
    obj->size = 0;
    obj->capacity = 0;
    return obj;
}

/* Book an event and return the current maximum overlap */
int myCalendarThreeBook(MyCalendarThree* obj, int startTime, int endTime) {
    addDelta(obj, startTime, 1);
    addDelta(obj, endTime, -1);

    int cur = 0, ans = 0;
    for (int i = 0; i < obj->size; ++i) {
        cur += obj->arr[i].delta;
        if (cur > ans) ans = cur;
    }
    return ans;
}

/* Free the MyCalendarThree object */
void myCalendarThreeFree(MyCalendarThree* obj) {
    if (!obj) return;
    free(obj->arr);
    free(obj);
}
```

## Csharp

```csharp
public class MyCalendarThree
{
    private readonly SortedDictionary<int, int> _timeline;

    public MyCalendarThree()
    {
        _timeline = new SortedDictionary<int, int>();
    }

    public int Book(int startTime, int endTime)
    {
        if (_timeline.ContainsKey(startTime))
            _timeline[startTime] += 1;
        else
            _timeline[startTime] = 1;

        if (_timeline.ContainsKey(endTime))
            _timeline[endTime] -= 1;
        else
            _timeline[endTime] = -1;

        int ongoing = 0, maxOverlap = 0;
        foreach (var kvp in _timeline)
        {
            ongoing += kvp.Value;
            if (ongoing > maxOverlap) maxOverlap = ongoing;
        }
        return maxOverlap;
    }
}
```

## Javascript

```javascript
var MyCalendarThree = function() {
    this.intervals = [];
};

MyCalendarThree.prototype.book = function(startTime, endTime) {
    this.intervals.push([startTime, endTime]);
    const events = [];
    for (const [s, e] of this.intervals) {
        events.push([s, 1]);
        events.push([e, -1]);
    }
    events.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        // same time: start (+1) before end (-1)
        return b[1] - a[1];
    });
    let cur = 0, max = 0;
    for (const [, delta] of events) {
        cur += delta;
        if (cur > max) max = cur;
    }
    return max;
};
```

## Typescript

```typescript
class MyCalendarThree {
    private events: [number, number][] = [];
    private maxOverlap: number = 0;

    constructor() {}

    book(startTime: number, endTime: number): number {
        this.events.push([startTime, 1]);
        this.events.push([endTime, -1]);

        const sorted = [...this.events].sort((a, b) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            // start (+1) before end (-1) when times are equal
            return b[1] - a[1];
        });

        let cur = 0;
        for (const [, delta] of sorted) {
            cur += delta;
            if (cur > this.maxOverlap) this.maxOverlap = cur;
        }
        return this.maxOverlap;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * var obj = new MyCalendarThree()
 * var param_1 = obj.book(startTime,endTime)
 */
```

## Php

```php
class MyCalendarThree {
    /**
     * @var array<int,int>
     */
    private $timeline;
    /**
     * @var int
     */
    private $maxOverlap;

    function __construct() {
        $this->timeline = [];
        $this->maxOverlap = 0;
    }

    /**
     * @param Integer $startTime
     * @param Integer $endTime
     * @return Integer
     */
    function book($startTime, $endTime) {
        if (!isset($this->timeline[$startTime])) {
            $this->timeline[$startTime] = 0;
        }
        $this->timeline[$startTime] += 1;

        if (!isset($this->timeline[$endTime])) {
            $this->timeline[$endTime] = 0;
        }
        $this->timeline[$endTime] -= 1;

        ksort($this->timeline);
        $current = 0;
        foreach ($this->timeline as $delta) {
            $current += $delta;
            if ($current > $this->maxOverlap) {
                $this->maxOverlap = $current;
            }
        }
        return $this->maxOverlap;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * $obj = new MyCalendarThree();
 * $ret_1 = $obj->book($startTime, $endTime);
 */
```

## Swift

```swift
class MyCalendarThree {
    private var intervals: [(Int, Int)] = []
    
    init() { }
    
    func book(_ startTime: Int, _ endTime: Int) -> Int {
        intervals.append((startTime, endTime))
        var delta: [Int: Int] = [:]
        for (s, e) in intervals {
            delta[s, default: 0] += 1
            delta[e, default: 0] -= 1
        }
        let sortedKeys = delta.keys.sorted()
        var cur = 0
        var maxOverlap = 0
        for key in sortedKeys {
            cur += delta[key]!
            if cur > maxOverlap { maxOverlap = cur }
        }
        return maxOverlap
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * let obj = MyCalendarThree()
 * let ret_1: Int = obj.book(startTime, endTime)
 */
```

## Kotlin

```kotlin
class MyCalendarThree() {
    private val timeline = java.util.TreeMap<Int, Int>()
    fun book(startTime: Int, endTime: Int): Int {
        timeline[startTime] = (timeline[startTime] ?: 0) + 1
        timeline[endTime] = (timeline[endTime] ?: 0) - 1
        var cur = 0
        var maxOverlap = 0
        for (delta in timeline.values) {
            cur += delta
            if (cur > maxOverlap) maxOverlap = cur
        }
        return maxOverlap
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * var obj = MyCalendarThree()
 * var param_1 = obj.book(startTime,endTime)
 */
```

## Dart

```dart
import 'dart:collection';

class MyCalendarThree {
  final SplayTreeMap<int, int> _timeline = SplayTreeMap<int, int>();

  MyCalendarThree();

  int book(int startTime, int endTime) {
    _timeline.update(startTime, (v) => v + 1, ifAbsent: () => 1);
    _timeline.update(endTime, (v) => v - 1, ifAbsent: () => -1);

    int ongoing = 0;
    int maxOverlap = 0;
    for (var delta in _timeline.values) {
      ongoing += delta;
      if (ongoing > maxOverlap) maxOverlap = ongoing;
    }
    return maxOverlap;
  }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = MyCalendarThree();
 * int param1 = obj.book(startTime,endTime);
 */
```

## Golang

```go
package main

import "sort"

type MyCalendarThree struct {
	diff map[int]int
}

func Constructor() MyCalendarThree {
	return MyCalendarThree{diff: make(map[int]int)}
}

func (this *MyCalendarThree) Book(startTime int, endTime int) int {
	this.diff[startTime]++
	this.diff[endTime]--

	keys := make([]int, 0, len(this.diff))
	for k := range this.diff {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	cur, maxOverlap := 0, 0
	for _, t := range keys {
		cur += this.diff[t]
		if cur > maxOverlap {
			maxOverlap = cur
		}
	}
	return maxOverlap
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(startTime,endTime);
 */
```

## Ruby

```ruby
class MyCalendarThree
  def initialize()
    @diff = Hash.new(0)
  end

=begin
  :type start_time: Integer
  :type end_time: Integer
  :rtype: Integer
=end
  def book(start_time, end_time)
    @diff[start_time] += 1
    @diff[end_time] -= 1
    cur = 0
    max = 0
    @diff.keys.sort.each do |t|
      cur += @diff[t]
      max = cur if cur > max
    end
    max
  end
end
```

## Scala

```scala
import java.util.TreeMap

class MyCalendarThree() {

  private val timeline = new TreeMap[Int, Int]()

  def book(startTime: Int, endTime: Int): Int = {
    timeline.put(startTime, timeline.getOrDefault(startTime, 0) + 1)
    timeline.put(endTime,   timeline.getOrDefault(endTime,   0) - 1)

    var cur = 0
    var maxOverlap = 0
    val it = timeline.entrySet().iterator()
    while (it.hasNext) {
      val entry = it.next()
      cur += entry.getValue
      if (cur > maxOverlap) maxOverlap = cur
    }
    maxOverlap
  }

}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * val obj = new MyCalendarThree()
 * val param_1 = obj.book(startTime,endTime)
 */
```

## Rust

```rust
use std::collections::BTreeMap;

struct MyCalendarThree {
    timeline: BTreeMap<i32, i32>,
}

impl MyCalendarThree {
    fn new() -> Self {
        MyCalendarThree {
            timeline: BTreeMap::new(),
        }
    }

    fn book(&mut self, start_time: i32, end_time: i32) -> i32 {
        *self.timeline.entry(start_time).or_insert(0) += 1;
        *self.timeline.entry(end_time).or_insert(0) -= 1;

        let mut cur = 0;
        let mut max_overlap = 0;
        for delta in self.timeline.values() {
            cur += delta;
            if cur > max_overlap {
                max_overlap = cur;
            }
        }
        max_overlap
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * let mut obj = MyCalendarThree::new();
 * let ret_1: i32 = obj.book(startTime, endTime);
 */
```

## Racket

```racket
(define my-calendar-three%
  (class object%
    (super-new)
    
    ;; store all time points with their delta (+1 for start, -1 for end)
    (define events '())
    
    ;; book : exact-integer? exact-integer? -> exact-integer?
    (define/public (book start-time end-time)
      (set! events (cons (list start-time 1) events))
      (set! events (cons (list end-time -1) events))
      
      (let* ([sorted
              (sort events
                    (lambda (a b)
                      (let ([ta (first a)] [tb (first b)])
                        (if (= ta tb)
                            (> (second a) (second b)) ; start (+1) before end (-1)
                            (< ta tb)))))]
             [cur 0]
             [mx 0])
        (for ([pt sorted])
          (set! cur (+ cur (second pt)))
          (when (> cur mx) (set! mx cur)))
        mx))))
```

## Erlang

```erlang
-spec my_calendar_three_init_() -> any().
my_calendar_three_init_() ->
    put(my_calendar_three_state, #{}),
    put(my_calendar_three_max, 0).

-spec my_calendar_three_book(StartTime :: integer(), EndTime :: integer()) -> integer().
my_calendar_three_book(StartTime, EndTime) ->
    Map = case get(my_calendar_three_state) of
        undefined -> #{};
        M -> M
    end,
    Updated1 = maps:update_with(
        StartTime,
        fun(V) -> V + 1 end,
        1,
        Map),
    Updated2 = maps:update_with(
        EndTime,
        fun(V) -> V - 1 end,
        -1,
        Updated1),
    put(my_calendar_three_state, Updated2),

    Keys = lists:sort(maps:keys(Updated2)),
    {Max, _} = lists:foldl(
        fun(K, {CurMax, Acc}) ->
            Delta = maps:get(K, Updated2),
            NewAcc = Acc + Delta,
            {erlang:max(CurMax, NewAcc), NewAcc}
        end,
        {0, 0},
        Keys),

    put(my_calendar_three_max, Max),
    Max.
```

## Elixir

```elixir
defmodule MyCalendarThree do
  @spec init_() :: any
  def init_() do
    Process.put(:my_calendar_three, %{deltas: %{}, max_overlap: 0})
  end

  @spec book(start_time :: integer, end_time :: integer) :: integer
  def book(start_time, end_time) do
    state = Process.get(:my_calendar_three)
    deltas = state.deltas

    deltas =
      Map.update(deltas, start_time, 1, fn v -> v + 1 end)
      |> Map.update(end_time, -1, fn v -> v - 1 end)

    sorted = Enum.sort_by(Map.to_list(deltas), fn {k, _v} -> k end)

    {_cur, max_overlap} =
      Enum.reduce(sorted, {0, state.max_overlap}, fn {_pt, delta}, {curr, max} ->
        curr = curr + delta
        if curr > max, do: {curr, curr}, else: {curr, max}
      end)

    new_state = %{deltas: deltas, max_overlap: max_overlap}
    Process.put(:my_calendar_three, new_state)
    max_overlap
  end
end
```

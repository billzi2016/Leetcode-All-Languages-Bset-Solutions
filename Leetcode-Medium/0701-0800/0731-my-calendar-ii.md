# 0731. My Calendar II

## Cpp

```cpp
class MyCalendarTwo {
    std::vector<std::pair<int,int>> bookings;
    std::vector<std::pair<int,int>> overlaps;
public:
    MyCalendarTwo() {}
    
    bool book(int startTime, int endTime) {
        // If it overlaps any double-booked interval, reject.
        for (const auto& o : overlaps) {
            if (std::max(startTime, o.first) < std::min(endTime, o.second))
                return false;
        }
        // Record new double bookings formed with existing single bookings.
        for (const auto& b : bookings) {
            int s = std::max(startTime, b.first);
            int e = std::min(endTime, b.second);
            if (s < e)
                overlaps.emplace_back(s, e);
        }
        bookings.emplace_back(startTime, endTime);
        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(startTime,endTime);
 */
```

## Java

```java
class MyCalendarTwo {
    private final java.util.List<int[]> bookings;
    private final java.util.List<int[]> overlaps;

    public MyCalendarTwo() {
        bookings = new java.util.ArrayList<>();
        overlaps = new java.util.ArrayList<>();
    }

    public boolean book(int startTime, int endTime) {
        // Check against existing double bookings
        for (int[] o : overlaps) {
            if (Math.max(o[0], startTime) < Math.min(o[1], endTime)) {
                return false; // would cause triple booking
            }
        }

        // Record new overlaps with single bookings
        for (int[] b : bookings) {
            int s = Math.max(b[0], startTime);
            int e = Math.min(b[1], endTime);
            if (s < e) { // overlap exists
                overlaps.add(new int[]{s, e});
            }
        }

        // Add the new booking
        bookings.add(new int[]{startTime, endTime});
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(startTime,endTime);
 */
```

## Python

```python
class MyCalendarTwo(object):
    def __init__(self):
        self.booked = []      # all accepted bookings
        self.overlaps = []    # intervals that are double booked

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        # Check against existing double-booked intervals.
        for s, e in self.overlaps:
            if max(startTime, s) < min(endTime, e):
                return False

        # Record new overlaps with single bookings.
        for s, e in self.booked:
            ov_start = max(startTime, s)
            ov_end = min(endTime, e)
            if ov_start < ov_end:
                self.overlaps.append((ov_start, ov_end))

        # Add the new booking.
        self.booked.append((startTime, endTime))
        return True
```

## Python3

```python
class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Check against existing double bookings
        for s, e in self.overlaps:
            if max(startTime, s) < min(endTime, e):
                return False

        # Record new overlaps with single bookings
        for s, e in self.bookings:
            ov_start = max(startTime, s)
            ov_end = min(endTime, e)
            if ov_start < ov_end:
                self.overlaps.append((ov_start, ov_end))

        # Add the new booking
        self.bookings.append((startTime, endTime))
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *start;
    int *end;
    int sz;
    int cap;
    int *ovStart;
    int *ovEnd;
    int ovSz;
    int ovCap;
} MyCalendarTwo;

static void ensureCapacity(int **arr, int *cap) {
    if (*cap == 0) {
        *cap = 4;
        *arr = (int *)malloc((*cap) * sizeof(int));
    } else if ((*cap) == 0) {
        // never reached
    }
}

static void addInterval(MyCalendarTwo *obj, int s, int e) {
    if (obj->sz == obj->cap) {
        int newCap = obj->cap ? obj->cap * 2 : 4;
        obj->start = (int *)realloc(obj->start, newCap * sizeof(int));
        obj->end   = (int *)realloc(obj->end,   newCap * sizeof(int));
        obj->cap = newCap;
    }
    obj->start[obj->sz] = s;
    obj->end[obj->sz]   = e;
    obj->sz++;
}

static void addOverlap(MyCalendarTwo *obj, int s, int e) {
    if (obj->ovSz == obj->ovCap) {
        int newCap = obj->ovCap ? obj->ovCap * 2 : 4;
        obj->ovStart = (int *)realloc(obj->ovStart, newCap * sizeof(int));
        obj->ovEnd   = (int *)realloc(obj->ovEnd,   newCap * sizeof(int));
        obj->ovCap = newCap;
    }
    obj->ovStart[obj->ovSz] = s;
    obj->ovEnd[obj->ovSz]   = e;
    obj->ovSz++;
}

static bool intervalsOverlap(int aStart, int aEnd, int bStart, int bEnd) {
    return !(aEnd <= bStart || aStart >= bEnd);
}

/** Initialize your data structure here. */
MyCalendarTwo* myCalendarTwoCreate() {
    MyCalendarTwo *obj = (MyCalendarTwo *)malloc(sizeof(MyCalendarTwo));
    obj->start = NULL;
    obj->end   = NULL;
    obj->sz = 0;
    obj->cap = 0;
    obj->ovStart = NULL;
    obj->ovEnd   = NULL;
    obj->ovSz = 0;
    obj->ovCap = 0;
    return obj;
}

/** Attempts to book an event. */
bool myCalendarTwoBook(MyCalendarTwo* obj, int startTime, int endTime) {
    // Check against existing double bookings
    for (int i = 0; i < obj->ovSz; ++i) {
        if (intervalsOverlap(startTime, endTime, obj->ovStart[i], obj->ovEnd[i]))
            return false;
    }
    // Record new overlaps with single bookings
    for (int i = 0; i < obj->sz; ++i) {
        if (intervalsOverlap(startTime, endTime, obj->start[i], obj->end[i])) {
            int os = startTime > obj->start[i] ? startTime : obj->start[i];
            int oe = endTime   < obj->end[i]   ? endTime   : obj->end[i];
            addOverlap(obj, os, oe);
        }
    }
    // Add the new booking
    addInterval(obj, startTime, endTime);
    return true;
}

/** Deallocate memory. */
void myCalendarTwoFree(MyCalendarTwo* obj) {
    if (!obj) return;
    free(obj->start);
    free(obj->end);
    free(obj->ovStart);
    free(obj->ovEnd);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class MyCalendarTwo
{
    private readonly List<(int start, int end)> bookings;
    private readonly List<(int start, int end)> overlaps;

    public MyCalendarTwo()
    {
        bookings = new List<(int, int)>();
        overlaps = new List<(int, int)>();
    }

    public bool Book(int startTime, int endTime)
    {
        foreach (var o in overlaps)
        {
            if (Math.Max(startTime, o.start) < Math.Min(endTime, o.end))
                return false;
        }

        foreach (var b in bookings)
        {
            int s = Math.Max(startTime, b.start);
            int e = Math.Min(endTime, b.end);
            if (s < e)
                overlaps.Add((s, e));
        }

        bookings.Add((startTime, endTime));
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * bool param_1 = obj.Book(startTime,endTime);
 */
```

## Javascript

```javascript
var MyCalendarTwo = function() {
    this.bookings = [];
    this.overlaps = [];
};

/**
 * @param {number} startTime
 * @param {number} endTime
 * @return {boolean}
 */
MyCalendarTwo.prototype.book = function(startTime, endTime) {
    // Check against double-booked intervals
    for (let i = 0; i < this.overlaps.length; i++) {
        const o = this.overlaps[i];
        if (Math.max(startTime, o[0]) < Math.min(endTime, o[1])) {
            return false;
        }
    }
    // Record new overlaps with existing single bookings
    for (let i = 0; i < this.bookings.length; i++) {
        const b = this.bookings[i];
        const s = Math.max(startTime, b[0]);
        const e = Math.min(endTime, b[1]);
        if (s < e) {
            this.overlaps.push([s, e]);
        }
    }
    // Add the new booking
    this.bookings.push([startTime, endTime]);
    return true;
};
```

## Typescript

```typescript
class MyCalendarTwo {
    private bookings: Array<[number, number]>;
    private overlaps: Array<[number, number]>;

    constructor() {
        this.bookings = [];
        this.overlaps = [];
    }

    book(startTime: number, endTime: number): boolean {
        // Check against existing double-booked intervals
        for (const [s, e] of this.overlaps) {
            if (Math.max(s, startTime) < Math.min(e, endTime)) {
                return false; // would cause a triple booking
            }
        }

        // Record new overlaps with single bookings
        for (const [s, e] of this.bookings) {
            const overlapStart = Math.max(s, startTime);
            const overlapEnd = Math.min(e, endTime);
            if (overlapStart < overlapEnd) {
                this.overlaps.push([overlapStart, overlapEnd]);
            }
        }

        // Add the new booking
        this.bookings.push([startTime, endTime]);
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = new MyCalendarTwo()
 * var param_1 = obj.book(startTime,endTime)
 */
```

## Php

```php
class MyCalendarTwo {
    /**
     * @var array
     */
    private $bookings = [];
    /**
     * @var array
     */
    private $overlaps = [];

    /**
     * Initialize your data structure here.
     */
    function __construct() {
        // No initialization needed beyond property defaults.
    }

    /**
     * @param Integer $startTime
     * @param Integer $endTime
     * @return Boolean
     */
    function book($startTime, $endTime) {
        // If the new event overlaps any double-booked interval, reject it.
        foreach ($this->overlaps as $interval) {
            if (max($startTime, $interval[0]) < min($endTime, $interval[1])) {
                return false;
            }
        }

        // Record new double bookings caused by overlapping with existing single bookings.
        foreach ($this->bookings as $b) {
            $s = max($startTime, $b[0]);
            $e = min($endTime, $b[1]);
            if ($s < $e) {
                $this->overlaps[] = [$s, $e];
            }
        }

        // Add the new booking to the list of all bookings.
        $this->bookings[] = [$startTime, $endTime];
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * $obj = new MyCalendarTwo();
 * $ret_1 = $obj->book($startTime, $endTime);
 */
```

## Swift

```swift
class MyCalendarTwo {
    private var bookings: [(Int, Int)] = []
    private var overlaps: [(Int, Int)] = []

    init() {}

    func book(_ startTime: Int, _ endTime: Int) -> Bool {
        // Check if new event would cause a triple booking
        for (s, e) in overlaps {
            if max(startTime, s) < min(endTime, e) {
                return false
            }
        }

        // Record new double bookings created by this event
        for (s, e) in bookings {
            let ovStart = max(startTime, s)
            let ovEnd = min(endTime, e)
            if ovStart < ovEnd {
                overlaps.append((ovStart, ovEnd))
            }
        }

        // Add the new booking
        bookings.append((startTime, endTime))
        return true
    }
}
```

## Kotlin

```kotlin
class MyCalendarTwo() {
    private val bookings = mutableListOf<Pair<Int, Int>>()
    private val overlaps = mutableListOf<Pair<Int, Int>>()

    fun book(startTime: Int, endTime: Int): Boolean {
        // Check if new interval would overlap any double-booked interval
        for ((s, e) in overlaps) {
            if (maxOf(startTime, s) < minOf(endTime, e)) return false
        }
        // Record new double bookings caused by this interval
        for ((s, e) in bookings) {
            val ovStart = maxOf(startTime, s)
            val ovEnd = minOf(endTime, e)
            if (ovStart < ovEnd) {
                overlaps.add(Pair(ovStart, ovEnd))
            }
        }
        // Add the new booking
        bookings.add(Pair(startTime, endTime))
        return true
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = MyCalendarTwo()
 * var param_1 = obj.book(startTime,endTime)
 */
```

## Dart

```dart
class MyCalendarTwo {
  final List<List<int>> _bookings = [];
  final List<List<int>> _overlaps = [];

  MyCalendarTwo();

  bool book(int startTime, int endTime) {
    // Check if new event overlaps any double-booked interval
    for (var o in _overlaps) {
      if (startTime < o[1] && endTime > o[0]) {
        return false;
      }
    }

    // Record new overlaps with existing single bookings
    for (var b in _bookings) {
      int s = startTime > b[0] ? startTime : b[0];
      int e = endTime < b[1] ? endTime : b[1];
      if (s < e) {
        _overlaps.add([s, e]);
      }
    }

    // Add the new booking
    _bookings.add([startTime, endTime]);
    return true;
  }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = MyCalendarTwo();
 * bool param1 = obj.book(startTime,endTime);
 */
```

## Golang

```go
type interval struct {
	start, end int
}

type MyCalendarTwo struct {
	bookings []interval
	overlaps []interval
}

func Constructor() MyCalendarTwo {
	return MyCalendarTwo{}
}

func (this *MyCalendarTwo) Book(startTime int, endTime int) bool {
	// Check against existing double bookings
	for _, ov := range this.overlaps {
		if max(startTime, ov.start) < min(endTime, ov.end) {
			return false
		}
	}
	// Record new overlaps with single bookings
	for _, b := range this.bookings {
		s := max(startTime, b.start)
		e := min(endTime, b.end)
		if s < e {
			this.overlaps = append(this.overlaps, interval{s, e})
		}
	}
	// Add the new booking
	this.bookings = append(this.bookings, interval{startTime, endTime})
	return true
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(startTime,endTime);
 */
```

## Ruby

```ruby
class MyCalendarTwo
  def initialize()
    @bookings = []
    @overlaps = []
  end

=begin
    :type start_time: Integer
    :type end_time: Integer
    :rtype: Boolean
=end
  def book(start_time, end_time)
    # If it overlaps any double-booked interval, it would become triple booked.
    @overlaps.each do |ov|
      return false if start_time < ov[1] && end_time > ov[0]
    end

    # Record new double bookings caused by this event.
    @bookings.each do |b|
      s = [start_time, b[0]].max
      e = [end_time, b[1]].min
      @overlaps << [s, e] if s < e
    end

    @bookings << [start_time, end_time]
    true
  end
end
```

## Scala

```scala
import scala.collection.mutable.ListBuffer

class MyCalendarTwo() {

  private val bookings = ListBuffer[(Int, Int)]()
  private val overlaps = ListBuffer[(Int, Int)]()

  def book(startTime: Int, endTime: Int): Boolean = {
    // Check if new event would overlap with any double-booked interval
    for ((os, oe) <- overlaps) {
      if (math.max(startTime, os) < math.min(endTime, oe)) return false
    }
    // Record new double bookings created by this event
    for ((bs, be) <- bookings) {
      val s = math.max(startTime, bs)
      val e = math.min(endTime, be)
      if (s < e) overlaps += ((s, e))
    }
    bookings += ((startTime, endTime))
    true
  }

}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * val obj = new MyCalendarTwo()
 * val param_1 = obj.book(startTime,endTime)
 */
```

## Rust

```rust
use std::cmp::{max, min};

struct MyCalendarTwo {
    bookings: Vec<(i32, i32)>,
    overlaps: Vec<(i32, i32)>,
}

impl MyCalendarTwo {
    fn new() -> Self {
        MyCalendarTwo {
            bookings: Vec::new(),
            overlaps: Vec::new(),
        }
    }

    fn book(&mut self, start_time: i32, end_time: i32) -> bool {
        // If it overlaps any double-booked interval, reject.
        for &(s, e) in &self.overlaps {
            if start_time < e && end_time > s {
                return false;
            }
        }

        // Record new double bookings created by this event.
        let mut new_overlaps = Vec::new();
        for &(s, e) in &self.bookings {
            if start_time < e && end_time > s {
                new_overlaps.push((max(start_time, s), min(end_time, e)));
            }
        }

        self.overlaps.extend(new_overlaps);
        self.bookings.push((start_time, end_time));
        true
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * let mut obj = MyCalendarTwo::new();
 * let ret_1: bool = obj.book(startTime, endTime);
 */
```

## Racket

```racket
(define (overlap? s1 e1 s2 e2)
  (< (max s1 s2) (min e1 e2)))

(define (get-overlap s1 e1 s2 e2)
  (cons (max s1 s2) (min e1 e2)))

(define my-calendar-two%
  (class object%
    (super-new)

    ; list of all bookings as pairs (start . end)
    (define bookings '())
    ; list of double‑booked intervals
    (define overlaps '())

    ;; book : exact-integer? exact-integer? -> boolean?
    (define/public (book start-time end-time)
      ;; if the new interval overlaps any existing double booking, reject
      (if (for/or ([ov overlaps])
            (overlap? start-time end-time (car ov) (cdr ov)))
          #f
          (begin
            ;; collect new double‑booking intervals caused by this booking
            (let loop ((bs bookings) (new-ovs '()))
              (cond
                [(null? bs)
                 (set! overlaps (append overlaps (reverse new-ovs)))]
                [else
                 (define b (car bs))
                 (define s (car b))
                 (define e (cdr b))
                 (if (overlap? start-time end-time s e)
                     (loop (cdr bs)
                           (cons (get-overlap start-time end-time s e) new-ovs))
                     (loop (cdr bs) new-ovs))]))
            ;; add the booking itself
            (set! bookings (cons (cons start-time end-time) bookings))
            #t))))
  )
;; Usage example:
;; (define obj (new my-calendar-two%))
;; (send obj book 10 20) ; => #t
;; (send obj book 5 15)  ; => #f etc.
```

## Erlang

```erlang
-module(my_calendar_two).
-export([my_calendar_two_init_/0, my_calendar_two_book/2]).

my_calendar_two_init_() ->
    case ets:info(bookings) of
        undefined -> ok;
        _ -> ets:delete(bookings)
    end,
    ets:new(bookings, [named_table, public, bag]),
    case ets:info(overlaps) of
        undefined -> ok;
        _ -> ets:delete(overlaps)
    end,
    ets:new(overlaps, [named_table, public, bag]),
    ok.

my_calendar_two_book(Start, End) ->
    OverlapExists = lists:any(
        fun({OS, OE}) ->
            erlang:max(Start, OS) < erlang:min(End, OE)
        end,
        ets:tab2list(overlaps)),
    if
        OverlapExists -> false;
        true ->
            Bookings = ets:tab2list(bookings),
            lists:foreach(
                fun({BS, BE}) ->
                    IStart = erlang:max(Start, BS),
                    IEnd   = erlang:min(End, BE),
                    case IStart < IEnd of
                        true -> ets:insert(overlaps, {IStart, IEnd});
                        false -> ok
                    end
                end,
                Bookings),
            ets:insert(bookings, {Start, End}),
            true
    end.
```

## Elixir

```elixir
defmodule MyCalendarTwo do
  @spec init_() :: any
  def init_() do
    Process.put(:bookings, [])
    Process.put(:overlaps, [])
    :ok
  end

  @spec book(start_time :: integer, end_time :: integer) :: boolean
  def book(start_time, end_time) do
    overlaps = Process.get(:overlaps, [])

    # If the new interval overlaps any double‑booked interval, reject it.
    if Enum.any?(overlaps, fn {s, e} ->
         max(s, start_time) < min(e, end_time)
       end) do
      false
    else
      bookings = Process.get(:bookings, [])

      # Find new overlaps with existing single bookings.
      new_overlaps =
        for {bs, be} <- bookings,
            s = max(bs, start_time),
            e = min(be, end_time),
            s < e,
            do: {s, e}

      # Update stored intervals.
      Process.put(:bookings, [{start_time, end_time} | bookings])
      Process.put(:overlaps, new_overlaps ++ overlaps)

      true
    end
  end
end
```

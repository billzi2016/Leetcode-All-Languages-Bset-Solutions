# 0729. My Calendar I

## Cpp

```cpp
class MyCalendar {
public:
    MyCalendar() = default;
    
    bool book(int startTime, int endTime) {
        auto it = events.lower_bound({startTime, endTime});
        if (it != events.end() && it->first < endTime) return false;
        if (it != events.begin()) {
            auto prev = std::prev(it);
            if (prev->second > startTime) return false;
        }
        events.insert({startTime, endTime});
        return true;
    }
private:
    std::set<std::pair<int,int>> events;
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */
```

## Java

```java
class MyCalendar {
    private final java.util.TreeMap<Integer, Integer> calendar;

    public MyCalendar() {
        calendar = new java.util.TreeMap<>();
    }

    public boolean book(int startTime, int endTime) {
        // Find the event with the greatest start time <= startTime
        java.util.Map.Entry<Integer, Integer> prev = calendar.floorEntry(startTime);
        if (prev != null && prev.getValue() > startTime) {
            return false; // Overlaps with previous event
        }
        // Find the first event with start time >= startTime
        java.util.Map.Entry<Integer, Integer> next = calendar.ceilingEntry(startTime);
        if (next != null && next.getKey() < endTime) {
            return false; // Overlaps with next event
        }
        calendar.put(startTime, endTime);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(startTime,endTime);
 */
```

## Python

```python
class MyCalendar(object):
    def __init__(self):
        self.intervals = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        import bisect
        i = bisect.bisect_left(self.intervals, (startTime, endTime))
        # Check previous interval
        if i > 0 and self.intervals[i - 1][1] > startTime:
            return False
        # Check next interval
        if i < len(self.intervals) and self.intervals[i][0] < endTime:
            return False
        self.intervals.insert(i, (startTime, endTime))
        return True
```

## Python3

```python
class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        import bisect
        idx = bisect.bisect_left(self.calendar, (startTime, endTime))
        # Check previous interval
        if idx > 0 and self.calendar[idx - 1][1] > startTime:
            return False
        # Check next interval
        if idx < len(self.calendar) and endTime > self.calendar[idx][0]:
            return False
        self.calendar.insert(idx, (startTime, endTime))
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *starts;
    int *ends;
    int size;
    int capacity;
} MyCalendar;

MyCalendar* myCalendarCreate() {
    MyCalendar *obj = (MyCalendar *)malloc(sizeof(MyCalendar));
    if (!obj) return NULL;
    obj->capacity = 16;
    obj->size = 0;
    obj->starts = (int *)malloc(obj->capacity * sizeof(int));
    obj->ends   = (int *)malloc(obj->capacity * sizeof(int));
    return obj;
}

bool myCalendarBook(MyCalendar* obj, int startTime, int endTime) {
    for (int i = 0; i < obj->size; ++i) {
        if (startTime < obj->ends[i] && obj->starts[i] < endTime) {
            return false; // overlap
        }
    }
    if (obj->size == obj->capacity) {
        int newCap = obj->capacity * 2;
        int *newStarts = (int *)realloc(obj->starts, newCap * sizeof(int));
        int *newEnds   = (int *)realloc(obj->ends,   newCap * sizeof(int));
        if (!newStarts || !newEnds) return false; // allocation failure
        obj->starts = newStarts;
        obj->ends = newEnds;
        obj->capacity = newCap;
    }
    obj->starts[obj->size] = startTime;
    obj->ends[obj->size]   = endTime;
    obj->size++;
    return true;
}

void myCalendarFree(MyCalendar* obj) {
    if (!obj) return;
    free(obj->starts);
    free(obj->ends);
    free(obj);
}
```

## Csharp

```csharp
public class MyCalendar
{
    private readonly List<(int start, int end)> _events;

    public MyCalendar()
    {
        _events = new List<(int, int)>();
    }

    public bool Book(int startTime, int endTime)
    {
        foreach (var ev in _events)
        {
            if (startTime < ev.end && ev.start < endTime)
                return false;
        }
        _events.Add((startTime, endTime));
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.Book(startTime,endTime);
 */
```

## Javascript

```javascript
var MyCalendar = function() {
    this.events = [];
};

MyCalendar.prototype.book = function(startTime, endTime) {
    let lo = 0, hi = this.events.length;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (this.events[mid][0] < startTime) lo = mid + 1;
        else hi = mid;
    }
    // Check previous event
    if (lo > 0 && this.events[lo - 1][1] > startTime) return false;
    // Check next event
    if (lo < this.events.length && endTime > this.events[lo][0]) return false;
    this.events.splice(lo, 0, [startTime, endTime]);
    return true;
};
```

## Typescript

```typescript
class MyCalendar {
    private calendar: [number, number][];

    constructor() {
        this.calendar = [];
    }

    book(startTime: number, endTime: number): boolean {
        let lo = 0;
        let hi = this.calendar.length;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (this.calendar[mid][0] < startTime) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        // Check overlap with previous interval
        if (lo > 0 && this.calendar[lo - 1][1] > startTime) {
            return false;
        }
        // Check overlap with next interval
        if (lo < this.calendar.length && endTime > this.calendar[lo][0]) {
            return false;
        }

        this.calendar.splice(lo, 0, [startTime, endTime]);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(startTime,endTime)
 */
```

## Php

```php
class MyCalendar {
    private $calendar;

    /**
     * Initialize your data structure here.
     */
    function __construct() {
        $this->calendar = [];
    }

    /**
     * @param Integer $startTime
     * @param Integer $endTime
     * @return Boolean
     */
    function book($startTime, $endTime) {
        foreach ($this->calendar as $interval) {
            // Check if there is an overlap
            if (!($endTime <= $interval[0] || $startTime >= $interval[1])) {
                return false;
            }
        }
        $this->calendar[] = [$startTime, $endTime];
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * $obj = new MyCalendar();
 * $ret_1 = $obj->book($startTime, $endTime);
 */
```

## Swift

```swift
class MyCalendar {
    private var events: [(start: Int, end: Int)] = []
    
    init() { }
    
    func book(_ startTime: Int, _ endTime: Int) -> Bool {
        // binary search for the first event with start >= startTime
        var left = 0
        var right = events.count
        while left < right {
            let mid = (left + right) / 2
            if events[mid].start < startTime {
                left = mid + 1
            } else {
                right = mid
            }
        }
        // check overlap with previous event
        if left > 0 && events[left - 1].end > startTime {
            return false
        }
        // check overlap with next event
        if left < events.count && endTime > events[left].start {
            return false
        }
        events.insert((start: startTime, end: endTime), at: left)
        return true
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar()
 * let ret_1: Bool = obj.book(startTime, endTime)
 */
```

## Kotlin

```kotlin
class MyCalendar() {
    private val calendar = java.util.TreeMap<Int, Int>()

    fun book(startTime: Int, endTime: Int): Boolean {
        val prev = calendar.floorEntry(startTime)
        if (prev != null && prev.value > startTime) return false
        val next = calendar.ceilingEntry(startTime)
        if (next != null && next.key < endTime) return false
        calendar[startTime] = endTime
        return true
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = MyCalendar()
 * var param_1 = obj.book(startTime,endTime)
 */
```

## Dart

```dart
class MyCalendar {
  final List<List<int>> _events = [];

  MyCalendar();

  bool book(int startTime, int endTime) {
    // Find insertion index using binary search
    int left = 0;
    int right = _events.length;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (_events[mid][0] < startTime) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    // Check overlap with previous interval
    if (left > 0 && _events[left - 1][1] > startTime) {
      return false;
    }
    // Check overlap with next interval
    if (left < _events.length && endTime > _events[left][0]) {
      return false;
    }

    _events.insert(left, [startTime, endTime]);
    return true;
  }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = MyCalendar();
 * bool param1 = obj.book(startTime,endTime);
 */
```

## Golang

```go
type MyCalendar struct {
	events [][]int
}

func Constructor() MyCalendar {
	return MyCalendar{events: make([][]int, 0)}
}

func (this *MyCalendar) Book(startTime int, endTime int) bool {
	for _, e := range this.events {
		if startTime < e[1] && e[0] < endTime {
			return false
		}
	}
	this.events = append(this.events, []int{startTime, endTime})
	return true
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(startTime,endTime);
 */
```

## Ruby

```ruby
class MyCalendar
  def initialize()
    @events = []
  end

=begin
    :type start_time: Integer
    :type end_time: Integer
    :rtype: Boolean
=end
  def book(start_time, end_time)
    # binary search for insertion index (first event with start >= start_time)
    lo = 0
    hi = @events.length
    while lo < hi
      mid = (lo + hi) / 2
      if @events[mid][0] < start_time
        lo = mid + 1
      else
        hi = mid
      end
    end
    idx = lo

    # check overlap with previous event
    if idx > 0 && @events[idx - 1][1] > start_time
      return false
    end

    # check overlap with next event
    if idx < @events.length && @events[idx][0] < end_time
      return false
    end

    @events.insert(idx, [start_time, end_time])
    true
  end
end
```

## Scala

```scala
class MyCalendar() {
  private val map = new java.util.TreeMap[Int, Int]()

  def book(startTime: Int, endTime: Int): Boolean = {
    val prev = map.floorEntry(startTime)
    if (prev != null && prev.getValue > startTime) return false

    val next = map.ceilingEntry(startTime)
    if (next != null && next.getKey < endTime) return false

    map.put(startTime, endTime)
    true
  }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * val obj = new MyCalendar()
 * val param_1 = obj.book(startTime,endTime)
 */
```

## Rust

```rust
struct MyCalendar {
    events: Vec<(i32, i32)>,
}

impl MyCalendar {
    fn new() -> Self {
        MyCalendar { events: Vec::new() }
    }

    fn book(&mut self, start_time: i32, end_time: i32) -> bool {
        for &(s, e) in &self.events {
            if start_time < e && s < end_time {
                return false;
            }
        }
        self.events.push((start_time, end_time));
        true
    }
}
```

## Racket

```racket
(define my-calendar%
  (class object%
    (super-new)
    (define events '())
    ;; book : exact-integer? exact-integer? -> boolean?
    (define/public (book start-time end-time)
      (let loop ((lst events))
        (cond
          [(null? lst)
           (set! events (cons (cons start-time end-time) events))
           #t]
          [else
           (let* ([interval (car lst)]
                  [s (car interval)]
                  [e (cdr interval)])
             (if (and (< start-time e) (< s end-time))
                 #f
                 (loop (cdr lst))))])))))
```

## Erlang

```erlang
-module(my_calendar).
-export([my_calendar_init_/0, my_calendar_book/2]).

my_calendar_init_() ->
    put(calendar, []).

my_calendar_book(Start, End) ->
    Calendar = get(calendar),
    case has_overlap(Calendar, Start, End) of
        true -> false;
        false ->
            put(calendar, [{Start, End} | Calendar]),
            true
    end.

has_overlap([], _, _) -> false;
has_overlap([{S, E} | Rest], Start, End) ->
    if
        End =< S; E =< Start ->
            has_overlap(Rest, Start, End);
        true ->
            true
    end.
```

## Elixir

```elixir
defmodule MyCalendar do
  @spec init_() :: any
  def init_() do
    Process.put(:my_calendar_intervals, [])
    :ok
  end

  @spec book(start_time :: integer, end_time :: integer) :: boolean
  def book(start_time, end_time) do
    intervals = Process.get(:my_calendar_intervals, [])

    conflict =
      Enum.any?(intervals, fn {s, e} ->
        start_time < e and s < end_time
      end)

    if conflict do
      false
    else
      idx = Enum.find_index(intervals, fn {s, _} -> start_time < s end) || length(intervals)
      new_intervals = List.insert_at(intervals, idx, {start_time, end_time})
      Process.put(:my_calendar_intervals, new_intervals)
      true
    end
  end
end
```

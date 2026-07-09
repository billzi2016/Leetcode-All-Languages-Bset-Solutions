# 0933. Number of Recent Calls

## Cpp

```cpp
class RecentCounter {
public:
    RecentCounter() {}
    
    int ping(int t) {
        timestamps.push(t);
        while (!timestamps.empty() && timestamps.front() < t - 3000) {
            timestamps.pop();
        }
        return (int)timestamps.size();
    }
private:
    std::queue<int> timestamps;
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

class RecentCounter {
    private Deque<Integer> q;

    public RecentCounter() {
        q = new ArrayDeque<>();
    }

    public int ping(int t) {
        q.addLast(t);
        while (!q.isEmpty() && q.peekFirst() < t - 3000) {
            q.pollFirst();
        }
        return q.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
```

## Python

```python
import collections

class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
```

## Python3

```python
class RecentCounter:
    def __init__(self):
        from collections import deque
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        limit = t - 3000
        while self.q and self.q[0] < limit:
            self.q.popleft()
        return len(self.q)
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *data;
    int head;      // index of the first valid timestamp
    int size;      // number of timestamps currently in the window
    int capacity;  // total allocated capacity
} RecentCounter;

RecentCounter* recentCounterCreate() {
    RecentCounter *obj = (RecentCounter *)malloc(sizeof(RecentCounter));
    if (!obj) return NULL;
    obj->capacity = 10005;               // enough for all possible calls (<=10^4)
    obj->data = (int *)malloc(obj->capacity * sizeof(int));
    obj->head = 0;
    obj->size = 0;
    return obj;
}

int recentCounterPing(RecentCounter* obj, int t) {
    // Append the new timestamp
    obj->data[obj->head + obj->size] = t;
    obj->size++;

    // Remove timestamps older than (t - 3000)
    while (obj->size > 0 && obj->data[obj->head] < t - 3000) {
        obj->head++;
        obj->size--;
    }
    return obj->size;
}

void recentCounterFree(RecentCounter* obj) {
    if (!obj) return;
    free(obj->data);
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class RecentCounter {
    private readonly Queue<int> _queue;

    public RecentCounter() {
        _queue = new Queue<int>();
    }
    
    public int Ping(int t) {
        _queue.Enqueue(t);
        while (_queue.Peek() < t - 3000) {
            _queue.Dequeue();
        }
        return _queue.Count;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.Ping(t);
 */
```

## Javascript

```javascript
var RecentCounter = function() {
    this.times = [];
    this.head = 0;
};

/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    this.times.push(t);
    while (this.times[this.head] < t - 3000) {
        this.head++;
    }
    return this.times.length - this.head;
};
```

## Typescript

```typescript
class RecentCounter {
    private timestamps: number[] = [];
    private startIdx: number = 0;

    constructor() {}

    ping(t: number): number {
        this.timestamps.push(t);
        while (this.startIdx < this.timestamps.length && this.timestamps[this.startIdx] < t - 3000) {
            this.startIdx++;
        }
        return this.timestamps.length - this.startIdx;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
```

## Php

```php
class RecentCounter {
    private array $times = [];
    private int $head = 0;

    function __construct() {
        $this->times = [];
        $this->head = 0;
    }

    /**
     * @param Integer $t
     * @return Integer
     */
    function ping($t) {
        $this->times[] = $t;
        while ($this->head < count($this->times) && $t - $this->times[$this->head] > 3000) {
            $this->head++;
        }
        return count($this->times) - $this->head;
    }
}
```

## Swift

```swift
class RecentCounter {
    private var timestamps: [Int] = []
    private var head: Int = 0

    init() { }

    func ping(_ t: Int) -> Int {
        timestamps.append(t)
        while head < timestamps.count && timestamps[head] < t - 3000 {
            head += 1
        }
        return timestamps.count - head
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class RecentCounter() {

    private val queue = ArrayDeque<Int>()

    fun ping(t: Int): Int {
        queue.addLast(t)
        while (queue.peekFirst() < t - 3000) {
            queue.removeFirst()
        }
        return queue.size
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = RecentCounter()
 * var param_1 = obj.ping(t)
 */
```

## Dart

```dart
import 'dart:collection';

class RecentCounter {
  final Queue<int> _queue = Queue<int>();

  RecentCounter();

  int ping(int t) {
    _queue.addLast(t);
    while (_queue.isNotEmpty && _queue.first < t - 3000) {
      _queue.removeFirst();
    }
    return _queue.length;
  }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = RecentCounter();
 * int param1 = obj.ping(t);
 */
```

## Golang

```go
type RecentCounter struct {
	q     []int
	start int
}

func Constructor() RecentCounter {
	return RecentCounter{
		q:     make([]int, 0),
		start: 0,
	}
}

func (this *RecentCounter) Ping(t int) int {
	this.q = append(this.q, t)
	for this.start < len(this.q) && this.q[this.start] < t-3000 {
		this.start++
	}
	return len(this.q) - this.start
}
```

## Ruby

```ruby
class RecentCounter
    def initialize()
        @times = []
    end

=begin
    :type t: Integer
    :rtype: Integer
=end
    def ping(t)
        @times << t
        while @times[0] < t - 3000
            @times.shift
        end
        @times.size
    end
end
```

## Scala

```scala
class RecentCounter() {
  private val q = scala.collection.mutable.Queue[Int]()
  
  def ping(t: Int): Int = {
    q.enqueue(t)
    while (q.nonEmpty && q.front < t - 3000) {
      q.dequeue()
    }
    q.size
  }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * val obj = new RecentCounter()
 * val param_1 = obj.ping(t)
 */
```

## Rust

```rust
use std::collections::VecDeque;

struct RecentCounter {
    q: VecDeque<i32>,
}

impl RecentCounter {
    fn new() -> Self {
        RecentCounter { q: VecDeque::new() }
    }

    fn ping(&mut self, t: i32) -> i32 {
        self.q.push_back(t);
        while let Some(&front) = self.q.front() {
            if front < t - 3000 {
                self.q.pop_front();
            } else {
                break;
            }
        }
        self.q.len() as i32
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * let mut obj = RecentCounter::new();
 * let ret_1: i32 = obj.ping(t);
 */
```

## Racket

```racket
(require racket)

(define recent-counter%
  (class object%
    (super-new)
    (define q '())
    ;; ping : exact-integer? -> exact-integer?
    (define/public (ping t)
      (set! q (append q (list t))) ; add new timestamp
      (let* ((low (- t 3000))
             (new-q (filter (lambda (x) (>= x low)) q)))
        (set! q new-q)
        (length q)))))
```

## Erlang

```erlang
-module(solution).
-export([recent_counter_init_/0, recent_counter_ping/1]).

-spec recent_counter_init_() -> any().
recent_counter_init_() ->
    case whereis(recent_counter_server) of
        undefined -> ok;
        Pid -> exit(Pid, kill), unregister(recent_counter_server)
    end,
    Pid = spawn(fun() -> loop(queue:new()) end),
    register(recent_counter_server, Pid),
    ok.

-spec recent_counter_ping(T :: integer()) -> integer().
recent_counter_ping(T) ->
    recent_counter_server ! {ping, T, self()},
    receive
        {reply, Count} -> Count
    after 5000 ->
        erlang:error(timeout)
    end.

%% internal server loop
loop(Q) ->
    receive
        {ping, T, From} ->
            Q1 = queue:in(T, Q),
            Q2 = clean(Q1, T),
            Count = queue:len(Q2),
            From ! {reply, Count},
            loop(Q2);
        stop ->
            ok
    end.

clean(Q, T) ->
    case queue:peek(Q) of
        empty -> Q;
        {value, V} when V < T - 3000 ->
            {_Val, Q1} = queue:out(Q),
            clean(Q1, T);
        _ -> Q
    end.
```

## Elixir

```elixir
defmodule RecentCounter do
  @spec init_() :: any
  def init_() do
    Process.put(:rc_queue, :queue.new())
  end

  @spec ping(t :: integer) :: integer
  def ping(t) do
    q = Process.get(:rc_queue)
    q = :queue.in(t, q)
    q = trim(q, t - 3000)
    Process.put(:rc_queue, q)
    :queue.len(q)
  end

  defp trim(queue, min_time) do
    case :queue.out(queue) do
      {:empty, _} ->
        queue

      {{:value, v}, rest} ->
        if v < min_time do
          trim(rest, min_time)
        else
          :queue.in_r(v, rest)
        end
    end
  end
end
```

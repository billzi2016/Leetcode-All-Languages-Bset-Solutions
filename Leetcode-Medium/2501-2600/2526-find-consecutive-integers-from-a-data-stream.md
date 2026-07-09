# 2526. Find Consecutive Integers from a Data Stream

## Cpp

```cpp
class DataStream {
private:
    int target;
    int k;
    int index = 0;          // number of elements processed (1-indexed)
    int lastBad = 0;        // position of most recent element not equal to target (0 means before stream starts)

public:
    DataStream(int value, int k) : target(value), k(k) {}

    bool consec(int num) {
        ++index;
        if (num != target) {
            lastBad = index;
        }
        return index >= k && (index - lastBad) >= k;
    }
};

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream* obj = new DataStream(value, k);
 * bool param_1 = obj->consec(num);
 */
```

## Java

```java
class DataStream {
    private final int value;
    private final int k;
    private int consecutiveCount;

    public DataStream(int value, int k) {
        this.value = value;
        this.k = k;
        this.consecutiveCount = 0;
    }

    public boolean consec(int num) {
        if (num == value) {
            consecutiveCount++;
        } else {
            consecutiveCount = 0;
        }
        return consecutiveCount >= k;
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream obj = new DataStream(value, k);
 * boolean param_1 = obj.consec(num);
 */
```

## Python

```python
import collections

class DataStream(object):
    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k
        self.q = collections.deque()
        self.cnt = 0

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        flag = 1 if num == self.value else 0
        self.q.append(flag)
        self.cnt += flag
        if len(self.q) > self.k:
            left = self.q.popleft()
            self.cnt -= left
        return len(self.q) == self.k and self.cnt == self.k
```

## Python3

```python
class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.consecutive = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.consecutive = min(self.consecutive + 1, self.k)
        else:
            self.consecutive = 0
        return self.consecutive == self.k
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int value;
    int k;
    int *buf;            // circular buffer storing 0 (equal) or 1 (not equal)
    int head;            // next position to write
    int size;            // number of elements currently in buffer (max k)
    int notEqualCount;   // count of entries != value in current window
} DataStream;

DataStream* dataStreamCreate(int value, int k) {
    DataStream *obj = (DataStream*)malloc(sizeof(DataStream));
    obj->value = value;
    obj->k = k;
    obj->buf = (int*)calloc(k, sizeof(int)); // initialized to 0
    obj->head = 0;
    obj->size = 0;
    obj->notEqualCount = 0;
    return obj;
}

bool dataStreamConsec(DataStream* obj, int num) {
    int isNot = (num != obj->value) ? 1 : 0;

    if (obj->size < obj->k) {
        // window not full yet
        obj->buf[obj->head] = isNot;
        obj->notEqualCount += isNot;
        obj->head = (obj->head + 1) % obj->k;
        obj->size++;
    } else {
        // remove oldest element at head position, then insert new one
        int old = obj->buf[obj->head];
        obj->notEqualCount -= old;

        obj->buf[obj->head] = isNot;
        obj->notEqualCount += isNot;
        obj->head = (obj->head + 1) % obj->k;
    }

    return (obj->size == obj->k && obj->notEqualCount == 0);
}

void dataStreamFree(DataStream* obj) {
    if (!obj) return;
    free(obj->buf);
    free(obj);
}

/**
 * Your DataStream struct will be instantiated and called as such:
 * DataStream* obj = dataStreamCreate(value, k);
 * bool param_1 = dataStreamConsec(obj, num);
 * 
 * dataStreamFree(obj);
 */
```

## Csharp

```csharp
public class DataStream
{
    private readonly int _value;
    private readonly int _k;
    private readonly int[] _buffer;
    private int _pos;
    private int _countValue;
    private int _total;

    public DataStream(int value, int k)
    {
        _value = value;
        _k = k;
        _buffer = new int[k];
        _pos = 0;
        _countValue = 0;
        _total = 0;
    }

    public bool Consec(int num)
    {
        if (_total >= _k)
        {
            int old = _buffer[_pos];
            if (old == _value) _countValue--;
        }

        _buffer[_pos] = num;
        if (num == _value) _countValue++;

        _pos++;
        if (_pos == _k) _pos = 0;

        _total++;

        return _total >= _k && _countValue == _k;
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream obj = new DataStream(value, k);
 * bool param_1 = obj.Consec(num);
 */
```

## Javascript

```javascript
/**
 * @param {number} value
 * @param {number} k
 */
var DataStream = function(value, k) {
    this.value = value;
    this.k = k;
    this.buffer = new Array(k);
    this.head = 0;   // points to the oldest element when buffer is full
    this.size = 0;   // current number of stored elements (max k)
    this.count = 0;  // how many of the stored elements equal `value`
};

/** 
 * @param {number} num
 * @return {boolean}
 */
DataStream.prototype.consec = function(num) {
    const isVal = num === this.value ? 1 : 0;
    if (this.size < this.k) {
        // buffer not full yet, append at tail
        this.buffer[(this.head + this.size) % this.k] = isVal;
        this.size++;
        this.count += isVal;
    } else {
        // overwrite the oldest element
        const old = this.buffer[this.head];
        this.count -= old;
        this.buffer[this.head] = isVal;
        this.count += isVal;
        this.head = (this.head + 1) % this.k;
    }
    return this.size === this.k && this.count === this.k;
};
```

## Typescript

```typescript
class DataStream {
    private readonly target: number;
    private readonly k: number;
    private idx: number = 0;          // index of the next incoming element
    private lastBadIdx: number = -1;   // most recent index where num !== target

    constructor(value: number, k: number) {
        this.target = value;
        this.k = k;
    }

    consec(num: number): boolean {
        if (num !== this.target) {
            this.lastBadIdx = this.idx;
        }
        const enoughElements = this.idx + 1 >= this.k;
        const windowClean = this.idx - this.k + 1 > this.lastBadIdx;
        this.idx++;
        return enoughElements && windowClean;
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * var obj = new DataStream(value, k)
 * var param_1 = obj.consec(num)
 */
```

## Php

```php
class DataStream {
    private int $value;
    private int $k;
    private SplQueue $queue;
    private int $matchCount;

    /**
     * @param Integer $value
     * @param Integer $k
     */
    function __construct($value, $k) {
        $this->value = $value;
        $this->k = $k;
        $this->queue = new SplQueue();
        $this->matchCount = 0;
    }

    /**
     * @param Integer $num
     * @return Boolean
     */
    function consec($num) {
        $isMatch = ($num == $this->value);
        $this->queue->enqueue($isMatch);
        if ($isMatch) {
            $this->matchCount++;
        }
        if ($this->queue->count() > $this->k) {
            $old = $this->queue->dequeue();
            if ($old) {
                $this->matchCount--;
            }
        }
        return $this->queue->count() == $this->k && $this->matchCount == $this->k;
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * $obj = new DataStream($value, $k);
 * $ret_1 = $obj->consec($num);
 */
```

## Swift

```swift
class DataStream {
    private let value: Int
    private let k: Int
    private var buffer: [Int]
    private var idx: Int = 0
    private var total: Int = 0
    private var equalCount: Int = 0

    init(_ value: Int, _ k: Int) {
        self.value = value
        self.k = k
        self.buffer = [Int](repeating: 0, count: k)
    }

    func consec(_ num: Int) -> Bool {
        let isEqual = (num == value) ? 1 : 0
        if total < k {
            equalCount += isEqual
            buffer[idx] = isEqual
            idx += 1
            if idx == k { idx = 0 }
            total += 1
        } else {
            let old = buffer[idx]
            if old == 1 { equalCount -= 1 }
            equalCount += isEqual
            buffer[idx] = isEqual
            idx += 1
            if idx == k { idx = 0 }
            total += 1
        }
        return total >= k && equalCount == k
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * let obj = DataStream(value, k)
 * let ret_1: Bool = obj.consec(num)
 */
```

## Kotlin

```kotlin
class DataStream(private val value: Int, private val k: Int) {
    private val buffer = IntArray(k)
    private var idx = 0          // position to overwrite next
    private var size = 0         // current number of elements stored (max k)
    private var countValue = 0   // how many of the stored elements equal `value`

    fun consec(num: Int): Boolean {
        if (size == k) {
            // buffer is full, remove the element that will be overwritten
            val old = buffer[idx]
            if (old == value) countValue--
        } else {
            size++
        }
        buffer[idx] = num
        if (num == value) countValue++
        idx = (idx + 1) % k
        return size == k && countValue == k
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * var obj = DataStream(value, k)
 * var param_1 = obj.consec(num)
 */
```

## Dart

```dart
import 'dart:collection';

class DataStream {
  final int _value;
  final int _k;
  final Queue<int> _queue = Queue<int>();
  int _cnt = 0;

  DataStream(int value, int k)
      : _value = value,
        _k = k;

  bool consec(int num) {
    if (num == _value) {
      _queue.addLast(1);
      _cnt++;
    } else {
      _queue.addLast(0);
    }
    if (_queue.length > _k) {
      int removed = _queue.removeFirst();
      if (removed == 1) _cnt--;
    }
    return _queue.length == _k && _cnt == _k;
  }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream obj = DataStream(value, k);
 * bool param1 = obj.consec(num);
 */
```

## Golang

```go
type DataStream struct {
	value int
	k     int
	buf   []bool
	idx   int
	cnt   int
	total int
}

func Constructor(value int, k int) DataStream {
	return DataStream{
		value: value,
		k:     k,
		buf:   make([]bool, k),
	}
}

func (this *DataStream) Consec(num int) bool {
	isVal := num == this.value

	if this.total >= this.k {
		if this.buf[this.idx] {
			this.cnt--
		}
	}
	this.buf[this.idx] = isVal
	if isVal {
		this.cnt++
	}
	this.idx = (this.idx + 1) % this.k
	this.total++

	return this.total >= this.k && this.cnt == this.k
}
```

## Ruby

```ruby
class DataStream
  # :type value: Integer
  # :type k: Integer
  def initialize(value, k)
    @value = value
    @k = k
    @streak = 0   # consecutive count of @value ending at the latest number
    @total = 0    # total numbers processed so far
  end

  # :type num: Integer
  # :rtype: Boolean
  def consec(num)
    @total += 1
    if num == @value
      @streak += 1
    else
      @streak = 0
    end
    @streak >= @k && @total >= @k
  end
end
```

## Scala

```scala
import java.util.ArrayDeque

class DataStream(_value: Int, _k: Int) {
  private val value = _value
  private val k = _k
  private val deque = new ArrayDeque[Boolean]()
  private var count = 0

  def consec(num: Int): Boolean = {
    val isVal = num == value
    deque.addLast(isVal)
    if (isVal) count += 1
    if (deque.size() > k) {
      val removed = deque.removeFirst()
      if (removed) count -= 1
    }
    deque.size() == k && count == k
  }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * val obj = new DataStream(value, k)
 * val param_1 = obj.consec(num)
 */
```

## Rust

```rust
use std::collections::VecDeque;

struct DataStream {
    value: i32,
    k: usize,
    window: VecDeque<bool>, // true if element != value
    not_eq_cnt: usize,
}

impl DataStream {
    fn new(value: i32, k: i32) -> Self {
        DataStream {
            value,
            k: k as usize,
            window: VecDeque::new(),
            not_eq_cnt: 0,
        }
    }

    fn consec(&mut self, num: i32) -> bool {
        let is_not_eq = num != self.value;
        if is_not_eq {
            self.not_eq_cnt += 1;
        }
        self.window.push_back(is_not_eq);
        if self.window.len() > self.k {
            if let Some(front) = self.window.pop_front() {
                if front {
                    self.not_eq_cnt -= 1;
                }
            }
        }
        self.window.len() == self.k && self.not_eq_cnt == 0
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * let mut obj = DataStream::new(value, k);
 * let ret_1: bool = obj.consec(num);
 */
```

## Racket

```racket
(define data-stream%
  (class object%
    (super-new)
    (init-field value k)
    (define idx 0)
    (define last-bad 0)
    (define/public (consec num)
      (set! idx (+ idx 1))
      (when (not (= num value))
        (set! last-bad idx))
      (>= (- idx last-bad) k))))
```

## Erlang

```erlang
-module(data_stream).
-export([data_stream_init_/2, data_stream_consec/1]).

-spec data_stream_init_(Value :: integer(), K :: integer()) -> any().
data_stream_init_(Value, K) ->
    put(data_stream_state, #{value => Value, k => K, streak => 0}),
    ok.

-spec data_stream_consec(Num :: integer()) -> boolean().
data_stream_consec(Num) ->
    State = get(data_stream_state),
    Value = maps:get(value, State),
    K = maps:get(k, State),
    StreakPrev = maps:get(streak, State),
    NewStreak = if Num == Value -> StreakPrev + 1; true -> 0 end,
    put(data_stream_state, State#{streak => NewStreak}),
    NewStreak >= K.
```

## Elixir

```elixir
defmodule DataStream do
  @spec init_(value :: integer, k :: integer) :: any
  def init_(value, k) do
    state = %{
      value: value,
      k: k,
      q: :queue.new(),
      sz: 0,
      not_eq_cnt: 0
    }

    Process.put(:ds_state, state)
  end

  @spec consec(num :: integer) :: boolean
  def consec(num) do
    state = Process.get(:ds_state)

    v = state.value
    k = state.k
    q = state.q
    sz = state.sz
    cnt = state.not_eq_cnt

    # add new number
    q1 = :queue.in(num, q)
    sz1 = sz + 1
    cnt1 = if num != v, do: cnt + 1, else: cnt

    # remove oldest if window exceeds k
    {q2, sz2, cnt2} =
      if sz1 > k do
        {{:value, removed}, q_rest} = :queue.out(q1)
        sz_tmp = sz1 - 1
        cnt_tmp = if removed != v, do: cnt1 - 1, else: cnt1
        {q_rest, sz_tmp, cnt_tmp}
      else
        {q1, sz1, cnt1}
      end

    result = (sz2 == k) and (cnt2 == 0)

    Process.put(:ds_state, %{
      value: v,
      k: k,
      q: q2,
      sz: sz2,
      not_eq_cnt: cnt2
    })

    result
  end
end
```

# 0622. Design Circular Queue

## Cpp

```cpp
class MyCircularQueue {
private:
    std::vector<int> data;
    int capacity;
    int frontIdx;
    int rearIdx;
    int count;
public:
    MyCircularQueue(int k) : data(k), capacity(k), frontIdx(0), rearIdx(-1), count(0) {}
    
    bool enQueue(int value) {
        if (isFull()) return false;
        rearIdx = (rearIdx + 1) % capacity;
        data[rearIdx] = value;
        ++count;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;
        frontIdx = (frontIdx + 1) % capacity;
        --count;
        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return data[frontIdx];
    }
    
    int Rear() {
        if (isEmpty()) return -1;
        return data[rearIdx];
    }
    
    bool isEmpty() {
        return count == 0;
    }
    
    bool isFull() {
        return count == capacity;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
```

## Java

```java
class MyCircularQueue {
    private final int[] data;
    private int front;
    private int rear;
    private int size;
    private final int capacity;

    public MyCircularQueue(int k) {
        this.capacity = k;
        this.data = new int[k];
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    public boolean enQueue(int value) {
        if (size == capacity) return false;
        rear = (rear + 1) % capacity;
        data[rear] = value;
        size++;
        return true;
    }

    public boolean deQueue() {
        if (size == 0) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }

    public int Front() {
        if (size == 0) return -1;
        return data[front];
    }

    public int Rear() {
        if (size == 0) return -1;
        return data[rear];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
```

## Python

```python
class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k
        self.queue = [0] * k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.capacity
```

## Python3

```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *data;
    int head;
    int tail;
    int size;
    int capacity;
} MyCircularQueue;

MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue* obj = (MyCircularQueue*)malloc(sizeof(MyCircularQueue));
    if (!obj) return NULL;
    obj->data = (int*)malloc(k * sizeof(int));
    obj->capacity = k;
    obj->size = 0;
    obj->head = 0;
    obj->tail = -1;
    return obj;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if (!obj || obj->size == obj->capacity) return false;
    obj->tail = (obj->tail + 1) % obj->capacity;
    obj->data[obj->tail] = value;
    obj->size++;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if (!obj || obj->size == 0) return false;
    obj->head = (obj->head + 1) % obj->capacity;
    obj->size--;
    if (obj->size == 0) {
        // Reset tail to keep consistency, though not strictly necessary
        obj->tail = -1;
    }
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    if (!obj || obj->size == 0) return -1;
    return obj->data[obj->head];
}

int myCircularQueueRear(MyCircularQueue* obj) {
    if (!obj || obj->size == 0) return -1;
    return obj->data[obj->tail];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    if (!obj) return true;
    return obj->size == 0;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    if (!obj) return false;
    return obj->size == obj->capacity;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    if (!obj) return;
    free(obj->data);
    free(obj);
}
```

## Csharp

```csharp
public class MyCircularQueue
{
    private readonly int[] _data;
    private int _head;
    private int _tail;
    private int _size;
    private readonly int _capacity;

    public MyCircularQueue(int k)
    {
        _capacity = k;
        _data = new int[k];
        _head = 0;
        _tail = -1;
        _size = 0;
    }

    public bool EnQueue(int value)
    {
        if (IsFull())
            return false;
        _tail = (_tail + 1) % _capacity;
        _data[_tail] = value;
        _size++;
        return true;
    }

    public bool DeQueue()
    {
        if (IsEmpty())
            return false;
        _head = (_head + 1) % _capacity;
        _size--;
        return true;
    }

    public int Front()
    {
        return IsEmpty() ? -1 : _data[_head];
    }

    public int Rear()
    {
        return IsEmpty() ? -1 : _data[_tail];
    }

    public bool IsEmpty()
    {
        return _size == 0;
    }

    public bool IsFull()
    {
        return _size == _capacity;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 */
var MyCircularQueue = function(k) {
    this.capacity = k;
    this.buffer = new Array(k);
    this.head = 0;      // index of front element
    this.tail = -1;     // index of rear element
    this.size = 0;
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularQueue.prototype.enQueue = function(value) {
    if (this.isFull()) return false;
    this.tail = (this.tail + 1) % this.capacity;
    this.buffer[this.tail] = value;
    this.size++;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.deQueue = function() {
    if (this.isEmpty()) return false;
    // move head forward
    this.head = (this.head + 1) % this.capacity;
    this.size--;
    // reset tail when queue becomes empty to keep consistency
    if (this.size === 0) {
        this.tail = -1;
        this.head = 0;
    }
    return true;
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Front = function() {
    if (this.isEmpty()) return -1;
    return this.buffer[this.head];
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Rear = function() {
    if (this.isEmpty()) return -1;
    return this.buffer[this.tail];
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isEmpty = function() {
    return this.size === 0;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isFull = function() {
    return this.size === this.capacity;
};
```

## Typescript

```typescript
class MyCircularQueue {
    private data: number[];
    private head: number;
    private count: number;
    private capacity: number;

    constructor(k: number) {
        this.capacity = k;
        this.data = new Array<number>(k);
        this.head = 0;
        this.count = 0;
    }

    enQueue(value: number): boolean {
        if (this.isFull()) return false;
        const tailIdx = (this.head + this.count) % this.capacity;
        this.data[tailIdx] = value;
        this.count++;
        return true;
    }

    deQueue(): boolean {
        if (this.isEmpty()) return false;
        this.head = (this.head + 1) % this.capacity;
        this.count--;
        return true;
    }

    Front(): number {
        if (this.isEmpty()) return -1;
        return this.data[this.head];
    }

    Rear(): number {
        if (this.isEmpty()) return -1;
        const tailIdx = (this.head + this.count - 1 + this.capacity) % this.capacity;
        return this.data[tailIdx];
    }

    isEmpty(): boolean {
        return this.count === 0;
    }

    isFull(): boolean {
        return this.count === this.capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
```

## Php

```php
class MyCircularQueue {
    /**
     * @param Integer $k
     */
    private $queue;
    private $head = 0;
    private $tail = -1;
    private $size = 0;
    private $capacity;

    function __construct($k) {
        $this->capacity = $k;
        $this->queue = array_fill(0, $k, 0);
    }
  
    /**
     * @param Integer $value
     * @return Boolean
     */
    function enQueue($value) {
        if ($this->isFull()) {
            return false;
        }
        $this->tail = ($this->tail + 1) % $this->capacity;
        $this->queue[$this->tail] = $value;
        $this->size++;
        return true;
    }
  
    /**
     * @return Boolean
     */
    function deQueue() {
        if ($this->isEmpty()) {
            return false;
        }
        $this->head = ($this->head + 1) % $this->capacity;
        $this->size--;
        return true;
    }
  
    /**
     * @return Integer
     */
    function Front() {
        if ($this->isEmpty()) {
            return -1;
        }
        return $this->queue[$this->head];
    }
  
    /**
     * @return Integer
     */
    function Rear() {
        if ($this->isEmpty()) {
            return -1;
        }
        return $this->queue[$this->tail];
    }
  
    /**
     * @return Boolean
     */
    function isEmpty() {
        return $this->size == 0;
    }
  
    /**
     * @return Boolean
     */
    function isFull() {
        return $this->size == $this->capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * $obj = new MyCircularQueue($k);
 * $ret_1 = $obj->enQueue($value);
 * $ret_2 = $obj->deQueue();
 * $ret_3 = $obj->Front();
 * $ret_4 = $obj->Rear();
 * $ret_5 = $obj->isEmpty();
 * $ret_6 = $obj->isFull();
 */
```

## Swift

```swift
class MyCircularQueue {
    private var data: [Int]
    private var head: Int = 0
    private var size: Int = 0
    private let capacity: Int

    init(_ k: Int) {
        self.capacity = k
        self.data = Array(repeating: 0, count: k)
    }
    
    func enQueue(_ value: Int) -> Bool {
        if size == capacity { return false }
        let tail = (head + size) % capacity
        data[tail] = value
        size += 1
        return true
    }
    
    func deQueue() -> Bool {
        if size == 0 { return false }
        head = (head + 1) % capacity
        size -= 1
        return true
    }
    
    func Front() -> Int {
        if size == 0 { return -1 }
        return data[head]
    }
    
    func Rear() -> Int {
        if size == 0 { return -1 }
        let tail = (head + size - 1) % capacity
        return data[tail]
    }
    
    func isEmpty() -> Bool {
        return size == 0
    }
    
    func isFull() -> Bool {
        return size == capacity
    }
}
```

## Kotlin

```kotlin
class MyCircularQueue(k: Int) {

    private val capacity = k
    private val data = IntArray(k)
    private var head = 0
    private var tail = -1
    private var count = 0

    fun enQueue(value: Int): Boolean {
        if (count == capacity) return false
        tail = (tail + 1) % capacity
        data[tail] = value
        count++
        return true
    }

    fun deQueue(): Boolean {
        if (count == 0) return false
        head = (head + 1) % capacity
        count--
        return true
    }

    fun Front(): Int {
        return if (count == 0) -1 else data[head]
    }

    fun Rear(): Int {
        return if (count == 0) -1 else data[tail]
    }

    fun isEmpty(): Boolean {
        return count == 0
    }

    fun isFull(): Boolean {
        return count == capacity
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
```

## Dart

```dart
class MyCircularQueue {
  late List<int> _data;
  int _capacity;
  int _front = 0;
  int _rear = -1;
  int _size = 0;

  MyCircularQueue(int k) {
    _capacity = k;
    _data = List.filled(k, 0);
  }

  bool enQueue(int value) {
    if (_size == _capacity) return false;
    _rear = (_rear + 1) % _capacity;
    _data[_rear] = value;
    _size++;
    return true;
  }

  bool deQueue() {
    if (_size == 0) return false;
    _front = (_front + 1) % _capacity;
    _size--;
    if (_size == 0) {
      // reset pointers to initial state
      _front = 0;
      _rear = -1;
    }
    return true;
  }

  int Front() {
    if (_size == 0) return -1;
    return _data[_front];
  }

  int Rear() {
    if (_size == 0) return -1;
    return _data[_rear];
  }

  bool isEmpty() => _size == 0;

  bool isFull() => _size == _capacity;
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = MyCircularQueue(k);
 * bool param1 = obj.enQueue(value);
 * bool param2 = obj.deQueue();
 * int param3 = obj.Front();
 * int param4 = obj.Rear();
 * bool param5 = obj.isEmpty();
 * bool param6 = obj.isFull();
 */
```

## Golang

```go
type MyCircularQueue struct {
	data     []int
	head     int
	size     int
	capacity int
}

func Constructor(k int) MyCircularQueue {
	return MyCircularQueue{
		data:     make([]int, k),
		head:     0,
		size:     0,
		capacity: k,
	}
}

func (this *MyCircularQueue) EnQueue(value int) bool {
	if this.size == this.capacity {
		return false
	}
	idx := (this.head + this.size) % this.capacity
	this.data[idx] = value
	this.size++
	return true
}

func (this *MyCircularQueue) DeQueue() bool {
	if this.size == 0 {
		return false
	}
	this.head = (this.head + 1) % this.capacity
	this.size--
	return true
}

func (this *MyCircularQueue) Front() int {
	if this.size == 0 {
		return -1
	}
	return this.data[this.head]
}

func (this *MyCircularQueue) Rear() int {
	if this.size == 0 {
		return -1
	}
	idx := (this.head + this.size - 1) % this.capacity
	return this.data[idx]
}

func (this *MyCircularQueue) IsEmpty() bool {
	return this.size == 0
}

func (this *MyCircularQueue) IsFull() bool {
	return this.size == this.capacity
}
```

## Ruby

```ruby
class MyCircularQueue
  def initialize(k)
    @capacity = k
    @queue = Array.new(k)
    @head = 0
    @tail = -1
    @size = 0
  end

  def en_queue(value)
    return false if is_full
    @tail = (@tail + 1) % @capacity
    @queue[@tail] = value
    @size += 1
    true
  end

  def de_queue()
    return false if is_empty
    @head = (@head + 1) % @capacity
    @size -= 1
    true
  end

  def front()
    return -1 if is_empty
    @queue[@head]
  end

  def rear()
    return -1 if is_empty
    @queue[@tail]
  end

  def is_empty()
    @size == 0
  end

  def is_full()
    @size == @capacity
  end
end
```

## Scala

```scala
class MyCircularQueue(_k: Int) {
  private val capacity = _k
  private val data = new Array[Int](capacity)
  private var head = 0
  private var tail = 0
  private var count = 0

  def enQueue(value: Int): Boolean = {
    if (isFull()) return false
    data(tail) = value
    tail = (tail + 1) % capacity
    count += 1
    true
  }

  def deQueue(): Boolean = {
    if (isEmpty()) return false
    head = (head + 1) % capacity
    count -= 1
    true
  }

  def Front(): Int = {
    if (isEmpty()) -1 else data(head)
  }

  def Rear(): Int = {
    if (isEmpty()) -1 else data((tail - 1 + capacity) % capacity)
  }

  def isEmpty(): Boolean = count == 0

  def isFull(): Boolean = count == capacity
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * val obj = new MyCircularQueue(k)
 * val param_1 = obj.enQueue(value)
 * val param_2 = obj.deQueue()
 * val param_3 = obj.Front()
 * val param_4 = obj.Rear()
 * val param_5 = obj.isEmpty()
 * val param_6 = obj.isFull()
 */
```

## Rust

```rust
struct MyCircularQueue {
    data: Vec<i32>,
    capacity: usize,
    head: usize,
    tail: usize,
    size: usize,
}

impl MyCircularQueue {
    fn new(k: i32) -> Self {
        let cap = k as usize;
        MyCircularQueue {
            data: vec![0; cap],
            capacity: cap,
            head: 0,
            tail: 0,
            size: 0,
        }
    }

    fn en_queue(&mut self, value: i32) -> bool {
        if self.size == self.capacity {
            return false;
        }
        self.data[self.tail] = value;
        self.tail = (self.tail + 1) % self.capacity;
        self.size += 1;
        true
    }

    fn de_queue(&mut self) -> bool {
        if self.size == 0 {
            return false;
        }
        self.head = (self.head + 1) % self.capacity;
        self.size -= 1;
        true
    }

    fn front(&self) -> i32 {
        if self.size == 0 {
            -1
        } else {
            self.data[self.head]
        }
    }

    fn rear(&self) -> i32 {
        if self.size == 0 {
            -1
        } else {
            let idx = (self.tail + self.capacity - 1) % self.capacity;
            self.data[idx]
        }
    }

    fn is_empty(&self) -> bool {
        self.size == 0
    }

    fn is_full(&self) -> bool {
        self.size == self.capacity
    }
}
```

## Racket

```racket
(define my-circular-queue%
  (class object%
    (super-new)
    
    ; k : exact-integer?
    (init-field
      k)
    
    ; internal storage and pointers
    (define vec (make-vector k #f))
    (define head 0)   ; index of front element
    (define tail 0)   ; index where next enQueue will be placed
    (define cnt 0)    ; current number of elements
    
    ; en-queue : exact-integer? -> boolean?
    (define/public (en-queue value)
      (if (= cnt k)
          #f
          (begin
            (vector-set! vec tail value)
            (set! tail (modulo (+ tail 1) k))
            (set! cnt (+ cnt 1))
            #t)))
    
    ; de-queue : -> boolean?
    (define/public (de-queue)
      (if (= cnt 0)
          #f
          (begin
            (vector-set! vec head #f) ; optional clear
            (set! head (modulo (+ head 1) k))
            (set! cnt (- cnt 1))
            #t)))
    
    ; front : -> exact-integer?
    (define/public (front)
      (if (= cnt 0)
          -1
          (vector-ref vec head)))
    
    ; rear : -> exact-integer?
    (define/public (rear)
      (if (= cnt 0)
          -1
          (let ((idx (if (= tail 0) (- k 1) (- tail 1))))
            (vector-ref vec idx))))
    
    ; is-empty : -> boolean?
    (define/public (is-empty)
      (= cnt 0))
    
    ; is-full : -> boolean?
    (define/public (is-full)
      (= cnt k))))
```

## Erlang

```erlang
-spec my_circular_queue_init_(K :: integer()) -> any().
my_circular_queue_init_(K) ->
    put(capacity, K),
    put(count, 0),
    put(head, 0),
    put(tail, -1),
    put(data, erlang:make_tuple(K, 0)),
    ok.

-spec my_circular_queue_en_queue(Value :: integer()) -> boolean().
my_circular_queue_en_queue(Value) ->
    Count = get(count),
    Capacity = get(capacity),
    if
        Count == Capacity ->
            false;
        true ->
            Tail = get(tail),
            NewTail = (Tail + 1) rem Capacity,
            Data = get(data),
            NewData = setelement(NewTail + 1, Data, Value),
            put(data, NewData),
            put(tail, NewTail),
            case Count of
                0 -> put(head, NewTail);
                _ -> ok
            end,
            put(count, Count + 1),
            true
    end.

-spec my_circular_queue_de_queue() -> boolean().
my_circular_queue_de_queue() ->
    Count = get(count),
    if
        Count == 0 ->
            false;
        true ->
            Head = get(head),
            Capacity = get(capacity),
            NewHead = (Head + 1) rem Capacity,
            NewCount = Count - 1,
            put(count, NewCount),
            case NewCount of
                0 -> put(tail, -1);
                _ -> ok
            end,
            put(head, NewHead),
            true
    end.

-spec my_circular_queue_front() -> integer().
my_circular_queue_front() ->
    Count = get(count),
    if
        Count == 0 ->
            -1;
        true ->
            Head = get(head),
            Data = get(data),
            element(Head + 1, Data)
    end.

-spec my_circular_queue_rear() -> integer().
my_circular_queue_rear() ->
    Count = get(count),
    if
        Count == 0 ->
            -1;
        true ->
            Tail = get(tail),
            Data = get(data),
            element(Tail + 1, Data)
    end.

-spec my_circular_queue_is_empty() -> boolean().
my_circular_queue_is_empty() ->
    get(count) == 0.

-spec my_circular_queue_is_full() -> boolean().
my_circular_queue_is_full() ->
    get(count) == get(capacity).
```

## Elixir

```elixir
defmodule MyCircularQueue do
  @spec init_(k :: integer) :: any
  def init_(k) do
    state = %{
      capacity: k,
      size: 0,
      head: 0,
      tail: 0,
      data: :array.new(k)
    }

    Process.put(:my_circular_queue_state, state)
  end

  @spec en_queue(value :: integer) :: boolean
  def en_queue(value) do
    state = Process.get(:my_circular_queue_state)

    if state.size == state.capacity do
      false
    else
      new_data = :array.set(state.tail, value, state.data)
      new_tail = rem(state.tail + 1, state.capacity)
      new_state = %{
        state |
        data: new_data,
        tail: new_tail,
        size: state.size + 1
      }

      Process.put(:my_circular_queue_state, new_state)
      true
    end
  end

  @spec de_queue() :: boolean
  def de_queue() do
    state = Process.get(:my_circular_queue_state)

    if state.size == 0 do
      false
    else
      new_head = rem(state.head + 1, state.capacity)
      new_state = %{
        state |
        head: new_head,
        size: state.size - 1
      }

      Process.put(:my_circular_queue_state, new_state)
      true
    end
  end

  @spec front() :: integer
  def front() do
    state = Process.get(:my_circular_queue_state)

    if state.size == 0 do
      -1
    else
      :array.get(state.head, state.data)
    end
  end

  @spec rear() :: integer
  def rear() do
    state = Process.get(:my_circular_queue_state)

    if state.size == 0 do
      -1
    else
      idx = rem(state.tail - 1 + state.capacity, state.capacity)
      :array.get(idx, state.data)
    end
  end

  @spec is_empty() :: boolean
  def is_empty() do
    state = Process.get(:my_circular_queue_state)
    state.size == 0
  end

  @spec is_full() :: boolean
  def is_full() do
    state = Process.get(:my_circular_queue_state)
    state.size == state.capacity
  end
end
```

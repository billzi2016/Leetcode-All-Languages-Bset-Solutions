# 0641. Design Circular Deque

## Cpp

```cpp
class MyCircularDeque {
private:
    std::vector<int> data;
    int capacity;
    int sz;
    int frontIdx;
    int rearIdx;
public:
    MyCircularDeque(int k) : data(k), capacity(k), sz(0), frontIdx(0), rearIdx(k - 1) {}
    
    bool insertFront(int value) {
        if (isFull()) return false;
        frontIdx = (frontIdx - 1 + capacity) % capacity;
        data[frontIdx] = value;
        ++sz;
        return true;
    }
    
    bool insertLast(int value) {
        if (isFull()) return false;
        rearIdx = (rearIdx + 1) % capacity;
        data[rearIdx] = value;
        ++sz;
        return true;
    }
    
    bool deleteFront() {
        if (isEmpty()) return false;
        frontIdx = (frontIdx + 1) % capacity;
        --sz;
        return true;
    }
    
    bool deleteLast() {
        if (isEmpty()) return false;
        rearIdx = (rearIdx - 1 + capacity) % capacity;
        --sz;
        return true;
    }
    
    int getFront() {
        if (isEmpty()) return -1;
        return data[frontIdx];
    }
    
    int getRear() {
        if (isEmpty()) return -1;
        return data[rearIdx];
    }
    
    bool isEmpty() {
        return sz == 0;
    }
    
    bool isFull() {
        return sz == capacity;
    }
};
```

## Java

```java
class MyCircularDeque {
    private final int[] data;
    private int front;
    private int rear;
    private int size;
    private final int capacity;

    public MyCircularDeque(int k) {
        this.capacity = k;
        this.data = new int[k];
        this.front = 0;
        this.rear = k - 1;
        this.size = 0;
    }

    public boolean insertFront(int value) {
        if (isFull()) return false;
        front = (front - 1 + capacity) % capacity;
        data[front] = value;
        size++;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) return false;
        rear = (rear + 1) % capacity;
        data[rear] = value;
        size++;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) return false;
        rear = (rear - 1 + capacity) % capacity;
        size--;
        return true;
    }

    public int getFront() {
        if (isEmpty()) return -1;
        return data[front];
    }

    public int getRear() {
        if (isEmpty()) return -1;
        return data[rear];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }
}
```

## Python

```python
class MyCircularDeque(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k
        self.buf = [0] * k
        self.size = 0
        self.front = 0
        self.rear = k - 1

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.buf[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.buf[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.buf[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.buf[self.rear]

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
class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k
        self.buf = [0] * k
        self.size = 0
        self.front = 0
        self.rear = k - 1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity
        self.buf[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.buf[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.buf[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.buf[self.rear]

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
    int capacity;
    int size;
    int front;
    int rear;
} MyCircularDeque;

MyCircularDeque* myCircularDequeCreate(int k) {
    MyCircularDeque* obj = (MyCircularDeque*)malloc(sizeof(MyCircularDeque));
    if (!obj) return NULL;
    obj->capacity = k;
    obj->size = 0;
    obj->data = (int*)malloc(k * sizeof(int));
    obj->front = 0;
    obj->rear = k - 1; // will be adjusted on first insert
    return obj;
}

bool myCircularDequeInsertFront(MyCircularDeque* obj, int value) {
    if (!obj || obj->size == obj->capacity) return false;
    obj->front = (obj->front - 1 + obj->capacity) % obj->capacity;
    obj->data[obj->front] = value;
    obj->size++;
    return true;
}

bool myCircularDequeInsertLast(MyCircularDeque* obj, int value) {
    if (!obj || obj->size == obj->capacity) return false;
    obj->rear = (obj->rear + 1) % obj->capacity;
    obj->data[obj->rear] = value;
    obj->size++;
    return true;
}

bool myCircularDequeDeleteFront(MyCircularDeque* obj) {
    if (!obj || obj->size == 0) return false;
    obj->front = (obj->front + 1) % obj->capacity;
    obj->size--;
    return true;
}

bool myCircularDequeDeleteLast(MyCircularDeque* obj) {
    if (!obj || obj->size == 0) return false;
    obj->rear = (obj->rear - 1 + obj->capacity) % obj->capacity;
    obj->size--;
    return true;
}

int myCircularDequeGetFront(MyCircularDeque* obj) {
    if (!obj || obj->size == 0) return -1;
    return obj->data[obj->front];
}

int myCircularDequeGetRear(MyCircularDeque* obj) {
    if (!obj || obj->size == 0) return -1;
    return obj->data[obj->rear];
}

bool myCircularDequeIsEmpty(MyCircularDeque* obj) {
    if (!obj) return true;
    return obj->size == 0;
}

bool myCircularDequeIsFull(MyCircularDeque* obj) {
    if (!obj) return false;
    return obj->size == obj->capacity;
}

void myCircularDequeFree(MyCircularDeque* obj) {
    if (!obj) return;
    free(obj->data);
    free(obj);
}
```

## Csharp

```csharp
public class MyCircularDeque
{
    private readonly int[] _data;
    private readonly int _capacity;
    private int _front;
    private int _rear;
    private int _size;

    public MyCircularDeque(int k)
    {
        _capacity = k;
        _data = new int[k];
        _front = 0;
        _rear = k - 1;
        _size = 0;
    }

    public bool InsertFront(int value)
    {
        if (IsFull()) return false;
        _front = (_front - 1 + _capacity) % _capacity;
        _data[_front] = value;
        _size++;
        return true;
    }

    public bool InsertLast(int value)
    {
        if (IsFull()) return false;
        _rear = (_rear + 1) % _capacity;
        _data[_rear] = value;
        _size++;
        return true;
    }

    public bool DeleteFront()
    {
        if (IsEmpty()) return false;
        _front = (_front + 1) % _capacity;
        _size--;
        return true;
    }

    public bool DeleteLast()
    {
        if (IsEmpty()) return false;
        _rear = (_rear - 1 + _capacity) % _capacity;
        _size--;
        return true;
    }

    public int GetFront()
    {
        return IsEmpty() ? -1 : _data[_front];
    }

    public int GetRear()
    {
        return IsEmpty() ? -1 : _data[_rear];
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
var MyCircularDeque = function(k) {
    this.capacity = k;
    this.size = 0;
    this.arr = new Array(k);
    this.front = 0;          // points to current front element
    this.rear = k - 1;       // points to current rear element
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertFront = function(value) {
    if (this.isFull()) return false;
    this.front = (this.front - 1 + this.capacity) % this.capacity;
    this.arr[this.front] = value;
    this.size++;
    return true;
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertLast = function(value) {
    if (this.isFull()) return false;
    this.rear = (this.rear + 1) % this.capacity;
    this.arr[this.rear] = value;
    this.size++;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteFront = function() {
    if (this.isEmpty()) return false;
    this.front = (this.front + 1) % this.capacity;
    this.size--;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteLast = function() {
    if (this.isEmpty()) return false;
    this.rear = (this.rear - 1 + this.capacity) % this.capacity;
    this.size--;
    return true;
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getFront = function() {
    if (this.isEmpty()) return -1;
    return this.arr[this.front];
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getRear = function() {
    if (this.isEmpty()) return -1;
    return this.arr[this.rear];
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isEmpty = function() {
    return this.size === 0;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isFull = function() {
    return this.size === this.capacity;
};
```

## Typescript

```typescript
class MyCircularDeque {
    private capacity: number;
    private arr: number[];
    private front: number;
    private rear: number;
    private size: number;

    constructor(k: number) {
        this.capacity = k;
        this.arr = new Array<number>(k);
        this.front = 0;
        this.rear = k - 1;
        this.size = 0;
    }

    insertFront(value: number): boolean {
        if (this.isFull()) return false;
        this.front = (this.front - 1 + this.capacity) % this.capacity;
        this.arr[this.front] = value;
        this.size++;
        return true;
    }

    insertLast(value: number): boolean {
        if (this.isFull()) return false;
        this.rear = (this.rear + 1) % this.capacity;
        this.arr[this.rear] = value;
        this.size++;
        return true;
    }

    deleteFront(): boolean {
        if (this.isEmpty()) return false;
        this.front = (this.front + 1) % this.capacity;
        this.size--;
        return true;
    }

    deleteLast(): boolean {
        if (this.isEmpty()) return false;
        this.rear = (this.rear - 1 + this.capacity) % this.capacity;
        this.size--;
        return true;
    }

    getFront(): number {
        if (this.isEmpty()) return -1;
        return this.arr[this.front];
    }

    getRear(): number {
        if (this.isEmpty()) return -1;
        return this.arr[this.rear];
    }

    isEmpty(): boolean {
        return this.size === 0;
    }

    isFull(): boolean {
        return this.size === this.capacity;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */
```

## Php

```php
class MyCircularDeque {
    private $capacity;
    private $size = 0;
    private $front = 0;
    private $rear;
    private $data = [];

    /**
     * @param Integer $k
     */
    function __construct($k) {
        $this->capacity = $k;
        $this->rear = $k - 1;
        // Pre-allocate array for performance (optional)
        $this->data = array_fill(0, $k, null);
    }

    /**
     * @param Integer $value
     * @return Boolean
     */
    function insertFront($value) {
        if ($this->isFull()) {
            return false;
        }
        $this->front = ($this->front - 1 + $this->capacity) % $this->capacity;
        $this->data[$this->front] = $value;
        $this->size++;
        return true;
    }

    /**
     * @param Integer $value
     * @return Boolean
     */
    function insertLast($value) {
        if ($this->isFull()) {
            return false;
        }
        $this->rear = ($this->rear + 1) % $this->capacity;
        $this->data[$this->rear] = $value;
        $this->size++;
        return true;
    }

    /**
     * @return Boolean
     */
    function deleteFront() {
        if ($this->isEmpty()) {
            return false;
        }
        $this->front = ($this->front + 1) % $this->capacity;
        $this->size--;
        return true;
    }

    /**
     * @return Boolean
     */
    function deleteLast() {
        if ($this->isEmpty()) {
            return false;
        }
        $this->rear = ($this->rear - 1 + $this->capacity) % $this->capacity;
        $this->size--;
        return true;
    }

    /**
     * @return Integer
     */
    function getFront() {
        if ($this->isEmpty()) {
            return -1;
        }
        return $this->data[$this->front];
    }

    /**
     * @return Integer
     */
    function getRear() {
        if ($this->isEmpty()) {
            return -1;
        }
        return $this->data[$this->rear];
    }

    /**
     * @return Boolean
     */
    function isEmpty() {
        return $this->size === 0;
    }

    /**
     * @return Boolean
     */
    function isFull() {
        return $this->size === $this->capacity;
    }
}
```

## Swift

```swift
class MyCircularDeque {
    private var capacity: Int
    private var size: Int = 0
    private var front: Int = 0
    private var rear: Int = 0
    private var data: [Int]

    init(_ k: Int) {
        self.capacity = k
        self.data = Array(repeating: 0, count: k)
        self.front = 0
        self.rear = k - 1
    }

    func insertFront(_ value: Int) -> Bool {
        if isFull() { return false }
        front = (front - 1 + capacity) % capacity
        data[front] = value
        size += 1
        return true
    }

    func insertLast(_ value: Int) -> Bool {
        if isFull() { return false }
        rear = (rear + 1) % capacity
        data[rear] = value
        size += 1
        return true
    }

    func deleteFront() -> Bool {
        if isEmpty() { return false }
        front = (front + 1) % capacity
        size -= 1
        return true
    }

    func deleteLast() -> Bool {
        if isEmpty() { return false }
        rear = (rear - 1 + capacity) % capacity
        size -= 1
        return true
    }

    func getFront() -> Int {
        return isEmpty() ? -1 : data[front]
    }

    func getRear() -> Int {
        return isEmpty() ? -1 : data[rear]
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
class MyCircularDeque(k: Int) {
    private val capacity = k
    private val data = IntArray(k)
    private var size = 0
    private var front = 0
    private var rear = if (k == 0) -1 else k - 1

    fun insertFront(value: Int): Boolean {
        if (isFull()) return false
        front = (front - 1 + capacity) % capacity
        data[front] = value
        size++
        return true
    }

    fun insertLast(value: Int): Boolean {
        if (isFull()) return false
        rear = (rear + 1) % capacity
        data[rear] = value
        size++
        return true
    }

    fun deleteFront(): Boolean {
        if (isEmpty()) return false
        front = (front + 1) % capacity
        size--
        return true
    }

    fun deleteLast(): Boolean {
        if (isEmpty()) return false
        rear = (rear - 1 + capacity) % capacity
        size--
        return true
    }

    fun getFront(): Int {
        return if (isEmpty()) -1 else data[front]
    }

    fun getRear(): Int {
        return if (isEmpty()) -1 else data[rear]
    }

    fun isEmpty(): Boolean {
        return size == 0
    }

    fun isFull(): Boolean {
        return size == capacity
    }
}
```

## Dart

```dart
class MyCircularDeque {
  late List<int> _data;
  late int _capacity;
  int _size = 0;
  int _front = 0;
  int _rear = 0;

  MyCircularDeque(int k) {
    _capacity = k;
    _data = List.filled(k, 0);
    _front = 0;
    _rear = k - 1;
  }

  bool insertFront(int value) {
    if (isFull()) return false;
    _front = (_front - 1 + _capacity) % _capacity;
    _data[_front] = value;
    _size++;
    return true;
  }

  bool insertLast(int value) {
    if (isFull()) return false;
    _rear = (_rear + 1) % _capacity;
    _data[_rear] = value;
    _size++;
    return true;
  }

  bool deleteFront() {
    if (isEmpty()) return false;
    _front = (_front + 1) % _capacity;
    _size--;
    return true;
  }

  bool deleteLast() {
    if (isEmpty()) return false;
    _rear = (_rear - 1 + _capacity) % _capacity;
    _size--;
    return true;
  }

  int getFront() {
    if (isEmpty()) return -1;
    return _data[_front];
  }

  int getRear() {
    if (isEmpty()) return -1;
    return _data[_rear];
  }

  bool isEmpty() => _size == 0;

  bool isFull() => _size == _capacity;
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = MyCircularDeque(k);
 * bool param1 = obj.insertFront(value);
 * bool param2 = obj.insertLast(value);
 * bool param3 = obj.deleteFront();
 * bool param4 = obj.deleteLast();
 * int param5 = obj.getFront();
 * int param6 = obj.getRear();
 * bool param7 = obj.isEmpty();
 * bool param8 = obj.isFull();
 */
```

## Golang

```go
type MyCircularDeque struct {
	data     []int
	capacity int
	size     int
	front    int
	rear     int
}

func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{
		data:     make([]int, k),
		capacity: k,
		size:     0,
		front:    0,
		rear:     k - 1,
	}
}

func (this *MyCircularDeque) InsertFront(value int) bool {
	if this.IsFull() {
		return false
	}
	this.front = (this.front - 1 + this.capacity) % this.capacity
	this.data[this.front] = value
	this.size++
	return true
}

func (this *MyCircularDeque) InsertLast(value int) bool {
	if this.IsFull() {
		return false
	}
	this.rear = (this.rear + 1) % this.capacity
	this.data[this.rear] = value
	this.size++
	return true
}

func (this *MyCircularDeque) DeleteFront() bool {
	if this.IsEmpty() {
		return false
	}
	this.front = (this.front + 1) % this.capacity
	this.size--
	return true
}

func (this *MyCircularDeque) DeleteLast() bool {
	if this.IsEmpty() {
		return false
	}
	this.rear = (this.rear - 1 + this.capacity) % this.capacity
	this.size--
	return true
}

func (this *MyCircularDeque) GetFront() int {
	if this.IsEmpty() {
		return -1
	}
	return this.data[this.front]
}

func (this *MyCircularDeque) GetRear() int {
	if this.IsEmpty() {
		return -1
	}
	return this.data[this.rear]
}

func (this *MyCircularDeque) IsEmpty() bool {
	return this.size == 0
}

func (this *MyCircularDeque) IsFull() bool {
	return this.size == this.capacity
}
```

## Ruby

```ruby
class MyCircularDeque
  def initialize(k)
    @capacity = k
    @arr = Array.new(k)
    @size = 0
    @front = 0
    @rear = k - 1
  end

  def insert_front(value)
    return false if is_full
    @front = (@front - 1) % @capacity
    @arr[@front] = value
    @size += 1
    true
  end

  def insert_last(value)
    return false if is_full
    @rear = (@rear + 1) % @capacity
    @arr[@rear] = value
    @size += 1
    true
  end

  def delete_front()
    return false if is_empty
    @front = (@front + 1) % @capacity
    @size -= 1
    true
  end

  def delete_last()
    return false if is_empty
    @rear = (@rear - 1) % @capacity
    @size -= 1
    true
  end

  def get_front()
    return -1 if is_empty
    @arr[@front]
  end

  def get_rear()
    return -1 if is_empty
    @arr[@rear]
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
class MyCircularDeque(_k: Int) {

  private val capacity: Int = _k
  private val data: Array[Int] = new Array[Int](capacity)
  private var front: Int = 0
  private var rear: Int = capacity - 1
  private var size: Int = 0

  def insertFront(value: Int): Boolean = {
    if (isFull()) return false
    front = (front - 1 + capacity) % capacity
    data(front) = value
    size += 1
    true
  }

  def insertLast(value: Int): Boolean = {
    if (isFull()) return false
    rear = (rear + 1) % capacity
    data(rear) = value
    size += 1
    true
  }

  def deleteFront(): Boolean = {
    if (isEmpty()) return false
    front = (front + 1) % capacity
    size -= 1
    true
  }

  def deleteLast(): Boolean = {
    if (isEmpty()) return false
    rear = (rear - 1 + capacity) % capacity
    size -= 1
    true
  }

  def getFront(): Int = {
    if (isEmpty()) -1 else data(front)
  }

  def getRear(): Int = {
    if (isEmpty()) -1 else data(rear)
  }

  def isEmpty(): Boolean = size == 0

  def isFull(): Boolean = size == capacity
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * val obj = new MyCircularDeque(k)
 * val param_1 = obj.insertFront(value)
 * val param_2 = obj.insertLast(value)
 * val param_3 = obj.deleteFront()
 * val param_4 = obj.deleteLast()
 * val param_5 = obj.getFront()
 * val param_6 = obj.getRear()
 * val param_7 = obj.isEmpty()
 * val param_8 = obj.isFull()
 */
```

## Rust

```rust
struct MyCircularDeque {
    data: Vec<i32>,
    front: usize,
    rear: usize,
    size: usize,
    capacity: usize,
}

impl MyCircularDeque {
    fn new(k: i32) -> Self {
        let cap = k as usize;
        MyCircularDeque {
            data: vec![0; cap],
            front: 0,
            rear: if cap == 0 { 0 } else { cap - 1 },
            size: 0,
            capacity: cap,
        }
    }

    fn insert_front(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        self.front = (self.front + self.capacity - 1) % self.capacity;
        self.data[self.front] = value;
        self.size += 1;
        true
    }

    fn insert_last(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }
        self.rear = (self.rear + 1) % self.capacity;
        self.data[self.rear] = value;
        self.size += 1;
        true
    }

    fn delete_front(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.front = (self.front + 1) % self.capacity;
        self.size -= 1;
        true
    }

    fn delete_last(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }
        self.rear = (self.rear + self.capacity - 1) % self.capacity;
        self.size -= 1;
        true
    }

    fn get_front(&self) -> i32 {
        if self.is_empty() {
            -1
        } else {
            self.data[self.front]
        }
    }

    fn get_rear(&self) -> i32 {
        if self.is_empty() {
            -1
        } else {
            self.data[self.rear]
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
(define my-circular-deque%
  (class object%
    (init-field k)
    (super-new)

    (define capacity k)
    (define size 0)
    (define front 0)
    (define rear (- capacity 1))
    (define data (make-vector capacity -1))

    (define/public (insert-front value)
      (if (send this is-full)
          #f
          (begin
            (set! front (modulo (- front 1) capacity))
            (vector-set! data front value)
            (set! size (+ size 1))
            #t)))

    (define/public (insert-last value)
      (if (send this is-full)
          #f
          (begin
            (set! rear (modulo (+ rear 1) capacity))
            (vector-set! data rear value)
            (set! size (+ size 1))
            #t)))

    (define/public (delete-front)
      (if (send this is-empty)
          #f
          (begin
            (set! front (modulo (+ front 1) capacity))
            (set! size (- size 1))
            #t)))

    (define/public (delete-last)
      (if (send this is-empty)
          #f
          (begin
            (set! rear (modulo (- rear 1) capacity))
            (set! size (- size 1))
            #t)))

    (define/public (get-front)
      (if (send this is-empty)
          -1
          (vector-ref data front)))

    (define/public (get-rear)
      (if (send this is-empty)
          -1
          (vector-ref data rear)))

    (define/public (is-empty)
      (= size 0))

    (define/public (is-full)
      (= size capacity))))
```

## Erlang

```erlang
-spec my_circular_deque_init_(K :: integer()) -> any().
my_circular_deque_init_(K) ->
    Data = erlang:make_tuple(K, undefined),
    State = #{capacity => K,
              size => 0,
              front => 0,
              rear => K - 1,
              data => Data},
    put(deque_state, State).

-spec my_circular_deque_insert_front(Value :: integer()) -> boolean().
my_circular_deque_insert_front(Value) ->
    State = get(deque_state),
    case maps:get(size, State) == maps:get(capacity, State) of
        true -> false;
        false ->
            Cap = maps:get(capacity, State),
            Front0 = maps:get(front, State),
            NewFront = (Front0 - 1 + Cap) rem Cap,
            Data0 = maps:get(data, State),
            Data1 = setelement(NewFront + 1, Data0, Value),
            NewState = State#{front => NewFront,
                              size => maps:get(size, State) + 1,
                              data => Data1},
            put(deque_state, NewState),
            true
    end.

-spec my_circular_deque_insert_last(Value :: integer()) -> boolean().
my_circular_deque_insert_last(Value) ->
    State = get(deque_state),
    case maps:get(size, State) == maps:get(capacity, State) of
        true -> false;
        false ->
            Cap = maps:get(capacity, State),
            Rear0 = maps:get(rear, State),
            NewRear = (Rear0 + 1) rem Cap,
            Data0 = maps:get(data, State),
            Data1 = setelement(NewRear + 1, Data0, Value),
            NewState = State#{rear => NewRear,
                              size => maps:get(size, State) + 1,
                              data => Data1},
            put(deque_state, NewState),
            true
    end.

-spec my_circular_deque_delete_front() -> boolean().
my_circular_deque_delete_front() ->
    State = get(deque_state),
    case maps:get(size, State) == 0 of
        true -> false;
        false ->
            Cap = maps:get(capacity, State),
            Front0 = maps:get(front, State),
            NewFront = (Front0 + 1) rem Cap,
            NewState = State#{front => NewFront,
                              size => maps:get(size, State) - 1},
            put(deque_state, NewState),
            true
    end.

-spec my_circular_deque_delete_last() -> boolean().
my_circular_deque_delete_last() ->
    State = get(deque_state),
    case maps:get(size, State) == 0 of
        true -> false;
        false ->
            Cap = maps:get(capacity, State),
            Rear0 = maps:get(rear, State),
            NewRear = (Rear0 - 1 + Cap) rem Cap,
            NewState = State#{rear => NewRear,
                              size => maps:get(size, State) - 1},
            put(deque_state, NewState),
            true
    end.

-spec my_circular_deque_get_front() -> integer().
my_circular_deque_get_front() ->
    State = get(deque_state),
    case maps:get(size, State) == 0 of
        true -> -1;
        false ->
            Front = maps:get(front, State),
            Data = maps:get(data, State),
            element(Front + 1, Data)
    end.

-spec my_circular_deque_get_rear() -> integer().
my_circular_deque_get_rear() ->
    State = get(deque_state),
    case maps:get(size, State) == 0 of
        true -> -1;
        false ->
            Rear = maps:get(rear, State),
            Data = maps:get(data, State),
            element(Rear + 1, Data)
    end.

-spec my_circular_deque_is_empty() -> boolean().
my_circular_deque_is_empty() ->
    State = get(deque_state),
    maps:get(size, State) == 0.

-spec my_circular_deque_is_full() -> boolean().
my_circular_deque_is_full() ->
    State = get(deque_state),
    maps:get(size, State) == maps:get(capacity, State).
```

## Elixir

```elixir
defmodule MyCircularDeque do
  @spec init_(k :: integer) :: any
  def init_(k) do
    state = %{capacity: k, size: 0, front: 0, rear: -1, data: %{}}
    Process.put(:deque_state, state)
  end

  defp get_state do
    Process.get(:deque_state)
  end

  defp put_state(state) do
    Process.put(:deque_state, state)
  end

  @spec insert_front(value :: integer) :: boolean
  def insert_front(value) do
    s = get_state()
    if s.size == s.capacity do
      false
    else
      {new_front, new_rear} =
        if s.size == 0 do
          {0, 0}
        else
          {rem(s.front - 1 + s.capacity, s.capacity), s.rear}
        end

      data = Map.put(s.data, new_front, value)
      new_state = %{s | front: new_front, rear: new_rear, size: s.size + 1, data: data}
      put_state(new_state)
      true
    end
  end

  @spec insert_last(value :: integer) :: boolean
  def insert_last(value) do
    s = get_state()
    if s.size == s.capacity do
      false
    else
      {new_rear, new_front} =
        if s.size == 0 do
          {0, 0}
        else
          {rem(s.rear + 1, s.capacity), s.front}
        end

      data = Map.put(s.data, new_rear, value)
      new_state = %{s | rear: new_rear, front: new_front, size: s.size + 1, data: data}
      put_state(new_state)
      true
    end
  end

  @spec delete_front() :: boolean
  def delete_front() do
    s = get_state()
    if s.size == 0 do
      false
    else
      if s.size == 1 do
        new_state = %{s | size: 0, front: 0, rear: -1, data: %{}}
        put_state(new_state)
        true
      else
        new_front = rem(s.front + 1, s.capacity)
        data = Map.delete(s.data, s.front)
        new_state = %{s | front: new_front, size: s.size - 1, data: data}
        put_state(new_state)
        true
      end
    end
  end

  @spec delete_last() :: boolean
  def delete_last() do
    s = get_state()
    if s.size == 0 do
      false
    else
      if s.size == 1 do
        new_state = %{s | size: 0, front: 0, rear: -1, data: %{}}
        put_state(new_state)
        true
      else
        new_rear = rem(s.rear - 1 + s.capacity, s.capacity)
        data = Map.delete(s.data, s.rear)
        new_state = %{s | rear: new_rear, size: s.size - 1, data: data}
        put_state(new_state)
        true
      end
    end
  end

  @spec get_front() :: integer
  def get_front() do
    s = get_state()
    if s.size == 0 do
      -1
    else
      Map.get(s.data, s.front, -1)
    end
  end

  @spec get_rear() :: integer
  def get_rear() do
    s = get_state()
    if s.size == 0 do
      -1
    else
      Map.get(s.data, s.rear, -1)
    end
  end

  @spec is_empty() :: boolean
  def is_empty() do
    s = get_state()
    s.size == 0
  end

  @spec is_full() :: boolean
  def is_full() do
    s = get_state()
    s.size == s.capacity
  end
end
```

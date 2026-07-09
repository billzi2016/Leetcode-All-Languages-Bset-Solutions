# 1670. Design Front Middle Back Queue

## Cpp

```cpp
class FrontMiddleBackQueue {
public:
    FrontMiddleBackQueue() {}
    
    void pushFront(int val) {
        left.push_front(val);
        rebalance();
    }
    
    void pushMiddle(int val) {
        if (left.size() > right.size()) {
            right.push_front(val);
        } else {
            left.push_back(val);
        }
        rebalance();
    }
    
    void pushBack(int val) {
        right.push_back(val);
        rebalance();
    }
    
    int popFront() {
        if (empty()) return -1;
        int ans;
        if (!left.empty()) {
            ans = left.front();
            left.pop_front();
        } else {
            ans = right.front();
            right.pop_front();
        }
        rebalance();
        return ans;
    }
    
    int popMiddle() {
        if (empty()) return -1;
        int ans = left.back();
        left.pop_back();
        rebalance();
        return ans;
    }
    
    int popBack() {
        if (empty()) return -1;
        int ans;
        if (!right.empty()) {
            ans = right.back();
            right.pop_back();
        } else {
            ans = left.back();
            left.pop_back();
        }
        rebalance();
        return ans;
    }

private:
    std::deque<int> left, right;
    
    bool empty() const {
        return left.empty() && right.empty();
    }
    
    void rebalance() {
        if (left.size() > right.size() + 1) {
            right.push_front(left.back());
            left.pop_back();
        } else if (left.size() < right.size()) {
            left.push_back(right.front());
            right.pop_front();
        }
    }
};

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = new FrontMiddleBackQueue();
 * obj->pushFront(val);
 * obj->pushMiddle(val);
 * obj->pushBack(val);
 * int param_4 = obj->popFront();
 * int param_5 = obj->popMiddle();
 * int param_6 = obj->popBack();
 */
```

## Java

```java
class FrontMiddleBackQueue {
    private java.util.Deque<Integer> left;
    private java.util.Deque<Integer> right;

    public FrontMiddleBackQueue() {
        left = new java.util.ArrayDeque<>();
        right = new java.util.ArrayDeque<>();
    }

    public void pushFront(int val) {
        left.addFirst(val);
        balance();
    }

    public void pushMiddle(int val) {
        left.addLast(val);
        balance();
    }

    public void pushBack(int val) {
        right.addLast(val);
        balance();
    }

    public int popFront() {
        if (left.isEmpty() && right.isEmpty()) return -1;
        int res = left.isEmpty() ? right.removeFirst() : left.removeFirst();
        balance();
        return res;
    }

    public int popMiddle() {
        if (left.isEmpty() && right.isEmpty()) return -1;
        int res = left.removeLast();
        balance();
        return res;
    }

    public int popBack() {
        if (left.isEmpty() && right.isEmpty()) return -1;
        int res = right.isEmpty() ? left.removeLast() : right.removeLast();
        balance();
        return res;
    }

    private void balance() {
        // Ensure left size == right size or left size == right size + 1
        while (left.size() > right.size() + 1) {
            right.addFirst(left.removeLast());
        }
        while (left.size() < right.size()) {
            left.addLast(right.removeFirst());
        }
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
 * obj.pushFront(val);
 * obj.pushMiddle(val);
 * obj.pushBack(val);
 * int param_4 = obj.popFront();
 * int param_5 = obj.popMiddle();
 * int param_6 = obj.popBack();
 */
```

## Python

```python
from collections import deque

class FrontMiddleBackQueue(object):
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _rebalance(self):
        # Ensure len(left) == len(right) or len(left) == len(right) + 1
        while len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        while len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.left.append(val)
        self._rebalance()

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.right.append(val)
        self._rebalance()

    def popFront(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self._rebalance()
        return val

    def popMiddle(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        val = self.left.pop()
        self._rebalance()
        return val

    def popBack(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._rebalance()
        return val
```

## Python3

```python
class FrontMiddleBackQueue:
    def __init__(self):
        from collections import deque
        self.left = deque()
        self.right = deque()

    def _rebalance(self):
        # Ensure len(left) == len(right) or len(left) == len(right) + 1
        while len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        while len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        self.left.append(val)
        self._rebalance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        val = self.left.popleft()
        self._rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        val = self.left.pop()
        self._rebalance()
        return val

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._rebalance()
        return val
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *data;
    int size;
    int cap;
} FrontMiddleBackQueue;

static void ensureCapacity(FrontMiddleBackQueue *obj) {
    if (obj->size + 1 > obj->cap) {
        int newCap = obj->cap * 2;
        int *newData = (int *)malloc(newCap * sizeof(int));
        memcpy(newData, obj->data, obj->size * sizeof(int));
        free(obj->data);
        obj->data = newData;
        obj->cap = newCap;
    }
}

/** Initialize your data structure here. */
FrontMiddleBackQueue* frontMiddleBackQueueCreate() {
    FrontMiddleBackQueue *obj = (FrontMiddleBackQueue *)malloc(sizeof(FrontMiddleBackQueue));
    obj->cap = 2048;
    obj->size = 0;
    obj->data = (int *)malloc(obj->cap * sizeof(int));
    return obj;
}

/** Push element val to the front of the queue. */
void frontMiddleBackQueuePushFront(FrontMiddleBackQueue* obj, int val) {
    ensureCapacity(obj);
    if (obj->size > 0) {
        memmove(&obj->data[1], &obj->data[0], obj->size * sizeof(int));
    }
    obj->data[0] = val;
    obj->size++;
}

/** Push element val to the middle of the queue. */
void frontMiddleBackQueuePushMiddle(FrontMiddleBackQueue* obj, int val) {
    ensureCapacity(obj);
    int pos = obj->size / 2; // frontmost middle position
    if (pos < obj->size) {
        memmove(&obj->data[pos + 1], &obj->data[pos], (obj->size - pos) * sizeof(int));
    }
    obj->data[pos] = val;
    obj->size++;
}

/** Push element val to the back of the queue. */
void frontMiddleBackQueuePushBack(FrontMiddleBackQueue* obj, int val) {
    ensureCapacity(obj);
    obj->data[obj->size] = val;
    obj->size++;
}

/** Pop the element from the front of the queue and return it. If the queue is empty, return -1. */
int frontMiddleBackQueuePopFront(FrontMiddleBackQueue* obj) {
    if (obj->size == 0) return -1;
    int val = obj->data[0];
    if (obj->size > 1) {
        memmove(&obj->data[0], &obj->data[1], (obj->size - 1) * sizeof(int));
    }
    obj->size--;
    return val;
}

/** Pop the element from the middle of the queue and return it. If the queue is empty, return -1. */
int frontMiddleBackQueuePopMiddle(FrontMiddleBackQueue* obj) {
    if (obj->size == 0) return -1;
    int pos = (obj->size - 1) / 2; // frontmost middle position
    int val = obj->data[pos];
    if (pos < obj->size - 1) {
        memmove(&obj->data[pos], &obj->data[pos + 1], (obj->size - pos - 1) * sizeof(int));
    }
    obj->size--;
    return val;
}

/** Pop the element from the back of the queue and return it. If the queue is empty, return -1. */
int frontMiddleBackQueuePopBack(FrontMiddleBackQueue* obj) {
    if (obj->size == 0) return -1;
    int val = obj->data[obj->size - 1];
    obj->size--;
    return val;
}

/** Free all memory associated with the queue. */
void frontMiddleBackQueueFree(FrontMiddleBackQueue* obj) {
    if (!obj) return;
    free(obj->data);
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class FrontMiddleBackQueue
{
    private LinkedList<int> left;
    private LinkedList<int> right;

    public FrontMiddleBackQueue()
    {
        left = new LinkedList<int>();
        right = new LinkedList<int>();
    }

    private void Rebalance()
    {
        // Ensure left.Count == right.Count or left.Count == right.Count + 1
        if (left.Count > right.Count + 1)
        {
            // move last of left to front of right
            var node = left.Last;
            left.RemoveLast();
            right.AddFirst(node.Value);
        }
        else if (left.Count < right.Count)
        {
            // move first of right to end of left
            var node = right.First;
            right.RemoveFirst();
            left.AddLast(node.Value);
        }
    }

    public void PushFront(int val)
    {
        left.AddFirst(val);
        Rebalance();
    }

    public void PushMiddle(int val)
    {
        // Insert at the end of left (frontmost middle position)
        left.AddLast(val);
        Rebalance();
    }

    public void PushBack(int val)
    {
        right.AddLast(val);
        Rebalance();
    }

    public int PopFront()
    {
        if (left.Count == 0 && right.Count == 0) return -1;

        int result;
        if (left.Count > 0)
        {
            result = left.First.Value;
            left.RemoveFirst();
        }
        else
        {
            result = right.First.Value;
            right.RemoveFirst();
        }
        Rebalance();
        return result;
    }

    public int PopMiddle()
    {
        if (left.Count == 0 && right.Count == 0) return -1;

        // frontmost middle is the last element of left
        int result = left.Last.Value;
        left.RemoveLast();
        Rebalance();
        return result;
    }

    public int PopBack()
    {
        if (left.Count == 0 && right.Count == 0) return -1;

        int result;
        if (right.Count > 0)
        {
            result = right.Last.Value;
            right.RemoveLast();
        }
        else
        {
            result = left.Last.Value;
            left.RemoveLast();
        }
        Rebalance();
        return result;
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
 * obj.PushFront(val);
 * obj.PushMiddle(val);
 * obj.PushBack(val);
 * int param_4 = obj.PopFront();
 * int param_5 = obj.PopMiddle();
 * int param_6 = obj.PopBack();
 */
```

## Javascript

```javascript
var FrontMiddleBackQueue = function() {
    this.arr = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
FrontMiddleBackQueue.prototype.pushFront = function(val) {
    this.arr.unshift(val);
};

/** 
 * @param {number} val
 * @return {void}
 */
FrontMiddleBackQueue.prototype.pushMiddle = function(val) {
    const mid = Math.floor(this.arr.length / 2);
    this.arr.splice(mid, 0, val);
};

/** 
 * @param {number} val
 * @return {void}
 */
FrontMiddleBackQueue.prototype.pushBack = function(val) {
    this.arr.push(val);
};

/**
 * @return {number}
 */
FrontMiddleBackQueue.prototype.popFront = function() {
    if (this.arr.length === 0) return -1;
    return this.arr.shift();
};

/**
 * @return {number}
 */
FrontMiddleBackQueue.prototype.popMiddle = function() {
    if (this.arr.length === 0) return -1;
    const mid = Math.floor((this.arr.length - 1) / 2);
    return this.arr.splice(mid, 1)[0];
};

/**
 * @return {number}
 */
FrontMiddleBackQueue.prototype.popBack = function() {
    if (this.arr.length === 0) return -1;
    return this.arr.pop();
};
```

## Typescript

```typescript
class FrontMiddleBackQueue {
    private left: number[];
    private right: number[];

    constructor() {
        this.left = [];
        this.right = [];
    }

    pushFront(val: number): void {
        this.left.unshift(val);
        this.rebalance();
    }

    pushMiddle(val: number): void {
        // Insert at the end of left (frontmost middle)
        this.left.push(val);
        this.rebalance();
    }

    pushBack(val: number): void {
        this.right.push(val);
        this.rebalance();
    }

    popFront(): number {
        if (this.isEmpty()) return -1;
        const val = this.left.shift()!;
        this.rebalance();
        return val;
    }

    popMiddle(): number {
        if (this.isEmpty()) return -1;
        const val = this.left.pop()!;
        this.rebalance();
        return val;
    }

    popBack(): number {
        if (this.isEmpty()) return -1;
        let val: number;
        if (this.right.length > 0) {
            val = this.right.pop()!;
        } else {
            // right empty, take from left
            val = this.left.pop()!;
        }
        this.rebalance();
        return val;
    }

    private isEmpty(): boolean {
        return this.left.length === 0 && this.right.length === 0;
    }

    private rebalance(): void {
        // Ensure left size == right size or left size == right size + 1
        while (this.left.length > this.right.length + 1) {
            const move = this.left.pop()!;
            this.right.unshift(move);
        }
        while (this.left.length < this.right.length) {
            const move = this.right.shift()!;
            this.left.push(move);
        }
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * var obj = new FrontMiddleBackQueue()
 * obj.pushFront(val)
 * obj.pushMiddle(val)
 * obj.pushBack(val)
 * var param_4 = obj.popFront()
 * var param_5 = obj.popMiddle()
 * var param_6 = obj.popBack()
 */
```

## Php

```php
class FrontMiddleBackQueue {
    private $arr;

    function __construct() {
        $this->arr = [];
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function pushFront($val) {
        array_unshift($this->arr, $val);
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function pushMiddle($val) {
        $mid = intdiv(count($this->arr), 2);
        array_splice($this->arr, $mid, 0, [$val]);
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function pushBack($val) {
        $this->arr[] = $val;
    }

    /**
     * @return Integer
     */
    function popFront() {
        if (empty($this->arr)) {
            return -1;
        }
        return array_shift($this->arr);
    }

    /**
     * @return Integer
     */
    function popMiddle() {
        $n = count($this->arr);
        if ($n == 0) {
            return -1;
        }
        $mid = intdiv(($n - 1), 2);
        $val = $this->arr[$mid];
        array_splice($this->arr, $mid, 1);
        return $val;
    }

    /**
     * @return Integer
     */
    function popBack() {
        if (empty($this->arr)) {
            return -1;
        }
        return array_pop($this->arr);
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * $obj = new FrontMiddleBackQueue();
 * $obj->pushFront($val);
 * $obj->pushMiddle($val);
 * $obj->pushBack($val);
 * $ret_4 = $obj->popFront();
 * $ret_5 = $obj->popMiddle();
 * $ret_6 = $obj->popBack();
 */
```

## Swift

```swift
class FrontMiddleBackQueue {
    private var data: [Int]

    init() {
        self.data = []
    }
    
    func pushFront(_ val: Int) {
        data.insert(val, at: 0)
    }
    
    func pushMiddle(_ val: Int) {
        let idx = data.count / 2
        data.insert(val, at: idx)
    }
    
    func pushBack(_ val: Int) {
        data.append(val)
    }
    
    func popFront() -> Int {
        if data.isEmpty { return -1 }
        return data.removeFirst()
    }
    
    func popMiddle() -> Int {
        if data.isEmpty { return -1 }
        let idx = (data.count - 1) / 2
        return data.remove(at: idx)
    }
    
    func popBack() -> Int {
        if data.isEmpty { return -1 }
        return data.removeLast()
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class FrontMiddleBackQueue() {
    private val front = ArrayDeque<Int>()
    private val back = ArrayDeque<Int>()

    fun pushFront(`val`: Int) {
        front.addFirst(`val`)
        balance()
    }

    fun pushMiddle(`val`: Int) {
        back.addFirst(`val`)
        balance()
    }

    fun pushBack(`val`: Int) {
        back.addLast(`val`)
        balance()
    }

    fun popFront(): Int {
        if (front.isEmpty() && back.isEmpty()) return -1
        val res = if (front.isNotEmpty()) front.removeFirst() else back.removeFirst()
        balance()
        return res
    }

    fun popMiddle(): Int {
        if (front.isEmpty() && back.isEmpty()) return -1
        val totalSize = front.size + back.size
        val res = if (totalSize % 2 == 0) {
            // even, middle is last of front
            front.removeLast()
        } else {
            // odd, middle is first of back
            back.removeFirst()
        }
        balance()
        return res
    }

    fun popBack(): Int {
        if (front.isEmpty() && back.isEmpty()) return -1
        val res = if (back.isNotEmpty()) back.removeLast() else front.removeLast()
        balance()
        return res
    }

    private fun balance() {
        // maintain front.size == floor(total/2)
        while (front.size > back.size) {
            back.addFirst(front.removeLast())
        }
        while (front.size < back.size - 1) {
            front.addLast(back.removeFirst())
        }
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * var obj = FrontMiddleBackQueue()
 * obj.pushFront(`val`)
 * obj.pushMiddle(`val`)
 * obj.pushBack(`val`)
 * var param_4 = obj.popFront()
 * var param_5 = obj.popMiddle()
 * var param_6 = obj.popBack()
 */
```

## Dart

```dart
class FrontMiddleBackQueue {
  List<int> _list;

  FrontMiddleBackQueue() : _list = [];

  void pushFront(int val) {
    _list.insert(0, val);
  }

  void pushMiddle(int val) {
    int idx = _list.length ~/ 2;
    _list.insert(idx, val);
  }

  void pushBack(int val) {
    _list.add(val);
  }

  int popFront() {
    if (_list.isEmpty) return -1;
    return _list.removeAt(0);
  }

  int popMiddle() {
    if (_list.isEmpty) return -1;
    int idx = (_list.length - 1) ~/ 2;
    return _list.removeAt(idx);
  }

  int popBack() {
    if (_list.isEmpty) return -1;
    return _list.removeLast();
  }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = FrontMiddleBackQueue();
 * obj.pushFront(val);
 * obj.pushMiddle(val);
 * obj.pushBack(val);
 * int param4 = obj.popFront();
 * int param5 = obj.popMiddle();
 * int param6 = obj.popBack();
 */
```

## Golang

```go
type FrontMiddleBackQueue struct {
	data []int
}

func Constructor() FrontMiddleBackQueue {
	return FrontMiddleBackQueue{}
}

func (this *FrontMiddleBackQueue) PushFront(val int) {
	this.data = append([]int{val}, this.data...)
}

func (this *FrontMiddleBackQueue) PushMiddle(val int) {
	idx := len(this.data) / 2
	if idx == len(this.data) {
		this.data = append(this.data, val)
	} else {
		this.data = append(this.data[:idx], append([]int{val}, this.data[idx:]...)...)
	}
}

func (this *FrontMiddleBackQueue) PushBack(val int) {
	this.data = append(this.data, val)
}

func (this *FrontMiddleBackQueue) PopFront() int {
	if len(this.data) == 0 {
		return -1
	}
	val := this.data[0]
	this.data = this.data[1:]
	return val
}

func (this *FrontMiddleBackQueue) PopMiddle() int {
	n := len(this.data)
	if n == 0 {
		return -1
	}
	idx := (n - 1) / 2
	val := this.data[idx]
	this.data = append(this.data[:idx], this.data[idx+1:]...)
	return val
}

func (this *FrontMiddleBackQueue) PopBack() int {
	if len(this.data) == 0 {
		return -1
	}
	n := len(this.data)
	val := this.data[n-1]
	this.data = this.data[:n-1]
	return val
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PushFront(val);
 * obj.PushMiddle(val);
 * obj.PushBack(val);
 * param_4 := obj.PopFront();
 * param_5 := obj.PopMiddle();
 * param_6 := obj.PopBack();
 */
```

## Ruby

```ruby
class FrontMiddleBackQueue
  def initialize()
    @arr = []
  end

=begin
    :type val: Integer
    :rtype: Void
=end
  def push_front(val)
    @arr.unshift(val)
  end

=begin
    :type val: Integer
    :rtype: Void
=end
  def push_middle(val)
    idx = @arr.size / 2
    @arr.insert(idx, val)
  end

=begin
    :type val: Integer
    :rtype: Void
=end
  def push_back(val)
    @arr.push(val)
  end

=begin
    :rtype: Integer
=end
  def pop_front()
    return -1 if @arr.empty?
    @arr.shift
  end

=begin
    :rtype: Integer
=end
  def pop_middle()
    return -1 if @arr.empty?
    idx = (@arr.size - 1) / 2
    @arr.delete_at(idx)
  end

=begin
    :rtype: Integer
=end
  def pop_back()
    return -1 if @arr.empty?
    @arr.pop
  end
end
```

## Scala

```scala
import scala.collection.mutable.ArrayDeque

class FrontMiddleBackQueue() {

  private val left = new ArrayDeque[Int]()
  private val right = new ArrayDeque[Int]()

  private def balance(): Unit = {
    while (left.size > right.size + 1) {
      right.prepend(left.removeLast())
    }
    while (left.size < right.size) {
      left.append(right.removeFirst())
    }
  }

  def pushFront(`val`: Int): Unit = {
    left.prepend(`val`)
    balance()
  }

  def pushMiddle(`val`: Int): Unit = {
    left.append(`val`)
    balance()
  }

  def pushBack(`val`: Int): Unit = {
    right.append(`val`)
    balance()
  }

  def popFront(): Int = {
    if (left.isEmpty && right.isEmpty) return -1
    val res = left.removeFirst()
    balance()
    res
  }

  def popMiddle(): Int = {
    if (left.isEmpty && right.isEmpty) return -1
    val res = left.removeLast()
    balance()
    res
  }

  def popBack(): Int = {
    if (left.isEmpty && right.isEmpty) return -1
    val res = if (right.nonEmpty) right.removeLast() else left.removeLast()
    balance()
    res
  }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * val obj = new FrontMiddleBackQueue()
 * obj.pushFront(`val`)
 * obj.pushMiddle(`val`)
 * obj.pushBack(`val`)
 * val param_4 = obj.popFront()
 * val param_5 = obj.popMiddle()
 * val param_6 = obj.popBack()
 */
```

## Rust

```rust
use std::vec::Vec;

struct FrontMiddleBackQueue {
    data: Vec<i32>,
}

impl FrontMiddleBackQueue {
    fn new() -> Self {
        FrontMiddleBackQueue { data: Vec::new() }
    }

    fn push_front(&mut self, val: i32) {
        self.data.insert(0, val);
    }

    fn push_middle(&mut self, val: i32) {
        let idx = self.data.len() / 2;
        self.data.insert(idx, val);
    }

    fn push_back(&mut self, val: i32) {
        self.data.push(val);
    }

    fn pop_front(&mut self) -> i32 {
        if self.data.is_empty() {
            -1
        } else {
            self.data.remove(0)
        }
    }

    fn pop_middle(&mut self) -> i32 {
        let n = self.data.len();
        if n == 0 {
            -1
        } else {
            let idx = (n - 1) / 2;
            self.data.remove(idx)
        }
    }

    fn pop_back(&mut self) -> i32 {
        match self.data.pop() {
            Some(v) => v,
            None => -1,
        }
    }
}
```

## Racket

```racket
(define front-middle-back-queue%
  (class object%
    (super-new)
    
    ;; internal storage
    (define data '())
    
    ;; push-front : exact-integer? -> void?
    (define/public (push-front val)
      (set! data (cons val data)))
    
    ;; push-back : exact-integer? -> void?
    (define/public (push-back val)
      (set! data (append data (list val))))
    
    ;; push-middle : exact-integer? -> void?
    (define/public (push-middle val)
      (let* ([n (length data)]
             [idx (quotient n 2)])
        (set! data (insert-at data idx val))))
    
    ;; pop-front : -> exact-integer?
    (define/public (pop-front)
      (if (null? data)
          -1
          (let ([v (car data)])
            (set! data (cdr data))
            v)))
    
    ;; pop-back : -> exact-integer?
    (define/public (pop-back)
      (if (null? data)
          -1
          (let-values ([(newlst removed) (remove-last data)])
            (set! data newlst)
            removed)))
    
    ;; pop-middle : -> exact-integer?
    (define/public (pop-middle)
      (if (null? data)
          -1
          (let* ([n (length data)]
                 [idx (quotient n 2)])
            (let-values ([(newlst removed) (delete-at data idx)])
              (set! data newlst)
              removed))))
    
    ;; helper: insert at index
    (define (insert-at lst idx val)
      (cond [(zero? idx) (cons val lst)]
            [(null? lst) (list val)] ; should only happen when idx == 0
            [else (cons (car lst) (insert-at (cdr lst) (sub1 idx) val))]))
    
    ;; helper: delete at index, returns multiple values (new-list removed-value)
    (define (delete-at lst idx)
      (cond [(zero? idx) (values (cdr lst) (car lst))]
            [else (let-values ([(rest removed) (delete-at (cdr lst) (sub1 idx))])
                    (values (cons (car lst) rest) removed))]))
    
    ;; helper: remove last element, returns multiple values (new-list removed-value)
    (define (remove-last lst)
      (cond [(null? (cdr lst)) (values '() (car lst))]
            [else (let-values ([(rest removed) (remove-last (cdr lst))])
                    (values (cons (car lst) rest) removed))]))))
```

## Erlang

```erlang
-module(front_middle_back_queue).

-export([front_middle_back_queue_init_/0,
         front_middle_back_queue_push_front/1,
         front_middle_back_queue_push_middle/1,
         front_middle_back_queue_push_back/1,
         front_middle_back_queue_pop_front/0,
         front_middle_back_queue_pop_middle/0,
         front_middle_back_queue_pop_back/0]).

%% Initialize the queue
-spec front_middle_back_queue_init_() -> any().
front_middle_back_queue_init_() ->
    put(queue_list, []).

%% Push value to the front
-spec front_middle_back_queue_push_front(integer()) -> any().
front_middle_back_queue_push_front(Val) ->
    L = get(queue_list),
    put(queue_list, [Val | L]).

%% Push value to the middle (frontmost middle position)
-spec front_middle_back_queue_push_middle(integer()) -> any().
front_middle_back_queue_push_middle(Val) ->
    L = get(queue_list),
    Len = length(L),
    MidIdx = Len div 2,
    {Left, Right} = lists:split(MidIdx, L),
    NewList = Left ++ [Val] ++ Right,
    put(queue_list, NewList).

%% Push value to the back
-spec front_middle_back_queue_push_back(integer()) -> any().
front_middle_back_queue_push_back(Val) ->
    L = get(queue_list),
    put(queue_list, L ++ [Val]).

%% Pop value from the front
-spec front_middle_back_queue_pop_front() -> integer().
front_middle_back_queue_pop_front() ->
    L = get(queue_list),
    case L of
        [] -> -1;
        [H | T] ->
            put(queue_list, T),
            H
    end.

%% Pop value from the middle (frontmost middle position)
-spec front_middle_back_queue_pop_middle() -> integer().
front_middle_back_queue_pop_middle() ->
    L = get(queue_list),
    Len = length(L),
    case Len of
        0 -> -1;
        _ ->
            MidIdx = (Len - 1) div 2,
            {Left, Rest} = lists:split(MidIdx, L),
            case Rest of
                [] -> -1; % should not happen
                [Removed | Right] ->
                    NewList = Left ++ Right,
                    put(queue_list, NewList),
                    Removed
            end
    end.

%% Pop value from the back
-spec front_middle_back_queue_pop_back() -> integer().
front_middle_back_queue_pop_back() ->
    L = get(queue_list),
    case lists:reverse(L) of
        [] -> -1;
        [H | RevTail] ->
            NewList = lists:reverse(RevTail),
            put(queue_list, NewList),
            H
    end.
```

## Elixir

```elixir
defmodule FrontMiddleBackQueue do
  @spec init_() :: any
  def init_() do
    case Process.whereis(__MODULE__) do
      nil ->
        Agent.start_link(fn -> {:queue.new(), :queue.new()} end, name: __MODULE__)

      pid ->
        Agent.stop(pid)
        Agent.start_link(fn -> {:queue.new(), :queue.new()} end, name: __MODULE__)
    end

    :ok
  end

  @spec push_front(val :: integer) :: any
  def push_front(val) do
    Agent.update(__MODULE__, fn {left, right} ->
      left = :queue.in_l(val, left)
      rebalance({left, right})
    end)
  end

  @spec push_middle(val :: integer) :: any
  def push_middle(val) do
    Agent.update(__MODULE__, fn {left, right} ->
      left = :queue.in_r(val, left)
      rebalance({left, right})
    end)
  end

  @spec push_back(val :: integer) :: any
  def push_back(val) do
    Agent.update(__MODULE__, fn {left, right} ->
      right = :queue.in_r(val, right)
      rebalance({left, right})
    end)
  end

  @spec pop_front() :: integer
  def pop_front() do
    Agent.get_and_update(__MODULE__, fn {left, right} ->
      case :queue.out_l(left) do
        {{:value, v}, new_left} ->
          {v, rebalance({new_left, right})}

        {:empty, _} ->
          {-1, {left, right}}
      end
    end)
  end

  @spec pop_middle() :: integer
  def pop_middle() do
    Agent.get_and_update(__MODULE__, fn {left, right} ->
      case :queue.out_r(left) do
        {{:value, v}, new_left} ->
          {v, rebalance({new_left, right})}

        {:empty, _} ->
          {-1, {left, right}}
      end
    end)
  end

  @spec pop_back() :: integer
  def pop_back() do
    Agent.get_and_update(__MODULE__, fn {left, right} ->
      case :queue.out_r(right) do
        {{:value, v}, new_right} ->
          {v, rebalance({left, new_right})}

        {:empty, _} ->
          case :queue.out_r(left) do
            {{:value, v}, new_left} ->
              {v, rebalance({new_left, right})}

            {:empty, _} ->
              {-1, {left, right}}
          end
      end
    end)
  end

  defp rebalance({left, right}) do
    lsize = :queue.len(left)
    rsize = :queue.len(right)

    cond do
      lsize > rsize + 1 ->
        {{:value, v}, new_left} = :queue.out_r(left)
        new_right = :queue.in_l(v, right)
        rebalance({new_left, new_right})

      lsize < rsize ->
        {{:value, v}, new_right} = :queue.out_l(right)
        new_left = :queue.in_r(v, left)
        rebalance({new_left, new_right})

      true ->
        {left, right}
    end
  end
end
```

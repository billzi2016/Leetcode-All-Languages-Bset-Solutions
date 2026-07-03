# 0225. Implement Stack using Queues

## Cpp

```cpp
class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {}
    
    /** Push element x onto stack. */
    void push(int x) {
        q2.push(x);
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        std::swap(q1, q2);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int val = q1.front();
        q1.pop();
        return val;
    }
    
    /** Get the top element. */
    int top() {
        return q1.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty();
    }
private:
    std::queue<int> q1, q2;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
```

## Java

```java
import java.util.LinkedList;
import java.util.Queue;

class MyStack {
    private Queue<Integer> q1;
    private Queue<Integer> q2;

    public MyStack() {
        q1 = new LinkedList<>();
        q2 = new LinkedList<>();
    }
    
    public void push(int x) {
        q2.offer(x);
        while (!q1.isEmpty()) {
            q2.offer(q1.poll());
        }
        // swap q1 and q2
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }
    
    public int pop() {
        return q1.poll();
    }
    
    public int top() {
        return q1.peek();
    }
    
    public boolean empty() {
        return q1.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
```

## Python

```python
class MyStack(object):
    def __init__(self):
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # Move elements except the last to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # Last element is the top of stack
        res = self.q1.popleft()
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # Peek the last element
        res = self.q1[0]
        # Move it to q2 as well
        self.q2.append(self.q1.popleft())
        # Swap queues back
        self.q1, self.q2 = self.q2, self.q1
        return res

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1
```

## Python3

```python
import collections

class MyStack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return res

    def empty(self) -> bool:
        return not self.q1
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

typedef struct Node {
    int val;
    struct Node* next;
} Node;

typedef struct Queue {
    Node* head;
    Node* tail;
} Queue;

static void queueInit(Queue* q) {
    q->head = q->tail = NULL;
}

static bool queueEmpty(const Queue* q) {
    return q->head == NULL;
}

static void enqueue(Queue* q, int x) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = x;
    n->next = NULL;
    if (q->tail) {
        q->tail->next = n;
        q->tail = n;
    } else {
        q->head = q->tail = n;
    }
}

static int dequeue(Queue* q) {
    Node* h = q->head;
    int v = h->val;
    q->head = h->next;
    if (!q->head) q->tail = NULL;
    free(h);
    return v;
}

/** 
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 *
 * int param_2 = myStackPop(obj);
 *
 * int param_3 = myStackTop(obj);
 *
 * bool param_4 = myStackEmpty(obj);
 *
 * myStackFree(obj);
*/

typedef struct {
    Queue q1;
    Queue q2;
} MyStack;

MyStack* myStackCreate() {
    MyStack* obj = (MyStack*)malloc(sizeof(MyStack));
    queueInit(&obj->q1);
    queueInit(&obj->q2);
    return obj;
}

void myStackPush(MyStack* obj, int x) {
    enqueue(&obj->q1, x);
}

/* Helper to move all but last element from src to dst */
static void transferExceptLast(Queue* src, Queue* dst) {
    while (src->head && src->head != src->tail) {
        int v = dequeue(src);
        enqueue(dst, v);
    }
}

int myStackPop(MyStack* obj) {
    // move all but last to q2
    transferExceptLast(&obj->q1, &obj->q2);
    // last element is the top of stack
    int topVal = dequeue(&obj->q1);
    // swap queues
    Queue temp = obj->q1;
    obj->q1 = obj->q2;
    obj->q2 = temp;
    return topVal;
}

int myStackTop(MyStack* obj) {
    transferExceptLast(&obj->q1, &obj->q2);
    int topVal = dequeue(&obj->q1);
    enqueue(&obj->q2, topVal); // put it back
    // swap queues to restore state
    Queue temp = obj->q1;
    obj->q1 = obj->q2;
    obj->q2 = temp;
    return topVal;
}

bool myStackEmpty(MyStack* obj) {
    return queueEmpty(&obj->q1);
}

void myStackFree(MyStack* obj) {
    // free remaining nodes in both queues
    while (!queueEmpty(&obj->q1)) dequeue(&obj->q1);
    while (!queueEmpty(&obj->q2)) dequeue(&obj->q2);
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class MyStack {
    private Queue<int> primary;
    private Queue<int> secondary;

    public MyStack() {
        primary = new Queue<int>();
        secondary = new Queue<int>();
    }
    
    public void Push(int x) {
        primary.Enqueue(x);
    }
    
    public int Pop() {
        while (primary.Count > 1) {
            secondary.Enqueue(primary.Dequeue());
        }
        int top = primary.Dequeue();
        SwapQueues();
        return top;
    }
    
    public int Top() {
        while (primary.Count > 1) {
            secondary.Enqueue(primary.Dequeue());
        }
        int top = primary.Peek();
        secondary.Enqueue(primary.Dequeue()); // move the last element to secondary
        SwapQueues();
        return top;
    }
    
    public bool Empty() {
        return primary.Count == 0;
    }

    private void SwapQueues() {
        var temp = primary;
        primary = secondary;
        secondary = temp;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */
```

## Javascript

```javascript
var MyStack = function() {
    this.q1 = [];
    this.q2 = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    this.q1.push(x);
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    while (this.q1.length > 1) {
        this.q2.push(this.q1.shift());
    }
    var popped = this.q1.shift();
    // swap queues
    var temp = this.q1;
    this.q1 = this.q2;
    this.q2 = temp;
    return popped;
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    while (this.q1.length > 1) {
        this.q2.push(this.q1.shift());
    }
    var topElem = this.q1[0];
    this.q2.push(this.q1.shift()); // move the last element as well
    // swap queues
    var temp = this.q1;
    this.q1 = this.q2;
    this.q2 = temp;
    return topElem;
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    return this.q1.length === 0;
};
```

## Typescript

```typescript
class MyStack {
    private q1: number[];
    private q2: number[];

    constructor() {
        this.q1 = [];
        this.q2 = [];
    }

    push(x: number): void {
        this.q1.push(x);
    }

    pop(): number {
        while (this.q1.length > 1) {
            this.q2.push(this.q1.shift()!);
        }
        const top = this.q1.shift()!;
        [this.q1, this.q2] = [this.q2, this.q1];
        return top;
    }

    top(): number {
        while (this.q1.length > 1) {
            this.q2.push(this.q1.shift()!);
        }
        const top = this.q1[0];
        this.q2.push(this.q1.shift()!);
        [this.q1, this.q2] = [this.q2, this.q1];
        return top;
    }

    empty(): boolean {
        return this.q1.length === 0 && this.q2.length === 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
```

## Php

```php
class MyStack {
    private $q1;
    private $q2;

    /**
     */
    function __construct() {
        $this->q1 = new SplQueue();
        $this->q2 = new SplQueue();
    }

    /**
     * @param Integer $x
     * @return NULL
     */
    function push($x) {
        $this->q1->enqueue($x);
    }

    /**
     * @return Integer
     */
    function pop() {
        while ($this->q1->count() > 1) {
            $this->q2->enqueue($this->q1->dequeue());
        }
        $top = $this->q1->dequeue();
        // swap queues
        $temp = $this->q1;
        $this->q1 = $this->q2;
        $this->q2 = $temp;
        return $top;
    }

    /**
     * @return Integer
     */
    function top() {
        while ($this->q1->count() > 1) {
            $this->q2->enqueue($this->q1->dequeue());
        }
        $top = $this->q1->dequeue();
        $this->q2->enqueue($top);
        // swap queues
        $temp = $this->q1;
        $this->q1 = $this->q2;
        $this->q2 = $temp;
        return $top;
    }

    /**
     * @return Boolean
     */
    function empty() {
        return $this->q1->isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * $obj = new MyStack();
 * $obj->push($x);
 * $ret_2 = $obj->pop();
 * $ret_3 = $obj->top();
 * $ret_4 = $obj->empty();
 */
```

## Swift

```swift
class MyStack {
    private var q1: [Int] = []
    private var q2: [Int] = []

    init() { }

    func push(_ x: Int) {
        q2.append(x)
        while !q1.isEmpty {
            q2.append(q1.removeFirst())
        }
        let temp = q1
        q1 = q2
        q2 = temp
    }

    func pop() -> Int {
        return q1.removeFirst()
    }

    func top() -> Int {
        return q1.first!
    }

    func empty() -> Bool {
        return q1.isEmpty
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class MyStack() {

    private var q1 = ArrayDeque<Int>()
    private var q2 = ArrayDeque<Int>()

    fun push(x: Int) {
        q2.addLast(x)
        while (!q1.isEmpty()) {
            q2.addLast(q1.removeFirst())
        }
        val temp = q1
        q1 = q2
        q2 = temp
    }

    fun pop(): Int {
        return q1.removeFirst()
    }

    fun top(): Int {
        return q1.first()
    }

    fun empty(): Boolean {
        return q1.isEmpty()
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
```

## Dart

```dart
class MyStack {
  List<int> _q1 = [];
  List<int> _q2 = [];

  MyStack();

  void push(int x) {
    _q2.add(x);
    while (_q1.isNotEmpty) {
      _q2.add(_q1.removeAt(0));
    }
    var temp = _q1;
    _q1 = _q2;
    _q2 = temp;
  }

  int pop() {
    return _q1.removeAt(0);
  }

  int top() {
    return _q1[0];
  }

  bool empty() {
    return _q1.isEmpty;
  }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = MyStack();
 * obj.push(x);
 * int param2 = obj.pop();
 * int param3 = obj.top();
 * bool param4 = obj.empty();
 */
```

## Golang

```go
type MyStack struct {
	q1 []int
	q2 []int
}

func Constructor() MyStack {
	return MyStack{
		q1: []int{},
		q2: []int{},
	}
}

func (this *MyStack) Push(x int) {
	this.q1 = append(this.q1, x)
}

func (this *MyStack) Pop() int {
	for len(this.q1) > 1 {
		this.q2 = append(this.q2, this.q1[0])
		this.q1 = this.q1[1:]
	}
	res := this.q1[0]
	this.q1 = this.q1[:0]
	this.q1, this.q2 = this.q2, this.q1
	return res
}

func (this *MyStack) Top() int {
	for len(this.q1) > 1 {
		this.q2 = append(this.q2, this.q1[0])
		this.q1 = this.q1[1:]
	}
	top := this.q1[0]
	this.q2 = append(this.q2, top)
	this.q1 = this.q1[:0]
	this.q1, this.q2 = this.q2, this.q1
	return top
}

func (this *MyStack) Empty() bool {
	return len(this.q1) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
```

## Ruby

```ruby
class MyStack
    def initialize()
        @q1 = []
        @q2 = []
    end

=begin
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        @q1 << x
    end

=begin
    :rtype: Integer
=end
    def pop()
        while @q1.size > 1
            @q2 << @q1.shift
        end
        val = @q1.shift
        swap_queues
        val
    end

=begin
    :rtype: Integer
=end
    def top()
        while @q1.size > 1
            @q2 << @q1.shift
        end
        val = @q1.shift
        @q2 << val
        swap_queues
        val
    end

=begin
    :rtype: Boolean
=end
    def empty()
        @q1.empty?
    end

    private

    def swap_queues
        @q1, @q2 = @q2, @q1
    end
end
```

## Scala

```scala
import scala.collection.mutable.Queue

class MyStack() {

  private val q1: Queue[Int] = Queue()
  private val q2: Queue[Int] = Queue()

  def push(x: Int): Unit = {
    q2.enqueue(x)
    while (q1.nonEmpty) {
      q2.enqueue(q1.dequeue())
    }
    // swap references
    val temp = q1.clone() // not needed, just swap contents
    q1.clear()
    q1 ++= q2
    q2.clear()
  }

  def pop(): Int = {
    q1.dequeue()
  }

  def top(): Int = {
    q1.front
  }

  def empty(): Boolean = {
    q1.isEmpty
  }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * val obj = new MyStack()
 * obj.push(x)
 * val param_2 = obj.pop()
 * val param_3 = obj.top()
 * val param_4 = obj.empty()
 */
```

## Rust

```rust
use std::collections::VecDeque;

struct MyStack {
    q1: VecDeque<i32>,
    q2: VecDeque<i32>,
}

impl MyStack {
    fn new() -> Self {
        MyStack { q1: VecDeque::new(), q2: VecDeque::new() }
    }

    fn push(&mut self, x: i32) {
        self.q1.push_back(x);
    }

    fn pop(&mut self) -> i32 {
        while self.q1.len() > 1 {
            let v = self.q1.pop_front().unwrap();
            self.q2.push_back(v);
        }
        let res = self.q1.pop_front().unwrap();
        std::mem::swap(&mut self.q1, &mut self.q2);
        res
    }

    fn top(&mut self) -> i32 {
        while self.q1.len() > 1 {
            let v = self.q1.pop_front().unwrap();
            self.q2.push_back(v);
        }
        let res = *self.q1.front().unwrap();
        let v = self.q1.pop_front().unwrap();
        self.q2.push_back(v);
        std::mem::swap(&mut self.q1, &mut self.q2);
        res
    }

    fn empty(&self) -> bool {
        self.q1.is_empty() && self.q2.is_empty()
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let mut obj = MyStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: bool = obj.empty();
 */
```

## Racket

```racket
#lang racket
(require racket/queue)

(define my-stack%
  (class object%
    (super-new)
    
    (init-field) ; no init fields
    
    (field [q1 (make-queue)]
           [q2 (make-queue)])
    
    ;; push : exact-integer? -> void?
    (define/public (push x)
      (enqueue! q1 x))
    
    ;; pop : -> exact-integer?
    (define/public (pop)
      (let loop ()
        (if (queue-empty? q1)
            (error "pop from empty stack")
            (let ([val (dequeue! q1)])
              (if (queue-empty? q1)
                  (begin
                    (set! q1 q2)
                    (set! q2 (make-queue))
                    val)
                  (begin
                    (enqueue! q2 val)
                    (loop)))))))
    
    ;; top : -> exact-integer?
    (define/public (top)
      (let loop ()
        (if (queue-empty? q1)
            (error "top from empty stack")
            (let ([val (dequeue! q1)])
              (if (queue-empty? q1)
                  (begin
                    (enqueue! q2 val)
                    (set! q1 q2)
                    (set! q2 (make-queue))
                    val)
                  (begin
                    (enqueue! q2 val)
                    (loop)))))))
    
    ;; empty : -> boolean?
    (define/public (empty)
      (and (queue-empty? q1) (queue-empty? q2)))))
```

## Erlang

```erlang
-spec my_stack_init_() -> any().
my_stack_init_() ->
    put(stack, []).

-spec my_stack_push(X :: integer()) -> any().
my_stack_push(X) ->
    Stack = case get(stack) of
                undefined -> [];
                S -> S
            end,
    put(stack, [X | Stack]).

-spec my_stack_pop() -> integer().
my_stack_pop() ->
    Stack = case get(stack) of
                undefined -> [];
                S -> S
            end,
    case Stack of
        [Top | Rest] ->
            put(stack, Rest),
            Top;
        [] ->
            0
    end.

-spec my_stack_top() -> integer().
my_stack_top() ->
    Stack = case get(stack) of
                undefined -> [];
                S -> S
            end,
    case Stack of
        [Top | _] -> Top;
        [] -> 0
    end.

-spec my_stack_empty() -> boolean().
my_stack_empty() ->
    Stack = case get(stack) of
                undefined -> [];
                S -> S
            end,
    Stack == [].
```

## Elixir

```elixir
defmodule MyStack do
  @spec init_() :: any
  def init_() do
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    {:ok, _pid} = Agent.start_link(fn -> %{q1: :queue.new(), q2: :queue.new()} end, name: __MODULE__)
    :ok
  end

  @spec push(x :: integer) :: any
  def push(x) do
    Agent.update(__MODULE__, fn state ->
      q2 = :queue.in(x, state.q2)
      {new_q1, _} = transfer(state.q1, q2)
      %{q1: new_q1, q2: :queue.new()}
    end)
  end

  defp transfer(q_from, q_to) do
    case :queue.out(q_from) do
      {:empty, _} -> {q_to, q_from}
      {{:value, val}, rest} ->
        transfer(rest, :queue.in(val, q_to))
    end
  end

  @spec pop() :: integer
  def pop() do
    Agent.get_and_update(__MODULE__, fn state ->
      case :queue.out(state.q1) do
        {:empty, _} -> {nil, state}
        {{:value, val}, new_q1} -> {val, %{state | q1: new_q1}}
      end
    end)
  end

  @spec top() :: integer
  def top() do
    Agent.get(__MODULE__, fn state ->
      case :queue.peek(state.q1) do
        :empty -> nil
        {:value, val} -> val
        val -> val
      end
    end)
  end

  @spec empty() :: boolean
  def empty() do
    Agent.get(__MODULE__, fn state ->
      :queue.is_empty(state.q1)
    end)
  end
end
```

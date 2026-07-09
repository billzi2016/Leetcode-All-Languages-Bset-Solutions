# 0155. Min Stack

## Cpp

```cpp
#include <stack>
using namespace std;

class MinStack {
private:
    stack<int> data;
    stack<int> mins;
public:
    MinStack() {
    }
    
    void push(int val) {
        data.push(val);
        if (mins.empty() || val <= mins.top()) {
            mins.push(val);
        }
    }
    
    void pop() {
        if (!data.empty()) {
            if (data.top() == mins.top()) {
                mins.pop();
            }
            data.pop();
        }
    }
    
    int top() {
        return data.top();
    }
    
    int getMin() {
        return mins.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

class MinStack {
    private Deque<Integer> stack;
    private Deque<Integer> minStack;

    public MinStack() {
        stack = new ArrayDeque<>();
        minStack = new ArrayDeque<>();
    }

    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }

    public void pop() {
        int removed = stack.pop();
        if (removed == minStack.peek()) {
            minStack.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

## Python

```python
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
```

## Python3

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

## C

```c
typedef struct Node {
    int val;
    int curMin;
    struct Node* next;
} Node;

typedef struct {
    Node* top;
} MinStack;

MinStack* minStackCreate() {
    MinStack* obj = (MinStack*)malloc(sizeof(MinStack));
    obj->top = NULL;
    return obj;
}

void minStackPush(MinStack* obj, int val) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->val = val;
    if (obj->top == NULL) {
        node->curMin = val;
    } else {
        node->curMin = val < obj->top->curMin ? val : obj->top->curMin;
    }
    node->next = obj->top;
    obj->top = node;
}

void minStackPop(MinStack* obj) {
    Node* tmp = obj->top;
    obj->top = obj->top->next;
    free(tmp);
}

int minStackTop(MinStack* obj) {
    return obj->top->val;
}

int minStackGetMin(MinStack* obj) {
    return obj->top->curMin;
}

void minStackFree(MinStack* obj) {
    while (obj->top != NULL) {
        Node* tmp = obj->top;
        obj->top = obj->top->next;
        free(tmp);
    }
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class MinStack {
    private Stack<int> _stack;
    private Stack<int> _minStack;

    public MinStack() {
        _stack = new Stack<int>();
        _minStack = new Stack<int>();
    }
    
    public void Push(int val) {
        _stack.Push(val);
        if (_minStack.Count == 0 || val <= _minStack.Peek()) {
            _minStack.Push(val);
        }
    }
    
    public void Pop() {
        int removed = _stack.Pop();
        if (removed == _minStack.Peek()) {
            _minStack.Pop();
        }
    }
    
    public int Top() {
        return _stack.Peek();
    }
    
    public int GetMin() {
        return _minStack.Peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
```

## Javascript

```javascript
var MinStack = function() {
    this.stack = [];
    this.minStack = [];
};

MinStack.prototype.push = function(val) {
    this.stack.push(val);
    if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) {
        this.minStack.push(val);
    }
};

MinStack.prototype.pop = function() {
    const popped = this.stack.pop();
    if (popped === this.minStack[this.minStack.length - 1]) {
        this.minStack.pop();
    }
};

MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1];
};

MinStack.prototype.getMin = function() {
    return this.minStack[this.minStack.length - 1];
};
```

## Typescript

```typescript
class MinStack {
    private stack: number[] = [];
    private minStack: number[] = [];

    constructor() {}

    push(val: number): void {
        this.stack.push(val);
        if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) {
            this.minStack.push(val);
        }
    }

    pop(): void {
        const popped = this.stack.pop();
        if (popped !== undefined && popped === this.minStack[this.minStack.length - 1]) {
            this.minStack.pop();
        }
    }

    top(): number {
        return this.stack[this.stack.length - 1];
    }

    getMin(): number {
        return this.minStack[this.minStack.length - 1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

## Php

```php
class MinStack {
    private $stack;
    private $minStack;

    function __construct() {
        $this->stack = [];
        $this->minStack = [];
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val) {
        $this->stack[] = $val;
        if (empty($this->minStack) || $val <= end($this->minStack)) {
            $this->minStack[] = $val;
        }
    }

    /**
     * @return NULL
     */
    function pop() {
        $val = array_pop($this->stack);
        if ($val === end($this->minStack)) {
            array_pop($this->minStack);
        }
    }

    /**
     * @return Integer
     */
    function top() {
        return end($this->stack);
    }

    /**
     * @return Integer
     */
    function getMin() {
        return end($this->minStack);
    }
}
```

## Swift

```swift
class MinStack {
    private var stack: [(value: Int, minSoFar: Int)] = []
    
    init() { }
    
    func push(_ val: Int) {
        let currentMin = stack.isEmpty ? val : min(val, stack.last!.minSoFar)
        stack.append((value: val, minSoFar: currentMin))
    }
    
    func pop() {
        if !stack.isEmpty {
            stack.removeLast()
        }
    }
    
    func top() -> Int {
        return stack.last!.value
    }
    
    func getMin() -> Int {
        return stack.last!.minSoFar
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class MinStack() {
    private val stack = ArrayDeque<Int>()
    private val minStack = ArrayDeque<Int>()

    fun push(`val`: Int) {
        stack.addLast(`val`)
        if (minStack.isEmpty() || `val` <= minStack.last()) {
            minStack.addLast(`val`)
        }
    }

    fun pop() {
        val removed = stack.removeLast()
        if (removed == minStack.last()) {
            minStack.removeLast()
        }
    }

    fun top(): Int = stack.last()

    fun getMin(): Int = minStack.last()
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = MinStack()
 * obj.push(`val`)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

## Dart

```dart
class MinStack {
  final List<int> _stack = [];
  final List<int> _minStack = [];

  MinStack();

  void push(int val) {
    _stack.add(val);
    if (_minStack.isEmpty || val <= _minStack.last) {
      _minStack.add(val);
    }
  }

  void pop() {
    int removed = _stack.removeLast();
    if (removed == _minStack.last) {
      _minStack.removeLast();
    }
  }

  int top() {
    return _stack.last;
  }

  int getMin() {
    return _minStack.last;
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = MinStack();
 * obj.push(val);
 * obj.pop();
 * int param3 = obj.top();
 * int param4 = obj.getMin();
 */
```

## Golang

```go
type MinStack struct {
	stack []int
	mins  []int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	this.stack = append(this.stack, val)
	if len(this.mins) == 0 || val < this.mins[len(this.mins)-1] {
		this.mins = append(this.mins, val)
	} else {
		this.mins = append(this.mins, this.mins[len(this.mins)-1])
	}
}

func (this *MinStack) Pop() {
	if len(this.stack) == 0 {
		return
	}
	this.stack = this.stack[:len(this.stack)-1]
	this.mins = this.mins[:len(this.mins)-1]
}

func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
	return this.mins[len(this.mins)-1]
}
```

## Ruby

```ruby
class MinStack
  def initialize()
    @stack = []
  end

=begin
    :type val: Integer
    :rtype: Void
=end
  def push(val)
    if @stack.empty?
      @stack << [val, val]
    else
      cur_min = @stack[-1][1]
      @stack << [val, (val < cur_min ? val : cur_min)]
    end
  end

=begin
    :rtype: Void
=end
  def pop()
    @stack.pop
  end

=begin
    :rtype: Integer
=end
  def top()
    @stack[-1][0]
  end

=begin
    :rtype: Integer
=end
  def get_min()
    @stack[-1][1]
  end
end
```

## Scala

```scala
import java.util.ArrayDeque

class MinStack() {

  private val stack = new ArrayDeque[Int]()
  private val minStack = new ArrayDeque[Int]()

  def push(`val`: Int): Unit = {
    stack.push(`val`)
    if (minStack.isEmpty || `val` <= minStack.peek()) {
      minStack.push(`val`)
    }
  }

  def pop(): Unit = {
    val removed = stack.pop()
    if (removed == minStack.peek()) {
      minStack.pop()
    }
  }

  def top(): Int = {
    stack.peek()
  }

  def getMin(): Int = {
    minStack.peek()
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * val obj = new MinStack()
 * obj.push(`val`)
 * obj.pop()
 * val param_3 = obj.top()
 * val param_4 = obj.getMin()
 */
```

## Rust

```rust
use std::cell::RefCell;

struct MinStack {
    data: RefCell<Vec<(i32, i32)>>,
}

impl MinStack {
    fn new() -> Self {
        MinStack {
            data: RefCell::new(Vec::new()),
        }
    }

    fn push(&self, val: i32) {
        let mut stack = self.data.borrow_mut();
        let cur_min = match stack.last() {
            Some(&(_, m)) => if val < m { val } else { m },
            None => val,
        };
        stack.push((val, cur_min));
    }

    fn pop(&self) {
        let mut stack = self.data.borrow_mut();
        stack.pop();
    }

    fn top(&self) -> i32 {
        let stack = self.data.borrow();
        stack.last().unwrap().0
    }

    fn get_min(&self) -> i32 {
        let stack = self.data.borrow();
        stack.last().unwrap().1
    }
}
```

## Racket

```racket
(define min-stack%
  (class object%
    (super-new)
    ;; internal stacks
    (define stack '())
    (define mins '())
    
    ; push : exact-integer? -> void?
    (define/public (push val)
      (set! stack (cons val stack))
      (let ((new-min (if (null? mins) 
                         val 
                         (min val (car mins)))))
        (set! mins (cons new-min mins))))
    
    ; pop : -> void?
    (define/public (pop)
      (set! stack (cdr stack))
      (set! mins (cdr mins)))
    
    ; top : -> exact-integer?
    (define/public (top)
      (car stack))
    
    ; get-min : -> exact-integer?
    (define/public (get-min)
      (car mins))))
```

## Erlang

```erlang
-module(solution).
-export([min_stack_init_/0,
         min_stack_push/1,
         min_stack_pop/0,
         min_stack_top/0,
         min_stack_get_min/0]).

min_stack_init_() ->
    put(min_stack_vals, []),
    put(min_stack_mins, []).

min_stack_push(Val) when is_integer(Val) ->
    Vals = get(min_stack_vals),
    Mins = get(min_stack_mins),
    NewVals = [Val | Vals],
    NewMins =
        case Mins of
            [] -> [Val];
            [CurMin | _] ->
                if Val < CurMin -> [Val | Mins];
                   true -> [CurMin | Mins]
                end
        end,
    put(min_stack_vals, NewVals),
    put(min_stack_mins, NewMins).

min_stack_pop() ->
    Vals = get(min_stack_vals),
    Mins = get(min_stack_mins),
    case {Vals, Mins} of
        {[_, | RestVals], [_ , | RestMins]} ->
            put(min_stack_vals, RestVals),
            put(min_stack_mins, RestMins);
        _ -> ok
    end.

min_stack_top() ->
    [Top | _] = get(min_stack_vals),
    Top.

min_stack_get_min() ->
    [Min | _] = get(min_stack_mins),
    Min.
```

## Elixir

```elixir
defmodule MinStack do
  @state_key {__MODULE__, :state}

  @spec init_() :: any
  def init_() do
    Process.put(@state_key, %{stack: [], mins: []})
    :ok
  end

  @spec push(val :: integer) :: any
  def push(val) do
    state = Process.get(@state_key)
    stack = [val | state.stack]

    mins =
      case state.mins do
        [] -> [val]
        [m | _] = ms when val <= m -> [val | ms]
        ms -> ms
      end

    Process.put(@state_key, %{stack: stack, mins: mins})
    :ok
  end

  @spec pop() :: any
  def pop() do
    state = Process.get(@state_key)
    [top | rest] = state.stack

    mins =
      case state.mins do
        [m | ms] when m == top -> ms
        ms -> ms
      end

    Process.put(@state_key, %{stack: rest, mins: mins})
    :ok
  end

  @spec top() :: integer
  def top() do
    state = Process.get(@state_key)
    [top | _] = state.stack
    top
  end

  @spec get_min() :: integer
  def get_min() do
    state = Process.get(@state_key)
    [min | _] = state.mins
    min
  end
end
```

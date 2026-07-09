# 1381. Design a Stack With Increment Operation

## Cpp

```cpp
class CustomStack {
public:
    CustomStack(int maxSize) : maxSize(maxSize), top(-1) {
        stack.assign(maxSize, 0);
        inc.assign(maxSize, 0);
    }
    
    void push(int x) {
        if (top + 1 < maxSize) {
            ++top;
            stack[top] = x;
        }
    }
    
    int pop() {
        if (top == -1) return -1;
        int res = stack[top] + inc[top];
        if (top > 0) inc[top - 1] += inc[top];
        inc[top] = 0;
        --top;
        return res;
    }
    
    void increment(int k, int val) {
        int idx = std::min(k, top + 1) - 1;
        if (idx >= 0) inc[idx] += val;
    }

private:
    int maxSize;
    int top;
    std::vector<int> stack;
    std::vector<int> inc;
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
```

## Java

```java
class CustomStack {
    private final int[] stack;
    private final int[] inc;
    private int top;
    private final int maxSize;

    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
        this.stack = new int[maxSize];
        this.inc = new int[maxSize];
        this.top = -1;
    }

    public void push(int x) {
        if (top + 1 < maxSize) {
            stack[++top] = x;
        }
    }

    public int pop() {
        if (top == -1) {
            return -1;
        }
        int result = stack[top] + inc[top];
        if (top > 0) {
            inc[top - 1] += inc[top];
        }
        inc[top] = 0;
        top--;
        return result;
    }

    public void increment(int k, int val) {
        int idx = Math.min(k, top + 1) - 1;
        if (idx >= 0) {
            inc[idx] += val;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
```

## Python

```python
class CustomStack(object):
    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []
        self.inc = [0] * maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1
        i = len(self.stack) - 1
        val = self.stack.pop() + self.inc[i]
        if i > 0:
            self.inc[i - 1] += self.inc[i]
        self.inc[i] = 0
        return val

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.inc[idx] += val
```

## Python3

```python
class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        i = len(self.stack) - 1
        val = self.stack.pop() + self.inc[i]
        if i > 0:
            self.inc[i - 1] += self.inc[i]
        self.inc[i] = 0
        return val

    def increment(self, k: int, val: int) -> None:
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.inc[idx] += val
```

## C

```c
#include <stdlib.h>

typedef struct {
    int maxSize;
    int top;
    int *stack;
    int *inc;
} CustomStack;

CustomStack* customStackCreate(int maxSize) {
    CustomStack* obj = (CustomStack*)malloc(sizeof(CustomStack));
    if (!obj) return NULL;
    obj->maxSize = maxSize;
    obj->top = -1;
    obj->stack = (int*)calloc(maxSize, sizeof(int));
    obj->inc   = (int*)calloc(maxSize, sizeof(int));
    return obj;
}

void customStackPush(CustomStack* obj, int x) {
    if (obj->top + 1 < obj->maxSize) {
        obj->top++;
        obj->stack[obj->top] = x;
    }
}

int customStackPop(CustomStack* obj) {
    if (obj->top == -1) return -1;
    int res = obj->stack[obj->top] + obj->inc[obj->top];
    if (obj->top > 0) {
        obj->inc[obj->top - 1] += obj->inc[obj->top];
    }
    obj->inc[obj->top] = 0;
    obj->top--;
    return res;
}

void customStackIncrement(CustomStack* obj, int k, int val) {
    if (obj->top == -1) return;
    int idx = k - 1;
    if (idx > obj->top) idx = obj->top;
    obj->inc[idx] += val;
}

void customStackFree(CustomStack* obj) {
    if (!obj) return;
    free(obj->stack);
    free(obj->inc);
    free(obj);
}
```

## Csharp

```csharp
public class CustomStack
{
    private readonly int[] _stack;
    private readonly int[] _inc;
    private int _top = -1;
    private readonly int _maxSize;

    public CustomStack(int maxSize)
    {
        _maxSize = maxSize;
        _stack = new int[maxSize];
        _inc = new int[maxSize];
    }

    public void Push(int x)
    {
        if (_top + 1 < _maxSize)
        {
            _top++;
            _stack[_top] = x;
        }
    }

    public int Pop()
    {
        if (_top == -1) return -1;

        int result = _stack[_top] + _inc[_top];
        if (_top > 0)
        {
            _inc[_top - 1] += _inc[_top];
        }
        _inc[_top] = 0;
        _top--;
        return result;
    }

    public void Increment(int k, int val)
    {
        int idx = Math.Min(k, _top + 1) - 1;
        if (idx >= 0)
        {
            _inc[idx] += val;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * obj.Increment(k,val);
 */
```

## Javascript

```javascript
/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    this.maxSize = maxSize;
    this.stack = new Array(maxSize);
    this.inc = new Array(maxSize).fill(0);
    this.size = 0;
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if (this.size < this.maxSize) {
        this.stack[this.size] = x;
        this.inc[this.size] = 0; // ensure inc at this position is reset
        this.size++;
    }
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    if (this.size === 0) return -1;
    const idx = this.size - 1;
    let val = this.stack[idx] + this.inc[idx];
    if (idx > 0) {
        this.inc[idx - 1] += this.inc[idx];
    }
    this.inc[idx] = 0; // clean up
    this.size--;
    return val;
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    const idx = Math.min(k, this.size) - 1;
    if (idx >= 0) {
        this.inc[idx] += val;
    }
};
```

## Typescript

```typescript
class CustomStack {
    private maxSize: number;
    private stack: number[];
    private inc: number[];
    private size: number = 0;

    constructor(maxSize: number) {
        this.maxSize = maxSize;
        this.stack = new Array(maxSize);
        this.inc = new Array(maxSize).fill(0);
    }

    push(x: number): void {
        if (this.size < this.maxSize) {
            this.stack[this.size] = x;
            // inc at this position is already 0 from initialization or previous use
            this.size++;
        }
    }

    pop(): number {
        if (this.size === 0) return -1;
        const idx = this.size - 1;
        let result = this.stack[idx] + this.inc[idx];
        if (idx > 0) {
            this.inc[idx - 1] += this.inc[idx];
        }
        this.inc[idx] = 0; // reset
        this.size--;
        return result;
    }

    increment(k: number, val: number): void {
        const idx = Math.min(k, this.size) - 1;
        if (idx >= 0) {
            this.inc[idx] += val;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */
```

## Php

```php
class CustomStack {
    private $maxSize;
    private $stack = [];
    private $inc = [];
    private $size = 0;

    /**
     * @param Integer $maxSize
     */
    public function __construct($maxSize) {
        $this->maxSize = $maxSize;
    }

    /**
     * @param Integer $x
     * @return NULL
     */
    public function push($x) {
        if ($this->size < $this->maxSize) {
            $this->stack[$this->size] = $x;
            $this->inc[$this->size] = 0;
            $this->size++;
        }
    }

    /**
     * @return Integer
     */
    public function pop() {
        if ($this->size == 0) {
            return -1;
        }
        $idx = $this->size - 1;
        $res = $this->stack[$idx] + $this->inc[$idx];
        if ($idx > 0) {
            $this->inc[$idx - 1] += $this->inc[$idx];
        }
        $this->inc[$idx] = 0;
        unset($this->stack[$idx]);
        $this->size--;
        return $res;
    }

    /**
     * @param Integer $k
     * @param Integer $val
     * @return NULL
     */
    public function increment($k, $val) {
        if ($this->size == 0) {
            return;
        }
        $index = min($k, $this->size) - 1;
        $this->inc[$index] += $val;
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * $obj = new CustomStack($maxSize);
 * $obj->push($x);
 * $ret_2 = $obj->pop();
 * $obj->increment($k, $val);
 */
```

## Swift

```swift
class CustomStack {
    private let capacity: Int
    private var stack: [Int]
    private var inc: [Int]
    private var size: Int = 0

    init(_ maxSize: Int) {
        self.capacity = maxSize
        self.stack = Array(repeating: 0, count: maxSize)
        self.inc = Array(repeating: 0, count: maxSize)
    }

    func push(_ x: Int) {
        if size < capacity {
            stack[size] = x
            inc[size] = 0
            size += 1
        }
    }

    func pop() -> Int {
        if size == 0 { return -1 }
        let idx = size - 1
        var result = stack[idx] + inc[idx]
        if idx > 0 {
            inc[idx - 1] += inc[idx]
        }
        inc[idx] = 0
        size -= 1
        return result
    }

    func increment(_ k: Int, _ val: Int) {
        let limit = min(k, size) - 1
        if limit >= 0 {
            inc[limit] += val
        }
    }
}
```

## Kotlin

```kotlin
class CustomStack(maxSize: Int) {
    private val stack = IntArray(maxSize)
    private val inc = IntArray(maxSize)
    private var size = 0

    fun push(x: Int) {
        if (size < stack.size) {
            stack[size] = x
            inc[size] = 0
            size++
        }
    }

    fun pop(): Int {
        if (size == 0) return -1
        val idx = size - 1
        var result = stack[idx] + inc[idx]
        if (idx > 0) {
            inc[idx - 1] += inc[idx]
        }
        inc[idx] = 0
        size--
        return result
    }

    fun increment(k: Int, `val`: Int) {
        val idx = kotlin.math.min(k, size) - 1
        if (idx >= 0) {
            inc[idx] += `val`
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * var obj = CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,`val`)
 */
```

## Dart

```dart
class CustomStack {
  final List<int> _stack;
  final List<int> _inc;
  final int _maxSize;
  int _size = 0;

  CustomStack(int maxSize)
      : _maxSize = maxSize,
        _stack = List.filled(maxSize, 0),
        _inc = List.filled(maxSize, 0);

  void push(int x) {
    if (_size < _maxSize) {
      _stack[_size] = x;
      _size++;
    }
  }

  int pop() {
    if (_size == 0) return -1;
    int idx = _size - 1;
    int result = _stack[idx] + _inc[idx];
    if (idx > 0) {
      _inc[idx - 1] += _inc[idx];
    }
    _inc[idx] = 0;
    _size--;
    return result;
  }

  void increment(int k, int val) {
    int limit = k < _size ? k : _size;
    if (limit > 0) {
      _inc[limit - 1] += val;
    }
  }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = CustomStack(maxSize);
 * obj.push(x);
 * int param2 = obj.pop();
 * obj.increment(k,val);
 */
```

## Golang

```go
type CustomStack struct {
	stack []int
	inc   []int
	top   int
	size  int
}

func Constructor(maxSize int) CustomStack {
	return CustomStack{
		stack: make([]int, maxSize),
		inc:   make([]int, maxSize),
		top:   -1,
		size:  maxSize,
	}
}

func (this *CustomStack) Push(x int) {
	if this.top+1 < this.size {
		this.top++
		this.stack[this.top] = x
	}
}

func (this *CustomStack) Pop() int {
	if this.top == -1 {
		return -1
	}
	val := this.stack[this.top] + this.inc[this.top]
	if this.top > 0 {
		this.inc[this.top-1] += this.inc[this.top]
	}
	this.inc[this.top] = 0
	this.top--
	return val
}

func (this *CustomStack) Increment(k int, val int) {
	if this.top == -1 {
		return
	}
	idx := k - 1
	if idx > this.top {
		idx = this.top
	}
	this.inc[idx] += val
}
```

## Ruby

```ruby
class CustomStack
  def initialize(max_size)
    @max = max_size
    @stack = Array.new(max_size, 0)
    @inc = Array.new(max_size, 0)
    @top = -1
  end

  def push(x)
    if @top + 1 < @max
      @top += 1
      @stack[@top] = x
    end
  end

  def pop()
    return -1 if @top == -1
    result = @stack[@top] + @inc[@top]
    if @top > 0
      @inc[@top - 1] += @inc[@top]
    end
    @inc[@top] = 0
    @top -= 1
    result
  end

  def increment(k, val)
    idx = [k, @top + 1].min - 1
    if idx >= 0
      @inc[idx] += val
    end
  end
end
```

## Scala

```scala
class CustomStack(_maxSize: Int) {
  private val maxSize = _maxSize
  private val stack = new Array[Int](maxSize)
  private val inc = new Array[Int](maxSize)
  private var top = -1

  def push(x: Int): Unit = {
    if (top + 1 < maxSize) {
      top += 1
      stack(top) = x
    }
  }

  def pop(): Int = {
    if (top == -1) return -1
    val res = stack(top) + inc(top)
    if (top > 0) {
      inc(top - 1) += inc(top)
    }
    inc(top) = 0
    top -= 1
    res
  }

  def increment(k: Int, `val`: Int): Unit = {
    if (top == -1) return
    val idx = math.min(k, top + 1) - 1
    inc(idx) += `val`
  }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * val obj = new CustomStack(maxSize)
 * obj.push(x)
 * val param_2 = obj.pop()
 * obj.increment(k,`val`)
 */
```

## Rust

```rust
struct CustomStack {
    max_size: usize,
    stack: Vec<i32>,
    inc: Vec<i32>,
}

impl CustomStack {
    fn new(maxSize: i32) -> Self {
        let size = maxSize as usize;
        CustomStack {
            max_size: size,
            stack: Vec::with_capacity(size),
            inc: vec![0; size],
        }
    }

    fn push(&mut self, x: i32) {
        if self.stack.len() < self.max_size {
            self.stack.push(x);
        }
    }

    fn pop(&mut self) -> i32 {
        match self.stack.len().checked_sub(1) {
            Some(idx) => {
                let inc_val = self.inc[idx];
                let mut result = self.stack.pop().unwrap() + inc_val;
                if idx > 0 {
                    self.inc[idx - 1] += inc_val;
                }
                self.inc[idx] = 0;
                result
            }
            None => -1,
        }
    }

    fn increment(&mut self, k: i32, val: i32) {
        let n = self.stack.len();
        if n == 0 {
            return;
        }
        let idx = std::cmp::min(k as usize, n) - 1;
        self.inc[idx] += val;
    }
}
```

## Racket

```racket
(define custom-stack%
  (class object%
    (init-field max-size)
    (super-new)

    ; internal storage
    (define stack (make-vector max-size 0))
    (define inc   (make-vector max-size 0))
    (define top -1)

    (define/public (push x)
      (when (< top (- max-size 1))
        (set! top (+ top 1))
        (vector-set! stack top x)))

    (define/public (pop)
      (if (= top -1)
          -1
          (let* ((val (vector-ref stack top))
                 (inc-val (vector-ref inc top))
                 (res (+ val inc-val)))
            (when (> top 0)
              (vector-set! inc (- top 1)
                           (+ (vector-ref inc (- top 1)) inc-val)))
            (vector-set! inc top 0)
            (set! top (- top 1))
            res)))

    (define/public (increment k val)
      (when (>= top 0)
        (let ((idx (min top (- k 1))))
          (vector-set! inc idx
                       (+ (vector-ref inc idx) val)))))))
```

## Erlang

```erlang
-module(customstack).
-export([custom_stack_init_/1,
         custom_stack_push/1,
         custom_stack_pop/0,
         custom_stack_increment/2]).

%% Initialize the stack with a maximum size.
-spec custom_stack_init_(MaxSize :: integer()) -> any().
custom_stack_init_(MaxSize) ->
    put(max_size, MaxSize),
    put(stack, []).

%% Push an element onto the stack if there is capacity.
-spec custom_stack_push(X :: integer()) -> any().
custom_stack_push(X) ->
    Stack = get(stack),
    Max   = get(max_size),
    case length(Stack) < Max of
        true  -> put(stack, Stack ++ [X]);
        false -> ok
    end.

%% Pop the top element; return -1 if empty.
-spec custom_stack_pop() -> integer().
custom_stack_pop() ->
    Stack = get(stack),
    case Stack of
        [] -> -1;
        _  ->
            {NewStack, Val} = pop_last(Stack),
            put(stack, NewStack),
            Val
    end.

%% Increment the bottom K elements by Val.
-spec custom_stack_increment(K :: integer(), Val :: integer()) -> any().
custom_stack_increment(K, Val) ->
    Stack = get(stack),
    Len   = length(Stack),
    Limit = erlang:min(K, Len),
    NewStack = increment_first(Limit, Val, Stack),
    put(stack, NewStack).

%% Helper: remove and return the last element of a list.
-spec pop_last([integer()]) -> {[integer()], integer()}.
pop_last([H]) ->
    {[], H};
pop_last([H|T]) ->
    {Rest, Last} = pop_last(T),
    {[H|Rest], Last}.

%% Helper: add Val to the first N elements of a list.
-spec increment_first(N :: non_neg_integer(), Val :: integer(), [integer()]) -> [integer()].
increment_first(0, _Val, List) ->
    List;
increment_first(_N, _Val, []) ->
    [];
increment_first(N, Val, [H|T]) when N > 0 ->
    [H + Val | increment_first(N - 1, Val, T)].
```

## Elixir

```elixir
defmodule CustomStack do
  @spec init_(max_size :: integer) :: any
  def init_(max_size) do
    stack = :array.new(max_size, default: 0)
    inc = :array.new(max_size, default: 0)
    Process.put(:stack_arr, stack)
    Process.put(:inc_arr, inc)
    Process.put(:top, -1)
    Process.put(:max_size, max_size)
    :ok
  end

  @spec push(x :: integer) :: any
  def push(x) do
    top = Process.get(:top)
    max = Process.get(:max_size)

    if top < max - 1 do
      new_top = top + 1
      stack = Process.get(:stack_arr) |> :array.set(new_top, x)
      Process.put(:stack_arr, stack)
      Process.put(:top, new_top)
    else
      :ok
    end
  end

  @spec pop() :: integer
  def pop() do
    top = Process.get(:top)

    if top < 0 do
      -1
    else
      stack = Process.get(:stack_arr)
      inc = Process.get(:inc_arr)

      val = :array.get(top, stack) + :array.get(top, inc)

      # propagate increment to the next element below
      if top > 0 do
        prev_inc = :array.get(top - 1, inc) + :array.get(top, inc)
        inc = :array.set(top - 1, prev_inc, inc)
      end

      # clear current increment slot
      inc = :array.set(top, 0, inc)

      Process.put(:inc_arr, inc)
      Process.put(:top, top - 1)
      val
    end
  end

  @spec increment(k :: integer, val :: integer) :: any
  def increment(k, val) do
    top = Process.get(:top)

    if top >= 0 do
      idx = min(k, top + 1) - 1
      inc = Process.get(:inc_arr)
      cur = :array.get(idx, inc)
      inc = :array.set(idx, cur + val, inc)
      Process.put(:inc_arr, inc)
    else
      :ok
    end
  end
end
```

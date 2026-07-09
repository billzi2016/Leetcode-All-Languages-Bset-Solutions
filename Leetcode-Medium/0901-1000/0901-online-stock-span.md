# 0901. Online Stock Span

## Cpp

```cpp
class StockSpanner {
public:
    StockSpanner() {
        // No initialization needed beyond the default constructor.
    }
    
    int next(int price) {
        int span = 1;
        while (!stk.empty() && stk.back().first <= price) {
            span += stk.back().second;
            stk.pop_back();
        }
        stk.emplace_back(price, span);
        return span;
    }

private:
    // Pair of (price, accumulated span)
    std::vector<std::pair<int,int>> stk;
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

class StockSpanner {
    private Deque<int[]> stack; // each element: [price, span]

    public StockSpanner() {
        stack = new ArrayDeque<>();
    }

    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peekLast()[0] <= price) {
            span += stack.pollLast()[1];
        }
        stack.addLast(new int[]{price, span});
        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */
```

## Python

```python
class StockSpanner(object):
    def __init__(self):
        self.stack = []  # each element is a tuple (price, span)

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
```

## Python3

```python
class StockSpanner:
    def __init__(self):
        self.stack = []  # each element is a tuple (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *prices;
    int *spans;
    int size;
    int cap;
} StockSpanner;

static void ensureCapacity(StockSpanner *obj) {
    if (obj->size >= obj->cap) {
        int newCap = obj->cap * 2;
        int *newPrices = (int *)realloc(obj->prices, newCap * sizeof(int));
        int *newSpans = (int *)realloc(obj->spans, newCap * sizeof(int));
        if (!newPrices || !newSpans) {
            // In case of allocation failure, keep original pointers (LeetCode won't test this)
            exit(1);
        }
        obj->prices = newPrices;
        obj->spans = newSpans;
        obj->cap = newCap;
    }
}

StockSpanner* stockSpannerCreate() {
    StockSpanner *obj = (StockSpanner *)malloc(sizeof(StockSpanner));
    if (!obj) return NULL;
    obj->cap = 1024;
    obj->size = 0;
    obj->prices = (int *)malloc(obj->cap * sizeof(int));
    obj->spans = (int *)malloc(obj->cap * sizeof(int));
    if (!obj->prices || !obj->spans) {
        free(obj->prices);
        free(obj->spans);
        free(obj);
        return NULL;
    }
    return obj;
}

int stockSpannerNext(StockSpanner* obj, int price) {
    int span = 1;
    while (obj->size > 0 && obj->prices[obj->size - 1] <= price) {
        span += obj->spans[obj->size - 1];
        obj->size--;
    }
    ensureCapacity(obj);
    obj->prices[obj->size] = price;
    obj->spans[obj->size] = span;
    obj->size++;
    return span;
}

void stockSpannerFree(StockSpanner* obj) {
    if (!obj) return;
    free(obj->prices);
    free(obj->spans);
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class StockSpanner
{
    private Stack<(int price, int span)> _stack;

    public StockSpanner()
    {
        _stack = new Stack<(int, int)>();
    }

    public int Next(int price)
    {
        int span = 1;
        while (_stack.Count > 0 && _stack.Peek().price <= price)
        {
            span += _stack.Pop().span;
        }
        _stack.Push((price, span));
        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.Next(price);
 */
```

## Javascript

```javascript
var StockSpanner = function() {
    this.stack = []; // each element is [price, span]
};

StockSpanner.prototype.next = function(price) {
    let span = 1;
    while (this.stack.length && this.stack[this.stack.length - 1][0] <= price) {
        span += this.stack.pop()[1];
    }
    this.stack.push([price, span]);
    return span;
};
```

## Typescript

```typescript
class StockSpanner {
    private stack: [number, number][] = [];

    constructor() {}

    next(price: number): number {
        let span = 1;
        while (this.stack.length && this.stack[this.stack.length - 1][0] <= price) {
            span += this.stack.pop()![1];
        }
        this.stack.push([price, span]);
        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */
```

## Php

```php
class StockSpanner {
    /**
     * @var array
     */
    private $stack;

    /**
     */
    function __construct() {
        $this->stack = [];
    }

    /**
     * @param Integer $price
     * @return Integer
     */
    function next($price) {
        $span = 1;
        while (!empty($this->stack) && end($this->stack)['price'] <= $price) {
            $top = array_pop($this->stack);
            $span += $top['span'];
        }
        $this->stack[] = ['price' => $price, 'span' => $span];
        return $span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * $obj = new StockSpanner();
 * $ret_1 = $obj->next($price);
 */
```

## Swift

```swift
class StockSpanner {
    private var stack: [(price: Int, span: Int)] = []
    
    init() {}
    
    func next(_ price: Int) -> Int {
        var span = 1
        while let last = stack.last, last.price <= price {
            span += last.span
            stack.removeLast()
        }
        stack.append((price, span))
        return span
    }
}
```

## Kotlin

```kotlin
class StockSpanner() {
    private val stack = java.util.ArrayDeque<IntArray>()

    fun next(price: Int): Int {
        var span = 1
        while (stack.isNotEmpty() && stack.peekLast()[0] <= price) {
            span += stack.removeLast()[1]
        }
        stack.addLast(intArrayOf(price, span))
        return span
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = StockSpanner()
 * var param_1 = obj.next(price)
 */
```

## Dart

```dart
class StockSpanner {
  final List<List<int>> _stack = [];

  StockSpanner() {}

  int next(int price) {
    int span = 1;
    while (_stack.isNotEmpty && _stack.last[0] <= price) {
      span += _stack.removeLast()[1];
    }
    _stack.add([price, span]);
    return span;
  }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = StockSpanner();
 * int param1 = obj.next(price);
 */
```

## Golang

```go
type pair struct {
	price int
	span  int
}

type StockSpanner struct {
	stack []pair
}

/** initialize your data structure here. */
func Constructor() StockSpanner {
	return StockSpanner{stack: make([]pair, 0)}
}

func (this *StockSpanner) Next(price int) int {
	span := 1
	for len(this.stack) > 0 && this.stack[len(this.stack)-1].price <= price {
		span += this.stack[len(this.stack)-1].span
		this.stack = this.stack[:len(this.stack)-1]
	}
	this.stack = append(this.stack, pair{price: price, span: span})
	return span
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
```

## Ruby

```ruby
class StockSpanner
  def initialize()
    @stack = []
  end

=begin
    :type price: Integer
    :rtype: Integer
=end
  def next(price)
    span = 1
    while !@stack.empty? && @stack[-1][0] <= price
      span += @stack.pop[1]
    end
    @stack << [price, span]
    span
  end
end
```

## Scala

```scala
import java.util.ArrayDeque

class StockSpanner() {

  private val stack = new ArrayDeque[(Int, Int)]()

  def next(price: Int): Int = {
    var span = 1
    while (!stack.isEmpty && stack.peek()._1 <= price) {
      val (_, s) = stack.pop()
      span += s
    }
    stack.push((price, span))
    span
  }

}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * val obj = new StockSpanner()
 * val param_1 = obj.next(price)
 */
```

## Rust

```rust
struct StockSpanner {
    stack: Vec<(i32, i32)>,
}

impl StockSpanner {
    fn new() -> Self {
        StockSpanner { stack: Vec::new() }
    }

    fn next(&mut self, price: i32) -> i32 {
        let mut span = 1;
        while let Some(&(prev_price, prev_span)) = self.stack.last() {
            if prev_price <= price {
                span += prev_span;
                self.stack.pop();
            } else {
                break;
            }
        }
        self.stack.push((price, span));
        span
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let mut obj = StockSpanner::new();
 * let ret_1: i32 = obj.next(price);
 */
```

## Racket

```racket
(define stock-spanner%
  (class object%
    (super-new)
    ;; stack of pairs: (price . span), top at the front of the list
    (define stack '())
    ;; next : exact-integer? -> exact-integer?
    (define/public (next price)
      (let loop ((span 1))
        (if (and (pair? stack) (<= (car (car stack)) price))
            (begin
              (set! span (+ span (cdr (car stack))))
              (set! stack (cdr stack))
              (loop span))
            (begin
              (set! stack (cons (cons price span) stack))
              span))))))
```

## Erlang

```erlang
-define(STACK_KEY, stock_span_stack).

-spec stock_spanner_init_() -> any().
stock_spanner_init_() ->
    put(?STACK_KEY, []),
    ok.

-spec stock_spanner_next(Price :: integer()) -> integer().
stock_spanner_next(Price) when is_integer(Price) ->
    Stack = get(?STACK_KEY),
    {Span, NewStack} = compute_span(Price, Stack, 1),
    put(?STACK_KEY, NewStack),
    Span.

-spec compute_span(integer(), [{integer(), integer()}], integer()) -> {integer(), [{integer(), integer()}]}.
compute_span(_Price, [], AccSpan) ->
    {AccSpan, [{_Price, AccSpan}]};
compute_span(Price, [{TopPrice, TopSpan} | Rest], AccSpan) when TopPrice =< Price ->
    compute_span(Price, Rest, AccSpan + TopSpan);
compute_span(Price, StackRest, AccSpan) ->
    NewStack = [{Price, AccSpan} | StackRest],
    {AccSpan, NewStack}.
```

## Elixir

```elixir
defmodule StockSpanner do
  @spec init_() :: any
  def init_() do
    Process.put(:stack, [])
    :ok
  end

  @spec next(price :: integer) :: integer
  def next(price) do
    stack = Process.get(:stack, [])
    {span, remaining_stack} = pop_and_compute(price, stack, 1)
    Process.put(:stack, [{price, span} | remaining_stack])
    span
  end

  defp pop_and_compute(_price, [], acc), do: {acc, []}

  defp pop_and_compute(price, [{prev_price, prev_span} | rest], acc) when price >= prev_price do
    pop_and_compute(price, rest, acc + prev_span)
  end

  defp pop_and_compute(_price, stack, acc), do: {acc, stack}
end
```

# 0895. Maximum Frequency Stack

## Cpp

```cpp
class FreqStack {
public:
    FreqStack() : maxFreq(0) {}
    
    void push(int val) {
        int f = ++freq[val];
        if (f > maxFreq) maxFreq = f;
        group[f].push_back(val);
    }
    
    int pop() {
        int val = group[maxFreq].back();
        group[maxFreq].pop_back();
        --freq[val];
        if (group[maxFreq].empty()) {
            --maxFreq;
        }
        return val;
    }

private:
    int maxFreq;
    std::unordered_map<int, int> freq;
    std::unordered_map<int, std::vector<int>> group;
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
```

## Java

```java
class FreqStack {
    private java.util.Map<Integer, Integer> freq;
    private java.util.Map<Integer, java.util.ArrayDeque<Integer>> group;
    private int maxFreq;

    public FreqStack() {
        freq = new java.util.HashMap<>();
        group = new java.util.HashMap<>();
        maxFreq = 0;
    }

    public void push(int val) {
        int f = freq.getOrDefault(val, 0) + 1;
        freq.put(val, f);
        if (f > maxFreq) {
            maxFreq = f;
        }
        group.computeIfAbsent(f, k -> new java.util.ArrayDeque<>()).push(val);
    }

    public int pop() {
        java.util.ArrayDeque<Integer> stack = group.get(maxFreq);
        int val = stack.pop();
        int f = freq.get(val) - 1;
        if (f == 0) {
            freq.remove(val);
        } else {
            freq.put(val, f);
        }
        if (stack.isEmpty()) {
            maxFreq--;
        }
        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */
```

## Python

```python
import collections

class FreqStack(object):
    def __init__(self):
        self.freq = {}
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```

## Python3

```python
class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val
```

## C

```c
#include <stdlib.h>
#include "uthash.h"

typedef struct {
    int val;
    int freq;
    UT_hash_handle hh;
} ValFreq;

typedef struct {
    int freq;
    int *vals;
    int size;
    int capacity;
    UT_hash_handle hh;
} FreqNode;

typedef struct {
    ValFreq *valMap;   // value -> frequency
    FreqNode *freqMap; // frequency -> stack of values
    int maxFreq;
} FreqStack;

FreqStack* freqStackCreate() {
    FreqStack *obj = (FreqStack*)malloc(sizeof(FreqStack));
    obj->valMap = NULL;
    obj->freqMap = NULL;
    obj->maxFreq = 0;
    return obj;
}

void freqStackPush(FreqStack* obj, int val) {
    ValFreq *vf;
    HASH_FIND_INT(obj->valMap, &val, vf);
    if (!vf) {
        vf = (ValFreq*)malloc(sizeof(ValFreq));
        vf->val = val;
        vf->freq = 1;
        HASH_ADD_INT(obj->valMap, val, vf);
    } else {
        vf->freq++;
    }
    int f = vf->freq;
    if (f > obj->maxFreq) obj->maxFreq = f;

    FreqNode *fn;
    HASH_FIND_INT(obj->freqMap, &f, fn);
    if (!fn) {
        fn = (FreqNode*)malloc(sizeof(FreqNode));
        fn->freq = f;
        fn->capacity = 4;
        fn->size = 0;
        fn->vals = (int*)malloc(fn->capacity * sizeof(int));
        HASH_ADD_INT(obj->freqMap, freq, fn);
    }
    if (fn->size == fn->capacity) {
        fn->capacity <<= 1;
        fn->vals = (int*)realloc(fn->vals, fn->capacity * sizeof(int));
    }
    fn->vals[fn->size++] = val;
}

int freqStackPop(FreqStack* obj) {
    int f = obj->maxFreq;
    FreqNode *fn;
    HASH_FIND_INT(obj->freqMap, &f, fn);
    int idx = fn->size - 1;
    int val = fn->vals[idx];
    fn->size--;

    ValFreq *vf;
    HASH_FIND_INT(obj->valMap, &val, vf);
    if (vf) {
        vf->freq--;
        if (vf->freq == 0) {
            HASH_DEL(obj->valMap, vf);
            free(vf);
        }
    }

    if (fn->size == 0) {
        HASH_DEL(obj->freqMap, fn);
        free(fn->vals);
        free(fn);
        obj->maxFreq--;
    }
    return val;
}

void freqStackFree(FreqStack* obj) {
    ValFreq *vf, *tmpVf;
    HASH_ITER(hh, obj->valMap, vf, tmpVf) {
        HASH_DEL(obj->valMap, vf);
        free(vf);
    }
    FreqNode *fn, *tmpFn;
    HASH_ITER(hh, obj->freqMap, fn, tmpFn) {
        HASH_DEL(obj->freqMap, fn);
        free(fn->vals);
        free(fn);
    }
    free(obj);
}

/**
 * Your FreqStack struct will be instantiated and called as such:
 * FreqStack* obj = freqStackCreate();
 * freqStackPush(obj, val);
 *
 * int param_2 = freqStackPop(obj);
 *
 * freqStackFree(obj);
 */
```

## Csharp

```csharp
using System.Collections.Generic;

public class FreqStack {
    private Dictionary<int, int> _freq;
    private Dictionary<int, Stack<int>> _group;
    private int _maxFreq;

    public FreqStack() {
        _freq = new Dictionary<int, int>();
        _group = new Dictionary<int, Stack<int>>();
        _maxFreq = 0;
    }
    
    public void Push(int val) {
        int f = 1;
        if (_freq.TryGetValue(val, out var cur)) {
            f = cur + 1;
        }
        _freq[val] = f;

        if (!_group.ContainsKey(f)) {
            _group[f] = new Stack<int>();
        }
        _group[f].Push(val);

        if (f > _maxFreq) {
            _maxFreq = f;
        }
    }
    
    public int Pop() {
        var stack = _group[_maxFreq];
        int val = stack.Pop();
        _freq[val]--;

        if (stack.Count == 0) {
            _maxFreq--;
        }

        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.Push(val);
 * int param_2 = obj.Pop();
 */
```

## Javascript

```javascript
var FreqStack = function() {
    this.freq = new Map();      // value -> frequency
    this.group = new Map();     // frequency -> stack of values
    this.maxFreq = 0;
};

/** 
 * @param {number} val
 * @return {void}
 */
FreqStack.prototype.push = function(val) {
    const f = (this.freq.get(val) || 0) + 1;
    this.freq.set(val, f);
    if (!this.group.has(f)) this.group.set(f, []);
    this.group.get(f).push(val);
    if (f > this.maxFreq) this.maxFreq = f;
};

/**
 * @return {number}
 */
FreqStack.prototype.pop = function() {
    const stack = this.group.get(this.maxFreq);
    const val = stack.pop();
    const f = this.freq.get(val) - 1;
    if (f === 0) this.freq.delete(val);
    else this.freq.set(val, f);
    if (stack.length === 0) {
        this.group.delete(this.maxFreq);
        this.maxFreq--;
    }
    return val;
};
```

## Typescript

```typescript
class FreqStack {
    private freq: Map<number, number>;
    private group: Map<number, number[]>;
    private maxFreq: number;

    constructor() {
        this.freq = new Map();
        this.group = new Map();
        this.maxFreq = 0;
    }

    push(val: number): void {
        const f = (this.freq.get(val) ?? 0) + 1;
        this.freq.set(val, f);
        if (!this.group.has(f)) {
            this.group.set(f, []);
        }
        this.group.get(f)!.push(val);
        if (f > this.maxFreq) {
            this.maxFreq = f;
        }
    }

    pop(): number {
        const stack = this.group.get(this.maxFreq)!;
        const val = stack.pop()!;
        const newF = this.freq.get(val)! - 1;
        if (newF === 0) {
            this.freq.delete(val);
        } else {
            this.freq.set(val, newF);
        }
        if (stack.length === 0) {
            this.group.delete(this.maxFreq);
            this.maxFreq--;
        }
        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(val)
 * var param_2 = obj.pop()
 */
```

## Php

```php
class FreqStack {
    private array $freq;
    private array $group;
    private int $maxFreq;

    function __construct() {
        $this->freq = [];
        $this->group = [];
        $this->maxFreq = 0;
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val) {
        if (!isset($this->freq[$val])) {
            $this->freq[$val] = 0;
        }
        $this->freq[$val]++;
        $f = $this->freq[$val];
        if (!isset($this->group[$f])) {
            $this->group[$f] = [];
        }
        $this->group[$f][] = $val; // push onto stack for this frequency
        if ($f > $this->maxFreq) {
            $this->maxFreq = $f;
        }
    }

    /**
     * @return Integer
     */
    function pop() {
        $val = array_pop($this->group[$this->maxFreq]);
        $this->freq[$val]--;
        if (empty($this->group[$this->maxFreq])) {
            $this->maxFreq--;
        }
        return $val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * $obj = new FreqStack();
 * $obj->push($val);
 * $ret_2 = $obj->pop();
 */
```

## Swift

```swift
class FreqStack {
    private var freq: [Int:Int] = [:]
    private var group: [Int:[Int]] = [:]
    private var maxFreq: Int = 0

    init() { }

    func push(_ val: Int) {
        let f = (freq[val] ?? 0) + 1
        freq[val] = f
        if group[f] == nil { group[f] = [] }
        group[f]!.append(val)
        if f > maxFreq { maxFreq = f }
    }

    func pop() -> Int {
        var stack = group[maxFreq]!
        let val = stack.removeLast()
        group[maxFreq] = stack
        freq[val]! -= 1
        if group[maxFreq]?.isEmpty ?? true {
            maxFreq -= 1
        }
        return val
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * let obj = FreqStack()
 * obj.push(val)
 * let ret_2: Int = obj.pop()
 */
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import java.util.HashMap

class FreqStack() {
    private val freqMap = HashMap<Int, Int>()
    private val group = HashMap<Int, ArrayDeque<Int>>()
    private var maxFreq = 0

    fun push(`val`: Int) {
        val f = (freqMap[`val`] ?: 0) + 1
        freqMap[`val`] = f
        if (f > maxFreq) maxFreq = f
        group.getOrPut(f) { ArrayDeque() }.addLast(`val`)
    }

    fun pop(): Int {
        val stack = group[maxFreq]!!
        val v = stack.removeLast()
        val newF = freqMap[v]!! - 1
        if (newF == 0) {
            freqMap.remove(v)
        } else {
            freqMap[v] = newF
        }
        if (stack.isEmpty()) {
            group.remove(maxFreq)
            maxFreq--
        }
        return v
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * var obj = FreqStack()
 * obj.push(`val`)
 * var param_2 = obj.pop()
 */
```

## Dart

```dart
class FreqStack {
  final Map<int, int> _freq = {};
  final Map<int, List<int>> _group = {};
  int _maxFreq = 0;

  FreqStack();

  void push(int val) {
    int f = (_freq[val] ?? 0) + 1;
    _freq[val] = f;
    if (f > _maxFreq) _maxFreq = f;
    _group.putIfAbsent(f, () => <int>[]).add(val);
  }

  int pop() {
    List<int> stack = _group[_maxFreq]!;
    int val = stack.removeLast();
    _freq[val] = _freq[val]! - 1;
    if (stack.isEmpty) {
      _group.remove(_maxFreq);
      _maxFreq--;
    }
    return val;
  }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = FreqStack();
 * obj.push(val);
 * int param2 = obj.pop();
 */
```

## Golang

```go
type FreqStack struct {
	freq    map[int]int
	group   map[int][]int
	maxFreq int
}

func Constructor() FreqStack {
	return FreqStack{
		freq:  make(map[int]int),
		group: make(map[int][]int),
	}
}

func (this *FreqStack) Push(val int) {
	this.freq[val]++
	f := this.freq[val]
	if f > this.maxFreq {
		this.maxFreq = f
	}
	this.group[f] = append(this.group[f], val)
}

func (this *FreqStack) Pop() int {
	stack := this.group[this.maxFreq]
	n := len(stack)
	val := stack[n-1]
	this.group[this.maxFreq] = stack[:n-1]
	this.freq[val]--
	if len(this.group[this.maxFreq]) == 0 {
		this.maxFreq--
	}
	return val
}
```

## Ruby

```ruby
class FreqStack
  def initialize()
    @freq = Hash.new(0)
    @group = Hash.new { |h, k| h[k] = [] }
    @maxfreq = 0
  end

=begin
  :type val: Integer
  :rtype: Void
=end
  def push(val)
    f = (@freq[val] += 1)
    @group[f] << val
    @maxfreq = f if f > @maxfreq
  end

=begin
  :rtype: Integer
=end
  def pop()
    val = @group[@maxfreq].pop
    @freq[val] -= 1
    @maxfreq -= 1 if @group[@maxfreq].empty?
    val
  end
end
```

## Scala

```scala
class FreqStack() {
    private val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
    private val group = scala.collection.mutable.Map[Int, scala.collection.mutable.Stack[Int]]()
    private var maxFreq = 0

    def push(`val`: Int): Unit = {
        val f = freq(`val`) + 1
        freq(`val`) = f
        if (f > maxFreq) maxFreq = f
        val stack = group.getOrElseUpdate(f, scala.collection.mutable.Stack[Int]())
        stack.push(`val`)
    }

    def pop(): Int = {
        val stack = group(maxFreq)
        val v = stack.pop()
        freq(v) -= 1
        if (stack.isEmpty) maxFreq -= 1
        v
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * val obj = new FreqStack()
 * obj.push(`val`)
 * val param_2 = obj.pop()
 */
```

## Rust

```rust
use std::collections::HashMap;

struct FreqStack {
    freq: HashMap<i32, usize>,
    group: HashMap<usize, Vec<i32>>,
    maxfreq: usize,
}

impl FreqStack {
    fn new() -> Self {
        FreqStack {
            freq: HashMap::new(),
            group: HashMap::new(),
            maxfreq: 0,
        }
    }

    fn push(&mut self, val: i32) {
        let f = self.freq.entry(val).or_insert(0);
        *f += 1;
        let freq_val = *f;
        self.group.entry(freq_val).or_insert_with(Vec::new).push(val);
        if freq_val > self.maxfreq {
            self.maxfreq = freq_val;
        }
    }

    fn pop(&mut self) -> i32 {
        // It's guaranteed that there is at least one element.
        let stack = self.group.get_mut(&self.maxfreq).unwrap();
        let val = stack.pop().unwrap();

        // Decrease frequency count for the popped value
        if let Some(cnt) = self.freq.get_mut(&val) {
            *cnt -= 1;
            if *cnt == 0 {
                self.freq.remove(&val);
            }
        }

        // If no more elements at current max frequency, decrease maxfreq
        if stack.is_empty() {
            self.group.remove(&self.maxfreq);
            if self.maxfreq > 0 {
                self.maxfreq -= 1;
            }
        }

        val
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * let mut obj = FreqStack::new();
 * obj.push(val);
 * let ret_2: i32 = obj.pop();
 */
```

## Racket

```racket
(define freq-stack%
  (class object%
    (super-new)
    
    (define freq (make-hash))          ; val -> count
    (define group (make-hash))         ; count -> list of vals (stack order)
    (define maxfreq 0)                 ; current maximum frequency
    
    ;; push : exact-integer? -> void?
    (define/public (push val)
      (let* ([newcnt (+ 1 (hash-ref freq val 0))]
             [_ (hash-set! freq val newcnt)]
             [lst (hash-ref group newcnt '())]
             [_ (hash-set! group newcnt (cons val lst))])
        (when (> newcnt maxfreq)
          (set! maxfreq newcnt))))
    
    ;; pop : -> exact-integer?
    (define/public (pop)
      (let* ([lst (hash-ref group maxfreq)]
             [val (car lst)])
        ;; update group for current max frequency
        (if (null? (cdr lst))
            (begin
              (hash-remove! group maxfreq)
              (set! maxfreq (- maxfreq 1)))
            (hash-set! group maxfreq (cdr lst)))
        ;; decrement frequency of popped value
        (let ([cnt (hash-ref freq val)])
          (if (= cnt 1)
              (hash-remove! freq val)
              (hash-set! freq val (- cnt 1))))
        val))
    ))
```

## Erlang

```erlang
-module(solution).
-export([freq_stack_init_/0, freq_stack_push/1, freq_stack_pop/0]).

%% Initialize the data structures.
-spec freq_stack_init_() -> any().
freq_stack_init_() ->
    put(freq_map, #{}),
    put(group_map, #{}),
    put(max_freq, 0).

%% Push a value onto the stack.
-spec freq_stack_push(Val :: integer()) -> any().
freq_stack_push(Val) ->
    FreqMap = get(freq_map),
    CurrFreq = maps:get(Val, FreqMap, 0) + 1,
    NewFreqMap = maps:put(Val, CurrFreq, FreqMap),
    put(freq_map, NewFreqMap),

    GroupMap = get(group_map),
    StackForFreq = maps:get(CurrFreq, GroupMap, []),
    NewStack = [Val | StackForFreq],
    NewGroupMap = maps:put(CurrFreq, NewStack, GroupMap),
    put(group_map, NewGroupMap),

    MaxFreq = get(max_freq),
    case CurrFreq > MaxFreq of
        true -> put(max_freq, CurrFreq);
        false -> ok
    end,
    ok.

%% Pop the most frequent element.
-spec freq_stack_pop() -> integer().
freq_stack_pop() ->
    MaxFreq = get(max_freq),

    GroupMap = get(group_map),
    [Val | RestStack] = maps:get(MaxFreq, GroupMap),

    NewGroupMap =
        case RestStack of
            [] -> maps:remove(MaxFreq, GroupMap);
            _  -> maps:put(MaxFreq, RestStack, GroupMap)
        end,
    put(group_map, NewGroupMap),

    FreqMap = get(freq_map),
    CurrFreq = maps:get(Val, FreqMap),
    NewFreqMap =
        case CurrFreq of
            1 -> maps:remove(Val, FreqMap);
            _ -> maps:put(Val, CurrFreq - 1, FreqMap)
        end,
    put(freq_map, NewFreqMap),

    %% Adjust max frequency if needed.
    case maps:is_key(MaxFreq, NewGroupMap) of
        true -> ok;
        false -> put(max_freq, MaxFreq - 1)
    end,

    Val.
```

## Elixir

```elixir
defmodule FreqStack do
  @spec init_() :: any
  def init_() do
    Agent.start_link(fn -> %{freq: %{}, group: %{}, max_freq: 0} end, name: __MODULE__)
  end

  @spec push(val :: integer) :: any
  def push(val) do
    Agent.update(__MODULE__, fn state ->
      freq = Map.update(state.freq, val, 1, &(&1 + 1))
      f = freq[val]
      max_freq = if f > state.max_freq, do: f, else: state.max_freq
      group = Map.update(state.group, f, [val], &[val | &1])
      %{state | freq: freq, group: group, max_freq: max_freq}
    end)
  end

  @spec pop() :: integer
  def pop() do
    Agent.get_and_update(__MODULE__, fn state ->
      stack = Map.fetch!(state.group, state.max_freq)
      [val | rest] = stack

      new_group =
        if rest == [] do
          Map.delete(state.group, state.max_freq)
        else
          Map.put(state.group, state.max_freq, rest)
        end

      new_freq = Map.update!(state.freq, val, &(&1 - 1))

      new_max_freq =
        if Map.has_key?(new_group, state.max_freq) do
          state.max_freq
        else
          state.max_freq - 1
        end

      {val, %{state | freq: new_freq, group: new_group, max_freq: new_max_freq}}
    end)
  end
end
```

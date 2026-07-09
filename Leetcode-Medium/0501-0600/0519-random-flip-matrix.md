# 0519. Random Flip Matrix

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int m, n;
    int remaining;
    unordered_map<int, int> mp;
    mt19937 rng;
    
    Solution(int m, int n) : m(m), n(n), remaining(m * n), rng(random_device{}()) {}
    
    vector<int> flip() {
        uniform_int_distribution<int> dist(0, remaining - 1);
        int r = dist(rng);
        
        int idx = mp.count(r) ? mp[r] : r;
        int last = remaining - 1;
        int lastVal = mp.count(last) ? mp[last] : last;
        mp[r] = lastVal;
        --remaining;
        return {idx / n, idx % n};
    }
    
    void reset() {
        mp.clear();
        remaining = m * n;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(m, n);
 * vector<int> param_1 = obj->flip();
 * obj->reset();
 */
```

## Java

```java
import java.util.HashMap;
import java.util.Random;

class Solution {
    private int m;
    private int n;
    private int total;
    private HashMap<Integer, Integer> map;
    private Random rand;

    public Solution(int m, int n) {
        this.m = m;
        this.n = n;
        this.map = new HashMap<>();
        this.rand = new Random();
        reset();
    }

    public int[] flip() {
        int r = rand.nextInt(total);
        int idx = map.getOrDefault(r, r);
        total--;
        int lastIdx = map.getOrDefault(total, total);
        map.put(r, lastIdx);
        return new int[]{idx / n, idx % n};
    }

    public void reset() {
        map.clear();
        total = m * n;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(m, n);
 * int[] param_1 = obj.flip();
 * obj.reset();
 */
```

## Python

```python
import random

class Solution(object):
    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.remain = self.total
        self.mapping = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        # pick a random index among the remaining positions
        idx = random.randint(0, self.remain - 1)
        # get the actual position for this index
        pos = self.mapping.get(idx, idx)

        # map the chosen index to the last available position
        last = self.remain - 1
        self.mapping[idx] = self.mapping.get(last, last)

        # decrease remaining count
        self.remain -= 1

        return [pos // self.n, pos % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.remain = self.total
        self.mapping.clear()
```

## Python3

```python
import random
from typing import List

class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.mapping = {}

    def flip(self) -> List[int]:
        # pick a random index among the remaining zeros
        idx = random.randint(0, self.total - 1)
        # actual position to return
        pos = self.mapping.get(idx, idx)

        # move the last available position into the spot of idx
        last = self.total - 1
        self.mapping[idx] = self.mapping.get(last, last)

        # decrease count of remaining zeros
        self.total -= 1

        return [pos // self.n, pos % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.mapping.clear()
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int key;
    int val;
    char used;
} Entry;

typedef struct {
    int m;
    int n;
    int total;          // remaining zero cells
    int capacity;       // size of hashmap (power of two)
    Entry *map;         // simple open-addressing hashmap
} Solution;

/* hash function for non‑negative integers */
static unsigned int hash_key(unsigned int key, unsigned int mask) {
    return (key * 2654435761u) & mask;
}

/* set mapping key -> val in hashmap */
static void map_set(Solution *obj, int key, int val) {
    unsigned int idx = hash_key((unsigned int)key, (unsigned int)(obj->capacity - 1));
    while (obj->map[idx].used) {
        if (obj->map[idx].key == key) {
            obj->map[idx].val = val;
            return;
        }
        idx = (idx + 1) & (obj->capacity - 1);
    }
    obj->map[idx].used = 1;
    obj->map[idx].key = key;
    obj->map[idx].val = val;
}

/* get mapping for key; returns -1 if not present */
static int map_get(Solution *obj, int key) {
    unsigned int idx = hash_key((unsigned int)key, (unsigned int)(obj->capacity - 1));
    while (obj->map[idx].used) {
        if (obj->map[idx].key == key)
            return obj->map[idx].val;
        idx = (idx + 1) & (obj->capacity - 1);
    }
    return -1;
}

/* clear hashmap */
static void map_clear(Solution *obj) {
    memset(obj->map, 0, sizeof(Entry) * obj->capacity);
}

Solution* solutionCreate(int m, int n) {
    Solution *obj = (Solution *)malloc(sizeof(Solution));
    obj->m = m;
    obj->n = n;
    obj->total = m * n;

    /* capacity >= 2 * max possible entries (1000), choose power of two */
    int cap = 1;
    while (cap < 2048) cap <<= 1;   // 2048 is enough for load factor <=0.5
    obj->capacity = cap;
    obj->map = (Entry *)malloc(sizeof(Entry) * obj->capacity);
    memset(obj->map, 0, sizeof(Entry) * obj->capacity);
    return obj;
}

int* solutionFlip(Solution* obj, int* retSize) {
    int r = rand() % obj->total;               // random index in [0, total-1]
    int val = map_get(obj, r);
    if (val == -1) val = r;                    // actual cell index

    int lastIdx = obj->total - 1;
    int lastVal = map_get(obj, lastIdx);
    if (lastVal == -1) lastVal = lastIdx;

    /* move the last element into position r */
    map_set(obj, r, lastVal);

    obj->total--;

    int *res = (int *)malloc(2 * sizeof(int));
    res[0] = val / obj->n;   // row
    res[1] = val % obj->n;   // col
    *retSize = 2;
    return res;
}

void solutionReset(Solution* obj) {
    obj->total = obj->m * obj->n;
    map_clear(obj);
}

void solutionFree(Solution* obj) {
    if (obj) {
        free(obj->map);
        free(obj);
    }
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(m, n);
 * int* param_1 = solutionFlip(obj, retSize);
 *
 * solutionReset(obj);
 *
 * solutionFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private readonly int rows;
    private readonly int cols;
    private readonly int total;
    private int remaining;
    private readonly Random rand;
    private readonly Dictionary<int, int> map;

    public Solution(int m, int n) {
        rows = m;
        cols = n;
        total = m * n;
        remaining = total;
        rand = new Random();
        map = new Dictionary<int, int>();
    }

    public int[] Flip() {
        int x = rand.Next(remaining);
        int idx = map.ContainsKey(x) ? map[x] : x;

        remaining--;
        int last = map.ContainsKey(remaining) ? map[remaining] : remaining;
        map[x] = last;

        return new int[] { idx / cols, idx % cols };
    }

    public void Reset() {
        map.Clear();
        remaining = total;
    }
}
```

## Javascript

```javascript
var Solution = function(m, n) {
    this.m = m;
    this.n = n;
    this.total = m * n;
    this.remain = this.total;
    this.map = new Map();
};

Solution.prototype.flip = function() {
    const x = Math.floor(Math.random() * this.remain);
    const idx = this.map.has(x) ? this.map.get(x) : x;
    const lastIdx = this.remain - 1;
    const last = this.map.has(lastIdx) ? this.map.get(lastIdx) : lastIdx;
    this.map.set(x, last);
    this.remain--;
    return [Math.floor(idx / this.n), idx % this.n];
};

Solution.prototype.reset = function() {
    this.remain = this.total;
    this.map.clear();
};
```

## Typescript

```typescript
class Solution {
    private m: number;
    private n: number;
    private remaining: number;
    private map: Map<number, number>;

    constructor(m: number, n: number) {
        this.m = m;
        this.n = n;
        this.remaining = m * n;
        this.map = new Map();
    }

    flip(): number[] {
        const randIdx = Math.floor(Math.random() * this.remaining);
        const actualIdx = this.map.has(randIdx) ? this.map.get(randIdx)! : randIdx;

        const lastIdx = this.remaining - 1;
        const lastMapped = this.map.has(lastIdx) ? this.map.get(lastIdx)! : lastIdx;
        this.map.set(randIdx, lastMapped);

        this.remaining--;

        return [Math.floor(actualIdx / this.n), actualIdx % this.n];
    }

    reset(): void {
        this.remaining = this.m * this.n;
        this.map.clear();
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(m, n)
 * var param_1 = obj.flip()
 * obj.reset()
 */
```

## Php

```php
class Solution {
    private $m;
    private $n;
    private $total;
    private $remaining;
    private $map;

    /**
     * @param Integer $m
     * @param Integer $n
     */
    function __construct($m, $n) {
        $this->m = $m;
        $this->n = $n;
        $this->total = $m * $n;
        $this->remaining = $this->total;
        $this->map = [];
    }

    /**
     * @return Integer[]
     */
    function flip() {
        // pick a random index among the remaining positions
        $randIdx = mt_rand(0, $this->remaining - 1);

        // get the actual position this index maps to
        if (isset($this->map[$randIdx])) {
            $actual = $this->map[$randIdx];
        } else {
            $actual = $randIdx;
        }

        // move the last available index into the place of the used one
        $lastIdx = $this->remaining - 1;
        if ($randIdx != $lastIdx) {
            if (isset($this->map[$lastIdx])) {
                $lastVal = $this->map[$lastIdx];
            } else {
                $lastVal = $lastIdx;
            }
            $this->map[$randIdx] = $lastVal;
        }

        // decrease the count of remaining zeros
        $this->remaining--;

        // convert linear index to 2D coordinates
        $row = intdiv($actual, $this->n);
        $col = $actual % $this->n;

        return [$row, $col];
    }

    /**
     * @return NULL
     */
    function reset() {
        $this->remaining = $this->total;
        $this->map = [];
        // explicit null return for clarity
        return null;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = new Solution($m, $n);
 * $ret_1 = $obj->flip();
 * $obj->reset();
 */
```

## Swift

```swift
class Solution {
    private let m: Int
    private let n: Int
    private var total: Int
    private var map: [Int: Int]

    init(_ m: Int, _ n: Int) {
        self.m = m
        self.n = n
        self.total = m * n
        self.map = [:]
    }

    func flip() -> [Int] {
        let randIdx = Int.random(in: 0..<total)
        let actualIdx = map[randIdx] ?? randIdx

        total -= 1
        let lastIdx = map[total] ?? total
        map[randIdx] = lastIdx
        // Optional cleanup: remove mapping for the moved-from position if it existed
        if let _ = map[total] {
            map.removeValue(forKey: total)
        }

        let row = actualIdx / n
        let col = actualIdx % n
        return [row, col]
    }

    func reset() {
        total = m * n
        map.removeAll()
    }
}
```

## Kotlin

```kotlin
class Solution(private val m: Int, private val n: Int) {
    private val total = m * n
    private var remaining = total
    private val map = HashMap<Int, Int>()
    private val rand = java.util.Random()

    fun flip(): IntArray {
        val x = rand.nextInt(remaining)
        val idx = map.getOrDefault(x, x)
        remaining--
        val last = map.getOrDefault(remaining, remaining)
        map[x] = last
        return intArrayOf(idx / n, idx % n)
    }

    fun reset() {
        map.clear()
        remaining = total
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  final int _m;
  final int _n;
  int _total;
  final Map<int, int> _map = {};
  final Random _rand = Random();

  Solution(this._m, this._n) : _total = _m * _n;

  List<int> flip() {
    int r = _rand.nextInt(_total);
    int idx = _map.containsKey(r) ? _map[r]! : r;

    int last = _total - 1;
    int lastVal = _map.containsKey(last) ? _map[last]! : last;
    _map[r] = lastVal;

    _total--;
    return [idx ~/ _n, idx % _n];
  }

  void reset() {
    _map.clear();
    _total = _m * _n;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(m, n);
 * List<int> param1 = obj.flip();
 * obj.reset();
 */
```

## Golang

```go
package main

import (
	"math/rand"
	"time"
)

type Solution struct {
	m, n   int
	total  int
	mapping map[int]int
}

func Constructor(m int, n int) Solution {
	rand.Seed(time.Now().UnixNano())
	return Solution{
		m:       m,
		n:       n,
		total:   m * n,
		mapping: make(map[int]int),
	}
}

func (this *Solution) Flip() []int {
	if this.total == 0 {
		return nil
	}
	idx := rand.Intn(this.total)
	// actual position for idx
	val, ok := this.mapping[idx]
	var actual int
	if ok {
		actual = val
	} else {
		actual = idx
	}
	// map idx to the last available element
	lastIdx := this.total - 1
	lastVal, okLast := this.mapping[lastIdx]
	if okLast {
		this.mapping[idx] = lastVal
	} else {
		this.mapping[idx] = lastIdx
	}
	this.total--
	return []int{actual / this.n, actual % this.n}
}

func (this *Solution) Reset() {
	this.total = this.m * this.n
	this.mapping = make(map[int]int)
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(m, n);
 * param_1 := obj.Flip();
 * obj.Reset();
 */
```

## Ruby

```ruby
class Solution
  def initialize(m, n)
    @m = m
    @n = n
    @total = m * n
    @used = 0
    @map = {}
  end

  def flip()
    r = rand(@total - @used)
    idx = @map.key?(r) ? @map[r] : r
    last = @total - 1 - @used
    @map[r] = @map.key?(last) ? @map[last] : last
    @used += 1
    [idx / @n, idx % @n]
  end

  def reset()
    @used = 0
    @map.clear
  end
end
```

## Scala

```scala
import scala.collection.mutable
import scala.util.Random

class Solution(_m: Int, _n: Int) {

  private val m: Int = _m
  private val n: Int = _n
  private val total: Int = m * n
  private var remaining: Int = total
  private val map: mutable.HashMap[Int, Int] = mutable.HashMap()
  private val rand: Random = new Random()

  def flip(): Array[Int] = {
    // pick a random index among the remaining positions
    val idx = rand.nextInt(remaining)
    // actual position after considering previous swaps
    val actual = map.getOrElse(idx, idx)

    // swap the chosen index with the last available one
    val last = remaining - 1
    val lastVal = map.getOrElse(last, last)
    map.update(idx, lastVal)

    remaining -= 1

    Array(actual / n, actual % n)
  }

  def reset(): Unit = {
    map.clear()
    remaining = total
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(m, n)
 * val param_1 = obj.flip()
 * obj.reset()
 */
```

## Rust

```rust
use std::cell::{Cell, RefCell};
use std::collections::HashMap;
use rand::{thread_rng, Rng};

struct Solution {
    m: i32,
    n: i32,
    total: i64,
    flipped: Cell<i64>,
    map: RefCell<HashMap<i64, i64>>,
}

impl Solution {
    fn new(m: i32, n: i32) -> Self {
        let total = (m as i64) * (n as i64);
        Solution {
            m,
            n,
            total,
            flipped: Cell::new(0),
            map: RefCell::new(HashMap::new()),
        }
    }

    fn flip(&self) -> Vec<i32> {
        let mut rng = thread_rng();
        let remaining = self.total - self.flipped.get();
        let idx = rng.gen_range(0..remaining);
        let mut map_ref = self.map.borrow_mut();

        let x = *map_ref.get(&idx).unwrap_or(&idx);
        let last = remaining - 1;
        let y = *map_ref.get(&last).unwrap_or(&last);
        map_ref.insert(idx, y);

        self.flipped.set(self.flipped.get() + 1);
        drop(map_ref); // release borrow

        let row = (x / self.n as i64) as i32;
        let col = (x % self.n as i64) as i32;
        vec![row, col]
    }

    fn reset(&self) {
        self.flipped.set(0);
        self.map.borrow_mut().clear();
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(m, n);
 * let ret_1: Vec<i32> = obj.flip();
 * obj.reset();
 */
```

## Racket

```racket
(define solution%
  (class object%
    (super-new)
    (init-field m n)

    ; total remaining zeros
    (define total (* m n))
    (define original-total total)
    ; mapping for virtual swaps
    (define dict (make-hash))

    (define/public (reset)
      (set! total original-total)
      (hash-clear! dict))

    (define/public (flip)
      (let* ([cur total]
             [randIdx (random cur)]
             [lastIdx (- cur 1)])
        (set! total lastIdx)
        (define actual
          (if (hash-has-key? dict randIdx)
              (hash-ref dict randIdx)
              randIdx))
        (define mapped
          (if (hash-has-key? dict lastIdx)
              (hash-ref dict lastIdx)
              lastIdx))
        (hash-set! dict randIdx mapped)
        (when (hash-has-key? dict lastIdx)
          (hash-remove! dict lastIdx))
        (list (quotient actual n) (remainder actual n))))))
```

## Erlang

```erlang
-module(solution).
-export([solution_init_/2, solution_flip/0, solution_reset/0]).

%% Initialize the matrix with dimensions M x N.
-spec solution_init_(M :: integer(), N :: integer()) -> any().
solution_init_(M, N) ->
    Total = M * N,
    put(state, {M, N, Total, #{}}),
    ok.

%% Randomly flip a zero to one and return its coordinates.
-spec solution_flip() -> [integer()].
solution_flip() ->
    {M, N, Total, Map} = get(state),
    %% Generate random index in range [0, Total-1]
    RandIdx = rand:uniform(Total) - 1,
    %% Resolve actual position
    X = maps:get(RandIdx, Map, RandIdx),
    %% Position of the last available element
    LastPos = Total - 1,
    Y = maps:get(LastPos, Map, LastPos),
    %% Update mapping: move Y into RandIdx slot
    NewMap = maps:put(RandIdx, Y, Map),
    NewTotal = Total - 1,
    put(state, {M, N, NewTotal, NewMap}),
    Row = X div N,
    Col = X rem N,
    [Row, Col].

%% Reset the matrix to all zeros.
-spec solution_reset() -> any().
solution_reset() ->
    {M, N, _, _} = get(state),
    Total = M * N,
    put(state, {M, N, Total, #{}}),
    ok.
```

## Elixir

```elixir
defmodule Solution do
  @spec init_(m :: integer, n :: integer) :: any
  def init_(m, n) do
    total = m * n
    # Seed the random generator for reproducibility
    :rand.seed(:exsplus, {System.system_time(), System.unique_integer([:positive]), :erlang.monotonic_time()})
    Process.put(:solution_state, %{
      m: m,
      n: n,
      total: total,
      remaining: total,
      map: %{}
    })
  end

  @spec flip() :: [integer]
  def flip() do
    state = Process.get(:solution_state)
    rem = state.remaining
    # random index in [0, rem-1]
    r = :rand.uniform(rem) - 1

    actual = Map.get(state.map, r, r)

    last_idx = rem - 1
    last_val = Map.get(state.map, last_idx, last_idx)

    new_map =
      if r != last_idx do
        state.map
        |> Map.put(r, last_val)
        |> Map.delete(last_idx)
      else
        Map.delete(state.map, last_idx)
      end

    new_state = %{state | remaining: rem - 1, map: new_map}
    Process.put(:solution_state, new_state)

    [div(actual, state.n), rem(actual, state.n)]
  end

  @spec reset() :: any
  def reset() do
    state = Process.get(:solution_state)
    new_state = %{state | remaining: state.total, map: %{}}
    Process.put(:solution_state, new_state)
  end
end
```

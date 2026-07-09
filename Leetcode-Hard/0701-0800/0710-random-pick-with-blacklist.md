# 0710. Random Pick with Blacklist

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    Solution(int n, vector<int>& blacklist) {
        int m = blacklist.size();
        limit = n - m;
        unordered_set<int> bset(blacklist.begin(), blacklist.end());
        int w = n - 1;
        for (int b : blacklist) {
            if (b < limit) {
                while (bset.count(w)) --w;
                mp[b] = w;
                --w;
            }
        }
        rng.seed(chrono::steady_clock::now().time_since_epoch().count());
        dist = uniform_int_distribution<int>(0, limit - 1);
    }
    
    int pick() {
        int x = dist(rng);
        auto it = mp.find(x);
        return it != mp.end() ? it->second : x;
    }
private:
    unordered_map<int,int> mp;
    int limit;
    mt19937 rng;
    uniform_int_distribution<int> dist;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(n, blacklist);
 * int param_1 = obj->pick();
 */
```

## Java

```java
import java.util.*;

class Solution {
    private final int bound;
    private final Map<Integer, Integer> mapping;
    private final Random rand;

    public Solution(int n, int[] blacklist) {
        this.rand = new Random();
        int m = blacklist.length;
        this.bound = n - m;
        this.mapping = new HashMap<>(m);
        Set<Integer> blackSet = new HashSet<>(m);
        for (int b : blacklist) {
            blackSet.add(b);
        }
        int w = bound; // candidate from the tail region
        for (int b : blacklist) {
            if (b < bound) {
                while (blackSet.contains(w)) {
                    w++;
                }
                mapping.put(b, w);
                w++;
            }
        }
    }

    public int pick() {
        int x = rand.nextInt(bound);
        return mapping.getOrDefault(x, x);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(n, blacklist);
 * int param_1 = obj.pick();
 */
```

## Python

```python
import random

class Solution(object):
    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.sz = n - len(blacklist)
        blackset = set(blacklist)
        self.mapping = {}
        last = n - 1
        for b in blacklist:
            if b < self.sz:
                while last in blackset:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self):
        """
        :rtype: int
        """
        x = random.randint(0, self.sz - 1)
        return self.mapping.get(x, x)
```

## Python3

```python
import random
from typing import List

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.bound = n - len(blacklist)  # size of the allowed range [0, bound)
        black_set = set(blacklist)

        # candidates in the upper part that are not blacklisted
        high_candidates = {i for i in range(self.bound, n) if i not in black_set}

        self.mapping = {}
        for b in blacklist:
            if b < self.bound:
                # map this small blacklisted number to a valid high candidate
                self.mapping[b] = high_candidates.pop()

    def pick(self) -> int:
        x = random.randrange(self.bound)
        return self.mapping.get(x, x)
```

## C

```c
#include <stdlib.h>

typedef struct {
    int w;
    int *keys;
    int *vals;
    int cap;
} Solution;

/* comparator for qsort */
static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/* binary search in sorted array */
static int is_blacklisted(int *arr, int size, int target) {
    int l = 0, r = size - 1;
    while (l <= r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] == target) return 1;
        if (arr[m] < target) l = m + 1;
        else r = m - 1;
    }
    return 0;
}

/* hash map helpers: keys initialized to -1 (empty slot) */
static void hashmap_put(Solution *obj, int key, int val) {
    int idx = key & (obj->cap - 1);
    while (obj->keys[idx] != -1) {
        idx = (idx + 1) & (obj->cap - 1);
    }
    obj->keys[idx] = key;
    obj->vals[idx] = val;
}

static int hashmap_get(Solution *obj, int key) {
    int idx = key & (obj->cap - 1);
    while (obj->keys[idx] != -1) {
        if (obj->keys[idx] == key) return obj->vals[idx];
        idx = (idx + 1) & (obj->cap - 1);
    }
    return -1; /* not found */
}

/* LeetCode API */
Solution* solutionCreate(int n, int* blacklist, int blacklistSize) {
    Solution *obj = (Solution *)malloc(sizeof(Solution));
    obj->w = n - blacklistSize;

    /* sort blacklist for binary search */
    qsort(blacklist, blacklistSize, sizeof(int), cmp_int);

    /* prepare hash map */
    int cap = 1;
    while (cap < blacklistSize * 2) cap <<= 1;
    if (cap == 0) cap = 1;               // when blacklistSize==0
    obj->cap = cap;
    obj->keys = (int *)malloc(sizeof(int) * cap);
    obj->vals = (int *)malloc(sizeof(int) * cap);
    for (int i = 0; i < cap; ++i) obj->keys[i] = -1;

    int last = n - 1;
    for (int i = 0; i < blacklistSize; ++i) {
        int b = blacklist[i];
        if (b >= obj->w) continue;      // only need to map small blacklisted numbers
        while (is_blacklisted(blacklist, blacklistSize, last)) {
            --last;
        }
        hashmap_put(obj, b, last);
        --last;
    }

    return obj;
}

int solutionPick(Solution* obj) {
    int x = rand() % obj->w;
    int mapped = hashmap_get(obj, x);
    return (mapped == -1) ? x : mapped;
}

void solutionFree(Solution* obj) {
    if (!obj) return;
    free(obj->keys);
    free(obj->vals);
    free(obj);
}
```

## Csharp

```csharp
public class Solution
{
    private readonly Random _rand;
    private readonly int _bound;
    private readonly Dictionary<int, int> _map;

    public Solution(int n, int[] blacklist)
    {
        _rand = new Random();
        int bLen = blacklist.Length;
        _bound = n - bLen; // size of the valid range [0, _bound-1]

        _map = new Dictionary<int, int>(bLen);
        var blackSet = new HashSet<int>(blacklist);

        int w = n - 1; // pointer to the end of the range
        foreach (int b in blacklist)
        {
            if (b < _bound)
            {
                while (blackSet.Contains(w))
                {
                    w--;
                }
                _map[b] = w;
                w--;
            }
        }
    }

    public int Pick()
    {
        int x = _rand.Next(_bound);
        return _map.TryGetValue(x, out int v) ? v : x;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} blacklist
 */
var Solution = function(n, blacklist) {
    this.bound = n - blacklist.length;
    this.map = new Map();
    const blackSet = new Set(blacklist);
    let w = n - 1;
    for (const b of blacklist) {
        if (b < this.bound) {
            while (blackSet.has(w)) {
                w--;
            }
            this.map.set(b, w);
            w--;
        }
    }
};

/**
 * @return {number}
 */
Solution.prototype.pick = function() {
    const x = Math.floor(Math.random() * this.bound);
    return this.map.get(x) ?? x;
};
```

## Typescript

```typescript
class Solution {
    private bound: number;
    private map: Map<number, number>;

    constructor(n: number, blacklist: number[]) {
        const m = blacklist.length;
        this.bound = n - m;
        this.map = new Map();

        const blackSet = new Set(blacklist);
        let last = n - 1;

        for (const b of blacklist) {
            if (b < this.bound) {
                while (blackSet.has(last)) {
                    last--;
                }
                this.map.set(b, last);
                last--;
            }
        }
    }

    pick(): number {
        const x = Math.floor(Math.random() * this.bound);
        return this.map.get(x) ?? x;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(n, blacklist)
 * var param_1 = obj.pick()
 */
```

## Php

```php
class Solution {
    private int $bound;
    private array $map = [];

    /**
     * @param Integer $n
     * @param Integer[] $blacklist
     */
    function __construct($n, $blacklist) {
        $m = count($blacklist);
        $this->bound = $n - $m;

        // Set of blacklisted numbers for O(1) lookup
        $blackSet = array_flip($blacklist);

        $last = $n - 1;
        foreach ($blacklist as $b) {
            if ($b < $this->bound) {
                while (isset($blackSet[$last])) {
                    $last--;
                }
                $this->map[$b] = $last;
                $last--;
            }
        }
    }

    /**
     * @return Integer
     */
    function pick() {
        $rand = random_int(0, $this->bound - 1);
        return $this->map[$rand] ?? $rand;
    }
}
```

## Swift

```swift
class Solution {
    private let bound: Int
    private var map: [Int: Int] = [:]

    init(_ n: Int, _ blacklist: [Int]) {
        let m = blacklist.count
        self.bound = n - m
        var blackSet = Set<Int>(blacklist)
        var w = bound
        for b in blacklist where b < bound {
            while blackSet.contains(w) {
                w += 1
            }
            map[b] = w
            w += 1
        }
    }

    func pick() -> Int {
        let x = Int.random(in: 0..<bound)
        return map[x] ?? x
    }
}
```

## Kotlin

```kotlin
class Solution(n: Int, blacklist: IntArray) {
    private val bound: Int
    private val map = HashMap<Int, Int>()
    private val rand = java.util.Random()

    init {
        val m = blacklist.size
        bound = n - m
        val blackSet = HashSet<Int>()
        for (b in blacklist) {
            if (b >= bound) {
                blackSet.add(b)
            }
        }
        var w = n - 1
        for (b in blacklist) {
            if (b < bound) {
                while (blackSet.contains(w)) {
                    w--
                }
                map[b] = w
                w--
            }
        }
    }

    fun pick(): Int {
        val x = rand.nextInt(bound)
        return map.getOrDefault(x, x)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  final int _bound;
  final Random _rand = Random();
  final Map<int, int> _map = {};

  Solution(int n, List<int> blacklist)
      : _bound = n - blacklist.length {
    final Set<int> bSet = Set.from(blacklist);
    int last = n - 1;
    for (final int b in blacklist) {
      if (b < _bound) {
        while (bSet.contains(last)) {
          last--;
        }
        _map[b] = last;
        last--;
      }
    }
  }

  int pick() {
    final int x = _rand.nextInt(_bound);
    return _map[x] ?? x;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(n, blacklist);
 * int param1 = obj.pick();
 */
```

## Golang

```go
import (
	"math/rand"
	"time"
)

type Solution struct {
	bound int
	mapping map[int]int
}

func Constructor(n int, blacklist []int) Solution {
	rand.Seed(time.Now().UnixNano())
	blackSet := make(map[int]struct{}, len(blacklist))
	for _, b := range blacklist {
		blackSet[b] = struct{}{}
	}
	bound := n - len(blacklist)
	mapping := make(map[int]int)

	w := n - 1
	for _, b := range blacklist {
		if b >= bound {
			continue
		}
		for {
			if _, ok := blackSet[w]; !ok {
				break
			}
			w--
		}
		mapping[b] = w
		w--
	}
	return Solution{bound: bound, mapping: mapping}
}

func (this *Solution) Pick() int {
	x := rand.Intn(this.bound)
	if v, ok := this.mapping[x]; ok {
		return v
	}
	return x
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(n, blacklist);
 * param_1 := obj.Pick();
 */
```

## Ruby

```ruby
class Solution
  def initialize(n, blacklist)
    @bound = n - blacklist.length
    @map = {}
    big = {}
    blacklist.each do |b|
      big[b] = true if b >= @bound
    end

    w = @bound
    blacklist.each do |b|
      next unless b < @bound
      while big.key?(w)
        w += 1
      end
      @map[b] = w
      w += 1
    end
  end

  def pick
    x = rand(@bound)
    @map.fetch(x, x)
  end
end
```

## Scala

```scala
import java.util.{Random, HashSet}
import scala.collection.mutable

class Solution(_n: Int, _blacklist: Array[Int]) {
  private val rand = new Random()
  private val N: Int = _n - _blacklist.length
  private val map = mutable.HashMap[Int, Int]()

  // Blacklisted numbers that are in the upper range [N, n)
  private val blacklistSet = new HashSet[Int]()
  for (b <- _blacklist) {
    if (b >= N) blacklistSet.add(b)
  }

  var w: Int = N
  for (b <- _blacklist) {
    if (b < N) {
      while (blacklistSet.contains(w)) {
        w += 1
      }
      map.put(b, w)
      w += 1
    }
  }

  def pick(): Int = {
    val x = rand.nextInt(N)
    map.getOrElse(x, x)
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(n, blacklist)
 * val param_1 = obj.pick()
 */
```

## Rust

```rust
use std::collections::{HashMap, HashSet};
use rand::Rng;

struct Solution {
    bound: i32,
    map: HashMap<i32, i32>,
}

impl Solution {
    fn new(n: i32, blacklist: Vec<i32>) -> Self {
        let m = blacklist.len() as i32;
        let bound = n - m;
        let black_set: HashSet<i32> = blacklist.iter().cloned().collect();
        let mut map = HashMap::new();

        let mut w = n - 1;
        for &b in &blacklist {
            if b < bound {
                while black_set.contains(&w) {
                    w -= 1;
                }
                map.insert(b, w);
                w -= 1;
            }
        }

        Solution { bound, map }
    }

    fn pick(&self) -> i32 {
        let mut rng = rand::thread_rng();
        let x = rng.gen_range(0..self.bound);
        *self.map.get(&x).unwrap_or(&x)
    }
}
```

## Racket

```racket
(define solution%
  (class object%
    (init-field n blacklist)
    (super-new)

    ;; internal fields
    (field [m 0]               ; size of whitelist
           [mapping (make-hash)]) ; blacklisted small -> whitelisted large

    ;; initialization logic
    (define/public (initialize)
      (set! m (- n (length blacklist)))
      (define bl-set (make-hash))
      (for ([b blacklist])
        (hash-set! bl-set b #t))
      (define w m)
      (for ([b blacklist])
        (when (< b m)
          ;; find next w not in blacklist
          (let loop ()
            (when (hash-has-key? bl-set w)
              (set! w (+ w 1))
              (loop)))
          (hash-set! mapping b w)
          (set! w (+ w 1)))))

    (initialize)

    ;; pick a random allowed integer
    (define/public (pick)
      (let ([k (random m)])
        (define mapped (hash-ref mapping k #f))
        (if mapped mapped k))))
```

## Erlang

```erlang
-export([solution_init_/2, solution_pick/0]).

-spec solution_init_(N :: integer(), Blacklist :: [integer()]) -> any().
solution_init_(N, Blacklist) ->
    _ = rand:seed(exsplus, erlang:monotonic_time()),
    B = length(Blacklist),
    M = N - B,
    % set of blacklisted numbers >= M
    BigSet = lists:foldl(
        fun(X, Acc) ->
            if X >= M -> maps:put(X, true, Acc); true -> Acc end
        end, #{}, Blacklist),
    {Map, _} = lists:foldl(
        fun(Bsmall, {AccMap, W}) when Bsmall < M ->
                NewW = find_valid(W, BigSet),
                {maps:put(Bsmall, NewW, AccMap), NewW - 1};
            (_, State) -> % Bsmall >= M, ignore
                State
        end,
        {#{}, N-1},
        Blacklist),
    put(solution_state, {M, Map}),
    ok.

-spec solution_pick() -> integer().
solution_pick() ->
    {M, Map} = get(solution_state),
    X = rand:uniform(M) - 1,
    case maps:find(X, Map) of
        {ok, V} -> V;
        error   -> X
    end.

% Helper to find the next candidate not in BigSet
find_valid(W, Set) ->
    case maps:is_key(W, Set) of
        true  -> find_valid(W - 1, Set);
        false -> W
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec init_(n :: integer, blacklist :: [integer]) :: any
  def init_(n, blacklist) do
    m = length(blacklist)
    limit = n - m
    bset = MapSet.new(blacklist)

    {mapping, _} =
      Enum.reduce(blacklist, {%{}, n - 1}, fn b, {acc_map, cur_tail} ->
        if b < limit do
          # find the next tail not in blacklist
          new_tail =
            Stream.iterate(cur_tail, &(&1 - 1))
            |> Enum.find(fn x -> not MapSet.member?(bset, x) end)

          {Map.put(acc_map, b, new_tail), new_tail - 1}
        else
          {acc_map, cur_tail}
        end
      end)

    Process.put(:solution_state, %{limit: limit, map: mapping})
    :ok
  end

  @spec pick() :: integer
  def pick() do
    state = Process.get(:solution_state)
    limit = state.limit
    mapping = state.map

    # :rand.uniform/1 returns 1..limit inclusive
    x = :rand.uniform(limit) - 1
    Map.get(mapping, x, x)
  end
end
```

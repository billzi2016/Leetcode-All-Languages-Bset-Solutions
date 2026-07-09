# 0528. Random Pick with Weight

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    vector<long long> prefix;
    long long total;
    mt19937 rng;
public:
    Solution(vector<int>& w) : total(0), rng(random_device{}()) {
        prefix.reserve(w.size());
        for (int weight : w) {
            total += weight;
            prefix.push_back(total);
        }
    }

    int pickIndex() {
        long long target = uniform_int_distribution<long long>(1, total)(rng);
        return lower_bound(prefix.begin(), prefix.end(), target) - prefix.begin();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
```

## Java

```java
import java.util.concurrent.ThreadLocalRandom;

class Solution {
    private final long[] prefix;
    private final long total;

    public Solution(int[] w) {
        int n = w.length;
        prefix = new long[n];
        long sum = 0;
        for (int i = 0; i < n; i++) {
            sum += w[i];
            prefix[i] = sum;
        }
        total = sum;
    }

    public int pickIndex() {
        long target = ThreadLocalRandom.current().nextLong(total) + 1;
        int lo = 0, hi = prefix.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (prefix[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
```

## Python

```python
class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix = []
        s = 0
        for weight in w:
            s += weight
            self.prefix.append(s)
        self.total = s

    def pickIndex(self):
        """
        :rtype: int
        """
        import random, bisect
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)
```

## Python3

```python
from bisect import bisect_left
import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        s = 0
        for weight in w:
            s += weight
            self.prefix.append(s)
        self.total = s

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect_left(self.prefix, target)
```

## C

```c
#include <stdlib.h>
#include <time.h>

typedef struct {
    long long *pref;
    int size;
    long long total;
} Solution;

Solution* solutionCreate(int* w, int wSize) {
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    obj->size = wSize;
    obj->pref = (long long*)malloc(sizeof(long long) * wSize);
    long long sum = 0;
    for (int i = 0; i < wSize; ++i) {
        sum += (long long)w[i];
        obj->pref[i] = sum;
    }
    obj->total = sum;
    srand((unsigned)time(NULL));
    return obj;
}

int solutionPickIndex(Solution* obj) {
    // generate a random target in [1, total]
    double r = (double)rand() / ((double)RAND_MAX + 1.0);
    long long target = (long long)(r * obj->total) + 1;

    int left = 0, right = obj->size - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (obj->pref[mid] < target)
            left = mid + 1;
        else
            right = mid;
    }
    return left;
}

void solutionFree(Solution* obj) {
    if (!obj) return;
    free(obj->pref);
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(w, wSize);
 * int param_1 = solutionPickIndex(obj);
 * solutionFree(obj);
 */
```

## Csharp

```csharp
public class Solution
{
    private readonly long[] _prefix;
    private readonly long _total;
    private readonly Random _rand;

    public Solution(int[] w)
    {
        _prefix = new long[w.Length];
        long sum = 0;
        for (int i = 0; i < w.Length; i++)
        {
            sum += w[i];
            _prefix[i] = sum;
        }
        _total = sum;
        _rand = new Random();
    }

    public int PickIndex()
    {
        double target = _rand.NextDouble() * _total;
        int left = 0, right = _prefix.Length - 1;
        while (left < right)
        {
            int mid = (left + right) >> 1;
            if (target < _prefix[mid])
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} w
 */
var Solution = function(w) {
    this.prefix = [];
    let sum = 0;
    for (let weight of w) {
        sum += weight;
        this.prefix.push(sum);
    }
    this.total = sum;
};

/**
 * @return {number}
 */
Solution.prototype.pickIndex = function() {
    const target = Math.random() * this.total; // [0, total)
    let left = 0, right = this.prefix.length - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (target < this.prefix[mid]) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
class Solution {
    private prefix: number[];
    private total: number;

    constructor(w: number[]) {
        this.prefix = new Array(w.length);
        let sum = 0;
        for (let i = 0; i < w.length; i++) {
            sum += w[i];
            this.prefix[i] = sum;
        }
        this.total = sum;
    }

    pickIndex(): number {
        const target = Math.random() * this.total;
        let low = 0, high = this.prefix.length - 1;
        while (low < high) {
            const mid = Math.floor((low + high) / 2);
            if (target < this.prefix[mid]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */
```

## Php

```php
class Solution {
    private $prefix = [];
    private $total = 0;

    /**
     * @param Integer[] $w
     */
    function __construct($w) {
        $sum = 0;
        foreach ($w as $weight) {
            $sum += $weight;
            $this->prefix[] = $sum;
        }
        $this->total = $sum;
    }

    /**
     * @return Integer
     */
    function pickIndex() {
        $target = mt_rand(1, $this->total);
        $low = 0;
        $high = count($this->prefix) - 1;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($target <= $this->prefix[$mid]) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = new Solution($w);
 * $ret_1 = $obj->pickIndex();
 */
```

## Swift

```swift
class Solution {
    private var prefix: [Int]
    private var total: Int

    init(_ w: [Int]) {
        self.prefix = []
        var sum = 0
        for weight in w {
            sum += weight
            self.prefix.append(sum)
        }
        self.total = sum
    }

    func pickIndex() -> Int {
        let target = Int.random(in: 0..<total)
        var left = 0
        var right = prefix.count - 1
        while left < right {
            let mid = (left + right) / 2
            if prefix[mid] <= target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
import java.util.concurrent.ThreadLocalRandom
import java.util.Arrays

class Solution(w: IntArray) {
    private val prefix: LongArray
    private val total: Long

    init {
        prefix = LongArray(w.size)
        var sum = 0L
        for (i in w.indices) {
            sum += w[i]
            prefix[i] = sum
        }
        total = sum
    }

    fun pickIndex(): Int {
        val target = ThreadLocalRandom.current().nextLong(total) + 1 // [1, total]
        var idx = Arrays.binarySearch(prefix, target)
        if (idx < 0) idx = -idx - 1
        return idx
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(w)
 * var param_1 = obj.pickIndex()
 */
```

## Dart

```dart
import 'dart:math';

class Solution {
  late final List<int> _prefix;
  late final int _total;
  final Random _rand = Random();

  Solution(List<int> w) {
    _prefix = List.filled(w.length, 0);
    int sum = 0;
    for (int i = 0; i < w.length; i++) {
      sum += w[i];
      _prefix[i] = sum;
    }
    _total = sum;
  }

  int pickIndex() {
    int target = _rand.nextInt(_total) + 1;
    int left = 0, right = _prefix.length - 1;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (target <= _prefix[mid]) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(w);
 * int param1 = obj.pickIndex();
 */
```

## Golang

```go
package main

import (
	"math/rand"
	"sort"
	"time"
)

type Solution struct {
	pref  []int64
	total int64
	rnd   *rand.Rand
}

func Constructor(w []int) Solution {
	pref := make([]int64, len(w))
	var sum int64
	for i, weight := range w {
		sum += int64(weight)
		pref[i] = sum
	}
	return Solution{
		pref:  pref,
		total: sum,
		rnd:   rand.New(rand.NewSource(time.Now().UnixNano())),
	}
}

func (this *Solution) PickIndex() int {
	target := this.rnd.Int63n(this.total) + 1
	idx := sort.Search(len(this.pref), func(i int) bool { return this.pref[i] >= target })
	return idx
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(w);
 * param_1 := obj.PickIndex();
 */
```

## Ruby

```ruby
class Solution
  def initialize(w)
    @prefix = []
    sum = 0
    w.each do |weight|
      sum += weight
      @prefix << sum
    end
    @total = sum
  end

  def pick_index
    target = rand(@total) + 1
    left = 0
    right = @prefix.length - 1
    while left < right
      mid = (left + right) / 2
      if @prefix[mid] >= target
        right = mid
      else
        left = mid + 1
      end
    end
    left
  end
end
```

## Scala

```scala
class Solution(_w: Array[Int]) {

  private val prefix: Array[Long] = {
    val arr = new Array[Long](_w.length)
    var sum: Long = 0L
    for (i <- _w.indices) {
      sum += _w(i).toLong
      arr(i) = sum
    }
    arr
  }

  private val total: Long = prefix.last

  def pickIndex(): Int = {
    val target = java.util.concurrent.ThreadLocalRandom.current().nextLong(total)
    var l = 0
    var r = prefix.length - 1
    while (l < r) {
      val mid = (l + r) >>> 1
      if (prefix(mid) > target) r = mid else l = mid + 1
    }
    l
  }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(w)
 * val param_1 = obj.pickIndex()
 */
```

## Rust

```rust
struct Solution {
    pref: Vec<i64>,
    total: i64,
}

impl Solution {
    fn new(w: Vec<i32>) -> Self {
        let mut pref = Vec::with_capacity(w.len());
        let mut sum: i64 = 0;
        for weight in w {
            sum += weight as i64;
            pref.push(sum);
        }
        Solution { pref, total: sum }
    }

    fn pick_index(&self) -> i32 {
        use rand::Rng;
        let target = rand::thread_rng().gen_range(1..=self.total);
        match self.pref.binary_search(&target) {
            Ok(idx) => idx as i32,
            Err(idx) => idx as i32,
        }
    }
}
```

## Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; w : (listof exact-integer?)
    (init-field w)
    
    ; Prefix sums stored in a vector for O(1) access
    (define prefix
      (let* ([n (length w)]
             [vec (make-vector n)])
        (let loop ((i 0) (acc 0) (lst w))
          (if (null? lst)
              vec
              (begin
                (set! acc (+ acc (car lst)))
                (vector-set! vec i acc)
                (loop (+ i 1) acc (cdr lst)))))))
    
    ; Total weight (last element of prefix vector)
    (define total
      (if (= (vector-length prefix) 0)
          0
          (vector-ref prefix (sub1 (vector-length prefix)))))
    
    ; Binary search: first index with prefix >= target
    (define (find-index target)
      (let loop ((lo 0) (hi (sub1 (vector-length prefix))))
        (if (= lo hi)
            lo
            (let* ([mid (quotient (+ lo hi) 2)]
                   [mid-val (vector-ref prefix mid)])
              (if (< mid-val target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    
    ; pick-index : -> exact-integer?
    (define/public (pick-index)
      (let* ([r (+ 1 (random total))]
             [idx (find-index r)])
        idx))))
```

## Erlang

```erlang
-module(solution).
-export([solution_init_/1, solution_pick_index/0]).

%% Initialize with weight array W
-spec solution_init_(W :: [integer()]) -> ok.
solution_init_(W) ->
    {PrefixList, Total} = lists:foldl(
        fun(Weight, {Acc, Sum}) ->
            NewSum = Sum + Weight,
            {[NewSum | Acc], NewSum}
        end,
        {[], 0},
        W),
    Prefix = list_to_tuple(lists:reverse(PrefixList)),
    put(prefix, Prefix),
    put(total, Total),
    put(size, length(W)),
    ok.

%% Pick an index based on weight
-spec solution_pick_index() -> integer().
solution_pick_index() ->
    Total = get(total),
    Target = rand:uniform(Total),
    Prefix = get(prefix),
    Size = get(size),
    Index1 = binary_search(Prefix, Size, Target, 1, Size),
    Index1 - 1.

%% Binary search for first position where element >= Target
binary_search(_Tuple, _Size, _Target, Low, High) when Low == High ->
    Low;
binary_search(Tuple, Size, Target, Low, High) ->
    Mid = (Low + High) div 2,
    case element(Mid, Tuple) >= Target of
        true -> binary_search(Tuple, Size, Target, Low, Mid);
        false -> binary_search(Tuple, Size, Target, Mid + 1, High)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec init_(w :: [integer]) :: any
  def init_(w) do
    {rev_prefix, total} =
      Enum.reduce(w, {[], 0}, fn x, {list, sum} ->
        new_sum = sum + x
        {[new_sum | list], new_sum}
      end)

    prefix = Enum.reverse(rev_prefix)
    Process.put(:prefix, prefix)
    Process.put(:total, total)
    :ok
  end

  @spec pick_index() :: integer
  def pick_index() do
    total = Process.get(:total)
    target = :rand.uniform(total)
    prefix = Process.get(:prefix)

    binary_search(prefix, target, 0, length(prefix) - 1)
  end

  defp binary_search(arr, target, lo, hi) when lo < hi do
    mid = div(lo + hi, 2)

    if Enum.at(arr, mid) >= target do
      binary_search(arr, target, lo, mid)
    else
      binary_search(arr, target, mid + 1, hi)
    end
  end

  defp binary_search(_arr, _target, lo, _hi), do: lo
end
```

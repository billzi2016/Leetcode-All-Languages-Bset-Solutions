# 2080. Range Frequency Queries

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class RangeFreqQuery {
    unordered_map<int, vector<int>> pos;
public:
    RangeFreqQuery(vector<int>& arr) {
        for (int i = 0; i < (int)arr.size(); ++i) {
            pos[arr[i]].push_back(i);
        }
    }
    
    int query(int left, int right, int value) {
        auto it = pos.find(value);
        if (it == pos.end()) return 0;
        const vector<int>& v = it->second;
        auto lIt = lower_bound(v.begin(), v.end(), left);
        auto rIt = upper_bound(v.begin(), v.end(), right);
        return static_cast<int>(rIt - lIt);
    }
};

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery* obj = new RangeFreqQuery(arr);
 * int param_1 = obj->query(left,right,value);
 */
```

## Java

```java
import java.util.*;

class RangeFreqQuery {
    private final Map<Integer, List<Integer>> posMap;

    public RangeFreqQuery(int[] arr) {
        posMap = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            posMap.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }
    }

    public int query(int left, int right, int value) {
        List<Integer> list = posMap.get(value);
        if (list == null) return 0;
        int lIdx = lowerBound(list, left);
        int rIdx = upperBound(list, right);
        return rIdx - lIdx;
    }

    private int lowerBound(List<Integer> list, int target) {
        int lo = 0, hi = list.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid) >= target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private int upperBound(List<Integer> list, int target) {
        int lo = 0, hi = list.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid) > target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = new RangeFreqQuery(arr);
 * int param_1 = obj.query(left,right,value);
 */
```

## Python

```python
class RangeFreqQuery(object):
    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        from collections import defaultdict
        self.pos = defaultdict(list)
        for i, v in enumerate(arr):
            self.pos[v].append(i)

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        import bisect
        lst = self.pos.get(value)
        if not lst:
            return 0
        lo = bisect.bisect_left(lst, left)
        hi = bisect.bisect_right(lst, right)
        return hi - lo
```

## Python3

```python
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List

class RangeFreqQuery:
    def __init__(self, arr: List[int]) -> None:
        self.idx_map = defaultdict(list)
        for i, v in enumerate(arr):
            self.idx_map[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        positions = self.idx_map.get(value)
        if not positions:
            return 0
        l = bisect_left(positions, left)
        r = bisect_right(positions, right)
        return r - l
```

## C

```c
#include <stdlib.h>

#define MAX_VAL 100000

typedef struct {
    int *data;
    int size;
    int capacity;
} Vec;

typedef struct {
    Vec *pos; // array of vectors indexed by value
} RangeFreqQuery;

/* binary search: first index >= target */
static int lowerBound(const int *a, int n, int target) {
    int l = 0, r = n;
    while (l < r) {
        int m = (l + r) >> 1;
        if (a[m] < target)
            l = m + 1;
        else
            r = m;
    }
    return l;
}

/* binary search: first index > target */
static int upperBound(const int *a, int n, int target) {
    int l = 0, r = n;
    while (l < r) {
        int m = (l + r) >> 1;
        if (a[m] <= target)
            l = m + 1;
        else
            r = m;
    }
    return l;
}

RangeFreqQuery* rangeFreqQueryCreate(int* arr, int arrSize) {
    RangeFreqQuery *obj = (RangeFreqQuery *)malloc(sizeof(RangeFreqQuery));
    obj->pos = (Vec *)calloc(MAX_VAL + 1, sizeof(Vec));

    for (int i = 0; i < arrSize; ++i) {
        int v = arr[i];
        if (v < 0 || v > MAX_VAL) continue;
        Vec *vec = &obj->pos[v];
        if (vec->capacity == 0) {
            vec->capacity = 4;
            vec->data = (int *)malloc(vec->capacity * sizeof(int));
        } else if (vec->size == vec->capacity) {
            vec->capacity <<= 1;
            vec->data = (int *)realloc(vec->data, vec->capacity * sizeof(int));
        }
        vec->data[vec->size++] = i;
    }
    return obj;
}

int rangeFreqQueryQuery(RangeFreqQuery* obj, int left, int right, int value) {
    if (value < 0 || value > MAX_VAL) return 0;
    Vec *vec = &obj->pos[value];
    if (vec->size == 0) return 0;

    int lb = lowerBound(vec->data, vec->size, left);
    int ub = upperBound(vec->data, vec->size, right);
    return ub - lb;
}

void rangeFreqQueryFree(RangeFreqQuery* obj) {
    for (int i = 0; i <= MAX_VAL; ++i) {
        if (obj->pos[i].data)
            free(obj->pos[i].data);
    }
    free(obj->pos);
    free(obj);
}

/**
 * Your RangeFreqQuery struct will be instantiated and called as such:
 * RangeFreqQuery* obj = rangeFreqQueryCreate(arr, arrSize);
 * int param_1 = rangeFreqQueryQuery(obj, left, right, value);
 * rangeFreqQueryFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class RangeFreqQuery
{
    private readonly Dictionary<int, List<int>> _positions;

    public RangeFreqQuery(int[] arr)
    {
        _positions = new Dictionary<int, List<int>>();
        for (int i = 0; i < arr.Length; i++)
        {
            int val = arr[i];
            if (!_positions.TryGetValue(val, out var list))
            {
                list = new List<int>();
                _positions[val] = list;
            }
            list.Add(i);
        }
    }

    public int Query(int left, int right, int value)
    {
        if (!_positions.TryGetValue(value, out var list))
            return 0;

        int lIdx = LowerBound(list, left);
        int rIdx = UpperBound(list, right);
        return rIdx - lIdx;
    }

    private static int LowerBound(List<int> list, int target)
    {
        int lo = 0, hi = list.Count;
        while (lo < hi)
        {
            int mid = lo + ((hi - lo) >> 1);
            if (list[mid] >= target)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }

    private static int UpperBound(List<int> list, int target)
    {
        int lo = 0, hi = list.Count;
        while (lo < hi)
        {
            int mid = lo + ((hi - lo) >> 1);
            if (list[mid] > target)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = new RangeFreqQuery(arr);
 * int param_1 = obj.Query(left,right,value);
 */
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 */
var RangeFreqQuery = function(arr) {
    this.posMap = new Map();
    for (let i = 0; i < arr.length; i++) {
        const v = arr[i];
        if (!this.posMap.has(v)) this.posMap.set(v, []);
        this.posMap.get(v).push(i);
    }
};

function lowerBound(arr, target) {
    let lo = 0, hi = arr.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

function upperBound(arr, target) {
    let lo = 0, hi = arr.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (arr[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

/** 
 * @param {number} left 
 * @param {number} right 
 * @param {number} value
 * @return {number}
 */
RangeFreqQuery.prototype.query = function(left, right, value) {
    const list = this.posMap.get(value);
    if (!list) return 0;
    const lIdx = lowerBound(list, left);
    const rIdx = upperBound(list, right);
    return rIdx - lIdx;
};
```

## Typescript

```typescript
class RangeFreqQuery {
    private idxMap: Map<number, number[]>;

    constructor(arr: number[]) {
        this.idxMap = new Map();
        for (let i = 0; i < arr.length; i++) {
            const val = arr[i];
            if (!this.idxMap.has(val)) {
                this.idxMap.set(val, []);
            }
            this.idxMap.get(val)!.push(i);
        }
    }

    private lowerBound(arr: number[], target: number): number {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    query(left: number, right: number, value: number): number {
        const positions = this.idxMap.get(value);
        if (!positions) return 0;
        const lIdx = this.lowerBound(positions, left);
        const rIdx = this.lowerBound(positions, right + 1);
        return rIdx - lIdx;
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * var obj = new RangeFreqQuery(arr)
 * var param_1 = obj.query(left,right,value)
 */
```

## Php

```php
class RangeFreqQuery {
    private array $pos = [];

    /**
     * @param Integer[] $arr
     */
    function __construct($arr) {
        foreach ($arr as $i => $v) {
            if (!isset($this->pos[$v])) {
                $this->pos[$v] = [];
            }
            $this->pos[$v][] = $i;
        }
    }

    private function lowerBound(array $arr, int $target): int {
        $l = 0;
        $r = count($arr);
        while ($l < $r) {
            $mid = intdiv($l + $r, 2);
            if ($arr[$mid] >= $target) {
                $r = $mid;
            } else {
                $l = $mid + 1;
            }
        }
        return $l;
    }

    private function upperBound(array $arr, int $target): int {
        $l = 0;
        $r = count($arr);
        while ($l < $r) {
            $mid = intdiv($l + $r, 2);
            if ($arr[$mid] > $target) {
                $r = $mid;
            } else {
                $l = $mid + 1;
            }
        }
        return $l;
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @param Integer $value
     * @return Integer
     */
    function query($left, $right, $value) {
        if (!isset($this->pos[$value])) {
            return 0;
        }
        $indices = $this->pos[$value];
        $lb = $this->lowerBound($indices, $left);
        $ub = $this->upperBound($indices, $right);
        return $ub - $lb;
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * $obj = new RangeFreqQuery($arr);
 * $ret_1 = $obj->query($left, $right, $value);
 */
```

## Swift

```swift
class RangeFreqQuery {
    private var positions: [Int: [Int]] = [:]

    init(_ arr: [Int]) {
        for (index, value) in arr.enumerated() {
            positions[value, default: []].append(index)
        }
    }

    func query(_ left: Int, _ right: Int, _ value: Int) -> Int {
        guard let list = positions[value] else { return 0 }
        // lower bound for left (first index >= left)
        var lo = 0
        var hi = list.count
        while lo < hi {
            let mid = (lo + hi) >> 1
            if list[mid] >= left {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        let lower = lo

        // upper bound for right (first index > right)
        lo = 0
        hi = list.count
        while lo < hi {
            let mid = (lo + hi) >> 1
            if list[mid] > right {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        let upper = lo

        return upper - lower
    }
}
```

## Kotlin

```kotlin
class RangeFreqQuery(arr: IntArray) {
    private val posMap: HashMap<Int, IntArray> = HashMap()

    init {
        val temp = HashMap<Int, MutableList<Int>>()
        for (i in arr.indices) {
            val v = arr[i]
            val list = temp.getOrPut(v) { mutableListOf() }
            list.add(i)
        }
        for ((k, list) in temp) {
            posMap[k] = list.toIntArray()
        }
    }

    private fun lowerBound(a: IntArray, target: Int): Int {
        var l = 0
        var r = a.size
        while (l < r) {
            val m = (l + r) ushr 1
            if (a[m] >= target) {
                r = m
            } else {
                l = m + 1
            }
        }
        return l
    }

    fun query(left: Int, right: Int, value: Int): Int {
        val indices = posMap[value] ?: return 0
        val lo = lowerBound(indices, left)
        val hi = lowerBound(indices, right + 1)
        return hi - lo
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * var obj = RangeFreqQuery(arr)
 * var param_1 = obj.query(left,right,value)
 */
```

## Dart

```dart
class RangeFreqQuery {
  final Map<int, List<int>> _positions = {};

  RangeFreqQuery(List<int> arr) {
    for (int i = 0; i < arr.length; ++i) {
      int v = arr[i];
      _positions.putIfAbsent(v, () => []).add(i);
    }
  }

  int query(int left, int right, int value) {
    final list = _positions[value];
    if (list == null) return 0;
    int lIdx = _lowerBound(list, left);
    int rIdx = _upperBound(list, right);
    return rIdx - lIdx;
  }

  int _lowerBound(List<int> arr, int target) {
    int lo = 0, hi = arr.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (arr[mid] < target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }

  int _upperBound(List<int> arr, int target) {
    int lo = 0, hi = arr.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (arr[mid] <= target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = RangeFreqQuery(arr);
 * int param1 = obj.query(left,right,value);
 */
```

## Golang

```go
package main

import "sort"

type RangeFreqQuery struct {
	pos map[int][]int
}

func Constructor(arr []int) RangeFreqQuery {
	m := make(map[int][]int)
	for i, v := range arr {
		m[v] = append(m[v], i)
	}
	return RangeFreqQuery{pos: m}
}

func (this *RangeFreqQuery) Query(left int, right int, value int) int {
	indices, ok := this.pos[value]
	if !ok {
		return 0
	}
	lo := sort.Search(len(indices), func(i int) bool { return indices[i] >= left })
	hi := sort.Search(len(indices), func(i int) bool { return indices[i] > right })
	return hi - lo
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,value);
 */
```

## Ruby

```ruby
class RangeFreqQuery
  def initialize(arr)
    @indices = Hash.new { |h, k| h[k] = [] }
    arr.each_with_index do |v, i|
      @indices[v] << i
    end
  end

  def query(left, right, value)
    list = @indices[value]
    return 0 if list.empty?
    lower = lower_bound(list, left)
    upper = upper_bound(list, right)
    upper - lower
  end

  private

  def lower_bound(arr, target)
    l = 0
    r = arr.length
    while l < r
      m = (l + r) / 2
      if arr[m] >= target
        r = m
      else
        l = m + 1
      end
    end
    l
  end

  def upper_bound(arr, target)
    l = 0
    r = arr.length
    while l < r
      m = (l + r) / 2
      if arr[m] > target
        r = m
      else
        l = m + 1
      end
    end
    l
  end
end
```

## Scala

```scala
class RangeFreqQuery(_arr: Array[Int]) {
  private val idxMap: Map[Int, Array[Int]] = {
    val tmp = scala.collection.mutable.Map[Int, scala.collection.mutable.ArrayBuffer[Int]]()
    var i = 0
    while (i < _arr.length) {
      val v = _arr(i)
      val buf = tmp.getOrElseUpdate(v, scala.collection.mutable.ArrayBuffer[Int]())
      buf += i
      i += 1
    }
    tmp.view.mapValues(_.toArray).toMap
  }

  private def lowerBound(arr: Array[Int], target: Int): Int = {
    var lo = 0
    var hi = arr.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (arr(mid) < target) lo = mid + 1 else hi = mid
    }
    lo
  }

  private def upperBound(arr: Array[Int], target: Int): Int = {
    var lo = 0
    var hi = arr.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (arr(mid) <= target) lo = mid + 1 else hi = mid
    }
    lo
  }

  def query(left: Int, right: Int, value: Int): Int = {
    idxMap.get(value) match {
      case None => 0
      case Some(arr) =>
        val l = lowerBound(arr, left)
        val r = upperBound(arr, right)
        r - l
    }
  }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * val obj = new RangeFreqQuery(arr)
 * val param_1 = obj.query(left,right,value)
 */
```

## Rust

```rust
use std::collections::HashMap;

struct RangeFreqQuery {
    pos: HashMap<i32, Vec<usize>>,
}

impl RangeFreqQuery {
    fn new(arr: Vec<i32>) -> Self {
        let mut map: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, v) in arr.into_iter().enumerate() {
            map.entry(v).or_insert_with(Vec::new).push(i);
        }
        RangeFreqQuery { pos: map }
    }

    fn query(&self, left: i32, right: i32, value: i32) -> i32 {
        if let Some(indices) = self.pos.get(&value) {
            let l = left as usize;
            let r = right as usize;
            let lo = indices.partition_point(|&x| x < l);
            let hi = indices.partition_point(|&x| x <= r);
            (hi - lo) as i32
        } else {
            0
        }
    }
}
```

## Racket

```racket
(define range-freq-query%
  (class object%
    (super-new)
    
    ; arr : (listof exact-integer?)
    (init-field arr)
    
    ; internal map: value -> vector of sorted indices
    (define pos-map (make-hash))
    
    ;; Build the map: collect indices in reverse order, then fix ordering
    (for ([val (in-list arr)] [i (in-naturals)])
      (hash-set! pos-map val (cons i (hash-ref pos-map val '()))))
    
    (for ([k (in-hash-keys pos-map)])
      (hash-set! pos-map k
                 (list->vector (reverse (hash-ref pos-map k)))))
    
    ;; lower bound: first index >= target
    (define (lower-bound vec target)
      (let loop ([lo 0] [hi (vector-length vec)])
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (midval (vector-ref vec mid)))
              (if (< midval target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    
    ;; upper bound: first index > target
    (define (upper-bound vec target)
      (let loop ([lo 0] [hi (vector-length vec)])
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (midval (vector-ref vec mid)))
              (if (<= midval target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    
    ; query : exact-integer? exact-integer? exact-integer? -> exact-integer?
    (define/public (query left right value)
      (let ([vec (hash-ref pos-map value #f)])
        (if (not vec)
            0
            (let* ((lidx (lower-bound vec left))
                   (ridx (upper-bound vec right)))
              (- ridx lidx)))))))
```

## Erlang

```erlang
-spec range_freq_query_init_(Arr :: [integer()]) -> any().
range_freq_query_init_(Arr) ->
    Map = build_map(Arr),
    put(range_freq_query_data, Map).

-spec range_freq_query_query(Left :: integer(), Right :: integer(), Value :: integer()) -> integer().
range_freq_query_query(Left, Right, Value) ->
    case get(range_freq_query_data) of
        undefined -> 0;
        Map ->
            case maps:find(Value, Map) of
                error -> 0;
                {ok, Tuple} ->
                    Lower = lower_bound(Tuple, Left),
                    Upper = upper_bound(Tuple, Right),
                    Upper - Lower
            end
    end.

%% internal helpers

build_map(Arr) ->
    Indices = lists:seq(0, length(Arr) - 1),
    Pairs = lists:zip(Indices, Arr),
    RevMap = lists:foldl(
        fun({Idx, Val}, M) ->
            maps:update_with(
                Val,
                fun(L) -> [Idx | L] end,
                [Idx],
                M)
        end,
        #{},
        Pairs),
    maps:map(
        fun(_Key, List) ->
            list_to_tuple(lists:reverse(List))
        end,
        RevMap).

lower_bound(Tuple, Target) ->
    Size = tuple_size(Tuple),
    lb_loop(1, Size + 1, Tuple, Target) - 1.

upper_bound(Tuple, Target) ->
    Size = tuple_size(Tuple),
    ub_loop(1, Size + 1, Tuple, Target) - 1.

lb_loop(Low, High, _Tuple, _Target) when Low >= High ->
    Low;
lb_loop(Low, High, Tuple, Target) ->
    Mid = (Low + High) bsr 1,
    Val = element(Mid, Tuple),
    if
        Val >= Target -> lb_loop(Low, Mid, Tuple, Target);
        true -> lb_loop(Mid + 1, High, Tuple, Target)
    end.

ub_loop(Low, High, _Tuple, _Target) when Low >= High ->
    Low;
ub_loop(Low, High, Tuple, Target) ->
    Mid = (Low + High) bsr 1,
    Val = element(Mid, Tuple),
    if
        Val > Target -> ub_loop(Low, Mid, Tuple, Target);
        true -> ub_loop(Mid + 1, High, Tuple, Target)
    end.
```

## Elixir

```elixir
defmodule RangeFreqQuery do
  @spec init_(arr :: [integer]) :: any
  def init_(arr) do
    # Build a map from value to a tuple of sorted indices
    map =
      Enum.reduce(Enum.with_index(arr), %{}, fn {v, i}, acc ->
        Map.update(acc, v, [i], &[i | &1])
      end)
      |> Enum.map(fn {k, list} -> {k, List.to_tuple(Enum.reverse(list))} end)
      |> Enum.into(%{})

    :persistent_term.put({__MODULE__, :data}, map)
    :ok
  end

  @spec query(left :: integer, right :: integer, value :: integer) :: integer
  def query(left, right, value) do
    map = :persistent_term.get({__MODULE__, :data})
    case Map.get(map, value) do
      nil -> 0
      indices_tuple ->
        lo = lower_bound(indices_tuple, left)
        hi = upper_bound(indices_tuple, right)
        hi - lo
    end
  end

  defp lower_bound(tuple, target) do
    len = tuple_size(tuple)
    do_lower(tuple, target, 0, len)
  end

  defp do_lower(_tuple, _target, lo, hi) when lo >= hi, do: lo

  defp do_lower(tuple, target, lo, hi) do
    mid = div(lo + hi, 2)

    if :erlang.element(mid + 1, tuple) < target do
      do_lower(tuple, target, mid + 1, hi)
    else
      do_lower(tuple, target, lo, mid)
    end
  end

  defp upper_bound(tuple, target) do
    len = tuple_size(tuple)
    do_upper(tuple, target, 0, len)
  end

  defp do_upper(_tuple, _target, lo, hi) when lo >= hi, do: lo

  defp do_upper(tuple, target, lo, hi) do
    mid = div(lo + hi, 2)

    if :erlang.element(mid + 1, tuple) <= target do
      do_upper(tuple, target, mid + 1, hi)
    else
      do_upper(tuple, target, lo, mid)
    end
  end
end
```

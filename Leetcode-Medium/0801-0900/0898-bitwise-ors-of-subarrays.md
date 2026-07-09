# 0898. Bitwise ORs of Subarrays

## Cpp

```cpp
class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        unordered_set<int> ans;
        vector<int> prev;
        for (int a : arr) {
            vector<int> cur;
            cur.reserve(prev.size() + 1);
            cur.push_back(a);
            for (int x : prev) {
                cur.push_back(x | a);
            }
            sort(cur.begin(), cur.end());
            cur.erase(unique(cur.begin(), cur.end()), cur.end());
            for (int v : cur) ans.insert(v);
            prev.swap(cur);
        }
        return static_cast<int>(ans.size());
    }
};
```

## Java

```java
class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        java.util.HashSet<Integer> result = new java.util.HashSet<>();
        java.util.HashSet<Integer> cur = new java.util.HashSet<>();
        for (int num : arr) {
            java.util.HashSet<Integer> next = new java.util.HashSet<>();
            next.add(num);
            for (int v : cur) {
                next.add(v | num);
            }
            cur = next;
            result.addAll(cur);
        }
        return result.size();
    }
}
```

## Python

```python
class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = set()
        cur = set()
        for num in arr:
            # OR with previous subarrays ending at previous index and start new subarray at current index
            cur = {num | val for val in cur}
            cur.add(num)
            result.update(cur)
        return len(result)
```

## Python3

```python
from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        cur = set()
        for num in arr:
            cur = {num} | {prev | num for prev in cur}
            result.update(cur)
        return len(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}

int subarrayBitwiseORs(int* arr, int arrSize) {
    if (arrSize == 0) return 0;

    int capacity = arrSize * 32 + 1;          // enough for all intermediate results
    int *all = (int *)malloc(capacity * sizeof(int));
    int total = 0;

    int prev[32];
    int prevSize = 0;
    int cur[32];

    for (int i = 0; i < arrSize; ++i) {
        int x = arr[i];
        cur[0] = x;
        int curSize = 1;

        for (int j = 0; j < prevSize; ++j) {
            int v = prev[j] | x;
            if (v != cur[curSize - 1]) {
                cur[curSize++] = v;
            }
        }

        if (total + curSize > capacity) {
            while (total + curSize > capacity) capacity <<= 1;
            all = (int *)realloc(all, capacity * sizeof(int));
        }
        memcpy(&all[total], cur, curSize * sizeof(int));
        total += curSize;

        memcpy(prev, cur, curSize * sizeof(int));
        prevSize = curSize;
    }

    qsort(all, total, sizeof(int), cmp_int);

    int uniqueCount = 0;
    for (int i = 0; i < total; ++i) {
        if (i == 0 || all[i] != all[i - 1]) {
            ++uniqueCount;
        }
    }

    free(all);
    return uniqueCount;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int SubarrayBitwiseORs(int[] arr) {
        var result = new HashSet<int>();
        var cur = new HashSet<int>();
        foreach (int num in arr) {
            var next = new HashSet<int>();
            next.Add(num);
            foreach (int v in cur) {
                next.Add(v | num);
            }
            cur = next;
            foreach (int v in cur) {
                result.Add(v);
            }
        }
        return result.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var subarrayBitwiseORs = function(arr) {
    const all = new Set();
    let cur = new Set();
    for (const num of arr) {
        const nxt = new Set([num]);
        for (const v of cur) {
            nxt.add(v | num);
        }
        cur = nxt;
        for (const v of cur) {
            all.add(v);
        }
    }
    return all.size;
};
```

## Typescript

```typescript
function subarrayBitwiseORs(arr: number[]): number {
    const result = new Set<number>();
    let prev = new Set<number>();

    for (const num of arr) {
        const cur = new Set<number>();
        cur.add(num);
        for (const v of prev) {
            cur.add(v | num);
        }
        for (const v of cur) {
            result.add(v);
        }
        prev = cur;
    }

    return result.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function subarrayBitwiseORs($arr) {
        $result = [];
        $prev = [];

        foreach ($arr as $num) {
            $cur = [$num => true];
            foreach ($prev as $val => $_) {
                $cur[$val | $num] = true;
            }
            $prev = $cur;
            foreach ($cur as $val => $_) {
                $result[$val] = true;
            }
        }

        return count($result);
    }
}
```

## Swift

```swift
class Solution {
    func subarrayBitwiseORs(_ arr: [Int]) -> Int {
        var result = Set<Int>()
        var cur = Set<Int>()
        for num in arr {
            var next = Set<Int>()
            next.insert(num)
            for v in cur {
                next.insert(v | num)
            }
            cur = next
            result.formUnion(cur)
        }
        return result.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subarrayBitwiseORs(arr: IntArray): Int {
        val result = HashSet<Int>()
        var cur = HashSet<Int>()
        for (num in arr) {
            val next = HashSet<Int>()
            next.add(num)
            for (v in cur) {
                next.add(v or num)
            }
            cur = next
            result.addAll(cur)
        }
        return result.size
    }
}
```

## Dart

```dart
class Solution {
  int subarrayBitwiseORs(List<int> arr) {
    Set<int> cur = <int>{};
    Set<int> total = <int>{};
    for (var x in arr) {
      Set<int> next = {x};
      for (var v in cur) {
        next.add(v | x);
      }
      cur = next;
      total.addAll(cur);
    }
    return total.length;
  }
}
```

## Golang

```go
func subarrayBitwiseORs(arr []int) int {
    cur := make(map[int]struct{})
    all := make(map[int]struct{})
    for _, x := range arr {
        next := make(map[int]struct{})
        // start new subarray with only current element
        next[x] = struct{}{}
        // extend previous subarrays
        for v := range cur {
            next[v|x] = struct{}{}
        }
        cur = next
        for v := range cur {
            all[v] = struct{}{}
        }
    }
    return len(all)
}
```

## Ruby

```ruby
require 'set'

def subarray_bitwise_o_rs(arr)
  overall = Set.new
  cur = Set.new
  arr.each do |x|
    new_cur = Set[x]
    cur.each { |v| new_cur.add(v | x) }
    cur = new_cur
    overall.merge(cur)
  end
  overall.size
end
```

## Scala

```scala
object Solution {
    def subarrayBitwiseORs(arr: Array[Int]): Int = {
        import scala.collection.mutable.HashSet
        val result = HashSet[Int]()
        var prev = HashSet[Int]()
        for (x <- arr) {
            val cur = HashSet[Int]()
            cur += x
            for (v <- prev) {
                cur += (v | x)
            }
            result ++= cur
            prev = cur
        }
        result.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subarray_bitwise_o_rs(arr: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        let mut cur: HashSet<i32> = HashSet::new();
        let mut all: HashSet<i32> = HashSet::new();

        for &x in arr.iter() {
            let mut nxt: HashSet<i32> = HashSet::with_capacity(cur.len() + 1);
            nxt.insert(x);
            for &v in cur.iter() {
                nxt.insert(v | x);
            }
            cur = nxt;
            all.extend(&cur);
        }

        all.len() as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/set)

(define/contract (subarray-bitwise-o-rs arr)
  (-> (listof exact-integer?) exact-integer?)
  (let-values ([(global prev)
                (for/fold ([global (set)] [prev (set)]) ([a arr])
                  (define cur
                    (foldl (lambda (v acc) (set-add acc (bitwise-ior v a)))
                           (set a)
                           (in-set prev)))
                  (values (set-union global cur) cur))])
    (set-count global)))
```

## Erlang

```erlang
-module(solution).
-export([subarray_bitwise_o_rs/1]).

-spec subarray_bitwise_o_rs(Arr :: [integer()]) -> integer().
subarray_bitwise_o_rs([]) ->
    0;
subarray_bitwise_o_rs(Arr) ->
    {_, All} = lists:foldl(
        fun(A, {Cur, All}) ->
            NewSet = new_set(Cur, A),
            NewAll = add_to_all(NewSet, All),
            {NewSet, NewAll}
        end,
        {maps:new(), maps:new()},
        Arr
    ),
    maps:size(All).

new_set(Cur, A) ->
    maps:fold(
        fun(B, _V, Acc) -> maps:put(A bor B, true, Acc) end,
        #{A => true},
        Cur
    ).

add_to_all(Set, Acc) ->
    maps:fold(fun(K, _V, Acc1) -> maps:put(K, true, Acc1) end, Acc, Set).
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @spec subarray_bitwise_o_rs(arr :: [integer]) :: integer
  def subarray_bitwise_o_rs(arr) do
    {_, result_set} =
      Enum.reduce(arr, {MapSet.new(), MapSet.new()}, fn x, {prev_set, global_set} ->
        new_set =
          prev_set
          |> Enum.reduce(MapSet.new([x]), fn v, acc -> MapSet.put(acc, Bitwise.bor(v, x)) end)

        {new_set, MapSet.union(global_set, new_set)}
      end)

    MapSet.size(result_set)
  end
end
```

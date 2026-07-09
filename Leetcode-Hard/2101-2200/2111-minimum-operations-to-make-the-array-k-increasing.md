# 2111. Minimum Operations to Make the Array K-Increasing

## Cpp

```cpp
class Solution {
public:
    int kIncreasing(vector<int>& arr, int k) {
        long long operations = 0;
        int n = arr.size();
        for (int start = 0; start < k; ++start) {
            vector<int> dp;
            for (int i = start; i < n; i += k) {
                int x = arr[i];
                auto it = upper_bound(dp.begin(), dp.end(), x);
                if (it == dp.end())
                    dp.push_back(x);
                else
                    *it = x;
            }
            int len = dp.size();
            int total = ((n - start + k - 1) / k); // number of elements in this subsequence
            operations += total - len;
        }
        return (int)operations;
    }
};
```

## Java

```java
class Solution {
    public int kIncreasing(int[] arr, int k) {
        int n = arr.length;
        int totalOps = 0;
        for (int start = 0; start < k; start++) {
            // Build the subsequence for this modulo class
            java.util.ArrayList<Integer> tails = new java.util.ArrayList<>();
            int count = 0;
            for (int i = start; i < n; i += k) {
                int val = arr[i];
                count++;
                int pos = upperBound(tails, val);
                if (pos == tails.size()) {
                    tails.add(val);
                } else {
                    tails.set(pos, val);
                }
            }
            totalOps += count - tails.size();
        }
        return totalOps;
    }

    private int upperBound(java.util.ArrayList<Integer> list, int target) {
        int l = 0, r = list.size();
        while (l < r) {
            int m = (l + r) >>> 1;
            if (list.get(m) <= target) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
}
```

## Python

```python
class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        import bisect
        n = len(arr)
        ops = 0
        for start in range(k):
            seq = []
            i = start
            while i < n:
                seq.append(arr[i])
                i += k
            # longest non-decreasing subsequence length
            tails = []
            for x in seq:
                pos = bisect.bisect_right(tails, x)
                if pos == len(tails):
                    tails.append(x)
                else:
                    tails[pos] = x
            ops += len(seq) - len(tails)
        return ops
```

## Python3

```python
from bisect import bisect_right
from typing import List

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ops = 0
        for start in range(k):
            seq = []
            i = start
            while i < n:
                seq.append(arr[i])
                i += k
            # longest non-decreasing subsequence length
            tails = []
            for x in seq:
                idx = bisect_right(tails, x)
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x
            ops += len(seq) - len(tails)
        return ops
```

## C

```c
#include <stdlib.h>

int kIncreasing(int* arr, int arrSize, int k) {
    int totalOps = 0;
    for (int start = 0; start < k; ++start) {
        // maximum possible length of this subsequence
        int maxLen = (arrSize - start + k - 1) / k;
        int *tails = (int *)malloc(maxLen * sizeof(int));
        int sz = 0;          // length of current LNDS
        int cnt = 0;         // number of elements in this subsequence

        for (int i = start; i < arrSize; i += k) {
            int x = arr[i];
            ++cnt;

            // binary search first element > x (upper_bound)
            int l = 0, r = sz;
            while (l < r) {
                int m = (l + r) >> 1;
                if (tails[m] > x)
                    r = m;
                else
                    l = m + 1;
            }
            if (l == sz) {
                tails[sz++] = x;
            } else {
                tails[l] = x;
            }
        }

        totalOps += cnt - sz;   // elements to change in this subsequence
        free(tails);
    }
    return totalOps;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int KIncreasing(int[] arr, int k) {
        int n = arr.Length;
        long ops = 0;
        for (int start = 0; start < k; ++start) {
            List<int> tails = new List<int>();
            int len = 0;
            for (int i = start; i < n; i += k) {
                int val = arr[i];
                int l = 0, r = tails.Count;
                while (l < r) {
                    int m = (l + r) >> 1;
                    if (tails[m] <= val) l = m + 1;
                    else r = m;
                }
                if (l == tails.Count) tails.Add(val);
                else tails[l] = val;
                len++;
            }
            ops += len - tails.Count;
        }
        return (int)ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var kIncreasing = function(arr, k) {
    const lengthOfLNDS = (seq) => {
        const tails = [];
        for (let x of seq) {
            // binary search first element > x (upper bound)
            let l = 0, r = tails.length;
            while (l < r) {
                const m = (l + r) >> 1;
                if (tails[m] > x) r = m;
                else l = m + 1;
            }
            if (l === tails.length) tails.push(x);
            else tails[l] = x;
        }
        return tails.length;
    };
    
    let ops = 0;
    const n = arr.length;
    for (let start = 0; start < k; ++start) {
        const seq = [];
        for (let i = start; i < n; i += k) {
            seq.push(arr[i]);
        }
        const keep = lengthOfLNDS(seq);
        ops += seq.length - keep;
    }
    return ops;
};
```

## Typescript

```typescript
function kIncreasing(arr: number[], k: number): number {
    const upperBound = (tails: number[], target: number): number => {
        let l = 0, r = tails.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (tails[m] <= target) l = m + 1;
            else r = m;
        }
        return l;
    };

    let operations = 0;
    for (let offset = 0; offset < k; ++offset) {
        const tails: number[] = [];
        for (let i = offset; i < arr.length; i += k) {
            const x = arr[i];
            const idx = upperBound(tails, x);
            if (idx === tails.length) tails.push(x);
            else tails[idx] = x;
        }
        const seqLen = Math.floor((arr.length - 1 - offset) / k) + 1;
        operations += seqLen - tails.length;
    }
    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function kIncreasing($arr, $k) {
        $n = count($arr);
        $operations = 0;

        for ($start = 0; $start < $k; $start++) {
            // Build the subsequence for this offset
            $seq = [];
            for ($i = $start; $i < $n; $i += $k) {
                $seq[] = $arr[$i];
            }

            // Find length of longest non‑decreasing subsequence (LNDS)
            $tails = []; // tails[i] = minimal possible tail value of a LNDS of length i+1
            foreach ($seq as $x) {
                $l = 0;
                $r = count($tails);
                while ($l < $r) {
                    $mid = intdiv($l + $r, 2);
                    if ($tails[$mid] > $x) { // upper bound: first element greater than x
                        $r = $mid;
                    } else {
                        $l = $mid + 1;
                    }
                }
                if ($l === count($tails)) {
                    $tails[] = $x;
                } else {
                    $tails[$l] = $x;
                }
            }

            $operations += count($seq) - count($tails);
        }

        return $operations;
    }
}
```

## Swift

```swift
class Solution {
    func kIncreasing(_ arr: [Int], _ k: Int) -> Int {
        let n = arr.count
        var result = 0
        
        for start in 0..<k {
            var seq = [Int]()
            var idx = start
            while idx < n {
                seq.append(arr[idx])
                idx += k
            }
            
            var tails = [Int]()
            for v in seq {
                var l = 0, r = tails.count
                while l < r {
                    let m = (l + r) >> 1
                    if tails[m] > v {
                        r = m
                    } else {
                        l = m + 1
                    }
                }
                if l == tails.count {
                    tails.append(v)
                } else {
                    tails[l] = v
                }
            }
            result += seq.count - tails.count
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kIncreasing(arr: IntArray, k: Int): Int {
        var operations = 0
        val n = arr.size
        for (start in 0 until k) {
            val tails = mutableListOf<Int>()
            var length = 0
            var idx = start
            while (idx < n) {
                val v = arr[idx]
                // binary search first element > v
                var l = 0
                var r = tails.size
                while (l < r) {
                    val m = (l + r) ushr 1
                    if (tails[m] <= v) {
                        l = m + 1
                    } else {
                        r = m
                    }
                }
                if (l == tails.size) {
                    tails.add(v)
                } else {
                    tails[l] = v
                }
                length++
                idx += k
            }
            operations += length - tails.size
        }
        return operations
    }
}
```

## Dart

```dart
class Solution {
  int kIncreasing(List<int> arr, int k) {
    int n = arr.length;
    int totalOps = 0;

    for (int start = 0; start < k; ++start) {
      List<int> seq = [];
      for (int i = start; i < n; i += k) {
        seq.add(arr[i]);
      }
      int lnds = _longestNonDecreasing(seq);
      totalOps += seq.length - lnds;
    }

    return totalOps;
  }

  int _longestNonDecreasing(List<int> seq) {
    List<int> tails = [];
    for (int val in seq) {
      int idx = _upperBound(tails, val);
      if (idx == tails.length) {
        tails.add(val);
      } else {
        tails[idx] = val;
      }
    }
    return tails.length;
  }

  int _upperBound(List<int> list, int target) {
    int l = 0, r = list.length;
    while (l < r) {
      int m = (l + r) >> 1;
      if (list[m] <= target) {
        l = m + 1;
      } else {
        r = m;
      }
    }
    return l;
  }
}
```

## Golang

```go
func kIncreasing(arr []int, k int) int {
    n := len(arr)
    totalOps := 0

    // Helper to compute length of longest non‑decreasing subsequence
    lnds := func(seq []int) int {
        tails := make([]int, 0)
        for _, x := range seq {
            lo, hi := 0, len(tails)
            for lo < hi {
                mid := (lo + hi) / 2
                if tails[mid] <= x { // upper bound: first > x
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            if lo == len(tails) {
                tails = append(tails, x)
            } else {
                tails[lo] = x
            }
        }
        return len(tails)
    }

    for start := 0; start < k; start++ {
        var seq []int
        for i := start; i < n; i += k {
            seq = append(seq, arr[i])
        }
        keep := lnds(seq)
        totalOps += len(seq) - keep
    }

    return totalOps
}
```

## Ruby

```ruby
def k_increasing(arr, k)
  n = arr.length
  total_ops = 0

  (0...k).each do |offset|
    tails = []
    cnt = 0
    i = offset
    while i < n
      cnt += 1
      x = arr[i]

      # upper_bound: first element > x
      l = 0
      r = tails.length
      while l < r
        m = (l + r) / 2
        if tails[m] <= x
          l = m + 1
        else
          r = m
        end
      end

      if l == tails.length
        tails << x
      else
        tails[l] = x
      end

      i += k
    end

    total_ops += cnt - tails.length
  end

  total_ops
end
```

## Scala

```scala
object Solution {
  def kIncreasing(arr: Array[Int], k: Int): Int = {
    val n = arr.length
    var keep = 0 // total length of longest non‑decreasing subsequences

    var start = 0
    while (start < k) {
      // collect the subsequence for this modulo class
      val seq = new scala.collection.mutable.ArrayBuffer[Int]()
      var i = start
      while (i < n) {
        seq += arr(i)
        i += k
      }

      // patience sorting for longest non‑decreasing subsequence (use upper bound)
      val tails = new scala.collection.mutable.ArrayBuffer[Int]()
      var idx = 0
      while (idx < seq.length) {
        val x = seq(idx)
        var l = 0
        var r = tails.length
        while (l < r) {
          val m = (l + r) >>> 1
          if (tails(m) <= x) l = m + 1 else r = m
        }
        if (l == tails.length) tails += x else tails(l) = x
        idx += 1
      }

      keep += tails.length
      start += 1
    }

    n - keep
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

impl Solution {
    pub fn k_increasing(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        let k_usize = k as usize;
        let mut keep_total: usize = 0;

        for start in 0..k_usize {
            // Build the subsequence for this modulo class
            let mut seq: Vec<i32> = Vec::new();
            let mut idx = start;
            while idx < n {
                seq.push(arr[idx]);
                idx += k_usize;
            }

            // Compute length of longest non‑decreasing subsequence (LNDS)
            let mut tails: Vec<i32> = Vec::new(); // tails[i] = minimal possible tail of a LNDS of length i+1
            for &x in seq.iter() {
                // Find first element > x (upper bound) to maintain non‑decreasing property
                let pos = match tails.binary_search_by(|v| {
                    if *v <= x { Ordering::Less } else { Ordering::Greater }
                }) {
                    Ok(p) => p,
                    Err(p) => p,
                };
                if pos == tails.len() {
                    tails.push(x);
                } else {
                    tails[pos] = x;
                }
            }

            keep_total += tails.len();
        }

        (n - keep_total) as i32
    }
}
```

## Racket

```racket
(define (upper-bound tails size x)
  (let loop ((lo 0) (hi size))
    (if (= lo hi)
        lo
        (let* ((mid (quotient (+ lo hi) 2))
               (mid-val (vector-ref tails mid)))
          (if (> mid-val x)
              (loop lo mid)
              (loop (+ mid 1) hi))))))

(define/contract (k-increasing arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((arrv (list->vector arr))
         (n (vector-length arrv))
         (total 0))
    (for ([offset (in-range (min k n))])
      (let ((tails (make-vector n 0))
            (size 0)
            (cnt 0))
        (let loop ((i offset))
          (when (< i n)
            (set! cnt (+ cnt 1))
            (let ((x (vector-ref arrv i)))
              (let ((pos (upper-bound tails size x)))
                (vector-set! tails pos x)
                (when (= pos size) (set! size (+ size 1)))))
            (loop (+ i k))))
        (set! total (+ total (- cnt size)))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([k_increasing/2]).
-spec k_increasing(Arr :: [integer()], K :: integer()) -> integer().
k_increasing(Arr, K) ->
    SubAcc = build_subseqs(Arr, K),
    total_ops(K, SubAcc).

build_subseqs(Arr, K) ->
    Empty = array:from_list(lists:duplicate(K, [])),
    build_subseqs(Arr, 0, K, Empty).

build_subseqs([], _Idx, _K, Acc) -> Acc;
build_subseqs([V|Rest], Idx, K, Acc) ->
    Offset = rem(Idx, K),
    OldList = array:get(Offset, Acc),
    NewAcc = array:set(Offset, [V|OldList], Acc),
    build_subseqs(Rest, Idx + 1, K, NewAcc).

total_ops(K, Acc) -> total_ops(0, K - 1, Acc, 0).

total_ops(Cur, Max, _Acc, Sum) when Cur > Max -> Sum;
total_ops(Cur, Max, Acc, Sum) ->
    RevList = array:get(Cur, Acc),
    List = lists:reverse(RevList),
    SubLen = length(List),
    Lnds = lnds_length(List),
    Ops = SubLen - Lnds,
    total_ops(Cur + 1, Max, Acc, Sum + Ops).

lnds_length(List) -> lnds_length(List, array:new(), 0).

lnds_length([], _TailArr, Len) -> Len;
lnds_length([X|Rest], TailArr, Len) ->
    Pos = find_pos(TailArr, Len, X),
    NewTailArr = if
        Pos == Len -> array:set(Len, X, TailArr);
        true       -> array:set(Pos, X, TailArr)
    end,
    NewLen = if Pos == Len -> Len + 1; true -> Len end,
    lnds_length(Rest, NewTailArr, NewLen).

find_pos(_TailArr, 0, _X) -> 0;
find_pos(TailArr, Len, X) ->
    binary_search(TailArr, 0, Len - 1, X).

binary_search(_Arr, Low, High, _X) when Low > High -> Low;
binary_search(Arr, Low, High, X) ->
    Mid = (Low + High) div 2,
    MidVal = array:get(Mid, Arr),
    if
        MidVal > X -> binary_search(Arr, Low, Mid - 1, X);
        true       -> binary_search(Arr, Mid + 1, High, X)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec k_increasing(arr :: [integer], k :: integer) :: integer
  def k_increasing(arr, k) do
    n = length(arr)
    tup = List.to_tuple(arr)

    Enum.reduce(0..(k - 1), 0, fn offset, acc ->
      seq = collect_seq(tup, n, offset, k, [])
      ops = min_operations(seq)
      acc + ops
    end)
  end

  defp collect_seq(_tup, n, idx, _step, acc) when idx >= n do
    Enum.reverse(acc)
  end

  defp collect_seq(tup, n, idx, step, acc) do
    val = elem(tup, idx)
    collect_seq(tup, n, idx + step, step, [val | acc])
  end

  defp min_operations([]), do: 0

  defp min_operations(seq) do
    comp = seq |> Enum.uniq() |> Enum.sort()
    index_map = Enum.with_index(comp, 1) |> Enum.into(%{}, fn {v, i} -> {v, i} end)
    size = length(comp) + 2
    bit = :array.new(size, default: 0)

    {_bit, max_len} =
      Enum.reduce(seq, {bit, 0}, fn x, {b, m} ->
        idx = Map.fetch!(index_map, x)
        best = query(b, idx)
        cur = best + 1
        new_m = if cur > m, do: cur, else: m
        new_b = update(b, idx, cur, size - 1)
        {new_b, new_m}
      end)

    length(seq) - max_len
  end

  defp query(_bit, i) when i <= 0, do: 0

  defp query(bit, i) do
    cur = :array.get(i, bit)
    rest = query(bit, i - (i &&& -i))
    if cur > rest, do: cur, else: rest
  end

  defp update(bit, i, _val, n) when i > n, do: bit

  defp update(bit, i, val, n) do
    cur = :array.get(i, bit)

    new_bit =
      if val > cur do
        :array.set(i, val, bit)
      else
        bit
      end

    next = i + (i &&& -i)
    update(new_bit, next, val, n)
  end
end
```

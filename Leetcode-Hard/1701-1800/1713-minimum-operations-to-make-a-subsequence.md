# 1713. Minimum Operations to Make a Subsequence

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& target, vector<int>& arr) {
        unordered_map<int,int> idx;
        idx.reserve(target.size()*2);
        for (int i = 0; i < (int)target.size(); ++i) {
            idx[target[i]] = i;
        }
        vector<int> seq;
        seq.reserve(arr.size());
        for (int x : arr) {
            auto it = idx.find(x);
            if (it != idx.end()) seq.push_back(it->second);
        }
        vector<int> dp;
        dp.reserve(seq.size());
        for (int v : seq) {
            auto it = lower_bound(dp.begin(), dp.end(), v);
            if (it == dp.end()) dp.push_back(v);
            else *it = v;
        }
        return (int)target.size() - (int)dp.size();
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minOperations(int[] target, int[] arr) {
        Map<Integer, Integer> indexMap = new HashMap<>(target.length * 2);
        for (int i = 0; i < target.length; i++) {
            indexMap.put(target[i], i);
        }
        int[] tails = new int[target.length];
        int length = 0;
        for (int num : arr) {
            Integer idxObj = indexMap.get(num);
            if (idxObj == null) continue;
            int idx = idxObj;
            int pos = Arrays.binarySearch(tails, 0, length, idx);
            if (pos < 0) pos = -(pos + 1);
            tails[pos] = idx;
            if (pos == length) {
                length++;
            }
        }
        return target.length - length;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        pos = {v: i for i, v in enumerate(target)}
        seq = [pos[x] for x in arr if x in pos]

        import bisect
        tails = []
        for num in seq:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(target) - len(tails)
```

## Python3

```python
class Solution:
    def minOperations(self, target, arr):
        pos = {v: i for i, v in enumerate(target)}
        seq = [pos[x] for x in arr if x in pos]
        import bisect
        lis = []
        for x in seq:
            idx = bisect.bisect_left(lis, x)
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
        return len(target) - len(lis)
```

## C

```c
#include <stdlib.h>

struct Pair {
    int val;
    int idx;
};

static int cmpPair(const void *a, const void *b) {
    int va = ((const struct Pair *)a)->val;
    int vb = ((const struct Pair *)b)->val;
    return (va > vb) - (va < vb);
}

/* binary search for key in sorted array of Pairs.
   returns the corresponding idx if found, otherwise -1 */
static int findIdx(const struct Pair *arr, int n, int key) {
    int l = 0, r = n - 1;
    while (l <= r) {
        int m = l + ((r - l) >> 1);
        if (arr[m].val == key) return arr[m].idx;
        if (arr[m].val < key) l = m + 1;
        else r = m - 1;
    }
    return -1;
}

/* lower bound: first position where arr[pos] >= key */
static int lowerBound(const int *arr, int size, int key) {
    int l = 0, r = size;
    while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m] < key) l = m + 1;
        else r = m;
    }
    return l;
}

int minOperations(int* target, int targetSize, int* arr, int arrSize) {
    /* map each value in target to its index */
    struct Pair *map = (struct Pair *)malloc(targetSize * sizeof(struct Pair));
    for (int i = 0; i < targetSize; ++i) {
        map[i].val = target[i];
        map[i].idx = i;
    }
    qsort(map, targetSize, sizeof(struct Pair), cmpPair);

    int *tails = (int *)malloc(targetSize * sizeof(int));
    int lisLen = 0;

    for (int i = 0; i < arrSize; ++i) {
        int idx = findIdx(map, targetSize, arr[i]);
        if (idx == -1) continue;               // not part of target
        int pos = lowerBound(tails, lisLen, idx);
        tails[pos] = idx;
        if (pos == lisLen) ++lisLen;
    }

    free(map);
    free(tails);
    return targetSize - lisLen;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] target, int[] arr) {
        var indexMap = new Dictionary<int, int>(target.Length);
        for (int i = 0; i < target.Length; i++) {
            indexMap[target[i]] = i;
        }

        var dp = new List<int>();
        foreach (var val in arr) {
            if (!indexMap.TryGetValue(val, out int mapped)) continue;

            int pos = dp.BinarySearch(mapped);
            if (pos < 0) pos = ~pos;
            if (pos == dp.Count) {
                dp.Add(mapped);
            } else {
                dp[pos] = mapped;
            }
        }

        return target.Length - dp.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {number}
 */
var minOperations = function(target, arr) {
    const indexMap = new Map();
    for (let i = 0; i < target.length; ++i) {
        indexMap.set(target[i], i);
    }
    
    const seq = [];
    for (const num of arr) {
        if (indexMap.has(num)) {
            seq.push(indexMap.get(num));
        }
    }
    
    const tails = [];
    for (const x of seq) {
        let l = 0, r = tails.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (tails[m] < x) l = m + 1;
            else r = m;
        }
        if (l === tails.length) tails.push(x);
        else tails[l] = x;
    }
    
    return target.length - tails.length;
};
```

## Typescript

```typescript
function minOperations(target: number[], arr: number[]): number {
    const indexMap = new Map<number, number>();
    target.forEach((val, idx) => indexMap.set(val, idx));

    const seq: number[] = [];
    for (const val of arr) {
        const mapped = indexMap.get(val);
        if (mapped !== undefined) seq.push(mapped);
    }

    const tails: number[] = [];
    for (const x of seq) {
        let left = 0, right = tails.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (tails[mid] < x) left = mid + 1;
            else right = mid;
        }
        if (left === tails.length) tails.push(x);
        else tails[left] = x;
    }

    return target.length - tails.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $target
     * @param Integer[] $arr
     * @return Integer
     */
    function minOperations($target, $arr) {
        // Map each value in target to its index
        $pos = [];
        foreach ($target as $i => $val) {
            $pos[$val] = $i;
        }

        // Build the sequence of indices for elements that appear in both arrays
        $seq = [];
        foreach ($arr as $v) {
            if (isset($pos[$v])) {
                $seq[] = $pos[$v];
            }
        }

        // Compute length of Longest Increasing Subsequence using patience sorting
        $tails = []; // tails[i] = smallest possible tail value for an LIS of length i+1
        foreach ($seq as $x) {
            $left = 0;
            $right = count($tails);
            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($tails[$mid] < $x) {
                    $left = $mid + 1;
                } else {
                    $right = $mid;
                }
            }
            if ($left === count($tails)) {
                $tails[] = $x;
            } else {
                $tails[$left] = $x;
            }
        }

        // Minimum operations needed
        return count($target) - count($tails);
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ target: [Int], _ arr: [Int]) -> Int {
        var indexMap = [Int: Int]()
        for (i, v) in target.enumerated() {
            indexMap[v] = i
        }
        
        var seq = [Int]()
        seq.reserveCapacity(arr.count)
        for v in arr {
            if let idx = indexMap[v] {
                seq.append(idx)
            }
        }
        
        var tails = [Int]()
        for x in seq {
            var left = 0
            var right = tails.count
            while left < right {
                let mid = (left + right) >> 1
                if tails[mid] < x {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            if left == tails.count {
                tails.append(x)
            } else {
                tails[left] = x
            }
        }
        
        return target.count - tails.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(target: IntArray, arr: IntArray): Int {
        val indexMap = HashMap<Int, Int>(target.size * 2)
        for (i in target.indices) {
            indexMap[target[i]] = i
        }
        val lis = java.util.ArrayList<Int>()
        for (value in arr) {
            val idx = indexMap[value] ?: continue
            var l = 0
            var r = lis.size
            while (l < r) {
                val m = (l + r) ushr 1
                if (lis[m] < idx) {
                    l = m + 1
                } else {
                    r = m
                }
            }
            if (l == lis.size) {
                lis.add(idx)
            } else {
                lis[l] = idx
            }
        }
        return target.size - lis.size
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> target, List<int> arr) {
    final Map<int, int> pos = {};
    for (int i = 0; i < target.length; i++) {
      pos[target[i]] = i;
    }

    List<int> dp = [];
    for (final val in arr) {
      if (!pos.containsKey(val)) continue;
      final idx = pos[val]!;

      int l = 0, r = dp.length;
      while (l < r) {
        final m = (l + r) >> 1;
        if (dp[m] < idx) {
          l = m + 1;
        } else {
          r = m;
        }
      }

      if (l == dp.length) {
        dp.add(idx);
      } else {
        dp[l] = idx;
      }
    }

    return target.length - dp.length;
  }
}
```

## Golang

```go
import "sort"

func minOperations(target []int, arr []int) int {
	pos := make(map[int]int, len(target))
	for i, v := range target {
		pos[v] = i
	}
	seq := make([]int, 0, len(arr))
	for _, v := range arr {
		if idx, ok := pos[v]; ok {
			seq = append(seq, idx)
		}
	}
	tails := []int{}
	for _, x := range seq {
		i := sort.Search(len(tails), func(i int) bool { return tails[i] >= x })
		if i == len(tails) {
			tails = append(tails, x)
		} else {
			tails[i] = x
		}
	}
	return len(target) - len(tails)
}
```

## Ruby

```ruby
def min_operations(target, arr)
  pos = {}
  target.each_with_index { |v, i| pos[v] = i }

  seq = []
  arr.each do |v|
    idx = pos[v]
    seq << idx if idx
  end

  tails = []
  seq.each do |x|
    l = 0
    r = tails.length
    while l < r
      m = (l + r) / 2
      if tails[m] < x
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
  end

  target.length - tails.length
end
```

## Scala

```scala
object Solution {
  def minOperations(target: Array[Int], arr: Array[Int]): Int = {
    import scala.collection.mutable

    val indexMap = mutable.HashMap[Int, Int]()
    for (i <- target.indices) {
      indexMap(target(i)) = i
    }

    val seq = new mutable.ArrayBuffer[Int]()
    for (v <- arr) {
      indexMap.get(v).foreach(seq += _)
    }

    val tails = new mutable.ArrayBuffer[Int]()
    for (x <- seq) {
      var l = 0
      var r = tails.length
      while (l < r) {
        val m = (l + r) >>> 1
        if (tails(m) < x) l = m + 1 else r = m
      }
      if (l == tails.length) tails += x
      else tails(l) = x
    }

    target.length - tails.length
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn min_operations(target: Vec<i32>, arr: Vec<i32>) -> i32 {
        let mut index_map: HashMap<i32, i32> = HashMap::with_capacity(target.len());
        for (i, &v) in target.iter().enumerate() {
            index_map.insert(v, i as i32);
        }

        let mut lis: Vec<i32> = Vec::new();
        for v in arr {
            if let Some(&idx) = index_map.get(&v) {
                match lis.binary_search(&idx) {
                    Ok(pos) => lis[pos] = idx,
                    Err(pos) => {
                        if pos == lis.len() {
                            lis.push(idx);
                        } else {
                            lis[pos] = idx;
                        }
                    }
                }
            }
        }

        (target.len() as i32) - (lis.len() as i32)
    }
}
```

## Racket

```racket
(define/contract (min-operations target arr)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((pos (make-hash))
         (n (length target)))
    ;; map each value in target to its index
    (let loop ((i 0) (lst target))
      (unless (null? lst)
        (hash-set! pos (car lst) i)
        (loop (+ i 1) (cdr lst))))
    ;; collect indices of arr elements that appear in target
    (define seq '())
    (for ([x (in-list arr)])
      (when (hash-has-key? pos x)
        (set! seq (cons (hash-ref pos x) seq))))
    (set! seq (reverse seq))
    ;; longest increasing subsequence on seq
    (define len 0)
    (define tails (make-vector (length seq) 0))
    (for ([v (in-list seq)])
      (let loop ((l 0) (r len))
        (if (= l r)
            (begin
              (vector-set! tails l v)
              (when (= l len) (set! len (+ len 1))))
            (let* ((m (quotient (+ l r) 2))
                   (mid-val (vector-ref tails m)))
              (if (< mid-val v)
                  (loop (+ m 1) r)
                  (loop l m))))))
    (- n len)))
```

## Erlang

```erlang
-spec min_operations(Target :: [integer()], Arr :: [integer()]) -> integer().
min_operations(Target, Arr) ->
    Map = maps:from_list(lists:zip(Target, lists:seq(1, length(Target)))),
    Positions = [Pos || V <- Arr,
                        {ok, Pos} <- [maps:find(V, Map)]],
    {_, LisLen} = lists:foldl(fun(Pos, {TailArr, Len}) ->
        case Len of
            0 ->
                NewArr = array:set(1, Pos, array:new()),
                {NewArr, 1};
            _ ->
                Index = binary_search(TailArr, 1, Len, Pos),
                if Index == 0 ->
                        NewLen = Len + 1,
                        NewArr = array:set(NewLen, Pos, TailArr),
                        {NewArr, NewLen};
                   true ->
                        NewArr = array:set(Index, Pos, TailArr),
                        {NewArr, Len}
                end
        end
    end, {array:new(), 0}, Positions),
    length(Target) - LisLen.

binary_search(TailArr, Low, High, Val) when Low =< High ->
    Mid = (Low + High) div 2,
    Elem = array:get(Mid, TailArr),
    if Elem < Val ->
            binary_search(TailArr, Mid + 1, High, Val);
       true ->
            case Mid of
                Low -> Mid;
                _ ->
                    Prev = binary_search(TailArr, Low, Mid - 1, Val),
                    case Prev of
                        0 -> Mid;
                        _ -> Prev
                    end
            end
    end;
binary_search(_, _, _, _) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(target :: [integer], arr :: [integer]) :: integer
  def min_operations(target, arr) do
    index_map = build_index_map(target)

    {_, lis_len} =
      Enum.reduce(arr, {:array.new(), 0}, fn v, {tails, len} ->
        case Map.fetch(index_map, v) do
          {:ok, pos} ->
            new_tails = update_tails(tails, len, pos)
            new_len = if pos_inserted_at(tails, len, pos) == len, do: len + 1, else: len
            {new_tails, new_len}

          :error ->
            {tails, len}
        end
      end)

    length(target) - lis_len
  end

  defp build_index_map(target) do
    target
    |> Enum.with_index()
    |> Enum.reduce(%{}, fn {val, idx}, acc -> Map.put(acc, val, idx) end)
  end

  # Returns the updated tails array after inserting/replacing position `pos`
  defp update_tails(tails, len, pos) do
    insert_idx = binary_search(tails, len, pos, 0, len)
    :array.set(insert_idx, pos, tails)
  end

  # Determines at which index the value would be inserted (first >= target)
  defp binary_search(_tails, _len, _target, lo, hi) when lo >= hi, do: lo

  defp binary_search(tails, len, target, lo, hi) do
    mid = div(lo + hi, 2)

    # When mid == len (possible only if len == 0), treat value as :infinity
    val =
      if mid < len do
        :array.get(mid, tails)
      else
        :infinity
      end

    if val < target do
      binary_search(tails, len, target, mid + 1, hi)
    else
      binary_search(tails, len, target, lo, mid)
    end
  end

  # Helper to find the index where `pos` was placed (used to update length)
  defp pos_inserted_at(tails, len, pos) do
    binary_search(tails, len, pos, 0, len)
  end
end
```

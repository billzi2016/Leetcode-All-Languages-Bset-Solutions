# 1906. Minimum Absolute Difference Queries

## Cpp

```cpp
class Solution {
public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        const int MAXV = 100;
        // prefix counts for each value 1..100
        vector<vector<int>> pref(MAXV + 1, vector<int>(n + 1, 0));
        for (int v = 1; v <= MAXV; ++v) {
            for (int i = 0; i < n; ++i) {
                pref[v][i + 1] = pref[v][i] + (nums[i] == v);
            }
        }

        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int l = q[0], r = q[1];
            int prev = -1;
            int best = MAXV + 1; // larger than any possible difference
            for (int v = 1; v <= MAXV; ++v) {
                int cnt = pref[v][r + 1] - pref[v][l];
                if (cnt > 0) {
                    if (prev != -1) best = min(best, v - prev);
                    prev = v;
                }
            }
            if (best == MAXV + 1) ans.push_back(-1);
            else ans.push_back(best);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] minDifference(int[] nums, int[][] queries) {
        int n = nums.length;
        // prefix counts for values 1..100
        int[][] pref = new int[n + 1][101];
        for (int i = 0; i < n; i++) {
            System.arraycopy(pref[i], 0, pref[i + 1], 0, 101);
            pref[i + 1][nums[i]]++;
        }

        int qlen = queries.length;
        int[] ans = new int[qlen];
        for (int qi = 0; qi < qlen; qi++) {
            int l = queries[qi][0];
            int r = queries[qi][1];

            int prev = -1;
            int minDiff = Integer.MAX_VALUE;
            int distinct = 0;

            for (int v = 1; v <= 100; v++) {
                int cnt = pref[r + 1][v] - pref[l][v];
                if (cnt > 0) {
                    distinct++;
                    if (prev != -1) {
                        int diff = v - prev;
                        if (diff < minDiff) {
                            minDiff = diff;
                        }
                    }
                    prev = v;
                }
            }

            ans[qi] = (distinct < 2) ? -1 : minDiff;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import bisect
        # positions for each possible value (1..100)
        pos = [[] for _ in range(101)]
        for i, v in enumerate(nums):
            pos[v].append(i)

        res = []
        for l, r in queries:
            prev = None
            best = 101  # larger than any possible difference
            distinct = 0
            for val in range(1, 101):
                lst = pos[val]
                if not lst:
                    continue
                idx = bisect.bisect_left(lst, l)
                if idx < len(lst) and lst[idx] <= r:
                    distinct += 1
                    if prev is not None:
                        diff = val - prev
                        if diff < best:
                            best = diff
                            if best == 1:   # cannot improve further
                                # still need to continue counting distinct values
                                pass
                    prev = val
            if distinct <= 1:
                res.append(-1)
            else:
                res.append(best)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        MAX_VAL = 100
        # prefix counts for each value 1..MAX_VAL
        pref = [[0] * (n + 1) for _ in range(MAX_VAL + 1)]
        for i, val in enumerate(nums):
            for v in range(1, MAX_VAL + 1):
                pref[v][i + 1] = pref[v][i]
            pref[val][i + 1] += 1

        res = []
        for l, r in queries:
            prev = -1
            best = MAX_VAL + 1
            uniq = 0
            rl = r + 1
            for v in range(1, MAX_VAL + 1):
                cnt = pref[v][rl] - pref[v][l]
                if cnt:
                    uniq += 1
                    if prev != -1:
                        diff = v - prev
                        if diff < best:
                            best = diff
                    prev = v
            res.append(-1 if uniq <= 1 else best)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minDifference(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    const int MAX_VAL = 100;
    int rows = MAX_VAL + 1;               // values from 0..100 (ignore 0)
    int cols = numsSize + 1;              // prefix length
    int *pref = (int *)calloc(rows * cols, sizeof(int));
    
    // Build prefix counts for each value
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        for (int v = 1; v <= MAX_VAL; ++v) {
            pref[v * cols + (i + 1)] = pref[v * cols + i];
        }
        pref[val * cols + (i + 1)]++;
    }
    
    int *ans = (int *)malloc(queriesSize * sizeof(int));
    
    for (int q = 0; q < queriesSize; ++q) {
        int l = queries[q][0];
        int r = queries[q][1];
        
        int prev = -1;
        int minDiff = MAX_VAL + 1;
        int distinct = 0;
        
        for (int v = 1; v <= MAX_VAL; ++v) {
            int cnt = pref[v * cols + (r + 1)] - pref[v * cols + l];
            if (cnt > 0) {
                ++distinct;
                if (prev != -1) {
                    int diff = v - prev;
                    if (diff < minDiff) minDiff = diff;
                }
                prev = v;
            }
        }
        
        ans[q] = (distinct <= 1) ? -1 : minDiff;
    }
    
    free(pref);
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] MinDifference(int[] nums, int[][] queries)
    {
        const int MAXV = 100;
        int n = nums.Length;
        // prefix counts for each value 1..100
        int[][] pref = new int[MAXV + 1][];
        for (int v = 1; v <= MAXV; v++)
            pref[v] = new int[n + 1];

        for (int i = 0; i < n; i++)
        {
            int val = nums[i];
            for (int v = 1; v <= MAXV; v++)
                pref[v][i + 1] = pref[v][i];
            pref[val][i + 1]++;
        }

        int qlen = queries.Length;
        int[] ans = new int[qlen];

        for (int qi = 0; qi < qlen; qi++)
        {
            int l = queries[qi][0];
            int r = queries[qi][1];

            int prev = -1;
            int minDiff = int.MaxValue;
            int distinct = 0;

            for (int v = 1; v <= MAXV; v++)
            {
                int cnt = pref[v][r + 1] - pref[v][l];
                if (cnt > 0)
                {
                    distinct++;
                    if (prev != -1)
                    {
                        int diff = v - prev;
                        if (diff < minDiff) minDiff = diff;
                    }
                    prev = v;
                }
            }

            ans[qi] = distinct < 2 ? -1 : minDiff;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var minDifference = function(nums, queries) {
    const n = nums.length;
    const MAXV = 100;
    // prefix counts for each possible value (1..100)
    const pref = Array.from({ length: MAXV + 1 }, () => new Uint32Array(n + 1));
    for (let i = 0; i < n; ++i) {
        // copy previous counts
        for (let v = 1; v <= MAXV; ++v) {
            pref[v][i + 1] = pref[v][i];
        }
        const val = nums[i];
        pref[val][i + 1]++;
    }

    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; ++qi) {
        const [l, r] = queries[qi];
        let prev = -1;
        let distinct = 0;
        let best = Infinity;
        for (let v = 1; v <= MAXV; ++v) {
            const cnt = pref[v][r + 1] - pref[v][l];
            if (cnt > 0) {
                distinct++;
                if (prev !== -1) {
                    const diff = v - prev;
                    if (diff < best) best = diff;
                }
                prev = v;
            }
        }
        ans[qi] = distinct <= 1 ? -1 : best;
    }
    return ans;
};
```

## Typescript

```typescript
function minDifference(nums: number[], queries: number[][]): number[] {
    const n = nums.length;
    const MAXV = 100;
    const pref: Uint32Array[] = Array.from({ length: MAXV + 1 }, () => new Uint32Array(n + 1));
    for (let v = 1; v <= MAXV; ++v) {
        const arr = pref[v];
        let cnt = 0;
        for (let i = 0; i < n; ++i) {
            if (nums[i] === v) cnt++;
            arr[i + 1] = cnt;
        }
    }
    const res: number[] = new Array(queries.length);
    const INF = MAXV + 1;
    for (let qi = 0; qi < queries.length; ++qi) {
        const [l, r] = queries[qi];
        let prev = -1;
        let best = INF;
        for (let v = 1; v <= MAXV; ++v) {
            if (pref[v][r + 1] - pref[v][l] > 0) {
                if (prev !== -1) {
                    const diff = v - prev;
                    if (diff < best) best = diff;
                }
                prev = v;
            }
        }
        res[qi] = best === INF ? -1 : best;
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function minDifference($nums, $queries) {
        // positions of each value (1..100)
        $pos = array_fill(0, 101, []);
        foreach ($nums as $idx => $val) {
            $pos[$val][] = $idx;
        }

        $answers = [];

        foreach ($queries as $q) {
            [$l, $r] = $q;
            $prev = -1;
            $best = PHP_INT_MAX;

            for ($v = 1; $v <= 100; ++$v) {
                $arr = $pos[$v];
                if (empty($arr)) continue;

                // binary search first index >= l
                $low = 0;
                $high = count($arr) - 1;
                while ($low <= $high) {
                    $mid = ($low + $high) >> 1;
                    if ($arr[$mid] < $l) {
                        $low = $mid + 1;
                    } else {
                        $high = $mid - 1;
                    }
                }

                // check if found index is within r
                if ($low < count($arr) && $arr[$low] <= $r) {
                    if ($prev != -1) {
                        $diff = $v - $prev;
                        if ($diff < $best) {
                            $best = $diff;
                            if ($best == 1) break; // cannot get smaller
                        }
                    }
                    $prev = $v;
                }
            }

            $answers[] = ($best === PHP_INT_MAX) ? -1 : $best;
        }

        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    func minDifference(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var pref = Array(repeating: [Int](repeating: 0, count: n + 1), count: 101)
        for i in 0..<n {
            let val = nums[i]
            for v in 1...100 {
                pref[v][i + 1] = pref[v][i]
            }
            pref[val][i + 1] += 1
        }
        
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let l = q[0]
            let r = q[1]
            var prev = -1
            var minDiff = Int.max
            var distinct = 0
            for v in 1...100 {
                let cnt = pref[v][r + 1] - pref[v][l]
                if cnt > 0 {
                    distinct += 1
                    if prev != -1 {
                        let diff = v - prev
                        if diff < minDiff { minDiff = diff }
                    }
                    prev = v
                }
            }
            if distinct <= 1 {
                result.append(-1)
            } else {
                result.append(minDiff)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDifference(nums: IntArray, queries: Array<IntArray>): IntArray {
        val n = nums.size
        val maxVal = 100
        // prefix counts for each possible value (1..100)
        val pref = Array(maxVal + 1) { IntArray(n + 1) }
        for (v in 1..maxVal) {
            val arr = pref[v]
            var cnt = 0
            for (i in 0 until n) {
                if (nums[i] == v) cnt++
                arr[i + 1] = cnt
            }
        }

        val ans = IntArray(queries.size)
        var idx = 0
        for (q in queries) {
            val l = q[0]
            val r = q[1]
            var prev = -1
            var minDiff = Int.MAX_VALUE
            var distinct = 0
            for (v in 1..maxVal) {
                if (pref[v][r + 1] - pref[v][l] > 0) {
                    distinct++
                    if (prev != -1) {
                        val diff = v - prev
                        if (diff < minDiff) minDiff = diff
                    }
                    prev = v
                }
            }
            ans[idx++] = if (distinct <= 1) -1 else minDiff
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:typed_data';

class Solution {
  List<int> minDifference(List<int> nums, List<List<int>> queries) {
    final n = nums.length;
    const maxVal = 100;

    // Prefix counts for each possible value (1..100)
    final pref = List<Uint32List>.generate(
        maxVal + 1, (_) => Uint32List(n + 1));

    for (int i = 0; i < n; ++i) {
      final cur = nums[i];
      // copy previous counts
      for (int v = 1; v <= maxVal; ++v) {
        pref[v][i + 1] = pref[v][i];
      }
      pref[cur][i + 1] += 1;
    }

    final result = List<int>.filled(queries.length, 0);
    for (int qi = 0; qi < queries.length; ++qi) {
      final l = queries[qi][0];
      final r = queries[qi][1];

      int prev = -1;
      int minDiff = maxVal + 1;
      int distinct = 0;

      for (int v = 1; v <= maxVal; ++v) {
        if (pref[v][r + 1] - pref[v][l] > 0) {
          distinct++;
          if (prev != -1) {
            final diff = v - prev;
            if (diff < minDiff) minDiff = diff;
          }
          prev = v;
        }
      }

      result[qi] = distinct <= 1 ? -1 : minDiff;
    }

    return result;
  }
}
```

## Golang

```go
func minDifference(nums []int, queries [][]int) []int {
    n := len(nums)
    // prefix counts for values 1..100
    pref := make([][101]int, n+1)
    for i := 0; i < n; i++ {
        pref[i+1] = pref[i]
        v := nums[i]
        pref[i+1][v]++
    }

    const INF = 200 // larger than any possible difference (max 99)
    ans := make([]int, len(queries))

    for i, q := range queries {
        l, r := q[0], q[1]
        last := -1
        best := INF
        for v := 1; v <= 100; v++ {
            cnt := pref[r+1][v] - pref[l][v]
            if cnt > 0 {
                if last != -1 {
                    diff := v - last
                    if diff < best {
                        best = diff
                    }
                }
                last = v
            }
        }
        if best == INF {
            ans[i] = -1
        } else {
            ans[i] = best
        }
    }

    return ans
}
```

## Ruby

```ruby
def min_difference(nums, queries)
  pos = Array.new(101) { [] }
  nums.each_with_index do |v, i|
    pos[v] << i
  end

  result = []
  queries.each do |l, r|
    prev = nil
    min_diff = 101
    distinct = 0
    v = 1
    while v <= 100
      arr = pos[v]
      unless arr.empty?
        lo = 0
        hi = arr.length
        while lo < hi
          mid = (lo + hi) >> 1
          if arr[mid] < l
            lo = mid + 1
          else
            hi = mid
          end
        end
        if lo < arr.length && arr[lo] <= r
          distinct += 1
          if prev
            diff = v - prev
            min_diff = diff if diff < min_diff
          end
          prev = v
        end
      end
      v += 1
    end
    result << (distinct <= 1 ? -1 : min_diff)
  end
  result
end
```

## Scala

```scala
object Solution {
  def minDifference(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val maxVal = 100
    // prefix counts [value][i]
    val pref = Array.ofDim[Int](maxVal + 1, n + 1)
    var i = 0
    while (i < n) {
      val x = nums(i)
      var v = 1
      while (v <= maxVal) {
        pref(v)(i + 1) = pref(v)(i)
        v += 1
      }
      pref(x)(i + 1) += 1
      i += 1
    }

    val m = queries.length
    val ansArr = new Array[Int](m)
    var qi = 0
    while (qi < m) {
      val l = queries(qi)(0)
      val r = queries(qi)(1)
      var prev = -1
      var best = Int.MaxValue
      var distinct = 0
      var v = 1
      while (v <= maxVal) {
        val cnt = pref(v)(r + 1) - pref(v)(l)
        if (cnt > 0) {
          distinct += 1
          if (prev != -1) {
            val diff = v - prev
            if (diff < best) best = diff
          }
          prev = v
        }
        v += 1
      }
      ansArr(qi) = if (distinct <= 1) -1 else best
      qi += 1
    }
    ansArr
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_difference(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        // prefix counts for each possible value (1..=100)
        let mut pref = vec![vec![0i32; n + 1]; 101];
        for v in 1..=100 {
            for i in 0..n {
                pref[v][i + 1] = pref[v][i] + if nums[i] == v as i32 { 1 } else { 0 };
            }
        }

        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let mut prev: Option<i32> = None;
            let mut best = i32::MAX;
            let mut distinct = 0;

            for v in 1..=100 {
                let cnt = pref[v][r + 1] - pref[v][l];
                if cnt > 0 {
                    distinct += 1;
                    if let Some(p) = prev {
                        let diff = v as i32 - p;
                        if diff < best {
                            best = diff;
                        }
                    }
                    prev = Some(v as i32);
                }
            }

            if distinct <= 1 {
                ans.push(-1);
            } else {
                ans.push(best);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-difference nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((maxV 100)
         (n (length nums))
         (numsV (list->vector nums))
         ;; prefix counts for each value 0..maxV
         (prefix (make-vector (+ maxV 1) #f)))
    ;; allocate vectors
    (for ([v (in-range 0 (+ maxV 1))])
      (vector-set! prefix v (make-vector (+ n 1) 0)))
    ;; fill prefix counts
    (for ([v (in-range 1 (+ maxV 1))])
      (let ((vec (vector-ref prefix v)))
        (vector-set! vec 0 0)
        (for ([i (in-range n)])
          (define prev (vector-ref vec i))
          (define add (if (= (vector-ref numsV i) v) 1 0))
          (vector-set! vec (add1 i) (+ prev add)))))
    ;; answer queries
    (let loop ((qs queries) (acc '()))
      (if (null? qs)
          (reverse acc)
          (let* ((pair (car qs))
                 (l (list-ref pair 0))
                 (r (list-ref pair 1)))
            (define prev #f)
            (define min-diff 101) ; larger than any possible diff
            (define distinct 0)
            (for ([v (in-range 1 (+ maxV 1))])
              (let* ((vec (vector-ref prefix v))
                     (cnt (- (vector-ref vec (add1 r))
                             (vector-ref vec l))))
                (when (> cnt 0)
                  (set! distinct (+ distinct 1))
                  (when prev
                    (define diff (- v prev))
                    (when (< diff min-diff) (set! min-diff diff)))
                  (set! prev v))))
            (define ans (if (<= distinct 1) -1 min-diff))
            (loop (cdr qs) (cons ans acc)))))))
```

## Erlang

```erlang
-spec min_difference([integer()], [[integer()]]) -> [integer()].
min_difference(Nums, Queries) ->
    PrefixData = build_prefix_data(Nums),
    lists:map(fun([L, R]) -> query_min_diff(L, R, PrefixData) end, Queries).

%% Build a tuple where each element is a tuple of prefix counts for a value 0..100
build_prefix_data(Nums) ->
    Counts0 = lists:duplicate(101, 0),
    Prefixes0 = [ [0] || _ <- lists:seq(0, 100) ],
    {_, PrefixesRev} =
        lists:foldl(
          fun(Num, {Counts, Prefixes}) ->
                  NewCounts = inc_counts(Num, Counts),
                  UpdatedPrefixes = zip_with_prepend(NewCounts, Prefixes),
                  {NewCounts, UpdatedPrefixes}
          end,
          {Counts0, Prefixes0},
          Nums),
    TuplesList = [ list_to_tuple(lists:reverse(P)) || P <- PrefixesRev ],
    list_to_tuple(TuplesList).

%% Increment count for a specific value in the counts list (index = value)
inc_counts(Num, Counts) ->
    Index = Num,
    {Before, [Old | After]} = lists:split(Index, Counts),
    NewVal = Old + 1,
    Before ++ [NewVal] ++ After.

%% Prepend each count to its corresponding prefix list
zip_with_prepend(Counts, Prefixes) ->
    lists:zipwith(fun(Cnt, Pref) -> [Cnt | Pref] end, Counts, Prefixes).

%% Answer a single query using the precomputed prefix data
query_min_diff(L, R, PrefixData) ->
    query_loop(0, L, R, PrefixData, undefined, 101, 0).

query_loop(V, L, R, PrefixData, Prev, MinDiff, DistinctCount) when V =< 100 ->
    TupleV = element(V + 1, PrefixData),
    Cnt = element(R + 1, TupleV) - element(L, TupleV),
    if
        Cnt > 0 ->
            NewDistinct = DistinctCount + 1,
            case Prev of
                undefined ->
                    query_loop(V + 1, L, R, PrefixData, V, MinDiff, NewDistinct);
                _PrevVal ->
                    Diff = V - Prev,
                    NewMin = if Diff < MinDiff -> Diff; true -> MinDiff end,
                    query_loop(V + 1, L, R, PrefixData, V, NewMin, NewDistinct)
            end;
        true ->
            query_loop(V + 1, L, R, PrefixData, Prev, MinDiff, DistinctCount)
    end;
query_loop(_V, _L, _R, _PrefixData, _Prev, MinDiff, DistinctCount) ->
    case DistinctCount =< 1 of
        true -> -1;
        false -> MinDiff
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_difference(nums :: [integer], queries :: [[integer]]) :: [integer]
  def min_difference(nums, queries) do
    pos_map = build_pos_map(nums)

    Enum.map(queries, fn [l, r] ->
      query_min_diff(l, r, pos_map)
    end)
  end

  # Build a map from value (1..100) to an Erlang array of sorted positions
  defp build_pos_map(nums) do
    temp =
      Enum.with_index(nums)
      |> Enum.reduce(%{}, fn {v, idx}, acc ->
        Map.update(acc, v, [idx], fn lst -> [idx | lst] end)
      end)

    Enum.into(temp, %{}, fn {v, rev_list} ->
      arr = :array.from_list(Enum.reverse(rev_list))
      {v, arr}
    end)
  end

  defp query_min_diff(l, r, pos_map) do
    min_diff = 101   # larger than any possible difference (max value diff is 99)
    prev = nil
    distinct_cnt = 0

    for v <- 1..100 do
      case Map.get(pos_map, v) do
        nil ->
          :ok

        arr ->
          if present_in_range?(arr, l, r) do
            distinct_cnt = distinct_cnt + 1
            if prev != nil do
              diff = v - prev
              min_diff = if diff < min_diff, do: diff, else: min_diff
            end
            prev = v
          end
      end
    end

    if distinct_cnt < 2, do: -1, else: min_diff
  end

  # Check whether the array of positions has any element within [l, r]
  defp present_in_range?(arr, l, r) do
    size = :array.size(arr)
    idx = lower_bound(arr, l, 0, size)

    if idx < size do
      pos = :array.get(idx, arr)
      pos <= r
    else
      false
    end
  end

  # Find the first index in sorted array where value >= target
  defp lower_bound(_arr, _target, low, high) when low >= high, do: low

  defp lower_bound(arr, target, low, high) do
    mid = div(low + high, 2)
    val = :array.get(mid, arr)

    if val < target do
      lower_bound(arr, target, mid + 1, high)
    else
      lower_bound(arr, target, low, mid)
    end
  end
end
```

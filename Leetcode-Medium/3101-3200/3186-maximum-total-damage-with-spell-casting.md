# 3186. Maximum Total Damage With Spell Casting

## Cpp

```cpp
class Solution {
public:
    long long maximumTotalDamage(std::vector<int>& power) {
        if (power.empty()) return 0;
        std::sort(power.begin(), power.end());
        std::vector<long long> vals;
        std::vector<long long> wts;
        int n = power.size();
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && power[j] == power[i]) ++j;
            long long cnt = j - i;
            long long v = power[i];
            vals.push_back(v);
            wts.push_back(v * cnt);
            i = j;
        }
        int m = vals.size();
        std::vector<long long> dp(m, 0);
        for (int i = 0; i < m; ++i) {
            // find last index with value <= vals[i] - 3
            long long target = vals[i] - 3;
            int idx = std::upper_bound(vals.begin(), vals.end(), target) - vals.begin() - 1;
            long long take = wts[i] + (idx >= 0 ? dp[idx] : 0);
            long long notTake = (i > 0 ? dp[i-1] : 0);
            dp[i] = std::max(take, notTake);
        }
        return dp.back();
    }
};
```

## Java

```java
class Solution {
    public long maximumTotalDamage(int[] power) {
        java.util.HashMap<Integer, Long> map = new java.util.HashMap<>();
        for (int p : power) {
            map.put(p, map.getOrDefault(p, 0L) + (long) p);
        }
        int m = map.size();
        int[] valsTmp = new int[m];
        long[] sumsTmp = new long[m];
        int idx = 0;
        for (java.util.Map.Entry<Integer, Long> e : map.entrySet()) {
            valsTmp[idx] = e.getKey();
            sumsTmp[idx] = e.getValue(); // value * count
            idx++;
        }
        Integer[] order = new Integer[m];
        for (int i = 0; i < m; i++) order[i] = i;
        java.util.Arrays.sort(order, (a, b) -> Integer.compare(valsTmp[a], valsTmp[b]));
        int[] vals = new int[m];
        long[] sums = new long[m];
        for (int i = 0; i < m; i++) {
            vals[i] = valsTmp[order[i]];
            sums[i] = sumsTmp[order[i]];
        }
        long[] dp = new long[m];
        for (int i = 0; i < m; i++) {
            // binary search for the last index j where vals[j] <= vals[i] - 3
            int lo = 0, hi = i - 1, pos = -1;
            while (lo <= hi) {
                int mid = (lo + hi) >>> 1;
                if (vals[mid] <= vals[i] - 3) {
                    pos = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            long take = sums[i] + (pos >= 0 ? dp[pos] : 0L);
            long skip = i > 0 ? dp[i - 1] : 0L;
            dp[i] = Math.max(take, skip);
        }
        return dp[m - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        from collections import Counter
        import bisect

        cnt = Counter(power)
        vals = sorted(cnt.keys())
        weights = [v * cnt[v] for v in vals]

        n = len(vals)
        if n == 0:
            return 0

        dp = [0] * n
        for i in range(n):
            # skip current value
            best_skip = dp[i - 1] if i > 0 else 0

            # find the last index with value <= vals[i] - 3
            target = vals[i] - 3
            j = bisect.bisect_right(vals, target) - 1

            take = weights[i] + (dp[j] if j >= 0 else 0)

            dp[i] = best_skip if best_skip > take else take

        return dp[-1]
```

## Python3

```python
from typing import List
import bisect
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        vals = sorted(cnt.keys())
        weights = [v * cnt[v] for v in vals]
        n = len(vals)
        dp = [0] * n
        for i, val in enumerate(vals):
            take = weights[i]
            j = bisect.bisect_right(vals, val - 3) - 1
            if j >= 0:
                take += dp[j]
            skip = dp[i - 1] if i > 0 else 0
            dp[i] = take if take > skip else skip
        return dp[-1] if dp else 0
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

long long maximumTotalDamage(int* power, int powerSize) {
    if (powerSize == 0) return 0LL;

    qsort(power, powerSize, sizeof(int), cmp_int);

    // Allocate arrays for distinct values and their total contributions
    int *vals = (int *)malloc(powerSize * sizeof(int));
    long long *totals = (long long *)malloc(powerSize * sizeof(long long));
    int m = 0;

    for (int i = 0; i < powerSize; ) {
        int v = power[i];
        long long cnt = 0;
        while (i < powerSize && power[i] == v) {
            ++cnt;
            ++i;
        }
        vals[m] = v;
        totals[m] = (long long)v * cnt;
        ++m;
    }

    long long *dp = (long long *)malloc(m * sizeof(long long));

    for (int i = 0; i < m; ++i) {
        // binary search for the last index with value <= vals[i] - 3
        int lo = 0, hi = i - 1, prev = -1;
        int target = vals[i] - 3;
        while (lo <= hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (vals[mid] <= target) {
                prev = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        long long take = totals[i] + (prev != -1 ? dp[prev] : 0LL);
        long long notTake = (i > 0) ? dp[i - 1] : 0LL;
        dp[i] = (take > notTake) ? take : notTake;
    }

    long long result = dp[m - 1];

    free(vals);
    free(totals);
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaximumTotalDamage(int[] power)
    {
        // Aggregate total damage for each distinct spell value
        var sumByValue = new Dictionary<int, long>();
        foreach (int p in power)
        {
            if (!sumByValue.ContainsKey(p))
                sumByValue[p] = 0;
            sumByValue[p] += p; // add this occurrence's damage
        }

        // Create a sorted list of (value, totalWeight) pairs
        var spells = new List<(int value, long weight)>();
        foreach (var kvp in sumByValue)
            spells.Add((kvp.Key, kvp.Value));
        spells.Sort((a, b) => a.value.CompareTo(b.value));

        int n = spells.Count;
        if (n == 0) return 0;

        long[] dp = new long[n];

        for (int i = 0; i < n; i++)
        {
            long take = spells[i].weight;
            int v = spells[i].value;

            // Find the last index j (< i) with value <= v - 3
            int lo = 0, hi = i - 1, idxPrev = -1;
            while (lo <= hi)
            {
                int mid = (lo + hi) >> 1;
                if (spells[mid].value <= v - 3)
                {
                    idxPrev = mid;
                    lo = mid + 1;
                }
                else
                {
                    hi = mid - 1;
                }
            }

            if (idxPrev >= 0)
                take += dp[idxPrev];

            long notTake = i > 0 ? dp[i - 1] : 0;
            dp[i] = take > notTake ? take : notTake;
        }

        return dp[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} power
 * @return {number}
 */
var maximumTotalDamage = function(power) {
    const freq = new Map();
    for (const p of power) {
        freq.set(p, (freq.get(p) || 0) + 1);
    }
    const vals = Array.from(freq.keys()).sort((a, b) => a - b);
    const n = vals.length;
    const dp = new Array(n).fill(0);

    // binary search: rightmost index with vals[idx] <= target
    function findPrev(target) {
        let lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (vals[mid] <= target) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }

    for (let i = 0; i < n; ++i) {
        const v = vals[i];
        const weight = v * freq.get(v);
        // find previous index with value <= v-3
        const prevIdx = findPrev(v - 3);
        const include = weight + (prevIdx >= 0 ? dp[prevIdx] : 0);
        const exclude = i > 0 ? dp[i - 1] : 0;
        dp[i] = Math.max(include, exclude);
    }
    return dp[n - 1];
};
```

## Typescript

```typescript
function maximumTotalDamage(power: number[]): number {
    const freq = new Map<number, number>();
    for (const p of power) {
        freq.set(p, (freq.get(p) ?? 0) + 1);
    }
    const values = Array.from(freq.keys()).sort((a, b) => a - b);
    const n = values.length;
    if (n === 0) return 0;
    const dp = new Array<number>(n).fill(0);
    for (let i = 0; i < n; i++) {
        const v = values[i];
        const weight = v * (freq.get(v) ?? 0);
        // binary search for the last index with value <= v - 3
        let lo = 0, hi = i - 1, idx = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (values[mid] <= v - 3) {
                idx = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        const take = weight + (idx >= 0 ? dp[idx] : 0);
        const skip = i > 0 ? dp[i - 1] : 0;
        dp[i] = take > skip ? take : skip;
    }
    return dp[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $power
     * @return Integer
     */
    function maximumTotalDamage($power) {
        // Count occurrences of each damage value
        $cnt = [];
        foreach ($power as $p) {
            if (!isset($cnt[$p])) {
                $cnt[$p] = 0;
            }
            $cnt[$p]++;
        }

        // Sort unique values
        ksort($cnt);
        $values = array_keys($cnt);
        $n = count($values);

        // dp[i]: max damage using first i unique values (1‑based)
        $dp = array_fill(0, $n + 1, 0);

        for ($i = 1; $i <= $n; $i++) {
            $v = $values[$i - 1];
            $weight = $v * $cnt[$v];

            // Find the last index j (0‑based) where values[j] <= v - 3
            $low = 0;
            $high = $i - 2;   // indices before current one
            $jIdx = 0;        // dp index corresponding to that position (+1)

            while ($low <= $high) {
                $mid = intdiv($low + $high, 2);
                if ($values[$mid] <= $v - 3) {
                    $jIdx = $mid + 1;   // convert to dp index
                    $low = $mid + 1;
                } else {
                    $high = $mid - 1;
                }
            }

            // Choose max between skipping current value or taking it
            $dp[$i] = max($dp[$i - 1], $dp[$jIdx] + $weight);
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func maximumTotalDamage(_ power: [Int]) -> Int {
        var freq = [Int: Int]()
        for p in power {
            freq[p, default: 0] += 1
        }
        let sortedVals = freq.keys.sorted()
        let m = sortedVals.count
        if m == 0 { return 0 }
        
        var vals = [Int](repeating: 0, count: m)
        var weights = [Int](repeating: 0, count: m)
        for (i, v) in sortedVals.enumerated() {
            vals[i] = v
            weights[i] = v * freq[v]!   // total damage if we take all spells of value v
        }
        
        var dp = [Int](repeating: 0, count: m)
        var ptr = -1               // last index whose value <= current value - 3
        var bestPrev = 0           // max dp up to ptr
        
        for i in 0..<m {
            while ptr + 1 < i && vals[ptr + 1] <= vals[i] - 3 {
                ptr += 1
                if dp[ptr] > bestPrev { bestPrev = dp[ptr] }
            }
            let take = weights[i] + bestPrev
            let notTake = i > 0 ? dp[i - 1] : 0
            dp[i] = max(take, notTake)
        }
        return dp[m - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumTotalDamage(power: IntArray): Long {
        if (power.isEmpty()) return 0L
        val sumMap = HashMap<Int, Long>()
        for (p in power) {
            sumMap[p] = (sumMap[p] ?: 0L) + p.toLong()
        }
        val values = sumMap.keys.sorted()
        val n = values.size
        val dp = LongArray(n)
        for (i in 0 until n) {
            val v = values[i]
            val curSum = sumMap[v]!!
            // binary search for the last index with value <= v - 3
            var lo = 0
            var hi = i - 1
            var idx = -1
            while (lo <= hi) {
                val mid = (lo + hi) ushr 1
                if (values[mid] <= v - 3) {
                    idx = mid
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }
            val take = curSum + if (idx >= 0) dp[idx] else 0L
            val skip = if (i > 0) dp[i - 1] else 0L
            dp[i] = kotlin.math.max(take, skip)
        }
        return dp[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int maximumTotalDamage(List<int> power) {
    // Build frequency map
    final Map<int, int> freq = {};
    for (var p in power) {
      freq[p] = (freq[p] ?? 0) + 1;
    }

    // Sorted unique values
    final List<int> vals = freq.keys.toList()..sort();
    final int n = vals.length;
    if (n == 0) return 0;

    // Total damage for each unique value (value * count)
    final List<int> sums = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      final int v = vals[i];
      sums[i] = v * freq[v]!;
    }

    // DP array
    final List<int> dp = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      // Include current value: need previous index with value <= vals[i] - 3
      int include = sums[i];
      int lo = 0, hi = i - 1, idx = -1;
      while (lo <= hi) {
        final int mid = (lo + hi) >> 1;
        if (vals[mid] <= vals[i] - 3) {
          idx = mid;
          lo = mid + 1;
        } else {
          hi = mid - 1;
        }
      }
      if (idx >= 0) include += dp[idx];

      // Exclude current value
      int exclude = i > 0 ? dp[i - 1] : 0;

      dp[i] = include > exclude ? include : exclude;
    }

    return dp[n - 1];
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func maximumTotalDamage(power []int) int64 {
	if len(power) == 0 {
		return 0
	}
	// Count occurrences of each damage value.
	cnt := make(map[int]int64, len(power))
	for _, v := range power {
		cnt[v]++
	}

	// Extract and sort unique values.
	vals := make([]int, 0, len(cnt))
	for v := range cnt {
		vals = append(vals, v)
	}
	sort.Ints(vals)

	m := len(vals)
	weights := make([]int64, m)
	for i, v := range vals {
		weights[i] = int64(v) * cnt[v]
	}

	dp := make([]int64, m)
	for i := 0; i < m; i++ {
		// Find the last index with value <= vals[i]-3.
		target := vals[i] - 3
		idx := sort.Search(m, func(k int) bool { return vals[k] > target })
		prevIdx := idx - 1

		take := weights[i]
		if prevIdx >= 0 {
			take += dp[prevIdx]
		}
		if i > 0 && dp[i-1] > take {
			dp[i] = dp[i-1]
		} else {
			dp[i] = take
		}
	}
	return dp[m-1]
}
```

## Ruby

```ruby
def maximum_total_damage(power)
  freq = Hash.new(0)
  power.each { |v| freq[v] += v }

  vals = freq.keys.sort
  sums = vals.map { |v| freq[v] }

  n = vals.size
  dp = Array.new(n + 1, 0)

  p = 0
  (1..n).each do |i|
    cur_val = vals[i - 1]
    while p < i && vals[p] <= cur_val - 3
      p += 1
    end
    take = dp[p] + sums[i - 1]
    dp[i] = dp[i - 1] > take ? dp[i - 1] : take
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def maximumTotalDamage(power: Array[Int]): Long = {
        import scala.collection.mutable

        // Count occurrences of each damage value
        val freq = mutable.Map[Long, Long]()
        for (p <- power) {
            val v = p.toLong
            freq(v) = freq.getOrElse(v, 0L) + 1L
        }

        if (freq.isEmpty) return 0L

        // Sort unique damage values
        val vals = freq.keys.toArray.sorted
        val n = vals.length
        val dp = new Array[Long](n)

        for (i <- 0 until n) {
            val v = vals(i)
            val weight = v * freq(v) // total damage if we take all spells of this value

            // Binary search for the last index j where vals(j) <= v - 3
            var lo = 0
            var hi = i - 1
            var idx = -1
            while (lo <= hi) {
                val mid = (lo + hi) >>> 1
                if (vals(mid) <= v - 3) {
                    idx = mid
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }

            val include = weight + (if (idx >= 0) dp(idx) else 0L)
            val exclude = if (i > 0) dp(i - 1) else 0L
            dp(i) = math.max(include, exclude)
        }

        dp(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_total_damage(power: Vec<i32>) -> i64 {
        use std::collections::HashMap;
        // Count occurrences of each damage value
        let mut cnt: HashMap<i32, i64> = HashMap::new();
        for p in power {
            *cnt.entry(p).or_insert(0) += 1;
        }

        // Create sorted list of unique values and their total contributions
        let mut pairs: Vec<(i32, i64)> = cnt
            .into_iter()
            .map(|(val, c)| (val, val as i64 * c))
            .collect();
        pairs.sort_by_key(|&(v, _)| v);

        let n = pairs.len();
        let mut values = Vec::with_capacity(n);
        let mut totals = Vec::with_capacity(n);
        for (v, tot) in pairs {
            values.push(v);
            totals.push(tot);
        }

        // dp[i] = max total using first i unique values (i from 0..=n)
        let mut dp = vec![0_i64; n + 1];
        for i in 1..=n {
            let v = values[i - 1];
            let cur_total = totals[i - 1];

            // Find the largest index j such that values[j] <= v - 3
            // pos will be number of elements satisfying the condition (i.e., j+1)
            let target = v - 3;
            let mut lo = 0usize;
            let mut hi = n;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if values[mid] <= target {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            let pos = lo; // dp[pos] corresponds to best up to that index

            dp[i] = dp[i - 1].max(dp[pos] + cur_total);
        }

        dp[n]
    }
}
```

## Racket

```racket
(define/contract (maximum-total-damage power)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((cnt (make-hash))
         (add-count
          (lambda (x)
            (hash-set! cnt x (+ 1 (hash-ref cnt x 0))))))
    (for-each add-count power)
    (define keys (sort (hash-keys cnt) <))
    (define n (length keys))
    (if (= n 0)
        0
        (let* ((vals (list->vector keys))
               (w (make-vector n)))
          ;; total damage contributed by each distinct value
          (for ([i (in-range n)])
            (let* ((v (vector-ref vals i))
                   (c (hash-ref cnt v)))
              (vector-set! w i (* v c))))
          (define dp (make-vector n))
          (for ([i (in-range n)])
            ;; binary search for the last index j < i with vals[j] <= vals[i] - 3
            (define prev-index
              (let loop ((lo 0) (hi i))
                (if (< lo hi)
                    (let* ((mid (quotient (+ lo hi) 2)))
                      (if (<= (vector-ref vals mid) (- (vector-ref vals i) 3))
                          (loop (+ mid 1) hi)
                          (loop lo mid)))
                    (- lo 1))))
            (define include
              (+ (vector-ref w i)
                 (if (>= prev-index 0) (vector-ref dp prev-index) 0)))
            (define exclude (if (> i 0) (vector-ref dp (- i 1)) 0))
            (vector-set! dp i (max include exclude)))
          (vector-ref dp (- n 1))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_total_damage/1]).

-spec maximum_total_damage(Power :: [integer()]) -> integer().
maximum_total_damage(Power) ->
    Sorted = lists:sort(Power),
    {ValuesList, WeightsList} = aggregate(Sorted),
    VTuple = list_to_tuple(ValuesList),
    WTuple = list_to_tuple(WeightsList),
    N = tuple_size(VTuple),
    DPMap = dp_forward(1, N, VTuple, WTuple, #{}),
    maps:get(N, DPMap).

aggregate([]) -> {[], []};
aggregate([H|T]) ->
    aggregate(T, H, 1, [], []).

aggregate([], Prev, Cnt, VAcc, WAcc) ->
    {lists:reverse([Prev | VAcc]), lists:reverse([Prev*Cnt | WAcc])};
aggregate([H|T], Prev, Cnt, VAcc, WAcc) when H =:= Prev ->
    aggregate(T, Prev, Cnt+1, VAcc, WAcc);
aggregate([H|T], Prev, Cnt, VAcc, WAcc) ->
    NewVAcc = [Prev | VAcc],
    NewWAcc = [Prev*Cnt | WAcc],
    aggregate(T, H, 1, NewVAcc, NewWAcc).

dp_forward(Index, N, _VT, _WT, DPMap) when Index > N ->
    DPMap;
dp_forward(Index, N, VT, WT, DPMap) ->
    Val = element(Index, VT),
    Weight = element(Index, WT),
    PrevIdx = case Index of
                  1 -> 0;
                  _ -> find_prev(VT, 1, Index-1, Val - 3)
              end,
    PrevDP = case maps:find(PrevIdx, DPMap) of
                 {ok, V} -> V;
                 error -> 0
             end,
    Take = Weight + PrevDP,
    Skip = case maps:find(Index-1, DPMap) of
               {ok, V} -> V;
               error -> 0
           end,
    Curr = if Take > Skip -> Take; true -> Skip end,
    NewDPMap = maps:put(Index, Curr, DPMap),
    dp_forward(Index+1, N, VT, WT, NewDPMap).

find_prev(VT, L, H, Target) when L =< H ->
    Mid = (L + H) div 2,
    MidVal = element(Mid, VT),
    if MidVal =< Target ->
            find_prev(VT, Mid+1, H, Target);
       true ->
            find_prev(VT, L, Mid-1, Target)
    end;
find_prev(_VT, _L, H, _Target) ->
    H.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_total_damage(power :: [integer]) :: integer
  def maximum_total_damage(power) do
    # Count occurrences of each power value
    counts =
      Enum.reduce(power, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    # Sort unique values
    sorted = counts |> Map.to_list() |> Enum.sort_by(fn {v, _} -> v end)
    values = Enum.map(sorted, fn {v, _} -> v end)
    weights = Enum.map(sorted, fn {v, c} -> v * c end)

    n = length(values)
    if n == 0 do
      0
    else
      vals_tuple = List.to_tuple(values)
      wts_tuple = List.to_tuple(weights)

      # Helper to move pointer p forward while compatible
      move_pointer = fn p, i, limit ->
        cond do
          p + 1 < i and elem(vals_tuple, p + 1) <= limit ->
            # tail‑recursive advance
            Stream.iterate(p + 1, &(&1 + 1))
            |> Enum.take_while(fn idx -> idx < i and elem(vals_tuple, idx) <= limit end)
            |> List.last()
          true ->
            p
        end
      end

      # Initialize DP array using Erlang's :array for O(1) access
      dp_arr = :array.new(n, default: 0)

      {final_dp, _} =
        Enum.reduce(0..(n - 1), {dp_arr, -1}, fn i, {dp_acc, p_acc} ->
          limit = elem(vals_tuple, i) - 3
          # advance pointer to the last compatible index
          new_p =
            if p_acc + 1 < i and elem(vals_tuple, p_acc + 1) <= limit do
              move_pointer.(p_acc, i, limit)
            else
              p_acc
            end

          take =
            elem(wts_tuple, i) +
              (if new_p >= 0, do: :array.get(new_p, dp_acc), else: 0)

          not_take = if i > 0, do: :array.get(i - 1, dp_acc), else: 0
          best = if take > not_take, do: take, else: not_take

          { :array.set(i, best, dp_acc), new_p }
        end)

      :array.get(n - 1, final_dp)
    end
  end
end
```

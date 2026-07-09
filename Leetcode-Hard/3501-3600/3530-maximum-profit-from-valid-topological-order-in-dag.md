# 3530. Maximum Profit from Valid Topological Order in DAG

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(int n, vector<vector<int>>& edges, vector<int>& score) {
        vector<unsigned int> pre(n, 0);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            pre[v] |= (1u << u);
        }
        int totalMask = 1 << n;
        const long long NEG = LLONG_MIN / 4;
        vector<long long> dp(totalMask, NEG);
        dp[0] = 0;
        for (int mask = 0; mask < totalMask; ++mask) {
            if (dp[mask] == NEG) continue;
            int placed = __builtin_popcount(mask);
            int pos = placed + 1; // next position (1‑based)
            unsigned int notTaken = (~(unsigned int)mask) & ((1u << n) - 1);
            for (int i = 0; i < n; ++i) {
                if (!(notTaken & (1u << i))) continue;
                if ((pre[i] & ~((unsigned int)mask)) == 0) { // all prerequisites already taken
                    int nxtMask = mask | (1 << i);
                    long long val = dp[mask] + 1LL * score[i] * pos;
                    if (val > dp[nxtMask]) dp[nxtMask] = val;
                }
            }
        }
        return (int)dp[totalMask - 1];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxProfit(int n, int[][] edges, int[] score) {
        int[] pre = new int[n];
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            pre[v] |= 1 << u;
        }
        int fullMask = (1 << n) - 1;
        long[] dp = new long[1 << n];
        Arrays.fill(dp, Long.MIN_VALUE / 4);
        dp[0] = 0;
        for (int mask = 0; mask <= fullMask; ++mask) {
            long cur = dp[mask];
            if (cur == Long.MIN_VALUE / 4) continue;
            int cnt = Integer.bitCount(mask);
            int pos = cnt + 1;
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) continue;
                if ((pre[i] & ~mask) != 0) continue;
                int nextMask = mask | (1 << i);
                long val = cur + (long) score[i] * pos;
                if (val > dp[nextMask]) dp[nextMask] = val;
            }
        }
        return (int) dp[fullMask];
    }
}
```

## Python

```python
class Solution(object):
    def maxProfit(self, n, edges, score):
        """
        :type n: int
        :type edges: List[List[int]]
        :type score: List[int]
        :rtype: int
        """
        pre = [0] * n
        for u, v in edges:
            pre[v] |= 1 << u

        full_mask = (1 << n) - 1
        dp = [-10**18] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            cur = dp[mask]
            if cur < 0:
                continue
            pos = mask.bit_count() + 1
            remaining = full_mask ^ mask
            r = remaining
            while r:
                low = r & -r
                i = low.bit_length() - 1
                if (pre[i] & ~mask) == 0:
                    new_mask = mask | (1 << i)
                    val = cur + score[i] * pos
                    if val > dp[new_mask]:
                        dp[new_mask] = val
                r &= r - 1

        return dp[full_mask]
```

## Python3

```python
from typing import List

class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        pred = [0] * n
        for u, v in edges:
            pred[v] |= 1 << u

        full_mask = (1 << n) - 1
        dp = [-10**18] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            cur = dp[mask]
            if cur < 0:
                continue
            pos = mask.bit_count() + 1
            remaining = (~mask) & full_mask
            while remaining:
                lsb = remaining & -remaining
                node = lsb.bit_length() - 1
                if (pred[node] & mask) == pred[node]:
                    new_mask = mask | lsb
                    val = cur + score[node] * pos
                    if val > dp[new_mask]:
                        dp[new_mask] = val
                remaining ^= lsb

        return dp[full_mask]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int maxProfit(int n, int** edges, int edgesSize, int* edgesColSize, int* score, int scoreSize) {
    unsigned int prereq[22] = {0};
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        prereq[v] |= 1u << u;
    }

    int totalMask = 1 << n;
    long long *dp = (long long *)malloc(sizeof(long long) * totalMask);
    const long long NEG_INF = -(1LL<<60);
    for (int i = 0; i < totalMask; ++i) dp[i] = NEG_INF;
    dp[0] = 0;

    unsigned int fullMask = (1u << n) - 1;
    for (int mask = 0; mask < totalMask; ++mask) {
        if (dp[mask] == NEG_INF) continue;
        int pos = __builtin_popcount((unsigned)mask) + 1;
        unsigned int remaining = fullMask ^ (unsigned)mask;
        while (remaining) {
            unsigned int vbit = remaining & -remaining;
            int v = __builtin_ctz(vbit);
            if ((prereq[v] & ~((unsigned)mask)) == 0) {
                int newMask = mask | (1 << v);
                long long val = dp[mask] + (long long)score[v] * pos;
                if (val > dp[newMask]) dp[newMask] = val;
            }
            remaining ^= vbit;
        }
    }

    long long ans = dp[totalMask - 1];
    free(dp);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Numerics;

public class Solution {
    public int MaxProfit(int n, int[][] edges, int[] score) {
        int[] prereqMask = new int[n];
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            prereqMask[v] |= 1 << u;
        }

        int totalMasks = 1 << n;
        long[] dp = new long[totalMasks];
        for (int i = 0; i < totalMasks; i++) dp[i] = long.MinValue;
        dp[0] = 0;

        for (int mask = 0; mask < totalMasks; mask++) {
            if (dp[mask] == long.MinValue) continue;
            int placed = BitOperations.PopCount((uint)mask);
            int pos = placed + 1; // next position (1‑based)

            for (int v = 0; v < n; v++) {
                if ((mask & (1 << v)) != 0) continue; // already placed
                if ((prereqMask[v] & ~mask) != 0) continue; // prerequisites not satisfied

                int newMask = mask | (1 << v);
                long profit = dp[mask] + (long)score[v] * pos;
                if (profit > dp[newMask]) dp[newMask] = profit;
            }
        }

        return (int)dp[totalMasks - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} score
 * @return {number}
 */
var maxProfit = function(n, edges, score) {
    const fullMask = 1 << n;
    // prerequisite mask for each node
    const pre = new Uint32Array(n);
    for (const [u, v] of edges) {
        pre[v] |= (1 << u);
    }
    // popcount for all masks
    const pc = new Uint8Array(fullMask);
    for (let m = 1; m < fullMask; ++m) {
        pc[m] = pc[m >> 1] + (m & 1);
    }
    const dp = new Float64Array(fullMask);
    for (let i = 0; i < fullMask; ++i) dp[i] = -Infinity;
    dp[0] = 0;
    for (let mask = 0; mask < fullMask; ++mask) {
        const curVal = dp[mask];
        if (curVal === -Infinity) continue;
        const pos = pc[mask] + 1; // next position (1‑based)
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) continue;               // already taken
            if ((pre[i] & ~mask) !== 0) continue;         // prerequisites not satisfied
            const newMask = mask | (1 << i);
            const cand = curVal + score[i] * pos;
            if (cand > dp[newMask]) dp[newMask] = cand;
        }
    }
    return dp[fullMask - 1];
};
```

## Typescript

```typescript
function maxProfit(n: number, edges: number[][], score: number[]): number {
    const fullMask = (1 << n) - 1;
    const pre = new Array<number>(n).fill(0);
    for (const [u, v] of edges) {
        pre[v] |= 1 << u;
    }

    const size = 1 << n;
    const dp = new Float64Array(size);
    for (let i = 0; i < size; i++) dp[i] = -Infinity;
    dp[0] = 0;

    const cnt = new Uint8Array(size);
    for (let mask = 1; mask < size; mask++) {
        cnt[mask] = cnt[mask >> 1] + (mask & 1);
    }

    for (let mask = 0; mask < size; mask++) {
        const cur = dp[mask];
        if (cur === -Infinity) continue;
        const pos = cnt[mask] + 1;
        for (let v = 0; v < n; v++) {
            const bit = 1 << v;
            if (mask & bit) continue;
            if ((pre[v] & mask) === pre[v]) {
                const nmask = mask | bit;
                const val = cur + score[v] * pos;
                if (val > dp[nmask]) dp[nmask] = val;
            }
        }
    }

    return dp[fullMask];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $score
     * @return Integer
     */
    function maxProfit($n, $edges, $score) {
        $pre = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $pre[$v] |= (1 << $u);
        }
        $size = 1 << $n;
        $dp = new SplFixedArray($size);
        $dp[0] = 0;

        for ($mask = 0; $mask < $size; $mask++) {
            $cur = $dp[$mask];
            if ($cur === null) continue;

            // count bits set in mask
            $cnt = 0;
            $tmp = $mask;
            while ($tmp) {
                $tmp &= ($tmp - 1);
                $cnt++;
            }
            $pos = $cnt + 1; // next position (1‑based)

            for ($v = 0; $v < $n; $v++) {
                if ((($mask >> $v) & 1) === 0) { // not yet taken
                    if (($pre[$v] & (~$mask)) === 0) { // all prerequisites already taken
                        $newMask = $mask | (1 << $v);
                        $val = $cur + $score[$v] * $pos;
                        $prev = $dp[$newMask];
                        if ($prev === null || $val > $prev) {
                            $dp[$newMask] = $val;
                        }
                    }
                }
            }
        }

        return $dp[$size - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maxProfit(_ n: Int, _ edges: [[Int]], _ score: [Int]) -> Int {
        var pre = [Int](repeating: 0, count: n)
        for e in edges {
            let u = e[0]
            let v = e[1]
            pre[v] |= (1 << u)
        }
        let totalMask = 1 << n
        var dp = [Int](repeating: -1, count: totalMask)
        dp[0] = 0
        for mask in 0..<totalMask {
            let cur = dp[mask]
            if cur < 0 { continue }
            let placed = mask.nonzeroBitCount
            let nextPos = placed + 1
            for i in 0..<n {
                let bit = 1 << i
                if (mask & bit) == 0 && (pre[i] & ~mask) == 0 {
                    let newMask = mask | bit
                    let profit = cur + nextPos * score[i]
                    if profit > dp[newMask] {
                        dp[newMask] = profit
                    }
                }
            }
        }
        return dp[totalMask - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProfit(n: Int, edges: Array<IntArray>, score: IntArray): Int {
        val prereq = IntArray(n)
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            prereq[v] = prereq[v] or (1 shl u)
        }
        val totalMask = 1 shl n
        val dp = LongArray(totalMask) { Long.MIN_VALUE }
        dp[0] = 0L
        for (mask in 0 until totalMask) {
            val cur = dp[mask]
            if (cur == Long.MIN_VALUE) continue
            val placed = Integer.bitCount(mask)
            val nextPos = placed + 1
            for (v in 0 until n) {
                val bit = 1 shl v
                if ((mask and bit) != 0) continue
                if ((prereq[v] and mask) == prereq[v]) {
                    val newMask = mask or bit
                    val profit = cur + score[v].toLong() * nextPos
                    if (profit > dp[newMask]) dp[newMask] = profit
                }
            }
        }
        return dp[totalMask - 1].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxProfit(int n, List<List<int>> edges, List<int> score) {
    int totalMask = 1 << n;
    // Predecessor mask for each node
    List<int> preMask = List.filled(n, 0);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      preMask[v] |= (1 << u);
    }

    // Popcount for all masks
    List<int> popcnt = List.filled(totalMask, 0);
    for (int i = 1; i < totalMask; ++i) {
      popcnt[i] = popcnt[i >> 1] + (i & 1);
    }

    const int negInf = -(1 << 60);
    List<int> dp = List.filled(totalMask, negInf);
    dp[0] = 0;

    for (int mask = 0; mask < totalMask; ++mask) {
      if (dp[mask] == negInf) continue;
      int pos = popcnt[mask] + 1; // next position (1‑based)
      for (int v = 0; v < n; ++v) {
        if ((mask >> v & 1) == 1) continue; // already taken
        if ((preMask[v] & ~mask) != 0) continue; // some predecessor not yet taken
        int newMask = mask | (1 << v);
        int val = dp[mask] + score[v] * pos;
        if (val > dp[newMask]) dp[newMask] = val;
      }
    }

    return dp[totalMask - 1];
  }
}
```

## Golang

```go
import "math/bits"

func maxProfit(n int, edges [][]int, score []int) int {
	prereq := make([]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		prereq[v] |= 1 << u
	}
	size := 1 << n
	const negInf int64 = -1 << 60
	dp := make([]int64, size)
	for i := range dp {
		dp[i] = negInf
	}
	dp[0] = 0
	fullMask := size - 1

	for mask := 0; mask <= fullMask; mask++ {
		if dp[mask] == negInf {
			continue
		}
		pos := bits.OnesCount(uint(mask)) + 1
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				continue
			}
			if prereq[i]&^mask != 0 {
				continue
			}
			newMask := mask | (1 << i)
			val := dp[mask] + int64(score[i])*int64(pos)
			if val > dp[newMask] {
				dp[newMask] = val
			}
		}
	}
	return int(dp[fullMask])
}
```

## Ruby

```ruby
def max_profit(n, edges, score)
  prereq = Array.new(n, 0)
  edges.each do |u, v|
    prereq[v] |= (1 << u)
  end

  total_masks = 1 << n
  dp = Array.new(total_masks, -(1 << 60))
  dp[0] = 0

  bits = Array.new(total_masks, 0)
  (1...total_masks).each do |mask|
    bits[mask] = bits[mask >> 1] + (mask & 1)
  end

  (0...total_masks).each do |mask|
    cur = dp[mask]
    next if cur == -(1 << 60)

    pos = bits[mask] + 1
    n.times do |v|
      bit = 1 << v
      next if (mask & bit) != 0
      # all prerequisites of v must be already in mask
      if (prereq[v] & ~mask).zero?
        new_mask = mask | bit
        profit = cur + score[v] * pos
        dp[new_mask] = profit if profit > dp[new_mask]
      end
    end
  end

  dp[total_masks - 1]
end
```

## Scala

```scala
object Solution {
    def maxProfit(n: Int, edges: Array[Array[Int]], score: Array[Int]): Int = {
        val prereq = new Array[Int](n)
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            prereq(v) |= 1 << u
        }
        val totalMask = 1 << n
        val dp = Array.fill[Long](totalMask)(Long.MinValue)
        dp(0) = 0L
        for (mask <- 0 until totalMask) {
            val cur = dp(mask)
            if (cur != Long.MinValue) {
                val cnt = Integer.bitCount(mask)
                var i = 0
                while (i < n) {
                    val bit = 1 << i
                    if ((mask & bit) == 0 && (prereq(i) & ~mask) == 0) {
                        val newMask = mask | bit
                        val profit = cur + (cnt + 1).toLong * score(i)
                        if (profit > dp(newMask)) dp(newMask) = profit
                    }
                    i += 1
                }
            }
        }
        dp(totalMask - 1).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_profit(n: i32, edges: Vec<Vec<i32>>, score: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut pre = vec![0usize; n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            pre[v] |= 1 << u;
        }
        let total = 1usize << n;
        let mut dp = vec![-1i64; total];
        dp[0] = 0;
        for mask in 0..total {
            if dp[mask] < 0 { continue; }
            let cnt = mask.count_ones() as i64;
            for i in 0..n {
                if (mask >> i) & 1 == 1 { continue; }
                if pre[i] & mask != pre[i] { continue; }
                let new_mask = mask | (1 << i);
                let profit = dp[mask] + score[i] as i64 * (cnt + 1);
                if profit > dp[new_mask] {
                    dp[new_mask] = profit;
                }
            }
        }
        dp[total - 1] as i32
    }
}
```

## Racket

```racket
(define/contract (max-profit n edges score)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ((size (arithmetic-shift 1 n))
         (dp (make-vector size -1000000000000))
         (popcnt (make-vector size 0))
         (pre (make-vector n 0))
         (scorev (list->vector score)))
    ;; prerequisite masks
    (for ([e edges])
      (let* ((u (first e))
             (v (second e)))
        (vector-set! pre v (bitwise-ior (vector-ref pre v) (arithmetic-shift 1 u)))))
    ;; popcount table
    (do ((mask 1 (+ mask 1))) ((= mask size))
      (let* ((lsb (bitwise-and mask (- mask)))
             (prev (bitwise-xor mask lsb)))
        (vector-set! popcnt mask (+ 1 (vector-ref popcnt prev)))))
    ;; DP over subsets
    (vector-set! dp 0 0)
    (do ((mask 0 (+ mask 1))) ((= mask size))
      (let ((cur (vector-ref dp mask)))
        (when (> cur -1000000000000)
          (let* ((k (vector-ref popcnt mask))
                 (pos (+ k 1)))
            (do ((i 0 (+ i 1))) ((= i n))
              (unless (bitwise-bit-set? mask i)
                (let ((need (vector-ref pre i)))
                  (when (= (bitwise-and need (bitwise-not mask)) 0)
                    (let* ((newmask (bitwise-ior mask (arithmetic-shift 1 i)))
                           (newval (+ cur (* (vector-ref scorev i) pos))))
                      (when (> newval (vector-ref dp newmask))
                        (vector-set! dp newmask newval))))))))))
    (vector-ref dp (- size 1))))
```

## Erlang

```erlang
-spec max_profit(N :: integer(), Edges :: [[integer()]], Score :: [integer()]) -> integer().
max_profit(N, Edges, Score) ->
    % Build prerequisite bitmask for each node
    PreArr0 = array:new(N, {default, 0}),
    PreArr = lists:foldl(fun([U, V], Arr) ->
                Old = array:get(V, Arr),
                array:set(V, Old bor (1 bsl U), Arr)
            end, PreArr0, Edges),

    Size = 1 bsl N,
    DP0 = array:new(Size, {default, -1000000000000}),
    DP1 = array:set(0, 0, DP0),

    FinalDP = dp_loop(0, Size - 1, N, PreArr, Score, DP1),
    array:get(Size - 1, FinalDP).

%% ------------------------------------------------------------------
%% DP over subsets
dp_loop(Mask, MaxMask, N, PreArr, Score, DP) when Mask =< MaxMask ->
    CurProf = array:get(Mask, DP),
    if
        CurProf < 0 ->
            dp_loop(Mask + 1, MaxMask, N, PreArr, Score, DP);
        true ->
            Pos = bit_count(Mask) + 1,
            DP2 = process_nodes(0, N, Mask, Pos, CurProf, PreArr, Score, DP),
            dp_loop(Mask + 1, MaxMask, N, PreArr, Score, DP2)
    end;
dp_loop(_, _, _, _, _, DP) ->
    DP.

process_nodes(I, N, Mask, Pos, CurProf, PreArr, Score, DP) when I < N ->
    Bit = 1 bsl I,
    case (Mask band Bit) of
        0 ->
            Pre = array:get(I, PreArr),
            if (Pre band Mask) == Pre ->
                    NewMask = Mask bor Bit,
                    NodeScore = lists:nth(I + 1, Score),
                    NewProf = CurProf + NodeScore * Pos,
                    Existing = array:get(NewMask, DP),
                    MaxProf = if NewProf > Existing -> NewProf; true -> Existing end,
                    DP2 = if MaxProf > Existing ->
                                array:set(NewMask, MaxProf, DP);
                          true ->
                                DP
                          end,
                    process_nodes(I + 1, N, Mask, Pos, CurProf, PreArr, Score, DP2);
               true ->
                    process_nodes(I + 1, N, Mask, Pos, CurProf, PreArr, Score, DP)
            end;
        _ -> % already taken
            process_nodes(I + 1, N, Mask, Pos, CurProf, PreArr, Score, DP)
    end;
process_nodes(_, _, _, _, _, _, _, DP) ->
    DP.

%% ------------------------------------------------------------------
%% Bit count (popcount)
bit_count(0) -> 0;
bit_count(X) -> 1 + bit_count(X band (X - 1)).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_profit(n :: integer, edges :: [[integer]], score :: [integer]) :: integer
  def max_profit(n, edges, score) do
    import Bitwise

    # prerequisite bitmask for each node
    prereq_arr =
      Enum.reduce(edges, :array.new(n, 0), fn [u, v], acc ->
        cur = :array.get(v, acc)
        :array.set(v, cur ||| (1 <<< u), acc)
      end)

    prereq_list = for i <- 0..(n - 1), do: :array.get(i, prereq_arr)

    max_mask = 1 <<< n

    # ETS table for DP values
    table = :ets.new(:dp_table, [:set, :private])

    :ets.insert(table, {0, 0})

    for mask <- 0..(max_mask - 1) do
      case :ets.lookup(table, mask) do
        [] ->
          :ok

        [{^mask, cur}] ->
          pos = :erlang.popcount(mask) + 1

          for v <- 0..(n - 1) do
            bit = 1 <<< v

            if (mask &&& bit) == 0 and ((prereq_list |> Enum.at(v)) &&& mask) == Enum.at(prereq_list, v) do
              new_mask = mask ||| bit
              new_profit = cur + score[v] * pos

              case :ets.lookup(table, new_mask) do
                [] ->
                  :ets.insert(table, {new_mask, new_profit})

                [{^new_mask, old}] when new_profit > old ->
                  :ets.insert(table, {new_mask, new_profit})

                _ ->
                  :ok
              end
            else
              :ok
            end
          end
      end
    end

    [{_, ans}] = :ets.lookup(table, max_mask - 1)
    ans
  end
end
```

# 2742. Painting the Walls

## Cpp

```cpp
class Solution {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        int n = cost.size();
        const long long INF = (1LL<<60);
        vector<long long> dp(n + 1, INF), ndp;
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            int w = 1 + time[i];
            ndp = dp;
            for (int covered = 0; covered <= n; ++covered) {
                if (dp[covered] == INF) continue;
                int newCov = covered + w;
                if (newCov > n) newCov = n;
                ndp[newCov] = min(ndp[newCov], dp[covered] + cost[i]);
            }
            dp.swap(ndp);
        }
        return (int)dp[n];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int paintWalls(int[] cost, int[] time) {
        int n = cost.length;
        long INF = Long.MAX_VALUE / 4;
        long[] prev = new long[n + 1];
        Arrays.fill(prev, INF);
        prev[0] = 0;

        for (int i = n - 1; i >= 0; --i) {
            long[] cur = new long[n + 1];
            Arrays.fill(cur, INF);
            cur[0] = 0;
            int cover = 1 + time[i];
            for (int remain = 1; remain <= n; ++remain) {
                long dontPaint = prev[remain];
                int nextRemain = Math.max(0, remain - cover);
                long paint = cost[i] + prev[nextRemain];
                cur[remain] = Math.min(dontPaint, paint);
            }
            prev = cur;
        }
        return (int) prev[n];
    }
}
```

## Python

```python
class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        n = len(cost)
        INF = 10**15
        # prevDp corresponds to dp[i+1][*]
        prev = [INF] * (n + 1)
        prev[0] = 0  # no remaining walls needs zero cost

        for i in range(n - 1, -1, -1):
            cur = [INF] * (n + 1)
            cur[0] = 0
            t = time[i]
            c = cost[i]
            for remain in range(1, n + 1):
                # option 1: hire paid painter for wall i
                nxt_remain = remain - 1 - t
                if nxt_remain < 0:
                    nxt_remain = 0
                paint = c + prev[nxt_remain]
                # option 2: skip hiring for this wall
                dont = prev[remain]
                cur[remain] = paint if paint < dont else dont
            prev = cur

        return prev[n]
```

## Python3

```python
from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        INF = 10**15
        prev = [INF] * (n + 1)
        prev[0] = 0  # no walls needed costs nothing

        for i in range(n - 1, -1, -1):
            dp = [0] * (n + 1)
            dp[0] = 0
            t = time[i]
            c = cost[i]
            for remain in range(1, n + 1):
                # walls painted by paid painter: 1 + t
                nxt = remain - 1 - t
                if nxt < 0:
                    nxt = 0
                paint = c + prev[nxt]
                dont = prev[remain]
                dp[remain] = paint if paint < dont else dont
            prev = dp

        return prev[n]
```

## C

```c
#include <stdlib.h>

int paintWalls(int* cost, int costSize, int* time, int timeSize) {
    int n = costSize;
    const long long INF = 400000000000000LL; // sufficiently large
    
    long long *prev = (long long *)malloc((n + 1) * sizeof(long long));
    long long *cur  = (long long *)malloc((n + 1) * sizeof(long long));
    
    for (int i = 0; i <= n; ++i) prev[i] = INF;
    prev[0] = 0;
    
    for (int idx = n - 1; idx >= 0; --idx) {
        cur[0] = 0;
        for (int remain = 1; remain <= n; ++remain) {
            int nxt = remain - 1 - time[idx];
            if (nxt < 0) nxt = 0;
            long long paint = (long long)cost[idx] + prev[nxt];
            long long dont  = prev[remain];
            cur[remain] = paint < dont ? paint : dont;
        }
        long long *tmp = prev;
        prev = cur;
        cur = tmp;
    }
    
    int result = (int)prev[n];
    free(prev);
    free(cur);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int PaintWalls(int[] cost, int[] time) {
        int n = cost.Length;
        int INF = int.MaxValue / 2;

        int[] prev = new int[n + 1];
        for (int j = 1; j <= n; ++j) prev[j] = INF;
        prev[0] = 0;

        for (int i = n - 1; i >= 0; --i) {
            int[] cur = new int[n + 1];
            cur[0] = 0;
            for (int remain = 1; remain <= n; ++remain) {
                int idx = remain - 1 - time[i];
                if (idx < 0) idx = 0;
                long paintCost = (long)cost[i] + prev[idx];
                int dontPaint = prev[remain];
                cur[remain] = paintCost < dontPaint ? (int)paintCost : dontPaint;
            }
            prev = cur;
        }

        return prev[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cost
 * @param {number[]} time
 * @return {number}
 */
var paintWalls = function(cost, time) {
    const n = cost.length;
    const INF = 1e15;
    let dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let i = 0; i < n; ++i) {
        const weight = Math.min(n, 1 + time[i]); // walls covered if this wall is paid
        const c = cost[i];
        const nextDp = dp.slice(); // copy current state

        for (let cur = 0; cur <= n; ++cur) {
            if (dp[cur] === INF) continue;
            const nxt = Math.min(n, cur + weight);
            const newCost = dp[cur] + c;
            if (newCost < nextDp[nxt]) {
                nextDp[nxt] = newCost;
            }
        }

        dp = nextDp;
    }

    return dp[n];
};
```

## Typescript

```typescript
function paintWalls(cost: number[], time: number[]): number {
    const n = cost.length;
    const INF = 1e18;
    let prev = new Array(n + 1).fill(INF);
    prev[0] = 0;

    for (let i = n - 1; i >= 0; i--) {
        const cur = new Array(n + 1).fill(0);
        cur[0] = 0;
        for (let remain = 1; remain <= n; remain++) {
            const paint = cost[i] + prev[Math.max(0, remain - 1 - time[i])];
            const dontPaint = prev[remain];
            cur[remain] = Math.min(paint, dontPaint);
        }
        prev = cur;
    }

    return prev[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @param Integer[] $time
     * @return Integer
     */
    function paintWalls($cost, $time) {
        $n = count($cost);
        $INF = 10**15; // sufficiently large
        
        // prevDp represents dp[i+1][*]
        $prev = array_fill(0, $n + 1, $INF);
        $prev[0] = 0;
        
        for ($i = $n - 1; $i >= 0; --$i) {
            $curr = array_fill(0, $n + 1, $INF);
            $curr[0] = 0; // no walls left to paint costs nothing
            for ($remain = 1; $remain <= $n; ++$remain) {
                $paintRemain = $remain - 1 - $time[$i];
                if ($paintRemain < 0) {
                    $paintRemain = 0;
                }
                $paintCost = $cost[$i] + $prev[$paintRemain];
                $dontCost = $prev[$remain];
                $curr[$remain] = min($paintCost, $dontCost);
            }
            $prev = $curr;
        }
        
        return $prev[$n];
    }
}
```

## Swift

```swift
class Solution {
    func paintWalls(_ cost: [Int], _ time: [Int]) -> Int {
        let n = cost.count
        let INF = Int.max / 4
        var prev = Array(repeating: INF, count: n + 1)
        prev[0] = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            var cur = Array(repeating: INF, count: n + 1)
            cur[0] = 0
            for remain in 1...n {
                let paintRemain = max(0, remain - 1 - time[i])
                let paintCost = cost[i] + prev[paintRemain]
                let dontCost = prev[remain]
                cur[remain] = min(paintCost, dontCost)
            }
            prev = cur
        }
        return prev[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun paintWalls(cost: IntArray, time: IntArray): Int {
        val n = cost.size
        val INF = Long.MAX_VALUE / 4
        var prev = LongArray(n + 1) { INF }
        prev[0] = 0L
        var cur = LongArray(n + 1)

        for (i in n - 1 downTo 0) {
            cur[0] = 0L
            for (remain in 1..n) {
                val dontPaint = prev[remain]
                val idx = if (remain - time[i] - 1 < 0) 0 else remain - time[i] - 1
                val paintCost = cost[i].toLong() + prev[idx]
                cur[remain] = kotlin.math.min(dontPaint, paintCost)
            }
            // swap arrays for next iteration
            val temp = prev
            prev = cur
            cur = temp
        }
        return prev[n].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int paintWalls(List<int> cost, List<int> time) {
    const int INF = 1 << 60;
    int n = cost.length;
    List<int> prev = List.filled(n + 1, INF);
    prev[0] = 0;

    for (int i = n - 1; i >= 0; --i) {
      List<int> cur = List.filled(n + 1, INF);
      cur[0] = 0;
      for (int remain = 1; remain <= n; ++remain) {
        int idx = remain - 1 - time[i];
        if (idx < 0) idx = 0;
        int paintCost = cost[i] + prev[idx];
        int dontCost = prev[remain];
        cur[remain] = paintCost < dontCost ? paintCost : dontCost;
      }
      prev = cur;
    }

    return prev[n];
  }
}
```

## Golang

```go
func paintWalls(cost []int, time []int) int {
    n := len(cost)
    const INF = int(1 << 60)

    prev := make([]int, n+1)
    for i := 1; i <= n; i++ {
        prev[i] = INF
    }
    dp := make([]int, n+1)

    for i := n - 1; i >= 0; i-- {
        dp[0] = 0
        for remain := 1; remain <= n; remain++ {
            idx := remain - 1 - time[i]
            if idx < 0 {
                idx = 0
            }
            paint := cost[i] + prev[idx]
            dont := prev[remain]
            if paint < dont {
                dp[remain] = paint
            } else {
                dp[remain] = dont
            }
        }
        copy(prev, dp)
    }

    return prev[n]
}
```

## Ruby

```ruby
INF = (1 << 60)

def paint_walls(cost, time)
  n = cost.length
  prev = Array.new(n + 1, INF)
  prev[0] = 0

  i = n - 1
  while i >= 0
    cur = Array.new(n + 1, INF)
    cur[0] = 0
    r = 1
    while r <= n
      paint = cost[i] + prev[[0, r - 1 - time[i]].max]
      dont = prev[r]
      cur[r] = paint < dont ? paint : dont
      r += 1
    end
    prev = cur
    i -= 1
  end

  prev[n]
end
```

## Scala

```scala
object Solution {
    def paintWalls(cost: Array[Int], time: Array[Int]): Int = {
        val n = cost.length
        val INF = Int.MaxValue / 2

        var prev = new Array[Int](n + 1)
        java.util.Arrays.fill(prev, INF)
        prev(0) = 0

        for (i <- (n - 1) to 0 by -1) {
            val dp = new Array[Int](n + 1)
            dp(0) = 0
            for (remain <- 1 to n) {
                val dont = prev(remain)

                var idx = remain - 1 - time(i)
                if (idx < 0) idx = 0

                val paintLong = cost(i).toLong + prev(idx).toLong
                val paint = if (paintLong > INF) INF else paintLong.toInt

                dp(remain) = Math.min(dont, paint)
            }
            prev = dp
        }

        prev(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn paint_walls(cost: Vec<i32>, time: Vec<i32>) -> i32 {
        let n = cost.len();
        const INF: i64 = i64::MAX / 4;
        // prev[remain] = min cost to cover 'remain' walls using indices >= current i
        let mut prev = vec![INF; n + 1];
        prev[0] = 0;
        for i in (0..n).rev() {
            let mut cur = vec![INF; n + 1];
            cur[0] = 0;
            for remain in 1..=n {
                // option: do not use paid painter at i
                let dont = prev[remain];
                // option: use paid painter at i, covering 1 + time[i] walls
                let covered = if remain > (time[i] as usize + 1) {
                    remain - (time[i] as usize + 1)
                } else {
                    0
                };
                let paint = cost[i] as i64 + prev[covered];
                cur[remain] = dont.min(paint);
            }
            prev = cur;
        }
        prev[n] as i32
    }
}
```

## Racket

```racket
(define/contract (paint-walls cost time)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length cost))
         (costv (list->vector cost))
         (timev (list->vector time))
         (INF (expt 2 60))
         (init-prev (make-vector (+ n 1) INF)))
    (vector-set! init-prev 0 0)
    (let loop ((i (- n 1)) (prevDp init-prev))
      (if (< i 0)
          (vector-ref prevDp n)
          (let* ((c (vector-ref costv i))
                 (t (vector-ref timev i))
                 (dp (make-vector (+ n 1) INF)))
            (for ([remain (in-range 1 (+ n 1))])
              (let* ((weight (+ 1 t))
                     (new-remain (max 0 (- remain weight)))
                     (paint-cost (+ c (vector-ref prevDp new-remain)))
                     (skip-cost (vector-ref prevDp remain))
                     (best (if (< paint-cost skip-cost) paint-cost skip-cost)))
                (vector-set! dp remain best)))
            (loop (- i 1) dp))))))
```

## Erlang

```erlang
-module(solution).
-export([paint_walls/2]).

-spec paint_walls(Cost :: [integer()], Time :: [integer()]) -> integer().
paint_walls(Cost, Time) ->
    N = length(Cost),
    INF = 1 bsl 60,
    Prev0 = [0 | lists:duplicate(N, INF)],
    FinalPrev = iter(N - 1, Cost, Time, Prev0, INF, N),
    lists:nth(N + 1, FinalPrev).

%% iterate over walls from index I down to 0
-spec iter(integer(), [integer()], [integer()], [integer()], integer(), integer()) -> [integer()].
iter(-1, _Cost, _Time, Prev, _INF, _N) ->
    Prev;
iter(I, Cost, Time, Prev, INF, N) ->
    CostI = nth0(I, Cost),
    TimeI = nth0(I, Time),
    NewPrev = build_dp(CostI, TimeI, Prev, INF, N),
    iter(I - 1, Cost, Time, NewPrev, INF, N).

%% build dp list for current wall
-spec build_dp(integer(), integer(), [integer()], integer(), integer()) -> [integer()].
build_dp(CostI, TimeI, Prev, _INF, N) ->
    Weight = 1 + TimeI,
    [ case Rem of
          0 -> 0;
          _ ->
              NeedIdx = erlang:max(0, Rem - Weight),
              PaintCost = CostI + nth0(NeedIdx, Prev),
              DontPaint = nth0(Rem, Prev),
              erlang:min(PaintCost, DontPaint)
      end || Rem <- lists:seq(0, N) ].

%% zero‑based list indexing
-spec nth0(integer(), [any()]) -> any().
nth0(Index, List) ->
    lists:nth(Index + 1, List).
```

## Elixir

```elixir
defmodule Solution do
  @spec paint_walls(cost :: [integer], time :: [integer]) :: integer
  def paint_walls(cost, time) do
    n = length(cost)
    inf = 1_000_000_000_000

    # dp for i = n (no walls left to consider)
    prev =
      0..n
      |> Enum.map(fn i -> if i == 0, do: 0, else: inf end)
      |> List.to_tuple()

    {final_dp, _} =
      Enum.reduce(Enum.reverse(0..(n - 1)), {prev, nil}, fn idx, {prev_dp, _} ->
        c = Enum.at(cost, idx)
        t = Enum.at(time, idx)

        cur =
          0..n
          |> Enum.map(fn remain ->
            if remain == 0 do
              0
            else
              paint = c + elem(prev_dp, max(0, remain - 1 - t))
              dont = elem(prev_dp, remain)
              if paint < dont, do: paint, else: dont
            end
          end)
          |> List.to_tuple()

        {cur, nil}
      end)

    elem(final_dp, n)
  end
end
```

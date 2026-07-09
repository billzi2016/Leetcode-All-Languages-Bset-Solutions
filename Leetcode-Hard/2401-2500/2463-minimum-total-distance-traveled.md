# 2463. Minimum Total Distance Traveled

## Cpp

```cpp
class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end(),
             [](const vector<int>& a, const vector<int>& b){ return a[0] < b[0]; });
        int n = robot.size();
        int m = factory.size();
        const long long INF = (long long)4e18;
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, INF));
        for (int j = 0; j <= m; ++j) dp[0][j] = 0; // zero robots cost zero
        
        for (int j = 1; j <= m; ++j) {
            int pos = factory[j - 1][0];
            int limit = factory[j - 1][1];
            // not using this factory
            for (int i = 0; i <= n; ++i) dp[i][j] = dp[i][j - 1];
            // try assigning k robots to this factory
            for (int i = 1; i <= n; ++i) {
                long long cur = 0;
                for (int k = 1; k <= limit && k <= i; ++k) {
                    int idx = i - k; // robot index (0‑based)
                    cur += llabs((long long)robot[idx] - pos);
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + cur);
                }
            }
        }
        return dp[n][m];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        // Sort robots
        int n = robot.size();
        int[] robots = new int[n];
        for (int i = 0; i < n; i++) robots[i] = robot.get(i);
        Arrays.sort(robots);

        // Sort factories by position
        Arrays.sort(factory, Comparator.comparingInt(a -> a[0]));

        // Expand factories according to their limits
        List<Integer> slotsList = new ArrayList<>();
        for (int[] f : factory) {
            int pos = f[0];
            int limit = f[1];
            for (int k = 0; k < limit; k++) {
                slotsList.add(pos);
            }
        }

        int m = slotsList.size();
        long INF = Long.MAX_VALUE / 4;

        // DP: prev[j] = min total distance to assign first i-1 robots using first j slots
        long[] prev = new long[m + 1];
        Arrays.fill(prev, 0L); // zero robots cost zero

        for (int i = 1; i <= n; i++) {
            long[] cur = new long[m + 1];
            Arrays.fill(cur, INF);
            // Need at least i slots to assign i robots
            for (int j = i; j <= m; j++) {
                long assignCost = prev[j - 1] + Math.abs((long)robots[i - 1] - (long)slotsList.get(j - 1));
                long skipCost = cur[j - 1];
                cur[j] = Math.min(assignCost, skipCost);
            }
            prev = cur;
        }

        return prev[m];
    }
}
```

## Python

```python
class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort(key=lambda x: x[0])
        n = len(robot)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0

        for fpos, limit in factory:
            # prefix sums of distances to this factory position
            pref = [0] * (n + 1)
            for i in range(1, n + 1):
                pref[i] = pref[i - 1] + abs(robot[i - 1] - fpos)

            newdp = [INF] * (n + 1)
            for j in range(n + 1):
                maxk = min(limit, j)
                best = INF
                # try assigning k robots ending at position j-1 to this factory
                for k in range(maxk + 1):
                    cost = pref[j] - pref[j - k]
                    val = dp[j - k] + cost
                    if val < best:
                        best = val
                newdp[j] = best
            dp = newdp

        return dp[n]
```

## Python3

```python
class Solution:
    def minimumTotalDistance(self, robot, factory):
        from math import inf
        robot.sort()
        factory.sort(key=lambda x: x[0])
        n = len(robot)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for pos, cap in factory:
            ndp = dp[:]  # skipping this factory
            for i in range(n):
                if dp[i] == inf:
                    continue
                cost = 0
                max_k = min(cap, n - i)
                for k in range(1, max_k + 1):
                    cost += abs(robot[i + k - 1] - pos)
                    if ndp[i + k] > dp[i] + cost:
                        ndp[i + k] = dp[i] + cost
            dp = ndp
        return dp[n]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

struct Factory {
    int pos;
    int limit;
};

static int cmp_factory(const void *a, const void *b) {
    const struct Factory *fa = (const struct Factory *)a;
    const struct Factory *fb = (const struct Factory *)b;
    return (fa->pos > fb->pos) - (fa->pos < fb->pos);
}

long long minimumTotalDistance(int* robot, int robotSize, int** factory, int factorySize, int* factoryColSize) {
    if (robotSize == 0) return 0;

    /* sort robots */
    int *robots = (int *)malloc(robotSize * sizeof(int));
    memcpy(robots, robot, robotSize * sizeof(int));
    qsort(robots, robotSize, sizeof(int), cmp_int);

    /* copy and sort factories */
    struct Factory *farr = (struct Factory *)malloc(factorySize * sizeof(struct Factory));
    long totalSlots = 0;
    for (int i = 0; i < factorySize; ++i) {
        farr[i].pos = factory[i][0];
        farr[i].limit = factory[i][1];
        totalSlots += farr[i].limit;
    }
    qsort(farr, factorySize, sizeof(struct Factory), cmp_factory);

    /* build slots array (factory positions repeated by limit) */
    int *slots = (int *)malloc(totalSlots * sizeof(int));
    long idx = 0;
    for (int i = 0; i < factorySize; ++i) {
        for (int k = 0; k < farr[i].limit; ++k) {
            slots[idx++] = farr[i].pos;
        }
    }

    /* DP: dp[j] = min cost to assign processed robots using first j slots */
    const long long INF = (1LL << 60);
    long long *dp = (long long *)malloc((totalSlots + 1) * sizeof(long long));
    long long *ndp = (long long *)malloc((totalSlots + 1) * sizeof(long long));

    for (long j = 0; j <= totalSlots; ++j) dp[j] = INF;
    dp[0] = 0;

    for (int i = 1; i <= robotSize; ++i) {
        ndp[0] = INF;
        for (long j = 1; j <= totalSlots; ++j) {
            long long assign = dp[j - 1] + llabs((long long)robots[i - 1] - (long long)slots[j - 1]);
            long long skip = ndp[j - 1];
            ndp[j] = (assign < skip) ? assign : skip;
        }
        long long *tmp = dp; dp = ndp; ndp = tmp;
    }

    long long answer = dp[totalSlots];

    free(robots);
    free(farr);
    free(slots);
    free(dp);
    free(ndp);
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public long MinimumTotalDistance(IList<int> robot, int[][] factory)
    {
        int n = robot.Count;
        int[] robots = new int[n];
        for (int i = 0; i < n; i++) robots[i] = robot[i];
        Array.Sort(robots);
        Array.Sort(factory, (a, b) => a[0].CompareTo(b[0]));

        const long INF = (long)4e18;
        long[] dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;

        foreach (var f in factory)
        {
            int pos = f[0];
            int cap = f[1];
            long[] ndp = new long[n + 1];
            Array.Copy(dp, ndp, n + 1);

            for (int i = 0; i <= n; i++)
            {
                if (dp[i] == INF) continue;
                long sum = 0;
                for (int t = 1; t <= cap && i + t <= n; ++t)
                {
                    sum += Math.Abs((long)robots[i + t - 1] - pos);
                    long cand = dp[i] + sum;
                    if (cand < ndp[i + t]) ndp[i + t] = cand;
                }
            }

            dp = ndp;
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} robot
 * @param {number[][]} factory
 * @return {number}
 */
var minimumTotalDistance = function(robot, factory) {
    const n = robot.length;
    // sort robots and factories by position
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);

    const INF = 1e18;
    let dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (const [pos, limit] of factory) {
        const ndp = new Array(n + 1).fill(INF);
        for (let i = 0; i <= n; ++i) {
            if (dp[i] === INF) continue;
            // assign zero robots to this factory
            if (ndp[i] > dp[i]) ndp[i] = dp[i];
            let sum = 0;
            for (let k = 1; k <= limit && i + k <= n; ++k) {
                sum += Math.abs(robot[i + k - 1] - pos);
                const nxt = i + k;
                const val = dp[i] + sum;
                if (ndp[nxt] > val) ndp[nxt] = val;
            }
        }
        dp = ndp;
    }

    return dp[n];
};
```

## Typescript

```typescript
function minimumTotalDistance(robot: number[], factory: number[][]): number {
    const n = robot.length;
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);

    const slots: number[] = [];
    for (const [pos, limit] of factory) {
        for (let i = 0; i < limit; ++i) {
            slots.push(pos);
        }
    }

    const m = slots.length;
    const INF = 1e18;

    const dp: number[][] = Array.from({ length: n + 1 }, () => Array(m + 1).fill(INF));
    for (let j = 0; j <= m; ++j) dp[0][j] = 0;

    for (let i = 1; i <= n; ++i) {
        // need at least i slots to assign i robots
        for (let j = i; j <= m; ++j) {
            const assign = dp[i - 1][j - 1] + Math.abs(robot[i - 1] - slots[j - 1]);
            const skip = dp[i][j - 1];
            dp[i][j] = assign < skip ? assign : skip;
        }
    }

    return dp[n][m];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $robot
     * @param Integer[][] $factory
     * @return Integer
     */
    function minimumTotalDistance($robot, $factory) {
        sort($robot);
        usort($factory, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $n = count($robot);
        $INF = 1 << 60; // sufficiently large

        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;

        foreach ($factory as $f) {
            [$pos, $cap] = $f;
            $newDp = $dp; // case of assigning 0 robots to this factory
            for ($i = 0; $i <= $n; $i++) {
                if ($dp[$i] === $INF) continue;
                $cost = 0;
                // try assigning t robots (t >=1) from current index i
                for ($t = 1; $t <= $cap && $i + $t <= $n; $t++) {
                    $cost += abs($robot[$i + $t - 1] - $pos);
                    $newIdx = $i + $t;
                    $candidate = $dp[$i] + $cost;
                    if ($candidate < $newDp[$newIdx]) {
                        $newDp[$newIdx] = $candidate;
                    }
                }
            }
            $dp = $newDp;
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func minimumTotalDistance(_ robot: [Int], _ factory: [[Int]]) -> Int {
        let robots = robot.sorted()
        var factories: [(pos: Int, limit: Int)] = []
        for f in factory {
            factories.append((pos: f[0], limit: f[1]))
        }
        factories.sort { $0.pos < $1.pos }
        
        var slots: [Int] = []
        for f in factories {
            if f.limit > 0 {
                slots.append(contentsOf: Array(repeating: f.pos, count: f.limit))
            }
        }
        
        let n = robots.count
        let s = slots.count
        // dpPrev[j]: min cost to assign first i-1 robots using first j slots
        var dpPrev = Array(repeating: Int64(0), count: s + 1)
        
        for i in 1...n {
            var cur = Array(repeating: Int64.max / 4, count: s + 1)
            // cur[0] stays INF because we cannot assign i robots with 0 slots
            for j in 1...s {
                let assignCost = dpPrev[j - 1] + Int64(abs(robots[i - 1] - slots[j - 1]))
                let skipCost = cur[j - 1]
                cur[j] = min(assignCost, skipCost)
            }
            dpPrev = cur
        }
        
        return Int(dpPrev[s])
    }
}
```

## Kotlin

```kotlin
import kotlin.math.abs

class Solution {
    private val INF = Long.MAX_VALUE / 4

    fun minimumTotalDistance(robot: List<Int>, factory: Array<IntArray>): Long {
        val robotsSorted = robot.sorted()
        val n = robotsSorted.size
        val rob = LongArray(n) { robotsSorted[it].toLong() }

        // sort factories by position
        val factories = factory.map { Pair(it[0], it[1]) }.sortedBy { it.first }

        var dp = LongArray(n + 1) { INF }
        dp[0] = 0L

        for ((posInt, limit) in factories) {
            val pos = posInt.toLong()
            // prefix sums of distances to this factory
            val pref = LongArray(n + 1)
            for (i in 1..n) {
                pref[i] = pref[i - 1] + abs(rob[i - 1] - pos)
            }

            val newDp = LongArray(n + 1) { INF }
            for (i in 0..n) {
                val maxT = if (limit < i) limit else i
                var t = 0
                while (t <= maxT) {
                    val prev = dp[i - t]
                    if (prev != INF) {
                        val cost = pref[i] - pref[i - t]
                        val cand = prev + cost
                        if (cand < newDp[i]) newDp[i] = cand
                    }
                    t++
                }
            }
            dp = newDp
        }

        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int minimumTotalDistance(List<int> robot, List<List<int>> factory) {
    robot.sort();
    factory.sort((a, b) => a[0].compareTo(b[0]));

    List<int> slots = [];
    for (var f in factory) {
      int pos = f[0];
      int limit = f[1];
      for (int i = 0; i < limit; i++) {
        slots.add(pos);
      }
    }

    int n = robot.length;
    int m = slots.length;
    const int INF = 1 << 60;

    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(m + 1, INF));
    for (int j = 0; j <= m; j++) {
      dp[0][j] = 0;
    }

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        int assign = dp[i - 1][j - 1];
        if (assign != INF) {
          assign += (robot[i - 1] - slots[j - 1]).abs();
        }
        int skip = dp[i][j - 1];
        dp[i][j] = assign < skip ? assign : skip;
      }
    }

    return dp[n][m];
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func minimumTotalDistance(robot []int, factory [][]int) int64 {
	const INF int64 = 1 << 60

	n := len(robot)
	if n == 0 {
		return 0
	}
	sort.Ints(robot)

	type Fact struct {
		pos   int
		limit int
	}
	facts := make([]Fact, len(factory))
	for i, f := range factory {
		facts[i] = Fact{pos: f[0], limit: f[1]}
	}
	sort.Slice(facts, func(i, j int) bool { return facts[i].pos < facts[j].pos })

	dpPrev := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		dpPrev[i] = INF
	}
	dpPrev[0] = 0

	for _, f := range facts {
		dpCurr := make([]int64, n+1)
		for i := 0; i <= n; i++ {
			dpCurr[i] = INF
		}
		for i := 0; i <= n; i++ {
			if dpPrev[i] == INF {
				continue
			}
			// assign zero robots to this factory
			if dpPrev[i] < dpCurr[i] {
				dpCurr[i] = dpPrev[i]
			}
			curCost := int64(0)
			maxK := f.limit
			if maxK > n-i {
				maxK = n - i
			}
			for k := 1; k <= maxK; k++ {
				rPos := robot[i+k-1]
				diff := rPos - f.pos
				if diff < 0 {
					diff = -diff
				}
				curCost += int64(diff)
				val := dpPrev[i] + curCost
				if val < dpCurr[i+k] {
					dpCurr[i+k] = val
				}
			}
		}
		dpPrev = dpCurr
	}

	return dpPrev[n]
}
```

## Ruby

```ruby
def minimum_total_distance(robot, factory)
  # Sort robots
  robot.sort!
  # Sort factories by position and expand according to their limits
  factory.sort_by! { |f| f[0] }
  positions = []
  factory.each do |pos, limit|
    limit.times { positions << pos }
  end

  n = robot.size
  m = positions.size
  inf = (1 << 60)

  # dp_prev[j]: minimum cost to assign processed robots using first j factories
  dp_prev = Array.new(m + 1, inf)
  dp_prev[0] = 0

  robot.each do |r|
    dp_cur = Array.new(m + 1, inf)
    (1..m).each do |j|
      assign = dp_prev[j - 1] + (r - positions[j - 1]).abs
      skip   = dp_cur[j - 1]
      dp_cur[j] = assign < skip ? assign : skip
    end
    dp_prev = dp_cur
  end

  dp_prev[m]
end
```

## Scala

```scala
object Solution {
  def minimumTotalDistance(robot: List[Int], factory: Array[Array[Int]]): Long = {
    val robotsSorted = robot.sorted
    val factoriesSorted = factory.sortBy(_(0))

    // Expand factories according to their limits
    val positionsBuffer = scala.collection.mutable.ArrayBuffer[Int]()
    for (f <- factoriesSorted) {
      val pos = f(0)
      val limit = f(1)
      var cnt = 0
      while (cnt < limit) {
        positionsBuffer += pos
        cnt += 1
      }
    }
    val factoryPos = positionsBuffer.toArray

    val n = robotsSorted.length
    val m = factoryPos.length
    val INF: Long = Long.MaxValue / 4

    var prev = Array.fill[Long](m + 1)(0L) // dp for 0 robots
    var cur = new Array[Long](m + 1)

    var i = 1
    while (i <= n) {
      cur(0) = INF
      var j = 1
      while (j <= m) {
        val assignPrev = prev(j - 1)
        val assign = if (assignPrev >= INF) INF else assignPrev + math.abs(robotsSorted(i - 1) - factoryPos(j - 1)).toLong
        val skip = cur(j - 1)
        cur(j) = if (assign < skip) assign else skip
        j += 1
      }
      // swap prev and cur for next iteration
      val temp = prev
      prev = cur
      cur = temp
      i += 1
    }

    prev(m)
  }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn minimum_total_distance(robot: Vec<i32>, factory: Vec<Vec<i32>>) -> i64 {
        let mut robots = robot;
        robots.sort_unstable();
        let n = robots.len();

        // sort factories by position and expand according to their limits
        let mut facs: Vec<(i32, i32)> = factory.into_iter().map(|v| (v[0], v[1])).collect();
        facs.sort_by_key(|&(pos, _)| pos);
        let mut slots: Vec<i32> = Vec::new();
        for (pos, limit) in facs {
            for _ in 0..limit {
                slots.push(pos);
            }
        }

        let m = slots.len();
        const INF: i64 = i64::MAX / 4;

        // dp[i][j]: min distance to assign first i robots using first j slots
        let mut dp = vec![vec![INF; m + 1]; n + 1];
        for j in 0..=m {
            dp[0][j] = 0;
        }

        for i in 1..=n {
            for j in 1..=m {
                // option 1: assign robot i-1 to slot j-1
                let mut assign = INF;
                if dp[i - 1][j - 1] != INF {
                    let dist = (robots[i - 1] as i64 - slots[j - 1] as i64).abs();
                    assign = dp[i - 1][j - 1] + dist;
                }
                // option 2: skip slot j-1
                let skip = dp[i][j - 1];
                dp[i][j] = min(assign, skip);
            }
        }

        dp[n][m]
    }
}
```

## Racket

```racket
(define/contract (minimum-total-distance robot factory)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((robots (sort robot <))
         (sorted-factory (sort factory (lambda (a b) (< (car a) (car b)))))
    ;; flatten factories according to their limits, preserving order
    (define flat
      (let loop ((lst sorted-factory) (acc '()))
        (if (null? lst)
            (reverse acc)
            (let* ((pair (car lst))
                   (pos (car pair))
                   (lim (cadr pair)))
              (loop (cdr lst) (append (make-list lim pos) acc))))))
    (define n (length robots))
    (define m (length flat))
    (define R (list->vector robots))
    (define F (list->vector flat))
    (define INF 1000000000000000)
    ;; dp is a vector of vectors, size (n+1) x (m+1)
    (define dp (make-vector (+ n 1)))
    (for ([i (in-range (+ n 1))])
      (vector-set! dp i (make-vector (+ m 1) INF)))
    ;; base case: when all robots are assigned, distance is 0
    (let ((last-row (vector-ref dp n)))
      (for ([j (in-range (+ m 1))])
        (vector-set! last-row j 0)))
    ;; fill DP bottom‑up
    (for ([i (in-range (- n 1) -1 -1)])
      (let* ((row (vector-ref dp i))
             (next-row (vector-ref dp (+ i 1))))
        (vector-set! row m INF)
        (for ([j (in-range (- m 1) -1 -1)])
          (let* ((assign (+ (abs (- (vector-ref R i) (vector-ref F j)))
                           (vector-ref next-row (+ j 1))))
                 (skip (vector-ref row (+ j 1)))
                 (best (if (< assign skip) assign skip)))
            (vector-set! row j best)))))
    (vector-ref (vector-ref dp 0) 0)))
```

## Erlang

```erlang
-spec minimum_total_distance(Robot :: [integer()], Factory :: [[integer()]]) -> integer().
minimum_total_distance(Robot, Factory) ->
    RobotsSorted = lists:sort(Robot),
    FactTuples = [{Pos, Lim} || [Pos, Lim] <- Factory],
    FactSorted = lists:keysort(1, FactTuples),
    Slots = build_slots(FactSorted),
    Len = length(Slots),
    Dp0 = [0 | lists:duplicate(Len, ?INF)],
    FinalDp = lists:foldl(fun(R, DpPrev) -> process_robot(R, Slots, DpPrev) end,
                          Dp0, RobotsSorted),
    lists:last(FinalDp).

-define(INF, 1 bsl 60).

build_slots(FactSorted) ->
    lists:foldl(fun({Pos, Lim}, Acc) ->
        Acc ++ lists:duplicate(Lim, Pos)
    end, [], FactSorted).

process_robot(R, Slots, DpPrev) ->
    {NewRev, _} = proc(R, Slots, DpPrev, [?INF], ?INF),
    lists:reverse(NewRev).

proc(_R, [], [_|RestDpPrev], Acc, _PrevNew) ->
    {Acc, RestDpPrev};
proc(R, [Slot|RestSlots], [DPPrevHead|RestDpPrev], Acc, PrevNew) ->
    Assign = DPPrevHead + abs(R - Slot),
    NewVal = if Assign < PrevNew -> Assign; true -> PrevNew end,
    proc(R, RestSlots, RestDpPrev, [NewVal | Acc], NewVal).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_total_distance(robot :: [integer], factory :: [[integer]]) :: integer
  def minimum_total_distance(robot, factory) do
    robots = Enum.sort(robot)

    factories_sorted =
      Enum.sort_by(factory, fn [pos, _] -> pos end)

    fpos_list =
      factories_sorted
      |> Enum.flat_map(fn [pos, limit] ->
        List.duplicate(pos, limit)
      end)

    m = length(fpos_list)
    fpos_tuple = List.to_tuple(fpos_list)

    inf = 1 <<< 60

    # dp tuple for the case with no robots left: cost 0 for any remaining factories
    dp_initial = :erlang.make_tuple(m + 1, 0)

    final_dp =
      Enum.reduce(Enum.reverse(robots), dp_initial, fn r, dp_acc ->
        cur_list =
          Enum.reduce(Enum.reverse(0..(m - 1)), [], fn j, acc ->
            assign = abs(r - elem(fpos_tuple, j)) + elem(dp_acc, j + 1)

            skip =
              case acc do
                [] -> inf
                [next_cur | _] -> next_cur
              end

            cur_j = if assign < skip, do: assign, else: skip
            [cur_j | acc]
          end)

        List.to_tuple(cur_list ++ [inf])
      end)

    elem(final_dp, 0)
  end
end
```

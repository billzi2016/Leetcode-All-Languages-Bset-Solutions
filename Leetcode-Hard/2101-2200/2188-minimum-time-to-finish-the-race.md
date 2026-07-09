# 2188. Minimum Time to Finish the Race

## Cpp

```cpp
class Solution {
public:
    int minimumFinishTime(vector<vector<int>>& tires, int changeTime, int numLaps) {
        const long long INF = 4e18;
        vector<long long> best(numLaps + 1, INF);
        for (auto &t : tires) {
            long long f = t[0], r = t[1];
            long long cur = f;
            long long sum = cur;
            int cnt = 1;
            while (cnt <= numLaps && sum <= changeTime + f) {
                if (sum < best[cnt]) best[cnt] = sum;
                // prepare next lap
                if (cur > INF / r) break; // avoid overflow
                cur *= r;
                sum += cur;
                ++cnt;
            }
        }
        vector<long long> dp(numLaps + 1, INF);
        dp[0] = 0;
        for (int i = 1; i <= numLaps; ++i) {
            for (int k = 1; k <= i; ++k) {
                if (best[k] == INF) continue;
                long long cost = best[k];
                if (k < i) cost += changeTime; // need to change before next segment
                dp[i] = min(dp[i], dp[i - k] + cost);
            }
        }
        return (int)dp[numLaps];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumFinishTime(int[][] tires, int changeTime, int numLaps) {
        int maxK = Math.min(numLaps, 30); // sufficient bound
        int[] best = new int[maxK + 1];
        Arrays.fill(best, Integer.MAX_VALUE);
        for (int[] tire : tires) {
            long f = tire[0];
            long r = tire[1];
            long lapTime = f;
            long total = 0;
            for (int k = 1; k <= maxK && lapTime <= changeTime + f; ++k) {
                total += lapTime;
                if (total < best[k]) best[k] = (int) total;
                lapTime *= r;
            }
        }

        int[] dp = new int[numLaps + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 1; i <= numLaps; ++i) {
            for (int k = 1; k <= Math.min(i, maxK); ++k) {
                if (best[k] == Integer.MAX_VALUE) continue;
                int prev = dp[i - k];
                if (prev == Integer.MAX_VALUE) continue;
                int cand = prev + best[k];
                if (i != k) cand += changeTime; // need a change before this segment
                dp[i] = Math.min(dp[i], cand);
            }
        }

        return dp[numLaps];
    }
}
```

## Python

```python
class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        INF = 10**18
        # best[k] = minimal time to run k consecutive laps without changing tire
        best = [INF] * (numLaps + 1)
        for f, r in tires:
            cur = f
            total = 0
            for k in range(1, numLaps + 1):
                total += cur
                if total > changeTime + f:   # no point to continue further with this tire
                    break
                if total < best[k]:
                    best[k] = total
                cur *= r

        dp = [INF] * (numLaps + 1)
        dp[0] = 0
        for i in range(1, numLaps + 1):
            # finish all i laps with a single stint (no prior change)
            if best[i] < INF:
                dp[i] = best[i]
            # try splitting: previous part ends at i-k laps, then change and run k laps
            for k in range(1, i):
                if best[k] == INF:
                    continue
                cand = dp[i - k] + changeTime + best[k]
                if cand < dp[i]:
                    dp[i] = cand
        return dp[numLaps]
```

## Python3

```python
from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        INF = 10**18
        best = [INF] * (numLaps + 1)

        # Precompute minimal time to run k consecutive laps with the same tire
        for f, r in tires:
            lap_time = f
            total = lap_time
            k = 1
            if total < best[k]:
                best[k] = total
            while k < numLaps:
                lap_time *= r
                # If continuing is slower than changing and taking a fresh first lap, stop
                if lap_time > changeTime + f:
                    break
                total += lap_time
                k += 1
                if total < best[k]:
                    best[k] = total

        dp = [INF] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            # Finish the race with a single segment of length i (no prior change time)
            if best[i] != INF:
                dp[i] = best[i]
            # Try splitting into previous laps plus a new segment
            for k in range(1, i):
                if best[k] == INF:
                    continue
                cand = dp[i - k] + changeTime + best[k]
                if cand < dp[i]:
                    dp[i] = cand

        return dp[numLaps]
```

## C

```c
#include <stddef.h>
#include <limits.h>

int minimumFinishTime(int** tires, int tiresSize, int* tiresColSize, int changeTime, int numLaps) {
    const long long INF = (1LL<<60);
    long long best[1001];
    for (int i = 0; i <= numLaps; ++i) best[i] = INF;

    for (int i = 0; i < tiresSize; ++i) {
        int f = tires[i][0];
        int r = tires[i][1];
        long long cur = f;
        long long sum = cur;
        int k = 1;
        while (k <= numLaps && sum < INF) {
            if (sum < best[k]) best[k] = sum;
            // decide whether continuing is ever beneficial
            if (cur > (long long)changeTime + f) break; // next lap would be worse than change+first
            if ((double)cur * r > 1e18) break; // avoid overflow
            cur *= r;
            if (cur > INF) break;
            sum += cur;
            ++k;
        }
    }

    long long dp[1001];
    for (int i = 0; i <= numLaps; ++i) dp[i] = INF;
    dp[0] = 0;

    for (int i = 1; i <= numLaps; ++i) {
        for (int k = 1; k <= i; ++k) {
            if (best[k] == INF) continue;
            long long cand = dp[i - k] + best[k];
            if (i - k > 0) cand += changeTime;
            if (cand < dp[i]) dp[i] = cand;
        }
    }

    return (int)dp[numLaps];
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumFinishTime(int[][] tires, int changeTime, int numLaps) {
        const long INF = long.MaxValue / 4;
        int max = numLaps;
        long[] best = new long[max + 1];
        for (int i = 0; i <= max; i++) best[i] = INF;
        best[0] = 0;

        foreach (var t in tires) {
            long f = t[0];
            long r = t[1];
            long curLapTime = f;
            long total = 0;
            for (int laps = 1; laps <= max && curLapTime <= changeTime + f; laps++) {
                total += curLapTime;
                if (total < best[laps]) best[laps] = total;
                // prepare next lap time, watch overflow
                if (curLapTime > INF / r) break;
                curLapTime *= r;
            }
        }

        long[] dp = new long[max + 1];
        for (int i = 0; i <= max; i++) dp[i] = INF;
        dp[0] = 0;

        for (int l = 1; l <= max; l++) {
            for (int k = 1; k <= l; k++) {
                if (best[k] == INF) continue;
                long cost = best[k];
                if (k < l) cost += changeTime; // need to change before next segment
                dp[l] = Math.Min(dp[l], dp[l - k] + cost);
            }
        }

        return (int)dp[max];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} tires
 * @param {number} changeTime
 * @param {number} numLaps
 * @return {number}
 */
var minimumFinishTime = function(tires, changeTime, numLaps) {
    const INF = 1e18;
    const best = new Array(numLaps + 1).fill(INF);
    
    for (const [f, r] of tires) {
        let cur = f;          // time for the current lap with this tire
        let sum = 0;          // cumulative time for consecutive laps without change
        for (let k = 1; k <= numLaps; ++k) {
            sum += cur;
            if (sum < best[k]) best[k] = sum;
            // decide whether to continue with this tire
            if (cur * r > changeTime + f) break; // next lap would be slower than changing
            cur *= r;
        }
    }
    
    const dp = new Array(numLaps + 1).fill(INF);
    dp[0] = 0;
    for (let i = 1; i <= numLaps; ++i) {
        // finish all i laps with a single segment (no preceding change)
        dp[i] = best[i];
        // split into previous part + a new segment of length k
        for (let k = 1; k < i; ++k) {
            if (best[k] === INF) continue;
            const candidate = dp[i - k] + changeTime + best[k];
            if (candidate < dp[i]) dp[i] = candidate;
        }
    }
    
    return dp[numLaps];
};
```

## Typescript

```typescript
function minimumFinishTime(tires: number[][], changeTime: number, numLaps: number): number {
    const INF = Number.MAX_SAFE_INTEGER;
    const best = new Array(numLaps + 1).fill(INF);
    best[0] = 0;

    for (const [f, r] of tires) {
        let lapTime = f;
        let sum = 0;
        for (let laps = 1; laps <= numLaps && lapTime <= changeTime + f; ++laps) {
            sum += lapTime;
            if (sum < best[laps]) best[laps] = sum;
            if (lapTime > INF / r) break; // avoid overflow
            lapTime *= r;
        }
    }

    const dp = new Array(numLaps + 1).fill(INF);
    dp[0] = 0;
    for (let i = 1; i <= numLaps; ++i) {
        dp[i] = best[i];
        for (let j = 1; j < i; ++j) {
            const cand = dp[i - j] + changeTime + best[j];
            if (cand < dp[i]) dp[i] = cand;
        }
    }

    return dp[numLaps];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $tires
     * @param Integer $changeTime
     * @param Integer $numLaps
     * @return Integer
     */
    function minimumFinishTime($tires, $changeTime, $numLaps) {
        $INF = PHP_INT_MAX;
        // best[k] = minimal time to run k consecutive laps without changing tires
        $best = array_fill(0, $numLaps + 1, $INF);

        foreach ($tires as $t) {
            $f = $t[0];
            $r = $t[1];
            $lapTime = $f;
            $sum = 0;
            for ($lap = 1; $lap <= $numLaps; $lap++) {
                $sum += $lapTime;
                if ($sum < $best[$lap]) {
                    $best[$lap] = $sum;
                }
                // prepare next lap time
                $nextLapTime = $lapTime * $r;
                // If continuing would be slower than changing now, stop.
                if ($nextLapTime > $changeTime + $f) {
                    break;
                }
                $lapTime = $nextLapTime;
            }
        }

        // dp[i] = minimal time to finish i laps
        $dp = array_fill(0, $numLaps + 1, $INF);
        $dp[0] = 0;

        for ($i = 1; $i <= $numLaps; $i++) {
            // Finish all i laps without any prior change
            $dp[$i] = $best[$i];
            // Try splitting the last segment of k laps (k < i)
            for ($k = 1; $k < $i; $k++) {
                if ($best[$k] == $INF) continue;
                $candidate = $dp[$i - $k] + $changeTime + $best[$k];
                if ($candidate < $dp[$i]) {
                    $dp[$i] = $candidate;
                }
            }
        }

        return $dp[$numLaps];
    }
}
```

## Swift

```swift
class Solution {
    func minimumFinishTime(_ tires: [[Int]], _ changeTime: Int, _ numLaps: Int) -> Int {
        let maxLaps = numLaps
        var best = Array(repeating: Int64.max, count: maxLaps + 1)
        let ct = Int64(changeTime)

        for tire in tires {
            let f = Int64(tire[0])
            let r = Int64(tire[1])
            var lapTime = f
            var total = f
            var laps = 1
            if total < best[laps] { best[laps] = total }

            while laps < maxLaps {
                // If the next lap would be slower than changing tires, stop.
                if lapTime > ct + f { break }
                if lapTime > Int64.max / r { break }   // avoid overflow
                let nextLap = lapTime * r
                if nextLap > ct + f { break }
                lapTime = nextLap
                total += lapTime
                laps += 1
                if total < best[laps] { best[laps] = total }
            }
        }

        var dp = Array(repeating: Int64.max, count: maxLaps + 1)
        dp[0] = 0

        for i in 1...maxLaps {
            // Finish all i laps with a single tire segment (no change before start)
            if best[i] != Int64.max {
                dp[i] = min(dp[i], best[i])
            }
            // Split the race: previous part + change + new segment of length k
            var k = 1
            while k < i {
                if best[k] != Int64.max {
                    let candidate = dp[i - k] + ct + best[k]
                    if candidate < dp[i] {
                        dp[i] = candidate
                    }
                }
                k += 1
            }
        }

        return Int(dp[maxLaps])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumFinishTime(tires: Array<IntArray>, changeTime: Int, numLaps: Int): Int {
        val INF = Long.MAX_VALUE / 4
        val best = LongArray(numLaps + 1) { INF }
        for (tire in tires) {
            val f = tire[0].toLong()
            val r = tire[1].toLong()
            var cur = f
            var sum = f
            var cnt = 1
            while (cnt <= numLaps && cur <= changeTime.toLong() + f) {
                if (sum < best[cnt]) best[cnt] = sum
                cur *= r
                sum += cur
                cnt++
            }
        }
        val dp = LongArray(numLaps + 1) { INF }
        dp[0] = 0L
        for (i in 1..numLaps) {
            if (best[i] < INF) dp[i] = best[i]
            var k = 1
            while (k < i) {
                if (best[k] != INF && dp[i - k] != INF) {
                    val cand = dp[i - k] + changeTime + best[k]
                    if (cand < dp[i]) dp[i] = cand
                }
                k++
            }
        }
        return dp[numLaps].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumFinishTime(List<List<int>> tires, int changeTime, int numLaps) {
    const int INF = 1 << 60;
    List<int> best = List.filled(numLaps + 1, INF);

    for (var tire in tires) {
      int f = tire[0];
      int r = tire[1];
      int cur = f;
      int sum = 0;
      int limit = changeTime + f;
      for (int lap = 1; lap <= numLaps && cur <= limit; ++lap) {
        sum += cur;
        if (sum < best[lap]) best[lap] = sum;
        cur *= r;
      }
    }

    List<int> dp = List.filled(numLaps + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= numLaps; ++i) {
      for (int k = 1; k <= i; ++k) {
        if (best[k] == INF) continue;
        int cand = dp[i - k] + best[k];
        if (i != k) cand += changeTime;
        if (cand < dp[i]) dp[i] = cand;
      }
    }

    return dp[numLaps];
  }
}
```

## Golang

```go
func minimumFinishTime(tires [][]int, changeTime int, numLaps int) int {
	const INF = int(1e18)

	// best[k] = minimal time to run k consecutive laps without changing tires
	best := make([]int, numLaps+1)
	for i := 1; i <= numLaps; i++ {
		best[i] = INF
	}
	ct := int64(changeTime)

	for _, t := range tires {
		f := int64(t[0])
		r := int64(t[1])

		cur := f          // time for the next lap with this tire
		sum := int64(0)   // cumulative time for consecutive laps
		for k := 1; k <= numLaps && cur <= ct+f; k++ {
			sum += cur
			if int(sum) < best[k] {
				best[k] = int(sum)
			}
			cur *= r
		}
	}

	// dp[l] = minimal total time to finish l laps
	dp := make([]int, numLaps+1)
	for i := 0; i <= numLaps; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	for l := 1; l <= numLaps; l++ {
		for k := 1; k <= l; k++ {
			if best[k] == INF {
				continue
			}
			cand := dp[l-k] + best[k]
			if l != k { // need a tire change before this segment
				cand += changeTime
			}
			if cand < dp[l] {
				dp[l] = cand
			}
		}
	}

	return dp[numLaps]
}
```

## Ruby

```ruby
def minimum_finish_time(tires, change_time, num_laps)
  max = num_laps
  inf = (1 << 60)
  best = Array.new(max + 1, inf)

  tires.each do |f, r|
    total = 0
    cur = f
    cnt = 0
    while cnt < max && cur <= change_time + f
      cnt += 1
      total += cur
      best[cnt] = total if total < best[cnt]
      cur *= r
    end
  end

  dp = Array.new(max + 1, inf)
  dp[0] = 0
  (1..max).each do |l|
    dp[l] = best[l] if best[l] < inf
    (1...l).each do |k|
      next if best[k] == inf
      cand = dp[l - k] + change_time + best[k]
      dp[l] = cand if cand < dp[l]
    end
  end

  dp[max]
end
```

## Scala

```scala
import scala.util.control.Breaks.{breakable, break}

object Solution {
  def minimumFinishTime(tires: Array[Array[Int]], changeTime: Int, numLaps: Int): Int = {
    val INF: Long = Long.MaxValue / 4
    val best = Array.fill(numLaps + 1)(INF)

    for (t <- tires) {
      val f = t(0).toLong
      val r = t(1).toLong
      var time = f
      var sum = 0L
      breakable {
        for (k <- 1 to numLaps) {
          sum += time
          if (sum < best(k)) best(k) = sum
          time = time * r
          if (time > changeTime + f) break
        }
      }
    }

    val dp = Array.fill(numLaps + 1)(INF)
    dp(0) = 0L

    for (i <- 1 to numLaps) {
      var k = 1
      while (k <= i) {
        if (best(k) < INF && dp(i - k) < INF) {
          var cand = dp(i - k) + best(k)
          if (i != k) cand += changeTime
          if (cand < dp(i)) dp(i) = cand
        }
        k += 1
      }
    }

    dp(numLaps).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_finish_time(tires: Vec<Vec<i32>>, change_time: i32, num_laps: i32) -> i32 {
        let n = num_laps as usize;
        const INF: i64 = 1_i64 << 60;
        let mut best_seg = vec![INF; n + 1]; // best time to run k laps without changing
        for tire in tires.iter() {
            let f = tire[0] as i64;
            let r = tire[1] as i64;
            let mut cur = f;
            let mut sum = 0_i64;
            for lap in 1..=n {
                sum += cur;
                // If continuing further is never better than changing now, stop.
                if sum > (change_time as i64) + f {
                    break;
                }
                if sum < best_seg[lap] {
                    best_seg[lap] = sum;
                }
                // prepare next lap time
                cur = cur * r;
                if cur > INF / 2 {
                    break;
                }
            }
        }

        let mut dp = vec![INF; n + 1];
        dp[0] = 0;
        for i in 1..=n {
            // try finishing the last segment with length k
            for k in 1..=i {
                if best_seg[k] == INF {
                    continue;
                }
                let add_change = if i == k { 0 } else { change_time as i64 };
                let cand = dp[i - k] + add_change + best_seg[k];
                if cand < dp[i] {
                    dp[i] = cand;
                }
            }
        }
        dp[n] as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-finish-time tires changeTime numLaps)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  (let* ((INF (expt 2 60))
         (best (make-vector (+ numLaps 1) INF)))
    ;; pre‑compute minimal time for a continuous stint of k laps
    (for ([ti tires])
      (let* ((f (list-ref ti 0))
             (r (list-ref ti 1)))
        (let loop ((k 1) (cur f) (sum 0))
          (when (and (<= k numLaps) (<= cur (+ changeTime f)))
            (set! sum (+ sum cur))
            (vector-set! best k (min (vector-ref best k) sum))
            (loop (+ k 1) (* cur r) sum)))))
    ;; DP over number of laps
    (let ((dp (make-vector (+ numLaps 1) 0)))
      (vector-set! dp 0 0)
      (for ([i (in-range 1 (+ numLaps 1))])
        (vector-set! dp i (vector-ref best i))
        (for ([k (in-range 1 i)])
          (let ((candidate (+ (vector-ref dp (- i k)) changeTime (vector-ref best k))))
            (when (< candidate (vector-ref dp i))
              (vector-set! dp i candidate)))))
      (vector-ref dp numLaps))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_finish_time/3]).

-spec minimum_finish_time(Tires :: [[integer()]], ChangeTime :: integer(), NumLaps :: integer()) -> integer().
minimum_finish_time(Tires, ChangeTime, NumLaps) ->
    MaxL = NumLaps,
    INF = 1 bsl 60,
    BestMap0 = maps:new(),
    BestMap = lists:foldl(fun([F,R], Acc) ->
                process_tire(F, R, ChangeTime, MaxL, Acc)
            end, BestMap0, Tires),
    DP0 = array:new(MaxL + 1, {default, INF}),
    DP1 = array:set(0, 0, DP0),
    DP = dp_loop(1, MaxL, ChangeTime, BestMap, DP1, INF),
    array:get(NumLaps, DP).

process_tire(F, R, ChangeTime, MaxL, BestMap) ->
    loop_tire(F, R, ChangeTime, MaxL, F, 0, 1, BestMap).

loop_tire(_F, _R, _ChangeTime, _MaxL, _Cur, _Cum, Lap, BestMap) when Lap > _MaxL ->
    BestMap;
loop_tire(F, R, ChangeTime, MaxL, Cur, Cum, Lap, BestMap) ->
    NewCum = Cum + Cur,
    UpdatedMap =
        case maps:find(Lap, BestMap) of
            {ok, Old} when NewCum < Old -> maps:put(Lap, NewCum, BestMap);
            error -> maps:put(Lap, NewCum, BestMap);
            _ -> BestMap
        end,
    NextCur = Cur * R,
    case (Lap + 1) > MaxL orelse NextCur > ChangeTime + F of
        true -> UpdatedMap;
        false -> loop_tire(F, R, ChangeTime, MaxL, NextCur, NewCum, Lap + 1, UpdatedMap)
    end.

dp_loop(I, MaxL, _ChangeTime, _BestMap, DP, _INF) when I > MaxL ->
    DP;
dp_loop(I, MaxL, ChangeTime, BestMap, DPAcc, INF) ->
    StartBest = maps:get(I, BestMap, INF),
    Min0 = StartBest,
    Min = min_over_k(1, I - 1, I, ChangeTime, BestMap, DPAcc, Min0),
    DPNew = array:set(I, Min, DPAcc),
    dp_loop(I + 1, MaxL, ChangeTime, BestMap, DPNew, INF).

min_over_k(K, End, _I, _ChangeTime, _BestMap, _DP, CurMin) when K > End ->
    CurMin;
min_over_k(K, End, I, ChangeTime, BestMap, DP, CurMin) ->
    case maps:find(K, BestMap) of
        {ok, Bk} ->
            Prev = array:get(I - K, DP),
            Candidate = Prev + ChangeTime + Bk,
            NewMin = if Candidate < CurMin -> Candidate; true -> CurMin end,
            min_over_k(K + 1, End, I, ChangeTime, BestMap, DP, NewMin);
        error ->
            min_over_k(K + 1, End, I, ChangeTime, BestMap, DP, CurMin)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_finish_time(tires :: [[integer]], change_time :: integer, num_laps :: integer) :: integer
  def minimum_finish_time(tires, change_time, num_laps) do
    inf = 1 <<< 60

    best_map =
      Enum.reduce(tires, %{}, fn [f, r], acc ->
        process_tire(f, r, change_time, num_laps, acc)
      end)

    dp = List.duplicate(inf, num_laps + 1) |> List.to_tuple()
    dp = put_elem(dp, 0, 0)

    dp =
      Enum.reduce(1..num_laps, dp, fn i, dp_acc ->
        min_val =
          Enum.reduce(1..i, inf, fn k, cur_min ->
            case Map.get(best_map, k) do
              nil -> cur_min
              best_k ->
                prev = elem(dp_acc, i - k)
                cost = prev + (if i == k, do: 0, else: change_time) + best_k
                if cost < cur_min, do: cost, else: cur_min
            end
          end)

        put_elem(dp_acc, i, min_val)
      end)

    elem(dp, num_laps)
  end

  defp process_tire(f, r, change_time, max_laps, best_map) do
    do_process(f, f, 0, 0, change_time, max_laps, best_map)
  end

  defp do_process(_f, _time, _total, laps, _change_time, max_laps, best_map) when laps >= max_laps,
    do: best_map

  defp do_process(f, time, total, laps, change_time, max_laps, best_map) do
    if total + time > change_time + f do
      best_map
    else
      new_total = total + time
      new_laps = laps + 1

      prev = Map.get(best_map, new_laps)

      best_map =
        cond do
          prev == nil -> Map.put(best_map, new_laps, new_total)
          new_total < prev -> Map.put(best_map, new_laps, new_total)
          true -> best_map
        end

      do_process(f, time * r, new_total, new_laps, change_time, max_laps, best_map)
    end
  end
end
```

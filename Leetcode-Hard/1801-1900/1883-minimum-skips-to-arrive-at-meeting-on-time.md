# 1883. Minimum Skips to Arrive at Meeting On Time

## Cpp

```cpp
class Solution {
public:
    int minSkips(vector<int>& dist, int speed, int hoursBefore) {
        int n = dist.size();
        const double INF = 1e30;
        vector<vector<double>> dp(n, vector<double>(n + 1, INF));
        dp[0][0] = (double)dist[0] / speed;
        for (int i = 0; i < n - 1; ++i) {
            double travel = (double)dist[i + 1] / speed;
            for (int k = 0; k <= i; ++k) {
                double cur = dp[i][k];
                if (cur >= INF) continue;
                // do not skip: wait until next integer hour
                double t1 = ceil(cur) + travel;
                if (t1 < dp[i + 1][k]) dp[i + 1][k] = t1;
                // skip the rest
                double t2 = cur + travel;
                if (t2 < dp[i + 1][k + 1]) dp[i + 1][k + 1] = t2;
            }
        }
        const double eps = 1e-9;
        for (int k = 0; k <= n - 1; ++k) {
            if (dp[n - 1][k] <= hoursBefore + eps) return k;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minSkips(int[] dist, int speed, int hoursBefore) {
        int n = dist.length;
        double INF = Double.POSITIVE_INFINITY;
        double[] dp = new double[n + 1];
        java.util.Arrays.fill(dp, INF);
        dp[0] = 0.0;
        double eps = 1e-9;

        for (int i = 0; i < n; i++) {
            double travel = (double) dist[i] / speed;
            double[] ndp = new double[n + 1];
            java.util.Arrays.fill(ndp, INF);
            for (int k = 0; k <= i; k++) { // at most i skips used so far
                if (dp[k] == INF) continue;
                if (i == n - 1) {
                    ndp[k] = Math.min(ndp[k], dp[k] + travel);
                } else {
                    double noSkip = Math.ceil(dp[k] + travel - eps);
                    ndp[k] = Math.min(ndp[k], noSkip);
                    ndp[k + 1] = Math.min(ndp[k + 1], dp[k] + travel);
                }
            }
            dp = ndp;
        }

        for (int k = 0; k <= n; k++) {
            if (dp[k] <= hoursBefore + eps) return k;
        }
        return -1;
    }
}
```

## Python

```python
import math

class Solution(object):
    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        n = len(dist)
        INF = float('inf')
        dp_cur = [INF] * (n + 1)
        dp_cur[0] = 0.0
        eps = 1e-9

        for i in range(n):
            t = dist[i] / speed
            dp_next = [INF] * (n + 1)
            for k in range(i + 1):  # possible skips used so far
                cur = dp_cur[k]
                if cur == INF:
                    continue
                new_time = cur + t
                if i == n - 1:  # last road, no waiting needed
                    if new_time < dp_next[k]:
                        dp_next[k] = new_time
                else:
                    wait = int(math.ceil(new_time - eps))
                    if wait < dp_next[k]:
                        dp_next[k] = wait
                    if new_time < dp_next[k + 1]:
                        dp_next[k + 1] = new_time
            dp_cur = dp_next

        for k in range(n + 1):
            if dp_cur[k] <= hoursBefore + eps:
                return k
        return -1
```

## Python3

```python
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = 10 ** 18
        # dp[i][k] = minimal scaled time after i roads using k skips
        dp = [[INF] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            for k in range(i + 1):  # at most i skips used so far
                cur = dp[i][k]
                if cur == INF:
                    continue
                after_travel = cur + dist[i]  # scaled time (distance units)
                if i == n - 1:  # last road, no waiting needed
                    if after_travel < dp[i + 1][k]:
                        dp[i + 1][k] = after_travel
                else:
                    # not skip: wait until next integer hour
                    waited = ((after_travel + speed - 1) // speed) * speed
                    if waited < dp[i + 1][k]:
                        dp[i + 1][k] = waited
                    # skip this rest
                    if after_travel < dp[i + 1][k + 1]:
                        dp[i + 1][k + 1] = after_travel
        limit = hoursBefore * speed
        for k in range(n):
            if dp[n][k] <= limit:
                return k
        return -1
```

## C

```c
#include <math.h>
#include <stdlib.h>

int minSkips(int* dist, int distSize, int speed, int hoursBefore) {
    const double INF = 1e30;
    const double EPS = 1e-9;
    int n = distSize;
    int sz = n + 1;
    double *dp = (double *)malloc(sizeof(double) * sz * sz);
    for (int i = 0; i < sz * sz; ++i) dp[i] = INF;
    #define IDX(i,k) ((i)*sz + (k))
    dp[IDX(0,0)] = 0.0;

    for (int i = 0; i < n; ++i) {
        double travel = (double)dist[i] / speed;
        for (int k = 0; k <= i; ++k) {
            double cur = dp[IDX(i,k)];
            if (cur >= INF) continue;

            if (i == n - 1) { // last road, no waiting
                double nxt = cur + travel;
                if (nxt < dp[IDX(i+1,k)]) dp[IDX(i+1,k)] = nxt;
            } else {
                // not skip: wait until next integer hour
                double afterTravel = cur + travel;
                double waited = ceil(afterTravel - EPS);
                if (waited < dp[IDX(i+1,k)]) dp[IDX(i+1,k)] = waited;

                // skip this rest
                double nxtSkip = cur + travel;
                if (nxtSkip < dp[IDX(i+1,k+1)]) dp[IDX(i+1,k+1)] = nxtSkip;
            }
        }
    }

    int answer = -1;
    for (int k = 0; k <= n; ++k) {
        double total = dp[IDX(n,k)];
        if (total <= hoursBefore + EPS) {
            answer = k;
            break;
        }
    }

    free(dp);
    return answer;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    public int MinSkips(int[] dist, int speed, int hoursBefore)
    {
        int n = dist.Length;
        const double INF = 1e30;
        double[][] dp = new double[n + 1][];
        for (int i = 0; i <= n; i++)
        {
            dp[i] = new double[n + 1];
            for (int j = 0; j <= n; j++) dp[i][j] = INF;
        }
        dp[0][0] = 0.0;

        for (int i = 0; i < n; i++)
        {
            double travel = (double)dist[i] / speed;
            for (int k = 0; k <= i; k++) // at most i skips used so far
            {
                double cur = dp[i][k];
                if (cur >= INF) continue;

                if (i == n - 1)
                {
                    double nt = cur + travel;
                    if (nt < dp[i + 1][k]) dp[i + 1][k] = nt;
                }
                else
                {
                    // not skip: wait until next integer hour
                    double nt = Math.Ceiling(cur + travel);
                    if (nt < dp[i + 1][k]) dp[i + 1][k] = nt;

                    // skip the rest
                    double ns = cur + travel;
                    if (ns < dp[i + 1][k + 1]) dp[i + 1][k + 1] = ns;
                }
            }
        }

        const double EPS = 1e-9;
        for (int k = 0; k <= n - 1; k++)
        {
            if (dp[n][k] <= hoursBefore + EPS) return k;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} dist
 * @param {number} speed
 * @param {number} hoursBefore
 * @return {number}
 */
var minSkips = function(dist, speed, hoursBefore) {
    const n = dist.length;
    const INF = 1e30;
    let dp = new Array(n + 1).fill(INF);
    dp[0] = 0; // time after processing 0 roads with 0 skips
    
    for (let i = 0; i < n; ++i) {
        const ndp = new Array(n + 1).fill(INF);
        const travel = dist[i] / speed;
        for (let k = 0; k <= i; ++k) { // at most i skips used so far
            const cur = dp[k];
            if (cur === INF) continue;
            let t = cur + travel;
            if (i === n - 1) {
                // last road, no waiting needed
                ndp[k] = Math.min(ndp[k], t);
            } else {
                // not skipping: wait until next integer hour
                const rounded = Math.ceil(t - 1e-9); // epsilon to avoid precision issues
                ndp[k] = Math.min(ndp[k], rounded);
                // skip this rest
                ndp[k + 1] = Math.min(ndp[k + 1], t);
            }
        }
        dp = ndp;
    }
    
    for (let k = 0; k <= n; ++k) {
        if (dp[k] <= hoursBefore + 1e-9) return k;
    }
    return -1;
};
```

## Typescript

```typescript
function minSkips(dist: number[], speed: number, hoursBefore: number): number {
    const n = dist.length;
    const INF = Number.POSITIVE_INFINITY;
    // dp[k] = minimal time after processing current road with k skips used
    let dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    // Process all roads except the last one (where no waiting is required)
    for (let i = 0; i < n - 1; ++i) {
        const travel = dist[i] / speed;
        const next = new Array(n + 1).fill(INF);
        for (let k = 0; k <= i; ++k) { // at most i skips can be used so far
            const cur = dp[k];
            if (cur === INF) continue;
            const afterTravel = cur + travel;

            // Option 1: do not skip the rest, wait until next integer hour
            const rounded = Math.ceil(afterTravel - 1e-9);
            if (rounded < next[k]) next[k] = rounded;

            // Option 2: skip this rest, use one more skip
            if (afterTravel < next[k + 1]) next[k + 1] = afterTravel;
        }
        dp = next;
    }

    // Add travel time of the last road (no waiting afterwards)
    const lastTravel = dist[n - 1] / speed;
    for (let k = 0; k <= n - 1; ++k) {
        if (dp[k] !== INF) dp[k] += lastTravel;
    }

    // Find minimal skips achieving total time within hoursBefore
    for (let k = 0; k <= n - 1; ++k) {
        if (dp[k] <= hoursBefore + 1e-9) return k;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $dist
     * @param Integer $speed
     * @param Integer $hoursBefore
     * @return Integer
     */
    function minSkips($dist, $speed, $hoursBefore) {
        $n = count($dist);
        $maxSkips = $n; // enough space
        $INF = 1e30;
        $dp = array_fill(0, $maxSkips + 1, $INF);
        $dp[0] = 0.0;

        for ($i = 0; $i < $n; $i++) {
            $ndp = array_fill(0, $maxSkips + 1, $INF);
            $travel = $dist[$i] / $speed;
            $isLast = ($i == $n - 1);
            for ($j = 0; $j <= $maxSkips; $j++) {
                if ($dp[$j] >= $INF / 2) continue;
                $newTime = $dp[$j] + $travel;
                if ($isLast) {
                    if ($newTime < $ndp[$j]) $ndp[$j] = $newTime;
                } else {
                    // wait for next integer hour (no skip)
                    $waited = ceil($newTime - 1e-9);
                    if ($waited < $ndp[$j]) $ndp[$j] = $waited;
                    // skip the waiting
                    if ($j + 1 <= $maxSkips && $newTime < $ndp[$j + 1]) {
                        $ndp[$j + 1] = $newTime;
                    }
                }
            }
            $dp = $ndp;
        }

        for ($j = 0; $j <= $maxSkips; $j++) {
            if ($dp[$j] <= $hoursBefore + 1e-9) return $j;
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minSkips(_ dist: [Int], _ speed: Int, _ hoursBefore: Int) -> Int {
        let n = dist.count
        let INF = Double.greatestFiniteMagnitude
        var dp = [Double](repeating: INF, count: n + 1)
        dp[0] = 0.0
        
        for i in 0..<n {
            var next = [Double](repeating: INF, count: n + 1)
            let travel = Double(dist[i]) / Double(speed)
            for k in 0...i {
                let cur = dp[k]
                if cur == INF { continue }
                if i == n - 1 {
                    let newTime = cur + travel
                    if newTime < next[k] {
                        next[k] = newTime
                    }
                } else {
                    // Do not skip: wait until the next integer hour
                    let noSkip = ceil(cur + travel - 1e-9)
                    if noSkip < next[k] {
                        next[k] = noSkip
                    }
                    // Skip the rest
                    let skipTime = cur + travel
                    if k + 1 <= n && skipTime < next[k + 1] {
                        next[k + 1] = skipTime
                    }
                }
            }
            dp = next
        }
        
        let limit = Double(hoursBefore) + 1e-9
        for k in 0...n {
            if dp[k] <= limit {
                return k
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSkips(dist: IntArray, speed: Int, hoursBefore: Int): Int {
        val n = dist.size
        if (n == 1) {
            val time = dist[0].toDouble() / speed
            return if (time <= hoursBefore + 1e-9) 0 else -1
        }
        val INF = Double.MAX_VALUE / 4
        var dp = DoubleArray(n + 1) { INF }
        dp[0] = 0.0
        for (i in 0 until n - 1) {
            val travel = dist[i].toDouble() / speed
            val next = DoubleArray(n + 1) { INF }
            for (k in 0..i) {
                if (dp[k] == INF) continue
                // without skipping the rest: wait until next integer hour
                val tNoSkip = Math.ceil(dp[k] + travel - 1e-9)
                if (tNoSkip < next[k]) next[k] = tNoSkip
                // skip the rest
                val tSkip = dp[k] + travel
                if (tSkip < next[k + 1]) next[k + 1] = tSkip
            }
            dp = next
        }
        val lastTravel = dist[n - 1].toDouble() / speed
        for (k in 0..n) {
            if (dp[k] == INF) continue
            val total = dp[k] + lastTravel
            if (total <= hoursBefore + 1e-9) return k
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minSkips(List<int> dist, int speed, int hoursBefore) {
    int n = dist.length;
    const double INF = double.infinity;
    List<double> dp = List.filled(n + 1, INF);
    dp[0] = 0.0;

    for (int i = 0; i < n; ++i) {
      List<double> ndp = List.filled(n + 1, INF);
      double travel = dist[i] / speed;
      for (int k = 0; k <= i; ++k) {
        double cur = dp[k];
        if (cur == INF) continue;
        double timeAfterTravel = cur + travel;
        if (i == n - 1) {
          // last road, no waiting needed
          if (timeAfterTravel < ndp[k]) ndp[k] = timeAfterTravel;
        } else {
          // not skipping the wait: round up to next integer hour
          double waited = timeAfterTravel.ceilToDouble();
          if (waited < ndp[k]) ndp[k] = waited;
          // skip the wait
          if (timeAfterTravel < ndp[k + 1]) ndp[k + 1] = timeAfterTravel;
        }
      }
      dp = ndp;
    }

    for (int k = 0; k <= n; ++k) {
      if (dp[k] <= hoursBefore + 1e-9) return k;
    }
    return -1;
  }
}
```

## Golang

```go
import "math"

func minSkips(dist []int, speed int, hoursBefore int) int {
    n := len(dist)
    // Quick impossibility check: even without any waits
    totalTravel := 0.0
    spd := float64(speed)
    for _, d := range dist {
        totalTravel += float64(d) / spd
    }
    if totalTravel-float64(hoursBefore) > 1e-9 {
        return -1
    }

    const INF = 1e30
    dp := make([][]float64, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]float64, n+1)
        for j := 0; j <= n; j++ {
            dp[i][j] = INF
        }
    }

    dp[0][0] = float64(dist[0]) / spd

    for i := 0; i < n-1; i++ {
        travel := float64(dist[i+1]) / spd
        for k := 0; k <= n; k++ {
            cur := dp[i][k]
            if cur >= INF/2 {
                continue
            }
            // Not skip: wait until next integer hour
            start := math.Ceil(cur - 1e-9)
            t := start + travel
            if t < dp[i+1][k] {
                dp[i+1][k] = t
            }
            // Skip the rest
            if k+1 <= n {
                t2 := cur + travel
                if t2 < dp[i+1][k+1] {
                    dp[i+1][k+1] = t2
                }
            }
        }
    }

    limit := float64(hoursBefore) + 1e-9
    for k := 0; k <= n; k++ {
        if dp[n-1][k] <= limit {
            return k
        }
    }
    return -1
}
```

## Ruby

```ruby
def min_skips(dist, speed, hours_before)
  n = dist.length
  inf = Float::INFINITY
  dp = Array.new(n + 1, inf)
  dp[0] = 0.0

  (0...n).each do |i|
    travel = dist[i].to_f / speed
    ndp = Array.new(n + 1, inf)

    (0..n).each do |k|
      cur = dp[k]
      next if cur == inf

      t = cur + travel
      if i == n - 1
        ndp[k] = [ndp[k], t].min
      else
        wait_time = t.ceil.to_f
        ndp[k] = [ndp[k], wait_time].min
        ndp[k + 1] = [ndp[k + 1], t].min if k + 1 <= n
      end
    end

    dp = ndp
  end

  (0..n).each do |k|
    return k if dp[k] <= hours_before + 1e-9
  end
  -1
end
```

## Scala

```scala
object Solution {
  def minSkips(dist: Array[Int], speed: Int, hoursBefore: Int): Int = {
    val n = dist.length
    val INF = 1e30
    val dp = Array.fill(n)(Array.fill(n + 1)(INF))

    if (n == 1) {
      val t = dist(0).toDouble / speed
      for (k <- 0 to n) dp(0)(k) = t
    } else {
      val t0 = dist(0).toDouble / speed
      dp(0)(0) = Math.ceil(t0 - 1e-9)
      dp(0)(1) = t0
    }

    for (i <- 1 until n) {
      val ti = dist(i).toDouble / speed
      for (k <- 0 to i) {
        if (i < n - 1) { // not the last road, need possible rounding
          // no skip after this road
          val candNoSkip = Math.ceil(dp(i - 1)(k) + ti - 1e-9)
          dp(i)(k) = math.min(dp(i)(k), candNoSkip)

          // skip this rest (consume one skip)
          if (k > 0) {
            val candSkip = dp(i - 1)(k - 1) + ti
            dp(i)(k) = math.min(dp(i)(k), candSkip)
          }
        } else { // last road, no rounding after it
          val cand = dp(i - 1)(k) + ti
          dp(i)(k) = math.min(dp(i)(k), cand)
        }
      }
    }

    for (k <- 0 to n) {
      if (dp(n - 1)(k) <= hoursBefore + 1e-9) return k
    }
    -1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_skips(dist: Vec<i32>, speed: i32, hours_before: i32) -> i32 {
        let n = dist.len();
        let inf = 1e30_f64;
        // dp[i][k] = minimal time after first i roads using k skips
        let mut dp = vec![vec![inf; n + 1]; n + 1];
        dp[0][0] = 0.0;

        for i in 0..n {
            let travel = dist[i] as f64 / speed as f64;
            for k in 0..=i {
                let cur = dp[i][k];
                if cur >= inf / 2.0 {
                    continue;
                }
                if i == n - 1 {
                    // last road, no rest needed
                    let new_time = cur + travel;
                    if new_time < dp[i + 1][k] {
                        dp[i + 1][k] = new_time;
                    }
                } else {
                    // not skipping the rest: round up to next integer hour
                    let t_no_skip = (cur + travel).ceil();
                    if t_no_skip < dp[i + 1][k] {
                        dp[i + 1][k] = t_no_skip;
                    }
                    // skip the rest
                    let t_skip = cur + travel;
                    if t_skip < dp[i + 1][k + 1] {
                        dp[i + 1][k + 1] = t_skip;
                    }
                }
            }
        }

        let limit = hours_before as f64 + 1e-9; // tolerance for floating errors
        for k in 0..=n {
            if dp[n][k] <= limit {
                return k as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (min-skips dist speed hoursBefore)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length dist))
         (INF 1e30)
         (eps 1e-9)
         (dp (make-vector (+ n 1) INF)))
    (vector-set! dp 0 0.0)
    (for ([i (in-range n)])
      (define travel (exact->inexact (/ (list-ref dist i) speed)))
      (define newdp (make-vector (+ n 1) INF))
      (for ([j (in-range (+ 1 i))])
        (let ((cur (vector-ref dp j)))
          (when (< cur INF)
            (if (= i (- n 1))
                ;; last road: no waiting
                (let ((t (+ cur travel)))
                  (when (< t (vector-ref newdp j))
                    (vector-set! newdp j t)))
                ;; intermediate roads
                (begin
                  ;; do not skip: wait for next integer hour
                  (define t1 (ceil (+ cur travel)))
                  (when (< t1 (vector-ref newdp j))
                    (vector-set! newdp j t1))
                  ;; skip the rest
                  (let ((t2 (+ cur travel)))
                    (when (< t2 (vector-ref newdp (+ j 1)))
                      (vector-set! newdp (+ j 1) t2))))))))
      (set! dp newdp))
    (let loop ((j 0))
      (if (> j n)
          -1
          (if (<= (vector-ref dp j) (+ hoursBefore eps))
              j
              (loop (+ j 1)))))))
```

## Erlang

```erlang
-export([min_skips/3]).

-spec min_skips(Dist :: [integer()], Speed :: integer(), HoursBefore :: integer()) -> integer().
min_skips(Dist, Speed, HoursBefore) ->
    N = length(Dist),
    case N of
        1 ->
            Travel = hd(Dist) / Speed,
            if Travel =< HoursBefore + 1.0e-9 -> 0; true -> -1 end;
        _ ->
            Init = lists:sublist(Dist, N - 1),
            Last = lists:nth(N, Dist),
            DP0 = #{0 => 0.0},
            DPF = process_roads(Init, Speed, DP0),
            TravelLast = Last / Speed,
            find_answer(DPF, TravelLast, HoursBefore)
    end.

process_roads([], _Speed, DP) -> DP;
process_roads([D|Rest], Speed, DP) ->
    Travel = D / Speed,
    NewDP = maps:fold(
        fun(J, Time, Acc) ->
            % not skip
            T1 = math:ceil(Time + Travel - 1.0e-9),
            Acc1 = maybe_put(Acc, J, T1),
            % skip
            J2 = J + 1,
            T2 = Time + Travel,
            maybe_put(Acc1, J2, T2)
        end,
        #{},
        DP),
    process_roads(Rest, Speed, NewDP).

maybe_put(Map, Key, Value) ->
    case maps:get(Key, Map, undefined) of
        undefined -> maps:put(Key, Value, Map);
        Existing when Value < Existing -> maps:put(Key, Value, Map);
        _ -> Map
    end.

find_answer(DP, TravelLast, HoursBefore) ->
    Tolerance = 1.0e-9,
    {Ans, _} = maps:fold(
        fun(J, Time, {BestJ, Found}) ->
            Total = Time + TravelLast,
            if Total =< HoursBefore + Tolerance ->
                case Found of
                    false -> {J, true};
                    true ->
                        if J < BestJ -> {J, true}; true -> {BestJ, true} end
                end;
               true -> {BestJ, Found}
            end
        end,
        {undefined, false},
        DP),
    case Ans of
        undefined -> -1;
        _ -> Ans
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_skips(dist :: [integer], speed :: integer, hours_before :: integer) :: integer
  def min_skips(dist, speed, hours_before) do
    n = length(dist)

    # Only one road: no rests needed.
    if n == 1 do
      total = hd(dist) / speed
      if total <= hours_before + 1.0e-9, do: 0, else: -1
    else
      last_travel = List.last(dist) / speed

      init_dp = %{0 => 0.0}

      dp =
        Enum.reduce(0..(n - 2), init_dp, fn i, acc ->
          travel = Enum.at(dist, i) / speed

          Enum.reduce(acc, %{}, fn {k, t}, new_acc ->
            # Option 1: do not skip the rest after this road
            time_no_skip = Float.ceil(t + travel)
            new_acc =
              Map.update(new_acc, k, time_no_skip, fn existing -> min(existing, time_no_skip) end)

            # Option 2: skip the rest
            time_skip = t + travel
            new_acc =
              Map.update(new_acc, k + 1, time_skip, fn existing -> min(existing, time_skip) end)

            new_acc
          end)
        end)

      max_skips = n - 1

      Enum.reduce_while(0..max_skips, -1, fn k, _ ->
        case Map.fetch(dp, k) do
          {:ok, t} ->
            total = t + last_travel

            if total <= hours_before + 1.0e-9 do
              {:halt, k}
            else
              {:cont, -1}
            end

          :error ->
            {:cont, -1}
        end
      end)
    end
  end
end
```

# 1335. Minimum Difficulty of a Job Schedule

## Cpp

```cpp
class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        int n = jobDifficulty.size();
        if (n < d) return -1;
        const int INF = 1e9;
        vector<int> dpPrev(n, INF), dpCurr(n, INF);
        
        // Day 1 initialization
        int curMax = 0;
        for (int i = 0; i < n; ++i) {
            curMax = max(curMax, jobDifficulty[i]);
            dpPrev[i] = curMax;
        }
        
        for (int day = 2; day <= d; ++day) {
            fill(dpCurr.begin(), dpCurr.end(), INF);
            // i is the last index assigned up to this day
            for (int i = day - 1; i < n; ++i) {
                int maxInSeg = 0;
                // k is the last index of previous day
                for (int k = i - 1; k >= day - 2; --k) {
                    maxInSeg = max(maxInSeg, jobDifficulty[k + 1]);
                    if (dpPrev[k] != INF) {
                        dpCurr[i] = min(dpCurr[i], dpPrev[k] + maxInSeg);
                    }
                }
            }
            dpPrev.swap(dpCurr);
        }
        
        return dpPrev[n - 1] >= INF ? -1 : dpPrev[n - 1];
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (d > n) return -1;
        final int INF = Integer.MAX_VALUE / 2;
        int[][] dp = new int[d + 1][n + 1];
        for (int i = 0; i <= d; i++) Arrays.fill(dp[i], INF);
        dp[0][0] = 0;

        for (int day = 1; day <= d; day++) {
            for (int i = day; i <= n; i++) { // i jobs scheduled in 'day' days
                int curMax = 0;
                for (int j = i - 1; j >= day - 1; j--) { // last day's segment starts at j
                    curMax = Math.max(curMax, jobDifficulty[j]);
                    if (dp[day - 1][j] != INF) {
                        dp[day][i] = Math.min(dp[day][i], dp[day - 1][j] + curMax);
                    }
                }
            }
        }

        return dp[d][n] == INF ? -1 : dp[d][n];
    }
}
```

## Python

```python
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)
        if n < d:
            return -1

        INF = float('inf')
        # dp[i]: min difficulty to schedule jobs[0..i] in current number of days
        dp = [INF] * n
        cur_max = 0
        for i in range(n):
            cur_max = max(cur_max, jobDifficulty[i])
            dp[i] = cur_max  # day = 1

        for day in range(2, d + 1):
            newdp = [INF] * n
            # we need at least 'day' jobs to fill 'day' days
            for i in range(day - 1, n):
                max_last_day = 0
                # split point k: last day starts at job k and ends at i (inclusive)
                # previous days cover up to k-1
                for k in range(i, day - 2, -1):
                    max_last_day = max(max_last_day, jobDifficulty[k])
                    if dp[k - 1] != INF:
                        newdp[i] = min(newdp[i], dp[k - 1] + max_last_day)
            dp = newdp

        return dp[-1] if dp[-1] != INF else -1
```

## Python3

```python
from typing import List
import math

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1

        INF = math.inf
        # dp[i]: minimum difficulty to schedule first i+1 jobs in current number of days
        dp = [INF] * n
        cur_max = 0
        for i in range(n):
            cur_max = max(cur_max, jobDifficulty[i])
            dp[i] = cur_max

        for day in range(2, d + 1):
            newdp = [INF] * n
            # we need at least 'day' jobs to fill 'day' days
            for i in range(day - 1, n):
                cur_max = 0
                # partition point k: last job of previous day is at k-1,
                # current day handles jobs k..i (k >= day-1)
                for k in range(i, day - 2, -1):
                    cur_max = max(cur_max, jobDifficulty[k])
                    if dp[k - 1] != INF:
                        newdp[i] = min(newdp[i], dp[k - 1] + cur_max)
            dp = newdp

        return int(dp[-1]) if dp[-1] != INF else -1
```

## C

```c
#include <limits.h>

int minDifficulty(int* jobDifficulty, int jobDifficultySize, int d) {
    int n = jobDifficultySize;
    if (n < d) return -1;

    const int INF = INT_MAX / 2;
    int dp[11][301];
    
    for (int i = 0; i <= d; ++i)
        for (int j = 0; j <= n; ++j)
            dp[i][j] = INF;
    dp[0][0] = 0;

    for (int day = 1; day <= d; ++day) {
        // i is the number of jobs taken so far (i >= day)
        for (int i = day; i <= n - (d - day); ++i) {
            int curMax = 0;
            // k is the split point: first k jobs done in previous days,
            // jobs k..i-1 are done on current day
            for (int k = i - 1; k >= day - 1; --k) {
                if (jobDifficulty[k] > curMax) curMax = jobDifficulty[k];
                if (dp[day - 1][k] != INF) {
                    int val = dp[day - 1][k] + curMax;
                    if (val < dp[day][i]) dp[day][i] = val;
                }
            }
        }
    }

    return dp[d][n] == INF ? -1 : dp[d][n];
}
```

## Csharp

```csharp
public class Solution {
    public int MinDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.Length;
        if (d > n) return -1;

        const int INF = int.MaxValue / 2;
        int[,] dp = new int[d, n];
        for (int i = 0; i < d; i++)
            for (int j = 0; j < n; j++)
                dp[i, j] = INF;

        int maxSoFar = 0;
        for (int i = 0; i < n; i++) {
            maxSoFar = Math.Max(maxSoFar, jobDifficulty[i]);
            dp[0, i] = maxSoFar;
        }

        for (int day = 1; day < d; day++) {
            for (int i = day; i < n; i++) {
                int curMax = 0;
                // k is the start index of current day's jobs
                for (int k = i; k >= day; k--) {
                    curMax = Math.Max(curMax, jobDifficulty[k]);
                    if (dp[day - 1, k - 1] != INF) {
                        dp[day, i] = Math.Min(dp[day, i], dp[day - 1, k - 1] + curMax);
                    }
                }
            }
        }

        int result = dp[d - 1, n - 1];
        return result >= INF ? -1 : result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} jobDifficulty
 * @param {number} d
 * @return {number}
 */
var minDifficulty = function(jobDifficulty, d) {
    const n = jobDifficulty.length;
    if (d > n) return -1;

    // dp[i]: minimum difficulty to schedule jobs[0..i] in current number of days
    let dp = new Array(n).fill(Infinity);
    let curMax = 0;
    for (let i = 0; i < n; ++i) {
        curMax = Math.max(curMax, jobDifficulty[i]);
        dp[i] = curMax; // day = 1
    }

    for (let day = 2; day <= d; ++day) {
        const newDP = new Array(n).fill(Infinity);
        // At least 'day' jobs must be scheduled to have one per day
        for (let j = day - 1; j < n; ++j) {
            let maxJob = 0;
            // p is the start index of the current day's segment
            for (let p = j; p >= day - 1; --p) {
                maxJob = Math.max(maxJob, jobDifficulty[p]);
                if (dp[p - 1] !== Infinity) {
                    newDP[j] = Math.min(newDP[j], dp[p - 1] + maxJob);
                }
            }
        }
        dp = newDP;
    }

    return dp[n - 1];
};
```

## Typescript

```typescript
function minDifficulty(jobDifficulty: number[], d: number): number {
    const n = jobDifficulty.length;
    if (n < d) return -1;

    const INF = Number.MAX_SAFE_INTEGER;
    let dpPrev = new Array(n).fill(INF);

    // Day 1 initialization
    let maxSoFar = 0;
    for (let i = 0; i < n; i++) {
        maxSoFar = Math.max(maxSoFar, jobDifficulty[i]);
        dpPrev[i] = maxSoFar;
    }

    // Subsequent days
    for (let day = 2; day <= d; day++) {
        const dpCurr = new Array(n).fill(INF);
        // i is the last index of jobs scheduled up to current day
        for (let i = day - 1; i < n; i++) {
            let maxDiff = 0;
            // k is the start index of the segment for the current day
            for (let k = i; k >= day - 1; k--) {
                maxDiff = Math.max(maxDiff, jobDifficulty[k]);
                const prev = dpPrev[k - 1];
                if (prev !== INF) {
                    dpCurr[i] = Math.min(dpCurr[i], prev + maxDiff);
                }
            }
        }
        dpPrev = dpCurr;
    }

    return dpPrev[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $jobDifficulty
     * @param Integer $d
     * @return Integer
     */
    function minDifficulty($jobDifficulty, $d) {
        $n = count($jobDifficulty);
        if ($n < $d) {
            return -1;
        }

        $INF = PHP_INT_MAX;
        // dp[day][i] = minimum difficulty to schedule first i jobs in exactly day days
        $dp = array_fill(0, $d + 1, array_fill(0, $n + 1, $INF));
        $dp[0][0] = 0;

        for ($day = 1; $day <= $d; $day++) {
            // at least one job per day, so i must be >= day
            for ($i = $day; $i <= $n; $i++) {
                $maxDiff = 0;
                // consider the last day's jobs start from position k-1 (0‑based) to i-1
                for ($k = $i; $k >= $day; $k--) {
                    $maxDiff = max($maxDiff, $jobDifficulty[$k - 1]);
                    if ($dp[$day - 1][$k - 1] !== $INF) {
                        $candidate = $dp[$day - 1][$k - 1] + $maxDiff;
                        if ($candidate < $dp[$day][$i]) {
                            $dp[$day][$i] = $candidate;
                        }
                    }
                }
            }
        }

        return $dp[$d][$n] === $INF ? -1 : $dp[$d][$n];
    }
}
```

## Swift

```swift
class Solution {
    func minDifficulty(_ jobDifficulty: [Int], _ d: Int) -> Int {
        let n = jobDifficulty.count
        if d > n { return -1 }
        let INF = Int.max / 2
        var dp = Array(repeating: Array(repeating: INF, count: n + 1), count: d + 1)
        dp[0][0] = 0
        
        for day in 1...d {
            if day > n { break }
            for i in day...n {
                var maxDiff = 0
                var j = i - 1
                while j >= day - 1 {
                    maxDiff = max(maxDiff, jobDifficulty[j])
                    let prev = dp[day - 1][j]
                    if prev != INF {
                        dp[day][i] = min(dp[day][i], prev + maxDiff)
                    }
                    j -= 1
                }
            }
        }
        
        let ans = dp[d][n]
        return ans == INF ? -1 : ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDifficulty(jobDifficulty: IntArray, d: Int): Int {
        val n = jobDifficulty.size
        if (d > n) return -1
        val INF = 1_000_000_007
        val dp = Array(d + 1) { IntArray(n + 1) { INF } }
        dp[0][0] = 0
        for (day in 1..d) {
            for (i in day..n) {
                var maxJob = 0
                var j = i
                while (j >= day) {
                    maxJob = kotlin.math.max(maxJob, jobDifficulty[j - 1])
                    val prev = dp[day - 1][j - 1]
                    if (prev + maxJob < dp[day][i]) {
                        dp[day][i] = prev + maxJob
                    }
                    j--
                }
            }
        }
        val ans = dp[d][n]
        return if (ans >= INF) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  int minDifficulty(List<int> jobDifficulty, int d) {
    int n = jobDifficulty.length;
    if (n < d) return -1;
    const int INF = 1 << 30;

    // dp[i]: minimum difficulty to schedule first i jobs in current number of days
    List<int> dp = List.filled(n + 1, INF);
    int curMax = 0;
    for (int i = 1; i <= n; ++i) {
      curMax = curMax > jobDifficulty[i - 1] ? curMax : jobDifficulty[i - 1];
      dp[i] = curMax;
    }

    // iterate over days
    for (int day = 2; day <= d; ++day) {
      List<int> ndp = List.filled(n + 1, INF);
      // need at least 'day' jobs to fill 'day' days
      for (int i = day; i <= n; ++i) {
        int maxInSegment = 0;
        // split point k: previous days cover first k-1 jobs,
        // current day covers jobs k..i (1‑based)
        for (int k = i; k >= day; --k) {
          int diff = jobDifficulty[k - 1];
          if (diff > maxInSegment) maxInSegment = diff;
          int candidate = dp[k - 1] + maxInSegment;
          if (candidate < ndp[i]) ndp[i] = candidate;
        }
      }
      dp = ndp;
    }

    return dp[n];
  }
}
```

## Golang

```go
func minDifficulty(jobDifficulty []int, d int) int {
    n := len(jobDifficulty)
    if n < d {
        return -1
    }
    const INF = int(1e9)

    dpPrev := make([]int, n+1)
    for i := 0; i <= n; i++ {
        dpPrev[i] = INF
    }
    dpPrev[0] = 0

    for day := 1; day <= d; day++ {
        dpCurr := make([]int, n+1)
        for i := 0; i <= n; i++ {
            dpCurr[i] = INF
        }
        // i is the number of jobs considered (first i jobs)
        for i := day; i <= n; i++ {
            maxDiff := 0
            // j is the split point: first j jobs scheduled in previous days,
            // jobs [j, i) are done on current day
            for j := i - 1; j >= day-1; j-- {
                if jobDifficulty[j] > maxDiff {
                    maxDiff = jobDifficulty[j]
                }
                if dpPrev[j] != INF && dpPrev[j]+maxDiff < dpCurr[i] {
                    dpCurr[i] = dpPrev[j] + maxDiff
                }
            }
        }
        dpPrev = dpCurr
    }

    if dpPrev[n] >= INF {
        return -1
    }
    return dpPrev[n]
}
```

## Ruby

```ruby
def min_difficulty(job_difficulty, d)
  n = job_difficulty.length
  return -1 if n < d

  inf = 1 << 60
  dp = Array.new(n, inf)

  cur_max = 0
  (0...n).each do |i|
    cur_max = [cur_max, job_difficulty[i]].max
    dp[i] = cur_max
  end

  (2..d).each do |day|
    new_dp = Array.new(n, inf)
    (day - 1...n).each do |j|
      max_seg = 0
      (j - 1).downto(day - 2) do |k|
        max_seg = [max_seg, job_difficulty[k + 1]].max
        if dp[k] != inf
          val = dp[k] + max_seg
          new_dp[j] = val if val < new_dp[j]
        end
      end
    end
    dp = new_dp
  end

  dp[n - 1]
end
```

## Scala

```scala
object Solution {
    def minDifficulty(jobDifficulty: Array[Int], d: Int): Int = {
        val n = jobDifficulty.length
        if (n < d) return -1
        val INF = Int.MaxValue / 2
        val dp = Array.fill(d + 1, n + 1)(INF)
        dp(0)(0) = 0

        for (day <- 1 to d) {
            for (i <- day to n) {
                var maxDiff = 0
                var j = i - 1
                while (j >= day - 1) {
                    maxDiff = math.max(maxDiff, jobDifficulty(j))
                    val prev = dp(day - 1)(j)
                    if (prev + maxDiff < dp(day)(i)) {
                        dp(day)(i) = prev + maxDiff
                    }
                    j -= 1
                }
            }
        }

        val ans = dp(d)(n)
        if (ans >= INF) -1 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_difficulty(job_difficulty: Vec<i32>, d: i32) -> i32 {
        let n = job_difficulty.len();
        let days = d as usize;
        if n < days {
            return -1;
        }
        const INF: i32 = 1_000_000_000;
        // dp[day][i] = min difficulty to schedule jobs[0..=i] in (day+1) days
        let mut dp = vec![vec![INF; n]; days];
        // first day
        let mut cur_max = 0;
        for i in 0..n {
            cur_max = cur_max.max(job_difficulty[i]);
            dp[0][i] = cur_max;
        }
        // subsequent days
        for day in 1..days {
            for i in day..n {
                let mut max_in_day = 0;
                let mut best = INF;
                // split point k: current day handles jobs[k..=i]
                for k in (day..=i).rev() {
                    max_in_day = max_in_day.max(job_difficulty[k]);
                    let prev = dp[day - 1][k - 1];
                    if prev != INF {
                        best = best.min(prev + max_in_day);
                    }
                }
                dp[day][i] = best;
            }
        }
        let ans = dp[days - 1][n - 1];
        if ans >= INF { -1 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (min-difficulty jobDifficulty d)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length jobDifficulty))
         (INF 1000000000))
    (if (< n d)
        -1
        (let* ((jobs (list->vector jobDifficulty))
               (dp   (make-vector (add1 d))))
          ;; allocate dp vectors
          (for ([day (in-range (add1 d))])
            (vector-set! dp day (make-vector (add1 n) INF)))
          ;; base case: day 1
          (let ((vec (vector-ref dp 1)))
            (define curMaxInt 0)
            (for ([i (in-range 1 (add1 n))])
              (set! curMaxInt (max curMaxInt (vector-ref jobs (- i 1))))
              (vector-set! vec i curMaxInt)))
          ;; DP for days 2..d
          (for ([day (in-range 2 (add1 d))])
            (let ((curVec  (vector-ref dp day))
                  (prevVec (vector-ref dp (- day 1))))
              (for ([i (in-range day (add1 n))]) ; i >= day
                (define best INF)
                (define curMaxInt 0)
                ;; k goes from i-1 down to day-1 inclusive
                (for ([k (in-range (sub1 i) (- day 2) -1)])
                  (set! curMaxInt (max curMaxInt (vector-ref jobs k)))
                  (define candidate (+ (vector-ref prevVec k) curMaxInt))
                  (when (< candidate best)
                    (set! best candidate)))
                (vector-set! curVec i best))))
          ;; answer
          (let ((ans (vector-ref (vector-ref dp d) n)))
            ans)))))
```

## Erlang

```erlang
-module(solution).
-export([min_difficulty/2]).

-define(INF, 1 bsl 60).

min_difficulty(JobDifficulty, D) ->
    N = length(JobDifficulty),
    if
        D > N -> -1;
        true ->
            JobArr = list_to_tuple(JobDifficulty),
            PrevMap0 = #{0 => 0},
            FinalMap = day_loop(1, D, N, JobArr, ?INF, PrevMap0),
            case maps:get(N, FinalMap, ?INF) of
                V when V >= ?INF -> -1;
                V -> V
            end
    end.

day_loop(CurDay, MaxDay, N, _JobArr, _Inf, PrevMap) when CurDay > MaxDay ->
    PrevMap;
day_loop(CurDay, MaxDay, N, JobArr, Inf, PrevMap) ->
    CurrMap = outer_loop(CurDay, N, CurDay, PrevMap, JobArr, Inf, #{}),
    day_loop(CurDay + 1, MaxDay, N, JobArr, Inf, CurrMap).

outer_loop(I, N, Day, PrevMap, JobArr, Inf, AccMap) when I =< N ->
    Best = inner_loop(I - 1, Day - 1, 0, Inf, JobArr, PrevMap, Inf),
    NewAccMap = maps:put(I, Best, AccMap),
    outer_loop(I + 1, N, Day, PrevMap, JobArr, Inf, NewAccMap);
outer_loop(_I, _N, _Day, _PrevMap, _JobArr, _Inf, AccMap) ->
    AccMap.

inner_loop(K, Stop, MaxSoFar, BestSoFar, _JobArr, _PrevMap, Inf) when K < Stop ->
    BestSoFar;
inner_loop(K, Stop, MaxSoFar, BestSoFar, JobArr, PrevMap, Inf) ->
    JobVal = element(K + 1, JobArr),
    NewMax = if JobVal > MaxSoFar -> JobVal; true -> MaxSoFar end,
    PrevVal = maps:get(K, PrevMap, Inf),
    Candidate = PrevVal + NewMax,
    NewBest = if Candidate < BestSoFar -> Candidate; true -> BestSoFar end,
    inner_loop(K - 1, Stop, NewMax, NewBest, JobArr, PrevMap, Inf).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_difficulty(job_difficulty :: [integer], d :: integer) :: integer
  def min_difficulty(job_difficulty, d) do
    n = length(job_difficulty)

    if n < d do
      -1
    else
      inf = 1_000_000_000

      # dp for day = 1: dp[i] = max of job_difficulty[0..i-1]
      {dp_prev, _} =
        Enum.reduce(1..n, {%{}, 0}, fn i, {acc, cur_max} ->
          val = Enum.at(job_difficulty, i - 1)
          new_max = if val > cur_max, do: val, else: cur_max
          {Map.put(acc, i, new_max), new_max}
        end)

      dp_final =
        Enum.reduce(2..d, dp_prev, fn day, dp_prev_day ->
          dp_curr =
            Enum.reduce(day..n, %{}, fn i, acc ->
              ks = Enum.to_list((day - 1)..(i - 1)) |> Enum.reverse

              {_, best} =
                Enum.reduce(ks, {0, inf}, fn k, {cur_max, best_val} ->
                  cur_job = Enum.at(job_difficulty, k)
                  cur_max = if cur_job > cur_max, do: cur_job, else: cur_max
                  prev = Map.get(dp_prev_day, k, inf)
                  cand = prev + cur_max
                  new_best = if cand < best_val, do: cand, else: best_val
                  {cur_max, new_best}
                end)

              Map.put(acc, i, best)
            end)

          dp_curr
        end)

      Map.get(dp_final, n, -1)
    end
  end
end
```

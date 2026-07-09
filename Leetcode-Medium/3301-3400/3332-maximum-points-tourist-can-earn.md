# 3332. Maximum Points Tourist Can Earn

## Cpp

```cpp
class Solution {
public:
    int maxScore(int n, int k, vector<vector<int>>& stayScore, vector<vector<int>>& travelScore) {
        const int INF_NEG = -1e9;
        vector<vector<int>> dp(k, vector<int>(n, INF_NEG));
        
        // Day 0 initialization
        for (int c = 0; c < n; ++c) {
            int bestTravel = 0;
            for (int s = 0; s < n; ++s) {
                bestTravel = max(bestTravel, travelScore[s][c]);
            }
            dp[0][c] = max(stayScore[0][c], bestTravel);
        }
        
        // Subsequent days
        for (int d = 1; d < k; ++d) {
            for (int c = 0; c < n; ++c) {
                int stayOption = dp[d-1][c] + stayScore[d][c];
                int travelOption = INF_NEG;
                for (int p = 0; p < n; ++p) {
                    if (p == c) continue;
                    travelOption = max(travelOption, dp[d-1][p] + travelScore[p][c]);
                }
                dp[d][c] = max(stayOption, travelOption);
            }
        }
        
        int ans = 0;
        for (int c = 0; c < n; ++c) {
            ans = max(ans, dp[k-1][c]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxScore(int n, int k, int[][] stayScore, int[][] travelScore) {
        int[] dpPrev = new int[n];
        // initially zero points before any day
        for (int day = 0; day < k; day++) {
            int[] dpCurr = new int[n];
            for (int city = 0; city < n; city++) {
                int stay = dpPrev[city] + stayScore[day][city];
                int bestTravel = Integer.MIN_VALUE;
                for (int prev = 0; prev < n; prev++) {
                    if (prev == city) continue;
                    int cand = dpPrev[prev] + travelScore[prev][city];
                    if (cand > bestTravel) bestTravel = cand;
                }
                dpCurr[city] = Math.max(stay, bestTravel);
            }
            dpPrev = dpCurr;
        }
        int ans = 0;
        for (int val : dpPrev) {
            if (val > ans) ans = val;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, n, k, stayScore, travelScore):
        """
        :type n: int
        :type k: int
        :type stayScore: List[List[int]]
        :type travelScore: List[List[int]]
        :rtype: int
        """
        INF_NEG = -10**9
        dp = [0] * n  # points after previous day, before any action it's zero for any start city
        for day in range(k):
            new_dp = [INF_NEG] * n
            # travel transitions
            for prev in range(n):
                base = dp[prev]
                row = travelScore[prev]
                for nxt in range(n):
                    if nxt == prev:
                        continue
                    val = base + row[nxt]
                    if val > new_dp[nxt]:
                        new_dp[nxt] = val
            # stay transitions
            cur_stay = stayScore[day]
            for city in range(n):
                val = dp[city] + cur_stay[city]
                if val > new_dp[city]:
                    new_dp[city] = val
            dp = new_dp
        return max(dp)
```

## Python3

```python
from typing import List

class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        # dp[c] = max points ending day d in city c
        dp = [0] * n
        # Day 0 initialization: either stay or travel from any start city
        for c in range(n):
            best = stayScore[0][c]
            for s in range(n):
                val = travelScore[s][c]
                if val > best:
                    best = val
            dp[c] = best

        # Process subsequent days
        for d in range(1, k):
            new_dp = [-10**9] * n
            for c in range(n):
                # Stay in the same city
                best = dp[c] + stayScore[d][c]
                # Travel from any other city
                for p in range(n):
                    if p == c:
                        continue
                    cand = dp[p] + travelScore[p][c]
                    if cand > best:
                        best = cand
                new_dp[c] = best
            dp = new_dp

        return max(dp)
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int maxScore(int n, int k, int** stayScore, int stayScoreSize, int* stayScoreColSize,
             int** travelScore, int travelScoreSize, int* travelScoreColSize) {
    int *prev = (int *)malloc(n * sizeof(int));
    int *cur  = (int *)malloc(n * sizeof(int));

    // Day 0 initialization
    for (int c = 0; c < n; ++c) {
        int best = stayScore[0][c];
        for (int s = 0; s < n; ++s) {
            if (travelScore[s][c] > best)
                best = travelScore[s][c];
        }
        prev[c] = best;
    }

    // Subsequent days
    for (int day = 1; day < k; ++day) {
        for (int c = 0; c < n; ++c) {
            int stay = stayScore[day][c] + prev[c];
            int travelBest = INT_MIN;
            for (int p = 0; p < n; ++p) {
                int cand = travelScore[p][c] + prev[p];
                if (cand > travelBest)
                    travelBest = cand;
            }
            cur[c] = stay > travelBest ? stay : travelBest;
        }
        // swap prev and cur
        int *tmp = prev;
        prev = cur;
        cur = tmp;
    }

    int answer = INT_MIN;
    for (int c = 0; c < n; ++c) {
        if (prev[c] > answer)
            answer = prev[c];
    }

    free(prev);
    free(cur);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxScore(int n, int k, int[][] stayScore, int[][] travelScore) {
        // dpPrev[j]: max points after previous day ending at city j
        long[] dpPrev = new long[n];
        for (int i = 0; i < n; i++) dpPrev[i] = 0;
        
        for (int day = 0; day < k; day++) {
            long[] dpCurr = new long[n];
            // Initialize with very small values
            for (int j = 0; j < n; j++) dpCurr[j] = long.MinValue / 4;
            
            for (int cur = 0; cur < n; cur++) {
                long baseScore = dpPrev[cur];
                
                // Stay in the same city
                long stayVal = baseScore + stayScore[day][cur];
                if (stayVal > dpCurr[cur]) dpCurr[cur] = stayVal;
                
                // Travel to another city
                for (int nxt = 0; nxt < n; nxt++) {
                    if (nxt == cur) continue;
                    long travelVal = baseScore + travelScore[cur][nxt];
                    if (travelVal > dpCurr[nxt]) dpCurr[nxt] = travelVal;
                }
            }
            dpPrev = dpCurr;
        }
        
        long ans = 0;
        foreach (var v in dpPrev) {
            if (v > ans) ans = v;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number[][]} stayScore
 * @param {number[][]} travelScore
 * @return {number}
 */
var maxScore = function(n, k, stayScore, travelScore) {
    let dpPrev = new Array(n).fill(0);
    for (let day = 0; day < k; day++) {
        const bestTravel = new Array(n).fill(-Infinity);
        // compute best value to arrive at each city by traveling today
        for (let p = 0; p < n; p++) {
            const base = dpPrev[p];
            const row = travelScore[p];
            for (let c = 0; c < n; c++) {
                const val = base + row[c];
                if (val > bestTravel[c]) bestTravel[c] = val;
            }
        }
        const cur = new Array(n);
        const stayRow = stayScore[day];
        // decide to stay or travel for each city
        for (let c = 0; c < n; c++) {
            const stay = dpPrev[c] + stayRow[c];
            cur[c] = Math.max(stay, bestTravel[c]);
        }
        dpPrev = cur;
    }
    let ans = 0;
    for (const v of dpPrev) if (v > ans) ans = v;
    return ans;
};
```

## Typescript

```typescript
function maxScore(n: number, k: number, stayScore: number[][], travelScore: number[][]): number {
    // dp[c] = max points after previous day ending at city c
    let dp = new Array<number>(n).fill(0);

    // Day 0 initialization: can start anywhere, then either stay or travel to c
    for (let c = 0; c < n; ++c) {
        let best = stayScore[0][c];
        for (let s = 0; s < n; ++s) {
            if (s === c) continue;
            const val = travelScore[s][c];
            if (val > best) best = val;
        }
        dp[c] = best;
    }

    // Process remaining days
    for (let day = 1; day < k; ++day) {
        const ndp = new Array<number>(n).fill(0);
        for (let c = 0; c < n; ++c) {
            // Stay in the same city
            let stay = dp[c] + stayScore[day][c];

            // Travel from any other city
            let travelBest = -Infinity;
            for (let p = 0; p < n; ++p) {
                if (p === c) continue;
                const cand = dp[p] + travelScore[p][c];
                if (cand > travelBest) travelBest = cand;
            }

            ndp[c] = stay > travelBest ? stay : travelBest;
        }
        dp = ndp;
    }

    // Answer is the maximum over all ending cities
    return Math.max(...dp);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer[][] $stayScore
     * @param Integer[][] $travelScore
     * @return Integer
     */
    function maxScore($n, $k, $stayScore, $travelScore) {
        // dp[city] = max points after previous day ending at city
        $dp = array_fill(0, $n, 0);
        for ($day = 0; $day < $k; $day++) {
            $new = array_fill(0, $n, 0);
            for ($city = 0; $city < $n; $city++) {
                // Stay in the same city
                $best = $dp[$city] + $stayScore[$day][$city];
                // Travel from any other city
                for ($prev = 0; $prev < $n; $prev++) {
                    if ($prev == $city) continue;
                    $cand = $dp[$prev] + $travelScore[$prev][$city];
                    if ($cand > $best) {
                        $best = $cand;
                    }
                }
                $new[$city] = $best;
            }
            $dp = $new;
        }
        return max($dp);
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ n: Int, _ k: Int, _ stayScore: [[Int]], _ travelScore: [[Int]]) -> Int {
        var dp = Array(repeating: 0, count: n)
        for day in 0..<k {
            var newDP = Array(repeating: Int.min / 2, count: n)
            // Stay option
            for city in 0..<n {
                let val = dp[city] + stayScore[day][city]
                if val > newDP[city] {
                    newDP[city] = val
                }
            }
            // Travel option
            for i in 0..<n {
                let base = dp[i]
                for j in 0..<n where i != j {
                    let val = base + travelScore[i][j]
                    if val > newDP[j] {
                        newDP[j] = val
                    }
                }
            }
            dp = newDP
        }
        return dp.max()!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(n: Int, k: Int, stayScore: Array<IntArray>, travelScore: Array<IntArray>): Int {
        var dpPrev = IntArray(n) { 0 }
        for (day in 0 until k) {
            val dpCur = IntArray(n) { Int.MIN_VALUE }
            for (i in 0 until n) {
                val base = dpPrev[i]
                // stay in the same city
                val stayVal = base + stayScore[day][i]
                if (stayVal > dpCur[i]) dpCur[i] = stayVal
                // travel to another city
                for (j in 0 until n) {
                    if (i == j) continue
                    val travelVal = base + travelScore[i][j]
                    if (travelVal > dpCur[j]) dpCur[j] = travelVal
                }
            }
            dpPrev = dpCur
        }
        var ans = 0
        for (v in dpPrev) {
            if (v > ans) ans = v
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(int n, int k, List<List<int>> stayScore, List<List<int>> travelScore) {
    // dpPrev[c] = max score after previous day ending at city c
    List<int> dpPrev = List.filled(n, 0);

    // Day 0 initialization: either stay or start somewhere and travel to c
    for (int c = 0; c < n; ++c) {
      int best = stayScore[0][c];
      for (int s = 0; s < n; ++s) {
        int cand = travelScore[s][c]; // start at s, travel to c on day 0
        if (cand > best) best = cand;
      }
      dpPrev[c] = best;
    }

    // Process remaining days
    for (int day = 1; day < k; ++day) {
      List<int> dpCurr = List.filled(n, 0);
      for (int c = 0; c < n; ++c) {
        int stayOption = dpPrev[c] + stayScore[day][c];
        int travelOption = -1;
        for (int p = 0; p < n; ++p) {
          int cand = dpPrev[p] + travelScore[p][c];
          if (cand > travelOption) travelOption = cand;
        }
        dpCurr[c] = stayOption > travelOption ? stayOption : travelOption;
      }
      dpPrev = dpCurr;
    }

    // Answer is the maximum over all ending cities
    int ans = dpPrev[0];
    for (int i = 1; i < n; ++i) {
      if (dpPrev[i] > ans) ans = dpPrev[i];
    }
    return ans;
  }
}
```

## Golang

```go
func maxScore(n int, k int, stayScore [][]int, travelScore [][]int) int {
	if k == 0 {
		return 0
	}
	dpPrev := make([]int, n)
	// Day 0 initialization: start anywhere, then either stay or travel from any city.
	for c := 0; c < n; c++ {
		best := stayScore[0][c]
		for p := 0; p < n; p++ {
			if travelScore[p][c] > best {
				best = travelScore[p][c]
			}
		}
		dpPrev[c] = best
	}
	// Process remaining days.
	for d := 1; d < k; d++ {
		dpCurr := make([]int, n)
		for c := 0; c < n; c++ {
			best := dpPrev[c] + stayScore[d][c]
			for p := 0; p < n; p++ {
				if p == c {
					continue
				}
				val := dpPrev[p] + travelScore[p][c]
				if val > best {
					best = val
				}
			}
			dpCurr[c] = best
		}
		dpPrev = dpCurr
	}
	ans := 0
	for _, v := range dpPrev {
		if v > ans {
			ans = v
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_score(n, k, stay_score, travel_score)
  neg_inf = -10**15
  prev = Array.new(n, 0)

  (0...k).each do |day|
    cur = Array.new(n, neg_inf)

    # Stay in the same city
    n.times do |city|
      val = prev[city] + stay_score[day][city]
      cur[city] = val if val > cur[city]
    end

    # Travel from any city i to city j
    n.times do |i|
      pi = prev[i]
      row = travel_score[i]
      n.times do |j|
        val = pi + row[j]
        cur[j] = val if val > cur[j]
      end
    end

    prev = cur
  end

  prev.max
end
```

## Scala

```scala
object Solution {
    def maxScore(n: Int, k: Int, stayScore: Array[Array[Int]], travelScore: Array[Array[Int]]): Int = {
        var dpPrev = Array.fill(n)(0)
        for (day <- 0 until k) {
            val stayRow = stayScore(day)
            val dpCurr = Array.ofDim[Int](n)
            for (cur <- 0 until n) {
                var best = dpPrev(cur) + stayRow(cur) // stay in the same city
                var prev = 0
                while (prev < n) {
                    if (prev != cur) {
                        val cand = dpPrev(prev) + travelScore(prev)(cur)
                        if (cand > best) best = cand
                    }
                    prev += 1
                }
                dpCurr(cur) = best
            }
            dpPrev = dpCurr
        }
        dpPrev.max
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(n: i32, k: i32, stay_score: Vec<Vec<i32>>, travel_score: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let k = k as usize;
        if k == 0 {
            return 0;
        }
        let mut dp = vec![vec![0i32; n]; k];
        // Day 0 initialization
        for c in 0..n {
            let mut best = stay_score[0][c];
            for s in 0..n {
                let val = travel_score[s][c];
                if val > best {
                    best = val;
                }
            }
            dp[0][c] = best;
        }
        // Subsequent days
        for d in 1..k {
            for c in 0..n {
                let stay_opt = dp[d - 1][c] + stay_score[d][c];
                let mut travel_best = i32::MIN;
                for p in 0..n {
                    let cand = dp[d - 1][p] + travel_score[p][c];
                    if cand > travel_best {
                        travel_best = cand;
                    }
                }
                dp[d][c] = stay_opt.max(travel_best);
            }
        }
        // Result
        *dp[k - 1].iter().max().unwrap()
    }
}
```

## Racket

```racket
(define/contract (max-score n k stayScore travelScore)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  (let* ([stay-vec (list->vector (map list->vector stayScore))]
         [travel-vec (list->vector (map list->vector travelScore))]
         [INF -1000000000]
         [dp-prev (make-vector n INF)])
    ;; day 0 initialization
    (for ([c (in-range n)])
      (let* ([stay (vector-ref (vector-ref stay-vec 0) c)]
             [best-travel INF])
        (for ([p (in-range n)])
          (when (not (= p c))
            (let ([t (vector-ref (vector-ref travel-vec p) c)])
              (when (> t best-travel)
                (set! best-travel t)))))
        (vector-set! dp-prev c (max stay best-travel))))
    ;; subsequent days
    (for ([day (in-range 1 k)])
      (define dp-curr (make-vector n INF))
      (for ([cur (in-range n)])
        ;; staying in the same city
        (let* ([stay (vector-ref (vector-ref stay-vec day) cur)]
               [cand (+ (vector-ref dp-prev cur) stay)])
          (when (> cand (vector-ref dp-curr cur))
            (vector-set! dp-curr cur cand)))
        ;; traveling from any other city
        (for ([prev (in-range n)])
          (unless (= prev cur)
            (let* ([t (vector-ref (vector-ref travel-vec prev) cur)]
                   [cand (+ (vector-ref dp-prev prev) t)])
              (when (> cand (vector-ref dp-curr cur))
                (vector-set! dp-curr cur cand))))))
      (set! dp-prev dp-curr))
    ;; answer is the maximum over all ending cities
    (apply max (vector->list dp-prev))))
```

## Erlang

```erlang
-spec max_score(N :: integer(), K :: integer(), StayScore :: [[integer()]], TravelScore :: [[integer()]]) -> integer().
max_score(N, K, StayScore, TravelScore) ->
    StayRows = [list_to_tuple(Row) || Row <- StayScore],
    TravelRows = [list_to_tuple(Row) || Row <- TravelScore],
    FirstStayRow = hd(StayRows),
    Prev0 = FirstStayRow,
    FinalPrev = dp_loop(1, K - 1, N, StayRows, TravelRows, Prev0),
    max_in_tuple(FinalPrev).

dp_loop(Day, MaxDay, _N, _StayRows, _TravelRows, Prev) when Day > MaxDay ->
    Prev;
dp_loop(Day, MaxDay, N, StayRows, TravelRows, Prev) ->
    StayRow = lists:nth(Day + 1, StayRows),
    NewList = [compute_new(C, Prev, StayRow, TravelRows, N) || C <- lists:seq(0, N - 1)],
    NewPrev = list_to_tuple(NewList),
    dp_loop(Day + 1, MaxDay, N, StayRows, TravelRows, NewPrev).

compute_new(C, Prev, StayRow, TravelRows, N) ->
    StayOpt = element(C + 1, Prev) + element(C + 1, StayRow),
    TravelMax = travel_max(C, 0, Prev, TravelRows, N, -1),
    erlang:max(StayOpt, TravelMax).

travel_max(_C, P, _Prev, _TravelRows, N, CurMax) when P >= N ->
    CurMax;
travel_max(C, P, Prev, TravelRows, N, CurMax) ->
    if
        P =:= C ->
            travel_max(C, P + 1, Prev, TravelRows, N, CurMax);
        true ->
            SrcPrev = element(P + 1, Prev),
            TravelRow = lists:nth(P + 1, TravelRows),
            TravelScore = element(C + 1, TravelRow),
            Val = SrcPrev + TravelScore,
            NewMax = if Val > CurMax -> Val; true -> CurMax end,
            travel_max(C, P + 1, Prev, TravelRows, N, NewMax)
    end.

max_in_tuple(Tuple) ->
    Size = tuple_size(Tuple),
    max_in_tuple(1, Size, Tuple, 0).

max_in_tuple(Index, Size, _Tuple, CurMax) when Index > Size ->
    CurMax;
max_in_tuple(Index, Size, Tuple, CurMax) ->
    Val = element(Index, Tuple),
    NewMax = if Val > CurMax -> Val; true -> CurMax end,
    max_in_tuple(Index + 1, Size, Tuple, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(n :: integer, k :: integer, stay_score :: [[integer]], travel_score :: [[integer]]) :: integer
  def max_score(n, k, stay_score, travel_score) do
    initial_dp = List.duplicate(0, n)

    final_dp =
      Enum.reduce(0..(k - 1), initial_dp, fn day, cur_dp ->
        stay_row = Enum.at(stay_score, day)

        for c <- 0..(n - 1) do
          stay_opt = Enum.at(cur_dp, c) + Enum.at(stay_row, c)

          travel_opt =
            Enum.reduce(0..(n - 1), 0, fn i, acc ->
              val = Enum.at(cur_dp, i) + (Enum.at(Enum.at(travel_score, i), c))
              if val > acc, do: val, else: acc
            end)

          max(stay_opt, travel_opt)
        end
      end)

    Enum.max(final_dp)
  end
end
```

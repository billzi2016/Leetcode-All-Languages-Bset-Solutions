# 2008. Maximum Earnings From Taxi

## Cpp

```cpp
class Solution {
public:
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        vector<vector<pair<int,long long>>> byStart(n + 2);
        for (const auto& r : rides) {
            int s = r[0], e = r[1], t = r[2];
            long long earn = (long long)(e - s) + t;
            byStart[s].push_back({e, earn});
        }
        vector<long long> dp(n + 2, 0);
        for (int i = n; i >= 1; --i) {
            dp[i] = dp[i + 1];
            for (const auto& p : byStart[i]) {
                int e = p.first;
                long long profit = p.second + dp[e];
                if (profit > dp[i]) dp[i] = profit;
            }
        }
        return dp[1];
    }
};
```

## Java

```java
class Solution {
    public long maxTaxiEarnings(int n, int[][] rides) {
        @SuppressWarnings("unchecked")
        List<int[]>[] byStart = new ArrayList[n + 1];
        for (int[] r : rides) {
            int s = r[0];
            if (byStart[s] == null) byStart[s] = new ArrayList<>();
            byStart[s].add(r);
        }
        long[] dp = new long[n + 2]; // dp[i]: max earnings from point i to n
        for (int i = n; i >= 1; --i) {
            dp[i] = dp[i + 1]; // skip any ride starting at i
            List<int[]> list = byStart[i];
            if (list != null) {
                for (int[] r : list) {
                    int s = r[0], e = r[1], t = r[2];
                    long profit = (long) (e - s + t) + dp[e];
                    if (profit > dp[i]) dp[i] = profit;
                }
            }
        }
        return dp[1];
    }
}
```

## Python

```python
class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        rides.sort(key=lambda x: x[0])
        dp = [0] * (n + 1)
        i = 0
        m = len(rides)
        for pos in range(1, n + 1):
            # carry forward the best earnings up to this point
            if dp[pos - 1] > dp[pos]:
                dp[pos] = dp[pos - 1]
            # process all rides that start at current position
            while i < m and rides[i][0] == pos:
                s, e, tip = rides[i]
                earn = e - s + tip
                if dp[e] < dp[s] + earn:
                    dp[e] = dp[s] + earn
                i += 1
        return dp[n]
```

## Python3

```python
from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides_by_start = [[] for _ in range(n + 1)]
        for s, e, t in rides:
            rides_by_start[s].append((e, e - s + t))
        
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # carry forward the best earnings up to point i
            if dp[i] < dp[i - 1]:
                dp[i] = dp[i - 1]
            cur = dp[i]
            for e, profit in rides_by_start[i]:
                if dp[e] < cur + profit:
                    dp[e] = cur + profit
        return dp[n]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int s;
    int e;
    int t;
} Ride;

int rideCmp(const void *a, const void *b) {
    const Ride *ra = (const Ride *)a;
    const Ride *rb = (const Ride *)b;
    return ra->s - rb->s;
}

long long maxTaxiEarnings(int n, int** rides, int ridesSize, int* ridesColSize) {
    if (ridesSize == 0) return 0LL;

    Ride *arr = (Ride *)malloc(ridesSize * sizeof(Ride));
    for (int i = 0; i < ridesSize; ++i) {
        arr[i].s = rides[i][0];
        arr[i].e = rides[i][1];
        arr[i].t = rides[i][2];
    }

    // Count rides per start point
    int *cnt = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i < ridesSize; ++i) {
        cnt[arr[i].s]++;
    }

    // Allocate lists of ride indices for each start point
    int **idxLists = (int **)malloc((n + 1) * sizeof(int *));
    int *pos = (int *)calloc(n + 1, sizeof(int));
    for (int s = 1; s <= n; ++s) {
        if (cnt[s] > 0) {
            idxLists[s] = (int *)malloc(cnt[s] * sizeof(int));
        } else {
            idxLists[s] = NULL;
        }
    }

    // Fill the lists
    for (int i = 0; i < ridesSize; ++i) {
        int s = arr[i].s;
        idxLists[s][pos[s]++] = i;
    }

    // DP from point n down to 1
    long long *dp = (long long *)calloc(n + 2, sizeof(long long)); // dp[n+1] = 0
    for (int point = n; point >= 1; --point) {
        long long best = dp[point + 1]; // skip any ride starting here
        if (cnt[point] > 0) {
            for (int k = 0; k < cnt[point]; ++k) {
                int idx = idxLists[point][k];
                Ride r = arr[idx];
                long long profit = (long long)(r.e - r.s + r.t) + dp[r.e];
                if (profit > best) best = profit;
            }
        }
        dp[point] = best;
    }

    long long result = dp[1];

    // Clean up
    free(arr);
    free(cnt);
    free(pos);
    for (int s = 1; s <= n; ++s) {
        if (idxLists[s]) free(idxLists[s]);
    }
    free(idxLists);
    free(dp);

    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaxTaxiEarnings(int n, int[][] rides)
    {
        var byStart = new List<(int end, long earn)>[n + 1];
        foreach (var r in rides)
        {
            int start = r[0];
            int end = r[1];
            int tip = r[2];
            long earn = (long)(end - start) + tip;
            if (byStart[start] == null) byStart[start] = new List<(int, long)>();
            byStart[start].Add((end, earn));
        }

        var dp = new long[n + 2]; // dp[i]: max earnings from point i to n
        for (int i = n; i >= 1; --i)
        {
            long best = dp[i + 1]; // skip any ride starting at i
            var list = byStart[i];
            if (list != null)
            {
                foreach (var ride in list)
                {
                    long candidate = ride.earn + dp[ride.end];
                    if (candidate > best) best = candidate;
                }
            }
            dp[i] = best;
        }

        return dp[1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} rides
 * @return {number}
 */
var maxTaxiEarnings = function(n, rides) {
    const startMap = Array.from({ length: n + 1 }, () => []);
    for (const [s, e, t] of rides) {
        startMap[s].push([e, t]);
    }
    
    const dp = new Array(n + 1).fill(0);
    
    for (let i = 1; i <= n; ++i) {
        // carry forward the best earnings up to point i
        if (dp[i] < dp[i - 1]) dp[i] = dp[i - 1];
        
        // consider all rides that start at i
        for (const [end, tip] of startMap[i]) {
            const earn = end - i + tip;
            const candidate = dp[i] + earn;
            if (dp[end] < candidate) dp[end] = candidate;
        }
    }
    
    return dp[n];
};
```

## Typescript

```typescript
function maxTaxiEarnings(n: number, rides: number[][]): number {
    const startMap = new Map<number, [number, number][]>();
    for (const [s, e, t] of rides) {
        const profit = e - s + t;
        if (!startMap.has(s)) startMap.set(s, []);
        startMap.get(s)!.push([e, profit]);
    }
    const dp = new Array<number>(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        dp[i] = Math.max(dp[i], dp[i - 1]);
        const list = startMap.get(i);
        if (list) {
            for (const [end, profit] of list) {
                const val = dp[i] + profit;
                if (val > dp[end]) dp[end] = val;
            }
        }
    }
    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $rides
     * @return Integer
     */
    function maxTaxiEarnings($n, $rides) {
        usort($rides, function($a, $b) {
            return $a[0] <=> $b[0];
        });
        $dp = array_fill(0, $n + 1, 0);
        $idx = 0;
        $m = count($rides);
        for ($i = 1; $i <= $n; $i++) {
            if ($dp[$i] < $dp[$i - 1]) {
                $dp[$i] = $dp[$i - 1];
            }
            while ($idx < $m && $rides[$idx][0] == $i) {
                $start = $rides[$idx][0];
                $end   = $rides[$idx][1];
                $tip   = $rides[$idx][2];
                $profit = $end - $start + $tip;
                $candidate = $dp[$i] + $profit;
                if ($dp[$end] < $candidate) {
                    $dp[$end] = $candidate;
                }
                $idx++;
            }
        }
        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func maxTaxiEarnings(_ n: Int, _ rides: [[Int]]) -> Int {
        var startRides = Array(repeating: [(end: Int, profit: Int)](), count: n + 1)
        for ride in rides {
            let s = ride[0]
            let e = ride[1]
            let t = ride[2]
            let profit = e - s + t
            startRides[s].append((end: e, profit: profit))
        }
        
        var dp = Array(repeating: 0, count: n + 1)
        for i in 1...n {
            if dp[i] < dp[i - 1] {
                dp[i] = dp[i - 1]
            }
            for r in startRides[i] {
                let e = r.end
                let newEarn = dp[i] + r.profit
                if dp[e] < newEarn {
                    dp[e] = newEarn
                }
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTaxiEarnings(n: Int, rides: Array<IntArray>): Long {
        val ridesByStart = Array(n + 1) { mutableListOf<IntArray>() }
        for (ride in rides) {
            ridesByStart[ride[0]].add(ride)
        }
        val dp = LongArray(n + 1)
        for (i in 1..n) {
            if (dp[i] < dp[i - 1]) dp[i] = dp[i - 1]
            for (ride in ridesByStart[i]) {
                val s = ride[0]
                val e = ride[1]
                val t = ride[2]
                val profit = (e - s + t).toLong()
                val candidate = dp[s] + profit
                if (dp[e] < candidate) dp[e] = candidate
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int maxTaxiEarnings(int n, List<List<int>> rides) {
    // Sort rides by their start point
    rides.sort((a, b) => a[0].compareTo(b[0]));
    // DP array where dp[i] is the maximum earnings up to point i
    List<int> dp = List.filled(n + 2, 0);
    int idx = 0;
    int m = rides.length;

    for (int i = 1; i <= n; ++i) {
      // Carry forward the best value from previous point
      if (dp[i] < dp[i - 1]) dp[i] = dp[i - 1];

      // Process all rides that start at current point i
      while (idx < m && rides[idx][0] == i) {
        int start = rides[idx][0];
        int end = rides[idx][1];
        int tip = rides[idx][2];
        int profit = (end - start) + tip;
        int candidate = dp[start] + profit;
        if (dp[end] < candidate) dp[end] = candidate;
        idx++;
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
func maxTaxiEarnings(n int, rides [][]int) int64 {
    sort.Slice(rides, func(i, j int) bool { return rides[i][0] < rides[j][0] })
    dp := make([]int64, n+1)
    idx, m := 0, len(rides)

    for i := 1; i <= n; i++ {
        if dp[i-1] > dp[i] {
            dp[i] = dp[i-1]
        }
        for idx < m && rides[idx][0] == i {
            start, end, tip := rides[idx][0], rides[idx][1], rides[idx][2]
            profit := int64(end - start + tip)
            if dp[end] < dp[start]+profit {
                dp[end] = dp[start] + profit
            }
            idx++
        }
    }
    return dp[n]
}
```

## Ruby

```ruby
def max_taxi_earnings(n, rides)
  starts = Array.new(n + 2) { [] }
  rides.each do |s, e, t|
    starts[s] << [e, t]
  end

  dp = Array.new(n + 2, 0)

  i = n
  while i >= 1
    best = dp[i + 1]
    starts[i].each do |e, t|
      profit = (e - i + t) + dp[e]
      best = profit if profit > best
    end
    dp[i] = best
    i -= 1
  end

  dp[1]
end
```

## Scala

```scala
object Solution {
  def maxTaxiEarnings(n: Int, rides: Array[Array[Int]]): Long = {
    val ridesByStart = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[(Int, Long)])
    for (r <- rides) {
      val start = r(0)
      val end = r(1)
      val tip = r(2).toLong
      val profit = (end - start).toLong + tip
      ridesByStart(start).append((end, profit))
    }
    val dp = new Array[Long](n + 1)
    for (i <- 1 to n) {
      if (dp(i - 1) > dp(i)) dp(i) = dp(i - 1)
      for ((end, profit) <- ridesByStart(i)) {
        val cand = dp(i) + profit
        if (cand > dp(end)) dp(end) = cand
      }
    }
    dp(n)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_taxi_earnings(n: i32, rides: Vec<Vec<i32>>) -> i64 {
        let n_usize = n as usize;
        // For each start point store list of (end, profit)
        let mut starts: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize + 1];
        for r in rides {
            let s = r[0] as usize;
            let e = r[1] as usize;
            let tip = r[2] as i64;
            let profit = (e - s) as i64 + tip;
            starts[s].push((e, profit));
        }

        // dp[i] = max earnings when reaching point i
        let mut dp: Vec<i64> = vec![0; n_usize + 1];
        for i in 1..=n_usize {
            if dp[i] < dp[i - 1] {
                dp[i] = dp[i - 1];
            }
            let cur = dp[i];
            for &(e, profit) in &starts[i] {
                let cand = cur + profit;
                if dp[e] < cand {
                    dp[e] = cand;
                }
            }
        }
        dp[n_usize]
    }
}
```

## Racket

```racket
(define/contract (max-taxi-earnings n rides)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((dp (make-vector (+ n 1) 0))
         (starts (make-vector (+ n 1) '())))
    ;; bucket rides by their start point
    (for-each (lambda (r)
                (let ((s (list-ref r 0)))
                  (vector-set! starts s (cons r (vector-ref starts s)))))
              rides)
    ;; DP over positions 1..n
    (for ([pos (in-range 1 (+ n 1))])
      (define prev (vector-ref dp (sub1 pos)))
      (define cur (max (vector-ref dp pos) prev))
      (vector-set! dp pos cur)
      (for ([r (in-list (vector-ref starts pos))])
        (let* ((s   (list-ref r 0))
               (e   (list-ref r 1))
               (tip (list-ref r 2))
               (profit (+ (- e s) tip))
               (newval (+ cur profit)))
          (when (> newval (vector-ref dp e))
            (vector-set! dp e newval)))))
    (vector-ref dp n)))
```

## Erlang

```erlang
-spec max_taxi_earnings(integer(), [[integer()]]) -> integer().
max_taxi_earnings(N, Rides) ->
    StartMap = build_start_map(Rides, #{}),
    DP = compute_dp(N, StartMap, #{N+1 => 0}),
    maps:get(1, DP).

build_start_map([], M) -> M;
build_start_map([[S,E,T]|Rest], M) ->
    List = maps:get(S, M, []),
    build_start_map(Rest, maps:put(S, [{E,T}|List], M)).

compute_dp(0, _StartMap, DP) -> DP;
compute_dp(I, StartMap, DP) ->
    NextEarn = maps:get(I+1, DP, 0),
    Rides = maps:get(I, StartMap, []),
    Best = lists:foldl(
        fun({E,T}, Acc) ->
            EarnAfter = maps:get(E, DP, 0),
            Profit = (E - I) + T + EarnAfter,
            if Profit > Acc -> Profit; true -> Acc end
        end,
        NextEarn,
        Rides),
    compute_dp(I-1, StartMap, maps:put(I, Best, DP)).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_taxi_earnings(n :: integer, rides :: [[integer]]) :: integer
  def max_taxi_earnings(n, rides) do
    # Build an array where each index holds the list of rides starting there
    start_arr = :array.from_list(List.duplicate([], n + 1))

    start_arr =
      Enum.reduce(rides, start_arr, fn [s, e, t], acc ->
        list = :array.get(s, acc)
        :array.set(s, [[s, e, t] | list], acc)
      end)

    # DP array storing best earnings achievable when reaching each point
    dp = :array.from_list(List.duplicate(0, n + 1))

    {_dp_final, answer} =
      Enum.reduce(1..n, {dp, 0}, fn i, {dp_acc, best_so_far} ->
        # Best earnings reachable at position i (including rides that end here)
        cur_best = max(best_so_far, :array.get(i, dp_acc))

        rides_i = :array.get(i, start_arr)

        dp_acc =
          Enum.reduce(rides_i, dp_acc, fn [_s, e, t], dpar ->
            profit = e - i + t
            new_val = cur_best + profit
            existing = :array.get(e, dpar)

            if new_val > existing do
              :array.set(e, new_val, dpar)
            else
              dpar
            end
          end)

        {dp_acc, cur_best}
      end)

    answer
  end
end
```

# 1824. Minimum Sideway Jumps

## Cpp

```cpp
class Solution {
public:
    int minSideJumps(vector<int>& obstacles) {
        const int INF = 1e9;
        // dp for lanes 1,2,3 respectively
        vector<int> dp = {1, 0, 1}; // start at lane 2 with 0 jumps
        
        int n = obstacles.size();
        for (int i = 1; i < n; ++i) {
            int obs = obstacles[i];
            if (obs != 0) dp[obs - 1] = INF; // cannot be on blocked lane
            
            int mn = min({dp[0], dp[1], dp[2]});
            for (int lane = 0; lane < 3; ++lane) {
                if (obstacles[i] != lane + 1) { // lane is free at this point
                    dp[lane] = min(dp[lane], mn + 1);
                }
            }
        }
        return min({dp[0], dp[1], dp[2]});
    }
};
```

## Java

```java
class Solution {
    public int minSideJumps(int[] obstacles) {
        int n = obstacles.length;
        int INF = 1_000_000; // larger than any possible answer
        int[] dp = new int[3];
        dp[0] = 1; // lane 1 needs one jump from start (lane 2)
        dp[1] = 0; // start lane
        dp[2] = 1; // lane 3 needs one jump from start

        for (int i = 1; i < n; i++) {
            int obs = obstacles[i];
            if (obs != 0) {
                dp[obs - 1] = INF; // cannot stay on blocked lane
            }
            // try to improve each reachable lane by side jumping from another reachable lane
            for (int lane = 0; lane < 3; lane++) {
                if (obstacles[i] == lane + 1) continue; // this lane is blocked at position i
                for (int other = 0; other < 3; other++) {
                    if (lane == other) continue;
                    if (obstacles[i] == other + 1) continue; // cannot jump from a blocked lane
                    dp[lane] = Math.min(dp[lane], dp[other] + 1);
                }
            }
        }

        return Math.min(dp[0], Math.min(dp[1], dp[2]));
    }
}
```

## Python

```python
class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        INF = 10 ** 9
        # dp[i] = minimum side jumps to be at current position on lane i+1 (i=0,1,2)
        dp = [1, 0, 1]  # start at lane 2 with 0 jumps; lanes 1 and 3 need one jump initially
        for i in range(1, len(obstacles)):
            obs = obstacles[i]
            if obs:
                dp[obs - 1] = INF  # cannot stay on a lane with an obstacle
            min_dp = min(dp)      # best among reachable lanes at this point
            for lane in range(3):
                if obstacles[i] != lane + 1:   # lane is not blocked
                    dp[lane] = min(dp[lane], min_dp + 1)
        return min(dp)
```

## Python3

```python
from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        INF = 10 ** 9
        # dp[lane] = minimum side jumps to be at current position on lane (0-indexed lanes 0..2)
        dp = [INF, 0, INF]  # start at lane 2 (index 1) with 0 jumps
        n = len(obstacles) - 1

        for i in range(1, n + 1):
            obs = obstacles[i] - 1  # convert to 0-indexed; -1 means no obstacle
            if obs >= 0:
                dp[obs] = INF  # cannot stay on blocked lane at this point

            prev = dp[:]  # snapshot before side jumps at this position
            for lane in range(3):
                if lane == obs:
                    continue  # blocked lane
                best_other = min(prev[k] for k in range(3) if k != lane)
                dp[lane] = min(dp[lane], best_other + 1)

        return min(dp)
```

## C

```c
int minSideJumps(int* obstacles, int obstaclesSize) {
    const int INF = 1000000000;
    int dp[4];
    // lanes are indexed 1..3
    dp[1] = 1;   // jump from lane 2 to lane 1 at start
    dp[2] = 0;   // start lane
    dp[3] = 1;   // jump from lane 2 to lane 3 at start

    for (int i = 1; i < obstaclesSize; ++i) {
        int obs = obstacles[i];
        if (obs != 0) {
            dp[obs] = INF;               // cannot stay on a blocked lane
        }
        // find minimal jumps among all lanes at this point
        int mn = dp[1];
        if (dp[2] < mn) mn = dp[2];
        if (dp[3] < mn) mn = dp[3];

        // try side jumps to each unblocked lane
        for (int lane = 1; lane <= 3; ++lane) {
            if (obs == lane) continue;   // lane is blocked at this point
            int candidate = 1 + mn;
            if (candidate < dp[lane]) dp[lane] = candidate;
        }
    }

    int result = dp[1];
    if (dp[2] < result) result = dp[2];
    if (dp[3] < result) result = dp[3];
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSideJumps(int[] obstacles) {
        const int INF = 1_000_000_0;
        int[] dp = new int[3];
        dp[0] = 1; // lane 1
        dp[1] = 0; // lane 2 (starting lane)
        dp[2] = 1; // lane 3

        for (int i = 1; i < obstacles.Length; i++) {
            if (obstacles[i] != 0) {
                dp[obstacles[i] - 1] = INF; // cannot be on this lane at point i
            }

            int best = Math.Min(dp[0], Math.Min(dp[1], dp[2]));
            for (int lane = 0; lane < 3; lane++) {
                if (obstacles[i] == lane + 1) continue; // blocked lane
                dp[lane] = Math.Min(dp[lane], best + 1);
            }
        }

        return Math.Min(dp[0], Math.Min(dp[1], dp[2]));
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} obstacles
 * @return {number}
 */
var minSideJumps = function(obstacles) {
    const INF = 1e9;
    // dp[1], dp[2], dp[3] – minimal side jumps to be at current point in each lane
    let dp = [INF, 1, 0, 1]; // start at lane 2 with 0 jumps; lanes 1 and 3 need one jump
    
    const n = obstacles.length;
    for (let i = 1; i < n - 1; ++i) { // process points 1 .. n-1
        const obs = obstacles[i];
        if (obs !== 0) {
            dp[obs] = INF; // lane blocked at this point
        }
        // best among reachable lanes at this point
        const best = Math.min(dp[1], dp[2], dp[3]);
        for (let lane = 1; lane <= 3; ++lane) {
            if (obstacles[i] !== lane) { // lane not blocked
                dp[lane] = Math.min(dp[lane], best + 1);
            }
        }
    }
    return Math.min(dp[1], dp[2], dp[3]);
};
```

## Typescript

```typescript
function minSideJumps(obstacles: number[]): number {
    const INF = 1e9;
    const dp = [1, 0, 1]; // lanes 1,2,3
    const n = obstacles.length - 1;

    for (let i = 1; i <= n; i++) {
        // block lanes with an obstacle at position i
        for (let lane = 0; lane < 3; lane++) {
            if (obstacles[i] === lane + 1) dp[lane] = INF;
        }
        // consider side jumps at this position
        for (let lane = 0; lane < 3; lane++) {
            if (dp[lane] !== INF) {
                const otherMin = Math.min(dp[(lane + 1) % 3], dp[(lane + 2) % 3]);
                dp[lane] = Math.min(dp[lane], 1 + otherMin);
            }
        }
    }

    return Math.min(...dp);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $obstacles
     * @return Integer
     */
    function minSideJumps($obstacles) {
        $n = count($obstacles);
        $INF = PHP_INT_MAX;
        // dp[1], dp[2], dp[3] represent lanes 1,2,3 respectively
        $dp = array_fill(0, 4, $INF);
        $dp[1] = 1;   // jump from lane 2 to lane 1 at start if needed later
        $dp[2] = 0;   // starting position
        $dp[3] = 1;   // jump from lane 2 to lane 3 at start if needed later

        for ($i = 1; $i < $n; $i++) {
            $obs = $obstacles[$i];
            // block the lane with an obstacle
            if ($obs != 0) {
                $dp[$obs] = $INF;
            }
            // try to improve each reachable lane by side jumping from other lanes
            for ($lane = 1; $lane <= 3; $lane++) {
                if ($obstacles[$i] == $lane) continue; // cannot stay on blocked lane
                $best = $dp[$lane];
                for ($other = 1; $other <= 3; $other++) {
                    if ($other == $lane) continue;
                    $candidate = $dp[$other] + 1;
                    if ($candidate < $best) {
                        $best = $candidate;
                    }
                }
                $dp[$lane] = $best;
            }
        }

        return min($dp[1], $dp[2], $dp[3]);
    }
}
```

## Swift

```swift
class Solution {
    func minSideJumps(_ obstacles: [Int]) -> Int {
        let INF = Int.max / 4
        var dp = [0, 1, 0, 1]   // index 0 unused; lanes 1..3
        let n = obstacles.count
        for i in 1..<n {
            let obs = obstacles[i]
            if obs != 0 {
                dp[obs] = INF               // lane blocked at this point
            }
            let curMin = min(dp[1], min(dp[2], dp[3]))
            for lane in 1...3 where obstacles[i] != lane {
                dp[lane] = min(dp[lane], curMin + 1)
            }
        }
        return min(dp[1], min(dp[2], dp[3]))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSideJumps(obstacles: IntArray): Int {
        val n = obstacles.size
        val INF = 1_000_000_000
        var dp = IntArray(3)
        dp[0] = 1
        dp[1] = 0
        dp[2] = 1

        for (i in 1 until n) {
            val obs = obstacles[i]
            if (obs != 0) {
                dp[obs - 1] = INF
            }
            var best = INF
            for (v in dp) {
                if (v < best) best = v
            }
            for (lane in 0..2) {
                if (obstacles[i] != lane + 1) {
                    dp[lane] = kotlin.math.min(dp[lane], best + 1)
                }
            }
        }
        return minOf(dp[0], dp[1], dp[2])
    }
}
```

## Dart

```dart
class Solution {
  int minSideJumps(List<int> obstacles) {
    const int INF = 1 << 30;
    // dp[lane] = minimum side jumps to be at current position on that lane
    List<int> dp = List.filled(4, INF);
    dp[1] = 1; // jump from lane 2 to lane 1 at start if needed later
    dp[2] = 0; // starting lane
    dp[3] = 1; // jump from lane 2 to lane 3 at start if needed later

    for (int i = 1; i < obstacles.length; ++i) {
      int obs = obstacles[i];
      if (obs != 0) {
        dp[obs] = INF; // cannot stay on a blocked lane
      }

      // best among reachable lanes at this point
      int best = dp[1];
      if (dp[2] < best) best = dp[2];
      if (dp[3] < best) best = dp[3];

      for (int lane = 1; lane <= 3; ++lane) {
        if (obstacles[i] != lane) {
          int candidate = best + 1;
          if (candidate < dp[lane]) dp[lane] = candidate;
        }
      }
    }

    int ans = dp[1];
    if (dp[2] < ans) ans = dp[2];
    if (dp[3] < ans) ans = dp[3];
    return ans;
  }
}
```

## Golang

```go
func minSideJumps(obstacles []int) int {
	const inf = int(1 << 60)
	// dp[0] for lane 1, dp[1] for lane 2, dp[2] for lane 3
	dp := [3]int{1, 0, 1}
	n := len(obstacles) - 1

	for i := 1; i <= n; i++ {
		obs := obstacles[i]
		// mark impossible lanes at this point
		if obs != 0 {
			dp[obs-1] = inf
		}
		// find minimal jumps among reachable lanes
		minVal := inf
		for j := 0; j < 3; j++ {
			if dp[j] < minVal {
				minVal = dp[j]
			}
		}
		// possibly side‑jump to a better lane at the same point
		for j := 0; j < 3; j++ {
			if obstacles[i] != j+1 && dp[j] > minVal+1 {
				dp[j] = minVal + 1
			}
		}
	}

	// answer is minimal jumps among three lanes at point n
	ans := dp[0]
	if dp[1] < ans {
		ans = dp[1]
	}
	if dp[2] < ans {
		ans = dp[2]
	}
	return ans
}
```

## Ruby

```ruby
def min_side_jumps(obstacles)
  n = obstacles.length - 1
  inf = 1 << 60
  dp = [inf, 1, 0, 1] # lanes are 1-indexed

  (1..n).each do |i|
    blocked = obstacles[i]
    dp[blocked] = inf if blocked != 0

    1.upto(3) do |lane|
      next if lane == blocked
      best = dp[lane]
      1.upto(3) do |other|
        next if other == lane || other == blocked
        cand = dp[other] + 1
        best = cand if cand < best
      end
      dp[lane] = best
    end
  end

  [dp[1], dp[2], dp[3]].min
end
```

## Scala

```scala
object Solution {
    def minSideJumps(obstacles: Array[Int]): Int = {
        val n = obstacles.length
        val INF = 1000000000
        val dp = new Array[Int](4) // indices 1..3

        dp(1) = 1
        dp(2) = 0
        dp(3) = 1

        for (i <- 1 until n) {
            // block lanes with an obstacle at position i
            for (lane <- 1 to 3) {
                if (obstacles(i) == lane) dp(lane) = INF
            }
            // find the minimal jumps among reachable lanes
            var best = INF
            for (lane <- 1 to 3) {
                if (dp(lane) < best) best = dp(lane)
            }
            // possibly side jump to any other lane at this point
            for (lane <- 1 to 3) {
                if (obstacles(i) != lane) {
                    dp(lane) = Math.min(dp(lane), best + 1)
                }
            }
        }

        var answer = INF
        for (lane <- 1 to 3) {
            if (dp(lane) < answer) answer = dp(lane)
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_side_jumps(obstacles: Vec<i32>) -> i32 {
        const INF: i32 = 1_000_000_000;
        let n = obstacles.len();
        // dp[lane] = minimum side jumps to be at current position on lane (0-indexed lanes)
        let mut dp = vec![INF; 3];
        dp[0] = 1; // need one jump from lane 2 to lane 1 at start
        dp[1] = 0; // start lane
        dp[2] = 1; // need one jump from lane 2 to lane 3 at start

        for i in 1..n {
            let obs = obstacles[i] as usize;
            if obs != 0 {
                dp[obs - 1] = INF; // cannot stay on blocked lane
            }
            // find the best (minimum) jumps among lanes not blocked at this position
            let mut best = INF;
            for lane in 0..3 {
                if obstacles[i] as usize != lane + 1 && dp[lane] < best {
                    best = dp[lane];
                }
            }
            // possibly jump from the best lane to others at the same point
            for lane in 0..3 {
                if obstacles[i] as usize != lane + 1 {
                    dp[lane] = dp[lane].min(best + 1);
                }
            }
        }

        *dp.iter().min().unwrap()
    }
}
```

## Racket

```racket
(define/contract (min-side-jumps obstacles)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((obs-vec (list->vector obstacles))
         (len (vector-length obs-vec))
         (INF (+ len 5))
         (dp (vector 1 0 1))) ; lanes 1,2,3 correspond to indices 0,1,2
    (for ([i (in-range 1 len)])
      (let ((obs (vector-ref obs-vec i)))
        (cond [(= obs 1) (vector-set! dp 0 INF)]
              [(= obs 2) (vector-set! dp 1 INF)]
              [(= obs 3) (vector-set! dp 2 INF)]))
      (define d0 (vector-ref dp 0))
      (define d1 (vector-ref dp 1))
      (define d2 (vector-ref dp 2))
      (let ((obs (vector-ref obs-vec i)))
        (when (not (= obs 1))
          (vector-set! dp 0 (min d0 (+ (min d1 d2) 1))))
        (when (not (= obs 2))
          (vector-set! dp 1 (min d1 (+ (min d0 d2) 1))))
        (when (not (= obs 3))
          (vector-set! dp 2 (min d2 (+ (min d0 d1) 1))))))
    (apply min (vector->list dp))))
```

## Erlang

```erlang
-module(solution).
-export([min_side_jumps/1]).

-define(INF, 1000000000).

-spec min_side_jumps(Obstacles :: [integer()]) -> integer().
min_side_jumps(Obstacles) ->
    [_Zero | Rest] = Obstacles,
    InitialDP = {1, 0, 1},
    FinalDP = go(Rest, InitialDP),
    min3(FinalDP).

go([], DP) ->
    DP;
go([Obs | Tail], {A, B, C}) ->
    % block lanes with obstacle at current point
    A1 = if Obs == 1 -> ?INF; true -> A end,
    B1 = if Obs == 2 -> ?INF; true -> B end,
    C1 = if Obs == 3 -> ?INF; true -> C end,
    MinVal = erlang:min(A1, erlang:min(B1, C1)),
    % consider side jumps at this point
    NewA = if Obs == 1 -> A1; true -> erlang:min(A1, 1 + MinVal) end,
    NewB = if Obs == 2 -> B1; true -> erlang:min(B1, 1 + MinVal) end,
    NewC = if Obs == 3 -> C1; true -> erlang:min(C1, 1 + MinVal) end,
    go(Tail, {NewA, NewB, NewC}).

min3({X, Y, Z}) ->
    erlang:min(X, erlang:min(Y, Z)).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_side_jumps(obstacles :: [integer]) :: integer
  def min_side_jumps(obstacles) do
    inf = 1_000_000_000
    # initial dp for lanes 1,2,3 at position 0 (starting in lane 2)
    dp = [1, 0, 1]
    process(tl(obstacles), dp, inf)
  end

  defp process([], dp, _inf), do: Enum.min(dp)

  defp process([obs | rest], dp, inf) do
    # block the lane with an obstacle at current position
    dp_blocked =
      case obs do
        0 -> dp
        lane when lane in [1, 2, 3] -> List.replace_at(dp, lane - 1, inf)
      end

    best = Enum.min(dp_blocked)

    # consider side jumps to any unblocked lane at this position
    dp_updated =
      for {val, idx} <- Enum.with_index(dp_blocked), into: [] do
        if obs == idx + 1 do
          inf
        else
          min(val, best + 1)
        end
      end

    process(rest, dp_updated, inf)
  end
end
```

# 2585. Number of Ways to Earn Points

## Cpp

```cpp
class Solution {
public:
    int waysToReachTarget(int target, vector<vector<int>>& types) {
        const int MOD = 1'000'000'007;
        vector<int> dp(target + 1, 0);
        dp[0] = 1;
        for (const auto& t : types) {
            int cnt = t[0];
            int mark = t[1];
            vector<int> ndp(target + 1, 0);
            for (int cur = 0; cur <= target; ++cur) {
                if (!dp[cur]) continue;
                long long ways = dp[cur];
                for (int k = 0; k <= cnt && cur + k * mark <= target; ++k) {
                    int nxt = cur + k * mark;
                    ndp[nxt] += ways;
                    if (ndp[nxt] >= MOD) ndp[nxt] -= MOD;
                }
            }
            dp.swap(ndp);
        }
        return dp[target];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int waysToReachTarget(int target, int[][] types) {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int[] type : types) {
            int cnt = type[0];
            int mark = type[1];
            int[] ndp = new int[target + 1];
            for (int cur = 0; cur <= target; ++cur) {
                if (dp[cur] == 0) continue;
                long ways = dp[cur];
                for (int k = 0, sum = cur; k <= cnt && sum <= target; ++k, sum += mark) {
                    ndp[sum] = (int)((ndp[sum] + ways) % MOD);
                }
            }
            dp = ndp;
        }
        return dp[target];
    }
}
```

## Python

```python
class Solution(object):
    def waysToReachTarget(self, target, types):
        """
        :type target: int
        :type types: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for count, marks in types:
            ndp = [0] * (target + 1)
            for cur in range(target + 1):
                if dp[cur] == 0:
                    continue
                max_k = min(count, (target - cur) // marks)
                val = dp[cur]
                for k in range(max_k + 1):
                    ndp[cur + k * marks] = (ndp[cur + k * marks] + val) % MOD
            dp = ndp
        return dp[target]
```

## Python3

```python
from typing import List

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for count, mark in types:
            ndp = [0] * (target + 1)
            for cur in range(target + 1):
                if dp[cur] == 0:
                    continue
                max_k = min(count, (target - cur) // mark)
                add = dp[cur]
                for k in range(max_k + 1):
                    ndp[cur + k * mark] = (ndp[cur + k * mark] + add) % MOD
            dp = ndp
        return dp[target]
```

## C

```c
#include <stdlib.h>

int waysToReachTarget(int target, int** types, int typesSize, int* typesColSize) {
    const int MOD = 1000000007;
    int *dp = (int *)calloc(target + 1, sizeof(int));
    dp[0] = 1;

    for (int i = 0; i < typesSize; ++i) {
        int cnt = types[i][0];
        int mark = types[i][1];

        int *ndp = (int *)calloc(target + 1, sizeof(int));

        for (int cur = 0; cur <= target; ++cur) {
            if (!dp[cur]) continue;
            long long ways = dp[cur];
            for (int k = 0; k <= cnt; ++k) {
                int nxt = cur + k * mark;
                if (nxt > target) break;
                ndp[nxt] += ways;
                if (ndp[nxt] >= MOD) ndp[nxt] -= MOD;
            }
        }

        free(dp);
        dp = ndp;
    }

    int result = dp[target];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int WaysToReachTarget(int target, int[][] types) {
        const int MOD = 1000000007;
        long[] dp = new long[target + 1];
        dp[0] = 1;
        foreach (var type in types) {
            int count = type[0];
            int marks = type[1];
            long[] ndp = new long[target + 1];
            for (int pts = 0; pts <= target; ++pts) {
                if (dp[pts] == 0) continue;
                for (int k = 0; k <= count && pts + k * marks <= target; ++k) {
                    int nxt = pts + k * marks;
                    ndp[nxt] += dp[pts];
                    if (ndp[nxt] >= MOD) ndp[nxt] -= MOD;
                }
            }
            dp = ndp;
        }
        return (int)(dp[target] % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} target
 * @param {number[][]} types
 * @return {number}
 */
var waysToReachTarget = function(target, types) {
    const MOD = 1000000007;
    let dp = new Array(target + 1).fill(0);
    dp[0] = 1;
    for (const [cnt, mark] of types) {
        const ndp = new Array(target + 1).fill(0);
        for (let s = 0; s <= target; ++s) {
            if (dp[s] === 0) continue;
            const maxK = Math.min(cnt, Math.floor((target - s) / mark));
            for (let k = 0; k <= maxK; ++k) {
                const ns = s + k * mark;
                ndp[ns] = (ndp[ns] + dp[s]) % MOD;
            }
        }
        dp = ndp;
    }
    return dp[target];
};
```

## Typescript

```typescript
function waysToReachTarget(target: number, types: number[][]): number {
    const MOD = 1_000_000_007;
    let dp: number[] = new Array(target + 1).fill(0);
    dp[0] = 1;

    for (const [cnt, mark] of types) {
        const ndp: number[] = new Array(target + 1).fill(0);
        for (let cur = 0; cur <= target; ++cur) {
            const ways = dp[cur];
            if (ways === 0) continue;
            const maxK = Math.min(cnt, Math.floor((target - cur) / mark));
            for (let k = 0; k <= maxK; ++k) {
                const nxt = cur + k * mark;
                ndp[nxt] = (ndp[nxt] + ways) % MOD;
            }
        }
        dp = ndp;
    }

    return dp[target];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer[][] $types
     * @return Integer
     */
    function waysToReachTarget($target, $types) {
        $mod = 1000000007;
        $dp = array_fill(0, $target + 1, 0);
        $dp[0] = 1;

        foreach ($types as $type) {
            [$cnt, $mark] = $type;
            $new = array_fill(0, $target + 1, 0);
            for ($p = 0; $p <= $target; $p++) {
                if ($dp[$p] == 0) continue;
                for ($k = 0; $k <= $cnt && $p + $k * $mark <= $target; $k++) {
                    $idx = $p + $k * $mark;
                    $new[$idx] = ($new[$idx] + $dp[$p]) % $mod;
                }
            }
            $dp = $new;
        }

        return $dp[$target];
    }
}
```

## Swift

```swift
class Solution {
    func waysToReachTarget(_ target: Int, _ types: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        var dp = [Int](repeating: 0, count: target + 1)
        dp[0] = 1
        
        for type in types {
            let cnt = type[0]
            let mark = type[1]
            var newDP = [Int](repeating: 0, count: target + 1)
            
            for tPrev in 0...target {
                let cur = dp[tPrev]
                if cur == 0 { continue }
                var k = 0
                while k <= cnt && tPrev + k * mark <= target {
                    let nt = tPrev + k * mark
                    newDP[nt] += cur
                    if newDP[nt] >= MOD { newDP[nt] -= MOD }
                    k += 1
                }
            }
            dp = newDP
        }
        
        return dp[target]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun waysToReachTarget(target: Int, types: Array<IntArray>): Int {
        val MOD = 1_000_000_007L
        var dp = LongArray(target + 1)
        dp[0] = 1L
        for (type in types) {
            val count = type[0]
            val marks = type[1]
            val ndp = LongArray(target + 1)
            for (points in 0..target) {
                val ways = dp[points]
                if (ways == 0L) continue
                var cur = points
                for (k in 0..count) {
                    if (cur > target) break
                    ndp[cur] = (ndp[cur] + ways) % MOD
                    cur += marks
                }
            }
            dp = ndp
        }
        return dp[target].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int waysToReachTarget(int target, List<List<int>> types) {
    List<int> dp = List.filled(target + 1, 0);
    dp[0] = 1;
    for (var t in types) {
      int count = t[0];
      int marks = t[1];
      List<int> ndp = List.filled(target + 1, 0);
      for (int cur = 0; cur <= target; ++cur) {
        if (dp[cur] == 0) continue;
        for (int k = 0; k <= count && cur + k * marks <= target; ++k) {
          int nxt = cur + k * marks;
          ndp[nxt] = (ndp[nxt] + dp[cur]) % _mod;
        }
      }
      dp = ndp;
    }
    return dp[target];
  }
}
```

## Golang

```go
func waysToReachTarget(target int, types [][]int) int {
	const MOD = 1000000007
	dp := make([]int, target+1)
	dp[0] = 1

	for _, t := range types {
		cnt, mark := t[0], t[1]
		next := make([]int, target+1)

		for pts := 0; pts <= target; pts++ {
			if dp[pts] == 0 {
				continue
			}
			for k := 0; k <= cnt && pts+k*mark <= target; k++ {
				nxt := pts + k*mark
				next[nxt] += dp[pts]
				if next[nxt] >= MOD {
					next[nxt] -= MOD
				}
			}
		}
		dp = next
	}

	return dp[target]
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def ways_to_reach_target(target, types)
  dp = Array.new(target + 1, 0)
  dp[0] = 1
  types.each do |cnt, mark|
    ndp = Array.new(target + 1, 0)
    (0..target).each do |pts|
      val = dp[pts]
      next if val == 0
      max_k = [cnt, (target - pts) / mark].min
      k = 0
      while k <= max_k
        new_pts = pts + k * mark
        ndp[new_pts] = (ndp[new_pts] + val) % MOD
        k += 1
      end
    end
    dp = ndp
  end
  dp[target]
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007

    def waysToReachTarget(target: Int, types: Array[Array[Int]]): Int = {
        var dp = new Array[Int](target + 1)
        dp(0) = 1
        for (t <- types) {
            val count = t(0)
            val mark = t(1)
            val ndp = new Array[Int](target + 1)
            for (points <- 0 to target) {
                val curWays = dp(points)
                if (curWays != 0) {
                    var k = 0
                    var sumPoints = points
                    while (k <= count && sumPoints <= target) {
                        val newVal = (ndp(sumPoints).toLong + curWays) % MOD
                        ndp(sumPoints) = newVal.toInt
                        k += 1
                        sumPoints += mark
                    }
                }
            }
            dp = ndp
        }
        dp(target)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn ways_to_reach_target(target: i32, types: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let target_usize = target as usize;
        let mut dp = vec![0i64; target_usize + 1];
        dp[0] = 1;
        for typ in types.iter() {
            let count = typ[0] as usize;
            let mark = typ[1] as usize;
            let mut ndp = vec![0i64; target_usize + 1];
            for pts in 0..=target_usize {
                if dp[pts] == 0 {
                    continue;
                }
                let max_k = ((target_usize - pts) / mark).min(count);
                for k in 0..=max_k {
                    let new_pts = pts + k * mark;
                    ndp[new_pts] = (ndp[new_pts] + dp[pts]) % MOD;
                }
            }
            dp = ndp;
        }
        dp[target_usize] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (ways-to-reach-target target types)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((dp (make-vector (+ target 1) 0))
         (_   (vector-set! dp 0 1)))
    (for ([type types])
      (define cnt  (first type))
      (define mark (second type))
      (define ndp (make-vector (+ target 1) 0))
      (for ([points (in-range 0 (+ target 1))])
        (let ((cur (vector-ref dp points)))
          (when (> cur 0)
            (for ([k (in-range 0 (+ cnt 1))])
              (define newp (+ points (* k mark)))
              (when (<= newp target)
                (define prev (vector-ref ndp newp))
                (vector-set! ndp newp (modulo (+ prev cur) MOD)))))))
      (set! dp ndp))
    (vector-ref dp target)))
```

## Erlang

```erlang
-module(solution).
-export([ways_to_reach_target/2]).

-define(MOD, 1000000007).

ways_to_reach_target(Target, Types) ->
    InitialMap = #{0 => 1},
    FinalMap = lists:foldl(fun([Count, Marks], AccMap) ->
        process_type(AccMap, Count, Marks, Target)
    end, InitialMap, Types),
    maps:get(Target, FinalMap, 0).

process_type(Map, Count, Marks, Target) ->
    lists:foldl(fun({Points, Ways}, AccMap) ->
        MaxK = erlang:min(Count, (Target - Points) div Marks),
        add_k(0, MaxK, Points, Ways, Marks, AccMap)
    end, #{}, maps:to_list(Map)).

add_k(K, MaxK, Base, Ways, Marks, Map) when K =< MaxK ->
    NewPoint = Base + K * Marks,
    Cur = maps:get(NewPoint, Map, 0),
    NewVal = (Cur + Ways) rem ?MOD,
    add_k(K + 1, MaxK, Base, Ways, Marks, maps:put(NewPoint, NewVal, Map));
add_k(_, _, _, _, _, Map) ->
    Map.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec ways_to_reach_target(target :: integer, types :: [[integer]]) :: integer
  def ways_to_reach_target(target, types) do
    mod = 1_000_000_007

    # dp[points] = number of ways using processed types
    dp0 = :array.new(target + 1, default: 0)
    dp0 = :array.set(0, 1, dp0)

    final_dp =
      Enum.reduce(types, dp0, fn [cnt, mark], dp ->
        ndp = :array.new(target + 1, default: 0)

        ndp =
          Enum.reduce(0..target, ndp, fn points, acc_ndp ->
            ways = :array.get(points, dp)

            if ways == 0 do
              acc_ndp
            else
              max_k = min(cnt, div(target - points, mark))

              Enum.reduce(0..max_k, acc_ndp, fn k, a ->
                new_points = points + k * mark
                cur = :array.get(new_points, a)
                new_val = rem(cur + ways, mod)
                :array.set(new_points, new_val, a)
              end)
            end
          end)

        ndp
      end)

    :array.get(target, final_dp)
  end
end
```

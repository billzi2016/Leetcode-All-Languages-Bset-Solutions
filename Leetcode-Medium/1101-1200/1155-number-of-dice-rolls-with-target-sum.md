# 1155. Number of Dice Rolls With Target Sum

## Cpp

```cpp
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        static const int MOD = 1000000007;
        vector<int> dp(target + 1, 0);
        dp[0] = 1;
        for (int dice = 1; dice <= n; ++dice) {
            vector<int> ndp(target + 1, 0);
            for (int t = 1; t <= target; ++t) {
                long long ways = 0;
                int maxFace = min(k, t);
                for (int face = 1; face <= maxFace; ++face) {
                    ways += dp[t - face];
                }
                ndp[t] = ways % MOD;
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
    
    public int numRollsToTarget(int n, int k, int target) {
        if (target > n * k) return 0;
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int dice = 1; dice <= n; dice++) {
            int[] ndp = new int[target + 1];
            for (int sum = 1; sum <= target; sum++) {
                long ways = 0;
                int maxFace = Math.min(k, sum);
                for (int face = 1; face <= maxFace; face++) {
                    ways += dp[sum - face];
                }
                ndp[sum] = (int) (ways % MOD);
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
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            ndp = [0] * (target + 1)
            for s in range(1, target + 1):
                # sum contributions from previous dice
                lo = max(0, s - k)
                total = 0
                for prev in range(lo, s):
                    total += dp[prev]
                ndp[s] = total % MOD
            dp = ndp
        return dp[target]
```

## Python3

```python
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            ndp = [0] * (target + 1)
            for t in range(1, target + 1):
                total = 0
                # sum over possible face values
                upper = min(k, t)
                for f in range(1, upper + 1):
                    total += dp[t - f]
                ndp[t] = total % MOD
            dp = ndp
        return dp[target]
```

## C

```c
#include <string.h>

int numRollsToTarget(int n, int k, int target) {
    const int MOD = 1000000007;
    if (target > n * k) return 0;
    static int dp[31][1001];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int t = 1; t <= target; ++t) {
            long long sum = 0;
            int maxFace = k < t ? k : t;
            for (int f = 1; f <= maxFace; ++f) {
                sum += dp[i - 1][t - f];
            }
            dp[i][t] = sum % MOD;
        }
    }
    return dp[n][target];
}
```

## Csharp

```csharp
public class Solution {
    public int NumRollsToTarget(int n, int k, int target) {
        const int MOD = 1_000_000_007;
        var dp = new int[target + 1];
        dp[0] = 1;
        for (int dice = 1; dice <= n; dice++) {
            var ndp = new int[target + 1];
            for (int sum = 1; sum <= target; sum++) {
                long ways = 0;
                int maxFace = Math.Min(k, sum);
                for (int face = 1; face <= maxFace; face++) {
                    ways += dp[sum - face];
                }
                ndp[sum] = (int)(ways % MOD);
            }
            dp = ndp;
        }
        return dp[target];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function(n, k, target) {
    const MOD = 1000000007;
    if (target > n * k || target < n) return 0;
    let dp = new Array(target + 1).fill(0);
    dp[0] = 1;
    for (let i = 1; i <= n; i++) {
        const next = new Array(target + 1).fill(0);
        for (let s = 1; s <= target; s++) {
            let sum = 0;
            const maxFace = Math.min(k, s);
            for (let f = 1; f <= maxFace; f++) {
                sum += dp[s - f];
                if (sum >= MOD) sum -= MOD;
            }
            next[s] = sum;
        }
        dp = next;
    }
    return dp[target];
};
```

## Typescript

```typescript
function numRollsToTarget(n: number, k: number, target: number): number {
    const MOD = 1_000_000_007;
    if (target > n * k) return 0;

    let dp = new Array(target + 1).fill(0);
    dp[0] = 1;

    for (let dice = 1; dice <= n; dice++) {
        const ndp = new Array(target + 1).fill(0);
        for (let sum = 1; sum <= target; sum++) {
            let ways = 0;
            const maxFace = Math.min(k, sum);
            for (let face = 1; face <= maxFace; face++) {
                ways += dp[sum - face];
                if (ways >= MOD) ways -= MOD;
            }
            ndp[sum] = ways;
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
     * @param Integer $n
     * @param Integer $k
     * @param Integer $target
     * @return Integer
     */
    function numRollsToTarget($n, $k, $target) {
        $MOD = 1000000007;
        $dp = array_fill(0, $target + 1, 0);
        $dp[0] = 1;

        for ($i = 1; $i <= $n; $i++) {
            $new = array_fill(0, $target + 1, 0);
            for ($s = 1; $s <= $target; $s++) {
                $maxFace = min($k, $s);
                $sum = 0;
                for ($face = 1; $face <= $maxFace; $face++) {
                    $sum += $dp[$s - $face];
                    if ($sum >= $MOD) {
                        $sum -= $MOD;
                    }
                }
                $new[$s] = $sum % $MOD;
            }
            $dp = $new;
        }

        return $dp[$target] % $MOD;
    }
}
```

## Swift

```swift
class Solution {
    func numRollsToTarget(_ n: Int, _ k: Int, _ target: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: 0, count: target + 1)
        dp[0] = 1
        for _ in 1...n {
            var ndp = Array(repeating: 0, count: target + 1)
            for sum in 0...target {
                let cur = dp[sum]
                if cur == 0 { continue }
                var face = 1
                while face <= k && sum + face <= target {
                    ndp[sum + face] = (ndp[sum + face] + cur) % MOD
                    face += 1
                }
            }
            dp = ndp
        }
        return dp[target]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numRollsToTarget(n: Int, k: Int, target: Int): Int {
        val MOD = 1_000_000_007L
        var dp = LongArray(target + 1)
        dp[0] = 1L
        for (i in 1..n) {
            val ndp = LongArray(target + 1)
            for (s in 1..target) {
                var ways = 0L
                for (f in 1..k) {
                    if (s - f >= 0) {
                        ways += dp[s - f]
                        if (ways >= MOD) ways -= MOD
                    }
                }
                ndp[s] = ways % MOD
            }
            dp = ndp
        }
        return (dp[target] % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;
  int numRollsToTarget(int n, int k, int target) {
    List<int> dp = List.filled(target + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
      List<int> ndp = List.filled(target + 1, 0);
      for (int t = 1; t <= target; t++) {
        int sum = 0;
        int maxFace = k < t ? k : t;
        for (int f = 1; f <= maxFace; f++) {
          sum += dp[t - f];
          if (sum >= _mod) sum -= _mod;
        }
        ndp[t] = sum;
      }
      dp = ndp;
    }
    return dp[target];
  }
}
```

## Golang

```go
func numRollsToTarget(n int, k int, target int) int {
	const MOD = 1000000007
	dp := make([]int, target+1)
	dp[0] = 1

	for i := 1; i <= n; i++ {
		next := make([]int, target+1)
		for t := 1; t <= target; t++ {
			sum := 0
			limit := k
			if limit > t {
				limit = t
			}
			for f := 1; f <= limit; f++ {
				sum += dp[t-f]
				if sum >= MOD {
					sum -= MOD
				}
			}
			next[t] = sum
		}
		dp = next
	}
	return dp[target]
}
```

## Ruby

```ruby
def num_rolls_to_target(n, k, target)
  mod = 1_000_000_007
  dp = Array.new(target + 1, 0)
  dp[0] = 1

  n.times do
    ndp = Array.new(target + 1, 0)
    (1..target).each do |s|
      max_face = [k, s].min
      1.upto(max_face) do |f|
        ndp[s] += dp[s - f]
        ndp[s] -= mod if ndp[s] >= mod
      end
    end
    dp = ndp
  end

  dp[target] % mod
end
```

## Scala

```scala
object Solution {
    def numRollsToTarget(n: Int, k: Int, target: Int): Int = {
        val MOD = 1000000007
        var dpPrev = new Array[Int](target + 1)
        dpPrev(0) = 1
        for (_ <- 1 to n) {
            val dpCurr = new Array[Int](target + 1)
            for (t <- 1 to target) {
                var sum: Long = 0L
                var face = 1
                while (face <= k && face <= t) {
                    sum += dpPrev(t - face)
                    if (sum >= MOD) sum -= MOD
                    face += 1
                }
                dpCurr(t) = (sum % MOD).toInt
            }
            dpPrev = dpCurr
        }
        dpPrev(target)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_rolls_to_target(n: i32, k: i32, target: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let target = target as usize;
        const MOD: i64 = 1_000_000_007;
        let mut dp = vec![0i64; target + 1];
        dp[0] = 1;
        for _ in 0..n {
            let mut ndp = vec![0i64; target + 1];
            for sum in 0..=target {
                if dp[sum] == 0 {
                    continue;
                }
                for face in 1..=k {
                    let ns = sum + face;
                    if ns > target {
                        break;
                    }
                    ndp[ns] = (ndp[ns] + dp[sum]) % MOD;
                }
            }
            dp = ndp;
        }
        dp[target] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-rolls-to-target n k target)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let ((dp (make-vector (+ target 1) 0)))
    (vector-set! dp 0 1)
    (for ([i (in-range n)])
      (let ((next (make-vector (+ target 1) 0)))
        (for ([s (in-range 1 (+ target 1))])
          (let ((total 0))
            (for ([face (in-range 1 (+ k 1))])
              (define prev (- s face))
              (when (>= prev 0)
                (set! total (modulo (+ total (vector-ref dp prev)) MOD))))
            (vector-set! next s total)))
        (set! dp next)))
    (vector-ref dp target)))
```

## Erlang

```erlang
-spec num_rolls_to_target(N :: integer(), K :: integer(), Target :: integer()) -> integer().
num_rolls_to_target(N, K, Target) ->
    Mod = 1000000007,
    DP0 = #{0 => 1},
    DPFinal = lists:foldl(
        fun(_Idx, DPPrev) ->
            maps:fold(
                fun(Sum, Ways, Acc) ->
                    add_faces(Sum, Ways, K, Target, Mod, Acc)
                end,
                #{},
                DPPrev
            )
        end,
        DP0,
        lists:seq(1, N)
    ),
    maps:get(Target, DPFinal, 0).

add_faces(Sum, Ways, K, Target, Mod, Acc) ->
    lists:foldl(
        fun(Face, A) ->
            NewSum = Sum + Face,
            if
                NewSum =< Target ->
                    Old = maps:get(NewSum, A, 0),
                    NewVal = (Old + Ways) rem Mod,
                    maps:put(NewSum, NewVal, A);
                true ->
                    A
            end
        end,
        Acc,
        lists:seq(1, K)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec num_rolls_to_target(n :: integer, k :: integer, target :: integer) :: integer
  def num_rolls_to_target(n, k, target) do
    # Quick impossibility check
    if target < n or target > n * k do
      0
    else
      # dp for 0 dice: only sum 0 is possible
      init_dp = List.duplicate(0, target + 1)
      init_dp = List.replace_at(init_dp, 0, 1)

      final_dp =
        Enum.reduce(1..n, init_dp, fn _dice_idx, dp ->
          for sum <- 0..target do
            Enum.reduce(1..k, 0, fn face, acc ->
              if sum - face >= 0 do
                rem(acc + Enum.at(dp, sum - face), @mod)
              else
                acc
              end
            end)
          end
        end)

      Enum.at(final_dp, target)
    end
  end
end
```

# 0920. Number of Music Playlists

## Cpp

```cpp
class Solution {
public:
    int numMusicPlaylists(int n, int goal, int k) {
        const int MOD = 1000000007;
        vector<vector<long long>> dp(goal + 1, vector<long long>(n + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= goal; ++i) {
            for (int j = 1; j <= min(i, n); ++j) {
                // add a new unique song
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (n - j + 1)) % MOD;
                // replay an old song if possible
                if (j > k) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD;
                }
            }
        }
        return (int)dp[goal][n];
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    
    public int numMusicPlaylists(int n, int goal, int k) {
        long[][] dp = new long[goal + 1][n + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= goal; i++) {
            int maxJ = Math.min(i, n);
            for (int j = 1; j <= maxJ; j++) {
                // add a new unique song
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (n - j + 1)) % MOD;
                // replay an old song if allowed
                if (j > k) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD;
                }
            }
        }
        return (int) dp[goal][n];
    }
}
```

## Python

```python
class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            max_j = min(i, n)
            for j in range(1, max_j + 1):
                # add a new unique song
                dp[i][j] = (dp[i - 1][j - 1] * (n - j + 1)) % MOD
                # replay an old song if possible
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD
        return dp[goal][n]
```

## Python3

```python
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            max_j = min(i, n)
            for j in range(1, max_j + 1):
                # add a new unique song
                dp[i][j] = (dp[i - 1][j - 1] * (n - j + 1)) % MOD
                # replay an old song if possible
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD
        return dp[goal][n]
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const int MOD = 1000000007;

int numMusicPlaylists(int n, int goal, int k) {
    static long long dp[101][101];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int i = 1; i <= goal; ++i) {
        int maxj = min(i, n);
        for (int j = 1; j <= maxj; ++j) {
            // add a new unique song
            dp[i][j] = (dp[i-1][j-1] * (n - (j - 1))) % MOD;
            // replay an old song if possible
            if (j > k) {
                dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - k)) % MOD;
            }
        }
    }
    return (int)dp[goal][n];
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;

    public int NumMusicPlaylists(int n, int goal, int k)
    {
        long[,] dp = new long[goal + 1, n + 1];
        dp[0, 0] = 1;
        for (int i = 1; i <= goal; i++)
        {
            int maxJ = Math.Min(i, n);
            for (int j = 1; j <= maxJ; j++)
            {
                dp[i, j] = (dp[i - 1, j - 1] * (n - j + 1)) % MOD;
                if (j > k)
                {
                    dp[i, j] = (dp[i, j] + dp[i - 1, j] * (j - k)) % MOD;
                }
            }
        }
        return (int)(dp[goal, n] % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} goal
 * @param {number} k
 * @return {number}
 */
var numMusicPlaylists = function(n, goal, k) {
    const MOD = 1000000007n;
    // dp[i][j]: length i playlist with j unique songs
    const dp = Array.from({length: goal + 1}, () => Array(n + 1).fill(0n));
    dp[0][0] = 1n;

    for (let i = 1; i <= goal; ++i) {
        const maxJ = Math.min(i, n);
        for (let j = 1; j <= maxJ; ++j) {
            // add a new unique song
            let val = dp[i - 1][j - 1] * BigInt(n - j + 1);
            // replay an old song if possible
            if (j > k) {
                val += dp[i - 1][j] * BigInt(j - k);
            }
            dp[i][j] = val % MOD;
        }
    }

    return Number(dp[goal][n]);
};
```

## Typescript

```typescript
function numMusicPlaylists(n: number, goal: number, k: number): number {
    const MOD = 1000000007n;
    const dp: bigint[][] = Array.from({ length: goal + 1 }, () => new Array<bigint>(n + 1).fill(0n));
    dp[0][0] = 1n;

    for (let i = 1; i <= goal; i++) {
        const maxJ = Math.min(i, n);
        for (let j = 1; j <= maxJ; j++) {
            // Add a new unique song
            dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * BigInt(n - j + 1)) % MOD;
            // Replay an old song if allowed
            if (j > k) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j] * BigInt(j - k)) % MOD;
            }
        }
    }

    return Number(dp[goal][n]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $goal
     * @param Integer $k
     * @return Integer
     */
    function numMusicPlaylists($n, $goal, $k) {
        $mod = 1000000007;
        // dp[i][j]: playlists of length i with j unique songs
        $dp = array_fill(0, $goal + 1, array_fill(0, $n + 1, 0));
        $dp[0][0] = 1;

        for ($i = 1; $i <= $goal; $i++) {
            $maxJ = min($i, $n);
            for ($j = 1; $j <= $maxJ; $j++) {
                // Add a new unique song
                $addNew = ($dp[$i - 1][$j - 1] * ($n - $j + 1)) % $mod;
                $dp[$i][$j] = $addNew;

                // Replay an old song if possible
                if ($j > $k) {
                    $replay = ($dp[$i - 1][$j] * ($j - $k)) % $mod;
                    $dp[$i][$j] = ($dp[$i][$j] + $replay) % $mod;
                }
            }
        }

        return (int)$dp[$goal][$n];
    }
}
```

## Swift

```swift
class Solution {
    func numMusicPlaylists(_ n: Int, _ goal: Int, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: goal + 1)
        dp[0][0] = 1
        if goal == 0 { return 0 }
        for i in 1...goal {
            let maxJ = min(i, n)
            for j in 1...maxJ {
                var ways = (dp[i - 1][j - 1] * (n - j + 1)) % MOD
                if j > k {
                    ways = (ways + dp[i - 1][j] * (j - k) % MOD) % MOD
                }
                dp[i][j] = ways
            }
        }
        return dp[goal][n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numMusicPlaylists(n: Int, goal: Int, k: Int): Int {
        val MOD = 1_000_000_007L
        val dp = Array(goal + 1) { LongArray(n + 1) }
        dp[0][0] = 1L
        for (i in 1..goal) {
            val maxJ = minOf(i, n)
            for (j in 1..maxJ) {
                // Add a new unique song
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (n - j + 1)) % MOD
                // Replay an old song if allowed
                if (j > k) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD
                }
            }
        }
        return dp[goal][n].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numMusicPlaylists(int n, int goal, int k) {
    List<List<int>> dp = List.generate(goal + 1, (_) => List.filled(n + 1, 0));
    dp[0][0] = 1;
    for (int i = 1; i <= goal; ++i) {
      int maxJ = i < n ? i : n;
      for (int j = 1; j <= maxJ; ++j) {
        // Add a new unique song
        dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (n - j + 1)) % _mod;
        // Replay an old song if allowed
        if (j > k) {
          dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % _mod;
        }
      }
    }
    return dp[goal][n];
  }
}
```

## Golang

```go
const mod int64 = 1000000007

func numMusicPlaylists(n int, goal int, k int) int {
    dp := make([][]int64, goal+1)
    for i := 0; i <= goal; i++ {
        dp[i] = make([]int64, n+1)
    }
    dp[0][0] = 1
    for i := 1; i <= goal; i++ {
        maxJ := n
        if i < maxJ {
            maxJ = i
        }
        for j := 1; j <= maxJ; j++ {
            // add a new unique song
            dp[i][j] = (dp[i][j] + dp[i-1][j-1]*int64(n-j+1)) % mod
            // replay an old song if allowed
            if j > k {
                dp[i][j] = (dp[i][j] + dp[i-1][j]*int64(j-k)) % mod
            }
        }
    }
    return int(dp[goal][n])
}
```

## Ruby

```ruby
def num_music_playlists(n, goal, k)
  mod = 1_000_000_007
  dp = Array.new(goal + 1) { Array.new(n + 1, 0) }
  dp[0][0] = 1

  (1..goal).each do |i|
    max_j = [i, n].min
    (1..max_j).each do |j|
      # add a new unique song
      dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (n - j + 1)) % mod
      # replay an old song if allowed
      if j > k
        dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod
      end
    end
  end

  dp[goal][n] % mod
end
```

## Scala

```scala
object Solution {
  def numMusicPlaylists(n: Int, goal: Int, k: Int): Int = {
    val MOD = 1000000007L
    val dp = Array.ofDim[Long](goal + 1, n + 1)
    dp(0)(0) = 1L
    for (i <- 1 to goal) {
      val maxJ = math.min(i, n)
      for (j <- 1 to maxJ) {
        // add a new unique song
        var ways = dp(i - 1)(j - 1) * (n - j + 1)
        ways %= MOD
        // replay an old song if possible
        if (j > k) {
          ways += dp(i - 1)(j) * (j - k)
          ways %= MOD
        }
        dp(i)(j) = ways
      }
    }
    dp(goal)(n).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn num_music_playlists(n: i32, goal: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n_usize = n as usize;
        let goal_usize = goal as usize;
        let k_usize = k as usize;

        // dp[i][j]: number of playlists of length i with exactly j unique songs
        let mut dp = vec![vec![0i64; n_usize + 1]; goal_usize + 1];
        dp[0][0] = 1;

        for i in 1..=goal_usize {
            let max_j = std::cmp::min(i, n_usize);
            for j in 1..=max_j {
                // Add a new unique song
                let add_new = dp[i - 1][j - 1] * (n - (j as i32) + 1) as i64;
                dp[i][j] = (dp[i][j] + add_new) % MOD;

                // Replay an old song if allowed
                if j > k_usize {
                    let add_old = dp[i - 1][j] * ((j - k_usize) as i64);
                    dp[i][j] = (dp[i][j] + add_old) % MOD;
                }
            }
        }

        dp[goal_usize][n_usize] as i32
    }
}
```

## Racket

```racket
(define/contract (num-music-playlists n goal k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let ([MOD 1000000007])
    (let ([dp (make-vector (+ goal 1))])
      ;; initialize DP rows
      (for ([i (in-range (+ goal 1))])
        (vector-set! dp i (make-vector (+ n 1) 0)))
      ;; base case: empty playlist with zero unique songs
      (let ([row0 (vector-ref dp 0)])
        (vector-set! row0 0 1))
      ;; fill DP table
      (for ([i (in-range 1 (+ goal 1))])
        (let* ([prev-row (vector-ref dp (sub1 i))]
               [curr-row (vector-ref dp i)]
               [maxj (min i n)])
          (for ([j (in-range 1 (add1 maxj))])
            (define add-new
              (* (vector-ref prev-row (sub1 j))
                 (- n j -1))) ; n - j + 1
            (define add-old
              (if (> j k)
                  (* (vector-ref prev-row j) (- j k))
                  0))
            (define total (+ add-new add-old))
            (vector-set! curr-row j (modulo total MOD)))))
      ;; answer is dp[goal][n]
      (let ([final-row (vector-ref dp goal)])
        (vector-ref final-row n)))))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec num_music_playlists(N :: integer(), Goal :: integer(), K :: integer()) -> integer().
num_music_playlists(N, Goal, K) ->
    Init = array:set(0, 1, array:new(N + 1, {default, 0})),
    Final = loop_goal(1, Goal, N, K, Init),
    array:get(N, Final).

loop_goal(I, Goal, N, K, Prev) when I =< Goal ->
    Upper = min(I, N),
    Curr0 = array:new(N + 1, {default, 0}),
    Curr = lists:foldl(
        fun(J, Acc) ->
            A = array:get(J - 1, Prev),
            New1 = (A * (N - J + 1)) rem ?MOD,
            New =
                if
                    J > K ->
                        B = array:get(J, Prev),
                        (New1 + (B * (J - K)) rem ?MOD) rem ?MOD;
                    true -> New1
                end,
            array:set(J, New, Acc)
        end,
        Curr0,
        lists:seq(1, Upper)
    ),
    loop_goal(I + 1, Goal, N, K, Curr);
loop_goal(_, _, _, _, Prev) ->
    Prev.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  @spec num_music_playlists(n :: integer, goal :: integer, k :: integer) :: integer
  def num_music_playlists(n, goal, k) do
    # dp for length 0: only one way with 0 unique songs
    init = List.duplicate(0, n + 1) |> List.replace_at(0, 1)
    final_dp = iter(1, goal, n, k, init)
    Enum.at(final_dp, n)
  end

  defp iter(i, goal, _n, _k, dp) when i > goal, do: dp

  defp iter(i, goal, n, k, prev) do
    max_j = min(i, n)

    cur =
      Enum.reduce(1..max_j, List.duplicate(0, n + 1), fn j, acc ->
        add_new = rem(Enum.at(prev, j - 1) * (n - j + 1), @mod)

        add_old =
          if j > k do
            rem(Enum.at(prev, j) * (j - k), @mod)
          else
            0
          end

        val = rem(add_new + add_old, @mod)
        List.replace_at(acc, j, val)
      end)

    iter(i + 1, goal, n, k, cur)
  end
end
```

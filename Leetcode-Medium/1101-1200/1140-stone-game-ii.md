# 1140. Stone Game II

## Cpp

```cpp
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<int> suffix(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            suffix[i] = suffix[i + 1] + piles[i];
        }
        // dp[i][m] = max stones current player can obtain from i with current M=m
        vector<vector<int>> dp(n, vector<int>(n + 1, -1));
        function<int(int,int)> solve = [&](int i, int m) -> int {
            if (i >= n) return 0;
            if (dp[i][m] != -1) return dp[i][m];
            int maxTake = min(2 * m, n - i);
            int best = 0;
            for (int x = 1; x <= maxTake; ++x) {
                // opponent will play from i+x with M' = max(m, x)
                int opp = solve(i + x, max(m, x));
                int cur = suffix[i] - opp;
                best = max(best, cur);
            }
            dp[i][m] = best;
            return best;
        };
        return solve(0, 1);
    }
};
```

## Java

```java
class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; --i) {
            suffix[i] = suffix[i + 1] + piles[i];
        }
        int[][] memo = new int[n][n + 1];
        for (int i = 0; i < n; ++i) {
            java.util.Arrays.fill(memo[i], -1);
        }
        return dfs(0, 1, n, suffix, memo);
    }

    private int dfs(int i, int m, int n, int[] suffix, int[][] memo) {
        if (i >= n) return 0;
        if (memo[i][m] != -1) return memo[i][m];
        // If we can take all remaining piles
        if (i + 2 * m >= n) {
            memo[i][m] = suffix[i];
            return memo[i][m];
        }
        int maxStones = 0;
        for (int x = 1; x <= 2 * m && i + x <= n; ++x) {
            int nextM = Math.max(m, x);
            int opponent = dfs(i + x, nextM, n, suffix, memo);
            int current = suffix[i] - opponent;
            if (current > maxStones) {
                maxStones = current;
            }
        }
        memo[i][m] = maxStones;
        return maxStones;
    }
}
```

## Python

```python
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        # suffix sums: total stones from i to end
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, m):
            # if remaining stones can all be taken
            if i >= n:
                return 0
            if 2 * m >= n - i:
                return suffix[i]
            best = 0
            # try taking x piles where 1 <= x <= 2*m
            for x in range(1, 2 * m + 1):
                next_i = i + x
                opponent_gain = dp(next_i, max(m, x))
                current_gain = suffix[i] - opponent_gain
                if current_gain > best:
                    best = current_gain
            return best

        return dp(0, 1)
```

## Python3

```python
from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            if i >= n:
                return 0
            # can take all remaining stones
            if i + 2 * m >= n:
                return suffix[i]
            best = 0
            limit = 2 * m
            for x in range(1, limit + 1):
                opponent = dp(i + x, max(m, x))
                cur = suffix[i] - opponent
                if cur > best:
                    best = cur
            return best

        return dp(0, 1)
```

## C

```c
#include <string.h>

static int suffix[101];
static int memo[101][101];

static int dfs(int i, int m, int n) {
    if (i >= n) return 0;
    if (memo[i][m] != -1) return memo[i][m];
    int maxTake = 2 * m;
    if (maxTake > n - i) maxTake = n - i;
    int best = 0;
    for (int x = 1; x <= maxTake; ++x) {
        int nextM = m > x ? m : x;
        int opponent = dfs(i + x, nextM, n);
        int cur = suffix[i] - opponent;
        if (cur > best) best = cur;
    }
    memo[i][m] = best;
    return best;
}

int stoneGameII(int* piles, int pilesSize) {
    for (int i = pilesSize - 1; i >= 0; --i) {
        suffix[i] = piles[i] + (i + 1 < pilesSize ? suffix[i + 1] : 0);
    }
    memset(memo, -1, sizeof(memo));
    return dfs(0, 1, pilesSize);
}
```

## Csharp

```csharp
public class Solution
{
    public int StoneGameII(int[] piles)
    {
        int n = piles.Length;
        int[] suffix = new int[n];
        suffix[n - 1] = piles[n - 1];
        for (int i = n - 2; i >= 0; --i)
            suffix[i] = piles[i] + suffix[i + 1];

        int[,] memo = new int[n, n + 1];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j <= n; ++j)
                memo[i, j] = -1;

        int Dfs(int idx, int m)
        {
            if (idx >= n) return 0;
            if (memo[idx, m] != -1) return memo[idx, m];
            // If we can take all remaining piles
            if (idx + 2 * m >= n)
                return memo[idx, m] = suffix[idx];

            int best = 0;
            for (int x = 1; x <= 2 * m; ++x)
            {
                int nextM = m > x ? m : x;
                int opponent = Dfs(idx + x, nextM);
                int cur = suffix[idx] - opponent;
                if (cur > best) best = cur;
            }
            memo[idx, m] = best;
            return best;
        }

        return Dfs(0, 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} piles
 * @return {number}
 */
var stoneGameII = function(piles) {
    const n = piles.length;
    const suffix = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        suffix[i] = suffix[i + 1] + piles[i];
    }
    const memo = Array.from({ length: n }, () => Array(n + 1));
    function dfs(i, m) {
        if (i >= n) return 0;
        if (memo[i][m] !== undefined) return memo[i][m];
        // If we can take all remaining piles
        if (i + 2 * m >= n) {
            memo[i][m] = suffix[i];
            return memo[i][m];
        }
        let minOpp = Infinity;
        const limit = 2 * m;
        for (let x = 1; x <= limit; ++x) {
            const nextM = Math.max(m, x);
            const opp = dfs(i + x, nextM);
            if (opp < minOpp) minOpp = opp;
        }
        memo[i][m] = suffix[i] - minOpp;
        return memo[i][m];
    }
    return dfs(0, 1);
};
```

## Typescript

```typescript
function stoneGameII(piles: number[]): number {
    const n = piles.length;
    const suffix = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        suffix[i] = suffix[i + 1] + piles[i];
    }

    const memo: Map<number, number>[] = Array.from({ length: n }, () => new Map());

    function dfs(i: number, m: number): number {
        if (i >= n) return 0;
        const cached = memo[i].get(m);
        if (cached !== undefined) return cached;

        let best = 0;
        const limit = Math.min(2 * m, n - i);
        for (let x = 1; x <= limit; ++x) {
            const opponent = dfs(i + x, Math.max(m, x));
            const current = suffix[i] - opponent;
            if (current > best) best = current;
        }

        memo[i].set(m, best);
        return best;
    }

    return dfs(0, 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $piles
     * @return Integer
     */
    function stoneGameII($piles) {
        $n = count($piles);
        // suffix sums: suffix[i] = sum of piles[i..n-1]
        $suffix = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $suffix[$i] = $piles[$i] + $suffix[$i + 1];
        }

        $memo = [];

        $dfs = function($i, $M) use (&$dfs, &$memo, $n, $suffix) {
            if ($i >= $n) {
                return 0;
            }
            $key = $i . ',' . $M;
            if (isset($memo[$key])) {
                return $memo[$key];
            }

            // If we can take all remaining piles
            if ($i + 2 * $M >= $n) {
                $memo[$key] = $suffix[$i];
                return $memo[$key];
            }

            $minOpp = PHP_INT_MAX;
            $maxTake = 2 * $M;
            for ($x = 1; $x <= $maxTake; $x++) {
                $nextI = $i + $x;
                $newM = max($M, $x);
                $opp = $dfs($nextI, $newM);
                if ($opp < $minOpp) {
                    $minOpp = $opp;
                }
            }

            // Current player's best is total remaining minus opponent's minimal result
            $memo[$key] = $suffix[$i] - $minOpp;
            return $memo[$key];
        };

        return $dfs(0, 1);
    }
}
```

## Swift

```swift
class Solution {
    func stoneGameII(_ piles: [Int]) -> Int {
        let n = piles.count
        var suffix = Array(repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            suffix[i] = suffix[i + 1] + piles[i]
        }
        var memo = Array(repeating: Array(repeating: -1, count: n + 1), count: n)
        
        func dfs(_ i: Int, _ m: Int) -> Int {
            if i >= n { return 0 }
            if memo[i][m] != -1 { return memo[i][m] }
            // If we can take all remaining piles
            if i + 2 * m >= n {
                memo[i][m] = suffix[i]
                return suffix[i]
            }
            var best = 0
            for x in 1...2 * m {
                let nextI = i + x
                let nextM = max(m, x)
                // opponent's optimal result from the next state
                let opp = dfs(nextI, nextM)
                // our stones = total remaining - opponent's best
                let cur = suffix[i] - opp
                if cur > best {
                    best = cur
                }
            }
            memo[i][m] = best
            return best
        }
        
        return dfs(0, 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stoneGameII(piles: IntArray): Int {
        val n = piles.size
        val suffix = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            suffix[i] = suffix[i + 1] + piles[i]
        }
        val memo = Array(n) { IntArray(n + 1) { -1 } }

        fun dfs(i: Int, m: Int): Int {
            if (i >= n) return 0
            if (memo[i][m] != -1) return memo[i][m]
            var best = 0
            val limit = kotlin.math.min(2 * m, n - i)
            for (x in 1..limit) {
                val nextM = if (x > m) x else m
                val opponent = dfs(i + x, nextM)
                val current = suffix[i] - opponent
                if (current > best) best = current
            }
            memo[i][m] = best
            return best
        }

        return dfs(0, 1)
    }
}
```

## Dart

```dart
class Solution {
  int stoneGameII(List<int> piles) {
    int n = piles.length;
    List<int> suffix = List.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      suffix[i] = suffix[i + 1] + piles[i];
    }
    List<List<int?>> dp = List.generate(n, (_) => List.filled(n + 1, null));

    int dfs(int i, int m) {
      if (i >= n) return 0;
      if (dp[i][m] != null) return dp[i][m]!;
      int maxTake = 2 * m;
      int best = 0;
      for (int x = 1; x <= maxTake && i + x <= n; ++x) {
        int nextM = m > x ? m : x;
        int opponent = dfs(i + x, nextM);
        int current = suffix[i] - opponent;
        if (current > best) best = current;
      }
      dp[i][m] = best;
      return best;
    }

    return dfs(0, 1);
  }
}
```

## Golang

```go
func stoneGameII(piles []int) int {
    n := len(piles)
    suffix := make([]int, n+1)
    for i := n - 1; i >= 0; i-- {
        suffix[i] = piles[i] + suffix[i+1]
    }
    dp := make([][]int, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]int, n+1)
        for j := 0; j <= n; j++ {
            dp[i][j] = -1
        }
    }

    var dfs func(i, m int) int
    dfs = func(i, m int) int {
        if i >= n {
            return 0
        }
        if dp[i][m] != -1 {
            return dp[i][m]
        }
        if i+2*m >= n {
            dp[i][m] = suffix[i]
            return dp[i][m]
        }
        best := 0
        limit := 2 * m
        for x := 1; x <= limit && i+x <= n; x++ {
            nextM := m
            if x > m {
                nextM = x
            }
            opponent := dfs(i+x, nextM)
            cur := suffix[i] - opponent
            if cur > best {
                best = cur
            }
        }
        dp[i][m] = best
        return best
    }

    return dfs(0, 1)
}
```

## Ruby

```ruby
def stone_game_ii(piles)
  n = piles.length
  suffix = Array.new(n + 1, 0)
  (n - 1).downto(0) { |i| suffix[i] = suffix[i + 1] + piles[i] }
  memo = Array.new(n) { Array.new(n + 1) }

  dfs = lambda do |i, m|
    return 0 if i >= n
    cached = memo[i][m]
    return cached unless cached.nil?

    max_take = [2 * m, n - i].min
    best = 0
    (1..max_take).each do |x|
      opponent = dfs.call(i + x, [m, x].max)
      current = suffix[i] - opponent
      best = current if current > best
    end

    memo[i][m] = best
    best
  end

  dfs.call(0, 1)
end
```

## Scala

```scala
object Solution {
    def stoneGameII(piles: Array[Int]): Int = {
        val n = piles.length
        val suffix = new Array[Int](n + 1)
        for (i <- n - 1 to 0 by -1) {
            suffix(i) = suffix(i + 1) + piles(i)
        }
        val memo = Array.ofDim[Int](n, n + 1)
        for (i <- 0 until n; j <- 0 to n) {
            memo(i)(j) = -1
        }

        def dfs(i: Int, m: Int): Int = {
            if (i >= n) return 0
            if (memo(i)(m) != -1) return memo(i)(m)
            if (i + 2 * m >= n) {
                memo(i)(m) = suffix(i)
                return memo(i)(m)
            }
            var best = 0
            var x = 1
            while (x <= 2 * m && i + x <= n) {
                val nextM = math.max(m, x)
                val opponent = dfs(i + x, nextM)
                val current = suffix(i) - opponent
                if (current > best) best = current
                x += 1
            }
            memo(i)(m) = best
            best
        }

        dfs(0, 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        let n = piles.len();
        let mut suffix = vec![0i32; n + 1];
        for i in (0..n).rev() {
            suffix[i] = suffix[i + 1] + piles[i];
        }
        // memo[i][m] stores the best result starting at index i with current M = m
        let mut memo = vec![vec![-1i32; n + 1]; n];

        fn dfs(
            i: usize,
            m: usize,
            n: usize,
            suffix: &Vec<i32>,
            memo: &mut Vec<Vec<i32>>,
        ) -> i32 {
            if i >= n {
                return 0;
            }
            if memo[i][m] != -1 {
                return memo[i][m];
            }
            let remaining = n - i;
            // Can take all remaining piles
            if remaining <= 2 * m {
                memo[i][m] = suffix[i];
                return suffix[i];
            }

            let mut best = 0i32;
            for x in 1..=2 * m {
                if i + x > n {
                    break;
                }
                let next_m = std::cmp::max(m, x);
                let opponent = dfs(i + x, next_m, n, suffix, memo);
                let current = suffix[i] - opponent;
                if current > best {
                    best = current;
                }
            }
            memo[i][m] = best;
            best
        }

        dfs(0, 1, n, &suffix, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (stone-game-ii piles)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector piles)]
         [n (vector-length v)])
    ;; suffix sums
    (define suffix (make-vector (+ n 1) 0))
    (for ([i (in-range (- n 1) -1 -1)])
      (vector-set! suffix i
                   (+ (vector-ref v i)
                      (vector-ref suffix (+ i 1)))))
    ;; memo table dp[i][m] initialized to -1
    (define dp (make-vector n))
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector (+ n 1) -1)))
    (letrec ((solve (lambda (i m)
                      (if (>= (+ i (* 2 m)) n)
                          (vector-ref suffix i)
                          (let* ([row (vector-ref dp i)]
                                 [cached (vector-ref row m)])
                            (if (not (= cached -1))
                                cached
                                (let loop ((x 1) (best 0))
                                  (cond
                                    [(> x (* 2 m)) (begin
                                                     (vector-set! row m best)
                                                     best)]
                                    [(> (+ i x) n) (begin
                                                    (vector-set! row m best)
                                                    best)]
                                    [else
                                     (let* ([nextM (max m x)]
                                            [opp (solve (+ i x) nextM)]
                                            [cur (- (vector-ref suffix i) opp)])
                                       (loop (+ x 1) (if (> cur best) cur best)))]))))))))
      (solve 0 1))))
```

## Erlang

```erlang
-module(solution).
-export([stone_game_ii/1]).

-spec stone_game_ii(Piles :: [integer()]) -> integer().
stone_game_ii(Piles) ->
    Suffix = suffix_sums(Piles, []),
    {Ans, _} = dp(0, 1, Piles, Suffix, maps:new()),
    Ans.

suffix_sums([], Acc) ->
    [0 | Acc];
suffix_sums([H|T], Acc) ->
    Rest = suffix_sums(T, Acc),
    SumNext = hd(Rest),
    [H + SumNext | Rest].

dp(I, M, Piles, Suffix, Memo) ->
    N = length(Piles),
    if I >= N ->
            {0, Memo};
       true ->
            Key = {I, M},
            case maps:find(Key, Memo) of
                {ok, Val} -> {Val, Memo};
                error ->
                    MaxTake = erlang:min(2 * M, N - I),
                    Total = lists:nth(I + 1, Suffix),
                    {Best, NewMemo} = dp_loop(1, MaxTake, I, M, Total,
                                             Piles, Suffix, Memo, 0),
                    UpdatedMemo = maps:put(Key, Best, NewMemo),
                    {Best, UpdatedMemo}
            end
    end.

dp_loop(X, MaxTake, _I, _M, _Total, _Piles, _Suffix, Memo, Best) when X > MaxTake ->
    {Best, Memo};
dp_loop(X, MaxTake, I, M, Total, Piles, Suffix, Memo, Best) ->
    NewM = erlang:max(M, X),
    {OppGain, Memo1} = dp(I + X, NewM, Piles, Suffix, Memo),
    Gain = Total - OppGain,
    NewBest = if Gain > Best -> Gain; true -> Best end,
    dp_loop(X + 1, MaxTake, I, M, Total, Piles, Suffix, Memo1, NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec stone_game_ii(piles :: [integer]) :: integer
  def stone_game_ii(piles) do
    n = length(piles)

    # suffix sums: suffix[i] = sum of piles[i..n-1], suffix[n] = 0
    suffix =
      piles
      |> Enum.reverse()
      |> Enum.reduce([0], fn val, [prev | _] = acc -> [val + prev | acc] end)

    {result, _} = dfs(0, 1, suffix, n, %{})
    result
  end

  defp dfs(i, m, suffix, n, memo) do
    case Map.fetch(memo, {i, m}) do
      {:ok, val} ->
        {val, memo}

      :error ->
        cond do
          i >= n ->
            {0, Map.put(memo, {i, m}, 0)}

          i + 2 * m >= n ->
            total = Enum.at(suffix, i)
            {total, Map.put(memo, {i, m}, total)}

          true ->
            total = Enum.at(suffix, i)

            {best, new_memo} =
              Enum.reduce(1..(2 * m), {0, memo}, fn x, {cur_best, cur_memo} ->
                next_i = i + x
                next_m = Integer.max(m, x)
                {opp_gain, updated_memo} = dfs(next_i, next_m, suffix, n, cur_memo)
                cur = total - opp_gain
                new_best = if cur > cur_best, do: cur, else: cur_best
                {new_best, updated_memo}
              end)

            {best, Map.put(new_memo, {i, m}, best)}
        end
    end
  end
end
```

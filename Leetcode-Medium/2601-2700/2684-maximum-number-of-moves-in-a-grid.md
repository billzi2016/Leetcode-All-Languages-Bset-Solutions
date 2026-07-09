# 2684. Maximum Number of Moves in a Grid

## Cpp

```cpp
class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        const int dirs[3] = {-1, 0, 1};
        for (int col = n - 2; col >= 0; --col) {
            for (int row = 0; row < m; ++row) {
                int best = 0;
                for (int d : dirs) {
                    int nr = row + d;
                    if (nr < 0 || nr >= m) continue;
                    if (grid[nr][col + 1] > grid[row][col]) {
                        best = max(best, 1 + dp[nr][col + 1]);
                    }
                }
                dp[row][col] = best;
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) ans = max(ans, dp[i][0]);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxMoves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] prev = new int[m];
        int[] cur = new int[m];

        for (int col = n - 2; col >= 0; col--) {
            Arrays.fill(cur, 0);
            for (int i = 0; i < m; i++) {
                int best = 0;
                for (int d = -1; d <= 1; d++) {
                    int nr = i + d;
                    if (nr < 0 || nr >= m) continue;
                    if (grid[nr][col + 1] > grid[i][col]) {
                        best = Math.max(best, 1 + prev[nr]);
                    }
                }
                cur[i] = best;
            }
            int[] tmp = prev;
            prev = cur;
            cur = tmp;
        }

        int ans = 0;
        for (int v : prev) {
            if (v > ans) ans = v;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # moves achieved when reaching each cell in current column
        prev = [0] * m  # column 0, starting cells have 0 moves
        max_moves = 0

        for col in range(1, n):
            cur = [-1] * m
            for i in range(m):
                best = -1
                # check three possible previous rows
                for dr in (-1, 0, 1):
                    pi = i + dr
                    if 0 <= pi < m and grid[pi][col - 1] < grid[i][col]:
                        if prev[pi] != -1:
                            cand = prev[pi] + 1
                            if cand > best:
                                best = cand
                cur[i] = best
                if best > max_moves:
                    max_moves = best
            prev = cur

        return max_moves
```

## Python3

```python
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]  # dp[i][j]: max moves starting from (i,j)

        for j in range(n - 2, -1, -1):
            for i in range(m):
                cur = grid[i][j]
                best = 0
                if i > 0 and grid[i - 1][j + 1] > cur:
                    best = max(best, 1 + dp[i - 1][j + 1])
                if grid[i][j + 1] > cur:
                    best = max(best, 1 + dp[i][j + 1])
                if i + 1 < m and grid[i + 1][j + 1] > cur:
                    best = max(best, 1 + dp[i + 1][j + 1])
                dp[i][j] = best

        return max(dp[i][0] for i in range(m))
```

## C

```c
#include <stdlib.h>
#include <string.h>

static inline int max(int a, int b) { return a > b ? a : b; }

int maxMoves(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    
    int *prev = (int *)calloc(m, sizeof(int));
    int *curr = (int *)calloc(m, sizeof(int));
    if (!prev || !curr) return 0; // safety
    
    for (int i = 0; i < m; ++i) prev[i] = 1; // starting cells are reachable
    
    int answer = 0;
    
    for (int col = 1; col < n; ++col) {
        memset(curr, 0, m * sizeof(int));
        for (int row = 0; row < m; ++row) {
            int best = 0;
            if (prev[row] > 0 && grid[row][col] > grid[row][col - 1])
                best = max(best, prev[row] + 1);
            if (row > 0 && prev[row - 1] > 0 && grid[row][col] > grid[row - 1][col - 1])
                best = max(best, prev[row - 1] + 1);
            if (row + 1 < m && prev[row + 1] > 0 && grid[row][col] > grid[row + 1][col - 1])
                best = max(best, prev[row + 1] + 1);
            curr[row] = best;
            if (best > 0) answer = max(answer, best - 1); // subtract initial offset
        }
        int *tmp = prev; prev = curr; curr = tmp;
    }
    
    free(prev);
    free(curr);
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxMoves(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;

        // dpPrev[i] stores the maximum moves to reach cell (i, col-1)
        int[] dpPrev = new int[m];
        for (int i = 0; i < m; i++) dpPrev[i] = 0; // starting cells reachable with 0 moves

        int maxMoves = 0;

        for (int col = 1; col < n; col++)
        {
            int[] dpCurr = new int[m];
            for (int i = 0; i < m; i++) dpCurr[i] = -1;

            for (int row = 0; row < m; row++)
            {
                int best = -1;
                // check three possible previous rows
                if (row > 0 && grid[row - 1][col - 1] < grid[row][col] && dpPrev[row - 1] != -1)
                    best = Math.Max(best, dpPrev[row - 1] + 1);
                if (grid[row][col - 1] < grid[row][col] && dpPrev[row] != -1)
                    best = Math.Max(best, dpPrev[row] + 1);
                if (row + 1 < m && grid[row + 1][col - 1] < grid[row][col] && dpPrev[row + 1] != -1)
                    best = Math.Max(best, dpPrev[row + 1] + 1);

                dpCurr[row] = best;
                if (best > maxMoves) maxMoves = best;
            }

            dpPrev = dpCurr;
        }

        return maxMoves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxMoves = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const memo = Array.from({ length: m }, () => Array(n).fill(-1));
    const dirs = [-1, 0, 1];
    
    function dfs(r, c) {
        if (memo[r][c] !== -1) return memo[r][c];
        let best = 0;
        for (const dr of dirs) {
            const nr = r + dr;
            const nc = c + 1;
            if (nr >= 0 && nr < m && nc < n && grid[nr][nc] > grid[r][c]) {
                const moves = 1 + dfs(nr, nc);
                if (moves > best) best = moves;
            }
        }
        memo[r][c] = best;
        return best;
    }
    
    let ans = 0;
    for (let i = 0; i < m; ++i) {
        ans = Math.max(ans, dfs(i, 0));
    }
    return ans;
};
```

## Typescript

```typescript
function maxMoves(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    // dpPrev[i] stores (max moves to reach cell (i, col-1)) + 1
    let dpPrev = new Array(m).fill(1);
    let maxMoves = 0;

    for (let col = 1; col < n; ++col) {
        const dpCurr = new Array(m).fill(0);
        for (let row = 0; row < m; ++row) {
            let bestPrev = 0;
            if (grid[row][col] > grid[row][col - 1]) {
                bestPrev = Math.max(bestPrev, dpPrev[row]);
            }
            if (row > 0 && grid[row][col] > grid[row - 1][col - 1]) {
                bestPrev = Math.max(bestPrev, dpPrev[row - 1]);
            }
            if (row + 1 < m && grid[row][col] > grid[row + 1][col - 1]) {
                bestPrev = Math.max(bestPrev, dpPrev[row + 1]);
            }
            if (bestPrev > 0) {
                dpCurr[row] = bestPrev + 1;
                const moves = dpCurr[row] - 1; // subtract the initial offset
                if (moves > maxMoves) maxMoves = moves;
            }
        }
        dpPrev = dpCurr;
    }

    return maxMoves;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxMoves($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        // dp for previous column: moves needed to reach each cell (0 for first column)
        $dpPrev = array_fill(0, $m, 0);
        $ans = 0;
        for ($col = 1; $col < $n; $col++) {
            $dpCurr = array_fill(0, $m, -1);
            for ($row = 0; $row < $m; $row++) {
                foreach ([-1, 0, 1] as $dr) {
                    $pr = $row + $dr;
                    if ($pr < 0 || $pr >= $m) continue;
                    if ($grid[$row][$col] > $grid[$pr][$col - 1] && $dpPrev[$pr] != -1) {
                        $cand = $dpPrev[$pr] + 1;
                        if ($cand > $dpCurr[$row]) {
                            $dpCurr[$row] = $cand;
                        }
                    }
                }
            }
            foreach ($dpCurr as $val) {
                if ($val > $ans) $ans = $val;
            }
            $dpPrev = $dpCurr;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxMoves(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        if n == 1 { return 0 }
        
        var prev = [Int](repeating: -1, count: m)
        for i in 0..<m {
            prev[i] = 0   // starting cells have 0 moves
        }
        var answer = 0
        
        for col in 1..<n {
            var cur = [Int](repeating: -1, count: m)
            for row in 0..<m {
                // from left
                if grid[row][col] > grid[row][col - 1], prev[row] != -1 {
                    cur[row] = max(cur[row], prev[row] + 1)
                }
                // from upper-left
                if row > 0, grid[row][col] > grid[row - 1][col - 1], prev[row - 1] != -1 {
                    cur[row] = max(cur[row], prev[row - 1] + 1)
                }
                // from lower-left
                if row + 1 < m, grid[row][col] > grid[row + 1][col - 1], prev[row + 1] != -1 {
                    cur[row] = max(cur[row], prev[row + 1] + 1)
                }
                if cur[row] > answer {
                    answer = cur[row]
                }
            }
            prev = cur
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxMoves(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dp = Array(m) { IntArray(n) { -1 } }

        fun dfs(r: Int, c: Int): Int {
            if (dp[r][c] != -1) return dp[r][c]
            var best = 0
            for (dr in -1..1) {
                val nr = r + dr
                val nc = c + 1
                if (nr in 0 until m && nc < n && grid[nr][nc] > grid[r][c]) {
                    val cand = 1 + dfs(nr, nc)
                    if (cand > best) best = cand
                }
            }
            dp[r][c] = best
            return best
        }

        var answer = 0
        for (row in 0 until m) {
            val moves = dfs(row, 0)
            if (moves > answer) answer = moves
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxMoves(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // moves needed to reach each cell in the current column.
    List<int> prev = List.filled(m, 0); // start cells have 0 moves
    int maxMoves = 0;

    for (int col = 1; col < n; ++col) {
      List<int> cur = List.filled(m, -1);
      for (int row = 0; row < m; ++row) {
        int best = -1;
        // directly left
        if (grid[row][col] > grid[row][col - 1] && prev[row] >= 0) {
          best = max(best, prev[row] + 1);
        }
        // upper-left diagonal
        if (row > 0 &&
            grid[row][col] > grid[row - 1][col - 1] &&
            prev[row - 1] >= 0) {
          best = max(best, prev[row - 1] + 1);
        }
        // lower-left diagonal
        if (row + 1 < m &&
            grid[row][col] > grid[row + 1][col - 1] &&
            prev[row + 1] >= 0) {
          best = max(best, prev[row + 1] + 1);
        }
        cur[row] = best;
        if (best > maxMoves) maxMoves = best;
      }
      prev = cur;
    }

    return maxMoves;
  }
}
```

## Golang

```go
func maxMoves(grid [][]int) int {
    m := len(grid)
    if m == 0 {
        return 0
    }
    n := len(grid[0])
    dp := make([][]int, m)
    for i := 0; i < m; i++ {
        dp[i] = make([]int, n)
        for j := 0; j < n; j++ {
            dp[i][j] = -1
        }
    }

    var dfs func(int, int) int
    dfs = func(i, j int) int {
        if dp[i][j] != -1 {
            return dp[i][j]
        }
        best := 0
        for _, d := range []int{-1, 0, 1} {
            ni, nj := i+d, j+1
            if ni >= 0 && ni < m && nj < n && grid[ni][nj] > grid[i][j] {
                moves := 1 + dfs(ni, nj)
                if moves > best {
                    best = moves
                }
            }
        }
        dp[i][j] = best
        return best
    }

    ans := 0
    for i := 0; i < m; i++ {
        if val := dfs(i, 0); val > ans {
            ans = val
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_moves(grid)
  m = grid.length
  n = grid[0].length
  prev = Array.new(m, 0) # moves count at column 0 (starting positions)
  ans = 0

  (1...n).each do |col|
    cur = Array.new(m, -1)
    i = 0
    while i < m
      best = -1
      dr = -1
      while dr <= 1
        pr = i + dr
        if pr >= 0 && pr < m && grid[pr][col - 1] < grid[i][col] && prev[pr] != -1
          cand = prev[pr] + 1
          best = cand if cand > best
        end
        dr += 1
      end
      cur[i] = best
      ans = best if best > ans
      i += 1
    end
    prev = cur
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxMoves(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        var prev = Array.fill(m)(1) // reachable start cells count as 1
        var maxMoves = 0

        for (j <- 1 until n) {
            val cur = new Array[Int](m)
            var i = 0
            while (i < m) {
                var best = 0
                // up-left
                if (i > 0 && grid(i)(j) > grid(i - 1)(j - 1) && prev(i - 1) > 0) {
                    best = math.max(best, prev(i - 1))
                }
                // left
                if (grid(i)(j) > grid(i)(j - 1) && prev(i) > 0) {
                    best = math.max(best, prev(i))
                }
                // down-left
                if (i + 1 < m && grid(i)(j) > grid(i + 1)(j - 1) && prev(i + 1) > 0) {
                    best = math.max(best, prev(i + 1))
                }

                if (best > 0) {
                    cur(i) = best + 1
                    maxMoves = math.max(maxMoves, cur(i) - 1)
                } else {
                    cur(i) = 0
                }
                i += 1
            }
            prev = cur
        }

        maxMoves
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_moves(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        // moves count reachable at each row of the previous column
        let mut prev = vec![0i32; m];
        let mut ans = 0i32;
        for col in 1..n {
            let mut cur = vec![-1i32; m];
            for i in 0..m {
                for dr in -1..=1 {
                    let pr = i as isize + dr;
                    if pr < 0 || pr >= m as isize {
                        continue;
                    }
                    let pr_usize = pr as usize;
                    if prev[pr_usize] >= 0 && grid[i][col] > grid[pr_usize][col - 1] {
                        cur[i] = cur[i].max(prev[pr_usize] + 1);
                    }
                }
            }
            for &v in &cur {
                if v > ans {
                    ans = v;
                }
            }
            prev = cur;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-moves grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows-vec (list->vector (map list->vector grid)))
         (m (vector-length rows-vec))
         (n (if (= m 0) 0 (vector-length (vector-ref rows-vec 0)))))
    (if (or (< m 2) (< n 2))
        0
        (let ((prev (make-vector m 1))) ; start cells count as 1
          (let loop ((col 1) (prev prev) (ans 0))
            (if (= col n)
                ans
                (let ((cur (make-vector m 0))
                      (col-max 0))
                  (for ([i (in-range m)])
                    (let* ((val (vector-ref (vector-ref rows-vec i) col))
                           (best 0))
                      ;; same row
                      (when (and (> val (vector-ref (vector-ref rows-vec i) (- col 1)))
                                 (> (vector-ref prev i) 0))
                        (set! best (max best (+ (vector-ref prev i) 1))))
                      ;; up diagonal
                      (when (> i 0)
                        (let ((up-val (vector-ref (vector-ref rows-vec (- i 1)) (- col 1)))
                              (up-prev (vector-ref prev (- i 1))))
                          (when (and (> val up-val) (> up-prev 0))
                            (set! best (max best (+ up-prev 1))))))
                      ;; down diagonal
                      (when (< i (- m 1))
                        (let ((down-val (vector-ref (vector-ref rows-vec (+ i 1)) (- col 1)))
                              (down-prev (vector-ref prev (+ i 1))))
                          (when (and (> val down-val) (> down-prev 0))
                            (set! best (max best (+ down-prev 1))))))
                      (vector-set! cur i best)
                      (when (> best 0)
                        (set! col-max (max col-max (- best 1))))))
                  (loop (+ col 1) cur (max ans col-max)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_moves/1]).
-spec max_moves(Grid :: [[integer()]]) -> integer().
max_moves(Grid) ->
    M = length(Grid),
    {FirstVals, RowTails} = extract_first(Grid, [], []),
    DpPrev = lists:duplicate(M, 1),
    loop(RowTails, FirstVals, DpPrev, 0).

extract_first([], VAcc, TAcc) ->
    {lists:reverse(VAcc), lists:reverse(TAcc)};
extract_first([Row|Rest], VAcc, TAcc) ->
    [H|Tail] = Row,
    extract_first(Rest, [H|VAcc], [Tail|TAcc]).

loop(RowLists, PrevVals, DpPrev, MaxSoFar) ->
    case RowLists of
        [] -> MaxSoFar;
        _ ->
            case hd(RowLists) of
                [] -> MaxSoFar; % no more columns
                _ ->
                    NextVals = [hd(Tail) || Tail <- RowLists],
                    {DpCurr, NewMax} = process(PrevVals, DpPrev, NextVals),
                    NewRowLists = [tl(Tail) || Tail <- RowLists],
                    loop(NewRowLists, NextVals, DpCurr,
                         erlang:max(MaxSoFar, NewMax))
            end
    end.

process(PrevVals, DpPrev, NextVals) ->
    process(PrevVals, DpPrev, NextVals, undefined, 0, [], 0).

process([], [], [], _UpVal, _UpDp, AccRev, Max) ->
    {lists:reverse(AccRev), Max};
process([CurPrev|RestPrev], [CurDp|RestDp], [NextVal|RestNext],
        UpVal, UpDp, AccRev, Max) ->
    DownVal = case RestPrev of
                  [] -> undefined;
                  [Down|_] -> Down
              end,
    DownDp = case RestDp of
                 [] -> 0;
                 [_|Tail] -> hd(Tail)
             end,
    Best1 = if UpVal =/= undefined, UpVal < NextVal, UpDp > 0 ->
                UpDp + 1;
            true -> 0
            end,
    Best2 = if CurPrev < NextVal, CurDp > 0 ->
                erlang:max(Best1, CurDp + 1);
            true -> Best1
            end,
    Best3 = if DownVal =/= undefined, DownVal < NextVal, DownDp > 0 ->
                erlang:max(Best2, DownDp + 1);
            true -> Best2
            end,
    NewMax = case Best3 of
                 0 -> Max;
                 _ -> erlang:max(Max, Best3 - 1)
             end,
    process(RestPrev, RestDp, RestNext, CurPrev, CurDp,
            [Best3|AccRev], NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_moves(grid :: [[integer]]) :: integer
  def max_moves(grid) do
    rows = Enum.map(grid, &List.to_tuple/1) |> List.to_tuple()
    m = tuple_size(rows)
    n = tuple_size(elem(rows, 0))

    # Initialize previous column DP with 1 for each row (reachable start cells)
    init_list = for _ <- 0..(m - 1), do: 1
    prev = :array.from_list(init_list)

    {max_moves, _} =
      Enum.reduce(1..(n - 1), {0, prev}, fn col, {cur_max, prev_arr} ->
        cur_arr = :array.new(m, default: 0)

        {new_max, new_cur_arr} =
          Enum.reduce(0..(m - 1), {cur_max, cur_arr}, fn row, {inner_max, arr} ->
            val = elem(elem(rows, row), col)
            best = 0

            # same row left
            prev_val = :array.get(row, prev_arr)

            if prev_val > 0 do
              left_val = elem(elem(rows, row), col - 1)

              if val > left_val do
                best = max(best, prev_val + 1)
              end
            end

            # up-left
            if row > 0 do
              prev_up = :array.get(row - 1, prev_arr)

              if prev_up > 0 do
                up_left_val = elem(elem(rows, row - 1), col - 1)

                if val > up_left_val do
                  best = max(best, prev_up + 1)
                end
              end
            end

            # down-left
            if row < m - 1 do
              prev_down = :array.get(row + 1, prev_arr)

              if prev_down > 0 do
                down_left_val = elem(elem(rows, row + 1), col - 1)

                if val > down_left_val do
                  best = max(best, prev_down + 1)
                end
              end
            end

            arr2 = :array.set(row, best, arr)
            inner_max2 = if best > 0, do: max(inner_max, best - 1), else: inner_max
            {inner_max2, arr2}
          end)

        {new_max, new_cur_arr}
      end)

    max_moves
  end
end
```

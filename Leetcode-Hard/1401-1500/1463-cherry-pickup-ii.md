# 1463. Cherry Pickup II

## Cpp

```cpp
class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        // dp[row][c1][c2]
        vector<vector<vector<int>>> memo(m, vector<vector<int>>(n, vector<int>(n, -1)));
        function<int(int,int,int)> dfs = [&](int r, int c1, int c2) -> int {
            if (c1 < 0 || c1 >= n || c2 < 0 || c2 >= n) return INT_MIN; // invalid
            if (memo[r][c1][c2] != -1) return memo[r][c1][c2];
            int cur = grid[r][c1];
            if (c1 != c2) cur += grid[r][c2];
            if (r == m - 1) {
                memo[r][c1][c2] = cur;
                return cur;
            }
            int best = INT_MIN;
            for (int d1 = -1; d1 <= 1; ++d1) {
                for (int d2 = -1; d2 <= 1; ++d2) {
                    int nc1 = c1 + d1, nc2 = c2 + d2;
                    int nxt = dfs(r + 1, nc1, nc2);
                    best = max(best, nxt);
                }
            }
            memo[r][c1][c2] = cur + best;
            return memo[r][c1][c2];
        };
        return dfs(0, 0, n - 1);
    }
};
```

## Java

```java
class Solution {
    private int[][][] memo;
    private int rows, cols;
    private int[][] grid;

    public int cherryPickup(int[][] grid) {
        this.grid = grid;
        rows = grid.length;
        cols = grid[0].length;
        memo = new int[rows][cols][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                java.util.Arrays.fill(memo[i][j], -1);
            }
        }
        return dfs(0, 0, cols - 1);
    }

    private int dfs(int r, int c1, int c2) {
        if (c1 < 0 || c1 >= cols || c2 < 0 || c2 >= cols) {
            return Integer.MIN_VALUE; // invalid position
        }
        if (memo[r][c1][c2] != -1) {
            return memo[r][c1][c2];
        }

        int result = grid[r][c1];
        if (c1 != c2) {
            result += grid[r][c2];
        }

        if (r == rows - 1) {
            memo[r][c1][c2] = result;
            return result;
        }

        int maxNext = Integer.MIN_VALUE;
        for (int d1 = -1; d1 <= 1; d1++) {
            for (int d2 = -1; d2 <= 1; d2++) {
                int next = dfs(r + 1, c1 + d1, c2 + d2);
                if (next > maxNext) {
                    maxNext = next;
                }
            }
        }

        result += maxNext;
        memo[r][c1][c2] = result;
        return result;
    }
}
```

## Python

```python
import functools

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        @functools.lru_cache(None)
        def dp(r, c1, c2):
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return -10**9
            cur = grid[r][c1]
            if c2 != c1:
                cur += grid[r][c2]
            if r == rows - 1:
                return cur
            best_next = -10**9
            for nc1 in (c1 - 1, c1, c1 + 1):
                for nc2 in (c2 - 1, c2, c2 + 1):
                    best_next = max(best_next, dp(r + 1, nc1, nc2))
            return cur + best_next

        return dp(0, 0, cols - 1)
```

## Python3

```python
class Solution:
    def cherryPickup(self, grid):
        from functools import lru_cache
        rows, cols = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(r, c1, c2):
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return -10**9  # invalid
            cur = grid[r][c1]
            if c1 != c2:
                cur += grid[r][c2]
            if r == rows - 1:
                return cur
            best = 0
            for d1 in (-1, 0, 1):
                nc1 = c1 + d1
                for d2 in (-1, 0, 1):
                    nc2 = c2 + d2
                    best = max(best, dp(r + 1, nc1, nc2))
            return cur + best

        return dp(0, 0, cols - 1)
```

## C

```c
int rows, cols;
int **g;
int dp[71][71][71];

int dfs(int r, int c1, int c2) {
    if (c1 < 0 || c1 >= cols || c2 < 0 || c2 >= cols) return -1000000;
    int *memo = &dp[r][c1][c2];
    if (*memo != -1) return *memo;
    int cur = g[r][c1] + (c1 == c2 ? 0 : g[r][c2]);
    if (r == rows - 1) {
        *memo = cur;
        return cur;
    }
    int best = -1000000;
    for (int d1 = -1; d1 <= 1; ++d1) {
        for (int d2 = -1; d2 <= 1; ++d2) {
            int nc1 = c1 + d1, nc2 = c2 + d2;
            if (nc1 >= 0 && nc1 < cols && nc2 >= 0 && nc2 < cols) {
                int nxt = dfs(r + 1, nc1, nc2);
                if (nxt > best) best = nxt;
            }
        }
    }
    *memo = cur + best;
    return *memo;
}

int cherryPickup(int** grid, int gridSize, int* gridColSize) {
    rows = gridSize;
    cols = gridColSize[0];
    g = grid;
    for (int i = 0; i < rows; ++i)
        for (int j = 0; j < cols; ++j)
            for (int k = 0; k < cols; ++k)
                dp[i][j][k] = -1;
    return dfs(0, 0, cols - 1);
}
```

## Csharp

```csharp
public class Solution
{
    private int[][] _grid;
    private int _rows, _cols;
    private int[,,] _memo;

    public int CherryPickup(int[][] grid)
    {
        _grid = grid;
        _rows = grid.Length;
        _cols = grid[0].Length;
        _memo = new int[_rows, _cols, _cols];
        for (int i = 0; i < _rows; i++)
            for (int j = 0; j < _cols; j++)
                for (int k = 0; k < _cols; k++)
                    _memo[i, j, k] = -1;

        return Dp(0, 0, _cols - 1);
    }

    private int Dp(int r, int c1, int c2)
    {
        if (c1 < 0 || c1 >= _cols || c2 < 0 || c2 >= _cols)
            return int.MinValue / 2; // invalid position

        if (_memo[r, c1, c2] != -1)
            return _memo[r, c1, c2];

        int cur = _grid[r][c1];
        if (c1 != c2) cur += _grid[r][c2];

        if (r == _rows - 1)
        {
            _memo[r, c1, c2] = cur;
            return cur;
        }

        int bestNext = int.MinValue / 2;
        for (int d1 = -1; d1 <= 1; d1++)
        {
            for (int d2 = -1; d2 <= 1; d2++)
            {
                int nxt = Dp(r + 1, c1 + d1, c2 + d2);
                if (nxt > bestNext) bestNext = nxt;
            }
        }

        cur += bestNext;
        _memo[r, c1, c2] = cur;
        return cur;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var cherryPickup = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    // memo[row][c1][c2] = max cherries from this state
    const memo = Array.from({ length: rows }, () =>
        Array.from({ length: cols }, () => Array(cols).fill(undefined))
    );

    function dfs(r, c1, c2) {
        if (c1 < 0 || c1 >= cols || c2 < 0 || c2 >= cols) return -Infinity;
        if (memo[r][c1][c2] !== undefined) return memo[r][c1][c2];

        let cur = grid[r][c1];
        if (c1 !== c2) cur += grid[r][c2];

        if (r === rows - 1) {
            memo[r][c1][c2] = cur;
            return cur;
        }

        let bestNext = -Infinity;
        for (let d1 = -1; d1 <= 1; ++d1) {
            for (let d2 = -1; d2 <= 1; ++d2) {
                const nc1 = c1 + d1;
                const nc2 = c2 + d2;
                if (nc1 < 0 || nc1 >= cols || nc2 < 0 || nc2 >= cols) continue;
                const val = dfs(r + 1, nc1, nc2);
                if (val > bestNext) bestNext = val;
            }
        }

        memo[r][c1][c2] = cur + bestNext;
        return memo[r][c1][c2];
    }

    return dfs(0, 0, cols - 1);
};
```

## Typescript

```typescript
function cherryPickup(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const memo: Int32Array[][] = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => new Int32Array(n).fill(-1))
    );
    const NEG_INF = -1e9;

    function dfs(r: number, c1: number, c2: number): number {
        if (c1 < 0 || c1 >= n || c2 < 0 || c2 >= n) return NEG_INF;
        if (memo[r][c1][c2] !== -1) return memo[r][c1][c2];

        let cur = grid[r][c1];
        if (c1 !== c2) cur += grid[r][c2];

        if (r === m - 1) {
            memo[r][c1][c2] = cur;
            return cur;
        }

        let bestNext = NEG_INF;
        for (let d1 = -1; d1 <= 1; ++d1) {
            const nc1 = c1 + d1;
            for (let d2 = -1; d2 <= 1; ++d2) {
                const nc2 = c2 + d2;
                const val = dfs(r + 1, nc1, nc2);
                if (val > bestNext) bestNext = val;
            }
        }

        cur += bestNext;
        memo[r][c1][c2] = cur;
        return cur;
    }

    return dfs(0, 0, n - 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function cherryPickup($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $negInf = -1000000000;

        // Initialize dp for the first row
        $dp = array_fill(0, $cols, array_fill(0, $cols, $negInf));
        $initial = $grid[0][0];
        if ($cols > 1) {
            $initial += $grid[0][$cols - 1];
        }
        $dp[0][$cols - 1] = $initial;

        // Directions robots can move: stay, left, right
        $dirs = [-1, 0, 1];

        for ($r = 1; $r < $rows; $r++) {
            $newDp = array_fill(0, $cols, array_fill(0, $cols, $negInf));
            for ($c1 = 0; $c1 < $cols; $c1++) {
                for ($c2 = 0; $c2 < $cols; $c2++) {
                    if ($dp[$c1][$c2] == $negInf) continue;
                    foreach ($dirs as $d1) {
                        $nc1 = $c1 + $d1;
                        if ($nc1 < 0 || $nc1 >= $cols) continue;
                        foreach ($dirs as $d2) {
                            $nc2 = $c2 + $d2;
                            if ($nc2 < 0 || $nc2 >= $cols) continue;

                            $gain = $grid[$r][$nc1];
                            if ($nc1 != $nc2) {
                                $gain += $grid[$r][$nc2];
                            }

                            $candidate = $dp[$c1][$c2] + $gain;
                            if ($candidate > $newDp[$nc1][$nc2]) {
                                $newDp[$nc1][$nc2] = $candidate;
                            }
                        }
                    }
                }
            }
            $dp = $newDp;
        }

        // Find the maximum value in dp after processing all rows
        $result = 0;
        for ($c1 = 0; $c1 < $cols; $c1++) {
            for ($c2 = 0; $c2 < $cols; $c2++) {
                if ($dp[$c1][$c2] > $result) {
                    $result = $dp[$c1][$c2];
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func cherryPickup(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        let cols = grid[0].count
        var memo = Array(repeating: Array(repeating: Array(repeating: -1, count: cols), count: cols), count: rows)
        let INF_NEG = -1_000_000_000

        func dfs(_ r: Int, _ c1: Int, _ c2: Int) -> Int {
            if c1 < 0 || c1 >= cols || c2 < 0 || c2 >= cols { return INF_NEG }
            if memo[r][c1][c2] != -1 { return memo[r][c1][c2] }

            var cur = grid[r][c1]
            if c1 != c2 {
                cur += grid[r][c2]
            }

            if r == rows - 1 {
                memo[r][c1][c2] = cur
                return cur
            }

            var bestNext = INF_NEG
            for dc1 in -1...1 {
                for dc2 in -1...1 {
                    let next = dfs(r + 1, c1 + dc1, c2 + dc2)
                    if next > bestNext {
                        bestNext = next
                    }
                }
            }

            cur += bestNext
            memo[r][c1][c2] = cur
            return cur
        }

        return dfs(0, 0, cols - 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun cherryPickup(grid: Array<IntArray>): Int {
        val rows = grid.size
        val cols = grid[0].size
        val dp = Array(rows) { Array(cols) { IntArray(cols) { -1 } } }

        fun dfs(r: Int, c1: Int, c2: Int): Int {
            if (c1 !in 0 until cols || c2 !in 0 until cols) return Int.MIN_VALUE
            if (dp[r][c1][c2] != -1) return dp[r][c1][c2]

            var cur = grid[r][c1]
            if (c1 != c2) cur += grid[r][c2]

            if (r < rows - 1) {
                var bestNext = Int.MIN_VALUE
                for (dc1 in -1..1) {
                    for (dc2 in -1..1) {
                        val next = dfs(r + 1, c1 + dc1, c2 + dc2)
                        if (next > bestNext) bestNext = next
                    }
                }
                cur += bestNext
            }

            dp[r][c1][c2] = cur
            return cur
        }

        return dfs(0, 0, cols - 1)
    }
}
```

## Dart

```dart
class Solution {
  int cherryPickup(List<List<int>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    List<List<List<int>>> dp = List.generate(
        rows, (_) => List.generate(cols, (_) => List.filled(cols, -1)));

    int dfs(int r, int c1, int c2) {
      if (c1 < 0 || c1 >= cols || c2 < 0 || c2 >= cols) {
        return -1000000000;
      }
      if (dp[r][c1][c2] != -1) {
        return dp[r][c1][c2];
      }
      int result = grid[r][c1];
      if (c1 != c2) result += grid[r][c2];
      if (r == rows - 1) {
        dp[r][c1][c2] = result;
        return result;
      }
      int maxNext = -1000000000;
      for (int dc1 = -1; dc1 <= 1; ++dc1) {
        for (int dc2 = -1; dc2 <= 1; ++dc2) {
          int nc1 = c1 + dc1;
          int nc2 = c2 + dc2;
          if (nc1 < 0 || nc1 >= cols || nc2 < 0 || nc2 >= cols) continue;
          int temp = dfs(r + 1, nc1, nc2);
          if (temp > maxNext) {
            maxNext = temp;
          }
        }
      }
      result += maxNext;
      dp[r][c1][c2] = result;
      return result;
    }

    return dfs(0, 0, cols - 1);
  }
}
```

## Golang

```go
func cherryPickup(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])

    // dp[row][col1][col2] = max cherries from this state
    dp := make([][][]int, rows)
    for i := 0; i < rows; i++ {
        dp[i] = make([][]int, cols)
        for j := 0; j < cols; j++ {
            dp[i][j] = make([]int, cols)
            for k := 0; k < cols; k++ {
                dp[i][j][k] = -1
            }
        }
    }

    var dfs func(r, c1, c2 int) int
    dfs = func(r, c1, c2 int) int {
        if c1 < 0 || c1 >= cols || c2 < 0 || c2 >= cols {
            return 0
        }
        if dp[r][c1][c2] != -1 {
            return dp[r][c1][c2]
        }

        cur := grid[r][c1]
        if c1 != c2 {
            cur += grid[r][c2]
        }

        if r < rows-1 {
            bestNext := 0
            for d1 := -1; d1 <= 1; d1++ {
                nc1 := c1 + d1
                if nc1 < 0 || nc1 >= cols {
                    continue
                }
                for d2 := -1; d2 <= 1; d2++ {
                    nc2 := c2 + d2
                    if nc2 < 0 || nc2 >= cols {
                        continue
                    }
                    val := dfs(r+1, nc1, nc2)
                    if val > bestNext {
                        bestNext = val
                    }
                }
            }
            cur += bestNext
        }

        dp[r][c1][c2] = cur
        return cur
    }

    return dfs(0, 0, cols-1)
}
```

## Ruby

```ruby
def cherry_pickup(grid)
  rows = grid.size
  cols = grid[0].size
  dp = Array.new(rows) { Array.new(cols) { Array.new(cols) } }

  dfs = nil
  dfs = lambda do |r, c1, c2|
    return 0 if r == rows
    memo = dp[r][c1][c2]
    return memo unless memo.nil?

    cur = grid[r][c1]
    cur += grid[r][c2] if c1 != c2

    max_next = -Float::INFINITY
    (-1..1).each do |d1|
      nc1 = c1 + d1
      next unless nc1.between?(0, cols - 1)
      (-1..1).each do |d2|
        nc2 = c2 + d2
        next unless nc2.between?(0, cols - 1)
        val = dfs.call(r + 1, nc1, nc2)
        max_next = val if val > max_next
      end
    end

    cur += max_next
    dp[r][c1][c2] = cur
  end

  dfs.call(0, 0, cols - 1)
end
```

## Scala

```scala
object Solution {
    def cherryPickup(grid: Array[Array[Int]]): Int = {
        val rows = grid.length
        val cols = grid(0).length
        val dp = Array.fill(rows, cols, cols)(-1)

        def dfs(r: Int, c1: Int, c2: Int): Int = {
            if (c1 < 0 || c1 >= cols || c2 < 0 || c2 >= cols) return Int.MinValue
            if (dp(r)(c1)(c2) != -1) return dp(r)(c1)(c2)

            var best = Int.MinValue
            for (d1 <- -1 to 1) {
                val nc1 = c1 + d1
                if (nc1 >= 0 && nc1 < cols) {
                    for (d2 <- -1 to 1) {
                        val nc2 = c2 + d2
                        if (nc2 >= 0 && nc2 < cols) {
                            val next = if (r == rows - 1) 0 else dfs(r + 1, nc1, nc2)
                            best = math.max(best, next)
                        }
                    }
                }
            }

            val cur = grid(r)(c1) + (if (c1 != c2) grid(r)(c2) else 0) + (if (best == Int.MinValue) 0 else best)
            dp(r)(c1)(c2) = cur
            cur
        }

        dfs(0, 0, cols - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut dp = vec![vec![i32::MIN; cols]; cols];
        for c1 in 0..cols {
            for c2 in 0..cols {
                if c1 == c2 {
                    dp[c1][c2] = grid[0][c1];
                } else {
                    dp[c1][c2] = grid[0][c1] + grid[0][c2];
                }
            }
        }
        for r in 1..rows {
            let mut ndp = vec![vec![i32::MIN; cols]; cols];
            for c1 in 0..cols {
                for c2 in 0..cols {
                    for dc1 in -1..=1 {
                        let pc1 = c1 as i32 + dc1;
                        if pc1 < 0 || pc1 >= cols as i32 { continue; }
                        for dc2 in -1..=1 {
                            let pc2 = c2 as i32 + dc2;
                            if pc2 < 0 || pc2 >= cols as i32 { continue; }
                            let prev = dp[pc1 as usize][pc2 as usize];
                            if prev == i32::MIN { continue; }
                            let mut val = prev + grid[r][c1];
                            if c1 != c2 {
                                val += grid[r][c2];
                            }
                            if val > ndp[c1][c2] {
                                ndp[c1][c2] = val;
                            }
                        }
                    }
                }
            }
            dp = ndp;
        }
        let mut ans = 0;
        for row in dp.iter() {
            for &v in row.iter() {
                if v > ans { ans = v; }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (cherry-pickup grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (zero? rows) 0 (length (first grid))))
         (dp   (make-vector rows)))
    ;; initialize 3‑dim memo table with #f
    (for ([i rows])
      (vector-set! dp i (make-vector cols))
      (for ([j cols])
        (vector-set! (vector-ref dp i) j (make-vector cols #f))))
    (letrec ((dfs
              (lambda (i j1 j2)
                (define memo (vector-ref (vector-ref (vector-ref dp i) j1) j2))
                (if memo
                    memo
                    (let* ((curr (+ (list-ref (list-ref grid i) j1)
                                    (if (= j1 j2) 0 (list-ref (list-ref grid i) j2)))))
                      (define best
                        (if (= i (- rows 1))
                            curr
                            (let loop ((d1 -1) (best -1))
                              (if (> d1 1)
                                  best
                                  (let inner ((d2 -1) (b best))
                                    (if (> d2 1)
                                        (loop (+ d1 1) b)
                                        (let* ((nj1 (+ j1 d1))
                                               (nj2 (+ j2 d2)))
                                          (if (and (>= nj1 0) (< nj1 cols)
                                                   (>= nj2 0) (< nj2 cols))
                                              (let ((val (dfs (+ i 1) nj1 nj2)))
                                                (inner (+ d2 1) (max b (+ curr val))))
                                              (inner (+ d2 1) b))))))))))
                      (vector-set! (vector-ref (vector-ref dp i) j1) j2 best)
                      best)))))
      (dfs 0 0 (- cols 1)))))
```

## Erlang

```erlang
-spec cherry_pickup([[integer()]]) -> integer().
cherry_pickup(Grid) ->
    Rows = length(Grid),
    Cols = length(hd(Grid)),
    StartVal = (lists:nth(1, hd(Grid))) + (lists:nth(Cols, hd(Grid))),
    InitMap = maps:put({0, Cols-1}, StartVal, #{}),
    process_rows(1, Rows, Grid, InitMap).

process_rows(RowIdx, TotalRows, _Grid, Map) when RowIdx == TotalRows ->
    max_in_map(Map);
process_rows(RowIdx, TotalRows, Grid, PrevMap) ->
    Row = lists:nth(RowIdx + 1, Grid),
    NewMap = maps:fold(
        fun({J, K}, Val, Acc) ->
            lists:foldl(
                fun(Dj, A1) ->
                    J2 = J + Dj,
                    if
                        J2 < 0; J2 >= length(Row) -> A1;
                        true ->
                            lists:foldl(
                                fun(Dk, A2) ->
                                    K2 = K + Dk,
                                    if
                                        K2 < 0; K2 >= length(Row) -> A2;
                                        true ->
                                            Sum = Val + elem_at(Row, J2) +
                                                  (if J2 == K2 -> 0 else elem_at(Row, K2) end),
                                            Key = {J2, K2},
                                            Prev = maps:get(Key, A2, -1),
                                            NewVal = if Sum > Prev -> Sum; true -> Prev end,
                                            maps:put(Key, NewVal, A2)
                                    end
                                end,
                                A1,
                                [-1, 0, 1]
                            )
                    end
                end,
                Acc,
                [-1, 0, 1]
            )
        end,
        #{},
        PrevMap
    ),
    process_rows(RowIdx + 1, TotalRows, Grid, NewMap).

elem_at(Row, Col) ->
    lists:nth(Col + 1, Row).

max_in_map(Map) ->
    maps:fold(fun(_K, V, Acc) -> if V > Acc -> V; true -> Acc end end, 0, Map).
```

## Elixir

```elixir
defmodule Solution do
  @spec cherry_pickup(grid :: [[integer]]) :: integer
  def cherry_pickup(grid) do
    m = length(grid)
    n = length(hd(grid))

    # DP for the last row
    last_row = List.last(grid)

    dp_next =
      for j <- 0..(n - 1) do
        for k <- 0..(n - 1) do
          base = Enum.at(last_row, j)
          if j != k, do: base + Enum.at(last_row, k), else: base
        end
      end

    # Process rows from bottom-2 up to top
    dp =
      Enum.reduce(Enum.reverse(0..(m - 2)), dp_next, fn i, dp_next_acc ->
        row = Enum.at(grid, i)

        for j <- 0..(n - 1) do
          for k <- 0..(n - 1) do
            cur =
              if j != k,
                do: Enum.at(row, j) + Enum.at(row, k),
                else: Enum.at(row, j)

            max_next =
              for d1 <- -1..1,
                  d2 <- -1..1,
                  nj = j + d1,
                  nk = k + d2,
                  nj >= 0,
                  nj < n,
                  nk >= 0,
                  nk < n do
                Enum.at(Enum.at(dp_next_acc, nj), nk)
              end
              |> Enum.max()

            cur + max_next
          end
        end
      end)

    # Starting positions are (0, 0) and (0, n-1)
    Enum.at(Enum.at(dp, 0), n - 1)
  end
end
```

# 0063. Unique Paths II

## Cpp

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<int> dp(n, 0);
        dp[0] = (obstacleGrid[0][0] == 0) ? 1 : 0;
        for (int i = 0; i < m; ++i) {
            // update first column for current row
            if (obstacleGrid[i][0] == 1) dp[0] = 0;
            else if (i > 0) dp[0] = dp[0]; // unchanged if no obstacle
            for (int j = 1; j < n; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp[n - 1];
    }
};
```

## Java

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        dp[0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else if (j > 0) {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[-1]
```

## Python3

```python
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j - 1]
        return dp[-1]
```

## C

```c
int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize){
    if (obstacleGridSize == 0) return 0;
    int m = obstacleGridSize;
    int n = obstacleGridColSize[0];
    int *dp = (int*)malloc(n * sizeof(int));
    for (int j = 0; j < n; ++j) dp[j] = 0;

    dp[0] = (obstacleGrid[0][0] == 0) ? 1 : 0;
    for (int j = 1; j < n; ++j){
        if (obstacleGrid[0][j] == 1) dp[j] = 0;
        else dp[j] = dp[j - 1];
    }

    for (int i = 1; i < m; ++i){
        if (obstacleGrid[i][0] == 1) dp[0] = 0;
        // else dp[0] remains as paths from above
        for (int j = 1; j < n; ++j){
            if (obstacleGrid[i][j] == 1) dp[j] = 0;
            else dp[j] = dp[j] + dp[j - 1];
        }
    }

    int result = dp[n - 1];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int UniquePathsWithObstacles(int[][] obstacleGrid)
    {
        int m = obstacleGrid.Length;
        int n = obstacleGrid[0].Length;
        int[] dp = new int[n];
        dp[0] = obstacleGrid[0][0] == 0 ? 1 : 0;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (obstacleGrid[i][j] == 1)
                {
                    dp[j] = 0;
                }
                else if (j > 0)
                {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return dp[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const dp = new Array(n).fill(0);
    
    // Initialize first cell
    dp[0] = obstacleGrid[0][0] === 0 ? 1 : 0;
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (obstacleGrid[i][j] === 1) {
                dp[j] = 0; // obstacle blocks any path to this cell
            } else if (j > 0) {
                dp[j] += dp[j - 1]; // paths from left + paths from top (dp[j])
            }
        }
    }
    
    return dp[n - 1];
};
```

## Typescript

```typescript
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const dp = new Array<number>(n).fill(0);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (obstacleGrid[i][j] === 1) {
                dp[j] = 0;
            } else if (i === 0 && j === 0) {
                dp[0] = 1;
            } else {
                const up = dp[j];
                const left = j > 0 ? dp[j - 1] : 0;
                dp[j] = up + left;
            }
        }
    }
    return dp[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $obstacleGrid
     * @return Integer
     */
    function uniquePathsWithObstacles($obstacleGrid) {
        $m = count($obstacleGrid);
        if ($m == 0) return 0;
        $n = count($obstacleGrid[0]);
        $dp = array_fill(0, $n, 0);
        $dp[0] = ($obstacleGrid[0][0] == 0) ? 1 : 0;

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($obstacleGrid[$i][$j] == 1) {
                    $dp[$j] = 0;
                } else {
                    if ($j > 0) {
                        $dp[$j] += $dp[$j - 1];
                    }
                }
            }
        }

        return $dp[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func uniquePathsWithObstacles(_ obstacleGrid: [[Int]]) -> Int {
        let m = obstacleGrid.count
        guard m > 0 else { return 0 }
        let n = obstacleGrid[0].count
        var dp = Array(repeating: 0, count: n)
        dp[0] = obstacleGrid[0][0] == 0 ? 1 : 0
        
        for i in 0..<m {
            for j in 0..<n {
                if obstacleGrid[i][j] == 1 {
                    dp[j] = 0
                } else if j > 0 {
                    dp[j] += dp[j - 1]
                }
            }
        }
        return dp[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uniquePathsWithObstacles(obstacleGrid: Array<IntArray>): Int {
        val m = obstacleGrid.size
        val n = obstacleGrid[0].size
        val dp = IntArray(n)
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0
                } else if (i == 0 && j == 0) {
                    dp[j] = 1
                } else {
                    val up = dp[j]
                    val left = if (j > 0) dp[j - 1] else 0
                    dp[j] = up + left
                }
            }
        }
        return dp[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int uniquePathsWithObstacles(List<List<int>> obstacleGrid) {
    final int m = obstacleGrid.length;
    final int n = obstacleGrid[0].length;

    // If starting cell has an obstacle, there is no path.
    if (obstacleGrid[0][0] == 1) return 0;

    List<List<int>> dp = List.generate(m, (_) => List.filled(n, 0));
    dp[0][0] = 1;

    // Initialize first row.
    for (int j = 1; j < n; ++j) {
      if (obstacleGrid[0][j] == 0 && dp[0][j - 1] != 0) {
        dp[0][j] = 1;
      }
    }

    // Initialize first column.
    for (int i = 1; i < m; ++i) {
      if (obstacleGrid[i][0] == 0 && dp[i - 1][0] != 0) {
        dp[i][0] = 1;
      }
    }

    // Fill the rest of dp table.
    for (int i = 1; i < m; ++i) {
      for (int j = 1; j < n; ++j) {
        if (obstacleGrid[i][j] == 0) {
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        } // else remains 0
      }
    }

    return dp[m - 1][n - 1];
  }
}
```

## Golang

```go
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    m := len(obstacleGrid)
    if m == 0 {
        return 0
    }
    n := len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 || obstacleGrid[m-1][n-1] == 1 {
        return 0
    }

    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
    }
    dp[0][0] = 1

    // first row
    for j := 1; j < n; j++ {
        if obstacleGrid[0][j] == 1 {
            dp[0][j] = 0
        } else {
            dp[0][j] = dp[0][j-1]
        }
    }

    // first column
    for i := 1; i < m; i++ {
        if obstacleGrid[i][0] == 1 {
            dp[i][0] = 0
        } else {
            dp[i][0] = dp[i-1][0]
        }
    }

    // rest of the grid
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            if obstacleGrid[i][j] == 1 {
                dp[i][j] = 0
            } else {
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            }
        }
    }

    return dp[m-1][n-1]
}
```

## Ruby

```ruby
def unique_paths_with_obstacles(obstacle_grid)
  m = obstacle_grid.size
  return 0 if m == 0
  n = obstacle_grid[0].size
  dp = Array.new(n, 0)
  dp[0] = 1 unless obstacle_grid[0][0] == 1

  (0...m).each do |i|
    (0...n).each do |j|
      if obstacle_grid[i][j] == 1
        dp[j] = 0
      else
        dp[j] += dp[j - 1] if j > 0
      end
    end
  end

  dp[n - 1]
end
```

## Scala

```scala
object Solution {
    def uniquePathsWithObstacles(obstacleGrid: Array[Array[Int]]): Int = {
        val m = obstacleGrid.length
        if (m == 0) return 0
        val n = obstacleGrid(0).length
        val dp = Array.ofDim[Int](m, n)

        // start cell
        dp(0)(0) = if (obstacleGrid(0)(0) == 0) 1 else 0

        // first row
        var j = 1
        while (j < n) {
            dp(0)(j) = if (obstacleGrid(0)(j) == 0) dp(0)(j - 1) else 0
            j += 1
        }

        // first column
        var i = 1
        while (i < m) {
            dp(i)(0) = if (obstacleGrid(i)(0) == 0) dp(i - 1)(0) else 0
            i += 1
        }

        // rest of the grid
        i = 1
        while (i < m) {
            j = 1
            while (j < n) {
                if (obstacleGrid(i)(j) == 0) {
                    dp(i)(j) = dp(i - 1)(j) + dp(i)(j - 1)
                } else {
                    dp(i)(j) = 0
                }
                j += 1
            }
            i += 1
        }

        dp(m - 1)(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut dp = vec![0i32; n];
        for i in 0..m {
            for j in 0..n {
                if obstacle_grid[i][j] == 1 {
                    dp[j] = 0;
                } else if i == 0 && j == 0 {
                    dp[j] = 1;
                } else {
                    let up = if i > 0 { dp[j] } else { 0 };
                    let left = if j > 0 { dp[j - 1] } else { 0 };
                    dp[j] = up + left;
                }
            }
        }
        dp[n - 1]
    }
}
```

## Racket

```racket
(define/contract (unique-paths-with-obstacles obstacleGrid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length obstacleGrid))
         (n (if (zero? m) 0 (length (first obstacleGrid))))
         (obs (list->vector (map list->vector obstacleGrid)))
         (dp (make-vector m)))
    (for ([i (in-range m)])
      (vector-set! dp i (make-vector n 0)))
    (if (= (vector-ref (vector-ref obs 0) 0) 1)
        0
        (begin
          (vector-set! (vector-ref dp 0) 0 1)
          ;; first row
          (for ([j (in-range 1 n)])
            (if (= (vector-ref (vector-ref obs 0) j) 1)
                (vector-set! (vector-ref dp 0) j 0)
                (vector-set! (vector-ref dp 0) j
                             (vector-ref (vector-ref dp 0) (- j 1)))))
          ;; first column
          (for ([i (in-range 1 m)])
            (if (= (vector-ref (vector-ref obs i) 0) 1)
                (vector-set! (vector-ref dp i) 0 0)
                (vector-set! (vector-ref dp i) 0
                             (vector-ref (vector-ref dp (- i 1)) 0))))
          ;; rest cells
          (for ([i (in-range 1 m)])
            (for ([j (in-range 1 n)])
              (if (= (vector-ref (vector-ref obs i) j) 1)
                  (vector-set! (vector-ref dp i) j 0)
                  (let ((val (+ (vector-ref (vector-ref dp (- i 1)) j)
                                (vector-ref (vector-ref dp i) (- j 1)))))
                    (vector-set! (vector-ref dp i) j val)))))
          (vector-ref (vector-ref dp (- m 1)) (- n 1))))))
```

## Erlang

```erlang
-module(solution).
-export([unique_paths_with_obstacles/1]).

-spec unique_paths_with_obstacles(ObstacleGrid :: [[integer()]]) -> integer().
unique_paths_with_obstacles(ObstacleGrid) ->
    case ObstacleGrid of
        [] -> 0;
        [FirstObsRow | RestRows] ->
            case hd(FirstObsRow) of
                1 -> 0;
                0 ->
                    FirstDPRow = build_first_row(tl(FirstObsRow), 1, [1]),
                    FinalDPRow = lists:foldl(fun(Row, PrevDP) ->
                        compute_dp_row(Row, PrevDP)
                    end, FirstDPRow, RestRows),
                    case FinalDPRow of
                        [] -> 0;
                        _ -> lists:last(FinalDPRow)
                    end
            end
    end.

build_first_row([], _PrevLeft, Acc) ->
    lists:reverse(Acc);
build_first_row([Obs|Rest], PrevLeft, Acc) ->
    NewVal = case Obs of
        1 -> 0;
        0 -> PrevLeft
    end,
    build_first_row(Rest, NewVal, [NewVal | Acc]).

compute_dp_row([Obs|RestObs], [Up|RestUp]) ->
    FirstVal = case Obs of
        1 -> 0;
        0 -> Up
    end,
    compute_rest(RestObs, RestUp, FirstVal, [FirstVal]).

compute_rest([], [], _LeftPrev, Acc) ->
    lists:reverse(Acc);
compute_rest([Obs|Os], [Up|Us], LeftPrev, Acc) ->
    Val = case Obs of
        1 -> 0;
        0 -> Up + LeftPrev
    end,
    compute_rest(Os, Us, Val, [Val | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec unique_paths_with_obstacles(obstacle_grid :: [[integer]]) :: integer
  def unique_paths_with_obstacles(obstacle_grid) do
    # dimensions
    n = obstacle_grid |> hd() |> length()

    # if starting cell is blocked, no paths exist
    if List.first(List.first(obstacle_grid)) == 1 do
      0
    else
      final_dp =
        Enum.reduce(Enum.with_index(obstacle_grid), List.duplicate(0, n), fn {row, i}, prev_dp ->
          cur_rev =
            Enum.reduce(Enum.with_index(row), {[], nil}, fn {cell, j}, {acc_rev, _} ->
              val =
                if cell == 1 do
                  0
                else
                  cond do
                    i == 0 and j == 0 -> 1
                    true ->
                      top = if i > 0, do: Enum.at(prev_dp, j), else: 0
                      left = if j > 0, do: hd(acc_rev), else: 0
                      top + left
                  end
                end

              {[val | acc_rev], nil}
            end)
            |> elem(0)

          Enum.reverse(cur_rev)
        end)

      List.last(final_dp)
    end
  end
end
```

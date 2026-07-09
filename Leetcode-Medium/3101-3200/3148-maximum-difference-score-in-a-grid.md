# 3148. Maximum Difference Score in a Grid

## Cpp

```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        const int INF = 1e9 + 7;
        vector<int> minPref(n, INF); // min value in rectangle (0..i-1, 0..j)
        int ans = INT_MIN;
        for (int i = 0; i < m; ++i) {
            int leftMin = INF; // min value in current row up to column j-1
            for (int j = 0; j < n; ++j) {
                int cur = grid[i][j];
                int upMin = minPref[j];               // rectangle above current cell
                int startMin = min(upMin, leftMin);    // best starting cell before (i,j)
                if (startMin != INF) {
                    ans = max(ans, cur - startMin);
                }
                // update minima for future cells
                leftMin = min(leftMin, cur);
                minPref[j] = min({cur, upMin, leftMin});
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxScore(List<List<Integer>> grid) {
        int m = grid.size();
        int n = grid.get(0).size();
        int[][] suffixMax = new int[m][n];
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                int cur = grid.get(i).get(j);
                int best = cur;
                if (i + 1 < m) best = Math.max(best, suffixMax[i + 1][j]);
                if (j + 1 < n) best = Math.max(best, suffixMax[i][j + 1]);
                suffixMax[i][j] = best;
            }
        }
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int future = Integer.MIN_VALUE;
                if (i + 1 < m) future = Math.max(future, suffixMax[i + 1][j]);
                if (j + 1 < n) future = Math.max(future, suffixMax[i][j + 1]);
                if (future != Integer.MIN_VALUE) {
                    ans = Math.max(ans, future - grid.get(i).get(j));
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        min_val = grid[0][0]
        ans = -10**9  # sufficiently small
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                diff = grid[i][j] - min_val
                if diff > ans:
                    ans = diff
                if grid[i][j] < min_val:
                    min_val = grid[i][j]
        return ans
```

## Python3

```python
class Solution:
    def maxScore(self, grid):
        m, n = len(grid), len(grid[0])
        INF_NEG = -10**9
        ans = INF_NEG
        down = [INF_NEG] * n  # dp for row i+1
        
        for i in range(m - 1, -1, -1):
            cur = [INF_NEG] * n
            for j in range(n - 1, -1, -1):
                max_down = down[j]
                max_right = cur[j + 1] if j + 1 < n else INF_NEG
                neighbor_max = max(max_down, max_right)
                if neighbor_max != INF_NEG:
                    ans = max(ans, neighbor_max - grid[i][j])
                cur[j] = max(grid[i][j], max_down, max_right)
            down = cur
        return ans
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int maxScore(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int n = gridColSize[0];
    int *dp = (int *)malloc(n * sizeof(int));
    for (int j = 0; j < n; ++j) dp[j] = INT_MAX;

    int ans = INT_MIN;

    for (int i = 0; i < gridSize; ++i) {
        int leftMin = INT_MAX;
        for (int j = 0; j < n; ++j) {
            int upMin = dp[j];
            int minPrev = (upMin < leftMin) ? upMin : leftMin;
            if (minPrev != INT_MAX) {
                int diff = grid[i][j] - minPrev;
                if (diff > ans) ans = diff;
            }
            int curMin = grid[i][j];
            if (upMin < curMin) curMin = upMin;
            if (leftMin < curMin) curMin = leftMin;
            dp[j] = curMin;
            leftMin = curMin;
        }
    }

    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxScore(IList<IList<int>> grid) {
        int m = grid.Count;
        int n = grid[0].Count;
        int[,] best = new int[m, n];
        int ans = int.MinValue;

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int maxNext = int.MinValue;
                if (i + 1 < m) maxNext = Math.Max(maxNext, best[i + 1, j]);
                if (j + 1 < n) maxNext = Math.Max(maxNext, best[i, j + 1]);

                if (maxNext != int.MinValue) {
                    ans = Math.Max(ans, maxNext - grid[i][j]);
                }

                // best value reachable from (i,j), including itself
                best[i, j] = Math.Max(grid[i][j], maxNext == int.MinValue ? grid[i][j] : maxNext);
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxScore = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const pref = Array.from({ length: m }, () => new Array(n).fill(Infinity));
    let ans = -Infinity;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            // minimum value among cells strictly above or left of (i,j)
            let minPrev = Infinity;
            if (i > 0) minPrev = Math.min(minPrev, pref[i - 1][j]);
            if (j > 0) minPrev = Math.min(minPrev, pref[i][j - 1]);

            if (minPrev !== Infinity) {
                ans = Math.max(ans, grid[i][j] - minPrev);
            }

            // prefix minimum up to (i,j), inclusive
            let curMin = grid[i][j];
            if (i > 0) curMin = Math.min(curMin, pref[i - 1][j]);
            if (j > 0) curMin = Math.min(curMin, pref[i][j - 1]);
            pref[i][j] = curMin;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxScore(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let minVal = Infinity;
    let maxDiff = -Infinity;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) {
                minVal = Math.min(minVal, grid[i][j]);
                continue;
            }
            const diff = grid[i][j] - minVal;
            if (diff > maxDiff) maxDiff = diff;
            if (grid[i][j] < minVal) minVal = grid[i][j];
        }
    }

    return maxDiff;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxScore($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        // prefix minimum matrix
        $prefMin = array_fill(0, $m, array_fill(0, $n, 0));
        $ans = -PHP_INT_MAX;

        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $cur = $grid[$i][$j];
                if ($i > 0 || $j > 0) {
                    $minPrev = PHP_INT_MAX;
                    if ($i > 0) {
                        $minPrev = min($minPrev, $prefMin[$i - 1][$j]);
                    }
                    if ($j > 0) {
                        $minPrev = min($minPrev, $prefMin[$i][$j - 1]);
                    }
                    $diff = $cur - $minPrev;
                    if ($diff > $ans) {
                        $ans = $diff;
                    }
                }

                // update prefix minimum for (i,j)
                $val = $cur;
                if ($i > 0) {
                    $val = min($val, $prefMin[$i - 1][$j]);
                }
                if ($j > 0) {
                    $val = min($val, $prefMin[$i][$j - 1]);
                }
                $prefMin[$i][$j] = $val;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var minSoFar = Int.max
        var best = Int.min
        
        for i in 0..<m {
            for j in 0..<n {
                if !(i == 0 && j == 0) {
                    let diff = grid[i][j] - minSoFar
                    if diff > best { best = diff }
                }
                if grid[i][j] < minSoFar {
                    minSoFar = grid[i][j]
                }
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(grid: List<List<Int>>): Int {
        val m = grid.size
        val n = grid[0].size
        val minVal = Array(m) { IntArray(n) }
        var ans = Int.MIN_VALUE
        for (i in 0 until m) {
            for (j in 0 until n) {
                val cur = grid[i][j]
                if (i == 0 && j == 0) {
                    minVal[0][0] = cur
                } else {
                    var prevMin = Int.MAX_VALUE
                    if (i > 0) prevMin = kotlin.math.min(prevMin, minVal[i - 1][j])
                    if (j > 0) prevMin = kotlin.math.min(prevMin, minVal[i][j - 1])
                    ans = kotlin.math.max(ans, cur - prevMin)
                    var curMin = cur
                    if (i > 0) curMin = kotlin.math.min(curMin, minVal[i - 1][j])
                    if (j > 0) curMin = kotlin.math.min(curMin, minVal[i][j - 1])
                    minVal[i][j] = curMin
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<int>> prefMin = List.generate(m, (_) => List.filled(n, 0));
    int ans = -1000000000; // sufficiently small
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == 0 && j == 0) {
          prefMin[0][0] = grid[0][0];
          continue;
        }
        int minPrev;
        if (i == 0) {
          minPrev = prefMin[i][j - 1];
        } else if (j == 0) {
          minPrev = prefMin[i - 1][j];
        } else {
          minPrev = prefMin[i - 1][j] < prefMin[i][j - 1]
              ? prefMin[i - 1][j]
              : prefMin[i][j - 1];
        }
        int cand = grid[i][j] - minPrev;
        if (cand > ans) ans = cand;

        int curMin = grid[i][j];
        if (i > 0 && prefMin[i - 1][j] < curMin) curMin = prefMin[i - 1][j];
        if (j > 0 && prefMin[i][j - 1] < curMin) curMin = prefMin[i][j - 1];
        prefMin[i][j] = curMin;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxScore(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])

	minPref := make([][]int, m)
	for i := 0; i < m; i++ {
		minPref[i] = make([]int, n)
	}

	const negInf = -1 << 60
	ans := negInf

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				minPref[i][j] = grid[i][j]
				continue
			}

			var minPrev int
			if i > 0 && j > 0 {
				a, b := minPref[i-1][j], minPref[i][j-1]
				if a < b {
					minPrev = a
				} else {
					minPrev = b
				}
			} else if i > 0 {
				minPrev = minPref[i-1][j]
			} else { // j > 0
				minPrev = minPref[i][j-1]
			}

			if diff := grid[i][j] - minPrev; diff > ans {
				ans = diff
			}

			curMin := grid[i][j]
			if i > 0 && minPref[i-1][j] < curMin {
				curMin = minPref[i-1][j]
			}
			if j > 0 && minPref[i][j-1] < curMin {
				curMin = minPref[i][j-1]
			}
			minPref[i][j] = curMin
		}
	}

	return ans
}
```

## Ruby

```ruby
def max_score(grid)
  m = grid.length
  n = grid[0].length
  min_val = Float::INFINITY
  best = -Float::INFINITY

  (0...m).each do |i|
    (0...n).each do |j|
      if i != 0 || j != 0
        diff = grid[i][j] - min_val
        best = diff if diff > best
      end
      val = grid[i][j]
      min_val = val if val < min_val
    end
  end

  best.to_i
end
```

## Scala

```scala
object Solution {
    def maxScore(grid: List[List[Int]]): Int = {
        val m = grid.length
        val n = grid.head.length
        // Convert to array for fast indexing
        val arr = Array.ofDim[Int](m, n)
        var i = 0
        while (i < m) {
            val row = grid(i)
            var j = 0
            while (j < n) {
                arr(i)(j) = row(j)
                j += 1
            }
            i += 1
        }

        var minVal = Int.MaxValue
        var maxDiff = Int.MinValue

        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                val cur = arr(i)(j)
                if (minVal != Int.MaxValue) {
                    val diff = cur - minVal
                    if (diff > maxDiff) maxDiff = diff
                }
                if (cur < minVal) minVal = cur
                j += 1
            }
            i += 1
        }

        maxDiff
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        // dp[i][j] = maximum value in subgrid with top-left corner (i,j)
        let mut dp = vec![vec![0i32; n]; m];
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                let mut best = grid[i][j];
                if i + 1 < m {
                    best = best.max(dp[i + 1][j]);
                }
                if j + 1 < n {
                    best = best.max(dp[i][j + 1]);
                }
                dp[i][j] = best;
            }
        }

        let mut ans = i32::MIN;
        for i in 0..m {
            for j in 0..n {
                let mut next_max = i32::MIN;
                if i + 1 < m {
                    next_max = next_max.max(dp[i + 1][j]);
                }
                if j + 1 < n {
                    next_max = next_max.max(dp[i][j + 1]);
                }
                if next_max != i32::MIN {
                    let diff = next_max - grid[i][j];
                    ans = ans.max(diff);
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(require racket/vector)
(require racket/sequence)

(define/contract (max-score grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (> m 0) (length (first grid)) 0))
         (dp (make-vector m)))
    ;; initialize dp rows
    (for ([i (in-range m)])
      (vector-set! dp i (make-vector n 0)))
    (define ans -1000000000) ; sufficiently small
    (for ([i (in-range m)])
      (let ((row (list-ref grid i))
            (dp-row (vector-ref dp i)))
        (for ([j (in-range n)])
          (define cur (list-ref row j))
          (if (and (= i 0) (= j 0))
              (vector-set! dp-row j cur)
              (begin
                ;; compute minimum value in the rectangle up‑left excluding (i,j)
                (define minPrev +inf.0)
                (when (> i 0)
                  (set! minPrev (min minPrev (vector-ref (vector-ref dp (- i 1)) j))))
                (when (> j 0)
                  (set! minPrev (min minPrev (vector-ref dp-row (- j 1)))))
                ;; candidate answer
                (define cand (- cur minPrev))
                (when (> cand ans) (set! ans cand))
                ;; update dp[i][j] = minimum in rectangle up‑left including (i,j)
                (define best cur)
                (when (> i 0)
                  (set! best (min best (vector-ref (vector-ref dp (- i 1)) j))))
                (when (> j 0)
                  (set! best (min best (vector-ref dp-row (- j 1)))))
                (vector-set! dp-row j best)))))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([max_score/1]).

-spec max_score(Grid :: [[integer()]]) -> integer().
max_score(Grid) ->
    {MaxDiff, _} = lists:foldl(
        fun(Row, {CurMax, MinSoFar}) ->
            process_row(Row, CurMax, MinSoFar)
        end,
        {-1000000, undefined},
        Grid),
    MaxDiff.

process_row([], CurMax, MinSoFar) -> 
    {CurMax, MinSoFar};
process_row([Val | Rest], CurMax, MinSoFar) ->
    case MinSoFar of
        undefined ->
            NewMin = Val,
            process_row(Rest, CurMax, NewMin);
        _ ->
            Diff = Val - MinSoFar,
            NewMax = if Diff > CurMax -> Diff; true -> CurMax end,
            NewMin = if Val < MinSoFar -> Val; true -> MinSoFar end,
            process_row(Rest, NewMax, NewMin)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @inf 1_000_001

  @spec max_score(grid :: [[integer]]) :: integer
  def max_score(grid) do
    n = grid |> List.first() |> length()
    init_col_mins = List.duplicate(@inf, n)
    {_final_cols, ans} =
      Enum.reduce(grid, {init_col_mins, -@inf}, fn row, {col_mins, best} ->
        {new_col_mins, new_best} = process_row(row, col_mins, @inf, best, [])
        {new_col_mins, new_best}
      end)

    ans
  end

  defp process_row([], [], _left_min, best, rev_new) do
    {Enum.reverse(rev_new), best}
  end

  defp process_row([val | rest_vals], [old_min | rest_old], left_min, best, rev_new) do
    min_prev =
      if old_min == @inf and left_min == @inf do
        nil
      else
        min(old_min, left_min)
      end

    new_best =
      case min_prev do
        nil -> best
        _ -> max(best, val - min_prev)
      end

    new_left = min(left_min, val)
    new_col_min = min(old_min, val)

    process_row(rest_vals, rest_old, new_left, new_best, [new_col_min | rev_new])
  end
end
```

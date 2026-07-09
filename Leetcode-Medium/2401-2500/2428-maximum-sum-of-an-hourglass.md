# 2428. Maximum Sum of an Hourglass

## Cpp

```cpp
class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int best = 0;
        for (int i = 0; i + 2 < m; ++i) {
            for (int j = 0; j + 2 < n; ++j) {
                int cur = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                        + grid[i+1][j+1]
                        + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2];
                if (cur > best) best = cur;
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maxSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i <= m - 3; i++) {
            for (int j = 0; j <= n - 3; j++) {
                int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                        + grid[i + 1][j + 1]
                        + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2];
                if (sum > max) {
                    max = sum;
                }
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        max_sum = -1  # since all values are non-negative, any hourglass sum will be >=0
        for i in range(m - 2):
            row_i = grid[i]
            row_mid = grid[i + 1]
            row_bottom = grid[i + 2]
            for j in range(n - 2):
                cur = (row_i[j] + row_i[j + 1] + row_i[j + 2] +
                       row_mid[j + 1] +
                       row_bottom[j] + row_bottom[j + 1] + row_bottom[j + 2])
                if cur > max_sum:
                    max_sum = cur
        return max_sum
```

## Python3

```python
class Solution:
    def maxSum(self, grid):
        m, n = len(grid), len(grid[0])
        max_sum = 0
        first = True
        for i in range(m - 2):
            row_top = grid[i]
            row_mid = grid[i + 1]
            row_bot = grid[i + 2]
            for j in range(n - 2):
                cur = (row_top[j] + row_top[j + 1] + row_top[j + 2] +
                       row_mid[j + 1] +
                       row_bot[j] + row_bot[j + 1] + row_bot[j + 2])
                if first:
                    max_sum = cur
                    first = False
                elif cur > max_sum:
                    max_sum = cur
        return max_sum
```

## C

```c
int maxSum(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = gridColSize[0];
    int best = 0;
    // Compute first hourglass to initialize best
    best = grid[0][0] + grid[0][1] + grid[0][2]
         + grid[1][1]
         + grid[2][0] + grid[2][1] + grid[2][2];
    for (int i = 0; i <= rows - 3; ++i) {
        for (int j = 0; j <= cols - 3; ++j) {
            int cur = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                    + grid[i+1][j+1]
                    + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2];
            if (cur > best) best = cur;
        }
    }
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSum(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int max = int.MinValue;
        for (int i = 0; i <= m - 3; i++) {
            for (int j = 0; j <= n - 3; j++) {
                int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                        + grid[i + 1][j + 1]
                        + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2];
                if (sum > max) max = sum;
            }
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxSum = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let best = -Infinity;
    for (let i = 0; i <= m - 3; ++i) {
        for (let j = 0; j <= n - 3; ++j) {
            const sum =
                grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
                grid[i + 1][j + 1] +
                grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2];
            if (sum > best) best = sum;
        }
    }
    return best;
};
```

## Typescript

```typescript
function maxSum(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let best = -Infinity;
    for (let i = 0; i <= m - 3; i++) {
        for (let j = 0; j <= n - 3; j++) {
            const sum =
                grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
                grid[i + 1][j + 1] +
                grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2];
            if (sum > best) best = sum;
        }
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxSum($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $max = PHP_INT_MIN;
        for ($i = 0; $i <= $m - 3; $i++) {
            for ($j = 0; $j <= $n - 3; $j++) {
                $sum = $grid[$i][$j] + $grid[$i][$j+1] + $grid[$i][$j+2]
                     + $grid[$i+1][$j+1]
                     + $grid[$i+2][$j] + $grid[$i+2][$j+1] + $grid[$i+2][$j+2];
                if ($sum > $max) {
                    $max = $sum;
                }
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxSum(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var best = Int.min
        for i in 0..<(m - 2) {
            for j in 0..<(n - 2) {
                let sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                        + grid[i + 1][j + 1]
                        + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                if sum > best {
                    best = sum
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
    fun maxSum(grid: Array<IntArray>): Int {
        var max = Int.MIN_VALUE
        val rows = grid.size
        val cols = grid[0].size
        for (i in 0 until rows - 2) {
            for (j in 0 until cols - 2) {
                val sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
                          grid[i + 1][j + 1] +
                          grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                if (sum > max) max = sum
            }
        }
        return max
    }
}
```

## Dart

```dart
class Solution {
  int maxSum(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int maxVal = 0;
    for (int i = 0; i <= m - 3; i++) {
      for (int j = 0; j <= n - 3; j++) {
        int sum = grid[i][j] +
            grid[i][j + 1] +
            grid[i][j + 2] +
            grid[i + 1][j + 1] +
            grid[i + 2][j] +
            grid[i + 2][j + 1] +
            grid[i + 2][j + 2];
        if (sum > maxVal) {
          maxVal = sum;
        }
      }
    }
    return maxVal;
  }
}
```

## Golang

```go
func maxSum(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	maxVal := 0
	for i := 0; i <= m-3; i++ {
		for j := 0; j <= n-3; j++ {
			sum := grid[i][j] + grid[i][j+1] + grid[i][j+2] +
				grid[i+1][j+1] +
				grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
			if sum > maxVal {
				maxVal = sum
			}
		}
	}
	return maxVal
}
```

## Ruby

```ruby
def max_sum(grid)
  m = grid.length
  n = grid[0].length
  max_val = -1 << 60
  (0..m - 3).each do |i|
    (0..n - 3).each do |j|
      s = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
          grid[i + 1][j + 1] +
          grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
      max_val = s if s > max_val
    end
  end
  max_val
end
```

## Scala

```scala
object Solution {
    def maxSum(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        var best = Int.MinValue
        var i = 0
        while (i <= m - 3) {
            var j = 0
            while (j <= n - 3) {
                val sum = grid(i)(j) + grid(i)(j + 1) + grid(i)(j + 2) +
                          grid(i + 1)(j + 1) +
                          grid(i + 2)(j) + grid(i + 2)(j + 1) + grid(i + 2)(j + 2)
                if (sum > best) best = sum
                j += 1
            }
            i += 1
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut max_val = i32::MIN;
        for i in 0..m - 2 {
            for j in 0..n - 2 {
                let sum = grid[i][j]
                    + grid[i][j + 1]
                    + grid[i][j + 2]
                    + grid[i + 1][j + 1]
                    + grid[i + 2][j]
                    + grid[i + 2][j + 1]
                    + grid[i + 2][j + 2];
                if sum > max_val {
                    max_val = sum;
                }
            }
        }
        max_val
    }
}
```

## Racket

```racket
(define/contract (max-sum grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length grid)]
         [n (if (null? grid) 0 (length (car grid)))])
    (define (cell i j)
      (list-ref (list-ref grid i) j))
    (for/fold ([best -1]) ([i (in-range (- m 2))]
                           [j (in-range (- n 2))])
      (let* ([s (+ (cell i j)
                   (cell i (+ j 1))
                   (cell i (+ j 2))
                   (cell (+ i 1) (+ j 1))
                   (cell (+ i 2) j)
                   (cell (+ i 2) (+ j 1))
                   (cell (+ i 2) (+ j 2)))])
        (if (> s best) s best)))))
```

## Erlang

```erlang
-module(solution).
-export([max_sum/1]).

-spec max_sum(Grid :: [[integer()]]) -> integer().
max_sum(Grid) ->
    M = length(Grid),
    N = case Grid of [] -> 0; [Row|_] -> length(Row) end,
    max_sum_rows(Grid, M, N, 0, -1).

max_sum_rows(_Grid, M, _N, I, Max) when I > M-3 ->
    Max;
max_sum_rows(Grid, M, N, I, Max) ->
    NewMax = max_sum_cols(Grid, I, N, 0, Max),
    max_sum_rows(Grid, M, N, I + 1, NewMax).

max_sum_cols(_Grid, _I, N, J, CurMax) when J > N-3 ->
    CurMax;
max_sum_cols(Grid, I, N, J, CurMax) ->
    Sum = hourglass_sum(Grid, I, J),
    Updated = if Sum > CurMax -> Sum; true -> CurMax end,
    max_sum_cols(Grid, I, N, J + 1, Updated).

hourglass_sum(Grid, I, J) ->
    Row0 = lists:nth(I + 1, Grid),
    Row1 = lists:nth(I + 2, Grid),
    Row2 = lists:nth(I + 3, Grid),

    A = lists:nth(J + 1, Row0),
    B = lists:nth(J + 2, Row0),
    C = lists:nth(J + 3, Row0),

    D = lists:nth(J + 2, Row1),

    E = lists:nth(J + 1, Row2),
    F = lists:nth(J + 2, Row2),
    G = lists:nth(J + 3, Row2),

    A + B + C + D + E + F + G.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum(grid :: [[integer]]) :: integer
  def max_sum(grid) do
    m = length(grid)
    n = length(hd(grid))

    sums =
      for i <- 0..(m - 3), j <- 0..(n - 3) do
        top = Enum.at(grid, i)
        middle = Enum.at(grid, i + 1)
        bottom = Enum.at(grid, i + 2)

        Enum.at(top, j) + Enum.at(top, j + 1) + Enum.at(top, j + 2) +
          Enum.at(middle, j + 1) +
          Enum.at(bottom, j) + Enum.at(bottom, j + 1) + Enum.at(bottom, j + 2)
      end

    Enum.max(sums)
  end
end
```

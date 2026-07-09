# 3239. Minimum Number of Flips to Make Binary Grid Palindromic I

## Cpp

```cpp
class Solution {
public:
    int minFlips(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long rowFlips = 0, colFlips = 0;
        
        // Make all rows palindromic
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n / 2; ++j) {
                if (grid[i][j] != grid[i][n - 1 - j])
                    ++rowFlips;
            }
        }
        
        // Make all columns palindromic
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m / 2; ++i) {
                if (grid[i][j] != grid[m - 1 - i][j])
                    ++colFlips;
            }
        }
        
        return (int)min(rowFlips, colFlips);
    }
};
```

## Java

```java
class Solution {
    public int minFlips(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long rowFlips = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n / 2; j++) {
                int cnt = grid[i][j] + grid[i][n - 1 - j];
                rowFlips += Math.min(cnt, 2 - cnt);
            }
        }
        long colFlips = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m / 2; i++) {
                int cnt = grid[i][j] + grid[m - 1 - i][j];
                colFlips += Math.min(cnt, 2 - cnt);
            }
        }
        return (int) Math.min(rowFlips, colFlips);
    }
}
```

## Python

```python
class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        row_flips = 0
        for i in range(m):
            row = grid[i]
            for j in range(n // 2):
                if row[j] != row[n - 1 - j]:
                    row_flips += 1
        col_flips = 0
        for j in range(n):
            for i in range(m // 2):
                if grid[i][j] != grid[m - 1 - i][j]:
                    col_flips += 1
        return min(row_flips, col_flips)
```

## Python3

```python
class Solution:
    def minFlips(self, grid):
        m = len(grid)
        n = len(grid[0])
        row_flips = 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][n - 1 - j]:
                    row_flips += 1
        col_flips = 0
        for j in range(n):
            for i in range(m // 2):
                if grid[i][j] != grid[m - 1 - i][j]:
                    col_flips += 1
        return min(row_flips, col_flips)
```

## C

```c
int minFlips(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int m = gridSize;
    int n = gridColSize[0];
    long long rowCost = 0, colCost = 0;

    // Cost to make all rows palindromic
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n / 2; ++j) {
            if (grid[i][j] != grid[i][n - 1 - j]) {
                rowCost++;
            }
        }
    }

    // Cost to make all columns palindromic
    for (int j = 0; j < n; ++j) {
        for (int i = 0; i < m / 2; ++i) {
            if (grid[i][j] != grid[m - 1 - i][j]) {
                colCost++;
            }
        }
    }

    return (int)(rowCost < colCost ? rowCost : colCost);
}
```

## Csharp

```csharp
public class Solution {
    public int MinFlips(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int flipsRows = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n / 2; j++) {
                if (grid[i][j] != grid[i][n - 1 - j]) flipsRows++;
            }
        }
        int flipsCols = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m / 2; i++) {
                if (grid[i][j] != grid[m - 1 - i][j]) flipsCols++;
            }
        }
        return Math.Min(flipsRows, flipsCols);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minFlips = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let rowCost = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0, limit = Math.floor(n / 2); j < limit; ++j) {
            if (grid[i][j] !== grid[i][n - 1 - j]) rowCost++;
        }
    }
    let colCost = 0;
    for (let j = 0; j < n; ++j) {
        for (let i = 0, limit = Math.floor(m / 2); i < limit; ++i) {
            if (grid[i][j] !== grid[m - 1 - i][j]) colCost++;
        }
    }
    return Math.min(rowCost, colCost);
};
```

## Typescript

```typescript
function minFlips(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    let rowFlips = 0;
    const halfN = Math.floor(n / 2);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < halfN; j++) {
            if (grid[i][j] !== grid[i][n - 1 - j]) rowFlips++;
        }
    }

    let colFlips = 0;
    const halfM = Math.floor(m / 2);
    for (let j = 0; j < n; j++) {
        for (let i = 0; i < halfM; i++) {
            if (grid[i][j] !== grid[m - 1 - i][j]) colFlips++;
        }
    }

    return Math.min(rowFlips, colFlips);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minFlips($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        $rowFlips = 0;
        $halfN = intdiv($n, 2);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $halfN; $j++) {
                if ($grid[$i][$j] !== $grid[$i][$n - 1 - $j]) {
                    $rowFlips++;
                }
            }
        }

        $colFlips = 0;
        $halfM = intdiv($m, 2);
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $halfM; $i++) {
                if ($grid[$i][$j] !== $grid[$m - 1 - $i][$j]) {
                    $colFlips++;
                }
            }
        }

        return min($rowFlips, $colFlips);
    }
}
```

## Swift

```swift
class Solution {
    func minFlips(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var rowFlips = 0
        for i in 0..<m {
            var l = 0
            var r = n - 1
            while l < r {
                if grid[i][l] != grid[i][r] {
                    rowFlips += 1
                }
                l += 1
                r -= 1
            }
        }
        var colFlips = 0
        for j in 0..<n {
            var top = 0
            var bottom = m - 1
            while top < bottom {
                if grid[top][j] != grid[bottom][j] {
                    colFlips += 1
                }
                top += 1
                bottom -= 1
            }
        }
        return min(rowFlips, colFlips)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minFlips(grid: Array<IntArray>): Int {
        val m = grid.size
        if (m == 0) return 0
        val n = grid[0].size
        var rowCost = 0
        for (i in 0 until m) {
            for (j in 0 until n / 2) {
                if (grid[i][j] != grid[i][n - 1 - j]) rowCost++
            }
        }
        var colCost = 0
        for (j in 0 until n) {
            for (i in 0 until m / 2) {
                if (grid[i][j] != grid[m - 1 - i][j]) colCost++
            }
        }
        return kotlin.math.min(rowCost, colCost)
    }
}
```

## Dart

```dart
class Solution {
  int minFlips(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    int rowCost = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n ~/ 2; ++j) {
        if (grid[i][j] != grid[i][n - 1 - j]) rowCost++;
      }
    }

    int colCost = 0;
    for (int j = 0; j < n; ++j) {
      for (int i = 0; i < m ~/ 2; ++i) {
        if (grid[i][j] != grid[m - 1 - i][j]) colCost++;
      }
    }

    return rowCost < colCost ? rowCost : colCost;
  }
}
```

## Golang

```go
func minFlips(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])

	rowFlips := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n/2; j++ {
			if grid[i][j] != grid[i][n-1-j] {
				rowFlips++
			}
		}
	}

	colFlips := 0
	for j := 0; j < n; j++ {
		for i := 0; i < m/2; i++ {
			if grid[i][j] != grid[m-1-i][j] {
				colFlips++
			}
		}
	}

	if rowFlips < colFlips {
		return rowFlips
	}
	return colFlips
}
```

## Ruby

```ruby
def min_flips(grid)
  m = grid.size
  n = grid[0].size

  row_flips = 0
  (0...m).each do |i|
    l = 0
    r = n - 1
    while l < r
      row_flips += 1 if grid[i][l] != grid[i][r]
      l += 1
      r -= 1
    end
  end

  col_flips = 0
  (0...n).each do |j|
    t = 0
    b = m - 1
    while t < b
      col_flips += 1 if grid[t][j] != grid[b][j]
      t += 1
      b -= 1
    end
  end

  row_flips < col_flips ? row_flips : col_flips
end
```

## Scala

```scala
object Solution {
    def minFlips(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length

        var rowCost = 0
        var i = 0
        while (i < m) {
            var l = 0
            var r = n - 1
            while (l < r) {
                if (grid(i)(l) != grid(i)(r)) rowCost += 1
                l += 1
                r -= 1
            }
            i += 1
        }

        var colCost = 0
        var j = 0
        while (j < n) {
            var top = 0
            var bottom = m - 1
            while (top < bottom) {
                if (grid(top)(j) != grid(bottom)(j)) colCost += 1
                top += 1
                bottom -= 1
            }
            j += 1
        }

        Math.min(rowCost, colCost)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_flips(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();

        let mut row_flips: i64 = 0;
        for i in 0..m {
            for j in 0..n / 2 {
                if grid[i][j] != grid[i][n - 1 - j] {
                    row_flips += 1;
                }
            }
        }

        let mut col_flips: i64 = 0;
        for j in 0..n {
            for i in 0..m / 2 {
                if grid[i][j] != grid[m - 1 - i][j] {
                    col_flips += 1;
                }
            }
        }

        std::cmp::min(row_flips, col_flips) as i32
    }
}
```

## Racket

```racket
(define/contract (min-flips grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (car grid))))
         (vec-grid (list->vector (map list->vector grid)))
         (row-half (quotient n 2))
         (col-half (quotient m 2)))

    (define (row-flips)
      (let loop ((i 0) (acc 0))
        (if (= i m)
            acc
            (let* ((row (vector-ref vec-grid i)))
              (let inner ((j 0) (cnt 0))
                (if (= j row-half)
                    (loop (+ i 1) (+ acc cnt))
                    (inner (+ j 1)
                           (+ cnt (if (not (= (vector-ref row j)
                                             (vector-ref row (- n 1 j))))
                                      1
                                      0)))))))))

    (define (col-flips)
      (let loop ((j 0) (acc 0))
        (if (= j n)
            acc
            (let inner ((i 0) (cnt 0))
              (if (= i col-half)
                  (loop (+ j 1) (+ acc cnt))
                  (inner (+ i 1)
                         (+ cnt (if (not (= (vector-ref (vector-ref vec-grid i) j)
                                           (vector-ref (vector-ref vec-grid (- m 1 i)) j)))
                                    1
                                    0)))))))))

    (min (row-flips) (col-flips))))
```

## Erlang

```erlang
-module(solution).
-export([min_flips/1]).

-spec min_flips(Grid :: [[integer()]]) -> integer().
min_flips(Grid) ->
    RowCost = compute_row_cost(Grid),
    ColCost = compute_col_cost(Grid),
    erlang:min(RowCost, ColCost).

compute_row_cost([]) -> 0;
compute_row_cost([Row|Rest]) ->
    N = length(Row),
    Half = N div 2,
    Rev = lists:reverse(Row),
    RowCost = pair_cost(Row, Rev, Half),
    RowCost + compute_row_cost(Rest).

pair_cost(_, _, 0) -> 0;
pair_cost([F|Fs], [B|Bs], K) ->
    (F bxor B) + pair_cost(Fs, Bs, K-1).

compute_col_cost(Grid) ->
    M = length(Grid),
    HalfM = M div 2,
    RevGrid = lists:reverse(Grid),
    col_cost_helper(Grid, RevGrid, HalfM).

col_cost_helper(_, _, 0) -> 0;
col_cost_helper([RowTop|RestTop], [RowBottom|RestBottom], K) ->
    RowCost = row_xor_sum(RowTop, RowBottom),
    RowCost + col_cost_helper(RestTop, RestBottom, K-1).

row_xor_sum([], []) -> 0;
row_xor_sum([A|As], [B|Bs]) ->
    (A bxor B) + row_xor_sum(As, Bs).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_flips(grid :: [[integer]]) :: integer
  def min_flips(grid) do
    rows = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    m = tuple_size(rows)
    n = tuple_size(elem(rows, 0))

    row_flips =
      0..(m - 1)
      |> Enum.reduce(0, fn i, acc ->
        row = elem(rows, i)
        acc + count_row_mismatches(row, n)
      end)

    col_flips =
      0..(n - 1)
      |> Enum.reduce(0, fn j, acc ->
        acc + count_col_mismatches(rows, m, j)
      end)

    if row_flips < col_flips, do: row_flips, else: col_flips
  end

  defp count_row_mismatches(row, n) do
    limit = div(n, 2)

    0..(limit - 1)
    |> Enum.reduce(0, fn j, cnt ->
      if elem(row, j) != elem(row, n - 1 - j), do: cnt + 1, else: cnt
    end)
  end

  defp count_col_mismatches(rows, m, col_idx) do
    limit = div(m, 2)

    0..(limit - 1)
    |> Enum.reduce(0, fn i, cnt ->
      top = elem(elem(rows, i), col_idx)
      bottom = elem(elem(rows, m - 1 - i), col_idx)

      if top != bottom, do: cnt + 1, else: cnt
    end)
  end
end
```

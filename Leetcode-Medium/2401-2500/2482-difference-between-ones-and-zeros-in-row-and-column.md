# 2482. Difference Between Ones and Zeros in Row and Column

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> rowOnes(m, 0), colOnes(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    ++rowOnes[i];
                    ++colOnes[j];
                }
            }
        }
        vector<vector<int>> diff(m, vector<int>(n));
        int base = -n - m;
        for (int i = 0; i < m; ++i) {
            int twoRow = 2 * rowOnes[i];
            for (int j = 0; j < n; ++j) {
                diff[i][j] = twoRow + 2 * colOnes[j] + base;
            }
        }
        return diff;
    }
};
```

## Java

```java
class Solution {
    public int[][] onesMinusZeros(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] rowOnes = new int[m];
        int[] colOnes = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    rowOnes[i]++;
                    colOnes[j]++;
                }
            }
        }
        int[][] diff = new int[m][n];
        int subtract = m + n;
        for (int i = 0; i < m; i++) {
            int baseRow = 2 * rowOnes[i];
            for (int j = 0; j < n; j++) {
                diff[i][j] = baseRow + 2 * colOnes[j] - subtract;
            }
        }
        return diff;
    }
}
```

## Python

```python
class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        row_ones = [0] * m
        col_ones = [0] * n

        for i in range(m):
            row = grid[i]
            cnt = 0
            for j, val in enumerate(row):
                if val:
                    cnt += 1
                    col_ones[j] += 1
            row_ones[i] = cnt

        base = -n - m
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            ri = 2 * row_ones[i]
            di = diff[i]
            for j in range(n):
                di[j] = ri + 2 * col_ones[j] + base
        return diff
```

## Python3

```python
from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row_ones = [0] * m
        col_ones = [0] * n

        for i in range(m):
            for j, val in enumerate(grid[i]):
                if val:
                    row_ones[i] += 1
                    col_ones[j] += 1

        res = [[0] * n for _ in range(m)]
        offset = -n - m
        for i in range(m):
            ri = 2 * row_ones[i]
            for j in range(n):
                res[i][j] = ri + 2 * col_ones[j] + offset

        return res
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** onesMinusZeros(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    int rows = gridSize;
    int cols = gridColSize[0];
    
    int *rowOnes = (int *)calloc(rows, sizeof(int));
    int *colOnes = (int *)calloc(cols, sizeof(int));
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                rowOnes[i]++;
                colOnes[j]++;
            }
        }
    }
    
    int **diff = (int **)malloc(rows * sizeof(int *));
    *returnColumnSizes = (int *)malloc(rows * sizeof(int));
    *returnSize = rows;
    
    for (int i = 0; i < rows; ++i) {
        diff[i] = (int *)malloc(cols * sizeof(int));
        (*returnColumnSizes)[i] = cols;
        int base = 2 * rowOnes[i] - cols - rows; // part depending on row
        for (int j = 0; j < cols; ++j) {
            diff[i][j] = base + 2 * colOnes[j];
        }
    }
    
    free(rowOnes);
    free(colOnes);
    return diff;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] OnesMinusZeros(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] rowOnes = new int[m];
        int[] colOnes = new int[n];

        for (int i = 0; i < m; i++) {
            int[] row = grid[i];
            for (int j = 0; j < n; j++) {
                int val = row[j];
                rowOnes[i] += val;
                colOnes[j] += val;
            }
        }

        int[][] diff = new int[m][];
        int offset = n + m; // will be subtracted
        for (int i = 0; i < m; i++) {
            diff[i] = new int[n];
            int rowPart = 2 * rowOnes[i];
            for (int j = 0; j < n; j++) {
                diff[i][j] = rowPart + 2 * colOnes[j] - offset;
            }
        }

        return diff;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var onesMinusZeros = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const rowOnes = new Array(m).fill(0);
    const colOnes = new Array(n).fill(0);
    
    for (let i = 0; i < m; ++i) {
        let cnt = 0;
        const row = grid[i];
        for (let j = 0; j < n; ++j) {
            if (row[j] === 1) {
                cnt++;
                colOnes[j]++;
            }
        }
        rowOnes[i] = cnt;
    }
    
    const diff = new Array(m);
    const base = -(n + m); // -n - m
    for (let i = 0; i < m; ++i) {
        diff[i] = new Array(n);
        const r = rowOnes[i];
        for (let j = 0; j < n; ++j) {
            diff[i][j] = 2 * r + 2 * colOnes[j] + base;
        }
    }
    
    return diff;
};
```

## Typescript

```typescript
function onesMinusZeros(grid: number[][]): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const rowOnes = new Array(m).fill(0);
    const colOnes = new Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        const row = grid[i];
        for (let j = 0; j < n; j++) {
            if (row[j] === 1) {
                rowOnes[i]++;
                colOnes[j]++;
            }
        }
    }

    const diff: number[][] = new Array(m);
    const offset = -n - m;
    for (let i = 0; i < m; i++) {
        diff[i] = new Array(n);
        const base = 2 * rowOnes[i];
        for (let j = 0; j < n; j++) {
            diff[i][j] = base + 2 * colOnes[j] + offset;
        }
    }

    return diff;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function onesMinusZeros($grid) {
        $m = count($grid);
        if ($m === 0) return [];
        $n = count($grid[0]);
        
        $rowOnes = array_fill(0, $m, 0);
        $colOnes = array_fill(0, $n, 0);
        
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $val = $grid[$i][$j];
                $rowOnes[$i] += $val;
                $colOnes[$j] += $val;
            }
        }
        
        $sub = $n + $m; // common subtraction part
        $result = [];
        for ($i = 0; $i < $m; $i++) {
            $row = [];
            $rPart = 2 * $rowOnes[$i];
            for ($j = 0; $j < $n; $j++) {
                $value = $rPart + 2 * $colOnes[$j] - $sub;
                $row[] = $value;
            }
            $result[] = $row;
        }
        
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func onesMinusZeros(_ grid: [[Int]]) -> [[Int]] {
        let m = grid.count
        let n = grid[0].count
        var rowOnes = [Int](repeating: 0, count: m)
        var colOnes = [Int](repeating: 0, count: n)
        
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    rowOnes[i] += 1
                    colOnes[j] += 1
                }
            }
        }
        
        var diff = Array(repeating: Array(repeating: 0, count: n), count: m)
        let offset = -n - m
        for i in 0..<m {
            let rowComponent = 2 * rowOnes[i]
            for j in 0..<n {
                diff[i][j] = rowComponent + 2 * colOnes[j] + offset
            }
        }
        return diff
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun onesMinusZeros(grid: Array<IntArray>): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val rowOnes = IntArray(m)
        val colOnes = IntArray(n)

        for (i in 0 until m) {
            val row = grid[i]
            for (j in 0 until n) {
                if (row[j] == 1) {
                    rowOnes[i]++
                    colOnes[j]++
                }
            }
        }

        val result = Array(m) { IntArray(n) }
        val offset = n + m
        for (i in 0 until m) {
            val r = 2 * rowOnes[i]
            for (j in 0 until n) {
                result[i][j] = r + 2 * colOnes[j] - offset
            }
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> onesMinusZeros(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<int> onesRow = List.filled(m, 0);
    List<int> onesCol = List.filled(n, 0);

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          onesRow[i]++;
          onesCol[j]++;
        }
      }
    }

    List<List<int>> diff = List.generate(m, (_) => List.filled(n, 0));
    int offset = -n - m;
    for (int i = 0; i < m; i++) {
      int rowPart = 2 * onesRow[i];
      for (int j = 0; j < n; j++) {
        diff[i][j] = rowPart + 2 * onesCol[j] + offset;
      }
    }

    return diff;
  }
}
```

## Golang

```go
func onesMinusZeros(grid [][]int) [][]int {
	m := len(grid)
	if m == 0 {
		return nil
	}
	n := len(grid[0])

	rowOnes := make([]int, m)
	colOnes := make([]int, n)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				rowOnes[i]++
				colOnes[j]++
			}
		}
	}

	diff := make([][]int, m)
	for i := 0; i < m; i++ {
		diff[i] = make([]int, n)
		for j := 0; j < n; j++ {
			diff[i][j] = 2*rowOnes[i] + 2*colOnes[j] - n - m
		}
	}

	return diff
}
```

## Ruby

```ruby
def ones_minus_zeros(grid)
  m = grid.length
  n = grid[0].length
  row_ones = Array.new(m, 0)
  col_ones = Array.new(n, 0)

  grid.each_with_index do |row, i|
    row.each_with_index do |val, j|
      if val == 1
        row_ones[i] += 1
        col_ones[j] += 1
      end
    end
  end

  diff = Array.new(m) { Array.new(n, 0) }
  grid.each_with_index do |row, i|
    row.each_with_index do |_val, j|
      diff[i][j] = 2 * row_ones[i] + 2 * col_ones[j] - n - m
    end
  end

  diff
end
```

## Scala

```scala
object Solution {
  def onesMinusZeros(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    if (m == 0) return Array.empty
    val n = grid(0).length

    val rowOnes = new Array[Int](m)
    val colOnes = new Array[Int](n)

    var i = 0
    while (i < m) {
      var j = 0
      var cntRow = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          cntRow += 1
          colOnes(j) += 1
        }
        j += 1
      }
      rowOnes(i) = cntRow
      i += 1
    }

    val diff = Array.ofDim[Int](m, n)
    i = 0
    while (i < m) {
      var j = 0
      val r = rowOnes(i)
      while (j < n) {
        diff(i)(j) = 2 * r + 2 * colOnes(j) - n - m
        j += 1
      }
      i += 1
    }

    diff
  }
}
```

## Rust

```rust
impl Solution {
    pub fn ones_minus_zeros(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        if m == 0 {
            return vec![];
        }
        let n = grid[0].len();

        let mut row_ones = vec![0i32; m];
        let mut col_ones = vec![0i32; n];

        for i in 0..m {
            for j in 0..n {
                let v = grid[i][j];
                row_ones[i] += v;
                col_ones[j] += v;
            }
        }

        let m_i32 = m as i32;
        let n_i32 = n as i32;

        let mut diff = vec![vec![0i32; n]; m];
        for i in 0..m {
            for j in 0..n {
                diff[i][j] = 2 * row_ones[i] + 2 * col_ones[j] - n_i32 - m_i32;
            }
        }

        diff
    }
}
```

## Racket

```racket
(define/contract (ones-minus-zeros grid)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (car grid))))
         (ones-row (make-vector m 0))
         (ones-col (make-vector n 0)))
    ;; first pass: count ones per row and column
    (for ([row grid] [i (in-naturals)])
      (for ([val row] [j (in-naturals)])
        (when (= val 1)
          (vector-set! ones-row i (+ (vector-ref ones-row i) 1))
          (vector-set! ones-col j (+ (vector-ref ones-col j) 1)))))
    ;; second pass: build diff matrix
    (let ((diff (make-vector m)))
      (for ([row grid] [i (in-naturals)])
        (define row-diff (make-vector n))
        (for ([val row] [j (in-naturals)])
          (define d
            (- (+ (* 2 (vector-ref ones-row i))
                  (* 2 (vector-ref ones-col j)))
               n m))
          (vector-set! row-diff j d))
        (vector-set! diff i (vector->list row-diff)))
      (vector->list diff))))
```

## Erlang

```erlang
-module(solution).
-export([ones_minus_zeros/1]).

-spec ones_minus_zeros(Grid :: [[integer()]]) -> [[integer()]].
ones_minus_zeros(Grid) ->
    M = length(Grid),
    N = case Grid of
            [] -> 0;
            [First|_] -> length(First)
        end,
    OnesRow = [lists:sum(Row) || Row <- Grid],
    InitCol = lists:duplicate(N, 0),
    OnesCol = lists:foldl(
                fun(Row, Acc) ->
                    lists:zipwith(fun(Cnt, Val) -> Cnt + Val end, Acc, Row)
                end,
                InitCol,
                Grid
              ),
    [begin
         RowOnes = lists:nth(I + 1, OnesRow),
         [(2 * RowOnes) + (2 * ColOnes) - N - M || ColOnes <- OnesCol]
     end
     || I <- lists:seq(0, M - 1)
    ].
```

## Elixir

```elixir
defmodule Solution do
  @spec ones_minus_zeros(grid :: [[integer]]) :: [[integer]]
  def ones_minus_zeros(grid) do
    m = length(grid)
    n = grid |> hd() |> length()

    # Count ones in each row
    ones_row = Enum.map(grid, &Enum.sum/1)

    # Count ones in each column
    col_sums =
      for j <- 0..(n - 1) do
        Enum.reduce(grid, 0, fn row, acc -> acc + Enum.at(row, j) end)
      end

    offset = n + m

    Enum.with_index(grid)
    |> Enum.map(fn {_row, i} ->
      orow = Enum.at(ones_row, i)

      Enum.map(0..(n - 1), fn j ->
        2 * orow + 2 * Enum.at(col_sums, j) - offset
      end)
    end)
  end
end
```

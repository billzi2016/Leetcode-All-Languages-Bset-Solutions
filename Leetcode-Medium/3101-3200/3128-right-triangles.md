# 3128. Right Triangles

## Cpp

```cpp
class Solution {
public:
    long long numberOfRightTriangles(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        vector<long long> row(m, 0), col(n, 0);
        for (int i = 0; i < m; ++i) {
            long long cnt = 0;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) ++cnt;
            }
            row[i] = cnt;
        }
        for (int j = 0; j < n; ++j) {
            long long cnt = 0;
            for (int i = 0; i < m; ++i) {
                if (grid[i][j] == 1) ++cnt;
            }
            col[j] = cnt;
        }
        long long ans = 0;
        for (int i = 0; i < m; ++i) {
            if (row[i] <= 1) continue;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1 && col[j] > 1) {
                    ans += (row[i] - 1) * (col[j] - 1);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long numberOfRightTriangles(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] rowCount = new int[m];
        int[] colCount = new int[n];
        
        // Count 1s in each row and column
        for (int i = 0; i < m; i++) {
            int[] row = grid[i];
            for (int j = 0; j < n; j++) {
                if (row[j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }
        
        long ans = 0L;
        // Sum contributions
        for (int i = 0; i < m; i++) {
            int[] row = grid[i];
            if (rowCount[i] <= 1) continue; // no contribution from this row
            for (int j = 0; j < n; j++) {
                if (row[j] == 1 && colCount[j] > 1) {
                    ans += (long)(rowCount[i] - 1) * (colCount[j] - 1);
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
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        row_counts = [0] * m
        col_counts = [0] * n

        for i in range(m):
            row = grid[i]
            cnt = 0
            for j in range(n):
                if row[j]:
                    cnt += 1
            row_counts[i] = cnt

        for j in range(n):
            cnt = 0
            for i in range(m):
                if grid[i][j]:
                    cnt += 1
            col_counts[j] = cnt

        ans = 0
        for i in range(m):
            ri = row_counts[i] - 1
            if ri <= 0:
                continue
            row = grid[i]
            for j in range(n):
                if row[j]:
                    cj = col_counts[j] - 1
                    if cj > 0:
                        ans += ri * cj
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        row_counts = [0] * m
        col_counts = [0] * n

        for i in range(m):
            cnt = 0
            row = grid[i]
            for j in range(n):
                if row[j]:
                    cnt += 1
            row_counts[i] = cnt

        for j in range(n):
            cnt = 0
            for i in range(m):
                if grid[i][j]:
                    cnt += 1
            col_counts[j] = cnt

        ans = 0
        for i in range(m):
            rc = row_counts[i] - 1
            if rc <= 0:
                continue
            row = grid[i]
            for j in range(n):
                if row[j]:
                    cc = col_counts[j] - 1
                    if cc > 0:
                        ans += rc * cc
        return ans
```

## C

```c
#include <stdlib.h>

long long numberOfRightTriangles(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int maxCols = 0;
    for (int i = 0; i < gridSize; ++i)
        if (gridColSize[i] > maxCols) maxCols = gridColSize[i];

    int *colCounts = (int *)calloc(maxCols, sizeof(int));
    int *rowCounts = (int *)malloc(gridSize * sizeof(int));

    for (int i = 0; i < gridSize; ++i) {
        int cnt = 0;
        int cols = gridColSize[i];
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                ++cnt;
                ++colCounts[j];
            }
        }
        rowCounts[i] = cnt;
    }

    long long ans = 0;
    for (int i = 0; i < gridSize; ++i) {
        int cols = gridColSize[i];
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                long long r = rowCounts[i] - 1;
                long long c = colCounts[j] - 1;
                ans += r * c;
            }
        }
    }

    free(colCounts);
    free(rowCounts);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long NumberOfRightTriangles(int[][] grid) {
        int m = grid.Length;
        if (m == 0) return 0L;
        int n = grid[0].Length;

        int[] rowCount = new int[m];
        int[] colCount = new int[n];

        // Count ones in each row and column
        for (int i = 0; i < m; i++) {
            int[] row = grid[i];
            for (int j = 0; j < n; j++) {
                if (row[j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }

        long result = 0L;
        // Sum contributions
        for (int i = 0; i < m; i++) {
            int[] row = grid[i];
            int rcMinus = rowCount[i] - 1;
            if (rcMinus <= 0) continue; // no possible triangles from this row
            for (int j = 0; j < n; j++) {
                if (row[j] == 1) {
                    int ccMinus = colCount[j] - 1;
                    if (ccMinus > 0) {
                        result += (long)rcMinus * ccMinus;
                    }
                }
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var numberOfRightTriangles = function(grid) {
    const m = grid.length;
    if (m === 0) return 0;
    const n = grid[0].length;
    
    const rowCnt = new Array(m).fill(0);
    const colCnt = new Array(n).fill(0);
    
    // First pass: count ones per row and column
    for (let i = 0; i < m; ++i) {
        const row = grid[i];
        for (let j = 0; j < n; ++j) {
            if (row[j] === 1) {
                rowCnt[i]++;
                colCnt[j]++;
            }
        }
    }
    
    let ans = 0;
    // Second pass: accumulate contributions
    for (let i = 0; i < m; ++i) {
        const row = grid[i];
        const r = rowCnt[i] - 1;
        if (r <= 0) continue; // no horizontal partner
        for (let j = 0; j < n; ++j) {
            if (row[j] === 1) {
                const c = colCnt[j] - 1;
                if (c > 0) ans += r * c;
            }
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function numberOfRightTriangles(grid: number[][]): number {
    const m = grid.length;
    if (m === 0) return 0;
    const n = grid[0].length;
    const rowCounts = new Array(m).fill(0);
    const colCounts = new Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                rowCounts[i]++;
                colCounts[j]++;
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < m; i++) {
        const rowsMinusOne = rowCounts[i] - 1;
        if (rowsMinusOne <= 0) continue;
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                const colsMinusOne = colCounts[j] - 1;
                if (colsMinusOne > 0) ans += rowsMinusOne * colsMinusOne;
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function numberOfRightTriangles($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);

        $rowCount = array_fill(0, $m, 0);
        $colCount = array_fill(0, $n, 0);

        // Count ones in each row and column
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 1) {
                    $rowCount[$i]++;
                    $colCount[$j]++;
                }
            }
        }

        $ans = 0;
        // Sum contributions of each cell with value 1
        for ($i = 0; $i < $m; $i++) {
            if ($rowCount[$i] <= 1) continue; // no possible triangle from this row
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 1 && $colCount[$j] > 1) {
                    $ans += ($rowCount[$i] - 1) * ($colCount[$j] - 1);
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfRightTriangles(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        guard let cols = grid.first?.count else { return 0 }
        
        var rowCounts = [Int](repeating: 0, count: rows)
        var colCounts = [Int](repeating: 0, count: cols)
        
        // Count ones in each row and column
        for i in 0..<rows {
            for j in 0..<cols {
                if grid[i][j] == 1 {
                    rowCounts[i] += 1
                    colCounts[j] += 1
                }
            }
        }
        
        var result = 0
        // For each cell with value 1, add (rowCount-1)*(colCount-1)
        for i in 0..<rows {
            let r = rowCounts[i]
            if r <= 1 { continue } // no contribution possible
            for j in 0..<cols where grid[i][j] == 1 {
                let c = colCounts[j]
                if c > 1 {
                    result += (r - 1) * (c - 1)
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfRightTriangles(grid: Array<IntArray>): Long {
        val m = grid.size
        val n = grid[0].size
        val rowCounts = IntArray(m)
        val colCounts = IntArray(n)

        for (i in 0 until m) {
            var cnt = 0
            val row = grid[i]
            for (j in 0 until n) {
                if (row[j] == 1) {
                    cnt++
                    colCounts[j]++
                }
            }
            rowCounts[i] = cnt
        }

        var ans = 0L
        for (i in 0 until m) {
            val row = grid[i]
            val rMinus = rowCounts[i] - 1
            if (rMinus <= 0) continue
            for (j in 0 until n) {
                if (row[j] == 1) {
                    val cMinus = colCounts[j] - 1
                    if (cMinus > 0) {
                        ans += rMinus.toLong() * cMinus.toLong()
                    }
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
  int numberOfRightTriangles(List<List<int>> grid) {
    int m = grid.length;
    if (m == 0) return 0;
    int n = grid[0].length;

    List<int> rowCount = List.filled(m, 0);
    List<int> colCount = List.filled(n, 0);

    // Count ones in each row and column
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          rowCount[i]++;
          colCount[j]++;
        }
      }
    }

    int result = 0;
    // For each cell with value 1, add (row-1)*(col-1)
    for (int i = 0; i < m; i++) {
      if (rowCount[i] <= 1) continue; // no contribution possible
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1 && colCount[j] > 1) {
          result += (rowCount[i] - 1) * (colCount[j] - 1);
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func numberOfRightTriangles(grid [][]int) int64 {
    m := len(grid)
    if m == 0 {
        return 0
    }
    n := len(grid[0])
    rowCounts := make([]int, m)
    colCounts := make([]int, n)

    // Count ones in each row and column
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                rowCounts[i]++
                colCounts[j]++
            }
        }
    }

    var ans int64 = 0
    // For each cell with value 1, add (row-1)*(col-1)
    for i := 0; i < m; i++ {
        if rowCounts[i] <= 1 {
            continue
        }
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 && colCounts[j] > 1 {
                ans += int64(rowCounts[i]-1) * int64(colCounts[j]-1)
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def number_of_right_triangles(grid)
  m = grid.length
  return 0 if m == 0
  n = grid[0].length

  row_counts = Array.new(m, 0)
  col_counts = Array.new(n, 0)

  # First pass: count 1s per row and column
  m.times do |i|
    row = grid[i]
    n.times do |j|
      if row[j] == 1
        row_counts[i] += 1
        col_counts[j] += 1
      end
    end
  end

  # Second pass: sum contributions
  ans = 0
  m.times do |i|
    next if row_counts[i] <= 1
    row = grid[i]
    n.times do |j|
      if row[j] == 1 && col_counts[j] > 1
        ans += (row_counts[i] - 1) * (col_counts[j] - 1)
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def numberOfRightTriangles(grid: Array[Array[Int]]): Long = {
        val m = grid.length
        if (m == 0) return 0L
        val n = grid(0).length

        val row = new Array[Int](m)
        val col = new Array[Int](n)

        // count ones per row
        var i = 0
        while (i < m) {
            var cnt = 0
            var j = 0
            while (j < n) {
                if (grid(i)(j) == 1) cnt += 1
                j += 1
            }
            row(i) = cnt
            i += 1
        }

        // count ones per column
        var j = 0
        while (j < n) {
            var cnt = 0
            var ii = 0
            while (ii < m) {
                if (grid(ii)(j) == 1) cnt += 1
                ii += 1
            }
            col(j) = cnt
            j += 1
        }

        var ans: Long = 0L
        i = 0
        while (i < m) {
            val rowCnt = row(i)
            if (rowCnt > 1) {
                j = 0
                while (j < n) {
                    if (grid(i)(j) == 1) {
                        val colCnt = col(j)
                        if (colCnt > 1) {
                            ans += (rowCnt - 1).toLong * (colCnt - 1).toLong
                        }
                    }
                    j += 1
                }
            } else {
                // still need to iterate to skip cells, but they contribute nothing
                j = 0
                while (j < n) {
                    j += 1
                }
            }
            i += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_right_triangles(grid: Vec<Vec<i32>>) -> i64 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();

        let mut row_counts = vec![0usize; m];
        let mut col_counts = vec![0usize; n];

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    row_counts[i] += 1;
                    col_counts[j] += 1;
                }
            }
        }

        let mut ans: i64 = 0;
        for i in 0..m {
            let rc = row_counts[i];
            if rc <= 1 {
                continue;
            }
            for j in 0..n {
                if grid[i][j] == 1 {
                    let cc = col_counts[j];
                    if cc > 1 {
                        ans += ((rc - 1) * (cc - 1)) as i64;
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (number-of-right-triangles grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (null? grid) 0 (length (car grid))))
         (row-counts (make-vector rows 0))
         (col-counts (make-vector cols 0)))
    ;; First pass: count 1's per row and column
    (for ([i (in-range rows)]
          [row (in-list grid)])
      (let ((row-sum (apply + row)))
        (vector-set! row-counts i row-sum)
        (for ([j (in-range cols)]
              [val (in-list row)])
          (when (= val 1)
            (vector-set! col-counts j (+ (vector-ref col-counts j) 1))))))
    ;; Second pass: accumulate triangles
    (let ((ans 0))
      (for ([i (in-range rows)]
            [row (in-list grid)])
        (let ((rcnt (- (vector-ref row-counts i) 1)))
          (when (> rcnt 0)
            (for ([j (in-range cols)]
                  [val (in-list row)])
              (when (= val 1)
                (define ccnt (- (vector-ref col-counts j) 1))
                (when (> ccnt 0)
                  (set! ans (+ ans (* rcnt ccnt)))))))))
      ans)))
```

## Erlang

```erlang
-spec number_of_right_triangles(Grid :: [[integer()]]) -> integer().
number_of_right_triangles(Grid) ->
    case Grid of
        [] -> 0;
        [FirstRow | _] ->
            ColNum = length(FirstRow),
            RowCounts = lists:map(fun count_ones/1, Grid),
            ColCounts = compute_col_counts(Grid, ColNum),
            lists:foldl(
                fun({RowCount, Row}, Acc) ->
                    Acc + row_contrib(RowCount, Row, ColCounts)
                end,
                0,
                lists:zip(RowCounts, Grid)
            )
    end.

count_ones(Row) ->
    lists:foldl(fun(X, Acc) -> Acc + X end, 0, Row).

compute_col_counts(Grid, ColNum) ->
    Init = lists:duplicate(ColNum, 0),
    lists:foldl(
        fun(Row, Acc) ->
            lists:zipwith(fun(Elem, Sum) -> Elem + Sum end, Row, Acc)
        end,
        Init,
        Grid).

row_contrib(_RowCount, [], []) ->
    0;
row_contrib(RowCount, [Cell | RestCells], [ColCount | RestCols]) ->
    Add = case Cell of
        1 -> (RowCount - 1) * (ColCount - 1);
        _ -> 0
    end,
    Add + row_contrib(RowCount, RestCells, RestCols).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_right_triangles(grid :: [[integer]]) :: integer
  def number_of_right_triangles(grid) do
    m = length(grid)
    n = if m == 0, do: 0, else: grid |> hd() |> length()

    row_counts =
      Enum.map(grid, fn row ->
        Enum.count(row, &(&1 == 1))
      end)

    col_counts =
      for j <- 0..(n - 1) do
        Enum.reduce(grid, 0, fn row, acc ->
          if Enum.at(row, j) == 1, do: acc + 1, else: acc
        end)
      end

    Enum.with_index(grid)
    |> Enum.reduce(0, fn {row, i}, total ->
      Enum.with_index(row)
      |> Enum.reduce(total, fn {val, j}, acc ->
        if val == 1 do
          (Enum.at(row_counts, i) - 1) * (Enum.at(col_counts, j) - 1) + acc
        else
          acc
        end
      end)
    end)
  end
end
```

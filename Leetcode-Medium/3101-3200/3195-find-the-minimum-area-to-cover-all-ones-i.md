# 3195. Find the Minimum Area to Cover All Ones I

## Cpp

```cpp
class Solution {
public:
    int minimumArea(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int minRow = n, maxRow = -1;
        int minCol = m, maxCol = -1;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    if (i < minRow) minRow = i;
                    if (i > maxRow) maxRow = i;
                    if (j < minCol) minCol = j;
                    if (j > maxCol) maxCol = j;
                }
            }
        }
        int height = maxRow - minRow + 1;
        int width = maxCol - minCol + 1;
        return height * width;
    }
};
```

## Java

```java
class Solution {
    public int minimumArea(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int minRow = rows, maxRow = -1, minCol = cols, maxCol = -1;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    if (i < minRow) minRow = i;
                    if (i > maxRow) maxRow = i;
                    if (j < minCol) minCol = j;
                    if (j > maxCol) maxCol = j;
                }
            }
        }
        int height = maxRow - minRow + 1;
        int width = maxCol - minCol + 1;
        return height * width;
    }
}
```

## Python

```python
class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        min_row = len(grid)
        max_row = -1
        min_col = len(grid[0])
        max_col = -1

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    if i < min_row:
                        min_row = i
                    if i > max_row:
                        max_row = i
                    if j < min_col:
                        min_col = j
                    if j > max_col:
                        max_col = j

        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width
```

## Python3

```python
from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row = len(grid)
        max_row = -1
        min_col = len(grid[0])
        max_col = -1
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    if i < min_row:
                        min_row = i
                    if i > max_row:
                        max_row = i
                    if j < min_col:
                        min_col = j
                    if j > max_col:
                        max_col = j
        
        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width
```

## C

```c
int minimumArea(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = gridColSize[0];
    int minRow = rows, maxRow = -1, minCol = cols, maxCol = -1;
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                if (i < minRow) minRow = i;
                if (i > maxRow) maxRow = i;
                if (j < minCol) minCol = j;
                if (j > maxCol) maxCol = j;
            }
        }
    }
    
    int height = maxRow - minRow + 1;
    int width = maxCol - minCol + 1;
    return height * width;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumArea(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int minRow = rows, maxRow = -1, minCol = cols, maxCol = -1;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    if (i < minRow) minRow = i;
                    if (i > maxRow) maxRow = i;
                    if (j < minCol) minCol = j;
                    if (j > maxCol) maxCol = j;
                }
            }
        }

        int height = maxRow - minRow + 1;
        int width = maxCol - minCol + 1;
        return height * width;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumArea = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    let minRow = rows, maxRow = -1, minCol = cols, maxCol = -1;
    
    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            if (grid[i][j] === 1) {
                if (i < minRow) minRow = i;
                if (i > maxRow) maxRow = i;
                if (j < minCol) minCol = j;
                if (j > maxCol) maxCol = j;
            }
        }
    }
    
    const height = maxRow - minRow + 1;
    const width = maxCol - minCol + 1;
    return height * width;
};
```

## Typescript

```typescript
function minimumArea(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let minRow = m, maxRow = -1, minCol = n, maxCol = -1;
    for (let i = 0; i < m; i++) {
        const row = grid[i];
        for (let j = 0; j < n; j++) {
            if (row[j] === 1) {
                if (i < minRow) minRow = i;
                if (i > maxRow) maxRow = i;
                if (j < minCol) minCol = j;
                if (j > maxCol) maxCol = j;
            }
        }
    }
    const height = maxRow - minRow + 1;
    const width = maxCol - minCol + 1;
    return height * width;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumArea($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);

        $minRow = $rows;
        $maxRow = -1;
        $minCol = $cols;
        $maxCol = -1;

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] == 1) {
                    if ($i < $minRow) $minRow = $i;
                    if ($i > $maxRow) $maxRow = $i;
                    if ($j < $minCol) $minCol = $j;
                    if ($j > $maxCol) $maxCol = $j;
                }
            }
        }

        $height = $maxRow - $minRow + 1;
        $width  = $maxCol - $minCol + 1;

        return $height * $width;
    }
}
```

## Swift

```swift
class Solution {
    func minimumArea(_ grid: [[Int]]) -> Int {
        var minRow = Int.max
        var maxRow = Int.min
        var minCol = Int.max
        var maxCol = Int.min
        
        for i in 0..<grid.count {
            let row = grid[i]
            for j in 0..<row.count {
                if row[j] == 1 {
                    if i < minRow { minRow = i }
                    if i > maxRow { maxRow = i }
                    if j < minCol { minCol = j }
                    if j > maxCol { maxCol = j }
                }
            }
        }
        
        let height = maxRow - minRow + 1
        let width = maxCol - minCol + 1
        return height * width
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumArea(grid: Array<IntArray>): Int {
        var minRow = Int.MAX_VALUE
        var maxRow = Int.MIN_VALUE
        var minCol = Int.MAX_VALUE
        var maxCol = Int.MIN_VALUE

        for (i in grid.indices) {
            val row = grid[i]
            for (j in row.indices) {
                if (row[j] == 1) {
                    if (i < minRow) minRow = i
                    if (i > maxRow) maxRow = i
                    if (j < minCol) minCol = j
                    if (j > maxCol) maxCol = j
                }
            }
        }

        val height = maxRow - minRow + 1
        val width = maxCol - minCol + 1
        return height * width
    }
}
```

## Dart

```dart
class Solution {
  int minimumArea(List<List<int>> grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    int minRow = rows, maxRow = -1, minCol = cols, maxCol = -1;

    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (grid[i][j] == 1) {
          if (i < minRow) minRow = i;
          if (i > maxRow) maxRow = i;
          if (j < minCol) minCol = j;
          if (j > maxCol) maxCol = j;
        }
      }
    }

    int height = maxRow - minRow + 1;
    int width = maxCol - minCol + 1;
    return height * width;
  }
}
```

## Golang

```go
func minimumArea(grid [][]int) int {
    if len(grid) == 0 || len(grid[0]) == 0 {
        return 0
    }
    rows, cols := len(grid), len(grid[0])
    minRow, maxRow := rows, -1
    minCol, maxCol := cols, -1

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 1 {
                if i < minRow {
                    minRow = i
                }
                if i > maxRow {
                    maxRow = i
                }
                if j < minCol {
                    minCol = j
                }
                if j > maxCol {
                    maxCol = j
                }
            }
        }
    }

    height := maxRow - minRow + 1
    width := maxCol - minCol + 1
    return height * width
}
```

## Ruby

```ruby
def minimum_area(grid)
  rows = grid.length
  cols = grid[0].length
  min_row = rows
  max_row = -1
  min_col = cols
  max_col = -1

  grid.each_with_index do |row, i|
    row.each_with_index do |val, j|
      next unless val == 1
      min_row = i if i < min_row
      max_row = i if i > max_row
      min_col = j if j < min_col
      max_col = j if j > max_col
    end
  end

  (max_row - min_row + 1) * (max_col - min_col + 1)
end
```

## Scala

```scala
object Solution {
    def minimumArea(grid: Array[Array[Int]]): Int = {
        var minRow = Int.MaxValue
        var maxRow = Int.MinValue
        var minCol = Int.MaxValue
        var maxCol = Int.MinValue

        for (i <- grid.indices) {
            val row = grid(i)
            for (j <- row.indices) {
                if (row(j) == 1) {
                    if (i < minRow) minRow = i
                    if (i > maxRow) maxRow = i
                    if (j < minCol) minCol = j
                    if (j > maxCol) maxCol = j
                }
            }
        }

        (maxRow - minRow + 1) * (maxCol - minCol + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_area(grid: Vec<Vec<i32>>) -> i32 {
        let mut min_row = usize::MAX;
        let mut max_row = 0usize;
        let mut min_col = usize::MAX;
        let mut max_col = 0usize;

        for (i, row) in grid.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                if val == 1 {
                    if i < min_row { min_row = i; }
                    if i > max_row { max_row = i; }
                    if j < min_col { min_col = j; }
                    if j > max_col { max_col = j; }
                }
            }
        }

        let height = max_row - min_row + 1;
        let width = max_col - min_col + 1;
        (height * width) as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-area grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([rows (length grid)]
         [cols (if (> rows 0) (length (first grid)) 0)]
         [min-row rows]
         [max-row -1]
         [min-col cols]
         [max-col -1])
    (for ([i (in-range rows)]
          [row (in-list grid)])
      (for ([j (in-range cols)]
            [val (in-list row)])
        (when (= val 1)
          (set! min-row (min min-row i))
          (set! max-row (max max-row i))
          (set! min-col (min min-col j))
          (set! max-col (max max-col j)))))
    (let ([height (+ (- max-row min-row) 1)]
          [width (+ (- max-col min-col) 1)])
      (* height width))))
```

## Erlang

```erlang
-spec minimum_area(Grid :: [[integer()]]) -> integer().
minimum_area(Grid) ->
    {MinR, MaxR, MinC, MaxC} = scan_rows(Grid, 0, {undefined, -1, undefined, -1}),
    Height = MaxR - MinR + 1,
    Width = MaxC - MinC + 1,
    Height * Width.

scan_rows([], _RowIdx, Acc) ->
    Acc;
scan_rows([Row|Rest], RowIdx, {MinR, MaxR, MinC, MaxC}) ->
    NewAcc = scan_cols(Row, RowIdx, 0, {MinR, MaxR, MinC, MaxC}),
    scan_rows(Rest, RowIdx + 1, NewAcc).

scan_cols([], _RowIdx, _ColIdx, Acc) ->
    Acc;
scan_cols([Cell|Rest], RowIdx, ColIdx, {MinR, MaxR, MinC, MaxC}) ->
    case Cell of
        1 ->
            NewMinR = case MinR of undefined -> RowIdx; _ -> erlang:min(MinR, RowIdx) end,
            NewMaxR = erlang:max(MaxR, RowIdx),
            NewMinC = case MinC of undefined -> ColIdx; _ -> erlang:min(MinC, ColIdx) end,
            NewMaxC = erlang:max(MaxC, ColIdx),
            scan_cols(Rest, RowIdx, ColIdx + 1, {NewMinR, NewMaxR, NewMinC, NewMaxC});
        _ ->
            scan_cols(Rest, RowIdx, ColIdx + 1, {MinR, MaxR, MinC, MaxC})
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_area(grid :: [[integer]]) :: integer
  def minimum_area(grid) do
    rows = length(grid)
    cols = if rows > 0, do: length(hd(grid)), else: 0

    {min_r, max_r, min_c, max_c} =
      Enum.reduce(Enum.with_index(grid), {rows, -1, cols, -1}, fn {row, i},
          {cur_min_r, cur_max_r, cur_min_c, cur_max_c} ->
        {new_min_r, new_max_r, new_min_c, new_max_c} =
          Enum.reduce(Enum.with_index(row), {cur_min_r, cur_max_r, cur_min_c, cur_max_c}, fn
            {val, j},
            {mr, Mr, mc, Mc} when val == 1 ->
              {
                min(mr, i),
                max(Mr, i),
                min(mc, j),
                max(Mc, j)
              }

            {_val, _j},
            acc ->
              acc
          end)

        {new_min_r, new_max_r, new_min_c, new_max_c}
      end)

    (max_r - min_r + 1) * (max_c - min_c + 1)
  end
end
```

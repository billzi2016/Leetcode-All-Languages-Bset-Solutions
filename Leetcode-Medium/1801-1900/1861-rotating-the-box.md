# 1861. Rotating the Box

## Cpp

```cpp
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        int m = boxGrid.size();
        int n = boxGrid[0].size();
        vector<vector<char>> res(n, vector<char>(m, '.'));
        
        for (int i = 0; i < m; ++i) {
            int writeRow = n - 1; // lowest empty row in the current rotated column
            int newCol = m - 1 - i;
            for (int j = n - 1; j >= 0; --j) {
                char c = boxGrid[i][j];
                if (c == '*') {
                    res[j][newCol] = '*';
                    writeRow = j - 1; // stones cannot pass this obstacle
                } else if (c == '#') {
                    if (writeRow >= 0) {
                        res[writeRow][newCol] = '#';
                        --writeRow;
                    }
                }
                // '.' does nothing
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public char[][] rotateTheBox(char[][] boxGrid) {
        int m = boxGrid.length;
        int n = boxGrid[0].length;
        // Rotate 90 degrees clockwise: new dimensions n x m
        char[][] rotated = new char[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][m - 1 - i] = boxGrid[i][j];
            }
        }
        // Apply gravity column by column
        for (int col = 0; col < m; col++) {
            int writeRow = n - 1; // lowest position a stone can fall to in this column
            for (int row = n - 1; row >= 0; row--) {
                char c = rotated[row][col];
                if (c == '*') {
                    writeRow = row - 1;
                } else if (c == '#') {
                    rotated[row][col] = '.';
                    rotated[writeRow][col] = '#';
                    writeRow--;
                }
            }
        }
        return rotated;
    }
}
```

## Python

```python
class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])
        # Rotate 90 degrees clockwise while building the new grid
        rotated = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]

        # Apply gravity column by column
        for col in range(m):
            empty_row = n - 1  # lowest position where a stone can fall
            for row in range(n - 1, -1, -1):
                cell = rotated[row][col]
                if cell == '*':
                    empty_row = row - 1
                elif cell == '#':
                    if empty_row != row:
                        rotated[empty_row][col] = '#'
                        rotated[row][col] = '.'
                    empty_row -= 1
        return rotated
```

## Python3

```python
from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Rotate 90 degrees clockwise: transpose then reverse each row
        rotated = [[boxGrid[i][j] for i in range(m)] for j in range(n)]
        for row in rotated:
            row.reverse()
        # Apply gravity column by column
        for col in range(m):
            empty_row = n - 1
            for row in range(n - 1, -1, -1):
                cell = rotated[row][col]
                if cell == '*':
                    empty_row = row - 1
                elif cell == '#':
                    if row != empty_row:
                        rotated[empty_row][col] = '#'
                        rotated[row][col] = '.'
                    empty_row -= 1
        return rotated
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char** rotateTheBox(char** boxGrid, int boxGridSize, int* boxGridColSize,
                    int* returnSize, int** returnColumnSizes) {
    int m = boxGridSize;                 // original rows
    int n = boxGridColSize[0];           // original columns

    // Allocate result matrix of size n x m
    char **res = (char **)malloc(n * sizeof(char *));
    for (int i = 0; i < n; ++i) {
        res[i] = (char *)malloc((m + 1) * sizeof(char)); // extra for '\0'
        memset(res[i], '.', m);
        res[i][m] = '\0';
    }

    // Allocate column sizes array
    int *colSizes = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) colSizes[i] = m;

    // Process each original row, applying gravity and rotating simultaneously
    for (int i = 0; i < m; ++i) {
        int emptyPos = n - 1; // rightmost position where a stone can fall in this row
        for (int j = n - 1; j >= 0; --j) {
            char c = boxGrid[i][j];
            if (c == '*') {
                // obstacle stays at its rotated location
                res[j][m - 1 - i] = '*';
                emptyPos = j - 1; // stones cannot pass this obstacle
            } else if (c == '#') {
                // stone falls to the lowest available position
                res[emptyPos][m - 1 - i] = '#';
                emptyPos--;
            }
            // '.' does nothing, cells already initialized as '.'
        }
    }

    *returnSize = n;
    *returnColumnSizes = colSizes;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public char[][] RotateTheBox(char[][] boxGrid)
    {
        int m = boxGrid.Length;
        int n = boxGrid[0].Length;

        // Rotate 90 degrees clockwise: (i, j) -> (j, m - 1 - i)
        char[][] rotated = new char[n][];
        for (int i = 0; i < n; i++)
            rotated[i] = new char[m];

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                rotated[j][m - 1 - i] = boxGrid[i][j];
            }
        }

        // Apply gravity column by column
        for (int col = 0; col < m; col++)
        {
            int emptyRow = n - 1;
            for (int row = n - 1; row >= 0; row--)
            {
                if (rotated[row][col] == '*')
                {
                    emptyRow = row - 1;
                }
                else if (rotated[row][col] == '#')
                {
                    if (emptyRow != row)
                    {
                        rotated[emptyRow][col] = '#';
                        rotated[row][col] = '.';
                    }
                    emptyRow--;
                }
            }
        }

        return rotated;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} boxGrid
 * @return {character[][]}
 */
var rotateTheBox = function(boxGrid) {
    const m = boxGrid.length;
    const n = boxGrid[0].length;
    // Rotate 90 degrees clockwise: result has dimensions n x m
    const rotated = Array.from({ length: n }, () => Array(m).fill('.'));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            rotated[j][m - 1 - i] = boxGrid[i][j];
        }
    }
    // Apply gravity column by column
    for (let col = 0; col < m; ++col) {
        let emptyRow = n - 1;
        for (let row = n - 1; row >= 0; --row) {
            const cell = rotated[row][col];
            if (cell === '#') {
                // Move stone down to the lowest available empty position
                rotated[row][col] = '.';
                rotated[emptyRow][col] = '#';
                emptyRow--;
            } else if (cell === '*') {
                // Obstacle blocks further falling stones above it
                emptyRow = row - 1;
            }
            // '.' does nothing
        }
    }
    return rotated;
};
```

## Typescript

```typescript
function rotateTheBox(boxGrid: string[][]): string[][] {
    const m = boxGrid.length;
    const n = boxGrid[0].length;
    const rotated: string[][] = Array.from({ length: n }, () => Array(m).fill('.'));

    // Rotate 90 degrees clockwise
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            rotated[j][m - 1 - i] = boxGrid[i][j];
        }
    }

    // Apply gravity column by column
    for (let col = 0; col < m; col++) {
        let emptyRow = n - 1;
        for (let row = n - 1; row >= 0; row--) {
            const cell = rotated[row][col];
            if (cell === '*') {
                emptyRow = row - 1;
            } else if (cell === '#') {
                if (row !== emptyRow) {
                    rotated[emptyRow][col] = '#';
                    rotated[row][col] = '.';
                }
                emptyRow--;
            }
        }
    }

    return rotated;
}
```

## Php

```php
class Solution {
    /**
     * @param String[][] $boxGrid
     * @return String[][]
     */
    function rotateTheBox($boxGrid) {
        $m = count($boxGrid);
        if ($m == 0) return [];
        $n = count($boxGrid[0]);

        // Rotate 90 degrees clockwise: (i, j) -> (j, m-1-i)
        $rotated = array_fill(0, $n, array_fill(0, $m, '.'));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $rotated[$j][$m - 1 - $i] = $boxGrid[$i][$j];
            }
        }

        // Apply gravity column by column
        for ($col = 0; $col < $m; $col++) {
            $emptyRow = $n - 1;
            for ($row = $n - 1; $row >= 0; $row--) {
                $cell = $rotated[$row][$col];
                if ($cell === '#') {
                    // Move stone down to the lowest empty position
                    $rotated[$row][$col] = '.';
                    $rotated[$emptyRow][$col] = '#';
                    $emptyRow--;
                } elseif ($cell === '*') {
                    // Obstacle blocks further falling stones above it
                    $emptyRow = $row - 1;
                }
            }
        }

        return $rotated;
    }
}
```

## Swift

```swift
class Solution {
    func rotateTheBox(_ boxGrid: [[Character]]) -> [[Character]] {
        let m = boxGrid.count
        guard m > 0 else { return [] }
        let n = boxGrid[0].count
        var result = Array(repeating: Array(repeating: Character("."), count: m), count: n)
        
        // Rotate 90 degrees clockwise
        for i in 0..<m {
            for j in 0..<n {
                result[j][m - 1 - i] = boxGrid[i][j]
            }
        }
        
        // Apply gravity column by column
        for col in 0..<m {
            var emptyRow = n - 1
            var row = n - 1
            while row >= 0 {
                let cell = result[row][col]
                if cell == "#" {
                    result[emptyRow][col] = "#"
                    if emptyRow != row {
                        result[row][col] = "."
                    }
                    emptyRow -= 1
                } else if cell == "*" {
                    emptyRow = row - 1
                }
                row -= 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rotateTheBox(boxGrid: Array<CharArray>): Array<CharArray> {
        val m = boxGrid.size
        val n = boxGrid[0].size

        // Apply gravity within each row (stones fall to the right)
        for (i in 0 until m) {
            var emptyPos = n - 1
            for (j in n - 1 downTo 0) {
                when (boxGrid[i][j]) {
                    '.' -> { /* nothing */ }
                    '*' -> {
                        // obstacle blocks stones; next empty position is left of it
                        emptyPos = j - 1
                    }
                    '#' -> {
                        if (emptyPos != j) {
                            boxGrid[i][emptyPos] = '#'
                            boxGrid[i][j] = '.'
                        }
                        emptyPos--
                    }
                }
            }
        }

        // Rotate the box clockwise
        val result = Array(n) { CharArray(m) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                result[j][m - 1 - i] = boxGrid[i][j]
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> rotateTheBox(List<List<String>> boxGrid) {
    int m = boxGrid.length;
    int n = boxGrid[0].length;

    // Rotate the grid clockwise: size becomes n x m
    List<List<String>> rotated =
        List.generate(n, (_) => List.filled(m, '.'));

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        rotated[j][m - 1 - i] = boxGrid[i][j];
      }
    }

    // Apply gravity column by column
    for (int col = 0; col < m; ++col) {
      int emptyRow = n - 1;
      for (int row = n - 1; row >= 0; --row) {
        if (rotated[row][col] == '*') {
          emptyRow = row - 1;
        } else if (rotated[row][col] == '#') {
          rotated[row][col] = '.';
          rotated[emptyRow][col] = '#';
          emptyRow--;
        }
      }
    }

    return rotated;
  }
}
```

## Golang

```go
func rotateTheBox(boxGrid [][]byte) [][]byte {
    m := len(boxGrid)
    n := len(boxGrid[0])

    // Rotate 90 degrees clockwise: (i, j) -> (j, m-1-i)
    rotated := make([][]byte, n)
    for i := 0; i < n; i++ {
        rotated[i] = make([]byte, m)
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            rotated[j][m-1-i] = boxGrid[i][j]
        }
    }

    // Apply gravity column by column
    for col := 0; col < m; col++ {
        emptyRow := n - 1
        for row := n - 1; row >= 0; row-- {
            cell := rotated[row][col]
            if cell == '*' {
                emptyRow = row - 1
            } else if cell == '#' {
                if row != emptyRow {
                    rotated[emptyRow][col] = '#'
                    rotated[row][col] = '.'
                }
                emptyRow--
            }
        }
    }

    return rotated
}
```

## Ruby

```ruby
def rotate_the_box(box_grid)
  m = box_grid.length
  n = box_grid[0].length
  result = Array.new(n) { Array.new(m, '.') }

  (0...m).each do |i|
    col = m - 1 - i
    lowest = n - 1
    (n - 1).downto(0) do |j|
      cell = box_grid[i][j]
      if cell == '#'
        result[lowest][col] = '#'
        lowest -= 1
      elsif cell == '*'
        result[j][col] = '*'
        lowest = j - 1
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def rotateTheBox(boxGrid: Array[Array[Char]]): Array[Array[Char]] = {
        val m = boxGrid.length
        val n = if (m == 0) 0 else boxGrid(0).length

        // result matrix of size n x m, initially filled with '.'
        val res = Array.ofDim[Char](n, m)
        var r = 0
        while (r < n) {
            var c = 0
            while (c < m) {
                res(r)(c) = '.'
                c += 1
            }
            r += 1
        }

        var i = 0
        while (i < m) {
            val newCol = m - 1 - i          // column index after rotation
            var emptyRow = n - 1           // lowest row where a stone can fall
            var j = n - 1
            while (j >= 0) {
                boxGrid(i)(j) match {
                    case '*' =>
                        res(j)(newCol) = '*'
                        emptyRow = j - 1   // stones cannot pass this obstacle
                    case '#' =>
                        if (emptyRow >= 0) {
                            res(emptyRow)(newCol) = '#'
                        }
                        emptyRow -= 1
                    case _ => // '.' do nothing, already '.'
                }
                j -= 1
            }
            i += 1
        }

        res
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn rotate_the_box(box_grid: Vec<Vec<char>>) -> Vec<Vec<char>> {
        let m = box_grid.len();
        if m == 0 {
            return vec![];
        }
        let n = box_grid[0].len();

        // Rotate clockwise: (i, j) -> (j, m - 1 - i)
        let mut res = vec![vec!['.'; m]; n];
        for i in 0..m {
            for j in 0..n {
                res[j][m - 1 - i] = box_grid[i][j];
            }
        }

        // Apply gravity column by column
        for col in 0..m {
            let mut empty_row: i32 = n as i32 - 1;
            for row_rev in (0..n).rev() {
                let ch = res[row_rev][col];
                match ch {
                    '*' => {
                        empty_row = row_rev as i32 - 1;
                    }
                    '#' => {
                        if empty_row >= 0 && empty_row != row_rev as i32 {
                            res[empty_row as usize][col] = '#';
                            res[row_rev][col] = '.';
                        }
                        empty_row -= 1;
                    }
                    _ => {}
                }
            }
        }

        res
    }
}
```

## Racket

```racket
(define/contract (rotate-the-box boxGrid)
  (-> (listof (listof char?)) (listof (listof char?)))
  (let* ((m (length boxGrid))
         (n (if (= m 0) 0 (length (first boxGrid))))
         (box-vecs (map list->vector boxGrid))
         (rotated (make-vector n)))
    ;; initialize rotated rows with '.'
    (for ([i (in-range n)])
      (vector-set! rotated i (make-vector m #\.)))
    ;; rotate 90 degrees clockwise
    (for ([i (in-range m)])
      (let ((row-vec (list-ref box-vecs i)))
        (for ([j (in-range n)])
          (let* ((ch (vector-ref row-vec j))
                 (new-row j)
                 (new-col (- m 1 i))
                 (dest-row-vec (vector-ref rotated new-row)))
            (vector-set! dest-row-vec new-col ch)))))
    ;; apply gravity column by column
    (for ([col (in-range m)])
      (let ((write-row (- m 1)))
        (for ([row (in-range (- m 1) -1 -1)])
          (let* ((cell (vector-ref (vector-ref rotated row) col)))
            (cond
              [(char=? cell #\*)
               (set! write-row (- row 1))]
              [(char=? cell #\#)
               (when (not (= row write-row))
                 (vector-set! (vector-ref rotated row) col #\.))
               (vector-set! (vector-ref rotated write-row) col #\#)
               (set! write-row (- write-row 1))])))))
    ;; convert result back to list of lists
    (for/list ([row-idx (in-range n)])
      (vector->list (vector-ref rotated row-idx)))))
```

## Erlang

```erlang
-module(solution).
-export([rotate_the_box/1]).

-spec rotate_the_box(BoxGrid :: [[char()]]) -> [[char()]].
rotate_the_box(BoxGrid) ->
    M = length(BoxGrid),
    N = case BoxGrid of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    % Initialize column arrays filled with '.'
    Cols = [array:new(N, {default, $.}) || _ <- lists:seq(1, M)],
    ColumnsOuter = array:from_list(Cols),
    UpdatedColumns = process_rows(BoxGrid, 0, M, N, ColumnsOuter),
    ColList = array:to_list(UpdatedColumns),
    [ [array:get(RowIdx, ColArr) || ColArr <- ColList] || RowIdx <- lists:seq(0, N-1) ].

process_rows([], _, _, _, ColumnsOuter) ->
    ColumnsOuter;
process_rows([Row|Rest], I, M, N, ColumnsOuter) ->
    ColIdx = M - 1 - I,
    ColumnArr = array:get(ColIdx, ColumnsOuter),
    {NewColumnArr, _} = process_cells(N-1, N-1, ColumnArr, Row),
    NewColumnsOuter = array:set(ColIdx, NewColumnArr, ColumnsOuter),
    process_rows(Rest, I+1, M, N, NewColumnsOuter).

process_cells(-1, _, ColumnArr, _) ->
    {ColumnArr, -1};
process_cells(J, Lowest, ColumnArr, Row) ->
    Char = lists:nth(J+1, Row),
    case Char of
        $* ->
            NewCol = array:set(J, $*, ColumnArr),
            process_cells(J-1, J-1, NewCol, Row);
        $# ->
            NewCol = array:set(Lowest, $#, ColumnArr),
            process_cells(J-1, Lowest-1, NewCol, Row);
        _ ->
            process_cells(J-1, Lowest, ColumnArr, Row)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec rotate_the_box(box_grid :: [[char]]) :: [[char]]
  def rotate_the_box(box_grid) do
    m = length(box_grid)
    n = length(List.first(box_grid))

    # Rotate clockwise: result has n rows and m columns
    rotated =
      Enum.map(0..(n - 1), fn j ->
        Enum.map(:lists.seq(m - 1, 0, -1), fn i ->
          Enum.at(box_grid[i], j)
        end)
      end)

    # Apply gravity column by column
    Enum.reduce(0..(m - 1), rotated, fn col_idx, rows ->
      col = Enum.map(rows, &Enum.at(&1, col_idx))
      new_col = apply_gravity(col)

      Enum.with_index(rows)
      |> Enum.map(fn {row, r_idx} ->
        List.replace_at(row, col_idx, Enum.at(new_col, r_idx))
      end)
    end)
  end

  defp apply_gravity(col) do
    n = length(col)
    empty_start = n - 1

    {new_col, _} =
      col
      |> Enum.reverse()
      |> Enum.with_index()
      |> Enum.reduce({List.duplicate(".", n), empty_start}, fn {cell, rev_idx},
                                                               {acc, empty} ->
        r = n - 1 - rev_idx

        cond do
          cell == "*" ->
            acc = List.replace_at(acc, r, "*")
            {acc, r - 1}

          cell == "#" ->
            acc = List.replace_at(acc, empty, "#")
            {acc, empty - 1}

          true ->
            {acc, empty}
        end
      end)

    new_col
  end
end
```

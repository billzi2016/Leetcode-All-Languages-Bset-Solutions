# 0807. Max Increase to Keep City Skyline

## Cpp

```cpp
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> rowMax(n, 0), colMax(n, 0);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                rowMax[i] = max(rowMax[i], grid[i][j]);
                colMax[j] = max(colMax[j], grid[i][j]);
            }
        }
        int totalIncrease = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int allowedHeight = min(rowMax[i], colMax[j]);
                totalIncrease += allowedHeight - grid[i][j];
            }
        }
        return totalIncrease;
    }
};
```

## Java

```java
class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int n = grid.length;
        int[] rowMax = new int[n];
        int[] colMax = new int[n];
        
        // Compute maximums for each row and column
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > rowMax[i]) rowMax[i] = grid[i][j];
                if (grid[i][j] > colMax[j]) colMax[j] = grid[i][j];
            }
        }
        
        int totalIncrease = 0;
        // Calculate possible increase for each cell
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int allowedHeight = Math.min(rowMax[i], colMax[j]);
                totalIncrease += allowedHeight - grid[i][j];
            }
        }
        
        return totalIncrease;
    }
}
```

## Python

```python
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]
        total_increase = 0
        for i in range(n):
            for j in range(n):
                allowed_height = min(row_max[i], col_max[j])
                total_increase += allowed_height - grid[i][j]
        return total_increase
```

## Python3

```python
from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]
        total_increase = 0
        for i in range(n):
            for j in range(n):
                allowed_height = min(row_max[i], col_max[j])
                total_increase += allowed_height - grid[i][j]
        return total_increase
```

## C

```c
int maxIncreaseKeepingSkyline(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int row_max[55] = {0};
    int col_max[55] = {0};

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] > row_max[i]) row_max[i] = grid[i][j];
            if (grid[i][j] > col_max[j]) col_max[j] = grid[i][j];
        }
    }

    int totalIncrease = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int allowed = row_max[i] < col_max[j] ? row_max[i] : col_max[j];
            totalIncrease += allowed - grid[i][j];
        }
    }

    return totalIncrease;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxIncreaseKeepingSkyline(int[][] grid)
    {
        int n = grid.Length;
        int[] rowMax = new int[n];
        int[] colMax = new int[n];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] > rowMax[i]) rowMax[i] = grid[i][j];
                if (grid[i][j] > colMax[j]) colMax[j] = grid[i][j];
            }
        }

        int totalIncrease = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int allowedHeight = Math.Min(rowMax[i], colMax[j]);
                totalIncrease += allowedHeight - grid[i][j];
            }
        }

        return totalIncrease;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxIncreaseKeepingSkyline = function(grid) {
    const n = grid.length;
    const rowMax = new Array(n).fill(0);
    const colMax = new Array(n).fill(0);
    
    // Compute maximums for each row and column
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const val = grid[i][j];
            if (val > rowMax[i]) rowMax[i] = val;
            if (val > colMax[j]) colMax[j] = val;
        }
    }
    
    let totalIncrease = 0;
    // Calculate possible increase for each cell
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const allowedHeight = Math.min(rowMax[i], colMax[j]);
            totalIncrease += allowedHeight - grid[i][j];
        }
    }
    
    return totalIncrease;
};
```

## Typescript

```typescript
function maxIncreaseKeepingSkyline(grid: number[][]): number {
    const n = grid.length;
    const rowMax = new Array(n).fill(0);
    const colMax = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] > rowMax[i]) rowMax[i] = grid[i][j];
            if (grid[i][j] > colMax[j]) colMax[j] = grid[i][j];
        }
    }
    let total = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const allowed = Math.min(rowMax[i], colMax[j]);
            total += allowed - grid[i][j];
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxIncreaseKeepingSkyline($grid) {
        $n = count($grid);
        $rowMax = [];
        for ($i = 0; $i < $n; $i++) {
            $rowMax[$i] = max($grid[$i]);
        }

        $colMax = array_fill(0, $n, 0);
        for ($j = 0; $j < $n; $j++) {
            $max = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($grid[$i][$j] > $max) {
                    $max = $grid[$i][$j];
                }
            }
            $colMax[$j] = $max;
        }

        $total = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $allowed = min($rowMax[$i], $colMax[$j]);
                $total += $allowed - $grid[$i][$j];
            }
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maxIncreaseKeepingSkyline(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var rowMax = Array(repeating: 0, count: n)
        var colMax = Array(repeating: 0, count: n)
        
        for i in 0..<n {
            for j in 0..<n {
                rowMax[i] = max(rowMax[i], grid[i][j])
                colMax[j] = max(colMax[j], grid[i][j])
            }
        }
        
        var totalIncrease = 0
        for i in 0..<n {
            for j in 0..<n {
                let allowedHeight = min(rowMax[i], colMax[j])
                totalIncrease += allowedHeight - grid[i][j]
            }
        }
        return totalIncrease
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxIncreaseKeepingSkyline(grid: Array<IntArray>): Int {
        val n = grid.size
        val rowMax = IntArray(n)
        val colMax = IntArray(n)

        for (i in 0 until n) {
            var rmax = 0
            for (j in 0 until n) {
                if (grid[i][j] > rmax) rmax = grid[i][j]
            }
            rowMax[i] = rmax
        }

        for (j in 0 until n) {
            var cmax = 0
            for (i in 0 until n) {
                if (grid[i][j] > cmax) cmax = grid[i][j]
            }
            colMax[j] = cmax
        }

        var total = 0
        for (i in 0 until n) {
            for (j in 0 until n) {
                val allowed = kotlin.math.min(rowMax[i], colMax[j])
                total += allowed - grid[i][j]
            }
        }
        return total
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxIncreaseKeepingSkyline(List<List<int>> grid) {
    int n = grid.length;
    List<int> rowMax = List.filled(n, 0);
    List<int> colMax = List.filled(n, 0);

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int val = grid[i][j];
        rowMax[i] = max(rowMax[i], val);
        colMax[j] = max(colMax[j], val);
      }
    }

    int total = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        total += min(rowMax[i], colMax[j]) - grid[i][j];
      }
    }
    return total;
  }
}
```

## Golang

```go
func maxIncreaseKeepingSkyline(grid [][]int) int {
    n := len(grid)
    if n == 0 {
        return 0
    }
    rowMax := make([]int, n)
    colMax := make([]int, n)

    // Compute maximums for each row and column
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] > rowMax[i] {
                rowMax[i] = grid[i][j]
            }
            if grid[i][j] > colMax[j] {
                colMax[j] = grid[i][j]
            }
        }
    }

    // Calculate total possible increase
    total := 0
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            allowedHeight := rowMax[i]
            if colMax[j] < allowedHeight {
                allowedHeight = colMax[j]
            }
            total += allowedHeight - grid[i][j]
        }
    }

    return total
}
```

## Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def max_increase_keeping_skyline(grid)
  n = grid.size
  row_max = grid.map { |row| row.max }
  col_max = Array.new(n) { |c| grid.map { |row| row[c] }.max }

  increase = 0
  n.times do |r|
    n.times do |c|
      allowed_height = [row_max[r], col_max[c]].min
      increase += allowed_height - grid[r][c]
    end
  end
  increase
end
```

## Scala

```scala
object Solution {
    def maxIncreaseKeepingSkyline(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        val rowMax = new Array[Int](n)
        val colMax = new Array[Int](n)

        for (i <- 0 until n) {
            var rmax = 0
            for (j <- 0 until n) {
                if (grid(i)(j) > rmax) rmax = grid(i)(j)
                if (grid(i)(j) > colMax(j)) colMax(j) = grid(i)(j)
            }
            rowMax(i) = rmax
        }

        var total = 0
        for (i <- 0 until n; j <- 0 until n) {
            val allowed = math.min(rowMax(i), colMax(j))
            total += allowed - grid(i)(j)
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_increase_keeping_skyline(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 0 {
            return 0;
        }
        let mut row_max = vec![0; n];
        let mut col_max = vec![0; n];

        // Compute max for each row and column
        for r in 0..n {
            for c in 0..n {
                let val = grid[r][c];
                if val > row_max[r] {
                    row_max[r] = val;
                }
                if val > col_max[c] {
                    col_max[c] = val;
                }
            }
        }

        // Calculate total increase
        let mut total = 0i32;
        for r in 0..n {
            for c in 0..n {
                let allowed = row_max[r].min(col_max[c]);
                total += allowed - grid[r][c];
            }
        }
        total
    }
}
```

## Racket

```racket
(define/contract (max-increase-keeping-skyline grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (row-maxes (map (lambda (row) (apply max row)) grid))
         (col-maxes
           (let loop ((c 0) (acc '()))
             (if (= c n)
                 (reverse acc)
                 (let ((col (map (lambda (row) (list-ref row c)) grid)))
                   (loop (+ c 1) (cons (apply max col) acc)))))))
    (for/sum ([r (in-range n)]
              [c (in-range n)])
      (let* ((allowed (min (list-ref row-maxes r)
                           (list-ref col-maxes c)))
             (current (list-ref (list-ref grid r) c))
             (increase (- allowed current)))
        (if (> increase 0) increase 0)))))
```

## Erlang

```erlang
-module(solution).
-export([max_increase_keeping_skyline/1]).

-spec max_increase_keeping_skyline(Grid :: [[integer()]]) -> integer().
max_increase_keeping_skyline(Grid) ->
    RowMaxes = [lists:max(Row) || Row <- Grid],
    N = length(Grid),
    ColMaxes = [col_max(Grid, Index) || Index <- lists:seq(1, N)],
    increase_sum(Grid, RowMaxes, ColMaxes, 0).

%% Compute maximum of a column (1‑based index)
-spec col_max([[integer()]], integer()) -> integer().
col_max(Grid, Index) ->
    Values = [lists:nth(Index, Row) || Row <- Grid],
    lists:max(Values).

%% Accumulate total increase over all rows
-spec increase_sum([[integer()]], [integer()], [integer()], integer()) -> integer().
increase_sum([], [], _ColMaxes, Acc) ->
    Acc;
increase_sum([Row|RestRows], [Rmax|RestRowMaxes], ColMaxes, Acc) ->
    RowInc = increase_row(Row, Rmax, ColMaxes, 0),
    increase_sum(RestRows, RestRowMaxes, ColMaxes, Acc + RowInc).

%% Accumulate increase for a single row
-spec increase_row([integer()], integer(), [integer()], integer()) -> integer().
increase_row([], _Rmax, [], Acc) ->
    Acc;
increase_row([Cell|RestCells], Rmax, [Cmax|RestColMaxes], Acc) ->
    NewHeight = erlang:min(Rmax, Cmax),
    increase_row(RestCells, Rmax, RestColMaxes, Acc + (NewHeight - Cell)).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_increase_keeping_skyline(grid :: [[integer]]) :: integer
  def max_increase_keeping_skyline(grid) do
    row_maxes = Enum.map(grid, &Enum.max/1)
    n = length(grid)

    col_maxes =
      for c <- 0..(n - 1) do
        grid
        |> Enum.map(fn row -> Enum.at(row, c) end)
        |> Enum.max()
      end

    Enum.with_index(grid)
    |> Enum.reduce(0, fn {row, r_idx}, acc ->
      Enum.with_index(row)
      |> Enum.reduce(acc, fn {val, c_idx}, inner_acc ->
        allowed = min(Enum.at(row_maxes, r_idx), Enum.at(col_maxes, c_idx))
        inner_acc + (allowed - val)
      end)
    end)
  end
end
```

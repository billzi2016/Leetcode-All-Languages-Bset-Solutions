# 1351. Count Negative Numbers in a Sorted Matrix

## Cpp

```cpp
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        int i = m - 1, j = 0;
        int cnt = 0;
        while (i >= 0 && j < n) {
            if (grid[i][j] < 0) {
                cnt += n - j;
                --i;
            } else {
                ++j;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countNegatives(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int row = m - 1;
        int col = 0;
        int count = 0;
        while (row >= 0 && col < n) {
            if (grid[row][col] < 0) {
                count += n - col;
                row--;
            } else {
                col++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        row, col = m - 1, 0
        count = 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                # all elements to the right in this row are also negative
                count += (n - col)
                row -= 1
            else:
                col += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        row, col = 0, n - 1
        cnt = 0
        while row < m and col >= 0:
            if grid[row][col] < 0:
                cnt += (m - row)
                col -= 1
            else:
                row += 1
        return cnt
```

## C

```c
int countNegatives(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int rows = gridSize;
    int cols = gridColSize[0];
    int row = rows - 1;
    int col = 0;
    int count = 0;
    
    while (row >= 0 && col < cols) {
        if (grid[row][col] < 0) {
            // all elements to the right are also negative
            count += cols - col;
            row--; // move up to previous row
        } else {
            col++; // move right to find first negative in this column
        }
    }
    
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountNegatives(int[][] grid)
    {
        int m = grid.Length;
        if (m == 0) return 0;
        int n = grid[0].Length;

        int count = 0;
        int row = m - 1;
        int col = 0;

        while (row >= 0 && col < n)
        {
            if (grid[row][col] < 0)
            {
                // All elements to the right are also negative
                count += n - col;
                row--;
            }
            else
            {
                col++;
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    let m = grid.length;
    if (m === 0) return 0;
    let n = grid[0].length;
    let i = m - 1; // start from bottom row
    let j = 0;     // start from leftmost column
    let count = 0;
    
    while (i >= 0 && j < n) {
        if (grid[i][j] < 0) {
            // all elements to the right are also negative
            count += (n - j);
            i--; // move up to previous row
        } else {
            j++; // move right to find first negative in this row
        }
    }
    
    return count;
};
```

## Typescript

```typescript
function countNegatives(grid: number[][]): number {
    const m = grid.length;
    if (m === 0) return 0;
    const n = grid[0].length;
    let row = m - 1;
    let col = 0;
    let count = 0;

    while (row >= 0 && col < n) {
        if (grid[row][col] < 0) {
            // All elements to the right are also negative
            count += n - col;
            row--;
        } else {
            col++;
        }
    }

    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countNegatives($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        $row = $m - 1;
        $col = 0;
        $count = 0;

        while ($row >= 0 && $col < $n) {
            if ($grid[$row][$col] < 0) {
                // All elements to the right are also negative
                $count += $n - $col;
                $row--;
            } else {
                $col++;
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countNegatives(_ grid: [[Int]]) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var row = m - 1
        var col = 0
        var count = 0
        
        while row >= 0 && col < n {
            if grid[row][col] < 0 {
                // All elements to the right in this row are also negative
                count += n - col
                row -= 1
            } else {
                col += 1
            }
        }
        
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countNegatives(grid: Array<IntArray>): Int {
        var m = grid.size
        if (m == 0) return 0
        val n = grid[0].size
        var i = m - 1
        var j = 0
        var count = 0
        while (i >= 0 && j < n) {
            if (grid[i][j] < 0) {
                count += n - j
                i--
            } else {
                j++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countNegatives(List<List<int>> grid) {
    int m = grid.length;
    if (m == 0) return 0;
    int n = grid[0].length;
    int row = 0;
    int col = n - 1;
    int count = 0;

    while (row < m && col >= 0) {
      if (grid[row][col] < 0) {
        // All elements below in this column are also negative
        count += (m - row);
        col--;
      } else {
        row++;
      }
    }

    return count;
  }
}
```

## Golang

```go
func countNegatives(grid [][]int) int {
    m := len(grid)
    if m == 0 {
        return 0
    }
    n := len(grid[0])
    row, col := m-1, 0
    count := 0
    for row >= 0 && col < n {
        if grid[row][col] < 0 {
            count += n - col
            row--
        } else {
            col++
        }
    }
    return count
}
```

## Ruby

```ruby
def count_negatives(grid)
  m = grid.size
  n = grid[0].size
  i = m - 1
  j = 0
  cnt = 0
  while i >= 0 && j < n
    if grid[i][j] < 0
      cnt += n - j
      i -= 1
    else
      j += 1
    end
  end
  cnt
end
```

## Scala

```scala
object Solution {
    def countNegatives(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        var i = m - 1
        var j = 0
        var count = 0
        while (i >= 0 && j < n) {
            if (grid(i)(j) < 0) {
                count += n - j
                i -= 1
            } else {
                j += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        let mut row: i32 = (m as i32) - 1;
        let mut col: usize = 0;
        let mut count: i32 = 0;

        while row >= 0 && col < n {
            if grid[row as usize][col] < 0 {
                // all elements to the right are also negative
                count += (n - col) as i32;
                row -= 1;
            } else {
                col += 1;
            }
        }

        count
    }
}
```

## Racket

```racket
#lang racket

(define/contract (count-negatives grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (for*/sum ([row grid]
             [x row])
    (if (< x 0) 1 0)))
```

## Erlang

```erlang
-module(solution).
-export([count_negatives/1]).

-spec count_negatives(Grid :: [[integer()]]) -> integer().
count_negatives([]) ->
    0;
count_negatives(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    count_negatives(Grid, 0, N - 1, M, N).

count_negatives(_Grid, I, _J, M, _N) when I >= M ->
    0;
count_negatives(_Grid, _I, J, _M, N) when J < 0 ->
    0;
count_negatives(Grid, I, J, M, N) ->
    Row = lists:nth(I + 1, Grid),
    Val = lists:nth(J + 1, Row),
    if
        Val < 0 ->
            (M - I) + count_negatives(Grid, I, J - 1, M, N);
        true ->
            count_negatives(Grid, I + 1, J, M, N)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_negatives(grid :: [[integer]]) :: integer
  def count_negatives(grid) do
    m = length(grid)
    n = grid |> List.first() |> length()
    traverse(grid, m - 1, 0, n, 0)
  end

  defp traverse(_grid, i, _j, _n, acc) when i < 0, do: acc
  defp traverse(_grid, _i, j, n, acc) when j >= n, do: acc

  defp traverse(grid, i, j, n, acc) do
    val = grid |> Enum.at(i) |> Enum.at(j)

    if val < 0 do
      # All elements to the right are also negative
      traverse(grid, i - 1, j, n, acc + (n - j))
    else
      traverse(grid, i, j + 1, n, acc)
    end
  end
end
```

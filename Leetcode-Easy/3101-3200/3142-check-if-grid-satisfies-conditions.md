# 3142. Check if Grid Satisfies Conditions

## Cpp

```cpp
class Solution {
public:
    bool satisfiesConditions(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return true;
        int n = grid[0].size();
        // Check each column has same value in all rows
        for (int j = 0; j < n; ++j) {
            int val = grid[0][j];
            for (int i = 1; i < m; ++i) {
                if (grid[i][j] != val) return false;
            }
        }
        // Check adjacent columns have different values
        for (int j = 1; j < n; ++j) {
            if (grid[0][j] == grid[0][j - 1]) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean satisfiesConditions(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        for (int j = 0; j < n; j++) {
            int val = grid[0][j];
            // Check column uniformity
            for (int i = 1; i < m; i++) {
                if (grid[i][j] != val) {
                    return false;
                }
            }
            // Check adjacent columns have different values
            if (j > 0 && val == grid[0][j - 1]) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        if not grid:
            return True
        m = len(grid)
        n = len(grid[0])
        for j in range(n):
            col_val = grid[0][j]
            # check column uniformity
            for i in range(1, m):
                if grid[i][j] != col_val:
                    return False
            # check adjacent columns differ
            if j > 0 and grid[0][j] == grid[0][j - 1]:
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        for j in range(n):
            col_val = grid[0][j]
            if col_val in seen:
                return False
            seen.add(col_val)
            for i in range(1, m):
                if grid[i][j] != col_val:
                    return False
        return True
```

## C

```c
#include <stdbool.h>

bool satisfiesConditions(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return true;
    int n = gridColSize[0];
    
    // Check each column has the same value in all rows
    for (int j = 0; j < n; ++j) {
        int val = grid[0][j];
        for (int i = 1; i < gridSize; ++i) {
            if (grid[i][j] != val) return false;
        }
    }
    
    // Check adjacent columns have different values
    for (int j = 0; j + 1 < n; ++j) {
        if (grid[0][j] == grid[0][j + 1]) return false;
    }
    
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool SatisfiesConditions(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        // Each column must have the same value in all rows
        for (int col = 0; col < n; col++) {
            int val = grid[0][col];
            for (int row = 1; row < m; row++) {
                if (grid[row][col] != val) return false;
            }
        }

        // Values of different columns must be distinct
        var seen = new System.Collections.Generic.HashSet<int>();
        for (int col = 0; col < n; col++) {
            int val = grid[0][col];
            if (!seen.Add(val)) return false;
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var satisfiesConditions = function(grid) {
    const m = grid.length;
    if (m === 0) return true;
    const n = grid[0].length;

    // Check each column has the same value in all rows
    for (let j = 0; j < n; ++j) {
        const val = grid[0][j];
        for (let i = 1; i < m; ++i) {
            if (grid[i][j] !== val) return false;
        }
    }

    // Check adjacent columns have different values (using first row)
    for (let j = 0; j + 1 < n; ++j) {
        if (grid[0][j] === grid[0][j + 1]) return false;
    }

    return true;
};
```

## Typescript

```typescript
function satisfiesConditions(grid: number[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;

    // Each column must have identical values across all rows
    for (let col = 0; col < n; col++) {
        const expected = grid[0][col];
        for (let row = 1; row < m; row++) {
            if (grid[row][col] !== expected) return false;
        }
    }

    // Adjacent columns must have different values
    for (let col = 1; col < n; col++) {
        if (grid[0][col] === grid[0][col - 1]) return false;
    }

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function satisfiesConditions($grid) {
        $m = count($grid);
        if ($m === 0) {
            return true;
        }
        $n = count($grid[0]);

        // Check each column has the same value in all rows
        for ($j = 0; $j < $n; $j++) {
            $val = $grid[0][$j];
            for ($i = 1; $i < $m; $i++) {
                if ($grid[$i][$j] !== $val) {
                    return false;
                }
            }
        }

        // Check adjacent columns have different values
        for ($j = 1; $j < $n; $j++) {
            if ($grid[0][$j] === $grid[0][$j - 1]) {
                return false;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func satisfiesConditions(_ grid: [[Int]]) -> Bool {
        let m = grid.count
        if m == 0 { return true }
        let n = grid[0].count
        
        // Each column must have identical values across rows
        for col in 0..<n {
            let expected = grid[0][col]
            for row in 1..<m {
                if grid[row][col] != expected {
                    return false
                }
            }
        }
        
        // Adjacent columns must have different values
        for col in 0..<(n - 1) {
            if grid[0][col] == grid[0][col + 1] {
                return false
            }
        }
        
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun satisfiesConditions(grid: Array<IntArray>): Boolean {
        if (grid.isEmpty() || grid[0].isEmpty()) return true
        val m = grid.size
        val n = grid[0].size
        var prevVal = -1
        for (j in 0 until n) {
            val colVal = grid[0][j]
            // check column uniformity
            for (i in 1 until m) {
                if (grid[i][j] != colVal) return false
            }
            // check adjacent columns differ
            if (j > 0 && colVal == prevVal) return false
            prevVal = colVal
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool satisfiesConditions(List<List<int>> grid) {
    int m = grid.length;
    if (m == 0) return true;
    int n = grid[0].length;

    for (int j = 0; j < n; j++) {
      int colVal = grid[0][j];
      // Check column uniformity
      for (int i = 1; i < m; i++) {
        if (grid[i][j] != colVal) return false;
      }
      // Check adjacent first-row values differ
      if (j > 0 && grid[0][j] == grid[0][j - 1]) return false;
    }
    return true;
  }
}
```

## Golang

```go
func satisfiesConditions(grid [][]int) bool {
    if len(grid) == 0 || len(grid[0]) == 0 {
        return true
    }
    rows, cols := len(grid), len(grid[0])

    // Check each column has the same value in all rows
    for c := 0; c < cols; c++ {
        val := grid[0][c]
        for r := 1; r < rows; r++ {
            if grid[r][c] != val {
                return false
            }
        }
    }

    // Check adjacent columns have different values (compare top row)
    for c := 0; c+1 < cols; c++ {
        if grid[0][c] == grid[0][c+1] {
            return false
        }
    }

    return true
}
```

## Ruby

```ruby
def satisfies_conditions(grid)
  m = grid.size
  n = grid[0].size
  col_vals = []
  (0...n).each do |j|
    val = grid[0][j]
    (1...m).each do |i|
      return false if grid[i][j] != val
    end
    col_vals << val
  end
  (0...n-1).each do |j|
    return false if col_vals[j] == col_vals[j + 1]
  end
  true
end
```

## Scala

```scala
object Solution {
    def satisfiesConditions(grid: Array[Array[Int]]): Boolean = {
        val m = grid.length
        if (m == 0) return true
        val n = grid(0).length

        // each column must have identical values
        for (j <- 0 until n) {
            val v = grid(0)(j)
            var i = 1
            while (i < m) {
                if (grid(i)(j) != v) return false
                i += 1
            }
        }

        // first row values must be all distinct
        val seen = scala.collection.mutable.HashSet[Int]()
        for (j <- 0 until n) {
            val v = grid(0)(j)
            if (!seen.add(v)) return false
        }

        true
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn satisfies_conditions(grid: Vec<Vec<i32>>) -> bool {
        if grid.is_empty() {
            return true;
        }
        let m = grid.len();
        let n = grid[0].len();

        // Each column must have the same value in all rows
        for j in 0..n {
            let val = grid[0][j];
            for i in 1..m {
                if grid[i][j] != val {
                    return false;
                }
            }
        }

        // Values across columns (in any row) must be distinct.
        // Since columns are uniform, checking the first row suffices.
        let mut seen = HashSet::new();
        for &v in &grid[0] {
            if !seen.insert(v) {
                return false;
            }
        }

        true
    }
}
```

## Racket

```racket
(define/contract (satisfies-conditions grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (car grid)))))
    (and (> m 0) (> n 0)
         ;; each column must have identical values
         (let loop-col ((j 0))
           (cond [(= j n) #t]
                 [else
                  (let ((val (list-ref (car grid) j)))
                    (let inner ((i 1))
                      (cond [(= i m) (loop-col (+ j 1))]
                            [(equal? (list-ref (list-ref grid i) j) val)
                             (inner (+ i 1))]
                            [else #f])))]))
         ;; adjacent columns must differ
         (let loop-adj ((j 0))
           (or (= j (- n 1))
               (and (not (equal? (list-ref (car grid) j)
                                 (list-ref (car grid) (+ j 1))))
                    (loop-adj (+ j 1)))))))))
```

## Erlang

```erlang
-spec satisfies_conditions(Grid :: [[integer()]]) -> boolean().
satisfies_conditions([]) ->
    true;
satisfies_conditions([FirstRow|RestRows]=Grid) ->
    N = length(FirstRow),
    ColIndices = lists:seq(0, N - 1),
    ColumnsOk = check_all_columns(Grid, ColIndices),
    AdjacentOk = adj_distinct(FirstRow),
    ColumnsOk andalso AdjacentOk.

check_all_columns(_Grid, []) ->
    true;
check_all_columns([FirstRow|RestRows]=Grid, [Idx | Idxs]) ->
    Expected = lists:nth(Idx + 1, FirstRow),
    case check_column(Idx, RestRows, Expected) of
        false -> false;
        true -> check_all_columns(Grid, Idxs)
    end.

check_column(_Idx, [], _Expected) ->
    true;
check_column(Idx, [Row | Rows], Expected) ->
    case lists:nth(Idx + 1, Row) of
        Expected -> check_column(Idx, Rows, Expected);
        _ -> false
    end.

adj_distinct([]) ->
    true;
adj_distinct([_]) ->
    true;
adj_distinct([A, B | Rest]) ->
    if
        A =/= B -> adj_distinct([B | Rest]);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec satisfies_conditions(grid :: [[integer]]) :: boolean
  def satisfies_conditions(grid) do
    rows = length(grid)
    cols = grid |> hd() |> length()

    # Verify each column has the same value in all rows
    columns_constant? =
      Enum.all?(0..(cols - 1), fn j ->
        first_val = get_in(grid, [Access.at(0), Access.at(j)])

        Enum.all?(1..(rows - 1), fn i ->
          get_in(grid, [Access.at(i), Access.at(j)]) == first_val
        end)
      end)

    if not columns_constant? do
      false
    else
      # Verify adjacent columns have different values (check first row)
      first_row = hd(grid)

      Enum.all?(0..(cols - 2), fn j ->
        Enum.at(first_row, j) != Enum.at(first_row, j + 1)
      end)
    end
  end
end
```

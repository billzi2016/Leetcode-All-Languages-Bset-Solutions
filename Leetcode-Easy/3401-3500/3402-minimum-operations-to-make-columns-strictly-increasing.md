# 3402. Minimum Operations to Make Columns Strictly Increasing

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long ops = 0;
        for (int j = 0; j < n; ++j) {
            for (int i = 1; i < m; ++i) {
                int need = grid[i-1][j] + 1;
                if (grid[i][j] < need) {
                    ops += need - grid[i][j];
                    grid[i][j] = need;
                }
            }
        }
        return (int)ops;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long ops = 0;
        for (int j = 0; j < n; ++j) {
            for (int i = 1; i < m; ++i) {
                int required = grid[i - 1][j] + 1;
                if (grid[i][j] < required) {
                    ops += required - grid[i][j];
                    grid[i][j] = required;
                }
            }
        }
        return (int) ops;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ops = 0
        for col in range(n):
            for row in range(1, m):
                if grid[row][col] <= grid[row - 1][col]:
                    need = grid[row - 1][col] + 1 - grid[row][col]
                    ops += need
                    grid[row][col] += need
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ops = 0
        for col in range(n):
            for row in range(m - 1):
                needed = grid[row][col] + 1
                if grid[row + 1][col] < needed:
                    inc = needed - grid[row + 1][col]
                    ops += inc
                    grid[row + 1][col] = needed
        return ops
```

## C

```c
int minimumOperations(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int rows = gridSize;
    int cols = gridColSize[0];
    long long ops = 0;
    for (int j = 0; j < cols; ++j) {
        int prev = grid[0][j];
        for (int i = 1; i < rows; ++i) {
            int need = prev + 1;
            if (grid[i][j] < need) {
                ops += need - grid[i][j];
                prev = need;
            } else {
                prev = grid[i][j];
            }
        }
    }
    return (int)ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumOperations(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        long ops = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 1; i < m; i++) {
                int required = grid[i - 1][j] + 1;
                if (grid[i][j] < required) {
                    ops += required - grid[i][j];
                    grid[i][j] = required;
                }
            }
        }
        return (int)ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumOperations = function(grid) {
    let m = grid.length;
    if (m === 0) return 0;
    let n = grid[0].length;
    let ops = 0;
    for (let col = 0; col < n; col++) {
        for (let row = 1; row < m; row++) {
            const prev = grid[row - 1][col];
            if (grid[row][col] <= prev) {
                const need = prev + 1 - grid[row][col];
                ops += need;
                grid[row][col] += need;
            }
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minimumOperations(grid: number[][]): number {
    const m = grid.length;
    if (m === 0) return 0;
    const n = grid[0].length;
    let operations = 0;

    for (let col = 0; col < n; col++) {
        let prev = grid[0][col];
        for (let row = 1; row < m; row++) {
            const cur = grid[row][col];
            const needed = prev + 1;
            if (cur < needed) {
                operations += needed - cur;
                prev = needed;
            } else {
                prev = cur;
            }
        }
    }

    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumOperations($grid) {
        $m = count($grid);
        if ($m === 0) return 0;
        $n = count($grid[0]);
        $ops = 0;
        for ($j = 0; $j < $n; $j++) {
            for ($i = 1; $i < $m; $i++) {
                $required = $grid[$i - 1][$j] + 1;
                if ($grid[$i][$j] < $required) {
                    $ops += $required - $grid[$i][$j];
                    $grid[$i][$j] = $required;
                }
            }
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ grid: [[Int]]) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var ops = 0
        var prev = Array(repeating: 0, count: n)
        // Initialize with first row values
        for j in 0..<n {
            prev[j] = grid[0][j]
        }
        if m > 1 {
            for i in 1..<m {
                for j in 0..<n {
                    let cur = grid[i][j]
                    let needed = max(cur, prev[j] + 1)
                    ops += needed - cur
                    prev[j] = needed
                }
            }
        }
        return ops
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(grid: Array<IntArray>): Int {
        var ops = 0L
        val m = grid.size
        val n = grid[0].size
        for (j in 0 until n) {
            var prev = grid[0][j]
            for (i in 1 until m) {
                val need = prev + 1
                if (grid[i][j] < need) {
                    ops += (need - grid[i][j])
                    grid[i][j] = need
                }
                prev = grid[i][j]
            }
        }
        return ops.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int ops = 0;
    for (int col = 0; col < n; col++) {
      for (int row = 1; row < m; row++) {
        int required = grid[row - 1][col] + 1;
        if (grid[row][col] < required) {
          ops += required - grid[row][col];
          grid[row][col] = required;
        }
      }
    }
    return ops;
  }
}
```

## Golang

```go
func minimumOperations(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])
    ops := 0
    for c := 0; c < cols; c++ {
        prev := grid[0][c]
        for r := 1; r < rows; r++ {
            cur := grid[r][c]
            if cur <= prev {
                needed := prev + 1
                ops += needed - cur
                prev = needed
            } else {
                prev = cur
            }
        }
    }
    return ops
}
```

## Ruby

```ruby
def minimum_operations(grid)
  m = grid.length
  n = grid[0].length
  operations = 0

  n.times do |col|
    (1...m).each do |row|
      needed = grid[row - 1][col] + 1
      if grid[row][col] < needed
        diff = needed - grid[row][col]
        operations += diff
        grid[row][col] = needed
      end
    end
  end

  operations
end
```

## Scala

```scala
object Solution {
    def minimumOperations(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        var ops: Long = 0L
        for (j <- 0 until n) {
            for (i <- 1 until m) {
                if (grid(i)(j) <= grid(i - 1)(j)) {
                    val need = grid(i - 1)(j) + 1 - grid(i)(j)
                    ops += need
                    grid(i)(j) = grid(i - 1)(j) + 1
                }
            }
        }
        ops.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        let mut ops: i32 = 0;
        for col in 0..n {
            for row in 1..m {
                let needed = grid[row - 1][col] + 1;
                if grid[row][col] < needed {
                    let diff = needed - grid[row][col];
                    ops += diff;
                    grid[row][col] = needed;
                }
            }
        }
        ops
    }
}
```

## Racket

```racket
(define/contract (minimum-operations grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (first grid)))))
    (for/sum ([j (in-range n)])
      (let loop ((i 1)
                 (prev (list-ref (list-ref grid 0) j))
                 (ops 0))
        (if (= i m)
            ops
            (let* ((curr (list-ref (list-ref grid i) j))
                   (need (+ prev 1))
                   (add (max 0 (- need curr)))
                   (newCurr (+ curr add)))
              (loop (+ i 1) newCurr (+ ops add))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_operations/1]).

-spec minimum_operations(Grid :: [[integer()]]) -> integer().
minimum_operations([]) ->
    0;
minimum_operations([FirstRow | RestRows]) ->
    {TotalOps, _} = lists:foldl(
        fun(Row, {AccOps, PrevRow}) ->
            {NewPrev, OpsRow} = process_row(Row, PrevRow),
            {AccOps + OpsRow, NewPrev}
        end,
        {0, FirstRow},
        RestRows
    ),
    TotalOps.

-spec process_row([integer()], [integer()]) -> {[integer()], integer()}.
process_row(Row, Prev) ->
    {RevNewPrev, Ops} = lists:foldl(
        fun({Val, P}, {AccPrev, AccOps}) ->
            Required = P + 1,
            if
                Val >= Required ->
                    {[Val | AccPrev], AccOps};
                true ->
                    Diff = Required - Val,
                    {[Required | AccPrev], AccOps + Diff}
            end
        end,
        {[], 0},
        lists:zip(Row, Prev)
    ),
    {lists:reverse(RevNewPrev), Ops}.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(grid :: [[integer]]) :: integer
  def minimum_operations(grid) do
    rows = length(grid)
    cols = length(hd(grid))

    Enum.reduce(0..cols - 1, 0, fn col, total_ops ->
      {col_ops, _} =
        Enum.reduce(1..rows - 1, {0, Enum.at(Enum.at(grid, 0), col)}, fn row_idx,
                                                                      {ops_acc, prev_val} ->
          cur = Enum.at(Enum.at(grid, row_idx), col)
          needed = prev_val + 1

          if cur >= needed do
            {ops_acc, cur}
          else
            inc = needed - cur
            {ops_acc + inc, needed}
          end
        end)

      total_ops + col_ops
    end)
  end
end
```

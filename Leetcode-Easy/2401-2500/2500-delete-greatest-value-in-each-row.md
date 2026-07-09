# 2500. Delete Greatest Value in Each Row

## Cpp

```cpp
class Solution {
public:
    int deleteGreatestValue(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        for (auto& row : grid) {
            sort(row.begin(), row.end());
        }
        int ans = 0;
        for (int col = n - 1; col >= 0; --col) {
            int mx = 0;
            for (int i = 0; i < m; ++i) {
                mx = max(mx, grid[i][col]);
            }
            ans += mx;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int deleteGreatestValue(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        for (int i = 0; i < m; i++) {
            Arrays.sort(grid[i]); // ascending
        }
        int answer = 0;
        for (int col = 0; col < n; col++) {
            int curMax = 0;
            for (int row = 0; row < m; row++) {
                int val = grid[row][n - 1 - col]; // descending order
                if (val > curMax) {
                    curMax = val;
                }
            }
            answer += curMax;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in grid:
            row.sort(reverse=True)
        total = 0
        n = len(grid[0])
        for c in range(n):
            max_val = 0
            for row in grid:
                if row[c] > max_val:
                    max_val = row[c]
            total += max_val
        return total
```

## Python3

```python
from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)
        n = len(grid[0])
        ans = 0
        for i in range(n):
            max_val = 0
            for row in grid:
                if row[i] > max_val:
                    max_val = row[i]
            ans += max_val
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int deleteGreatestValue(int** grid, int gridSize, int* gridColSize){
    if (gridSize == 0) return 0;
    int n = gridColSize[0];
    for (int i = 0; i < gridSize; ++i) {
        qsort(grid[i], n, sizeof(int), cmp_int);
    }
    int ans = 0;
    for (int col = n - 1; col >= 0; --col) {
        int curMax = 0;
        for (int i = 0; i < gridSize; ++i) {
            if (grid[i][col] > curMax) curMax = grid[i][col];
        }
        ans += curMax;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int DeleteGreatestValue(int[][] grid)
    {
        foreach (var row in grid)
        {
            Array.Sort(row); // ascending order
        }

        int m = grid.Length;
        int n = grid[0].Length;
        int answer = 0;

        for (int col = 0; col < n; col++)
        {
            int currentMax = 0;
            foreach (var row in grid)
            {
                int val = row[n - 1 - col]; // take the greatest remaining element
                if (val > currentMax)
                    currentMax = val;
            }
            answer += currentMax;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var deleteGreatestValue = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    for (let i = 0; i < m; ++i) {
        grid[i].sort((a, b) => b - a);
    }
    let ans = 0;
    for (let col = 0; col < n; ++col) {
        let maxVal = 0;
        for (let row = 0; row < m; ++row) {
            if (grid[row][col] > maxVal) maxVal = grid[row][col];
        }
        ans += maxVal;
    }
    return ans;
};
```

## Typescript

```typescript
function deleteGreatestValue(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    for (let i = 0; i < m; ++i) {
        grid[i].sort((a, b) => a - b);
    }
    let ans = 0;
    for (let col = 0; col < n; ++col) {
        let curMax = 0;
        for (let r = 0; r < m; ++r) {
            const val = grid[r][n - 1 - col];
            if (val > curMax) curMax = val;
        }
        ans += curMax;
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
    function deleteGreatestValue($grid) {
        foreach ($grid as &$row) {
            sort($row);
        }
        unset($row);
        $n = count($grid[0]);
        $ans = 0;
        for ($c = $n - 1; $c >= 0; $c--) {
            $maxVal = 0;
            foreach ($grid as $row) {
                if ($row[$c] > $maxVal) {
                    $maxVal = $row[$c];
                }
            }
            $ans += $maxVal;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func deleteGreatestValue(_ grid: [[Int]]) -> Int {
        var rows = grid.map { $0.sorted() }
        let m = rows.count
        guard m > 0 else { return 0 }
        let n = rows[0].count
        var answer = 0
        for step in 0..<n {
            var curMax = 0
            for r in 0..<m {
                let val = rows[r][n - 1 - step]
                if val > curMax { curMax = val }
            }
            answer += curMax
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun deleteGreatestValue(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        for (row in grid) {
            row.sort()
        }
        var answer = 0
        for (c in n - 1 downTo 0) {
            var curMax = 0
            for (r in 0 until m) {
                if (grid[r][c] > curMax) curMax = grid[r][c]
            }
            answer += curMax
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int deleteGreatestValue(List<List<int>> grid) {
    for (var row in grid) {
      row.sort((a, b) => b - a);
    }
    int m = grid.length;
    int n = grid[0].length;
    int ans = 0;
    for (int j = 0; j < n; ++j) {
      int colMax = 0;
      for (int i = 0; i < m; ++i) {
        if (grid[i][j] > colMax) colMax = grid[i][j];
      }
      ans += colMax;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func deleteGreatestValue(grid [][]int) int {
    for _, row := range grid {
        sort.Ints(row)
    }
    m, n := len(grid), len(grid[0])
    ans := 0
    for col := n - 1; col >= 0; col-- {
        maxVal := 0
        for i := 0; i < m; i++ {
            if grid[i][col] > maxVal {
                maxVal = grid[i][col]
            }
        }
        ans += maxVal
    }
    return ans
}
```

## Ruby

```ruby
def delete_greatest_value(grid)
  grid.each { |row| row.sort!.reverse! }
  ans = 0
  n = grid[0].size
  (0...n).each do |col|
    max_val = 0
    grid.each do |row|
      val = row[col]
      max_val = val if val > max_val
    end
    ans += max_val
  end
  ans
end
```

## Scala

```scala
object Solution {
    def deleteGreatestValue(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length

        // Sort each row in non‑decreasing order
        for (i <- 0 until m) java.util.Arrays.sort(grid(i))

        var answer = 0
        for (c <- (n - 1) to 0 by -1) {
            var maxVal = 0
            var r = 0
            while (r < m) {
                val v = grid(r)(c)
                if (v > maxVal) maxVal = v
                r += 1
            }
            answer += maxVal
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn delete_greatest_value(mut grid: Vec<Vec<i32>>) -> i32 {
        for row in grid.iter_mut() {
            row.sort_unstable_by(|a, b| b.cmp(a));
        }
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        let mut ans = 0;
        for col in 0..n {
            let mut max_val = 0;
            for i in 0..m {
                let v = grid[i][col];
                if v > max_val {
                    max_val = v;
                }
            }
            ans += max_val;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (delete-greatest-value grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted-grid (map (lambda (row) (sort row <)) grid))
         (n (if (null? sorted-grid) 0 (length (car sorted-grid)))))
    (let loop ((col 0) (sum 0))
      (if (= col n)
          sum
          (let* ((col-values (map (lambda (row) (list-ref row col)) sorted-grid))
                 (max-val (apply max col-values)))
            (loop (+ col 1) (+ sum max-val)))))))
```

## Erlang

```erlang
-spec delete_greatest_value(Grid :: [[integer()]]) -> integer().
delete_greatest_value(Grid) ->
    SortedRows = [lists:reverse(lists:sort(Row)) || Row <- Grid],
    N = case Grid of [] -> 0; [First|_] -> length(First) end,
    sum_max_per_col(SortedRows, N).

sum_max_per_col(Rows, N) -> sum_max_per_col(Rows, 0, N, 0).

sum_max_per_col(_Rows, Index, N, Acc) when Index == N ->
    Acc;
sum_max_per_col(Rows, Index, N, Acc) ->
    Values = [lists:nth(Index + 1, Row) || Row <- Rows],
    MaxVal = lists:max(Values),
    sum_max_per_col(Rows, Index + 1, N, Acc + MaxVal).
```

## Elixir

```elixir
defmodule Solution do
  @spec delete_greatest_value(grid :: [[integer]]) :: integer
  def delete_greatest_value(grid) do
    sorted_rows = Enum.map(grid, fn row -> Enum.sort(row, &>=/2) end)
    n = sorted_rows |> hd() |> length()

    0..(n - 1)
    |> Enum.reduce(0, fn col_idx, acc ->
      max_val =
        sorted_rows
        |> Enum.map(&Enum.at(&1, col_idx))
        |> Enum.max()

      acc + max_val
    end)
  end
end
```

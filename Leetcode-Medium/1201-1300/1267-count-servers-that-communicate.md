# 1267. Count Servers that Communicate

## Cpp

```cpp
class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        vector<int> row(m, 0), col(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    ++row[i];
                    ++col[j];
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1 && (row[i] > 1 || col[j] > 1)) {
                    ++ans;
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
    public int countServers(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] rowCounts = new int[m];
        int[] colCounts = new int[n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    rowCounts[i]++;
                    colCounts[j]++;
                }
            }
        }
        
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && (rowCounts[i] > 1 || colCounts[j] > 1)) {
                    result++;
                }
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        row_counts = [0] * m
        col_counts = [0] * n

        for i in range(m):
            cnt = 0
            for j in range(n):
                if grid[i][j]:
                    cnt += 1
                    col_counts[j] += 1
            row_counts[i] = cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row_counts[i] > 1 or col_counts[j] > 1):
                    ans += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_counts = [0] * m
        col_counts = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_counts[i] += 1
                    col_counts[j] += 1

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row_counts[i] > 1 or col_counts[j] > 1):
                    total += 1
        return total
```

## C

```c
int countServers(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0 || gridColSize == NULL) return 0;
    int rows = gridSize;
    int cols = gridColSize[0];
    
    int *rowCount = (int *)calloc(rows, sizeof(int));
    int *colCount = (int *)calloc(cols, sizeof(int));
    if (!rowCount || !colCount) {
        free(rowCount);
        free(colCount);
        return 0;
    }
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }
    
    int result = 0;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1 && (rowCount[i] > 1 || colCount[j] > 1)) {
                result++;
            }
        }
    }
    
    free(rowCount);
    free(colCount);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountServers(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] rowCount = new int[m];
        int[] colCount = new int[n];

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 1)
                {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }

        int result = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 1 && (rowCount[i] > 1 || colCount[j] > 1))
                {
                    result++;
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
var countServers = function(grid) {
    const m = grid.length;
    if (m === 0) return 0;
    const n = grid[0].length;
    
    const rowCounts = new Array(m).fill(0);
    const colCounts = new Array(n).fill(0);
    
    // First pass: count servers in each row and column
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) {
                rowCounts[i]++;
                colCounts[j]++;
            }
        }
    }
    
    // Second pass: count communicable servers
    let result = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1 && (rowCounts[i] > 1 || colCounts[j] > 1)) {
                result++;
            }
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function countServers(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const rowCount = new Array(m).fill(0);
    const colCount = new Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }

    let result = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1 && (rowCount[i] > 1 || colCount[j] > 1)) {
                result++;
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countServers($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);

        $rowCounts = array_fill(0, $m, 0);
        $colCounts = array_fill(0, $n, 0);

        // First pass: count servers in each row and column
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 1) {
                    $rowCounts[$i]++;
                    $colCounts[$j]++;
                }
            }
        }

        // Second pass: count communicable servers
        $result = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 1 && ($rowCounts[$i] > 1 || $colCounts[$j] > 1)) {
                    $result++;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countServers(_ grid: [[Int]]) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        
        var rowCounts = [Int](repeating: 0, count: m)
        var colCounts = [Int](repeating: 0, count: n)
        
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    rowCounts[i] += 1
                    colCounts[j] += 1
                }
            }
        }
        
        var result = 0
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 && (rowCounts[i] > 1 || colCounts[j] > 1) {
                    result += 1
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
    fun countServers(grid: Array<IntArray>): Int {
        val m = grid.size
        if (m == 0) return 0
        val n = grid[0].size
        val rowCount = IntArray(m)
        val colCount = IntArray(n)

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    rowCount[i]++
                    colCount[j]++
                }
            }
        }

        var ans = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1 && (rowCount[i] > 1 || colCount[j] > 1)) {
                    ans++
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
  int countServers(List<List<int>> grid) {
    int m = grid.length;
    if (m == 0) return 0;
    int n = grid[0].length;

    List<int> rowCounts = List.filled(m, 0);
    List<int> colCounts = List.filled(n, 0);

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          rowCounts[i]++;
          colCounts[j]++;
        }
      }
    }

    int result = 0;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1 && (rowCounts[i] > 1 || colCounts[j] > 1)) {
          result++;
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func countServers(grid [][]int) int {
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])

	rowCounts := make([]int, m)
	colCounts := make([]int, n)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				rowCounts[i]++
				colCounts[j]++
			}
		}
	}

	result := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 && (rowCounts[i] > 1 || colCounts[j] > 1) {
				result++
			}
		}
	}
	return result
}
```

## Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def count_servers(grid)
  m = grid.size
  return 0 if m == 0
  n = grid[0].size

  row_counts = Array.new(m, 0)
  col_counts = Array.new(n, 0)

  # First pass: count servers in each row and column
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        row_counts[i] += 1
        col_counts[j] += 1
      end
    end
  end

  # Second pass: sum communicable servers
  result = 0
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 1 && (row_counts[i] > 1 || col_counts[j] > 1)
        result += 1
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def countServers(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        val rowCnt = new Array[Int](m)
        val colCnt = new Array[Int](n)

        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                if (grid(i)(j) == 1) {
                    rowCnt(i) += 1
                    colCnt(j) += 1
                }
                j += 1
            }
            i += 1
        }

        var result = 0
        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                if (grid(i)(j) == 1 && (rowCnt(i) > 1 || colCnt(j) > 1)) {
                    result += 1
                }
                j += 1
            }
            i += 1
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
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

        let mut ans = 0i32;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 && (row_counts[i] > 1 || col_counts[j] > 1) {
                    ans += 1;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-servers grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (car grid))))
         (row-counts (make-vector m 0))
         (col-counts (make-vector n 0)))
    ;; First pass: count servers per row and column
    (for ([i (in-range m)]
          [row (in-list grid)])
      (for ([j (in-range n)]
            [val (in-list row)])
        (when (= val 1)
          (vector-set! row-counts i (+ (vector-ref row-counts i) 1))
          (vector-set! col-counts j (+ (vector-ref col-counts j) 1)))))
    ;; Second pass: sum communicable servers
    (let ((total 0))
      (for ([i (in-range m)]
            [row (in-list grid)])
        (for ([j (in-range n)]
              [val (in-list row)])
          (when (= val 1)
            (when (or (> (vector-ref row-counts i) 1)
                      (> (vector-ref col-counts j) 1))
              (set! total (+ total 1))))))
      total)))
```

## Erlang

```erlang
-spec count_servers(Grid :: [[integer()]]) -> integer().
count_servers([]) ->
    0;
count_servers(Grid) ->
    RowCounts = [length([1 || Cell <- Row, Cell == 1]) || Row <- Grid],
    N = length(hd(Grid)),
    ColCounts = compute_col_counts(Grid, N),
    count_communicable(Grid, RowCounts, ColCounts).

-spec compute_col_counts([[integer()]], integer()) -> [integer()].
compute_col_counts(Rows, N) ->
    Zero = lists:duplicate(N, 0),
    lists:foldl(fun(Row, Acc) -> add_row_to_cols(Row, Acc) end, Zero, Rows).

-spec add_row_to_cols([integer()], [integer()]) -> [integer()].
add_row_to_cols(Row, Acc) ->
    lists:zipwith(
        fun(Cell, Count) ->
            if Cell == 1 -> Count + 1; true -> Count end
        end,
        Row,
        Acc).

-spec count_communicable([[integer()]], [integer()], [integer()]) -> integer().
count_communicable(Grid, RowCounts, ColCounts) ->
    count_communicable(Grid, RowCounts, ColCounts, 0).

-spec count_communicable([[integer()]], [integer()], [integer()], integer()) -> integer().
count_communicable([], [], _, Acc) ->
    Acc;
count_communicable([Row|RestRows], [RCount|RestRC], ColCounts, Acc) ->
    NewAcc = count_row(Row, RCount, ColCounts, Acc),
    count_communicable(RestRows, RestRC, ColCounts, NewAcc).

-spec count_row([integer()], integer(), [integer()], integer()) -> integer().
count_row([], _, [], Acc) ->
    Acc;
count_row([Cell|RestCells], RCount, [CCount|RestCols], Acc) ->
    case Cell of
        1 when (RCount > 1) orelse (CCount > 1) ->
            count_row(RestCells, RCount, RestCols, Acc + 1);
        _ ->
            count_row(RestCells, RCount, RestCols, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_servers(grid :: [[integer]]) :: integer
  def count_servers(grid) do
    m = length(grid)
    n = if m == 0, do: 0, else: grid |> hd() |> length()

    # Count servers in each row
    row_counts = Enum.map(grid, fn row -> Enum.sum(row) end)

    # Count servers in each column using a map for O(1) updates
    col_counts =
      Enum.reduce(grid, %{}, fn row, acc ->
        Enum.with_index(row)
        |> Enum.reduce(acc, fn {val, j}, a ->
          if val == 1 do
            Map.update(a, j, 1, &(&1 + 1))
          else
            a
          end
        end)
      end)

    # Count communicable servers
    grid
    |> Enum.with_index()
    |> Enum.reduce(0, fn {row, i}, total ->
      row
      |> Enum.with_index()
      |> Enum.reduce(total, fn {val, j}, acc ->
        if val == 1 and (Enum.at(row_counts, i) > 1 or Map.get(col_counts, j, 0) > 1) do
          acc + 1
        else
          acc
        end
      end)
    end)
  end
end
```

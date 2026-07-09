# 3546. Equal Sum Grid Partition I

## Cpp

```cpp
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        using ll = long long;
        vector<ll> rowSum(m, 0), colSum(n, 0);
        ll total = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ll val = grid[i][j];
                rowSum[i] += val;
                colSum[j] += val;
                total += val;
            }
        }
        if (total % 2 != 0) return false;
        ll half = total / 2;
        // horizontal cut
        ll pref = 0;
        for (int i = 0; i < m - 1; ++i) {
            pref += rowSum[i];
            if (pref == half) return true;
        }
        // vertical cut
        pref = 0;
        for (int j = 0; j < n - 1; ++j) {
            pref += colSum[j];
            if (pref == half) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long[] rowSum = new long[m];
        long[] colSum = new long[n];
        long total = 0L;

        for (int i = 0; i < m; i++) {
            long rsum = 0L;
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                rsum += val;
                colSum[j] += val;
            }
            rowSum[i] = rsum;
            total += rsum;
        }

        // Horizontal cuts
        long prefix = 0L;
        for (int i = 0; i < m - 1; i++) {
            prefix += rowSum[i];
            if (prefix * 2 == total) return true;
        }

        // Vertical cuts
        prefix = 0L;
        for (int j = 0; j < n - 1; j++) {
            prefix += colSum[j];
            if (prefix * 2 == total) return true;
        }

        return false;
    }
}
```

## Python

```python
class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        row_sums = [0] * m
        col_sums = [0] * n
        total = 0

        for i in range(m):
            rs = 0
            row = grid[i]
            for j, val in enumerate(row):
                rs += val
                col_sums[j] += val
            row_sums[i] = rs
            total += rs

        # Check horizontal cuts
        cum = 0
        for i in range(m - 1):
            cum += row_sums[i]
            if cum * 2 == total:
                return True

        # Check vertical cuts
        cum = 0
        for j in range(n - 1):
            cum += col_sums[j]
            if cum * 2 == total:
                return True

        return False
```

## Python3

```python
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        row_sums = [sum(row) for row in grid]
        total = sum(row_sums)
        if total % 2 != 0:
            return False
        half = total // 2

        cur = 0
        for i in range(m - 1):
            cur += row_sums[i]
            if cur == half:
                return True

        col_sums = [0] * n
        for row in grid:
            for j, val in enumerate(row):
                col_sums[j] += val

        cur = 0
        for j in range(n - 1):
            cur += col_sums[j]
            if cur == half:
                return True

        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool canPartitionGrid(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    if (m == 0) return false;
    int n = gridColSize[0];
    
    long long total = 0;
    long long *rowSum = (long long*)calloc(m, sizeof(long long));
    long long *colSum = (long long*)calloc(n, sizeof(long long));
    if (!rowSum || !colSum) {
        free(rowSum);
        free(colSum);
        return false;
    }
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int val = grid[i][j];
            total += val;
            rowSum[i] += val;
            colSum[j] += val;
        }
    }
    
    // Horizontal cut
    if (m > 1) {
        long long prefix = 0;
        for (int i = 0; i < m - 1; ++i) {
            prefix += rowSum[i];
            if (prefix * 2 == total) {
                free(rowSum);
                free(colSum);
                return true;
            }
        }
    }
    
    // Vertical cut
    if (n > 1) {
        long long prefix = 0;
        for (int j = 0; j < n - 1; ++j) {
            prefix += colSum[j];
            if (prefix * 2 == total) {
                free(rowSum);
                free(colSum);
                return true;
            }
        }
    }
    
    free(rowSum);
    free(colSum);
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanPartitionGrid(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        long total = 0;
        long[] rowSums = new long[m];
        long[] colSums = new long[n];

        for (int i = 0; i < m; i++) {
            int[] row = grid[i];
            for (int j = 0; j < n; j++) {
                int val = row[j];
                total += val;
                rowSums[i] += val;
                colSums[j] += val;
            }
        }

        // Check horizontal cuts
        long prefix = 0;
        for (int i = 0; i < m - 1; i++) {
            prefix += rowSums[i];
            if (prefix * 2 == total) return true;
        }

        // Check vertical cuts
        prefix = 0;
        for (int j = 0; j < n - 1; j++) {
            prefix += colSums[j];
            if (prefix * 2 == total) return true;
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var canPartitionGrid = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const rowSums = new Array(m).fill(0);
    const colSums = new Array(n).fill(0);
    let total = 0;
    
    for (let i = 0; i < m; i++) {
        let rs = 0;
        const row = grid[i];
        for (let j = 0; j < n; j++) {
            const val = row[j];
            rs += val;
            colSums[j] += val;
        }
        rowSums[i] = rs;
        total += rs;
    }
    
    // Check horizontal cuts
    let prefix = 0;
    for (let i = 0; i < m - 1; i++) {
        prefix += rowSums[i];
        if (prefix * 2 === total) return true;
    }
    
    // Check vertical cuts
    prefix = 0;
    for (let j = 0; j < n - 1; j++) {
        prefix += colSums[j];
        if (prefix * 2 === total) return true;
    }
    
    return false;
};
```

## Typescript

```typescript
function canPartitionGrid(grid: number[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    const colSums = new Array(n).fill(0);
    const rowSums = new Array(m);
    let total = 0;

    for (let i = 0; i < m; i++) {
        let rs = 0;
        const row = grid[i];
        for (let j = 0; j < n; j++) {
            const val = row[j];
            rs += val;
            colSums[j] += val;
        }
        rowSums[i] = rs;
        total += rs;
    }

    // Check horizontal cuts
    let cum = 0;
    for (let i = 0; i < m - 1; i++) {
        cum += rowSums[i];
        if (cum * 2 === total) return true;
    }

    // Check vertical cuts
    cum = 0;
    for (let j = 0; j < n - 1; j++) {
        cum += colSums[j];
        if (cum * 2 === total) return true;
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function canPartitionGrid($grid) {
        $m = count($grid);
        if ($m == 0) return false;
        $n = count($grid[0]);
        $total = 0;
        $colSums = array_fill(0, $n, 0);
        $rowSums = [];

        // Compute total sum, row sums and column sums
        foreach ($grid as $row) {
            $rowSum = 0;
            for ($j = 0; $j < $n; $j++) {
                $val = $row[$j];
                $rowSum += $val;
                $colSums[$j] += $val;
            }
            $rowSums[] = $rowSum;
            $total += $rowSum;
        }

        // Check horizontal cuts
        $cum = 0;
        $rowsCount = count($rowSums);
        for ($i = 0; $i < $rowsCount - 1; $i++) {
            $cum += $rowSums[$i];
            if ($cum * 2 == $total) {
                return true;
            }
        }

        // Check vertical cuts
        $cum = 0;
        for ($j = 0; $j < $n - 1; $j++) {
            $cum += $colSums[$j];
            if ($cum * 2 == $total) {
                return true;
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func canPartitionGrid(_ grid: [[Int]]) -> Bool {
        let m = grid.count
        guard m > 0 else { return false }
        let n = grid[0].count
        var total: Int64 = 0
        var rowSums = [Int64](repeating: 0, count: m)
        var colSums = [Int64](repeating: 0, count: n)
        
        for i in 0..<m {
            var rSum: Int64 = 0
            for j in 0..<n {
                let val = Int64(grid[i][j])
                rSum += val
                colSums[j] += val
            }
            rowSums[i] = rSum
            total += rSum
        }
        
        // Horizontal cut
        var prefix: Int64 = 0
        if m > 1 {
            for i in 0..<(m - 1) {
                prefix += rowSums[i]
                if prefix == total - prefix {
                    return true
                }
            }
        }
        
        // Vertical cut
        prefix = 0
        if n > 1 {
            for j in 0..<(n - 1) {
                prefix += colSums[j]
                if prefix == total - prefix {
                    return true
                }
            }
        }
        
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canPartitionGrid(grid: Array<IntArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        var total = 0L
        val colSums = LongArray(n)
        // First pass: compute total sum and column sums
        for (i in 0 until m) {
            val row = grid[i]
            for (j in 0 until n) {
                val v = row[j].toLong()
                total += v
                colSums[j] += v
            }
        }
        // Check horizontal cuts
        var prefRow = 0L
        for (i in 0 until m - 1) {
            var rowSum = 0L
            val row = grid[i]
            for (j in 0 until n) {
                rowSum += row[j].toLong()
            }
            prefRow += rowSum
            if (prefRow * 2 == total) return true
        }
        // Check vertical cuts
        var prefCol = 0L
        for (c in 0 until n - 1) {
            prefCol += colSums[c]
            if (prefCol * 2 == total) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool canPartitionGrid(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<int> rowSum = List.filled(m, 0);
    List<int> colSum = List.filled(n, 0);
    int total = 0;

    for (int i = 0; i < m; ++i) {
      List<int> row = grid[i];
      for (int j = 0; j < n; ++j) {
        int v = row[j];
        total += v;
        rowSum[i] += v;
        colSum[j] += v;
      }
    }

    int cum = 0;
    for (int i = 0; i < m - 1; ++i) {
      cum += rowSum[i];
      if (cum * 2 == total) return true;
    }

    cum = 0;
    for (int j = 0; j < n - 1; ++j) {
      cum += colSum[j];
      if (cum * 2 == total) return true;
    }

    return false;
  }
}
```

## Golang

```go
func canPartitionGrid(grid [][]int) bool {
	m := len(grid)
	if m == 0 {
		return false
	}
	n := len(grid[0])

	rowSums := make([]int64, m)
	colSums := make([]int64, n)
	var total int64

	for i := 0; i < m; i++ {
		var rowSum int64
		for j := 0; j < n; j++ {
			val := int64(grid[i][j])
			rowSum += val
			colSums[j] += val
		}
		rowSums[i] = rowSum
		total += rowSum
	}

	var prefix int64
	// horizontal cuts
	for i := 0; i < m-1; i++ {
		prefix += rowSums[i]
		if prefix*2 == total {
			return true
		}
	}

	// vertical cuts
	prefix = 0
	for j := 0; j < n-1; j++ {
		prefix += colSums[j]
		if prefix*2 == total {
			return true
		}
	}
	return false
}
```

## Ruby

```ruby
def can_partition_grid(grid)
  m = grid.size
  n = grid[0].size
  total = 0
  col_sums = Array.new(n, 0)
  row_sums = []

  grid.each do |row|
    rs = 0
    row.each_with_index do |val, j|
      total += val
      rs += val
      col_sums[j] += val
    end
    row_sums << rs
  end

  # Horizontal cut
  prefix = 0
  (0...m - 1).each do |i|
    prefix += row_sums[i]
    return true if prefix * 2 == total
  end

  # Vertical cut
  prefix = 0
  (0...n - 1).each do |j|
    prefix += col_sums[j]
    return true if prefix * 2 == total
  end

  false
end
```

## Scala

```scala
object Solution {
    def canPartitionGrid(grid: Array[Array[Int]]): Boolean = {
        val m = grid.length
        if (m == 0) return false
        val n = grid(0).length

        val rowSums = new Array[Long](m)
        val colSums = new Array[Long](n)
        var total: Long = 0L

        var i = 0
        while (i < m) {
            var j = 0
            var rSum: Long = 0L
            while (j < n) {
                val v = grid(i)(j).toLong
                rSum += v
                colSums(j) += v
                j += 1
            }
            rowSums(i) = rSum
            total += rSum
            i += 1
        }

        // Horizontal cut
        var prefix: Long = 0L
        i = 0
        while (i < m - 1) {
            prefix += rowSums(i)
            if (prefix == total - prefix) return true
            i += 1
        }

        // Vertical cut
        prefix = 0L
        var c = 0
        while (c < n - 1) {
            prefix += colSums(c)
            if (prefix == total - prefix) return true
            c += 1
        }

        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_partition_grid(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        if m == 0 {
            return false;
        }
        let n = grid[0].len();

        let mut total: i64 = 0;
        let mut row_sums = vec![0i64; m];
        let mut col_sums = vec![0i64; n];

        for (i, row) in grid.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                let v = val as i64;
                total += v;
                row_sums[i] += v;
                col_sums[j] += v;
            }
        }

        if total % 2 != 0 {
            return false;
        }
        let half = total / 2;

        // Check horizontal cuts
        let mut prefix: i64 = 0;
        for i in 0..m - 1 {
            prefix += row_sums[i];
            if prefix == half {
                return true;
            }
        }

        // Check vertical cuts
        prefix = 0;
        for j in 0..n - 1 {
            prefix += col_sums[j];
            if prefix == half {
                return true;
            }
        }

        false
    }
}
```

## Racket

```racket
(define/contract (can-partition-grid grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (car grid))))
         (col-sums (make-vector n 0))
         (row-sums
           (for/list ([row grid])
             (let loop ((vals row) (j 0) (rsum 0))
               (if (null? vals)
                   rsum
                   (begin
                     (vector-set! col-sums j (+ (vector-ref col-sums j) (car vals)))
                     (loop (cdr vals) (add1 j) (+ rsum (car vals))))))))
         (total (apply + row-sums)))
    (define (has-equal-cut? sums)
      (let loop ((prefix 0) (lst sums))
        (cond [(null? lst) #f]
              [else
               (define new (+ prefix (car lst)))
               (if (= new (- total new)) #t
                   (loop new (cdr lst)))])))
    (or (has-equal-cut? row-sums)
        (let loop ((prefix 0) (idx 0))
          (if (= idx n) #f
              (let ((new (+ prefix (vector-ref col-sums idx))))
                (if (= new (- total new)) #t
                    (loop new (add1 idx)))))))))
```

## Erlang

```erlang
-module(solution).
-export([can_partition_grid/1]).

-spec can_partition_grid(Grid :: [[integer()]]) -> boolean().
can_partition_grid(Grid) ->
    case Grid of
        [] -> false;
        _ ->
            N = length(hd(Grid)),
            {Total, ColSums} = compute_totals_and_cols(Grid, 0, lists:duplicate(N, 0)),
            case has_horizontal_cut(Grid, Total) of
                true -> true;
                false -> has_vertical_cut(ColSums, Total)
            end
    end.

compute_totals_and_cols([], Tot, Cols) ->
    {Tot, Cols};
compute_totals_and_cols([Row|Rest], Tot, Cols) ->
    RowSum = lists:sum(Row),
    NewTot = Tot + RowSum,
    NewCols = add_row_to_cols(Row, Cols),
    compute_totals_and_cols(Rest, NewTot, NewCols).

add_row_to_cols([], []) -> [];
add_row_to_cols([V|Vs], [C|Cs]) ->
    [V + C | add_row_to_cols(Vs, Cs)].

has_horizontal_cut(Grid, Total) ->
    has_horizontal_cut(Grid, Total, 0).

has_horizontal_cut([], _Total, _Prefix) ->
    false;
has_horizontal_cut([Row|Rest], Total, Prefix) ->
    RowSum = lists:sum(Row),
    NewPrefix = Prefix + RowSum,
    case Rest of
        [] -> false; % cannot cut after last row
        _ ->
            if NewPrefix * 2 == Total -> true;
               true -> has_horizontal_cut(Rest, Total, NewPrefix)
            end
    end.

has_vertical_cut(ColSums, Total) ->
    has_vertical_cut(ColSums, Total, 0).

has_vertical_cut([], _Total, _Prefix) ->
    false;
has_vertical_cut([C|Rest], Total, Prefix) ->
    NewPrefix = Prefix + C,
    case Rest of
        [] -> false; % cannot cut after last column
        _ ->
            if NewPrefix * 2 == Total -> true;
               true -> has_vertical_cut(Rest, Total, NewPrefix)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_partition_grid(grid :: [[integer]]) :: boolean
  def can_partition_grid(grid) do
    m = length(grid)
    n = length(hd(grid))

    # Compute total sum and row sums
    {total, row_sums_rev} =
      Enum.reduce(grid, {0, []}, fn row, {tot, rows} ->
        rs = Enum.sum(row)
        {tot + rs, [rs | rows]}
      end)

    row_sums = Enum.reverse(row_sums_rev)

    if prefix_equal?(row_sums, total) do
      true
    else
      # Compute column sums using Erlang :array for O(1) updates
      col_arr = :array.new(n, default: 0)

      col_arr =
        Enum.reduce(grid, col_arr, fn row, arr ->
          Enum.with_index(row)
          |> Enum.reduce(arr, fn {val, idx}, a ->
            prev = :array.get(idx, a)
            :array.set(idx, prev + val, a)
          end)
        end)

      col_sums = for i <- 0..(n - 1), do: :array.get(i, col_arr)

      prefix_equal?(col_sums, total)
    end
  end

  defp prefix_equal?(sums, total) do
    check_prefix(sums, total, 0, length(sums))
  end

  defp check_prefix(_sums, _total, _cum, 0), do: false

  defp check_prefix([h | t], total, cum, rem) do
    new_cum = cum + h

    if rem > 1 and new_cum * 2 == total do
      true
    else
      check_prefix(t, total, new_cum, rem - 1)
    end
  end
end
```

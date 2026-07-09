# 1252. Cells with Odd Values in a Matrix

## Cpp

```cpp
class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        vector<int> row(m, 0), col(n, 0);
        for (const auto& idx : indices) {
            ++row[idx[0]];
            ++col[idx[1]];
        }
        int oddRows = 0, oddCols = 0;
        for (int v : row) if (v & 1) ++oddRows;
        for (int v : col) if (v & 1) ++oddCols;
        return oddRows * (n - oddCols) + (m - oddRows) * oddCols;
    }
};
```

## Java

```java
class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        boolean[] rows = new boolean[m];
        boolean[] cols = new boolean[n];
        for (int[] idx : indices) {
            rows[idx[0]] ^= true;
            cols[idx[1]] ^= true;
        }
        int oddRows = 0, oddCols = 0;
        for (boolean r : rows) if (r) oddRows++;
        for (boolean c : cols) if (c) oddCols++;
        return oddRows * (n - oddCols) + (m - oddRows) * oddCols;
    }
}
```

## Python

```python
class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
        odd_rows = sum(rows)
        odd_cols = sum(cols)
        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
```

## Python3

```python
from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        for r, c in indices:
            row[r] ^= 1
            col[c] ^= 1
        odd_rows = sum(row)
        odd_cols = sum(col)
        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
```

## C

```c
#include <stdlib.h>

int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize) {
    int *row = (int *)calloc(m, sizeof(int));
    int *col = (int *)calloc(n, sizeof(int));
    
    for (int i = 0; i < indicesSize; ++i) {
        int r = indices[i][0];
        int c = indices[i][1];
        row[r] ^= 1;
        col[c] ^= 1;
    }
    
    int oddRows = 0, oddCols = 0;
    for (int i = 0; i < m; ++i) if (row[i]) ++oddRows;
    for (int j = 0; j < n; ++j) if (col[j]) ++oddCols;
    
    free(row);
    free(col);
    
    return oddRows * (n - oddCols) + (m - oddRows) * oddCols;
}
```

## Csharp

```csharp
public class Solution
{
    public int OddCells(int m, int n, int[][] indices)
    {
        bool[] rowOdd = new bool[m];
        bool[] colOdd = new bool[n];

        foreach (var pair in indices)
        {
            int r = pair[0];
            int c = pair[1];
            rowOdd[r] ^= true;
            colOdd[c] ^= true;
        }

        int oddRows = 0, oddCols = 0;
        for (int i = 0; i < m; i++)
            if (rowOdd[i]) oddRows++;
        for (int j = 0; j < n; j++)
            if (colOdd[j]) oddCols++;

        return oddRows * (n - oddCols) + (m - oddRows) * oddCols;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function(m, n, indices) {
    const rowOdd = new Array(m).fill(false);
    const colOdd = new Array(n).fill(false);
    
    for (const [r, c] of indices) {
        rowOdd[r] = !rowOdd[r];
        colOdd[c] = !colOdd[c];
    }
    
    let oddRows = 0;
    for (let i = 0; i < m; ++i) if (rowOdd[i]) ++oddRows;
    let oddCols = 0;
    for (let j = 0; j < n; ++j) if (colOdd[j]) ++oddCols;
    
    return oddRows * (n - oddCols) + (m - oddRows) * oddCols;
};
```

## Typescript

```typescript
function oddCells(m: number, n: number, indices: number[][]): number {
    const rows = new Array(m).fill(0);
    const cols = new Array(n).fill(0);
    for (const [r, c] of indices) {
        rows[r]++;
        cols[c]++;
    }
    let rOdd = 0;
    for (let i = 0; i < m; i++) {
        if (rows[i] % 2 === 1) rOdd++;
    }
    let cOdd = 0;
    for (let j = 0; j < n; j++) {
        if (cols[j] % 2 === 1) cOdd++;
    }
    return rOdd * (n - cOdd) + (m - rOdd) * cOdd;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $indices
     * @return Integer
     */
    function oddCells($m, $n, $indices) {
        $row = array_fill(0, $m, 0);
        $col = array_fill(0, $n, 0);

        foreach ($indices as $pair) {
            $r = $pair[0];
            $c = $pair[1];
            $row[$r] ^= 1;
            $col[$c] ^= 1;
        }

        $oddRows = 0;
        foreach ($row as $v) {
            if ($v & 1) $oddRows++;
        }

        $oddCols = 0;
        foreach ($col as $v) {
            if ($v & 1) $oddCols++;
        }

        return $oddRows * ($n - $oddCols) + ($m - $oddRows) * $oddCols;
    }
}
```

## Swift

```swift
class Solution {
    func oddCells(_ m: Int, _ n: Int, _ indices: [[Int]]) -> Int {
        var rows = Array(repeating: 0, count: m)
        var cols = Array(repeating: 0, count: n)
        
        for pair in indices {
            let r = pair[0]
            let c = pair[1]
            rows[r] ^= 1
            cols[c] ^= 1
        }
        
        var oddRows = 0
        for v in rows where v == 1 { oddRows += 1 }
        var oddCols = 0
        for v in cols where v == 1 { oddCols += 1 }
        
        return oddRows * (n - oddCols) + (m - oddRows) * oddCols
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun oddCells(m: Int, n: Int, indices: Array<IntArray>): Int {
        val rows = BooleanArray(m)
        val cols = BooleanArray(n)
        for (pair in indices) {
            rows[pair[0]] = !rows[pair[0]]
            cols[pair[1]] = !cols[pair[1]]
        }
        var oddRows = 0
        for (r in rows) if (r) oddRows++
        var oddCols = 0
        for (c in cols) if (c) oddCols++
        return oddRows * (n - oddCols) + (m - oddRows) * oddCols
    }
}
```

## Dart

```dart
class Solution {
  int oddCells(int m, int n, List<List<int>> indices) {
    List<int> row = List.filled(m, 0);
    List<int> col = List.filled(n, 0);
    for (var idx in indices) {
      row[idx[0]]++;
      col[idx[1]]++;
    }
    int oddRows = 0;
    for (int v in row) if (v % 2 == 1) oddRows++;
    int evenRows = m - oddRows;

    int oddCols = 0;
    for (int v in col) if (v % 2 == 1) oddCols++;
    int evenCols = n - oddCols;

    return oddRows * evenCols + evenRows * oddCols;
  }
}
```

## Golang

```go
func oddCells(m int, n int, indices [][]int) int {
	rows := make([]bool, m)
	cols := make([]bool, n)
	for _, idx := range indices {
		r, c := idx[0], idx[1]
		rows[r] = !rows[r]
		cols[c] = !cols[c]
	}
	oddRows, oddCols := 0, 0
	for _, v := range rows {
		if v {
			oddRows++
		}
	}
	for _, v := range cols {
		if v {
			oddCols++
		}
	}
	return oddRows*(n-oddCols) + (m-oddRows)*oddCols
}
```

## Ruby

```ruby
def odd_cells(m, n, indices)
  rows = Array.new(m, false)
  cols = Array.new(n, false)

  indices.each do |r, c|
    rows[r] = !rows[r]
    cols[c] = !cols[c]
  end

  odd_rows = rows.count(true)
  odd_cols = cols.count(true)

  odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
end
```

## Scala

```scala
object Solution {
    def oddCells(m: Int, n: Int, indices: Array[Array[Int]]): Int = {
        val rows = new Array[Int](m)
        val cols = new Array[Int](n)

        var i = 0
        while (i < indices.length) {
            val r = indices(i)(0)
            val c = indices(i)(1)
            rows(r) += 1
            cols(c) += 1
            i += 1
        }

        var oddRows = 0
        var j = 0
        while (j < m) {
            if ((rows(j) & 1) == 1) oddRows += 1
            j += 1
        }

        var oddCols = 0
        j = 0
        while (j < n) {
            if ((cols(j) & 1) == 1) oddCols += 1
            j += 1
        }

        oddRows * (n - oddCols) + (m - oddRows) * oddCols
    }
}
```

## Rust

```rust
impl Solution {
    pub fn odd_cells(m: i32, n: i32, indices: Vec<Vec<i32>>) -> i32 {
        let m_usize = m as usize;
        let n_usize = n as usize;
        let mut row = vec![0i32; m_usize];
        let mut col = vec![0i32; n_usize];

        for pair in indices.iter() {
            let r = pair[0] as usize;
            let c = pair[1] as usize;
            row[r] += 1;
            col[c] += 1;
        }

        let odd_rows = row.iter().filter(|&&x| x % 2 != 0).count();
        let odd_cols = col.iter().filter(|&&x| x % 2 != 0).count();

        let even_rows = m_usize - odd_rows;
        let even_cols = n_usize - odd_cols;

        (odd_rows * even_cols + even_rows * odd_cols) as i32
    }
}
```

## Racket

```racket
(define/contract (odd-cells m n indices)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((row (make-vector m 0))
         (col (make-vector n 0)))
    (for ([pair indices])
      (let ([r (first pair)]
            [c (second pair)])
        (vector-set! row r (bitwise-xor (vector-ref row r) 1))
        (vector-set! col c (bitwise-xor (vector-ref col c) 1))))
    (define rows-odd
      (let loop ((i 0) (cnt 0))
        (if (= i m)
            cnt
            (loop (+ i 1) (+ cnt (vector-ref row i))))))
    (define cols-odd
      (let loop ((j 0) (cnt 0))
        (if (= j n)
            cnt
            (loop (+ j 1) (+ cnt (vector-ref col j))))))
    (+ (* rows-odd (- n cols-odd))
       (* (- m rows-odd) cols-odd))))
```

## Erlang

```erlang
-spec odd_cells(M :: integer(), N :: integer(), Indices :: [[integer()]]) -> integer().
odd_cells(M, N, Indices) ->
    {RowParity, ColParity} = lists:foldl(
        fun([R, C], {RP, CP}) ->
            RP2 = maps:update_with(R, fun(V) -> 1 - V end, 1, RP),
            CP2 = maps:update_with(C, fun(V) -> 1 - V end, 1, CP),
            {RP2, CP2}
        end,
        {#{}, #{}},
        Indices
    ),
    OddRows = maps:size(RowParity),
    OddCols = maps:size(ColParity),
    EvenRows = M - OddRows,
    EvenCols = N - OddCols,
    OddRows * EvenCols + EvenRows * OddCols.
```

## Elixir

```elixir
defmodule Solution do
  @spec odd_cells(m :: integer, n :: integer, indices :: [[integer]]) :: integer
  def odd_cells(m, n, indices) do
    row_counts = List.duplicate(0, m)
    col_counts = List.duplicate(0, n)

    {row_counts, col_counts} =
      Enum.reduce(indices, {row_counts, col_counts}, fn [r, c], {rows, cols} ->
        rows = List.update_at(rows, r, &(&1 + 1))
        cols = List.update_at(cols, c, &(&1 + 1))
        {rows, cols}
      end)

    rows_odd = Enum.count(row_counts, fn x -> rem(x, 2) == 1 end)
    cols_odd = Enum.count(col_counts, fn x -> rem(x, 2) == 1 end)

    rows_odd * (n - cols_odd) + (m - rows_odd) * cols_odd
  end
end
```

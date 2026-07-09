# 2661. First Completely Painted Row or Column

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int total = m * n;
        vector<pair<int,int>> pos(total + 1);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                pos[mat[i][j]] = {i, j};
            }
        }
        vector<int> rowCnt(m, 0), colCnt(n, 0);
        for (int i = 0; i < (int)arr.size(); ++i) {
            auto [r, c] = pos[arr[i]];
            if (++rowCnt[r] == n) return i;
            if (++colCnt[c] == m) return i;
        }
        return -1; // should never reach here per problem constraints
    }
};
```

## Java

```java
class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int total = arr.length; // equals m * n

        // Since values are from 1 to m*n, we can use direct indexing.
        int[] rowPos = new int[total + 1];
        int[] colPos = new int[total + 1];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = mat[i][j];
                rowPos[val] = i;
                colPos[val] = j;
            }
        }

        int[] rowCnt = new int[m];
        int[] colCnt = new int[n];

        for (int i = 0; i < total; i++) {
            int v = arr[i];
            int r = rowPos[v];
            int c = colPos[v];

            if (++rowCnt[r] == n) return i;
            if (++colCnt[c] == m) return i;
        }

        // According to problem constraints, this line is never reached.
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        # map each value to its (row, col) position
        pos = {}
        for i in range(m):
            row = mat[i]
            for j in range(n):
                pos[row[j]] = (i, j)

        row_cnt = [0] * m
        col_cnt = [0] * n

        for idx, val in enumerate(arr):
            r, c = pos[val]
            row_cnt[r] += 1
            if row_cnt[r] == n:
                return idx
            col_cnt[c] += 1
            if col_cnt[c] == m:
                return idx
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        total = m * n
        # position mapping: index by value (1..total)
        pos = [None] * (total + 1)
        for i in range(m):
            row = mat[i]
            for j in range(n):
                val = row[j]
                pos[val] = (i, j)

        row_cnt = [0] * m
        col_cnt = [0] * n

        for idx, val in enumerate(arr):
            r, c = pos[val]
            row_cnt[r] += 1
            if row_cnt[r] == n:
                return idx
            col_cnt[c] += 1
            if col_cnt[c] == m:
                return idx

        return -1
```

## C

```c
#include <stdlib.h>

int firstCompleteIndex(int* arr, int arrSize, int** mat, int matSize, int* matColSize) {
    int m = matSize;
    if (m == 0) return -1;
    int n = matColSize[0];
    
    int total = m * n;
    int *rowPos = (int *)malloc((total + 1) * sizeof(int));
    int *colPos = (int *)malloc((total + 1) * sizeof(int));
    for (int i = 0; i <= total; ++i) {
        rowPos[i] = -1;
        colPos[i] = -1;
    }
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int val = mat[i][j];
            rowPos[val] = i;
            colPos[val] = j;
        }
    }
    
    int *rowCnt = (int *)calloc(m, sizeof(int));
    int *colCnt = (int *)calloc(n, sizeof(int));
    
    for (int i = 0; i < arrSize; ++i) {
        int val = arr[i];
        int r = rowPos[val];
        int c = colPos[val];
        
        if (++rowCnt[r] == n) {
            free(rowPos);
            free(colPos);
            free(rowCnt);
            free(colCnt);
            return i;
        }
        if (++colCnt[c] == m) {
            free(rowPos);
            free(colPos);
            free(rowCnt);
            free(colCnt);
            return i;
        }
    }
    
    free(rowPos);
    free(colPos);
    free(rowCnt);
    free(colCnt);
    return -1;  // Should never be reached per problem constraints
}
```

## Csharp

```csharp
public class Solution
{
    public int FirstCompleteIndex(int[] arr, int[][] mat)
    {
        int m = mat.Length;
        int n = mat[0].Length;
        int total = m * n;

        // Position lookup arrays (values are 1..total)
        int[] posRow = new int[total + 1];
        int[] posCol = new int[total + 1];

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int val = mat[i][j];
                posRow[val] = i;
                posCol[val] = j;
            }
        }

        int[] rowCnt = new int[m];
        int[] colCnt = new int[n];

        for (int i = 0; i < arr.Length; i++)
        {
            int v = arr[i];
            int r = posRow[v];
            int c = posCol[v];

            if (++rowCnt[r] == n) return i;
            if (++colCnt[c] == m) return i;
        }

        // According to problem constraints, this line is never reached.
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */
var firstCompleteIndex = function(arr, mat) {
    const m = mat.length;
    const n = mat[0].length;
    const total = m * n;

    // position lookup for each value (values are 1..m*n)
    const rowPos = new Int32Array(total + 1);
    const colPos = new Int32Array(total + 1);

    for (let i = 0; i < m; ++i) {
        const row = mat[i];
        for (let j = 0; j < n; ++j) {
            const val = row[j];
            rowPos[val] = i;
            colPos[val] = j;
        }
    }

    const rowCnt = new Int32Array(m);
    const colCnt = new Int32Array(n);

    for (let idx = 0; idx < arr.length; ++idx) {
        const v = arr[idx];
        const r = rowPos[v];
        const c = colPos[v];

        if (++rowCnt[r] === n) return idx;
        if (++colCnt[c] === m) return idx;
    }

    return -1; // should never reach due to problem guarantees
};
```

## Typescript

```typescript
function firstCompleteIndex(arr: number[], mat: number[][]): number {
    const m = mat.length;
    const n = mat[0].length;
    const total = m * n;
    const rowPos = new Int32Array(total + 1);
    const colPos = new Int32Array(total + 1);

    for (let i = 0; i < m; i++) {
        const row = mat[i];
        for (let j = 0; j < n; j++) {
            const val = row[j];
            rowPos[val] = i;
            colPos[val] = j;
        }
    }

    const rowCnt = new Int32Array(m);
    const colCnt = new Int32Array(n);

    for (let idx = 0; idx < arr.length; idx++) {
        const v = arr[idx];
        const r = rowPos[v];
        const c = colPos[v];

        if (++rowCnt[r] === n) return idx;
        if (++colCnt[c] === m) return idx;
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[][] $mat
     * @return Integer
     */
    function firstCompleteIndex($arr, $mat) {
        $m = count($mat);
        $n = count($mat[0]);

        // position maps: value -> row, column
        $posRow = [];
        $posCol = [];

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $val = $mat[$i][$j];
                $posRow[$val] = $i;
                $posCol[$val] = $j;
            }
        }

        $rowCnt = array_fill(0, $m, 0);
        $colCnt = array_fill(0, $n, 0);

        foreach ($arr as $idx => $num) {
            $r = $posRow[$num];
            $c = $posCol[$num];

            $rowCnt[$r]++;
            if ($rowCnt[$r] == $n) {
                return $idx;
            }

            $colCnt[$c]++;
            if ($colCnt[$c] == $m) {
                return $idx;
            }
        }

        return -1; // should never reach here per problem constraints
    }
}
```

## Swift

```swift
class Solution {
    func firstCompleteIndex(_ arr: [Int], _ mat: [[Int]]) -> Int {
        let m = mat.count
        guard m > 0 else { return -1 }
        let n = mat[0].count
        let total = m * n
        
        var posRow = [Int](repeating: 0, count: total + 1)
        var posCol = [Int](repeating: 0, count: total + 1)
        
        for i in 0..<m {
            for j in 0..<n {
                let val = mat[i][j]
                posRow[val] = i
                posCol[val] = j
            }
        }
        
        var rowCount = [Int](repeating: 0, count: m)
        var colCount = [Int](repeating: 0, count: n)
        
        for (idx, num) in arr.enumerated() {
            let r = posRow[num]
            let c = posCol[num]
            
            rowCount[r] += 1
            if rowCount[r] == n { return idx }
            
            colCount[c] += 1
            if colCount[c] == m { return idx }
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun firstCompleteIndex(arr: IntArray, mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val total = m * n
        val posRow = IntArray(total + 1)
        val posCol = IntArray(total + 1)

        for (i in 0 until m) {
            val row = mat[i]
            for (j in 0 until n) {
                val v = row[j]
                posRow[v] = i
                posCol[v] = j
            }
        }

        val rowCnt = IntArray(m)
        val colCnt = IntArray(n)

        for (i in arr.indices) {
            val v = arr[i]
            val r = posRow[v]
            val c = posCol[v]

            rowCnt[r]++
            if (rowCnt[r] == n) return i

            colCnt[c]++
            if (colCnt[c] == m) return i
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int firstCompleteIndex(List<int> arr, List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    int total = m * n;

    // Store row and column for each value.
    List<int> rowPos = List.filled(total + 1, 0);
    List<int> colPos = List.filled(total + 1, 0);
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        int val = mat[i][j];
        rowPos[val] = i;
        colPos[val] = j;
      }
    }

    List<int> rowCnt = List.filled(m, 0);
    List<int> colCnt = List.filled(n, 0);

    for (int idx = 0; idx < arr.length; ++idx) {
      int val = arr[idx];
      int r = rowPos[val];
      int c = colPos[val];

      rowCnt[r]++;
      if (rowCnt[r] == n) return idx;

      colCnt[c]++;
      if (colCnt[c] == m) return idx;
    }

    return -1; // Should never reach due to problem constraints.
  }
}
```

## Golang

```go
func firstCompleteIndex(arr []int, mat [][]int) int {
	m := len(mat)
	n := len(mat[0])
	total := m * n

	posRow := make([]int, total+1)
	posCol := make([]int, total+1)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			val := mat[i][j]
			posRow[val] = i
			posCol[val] = j
		}
	}

	rowCnt := make([]int, m)
	colCnt := make([]int, n)

	for idx, val := range arr {
		r := posRow[val]
		c := posCol[val]

		rowCnt[r]++
		if rowCnt[r] == n {
			return idx
		}
		colCnt[c]++
		if colCnt[c] == m {
			return idx
		}
	}
	return -1
}
```

## Ruby

```ruby
def first_complete_index(arr, mat)
  m = mat.length
  n = mat[0].length
  max_val = m * n
  rows = Array.new(max_val + 1, -1)
  cols = Array.new(max_val + 1, -1)

  mat.each_with_index do |row_vals, i|
    row_vals.each_with_index do |val, j|
      rows[val] = i
      cols[val] = j
    end
  end

  row_cnt = Array.new(m, 0)
  col_cnt = Array.new(n, 0)

  arr.each_with_index do |val, idx|
    r = rows[val]
    c = cols[val]
    row_cnt[r] += 1
    return idx if row_cnt[r] == n
    col_cnt[c] += 1
    return idx if col_cnt[c] == m
  end

  -1
end
```

## Scala

```scala
object Solution {
    def firstCompleteIndex(arr: Array[Int], mat: Array[Array[Int]]): Int = {
        val m = mat.length
        val n = if (m == 0) 0 else mat(0).length
        val total = m * n
        // position lookup arrays, values are from 1 to total
        val posRow = new Array[Int](total + 1)
        val posCol = new Array[Int](total + 1)

        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                val v = mat(i)(j)
                posRow(v) = i
                posCol(v) = j
                j += 1
            }
            i += 1
        }

        val rowCount = new Array[Int](m)
        val colCount = new Array[Int](n)

        var idx = 0
        while (idx < arr.length) {
            val v = arr(idx)
            val r = posRow(v)
            val c = posCol(v)

            rowCount(r) += 1
            if (rowCount(r) == n) return idx

            colCount(c) += 1
            if (colCount(c) == m) return idx

            idx += 1
        }
        -1 // should never reach due to problem guarantees
    }
}
```

## Rust

```rust
impl Solution {
    pub fn first_complete_index(arr: Vec<i32>, mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = if m > 0 { mat[0].len() } else { 0 };
        // Direct mapping from value to its (row, col) position.
        let total = m * n;
        let mut pos: Vec<(usize, usize)> = vec![(0, 0); total + 1];
        for i in 0..m {
            for j in 0..n {
                let val = mat[i][j] as usize;
                pos[val] = (i, j);
            }
        }

        let mut row_cnt = vec![0usize; m];
        let mut col_cnt = vec![0usize; n];

        for (idx, &num) in arr.iter().enumerate() {
            let (r, c) = pos[num as usize];
            row_cnt[r] += 1;
            if row_cnt[r] == n {
                return idx as i32;
            }
            col_cnt[c] += 1;
            if col_cnt[c] == m {
                return idx as i32;
            }
        }

        -1 // According to constraints, this line is never reached.
    }
}
```

## Racket

```racket
(define/contract (first-complete-index arr mat)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length mat))
         (n (if (null? mat) 0 (length (car mat))))
         (pos (make-hash)))
    ;; map each value to its (row, col)
    (for ([row-index (in-range m)]
          [row (in-list mat)])
      (for ([col-index (in-range n)]
            [val (in-list row)])
        (hash-set! pos val (vector row-index col-index))))
    (define row-count (make-vector m 0))
    (define col-count (make-vector n 0))
    ;; process arr
    (let loop ((i 0) (lst arr))
      (if (null? lst)
          -1 ; should never happen per constraints
          (let* ((val (car lst))
                 (vec (hash-ref pos val))
                 (r (vector-ref vec 0))
                 (c (vector-ref vec 1)))
            (vector-set! row-count r (+ 1 (vector-ref row-count r)))
            (vector-set! col-count c (+ 1 (vector-ref col-count c)))
            (if (or (= (vector-ref row-count r) n)
                    (= (vector-ref col-count c) m))
                i
                (loop (+ i 1) (cdr lst)))))))))
```

## Erlang

```erlang
first_complete_index(Arr, Mat) ->
    case Mat of
        [] -> -1;
        [FirstRow|_] ->
            Rows = length(Mat),
            Cols = length(FirstRow),
            PosMap = build_pos_map(Mat),
            process_arr(Arr, 0, PosMap, #{}, #{}, Rows, Cols)
    end.

build_pos_map(Mat) ->
    build_pos_map(Mat, 0, #{}).

build_pos_map([], _RowIdx, PosMap) -> PosMap;
build_pos_map([Row|Rest], RowIdx, PosMap) ->
    NewPosMap = fill_row(Row, RowIdx, 0, PosMap),
    build_pos_map(Rest, RowIdx + 1, NewPosMap).

fill_row([], _RowIdx, _ColIdx, PosMap) -> PosMap;
fill_row([Val|RestVals], RowIdx, ColIdx, PosMap) ->
    Updated = maps:put(Val, {RowIdx, ColIdx}, PosMap),
    fill_row(RestVals, RowIdx, ColIdx + 1, Updated).

process_arr([], _Idx, _PosMap, _RowCnt, _ColCnt, _Rows, _Cols) -> -1;
process_arr([Val|Rest], Idx, PosMap, RowCnt, ColCnt, Rows, Cols) ->
    {R, C} = maps:get(Val, PosMap),
    NewRowCnt = maps:get(R, RowCnt, 0) + 1,
    UpdatedRowCnt = maps:put(R, NewRowCnt, RowCnt),
    case NewRowCnt of
        N when N == Cols -> Idx;
        _ ->
            NewColCnt = maps:get(C, ColCnt, 0) + 1,
            UpdatedColCnt = maps:put(C, NewColCnt, ColCnt),
            case NewColCnt of
                M when M == Rows -> Idx;
                _ -> process_arr(Rest, Idx + 1, PosMap, UpdatedRowCnt, UpdatedColCnt, Rows, Cols)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec first_complete_index(arr :: [integer], mat :: [[integer]]) :: integer
  def first_complete_index(arr, mat) do
    rows = length(mat)
    cols = if rows == 0, do: 0, else: length(hd mat)

    pos_map = build_pos_map(mat)

    result =
      Enum.reduce_while(Enum.with_index(arr), {%{}, %{}}, fn {num, idx},
                                                            {row_counts, col_counts} ->
        {r, c} = Map.fetch!(pos_map, num)

        rc = Map.get(row_counts, r, 0) + 1
        row_counts = Map.put(row_counts, r, rc)

        cc = Map.get(col_counts, c, 0) + 1
        col_counts = Map.put(col_counts, c, cc)

        if rc == cols or cc == rows do
          {:halt, idx}
        else
          {:cont, {row_counts, col_counts}}
        end
      end)

    case result do
      idx when is_integer(idx) -> idx
      _ -> -1
    end
  end

  defp build_pos_map(mat) do
    Enum.reduce(Enum.with_index(mat), %{}, fn {row, r}, acc ->
      Enum.reduce(Enum.with_index(row), acc, fn {val, c}, a ->
        Map.put(a, val, {r, c})
      end)
    end)
  end
end
```

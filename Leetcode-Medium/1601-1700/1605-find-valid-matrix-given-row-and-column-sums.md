# 1605. Find Valid Matrix Given Row and Column Sums

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        int n = rowSum.size(), m = colSum.size();
        vector<vector<int>> ans(n, vector<int>(m, 0));
        int i = 0, j = 0;
        while (i < n && j < m) {
            int x = min(rowSum[i], colSum[j]);
            ans[i][j] = x;
            rowSum[i] -= x;
            colSum[j] -= x;
            if (rowSum[i] == 0) ++i;
            else ++j;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int n = rowSum.length;
        int m = colSum.length;
        int[][] matrix = new int[n][m];
        int i = 0, j = 0;
        while (i < n && j < m) {
            int val = Math.min(rowSum[i], colSum[j]);
            matrix[i][j] = val;
            rowSum[i] -= val;
            colSum[j] -= val;
            if (rowSum[i] == 0) {
                i++;
            } else {
                j++;
            }
        }
        return matrix;
    }
}
```

## Python

```python
class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        n, m = len(rowSum), len(colSum)
        ans = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            val = rowSum[i] if rowSum[i] < colSum[j] else colSum[j]
            ans[i][j] = val
            rowSum[i] -= val
            colSum[j] -= val
            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        return ans
```

## Python3

```python
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        ans = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            x = min(rowSum[i], colSum[j])
            ans[i][j] = x
            rowSum[i] -= x
            colSum[j] -= x
            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** restoreMatrix(int* rowSum, int rowSumSize, int* colSum, int colSumSize, int* returnSize, int*** returnColumnSizes) {
    (void)returnColumnSizes; // placeholder to avoid unused warning if not needed
    *returnSize = rowSumSize;
    int **colSizesPtr = malloc(sizeof(int*));
    *colSizesPtr = malloc(rowSumSize * sizeof(int));
    for (int i = 0; i < rowSumSize; ++i) {
        (*colSizesPtr)[i] = colSumSize;
    }
    *returnColumnSizes = colSizesPtr;

    int **matrix = malloc(rowSumSize * sizeof(int*));
    for (int i = 0; i < rowSumSize; ++i) {
        matrix[i] = calloc(colSumSize, sizeof(int));
    }

    int i = 0, j = 0;
    while (i < rowSumSize && j < colSumSize) {
        int val = rowSum[i] < colSum[j] ? rowSum[i] : colSum[j];
        matrix[i][j] = val;
        rowSum[i] -= val;
        colSum[j] -= val;
        if (rowSum[i] == 0)
            ++i;
        else
            ++j;
    }

    return matrix;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] RestoreMatrix(int[] rowSum, int[] colSum) {
        int n = rowSum.Length;
        int m = colSum.Length;
        int[][] result = new int[n][];
        for (int i = 0; i < n; i++) {
            result[i] = new int[m];
        }

        int i = 0, j = 0;
        while (i < n && j < m) {
            int val = Math.Min(rowSum[i], colSum[j]);
            result[i][j] = val;
            rowSum[i] -= val;
            colSum[j] -= val;

            if (rowSum[i] == 0) {
                i++;
            } else {
                j++;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rowSum
 * @param {number[]} colSum
 * @return {number[][]}
 */
var restoreMatrix = function(rowSum, colSum) {
    const n = rowSum.length;
    const m = colSum.length;
    const ans = Array.from({ length: n }, () => Array(m).fill(0));
    let i = 0, j = 0;
    while (i < n && j < m) {
        const val = Math.min(rowSum[i], colSum[j]);
        ans[i][j] = val;
        rowSum[i] -= val;
        colSum[j] -= val;
        if (rowSum[i] === 0) {
            i++;
        } else {
            j++;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function restoreMatrix(rowSum: number[], colSum: number[]): number[][] {
    const n = rowSum.length;
    const m = colSum.length;
    const result: number[][] = Array.from({ length: n }, () => Array(m).fill(0));
    let i = 0, j = 0;
    while (i < n && j < m) {
        const val = Math.min(rowSum[i], colSum[j]);
        result[i][j] = val;
        rowSum[i] -= val;
        colSum[j] -= val;
        if (rowSum[i] === 0) i++;
        else j++;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $rowSum
     * @param Integer[] $colSum
     * @return Integer[][]
     */
    function restoreMatrix($rowSum, $colSum) {
        $n = count($rowSum);
        $m = count($colSum);
        $ans = array_fill(0, $n, array_fill(0, $m, 0));
        $i = 0;
        $j = 0;
        while ($i < $n && $j < $m) {
            $val = min($rowSum[$i], $colSum[$j]);
            $ans[$i][$j] = $val;
            $rowSum[$i] -= $val;
            $colSum[$j] -= $val;
            if ($rowSum[$i] == 0) {
                $i++;
            } else {
                $j++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func restoreMatrix(_ rowSum: [Int], _ colSum: [Int]) -> [[Int]] {
        var rows = rowSum
        var cols = colSum
        let n = rows.count
        let m = cols.count
        var result = Array(repeating: Array(repeating: 0, count: m), count: n)
        var i = 0
        var j = 0
        while i < n && j < m {
            let val = min(rows[i], cols[j])
            result[i][j] = val
            rows[i] -= val
            cols[j] -= val
            if rows[i] == 0 {
                i += 1
            } else {
                j += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun restoreMatrix(rowSum: IntArray, colSum: IntArray): Array<IntArray> {
        val n = rowSum.size
        val m = colSum.size
        val ans = Array(n) { IntArray(m) }
        var i = 0
        var j = 0
        while (i < n && j < m) {
            val v = kotlin.math.min(rowSum[i], colSum[j])
            ans[i][j] = v
            rowSum[i] -= v
            colSum[j] -= v
            if (rowSum[i] == 0) i++ else j++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> restoreMatrix(List<int> rowSum, List<int> colSum) {
    int n = rowSum.length;
    int m = colSum.length;
    List<List<int>> ans = List.generate(n, (_) => List.filled(m, 0));
    int i = 0, j = 0;
    while (i < n && j < m) {
      int val = rowSum[i] < colSum[j] ? rowSum[i] : colSum[j];
      ans[i][j] = val;
      rowSum[i] -= val;
      colSum[j] -= val;
      if (rowSum[i] == 0) {
        i++;
      } else {
        j++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func restoreMatrix(rowSum []int, colSum []int) [][]int {
	n := len(rowSum)
	m := len(colSum)
	ans := make([][]int, n)
	for i := 0; i < n; i++ {
		ans[i] = make([]int, m)
	}
	i, j := 0, 0
	for i < n && j < m {
		val := rowSum[i]
		if colSum[j] < val {
			val = colSum[j]
		}
		ans[i][j] = val
		rowSum[i] -= val
		colSum[j] -= val
		if rowSum[i] == 0 {
			i++
		} else {
			j++
		}
	}
	return ans
}
```

## Ruby

```ruby
def restore_matrix(row_sum, col_sum)
  n = row_sum.length
  m = col_sum.length
  result = Array.new(n) { Array.new(m, 0) }
  i = 0
  j = 0
  while i < n && j < m
    val = [row_sum[i], col_sum[j]].min
    result[i][j] = val
    row_sum[i] -= val
    col_sum[j] -= val
    if row_sum[i] == 0
      i += 1
    else
      j += 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def restoreMatrix(rowSum: Array[Int], colSum: Array[Int]): Array[Array[Int]] = {
        val rows = rowSum.clone()
        val cols = colSum.clone()
        val n = rows.length
        val m = cols.length
        val result = Array.ofDim[Int](n, m)
        var i = 0
        var j = 0
        while (i < n && j < m) {
            val v = math.min(rows(i), cols(j))
            result(i)(j) = v
            rows(i) -= v
            cols(j) -= v
            if (rows(i) == 0) i += 1 else j += 1
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn restore_matrix(row_sum: Vec<i32>, col_sum: Vec<i32>) -> Vec<Vec<i32>> {
        let mut rows = row_sum.clone();
        let mut cols = col_sum.clone();
        let n = rows.len();
        let m = cols.len();
        let mut ans = vec![vec![0i32; m]; n];
        let (mut i, mut j) = (0usize, 0usize);
        while i < n && j < m {
            let v = std::cmp::min(rows[i], cols[j]);
            ans[i][j] = v;
            rows[i] -= v;
            cols[j] -= v;
            if rows[i] == 0 {
                i += 1;
            } else {
                j += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define/contract (restore-matrix rowSum colSum)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ((r (list->vector rowSum))
         (c (list->vector colSum))
         (n (vector-length r))
         (m (vector-length c))
         (ans (make-vector n)))
    ;; initialize answer matrix with zeros
    (for ([i (in-range n)])
      (vector-set! ans i (make-vector m 0)))
    ;; greedy filling using two pointers
    (let loop ((i 0) (j 0))
      (when (and (< i n) (< j m))
        (define val (min (vector-ref r i) (vector-ref c j)))
        (vector-set! (vector-ref ans i) j val)
        (vector-set! r i (- (vector-ref r i) val))
        (vector-set! c j (- (vector-ref c j) val))
        (if (= (vector-ref r i) 0)
            (loop (+ i 1) j)
            (loop i (+ j 1)))))
    ;; convert to list of lists
    (let ((result (make-vector n)))
      (for ([i (in-range n)])
        (vector-set! result i (vector->list (vector-ref ans i))))
      (vector->list result))))
```

## Erlang

```erlang
-module(solution).
-export([restore_matrix/2]).

-spec restore_matrix(RowSum :: [integer()], ColSum :: [integer()]) -> [[integer()]].
restore_matrix(RowSum, ColSum) ->
    restore_rows(RowSum, ColSum).

%% Process each row recursively
-spec restore_rows([integer()], [integer()]) -> [[integer()]].
restore_rows([], _ColRem) ->
    [];
restore_rows([Row|Rows], ColRem) ->
    {NewColRem, RowValsRev, 0} = process_row(Row, ColRem),
    RowVals = lists:reverse(RowValsRev),
    [RowVals | restore_rows(Rows, NewColRem)].

%% Process a single row across all columns
-spec process_row(integer(), [integer()]) -> {[integer()], [integer()], integer()}.
process_row(RowRem, []) ->
    {[], [], RowRem};
process_row(RowRem, [C|Cs]) ->
    Val = if RowRem < C -> RowRem; true -> C end,
    NewRowRem = RowRem - Val,
    NewC = C - Val,
    {RestCols, RestVals, FinalRowRem} = process_row(NewRowRem, Cs),
    {[NewC | RestCols], [Val | RestVals], FinalRowRem}.
```

## Elixir

```elixir
defmodule Solution do
  @spec restore_matrix(row_sum :: [integer], col_sum :: [integer]) :: [[integer]]
  def restore_matrix(row_sum, col_sum) do
    rows = length(row_sum)
    cols = length(col_sum)

    # initialize result matrix with zeros
    result = for _ <- 1..rows, do: List.duplicate(0, cols)

    loop(0, 0, row_sum, col_sum, result)
  end

  defp loop(i, j, row_sum, col_sum, result) do
    rows = length(row_sum)
    cols = length(col_sum)

    cond do
      i >= rows or j >= cols ->
        result

      true ->
        r_val = Enum.at(row_sum, i)
        c_val = Enum.at(col_sum, j)
        v = if r_val < c_val, do: r_val, else: c_val

        # update matrix cell
        row = Enum.at(result, i) |> List.replace_at(j, v)
        result2 = List.replace_at(result, i, row)

        # update remaining sums
        new_r = r_val - v
        new_c = c_val - v
        row_sum2 = List.replace_at(row_sum, i, new_r)
        col_sum2 = List.replace_at(col_sum, j, new_c)

        if new_r == 0 do
          loop(i + 1, j, row_sum2, col_sum2, result2)
        else
          loop(i, j + 1, row_sum2, col_sum2, result2)
        end
    end
  end
end
```

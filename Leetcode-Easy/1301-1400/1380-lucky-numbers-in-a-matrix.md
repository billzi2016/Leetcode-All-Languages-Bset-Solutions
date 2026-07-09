# 1380. Lucky Numbers in a Matrix

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> luckyNumbers(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> rowMin(m, INT_MAX);
        vector<int> colMax(n, INT_MIN);
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rowMin[i] = min(rowMin[i], matrix[i][j]);
                colMax[j] = max(colMax[j], matrix[i][j]);
            }
        }
        
        vector<int> ans;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == rowMin[i] && matrix[i][j] == colMax[j]) {
                    ans.push_back(matrix[i][j]);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        int[] rowMin = new int[m];
        Arrays.fill(rowMin, Integer.MAX_VALUE);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] < rowMin[i]) {
                    rowMin[i] = matrix[i][j];
                }
            }
        }

        int[] colMax = new int[n];
        Arrays.fill(colMax, Integer.MIN_VALUE);
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                if (matrix[i][j] > colMax[j]) {
                    colMax[j] = matrix[i][j];
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = matrix[i][j];
                if (val == rowMin[i] && val == colMax[j]) {
                    result.add(val);
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
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        row_min = [min(row) for row in matrix]
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        res = []
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                if val == row_min[i] and val == col_max[j]:
                    res.append(val)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_min = [min(row) for row in matrix]
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        res = []
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                if val == row_min[i] and val == col_max[j]:
                    res.append(val)
        return res
```

## C

```c
#include <stdlib.h>
#include <limits.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* luckyNumbers(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    if (matrixSize == 0 || matrixColSize == NULL) {
        *returnSize = 0;
        return NULL;
    }
    
    int rows = matrixSize;
    int cols = matrixColSize[0];
    
    int *rowMin = (int *)malloc(rows * sizeof(int));
    int *colMax = (int *)malloc(cols * sizeof(int));
    
    for (int i = 0; i < rows; ++i) rowMin[i] = INT_MAX;
    for (int j = 0; j < cols; ++j) colMax[j] = INT_MIN;
    
    // Compute row minima and column maxima
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            int val = matrix[i][j];
            if (val < rowMin[i]) rowMin[i] = val;
            if (val > colMax[j]) colMax[j] = val;
        }
    }
    
    // Collect lucky numbers
    int *result = (int *)malloc(rows * sizeof(int)); // at most one per row
    int cnt = 0;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            int val = matrix[i][j];
            if (val == rowMin[i] && val == colMax[j]) {
                result[cnt++] = val;
            }
        }
    }
    
    free(rowMin);
    free(colMax);
    
    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> LuckyNumbers(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[] rowMin = new int[m];
        int[] colMax = new int[n];
        
        for (int i = 0; i < m; i++) {
            rowMin[i] = int.MaxValue;
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] < rowMin[i]) rowMin[i] = matrix[i][j];
            }
        }
        
        for (int j = 0; j < n; j++) {
            colMax[j] = int.MinValue;
            for (int i = 0; i < m; i++) {
                if (matrix[i][j] > colMax[j]) colMax[j] = matrix[i][j];
            }
        }
        
        List<int> result = new List<int>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == rowMin[i] && matrix[i][j] == colMax[j]) {
                    result.Add(matrix[i][j]);
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
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const rowMin = new Array(m).fill(Infinity);
    const colMax = new Array(n).fill(-Infinity);
    
    // Compute minimum of each row and maximum of each column
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const val = matrix[i][j];
            if (val < rowMin[i]) rowMin[i] = val;
            if (val > colMax[j]) colMax[j] = val;
        }
    }
    
    // Collect lucky numbers
    const result = [];
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const val = matrix[i][j];
            if (val === rowMin[i] && val === colMax[j]) {
                result.push(val);
            }
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function luckyNumbers(matrix: number[][]): number[] {
    const m = matrix.length;
    const n = matrix[0].length;
    const rowMin = new Array(m).fill(Infinity);
    const colMax = new Array(n).fill(-Infinity);
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const val = matrix[i][j];
            if (val < rowMin[i]) rowMin[i] = val;
            if (val > colMax[j]) colMax[j] = val;
        }
    }
    
    const result: number[] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const val = matrix[i][j];
            if (val === rowMin[i] && val === colMax[j]) {
                result.push(val);
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
     * @param Integer[][] $matrix
     * @return Integer[]
     */
    function luckyNumbers($matrix) {
        $m = count($matrix);
        if ($m == 0) return [];
        $n = count($matrix[0]);

        // Row minima
        $rowMins = [];
        for ($i = 0; $i < $m; $i++) {
            $minVal = $matrix[$i][0];
            for ($j = 1; $j < $n; $j++) {
                if ($matrix[$i][$j] < $minVal) {
                    $minVal = $matrix[$i][$j];
                }
            }
            $rowMins[$i] = $minVal;
        }

        // Column maxima
        $colMaxes = array_fill(0, $n, PHP_INT_MIN);
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $m; $i++) {
                if ($matrix[$i][$j] > $colMaxes[$j]) {
                    $colMaxes[$j] = $matrix[$i][$j];
                }
            }
        }

        // Collect lucky numbers
        $result = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($matrix[$i][$j] === $rowMins[$i] && $matrix[$i][$j] === $colMaxes[$j]) {
                    $result[] = $matrix[$i][$j];
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
    func luckyNumbers(_ matrix: [[Int]]) -> [Int] {
        let m = matrix.count
        guard m > 0 else { return [] }
        let n = matrix[0].count
        
        var rowMins = Array(repeating: Int.max, count: m)
        for i in 0..<m {
            for val in matrix[i] {
                if val < rowMins[i] {
                    rowMins[i] = val
                }
            }
        }
        
        var colMaxs = Array(repeating: Int.min, count: n)
        for j in 0..<n {
            for i in 0..<m {
                let val = matrix[i][j]
                if val > colMaxs[j] {
                    colMaxs[j] = val
                }
            }
        }
        
        var result = [Int]()
        for i in 0..<m {
            for j in 0..<n {
                let val = matrix[i][j]
                if val == rowMins[i] && val == colMaxs[j] {
                    result.append(val)
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
    fun luckyNumbers(matrix: Array<IntArray>): List<Int> {
        val m = matrix.size
        if (m == 0) return emptyList()
        val n = matrix[0].size

        val rowMins = IntArray(m) { Int.MAX_VALUE }
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (matrix[i][j] < rowMins[i]) rowMins[i] = matrix[i][j]
            }
        }

        val colMaxs = IntArray(n) { Int.MIN_VALUE }
        for (j in 0 until n) {
            for (i in 0 until m) {
                if (matrix[i][j] > colMaxs[j]) colMaxs[j] = matrix[i][j]
            }
        }

        val result = mutableListOf<Int>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                val v = matrix[i][j]
                if (v == rowMins[i] && v == colMaxs[j]) {
                    result.add(v)
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> luckyNumbers(List<List<int>> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;

    // Minimum of each row
    List<int> rowMins = List.filled(m, 0);
    for (int i = 0; i < m; i++) {
      int minVal = matrix[i][0];
      for (int j = 1; j < n; j++) {
        if (matrix[i][j] < minVal) {
          minVal = matrix[i][j];
        }
      }
      rowMins[i] = minVal;
    }

    // Maximum of each column
    List<int> colMaxs = List.filled(n, 0);
    for (int j = 0; j < n; j++) {
      int maxVal = matrix[0][j];
      for (int i = 1; i < m; i++) {
        if (matrix[i][j] > maxVal) {
          maxVal = matrix[i][j];
        }
      }
      colMaxs[j] = maxVal;
    }

    // Collect lucky numbers
    List<int> result = [];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int val = matrix[i][j];
        if (val == rowMins[i] && val == colMaxs[j]) {
          result.add(val);
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func luckyNumbers(matrix [][]int) []int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return []int{}
	}
	m, n := len(matrix), len(matrix[0])
	rowMins := make([]int, m)
	colMaxs := make([]int, n)

	for i := 0; i < m; i++ {
		rowMins[i] = matrix[i][0]
	}
	for j := 0; j < n; j++ {
		colMaxs[j] = matrix[0][j]
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] < rowMins[i] {
				rowMins[i] = matrix[i][j]
			}
			if matrix[i][j] > colMaxs[j] {
				colMaxs[j] = matrix[i][j]
			}
		}
	}

	res := []int{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == rowMins[i] && matrix[i][j] == colMaxs[j] {
				res = append(res, matrix[i][j])
			}
		}
	}
	return res
}
```

## Ruby

```ruby
def lucky_numbers(matrix)
  rows = matrix.size
  cols = matrix[0].size
  row_min = Array.new(rows, Float::INFINITY)
  col_max = Array.new(cols, -Float::INFINITY)

  matrix.each_with_index do |row, i|
    row.each_with_index do |val, j|
      row_min[i] = val if val < row_min[i]
      col_max[j] = val if val > col_max[j]
    end
  end

  result = []
  matrix.each_with_index do |row, i|
    row.each_with_index do |val, j|
      result << val if val == row_min[i] && val == col_max[j]
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def luckyNumbers(matrix: Array[Array[Int]]): List[Int] = {
        val m = matrix.length
        if (m == 0) return Nil
        val n = matrix(0).length

        // Minimum of each row
        val rowMin = new Array[Int](m)
        for (i <- 0 until m) {
            var minVal = Int.MaxValue
            for (j <- 0 until n) {
                if (matrix(i)(j) < minVal) minVal = matrix(i)(j)
            }
            rowMin(i) = minVal
        }

        // Maximum of each column
        val colMax = new Array[Int](n)
        java.util.Arrays.fill(colMax, Int.MinValue)
        for (j <- 0 until n) {
            var maxVal = Int.MinValue
            for (i <- 0 until m) {
                if (matrix(i)(j) > maxVal) maxVal = matrix(i)(j)
            }
            colMax(j) = maxVal
        }

        // Collect lucky numbers
        val result = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 0 until m; j <- 0 until n) {
            val v = matrix(i)(j)
            if (v == rowMin(i) && v == colMax(j)) result += v
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn lucky_numbers(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let m = matrix.len();
        if m == 0 {
            return vec![];
        }
        let n = matrix[0].len();

        // Minimum of each row
        let mut row_mins = vec![i32::MAX; m];
        for i in 0..m {
            for &val in &matrix[i] {
                if val < row_mins[i] {
                    row_mins[i] = val;
                }
            }
        }

        // Maximum of each column
        let mut col_maxs = vec![i32::MIN; n];
        for i in 0..m {
            for j in 0..n {
                let val = matrix[i][j];
                if val > col_maxs[j] {
                    col_maxs[j] = val;
                }
            }
        }

        // Collect lucky numbers
        let mut result = Vec::new();
        for i in 0..m {
            for j in 0..n {
                let val = matrix[i][j];
                if val == row_mins[i] && val == col_maxs[j] {
                    result.push(val);
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (lucky-numbers matrix)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((rows (length matrix))
         (cols (if (null? matrix) 0 (length (first matrix))))
         (row-mins (map (lambda (row) (apply min row)) matrix))
         (col-maxs
           (let ((vec (make-vector cols #f)))
             (for ([row matrix])
               (for ([j (in-range cols)])
                 (define val (list-ref row j))
                 (define cur (vector-ref vec j))
                 (when (or (not cur) (> val cur))
                   (vector-set! vec j val))))
             (vector->list vec))))
    (for/list ([i (in-range rows)]
               [j (in-range cols)]
               #:when (= (list-ref (list-ref matrix i) j)
                         (list-ref row-mins i))
               #:when (= (list-ref (list-ref matrix i) j)
                         (list-ref col-maxs j)))
      (list-ref (list-ref matrix i) j))))
```

## Erlang

```erlang
-spec lucky_numbers(Matrix :: [[integer()]]) -> [integer()].
lucky_numbers(Matrix) ->
    RowMins = [lists:min(Row) || Row <- Matrix],
    C = length(hd(Matrix)),
    ColMaxes = [max_in_column(J, Matrix) || J <- lists:seq(1, C)],
    RowIndices = lists:seq(1, length(Matrix)),
    RowsWithIdx = lists:zip(RowIndices, Matrix),
    ColIndices = lists:seq(1, C),
    [Val ||
        {I, Row} <- RowsWithIdx,
        {J, Val} <- lists:zip(ColIndices, Row),
        Val == lists:nth(I, RowMins),
        Val == lists:nth(J, ColMaxes)].

max_in_column(Index, Matrix) ->
    lists:max([lists:nth(Index, Row) || Row <- Matrix]).
```

## Elixir

```elixir
defmodule Solution do
  @spec lucky_numbers(matrix :: [[integer]]) :: [integer]
  def lucky_numbers(matrix) do
    rows = length(matrix)
    cols = matrix |> List.first() |> length()

    # Minimum of each row
    row_mins = Enum.map(matrix, &Enum.min/1)

    # Maximum of each column
    col_maxs =
      Enum.reduce(matrix, List.duplicate(0, cols), fn row, acc ->
        Enum.with_index(row)
        |> Enum.reduce(acc, fn {val, j}, cur_acc ->
          if val > Enum.at(cur_acc, j) do
            List.replace_at(cur_acc, j, val)
          else
            cur_acc
          end
        end)
      end)

    # Collect lucky numbers
    matrix
    |> Enum.with_index()
    |> Enum.flat_map(fn {row, i} ->
      row
      |> Enum.with_index()
      |> Enum.filter(fn {val, j} ->
        val == Enum.at(row_mins, i) and val == Enum.at(col_maxs, j)
      end)
      |> Enum.map(fn {val, _j} -> val end)
    end)
  end
end
```

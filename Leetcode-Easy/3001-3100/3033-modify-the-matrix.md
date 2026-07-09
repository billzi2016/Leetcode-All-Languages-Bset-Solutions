# 3033. Modify the Matrix

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> modifiedMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> colMax(n, INT_MIN);
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                colMax[j] = max(colMax[j], matrix[i][j]);
            }
        }
        vector<vector<int>> answer = matrix;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (answer[i][j] == -1) {
                    answer[i][j] = colMax[j];
                }
            }
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[][] modifiedMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] colMax = new int[n];
        for (int j = 0; j < n; j++) {
            colMax[j] = Integer.MIN_VALUE;
        }
        // Find maximum in each column
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] > colMax[j]) {
                    colMax[j] = matrix[i][j];
                }
            }
        }
        // Build answer matrix with replacements
        int[][] answer = new int[m][n];
        for (int i = 0; i < m; i++) {
            System.arraycopy(matrix[i], 0, answer[i], 0, n);
            for (int j = 0; j < n; j++) {
                if (answer[i][j] == -1) {
                    answer[i][j] = colMax[j];
                }
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        # Compute maximum for each column
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        # Build answer matrix with replacements
        ans = []
        for i in range(m):
            row = []
            for j in range(n):
                if matrix[i][j] == -1:
                    row.append(col_max[j])
                else:
                    row.append(matrix[i][j])
            ans.append(row)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        # Compute max for each column
        col_max = [float('-inf')] * n
        for j in range(n):
            mx = float('-inf')
            for i in range(m):
                val = matrix[i][j]
                if val != -1 and val > mx:
                    mx = val
            col_max[j] = mx
        # Build answer matrix with replacements
        ans = [row[:] for row in matrix]
        for i in range(m):
            for j in range(n):
                if ans[i][j] == -1:
                    ans[i][j] = col_max[j]
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** modifiedMatrix(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int*** returnColumnSizes) {
    // The problem expects returnColumnSizes as int**, but the provided signature uses int**.
    // Adjust to match typical LeetCode signature:
    // int** modifiedMatrix(..., int** returnColumnSizes)
    // However, we keep the given parameters and cast accordingly.
    (void)returnColumnSizes; // suppress unused warning if not needed
    int m = matrixSize;
    int n = matrixColSize[0];
    
    // Compute column maxima
    int *colMax = (int *)malloc(n * sizeof(int));
    for (int j = 0; j < n; ++j) colMax[j] = INT_MIN;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (matrix[i][j] > colMax[j]) colMax[j] = matrix[i][j];
        }
    }
    
    // Allocate answer matrix
    int **ans = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        ans[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) {
            if (matrix[i][j] == -1)
                ans[i][j] = colMax[j];
            else
                ans[i][j] = matrix[i][j];
        }
    }
    
    // Set return sizes
    *returnSize = m;
    int **colSizesPtr = (int **)malloc(sizeof(int *));
    *colSizesPtr = (int *)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) {
        (*colSizesPtr)[i] = n;
    }
    // The caller expects returnColumnSizes to be int**, so assign
    *(int ***)returnColumnSizes = colSizesPtr;
    
    free(colMax);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] ModifiedMatrix(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[] colMax = new int[n];
        // Initialize with minimum possible value
        for (int j = 0; j < n; j++) colMax[j] = int.MinValue;

        // Compute maximum of each column
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] > colMax[j]) {
                    colMax[j] = matrix[i][j];
                }
            }
        }

        // Create answer copy and replace -1s
        int[][] answer = new int[m][];
        for (int i = 0; i < m; i++) {
            answer[i] = (int[])matrix[i].Clone();
            for (int j = 0; j < n; j++) {
                if (answer[i][j] == -1) {
                    answer[i][j] = colMax[j];
                }
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var modifiedMatrix = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    // Compute max for each column
    const colMax = new Array(n).fill(-Infinity);
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (matrix[i][j] > colMax[j]) {
                colMax[j] = matrix[i][j];
            }
        }
    }
    // Build answer matrix
    const ans = new Array(m);
    for (let i = 0; i < m; ++i) {
        ans[i] = matrix[i].slice(); // copy row
        for (let j = 0; j < n; ++j) {
            if (ans[i][j] === -1) {
                ans[i][j] = colMax[j];
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function modifiedMatrix(matrix: number[][]): number[][] {
    const m = matrix.length;
    const n = matrix[0].length;
    const colMax = new Array(n).fill(-Infinity);
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] > colMax[j]) {
                colMax[j] = matrix[i][j];
            }
        }
    }
    
    const answer: number[][] = matrix.map(row => row.slice());
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (answer[i][j] === -1) {
                answer[i][j] = colMax[j];
            }
        }
    }
    
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function modifiedMatrix($matrix) {
        $m = count($matrix);
        if ($m === 0) return $matrix;
        $n = count($matrix[0]);
        $colMax = array_fill(0, $n, PHP_INT_MIN);

        // Find maximum in each column (ignore -1)
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($matrix[$i][$j] != -1 && $matrix[$i][$j] > $colMax[$j]) {
                    $colMax[$j] = $matrix[$i][$j];
                }
            }
        }

        // Replace -1 with column maximum
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($matrix[$i][$j] == -1) {
                    $matrix[$i][$j] = $colMax[$j];
                }
            }
        }

        return $matrix;
    }
}
```

## Swift

```swift
class Solution {
    func modifiedMatrix(_ matrix: [[Int]]) -> [[Int]] {
        let m = matrix.count
        guard m > 0 else { return [] }
        let n = matrix[0].count
        var colMax = Array(repeating: Int.min, count: n)
        for i in 0..<m {
            for j in 0..<n {
                if matrix[i][j] > colMax[j] {
                    colMax[j] = matrix[i][j]
                }
            }
        }
        var ans = matrix
        for i in 0..<m {
            for j in 0..<n {
                if ans[i][j] == -1 {
                    ans[i][j] = colMax[j]
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun modifiedMatrix(matrix: Array<IntArray>): Array<IntArray> {
        val m = matrix.size
        if (m == 0) return arrayOf()
        val n = matrix[0].size
        val colMax = IntArray(n) { Int.MIN_VALUE }
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (matrix[i][j] > colMax[j]) {
                    colMax[j] = matrix[i][j]
                }
            }
        }
        val answer = Array(m) { IntArray(n) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                answer[i][j] = if (matrix[i][j] == -1) colMax[j] else matrix[i][j]
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> modifiedMatrix(List<List<int>> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    List<int> colMax = List.filled(n, -1);
    for (int j = 0; j < n; j++) {
      int mx = -1;
      for (int i = 0; i < m; i++) {
        if (matrix[i][j] > mx) mx = matrix[i][j];
      }
      colMax[j] = mx;
    }

    List<List<int>> ans = List.generate(m, (_) => List.filled(n, 0));
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int val = matrix[i][j];
        if (val == -1) val = colMax[j];
        ans[i][j] = val;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func modifiedMatrix(matrix [][]int) [][]int {
	m := len(matrix)
	n := len(matrix[0])
	colMax := make([]int, n)

	// Compute maximum for each column
	for j := 0; j < n; j++ {
		maxVal := matrix[0][j]
		for i := 1; i < m; i++ {
			if matrix[i][j] > maxVal {
				maxVal = matrix[i][j]
			}
		}
		colMax[j] = maxVal
	}

	// Build answer matrix with replacements
	ans := make([][]int, m)
	for i := 0; i < m; i++ {
		rowCopy := make([]int, n)
		copy(rowCopy, matrix[i])
		for j := 0; j < n; j++ {
			if rowCopy[j] == -1 {
				rowCopy[j] = colMax[j]
			}
		}
		ans[i] = rowCopy
	}
	return ans
}
```

## Ruby

```ruby
def modified_matrix(matrix)
  m = matrix.size
  n = matrix[0].size
  col_max = Array.new(n, -Float::INFINITY)

  matrix.each do |row|
    row.each_with_index do |val, j|
      col_max[j] = val if val > col_max[j]
    end
  end

  answer = matrix.map(&:dup)
  answer.each do |row|
    row.each_index do |j|
      row[j] = col_max[j] if row[j] == -1
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
    def modifiedMatrix(matrix: Array[Array[Int]]): Array[Array[Int]] = {
        val m = matrix.length
        val n = if (m == 0) 0 else matrix(0).length
        val colMax = Array.fill(n)(Int.MinValue)

        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                val v = matrix(i)(j)
                if (v != -1 && v > colMax(j)) colMax(j) = v
                j += 1
            }
            i += 1
        }

        val ans = Array.ofDim[Int](m, n)
        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                val v = matrix(i)(j)
                ans(i)(j) = if (v == -1) colMax(j) else v
                j += 1
            }
            i += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn modified_matrix(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = matrix.len();
        if m == 0 {
            return matrix;
        }
        let n = matrix[0].len();
        // Compute maximum for each column
        let mut col_max = vec![i32::MIN; n];
        for i in 0..m {
            for j in 0..n {
                if matrix[i][j] > col_max[j] {
                    col_max[j] = matrix[i][j];
                }
            }
        }
        // Build answer matrix with replacements
        let mut ans = matrix.clone();
        for i in 0..m {
            for j in 0..n {
                if ans[i][j] == -1 {
                    ans[i][j] = col_max[j];
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (modified-matrix matrix)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((n (length (car matrix)))
         (col-maxes
          (let ((maxs (make-vector n -1))) ; each column has at least one non‑negative value
            (for-each (lambda (row)
                        (for ([j (in-range n)])
                          (let ((val (list-ref row j)))
                            (when (> val (vector-ref maxs j))
                              (vector-set! maxs j val)))))
                      matrix)
            (vector->list maxs))))
    (for/list ([row matrix])
      (for/list ([val row] [idx (in-naturals)])
        (if (= val -1) (list-ref col-maxes idx) val)))))
```

## Erlang

```erlang
-spec modified_matrix(Matrix :: [[integer()]]) -> [[integer()]].
modified_matrix(Matrix) ->
    MaxCols = column_maxes(Matrix),
    [replace_row(Row, MaxCols) || Row <- Matrix].

column_maxes(Matrix) ->
    Transposed = transpose(Matrix),
    [lists:max(Col) || Col <- Transposed].

transpose([]) -> [];
transpose([[]|_]) -> [];
transpose(Rows) ->
    FirstCol = [hd(Row) || Row <- Rows],
    RestRows = [tl(Row) || Row <- Rows],
    [FirstCol | transpose(RestRows)].

replace_row([], []) -> [];
replace_row([V|Vs], [M|Ms]) ->
    NewVal = case V of
        -1 -> M;
        _  -> V
    end,
    [NewVal | replace_row(Vs, Ms)].
```

## Elixir

```elixir
defmodule Solution do
  @spec modified_matrix(matrix :: [[integer]]) :: [[integer]]
  def modified_matrix(matrix) do
    n = length(List.first(matrix))

    col_maxes =
      for j <- 0..(n - 1) do
        matrix
        |> Enum.map(&Enum.at(&1, j))
        |> Enum.max()
      end

    for row <- matrix do
      for {val, idx} <- Enum.with_index(row) do
        if val == -1, do: Enum.at(col_maxes, idx), else: val
      end
    end
  end
end
```

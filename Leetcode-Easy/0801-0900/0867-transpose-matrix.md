# 0867. Transpose Matrix

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> ans(n, vector<int>(m));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans[j][i] = matrix[i][j];
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[][] transpose(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] ans = new int[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans[j][i] = matrix[i][j];
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(col) for col in zip(*matrix)]
```

## Python3

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(col) for col in zip(*matrix)]
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    if (matrixSize == 0 || matrixColSize == NULL) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    int rows = matrixSize;          // original number of rows
    int cols = matrixColSize[0];    // original number of columns (all rows have same length)
    
    *returnSize = cols;
    *returnColumnSizes = (int*)malloc(sizeof(int) * cols);
    for (int i = 0; i < cols; ++i) {
        (*returnColumnSizes)[i] = rows;
    }
    
    int** result = (int**)malloc(sizeof(int*) * cols);
    for (int i = 0; i < cols; ++i) {
        result[i] = (int*)malloc(sizeof(int) * rows);
        for (int j = 0; j < rows; ++j) {
            result[i][j] = matrix[j][i];
        }
    }
    
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] Transpose(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[][] transposed = new int[n][];
        for (int i = 0; i < n; i++) {
            transposed[i] = new int[m];
            for (int j = 0; j < m; j++) {
                transposed[i][j] = matrix[j][i];
            }
        }
        return transposed;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const res = new Array(n);
    for (let i = 0; i < n; ++i) {
        const row = new Array(m);
        for (let j = 0; j < m; ++j) {
            row[j] = matrix[j][i];
        }
        res[i] = row;
    }
    return res;
};
```

## Typescript

```typescript
function transpose(matrix: number[][]): number[][] {
    const m = matrix.length;
    const n = matrix[0].length;
    const result: number[][] = Array.from({ length: n }, () => new Array<number>(m));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            result[j][i] = matrix[i][j];
        }
    }
    return result;
};
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function transpose($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $result = array_fill(0, $n, []);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $result[$j][$i] = $matrix[$i][$j];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func transpose(_ matrix: [[Int]]) -> [[Int]] {
        let m = matrix.count
        guard m > 0 else { return [] }
        let n = matrix[0].count
        var result = Array(repeating: Array(repeating: 0, count: m), count: n)
        for i in 0..<m {
            for j in 0..<n {
                result[j][i] = matrix[i][j]
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun transpose(matrix: Array<IntArray>): Array<IntArray> {
        val m = matrix.size
        val n = matrix[0].size
        val result = Array(n) { IntArray(m) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                result[j][i] = matrix[i][j]
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> transpose(List<List<int>> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    List<List<int>> result = List.generate(n, (_) => List.filled(m, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        result[j][i] = matrix[i][j];
      }
    }
    return result;
  }
}
```

## Golang

```go
func transpose(matrix [][]int) [][]int {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return [][]int{}
    }
    rows, cols := len(matrix), len(matrix[0])
    ans := make([][]int, cols)
    for i := 0; i < cols; i++ {
        ans[i] = make([]int, rows)
        for j := 0; j < rows; j++ {
            ans[i][j] = matrix[j][i]
        }
    }
    return ans
}
```

## Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Integer[][]}
def transpose(matrix)
  rows = matrix.length
  cols = matrix[0].length
  (0...cols).map { |c| (0...rows).map { |r| matrix[r][c] } }
end
```

## Scala

```scala
object Solution {
    def transpose(matrix: Array[Array[Int]]): Array[Array[Int]] = {
        val m = matrix.length
        val n = matrix(0).length
        val res = Array.ofDim[Int](n, m)
        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                res(j)(i) = matrix(i)(j)
                j += 1
            }
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn transpose(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = matrix.len();
        if m == 0 {
            return vec![];
        }
        let n = matrix[0].len();
        let mut ans = vec![vec![0; m]; n];
        for i in 0..m {
            for j in 0..n {
                ans[j][i] = matrix[i][j];
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (transpose matrix)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ([rows (length matrix)]
         [cols (if (null? matrix) 0 (length (car matrix)))])
    (for/list ([j (in-range cols)])
      (for/list ([i (in-range rows)])
        (list-ref (list-ref matrix i) j)))))
```

## Erlang

```erlang
-spec transpose(Matrix :: [[integer()]]) -> [[integer()]].
transpose([]) -> [];
transpose([[]|_]) -> [];
transpose(Matrix) ->
    Heads = [hd(Row) || Row <- Matrix],
    Tails = [tl(Row) || Row <- Matrix],
    [Heads | transpose(Tails)].
```

## Elixir

```elixir
defmodule Solution do
  @spec transpose(matrix :: [[integer]]) :: [[integer]]
  def transpose(matrix) do
    cols = length(hd(matrix))
    for col_idx <- 0..(cols - 1) do
      for row <- matrix, do: Enum.at(row, col_idx)
    end
  end
end
```

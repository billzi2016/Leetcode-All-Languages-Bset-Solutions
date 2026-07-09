# 0766. Toeplitz Matrix

## Cpp

```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return true;
        int n = matrix[0].size();
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] != matrix[i-1][j-1])
                    return false;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (matrix[i][j] != matrix[i + 1][j + 1]) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
```

## C

```c
#include <stdbool.h>

bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) return true;
    int n = matrixColSize[0];
    for (int i = 1; i < matrixSize; ++i) {
        for (int j = 1; j < n; ++j) {
            if (matrix[i][j] != matrix[i - 1][j - 1]) {
                return false;
            }
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsToeplitzMatrix(int[][] matrix) {
        int m = matrix.Length;
        int n = matrix[0].Length;
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (matrix[i][j] != matrix[i + 1][j + 1]) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var isToeplitzMatrix = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    for (let i = 0; i < m - 1; ++i) {
        for (let j = 0; j < n - 1; ++j) {
            if (matrix[i][j] !== matrix[i + 1][j + 1]) {
                return false;
            }
        }
    }
    return true;
};
```

## Typescript

```typescript
function isToeplitzMatrix(matrix: number[][]): boolean {
    const m = matrix.length;
    const n = matrix[0].length;
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (matrix[i][j] !== matrix[i - 1][j - 1]) {
                return false;
            }
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Boolean
     */
    function isToeplitzMatrix($matrix) {
        $rows = count($matrix);
        $cols = count($matrix[0]);

        for ($i = 1; $i < $rows; $i++) {
            for ($j = 1; $j < $cols; $j++) {
                if ($matrix[$i][$j] !== $matrix[$i - 1][$j - 1]) {
                    return false;
                }
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        let rows = matrix.count
        guard rows > 0 else { return true }
        let cols = matrix[0].count
        
        for i in 1..<rows {
            for j in 1..<cols {
                if matrix[i][j] != matrix[i - 1][j - 1] {
                    return false
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isToeplitzMatrix(matrix: Array<IntArray>): Boolean {
        val m = matrix.size
        val n = matrix[0].size
        for (i in 0 until m - 1) {
            for (j in 0 until n - 1) {
                if (matrix[i][j] != matrix[i + 1][j + 1]) return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isToeplitzMatrix(List<List<int>> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        if (matrix[i][j] != matrix[i - 1][j - 1]) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func isToeplitzMatrix(matrix [][]int) bool {
    m := len(matrix)
    n := len(matrix[0])
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            if matrix[i][j] != matrix[i-1][j-1] {
                return false
            }
        }
    }
    return true
}
```

## Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Boolean}
def is_toeplitz_matrix(matrix)
  rows = matrix.length
  cols = matrix[0].length
  (0...rows-1).each do |i|
    (0...cols-1).each do |j|
      return false if matrix[i][j] != matrix[i+1][j+1]
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def isToeplitzMatrix(matrix: Array[Array[Int]]): Boolean = {
        val m = matrix.length
        if (m == 0) return true
        val n = matrix(0).length
        for (i <- 1 until m) {
            for (j <- 1 until n) {
                if (matrix(i)(j) != matrix(i - 1)(j - 1)) return false
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_toeplitz_matrix(matrix: Vec<Vec<i32>>) -> bool {
        let m = matrix.len();
        if m == 0 {
            return true;
        }
        let n = matrix[0].len();
        for i in 1..m {
            for j in 1..n {
                if matrix[i][j] != matrix[i - 1][j - 1] {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-toeplitz-matrix matrix)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((m (length matrix))
         (n (if (null? matrix) 0 (length (car matrix)))))
    (let loop ((i 0))
      (if (>= i (- m 1))
          #t
          (let inner-loop ((j 0))
            (cond
              [(>= j (- n 1)) (loop (+ i 1))]
              [else
               (if (= (list-ref (list-ref matrix i) j)
                      (list-ref (list-ref matrix (+ i 1)) (+ j 1)))
                   (inner-loop (+ j 1))
                   #f)]))))))
```

## Erlang

```erlang
-module(solution).
-export([is_toeplitz_matrix/1]).

-spec is_toeplitz_matrix(Matrix :: [[integer()]]) -> boolean().
is_toeplitz_matrix(Matrix) ->
    case Matrix of
        [] -> true;
        [_|_] ->
            Rows = length(Matrix),
            Cols = length(hd(Matrix)),
            check_rows(Matrix, Rows, Cols, 1)
    end.

check_rows(_Matrix, _Rows, _Cols, RowIdx) when RowIdx > _Rows - 1 ->
    true;
check_rows(Matrix, Rows, Cols, RowIdx) ->
    case check_cols(Matrix, Rows, Cols, RowIdx, 1) of
        false -> false;
        true -> check_rows(Matrix, Rows, Cols, RowIdx + 1)
    end.

check_cols(_Matrix, _Rows, _Cols, _RowIdx, ColIdx) when ColIdx > _Cols - 1 ->
    true;
check_cols(Matrix, _Rows, _Cols, RowIdx, ColIdx) ->
    A = get_elem(Matrix, RowIdx, ColIdx),
    B = get_elem(Matrix, RowIdx + 1, ColIdx + 1),
    if
        A =:= B -> check_cols(Matrix, _Rows, _Cols, RowIdx, ColIdx + 1);
        true -> false
    end.

get_elem(Matrix, R, C) ->
    lists:nth(C, lists:nth(R, Matrix)).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_toeplitz_matrix(matrix :: [[integer]]) :: boolean
  def is_toeplitz_matrix(matrix) do
    rows = length(matrix)
    cols = length(List.first(matrix))

    Enum.all?(0..rows - 1, fn i ->
      Enum.all?(0..cols - 1, fn j ->
        if i > 0 and j > 0 do
          Enum.at(Enum.at(matrix, i), j) == Enum.at(Enum.at(matrix, i - 1), j - 1)
        else
          true
        end
      end)
    end)
  end
end
```

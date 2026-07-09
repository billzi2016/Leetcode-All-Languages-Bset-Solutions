# 0074. Search a 2D Matrix

## Cpp

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        int m = matrix.size();
        int n = matrix[0].size();
        long long left = 0, right = static_cast<long long>(m) * n - 1;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            int val = matrix[mid / n][mid % n];
            if (val == target) return true;
            else if (val < target) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if (m == 0) return false;
        int n = matrix[0].length;
        int left = 0, right = m * n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int val = matrix[mid / n][mid % n];
            if (val == target) return true;
            if (val < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

## Python3

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

## C

```c
#include <stdbool.h>

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    if (matrixSize == 0 || matrixColSize == NULL || matrixColSize[0] == 0)
        return false;
    
    int n = matrixColSize[0];
    long left = 0;
    long right = (long)matrixSize * n - 1;
    
    while (left <= right) {
        long mid = left + (right - left) / 2;
        int row = mid / n;
        int col = mid % n;
        int val = matrix[row][col];
        
        if (val == target)
            return true;
        else if (val < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0) return false;
        int m = matrix.Length;
        int n = matrix[0].Length;
        int left = 0, right = m * n - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            int val = matrix[mid / n][mid % n];
            if (val == target) return true;
            if (val < target) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return false;
    const m = matrix.length;
    const n = matrix[0].length;
    let left = 0, right = m * n - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const row = Math.floor(mid / n);
        const col = mid % n;
        const val = matrix[row][col];
        if (val === target) return true;
        if (val < target) left = mid + 1;
        else right = mid - 1;
    }
    return false;
};
```

## Typescript

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    if (matrix.length === 0 || matrix[0].length === 0) return false;
    const m = matrix.length;
    const n = matrix[0].length;
    let left = 0;
    let right = m * n - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const i = Math.floor(mid / n);
        const j = mid % n;
        const val = matrix[i][j];
        if (val === target) return true;
        if (val < target) left = mid + 1;
        else right = mid - 1;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Boolean
     */
    function searchMatrix($matrix, $target) {
        $m = count($matrix);
        if ($m == 0) return false;
        $n = count($matrix[0]);
        $left = 0;
        $right = $m * $n - 1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            $row = intdiv($mid, $n);
            $col = $mid % $n;
            $val = $matrix[$row][$col];

            if ($val == $target) {
                return true;
            } elseif ($val < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        guard !matrix.isEmpty && !matrix[0].isEmpty else { return false }
        let rows = matrix.count
        let cols = matrix[0].count
        var left = 0
        var right = rows * cols - 1
        
        while left <= right {
            let mid = (left + right) / 2
            let i = mid / cols
            let j = mid % cols
            let value = matrix[i][j]
            
            if value == target {
                return true
            } else if value < target {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        val m = matrix.size
        if (m == 0) return false
        val n = matrix[0].size
        var left = 0
        var right = m * n - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            val row = mid / n
            val col = mid % n
            val value = matrix[row][col]
            when {
                value == target -> return true
                value < target -> left = mid + 1
                else -> right = mid - 1
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool searchMatrix(List<List<int>> matrix, int target) {
    if (matrix.isEmpty || matrix[0].isEmpty) return false;
    final int m = matrix.length;
    final int n = matrix[0].length;
    int left = 0;
    int right = m * n - 1;

    while (left <= right) {
      final int mid = left + ((right - left) >> 1);
      final int row = mid ~/ n;
      final int col = mid % n;
      final int val = matrix[row][col];

      if (val == target) return true;
      if (val < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return false;
  }
}
```

## Golang

```go
func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	m, n := len(matrix), len(matrix[0])
	left, right := 0, m*n-1
	for left <= right {
		mid := left + (right-left)/2
		i, j := mid/n, mid%n
		val := matrix[i][j]
		if val == target {
			return true
		}
		if val < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return false
}
```

## Ruby

```ruby
def search_matrix(matrix, target)
  return false if matrix.nil? || matrix.empty? || matrix[0].empty?
  m = matrix.length
  n = matrix[0].length
  left = 0
  right = m * n - 1
  while left <= right
    mid = (left + right) / 2
    val = matrix[mid / n][mid % n]
    if val == target
      return true
    elsif val < target
      left = mid + 1
    else
      right = mid - 1
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def searchMatrix(matrix: Array[Array[Int]], target: Int): Boolean = {
        val m = matrix.length
        val n = matrix(0).length
        var left = 0
        var right = m * n - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            val i = mid / n
            val j = mid % n
            val value = matrix(i)(j)
            if (value == target) return true
            else if (value < target) left = mid + 1
            else right = mid - 1
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        if matrix.is_empty() || matrix[0].is_empty() {
            return false;
        }
        let m = matrix.len();
        let n = matrix[0].len();
        let mut left: i64 = 0;
        let mut right: i64 = (m * n - 1) as i64;

        while left <= right {
            let mid = left + (right - left) / 2;
            let i = (mid / n as i64) as usize;
            let j = (mid % n as i64) as usize;
            let val = matrix[i][j];
            if val == target {
                return true;
            } else if val < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (search-matrix matrix target)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  (let* ((row-vecs (list->vector (map list->vector matrix)))
         (m (vector-length row-vecs))
         (n (if (> m 0) (vector-length (vector-ref row-vecs 0)) 0)))
    (let loop ((low 0) (high (- (* m n) 1)))
      (if (> low high)
          #f
          (let* ((mid (quotient (+ low high) 2))
                 (row (quotient mid n))
                 (col (remainder mid n))
                 (val (vector-ref (vector-ref row-vecs row) col)))
            (cond [(= val target) #t]
                  [(< val target) (loop (+ mid 1) high)]
                  [else (loop low (- mid 1))]))))))
```

## Erlang

```erlang
-module(solution).
-export([search_matrix/2]).
-spec search_matrix(Matrix :: [[integer()]], Target :: integer()) -> boolean().
search_matrix(Matrix, Target) ->
    Rows = length(Matrix),
    Cols = case Matrix of
               [] -> 0;
               [First|_] -> length(First)
           end,
    Total = Rows * Cols,
    binary_search(Matrix, Cols, Target, 0, Total - 1).

binary_search(_, _, _, Low, High) when Low > High ->
    false;
binary_search(Matrix, Cols, Target, Low, High) ->
    Mid = (Low + High) div 2,
    RowIdx = Mid div Cols,
    ColIdx = Mid rem Cols,
    RowList = lists:nth(RowIdx + 1, Matrix),
    Val = lists:nth(ColIdx + 1, RowList),
    case Target of
        T when T == Val -> true;
        T when T < Val -> binary_search(Matrix, Cols, Target, Low, Mid - 1);
        _ -> binary_search(Matrix, Cols, Target, Mid + 1, High)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec search_matrix(matrix :: [[integer]], target :: integer) :: boolean
  def search_matrix(matrix, target) do
    rows = length(matrix)
    cols = matrix |> List.first() |> length()
    binary_search(matrix, rows, cols, target, 0, rows * cols - 1)
  end

  defp binary_search(_matrix, _rows, _cols, _target, low, high) when low > high,
    do: false

  defp binary_search(matrix, rows, cols, target, low, high) do
    mid = div(low + high, 2)
    row = div(mid, cols)
    col = rem(mid, cols)

    val =
      matrix
      |> Enum.at(row)
      |> Enum.at(col)

    cond do
      val == target ->
        true

      val < target ->
        binary_search(matrix, rows, cols, target, mid + 1, high)

      true ->
        binary_search(matrix, rows, cols, target, low, mid - 1)
    end
  end
end
```

# 2133. Check if Every Row and Column Contains All Numbers

## Cpp

```cpp
class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> seen(n + 1);
        // Check rows
        for (int i = 0; i < n; ++i) {
            fill(seen.begin(), seen.end(), 0);
            for (int j = 0; j < n; ++j) {
                int val = matrix[i][j];
                if (seen[val]) return false;
                seen[val] = 1;
            }
        }
        // Check columns
        for (int j = 0; j < n; ++j) {
            fill(seen.begin(), seen.end(), 0);
            for (int i = 0; i < n; ++i) {
                int val = matrix[i][j];
                if (seen[val]) return false;
                seen[val] = 1;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkValid(int[][] matrix) {
        int n = matrix.length;
        // Check each row
        for (int i = 0; i < n; i++) {
            boolean[] seen = new boolean[n + 1];
            for (int j = 0; j < n; j++) {
                int val = matrix[i][j];
                if (val < 1 || val > n || seen[val]) {
                    return false;
                }
                seen[val] = true;
            }
        }
        // Check each column
        for (int j = 0; j < n; j++) {
            boolean[] seen = new boolean[n + 1];
            for (int i = 0; i < n; i++) {
                int val = matrix[i][j];
                if (val < 1 || val > n || seen[val]) {
                    return false;
                }
                seen[val] = true;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        target = set(range(1, n + 1))
        for i in range(n):
            if set(matrix[i]) != target:
                return False
            col_set = {matrix[row][i] for row in range(n)}
            if col_set != target:
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected = set(range(1, n + 1))
        for i in range(n):
            if set(matrix[i]) != expected:
                return False
            col_set = {matrix[row][i] for row in range(n)}
            if col_set != expected:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool checkValid(int** matrix, int matrixSize, int* matrixColSize) {
    int n = matrixSize;
    bool seen[101];  // n <= 100

    // Check rows
    for (int i = 0; i < n; ++i) {
        memset(seen, 0, sizeof(bool) * (n + 1));
        for (int j = 0; j < n; ++j) {
            int val = matrix[i][j];
            if (val < 1 || val > n || seen[val]) return false;
            seen[val] = true;
        }
    }

    // Check columns
    for (int j = 0; j < n; ++j) {
        memset(seen, 0, sizeof(bool) * (n + 1));
        for (int i = 0; i < n; ++i) {
            int val = matrix[i][j];
            if (val < 1 || val > n || seen[val]) return false;
            seen[val] = true;
        }
    }

    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckValid(int[][] matrix) {
        int n = matrix.Length;
        // Validate rows
        for (int i = 0; i < n; i++) {
            var seen = new bool[n + 1];
            for (int j = 0; j < n; j++) {
                int val = matrix[i][j];
                if (seen[val]) return false;
                seen[val] = true;
            }
        }
        // Validate columns
        for (int j = 0; j < n; j++) {
            var seen = new bool[n + 1];
            for (int i = 0; i < n; i++) {
                int val = matrix[i][j];
                if (seen[val]) return false;
                seen[val] = true;
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
var checkValid = function(matrix) {
    const n = matrix.length;
    for (let i = 0; i < n; i++) {
        const rowSet = new Set();
        const colSet = new Set();
        for (let j = 0; j < n; j++) {
            rowSet.add(matrix[i][j]);
            colSet.add(matrix[j][i]);
        }
        if (rowSet.size !== n || colSet.size !== n) return false;
    }
    return true;
};
```

## Typescript

```typescript
function checkValid(matrix: number[][]): boolean {
    const n = matrix.length;
    // Check rows
    for (let i = 0; i < n; i++) {
        const seen = new Array(n + 1).fill(false);
        for (let j = 0; j < n; j++) {
            const val = matrix[i][j];
            if (val < 1 || val > n || seen[val]) return false;
            seen[val] = true;
        }
    }
    // Check columns
    for (let j = 0; j < n; j++) {
        const seen = new Array(n + 1).fill(false);
        for (let i = 0; i < n; i++) {
            const val = matrix[i][j];
            if (val < 1 || val > n || seen[val]) return false;
            seen[val] = true;
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
    function checkValid($matrix) {
        $n = count($matrix);
        // Check rows
        for ($i = 0; $i < $n; $i++) {
            $seen = array_fill(0, $n + 1, false);
            for ($j = 0; $j < $n; $j++) {
                $val = $matrix[$i][$j];
                if ($val < 1 || $val > $n || $seen[$val]) {
                    return false;
                }
                $seen[$val] = true;
            }
        }

        // Check columns
        for ($j = 0; $j < $n; $j++) {
            $seen = array_fill(0, $n + 1, false);
            for ($i = 0; $i < $n; $i++) {
                $val = $matrix[$i][$j];
                if ($val < 1 || $val > $n || $seen[$val]) {
                    return false;
                }
                $seen[$val] = true;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkValid(_ matrix: [[Int]]) -> Bool {
        let n = matrix.count
        // Check each row
        for i in 0..<n {
            var seen = [Bool](repeating: false, count: n + 1)
            for j in 0..<n {
                let val = matrix[i][j]
                if seen[val] { return false }
                seen[val] = true
            }
        }
        // Check each column
        for j in 0..<n {
            var seen = [Bool](repeating: false, count: n + 1)
            for i in 0..<n {
                let val = matrix[i][j]
                if seen[val] { return false }
                seen[val] = true
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkValid(matrix: Array<IntArray>): Boolean {
        val n = matrix.size
        for (i in 0 until n) {
            val seenRow = BooleanArray(n + 1)
            val seenCol = BooleanArray(n + 1)
            for (j in 0 until n) {
                val rowVal = matrix[i][j]
                if (seenRow[rowVal]) return false
                seenRow[rowVal] = true

                val colVal = matrix[j][i]
                if (seenCol[colVal]) return false
                seenCol[colVal] = true
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkValid(List<List<int>> matrix) {
    int n = matrix.length;

    // Check each row
    for (int i = 0; i < n; i++) {
      List<bool> seen = List.filled(n + 1, false);
      for (int j = 0; j < n; j++) {
        int val = matrix[i][j];
        if (seen[val]) return false;
        seen[val] = true;
      }
    }

    // Check each column
    for (int j = 0; j < n; j++) {
      List<bool> seen = List.filled(n + 1, false);
      for (int i = 0; i < n; i++) {
        int val = matrix[i][j];
        if (seen[val]) return false;
        seen[val] = true;
      }
    }

    return true;
  }
}
```

## Golang

```go
func checkValid(matrix [][]int) bool {
    n := len(matrix)
    for i := 0; i < n; i++ {
        rowSeen := make([]bool, n+1)
        colSeen := make([]bool, n+1)
        for j := 0; j < n; j++ {
            rowVal := matrix[i][j]
            colVal := matrix[j][i]
            if rowVal < 1 || rowVal > n || colVal < 1 || colVal > n {
                return false
            }
            if rowSeen[rowVal] || colSeen[colVal] {
                // duplicate in current row or column
                return false
            }
            rowSeen[rowVal] = true
            colSeen[colVal] = true
        }
        // all numbers 1..n must appear; duplicates already caught, just verify completeness
        for k := 1; k <= n; k++ {
            if !rowSeen[k] || !colSeen[k] {
                return false
            }
        }
    }
    return true
}
```

## Ruby

```ruby
def check_valid(matrix)
  n = matrix.size
  target = (1..n).to_a
  matrix.each do |row|
    return false unless row.sort == target
  end
  (0...n).each do |c|
    col = []
    (0...n).each { |r| col << matrix[r][c] }
    return false unless col.sort == target
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkValid(matrix: Array[Array[Int]]): Boolean = {
        val n = matrix.length
        for (i <- 0 until n) {
            val rowSeen = new Array[Boolean](n + 1)
            val colSeen = new Array[Boolean](n + 1)
            for (j <- 0 until n) {
                val rv = matrix(i)(j)
                if (rowSeen(rv)) return false
                rowSeen(rv) = true

                val cv = matrix(j)(i)
                if (colSeen(cv)) return false
                colSeen(cv) = true
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_valid(matrix: Vec<Vec<i32>>) -> bool {
        let n = matrix.len();
        // Check rows
        for i in 0..n {
            let mut seen = vec![false; n + 1];
            for j in 0..n {
                let val = matrix[i][j] as usize;
                if val == 0 || val > n || seen[val] {
                    return false;
                }
                seen[val] = true;
            }
        }
        // Check columns
        for j in 0..n {
            let mut seen = vec![false; n + 1];
            for i in 0..n {
                let val = matrix[i][j] as usize;
                if val == 0 || val > n || seen[val] {
                    return false;
                }
                seen[val] = true;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-valid matrix)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((n (length matrix))
         (expected (range 1 (+ n 1))))
    (and
     ;; check each row
     (for/and ([row matrix])
       (equal? (sort row <) expected))
     ;; check each column
     (for/and ([j (in-range n)])
       (let ((col (map (lambda (row) (list-ref row j)) matrix)))
         (equal? (sort col <) expected))))))
```

## Erlang

```erlang
-spec check_valid(Matrix :: [[integer()]]) -> boolean().
check_valid(Matrix) ->
    N = length(Matrix),
    Expected = lists:seq(1, N),
    RowsValid = lists:all(fun(Row) -> lists:sort(Row) == Expected end, Matrix),
    if
        not RowsValid -> false;
        true -> columns_valid(1, N, Matrix, Expected)
    end.

columns_valid(J, N, _Matrix, _Expected) when J > N -> true;
columns_valid(J, N, Matrix, Expected) ->
    Col = [lists:nth(J, Row) || Row <- Matrix],
    case lists:sort(Col) == Expected of
        false -> false;
        true -> columns_valid(J + 1, N, Matrix, Expected)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_valid(matrix :: [[integer]]) :: boolean
  def check_valid(matrix) do
    n = length(matrix)

    rows_ok =
      Enum.all?(matrix, fn row ->
        MapSet.size(MapSet.new(row)) == n
      end)

    if not rows_ok do
      false
    else
      Enum.reduce_while(0..(n - 1), true, fn i, _acc ->
        col = Enum.map(matrix, fn row -> Enum.at(row, i) end)

        if MapSet.size(MapSet.new(col)) == n do
          {:cont, true}
        else
          {:halt, false}
        end
      end)
    end
  end
end
```

# 0073. Set Matrix Zeroes

## Cpp

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return;
        int n = matrix[0].size();
        bool firstRowZero = false, firstColZero = false;
        for (int j = 0; j < n; ++j) {
            if (matrix[0][j] == 0) { firstRowZero = true; break; }
        }
        for (int i = 0; i < m; ++i) {
            if (matrix[i][0] == 0) { firstColZero = true; break; }
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (firstRowZero) {
            for (int j = 0; j < n; ++j) matrix[0][j] = 0;
        }
        if (firstColZero) {
            for (int i = 0; i < m; ++i) matrix[i][0] = 0;
        }
    }
};
```

## Java

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean firstRowZero = false;
        boolean firstColZero = false;

        // Check first row for zero
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }
        }

        // Check first column for zero
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }

        // Use first row and column as markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Zero out cells based on markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Zero out first row if needed
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

        // Zero out first column if needed
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set zeroes based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # handle first row and column
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

## Python3

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

## C

```c
void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0 || matrixColSize == NULL) return;
    int m = matrixSize;
    int n = matrixColSize[0];
    
    int firstRowZero = 0, firstColZero = 0;
    // check first row
    for (int j = 0; j < n; ++j) {
        if (matrix[0][j] == 0) {
            firstRowZero = 1;
            break;
        }
    }
    // check first column
    for (int i = 0; i < m; ++i) {
        if (matrix[i][0] == 0) {
            firstColZero = 1;
            break;
        }
    }
    // use first row and column as markers
    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    // set zeros based on markers
    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }
    // handle first row
    if (firstRowZero) {
        for (int j = 0; j < n; ++j) {
            matrix[0][j] = 0;
        }
    }
    // handle first column
    if (firstColZero) {
        for (int i = 0; i < m; ++i) {
            matrix[i][0] = 0;
        }
    }
}
```

## Csharp

```csharp
public class Solution {
    public void SetZeroes(int[][] matrix) {
        if (matrix == null || matrix.Length == 0) return;
        int m = matrix.Length;
        int n = matrix[0].Length;

        bool firstRowZero = false, firstColZero = false;

        // Check first row for zero
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }
        }

        // Check first column for zero
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }

        // Use first row and column as markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Zero out cells based on markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Zero first row if needed
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

        // Zero first column if needed
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    
    let firstRowZero = false;
    for (let j = 0; j < n; j++) {
        if (matrix[0][j] === 0) {
            firstRowZero = true;
            break;
        }
    }
    
    let firstColZero = false;
    for (let i = 0; i < m; i++) {
        if (matrix[i][0] === 0) {
            firstColZero = true;
            break;
        }
    }
    
    // Use first row and column as markers
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    
    // Zero out cells based on markers
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (matrix[i][0] === 0 || matrix[0][j] === 0) {
                matrix[i][j] = 0;
            }
        }
    }
    
    // Zero out first row if needed
    if (firstRowZero) {
        for (let j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }
    
    // Zero out first column if needed
    if (firstColZero) {
        for (let i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
};
```

## Typescript

```typescript
/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    const m = matrix.length;
    if (m === 0) return;
    const n = matrix[0].length;

    let firstRowZero = false;
    for (let j = 0; j < n; j++) {
        if (matrix[0][j] === 0) {
            firstRowZero = true;
            break;
        }
    }

    let firstColZero = false;
    for (let i = 0; i < m; i++) {
        if (matrix[i][0] === 0) {
            firstColZero = true;
            break;
        }
    }

    // Use first row and column as markers
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // Zero out cells based on markers
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (matrix[i][0] === 0 || matrix[0][j] === 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero first row if needed
    if (firstRowZero) {
        for (let j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Zero first column if needed
    if (firstColZero) {
        for (let i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function setZeroes(&$matrix) {
        $m = count($matrix);
        if ($m == 0) {
            return;
        }
        $n = count($matrix[0]);

        // Check if first row has a zero
        $firstRowZero = false;
        for ($j = 0; $j < $n; $j++) {
            if ($matrix[0][$j] === 0) {
                $firstRowZero = true;
                break;
            }
        }

        // Check if first column has a zero
        $firstColZero = false;
        for ($i = 0; $i < $m; $i++) {
            if ($matrix[$i][0] === 0) {
                $firstColZero = true;
                break;
            }
        }

        // Use first row and column as markers
        for ($i = 1; $i < $m; $i++) {
            for ($j = 1; $j < $n; $j++) {
                if ($matrix[$i][$j] === 0) {
                    $matrix[$i][0] = 0;
                    $matrix[0][$j] = 0;
                }
            }
        }

        // Zero rows based on markers
        for ($i = 1; $i < $m; $i++) {
            if ($matrix[$i][0] === 0) {
                for ($j = 1; $j < $n; $j++) {
                    $matrix[$i][$j] = 0;
                }
            }
        }

        // Zero columns based on markers
        for ($j = 1; $j < $n; $j++) {
            if ($matrix[0][$j] === 0) {
                for ($i = 1; $i < $m; $i++) {
                    $matrix[$i][$j] = 0;
                }
            }
        }

        // Zero first row if needed
        if ($firstRowZero) {
            for ($j = 0; $j < $n; $j++) {
                $matrix[0][$j] = 0;
            }
        }

        // Zero first column if needed
        if ($firstColZero) {
            for ($i = 0; $i < $m; $i++) {
                $matrix[$i][0] = 0;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func setZeroes(_ matrix: inout [[Int]]) {
        let m = matrix.count
        let n = matrix[0].count
        var firstRowZero = false
        var firstColZero = false
        
        // Check if first row has a zero
        for j in 0..<n {
            if matrix[0][j] == 0 {
                firstRowZero = true
                break
            }
        }
        // Check if first column has a zero
        for i in 0..<m {
            if matrix[i][0] == 0 {
                firstColZero = true
                break
            }
        }
        
        // Use first row and column as markers
        if m > 1 && n > 1 {
            for i in 1..<m {
                for j in 1..<n {
                    if matrix[i][j] == 0 {
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    }
                }
            }
            
            // Zero out cells based on markers
            for i in 1..<m {
                for j in 1..<n {
                    if matrix[i][0] == 0 || matrix[0][j] == 0 {
                        matrix[i][j] = 0
                    }
                }
            }
        }
        
        // Zero first row if needed
        if firstRowZero {
            for j in 0..<n {
                matrix[0][j] = 0
            }
        }
        // Zero first column if needed
        if firstColZero {
            for i in 0..<m {
                matrix[i][0] = 0
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun setZeroes(matrix: Array<IntArray>) {
        val m = matrix.size
        if (m == 0) return
        val n = matrix[0].size

        var firstRowZero = false
        var firstColZero = false

        for (j in 0 until n) {
            if (matrix[0][j] == 0) {
                firstRowZero = true
                break
            }
        }

        for (i in 0 until m) {
            if (matrix[i][0] == 0) {
                firstColZero = true
                break
            }
        }

        for (i in 1 until m) {
            for (j in 1 until n) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                }
            }
        }

        for (i in 1 until m) {
            if (matrix[i][0] == 0) {
                for (j in 1 until n) {
                    matrix[i][j] = 0
                }
            }
        }

        for (j in 1 until n) {
            if (matrix[0][j] == 0) {
                for (i in 1 until m) {
                    matrix[i][j] = 0
                }
            }
        }

        if (firstRowZero) {
            for (j in 0 until n) {
                matrix[0][j] = 0
            }
        }

        if (firstColZero) {
            for (i in 0 until m) {
                matrix[i][0] = 0
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  void setZeroes(List<List<int>> matrix) {
    int m = matrix.length;
    int n = matrix[0].length;

    bool firstRowZero = false;
    for (int j = 0; j < n; j++) {
      if (matrix[0][j] == 0) {
        firstRowZero = true;
        break;
      }
    }

    bool firstColZero = false;
    for (int i = 0; i < m; i++) {
      if (matrix[i][0] == 0) {
        firstColZero = true;
        break;
      }
    }

    // Use first row and column as markers
    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        if (matrix[i][j] == 0) {
          matrix[i][0] = 0;
          matrix[0][j] = 0;
        }
      }
    }

    // Zero rows based on markers
    for (int i = 1; i < m; i++) {
      if (matrix[i][0] == 0) {
        for (int j = 1; j < n; j++) {
          matrix[i][j] = 0;
        }
      }
    }

    // Zero columns based on markers
    for (int j = 1; j < n; j++) {
      if (matrix[0][j] == 0) {
        for (int i = 1; i < m; i++) {
          matrix[i][j] = 0;
        }
      }
    }

    // Zero first row if needed
    if (firstRowZero) {
      for (int j = 0; j < n; j++) {
        matrix[0][j] = 0;
      }
    }

    // Zero first column if needed
    if (firstColZero) {
      for (int i = 0; i < m; i++) {
        matrix[i][0] = 0;
      }
    }
  }
}
```

## Golang

```go
func setZeroes(matrix [][]int) {
    m := len(matrix)
    if m == 0 {
        return
    }
    n := len(matrix[0])

    firstRowZero, firstColZero := false, false

    // Check first row for zero
    for j := 0; j < n; j++ {
        if matrix[0][j] == 0 {
            firstRowZero = true
            break
        }
    }

    // Check first column for zero
    for i := 0; i < m; i++ {
        if matrix[i][0] == 0 {
            firstColZero = true
            break
        }
    }

    // Use first row and column as markers
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            if matrix[i][j] == 0 {
                matrix[i][0] = 0
                matrix[0][j] = 0
            }
        }
    }

    // Set zeros based on markers, iterating from bottom-right to avoid overwriting markers prematurely
    for i := m - 1; i >= 1; i-- {
        for j := n - 1; j >= 1; j-- {
            if matrix[i][0] == 0 || matrix[0][j] == 0 {
                matrix[i][j] = 0
            }
        }
    }

    // Zero first row if needed
    if firstRowZero {
        for j := 0; j < n; j++ {
            matrix[0][j] = 0
        }
    }

    // Zero first column if needed
    if firstColZero {
        for i := 0; i < m; i++ {
            matrix[i][0] = 0
        }
    }
}
```

## Ruby

```ruby
def set_zeroes(matrix)
  return if matrix.empty?
  rows = matrix.size
  cols = matrix[0].size

  first_row_has_zero = false
  first_col_has_zero = false

  (0...cols).each do |j|
    if matrix[0][j] == 0
      first_row_has_zero = true
      break
    end
  end

  (0...rows).each do |i|
    if matrix[i][0] == 0
      first_col_has_zero = true
      break
    end
  end

  (1...rows).each do |i|
    (1...cols).each do |j|
      if matrix[i][j] == 0
        matrix[i][0] = 0
        matrix[0][j] = 0
      end
    end
  end

  (1...rows).each do |i|
    (1...cols).each do |j|
      if matrix[i][0] == 0 || matrix[0][j] == 0
        matrix[i][j] = 0
      end
    end
  end

  if first_row_has_zero
    (0...cols).each { |j| matrix[0][j] = 0 }
  end

  if first_col_has_zero
    (0...rows).each { |i| matrix[i][0] = 0 }
  end
end
```

## Scala

```scala
object Solution {
    def setZeroes(matrix: Array[Array[Int]]): Unit = {
        val m = matrix.length
        if (m == 0) return
        val n = matrix(0).length

        var firstRowZero = false
        var firstColZero = false

        // Check first row for zero
        var j = 0
        while (j < n) {
            if (matrix(0)(j) == 0) {
                firstRowZero = true
            }
            j += 1
        }

        // Check first column for zero
        var i = 0
        while (i < m) {
            if (matrix(i)(0) == 0) {
                firstColZero = true
            }
            i += 1
        }

        // Use first row and column as markers
        i = 1
        while (i < m) {
            j = 1
            while (j < n) {
                if (matrix(i)(j) == 0) {
                    matrix(i)(0) = 0
                    matrix(0)(j) = 0
                }
                j += 1
            }
            i += 1
        }

        // Zero rows based on markers
        i = 1
        while (i < m) {
            if (matrix(i)(0) == 0) {
                j = 1
                while (j < n) {
                    matrix(i)(j) = 0
                    j += 1
                }
            }
            i += 1
        }

        // Zero columns based on markers
        j = 1
        while (j < n) {
            if (matrix(0)(j) == 0) {
                i = 1
                while (i < m) {
                    matrix(i)(j) = 0
                    i += 1
                }
            }
            j += 1
        }

        // Zero first row if needed
        if (firstRowZero) {
            j = 0
            while (j < n) {
                matrix(0)(j) = 0
                j += 1
            }
        }

        // Zero first column if needed
        if (firstColZero) {
            i = 0
            while (i < m) {
                matrix(i)(0) = 0
                i += 1
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let m = matrix.len();
        if m == 0 {
            return;
        }
        let n = matrix[0].len();

        // Check if first row has a zero
        let mut first_row_has_zero = false;
        for j in 0..n {
            if matrix[0][j] == 0 {
                first_row_has_zero = true;
                break;
            }
        }

        // Check if first column has a zero
        let mut first_col_has_zero = false;
        for i in 0..m {
            if matrix[i][0] == 0 {
                first_col_has_zero = true;
                break;
            }
        }

        // Use first row and column as markers
        for i in 1..m {
            for j in 1..n {
                if matrix[i][j] == 0 {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Zero rows based on markers in first column
        for i in 1..m {
            if matrix[i][0] == 0 {
                for j in 1..n {
                    matrix[i][j] = 0;
                }
            }
        }

        // Zero columns based on markers in first row
        for j in 1..n {
            if matrix[0][j] == 0 {
                for i in 1..m {
                    matrix[i][j] = 0;
                }
            }
        }

        // Zero the first row if needed
        if first_row_has_zero {
            for j in 0..n {
                matrix[0][j] = 0;
            }
        }

        // Zero the first column if needed
        if first_col_has_zero {
            for i in 0..m {
                matrix[i][0] = 0;
            }
        }
    }
}
```

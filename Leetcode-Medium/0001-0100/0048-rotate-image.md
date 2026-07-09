# 0048. Rotate Image

## Cpp

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        // Transpose the matrix
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        // Reverse each row
        for (int i = 0; i < n; ++i) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
```

## Java

```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        // Transpose the matrix
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        // Reverse each row
        for (int i = 0; i < n; i++) {
            int left = 0, right = n - 1;
            while (left < right) {
                int tmp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = tmp;
                left++;
                right--;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()
```

## Python3

```python
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()
```

## C

```c
void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int n = matrixSize;
    for (int layer = 0; layer < n / 2; ++layer) {
        int first = layer;
        int last = n - 1 - layer;
        for (int i = first; i < last; ++i) {
            int offset = i - first;
            int top = matrix[first][i];
            // left -> top
            matrix[first][i] = matrix[last - offset][first];
            // bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset];
            // right -> bottom
            matrix[last][last - offset] = matrix[i][last];
            // top -> right
            matrix[i][last] = top;
        }
    }
}
```

## Csharp

```csharp
public class Solution
{
    public void Rotate(int[][] matrix)
    {
        int n = matrix.Length;
        // Transpose the matrix
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Reverse each row
        for (int i = 0; i < n; i++)
        {
            int left = 0, right = n - 1;
            while (left < right)
            {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left++;
                right--;
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
var rotate = function(matrix) {
    const n = matrix.length;
    // Transpose the matrix
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }
    // Reverse each row
    for (let i = 0; i < n; i++) {
        let left = 0, right = n - 1;
        while (left < right) {
            [matrix[i][left], matrix[i][right]] = [matrix[i][right], matrix[i][left]];
            left++;
            right--;
        }
    }
};
```

## Typescript

```typescript
/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    const n = matrix.length;
    // Transpose the matrix
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }
    // Reverse each row
    for (let i = 0; i < n; i++) {
        let left = 0, right = n - 1;
        while (left < right) {
            [matrix[i][left], matrix[i][right]] = [matrix[i][right], matrix[i][left]];
            left++;
            right--;
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
    function rotate(&$matrix) {
        $n = count($matrix);
        // Transpose the matrix
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $tmp = $matrix[$i][$j];
                $matrix[$i][$j] = $matrix[$j][$i];
                $matrix[$j][$i] = $tmp;
            }
        }
        // Reverse each row
        for ($i = 0; $i < $n; $i++) {
            $left = 0;
            $right = $n - 1;
            while ($left < $right) {
                $tmp = $matrix[$i][$left];
                $matrix[$i][$left] = $matrix[$i][$right];
                $matrix[$i][$right] = $tmp;
                $left++;
                $right--;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let n = matrix.count
        // Transpose the matrix
        for i in 0..<n {
            for j in (i + 1)..<n {
                let temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }
        // Reverse each row
        for i in 0..<n {
            var left = 0
            var right = n - 1
            while left < right {
                let temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rotate(matrix: Array<IntArray>) {
        val n = matrix.size
        // Transpose the matrix
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
            }
        }
        // Reverse each row
        for (i in 0 until n) {
            var left = 0
            var right = n - 1
            while (left < right) {
                val tmp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = tmp
                left++
                right--
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  void rotate(List<List<int>> matrix) {
    int n = matrix.length;
    // Transpose the matrix
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
      }
    }
    // Reverse each row
    for (int i = 0; i < n; i++) {
      int left = 0, right = n - 1;
      while (left < right) {
        int temp = matrix[i][left];
        matrix[i][left] = matrix[i][right];
        matrix[i][right] = temp;
        left++;
        right--;
      }
    }
  }
}
```

## Golang

```go
func rotate(matrix [][]int) {
    n := len(matrix)
    // Transpose the matrix
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        }
    }
    // Reverse each row
    for i := 0; i < n; i++ {
        for l, r := 0, n-1; l < r; {
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l++
            r--
        }
    }
}
```

## Ruby

```ruby
def rotate(matrix)
  n = matrix.size
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    end
  end
  matrix.each { |row| row.reverse! }
end
```

## Scala

```scala
object Solution {
    def rotate(matrix: Array[Array[Int]]): Unit = {
        val n = matrix.length
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n) {
                val tmp = matrix(i)(j)
                matrix(i)(j) = matrix(j)(i)
                matrix(j)(i) = tmp
                j += 1
            }
            i += 1
        }
        var r = 0
        while (r < n) {
            var left = 0
            var right = n - 1
            while (left < right) {
                val tmp = matrix(r)(left)
                matrix(r)(left) = matrix(r)(right)
                matrix(r)(right) = tmp
                left += 1
                right -= 1
            }
            r += 1
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        for i in 0..n {
            for j in (i + 1)..n {
                let ptr1 = &mut matrix[i][j] as *mut i32;
                let ptr2 = &mut matrix[j][i] as *mut i32;
                unsafe { std::ptr::swap(ptr1, ptr2); }
            }
        }
        for row in matrix.iter_mut() {
            row.reverse();
        }
    }
}
```

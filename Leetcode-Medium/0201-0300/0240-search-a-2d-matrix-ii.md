# 0240. Search a 2D Matrix II

## Cpp

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        int m = matrix.size();
        int n = matrix[0].size();
        int row = 0, col = n - 1;
        while (row < m && col >= 0) {
            int val = matrix[row][col];
            if (val == target) return true;
            else if (val > target) --col;
            else ++row;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        int rows = matrix.length;
        int cols = matrix[0].length;
        int r = 0, c = cols - 1;
        while (r < rows && c >= 0) {
            int val = matrix[r][c];
            if (val == target) {
                return true;
            } else if (val > target) {
                c--;
            } else {
                r++;
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
        row, col = 0, n - 1
        while row < m and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1
        return False
```

## Python3

```python
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1
        while r < rows and c >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                c -= 1
            else:
                r += 1
        return False
```

## C

```c
#include <stdbool.h>

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    if (matrixSize == 0 || matrixColSize == NULL) return false;
    int rows = matrixSize;
    int cols = matrixColSize[0];
    if (cols == 0) return false;

    int r = 0;
    int c = cols - 1;
    while (r < rows && c >= 0) {
        int val = matrix[r][c];
        if (val == target) return true;
        else if (val > target) c--;
        else r++;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0)
            return false;
        
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int r = 0;
        int c = cols - 1;
        
        while (r < rows && c >= 0) {
            int val = matrix[r][c];
            if (val == target)
                return true;
            else if (val > target)
                c--;
            else
                r++;
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
    let rows = matrix.length;
    let cols = matrix[0].length;
    // start from top-right corner
    let r = 0, c = cols - 1;
    while (r < rows && c >= 0) {
        const val = matrix[r][c];
        if (val === target) return true;
        if (val > target) {
            c--;
        } else {
            r++;
        }
    }
    return false;
};
```

## Typescript

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return false;
    let rows = matrix.length;
    let cols = matrix[0].length;
    let r = 0;
    let c = cols - 1;
    while (r < rows && c >= 0) {
        const val = matrix[r][c];
        if (val === target) return true;
        if (val > target) {
            c--;
        } else {
            r++;
        }
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
        $rows = count($matrix);
        if ($rows === 0) {
            return false;
        }
        $cols = count($matrix[0]);
        $r = 0;
        $c = $cols - 1;

        while ($r < $rows && $c >= 0) {
            $val = $matrix[$r][$c];
            if ($val === $target) {
                return true;
            } elseif ($val > $target) {
                $c--;
            } else {
                $r++;
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
        var row = 0
        var col = matrix[0].count - 1
        
        while row < matrix.count && col >= 0 {
            let value = matrix[row][col]
            if value == target {
                return true
            } else if value > target {
                col -= 1
            } else {
                row += 1
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
        if (matrix.isEmpty() || matrix[0].isEmpty()) return false
        var row = 0
        var col = matrix[0].size - 1
        while (row < matrix.size && col >= 0) {
            val value = matrix[row][col]
            when {
                value == target -> return true
                value > target -> col--
                else -> row++
            }
        }
        return false
    }
}
```

## Golang

```go
func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	rows, cols := len(matrix), len(matrix[0])
	r, c := 0, cols-1
	for r < rows && c >= 0 {
		val := matrix[r][c]
		if val == target {
			return true
		} else if val > target {
			c--
		} else {
			r++
		}
	}
	return false
}
```

## Ruby

```ruby
def search_matrix(matrix, target)
  return false if matrix.nil? || matrix.empty? || matrix[0].empty?
  rows = matrix.size
  cols = matrix[0].size
  r = 0
  c = cols - 1
  while r < rows && c >= 0
    val = matrix[r][c]
    return true if val == target
    if val > target
      c -= 1
    else
      r += 1
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def searchMatrix(matrix: Array[Array[Int]], target: Int): Boolean = {
        if (matrix.isEmpty || matrix.head.isEmpty) return false
        var row = 0
        var col = matrix(0).length - 1
        while (row < matrix.length && col >= 0) {
            val value = matrix(row)(col)
            if (value == target) return true
            else if (value > target) col -= 1
            else row += 1
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
        let mut i: usize = 0;
        let mut j: i32 = n as i32 - 1;
        while i < m && j >= 0 {
            let val = matrix[i][j as usize];
            if val == target {
                return true;
            } else if val > target {
                j -= 1;
            } else {
                i += 1;
            }
        }
        false
    }
}
```

# 1139. Largest 1-Bordered Square

## Cpp

```cpp
class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        vector<vector<int>> horiz(m, vector<int>(n, 0));
        vector<vector<int>> vert(m, vector<int>(n, 0));
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    horiz[i][j] = (j > 0 ? horiz[i][j - 1] : 0) + 1;
                    vert[i][j] = (i > 0 ? vert[i - 1][j] : 0) + 1;
                }
            }
        }
        
        int maxLen = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    int possible = min(horiz[i][j], vert[i][j]);
                    while (possible > maxLen) {
                        int ii = i - possible + 1;
                        int jj = j - possible + 1;
                        if (horiz[ii][j] >= possible && vert[i][jj] >= possible) {
                            maxLen = possible;
                            break;
                        }
                        --possible;
                    }
                }
            }
        }
        return maxLen * maxLen;
    }
};
```

## Java

```java
class Solution {
    public int largest1BorderedSquare(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] horiz = new int[m][n];
        int[][] vert = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    horiz[i][j] = (j > 0 ? horiz[i][j - 1] : 0) + 1;
                    vert[i][j] = (i > 0 ? vert[i - 1][j] : 0) + 1;
                }
            }
        }
        int maxLen = 0;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int possible = Math.min(horiz[i][j], vert[i][j]);
                while (possible > maxLen) {
                    if (horiz[i - possible + 1][j] >= possible && vert[i][j - possible + 1] >= possible) {
                        maxLen = possible;
                        break;
                    }
                    possible--;
                }
            }
        }
        return maxLen * maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # fill DP tables from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = 1 + (right[i][j + 1] if j + 1 < n else 0)
                    down[i][j] = 1 + (down[i + 1][j] if i + 1 < m else 0)

        max_side = 0
        for i in range(m):
            for j in range(n):
                # possible maximum side length from this top-left corner
                limit = min(right[i][j], down[i][j])
                while limit > max_side:
                    # check bottom border and right border
                    if right[i + limit - 1][j] >= limit and down[i][j + limit - 1] >= limit:
                        max_side = limit
                        break
                    limit -= 1

        return max_side * max_side
```

## Python3

```python
from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # Precompute consecutive 1s to the right and downward
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = 1 + (right[i][j + 1] if j + 1 < n else 0)
                    down[i][j] = 1 + (down[i + 1][j] if i + 1 < m else 0)

        max_side = 0
        for i in range(m):
            for j in range(n):
                # maximum possible side length with top‑left corner at (i, j)
                limit = min(right[i][j], down[i][j])
                while limit > max_side:
                    if right[i + limit - 1][j] >= limit and down[i][j + limit - 1] >= limit:
                        max_side = limit
                        break
                    limit -= 1

        return max_side * max_side
```

## C

```c
#include <stdlib.h>

int largest1BorderedSquare(int** grid, int gridSize, int* gridColSize){
    if (gridSize == 0) return 0;
    int rows = gridSize;
    int cols = gridColSize[0];
    
    // Allocate DP arrays
    int **right = (int**)malloc(rows * sizeof(int*));
    int **down  = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; ++i) {
        right[i] = (int*)calloc(cols, sizeof(int));
        down[i]  = (int*)calloc(cols, sizeof(int));
    }
    
    // Fill DP arrays: number of consecutive 1's to the right and downwards
    for (int i = rows - 1; i >= 0; --i) {
        for (int j = cols - 1; j >= 0; --j) {
            if (grid[i][j] == 1) {
                right[i][j] = 1 + (j + 1 < cols ? right[i][j + 1] : 0);
                down[i][j]  = 1 + (i + 1 < rows ? down[i + 1][j] : 0);
            } else {
                right[i][j] = down[i][j] = 0;
            }
        }
    }
    
    int maxLen = 0;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            // The maximum possible side length from this top‑left corner
            int limit = right[i][j];
            if (down[i][j] < limit) limit = down[i][j];
            
            for (int len = limit; len > maxLen; --len) {
                int i2 = i + len - 1;
                int j2 = j + len - 1;
                if (i2 >= rows || j2 >= cols) continue;
                
                // Check bottom border and right border
                if (right[i2][j] >= len && down[i][j2] >= len) {
                    maxLen = len;
                    break; // larger lengths for this cell are impossible now
                }
            }
        }
    }
    
    // Free DP arrays
    for (int i = 0; i < rows; ++i) {
        free(right[i]);
        free(down[i]);
    }
    free(right);
    free(down);
    
    return maxLen * maxLen;
}
```

## Csharp

```csharp
public class Solution {
    public int Largest1BorderedSquare(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[,] right = new int[m, n];
        int[,] down = new int[m, n];

        // Precompute consecutive ones to the right and down
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 1) {
                    right[i, j] = 1 + (j + 1 < n ? right[i, j + 1] : 0);
                    down[i, j] = 1 + (i + 1 < m ? down[i + 1, j] : 0);
                }
            }
        }

        int maxSide = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // maximum possible side length from (i,j)
                int maxPossible = Math.Min(m - i, n - j);
                for (int len = maxPossible; len > maxSide; len--) {
                    if (right[i, j] >= len &&
                        down[i, j] >= len &&
                        right[i + len - 1, j] >= len &&
                        down[i, j + len - 1] >= len) {
                        maxSide = len;
                        break; // no need to check smaller lengths for this (i,j)
                    }
                }
            }
        }

        return maxSide * maxSide;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var largest1BorderedSquare = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const right = Array.from({ length: m }, () => Array(n).fill(0));
    const down = Array.from({ length: m }, () => Array(n).fill(0));

    // Precompute consecutive 1s to the right and down for each cell
    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (grid[i][j] === 1) {
                right[i][j] = (j + 1 < n ? right[i][j + 1] : 0) + 1;
                down[i][j] = (i + 1 < m ? down[i + 1][j] : 0) + 1;
            }
        }
    }

    let maxSide = 0;

    // Try each cell as the top-left corner of a square
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            // The maximum possible side length from this cell
            let limit = Math.min(right[i][j], down[i][j]);
            // Check larger lengths first to allow early break
            for (let len = limit; len > maxSide; len--) {
                // Verify bottom border and right border have enough 1s
                if (right[i + len - 1][j] >= len && down[i][j + len - 1] >= len) {
                    maxSide = len;
                    break; // No need to check smaller lengths for this cell
                }
            }
        }
    }

    return maxSide * maxSide;
};
```

## Typescript

```typescript
function largest1BorderedSquare(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const horiz: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));
    const vert: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                horiz[i][j] = (j > 0 ? horiz[i][j - 1] : 0) + 1;
                vert[i][j] = (i > 0 ? vert[i - 1][j] : 0) + 1;
            }
        }
    }

    let maxSide = 0;

    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            const limit = Math.min(horiz[i][j], vert[i][j]);
            for (let len = limit; len > maxSide; len--) {
                if (
                    horiz[i - len + 1][j] >= len &&
                    vert[i][j - len + 1] >= len
                ) {
                    maxSide = len;
                    break;
                }
            }
        }
    }

    return maxSide * maxSide;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largest1BorderedSquare($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        // DP arrays for consecutive ones to the right and downwards
        $right = array_fill(0, $m, array_fill(0, $n, 0));
        $down  = array_fill(0, $m, array_fill(0, $n, 0));

        for ($i = $m - 1; $i >= 0; --$i) {
            for ($j = $n - 1; $j >= 0; --$j) {
                if ($grid[$i][$j] == 1) {
                    $right[$i][$j] = 1 + ($j + 1 < $n ? $right[$i][$j + 1] : 0);
                    $down[$i][$j]  = 1 + ($i + 1 < $m ? $down[$i + 1][$j] : 0);
                } else {
                    $right[$i][$j] = 0;
                    $down[$i][$j]  = 0;
                }
            }
        }

        $maxSide = min($m, $n);
        for ($len = $maxSide; $len > 0; --$len) {
            for ($i = 0; $i <= $m - $len; ++$i) {
                for ($j = 0; $j <= $n - $len; ++$j) {
                    if (
                        $right[$i][$j] >= $len &&
                        $down[$i][$j] >= $len &&
                        $right[$i + $len - 1][$j] >= $len &&
                        $down[$i][$j + $len - 1] >= $len
                    ) {
                        return $len * $len;
                    }
                }
            }
        }

        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func largest1BorderedSquare(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var right = Array(repeating: Array(repeating: 0, count: n), count: m)
        var down = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        for i in stride(from: m - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                if grid[i][j] == 1 {
                    right[i][j] = 1 + (j + 1 < n ? right[i][j + 1] : 0)
                    down[i][j] = 1 + (i + 1 < m ? down[i + 1][j] : 0)
                }
            }
        }
        
        var maxLen = 0
        for i in 0..<m {
            for j in 0..<n {
                let possible = min(right[i][j], down[i][j])
                if possible <= maxLen { continue }
                var len = possible
                while len > maxLen {
                    if right[i + len - 1][j] >= len && down[i][j + len - 1] >= len {
                        maxLen = len
                        break
                    }
                    len -= 1
                }
            }
        }
        return maxLen * maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largest1BorderedSquare(grid: Array<IntArray>): Int {
        val m = grid.size
        if (m == 0) return 0
        val n = grid[0].size
        val right = Array(m) { IntArray(n) }
        val down = Array(m) { IntArray(n) }

        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (grid[i][j] == 1) {
                    right[i][j] = 1 + if (j + 1 < n) right[i][j + 1] else 0
                    down[i][j] = 1 + if (i + 1 < m) down[i + 1][j] else 0
                }
            }
        }

        var maxLen = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                val possible = kotlin.math.min(right[i][j], down[i][j])
                var len = possible
                while (len > maxLen) {
                    if (right[i + len - 1][j] >= len && down[i][j + len - 1] >= len) {
                        maxLen = len
                        break
                    }
                    len--
                }
            }
        }
        return maxLen * maxLen
    }
}
```

## Golang

```go
func largest1BorderedSquare(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])
    right := make([][]int, m)
    down := make([][]int, m)
    for i := 0; i < m; i++ {
        right[i] = make([]int, n)
        down[i] = make([]int, n)
    }

    // Precompute consecutive ones to the right and down
    for i := m - 1; i >= 0; i-- {
        for j := n - 1; j >= 0; j-- {
            if grid[i][j] == 1 {
                if j+1 < n {
                    right[i][j] = right[i][j+1] + 1
                } else {
                    right[i][j] = 1
                }
                if i+1 < m {
                    down[i][j] = down[i+1][j] + 1
                } else {
                    down[i][j] = 1
                }
            }
        }
    }

    maxLen := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            // maximum possible side length with top-left corner at (i,j)
            limit := right[i][j]
            if down[i][j] < limit {
                limit = down[i][j]
            }
            for l := limit; l > maxLen; l-- {
                // check bottom border and right border
                if right[i+l-1][j] >= l && down[i][j+l-1] >= l {
                    maxLen = l
                    break
                }
            }
        }
    }

    return maxLen * maxLen
}
```

## Ruby

```ruby
def largest1_bordered_square(grid)
  rows = grid.size
  cols = grid[0].size
  horiz = Array.new(rows) { Array.new(cols, 0) }
  vert = Array.new(rows) { Array.new(cols, 0) }

  (0...rows).each do |i|
    (0...cols).each do |j|
      if grid[i][j] == 1
        horiz[i][j] = (j > 0 ? horiz[i][j - 1] : 0) + 1
        vert[i][j] = (i > 0 ? vert[i - 1][j] : 0) + 1
      end
    end
  end

  max_side = 0
  (0...rows).each do |i|
    (0...cols).each do |j|
      next if grid[i][j] == 0
      limit = [horiz[i][j], vert[i][j]].min
      while limit > max_side
        top_i = i - limit + 1
        left_j = j - limit + 1
        break if top_i < 0 || left_j < 0
        if horiz[top_i][j] >= limit && vert[i][left_j] >= limit
          max_side = limit
          break
        end
        limit -= 1
      end
    end
  end

  max_side * max_side
end
```

## Scala

```scala
object Solution {
    def largest1BorderedSquare(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        val horiz = Array.ofDim[Int](m, n)
        val vert = Array.ofDim[Int](m, n)

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (grid(i)(j) == 1) {
                    horiz(i)(j) = (if (j > 0) horiz(i)(j - 1) else 0) + 1
                    vert(i)(j) = (if (i > 0) vert(i - 1)(j) else 0) + 1
                } // else defaults to 0
            }
        }

        var maxSide = 0

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                var side = Math.min(horiz(i)(j), vert(i)(j))
                while (side > maxSide) {
                    if (horiz(i - side + 1)(j) >= side && vert(i)(j - side + 1) >= side) {
                        maxSide = side
                    }
                    side -= 1
                }
            }
        }

        maxSide * maxSide
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest1_bordered_square(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut right = vec![vec![0usize; n]; m];
        let mut down = vec![vec![0usize; n]; m];

        // Precompute consecutive 1's to the right and down from each cell
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                if grid[i][j] == 1 {
                    right[i][j] = 1 + if j + 1 < n { right[i][j + 1] } else { 0 };
                    down[i][j] = 1 + if i + 1 < m { down[i + 1][j] } else { 0 };
                }
            }
        }

        let mut max_len = 0usize;

        for i in 0..m {
            for j in 0..n {
                // maximum possible side length with top-left corner at (i, j)
                let limit = std::cmp::min(right[i][j], down[i][j]);
                let mut len = limit;
                while len > max_len {
                    // Check bottom border and right border
                    if right[i + len - 1][j] >= len && down[i][j + len - 1] >= len {
                        max_len = len;
                        break;
                    }
                    len -= 1;
                }
            }
        }

        (max_len * max_len) as i32
    }
}
```

# 0840. Magic Squares In Grid

## Cpp

```cpp
class Solution {
public:
    bool isMagic(const vector<vector<int>>& g, int r, int c) {
        // center must be 5
        if (g[r+1][c+1] != 5) return false;
        bool seen[10] = {false};
        for (int i = r; i < r + 3; ++i) {
            for (int j = c; j < c + 3; ++j) {
                int val = g[i][j];
                if (val < 1 || val > 9 || seen[val]) return false;
                seen[val] = true;
            }
        }
        // all rows, columns and diagonals must sum to 15
        int s = 15;
        for (int i = 0; i < 3; ++i) {
            if (g[r+i][c] + g[r+i][c+1] + g[r+i][c+2] != s) return false;
            if (g[r][c+i] + g[r+1][c+i] + g[r+2][c+i] != s) return false;
        }
        if (g[r][c] + g[r+1][c+1] + g[r+2][c+2] != s) return false;
        if (g[r][c+2] + g[r+1][c+1] + g[r+2][c] != s) return false;
        return true;
    }
    
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if (m < 3 || n < 3) return 0;
        int ans = 0;
        for (int i = 0; i <= m - 3; ++i) {
            for (int j = 0; j <= n - 3; ++j) {
                if (isMagic(grid, i, j)) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        for (int i = 0; i <= m - 3; i++) {
            for (int j = 0; j <= n - 3; j++) {
                if (isMagic(grid, i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    private boolean isMagic(int[][] g, int r, int c) {
        // Center must be 5
        if (g[r + 1][c + 1] != 5) {
            return false;
        }
        int[] seen = new int[10];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int val = g[r + i][c + j];
                if (val < 1 || val > 9) {
                    return false;
                }
                if (seen[val]++ != 0) {
                    return false;
                }
            }
        }
        int a = g[r][c], b = g[r][c + 1], d = g[r][c + 2];
        int e = g[r + 1][c], f = g[r + 1][c + 1], h = g[r + 1][c + 2];
        int i1 = g[r + 2][c], j = g[r + 2][c + 1], k = g[r + 2][c + 2];

        int sum = a + b + d;
        if (e + f + h != sum) return false;
        if (i1 + j + k != sum) return false;
        if (a + e + i1 != sum) return false;
        if (b + f + j != sum) return false;
        if (d + h + k != sum) return false;
        if (a + f + k != sum) return false;
        if (d + f + i1 != sum) return false;

        return true;
    }
}
```

## Python

```python
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        count = 0

        def is_magic(r, c):
            # center must be 5
            if grid[r + 1][c + 1] != 5:
                return False
            seen = [False] * 10
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9 or seen[val]:
                        return False
                    seen[val] = True
            # all rows, columns and diagonals must sum to 15
            target = 15
            for i in range(3):
                if grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2] != target:
                    return False
                if grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] != target:
                    return False
            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != target:
                return False
            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != target:
                return False
            return True

        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic(i, j):
                    count += 1
        return count
```

## Python3

```python
class Solution:
    def numMagicSquaresInside(self, grid):
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0

        def is_magic(r, c):
            # center must be 5
            if grid[r + 1][c + 1] != 5:
                return False
            vals = []
            for i in range(3):
                for j in range(3):
                    v = grid[r + i][c + j]
                    if v < 1 or v > 9:
                        return False
                    vals.append(v)
            if len(set(vals)) != 9:
                return False

            target = 15
            # rows and columns
            for k in range(3):
                if sum(grid[r + k][c:c + 3]) != target:
                    return False
                if grid[r][c + k] + grid[r + 1][c + k] + grid[r + 2][c + k] != target:
                    return False
            # diagonals
            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != target:
                return False
            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != target:
                return False
            return True

        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic(i, j):
                    count += 1
        return count
```

## C

```c
#include <stdbool.h>

int numMagicSquaresInside(int** grid, int gridSize, int* gridColSize) {
    int count = 0;
    if (gridSize < 3) return 0;
    for (int i = 0; i + 2 < gridSize; ++i) {
        int cols = gridColSize[i];
        if (cols < 3) continue;
        for (int j = 0; j + 2 < cols; ++j) {
            /* center must be 5 */
            if (grid[i + 1][j + 1] != 5) continue;

            bool ok = true;
            int seen[10] = {0};

            /* check distinct numbers from 1 to 9 */
            for (int r = 0; r < 3 && ok; ++r) {
                for (int c = 0; c < 3; ++c) {
                    int val = grid[i + r][j + c];
                    if (val < 1 || val > 9 || seen[val]) {
                        ok = false;
                        break;
                    }
                    seen[val] = 1;
                }
            }
            if (!ok) continue;

            /* check rows */
            for (int r = 0; r < 3 && ok; ++r) {
                int sum = grid[i + r][j] + grid[i + r][j + 1] + grid[i + r][j + 2];
                if (sum != 15) ok = false;
            }
            /* check columns */
            for (int c = 0; c < 3 && ok; ++c) {
                int sum = grid[i][j + c] + grid[i + 1][j + c] + grid[i + 2][j + c];
                if (sum != 15) ok = false;
            }
            /* check diagonals */
            if (ok) {
                int d1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2];
                int d2 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j];
                if (d1 != 15 || d2 != 15) ok = false;
            }

            if (ok) ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumMagicSquaresInside(int[][] grid)
    {
        if (grid == null || grid.Length < 3 || grid[0].Length < 3) return 0;
        int rows = grid.Length, cols = grid[0].Length;
        int count = 0;
        for (int i = 0; i <= rows - 3; i++)
        {
            for (int j = 0; j <= cols - 3; j++)
            {
                if (IsMagic(grid, i, j))
                    count++;
            }
        }
        return count;
    }

    private bool IsMagic(int[][] g, int r, int c)
    {
        // middle must be 5
        if (g[r + 1][c + 1] != 5) return false;

        bool[] seen = new bool[10];
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                int val = g[r + i][c + j];
                if (val < 1 || val > 9 || seen[val]) return false;
                seen[val] = true;
            }
        }

        // check rows and columns sum to 15
        for (int i = 0; i < 3; i++)
        {
            int rowSum = g[r + i][c] + g[r + i][c + 1] + g[r + i][c + 2];
            if (rowSum != 15) return false;
            int colSum = g[r][c + i] + g[r + 1][c + i] + g[r + 2][c + i];
            if (colSum != 15) return false;
        }

        // diagonals
        if (g[r][c] + g[r + 1][c + 1] + g[r + 2][c + 2] != 15) return false;
        if (g[r][c + 2] + g[r + 1][c + 1] + g[r + 2][c] != 15) return false;

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var numMagicSquaresInside = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    let count = 0;

    const isMagic = (r, c) => {
        // center must be 5
        if (grid[r + 1][c + 1] !== 5) return false;

        // check distinct numbers 1..9
        const seen = new Array(10).fill(false);
        for (let i = r; i < r + 3; i++) {
            for (let j = c; j < c + 3; j++) {
                const val = grid[i][j];
                if (val < 1 || val > 9) return false;
                if (seen[val]) return false;
                seen[val] = true;
            }
        }

        // all rows, columns and diagonals must sum to 15
        const target = 15;
        for (let i = 0; i < 3; i++) {
            if (grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2] !== target) return false;
            if (grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] !== target) return false;
        }
        if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] !== target) return false;
        if (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] !== target) return false;

        return true;
    };

    for (let i = 0; i <= rows - 3; i++) {
        for (let j = 0; j <= cols - 3; j++) {
            if (isMagic(i, j)) count++;
        }
    }

    return count;
};
```

## Typescript

```typescript
function numMagicSquaresInside(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let count = 0;

    for (let i = 0; i <= m - 3; ++i) {
        for (let j = 0; j <= n - 3; ++j) {
            if (isMagic(i, j)) count++;
        }
    }

    return count;

    function isMagic(r: number, c: number): boolean {
        // center must be 5
        if (grid[r + 1][c + 1] !== 5) return false;

        const seen = new Array(10).fill(false);
        for (let x = 0; x < 3; ++x) {
            for (let y = 0; y < 3; ++y) {
                const val = grid[r + x][c + y];
                if (val < 1 || val > 9) return false;
                if (seen[val]) return false;
                seen[val] = true;
            }
        }

        // rows
        const row0 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2];
        const row1 = grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2];
        const row2 = grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2];
        if (row0 !== 15 || row1 !== 15 || row2 !== 15) return false;

        // columns
        const col0 = grid[r][c] + grid[r + 1][c] + grid[r + 2][c];
        const col1 = grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1];
        const col2 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2];
        if (col0 !== 15 || col1 !== 15 || col2 !== 15) return false;

        // diagonals
        const diag1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2];
        const diag2 = grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c];
        if (diag1 !== 15 || diag2 !== 15) return false;

        return true;
    }
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function numMagicSquaresInside($grid) {
        $m = count($grid);
        if ($m < 3) return 0;
        $n = count($grid[0]);
        if ($n < 3) return 0;
        $count = 0;
        for ($i = 0; $i <= $m - 3; $i++) {
            for ($j = 0; $j <= $n - 3; $j++) {
                if ($this->isMagic($grid, $i, $j)) {
                    $count++;
                }
            }
        }
        return $count;
    }

    private function isMagic($grid, $r, $c) {
        // center must be 5
        if ($grid[$r + 1][$c + 1] !== 5) {
            return false;
        }
        // check distinctness and range 1..9
        $seen = array_fill(0, 10, false);
        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                $val = $grid[$r + $i][$c + $j];
                if ($val < 1 || $val > 9) {
                    return false;
                }
                if ($seen[$val]) {
                    return false;
                }
                $seen[$val] = true;
            }
        }
        // rows, columns and diagonals must sum to 15
        for ($i = 0; $i < 3; $i++) {
            $rowSum = $grid[$r + $i][$c] + $grid[$r + $i][$c + 1] + $grid[$r + $i][$c + 2];
            if ($rowSum !== 15) {
                return false;
            }
            $colSum = $grid[$r][$c + $i] + $grid[$r + 1][$c + $i] + $grid[$r + 2][$c + $i];
            if ($colSum !== 15) {
                return false;
            }
        }
        $diag1 = $grid[$r][$c] + $grid[$r + 1][$c + 1] + $grid[$r + 2][$c + 2];
        $diag2 = $grid[$r][$c + 2] + $grid[$r + 1][$c + 1] + $grid[$r + 2][$c];
        if ($diag1 !== 15 || $diag2 !== 15) {
            return false;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func numMagicSquaresInside(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        guard rows >= 3 else { return 0 }
        let cols = grid[0].count
        guard cols >= 3 else { return 0 }
        var result = 0
        
        for i in 0..<(rows - 2) {
            for j in 0..<(cols - 2) {
                if isMagic(grid, i, j) {
                    result += 1
                }
            }
        }
        return result
    }
    
    private func isMagic(_ grid: [[Int]], _ r: Int, _ c: Int) -> Bool {
        // Center must be 5 for a 3x3 magic square using numbers 1..9
        if grid[r + 1][c + 1] != 5 { return false }
        
        var seen = [Bool](repeating: false, count: 10)
        for i in 0..<3 {
            for j in 0..<3 {
                let val = grid[r + i][c + j]
                if val < 1 || val > 9 { return false }
                if seen[val] { return false }
                seen[val] = true
            }
        }
        
        // All rows, columns and diagonals must sum to 15
        for i in 0..<3 {
            let rowSum = grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2]
            if rowSum != 15 { return false }
            let colSum = grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i]
            if colSum != 15 { return false }
        }
        
        let diag1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]
        let diag2 = grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]
        if diag1 != 15 || diag2 != 15 { return false }
        
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numMagicSquaresInside(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var count = 0
        for (i in 0 until m - 2) {
            for (j in 0 until n - 2) {
                if (grid[i + 1][j + 1] != 5) continue
                if (isMagic(grid, i, j)) count++
            }
        }
        return count
    }

    private fun isMagic(g: Array<IntArray>, r: Int, c: Int): Boolean {
        val seen = BooleanArray(10)
        for (i in 0..2) {
            for (j in 0..2) {
                val v = g[r + i][c + j]
                if (v < 1 || v > 9 || seen[v]) return false
                seen[v] = true
            }
        }
        val target = 15
        // rows
        for (i in 0..2) {
            if (g[r + i][c] + g[r + i][c + 1] + g[r + i][c + 2] != target) return false
        }
        // columns
        for (j in 0..2) {
            if (g[r][c + j] + g[r + 1][c + j] + g[r + 2][c + j] != target) return false
        }
        // diagonals
        if (g[r][c] + g[r + 1][c + 1] + g[r + 2][c + 2] != target) return false
        if (g[r][c + 2] + g[r + 1][c + 1] + g[r + 2][c] != target) return false
        return true
    }
}
```

## Dart

```dart
class Solution {
  int numMagicSquaresInside(List<List<int>> grid) {
    int m = grid.length;
    if (m < 3) return 0;
    int n = grid[0].length;
    if (n < 3) return 0;

    int count = 0;
    for (int i = 0; i <= m - 3; ++i) {
      for (int j = 0; j <= n - 3; ++j) {
        if (_isMagic(grid, i, j)) {
          count++;
        }
      }
    }
    return count;
  }

  bool _isMagic(List<List<int>> g, int r, int c) {
    // middle must be 5
    if (g[r + 1][c + 1] != 5) return false;

    var seen = List<bool>.filled(10, false);
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        int val = g[r + i][c + j];
        if (val < 1 || val > 9 || seen[val]) return false;
        seen[val] = true;
      }
    }

    // all rows, columns and diagonals must sum to the same value
    int target = g[r][c] + g[r][c + 1] + g[r][c + 2];
    for (int i = 0; i < 3; ++i) {
      int rowSum = g[r + i][c] + g[r + i][c + 1] + g[r + i][c + 2];
      if (rowSum != target) return false;
    }
    for (int j = 0; j < 3; ++j) {
      int colSum = g[r][c + j] + g[r + 1][c + j] + g[r + 2][c + j];
      if (colSum != target) return false;
    }
    int diag1 = g[r][c] + g[r + 1][c + 1] + g[r + 2][c + 2];
    int diag2 = g[r][c + 2] + g[r + 1][c + 1] + g[r + 2][c];
    if (diag1 != target || diag2 != target) return false;

    return true;
  }
}
```

## Golang

```go
func numMagicSquaresInside(grid [][]int) int {
	m := len(grid)
	if m < 3 {
		return 0
	}
	n := len(grid[0])
	if n < 3 {
		return 0
	}
	count := 0
	for i := 0; i <= m-3; i++ {
		for j := 0; j <= n-3; j++ {
			if isMagic(grid, i, j) {
				count++
			}
		}
	}
	return count
}

func isMagic(g [][]int, r, c int) bool {
	// center must be 5
	if g[r+1][c+1] != 5 {
		return false
	}
	mask := 0
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			v := g[r+i][c+j]
			if v < 1 || v > 9 {
				return false
			}
			bit := 1 << v
			if mask&bit != 0 {
				return false
			}
			mask |= bit
		}
	}
	s := g[r][c] + g[r][c+1] + g[r][c+2]
	if s != 15 {
		return false
	}
	if g[r+1][c]+g[r+1][c+1]+g[r+1][c+2] != s {
		return false
	}
	if g[r+2][c]+g[r+2][c+1]+g[r+2][c+2] != s {
		return false
	}
	if g[r][c]+g[r+1][c]+g[r+2][c] != s {
		return false
	}
	if g[r][c+1]+g[r+1][c+1]+g[r+2][c+1] != s {
		return false
	}
	if g[r][c+2]+g[r+1][c+2]+g[r+2][c+2] != s {
		return false
	}
	if g[r][c]+g[r+1][c+1]+g[r+2][c+2] != s {
		return false
	}
	if g[r][c+2]+g[r+1][c+1]+g[r+2][c] != s {
		return false
	}
	return true
}
```

## Ruby

```ruby
def num_magic_squares_inside(grid)
  m = grid.size
  n = grid[0].size
  return 0 if m < 3 || n < 3

  count = 0

  (0..m - 3).each do |i|
    (0..n - 3).each do |j|
      # middle must be 5
      next unless grid[i + 1][j + 1] == 5

      seen = Array.new(10, false)
      valid = true

      3.times do |dx|
        3.times do |dy|
          val = grid[i + dx][j + dy]
          if val < 1 || val > 9 || seen[val]
            valid = false
            break
          end
          seen[val] = true
        end
        break unless valid
      end

      next unless valid

      s = 15
      # rows
      3.times do |dx|
        row_sum = grid[i + dx][j] + grid[i + dx][j + 1] + grid[i + dx][j + 2]
        unless row_sum == s
          valid = false
          break
        end
      end
      next unless valid

      # columns
      3.times do |dy|
        col_sum = grid[i][j + dy] + grid[i + 1][j + dy] + grid[i + 2][j + dy]
        unless col_sum == s
          valid = false
          break
        end
      end
      next unless valid

      # diagonals
      diag1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
      diag2 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
      valid &&= (diag1 == s && diag2 == s)

      count += 1 if valid
    end
  end

  count
end
```

## Scala

```scala
object Solution {
  def numMagicSquaresInside(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    if (m < 3) return 0
    val n = grid(0).length
    var count = 0
    for (i <- 0 until m - 2) {
      for (j <- 0 until n - 2) {
        if (grid(i + 1)(j + 1) == 5 && isMagic(grid, i, j)) {
          count += 1
        }
      }
    }
    count
  }

  private def isMagic(grid: Array[Array[Int]], r: Int, c: Int): Boolean = {
    val seen = new Array[Boolean](10)
    for (i <- 0 until 3) {
      for (j <- 0 until 3) {
        val v = grid(r + i)(c + j)
        if (v < 1 || v > 9 || seen(v)) return false
        seen(v) = true
      }
    }
    // check rows and columns sums
    for (i <- 0 until 3) {
      var sumRow = 0
      var sumCol = 0
      for (j <- 0 until 3) {
        sumRow += grid(r + i)(c + j)
        sumCol += grid(r + j)(c + i)
      }
      if (sumRow != 15 || sumCol != 15) return false
    }
    // check diagonals
    if (grid(r)(c) + grid(r + 1)(c + 1) + grid(r + 2)(c + 2) != 15) return false
    if (grid(r)(c + 2) + grid(r + 1)(c + 1) + grid(r + 2)(c) != 15) return false
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        if rows < 3 {
            return 0;
        }
        let cols = grid[0].len();
        if cols < 3 {
            return 0;
        }

        fn is_magic(g: &Vec<Vec<i32>>, r: usize, c: usize) -> bool {
            // middle must be 5
            if g[r + 1][c + 1] != 5 {
                return false;
            }
            // check numbers are 1..9 and distinct
            let mut seen = [false; 10];
            for i in 0..3 {
                for j in 0..3 {
                    let v = g[r + i][c + j];
                    if v < 1 || v > 9 {
                        return false;
                    }
                    let idx = v as usize;
                    if seen[idx] {
                        return false;
                    }
                    seen[idx] = true;
                }
            }
            // check rows, columns and diagonals sum to 15
            for i in 0..3 {
                let row_sum = g[r + i][c] + g[r + i][c + 1] + g[r + i][c + 2];
                if row_sum != 15 {
                    return false;
                }
                let col_sum = g[r][c + i] + g[r + 1][c + i] + g[r + 2][c + i];
                if col_sum != 15 {
                    return false;
                }
            }
            let diag1 = g[r][c] + g[r + 1][c + 1] + g[r + 2][c + 2];
            let diag2 = g[r][c + 2] + g[r + 1][c + 1] + g[r + 2][c];
            if diag1 != 15 || diag2 != 15 {
                return false;
            }
            true
        }

        let mut count = 0;
        for r in 0..=rows - 3 {
            for c in 0..=cols - 3 {
                if is_magic(&grid, r, c) {
                    count += 1;
                }
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (num-magic-squares-inside grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (null? grid) 0 (length (first grid))))
         (get (lambda (i j) (list-ref (list-ref grid i) j)))
         (magic?
          (lambda (r c)
            ;; middle must be 5
            (when (not (= ((get (+ r 1)) (+ c 1)) 5))
              (return #f))
            ;; check values 1..9 distinct
            (let ((seen (make-vector 10 #f)))
              (for ([dr (in-range 3)]
                    [dc (in-range 3)])
                (define val ((get (+ r dr)) (+ c dc)))
                (when (or (< val 1) (> val 9))
                  (return #f))
                (when (vector-ref seen val)
                  (return #f))
                (vector-set! seen val #t))
              ;; sums must be 15
              (define s15 15)
              (define row0 (+ ((get r) c) ((get r) (+ c 1)) ((get r) (+ c 2))))
              (define row1 (+ ((get (+ r 1)) c) ((get (+ r 1)) (+ c 1)) ((get (+ r 1)) (+ c 2))))
              (define row2 (+ ((get (+ r 2)) c) ((get (+ r 2)) (+ c 1)) ((get (+ r 2)) (+ c 2))))
              (when (or (!= row0 s15) (!= row1 s15) (!= row2 s15))
                (return #f))
              (define col0 (+ ((get r) c) ((get (+ r 1)) c) ((get (+ r 2)) c)))
              (define col1 (+ ((get r) (+ c 1)) ((get (+ r 1)) (+ c 1)) ((get (+ r 2)) (+ c 1))))
              (define col2 (+ ((get r) (+ c 2)) ((get (+ r 1)) (+ c 2)) ((get (+ r 2)) (+ c 2))))
              (when (or (!= col0 s15) (!= col1 s15) (!= col2 s15))
                (return #f))
              (define diag1 (+ ((get r) c) ((get (+ r 1)) (+ c 1)) ((get (+ r 2)) (+ c 2))))
              (define diag2 (+ ((get r) (+ c 2)) ((get (+ r 1)) (+ c 1)) ((get (+ r 2)) c)))
              (when (or (!= diag1 s15) (!= diag2 s15))
                (return #f))
              #t))))
    (let ((cnt 0))
      (for ([i (in-range (- rows 2))]
            [j (in-range (- cols 2))])
        (when (magic? i j)
          (set! cnt (+ cnt 1))))
      cnt)))
```

## Erlang

```erlang
-module(solution).
-export([num_magic_squares_inside/1]).

-spec num_magic_squares_inside(Grid :: [[integer()]]) -> integer().
num_magic_squares_inside(Grid) ->
    R = length(Grid),
    case Grid of
        [] -> 0;
        _ ->
            C = length(lists:nth(1, Grid)),
            if
                R < 3 orelse C < 3 -> 0;
                true ->
                    Rows = lists:seq(0, R - 3),
                    Cols = lists:seq(0, C - 3),
                    count_magic(Grid, Rows, Cols, 0)
            end
    end.

count_magic(_, [], _, Acc) -> Acc;
count_magic(Grid, [I|RestRows], Cols, Acc) ->
    NewAcc = count_row(Grid, I, Cols, Acc),
    count_magic(Grid, RestRows, Cols, NewAcc).

count_row(_, _, [], Acc) -> Acc;
count_row(Grid, I, [J|RestCols], Acc) ->
    case is_magic(Grid, I, J) of
        true -> count_row(Grid, I, RestCols, Acc + 1);
        false -> count_row(Grid, I, RestCols, Acc)
    end.

is_magic(Grid, I, J) ->
    A = get(Grid, I, J),
    B = get(Grid, I, J+1),
    Cc = get(Grid, I, J+2),
    D = get(Grid, I+1, J),
    E = get(Grid, I+1, J+1),
    F = get(Grid, I+1, J+2),
    Gg = get(Grid, I+2, J),
    H = get(Grid, I+2, J+1),
    I_ = get(Grid, I+2, J+2),

    case check_vals([A,B,Cc,D,E,F,Gg,H,I_]) of
        false -> false;
        true ->
            Sum = A + B + Cc,
            (Sum == D + E + F) andalso
            (Sum == Gg + H + I_) andalso
            (Sum == A + D + Gg) andalso
            (Sum == B + E + H) andalso
            (Sum == Cc + F + I_) andalso
            (Sum == A + E + I_) andalso
            (Sum == Cc + E + Gg)
    end.

check_vals(Values) ->
    check_vals(Values, 0).

check_vals([], _) -> true;
check_vals([V|Rest], Mask) when V >= 1, V =< 9 ->
    Bit = 1 bsl (V - 1),
    case (Mask band Bit) of
        0 -> check_vals(Rest, Mask bor Bit);
        _ -> false
    end;
check_vals(_, _) -> false.

get(Grid, R, C) ->
    Row = lists:nth(R + 1, Grid),
    lists:nth(C + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_magic_squares_inside(grid :: [[integer]]) :: integer
  def num_magic_squares_inside(grid) do
    rows = length(grid)
    cols = if rows == 0, do: 0, else: length(hd(grid))

    if rows < 3 or cols < 3 do
      0
    else
      Enum.reduce(0..(rows - 3), 0, fn i, acc ->
        Enum.reduce(0..(cols - 3), acc, fn j, inner_acc ->
          if magic?(grid, i, j), do: inner_acc + 1, else: inner_acc
        end)
      end)
    end
  end

  defp magic?(grid, i, j) do
    a = get(grid, i, j)
    b = get(grid, i, j + 1)
    c = get(grid, i, j + 2)
    d = get(grid, i + 1, j)
    e = get(grid, i + 1, j + 1)
    f = get(grid, i + 1, j + 2)
    g = get(grid, i + 2, j)
    h = get(grid, i + 2, j + 1)
    k = get(grid, i + 2, j + 2)

    vals = [a, b, c, d, e, f, g, h, k]

    # All numbers must be between 1 and 9 and distinct
    if Enum.any?(vals, fn v -> v < 1 or v > 9 end) do
      false
    else
      if length(Enum.uniq(vals)) != 9 do
        false
      else
        sum = a + b + c

        sum == d + e + f and
          sum == g + h + k and
          sum == a + d + g and
          sum == b + e + h and
          sum == c + f + k and
          sum == a + e + k and
          sum == c + e + g
      end
    end
  end

  defp get(grid, i, j) do
    grid |> Enum.at(i) |> Enum.at(j)
  end
end
```

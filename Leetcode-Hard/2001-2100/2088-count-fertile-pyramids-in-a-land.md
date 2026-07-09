# 2088. Count Fertile Pyramids in a Land

## Cpp

```cpp
class Solution {
public:
    int countPyramids(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> down(m, vector<int>(n, 0));
        vector<vector<int>> up(m, vector<int>(n, 0));
        
        // pyramids pointing down (apex at top)
        for (int i = m - 1; i >= 0; --i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    int left = (i + 1 < m && j - 1 >= 0) ? down[i + 1][j - 1] : 0;
                    int right = (i + 1 < m && j + 1 < n) ? down[i + 1][j + 1] : 0;
                    down[i][j] = 1 + min(left, right);
                }
            }
        }
        
        // pyramids pointing up (apex at bottom)
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    int left = (i - 1 >= 0 && j - 1 >= 0) ? up[i - 1][j - 1] : 0;
                    int right = (i - 1 >= 0 && j + 1 < n) ? up[i - 1][j + 1] : 0;
                    up[i][j] = 1 + min(left, right);
                }
            }
        }
        
        long long ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (down[i][j] > 1) ans += down[i][j] - 1;
                if (up[i][j] > 1)   ans += up[i][j] - 1;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countPyramids(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] up = new int[m][n];
        int[][] down = new int[m][n];
        long total = 0L;

        // pyramids pointing upwards (apex at top)
        for (int i = m - 1; i >= 0; --i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    if (i + 1 < m && j - 1 >= 0 && j + 1 < n) {
                        up[i][j] = 1 + Math.min(up[i + 1][j - 1], up[i + 1][j + 1]);
                    } else {
                        up[i][j] = 1;
                    }
                    total += up[i][j] - 1; // count pyramids of height >=2
                }
            }
        }

        // pyramids pointing downwards (apex at bottom)
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    if (i - 1 >= 0 && j - 1 >= 0 && j + 1 < n) {
                        down[i][j] = 1 + Math.min(down[i - 1][j - 1], down[i - 1][j + 1]);
                    } else {
                        down[i][j] = 1;
                    }
                    total += down[i][j] - 1; // count pyramids of height >=2
                }
            }
        }

        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0

        # upright pyramids (apex at top)
        dp_up = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            row = grid[i]
            for j in range(n):
                if row[j]:
                    if i == m - 1 or j == 0 or j == n - 1:
                        dp_up[i][j] = 1
                    else:
                        dp_up[i][j] = 1 + min(dp_up[i + 1][j - 1], dp_up[i + 1][j + 1])
                    ans += dp_up[i][j] - 1

        # inverted pyramids (apex at bottom)
        dp_down = [[0] * n for _ in range(m)]
        for i in range(m):
            row = grid[i]
            for j in range(n):
                if row[j]:
                    if i == 0 or j == 0 or j == n - 1:
                        dp_down[i][j] = 1
                    else:
                        dp_down[i][j] = 1 + min(dp_down[i - 1][j - 1], dp_down[i - 1][j + 1])
                    ans += dp_down[i][j] - 1

        return ans
```

## Python3

```python
class Solution:
    def countPyramids(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0

        # pyramids pointing upwards (apex at top)
        dp_up = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            row = grid[i]
            for j in range(n):
                if row[j]:
                    if i == m - 1 or j == 0 or j == n - 1:
                        dp_up[i][j] = 1
                    else:
                        dp_up[i][j] = 1 + min(dp_up[i + 1][j - 1], dp_up[i + 1][j + 1])
                    ans += dp_up[i][j] - 1

        # pyramids pointing downwards (apex at bottom)
        dp_down = [[0] * n for _ in range(m)]
        for i in range(m):
            row = grid[i]
            for j in range(n):
                if row[j]:
                    if i == 0 or j == 0 or j == n - 1:
                        dp_down[i][j] = 1
                    else:
                        dp_down[i][j] = 1 + min(dp_down[i - 1][j - 1], dp_down[i - 1][j + 1])
                    ans += dp_down[i][j] - 1

        return ans
```

## C

```c
int countPyramids(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    if (m == 0) return 0;
    int n = gridColSize[0];
    // allocate dp arrays
    int **up = (int **)malloc(m * sizeof(int *));
    int **down = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        up[i] = (int *)calloc(n, sizeof(int));
        down[i] = (int *)calloc(n, sizeof(int));
    }
    
    // compute upward pyramids (apex at top, base downward)
    for (int i = m - 1; i >= 0; --i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 1) {
                if (i == m - 1 || j == 0 || j == n - 1) {
                    up[i][j] = 1;
                } else {
                    int a = up[i + 1][j - 1];
                    int b = up[i + 1][j + 1];
                    up[i][j] = 1 + (a < b ? a : b);
                }
            }
        }
    }
    
    // compute downward pyramids (apex at bottom, base upward)
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 1) {
                if (i == 0 || j == 0 || j == n - 1) {
                    down[i][j] = 1;
                } else {
                    int a = down[i - 1][j - 1];
                    int b = down[i - 1][j + 1];
                    down[i][j] = 1 + (a < b ? a : b);
                }
            }
        }
    }
    
    long long total = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (up[i][j] > 1) total += up[i][j] - 1;
            if (down[i][j] > 1) total += down[i][j] - 1;
        }
    }
    
    // free memory
    for (int i = 0; i < m; ++i) {
        free(up[i]);
        free(down[i]);
    }
    free(up);
    free(down);
    
    return (int)total;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountPyramids(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int[,] down = new int[m, n];
        int[,] up = new int[m, n];
        int ans = 0;

        // pyramids with apex at top (pointing downwards)
        for (int r = m - 1; r >= 0; --r)
        {
            for (int c = 0; c < n; ++c)
            {
                if (grid[r][c] == 1)
                {
                    if (r == m - 1 || c == 0 || c == n - 1)
                        down[r, c] = 1;
                    else
                        down[r, c] = 1 + Math.Min(down[r + 1, c - 1], down[r + 1, c + 1]);

                    ans += down[r, c] - 1; // count pyramids of height >=2
                }
            }
        }

        // pyramids with apex at bottom (pointing upwards)
        for (int r = 0; r < m; ++r)
        {
            for (int c = 0; c < n; ++c)
            {
                if (grid[r][c] == 1)
                {
                    if (r == 0 || c == 0 || c == n - 1)
                        up[r, c] = 1;
                    else
                        up[r, c] = 1 + Math.Min(up[r - 1, c - 1], up[r - 1, c + 1]);

                    ans += up[r, c] - 1; // count inverse pyramids of height >=2
                }
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPyramids = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const dpUp = Array.from({ length: m }, () => new Int32Array(n));
    let ans = 0;

    // pyramids pointing up (apex at top)
    for (let i = m - 1; i >= 0; --i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) {
                if (i + 1 < m && j - 1 >= 0 && j + 1 < n) {
                    dpUp[i][j] = 1 + Math.min(dpUp[i + 1][j - 1], dpUp[i + 1][j + 1]);
                } else {
                    dpUp[i][j] = 1;
                }
                if (dpUp[i][j] > 1) ans += dpUp[i][j] - 1; // count pyramids of height >=2
            }
        }
    }

    const dpDown = Array.from({ length: m }, () => new Int32Array(n));

    // pyramids pointing down (apex at bottom)
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) {
                if (i - 1 >= 0 && j - 1 >= 0 && j + 1 < n) {
                    dpDown[i][j] = 1 + Math.min(dpDown[i - 1][j - 1], dpDown[i - 1][j + 1]);
                } else {
                    dpDown[i][j] = 1;
                }
                if (dpDown[i][j] > 1) ans += dpDown[i][j] - 1; // count pyramids of height >=2
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function countPyramids(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;

    // dp for pyramids pointing up (apex at top)
    const up: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = m - 1; i >= 0; --i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) {
                if (i === m - 1 || j === 0 || j === n - 1) {
                    up[i][j] = 1;
                } else {
                    up[i][j] = 1 + Math.min(up[i + 1][j - 1], up[i + 1][j + 1]);
                }
            }
        }
    }

    // dp for pyramids pointing down (apex at bottom)
    const down: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) {
                if (i === 0 || j === 0 || j === n - 1) {
                    down[i][j] = 1;
                } else {
                    down[i][j] = 1 + Math.min(down[i - 1][j - 1], down[i - 1][j + 1]);
                }
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (up[i][j] >= 2) ans += up[i][j] - 1;
            if (down[i][j] >= 2) ans += down[i][j] - 1;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countPyramids($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        // dp for pyramids pointing downwards (apex at top)
        $downward = array_fill(0, $m, array_fill(0, $n, 0));
        $ans = 0;
        for ($i = $m - 1; $i >= 0; --$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] == 1) {
                    if ($i == $m - 1 || $j == 0 || $j == $n - 1) {
                        $downward[$i][$j] = 1;
                    } else {
                        $downward[$i][$j] = min($downward[$i + 1][$j - 1], $downward[$i + 1][$j + 1]) + 1;
                    }
                    if ($downward[$i][$j] > 1) {
                        $ans += $downward[$i][$j] - 1;
                    }
                }
            }
        }

        // dp for pyramids pointing upwards (apex at bottom)
        $upward = array_fill(0, $m, array_fill(0, $n, 0));
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] == 1) {
                    if ($i == 0 || $j == 0 || $j == $n - 1) {
                        $upward[$i][$j] = 1;
                    } else {
                        $upward[$i][$j] = min($upward[$i - 1][$j - 1], $upward[$i - 1][$j + 1]) + 1;
                    }
                    if ($upward[$i][$j] > 1) {
                        $ans += $upward[$i][$j] - 1;
                    }
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countPyramids(_ grid: [[Int]]) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        
        var up = Array(repeating: Array(repeating: 0, count: n), count: m)
        var down = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        // pyramids pointing upwards (apex at top)
        for r in stride(from: m - 1, through: 0, by: -1) {
            for c in 0..<n {
                if grid[r][c] == 1 {
                    if r == m - 1 || c == 0 || c == n - 1 {
                        up[r][c] = 1
                    } else {
                        let minNeighbor = min(up[r + 1][c - 1], up[r + 1][c + 1])
                        up[r][c] = 1 + minNeighbor
                    }
                }
            }
        }
        
        // pyramids pointing downwards (apex at bottom)
        for r in 0..<m {
            for c in 0..<n {
                if grid[r][c] == 1 {
                    if r == 0 || c == 0 || c == n - 1 {
                        down[r][c] = 1
                    } else {
                        let minNeighbor = min(down[r - 1][c - 1], down[r - 1][c + 1])
                        down[r][c] = 1 + minNeighbor
                    }
                }
            }
        }
        
        var ans = 0
        for r in 0..<m {
            for c in 0..<n {
                if up[r][c] > 1 { ans += up[r][c] - 1 }
                if down[r][c] > 1 { ans += down[r][c] - 1 }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPyramids(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var total = 0L

        // pyramids pointing up (apex at top)
        val dpUp = Array(m) { IntArray(n) }
        for (i in m - 1 downTo 0) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    var left = 0
                    var right = 0
                    if (i + 1 < m && j - 1 >= 0) left = dpUp[i + 1][j - 1]
                    if (i + 1 < m && j + 1 < n) right = dpUp[i + 1][j + 1]
                    val h = 1 + kotlin.math.min(left, right)
                    dpUp[i][j] = h
                    if (h > 1) total += (h - 1).toLong()
                }
            }
        }

        // pyramids pointing down (apex at bottom)
        val dpDown = Array(m) { IntArray(n) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    var left = 0
                    var right = 0
                    if (i - 1 >= 0 && j - 1 >= 0) left = dpDown[i - 1][j - 1]
                    if (i - 1 >= 0 && j + 1 < n) right = dpDown[i - 1][j + 1]
                    val h = 1 + kotlin.math.min(left, right)
                    dpDown[i][j] = h
                    if (h > 1) total += (h - 1).toLong()
                }
            }
        }

        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countPyramids(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    List<List<int>> down = List.generate(m, (_) => List.filled(n, 0));
    for (int i = m - 1; i >= 0; --i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) {
          int left = (i + 1 < m && j - 1 >= 0) ? down[i + 1][j - 1] : 0;
          int right = (i + 1 < m && j + 1 < n) ? down[i + 1][j + 1] : 0;
          down[i][j] = 1 + (left < right ? left : right);
        }
      }
    }

    List<List<int>> up = List.generate(m, (_) => List.filled(n, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) {
          int left = (i - 1 >= 0 && j - 1 >= 0) ? up[i - 1][j - 1] : 0;
          int right = (i - 1 >= 0 && j + 1 < n) ? up[i - 1][j + 1] : 0;
          up[i][j] = 1 + (left < right ? left : right);
        }
      }
    }

    int ans = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (down[i][j] > 1) ans += down[i][j] - 1;
        if (up[i][j] > 1) ans += up[i][j] - 1;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countPyramids(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	ans := 0

	// upright pyramids
	dpUp := make([][]int, m)
	for i := 0; i < m; i++ {
		dpUp[i] = make([]int, n)
	}
	for r := m - 1; r >= 0; r-- {
		for c := 0; c < n; c++ {
			if grid[r][c] == 1 {
				if r == m-1 || c == 0 || c == n-1 {
					dpUp[r][c] = 1
				} else {
					left := dpUp[r+1][c-1]
					right := dpUp[r+1][c+1]
					if left < right {
						dpUp[r][c] = left + 1
					} else {
						dpUp[r][c] = right + 1
					}
				}
				if dpUp[r][c] > 1 {
					ans += dpUp[r][c] - 1
				}
			}
		}
	}

	// inverted pyramids
	dpDown := make([][]int, m)
	for i := 0; i < m; i++ {
		dpDown[i] = make([]int, n)
	}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] == 1 {
				if r == 0 || c == 0 || c == n-1 {
					dpDown[r][c] = 1
				} else {
					left := dpDown[r-1][c-1]
					right := dpDown[r-1][c+1]
					if left < right {
						dpDown[r][c] = left + 1
					} else {
						dpDown[r][c] = right + 1
					}
				}
				if dpDown[r][c] > 1 {
					ans += dpDown[r][c] - 1
				}
			}
		}
	}

	return ans
}
```

## Ruby

```ruby
def count_pyramids(grid)
  m = grid.size
  n = grid[0].size
  ans = 0

  # pyramids pointing up
  dp_up = Array.new(m) { Array.new(n, 0) }
  (m - 1).downto(0) do |r|
    (0...n).each do |c|
      next unless grid[r][c] == 1
      if r + 1 < m && c - 1 >= 0 && c + 1 < n
        dp_up[r][c] = 1 + [dp_up[r + 1][c - 1], dp_up[r + 1][c + 1]].min
      else
        dp_up[r][c] = 1
      end
      ans += dp_up[r][c] - 1 if dp_up[r][c] > 1
    end
  end

  # pyramids pointing down (inverse)
  dp_down = Array.new(m) { Array.new(n, 0) }
  (0...m).each do |r|
    (0...n).each do |c|
      next unless grid[r][c] == 1
      if r - 1 >= 0 && c - 1 >= 0 && c + 1 < n
        dp_down[r][c] = 1 + [dp_down[r - 1][c - 1], dp_down[r - 1][c + 1]].min
      else
        dp_down[r][c] = 1
      end
      ans += dp_down[r][c] - 1 if dp_down[r][c] > 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countPyramids(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        var total: Long = 0L

        // Upward pyramids (apex at top)
        val up = Array.ofDim[Int](m, n)
        for (i <- (m - 1) to 0 by -1) {
            for (j <- 0 until n) {
                if (grid(i)(j) == 1) {
                    val left  = if (i + 1 < m && j - 1 >= 0) up(i + 1)(j - 1) else 0
                    val right = if (i + 1 < m && j + 1 < n) up(i + 1)(j + 1) else 0
                    up(i)(j) = 1 + Math.min(left, right)
                    if (up(i)(j) > 1) total += up(i)(j) - 1
                }
            }
        }

        // Downward pyramids (apex at bottom)
        val down = Array.ofDim[Int](m, n)
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (grid(i)(j) == 1) {
                    val left  = if (i - 1 >= 0 && j - 1 >= 0) down(i - 1)(j - 1) else 0
                    val right = if (i - 1 >= 0 && j + 1 < n) down(i - 1)(j + 1) else 0
                    down(i)(j) = 1 + Math.min(left, right)
                    if (down(i)(j) > 1) total += down(i)(j) - 1
                }
            }
        }

        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_pyramids(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();

        // dp_up[r][c] = max height of upward pyramid with apex at (r,c)
        let mut dp_up = vec![vec![0usize; n]; m];
        for r in (0..m).rev() {
            for c in 0..n {
                if grid[r][c] == 1 {
                    if r + 1 < m && c > 0 && c + 1 < n {
                        let min_adj = dp_up[r + 1][c - 1].min(dp_up[r + 1][c + 1]);
                        dp_up[r][c] = 1 + min_adj;
                    } else {
                        dp_up[r][c] = 1;
                    }
                }
            }
        }

        // dp_down[r][c] = max height of inverted pyramid with apex at (r,c)
        let mut dp_down = vec![vec![0usize; n]; m];
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] == 1 {
                    if r > 0 && c > 0 && c + 1 < n {
                        let min_adj = dp_down[r - 1][c - 1].min(dp_down[r - 1][c + 1]);
                        dp_down[r][c] = 1 + min_adj;
                    } else {
                        dp_down[r][c] = 1;
                    }
                }
            }
        }

        let mut ans: i64 = 0;
        for r in 0..m {
            for c in 0..n {
                if dp_up[r][c] > 1 {
                    ans += (dp_up[r][c] - 1) as i64;
                }
                if dp_down[r][c] > 1 {
                    ans += (dp_down[r][c] - 1) as i64;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-pyramids grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([gridV (list->vector (map list->vector grid))]
         [m (vector-length gridV)]
         [n (if (= m 0) 0 (vector-length (vector-ref gridV 0)))])
    (define up (make-vector m))
    (define down (make-vector m))
    ;; initialize DP tables with the original cell values
    (for ([i (in-range m)])
      (let* ([row-up (make-vector n 0)]
             [row-down (make-vector n 0)]
             [grid-row (vector-ref gridV i)])
        (for ([j (in-range n)])
          (let ([val (vector-ref grid-row j)])
            (vector-set! row-up j val)
            (vector-set! row-down j val)))
        (vector-set! up i row-up)
        (vector-set! down i row-down)))
    ;; upward pyramids (apex at top, expands downward)
    (when (>= m 2)
      (for ([i (in-range (- m 2) -1 -1)]) ; from m-2 downto 0
        (let* ([row-up (vector-ref up i)]
               [row-below (vector-ref up (+ i 1))]
               [grid-row (vector-ref gridV i)])
          (for ([j (in-range 1 (- n 1))])
            (when (= (vector-ref grid-row j) 1)
              (let* ([left (vector-ref row-below (- j 1))]
                     [right (vector-ref row-below (+ j 1))]
                     [val (+ 1 (min left right))])
                (vector-set! row-up j val)))))))
    ;; downward pyramids (apex at bottom, expands upward)
    (when (>= m 2)
      (for ([i (in-range 1 m)]) ; from 1 to m-1
        (let* ([row-down (vector-ref down i)]
               [row-above (vector-ref down (- i 1))]
               [grid-row (vector-ref gridV i)])
          (for ([j (in-range 1 (- n 1))])
            (when (= (vector-ref grid-row j) 1)
              (let* ([left (vector-ref row-above (- j 1))]
                     [right (vector-ref row-above (+ j 1))]
                     [val (+ 1 (min left right))])
                (vector-set! row-down j val)))))))
    ;; sum contributions: each cell contributes (height-1) pyramids of each type
    (let ([total (make-parameter 0)])
      (for ([i (in-range m)])
        (let* ([row-up (vector-ref up i)]
               [row-down (vector-ref down i)])
          (for ([j (in-range n)])
            (let ([u (vector-ref row-up j)]
                  [d (vector-ref row-down j)])
              (when (> u 1) (total (+ (total) (- u 1))))
              (when (> d 1) (total (+ (total) (- d 1))))))))
      (total))))
```

## Erlang

```erlang
-module(solution).
-export([count_pyramids/1]).

-spec count_pyramids(Grid :: [[integer()]]) -> integer().
count_pyramids(Grid) ->
    RowsTuples = [list_to_tuple(Row) || Row <- Grid],
    case RowsTuples of
        [] -> 0;
        [First|_] ->
            N = tuple_size(First),
            Zero = zero_tuple(N),
            TotalUp = compute_up(lists:reverse(RowsTuples), N, Zero, 0),
            TotalDown = compute_down(RowsTuples, N, Zero, 0),
            TotalUp + TotalDown
    end.

zero_tuple(N) ->
    list_to_tuple(lists:duplicate(N, 0)).

compute_up([], _N, _Prev, Total) -> Total;
compute_up([Row|Rest], N, Prev, Total) ->
    {CurrVals, Add} = process_row(Row, Prev, N),
    NewTotal = Total + Add,
    compute_up(Rest, N, list_to_tuple(CurrVals), NewTotal).

compute_down([], _N, _Prev, Total) -> Total;
compute_down([Row|Rest], N, Prev, Total) ->
    {CurrVals, Add} = process_row(Row, Prev, N),
    NewTotal = Total + Add,
    compute_down(Rest, N, list_to_tuple(CurrVals), NewTotal).

process_row(RowTuple, PrevTuple, N) ->
    Indices = lists:seq(1, N),
    {RevList, Add} =
        lists:foldl(
            fun(I, {AccL, AccA}) ->
                Val = case element(I, RowTuple) of
                    0 -> 0;
                    1 ->
                        L = if I > 1 -> element(I-1, PrevTuple); true -> 0 end,
                        R = if I < N -> element(I+1, PrevTuple); true -> 0 end,
                        1 + min(L, R)
                end,
                { [Val | AccL], AccA + max(Val - 1, 0) }
            end,
            {[], 0},
            Indices),
    {lists:reverse(RevList), Add}.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pyramids(grid :: [[integer]]) :: integer
  def count_pyramids(grid) do
    n = length(hd(grid))

    down = compute_direction(Enum.reverse(grid), n)
    up   = compute_direction(grid, n)

    down + up
  end

  defp compute_direction(rows, n) do
    {total, _} =
      Enum.reduce(rows, {0, :array.new(n, default: 0)}, fn row, {acc, prev_arr} ->
        dp_vals =
          Enum.with_index(row)
          |> Enum.map(fn {val, j} ->
            if val == 1 do
              left = if j > 0, do: :array.get(j - 1, prev_arr), else: 0
              right = if j + 1 < n, do: :array.get(j + 1, prev_arr), else: 0
              1 + min(left, right)
            else
              0
            end
          end)

        add =
          Enum.reduce(dp_vals, 0, fn v, sum ->
            if v > 1, do: sum + v - 1, else: sum
          end)

        {acc + add, :array.from_list(dp_vals)}
      end)

    total
  end
end
```

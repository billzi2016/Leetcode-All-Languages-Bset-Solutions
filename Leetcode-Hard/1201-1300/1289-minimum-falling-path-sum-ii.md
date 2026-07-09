# 1289. Minimum Falling Path Sum II

## Cpp

```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        const int INF = INT_MAX;
        int next_min1 = INF, next_min2 = INF;
        int next_min1_c = -1, next_min2_c = -1;

        // Initialize with the last row
        for (int col = 0; col < n; ++col) {
            int val = grid[n - 1][col];
            if (val <= next_min1) {
                next_min2 = next_min1;
                next_min2_c = next_min1_c;
                next_min1 = val;
                next_min1_c = col;
            } else if (val <= next_min2) {
                next_min2 = val;
                next_min2_c = col;
            }
        }

        // Process rows from bottom-2 up to top
        for (int row = n - 2; row >= 0; --row) {
            int min1 = INF, min2 = INF;
            int min1_c = -1, min2_c = -1;
            for (int col = 0; col < n; ++col) {
                int cur = grid[row][col] + (col != next_min1_c ? next_min1 : next_min2);
                if (cur <= min1) {
                    min2 = min1;
                    min2_c = min1_c;
                    min1 = cur;
                    min1_c = col;
                } else if (cur <= min2) {
                    min2 = cur;
                    min2_c = col;
                }
            }
            next_min1 = min1; next_min1_c = min1_c;
            next_min2 = min2; next_min2_c = min2_c;
        }

        return next_min1;
    }
};
```

## Java

```java
class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length;
        if (n == 1) return grid[0][0];

        // Initialize minimum and second minimum for the last row
        int nextMin1 = Integer.MAX_VALUE, nextMin2 = Integer.MAX_VALUE;
        int nextIdx1 = -1, nextIdx2 = -1;

        for (int col = 0; col < n; col++) {
            int val = grid[n - 1][col];
            if (val <= nextMin1) {
                nextMin2 = nextMin1;
                nextIdx2 = nextIdx1;
                nextMin1 = val;
                nextIdx1 = col;
            } else if (val <= nextMin2) {
                nextMin2 = val;
                nextIdx2 = col;
            }
        }

        // Process rows from bottom-1 up to top
        for (int row = n - 2; row >= 0; row--) {
            int curMin1 = Integer.MAX_VALUE, curMin2 = Integer.MAX_VALUE;
            int curIdx1 = -1, curIdx2 = -1;

            for (int col = 0; col < n; col++) {
                int add = (col != nextIdx1) ? nextMin1 : nextMin2;
                int val = grid[row][col] + add;

                if (val <= curMin1) {
                    curMin2 = curMin1;
                    curIdx2 = curIdx1;
                    curMin1 = val;
                    curIdx1 = col;
                } else if (val <= curMin2) {
                    curMin2 = val;
                    curIdx2 = col;
                }
            }

            nextMin1 = curMin1;
            nextIdx1 = curIdx1;
            nextMin2 = curMin2;
            nextIdx2 = curIdx2;
        }

        return nextMin1;
    }
}
```

## Python

```python
class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        # Initialize minima for the last row
        next_min1 = None
        next_min2 = None
        next_min1_c = -1
        next_min2_c = -1
        for c in range(n):
            v = grid[n-1][c]
            if next_min1 is None or v < next_min1:
                next_min2, next_min2_c = next_min1, next_min1_c
                next_min1, next_min1_c = v, c
            elif next_min2 is None or v < next_min2:
                next_min2, next_min2_c = v, c

        # Process rows from bottom-2 up to top
        for r in range(n-2, -1, -1):
            cur_min1 = None
            cur_min2 = None
            cur_min1_c = -1
            cur_min2_c = -1
            for c in range(n):
                if c != next_min1_c:
                    val = grid[r][c] + next_min1
                else:
                    val = grid[r][c] + next_min2
                if cur_min1 is None or val < cur_min1:
                    cur_min2, cur_min2_c = cur_min1, cur_min1_c
                    cur_min1, cur_min1_c = val, c
                elif cur_min2 is None or val < cur_min2:
                    cur_min2, cur_min2_c = val, c
            next_min1, next_min1_c = cur_min1, cur_min1_c
            next_min2, next_min2_c = cur_min2, cur_min2_c

        return next_min1
```

## Python3

```python
class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        INF = 10**15

        # Initialize mins for the last row
        next_min1 = INF
        next_min2 = INF
        next_min1_c = -1
        next_min2_c = -1
        for c in range(n):
            val = grid[n - 1][c]
            if val <= next_min1:
                next_min2, next_min2_c = next_min1, next_min1_c
                next_min1, next_min1_c = val, c
            elif val <= next_min2:
                next_min2, next_min2_c = val, c

        # Process rows from bottom-2 up to top
        for r in range(n - 2, -1, -1):
            cur_min1 = INF
            cur_min2 = INF
            cur_min1_c = -1
            cur_min2_c = -1
            row_vals = grid[r]
            for c in range(n):
                if c != next_min1_c:
                    v = row_vals[c] + next_min1
                else:
                    v = row_vals[c] + next_min2

                if v <= cur_min1:
                    cur_min2, cur_min2_c = cur_min1, cur_min1_c
                    cur_min1, cur_min1_c = v, c
                elif v <= cur_min2:
                    cur_min2, cur_min2_c = v, c

            next_min1, next_min1_c = cur_min1, cur_min1_c
            next_min2, next_min2_c = cur_min2, cur_min2_c

        return next_min1
```

## C

```c
int minFallingPathSum(int** grid, int gridSize, int* gridColSize) {
    const int INF = 1e9;
    int n = gridSize;

    // Initialize minimums for the last row
    int next_min1 = INF, next_min2 = INF;
    int next_min1_c = -1, next_min2_c = -1;

    for (int col = 0; col < n; ++col) {
        int val = grid[n - 1][col];
        if (val <= next_min1) {
            next_min2 = next_min1;
            next_min2_c = next_min1_c;
            next_min1 = val;
            next_min1_c = col;
        } else if (val <= next_min2) {
            next_min2 = val;
            next_min2_c = col;
        }
    }

    // Process rows from bottom-1 up to top
    for (int row = n - 2; row >= 0; --row) {
        int min1 = INF, min2 = INF;
        int min1_c = -1, min2_c = -1;

        for (int col = 0; col < n; ++col) {
            int cur = grid[row][col];
            int value = (col != next_min1_c) ? cur + next_min1 : cur + next_min2;

            if (value <= min1) {
                min2 = min1;
                min2_c = min1_c;
                min1 = value;
                min1_c = col;
            } else if (value <= min2) {
                min2 = value;
                min2_c = col;
            }
        }

        next_min1 = min1;
        next_min1_c = min1_c;
        next_min2 = min2;
        next_min2_c = min2_c;
    }

    return next_min1;
}
```

## Csharp

```csharp
using System;
public class Solution {
    public int MinFallingPathSum(int[][] grid) {
        int n = grid.Length;
        // Initialize minima for the last row
        int nextMin1 = int.MaxValue, nextMin2 = int.MaxValue;
        int nextIdx1 = -1, nextIdx2 = -1;
        for (int col = 0; col < n; col++) {
            int val = grid[n - 1][col];
            if (val <= nextMin1) {
                nextMin2 = nextMin1;
                nextIdx2 = nextIdx1;
                nextMin1 = val;
                nextIdx1 = col;
            } else if (val <= nextMin2) {
                nextMin2 = val;
                nextIdx2 = col;
            }
        }

        // Process rows from bottom-2 up to top
        for (int row = n - 2; row >= 0; row--) {
            int curMin1 = int.MaxValue, curMin2 = int.MaxValue;
            int curIdx1 = -1, curIdx2 = -1;
            for (int col = 0; col < n; col++) {
                int add = (col != nextIdx1) ? nextMin1 : nextMin2;
                int value = grid[row][col] + add;

                if (value <= curMin1) {
                    curMin2 = curMin1;
                    curIdx2 = curIdx1;
                    curMin1 = value;
                    curIdx1 = col;
                } else if (value <= curMin2) {
                    curMin2 = value;
                    curIdx2 = col;
                }
            }
            nextMin1 = curMin1; nextIdx1 = curIdx1;
            nextMin2 = curMin2; nextIdx2 = curIdx2;
        }

        return nextMin1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minFallingPathSum = function(grid) {
    const n = grid.length;
    if (n === 0) return 0;
    // Initialize minima for the last row
    let nextMinVal = Infinity, nextSecondVal = Infinity;
    let nextMinIdx = -1, nextSecondIdx = -1;
    for (let col = 0; col < n; ++col) {
        const v = grid[n - 1][col];
        if (v <= nextMinVal) {
            nextSecondVal = nextMinVal;
            nextSecondIdx = nextMinIdx;
            nextMinVal = v;
            nextMinIdx = col;
        } else if (v <= nextSecondVal) {
            nextSecondVal = v;
            nextSecondIdx = col;
        }
    }

    // Process rows from bottom-2 up to top
    for (let row = n - 2; row >= 0; --row) {
        let curMinVal = Infinity, curSecondVal = Infinity;
        let curMinIdx = -1, curSecondIdx = -1;
        for (let col = 0; col < n; ++col) {
            const add = (col !== nextMinIdx) ? nextMinVal : nextSecondVal;
            const val = grid[row][col] + add;
            if (val <= curMinVal) {
                curSecondVal = curMinVal;
                curSecondIdx = curMinIdx;
                curMinVal = val;
                curMinIdx = col;
            } else if (val <= curSecondVal) {
                curSecondVal = val;
                curSecondIdx = col;
            }
        }
        nextMinVal = curMinVal;
        nextSecondVal = curSecondVal;
        nextMinIdx = curMinIdx;
        nextSecondIdx = curSecondIdx;
    }

    return nextMinVal;
};
```

## Typescript

```typescript
function minFallingPathSum(grid: number[][]): number {
    const n = grid.length;
    // Initialize minima for the last row
    let nextMin = Infinity, nextSecond = Infinity;
    let nextIdx = -1, nextSecondIdx = -1;

    for (let col = 0; col < n; col++) {
        const val = grid[n - 1][col];
        if (val <= nextMin) {
            nextSecond = nextMin;
            nextSecondIdx = nextIdx;
            nextMin = val;
            nextIdx = col;
        } else if (val <= nextSecond) {
            nextSecond = val;
            nextSecondIdx = col;
        }
    }

    // Process rows from bottom-2 up to top
    for (let row = n - 2; row >= 0; row--) {
        let curMin = Infinity, curSecond = Infinity;
        let curIdx = -1, curSecondIdx = -1;

        for (let col = 0; col < n; col++) {
            const add = (col !== nextIdx) ? nextMin : nextSecond;
            const val = grid[row][col] + add;

            if (val <= curMin) {
                curSecond = curMin;
                curSecondIdx = curIdx;
                curMin = val;
                curIdx = col;
            } else if (val <= curSecond) {
                curSecond = val;
                curSecondIdx = col;
            }
        }

        nextMin = curMin;
        nextSecond = curSecond;
        nextIdx = curIdx;
        nextSecondIdx = curSecondIdx;
    }

    return nextMin;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minFallingPathSum($grid) {
        $n = count($grid);
        // Initialize minimums from the last row
        $nextMin1 = null;
        $nextMin2 = null;
        $nextMin1c = -1;
        $nextMin2c = -1;

        for ($col = 0; $col < $n; $col++) {
            $val = $grid[$n - 1][$col];
            if ($nextMin1 === null || $val <= $nextMin1) {
                $nextMin2 = $nextMin1;
                $nextMin2c = $nextMin1c;
                $nextMin1 = $val;
                $nextMin1c = $col;
            } elseif ($nextMin2 === null || $val <= $nextMin2) {
                $nextMin2 = $val;
                $nextMin2c = $col;
            }
        }

        // Process rows from bottom-2 up to top
        for ($row = $n - 2; $row >= 0; $row--) {
            $min1 = null;
            $min2 = null;
            $min1c = -1;
            $min2c = -1;

            for ($col = 0; $col < $n; $col++) {
                if ($col != $nextMin1c) {
                    $value = $grid[$row][$col] + $nextMin1;
                } else {
                    // Use second minimum when column clashes
                    $value = $grid[$row][$col] + $nextMin2;
                }

                if ($min1 === null || $value <= $min1) {
                    $min2 = $min1;
                    $min2c = $min1c;
                    $min1 = $value;
                    $min1c = $col;
                } elseif ($min2 === null || $value <= $min2) {
                    $min2 = $value;
                    $min2c = $col;
                }
            }

            // Update next row's minima
            $nextMin1 = $min1;
            $nextMin2 = $min2;
            $nextMin1c = $min1c;
            $nextMin2c = $min2c;
        }

        return $nextMin1;
    }
}
```

## Swift

```swift
class Solution {
    func minFallingPathSum(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var nextMin1 = 0, nextMin2 = 0
        var nextMin1c = -1, nextMin2c = -1

        // Initialize with the last row
        for col in 0..<n {
            let val = grid[n - 1][col]
            if nextMin1c == -1 || val <= nextMin1 {
                nextMin2 = nextMin1
                nextMin2c = nextMin1c
                nextMin1 = val
                nextMin1c = col
            } else if nextMin2c == -1 || val <= nextMin2 {
                nextMin2 = val
                nextMin2c = col
            }
        }

        if n > 1 {
            for row in stride(from: n - 2, through: 0, by: -1) {
                var min1 = Int.max
                var min2 = Int.max
                var min1c = -1
                var min2c = -1

                for col in 0..<n {
                    let add = (col != nextMin1c) ? nextMin1 : nextMin2
                    let val = grid[row][col] + add

                    if val <= min1 {
                        min2 = min1
                        min2c = min1c
                        min1 = val
                        min1c = col
                    } else if val <= min2 {
                        min2 = val
                        min2c = col
                    }
                }

                nextMin1 = min1
                nextMin2 = min2
                nextMin1c = min1c
                nextMin2c = min2c
            }
        }

        return nextMin1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minFallingPathSum(grid: Array<IntArray>): Int {
        val n = grid.size
        if (n == 1) return grid[0][0]

        var nextMin1 = Int.MAX_VALUE
        var nextMin2 = Int.MAX_VALUE
        var nextIdx1 = -1
        var nextIdx2 = -1

        // Initialize with the last row values
        for (c in 0 until n) {
            val v = grid[n - 1][c]
            if (v <= nextMin1) {
                nextMin2 = nextMin1
                nextIdx2 = nextIdx1
                nextMin1 = v
                nextIdx1 = c
            } else if (v <= nextMin2) {
                nextMin2 = v
                nextIdx2 = c
            }
        }

        // Process rows from bottom-1 up to top
        for (row in n - 2 downTo 0) {
            var curMin1 = Int.MAX_VALUE
            var curMin2 = Int.MAX_VALUE
            var curIdx1 = -1
            var curIdx2 = -1

            for (c in 0 until n) {
                val add = if (c != nextIdx1) nextMin1 else nextMin2
                val v = grid[row][c] + add
                if (v <= curMin1) {
                    curMin2 = curMin1
                    curIdx2 = curIdx1
                    curMin1 = v
                    curIdx1 = c
                } else if (v <= curMin2) {
                    curMin2 = v
                    curIdx2 = c
                }
            }

            nextMin1 = curMin1
            nextIdx1 = curIdx1
            nextMin2 = curMin2
            nextIdx2 = curIdx2
        }

        return nextMin1
    }
}
```

## Dart

```dart
class Solution {
  int minFallingPathSum(List<List<int>> grid) {
    int n = grid.length;
    const int INF = 1 << 60;

    int? nextMin1Col;
    int? nextMin2Col;
    int nextMin1Val = INF;
    int nextMin2Val = INF;

    // Initialize with the last row
    for (int col = 0; col < n; ++col) {
      int val = grid[n - 1][col];
      if (val <= nextMin1Val) {
        nextMin2Val = nextMin1Val;
        nextMin2Col = nextMin1Col;
        nextMin1Val = val;
        nextMin1Col = col;
      } else if (val <= nextMin2Val) {
        nextMin2Val = val;
        nextMin2Col = col;
      }
    }

    // Process rows from bottom-1 to top
    for (int row = n - 2; row >= 0; --row) {
      int? curMin1Col;
      int? curMin2Col;
      int curMin1Val = INF;
      int curMin2Val = INF;

      for (int col = 0; col < n; ++col) {
        int add = (nextMin1Col != null && col != nextMin1Col) ? nextMin1Val : nextMin2Val;
        int value = grid[row][col] + add;

        if (value <= curMin1Val) {
          curMin2Val = curMin1Val;
          curMin2Col = curMin1Col;
          curMin1Val = value;
          curMin1Col = col;
        } else if (value <= curMin2Val) {
          curMin2Val = value;
          curMin2Col = col;
        }
      }

      nextMin1Val = curMin1Val;
      nextMin1Col = curMin1Col;
      nextMin2Val = curMin2Val;
      nextMin2Col = curMin2Col;
    }

    return nextMin1Val;
  }
}
```

## Golang

```go
func minFallingPathSum(grid [][]int) int {
	const INF = int(1 << 60)

	n := len(grid)
	if n == 0 {
		return 0
	}

	// Initialize minima for the last row.
	nextMin1, nextMin2 := INF, INF
	nextMin1c, nextMin2c := -1, -1
	for c, v := range grid[n-1] {
		if v <= nextMin1 {
			nextMin2, nextMin2c = nextMin1, nextMin1c
			nextMin1, nextMin1c = v, c
		} else if v <= nextMin2 {
			nextMin2, nextMin2c = v, c
		}
	}

	// Process rows from bottom-1 up to top.
	for r := n - 2; r >= 0; r-- {
		curMin1, curMin2 := INF, INF
		curMin1c, curMin2c := -1, -1
		for c, val := range grid[r] {
			var sum int
			if c != nextMin1c {
				sum = val + nextMin1
			} else {
				sum = val + nextMin2
			}
			if sum <= curMin1 {
				curMin2, curMin2c = curMin1, curMin1c
				curMin1, curMin1c = sum, c
			} else if sum <= curMin2 {
				curMin2, curMin2c = sum, c
			}
		}
		nextMin1, nextMin2 = curMin1, curMin2
		nextMin1c, nextMin2c = curMin1c, curMin2c
	}

	return nextMin1
}
```

## Ruby

```ruby
def min_falling_path_sum(grid)
  n = grid.size
  # Initialize minima for the last row
  next_min1 = nil
  next_min2 = nil
  next_min1_c = -1
  next_min2_c = -1

  (0...n).each do |col|
    val = grid[n - 1][col]
    if next_min1.nil? || val <= next_min1
      next_min2 = next_min1
      next_min2_c = next_min1_c
      next_min1 = val
      next_min1_c = col
    elsif next_min2.nil? || val <= next_min2
      next_min2 = val
      next_min2_c = col
    end
  end

  (n - 2).downto(0) do |row|
    min1 = nil
    min2 = nil
    min1_c = -1
    min2_c = -1

    (0...n).each do |col|
      if col != next_min1_c
        cur = grid[row][col] + next_min1
      else
        # If there is no second minimum (happens when n == 1), reuse the only value
        cur = grid[row][col] + (next_min2.nil? ? next_min1 : next_min2)
      end

      if min1.nil? || cur <= min1
        min2 = min1
        min2_c = min1_c
        min1 = cur
        min1_c = col
      elsif min2.nil? || cur <= min2
        min2 = cur
        min2_c = col
      end
    end

    next_min1, next_min2 = min1, min2
    next_min1_c, next_min2_c = min1_c, min2_c
  end

  next_min1
end
```

## Scala

```scala
object Solution {
    def minFallingPathSum(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        if (n == 1) return grid(0)(0)

        var nextMin1 = Int.MaxValue
        var nextMin2 = Int.MaxValue
        var nextMin1Idx = -1
        var nextMin2Idx = -1

        // Initialize with the last row
        for (c <- 0 until n) {
            val v = grid(n - 1)(c)
            if (v <= nextMin1) {
                nextMin2 = nextMin1
                nextMin2Idx = nextMin1Idx
                nextMin1 = v
                nextMin1Idx = c
            } else if (v <= nextMin2) {
                nextMin2 = v
                nextMin2Idx = c
            }
        }

        // Process rows from bottom-2 up to top
        for (row <- (n - 2) to 0 by -1) {
            var curMin1 = Int.MaxValue
            var curMin2 = Int.MaxValue
            var curMin1Idx = -1
            var curMin2Idx = -1

            for (c <- 0 until n) {
                val add = if (c != nextMin1Idx) nextMin1 else nextMin2
                val value = grid(row)(c) + add

                if (value <= curMin1) {
                    curMin2 = curMin1
                    curMin2Idx = curMin1Idx
                    curMin1 = value
                    curMin1Idx = c
                } else if (value <= curMin2) {
                    curMin2 = value
                    curMin2Idx = c
                }
            }

            nextMin1 = curMin1
            nextMin1Idx = curMin1Idx
            nextMin2 = curMin2
            nextMin2Idx = curMin2Idx
        }

        nextMin1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 0 {
            return 0;
        }
        // Initialize minima for the last row
        let mut next_min1_val = i32::MAX;
        let mut next_min2_val = i32::MAX;
        let mut next_min1_c = n; // sentinel out of range
        let mut next_min2_c = n;

        for col in 0..n {
            let v = grid[n - 1][col];
            if v <= next_min1_val {
                next_min2_val = next_min1_val;
                next_min2_c = next_min1_c;
                next_min1_val = v;
                next_min1_c = col;
            } else if v <= next_min2_val {
                next_min2_val = v;
                next_min2_c = col;
            }
        }

        if n == 1 {
            return next_min1_val;
        }

        // Process rows from second last up to the first
        for row in (0..n - 1).rev() {
            let mut cur_min1_val = i32::MAX;
            let mut cur_min2_val = i32::MAX;
            let mut cur_min1_c = n;
            let mut cur_min2_c = n;

            for col in 0..n {
                let add = if col != next_min1_c { next_min1_val } else { next_min2_val };
                let v = grid[row][col] + add;
                if v <= cur_min1_val {
                    cur_min2_val = cur_min1_val;
                    cur_min2_c = cur_min1_c;
                    cur_min1_val = v;
                    cur_min1_c = col;
                } else if v <= cur_min2_val {
                    cur_min2_val = v;
                    cur_min2_c = col;
                }
            }

            next_min1_val = cur_min1_val;
            next_min2_val = cur_min2_val;
            next_min1_c = cur_min1_c;
            next_min2_c = cur_min2_c;
        }

        next_min1_val
    }
}
```

## Racket

```racket
(define/contract (min-falling-path-sum grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((INF 1000000000)
         (n   (length grid))
         (vec-grid (list->vector (map list->vector grid))))
    (if (= n 0)
        0
        (begin
          ;; helper: find min and second min in a vector
          (define (scan-row vec)
            (let recur ((i 0) (min1 INF) (c1 -1) (min2 INF) (c2 -1))
              (if (= i n)
                  (list min1 c1 min2 c2)
                  (let* ((val (vector-ref vec i))
                         (new-values
                          (cond [(<= val min1) (values val i min1 c1)]
                                [(<= val min2) (values min1 c1 val i)]
                                [else            (values min1 c1 min2 c2)])))
                    (call-with-values (lambda () new-values)
                      (lambda (new-min1 new-c1 new-min2 new-c2)
                        (recur (+ i 1) new-min1 new-c1 new-min2 new-c2)))))))

          ;; initialise with the last row
          (let* ((last-vec (vector-ref vec-grid (- n 1)))
                 (init     (scan-row last-vec))
                 (next-min1   (list-ref init 0))
                 (next-min1-c (list-ref init 1))
                 (next-min2   (list-ref init 2))
                 (next-min2-c (list-ref init 3)))

            ;; process rows from bottom‑1 up to the first row
            (let rec ((row (- n 2))
                     (nm1 next-min1) (nc1 next-min1-c)
                     (nm2 next-min2) (nc2 next-min2-c))
              (if (< row 0)
                  nm1                                   ; answer is min of first row
                  (let* ((vec (vector-ref vec-grid row))
                         ;; compute min / second min for this row using mins from the row below
                         (cur (let recur2 ((i 0) (min1 INF) (c1 -1) (min2 INF) (c2 -1))
                                (if (= i n)
                                    (list min1 c1 min2 c2)
                                    (let* ((val   (vector-ref vec i))
                                           (add   (if (= i nc1) nm2 nm1))
                                           (total (+ val add)))
                                      (cond [(<= total min1) (recur2 (+ i 1) total i min1 c1)]
                                            [(<= total min2) (recur2 (+ i 1) min1 c1 total i)]
                                            [else            (recur2 (+ i 1) min1 c1 min2 c2)]))))))
                    (rec (- row 1)
                         (list-ref cur 0) (list-ref cur 1)
                         (list-ref cur 2) (list-ref cur 3)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_falling_path_sum/1]).

-spec min_falling_path_sum(Grid :: [[integer()]]) -> integer().
min_falling_path_sum(Grid) ->
    case Grid of
        [] -> 0;
        [Row] -> hd(Row);
        _ ->
            N = length(Grid),
            LastRow = lists:last(Grid),
            IndexedLast = lists:zip(lists:seq(0, N - 1), LastRow),
            {Min1V, Min1I, Min2V, Min2I} = find_two_min(IndexedLast),
            RowsToProcess = lists:reverse(lists:sublist(Grid, N - 1)),
            process_rows(RowsToProcess, Min1V, Min1I, Min2V, Min2I)
    end.

find_two_min(Pairs) ->
    find_two_min(Pairs, undefined, undefined, undefined, undefined).

find_two_min([], Min1V, Min1I, Min2V, Min2I) ->
    {Min1V, Min1I, Min2V, Min2I};
find_two_min([{Idx, Val} | Rest], undefined, _, undefined, _) ->
    find_two_min(Rest, Val, Idx, undefined, undefined);
find_two_min([{Idx, Val} | Rest], Min1V, Min1I, Min2V, Min2I) ->
    if
        Val =< Min1V ->
            NewMin2V = Min1V,
            NewMin2I = Min1I,
            find_two_min(Rest, Val, Idx, NewMin2V, NewMin2I);
        (Min2V == undefined) orelse (Val =< Min2V) ->
            find_two_min(Rest, Min1V, Min1I, Val, Idx);
        true ->
            find_two_min(Rest, Min1V, Min1I, Min2V, Min2I)
    end.

process_rows([], Min1V, _Min1I, _Min2V, _Min2I) -> Min1V;
process_rows([Row | Rest], NextMin1V, NextMin1I, NextMin2V, NextMin2I) ->
    {CurMin1V, CurMin1I, CurMin2V, CurMin2I} =
        compute_row_mins(Row, NextMin1V, NextMin1I, NextMin2V, NextMin2I),
    process_rows(Rest, CurMin1V, CurMin1I, CurMin2V, CurMin2I).

compute_row_mins(Row, NM1V, NM1I, NM2V, NM2I) ->
    compute_row_mins(
        lists:zip(lists:seq(0, length(Row) - 1), Row),
        undefined, undefined, undefined, undefined,
        NM1V, NM1I, NM2V, NM2I).

compute_row_mins([], Min1V, Min1I, Min2V, Min2I, _NM1V, _NM1I, _NM2V, _NM2I) ->
    {Min1V, Min1I, Min2V, Min2I};
compute_row_mins([{Idx, Val} | Rest],
                 undefined, _, undefined, _,
                 NM1V, NM1I, NM2V, NM2I) ->
    NewVal = if Idx =/= NM1I -> Val + NM1V; true -> Val + NM2V end,
    compute_row_mins(Rest, NewVal, Idx, undefined, undefined,
                     NM1V, NM1I, NM2V, NM2I);
compute_row_mins([{Idx, Val} | Rest],
                 Min1V, Min1I, Min2V, Min2I,
                 NM1V, NM1I, NM2V, NM2I) ->
    NewVal = if Idx =/= NM1I -> Val + NM1V; true -> Val + NM2V end,
    if
        NewVal =< Min1V ->
            compute_row_mins(Rest, NewVal, Idx, Min1V, Min1I,
                             NM1V, NM1I, NM2V, NM2I);
        (Min2V == undefined) orelse (NewVal =< Min2V) ->
            compute_row_mins(Rest, Min1V, Min1I, NewVal, Idx,
                             NM1V, NM1I, NM2V, NM2I);
        true ->
            compute_row_mins(Rest, Min1V, Min1I, Min2V, Min2I,
                             NM1V, NM1I, NM2V, NM2I)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_falling_path_sum(grid :: [[integer]]) :: integer
  def min_falling_path_sum(grid) do
    n = length(grid)

    # Initialize mins from the last row
    {next_min1_val, next_min1_idx, next_min2_val, next_min2_idx} =
      Enum.reduce(Enum.with_index(List.last(grid)), {nil, nil, nil, nil}, fn {val, idx},
          {m1v, m1i, m2v, m2i} ->
        cond do
          m1v == nil or val <= m1v ->
            {val, idx, m1v, m1i}
          m2v == nil or val <= m2v ->
            {m1v, m1i, val, idx}
          true ->
            {m1v, m1i, m2v, m2i}
        end
      end)

    rows =
      if n > 1 do
        0..(n - 2) |> Enum.to_list() |> Enum.reverse()
      else
        []
      end

    {final_min, _, _, _} =
      Enum.reduce(rows, {next_min1_val, next_min1_idx, next_min2_val, next_min2_idx},
        fn row_idx,
           {nm1v, nm1i, nm2v, nm2i} ->

          row = Enum.at(grid, row_idx)

          {cur_m1v, cur_m1i, cur_m2v, cur_m2i} =
            Enum.reduce(Enum.with_index(row), {nil, nil, nil, nil}, fn {val, col},
                {c1v, c1i, c2v, c2i} ->

              add = if col != nm1i, do: nm1v, else: nm2v
              total = val + add

              cond do
                c1v == nil or total <= c1v ->
                  {total, col, c1v, c1i}
                c2v == nil or total <= c2v ->
                  {c1v, c1i, total, col}
                true ->
                  {c1v, c1i, c2v, c2i}
              end
            end)

          {cur_m1v, cur_m1i, cur_m2v, cur_m2i}
        end)

    final_min
  end
end
```

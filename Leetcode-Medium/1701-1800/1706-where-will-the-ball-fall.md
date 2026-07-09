# 1706. Where Will the Ball Fall

## Cpp

```cpp
class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> result(n, -1);
        for (int start = 0; start < n; ++start) {
            int col = start;
            bool stuck = false;
            for (int row = 0; row < m; ++row) {
                int dir = grid[row][col];
                int nextCol = col + dir;
                // Check boundaries and V shape
                if (nextCol < 0 || nextCol >= n || grid[row][nextCol] != dir) {
                    stuck = true;
                    break;
                }
                col = nextCol;
            }
            if (!stuck) result[start] = col;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] findBall(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] ans = new int[n];
        for (int start = 0; start < n; ++start) {
            int col = start;
            boolean stuck = false;
            for (int row = 0; row < m; ++row) {
                int dir = grid[row][col];
                int nextCol = col + dir;
                if (nextCol < 0 || nextCol >= n || grid[row][nextCol] != dir) {
                    stuck = true;
                    break;
                }
                col = nextCol;
            }
            ans[start] = stuck ? -1 : col;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        result = []
        for start in range(n):
            col = start
            stuck = False
            for row in range(m):
                direction = grid[row][col]
                next_col = col + direction
                # check bounds and V shape
                if next_col < 0 or next_col >= n or grid[row][next_col] != direction:
                    stuck = True
                    break
                col = next_col
            result.append(-1 if stuck else col)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = []
        for start in range(n):
            col = start
            stuck = False
            for row in range(m):
                direction = grid[row][col]
                next_col = col + direction
                # Check wall collision
                if next_col < 0 or next_col >= n:
                    stuck = True
                    break
                # Check V shape (adjacent board must have same direction)
                if grid[row][next_col] != direction:
                    stuck = True
                    break
                col = next_col
            result.append(-1 if stuck else col)
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findBall(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    int m = gridSize;
    int n = gridColSize[0];
    *returnSize = n;
    int *ans = (int *)malloc(n * sizeof(int));
    
    for (int start = 0; start < n; ++start) {
        int c = start;
        int r;
        for (r = 0; r < m; ++r) {
            int dir = grid[r][c];
            int nc = c + dir;
            if (nc < 0 || nc >= n) {          // hits wall
                break;
            }
            if (grid[r][nc] != dir) {         // V-shaped trap
                break;
            }
            c = nc;                           // move to next column
        }
        ans[start] = (r == m) ? c : -1;
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindBall(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] answer = new int[n];
        
        for (int startCol = 0; startCol < n; startCol++) {
            int col = startCol;
            bool stuck = false;
            
            for (int row = 0; row < m; row++) {
                int dir = grid[row][col];
                int nextCol = col + dir;
                
                // Check wall collision
                if (nextCol < 0 || nextCol >= n) {
                    stuck = true;
                    break;
                }
                // Check V shape (adjacent board must have same direction)
                if (grid[row][nextCol] != dir) {
                    stuck = true;
                    break;
                }
                
                col = nextCol; // move to next column
            }
            
            answer[startCol] = stuck ? -1 : col;
        }
        
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findBall = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const ans = new Array(n);
    
    for (let start = 0; start < n; ++start) {
        let col = start;
        for (let row = 0; row < m; ++row) {
            const dir = grid[row][col];
            const nextCol = col + dir;
            // check bounds and V-shaped trap
            if (nextCol < 0 || nextCol >= n || grid[row][nextCol] !== dir) {
                col = -1;
                break;
            }
            col = nextCol;
        }
        ans[start] = col;
    }
    
    return ans;
};
```

## Typescript

```typescript
function findBall(grid: number[][]): number[] {
    const m = grid.length;
    const n = grid[0].length;
    const ans = new Array<number>(n).fill(-1);
    for (let start = 0; start < n; ++start) {
        let col = start;
        let row = 0;
        while (row < m) {
            const dir = grid[row][col];
            const nextCol = col + dir;
            if (
                nextCol < 0 ||
                nextCol >= n ||
                grid[row][nextCol] !== dir
            ) {
                col = -1;
                break;
            }
            col = nextCol;
            row++;
        }
        ans[start] = col;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function findBall($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $result = [];

        for ($startCol = 0; $startCol < $n; $startCol++) {
            $col = $startCol;
            $row = 0;

            while ($row < $m) {
                $dir = $grid[$row][$col];
                $nextCol = $col + $dir;

                // Check wall collision
                if ($nextCol < 0 || $nextCol >= $n) {
                    $col = -1;
                    break;
                }

                // Check V-shaped trap
                if ($grid[$row][$nextCol] != $dir) {
                    $col = -1;
                    break;
                }

                // Move ball to next position
                $col = $nextCol;
                $row++;
            }

            $result[] = $col;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findBall(_ grid: [[Int]]) -> [Int] {
        let m = grid.count
        guard m > 0 else { return [] }
        let n = grid[0].count
        var result = Array(repeating: -1, count: n)
        
        for start in 0..<n {
            var col = start
            var stuck = false
            
            for row in 0..<m {
                let dir = grid[row][col]
                let nextCol = col + dir
                // Check bounds and V-shaped trap
                if nextCol < 0 || nextCol >= n || grid[row][nextCol] != dir {
                    stuck = true
                    break
                }
                col = nextCol
            }
            
            if !stuck {
                result[start] = col
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findBall(grid: Array<IntArray>): IntArray {
        val m = grid.size
        val n = grid[0].size
        val result = IntArray(n) { -1 }
        for (start in 0 until n) {
            var col = start
            var stuck = false
            for (row in 0 until m) {
                val dir = grid[row][col]
                val nextCol = col + dir
                if (nextCol < 0 || nextCol >= n || grid[row][nextCol] != dir) {
                    stuck = true
                    break
                }
                col = nextCol
            }
            if (!stuck) result[start] = col
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findBall(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<int> result = List.filled(n, -1);
    for (int start = 0; start < n; ++start) {
      int col = start;
      bool stuck = false;
      for (int row = 0; row < m; ++row) {
        int dir = grid[row][col];
        int nextCol = col + dir;
        if (nextCol < 0 || nextCol >= n || grid[row][nextCol] != dir) {
          stuck = true;
          break;
        }
        col = nextCol;
      }
      if (!stuck) result[start] = col;
    }
    return result;
  }
}
```

## Golang

```go
func findBall(grid [][]int) []int {
	m := len(grid)
	n := len(grid[0])
	result := make([]int, n)
	for start := 0; start < n; start++ {
		col := start
		stuck := false
		for row := 0; row < m; row++ {
			dir := grid[row][col]
			nextCol := col + dir
			if nextCol < 0 || nextCol >= n || grid[row][nextCol] != dir {
				stuck = true
				break
			}
			col = nextCol
		}
		if stuck {
			result[start] = -1
		} else {
			result[start] = col
		}
	}
	return result
}
```

## Ruby

```ruby
def find_ball(grid)
  m = grid.size
  n = grid[0].size
  result = Array.new(n, -1)

  (0...n).each do |c|
    col = c
    stuck = false

    (0...m).each do |row|
      dir = grid[row][col]
      next_col = col + dir
      if next_col < 0 || next_col >= n || grid[row][next_col] != dir
        stuck = true
        break
      end
      col = next_col
    end

    result[c] = stuck ? -1 : col
  end

  result
end
```

## Scala

```scala
object Solution {
    def findBall(grid: Array[Array[Int]]): Array[Int] = {
        val m = grid.length
        val n = grid(0).length
        val result = new Array[Int](n)

        for (startCol <- 0 until n) {
            var col = startCol
            var row = 0
            var stuck = false

            while (row < m && !stuck) {
                val dir = grid(row)(col)
                val nextCol = col + dir
                if (nextCol < 0 || nextCol >= n || grid(row)(nextCol) != dir) {
                    stuck = true
                } else {
                    col = nextCol
                    row += 1
                }
            }

            result(startCol) = if (stuck) -1 else col
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_ball(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        if m == 0 {
            return vec![];
        }
        let n = grid[0].len();
        let mut ans = vec![-1; n];
        for start in 0..n {
            let mut col: i32 = start as i32;
            for row in 0..m {
                let dir = grid[row][col as usize];
                let next_col = col + dir;
                if next_col < 0 || next_col >= n as i32 {
                    col = -1;
                    break;
                }
                if grid[row][next_col as usize] != dir {
                    col = -1;
                    break;
                }
                col = next_col;
            }
            ans[start] = col;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-ball grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((m (length grid))
         (n (if (zero? m) 0 (length (first grid))))
         (get-cell (lambda (i j) (list-ref (list-ref grid i) j)))
         (simulate
          (lambda (start-col)
            (let loop ((row 0) (col start-col))
              (if (= row m)
                  col
                  (let* ((dir (get-cell row col))
                         (next (+ col dir)))
                    (cond
                      [(or (< next 0) (>= next n)) -1]
                      [(not (= (get-cell row next) dir)) -1]
                      [else (loop (+ row 1) next)])))))))
    (build-list n simulate)))
```

## Erlang

```erlang
-module(solution).
-export([find_ball/1]).
-spec find_ball([[integer()]]) -> [integer()].
find_ball(Grid) ->
    N = length(hd(Grid)),
    lists:map(fun(Col) -> simulate(Grid, 0, Col) end,
              lists:seq(0, N - 1)).

simulate(_Grid, Row, _Col) when Row == length(_Grid) ->
    _Col;
simulate(Grid, Row, Col) ->
    Dir = get_elem(Grid, Row, Col),
    case Dir of
        1 ->
            NextCol = Col + 1,
            if NextCol >= length(hd(Grid)) ->
                    -1;
               true ->
                    NextDir = get_elem(Grid, Row, NextCol),
                    if NextDir == 1 ->
                            simulate(Grid, Row + 1, NextCol);
                       true ->
                            -1
                    end
            end;
        -1 ->
            NextCol = Col - 1,
            if NextCol < 0 ->
                    -1;
               true ->
                    NextDir = get_elem(Grid, Row, NextCol),
                    if NextDir == -1 ->
                            simulate(Grid, Row + 1, NextCol);
                       true ->
                            -1
                    end
            end
    end.

get_elem(Grid, RowIdx, ColIdx) ->
    Row = lists:nth(RowIdx + 1, Grid),
    lists:nth(ColIdx + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_ball(grid :: [[integer]]) :: [integer]
  def find_ball(grid) do
    m = length(grid)
    n = grid |> hd() |> length()

    Enum.map(0..(n - 1), fn start_col ->
      Enum.reduce_while(0..(m - 1), start_col, fn row, col ->
        dir = get_cell(grid, row, col)
        next_col = col + dir

        cond do
          next_col < 0 or next_col >= n ->
            {:halt, -1}

          get_cell(grid, row, next_col) != dir ->
            {:halt, -1}

          true ->
            {:cont, next_col}
        end
      end)
    end)
  end

  defp get_cell(grid, row, col) do
    grid |> Enum.at(row) |> Enum.at(col)
  end
end
```

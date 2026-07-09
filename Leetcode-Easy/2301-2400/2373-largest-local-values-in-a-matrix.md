# 2373. Largest Local Values in a Matrix

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> res(n - 2, vector<int>(n - 2));
        for (int i = 0; i <= n - 3; ++i) {
            for (int j = 0; j <= n - 3; ++j) {
                int mx = 0;
                for (int di = 0; di < 3; ++di) {
                    for (int dj = 0; dj < 3; ++dj) {
                        mx = max(mx, grid[i + di][j + dj]);
                    }
                }
                res[i][j] = mx;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] largestLocal(int[][] grid) {
        int n = grid.length;
        int m = n - 2;
        int[][] res = new int[m][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                int maxVal = 0;
                for (int di = 0; di < 3; di++) {
                    for (int dj = 0; dj < 3; dj++) {
                        int val = grid[i + di][j + dj];
                        if (val > maxVal) {
                            maxVal = val;
                        }
                    }
                }
                res[i][j] = maxVal;
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                mx = 0
                for x in range(i, i + 3):
                    row = grid[x]
                    for y in range(j, j + 3):
                        if row[y] > mx:
                            mx = row[y]
                res[i][j] = mx
        return res
```

## Python3

```python
class Solution:
    def largestLocal(self, grid):
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                mx = 0
                for x in range(i, i + 3):
                    row_max = max(grid[x][j:j + 3])
                    if row_max > mx:
                        mx = row_max
                ans[i][j] = mx
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** largestLocal(int** grid, int gridSize, int* gridColSize, int* returnSize, int*** returnColumnSizes) {
    int n = gridSize;
    int newSize = n - 2;
    *returnSize = newSize;

    // Allocate column sizes array
    int* colSizes = (int*)malloc(newSize * sizeof(int));
    for (int i = 0; i < newSize; ++i) {
        colSizes[i] = newSize;
    }
    *returnColumnSizes = &colSizes;

    // Allocate result matrix
    int** res = (int**)malloc(newSize * sizeof(int*));
    for (int i = 0; i < newSize; ++i) {
        res[i] = (int*)malloc(newSize * sizeof(int));
    }

    // Compute largest local values
    for (int i = 0; i < newSize; ++i) {
        for (int j = 0; j < newSize; ++j) {
            int maxVal = grid[i][j];
            for (int di = 0; di < 3; ++di) {
                for (int dj = 0; dj < 3; ++dj) {
                    int val = grid[i + di][j + dj];
                    if (val > maxVal) {
                        maxVal = val;
                    }
                }
            }
            res[i][j] = maxVal;
        }
    }

    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] LargestLocal(int[][] grid)
    {
        int n = grid.Length;
        int m = n - 2;
        int[][] maxLocal = new int[m][];
        for (int i = 0; i < m; i++)
        {
            maxLocal[i] = new int[m];
            for (int j = 0; j < m; j++)
            {
                int maxVal = 0;
                for (int di = 0; di < 3; di++)
                {
                    for (int dj = 0; dj < 3; dj++)
                    {
                        int val = grid[i + di][j + dj];
                        if (val > maxVal) maxVal = val;
                    }
                }
                maxLocal[i][j] = maxVal;
            }
        }
        return maxLocal;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var largestLocal = function(grid) {
    const n = grid.length;
    const m = n - 2;
    const result = Array.from({ length: m }, () => new Array(m));
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++) {
            let maxVal = -Infinity;
            for (let di = 0; di < 3; di++) {
                for (let dj = 0; dj < 3; dj++) {
                    const val = grid[i + di][j + dj];
                    if (val > maxVal) maxVal = val;
                }
            }
            result[i][j] = maxVal;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function largestLocal(grid: number[][]): number[][] {
    const n = grid.length;
    const result: number[][] = Array.from({ length: n - 2 }, () => new Array(n - 2).fill(0));
    for (let i = 0; i < n - 2; i++) {
        for (let j = 0; j < n - 2; j++) {
            let maxVal = -Infinity;
            for (let di = 0; di < 3; di++) {
                for (let dj = 0; dj < 3; dj++) {
                    const val = grid[i + di][j + dj];
                    if (val > maxVal) maxVal = val;
                }
            }
            result[i][j] = maxVal;
        }
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function largestLocal($grid) {
        $n = count($grid);
        $size = $n - 2;
        $result = [];
        for ($i = 0; $i < $size; $i++) {
            $row = [];
            for ($j = 0; $j < $size; $j++) {
                $maxVal = 0;
                for ($di = 0; $di < 3; $di++) {
                    for ($dj = 0; $dj < 3; $dj++) {
                        $val = $grid[$i + $di][$j + $dj];
                        if ($val > $maxVal) {
                            $maxVal = $val;
                        }
                    }
                }
                $row[] = $maxVal;
            }
            $result[] = $row;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func largestLocal(_ grid: [[Int]]) -> [[Int]] {
        let n = grid.count
        var result = Array(repeating: Array(repeating: 0, count: n - 2), count: n - 2)
        for i in 0..<(n - 2) {
            for j in 0..<(n - 2) {
                var maxVal = 0
                for di in 0...2 {
                    for dj in 0...2 {
                        let val = grid[i + di][j + dj]
                        if val > maxVal {
                            maxVal = val
                        }
                    }
                }
                result[i][j] = maxVal
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestLocal(grid: Array<IntArray>): Array<IntArray> {
        val n = grid.size
        val m = n - 2
        val ans = Array(m) { IntArray(m) }
        for (i in 0 until m) {
            for (j in 0 until m) {
                var maxVal = 0
                for (di in 0..2) {
                    for (dj in 0..2) {
                        val v = grid[i + di][j + dj]
                        if (v > maxVal) maxVal = v
                    }
                }
                ans[i][j] = maxVal
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> largestLocal(List<List<int>> grid) {
    int n = grid.length;
    List<List<int>> result = List.generate(n - 2, (_) => List.filled(n - 2, 0));
    for (int i = 0; i < n - 2; ++i) {
      for (int j = 0; j < n - 2; ++j) {
        int maxVal = 0;
        for (int di = 0; di < 3; ++di) {
          for (int dj = 0; dj < 3; ++dj) {
            int val = grid[i + di][j + dj];
            if (val > maxVal) {
              maxVal = val;
            }
          }
        }
        result[i][j] = maxVal;
      }
    }
    return result;
  }
}
```

## Golang

```go
func largestLocal(grid [][]int) [][]int {
    n := len(grid)
    size := n - 2
    res := make([][]int, size)
    for i := 0; i < size; i++ {
        row := make([]int, size)
        for j := 0; j < size; j++ {
            maxVal := 0
            for x := i; x < i+3; x++ {
                for y := j; y < j+3; y++ {
                    if grid[x][y] > maxVal {
                        maxVal = grid[x][y]
                    }
                }
            }
            row[j] = maxVal
        }
        res[i] = row
    }
    return res
}
```

## Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer[][]}
def largest_local(grid)
  n = grid.length
  size = n - 2
  result = Array.new(size) { Array.new(size, 0) }

  (0...size).each do |i|
    (0...size).each do |j|
      max_val = 0
      (i..i+2).each do |x|
        (j..j+2).each do |y|
          val = grid[x][y]
          max_val = val if val > max_val
        end
      end
      result[i][j] = max_val
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def largestLocal(grid: Array[Array[Int]]): Array[Array[Int]] = {
        val n = grid.length
        val m = n - 2
        val res = Array.ofDim[Int](m, m)
        var i = 0
        while (i < m) {
            var j = 0
            while (j < m) {
                var maxVal = Int.MinValue
                var di = 0
                while (di < 3) {
                    var dj = 0
                    while (dj < 3) {
                        val v = grid(i + di)(j + dj)
                        if (v > maxVal) maxVal = v
                        dj += 1
                    }
                    di += 1
                }
                res(i)(j) = maxVal
                j += 1
            }
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        if n < 3 {
            return vec![];
        }
        let m = n - 2;
        let mut result = vec![vec![0; m]; m];
        for i in 0..m {
            for j in 0..m {
                let mut max_val = i32::MIN;
                for di in 0..3 {
                    for dj in 0..3 {
                        let val = grid[i + di][j + dj];
                        if val > max_val {
                            max_val = val;
                        }
                    }
                }
                result[i][j] = max_val;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (largest-local grid)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let* ((n (length grid))
         (m (- n 2)))
    (for/list ([i (in-range m)])
      (for/list ([j (in-range m)])
        (let ((sub-values
               (for*/list ([di (in-range 3)]
                           [dj (in-range 3)])
                 (list-ref (list-ref grid (+ i di)) (+ j dj)))))
          (apply max sub-values))))))
```

## Erlang

```erlang
-spec largest_local(Grid :: [[integer()]]) -> [[integer()]].
largest_local(Grid) ->
    N = length(Grid),
    M = N - 2,
    generate_rows(0, M, Grid).

generate_rows(I, M, _Grid) when I >= M -> [];
generate_rows(I, M, Grid) ->
    Row = generate_cols(0, M, I, Grid),
    [Row | generate_rows(I + 1, M, Grid)].

generate_cols(J, M, _I, _Grid) when J >= M -> [];
generate_cols(J, M, I, Grid) ->
    Max = max_in_window(I, J, Grid),
    [Max | generate_cols(J + 1, M, I, Grid)].

max_in_window(I, J, Grid) ->
    Row0 = lists:nth(I + 1, Grid),
    Row1 = lists:nth(I + 2, Grid),
    Row2 = lists:nth(I + 3, Grid),

    C0 = lists:nth(J + 1, Row0), C1 = lists:nth(J + 2, Row0), C2 = lists:nth(J + 3, Row0),
    D0 = lists:nth(J + 1, Row1), D1 = lists:nth(J + 2, Row1), D2 = lists:nth(J + 3, Row1),
    E0 = lists:nth(J + 1, Row2), E1 = lists:nth(J + 2, Row2), E2 = lists:nth(J + 3, Row2),

    max_list([C0, C1, C2, D0, D1, D2, E0, E1, E2]).

max_list([H|T]) -> max_list(T, H).
max_list([], Max) -> Max;
max_list([X|Xs], Max) when X > Max -> max_list(Xs, X);
max_list([_|Xs], Max) -> max_list(Xs, Max).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_local(grid :: [[integer]]) :: [[integer]]
  def largest_local(grid) do
    n = length(grid)
    limit = n - 3

    for i <- 0..limit do
      for j <- 0..limit do
        values =
          for di <- 0..2, dj <- 0..2 do
            grid |> Enum.at(i + di) |> Enum.at(j + dj)
          end

        Enum.max(values)
      end
    end
  end
end
```

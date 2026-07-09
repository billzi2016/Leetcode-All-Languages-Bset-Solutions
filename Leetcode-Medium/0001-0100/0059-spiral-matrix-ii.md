# 0059. Spiral Matrix II

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> matrix(n, vector<int>(n));
        int cnt = 1;
        int layers = (n + 1) / 2;
        for (int layer = 0; layer < layers; ++layer) {
            // top row
            for (int col = layer; col < n - layer; ++col)
                matrix[layer][col] = cnt++;
            // right column
            for (int row = layer + 1; row < n - layer; ++row)
                matrix[row][n - layer - 1] = cnt++;
            // bottom row
            if (n - layer - 1 != layer) {
                for (int col = n - layer - 2; col >= layer; --col)
                    matrix[n - layer - 1][col] = cnt++;
                // left column
                for (int row = n - layer - 2; row > layer; --row)
                    matrix[row][layer] = cnt++;
            }
        }
        return matrix;
    }
};
```

## Java

```java
class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int num = 1;
        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;

        while (top <= bottom && left <= right) {
            for (int col = left; col <= right; col++) {
                matrix[top][col] = num++;
            }
            top++;

            for (int row = top; row <= bottom; row++) {
                matrix[row][right] = num++;
            }
            right--;

            if (top <= bottom) {
                for (int col = right; col >= left; col--) {
                    matrix[bottom][col] = num++;
                }
                bottom--;
            }

            if (left <= right) {
                for (int row = bottom; row >= top; row--) {
                    matrix[row][left] = num++;
                }
                left++;
            }
        }

        return matrix;
    }
}
```

## Python

```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1

        while left <= right and top <= bottom:
            # left to right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # top to bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                # right to left
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            if left <= right:
                # bottom to top
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix
```

## Python3

```python
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generateMatrix(int n, int* returnSize, int*** returnColumnSizes) {
    int **matrix = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        matrix[i] = (int*)malloc(n * sizeof(int));
    }

    int top = 0, bottom = n - 1;
    int left = 0, right = n - 1;
    int num = 1, total = n * n;

    while (num <= total) {
        for (int col = left; col <= right && num <= total; ++col)
            matrix[top][col] = num++;
        ++top;

        for (int row = top; row <= bottom && num <= total; ++row)
            matrix[row][right] = num++;
        --right;

        for (int col = right; col >= left && num <= total; --col)
            matrix[bottom][col] = num++;
        --bottom;

        for (int row = bottom; row >= top && num <= total; --row)
            matrix[row][left] = num++;
        ++left;
    }

    *returnSize = n;
    *returnColumnSizes = (int**)malloc(sizeof(int*));
    (*returnColumnSizes)[0] = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        (*returnColumnSizes)[0][i] = n;
    }

    return matrix;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int[][] GenerateMatrix(int n) {
        int[][] matrix = new int[n][];
        for (int i = 0; i < n; i++) {
            matrix[i] = new int[n];
        }

        int left = 0, right = n - 1;
        int top = 0, bottom = n - 1;
        int num = 1;

        while (left <= right && top <= bottom) {
            // Move right
            for (int col = left; col <= right; col++) {
                matrix[top][col] = num++;
            }
            top++;

            // Move down
            for (int row = top; row <= bottom; row++) {
                matrix[row][right] = num++;
            }
            right--;

            // Move left
            if (top <= bottom) {
                for (int col = right; col >= left; col--) {
                    matrix[bottom][col] = num++;
                }
                bottom--;
            }

            // Move up
            if (left <= right) {
                for (int row = bottom; row >= top; row--) {
                    matrix[row][left] = num++;
                }
                left++;
            }
        }

        return matrix;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    const matrix = Array.from({ length: n }, () => Array(n).fill(0));
    let num = 1;
    let top = 0, bottom = n - 1, left = 0, right = n - 1;
    
    while (top <= bottom && left <= right) {
        // left to right
        for (let col = left; col <= right; col++) {
            matrix[top][col] = num++;
        }
        top++;
        
        // top to bottom
        for (let row = top; row <= bottom; row++) {
            matrix[row][right] = num++;
        }
        right--;
        
        // right to left
        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                matrix[bottom][col] = num++;
            }
            bottom--;
        }
        
        // bottom to top
        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                matrix[row][left] = num++;
            }
            left++;
        }
    }
    
    return matrix;
};
```

## Typescript

```typescript
function generateMatrix(n: number): number[][] {
    const matrix: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    let num = 1;
    let top = 0, bottom = n - 1, left = 0, right = n - 1;

    while (top <= bottom && left <= right) {
        for (let col = left; col <= right; col++) {
            matrix[top][col] = num++;
        }
        top++;

        for (let row = top; row <= bottom; row++) {
            matrix[row][right] = num++;
        }
        right--;

        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                matrix[bottom][col] = num++;
            }
            bottom--;
        }

        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                matrix[row][left] = num++;
            }
            left++;
        }
    }

    return matrix;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[][]
     */
    function generateMatrix($n) {
        $matrix = array_fill(0, $n, array_fill(0, $n, 0));
        $num = 1;
        $layers = intdiv($n + 1, 2);
        for ($layer = 0; $layer < $layers; $layer++) {
            // top row
            for ($col = $layer; $col < $n - $layer; $col++) {
                $matrix[$layer][$col] = $num++;
            }
            // right column
            for ($row = $layer + 1; $row < $n - $layer; $row++) {
                $matrix[$row][$n - $layer - 1] = $num++;
            }
            // bottom row (if not the same as top)
            if ($n - $layer - 1 != $layer) {
                for ($col = $n - $layer - 2; $col >= $layer; $col--) {
                    $matrix[$n - $layer - 1][$col] = $num++;
                }
                // left column (if not the same as right)
                for ($row = $n - $layer - 2; $row > $layer; $row--) {
                    $matrix[$row][$layer] = $num++;
                }
            }
        }
        return $matrix;
    }
}
```

## Swift

```swift
class Solution {
    func generateMatrix(_ n: Int) -> [[Int]] {
        var matrix = Array(repeating: Array(repeating: 0, count: n), count: n)
        var num = 1
        var top = 0
        var bottom = n - 1
        var left = 0
        var right = n - 1
        
        while top <= bottom && left <= right {
            // Left to Right
            for col in left...right {
                matrix[top][col] = num
                num += 1
            }
            top += 1
            if top > bottom { break }
            
            // Top to Bottom
            for row in top...bottom {
                matrix[row][right] = num
                num += 1
            }
            right -= 1
            if left > right { break }
            
            // Right to Left
            if top <= bottom {
                for col in stride(from: right, through: left, by: -1) {
                    matrix[bottom][col] = num
                    num += 1
                }
                bottom -= 1
            }
            if top > bottom { break }
            
            // Bottom to Top
            if left <= right {
                for row in stride(from: bottom, through: top, by: -1) {
                    matrix[row][left] = num
                    num += 1
                }
                left += 1
            }
        }
        
        return matrix
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun generateMatrix(n: Int): Array<IntArray> {
        val matrix = Array(n) { IntArray(n) }
        var num = 1
        val layers = (n + 1) / 2
        for (layer in 0 until layers) {
            // top row
            for (col in layer until n - layer) {
                matrix[layer][col] = num++
            }
            // right column
            for (row in layer + 1 until n - layer) {
                matrix[row][n - layer - 1] = num++
            }
            // bottom row
            if (layer != n - layer - 1) {
                for (col in n - layer - 2 downTo layer) {
                    matrix[n - layer - 1][col] = num++
                }
                // left column
                for (row in n - layer - 2 downTo layer + 1) {
                    matrix[row][layer] = num++
                }
            }
        }
        return matrix
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> generateMatrix(int n) {
    List<List<int>> matrix = List.generate(n, (_) => List.filled(n, 0));
    int top = 0, bottom = n - 1;
    int left = 0, right = n - 1;
    int num = 1;

    while (top <= bottom && left <= right) {
      // Left to Right
      for (int col = left; col <= right; ++col) {
        matrix[top][col] = num++;
      }
      top++;

      // Top to Bottom
      for (int row = top; row <= bottom; ++row) {
        matrix[row][right] = num++;
      }
      right--;

      if (top <= bottom) {
        // Right to Left
        for (int col = right; col >= left; --col) {
          matrix[bottom][col] = num++;
        }
        bottom--;
      }

      if (left <= right) {
        // Bottom to Top
        for (int row = bottom; row >= top; --row) {
          matrix[row][left] = num++;
        }
        left++;
      }
    }

    return matrix;
  }
}
```

## Golang

```go
func generateMatrix(n int) [][]int {
    matrix := make([][]int, n)
    for i := range matrix {
        matrix[i] = make([]int, n)
    }
    top, bottom := 0, n-1
    left, right := 0, n-1
    num := 1
    for top <= bottom && left <= right {
        // left to right
        for col := left; col <= right; col++ {
            matrix[top][col] = num
            num++
        }
        top++

        // top to bottom
        for row := top; row <= bottom; row++ {
            matrix[row][right] = num
            num++
        }
        right--

        if top <= bottom {
            // right to left
            for col := right; col >= left; col-- {
                matrix[bottom][col] = num
                num++
            }
            bottom--
        }

        if left <= right {
            // bottom to top
            for row := bottom; row >= top; row-- {
                matrix[row][left] = num
                num++
            }
            left++
        }
    }
    return matrix
}
```

## Ruby

```ruby
def generate_matrix(n)
  matrix = Array.new(n) { Array.new(n, 0) }
  num = 1
  top = 0
  bottom = n - 1
  left = 0
  right = n - 1

  while top <= bottom && left <= right
    (left..right).each do |col|
      matrix[top][col] = num
      num += 1
    end
    top += 1

    (top..bottom).each do |row|
      matrix[row][right] = num
      num += 1
    end
    right -= 1

    if top <= bottom
      right.downto(left) do |col|
        matrix[bottom][col] = num
        num += 1
      end
      bottom -= 1
    end

    if left <= right
      bottom.downto(top) do |row|
        matrix[row][left] = num
        num += 1
      end
      left += 1
    end
  end

  matrix
end
```

## Scala

```scala
object Solution {
  def generateMatrix(n: Int): Array[Array[Int]] = {
    val matrix = Array.ofDim[Int](n, n)
    var num = 1
    var top = 0
    var bottom = n - 1
    var left = 0
    var right = n - 1

    while (top <= bottom && left <= right) {
      // left to right
      for (j <- left to right) {
        matrix(top)(j) = num
        num += 1
      }
      top += 1

      // top to bottom
      for (i <- top to bottom) {
        matrix(i)(right) = num
        num += 1
      }
      right -= 1

      // right to left
      if (top <= bottom) {
        for (j <- right to left by -1) {
          matrix(bottom)(j) = num
          num += 1
        }
        bottom -= 1
      }

      // bottom to top
      if (left <= right) {
        for (i <- bottom to top by -1) {
          matrix(i)(left) = num
          num += 1
        }
        left += 1
      }
    }

    matrix
  }
}
```

## Rust

```rust
impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut mat = vec![vec![0i32; n]; n];
        let mut cnt = 1i32;
        let layers = (n + 1) / 2;
        for layer in 0..layers {
            // top row
            for col in layer..n - layer {
                mat[layer][col] = cnt;
                cnt += 1;
            }
            // right column
            for row in layer + 1..n - layer {
                mat[row][n - layer - 1] = cnt;
                cnt += 1;
            }
            // bottom row (if not the same as top)
            if n - layer - 1 != layer {
                for col in (layer..n - layer - 1).rev() {
                    mat[n - layer - 1][col] = cnt;
                    cnt += 1;
                }
                // left column
                for row in (layer + 1..n - layer - 1).rev() {
                    mat[row][layer] = cnt;
                    cnt += 1;
                }
            }
        }
        mat
    }
}
```

## Racket

```racket
(define/contract (generate-matrix n)
  (-> exact-integer? (listof (listof exact-integer?)))
  (let ((matrix (make-vector n))
        (cnt 1))
    ;; initialize rows
    (for ([i (in-range n)])
      (vector-set! matrix i (make-vector n 0)))
    (let loop ((layer 0))
      (when (< layer (quotient (+ n 1) 2))
        (define start layer)
        (define end (- n layer 1))
        ;; top row
        (for ([col (in-range start (+ end 1))])
          (vector-set! (vector-ref matrix start) col cnt)
          (set! cnt (+ cnt 1)))
        ;; right column
        (for ([row (in-range (+ start 1) (+ end 1))])
          (vector-set! (vector-ref matrix row) end cnt)
          (set! cnt (+ cnt 1)))
        ;; bottom row
        (when (> end start)
          (for ([col (in-range (- end 1) (sub1 start) -1)])
            (vector-set! (vector-ref matrix end) col cnt)
            (set! cnt (+ cnt 1))))
        ;; left column
        (when (> end start)
          (for ([row (in-range (- end 1) start -1)])
            (vector-set! (vector-ref matrix row) start cnt)
            (set! cnt (+ cnt 1))))
        (loop (+ layer 1))))
    (build-list n (lambda (i) (vector->list (vector-ref matrix i))))))
```

## Erlang

```erlang
-module(solution).
-export([generate_matrix/1]).

-spec generate_matrix(N :: integer()) -> [[integer()]].
generate_matrix(N) ->
    Positions = gen_positions(N),
    Map = maps:from_list([{Pos, Num} || {Num, Pos} <- lists:zip(lists:seq(1, N * N), Positions)]),
    [ [maps:get({Row, Col}, Map) || Col <- lists:seq(0, N - 1)]
      || Row <- lists:seq(0, N - 1) ].

gen_positions(N) ->
    gen_layers(0, N - 1, 0, N - 1).

gen_layers(Top, Bottom, Left, Right) when Top > Bottom; Left > Right ->
    [];
gen_layers(Top, Bottom, Left, Right) ->
    TopRow = [{Top, C} || C <- lists:seq(Left, Right)],
    RightCol = [{R, Right} || R <- lists:seq(Top + 1, Bottom)],
    BottomRow = if
        Top < Bottom -> [{Bottom, C} || C <- lists:seq(Right - 1, Left, -1)];
        true -> []
    end,
    LeftCol = if
        Left < Right -> [{R, Left} || R <- lists:seq(Bottom - 1, Top + 1, -1)];
        true -> []
    end,
    TopRow ++ RightCol ++ BottomRow ++ LeftCol ++ gen_layers(Top + 1, Bottom - 1, Left + 1, Right - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec generate_matrix(n :: integer) :: [[integer]]
  def generate_matrix(n) do
    dirs = [{0, 1}, {1, 0}, {0, -1}, {-1, 0}]
    total = n * n

    {filled_map, _, _, _} =
      Enum.reduce(1..total, {%{}, 0, 0, 0}, fn i, {m, r, c, d} ->
        m = Map.put(m, {r, c}, i)
        {dr, dc} = Enum.at(dirs, d)
        nr = r + dr
        nc = c + dc

        if nr < 0 or nr >= n or nc < 0 or nc >= n or Map.has_key?(m, {nr, nc}) do
          nd = rem(d + 1, 4)
          {ndr, ndc} = Enum.at(dirs, nd)
          {m, r + ndr, c + ndc, nd}
        else
          {m, nr, nc, d}
        end
      end)

    for row <- 0..(n - 1) do
      for col <- 0..(n - 1) do
        Map.get(filled_map, {row, col})
      end
    end
  end
end
```

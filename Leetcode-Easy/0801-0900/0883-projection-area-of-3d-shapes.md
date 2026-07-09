# 0883. Projection Area of 3D Shapes

## Cpp

```cpp
class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        int n = grid.size();
        int top = 0, side = 0, front = 0;
        vector<int> colMax(n, 0);
        for (int i = 0; i < n; ++i) {
            int rowMax = 0;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] > 0) ++top;
                rowMax = max(rowMax, grid[i][j]);
                colMax[j] = max(colMax[j], grid[i][j]);
            }
            side += rowMax;
        }
        for (int j = 0; j < n; ++j) front += colMax[j];
        return top + side + front;
    }
};
```

## Java

```java
class Solution {
    public int projectionArea(int[][] grid) {
        int n = grid.length;
        int top = 0, side = 0, front = 0;

        // Top view: count non-zero cells
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) top++;
            }
        }

        // Side view: max in each row
        for (int i = 0; i < n; i++) {
            int rowMax = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > rowMax) rowMax = grid[i][j];
            }
            side += rowMax;
        }

        // Front view: max in each column
        for (int j = 0; j < n; j++) {
            int colMax = 0;
            for (int i = 0; i < n; i++) {
                if (grid[i][j] > colMax) colMax = grid[i][j];
            }
            front += colMax;
        }

        return top + side + front;
    }
}
```

## Python

```python
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        top = 0
        side = 0
        front = [0] * n

        for i in range(n):
            row_max = 0
            for j in range(n):
                v = grid[i][j]
                if v:
                    top += 1
                row_max = max(row_max, v)
                front[j] = max(front[j], v)
            side += row_max

        return top + side + sum(front)
```

## Python3

```python
from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        top = 0
        side = 0
        front = 0
        
        # Top view: count of non-zero cells
        for i in range(n):
            row_max = 0
            for j in range(n):
                val = grid[i][j]
                if val:
                    top += 1
                if val > row_max:
                    row_max = val
            side += row_max
        
        # Front view: max of each column
        for j in range(n):
            col_max = 0
            for i in range(n):
                if grid[i][j] > col_max:
                    col_max = grid[i][j]
            front += col_max
        
        return top + side + front
```

## C

```c
int projectionArea(int** grid, int gridSize, int* gridColSize){
    int top = 0;
    int side = 0;
    int front = 0;
    int colMax[51] = {0}; // gridSize <= 50
    
    for (int i = 0; i < gridSize; ++i) {
        int rowMax = 0;
        for (int j = 0; j < gridColSize[i]; ++j) {
            int val = grid[i][j];
            if (val > 0) top++;
            if (val > rowMax) rowMax = val;
            if (val > colMax[j]) colMax[j] = val;
        }
        side += rowMax;
    }
    
    for (int j = 0; j < gridSize; ++j) {
        front += colMax[j];
    }
    
    return top + side + front;
}
```

## Csharp

```csharp
public class Solution {
    public int ProjectionArea(int[][] grid) {
        int n = grid.Length;
        int top = 0, side = 0, front = 0;

        // Top projection: count non-zero cells
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) top++;
            }
        }

        // Side projection: max in each row
        for (int i = 0; i < n; i++) {
            int rowMax = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > rowMax) rowMax = grid[i][j];
            }
            side += rowMax;
        }

        // Front projection: max in each column
        for (int j = 0; j < n; j++) {
            int colMax = 0;
            for (int i = 0; i < n; i++) {
                if (grid[i][j] > colMax) colMax = grid[i][j];
            }
            front += colMax;
        }

        return top + side + front;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var projectionArea = function(grid) {
    const n = grid.length;
    let top = 0, side = 0, front = 0;
    
    // Top view: count non-zero cells
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] > 0) top++;
        }
    }
    
    // Side view (yz plane): max in each row
    for (let i = 0; i < n; ++i) {
        let rowMax = 0;
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] > rowMax) rowMax = grid[i][j];
        }
        side += rowMax;
    }
    
    // Front view (zx plane): max in each column
    for (let j = 0; j < n; ++j) {
        let colMax = 0;
        for (let i = 0; i < n; ++i) {
            if (grid[i][j] > colMax) colMax = grid[i][j];
        }
        front += colMax;
    }
    
    return top + side + front;
};
```

## Typescript

```typescript
function projectionArea(grid: number[][]): number {
    const n = grid.length;
    let top = 0;
    let side = 0;
    let front = 0;

    for (let i = 0; i < n; ++i) {
        let rowMax = 0;
        for (let j = 0; j < n; ++j) {
            const v = grid[i][j];
            if (v > 0) top++;
            if (v > rowMax) rowMax = v;
        }
        side += rowMax;
    }

    for (let j = 0; j < n; ++j) {
        let colMax = 0;
        for (let i = 0; i < n; ++i) {
            const v = grid[i][j];
            if (v > colMax) colMax = v;
        }
        front += colMax;
    }

    return top + side + front;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function projectionArea($grid) {
        $n = count($grid);
        $top = 0;
        $side = 0;
        $colMax = array_fill(0, $n, 0);

        for ($i = 0; $i < $n; $i++) {
            $rowMax = 0;
            for ($j = 0; $j < $n; $j++) {
                $val = $grid[$i][$j];
                if ($val > 0) {
                    $top++;
                }
                if ($val > $rowMax) {
                    $rowMax = $val;
                }
                if ($val > $colMax[$j]) {
                    $colMax[$j] = $val;
                }
            }
            $side += $rowMax;
        }

        $front = array_sum($colMax);
        return $top + $side + $front;
    }
}
```

## Swift

```swift
class Solution {
    func projectionArea(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var top = 0
        var side = 0
        var front = Array(repeating: 0, count: n)
        
        for i in 0..<n {
            var rowMax = 0
            for j in 0..<n {
                let v = grid[i][j]
                if v > 0 { top += 1 }
                if v > rowMax { rowMax = v }
                if v > front[j] { front[j] = v }
            }
            side += rowMax
        }
        
        let frontSum = front.reduce(0, +)
        return top + side + frontSum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun projectionArea(grid: Array<IntArray>): Int {
        var top = 0
        var side = 0
        var front = 0
        val n = grid.size
        // side (row max) and top count
        for (i in 0 until n) {
            var rowMax = 0
            for (j in 0 until n) {
                val v = grid[i][j]
                if (v > 0) top++
                if (v > rowMax) rowMax = v
            }
            side += rowMax
        }
        // front (column max)
        for (j in 0 until n) {
            var colMax = 0
            for (i in 0 until n) {
                val v = grid[i][j]
                if (v > colMax) colMax = v
            }
            front += colMax
        }
        return top + side + front
    }
}
```

## Dart

```dart
class Solution {
  int projectionArea(List<List<int>> grid) {
    int n = grid.length;
    int top = 0;
    int side = 0;
    List<int> colMax = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int rowMax = 0;
      for (int j = 0; j < n; ++j) {
        int v = grid[i][j];
        if (v > 0) top++;
        if (v > rowMax) rowMax = v;
        if (v > colMax[j]) colMax[j] = v;
      }
      side += rowMax;
    }
    int front = colMax.reduce((a, b) => a + b);
    return top + side + front;
  }
}
```

## Golang

```go
func projectionArea(grid [][]int) int {
	n := len(grid)
	top, side := 0, 0
	colMax := make([]int, n)

	for i := 0; i < n; i++ {
		rowMax := 0
		for j := 0; j < n; j++ {
			val := grid[i][j]
			if val > 0 {
				top++
			}
			if val > rowMax {
				rowMax = val
			}
			if val > colMax[j] {
				colMax[j] = val
			}
		}
		side += rowMax
	}

	front := 0
	for _, v := range colMax {
		front += v
	}
	return top + side + front
}
```

## Ruby

```ruby
def projection_area(grid)
  n = grid.size
  top = 0
  side = 0
  front = Array.new(n, 0)

  grid.each do |row|
    max_row = 0
    row.each_with_index do |val, j|
      top += 1 if val > 0
      max_row = val if val > max_row
      front[j] = val if val > front[j]
    end
    side += max_row
  end

  top + side + front.sum
end
```

## Scala

```scala
object Solution {
    def projectionArea(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        var top = 0
        var side = 0
        val colMax = Array.fill(n)(0)
        for (i <- 0 until n) {
            var rowMax = 0
            for (j <- 0 until n) {
                val v = grid(i)(j)
                if (v > 0) top += 1
                if (v > rowMax) rowMax = v
                if (v > colMax(j)) colMax(j) = v
            }
            side += rowMax
        }
        val front = colMax.sum
        top + side + front
    }
}
```

## Rust

```rust
impl Solution {
    pub fn projection_area(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut col_max = vec![0i32; n];
        let mut top = 0i32;
        let mut side = 0i32;

        for row in &grid {
            let mut row_max = 0i32;
            for (j, &v) in row.iter().enumerate() {
                if v > 0 {
                    top += 1;
                }
                if v > row_max {
                    row_max = v;
                }
                if v > col_max[j] {
                    col_max[j] = v;
                }
            }
            side += row_max;
        }

        let front: i32 = col_max.iter().sum();
        top + side + front
    }
}
```

## Racket

```racket
#lang racket

(define/contract (projection-area grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (front (make-vector n 0))
         (top 0)
         (side 0))
    (for ([i (in-range n)])
      (let* ((row (list-ref grid i))
             (row-max 0))
        (for ([j (in-range n)])
          (let ((v (list-ref row j)))
            (when (> v 0) (set! top (+ top 1)))
            (when (> v row-max) (set! row-max v))
            (let ((col-max (vector-ref front j)))
              (when (> v col-max)
                (vector-set! front j v)))))
        (set! side (+ side row-max))))
    (let ((front-sum 0))
      (for ([j (in-range n)])
        (set! front-sum (+ front-sum (vector-ref front j))))
      (+ top side front-sum))))
```

## Erlang

```erlang
-module(solution).
-export([projection_area/1]).

-spec projection_area(Grid :: [[integer()]]) -> integer().
projection_area(Grid) ->
    Top = count_nonzero(Grid, 0),
    Side = sum_row_max(Grid, 0),
    Front = sum_col_max(Grid),
    Top + Side + Front.

count_nonzero([], Acc) -> Acc;
count_nonzero([Row|Rest], Acc) ->
    NewAcc = lists:foldl(fun(V, A) -> if V > 0 -> A + 1; true -> A end end, Acc, Row),
    count_nonzero(Rest, NewAcc).

sum_row_max([], Acc) -> Acc;
sum_row_max([Row|Rest], Acc) ->
    Max = lists:max(Row),
    sum_row_max(Rest, Acc + Max).

sum_col_max([]) -> 0;
sum_col_max([FirstRow|Rest]) ->
    Maxes = lists:foldl(fun(Row, Acc) -> zip_max(Acc, Row) end, FirstRow, Rest),
    lists:sum(Maxes).

zip_max([], []) -> [];
zip_max([A|As], [B|Bs]) ->
    [erlang:max(A, B) | zip_max(As, Bs)].
```

## Elixir

```elixir
defmodule Solution do
  @spec projection_area(grid :: [[integer]]) :: integer
  def projection_area(grid) do
    top = Enum.reduce(grid, 0, fn row, acc -> acc + Enum.count(row, &(&1 > 0)) end)

    side = Enum.reduce(grid, 0, fn row, acc -> acc + Enum.max(row) end)

    n = length(grid)

    front =
      0..(n - 1)
      |> Enum.map(fn j ->
        grid
        |> Enum.map(&Enum.at(&1, j))
        |> Enum.max()
      end)
      |> Enum.sum()

    top + side + front
  end
end
```

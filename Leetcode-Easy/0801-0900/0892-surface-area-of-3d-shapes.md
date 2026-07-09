# 0892. Surface Area of 3D Shapes

## Cpp

```cpp
class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        int n = grid.size();
        int area = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int h = grid[i][j];
                if (h == 0) continue;
                // top and bottom
                area += 2;
                // north
                int up = (i > 0) ? grid[i-1][j] : 0;
                area += max(h - up, 0);
                // south
                int down = (i < n-1) ? grid[i+1][j] : 0;
                area += max(h - down, 0);
                // west
                int left = (j > 0) ? grid[i][j-1] : 0;
                area += max(h - left, 0);
                // east
                int right = (j < n-1) ? grid[i][j+1] : 0;
                area += max(h - right, 0);
            }
        }
        return area;
    }
};
```

## Java

```java
class Solution {
    public int surfaceArea(int[][] grid) {
        int n = grid.length;
        int area = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int h = grid[i][j];
                if (h > 0) {
                    // top and bottom
                    area += 2;
                    // north
                    int north = (i == 0) ? 0 : grid[i - 1][j];
                    area += Math.max(h - north, 0);
                    // south
                    int south = (i == n - 1) ? 0 : grid[i + 1][j];
                    area += Math.max(h - south, 0);
                    // west
                    int west = (j == 0) ? 0 : grid[i][j - 1];
                    area += Math.max(h - west, 0);
                    // east
                    int east = (j == n - 1) ? 0 : grid[i][j + 1];
                    area += Math.max(h - east, 0);
                }
            }
        }
        return area;
    }
}
```

## Python

```python
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v:
                    area += 2  # top and bottom
                    up = grid[i-1][j] if i > 0 else 0
                    down = grid[i+1][j] if i < n - 1 else 0
                    left = grid[i][j-1] if j > 0 else 0
                    right = grid[i][j+1] if j < n - 1 else 0
                    area += max(v - up, 0)
                    area += max(v - down, 0)
                    area += max(v - left, 0)
                    area += max(v - right, 0)
        return area
```

## Python3

```python
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h == 0:
                    continue
                # top and bottom
                area += 2
                # north
                neighbor = grid[i-1][j] if i > 0 else 0
                area += max(h - neighbor, 0)
                # south
                neighbor = grid[i+1][j] if i < n - 1 else 0
                area += max(h - neighbor, 0)
                # west
                neighbor = grid[i][j-1] if j > 0 else 0
                area += max(h - neighbor, 0)
                # east
                neighbor = grid[i][j+1] if j < n - 1 else 0
                area += max(h - neighbor, 0)
        return area
```

## C

```c
int surfaceArea(int** grid, int gridSize, int* gridColSize){
    int area = 0;
    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < gridColSize[i]; ++j) {
            int v = grid[i][j];
            if (v == 0) continue;
            area += 2; // top and bottom
            int up    = (i > 0)          ? grid[i-1][j] : 0;
            int down  = (i < gridSize-1)? grid[i+1][j] : 0;
            int left  = (j > 0)          ? grid[i][j-1] : 0;
            int right = (j < gridColSize[i]-1) ? grid[i][j+1] : 0;
            if (v > up)    area += v - up;
            if (v > down)  area += v - down;
            if (v > left)  area += v - left;
            if (v > right) area += v - right;
        }
    }
    return area;
}
```

## Csharp

```csharp
public class Solution
{
    public int SurfaceArea(int[][] grid)
    {
        int n = grid.Length;
        int area = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int v = grid[i][j];
                if (v > 0)
                {
                    area += 2 + 4 * v; // top, bottom and four sides
                    if (i > 0) area -= 2 * Math.Min(v, grid[i - 1][j]); // overlap with upper cell
                    if (j > 0) area -= 2 * Math.Min(v, grid[i][j - 1]); // overlap with left cell
                }
            }
        }
        return area;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var surfaceArea = function(grid) {
    const n = grid.length;
    let area = 0;
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            const h = grid[i][j];
            if (h === 0) continue;
            // top and bottom
            area += 2;
            // four sides
            area += 4 * h;
            // subtract shared faces with north neighbor
            if (i > 0) area -= 2 * Math.min(h, grid[i - 1][j]);
            // subtract shared faces with west neighbor
            if (j > 0) area -= 2 * Math.min(h, grid[i][j - 1]);
        }
    }
    return area;
};
```

## Typescript

```typescript
function surfaceArea(grid: number[][]): number {
    const n = grid.length;
    let area = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const v = grid[i][j];
            if (v > 0) {
                area += 2 + 4 * v;
                if (j > 0) {
                    area -= 2 * Math.min(v, grid[i][j - 1]);
                }
                if (i > 0) {
                    area -= 2 * Math.min(v, grid[i - 1][j]);
                }
            }
        }
    }
    return area;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function surfaceArea($grid) {
        $n = count($grid);
        $area = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $h = $grid[$i][$j];
                if ($h == 0) continue;
                // top and bottom
                $area += 2;
                // up
                $up = ($i == 0) ? 0 : $grid[$i - 1][$j];
                $area += max($h - $up, 0);
                // down
                $down = ($i == $n - 1) ? 0 : $grid[$i + 1][$j];
                $area += max($h - $down, 0);
                // left
                $left = ($j == 0) ? 0 : $grid[$i][$j - 1];
                $area += max($h - $left, 0);
                // right
                $right = ($j == $n - 1) ? 0 : $grid[$i][$j + 1];
                $area += max($h - $right, 0);
            }
        }
        return $area;
    }
}
```

## Swift

```swift
class Solution {
    func surfaceArea(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var area = 0
        for i in 0..<n {
            for j in 0..<n {
                let v = grid[i][j]
                if v > 0 {
                    area += 2               // top and bottom
                    area += 4 * v           // four sides
                    if i > 0 {
                        let overlap = min(v, grid[i - 1][j])
                        area -= 2 * overlap
                    }
                    if j > 0 {
                        let overlap = min(v, grid[i][j - 1])
                        area -= 2 * overlap
                    }
                }
            }
        }
        return area
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun surfaceArea(grid: Array<IntArray>): Int {
        var area = 0
        val n = grid.size
        for (i in 0 until n) {
            for (j in 0 until n) {
                val h = grid[i][j]
                if (h > 0) {
                    area += 2 // top and bottom faces
                    var neighbor = if (i > 0) grid[i - 1][j] else 0
                    area += kotlin.math.max(h - neighbor, 0)
                    neighbor = if (i < n - 1) grid[i + 1][j] else 0
                    area += kotlin.math.max(h - neighbor, 0)
                    neighbor = if (j > 0) grid[i][j - 1] else 0
                    area += kotlin.math.max(h - neighbor, 0)
                    neighbor = if (j < n - 1) grid[i][j + 1] else 0
                    area += kotlin.math.max(h - neighbor, 0)
                }
            }
        }
        return area
    }
}
```

## Dart

```dart
class Solution {
  int surfaceArea(List<List<int>> grid) {
    int n = grid.length;
    int area = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int v = grid[i][j];
        if (v == 0) continue;
        // top and bottom
        area += 2;
        // up
        int up = i == 0 ? 0 : grid[i - 1][j];
        if (v > up) area += v - up;
        // down
        int down = i == n - 1 ? 0 : grid[i + 1][j];
        if (v > down) area += v - down;
        // left
        int left = j == 0 ? 0 : grid[i][j - 1];
        if (v > left) area += v - left;
        // right
        int right = j == n - 1 ? 0 : grid[i][j + 1];
        if (v > right) area += v - right;
      }
    }
    return area;
  }
}
```

## Golang

```go
func surfaceArea(grid [][]int) int {
	n := len(grid)
	area := 0
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			h := grid[i][j]
			if h == 0 {
				continue
			}
			area += 2 // top and bottom
			for _, d := range dirs {
				ni, nj := i+d[0], j+d[1]
				neighbor := 0
				if ni >= 0 && ni < n && nj >= 0 && nj < n {
					neighbor = grid[ni][nj]
				}
				if h > neighbor {
					area += h - neighbor
				}
			}
		}
	}
	return area
}
```

## Ruby

```ruby
def surface_area(grid)
  n = grid.size
  total = 0
  (0...n).each do |i|
    (0...n).each do |j|
      v = grid[i][j]
      next if v == 0
      total += v * 4 + 2
      total -= 2 * [v, grid[i - 1][j]].min if i > 0
      total -= 2 * [v, grid[i][j - 1]].min if j > 0
    end
  end
  total
end
```

## Scala

```scala
object Solution {
    def surfaceArea(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        var area = 0
        for (i <- 0 until n; j <- 0 until n) {
            val h = grid(i)(j)
            if (h > 0) {
                area += 2 // top and bottom
                val up    = if (i == 0) 0 else grid(i - 1)(j)
                val down  = if (i == n - 1) 0 else grid(i + 1)(j)
                val left  = if (j == 0) 0 else grid(i)(j - 1)
                val right = if (j == n - 1) 0 else grid(i)(j + 1)
                area += math.max(h - up, 0)
                area += math.max(h - down, 0)
                area += math.max(h - left, 0)
                area += math.max(h - right, 0)
            }
        }
        area
    }
}
```

## Rust

```rust
impl Solution {
    pub fn surface_area(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut area: i32 = 0;
        for i in 0..n {
            for j in 0..n {
                let h = grid[i][j];
                if h > 0 {
                    // top and bottom
                    area += 2;
                    // up
                    let neighbor = if i > 0 { grid[i - 1][j] } else { 0 };
                    area += (h - neighbor).max(0);
                    // down
                    let neighbor = if i + 1 < n { grid[i + 1][j] } else { 0 };
                    area += (h - neighbor).max(0);
                    // left
                    let neighbor = if j > 0 { grid[i][j - 1] } else { 0 };
                    area += (h - neighbor).max(0);
                    // right
                    let neighbor = if j + 1 < n { grid[i][j + 1] } else { 0 };
                    area += (h - neighbor).max(0);
                }
            }
        }
        area
    }
}
```

## Racket

```racket
(define/contract (surface-area grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length grid)]
         [cell (lambda (i j) (list-ref (list-ref grid i) j))])
    (let ([total
           (for/fold ([sum 0]) ([i (in-range n)] [j (in-range n)])
             (let ([v (cell i j)])
               (if (> v 0)
                   (+ sum 2 (* 4 v))
                   sum)))])
      (let ([overlap
             (for/fold ([sub 0]) ([i (in-range n)] [j (in-range n)])
               (let* ([v (cell i j)]
                      [down (if (< (+ i 1) n) (cell (+ i 1) j) 0)]
                      [right (if (< (+ j 1) n) (cell i (+ j 1)) 0)])
                 (+ sub (* 2 (min v down)) (* 2 (min v right)))) )])
        (- total overlap)))))
```

## Erlang

```erlang
-spec surface_area(Grid :: [[integer()]]) -> integer().
surface_area(Grid) ->
    N = length(Grid),
    Area0 = compute_area(Grid, N),
    Overlap = compute_overlap(Grid, N),
    Area0 - Overlap.

compute_area(_Grid, 0) -> 0;
compute_area(Grid, N) ->
    lists:foldl(fun(I, AccI) ->
        lists:foldl(fun(J, AccJ) ->
            V = get(Grid, I, J),
            if V > 0 -> AccJ + 2 + 4 * V; true -> AccJ end
        end, AccI, lists:seq(0, N - 1))
    end, 0, lists:seq(0, N - 1)).

compute_overlap(_Grid, 0) -> 0;
compute_overlap(Grid, N) ->
    lists:foldl(fun(I, AccI) ->
        lists:foldl(fun(J, AccJ) ->
            V = get(Grid, I, J),
            O1 = if J + 1 < N -> 2 * erlang:min(V, get(Grid, I, J + 1)); true -> 0 end,
            O2 = if I + 1 < N -> 2 * erlang:min(V, get(Grid, I + 1, J)); true -> 0 end,
            AccJ + O1 + O2
        end, AccI, lists:seq(0, N - 1))
    end, 0, lists:seq(0, N - 1)).

get(Grid, I, J) ->
    Row = lists:nth(I + 1, Grid),
    lists:nth(J + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec surface_area(grid :: [[integer]]) :: integer
  def surface_area(grid) do
    n = length(grid)

    Enum.with_index(grid)
    |> Enum.reduce(0, fn {row, i}, acc ->
      Enum.with_index(row)
      |> Enum.reduce(acc, fn {h, j}, acc2 ->
        if h == 0 do
          acc2
        else
          up = if i > 0, do: Enum.at(Enum.at(grid, i - 1), j), else: 0
          down = if i < n - 1, do: Enum.at(Enum.at(grid, i + 1), j), else: 0
          left = if j > 0, do: Enum.at(row, j - 1), else: 0
          right = if j < length(row) - 1, do: Enum.at(row, j + 1), else: 0

          area =
            2 +
              max(h - up, 0) +
              max(h - down, 0) +
              max(h - left, 0) +
              max(h - right, 0)

          acc2 + area
        end
      end)
    end)
  end
end
```

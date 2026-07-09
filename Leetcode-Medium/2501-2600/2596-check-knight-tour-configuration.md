# 2596. Check Knight Tour Configuration

## Cpp

```cpp
class Solution {
public:
    bool checkValidGrid(vector<vector<int>>& grid) {
        int n = grid.size();
        int total = n * n;
        vector<pair<int,int>> pos(total);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int step = grid[i][j];
                if (step < 0 || step >= total) return false;
                pos[step] = {i, j};
            }
        }
        // start must be at top-left
        if (pos[0] != make_pair(0, 0)) return false;
        for (int k = 1; k < total; ++k) {
            int dr = abs(pos[k].first - pos[k-1].first);
            int dc = abs(pos[k].second - pos[k-1].second);
            if (!((dr == 1 && dc == 2) || (dr == 2 && dc == 1))) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkValidGrid(int[][] grid) {
        int n = grid.length;
        // The first move must start at (0,0)
        if (grid[0][0] != 0) return false;

        int total = n * n;
        int[] rows = new int[total];
        int[] cols = new int[total];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                rows[val] = i;
                cols[val] = j;
            }
        }

        for (int k = 0; k < total - 1; k++) {
            int dr = Math.abs(rows[k + 1] - rows[k]);
            int dc = Math.abs(cols[k + 1] - cols[k]);
            if (!((dr == 1 && dc == 2) || (dr == 2 && dc == 1))) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        total = n * n
        # position of each step
        pos = [None] * total
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if val < 0 or val >= total:
                    return False
                pos[val] = (i, j)
        # start must be top-left
        if pos[0] != (0, 0):
            return False
        for k in range(total - 1):
            r1, c1 = pos[k]
            r2, c2 = pos[k + 1]
            dr = abs(r1 - r2)
            dc = abs(c1 - c2)
            if not ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False
        total = n * n
        pos = [None] * total
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                pos[val] = (i, j)
        for k in range(total - 1):
            x1, y1 = pos[k]
            x2, y2 = pos[k + 1]
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            if not ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)):
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool checkValidGrid(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int total = n * n;

    int *rowPos = (int *)malloc(total * sizeof(int));
    int *colPos = (int *)malloc(total * sizeof(int));
    if (!rowPos || !colPos) return false; // allocation failure safeguard

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < gridColSize[i]; ++j) {
            int val = grid[i][j];
            if (val < 0 || val >= total) {
                free(rowPos);
                free(colPos);
                return false;
            }
            rowPos[val] = i;
            colPos[val] = j;
        }
    }

    // The tour must start at the top‑left cell.
    if (rowPos[0] != 0 || colPos[0] != 0) {
        free(rowPos);
        free(colPos);
        return false;
    }

    const int moves[8][2] = {
        { 2, 1}, { 1, 2}, {-1, 2}, {-2, 1},
        {-2,-1}, {-1,-2}, { 1,-2}, { 2,-1}
    };

    for (int k = 1; k < total; ++k) {
        int dr = rowPos[k] - rowPos[k - 1];
        int dc = colPos[k] - colPos[k - 1];
        bool ok = false;
        for (int m = 0; m < 8; ++m) {
            if (dr == moves[m][0] && dc == moves[m][1]) {
                ok = true;
                break;
            }
        }
        if (!ok) {
            free(rowPos);
            free(colPos);
            return false;
        }
    }

    free(rowPos);
    free(colPos);
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckValidGrid(int[][] grid)
    {
        int n = grid.Length;
        int total = n * n;
        int[] rowPos = new int[total];
        int[] colPos = new int[total];

        for (int r = 0; r < n; r++)
        {
            for (int c = 0; c < n; c++)
            {
                int val = grid[r][c];
                rowPos[val] = r;
                colPos[val] = c;
            }
        }

        // The knight must start at top-left corner
        if (rowPos[0] != 0 || colPos[0] != 0)
            return false;

        for (int i = 0; i < total - 1; i++)
        {
            int dr = Math.Abs(rowPos[i] - rowPos[i + 1]);
            int dc = Math.Abs(colPos[i] - colPos[i + 1]);

            bool validMove = (dr == 1 && dc == 2) || (dr == 2 && dc == 1);
            if (!validMove)
                return false;
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var checkValidGrid = function(grid) {
    const n = grid.length;
    const total = n * n;
    // positions[value] = [row, col]
    const positions = new Array(total);
    
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            const val = grid[i][j];
            if (val === 0 && (i !== 0 || j !== 0)) return false; // start must be top-left
            positions[val] = [i, j];
        }
    }
    
    for (let k = 0; k < total - 1; ++k) {
        const [x1, y1] = positions[k];
        const [x2, y2] = positions[k + 1];
        const dx = Math.abs(x1 - x2);
        const dy = Math.abs(y1 - y2);
        if (!((dx === 1 && dy === 2) || (dx === 2 && dy === 1))) {
            return false;
        }
    }
    
    return true;
};
```

## Typescript

```typescript
function checkValidGrid(grid: number[][]): boolean {
    const n = grid.length;
    if (grid[0][0] !== 0) return false;

    const total = n * n;
    const rows = new Array<number>(total);
    const cols = new Array<number>(total);

    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            const val = grid[i][j];
            rows[val] = i;
            cols[val] = j;
        }
    }

    for (let k = 0; k < total - 1; ++k) {
        const dr = Math.abs(rows[k + 1] - rows[k]);
        const dc = Math.abs(cols[k + 1] - cols[k]);
        if (!((dr === 1 && dc === 2) || (dr === 2 && dc === 1))) {
            return false;
        }
    }

    return true;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function checkValidGrid($grid) {
        $n = count($grid);
        $total = $n * $n;
        $pos = array_fill(0, $total, null);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $val = $grid[$i][$j];
                $pos[$val] = [$i, $j];
            }
        }
        // The first move must start at (0,0)
        if ($pos[0][0] !== 0 || $pos[0][1] !== 0) {
            return false;
        }
        for ($k = 0; $k < $total - 1; $k++) {
            [$r1, $c1] = $pos[$k];
            [$r2, $c2] = $pos[$k + 1];
            $dr = abs($r1 - $r2);
            $dc = abs($c1 - $c2);
            if (!(($dr === 1 && $dc === 2) || ($dr === 2 && $dc === 1))) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkValidGrid(_ grid: [[Int]]) -> Bool {
        let n = grid.count
        var rows = Array(repeating: 0, count: n * n)
        var cols = Array(repeating: 0, count: n * n)
        
        for i in 0..<n {
            for j in 0..<n {
                let val = grid[i][j]
                rows[val] = i
                cols[val] = j
            }
        }
        
        // The knight must start at the top-left corner (0,0) with value 0.
        if rows[0] != 0 || cols[0] != 0 {
            return false
        }
        
        for k in 0..<(n * n - 1) {
            let dr = abs(rows[k + 1] - rows[k])
            let dc = abs(cols[k + 1] - cols[k])
            if !((dr == 1 && dc == 2) || (dr == 2 && dc == 1)) {
                return false
            }
        }
        
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkValidGrid(grid: Array<IntArray>): Boolean {
        val n = grid.size
        if (grid[0][0] != 0) return false
        val total = n * n
        val rows = IntArray(total)
        val cols = IntArray(total)
        for (i in 0 until n) {
            for (j in 0 until n) {
                val v = grid[i][j]
                rows[v] = i
                cols[v] = j
            }
        }
        for (k in 0 until total - 1) {
            val dr = kotlin.math.abs(rows[k + 1] - rows[k])
            val dc = kotlin.math.abs(cols[k + 1] - cols[k])
            if (!((dr == 1 && dc == 2) || (dr == 2 && dc == 1))) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkValidGrid(List<List<int>> grid) {
    int n = grid.length;
    int total = n * n;
    List<int> rowPos = List.filled(total, -1);
    List<int> colPos = List.filled(total, -1);

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        int val = grid[i][j];
        rowPos[val] = i;
        colPos[val] = j;
      }
    }

    if (rowPos[0] != 0 || colPos[0] != 0) return false;

    for (int k = 0; k < total - 1; ++k) {
      int dr = (rowPos[k + 1] - rowPos[k]).abs();
      int dc = (colPos[k + 1] - colPos[k]).abs();
      if (!((dr == 1 && dc == 2) || (dr == 2 && dc == 1))) {
        return false;
      }
    }

    return true;
  }
}
```

## Golang

```go
func checkValidGrid(grid [][]int) bool {
	n := len(grid)
	if grid[0][0] != 0 {
		return false
	}
	total := n * n
	rows := make([]int, total)
	cols := make([]int, total)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			v := grid[i][j]
			rows[v] = i
			cols[v] = j
		}
	}
	for k := 0; k < total-1; k++ {
		dr := rows[k+1] - rows[k]
		if dr < 0 {
			dr = -dr
		}
		dc := cols[k+1] - cols[k]
		if dc < 0 {
			dc = -dc
		}
		if !((dr == 1 && dc == 2) || (dr == 2 && dc == 1)) {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def check_valid_grid(grid)
  n = grid.size
  return false unless grid[0][0] == 0
  
  total = n * n
  positions = Array.new(total)
  
  grid.each_with_index do |row, i|
    row.each_with_index do |val, j|
      positions[val] = [i, j]
    end
  end
  
  (0...total - 1).each do |k|
    r1, c1 = positions[k]
    r2, c2 = positions[k + 1]
    dr = (r1 - r2).abs
    dc = (c1 - c2).abs
    return false unless (dr == 1 && dc == 2) || (dr == 2 && dc == 1)
  end
  
  true
end
```

## Scala

```scala
object Solution {
  def checkValidGrid(grid: Array[Array[Int]]): Boolean = {
    val n = grid.length
    if (grid(0)(0) != 0) return false
    val total = n * n
    val rows = new Array[Int](total)
    val cols = new Array[Int](total)

    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val v = grid(i)(j)
        rows(v) = i
        cols(v) = j
        j += 1
      }
      i += 1
    }

    var k = 0
    while (k < total - 1) {
      val dr = Math.abs(rows(k + 1) - rows(k))
      val dc = Math.abs(cols(k + 1) - cols(k))
      if (!((dr == 2 && dc == 1) || (dr == 1 && dc == 2))) return false
      k += 1
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn check_valid_grid(grid: Vec<Vec<i32>>) -> bool {
        let n = grid.len();
        let total = n * n;
        let mut pos = vec![(0usize, 0usize); total];
        for (i, row) in grid.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                let v = val as usize;
                if v >= total {
                    return false;
                }
                pos[v] = (i, j);
            }
        }
        // Knight must start at top-left cell
        if pos[0] != (0, 0) {
            return false;
        }
        for k in 0..total - 1 {
            let (r1, c1) = pos[k];
            let (r2, c2) = pos[k + 1];
            let dr = if r1 > r2 { r1 - r2 } else { r2 - r1 };
            let dc = if c1 > c2 { c1 - c2 } else { c2 - c1 };
            if !((dr == 1 && dc == 2) || (dr == 2 && dc == 1)) {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-valid-grid grid)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((n (length grid))
         (total (* n n))
         (pos (make-vector total #f)))
    ;; Record the position of each step number
    (for ([i (in-range n)])
      (let ((row (list-ref grid i)))
        (for ([j (in-range n)])
          (let ((val (list-ref row j)))
            (vector-set! pos val (cons i j))))))
    ;; The tour must start at the top‑left cell
    (if (not (equal? (vector-ref pos 0) (cons 0 0)))
        #f
        (let loop ((k 0))
          (if (= k (- total 1))
              #t
              (let* ((p1 (vector-ref pos k))
                     (p2 (vector-ref pos (+ k 1)))
                     (dr (abs (- (car p2) (car p1))))
                     (dc (abs (- (cdr p2) (cdr p1)))))
                (if (or (and (= dr 1) (= dc 2))
                        (and (= dr 2) (= dc 1)))
                    (loop (+ k 1))
                    #f)))))))
```

## Erlang

```erlang
-spec check_valid_grid(Grid :: [[integer()]]) -> boolean().
check_valid_grid(Grid) ->
    N = length(Grid),
    Map = build_map(Grid, 0, #{}),
    case maps:get(0, Map) of
        {0,0} ->
            MaxK = N * N - 2,
            check_moves(0, MaxK, Map);
        _ -> false
    end.

build_map([], _RowIdx, Map) -> Map;
build_map([Row|Rest], RowIdx, Map0) ->
    Map1 = build_row(Row, RowIdx, 0, Map0),
    build_map(Rest, RowIdx + 1, Map1).

build_row([], _RowIdx, _ColIdx, Map) -> Map;
build_row([Val|RestVals], RowIdx, ColIdx, Map0) ->
    Map1 = maps:put(Val, {RowIdx, ColIdx}, Map0),
    build_row(RestVals, RowIdx, ColIdx + 1, Map1).

check_moves(K, MaxK, _Map) when K > MaxK -> true;
check_moves(K, MaxK, Map) ->
    {R1,C1} = maps:get(K, Map),
    {R2,C2} = maps:get(K+1, Map),
    DR = erlang:abs(R2 - R1),
    DC = erlang:abs(C2 - C1),
    case (DR == 1 andalso DC == 2) orelse (DR == 2 andalso DC == 1) of
        true -> check_moves(K+1, MaxK, Map);
        false -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_valid_grid(grid :: [[integer]]) :: boolean
  def check_valid_grid(grid) do
    n = length(grid)
    total = n * n

    positions =
      grid
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {row, r}, acc ->
        row
        |> Enum.with_index()
        |> Enum.reduce(acc, fn {val, c}, a -> Map.put(a, val, {r, c}) end)
      end)

    case Map.get(positions, 0) do
      {0, 0} -> :ok
      _ -> false
    end
    |> case do
      false -> false
      :ok ->
        Enum.all?(0..total - 2, fn k ->
          {r1, c1} = Map.get(positions, k)
          {r2, c2} = Map.get(positions, k + 1)

          dr = abs(r1 - r2)
          dc = abs(c1 - c2)

          (dr == 1 and dc == 2) or (dr == 2 and dc == 1)
        end)
    end
  end
end
```

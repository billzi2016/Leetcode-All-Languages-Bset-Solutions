# 2711. Difference of Number of Distinct Values on Diagonals

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> differenceOfDistinctValues(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> answer(m, vector<int>(n, 0));
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                unordered_set<int> upLeft;
                for (int i = r - 1, j = c - 1; i >= 0 && j >= 0; --i, --j) {
                    upLeft.insert(grid[i][j]);
                }
                unordered_set<int> downRight;
                for (int i = r + 1, j = c + 1; i < m && j < n; ++i, ++j) {
                    downRight.insert(grid[i][j]);
                }
                answer[r][c] = abs((int)upLeft.size() - (int)downRight.size());
            }
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[][] differenceOfDistinctValues(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] answer = new int[m][n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                java.util.HashSet<Integer> topLeft = new java.util.HashSet<>();
                int i = r - 1, j = c - 1;
                while (i >= 0 && j >= 0) {
                    topLeft.add(grid[i][j]);
                    i--;
                    j--;
                }
                java.util.HashSet<Integer> bottomRight = new java.util.HashSet<>();
                i = r + 1;
                j = c + 1;
                while (i < m && j < n) {
                    bottomRight.add(grid[i][j]);
                    i++;
                    j++;
                }
                answer[r][c] = Math.abs(topLeft.size() - bottomRight.size());
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def differenceOfDistinctValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        # Up-left diagonal distinct counts (excluding current cell)
        diag_up = {}
        for i in range(m):
            for j in range(n):
                d = i - j
                s = diag_up.get(d, set())
                ans[i][j] = len(s)          # store up count temporarily
                # add current value for future cells on this diagonal
                new_set = s | {grid[i][j]}
                diag_up[d] = new_set

        # Down-right diagonal distinct counts (excluding current cell)
        diag_down = {}
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                d = i - j
                s = diag_down.get(d, set())
                down_cnt = len(s)
                ans[i][j] = abs(ans[i][j] - down_cnt)   # final answer
                # add current value for cells above/left on this diagonal
                new_set = s | {grid[i][j]}
                diag_down[d] = new_set

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up_left = set()
                x, y = i - 1, j - 1
                while x >= 0 and y >= 0:
                    up_left.add(grid[x][y])
                    x -= 1
                    y -= 1
                down_right = set()
                x, y = i + 1, j + 1
                while x < m and y < n:
                    down_right.add(grid[x][y])
                    x += 1
                    y += 1
                ans[i][j] = abs(len(up_left) - len(down_right))
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

int** differenceOfDistinctValues(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    int m = gridSize;
    int n = gridColSize[0];
    
    *returnSize = m;
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) {
        (*returnColumnSizes)[i] = n;
    }
    
    int** ans = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i) {
        ans[i] = (int*)malloc(n * sizeof(int));
    }
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int cntTop = 0, cntBottom = 0;
            char seen[51];
            
            memset(seen, 0, sizeof(seen));
            int x = i - 1, y = j - 1;
            while (x >= 0 && y >= 0) {
                int v = grid[x][y];
                if (!seen[v]) {
                    seen[v] = 1;
                    ++cntTop;
                }
                --x; --y;
            }
            
            memset(seen, 0, sizeof(seen));
            x = i + 1; y = j + 1;
            while (x < m && y < n) {
                int v = grid[x][y];
                if (!seen[v]) {
                    seen[v] = 1;
                    ++cntBottom;
                }
                ++x; ++y;
            }
            
            ans[i][j] = cntTop > cntBottom ? cntTop - cntBottom : cntBottom - cntTop;
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] DifferenceOfDistinctValues(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) ans[i] = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                var upLeft = new HashSet<int>();
                int x = i - 1, y = j - 1;
                while (x >= 0 && y >= 0) {
                    upLeft.Add(grid[x][y]);
                    x--; y--;
                }

                var downRight = new HashSet<int>();
                x = i + 1; y = j + 1;
                while (x < m && y < n) {
                    downRight.Add(grid[x][y]);
                    x++; y++;
                }

                ans[i][j] = Math.Abs(upLeft.Count - downRight.Count);
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
 * @return {number[][]}
 */
var differenceOfDistinctValues = function(grid) {
    const m = grid.length, n = grid[0].length;
    const ans = Array.from({ length: m }, () => Array(n).fill(0));
    for (let r = 0; r < m; ++r) {
        for (let c = 0; c < n; ++c) {
            const topSet = new Set();
            let i = r - 1, j = c - 1;
            while (i >= 0 && j >= 0) {
                topSet.add(grid[i][j]);
                --i; --j;
            }
            const bottomSet = new Set();
            i = r + 1; j = c + 1;
            while (i < m && j < n) {
                bottomSet.add(grid[i][j]);
                ++i; ++j;
            }
            ans[r][c] = Math.abs(topSet.size - bottomSet.size);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function differenceOfDistinctValues(grid: number[][]): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const answer: number[][] = Array.from({ length: m }, () => Array(n).fill(0));

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const upLeft = new Set<number>();
            let x = i - 1, y = j - 1;
            while (x >= 0 && y >= 0) {
                upLeft.add(grid[x][y]);
                x--;
                y--;
            }

            const downRight = new Set<number>();
            x = i + 1; y = j + 1;
            while (x < m && y < n) {
                downRight.add(grid[x][y]);
                x++;
                y++;
            }

            answer[i][j] = Math.abs(upLeft.size - downRight.size);
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function differenceOfDistinctValues($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = array_fill(0, $m, array_fill(0, $n, 0));

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                // top-left diagonal (excluding current cell)
                $set1 = [];
                $x = $i - 1;
                $y = $j - 1;
                while ($x >= 0 && $y >= 0) {
                    $set1[$grid[$x][$y]] = true;
                    $x--;
                    $y--;
                }

                // bottom-right diagonal (excluding current cell)
                $set2 = [];
                $x = $i + 1;
                $y = $j + 1;
                while ($x < $m && $y < $n) {
                    $set2[$grid[$x][$y]] = true;
                    $x++;
                    $y++;
                }

                $cnt1 = count($set1);
                $cnt2 = count($set2);
                $ans[$i][$j] = abs($cnt1 - $cnt2);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func differenceOfDistinctValues(_ grid: [[Int]]) -> [[Int]] {
        let m = grid.count
        let n = grid[0].count
        var answer = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        for i in 0..<m {
            for j in 0..<n {
                var upLeftSet = Set<Int>()
                var x = i - 1
                var y = j - 1
                while x >= 0 && y >= 0 {
                    upLeftSet.insert(grid[x][y])
                    x -= 1
                    y -= 1
                }
                
                var downRightSet = Set<Int>()
                x = i + 1
                y = j + 1
                while x < m && y < n {
                    downRightSet.insert(grid[x][y])
                    x += 1
                    y += 1
                }
                
                answer[i][j] = abs(upLeftSet.count - downRightSet.count)
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun differenceOfDistinctValues(grid: Array<IntArray>): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val topCounts = Array(m) { IntArray(n) }
        val answer = Array(m) { IntArray(n) }

        // Top-left diagonal counts (excluding current cell)
        val topMap = HashMap<Int, MutableSet<Int>>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                val d = i - j
                val set = topMap.getOrPut(d) { mutableSetOf() }
                topCounts[i][j] = set.size
                set.add(grid[i][j])
            }
        }

        // Bottom-right diagonal counts and compute answer
        val bottomMap = HashMap<Int, MutableSet<Int>>()
        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                val d = i - j
                val set = bottomMap.getOrPut(d) { mutableSetOf() }
                val bottomCount = set.size
                answer[i][j] = kotlin.math.abs(topCounts[i][j] - bottomCount)
                set.add(grid[i][j])
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> differenceOfDistinctValues(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<int>> ans = List.generate(m, (_) => List.filled(n, 0));
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        Set<int> top = {};
        int x = i - 1, y = j - 1;
        while (x >= 0 && y >= 0) {
          top.add(grid[x][y]);
          x--;
          y--;
        }
        Set<int> bottom = {};
        x = i + 1;
        y = j + 1;
        while (x < m && y < n) {
          bottom.add(grid[x][y]);
          x++;
          y++;
        }
        ans[i][j] = (top.length - bottom.length).abs();
      }
    }
    return ans;
  }
}
```

## Golang

```go
func differenceOfDistinctValues(grid [][]int) [][]int {
    m := len(grid)
    n := len(grid[0])
    ans := make([][]int, m)
    for i := 0; i < m; i++ {
        ans[i] = make([]int, n)
    }

    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            // top-left diagonal
            set1 := make(map[int]struct{})
            i, j := r-1, c-1
            for i >= 0 && j >= 0 {
                set1[grid[i][j]] = struct{}{}
                i--
                j--
            }
            cnt1 := len(set1)

            // bottom-right diagonal
            set2 := make(map[int]struct{})
            i, j = r+1, c+1
            for i < m && j < n {
                set2[grid[i][j]] = struct{}{}
                i++
                j++
            }
            cnt2 := len(set2)

            if cnt1 > cnt2 {
                ans[r][c] = cnt1 - cnt2
            } else {
                ans[r][c] = cnt2 - cnt1
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def difference_of_distinct_values(grid)
  m = grid.size
  n = grid[0].size
  ans = Array.new(m) { Array.new(n, 0) }

  (0...m).each do |i|
    (0...n).each do |j|
      # distinct values on the top‑left diagonal
      seen_up = {}
      x = i - 1
      y = j - 1
      while x >= 0 && y >= 0
        seen_up[grid[x][y]] = true
        x -= 1
        y -= 1
      end
      cnt_up = seen_up.size

      # distinct values on the bottom‑right diagonal
      seen_down = {}
      x = i + 1
      y = j + 1
      while x < m && y < n
        seen_down[grid[x][y]] = true
        x += 1
        y += 1
      end
      cnt_down = seen_down.size

      ans[i][j] = (cnt_up - cnt_down).abs
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def differenceOfDistinctValues(grid: Array[Array[Int]]): Array[Array[Int]] = {
        val m = grid.length
        val n = grid(0).length
        val ans = Array.ofDim[Int](m, n)

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                val setTopLeft = scala.collection.mutable.HashSet[Int]()
                var x = i - 1
                var y = j - 1
                while (x >= 0 && y >= 0) {
                    setTopLeft += grid(x)(y)
                    x -= 1
                    y -= 1
                }

                val setBottomRight = scala.collection.mutable.HashSet[Int]()
                x = i + 1
                y = j + 1
                while (x < m && y < n) {
                    setBottomRight += grid(x)(y)
                    x += 1
                    y += 1
                }

                ans(i)(j) = math.abs(setTopLeft.size - setBottomRight.size)
            }
        }

        ans
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn difference_of_distinct_values(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = vec![vec![0i32; n]; m];

        for i in 0..m {
            for j in 0..n {
                // distinct values on the top‑left diagonal (excluding current cell)
                let mut set_up = HashSet::new();
                let mut x: isize = i as isize - 1;
                let mut y: isize = j as isize - 1;
                while x >= 0 && y >= 0 {
                    set_up.insert(grid[x as usize][y as usize]);
                    x -= 1;
                    y -= 1;
                }

                // distinct values on the bottom‑right diagonal (excluding current cell)
                let mut set_down = HashSet::new();
                let mut x = i + 1;
                let mut y = j + 1;
                while x < m && y < n {
                    set_down.insert(grid[x][y]);
                    x += 1;
                    y += 1;
                }

                ans[i][j] = (set_up.len() as i32 - set_down.len() as i32).abs();
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (difference-of-distinct-values grid)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (car grid)))))
    (for/list ([i (in-range m)])
      (for/list ([j (in-range n)])
        (let ((before (make-hash))
              (after (make-hash)))
          ;; cells on the top‑left diagonal of (i,j)
          (let loop ((x (- i 1)) (y (- j 1)))
            (when (and (>= x 0) (>= y 0))
              (hash-set! before (list-ref (list-ref grid x) y) #t)
              (loop (- x 1) (- y 1))))
          ;; cells on the bottom‑right diagonal of (i,j)
          (let loop ((x (+ i 1)) (y (+ j 1)))
            (when (and (< x m) (< y n))
              (hash-set! after (list-ref (list-ref grid x) y) #t)
              (loop (+ x 1) (+ y 1))))
          (abs (- (hash-count before) (hash-count after))))))))
```

## Erlang

```erlang
-spec difference_of_distinct_values(Grid :: [[integer()]]) -> [[integer()]].
difference_of_distinct_values(Grid) ->
    Rows = length(Grid),
    Cols = case Grid of [] -> 0; [First|_] -> length(First) end,
    lists:map(
        fun(RIdx) ->
            lists:map(
                fun(CIdx) ->
                    Before = distinct_before(Grid, RIdx - 1, CIdx - 1, #{}),
                    After  = distinct_after(Grid, Rows, Cols, RIdx + 1, CIdx + 1, #{}),
                    abs(Before - After)
                end,
                lists:seq(0, Cols - 1)
            )
        end,
        lists:seq(0, Rows - 1)
    ).

distinct_before(_Grid, R, _C, Set) when R < 0 orelse _C < 0 ->
    maps:size(Set);
distinct_before(Grid, R, C, Set) ->
    Row = lists:nth(R + 1, Grid),
    Val = lists:nth(C + 1, Row),
    NewSet = maps:put(Val, true, Set),
    distinct_before(Grid, R - 1, C - 1, NewSet).

distinct_after(_Grid, Rows, _Cols, R, _C, Set) when R >= Rows orelse _C >= _Cols ->
    maps:size(Set);
distinct_after(Grid, Rows, Cols, R, C, Set) ->
    Row = lists:nth(R + 1, Grid),
    Val = lists:nth(C + 1, Row),
    NewSet = maps:put(Val, true, Set),
    distinct_after(Grid, Rows, Cols, R + 1, C + 1, NewSet).
```

## Elixir

```elixir
defmodule Solution do
  @spec difference_of_distinct_values(grid :: [[integer]]) :: [[integer]]
  def difference_of_distinct_values(grid) do
    m = length(grid)
    n = length(hd(grid))

    for r <- 0..(m - 1), into: [] do
      for c <- 0..(n - 1) do
        tl_set = collect_set(grid, r - 1, c - 1, -1, -1, m, n, MapSet.new())
        br_set = collect_set(grid, r + 1, c + 1, 1, 1, m, n, MapSet.new())
        abs(MapSet.size(tl_set) - MapSet.size(br_set))
      end
    end
  end

  defp collect_set(_grid, r, _c, _dr, _dc, m, _n, set) when r < 0 or r >= m, do: set
  defp collect_set(_grid, _r, c, _dr, _dc, _m, n, set) when c < 0 or c >= n, do: set

  defp collect_set(grid, r, c, dr, dc, m, n, set) do
    val = Enum.at(Enum.at(grid, r), c)
    new_set = MapSet.put(set, val)
    collect_set(grid, r + dr, c + dc, dr, dc, m, n, new_set)
  end
end
```

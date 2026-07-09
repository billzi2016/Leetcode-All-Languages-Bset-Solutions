# 1992. Find All Groups of Farmland

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        int m = land.size();
        if (m == 0) return {};
        int n = land[0].size();
        vector<vector<int>> res;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (land[i][j] == 1) {
                    int r = i;
                    while (r + 1 < m && land[r + 1][j] == 1) ++r;
                    int c = j;
                    while (c + 1 < n && land[i][c + 1] == 1) ++c;
                    // mark visited
                    for (int x = i; x <= r; ++x)
                        for (int y = j; y <= c; ++y)
                            land[x][y] = 0;
                    res.push_back({i, j, r, c});
                }
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] findFarmland(int[][] land) {
        int m = land.length;
        int n = land[0].length;
        java.util.List<int[]> res = new java.util.ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == 1) {
                    int r = i;
                    while (r < m && land[r][j] == 1) {
                        r++;
                    }
                    r--; // last row of the rectangle
                    int c = j;
                    while (c < n && land[i][c] == 1) {
                        c++;
                    }
                    c--; // last column of the rectangle
                    // mark visited
                    for (int x = i; x <= r; x++) {
                        for (int y = j; y <= c; y++) {
                            land[x][y] = 0;
                        }
                    }
                    res.add(new int[]{i, j, r, c});
                }
            }
        }
        int[][] ans = new int[res.size()][4];
        for (int i = 0; i < res.size(); i++) {
            ans[i] = res.get(i);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(land)
        if m == 0:
            return []
        n = len(land[0])
        res = []
        i = 0
        while i < m:
            j = 0
            while j < n:
                if land[i][j] == 1:
                    r, c = i, j
                    # find bottom boundary
                    rr = r
                    while rr + 1 < m and land[rr + 1][c] == 1:
                        rr += 1
                    # find right boundary using the top row (rectangle guarantee)
                    cc = c
                    while cc + 1 < n and land[r][cc + 1] == 1:
                        cc += 1
                    # mark visited cells as 0
                    for x in range(r, rr + 1):
                        for y in range(c, cc + 1):
                            land[x][y] = 0
                    res.append([r, c, rr, cc])
                    j = cc + 1  # skip processed columns
                else:
                    j += 1
            i += 1
        return res
```

## Python3

```python
class Solution:
    def findFarmland(self, land):
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    # expand right on the top row
                    c = j
                    while c + 1 < n and land[i][c + 1] == 1:
                        c += 1
                    # expand down while all cells in current width are 1
                    r = i
                    while r + 1 < m and all(land[r + 1][k] == 1 for k in range(j, c + 1)):
                        r += 1
                    # mark visited
                    for x in range(i, r + 1):
                        for y in range(j, c + 1):
                            land[x][y] = 0
                    res.append([i, j, r, c])
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findFarmland(int** land, int landSize, int* landColSize, int* returnSize, int*** returnColumnSizes) {
    int m = landSize;
    if (m == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int n = landColSize[0];

    int maxGroups = m * n;                     // worst case each cell is a group
    int** res = (int**)malloc(maxGroups * sizeof(int*));
    int* colSizes = (int*)malloc(maxGroups * sizeof(int));

    int count = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (land[i][j] == 1) {
                // find bottom row of the rectangle
                int r = i;
                while (r + 1 < m && land[r + 1][j] == 1) {
                    ++r;
                }
                // find rightmost column of the rectangle
                int c = j;
                while (c + 1 < n && land[i][c + 1] == 1) {
                    ++c;
                }

                // mark all cells in this rectangle as visited (set to 0)
                for (int ii = i; ii <= r; ++ii) {
                    for (int jj = j; jj <= c; ++jj) {
                        land[ii][jj] = 0;
                    }
                }

                int* rect = (int*)malloc(4 * sizeof(int));
                rect[0] = i;
                rect[1] = j;
                rect[2] = r;
                rect[3] = c;

                res[count] = rect;
                colSizes[count] = 4;
                ++count;
            }
        }
    }

    *returnSize = count;
    *returnColumnSizes = &colSizes;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] FindFarmland(int[][] land) {
        int m = land.Length;
        int n = land[0].Length;
        var res = new List<int[]>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == 1) {
                    int r = i;
                    while (r + 1 < m && land[r + 1][j] == 1) r++;
                    int c = j;
                    while (c + 1 < n && land[i][c + 1] == 1) c++;
                    for (int x = i; x <= r; x++) {
                        for (int y = j; y <= c; y++) {
                            land[x][y] = 0;
                        }
                    }
                    res.Add(new int[] { i, j, r, c });
                }
            }
        }
        return res.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} land
 * @return {number[][]}
 */
var findFarmland = function(land) {
    const m = land.length;
    if (m === 0) return [];
    const n = land[0].length;
    const res = [];

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (land[i][j] !== 1) continue;

            // find bottom boundary
            let endRow = i;
            while (endRow + 1 < m && land[endRow + 1][j] === 1) {
                endRow++;
            }

            // find right boundary
            let endCol = j;
            while (endCol + 1 < n && land[i][endCol + 1] === 1) {
                endCol++;
            }

            // mark the whole rectangle as visited (set to 0)
            for (let r = i; r <= endRow; ++r) {
                for (let c = j; c <= endCol; ++c) {
                    land[r][c] = 0;
                }
            }

            res.push([i, j, endRow, endCol]);
        }
    }

    return res;
};
```

## Typescript

```typescript
function findFarmland(land: number[][]): number[][] {
    const m = land.length;
    if (m === 0) return [];
    const n = land[0].length;
    const res: number[][] = [];

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (land[i][j] === 1) {
                // find bottom boundary
                let r = i;
                while (r + 1 < m && land[r + 1][j] === 1) {
                    r++;
                }
                // find right boundary
                let c = j;
                while (c + 1 < n && land[i][c + 1] === 1) {
                    c++;
                }
                // mark the rectangle as visited
                for (let x = i; x <= r; x++) {
                    for (let y = j; y <= c; y++) {
                        land[x][y] = 0;
                    }
                }
                res.push([i, j, r, c]);
            }
        }
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $land
     * @return Integer[][]
     */
    function findFarmland($land) {
        $m = count($land);
        if ($m == 0) return [];
        $n = count($land[0]);
        $result = [];

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($land[$i][$j] == 1) {
                    // Find bottom boundary
                    $r = $i;
                    while ($r < $m && $land[$r][$j] == 1) {
                        $r++;
                    }
                    $bottom = $r - 1;

                    // Find right boundary using the top row (rectangular guarantee)
                    $c = $j;
                    while ($c < $n && $land[$i][$c] == 1) {
                        $c++;
                    }
                    $right = $c - 1;

                    // Mark all cells in this rectangle as visited
                    for ($x = $i; $x <= $bottom; $x++) {
                        for ($y = $j; $y <= $right; $y++) {
                            $land[$x][$y] = 0;
                        }
                    }

                    $result[] = [$i, $j, $bottom, $right];
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findFarmland(_ land: [[Int]]) -> [[Int]] {
        var grid = land
        let m = grid.count
        guard m > 0 else { return [] }
        let n = grid[0].count
        var result: [[Int]] = []
        
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    var r = i
                    while r < m && grid[r][j] == 1 {
                        r += 1
                    }
                    let bottom = r - 1
                    
                    var c = j
                    while c < n && grid[i][c] == 1 {
                        c += 1
                    }
                    let right = c - 1
                    
                    for row in i...bottom {
                        for col in j...right {
                            grid[row][col] = 0
                        }
                    }
                    
                    result.append([i, j, bottom, right])
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findFarmland(land: Array<IntArray>): Array<IntArray> {
        val m = land.size
        if (m == 0) return arrayOf()
        val n = land[0].size
        val result = mutableListOf<IntArray>()
        for (i in 0 until m) {
            var j = 0
            while (j < n) {
                if (land[i][j] == 1) {
                    var r = i
                    while (r + 1 < m && land[r + 1][j] == 1) r++
                    var c = j
                    while (c + 1 < n && land[i][c + 1] == 1) c++
                    for (row in i..r) {
                        for (col in j..c) {
                            land[row][col] = 0
                        }
                    }
                    result.add(intArrayOf(i, j, r, c))
                }
                j++
            }
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> findFarmland(List<List<int>> land) {
    int m = land.length;
    if (m == 0) return [];
    int n = land[0].length;
    List<List<int>> res = [];

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (land[i][j] == 1) {
          // Find bottom boundary
          int r = i;
          while (r < m && land[r][j] == 1) {
            r++;
          }
          int bottom = r - 1;

          // Find right boundary using the top row of this rectangle
          int c = j;
          while (c < n && land[i][c] == 1) {
            c++;
          }
          int right = c - 1;

          // Mark all cells in this rectangle as visited
          for (int rr = i; rr <= bottom; rr++) {
            for (int cc = j; cc <= right; cc++) {
              land[rr][cc] = 0;
            }
          }

          res.add([i, j, bottom, right]);
        }
      }
    }

    return res;
  }
}
```

## Golang

```go
func findFarmland(land [][]int) [][]int {
	m := len(land)
	if m == 0 {
		return nil
	}
	n := len(land[0])
	var res [][]int

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if land[i][j] != 1 {
				continue
			}
			// find bottom boundary
			r := i
			for r+1 < m && land[r+1][j] == 1 {
				r++
			}
			// find right boundary using the top row (any row works)
			c := j
			for c+1 < n && land[i][c+1] == 1 {
				c++
			}
			// mark rectangle as visited
			for x := i; x <= r; x++ {
				for y := j; y <= c; y++ {
					land[x][y] = 0
				}
			}
			res = append(res, []int{i, j, r, c})
		}
	}
	return res
}
```

## Ruby

```ruby
def find_farmland(land)
  m = land.length
  n = land[0].length
  res = []

  i = 0
  while i < m
    j = 0
    while j < n
      if land[i][j] == 1
        r = i
        while r + 1 < m && land[r + 1][j] == 1
          r += 1
        end

        c = j
        while c + 1 < n && land[i][c + 1] == 1
          c += 1
        end

        (i..r).each do |x|
          (j..c).each do |y|
            land[x][y] = 0
          end
        end

        res << [i, j, r, c]
      end
      j += 1
    end
    i += 1
  end

  res
end
```

## Scala

```scala
object Solution {
  def findFarmland(land: Array[Array[Int]]): Array[Array[Int]] = {
    val m = land.length
    if (m == 0) return Array.empty
    val n = land(0).length
    val res = scala.collection.mutable.ArrayBuffer[Array[Int]]()

    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (land(i)(j) == 1) {
          var r = i
          while (r < m && land(r)(j) == 1) r += 1
          var c = j
          while (c < n && land(i)(c) == 1) c += 1

          // mark visited
          var x = i
          while (x < r) {
            var y = j
            while (y < c) {
              land(x)(y) = 0
              y += 1
            }
            x += 1
          }

          res += Array(i, j, r - 1, c - 1)
        }
        j += 1
      }
      i += 1
    }

    res.toArray
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_farmland(mut land: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = land.len();
        if m == 0 {
            return vec![];
        }
        let n = land[0].len();
        let mut res = Vec::new();

        for i in 0..m {
            for j in 0..n {
                if land[i][j] == 1 {
                    // find right boundary of the rectangle
                    let mut c = j;
                    while c < n && land[i][c] == 1 {
                        c += 1;
                    }
                    let right = c - 1;

                    // find bottom boundary using the width determined above
                    let mut r = i;
                    loop {
                        if r >= m {
                            break;
                        }
                        let mut ok = true;
                        for col in j..=right {
                            if land[r][col] != 1 {
                                ok = false;
                                break;
                            }
                        }
                        if !ok {
                            break;
                        }
                        r += 1;
                    }
                    let bottom = r - 1;

                    // mark visited cells
                    for row in i..=bottom {
                        for col in j..=right {
                            land[row][col] = 0;
                        }
                    }

                    res.push(vec![i as i32, j as i32, bottom as i32, right as i32]);
                }
            }
        }

        res
    }
}
```

## Racket

```racket
(define/contract (find-farmland land)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((m (length land))
         (n (if (= m 0) 0 (length (car land))))
         (grid (list->vector (map list->vector land)))
         (result '()))
    (define (row-all-ones? rowvec start end)
      (let loop ((c start))
        (if (> c end) #t
            (and (= (vector-ref rowvec c) 1)
                 (loop (+ c 1))))))
    (for ([i (in-range m)])
      (for ([j (in-range n)])
        (when (= (vector-ref (vector-ref grid i) j) 1)
          ;; find right boundary
          (define c j)
          (let loop ((col (+ j 1)))
            (if (and (< col n) (= (vector-ref (vector-ref grid i) col) 1))
                (begin (set! c col) (loop (+ col 1)))))
          ;; find bottom boundary
          (define r i)
          (let loop2 ((row (+ i 1)))
            (if (and (< row m)
                     (row-all-ones? (vector-ref grid row) j c))
                (begin (set! r row) (loop2 (+ row 1)))))
          ;; mark visited cells
          (for ([row (in-range i (+ r 1))])
            (let ((rowvec (vector-ref grid row)))
              (for ([col (in-range j (+ c 1))])
                (vector-set! rowvec col 0))))
          (set! result (cons (list i j r c) result)))))
    (reverse result)))
```

## Erlang

```erlang
-spec find_farmland(Land :: [[integer()]]) -> [[integer()]].
find_farmland(Land) ->
    Tuples = [list_to_tuple(R) || R <- Land],
    M = length(Tuples),
    N = case Tuples of [] -> 0; [First|_] -> tuple_size(First) end,
    find_rows(0, M, N, Tuples, #{}, []).

%% iterate over rows
find_rows(RowIdx, M, _N, _Tuples, Visited, Acc) when RowIdx >= M ->
    lists:reverse(Acc);
find_rows(RowIdx, M, N, Tuples, Visited, Acc) ->
    find_cols(RowIdx, 0, M, N, Tuples, Visited, Acc).

%% iterate over columns in a given row
find_cols(_RowIdx, ColIdx, _M, N, _Tuples, Visited, Acc) when ColIdx >= N ->
    %% move to next row
    find_rows(_RowIdx+1, _M, N, _Tuples, Visited, Acc);
find_cols(RowIdx, ColIdx, M, N, Tuples, Visited, Acc) ->
    case maps:is_key({RowIdx,ColIdx}, Visited) of
        true ->
            find_cols(RowIdx, ColIdx+1, M, N, Tuples, Visited, Acc);
        false ->
            Val = get_cell(Tuples, RowIdx, ColIdx),
            if Val == 1 ->
                    {R2,C2} = expand_rectangle(Tuples, RowIdx, ColIdx, M, N),
                    NewVisited = mark_visited(Visited, RowIdx, ColIdx, R2, C2),
                    find_cols(RowIdx, ColIdx+1, M, N, Tuples, NewVisited,
                              [[RowIdx,ColIdx,R2,C2]|Acc]);
               true ->
                    find_cols(RowIdx, ColIdx+1, M, N, Tuples, Visited, Acc)
            end
    end.

%% get cell value (0‑based indices)
get_cell(Tuples, R, C) ->
    RowTuple = lists:nth(R+1, Tuples),
    element(C+1, RowTuple).

%% expand rectangle from top‑left corner
expand_rectangle(Tuples, R, C, M, N) ->
    C2 = find_c2(Tuples, R, C, N),
    R2 = find_r2(Tuples, R, C, C2, M),
    {R2, C2}.

%% find rightmost column of the top row
find_c2(_Tuples, _R, C, N) when C+1 >= N ->
    C;
find_c2(Tuples, R, C, N) ->
    case get_cell(Tuples, R, C+1) of
        1 -> find_c2(Tuples, R, C+1, N);
        _ -> C
    end.

%% find bottommost row where all columns C..C2 are 1
find_r2(_Tuples, R, _C, _C2, M) when R+1 >= M ->
    R;
find_r2(Tuples, R, C, C2, M) ->
    case row_all_one(Tuples, R+1, C, C2) of
        true -> find_r2(Tuples, R+1, C, C2, M);
        false -> R
    end.

%% check that a whole segment in a row consists of 1s
row_all_one(_Tuples, _Row, Col, End) when Col > End ->
    true;
row_all_one(Tuples, Row, Col, End) ->
    case get_cell(Tuples, Row, Col) of
        1 -> row_all_one(Tuples, Row, Col+1, End);
        _ -> false
    end.

%% mark all cells inside rectangle as visited
mark_visited(Visited, R1, C1, R2, C2) ->
    mark_rows(R1, C1, R2, C2, Visited).

mark_rows(R, _C1, Rmax, _C2, Visited) when R > Rmax ->
    Visited;
mark_rows(R, C1, Rmax, C2, Visited) ->
    NewVis = mark_cols(R, C1, C2, Visited),
    mark_rows(R+1, C1, Rmax, C2, NewVis).

mark_cols(_Row, Col, Cmax, Visited) when Col > Cmax ->
    Visited;
mark_cols(Row, Col, Cmax, Visited) ->
    mark_cols(Row, Col+1, Cmax,
              maps:put({Row,Col}, true, Visited)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_farmland(land :: [[integer]]) :: [[integer]]
  def find_farmland(land) do
    m = length(land)
    n = if m == 0, do: 0, else: land |> hd() |> length()

    {res, _} =
      Enum.reduce(0..(m - 1), {[], MapSet.new()}, fn i, {acc, visited} ->
        {new_acc, new_vis} =
          Enum.reduce(0..(n - 1), {acc, visited}, fn j, {inner_acc, inner_vis} ->
            if cell_one?(land, i, j) and not MapSet.member?(inner_vis, {i, j}) do
              r = find_bottom(i, j, m, land)
              c = find_right(i, j, n, land)

              vis =
                Enum.reduce(i..r, inner_vis, fn x, vs ->
                  Enum.reduce(j..c, vs, fn y, vs2 -> MapSet.put(vs2, {x, y}) end)
                end)

              {[ [i, j, r, c] | inner_acc ], vis}
            else
              {inner_acc, inner_vis}
            end
          end)

        {new_acc, new_vis}
      end)

    Enum.reverse(res)
  end

  defp cell_one?(land, i, j) do
    land |> Enum.at(i) |> Enum.at(j) == 1
  end

  defp find_bottom(i, j, m, land) do
    if i + 1 < m and cell_one?(land, i + 1, j) do
      find_bottom(i + 1, j, m, land)
    else
      i
    end
  end

  defp find_right(i, j, n, land) do
    if j + 1 < n and cell_one?(land, i, j + 1) do
      find_right(i, j + 1, n, land)
    else
      j
    end
  end
end
```

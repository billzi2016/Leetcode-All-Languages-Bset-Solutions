# 0885. Spiral Matrix III

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        vector<vector<int>> ans;
        ans.reserve(rows * cols);
        ans.push_back({rStart, cStart});
        if (rows * cols == 1) return ans;

        const int dr[4] = {0, 1, 0, -1}; // East, South, West, North
        const int dc[4] = {1, 0, -1, 0};

        int r = rStart, c = cStart;
        int dir = 0;          // start moving east
        int step = 1;

        while ((int)ans.size() < rows * cols) {
            for (int i = 0; i < 2; ++i) {           // two directions with same step length
                for (int s = 0; s < step && (int)ans.size() < rows * cols; ++s) {
                    r += dr[dir];
                    c += dc[dir];
                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        ans.push_back({r, c});
                    }
                }
                dir = (dir + 1) % 4;               // turn clockwise
            }
            ++step;                                 // increase step after two directions
        }

        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int total = rows * cols;
        int[][] ans = new int[total][2];
        int idx = 0;
        ans[idx][0] = rStart;
        ans[idx][1] = cStart;
        idx++;
        int r = rStart;
        int c = cStart;
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};
        int steps = 1;
        while (idx < total) {
            for (int d = 0; d < 4 && idx < total; d++) {
                for (int i = 0; i < steps && idx < total; i++) {
                    r += dr[d];
                    c += dc[d];
                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        ans[idx][0] = r;
                        ans[idx][1] = c;
                        idx++;
                    }
                }
                if (d % 2 == 1) {
                    steps++;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        total = rows * cols
        res = []
        r, c = rStart, cStart
        # directions: East, South, West, North
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        step = 1          # current step length
        dir_idx = 0       # index in dirs

        while len(res) < total:
            for _ in range(2):   # each step size is used for two directions
                dr, dc = dirs[dir_idx % 4]
                for _ in range(step):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                        if len(res) == total:
                            return res
                    r += dr
                    c += dc
                dir_idx += 1
            step += 1

        return res
```

## Python3

```python
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        total = rows * cols
        res = []
        # starting position is always inside the grid per constraints
        res.append([rStart, cStart])
        if total == 1:
            return res

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # east, south, west, north
        step = 1
        r, c = rStart, cStart
        dir_idx = 0

        while len(res) < total:
            for _ in range(2):  # each step length is used twice before incrementing
                dr, dc = dirs[dir_idx % 4]
                for _ in range(step):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                        if len(res) == total:
                            return res
                dir_idx += 1
            step += 1

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
int** spiralMatrixIII(int rows, int cols, int rStart, int cStart, int* returnSize, int*** returnColumnSizes) {
    (void)returnColumnSizes; // placeholder to avoid unused warning if not used
    int total = rows * cols;
    int **result = (int **)malloc(total * sizeof(int *));
    int *colSizes = (int *)malloc(total * sizeof(int));

    int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // East, South, West, North
    int r = rStart, c = cStart;
    int count = 0;

    // Record the starting cell
    if (r >= 0 && r < rows && c >= 0 && c < cols) {
        result[count] = (int *)malloc(2 * sizeof(int));
        result[count][0] = r;
        result[count][1] = c;
        colSizes[count] = 2;
        ++count;
    }

    int step = 1;          // number of steps in current direction segment
    int dirIdx = 0;        // index into dirs

    while (count < total) {
        for (int repeat = 0; repeat < 2 && count < total; ++repeat) {
            int dr = dirs[dirIdx][0];
            int dc = dirs[dirIdx][1];
            for (int i = 0; i < step && count < total; ++i) {
                r += dr;
                c += dc;
                if (r >= 0 && r < rows && c >= 0 && c < cols) {
                    result[count] = (int *)malloc(2 * sizeof(int));
                    result[count][0] = r;
                    result[count][1] = c;
                    colSizes[count] = 2;
                    ++count;
                }
            }
            dirIdx = (dirIdx + 1) % 4;
        }
        ++step;
    }

    *returnSize = total;
    *returnColumnSizes = &colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] SpiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int total = rows * cols;
        var result = new List<int[]>(total);
        int r = rStart, c = cStart;
        if (r >= 0 && r < rows && c >= 0 && c < cols)
            result.Add(new int[] { r, c });

        int[] dr = { 0, 1, 0, -1 };
        int[] dc = { 1, 0, -1, 0 };
        int step = 1;
        int dirIdx = 0; // start moving east

        while (result.Count < total) {
            for (int i = 0; i < 2; i++) {
                for (int s = 0; s < step; s++) {
                    r += dr[dirIdx];
                    c += dc[dirIdx];
                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        result.Add(new int[] { r, c });
                        if (result.Count == total) break;
                    }
                }
                dirIdx = (dirIdx + 1) % 4;
                if (result.Count == total) break;
            }
            step++;
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} rows
 * @param {number} cols
 * @param {number} rStart
 * @param {number} cStart
 * @return {number[][]}
 */
var spiralMatrixIII = function(rows, cols, rStart, cStart) {
    const total = rows * cols;
    const result = [];
    // directions: east, south, west, north
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    
    let r = rStart, c = cStart;
    result.push([r, c]);
    let visited = 1;
    let step = 1;          // current step length
    let dirIdx = 0;        // index in dirs
    
    while (visited < total) {
        for (let i = 0; i < 2; i++) {           // two directions with same step size
            const dr = dirs[dirIdx][0];
            const dc = dirs[dirIdx][1];
            for (let s = 0; s < step; s++) {
                r += dr;
                c += dc;
                if (r >= 0 && r < rows && c >= 0 && c < cols) {
                    result.push([r, c]);
                    visited++;
                    if (visited === total) break;
                }
            }
            dirIdx = (dirIdx + 1) % 4;
            if (visited === total) break;
        }
        step++;
    }
    
    return result;
};
```

## Typescript

```typescript
function spiralMatrixIII(rows: number, cols: number, rStart: number, cStart: number): number[][] {
    const total = rows * cols;
    const result: number[][] = [];
    let r = rStart;
    let c = cStart;

    if (r >= 0 && r < rows && c >= 0 && c < cols) {
        result.push([r, c]);
    }

    const dirs: [number, number][] = [
        [0, 1],   // east
        [1, 0],   // south
        [0, -1],  // west
        [-1, 0]   // north
    ];

    let step = 1;
    let dirIdx = 0;

    while (result.length < total) {
        for (let i = 0; i < 2; i++) { // two directions with the same step length
            const [dr, dc] = dirs[dirIdx];
            for (let s = 0; s < step; s++) {
                r += dr;
                c += dc;
                if (r >= 0 && r < rows && c >= 0 && c < cols) {
                    result.push([r, c]);
                    if (result.length === total) break;
                }
            }
            dirIdx = (dirIdx + 1) % 4;
            if (result.length === total) break;
        }
        step++;
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $rows
     * @param Integer $cols
     * @param Integer $rStart
     * @param Integer $cStart
     * @return Integer[][]
     */
    function spiralMatrixIII($rows, $cols, $rStart, $cStart) {
        $total = $rows * $cols;
        $result = [];

        // Directions: East, South, West, North
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $r = $rStart;
        $c = $cStart;

        if ($r >= 0 && $r < $rows && $c >= 0 && $c < $cols) {
            $result[] = [$r, $c];
        }
        $visited = count($result);
        $step = 1;          // current step length
        $dirIdx = 0;        // index in $dirs

        while ($visited < $total) {
            for ($pair = 0; $pair < 2; $pair++) {   // two directions share the same step size
                $dr = $dirs[$dirIdx][0];
                $dc = $dirs[$dirIdx][1];
                for ($i = 0; $i < $step; $i++) {
                    $r += $dr;
                    $c += $dc;
                    if ($r >= 0 && $r < $rows && $c >= 0 && $c < $cols) {
                        $result[] = [$r, $c];
                        $visited++;
                        if ($visited == $total) {
                            break 3; // exit all loops
                        }
                    }
                }
                $dirIdx = ($dirIdx + 1) % 4;
            }
            $step++;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func spiralMatrixIII(_ rows: Int, _ cols: Int, _ rStart: Int, _ cStart: Int) -> [[Int]] {
        var result = [[Int]]()
        result.reserveCapacity(rows * cols)
        
        var r = rStart
        var c = cStart
        
        if r >= 0 && r < rows && c >= 0 && c < cols {
            result.append([r, c])
        }
        
        let dr = [0, 1, 0, -1]   // east, south, west, north
        let dc = [1, 0, -1, 0]
        var step = 1
        var dirIdx = 0
        
        while result.count < rows * cols {
            for _ in 0..<2 {               // each step length is used twice
                for _ in 0..<step {
                    r += dr[dirIdx]
                    c += dc[dirIdx]
                    if r >= 0 && r < rows && c >= 0 && c < cols {
                        result.append([r, c])
                        if result.count == rows * cols { break }
                    }
                }
                dirIdx = (dirIdx + 1) % 4
                if result.count == rows * cols { break }
            }
            step += 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun spiralMatrixIII(rows: Int, cols: Int, rStart: Int, cStart: Int): Array<IntArray> {
        val total = rows * cols
        val result = ArrayList<IntArray>(total)
        var r = rStart
        var c = cStart
        if (r in 0 until rows && c in 0 until cols) {
            result.add(intArrayOf(r, c))
            if (result.size == total) return result.toTypedArray()
        }
        val dirs = arrayOf(
            intArrayOf(0, 1),   // east
            intArrayOf(1, 0),   // south
            intArrayOf(0, -1),  // west
            intArrayOf(-1, 0)   // north
        )
        var step = 1
        while (result.size < total) {
            for (d in 0..3) {
                val dr = dirs[d][0]
                val dc = dirs[d][1]
                repeat(step) {
                    r += dr
                    c += dc
                    if (r in 0 until rows && c in 0 until cols) {
                        result.add(intArrayOf(r, c))
                        if (result.size == total) return result.toTypedArray()
                    }
                }
                if (d % 2 == 1) step++
            }
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
    const dirs = [
      [0, 1],   // east
      [1, 0],   // south
      [0, -1],  // west
      [-1, 0]   // north
    ];
    final total = rows * cols;
    final result = <List<int>>[];
    int r = rStart, c = cStart;
    result.add([r, c]); // starting cell is always inside the grid

    int step = 1;      // current length of movement
    int dirIdx = 0;    // index in dirs

    while (result.length < total) {
      for (int repeat = 0; repeat < 2; ++repeat) {
        final dr = dirs[dirIdx][0];
        final dc = dirs[dirIdx][1];
        for (int s = 0; s < step; ++s) {
          r += dr;
          c += dc;
          if (r >= 0 && r < rows && c >= 0 && c < cols) {
            result.add([r, c]);
            if (result.length == total) break;
          }
        }
        dirIdx = (dirIdx + 1) % 4;
        if (result.length == total) break;
      }
      step++;
    }

    return result;
  }
}
```

## Golang

```go
func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
	total := rows * cols
	res := make([][]int, 0, total)

	r, c := rStart, cStart
	if r >= 0 && r < rows && c >= 0 && c < cols {
		res = append(res, []int{r, c})
	}

	dirs := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	step := 1
	dirIdx := 0

	for len(res) < total {
		for i := 0; i < 2; i++ {
			dr, dc := dirs[dirIdx][0], dirs[dirIdx][1]
			for s := 0; s < step; s++ {
				r += dr
				c += dc
				if r >= 0 && r < rows && c >= 0 && c < cols {
					res = append(res, []int{r, c})
					if len(res) == total {
						return res
					}
				}
			}
			dirIdx = (dirIdx + 1) % 4
		}
		step++
	}
	return res
}
```

## Ruby

```ruby
def spiral_matrix_iii(rows, cols, r_start, c_start)
  total = rows * cols
  res = []
  r = r_start
  c = c_start
  if r >= 0 && r < rows && c >= 0 && c < cols
    res << [r, c]
  end

  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  step = 1
  d = 0

  while res.size < total
    2.times do
      dx, dy = dirs[d % 4]
      step.times do
        r += dx
        c += dy
        if r >= 0 && r < rows && c >= 0 && c < cols
          res << [r, c]
          return res if res.size == total
        end
      end
      d += 1
    end
    step += 1
  end

  res
end
```

## Scala

```scala
object Solution {
    def spiralMatrixIII(rows: Int, cols: Int, rStart: Int, cStart: Int): Array[Array[Int]] = {
        val total = rows * cols
        val result = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
        var r = rStart
        var c = cStart
        result += Array(r, c)

        val dr = Array(0, 1, 0, -1) // East, South, West, North
        val dc = Array(1, 0, -1, 0)

        var step = 1

        while (result.size < total) {
            for (dir <- 0 until 4 if result.size < total) {
                var cnt = 0
                while (cnt < step && result.size < total) {
                    r += dr(dir)
                    c += dc(dir)
                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        result += Array(r, c)
                    }
                    cnt += 1
                }
                if (dir % 2 == 1) step += 1
            }
        }

        result.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn spiral_matrix_iii(rows: i32, cols: i32, r_start: i32, c_start: i32) -> Vec<Vec<i32>> {
        let total = (rows * cols) as usize;
        let mut result: Vec<Vec<i32>> = Vec::with_capacity(total);
        let mut r = r_start;
        let mut c = c_start;

        // starting cell is always inside the grid
        result.push(vec![r, c]);

        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]; // east, south, west, north
        let mut step = 1;
        let mut dir_idx = 0usize;

        while result.len() < total {
            for _ in 0..2 {
                let (dr, dc) = dirs[dir_idx];
                for _ in 0..step {
                    r += dr;
                    c += dc;
                    if r >= 0 && r < rows && c >= 0 && c < cols {
                        result.push(vec![r, c]);
                        if result.len() == total {
                            break;
                        }
                    }
                }
                dir_idx = (dir_idx + 1) % 4;
                if result.len() == total {
                    break;
                }
            }
            step += 1;
        }

        result
    }
}
```

## Racket

```racket
(define/contract (spiral-matrix-iii rows cols rStart cStart)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?
      (listof (listof exact-integer?)))
  (let* ((total (* rows cols))
         (result (make-vector total))
         (dirs (vector (list 0 1)   ; east
                       (list 1 0)   ; south
                       (list 0 -1)  ; west
                       (list -1 0))) ; north
         (r rStart)
         (c cStart)
         (cnt 0)
         (step 1)
         (d 0))
    ;; add the starting position
    (when (and (>= r 0) (< r rows) (>= c 0) (< c cols))
      (vector-set! result cnt (list r c))
      (set! cnt (+ cnt 1)))
    (let loop ()
      (when (< cnt total)
        (for ([repeat (in-range 2)])
          (define dr (first (vector-ref dirs d)))
          (define dc (second (vector-ref dirs d)))
          (for ([s (in-range step)])
            (when (< cnt total)
              (set! r (+ r dr))
              (set! c (+ c dc))
              (when (and (>= r 0) (< r rows) (>= c 0) (< c cols))
                (vector-set! result cnt (list r c))
                (set! cnt (+ cnt 1)))))
          (set! d (modulo (+ d 1) 4)))
        (set! step (+ step 1))
        (loop)))
    ;; convert vector to list in order
    (let build ((i 0) (acc '()))
      (if (= i total)
          (reverse acc)
          (build (+ i 1) (cons (vector-ref result i) acc))))))
```

## Erlang

```erlang
-module(solution).
-export([spiral_matrix_iii/4]).
-spec spiral_matrix_iii(Rows :: integer(), Cols :: integer(), RStart :: integer(), CStart :: integer()) -> [[integer()]].
spiral_matrix_iii(Rows, Cols, RStart, CStart) ->
    Total = Rows * Cols,
    Dir = [{0,1}, {1,0}, {0,-1}, {-1,0}],
    Acc0 = [[RStart, CStart]],
    go(Total, Rows, Cols, RStart, CStart, 1, 0, Dir, Acc0, 1).

go(Total, _Rows, _Cols, _R, _C, _Step, _DirIdx, _DirList, Acc, Count) when Count >= Total ->
    lists:reverse(Acc);
go(Total, Rows, Cols, R, C, Step, DirIdx, DirList, Acc, Count) ->
    {R1, C1, Acc1, Count1} = move(R, C, Step, DirIdx, Rows, Cols, DirList, Acc, Count),
    NextDirIdx = (DirIdx + 1) rem 4,
    {R2, C2, Acc2, Count2} = move(R1, C1, Step, NextDirIdx, Rows, Cols, DirList, Acc1, Count1),
    go(Total, Rows, Cols, R2, C2, Step + 1, (NextDirIdx + 1) rem 4, DirList, Acc2, Count2).

move(R, C, 0, _DirIdx, _Rows, _Cols, _DirList, Acc, Count) ->
    {R, C, Acc, Count};
move(R, C, N, DirIdx, Rows, Cols, DirList, Acc, Count) ->
    {DR, DC} = lists:nth(DirIdx + 1, DirList),
    R2 = R + DR,
    C2 = C + DC,
    case (R2 >= 0 andalso R2 < Rows andalso C2 >= 0 andalso C2 < Cols) of
        true ->
            move(R2, C2, N - 1, DirIdx, Rows, Cols, DirList, [[R2, C2] | Acc], Count + 1);
        false ->
            move(R2, C2, N - 1, DirIdx, Rows, Cols, DirList, Acc, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec spiral_matrix_iii(rows :: integer, cols :: integer, r_start :: integer, c_start :: integer) :: [[integer]]
  def spiral_matrix_iii(rows, cols, r_start, c_start) do
    total = rows * cols
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    init_acc = [[r_start, c_start]]
    walk(r_start, c_start, 0, 1, init_acc, 1, rows, cols, total, dr, dc)
  end

  defp walk(_r, _c, _dir_idx, _step_len, acc, visited, _rows, _cols, total, _dr, _dc) when visited == total do
    Enum.reverse(acc)
  end

  defp walk(r, c, dir_idx, step_len, acc, visited, rows, cols, total, dr, dc) do
    {r1, c1, visited1, acc1} = move(r, c, dir_idx, step_len, acc, visited, rows, cols, dr, dc)
    dir_next = rem(dir_idx + 1, 4)

    {r2, c2, visited2, acc2} = move(r1, c1, dir_next, step_len, acc1, visited1, rows, cols, dr, dc)
    dir_after = rem(dir_next + 1, 4)

    walk(r2, c2, dir_after, step_len + 1, acc2, visited2, rows, cols, total, dr, dc)
  end

  defp move(r, c, dir_idx, steps, acc, visited, rows, cols, dr, dc) do
    Enum.reduce(1..steps, {r, c, visited, acc}, fn _,
        {cur_r, cur_c, vis, a} ->
      nr = cur_r + Enum.at(dr, dir_idx)
      nc = cur_c + Enum.at(dc, dir_idx)

      inside = nr >= 0 and nr < rows and nc >= 0 and nc < cols

      new_vis = if inside, do: vis + 1, else: vis
      new_acc = if inside, do: [[nr, nc] | a], else: a

      {nr, nc, new_vis, new_acc}
    end)
  end
end
```

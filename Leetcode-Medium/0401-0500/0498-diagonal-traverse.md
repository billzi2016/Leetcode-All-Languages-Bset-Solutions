# 0498. Diagonal Traverse

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int m = mat.size();
        if (m == 0) return {};
        int n = mat[0].size();
        vector<int> res;
        res.reserve(m * n);
        int i = 0, j = 0;
        bool up = true;
        while ((int)res.size() < m * n) {
            res.push_back(mat[i][j]);
            if (up) { // moving up-right
                if (j == n - 1) {
                    ++i;
                    up = false;
                } else if (i == 0) {
                    ++j;
                    up = false;
                } else {
                    --i;
                    ++j;
                }
            } else { // moving down-left
                if (i == m - 1) {
                    ++j;
                    up = true;
                } else if (j == 0) {
                    ++i;
                    up = true;
                } else {
                    ++i;
                    --j;
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
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int total = m * n;
        int[] res = new int[total];
        int row = 0, col = 0, idx = 0;
        boolean up = true;
        while (idx < total) {
            res[idx++] = mat[row][col];
            if (up) {
                if (col == n - 1) {          // hit the right border
                    row++;
                    up = false;
                } else if (row == 0) {       // hit the top border
                    col++;
                    up = false;
                } else {
                    row--;
                    col++;
                }
            } else {
                if (row == m - 1) {          // hit the bottom border
                    col++;
                    up = true;
                } else if (col == 0) {       // hit the left border
                    row++;
                    up = true;
                } else {
                    row++;
                    col--;
                }
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        row = col = 0
        up = True
        total = m * n
        while len(result) < total:
            result.append(mat[row][col])
            if up:
                if col == n - 1:
                    row += 1
                    up = False
                elif row == 0:
                    col += 1
                    up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    up = True
                elif col == 0:
                    row += 1
                    up = True
                else:
                    row += 1
                    col -= 1
        return result
```

## Python3

```python
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        row = col = 0
        up = True  # direction flag

        while len(result) < m * n:
            result.append(mat[row][col])

            if up:
                if col == n - 1:          # hit the right border, go down
                    row += 1
                    up = False
                elif row == 0:            # hit the top border, go right
                    col += 1
                    up = False
                else:                     # move up-right
                    row -= 1
                    col += 1
            else:
                if row == m - 1:          # hit the bottom border, go right
                    col += 1
                    up = True
                elif col == 0:            # hit the left border, go down
                    row += 1
                    up = True
                else:                     # move down-left
                    row += 1
                    col -= 1

        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDiagonalOrder(int** mat, int matSize, int* matColSize, int* returnSize) {
    if (matSize == 0 || matColSize == NULL) {
        *returnSize = 0;
        return NULL;
    }
    
    int m = matSize;
    int n = matColSize[0];
    int total = m * n;
    int *res = (int *)malloc(total * sizeof(int));
    if (!res) {
        *returnSize = 0;
        return NULL;
    }
    
    int i = 0, j = 0;
    int idx = 0;
    int up = 1; // 1 means moving up-right, 0 down-left
    
    while (idx < total) {
        res[idx++] = mat[i][j];
        
        if (up) {
            if (j == n - 1) {          // hit right border
                i++;
                up = 0;
            } else if (i == 0) {       // hit top border
                j++;
                up = 0;
            } else {
                i--;
                j++;
            }
        } else {
            if (i == m - 1) {          // hit bottom border
                j++;
                up = 1;
            } else if (j == 0) {       // hit left border
                i++;
                up = 1;
            } else {
                i++;
                j--;
            }
        }
    }
    
    *returnSize = total;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] FindDiagonalOrder(int[][] mat)
    {
        int m = mat.Length;
        int n = mat[0].Length;
        int total = m * n;
        int[] result = new int[total];
        int index = 0;
        int row = 0, col = 0;
        bool up = true;

        while (index < total)
        {
            result[index++] = mat[row][col];

            if (up)
            {
                if (col == n - 1)
                {
                    row++;
                    up = false;
                }
                else if (row == 0)
                {
                    col++;
                    up = false;
                }
                else
                {
                    row--;
                    col++;
                }
            }
            else
            {
                if (row == m - 1)
                {
                    col++;
                    up = true;
                }
                else if (col == 0)
                {
                    row++;
                    up = true;
                }
                else
                {
                    row++;
                    col--;
                }
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const total = m * n;
    const result = new Array(total);
    let idx = 0;
    let i = 0, j = 0;
    let up = true; // direction flag
    
    while (idx < total) {
        result[idx++] = mat[i][j];
        
        if (up) {
            // moving up-right
            if (j === n - 1) {          // hit right border, move down
                i++;
                up = false;
            } else if (i === 0) {       // hit top border, move right
                j++;
                up = false;
            } else {
                i--;
                j++;
            }
        } else {
            // moving down-left
            if (i === m - 1) {          // hit bottom border, move right
                j++;
                up = true;
            } else if (j === 0) {       // hit left border, move down
                i++;
                up = true;
            } else {
                i++;
                j--;
            }
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function findDiagonalOrder(mat: number[][]): number[] {
    const m = mat.length;
    if (m === 0) return [];
    const n = mat[0].length;
    const total = m * n;
    const result: number[] = new Array(total);
    let row = 0, col = 0;
    let up = true;

    for (let i = 0; i < total; i++) {
        result[i] = mat[row][col];

        if (up) {
            if (col === n - 1) {
                row++;
                up = false;
            } else if (row === 0) {
                col++;
                up = false;
            } else {
                row--;
                col++;
            }
        } else {
            if (row === m - 1) {
                col++;
                up = true;
            } else if (col === 0) {
                row++;
                up = true;
            } else {
                row++;
                col--;
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[]
     */
    function findDiagonalOrder($mat) {
        $m = count($mat);
        if ($m == 0) return [];
        $n = count($mat[0]);
        $total = $m * $n;
        $result = [];

        $row = 0;
        $col = 0;
        $up = true; // direction flag

        for ($i = 0; $i < $total; $i++) {
            $result[] = $mat[$row][$col];

            if ($up) { // moving up-right
                $newRow = $row - 1;
                $newCol = $col + 1;

                if ($newRow < 0 || $newCol >= $n) {
                    $up = false; // change direction

                    if ($newCol >= $n && $newRow < 0) {          // top‑right corner
                        $row += 1;
                    } elseif ($newCol >= $n) {                  // hit right border
                        $row += 1;
                    } else {                                    // hit top border
                        $col += 1;
                    }
                } else {
                    $row = $newRow;
                    $col = $newCol;
                }
            } else { // moving down-left
                $newRow = $row + 1;
                $newCol = $col - 1;

                if ($newRow >= $m || $newCol < 0) {
                    $up = true; // change direction

                    if ($newRow >= $m && $newCol < 0) {          // bottom‑left corner
                        $col += 1;
                    } elseif ($newRow >= $m) {                  // hit bottom border
                        $col += 1;
                    } else {                                    // hit left border
                        $row += 1;
                    }
                } else {
                    $row = $newRow;
                    $col = $newCol;
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
    func findDiagonalOrder(_ mat: [[Int]]) -> [Int] {
        let m = mat.count
        guard m > 0 else { return [] }
        let n = mat[0].count
        var result = [Int]()
        result.reserveCapacity(m * n)
        var row = 0, col = 0
        var up = true
        while result.count < m * n {
            result.append(mat[row][col])
            if up {
                if col == n - 1 {
                    row += 1
                    up = false
                } else if row == 0 {
                    col += 1
                    up = false
                } else {
                    row -= 1
                    col += 1
                }
            } else {
                if row == m - 1 {
                    col += 1
                    up = true
                } else if col == 0 {
                    row += 1
                    up = true
                } else {
                    row += 1
                    col -= 1
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
    fun findDiagonalOrder(mat: Array<IntArray>): IntArray {
        val m = mat.size
        val n = mat[0].size
        val total = m * n
        val result = IntArray(total)
        var row = 0
        var col = 0
        var up = true
        for (k in 0 until total) {
            result[k] = mat[row][col]
            if (up) {
                if (col == n - 1) {
                    row++
                    up = false
                } else if (row == 0) {
                    col++
                    up = false
                } else {
                    row--
                    col++
                }
            } else {
                if (row == m - 1) {
                    col++
                    up = true
                } else if (col == 0) {
                    row++
                    up = true
                } else {
                    row++
                    col--
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findDiagonalOrder(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    int total = m * n;
    List<int> res = List.filled(total, 0);
    int idx = 0;
    int row = 0, col = 0;
    bool up = true;

    while (idx < total) {
      res[idx++] = mat[row][col];
      if (up) {
        if (col == n - 1) {
          row++;
          up = false;
        } else if (row == 0) {
          col++;
          up = false;
        } else {
          row--;
          col++;
        }
      } else {
        if (row == m - 1) {
          col++;
          up = true;
        } else if (col == 0) {
          row++;
          up = true;
        } else {
          row++;
          col--;
        }
      }
    }

    return res;
  }
}
```

## Golang

```go
func findDiagonalOrder(mat [][]int) []int {
    m := len(mat)
    if m == 0 {
        return []int{}
    }
    n := len(mat[0])
    total := m * n
    result := make([]int, 0, total)

    row, col := 0, 0
    up := true

    for len(result) < total {
        result = append(result, mat[row][col])

        if up {
            // moving up-right
            if col == n-1 { // hit right border, go down
                row++
                up = false
            } else if row == 0 { // hit top border, go right
                col++
                up = false
            } else {
                row--
                col++
            }
        } else {
            // moving down-left
            if row == m-1 { // hit bottom border, go right
                col++
                up = true
            } else if col == 0 { // hit left border, go down
                row++
                up = true
            } else {
                row++
                col--
            }
        }
    }

    return result
}
```

## Ruby

```ruby
def find_diagonal_order(mat)
  m = mat.length
  n = mat[0].length
  total = m * n
  result = Array.new(total)
  idx = 0
  r = 0
  c = 0
  up = true

  while idx < total
    result[idx] = mat[r][c]
    idx += 1

    if up
      if c == n - 1
        r += 1
        up = false
      elsif r == 0
        c += 1
        up = false
      else
        r -= 1
        c += 1
      end
    else
      if r == m - 1
        c += 1
        up = true
      elsif c == 0
        r += 1
        up = true
      else
        r += 1
        c -= 1
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def findDiagonalOrder(mat: Array[Array[Int]]): Array[Int] = {
        val m = mat.length
        if (m == 0) return Array.emptyIntArray
        val n = mat(0).length
        val res = new Array[Int](m * n)
        var row = 0
        var col = 0
        var idx = 0
        var upward = true
        while (idx < m * n) {
            res(idx) = mat(row)(col)
            idx += 1
            if (upward) {
                if (col == n - 1) {
                    row += 1
                } else if (row == 0) {
                    col += 1
                } else {
                    row -= 1
                    col += 1
                }
            } else {
                if (row == m - 1) {
                    col += 1
                } else if (col == 0) {
                    row += 1
                } else {
                    row += 1
                    col -= 1
                }
            }
            upward = !upward
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let m = mat.len();
        if m == 0 {
            return Vec::new();
        }
        let n = mat[0].len();
        let mut result = Vec::with_capacity(m * n);
        let (mut row, mut col) = (0usize, 0usize);
        let mut up = true;

        while result.len() < m * n {
            result.push(mat[row][col]);

            if up {
                // moving up-right
                if col + 1 == n {
                    // hit the last column, go down to next row
                    row += 1;
                    up = false;
                } else if row == 0 {
                    // hit the top row, move right
                    col += 1;
                    up = false;
                } else {
                    row -= 1;
                    col += 1;
                }
            } else {
                // moving down-left
                if row + 1 == m {
                    // hit the last row, go right
                    col += 1;
                    up = true;
                } else if col == 0 {
                    // hit the first column, move down
                    row += 1;
                    up = true;
                } else {
                    row += 1;
                    col -= 1;
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (find-diagonal-order mat)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((rows (length mat))
         (cols (if (zero? rows) 0 (length (car mat))))
         (vec (list->vector (map list->vector mat)))
         (total (* rows cols))
         (result (make-vector total))
         (i 0)
         (j 0)
         (direction #t) ; #t = up-right, #f = down-left
         (idx 0))
    (let loop ()
      (when (< idx total)
        (vector-set! result idx (vector-ref (vector-ref vec i) j))
        (set! idx (+ idx 1))
        (if direction
            (let ((ni (- i 1))
                  (nj (+ j 1)))
              (if (and (>= ni 0) (< nj cols))
                  (begin (set! i ni) (set! j nj))
                  (begin
                    (if (= i 0)
                        (set! j (+ j 1))
                        (set! i (+ i 1)))
                    (set! direction (not direction)))))
            (let ((ni (+ i 1))
                  (nj (- j 1)))
              (if (and (< ni rows) (>= nj 0))
                  (begin (set! i ni) (set! j nj))
                  (begin
                    (if (= j 0)
                        (set! i (+ i 1))
                        (set! j (+ j 1)))
                    (set! direction (not direction))))))
        (loop)))
    (vector->list result)))
```

## Erlang

```erlang
-module(diagonal_traverse).
-export([find_diagonal_order/1]).

-spec find_diagonal_order(Mat :: [[integer()]]) -> [integer()].
find_diagonal_order(Mat) ->
    Rows = length(Mat),
    Cols = case Mat of
               [] -> 0;
               [First|_] -> length(First)
           end,
    Total = Rows * Cols,
    loop(Mat, Rows, Cols, 0, 0, true, Total, []).

loop(_Mat, _Rows, _Cols, _I, _J, _Dir, 0, Acc) ->
    lists:reverse(Acc);
loop(Mat, Rows, Cols, I, J, Dir, Remaining, Acc) ->
    Row = lists:nth(I + 1, Mat),
    Elem = lists:nth(J + 1, Row),
    NewAcc = [Elem | Acc],
    case Dir of
        true -> % moving up
            if I == 0 orelse J == Cols - 1 ->
                    NewDir = false,
                    if J < Cols - 1 ->
                        NextI = I,
                        NextJ = J + 1;
                       true ->
                        NextI = I + 1,
                        NextJ = J
                    end;
               true ->
                    NewDir = Dir,
                    NextI = I - 1,
                    NextJ = J + 1
            end;
        false -> % moving down
            if J == 0 orelse I == Rows - 1 ->
                    NewDir = true,
                    if I < Rows - 1 ->
                        NextI = I + 1,
                        NextJ = J;
                       true ->
                        NextI = I,
                        NextJ = J + 1
                    end;
               true ->
                    NewDir = Dir,
                    NextI = I + 1,
                    NextJ = J - 1
            end
    end,
    loop(Mat, Rows, Cols, NextI, NextJ, NewDir, Remaining - 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_diagonal_order(mat :: [[integer]]) :: [integer]
  def find_diagonal_order(mat) do
    m = length(mat)
    n = mat |> hd() |> length()
    matrix = mat |> Enum.map(&List.to_tuple/1) |> List.to_tuple
    total = m * n
    go(m, n, 0, 0, true, matrix, total, 0, [])
  end

  defp go(_m, _n, _i, _j, _up, _matrix, total, count, acc) when count == total do
    :lists.reverse(acc)
  end

  defp go(m, n, i, j, up, matrix, total, count, acc) do
    val = elem(elem(matrix, i), j)
    new_acc = [val | acc]
    new_count = count + 1

    if up do
      cond do
        j == n - 1 ->
          go(m, n, i + 1, j, false, matrix, total, new_count, new_acc)

        i == 0 ->
          go(m, n, i, j + 1, false, matrix, total, new_count, new_acc)

        true ->
          go(m, n, i - 1, j + 1, true, matrix, total, new_count, new_acc)
      end
    else
      cond do
        i == m - 1 ->
          go(m, n, i, j + 1, true, matrix, total, new_count, new_acc)

        j == 0 ->
          go(m, n, i + 1, j, true, matrix, total, new_count, new_acc)

        true ->
          go(m, n, i + 1, j - 1, false, matrix, total, new_count, new_acc)
      end
    end
  end
end
```

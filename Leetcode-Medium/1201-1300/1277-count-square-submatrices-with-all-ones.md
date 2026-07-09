# 1277. Count Square Submatrices with All Ones

## Cpp

```cpp
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return 0;
        int n = matrix[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        int ans = 0;
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (matrix[i - 1][j - 1] == 1) {
                    dp[i][j] = min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]}) + 1;
                    ans += dp[i][j];
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countSquares(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] dp = new int[rows + 1][cols + 1];
        int total = 0;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (matrix[i - 1][j - 1] == 1) {
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
                    total += dp[i][j];
                }
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        total = 0
        for i in range(1, m + 1):
            row = matrix[i - 1]
            cur_dp = dp[i]
            prev_dp = dp[i - 1]
            for j in range(1, n + 1):
                if row[j - 1] == 1:
                    cur_dp[j] = min(prev_dp[j], cur_dp[j - 1], prev_dp[j - 1]) + 1
                    total += cur_dp[j]
        return total
```

## Python3

```python
from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        total = 0
        for i in range(rows):
            prev = 0
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i][j - 1] == 1:
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                    total += dp[j]
                else:
                    dp[j] = 0
                prev = temp
        return total
```

## C

```c
#include <stdlib.h>

int countSquares(int** matrix, int matrixSize, int* matrixColSize) {
    int rows = matrixSize;
    if (rows == 0) return 0;
    int cols = matrixColSize[0];

    // Allocate DP table with an extra row and column initialized to 0
    int **dp = (int **)malloc((rows + 1) * sizeof(int *));
    for (int i = 0; i <= rows; ++i) {
        dp[i] = (int *)calloc(cols + 1, sizeof(int));
    }

    int total = 0;
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= cols; ++j) {
            if (matrix[i - 1][j - 1] == 1) {
                int a = dp[i - 1][j];
                int b = dp[i][j - 1];
                int c = dp[i - 1][j - 1];
                int min = a < b ? a : b;
                min = min < c ? min : c;
                dp[i][j] = min + 1;
                total += dp[i][j];
            }
        }
    }

    // Free DP table
    for (int i = 0; i <= rows; ++i) {
        free(dp[i]);
    }
    free(dp);

    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountSquares(int[][] matrix)
    {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0)
            return 0;

        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int[,] dp = new int[rows + 1, cols + 1];
        int total = 0;

        for (int i = 1; i <= rows; i++)
        {
            for (int j = 1; j <= cols; j++)
            {
                if (matrix[i - 1][j - 1] == 1)
                {
                    dp[i, j] = Math.Min(dp[i - 1, j], Math.Min(dp[i, j - 1], dp[i - 1, j - 1])) + 1;
                    total += dp[i, j];
                }
            }
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function(matrix) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return 0;
    const rows = matrix.length;
    const cols = matrix[0].length;
    const dp = new Array(cols + 1).fill(0);
    let total = 0;
    for (let i = 0; i < rows; i++) {
        let prev = 0; // dp value from previous row and previous column (top-left)
        for (let j = 1; j <= cols; j++) {
            const temp = dp[j]; // store current top value before updating
            if (matrix[i][j - 1] === 1) {
                dp[j] = Math.min(dp[j], dp[j - 1], prev) + 1;
                total += dp[j];
            } else {
                dp[j] = 0;
            }
            prev = temp; // update top-left for next column
        }
    }
    return total;
};
```

## Typescript

```typescript
function countSquares(matrix: number[][]): number {
    const rows = matrix.length;
    const cols = matrix[0].length;
    const dp: number[][] = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));
    let total = 0;

    for (let i = 1; i <= rows; i++) {
        for (let j = 1; j <= cols; j++) {
            if (matrix[i - 1][j - 1] === 1) {
                dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
                total += dp[i][j];
            }
        }
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function countSquares($matrix) {
        $rows = count($matrix);
        if ($rows == 0) return 0;
        $cols = count($matrix[0]);
        if ($cols == 0) return 0;

        // DP table initialized with zeros
        $dp = array_fill(0, $rows, array_fill(0, $cols, 0));
        $ans = 0;

        for ($i = 0; $i < $rows; ++$i) {
            for ($j = 0; $j < $cols; ++$j) {
                if ($matrix[$i][$j] == 1) {
                    if ($i == 0 || $j == 0) {
                        $dp[$i][$j] = 1;
                    } else {
                        $dp[$i][$j] = min($dp[$i-1][$j], $dp[$i][$j-1], $dp[$i-1][$j-1]) + 1;
                    }
                    $ans += $dp[$i][$j];
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countSquares(_ matrix: [[Int]]) -> Int {
        let rows = matrix.count
        guard rows > 0 else { return 0 }
        let cols = matrix[0].count
        var dp = Array(repeating: Array(repeating: 0, count: cols + 1), count: rows + 1)
        var total = 0
        
        for i in 1...rows {
            for j in 1...cols {
                if matrix[i - 1][j - 1] == 1 {
                    let minNeighbor = min(dp[i - 1][j], dp[i][j - 1])
                    dp[i][j] = min(minNeighbor, dp[i - 1][j - 1]) + 1
                    total += dp[i][j]
                }
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSquares(matrix: Array<IntArray>): Int {
        val m = matrix.size
        if (m == 0) return 0
        val n = matrix[0].size
        val dp = Array(m + 1) { IntArray(n + 1) }
        var ans = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (matrix[i][j] == 1) {
                    dp[i + 1][j + 1] = minOf(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    ans += dp[i + 1][j + 1]
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int countSquares(List<List<int>> matrix) {
    if (matrix.isEmpty || matrix[0].isEmpty) return 0;
    final rows = matrix.length;
    final cols = matrix[0].length;
    final dp = List.generate(rows + 1, (_) => List.filled(cols + 1, 0));
    int ans = 0;

    for (int i = 1; i <= rows; ++i) {
      for (int j = 1; j <= cols; ++j) {
        if (matrix[i - 1][j - 1] == 1) {
          dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
          ans += dp[i][j];
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countSquares(matrix [][]int) int {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return 0
    }
    rows, cols := len(matrix), len(matrix[0])
    dp := make([][]int, rows+1)
    for i := range dp {
        dp[i] = make([]int, cols+1)
    }

    ans := 0
    for i := 1; i <= rows; i++ {
        for j := 1; j <= cols; j++ {
            if matrix[i-1][j-1] == 1 {
                // compute min of three neighbors
                a, b, c := dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
                // find minimum
                if a > b {
                    a = b
                }
                if a > c {
                    a = c
                }
                dp[i][j] = a + 1
                ans += dp[i][j]
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def count_squares(matrix)
  rows = matrix.length
  cols = matrix[0].length
  dp = Array.new(rows + 1) { Array.new(cols + 1, 0) }
  ans = 0

  (1..rows).each do |i|
    (1..cols).each do |j|
      if matrix[i - 1][j - 1] == 1
        dp[i][j] = [dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]].min + 1
        ans += dp[i][j]
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countSquares(matrix: Array[Array[Int]]): Int = {
        val m = matrix.length
        if (m == 0) return 0
        val n = matrix(0).length
        var ans = 0
        val dp = new Array[Int](n + 1)
        for (i <- 0 until m) {
            var prev = 0
            for (j <- 1 to n) {
                val temp = dp(j)
                if (matrix(i)(j - 1) == 1) {
                    dp(j) = 1 + math.min(prev, math.min(dp(j - 1), dp(j)))
                    ans += dp(j)
                } else {
                    dp(j) = 0
                }
                prev = temp
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_squares(matrix: Vec<Vec<i32>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }
        let m = matrix.len();
        let n = matrix[0].len();
        let mut dp = vec![vec![0i32; n + 1]; m + 1];
        let mut ans: i32 = 0;
        for i in 0..m {
            for j in 0..n {
                if matrix[i][j] == 1 {
                    let min_val = dp[i][j + 1].min(dp[i + 1][j]).min(dp[i][j]);
                    dp[i + 1][j + 1] = min_val + 1;
                    ans += dp[i + 1][j + 1];
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-squares matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length matrix))
         (cols (if (null? matrix) 0 (length (car matrix))))
         ;; dp is a (rows+1) x (cols+1) table initialized to 0
         (dp (let ([v (make-vector (+ rows 1))])
               (for ([i (in-range (+ rows 1))])
                 (vector-set! v i (make-vector (+ cols 1) 0)))
               v))
         (ans 0))
    (for ([i (in-range rows)])
      (let ((row (list-ref matrix i)))
        (for ([j (in-range cols)])
          (if (= (list-ref row j) 1)
              (let* ((up   (vector-ref (vector-ref dp i) (+ j 1)))   ; dp[i][j+1]
                     (left (vector-ref (vector-ref dp (+ i 1)) j))   ; dp[i+1][j]
                     (diag (vector-ref (vector-ref dp i) j))       ; dp[i][j]
                     (val  (+ 1 (min up left diag))))
                (vector-set! (vector-ref dp (+ i 1)) (+ j 1) val)
                (set! ans (+ ans val)))
              (vector-set! (vector-ref dp (+ i 1)) (+ j 1) 0)))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_squares/1]).

count_squares(Matrix) ->
    case Matrix of
        [] -> 0;
        _ ->
            Cols = length(hd(Matrix)),
            DpInit = lists:duplicate(Cols, 0),
            {_, Total} = lists:foldl(fun(Row, {DpPrev, Acc}) ->
                {NewDp, RowSum} = process_row(Row, DpPrev),
                {NewDp, Acc + RowSum}
            end, {DpInit, 0}, Matrix),
            Total
    end.

process_row(RowVals, DpPrev) ->
    process_row(RowVals, DpPrev, 0, 0, [], 0).

process_row([], [], _PrevDiag, _LeftVal, RevAcc, Sum) ->
    {lists:reverse(RevAcc), Sum};
process_row([Cell|RestCells], [Top|RestTop], PrevDiag, LeftVal, RevAcc, Sum) ->
    if Cell =:= 1 ->
            Min = min(min(PrevDiag, LeftVal), Top),
            NewVal = Min + 1,
            process_row(RestCells, RestTop, Top, NewVal, [NewVal|RevAcc], Sum + NewVal);
       true ->
            process_row(RestCells, RestTop, Top, 0, [0|RevAcc], Sum)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_squares(matrix :: [[integer]]) :: integer
  def count_squares([]), do: 0

  def count_squares(matrix) do
    cols = matrix |> hd() |> length()
    init_prev = List.duplicate(0, cols)

    {total, _} =
      Enum.reduce(matrix, {0, init_prev}, fn row, {acc, prev_dp} ->
        {rev_cur, new_total, _prev_diag} =
          Enum.zip(row, prev_dp)
          |> Enum.reduce({[], acc, 0}, fn {val, up}, {cur_rev, tot, prev_diag} ->
            left = case cur_rev do
              [] -> 0
              [h | _] -> h
            end

            cur =
              if val == 1 do
                1 + min(min(left, up), prev_diag)
              else
                0
              end

            {[cur | cur_rev], tot + cur, up}
          end)

        new_dp = Enum.reverse(rev_cur)
        {new_total, new_dp}
      end)

    total
  end
end
```

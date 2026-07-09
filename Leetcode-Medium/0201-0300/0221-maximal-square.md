# 0221. Maximal Square

## Cpp

```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        vector<int> dp(n + 1, 0);
        int maxSide = 0, prev = 0;
        for (int i = 1; i <= m; ++i) {
            prev = 0;
            for (int j = 1; j <= n; ++j) {
                int temp = dp[j];
                if (matrix[i - 1][j - 1] == '1') {
                    dp[j] = min({dp[j], dp[j - 1], prev}) + 1;
                    maxSide = max(maxSide, dp[j]);
                } else {
                    dp[j] = 0;
                }
                prev = temp;
            }
        }
        return maxSide * maxSide;
    }
};
```

## Java

```java
class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
        int rows = matrix.length, cols = matrix[0].length;
        int[] dp = new int[cols + 1];
        int maxSide = 0, prev = 0; // prev holds dp[j-1] from previous row (top-left)
        for (int i = 1; i <= rows; i++) {
            prev = 0;
            for (int j = 1; j <= cols; j++) {
                int temp = dp[j];
                if (matrix[i - 1][j - 1] == '1') {
                    dp[j] = Math.min(Math.min(dp[j], dp[j - 1]), prev) + 1;
                    maxSide = Math.max(maxSide, dp[j]);
                } else {
                    dp[j] = 0;
                }
                prev = temp;
            }
        }
        return maxSide * maxSide;
    }
}
```

## Python

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0  # dp[j-1] from previous row (top-left diagonal)

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev = temp
            prev = 0  # reset for next row's first column

        return max_side * max_side
```

## Python3

```python
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0  # dp[j-1] from previous row (top-left)

        for i in range(1, rows + 1):
            prev = 0
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return max_side * max_side
```

## C

```c
#include <stdlib.h>

int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0 || matrixColSize[0] == 0) return 0;
    int rows = matrixSize;
    int cols = matrixColSize[0];
    int *dp = (int *)calloc(cols + 1, sizeof(int));
    int maxSide = 0;

    for (int i = 1; i <= rows; ++i) {
        int prev = 0; // dp[i-1][j-1]
        for (int j = 1; j <= cols; ++j) {
            int temp = dp[j]; // dp[i-1][j] before update
            if (matrix[i - 1][j - 1] == '1') {
                int minVal = dp[j];
                if (dp[j - 1] < minVal) minVal = dp[j - 1];
                if (prev < minVal)   minVal = prev;
                dp[j] = minVal + 1;
                if (dp[j] > maxSide) maxSide = dp[j];
            } else {
                dp[j] = 0;
            }
            prev = temp;
        }
    }

    free(dp);
    return maxSide * maxSide;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximalSquare(char[][] matrix)
    {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0)
            return 0;

        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int[] dp = new int[cols + 1];
        int maxSide = 0, prev = 0;

        for (int i = 1; i <= rows; i++)
        {
            prev = 0;
            for (int j = 1; j <= cols; j++)
            {
                int temp = dp[j];
                if (matrix[i - 1][j - 1] == '1')
                {
                    dp[j] = Math.Min(Math.Min(dp[j], dp[j - 1]), prev) + 1;
                    maxSide = Math.Max(maxSide, dp[j]);
                }
                else
                {
                    dp[j] = 0;
                }
                prev = temp;
            }
        }

        return maxSide * maxSide;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return 0;
    const rows = matrix.length, cols = matrix[0].length;
    const dp = new Array(cols + 1).fill(0);
    let maxSide = 0, prev = 0;

    for (let i = 1; i <= rows; i++) {
        prev = 0;
        for (let j = 1; j <= cols; j++) {
            const temp = dp[j];
            if (matrix[i - 1][j - 1] === '1') {
                dp[j] = Math.min(dp[j], dp[j - 1], prev) + 1;
                maxSide = Math.max(maxSide, dp[j]);
            } else {
                dp[j] = 0;
            }
            prev = temp;
        }
    }

    return maxSide * maxSide;
};
```

## Typescript

```typescript
function maximalSquare(matrix: string[][]): number {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return 0;
    const m = matrix.length, n = matrix[0].length;
    let maxSide = 0;
    const dp = new Array(n + 1).fill(0);
    let prev = 0;
    for (let i = 1; i <= m; i++) {
        prev = 0;
        for (let j = 1; j <= n; j++) {
            const temp = dp[j];
            if (matrix[i - 1][j - 1] === '1') {
                dp[j] = Math.min(dp[j], dp[j - 1], prev) + 1;
                maxSide = Math.max(maxSide, dp[j]);
            } else {
                dp[j] = 0;
            }
            prev = temp;
        }
    }
    return maxSide * maxSide;
}
```

## Php

```php
class Solution {
    /**
     * @param String[][] $matrix
     * @return Integer
     */
    function maximalSquare($matrix) {
        $rows = count($matrix);
        if ($rows == 0) return 0;
        $cols = count($matrix[0]);
        $dp = array_fill(0, $cols + 1, 0);
        $maxSide = 0;
        for ($i = 1; $i <= $rows; $i++) {
            $prev = 0;
            for ($j = 1; $j <= $cols; $j++) {
                $temp = $dp[$j];
                if ($matrix[$i - 1][$j - 1] === '1') {
                    $dp[$j] = min($dp[$j], $dp[$j - 1], $prev) + 1;
                    if ($dp[$j] > $maxSide) {
                        $maxSide = $dp[$j];
                    }
                } else {
                    $dp[$j] = 0;
                }
                $prev = $temp;
            }
        }
        return $maxSide * $maxSide;
    }
}
```

## Swift

```swift
class Solution {
    func maximalSquare(_ matrix: [[Character]]) -> Int {
        let m = matrix.count
        guard m > 0 else { return 0 }
        let n = matrix[0].count
        var dp = Array(repeating: 0, count: n + 1)
        var maxSide = 0
        var prev = 0
        
        for i in 1...m {
            prev = 0
            for j in 1...n {
                let temp = dp[j]
                if matrix[i - 1][j - 1] == "1" {
                    let left = dp[j - 1]
                    let up = dp[j]
                    let diag = prev
                    dp[j] = min(min(left, up), diag) + 1
                    maxSide = max(maxSide, dp[j])
                } else {
                    dp[j] = 0
                }
                prev = temp
            }
        }
        return maxSide * maxSide
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximalSquare(matrix: Array<CharArray>): Int {
        if (matrix.isEmpty() || matrix[0].isEmpty()) return 0
        val rows = matrix.size
        val cols = matrix[0].size
        var maxSide = 0
        val dp = IntArray(cols + 1)
        var prev = 0
        for (i in 1..rows) {
            for (j in 1..cols) {
                val temp = dp[j]
                if (matrix[i - 1][j - 1] == '1') {
                    dp[j] = minOf(dp[j], dp[j - 1], prev) + 1
                    maxSide = kotlin.math.max(maxSide, dp[j])
                } else {
                    dp[j] = 0
                }
                prev = temp
            }
            prev = 0
        }
        return maxSide * maxSide
    }
}
```

## Dart

```dart
class Solution {
  int maximalSquare(List<List<String>> matrix) {
    if (matrix.isEmpty || matrix[0].isEmpty) return 0;
    int m = matrix.length;
    int n = matrix[0].length;
    List<int> dp = List.filled(n + 1, 0);
    int maxSide = 0;
    for (int i = 1; i <= m; i++) {
      int prev = 0;
      for (int j = 1; j <= n; j++) {
        int temp = dp[j];
        if (matrix[i - 1][j - 1] == '1') {
          dp[j] = 1 + _min(dp[j], dp[j - 1], prev);
          if (dp[j] > maxSide) maxSide = dp[j];
        } else {
          dp[j] = 0;
        }
        prev = temp;
      }
    }
    return maxSide * maxSide;
  }

  int _min(int a, int b, int c) {
    int m = a < b ? a : b;
    return m < c ? m : c;
  }
}
```

## Golang

```go
func maximalSquare(matrix [][]byte) int {
    rows := len(matrix)
    if rows == 0 {
        return 0
    }
    cols := len(matrix[0])
    dp := make([]int, cols+1)
    maxSide := 0
    prev := 0

    for i := 1; i <= rows; i++ {
        prev = 0
        for j := 1; j <= cols; j++ {
            temp := dp[j]
            if matrix[i-1][j-1] == '1' {
                minVal := dp[j]
                if dp[j-1] < minVal {
                    minVal = dp[j-1]
                }
                if prev < minVal {
                    minVal = prev
                }
                dp[j] = minVal + 1
                if dp[j] > maxSide {
                    maxSide = dp[j]
                }
            } else {
                dp[j] = 0
            }
            prev = temp
        }
    }
    return maxSide * maxSide
}
```

## Ruby

```ruby
# @param {Character[][]} matrix
# @return {Integer}
def maximal_square(matrix)
  return 0 if matrix.nil? || matrix.empty? || matrix[0].empty?

  rows = matrix.size
  cols = matrix[0].size
  dp = Array.new(cols, 0)
  max_side = 0

  rows.times do |i|
    prev = 0
    cols.times do |j|
      temp = dp[j]
      if matrix[i][j] == '1'
        if j == 0
          dp[j] = 1
        else
          dp[j] = [dp[j], dp[j - 1], prev].min + 1
        end
        max_side = dp[j] if dp[j] > max_side
      else
        dp[j] = 0
      end
      prev = temp
    end
  end

  max_side * max_side
end
```

## Scala

```scala
object Solution {
    def maximalSquare(matrix: Array[Array[Char]]): Int = {
        if (matrix.isEmpty || matrix.head.isEmpty) return 0
        val rows = matrix.length
        val cols = matrix(0).length
        val dp = new Array[Int](cols + 1)
        var maxSide = 0
        var prev = 0

        for (i <- 1 to rows) {
            prev = 0
            for (j <- 1 to cols) {
                val temp = dp(j)
                if (matrix(i - 1)(j - 1) == '1') {
                    dp(j) = math.min(math.min(dp(j), dp(j - 1)), prev) + 1
                    maxSide = math.max(maxSide, dp(j))
                } else {
                    dp(j) = 0
                }
                prev = temp
            }
        }

        maxSide * maxSide
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }
        let m = matrix.len();
        let n = matrix[0].len();
        let mut prev = vec![0usize; n + 1];
        let mut max_side = 0usize;

        for i in 0..m {
            let mut cur = vec![0usize; n + 1];
            for j in 0..n {
                if matrix[i][j] == '1' {
                    let min_val = std::cmp::min(prev[j + 1], std::cmp::min(cur[j], prev[j]));
                    cur[j + 1] = min_val + 1;
                    if cur[j + 1] > max_side {
                        max_side = cur[j + 1];
                    }
                }
            }
            prev = cur;
        }

        (max_side * max_side) as i32
    }
}
```

## Racket

```racket
(define/contract (maximal-square matrix)
  (-> (listof (listof char?)) exact-integer?)
  (let* ((m (length matrix))
         (n (if (zero? m) 0 (length (first matrix)))))
    (define dp (make-vector (+ n 1) 0))
    (define max-side 0)
    (for ([i (in-range 1 (+ m 1))])
      (let ((prev 0))
        (for ([j (in-range 1 (+ n 1))])
          (let* ((temp (vector-ref dp j))
                 (cell (list-ref (list-ref matrix (- i 1)) (- j 1))))
            (if (char=? cell #\1)
                (let ((new (add1 (min (vector-ref dp j)      ; top
                                      (vector-ref dp (- j 1)) ; left
                                      prev))))               ; top-left
                  (vector-set! dp j new)
                  (when (> new max-side) (set! max-side new)))
                (vector-set! dp j 0))
            (set! prev temp)))))
    (* max-side max-side)))
```

## Erlang

```erlang
-module(solution).
-export([maximal_square/1]).

-spec maximal_square(Matrix :: [[char()]]) -> integer().
maximal_square([]) ->
    0;
maximal_square(Matrix) ->
    N = length(hd(Matrix)),
    ZeroRow = lists:duplicate(N + 1, 0),
    {MaxSide, _} = lists:foldl(
        fun(Row, {CurMax, PrevDP}) ->
            {CurrList, NewMax} = process_row(Row, PrevDP, 0, [], CurMax),
            NextPrev = [0 | CurrList],
            {NewMax, NextPrev}
        end,
        {0, ZeroRow},
        Matrix
    ),
    MaxSide * MaxSide.

% Row processing: returns {CurrentDPValuesWithoutLeadingZero, UpdatedMaxSide}
-spec process_row([char()], [integer()], integer(), [integer()], integer()) ->
          {[integer()], integer()}.
process_row([], _PrevDP, _Left, AccRev, Max) ->
    {lists:reverse(AccRev), Max};
process_row([Cell | RestCells], PrevDP = [_Diag | RestPrev], Left, AccRev, Max) ->
    Up = case RestPrev of
        [] -> 0;
        [U | _] -> U
    end,
    if Cell == $1 ->
            MinVal = min(min(Left, Up), hd(PrevDP)),
            Curr = MinVal + 1,
            NewMax = max(Max, Curr);
       true ->
            Curr = 0,
            NewMax = Max
    end,
    process_row(RestCells, RestPrev, Curr, [Curr | AccRev], NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximal_square(matrix :: [[char]]) :: integer
  def maximal_square(matrix) do
    rows = length(matrix)

    if rows == 0 do
      0
    else
      cols = matrix |> List.first() |> length()

      {max_side, _} =
        Enum.reduce(matrix, {0, :erlang.make_tuple(cols + 1, 0)}, fn row,
                                                                   {max_acc, prev_tuple} ->
          {cur_rev, new_max} =
            Enum.with_index(row, 1)
            |> Enum.reduce({[0], max_acc}, fn {val, j},
                                             {cur_rev_acc, cur_max_acc} ->
              if val == "1" do
                up = elem(prev_tuple, j)
                left = hd(cur_rev_acc)
                diag = elem(prev_tuple, j - 1)

                size = min(min(up, left), diag) + 1
                {[size | cur_rev_acc], max(cur_max_acc, size)}
              else
                {[0 | cur_rev_acc], cur_max_acc}
              end
            end)

          cur_tuple = List.to_tuple(Enum.reverse(cur_rev))
          {new_max, cur_tuple}
        end)

      max_side * max_side
    end
  end
end
```

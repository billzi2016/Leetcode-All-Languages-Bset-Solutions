# 0861. Score After Flipping Matrix

## Cpp

```cpp
class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long score = (1LL << (n - 1)) * m; // first column all ones after row flips
        for (int col = 1; col < n; ++col) {
            int sameCount = 0;
            for (int row = 0; row < m; ++row) {
                if (grid[row][col] == grid[row][0]) ++sameCount;
            }
            int maxOnes = max(sameCount, m - sameCount);
            score += (1LL << (n - col - 1)) * maxOnes;
        }
        return static_cast<int>(score);
    }
};
```

## Java

```java
class Solution {
    public int matrixScore(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int score = 0;
        for (int col = 0; col < n; col++) {
            int cntSame = 0;
            for (int row = 0; row < m; row++) {
                if (grid[row][col] == grid[row][0]) {
                    cntSame++;
                }
            }
            int ones = Math.max(cntSame, m - cntSame);
            score += ones << (n - 1 - col);
        }
        return score;
    }
}
```

## Python

```python
class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # contribution of the first column (all 1 after row flips)
        score = m * (1 << (n - 1))
        for col in range(1, n):
            same_as_first = 0
            for r in range(m):
                if grid[r][col] == grid[r][0]:
                    same_as_first += 1
            ones = max(same_as_first, m - same_as_first)
            score += ones * (1 << (n - 1 - col))
        return score
```

## Python3

```python
from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # contribution of the first column (all 1s after optimal row flips)
        score = m * (1 << (n - 1))
        for col in range(1, n):
            same_as_first = 0
            for row in range(m):
                if grid[row][col] == grid[row][0]:
                    same_as_first += 1
            ones = max(same_as_first, m - same_as_first)
            score += ones * (1 << (n - col - 1))
        return score
```

## C

```c
int matrixScore(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int score = 0;

    // Contribution of the first column (all ones after optimal row flips)
    score += m * (1 << (n - 1));

    for (int col = 1; col < n; ++col) {
        int ones = 0;
        for (int row = 0; row < m; ++row) {
            if (grid[row][0] == grid[row][col]) {
                ++ones;
            }
        }
        int maxOnes = ones > (m - ones) ? ones : (m - ones);
        score += maxOnes * (1 << (n - 1 - col));
    }

    return score;
}
```

## Csharp

```csharp
public class Solution
{
    public int MatrixScore(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;

        // Contribution of the first column (all 1s after optimal row flips)
        int score = m * (1 << (n - 1));

        for (int col = 1; col < n; ++col)
        {
            int ones = 0;
            for (int row = 0; row < m; ++row)
            {
                // After ensuring the first column is all 1s, a cell equals 1
                // if it matches the original first cell of its row.
                if (grid[row][col] == grid[row][0])
                    ones++;
            }
            int maxOnes = Math.Max(ones, m - ones);
            score += maxOnes * (1 << (n - col - 1));
        }

        return score;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var matrixScore = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let score = 0;
    for (let col = 0; col < n; ++col) {
        let ones = 0;
        for (let row = 0; row < m; ++row) {
            // If the first cell of this row is 0, we consider that row flipped.
            let val = grid[row][col];
            if (grid[row][0] === 0) {
                val ^= 1; // toggle due to row flip
            }
            if (val === 1) ++ones;
        }
        const maxOnes = Math.max(ones, m - ones);
        score += maxOnes * (1 << (n - col - 1));
    }
    return score;
};
```

## Typescript

```typescript
function matrixScore(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let score = 0;

    // Contribution of the first column (all ones after row flips)
    score += m * (1 << (n - 1));

    for (let col = 1; col < n; col++) {
        let sameCount = 0;
        for (let row = 0; row < m; row++) {
            if (grid[row][col] === grid[row][0]) {
                sameCount++;
            }
        }
        const maxOnes = Math.max(sameCount, m - sameCount);
        score += maxOnes * (1 << (n - col - 1));
    }

    return score;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function matrixScore($grid) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        // contribution of the first column after ensuring all are 1
        $score = $m * (1 << ($n - 1));
        for ($col = 1; $col < $n; $col++) {
            $same = 0;
            for ($row = 0; $row < $m; $row++) {
                if ($grid[$row][0] == $grid[$row][$col]) {
                    $same++;
                }
            }
            $ones = max($same, $m - $same);
            $score += $ones * (1 << ($n - 1 - $col));
        }
        return $score;
    }
}
```

## Swift

```swift
class Solution {
    func matrixScore(_ grid: [[Int]]) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var total = 0
        for col in 0..<n {
            var ones = 0
            for row in 0..<m {
                let flip = grid[row][0] == 0 ? 1 : 0
                let val = grid[row][col] ^ flip
                if val == 1 { ones += 1 }
            }
            let maxOnes = max(ones, m - ones)
            total += maxOnes * (1 << (n - col - 1))
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun matrixScore(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var score = 0
        for (c in 0 until n) {
            var ones = 0
            for (r in 0 until m) {
                val bit = if (grid[r][0] == 1) grid[r][c] else 1 - grid[r][c]
                if (bit == 1) ones++
            }
            val maxOnes = if (ones > m - ones) ones else m - ones
            score += maxOnes shl (n - c - 1)
        }
        return score
    }
}
```

## Dart

```dart
class Solution {
  int matrixScore(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    int score = m * (1 << (n - 1)); // contribution of first column after row flips

    for (int col = 1; col < n; col++) {
      int same = 0;
      for (int row = 0; row < m; row++) {
        if (grid[row][col] == grid[row][0]) {
          same++;
        }
      }
      int maxOnes = same > (m - same) ? same : (m - same);
      score += maxOnes * (1 << (n - col - 1));
    }

    return score;
  }
}
```

## Golang

```go
func matrixScore(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	score := 0
	for col := 0; col < n; col++ {
		ones := 0
		for row := 0; row < m; row++ {
			val := grid[row][col]
			if grid[row][0] == 0 { // row would be flipped to make first bit 1
				val ^= 1
			}
			if val == 1 {
				ones++
			}
		}
		maxOnes := ones
		if m-ones > maxOnes {
			maxOnes = m - ones
		}
		score += maxOnes << (n - 1 - col)
	}
	return score
}
```

## Ruby

```ruby
def matrix_score(grid)
  m = grid.length
  n = grid[0].length
  score = m * (1 << (n - 1))
  (1...n).each do |j|
    ones = 0
    grid.each do |row|
      if row[0] == 1
        ones += row[j]
      else
        ones += 1 - row[j]
      end
    end
    max_ones = [ones, m - ones].max
    score += max_ones * (1 << (n - 1 - j))
  end
  score
end
```

## Scala

```scala
object Solution {
    def matrixScore(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        var score = 0
        for (j <- 0 until n) {
            var ones = 0
            var i = 0
            while (i < m) {
                val bit = if (grid(i)(0) == 1) grid(i)(j) else 1 - grid(i)(j)
                if (bit == 1) ones += 1
                i += 1
            }
            val maxOnes = if (ones > m - ones) ones else m - ones
            score += maxOnes * (1 << (n - j - 1))
        }
        score
    }
}
```

## Rust

```rust
impl Solution {
    pub fn matrix_score(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();

        // contribution of the first column after ensuring all are 1
        let mut score: i32 = ((1 << (n - 1)) as i32) * m as i32;

        for col in 1..n {
            let mut same = 0;
            for row in 0..m {
                if grid[row][col] == grid[row][0] {
                    same += 1;
                }
            }
            let max_ones = std::cmp::max(same, m - same);
            score += (max_ones as i32) * ((1 << (n - 1 - col)) as i32);
        }

        score
    }
}
```

## Racket

```racket
(define/contract (matrix-score grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (car grid))))
         (first-col (map car grid)))
    (define score (* m (arithmetic-shift 1 (- n 1)))) ; contribution of first column
    (for ([j (in-range 1 n)])
      (define weight (arithmetic-shift 1 (- n 1 j))) ; value of this bit position
      (define count-same
        (let loop ((rows grid) (firsts first-col) (cnt 0))
          (if (null? rows)
              cnt
              (let* ((row (car rows))
                     (first (car firsts))
                     (val (list-ref row j)))
                (loop (cdr rows) (cdr firsts) (+ cnt (if (= val first) 1 0)))))))
      (define max-ones (max count-same (- m count-same)))
      (set! score (+ score (* weight max-ones))))
    score))
```

## Erlang

```erlang
-module(solution).
-export([matrix_score/1]).

-spec matrix_score(Grid :: [[integer()]]) -> integer().
matrix_score(Grid) ->
    M = length(Grid),
    [FirstRow|_] = Grid,
    N = length(FirstRow),
    FirstColScore = M * (1 bsl (N - 1)),
    ScoreRest = lists:foldl(
        fun(ColIdx, Acc) ->
            Ones = same_count(Grid, ColIdx),
            MaxOnes = erlang:max(Ones, M - Ones),
            Acc + MaxOnes * (1 bsl (N - 1 - ColIdx))
        end,
        0,
        lists:seq(1, N - 1)
    ),
    FirstColScore + ScoreRest.

same_count([], _) -> 0;
same_count([Row|Rest], ColIdx) ->
    First = hd(Row),
    Elem = lists:nth(ColIdx + 1, Row), % nth is 1‑based
    Same = if Elem == First -> 1; true -> 0 end,
    Same + same_count(Rest, ColIdx).
```

## Elixir

```elixir
defmodule Solution do
  @spec matrix_score(grid :: [[integer]]) :: integer
  def matrix_score(grid) do
    m = length(grid)
    n = length(hd(grid))

    base = m * (1 <<< (n - 1))

    extra =
      if n > 1 do
        Enum.reduce(1..(n - 1), 0, fn col_idx, acc ->
          count_same =
            Enum.count(grid, fn row -> Enum.at(row, col_idx) == hd(row) end)

          max_ones = max(count_same, m - count_same)
          acc + max_ones * (1 <<< (n - 1 - col_idx))
        end)
      else
        0
      end

    base + extra
  end
end
```

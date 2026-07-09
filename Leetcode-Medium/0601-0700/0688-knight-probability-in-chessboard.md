# 0688. Knight Probability in Chessboard

## Cpp

```cpp
class Solution {
public:
    double knightProbability(int n, int k, int row, int column) {
        static const int dirs[8][2] = {{1,2},{1,-2},{-1,2},{-1,-2},{2,1},{2,-1},{-2,1},{-2,-1}};
        vector<vector<double>> dp(n, vector<double>(n, 0.0));
        dp[row][column] = 1.0;
        for (int step = 0; step < k; ++step) {
            vector<vector<double>> ndp(n, vector<double>(n, 0.0));
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (dp[i][j] == 0.0) continue;
                    double prob = dp[i][j] / 8.0;
                    for (auto &d : dirs) {
                        int ni = i + d[0];
                        int nj = j + d[1];
                        if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                            ndp[ni][nj] += prob;
                        }
                    }
                }
            }
            dp.swap(ndp);
        }
        double ans = 0.0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                ans += dp[i][j];
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final int[][] DIRS = {
        {1, 2}, {1, -2}, {-1, 2}, {-1, -2},
        {2, 1}, {2, -1}, {-2, 1}, {-2, -1}
    };
    
    public double knightProbability(int n, int k, int row, int column) {
        double[][] prev = new double[n][n];
        prev[row][column] = 1.0;
        
        for (int step = 0; step < k; step++) {
            double[][] curr = new double[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    double prob = prev[i][j];
                    if (prob == 0.0) continue;
                    double share = prob / 8.0;
                    for (int[] d : DIRS) {
                        int ni = i + d[0];
                        int nj = j + d[1];
                        if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                            curr[ni][nj] += share;
                        }
                    }
                }
            }
            prev = curr;
        }
        
        double total = 0.0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                total += prev[i][j];
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        if k == 0:
            return 1.0

        dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]

        prev = [[0.0] * n for _ in range(n)]
        prev[row][column] = 1.0

        for _ in range(k):
            cur = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if prev[i][j] == 0:
                        continue
                    prob = prev[i][j] / 8.0
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            cur[ni][nj] += prob
            prev = cur

        return sum(map(sum, prev))
```

## Python3

```python
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1.0
        dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]
        prev = [[0.0] * n for _ in range(n)]
        prev[row][column] = 1.0
        for _ in range(k):
            cur = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if prev[i][j] == 0.0:
                        continue
                    prob = prev[i][j] / 8.0
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:
                            cur[ni][nj] += prob
            prev = cur
        return sum(map(sum, prev))
```

## C

```c
double knightProbability(int n, int k, int row, int column) {
    if (k == 0) return 1.0;
    const int dirs[8][2] = {{2,1},{2,-1},{-2,1},{-2,-1},{1,2},{1,-2},{-1,2},{-1,-2}};
    double *prev = (double*)calloc(n * n, sizeof(double));
    double *curr = (double*)calloc(n * n, sizeof(double));
    prev[row * n + column] = 1.0;
    
    for (int step = 0; step < k; ++step) {
        memset(curr, 0, n * n * sizeof(double));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                double p = prev[i * n + j];
                if (p == 0.0) continue;
                double add = p / 8.0;
                for (int d = 0; d < 8; ++d) {
                    int ni = i + dirs[d][0];
                    int nj = j + dirs[d][1];
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        curr[ni * n + nj] += add;
                    }
                }
            }
        }
        double *tmp = prev;
        prev = curr;
        curr = tmp;
    }
    
    double result = 0.0;
    for (int i = 0; i < n * n; ++i) {
        result += prev[i];
    }
    free(prev);
    free(curr);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public double KnightProbability(int n, int k, int row, int column)
    {
        // Directions a knight can move
        int[] dr = { 2, 2, -2, -2, 1, 1, -1, -1 };
        int[] dc = { 1, -1, 1, -1, 2, -2, 2, -2 };

        double[,] prev = new double[n, n];
        prev[row, column] = 1.0;

        for (int step = 0; step < k; ++step)
        {
            double[,] curr = new double[n, n];

            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < n; ++j)
                {
                    double prob = prev[i, j];
                    if (prob == 0.0) continue;

                    double share = prob / 8.0;
                    for (int d = 0; d < 8; ++d)
                    {
                        int ni = i + dr[d];
                        int nj = j + dc[d];
                        if (ni >= 0 && ni < n && nj >= 0 && nj < n)
                        {
                            curr[ni, nj] += share;
                        }
                    }
                }
            }

            prev = curr;
        }

        double result = 0.0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                result += prev[i, j];

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} row
 * @param {number} column
 * @return {number}
 */
var knightProbability = function(n, k, row, column) {
    const dirs = [
        [2, 1], [1, 2], [-1, 2], [-2, 1],
        [-2, -1], [-1, -2], [1, -2], [2, -1]
    ];
    
    // dp for previous step
    let prev = Array.from({ length: n }, () => Array(n).fill(0));
    prev[row][column] = 1;
    
    for (let step = 0; step < k; step++) {
        const curr = Array.from({ length: n }, () => Array(n).fill(0));
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                const prob = prev[i][j];
                if (prob === 0) continue;
                const share = prob / 8;
                for (const [dx, dy] of dirs) {
                    const ni = i + dx;
                    const nj = j + dy;
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        curr[ni][nj] += share;
                    }
                }
            }
        }
        prev = curr;
    }
    
    let total = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            total += prev[i][j];
        }
    }
    return total;
};
```

## Typescript

```typescript
function knightProbability(n: number, k: number, row: number, column: number): number {
    const dirs = [
        [2, 1],
        [1, 2],
        [-1, 2],
        [-2, 1],
        [-2, -1],
        [-1, -2],
        [1, -2],
        [2, -1],
    ];
    let prev: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    prev[row][column] = 1;

    for (let step = 0; step < k; step++) {
        const curr: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                const prob = prev[i][j];
                if (prob === 0) continue;
                const add = prob / 8;
                for (const [dx, dy] of dirs) {
                    const ni = i + dx;
                    const nj = j + dy;
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        curr[ni][nj] += add;
                    }
                }
            }
        }
        prev = curr;
    }

    let total = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            total += prev[i][j];
        }
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $row
     * @param Integer $column
     * @return Float
     */
    function knightProbability($n, $k, $row, $column) {
        $dirs = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]];
        $prev = array_fill(0, $n, array_fill(0, $n, 0.0));
        $prev[$row][$column] = 1.0;

        for ($step = 1; $step <= $k; $step++) {
            $curr = array_fill(0, $n, array_fill(0, $n, 0.0));
            for ($i = 0; $i < $n; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    $prob = 0.0;
                    foreach ($dirs as $d) {
                        $ni = $i - $d[0];
                        $nj = $j - $d[1];
                        if ($ni >= 0 && $ni < $n && $nj >= 0 && $nj < $n) {
                            $prob += $prev[$ni][$nj] / 8.0;
                        }
                    }
                    $curr[$i][$j] = $prob;
                }
            }
            $prev = $curr;
        }

        $total = 0.0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $total += $prev[$i][$j];
            }
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func knightProbability(_ n: Int, _ k: Int, _ row: Int, _ column: Int) -> Double {
        let dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                    (1, 2), (1, -2), (-1, 2), (-1, -2)]
        var prev = Array(repeating: Array(repeating: 0.0, count: n), count: n)
        prev[row][column] = 1.0
        if k == 0 { return 1.0 }
        for _ in 1...k {
            var curr = Array(repeating: Array(repeating: 0.0, count: n), count: n)
            for i in 0..<n {
                for j in 0..<n {
                    let prob = prev[i][j]
                    if prob == 0 { continue }
                    for d in dirs {
                        let ni = i + d.0
                        let nj = j + d.1
                        if ni >= 0 && ni < n && nj >= 0 && nj < n {
                            curr[ni][nj] += prob / 8.0
                        }
                    }
                }
            }
            prev = curr
        }
        var total = 0.0
        for i in 0..<n {
            for j in 0..<n {
                total += prev[i][j]
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun knightProbability(n: Int, k: Int, row: Int, column: Int): Double {
        val dirs = arrayOf(
            intArrayOf(2, 1), intArrayOf(2, -1),
            intArrayOf(-2, 1), intArrayOf(-2, -1),
            intArrayOf(1, 2), intArrayOf(1, -2),
            intArrayOf(-1, 2), intArrayOf(-1, -2)
        )
        var prev = Array(n) { DoubleArray(n) }
        prev[row][column] = 1.0

        repeat(k) {
            val curr = Array(n) { DoubleArray(n) }
            for (i in 0 until n) {
                for (j in 0 until n) {
                    var prob = 0.0
                    for (d in dirs) {
                        val ni = i + d[0]
                        val nj = j + d[1]
                        if (ni in 0 until n && nj in 0 until n) {
                            prob += prev[ni][nj] / 8.0
                        }
                    }
                    curr[i][j] = prob
                }
            }
            prev = curr
        }

        var total = 0.0
        for (i in 0 until n) {
            for (j in 0 until n) {
                total += prev[i][j]
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  double knightProbability(int n, int k, int row, int column) {
    const List<List<int>> dirs = [
      [2, 1],
      [1, 2],
      [-1, 2],
      [-2, 1],
      [-2, -1],
      [-1, -2],
      [1, -2],
      [2, -1]
    ];

    List<List<double>> prev = List.generate(
        n, (_) => List.filled(n, 0.0));
    prev[row][column] = 1.0;

    for (int step = 0; step < k; ++step) {
      List<List<double>> curr = List.generate(
          n, (_) => List.filled(n, 0.0));
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          double sum = 0.0;
          for (var d in dirs) {
            int pi = i - d[0];
            int pj = j - d[1];
            if (pi >= 0 && pi < n && pj >= 0 && pj < n) {
              sum += prev[pi][pj];
            }
          }
          curr[i][j] = sum / 8.0;
        }
      }
      prev = curr;
    }

    double result = 0.0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        result += prev[i][j];
      }
    }
    return result;
  }
}
```

## Golang

```go
func knightProbability(n int, k int, row int, column int) float64 {
    dirs := [8][2]int{{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}}
    prev := make([][]float64, n)
    for i := 0; i < n; i++ {
        prev[i] = make([]float64, n)
    }
    prev[row][column] = 1.0

    curr := make([][]float64, n)
    for i := 0; i < n; i++ {
        curr[i] = make([]float64, n)
    }

    for step := 0; step < k; step++ {
        // reset current layer
        for i := 0; i < n; i++ {
            for j := 0; j < n; j++ {
                curr[i][j] = 0.0
            }
        }
        for i := 0; i < n; i++ {
            for j := 0; j < n; j++ {
                if prev[i][j] == 0 {
                    continue
                }
                prob := prev[i][j] / 8.0
                for _, d := range dirs {
                    ni, nj := i+d[0], j+d[1]
                    if ni >= 0 && ni < n && nj >= 0 && nj < n {
                        curr[ni][nj] += prob
                    }
                }
            }
        }
        prev, curr = curr, prev
    }

    total := 0.0
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            total += prev[i][j]
        }
    }
    return total
}
```

## Ruby

```ruby
def knight_probability(n, k, row, column)
  dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
  prev = Array.new(n) { Array.new(n, 0.0) }
  prev[row][column] = 1.0

  k.times do
    curr = Array.new(n) { Array.new(n, 0.0) }
    n.times do |i|
      n.times do |j|
        prob = prev[i][j]
        next if prob == 0.0
        dirs.each do |dx, dy|
          ni = i + dx
          nj = j + dy
          if ni >= 0 && ni < n && nj >= 0 && nj < n
            curr[ni][nj] += prob / 8.0
          end
        end
      end
    end
    prev = curr
  end

  total = 0.0
  n.times do |i|
    n.times do |j|
      total += prev[i][j]
    end
  end
  total
end
```

## Scala

```scala
object Solution {
    def knightProbability(n: Int, k: Int, row: Int, column: Int): Double = {
        val dirs = Array((2, 1), (2, -1), (-2, 1), (-2, -1),
                         (1, 2), (1, -2), (-1, 2), (-1, -2))
        var prev = Array.ofDim[Double](n, n)
        var curr = Array.ofDim[Double](n, n)
        prev(row)(column) = 1.0

        for (_ <- 1 to k) {
            for (i <- 0 until n) java.util.Arrays.fill(curr(i), 0.0)

            for (i <- 0 until n; j <- 0 until n) {
                var sum = 0.0
                for ((dx, dy) <- dirs) {
                    val ni = i + dx
                    val nj = j + dy
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        sum += prev(ni)(nj)
                    }
                }
                curr(i)(j) = sum / 8.0
            }

            val tmp = prev
            prev = curr
            curr = tmp
        }

        var total = 0.0
        for (i <- 0 until n; j <- 0 until n) {
            total += prev(i)(j)
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn knight_probability(n: i32, k: i32, row: i32, column: i32) -> f64 {
        let n_usize = n as usize;
        let mut prev = vec![vec![0f64; n_usize]; n_usize];
        prev[row as usize][column as usize] = 1.0;

        let dirs = [
            (2i32, 1i32),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
        ];

        for _ in 0..k {
            let mut curr = vec![vec![0f64; n_usize]; n_usize];
            for i in 0..n_usize {
                for j in 0..n_usize {
                    let prob = prev[i][j];
                    if prob == 0.0 {
                        continue;
                    }
                    for &(dx, dy) in &dirs {
                        let ni = i as i32 + dx;
                        let nj = j as i32 + dy;
                        if ni >= 0 && ni < n && nj >= 0 && nj < n {
                            curr[ni as usize][nj as usize] += prob / 8.0;
                        }
                    }
                }
            }
            prev = curr;
        }

        let mut total = 0f64;
        for i in 0..n_usize {
            for j in 0..n_usize {
                total += prev[i][j];
            }
        }
        total
    }
}
```

## Racket

```racket
(define/contract (knight-probability n k row column)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? flonum?)
  (let* ([prev (make-vector n)]
         [curr (make-vector n)])
    ;; initialize matrices with zeros
    (for ([i (in-range n)])
      (vector-set! prev i (make-vector n 0.0))
      (vector-set! curr i (make-vector n 0.0)))
    ;; starting position
    (vector-set! (vector-ref prev row) column 1.0)
    (define dirs '((2 . 1) (1 . 2) (-1 . 2) (-2 . 1)
                   (-2 . -1) (-1 . -2) (1 . -2) (2 . -1)))
    ;; DP over moves
    (for ([move (in-range k)])
      (for ([i (in-range n)])
        (let ([curr-row (vector-ref curr i)])
          (for ([j (in-range n)])
            (let ([sum 0.0])
              (for ([d dirs])
                (define dx (car d))
                (define dy (cdr d))
                (define pi (+ i dx))
                (define pj (+ j dy))
                (when (and (>= pi 0) (< pi n) (>= pj 0) (< pj n))
                  (set! sum (+ sum (/ (vector-ref (vector-ref prev pi) pj) 8.0)))))
              (vector-set! curr-row j sum)))))
      ;; swap matrices
      (let ([tmp prev])
        (set! prev curr)
        (set! curr tmp))
      ;; reset new curr to zeros
      (for ([i (in-range n)])
        (let ([rowvec (vector-ref curr i)])
          (for ([j (in-range n)])
            (vector-set! rowvec j 0.0)))))
    ;; sum probabilities after k moves
    (let ([total 0.0])
      (for ([i (in-range n)])
        (let ([rowvec (vector-ref prev i)])
          (for ([j (in-range n)])
            (set! total (+ total (vector-ref rowvec j))))))
      total)))
```

## Erlang

```erlang
-module(solution).
-export([knight_probability/4]).

-spec knight_probability(N :: integer(), K :: integer(), Row :: integer(), Column :: integer()) -> float().
knight_probability(N, K, Row, Column) ->
    Prev0 = init_matrix(N, Row, Column),
    Final = loop(K, Prev0, N),
    total_prob(Final).

init_matrix(N, Row, Column) ->
    [ [ if I == Row andalso J == Column -> 1.0; true -> 0.0 end
        || J <- lists:seq(0, N-1) ]
      || I <- lists:seq(0, N-1) ].

loop(0, Matrix, _N) ->
    Matrix;
loop(MovesLeft, Prev, N) ->
    Curr = [ [ prob(I, J, Prev, N) || J <- lists:seq(0, N-1) ]
            || I <- lists:seq(0, N-1) ],
    loop(MovesLeft - 1, Curr, N).

prob(I, J, Prev, N) ->
    Sum = lists:foldl(
        fun({DR, DC}, Acc) ->
                PrevR = I - DR,
                PrevC = J - DC,
                Acc + get_cell(Prev, PrevR, PrevC, N)
        end,
        0.0,
        directions()
    ),
    Sum / 8.0.

directions() -> [{2,1},{2,-1},{-2,1},{-2,-1},{1,2},{1,-2},{-1,2},{-1,-2}].

get_cell(_Matrix, R, _C, N) when R < 0; R >= N ->
    0.0;
get_cell(Matrix, R, C, N) when C < 0; C >= N ->
    0.0;
get_cell(Matrix, R, C, _N) ->
    Row = lists:nth(R + 1, Matrix),
    lists:nth(C + 1, Row).

total_prob(Matrix) ->
    lists:foldl(fun(RowAcc, Row) -> RowAcc + lists:sum(Row) end, 0.0, Matrix).
```

## Elixir

```elixir
defmodule Solution do
  @spec knight_probability(n :: integer, k :: integer, row :: integer, column :: integer) :: float
  def knight_probability(n, k, row, column) do
    directions = [
      {1, 2}, {1, -2}, {-1, 2}, {-1, -2},
      {2, 1}, {2, -1}, {-2, 1}, {-2, -1}
    ]

    # initial probability matrix
    prev =
      for i <- 0..(n - 1) do
        for j <- 0..(n - 1) do
          if i == row and j == column, do: 1.0, else: 0.0
        end
      end

    final_matrix =
      Enum.reduce(1..k, prev, fn _step, acc ->
        for i <- 0..(n - 1) do
          for j <- 0..(n - 1) do
            prob =
              Enum.reduce(directions, 0.0, fn {dx, dy}, sum ->
                pi = i - dx
                pj = j - dy

                if pi >= 0 and pi < n and pj >= 0 and pj < n do
                  sum + (Enum.at(Enum.at(acc, pi), pj) / 8.0)
                else
                  sum
                end
              end)

            prob
          end
        end
      end)

    final_matrix
    |> Enum.flat_map(& &1)
    |> Enum.sum()
  end
end
```

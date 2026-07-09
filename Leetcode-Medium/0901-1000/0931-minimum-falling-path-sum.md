# 0931. Minimum Falling Path Sum

## Cpp

```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> dp = matrix[0];
        for (int i = 1; i < n; ++i) {
            vector<int> cur(n);
            for (int j = 0; j < n; ++j) {
                int best = dp[j];
                if (j > 0) best = min(best, dp[j - 1]);
                if (j + 1 < n) best = min(best, dp[j + 1]);
                cur[j] = matrix[i][j] + best;
            }
            dp.swap(cur);
        }
        return *min_element(dp.begin(), dp.end());
    }
};
```

## Java

```java
class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[] dp = new int[n];
        // initialize with first row
        for (int j = 0; j < n; j++) {
            dp[j] = matrix[0][j];
        }
        // iterate rows starting from second
        for (int i = 1; i < n; i++) {
            int[] newDp = new int[n];
            for (int j = 0; j < n; j++) {
                int best = dp[j]; // directly above
                if (j > 0) {
                    best = Math.min(best, dp[j - 1]); // left diagonal
                }
                if (j + 1 < n) {
                    best = Math.min(best, dp[j + 1]); // right diagonal
                }
                newDp[j] = matrix[i][j] + best;
            }
            dp = newDp;
        }
        int ans = dp[0];
        for (int j = 1; j < n; j++) {
            if (dp[j] < ans) ans = dp[j];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp = matrix[0][:]
        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                best = dp[j]
                if j > 0:
                    best = min(best, dp[j - 1])
                if j < n - 1:
                    best = min(best, dp[j + 1])
                new_dp[j] = matrix[i][j] + best
            dp = new_dp
        return min(dp)
```

## Python3

```python
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        for i in range(1, n):
            ndp = [0] * n
            for j in range(n):
                best = dp[j]
                if j > 0:
                    best = min(best, dp[j - 1])
                if j < n - 1:
                    best = min(best, dp[j + 1])
                ndp[j] = matrix[i][j] + best
            dp = ndp
        return min(dp)
```

## C

```c
int minFallingPathSum(int** matrix, int matrixSize, int* matrixColSize){
    int n = matrixSize;
    if (n == 0) return 0;
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int best = matrix[i-1][j];
            if (j > 0 && matrix[i-1][j-1] < best) best = matrix[i-1][j-1];
            if (j + 1 < n && matrix[i-1][j+1] < best) best = matrix[i-1][j+1];
            matrix[i][j] += best;
        }
    }
    int ans = matrix[n-1][0];
    for (int j = 1; j < n; ++j) {
        if (matrix[n-1][j] < ans) ans = matrix[n-1][j];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinFallingPathSum(int[][] matrix) {
        int n = matrix.Length;
        int[] dp = new int[n];
        for (int j = 0; j < n; j++) dp[j] = matrix[0][j];

        for (int i = 1; i < n; i++) {
            int[] ndp = new int[n];
            for (int j = 0; j < n; j++) {
                int best = dp[j];
                if (j > 0) best = Math.Min(best, dp[j - 1]);
                if (j + 1 < n) best = Math.Min(best, dp[j + 1]);
                ndp[j] = matrix[i][j] + best;
            }
            dp = ndp;
        }

        int ans = dp[0];
        for (int j = 1; j < n; j++) {
            if (dp[j] < ans) ans = dp[j];
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function(matrix) {
    const n = matrix.length;
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < n; j++) {
            let best = matrix[i - 1][j];
            if (j > 0) best = Math.min(best, matrix[i - 1][j - 1]);
            if (j + 1 < n) best = Math.min(best, matrix[i - 1][j + 1]);
            matrix[i][j] += best;
        }
    }
    return Math.min(...matrix[n - 1]);
};
```

## Typescript

```typescript
function minFallingPathSum(matrix: number[][]): number {
    const n = matrix.length;
    if (n === 0) return 0;
    let dp = matrix[0].slice(); // copy first row

    for (let i = 1; i < n; i++) {
        const newDp = new Array(n);
        for (let j = 0; j < n; j++) {
            let best = dp[j];
            if (j > 0) best = Math.min(best, dp[j - 1]);
            if (j + 1 < n) best = Math.min(best, dp[j + 1]);
            newDp[j] = matrix[i][j] + best;
        }
        dp = newDp;
    }

    return Math.min(...dp);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function minFallingPathSum($matrix) {
        $n = count($matrix);
        for ($i = 1; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $minPrev = $matrix[$i - 1][$j];
                if ($j > 0) {
                    $minPrev = min($minPrev, $matrix[$i - 1][$j - 1]);
                }
                if ($j < $n - 1) {
                    $minPrev = min($minPrev, $matrix[$i - 1][$j + 1]);
                }
                $matrix[$i][$j] += $minPrev;
            }
        }
        return min($matrix[$n - 1]);
    }
}
```

## Swift

```swift
class Solution {
    func minFallingPathSum(_ matrix: [[Int]]) -> Int {
        let n = matrix.count
        var dp = matrix[0]
        if n == 1 { return dp.min()! }
        for i in 1..<n {
            var cur = Array(repeating: 0, count: n)
            for j in 0..<n {
                var best = dp[j]
                if j > 0 { best = min(best, dp[j - 1]) }
                if j + 1 < n { best = min(best, dp[j + 1]) }
                cur[j] = matrix[i][j] + best
            }
            dp = cur
        }
        return dp.min()!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minFallingPathSum(matrix: Array<IntArray>): Int {
        val n = matrix.size
        var dp = matrix[0].clone()
        for (i in 1 until n) {
            val newDp = IntArray(n)
            for (j in 0 until n) {
                var best = dp[j]
                if (j > 0) best = kotlin.math.min(best, dp[j - 1])
                if (j < n - 1) best = kotlin.math.min(best, dp[j + 1])
                newDp[j] = matrix[i][j] + best
            }
            dp = newDp
        }
        var ans = dp[0]
        for (v in dp) {
            if (v < ans) ans = v
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minFallingPathSum(List<List<int>> matrix) {
    int n = matrix.length;
    List<int> dp = List<int>.from(matrix[0]);
    for (int i = 1; i < n; ++i) {
      List<int> newRow = List<int>.filled(n, 0);
      for (int j = 0; j < n; ++j) {
        int best = dp[j];
        if (j > 0 && dp[j - 1] < best) best = dp[j - 1];
        if (j + 1 < n && dp[j + 1] < best) best = dp[j + 1];
        newRow[j] = matrix[i][j] + best;
      }
      dp = newRow;
    }
    int ans = dp[0];
    for (int v in dp) {
      if (v < ans) ans = v;
    }
    return ans;
  }
}
```

## Golang

```go
func minFallingPathSum(matrix [][]int) int {
	n := len(matrix)
	if n == 0 {
		return 0
	}
	dp := make([]int, n)
	copy(dp, matrix[0])

	for i := 1; i < n; i++ {
		newDP := make([]int, n)
		for j := 0; j < n; j++ {
			best := dp[j]
			if j > 0 && dp[j-1] < best {
				best = dp[j-1]
			}
			if j+1 < n && dp[j+1] < best {
				best = dp[j+1]
			}
			newDP[j] = matrix[i][j] + best
		}
		dp = newDP
	}

	ans := dp[0]
	for _, v := range dp {
		if v < ans {
			ans = v
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_falling_path_sum(matrix)
  n = matrix.size
  (1...n).each do |i|
    (0...n).each do |j|
      best = matrix[i - 1][j]
      best = [best, matrix[i - 1][j - 1]].min if j > 0
      best = [best, matrix[i - 1][j + 1]].min if j + 1 < n
      matrix[i][j] += best
    end
  end
  matrix[-1].min
end
```

## Scala

```scala
object Solution {
    def minFallingPathSum(matrix: Array[Array[Int]]): Int = {
        val n = matrix.length
        var dp = matrix(0).clone()
        for (i <- 1 until n) {
            val newDp = new Array[Int](n)
            for (j <- 0 until n) {
                var best = dp(j)
                if (j > 0 && dp(j - 1) < best) best = dp(j - 1)
                if (j + 1 < n && dp(j + 1) < best) best = dp(j + 1)
                newDp(j) = matrix(i)(j) + best
            }
            dp = newDp
        }
        dp.min
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let n = matrix.len();
        if n == 0 {
            return 0;
        }
        let mut dp = matrix;
        for i in 1..n {
            for j in 0..n {
                let mut best = dp[i - 1][j];
                if j > 0 {
                    best = best.min(dp[i - 1][j - 1]);
                }
                if j + 1 < n {
                    best = best.min(dp[i - 1][j + 1]);
                }
                dp[i][j] += best;
            }
        }
        *dp[n - 1].iter().min().unwrap()
    }
}
```

## Racket

```racket
#lang racket

(define/contract (min-falling-path-sum matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length matrix))
         (rows (map list->vector matrix)))
    (if (= n 0)
        0
        (let loop ((i (- n 2))
                   (dp (vector-copy (list-ref rows (- n 1)))))
          (if (< i 0)
              (apply min (vector->list dp))
              (let* ((cur (list-ref rows i))
                     (new-dp (make-vector n)))
                (for ([j (in-range n)])
                  (define curval (vector-ref cur j))
                  (define minprev (vector-ref dp j))
                  (when (> j 0)
                    (set! minprev (min minprev (vector-ref dp (- j 1)))))
                  (when (< j (- n 1))
                    (set! minprev (min minprev (vector-ref dp (+ j 1)))))
                  (vector-set! new-dp j (+ curval minprev)))
                (loop (- i 1) new-dp)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_falling_path_sum/1]).

-spec min_falling_path_sum(Matrix :: [[integer()]]) -> integer().
min_falling_path_sum([]) ->
    0;
min_falling_path_sum([FirstRow|RestRows]) ->
    dp_loop(RestRows, FirstRow).

dp_loop([], PrevDP) ->
    lists:min(PrevDP);
dp_loop([Row|Rows], PrevDP) ->
    PrevTuple = list_to_tuple(PrevDP),
    CurrDP = compute_row(Row, PrevTuple),
    dp_loop(Rows, CurrDP).

compute_row(Row, PrevTuple) ->
    N = tuple_size(PrevTuple),
    compute_row(Row, PrevTuple, N, 0, []).

compute_row([], _PrevTuple, _N, _Idx, Acc) ->
    lists:reverse(Acc);
compute_row([Val|RestRow], PrevTuple, N, Idx, Acc) ->
    Mid = element(Idx+1, PrevTuple),
    Left = case Idx > 0 of
        true -> element(Idx, PrevTuple);
        false -> undefined
    end,
    Right = case Idx < N-1 of
        true -> element(Idx+2, PrevTuple);
        false -> undefined
    end,
    MinPrev = min_of_three(Left, Mid, Right),
    NewVal = Val + MinPrev,
    compute_row(RestRow, PrevTuple, N, Idx+1, [NewVal|Acc]).

min_of_three(undefined, B, C) when is_integer(B), is_integer(C) ->
    erlang:min(B, C);
min_of_three(A, undefined, C) when is_integer(A), is_integer(C) ->
    erlang:min(A, C);
min_of_three(A, B, undefined) when is_integer(A), is_integer(B) ->
    erlang:min(A, B);
min_of_three(A, B, C) ->
    lists:min([A,B,C]).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_falling_path_sum(matrix :: [[integer]]) :: integer
  def min_falling_path_sum(matrix) do
    [first_row | rest_rows] = matrix
    dp = first_row

    final_dp =
      Enum.reduce(rest_rows, dp, fn row, prev ->
        n = length(row)

        for j <- 0..(n - 1), into: [] do
          val = Enum.at(row, j)

          candidates =
            [j, j - 1, j + 1]
            |> Enum.filter(fn idx -> idx >= 0 and idx < n end)
            |> Enum.map(&Enum.at(prev, &1))

          val + Enum.min(candidates)
        end
      end)

    Enum.min(final_dp)
  end
end
```

# 3070. Count Submatrices with Top-Left Element and Sum Less Than k

## Cpp

```cpp
class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        vector<long long> colSum(n, 0);
        long long ans = 0;
        for (int i = 0; i < m; ++i) {
            long long rowPref = 0;
            for (int j = 0; j < n; ++j) {
                colSum[j] += grid[i][j];
                rowPref += colSum[j]; // sum of rectangle (0,0)-(i,j)
                if (rowPref <= k) ++ans;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int countSubmatrices(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        long[][] pref = new long[m][n];
        int ans = 0;
        for (int i = 0; i < m; i++) {
            long rowSum = 0;
            for (int j = 0; j < n; j++) {
                long cur = grid[i][j];
                if (i > 0) cur += pref[i - 1][j];
                if (j > 0) cur += pref[i][j - 1];
                if (i > 0 && j > 0) cur -= pref[i - 1][j - 1];
                pref[i][j] = cur;
                if (cur <= k) ans++;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        col_acc = [0] * n
        ans = 0
        for i in range(m):
            # update column accumulations up to current row
            for j in range(n):
                col_acc[j] += grid[i][j]
            cur = 0
            # compute prefix sum for each (i, j)
            for j in range(n):
                cur += col_acc[j]
                if cur <= k:
                    ans += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        col_sums = [0] * n
        ans = 0
        for i in range(m):
            row_prefix = 0
            for j in range(n):
                col_sums[j] += grid[i][j]
                row_prefix += col_sums[j]
                if row_prefix <= k:
                    ans += 1
        return ans
```

## C

```c
#include <stdlib.h>

int countSubmatrices(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize;
    if (m == 0) return 0;
    int n = gridColSize[0];
    // Allocate prefix sum matrix of size (m+1) x (n+1)
    long long **pref = (long long **)malloc((m + 1) * sizeof(long long *));
    pref[0] = (long long *)calloc(n + 1, sizeof(long long));
    for (int i = 1; i <= m; ++i) {
        pref[i] = (long long *)calloc(n + 1, sizeof(long long));
    }

    int count = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            pref[i + 1][j + 1] = grid[i][j]
                                + pref[i][j + 1]
                                + pref[i + 1][j]
                                - pref[i][j];
            if (pref[i + 1][j + 1] <= (long long)k) {
                ++count;
            }
        }
    }

    // Free allocated memory
    for (int i = 0; i <= m; ++i) {
        free(pref[i]);
    }
    free(pref);

    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountSubmatrices(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        long[,] pref = new long[m, n];
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                long sum = grid[i][j];
                if (i > 0) sum += pref[i - 1, j];
                if (j > 0) sum += pref[i, j - 1];
                if (i > 0 && j > 0) sum -= pref[i - 1, j - 1];
                pref[i, j] = sum;
                if (sum <= k) count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var countSubmatrices = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    let ans = 0;
    // create prefix sum matrix
    const pre = Array.from({ length: m }, () => new Array(n));
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            let sum = grid[i][j];
            if (i > 0) sum += pre[i - 1][j];
            if (j > 0) sum += pre[i][j - 1];
            if (i > 0 && j > 0) sum -= pre[i - 1][j - 1];
            pre[i][j] = sum;
            if (sum <= k) ++ans;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countSubmatrices(grid: number[][], k: number): number {
    const m = grid.length;
    const n = grid[0].length;
    let prev = new Array<number>(n).fill(0);
    let ans = 0;

    for (let i = 0; i < m; i++) {
        const cur = new Array<number>(n);
        for (let j = 0; j < n; j++) {
            const up = i > 0 ? prev[j] : 0;
            const left = j > 0 ? cur[j - 1] : 0;
            const diag = i > 0 && j > 0 ? prev[j - 1] : 0;
            const sum = grid[i][j] + up + left - diag;
            cur[j] = sum;
            if (sum <= k) ans++;
        }
        prev = cur;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer
     */
    function countSubmatrices($grid, $k) {
        $m = count($grid);
        if ($m == 0) return 0;
        $n = count($grid[0]);
        $prev = array_fill(0, $n, 0);
        $ans = 0;

        for ($i = 0; $i < $m; $i++) {
            $rowCum = 0;
            $curr = array_fill(0, $n, 0);
            for ($j = 0; $j < $n; $j++) {
                $rowCum += $grid[$i][$j];
                $sum = $rowCum + ($i > 0 ? $prev[$j] : 0);
                $curr[$j] = $sum;
                if ($sum <= $k) {
                    $ans++;
                }
            }
            $prev = $curr;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countSubmatrices(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        var pref = Array(repeating: Array(repeating: 0, count: n), count: m)
        var ans = 0
        for i in 0..<m {
            for j in 0..<n {
                let up = i > 0 ? pref[i - 1][j] : 0
                let left = j > 0 ? pref[i][j - 1] : 0
                let diag = (i > 0 && j > 0) ? pref[i - 1][j - 1] : 0
                pref[i][j] = grid[i][j] + up + left - diag
                if pref[i][j] <= k {
                    ans += 1
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubmatrices(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        var cnt = 0
        val prefix = Array(m) { LongArray(n) }
        for (i in 0 until m) {
            var rowSum = 0L
            for (j in 0 until n) {
                rowSum += grid[i][j]
                val above = if (i > 0) prefix[i - 1][j] else 0L
                prefix[i][j] = rowSum + above
                if (prefix[i][j] <= k.toLong()) cnt++
            }
        }
        return cnt
    }
}
```

## Dart

```dart
class Solution {
  int countSubmatrices(List<List<int>> grid, int k) {
    int m = grid.length;
    if (m == 0) return 0;
    int n = grid[0].length;
    List<List<int>> pref = List.generate(m, (_) => List.filled(n, 0));
    int ans = 0;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int sum = grid[i][j];
        if (i > 0) sum += pref[i - 1][j];
        if (j > 0) sum += pref[i][j - 1];
        if (i > 0 && j > 0) sum -= pref[i - 1][j - 1];
        pref[i][j] = sum;
        if (sum <= k) ans++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countSubmatrices(grid [][]int, k int) int {
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])
	colSums := make([]int64, n)
	var ans int
	limit := int64(k)

	for i := 0; i < m; i++ {
		var rowSum int64
		for j := 0; j < n; j++ {
			rowSum += int64(grid[i][j])
			colSums[j] += rowSum // prefix sum up to (i,j)
			if colSums[j] <= limit {
				ans++
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_submatrices(grid, k)
  m = grid.length
  return 0 if m == 0
  n = grid[0].length
  col_sum = Array.new(n, 0)
  ans = 0

  grid.each do |row|
    j = 0
    while j < n
      col_sum[j] += row[j]
      j += 1
    end

    total = 0
    j = 0
    while j < n
      total += col_sum[j]
      ans += 1 if total <= k
      j += 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countSubmatrices(grid: Array[Array[Int]], k: Int): Int = {
        val m = grid.length
        if (m == 0) return 0
        val n = grid(0).length
        val kk = k.toLong
        var cnt = 0L
        val prefix = Array.ofDim[Long](m, n)
        for (i <- 0 until m) {
            var rowSum = 0L
            for (j <- 0 until n) {
                rowSum += grid(i)(j).toLong
                val above = if (i > 0) prefix(i - 1)(j) else 0L
                val sum = rowSum + above
                prefix(i)(j) = sum
                if (sum <= kk) cnt += 1
            }
        }
        cnt.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_submatrices(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        if m == 0 {
            return 0;
        }
        let n = grid[0].len();
        let mut prefix = vec![vec![0i64; n]; m];
        let mut count: i32 = 0;
        let kk = k as i64;
        for i in 0..m {
            for j in 0..n {
                let val = grid[i][j] as i64;
                let mut sum = val;
                if i > 0 {
                    sum += prefix[i - 1][j];
                }
                if j > 0 {
                    sum += prefix[i][j - 1];
                }
                if i > 0 && j > 0 {
                    sum -= prefix[i - 1][j - 1];
                }
                prefix[i][j] = sum;
                if sum <= kk {
                    count += 1;
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (count-submatrices grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (car grid))))
         (grid-v (list->vector (map list->vector grid)))
         (pref (make-vector m)))
    ;; build prefix sum matrix
    (do ([i 0 (+ i 1)]) ((= i m))
      (let ((row (make-vector n 0)))
        (vector-set! pref i row)
        (do ([j 0 (+ j 1)]) ((= j n))
          (define val (vector-ref (vector-ref grid-v i) j))
          (define up (if (= i 0) 0 (vector-ref (vector-ref pref (- i 1)) j)))
          (define left (if (= j 0) 0 (vector-ref row (- j 1))))
          (define diag (if (and (> i 0) (> j 0))
                           (vector-ref (vector-ref pref (- i 1)) (- j 1))
                           0))
          (vector-set! row j (+ val up left (- diag))))))
    ;; count submatrices whose sum <= k
    (let ((cnt 0))
      (do ([i 0 (+ i 1)]) ((= i m))
        (do ([j 0 (+ j 1)]) ((= j n))
          (when (<= (vector-ref (vector-ref pref i) j) k)
            (set! cnt (+ cnt 1)))))
      cnt)))
```

## Erlang

```erlang
-spec count_submatrices(Grid :: [[integer()]], K :: integer()) -> integer().
count_submatrices([], _K) ->
    0;
count_submatrices(Grid, K) ->
    N = length(hd(Grid)),
    ZeroCols = lists:duplicate(N, 0),
    process_rows(Grid, ZeroCols, K, 0).

process_rows([], _ColSums, _K, Count) ->
    Count;
process_rows([Row | RestRows], ColSums, K, Count) ->
    UpdatedCols = lists:zipwith(fun(A, B) -> A + B end, ColSums, Row),
    NewCount = process_cols(UpdatedCols, 0, K, Count),
    process_rows(RestRows, UpdatedCols, K, NewCount).

process_cols([], _RunningSum, _K, Count) ->
    Count;
process_cols([C | Rest], RunningSum0, K, Count0) ->
    RunningSum = RunningSum0 + C,
    NewCount = if
        RunningSum =< K -> Count0 + 1;
        true -> Count0
    end,
    process_cols(Rest, RunningSum, K, NewCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_submatrices(grid :: [[integer]], k :: integer) :: integer
  def count_submatrices(grid, k) do
    n = length(hd(grid))

    {_final_cols, ans} =
      Enum.reduce(grid, {List.duplicate(0, n), 0}, fn row, {col_sums, cnt} ->
        new_col_sums = Enum.zip(col_sums, row) |> Enum.map(fn {c, v} -> c + v end)

        {new_cnt, _} =
          Enum.reduce(new_col_sums, {cnt, 0}, fn val, {c_acc, run_sum} ->
            new_run = run_sum + val
            new_c = if new_run <= k, do: c_acc + 1, else: c_acc
            {new_c, new_run}
          end)

        {new_col_sums, new_cnt}
      end)

    ans
  end
end
```

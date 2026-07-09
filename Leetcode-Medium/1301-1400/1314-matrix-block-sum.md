# 1314. Matrix Block Sum

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();
        vector<vector<int>> ps(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i < m; ++i) {
            int rowSum = 0;
            for (int j = 0; j < n; ++j) {
                rowSum += mat[i][j];
                ps[i + 1][j + 1] = ps[i][j + 1] + rowSum;
            }
        }
        vector<vector<int>> ans(m, vector<int>(n));
        for (int i = 0; i < m; ++i) {
            int r1 = max(0, i - k);
            int r2 = min(m - 1, i + k);
            for (int j = 0; j < n; ++j) {
                int c1 = max(0, j - k);
                int c2 = min(n - 1, j + k);
                ans[i][j] = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[][] matrixBlockSum(int[][] mat, int k) {
        int m = mat.length;
        int n = mat[0].length;
        long[][] pref = new long[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            long rowSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += mat[i][j];
                pref[i + 1][j + 1] = pref[i][j + 1] + rowSum;
            }
        }

        int[][] ans = new int[m][n];
        for (int i = 0; i < m; i++) {
            int r1 = Math.max(0, i - k);
            int r2 = Math.min(m - 1, i + k);
            for (int j = 0; j < n; j++) {
                int c1 = Math.max(0, j - k);
                int c2 = Math.min(n - 1, j + k);
                long sum = pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1];
                ans[i][j] = (int) sum;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        # prefix sum matrix with extra row and column (0-indexed)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = (
                    dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + mat[i][j]
                )
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            r1 = max(0, i - k)
            r2 = min(m - 1, i + k)
            for j in range(n):
                c1 = max(0, j - k)
                c2 = min(n - 1, j + k)
                total = (
                    dp[r2 + 1][c2 + 1]
                    - dp[r1][c2 + 1]
                    - dp[r2 + 1][c1]
                    + dp[r1][c1]
                )
                ans[i][j] = total
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # prefix sum matrix with extra row and column (0-indexed)
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row_sum

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            r1 = max(0, i - k)
            r2 = min(m - 1, i + k)
            for j in range(n):
                c1 = max(0, j - k)
                c2 = min(n - 1, j + k)
                total = (
                    ps[r2 + 1][c2 + 1]
                    - ps[r1][c2 + 1]
                    - ps[r2 + 1][c1]
                    + ps[r1][c1]
                )
                ans[i][j] = total
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixBlockSum(int** mat, int matSize, int* matColSize, int k, int* returnSize, int** returnColumnSizes) {
    int m = matSize;
    int n = matColSize[0];

    *returnSize = m;
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) {
        (*returnColumnSizes)[i] = n;
    }

    int rows = m + 1, cols = n + 1;
    int* ps = (int*)calloc(rows * cols, sizeof(int));

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int idx = (i + 1) * cols + (j + 1);
            ps[idx] = mat[i][j] + ps[i * cols + (j + 1)] + ps[(i + 1) * cols + j] - ps[i * cols + j];
        }
    }

    int** ans = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i) {
        ans[i] = (int*)malloc(n * sizeof(int));
    }

    for (int i = 0; i < m; ++i) {
        int r1 = i - k;
        if (r1 < 0) r1 = 0;
        int r2 = i + k;
        if (r2 >= m) r2 = m - 1;
        for (int j = 0; j < n; ++j) {
            int c1 = j - k;
            if (c1 < 0) c1 = 0;
            int c2 = j + k;
            if (c2 >= n) c2 = n - 1;

            int total = ps[(r2 + 1) * cols + (c2 + 1)]
                      - ps[r1 * cols + (c2 + 1)]
                      - ps[(r2 + 1) * cols + c1]
                      + ps[r1 * cols + c1];
            ans[i][j] = total;
        }
    }

    free(ps);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] MatrixBlockSum(int[][] mat, int k) {
        int m = mat.Length;
        int n = mat[0].Length;
        long[,] prefix = new long[m + 1, n + 1];
        for (int i = 0; i < m; i++) {
            long rowSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += mat[i][j];
                prefix[i + 1, j + 1] = prefix[i, j + 1] + rowSum;
            }
        }

        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) {
            ans[i] = new int[n];
            for (int j = 0; j < n; j++) {
                int r1 = Math.Max(0, i - k);
                int c1 = Math.Max(0, j - k);
                int r2 = Math.Min(m - 1, i + k);
                int c2 = Math.Min(n - 1, j + k);

                long sum = prefix[r2 + 1, c2 + 1]
                         - prefix[r1, c2 + 1]
                         - prefix[r2 + 1, c1]
                         + prefix[r1, c1];
                ans[i][j] = (int)sum;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[][]}
 */
var matrixBlockSum = function(mat, k) {
    const m = mat.length;
    const n = mat[0].length;
    // prefix sum with extra row and column (size (m+1)*(n+1))
    const ps = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; ++i) {
        let rowSum = 0;
        for (let j = 0; j < n; ++j) {
            rowSum += mat[i][j];
            ps[i + 1][j + 1] = ps[i][j + 1] + rowSum;
        }
    }

    const ans = Array.from({ length: m }, () => new Array(n).fill(0));
    for (let i = 0; i < m; ++i) {
        const r1 = Math.max(0, i - k);
        const r2 = Math.min(m - 1, i + k);
        for (let j = 0; j < n; ++j) {
            const c1 = Math.max(0, j - k);
            const c2 = Math.min(n - 1, j + k);
            // using prefix sums: sum of rectangle [r1..r2][c1..c2]
            const total = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
            ans[i][j] = total;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function matrixBlockSum(mat: number[][], k: number): number[][] {
    const m = mat.length;
    const n = mat[0].length;
    // prefix sum matrix (m+1) x (n+1)
    const ps: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i < m; ++i) {
        let rowSum = 0;
        for (let j = 0; j < n; ++j) {
            rowSum += mat[i][j];
            ps[i + 1][j + 1] = ps[i][j + 1] + rowSum;
        }
    }

    const ans: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));
    for (let i = 0; i < m; ++i) {
        const r1 = Math.max(0, i - k);
        const r2 = Math.min(m - 1, i + k);
        for (let j = 0; j < n; ++j) {
            const c1 = Math.max(0, j - k);
            const c2 = Math.min(n - 1, j + k);
            // using prefix sums: sum of rectangle [r1..r2][c1..c2]
            const total = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
            ans[i][j] = total;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Integer[][]
     */
    function matrixBlockSum($mat, $k) {
        $m = count($mat);
        $n = count($mat[0]);
        // Prefix sum matrix with extra row and column (initialized to 0)
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $dp[$i + 1][$j + 1] = $mat[$i][$j]
                    + $dp[$i][$j + 1]
                    + $dp[$i + 1][$j]
                    - $dp[$i][$j];
            }
        }

        $ans = array_fill(0, $m, array_fill(0, $n, 0));
        for ($i = 0; $i < $m; $i++) {
            $r1 = max(0, $i - $k);
            $r2 = min($m - 1, $i + $k);
            for ($j = 0; $j < $n; $j++) {
                $c1 = max(0, $j - $k);
                $c2 = min($n - 1, $j + $k);
                // Use prefix sums to compute block sum
                $sum = $dp[$r2 + 1][$c2 + 1]
                    - $dp[$r1][$c2 + 1]
                    - $dp[$r2 + 1][$c1]
                    + $dp[$r1][$c1];
                $ans[$i][$j] = $sum;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func matrixBlockSum(_ mat: [[Int]], _ k: Int) -> [[Int]] {
        let m = mat.count
        guard m > 0 else { return [] }
        let n = mat[0].count
        
        // Prefix sum matrix with extra row and column (size (m+1) x (n+1))
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        
        for i in 0..<m {
            var rowSum = 0
            for j in 0..<n {
                rowSum += mat[i][j]
                dp[i + 1][j + 1] = dp[i][j + 1] + rowSum
            }
        }
        
        var answer = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        for i in 0..<m {
            let r1 = max(0, i - k)
            let r2 = min(m - 1, i + k)
            for j in 0..<n {
                let c1 = max(0, j - k)
                let c2 = min(n - 1, j + k)
                
                // Using inclusion-exclusion on prefix sums
                let total = dp[r2 + 1][c2 + 1]
                        - dp[r1][c2 + 1]
                        - dp[r2 + 1][c1]
                        + dp[r1][c1]
                answer[i][j] = total
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun matrixBlockSum(mat: Array<IntArray>, k: Int): Array<IntArray> {
        val m = mat.size
        val n = mat[0].size
        val ps = Array(m + 1) { LongArray(n + 1) }
        for (i in 1..m) {
            var rowSum = 0L
            for (j in 1..n) {
                rowSum += mat[i - 1][j - 1]
                ps[i][j] = ps[i - 1][j] + rowSum
            }
        }
        val ans = Array(m) { IntArray(n) }
        for (i in 0 until m) {
            val r1 = maxOf(0, i - k)
            val r2 = minOf(m - 1, i + k)
            for (j in 0 until n) {
                val c1 = maxOf(0, j - k)
                val c2 = minOf(n - 1, j + k)
                val sum = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
                ans[i][j] = sum.toInt()
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> matrixBlockSum(List<List<int>> mat, int k) {
    int m = mat.length;
    int n = mat[0].length;

    // Prefix sum matrix with extra row and column (size (m+1) x (n+1))
    List<List<int>> prefix = List.generate(m + 1, (_) => List.filled(n + 1, 0));

    for (int i = 1; i <= m; ++i) {
      for (int j = 1; j <= n; ++j) {
        prefix[i][j] = mat[i - 1][j - 1] +
            prefix[i - 1][j] +
            prefix[i][j - 1] -
            prefix[i - 1][j - 1];
      }
    }

    List<List<int>> answer = List.generate(m, (_) => List.filled(n, 0));

    for (int i = 0; i < m; ++i) {
      int r1 = (i - k).clamp(0, m);
      int r2 = (i + k).clamp(0, m - 1);
      for (int j = 0; j < n; ++j) {
        int c1 = (j - k).clamp(0, n);
        int c2 = (j + k).clamp(0, n - 1);

        // Convert to prefix indices (+1)
        int sum = prefix[r2 + 1][c2 + 1] -
            prefix[r1][c2 + 1] -
            prefix[r2 + 1][c1] +
            prefix[r1][c1];
        answer[i][j] = sum;
      }
    }

    return answer;
  }
}
```

## Golang

```go
func matrixBlockSum(mat [][]int, k int) [][]int {
	m := len(mat)
	n := len(mat[0])
	// Prefix sum matrix with extra row and column
	dp := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		dp[i] = make([]int, n+1)
	}
	for i := 1; i <= m; i++ {
		rowSum := 0
		for j := 1; j <= n; j++ {
			rowSum += mat[i-1][j-1]
			dp[i][j] = dp[i-1][j] + rowSum
		}
	}
	ans := make([][]int, m)
	for i := 0; i < m; i++ {
		ans[i] = make([]int, n)
		r1 := i - k
		if r1 < 0 {
			r1 = 0
		}
		r2 := i + k
		if r2 >= m {
			r2 = m - 1
		}
		for j := 0; j < n; j++ {
			c1 := j - k
			if c1 < 0 {
				c1 = 0
			}
			c2 := j + k
			if c2 >= n {
				c2 = n - 1
			}
			sum := dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1]
			ans[i][j] = sum
		}
	}
	return ans
}
```

## Ruby

```ruby
def matrix_block_sum(mat, k)
  m = mat.length
  n = mat[0].length
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }

  (0...m).each do |i|
    row_sum = 0
    (0...n).each do |j|
      row_sum += mat[i][j]
      dp[i + 1][j + 1] = dp[i][j + 1] + row_sum
    end
  end

  ans = Array.new(m) { Array.new(n, 0) }
  (0...m).each do |i|
    r1 = [i - k, 0].max
    r2 = [i + k, m - 1].min
    (0...n).each do |j|
      c1 = [j - k, 0].max
      c2 = [j + k, n - 1].min
      ans[i][j] = dp[r2 + 1][c2 + 1] - dp[r1][c2 + 1] - dp[r2 + 1][c1] + dp[r1][c1]
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def matrixBlockSum(mat: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        val m = mat.length
        val n = if (m == 0) 0 else mat(0).length
        val ps = Array.ofDim[Int](m + 1, n + 1)
        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                ps(i + 1)(j + 1) = mat(i)(j) + ps(i)(j + 1) + ps(i + 1)(j) - ps(i)(j)
                j += 1
            }
            i += 1
        }

        val ans = Array.ofDim[Int](m, n)
        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                val r1 = math.max(0, i - k)
                val c1 = math.max(0, j - k)
                val r2 = math.min(m - 1, i + k)
                val c2 = math.min(n - 1, j + k)

                ans(i)(j) = ps(r2 + 1)(c2 + 1) - ps(r1)(c2 + 1) - ps(r2 + 1)(c1) + ps(r1)(c1)
                j += 1
            }
            i += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn matrix_block_sum(mat: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = mat.len();
        let n = mat[0].len();
        // Prefix sum matrix using i64 to avoid overflow
        let mut ps = vec![vec![0i64; n + 1]; m + 1];
        for i in 0..m {
            let mut row_sum: i64 = 0;
            for j in 0..n {
                row_sum += mat[i][j] as i64;
                ps[i + 1][j + 1] = ps[i][j + 1] + row_sum;
            }
        }

        let k_usize = k as usize;
        let mut ans = vec![vec![0i32; n]; m];
        for i in 0..m {
            let r1 = if i >= k_usize { i - k_usize } else { 0 };
            let r2 = std::cmp::min(i + k_usize, m - 1);
            for j in 0..n {
                let c1 = if j >= k_usize { j - k_usize } else { 0 };
                let c2 = std::cmp::min(j + k_usize, n - 1);
                let total = ps[r2 + 1][c2 + 1]
                    - ps[r1][c2 + 1]
                    - ps[r2 + 1][c1]
                    + ps[r1][c1];
                ans[i][j] = total as i32;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (matrix-block-sum mat k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let* ((m (length mat))
         (n (if (zero? m) 0 (length (first mat))))
         (dp (make-vector (+ m 1))))
    ;; initialize dp rows
    (for ([i (in-range (+ m 1))])
      (vector-set! dp i (make-vector (+ n 1) 0)))
    ;; build prefix sum matrix
    (for ([i (in-range 1 (add1 m))])
      (let ((row (list-ref mat (sub1 i))))
        (for ([j (in-range 1 (add1 n))])
          (define val (list-ref row (sub1 j)))
          (define up   (vector-ref (vector-ref dp (sub1 i)) j))
          (define left (vector-ref (vector-ref dp i) (sub1 j)))
          (define diag (vector-ref (vector-ref dp (sub1 i)) (sub1 j)))
          (vector-set! (vector-ref dp i) j (+ val up left (- diag))))))
    ;; compute answer matrix
    (for/list ([i (in-range m)])
      (for/list ([j (in-range n)])
        (let* ((r1 (max 0 (- i k)))
               (c1 (max 0 (- j k)))
               (r2 (min (sub1 m) (+ i k)))
               (c2 (min (sub1 n) (+ j k)))
               (a (vector-ref (vector-ref dp (+ r2 1)) (+ c2 1))) ; dp[r2+1][c2+1]
               (b (vector-ref (vector-ref dp r1)       (+ c2 1))) ; dp[r1][c2+1]
               (c (vector-ref (vector-ref dp (+ r2 1)) c1))        ; dp[r2+1][c1]
               (d (vector-ref (vector-ref dp r1)       c1)))      ; dp[r1][c1]
          (- a b c d))))))
```

## Erlang

```erlang
-spec matrix_block_sum(Mat :: [[integer()]], K :: integer()) -> [[integer()]].
matrix_block_sum(Mat, K) ->
    M = length(Mat),
    N = length(hd(Mat)),
    [ [ block_sum(I, J, Mat, K, M, N) || J <- lists:seq(1, N) ] || I <- lists:seq(1, M) ].

block_sum(I, J, Mat, K, M, N) ->
    R1 = erlang:max(1, I - K),
    R2 = erlang:min(M, I + K),
    C1 = erlang:max(1, J - K),
    C2 = erlang:min(N, J + K),
    lists:foldl(fun(R, Acc) ->
        RowList = lists:nth(R, Mat),
        RowSum = sum_range(RowList, C1, C2),
        Acc + RowSum
    end, 0, lists:seq(R1, R2)).

sum_range(List, From, To) ->
    Len = To - From + 1,
    Sub = lists:sublist(List, From, Len),
    lists:foldl(fun(X, Acc) -> X + Acc end, 0, Sub).
```

## Elixir

```elixir
defmodule Solution do
  @spec matrix_block_sum(mat :: [[integer]], k :: integer) :: [[integer]]
  def matrix_block_sum(mat, k) do
    m = length(mat)
    n = mat |> hd() |> length()

    for i <- 0..(m - 1) do
      for j <- 0..(n - 1) do
        r_start = max(i - k, 0)
        r_end = min(i + k, m - 1)
        c_start = max(j - k, 0)
        c_end = min(j + k, n - 1)

        Enum.reduce(r_start..r_end, 0, fn r, acc ->
          row = Enum.at(mat, r)
          len = c_end - c_start + 1
          segment = Enum.slice(row, c_start, len)
          acc + Enum.sum(segment)
        end)
      end
    end
  end
end
```

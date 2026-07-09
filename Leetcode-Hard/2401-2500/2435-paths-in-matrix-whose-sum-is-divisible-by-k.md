# 2435. Paths in Matrix Whose Sum Is Divisible by K

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        const int MOD = 1'000'000'007;
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(k, 0)));
        dp[0][0][grid[0][0] % k] = 1;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) continue;
                vector<int> cur(k, 0);
                int valMod = grid[i][j] % k;
                if (i > 0) {
                    for (int r = 0; r < k; ++r) {
                        if (dp[i-1][j][r]) {
                            int nr = (r + valMod) % k;
                            cur[nr] = (cur[nr] + dp[i-1][j][r]) % MOD;
                        }
                    }
                }
                if (j > 0) {
                    for (int r = 0; r < k; ++r) {
                        if (dp[i][j-1][r]) {
                            int nr = (r + valMod) % k;
                            cur[nr] = (cur[nr] + dp[i][j-1][r]) % MOD;
                        }
                    }
                }
                dp[i][j].swap(cur);
            }
        }
        return dp[m-1][n-1][0];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int numberOfPaths(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[n][k]; // dp[j] holds counts for cell (current row, j)
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j] % k;
                if (val < 0) val += k;
                int[] cur = new int[k];
                
                if (i == 0 && j == 0) {
                    cur[val] = 1;
                } else {
                    // from top
                    if (i > 0) {
                        int[] up = dp[j];
                        for (int r = 0; r < k; r++) {
                            int cnt = up[r];
                            if (cnt != 0) {
                                int nr = r + val;
                                if (nr >= k) nr -= k;
                                cur[nr] = (int)((cur[nr] + (long)cnt) % MOD);
                            }
                        }
                    }
                    // from left
                    if (j > 0) {
                        int[] left = dp[j - 1];
                        for (int r = 0; r < k; r++) {
                            int cnt = left[r];
                            if (cnt != 0) {
                                int nr = r + val;
                                if (nr >= k) nr -= k;
                                cur[nr] = (int)((cur[nr] + (long)cnt) % MOD);
                            }
                        }
                    }
                }
                dp[j] = cur; // store result for this cell
            }
        }
        return dp[n - 1][0];
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        # dp[j][r] - number of ways to reach cell (current row, j) with sum % k == r
        dp = [[0] * k for _ in range(n)]
        for i in range(m):
            new_dp = [[0] * k for _ in range(n)]
            for j in range(n):
                cur_mod = grid[i][j] % k
                if i == 0 and j == 0:
                    new_dp[j][cur_mod] = 1
                    continue
                # from top cell (i-1, j)
                if i > 0:
                    for r in range(k):
                        cnt = dp[j][r]
                        if cnt:
                            nr = (r + cur_mod) % k
                            new_dp[j][nr] = (new_dp[j][nr] + cnt) % MOD
                # from left cell (i, j-1)
                if j > 0:
                    for r in range(k):
                        cnt = new_dp[j - 1][r]
                        if cnt:
                            nr = (r + cur_mod) % k
                            new_dp[j][nr] = (new_dp[j][nr] + cnt) % MOD
            dp = new_dp
        return dp[n - 1][0]
```

## Python3

```python
class Solution:
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp_prev_row = [[0] * k for _ in range(n)]
        for i in range(m):
            cur_row = [[0] * k for _ in range(n)]
            for j in range(n):
                val = grid[i][j] % k
                if i == 0 and j == 0:
                    cur_row[j][val] = 1
                else:
                    # from top
                    if i > 0:
                        prev = dp_prev_row[j]
                        for r, cnt in enumerate(prev):
                            if cnt:
                                nr = (r + val) % k
                                cur_row[j][nr] = (cur_row[j][nr] + cnt) % MOD
                    # from left
                    if j > 0:
                        prev = cur_row[j - 1]
                        for r, cnt in enumerate(prev):
                            if cnt:
                                nr = (r + val) % k
                                cur_row[j][nr] = (cur_row[j][nr] + cnt) % MOD
            dp_prev_row = cur_row
        return dp_prev_row[-1][0]
```

## C

```c
#include <stdlib.h>
#include <string.h>

int numberOfPaths(int** grid, int gridSize, int* gridColSize, int k) {
    const int MOD = 1000000007;
    int m = gridSize;
    int n = gridColSize[0];
    long long totalCells = (long long)m * n;
    int *dp = (int *)calloc(totalCells * k, sizeof(int));
    if (!dp) return 0;

    int startRem = grid[0][0] % k;
    dp[(0 * n + 0) * k + startRem] = 1;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) continue;
            int *cur = dp + ((i * n + j) * k);
            if (i > 0) {
                int *up = dp + (((i - 1) * n + j) * k);
                for (int r = 0; r < k; ++r) {
                    int cnt = up[r];
                    if (!cnt) continue;
                    int nr = (r + grid[i][j]) % k;
                    cur[nr] = (cur[nr] + cnt) % MOD;
                }
            }
            if (j > 0) {
                int *left = dp + ((i * n + (j - 1)) * k);
                for (int r = 0; r < k; ++r) {
                    int cnt = left[r];
                    if (!cnt) continue;
                    int nr = (r + grid[i][j]) % k;
                    cur[nr] = (cur[nr] + cnt) % MOD;
                }
            }
        }
    }

    int result = dp[((m - 1) * n + (n - 1)) * k + 0];
    free(dp);
    return result;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1_000_000_007;
    public int NumberOfPaths(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[,,] dp = new int[m, n, k];
        
        int startRem = grid[0][0] % k;
        dp[0, 0, startRem] = 1;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                int curVal = grid[i][j] % k;
                
                // From top
                if (i > 0) {
                    for (int r = 0; r < k; r++) {
                        int cnt = dp[i - 1, j, r];
                        if (cnt != 0) {
                            int nr = r + curVal;
                            if (nr >= k) nr -= k;
                            int sum = dp[i, j, nr] + cnt;
                            if (sum >= MOD) sum -= MOD;
                            dp[i, j, nr] = sum;
                        }
                    }
                }
                
                // From left
                if (j > 0) {
                    for (int r = 0; r < k; r++) {
                        int cnt = dp[i, j - 1, r];
                        if (cnt != 0) {
                            int nr = r + curVal;
                            if (nr >= k) nr -= k;
                            int sum = dp[i, j, nr] + cnt;
                            if (sum >= MOD) sum -= MOD;
                            dp[i, j, nr] = sum;
                        }
                    }
                }
            }
        }
        
        return dp[m - 1, n - 1, 0];
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
var numberOfPaths = function(grid, k) {
    const MOD = 1000000007;
    const m = grid.length;
    const n = grid[0].length;

    let prevRow = new Array(n);
    for (let i = 0; i < m; ++i) {
        const currRow = new Array(n);
        for (let j = 0; j < n; ++j) {
            const valMod = grid[i][j] % k;
            const cur = new Array(k).fill(0);

            if (i === 0 && j === 0) {
                cur[valMod] = 1;
            } else {
                // from top
                if (i > 0) {
                    const up = prevRow[j];
                    for (let r = 0; r < k; ++r) {
                        const cnt = up[r];
                        if (cnt) {
                            const nr = (r + valMod) % k;
                            cur[nr] = (cur[nr] + cnt) % MOD;
                        }
                    }
                }
                // from left
                if (j > 0) {
                    const left = currRow[j - 1];
                    for (let r = 0; r < k; ++r) {
                        const cnt = left[r];
                        if (cnt) {
                            const nr = (r + valMod) % k;
                            cur[nr] = (cur[nr] + cnt) % MOD;
                        }
                    }
                }
            }

            currRow[j] = cur;
        }
        prevRow = currRow;
    }

    return prevRow[n - 1][0] % MOD;
};
```

## Typescript

```typescript
function numberOfPaths(grid: number[][], k: number): number {
    const MOD = 1_000_000_007;
    const m = grid.length;
    const n = grid[0].length;

    // previous row DP
    let prev: number[][] = new Array(n);
    for (let j = 0; j < n; ++j) prev[j] = new Array(k).fill(0);

    for (let i = 0; i < m; ++i) {
        const cur: number[][] = new Array(n);
        for (let j = 0; j < n; ++j) cur[j] = new Array(k).fill(0);

        for (let j = 0; j < n; ++j) {
            const val = ((grid[i][j] % k) + k) % k;

            if (i === 0 && j === 0) {
                cur[0][val] = 1;
                continue;
            }

            // from top
            if (i > 0) {
                const top = prev[j];
                for (let r = 0; r < k; ++r) {
                    const cnt = top[r];
                    if (cnt !== 0) {
                        const nr = (r + val) % k;
                        let sum = cur[j][nr] + cnt;
                        if (sum >= MOD) sum -= MOD;
                        cur[j][nr] = sum;
                    }
                }
            }

            // from left
            if (j > 0) {
                const left = cur[j - 1];
                for (let r = 0; r < k; ++r) {
                    const cnt = left[r];
                    if (cnt !== 0) {
                        const nr = (r + val) % k;
                        let sum = cur[j][nr] + cnt;
                        if (sum >= MOD) sum -= MOD;
                        cur[j][nr] = sum;
                    }
                }
            }
        }

        prev = cur;
    }

    return prev[n - 1][0];
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
    function numberOfPaths($grid, $k) {
        $mod = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);

        // previous row DP: n columns each with k remainders
        $prev = array_fill(0, $n, array_fill(0, $k, 0));

        for ($i = 0; $i < $m; $i++) {
            // current row DP
            $curr = array_fill(0, $n, array_fill(0, $k, 0));
            for ($j = 0; $j < $n; $j++) {
                $valMod = $grid[$i][$j] % $k;
                if ($i == 0 && $j == 0) {
                    $curr[0][$valMod] = 1;
                    continue;
                }

                // from top cell
                if ($i > 0) {
                    for ($r = 0; $r < $k; $r++) {
                        $cnt = $prev[$j][$r];
                        if ($cnt) {
                            $nr = ($r + $valMod) % $k;
                            $curr[$j][$nr] = ($curr[$j][$nr] + $cnt) % $mod;
                        }
                    }
                }

                // from left cell
                if ($j > 0) {
                    for ($r = 0; $r < $k; $r++) {
                        $cnt = $curr[$j - 1][$r];
                        if ($cnt) {
                            $nr = ($r + $valMod) % $k;
                            $curr[$j][$nr] = ($curr[$j][$nr] + $cnt) % $mod;
                        }
                    }
                }
            }
            $prev = $curr;
        }

        return $prev[$n - 1][0];
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPaths(_ grid: [[Int]], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let m = grid.count
        let n = grid[0].count
        var prev = Array(repeating: Array(repeating: 0, count: k), count: n)
        var curr = Array(repeating: Array(repeating: 0, count: k), count: n)

        for i in 0..<m {
            for j in 0..<n {
                var ways = Array(repeating: 0, count: k)
                let valMod = grid[i][j] % k
                if i == 0 && j == 0 {
                    ways[valMod] = 1
                } else {
                    if i > 0 {
                        let top = prev[j]
                        for r in 0..<k where top[r] != 0 {
                            let newRem = (r + valMod) % k
                            var sum = ways[newRem] + top[r]
                            if sum >= MOD { sum -= MOD }
                            ways[newRem] = sum
                        }
                    }
                    if j > 0 {
                        let left = curr[j - 1]
                        for r in 0..<k where left[r] != 0 {
                            let newRem = (r + valMod) % k
                            var sum = ways[newRem] + left[r]
                            if sum >= MOD { sum -= MOD }
                            ways[newRem] = sum
                        }
                    }
                }
                curr[j] = ways
            }
            prev = curr
            if i != m - 1 {
                for col in 0..<n {
                    curr[col] = Array(repeating: 0, count: k)
                }
            }
        }

        return prev[n - 1][0] % MOD
    }
}
```

## Kotlin

```kotlin
import java.util.Arrays

class Solution {
    fun numberOfPaths(grid: Array<IntArray>, k: Int): Int {
        val MOD = 1_000_000_007L
        val m = grid.size
        val n = grid[0].size

        var prev = Array(n) { IntArray(k) }
        var curr = Array(n) { IntArray(k) }

        for (i in 0 until m) {
            for (j in 0 until n) {
                val cur = IntArray(k)
                val add = grid[i][j] % k
                if (i == 0 && j == 0) {
                    cur[add] = 1
                } else {
                    if (i > 0) {
                        val top = prev[j]
                        for (r in 0 until k) {
                            val cnt = top[r]
                            if (cnt != 0) {
                                val nr = (r + add) % k
                                cur[nr] = ((cur[nr].toLong() + cnt) % MOD).toInt()
                            }
                        }
                    }
                    if (j > 0) {
                        val left = curr[j - 1]
                        for (r in 0 until k) {
                            val cnt = left[r]
                            if (cnt != 0) {
                                val nr = (r + add) % k
                                cur[nr] = ((cur[nr].toLong() + cnt) % MOD).toInt()
                            }
                        }
                    }
                }
                curr[j] = cur
            }
            // swap prev and curr for next row
            val temp = prev
            prev = curr
            curr = temp
            // clear the new curr (old prev) arrays
            for (j in 0 until n) {
                Arrays.fill(curr[j], 0)
            }
        }
        return prev[n - 1][0] % MOD.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int numberOfPaths(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;

    // dpPrev and dpCurr store for each column a list of size k
    List<List<int>> dpPrev =
        List.generate(n, (_) => List.filled(k, 0), growable: false);
    List<List<int>> dpCurr =
        List.generate(n, (_) => List.filled(k, 0), growable: false);

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        List<int> cur = List.filled(k, 0);
        int valMod = grid[i][j] % k;

        if (i == 0 && j == 0) {
          // Starting cell
          cur[valMod] = 1;
        } else {
          // From top
          if (i > 0) {
            List<int> top = dpPrev[j];
            for (int r = 0; r < k; ++r) {
              int cnt = top[r];
              if (cnt != 0) {
                int nr = r + valMod;
                if (nr >= k) nr -= k;
                cur[nr] = (cur[nr] + cnt) % _MOD;
              }
            }
          }
          // From left
          if (j > 0) {
            List<int> left = dpCurr[j - 1];
            for (int r = 0; r < k; ++r) {
              int cnt = left[r];
              if (cnt != 0) {
                int nr = r + valMod;
                if (nr >= k) nr -= k;
                cur[nr] = (cur[nr] + cnt) % _MOD;
              }
            }
          }
        }

        dpCurr[j] = cur;
      }
      // Prepare for next row: swap references
      var temp = dpPrev;
      dpPrev = dpCurr;
      dpCurr = temp;
    }

    return dpPrev[n - 1][0] % _MOD;
  }
}
```

## Golang

```go
func numberOfPaths(grid [][]int, k int) int {
	const mod = 1000000007
	m, n := len(grid), len(grid[0])
	// dp[j] holds the remainder counts for column j of the previous processed row (or current row after update)
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, k)
	}
	var left []int
	for i := 0; i < m; i++ {
		left = nil
		for j := 0; j < n; j++ {
			cur := make([]int, k)
			valMod := grid[i][j] % k
			if i == 0 && j == 0 {
				cur[valMod] = 1
			} else {
				// from top
				if i > 0 {
					top := dp[j]
					for r := 0; r < k; r++ {
						cnt := top[r]
						if cnt == 0 {
							continue
						}
						newRem := (r + valMod) % k
						cur[newRem] = (cur[newRem] + cnt) % mod
					}
				}
				// from left
				if j > 0 {
					for r := 0; r < k; r++ {
						cnt := left[r]
						if cnt == 0 {
							continue
						}
						newRem := (r + valMod) % k
						cur[newRem] = (cur[newRem] + cnt) % mod
					}
				}
			}
			dp[j] = cur
			left = cur
		}
	}
	return dp[n-1][0] % mod
}
```

## Ruby

```ruby
def number_of_paths(grid, k)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length

  dp_prev = Array.new(n) { Array.new(k, 0) }
  dp_curr = Array.new(n) { Array.new(k, 0) }

  (0...m).each do |i|
    (0...n).each do |j|
      val = grid[i][j] % k
      new_counts = Array.new(k, 0)

      if i == 0 && j == 0
        new_counts[val] = 1
      else
        if i > 0
          top = dp_prev[j]
          r = 0
          while r < k
            cnt = top[r]
            if cnt != 0
              nr = (r + val) % k
              new_counts[nr] = (new_counts[nr] + cnt) % mod
            end
            r += 1
          end
        end

        if j > 0
          left = dp_curr[j - 1]
          r = 0
          while r < k
            cnt = left[r]
            if cnt != 0
              nr = (r + val) % k
              new_counts[nr] = (new_counts[nr] + cnt) % mod
            end
            r += 1
          end
        end
      end

      dp_curr[j] = new_counts
    end
    dp_prev, dp_curr = dp_curr, dp_prev
  end

  dp_prev[n - 1][0] % mod
end
```

## Scala

```scala
object Solution {
  def numberOfPaths(grid: Array[Array[Int]], k: Int): Int = {
    val MOD = 1000000007
    val m = grid.length
    val n = grid(0).length

    var prev = Array.ofDim[Int](n, k)
    var cur = Array.ofDim[Int](n, k)

    for (i <- 0 until m) {
      for (j <- 0 until n) {
        // reset current cell array
        java.util.Arrays.fill(cur(j), 0)

        if (i == 0 && j == 0) {
          val rem = ((grid(0)(0) % k) + k) % k
          cur(j)(rem) = 1
        } else {
          // from top
          if (i > 0) {
            val topArr = prev(j)
            var r = 0
            while (r < k) {
              val cnt = topArr(r)
              if (cnt != 0) {
                val newRem = (r + grid(i)(j)) % k
                var v = cur(j)(newRem) + cnt
                if (v >= MOD) v -= MOD
                cur(j)(newRem) = v
              }
              r += 1
            }
          }
          // from left
          if (j > 0) {
            val leftArr = cur(j - 1)
            var r = 0
            while (r < k) {
              val cnt = leftArr(r)
              if (cnt != 0) {
                val newRem = (r + grid(i)(j)) % k
                var v = cur(j)(newRem) + cnt
                if (v >= MOD) v -= MOD
                cur(j)(newRem) = v
              }
              r += 1
            }
          }
        }
      }
      // swap rows for next iteration
      val temp = prev
      prev = cur
      cur = temp
    }

    prev(n - 1)(0) % MOD
  }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m = grid.len();
        let n = grid[0].len();
        let k_usize = k as usize;

        // dp[j][r] = number of ways to reach cell (current row, j) with sum % k == r
        let mut dp: Vec<Vec<i64>> = vec![vec![0; k_usize]; n];

        for i in 0..m {
            let mut left: Vec<i64> = vec![0; k_usize];
            for j in 0..n {
                let mut cur = vec![0i64; k_usize];
                let val = (grid[i][j] % k) as usize;

                if i == 0 && j == 0 {
                    cur[val] = 1;
                } else {
                    // from top
                    if i > 0 {
                        for r in 0..k_usize {
                            let cnt = dp[j][r];
                            if cnt != 0 {
                                let nr = (r + val) % k_usize;
                                cur[nr] = (cur[nr] + cnt) % MOD;
                            }
                        }
                    }
                    // from left
                    if j > 0 {
                        for r in 0..k_usize {
                            let cnt = left[r];
                            if cnt != 0 {
                                let nr = (r + val) % k_usize;
                                cur[nr] = (cur[nr] + cnt) % MOD;
                            }
                        }
                    }
                }

                // store results for this column and update left neighbor
                dp[j] = cur.clone();
                left = cur;
            }
        }

        dp[n - 1][0] as i32
    }
}
```

## Racket

```racket
#lang racket
(require rackunit) ; for contract support if needed

(define MOD 1000000007)

(define/contract (number-of-paths grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([rows (list->vector (map list->vector grid))]
         [m (vector-length rows)]
         [n (if (= m 0) 0 (vector-length (vector-ref rows 0)))])
    (define prev (make-vector n #f))
    (for ([i (in-range m)])
      (define curr (make-vector n #f))
      (for ([j (in-range n)])
        (define cur-vec (make-vector k 0))
        (define val (modulo (vector-ref (vector-ref rows i) j) k))
        (if (and (= i 0) (= j 0))
            (vector-set! cur-vec val 1)
            (begin
              (when (> i 0)
                (define top-vec (vector-ref prev j))
                (for ([r (in-range k)])
                  (define cnt (vector-ref top-vec r))
                  (when (positive? cnt)
                    (define new-r (modulo (+ r val) k))
                    (vector-set! cur-vec new-r
                                 (modulo (+ (vector-ref cur-vec new-r) cnt) MOD)))))
              (when (> j 0)
                (define left-vec (vector-ref curr (sub1 j)))
                (for ([r (in-range k)])
                  (define cnt (vector-ref left-vec r))
                  (when (positive? cnt)
                    (define new-r (modulo (+ r val) k))
                    (vector-set! cur-vec new-r
                                 (modulo (+ (vector-ref cur-vec new-r) cnt) MOD)))))))
        (vector-set! curr j cur-vec))
      (set! prev curr))
    (define final-vec (vector-ref prev (sub1 n)))
    (vector-ref final-vec 0)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_paths/2]).

-define(MOD, 1000000007).

number_of_paths(Grid, K) ->
    {FinalRowDP,_} = lists:foldl(
        fun(RowVals, {PrevRowDP, RowIdx}) ->
            CurrRowDP = process_row(RowIdx, RowVals, PrevRowDP, K),
            {CurrRowDP, RowIdx + 1}
        end,
        {[],0},
        Grid),
    case FinalRowDP of
        [] -> 0;
        _ ->
            N = length(FinalRowDP),
            LastCellDP = lists:nth(N, FinalRowDP),
            array:get(0, LastCellDP) rem ?MOD
    end.

process_row(RowIdx, RowVals, PrevRowDP, K) ->
    N = length(RowVals),
    {RevRowDP,_} = lists:foldl(
        fun(ColIdx, {RevAcc, LeftDP}) ->
            Val = lists:nth(ColIdx + 1, RowVals),
            TopDP = case RowIdx of
                0 -> undefined;
                _ -> lists:nth(ColIdx + 1, PrevRowDP)
            end,
            CurrDP = compute_cell_dp(Val, TopDP, LeftDP, K),
            {[CurrDP | RevAcc], CurrDP}
        end,
        {[], undefined},
        lists:seq(0, N - 1)),
    lists:reverse(RevRowDP).

compute_cell_dp(Val, undefined, undefined, K) ->
    Arr = array:new(K, {default,0}),
    R = Val rem K,
    array:set(R, 1, Arr);
compute_cell_dp(Val, TopDP, LeftDP, K) ->
    Sources = case {TopDP,LeftDP} of
        {undefined, undefined} -> [];
        {undefined, L} when L =/= undefined -> [L];
        {T, undefined} when T =/= undefined -> [T];
        {T, L} -> [T,L]
    end,
    combine_sources(Sources, Val, K).

combine_sources(SrcList, Val, K) ->
    InitArr = array:new(K, {default,0}),
    lists:foldl(
        fun(SrcDP, AccArr) ->
            fold_src_dp(SrcDP, Val, AccArr, K)
        end,
        InitArr,
        SrcList).

fold_src_dp(SrcDP, Val, AccArr, K) ->
    lists:foldl(
        fun(R, A) ->
            C = array:get(R, SrcDP),
            case C of
                0 -> A;
                _ ->
                    NewR = (R + Val) rem K,
                    Old = array:get(NewR, A),
                    NewVal = (Old + C) rem ?MOD,
                    array:set(NewR, NewVal, A)
            end
        end,
        AccArr,
        lists:seq(0, K - 1)).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec number_of_paths(grid :: [[integer]], k :: integer) :: integer
  def number_of_paths(grid, k) do
    m = length(grid)
    n = length(hd(grid))

    zero_vec = :erlang.list_to_tuple(List.duplicate(0, k))
    # initial previous row (all zeros)
    prev_row = List.duplicate(zero_vec, n)

    final_prev =
      Enum.reduce(Enum.with_index(grid), prev_row, fn {row, i}, prev ->
        # process one row
        {cur_rev, _left, _rest} =
          Enum.reduce(row, {[], nil, if(i > 0, do: prev, else: [])}, fn cell,
                                                                    {cur_rev, left_vec, tops} ->
            {top_vec, new_tops} =
              case tops do
                [] -> {nil, []}
                [h | t] -> {h, t}
              end

            new_vec =
              if i == 0 and cur_rev == [] do
                # (0,0) cell
                rem = rem(cell, k)
                put_elem(zero_vec, rem, 1)
              else
                Enum.reduce(0..k - 1, zero_vec, fn r, acc ->
                  cnt = 0

                  if top_vec != nil do
                    cnt = cnt + elem(top_vec, r)
                  end

                  if left_vec != nil do
                    cnt = cnt + elem(left_vec, r)
                  end

                  if cnt == 0 do
                    acc
                  else
                    new_rem = rem(r + cell, k)
                    cur = elem(acc, new_rem)
                    updated = rem(cur + cnt, @mod)
                    put_elem(acc, new_rem, updated)
                  end
                end)
              end

            {[new_vec | cur_rev], new_vec, new_tops}
          end)

        Enum.reverse(cur_rev)
      end)

    final_vec = List.last(final_prev)
    elem(final_vec, 0) |> rem(@mod)
  end
end
```

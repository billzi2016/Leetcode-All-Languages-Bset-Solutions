# 1594. Maximum Non Negative Product in a Matrix

## Cpp

```cpp
class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        const long long MOD = 1000000007LL;
        int m = grid.size(), n = grid[0].size();
        vector<vector<long long>> dpMax(m, vector<long long>(n, LLONG_MIN));
        vector<vector<long long>> dpMin(m, vector<long long>(n, LLONG_MAX));
        dpMax[0][0] = dpMin[0][0] = grid[0][0];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) continue;
                long long curMax = LLONG_MIN, curMin = LLONG_MAX;
                long long val = grid[i][j];
                // from top
                if (i > 0) {
                    long long a = dpMax[i-1][j];
                    long long b = dpMin[i-1][j];
                    if (a != LLONG_MIN) {
                        curMax = max(curMax, a * val);
                        curMin = min(curMin, a * val);
                    }
                    if (b != LLONG_MAX) {
                        curMax = max(curMax, b * val);
                        curMin = min(curMin, b * val);
                    }
                }
                // from left
                if (j > 0) {
                    long long a = dpMax[i][j-1];
                    long long b = dpMin[i][j-1];
                    if (a != LLONG_MIN) {
                        curMax = max(curMax, a * val);
                        curMin = min(curMin, a * val);
                    }
                    if (b != LLONG_MAX) {
                        curMax = max(curMax, b * val);
                        curMin = min(curMin, b * val);
                    }
                }
                dpMax[i][j] = curMax;
                dpMin[i][j] = curMin;
            }
        }
        long long ans = dpMax[m-1][n-1];
        if (ans < 0) return -1;
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int maxProductPath(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        long[][] maxDP = new long[m][n];
        long[][] minDP = new long[m][n];
        maxDP[0][0] = minDP[0][0] = grid[0][0];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                long curMax = Long.MIN_VALUE;
                long curMin = Long.MAX_VALUE;
                int val = grid[i][j];
                // from top
                if (i > 0) {
                    long a = maxDP[i - 1][j];
                    long b = minDP[i - 1][j];
                    if (val >= 0) {
                        curMax = Math.max(curMax, a * val);
                        curMin = Math.min(curMin, b * val);
                    } else {
                        curMax = Math.max(curMax, b * val);
                        curMin = Math.min(curMin, a * val);
                    }
                }
                // from left
                if (j > 0) {
                    long a = maxDP[i][j - 1];
                    long b = minDP[i][j - 1];
                    if (val >= 0) {
                        curMax = Math.max(curMax, a * val);
                        curMin = Math.min(curMin, b * val);
                    } else {
                        curMax = Math.max(curMax, b * val);
                        curMin = Math.min(curMin, a * val);
                    }
                }
                maxDP[i][j] = curMax;
                minDP[i][j] = curMin;
            }
        }
        long result = maxDP[m - 1][n - 1];
        if (result < 0) return -1;
        return (int)(result % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]

        dp_max[0][0] = dp_min[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                candidates = []
                if i > 0:
                    candidates.append(dp_max[i - 1][j] * val)
                    candidates.append(dp_min[i - 1][j] * val)
                if j > 0:
                    candidates.append(dp_max[i][j - 1] * val)
                    candidates.append(dp_min[i][j - 1] * val)
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)

        result = dp_max[m - 1][n - 1]
        return -1 if result < 0 else result % MOD
```

## Python3

```python
class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if i == 0 and j == 0:
                    max_dp[i][j] = min_dp[i][j] = val
                else:
                    candidates = []
                    if i > 0:
                        candidates.append(max_dp[i-1][j] * val)
                        candidates.append(min_dp[i-1][j] * val)
                    if j > 0:
                        candidates.append(max_dp[i][j-1] * val)
                        candidates.append(min_dp[i][j-1] * val)
                    max_dp[i][j] = max(candidates)
                    min_dp[i][j] = min(candidates)

        result = max_dp[m-1][n-1]
        return -1 if result < 0 else result % MOD
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int maxProductPath(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    const long long MOD = 1000000007LL;

    long long *dpMin = (long long *)malloc(m * n * sizeof(long long));
    long long *dpMax = (long long *)malloc(m * n * sizeof(long long));

    dpMin[0] = dpMax[0] = grid[0][0];

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) continue;
            long long cur = grid[i][j];
            long long minVal = LLONG_MAX;
            long long maxVal = LLONG_MIN;

            if (i > 0) {
                long long a = dpMin[(i - 1) * n + j];
                long long b = dpMax[(i - 1) * n + j];
                long long p1 = a * cur;
                long long p2 = b * cur;
                if (p1 < minVal) minVal = p1;
                if (p2 < minVal) minVal = p2;
                if (p1 > maxVal) maxVal = p1;
                if (p2 > maxVal) maxVal = p2;
            }
            if (j > 0) {
                long long a = dpMin[i * n + (j - 1)];
                long long b = dpMax[i * n + (j - 1)];
                long long p1 = a * cur;
                long long p2 = b * cur;
                if (p1 < minVal) minVal = p1;
                if (p2 < minVal) minVal = p2;
                if (p1 > maxVal) maxVal = p1;
                if (p2 > maxVal) maxVal = p2;
            }

            dpMin[i * n + j] = minVal;
            dpMax[i * n + j] = maxVal;
        }
    }

    long long result = dpMax[(m - 1) * n + (n - 1)];
    free(dpMin);
    free(dpMax);

    if (result < 0) return -1;
    return (int)(result % MOD);
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaxProductPath(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        const long MOD = 1000000007L;
        long[,] maxProd = new long[m, n];
        long[,] minProd = new long[m, n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                long val = grid[i][j];
                if (i == 0 && j == 0) {
                    maxProd[i, j] = val;
                    minProd[i, j] = val;
                } else {
                    long curMax = long.MinValue;
                    long curMin = long.MaxValue;

                    if (i > 0) {
                        long a = maxProd[i - 1, j] * val;
                        long b = minProd[i - 1, j] * val;
                        curMax = Math.Max(curMax, Math.Max(a, b));
                        curMin = Math.Min(curMin, Math.Min(a, b));
                    }
                    if (j > 0) {
                        long a = maxProd[i, j - 1] * val;
                        long b = minProd[i, j - 1] * val;
                        curMax = Math.Max(curMax, Math.Max(a, b));
                        curMin = Math.Min(curMin, Math.Min(a, b));
                    }

                    maxProd[i, j] = curMax;
                    minProd[i, j] = curMin;
                }
            }
        }

        long result = maxProd[m - 1, n - 1];
        if (result < 0) return -1;
        return (int)(result % MOD);
    }
}
```

## Javascript

```javascript
var maxProductPath = function(grid) {
    const MOD = 1000000007n;
    const m = grid.length, n = grid[0].length;
    const maxDP = Array.from({ length: m }, () => Array(n));
    const minDP = Array.from({ length: m }, () => Array(n));
    maxDP[0][0] = minDP[0][0] = BigInt(grid[0][0]);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            const cur = BigInt(grid[i][j]);
            let candidates = [];
            if (i > 0) {
                candidates.push(maxDP[i - 1][j] * cur);
                candidates.push(minDP[i - 1][j] * cur);
            }
            if (j > 0) {
                candidates.push(maxDP[i][j - 1] * cur);
                candidates.push(minDP[i][j - 1] * cur);
            }
            let mx = candidates[0];
            let mn = candidates[0];
            for (let k = 1; k < candidates.length; k++) {
                const v = candidates[k];
                if (v > mx) mx = v;
                if (v < mn) mn = v;
            }
            maxDP[i][j] = mx;
            minDP[i][j] = mn;
        }
    }
    const result = maxDP[m - 1][n - 1];
    if (result < 0n) return -1;
    return Number(result % MOD);
};
```

## Typescript

```typescript
function maxProductPath(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const dpMax: bigint[][] = Array.from({ length: m }, () => Array(n).fill(0n));
    const dpMin: bigint[][] = Array.from({ length: m }, () => Array(n).fill(0n));

    dpMax[0][0] = BigInt(grid[0][0]);
    dpMin[0][0] = BigInt(grid[0][0]);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            const val = BigInt(grid[i][j]);
            const candidates: bigint[] = [];

            if (i > 0) {
                candidates.push(dpMax[i - 1][j] * val);
                candidates.push(dpMin[i - 1][j] * val);
            }
            if (j > 0) {
                candidates.push(dpMax[i][j - 1] * val);
                candidates.push(dpMin[i][j - 1] * val);
            }

            let curMax = candidates[0];
            let curMin = candidates[0];
            for (let k = 1; k < candidates.length; k++) {
                const c = candidates[k];
                if (c > curMax) curMax = c;
                if (c < curMin) curMin = c;
            }
            dpMax[i][j] = curMax;
            dpMin[i][j] = curMin;
        }
    }

    const finalMax = dpMax[m - 1][n - 1];
    if (finalMax < 0n) return -1;
    const MOD = 1000000007n;
    return Number(finalMax % MOD);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxProductPath($grid) {
        $mod = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);
        $maxDP = array_fill(0, $n, 0);
        $minDP = array_fill(0, $n, 0);

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $val = $grid[$i][$j];
                if ($i === 0 && $j === 0) {
                    $maxDP[$j] = $val;
                    $minDP[$j] = $val;
                    continue;
                }

                $candidates = [];

                if ($i > 0) { // from top
                    $candidates[] = $maxDP[$j] * $val;
                    $candidates[] = $minDP[$j] * $val;
                }
                if ($j > 0) { // from left (already updated for current row)
                    $candidates[] = $maxDP[$j - 1] * $val;
                    $candidates[] = $minDP[$j - 1] * $val;
                }

                $newMax = max($candidates);
                $newMin = min($candidates);

                $maxDP[$j] = $newMax;
                $minDP[$j] = $newMin;
            }
        }

        $result = $maxDP[$n - 1];
        if ($result < 0) {
            return -1;
        }
        $result %= $mod;
        if ($result < 0) {
            $result += $mod;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maxProductPath(_ grid: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let m = grid.count
        let n = grid[0].count
        var dpMin = Array(repeating: Array(repeating: Int64(0), count: n), count: m)
        var dpMax = Array(repeating: Array(repeating: Int64(0), count: n), count: m)

        for i in 0..<m {
            for j in 0..<n {
                let val = Int64(grid[i][j])
                if i == 0 && j == 0 {
                    dpMin[i][j] = val
                    dpMax[i][j] = val
                } else {
                    var curMin = Int64.max
                    var curMax = Int64.min

                    if i > 0 {
                        let a = dpMin[i - 1][j] * val
                        let b = dpMax[i - 1][j] * val
                        curMin = min(curMin, a)
                        curMin = min(curMin, b)
                        curMax = max(curMax, a)
                        curMax = max(curMax, b)
                    }
                    if j > 0 {
                        let a = dpMin[i][j - 1] * val
                        let b = dpMax[i][j - 1] * val
                        curMin = min(curMin, a)
                        curMin = min(curMin, b)
                        curMax = max(curMax, a)
                        curMax = max(curMax, b)
                    }
                    dpMin[i][j] = curMin
                    dpMax[i][j] = curMax
                }
            }
        }

        let result = dpMax[m - 1][n - 1]
        if result < 0 {
            return -1
        } else {
            return Int(result % Int64(MOD))
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProductPath(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dpMax = Array(m) { LongArray(n) { Long.MIN_VALUE } }
        val dpMin = Array(m) { LongArray(n) { Long.MAX_VALUE } }

        dpMax[0][0] = grid[0][0].toLong()
        dpMin[0][0] = grid[0][0].toLong()

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue
                val cur = grid[i][j].toLong()
                var maxVal = Long.MIN_VALUE
                var minVal = Long.MAX_VALUE

                if (i > 0 && dpMax[i - 1][j] != Long.MIN_VALUE) {
                    val a = dpMax[i - 1][j] * cur
                    val b = dpMin[i - 1][j] * cur
                    maxVal = maxOf(maxVal, maxOf(a, b))
                    minVal = minOf(minVal, minOf(a, b))
                }
                if (j > 0 && dpMax[i][j - 1] != Long.MIN_VALUE) {
                    val a = dpMax[i][j - 1] * cur
                    val b = dpMin[i][j - 1] * cur
                    maxVal = maxOf(maxVal, maxOf(a, b))
                    minVal = minOf(minVal, minOf(a, b))
                }

                dpMax[i][j] = maxVal
                dpMin[i][j] = minVal
            }
        }

        val result = dpMax[m - 1][n - 1]
        return if (result < 0) -1 else ((result % 1_000_000_007L).toInt())
    }
}
```

## Dart

```dart
class Solution {
  int maxProductPath(List<List<int>> grid) {
    const int MOD = 1000000007;
    int m = grid.length;
    int n = grid[0].length;

    List<List<int>> maxDP = List.generate(m, (_) => List.filled(n, 0));
    List<List<int>> minDP = List.generate(m, (_) => List.filled(n, 0));

    maxDP[0][0] = grid[0][0];
    minDP[0][0] = grid[0][0];

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i == 0 && j == 0) continue;
        int cur = grid[i][j];
        List<int> candidates = [];

        if (i > 0) {
          candidates.add(maxDP[i - 1][j] * cur);
          candidates.add(minDP[i - 1][j] * cur);
        }
        if (j > 0) {
          candidates.add(maxDP[i][j - 1] * cur);
          candidates.add(minDP[i][j - 1] * cur);
        }

        int cellMax = candidates[0];
        int cellMin = candidates[0];
        for (int v in candidates) {
          if (v > cellMax) cellMax = v;
          if (v < cellMin) cellMin = v;
        }
        maxDP[i][j] = cellMax;
        minDP[i][j] = cellMin;
      }
    }

    int result = maxDP[m - 1][n - 1];
    if (result < 0) return -1;
    return result % MOD;
  }
}
```

## Golang

```go
package main

func maxProductPath(grid [][]int) int {
	const MOD int64 = 1_000_000_007
	const (
		INF_NEG = -(1 << 63)
		INF_POS = 1<<63 - 1
	)

	m, n := len(grid), len(grid[0])
	dpMax := make([][]int64, m)
	dpMin := make([][]int64, m)
	for i := 0; i < m; i++ {
		dpMax[i] = make([]int64, n)
		dpMin[i] = make([]int64, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			val := int64(grid[i][j])
			if i == 0 && j == 0 {
				dpMax[i][j] = val
				dpMin[i][j] = val
				continue
			}
			maxVal, minVal := INF_NEG, INF_POS

			if i > 0 {
				a := dpMax[i-1][j] * val
				b := dpMin[i-1][j] * val
				if a > maxVal {
					maxVal = a
				}
				if b > maxVal {
					maxVal = b
				}
				if a < minVal {
					minVal = a
				}
				if b < minVal {
					minVal = b
				}
			}
			if j > 0 {
				a := dpMax[i][j-1] * val
				b := dpMin[i][j-1] * val
				if a > maxVal {
					maxVal = a
				}
				if b > maxVal {
					maxVal = b
				}
				if a < minVal {
					minVal = a
				}
				if b < minVal {
					minVal = b
				}
			}
			dpMax[i][j] = maxVal
			dpMin[i][j] = minVal
		}
	}

	res := dpMax[m-1][n-1]
	if res < 0 {
		return -1
	}
	return int(res % MOD)
}
```

## Ruby

```ruby
def max_product_path(grid)
  m = grid.size
  n = grid[0].size
  mod = 1_000_000_007

  dp_max = Array.new(m) { Array.new(n, 0) }
  dp_min = Array.new(m) { Array.new(n, 0) }

  (0...m).each do |i|
    (0...n).each do |j|
      val = grid[i][j]
      if i == 0 && j == 0
        dp_max[i][j] = val
        dp_min[i][j] = val
      else
        candidates = []
        if i > 0
          candidates << dp_max[i - 1][j] * val
          candidates << dp_min[i - 1][j] * val
        end
        if j > 0
          candidates << dp_max[i][j - 1] * val
          candidates << dp_min[i][j - 1] * val
        end
        dp_max[i][j] = candidates.max
        dp_min[i][j] = candidates.min
      end
    end
  end

  result = dp_max[m - 1][n - 1]
  return -1 if result < 0
  result % mod
end
```

## Scala

```scala
object Solution {
  def maxProductPath(grid: Array[Array[Int]]): Int = {
    val MOD = 1000000007L
    val m = grid.length
    val n = grid(0).length
    val maxDP = Array.ofDim[Long](m, n)
    val minDP = Array.ofDim[Long](m, n)

    for (i <- 0 until m) {
      for (j <- 0 until n) {
        val cur = grid(i)(j).toLong
        if (i == 0 && j == 0) {
          maxDP(i)(j) = cur
          minDP(i)(j) = cur
        } else {
          var candMax = Long.MinValue
          var candMin = Long.MaxValue

          if (i > 0) {
            val a = maxDP(i - 1)(j) * cur
            val b = minDP(i - 1)(j) * cur
            candMax = math.max(candMax, math.max(a, b))
            candMin = math.min(candMin, math.min(a, b))
          }
          if (j > 0) {
            val a = maxDP(i)(j - 1) * cur
            val b = minDP(i)(j - 1) * cur
            candMax = math.max(candMax, math.max(a, b))
            candMin = math.min(candMin, math.min(a, b))
          }

          maxDP(i)(j) = candMax
          minDP(i)(j) = candMin
        }
      }
    }

    val result = maxDP(m - 1)(n - 1)
    if (result < 0) -1 else ((result % MOD + MOD) % MOD).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_product_path(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const MOD: i64 = 1_000_000_007;
        let mut prev: Vec<(i64, i64)> = vec![(0, 0); n];
        for i in 0..m {
            let mut cur: Vec<(i64, i64)> = vec![(0, 0); n];
            for j in 0..n {
                let v = grid[i][j] as i64;
                if i == 0 && j == 0 {
                    cur[j] = (v, v);
                } else {
                    let mut candidates: Vec<i64> = Vec::with_capacity(4);
                    if i > 0 {
                        let (tmin, tmax) = prev[j];
                        candidates.push(tmin * v);
                        candidates.push(tmax * v);
                    }
                    if j > 0 {
                        let (lmin, lmax) = cur[j - 1];
                        candidates.push(lmin * v);
                        candidates.push(lmax * v);
                    }
                    let min_val = *candidates.iter().min().unwrap();
                    let max_val = *candidates.iter().max().unwrap();
                    cur[j] = (min_val, max_val);
                }
            }
            prev = cur;
        }
        let (_, max_prod) = prev[n - 1];
        if max_prod < 0 {
            -1
        } else {
            (max_prod % MOD) as i32
        }
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (max-product-path grid)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (car grid))))
         (maxv (make-vector m))
         (minv (make-vector m)))
    ;; initialize storage vectors
    (for ([i (in-range m)])
      (vector-set! maxv i (make-vector n #f))
      (vector-set! minv i (make-vector n #f)))
    ;; dynamic programming
    (for* ([i (in-range m)]
           [j (in-range n)])
      (let ((val (list-ref (list-ref grid i) j)))
        (if (and (= i 0) (= j 0))
            (begin
              (vector-set! (vector-ref maxv i) j val)
              (vector-set! (vector-ref minv i) j val))
            (let ((products '()))
              (when (> i 0)
                (let* ((up-max (vector-ref (vector-ref maxv (- i 1)) j))
                       (up-min (vector-ref (vector-ref minv (- i 1)) j)))
                  (set! products (cons (* up-max val) products))
                  (set! products (cons (* up-min val) products))))
              (when (> j 0)
                (let* ((left-max (vector-ref (vector-ref maxv i) (- j 1)))
                       (left-min (vector-ref (vector-ref minv i) (- j 1))))
                  (set! products (cons (* left-max val) products))
                  (set! products (cons (* left-min val) products))))
              (let ((new-max (apply max products))
                    (new-min (apply min products)))
                (vector-set! (vector-ref maxv i) j new-max)
                (vector-set! (vector-ref minv i) j new-min))))))
    (let ((final-max (vector-ref (vector-ref maxv (- m 1)) (- n 1))))
      (if (< final-max 0)
          -1
          (remainder final-max MOD)))))
```

## Erlang

```erlang
-module(solution).
-export([max_product_path/1]).

-spec max_product_path(Grid :: [[integer()]]) -> integer().
max_product_path(Grid) ->
    Mod = 1000000007,
    case Grid of
        [] -> -1;
        _ ->
            N = length(hd(Grid)),
            {FinalRow, _} = lists:foldl(
                fun(RowVals, {PrevDP, RowIdx}) ->
                    CurrDP = compute_dp_row(RowVals, PrevDP, RowIdx, N),
                    {CurrDP, RowIdx + 1}
                end,
                {[], 0},
                Grid
            ),
            BottomTuple = lists:last(FinalRow),
            MaxVal = element(1, BottomTuple),
            if MaxVal < 0 -> -1;
               true -> MaxVal rem Mod
            end
    end.

%% compute DP for a single row
-spec compute_dp_row([integer()], [{integer(), integer()}], non_neg_integer(), pos_integer()) ->
          [{integer(), integer()}].
compute_dp_row(RowVals, PrevDPRow, RowIdx, N) ->
    {RevCurr, _} = lists:foldl(
        fun(ColIdx, {AccRev, PrevLeft}) ->
            Val = lists:nth(ColIdx + 1, RowVals),
            CurrTuple =
                case {RowIdx, ColIdx} of
                    {0, 0} -> {Val, Val};
                    _ ->
                        Candidates = collect_candidates(RowIdx, ColIdx, Val, PrevDPRow, PrevLeft),
                        MaxC = max_in_list(Candidates),
                        MinC = min_in_list(Candidates),
                        {MaxC, MinC}
                end,
            {[CurrTuple | AccRev], CurrTuple}
        end,
        {[], undefined},
        lists:seq(0, N - 1)
    ),
    lists:reverse(RevCurr).

%% gather possible products from top and left cells
-spec collect_candidates(non_neg_integer(), non_neg_integer(), integer(),
                         [{integer(), integer()}] | [], tuple() | undefined) -> [integer()].
collect_candidates(RowIdx, ColIdx, Val, PrevDPRow, PrevLeft) ->
    TopCandidates =
        case RowIdx > 0 of
            true ->
                {TopMax, TopMin} = lists:nth(ColIdx + 1, PrevDPRow),
                [Val * TopMax, Val * TopMin];
            false -> []
        end,
    LeftCandidates =
        case ColIdx > 0 of
            true ->
                {LeftMax, LeftMin} = PrevLeft,
                [Val * LeftMax, Val * LeftMin];
            false -> []
        end,
    TopCandidates ++ LeftCandidates.

%% maximum in a non‑empty list
-spec max_in_list([integer()]) -> integer().
max_in_list([H|T]) ->
    lists:foldl(fun(X, Acc) -> if X > Acc -> X; true -> Acc end end, H, T).

%% minimum in a non‑empty list
-spec min_in_list([integer()]) -> integer().
min_in_list([H|T]) ->
    lists:foldl(fun(X, Acc) -> if X < Acc -> X; true -> Acc end end, H, T).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_product_path(grid :: [[integer]]) :: integer
  def max_product_path(grid) do
    mod = 1_000_000_007
    m = length(grid)
    n = length(hd(grid))

    dp =
      Enum.reduce(0..(m - 1), %{}, fn i, acc ->
        Enum.reduce(0..(n - 1), acc, fn j, inner_acc ->
          val = grid |> Enum.at(i) |> Enum.at(j)

          cond do
            i == 0 and j == 0 ->
              Map.put(inner_acc, {i, j}, {val, val})

            true ->
              candidates = []

              candidates =
                if i > 0 do
                  {max_up, min_up} = Map.get(inner_acc, {i - 1, j})
                  [max_up * val, min_up * val | candidates]
                else
                  candidates
                end

              candidates =
                if j > 0 do
                  {max_left, min_left} = Map.get(inner_acc, {i, j - 1})
                  [max_left * val, min_left * val | candidates]
                else
                  candidates
                end

              max_val = Enum.max(candidates)
              min_val = Enum.min(candidates)
              Map.put(inner_acc, {i, j}, {max_val, min_val})
          end
        end)
      end)

    {final_max, _} = Map.get(dp, {m - 1, n - 1})

    if final_max < 0 do
      -1
    else
      rem(final_max, mod)
    end
  end
end
```

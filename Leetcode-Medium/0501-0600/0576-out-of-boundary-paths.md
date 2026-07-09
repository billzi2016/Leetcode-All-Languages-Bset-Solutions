# 0576. Out of Boundary Paths

## Cpp

```cpp
class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        const int MOD = 1000000007;
        if (maxMove == 0) return 0;
        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[startRow][startColumn] = 1;
        long long ans = 0;
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        for (int move = 1; move <= maxMove; ++move) {
            vector<vector<int>> ndp(m, vector<int>(n, 0));
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    int ways = dp[i][j];
                    if (!ways) continue;
                    for (auto &d : dirs) {
                        int ni = i + d[0], nj = j + d[1];
                        if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
                            ans += ways;
                            if (ans >= MOD) ans -= MOD;
                        } else {
                            ndp[ni][nj] = (ndp[ni][nj] + ways) % MOD;
                        }
                    }
                }
            }
            dp.swap(ndp);
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int[][] dp = new int[m][n];
        dp[startRow][startColumn] = 1;
        long ans = 0;
        for (int move = 0; move < maxMove; move++) {
            int[][] next = new int[m][n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    int ways = dp[i][j];
                    if (ways == 0) continue;
                    // up
                    if (i - 1 < 0) ans = (ans + ways) % MOD;
                    else next[i - 1][j] = (int)((next[i - 1][j] + ways) % MOD);
                    // down
                    if (i + 1 >= m) ans = (ans + ways) % MOD;
                    else next[i + 1][j] = (int)((next[i + 1][j] + ways) % MOD);
                    // left
                    if (j - 1 < 0) ans = (ans + ways) % MOD;
                    else next[i][j - 1] = (int)((next[i][j - 1] + ways) % MOD);
                    // right
                    if (j + 1 >= n) ans = (ans + ways) % MOD;
                    else next[i][j + 1] = (int)((next[i][j + 1] + ways) % MOD);
                }
            }
            dp = next;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if maxMove == 0:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0

        for _ in range(maxMove):
            ndp = [[0] * n for _ in range(m)]
            for i in range(m):
                row_dp_i = dp[i]
                for j in range(n):
                    cnt = row_dp_i[j]
                    if not cnt:
                        continue
                    # up
                    if i == 0:
                        result = (result + cnt) % MOD
                    else:
                        ndp[i-1][j] = (ndp[i-1][j] + cnt) % MOD
                    # down
                    if i == m - 1:
                        result = (result + cnt) % MOD
                    else:
                        ndp[i+1][j] = (ndp[i+1][j] + cnt) % MOD
                    # left
                    if j == 0:
                        result = (result + cnt) % MOD
                    else:
                        ndp[i][j-1] = (ndp[i][j-1] + cnt) % MOD
                    # right
                    if j == n - 1:
                        result = (result + cnt) % MOD
                    else:
                        ndp[i][j+1] = (ndp[i][j+1] + cnt) % MOD
            dp = ndp

        return result % MOD
```

## Python3

```python
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        ans = 0
        for _ in range(maxMove):
            ndp = [[0] * n for _ in range(m)]
            for i in range(m):
                row = dp[i]
                for j in range(n):
                    cur = row[j]
                    if not cur:
                        continue
                    # up
                    if i == 0:
                        ans = (ans + cur) % MOD
                    else:
                        ndp[i - 1][j] = (ndp[i - 1][j] + cur) % MOD
                    # down
                    if i == m - 1:
                        ans = (ans + cur) % MOD
                    else:
                        ndp[i + 1][j] = (ndp[i + 1][j] + cur) % MOD
                    # left
                    if j == 0:
                        ans = (ans + cur) % MOD
                    else:
                        ndp[i][j - 1] = (ndp[i][j - 1] + cur) % MOD
                    # right
                    if j == n - 1:
                        ans = (ans + cur) % MOD
                    else:
                        ndp[i][j + 1] = (ndp[i][j + 1] + cur) % MOD
            dp = ndp
        return ans % MOD
```

## C

```c
#include <stdint.h>

int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
    const int MOD = 1000000007;
    if (maxMove == 0) return 0;

    static int64_t dp[55][55];
    static int64_t ndp[55][55];

    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            dp[i][j] = 0;
    dp[startRow][startColumn] = 1;

    int64_t result = 0;
    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    for (int move = 0; move < maxMove; ++move) {
        // reset ndp
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                ndp[i][j] = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int64_t cur = dp[i][j];
                if (!cur) continue;
                // count exits from this cell
                if (i == 0) result = (result + cur) % MOD;
                if (i == m - 1) result = (result + cur) % MOD;
                if (j == 0) result = (result + cur) % MOD;
                if (j == n - 1) result = (result + cur) % MOD;

                // propagate to neighbors inside grid
                for (int d = 0; d < 4; ++d) {
                    int ni = i + dirs[d][0];
                    int nj = j + dirs[d][1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                        ndp[ni][nj] += cur;
                        if (ndp[ni][nj] >= MOD) ndp[ni][nj] %= MOD;
                    }
                }
            }
        }

        // copy back
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                dp[i][j] = ndp[i][j];
    }

    return (int)(result % MOD);
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;

    public int FindPaths(int m, int n, int maxMove, int startRow, int startColumn)
    {
        long result = 0;
        int[,] dp = new int[m, n];
        dp[startRow, startColumn] = 1;

        int[] dr = { -1, 1, 0, 0 };
        int[] dc = { 0, 0, -1, 1 };

        for (int move = 0; move < maxMove; ++move)
        {
            int[,] next = new int[m, n];
            for (int i = 0; i < m; ++i)
            {
                for (int j = 0; j < n; ++j)
                {
                    int ways = dp[i, j];
                    if (ways == 0) continue;

                    for (int d = 0; d < 4; ++d)
                    {
                        int ni = i + dr[d];
                        int nj = j + dc[d];

                        if (ni < 0 || ni >= m || nj < 0 || nj >= n)
                        {
                            result = (result + ways) % MOD;
                        }
                        else
                        {
                            next[ni, nj] = (int)((next[ni, nj] + (long)ways) % MOD);
                        }
                    }
                }
            }
            dp = next;
        }

        return (int)(result % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} maxMove
 * @param {number} startRow
 * @param {number} startColumn
 * @return {number}
 */
var findPaths = function(m, n, maxMove, startRow, startColumn) {
    const MOD = 1000000007;
    let dp = Array.from({ length: m }, () => Array(n).fill(0));
    dp[startRow][startColumn] = 1;
    let ans = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    for (let move = 0; move < maxMove; move++) {
        const ndp = Array.from({ length: m }, () => Array(n).fill(0));
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                const cur = dp[i][j];
                if (!cur) continue;
                for (const [dx, dy] of dirs) {
                    const ni = i + dx, nj = j + dy;
                    if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
                        ans = (ans + cur) % MOD;
                    } else {
                        ndp[ni][nj] = (ndp[ni][nj] + cur) % MOD;
                    }
                }
            }
        }
        dp = ndp;
    }
    
    return ans;
};
```

## Typescript

```typescript
function findPaths(m: number, n: number, maxMove: number, startRow: number, startColumn: number): number {
    const MOD = 1000000007;
    let dp: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    dp[startRow][startColumn] = 1;
    let ans = 0;

    const dirs = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ];

    for (let move = 0; move < maxMove; move++) {
        const ndp: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                const cur = dp[i][j];
                if (cur === 0) continue;
                for (const [dx, dy] of dirs) {
                    const ni = i + dx;
                    const nj = j + dy;
                    if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
                        ans = (ans + cur) % MOD;
                    } else {
                        ndp[ni][nj] = (ndp[ni][nj] + cur) % MOD;
                    }
                }
            }
        }
        dp = ndp;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer $maxMove
     * @param Integer $startRow
     * @param Integer $startColumn
     * @return Integer
     */
    function findPaths($m, $n, $maxMove, $startRow, $startColumn) {
        $mod = 1000000007;
        // Initialize dp grid
        $dp = [];
        for ($i = 0; $i < $m; $i++) {
            $dp[$i] = array_fill(0, $n, 0);
        }
        $dp[$startRow][$startColumn] = 1;

        $ans = 0;
        // Directions: up, down, left, right
        for ($move = 1; $move <= $maxMove; $move++) {
            $temp = [];
            for ($i = 0; $i < $m; $i++) {
                $temp[$i] = array_fill(0, $n, 0);
            }

            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    $cnt = $dp[$i][$j];
                    if ($cnt == 0) continue;

                    // Up
                    if ($i - 1 < 0) {
                        $ans = ($ans + $cnt) % $mod;
                    } else {
                        $temp[$i - 1][$j] = ($temp[$i - 1][$j] + $cnt) % $mod;
                    }
                    // Down
                    if ($i + 1 >= $m) {
                        $ans = ($ans + $cnt) % $mod;
                    } else {
                        $temp[$i + 1][$j] = ($temp[$i + 1][$j] + $cnt) % $mod;
                    }
                    // Left
                    if ($j - 1 < 0) {
                        $ans = ($ans + $cnt) % $mod;
                    } else {
                        $temp[$i][$j - 1] = ($temp[$i][$j - 1] + $cnt) % $mod;
                    }
                    // Right
                    if ($j + 1 >= $n) {
                        $ans = ($ans + $cnt) % $mod;
                    } else {
                        $temp[$i][$j + 1] = ($temp[$i][$j + 1] + $cnt) % $mod;
                    }
                }
            }

            $dp = $temp;
        }

        return $ans % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func findPaths(_ m: Int, _ n: Int, _ maxMove: Int, _ startRow: Int, _ startColumn: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: n), count: m)
        dp[startRow][startColumn] = 1
        var result = 0
        
        for _ in 0..<maxMove {
            var newDP = Array(repeating: Array(repeating: 0, count: n), count: m)
            for i in 0..<m {
                for j in 0..<n {
                    let val = dp[i][j]
                    if val == 0 { continue }
                    
                    // up
                    if i == 0 {
                        result = (result + val) % MOD
                    } else {
                        newDP[i - 1][j] = (newDP[i - 1][j] + val) % MOD
                    }
                    // down
                    if i == m - 1 {
                        result = (result + val) % MOD
                    } else {
                        newDP[i + 1][j] = (newDP[i + 1][j] + val) % MOD
                    }
                    // left
                    if j == 0 {
                        result = (result + val) % MOD
                    } else {
                        newDP[i][j - 1] = (newDP[i][j - 1] + val) % MOD
                    }
                    // right
                    if j == n - 1 {
                        result = (result + val) % MOD
                    } else {
                        newDP[i][j + 1] = (newDP[i][j + 1] + val) % MOD
                    }
                }
            }
            dp = newDP
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPaths(m: Int, n: Int, maxMove: Int, startRow: Int, startColumn: Int): Int {
        val MOD = 1_000_000_007L
        var dp = Array(m) { LongArray(n) }
        dp[startRow][startColumn] = 1L
        var result = 0L

        for (move in 1..maxMove) {
            val ndp = Array(m) { LongArray(n) }
            for (i in 0 until m) {
                for (j in 0 until n) {
                    val cur = dp[i][j]
                    if (cur == 0L) continue
                    // up
                    if (i - 1 < 0) {
                        result += cur
                    } else {
                        ndp[i - 1][j] = (ndp[i - 1][j] + cur) % MOD
                    }
                    // down
                    if (i + 1 >= m) {
                        result += cur
                    } else {
                        ndp[i + 1][j] = (ndp[i + 1][j] + cur) % MOD
                    }
                    // left
                    if (j - 1 < 0) {
                        result += cur
                    } else {
                        ndp[i][j - 1] = (ndp[i][j - 1] + cur) % MOD
                    }
                    // right
                    if (j + 1 >= n) {
                        result += cur
                    } else {
                        ndp[i][j + 1] = (ndp[i][j + 1] + cur) % MOD
                    }
                }
            }
            result %= MOD
            dp = ndp
        }

        return (result % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
    const int MOD = 1000000007;
    List<List<int>> dp = List.generate(m, (_) => List.filled(n, 0));
    dp[startRow][startColumn] = 1;
    int ans = 0;

    for (int move = 0; move < maxMove; ++move) {
      List<List<int>> ndp = List.generate(m, (_) => List.filled(n, 0));
      for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
          int cur = dp[i][j];
          if (cur == 0) continue;

          // up
          if (i - 1 < 0) {
            ans += cur;
            if (ans >= MOD) ans -= MOD;
          } else {
            ndp[i - 1][j] = (ndp[i - 1][j] + cur) % MOD;
          }

          // down
          if (i + 1 >= m) {
            ans += cur;
            if (ans >= MOD) ans -= MOD;
          } else {
            ndp[i + 1][j] = (ndp[i + 1][j] + cur) % MOD;
          }

          // left
          if (j - 1 < 0) {
            ans += cur;
            if (ans >= MOD) ans -= MOD;
          } else {
            ndp[i][j - 1] = (ndp[i][j - 1] + cur) % MOD;
          }

          // right
          if (j + 1 >= n) {
            ans += cur;
            if (ans >= MOD) ans -= MOD;
          } else {
            ndp[i][j + 1] = (ndp[i][j + 1] + cur) % MOD;
          }
        }
      }
      dp = ndp;
    }

    return ans % MOD;
  }
}
```

## Golang

```go
func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
	const MOD = 1000000007
	if maxMove == 0 {
		return 0
	}
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dp[startRow][startColumn] = 1

	dirs := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	result := 0

	for move := 0; move < maxMove; move++ {
		ndp := make([][]int, m)
		for i := range ndp {
			ndp[i] = make([]int, n)
		}
		for i := 0; i < m; i++ {
			for j := 0; j < n; j++ {
				if dp[i][j] == 0 {
					continue
				}
				val := dp[i][j]
				for _, d := range dirs {
					ni, nj := i+d[0], j+d[1]
					if ni < 0 || ni >= m || nj < 0 || nj >= n {
						result += val
						if result >= MOD {
							result -= MOD
						}
					} else {
						ndp[ni][nj] += val
						if ndp[ni][nj] >= MOD {
							ndp[ni][nj] -= MOD
						}
					}
				}
			}
		}
		dp = ndp
	}
	return result % MOD
}
```

## Ruby

```ruby
MOD = 1_000_000_007

# @param {Integer} m
# @param {Integer} n
# @param {Integer} max_move
# @param {Integer} start_row
# @param {Integer} start_column
# @return {Integer}
def find_paths(m, n, max_move, start_row, start_column)
  dp = Array.new(m) { Array.new(n, 0) }
  dp[start_row][start_column] = 1
  ans = 0
  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

  (1..max_move).each do |_|
    nxt = Array.new(m) { Array.new(n, 0) }
    m.times do |i|
      n.times do |j|
        cur = dp[i][j]
        next if cur == 0
        dirs.each do |dx, dy|
          ni = i + dx
          nj = j + dy
          if ni < 0 || ni >= m || nj < 0 || nj >= n
            ans += cur
            ans -= MOD if ans >= MOD
          else
            nxt[ni][nj] += cur
            nxt[ni][nj] -= MOD if nxt[ni][nj] >= MOD
          end
        end
      end
    end
    dp = nxt
  end

  ans % MOD
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007

    def findPaths(m: Int, n: Int, maxMove: Int, startRow: Int, startColumn: Int): Int = {
        var cur = Array.ofDim[Int](m, n)
        cur(startRow)(startColumn) = 1
        var result: Long = 0L

        val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))

        for (_ <- 1 to maxMove) {
            val nxt = Array.ofDim[Int](m, n)
            var i = 0
            while (i < m) {
                var j = 0
                while (j < n) {
                    val ways = cur(i)(j)
                    if (ways != 0) {
                        var d = 0
                        while (d < 4) {
                            val ni = i + dirs(d)._1
                            val nj = j + dirs(d)._2
                            if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
                                result += ways
                                if (result >= MOD) result -= MOD
                            } else {
                                val sum = nxt(ni)(nj).toLong + ways
                                nxt(ni)(nj) = (sum % MOD).toInt
                            }
                            d += 1
                        }
                    }
                    j += 1
                }
                i += 1
            }
            cur = nxt
        }

        (result % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m_usize = m as usize;
        let n_usize = n as usize;

        let mut cur = vec![vec![0i64; n_usize]; m_usize];
        cur[start_row as usize][start_column as usize] = 1;

        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        let mut ans: i64 = 0;

        for _ in 0..max_move {
            let mut next = vec![vec![0i64; n_usize]; m_usize];
            for i in 0..m_usize {
                for j in 0..n_usize {
                    let val = cur[i][j];
                    if val == 0 {
                        continue;
                    }
                    for &(dx, dy) in &dirs {
                        let ni = i as i32 + dx;
                        let nj = j as i32 + dy;
                        if ni < 0 || ni >= m || nj < 0 || nj >= n {
                            ans += val;
                            if ans >= MOD {
                                ans -= MOD;
                            }
                        } else {
                            let entry = &mut next[ni as usize][nj as usize];
                            *entry += val;
                            if *entry >= MOD {
                                *entry -= MOD;
                            }
                        }
                    }
                }
            }
            cur = next;
        }

        (ans % MOD) as i32
    }
}
```

## Racket

```racket
(define/contract (find-paths m n maxMove startRow startColumn)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((MOD 1000000007)
         (dp (make-vector m (lambda (_) (make-vector n 0))))
         (_ (vector-set! (vector-ref dp startRow) startColumn 1))
         (ans 0))
    (for ([step (in-range maxMove)])
      (let ((newdp (make-vector m (lambda (_) (make-vector n 0)))))
        (for ([i (in-range m)])
          (let ((row (vector-ref dp i)))
            (for ([j (in-range n)])
              (let ((ways (vector-ref row j)))
                (when (> ways 0)
                  (for ([dir '((-1 . 0) (1 . 0) (0 . -1) (0 . 1))])
                    (define di (car dir))
                    (define dj (cdr dir))
                    (let ((ni (+ i di))
                          (nj (+ j dj)))
                      (if (or (< ni 0) (>= ni m) (< nj 0) (>= nj n))
                          (set! ans (modulo (+ ans ways) MOD))
                          (let* ((row2 (vector-ref newdp ni))
                                 (old (vector-ref row2 nj))
                                 (newval (modulo (+ old ways) MOD)))
                            (vector-set! row2 nj newval))))))))))
        (set! dp newdp))
    ans)))
```

## Erlang

```erlang
-define(MOD, 1000000007).

find_paths(M, N, MaxMove, StartRow, StartColumn) ->
    case MaxMove of
        0 -> 0;
        _ ->
            DP0 = init_dp(M, N, StartRow, StartColumn),
            loop(1, MaxMove, DP0, 0, M, N)
    end.

init_dp(M, N, SR, SC) ->
    [ [ if I =:= SR andalso J =:= SC -> 1; true -> 0 end
        || J <- lists:seq(0, N-1) ]
      || I <- lists:seq(0, M-1) ].

loop(Move, MaxMove, DPPrev, Acc, M, N) when Move =< MaxMove ->
    Contrib = contribution(DPPrev, M, N, 0),
    NewAcc = (Acc + Contrib) rem ?MOD,
    NewDP = next_dp(DPPrev, M, N),
    case Move of
        MaxMove -> NewAcc;
        _ -> loop(Move + 1, MaxMove, NewDP, NewAcc, M, N)
    end.

contribution(DPRows, M, N, Acc) ->
    contribution_rows(DPRows, 0, M, N, Acc).

contribution_rows([], _I, _M, _N, Acc) -> Acc;
contribution_rows([Row|Rest], I, M, N, Acc) ->
    NewAcc = contribution_row(Row, I, 0, M, N, Acc),
    contribution_rows(Rest, I + 1, M, N, NewAcc).

contribution_row([], _I, _J, _M, _N, Acc) -> Acc;
contribution_row([V|Rest], I, J, M, N, Acc) ->
    A1 = case I of
        0 -> (Acc + V) rem ?MOD;
        _ -> Acc
    end,
    A2 = case I of
        M-1 -> (A1 + V) rem ?MOD;
        _ -> A1
    end,
    A3 = case J of
        0 -> (A2 + V) rem ?MOD;
        _ -> A2
    end,
    A4 = case J of
        N-1 -> (A3 + V) rem ?MOD;
        _ -> A3
    end,
    contribution_row(Rest, I, J + 1, M, N, A4).

next_dp(DPPrev, M, N) ->
    [ [ calc_cell(I, J, DPPrev, M, N) || J <- lists:seq(0, N-1) ]
      || I <- lists:seq(0, M-1) ].

calc_cell(I, J, DPPrev, M, N) ->
    S0 = 0,
    S1 = if I > 0 -> (S0 + get(DPPrev, I - 1, J)) rem ?MOD; true -> S0 end,
    S2 = if I < M - 1 -> (S1 + get(DPPrev, I + 1, J)) rem ?MOD; true -> S1 end,
    S3 = if J > 0 -> (S2 + get(DPPrev, I, J - 1)) rem ?MOD; true -> S2 end,
    S4 = if J < N - 1 -> (S3 + get(DPPrev, I, J + 1)) rem ?MOD; true -> S3 end,
    S4.

get(DP, I, J) ->
    Row = lists:nth(I + 1, DP),
    lists:nth(J + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec find_paths(m :: integer, n :: integer, max_move :: integer, start_row :: integer, start_column :: integer) :: integer
  def find_paths(m, n, max_move, start_row, start_column) do
    dp = %{{start_row, start_column} => 1}
    dfs(1, max_move, m, n, dp, 0)
  end

  defp dfs(step, max_move, _m, _n, _dp, ans) when step > max_move, do: ans

  defp dfs(step, max_move, m, n, dp, ans) do
    {new_dp, new_ans} =
      Enum.reduce(dp, {%{}, ans}, fn {{i, j}, cnt}, {acc_dp, acc_ans} ->
        dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]
        Enum.reduce(dirs, {acc_dp, acc_ans}, fn {di, dj}, {inner_dp, inner_ans} ->
          ni = i + di
          nj = j + dj

          if ni < 0 or ni >= m or nj < 0 or nj >= n do
            {inner_dp, rem(inner_ans + cnt, @mod)}
          else
            key = {ni, nj}
            updated_inner_dp = Map.update(inner_dp, key, cnt, fn existing -> rem(existing + cnt, @mod) end)
            {updated_inner_dp, inner_ans}
          end
        end)
      end)

    dfs(step + 1, max_move, m, n, new_dp, new_ans)
  end
end
```

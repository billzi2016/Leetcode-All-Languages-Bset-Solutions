# 1444. Number of Ways of Cutting a Pizza

## Cpp

```cpp
class Solution {
public:
    int ways(vector<string>& pizza, int k) {
        const int MOD = 1'000'000'007;
        int n = pizza.size();
        int m = pizza[0].size();
        // suffix sum of apples
        vector<vector<int>> apple(n + 1, vector<int>(m + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                apple[i][j] = (pizza[i][j] == 'A') + apple[i + 1][j] + apple[i][j + 1] - apple[i + 1][j + 1];
            }
        }
        // dp[row][col][cuts]
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(k + 1, 0)));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (apple[i][j] > 0) dp[i][j][1] = 1;
            }
        }
        for (int cuts = 2; cuts <= k; ++cuts) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    if (apple[i][j] == 0) continue;
                    long long ways = 0;
                    // horizontal cuts
                    for (int r = i + 1; r < n; ++r) {
                        if (apple[i][j] - apple[r][j] > 0) { // top piece has an apple
                            ways += dp[r][j][cuts - 1];
                        }
                    }
                    // vertical cuts
                    for (int c = j + 1; c < m; ++c) {
                        if (apple[i][j] - apple[i][c] > 0) { // left piece has an apple
                            ways += dp[i][c][cuts - 1];
                        }
                    }
                    dp[i][j][cuts] = ways % MOD;
                }
            }
        }
        return dp[0][0][k];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int ways(String[] pizza, int k) {
        int rows = pizza.length;
        int cols = pizza[0].length();
        
        // suffix sum of apples
        int[][] apple = new int[rows + 1][cols + 1];
        for (int i = rows - 1; i >= 0; --i) {
            for (int j = cols - 1; j >= 0; --j) {
                apple[i][j] = (pizza[i].charAt(j) == 'A' ? 1 : 0)
                        + apple[i + 1][j] + apple[i][j + 1] - apple[i + 1][j + 1];
            }
        }
        
        int[][][] dp = new int[k + 1][rows][cols];
        // base: one piece
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                dp[1][i][j] = apple[i][j] > 0 ? 1 : 0;
            }
        }
        
        for (int pieces = 2; pieces <= k; ++pieces) {
            for (int i = rows - 1; i >= 0; --i) {
                for (int j = cols - 1; j >= 0; --j) {
                    long ways = 0;
                    // horizontal cuts
                    for (int r = i + 1; r < rows; ++r) {
                        if (apple[i][j] - apple[r][j] > 0) { // top part has an apple
                            ways += dp[pieces - 1][r][j];
                        }
                    }
                    // vertical cuts
                    for (int c = j + 1; c < cols; ++c) {
                        if (apple[i][j] - apple[i][c] > 0) { // left part has an apple
                            ways += dp[pieces - 1][i][c];
                        }
                    }
                    dp[pieces][i][j] = (int)(ways % MOD);
                }
            }
        }
        
        return dp[k][0][0];
    }
}
```

## Python

```python
class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        R, C = len(pizza), len(pizza[0])
        # suffix sum of apples from (i,j) to bottom-right
        pre = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                pre[i][j] = (1 if pizza[i][j] == 'A' else 0) + pre[i + 1][j] + pre[i][j + 1] - pre[i + 1][j + 1]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j, cuts):
            # cuts = number of pieces we still need (including current piece)
            if pre[i][j] == 0:
                return 0
            if cuts == 1:
                return 1
            ans = 0
            # horizontal cut
            for row in range(i + 1, R):
                if pre[i][j] - pre[row][j] > 0:  # top part has at least one apple
                    ans += dp(row, j, cuts - 1)
            # vertical cut
            for col in range(j + 1, C):
                if pre[i][j] - pre[i][col] > 0:  # left part has at least one apple
                    ans += dp(i, col, cuts - 1)
            return ans % MOD

        return dp(0, 0, k) % MOD
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        # suffix sum of apples from (i,j) to bottom-right
        suff = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                suff[i][j] = (pizza[i][j] == 'A') + suff[i + 1][j] + suff[i][j + 1] - suff[i + 1][j + 1]

        @lru_cache(None)
        def dfs(r: int, c: int, pieces: int) -> int:
            if suff[r][c] == 0:
                return 0
            if pieces == 1:
                return 1
            ans = 0
            # horizontal cuts
            for nr in range(r + 1, rows):
                if suff[r][c] - suff[nr][c] > 0:   # top part has at least one apple
                    ans += dfs(nr, c, pieces - 1)
            # vertical cuts
            for nc in range(c + 1, cols):
                if suff[r][c] - suff[r][nc] > 0:   # left part has at least one apple
                    ans += dfs(r, nc, pieces - 1)
            return ans % MOD

        return dfs(0, 0, k)
```

## C

```c
#include <string.h>
#include <stdlib.h>

#define MOD 1000000007

static int rows, cols;
static int suffix[55][55];
static int dp[55][55][11];

int dfs(int r, int c, int cuts) {
    if (suffix[r][c] == 0) return 0;          // no apple in current piece
    if (cuts == 1) return 1;                  // last piece, valid

    int *memo = &dp[r][c][cuts];
    if (*memo != -1) return *memo;

    long ans = 0;
    // horizontal cuts
    for (int nr = r + 1; nr < rows; ++nr) {
        if (suffix[r][c] - suffix[nr][c] > 0) {   // upper part has an apple
            ans += dfs(nr, c, cuts - 1);
        }
    }
    // vertical cuts
    for (int nc = c + 1; nc < cols; ++nc) {
        if (suffix[r][c] - suffix[r][nc] > 0) {   // left part has an apple
            ans += dfs(r, nc, cuts - 1);
        }
    }

    ans %= MOD;
    *memo = (int)ans;
    return *memo;
}

int ways(char** pizza, int pizzaSize, int k) {
    rows = pizzaSize;
    cols = strlen(pizza[0]);

    // compute suffix sum of apples
    for (int i = 0; i <= rows; ++i)
        for (int j = 0; j <= cols; ++j)
            suffix[i][j] = 0;

    for (int i = rows - 1; i >= 0; --i) {
        for (int j = cols - 1; j >= 0; --j) {
            suffix[i][j] = (pizza[i][j] == 'A') +
                           suffix[i + 1][j] + suffix[i][j + 1] -
                           suffix[i + 1][j + 1];
        }
    }

    memset(dp, -1, sizeof(dp));
    return dfs(0, 0, k);
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1_000_000_007;
    public int Ways(string[] pizza, int k) {
        int rows = pizza.Length;
        int cols = pizza[0].Length;

        // suffix sum of apples: suff[i,j] = apples in submatrix (i,j) to bottom-right
        int[,] suff = new int[rows + 1, cols + 1];
        for (int i = rows - 1; i >= 0; i--) {
            for (int j = cols - 1; j >= 0; j--) {
                suff[i, j] = (pizza[i][j] == 'A' ? 1 : 0)
                             + suff[i + 1, j]
                             + suff[i, j + 1]
                             - suff[i + 1, j + 1];
            }
        }

        int[,,] memo = new int[rows, cols, k];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                for (int t = 0; t < k; t++)
                    memo[i, j, t] = -1;

        int Dfs(int r, int c, int cuts) {
            if (suff[r, c] == 0) return 0;
            if (cuts == 0) return 1;
            if (memo[r, c, cuts] != -1) return memo[r, c, cuts];

            long ans = 0;

            // horizontal cuts
            for (int nr = r + 1; nr < rows; nr++) {
                if (suff[r, c] - suff[nr, c] > 0) {
                    ans += Dfs(nr, c, cuts - 1);
                }
            }

            // vertical cuts
            for (int nc = c + 1; nc < cols; nc++) {
                if (suff[r, c] - suff[r, nc] > 0) {
                    ans += Dfs(r, nc, cuts - 1);
                }
            }

            memo[r, c, cuts] = (int)(ans % MOD);
            return memo[r, c, cuts];
        }

        return Dfs(0, 0, k - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} pizza
 * @param {number} k
 * @return {number}
 */
var ways = function(pizza, k) {
    const MOD = 1000000007;
    const rows = pizza.length;
    const cols = pizza[0].length;

    // prefix sum of apples (suffix style not needed)
    const ps = Array.from({ length: rows + 1 }, () => new Uint16Array(cols + 1));
    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            const val = pizza[i][j] === 'A' ? 1 : 0;
            ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + val;
        }
    }

    function hasApple(r1, c1, r2, c2) {
        const cnt = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
        return cnt > 0;
    }

    const dp = Array.from({ length: rows }, () =>
        Array.from({ length: cols }, () => new Int32Array(k + 1).fill(-1))
    );

    function dfs(r, c, remain) {
        if (!hasApple(r, c, rows - 1, cols - 1)) return 0;
        if (remain === 1) return 1;
        const memo = dp[r][c][remain];
        if (memo !== -1) return memo;

        let ans = 0;
        // horizontal cuts
        for (let nr = r + 1; nr < rows; ++nr) {
            if (hasApple(r, c, nr - 1, cols - 1)) {
                ans = (ans + dfs(nr, c, remain - 1)) % MOD;
            }
        }
        // vertical cuts
        for (let nc = c + 1; nc < cols; ++nc) {
            if (hasApple(r, c, rows - 1, nc - 1)) {
                ans = (ans + dfs(r, nc, remain - 1)) % MOD;
            }
        }

        dp[r][c][remain] = ans;
        return ans;
    }

    return dfs(0, 0, k);
};
```

## Typescript

```typescript
function ways(pizza: string[], k: number): number {
    const MOD = 1_000_000_007;
    const rows = pizza.length;
    const cols = pizza[0].length;

    // suffix sum of apples
    const apples: number[][] = Array.from({ length: rows + 1 }, () => new Array(cols + 1).fill(0));
    for (let i = rows - 1; i >= 0; i--) {
        for (let j = cols - 1; j >= 0; j--) {
            apples[i][j] =
                (pizza[i][j] === 'A' ? 1 : 0) +
                apples[i + 1][j] +
                apples[i][j + 1] -
                apples[i + 1][j + 1];
        }
    }

    const memo: number[][][] = Array.from({ length: rows }, () =>
        Array.from({ length: cols }, () => new Array(k).fill(-1))
    );

    function dfs(r: number, c: number, cuts: number): number {
        if (apples[r][c] === 0) return 0;
        if (cuts === 0) return 1;
        const cached = memo[r][c][cuts];
        if (cached !== -1) return cached;

        let ans = 0;

        // horizontal cuts
        for (let nr = r + 1; nr < rows; nr++) {
            if (apples[r][c] - apples[nr][c] > 0) {
                ans = (ans + dfs(nr, c, cuts - 1)) % MOD;
            }
        }

        // vertical cuts
        for (let nc = c + 1; nc < cols; nc++) {
            if (apples[r][c] - apples[r][nc] > 0) {
                ans = (ans + dfs(r, nc, cuts - 1)) % MOD;
            }
        }

        memo[r][c][cuts] = ans;
        return ans;
    }

    return dfs(0, 0, k - 1);
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $pizza
     * @param Integer $k
     * @return Integer
     */
    function ways($pizza, $k) {
        $mod = 1000000007;
        $rows = count($pizza);
        $cols = strlen($pizza[0]);

        // suffix sum of apples from (i,j) to bottom-right
        $pre = array_fill(0, $rows + 1, array_fill(0, $cols + 1, 0));
        for ($i = $rows - 1; $i >= 0; --$i) {
            for ($j = $cols - 1; $j >= 0; --$j) {
                $apple = ($pizza[$i][$j] === 'A') ? 1 : 0;
                $pre[$i][$j] = $apple + $pre[$i + 1][$j] + $pre[$i][$j + 1] - $pre[$i + 1][$j + 1];
            }
        }

        $memo = [];

        $dfs = function($r, $c, $cuts) use (&$dfs, &$pre, $rows, $cols, $mod, &$memo) {
            if ($pre[$r][$c] == 0) {
                return 0;
            }
            if ($cuts == 0) {
                return 1;
            }
            if (isset($memo[$r][$c][$cuts])) {
                return $memo[$r][$c][$cuts];
            }

            $ways = 0;

            // horizontal cuts
            for ($nr = $r + 1; $nr < $rows; ++$nr) {
                if ($pre[$r][$c] - $pre[$nr][$c] > 0) {
                    $ways = ($ways + $dfs($nr, $c, $cuts - 1)) % $mod;
                }
            }

            // vertical cuts
            for ($nc = $c + 1; $nc < $cols; ++$nc) {
                if ($pre[$r][$c] - $pre[$r][$nc] > 0) {
                    $ways = ($ways + $dfs($r, $nc, $cuts - 1)) % $mod;
                }
            }

            $memo[$r][$c][$cuts] = $ways;
            return $ways;
        };

        return $dfs(0, 0, $k - 1);
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007
    private var rows: Int = 0
    private var cols: Int = 0
    private var suffix: [[Int]] = []
    private var memo: [[[Int]]] = []

    func ways(_ pizza: [String], _ k: Int) -> Int {
        rows = pizza.count
        cols = pizza[0].count

        // suffix[i][j] = number of apples in submatrix (i,j) to bottom-right inclusive
        suffix = Array(repeating: Array(repeating: 0, count: cols + 1), repeatCount: rows + 1)
        for i in stride(from: rows - 1, through: 0, by: -1) {
            let line = Array(pizza[i])
            for j in stride(from: cols - 1, through: 0, by: -1) {
                let add = (line[j] == "A") ? 1 : 0
                suffix[i][j] = add + suffix[i + 1][j] + suffix[i][j + 1] - suffix[i + 1][j + 1]
            }
        }

        // memo[row][col][pieces] = ways, initialize with -1
        memo = Array(repeating: Array(repeating: Array(repeating: -1, count: k + 1), count: cols), repeatCount: rows)

        return dfs(0, 0, k)
    }

    private func hasApple(_ r: Int, _ c: Int) -> Bool {
        return suffix[r][c] > 0
    }

    private func dfs(_ r: Int, _ c: Int, _ pieces: Int) -> Int {
        if !hasApple(r, c) { return 0 }
        if pieces == 1 { return 1 }
        if memo[r][c][pieces] != -1 { return memo[r][c][pieces] }

        var ans = 0

        // horizontal cuts
        for nr in (r + 1)..<rows {
            // apples in top part (r..nr-1, c..end)
            if suffix[r][c] - suffix[nr][c] > 0 {
                ans = (ans + dfs(nr, c, pieces - 1)) % MOD
            }
        }

        // vertical cuts
        for nc in (c + 1)..<cols {
            // apples in left part (r..end, c..nc-1)
            if suffix[r][c] - suffix[r][nc] > 0 {
                ans = (ans + dfs(r, nc, pieces - 1)) % MOD
            }
        }

        memo[r][c][pieces] = ans
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007
    private lateinit var apples: Array<IntArray>
    private lateinit var dp: Array<Array<IntArray>>
    private var rows = 0
    private var cols = 0

    fun ways(pizza: Array<String>, k: Int): Int {
        rows = pizza.size
        cols = pizza[0].length
        // suffix sum of apples
        apples = Array(rows + 1) { IntArray(cols + 1) }
        for (i in rows - 1 downTo 0) {
            for (j in cols - 1 downTo 0) {
                val add = if (pizza[i][j] == 'A') 1 else 0
                apples[i][j] = add + apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]
            }
        }
        dp = Array(rows) { Array(cols) { IntArray(k) { -1 } } }
        return dfs(0, 0, k - 1)
    }

    private fun dfs(r: Int, c: Int, cuts: Int): Int {
        if (apples[r][c] == 0) return 0
        if (cuts == 0) return 1
        val cached = dp[r][c][cuts]
        if (cached != -1) return cached

        var res = 0L
        // horizontal cuts
        for (nr in r + 1 until rows) {
            if (apples[r][c] - apples[nr][c] > 0) {
                res += dfs(nr, c, cuts - 1)
            }
        }
        // vertical cuts
        for (nc in c + 1 until cols) {
            if (apples[r][c] - apples[r][nc] > 0) {
                res += dfs(r, nc, cuts - 1)
            }
        }

        val ans = (res % MOD).toInt()
        dp[r][c][cuts] = ans
        return ans
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;
  late List<List<int>> _suffix;
  late List<List<List<int>>> _memo;
  late int _rows, _cols;

  int ways(List<String> pizza, int k) {
    _rows = pizza.length;
    _cols = pizza[0].length;
    _suffix = List.generate(_rows, (_) => List.filled(_cols, 0));

    // compute suffix sum of apples
    for (int i = _rows - 1; i >= 0; --i) {
      for (int j = _cols - 1; j >= 0; --j) {
        int cur = pizza[i][j] == 'A' ? 1 : 0;
        int down = i + 1 < _rows ? _suffix[i + 1][j] : 0;
        int right = j + 1 < _cols ? _suffix[i][j + 1] : 0;
        int diag = (i + 1 < _rows && j + 1 < _cols) ? _suffix[i + 1][j + 1] : 0;
        _suffix[i][j] = cur + down + right - diag;
      }
    }

    // memo[row][col][cutsRemaining]
    _memo = List.generate(
        _rows, (_) => List.generate(_cols, (_) => List.filled(k, -1)));
    return _dfs(0, 0, k - 1);
  }

  int _dfs(int r, int c, int cuts) {
    if (_suffix[r][c] == 0) return 0;
    if (cuts == 0) return 1;
    if (_memo[r][c][cuts] != -1) return _memo[r][c][cuts];

    int res = 0;

    // horizontal cuts
    for (int nr = r + 1; nr < _rows; ++nr) {
      if (_suffix[r][c] - _suffix[nr][c] > 0) {
        res = (res + _dfs(nr, c, cuts - 1)) % _mod;
      }
    }

    // vertical cuts
    for (int nc = c + 1; nc < _cols; ++nc) {
      if (_suffix[r][c] - _suffix[r][nc] > 0) {
        res = (res + _dfs(r, nc, cuts - 1)) % _mod;
      }
    }

    _memo[r][c][cuts] = res;
    return res;
  }
}
```

## Golang

```go
func ways(pizza []string, k int) int {
	const MOD = 1000000007
	rows, cols := len(pizza), len(pizza[0])

	// prefix sum of apples
	ps := make([][]int, rows+1)
	for i := range ps {
		ps[i] = make([]int, cols+1)
	}
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			val := 0
			if pizza[i][j] == 'A' {
				val = 1
			}
			ps[i+1][j+1] = ps[i+1][j] + ps[i][j+1] - ps[i][j] + val
		}
	}

	getSum := func(r1, c1, r2, c2 int) int {
		if r1 > r2 || c1 > c2 {
			return 0
		}
		return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]
	}

	// dp memo: rows x cols x k (cuts remaining)
	dp := make([][][]int, rows)
	for i := 0; i < rows; i++ {
		dp[i] = make([][]int, cols)
		for j := 0; j < cols; j++ {
			dp[i][j] = make([]int, k)
			for c := 0; c < k; c++ {
				dp[i][j][c] = -1
			}
		}
	}

	var dfs func(r, c, rem int) int
	dfs = func(r, c, rem int) int {
		if dp[r][c][rem] != -1 {
			return dp[r][c][rem]
		}
		// no apple in current sub‑pizza
		if getSum(r, c, rows-1, cols-1) == 0 {
			dp[r][c][rem] = 0
			return 0
		}
		if rem == 0 {
			dp[r][c][rem] = 1
			return 1
		}
		ans := 0
		// horizontal cuts
		for nr := r + 1; nr < rows; nr++ {
			if getSum(r, c, nr-1, cols-1) > 0 {
				ans = (ans + dfs(nr, c, rem-1)) % MOD
			}
		}
		// vertical cuts
		for nc := c + 1; nc < cols; nc++ {
			if getSum(r, c, rows-1, nc-1) > 0 {
				ans = (ans + dfs(r, nc, rem-1)) % MOD
			}
		}
		dp[r][c][rem] = ans
		return ans
	}

	return dfs(0, 0, k-1)
}
```

## Ruby

```ruby
def ways(pizza, k)
  mod = 1_000_000_007
  rows = pizza.size
  cols = pizza[0].size

  # suffix sum of apples: apples[i][j] = number of 'A' in submatrix (i,j) to bottom‑right
  apples = Array.new(rows + 1) { Array.new(cols + 1, 0) }
  (rows - 1).downto(0) do |i|
    (cols - 1).downto(0) do |j|
      apples[i][j] = (pizza[i][j] == 'A' ? 1 : 0) + apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]
    end
  end

  dp = Array.new(rows) { Array.new(cols) { Array.new(k + 1) } }

  dfs = nil
  dfs = ->(r, c, cuts_left) do
    return 0 if apples[r][c] == 0
    return 1 if cuts_left == 1

    memo = dp[r][c][cuts_left]
    return memo unless memo.nil?

    ans = 0

    # horizontal cuts
    (r + 1...rows).each do |nr|
      if apples[r][c] - apples[nr][c] > 0
        ans += dfs.call(nr, c, cuts_left - 1)
        ans %= mod
      end
    end

    # vertical cuts
    (c + 1...cols).each do |nc|
      if apples[r][c] - apples[r][nc] > 0
        ans += dfs.call(r, nc, cuts_left - 1)
        ans %= mod
      end
    end

    dp[r][c][cuts_left] = ans
    ans
  end

  dfs.call(0, 0, k) % mod
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007

    def ways(pizza: Array[String], k: Int): Int = {
        val R = pizza.length
        val C = pizza(0).length

        // suffix sum of apples
        val apples = Array.ofDim[Int](R + 1, C + 1)
        for (i <- R - 1 to 0 by -1) {
            for (j <- C - 1 to 0 by -1) {
                apples(i)(j) = (if (pizza(i)(j) == 'A') 1 else 0) +
                               apples(i + 1)(j) + apples(i)(j + 1) -
                               apples(i + 1)(j + 1)
            }
        }

        // memoization array, -1 means uncomputed
        val memo = Array.ofDim[Int](R, C, k + 1)
        for (i <- 0 until R; j <- 0 until C) java.util.Arrays.fill(memo(i)(j), -1)

        def dfs(r: Int, c: Int, pieces: Int): Int = {
            if (apples(r)(c) == 0) return 0
            if (pieces == 1) return 1
            val cached = memo(r)(c)(pieces)
            if (cached != -1) return cached

            var res: Long = 0L

            // horizontal cuts
            var nr = r + 1
            while (nr < R) {
                // top part must contain at least one apple
                if (apples(r)(c) - apples(nr)(c) > 0) {
                    res += dfs(nr, c, pieces - 1)
                }
                nr += 1
            }

            // vertical cuts
            var nc = c + 1
            while (nc < C) {
                // left part must contain at least one apple
                if (apples(r)(c) - apples(r)(nc) > 0) {
                    res += dfs(r, nc, pieces - 1)
                }
                nc += 1
            }

            val ans = (res % MOD).toInt
            memo(r)(c)(pieces) = ans
            ans
        }

        dfs(0, 0, k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn ways(pizza: Vec<String>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let rows = pizza.len();
        let cols = pizza[0].len();

        // suffix sum of apples
        let mut sum = vec![vec![0usize; cols + 1]; rows + 1];
        for i in (0..rows).rev() {
            let bytes = pizza[i].as_bytes();
            for j in (0..cols).rev() {
                sum[i][j] = (bytes[j] == b'A') as usize
                    + sum[i + 1][j]
                    + sum[i][j + 1]
                    - sum[i + 1][j + 1];
            }
        }

        let k_usize = k as usize;
        // memo[row][col][cuts_left]
        let mut memo = vec![vec![vec![-1i64; k_usize + 1]; cols]; rows];

        fn dfs(
            r: usize,
            c: usize,
            cuts_left: usize,
            rows: usize,
            cols: usize,
            sum: &Vec<Vec<usize>>,
            memo: &mut Vec<Vec<Vec<i64>>>,
        ) -> i64 {
            const MOD: i64 = 1_000_000_007;
            if sum[r][c] == 0 {
                return 0;
            }
            if cuts_left == 1 {
                return 1;
            }
            if memo[r][c][cuts_left] != -1 {
                return memo[r][c][cuts_left];
            }
            let mut ans: i64 = 0;

            // horizontal cuts
            for nr in r + 1..rows {
                if sum[r][c] > sum[nr][c] {
                    ans += dfs(nr, c, cuts_left - 1, rows, cols, sum, memo);
                    if ans >= MOD {
                        ans -= MOD;
                    }
                }
            }

            // vertical cuts
            for nc in c + 1..cols {
                if sum[r][c] > sum[r][nc] {
                    ans += dfs(r, nc, cuts_left - 1, rows, cols, sum, memo);
                    if ans >= MOD {
                        ans -= MOD;
                    }
                }
            }

            ans %= MOD;
            memo[r][c][cuts_left] = ans;
            ans
        }

        let result = dfs(0, 0, k_usize, rows, cols, &sum, &mut memo);
        (result % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (ways pizza k)
  (-> (listof string?) exact-integer? exact-integer?)
  (let* ((rows (length pizza))
         (cols (if (= rows 0) 0 (string-length (first pizza))))
         ;; suffix sum matrix: sum[i][j] = apples in sub‑matrix (i,j) .. (rows-1, cols-1)
         (sum (make-vector (+ rows 1) #f)))
    (for ([i (in-range (+ rows 1))])
      (vector-set! sum i (make-vector (+ cols 1) 0)))
    (for ([i (in-range (sub1 rows) -1 -1)])
      (for ([j (in-range (sub1 cols) -1 -1)])
        (let* ((val (if (char=? (string-ref (list-ref pizza i) j) #\A) 1 0))
               (down (vector-ref (vector-ref sum (+ i 1)) j))
               (right (vector-ref (vector-ref sum i) (+ j 1)))
               (diag (vector-ref (vector-ref sum (+ i 1)) (+ j 1)))
               (total (+ val down right (- diag))))
          (vector-set! (vector-ref sum i) j total))))
    ;; memo table dp[row][col][cuts]
    (define dp (make-vector rows #f))
    (for ([i (in-range rows)])
      (let ((rowvec (make-vector cols #f)))
        (vector-set! dp i rowvec)
        (for ([j (in-range cols)])
          (vector-set! rowvec j (make-vector k -1)))))
    ;; recursive DP
    (define (dfs r c cuts)
      (if (= (vector-ref (vector-ref sum r) c) 0)
          0
          (if (= cuts 0)
              1
              (let ((memo (vector-ref (vector-ref (vector-ref dp r) c) cuts)))
                (if (not (= memo -1))
                    memo
                    (let ((total
                           (let ((tot 0))
                             ;; horizontal cuts
                             (for ([nr (in-range (+ r 1) rows)])
                               (when (> (- (vector-ref (vector-ref sum r) c)
                                          (vector-ref (vector-ref sum nr) c)) 0)
                                 (set! tot (modulo (+ tot (dfs nr c (sub1 cuts))) MOD))))
                             ;; vertical cuts
                             (for ([nc (in-range (+ c 1) cols)])
                               (when (> (- (vector-ref (vector-ref sum r) c)
                                          (vector-ref (vector-ref sum r) nc)) 0)
                                 (set! tot (modulo (+ tot (dfs r nc (sub1 cuts))) MOD))))
                             tot)))
                      (vector-set! (vector-ref (vector-ref dp r) c) cuts total)
                      total))))))
    (dfs 0 0 (- k 1))))
```

## Erlang

```erlang
-module(solution).
-export([ways/2]).

-define(MOD, 1000000007).

ways(Pizza, K) ->
    Rows = length(Pizza),
    RowLists = [binary_to_list(RowBin) || RowBin <- Pizza],
    Cols = case RowLists of [] -> 0; [First|_] -> length(First) end,
    SuffixMap = build_suffix(RowLists, Rows, Cols, #{}),
    BaseDP = base_dp(SuffixMap, Rows, Cols),
    FinalDP = dp_iterations(BaseDP, SuffixMap, Rows, Cols, K - 1),
    maps:get({0,0}, FinalDP, 0).

%% Build suffix sum map: number of apples in submatrix (r,c) .. bottom-right
build_suffix(_RowsList, -1, _Cols, Acc) ->
    Acc;
build_suffix(RowsList, R, Cols, Acc) ->
    Acc2 = build_suffix_row(RowsList, R, Cols - 1, Acc),
    build_suffix(RowsList, R - 1, Cols, Acc2).

build_suffix_row(_RowsList, _R, -1, Acc) ->
    Acc;
build_suffix_row(RowsList, R, C, Acc) ->
    Row = lists:nth(R + 1, RowsList),
    Cell = lists:nth(C + 1, Row),
    Apple = if Cell == $A -> 1; true -> 0 end,
    Count = Apple
            + get_suf(Acc, {R+1, C})
            + get_suf(Acc, {R,   C+1})
            - get_suf(Acc, {R+1, C+1}),
    NewAcc = maps:put({R, C}, Count, Acc),
    build_suffix_row(RowsList, R, C - 1, NewAcc).

get_suf(Map, Key) ->
    maps:get(Key, Map, 0).

%% Base DP for 0 remaining cuts
base_dp(SuffixMap, Rows, Cols) ->
    lists:foldl(fun(R, AccR) ->
        lists:foldl(fun(C, AccC) ->
            Count = maps:get({R,C}, SuffixMap),
            if Count > 0 -> maps:put({R,C}, 1, AccC);
               true      -> AccC
            end
        end, AccR, lists:seq(0, Cols-1))
    end, #{}, lists:seq(0, Rows-1)).

%% Perform DP for remaining cuts
dp_iterations(DPPrev, _SuffixMap, _Rows, _Cols, 0) ->
    DPPrev;
dp_iterations(DPPrev, SuffixMap, Rows, Cols, CutsLeft) ->
    DPCurr = compute_one_step(DPPrev, SuffixMap, Rows, Cols),
    dp_iterations(DPCurr, SuffixMap, Rows, Cols, CutsLeft - 1).

compute_one_step(DPPrev, SuffixMap, Rows, Cols) ->
    lists:foldl(fun(R, AccR) ->
        lists:foldl(fun(C, AccC) ->
            Ways = compute_ways_at(R, C, DPPrev, SuffixMap, Rows, Cols),
            if Ways > 0 -> maps:put({R,C}, Ways, AccC);
               true      -> AccC
            end
        end, AccR, lists:seq(0, Cols-1))
    end, #{}, lists:seq(0, Rows-1)).

compute_ways_at(R, C, DPPrev, SuffixMap, Rows, Cols) ->
    Total = get_suf(SuffixMap, {R,C}),
    Hor = horizontal_cuts(R+1, Rows-1, R, C, Total, DPPrev, SuffixMap),
    Vert = vertical_cuts(C+1, Cols-1, R, C, Total, DPPrev, SuffixMap),
    (Hor + Vert) rem ?MOD.

horizontal_cuts(Start, End, R, C, Total, DPPrev, SuffixMap) when Start > End ->
    0;
horizontal_cuts(Start, End, R, C, Total, DPPrev, SuffixMap) ->
    lists:foldl(fun(NR, Acc) ->
        Upper = Total - get_suf(SuffixMap, {NR, C}),
        if Upper > 0 ->
                add_mod(Acc, maps:get({NR, C}, DPPrev, 0));
           true -> Acc
        end
    end, 0, lists:seq(Start, End)).

vertical_cuts(Start, End, R, C, Total, DPPrev, SuffixMap) when Start > End ->
    0;
vertical_cuts(Start, End, R, C, Total, DPPrev, SuffixMap) ->
    lists:foldl(fun(NC, Acc) ->
        Left = Total - get_suf(SuffixMap, {R, NC}),
        if Left > 0 ->
                add_mod(Acc, maps:get({R, NC}, DPPrev, 0));
           true -> Acc
        end
    end, 0, lists:seq(Start, End)).

add_mod(A, B) ->
    (A + B) rem ?MOD.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec ways(pizza :: [String.t()], k :: integer) :: integer
  def ways(pizza, k) do
    rows = length(pizza)
    cols = String.length(List.first(pizza))

    apples =
      Enum.map(pizza, fn row ->
        row
        |> String.graphemes()
        |> Enum.map(fn ch -> if ch == "A", do: 1, else: 0 end)
      end)

    total_cols = cols + 1
    size = (rows + 1) * total_cols
    arr0 = :array.new(size, default: 0)

    arr =
      Enum.reduce((rows - 1)..0, arr0, fn i, acc ->
        Enum.reduce((cols - 1)..0, acc, fn j, acc2 ->
          idx = i * total_cols + j
          val = Enum.at(apples, i) |> Enum.at(j)
          down = :array.get(((i + 1) * total_cols) + j, acc2)
          right = :array.get(i * total_cols + (j + 1), acc2)
          diag = :array.get(((i + 1) * total_cols) + (j + 1), acc2)
          sum = val + down + right - diag
          :array.set(idx, sum, acc2)
        end)
      end)

    has_apple = fn i, j ->
      :array.get(i * total_cols + j, arr) > 0
    end

    top_has_apple = fn i, j, r ->
      (:array.get(i * total_cols + j, arr) - :array.get(r * total_cols + j, arr)) > 0
    end

    left_has_apple = fn i, j, ccol ->
      (:array.get(i * total_cols + j, arr) - :array.get(i * total_cols + ccol, arr)) > 0
    end

    mod = 1_000_000_007

    dp_prev =
      Enum.reduce(0..(rows - 1), %{}, fn i, acc ->
        Enum.reduce(0..(cols - 1), acc, fn j, acc2 ->
          val = if has_apple.(i, j), do: 1, else: 0
          Map.put(acc2, {i, j}, val)
        end)
      end)

    dp_final =
      Enum.reduce(1..(k - 1), dp_prev, fn _cut, dp_prev_cur ->
        dp_cur =
          Enum.reduce(0..(rows - 1), %{}, fn i, acc_i ->
            Enum.reduce(0..(cols - 1), acc_i, fn j, acc_j ->
              if not has_apple.(i, j) do
                Map.put(acc_j, {i, j}, 0)
              else
                sum0 = 0

                sum1 =
                  if i < rows - 1 do
                    Enum.reduce((i + 1)..(rows - 1), sum0, fn r, s ->
                      if top_has_apple.(i, j, r) do
                        rem(s + Map.get(dp_prev_cur, {r, j}), mod)
                      else
                        s
                      end
                    end)
                  else
                    sum0
                  end

                sum2 =
                  if j < cols - 1 do
                    Enum.reduce((j + 1)..(cols - 1), sum1, fn ccol, s ->
                      if left_has_apple.(i, j, ccol) do
                        rem(s + Map.get(dp_prev_cur, {i, ccol}), mod)
                      else
                        s
                      end
                    end)
                  else
                    sum1
                  end

                Map.put(acc_j, {i, j}, sum2)
              end
            end)
          end)

        dp_cur
      end)

    Map.get(dp_final, {0, 0}, 0)
  end
end
```

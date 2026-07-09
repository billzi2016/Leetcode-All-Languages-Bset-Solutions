# 3393. Count Paths With the Given XOR Value

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countPathsWithXorValue(vector<vector<int>>& grid, int k) {
        const int MOD = 1'000'000'007;
        int m = grid.size();
        int n = grid[0].size();
        int totalSteps = m + n - 2;
        int half = totalSteps / 2;

        // forward DP: from (0,0) to cells with i+j <= half
        vector<vector<array<int,16>>> f(m, vector<array<int,16>>(n));
        for (int i=0;i<m;i++) for(int j=0;j<n;j++) f[i][j].fill(0);
        f[0][0][grid[0][0]] = 1;

        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                if (i + j > half) continue;
                for (int x=0;x<16;x++) {
                    int cnt = f[i][j][x];
                    if (!cnt) continue;
                    if (i+1 < m && i+1 + j <= half) {
                        int nx = x ^ grid[i+1][j];
                        f[i+1][j][nx] = (f[i+1][j][nx] + cnt) % MOD;
                    }
                    if (j+1 < n && i + j+1 <= half) {
                        int nx = x ^ grid[i][j+1];
                        f[i][j+1][nx] = (f[i][j+1][nx] + cnt) % MOD;
                    }
                }
            }
        }

        // backward DP: from (m-1,n-1) to cells with i+j >= half
        vector<vector<array<int,16>>> g(m, vector<array<int,16>>(n));
        for (int i=0;i<m;i++) for(int j=0;j<n;j++) g[i][j].fill(0);
        g[m-1][n-1][grid[m-1][n-1]] = 1;

        for (int i=m-1;i>=0;i--) {
            for (int j=n-1;j>=0;j--) {
                if (i + j < half) continue;
                for (int x=0;x<16;x++) {
                    int cnt = g[i][j][x];
                    if (!cnt) continue;
                    if (i-1 >= 0 && i-1 + j >= half) {
                        int nx = x ^ grid[i-1][j];
                        g[i-1][j][nx] = (g[i-1][j][nx] + cnt) % MOD;
                    }
                    if (j-1 >= 0 && i + j-1 >= half) {
                        int nx = x ^ grid[i][j-1];
                        g[i][j-1][nx] = (g[i][j-1][nx] + cnt) % MOD;
                    }
                }
            }
        }

        long long ans = 0;
        for (int i=0;i<m;i++) {
            int j = half - i;
            if (j < 0 || j >= n) continue;
            // cell (i,j) lies on the middle diagonal
            for (int x=0;x<16;x++) {
                long long cntF = f[i][j][x];
                if (!cntF) continue;
                for (int y=0;y<16;y++) {
                    long long cntG = g[i][j][y];
                    if (!cntG) continue;
                    int totalXor = x ^ y ^ grid[i][j];
                    if (totalXor == k) {
                        ans = (ans + cntF * cntG) % MOD;
                    }
                }
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countPathsWithXorValue(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        final int MOD = 1_000_000_007;
        int totalSteps = m + n - 2;
        int mid = totalSteps / 2;

        int[][][] fwd = new int[m][n][16];
        fwd[0][0][grid[0][0]] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i + j > mid) continue;
                int[] cur = fwd[i][j];
                // down
                if (i + 1 < m && i + 1 + j <= mid) {
                    int[] nxt = fwd[i + 1][j];
                    int val = grid[i + 1][j];
                    for (int x = 0; x < 16; x++) {
                        int cnt = cur[x];
                        if (cnt != 0) {
                            int nx = x ^ val;
                            nxt[nx] = (nxt[nx] + cnt) % MOD;
                        }
                    }
                }
                // right
                if (j + 1 < n && i + j + 1 <= mid) {
                    int[] nxt = fwd[i][j + 1];
                    int val = grid[i][j + 1];
                    for (int x = 0; x < 16; x++) {
                        int cnt = cur[x];
                        if (cnt != 0) {
                            int nx = x ^ val;
                            nxt[nx] = (nxt[nx] + cnt) % MOD;
                        }
                    }
                }
            }
        }

        int[][][] back = new int[m][n][16];
        back[m - 1][n - 1][grid[m - 1][n - 1]] = 1;

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i + j < mid) continue;
                int[] cur = back[i][j];
                // up
                if (i - 1 >= 0 && i - 1 + j >= mid) {
                    int[] nxt = back[i - 1][j];
                    int val = grid[i - 1][j];
                    for (int x = 0; x < 16; x++) {
                        int cnt = cur[x];
                        if (cnt != 0) {
                            int nx = x ^ val;
                            nxt[nx] = (nxt[nx] + cnt) % MOD;
                        }
                    }
                }
                // left
                if (j - 1 >= 0 && i + j - 1 >= mid) {
                    int[] nxt = back[i][j - 1];
                    int val = grid[i][j - 1];
                    for (int x = 0; x < 16; x++) {
                        int cnt = cur[x];
                        if (cnt != 0) {
                            int nx = x ^ val;
                            nxt[nx] = (nxt[nx] + cnt) % MOD;
                        }
                    }
                }
            }
        }

        long ans = 0;
        for (int i = 0; i < m; i++) {
            int j = mid - i;
            if (j < 0 || j >= n) continue;
            int[] fArr = fwd[i][j];
            int[] bArr = back[i][j];
            for (int a = 0; a < 16; a++) {
                int cntF = fArr[a];
                if (cntF == 0) continue;
                int needB = a ^ grid[i][j] ^ k;
                if (needB < 0 || needB >= 16) continue;
                int cntB = bArr[needB];
                if (cntB != 0) {
                    ans = (ans + (long) cntF * cntB) % MOD;
                }
            }
        }

        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        # dp[i][j][x] = number of ways to reach (i,j) with xor value x
        dp = [[[0] * 16 for _ in range(n)] for __ in range(m)]
        dp[0][0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                cur = dp[i][j]
                if i > 0:
                    prev = dp[i - 1][j]
                    for x in range(16):
                        cnt = prev[x]
                        if cnt:
                            cur[x ^ val] = (cur[x ^ val] + cnt) % MOD
                if j > 0:
                    prev = dp[i][j - 1]
                    for x in range(16):
                        cnt = prev[x]
                        if cnt:
                            cur[x ^ val] = (cur[x ^ val] + cnt) % MOD

        return dp[m - 1][n - 1][k] % MOD
```

## Python3

```python
from typing import List

class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0] * 16 for _ in range(n)]  # previous row
        
        for i in range(m):
            cur = [[0] * 16 for _ in range(n)]
            for j in range(n):
                val = grid[i][j]
                if i == 0 and j == 0:
                    cur[j][val] = 1
                    continue
                # from top
                if i > 0:
                    prev_row = dp[j]
                    for x in range(16):
                        cnt = prev_row[x]
                        if cnt:
                            cur[j][x ^ val] = (cur[j][x ^ val] + cnt) % MOD
                # from left
                if j > 0:
                    left_cell = cur[j - 1]
                    for x in range(16):
                        cnt = left_cell[x]
                        if cnt:
                            cur[j][x ^ val] = (cur[j][x ^ val] + cnt) % MOD
            dp = cur
        
        return dp[n - 1][k]
```

## C

```c
int countPathsWithXorValue(int** grid, int gridSize, int* gridColSize, int k) {
    const int MOD = 1000000007;
    int m = gridSize;
    int n = gridColSize[0];
    long long *dp = (long long*)calloc((size_t)m * n * 16, sizeof(long long));
    #define IDX(i,j,x) ((i) * n * 16 + (j) * 16 + (x))
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int cur = grid[i][j];
            if (i == 0 && j == 0) {
                dp[IDX(0, 0, cur)] = 1;
                continue;
            }
            for (int x = 0; x < 16; ++x) {
                int prev = x ^ cur;
                long long ways = 0;
                if (i > 0) ways += dp[IDX(i - 1, j, prev)];
                if (j > 0) ways += dp[IDX(i, j - 1, prev)];
                if (ways >= MOD) ways %= MOD;
                dp[IDX(i, j, x)] = ways;
            }
        }
    }
    
    long long ans = dp[IDX(m - 1, n - 1, k)] % MOD;
    free(dp);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPathsWithXorValue(int[][] grid, int k) {
        const int MOD = 1000000007;
        int m = grid.Length;
        int n = grid[0].Length;
        var dp = new int[m, n, 16];
        dp[0, 0, grid[0][0]] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int x = 0; x < 16; x++) {
                    int cur = dp[i, j, x];
                    if (cur == 0) continue;
                    if (i + 1 < m) {
                        int nx = x ^ grid[i + 1][j];
                        dp[i + 1, j, nx] = (dp[i + 1, j, nx] + cur) % MOD;
                    }
                    if (j + 1 < n) {
                        int nx = x ^ grid[i][j + 1];
                        dp[i, j + 1, nx] = (dp[i, j + 1, nx] + cur) % MOD;
                    }
                }
            }
        }

        return dp[m - 1, n - 1, k];
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
var countPathsWithXorValue = function(grid, k) {
    const MOD = 1000000007;
    const m = grid.length;
    const n = grid[0].length;
    // dp for previous row: array of length n, each is an array of size 16
    let prev = Array.from({ length: n }, () => new Array(16).fill(0));

    for (let i = 0; i < m; i++) {
        const cur = Array.from({ length: n }, () => new Array(16).fill(0));
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) {
                cur[0][grid[0][0]] = 1;
                continue;
            }
            const val = grid[i][j];
            // from top
            if (i > 0) {
                const up = prev[j];
                for (let x = 0; x < 16; x++) {
                    const cnt = up[x];
                    if (cnt !== 0) {
                        const nx = x ^ val;
                        cur[j][nx] = (cur[j][nx] + cnt) % MOD;
                    }
                }
            }
            // from left
            if (j > 0) {
                const left = cur[j - 1];
                for (let x = 0; x < 16; x++) {
                    const cnt = left[x];
                    if (cnt !== 0) {
                        const nx = x ^ val;
                        cur[j][nx] = (cur[j][nx] + cnt) % MOD;
                    }
                }
            }
        }
        prev = cur;
    }

    return prev[n - 1][k] % MOD;
};
```

## Typescript

```typescript
function countPathsWithXorValue(grid: number[][], k: number): number {
    const MOD = 1_000_000_007;
    const m = grid.length;
    const n = grid[0].length;

    // dp[i][j][xor] = number of ways to reach (i,j) with xor value
    const dp: number[][][] = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => new Array(16).fill(0))
    );

    dp[0][0][grid[0][0]] = 1;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (i === 0 && j === 0) continue;
            const v = grid[i][j];
            const cur = dp[i][j];

            if (i > 0) {
                const up = dp[i - 1][j];
                for (let x = 0; x < 16; ++x) {
                    const cnt = up[x];
                    if (cnt !== 0) {
                        const nx = x ^ v;
                        cur[nx] = (cur[nx] + cnt) % MOD;
                    }
                }
            }

            if (j > 0) {
                const left = dp[i][j - 1];
                for (let x = 0; x < 16; ++x) {
                    const cnt = left[x];
                    if (cnt !== 0) {
                        const nx = x ^ v;
                        cur[nx] = (cur[nx] + cnt) % MOD;
                    }
                }
            }
        }
    }

    return dp[m - 1][n - 1][k] % MOD;
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
    function countPathsWithXorValue($grid, $k) {
        $mod = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);
        
        // Initialize DP array: dp[i][j][xor] = number of ways to reach (i,j) with xor value
        $dp = [];
        for ($i = 0; $i < $m; $i++) {
            $row = [];
            for ($j = 0; $j < $n; $j++) {
                $row[$j] = array_fill(0, 16, 0);
            }
            $dp[$i] = $row;
        }
        
        $startVal = $grid[0][0];
        $dp[0][0][$startVal] = 1;
        
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                for ($xor = 0; $xor < 16; $xor++) {
                    $cnt = $dp[$i][$j][$xor];
                    if ($cnt == 0) continue;
                    
                    // Move right
                    if ($j + 1 < $n) {
                        $newXor = $xor ^ $grid[$i][$j + 1];
                        $dp[$i][$j + 1][$newXor] = ($dp[$i][$j + 1][$newXor] + $cnt) % $mod;
                    }
                    
                    // Move down
                    if ($i + 1 < $m) {
                        $newXor = $xor ^ $grid[$i + 1][$j];
                        $dp[$i + 1][$j][$newXor] = ($dp[$i + 1][$j][$newXor] + $cnt) % $mod;
                    }
                }
            }
        }
        
        return $dp[$m - 1][$n - 1][$k] % $mod;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func countPathsWithXorValue(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count
        let n = grid[0].count
        // forward DP: from (0,0) to each cell
        var forward = Array(repeating: Array(repeating: [Int](repeating: 0, count: 16), count: n), count: m)
        forward[0][0][grid[0][0]] = 1

        for i in 0..<m {
            for j in 0..<n {
                let curArr = forward[i][j]
                if i + 1 < m {
                    var nextArr = forward[i + 1][j]
                    for xorVal in 0..<16 {
                        let cnt = curArr[xorVal]
                        if cnt == 0 { continue }
                        let newXor = xorVal ^ grid[i + 1][j]
                        let sum = (nextArr[newXor] + cnt) % MOD
                        nextArr[newXor] = sum
                    }
                    forward[i + 1][j] = nextArr
                }
                if j + 1 < n {
                    var nextArr = forward[i][j + 1]
                    for xorVal in 0..<16 {
                        let cnt = curArr[xorVal]
                        if cnt == 0 { continue }
                        let newXor = xorVal ^ grid[i][j + 1]
                        let sum = (nextArr[newXor] + cnt) % MOD
                        nextArr[newXor] = sum
                    }
                    forward[i][j + 1] = nextArr
                }
            }
        }

        // backward DP: from (m-1,n-1) to each cell moving up/left
        var backward = Array(repeating: Array(repeating: [Int](repeating: 0, count: 16), count: n), count: m)
        backward[m - 1][n - 1][grid[m - 1][n - 1]] = 1

        if m > 0 && n > 0 {
            for i in stride(from: m - 1, through: 0, by: -1) {
                for j in stride(from: n - 1, through: 0, by: -1) {
                    let curArr = backward[i][j]
                    if i > 0 {
                        var nextArr = backward[i - 1][j]
                        for xorVal in 0..<16 {
                            let cnt = curArr[xorVal]
                            if cnt == 0 { continue }
                            let newXor = xorVal ^ grid[i - 1][j]
                            let sum = (nextArr[newXor] + cnt) % MOD
                            nextArr[newXor] = sum
                        }
                        backward[i - 1][j] = nextArr
                    }
                    if j > 0 {
                        var nextArr = backward[i][j - 1]
                        for xorVal in 0..<16 {
                            let cnt = curArr[xorVal]
                            if cnt == 0 { continue }
                            let newXor = xorVal ^ grid[i][j - 1]
                            let sum = (nextArr[newXor] + cnt) % MOD
                            nextArr[newXor] = sum
                        }
                        backward[i][j - 1] = nextArr
                    }
                }
            }
        }

        let totalSteps = m + n - 2
        let half = totalSteps / 2
        var result: Int64 = 0

        for i in 0..<m {
            let j = half - i
            if j < 0 || j >= n { continue }
            let fArr = forward[i][j]
            let bArr = backward[i][j]
            let cellVal = grid[i][j]
            for xorF in 0..<16 {
                let cntF = fArr[xorF]
                if cntF == 0 { continue }
                let need = xorF ^ k ^ cellVal
                let cntB = bArr[need]
                if cntB == 0 { continue }
                result = (result + Int64(cntF) * Int64(cntB)) % Int64(MOD)
            }
        }

        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPathsWithXorValue(grid: Array<IntArray>, k: Int): Int {
        val MOD = 1_000_000_007L
        val m = grid.size
        val n = grid[0].size
        val totalSteps = m + n - 2
        val half = totalSteps / 2

        // forward DP up to steps == half
        val f = Array(m) { Array(n) { IntArray(16) } }
        f[0][0][grid[0][0]] = 1
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i + j > half) continue
                val cur = f[i][j]
                if (i + 1 < m && i + 1 + j <= half) {
                    val nxt = f[i + 1][j]
                    for (x in 0 until 16) {
                        val cnt = cur[x]
                        if (cnt != 0) {
                            val nx = x xor grid[i + 1][j]
                            var v = nxt[nx] + cnt
                            if (v >= MOD.toInt()) v -= MOD.toInt()
                            nxt[nx] = v
                        }
                    }
                }
                if (j + 1 < n && i + j + 1 <= half) {
                    val nxt = f[i][j + 1]
                    for (x in 0 until 16) {
                        val cnt = cur[x]
                        if (cnt != 0) {
                            val nx = x xor grid[i][j + 1]
                            var v = nxt[nx] + cnt
                            if (v >= MOD.toInt()) v -= MOD.toInt()
                            nxt[nx] = v
                        }
                    }
                }
            }
        }

        // backward DP from end down to steps == half
        val b = Array(m) { Array(n) { IntArray(16) } }
        b[m - 1][n - 1][grid[m - 1][n - 1]] = 1
        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (i + j < half) continue
                val cur = b[i][j]
                if (i - 1 >= 0 && i - 1 + j >= half) {
                    val nxt = b[i - 1][j]
                    for (x in 0 until 16) {
                        val cnt = cur[x]
                        if (cnt != 0) {
                            val nx = x xor grid[i - 1][j]
                            var v = nxt[nx] + cnt
                            if (v >= MOD.toInt()) v -= MOD.toInt()
                            nxt[nx] = v
                        }
                    }
                }
                if (j - 1 >= 0 && i + j - 1 >= half) {
                    val nxt = b[i][j - 1]
                    for (x in 0 until 16) {
                        val cnt = cur[x]
                        if (cnt != 0) {
                            val nx = x xor grid[i][j - 1]
                            var v = nxt[nx] + cnt
                            if (v >= MOD.toInt()) v -= MOD.toInt()
                            nxt[nx] = v
                        }
                    }
                }
            }
        }

        var ans = 0L
        for (i in 0 until m) {
            val j = half - i
            if (j < 0 || j >= n) continue
            val fArr = f[i][j]
            val bArr = b[i][j]
            for (a in 0 until 16) {
                val cntF = fArr[a]
                if (cntF == 0) continue
                val need = a xor k xor grid[i][j]
                val cntB = bArr[need]
                if (cntB != 0) {
                    ans += (cntF.toLong() * cntB.toLong()) % MOD
                    if (ans >= MOD) ans -= MOD
                }
            }
        }

        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int countPathsWithXorValue(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int totalSteps = (m - 1) + (n - 1);
    int mid = totalSteps ~/ 2;

    // forward DP: from (0,0) to cells with i+j <= mid
    List<List<List<int>>> f = List.generate(
        m, (_) => List.generate(n, (_) => List.filled(16, 0)));
    f[0][0][grid[0][0]] = 1;

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i + j > mid) continue;
        List<int> cur = f[i][j];
        for (int x = 0; x < 16; ++x) {
          int cnt = cur[x];
          if (cnt == 0) continue;
          // move right
          if (j + 1 < n && i + j + 1 <= mid) {
            int nx = x ^ grid[i][j + 1];
            f[i][j + 1][nx] = (f[i][j + 1][nx] + cnt) % _MOD;
          }
          // move down
          if (i + 1 < m && i + 1 + j <= mid) {
            int nx = x ^ grid[i + 1][j];
            f[i + 1][j][nx] = (f[i + 1][j][nx] + cnt) % _MOD;
          }
        }
      }
    }

    // backward DP: from (m-1,n-1) to cells with i+j >= mid
    List<List<List<int>>> b = List.generate(
        m, (_) => List.generate(n, (_) => List.filled(16, 0)));
    b[m - 1][n - 1][grid[m - 1][n - 1]] = 1;

    for (int i = m - 1; i >= 0; --i) {
      for (int j = n - 1; j >= 0; --j) {
        if (i + j < mid) continue;
        List<int> cur = b[i][j];
        for (int x = 0; x < 16; ++x) {
          int cnt = cur[x];
          if (cnt == 0) continue;
          // move left
          if (j - 1 >= 0 && i + j - 1 >= mid) {
            int nx = x ^ grid[i][j - 1];
            b[i][j - 1][nx] = (b[i][j - 1][nx] + cnt) % _MOD;
          }
          // move up
          if (i - 1 >= 0 && i - 1 + j >= mid) {
            int nx = x ^ grid[i - 1][j];
            b[i - 1][j][nx] = (b[i - 1][j][nx] + cnt) % _MOD;
          }
        }
      }
    }

    // combine at the middle diagonal
    int ans = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (i + j != mid) continue;
        List<int> fv = f[i][j];
        List<int> bv = b[i][j];
        for (int a = 0; a < 16; ++a) {
          int cntF = fv[a];
          if (cntF == 0) continue;
          int need = a ^ k ^ grid[i][j];
          int cntB = bv[need];
          if (cntB == 0) continue;
          ans = (ans + (cntF * cntB) % _MOD) % _MOD;
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countPathsWithXorValue(grid [][]int, k int) int {
	const MOD = 1000000007
	m, n := len(grid), len(grid[0])

	// dp[i][j][x] = number of ways to reach (i,j) with xor value x
	dp := make([][][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]int, 16)
		}
	}

	startXor := grid[0][0]
	dp[0][0][startXor] = 1

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			val := grid[i][j]

			if i > 0 {
				prev := dp[i-1][j]
				cur := dp[i][j]
				for x := 0; x < 16; x++ {
					if cnt := prev[x]; cnt != 0 {
						nx := x ^ val
						cur[nx] = (cur[nx] + cnt) % MOD
					}
				}
			}
			if j > 0 {
				prev := dp[i][j-1]
				cur := dp[i][j]
				for x := 0; x < 16; x++ {
					if cnt := prev[x]; cnt != 0 {
						nx := x ^ val
						cur[nx] = (cur[nx] + cnt) % MOD
					}
				}
			}
		}
	}

	return dp[m-1][n-1][k] % MOD
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def count_paths_with_xor_value(grid, k)
  m = grid.length
  n = grid[0].length
  dp = Array.new(n) { Array.new(16, 0) }

  (0...m).each do |i|
    new_dp = Array.new(n) { Array.new(16, 0) }
    (0...n).each do |j|
      val = grid[i][j]
      if i == 0 && j == 0
        new_dp[j][val] = 1
        next
      end

      # from top
      if i > 0
        prev = dp[j]
        16.times do |x|
          cnt = prev[x]
          next if cnt.zero?
          nx = x ^ val
          new_dp[j][nx] = (new_dp[j][nx] + cnt) % MOD
        end
      end

      # from left
      if j > 0
        left = new_dp[j - 1]
        16.times do |x|
          cnt = left[x]
          next if cnt.zero?
          nx = x ^ val
          new_dp[j][nx] = (new_dp[j][nx] + cnt) % MOD
        end
      end
    end
    dp = new_dp
  end

  dp[n - 1][k] % MOD
end
```

## Scala

```scala
object Solution {
    def countPathsWithXorValue(grid: Array[Array[Int]], k: Int): Int = {
        val MOD = 1000000007L
        val m = grid.length
        val n = grid(0).length
        val dp = Array.ofDim[Long](m, n, 16)
        dp(0)(0)(grid(0)(0)) = 1L
        for (i <- 0 until m) {
            for (j <- 0 until n) {
                for (x <- 0 until 16) {
                    val ways = dp(i)(j)(x)
                    if (ways != 0) {
                        if (i + 1 < m) {
                            val nx = x ^ grid(i + 1)(j)
                            dp(i + 1)(j)(nx) = (dp(i + 1)(j)(nx) + ways) % MOD
                        }
                        if (j + 1 < n) {
                            val ny = x ^ grid(i)(j + 1)
                            dp(i)(j + 1)(ny) = (dp(i)(j + 1)(ny) + ways) % MOD
                        }
                    }
                }
            }
        }
        dp(m - 1)(n - 1)(k).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_paths_with_xor_value(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const MOD: i64 = 1_000_000_007;
        // dp[i][j][xor] = number of ways to reach (i,j) with given xor
        let mut dp = vec![vec![[0i64; 16]; n]; m];
        dp[0][0][grid[0][0] as usize] = 1;
        for i in 0..m {
            for j in 0..n {
                if i == 0 && j == 0 {
                    continue;
                }
                let val = grid[i][j] as usize;
                // from top
                if i > 0 {
                    for x in 0..16 {
                        let cnt = dp[i - 1][j][x];
                        if cnt != 0 {
                            let nx = x ^ val;
                            dp[i][j][nx] = (dp[i][j][nx] + cnt) % MOD;
                        }
                    }
                }
                // from left
                if j > 0 {
                    for x in 0..16 {
                        let cnt = dp[i][j - 1][x];
                        if cnt != 0 {
                            let nx = x ^ val;
                            dp[i][j][nx] = (dp[i][j][nx] + cnt) % MOD;
                        }
                    }
                }
            }
        }
        dp[m - 1][n - 1][k as usize] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-paths-with-xor-value grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([m (length grid)]
         [n (if (= m 0) 0 (length (first grid)))]
         [grid-vec
          (list->vector
           (map (lambda (row) (list->vector row)) grid))]
         [dp (make-vector m)])
    ;; initialise dp matrix of vectors
    (for ([i (in-range m)])
      (vector-set! dp i (make-vector n)))
    ;; DP computation
    (for ([i (in-range m)])
      (for ([j (in-range n)])
        (let* ([val (vector-ref (vector-ref grid-vec i) j)]
               [cur (make-vector 16 0)])
          (cond
            [(and (= i 0) (= j 0))
             (vector-set! cur val
                          (modulo (+ (vector-ref cur val) 1) MOD))]
            [else
             (when (> i 0)
               (let ([up (vector-ref (vector-ref dp (- i 1)) j)])
                 (for ([x (in-range 16)])
                   (let ([cnt (vector-ref up x)])
                     (when (not (= cnt 0))
                       (let* ([newx (bitwise-xor x val)]
                              [old (vector-ref cur newx)])
                         (vector-set! cur newx
                                      (modulo (+ old cnt) MOD))))))))
             (when (> j 0)
               (let ([left (vector-ref (vector-ref dp i) (- j 1))])
                 (for ([x (in-range 16)])
                   (let ([cnt (vector-ref left x)])
                     (when (not (= cnt 0))
                       (let* ([newx (bitwise-xor x val)]
                              [old (vector-ref cur newx)])
                         (vector-set! cur newx
                                      (modulo (+ old cnt) MOD)))))))))])
          (vector-set! (vector-ref dp i) j cur))))
    (let ([ans (vector-ref (vector-ref (vector-ref dp (- m 1))
                                       (- n 1))
                           k)])
      ans)))
```

## Erlang

```erlang
-spec count_paths_with_xor_value(Grid :: [[integer()]], K :: integer()) -> integer().
count_paths_with_xor_value(Grid, K) ->
    ?MOD = 1000000007,
    M = length(Grid),
    N = length(hd(Grid)),
    GridT = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    L = M - 1 + N - 1,
    Mid = L div 2,
    ForwardMap = forward_dp(GridT, M, N, Mid),
    BackwardMap = backward_dp(GridT, M, N, Mid, L),
    combine(ForwardMap, BackwardMap, GridT, K, Mid, M, N).

%% ------------------------------------------------------------------
%% Forward DP (from start to middle diagonal)
%% ------------------------------------------------------------------
forward_dp(GridT, M, N, Mid) ->
    InitCounts = setelement(get_val(GridT, 0, 0) + 1, make_tuple(16, 0), 1),
    Map0 = #{ {0, 0} => InitCounts },
    forward_loop(0, Mid, M, N, GridT, Map0).

forward_loop(S, Mid, _M, _N, _GridT, Map) when S > Mid ->
    Map;
forward_loop(S, Mid, M, N, GridT, Map) ->
    MaxI = erlang:min(S, M - 1),
    NewMap = lists:foldl(
        fun(I, AccMap) ->
            J = S - I,
            case (J >= 0 andalso J < N) of
                true ->
                    case maps:get({I, J}, AccMap, undefined) of
                        undefined -> AccMap;
                        Counts ->
                            Acc1 = if J + 1 < N, (I + J + 1) =< Mid ->
                                        ValR = get_val(GridT, I, J + 1),
                                        NewCountsR = shift_counts(Counts, ValR),
                                        update_map({I, J + 1}, NewCountsR, AccMap);
                                   true -> AccMap
                                end,
                            Acc2 = if I + 1 < M, (I + 1 + J) =< Mid ->
                                        ValD = get_val(GridT, I + 1, J),
                                        NewCountsD = shift_counts(Counts, ValD),
                                        update_map({I + 1, J}, NewCountsD, Acc1);
                                   true -> Acc1
                                end,
                            Acc2
                    end;
                false -> AccMap
            end
        end,
        Map,
        lists:seq(0, MaxI)
    ),
    forward_loop(S + 1, Mid, M, N, GridT, NewMap).

%% ------------------------------------------------------------------
%% Backward DP (from end to middle diagonal)
%% ------------------------------------------------------------------
backward_dp(GridT, M, N, Mid, L) ->
    InitCounts = setelement(get_val(GridT, M - 1, N - 1) + 1, make_tuple(16, 0), 1),
    Map0 = #{ {M - 1, N - 1} => InitCounts },
    backward_loop(L, Mid + 1, M, N, GridT, Map0).

backward_loop(S, Stop, _M, _N, _GridT, Map) when S < Stop ->
    Map;
backward_loop(S, Stop, M, N, GridT, Map) ->
    IStart = erlang:max(0, S - (N - 1)),
    IEnd   = erlang:min(S, M - 1),
    NewMap = lists:foldl(
        fun(I, AccMap) ->
            J = S - I,
            case (J >= 0 andalso J < N) of
                true ->
                    case maps:get({I, J}, AccMap, undefined) of
                        undefined -> AccMap;
                        Counts ->
                            Acc1 = if I - 1 >= 0, (I - 1 + J) >= Stop ->
                                        ValU = get_val(GridT, I - 1, J),
                                        NewCountsU = shift_counts(Counts, ValU),
                                        update_map({I - 1, J}, NewCountsU, AccMap);
                                   true -> AccMap
                                end,
                            Acc2 = if J - 1 >= 0, (I + J - 1) >= Stop ->
                                        ValL = get_val(GridT, I, J - 1),
                                        NewCountsL = shift_counts(Counts, ValL),
                                        update_map({I, J - 1}, NewCountsL, Acc1);
                                   true -> Acc1
                                end,
                            Acc2
                    end;
                false -> AccMap
            end
        end,
        Map,
        lists:seq(IStart, IEnd)
    ),
    backward_loop(S - 1, Stop, M, N, GridT, NewMap).

%% ------------------------------------------------------------------
%% Combine results on the middle diagonal
%% ------------------------------------------------------------------
combine(FwdMap, BckMap, GridT, K, Mid, M, N) ->
    IStart = erlang:max(0, Mid - (N - 1)),
    IEnd   = erlang:min(Mid, M - 1),
    lists:foldl(
        fun(I, AccAns) ->
            J = Mid - I,
            FwdCounts = maps:get({I, J}, FwdMap, empty_counts()),
            BckCounts = maps:get({I, J}, BckMap, empty_counts()),
            CellVal   = get_val(GridT, I, J),
            combine_cell(FwdCounts, BckCounts, CellVal, K, AccAns)
        end,
        0,
        lists:seq(IStart, IEnd)
    ).

combine_cell(Fwd, Bck, CellVal, K, Acc) ->
    combine_xor_loop(1, Fwd, Bck, CellVal, K, Acc).

combine_xor_loop(Index, _Fwd, _Bck, _CellVal, _K, Acc) when Index > 16 ->
    Acc;
combine_xor_loop(Index, Fwd, Bck, CellVal, K, Acc) ->
    CountF = element(Index, Fwd),
    case CountF of
        0 -> combine_xor_loop(Index + 1, Fwd, Bck, CellVal, K, Acc);
        _ ->
            X = Index - 1,
            Need = (X bxor CellVal bxor K) band 15,
            CountB = element(Need + 1, Bck),
            Add = (CountF * CountB) rem ?MOD,
            NewAcc = (Acc + Add) rem ?MOD,
            combine_xor_loop(Index + 1, Fwd, Bck, CellVal, K, NewAcc)
    end.

%% ------------------------------------------------------------------
%% Helper utilities
%% ------------------------------------------------------------------
empty_counts() ->
    make_tuple(16, 0).

update_map(Key, AddCounts, Map) ->
    Existing = maps:get(Key, Map, empty_counts()),
    Updated = merge_counts(Existing, AddCounts),
    maps:put(Key, Updated, Map).

shift_counts(Counts, Val) ->
    shift_counts_loop(1, Counts, Val, make_tuple(16, 0)).

shift_counts_loop(Index, _Counts, _Val, Acc) when Index > 16 ->
    Acc;
shift_counts_loop(Index, Counts, Val, Acc) ->
    C = element(Index, Counts),
    case C of
        0 -> shift_counts_loop(Index + 1, Counts, Val, Acc);
        _ ->
            NewXor = (Index - 1) bxor Val,
            Pos = NewXor + 1,
            Old = element(Pos, Acc),
            NewVal = (Old + C) rem ?MOD,
            Acc2 = setelement(Pos, Acc, NewVal),
            shift_counts_loop(Index + 1, Counts, Val, Acc2)
    end.

merge_counts(A, B) ->
    merge_counts_loop(1, A, B, make_tuple(16, 0)).

merge_counts_loop(Index, _A, _B, Acc) when Index > 16 ->
    Acc;
merge_counts_loop(Index, A, B, Acc) ->
    Sum = (element(Index, A) + element(Index, B)) rem ?MOD,
    merge_counts_loop(Index + 1, A, B, setelement(Index, Acc, Sum)).

get_val(GridT, I, J) ->
    Row = element(I + 1, GridT),
    element(J + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  require Bitwise

  @spec count_paths_with_xor_value(grid :: [[integer]], k :: integer) :: integer
  def count_paths_with_xor_value(grid, k) do
    m = length(grid)
    n = length(List.first(grid))
    total_steps = m + n - 2
    mid = div(total_steps, 2)
    mod = 1_000_000_007

    # Forward DP up to mid steps
    forward =
      Enum.reduce(0..(m - 1), %{}, fn i, f_acc ->
        Enum.reduce(0..(n - 1), f_acc, fn j, acc2 ->
          if i + j <= mid do
            cell_val = Enum.at(grid, i) |> Enum.at(j)

            cond do
              i == 0 and j == 0 ->
                Map.put(acc2, {i, j}, %{cell_val => 1})

              true ->
                prev_maps =
                  []
                  |> maybe_prepend(i > 0 and (i - 1 + j) <= mid,
                    Map.get(acc2, {i - 1, j})
                  )
                  |> maybe_prepend(j > 0 and (i + j - 1) <= mid,
                    Map.get(acc2, {i, j - 1})
                  )

                new_map =
                  Enum.reduce(prev_maps, %{}, fn pm, macc ->
                    Enum.reduce(pm, macc, fn {xor, cnt}, inner_acc ->
                      nxor = Bitwise.bxor(xor, cell_val)
                      Map.update(inner_acc, nxor, cnt, &(&1 + cnt))
                    end)
                  end)

                Map.put(acc2, {i, j}, new_map)
            end
          else
            acc2
          end
        end)
      end)

    # Backward DP from end down to mid steps
    backward =
      Enum.reduce((m - 1)..0, %{}, fn i, b_acc ->
        Enum.reduce((n - 1)..0, b_acc, fn j, acc2 ->
          if i + j >= mid do
            cell_val = Enum.at(grid, i) |> Enum.at(j)

            cond do
              i == m - 1 and j == n - 1 ->
                Map.put(acc2, {i, j}, %{cell_val => 1})

              true ->
                next_maps =
                  []
                  |> maybe_prepend(i + 1 < m and (i + 1 + j) >= mid,
                    Map.get(acc2, {i + 1, j})
                  )
                  |> maybe_prepend(j + 1 < n and (i + j + 1) >= mid,
                    Map.get(acc2, {i, j + 1})
                  )

                new_map =
                  Enum.reduce(next_maps, %{}, fn nm, macc ->
                    Enum.reduce(nm, macc, fn {xor, cnt}, inner_acc ->
                      nxor = Bitwise.bxor(xor, cell_val)
                      Map.update(inner_acc, nxor, cnt, &(&1 + cnt))
                    end)
                  end)

                Map.put(acc2, {i, j}, new_map)
            end
          else
            acc2
          end
        end)
      end)

    # Combine at middle diagonal
    ans =
      Enum.reduce(0..(m - 1), 0, fn i, sum ->
        Enum.reduce(0..(n - 1), sum, fn j, sum2 ->
          if i + j == mid do
            f_map = Map.get(forward, {i, j}, %{})
            b_map = Map.get(backward, {i, j}, %{})
            cell_val = Enum.at(grid, i) |> Enum.at(j)

            Enum.reduce(f_map, sum2, fn {xor_f, cnt_f}, acc ->
              target = Bitwise.bxor(Bitwise.bxor(xor_f, cell_val), k)
              cnt_b = Map.get(b_map, target, 0)
              (acc + rem(cnt_f * cnt_b, mod)) |> rem(mod)
            end)
          else
            sum2
          end
        end)
      end)

    ans
  end

  defp maybe_prepend(list, condition, value) do
    if condition and not is_nil(value), do: [value | list], else: list
  end
end
```

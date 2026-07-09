# 0764. Largest Plus Sign

## Cpp

```cpp
class Solution {
public:
    int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
        vector<vector<int>> grid(n, vector<int>(n, 1));
        for (const auto& m : mines) {
            grid[m[0]][m[1]] = 0;
        }
        vector<vector<int>> dp(n, vector<int>(n, n)); // max possible arm length
        
        // left
        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            for (int j = 0; j < n; ++j) {
                cnt = grid[i][j] ? cnt + 1 : 0;
                dp[i][j] = min(dp[i][j], cnt);
            }
        }
        // right
        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            for (int j = n - 1; j >= 0; --j) {
                cnt = grid[i][j] ? cnt + 1 : 0;
                dp[i][j] = min(dp[i][j], cnt);
            }
        }
        // up
        for (int j = 0; j < n; ++j) {
            int cnt = 0;
            for (int i = 0; i < n; ++i) {
                cnt = grid[i][j] ? cnt + 1 : 0;
                dp[i][j] = min(dp[i][j], cnt);
            }
        }
        // down
        for (int j = 0; j < n; ++j) {
            int cnt = 0;
            for (int i = n - 1; i >= 0; --i) {
                cnt = grid[i][j] ? cnt + 1 : 0;
                dp[i][j] = min(dp[i][j], cnt);
            }
        }
        
        int ans = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                ans = max(ans, dp[i][j]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int orderOfLargestPlusSign(int n, int[][] mines) {
        boolean[][] zero = new boolean[n][n];
        for (int[] m : mines) {
            zero[m[0]][m[1]] = true;
        }
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = zero[i][j] ? 0 : n;
            }
        }

        // left
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (!zero[i][j]) cnt++;
                else cnt = 0;
                dp[i][j] = Math.min(dp[i][j], cnt);
            }
        }

        // right
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (!zero[i][j]) cnt++;
                else cnt = 0;
                dp[i][j] = Math.min(dp[i][j], cnt);
            }
        }

        // top
        for (int j = 0; j < n; j++) {
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (!zero[i][j]) cnt++;
                else cnt = 0;
                dp[i][j] = Math.min(dp[i][j], cnt);
            }
        }

        // bottom and compute answer
        int ans = 0;
        for (int j = 0; j < n; j++) {
            int cnt = 0;
            for (int i = n - 1; i >= 0; i--) {
                if (!zero[i][j]) cnt++;
                else cnt = 0;
                dp[i][j] = Math.min(dp[i][j], cnt);
                ans = Math.max(ans, dp[i][j]);
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mine_set = set((x, y) for x, y in mines)
        dp = [[n] * n for _ in range(n)]

        # Left & Right passes
        for i in range(n):
            cnt = 0
            for j in range(n):
                if (i, j) not in mine_set:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = min(dp[i][j], cnt)
            cnt = 0
            for j in range(n - 1, -1, -1):
                if (i, j) not in mine_set:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = min(dp[i][j], cnt)

        # Up & Down passes
        for j in range(n):
            cnt = 0
            for i in range(n):
                if (i, j) not in mine_set:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = min(dp[i][j], cnt)
            cnt = 0
            for i in range(n - 1, -1, -1):
                if (i, j) not in mine_set:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = min(dp[i][j], cnt)

        ans = 0
        for i in range(n):
            for j in range(n):
                ans = max(ans, dp[i][j])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Initialize grid with 1s
        grid = [[1] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0

        dp = [[n] * n for _ in range(n)]

        # Left pass
        for i in range(n):
            cnt = 0
            for j in range(n):
                if grid[i][j]:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = min(dp[i][j], cnt)

        # Right pass
        for i in range(n):
            cnt = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = min(dp[i][j], cnt)

        # Top pass
        for j in range(n):
            cnt = 0
            for i in range(n):
                if grid[i][j]:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = min(dp[i][j], cnt)

        # Bottom pass
        for j in range(n):
            cnt = 0
            for i in range(n - 1, -1, -1):
                if grid[i][j]:
                    cnt += 1
                else:
                    cnt = 0
                dp[i][j] = min(dp[i][j], cnt)

        ans = 0
        for i in range(n):
            for j in range(n):
                ans = max(ans, dp[i][j])
        return ans
```

## C

```c
#include <stdlib.h>

int orderOfLargestPlusSign(int n, int** mines, int minesSize, int* minesColSize) {
    if (n == 0) return 0;
    
    int total = n * n;
    int *grid = (int *)malloc(total * sizeof(int));
    int *dp   = (int *)malloc(total * sizeof(int));
    if (!grid || !dp) {
        free(grid);
        free(dp);
        return 0;
    }
    
    for (int i = 0; i < total; ++i) {
        grid[i] = 1;          // initially all ones
        dp[i]   = n;          // upper bound for arm length
    }
    
    for (int k = 0; k < minesSize; ++k) {
        int x = mines[k][0];
        int y = mines[k][1];
        grid[x * n + y] = 0;
        dp[x * n + y] = 0;    // zero cannot be center
    }
    
    // Left & Right passes
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        for (int j = 0; j < n; ++j) {               // left to right
            int idx = i * n + j;
            if (grid[idx]) cnt++;
            else cnt = 0;
            if (cnt < dp[idx]) dp[idx] = cnt;
        }
        cnt = 0;
        for (int j = n - 1; j >= 0; --j) {          // right to left
            int idx = i * n + j;
            if (grid[idx]) cnt++;
            else cnt = 0;
            if (cnt < dp[idx]) dp[idx] = cnt;
        }
    }
    
    // Up & Down passes
    for (int j = 0; j < n; ++j) {
        int cnt = 0;
        for (int i = 0; i < n; ++i) {               // top to bottom
            int idx = i * n + j;
            if (grid[idx]) cnt++;
            else cnt = 0;
            if (cnt < dp[idx]) dp[idx] = cnt;
        }
        cnt = 0;
        for (int i = n - 1; i >= 0; --i) {          // bottom to top
            int idx = i * n + j;
            if (grid[idx]) cnt++;
            else cnt = 0;
            if (cnt < dp[idx]) dp[idx] = cnt;
        }
    }
    
    int best = 0;
    for (int i = 0; i < total; ++i) {
        if (dp[i] > best) best = dp[i];
    }
    
    free(grid);
    free(dp);
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int OrderOfLargestPlusSign(int n, int[][] mines) {
        bool[,] grid = new bool[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i, j] = true;
            }
        }
        foreach (var m in mines) {
            int x = m[0], y = m[1];
            grid[x, y] = false;
        }

        int[,] dp = new int[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i, j] = n;
            }
        }

        // left
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i, j]) cnt++; else cnt = 0;
                dp[i, j] = Math.Min(dp[i, j], cnt);
            }
        }

        // right
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i, j]) cnt++; else cnt = 0;
                dp[i, j] = Math.Min(dp[i, j], cnt);
            }
        }

        // up
        for (int j = 0; j < n; j++) {
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (grid[i, j]) cnt++; else cnt = 0;
                dp[i, j] = Math.Min(dp[i, j], cnt);
            }
        }

        // down and find max
        int best = 0;
        for (int j = 0; j < n; j++) {
            int cnt = 0;
            for (int i = n - 1; i >= 0; i--) {
                if (grid[i, j]) cnt++; else cnt = 0;
                dp[i, j] = Math.Min(dp[i, j], cnt);
                if (dp[i, j] > best) best = dp[i, j];
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} mines
 * @return {number}
 */
var orderOfLargestPlusSign = function(n, mines) {
    const mineSet = new Set();
    for (const [x, y] of mines) {
        mineSet.add(`${x},${y}`);
    }
    
    // dp[r][c] will hold the minimal arm length (including center) among four directions
    const dp = Array.from({ length: n }, () => Array(n).fill(n));
    
    // Left to Right
    for (let r = 0; r < n; ++r) {
        let count = 0;
        for (let c = 0; c < n; ++c) {
            if (mineSet.has(`${r},${c}`)) {
                count = 0;
            } else {
                count += 1;
            }
            dp[r][c] = Math.min(dp[r][c], count);
        }
    }
    
    // Right to Left
    for (let r = 0; r < n; ++r) {
        let count = 0;
        for (let c = n - 1; c >= 0; --c) {
            if (mineSet.has(`${r},${c}`)) {
                count = 0;
            } else {
                count += 1;
            }
            dp[r][c] = Math.min(dp[r][c], count);
        }
    }
    
    // Top to Bottom
    for (let c = 0; c < n; ++c) {
        let count = 0;
        for (let r = 0; r < n; ++r) {
            if (mineSet.has(`${r},${c}`)) {
                count = 0;
            } else {
                count += 1;
            }
            dp[r][c] = Math.min(dp[r][c], count);
        }
    }
    
    // Bottom to Top
    for (let c = 0; c < n; ++c) {
        let count = 0;
        for (let r = n - 1; r >= 0; --r) {
            if (mineSet.has(`${r},${c}`)) {
                count = 0;
            } else {
                count += 1;
            }
            dp[r][c] = Math.min(dp[r][c], count);
        }
    }
    
    let ans = 0;
    for (let r = 0; r < n; ++r) {
        for (let c = 0; c < n; ++c) {
            if (dp[r][c] > ans) ans = dp[r][c];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function orderOfLargestPlusSign(n: number, mines: number[][]): number {
    const grid = Array.from({ length: n }, () => Array(n).fill(1));
    for (const [x, y] of mines) {
        grid[x][y] = 0;
    }

    const left = Array.from({ length: n }, () => Array(n).fill(0));
    const right = Array.from({ length: n }, () => Array(n).fill(0));
    const up = Array.from({ length: n }, () => Array(n).fill(0));
    const down = Array.from({ length: n }, () => Array(n).fill(0));

    // left counts
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) cnt++;
            else cnt = 0;
            left[i][j] = cnt;
        }
    }

    // right counts
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = n - 1; j >= 0; j--) {
            if (grid[i][j] === 1) cnt++;
            else cnt = 0;
            right[i][j] = cnt;
        }
    }

    // up counts
    for (let j = 0; j < n; j++) {
        let cnt = 0;
        for (let i = 0; i < n; i++) {
            if (grid[i][j] === 1) cnt++;
            else cnt = 0;
            up[i][j] = cnt;
        }
    }

    // down counts
    for (let j = 0; j < n; j++) {
        let cnt = 0;
        for (let i = n - 1; i >= 0; i--) {
            if (grid[i][j] === 1) cnt++;
            else cnt = 0;
            down[i][j] = cnt;
        }
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const order = Math.min(left[i][j], right[i][j], up[i][j], down[i][j]);
            if (order > ans) ans = order;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $mines
     * @return Integer
     */
    function orderOfLargestPlusSign($n, $mines) {
        // Initialize grid with 1s
        $grid = array_fill(0, $n, array_fill(0, $n, 1));
        foreach ($mines as $mine) {
            $x = $mine[0];
            $y = $mine[1];
            $grid[$x][$y] = 0;
        }

        // dp holds the minimal arm length (including center) for each cell
        $dp = array_fill(0, $n, array_fill(0, $n, $n));

        // Left direction
        for ($i = 0; $i < $n; ++$i) {
            $cnt = 0;
            for ($j = 0; $j < $n; ++$j) {
                if ($grid[$i][$j] == 1) {
                    $cnt++;
                } else {
                    $cnt = 0;
                }
                $dp[$i][$j] = min($dp[$i][$j], $cnt);
            }
        }

        // Right direction
        for ($i = 0; $i < $n; ++$i) {
            $cnt = 0;
            for ($j = $n - 1; $j >= 0; --$j) {
                if ($grid[$i][$j] == 1) {
                    $cnt++;
                } else {
                    $cnt = 0;
                }
                $dp[$i][$j] = min($dp[$i][$j], $cnt);
            }
        }

        // Up direction
        for ($j = 0; $j < $n; ++$j) {
            $cnt = 0;
            for ($i = 0; $i < $n; ++$i) {
                if ($grid[$i][$j] == 1) {
                    $cnt++;
                } else {
                    $cnt = 0;
                }
                $dp[$i][$j] = min($dp[$i][$j], $cnt);
            }
        }

        // Down direction
        for ($j = 0; $j < $n; ++$j) {
            $cnt = 0;
            for ($i = $n - 1; $i >= 0; --$i) {
                if ($grid[$i][$j] == 1) {
                    $cnt++;
                } else {
                    $cnt = 0;
                }
                $dp[$i][$j] = min($dp[$i][$j], $cnt);
            }
        }

        // Find maximum order
        $maxOrder = 0;
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($dp[$i][$j] > $maxOrder) {
                    $maxOrder = $dp[$i][$j];
                }
            }
        }

        return $maxOrder;
    }
}
```

## Swift

```swift
class Solution {
    func orderOfLargestPlusSign(_ n: Int, _ mines: [[Int]]) -> Int {
        if n == 0 { return 0 }
        var isOne = Array(repeating: Array(repeating: true, count: n), count: n)
        for m in mines {
            let x = m[0], y = m[1]
            isOne[x][y] = false
        }
        var dp = Array(repeating: Array(repeating: n, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n {
                if !isOne[i][j] { dp[i][j] = 0 }
            }
        }
        // left
        for i in 0..<n {
            var cnt = 0
            for j in 0..<n {
                if isOne[i][j] { cnt += 1 } else { cnt = 0 }
                dp[i][j] = min(dp[i][j], cnt)
            }
        }
        // right
        for i in 0..<n {
            var cnt = 0
            for j in stride(from: n - 1, through: 0, by: -1) {
                if isOne[i][j] { cnt += 1 } else { cnt = 0 }
                dp[i][j] = min(dp[i][j], cnt)
            }
        }
        // top
        for j in 0..<n {
            var cnt = 0
            for i in 0..<n {
                if isOne[i][j] { cnt += 1 } else { cnt = 0 }
                dp[i][j] = min(dp[i][j], cnt)
            }
        }
        // bottom
        for j in 0..<n {
            var cnt = 0
            for i in stride(from: n - 1, through: 0, by: -1) {
                if isOne[i][j] { cnt += 1 } else { cnt = 0 }
                dp[i][j] = min(dp[i][j], cnt)
            }
        }
        var ans = 0
        for i in 0..<n {
            for j in 0..<n {
                if dp[i][j] > ans { ans = dp[i][j] }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun orderOfLargestPlusSign(n: Int, mines: Array<IntArray>): Int {
        val grid = Array(n) { BooleanArray(n) { true } }
        for (mine in mines) {
            grid[mine[0]][mine[1]] = false
        }

        val dp = Array(n) { IntArray(n) { n } }

        // Horizontal passes
        for (i in 0 until n) {
            var count = 0
            for (j in 0 until n) {
                if (grid[i][j]) {
                    count++
                } else {
                    count = 0
                }
                dp[i][j] = minOf(dp[i][j], count)
            }
            count = 0
            for (j in n - 1 downTo 0) {
                if (grid[i][j]) {
                    count++
                } else {
                    count = 0
                }
                dp[i][j] = minOf(dp[i][j], count)
            }
        }

        // Vertical passes
        for (j in 0 until n) {
            var count = 0
            for (i in 0 until n) {
                if (grid[i][j]) {
                    count++
                } else {
                    count = 0
                }
                dp[i][j] = minOf(dp[i][j], count)
            }
            count = 0
            for (i in n - 1 downTo 0) {
                if (grid[i][j]) {
                    count++
                } else {
                    count = 0
                }
                dp[i][j] = minOf(dp[i][j], count)
            }
        }

        var answer = 0
        for (i in 0 until n) {
            for (j in 0 until n) {
                answer = maxOf(answer, dp[i][j])
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int orderOfLargestPlusSign(int n, List<List<int>> mines) {
    // Initialize grid with all ones
    List<List<int>> grid = List.generate(n, (_) => List.filled(n, 1));
    for (var m in mines) {
      int x = m[0];
      int y = m[1];
      grid[x][y] = 0;
    }

    // Directional counts
    List<List<int>> left = List.generate(n, (_) => List.filled(n, 0));
    List<List<int>> right = List.generate(n, (_) => List.filled(n, 0));
    List<List<int>> up = List.generate(n, (_) => List.filled(n, 0));
    List<List<int>> down = List.generate(n, (_) => List.filled(n, 0));

    // Left counts
    for (int i = 0; i < n; i++) {
      int cnt = 0;
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          cnt++;
        } else {
          cnt = 0;
        }
        left[i][j] = cnt;
      }
    }

    // Right counts
    for (int i = 0; i < n; i++) {
      int cnt = 0;
      for (int j = n - 1; j >= 0; j--) {
        if (grid[i][j] == 1) {
          cnt++;
        } else {
          cnt = 0;
        }
        right[i][j] = cnt;
      }
    }

    // Up counts
    for (int j = 0; j < n; j++) {
      int cnt = 0;
      for (int i = 0; i < n; i++) {
        if (grid[i][j] == 1) {
          cnt++;
        } else {
          cnt = 0;
        }
        up[i][j] = cnt;
      }
    }

    // Down counts
    for (int j = 0; j < n; j++) {
      int cnt = 0;
      for (int i = n - 1; i >= 0; i--) {
        if (grid[i][j] == 1) {
          cnt++;
        } else {
          cnt = 0;
        }
        down[i][j] = cnt;
      }
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int order = left[i][j];
        if (right[i][j] < order) order = right[i][j];
        if (up[i][j] < order) order = up[i][j];
        if (down[i][j] < order) order = down[i][j];
        if (order > ans) ans = order;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func orderOfLargestPlusSign(n int, mines [][]int) int {
    // Initialize grid with all 1's (true)
    grid := make([][]bool, n)
    for i := 0; i < n; i++ {
        row := make([]bool, n)
        for j := 0; j < n; j++ {
            row[j] = true
        }
        grid[i] = row
    }
    // Apply mines (set to 0 / false)
    for _, m := range mines {
        x, y := m[0], m[1]
        grid[x][y] = false
    }

    // dp holds the minimal arm length (including center) for each cell
    dp := make([][]int, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]int, n)
        for j := 0; j < n; j++ {
            dp[i][j] = n // maximum possible value
        }
    }

    // Horizontal passes: left-to-right and right-to-left
    for i := 0; i < n; i++ {
        cnt := 0
        for j := 0; j < n; j++ {
            if grid[i][j] {
                cnt++
            } else {
                cnt = 0
            }
            if cnt < dp[i][j] {
                dp[i][j] = cnt
            }
        }
        cnt = 0
        for j := n - 1; j >= 0; j-- {
            if grid[i][j] {
                cnt++
            } else {
                cnt = 0
            }
            if cnt < dp[i][j] {
                dp[i][j] = cnt
            }
        }
    }

    // Vertical passes: top-to-bottom and bottom-to-top
    for j := 0; j < n; j++ {
        cnt := 0
        for i := 0; i < n; i++ {
            if grid[i][j] {
                cnt++
            } else {
                cnt = 0
            }
            if cnt < dp[i][j] {
                dp[i][j] = cnt
            }
        }
        cnt = 0
        for i := n - 1; i >= 0; i-- {
            if grid[i][j] {
                cnt++
            } else {
                cnt = 0
            }
            if cnt < dp[i][j] {
                dp[i][j] = cnt
            }
        }
    }

    // Find the maximum order among all cells
    ans := 0
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if dp[i][j] > ans {
                ans = dp[i][j]
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def order_of_largest_plus_sign(n, mines)
  grid = Array.new(n) { Array.new(n, true) }
  mines.each do |x, y|
    grid[x][y] = false
  end

  dp = Array.new(n) { Array.new(n, n) }

  # left
  (0...n).each do |r|
    cnt = 0
    (0...n).each do |c|
      if grid[r][c]
        cnt += 1
      else
        cnt = 0
      end
      dp[r][c] = cnt if cnt < dp[r][c]
    end
  end

  # right
  (0...n).each do |r|
    cnt = 0
    (n - 1).downto(0) do |c|
      if grid[r][c]
        cnt += 1
      else
        cnt = 0
      end
      dp[r][c] = cnt if cnt < dp[r][c]
    end
  end

  # up
  (0...n).each do |c|
    cnt = 0
    (0...n).each do |r|
      if grid[r][c]
        cnt += 1
      else
        cnt = 0
      end
      dp[r][c] = cnt if cnt < dp[r][c]
    end
  end

  # down
  (0...n).each do |c|
    cnt = 0
    (n - 1).downto(0) do |r|
      if grid[r][c]
        cnt += 1
      else
        cnt = 0
      end
      dp[r][c] = cnt if cnt < dp[r][c]
    end
  end

  max_order = 0
  (0...n).each do |r|
    (0...n).each do |c|
      max_order = dp[r][c] if dp[r][c] > max_order
    end
  end
  max_order
end
```

## Scala

```scala
object Solution {
    def orderOfLargestPlusSign(n: Int, mines: Array[Array[Int]]): Int = {
        val grid = Array.fill(n)(Array.fill(n)(true))
        for (m <- mines) {
            grid(m(0))(m(1)) = false
        }
        val dp = Array.ofDim[Int](n, n)
        for (i <- 0 until n; j <- 0 until n) dp(i)(j) = n

        // left
        for (i <- 0 until n) {
            var cnt = 0
            for (j <- 0 until n) {
                if (grid(i)(j)) cnt += 1 else cnt = 0
                dp(i)(j) = math.min(dp(i)(j), cnt)
            }
        }

        // right
        for (i <- 0 until n) {
            var cnt = 0
            for (j <- (n - 1) to 0 by -1) {
                if (grid(i)(j)) cnt += 1 else cnt = 0
                dp(i)(j) = math.min(dp(i)(j), cnt)
            }
        }

        // up
        for (j <- 0 until n) {
            var cnt = 0
            for (i <- 0 until n) {
                if (grid(i)(j)) cnt += 1 else cnt = 0
                dp(i)(j) = math.min(dp(i)(j), cnt)
            }
        }

        // down
        for (j <- 0 until n) {
            var cnt = 0
            for (i <- (n - 1) to 0 by -1) {
                if (grid(i)(j)) cnt += 1 else cnt = 0
                dp(i)(j) = math.min(dp(i)(j), cnt)
            }
        }

        var ans = 0
        for (i <- 0 until n; j <- 0 until n) {
            if (dp(i)(j) > ans) ans = dp(i)(j)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn order_of_largest_plus_sign(n: i32, mines: Vec<Vec<i32>>) -> i32 {
        let size = n as usize;
        let mut grid = vec![vec![true; size]; size];
        for m in mines.iter() {
            let x = m[0] as usize;
            let y = m[1] as usize;
            grid[x][y] = false;
        }

        let mut dp = vec![vec![n; size]; size]; // initialize with maximum possible arm length

        // left pass
        for r in 0..size {
            let mut cnt = 0i32;
            for c in 0..size {
                if grid[r][c] {
                    cnt += 1;
                } else {
                    cnt = 0;
                }
                dp[r][c] = dp[r][c].min(cnt);
            }
        }

        // right pass
        for r in 0..size {
            let mut cnt = 0i32;
            for c in (0..size).rev() {
                if grid[r][c] {
                    cnt += 1;
                } else {
                    cnt = 0;
                }
                dp[r][c] = dp[r][c].min(cnt);
            }
        }

        // up pass
        for c in 0..size {
            let mut cnt = 0i32;
            for r in 0..size {
                if grid[r][c] {
                    cnt += 1;
                } else {
                    cnt = 0;
                }
                dp[r][c] = dp[r][c].min(cnt);
            }
        }

        // down pass
        for c in 0..size {
            let mut cnt = 0i32;
            for r in (0..size).rev() {
                if grid[r][c] {
                    cnt += 1;
                } else {
                    cnt = 0;
                }
                dp[r][c] = dp[r][c].min(cnt);
            }
        }

        let mut ans = 0i32;
        for r in 0..size {
            for c in 0..size {
                if dp[r][c] > ans {
                    ans = dp[r][c];
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (order-of-largest-plus-sign n mines)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((grid (let ((g (make-vector n)))
                 (for ([i (in-range n)])
                   (vector-set! g i (make-vector n 1)))
                 g))
         (dp   (let ((d (make-vector n)))
                 (for ([i (in-range n)])
                   (vector-set! d i (make-vector n n))) ; initialize with max possible
                 d)))
    ;; place mines
    (for ([m mines])
      (define x (first m))
      (define y (second m))
      (vector-set! (vector-ref grid x) y 0))
    ;; left pass
    (for ([r (in-range n)])
      (let ((row (vector-ref grid r))
            (dp-row (vector-ref dp r)))
        (define cnt 0)
        (for ([c (in-range n)])
          (if (= (vector-ref row c) 1)
              (begin
                (set! cnt (+ cnt 1))
                (vector-set! dp-row c cnt))
              (begin
                (set! cnt 0)
                (vector-set! dp-row c 0))))))
    ;; right pass
    (for ([r (in-range n)])
      (let ((row (vector-ref grid r))
            (dp-row (vector-ref dp r)))
        (define cnt 0)
        (for ([c (in-range (- n 1) -1 -1)])
          (if (= (vector-ref row c) 1)
              (begin
                (set! cnt (+ cnt 1))
                (let ((prev (vector-ref dp-row c)))
                  (vector-set! dp-row c (min prev cnt))))
              (begin
                (set! cnt 0)
                (vector-set! dp-row c 0))))))
    ;; up pass
    (for ([c (in-range n)])
      (define cnt 0)
      (for ([r (in-range n)])
        (let* ((cell (vector-ref (vector-ref grid r) c))
               (dp-cell (vector-ref (vector-ref dp r) c)))
          (if (= cell 1)
              (begin
                (set! cnt (+ cnt 1))
                (vector-set! (vector-ref dp r) c (min dp-cell cnt)))
              (begin
                (set! cnt 0)
                (vector-set! (vector-ref dp r) c 0))))))
    ;; down pass
    (for ([c (in-range n)])
      (define cnt 0)
      (for ([r (in-range (- n 1) -1 -1)])
        (let* ((cell (vector-ref (vector-ref grid r) c))
               (dp-cell (vector-ref (vector-ref dp r) c)))
          (if (= cell 1)
              (begin
                (set! cnt (+ cnt 1))
                (vector-set! (vector-ref dp r) c (min dp-cell cnt)))
              (begin
                (set! cnt 0)
                (vector-set! (vector-ref dp r) c 0))))))
    ;; find maximum order
    (define ans 0)
    (for ([r (in-range n)])
      (for ([c (in-range n)])
        (let ((v (vector-ref (vector-ref dp r) c)))
          (when (> v ans) (set! ans v)))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([order_of_largest_plus_sign/2]).

-spec order_of_largest_plus_sign(integer(), [[integer()]]) -> integer().
order_of_largest_plus_sign(N, Mines) ->
    ZeroSet = maps:from_list([{ {R, C}, true } || [R, C] <- Mines]),
    InitVal = N,
    RowTemplate = array:new(N, {default, InitVal}),
    Rows = lists:map(fun(_)-> RowTemplate end, lists:seq(1, N)),
    DP0 = array:from_list(Rows),
    UpCounts0 = array:new(N, {default, 0}),
    {DP1, _UpCounts} = first_pass(0, N, ZeroSet, DP0, UpCounts0),
    DownCounts0 = array:new(N, {default, 0}),
    MaxOrder = second_pass(N - 1, N, ZeroSet, DP1, DownCounts0, 0),
    MaxOrder.

%% First pass: left and up directions
first_pass(R, N, _ZS, DP, Up) when R == N ->
    {DP, Up};
first_pass(R, N, ZS, DP0, Up0) ->
    {DP1, Up1} = process_row_left_up(R, 0, N, ZS, DP0, Up0, 0),
    first_pass(R + 1, N, ZS, DP1, Up1).

process_row_left_up(_R, C, N, _ZS, DP, Up, _Left) when C == N ->
    {DP, Up};
process_row_left_up(R, C, N, ZS, DPAcc, UpAcc, LeftPrev) ->
    IsMine = maps:is_key({R, C}, ZS),
    NewLeft = if IsMine -> 0; true -> LeftPrev + 1 end,
    UpPrev = array:get(C + 1, UpAcc),
    NewUp = if IsMine -> 0; true -> UpPrev + 1 end,
    UpTmp = array:set(C + 1, NewUp, UpAcc),
    Curr = get(DPAcc, R, C),
    MinVal = erlang:min(Curr, erlang:min(NewLeft, NewUp)),
    DPNew = set(DPAcc, R, C, MinVal),
    process_row_left_up(R, C + 1, N, ZS, DPNew, UpTmp, NewLeft).

%% Second pass: right and down directions, also compute answer
second_pass(R, _N, _ZS, DP, _Down, Max) when R < 0 ->
    Max;
second_pass(R, N, ZS, DP0, Down0, Max0) ->
    {DP1, Down1, Max1} = process_row_right_down(R, N - 1, N, ZS, DP0, Down0, 0, Max0),
    second_pass(R - 1, N, ZS, DP1, Down1, Max1).

process_row_right_down(_R, C, _N, _ZS, DP, Down, _Right, Max) when C < 0 ->
    {DP, Down, Max};
process_row_right_down(R, C, N, ZS, DPAcc, DownAcc, RightPrev, MaxAcc) ->
    IsMine = maps:is_key({R, C}, ZS),
    NewRight = if IsMine -> 0; true -> RightPrev + 1 end,
    DownPrev = array:get(C + 1, DownAcc),
    NewDown = if IsMine -> 0; true -> DownPrev + 1 end,
    DownTmp = array:set(C + 1, NewDown, DownAcc),
    Curr = get(DPAcc, R, C),
    MinVal = erlang:min(Curr, erlang:min(NewRight, NewDown)),
    DPNew = set(DPAcc, R, C, MinVal),
    MaxNew = erlang:max(MaxAcc, MinVal),
    process_row_right_down(R, C - 1, N, ZS, DPNew, DownTmp, NewRight, MaxNew).

%% Helpers to get and set values in the 2D array
get(DP, R, C) ->
    RowArr = array:get(R + 1, DP),
    array:get(C + 1, RowArr).

set(DP, R, C, Val) ->
    RowIdx = R + 1,
    ColIdx = C + 1,
    RowArr = array:get(RowIdx, DP),
    NewRow = array:set(ColIdx, Val, RowArr),
    array:set(RowIdx, NewRow, DP).
```

## Elixir

```elixir
defmodule Solution do
  @spec order_of_largest_plus_sign(n :: integer, mines :: [[integer]]) :: integer
  def order_of_largest_plus_sign(n, mines) do
    total = n * n

    # grid: 1 for empty cell, 0 for mine
    grid =
      Enum.reduce(mines, :array.new(total, default: 1), fn [r, c], acc ->
        idx = r * n + c
        :array.set(idx, 0, acc)
      end)

    # dp stores the minimal arm length seen so far for each cell
    dp = :array.new(total, default: n)

    # left pass
    dp =
      Enum.reduce(0..(n - 1), dp, fn r, dp_acc ->
        {_, dp_new} =
          Enum.reduce(0..(n - 1), {0, dp_acc}, fn c, {cnt, dp_inner} ->
            idx = r * n + c

            cnt =
              if :array.get(idx, grid) == 0 do
                0
              else
                cnt + 1
              end

            cur = :array.get(idx, dp_inner)
            new_min = if cur < cnt, do: cur, else: cnt
            {cnt, :array.set(idx, new_min, dp_inner)}
          end)

        dp_new
      end)

    # right pass
    cols_rev = Enum.to_list(0..(n - 1)) |> Enum.reverse()

    dp =
      Enum.reduce(0..(n - 1), dp, fn r, dp_acc ->
        {_, dp_new} =
          Enum.reduce(cols_rev, {0, dp_acc}, fn c, {cnt, dp_inner} ->
            idx = r * n + c

            cnt =
              if :array.get(idx, grid) == 0 do
                0
              else
                cnt + 1
              end

            cur = :array.get(idx, dp_inner)
            new_min = if cur < cnt, do: cur, else: cnt
            {cnt, :array.set(idx, new_min, dp_inner)}
          end)

        dp_new
      end)

    # up pass
    dp =
      Enum.reduce(0..(n - 1), dp, fn c, dp_acc ->
        {_, dp_new} =
          Enum.reduce(0..(n - 1), {0, dp_acc}, fn r, {cnt, dp_inner} ->
            idx = r * n + c

            cnt =
              if :array.get(idx, grid) == 0 do
                0
              else
                cnt + 1
              end

            cur = :array.get(idx, dp_inner)
            new_min = if cur < cnt, do: cur, else: cnt
            {cnt, :array.set(idx, new_min, dp_inner)}
          end)

        dp_new
      end)

    # down pass
    rows_rev = Enum.to_list(0..(n - 1)) |> Enum.reverse()

    dp =
      Enum.reduce(0..(n - 1), dp, fn c, dp_acc ->
        {_, dp_new} =
          Enum.reduce(rows_rev, {0, dp_acc}, fn r, {cnt, dp_inner} ->
            idx = r * n + c

            cnt =
              if :array.get(idx, grid) == 0 do
                0
              else
                cnt + 1
              end

            cur = :array.get(idx, dp_inner)
            new_min = if cur < cnt, do: cur, else: cnt
            {cnt, :array.set(idx, new_min, dp_inner)}
          end)

        dp_new
      end)

    # find maximum order
    Enum.reduce(0..(total - 1), 0, fn idx, acc ->
      val = :array.get(idx, dp)
      if val > acc, do: val, else: acc
    end)
  end
end
```

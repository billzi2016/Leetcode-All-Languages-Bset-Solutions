# 2257. Count Unguarded Cells in the Grid

## Cpp

```cpp
class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        const int UNGUARDED = 0;
        const int GUARDED = 1;
        const int GUARD = 2;
        const int WALL = 3;
        
        vector<vector<int>> grid(m, vector<int>(n, UNGUARDED));
        for (auto &g : guards) {
            grid[g[0]][g[1]] = GUARD;
        }
        for (auto &w : walls) {
            grid[w[0]][w[1]] = WALL;
        }
        
        // Row scans
        for (int i = 0; i < m; ++i) {
            bool seenGuard = false;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == GUARD) {
                    seenGuard = true;
                } else if (grid[i][j] == WALL) {
                    seenGuard = false;
                } else if (seenGuard && grid[i][j] == UNGUARDED) {
                    grid[i][j] = GUARDED;
                }
            }
            seenGuard = false;
            for (int j = n - 1; j >= 0; --j) {
                if (grid[i][j] == GUARD) {
                    seenGuard = true;
                } else if (grid[i][j] == WALL) {
                    seenGuard = false;
                } else if (seenGuard && grid[i][j] == UNGUARDED) {
                    grid[i][j] = GUARDED;
                }
            }
        }
        
        // Column scans
        for (int j = 0; j < n; ++j) {
            bool seenGuard = false;
            for (int i = 0; i < m; ++i) {
                if (grid[i][j] == GUARD) {
                    seenGuard = true;
                } else if (grid[i][j] == WALL) {
                    seenGuard = false;
                } else if (seenGuard && grid[i][j] == UNGUARDED) {
                    grid[i][j] = GUARDED;
                }
            }
            seenGuard = false;
            for (int i = m - 1; i >= 0; --i) {
                if (grid[i][j] == GUARD) {
                    seenGuard = true;
                } else if (grid[i][j] == WALL) {
                    seenGuard = false;
                } else if (seenGuard && grid[i][j] == UNGUARDED) {
                    grid[i][j] = GUARDED;
                }
            }
        }
        
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == UNGUARDED) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final int EMPTY = 0;
    private static final int GUARD = 1;
    private static final int WALL = 2;
    private static final int GUARDED = 3;

    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] grid = new int[m][n];

        for (int[] g : guards) {
            grid[g[0]][g[1]] = GUARD;
        }
        for (int[] w : walls) {
            grid[w[0]][w[1]] = WALL;
        }

        // Row scans
        for (int i = 0; i < m; i++) {
            boolean seenGuard = false;
            for (int j = 0; j < n; j++) {
                int cell = grid[i][j];
                if (cell == GUARD) {
                    seenGuard = true;
                } else if (cell == WALL) {
                    seenGuard = false;
                } else if (seenGuard && cell == EMPTY) {
                    grid[i][j] = GUARDED;
                }
            }
            seenGuard = false;
            for (int j = n - 1; j >= 0; j--) {
                int cell = grid[i][j];
                if (cell == GUARD) {
                    seenGuard = true;
                } else if (cell == WALL) {
                    seenGuard = false;
                } else if (seenGuard && cell == EMPTY) {
                    grid[i][j] = GUARDED;
                }
            }
        }

        // Column scans
        for (int j = 0; j < n; j++) {
            boolean seenGuard = false;
            for (int i = 0; i < m; i++) {
                int cell = grid[i][j];
                if (cell == GUARD) {
                    seenGuard = true;
                } else if (cell == WALL) {
                    seenGuard = false;
                } else if (seenGuard && cell == EMPTY) {
                    grid[i][j] = GUARDED;
                }
            }
            seenGuard = false;
            for (int i = m - 1; i >= 0; i--) {
                int cell = grid[i][j];
                if (cell == GUARD) {
                    seenGuard = true;
                } else if (cell == WALL) {
                    seenGuard = false;
                } else if (seenGuard && cell == EMPTY) {
                    grid[i][j] = GUARDED;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == EMPTY) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        # 0 = empty, 1 = guard, 2 = wall, 3 = guarded
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in (1, 2):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc

        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unguarded += 1
        return unguarded
```

## Python3

```python
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        GUARD = 2
        WALL = 3
        GUARDED = 1

        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = GUARD
        for r, c in walls:
            grid[r][c] = WALL

        # Row scans
        for i in range(m):
            seen = False
            for j in range(n):
                if grid[i][j] == GUARD:
                    seen = True
                elif grid[i][j] == WALL:
                    seen = False
                else:
                    if seen and grid[i][j] == 0:
                        grid[i][j] = GUARDED
            seen = False
            for j in range(n - 1, -1, -1):
                if grid[i][j] == GUARD:
                    seen = True
                elif grid[i][j] == WALL:
                    seen = False
                else:
                    if seen and grid[i][j] == 0:
                        grid[i][j] = GUARDED

        # Column scans
        for j in range(n):
            seen = False
            for i in range(m):
                if grid[i][j] == GUARD:
                    seen = True
                elif grid[i][j] == WALL:
                    seen = False
                else:
                    if seen and grid[i][j] == 0:
                        grid[i][j] = GUARDED
            seen = False
            for i in range(m - 1, -1, -1):
                if grid[i][j] == GUARD:
                    seen = True
                elif grid[i][j] == WALL:
                    seen = False
                else:
                    if seen and grid[i][j] == 0:
                        grid[i][j] = GUARDED

        # Count unguarded empty cells
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += 1
        return cnt
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int countUnguarded(int m, int n, int** guards, int guardsSize, int* guardsColSize,
                   int** walls, int wallsSize, int* wallsColSize) {
    int total = m * n;
    char *grid = (char *)calloc(total, sizeof(char)); // 0: empty, 1: guarded, 2: guard, 3: wall

    for (int i = 0; i < guardsSize; ++i) {
        int r = guards[i][0];
        int c = guards[i][1];
        grid[r * n + c] = 2;
    }
    for (int i = 0; i < wallsSize; ++i) {
        int r = walls[i][0];
        int c = walls[i][1];
        grid[r * n + c] = 3;
    }

    // Left to Right
    for (int i = 0; i < m; ++i) {
        bool seenGuard = false;
        for (int j = 0; j < n; ++j) {
            int idx = i * n + j;
            if (grid[idx] == 2) {
                seenGuard = true;
            } else if (grid[idx] == 3) {
                seenGuard = false;
            } else if (seenGuard && grid[idx] == 0) {
                grid[idx] = 1;
            }
        }
    }

    // Right to Left
    for (int i = 0; i < m; ++i) {
        bool seenGuard = false;
        for (int j = n - 1; j >= 0; --j) {
            int idx = i * n + j;
            if (grid[idx] == 2) {
                seenGuard = true;
            } else if (grid[idx] == 3) {
                seenGuard = false;
            } else if (seenGuard && grid[idx] == 0) {
                grid[idx] = 1;
            }
        }
    }

    // Top to Bottom
    for (int j = 0; j < n; ++j) {
        bool seenGuard = false;
        for (int i = 0; i < m; ++i) {
            int idx = i * n + j;
            if (grid[idx] == 2) {
                seenGuard = true;
            } else if (grid[idx] == 3) {
                seenGuard = false;
            } else if (seenGuard && grid[idx] == 0) {
                grid[idx] = 1;
            }
        }
    }

    // Bottom to Top
    for (int j = 0; j < n; ++j) {
        bool seenGuard = false;
        for (int i = m - 1; i >= 0; --i) {
            int idx = i * n + j;
            if (grid[idx] == 2) {
                seenGuard = true;
            } else if (grid[idx] == 3) {
                seenGuard = false;
            } else if (seenGuard && grid[idx] == 0) {
                grid[idx] = 1;
            }
        }
    }

    int unguarded = 0;
    for (int i = 0; i < total; ++i) {
        if (grid[i] == 0) {
            ++unguarded;
        }
    }

    free(grid);
    return unguarded;
}
```

## Csharp

```csharp
public class Solution {
    public int CountUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[,] grid = new int[m, n]; // 0: empty, 1: guarded, 2: guard, 3: wall

        foreach (var g in guards) {
            grid[g[0], g[1]] = 2;
        }
        foreach (var w in walls) {
            grid[w[0], w[1]] = 3;
        }

        // Row scans
        for (int i = 0; i < m; i++) {
            bool seenGuard = false;
            for (int j = 0; j < n; j++) {
                int cell = grid[i, j];
                if (cell == 2) {
                    seenGuard = true;
                } else if (cell == 3) {
                    seenGuard = false;
                } else if (seenGuard && cell == 0) {
                    grid[i, j] = 1;
                }
            }
            seenGuard = false;
            for (int j = n - 1; j >= 0; j--) {
                int cell = grid[i, j];
                if (cell == 2) {
                    seenGuard = true;
                } else if (cell == 3) {
                    seenGuard = false;
                } else if (seenGuard && cell == 0) {
                    grid[i, j] = 1;
                }
            }
        }

        // Column scans
        for (int j = 0; j < n; j++) {
            bool seenGuard = false;
            for (int i = 0; i < m; i++) {
                int cell = grid[i, j];
                if (cell == 2) {
                    seenGuard = true;
                } else if (cell == 3) {
                    seenGuard = false;
                } else if (seenGuard && cell == 0) {
                    grid[i, j] = 1;
                }
            }
            seenGuard = false;
            for (int i = m - 1; i >= 0; i--) {
                int cell = grid[i, j];
                if (cell == 2) {
                    seenGuard = true;
                } else if (cell == 3) {
                    seenGuard = false;
                } else if (seenGuard && cell == 0) {
                    grid[i, j] = 1;
                }
            }
        }

        int unguarded = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i, j] == 0) unguarded++;
            }
        }

        return unguarded;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} guards
 * @param {number[][]} walls
 * @return {number}
 */
var countUnguarded = function(m, n, guards, walls) {
    const UNGUARDED = 0;
    const GUARDED = 1;
    const GUARD = 2;
    const WALL = 3;

    // initialize grid
    const grid = Array.from({ length: m }, () => new Uint8Array(n));

    for (const [r, c] of guards) {
        grid[r][c] = GUARD;
    }
    for (const [r, c] of walls) {
        grid[r][c] = WALL;
    }

    // Row scans
    for (let i = 0; i < m; ++i) {
        let seen = false;
        for (let j = 0; j < n; ++j) {
            const cell = grid[i][j];
            if (cell === GUARD) {
                seen = true;
            } else if (cell === WALL) {
                seen = false;
            } else if (seen) {
                grid[i][j] = GUARDED;
            }
        }
        seen = false;
        for (let j = n - 1; j >= 0; --j) {
            const cell = grid[i][j];
            if (cell === GUARD) {
                seen = true;
            } else if (cell === WALL) {
                seen = false;
            } else if (seen) {
                grid[i][j] = GUARDED;
            }
        }
    }

    // Column scans
    for (let j = 0; j < n; ++j) {
        let seen = false;
        for (let i = 0; i < m; ++i) {
            const cell = grid[i][j];
            if (cell === GUARD) {
                seen = true;
            } else if (cell === WALL) {
                seen = false;
            } else if (seen) {
                grid[i][j] = GUARDED;
            }
        }
        seen = false;
        for (let i = m - 1; i >= 0; --i) {
            const cell = grid[i][j];
            if (cell === GUARD) {
                seen = true;
            } else if (cell === WALL) {
                seen = false;
            } else if (seen) {
                grid[i][j] = GUARDED;
            }
        }
    }

    // Count unguarded cells
    let count = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === UNGUARDED) {
                ++count;
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    const EMPTY = 0;
    const GUARD = 1;
    const WALL = 2;
    const GUARDED = 3;

    const grid: number[][] = Array.from({ length: m }, () => Array(n).fill(EMPTY));

    for (const [r, c] of guards) {
        grid[r][c] = GUARD;
    }
    for (const [r, c] of walls) {
        grid[r][c] = WALL;
    }

    // Row scans
    for (let i = 0; i < m; i++) {
        let seen = false;
        for (let j = 0; j < n; j++) {
            const cell = grid[i][j];
            if (cell === GUARD) {
                seen = true;
            } else if (cell === WALL) {
                seen = false;
            } else if (seen && cell === EMPTY) {
                grid[i][j] = GUARDED;
            }
        }
        seen = false;
        for (let j = n - 1; j >= 0; j--) {
            const cell = grid[i][j];
            if (cell === GUARD) {
                seen = true;
            } else if (cell === WALL) {
                seen = false;
            } else if (seen && cell === EMPTY) {
                grid[i][j] = GUARDED;
            }
        }
    }

    // Column scans
    for (let j = 0; j < n; j++) {
        let seen = false;
        for (let i = 0; i < m; i++) {
            const cell = grid[i][j];
            if (cell === GUARD) {
                seen = true;
            } else if (cell === WALL) {
                seen = false;
            } else if (seen && cell === EMPTY) {
                grid[i][j] = GUARDED;
            }
        }
        seen = false;
        for (let i = m - 1; i >= 0; i--) {
            const cell = grid[i][j];
            if (cell === GUARD) {
                seen = true;
            } else if (cell === WALL) {
                seen = false;
            } else if (seen && cell === EMPTY) {
                grid[i][j] = GUARDED;
            }
        }
    }

    let count = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === EMPTY) {
                count++;
            }
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $guards
     * @param Integer[][] $walls
     * @return Integer
     */
    function countUnguarded($m, $n, $guards, $walls) {
        // 0 = empty, 1 = guard, 2 = wall, 3 = guarded
        $grid = array_fill(0, $m, []);
        for ($i = 0; $i < $m; $i++) {
            $grid[$i] = array_fill(0, $n, 0);
        }

        foreach ($guards as $g) {
            $r = $g[0];
            $c = $g[1];
            $grid[$r][$c] = 1;
        }
        foreach ($walls as $w) {
            $r = $w[0];
            $c = $w[1];
            $grid[$r][$c] = 2;
        }

        // Horizontal passes
        for ($i = 0; $i < $m; $i++) {
            $hasGuard = false;
            for ($j = 0; $j < $n; $j++) {
                $cell = $grid[$i][$j];
                if ($cell == 1) {          // guard
                    $hasGuard = true;
                } elseif ($cell == 2) {    // wall
                    $hasGuard = false;
                } else {
                    if ($hasGuard && $cell == 0) {
                        $grid[$i][$j] = 3; // guarded
                    }
                }
            }
            $hasGuard = false;
            for ($j = $n - 1; $j >= 0; $j--) {
                $cell = $grid[$i][$j];
                if ($cell == 1) {
                    $hasGuard = true;
                } elseif ($cell == 2) {
                    $hasGuard = false;
                } else {
                    if ($hasGuard && $cell == 0) {
                        $grid[$i][$j] = 3;
                    }
                }
            }
        }

        // Vertical passes
        for ($j = 0; $j < $n; $j++) {
            $hasGuard = false;
            for ($i = 0; $i < $m; $i++) {
                $cell = $grid[$i][$j];
                if ($cell == 1) {
                    $hasGuard = true;
                } elseif ($cell == 2) {
                    $hasGuard = false;
                } else {
                    if ($hasGuard && $cell == 0) {
                        $grid[$i][$j] = 3;
                    }
                }
            }
            $hasGuard = false;
            for ($i = $m - 1; $i >= 0; $i--) {
                $cell = $grid[$i][$j];
                if ($cell == 1) {
                    $hasGuard = true;
                } elseif ($cell == 2) {
                    $hasGuard = false;
                } else {
                    if ($hasGuard && $cell == 0) {
                        $grid[$i][$j] = 3;
                    }
                }
            }
        }

        // Count unguarded empty cells
        $count = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 0) {
                    $count++;
                }
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countUnguarded(_ m: Int, _ n: Int, _ guards: [[Int]], _ walls: [[Int]]) -> Int {
        let total = m * n
        var grid = [UInt8](repeating: 0, count: total)
        
        let EMPTY: UInt8 = 0
        let GUARDED: UInt8 = 1
        let GUARD: UInt8 = 2
        let WALL: UInt8 = 3
        
        func idx(_ r: Int, _ c: Int) -> Int { r * n + c }
        
        for g in guards {
            grid[idx(g[0], g[1])] = GUARD
        }
        for w in walls {
            grid[idx(w[0], w[1])] = WALL
        }
        
        // Row sweeps
        for r in 0..<m {
            var seenGuard = false
            // left to right
            for c in 0..<n {
                let i = idx(r, c)
                let cell = grid[i]
                if cell == GUARD {
                    seenGuard = true
                } else if cell == WALL {
                    seenGuard = false
                } else if seenGuard && cell == EMPTY {
                    grid[i] = GUARDED
                }
            }
            // right to left
            seenGuard = false
            for c in stride(from: n - 1, through: 0, by: -1) {
                let i = idx(r, c)
                let cell = grid[i]
                if cell == GUARD {
                    seenGuard = true
                } else if cell == WALL {
                    seenGuard = false
                } else if seenGuard && cell == EMPTY {
                    grid[i] = GUARDED
                }
            }
        }
        
        // Column sweeps
        for c in 0..<n {
            var seenGuard = false
            // top to bottom
            for r in 0..<m {
                let i = idx(r, c)
                let cell = grid[i]
                if cell == GUARD {
                    seenGuard = true
                } else if cell == WALL {
                    seenGuard = false
                } else if seenGuard && cell == EMPTY {
                    grid[i] = GUARDED
                }
            }
            // bottom to top
            seenGuard = false
            for r in stride(from: m - 1, through: 0, by: -1) {
                let i = idx(r, c)
                let cell = grid[i]
                if cell == GUARD {
                    seenGuard = true
                } else if cell == WALL {
                    seenGuard = false
                } else if seenGuard && cell == EMPTY {
                    grid[i] = GUARDED
                }
            }
        }
        
        var count = 0
        for v in grid where v == EMPTY {
            count += 1
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countUnguarded(m: Int, n: Int, guards: Array<IntArray>, walls: Array<IntArray>): Int {
        val grid = Array(m) { IntArray(n) }
        for (g in guards) {
            grid[g[0]][g[1]] = 1 // guard
        }
        for (w in walls) {
            grid[w[0]][w[1]] = 2 // wall
        }

        // Row scans
        for (i in 0 until m) {
            var seenGuard = false
            for (j in 0 until n) {
                when (grid[i][j]) {
                    1 -> seenGuard = true
                    2 -> seenGuard = false
                    else -> if (seenGuard) grid[i][j] = 3
                }
            }
            seenGuard = false
            for (j in n - 1 downTo 0) {
                when (grid[i][j]) {
                    1 -> seenGuard = true
                    2 -> seenGuard = false
                    else -> if (seenGuard) grid[i][j] = 3
                }
            }
        }

        // Column scans
        for (j in 0 until n) {
            var seenGuard = false
            for (i in 0 until m) {
                when (grid[i][j]) {
                    1 -> seenGuard = true
                    2 -> seenGuard = false
                    else -> if (seenGuard) grid[i][j] = 3
                }
            }
            seenGuard = false
            for (i in m - 1 downTo 0) {
                when (grid[i][j]) {
                    1 -> seenGuard = true
                    2 -> seenGuard = false
                    else -> if (seenGuard) grid[i][j] = 3
                }
            }
        }

        var count = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 0) count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countUnguarded(int m, int n, List<List<int>> guards, List<List<int>> walls) {
    // 0: empty, -1: guard, -2: wall, 1: guarded
    List<List<int>> grid = List.generate(m, (_) => List.filled(n, 0));

    for (var g in guards) {
      int r = g[0];
      int c = g[1];
      grid[r][c] = -1;
    }
    for (var w in walls) {
      int r = w[0];
      int c = w[1];
      grid[r][c] = -2;
    }

    // Row scans
    for (int i = 0; i < m; ++i) {
      bool seenGuard = false;
      for (int j = 0; j < n; ++j) {
        int cell = grid[i][j];
        if (cell == -1) {
          seenGuard = true;
        } else if (cell == -2) {
          seenGuard = false;
        } else if (seenGuard && cell == 0) {
          grid[i][j] = 1; // guarded
        }
      }
      seenGuard = false;
      for (int j = n - 1; j >= 0; --j) {
        int cell = grid[i][j];
        if (cell == -1) {
          seenGuard = true;
        } else if (cell == -2) {
          seenGuard = false;
        } else if (seenGuard && cell == 0) {
          grid[i][j] = 1;
        }
      }
    }

    // Column scans
    for (int j = 0; j < n; ++j) {
      bool seenGuard = false;
      for (int i = 0; i < m; ++i) {
        int cell = grid[i][j];
        if (cell == -1) {
          seenGuard = true;
        } else if (cell == -2) {
          seenGuard = false;
        } else if (seenGuard && cell == 0) {
          grid[i][j] = 1;
        }
      }
      seenGuard = false;
      for (int i = m - 1; i >= 0; --i) {
        int cell = grid[i][j];
        if (cell == -1) {
          seenGuard = true;
        } else if (cell == -2) {
          seenGuard = false;
        } else if (seenGuard && cell == 0) {
          grid[i][j] = 1;
        }
      }
    }

    int unguarded = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 0) {
          ++unguarded;
        }
      }
    }
    return unguarded;
  }
}
```

## Golang

```go
func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	const (
		empty   = 0
		guard   = 1
		wall    = 2
		guarded = 3
	)

	grid := make([][]int, m)
	for i := 0; i < m; i++ {
		grid[i] = make([]int, n)
	}

	for _, g := range guards {
		r, c := g[0], g[1]
		grid[r][c] = guard
	}
	for _, w := range walls {
		r, c := w[0], w[1]
		grid[r][c] = wall
	}

	// Row scans
	for i := 0; i < m; i++ {
		seen := false
		for j := 0; j < n; j++ {
			switch grid[i][j] {
			case guard:
				seen = true
			case wall:
				seen = false
			default:
				if seen && grid[i][j] == empty {
					grid[i][j] = guarded
				}
			}
		}
		seen = false
		for j := n - 1; j >= 0; j-- {
			switch grid[i][j] {
			case guard:
				seen = true
			case wall:
				seen = false
			default:
				if seen && grid[i][j] == empty {
					grid[i][j] = guarded
				}
			}
		}
	}

	// Column scans
	for j := 0; j < n; j++ {
		seen := false
		for i := 0; i < m; i++ {
			switch grid[i][j] {
			case guard:
				seen = true
			case wall:
				seen = false
			default:
				if seen && grid[i][j] == empty {
					grid[i][j] = guarded
				}
			}
		}
		seen = false
		for i := m - 1; i >= 0; i-- {
			switch grid[i][j] {
			case guard:
				seen = true
			case wall:
				seen = false
			default:
				if seen && grid[i][j] == empty {
					grid[i][j] = guarded
				}
			}
		}
	}

	count := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == empty {
				count++
			}
		}
	}
	return count
}
```

## Ruby

```ruby
def count_unguarded(m, n, guards, walls)
  EMPTY = 0
  GUARD = 1
  WALL = 2
  GUARDED = 3

  grid = Array.new(m) { Array.new(n, EMPTY) }

  guards.each do |r, c|
    grid[r][c] = GUARD
  end

  walls.each do |r, c|
    grid[r][c] = WALL
  end

  guards.each do |r, c|
    i = r - 1
    while i >= 0 && grid[i][c] == EMPTY
      grid[i][c] = GUARDED
      i -= 1
    end

    i = r + 1
    while i < m && grid[i][c] == EMPTY
      grid[i][c] = GUARDED
      i += 1
    end

    j = c - 1
    while j >= 0 && grid[r][j] == EMPTY
      grid[r][j] = GUARDED
      j -= 1
    end

    j = c + 1
    while j < n && grid[r][j] == EMPTY
      grid[r][j] = GUARDED
      j += 1
    end
  end

  count = 0
  (0...m).each do |i|
    row = grid[i]
    (0...n).each do |j|
      count += 1 if row[j] == EMPTY
    end
  end
  count
end
```

## Scala

```scala
object Solution {
  def countUnguarded(m: Int, n: Int, guards: Array[Array[Int]], walls: Array[Array[Int]]): Int = {
    val grid = Array.ofDim[Int](m, n) // 0: empty, 1: guarded, 2: guard, 3: wall

    for (g <- guards) {
      grid(g(0))(g(1)) = 2
    }
    for (w <- walls) {
      grid(w(0))(w(1)) = 3
    }

    // Row left to right
    var i = 0
    while (i < m) {
      var seenGuard = false
      var j = 0
      while (j < n) {
        grid(i)(j) match {
          case 2 => seenGuard = true
          case 3 => seenGuard = false
          case _ =>
            if (seenGuard && grid(i)(j) == 0) grid(i)(j) = 1
        }
        j += 1
      }
      i += 1
    }

    // Row right to left
    i = 0
    while (i < m) {
      var seenGuard = false
      var j = n - 1
      while (j >= 0) {
        grid(i)(j) match {
          case 2 => seenGuard = true
          case 3 => seenGuard = false
          case _ =>
            if (seenGuard && grid(i)(j) == 0) grid(i)(j) = 1
        }
        j -= 1
      }
      i += 1
    }

    // Column top to bottom
    var j = 0
    while (j < n) {
      var seenGuard = false
      i = 0
      while (i < m) {
        grid(i)(j) match {
          case 2 => seenGuard = true
          case 3 => seenGuard = false
          case _ =>
            if (seenGuard && grid(i)(j) == 0) grid(i)(j) = 1
        }
        i += 1
      }
      j += 1
    }

    // Column bottom to top
    j = 0
    while (j < n) {
      var seenGuard = false
      i = m - 1
      while (i >= 0) {
        grid(i)(j) match {
          case 2 => seenGuard = true
          case 3 => seenGuard = false
          case _ =>
            if (seenGuard && grid(i)(j) == 0) grid(i)(j) = 1
        }
        i -= 1
      }
      j += 1
    }

    // Count unguarded empty cells
    var count = 0
    i = 0
    while (i < m) {
      j = 0
      while (j < n) {
        if (grid(i)(j) == 0) count += 1
        j += 1
      }
      i += 1
    }

    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_unguarded(m: i32, n: i32, guards: Vec<Vec<i32>>, walls: Vec<Vec<i32>>) -> i32 {
        let rows = m as usize;
        let cols = n as usize;
        const EMPTY: i8 = 0;
        const GUARD: i8 = 1;
        const WALL: i8 = 2;
        const GUARDED: i8 = 3;

        let mut grid = vec![EMPTY; rows * cols];

        for g in guards.iter() {
            let r = g[0] as usize;
            let c = g[1] as usize;
            grid[r * cols + c] = GUARD;
        }
        for w in walls.iter() {
            let r = w[0] as usize;
            let c = w[1] as usize;
            grid[r * cols + c] = WALL;
        }

        let directions = [(-1i32, 0i32), (1, 0), (0, -1), (0, 1)];

        for g in guards.iter() {
            let (gr, gc) = (g[0], g[1]);
            for &(dr, dc) in &directions {
                let mut r = gr + dr;
                let mut c = gc + dc;
                while r >= 0 && r < m && c >= 0 && c < n {
                    let idx = (r as usize) * cols + c as usize;
                    if grid[idx] == GUARD || grid[idx] == WALL {
                        break;
                    }
                    if grid[idx] == EMPTY {
                        grid[idx] = GUARDED;
                    }
                    r += dr;
                    c += dc;
                }
            }
        }

        let mut count = 0i32;
        for &cell in grid.iter() {
            if cell == EMPTY {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (count-unguarded m n guards walls)
  (-> exact-integer? exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      exact-integer?)
  (let* ((grid (make-vector m))
         (make-row (lambda () (make-vector n 0))))
    ;; initialize empty grid
    (for ([i (in-range m)])
      (vector-set! grid i (make-row)))
    ;; place guards (value 1)
    (for ([g guards])
      (define r (first g))
      (define c (second g))
      (vector-set! (vector-ref grid r) c 1))
    ;; place walls (value 2)
    (for ([w walls])
      (define r (first w))
      (define c (second w))
      (vector-set! (vector-ref grid r) c 2))
    ;; row passes: left->right
    (for ([i (in-range m)])
      (define rowvec (vector-ref grid i))
      (let ([guarded? #f])
        (for ([j (in-range n)])
          (define cell (vector-ref rowvec j))
          (cond [(= cell 1) (set! guarded? #t)]
                [(= cell 2) (set! guarded? #f)]
                [else (when (and guarded? (= cell 0))
                        (vector-set! rowvec j 3))])))
      ;; right->left
      (let ([guarded? #f])
        (for ([j (in-range (sub1 n) -1 -1)])
          (define cell (vector-ref rowvec j))
          (cond [(= cell 1) (set! guarded? #t)]
                [(= cell 2) (set! guarded? #f)]
                [else (when (and guarded? (= cell 0))
                        (vector-set! rowvec j 3))]))))
    ;; column passes: top->bottom and bottom->top
    (for ([j (in-range n)])
      ;; top -> bottom
      (let ([guarded? #f])
        (for ([i (in-range m)])
          (define cell (vector-ref (vector-ref grid i) j))
          (cond [(= cell 1) (set! guarded? #t)]
                [(= cell 2) (set! guarded? #f)]
                [else (when (and guarded? (= cell 0))
                        (vector-set! (vector-ref grid i) j 3))])))
      ;; bottom -> top
      (let ([guarded? #f])
        (for ([i (in-range (sub1 m) -1 -1)])
          (define cell (vector-ref (vector-ref grid i) j))
          (cond [(= cell 1) (set! guarded? #t)]
                [(= cell 2) (set! guarded? #f)]
                [else (when (and guarded? (= cell 0))
                        (vector-set! (vector-ref grid i) j 3))]))))
    ;; count unguarded cells (value 0)
    (let ((cnt 0))
      (for ([i (in-range m)])
        (define rowvec (vector-ref grid i))
        (for ([j (in-range n)])
          (when (= (vector-ref rowvec j) 0)
            (set! cnt (+ cnt 1)))))
      cnt)))
```

## Erlang

```erlang
-spec count_unguarded(integer(), integer(), [[integer()]], [[integer()]]) -> integer().
count_unguarded(M, N, Guards, Walls) ->
    GuardVal = 2,
    WallVal = 3,
    GuardedVal = 1,

    Grid0 = lists:foldl(fun([R, C], Acc) -> maps:put({R, C}, GuardVal, Acc) end,
                        maps:new(),
                        Guards),
    Grid1 = lists:foldl(fun([R, C], Acc) -> maps:put({R, C}, WallVal, Acc) end,
                        Grid0,
                        Walls),

    RowSeq = lists:seq(0, M - 1),
    ColSeq = lists:seq(0, N - 1),

    %% Process rows
    GridRows = lists:foldl(fun(R, GIn) ->
        {GAfterLR, _} =
            lists:foldl(fun(C, {G, Seen}) ->
                Pos = {R, C},
                case maps:get(Pos, G, 0) of
                    GuardVal -> {G, true};
                    WallVal -> {G, false};
                    _ when Seen ->
                        NewG = case maps:is_key(Pos, G) of
                            true ->
                                case maps:get(Pos, G) of
                                    GuardedVal -> G;
                                    _ -> G
                                end;
                            false -> maps:put(Pos, GuardedVal, G)
                        end,
                        {NewG, Seen};
                    _ -> {G, Seen}
                end
            end, {GIn, false}, ColSeq),

        RevCol = lists:reverse(ColSeq),
        {GAfterRL, _} =
            lists:foldl(fun(C, {G, Seen}) ->
                Pos = {R, C},
                case maps:get(Pos, G, 0) of
                    GuardVal -> {G, true};
                    WallVal -> {G, false};
                    _ when Seen ->
                        NewG = case maps:is_key(Pos, G) of
                            true ->
                                case maps:get(Pos, G) of
                                    GuardedVal -> G;
                                    _ -> G
                                end;
                            false -> maps:put(Pos, GuardedVal, G)
                        end,
                        {NewG, Seen};
                    _ -> {G, Seen}
                end
            end, {GAfterLR, false}, RevCol),
        GAfterRL
    end, Grid1, RowSeq),

    %% Process columns
    FinalGrid = lists:foldl(fun(C, GIn) ->
        {GAfterTB, _} =
            lists:foldl(fun(R, {G, Seen}) ->
                Pos = {R, C},
                case maps:get(Pos, G, 0) of
                    GuardVal -> {G, true};
                    WallVal -> {G, false};
                    _ when Seen ->
                        NewG = case maps:is_key(Pos, G) of
                            true ->
                                case maps:get(Pos, G) of
                                    GuardedVal -> G;
                                    _ -> G
                                end;
                            false -> maps:put(Pos, GuardedVal, G)
                        end,
                        {NewG, Seen};
                    _ -> {G, Seen}
                end
            end, {GIn, false}, RowSeq),

        RevRow = lists:reverse(RowSeq),
        {GAfterBT, _} =
            lists:foldl(fun(R, {G, Seen}) ->
                Pos = {R, C},
                case maps:get(Pos, G, 0) of
                    GuardVal -> {G, true};
                    WallVal -> {G, false};
                    _ when Seen ->
                        NewG = case maps:is_key(Pos, G) of
                            true ->
                                case maps:get(Pos, G) of
                                    GuardedVal -> G;
                                    _ -> G
                                end;
                            false -> maps:put(Pos, GuardedVal, G)
                        end,
                        {NewG, Seen};
                    _ -> {G, Seen}
                end
            end, {GAfterTB, false}, RevRow),
        GAfterBT
    end, GridRows, ColSeq),

    %% Count unguarded cells
    lists:foldl(fun(R, Acc) ->
        lists:foldl(fun(C, Acc2) ->
            case maps:get({R, C}, FinalGrid, 0) of
                0 -> Acc2 + 1;
                _ -> Acc2
            end
        end, Acc, ColSeq)
    end, 0, RowSeq).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_unguarded(integer, integer, [[integer]], [[integer]]) :: integer
  def count_unguarded(m, n, guards, walls) do
    guard_set = MapSet.new(Enum.map(guards, fn [r, c] -> {r, c} end))
    wall_set = MapSet.new(Enum.map(walls, fn [r, c] -> {r, c} end))

    guarded =
      Enum.reduce(guards, MapSet.new(), fn [gr, gc], acc ->
        dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]
        Enum.reduce(dirs, acc, fn {dr, dc}, a ->
          walk(gr + dr, gc + dc, dr, dc, m, n, guard_set, wall_set, a)
        end)
      end)

    total = m * n
    occupied = MapSet.size(guard_set) + MapSet.size(wall_set)
    total - occupied - MapSet.size(guarded)
  end

  defp walk(r, c, dr, dc, m, n, guard_set, wall_set, guarded_set) do
    cond do
      r < 0 or r >= m or c < 0 or c >= n ->
        guarded_set

      MapSet.member?(guard_set, {r, c}) or MapSet.member?(wall_set, {r, c}) ->
        guarded_set

      true ->
        new_guarded = MapSet.put(guarded_set, {r, c})
        walk(r + dr, c + dc, dr, dc, m, n, guard_set, wall_set, new_guarded)
    end
  end
end
```

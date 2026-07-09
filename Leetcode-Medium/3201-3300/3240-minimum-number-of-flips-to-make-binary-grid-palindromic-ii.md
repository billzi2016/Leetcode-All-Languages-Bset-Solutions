# 3240. Minimum Number of Flips to Make Binary Grid Palindromic II

## Cpp

```cpp
class Solution {
public:
    int minFlips(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        const long long INF = 1e18;
        long long baseCost = 0;
        vector<array<long long,3>> smallGroups; // {cost0, cost1, addMod}
        for (int i = 0; i <= (m - 1) / 2; ++i) {
            int i2 = m - 1 - i;
            for (int j = 0; j <= (n - 1) / 2; ++j) {
                int j2 = n - 1 - j;
                vector<int> cells;
                cells.push_back(grid[i][j]);
                if (j2 != j) cells.push_back(grid[i][j2]);
                if (i2 != i) cells.push_back(grid[i2][j]);
                if (i2 != i && j2 != j) cells.push_back(grid[i2][j2]);
                
                int sz = cells.size();
                int cntOnes = 0;
                for (int v : cells) cntOnes += v;
                
                if (sz == 4) {
                    baseCost += min(cntOnes, 4 - cntOnes);
                } else {
                    long long cost0 = cntOnes;          // make all 0
                    long long cost1 = sz - cntOnes;     // make all 1
                    int addMod = sz % 4;                // contribution to total ones modulo 4
                    smallGroups.push_back({cost0, cost1, addMod});
                }
            }
        }
        
        long long dp[4];
        for (int k = 0; k < 4; ++k) dp[k] = INF;
        dp[0] = 0;
        for (auto &g : smallGroups) {
            long long ndp[4];
            for (int k = 0; k < 4; ++k) ndp[k] = INF;
            long long cost0 = g[0], cost1 = g[1];
            int addMod = (int)g[2];
            for (int mod = 0; mod < 4; ++mod) {
                if (dp[mod] == INF) continue;
                // choose all 0
                ndp[mod] = min(ndp[mod], dp[mod] + cost0);
                // choose all 1
                int nmod = (mod + addMod) % 4;
                ndp[nmod] = min(ndp[nmod], dp[mod] + cost1);
            }
            for (int k = 0; k < 4; ++k) dp[k] = ndp[k];
        }
        
        return (int)(baseCost + dp[0]);
    }
};
```

## Java

```java
class Solution {
    public int minFlips(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        final int INF = 1_000_000_000;
        int[] dp = new int[4];
        for (int i = 0; i < 4; i++) dp[i] = INF;
        dp[0] = 0;

        for (int i = 0; i <= (m - 1) / 2; i++) {
            int i2 = m - 1 - i;
            for (int j = 0; j <= (n - 1) / 2; j++) {
                int j2 = n - 1 - j;

                int cntOnes = 0;
                int sz = 0;

                // (i, j)
                cntOnes += grid[i][j];
                sz++;

                if (i2 != i) { // (i2, j)
                    cntOnes += grid[i2][j];
                    sz++;
                }
                if (j2 != j) { // (i, j2)
                    cntOnes += grid[i][j2];
                    sz++;
                }
                if (i2 != i && j2 != j) { // (i2, j2)
                    cntOnes += grid[i2][j2];
                    sz++;
                }

                int cost0 = cntOnes;          // flip all to 0
                int cost1 = sz - cntOnes;     // flip all to 1
                int w = sz % 4;               // added ones modulo 4

                int[] ndp = new int[4];
                for (int k = 0; k < 4; k++) ndp[k] = INF;

                for (int r = 0; r < 4; r++) {
                    if (dp[r] == INF) continue;
                    // choose value 0
                    ndp[r] = Math.min(ndp[r], dp[r] + cost0);
                    // choose value 1
                    int nr = (r + w) & 3; // modulo 4
                    ndp[nr] = Math.min(ndp[nr], dp[r] + cost1);
                }
                dp = ndp;
            }
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        INF = 10**18
        dp = [INF] * 4
        dp[0] = 0

        for i in range((m + 1) // 2):
            mi = m - 1 - i
            for j in range((n + 1) // 2):
                nj = n - 1 - j

                if i == mi and j == nj:
                    vals = [grid[i][j]]
                elif i == mi:
                    vals = [grid[i][j], grid[i][nj]]
                elif j == nj:
                    vals = [grid[i][j], grid[mi][j]]
                else:
                    vals = [
                        grid[i][j],
                        grid[mi][j],
                        grid[i][nj],
                        grid[mi][nj]
                    ]

                ones = sum(vals)
                size = len(vals)
                cost0 = ones               # make all 0
                cost1 = size - ones        # make all 1
                add_mod = size % 4

                newdp = [INF] * 4
                for r in range(4):
                    if dp[r] == INF:
                        continue
                    # set to 0
                    nr = r
                    if dp[r] + cost0 < newdp[nr]:
                        newdp[nr] = dp[r] + cost0
                    # set to 1
                    nr = (r + add_mod) % 4
                    if dp[r] + cost1 < newdp[nr]:
                        newdp[nr] = dp[r] + cost1
                dp = newdp

        return dp[0]
```

## Python3

```python
from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10 ** 9
        dp = [0] + [INF] * 3  # dp[mod] = min flips achieving total ones %4 == mod

        for i in range((m + 1) // 2):
            for j in range((n + 1) // 2):
                positions = [
                    (i, j),
                    (i, n - 1 - j),
                    (m - 1 - i, j),
                    (m - 1 - i, n - 1 - j)
                ]
                uniq = set(positions)
                k = len(uniq)                     # size of the group
                cnt1 = sum(grid[x][y] for x, y in uniq)

                cost0 = cnt1          # flips to make all zeros
                cost1 = k - cnt1      # flips to make all ones

                ndp = [INF] * 4
                for mod in range(4):
                    if dp[mod] == INF:
                        continue
                    # choose value 0 for this group
                    new_mod = mod
                    ndp[new_mod] = min(ndp[new_mod], dp[mod] + cost0)
                    # choose value 1 for this group
                    new_mod = (mod + k) % 4
                    ndp[new_mod] = min(ndp[new_mod], dp[mod] + cost1)
                dp = ndp

        return dp[0]
```

## C

```c
int minFlips(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    long long totalOnes = 0;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            totalOnes += grid[i][j];

    const int INF = 1e9;
    int dp[4];
    for (int r = 0; r < 4; ++r) dp[r] = INF;
    dp[0] = 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int i2 = m - 1 - i;
            int j2 = n - 1 - j;
            if (i > i2) continue;
            if (i == i2 && j > j2) continue;

            int vals[4];
            int sz = 0;
            vals[sz++] = grid[i][j];
            if (i2 != i) vals[sz++] = grid[i2][j];
            if (j2 != j) vals[sz++] = grid[i][j2];
            if (i2 != i && j2 != j) vals[sz++] = grid[i2][j2];

            int cntOnes = 0;
            for (int k = 0; k < sz; ++k) cntOnes += vals[k];

            int ndp[4];
            for (int r = 0; r < 4; ++r) ndp[r] = INF;

            for (int r = 0; r < 4; ++r) {
                if (dp[r] == INF) continue;
                // set group to 0
                int cost0 = cntOnes;
                int delta0 = -cntOnes;
                int nr0 = (r + ((delta0 % 4) + 4) % 4) % 4;
                if (dp[r] + cost0 < ndp[nr0]) ndp[nr0] = dp[r] + cost0;

                // set group to 1
                int cost1 = sz - cntOnes;
                int delta1 = sz - cntOnes;
                int nr1 = (r + ((delta1 % 4) + 4) % 4) % 4;
                if (dp[r] + cost1 < ndp[nr1]) ndp[nr1] = dp[r] + cost1;
            }

            for (int r = 0; r < 4; ++r) dp[r] = ndp[r];
        }
    }

    int need = (int)((4 - (totalOnes % 4)) % 4);
    return dp[need];
}
```

## Csharp

```csharp
public class Solution {
    public int MinFlips(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int flips = 0;

        for (int i = 0; i < (m + 1) / 2; i++) {
            for (int j = 0; j < (n + 1) / 2; j++) {
                int iOpp = m - 1 - i;
                int jOpp = n - 1 - j;

                // collect the values of the symmetric cells
                int countOnes = 0;
                int total = 0;

                // (i, j)
                countOnes += grid[i][j];
                total++;

                // (iOpp, j) if different row
                if (iOpp != i) {
                    countOnes += grid[iOpp][j];
                    total++;
                }

                // (i, jOpp) if different column
                if (jOpp != j) {
                    countOnes += grid[i][jOpp];
                    total++;
                }

                // (iOpp, jOpp) if both row and column differ
                if (iOpp != i && jOpp != j) {
                    countOnes += grid[iOpp][jOpp];
                    total++;
                }

                flips += Math.Min(countOnes, total - countOnes);
            }
        }

        return flips;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minFlips = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let baseCost = 0; // cost from groups of size 4 (mod 4 contribution always 0)
    const groups = []; // groups with size 1 or 2
    
    for (let i = 0; i <= Math.floor((m - 1) / 2); i++) {
        for (let j = 0; j <= Math.floor((n - 1) / 2); j++) {
            const i2 = m - 1 - i;
            const j2 = n - 1 - j;
            
            let vals = [];
            if (i === i2 && j === j2) {                 // single center cell
                vals.push(grid[i][j]);
            } else if (i === i2) {                      // same row, two columns
                vals.push(grid[i][j], grid[i][j2]);
            } else if (j === j2) {                      // same column, two rows
                vals.push(grid[i][j], grid[i2][j]);
            } else {                                    // four distinct cells
                vals.push(grid[i][j], grid[i2][j], grid[i][j2], grid[i2][j2]);
            }
            
            const cntOnes = vals.reduce((a, b) => a + b, 0);
            const sz = vals.length;
            
            if (sz === 4) {
                baseCost += Math.min(cntOnes, 4 - cntOnes);
            } else {
                const costZero = cntOnes;          // flip all to 0
                const costOne = sz - cntOnes;      // flip all to 1
                const modAdd = sz % 4;             // contribution to total ones modulo 4 if we choose all 1
                groups.push({costZero, costOne, modAdd});
            }
        }
    }
    
    // DP over remainder modulo 4
    const INF = Number.MAX_SAFE_INTEGER;
    let dp = [0, INF, INF, INF];
    for (const g of groups) {
        const ndp = [INF, INF, INF, INF];
        for (let r = 0; r < 4; r++) {
            if (dp[r] === INF) continue;
            // make all zeros
            ndp[r] = Math.min(ndp[r], dp[r] + g.costZero);
            // make all ones
            const nr = (r + g.modAdd) % 4;
            ndp[nr] = Math.min(ndp[nr], dp[r] + g.costOne);
        }
        dp = ndp;
    }
    
    return baseCost + dp[0];
};
```

## Typescript

```typescript
function minFlips(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const INF = 1e9;

    // DP over remainder modulo 4 of total ones
    let dp = new Array(4).fill(INF);
    dp[0] = 0;

    const rowMid = Math.floor((m - 1) / 2);
    const colMid = Math.floor((n - 1) / 2);

    for (let i = 0; i <= rowMid; i++) {
        for (let j = 0; j <= colMid; j++) {
            // collect unique symmetric positions
            const cells: [number, number][] = [];
            const a = i, b = j;
            const c = m - 1 - i, d = n - 1 - j;

            cells.push([a, b]);
            if (c !== a) cells.push([c, b]);
            if (d !== b) cells.push([a, d]);
            if (c !== a && d !== b) cells.push([c, d]);

            const s = cells.length;
            let cntOnes = 0;
            for (const [x, y] of cells) {
                cntOnes += grid[x][y];
            }

            const costToZero = cntOnes;          // flip all ones to zero
            const costToOne = s - cntOnes;       // flip zeros to one

            const newDp = new Array(4).fill(INF);
            for (let mod = 0; mod < 4; mod++) {
                if (dp[mod] === INF) continue;
                // make this group all zero
                if (newDp[mod] > dp[mod] + costToZero) {
                    newDp[mod] = dp[mod] + costToZero;
                }
                // make this group all one
                const nMod = (mod + s) % 4;
                if (newDp[nMod] > dp[mod] + costToOne) {
                    newDp[nMod] = dp[mod] + costToOne;
                }
            }
            dp = newDp;
        }
    }

    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minFlips($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $baseCost = 0;
        $totalOnesAfter = 0;

        $hasTieSize2 = false;          // a size‑2 group with equal cost (ones == 1)
        $minDiffSize2 = PHP_INT_MAX;   // minimal extra cost to switch a size‑2 group
        $hasCenter = false;            // central cell when both dimensions are odd

        for ($i = 0; $i <= intdiv($m - 1, 2); $i++) {
            for ($j = 0; $j <= intdiv($n - 1, 2); $j++) {
                $positions = [];
                $seen = [];

                $coords = [
                    [$i, $j],
                    [$m - 1 - $i, $j],
                    [$i, $n - 1 - $j],
                    [$m - 1 - $i, $n - 1 - $j]
                ];

                foreach ($coords as $c) {
                    $key = $c[0] . ',' . $c[1];
                    if (!isset($seen[$key])) {
                        $seen[$key] = true;
                        $positions[] = $c;
                    }
                }

                $k = count($positions);
                $ones = 0;
                foreach ($positions as $p) {
                    $ones += $grid[$p[0]][$p[1]];
                }

                $costZero = $ones;          // make all cells 0
                $costOne  = $k - $ones;     // make all cells 1

                if ($costZero < $costOne) {
                    $baseCost += $costZero;
                    // contribution to total ones is 0
                } elseif ($costOne < $costZero) {
                    $baseCost += $costOne;
                    $totalOnesAfter += $k;   // all become 1
                } else { // tie
                    $baseCost += $costZero; // same as costOne
                    if ($k == 2) {
                        $hasTieSize2 = true; // we can later choose 0 or 2 without extra cost
                        // currently treat contribution as 0
                    }
                }

                if ($k == 2 && $costZero != $costOne) {
                    $diff = abs($costZero - $costOne); // always 2 when not tie
                    if ($diff < $minDiffSize2) {
                        $minDiffSize2 = $diff;
                    }
                }

                if ($k == 1) { // central cell when both dimensions are odd
                    $hasCenter = true;
                    $totalOnesAfter += $ones; // we keep its original value (cheapest)
                }
            }
        }

        $rem = $totalOnesAfter % 4;
        $extra = 0;

        if ($rem == 0) {
            $extra = 0;
        } elseif ($rem == 2) {
            if ($hasTieSize2) {
                $extra = 0; // flip a tied size‑2 group at no extra cost
            } else {
                $extra = $minDiffSize2; // must pay the minimal diff (should be 2)
            }
        } else { // rem == 1 or 3, need central cell adjustment
            if ($hasCenter) {
                $extra = 1; // flip the center cell
                if ($rem == 3) {
                    if ($hasTieSize2) {
                        // no additional cost needed
                    } else {
                        $extra += $minDiffSize2; // add a size‑2 adjustment (cost 2)
                    }
                }
            } else {
                // This situation should not occur with valid inputs
                $extra = PHP_INT_MAX;
            }
        }

        return $baseCost + $extra;
    }
}
```

## Swift

```swift
class Solution {
    func minFlips(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var groups: [(size: Int, ones: Int)] = []
        
        let maxI = (m - 1) / 2
        let maxJ = (n - 1) / 2
        
        for i in 0...maxI {
            for j in 0...maxJ {
                var positions: [(Int, Int)] = []
                let i2 = m - 1 - i
                let j2 = n - 1 - j
                
                positions.append((i, j))
                if i2 != i { positions.append((i2, j)) }
                if j2 != j { positions.append((i, j2)) }
                if i2 != i && j2 != j { positions.append((i2, j2)) }
                
                var cntOnes = 0
                for (x, y) in positions {
                    cntOnes += grid[x][y]
                }
                groups.append((size: positions.count, ones: cntOnes))
            }
        }
        
        let INF = Int.max / 4
        var dp = [Int](repeating: INF, count: 4)
        dp[0] = 0
        
        for g in groups {
            var ndp = [Int](repeating: INF, count: 4)
            let sizeMod = g.size % 4
            for r in 0..<4 where dp[r] < INF {
                // make all zeros
                let costZero = dp[r] + g.ones
                if costZero < ndp[r] { ndp[r] = costZero }
                
                // make all ones
                let newR = (r + sizeMod) % 4
                let costOne = dp[r] + (g.size - g.ones)
                if costOne < ndp[newR] { ndp[newR] = costOne }
            }
            dp = ndp
        }
        
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minFlips(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var ans = 0
        val INF = 1_000_000_000
        var dp = IntArray(4) { INF }
        dp[0] = 0

        for (i in 0 until m) {
            val i2 = m - 1 - i
            if (i > i2) continue
            for (j in 0 until n) {
                val j2 = n - 1 - j
                if (i == i2 && j > j2) continue

                // collect unique symmetric cells
                var cnt = 0
                var ones = 0
                // (i, j)
                cnt++
                ones += grid[i][j]
                // (i2, j)
                if (i2 != i) {
                    cnt++
                    ones += grid[i2][j]
                }
                // (i, j2)
                if (j2 != j) {
                    cnt++
                    ones += grid[i][j2]
                }
                // (i2, j2)
                if (i2 != i && j2 != j) {
                    cnt++
                    ones += grid[i2][j2]
                }

                when (cnt) {
                    4 -> {
                        val cost0 = ones               // make all 0
                        val cost1 = 4 - ones           // make all 1
                        ans += kotlin.math.min(cost0, cost1)
                    }
                    2 -> {
                        val cost0 = ones               // both 0
                        val cost1 = 2 - ones           // both 1 (contribute 2 ones)
                        val newDp = IntArray(4) { INF }
                        for (mod in 0..3) {
                            if (dp[mod] == INF) continue
                            // option: both 0, contribution 0
                            if (dp[mod] + cost0 < newDp[mod]) newDp[mod] = dp[mod] + cost0
                            // option: both 1, contribution 2
                            val mod2 = (mod + 2) % 4
                            if (dp[mod] + cost1 < newDp[mod2]) newDp[mod2] = dp[mod] + cost1
                        }
                        dp = newDp
                    }
                    1 -> {
                        val v = ones // value of the single cell
                        val cost0 = v          // make it 0, contribution 0
                        val cost1 = 1 - v      // make it 1, contribution 1
                        val newDp = IntArray(4) { INF }
                        for (mod in 0..3) {
                            if (dp[mod] == INF) continue
                            // make 0
                            if (dp[mod] + cost0 < newDp[mod]) newDp[mod] = dp[mod] + cost0
                            // make 1, contribution 1
                            val mod2 = (mod + 1) % 4
                            if (dp[mod] + cost1 < newDp[mod2]) newDp[mod2] = dp[mod] + cost1
                        }
                        dp = newDp
                    }
                }
            }
        }
        return ans + dp[0]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minFlips(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    const int INF = 1 << 60;
    List<int> dp = [0, INF, INF, INF];
    for (int i = 0; i <= (m - 1) ~/ 2; ++i) {
      for (int j = 0; j <= (n - 1) ~/ 2; ++j) {
        int sz;
        int cntOnes;
        int a = grid[i][j];
        int b = grid[i][n - 1 - j];
        int c = grid[m - 1 - i][j];
        int d = grid[m - 1 - i][n - 1 - j];
        if (i == m - 1 - i && j == n - 1 - j) {
          sz = 1;
          cntOnes = a;
        } else if (i == m - 1 - i || j == n - 1 - j) {
          sz = 2;
          if (i == m - 1 - i) {
            // middle row
            cntOnes = a + b;
          } else {
            // middle column
            cntOnes = a + c;
          }
        } else {
          sz = 4;
          cntOnes = a + b + c + d;
        }
        int cost0 = cntOnes;       // flips to make all 0
        int cost1 = sz - cntOnes;   // flips to make all 1
        List<int> ndp = [INF, INF, INF, INF];
        for (int r = 0; r < 4; ++r) {
          if (dp[r] == INF) continue;
          int nr = r % 4;
          int val = dp[r] + cost0;
          if (val < ndp[nr]) ndp[nr] = val;
          nr = (r + sz) % 4;
          val = dp[r] + cost1;
          if (val < ndp[nr]) ndp[nr] = val;
        }
        dp = ndp;
      }
    }
    return dp[0];
  }
}
```

## Golang

```go
func minFlips(grid [][]int) int {
	const INF = int(1 << 60)
	m, n := len(grid), len(grid[0])
	dp := [4]int{0, INF, INF, INF}
	for i := 0; i < m; i++ {
		ii := m - 1 - i
		for j := 0; j < n; j++ {
			jj := n - 1 - j
			if i > ii || (i == ii && j > jj) {
				continue
			}
			cntOnes, sz := 0, 0
			// (i,j)
			cntOnes += grid[i][j]
			sz++
			// (ii,j)
			if i != ii {
				cntOnes += grid[ii][j]
				sz++
			}
			// (i,jj)
			if j != jj {
				cntOnes += grid[i][jj]
				sz++
			}
			// (ii,jj)
			if i != ii && j != jj {
				cntOnes += grid[ii][jj]
				sz++
			}
			costZero := cntOnes
			costOne := sz - cntOnes
			addMod := sz % 4 // 1,2,0 for sizes 1,2,4
			newdp := [4]int{INF, INF, INF, INF}
			for mod := 0; mod < 4; mod++ {
				if dp[mod] == INF {
					continue
				}
				// make this group all 0
				if v := dp[mod] + costZero; v < newdp[mod] {
					newdp[mod] = v
				}
				// make this group all 1
				nmod := (mod + addMod) % 4
				if v := dp[mod] + costOne; v < newdp[nmod] {
					newdp[nmod] = v
				}
			}
			dp = newdp
		}
	}
	return dp[0]
}
```

## Ruby

```ruby
def min_flips(grid)
  m = grid.length
  n = grid[0].length
  groups = []
  ((m + 1) / 2).times do |i|
    ((n + 1) / 2).times do |j|
      cells = [[i, j], [m - 1 - i, j], [i, n - 1 - j], [m - 1 - i, n - 1 - j]]
      uniq_cells = cells.uniq
      s = uniq_cells.size
      ones = 0
      uniq_cells.each { |x, y| ones += grid[x][y] }
      groups << [s, ones]
    end
  end

  inf = 1 << 60
  dp = Array.new(4, inf)
  dp[0] = 0

  groups.each do |size, ones|
    cost0 = ones          # make all zeros
    cost1 = size - ones   # make all ones
    ndp = Array.new(4, inf)
    4.times do |r|
      next if dp[r] == inf
      # choose zero value for this group
      nr = r % 4
      ndp[nr] = [ndp[nr], dp[r] + cost0].min
      # choose one value for this group
      nr2 = (r + size) % 4
      ndp[nr2] = [ndp[nr2], dp[r] + cost1].min
    end
    dp = ndp
  end

  dp[0]
end
```

## Scala

```scala
object Solution {
    def minFlips(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        var total = 0
        var parity = 0 // 0 = even number of size-2 groups set to 1, 1 = odd
        var minExtra = Int.MaxValue

        val halfM = (m + 1) / 2
        val halfN = (n + 1) / 2

        for (i <- 0 until halfM) {
            val iOpp = m - 1 - i
            for (j <- 0 until halfN) {
                val jOpp = n - 1 - j

                if (i == iOpp && j == jOpp) {
                    // single central cell, must become 0
                    if (grid(i)(j) == 1) total += 1
                } else if (i == iOpp || j == jOpp) {
                    // size 2 group
                    val cntOnes = if (i == iOpp) {
                        grid(i)(j) + grid(i)(jOpp)
                    } else {
                        grid(i)(j) + grid(iOpp)(j)
                    }
                    val cost0 = cntOnes               // make both 0
                    val cost1 = 2 - cntOnes           // make both 1
                    if (cost0 <= cost1) {
                        total += cost0
                        // choosing 0 adds 0 ones, parity unchanged
                        val extra = cost1 - cost0
                        if (extra < minExtra) minExtra = extra
                    } else {
                        total += cost1
                        parity ^= 1                     // choosing 1 adds two ones -> toggle parity
                        val extra = cost0 - cost1
                        if (extra < minExtra) minExtra = extra
                    }
                } else {
                    // size 4 group
                    val cntOnes = grid(i)(j) + grid(i)(jOpp) + grid(iOpp)(j) + grid(iOpp)(jOpp)
                    total += math.min(cntOnes, 4 - cntOnes)
                }
            }
        }

        if (parity == 1) total + minExtra else total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_flips(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        // flips for 4‑cell groups
        let mut total_flips: i64 = 0;
        for i in 0..m / 2 {
            for j in 0..n / 2 {
                let mut cnt = 0;
                cnt += grid[i][j];
                cnt += grid[m - 1 - i][j];
                cnt += grid[i][n - 1 - j];
                cnt += grid[m - 1 - i][n - 1 - j];
                total_flips += std::cmp::min(cnt, 4 - cnt) as i64;
            }
        }

        // flips for pair groups (middle row / column)
        let mut pair_flips: i64 = 0;
        let mut parity_one_groups = 0; // number of chosen "1" groups modulo 2
        let mut has_equal_cost_group = false; // cnt == 1

        if m % 2 == 1 {
            let mid_i = m / 2;
            for j in 0..n / 2 {
                let a = grid[mid_i][j];
                let b = grid[mid_i][n - 1 - j];
                let cnt = a + b; // 0..2
                let cost0 = cnt;
                let cost1 = 2 - cnt;
                if cost0 <= cost1 {
                    pair_flips += cost0 as i64;
                } else {
                    pair_flips += cost1 as i64;
                    parity_one_groups ^= 1;
                }
                if cnt == 1 {
                    has_equal_cost_group = true;
                }
            }
        }

        if n % 2 == 1 {
            let mid_j = n / 2;
            for i in 0..m / 2 {
                let a = grid[i][mid_j];
                let b = grid[m - 1 - i][mid_j];
                let cnt = a + b; // 0..2
                let cost0 = cnt;
                let cost1 = 2 - cnt;
                if cost0 <= cost1 {
                    pair_flips += cost0 as i64;
                } else {
                    pair_flips += cost1 as i64;
                    parity_one_groups ^= 1;
                }
                if cnt == 1 {
                    has_equal_cost_group = true;
                }
            }
        }

        // central cell (both dimensions odd) must become 0
        if m % 2 == 1 && n % 2 == 1 {
            let mid_i = m / 2;
            let mid_j = n / 2;
            if grid[mid_i][mid_j] == 1 {
                total_flips += 1;
            }
        }

        // ensure number of "1" pair groups is even
        if parity_one_groups % 2 == 1 {
            if !has_equal_cost_group {
                pair_flips += 2; // flip a group with extra cost 2
            }
        }

        (total_flips + pair_flips) as i32
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (min-flips grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (null? grid) 0 (length (first grid))))
         (half-m (quotient (+ m 1) 2))
         (half-n (quotient (+ n 1) 2))
         (INF 1000000000)
         (baseline-flips 0)
         (baseline-ones 0)
         (toggles '()))
    ;; iterate over groups
    (for ([i (in-range half-m)])
      (for ([j (in-range half-n)])
        (let* ((coords (list (list i j)
                             (list (- m 1 i) j)
                             (list i (- n 1 j))
                             (list (- m 1 i) (- n 1 j))))
               (unique (remove-duplicates coords equal?))
               (size (length unique))
               (cnt (apply + (map (lambda (coord)
                                    (let ((r (first coord)) (c (second coord)))
                                      (list-ref (list-ref grid r) c)))
                                  unique))))
          (cond
            [(= size 4)
             (define min-flip (min cnt (- size cnt)))
             (set! baseline-flips (+ baseline-flips min-flip))
             (if (<= cnt 2)
                 (set! baseline-ones (+ baseline-ones 0))
                 (set! baseline-ones (+ baseline-ones 4)))]
            [(= size 2)
             (define min-flip (min cnt (- size cnt)))
             (set! baseline-flips (+ baseline-flips min-flip))
             (cond
               [(= cnt 1) ; both options equal cost
                (set! baseline-ones (+ baseline-ones 0)) ; choose 0 for baseline
                (set! toggles (cons (list 2 0) toggles))]
               [(= cnt 0)
                (set! baseline-ones (+ baseline-ones 0))
                (set! toggles (cons (list 2 2) toggles))]
               [else ; cnt = 2
                (set! baseline-ones (+ baseline-ones 2))
                (set! toggles (cons (list 2 2) toggles))])]
            [(= size 1)
             (set! baseline-flips (+ baseline-flips 0))
             (set! baseline-ones (+ baseline-ones cnt))
             (define delta-mod (modulo (- (- size cnt) cnt) 4)) ; change if flipped
             (set! toggles (cons (list delta-mod 1) toggles))]
            [else (void)]))))
    ;; DP over modulo 4
    (define dp (make-vector 4 INF))
    (vector-set! dp 0 0)
    (for ([t toggles])
      (let* ((dmod (first t))
             (dcost (second t)))
        (define newdp (make-vector 4 INF))
        (for ([r (in-range 4)])
          (define cur (vector-ref dp r))
          (when (< cur INF)
            ;; keep current state
            (when (< cur (vector-ref newdp r))
              (vector-set! newdp r cur))
            ;; apply toggle
            (define nr (modulo (+ r dmod) 4))
            (define cand (+ cur dcost))
            (when (< cand (vector-ref newdp nr))
              (vector-set! newdp nr cand))))
        (set! dp newdp)))
    (let* ((rem (modulo baseline-ones 4))
           (need (modulo (- rem) 4)))
      (+ baseline-flips (vector-ref dp need)))))
```

## Erlang

```erlang
-spec min_flips(Grid :: [[integer()]]) -> integer().
min_flips(Grid) ->
    M = length(Grid),
    N = case Grid of [] -> 0; [Row|_] -> length(Row) end,
    HalfM = (M - 1) div 2,
    HalfN = (N - 1) div 2,
    Inf = 1 bsl 60,
    InitDP = {0, Inf, Inf, Inf},
    DPFinal = loop_i(0, HalfM, Grid, M, N, HalfN, InitDP),
    element(1, DPFinal).

%% iterate over rows
loop_i(I, MaxI, _Grid, _M, _N, _HalfN, Dp) when I > MaxI ->
    Dp;
loop_i(I, MaxI, Grid, M, N, HalfN, Dp) ->
    Dp1 = loop_j(I, 0, HalfN, Grid, M, N, Dp),
    loop_i(I + 1, MaxI, Grid, M, N, HalfN, Dp1).

%% iterate over columns
loop_j(_I, J, MaxJ, _Grid, _M, _N, Dp) when J > MaxJ ->
    Dp;
loop_j(I, J, MaxJ, Grid, M, N, Dp) ->
    I2 = M - 1 - I,
    J2 = N - 1 - J,
    {Size, Ones} =
        case {I == I2, J == J2} of
            {true, true} ->                     % single center cell
                {1, get(Grid, I, J)};
            {true, false} ->                    % middle row pair
                A = get(Grid, I, J),
                B = get(Grid, I, J2),
                {2, A + B};
            {false, true} ->                    % middle column pair
                A = get(Grid, I, J),
                B = get(Grid, I2, J),
                {2, A + B};
            {false, false} ->                   % four distinct cells
                A = get(Grid, I, J),
                B = get(Grid, I, J2),
                C = get(Grid, I2, J),
                D = get(Grid, I2, J2),
                {4, A + B + C + D}
        end,
    NewDP = update_dp(Dp, Size, Ones),
    loop_j(I, J + 1, MaxJ, Grid, M, N, NewDP).

%% fetch element at (I,J) – zero based indices
get(Grid, I, J) ->
    Row = lists:nth(I + 1, Grid),
    lists:nth(J + 1, Row).

%% DP transition for a group of given size and current number of ones
update_dp({D0, D1, D2, D3} = _OldDP, Size, Ones) ->
    Cost0 = Ones,
    Cost1 = Size - Ones,
    Inf = 1 bsl 60,
    Init = {Inf, Inf, Inf, Inf},
    PrevList = [{0, D0}, {1, D1}, {2, D2}, {3, D3}],
    lists:foldl(
        fun({R, Prev}, Acc) ->
            if
                Prev < Inf ->
                    Idx0 = R rem 4,
                    Old0 = element(Idx0 + 1, Acc),
                    New0 = min(Old0, Prev + Cost0),
                    Acc1 = setelement(Idx0 + 1, Acc, New0),

                    Idx1 = (R + Size) rem 4,
                    Old1 = element(Idx1 + 1, Acc1),
                    New1 = min(Old1, Prev + Cost1),
                    setelement(Idx1 + 1, Acc1, New1);
                true ->
                    Acc
            end
        end,
        Init,
        PrevList
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_flips(grid :: [[integer]]) :: integer
  def min_flips(grid) do
    m = length(grid)
    n = length(hd(grid))

    # convert to tuple of tuples for O(1) access
    grid_t =
      grid
      |> Enum.map(&List.to_tuple/1)
      |> List.to_tuple()

    inf = 1_000_000_000

    max_i = div(m - 1, 2)
    max_j = div(n - 1, 2)

    # initial dp tuple: {mod0, mod1, mod2, mod3}
    init_dp = {0, inf, inf, inf}

    final_dp =
      Enum.reduce(0..max_i, init_dp, fn i, dp_acc ->
        Enum.reduce(0..max_j, dp_acc, fn j, dp_inner ->
          i2 = m - 1 - i
          j2 = n - 1 - j

          {size, cnt_one} =
            cond do
              i == i2 and j == j2 ->
                # central single cell
                {1, cell(grid_t, i, j)}

              i == i2 ->
                # middle row, two symmetric columns (j != j2)
                {2,
                 cell(grid_t, i, j) + cell(grid_t, i, j2)}

              j == j2 ->
                # middle column, two symmetric rows (i != i2)
                {2,
                 cell(grid_t, i, j) + cell(grid_t, i2, j)}

              true ->
                # regular 4-cell group
                {
                  4,
                  cell(grid_t, i, j) +
                    cell(grid_t, i, j2) +
                    cell(grid_t, i2, j) +
                    cell(grid_t, i2, j2)
                }
            end

          cost0 = cnt_one               # flip all to 0
          cost1 = size - cnt_one        # flip all to 1

          # DP transition for this group
          new_dp = {inf, inf, inf, inf}

          new_dp =
            Enum.reduce(0..3, new_dp, fn mod, acc ->
              cur = elem(dp_inner, mod)

              if cur < inf do
                # choose value 0
                nd0 = cur + cost0
                idx0 = rem(mod, 4)
                acc = update_min(acc, idx0, nd0)

                # choose value 1
                nd1 = cur + cost1
                idx1 = rem(mod + size, 4)
                update_min(acc, idx1, nd1)
              else
                acc
              end
            end)

          new_dp
        end)
      end)

    elem(final_dp, 0)
  end

  defp cell(grid_t, x, y) do
    row = elem(grid_t, x)
    elem(row, y)
  end

  defp update_min(dp_tuple, idx, val) do
    current = elem(dp_tuple, idx)

    if val < current do
      put_elem(dp_tuple, idx, val)
    else
      dp_tuple
    end
  end
end
```

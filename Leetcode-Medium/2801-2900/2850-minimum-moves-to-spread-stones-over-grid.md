# 2850. Minimum Moves to Spread Stones Over Grid

## Cpp

```cpp
class Solution {
public:
    int minimumMoves(vector<vector<int>>& grid) {
        vector<pair<int,int>> supply, demand;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int cnt = grid[i][j];
                if (cnt > 1) {
                    for (int k = 0; k < cnt - 1; ++k)
                        supply.emplace_back(i, j);
                } else if (cnt == 0) {
                    demand.emplace_back(i, j);
                }
            }
        }
        int n = supply.size();
        if (n == 0) return 0;
        int m = demand.size(); // should equal n
        const int INF = 1e9;
        vector<int> dp(1 << m, INF), ndp;
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            ndp.assign(1 << m, INF);
            for (int mask = 0; mask < (1 << m); ++mask) {
                if (dp[mask] == INF) continue;
                int used = __builtin_popcount(mask);
                if (used != i) continue; // ensure we assign exactly i supplies so far
                for (int j = 0; j < m; ++j) {
                    if (!(mask & (1 << j))) {
                        int dist = abs(supply[i].first - demand[j].first) + 
                                   abs(supply[i].second - demand[j].second);
                        int nmask = mask | (1 << j);
                        ndp[nmask] = min(ndp[nmask], dp[mask] + dist);
                    }
                }
            }
            dp.swap(ndp);
        }
        return dp[(1 << m) - 1];
    }
};
```

## Java

```java
class Solution {
    public int minimumMoves(int[][] grid) {
        // Lists to store positions of extra stones and empty cells
        int[] extraR = new int[9];
        int[] extraC = new int[9];
        int[] emptyR = new int[9];
        int[] emptyC = new int[9];
        int extraCnt = 0, emptyCnt = 0;
        
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int val = grid[i][j];
                if (val > 1) {
                    // keep one stone, the rest are extra
                    for (int k = 0; k < val - 1; ++k) {
                        extraR[extraCnt] = i;
                        extraC[extraCnt] = j;
                        extraCnt++;
                    }
                } else if (val == 0) {
                    emptyR[emptyCnt] = i;
                    emptyC[emptyCnt] = j;
                    emptyCnt++;
                }
            }
        }
        
        int m = extraCnt; // number of stones to move, equals number of empty cells
        if (m == 0) return 0;
        
        int[][] dist = new int[m][m];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < m; ++j) {
                dist[i][j] = Math.abs(extraR[i] - emptyR[j]) + Math.abs(extraC[i] - emptyC[j]);
            }
        }
        
        int size = 1 << m;
        int INF = Integer.MAX_VALUE / 4;
        int[] dp = new int[size];
        for (int i = 0; i < size; ++i) dp[i] = INF;
        dp[0] = 0;
        
        for (int mask = 0; mask < size; ++mask) {
            int i = Integer.bitCount(mask); // index of extra stone to assign next
            if (i >= m) continue;
            int cur = dp[mask];
            if (cur == INF) continue;
            for (int j = 0; j < m; ++j) {
                if ((mask & (1 << j)) == 0) {
                    int newMask = mask | (1 << j);
                    int nd = cur + dist[i][j];
                    if (nd < dp[newMask]) dp[newMask] = nd;
                }
            }
        }
        
        return dp[size - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sources = []
        targets = []
        for i in range(3):
            for j in range(3):
                val = grid[i][j]
                if val > 1:
                    for _ in range(val - 1):
                        sources.append((i, j))
                elif val == 0:
                    targets.append((i, j))
        n = len(sources)
        if n == 0:
            return 0
        # cost matrix
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            si, sj = sources[i]
            for j in range(n):
                ti, tj = targets[j]
                cost[i][j] = abs(si - ti) + abs(sj - tj)
        # DP over subsets
        INF = 10 ** 9
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            i = bin(mask).count('1')  # number of sources already assigned
            if i >= n:
                continue
            for j in range(n):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + cost[i][j])
        return dp[(1 << n) - 1]
```

## Python3

```python
class Solution:
    def minimumMoves(self, grid):
        surplus = []
        deficit = []
        for i in range(3):
            for j in range(3):
                cnt = grid[i][j]
                if cnt > 1:
                    for _ in range(cnt - 1):
                        surplus.append((i, j))
                elif cnt == 0:
                    deficit.append((i, j))
        n = len(surplus)
        if n == 0:
            return 0
        # cost matrix
        cost = [[abs(si - di) + abs(sj - dj) for (di, dj) in deficit] for (si, sj) in surplus]
        INF = 10 ** 9
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            i = bin(mask).count("1")
            if i >= n:
                continue
            cur = dp[mask]
            if cur == INF:
                continue
            for j in range(n):
                if not (mask >> j) & 1:
                    new_mask = mask | (1 << j)
                    nd = cur + cost[i][j]
                    if nd < dp[new_mask]:
                        dp[new_mask] = nd
        return dp[(1 << n) - 1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minimumMoves(int** grid, int gridSize, int* gridColSize) {
    // positions of extra stones (source) and empty cells (target)
    int srcX[9], srcY[9];
    int dstX[9], dstY[9];
    int n = 0; // number of excess stones == number of empty cells

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            int cnt = grid[i][j];
            if (cnt > 1) {
                for (int k = 0; k < cnt - 1; ++k) {
                    srcX[n] = i;
                    srcY[n] = j;
                    n++;
                }
            } else if (cnt == 0) {
                dstX[n - (cnt > 1 ? 0 : 0)] = i; // placeholder, will be overwritten later
                dstY[n - (cnt > 1 ? 0 : 0)] = j;
            }
        }
    }

    // The above loop incorrectly mixes src and dst indices.
    // Recollect correctly:
    n = 0;
    int srcCnt = 0, dstCnt = 0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            int cnt = grid[i][j];
            if (cnt > 1) {
                for (int k = 0; k < cnt - 1; ++k) {
                    srcX[srcCnt] = i;
                    srcY[srcCnt] = j;
                    srcCnt++;
                }
            } else if (cnt == 0) {
                dstX[dstCnt] = i;
                dstY[dstCnt] = j;
                dstCnt++;
            }
        }
    }

    n = srcCnt; // should equal dstCnt
    if (n == 0) return 0;

    int dist[9][9];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            dist[i][j] = abs(srcX[i] - dstX[j]) + abs(srcY[i] - dstY[j]);
        }
    }

    int memo[5][1 << 4];
    for (int i = 0; i <= n; ++i)
        for (int mask = 0; mask < (1 << n); ++mask)
            memo[i][mask] = -1;

    // recursive DP
    int dfs(int idx, int usedMask) {
        if (idx == n) return 0;
        int *mem = &memo[idx][usedMask];
        if (*mem != -1) return *mem;
        int best = INT_MAX;
        for (int j = 0; j < n; ++j) {
            if (!(usedMask & (1 << j))) {
                int cost = dist[idx][j] + dfs(idx + 1, usedMask | (1 << j));
                if (cost < best) best = cost;
            }
        }
        *mem = best;
        return best;
    }

    // Helper function needs to be defined before use; using static nested function via GCC extension is not portable.
    // Instead implement iterative DP with memoization array.

    // Iterative DP over masks
    int dp[1 << 4];
    for (int mask = 0; mask < (1 << n); ++mask) dp[mask] = INT_MAX;
    dp[0] = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        int i = __builtin_popcount(mask); // number of sources already assigned
        if (i >= n) continue;
        if (dp[mask] == INT_MAX) continue;
        for (int j = 0; j < n; ++j) {
            if (!(mask & (1 << j))) {
                int newMask = mask | (1 << j);
                int val = dp[mask] + dist[i][j];
                if (val < dp[newMask]) dp[newMask] = val;
            }
        }
    }

    return dp[(1 << n) - 1];
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumMoves(int[][] grid) {
        List<(int r, int c)> surplus = new List<(int, int)>();
        List<(int r, int c)> empty = new List<(int, int)>();
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int cnt = grid[i][j];
                if (cnt == 0) {
                    empty.Add((i, j));
                } else if (cnt > 1) {
                    for (int k = 0; k < cnt - 1; k++) {
                        surplus.Add((i, j));
                    }
                }
            }
        }
        
        int n = surplus.Count;
        if (n == 0) return 0; // already balanced
        
        int[,] dist = new int[n, n];
        for (int i = 0; i < n; i++) {
            var (sr, sc) = surplus[i];
            for (int j = 0; j < n; j++) {
                var (er, ec) = empty[j];
                dist[i, j] = Math.Abs(sr - er) + Math.Abs(sc - ec);
            }
        }
        
        int size = 1 << n;
        int[] dp = new int[size];
        const int INF = int.MaxValue / 2;
        for (int i = 0; i < size; i++) dp[i] = INF;
        dp[0] = 0;
        
        for (int mask = 0; mask < size; mask++) {
            int assigned = BitCount(mask);
            if (assigned >= n) continue;
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << j)) == 0) {
                    int newMask = mask | (1 << j);
                    int val = dp[mask] + dist[assigned, j];
                    if (val < dp[newMask]) dp[newMask] = val;
                }
            }
        }
        
        return dp[size - 1];
    }
    
    private static int BitCount(int x) {
        // Simple popcount
        int count = 0;
        while (x != 0) {
            x &= x - 1;
            count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
var minimumMoves = function(grid) {
    const extra = [];
    const empty = [];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cnt = grid[i][j];
            if (cnt === 0) {
                empty.push([i, j]);
            } else if (cnt > 1) {
                for (let k = 0; k < cnt - 1; k++) extra.push([i, j]);
            }
        }
    }
    const n = empty.length;
    if (n === 0) return 0;
    const dist = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        const [ex, ey] = extra[i];
        for (let j = 0; j < n; j++) {
            const [dx, dy] = empty[j];
            dist[i][j] = Math.abs(ex - dx) + Math.abs(ey - dy);
        }
    }
    let ans = Infinity;
    const dfs = (pos, mask, cur) => {
        if (pos === n) {
            if (cur < ans) ans = cur;
            return;
        }
        if (cur >= ans) return;
        for (let j = 0; j < n; j++) {
            if ((mask & (1 << j)) === 0) {
                dfs(pos + 1, mask | (1 << j), cur + dist[pos][j]);
            }
        }
    };
    dfs(0, 0, 0);
    return ans;
};
```

## Typescript

```typescript
function minimumMoves(grid: number[][]): number {
    const surplus: [number, number][] = [];
    const deficit: [number, number][] = [];

    for (let r = 0; r < 3; ++r) {
        for (let c = 0; c < 3; ++c) {
            const cnt = grid[r][c];
            if (cnt > 1) {
                for (let k = 0; k < cnt - 1; ++k) surplus.push([r, c]);
            } else if (cnt === 0) {
                deficit.push([r, c]);
            }
        }
    }

    const n = surplus.length;
    if (n === 0) return 0;

    const dist: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; ++i) {
        const [sr, sc] = surplus[i];
        for (let j = 0; j < n; ++j) {
            const [dr, dc] = deficit[j];
            dist[i][j] = Math.abs(sr - dr) + Math.abs(sc - dc);
        }
    }

    const size = 1 << n;
    const dp: number[] = new Array(size).fill(Infinity);
    dp[0] = 0;

    const popcnt = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    };

    for (let mask = 0; mask < size; ++mask) {
        const i = popcnt(mask);
        if (i >= n) continue;
        const cur = dp[mask];
        if (cur === Infinity) continue;
        for (let j = 0; j < n; ++j) {
            if ((mask & (1 << j)) === 0) {
                const newMask = mask | (1 << j);
                const val = cur + dist[i][j];
                if (val < dp[newMask]) dp[newMask] = val;
            }
        }
    }

    return dp[size - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumMoves($grid) {
        $surplus = [];
        $empty = [];

        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                $cnt = $grid[$i][$j];
                if ($cnt > 1) {
                    for ($k = 0; $k < $cnt - 1; $k++) {
                        $surplus[] = [$i, $j];
                    }
                } elseif ($cnt == 0) {
                    $empty[] = [$i, $j];
                }
            }
        }

        $m = count($surplus);
        if ($m == 0) return 0; // already balanced

        // cost matrix
        $cost = array_fill(0, $m, array_fill(0, $m, 0));
        for ($i = 0; $i < $m; $i++) {
            [$sr, $sc] = $surplus[$i];
            for ($j = 0; $j < $m; $j++) {
                [$er, $ec] = $empty[$j];
                $cost[$i][$j] = abs($sr - $er) + abs($sc - $ec);
            }
        }

        $maxMask = 1 << $m;
        $dp = array_fill(0, $maxMask, PHP_INT_MAX);
        $dp[0] = 0;

        // precompute popcounts
        $bits = array_fill(0, $maxMask, 0);
        for ($mask = 1; $mask < $maxMask; $mask++) {
            $bits[$mask] = $bits[$mask >> 1] + ($mask & 1);
        }

        for ($mask = 0; $mask < $maxMask; $mask++) {
            $i = $bits[$mask]; // number of surplus stones already assigned
            if ($i >= $m) continue;
            $base = $dp[$mask];
            if ($base == PHP_INT_MAX) continue;
            for ($j = 0; $j < $m; $j++) {
                if (($mask & (1 << $j)) == 0) {
                    $newMask = $mask | (1 << $j);
                    $newCost = $base + $cost[$i][$j];
                    if ($newCost < $dp[$newMask]) {
                        $dp[$newMask] = $newCost;
                    }
                }
            }
        }

        return $dp[$maxMask - 1];
    }
}
```

## Swift

```swift
class Solution {
    func minimumMoves(_ grid: [[Int]]) -> Int {
        var surplus: [(Int, Int)] = []
        var empty: [(Int, Int)] = []
        
        for i in 0..<3 {
            for j in 0..<3 {
                let val = grid[i][j]
                if val > 1 {
                    for _ in 0..<(val - 1) {
                        surplus.append((i, j))
                    }
                } else if val == 0 {
                    empty.append((i, j))
                }
            }
        }
        
        let m = surplus.count
        if m == 0 { return 0 }
        
        var dist = Array(repeating: Array(repeating: 0, count: m), count: m)
        for i in 0..<m {
            for j in 0..<m {
                let (sx, sy) = surplus[i]
                let (ex, ey) = empty[j]
                dist[i][j] = abs(sx - ex) + abs(sy - ey)
            }
        }
        
        let size = 1 << m
        var dp = Array(repeating: Int.max / 2, count: size)
        dp[0] = 0
        
        for mask in 0..<size {
            let i = mask.nonzeroBitCount
            if i >= m { continue }
            for j in 0..<m where (mask & (1 << j)) == 0 {
                let newMask = mask | (1 << j)
                let candidate = dp[mask] + dist[i][j]
                if candidate < dp[newMask] {
                    dp[newMask] = candidate
                }
            }
        }
        
        return dp[size - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumMoves(grid: Array<IntArray>): Int {
        val sources = mutableListOf<Pair<Int, Int>>()
        val targets = mutableListOf<Pair<Int, Int>>()
        for (i in 0..2) {
            for (j in 0..2) {
                val v = grid[i][j]
                if (v > 1) repeat(v - 1) { sources.add(Pair(i, j)) }
                else if (v == 0) targets.add(Pair(i, j))
            }
        }
        val n = sources.size
        if (n == 0) return 0
        val dist = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            val (sx, sy) = sources[i]
            for (j in 0 until n) {
                val (tx, ty) = targets[j]
                dist[i][j] = kotlin.math.abs(sx - tx) + kotlin.math.abs(sy - ty)
            }
        }
        val size = 1 shl n
        val INF = Int.MAX_VALUE / 4
        val dp = IntArray(size) { INF }
        dp[0] = 0
        for (mask in 0 until size) {
            val i = Integer.bitCount(mask)
            if (i >= n) continue
            val cur = dp[mask]
            if (cur == INF) continue
            for (j in 0 until n) {
                if ((mask and (1 shl j)) == 0) {
                    val newMask = mask or (1 shl j)
                    val nd = cur + dist[i][j]
                    if (nd < dp[newMask]) dp[newMask] = nd
                }
            }
        }
        return dp[size - 1]
    }
}
```

## Dart

```dart
class Solution {
  int minimumMoves(List<List<int>> grid) {
    List<int> surplus = [];
    List<int> deficit = [];

    for (int r = 0; r < 3; r++) {
      for (int c = 0; c < 3; c++) {
        int cnt = grid[r][c];
        if (cnt > 1) {
          for (int k = 0; k < cnt - 1; k++) surplus.add(r * 3 + c);
        } else if (cnt == 0) {
          deficit.add(r * 3 + c);
        }
      }
    }

    int n = surplus.length;
    if (n == 0) return 0;

    List<List<int>> dist = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; i++) {
      int sr = surplus[i] ~/ 3;
      int sc = surplus[i] % 3;
      for (int j = 0; j < n; j++) {
        int dr = deficit[j] ~/ 3;
        int dc = deficit[j] % 3;
        dist[i][j] = (sr - dr).abs() + (sc - dc).abs();
      }
    }

    int size = 1 << n;
    const int INF = 1 << 30;
    List<int> dp = List.filled(size, INF);
    dp[0] = 0;

    for (int mask = 0; mask < size; mask++) {
      int i = _popcnt(mask);
      if (i >= n) continue;
      for (int j = 0; j < n; j++) {
        if ((mask & (1 << j)) == 0) {
          int newMask = mask | (1 << j);
          int val = dp[mask] + dist[i][j];
          if (val < dp[newMask]) dp[newMask] = val;
        }
      }
    }

    return dp[size - 1];
  }

  int _popcnt(int x) {
    int cnt = 0;
    while (x > 0) {
      cnt += x & 1;
      x >>= 1;
    }
    return cnt;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func minimumMoves(grid [][]int) int {
	type Pos struct{ x, y int }
	var src []Pos
	var dst []Pos

	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			c := grid[i][j]
			if c > 1 {
				for k := 0; k < c-1; k++ {
					src = append(src, Pos{i, j})
				}
			} else if c == 0 {
				dst = append(dst, Pos{i, j})
			}
		}
	}

	n := len(src)
	if n == 0 {
		return 0
	}

	cost := make([][]int, n)
	for i := 0; i < n; i++ {
		cost[i] = make([]int, n)
		for j := 0; j < n; j++ {
			cost[i][j] = abs(src[i].x-dst[j].x) + abs(src[i].y-dst[j].y)
		}
	}

	size := 1 << n
	const INF int = 1 << 30
	dp := make([]int, size)
	for i := range dp {
		dp[i] = INF
	}
	dp[0] = 0

	for mask := 0; mask < size; mask++ {
		i := bits.OnesCount(uint(mask))
		if i >= n || dp[mask] == INF {
			continue
		}
		cur := dp[mask]
		for j := 0; j < n; j++ {
			if mask&(1<<j) == 0 {
				newMask := mask | (1 << j)
				val := cur + cost[i][j]
				if val < dp[newMask] {
					dp[newMask] = val
				}
			}
		}
	}

	return dp[size-1]
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def minimum_moves(grid)
  excess = []
  deficit = []

  (0...3).each do |i|
    (0...3).each do |j|
      cnt = grid[i][j]
      if cnt > 1
        (cnt - 1).times { excess << [i, j] }
      elsif cnt == 0
        deficit << [i, j]
      end
    end
  end

  n = excess.size
  return 0 if n.zero?

  m = deficit.size
  size = 1 << m
  dp = Array.new(size, Float::INFINITY)
  dp[0] = 0

  (0...size).each do |mask|
    k = mask.to_s(2).count('1')
    next if k >= n
    ex_i, ex_j = excess[k]
    (0...m).each do |j|
      next if (mask & (1 << j)) != 0
      d_i, d_j = deficit[j]
      dist = (ex_i - d_i).abs + (ex_j - d_j).abs
      new_mask = mask | (1 << j)
      val = dp[mask] + dist
      dp[new_mask] = val if val < dp[new_mask]
    end
  end

  dp[size - 1].to_i
end
```

## Scala

```scala
object Solution {
    def minimumMoves(grid: Array[Array[Int]]): Int = {
        val sources = scala.collection.mutable.ArrayBuffer[(Int, Int)]()
        val targets = scala.collection.mutable.ArrayBuffer[(Int, Int)]()
        for (i <- 0 until 3; j <- 0 until 3) {
            grid(i)(j) match {
                case cnt if cnt > 1 =>
                    for (_ <- 0 until cnt - 1) sources.append((i, j))
                case 0 => targets.append((i, j))
                case _ => // do nothing
            }
        }
        val n = sources.length
        if (n == 0) return 0

        val dist = Array.ofDim[Int](n, n)
        for (i <- 0 until n) {
            val (si, sj) = sources(i)
            for (j <- 0 until n) {
                val (ti, tj) = targets(j)
                dist(i)(j) = math.abs(si - ti) + math.abs(sj - tj)
            }
        }

        val size = 1 << n
        val INF = Int.MaxValue / 2
        val dp = Array.fill(size)(INF)
        dp(0) = 0

        for (mask <- 0 until size) {
            val i = Integer.bitCount(mask)
            if (i < n && dp(mask) < INF) {
                for (j <- 0 until n) {
                    if ((mask & (1 << j)) == 0) {
                        val newMask = mask | (1 << j)
                        val newCost = dp(mask) + dist(i)(j)
                        if (newCost < dp(newMask)) dp(newMask) = newCost
                    }
                }
            }
        }

        dp(size - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_moves(grid: Vec<Vec<i32>>) -> i32 {
        let mut surplus = Vec::new(); // positions of extra stones
        let mut deficit = Vec::new(); // empty cells

        for (i, row) in grid.iter().enumerate() {
            for (j, &cnt) in row.iter().enumerate() {
                if cnt > 1 {
                    for _ in 0..(cnt - 1) {
                        surplus.push((i as i32, j as i32));
                    }
                } else if cnt == 0 {
                    deficit.push((i as i32, j as i32));
                }
            }
        }

        let n = surplus.len();
        if n == 0 {
            return 0;
        }

        // cost matrix
        let mut cost = vec![vec![0i32; n]; n];
        for (s_idx, &(sx, sy)) in surplus.iter().enumerate() {
            for (d_idx, &(dx, dy)) in deficit.iter().enumerate() {
                cost[s_idx][d_idx] = (sx - dx).abs() + (sy - dy).abs();
            }
        }

        let size = 1usize << n;
        let mut dp = vec![i32::MAX / 2; size];
        dp[0] = 0;

        for mask in 0..size {
            let k = mask.count_ones() as usize; // number of assigned surplus stones
            if k >= n { continue; }
            for t in 0..n {
                if (mask & (1 << t)) == 0 {
                    let new_mask = mask | (1 << t);
                    let new_cost = dp[mask] + cost[k][t];
                    if new_cost < dp[new_mask] {
                        dp[new_mask] = new_cost;
                    }
                }
            }
        }

        dp[size - 1]
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define (minimum-moves grid)
  (let* ([sources '()] [targets '()])
    (for ([i (in-range 3)] [row (in-list grid)])
      (for ([j (in-range 3)] [val (in-list row)])
        (cond [(> val 1) (set! sources
                               (append sources
                                       (make-list (- val 1) (list i j))))]
              [(= val 0) (set! targets (cons (list i j) targets))])))
    (let ([m (length sources)])
      (if (= m 0)
          0
          (let* ([dist (for/list ([s sources])
                         (for/list ([t targets])
                           (+ (abs (- (first s) (first t)))
                              (abs (- (second s) (second t))))))]
                 [size (arithmetic-shift 1 m)]
                 [INF 1000000]
                 [dp (make-vector size INF)])
            (vector-set! dp 0 0)
            (for ([mask (in-range size)])
              (let* ([i (bitwise-bit-count mask)]
                     [cur (vector-ref dp mask)])
                (when (< cur INF)
                  (for ([j (in-range m)]
                        #:when (zero? (bitwise-and mask (arithmetic-shift 1 j))))
                    (let* ([newmask (bitwise-ior mask (arithmetic-shift 1 j))]
                           [newcost (+ cur (list-ref (list-ref dist i) j))])
                      (when (< newcost (vector-ref dp newmask))
                        (vector-set! dp newmask newcost)))))))
            (vector-ref dp (sub1 size)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_moves/1]).

-spec minimum_moves(Grid :: [[integer()]]) -> integer().
minimum_moves(Grid) ->
    {SurplusRev, DeficitRev} = collect(Grid, 0, [], []),
    Surplus = lists:reverse(SurplusRev),
    Deficit = lists:reverse(DeficitRev),
    N = length(Surplus),
    case N of
        0 -> 0;
        _ ->
            MaxMask = 1 bsl N,
            DPMap0 = #{0 => 0},
            DPMapFinal = dp_loop(0, MaxMask, DPMap0, Surplus, Deficit),
            maps:get(MaxMask - 1, DPMapFinal)
    end.

%% Collect surplus stones (extra copies) and empty cells
collect([], _R, SurpAcc, DefAcc) ->
    {SurpAcc, DefAcc};
collect([Row | RestRows], R, SurpAcc, DefAcc) ->
    {NewSurp, NewDef} = collect_row(Row, R, 0, SurpAcc, DefAcc),
    collect(RestRows, R + 1, NewSurp, NewDef).

collect_row([], _R, _C, SurpAcc, DefAcc) ->
    {SurpAcc, DefAcc};
collect_row([Val | RestCols], R, C, SurpAcc, DefAcc) ->
    case Val of
        0 ->
            collect_row(RestCols, R, C + 1, SurpAcc, [{R, C} | DefAcc]);
        _ when Val > 1 ->
            Extra = Val - 1,
            NewSurp = lists:duplicate(Extra, {R, C}) ++ SurpAcc,
            collect_row(RestCols, R, C + 1, NewSurp, DefAcc);
        _ -> % Val == 1
            collect_row(RestCols, R, C + 1, SurpAcc, DefAcc)
    end.

%% DP over masks
dp_loop(Mask, MaxMask, DPMap, Surplus, Deficit) when Mask < MaxMask ->
    case maps:find(Mask, DPMap) of
        {ok, CurCost} ->
            I = popcnt(Mask),
            DPMap1 = assign_from_i(I, CurCost, Mask, Surplus, Deficit, DPMap),
            dp_loop(Mask + 1, MaxMask, DPMap1, Surplus, Deficit);
        error ->
            dp_loop(Mask + 1, MaxMask, DPMap, Surplus, Deficit)
    end;
dp_loop(_, _, DPMap, _Surplus, _Deficit) ->
    DPMap.

assign_from_i(I, CurCost, Mask, Surplus, Deficit, DPMap) ->
    assign_j(0, length(Deficit), I, CurCost, Mask, Surplus, Deficit, DPMap).

assign_j(Index, N, _I, _CurCost, _Mask, _Surplus, _Deficit, DPMap) when Index >= N ->
    DPMap;
assign_j(Index, N, I, CurCost, Mask, Surplus, Deficit, DPMap) ->
    Bit = 1 bsl Index,
    case (Mask band Bit) of
        0 ->
            NewMask = Mask bor Bit,
            {SR, SC} = lists:nth(I + 1, Surplus),
            {DR, DC} = lists:nth(Index + 1, Deficit),
            Dist = abs(SR - DR) + abs(SC - DC),
            NewCost = CurCost + Dist,
            Existing = maps:get(NewMask, DPMap, 1000000),
            UpdatedDP =
                if NewCost < Existing ->
                        maps:put(NewMask, NewCost, DPMap);
                   true -> DPMap
                end,
            assign_j(Index + 1, N, I, CurCost, Mask, Surplus, Deficit, UpdatedDP);
        _ ->
            assign_j(Index + 1, N, I, CurCost, Mask, Surplus, Deficit, DPMap)
    end.

popcnt(0) -> 0;
popcnt(N) -> 1 + popcnt(N band (N - 1)).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec minimum_moves(grid :: [[integer]]) :: integer
  def minimum_moves(grid) do
    {surplus, deficit} = build_lists(grid)

    n = length(surplus)

    if n == 0 do
      0
    else
      dist =
        for s <- surplus do
          for d <- deficit do
            manhattan(s, d)
          end
        end

      max_mask = 1 <<< n
      inf = 1_000_000
      dp = :array.new(max_mask, default: inf) |> :array.set(0, 0)

      dp =
        Enum.reduce(0..max_mask - 1, dp, fn mask, acc_dp ->
          cur = :array.get(mask, acc_dp)

          if cur < inf do
            i = bit_count(mask)

            Enum.reduce(0..n - 1, acc_dp, fn j, inner_dp ->
              if (mask &&& (1 <<< j)) == 0 do
                new_mask = mask ||| (1 <<< j)
                val = cur + Enum.at(Enum.at(dist, i), j)
                old = :array.get(new_mask, inner_dp)

                if val < old,
                  do: :array.set(new_mask, val, inner_dp),
                  else: inner_dp
              else
                inner_dp
              end
            end)
          else
            acc_dp
          end
        end)

      :array.get(max_mask - 1, dp)
    end
  end

  defp build_lists(grid) do
    Enum.with_index(grid)
    |> Enum.reduce({[], []}, fn {row, i}, {s_acc, d_acc} ->
      Enum.with_index(row)
      |> Enum.reduce({s_acc, d_acc}, fn {cnt, j}, {s2, d2} ->
        cond do
          cnt > 1 ->
            extra = cnt - 1
            {s2 ++ List.duplicate({i, j}, extra), d2}

          cnt == 0 ->
            {s2, [{i, j} | d2]}

          true ->
            {s2, d2}
        end
      end)
    end)
  end

  defp manhattan({x1, y1}, {x2, y2}) do
    abs(x1 - x2) + abs(y1 - y2)
  end

  defp bit_count(0), do: 0
  defp bit_count(n), do: (n &&& 1) + bit_count(n >>> 1)
end
```

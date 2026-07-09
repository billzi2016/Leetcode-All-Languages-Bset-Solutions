# 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

## Cpp

```cpp
class Solution {
public:
    int minFlips(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int total = m * n;
        int initMask = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (mat[i][j] == 1)
                    initMask |= 1 << (i * n + j);
        
        vector<int> flipMask(total, 0);
        const int dirs[5][2] = {{0,0},{-1,0},{1,0},{0,-1},{0,1}};
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int mask = 0;
                for (auto &d : dirs) {
                    int ni = i + d[0], nj = j + d[1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n)
                        mask |= 1 << (ni * n + nj);
                }
                flipMask[i * n + j] = mask;
            }
        }
        
        int ans = INT_MAX;
        int limit = 1 << total;
        for (int s = 0; s < limit; ++s) {
            int cur = initMask;
            // apply flips indicated by bits in s
            int temp = s;
            while (temp) {
                int lsb = temp & -temp;
                int idx = __builtin_ctz(lsb);
                cur ^= flipMask[idx];
                temp ^= lsb;
            }
            if (cur == 0) {
                ans = min(ans, __builtin_popcount(s));
            }
        }
        return ans == INT_MAX ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minFlips(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int total = m * n;
        int best = Integer.MAX_VALUE;

        for (int mask = 0; mask < (1 << total); mask++) {
            int[][] cur = new int[m][n];
            for (int i = 0; i < m; i++) {
                System.arraycopy(mat[i], 0, cur[i], 0, n);
            }

            for (int k = 0; k < total; k++) {
                if (((mask >> k) & 1) == 1) {
                    int r = k / n;
                    int c = k % n;
                    // flip (r,c)
                    cur[r][c] ^= 1;
                    // up
                    if (r > 0) cur[r - 1][c] ^= 1;
                    // down
                    if (r + 1 < m) cur[r + 1][c] ^= 1;
                    // left
                    if (c > 0) cur[r][c - 1] ^= 1;
                    // right
                    if (c + 1 < n) cur[r][c + 1] ^= 1;
                }
            }

            boolean allZero = true;
            for (int i = 0; i < m && allZero; i++) {
                for (int j = 0; j < n; j++) {
                    if (cur[i][j] != 0) {
                        allZero = false;
                        break;
                    }
                }
            }

            if (allZero) {
                int flips = Integer.bitCount(mask);
                if (flips < best) best = flips;
            }
        }

        return best == Integer.MAX_VALUE ? -1 : best;
    }
}
```

## Python

```python
class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        from collections import deque

        m, n = len(mat), len(mat[0])
        # encode matrix to bitmask
        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1 << (i * n + j)

        # precompute flip masks for each cell
        flips = []
        dirs = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                mask = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        mask |= 1 << (ni * n + nj)
                flips.append(mask)

        # BFS over states
        queue = deque()
        queue.append((start, 0))
        visited = {start}
        while queue:
            cur, steps = queue.popleft()
            if cur == 0:
                return steps
            for f in flips:
                nxt = cur ^ f
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1
```

## Python3

```python
class Solution:
    def minFlips(self, mat):
        from itertools import product
        m, n = len(mat), len(mat[0])
        total = m * n

        # encode initial matrix into bits
        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1 << (i * n + j)

        # precompute flip mask for each cell
        masks = []
        for i in range(m):
            for j in range(n):
                mask = 0
                for di, dj in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        mask |= 1 << (ni * n + nj)
                masks.append(mask)

        ans = float('inf')
        for subset in range(1 << total):
            cur = start
            s = subset
            idx = 0
            while s:
                if s & 1:
                    cur ^= masks[idx]
                s >>= 1
                idx += 1
            # remaining bits where subset has 0 are ignored; need to process those indices too?
            # Actually we only toggled for bits set; others do nothing.
            if cur == 0:
                flips = subset.bit_count()
                if flips < ans:
                    ans = flips

        return -1 if ans == float('inf') else ans
```

## C

```c
#include <string.h>

int minFlips(int** mat, int matSize, int* matColSize) {
    int m = matSize;
    int n = matColSize[0];
    int total = m * n;
    const int INF = 1 << 30;
    int ans = INF;

    int orig[9];
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            orig[i * n + j] = mat[i][j];

    const int dirs[5][2] = {{0,0},{1,0},{-1,0},{0,1},{0,-1}};
    int maxMask = 1 << total;

    for (int mask = 0; mask < maxMask; ++mask) {
        int cur[9];
        memcpy(cur, orig, total * sizeof(int));

        for (int idx = 0; idx < total; ++idx) {
            if (mask & (1 << idx)) {
                int r = idx / n;
                int c = idx % n;
                for (int d = 0; d < 5; ++d) {
                    int nr = r + dirs[d][0];
                    int nc = c + dirs[d][1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                        int pos = nr * n + nc;
                        cur[pos] ^= 1;
                    }
                }
            }
        }

        int allZero = 1;
        for (int i = 0; i < total; ++i) {
            if (cur[i]) { allZero = 0; break; }
        }
        if (allZero) {
            int flips = __builtin_popcount(mask);
            if (flips < ans) ans = flips;
        }
    }

    return ans == INF ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinFlips(int[][] mat)
    {
        int m = mat.Length;
        int n = mat[0].Length;
        int total = m * n;

        // initial state mask
        int initMask = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (mat[i][j] == 1)
                    initMask |= 1 << (i * n + j);
            }
        }

        // precompute effect of flipping each cell
        int[] effect = new int[total];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int mask = 0;
                int idx = i * n + j;
                mask |= 1 << idx; // self
                if (i > 0) mask |= 1 << ((i - 1) * n + j);
                if (i + 1 < m) mask |= 1 << ((i + 1) * n + j);
                if (j > 0) mask |= 1 << (i * n + (j - 1));
                if (j + 1 < n) mask |= 1 << (i * n + (j + 1));
                effect[idx] = mask;
            }
        }

        int limit = 1 << total;
        int best = int.MaxValue;

        for (int subset = 0; subset < limit; subset++)
        {
            int cur = initMask;
            for (int k = 0; k < total; k++)
            {
                if (((subset >> k) & 1) == 1)
                    cur ^= effect[k];
            }

            if (cur == 0)
            {
                int flips = CountBits(subset);
                if (flips < best) best = flips;
            }
        }

        return best == int.MaxValue ? -1 : best;
    }

    private int CountBits(int x)
    {
        int cnt = 0;
        while (x != 0)
        {
            cnt++;
            x &= x - 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var minFlips = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const totalMasks = 1 << (m * n);
    let best = Infinity;

    for (let mask = 0; mask < totalMasks; ++mask) {
        // copy original matrix
        const cur = Array.from({ length: m }, (_, i) => mat[i].slice());
        let flips = 0;

        for (let i = 0; i < m; ++i) {
            for (let j = 0; j < n; ++j) {
                const bitIdx = i * n + j;
                if ((mask >> bitIdx) & 1) {
                    flips++;
                    // flip self
                    cur[i][j] ^= 1;
                    // up
                    if (i > 0) cur[i - 1][j] ^= 1;
                    // down
                    if (i < m - 1) cur[i + 1][j] ^= 1;
                    // left
                    if (j > 0) cur[i][j - 1] ^= 1;
                    // right
                    if (j < n - 1) cur[i][j + 1] ^= 1;
                }
            }
        }

        let allZero = true;
        for (let i = 0; i < m && allZero; ++i) {
            for (let j = 0; j < n; ++j) {
                if (cur[i][j] === 1) {
                    allZero = false;
                    break;
                }
            }
        }

        if (allZero) best = Math.min(best, flips);
    }

    return best === Infinity ? -1 : best;
};
```

## Typescript

```typescript
function minFlips(mat: number[][]): number {
    const m = mat.length;
    const n = mat[0].length;
    const total = m * n;

    // Encode initial matrix as a bitmask
    let startMask = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (mat[i][j] === 1) {
                startMask |= 1 << (i * n + j);
            }
        }
    }

    // Precompute toggle masks for each cell
    const toggleMasks: number[] = new Array(total).fill(0);
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const idx = i * n + j;
            let mask = 0;
            mask |= 1 << idx; // self
            if (i > 0) mask |= 1 << ((i - 1) * n + j); // up
            if (i < m - 1) mask |= 1 << ((i + 1) * n + j); // down
            if (j > 0) mask |= 1 << (i * n + (j - 1)); // left
            if (j < n - 1) mask |= 1 << (i * n + (j + 1)); // right
            toggleMasks[idx] = mask;
        }
    }

    const limit = 1 << total;
    let ans = Infinity;

    const bitCount = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    };

    for (let mask = 0; mask < limit; ++mask) {
        let cur = startMask;
        for (let i = 0; i < total; ++i) {
            if ((mask >> i) & 1) {
                cur ^= toggleMasks[i];
            }
        }
        if (cur === 0) {
            const cnt = bitCount(mask);
            if (cnt < ans) ans = cnt;
        }
    }

    return ans === Infinity ? -1 : ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function minFlips($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $total = $m * $n;
        $maxMask = 1 << $total;
        $best = PHP_INT_MAX;

        for ($mask = 0; $mask < $maxMask; $mask++) {
            // copy matrix
            $grid = [];
            for ($i = 0; $i < $m; $i++) {
                $grid[$i] = $mat[$i];
            }
            $flips = 0;
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    $pos = $i * $n + $j;
                    if ((($mask >> $pos) & 1) === 1) {
                        $flips++;
                        // toggle self and neighbors
                        $dirs = [[0,0],[1,0],[-1,0],[0,1],[0,-1]];
                        foreach ($dirs as $d) {
                            $ni = $i + $d[0];
                            $nj = $j + $d[1];
                            if ($ni >= 0 && $ni < $m && $nj >= 0 && $nj < $n) {
                                $grid[$ni][$nj] ^= 1;
                            }
                        }
                    }
                }
            }

            // check all zero
            $ok = true;
            for ($i = 0; $i < $m && $ok; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    if ($grid[$i][$j] !== 0) {
                        $ok = false;
                        break;
                    }
                }
            }

            if ($ok && $flips < $best) {
                $best = $flips;
            }
        }

        return $best === PHP_INT_MAX ? -1 : $best;
    }
}
```

## Swift

```swift
class Solution {
    func minFlips(_ mat: [[Int]]) -> Int {
        let m = mat.count
        let n = mat[0].count
        let total = m * n
        
        var start = 0
        for i in 0..<m {
            for j in 0..<n {
                if mat[i][j] == 1 {
                    let pos = i * n + j
                    start |= (1 << pos)
                }
            }
        }
        
        // Precompute toggle masks for each cell
        var toggle = [Int](repeating: 0, count: total)
        let dirs = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
        for i in 0..<m {
            for j in 0..<n {
                var mask = 0
                for (dx, dy) in dirs {
                    let ni = i + dx
                    let nj = j + dy
                    if ni >= 0 && ni < m && nj >= 0 && nj < n {
                        let pos = ni * n + nj
                        mask |= (1 << pos)
                    }
                }
                toggle[i * n + j] = mask
            }
        }
        
        var answer = Int.max
        let limit = 1 << total
        
        for flipMask in 0..<limit {
            var state = start
            var fm = flipMask
            var idx = 0
            while fm != 0 {
                if (fm & 1) == 1 {
                    state ^= toggle[idx]
                }
                fm >>= 1
                idx += 1
            }
            // Remaining bits are zero, no effect
            
            if state == 0 {
                let flips = flipMask.nonzeroBitCount
                if flips < answer { answer = flips }
            }
        }
        
        return answer == Int.max ? -1 : answer
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun minFlips(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val total = m * n
        var start = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (mat[i][j] == 1) {
                    start = start or (1 shl (i * n + j))
                }
            }
        }
        if (start == 0) return 0

        val flipMasks = IntArray(total)
        val dirs = arrayOf(
            intArrayOf(0, 0),
            intArrayOf(-1, 0),
            intArrayOf(1, 0),
            intArrayOf(0, -1),
            intArrayOf(0, 1)
        )
        for (i in 0 until m) {
            for (j in 0 until n) {
                var mask = 0
                for (d in dirs) {
                    val ni = i + d[0]
                    val nj = j + d[1]
                    if (ni in 0 until m && nj in 0 until n) {
                        mask = mask or (1 shl (ni * n + nj))
                    }
                }
                flipMasks[i * n + j] = mask
            }
        }

        val maxState = 1 shl total
        val dist = IntArray(maxState) { -1 }
        val queue: ArrayDeque<Int> = ArrayDeque()
        dist[start] = 0
        queue.add(start)

        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            val d = dist[cur]
            if (cur == 0) return d
            for (idx in 0 until total) {
                val next = cur xor flipMasks[idx]
                if (dist[next] == -1) {
                    dist[next] = d + 1
                    queue.add(next)
                }
            }
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int minFlips(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    int totalBits = m * n;

    // Encode initial matrix into a bitmask
    int start = 0;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 1) {
          start |= 1 << (i * n + j);
        }
      }
    }

    // Precompute flip masks for each cell
    List<int> flipMasks = List.filled(totalBits, 0);
    const List<List<int>> dirs = [
      [0, 0],
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int mask = 0;
        for (var d in dirs) {
          int ni = i + d[0];
          int nj = j + d[1];
          if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
            mask |= 1 << (ni * n + nj);
          }
        }
        flipMasks[i * n + j] = mask;
      }
    }

    if (start == 0) return 0;

    // BFS over states
    Queue<int> q = Queue<int>();
    Set<int> visited = <int>{};
    q.add(start);
    visited.add(start);
    int steps = 0;

    while (q.isNotEmpty) {
      int size = q.length;
      for (int s = 0; s < size; s++) {
        int cur = q.removeFirst();
        if (cur == 0) return steps;
        for (int idx = 0; idx < totalBits; idx++) {
          int next = cur ^ flipMasks[idx];
          if (!visited.contains(next)) {
            visited.add(next);
            q.add(next);
          }
        }
      }
      steps++;
    }

    return -1;
  }
}
```

## Golang

```go
import "math/bits"

func minFlips(mat [][]int) int {
	m, n := len(mat), len(mat[0])
	total := m * n

	// initial state as bitmask
	start := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] == 1 {
				pos := i*n + j
				start |= 1 << pos
			}
		}
	}

	// precompute toggle masks for each cell
	toggles := make([]int, total)
	dirs := [][]int{{0, 0}, {-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			mask := 0
			for _, d := range dirs {
				ni, nj := i+d[0], j+d[1]
				if ni >= 0 && ni < m && nj >= 0 && nj < n {
					pos := ni*n + nj
					mask |= 1 << pos
				}
			}
			toggles[i*n+j] = mask
		}
	}

	ans := total + 1
	limit := 1 << total
	for flipMask := 0; flipMask < limit; flipMask++ {
		state := start
		fm := flipMask
		for fm != 0 {
			lsb := fm & -fm
			idx := bits.TrailingZeros(uint(lsb))
			state ^= toggles[idx]
			fm &= fm - 1
		}
		if state == 0 {
			cnt := bits.OnesCount(uint(flipMask))
			if cnt < ans {
				ans = cnt
			}
		}
	}

	if ans == total+1 {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def min_flips(mat)
  m = mat.size
  n = mat[0].size
  total = m * n
  best = Float::INFINITY

  (0...(1 << total)).each do |mask|
    grid = mat.map { |row| row.clone }
    flips = 0

    total.times do |k|
      next if ((mask >> k) & 1).zero?
      i = k / n
      j = k % n
      flips += 1
      [[i, j], [i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]].each do |x, y|
        if x.between?(0, m - 1) && y.between?(0, n - 1)
          grid[x][y] ^= 1
        end
      end
    end

    all_zero = true
    m.times do |i|
      n.times do |j|
        if grid[i][j] == 1
          all_zero = false
          break
        end
      end
      break unless all_zero
    end

    best = flips if all_zero && flips < best
  end

  best == Float::INFINITY ? -1 : best
end
```

## Scala

```scala
object Solution {
  def minFlips(mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    var ans = Int.MaxValue

    val totalMask = 1 << n
    for (mask <- 0 until totalMask) {
      // copy matrix
      val grid = Array.ofDim[Int](m, n)
      var i = 0
      while (i < m) {
        var j = 0
        while (j < n) {
          grid(i)(j) = mat(i)(j)
          j += 1
        }
        i += 1
      }

      var flips = 0

      // apply first row decisions according to mask
      var col = 0
      while (col < n) {
        if (((mask >> col) & 1) == 1) {
          flip(grid, 0, col)
          flips += 1
        }
        col += 1
      }

      // determine flips for subsequent rows
      var row = 1
      while (row < m) {
        var c = 0
        while (c < n) {
          if (grid(row - 1)(c) == 1) {
            flip(grid, row, c)
            flips += 1
          }
          c += 1
        }
        row += 1
      }

      // check if last row is all zero
      var ok = true
      var j = 0
      while (j < n && ok) {
        if (grid(m - 1)(j) == 1) ok = false
        j += 1
      }
      if (ok) ans = math.min(ans, flips)
    }

    if (ans == Int.MaxValue) -1 else ans
  }

  private def flip(grid: Array[Array[Int]], i: Int, j: Int): Unit = {
    val m = grid.length
    val n = grid(0).length
    // self
    grid(i)(j) ^= 1
    // up
    if (i > 0) grid(i - 1)(j) ^= 1
    // down
    if (i + 1 < m) grid(i + 1)(j) ^= 1
    // left
    if (j > 0) grid(i)(j - 1) ^= 1
    // right
    if (j + 1 < n) grid(i)(j + 1) ^= 1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_flips(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let total = m * n;
        // precompute flip masks for each cell
        let mut flip_masks = vec![0usize; total];
        for i in 0..m {
            for j in 0..n {
                let idx = i * n + j;
                let mut mask = 1usize << idx;
                if i > 0 {
                    mask |= 1usize << ((i - 1) * n + j);
                }
                if i + 1 < m {
                    mask |= 1usize << ((i + 1) * n + j);
                }
                if j > 0 {
                    mask |= 1usize << (i * n + (j - 1));
                }
                if j + 1 < n {
                    mask |= 1usize << (i * n + (j + 1));
                }
                flip_masks[idx] = mask;
            }
        }
        // initial state mask
        let mut start = 0usize;
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 1 {
                    start |= 1usize << (i * n + j);
                }
            }
        }

        let limit = 1usize << total;
        let mut best = usize::MAX;

        for mask in 0..limit {
            let mut cur = start;
            for p in 0..total {
                if (mask >> p) & 1 == 1 {
                    cur ^= flip_masks[p];
                }
            }
            if cur == 0 {
                let flips = mask.count_ones() as usize;
                if flips < best {
                    best = flips;
                }
            }
        }

        if best == usize::MAX {
            -1
        } else {
            best as i32
        }
    }
}
```

## Racket

```racket
(define/contract (min-flips mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length mat))
         (n (if (zero? m) 0 (length (car mat))))
         (total (* m n))
         (max-mask (expt 2 total))
         (inf +inf.0)
         (best inf))

    ;; helper to toggle a cell in mutable matrix
    (define (toggle! mm i j)
      (let* ((row (vector-ref mm i))
             (val (vector-ref row j)))
        (vector-set! row j (bitwise-xor val 1))))

    ;; check if all cells are zero
    (define (all-zero? mm)
      (for/and ([i (in-range m)])
        (let ((row (vector-ref mm i)))
          (for/and ([j (in-range n)])
            (= (vector-ref row j) 0)))))

    ;; iterate over all possible flip subsets
    (for ([mask (in-range max-mask)])
      (let* ((mm (make-vector m))
             ;; copy original matrix into mutable vectors
             (_ (for ([i (in-range m)]
                      [row (in-list mat)])
                  (vector-set! mm i (list->vector row))))
             (flips 0))

        ;; apply flips according to mask bits
        (for ([k (in-range total)])
          (when (bitwise-bit-set? mask k)
            (set! flips (+ flips 1))
            (define i (quotient k n))
            (define j (remainder k n))
            (toggle! mm i j)
            (when (> i 0)      (toggle! mm (- i 1) j))
            (when (< i (- m 1)) (toggle! mm (+ i 1) j))
            (when (> j 0)      (toggle! mm i (- j 1)))
            (when (< j (- n 1)) (toggle! mm i (+ j 1)))))

        ;; if resulting matrix is all zero, possibly update best
        (when (and (= flips best) (all-zero? mm))
          (set! best flips))
        (when (and (< flips best) (all-zero? mm))
          (set! best flips))))

    (if (finite? best) best -1)))
```

## Erlang

```erlang
-spec min_flips(Mat :: [[integer()]]) -> integer().
min_flips(Mat) ->
    M = length(Mat),
    N = length(hd(Mat)),
    Total = M * N,
    MatFlat = [Elem || Row <- Mat, Elem <- Row],
    InfluenceMasks = [calc_influence(Index, M, N) || Index <- lists:seq(0, Total - 1)],
    MaxMask = (1 bsl Total) - 1,
    Best = find_min(0, MaxMask, MatFlat, InfluenceMasks, Total + 1),
    if Best =< Total -> Best; true -> -1 end.

calc_influence(Index, M, N) ->
    I = Index div N,
    J = Index rem N,
    Positions = [{I, J}, {I - 1, J}, {I + 1, J}, {I, J - 1}, {I, J + 1}],
    lists:foldl(fun({R, C}, Acc) ->
        if R >= 0, R < M, C >= 0, C < N ->
                PosIdx = R * N + C,
                Acc bor (1 bsl PosIdx);
           true -> Acc
        end
    end, 0, Positions).

parity(0) -> 0;
parity(B) -> parity(B band (B - 1), 0).
parity(0, Acc) -> Acc;
parity(B, Acc) -> parity(B band (B - 1), Acc bxor 1).

popcount(0) -> 0;
popcount(B) -> 1 + popcount(B band (B - 1)).

find_min(CurrentMask, MaxMask, MatFlat, InfluenceMasks, Best) when CurrentMask > MaxMask ->
    Best;
find_min(CurrentMask, MaxMask, MatFlat, InfluenceMasks, Best) ->
    case all_zero(CurrentMask, MatFlat, InfluenceMasks) of
        true ->
            Flips = popcount(CurrentMask),
            NewBest = if Flips < Best -> Flips; true -> Best end,
            find_min(CurrentMask + 1, MaxMask, MatFlat, InfluenceMasks, NewBest);
        false ->
            find_min(CurrentMask + 1, MaxMask, MatFlat, InfluenceMasks, Best)
    end.

all_zero(Mask, MatFlat, InfluenceMasks) ->
    all_zero(0, length(MatFlat), Mask, MatFlat, InfluenceMasks).

all_zero(Index, Len, _Mask, _MatFlat, _InfluenceMasks) when Index == Len -> true;
all_zero(Index, Len, Mask, MatFlat, InfluenceMasks) ->
    Init = lists:nth(Index + 1, MatFlat),
    InfMask = lists:nth(Index + 1, InfluenceMasks),
    Par = parity(Mask band InfMask),
    if (Init bxor Par) =:= 0 ->
            all_zero(Index + 1, Len, Mask, MatFlat, InfluenceMasks);
       true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec min_flips(mat :: [[integer]]) :: integer
  def min_flips(mat) do
    m = length(mat)
    n = length(List.first(mat))
    total = m * n

    start_state = encode(mat, m, n)

    flip_masks =
      for i <- 0..(m - 1), j <- 0..(n - 1) do
        idx = i * n + j
        mask = 1 <<< idx

        mask =
          if i > 0, do: mask ||| (1 <<< ((i - 1) * n + j)), else: mask

        mask =
          if i < m - 1, do: mask ||| (1 <<< ((i + 1) * n + j)), else: mask

        mask =
          if j > 0, do: mask ||| (1 <<< (i * n + (j - 1))), else: mask

        mask =
          if j < n - 1, do: mask ||| (1 <<< (i * n + (j + 1))), else: mask

        mask
      end

    max_mask = 1 <<< total

    best =
      Enum.reduce(0..(max_mask - 1), nil, fn mask, cur_best ->
        combined = combine(mask, flip_masks)
        final_state = start_state ^^^ combined

        if final_state == 0 do
          cnt = popcnt(mask)

          cond do
            cur_best == nil -> cnt
            cnt < cur_best -> cnt
            true -> cur_best
          end
        else
          cur_best
        end
      end)

    case best do
      nil -> -1
      v -> v
    end
  end

  defp encode(mat, m, n) do
    Enum.reduce(0..(m - 1), 0, fn i, acc ->
      row = Enum.at(mat, i)

      Enum.reduce(0..(n - 1), acc, fn j, a2 ->
        if Enum.at(row, j) == 1 do
          a2 ||| (1 <<< (i * n + j))
        else
          a2
        end
      end)
    end)
  end

  defp combine(mask, flip_masks) do
    Enum.reduce(0..(length(flip_masks) - 1), 0, fn idx, acc ->
      if (mask &&& (1 <<< idx)) != 0 do
        acc ^^^ Enum.at(flip_masks, idx)
      else
        acc
      end
    end)
  end

  defp popcnt(0), do: 0
  defp popcnt(x), do: popcnt(x &&& (x - 1)) + 1
end
```

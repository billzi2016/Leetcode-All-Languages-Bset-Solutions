# 2328. Number of Increasing Paths in a Grid

## Cpp

```cpp
class Solution {
public:
    int countPaths(vector<vector<int>>& grid) {
        const int MOD = 1'000'000'007;
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 1));
        vector<tuple<int,int,int>> cells;
        cells.reserve(m * n);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cells.emplace_back(grid[i][j], i, j);
            }
        }
        sort(cells.begin(), cells.end(),
             [](const auto& a, const auto& b) { return get<0>(a) > get<0>(b); });
        long long ans = 0;
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        for (auto &cell : cells) {
            int val, i, j;
            tie(val, i, j) = cell;
            for (auto &d : dirs) {
                int ni = i + d[0];
                int nj = j + d[1];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] > val) {
                    dp[i][j] += dp[ni][nj];
                    if (dp[i][j] >= MOD) dp[i][j] -= MOD;
                }
            }
            ans += dp[i][j];
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int countPaths(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int total = m * n;
        Cell[] cells = new Cell[total];
        int idx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cells[idx++] = new Cell(grid[i][j], i, j);
            }
        }
        java.util.Arrays.sort(cells, (a, b) -> Integer.compare(a.val, b.val));
        
        long[][] dp = new long[m][n];
        for (int i = 0; i < m; i++) {
            java.util.Arrays.fill(dp[i], 1L);
        }
        
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        
        for (Cell c : cells) {
            long cur = dp[c.r][c.c];
            int v = c.val;
            for (int d = 0; d < 4; d++) {
                int nr = c.r + dr[d];
                int nc = c.c + dc[d];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > v) {
                    dp[nr][nc] += cur;
                    if (dp[nr][nc] >= MOD) dp[nr][nc] -= MOD;
                }
            }
        }
        
        long ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans += dp[i][j];
                if (ans >= MOD) ans -= MOD;
            }
        }
        return (int) ans;
    }
    
    private static class Cell {
        int val, r, c;
        Cell(int v, int row, int col) { this.val = v; this.r = row; this.c = col; }
    }
}
```

## Python

```python
class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        cells = []
        for i in range(m):
            row = grid[i]
            for j in range(n):
                cells.append((row[j], i, j))
        cells.sort()
        dp = [[0] * n for _ in range(m)]
        ans = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for val, i, j in cells:
            cnt = 1  # path consisting of the cell itself
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < val:
                    cnt += dp[ni][nj]
            cnt %= MOD
            dp[i][j] = cnt
            ans += cnt
            if ans >= MOD:
                ans -= MOD
        return ans % MOD
```

## Python3

```python
class Solution:
    def countPaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        cells = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort()
        ans = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for val, i, j in cells:
            total = 1  # path consisting of only this cell
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < val:
                    total += dp[ni][nj]
            total %= MOD
            dp[i][j] = total
            ans = (ans + total) % MOD
        return ans
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007

typedef struct {
    int val;
    int r;
    int c;
} Cell;

static int cmpCell(const void *a, const void *b) {
    int va = ((const Cell *)a)->val;
    int vb = ((const Cell *)b)->val;
    return (va > vb) - (va < vb);
}

int countPaths(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int total = m * n;

    Cell *cells = (Cell *)malloc(total * sizeof(Cell));
    if (!cells) return 0;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int idx = i * n + j;
            cells[idx].val = grid[i][j];
            cells[idx].r = i;
            cells[idx].c = j;
        }
    }

    qsort(cells, total, sizeof(Cell), cmpCell);

    int *dp = (int *)calloc(total, sizeof(int));
    if (!dp) {
        free(cells);
        return 0;
    }

    long long answer = 0;
    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    for (int k = 0; k < total; ++k) {
        int r = cells[k].r;
        int c = cells[k].c;
        long long ways = 1; // path consisting of the cell itself

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                if (grid[nr][nc] < grid[r][c]) {
                    ways += dp[nr * n + nc];
                    if (ways >= MOD) ways -= MOD;
                }
            }
        }

        int curIdx = r * n + c;
        dp[curIdx] = (int)(ways % MOD);
        answer += dp[curIdx];
        if (answer >= MOD) answer -= MOD;
    }

    free(cells);
    free(dp);
    return (int)answer;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    public int CountPaths(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        int total = m * n;
        var cells = new (int val, int i, int j)[total];
        int idx = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cells[idx++] = (grid[i][j], i, j);
            }
        }

        Array.Sort(cells, (a, b) => a.val.CompareTo(b.val));

        long[,] dp = new long[m, n];
        long ans = 0;
        int[] dirs = new int[] { -1, 0, 1, 0, -1 };

        foreach (var cell in cells)
        {
            int i = cell.i, j = cell.j;
            long ways = 1; // path consisting of the cell itself
            for (int d = 0; d < 4; d++)
            {
                int ni = i + dirs[d];
                int nj = j + dirs[d + 1];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] < cell.val)
                {
                    ways += dp[ni, nj];
                    if (ways >= MOD) ways -= MOD;
                }
            }
            dp[i, j] = ways % MOD;
            ans += ways;
            if (ans >= MOD) ans -= MOD;
        }

        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPaths = function(grid) {
    const MOD = 1000000007;
    const m = grid.length, n = grid[0].length;
    const cells = [];
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            cells.push([grid[i][j], i, j]);
        }
    }
    cells.sort((a, b) => a[0] - b[0]);

    const dp = Array.from({ length: m }, () => Array(n).fill(0));
    let ans = 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];

    for (const [val, i, j] of cells) {
        let ways = 1; // path consisting only this cell
        for (const [dx, dy] of dirs) {
            const ni = i + dx, nj = j + dy;
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] < val) {
                ways += dp[ni][nj];
                if (ways >= MOD) ways -= MOD;
            }
        }
        ways %= MOD;
        dp[i][j] = ways;
        ans += ways;
        if (ans >= MOD) ans -= MOD;
    }

    return ans % MOD;
};
```

## Typescript

```typescript
function countPaths(grid: number[][]): number {
    const MOD = 1_000_000_007;
    const m = grid.length;
    const n = grid[0].length;

    const cells: { val: number; i: number; j: number }[] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            cells.push({ val: grid[i][j], i, j });
        }
    }

    // Process from larger values to smaller ones
    cells.sort((a, b) => b.val - a.val);

    const dp: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    let ans = 0;
    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ];

    for (const { val, i, j } of cells) {
        let ways = 1; // path consisting only this cell
        for (const [dx, dy] of dirs) {
            const ni = i + dx;
            const nj = j + dy;
            if (
                ni >= 0 &&
                ni < m &&
                nj >= 0 &&
                nj < n &&
                grid[ni][nj] > val
            ) {
                ways += dp[ni][nj];
                if (ways >= MOD) ways -= MOD;
            }
        }
        dp[i][j] = ways % MOD;
        ans += dp[i][j];
        if (ans >= MOD) ans -= MOD;
    }

    return ans % MOD;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countPaths($grid) {
        $mod = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);
        $cells = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $cells[] = [$grid[$i][$j], $i, $j];
            }
        }
        usort($cells, function($a, $b) {
            return $a[0] <=> $b[0];
        });
        $dp = array_fill(0, $m, array_fill(0, $n, 0));
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        $ans = 0;
        foreach ($cells as $cell) {
            [$val, $i, $j] = $cell;
            $cnt = 1; // path consisting of the cell itself
            foreach ($dirs as $d) {
                $ni = $i + $d[0];
                $nj = $j + $d[1];
                if ($ni >= 0 && $ni < $m && $nj >= 0 && $nj < $n && $grid[$ni][$nj] < $val) {
                    $cnt = ($cnt + $dp[$ni][$nj]) % $mod;
                }
            }
            $dp[$i][$j] = $cnt;
            $ans = ($ans + $cnt) % $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countPaths(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var cells: [(value: Int, i: Int, j: Int)] = []
        cells.reserveCapacity(m * n)
        for i in 0..<m {
            for j in 0..<n {
                cells.append((grid[i][j], i, j))
            }
        }
        cells.sort { $0.value > $1.value }   // descending by value
        
        var dp = Array(repeating: Array(repeating: Int64(0), count: n), count: m)
        let MOD: Int64 = 1_000_000_007
        var answer: Int64 = 0
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for cell in cells {
            let i = cell.i
            let j = cell.j
            var cnt: Int64 = 1   // path consisting of the cell itself
            for d in dirs {
                let ni = i + d.0
                let nj = j + d.1
                if ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] > cell.value {
                    cnt += dp[ni][nj]
                    if cnt >= MOD { cnt -= MOD }   // keep within range during accumulation
                }
            }
            cnt %= MOD
            dp[i][j] = cnt
            answer += cnt
            if answer >= MOD { answer -= MOD }
        }
        
        return Int(answer % MOD)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun countPaths(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val total = m * n
        val indices = IntArray(total) { it }
        // sort indices by cell value descending
        Arrays.sort(indices) { a, b ->
            val diff = grid[b / n][b % n] - grid[a / n][a % n]
            if (diff != 0) diff else a - b
        }

        val dp = LongArray(total)
        var ans = 0L
        val MOD = 1_000_000_007L
        val dirs = intArrayOf(-1, 0, 1, 0, -1)

        for (idx in indices) {
            val i = idx / n
            val j = idx % n
            var ways = 1L // path consisting of the cell itself
            for (k in 0 until 4) {
                val ni = i + dirs[k]
                val nj = j + dirs[k + 1]
                if (ni in 0 until m && nj in 0 until n && grid[ni][nj] > grid[i][j]) {
                    val nIdx = ni * n + nj
                    ways += dp[nIdx]
                    if (ways >= MOD) ways -= MOD
                }
            }
            dp[idx] = ways
            ans += ways
            if (ans >= MOD) ans -= MOD
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int countPaths(List<List<int>> grid) {
    final int m = grid.length;
    final int n = grid[0].length;
    // dp[i][j] stores number of increasing paths starting at (i,j)
    List<List<int>> dp = List.generate(m, (_) => List.filled(n, 1));

    // Collect cells with their values
    List<_Cell> cells = [];
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        cells.add(_Cell(grid[i][j], i, j));
      }
    }

    // Sort cells by value ascending
    cells.sort((a, b) => a.val.compareTo(b.val));

    const List<int> dirs = [-1, 0, 1, 0, -1]; // for four directions

    for (final cell in cells) {
      int i = cell.i;
      int j = cell.j;
      int curVal = cell.val;
      int curDp = dp[i][j];
      for (int d = 0; d < 4; ++d) {
        int ni = i + dirs[d];
        int nj = j + dirs[d + 1];
        if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] < curVal) {
          curDp += dp[ni][nj];
          if (curDp >= _MOD) curDp -= _MOD;
        }
      }
      dp[i][j] = curDp;
    }

    int ans = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        ans += dp[i][j];
        if (ans >= _MOD) ans -= _MOD;
      }
    }
    return ans;
  }
}

class _Cell {
  final int val;
  final int i;
  final int j;
  _Cell(this.val, this.i, this.j);
}
```

## Golang

```go
import "sort"

const MOD int64 = 1000000007

func countPaths(grid [][]int) int {
	m, n := len(grid), len(grid[0])

	type Cell struct{ val, i, j int }
	cells := make([]Cell, 0, m*n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			cells = append(cells, Cell{grid[i][j], i, j})
		}
	}
	sort.Slice(cells, func(a, b int) bool { return cells[a].val < cells[b].val })

	dp := make([][]int64, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int64, n)
	}

	var ans int64
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	for _, c := range cells {
		sum := int64(1) // path consisting of the cell itself
		for _, d := range dirs {
			ni, nj := c.i+d[0], c.j+d[1]
			if ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] < c.val {
				sum += dp[ni][nj]
				if sum >= MOD {
					sum %= MOD
				}
			}
		}
		sum %= MOD
		dp[c.i][c.j] = sum
		ans += sum
		if ans >= MOD {
			ans %= MOD
		}
	}

	return int(ans % MOD)
}
```

## Ruby

```ruby
def count_paths(grid)
  m = grid.length
  n = grid[0].length
  mod = 1_000_000_007

  cells = []
  m.times do |i|
    n.times do |j|
      cells << [grid[i][j], i, j]
    end
  end
  cells.sort_by! { |c| c[0] }

  dp = Array.new(m) { Array.new(n, 1) }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  cells.each do |val, i, j|
    cur = dp[i][j]
    dirs.each do |dx, dy|
      ni = i + dx
      nj = j + dy
      next if ni < 0 || ni >= m || nj < 0 || nj >= n
      next unless grid[ni][nj] > val
      dp[ni][nj] += cur
      dp[ni][nj] -= mod if dp[ni][nj] >= mod
    end
  end

  ans = 0
  dp.each do |row|
    row.each do |v|
      ans += v
      ans -= mod if ans >= mod
    end
  end
  ans % mod
end
```

## Scala

```scala
object Solution {
    def countPaths(grid: Array[Array[Int]]): Int = {
        val MOD = 1000000007L
        val m = grid.length
        val n = grid(0).length
        val total = m * n

        // collect cells with their values and coordinates
        val cells = new Array[(Int, Int, Int)](total)
        var idx = 0
        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                cells(idx) = (grid(i)(j), i, j)
                idx += 1
                j += 1
            }
            i += 1
        }

        // sort cells by value ascending
        scala.util.Sorting.stableSort(cells)(Ordering.by[(Int, Int, Int), Int](_._1))

        // dp[x][y] = number of increasing paths starting at (x,y)
        val dp = Array.ofDim[Long](m, n)
        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                dp(i)(j) = 1L // path consisting of the cell itself
                j += 1
            }
            i += 1
        }

        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

        var k = 0
        while (k < total) {
            val (value, x, y) = cells(k)
            val cur = dp(x)(y)
            var d = 0
            while (d < 4) {
                val nx = x + dirs(d)._1
                val ny = y + dirs(d)._2
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid(nx)(ny) > value) {
                    dp(nx)(ny) = (dp(nx)(ny) + cur) % MOD
                }
                d += 1
            }
            k += 1
        }

        var ans = 0L
        i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                ans += dp(i)(j)
                if (ans >= MOD) ans -= MOD
                j += 1
            }
            i += 1
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_paths(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut cells = Vec::with_capacity(m * n);
        for i in 0..m {
            for j in 0..n {
                cells.push((grid[i][j], i, j));
            }
        }
        cells.sort_by_key(|k| k.0);
        const MOD: i64 = 1_000_000_007;
        let mut dp = vec![1i64; m * n];
        let dirs = [(1_i32, 0_i32), (-1, 0), (0, 1), (0, -1)];
        for &(val, i, j) in &cells {
            let cur_idx = i * n + j;
            let cur_dp = dp[cur_idx];
            for &(dx, dy) in &dirs {
                let ni = i as i32 + dx;
                let nj = j as i32 + dy;
                if ni >= 0 && ni < m as i32 && nj >= 0 && nj < n as i32 {
                    let ui = ni as usize;
                    let uj = nj as usize;
                    if grid[ui][uj] > val {
                        let nidx = ui * n + uj;
                        dp[nidx] += cur_dp;
                        if dp[nidx] >= MOD {
                            dp[nidx] -= MOD;
                        }
                    }
                }
            }
        }
        let mut ans: i64 = 0;
        for v in dp {
            ans += v;
            if ans >= MOD {
                ans -= MOD;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-paths grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (list->vector (map list->vector grid)))
         (m (vector-length rows))
         (n (if (> m 0) (vector-length (vector-ref rows 0)) 0))
         ;; dp matrix initialized to 0
         (dp (let ((v (make-vector m)))
               (for ([i (in-range m)])
                 (vector-set! v i (make-vector n 0)))
               v))
         ;; collect cells as (value i j)
         (cells (for*/list ([i (in-range m)]
                            [j (in-range n)])
                  (list (vector-ref (vector-ref rows i) j) i j)))
         ;; sort descending by value
         (sorted-cells (sort cells (lambda (a b) (> (first a) (first b))))))
    (let ((ans 0))
      (for ([cell sorted-cells])
        (define val (first cell))
        (define i (second cell))
        (define j (third cell))
        (define dpij 1)
        (for ([dir '((1 0) (-1 0) (0 1) (0 -1))])
          (define ni (+ i (first dir)))
          (define nj (+ j (second dir)))
          (when (and (>= ni 0) (< ni m) (>= nj 0) (< nj n))
            (define neighbor-val (vector-ref (vector-ref rows ni) nj))
            (when (> neighbor-val val)
              (set! dpij (modulo (+ dpij (vector-ref (vector-ref dp ni) nj)) MOD)))))
        (vector-set! (vector-ref dp i) j dpij)
        (set! ans (modulo (+ ans dpij) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_paths/1]).

-define(MOD, 1000000007).

count_paths(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    {Cells, ValMap} = build_cells(Grid, M, N),

    Sorted = lists:sort(fun({V1,_},{V2,_}) -> V1 > V2 end, Cells),

    {_, Total} = lists:foldl(
        fun({Val, Idx}, {DPMap, Acc}) ->
            I = Idx div N,
            J = Idx rem N,
            Sum = neighbor_sum(I, J, Val, DPMap, ValMap, M, N),
            Dp = (1 + Sum) rem ?MOD,
            NewDPMap = maps:put(Idx, Dp, DPMap),
            {NewDPMap, (Acc + Dp) rem ?MOD}
        end,
        {#{}, 0},
        Sorted),

    Total.

%% Build list of cells {Value, Index} and map Index -> Value
build_cells(Grid, M, N) ->
    build_rows(Grid, 0, N, [], #{}).

build_rows([], _RowIdx, _N, CellsAcc, ValMapAcc) ->
    {CellsAcc, ValMapAcc};
build_rows([Row|RestRows], RowIdx, N, CellsAcc, ValMapAcc) ->
    {NewCellsAcc, NewValMap} = build_cols(Row, RowIdx, 0, N, CellsAcc, ValMapAcc),
    build_rows(RestRows, RowIdx + 1, N, NewCellsAcc, NewValMap).

build_cols(_Row, _RowIdx, ColIdx, N, CellsAcc, ValMapAcc) when ColIdx >= N ->
    {CellsAcc, ValMapAcc};
build_cols(Row, RowIdx, ColIdx, N, CellsAcc, ValMapAcc) ->
    Val = lists:nth(ColIdx + 1, Row),
    Idx = RowIdx * N + ColIdx,
    NewCellsAcc = [{Val, Idx} | CellsAcc],
    NewValMap = maps:put(Idx, Val, ValMapAcc),
    build_cols(Row, RowIdx, ColIdx + 1, N, NewCellsAcc, NewValMap).

%% Sum dp values of already processed neighbors with larger value
neighbor_sum(I, J, Val, DPMap, ValMap, M, N) ->
    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
    lists:foldl(
        fun({Di,Dj}, Acc) ->
            Ni = I + Di,
            Nj = J + Dj,
            if
                Ni >= 0, Ni < M, Nj >= 0, Nj < N ->
                    NIdx = Ni * N + Nj,
                    case maps:get(NIdx, ValMap) of
                        NVal when NVal > Val ->
                            DpN = maps:get(NIdx, DPMap),
                            (Acc + DpN) rem ?MOD;
                        _ -> Acc
                    end;
                true -> Acc
            end
        end,
        0,
        Directions).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_paths(grid :: [[integer]]) :: integer
  def count_paths(grid) do
    m = length(grid)
    n = length(hd(grid))
    size = m * n

    grid_t =
      grid
      |> Enum.map(&List.to_tuple/1)
      |> List.to_tuple()

    cells =
      for {row, i} <- Enum.with_index(grid),
          {val, j} <- Enum.with_index(row),
          do: {val, i, j}

    sorted_cells = Enum.sort_by(cells, fn {v, _, _} -> v end)

    dp0 =
      0..(size - 1)
      |> Enum.reduce(%{}, fn idx, acc -> Map.put(acc, idx, 1) end)

    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    dp =
      Enum.reduce(sorted_cells, dp0, fn {val, i, j}, acc ->
        idx = i * n + j
        cur = Map.get(acc, idx)

        Enum.reduce(dirs, acc, fn {dx, dy}, a ->
          ni = i + dx
          nj = j + dy

          if ni >= 0 and ni < m and nj >= 0 and nj < n do
            neighbor_val = elem(elem(grid_t, ni), nj)

            if neighbor_val > val do
              n_idx = ni * n + nj
              prev = Map.get(a, n_idx)
              new = (prev + cur) |> rem(@mod)
              Map.put(a, n_idx, new)
            else
              a
            end
          else
            a
          end
        end)
      end)

    Enum.reduce(dp, 0, fn {_k, v}, sum -> (sum + v) |> rem(@mod) end)
  end
end
```

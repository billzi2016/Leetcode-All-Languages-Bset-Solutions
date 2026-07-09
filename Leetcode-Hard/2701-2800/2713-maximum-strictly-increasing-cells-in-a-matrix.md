# 2713. Maximum Strictly Increasing Cells in a Matrix

## Cpp

```cpp
class Solution {
public:
    int maxIncreasingCells(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        struct Cell {int val, r, c;};
        vector<Cell> cells;
        cells.reserve(m * n);
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                cells.push_back({mat[i][j], i, j});
        sort(cells.begin(), cells.end(), [](const Cell& a, const Cell& b){
            return a.val < b.val;
        });
        
        vector<int> rowBest(m, 0), colBest(n, 0);
        int ans = 0;
        int idx = 0;
        while (idx < (int)cells.size()) {
            int curVal = cells[idx].val;
            int start = idx;
            // compute dp for this group
            vector<int> dps;
            dps.reserve(64);
            while (idx < (int)cells.size() && cells[idx].val == curVal) {
                const Cell& cell = cells[idx];
                int bestPrev = max(rowBest[cell.r], colBest[cell.c]);
                dps.push_back(bestPrev + 1);
                ans = max(ans, bestPrev + 1);
                ++idx;
            }
            // update rowBest and colBest with results of this group
            for (int k = start; k < idx; ++k) {
                const Cell& cell = cells[k];
                int dp = dps[k - start];
                if (dp > rowBest[cell.r]) rowBest[cell.r] = dp;
                if (dp > colBest[cell.c]) colBest[cell.c] = dp;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Cell {
        int val;
        int r;
        int c;
        Cell(int v, int i, int j) {
            this.val = v;
            this.r = i;
            this.c = j;
        }
    }

    public int maxIncreasingCells(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int total = m * n;
        Cell[] cells = new Cell[total];
        int idx = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cells[idx++] = new Cell(mat[i][j], i, j);
            }
        }

        java.util.Arrays.sort(cells, (a, b) -> Integer.compare(a.val, b.val));

        int[] rowBest = new int[m];
        int[] colBest = new int[n];
        int answer = 0;

        for (int i = 0; i < total; ) {
            int j = i;
            while (j < total && cells[j].val == cells[i].val) {
                ++j;
            }
            // compute dp for group [i, j)
            int[] curVals = new int[j - i];
            for (int k = i; k < j; ++k) {
                Cell cell = cells[k];
                int bestPrev = Math.max(rowBest[cell.r], colBest[cell.c]);
                int cur = bestPrev + 1;
                curVals[k - i] = cur;
                if (cur > answer) answer = cur;
            }
            // update rowBest and colBest with group results
            for (int k = i; k < j; ++k) {
                Cell cell = cells[k];
                int cur = curVals[k - i];
                if (cur > rowBest[cell.r]) rowBest[cell.r] = cur;
                if (cur > colBest[cell.c]) colBest[cell.c] = cur;
            }
            i = j;
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maxIncreasingCells(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        cells = []
        for i in range(m):
            row = mat[i]
            for j in range(n):
                cells.append((row[j], i, j))
        cells.sort(key=lambda x: x[0])

        row_best = [0] * m
        col_best = [0] * n
        ans = 0
        idx = 0
        total = len(cells)

        while idx < total:
            cur_val = cells[idx][0]
            batch = []
            # compute dp for all cells with the same value using previous bests only
            while idx < total and cells[idx][0] == cur_val:
                _, r, c = cells[idx]
                dp = max(row_best[r], col_best[c]) + 1
                batch.append((r, c, dp))
                if dp > ans:
                    ans = dp
                idx += 1
            # update row and column bests after the whole batch is processed
            for r, c, dp in batch:
                if dp > row_best[r]:
                    row_best[r] = dp
                if dp > col_best[c]:
                    col_best[c] = dp

        return ans
```

## Python3

```python
class Solution:
    def maxIncreasingCells(self, mat):
        from itertools import groupby

        m = len(mat)
        n = len(mat[0])
        cells = []
        for i in range(m):
            row = mat[i]
            for j in range(n):
                cells.append((row[j], i, j))
        cells.sort(key=lambda x: x[0])

        row_best = [0] * m
        col_best = [0] * n
        ans = 0

        idx = 0
        total = len(cells)
        while idx < total:
            val = cells[idx][0]
            group = []
            while idx < total and cells[idx][0] == val:
                _, i, j = cells[idx]
                dp = max(row_best[i], col_best[j]) + 1
                group.append((i, j, dp))
                ans = max(ans, dp)
                idx += 1
            for i, j, dp in group:
                if dp > row_best[i]:
                    row_best[i] = dp
                if dp > col_best[j]:
                    col_best[j] = dp

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int val;
    int r;
    int c;
} Cell;

static int cellCmp(const void *a, const void *b) {
    const Cell *ca = (const Cell *)a;
    const Cell *cb = (const Cell *)b;
    if (ca->val < cb->val) return -1;
    if (ca->val > cb->val) return 1;
    return 0;
}

int maxIncreasingCells(int** mat, int matSize, int* matColSize) {
    int m = matSize;
    int n = matColSize[0];
    int total = m * n;

    Cell *cells = (Cell *)malloc(sizeof(Cell) * total);
    int idx = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cells[idx].val = mat[i][j];
            cells[idx].r = i;
            cells[idx].c = j;
            ++idx;
        }
    }

    qsort(cells, total, sizeof(Cell), cellCmp);

    int *rowBest = (int *)calloc(m, sizeof(int));
    int *colBest = (int *)calloc(n, sizeof(int));
    int *dp = (int *)malloc(sizeof(int) * total);

    int answer = 0;
    int i = 0;
    while (i < total) {
        int start = i;
        while (i < total && cells[i].val == cells[start].val) ++i; // group [start, i)

        for (int k = start; k < i; ++k) {
            int r = cells[k].r;
            int c = cells[k].c;
            int bestPrev = rowBest[r] > colBest[c] ? rowBest[r] : colBest[c];
            dp[k] = bestPrev + 1;
            if (dp[k] > answer) answer = dp[k];
        }

        for (int k = start; k < i; ++k) {
            int r = cells[k].r;
            int c = cells[k].c;
            if (dp[k] > rowBest[r]) rowBest[r] = dp[k];
            if (dp[k] > colBest[c]) colBest[c] = dp[k];
        }
    }

    free(cells);
    free(rowBest);
    free(colBest);
    free(dp);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private struct Cell {
        public int val;
        public int r;
        public int c;
        public Cell(int v, int row, int col) {
            val = v; r = row; c = col;
        }
    }

    public int MaxIncreasingCells(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;
        int total = m * n;
        var cells = new List<Cell>(total);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cells.Add(new Cell(mat[i][j], i, j));
            }
        }

        cells.Sort((a, b) => a.val.CompareTo(b.val));

        int[] rowBest = new int[m];
        int[] colBest = new int[n];
        int answer = 0;

        int idx = 0;
        while (idx < total) {
            int start = idx;
            int curVal = cells[idx].val;
            // find group end
            while (idx < total && cells[idx].val == curVal) idx++;
            int groupSize = idx - start;
            int[] dpGroup = new int[groupSize];

            // compute dp for each cell in the group using previous smaller values only
            for (int k = 0; k < groupSize; k++) {
                var cell = cells[start + k];
                int bestPrev = Math.Max(rowBest[cell.r], colBest[cell.c]);
                int curDp = bestPrev + 1;
                dpGroup[k] = curDp;
                if (curDp > answer) answer = curDp;
            }

            // update rowBest and colBest with results from this group
            for (int k = 0; k < groupSize; k++) {
                var cell = cells[start + k];
                int curDp = dpGroup[k];
                if (curDp > rowBest[cell.r]) rowBest[cell.r] = curDp;
                if (curDp > colBest[cell.c]) colBest[cell.c] = curDp;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var maxIncreasingCells = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const cells = [];
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            cells.push([mat[i][j], i, j]);
        }
    }
    cells.sort((a, b) => a[0] - b[0]);

    const rowBest = new Array(m).fill(0);
    const colBest = new Array(n).fill(0);
    let ans = 1;
    let idx = 0;

    while (idx < cells.length) {
        const curVal = cells[idx][0];
        const batch = [];
        // process all cells with the same value
        while (idx < cells.length && cells[idx][0] === curVal) {
            const [, i, j] = cells[idx];
            const dp = Math.max(rowBest[i], colBest[j]) + 1;
            batch.push([i, j, dp]);
            if (dp > ans) ans = dp;
            ++idx;
        }
        // update row and column bests after the whole group
        for (const [i, j, dp] of batch) {
            if (dp > rowBest[i]) rowBest[i] = dp;
            if (dp > colBest[j]) colBest[j] = dp;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxIncreasingCells(mat: number[][]): number {
    const m = mat.length;
    const n = mat[0].length;
    const cells: { val: number; r: number; c: number }[] = [];
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            cells.push({ val: mat[i][j], r: i, c: j });
        }
    }
    cells.sort((a, b) => a.val - b.val);
    const rowBest = new Int32Array(m); // longest path ending in each row with smaller values
    const colBest = new Int32Array(n); // same for columns
    let ans = 0;
    let idx = 0;
    while (idx < cells.length) {
        let nxt = idx;
        while (nxt < cells.length && cells[nxt].val === cells[idx].val) ++nxt;
        const dp: number[] = new Array(nxt - idx);
        for (let k = idx; k < nxt; ++k) {
            const { r, c } = cells[k];
            const bestPrev = Math.max(rowBest[r], colBest[c]);
            dp[k - idx] = bestPrev + 1;
            if (dp[k - idx] > ans) ans = dp[k - idx];
        }
        for (let k = idx; k < nxt; ++k) {
            const { r, c } = cells[k];
            const cur = dp[k - idx];
            if (cur > rowBest[r]) rowBest[r] = cur;
            if (cur > colBest[c]) colBest[c] = cur;
        }
        idx = nxt;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function maxIncreasingCells($mat) {
        $m = count($mat);
        if ($m == 0) return 0;
        $n = count($mat[0]);
        $cells = [];
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $cells[] = [$mat[$i][$j], $i, $j];
            }
        }

        usort($cells, function($a, $b) {
            if ($a[0] == $b[0]) return 0;
            return ($a[0] < $b[0]) ? -1 : 1;
        });

        $rowBest = array_fill(0, $m, 0);
        $colBest = array_fill(0, $n, 0);
        $res = 0;
        $idx = 0;
        $total = count($cells);

        while ($idx < $total) {
            $val = $cells[$idx][0];
            $temp = [];

            // process all cells with the same value
            while ($idx < $total && $cells[$idx][0] == $val) {
                [$v, $r, $c] = $cells[$idx];
                $dp = max($rowBest[$r], $colBest[$c]) + 1;
                $temp[] = [$r, $c, $dp];
                if ($dp > $res) $res = $dp;
                ++$idx;
            }

            // update row and column bests after the group
            foreach ($temp as $info) {
                [$r, $c, $dp] = $info;
                if ($dp > $rowBest[$r]) $rowBest[$r] = $dp;
                if ($dp > $colBest[$c]) $colBest[$c] = $dp;
            }
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func maxIncreasingCells(_ mat: [[Int]]) -> Int {
        let m = mat.count
        guard m > 0 else { return 0 }
        let n = mat[0].count
        struct Cell {
            let val: Int
            let r: Int
            let c: Int
        }
        var cells = [Cell]()
        cells.reserveCapacity(m * n)
        for i in 0..<m {
            for j in 0..<n {
                cells.append(Cell(val: mat[i][j], r: i, c: j))
            }
        }
        cells.sort { $0.val < $1.val }
        
        var rowBest = [Int](repeating: 0, count: m)
        var colBest = [Int](repeating: 0, count: n)
        var idx = 0
        let total = cells.count
        var answer = 0
        
        while idx < total {
            let curVal = cells[idx].val
            var group = [(r: Int, c: Int, dp: Int)]()
            while idx < total && cells[idx].val == curVal {
                let r = cells[idx].r
                let c = cells[idx].c
                let dp = max(rowBest[r], colBest[c]) + 1
                group.append((r, c, dp))
                if dp > answer { answer = dp }
                idx += 1
            }
            for item in group {
                if item.dp > rowBest[item.r] { rowBest[item.r] = item.dp }
                if item.dp > colBest[item.c] { colBest[item.c] = item.dp }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxIncreasingCells(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        data class Cell(val value: Int, val r: Int, val c: Int)
        val cells = ArrayList<Cell>(m * n)
        for (i in 0 until m) {
            for (j in 0 until n) {
                cells.add(Cell(mat[i][j], i, j))
            }
        }
        cells.sortWith(compareBy { it.value })
        val rowBest = IntArray(m)
        val colBest = IntArray(n)
        val dp = IntArray(cells.size)
        var ans = 1
        var idx = 0
        while (idx < cells.size) {
            var j = idx
            val curVal = cells[idx].value
            while (j < cells.size && cells[j].value == curVal) j++
            // compute dp for batch [idx, j)
            for (k in idx until j) {
                val cell = cells[k]
                dp[k] = maxOf(rowBest[cell.r], colBest[cell.c]) + 1
                if (dp[k] > ans) ans = dp[k]
            }
            // update rowBest and colBest with batch results
            for (k in idx until j) {
                val cell = cells[k]
                if (dp[k] > rowBest[cell.r]) rowBest[cell.r] = dp[k]
                if (dp[k] > colBest[cell.c]) colBest[cell.c] = dp[k]
            }
            idx = j
        }
        return ans
    }
}
```

## Dart

```dart
class Cell {
  int val;
  int r;
  int c;
  Cell(this.val, this.r, this.c);
}

class Solution {
  int maxIncreasingCells(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    List<Cell> cells = [];
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        cells.add(Cell(mat[i][j], i, j));
      }
    }
    cells.sort((a, b) => a.val.compareTo(b.val));

    List<int> rowBest = List.filled(m, 0);
    List<int> colBest = List.filled(n, 0);
    int ans = 0;
    int idx = 0;
    while (idx < cells.length) {
      int start = idx;
      int curVal = cells[idx].val;
      while (idx < cells.length && cells[idx].val == curVal) {
        idx++;
      }
      // compute dp for this group
      List<int> dpGroup = List.filled(idx - start, 0);
      for (int k = start; k < idx; ++k) {
        Cell cell = cells[k];
        int bestPrev = rowBest[cell.r] > colBest[cell.c]
            ? rowBest[cell.r]
            : colBest[cell.c];
        int cur = bestPrev + 1;
        dpGroup[k - start] = cur;
        if (cur > ans) ans = cur;
      }
      // update row and column bests
      for (int k = start; k < idx; ++k) {
        Cell cell = cells[k];
        int cur = dpGroup[k - start];
        if (cur > rowBest[cell.r]) rowBest[cell.r] = cur;
        if (cur > colBest[cell.c]) colBest[cell.c] = cur;
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func maxIncreasingCells(mat [][]int) int {
	m := len(mat)
	n := len(mat[0])
	type Cell struct{ val, r, c int }
	cells := make([]Cell, 0, m*n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			cells = append(cells, Cell{mat[i][j], i, j})
		}
	}
	sort.Slice(cells, func(i, j int) bool { return cells[i].val < cells[j].val })
	rowBest := make([]int, m)
	colBest := make([]int, n)
	dp := make([]int, len(cells))
	ans := 0
	for i := 0; i < len(cells); {
		j := i
		for j < len(cells) && cells[j].val == cells[i].val {
			r, c := cells[j].r, cells[j].c
			best := rowBest[r]
			if colBest[c] > best {
				best = colBest[c]
			}
			dp[j] = best + 1
			if dp[j] > ans {
				ans = dp[j]
			}
			j++
		}
		for k := i; k < j; k++ {
			r, c := cells[k].r, cells[k].c
			if dp[k] > rowBest[r] {
				rowBest[r] = dp[k]
			}
			if dp[k] > colBest[c] {
				colBest[c] = dp[k]
			}
		}
		i = j
	}
	return ans
}
```

## Ruby

```ruby
def max_increasing_cells(mat)
  m = mat.length
  n = mat[0].length
  cells = []
  mat.each_with_index do |row, i|
    row.each_with_index do |val, j|
      cells << [val, i, j]
    end
  end
  cells.sort_by! { |c| c[0] }
  row_best = Array.new(m, 0)
  col_best = Array.new(n, 0)
  ans = 1
  idx = 0
  while idx < cells.size
    v = cells[idx][0]
    start_idx = idx
    idx += 1 while idx < cells.size && cells[idx][0] == v
    temp = []
    (start_idx...idx).each do |k|
      _, i, j = cells[k]
      best = row_best[i] > col_best[j] ? row_best[i] : col_best[j]
      dp = best + 1
      temp << [i, j, dp]
      ans = dp if dp > ans
    end
    temp.each do |i, j, dp|
      row_best[i] = dp if dp > row_best[i]
      col_best[j] = dp if dp > col_best[j]
    end
  end
  ans
end
```

## Scala

```scala
import scala.util.Sorting

object Solution {
  def maxIncreasingCells(mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    val total = m * n
    val cells = new Array[(Int, Int, Int)](total)
    var idx = 0
    var i = 0
    while (i < m) {
      val row = mat(i)
      var j = 0
      while (j < n) {
        cells(idx) = (row(j), i, j)
        idx += 1
        j += 1
      }
      i += 1
    }

    Sorting.stableSort(cells)(Ordering.by[(Int, Int, Int), Int](_._1))

    val rowBest = new Array[Int](m)
    val colBest = new Array[Int](n)
    var ans = 0

    var pos = 0
    while (pos < total) {
      var next = pos
      // find range with same value
      while (next < total && cells(next)._1 == cells(pos)._1) {
        next += 1
      }
      val sz = next - pos
      val rs = new Array[Int](sz)
      val cs = new Array[Int](sz)
      val dps = new Array[Int](sz)

      var k = 0
      while (k < sz) {
        val (_, r, c) = cells(pos + k)
        val dp = math.max(rowBest(r), colBest(c)) + 1
        rs(k) = r
        cs(k) = c
        dps(k) = dp
        if (dp > ans) ans = dp
        k += 1
      }

      var t = 0
      while (t < sz) {
        val r = rs(t)
        val c = cs(t)
        val dp = dps(t)
        if (dp > rowBest(r)) rowBest(r) = dp
        if (dp > colBest(c)) colBest(c) = dp
        t += 1
      }

      pos = next
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_increasing_cells(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut cells: Vec<(i32, usize, usize)> = Vec::with_capacity(m * n);
        for (i, row) in mat.iter().enumerate() {
            for (j, &val) in row.iter().enumerate() {
                cells.push((val, i, j));
            }
        }
        cells.sort_unstable_by_key(|k| k.0);

        let mut row_best = vec![0i32; m];
        let mut col_best = vec![0i32; n];
        let mut ans = 1i32;
        let mut idx = 0usize;
        while idx < cells.len() {
            let cur_val = cells[idx].0;
            let mut temp: Vec<(usize, usize, i32)> = Vec::new();
            // compute dp for all cells with the same value
            while idx < cells.len() && cells[idx].0 == cur_val {
                let (_, r, c) = cells[idx];
                let best_prev = std::cmp::max(row_best[r], col_best[c]);
                let dp = best_prev + 1;
                ans = ans.max(dp);
                temp.push((r, c, dp));
                idx += 1;
            }
            // update row and column bests after the group
            for (r, c, dp) in temp {
                if dp > row_best[r] {
                    row_best[r] = dp;
                }
                if dp > col_best[c] {
                    col_best[c] = dp;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(struct cell (i j v) #:transparent)

(define/contract (max-increasing-cells mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length mat))
         (n (if (= m 0) 0 (length (car mat))))
         (cells (for*/list ([i (in-range m)]
                            [j (in-range n)])
                  (cell i j (list-ref (list-ref mat i) j))))
         (sorted-cells (sort cells < #:key cell-v))
         (rowBest (make-vector m 0))
         (colBest (make-vector n 0)))
    (define ans 0)
    (define prev-val #f)
    (define updates '())
    (for ([c sorted-cells])
      (let ((val (cell-v c))
            (i (cell-i c))
            (j (cell-j c)))
        (when (and (not (eq? prev-val #f)) (not (= val prev-val)))
          (for ([u updates])
            (define ui (list-ref u 0))
            (define uj (list-ref u 1))
            (define cur (list-ref u 2))
            (vector-set! rowBest ui (max (vector-ref rowBest ui) cur))
            (vector-set! colBest uj (max (vector-ref colBest uj) cur)))
          (set! updates '()))
        (let* ((best (max (vector-ref rowBest i) (vector-ref colBest j)))
               (cur (+ 1 best)))
          (when (> cur ans) (set! ans cur))
          (set! updates (cons (list i j cur) updates))
          (set! prev-val val))))
    (for ([u updates])
      (define ui (list-ref u 0))
      (define uj (list-ref u 1))
      (define cur (list-ref u 2))
      (vector-set! rowBest ui (max (vector-ref rowBest ui) cur))
      (vector-set! colBest uj (max (vector-ref colBest uj) cur)))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([max_increasing_cells/1]).
-spec max_increasing_cells(Mat :: [[integer()]]) -> integer().
max_increasing_cells(Mat) ->
    Cells = flatten_mat(Mat, 0, []),
    Sorted = lists:keysort(1, Cells), % sort by value
    process(Sorted, #{}, #{}, 0).

flatten_mat([], _RowIdx, Acc) -> Acc;
flatten_mat([Row|RestRows], RowIdx, Acc) ->
    NewAcc = flatten_row(Row, RowIdx, 0, Acc),
    flatten_mat(RestRows, RowIdx + 1, NewAcc).

flatten_row([], _RowIdx, _ColIdx, Acc) -> Acc;
flatten_row([Val|RestVals], RowIdx, ColIdx, Acc) ->
    flatten_row(RestVals, RowIdx, ColIdx + 1,
                [{Val, RowIdx, ColIdx} | Acc]).

process([], _RowBest, _ColBest, MaxAns) -> MaxAns;
process(Sorted, RowBest, ColBest, MaxAns) ->
    {Group, Rest} = take_same_value(Sorted),
    {DPs, NewMax} = compute_group(Group, RowBest, ColBest, MaxAns),
    UpdatedRowBest = update_row_best(DPs, RowBest),
    UpdatedColBest = update_col_best(DPs, ColBest),
    process(Rest, UpdatedRowBest, UpdatedColBest, NewMax).

take_same_value([]) -> {[], []};
take_same_value([{Val,_R,_C}=H|T]) ->
    {SameRev, Rest} = take_same_val(T, Val, [H]),
    {lists:reverse(SameRev), Rest}.

take_same_val([], _Val, Acc) -> {Acc, []};
take_same_val([{V,R,C}=E|Rest], V, Acc) ->
    take_same_val(Rest, V, [E|Acc]);
take_same_val(List, _V, Acc) -> {Acc, List}.

compute_group(Group, RowBest, ColBest, MaxAns) ->
    compute_group(Group, RowBest, ColBest, [], MaxAns).

compute_group([], _RowBest, _ColBest, AccDPs, CurMax) ->
    {AccDPs, CurMax};
compute_group([{_Val,R,C}|Rest], RowBest, ColBest, AccDPs, CurMax) ->
    RB = maps:get(R, RowBest, 0),
    CB = maps:get(C, ColBest, 0),
    DP = 1 + max(RB, CB),
    NewMax = if DP > CurMax -> DP; true -> CurMax end,
    compute_group(Rest, RowBest, ColBest, [{R,C,DP}|AccDPs], NewMax).

update_row_best(DPs, RowBest) ->
    lists:foldl(fun({R,_C,DP}, RB) ->
        Prev = maps:get(R, RB, 0),
        if DP > Prev -> maps:put(R, DP, RB); true -> RB end
    end, RowBest, DPs).

update_col_best(DPs, ColBest) ->
    lists:foldl(fun({_R,C,DP}, CB) ->
        Prev = maps:get(C, CB, 0),
        if DP > Prev -> maps:put(C, DP, CB); true -> CB end
    end, ColBest, DPs).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_increasing_cells(mat :: [[integer]]) :: integer
  def max_increasing_cells(mat) do
    m = length(mat)
    n = mat |> hd() |> length()

    # Flatten cells with their coordinates
    cells =
      for {row, i} <- Enum.with_index(mat),
          {val, j} <- Enum.with_index(row),
          do: {val, i, j}

    # Sort cells by value ascending
    sorted_cells = Enum.sort_by(cells, fn {v, _, _} -> v end)

    # Group cells with the same value
    groups = Enum.chunk_by(sorted_cells, fn {v, _, _} -> v end)

    # Initialize row and column best arrays
    row_best = :array.new(m, default: 0)
    col_best = :array.new(n, default: 0)

    {_final_row, _final_col, answer} =
      Enum.reduce(groups, {row_best, col_best, 0}, fn group,
                                                      {rb_acc, cb_acc, best_acc} ->
        # Compute dp for each cell in the current group using previous bests
        dps =
          Enum.map(group, fn {_v, r, c} ->
            max(:array.get(r, rb_acc), :array.get(c, cb_acc)) + 1
          end)

        # Update row/col bests and global answer
        {new_rb, new_cb, new_best} =
          Enum.zip(group, dps)
          |> Enum.reduce({rb_acc, cb_acc, best_acc}, fn {{_v, r, c}, dp},
                                                      {rb_cur, cb_cur, best_cur} ->
            best_cur = if dp > best_cur, do: dp, else: best_cur

            rb_cur =
              case :array.get(r, rb_cur) do
                cur when dp > cur -> :array.set(r, dp, rb_cur)
                _ -> rb_cur
              end

            cb_cur =
              case :array.get(c, cb_cur) do
                cur when dp > cur -> :array.set(c, dp, cb_cur)
                _ -> cb_cur
              end

            {rb_cur, cb_cur, best_cur}
          end)

        {new_rb, new_cb, new_best}
      end)

    answer
  end
end
```

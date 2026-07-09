# 3567. Minimum Absolute Difference in Sliding Submatrix

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int rows = m - k + 1;
        int cols = n - k + 1;
        vector<vector<int>> ans(rows, vector<int>(cols, 0));
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                vector<int> vals;
                vals.reserve(k * k);
                for (int x = i; x < i + k; ++x) {
                    for (int y = j; y < j + k; ++y) {
                        vals.push_back(grid[x][y]);
                    }
                }
                if (vals.size() <= 1) {
                    ans[i][j] = 0;
                    continue;
                }
                sort(vals.begin(), vals.end());
                int best = INT_MAX;
                for (size_t p = 1; p < vals.size(); ++p) {
                    int diff = vals[p] - vals[p - 1];
                    if (diff < best) best = diff;
                    if (best == 0) break;
                }
                ans[i][j] = best;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[][] minAbsDiff(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int rows = m - k + 1;
        int cols = n - k + 1;
        int[][] ans = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int size = k * k;
                if (size <= 1) {
                    ans[i][j] = 0;
                    continue;
                }
                int[] vals = new int[size];
                int idx = 0;
                for (int r = i; r < i + k; r++) {
                    for (int c = j; c < j + k; c++) {
                        vals[idx++] = grid[r][c];
                    }
                }
                java.util.Arrays.sort(vals);
                int minDiff = Integer.MAX_VALUE;
                for (int p = 1; p < size; p++) {
                    int diff = vals[p] - vals[p - 1];
                    if (diff < minDiff) {
                        minDiff = diff;
                        if (minDiff == 0) break;
                    }
                }
                ans[i][j] = minDiff;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        rows = m - k + 1
        cols = n - k + 1
        ans = [[0] * cols for _ in range(rows)]
        if k == 1:
            return ans
        for i in range(rows):
            for j in range(cols):
                vals = []
                for x in range(i, i + k):
                    vals.extend(grid[x][j:j + k])
                vals.sort()
                min_diff = vals[1] - vals[0]
                if min_diff == 0:
                    ans[i][j] = 0
                    continue
                for idx in range(2, len(vals)):
                    diff = vals[idx] - vals[idx - 1]
                    if diff < min_diff:
                        min_diff = diff
                        if min_diff == 0:
                            break
                ans[i][j] = min_diff
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = m - k + 1, n - k + 1
        ans = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                vals = []
                for r in range(i, i + k):
                    vals.extend(grid[r][j:j + k])
                if len(vals) <= 1:
                    ans[i][j] = 0
                    continue
                vals.sort()
                min_diff = float('inf')
                for p in range(1, len(vals)):
                    diff = vals[p] - vals[p - 1]
                    if diff < min_diff:
                        min_diff = diff
                        if min_diff == 0:
                            break
                ans[i][j] = int(min_diff) if min_diff != float('inf') else 0
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** minAbsDiff(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int*** returnColumnSizes) {
    int rows = gridSize;
    int cols = gridColSize[0];
    int outRows = rows - k + 1;
    int outCols = cols - k + 1;

    int **ans = (int **)malloc(outRows * sizeof(int *));
    for (int i = 0; i < outRows; ++i) {
        ans[i] = (int *)malloc(outCols * sizeof(int));
    }

    *returnSize = outRows;
    *returnColumnSizes = (int **)malloc(outRows * sizeof(int *));
    for (int i = 0; i < outRows; ++i) {
        (*returnColumnSizes)[i] = (int *)malloc(sizeof(int));
        (*returnColumnSizes)[i][0] = outCols;
    }

    int maxVals = k * k;
    int *vals = (int *)malloc(maxVals * sizeof(int));

    for (int i = 0; i < outRows; ++i) {
        for (int j = 0; j < outCols; ++j) {
            int cnt = 0;
            for (int r = i; r < i + k; ++r) {
                for (int c = j; c < j + k; ++c) {
                    vals[cnt++] = grid[r][c];
                }
            }

            if (cnt < 2) {
                ans[i][j] = 0;
                continue;
            }

            qsort(vals, cnt, sizeof(int), cmp_int);

            int minDiff = INT_MAX;
            for (int p = 1; p < cnt; ++p) {
                int diff = vals[p] - vals[p - 1];
                if (diff < 0) diff = -diff;
                if (diff < minDiff) {
                    minDiff = diff;
                    if (minDiff == 0) break;
                }
            }
            ans[i][j] = minDiff;
        }
    }

    free(vals);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] MinAbsDiff(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int rows = m - k + 1;
        int cols = n - k + 1;
        int[][] ans = new int[rows][];
        for (int i = 0; i < rows; i++) {
            ans[i] = new int[cols];
            for (int j = 0; j < cols; j++) {
                if (k == 1) {
                    ans[i][j] = 0;
                    continue;
                }
                List<int> vals = new List<int>(k * k);
                for (int a = i; a < i + k; a++) {
                    for (int b = j; b < j + k; b++) {
                        vals.Add(grid[a][b]);
                    }
                }
                vals.Sort();
                int minDiff = int.MaxValue;
                for (int idx = 1; idx < vals.Count; idx++) {
                    int diff = Math.Abs(vals[idx] - vals[idx - 1]);
                    if (diff < minDiff) {
                        minDiff = diff;
                        if (minDiff == 0) break;
                    }
                }
                ans[i][j] = minDiff == int.MaxValue ? 0 : minDiff;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var minAbsDiff = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const outRows = m - k + 1;
    const outCols = n - k + 1;
    const ans = new Array(outRows);
    for (let i = 0; i < outRows; ++i) {
        ans[i] = new Array(outCols);
        for (let j = 0; j < outCols; ++j) {
            const vals = [];
            for (let r = i; r < i + k; ++r) {
                for (let c = j; c < j + k; ++c) {
                    vals.push(grid[r][c]);
                }
            }
            if (vals.length <= 1) {
                ans[i][j] = 0;
                continue;
            }
            vals.sort((a, b) => a - b);
            let minDiff = Infinity;
            for (let t = 1; t < vals.length; ++t) {
                const diff = vals[t] - vals[t - 1];
                if (diff < minDiff) {
                    minDiff = diff;
                    if (minDiff === 0) break;
                }
            }
            ans[i][j] = minDiff;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minAbsDiff(grid: number[][], k: number): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const rows = m - k + 1;
    const cols = n - k + 1;
    const ans: number[][] = Array.from({ length: rows }, () => new Array(cols).fill(0));

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (k === 1) {
                ans[i][j] = 0;
                continue;
            }
            const vals: number[] = [];
            for (let di = 0; di < k; di++) {
                for (let dj = 0; dj < k; dj++) {
                    vals.push(grid[i + di][j + dj]);
                }
            }
            vals.sort((a, b) => a - b);
            let minDiff = Infinity;
            for (let p = 1; p < vals.length; p++) {
                const diff = vals[p] - vals[p - 1];
                if (diff < minDiff) minDiff = diff;
                if (minDiff === 0) break; // can't get smaller
            }
            ans[i][j] = minDiff === Infinity ? 0 : minDiff;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function minAbsDiff($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = [];

        for ($i = 0; $i <= $m - $k; $i++) {
            $rowAns = [];
            for ($j = 0; $j <= $n - $k; $j++) {
                $vals = [];
                for ($p = $i; $p < $i + $k; $p++) {
                    for ($q = $j; $q < $j + $k; $q++) {
                        $vals[] = $grid[$p][$q];
                    }
                }
                sort($vals, SORT_NUMERIC);
                $len = count($vals);

                if ($len < 2) {
                    $rowAns[] = 0;
                    continue;
                }

                $minDiff = PHP_INT_MAX;
                $found = false;
                for ($t = 1; $t < $len; $t++) {
                    if ($vals[$t] == $vals[$t - 1]) {
                        continue; // same value, not distinct
                    }
                    $diff = $vals[$t] - $vals[$t - 1]; // sorted => non‑negative
                    if ($diff < $minDiff) {
                        $minDiff = $diff;
                        $found = true;
                        if ($minDiff == 0) {
                            break;
                        }
                    }
                }

                $rowAns[] = $found ? $minDiff : 0;
            }
            $ans[] = $rowAns;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minAbsDiff(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        let m = grid.count
        let n = grid[0].count
        var result = Array(repeating: Array(repeating: 0, count: n - k + 1), count: m - k + 1)
        for i in 0..<(m - k + 1) {
            for j in 0..<(n - k + 1) {
                var values = [Int]()
                values.reserveCapacity(k * k)
                for r in i..<(i + k) {
                    for c in j..<(j + k) {
                        values.append(grid[r][c])
                    }
                }
                if values.count <= 1 {
                    result[i][j] = 0
                } else {
                    values.sort()
                    var minDiff = Int.max
                    for idx in 1..<values.count {
                        let diff = abs(values[idx] - values[idx - 1])
                        if diff < minDiff {
                            minDiff = diff
                            if minDiff == 0 { break }
                        }
                    }
                    result[i][j] = minDiff
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minAbsDiff(grid: Array<IntArray>, k: Int): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val rows = m - k + 1
        val cols = n - k + 1
        val ans = Array(rows) { IntArray(cols) }
        for (i in 0 until rows) {
            for (j in 0 until cols) {
                val vals = IntArray(k * k)
                var idx = 0
                for (r in i until i + k) {
                    for (c in j until j + k) {
                        vals[idx++] = grid[r][c]
                    }
                }
                java.util.Arrays.sort(vals)
                var minDiff = Int.MAX_VALUE
                for (p in 1 until vals.size) {
                    val diff = kotlin.math.abs(vals[p] - vals[p - 1])
                    if (diff < minDiff) {
                        minDiff = diff
                        if (minDiff == 0) break
                    }
                }
                ans[i][j] = if (minDiff == Int.MAX_VALUE) 0 else minDiff
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> minAbsDiff(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    int rows = m - k + 1;
    int cols = n - k + 1;
    List<List<int>> ans = List.generate(rows, (_) => List.filled(cols, 0));

    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        List<int> vals = [];
        for (int a = i; a < i + k; ++a) {
          for (int b = j; b < j + k; ++b) {
            vals.add(grid[a][b]);
          }
        }
        if (vals.length <= 1) {
          ans[i][j] = 0;
          continue;
        }
        vals.sort();
        int minDiff = (1 << 60);
        for (int idx = 1; idx < vals.length; ++idx) {
          int diff = (vals[idx] - vals[idx - 1]).abs();
          if (diff < minDiff) minDiff = diff;
        }
        ans[i][j] = minDiff;
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

func minAbsDiff(grid [][]int, k int) [][]int {
	m := len(grid)
	n := len(grid[0])
	rows := m - k + 1
	cols := n - k + 1
	ans := make([][]int, rows)
	maxInt := int(^uint(0) >> 1)

	for i := 0; i < rows; i++ {
		ans[i] = make([]int, cols)
		for j := 0; j < cols; j++ {
			vals := make([]int, 0, k*k)
			for r := i; r < i+k; r++ {
				for c := j; c < j+k; c++ {
					vals = append(vals, grid[r][c])
				}
			}
			if len(vals) < 2 {
				ans[i][j] = 0
				continue
			}
			sort.Ints(vals)
			minDiff := maxInt
			for idx := 1; idx < len(vals); idx++ {
				diff := vals[idx] - vals[idx-1]
				if diff < minDiff {
					minDiff = diff
					if minDiff == 0 {
						break
					}
				}
			}
			ans[i][j] = minDiff
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_abs_diff(grid, k)
  m = grid.length
  n = grid[0].length
  rows = m - k + 1
  cols = n - k + 1
  ans = Array.new(rows) { Array.new(cols, 0) }

  (0...rows).each do |i|
    (0...cols).each do |j|
      vals = []
      (i...(i + k)).each do |x|
        (j...(j + k)).each do |y|
          vals << grid[x][y]
        end
      end

      if vals.length <= 1
        ans[i][j] = 0
        next
      end

      vals.sort!
      min_diff = Float::INFINITY
      (1...vals.length).each do |idx|
        diff = (vals[idx] - vals[idx - 1]).abs
        if diff < min_diff
          min_diff = diff
          break if min_diff == 0
        end
      end
      ans[i][j] = min_diff == Float::INFINITY ? 0 : min_diff
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minAbsDiff(grid: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        val m = grid.length
        val n = grid(0).length
        val rows = m - k + 1
        val cols = n - k + 1
        val ans = Array.ofDim[Int](rows, cols)

        for (i <- 0 until rows) {
            for (j <- 0 until cols) {
                var minDiff = Int.MaxValue
                val values = new scala.collection.mutable.ArrayBuffer[Int]()
                var r = i
                while (r < i + k) {
                    var c = j
                    while (c < j + k) {
                        values += grid(r)(c)
                        c += 1
                    }
                    r += 1
                }
                val sorted = values.sorted
                var idx = 1
                while (idx < sorted.length) {
                    val diff = math.abs(sorted(idx) - sorted(idx - 1))
                    if (diff < minDiff) minDiff = diff
                    idx += 1
                }
                ans(i)(j) = if (minDiff == Int.MaxValue) 0 else minDiff
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_abs_diff(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let kk = k as usize;
        if kk == 0 {
            return vec![];
        }
        let rows = m - kk + 1;
        let cols = n - kk + 1;
        let mut ans: Vec<Vec<i32>> = vec![vec![0; cols]; rows];

        for i in 0..=m - kk {
            for j in 0..=n - kk {
                let mut vals: Vec<i32> = Vec::with_capacity(kk * kk);
                for x in i..i + kk {
                    for y in j..j + kk {
                        vals.push(grid[x][y]);
                    }
                }
                if vals.len() <= 1 {
                    ans[i][j] = 0;
                    continue;
                }
                vals.sort_unstable();
                let mut min_diff = i32::MAX;
                for idx in 1..vals.len() {
                    let diff = (vals[idx] - vals[idx - 1]).abs();
                    if diff < min_diff {
                        min_diff = diff;
                        if min_diff == 0 {
                            break;
                        }
                    }
                }
                ans[i][j] = min_diff;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-abs-diff grid k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let* ((m (length grid))
         (n (if (> m 0) (length (first grid)) 0))
         (out-rows (+ (- m k) 1))
         (out-cols (+ (- n k) 1)))
    (for/list ([i (in-range out-rows)])
      (for/list ([j (in-range out-cols)])
        (let* ((vals
                (for*/list ([di (in-range k)]
                            [dj (in-range k)])
                  (list-ref (list-ref grid (+ i di)) (+ j dj)))))
          (if (= (length vals) 1)
              0
              (let* ((sorted (sort vals <))
                     (diffs (for/list ([idx (in-range (- (length sorted) 1))])
                              (abs (- (list-ref sorted (+ idx 1))
                                      (list-ref sorted idx)))))
                     (min-diff (apply min diffs)))
                min-diff)))))))
```

## Erlang

```erlang
-spec min_abs_diff(Grid :: [[integer()]], K :: integer()) -> [[integer()]].
-export([min_abs_diff/2]).

min_abs_diff(Grid, K) ->
    M = length(Grid),
    N = length(hd(Grid)),
    R = M - K + 1,
    C = N - K + 1,
    [ [ compute_min(Grid, K, I, J) || J <- lists:seq(0, C-1) ] || I <- lists:seq(0, R-1) ].

compute_min(Grid, K, I, J) ->
    Elements = get_window(Grid, I, J, K),
    case length(Elements) of
        L when L < 2 -> 0;
        _ ->
            Sorted = lists:sort(Elements),
            min_adjacent_diff(Sorted)
    end.

get_window(Grid, I, J, K) ->
    Rows = lists:sublist(lists:nthtail(I, Grid), K),
    lists:flatten([lists:sublist(lists:nthtail(J, Row), K) || Row <- Rows]).

min_adjacent_diff([First|Rest]) ->
    min_adjacent_diff(Rest, First, 1000000000).

min_adjacent_diff([], _Prev, Min) -> Min;
min_adjacent_diff([Curr|Tail], Prev, Min) ->
    D = erlang:abs(Curr - Prev),
    NewMin = if D < Min -> D; true -> Min end,
    min_adjacent_diff(Tail, Curr, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_abs_diff(grid :: [[integer]], k :: integer) :: [[integer]]
  def min_abs_diff(grid, k) do
    m = length(grid)
    n = length(hd(grid))
    rows_out = m - k + 1
    cols_out = n - k + 1

    for i <- 0..(rows_out - 1) do
      for j <- 0..(cols_out - 1) do
        vals =
          for r <- i..(i + k - 1), into: [] do
            row = Enum.at(grid, r)
            Enum.slice(row, j, k)
          end
          |> List.flatten()

        case vals do
          [_] -> 0
          _ ->
            sorted = Enum.sort(vals)

            diffs =
              for idx <- 0..(length(sorted) - 2) do
                abs(Enum.at(sorted, idx + 1) - Enum.at(sorted, idx))
              end

            Enum.min(diffs)
        end
      end
    end
  end
end
```

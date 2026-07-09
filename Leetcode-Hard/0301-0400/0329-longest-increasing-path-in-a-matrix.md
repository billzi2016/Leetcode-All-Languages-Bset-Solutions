# 0329. Longest Increasing Path in a Matrix

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        
        function<int(int,int)> dfs = [&](int i, int j) -> int {
            if (dp[i][j]) return dp[i][j];
            int best = 1;
            for (auto &d : dirs) {
                int ni = i + d[0], nj = j + d[1];
                if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
                if (matrix[ni][nj] > matrix[i][j]) {
                    best = max(best, 1 + dfs(ni, nj));
                }
            }
            dp[i][j] = best;
            return best;
        };
        
        int ans = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                ans = max(ans, dfs(i, j));
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int rows;
    private int cols;
    private int[][] memo;
    private static final int[][] DIRS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
        rows = matrix.length;
        cols = matrix[0].length;
        memo = new int[rows][cols];
        int maxLen = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                maxLen = Math.max(maxLen, dfs(matrix, i, j));
            }
        }
        return maxLen;
    }
    
    private int dfs(int[][] matrix, int r, int c) {
        if (memo[r][c] != 0) return memo[r][c];
        int best = 1;
        for (int[] d : DIRS) {
            int nr = r + d[0], nc = c + d[1];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            if (matrix[nr][nc] > matrix[r][c]) {
                best = Math.max(best, 1 + dfs(matrix, nr, nc));
            }
        }
        memo[r][c] = best;
        return best;
    }
}
```

## Python

```python
import sys

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        sys.setrecursionlimit(1000000)
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            max_len = 1
            cur_val = matrix[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > cur_val:
                    length = 1 + dfs(ni, nj)
                    if length > max_len:
                        max_len = length
            dp[i][j] = max_len
            return max_len

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        return result
```

## Python3

```python
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i: int, j: int) -> int:
            if dp[i][j]:
                return dp[i][j]
            best = 1
            cur = matrix[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > cur:
                    best = max(best, 1 + dfs(ni, nj))
            dp[i][j] = best
            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
```

## C

```c
#include <stdlib.h>

static int dfs(int i, int j, int rows, int cols, int **matrix, int **dp) {
    if (dp[i][j] != 0) return dp[i][j];
    static const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    int maxLen = 1;
    for (int d = 0; d < 4; ++d) {
        int ni = i + dirs[d][0];
        int nj = j + dirs[d][1];
        if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && matrix[ni][nj] > matrix[i][j]) {
            int len = 1 + dfs(ni, nj, rows, cols, matrix, dp);
            if (len > maxLen) maxLen = len;
        }
    }
    dp[i][j] = maxLen;
    return maxLen;
}

int longestIncreasingPath(int** matrix, int matrixSize, int* matrixColSize){
    if (matrixSize == 0 || matrixColSize == NULL) return 0;
    int rows = matrixSize;
    int cols = *matrixColSize;

    int **dp = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; ++i) {
        dp[i] = (int *)calloc(cols, sizeof(int));
    }

    int result = 0;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            int cur = dfs(i, j, rows, cols, matrix, dp);
            if (cur > result) result = cur;
        }
    }

    for (int i = 0; i < rows; ++i) {
        free(dp[i]);
    }
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0)
            return 0;

        int m = matrix.Length;
        int n = matrix[0].Length;
        int[,] memo = new int[m, n];
        int maxLen = 0;
        int[] dirs = new int[] { -1, 0, 1, 0, -1 };

        int Dfs(int i, int j) {
            if (memo[i, j] != 0)
                return memo[i, j];

            int best = 1;
            int curVal = matrix[i][j];
            for (int d = 0; d < 4; ++d) {
                int ni = i + dirs[d];
                int nj = j + dirs[d + 1];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && matrix[ni][nj] > curVal) {
                    int len = 1 + Dfs(ni, nj);
                    if (len > best)
                        best = len;
                }
            }

            memo[i, j] = best;
            return best;
        }

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int curLen = Dfs(i, j);
                if (curLen > maxLen)
                    maxLen = curLen;
            }
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function(matrix) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return 0;
    const rows = matrix.length, cols = matrix[0].length;
    const cache = Array.from({ length: rows }, () => Array(cols).fill(0));
    const dirs = [[-1,0],[1,0],[0,-1],[0,1]];
    
    function dfs(r, c) {
        if (cache[r][c] !== 0) return cache[r][c];
        let maxLen = 1;
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && matrix[nr][nc] > matrix[r][c]) {
                const len = 1 + dfs(nr, nc);
                if (len > maxLen) maxLen = len;
            }
        }
        cache[r][c] = maxLen;
        return maxLen;
    }
    
    let result = 0;
    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            const cur = dfs(i, j);
            if (cur > result) result = cur;
        }
    }
    return result;
};
```

## Typescript

```typescript
function longestIncreasingPath(matrix: number[][]): number {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return 0;
    const m = matrix.length, n = matrix[0].length;
    const indegree: number[][] = Array.from({ length: m }, () => Array(n).fill(0));
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            for (const [dx, dy] of dirs) {
                const x = i + dx, y = j + dy;
                if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] > matrix[i][j]) {
                    indegree[x][y]++;
                }
            }
        }
    }
    
    let queue: [number, number][] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (indegree[i][j] === 0) queue.push([i, j]);
        }
    }
    
    let length = 0;
    while (queue.length > 0) {
        const next: [number, number][] = [];
        for (const [i, j] of queue) {
            for (const [dx, dy] of dirs) {
                const x = i + dx, y = j + dy;
                if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] > matrix[i][j]) {
                    indegree[x][y]--;
                    if (indegree[x][y] === 0) next.push([x, y]);
                }
            }
        }
        length++;
        queue = next;
    }
    
    return length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function longestIncreasingPath($matrix) {
        $rows = count($matrix);
        if ($rows == 0) return 0;
        $cols = count($matrix[0]);
        $cache = array_fill(0, $rows, array_fill(0, $cols, 0));
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];
        
        $dfs = function($r, $c) use (&$dfs, &$matrix, &$cache, $rows, $cols, $dirs) {
            if ($cache[$r][$c] != 0) {
                return $cache[$r][$c];
            }
            $maxLen = 1;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols && $matrix[$nr][$nc] > $matrix[$r][$c]) {
                    $len = 1 + $dfs($nr, $nc);
                    if ($len > $maxLen) {
                        $maxLen = $len;
                    }
                }
            }
            $cache[$r][$c] = $maxLen;
            return $maxLen;
        };
        
        $result = 0;
        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                $res = $dfs($i, $j);
                if ($res > $result) {
                    $result = $res;
                }
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func longestIncreasingPath(_ matrix: [[Int]]) -> Int {
        let m = matrix.count
        guard m > 0 else { return 0 }
        let n = matrix[0].count
        var memo = Array(repeating: Array(repeating: 0, count: n), count: m)
        let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        func dfs(_ i: Int, _ j: Int) -> Int {
            if memo[i][j] != 0 { return memo[i][j] }
            var maxLen = 1
            for d in dirs {
                let ni = i + d.0
                let nj = j + d.1
                if ni >= 0 && ni < m && nj >= 0 && nj < n && matrix[ni][nj] > matrix[i][j] {
                    let len = 1 + dfs(ni, nj)
                    if len > maxLen { maxLen = len }
                }
            }
            memo[i][j] = maxLen
            return maxLen
        }
        
        var result = 0
        for i in 0..<m {
            for j in 0..<n {
                let cur = dfs(i, j)
                if cur > result { result = cur }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestIncreasingPath(matrix: Array<IntArray>): Int {
        if (matrix.isEmpty() || matrix[0].isEmpty()) return 0
        val m = matrix.size
        val n = matrix[0].size
        val dp = Array(m) { IntArray(n) }
        var result = 0
        val dirs = intArrayOf(-1, 0, 1, 0, -1)

        fun dfs(i: Int, j: Int): Int {
            if (dp[i][j] != 0) return dp[i][j]
            var best = 1
            for (k in 0 until 4) {
                val ni = i + dirs[k]
                val nj = j + dirs[k + 1]
                if (ni in 0 until m && nj in 0 until n && matrix[ni][nj] > matrix[i][j]) {
                    best = maxOf(best, 1 + dfs(ni, nj))
                }
            }
            dp[i][j] = best
            return best
        }

        for (i in 0 until m) {
            for (j in 0 until n) {
                result = maxOf(result, dfs(i, j))
            }
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int longestIncreasingPath(List<List<int>> matrix) {
    if (matrix.isEmpty || matrix[0].isEmpty) return 0;
    final m = matrix.length;
    final n = matrix[0].length;

    List<List<int>> indegree = List.generate(m, (_) => List.filled(n, 0));
    const dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    // Compute indegrees: edge from lower to higher value cell
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        for (var d in dirs) {
          int ni = i + d[0];
          int nj = j + d[1];
          if (ni >= 0 &&
              ni < m &&
              nj >= 0 &&
              nj < n &&
              matrix[ni][nj] > matrix[i][j]) {
            indegree[ni][nj]++;
          }
        }
      }
    }

    // Initialize queue with cells having zero indegree
    Queue<List<int>> queue = Queue();
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (indegree[i][j] == 0) {
          queue.add([i, j]);
        }
      }
    }

    int pathLen = 0;
    while (queue.isNotEmpty) {
      int size = queue.length;
      for (int s = 0; s < size; s++) {
        final cell = queue.removeFirst();
        int i = cell[0];
        int j = cell[1];
        for (var d in dirs) {
          int ni = i + d[0];
          int nj = j + d[1];
          if (ni >= 0 &&
              ni < m &&
              nj >= 0 &&
              nj < n &&
              matrix[ni][nj] > matrix[i][j]) {
            indegree[ni][nj]--;
            if (indegree[ni][nj] == 0) {
              queue.add([ni, nj]);
            }
          }
        }
      }
      pathLen++;
    }

    return pathLen;
  }
}
```

## Golang

```go
func longestIncreasingPath(matrix [][]int) int {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return 0
    }
    m, n := len(matrix), len(matrix[0])
    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
    }
    dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    var dfs func(int, int) int
    dfs = func(i, j int) int {
        if dp[i][j] != 0 {
            return dp[i][j]
        }
        maxLen := 1
        for _, d := range dirs {
            ni, nj := i+d[0], j+d[1]
            if ni >= 0 && ni < m && nj >= 0 && nj < n && matrix[ni][nj] > matrix[i][j] {
                length := 1 + dfs(ni, nj)
                if length > maxLen {
                    maxLen = length
                }
            }
        }
        dp[i][j] = maxLen
        return maxLen
    }

    ans := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if v := dfs(i, j); v > ans {
                ans = v
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def longest_increasing_path(matrix)
  return 0 if matrix.empty? || matrix[0].empty?
  m = matrix.size
  n = matrix[0].size
  dp = Array.new(m) { Array.new(n, 0) }
  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  dfs = nil
  dfs = ->(i, j) do
    return dp[i][j] if dp[i][j] != 0
    best = 1
    dirs.each do |dx, dy|
      x = i + dx
      y = j + dy
      next unless x.between?(0, m - 1) && y.between?(0, n - 1)
      if matrix[x][y] > matrix[i][j]
        len = 1 + dfs.call(x, y)
        best = len if len > best
      end
    end
    dp[i][j] = best
    best
  end

  max_len = 0
  (0...m).each do |i|
    (0...n).each do |j|
      cur = dfs.call(i, j)
      max_len = cur if cur > max_len
    end
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def longestIncreasingPath(matrix: Array[Array[Int]]): Int = {
        if (matrix.isEmpty || matrix.head.isEmpty) return 0
        val m = matrix.length
        val n = matrix(0).length
        val dp = Array.ofDim[Int](m, n)
        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i: Int, j: Int): Int = {
            if (dp(i)(j) != 0) return dp(i)(j)
            var best = 1
            for ((dx, dy) <- dirs) {
                val x = i + dx
                val y = j + dy
                if (x >= 0 && x < m && y >= 0 && y < n && matrix(x)(y) > matrix(i)(j)) {
                    val len = 1 + dfs(x, y)
                    if (len > best) best = len
                }
            }
            dp(i)(j) = best
            best
        }

        var ans = 0
        for (i <- 0 until m; j <- 0 until n) {
            val cur = dfs(i, j)
            if (cur > ans) ans = cur
        }
        ans
    }
}
```

## Rust

```rust
pub struct Solution;

fn dfs(i: usize, j: usize, matrix: &Vec<Vec<i32>>, dp: &mut Vec<Vec<i32>>) -> i32 {
    if dp[i][j] != 0 {
        return dp[i][j];
    }
    let m = matrix.len() as i32;
    let n = matrix[0].len() as i32;
    let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    let mut best = 1i32;
    for &(dx, dy) in &dirs {
        let ni = i as i32 + dx;
        let nj = j as i32 + dy;
        if ni >= 0 && ni < m && nj >= 0 && nj < n {
            if matrix[ni as usize][nj as usize] > matrix[i][j] {
                let len = 1 + dfs(ni as usize, nj as usize, matrix, dp);
                if len > best {
                    best = len;
                }
            }
        }
    }
    dp[i][j] = best;
    best
}

impl Solution {
    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }
        let m = matrix.len();
        let n = matrix[0].len();
        let mut dp = vec![vec![0i32; n]; m];
        let mut result = 0i32;
        for i in 0..m {
            for j in 0..n {
                let len = dfs(i, j, &matrix, &mut dp);
                if len > result {
                    result = len;
                }
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (longest-increasing-path matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length matrix))
         (n (if (> m 0) (length (first matrix)) 0))
         (mat (list->vector (map list->vector matrix)))
         ;; dp[i][j] = longest path starting at (i,j), 0 means uncomputed
         (dp (let ((v (make-vector m)))
               (for ([i (in-range m)])
                 (vector-set! v i (make-vector n 0)))
               v))
         (dirs '((1 0) (-1 0) (0 1) (0 -1))))
    (letrec ((dfs (lambda (i j)
                    (let ((cached (vector-ref (vector-ref dp i) j)))
                      (if (> cached 0)
                          cached
                          (let* ((cur (vector-ref (vector-ref mat i) j))
                                 (best 1))
                            (for-each (lambda (d)
                                        (define ni (+ i (car d)))
                                        (define nj (+ j (cadr d)))
                                        (when (and (>= ni 0) (< ni m)
                                                   (>= nj 0) (< nj n))
                                          (let ((next-val (vector-ref (vector-ref mat ni) nj)))
                                            (when (> next-val cur)
                                              (set! best (max best (+ 1 (dfs ni nj))))))))
                                      dirs)
                            (vector-set! (vector-ref dp i) j best)
                            best))))))
      (let ((ans 0))
        (for ([i (in-range m)])
          (for ([j (in-range n)])
            (set! ans (max ans (dfs i j)))))
        ans))))
```

## Erlang

```erlang
-export([longest_increasing_path/1]).

-spec longest_increasing_path(Matrix :: [[integer()]]) -> integer().
longest_increasing_path(Matrix) ->
    case Matrix of
        [] -> 0;
        _ ->
            M = length(Matrix),
            N = length(lists:nth(1, Matrix)),
            ValueList = [
                {{I, J}, Val}
                ||
                {Row, I} <- lists:zip(Matrix, lists:seq(0, M - 1)),
                {Val, J} <- lists:zip(Row, lists:seq(0, N - 1))
            ],
            ValueMap = maps:from_list(ValueList),
            IndegMap = build_indeg(ValueMap),
            Queue0 = [
                Key
                ||
                {Key, _} <- maps:to_list(ValueMap),
                maps:get(Key, IndegMap, 0) == 0
            ],
            bfs(lists:reverse(Queue0), IndegMap, ValueMap)
    end.

%% Build indegree map: for each cell, count incoming edges from lower neighbors.
build_indeg(ValueMap) ->
    lists:foldl(
        fun({{I, J}, Val}, Acc) ->
            Neighs = [{I - 1, J}, {I + 1, J}, {I, J - 1}, {I, J + 1}],
            lists:foldl(
                fun(NKey, M2) ->
                    case maps:get(NKey, ValueMap, undefined) of
                        undefined -> M2;
                        NVal when NVal > Val ->
                            maps:update_with(NKey,
                                fun(V) -> V + 1 end,
                                1,
                                M2);
                        _ -> M2
                    end
                end,
                Acc,
                Neighs)
        end,
        #{},
        maps:to_list(ValueMap)).

%% BFS layer by layer; each layer corresponds to one step in longest path.
bfs([], _, _) ->
    0;
bfs(Queue, IndegMap, ValueMap) ->
    {NextQueue, NewIndeg} = process_layer(Queue, IndegMap, ValueMap, []),
    1 + bfs(lists:reverse(NextQueue), NewIndeg, ValueMap).

process_layer([], IndegMap, _ValueMap, Acc) ->
    {Acc, IndegMap};
process_layer([Cell | Rest], IndegMap, ValueMap, Acc) ->
    Val = maps:get(Cell, ValueMap),
    {I, J} = Cell,
    Neighs = [{I - 1, J}, {I + 1, J}, {I, J - 1}, {I, J + 1}],
    {Indeg2, Acc2} = lists:foldl(
        fun(NKey, {MAcc, NextAcc}) ->
            case maps:get(NKey, ValueMap, undefined) of
                undefined -> {MAcc, NextAcc};
                NVal when NVal > Val ->
                    MNew = maps:update_with(NKey,
                        fun(V) -> V - 1 end,
                        0,
                        MAcc),
                    case maps:get(NKey, MNew) of
                        0 -> {MNew, [NKey | NextAcc]};
                        _ -> {MNew, NextAcc}
                    end;
                _ -> {MAcc, NextAcc}
            end
        end,
        {IndegMap, Acc},
        Neighs),
    process_layer(Rest, Indeg2, ValueMap, Acc2).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_increasing_path(matrix :: [[integer]]) :: integer
  def longest_increasing_path(matrix) do
    rows = Enum.map(matrix, &List.to_tuple/1) |> List.to_tuple()
    m = tuple_size(rows)
    n = tuple_size(elem(rows, 0))
    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    indeg_map =
      Enum.reduce(0..m - 1, %{}, fn i, acc ->
        Enum.reduce(0..n - 1, acc, fn j, acc2 ->
          val = elem(elem(rows, i), j)

          indeg =
            Enum.count(dirs, fn {di, dj} ->
              ni = i + di
              nj = j + dj

              if ni >= 0 and ni < m and nj >= 0 and nj < n do
                neighbor_val = elem(elem(rows, ni), nj)
                neighbor_val < val
              else
                false
              end
            end)

          Map.put(acc2, {i, j}, indeg)
        end)
      end)

    init_queue =
      for i <- 0..m - 1,
          j <- 0..n - 1,
          Map.get(indeg_map, {i, j}) == 0,
          do: {i, j}

    queue = :queue.from_list(init_queue)
    bfs(queue, indeg_map, rows, m, n, 0)
  end

  defp bfs(queue, indeg_map, rows, m, n, len) do
    if :queue.is_empty(queue) do
      len
    else
      {new_queue, new_indeg} = process_layer(queue, indeg_map, [], rows, m, n)
      bfs(new_queue, new_indeg, rows, m, n, len + 1)
    end
  end

  defp process_layer(queue, indeg_map, next_acc, rows, m, n) do
    case :queue.out(queue) do
      {:empty, _} ->
        {Enum.reverse(next_acc) |> :queue.from_list(), indeg_map}

      {{:value, {i, j}}, q_rest} ->
        val = elem(elem(rows, i), j)

        {updated_indeg, updated_next} =
          Enum.reduce([{-1, 0}, {1, 0}, {0, -1}, {0, 1}], {indeg_map, next_acc},
            fn {di, dj}, {imap, acc} ->
              ni = i + di
              nj = j + dj

              if ni >= 0 and ni < m and nj >= 0 and nj < n do
                neighbor_val = elem(elem(rows, ni), nj)

                if neighbor_val > val do
                  key = {ni, nj}
                  cur = Map.get(imap, key)
                  new_cur = cur - 1
                  imap2 = Map.put(imap, key, new_cur)
                  acc2 = if new_cur == 0, do: [{ni, nj} | acc], else: acc
                  {imap2, acc2}
                else
                  {imap, acc}
                end
              else
                {imap, acc}
              end
            end)

        process_layer(q_rest, updated_indeg, updated_next, rows, m, n)
    end
  end
end
```

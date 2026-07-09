# 1905. Count Sub Islands

## Cpp

```cpp
class Solution {
public:
    int countSubIslands(std::vector<std::vector<int>>& grid1, std::vector<std::vector<int>>& grid2) {
        int m = grid1.size();
        int n = grid1[0].size();
        std::vector<std::vector<char>> visited(m, std::vector<char>(n, 0));
        int subIslands = 0;
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid2[i][j] == 1 && !visited[i][j]) {
                    bool isSub = true;
                    std::stack<std::pair<int,int>> st;
                    st.emplace(i, j);
                    visited[i][j] = 1;
                    
                    while (!st.empty()) {
                        auto [x, y] = st.top();
                        st.pop();
                        if (grid1[x][y] == 0) isSub = false;
                        
                        for (auto &d : dirs) {
                            int nx = x + d[0];
                            int ny = y + d[1];
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
                                grid2[nx][ny] == 1 && !visited[nx][ny]) {
                                visited[nx][ny] = 1;
                                st.emplace(nx, ny);
                            }
                        }
                    }
                    
                    if (isSub) ++subIslands;
                }
            }
        }
        
        return subIslands;
    }
};
```

## Java

```java
class Solution {
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int m = grid1.length;
        int n = grid1[0].length;
        boolean[][] visited = new boolean[m][n];
        int subIslandCount = 0;
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid2[i][j] == 1 && !visited[i][j]) {
                    boolean isSubIsland = true;
                    java.util.ArrayDeque<int[]> queue = new java.util.ArrayDeque<>();
                    visited[i][j] = true;
                    queue.offer(new int[]{i, j});

                    while (!queue.isEmpty()) {
                        int[] cur = queue.poll();
                        int r = cur[0], c = cur[1];
                        if (grid1[r][c] == 0) {
                            isSubIsland = false;
                        }
                        for (int d = 0; d < 4; d++) {
                            int nr = r + dr[d];
                            int nc = c + dc[d];
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                                grid2[nr][nc] == 1 && !visited[nr][nc]) {
                                visited[nr][nc] = true;
                                queue.offer(new int[]{nr, nc});
                            }
                        }
                    }

                    if (isSubIsland) {
                        subIslandCount++;
                    }
                }
            }
        }

        return subIslandCount;
    }
}
```

## Python

```python
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid1), len(grid1[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    stack = [(i, j)]
                    is_sub = True
                    while stack:
                        x, y = stack.pop()
                        if grid2[x][y] == 0:
                            continue
                        grid2[x][y] = 0
                        if grid1[x][y] == 0:
                            is_sub = False
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                                stack.append((nx, ny))
                    if is_sub:
                        count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        sub_islands = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    stack = [(i, j)]
                    visited[i][j] = True
                    is_sub = True
                    while stack:
                        x, y = stack.pop()
                        if grid1[x][y] == 0:
                            is_sub = False
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid2[nx][ny] == 1:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                    if is_sub:
                        sub_islands += 1

        return sub_islands
```

## C

```c
#include <stdlib.h>

int countSubIslands(int** grid1, int grid1Size, int* grid1ColSize,
                    int** grid2, int grid2Size, int* grid2ColSize) {
    int rows = grid1Size;
    int cols = grid1ColSize[0];

    char *visited = (char *)calloc(rows * cols, sizeof(char));
    int *queue = (int *)malloc(rows * cols * sizeof(int));

    int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int subIslands = 0;

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            int idx = i * cols + j;
            if (grid2[i][j] == 1 && !visited[idx]) {
                int front = 0, back = 0;
                queue[back++] = idx;
                visited[idx] = 1;
                int isSub = 1;

                while (front < back) {
                    int cur = queue[front++];
                    int x = cur / cols;
                    int y = cur % cols;

                    if (grid1[x][y] == 0)
                        isSub = 0;

                    for (int d = 0; d < 4; ++d) {
                        int nx = x + dirs[d][0];
                        int ny = y + dirs[d][1];
                        if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                            int nidx = nx * cols + ny;
                            if (!visited[nidx] && grid2[nx][ny] == 1) {
                                visited[nidx] = 1;
                                queue[back++] = nidx;
                            }
                        }
                    }
                }

                if (isSub)
                    ++subIslands;
            }
        }
    }

    free(visited);
    free(queue);
    return subIslands;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountSubIslands(int[][] grid1, int[][] grid2)
    {
        int m = grid1.Length;
        int n = grid1[0].Length;

        bool[][] visited = new bool[m][];
        for (int i = 0; i < m; i++)
            visited[i] = new bool[n];

        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        int subIslandCount = 0;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid2[i][j] == 1 && !visited[i][j])
                {
                    bool isSubIsland = true;
                    var queue = new System.Collections.Generic.Queue<int[]>();
                    queue.Enqueue(new int[] { i, j });
                    visited[i][j] = true;

                    if (grid1[i][j] == 0)
                        isSubIsland = false;

                    while (queue.Count > 0)
                    {
                        int[] cur = queue.Dequeue();
                        int r = cur[0], c = cur[1];

                        for (int d = 0; d < 4; d++)
                        {
                            int nr = r + dr[d];
                            int nc = c + dc[d];

                            if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                                grid2[nr][nc] == 1 && !visited[nr][nc])
                            {
                                visited[nr][nc] = true;
                                if (grid1[nr][nc] == 0)
                                    isSubIsland = false;
                                queue.Enqueue(new int[] { nr, nc });
                            }
                        }
                    }

                    if (isSubIsland)
                        subIslandCount++;
                }
            }
        }

        return subIslandCount;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid1
 * @param {number[][]} grid2
 * @return {number}
 */
var countSubIslands = function(grid1, grid2) {
    const m = grid1.length;
    const n = grid1[0].length;
    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let subCount = 0;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid2[i][j] === 1 && !visited[i][j]) {
                // start BFS for this island
                const queue = [];
                let qh = 0;
                queue.push([i, j]);
                visited[i][j] = true;
                let isSub = true;

                while (qh < queue.length) {
                    const [x, y] = queue[qh++];
                    if (grid1[x][y] === 0) {
                        isSub = false;
                    }
                    for (const [dx, dy] of dirs) {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (
                            nx >= 0 && nx < m &&
                            ny >= 0 && ny < n &&
                            grid2[nx][ny] === 1 &&
                            !visited[nx][ny]
                        ) {
                            visited[nx][ny] = true;
                            queue.push([nx, ny]);
                        }
                    }
                }

                if (isSub) subCount++;
            }
        }
    }

    return subCount;
};
```

## Typescript

```typescript
function countSubIslands(grid1: number[][], grid2: number[][]): number {
    const m = grid1.length;
    const n = grid1[0].length;
    const visited: Uint8Array[] = Array.from({ length: m }, () => new Uint8Array(n));
    let result = 0;
    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid2[i][j] === 1 && visited[i][j] === 0) {
                let isSub = true;
                const queue: [number, number][] = [[i, j]];
                visited[i][j] = 1;
                let qIdx = 0;

                while (qIdx < queue.length) {
                    const [x, y] = queue[qIdx++];
                    if (grid1[x][y] === 0) isSub = false;

                    for (const [dx, dy] of dirs) {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (
                            nx >= 0 &&
                            nx < m &&
                            ny >= 0 &&
                            ny < n &&
                            grid2[nx][ny] === 1 &&
                            visited[nx][ny] === 0
                        ) {
                            visited[nx][ny] = 1;
                            queue.push([nx, ny]);
                        }
                    }
                }

                if (isSub) result++;
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $grid1
     * @param Integer[][] $grid2
     * @return Integer
     */
    function countSubIslands($grid1, $grid2) {
        $m = count($grid1);
        $n = count($grid1[0]);
        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $count = 0;
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];
        
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid2[$i][$j] == 1 && !$visited[$i][$j]) {
                    $queue = new SplQueue();
                    $queue->enqueue([$i, $j]);
                    $visited[$i][$j] = true;
                    $isSub = true;
                    
                    while (!$queue->isEmpty()) {
                        [$x, $y] = $queue->dequeue();
                        if ($grid1[$x][$y] == 0) {
                            $isSub = false;
                        }
                        foreach ($dirs as $d) {
                            $nx = $x + $d[0];
                            $ny = $y + $d[1];
                            if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n &&
                                $grid2[$nx][$ny] == 1 && !$visited[$nx][$ny]) {
                                $visited[$nx][$ny] = true;
                                $queue->enqueue([$nx, $ny]);
                            }
                        }
                    }
                    
                    if ($isSub) {
                        $count++;
                    }
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
    func countSubIslands(_ grid1: [[Int]], _ grid2: [[Int]]) -> Int {
        let m = grid1.count
        guard m > 0 else { return 0 }
        let n = grid1[0].count
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        var result = 0
        
        for i in 0..<m {
            for j in 0..<n {
                if grid2[i][j] == 1 && !visited[i][j] {
                    var isSubIsland = true
                    var queue: [(Int, Int)] = [(i, j)]
                    visited[i][j] = true
                    var index = 0
                    
                    while index < queue.count {
                        let (x, y) = queue[index]
                        index += 1
                        
                        if grid1[x][y] == 0 {
                            isSubIsland = false
                        }
                        
                        for (dx, dy) in dirs {
                            let nx = x + dx
                            let ny = y + dy
                            if nx >= 0 && nx < m && ny >= 0 && ny < n {
                                if grid2[nx][ny] == 1 && !visited[nx][ny] {
                                    visited[nx][ny] = true
                                    queue.append((nx, ny))
                                }
                            }
                        }
                    }
                    
                    if isSubIsland {
                        result += 1
                    }
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun countSubIslands(grid1: Array<IntArray>, grid2: Array<IntArray>): Int {
        val m = grid1.size
        val n = grid1[0].size
        val visited = Array(m) { BooleanArray(n) }
        var subIslandCount = 0
        val dirs = intArrayOf(-1, 0, 1, 0, -1)

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid2[i][j] == 1 && !visited[i][j]) {
                    var isSub = true
                    val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
                    queue.add(Pair(i, j))
                    visited[i][j] = true

                    while (queue.isNotEmpty()) {
                        val (x, y) = queue.removeFirst()
                        if (grid1[x][y] == 0) isSub = false
                        for (k in 0 until 4) {
                            val nx = x + dirs[k]
                            val ny = y + dirs[k + 1]
                            if (nx in 0 until m && ny in 0 until n &&
                                grid2[nx][ny] == 1 && !visited[nx][ny]) {
                                visited[nx][ny] = true
                                queue.add(Pair(nx, ny))
                            }
                        }
                    }

                    if (isSub) subIslandCount++
                }
            }
        }

        return subIslandCount
    }
}
```

## Dart

```dart
class Solution {
  int countSubIslands(List<List<int>> grid1, List<List<int>> grid2) {
    final int m = grid1.length;
    final int n = grid1[0].length;
    final List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));
    int subIslandCount = 0;
    const List<List<int>> dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1]
    ];

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid2[i][j] == 1 && !visited[i][j]) {
          bool isSubIsland = true;
          final List<int> queue = [];
          int head = 0;
          queue.add(i * n + j);
          visited[i][j] = true;

          while (head < queue.length) {
            final int cur = queue[head++];
            final int x = cur ~/ n;
            final int y = cur % n;

            if (grid1[x][y] == 0) {
              isSubIsland = false;
            }

            for (final dir in dirs) {
              final int nx = x + dir[0];
              final int ny = y + dir[1];
              if (nx >= 0 &&
                  nx < m &&
                  ny >= 0 &&
                  ny < n &&
                  grid2[nx][ny] == 1 &&
                  !visited[nx][ny]) {
                visited[nx][ny] = true;
                queue.add(nx * n + ny);
              }
            }
          }

          if (isSubIsland) {
            subIslandCount++;
          }
        }
      }
    }

    return subIslandCount;
  }
}
```

## Golang

```go
func countSubIslands(grid1 [][]int, grid2 [][]int) int {
	m := len(grid2)
	if m == 0 {
		return 0
	}
	n := len(grid2[0])

	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	count := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid2[i][j] == 1 && !visited[i][j] {
				sub := true
				queue := make([][2]int, 0)
				queue = append(queue, [2]int{i, j})
				visited[i][j] = true

				for len(queue) > 0 {
					cur := queue[0]
					queue = queue[1:]
					x, y := cur[0], cur[1]

					if grid1[x][y] == 0 {
						sub = false
					}

					for _, d := range dirs {
						nx, ny := x+d[0], y+d[1]
						if nx >= 0 && nx < m && ny >= 0 && ny < n &&
							grid2[nx][ny] == 1 && !visited[nx][ny] {
							visited[nx][ny] = true
							queue = append(queue, [2]int{nx, ny})
						}
					}
				}

				if sub {
					count++
				}
			}
		}
	}

	return count
}
```

## Ruby

```ruby
def count_sub_islands(grid1, grid2)
  m = grid1.size
  n = grid1[0].size
  visited = Array.new(m) { Array.new(n, false) }
  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  count = 0

  (0...m).each do |i|
    (0...n).each do |j|
      next unless grid2[i][j] == 1 && !visited[i][j]

      stack = [[i, j]]
      visited[i][j] = true
      is_sub = true

      until stack.empty?
        x, y = stack.pop
        is_sub = false if grid1[x][y] == 0

        dirs.each do |dx, dy|
          nx = x + dx
          ny = y + dy
          if nx.between?(0, m - 1) && ny.between?(0, n - 1) &&
             grid2[nx][ny] == 1 && !visited[nx][ny]
            visited[nx][ny] = true
            stack << [nx, ny]
          end
        end
      end

      count += 1 if is_sub
    end
  end

  count
end
```

## Scala

```scala
object Solution {
  import java.util.ArrayDeque

  def countSubIslands(grid1: Array[Array[Int]], grid2: Array[Array[Int]]): Int = {
    val m = grid1.length
    val n = if (m == 0) 0 else grid1(0).length
    val visited = Array.ofDim[Boolean](m, n)
    var count = 0

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    for (i <- 0 until m; j <- 0 until n) {
      if (grid2(i)(j) == 1 && !visited(i)(j)) {
        val queue = new ArrayDeque[(Int, Int)]()
        queue.add((i, j))
        visited(i)(j) = true
        var isSub = true

        while (!queue.isEmpty) {
          val (x, y) = queue.poll()
          if (grid1(x)(y) == 0) isSub = false

          for ((dx, dy) <- dirs) {
            val nx = x + dx
            val ny = y + dy
            if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
                grid2(nx)(ny) == 1 && !visited(nx)(ny)) {
              visited(nx)(ny) = true
              queue.add((nx, ny))
            }
          }
        }

        if (isSub) count += 1
      }
    }

    count
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn count_sub_islands(grid1: Vec<Vec<i32>>, grid2: Vec<Vec<i32>>) -> i32 {
        let m = grid1.len();
        if m == 0 {
            return 0;
        }
        let n = grid1[0].len();

        let mut visited = vec![vec![false; n]; m];
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        let mut count = 0;

        for i in 0..m {
            for j in 0..n {
                if grid2[i][j] == 1 && !visited[i][j] {
                    let mut queue = VecDeque::new();
                    visited[i][j] = true;
                    queue.push_back((i, j));
                    let mut is_sub = true;

                    while let Some((x, y)) = queue.pop_front() {
                        if grid1[x][y] == 0 {
                            is_sub = false;
                        }
                        for (dx, dy) in &dirs {
                            let nx = x as i32 + dx;
                            let ny = y as i32 + dy;
                            if nx >= 0 && nx < m as i32 && ny >= 0 && ny < n as i32 {
                                let ux = nx as usize;
                                let uy = ny as usize;
                                if grid2[ux][uy] == 1 && !visited[ux][uy] {
                                    visited[ux][uy] = true;
                                    queue.push_back((ux, uy));
                                }
                            }
                        }
                    }

                    if is_sub {
                        count += 1;
                    }
                }
            }
        }

        count as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (count-sub-islands grid1 grid2)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      exact-integer?)
  (let* ((m (length grid1))
         (n (if (= m 0) 0 (length (car grid1))))
         (g1 (list->vector (map list->vector grid1)))
         (g2 (list->vector (map list->vector grid2)))
         (visited
          (let ((v (make-vector m)))
            (for ([i (in-range m)])
              (vector-set! v i (make-vector n #f)))
            v))
         (queue (make-vector (* m n) -1))
         (dirs '((-1 . 0) (1 . 0) (0 . -1) (0 . 1))))
    (define (in-bounds x y)
      (and (>= x 0) (< x m) (>= y 0) (< y n)))
    (let ((count 0))
      (for ([i (in-range m)])
        (for ([j (in-range n)])
          (when (and (= (vector-ref (vector-ref g2 i) j) 1)
                     (not (vector-ref (vector-ref visited i) j)))
            ;; start BFS for this island
            (let ((head 0) (tail 0) (is-sub #t))
              (define start-idx (+ (* i n) j))
              (vector-set! queue tail start-idx)
              (set! tail (+ tail 1))
              (vector-set! (vector-ref visited i) j #t)
              (when (= (vector-ref (vector-ref g1 i) j) 0)
                (set! is-sub #f))
              ;; BFS traversal
              (let bfs-loop ()
                (when (< head tail)
                  (define idx (vector-ref queue head))
                  (set! head (+ head 1))
                  (define x (quotient idx n))
                  (define y (remainder idx n))
                  (for ([d dirs])
                    (define nx (+ x (car d)))
                    (define ny (+ y (cdr d)))
                    (when (in-bounds nx ny)
                      (when (and (= (vector-ref (vector-ref g2 nx) ny) 1)
                                 (not (vector-ref (vector-ref visited nx) ny)))
                        (vector-set! (vector-ref visited nx) ny #t)
                        (define nidx (+ (* nx n) ny))
                        (vector-set! queue tail nidx)
                        (set! tail (+ tail 1))
                        (when (= (vector-ref (vector-ref g1 nx) ny) 0)
                          (set! is-sub #f)))))
                  (bfs-loop)))
              (when is-sub
                (set! count (+ count 1))))))))
      count)))
```

## Erlang

```erlang
-module(solution).
-export([count_sub_islands/2]).

-spec count_sub_islands(Grid1 :: [[integer()]], Grid2 :: [[integer()]]) -> integer().
count_sub_islands(Grid1, Grid2) ->
    Rows = length(Grid1),
    Cols = length(hd(Grid1)),
    G1Rows = [list_to_tuple(R) || R <- Grid1],
    G2Rows = [list_to_tuple(R) || R <- Grid2],
    G1 = list_to_tuple(G1Rows),
    G2 = list_to_tuple(G2Rows),
    Vis0 = #{},
    {Count,_} = lists:foldl(
        fun(I, {Cnt,Vis}) ->
            {NewCnt, NewVis} =
                lists:foldl(
                    fun(J,{C,V}) ->
                        case get_cell(G2,I,J) of
                            1 ->
                                case maps:is_key({I,J}, V) of
                                    true -> {C,V};
                                    false ->
                                        {IsSub, V2} = explore_island(I,J,G1,G2,Rows,Cols,V),
                                        C2 = if IsSub -> C+1; true -> C end,
                                        {C2, V2}
                                end;
                            _ -> {C,V}
                        end
                    end,
                    {Cnt,Vis},
                    lists:seq(0, Cols-1)
                ),
            {NewCnt, NewVis}
        end,
        {0, Vis0},
        lists:seq(0, Rows-1)
    ),
    Count.

get_cell(GridRowsTuple, I, J) ->
    Row = element(I+1, GridRowsTuple),
    element(J+1, Row).

explore_island(StartI, StartJ, G1, G2, MaxI, MaxJ, Vis0) ->
    explore_stack([{StartI,StartJ}], G1, G2, MaxI, MaxJ, Vis0, true).

explore_stack([], _G1,_G2,_MaxI,_MaxJ,Vis,Flag) -> {Flag, Vis};
explore_stack([{I,J}|Rest], G1,G2,MaxI,MaxJ,Vis,Flag) ->
    case maps:is_key({I,J}, Vis) of
        true ->
            explore_stack(Rest, G1,G2,MaxI,MaxJ,Vis,Flag);
        false ->
            Cell2 = get_cell(G2,I,J),
            if Cell2 =:= 0 ->
                    Vis1 = maps:put({I,J}, true, Vis),
                    explore_stack(Rest, G1,G2,MaxI,MaxJ,Vis1,Flag);
               true ->
                    Cell1 = get_cell(G1,I,J),
                    NewFlag = Flag andalso (Cell1 =:= 1),
                    Vis1 = maps:put({I,J}, true, Vis),
                    Neigh = neighbors(I,J,MaxI,MaxJ),
                    ValidNeigh = [N || N={X,Y} <- Neigh,
                                       get_cell(G2,X,Y) =:= 1],
                    explore_stack(ValidNeigh ++ Rest, G1,G2,MaxI,MaxJ,Vis1,NewFlag)
            end
    end.

neighbors(I,J, MaxI, MaxJ) ->
    Up = if I > 0 -> [{I-1,J}] else [] end,
    Down = if I+1 < MaxI -> [{I+1,J}] else [] end,
    Left = if J > 0 -> [{I,J-1}] else [] end,
    Right = if J+1 < MaxJ -> [{I,J+1}] else [] end,
    Up ++ Down ++ Left ++ Right.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_sub_islands(grid1 :: [[integer]], grid2 :: [[integer]]) :: integer
  def count_sub_islands(grid1, grid2) do
    m = length(grid1)
    n = length(hd(grid1))

    g1 = build_map(grid1)
    g2 = build_map(grid2)

    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]
    positions = for i <- 0..(m - 1), j <- 0..(n - 1), do: {i, j}

    {count, _} =
      Enum.reduce(positions, {0, MapSet.new()}, fn {i, j}, {cnt, visited} ->
        if Map.get(g2, {i, j}) == 1 and not MapSet.member?(visited, {i, j}) do
          {is_sub, new_visited} = bfs(i, j, g1, g2, visited, dirs, m, n)
          new_cnt = if is_sub, do: cnt + 1, else: cnt
          {new_cnt, new_visited}
        else
          {cnt, visited}
        end
      end)

    count
  end

  defp build_map(grid) do
    Enum.with_index(grid)
    |> Enum.reduce(%{}, fn {row, i}, acc ->
      row
      |> Enum.with_index()
      |> Enum.reduce(acc, fn {val, j}, a -> Map.put(a, {i, j}, val) end)
    end)
  end

  defp bfs(i, j, g1, g2, visited, dirs, m, n) do
    queue = :queue.new() |> :queue.in({i, j})
    visited = MapSet.put(visited, {i, j})
    is_sub = Map.get(g1, {i, j}) == 1

    bfs_loop(queue, g1, g2, visited, dirs, m, n, is_sub)
  end

  defp bfs_loop(queue, g1, g2, visited, dirs, m, n, is_sub) do
    case :queue.out(queue) do
      {:empty, _} ->
        {is_sub, visited}

      {{:value, {x, y}}, q_rest} ->
        {new_is_sub, new_queue, new_visited} =
          Enum.reduce(dirs, {is_sub, q_rest, visited}, fn {dx, dy},
                                                          {cur_sub, q_acc,
                                                           vis_acc} ->
            nx = x + dx
            ny = y + dy

            if nx >= 0 and nx < m and ny >= 0 and ny < n do
              if Map.get(g2, {nx, ny}) == 1 and not MapSet.member?(vis_acc, {nx, ny}) do
                new_vis = MapSet.put(vis_acc, {nx, ny})
                new_q = :queue.in({nx, ny}, q_acc)
                new_sub = cur_sub and (Map.get(g1, {nx, ny}) == 1)
                {new_sub, new_q, new_vis}
              else
                {cur_sub, q_acc, vis_acc}
              end
            else
              {cur_sub, q_acc, vis_acc}
            end
          end)

        bfs_loop(new_queue, g1, g2, new_visited, dirs, m, n, new_is_sub)
    end
  end
end
```

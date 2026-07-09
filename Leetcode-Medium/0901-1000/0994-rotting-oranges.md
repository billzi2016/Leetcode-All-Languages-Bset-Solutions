# 0994. Rotting Oranges

## Cpp

```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        queue<pair<int,int>> q;
        int fresh = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 2) q.emplace(i, j);
                else if (grid[i][j] == 1) ++fresh;
            }
        }
        if (fresh == 0) return 0;
        int minutes = 0;
        const vector<int> dirs = {-1, 0, 1, 0, -1};
        while (!q.empty() && fresh > 0) {
            int sz = q.size();
            ++minutes;
            for (int k = 0; k < sz; ++k) {
                auto [x, y] = q.front(); q.pop();
                for (int d = 0; d < 4; ++d) {
                    int nx = x + dirs[d];
                    int ny = y + dirs[d+1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                        grid[nx][ny] = 2;
                        --fresh;
                        q.emplace(nx, ny);
                    }
                }
            }
        }
        return fresh == 0 ? minutes : -1;
    }
};
```

## Java

```java
class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        java.util.ArrayDeque<int[]> queue = new java.util.ArrayDeque<>();
        int fresh = 0;
        
        // Initialize the queue with all rotten oranges and count fresh ones
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 2) {
                    queue.offer(new int[]{r, c});
                } else if (grid[r][c] == 1) {
                    fresh++;
                }
            }
        }
        
        if (fresh == 0) return 0;
        int minutes = 0;
        int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            boolean rottedThisMinute = false;
            for (int i = 0; i < size; ++i) {
                int[] cell = queue.poll();
                int r = cell[0], c = cell[1];
                for (int[] d : dirs) {
                    int nr = r + d[0];
                    int nc = c + d[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        queue.offer(new int[]{nr, nc});
                        rottedThisMinute = true;
                    }
                }
            }
            if (rottedThisMinute) minutes++;
        }
        
        return fresh == 0 ? minutes : -1;
    }
}
```

## Python

```python
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))

        # If there are no fresh oranges, answer is 0
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, t = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))
                    minutes = t + 1

        return minutes if fresh == 0 else -1
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = -1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
        
        return minutes if fresh == 0 else -1
```

## C

```c
#include <stdlib.h>

int orangesRotting(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0 || gridColSize == NULL) return -1;
    int rows = gridSize;
    int cols = gridColSize[0];
    int total = rows * cols;

    int *qx = (int *)malloc(total * sizeof(int));
    int *qy = (int *)malloc(total * sizeof(int));
    if (!qx || !qy) {
        free(qx);
        free(qy);
        return -1;
    }

    int front = 0, back = 0;
    int fresh = 0;

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 2) {
                qx[back] = i;
                qy[back] = j;
                back++;
            } else if (grid[i][j] == 1) {
                fresh++;
            }
        }
    }

    if (fresh == 0) {
        free(qx);
        free(qy);
        return 0;
    }

    int minutes = 0;
    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    while (front < back && fresh > 0) {
        int curLevelSize = back - front;
        for (int k = 0; k < curLevelSize; ++k) {
            int x = qx[front];
            int y = qy[front];
            front++;
            for (int d = 0; d < 4; ++d) {
                int nx = x + dirs[d][0];
                int ny = y + dirs[d][1];
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 1) {
                    grid[nx][ny] = 2;
                    fresh--;
                    qx[back] = nx;
                    qy[back] = ny;
                    back++;
                }
            }
        }
        minutes++;
    }

    free(qx);
    free(qy);

    return (fresh == 0) ? minutes : -1;
}
```

## Csharp

```csharp
public class Solution {
    public int OrangesRotting(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        var q = new System.Collections.Generic.Queue<(int r, int c, int t)>();
        int fresh = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) q.Enqueue((i, j, 0));
                else if (grid[i][j] == 1) fresh++;
            }
        }

        int minutes = 0;
        int[][] dirs = new int[][] {
            new int[] {1, 0},
            new int[] {-1, 0},
            new int[] {0, 1},
            new int[] {0, -1}
        };

        while (q.Count > 0) {
            var (r, c, t) = q.Dequeue();
            minutes = Math.Max(minutes, t);
            foreach (var d in dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    fresh--;
                    q.Enqueue((nr, nc, t + 1));
                }
            }
        }

        return fresh == 0 ? minutes : -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const queue = [];
    let fresh = 0;
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 2) {
                queue.push([i, j]);
            } else if (grid[i][j] === 1) {
                fresh++;
            }
        }
    }
    
    if (fresh === 0) return 0;
    
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let minutes = 0;
    let qIndex = 0;
    
    while (qIndex < queue.length && fresh > 0) {
        const currentLevelSize = queue.length - qIndex;
        for (let k = 0; k < currentLevelSize; ++k) {
            const [x, y] = queue[qIndex++];
            for (const [dx, dy] of dirs) {
                const nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] === 1) {
                    grid[nx][ny] = 2;
                    fresh--;
                    queue.push([nx, ny]);
                }
            }
        }
        minutes++;
    }
    
    return fresh === 0 ? minutes : -1;
};
```

## Typescript

```typescript
function orangesRotting(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const queue: [number, number, number][] = [];
    let fresh = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 2) {
                queue.push([i, j, 0]);
            } else if (grid[i][j] === 1) {
                fresh++;
            }
        }
    }

    let minutes = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let idx = 0;

    while (idx < queue.length) {
        const [r, c, t] = queue[idx++];
        minutes = Math.max(minutes, t);
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === 1) {
                grid[nr][nc] = 2;
                fresh--;
                queue.push([nr, nc, t + 1]);
            }
        }
    }

    return fresh === 0 ? minutes : -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function orangesRotting($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $queue = new SplQueue();
        $fresh = 0;

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($grid[$i][$j] === 2) {
                    $queue->enqueue([$i, $j]);
                } elseif ($grid[$i][$j] === 1) {
                    $fresh++;
                }
            }
        }

        if ($fresh === 0) {
            return 0;
        }

        $minutes = 0;
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            $rottedThisLevel = false;

            for ($k = 0; $k < $size; $k++) {
                [$x, $y] = $queue->dequeue();

                foreach ($dirs as $d) {
                    $nx = $x + $d[0];
                    $ny = $y + $d[1];

                    if ($nx >= 0 && $nx < $rows && $ny >= 0 && $ny < $cols && $grid[$nx][$ny] === 1) {
                        $grid[$nx][$ny] = 2;
                        $fresh--;
                        $queue->enqueue([$nx, $ny]);
                        $rottedThisLevel = true;
                    }
                }
            }

            if ($rottedThisLevel) {
                $minutes++;
            }
        }

        return $fresh === 0 ? $minutes : -1;
    }
}
```

## Swift

```swift
class Solution {
    func orangesRotting(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var fresh = 0
        var queue: [(Int, Int, Int)] = [] // row, col, time
        var mutableGrid = grid
        
        for i in 0..<m {
            for j in 0..<n {
                if mutableGrid[i][j] == 1 {
                    fresh += 1
                } else if mutableGrid[i][j] == 2 {
                    queue.append((i, j, 0))
                }
            }
        }
        
        var minutes = 0
        let directions = [(1,0), (-1,0), (0,1), (0,-1)]
        var index = 0
        
        while index < queue.count {
            let (x, y, time) = queue[index]
            index += 1
            minutes = max(minutes, time)
            
            for dir in directions {
                let nx = x + dir.0
                let ny = y + dir.1
                if nx >= 0 && nx < m && ny >= 0 && ny < n && mutableGrid[nx][ny] == 1 {
                    mutableGrid[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx, ny, time + 1))
                }
            }
        }
        
        return fresh == 0 ? minutes : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun orangesRotting(grid: Array<IntArray>): Int {
        val rows = grid.size
        val cols = grid[0].size
        val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        var fresh = 0

        for (i in 0 until rows) {
            for (j in 0 until cols) {
                when (grid[i][j]) {
                    2 -> queue.add(Pair(i, j))
                    1 -> fresh++
                }
            }
        }

        if (fresh == 0) return 0

        var minutes = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

        while (queue.isNotEmpty() && fresh > 0) {
            val size = queue.size
            repeat(size) {
                val (r, c) = queue.removeFirst()
                for (d in dirs) {
                    val nr = r + d[0]
                    val nc = c + d[1]
                    if (nr in 0 until rows && nc in 0 until cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2
                        fresh--
                        queue.add(Pair(nr, nc))
                    }
                }
            }
            minutes++
        }

        return if (fresh == 0) minutes else -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int orangesRotting(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    Queue<List<int>> q = Queue();
    int fresh = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 2) {
          q.add([i, j]);
        } else if (grid[i][j] == 1) {
          fresh++;
        }
      }
    }

    int minutes = 0;
    const List<List<int>> dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1]
    ];

    while (q.isNotEmpty && fresh > 0) {
      int size = q.length;
      for (int i = 0; i < size; i++) {
        var cur = q.removeFirst();
        int r = cur[0];
        int c = cur[1];
        for (var d in dirs) {
          int nr = r + d[0];
          int nc = c + d[1];
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
            grid[nr][nc] = 2;
            fresh--;
            q.add([nr, nc]);
          }
        }
      }
      minutes++;
    }

    return fresh == 0 ? minutes : -1;
  }
}
```

## Golang

```go
func orangesRotting(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])
    type point struct{ r, c int }
    queue := []point{}
    fresh := 0

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 2 {
                queue = append(queue, point{i, j})
            } else if grid[i][j] == 1 {
                fresh++
            }
        }
    }

    if fresh == 0 {
        return 0
    }

    minutes := -1
    dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i < size; i++ {
            cur := queue[0]
            queue = queue[1:]
            for _, d := range dirs {
                nr, nc := cur.r+d[0], cur.c+d[1]
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1 {
                    grid[nr][nc] = 2
                    fresh--
                    queue = append(queue, point{nr, nc})
                }
            }
        }
        minutes++
    }

    if fresh > 0 {
        return -1
    }
    if minutes < 0 {
        minutes = 0
    }
    return minutes
}
```

## Ruby

```ruby
def oranges_rotting(grid)
  rows = grid.size
  cols = grid[0].size
  queue = []
  head = 0
  fresh = 0

  rows.times do |i|
    cols.times do |j|
      case grid[i][j]
      when 2
        queue << [i, j, 0]
      when 1
        fresh += 1
      end
    end
  end

  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  minutes = 0

  while head < queue.size
    i, j, t = queue[head]
    head += 1
    minutes = t
    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      next unless ni.between?(0, rows - 1) && nj.between?(0, cols - 1)
      if grid[ni][nj] == 1
        grid[ni][nj] = 2
        fresh -= 1
        queue << [ni, nj, t + 1]
      end
    end
  end

  fresh.zero? ? minutes : -1
end
```

## Scala

```scala
object Solution {
    def orangesRotting(grid: Array[Array[Int]]): Int = {
        val rows = grid.length
        val cols = grid(0).length
        val q = scala.collection.mutable.Queue[(Int, Int)]()
        var fresh = 0

        for (i <- 0 until rows; j <- 0 until cols) {
            grid(i)(j) match {
                case 2 => q.enqueue((i, j))
                case 1 => fresh += 1
                case _ =>
            }
        }

        if (fresh == 0) return 0

        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
        var minutes = 0

        while (q.nonEmpty) {
            val size = q.size
            var rottedThisRound = false
            for (_ <- 0 until size) {
                val (x, y) = q.dequeue()
                for ((dx, dy) <- dirs) {
                    val nx = x + dx
                    val ny = y + dy
                    if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid(nx)(ny) == 1) {
                        grid(nx)(ny) = 2
                        fresh -= 1
                        q.enqueue((nx, ny))
                        rottedThisRound = true
                    }
                }
            }
            if (rottedThisRound) minutes += 1
        }

        if (fresh > 0) -1 else minutes
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
        let mut grid = grid;
        let rows = grid.len();
        if rows == 0 {
            return 0;
        }
        let cols = grid[0].len();

        let mut fresh = 0i32;
        let mut q: VecDeque<(usize, usize)> = VecDeque::new();

        for r in 0..rows {
            for c in 0..cols {
                match grid[r][c] {
                    1 => fresh += 1,
                    2 => q.push_back((r, c)),
                    _ => {}
                }
            }
        }

        if fresh == 0 {
            return 0;
        }

        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        let mut minutes = -1i32;

        while !q.is_empty() {
            let level_size = q.len();
            for _ in 0..level_size {
                if let Some((r, c)) = q.pop_front() {
                    for &(dr, dc) in &dirs {
                        let nr = r as i32 + dr;
                        let nc = c as i32 + dc;
                        if nr >= 0 && nr < rows as i32 && nc >= 0 && nc < cols as i32 {
                            let (nr_usize, nc_usize) = (nr as usize, nc as usize);
                            if grid[nr_usize][nc_usize] == 1 {
                                grid[nr_usize][nc_usize] = 2;
                                fresh -= 1;
                                q.push_back((nr_usize, nc_usize));
                            }
                        }
                    }
                }
            }
            minutes += 1;
        }

        if fresh > 0 { -1 } else { minutes }
    }
}
```

## Racket

```racket
(define/contract (oranges-rotting grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (= rows 0) 0 (length (first grid))))
         (gridv (list->vector (map list->vector grid)))
         ;; collect initial rotten oranges
         (init-queue
          (let loop ((i 0) (acc '()))
            (if (= i rows)
                acc
                (loop (+ i 1)
                      (let inner ((j 0) (a acc))
                        (if (= j cols)
                            a
                            (inner (+ j 1)
                                   (if (= (vector-ref (vector-ref gridv i) j) 2)
                                       (cons (cons i j) a)
                                       a))))))))
         ;; count fresh oranges
         (fresh-count
          (let loop ((i 0) (cnt 0))
            (if (= i rows)
                cnt
                (loop (+ i 1)
                      (let inner ((j 0) (c cnt))
                        (if (= j cols)
                            c
                            (inner (+ j 1)
                                   (if (= (vector-ref (vector-ref gridv i) j) 1)
                                       (+ c 1)
                                       c)))))))))
    (if (= fresh-count 0)
        0
        (let bfs ((queue init-queue) (minutes -1) (fresh fresh-count))
          (if (null? queue)
              (if (= fresh 0) minutes -1)
              (let loop-queue ((qs queue) (next '()) (f fresh))
                (if (null? qs)
                    (bfs (reverse next) (+ minutes 1) f)
                    (let* ((pos (car qs))
                           (i (car pos))
                           (j (cdr pos)))
                      (for ([d '((-1 . 0) (1 . 0) (0 . -1) (0 . 1))])
                        (define ni (+ i (car d)))
                        (define nj (+ j (cdr d)))
                        (when (and (>= ni 0) (< ni rows)
                                   (>= nj 0) (< nj cols)
                                   (= (vector-ref (vector-ref gridv ni) nj) 1))
                          (vector-set! (vector-ref gridv ni) nj 2)
                          (set! f (- f 1))
                          (set! next (cons (cons ni nj) next))))
                      (loop-queue (cdr qs) next f)))))))))
```

## Erlang

```erlang
-module(solution).
-export([oranges_rotting/1]).

-spec oranges_rotting(Grid :: [[integer()]]) -> integer().
oranges_rotting(Grid) ->
    {Map, Queue0, Fresh} = build_grid(Grid, 0, #{}, [], 0),
    case Fresh of
        0 -> 0;
        _ -> bfs_loop(Map, lists:reverse(Queue0), Fresh, 0)
    end.

build_grid([], _, Map, QAcc, Fresh) ->
    {Map, QAcc, Fresh};
build_grid([Row|Rows], RIdx, Map, QAcc, Fresh) ->
    {NewMap, NewQAcc, NewFresh} = build_row(Row, RIdx, 0, Map, QAcc, Fresh),
    build_grid(Rows, RIdx + 1, NewMap, NewQAcc, NewFresh).

build_row([], _, _, Map, QAcc, Fresh) ->
    {Map, QAcc, Fresh};
build_row([V|Vs], R, C, Map, QAcc, Fresh) ->
    Key = {R, C},
    Map1 = maps:put(Key, V, Map),
    case V of
        2 -> build_row(Vs, R, C + 1, Map1, [Key | QAcc], Fresh);
        1 -> build_row(Vs, R, C + 1, Map1, QAcc, Fresh + 1);
        _ -> build_row(Vs, R, C + 1, Map1, QAcc, Fresh)
    end.

bfs_loop(_, [], Fresh, Minutes) ->
    case Fresh of
        0 -> Minutes;
        _ -> -1
    end;
bfs_loop(Map, Queue, Fresh, Minutes) when Fresh =:= 0 ->
    Minutes;
bfs_loop(Map, Queue, Fresh, Minutes) ->
    {NewMap, NewQueue, NewFresh} = bfs_level(Map, Queue, [], Fresh),
    bfs_loop(NewMap, NewQueue, NewFresh, Minutes + 1).

bfs_level(Map, [], AccQ, Fresh) ->
    {Map, lists:reverse(AccQ), Fresh};
bfs_level(Map, [Pos | Rest], AccQ, Fresh) ->
    {M1, Q1, F1} = process_neighbors(Pos, Map, AccQ, Fresh),
    bfs_level(M1, Rest, Q1, F1).

process_neighbors({R, C}, Map, AccQ, Fresh) ->
    Directions = [{-1,0},{1,0},{0,-1},{0,1}],
    lists:foldl(fun({DR, DC}, {M, Q, F}) ->
        NR = R + DR,
        NC = C + DC,
        Key = {NR, NC},
        case maps:get(Key, M, 0) of
            1 -> {maps:put(Key, 2, M), [Key | Q], F - 1};
            _ -> {M, Q, F}
        end
    end, {Map, AccQ, Fresh}, Directions).
```

## Elixir

```elixir
defmodule Solution do
  @spec oranges_rotting(grid :: [[integer]]) :: integer
  def oranges_rotting(grid) do
    rows = length(grid)
    cols = length(List.first(grid))

    # Build map of positions to values
    pos_map =
      for r <- 0..rows - 1, c <- 0..cols - 1, into: %{} do
        val = grid |> Enum.at(r) |> Enum.at(c)
        {{r, c}, val}
      end

    fresh_count = Enum.count(pos_map, fn {_k, v} -> v == 1 end)

    if fresh_count == 0 do
      0
    else
      # Initialize queue with all rotten oranges at time 0
      init_queue =
        Enum.reduce(pos_map, :queue.new(), fn
          ({{r, c}, 2}, q) -> :queue.in({r, c, 0}, q)
          (_, q) -> q
        end)

      {remaining_fresh, minutes} = bfs(init_queue, pos_map, fresh_count, 0)

      if remaining_fresh == 0, do: minutes, else: -1
    end
  end

  defp bfs(queue, map, fresh, max_time) do
    case :queue.out(queue) do
      {:empty, _} ->
        {fresh, max_time}

      {{:value, {r, c, time}}, q2} ->
        dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

        {q3, map2, fresh2, max_t2} =
          Enum.reduce(dirs, {q2, map, fresh, max_time}, fn {dr, dc},
                                                          {q_acc, m_acc, f_acc,
                                                           t_acc} ->
            nr = r + dr
            nc = c + dc

            case Map.get(m_acc, {nr, nc}) do
              1 ->
                m_new = Map.put(m_acc, {nr, nc}, 2)
                q_new = :queue.in({nr, nc, time + 1}, q_acc)
                {q_new, m_new, f_acc - 1, max(t_acc, time + 1)}

              _ ->
                {q_acc, m_acc, f_acc, t_acc}
            end
          end)

        bfs(q3, map2, fresh2, max_t2)
    end
  end
end
```

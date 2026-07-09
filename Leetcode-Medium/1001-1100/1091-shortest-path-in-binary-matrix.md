# 1091. Shortest Path in Binary Matrix

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] != 0 || grid[n-1][n-1] != 0) return -1;
        const int dirs[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        vector<vector<int>> dist(n, vector<int>(n, 0));
        queue<pair<int,int>> q;
        q.emplace(0,0);
        dist[0][0] = 1;
        while (!q.empty()) {
            auto [x,y] = q.front(); q.pop();
            if (x == n-1 && y == n-1) return dist[x][y];
            for (auto &d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                if (grid[nx][ny] != 0 || dist[nx][ny]) continue;
                dist[nx][ny] = dist[x][y] + 1;
                q.emplace(nx, ny);
            }
        }
        return -1;
    }
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        if (n == 1) return 1;

        int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};

        boolean[][] visited = new boolean[n][n];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0, 1}); // row, col, distance
        visited[0][0] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1], dist = cur[2];
            if (r == n - 1 && c == n - 1) return dist;
            for (int k = 0; k < 8; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n &&
                    !visited[nr][nc] && grid[nr][nc] == 0) {
                    visited[nr][nc] = true;
                    q.offer(new int[]{nr, nc, dist + 1});
                }
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        q = deque()
        q.append((0, 0, 1))  # row, col, path length
        grid[0][0] = 1  # mark visited

        while q:
            r, c, dist = q.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, dist + 1))

        return -1
```

## Python3

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        from collections import deque
        q = deque()
        q.append((0, 0, 1))
        grid[0][0] = 1
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]
        while q:
            i, j, d = q.popleft()
            if i == n - 1 and j == n - 1:
                return d
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    q.append((ni, nj, d + 1))
        return -1
```

## C

```c
#include <stdlib.h>
#include <string.h>

int shortestPathBinaryMatrix(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;

    const int dirs[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    char visited[101][101];
    memset(visited, 0, sizeof(visited));

    int maxCells = n * n;
    int *qx = (int *)malloc(maxCells * sizeof(int));
    int *qy = (int *)malloc(maxCells * sizeof(int));
    int *qd = (int *)malloc(maxCells * sizeof(int));
    if (!qx || !qy || !qd) {
        free(qx); free(qy); free(qd);
        return -1;
    }

    int front = 0, rear = 0;
    qx[rear] = 0; qy[rear] = 0; qd[rear] = 1; rear++;
    visited[0][0] = 1;

    while (front < rear) {
        int x = qx[front];
        int y = qy[front];
        int d = qd[front];
        front++;

        if (x == n - 1 && y == n - 1) {
            free(qx); free(qy); free(qd);
            return d;
        }

        for (int k = 0; k < 8; ++k) {
            int nx = x + dirs[k][0];
            int ny = y + dirs[k][1];
            if (nx >= 0 && nx < n && ny >= 0 && ny < n &&
                !visited[nx][ny] && grid[nx][ny] == 0) {
                visited[nx][ny] = 1;
                qx[rear] = nx;
                qy[rear] = ny;
                qd[rear] = d + 1;
                rear++;
            }
        }
    }

    free(qx); free(qy); free(qd);
    return -1;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int ShortestPathBinaryMatrix(int[][] grid) {
        int n = grid.Length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        if (n == 1) return 1;

        int[] dr = { -1, -1, -1, 0, 0, 1, 1, 1 };
        int[] dc = { -1, 0, 1, -1, 1, -1, 0, 1 };

        var visited = new bool[n, n];
        var q = new Queue<(int r, int c)>();
        q.Enqueue((0, 0));
        visited[0, 0] = true;
        int pathLen = 1;

        while (q.Count > 0) {
            int size = q.Count;
            for (int i = 0; i < size; i++) {
                var (r, c) = q.Dequeue();
                if (r == n - 1 && c == n - 1) return pathLen;

                for (int d = 0; d < 8; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n &&
                        !visited[nr, nc] && grid[nr][nc] == 0) {
                        visited[nr, nc] = true;
                        q.Enqueue((nr, nc));
                    }
                }
            }
            pathLen++;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {
    const n = grid.length;
    if (grid[0][0] !== 0 || grid[n - 1][n - 1] !== 0) return -1;
    if (n === 1) return 1;

    const dirs = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];

    let queue = [[0, 0]];
    let head = 0;
    grid[0][0] = 1; // mark visited
    let steps = 1;

    while (head < queue.length) {
        const levelSize = queue.length - head;
        for (let i = 0; i < levelSize; i++) {
            const [x, y] = queue[head++];
            if (x === n - 1 && y === n - 1) return steps;

            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (
                    nx >= 0 && nx < n &&
                    ny >= 0 && ny < n &&
                    grid[nx][ny] === 0
                ) {
                    grid[nx][ny] = 1; // mark visited
                    queue.push([nx, ny]);
                }
            }
        }
        steps++;
    }

    return -1;
};
```

## Typescript

```typescript
function shortestPathBinaryMatrix(grid: number[][]): number {
    const n = grid.length;
    if (grid[0][0] === 1 || grid[n - 1][n - 1] === 1) return -1;

    const dirs = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ] as const;

    const visited: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    const queue: [number, number, number][] = [];
    queue.push([0, 0, 1]);
    visited[0][0] = true;
    let idx = 0;

    while (idx < queue.length) {
        const [r, c, d] = queue[idx++];
        if (r === n - 1 && c === n - 1) return d;

        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (
                nr >= 0 && nr < n &&
                nc >= 0 && nc < n &&
                !visited[nr][nc] &&
                grid[nr][nc] === 0
            ) {
                visited[nr][nc] = true;
                queue.push([nr, nc, d + 1]);
            }
        }
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function shortestPathBinaryMatrix($grid) {
        $n = count($grid);
        if ($grid[0][0] == 1 || $grid[$n - 1][$n - 1] == 1) {
            return -1;
        }

        $directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],           [0, 1],
            [1, -1],  [1, 0],  [1, 1]
        ];

        $queue = new SplQueue();
        $queue->enqueue([0, 0, 1]); // row, col, distance
        $grid[0][0] = 1; // mark visited

        while (!$queue->isEmpty()) {
            [$r, $c, $dist] = $queue->dequeue();

            if ($r == $n - 1 && $c == $n - 1) {
                return $dist;
            }

            foreach ($directions as $dir) {
                $nr = $r + $dir[0];
                $nc = $c + $dir[1];

                if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n && $grid[$nr][$nc] == 0) {
                    $queue->enqueue([$nr, $nc, $dist + 1]);
                    $grid[$nr][$nc] = 1; // mark visited
                }
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func shortestPathBinaryMatrix(_ grid: [[Int]]) -> Int {
        let n = grid.count
        if grid[0][0] == 1 || grid[n - 1][n - 1] == 1 { return -1 }
        if n == 1 { return 1 }
        
        var g = grid
        var queue: [(Int, Int)] = [(0, 0)]
        var head = 0
        g[0][0] = 1
        
        let dirs = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1),  (1, 0), (1, 1)]
        
        var steps = 1
        while head < queue.count {
            let currentLevelCount = queue.count - head
            for _ in 0..<currentLevelCount {
                let (x, y) = queue[head]
                head += 1
                if x == n - 1 && y == n - 1 { return steps }
                
                for d in dirs {
                    let nx = x + d.0
                    let ny = y + d.1
                    if nx >= 0 && nx < n && ny >= 0 && ny < n && g[nx][ny] == 0 {
                        queue.append((nx, ny))
                        g[nx][ny] = 1
                    }
                }
            }
            steps += 1
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
        val n = grid.size
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1
        if (n == 1) return 1

        val dirs = arrayOf(
            intArrayOf(-1, -1), intArrayOf(-1, 0), intArrayOf(-1, 1),
            intArrayOf(0, -1),                 intArrayOf(0, 1),
            intArrayOf(1, -1), intArrayOf(1, 0), intArrayOf(1, 1)
        )

        val visited = Array(n) { IntArray(n) }
        val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        queue.add(Pair(0, 0))
        visited[0][0] = 1

        while (queue.isNotEmpty()) {
            val (r, c) = queue.removeFirst()
            val dist = visited[r][c]
            for (d in dirs) {
                val nr = r + d[0]
                val nc = c + d[1]
                if (nr !in 0 until n || nc !in 0 until n) continue
                if (grid[nr][nc] == 1 || visited[nr][nc] != 0) continue
                visited[nr][nc] = dist + 1
                if (nr == n - 1 && nc == n - 1) return dist + 1
                queue.add(Pair(nr, nc))
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
  int shortestPathBinaryMatrix(List<List<int>> grid) {
    int n = grid.length;
    if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
    const dirs = [
      [-1, -1],
      [-1, 0],
      [-1, 1],
      [0, -1],
      [0, 1],
      [1, -1],
      [1, 0],
      [1, 1]
    ];
    Queue<List<int>> q = Queue();
    q.add([0, 0]);
    List<List<int>> dist = List.generate(n, (_) => List.filled(n, 0));
    dist[0][0] = 1;
    while (q.isNotEmpty) {
      var cur = q.removeFirst();
      int x = cur[0], y = cur[1];
      if (x == n - 1 && y == n - 1) return dist[x][y];
      for (var d in dirs) {
        int nx = x + d[0];
        int ny = y + d[1];
        if (nx >= 0 &&
            nx < n &&
            ny >= 0 &&
            ny < n &&
            grid[nx][ny] == 0 &&
            dist[nx][ny] == 0) {
          dist[nx][ny] = dist[x][y] + 1;
          q.add([nx, ny]);
        }
      }
    }
    return -1;
  }
}
```

## Golang

```go
func shortestPathBinaryMatrix(grid [][]int) int {
    n := len(grid)
    if n == 0 {
        return -1
    }
    if grid[0][0] != 0 || grid[n-1][n-1] != 0 {
        return -1
    }
    if n == 1 {
        return 1
    }

    dirs := [8][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}
    type point struct{ x, y int }
    queue := make([]point, 0, n*n)
    queue = append(queue, point{0, 0})
    grid[0][0] = 1 // mark visited

    steps := 1
    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i < size; i++ {
            cur := queue[0]
            queue = queue[1:]
            if cur.x == n-1 && cur.y == n-1 {
                return steps
            }
            for _, d := range dirs {
                nx, ny := cur.x+d[0], cur.y+d[1]
                if nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] == 0 {
                    grid[nx][ny] = 1 // visited
                    queue = append(queue, point{nx, ny})
                }
            }
        }
        steps++
    }
    return -1
}
```

## Ruby

```ruby
def shortest_path_binary_matrix(grid)
  n = grid.size
  return -1 if grid[0][0] == 1 || grid[n - 1][n - 1] == 1

  dirs = [-1, 0, 1].product([-1, 0, 1]) - [[0, 0]]
  queue = [[0, 0, 1]]
  grid[0][0] = 1
  front = 0

  while front < queue.size
    x, y, d = queue[front]
    front += 1
    return d if x == n - 1 && y == n - 1

    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      next unless nx.between?(0, n - 1) && ny.between?(0, n - 1)
      next if grid[nx][ny] != 0
      grid[nx][ny] = 1
      queue << [nx, ny, d + 1]
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
  def shortestPathBinaryMatrix(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    if (grid(0)(0) != 0 || grid(n - 1)(n - 1) != 0) return -1
    if (n == 1) return 1

    case class Node(x: Int, y: Int, d: Int)

    val dirs = Array((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    val visited = Array.ofDim[Boolean](n, n)
    val q = new java.util.ArrayDeque[Node]()
    q.add(Node(0, 0, 1))
    visited(0)(0) = true

    while (!q.isEmpty) {
      val cur = q.poll()
      for ((dx, dy) <- dirs) {
        val nx = cur.x + dx
        val ny = cur.y + dy
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited(nx)(ny) && grid(nx)(ny) == 0) {
          if (nx == n - 1 && ny == n - 1) return cur.d + 1
          visited(nx)(ny) = true
          q.add(Node(nx, ny, cur.d + 1))
        }
      }
    }
    -1
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

pub struct Solution;

impl Solution {
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 0 {
            return -1;
        }
        let mut g = grid;
        if g[0][0] != 0 || g[n - 1][n - 1] != 0 {
            return -1;
        }
        if n == 1 {
            return 1;
        }

        let dirs = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ];

        let mut q: VecDeque<(usize, usize, i32)> = VecDeque::new();
        q.push_back((0, 0, 1));
        g[0][0] = 1; // mark visited

        while let Some((x, y, d)) = q.pop_front() {
            for (dx, dy) in dirs.iter() {
                let nx = x as isize + dx;
                let ny = y as isize + dy;
                if nx >= 0 && nx < n as isize && ny >= 0 && ny < n as isize {
                    let ux = nx as usize;
                    let uy = ny as usize;
                    if g[ux][uy] == 0 {
                        if ux == n - 1 && uy == n - 1 {
                            return d + 1;
                        }
                        q.push_back((ux, uy, d + 1));
                        g[ux][uy] = 1; // mark visited
                    }
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
#lang racket
(require racket/queue)

(define/contract (shortest-path-binary-matrix grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid)))
    (if (or (= (list-ref (list-ref grid 0) 0) 1)
            (= (list-ref (list-ref grid (- n 1)) (- n 1)) 1))
        -1
        (if (= n 1)
            1
            (let* ((dirs (list (vector -1 -1) (vector -1 0) (vector -1 1)
                               (vector 0 -1) (vector 0 1)
                               (vector 1 -1) (vector 1 0) (vector 1 1)))
                   (visited (for/vector ([i (in-range n)]) (make-vector n #f)))
                   (q (make-queue)))
              (vector-set! (vector-ref visited 0) 0 #t)
              (enqueue! q (vector 0 0 1))
              (let loop ()
                (if (queue-empty? q)
                    -1
                    (let* ((item (dequeue! q))
                           (x (vector-ref item 0))
                           (y (vector-ref item 1))
                           (dist (vector-ref item 2)))
                      (if (and (= x (- n 1)) (= y (- n 1)))
                          dist
                          (begin
                            (for ([d dirs])
                              (define nx (+ x (vector-ref d 0)))
                              (define ny (+ y (vector-ref d 1)))
                              (when (and (>= nx 0) (< nx n)
                                         (>= ny 0) (< ny n)
                                         (= (list-ref (list-ref grid nx) ny) 0)
                                         (not (vector-ref (vector-ref visited nx) ny)))
                                (vector-set! (vector-ref visited nx) ny #t)
                                (enqueue! q (vector nx ny (+ dist 1)))))
                            (loop)))))))))))))
```

## Erlang

```erlang
-module(solution).
-export([shortest_path_binary_matrix/1]).

-spec shortest_path_binary_matrix(Grid :: [[integer()]]) -> integer().
shortest_path_binary_matrix(Grid) ->
    N = length(Grid),
    case {cell(Grid, 0, 0), cell(Grid, N-1, N-1)} of
        {0, 0} -> bfs(Grid, N, queue:in({0, 0, 1}, queue:new()), #{ {0,0} => true });
        _      -> -1
    end.

%% BFS loop
bfs(_Grid, N, Queue, Visited) ->
    case queue:out(Queue) of
        {empty, _} ->
            -1;
        {{value, {X, Y, Dist}}, QRest} ->
            if X =:= N-1, Y =:= N-1 ->
                    Dist;
               true ->
                    {NewQ, NewVis} = explore_neighbors(_Grid, N, X, Y, Dist, QRest, Visited),
                    bfs(_Grid, N, NewQ, NewVis)
            end
    end.

%% Explore all 8 directions from (X,Y)
explore_neighbors(Grid, N, X, Y, Dist, Queue, Visited) ->
    Directions = [{-1,-1},{-1,0},{-1,1},
                  {0,-1},        {0,1},
                  {1,-1},{1,0},{1,1}],
    lists:foldl(fun({DX,DY}, {QAcc,VAcc}) ->
                        NX = X + DX,
                        NY = Y + DY,
                        case (NX >= 0 andalso NX < N andalso NY >= 0 andalso NY < N) of
                            true ->
                                case cell(Grid, NX, NY) of
                                    0 ->
                                        Key = {NX,NY},
                                        case maps:is_key(Key, VAcc) of
                                            false ->
                                                Q1 = queue:in({NX,NY,Dist+1}, QAcc),
                                                {Q1, maps:put(Key, true, VAcc)};
                                            true ->
                                                {QAcc, VAcc}
                                        end;
                                    _ -> {QAcc, VAcc}
                                end;
                            false -> {QAcc, VAcc}
                        end
                end, {Queue, Visited}, Directions).

%% Retrieve cell value; assumes coordinates are valid.
cell(Grid, X, Y) ->
    Row = lists:nth(Y + 1, Grid),
    lists:nth(X + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_path_binary_matrix(grid :: [[integer]]) :: integer
  def shortest_path_binary_matrix(grid) do
    n = length(grid)

    # If start or end is blocked, no path exists
    if get_cell(grid, 0, 0) == 1 or get_cell(grid, n - 1, n - 1) == 1 do
      -1
    else
      dirs = [
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1},           {0, 1},
        {1, -1},  {1, 0},  {1, 1}
      ]

      queue = :queue.new() |> :queue.in({0, 0, 1})
      visited = MapSet.new([{0, 0}])

      bfs(queue, visited, grid, n, dirs)
    end
  end

  defp bfs(queue, visited, grid, n, dirs) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {r, c, d}}, q_rest} ->
        if r == n - 1 and c == n - 1 do
          d
        else
          {new_queue, new_visited} =
            Enum.reduce(dirs, {q_rest, visited}, fn {dr, dc}, {q_acc, v_acc} ->
              nr = r + dr
              nc = c + dc

              if nr in 0..(n - 1) and nc in 0..(n - 1) do
                if get_cell(grid, nr, nc) == 0 and not MapSet.member?(v_acc, {nr, nc}) do
                  {
                    :queue.in({nr, nc, d + 1}, q_acc),
                    MapSet.put(v_acc, {nr, nc})
                  }
                else
                  {q_acc, v_acc}
                end
              else
                {q_acc, v_acc}
              end
            end)

          bfs(new_queue, new_visited, grid, n, dirs)
        end
    end
  end

  defp get_cell(grid, r, c) do
    grid |> Enum.at(r) |> Enum.at(c)
  end
end
```

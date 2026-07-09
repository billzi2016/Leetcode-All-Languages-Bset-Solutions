# 1162. As Far from Land as Possible

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size();
        queue<pair<int,int>> q;
        vector<vector<int>> dist(n, vector<int>(n, -1));
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    q.emplace(i, j);
                    dist[i][j] = 0;
                }
            }
        }
        
        if (q.empty()) return -1; // no land
        int maxDist = -1;
        const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
        
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            for (auto &d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if (dist[nx][ny] != -1) continue; // already visited
                dist[nx][ny] = dist[x][y] + 1;
                maxDist = max(maxDist, dist[nx][ny]);
                q.emplace(nx, ny);
            }
        }
        
        return maxDist == 0 ? -1 : maxDist;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxDistance(int[][] grid) {
        int n = grid.length;
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], -1);
        Deque<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0;
                    q.offer(new int[]{i, j});
                }
            }
        }
        if (q.isEmpty() || q.size() == n * n) return -1;
        int max = -1;
        int[] dirs = {-1, 0, 1, 0, -1};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            for (int d = 0; d < 4; d++) {
                int nx = x + dirs[d];
                int ny = y + dirs[d + 1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] == -1) {
                    dist[nx][ny] = dist[x][y] + 1;
                    max = Math.max(max, dist[nx][ny]);
                    q.offer(new int[]{nx, ny});
                }
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(grid)
        q = deque()
        # enqueue all land cells
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        # if no land or all land, return -1
        if not q or len(q) == n * n:
            return -1

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        max_dist = -1

        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    grid[ni][nj] = grid[i][j] + 1
                    max_dist = grid[ni][nj] - 1
                    q.append((ni, nj))

        return max_dist
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        # Initialize queue with all land cells
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        # If there is no land or the whole grid is land, return -1
        if not q or len(q) == n * n:
            return -1
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        max_dist = 0
        
        while q:
            i, j = q.popleft()
            cur = dist[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == -1:
                    dist[ni][nj] = cur + 1
                    max_dist = max(max_dist, cur + 1)
                    q.append((ni, nj))
        
        return max_dist if max_dist > 0 else -1
```

## C

```c
int maxDistance(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    if (n == 0) return -1;
    int total = n * n;
    int *dist = (int *)malloc(total * sizeof(int));
    for (int i = 0; i < total; ++i) dist[i] = -1;

    int *queue = (int *)malloc(total * sizeof(int));
    int front = 0, rear = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < gridColSize[i]; ++j) {
            if (grid[i][j] == 1) {
                int idx = i * n + j;
                dist[idx] = 0;
                queue[rear++] = idx;
            }
        }
    }

    if (front == rear) { // no land cells
        free(dist);
        free(queue);
        return -1;
    }

    int maxDist = 0;
    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    while (front < rear) {
        int idx = queue[front++];
        int r = idx / n;
        int c = idx % n;
        for (int d = 0; d < 4; ++d) {
            int nr = r + dirs[d][0];
            int nc = c + dirs[d][1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                int nIdx = nr * n + nc;
                if (dist[nIdx] == -1) {
                    dist[nIdx] = dist[idx] + 1;
                    if (dist[nIdx] > maxDist) maxDist = dist[nIdx];
                    queue[rear++] = nIdx;
                }
            }
        }
    }

    free(dist);
    free(queue);
    return maxDist == 0 ? -1 : maxDist;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxDistance(int[][] grid)
    {
        int n = grid.Length;
        var queue = new System.Collections.Generic.Queue<(int r, int c)>();
        int[][] dist = new int[n][];
        for (int i = 0; i < n; i++)
        {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++)
                dist[i][j] = -1;
        }

        // Initialize queue with all land cells
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 1)
                {
                    queue.Enqueue((i, j));
                    dist[i][j] = 0;
                }
            }
        }

        // If there is no land or no water, return -1
        if (queue.Count == 0 || queue.Count == n * n)
            return -1;

        int maxDist = -1;
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (queue.Count > 0)
        {
            var (r, c) = queue.Dequeue();
            for (int k = 0; k < 4; k++)
            {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1)
                {
                    dist[nr][nc] = dist[r][c] + 1;
                    maxDist = System.Math.Max(maxDist, dist[nr][nc]);
                    queue.Enqueue((nr, nc));
                }
            }
        }

        return maxDist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxDistance = function(grid) {
    const n = grid.length;
    const dist = Array.from({ length: n }, () => Array(n).fill(-1));
    const qx = [];
    const qy = [];
    let head = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                dist[i][j] = 0;
                qx.push(i);
                qy.push(j);
            }
        }
    }

    // No land or no water
    if (qx.length === 0 || qx.length === n * n) return -1;

    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let maxDist = 0;

    while (head < qx.length) {
        const x = qx[head];
        const y = qy[head];
        head++;
        const cur = dist[x][y];

        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] === -1) {
                dist[nx][ny] = cur + 1;
                maxDist = Math.max(maxDist, cur + 1);
                qx.push(nx);
                qy.push(ny);
            }
        }
    }

    return maxDist === 0 ? -1 : maxDist;
};
```

## Typescript

```typescript
function maxDistance(grid: number[][]): number {
    const n = grid.length;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const queue: [number, number][] = [];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                queue.push([i, j]);
            }
        }
    }

    if (queue.length === 0 || queue.length === n * n) return -1;

    const dist: number[][] = Array.from({ length: n }, () => Array(n).fill(-1));
    for (const [x, y] of queue) {
        dist[x][y] = 0;
    }

    let maxDist = -1;
    let head = 0;
    while (head < queue.length) {
        const [x, y] = queue[head++];
        const d = dist[x][y];
        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] === -1) {
                dist[nx][ny] = d + 1;
                maxDist = Math.max(maxDist, d + 1);
                queue.push([nx, ny]);
            }
        }
    }

    return maxDist;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxDistance($grid) {
        $n = count($grid);
        $queue = new SplQueue();
        $dist = array_fill(0, $n, array_fill(0, $n, -1));
        $landCount = 0;

        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 1) {
                    $queue->enqueue([$i, $j]);
                    $dist[$i][$j] = 0;
                    $landCount++;
                }
            }
        }

        if ($landCount == 0 || $landCount == $n * $n) {
            return -1;
        }

        $maxDist = 0;
        $dirs = [[1,0], [-1,0], [0,1], [0,-1]];

        while (!$queue->isEmpty()) {
            [$x, $y] = $queue->dequeue();
            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx >= 0 && $nx < $n && $ny >= 0 && $ny < $n && $dist[$nx][$ny] == -1) {
                    $dist[$nx][$ny] = $dist[$x][$y] + 1;
                    $maxDist = max($maxDist, $dist[$nx][$ny]);
                    $queue->enqueue([$nx, $ny]);
                }
            }
        }

        return $maxDist;
    }
}
```

## Swift

```swift
class Solution {
    func maxDistance(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var queue = [(Int, Int)]()
        var dist = Array(repeating: Array(repeating: -1, count: n), count: n)
        
        for i in 0..<n {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    queue.append((i, j))
                    dist[i][j] = 0
                }
            }
        }
        
        // If there is no land or no water, return -1
        if queue.isEmpty || queue.count == n * n {
            return -1
        }
        
        var head = 0
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var maxDist = -1
        
        while head < queue.count {
            let (x, y) = queue[head]
            head += 1
            
            for dir in directions {
                let nx = x + dir.0
                let ny = y + dir.1
                if nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] == -1 {
                    dist[nx][ny] = dist[x][y] + 1
                    maxDist = max(maxDist, dist[nx][ny])
                    queue.append((nx, ny))
                }
            }
        }
        
        return maxDist
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDistance(grid: Array<IntArray>): Int {
        val n = grid.size
        val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    queue.add(Pair(i, j))
                }
            }
        }
        // If there is no land or no water
        if (queue.isEmpty() || queue.size == n * n) return -1

        val dirs = intArrayOf(-1, 0, 1, 0, -1)
        var maxVal = -1

        while (queue.isNotEmpty()) {
            val (x, y) = queue.removeFirst()
            for (k in 0 until 4) {
                val nx = x + dirs[k]
                val ny = y + dirs[k + 1]
                if (nx in 0 until n && ny in 0 until n && grid[nx][ny] == 0) {
                    grid[nx][ny] = grid[x][y] + 1
                    maxVal = kotlin.math.max(maxVal, grid[nx][ny])
                    queue.add(Pair(nx, ny))
                }
            }
        }

        return if (maxVal == -1) -1 else maxVal - 1
    }
}
```

## Dart

```dart
class Solution {
  int maxDistance(List<List<int>> grid) {
    int n = grid.length;
    List<List<int>> dist = List.generate(n, (_) => List.filled(n, -1));
    List<List<int>> queue = [];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          dist[i][j] = 0;
          queue.add([i, j]);
        }
      }
    }

    // If there is no land or no water
    if (queue.isEmpty || queue.length == n * n) return -1;

    int maxDist = 0;
    List<int> dirs = [-1, 0, 1, 0, -1];
    int idx = 0;

    while (idx < queue.length) {
      var cell = queue[idx++];
      int x = cell[0], y = cell[1];

      for (int d = 0; d < 4; d++) {
        int nx = x + dirs[d];
        int ny = y + dirs[d + 1];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] == -1) {
          dist[nx][ny] = dist[x][y] + 1;
          maxDist = dist[nx][ny];
          queue.add([nx, ny]);
        }
      }
    }

    return maxDist;
  }
}
```

## Golang

```go
func maxDistance(grid [][]int) int {
    n := len(grid)
    if n == 0 {
        return -1
    }

    // Initialize queue with all land cells.
    type point struct{ x, y int }
    queue := make([]point, 0, n*n)
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                queue = append(queue, point{i, j})
            }
        }
    }

    // If there is no land or the whole grid is land, return -1.
    if len(queue) == 0 || len(queue) == n*n {
        return -1
    }

    dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    idx := 0
    for idx < len(queue) {
        cur := queue[idx]
        idx++
        for _, d := range dirs {
            nx, ny := cur.x+d[0], cur.y+d[1]
            if nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] == 0 {
                // Set distance as parent's distance + 1.
                grid[nx][ny] = grid[cur.x][cur.y] + 1
                queue = append(queue, point{nx, ny})
            }
        }
    }

    maxDist := 0
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] > maxDist {
                maxDist = grid[i][j]
            }
        }
    }
    return maxDist - 1
}
```

## Ruby

```ruby
def max_distance(grid)
  n = grid.size
  queue = []
  dist = Array.new(n) { Array.new(n, -1) }

  n.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        queue << [i, j]
        dist[i][j] = 0
      end
    end
  end

  return -1 if queue.empty? || queue.size == n * n

  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  front = 0
  max_d = 0

  while front < queue.length
    i, j = queue[front]
    front += 1
    d = dist[i][j]

    dirs.each do |di, dj|
      ni = i + di
      nj = j + dj
      next unless ni.between?(0, n - 1) && nj.between?(0, n - 1)
      next if dist[ni][nj] != -1

      dist[ni][nj] = d + 1
      max_d = d + 1 if d + 1 > max_d
      queue << [ni, nj]
    end
  end

  max_d
end
```

## Scala

```scala
object Solution {
    def maxDistance(grid: Array[Array[Int]]): Int = {
        val n = grid.length
        import scala.collection.mutable.Queue
        val q = Queue[(Int, Int)]()
        var hasLand = false
        var hasWater = false

        for (i <- 0 until n; j <- 0 until n) {
            if (grid(i)(j) == 1) {
                q.enqueue((i, j))
                hasLand = true
            } else {
                hasWater = true
            }
        }

        if (!hasLand || !hasWater) return -1

        val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
        var maxDist = 0

        while (q.nonEmpty) {
            val (x, y) = q.dequeue()
            for ((dx, dy) <- dirs) {
                val nx = x + dx
                val ny = y + dy
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && grid(nx)(ny) == 0) {
                    grid(nx)(ny) = grid(x)(y) + 1
                    maxDist = math.max(maxDist, grid(nx)(ny) - 1)
                    q.enqueue((nx, ny))
                }
            }
        }

        maxDist
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

pub struct Solution;

impl Solution {
    pub fn max_distance(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 0 {
            return -1;
        }
        let mut dist = vec![vec![-1i32; n]; n];
        let mut q = VecDeque::new();

        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 1 {
                    dist[i][j] = 0;
                    q.push_back((i as i32, j as i32));
                }
            }
        }

        if q.is_empty() {
            return -1; // no land
        }

        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((x, y)) = q.pop_front() {
            for &(dx, dy) in &dirs {
                let nx = x + dx;
                let ny = y + dy;
                if nx >= 0 && nx < n as i32 && ny >= 0 && ny < n as i32 {
                    let ux = nx as usize;
                    let uy = ny as usize;
                    if dist[ux][uy] == -1 {
                        dist[ux][uy] = dist[x as usize][y as usize] + 1;
                        q.push_back((nx, ny));
                    }
                }
            }
        }

        let mut maxd = -1;
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 0 && dist[i][j] > maxd {
                    maxd = dist[i][j];
                }
            }
        }

        maxd
    }
}
```

## Racket

```racket
#lang racket

(define/contract (max-distance grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         (dist (make-vector n))
         (queue-x (make-vector (* n n) 0))
         (queue-y (make-vector (* n n) 0)))
    (for ([i (in-range n)])
      (vector-set! dist i (make-vector n -1)))
    (define head 0)
    (define tail 0)
    ;; enqueue all land cells
    (for* ([i (in-range n)]
           [j (in-range n)])
      (when (= (list-ref (list-ref grid i) j) 1)
        (vector-set! (vector-ref dist i) j 0)
        (vector-set! queue-x tail i)
        (vector-set! queue-y tail j)
        (set! tail (+ tail 1))))
    (define land-count (- tail 0))
    (if (or (= land-count 0) (= land-count (* n n)))
        -1
        (let ((maxDist -1))
          (let loop ()
            (when (< head tail)
              (define x (vector-ref queue-x head))
              (define y (vector-ref queue-y head))
              (set! head (+ head 1))
              (for ([d '((1 . 0) (-1 . 0) (0 . 1) (0 . -1))])
                (define nx (+ x (car d)))
                (define ny (+ y (cdr d)))
                (when (and (>= nx 0) (< nx n) (>= ny 0) (< ny n))
                  (when (= (vector-ref (vector-ref dist nx) ny) -1)
                    (define nd (+ (vector-ref (vector-ref dist x) y) 1))
                    (vector-set! (vector-ref dist nx) ny nd)
                    (when (> nd maxDist) (set! maxDist nd))
                    (vector-set! queue-x tail nx)
                    (vector-set! queue-y tail ny)
                    (set! tail (+ tail 1)))))
              (loop)))
          maxDist))))
))))
```

## Erlang

```erlang
-module(solution).
-export([max_distance/1]).

-spec max_distance(Grid :: [[integer()]]) -> integer().
max_distance(Grid) ->
    N = length(Grid),
    LandPositions = [{I, J} ||
        {Row, I} <- lists:zip(Grid, lists:seq(0, N - 1)),
        {Val, J} <- lists:zip(Row, lists:seq(0, N - 1)),
        Val == 1],
    LandCount = length(LandPositions),
    WaterCount = N * N - LandCount,
    case {LandCount, WaterCount} of
        {0, _} -> -1;
        {_, 0} -> -1;
        _ ->
            Queue0 = lists:foldl(fun(Pos, Q) -> queue:in(Pos, Q) end, queue:new(), LandPositions),
            Visited0 = maps:from_list([{Pos, 0} || Pos <- LandPositions]),
            bfs(Queue0, Visited0, N, 0)
    end.

bfs(Queue, Visited, N, MaxDist) ->
    case queue:out(Queue) of
        {empty, _} -> MaxDist;
        {{value, {X, Y}}, Q1} ->
            CurrDist = maps:get({X, Y}, Visited),
            Neighs = [{X - 1, Y}, {X + 1, Y}, {X, Y - 1}, {X, Y + 1}],
            {Q2, Vis2, NewMax} =
                lists:foldl(
                    fun({NX, NY}, {QAcc, VAcc, MAcc}) ->
                        if
                            NX >= 0, NX < N,
                            NY >= 0, NY < N,
                            not maps:is_key({NX, NY}, VAcc) ->
                                D = CurrDist + 1,
                                Qn = queue:in({NX, NY}, QAcc),
                                Vn = maps:put({NX, NY}, D, VAcc),
                                {Qn, Vn, max(MAcc, D)};
                            true ->
                                {QAcc, VAcc, MAcc}
                        end
                    end,
                    {Q1, Visited, MaxDist},
                    Neighs),
            bfs(Q2, Vis2, N, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_distance(grid :: [[integer]]) :: integer
  def max_distance(grid) do
    n = length(grid)

    land_coords =
      for i <- 0..(n - 1),
          j <- 0..(n - 1),
          Enum.at(Enum.at(grid, i), j) == 1,
          do: {i, j}

    if land_coords == [] do
      -1
    else
      queue = :queue.from_list(Enum.map(land_coords, fn coord -> {coord, 0} end))
      visited = MapSet.new(land_coords)
      max_dist = bfs(queue, visited, grid, n, -1)

      if max_dist <= 0 do
        -1
      else
        max_dist
      end
    end
  end

  defp bfs(queue, visited, grid, n, current_max) do
    case :queue.out(queue) do
      {:empty, _} ->
        current_max

      {{:value, {coord, dist}}, q_rest} ->
        new_max = if dist > current_max, do: dist, else: current_max
        {r, c} = coord
        dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

        {new_queue, new_visited} =
          Enum.reduce(dirs, {q_rest, visited}, fn {dr, dc}, {q_acc, vis_acc} ->
            nr = r + dr
            nc = c + dc

            if nr >= 0 and nr < n and nc >= 0 and nc < n do
              if not MapSet.member?(vis_acc, {nr, nc}) and Enum.at(Enum.at(grid, nr), nc) == 0 do
                {
                  :queue.in({{nr, nc}, dist + 1}, q_acc),
                  MapSet.put(vis_acc, {nr, nc})
                }
              else
                {q_acc, vis_acc}
              end
            else
              {q_acc, vis_acc}
            end
          end)

        bfs(new_queue, new_visited, grid, n, new_max)
    end
  end
end
```

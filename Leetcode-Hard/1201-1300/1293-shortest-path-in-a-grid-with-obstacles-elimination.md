# 1293. Shortest Path in a Grid with Obstacles Elimination

## Cpp

```cpp
class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        if (m == 1 && n == 1) return 0;
        int minSteps = m + n - 2;
        if (k >= minSteps) return minSteps;
        
        vector<vector<int>> best(m, vector<int>(n, -1));
        struct Node {int x,y,steps,rem;};
        queue<Node> q;
        q.push({0,0,0,k});
        best[0][0] = k;
        const int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        
        while (!q.empty()) {
            Node cur = q.front(); q.pop();
            for (auto &d : dirs) {
                int nx = cur.x + d[0];
                int ny = cur.y + d[1];
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                int nrem = cur.rem - grid[nx][ny];
                if (nrem < 0) continue;
                int nsteps = cur.steps + 1;
                if (nx == m-1 && ny == n-1) return nsteps;
                if (best[nx][ny] >= nrem) continue;
                best[nx][ny] = nrem;
                q.push({nx,ny,nsteps,nrem});
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        if (k >= m + n - 2) return m + n - 2; // can go straight
        
        int[][] visited = new int[m][n];
        for (int i = 0; i < m; i++) {
            java.util.Arrays.fill(visited[i], -1);
        }
        java.util.ArrayDeque<int[]> q = new java.util.ArrayDeque<>();
        q.offer(new int[]{0, 0, k});
        visited[0][0] = k;
        int steps = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] cur = q.poll();
                int x = cur[0], y = cur[1], remain = cur[2];
                if (x == m - 1 && y == n - 1) return steps;
                
                for (int[] d : dirs) {
                    int nx = x + d[0];
                    int ny = y + d[1];
                    if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                    int nr = remain - grid[nx][ny];
                    if (nr < 0) continue;
                    if (visited[nx][ny] >= nr) continue; // already visited with equal or more remaining eliminations
                    visited[nx][ny] = nr;
                    q.offer(new int[]{nx, ny, nr});
                }
            }
            steps++;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        # If we can eliminate enough obstacles to go straight line
        if k >= m + n - 2:
            return m + n - 2

        # Directions: up, down, left, right
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # visited[x][y] stores the maximum remaining eliminations we've had at this cell
        visited = [[-1]*n for _ in range(m)]
        dq = deque()
        dq.append((0, 0, k))
        visited[0][0] = k
        steps = 0

        while dq:
            for _ in range(len(dq)):
                x, y, rem = dq.popleft()
                if x == m-1 and y == n-1:
                    return steps
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        nrem = rem - grid[nx][ny]
                        if nrem < 0:
                            continue
                        # If we have visited with equal or more remaining eliminations, skip
                        if visited[nx][ny] >= nrem:
                            continue
                        visited[nx][ny] = nrem
                        dq.append((nx, ny, nrem))
            steps += 1

        return -1
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        # If we can eliminate enough obstacles to go straight line
        if k >= m + n - 2:
            return m + n - 2

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[-1] * n for _ in range(m)]   # max remaining eliminations when visiting cell
        q = deque()
        q.append((0, 0, k, 0))  # x, y, remaining k, steps
        visited[0][0] = k

        while q:
            x, y, rem, steps = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nk = rem - grid[nx][ny]
                    if nk < 0:
                        continue
                    if nx == m - 1 and ny == n - 1:
                        return steps + 1
                    if visited[nx][ny] >= nk:
                        continue
                    visited[nx][ny] = nk
                    q.append((nx, ny, nk, steps + 1))
        return -1
```

## C

```c
#include <stdlib.h>

typedef struct {
    short x;
    short y;
    short rem;
    int steps;
} Node;

static inline long idx(int x, int y, int rem, int n, int maxRem) {
    return ((long)x * n + y) * (maxRem + 1) + rem;
}

int shortestPath(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize;
    int n = gridColSize[0];
    if (m == 1 && n == 1) return 0;
    if (k >= m + n - 2) return m + n - 2;

    int maxRem = k;
    long totalStates = (long)m * n * (maxRem + 1);
    char *visited = calloc(totalStates, sizeof(char));
    if (!visited) return -1;

    Node *queue = malloc(totalStates * sizeof(Node));
    if (!queue) {
        free(visited);
        return -1;
    }

    int head = 0, tail = 0;
    queue[tail++] = (Node){0, 0, (short)k, 0};
    visited[idx(0, 0, k, n, maxRem)] = 1;

    const int dx[4] = {-1, 1, 0, 0};
    const int dy[4] = {0, 0, -1, 1};

    while (head < tail) {
        Node cur = queue[head++];
        if (cur.x == m - 1 && cur.y == n - 1) {
            free(visited);
            free(queue);
            return cur.steps;
        }
        for (int d = 0; d < 4; ++d) {
            int nx = cur.x + dx[d];
            int ny = cur.y + dy[d];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            int nrem = cur.rem - grid[nx][ny];
            if (nrem < 0) continue;
            long id = idx(nx, ny, nrem, n, maxRem);
            if (visited[id]) continue;
            visited[id] = 1;
            queue[tail++] = (Node){(short)nx, (short)ny, (short)nrem, cur.steps + 1};
        }
    }

    free(visited);
    free(queue);
    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int ShortestPath(int[][] grid, int k)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        // If we can eliminate enough obstacles to go straight line
        if (k >= m + n - 2) return m + n - 2;

        var visited = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                visited[i, j] = -1;

        var q = new System.Collections.Generic.Queue<(int x, int y, int steps, int remain)>();
        q.Enqueue((0, 0, 0, k));
        visited[0, 0] = k;

        int[] dx = new int[] { 1, -1, 0, 0 };
        int[] dy = new int[] { 0, 0, 1, -1 };

        while (q.Count > 0)
        {
            var cur = q.Dequeue();
            int x = cur.x, y = cur.y, steps = cur.steps, remain = cur.remain;

            if (x == m - 1 && y == n - 1) return steps;

            for (int dir = 0; dir < 4; dir++)
            {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;

                int nr = remain - grid[nx][ny];
                if (nr < 0) continue;

                if (visited[nx, ny] >= nr) continue;
                visited[nx, ny] = nr;
                q.Enqueue((nx, ny, steps + 1, nr));
            }
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var shortestPath = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    if (m === 1 && n === 1) return 0;
    const minSteps = m - 1 + n - 1;
    if (k >= minSteps) return minSteps;

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    const visited = Array.from({length: m}, () => Array(n).fill(-1));
    let queue = [];
    let head = 0;
    queue.push([0, 0, k]);
    visited[0][0] = k;

    let steps = 0;
    while (head < queue.length) {
        const levelSize = queue.length - head;
        for (let i = 0; i < levelSize; i++) {
            const [x, y, rem] = queue[head++];
            if (x === m - 1 && y === n - 1) return steps;
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                const nrem = rem - grid[nx][ny];
                if (nrem < 0) continue;
                if (visited[nx][ny] >= nrem) continue;
                visited[nx][ny] = nrem;
                queue.push([nx, ny, nrem]);
            }
        }
        steps++;
    }
    return -1;
};
```

## Typescript

```typescript
function shortestPath(grid: number[][], k: number): number {
    const m = grid.length;
    const n = grid[0].length;
    // If we can eliminate enough obstacles to go straight line
    if (k >= m + n - 2) return m + n - 2;

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    // visited[x][y] stores the maximum remaining eliminations when reaching (x,y)
    const visited: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
    const queue: [number, number, number][] = [];
    let head = 0;

    queue.push([0, 0, k]);
    visited[0][0] = k;
    let steps = 0;

    while (head < queue.length) {
        const size = queue.length - head;
        for (let i = 0; i < size; i++) {
            const [x, y, remain] = queue[head++];
            if (x === m - 1 && y === n - 1) return steps;

            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                const nk = remain - grid[nx][ny];
                if (nk < 0) continue;
                if (visited[nx][ny] >= nk) continue; // already visited with equal or more remaining eliminations
                visited[nx][ny] = nk;
                queue.push([nx, ny, nk]);
            }
        }
        steps++;
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer
     */
    function shortestPath($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        if ($m == 1 && $n == 1) return 0;

        // Optional early exit: Manhattan distance <= k
        $minSteps = $m + $n - 2;
        if ($k >= $minSteps) return $minSteps;

        // visited[x][y] = max remaining eliminations when reaching (x,y)
        $visited = array_fill(0, $m, array_fill(0, $n, -1));
        $queue = new SplQueue();
        $queue->enqueue([0, 0, $k, 0]); // x, y, remaining k, steps
        $visited[0][0] = $k;

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$queue->isEmpty()) {
            [$x, $y, $rem, $steps] = $queue->dequeue();

            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];

                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;

                $nr = $rem - $grid[$nx][$ny];
                if ($nr < 0) continue; // cannot pass this obstacle

                if ($nx == $m - 1 && $ny == $n - 1) {
                    return $steps + 1;
                }

                if ($visited[$nx][$ny] >= $nr) continue; // already visited with equal or more remaining eliminations

                $visited[$nx][$ny] = $nr;
                $queue->enqueue([$nx, $ny, $nr, $steps + 1]);
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func shortestPath(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count
        let n = grid[0].count
        if m == 1 && n == 1 { return 0 }
        // Optional early exit: if we can eliminate enough obstacles to go straight line
        if k >= m + n - 2 { return m + n - 2 }
        
        var visited = Array(repeating: Array(repeating: -1, count: n), count: m)
        var queue: [(Int, Int, Int, Int)] = [] // x, y, remaining eliminations, steps
        var head = 0
        
        visited[0][0] = k
        queue.append((0, 0, k, 0))
        
        let dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while head < queue.count {
            let (x, y, rem, steps) = queue[head]
            head += 1
            
            for d in dirs {
                let nx = x + d.0
                let ny = y + d.1
                if nx < 0 || nx >= m || ny < 0 || ny >= n { continue }
                
                if nx == m - 1 && ny == n - 1 {
                    return steps + 1
                }
                
                var newRem = rem - grid[nx][ny]
                if newRem < 0 { continue }
                
                if visited[nx][ny] >= newRem { continue }
                visited[nx][ny] = newRem
                queue.append((nx, ny, newRem, steps + 1))
            }
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestPath(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        if (m == 1 && n == 1) return 0
        // If we can eliminate enough obstacles to go straight line, answer is Manhattan distance
        if (k >= m + n - 2) return m + n - 2

        val visited = Array(m) { Array(n) { BooleanArray(k + 1) } }
        val queue: ArrayDeque<IntArray> = ArrayDeque()
        queue.add(intArrayOf(0, 0, k))
        visited[0][0][k] = true
        var steps = 0
        val dirs = intArrayOf(0, 1, 0, -1, 0)

        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) {
                val cur = queue.removeFirst()
                val x = cur[0]
                val y = cur[1]
                var remain = cur[2]

                if (x == m - 1 && y == n - 1) return steps

                for (d in 0 until 4) {
                    val nx = x + dirs[d]
                    val ny = y + dirs[d + 1]
                    if (nx !in 0 until m || ny !in 0 until n) continue
                    var newRemain = remain - grid[nx][ny]
                    if (newRemain < 0) continue
                    if (!visited[nx][ny][newRemain]) {
                        visited[nx][ny][newRemain] = true
                        queue.add(intArrayOf(nx, ny, newRemain))
                    }
                }
            }
            steps++
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int shortestPath(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    if (m == 1 && n == 1) return 0;
    if (k >= m + n - 2) return m + n - 2;

    List<List<int>> best = List.generate(m, (_) => List.filled(n, -1));
    Queue<List<int>> q = Queue();
    q.add([0, 0, k, 0]);
    best[0][0] = k;
    const List<int> dirs = [0, 1, 0, -1, 0];

    while (q.isNotEmpty) {
      var cur = q.removeFirst();
      int x = cur[0];
      int y = cur[1];
      int rem = cur[2];
      int steps = cur[3];

      if (x == m - 1 && y == n - 1) return steps;

      for (int d = 0; d < 4; ++d) {
        int nx = x + dirs[d];
        int ny = y + dirs[d + 1];
        if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
        int nrem = rem - grid[nx][ny];
        if (nrem < 0) continue;
        if (best[nx][ny] >= nrem) continue;
        best[nx][ny] = nrem;
        q.add([nx, ny, nrem, steps + 1]);
      }
    }

    return -1;
  }
}
```

## Golang

```go
func shortestPath(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	if m == 1 && n == 1 {
		return 0
	}
	// Early exit: if we can eliminate enough obstacles to go straight.
	if k >= m+n-2 {
		return m + n - 2
	}
	type node struct {
		x, y   int
		remain int
	}
	visited := make([][]int, m)
	for i := range visited {
		visited[i] = make([]int, n)
		for j := range visited[i] {
			visited[i][j] = -1
		}
	}
	q := []node{{0, 0, k}}
	visited[0][0] = k
	steps := 0
	dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(q) > 0 {
		size := len(q)
		for i := 0; i < size; i++ {
			cur := q[0]
			q = q[1:]
			if cur.x == m-1 && cur.y == n-1 {
				return steps
			}
			for _, d := range dir {
				nx, ny := cur.x+d[0], cur.y+d[1]
				if nx < 0 || nx >= m || ny < 0 || ny >= n {
					continue
				}
				nr := cur.remain - grid[nx][ny]
				if nr < 0 {
					continue
				}
				if visited[nx][ny] >= nr {
					continue
				}
				visited[nx][ny] = nr
				q = append(q, node{nx, ny, nr})
			}
		}
		steps++
	}
	return -1
}
```

## Ruby

```ruby
def shortest_path(grid, k)
  m = grid.size
  n = grid[0].size
  return m - 1 + n - 1 if k >= m + n - 2

  dirs = [[1,0],[-1,0],[0,1],[0,-1]]
  visited = Array.new(m) { Array.new(n, -1) }
  queue = []
  head = 0
  queue << [0, 0, k, 0]
  visited[0][0] = k

  while head < queue.size
    x, y, rem, steps = queue[head]
    head += 1
    return steps if x == m - 1 && y == n - 1

    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      next unless nx.between?(0, m - 1) && ny.between?(0, n - 1)

      nrem = rem - grid[nx][ny]
      next if nrem < 0
      next if visited[nx][ny] >= nrem

      visited[nx][ny] = nrem
      queue << [nx, ny, nrem, steps + 1]
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
  def shortestPath(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    if (m == 1 && n == 1) return 0
    // If we can eliminate enough obstacles to go straight line, answer is Manhattan distance
    if (k >= m + n - 2) return m + n - 2

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    val visited = Array.fill(m, n)(-1)
    import scala.collection.mutable.ArrayDeque
    val q = new ArrayDeque[(Int, Int, Int)]()
    q.append((0, 0, k))
    visited(0)(0) = k

    var steps = 0
    while (q.nonEmpty) {
      val size = q.size
      for (_ <- 0 until size) {
        val (x, y, rem) = q.removeHead()
        if (x == m - 1 && y == n - 1) return steps
        for ((dx, dy) <- dirs) {
          val nx = x + dx
          val ny = y + dy
          if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
            val nrem = rem - grid(nx)(ny)
            if (nrem >= 0 && nrem > visited(nx)(ny)) {
              visited(nx)(ny) = nrem
              q.append((nx, ny, nrem))
            }
          }
        }
      }
      steps += 1
    }
    -1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_path(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        use std::collections::VecDeque;
        let m = grid.len();
        let n = grid[0].len();

        // If start is the same as end
        if m == 1 && n == 1 {
            return 0;
        }

        // Early exit: enough eliminations to go straight Manhattan distance
        let min_needed = (m - 1 + n - 1) as i32;
        if k >= min_needed {
            return min_needed;
        }

        let mut visited = vec![vec![-1i32; n]; m];
        let mut q: VecDeque<(usize, usize, i32, usize)> = VecDeque::new();
        visited[0][0] = k;
        q.push_back((0, 0, k, 0));

        let dirs = [(1_i32, 0_i32), (-1, 0), (0, 1), (0, -1)];

        while let Some((x, y, rem, steps)) = q.pop_front() {
            for &(dx, dy) in &dirs {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx < 0 || ny < 0 || nx >= m as i32 || ny >= n as i32 {
                    continue;
                }
                let ux = nx as usize;
                let uy = ny as usize;

                let mut new_rem = rem;
                if grid[ux][uy] == 1 {
                    new_rem -= 1;
                }
                if new_rem < 0 {
                    continue;
                }

                // If we reached the target
                if ux == m - 1 && uy == n - 1 {
                    return (steps + 1) as i32;
                }

                if visited[ux][uy] >= new_rem {
                    continue;
                }
                visited[ux][uy] = new_rem;
                q.push_back((ux, uy, new_rem, steps + 1));
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

(define/contract (shortest-path grid k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (first grid))))
         (gridV (list->vector (map list->vector grid)))
         (visited (make-vector m)))
    (for ([i (in-range m)])
      (vector-set! visited i (make-vector n -1)))
    (define dirs '((1 0) (-1 0) (0 1) (0 -1)))
    (define q (make-queue))
    (enqueue! q (list 0 0 k 0)) ; x y remaining steps
    (vector-set! (vector-ref visited 0) 0 k)
    (let bfs ()
      (if (queue-empty? q)
          -1
          (let* ((state (dequeue! q))
                 (x (list-ref state 0))
                 (y (list-ref state 1))
                 (rem (list-ref state 2))
                 (steps (list-ref state 3)))
            (if (and (= x (- m 1)) (= y (- n 1)))
                steps
                (begin
                  (for ([dir dirs])
                    (define dx (first dir))
                    (define dy (second dir))
                    (define nx (+ x dx))
                    (define ny (+ y dy))
                    (when (and (>= nx 0) (< nx m) (>= ny 0) (< ny n))
                      (let* ((cell (vector-ref (vector-ref gridV nx) ny))
                             (newRem (- rem cell)))
                        (when (and (>= newRem 0)
                                   (> newRem (vector-ref (vector-ref visited nx) ny)))
                          (vector-set! (vector-ref visited nx) ny newRem)
                          (enqueue! q (list nx ny newRem (+ steps 1))))))))
                  (bfs))))))))
```

## Erlang

```erlang
-module(solution).
-export([shortest_path/2]).

-spec shortest_path(Grid :: [[integer()]], K :: integer()) -> integer().
shortest_path(Grid, K) ->
    M = length(Grid),
    N = length(hd(Grid)),
    case {M, N} of
        {1, 1} -> 0;
        _ ->
            bfs(queue:in({0, 0, K, 0}, queue:new()),
                #{ {0, 0} => K },
                Grid,
                M,
                N)
    end.

bfs(Queue, Visited, Grid, M, N) ->
    case queue:out(Queue) of
        empty -> -1;
        {{value, {X, Y, Rem, Dist}}, Q1} ->
            if X =:= M - 1 andalso Y =:= N - 1 ->
                    Dist;
               true ->
                    Directions = [{1,0}, {-1,0}, {0,1}, {0,-1}],
                    {NewQueue, NewVisited} = lists:foldl(
                        fun({DX, DY}, {QAcc, VAcc}) ->
                            NX = X + DX,
                            NY = Y + DY,
                            if NX >= 0, NX < M, NY >= 0, NY < N ->
                                    Cell = get_cell(Grid, NX, NY),
                                    case Cell of
                                        0 ->
                                            try_enqueue(NX, NY, Rem, Dist + 1, QAcc, VAcc);
                                        1 when Rem > 0 ->
                                            try_enqueue(NX, NY, Rem - 1, Dist + 1, QAcc, VAcc);
                                        _ -> {QAcc, VAcc}
                                    end;
                               true -> {QAcc, VAcc}
                            end
                        end,
                        {Q1, Visited},
                        Directions),
                    bfs(NewQueue, NewVisited, Grid, M, N)
            end
    end.

try_enqueue(NX, NY, NewRem, NewDist, Q, Vis) ->
    Prev = maps:get({NX, NY}, Vis, -1),
    if NewRem > Prev ->
            {queue:in({NX, NY, NewRem, NewDist}, Q), maps:put({NX, NY}, NewRem, Vis)};
       true -> {Q, Vis}
    end.

get_cell(Grid, X, Y) ->
    Row = lists:nth(X + 1, Grid),
    lists:nth(Y + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_path(grid :: [[integer]], k :: integer) :: integer
  def shortest_path(grid, k) do
    m = length(grid)
    n = length(hd(grid))

    # If we can eliminate enough obstacles to go straight line
    if k >= m + n - 2 do
      m + n - 2
    else
      rows = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
      visited = %{{0, 0} => k}
      queue = :queue.in({0, 0, k, 0}, :queue.new())
      bfs(queue, visited, rows, m, n)
    end
  end

  defp bfs(queue, visited, rows, m, n) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {x, y, rem, steps}}, q2} ->
        if x == m - 1 and y == n - 1 do
          steps
        else
          dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

          {new_queue, new_visited} =
            Enum.reduce(dirs, {q2, visited}, fn {dx, dy}, {q_acc, vis_acc} ->
              nx = x + dx
              ny = y + dy

              if nx < 0 or nx >= m or ny < 0 or ny >= n do
                {q_acc, vis_acc}
              else
                cell = :erlang.element(ny + 1, elem(rows, nx))
                new_rem = rem - cell

                cond do
                  new_rem < 0 ->
                    {q_acc, vis_acc}

                  true ->
                    key = {nx, ny}
                    prev = Map.get(vis_acc, key, -1)

                    if new_rem > prev do
                      q_next = :queue.in({nx, ny, new_rem, steps + 1}, q_acc)
                      vis_next = Map.put(vis_acc, key, new_rem)
                      {q_next, vis_next}
                    else
                      {q_acc, vis_acc}
                    end
                end
              end
            end)

          bfs(new_queue, new_visited, rows, m, n)
        end
    end
  end
end
```

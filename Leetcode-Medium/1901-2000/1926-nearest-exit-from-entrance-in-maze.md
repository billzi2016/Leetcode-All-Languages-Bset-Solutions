# 1926. Nearest Exit from Entrance in Maze

## Cpp

```cpp
class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size();
        int n = maze[0].size();
        const int dr[4] = {1, -1, 0, 0};
        const int dc[4] = {0, 0, 1, -1};
        
        vector<vector<int>> dist(m, vector<int>(n, -1));
        queue<pair<int,int>> q;
        int sr = entrance[0], sc = entrance[1];
        q.emplace(sr, sc);
        dist[sr][sc] = 0;
        
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (maze[nr][nc] != '.' || dist[nr][nc] != -1) continue;
                dist[nr][nc] = dist[r][c] + 1;
                // check if it's an exit (border cell, not the entrance)
                if (nr == 0 || nr == m-1 || nc == 0 || nc == n-1) {
                    return dist[nr][nc];
                }
                q.emplace(nr, nc);
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length;
        int n = maze[0].length;
        boolean[][] visited = new boolean[m][n];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        int sr = entrance[0], sc = entrance[1];
        q.offer(new int[]{sr, sc, 0});
        visited[sr][sc] = true;

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1], d = cur[2];

            // Check if current cell is an exit (border) and not the entrance
            if ((r == 0 || r == m - 1 || c == 0 || c == n - 1) && !(r == sr && c == sc)) {
                return d;
            }

            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                    maze[nr][nc] == '.' && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.offer(new int[]{nr, nc, d + 1});
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
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        from collections import deque

        m, n = len(maze), len(maze[0])
        sr, sc = entrance
        # mark entrance as visited
        maze[sr][sc] = '+'
        q = deque()
        q.append((sr, sc, 0))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, d = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    # check if it's an exit (border cell)
                    if nr == 0 or nr == m-1 or nc == 0 or nc == n-1:
                        return d + 1
                    maze[nr][nc] = '+'
                    q.append((nr, nc, d + 1))
        return -1
```

## Python3

```python
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque

        m, n = len(maze), len(maze[0])
        sr, sc = entrance
        q = deque()
        q.append((sr, sc, 0))
        # mark visited
        maze[sr][sc] = '+'

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, d = q.popleft()
            # check if this cell is an exit (border) but not the entrance
            if (r != sr or c != sc) and (r == 0 or r == m-1 or c == 0 or c == n-1):
                return d
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    maze[nr][nc] = '+'  # mark visited
                    q.append((nr, nc, d + 1))
        return -1
```

## C

```c
#include <stdlib.h>

int nearestExit(char** maze, int mazeSize, int* mazeColSize, int* entrance, int entranceSize) {
    int m = mazeSize;
    int n = mazeColSize[0];

    char **vis = (char **)malloc(m * sizeof(char *));
    for (int i = 0; i < m; ++i) {
        vis[i] = (char *)calloc(n, sizeof(char));
    }

    int max = m * n;
    int *qr = (int *)malloc(max * sizeof(int));
    int *qc = (int *)malloc(max * sizeof(int));
    int *qd = (int *)malloc(max * sizeof(int));

    int front = 0, back = 0;
    int sr = entrance[0], sc = entrance[1];
    qr[back] = sr; qc[back] = sc; qd[back] = 0; ++back;
    vis[sr][sc] = 1;

    const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    while (front < back) {
        int r = qr[front];
        int c = qc[front];
        int d = qd[front];
        ++front;

        for (int k = 0; k < 4; ++k) {
            int nr = r + dirs[k][0];
            int nc = c + dirs[k][1];

            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (maze[nr][nc] == '+') continue;
            if (vis[nr][nc]) continue;

            if (nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1) {
                for (int i = 0; i < m; ++i) free(vis[i]);
                free(vis);
                free(qr); free(qc); free(qd);
                return d + 1;
            }

            vis[nr][nc] = 1;
            qr[back] = nr; qc[back] = nc; qd[back] = d + 1;
            ++back;
        }
    }

    for (int i = 0; i < m; ++i) free(vis[i]);
    free(vis);
    free(qr); free(qc); free(qd);
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int NearestExit(char[][] maze, int[] entrance) {
        int m = maze.Length;
        int n = maze[0].Length;
        bool[,] visited = new bool[m, n];
        var q = new System.Collections.Generic.Queue<(int r, int c, int d)>();
        q.Enqueue((entrance[0], entrance[1], 0));
        visited[entrance[0], entrance[1]] = true;

        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (q.Count > 0) {
            var cur = q.Dequeue();
            int r = cur.r, c = cur.c, d = cur.d;

            if ((r == 0 || r == m - 1 || c == 0 || c == n - 1) &&
                !(r == entrance[0] && c == entrance[1])) {
                return d;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                    !visited[nr, nc] && maze[nr][nc] == '.') {
                    visited[nr, nc] = true;
                    q.Enqueue((nr, nc, d + 1));
                }
            }
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function(maze, entrance) {
    const m = maze.length;
    const n = maze[0].length;
    const [sr, sc] = entrance;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    // visited matrix
    const visited = Array.from({length: m}, () => Array(n).fill(false));
    const queue = [];
    let head = 0;
    
    visited[sr][sc] = true;
    queue.push([sr, sc, 0]); // row, col, distance
    
    while (head < queue.length) {
        const [r, c, d] = queue[head++];
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (maze[nr][nc] === '+' || visited[nr][nc]) continue;
            // If this cell is on the border, it's an exit
            if (nr === 0 || nr === m - 1 || nc === 0 || nc === n - 1) {
                return d + 1;
            }
            visited[nr][nc] = true;
            queue.push([nr, nc, d + 1]);
        }
    }
    
    return -1;
};
```

## Typescript

```typescript
function nearestExit(maze: string[][], entrance: number[]): number {
    const m = maze.length;
    const n = maze[0].length;
    const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));
    const queue: [number, number, number][] = [];
    const [sr, sc] = entrance;
    visited[sr][sc] = true;
    queue.push([sr, sc, 0]);
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let head = 0;
    while (head < queue.length) {
        const [r, c, d] = queue[head++];
        if ((r === 0 || r === m - 1 || c === 0 || c === n - 1) && !(r === sr && c === sc)) {
            return d;
        }
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (
                nr >= 0 && nr < m &&
                nc >= 0 && nc < n &&
                !visited[nr][nc] &&
                maze[nr][nc] === '.'
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
     * @param String[][] $maze
     * @param Integer[] $entrance
     * @return Integer
     */
    function nearestExit($maze, $entrance) {
        $m = count($maze);
        $n = count($maze[0]);
        [$sr, $sc] = $entrance;

        $queue = new SplQueue();
        $queue->enqueue([$sr, $sc, 0]);

        $visited = array_fill(0, $m, array_fill(0, $n, false));
        $visited[$sr][$sc] = true;

        $dirs = [[1,0], [-1,0], [0,1], [0,-1]];

        while (!$queue->isEmpty()) {
            [$r, $c, $d] = $queue->dequeue();
            foreach ($dirs as $dir) {
                $nr = $r + $dir[0];
                $nc = $c + $dir[1];

                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) {
                    continue;
                }
                if ($maze[$nr][$nc] === '+' || $visited[$nr][$nc]) {
                    continue;
                }

                // If it's on the border, it's an exit.
                if ($nr == 0 || $nr == $m - 1 || $nc == 0 || $nc == $n - 1) {
                    return $d + 1;
                }

                $queue->enqueue([$nr, $nc, $d + 1]);
                $visited[$nr][$nc] = true;
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func nearestExit(_ maze: [[Character]], _ entrance: [Int]) -> Int {
        let m = maze.count
        let n = maze[0].count
        var visited = Array(repeating: Array(repeating: false, count: n), count: m)
        var queue: [(Int, Int, Int)] = []
        let startR = entrance[0]
        let startC = entrance[1]
        visited[startR][startC] = true
        queue.append((startR, startC, 0))
        var idx = 0
        let dr = [-1, 1, 0, 0]
        let dc = [0, 0, -1, 1]
        
        while idx < queue.count {
            let (r, c, d) = queue[idx]
            idx += 1
            for k in 0..<4 {
                let nr = r + dr[k]
                let nc = c + dc[k]
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                if visited[nr][nc] { continue }
                if maze[nr][nc] == "+" { continue }
                
                // Check if this cell is an exit (border cell)
                if nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1 {
                    return d + 1
                }
                
                visited[nr][nc] = true
                queue.append((nr, nc, d + 1))
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nearestExit(maze: Array<CharArray>, entrance: IntArray): Int {
        val m = maze.size
        val n = maze[0].size
        val visited = Array(m) { BooleanArray(n) }
        val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        val (sr, sc) = entrance
        visited[sr][sc] = true
        queue.add(Pair(sr, sc))
        var steps = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) {
                val (r, c) = queue.removeFirst()
                if (steps > 0 && (r == 0 || r == m - 1 || c == 0 || c == n - 1)) {
                    return steps
                }
                for (d in dirs) {
                    val nr = r + d[0]
                    val nc = c + d[1]
                    if (nr in 0 until m && nc in 0 until n &&
                        maze[nr][nc] == '.' && !visited[nr][nc]) {
                        visited[nr][nc] = true
                        queue.add(Pair(nr, nc))
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

class _Node {
  final int r;
  final int c;
  final int dist;
  _Node(this.r, this.c, this.dist);
}

class Solution {
  int nearestExit(List<List<String>> maze, List<int> entrance) {
    final m = maze.length;
    final n = maze[0].length;
    final visited = List.generate(m, (_) => List.filled(n, false));
    final queue = Queue<_Node>();

    final startR = entrance[0];
    final startC = entrance[1];
    visited[startR][startC] = true;
    queue.add(_Node(startR, startC, 0));

    const dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1]
    ];

    while (queue.isNotEmpty) {
      final cur = queue.removeFirst();
      for (final d in dirs) {
        final nr = cur.r + d[0];
        final nc = cur.c + d[1];

        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
        if (maze[nr][nc] != '.' || visited[nr][nc]) continue;

        visited[nr][nc] = true;
        final ndist = cur.dist + 1;

        // Check if it's an exit (border cell, not the entrance)
        if (nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1) {
          return ndist;
        }

        queue.add(_Node(nr, nc, ndist));
      }
    }

    return -1;
  }
}
```

## Golang

```go
func nearestExit(maze [][]byte, entrance []int) int {
	m, n := len(maze), len(maze[0])
	type point struct{ r, c, d int }
	q := make([]point, 0, m*n)
	er, ec := entrance[0], entrance[1]
	maze[er][ec] = '+'
	q = append(q, point{er, ec, 0})
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for i := 0; i < len(q); i++ {
		cur := q[i]
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n {
				continue
			}
			if maze[nr][nc] != '.' {
				continue
			}
			if nr == 0 || nr == m-1 || nc == 0 || nc == n-1 {
				return cur.d + 1
			}
			maze[nr][nc] = '+'
			q = append(q, point{nr, nc, cur.d + 1})
		}
	}
	return -1
}
```

## Ruby

```ruby
def nearest_exit(maze, entrance)
  m = maze.size
  n = maze[0].size
  sr, sc = entrance
  queue = []
  head = 0
  queue << [sr, sc, 0]
  maze[sr][sc] = '+'

  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

  while head < queue.size
    r, c, d = queue[head]
    head += 1
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= m || nc < 0 || nc >= n
      next unless maze[nr][nc] == '.'
      return d + 1 if nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1
      queue << [nr, nc, d + 1]
      maze[nr][nc] = '+'
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.ArrayDeque

    def nearestExit(maze: Array[Array[Char]], entrance: Array[Int]): Int = {
        val m = maze.length
        val n = maze(0).length
        val visited = Array.ofDim[Boolean](m, n)
        val queue = new ArrayDeque[(Int, Int, Int)]()
        val (sr, sc) = (entrance(0), entrance(1))
        visited(sr)(sc) = true
        queue.append((sr, sc, 0))

        val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))

        while (queue.nonEmpty) {
            val (r, c, d) = queue.removeHead()
            if ((r == 0 || r == m - 1 || c == 0 || c == n - 1) && !(r == sr && c == sc)) {
                return d
            }
            for ((dr, dc) <- dirs) {
                val nr = r + dr
                val nc = c + dc
                if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                    !visited(nr)(nc) && maze(nr)(nc) == '.') {
                    visited(nr)(nc) = true
                    queue.append((nr, nc, d + 1))
                }
            }
        }

        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn nearest_exit(maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        use std::collections::VecDeque;
        let m = maze.len();
        if m == 0 {
            return -1;
        }
        let n = maze[0].len();

        let start_r = entrance[0] as usize;
        let start_c = entrance[1] as usize;

        let mut visited = vec![vec![false; n]; m];
        let mut q: VecDeque<(usize, usize, i32)> = VecDeque::new();
        visited[start_r][start_c] = true;
        q.push_back((start_r, start_c, 0));

        while let Some((r, c, d)) = q.pop_front() {
            if (r == 0 || r + 1 == m || c == 0 || c + 1 == n) && !(r == start_r && c == start_c) {
                return d;
            }
            const DIRS: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
            for &(dr, dc) in &DIRS {
                let nr_i = r as i32 + dr;
                let nc_i = c as i32 + dc;
                if nr_i < 0 || nr_i >= m as i32 || nc_i < 0 || nc_i >= n as i32 {
                    continue;
                }
                let nr = nr_i as usize;
                let nc = nc_i as usize;
                if !visited[nr][nc] && maze[nr][nc] == '.' {
                    visited[nr][nc] = true;
                    q.push_back((nr, nc, d + 1));
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
(require racket/queue)

(define/contract (nearest-exit maze entrance)
  (-> (listof (listof char?)) (listof exact-integer?) exact-integer?)
  (let* ((m (length maze))
         (n (if (zero? m) 0 (length (first maze))))
         (visited (let ([v (make-vector m)])
                    (for ([i (in-range m)])
                      (vector-set! v i (make-vector n #f)))
                    v))
         (entrance-row (first entrance))
         (entrance-col (second entrance))
         (q (make-queue)))
    ;; start BFS
    (vector-set! (vector-ref visited entrance-row) entrance-col #t)
    (queue-enqueue! q (list (list entrance-row entrance-col) 0))
    (let loop ()
      (if (queue-empty? q)
          -1
          (let* ((item (queue-dequeue! q))
                 (pos (first item))
                 (dist (second item))
                 (r (first pos))
                 (c (second pos)))
            (if (and (or (= r 0) (= r (- m 1)) (= c 0) (= c (- n 1)))
                     (not (and (= r entrance-row) (= c entrance-col))))
                dist
                (begin
                  (for ([dr '(1 -1 0 0)] [dc '(0 0 1 -1)])
                    (let ((nr (+ r dr))
                          (nc (+ c dc)))
                      (when (and (>= nr 0) (< nr m)
                                 (>= nc 0) (< nc n)
                                 (not (vector-ref (vector-ref visited nr) nc))
                                 (char=? (list-ref (list-ref maze nr) nc) #\.))
                        (vector-set! (vector-ref visited nr) nc #t)
                        (queue-enqueue! q (list (list nr nc) (+ dist 1))))))
                  (loop))))))))
```

## Erlang

```erlang
-spec nearest_exit([[char()]], [integer()]) -> integer().
nearest_exit(Maze, Entrance) ->
    [Er, Ec] = Entrance,
    MazeMap = build_map(Maze, 0, #{}),
    M = length(Maze),
    N = case Maze of [] -> 0; [Row|_] -> length(Row) end,
    Visited0 = #{ {Er,Ec} => true },
    Queue0 = queue:in({Er,Ec,0}, queue:new()),
    try bfs(Queue0, Visited0, MazeMap, Er, Ec, M, N) of
        Res -> Res
    catch
        {found, Dist} -> Dist
    end.

build_map([], _, Acc) ->
    Acc;
build_map([Row|Rows], RIdx, Acc) ->
    Acc1 = build_row(Row, 0, RIdx, Acc),
    build_map(Rows, RIdx + 1, Acc1).

build_row([], _, _, Acc) ->
    Acc;
build_row([Cell|Cells], CIdx, RIdx, Acc) ->
    NewAcc = maps:put({RIdx, CIdx}, Cell, Acc),
    build_row(Cells, CIdx + 1, RIdx, NewAcc).

bfs(Queue, Visited, MazeMap, Er, Ec, M, N) ->
    case queue:out(Queue) of
        {{value, {R, C, D}}, RestQueue} ->
            NewDist = D + 1,
            Directions = [{1,0}, {-1,0}, {0,1}, {0,-1}],
            {NextQueue, NextVisited} =
                lists:foldl(
                    fun({DR, DC}, {QAcc, VAcc}) ->
                        NR = R + DR,
                        NC = C + DC,
                        if not in_bounds(NR, NC, M, N) ->
                                {QAcc, VAcc};
                           true ->
                                case maps:get({NR, NC}, MazeMap) of
                                    $+ -> {QAcc, VAcc};
                                    $. ->
                                        case maps:is_key({NR, NC}, VAcc) of
                                            true -> {QAcc, VAcc};
                                            false ->
                                                if is_border(NR, NC, M, N),
                                                   not (NR =:= Er andalso NC =:= Ec) ->
                                                        throw({found, NewDist});
                                                   true ->
                                                        Q1 = queue:in({NR, NC, NewDist}, QAcc),
                                                        V1 = maps:put({NR, NC}, true, VAcc),
                                                        {Q1, V1}
                                                end
                                        end
                                end
                        end
                    end,
                    {RestQueue, Visited},
                    Directions),
            bfs(NextQueue, NextVisited, MazeMap, Er, Ec, M, N);
        {empty, _} ->
            -1
    end.

in_bounds(R, C, M, N) ->
    R >= 0 andalso R < M andalso C >= 0 andalso C < N.

is_border(R, C, M, N) ->
    R =:= 0 orelse R =:= M-1 orelse C =:= 0 orelse C =:= N-1.
```

## Elixir

```elixir
defmodule Solution do
  @spec nearest_exit(maze :: [[char]], entrance :: [integer]) :: integer
  def nearest_exit(maze, entrance) do
    m = length(maze)
    n = if m == 0, do: 0, else: length(List.first(maze))
    sr = Enum.at(entrance, 0)
    sc = Enum.at(entrance, 1)

    visited = MapSet.new([{sr, sc}])
    queue = :queue.in({sr, sc, 0}, :queue.new())
    bfs(queue, visited, maze, m, n)
  end

  defp bfs(queue, visited, maze, m, n) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {r, c, dist}}, q2} ->
        dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]
        process_dirs(dirs, {q2, visited}, r, c, dist, maze, m, n)
    end
  end

  defp process_dirs([], {queue, visited}, _r, _c, _dist, maze, m, n) do
    bfs(queue, visited, maze, m, n)
  end

  defp process_dirs([{dr, dc} | rest], {queue, visited}, r, c, dist, maze, m, n) do
    nr = r + dr
    nc = c + dc

    if in_bounds?(nr, nc, m, n) do
      cell = get_in(maze, [Access.at(nr), Access.at(nc)])

      cond do
        cell == "." and not MapSet.member?(visited, {nr, nc}) ->
          new_visited = MapSet.put(visited, {nr, nc})

          if is_exit?(nr, nc, m, n) do
            dist + 1
          else
            new_queue = :queue.in({nr, nc, dist + 1}, queue)
            process_dirs(rest, {new_queue, new_visited}, r, c, dist, maze, m, n)
          end

        true ->
          process_dirs(rest, {queue, visited}, r, c, dist, maze, m, n)
      end
    else
      process_dirs(rest, {queue, visited}, r, c, dist, maze, m, n)
    end
  end

  defp in_bounds?(r, c, m, n), do: r >= 0 and r < m and c >= 0 and c < n
  defp is_exit?(r, c, m, n), do: r == 0 or r == m - 1 or c == 0 or c == n - 1
end
```

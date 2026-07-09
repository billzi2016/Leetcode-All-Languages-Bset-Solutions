# 1765. Map of Highest Peak

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int m = isWater.size();
        int n = isWater[0].size();
        vector<vector<int>> height(m, vector<int>(n, -1));
        queue<pair<int,int>> q;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (isWater[i][j] == 1) {
                    height[i][j] = 0;
                    q.emplace(i, j);
                }
            }
        }
        const int dirs[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            for (auto &d : dirs) {
                int nx = x + d[0];
                int ny = y + d[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (height[nx][ny] != -1) continue;
                height[nx][ny] = height[x][y] + 1;
                q.emplace(nx, ny);
            }
        }
        return height;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int m = isWater.length;
        int n = isWater[0].length;
        int[][] height = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(height[i], -1);
        }
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (isWater[i][j] == 1) {
                    height[i][j] = 0;
                    queue.add(new int[]{i, j});
                }
            }
        }
        int[] dirs = {0, 1, 0, -1, 0};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0], y = cur[1];
            for (int d = 0; d < 4; d++) {
                int nx = x + dirs[d];
                int ny = y + dirs[d + 1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && height[nx][ny] == -1) {
                    height[nx][ny] = height[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        return height;
    }
}
```

## Python

```python
class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.popleft()
            cur_h = heights[x][y]
            nh = cur_h + 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    heights[nx][ny] = nh
                    q.append((nx, ny))
        return heights
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    q.append((i, j))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.popleft()
            cur_h = heights[x][y]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    heights[nx][ny] = cur_h + 1
                    q.append((nx, ny))
        
        return heights
```

## C

```c
#include <stdlib.h>

int** highestPeak(int** isWater, int isWaterSize, int* isWaterColSize,
                  int* returnSize, int*** returnColumnSizes) {
    int rows = isWaterSize;
    int cols = isWaterColSize[0];
    
    *returnSize = rows;
    *returnColumnSizes = (int*)malloc(rows * sizeof(int));
    for (int i = 0; i < rows; ++i) {
        (*returnColumnSizes)[i] = cols;
    }
    
    int** height = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; ++i) {
        height[i] = (int*)malloc(cols * sizeof(int));
        for (int j = 0; j < cols; ++j) {
            height[i][j] = -1;
        }
    }
    
    int total = rows * cols;
    int* qx = (int*)malloc(total * sizeof(int));
    int* qy = (int*)malloc(total * sizeof(int));
    int front = 0, back = 0;
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (isWater[i][j] == 1) {
                height[i][j] = 0;
                qx[back] = i;
                qy[back] = j;
                ++back;
            }
        }
    }
    
    const int dx[4] = {-1, 1, 0, 0};
    const int dy[4] = {0, 0, -1, 1};
    
    while (front < back) {
        int x = qx[front];
        int y = qy[front];
        ++front;
        int curH = height[x][y];
        for (int d = 0; d < 4; ++d) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && height[nx][ny] == -1) {
                height[nx][ny] = curH + 1;
                qx[back] = nx;
                qy[back] = ny;
                ++back;
            }
        }
    }
    
    free(qx);
    free(qy);
    return height;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] HighestPeak(int[][] isWater)
    {
        int m = isWater.Length;
        int n = isWater[0].Length;

        int[][] height = new int[m][];
        var queue = new System.Collections.Generic.Queue<(int, int)>();

        for (int i = 0; i < m; i++)
        {
            height[i] = new int[n];
            for (int j = 0; j < n; j++)
            {
                if (isWater[i][j] == 1)
                {
                    height[i][j] = 0;
                    queue.Enqueue((i, j));
                }
                else
                {
                    height[i][j] = -1;
                }
            }
        }

        int[] dx = { 0, 0, 1, -1 };
        int[] dy = { 1, -1, 0, 0 };

        while (queue.Count > 0)
        {
            var (x, y) = queue.Dequeue();
            int cur = height[x][y];

            for (int d = 0; d < 4; d++)
            {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n && height[nx][ny] == -1)
                {
                    height[nx][ny] = cur + 1;
                    queue.Enqueue((nx, ny));
                }
            }
        }

        return height;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} isWater
 * @return {number[][]}
 */
var highestPeak = function(isWater) {
    const m = isWater.length;
    const n = isWater[0].length;
    const heights = Array.from({ length: m }, () => Array(n).fill(-1));
    
    // Preallocate queue arrays for performance
    const qx = new Array(m * n);
    const qy = new Array(m * n);
    let head = 0, tail = 0;
    
    // Initialize queue with all water cells (height 0)
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (isWater[i][j] === 1) {
                heights[i][j] = 0;
                qx[tail] = i;
                qy[tail] = j;
                ++tail;
            }
        }
    }
    
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    // Multi-source BFS
    while (head < tail) {
        const x = qx[head];
        const y = qy[head];
        ++head;
        const curH = heights[x][y];
        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && heights[nx][ny] === -1) {
                heights[nx][ny] = curH + 1;
                qx[tail] = nx;
                qy[tail] = ny;
                ++tail;
            }
        }
    }
    
    return heights;
};
```

## Typescript

```typescript
function highestPeak(isWater: number[][]): number[][] {
    const m = isWater.length;
    const n = isWater[0].length;
    const heights: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
    const qx: number[] = [];
    const qy: number[] = [];

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (isWater[i][j] === 1) {
                heights[i][j] = 0;
                qx.push(i);
                qy.push(j);
            }
        }
    }

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ];

    let head = 0;
    while (head < qx.length) {
        const x = qx[head];
        const y = qy[head];
        ++head;

        const curH = heights[x][y];
        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && heights[nx][ny] === -1) {
                heights[nx][ny] = curH + 1;
                qx.push(nx);
                qy.push(ny);
            }
        }
    }

    return heights;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $isWater
     * @return Integer[][]
     */
    function highestPeak($isWater) {
        $m = count($isWater);
        $n = count($isWater[0]);
        
        // Initialize height matrix with -1 (unvisited)
        $height = array_fill(0, $m, array_fill(0, $n, -1));
        
        $queue = new SplQueue();
        
        // Enqueue all water cells and set their height to 0
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                if ($isWater[$i][$j] == 1) {
                    $height[$i][$j] = 0;
                    $queue->enqueue([$i, $j]);
                }
            }
        }
        
        // Directions: up, down, left, right
        $dx = [0, 0, 1, -1];
        $dy = [1, -1, 0, 0];
        
        while (!$queue->isEmpty()) {
            [$x, $y] = $queue->dequeue();
            $currentHeight = $height[$x][$y];
            
            for ($d = 0; $d < 4; ++$d) {
                $nx = $x + $dx[$d];
                $ny = $y + $dy[$d];
                
                if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n && $height[$nx][$ny] == -1) {
                    $height[$nx][$ny] = $currentHeight + 1;
                    $queue->enqueue([$nx, $ny]);
                }
            }
        }
        
        return $height;
    }
}
```

## Swift

```swift
class Solution {
    func highestPeak(_ isWater: [[Int]]) -> [[Int]] {
        let m = isWater.count
        guard m > 0 else { return [] }
        let n = isWater[0].count
        var height = Array(repeating: Array(repeating: -1, count: n), count: m)
        var queue = [(Int, Int)]()
        queue.reserveCapacity(m * n)
        
        for i in 0..<m {
            for j in 0..<n {
                if isWater[i][j] == 1 {
                    height[i][j] = 0
                    queue.append((i, j))
                }
            }
        }
        
        var index = 0
        let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while index < queue.count {
            let (x, y) = queue[index]
            index += 1
            for d in dirs {
                let nx = x + d.0
                let ny = y + d.1
                if nx >= 0 && nx < m && ny >= 0 && ny < n && height[nx][ny] == -1 {
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))
                }
            }
        }
        
        return height
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun highestPeak(isWater: Array<IntArray>): Array<IntArray> {
        val m = isWater.size
        val n = isWater[0].size
        val height = Array(m) { IntArray(n) { -1 } }
        val total = m * n
        val qR = IntArray(total)
        val qC = IntArray(total)
        var head = 0
        var tail = 0

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (isWater[i][j] == 1) {
                    height[i][j] = 0
                    qR[tail] = i
                    qC[tail] = j
                    tail++
                }
            }
        }

        val dr = intArrayOf(1, -1, 0, 0)
        val dc = intArrayOf(0, 0, 1, -1)

        while (head < tail) {
            val r = qR[head]
            val c = qC[head]
            head++
            val curH = height[r][c] + 1
            for (d in 0..3) {
                val nr = r + dr[d]
                val nc = c + dc[d]
                if (nr in 0 until m && nc in 0 until n && height[nr][nc] == -1) {
                    height[nr][nc] = curH
                    qR[tail] = nr
                    qC[tail] = nc
                    tail++
                }
            }
        }

        return height
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<List<int>> highestPeak(List<List<int>> isWater) {
    int m = isWater.length;
    int n = isWater[0].length;

    // Initialize heights with -1 (unvisited)
    List<List<int>> height =
        List.generate(m, (_) => List.filled(n, -1));

    Queue<int> q = Queue<int>();

    // Multi-source BFS initialization: all water cells have height 0
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (isWater[i][j] == 1) {
          height[i][j] = 0;
          q.add(i * n + j);
        }
      }
    }

    const List<int> dr = [0, 0, 1, -1];
    const List<int> dc = [1, -1, 0, 0];

    while (q.isNotEmpty) {
      int pos = q.removeFirst();
      int r = pos ~/ n;
      int c = pos % n;

      for (int d = 0; d < 4; ++d) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && height[nr][nc] == -1) {
          height[nr][nc] = height[r][c] + 1;
          q.add(nr * n + nc);
        }
      }
    }

    return height;
  }
}
```

## Golang

```go
func highestPeak(isWater [][]int) [][]int {
	m := len(isWater)
	n := len(isWater[0])

	heights := make([][]int, m)
	for i := 0; i < m; i++ {
		heights[i] = make([]int, n)
		for j := 0; j < n; j++ {
			heights[i][j] = -1
		}
	}

	type cell struct{ r, c int }
	queue := make([]cell, 0, m*n)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if isWater[i][j] == 1 {
				heights[i][j] = 0
				queue = append(queue, cell{i, j})
			}
		}
	}

	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for front := 0; front < len(queue); front++ {
		cur := queue[front]
		h := heights[cur.r][cur.c]
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && heights[nr][nc] == -1 {
				heights[nr][nc] = h + 1
				queue = append(queue, cell{nr, nc})
			}
		}
	}

	return heights
}
```

## Ruby

```ruby
# @param {Integer[][]} is_water
# @return {Integer[][]}
def highest_peak(is_water)
  m = is_water.size
  n = is_water[0].size
  heights = Array.new(m) { Array.new(n, -1) }

  qx = []
  qy = []
  head = 0

  (0...m).each do |i|
    (0...n).each do |j|
      if is_water[i][j] == 1
        heights[i][j] = 0
        qx << i
        qy << j
      end
    end
  end

  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  while head < qx.size
    x = qx[head]
    y = qy[head]
    head += 1
    cur_h = heights[x][y]

    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      next unless nx.between?(0, m - 1) && ny.between?(0, n - 1)
      if heights[nx][ny] == -1
        heights[nx][ny] = cur_h + 1
        qx << nx
        qy << ny
      end
    end
  end

  heights
end
```

## Scala

```scala
object Solution {
  def highestPeak(isWater: Array[Array[Int]]): Array[Array[Int]] = {
    val m = isWater.length
    val n = if (m == 0) 0 else isWater(0).length
    val res = Array.ofDim[Int](m, n)
    for (i <- 0 until m; j <- 0 until n) res(i)(j) = -1

    import java.util.ArrayDeque
    val q: ArrayDeque[(Int, Int)] = new ArrayDeque()
    for (i <- 0 until m; j <- 0 until n) {
      if (isWater(i)(j) == 1) {
        res(i)(j) = 0
        q.add((i, j))
      }
    }

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (!q.isEmpty) {
      val (x, y) = q.poll()
      val cur = res(x)(y)
      for ((dx, dy) <- dirs) {
        val nx = x + dx
        val ny = y + dy
        if (nx >= 0 && nx < m && ny >= 0 && ny < n && res(nx)(ny) == -1) {
          res(nx)(ny) = cur + 1
          q.add((nx, ny))
        }
      }
    }

    res
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn highest_peak(is_water: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = is_water.len();
        let n = is_water[0].len();
        let mut heights = vec![vec![-1; n]; m];
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();

        for i in 0..m {
            for j in 0..n {
                if is_water[i][j] == 1 {
                    heights[i][j] = 0;
                    queue.push_back((i, j));
                }
            }
        }

        let dirs: [(i32, i32); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];

        while let Some((r, c)) = queue.pop_front() {
            let cur_h = heights[r][c];
            for (dr, dc) in dirs.iter() {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                    let ur = nr as usize;
                    let uc = nc as usize;
                    if heights[ur][uc] == -1 {
                        heights[ur][uc] = cur_h + 1;
                        queue.push_back((ur, uc));
                    }
                }
            }
        }

        heights
    }
}
```

## Racket

```racket
(define/contract (highest-peak isWater)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let* ((rows (length isWater))
         (cols (if (zero? rows) 0 (length (first isWater))))
         (heights (make-vector rows))
         (queue (make-vector (* rows cols)))
         (dx '#(0 0 1 -1))
         (dy '#(1 -1 0 0))
         (head 0)
         (tail 0))
    ;; initialize height matrix with -1
    (for ([i (in-range rows)])
      (vector-set! heights i (make-vector cols -1)))
    ;; enqueue all water cells and set their height to 0
    (for* ([i (in-range rows)]
           [j (in-range cols)])
      (when (= (list-ref (list-ref isWater i) j) 1)
        (let ((row-vec (vector-ref heights i)))
          (vector-set! row-vec j 0))
        (vector-set! queue tail (list i j))
        (set! tail (+ tail 1))))
    ;; BFS
    (let loop ()
      (when (< head tail)
        (define coord (vector-ref queue head))
        (set! head (+ head 1))
        (define i (first coord))
        (define j (second coord))
        (define cur-height (vector-ref (vector-ref heights i) j))
        (for ([d (in-range 4)])
          (define ni (+ i (vector-ref dx d)))
          (define nj (+ j (vector-ref dy d)))
          (when (and (>= ni 0) (< ni rows) (>= nj 0) (< nj cols))
            (define neighbor-row (vector-ref heights ni))
            (when (= (vector-ref neighbor-row nj) -1)
              (vector-set! neighbor-row nj (+ cur-height 1))
              (vector-set! queue tail (list ni nj))
              (set! tail (+ tail 1))))))
        (loop)))
    ;; convert result to list of lists
    (for/list ([i (in-range rows)])
      (vector->list (vector-ref heights i)))) )
```

## Erlang

```erlang
-module(solution).
-export([highest_peak/1]).

-spec highest_peak(IsWater :: [[integer()]]) -> [[integer()]].
highest_peak(IsWater) ->
    M = length(IsWater),
    N = case IsWater of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    {Queue0, Map0} = init(IsWater, 0, queue:new(), maps:new()),
    FinalMap = bfs(Queue0, Map0, M, N),
    build_result(M, N, FinalMap).

%% Initialize queue with all water cells and map with height 0 for them
init([], _RowIdx, Q, Map) ->
    {Q, Map};
init([Row|RestRows], RowIdx, QAcc, MapAcc) ->
    {QNew, MapNew} = init_row(Row, RowIdx, 0, QAcc, MapAcc),
    init(RestRows, RowIdx + 1, QNew, MapNew).

init_row([], _R, _C, Q, Map) ->
    {Q, Map};
init_row([Cell|Rest], R, C, Q, Map) ->
    case Cell of
        1 ->
            NewQ = queue:in({R, C}, Q),
            NewMap = maps:put({R, C}, 0, Map);
        _ ->
            NewQ = Q,
            NewMap = Map
    end,
    init_row(Rest, R, C + 1, NewQ, NewMap).

%% Multi-source BFS
bfs(Queue, Map, M, N) ->
    case queue:out(Queue) of
        {empty, _} ->
            Map;
        {{value, {R, C}}, Q1} ->
            H = maps:get({R, C}, Map),
            NextH = H + 1,
            {Map2, Q2} = process_neighbors([{0,1},{0,-1},{1,0},{-1,0}], R, C, NextH, Map, Q1, M, N),
            bfs(Q2, Map2, M, N)
    end.

process_neighbors([], _R, _C, _H, Map, Queue, _M, _N) ->
    {Map, Queue};
process_neighbors([{DR, DC}|Rest], R, C, H, Map, Queue, M, N) ->
    NR = R + DR,
    NC = C + DC,
    if
        NR >= 0, NR < M, NC >= 0, NC < N,
        not maps:is_key({NR, NC}, Map) ->
            NewMap = maps:put({NR, NC}, H, Map),
            NewQueue = queue:in({NR, NC}, Queue);
        true ->
            NewMap = Map,
            NewQueue = Queue
    end,
    process_neighbors(Rest, R, C, H, NewMap, NewQueue, M, N).

%% Build result matrix from map
build_result(M, N, Map) ->
    [ [ maps:get({R, C}, Map) || C <- lists:seq(0, N-1) ] ||
        R <- lists:seq(0, M-1) ].
```

## Elixir

```elixir
defmodule Solution do
  @spec highest_peak(is_water :: [[integer]]) :: [[integer]]
  def highest_peak(is_water) do
    rows = length(is_water)
    cols = is_water |> List.first() |> length()

    # Initialize heights matrix with -1
    heights =
      Enum.reduce(0..rows - 1, :array.new(rows, default: nil), fn i, outer_acc ->
        inner = :array.new(cols, default: -1)
        :array.set(i, inner, outer_acc)
      end)

    # Initialize queue with all water cells (value == 1) and set their height to 0
    {heights, queue} =
      Enum.reduce(0..rows - 1, {heights, :queue.new()}, fn i, {h_acc, q_acc} ->
        row = Enum.at(is_water, i)

        Enum.reduce(0..cols - 1, {h_acc, q_acc}, fn j, {hh, qq} ->
          if Enum.at(row, j) == 1 do
            hh2 = put(hh, i, j, 0)
            qq2 = :queue.in({i, j}, qq)
            {hh2, qq2}
          else
            {hh, qq}
          end
        end)
      end)

    # Perform multi-source BFS
    final_heights = bfs(queue, heights, rows, cols)

    # Convert the array structure back to list of lists
    for i <- 0..rows - 1 do
      row_arr = :array.get(i, final_heights)
      :array.to_list(row_arr)
    end
  end

  defp bfs(queue, heights, rows, cols) do
    case :queue.out(queue) do
      {:empty, _} ->
        heights

      {{:value, {i, j}}, q_rest} ->
        cur_h = get(heights, i, j)
        next_h = cur_h + 1

        {q_next, h_updated} =
          Enum.reduce(
            [{1, 0}, {-1, 0}, {0, 1}, {0, -1}],
            {q_rest, heights},
            fn {dx, dy}, {qq, hh} ->
              ni = i + dx
              nj = j + dy

              if ni >= 0 and ni < rows and nj >= 0 and nj < cols do
                if get(hh, ni, nj) == -1 do
                  hh2 = put(hh, ni, nj, next_h)
                  qq2 = :queue.in({ni, nj}, qq)
                  {qq2, hh2}
                else
                  {qq, hh}
                end
              else
                {qq, hh}
              end
            end
          )

        bfs(q_next, h_updated, rows, cols)
    end
  end

  defp get(matrix, i, j) do
    row = :array.get(i, matrix)
    :array.get(j, row)
  end

  defp put(matrix, i, j, val) do
    row = :array.get(i, matrix)
    new_row = :array.set(j, val, row)
    :array.set(i, new_row, matrix)
  end
end
```

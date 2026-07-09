# 0934. Shortest Bridge

## Cpp

```cpp
class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int n = grid.size();
        const vector<pair<int,int>> dirs{{-1,0},{1,0},{0,-1},{0,1}};
        deque<pair<int,int>> q;
        
        function<void(int,int)> dfs = [&](int i, int j){
            if(i<0||i>=n||j<0||j>=n||grid[i][j]!=1) return;
            grid[i][j]=2;
            q.emplace_back(i,j);
            for(auto &d:dirs) dfs(i+d.first, j+d.second);
        };
        
        bool found = false;
        for(int i=0;i<n && !found;i++){
            for(int j=0;j<n && !found;j++){
                if(grid[i][j]==1){
                    dfs(i,j);
                    found = true;
                }
            }
        }
        
        int steps = 0;
        while(!q.empty()){
            int sz = q.size();
            while(sz--){
                auto [x,y] = q.front(); q.pop_front();
                for(auto &d:dirs){
                    int nx = x + d.first, ny = y + d.second;
                    if(nx<0||nx>=n||ny<0||ny>=n) continue;
                    if(grid[nx][ny]==1) return steps;
                    if(grid[nx][ny]==0){
                        grid[nx][ny]=2;
                        q.emplace_back(nx,ny);
                    }
                }
            }
            ++steps;
        }
        return -1;
    }
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int shortestBridge(int[][] grid) {
        int n = grid.length;
        Deque<int[]> bfsQueue = new ArrayDeque<>();
        // Find first land cell
        boolean found = false;
        for (int i = 0; i < n && !found; i++) {
            for (int j = 0; j < n && !found; j++) {
                if (grid[i][j] == 1) {
                    dfsMark(grid, i, j, bfsQueue);
                    found = true;
                }
            }
        }

        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        int steps = 0;
        while (!bfsQueue.isEmpty()) {
            int size = bfsQueue.size();
            for (int s = 0; s < size; s++) {
                int[] cur = bfsQueue.poll();
                int x = cur[0], y = cur[1];
                for (int[] d : dirs) {
                    int nx = x + d[0];
                    int ny = y + d[1];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                    if (grid[nx][ny] == 1) return steps;
                    if (grid[nx][ny] == 0) {
                        grid[nx][ny] = -1; // mark visited water
                        bfsQueue.offer(new int[]{nx, ny});
                    }
                }
            }
            steps++;
        }
        return -1; // should never reach here
    }

    private void dfsMark(int[][] grid, int i, int j, Deque<int[]> queue) {
        int n = grid.length;
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{i, j});
        grid[i][j] = 2; // mark as visited island A
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int x = cur[0], y = cur[1];
            queue.offer(cur);
            if (x > 0 && grid[x - 1][y] == 1) {
                grid[x - 1][y] = 2;
                stack.push(new int[]{x - 1, y});
            }
            if (x < n - 1 && grid[x + 1][y] == 1) {
                grid[x + 1][y] = 2;
                stack.push(new int[]{x + 1, y});
            }
            if (y > 0 && grid[x][y - 1] == 1) {
                grid[x][y - 1] = 2;
                stack.push(new int[]{x, y - 1});
            }
            if (y < n - 1 && grid[x][y + 1] == 1) {
                grid[x][y + 1] = 2;
                stack.push(new int[]{x, y + 1});
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # locate first land cell
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    found = True
                    break

        # DFS to mark the first island and collect its cells
        stack = [start]
        island_cells = []
        while stack:
            x, y = stack.pop()
            if grid[x][y] != 1:
                continue
            grid[x][y] = 2
            island_cells.append((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    stack.append((nx, ny))

        # BFS from the first island outward until reaching second island
        from collections import deque
        q = deque(island_cells)
        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:   # reached second island
                            return steps
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = -1    # mark visited water
                            q.append((nx, ny))
            steps += 1
        return steps
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # locate first land cell
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    found = True
                    break

        # DFS to mark the first island and collect its cells
        stack = [start]
        island = []
        while stack:
            x, y = stack.pop()
            if grid[x][y] != 1:
                continue
            grid[x][y] = 2
            island.append((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    stack.append((nx, ny))

        # BFS from all cells of the first island
        q = deque()
        for x, y in island:
            q.append((x, y, 0))

        while q:
            x, y, d = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 1:      # reached second island
                        return d
                    if grid[nx][ny] == 0:      # water, expand outward
                        grid[nx][ny] = -1
                        q.append((nx, ny, d + 1))
        return -1
```

## C

```c
#include <stdlib.h>

int shortestBridge(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int m = gridColSize[0];
    int maxCells = n * m;

    int *qx = (int *)malloc(maxCells * sizeof(int));
    int *qy = (int *)malloc(maxCells * sizeof(int));
    int front = 0, back = 0;

    // directions
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    // DFS to mark first island and enqueue its cells
    void dfs(int x, int y) {
        if (x < 0 || x >= n || y < 0 || y >= m || grid[x][y] != 1)
            return;
        grid[x][y] = 2;                     // mark as visited island cell
        qx[back] = x;
        qy[back] = y;
        back++;                             // enqueue
        for (int d = 0; d < 4; ++d) {
            dfs(x + dx[d], y + dy[d]);
        }
    }

    // find first land cell
    int found = 0;
    for (int i = 0; i < n && !found; ++i) {
        for (int j = 0; j < m && !found; ++j) {
            if (grid[i][j] == 1) {
                dfs(i, j);
                found = 1;
            }
        }
    }

    int distance = 0;
    while (front < back) {
        int layerSize = back - front;
        for (int i = 0; i < layerSize; ++i) {
            int x = qx[front];
            int y = qy[front];
            front++;
            for (int d = 0; d < 4; ++d) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (grid[nx][ny] == 1) {          // reached second island
                    free(qx);
                    free(qy);
                    return distance;
                }
                if (grid[nx][ny] == 0) {
                    grid[nx][ny] = -1;            // mark water as visited
                    qx[back] = nx;
                    qy[back] = ny;
                    back++;
                }
            }
        }
        distance++;
    }

    free(qx);
    free(qy);
    return -1;  // should never reach here per problem constraints
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int ShortestBridge(int[][] grid) {
        int n = grid.Length;
        var q = new Queue<(int, int)>();
        bool found = false;
        for (int i = 0; i < n && !found; i++) {
            for (int j = 0; j < n && !found; j++) {
                if (grid[i][j] == 1) {
                    Dfs(grid, i, j, n, q);
                    found = true;
                }
            }
        }

        int steps = 0;
        int[] dirs = new int[] { -1, 0, 1, 0, -1 };
        while (q.Count > 0) {
            int size = q.Count;
            for (int s = 0; s < size; s++) {
                var (x, y) = q.Dequeue();
                for (int d = 0; d < 4; d++) {
                    int nx = x + dirs[d];
                    int ny = y + dirs[d + 1];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                    if (grid[nx][ny] == 1) return steps;
                    if (grid[nx][ny] == 0) {
                        grid[nx][ny] = -1; // mark visited water
                        q.Enqueue((nx, ny));
                    }
                }
            }
            steps++;
        }

        return -1; // should never reach here per problem constraints
    }

    private void Dfs(int[][] grid, int i, int j, int n, Queue<(int, int)> q) {
        if (i < 0 || j < 0 || i >= n || j >= n || grid[i][j] != 1) return;
        grid[i][j] = 2; // mark as part of first island
        q.Enqueue((i, j));
        Dfs(grid, i + 1, j, n, q);
        Dfs(grid, i - 1, j, n, q);
        Dfs(grid, i, j + 1, n, q);
        Dfs(grid, i, j - 1, n, q);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestBridge = function(grid) {
    const n = grid.length;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    // find first land cell
    let startX = -1, startY = -1;
    outer:
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                startX = i;
                startY = j;
                break outer;
            }
        }
    }
    
    // DFS to mark the first island as 2 and collect its cells
    const stack = [[startX, startY]];
    const queue = [];
    while (stack.length) {
        const [x, y] = stack.pop();
        if (x < 0 || x >= n || y < 0 || y >= n || grid[x][y] !== 1) continue;
        grid[x][y] = 2;               // mark as visited island cell
        queue.push([x, y]);           // will be BFS sources
        for (const [dx, dy] of dirs) {
            stack.push([x + dx, y + dy]);
        }
    }
    
    // BFS expansion from the first island
    let distance = 0;
    let head = 0;
    while (head < queue.length) {
        const levelSize = queue.length - head; // nodes at current distance
        for (let i = 0; i < levelSize; i++) {
            const [x, y] = queue[head++];
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] === 1) {
                    return distance; // reached second island
                }
                if (grid[nx][ny] === 0) {
                    grid[nx][ny] = -1; // mark water as visited
                    queue.push([nx, ny]);
                }
            }
        }
        distance++;
    }
    
    return distance;
};
```

## Typescript

```typescript
function shortestBridge(grid: number[][]): number {
    const n = grid.length;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let queue: [number, number][] = [];

    // Find and mark the first island using DFS (iterative)
    outer:
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                const stack: [number, number][] = [[i, j]];
                while (stack.length) {
                    const [x, y] = stack.pop()!;
                    if (x < 0 || x >= n || y < 0 || y >= n) continue;
                    if (grid[x][y] !== 1) continue;
                    grid[x][y] = 2; // mark as part of first island
                    queue.push([x, y]);
                    for (const [dx, dy] of dirs) {
                        stack.push([x + dx, y + dy]);
                    }
                }
                break outer;
            }
        }
    }

    // BFS outward from the first island to reach the second island
    let steps = 0;
    while (queue.length) {
        const next: [number, number][] = [];
        for (const [x, y] of queue) {
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] === 1) {
                    return steps; // reached second island
                }
                if (grid[nx][ny] === 0) {
                    grid[nx][ny] = -1; // visited water
                    next.push([nx, ny]);
                }
            }
        }
        queue = next;
        steps++;
    }

    return -1; // should never reach here per problem constraints
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function shortestBridge($grid) {
        $n = count($grid);
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        $queue = new SplQueue();

        // Find first island and mark it as 2, also add its cells to BFS queue
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 1) {
                    $stack = [[$i, $j]];
                    while (!empty($stack)) {
                        [$x, $y] = array_pop($stack);
                        if ($grid[$x][$y] != 1) continue;
                        $grid[$x][$y] = 2;               // mark as visited island A
                        $queue->enqueue([$x, $y]);        // add to BFS start points
                        foreach ($dirs as $d) {
                            $nx = $x + $d[0];
                            $ny = $y + $d[1];
                            if ($nx >= 0 && $nx < $n && $ny >= 0 && $ny < $n && $grid[$nx][$ny] == 1) {
                                $stack[] = [$nx, $ny];
                            }
                        }
                    }
                    // break out of both loops after first island is processed
                    $i = $n; // force outer loop termination
                    break;
                }
            }
        }

        // BFS expansion from island A to reach island B
        $distance = 0;
        while (!$queue->isEmpty()) {
            $size = $queue->count();
            for ($k = 0; $k < $size; $k++) {
                [$x, $y] = $queue->dequeue();
                foreach ($dirs as $d) {
                    $nx = $x + $d[0];
                    $ny = $y + $d[1];
                    if ($nx < 0 || $nx >= $n || $ny < 0 || $ny >= $n) continue;
                    if ($grid[$nx][$ny] == 1) {
                        return $distance; // reached second island
                    }
                    if ($grid[$nx][$ny] == 0) {
                        $grid[$nx][$ny] = -1; // mark water as visited
                        $queue->enqueue([$nx, $ny]);
                    }
                }
            }
            $distance++;
        }

        return -1; // should never reach here per problem constraints
    }
}
```

## Swift

```swift
class Solution {
    func shortestBridge(_ grid: [[Int]]) -> Int {
        var g = grid
        let n = g.count
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        // Find first land cell
        var startX = -1, startY = -1
        outer: for i in 0..<n {
            for j in 0..<n {
                if g[i][j] == 1 {
                    startX = i
                    startY = j
                    break outer
                }
            }
        }
        
        // DFS to mark the first island as 2 and collect its cells
        var stack: [(Int, Int)] = [(startX, startY)]
        g[startX][startY] = 2
        var islandCells: [(Int, Int)] = [(startX, startY)]
        
        while let (x, y) = stack.popLast() {
            for (dx, dy) in dirs {
                let nx = x + dx, ny = y + dy
                if nx >= 0 && nx < n && ny >= 0 && ny < n && g[nx][ny] == 1 {
                    g[nx][ny] = 2
                    stack.append((nx, ny))
                    islandCells.append((nx, ny))
                }
            }
        }
        
        // BFS from the first island to reach the second island
        var queue = islandCells
        var head = 0
        var steps = 0
        
        while head < queue.count {
            let currentLevelCount = queue.count - head
            for _ in 0..<currentLevelCount {
                let (x, y) = queue[head]
                head += 1
                for (dx, dy) in dirs {
                    let nx = x + dx, ny = y + dy
                    if nx < 0 || nx >= n || ny < 0 || ny >= n { continue }
                    if g[nx][ny] == 1 {
                        return steps
                    } else if g[nx][ny] == 0 {
                        g[nx][ny] = -1   // mark visited water
                        queue.append((nx, ny))
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
import java.util.ArrayDeque

class Solution {
    fun shortestBridge(grid: Array<IntArray>): Int {
        val n = grid.size
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()

        fun dfs(x: Int, y: Int) {
            if (x !in 0 until n || y !in 0 until n || grid[x][y] != 1) return
            grid[x][y] = 2
            queue.add(Pair(x, y))
            for (d in dirs) {
                dfs(x + d[0], y + d[1])
            }
        }

        outer@ for (i in 0 until n) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    dfs(i, j)
                    break@outer
                }
            }
        }

        var steps = 0
        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) {
                val (x, y) = queue.removeFirst()
                for (d in dirs) {
                    val nx = x + d[0]
                    val ny = y + d[1]
                    if (nx !in 0 until n || ny !in 0 until n) continue
                    when (grid[nx][ny]) {
                        1 -> return steps
                        0 -> {
                            grid[nx][ny] = -1
                            queue.add(Pair(nx, ny))
                        }
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
  int shortestBridge(List<List<int>> grid) {
    int n = grid.length;
    const dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    // Find first land cell and start BFS to mark the whole first island.
    Queue<List<int>> q = Queue();
    bool found = false;
    for (int i = 0; i < n && !found; ++i) {
      for (int j = 0; j < n && !found; ++j) {
        if (grid[i][j] == 1) {
          grid[i][j] = 2;
          q.add([i, j]);
          found = true;
        }
      }
    }

    // Mark all cells of the first island as 2.
    while (q.isNotEmpty) {
      var cell = q.removeFirst();
      for (var d in dirs) {
        int nx = cell[0] + d[0];
        int ny = cell[1] + d[1];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] == 1) {
          grid[nx][ny] = 2;
          q.add([nx, ny]);
        }
      }
    }

    // Multi-source BFS from the first island to reach the second.
    Queue<List<int>> bfs = Queue();
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 2) {
          bfs.add([i, j]);
        }
      }
    }

    int steps = 0;
    while (bfs.isNotEmpty) {
      int size = bfs.length;
      for (int i = 0; i < size; ++i) {
        var cell = bfs.removeFirst();
        for (var d in dirs) {
          int nx = cell[0] + d[0];
          int ny = cell[1] + d[1];
          if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
          if (grid[nx][ny] == 1) return steps;
          if (grid[nx][ny] == 0) {
            grid[nx][ny] = -1; // mark visited water
            bfs.add([nx, ny]);
          }
        }
      }
      ++steps;
    }

    return -1; // Should never reach here as per problem constraints.
  }
}
```

## Golang

```go
func shortestBridge(grid [][]int) int {
	n := len(grid)
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	type point struct{ x, y int }
	var queue []point

	// Find and mark the first island
	found := false
	for i := 0; i < n && !found; i++ {
		for j := 0; j < n && !found; j++ {
			if grid[i][j] == 1 {
				stack := []point{{i, j}}
				grid[i][j] = 2
				queue = append(queue, point{i, j})
				for len(stack) > 0 {
					cur := stack[len(stack)-1]
					stack = stack[:len(stack)-1]
					for _, d := range dirs {
						nx, ny := cur.x+d[0], cur.y+d[1]
						if nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] == 1 {
							grid[nx][ny] = 2
							stack = append(stack, point{nx, ny})
							queue = append(queue, point{nx, ny})
						}
					}
				}
				found = true
			}
		}
	}

	// BFS expansion from the first island
	steps := 0
	for len(queue) > 0 {
		next := []point{}
		for _, cur := range queue {
			for _, d := range dirs {
				nx, ny := cur.x+d[0], cur.y+d[1]
				if nx < 0 || nx >= n || ny < 0 || ny >= n {
					continue
				}
				if grid[nx][ny] == 1 { // reached second island
					return steps
				}
				if grid[nx][ny] == 0 {
					grid[nx][ny] = -1 // mark visited water
					next = append(next, point{nx, ny})
				}
			}
		}
		queue = next
		steps++
	}
	return -1
}
```

## Ruby

```ruby
def shortest_bridge(grid)
  n = grid.size
  dirs = [[1,0],[-1,0],[0,1],[0,-1]]

  # find first land cell
  start_i = nil
  start_j = nil
  (0...n).each do |i|
    break if start_i
    (0...n).each do |j|
      if grid[i][j] == 1
        start_i, start_j = i, j
        break
      end
    end
  end

  # DFS to mark first island as 2 and collect its cells
  stack = [[start_i, start_j]]
  bfs_queue = []
  while !stack.empty?
    x, y = stack.pop
    next unless grid[x][y] == 1
    grid[x][y] = 2
    bfs_queue << [x, y]
    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      if nx.between?(0, n - 1) && ny.between?(0, n - 1) && grid[nx][ny] == 1
        stack << [nx, ny]
      end
    end
  end

  # BFS outward from first island to reach second island
  steps = 0
  while !bfs_queue.empty?
    new_queue = []
    bfs_queue.each do |x, y|
      dirs.each do |dx, dy|
        nx = x + dx
        ny = y + dy
        next unless nx.between?(0, n - 1) && ny.between?(0, n - 1)
        if grid[nx][ny] == 1
          return steps
        elsif grid[nx][ny] == 0
          grid[nx][ny] = -1
          new_queue << [nx, ny]
        end
      end
    end
    bfs_queue = new_queue
    steps += 1
  end
  steps
end
```

## Scala

```scala
object Solution {
  def shortestBridge(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val dirs = Array((1,0), (-1,0), (0,1), (0,-1))

    var found = false
    var startX = 0
    var startY = 0
    var i = 0
    while (i < n && !found) {
      var j = 0
      while (j < n && !found) {
        if (grid(i)(j) == 1) {
          startX = i
          startY = j
          found = true
        }
        j += 1
      }
      i += 1
    }

    import scala.collection.mutable.ArrayDeque

    // BFS to mark the first island as 2 and collect its cells
    val queue = ArrayDeque[(Int, Int)]()
    queue.append((startX, startY))
    grid(startX)(startY) = 2
    val island = ArrayDeque[(Int, Int)]()
    island.append((startX, startY))

    while (queue.nonEmpty) {
      val (x, y) = queue.removeHead()
      for ((dx, dy) <- dirs) {
        val nx = x + dx
        val ny = y + dy
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && grid(nx)(ny) == 1) {
          grid(nx)(ny) = 2
          queue.append((nx, ny))
          island.append((nx, ny))
        }
      }
    }

    // BFS expansion from the first island to reach the second island
    var steps = 0
    val bfs = ArrayDeque[(Int, Int)]()
    bfs ++= island

    while (bfs.nonEmpty) {
      val size = bfs.size
      for (_ <- 0 until size) {
        val (x, y) = bfs.removeHead()
        for ((dx, dy) <- dirs) {
          val nx = x + dx
          val ny = y + dy
          if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
            grid(nx)(ny) match {
              case 1 => return steps
              case 0 =>
                grid(nx)(ny) = -1 // mark visited water
                bfs.append((nx, ny))
              case _ => // ignore already visited or island cells
            }
          }
        }
      }
      steps += 1
    }

    -1 // should never reach here given problem constraints
  }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_bridge(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 0 {
            return 0;
        }
        let mut grid = grid;
        let dirs = [(0i32, 1i32), (0, -1), (1, 0), (-1, 0)];
        let mut island_cells: Vec<(usize, usize)> = Vec::new();

        // Find and mark the first island
        'outer: for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 1 {
                    let mut stack = vec![(i, j)];
                    while let Some((x, y)) = stack.pop() {
                        if grid[x][y] != 1 {
                            continue;
                        }
                        grid[x][y] = 2; // mark as visited island
                        island_cells.push((x, y));
                        for &(dx, dy) in &dirs {
                            let nx = x as i32 + dx;
                            let ny = y as i32 + dy;
                            if nx >= 0 && nx < n as i32 && ny >= 0 && ny < n as i32 {
                                let ux = nx as usize;
                                let uy = ny as usize;
                                if grid[ux][uy] == 1 {
                                    stack.push((ux, uy));
                                }
                            }
                        }
                    }
                    break 'outer;
                }
            }
        }

        use std::collections::VecDeque;
        let mut queue: VecDeque<(usize, usize)> = VecDeque::from(island_cells);
        let mut steps = 0;

        // BFS expansion from the first island
        while !queue.is_empty() {
            let level_size = queue.len();
            for _ in 0..level_size {
                if let Some((x, y)) = queue.pop_front() {
                    for &(dx, dy) in &dirs {
                        let nx = x as i32 + dx;
                        let ny = y as i32 + dy;
                        if nx >= 0 && nx < n as i32 && ny >= 0 && ny < n as i32 {
                            let ux = nx as usize;
                            let uy = ny as usize;
                            match grid[ux][uy] {
                                1 => return steps as i32, // reached second island
                                0 => {
                                    grid[ux][uy] = -1; // mark water as visited
                                    queue.push_back((ux, uy));
                                }
                                _ => {}
                            }
                        }
                    }
                }
            }
            steps += 1;
        }

        0
    }
}
```

## Racket

```racket
(define/contract (shortest-bridge grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length grid))
         ;; convert to mutable vector of vectors
         (grid-vec (list->vector (map list->vector grid)))
         (dirs '((1 . 0) (-1 . 0) (0 . 1) (0 . -1))))
    (define (in-bounds? x y)
      (and (>= x 0) (< x n) (>= y 0) (< y n)))
    ;; find first land cell
    (let loop-find ((i 0) (j 0) (found #f))
      (if found
          found
          (if (= i n)
              (error "no land found")
              (if (= j n)
                  (loop-find (+ i 1) 0 #f)
                  (if (= (vector-ref (vector-ref grid-vec i) j) 1)
                      (list i j)
                      (loop-find i (+ j 1) #f))))))
    ;; dfs to mark first island as 2 and collect its cells
    (let* ((start (let loop-find ((i 0) (j 0))
                    (if (= i n)
                        (error "no land")
                        (if (= j n)
                            (loop-find (+ i 1) 0)
                            (if (= (vector-ref (vector-ref grid-vec i) j) 1)
                                (list i j)
                                (loop-find i (+ j 1)))))))
           (stack (list start))
           (island-cells '()))
      (let dfs ()
        (when (not (null? stack))
          (define-values (x y) (apply values (car stack)))
          (set! stack (cdr stack))
          (when (in-bounds? x y)
            (let ((row (vector-ref grid-vec x))
                  (val (vector-ref (vector-ref grid-vec x) y)))
              (when (= val 1)
                ;; mark as visited island
                (vector-set! row y 2)
                (set! island-cells (cons (list x y) island-cells))
                ;; push neighbors
                (for-each (lambda (d)
                            (define nx (+ x (car d)))
                            (define ny (+ y (cdr d)))
                            (when (in-bounds? nx ny)
                              (set! stack (cons (list nx ny) stack))))
                          dirs)))))
          (dfs)))
      ;; BFS expansion from island cells
      (let bfs ((frontier island-cells) (dist 0))
        (if (null? frontier)
            -1 ; should never happen
            (let ((next '()))
              (define found #f)
              (for-each
               (lambda (cell)
                 (define x (first cell))
                 (define y (second cell))
                 (for-each
                  (lambda (d)
                    (define nx (+ x (car d)))
                    (define ny (+ y (cdr d)))
                    (when (in-bounds? nx ny)
                      (let ((row (vector-ref grid-vec nx))
                            (val (vector-ref (vector-ref grid-vec nx) ny)))
                        (cond
                          [(= val 1) (set! found #t)]
                          [(= val 0)
                           (vector-set! row ny -1)
                           (set! next (cons (list nx ny) next))]))))
                  dirs))
               frontier)
              (if found
                  dist
                  (bfs next (+ dist 1)))))))))
```

## Erlang

```erlang
-spec shortest_bridge(Grid :: [[integer()]]) -> integer().
shortest_bridge(Grid) ->
    N = length(Grid),
    GridTuple = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    {StartI, StartJ} = find_first(GridTuple, N),
    {MarkedGrid, IslandCoords} = dfs(GridTuple, [{StartI, StartJ}], [], N),
    bfs(MarkedGrid, IslandCoords, 0, N).

%% ------------------------------------------------------------------
%% Find first land cell (value 1)
find_first(Grid, N) ->
    find_first_row(0, Grid, N).

find_first_row(I, Grid, N) when I < N ->
    Row = element(I + 1, Grid),
    case find_first_col(Row, 0, N) of
        {J} -> {I, J};
        none -> find_first_row(I + 1, Grid, N)
    end;
find_first_row(_, _, _) ->
    erlang:error(no_land_found).

find_first_col(_Row, J, N) when J >= N ->
    none;
find_first_col(Row, J, _N) ->
    case element(J + 1, Row) of
        1 -> {J};
        _ -> find_first_col(Row, J + 1, _N)
    end.

%% ------------------------------------------------------------------
%% Depth‑first search to mark the first island (change 1 → 2)
dfs(Grid, [], Acc, _N) ->
    {Grid, lists:reverse(Acc)};
dfs(Grid, [{I, J} | Rest], Acc, N) ->
    case get(Grid, I, J) of
        1 ->
            G2 = set(Grid, I, J, 2),
            NewStack = [{I - 1, J}, {I + 1, J}, {I, J - 1}, {I, J + 1}] ++ Rest,
            dfs(G2, NewStack, [{I, J} | Acc], N);
        _ ->
            dfs(Grid, Rest, Acc, N)
    end.

%% ------------------------------------------------------------------
%% Breadth‑first search expanding from the first island
bfs(Grid, Queue, Dist, N) ->
    bfs_loop(Grid, Queue, Dist, N).

bfs_loop(_Grid, [], _Dist, _N) ->
    -1; % should never happen
bfs_loop(Grid, Queue, Dist, N) ->
    case process_queue(Grid, Queue, [], N) of
        {true, _NewGrid, _} -> Dist;
        {false, NewGrid, NextQueue} -> bfs_loop(NewGrid, NextQueue, Dist + 1, N)
    end.

process_queue(Grid, [], AccNext, _N) ->
    {false, Grid, lists:reverse(AccNext)};
process_queue(Grid, [{I, J} | Rest], AccNext, N) ->
    case check_neighbors(Grid, I, J, N) of
        {found, NewGrid} -> {true, NewGrid, []};
        {continue, UpdatedGrid, NextCells} ->
            process_queue(UpdatedGrid, Rest, NextCells ++ AccNext, N)
    end.

check_neighbors(Grid, I, J, N) ->
    Directions = [{I - 1, J}, {I + 1, J}, {I, J - 1}, {I, J + 1}],
    check_dirs(Directions, Grid, [], N).

check_dirs([], GridAcc, NewCells, _N) ->
    {continue, GridAcc, NewCells};
check_dirs([{X, Y} | Rest], GridAcc, NewCells, N) ->
    if
        X < 0 orelse X >= N orelse Y < 0 orelse Y >= N ->
            check_dirs(Rest, GridAcc, NewCells, N);
        true ->
            Val = get(GridAcc, X, Y),
            case Val of
                1 -> {found, GridAcc};
                0 ->
                    G2 = set(GridAcc, X, Y, -1),
                    check_dirs(Rest, G2, [{X, Y} | NewCells], N);
                _ -> % already visited (-1) or part of first island (2)
                    check_dirs(Rest, GridAcc, NewCells, N)
            end
    end.

%% ------------------------------------------------------------------
%% Helper to get and set cell values in the immutable grid representation
get(Grid, I, J) ->
    Row = element(I + 1, Grid),
    element(J + 1, Row).

set(Grid, I, J, Val) ->
    Row = element(I + 1, Grid),
    NewRow = setelement(J + 1, Row, Val),
    setelement(I + 1, Grid, NewRow).
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_bridge(grid :: [[integer]]) :: integer
  def shortest_bridge(grid) do
    n = length(grid)
    m = length(hd(grid))

    # Find first land cell
    {start_i, start_j} =
      Enum.find_value(0..(n - 1), fn i ->
        case Enum.find_index(Enum.at(grid, i), &(&1 == 1)) do
          nil -> nil
          j -> {i, j}
        end
      end)

    # BFS to collect all cells of the first island
    {island_cells, _grid} = bfs_island(grid, [{start_i, start_j}], MapSet.new([{start_i, start_j}]))

    # Expand from the island cells until reaching the second island
    expand(island_cells, MapSet.new(), 0, grid)
  end

  defp bfs_island(grid, queue, visited) do
    dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]
    bfs_island(queue, visited, [], grid, dirs)
  end

  defp bfs_island([], visited, island_cells_rev, _grid, _dirs) do
    {Enum.reverse(island_cells_rev), nil}
  end

  defp bfs_island([{x, y} | rest], visited, island_cells_rev, grid, dirs) do
    new_island = [{x, y} | island_cells_rev]

    {new_queue, new_visited} =
      Enum.reduce(dirs, {rest, visited}, fn {dx, dy}, {q, v} ->
        nx = x + dx
        ny = y + dy

        if in_bounds?(grid, nx, ny) and get(grid, nx, ny) == 1 and not MapSet.member?(v, {nx, ny}) do
          {[{nx, ny} | q], MapSet.put(v, {nx, ny})}
        else
          {q, v}
        end
      end)

    bfs_island(new_queue, new_visited, new_island, grid, dirs)
  end

  defp expand(queue_cells, visited_water, distance, grid) do
    # queue for current level
    q = :queue.from_list(queue_cells)
    {next_q, new_visited, found} = process_level(q, :queue.new(), visited_water, grid, distance)

    if found != nil do
      found
    else
      expand(:queue.to_list(next_q), new_visited, distance + 1, grid)
    end
  end

  defp process_level(queue, next_queue, visited_water, grid, distance) do
    case :queue.out(queue) do
      {:empty, _} ->
        {next_queue, visited_water, nil}

      {{:value, {x, y}}, rest} ->
        dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

        {new_next_q, new_visited, found} =
          Enum.reduce(dirs, {next_queue, visited_water, nil}, fn {dx, dy},
                                                                 {nq, vw, fnd} ->
            nx = x + dx
            ny = y + dy

            cond do
              not in_bounds?(grid, nx, ny) ->
                {nq, vw, fnd}

              get(grid, nx, ny) == 1 ->
                # reached second island
                {nq, vw, distance}

              get(grid, nx, ny) == 0 and not MapSet.member?(vw, {nx, ny}) ->
                {:queue.in({nx, ny}, nq), MapSet.put(vw, {nx, ny}), fnd}

              true ->
                {nq, vw, fnd}
            end
          end)

        if found != nil do
          {new_next_q, new_visited, found}
        else
          process_level(rest, new_next_q, new_visited, grid, distance)
        end
    end
  end

  defp in_bounds?(grid, i, j) do
    i >= 0 and j >= 0 and i < length(grid) and j < length(hd(grid))
  end

  defp get(grid, i, j) do
    Enum.at(Enum.at(grid, i), j)
  end
end
```

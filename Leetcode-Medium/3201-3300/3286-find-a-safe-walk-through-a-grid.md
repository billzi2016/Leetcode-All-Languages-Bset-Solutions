# 3286. Find a Safe Walk Through a Grid

## Cpp

```cpp
class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size();
        int n = grid[0].size();
        const int INF = 1e9;
        vector<vector<int>> dist(m, vector<int>(n, INF));
        deque<pair<int,int>> dq;
        dist[0][0] = grid[0][0];
        if (grid[0][0] == 0) dq.emplace_front(0,0);
        else dq.emplace_back(0,0);
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!dq.empty()) {
            auto [x,y] = dq.front();
            dq.pop_front();
            int cur = dist[x][y];
            for (auto &d: dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx<0||ny<0||nx>=m||ny>=n) continue;
                int nd = cur + grid[nx][ny];
                if (nd < dist[nx][ny]) {
                    dist[nx][ny] = nd;
                    if (grid[nx][ny]==0) dq.emplace_front(nx,ny);
                    else dq.emplace_back(nx,ny);
                }
            }
        }
        int minUnsafe = dist[m-1][n-1];
        return minUnsafe <= health - 1;
    }
};
```

## Java

```java
class Solution {
    public boolean findSafeWalk(java.util.List<java.util.List<Integer>> grid, int health) {
        int m = grid.size();
        int n = grid.get(0).size();
        int INF = Integer.MAX_VALUE;
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) {
            java.util.Arrays.fill(dist[i], INF);
        }
        java.util.Deque<int[]> dq = new java.util.ArrayDeque<>();
        dist[0][0] = grid.get(0).get(0);
        dq.offerFirst(new int[]{0, 0});
        int[] dirs = {-1, 0, 1, 0, -1};
        while (!dq.isEmpty()) {
            int[] cur = dq.pollFirst();
            int x = cur[0], y = cur[1];
            int curDist = dist[x][y];
            for (int d = 0; d < 4; d++) {
                int nx = x + dirs[d];
                int ny = y + dirs[d + 1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                int w = grid.get(nx).get(ny);
                int nd = curDist + w;
                if (nd < dist[nx][ny]) {
                    dist[nx][ny] = nd;
                    if (w == 0) dq.offerFirst(new int[]{nx, ny});
                    else dq.offerLast(new int[]{nx, ny});
                }
            }
        }
        return dist[m - 1][n - 1] <= health - 1;
    }
}
```

## Python

```python
class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        INF = 10 ** 9
        dist = [[INF] * n for _ in range(m)]

        dq = deque()
        dist[0][0] = grid[0][0]
        dq.append((0, 0))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            i, j = dq.popleft()
            cur = dist[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nd = cur + grid[ni][nj]  # add cost if unsafe
                    if nd < dist[ni][nj]:
                        dist[ni][nj] = nd
                        if grid[ni][nj] == 0:
                            dq.appendleft((ni, nj))
                        else:
                            dq.append((ni, nj))

        return dist[m - 1][n - 1] <= health - 1
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        INF = 10 ** 9
        dist = [[INF] * n for _ in range(m)]
        dq = deque()
        dist[0][0] = grid[0][0]
        dq.append((0, 0))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            i, j = dq.popleft()
            cur = dist[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nd = cur + grid[ni][nj]
                    if nd < dist[ni][nj]:
                        dist[ni][nj] = nd
                        if grid[ni][nj] == 0:
                            dq.appendleft((ni, nj))
                        else:
                            dq.append((ni, nj))

        min_unsafe = dist[m - 1][n - 1]
        return min_unsafe <= health - 1
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int x;
    int y;
} Pos;

bool findSafeWalk(int** grid, int gridSize, int* gridColSize, int health) {
    int m = gridSize;
    int n = gridColSize[0];
    const int INF = 1e9;

    // Allocate distance matrix
    int **dist = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        dist[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) dist[i][j] = INF;
    }

    // Deque implementation
    int maxSize = m * n;
    int cap = maxSize * 4 + 5;
    Pos *dq = (Pos *)malloc(cap * sizeof(Pos));
    int head = cap / 2, tail = cap / 2 - 1; // empty

    #define EMPTY (head > tail)
    #define PUSH_FRONT(p) dq[--head] = p
    #define PUSH_BACK(p)  dq[++tail] = p
    #define POP_FRONT()   dq[head++]

    dist[0][0] = grid[0][0];
    Pos start = {0, 0};
    if (grid[0][0] == 0)
        PUSH_FRONT(start);
    else
        PUSH_BACK(start);

    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    while (!EMPTY) {
        Pos cur = POP_FRONT();
        int x = cur.x, y = cur.y;
        int curDist = dist[x][y];

        for (int d = 0; d < 4; ++d) {
            int nx = x + dirs[d][0];
            int ny = y + dirs[d][1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            int ndist = curDist + grid[nx][ny];
            if (ndist < dist[nx][ny]) {
                dist[nx][ny] = ndist;
                Pos nxt = {nx, ny};
                if (grid[nx][ny] == 0)
                    PUSH_FRONT(nxt);
                else
                    PUSH_BACK(nxt);
            }
        }
    }

    int minUnsafe = dist[m-1][n-1];
    bool result = (minUnsafe <= health - 1);

    // Free memory
    for (int i = 0; i < m; ++i) free(dist[i]);
    free(dist);
    free(dq);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public bool FindSafeWalk(IList<IList<int>> grid, int health) {
        int m = grid.Count;
        int n = grid[0].Count;
        int[,] dist = new int[m, n];
        const int INF = int.MaxValue / 2;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dist[i, j] = INF;
            }
        }

        var deque = new LinkedList<(int r, int c)>();
        dist[0, 0] = 0;
        deque.AddFirst((0, 0));

        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (deque.Count > 0) {
            var cur = deque.First.Value;
            deque.RemoveFirst();
            int r = cur.r, c = cur.c;
            int curDist = dist[r, c];

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;

                int w = grid[nr][nc]; // 0 or 1
                int nd = curDist + w;
                if (nd < dist[nr, nc]) {
                    dist[nr, nc] = nd;
                    if (w == 0) {
                        deque.AddFirst((nr, nc));
                    } else {
                        deque.AddLast((nr, nc));
                    }
                }
            }
        }

        int minUnsafe = dist[m - 1, n - 1];
        return minUnsafe <= health - 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number} health
 * @return {boolean}
 */
var findSafeWalk = function(grid, health) {
    const m = grid.length;
    const n = grid[0].length;
    const INF = 1 << 30;
    const dist = Array.from({ length: m }, () => Array(n).fill(INF));
    const dq = [];
    
    dist[0][0] = grid[0][0];
    dq.push([0, 0]); // push to back
    
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    while (dq.length) {
        const [i, j] = dq.shift(); // pop front
        const curDist = dist[i][j];
        for (const [dx, dy] of dirs) {
            const ni = i + dx;
            const nj = j + dy;
            if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
            const w = grid[ni][nj]; // 0 or 1
            if (curDist + w < dist[ni][nj]) {
                dist[ni][nj] = curDist + w;
                if (w === 0) {
                    dq.unshift([ni, nj]); // push to front
                } else {
                    dq.push([ni, nj]); // push to back
                }
            }
        }
    }
    
    return dist[m-1][n-1] <= health - 1;
};
```

## Typescript

```typescript
function findSafeWalk(grid: number[][], health: number): boolean {
    const m = grid.length;
    const n = grid[0].length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dist: number[][] = Array.from({ length: m }, () => new Array(n).fill(INF));
    // simple deque using array with push/pop at both ends
    const dq: [number, number][] = [];
    dist[0][0] = grid[0][0];
    dq.unshift([0, 0]); // start node

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    while (dq.length) {
        const [x, y] = dq.shift()!;
        const curDist = dist[x][y];
        for (const [dx, dy] of dirs) {
            const nx = x + dx;
            const ny = y + dy;
            if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
            const nd = curDist + grid[nx][ny];
            if (nd < dist[nx][ny]) {
                dist[nx][ny] = nd;
                if (grid[nx][ny] === 0) {
                    dq.unshift([nx, ny]); // zero cost edge
                } else {
                    dq.push([nx, ny]);   // cost 1 edge
                }
            }
        }
    }

    const minCost = dist[m - 1][n - 1];
    return minCost <= health - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $health
     * @return Boolean
     */
    function findSafeWalk($grid, $health) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $m, array_fill(0, $n, $INF));

        $deque = new SplDoublyLinkedList();
        // start cell cost includes its own safety
        $dist[0][0] = $grid[0][0];
        if ($grid[0][0] == 0) {
            $deque->unshift([0, 0]); // front
        } else {
            $deque->push([0, 0]);    // back
        }

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        while (!$deque->isEmpty()) {
            [$x, $y] = $deque->shift(); // pop from front
            $curDist = $dist[$x][$y];
            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) continue;
                $weight = $grid[$nx][$ny]; // 0 or 1
                $newDist = $curDist + $weight;
                if ($newDist < $dist[$nx][$ny]) {
                    $dist[$nx][$ny] = $newDist;
                    if ($weight == 0) {
                        $deque->unshift([$nx, $ny]); // front for 0-weight edge
                    } else {
                        $deque->push([$nx, $ny]);    // back for 1-weight edge
                    }
                }
            }
        }

        $minUnsafe = $dist[$m-1][$n-1];
        return $minUnsafe <= $health - 1;
    }
}
```

## Swift

```swift
import Foundation

struct MinHeap {
    private var heap: [(cost: Int, x: Int, y: Int)] = []
    
    mutating func push(_ element: (Int, Int, Int)) {
        heap.append((cost: element.0, x: element.1, y: element.2))
        siftUp(heap.count - 1)
    }
    
    mutating func pop() -> (Int, Int, Int)? {
        guard !heap.isEmpty else { return nil }
        let top = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            siftDown(0)
        }
        return (top.cost, top.x, top.y)
    }
    
    var isEmpty: Bool {
        return heap.isEmpty
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) >> 1
            if heap[child].cost < heap[parent].cost {
                heap.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < heap.count && heap[left].cost < heap[smallest].cost {
                smallest = left
            }
            if right < heap.count && heap[right].cost < heap[smallest].cost {
                smallest = right
            }
            if smallest == parent { break }
            heap.swapAt(parent, smallest)
            parent = smallest
        }
    }
}

class Solution {
    func findSafeWalk(_ grid: [[Int]], _ health: Int) -> Bool {
        let m = grid.count
        let n = grid[0].count
        var dist = Array(repeating: Array(repeating: Int.max, count: n), count: m)
        var heap = MinHeap()
        
        dist[0][0] = grid[0][0]
        heap.push((dist[0][0], 0, 0))
        
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while !heap.isEmpty {
            guard let (cost, x, y) = heap.pop() else { break }
            if cost != dist[x][y] { continue }
            if x == m - 1 && y == n - 1 { break } // reached target with minimal cost
            for d in dirs {
                let nx = x + d.0
                let ny = y + d.1
                if nx < 0 || nx >= m || ny < 0 || ny >= n { continue }
                let newCost = cost + grid[nx][ny]
                if newCost < dist[nx][ny] {
                    dist[nx][ny] = newCost
                    heap.push((newCost, nx, ny))
                }
            }
        }
        
        let minUnsafe = dist[m - 1][n - 1]
        return minUnsafe <= health - 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSafeWalk(grid: List<List<Int>>, health: Int): Boolean {
        val m = grid.size
        val n = grid[0].size
        val INF = Int.MAX_VALUE / 4
        val dist = Array(m) { IntArray(n) { INF } }
        val deque = java.util.ArrayDeque<Pair<Int, Int>>()
        dist[0][0] = grid[0][0]
        deque.addFirst(0 to 0)
        val dirs = intArrayOf(-1, 0, 1, 0, -1)
        while (deque.isNotEmpty()) {
            val (x, y) = deque.removeFirst()
            val cur = dist[x][y]
            for (k in 0 until 4) {
                val nx = x + dirs[k]
                val ny = y + dirs[k + 1]
                if (nx !in 0 until m || ny !in 0 until n) continue
                val w = grid[nx][ny]
                val nd = cur + w
                if (nd < dist[nx][ny]) {
                    dist[nx][ny] = nd
                    if (w == 0) deque.addFirst(nx to ny) else deque.addLast(nx to ny)
                }
            }
        }
        return dist[m - 1][n - 1] <= health - 1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  bool findSafeWalk(List<List<int>> grid, int health) {
    int m = grid.length;
    int n = grid[0].length;
    const int INF = 1 << 30;

    List<List<int>> dist =
        List.generate(m, (_) => List.filled(n, INF), growable: false);

    var dq = DoubleLinkedQueue<_Pos>();
    int startCost = grid[0][0];
    dist[0][0] = startCost;
    if (startCost == 0) {
      dq.addFirst(_Pos(0, 0));
    } else {
      dq.addLast(_Pos(0, 0));
    }

    const List<int> dirs = [-1, 0, 1, 0, -1];
    while (dq.isNotEmpty) {
      var cur = dq.removeFirst();
      int x = cur.x;
      int y = cur.y;
      int curDist = dist[x][y];

      for (int k = 0; k < 4; ++k) {
        int nx = x + dirs[k];
        int ny = y + dirs[k + 1];
        if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
        int ndist = curDist + grid[nx][ny];
        if (ndist < dist[nx][ny]) {
          dist[nx][ny] = ndist;
          if (grid[nx][ny] == 0) {
            dq.addFirst(_Pos(nx, ny));
          } else {
            dq.addLast(_Pos(nx, ny));
          }
        }
      }
    }

    int minCost = dist[m - 1][n - 1];
    return minCost <= health - 1;
  }
}

class _Pos {
  final int x;
  final int y;
  const _Pos(this.x, this.y);
}
```

## Golang

```go
import "container/list"

func findSafeWalk(grid [][]int, health int) bool {
	m, n := len(grid), len(grid[0])
	const INF = int(^uint(0) >> 1)

	dist := make([][]int, m)
	for i := 0; i < m; i++ {
		dist[i] = make([]int, n)
		for j := 0; j < n; j++ {
			dist[i][j] = INF
		}
	}

	dq := list.New()
	dist[0][0] = grid[0][0]
	if grid[0][0] == 0 {
		dq.PushFront([2]int{0, 0})
	} else {
		dq.PushBack([2]int{0, 0})
	}

	dir := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for dq.Len() > 0 {
		e := dq.Front()
		dq.Remove(e)
		cur := e.Value.([2]int)
		x, y := cur[0], cur[1]
		curDist := dist[x][y]

		for _, d := range dir {
			nx, ny := x+d[0], y+d[1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			newDist := curDist + grid[nx][ny]
			if newDist < dist[nx][ny] {
				dist[nx][ny] = newDist
				if grid[nx][ny] == 0 {
					dq.PushFront([2]int{nx, ny})
				} else {
					dq.PushBack([2]int{nx, ny})
				}
			}
		}
	}

	minUnsafe := dist[m-1][n-1]
	return minUnsafe <= health-1
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(item)
    @data << item
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    top
  end

  def empty?
    @data.empty?
  end

  private

  def sift_up(i)
    while i > 0
      p = (i - 1) / 2
      break if @data[p][0] <= @data[i][0]
      @data[p], @data[i] = @data[i], @data[p]
      i = p
    end
  end

  def sift_down(i)
    n = @data.size
    loop do
      l = i * 2 + 1
      r = i * 2 + 2
      smallest = i
      smallest = l if l < n && @data[l][0] < @data[smallest][0]
      smallest = r if r < n && @data[r][0] < @data[smallest][0]
      break if smallest == i
      @data[i], @data[smallest] = @data[smallest], @data[i]
      i = smallest
    end
  end
end

# @param {Integer[][]} grid
# @param {Integer} health
# @return {Boolean}
def find_safe_walk(grid, health)
  m = grid.size
  n = grid[0].size
  INF = 1 << 30
  dist = Array.new(m) { Array.new(n, INF) }

  heap = MinHeap.new
  start_cost = grid[0][0]
  dist[0][0] = start_cost
  heap.push([start_cost, 0, 0])

  dirs = [[1,0],[-1,0],[0,1],[0,-1]]

  until heap.empty?
    cost, x, y = heap.pop
    next if cost != dist[x][y]

    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      next unless nx.between?(0, m - 1) && ny.between?(0, n - 1)
      new_cost = cost + grid[nx][ny]
      if new_cost < dist[nx][ny]
        dist[nx][ny] = new_cost
        heap.push([new_cost, nx, ny])
      end
    end
  end

  min_unsafe = dist[m - 1][n - 1]
  min_unsafe <= health - 1
end
```

## Scala

```scala
import java.util.ArrayDeque

object Solution {
  def findSafeWalk(grid: List[List[Int]], health: Int): Boolean = {
    val m = grid.length
    val n = grid.head.length
    val arr = grid.map(_.toArray).toArray

    val dist = Array.fill(m)(Array.fill(n)(Int.MaxValue))
    val deque = new ArrayDeque[(Int, Int)]()

    dist(0)(0) = arr(0)(0)
    if (arr(0)(0) == 0) deque.addFirst((0, 0)) else deque.addLast((0, 0))

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (!deque.isEmpty) {
      val (x, y) = deque.pollFirst()
      val curDist = dist(x)(y)

      for ((dx, dy) <- dirs) {
        val nx = x + dx
        val ny = y + dy
        if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
          val w = arr(nx)(ny)
          val nd = curDist + w
          if (nd < dist(nx)(ny)) {
            dist(nx)(ny) = nd
            if (w == 0) deque.addFirst((nx, ny))
            else deque.addLast((nx, ny))
          }
        }
      }
    }

    val minCost = dist(m - 1)(n - 1)
    health > minCost
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_safe_walk(grid: Vec<Vec<i32>>, health: i32) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        // distance = minimal number of unsafe cells (value 1) visited, including start cell
        let mut dist = vec![vec![i32::MAX; n]; m];
        dist[0][0] = grid[0][0];

        use std::collections::VecDeque;
        let mut deque: VecDeque<(usize, usize)> = VecDeque::new();
        deque.push_back((0, 0));

        let dirs = [(1_i32, 0_i32), (-1, 0), (0, 1), (0, -1)];

        while let Some((x, y)) = deque.pop_front() {
            let cur = dist[x][y];
            for &(dx, dy) in &dirs {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx < 0 || ny < 0 || nx >= m as i32 || ny >= n as i32 {
                    continue;
                }
                let ux = nx as usize;
                let uy = ny as usize;
                let w = grid[ux][uy]; // 0 or 1
                let ndist = cur + w;
                if ndist < dist[ux][uy] {
                    dist[ux][uy] = ndist;
                    if w == 0 {
                        deque.push_front((ux, uy));
                    } else {
                        deque.push_back((ux, uy));
                    }
                }
            }
        }

        let min_cost = dist[m - 1][n - 1];
        // need health after reductions to be at least 1
        min_cost <= health - 1
    }
}
```

## Racket

```racket
(define (find-safe-walk grid health)
  (let* ([m (length grid)]
         [n (if (= m 0) 0 (length (first grid)))]
         [total (* m n)]
         [INF 1000000000]
         [dist (make-vector total INF)]
         [visited (make-vector total #f)]
         [idx (lambda (r c) (+ (* r n) c))]
         [start-idx (idx 0 0)]
         [target-idx (idx (- m 1) (- n 1))])
    ;; initial cost includes the starting cell
    (vector-set! dist start-idx (list-ref (list-ref grid 0) 0))
    (let loop ()
      (define min-dist INF)
      (define u -1)
      (for ([i total])
        (when (and (not (vector-ref visited i))
                   (< (vector-ref dist i) min-dist))
          (set! min-dist (vector-ref dist i))
          (set! u i)))
      (if (= u -1)
          (void) ; all reachable nodes processed
          (begin
            (vector-set! visited u #t)
            (let* ([r (quotient u n)]
                   [c (remainder u n)])
              (for ([dr '(-1 0 1 0)] [dc '(0 1 0 -1)])
                (define nr (+ r dr))
                (define nc (+ c dc))
                (when (and (>= nr 0) (< nr m) (>= nc 0) (< nc n))
                  (let ([v (idx nr nc)])
                    (unless (vector-ref visited v)
                      (define new-dist
                        (+ (vector-ref dist u)
                           (list-ref (list-ref grid nr) nc)))
                      (when (< new-dist (vector-ref dist v))
                        (vector-set! dist v new-dist))))))))
            (loop)))))
    (<= (vector-ref dist target-idx) (- health 1))))
```

## Erlang

```erlang
-module(solution).
-export([find_safe_walk/2]).

-spec find_safe_walk(Grid :: [[integer()]], Health :: integer()) -> boolean().
find_safe_walk(Grid, Health) ->
    M = length(Grid),
    N = length(lists:nth(1, Grid)),
    StartCost = get_cell(Grid, 0, 0),
    MaxAllowed = Health - 1,
    case StartCost =< MaxAllowed of
        false -> false;
        true ->
            Dist0 = maps:put({0, 0}, StartCost, #{}),
            Deque0 = queue:in_r({0, 0}, queue:new()),
            bfs(Grid, M, N, Dist0, Deque0, MaxAllowed)
    end.

bfs(_Grid, _M, _N, _DistMap, Deque, _MaxAllowed) ->
    case queue:out(Deque) of
        empty -> false;
        {{value, {X, Y}}, Deque1} ->
            Dist = maps:get({X, Y}, _DistMap),
            if X == _M - 1 andalso Y == _N - 1 ->
                    Dist =< _MaxAllowed;
               true ->
                    Neigh = [{X - 1, Y}, {X + 1, Y}, {X, Y - 1}, {X, Y + 1}],
                    {DistMap2, Deque2} = process_neighbors(Neigh, _Grid, _M, _N,
                                                          Dist, _DistMap, Deque1),
                    bfs(_Grid, _M, _N, DistMap2, Deque2, _MaxAllowed)
            end
    end.

process_neighbors([], _Grid, _M, _N, _CurDist, DistMap, Deque) ->
    {DistMap, Deque};
process_neighbors([{NX, NY} | Rest], Grid, M, N, CurDist, DistMap, Deque) ->
    if NX >= 0, NX < M, NY >= 0, NY < N ->
            CellCost = get_cell(Grid, NX, NY),
            NewDist = CurDist + CellCost,
            OldDist = maps:get({NX, NY}, DistMap, 1000000),
            if NewDist < OldDist ->
                    DistMap1 = maps:put({NX, NY}, NewDist, DistMap),
                    Deque1 = case CellCost of
                                 0 -> queue:in_r({NX, NY}, Deque);
                                 _ -> queue:in({NX, NY}, Deque)
                             end,
                    process_neighbors(Rest, Grid, M, N, CurDist, DistMap1, Deque1);
               true ->
                    process_neighbors(Rest, Grid, M, N, CurDist, DistMap, Deque)
            end;
       true ->
            process_neighbors(Rest, Grid, M, N, CurDist, DistMap, Deque)
    end.

get_cell(Grid, X, Y) ->
    Row = lists:nth(X + 1, Grid),
    lists:nth(Y + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_safe_walk(grid :: [[integer]], health :: integer) :: boolean
  def find_safe_walk(grid, health) do
    rows = length(grid)
    cols = length(List.first(grid))

    cells =
      for r <- 0..rows - 1,
          c <- 0..cols - 1,
          into: %{},
          do: {{r, c}, Enum.at(Enum.at(grid, r), c)}

    start_cost = Map.get(cells, {0, 0})
    dist = %{{0, 0} => start_cost}
    queue = :queue.new() |> :queue.in({0, 0})

    final_dist = bfs(queue, dist, cells, rows, cols)
    min_unsafe = Map.get(final_dist, {rows - 1, cols - 1}, :infinity)

    min_unsafe <= health - 1
  end

  defp bfs(queue, dist, cells, rows, cols) do
    case :queue.out(queue) do
      {:empty, _} ->
        dist

      {{:value, {r, c}}, q2} ->
        cur = Map.get(dist, {r, c})
        dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

        {new_dist, new_queue} =
          Enum.reduce(dirs, {dist, q2}, fn {dr, dc}, {dacc, qacc} ->
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols do
              {dacc, qacc}
            else
              key = {nr, nc}
              cell_val = Map.get(cells, key)
              cost = cur + cell_val
              prev = Map.get(dacc, key, :infinity)

              if cost < prev do
                dnew = Map.put(dacc, key, cost)

                qnew =
                  if cell_val == 0 do
                    :queue.in_r(key, qacc)
                  else
                    :queue.in(key, qacc)
                  end

                {dnew, qnew}
              else
                {dacc, qacc}
              end
            end
          end)

        bfs(new_queue, new_dist, cells, rows, cols)
    end
  end
end
```

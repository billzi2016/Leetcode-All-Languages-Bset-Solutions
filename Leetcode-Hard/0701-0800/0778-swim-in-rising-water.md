# 0778. Swim in Rising Water

## Cpp

```cpp
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        const int INF = 1e9;
        vector<vector<int>> dist(n, vector<int>(n, INF));
        using T = tuple<int,int,int>;
        priority_queue<T, vector<T>, greater<T>> pq;
        dist[0][0] = grid[0][0];
        pq.emplace(dist[0][0], 0, 0);
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.empty()) {
            auto [d, x, y] = pq.top(); pq.pop();
            if (x == n-1 && y == n-1) return d;
            if (d != dist[x][y]) continue;
            for (auto &dir : dirs) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                int nd = max(d, grid[nx][ny]);
                if (nd < dist[nx][ny]) {
                    dist[nx][ny] = nd;
                    pq.emplace(nd, nx, ny);
                }
            }
        }
        return -1; // should never reach here
    }
};
```

## Java

```java
class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        boolean[][] visited = new boolean[n][n];
        java.util.PriorityQueue<int[]> pq = new java.util.PriorityQueue<>(
            (a, b) -> Integer.compare(a[0], b[0])
        );
        pq.offer(new int[]{grid[0][0], 0, 0});
        int ans = 0;
        int[] dirs = {-1, 0, 1, 0, -1};
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int h = cur[0];
            int x = cur[1];
            int y = cur[2];
            if (visited[x][y]) continue;
            visited[x][y] = true;
            ans = Math.max(ans, h);
            if (x == n - 1 && y == n - 1) return ans;
            for (int k = 0; k < 4; ++k) {
                int nx = x + dirs[k];
                int ny = y + dirs[k + 1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                    pq.offer(new int[]{grid[nx][ny], nx, ny});
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            t, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == n - 1 and y == n - 1:
                return t
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(heap, (max(t, grid[nx][ny]), nx, ny))
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (time needed to reach cell, x, y)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            t, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == n - 1 and y == n - 1:
                return t
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(heap, (max(t, grid[nx][ny]), nx, ny))
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int x;
    int y;
    int cost;
} Node;

int swimInWater(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int total = n * n;

    int *dist = (int *)malloc(total * sizeof(int));
    for (int i = 0; i < total; ++i) dist[i] = INT_MAX;

    Node *heap = (Node *)malloc((total + 5) * sizeof(Node));
    int heapSize = 0;

    // push start node
    int startCost = grid[0][0];
    dist[0] = startCost;
    heap[++heapSize] = (Node){0, 0, startCost};

    while (heapSize) {
        // pop min
        Node cur = heap[1];
        heap[1] = heap[heapSize--];

        // down-heap
        int i = 1;
        while (1) {
            int l = i * 2, r = l + 1, smallest = i;
            if (l <= heapSize && heap[l].cost < heap[smallest].cost) smallest = l;
            if (r <= heapSize && heap[r].cost < heap[smallest].cost) smallest = r;
            if (smallest == i) break;
            Node tmp = heap[i];
            heap[i] = heap[smallest];
            heap[smallest] = tmp;
            i = smallest;
        }

        int x = cur.x, y = cur.y, curCost = cur.cost;

        if (x == n - 1 && y == n - 1) {
            free(dist);
            free(heap);
            return curCost;
        }

        if (curCost != dist[x * n + y]) continue; // outdated entry

        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        for (int d = 0; d < 4; ++d) {
            int nx = x + dirs[d][0];
            int ny = y + dirs[d][1];
            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                int newCost = grid[nx][ny] > curCost ? grid[nx][ny] : curCost;
                int idx = nx * n + ny;
                if (newCost < dist[idx]) {
                    dist[idx] = newCost;
                    heap[++heapSize] = (Node){nx, ny, newCost};
                    // up-heap
                    int j = heapSize;
                    while (j > 1) {
                        int p = j / 2;
                        if (heap[p].cost <= heap[j].cost) break;
                        Node tmp = heap[p];
                        heap[p] = heap[j];
                        heap[j] = tmp;
                        j = p;
                    }
                }
            }
        }
    }

    free(dist);
    free(heap);
    return -1; // unreachable (should not happen)
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int SwimInWater(int[][] grid) {
        int n = grid.Length;
        bool[,] visited = new bool[n, n];
        var pq = new PriorityQueue<int, int>(); // element: encoded position, priority: cell height
        pq.Enqueue(0, grid[0][0]); // start at (0,0)
        visited[0, 0] = true;

        int time = 0;
        int[] dirs = { 1, 0, -1, 0, 1 };

        while (pq.Count > 0) {
            int idx = pq.Dequeue();
            int x = idx / n;
            int y = idx % n;

            time = Math.Max(time, grid[x][y]);
            if (x == n - 1 && y == n - 1) return time;

            for (int k = 0; k < 4; k++) {
                int nx = x + dirs[k];
                int ny = y + dirs[k + 1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx, ny]) {
                    visited[nx, ny] = true;
                    pq.Enqueue(nx * n + ny, grid[nx][ny]);
                }
            }
        }

        return -1; // unreachable (problem guarantees a path)
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var swimInWater = function(grid) {
    const n = grid.length;
    if (n === 1) return grid[0][0];
    const visited = Array.from({ length: n }, () => Array(n).fill(false));
    
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(item) {
            this.heap.push(item);
            this._siftUp(this.heap.length - 1);
        }
        pop() {
            if (this.heap.length === 0) return null;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this._siftDown(0);
            }
            return top;
        }
        _siftUp(idx) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        _siftDown(idx) {
            const len = this.heap.length;
            while (true) {
                let left = idx * 2 + 1,
                    right = left + 1,
                    smallest = idx;
                if (left < len && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < len && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }
    
    const heap = new MinHeap();
    heap.push([grid[0][0], 0, 0]);
    visited[0][0] = true;
    let answer = 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    while (heap.size()) {
        const [elev, x, y] = heap.pop();
        if (elev > answer) answer = elev;
        if (x === n - 1 && y === n - 1) return answer;
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                visited[nx][ny] = true;
                heap.push([grid[nx][ny], nx, ny]);
            }
        }
    }
    return answer;
};
```

## Typescript

```typescript
function swimInWater(grid: number[][]): number {
    const n = grid.length;
    const visited: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    class MinHeap {
        data: number[][];
        constructor() { this.data = []; }
        push(item: number[]) {
            this.data.push(item);
            this.bubbleUp(this.data.length - 1);
        }
        bubbleUp(idx: number) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.data[parent][0] <= this.data[idx][0]) break;
                [this.data[parent], this.data[idx]] = [this.data[idx], this.data[parent]];
                idx = parent;
            }
        }
        pop(): number[] | undefined {
            if (this.data.length === 0) return undefined;
            const top = this.data[0];
            const end = this.data.pop()!;
            if (this.data.length > 0) {
                this.data[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }
        bubbleDown(idx: number) {
            const length = this.data.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < length && this.data[left][0] < this.data[smallest][0]) smallest = left;
                if (right < length && this.data[right][0] < this.data[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.data[smallest], this.data[idx]] = [this.data[idx], this.data[smallest]];
                idx = smallest;
            }
        }
        size(): number { return this.data.length; }
    }

    const heap = new MinHeap();
    heap.push([grid[0][0], 0, 0]);
    visited[0][0] = true;
    let answer = 0;

    while (heap.size() > 0) {
        const cur = heap.pop()!;
        const val = cur[0];
        const x = cur[1];
        const y = cur[2];
        if (val > answer) answer = val;
        if (x === n - 1 && y === n - 1) return answer;
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                visited[nx][ny] = true;
                heap.push([grid[nx][ny], nx, ny]);
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
    function swimInWater($grid) {
        $n = count($grid);
        $low = max($grid[0][0], $grid[$n - 1][$n - 1]);
        $high = $n * $n - 1;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canReach($grid, $mid)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }

    private function canReach($grid, $t) {
        $n = count($grid);
        if ($grid[0][0] > $t) {
            return false;
        }
        $visited = array_fill(0, $n, array_fill(0, $n, false));
        $queue = new SplQueue();
        $queue->enqueue([0, 0]);
        $visited[0][0] = true;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (!$queue->isEmpty()) {
            [$x, $y] = $queue->dequeue();
            if ($x == $n - 1 && $y == $n - 1) {
                return true;
            }
            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx >= 0 && $nx < $n && $ny >= 0 && $ny < $n &&
                    !$visited[$nx][$ny] && $grid[$nx][$ny] <= $t) {
                    $visited[$nx][$ny] = true;
                    $queue->enqueue([$nx, $ny]);
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    struct Node {
        let val: Int
        let x: Int
        let y: Int
    }
    
    struct MinHeap {
        private var data = [Node]()
        
        var isEmpty: Bool { data.isEmpty }
        
        mutating func push(_ node: Node) {
            data.append(node)
            siftUp(data.count - 1)
        }
        
        mutating func pop() -> Node {
            let top = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                siftDown(0)
            }
            return top
        }
        
        private mutating func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) / 2
                if data[child].val < data[parent].val {
                    data.swapAt(child, parent)
                    child = parent
                } else { break }
            }
        }
        
        private mutating func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < data.count && data[left].val < data[smallest].val {
                    smallest = left
                }
                if right < data.count && data[right].val < data[smallest].val {
                    smallest = right
                }
                if smallest == parent { break }
                data.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }
    
    func swimInWater(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var visited = Array(repeating: Array(repeating: false, count: n), count: n)
        var heap = MinHeap()
        heap.push(Node(val: grid[0][0], x: 0, y: 0))
        visited[0][0] = true
        var answer = 0
        let dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while !heap.isEmpty {
            let cur = heap.pop()
            answer = max(answer, cur.val)
            if cur.x == n - 1 && cur.y == n - 1 {
                return answer
            }
            for d in dirs {
                let nx = cur.x + d.0
                let ny = cur.y + d.1
                if nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny] {
                    visited[nx][ny] = true
                    heap.push(Node(val: grid[nx][ny], x: nx, y: ny))
                }
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    data class Cell(val height: Int, val x: Int, val y: Int)

    fun swimInWater(grid: Array<IntArray>): Int {
        val n = grid.size
        if (n == 1) return grid[0][0]

        val visited = Array(n) { BooleanArray(n) }
        val dirs = intArrayOf(0, 1, 0, -1, 0)
        var time = 0

        val pq = java.util.PriorityQueue<Cell>(compareBy { it.height })
        pq.offer(Cell(grid[0][0], 0, 0))

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (visited[cur.x][cur.y]) continue
            visited[cur.x][cur.y] = true
            time = kotlin.math.max(time, cur.height)
            if (cur.x == n - 1 && cur.y == n - 1) return time

            for (k in 0 until 4) {
                val nx = cur.x + dirs[k]
                val ny = cur.y + dirs[k + 1]
                if (nx in 0 until n && ny in 0 until n && !visited[nx][ny]) {
                    pq.offer(Cell(grid[nx][ny], nx, ny))
                }
            }
        }
        return time
    }
}
```

## Dart

```dart
import 'dart:collection';
import 'dart:math';

class Cell {
  final int x;
  final int y;
  final int time;
  Cell(this.x, this.y, this.time);
}

class Solution {
  int swimInWater(List<List<int>> grid) {
    final n = grid.length;
    final visited = List.generate(n, (_) => List.filled(n, false));
    final pq = HeapPriorityQueue<Cell>((a, b) => a.time.compareTo(b.time));

    pq.add(Cell(0, 0, grid[0][0]));

    const dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    while (pq.isNotEmpty) {
      final cur = pq.removeFirst();
      final x = cur.x;
      final y = cur.y;
      final t = cur.time;

      if (visited[x][y]) continue;
      visited[x][y] = true;

      if (x == n - 1 && y == n - 1) return t;

      for (final d in dirs) {
        final nx = x + d[0];
        final ny = y + d[1];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
          final nt = max(t, grid[nx][ny]);
          pq.add(Cell(nx, ny, nt));
        }
      }
    }

    return -1; // unreachable (problem guarantees a solution)
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type item struct {
	x, y int
	val  int
}

type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].val < h[j].val }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func swimInWater(grid [][]int) int {
	n := len(grid)
	if n == 0 {
		return 0
	}
	visited := make([][]bool, n)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	h := &minHeap{}
	heap.Push(h, item{0, 0, grid[0][0]})
	visited[0][0] = true

	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		if cur.x == n-1 && cur.y == n-1 {
			return cur.val
		}
		for _, d := range dir {
			nx, ny := cur.x+d[0], cur.y+d[1]
			if nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny] {
				newVal := cur.val
				if grid[nx][ny] > newVal {
					newVal = grid[nx][ny]
				}
				heap.Push(h, item{nx, ny, newVal})
				visited[nx][ny] = true
			}
		}
	}
	return -1
}
```

## Ruby

```ruby
def heappush(heap, item)
  heap << item
  i = heap.size - 1
  while i > 0
    parent = (i - 1) / 2
    break if heap[parent][0] <= heap[i][0]
    heap[parent], heap[i] = heap[i], heap[parent]
    i = parent
  end
end

def heappop(heap)
  top = heap[0]
  last = heap.pop
  unless heap.empty?
    heap[0] = last
    i = 0
    size = heap.size
    loop do
      l = i * 2 + 1
      r = i * 2 + 2
      smallest = i
      smallest = l if l < size && heap[l][0] < heap[smallest][0]
      smallest = r if r < size && heap[r][0] < heap[smallest][0]
      break if smallest == i
      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
  end
  top
end

# @param {Integer[][]} grid
# @return {Integer}
def swim_in_water(grid)
  n = grid.size
  return grid[0][0] if n == 1

  visited = Array.new(n) { Array.new(n, false) }
  heap = []
  heappush(heap, [grid[0][0], 0, 0])

  dirs = [[1,0],[-1,0],[0,1],[0,-1]]

  until heap.empty?
    cost, x, y = heappop(heap)
    next if visited[x][y]
    return cost if x == n - 1 && y == n - 1
    visited[x][y] = true

    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      next unless nx.between?(0, n-1) && ny.between?(0, n-1)
      next if visited[nx][ny]
      new_cost = [cost, grid[nx][ny]].max
      heappush(heap, [new_cost, nx, ny])
    end
  end
end
```

## Scala

```scala
object Solution {
  import java.util.PriorityQueue

  def swimInWater(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    if (n == 1) return grid(0)(0)

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    val visited = Array.ofDim[Boolean](n, n)
    val pq = new PriorityQueue[Array[Int]](
      (a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(0), b(0))
    )

    pq.offer(Array(grid(0)(0), 0, 0))
    var answer = 0

    while (!pq.isEmpty) {
      val cur = pq.poll()
      val time = cur(0)
      val i = cur(1)
      val j = cur(2)

      if (visited(i)(j)) {
        // skip already processed cell
      } else {
        visited(i)(j) = true
        answer = math.max(answer, time)

        if (i == n - 1 && j == n - 1) return answer

        for ((dx, dy) <- dirs) {
          val ni = i + dx
          val nj = j + dy
          if (ni >= 0 && ni < n && nj >= 0 && nj < n && !visited(ni)(nj)) {
            pq.offer(Array(grid(ni)(nj), ni, nj))
          }
        }
      }
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if n == 1 {
            return grid[0][0];
        }
        let mut visited = vec![vec![false; n]; n];
        let dirs = [(0i32, 1i32), (1, 0), (-1, 0), (0, -1)];
        use std::cmp::{max, Reverse};
        use std::collections::BinaryHeap;
        let mut heap: BinaryHeap<(Reverse<i32>, usize, usize)> = BinaryHeap::new();
        heap.push((Reverse(grid[0][0]), 0, 0));
        while let Some((Reverse(cost), x, y)) = heap.pop() {
            if visited[x][y] {
                continue;
            }
            visited[x][y] = true;
            if x == n - 1 && y == n - 1 {
                return cost;
            }
            for (dx, dy) in dirs.iter() {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx >= 0 && nx < n as i32 && ny >= 0 && ny < n as i32 {
                    let ux = nx as usize;
                    let uy = ny as usize;
                    if !visited[ux][uy] {
                        let next_cost = max(cost, grid[ux][uy]);
                        heap.push((Reverse(next_cost), ux, uy));
                    }
                }
            }
        }
        0
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (swim-in-water grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (list->vector (map list->vector grid)))
         (n (vector-length rows))
         (visited
           (let ((v (make-vector n)))
             (for ([i (in-range n)])
               (vector-set! v i (make-vector n #f)))
             v))
         (heap (make-heap (lambda (a b) (< (first a) (first b))))))
    (define start-time (vector-ref (vector-ref rows 0) 0))
    (heap-push! heap (list start-time 0 0))
    (let recur ()
      (define cur (heap-pop! heap))
      (define t (first cur))
      (define i (second cur))
      (define j (third cur))
      (unless (vector-ref (vector-ref visited i) j)
        (vector-set! (vector-ref visited i) j #t)
        (if (and (= i (- n 1)) (= j (- n 1)))
            t
            (begin
              (for ([d '((0 1) (1 0) (0 -1) (-1 0))])
                (define ni (+ i (first d)))
                (define nj (+ j (second d)))
                (when (and (>= ni 0) (< ni n) (>= nj 0) (< nj n))
                  (unless (vector-ref (vector-ref visited ni) nj)
                    (define newt (max t (vector-ref (vector-ref rows ni) nj)))
                    (heap-push! heap (list newt ni nj)))))
              (recur)))))))
```

## Erlang

```erlang
-module(solution).
-export([swim_in_water/1]).

-spec swim_in_water(Grid :: [[integer()]]) -> integer().
swim_in_water(Grid) ->
    N = length(Grid),
    MaxVal = N * N - 1,
    Start = get_val(Grid, 0, 0),
    binary_search(Grid, Start, MaxVal).

%% binary search for minimal time
binary_search(_Grid, Low, High) when Low >= High -> Low;
binary_search(Grid, Low, High) ->
    Mid = (Low + High) div 2,
    case reachable(Grid, Mid) of
        true  -> binary_search(Grid, Low, Mid);
        false -> binary_search(Grid, Mid + 1, High)
    end.

%% check if bottom-right is reachable with water level T
reachable(Grid, T) ->
    N = length(Grid),
    case get_val(Grid, 0, 0) =< T of
        false -> false;
        true  -> bfs([{0,0}], #{ {0,0} => true }, Grid, T, N)
    end.

bfs([], _Visited, _Grid, _T, _N) ->
    false;
bfs([{I,J}|Rest], Visited, Grid, T, N) ->
    case {I, J} of
        {X, Y} when X =:= N-1, Y =:= N-1 -> true;
        _ ->
            Neigh = [{I-1,J},{I+1,J},{I,J-1},{I,J+1}],
            {NewQueue, NewVisited} =
                lists:foldl(fun({Ni,Nj}, {Q,V}) ->
                    if Ni >= 0, Nj >= 0, Ni < N, Nj < N,
                       not maps:is_key({Ni,Nj}, V),
                       get_val(Grid, Ni, Nj) =< T ->
                            {[{Ni,Nj}|Q], maps:put({Ni,Nj}, true, V)};
                       true -> {Q,V}
                    end
                end, {Rest, Visited}, Neigh),
            bfs(NewQueue, NewVisited, Grid, T, N)
    end.

%% get value at (I,J) where indices are 0‑based
get_val(Grid, I, J) ->
    Row = lists:nth(I + 1, Grid),
    lists:nth(J + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec swim_in_water(grid :: [[integer]]) :: integer
  def swim_in_water(grid) do
    n = length(grid)
    max_val = n * n - 1
    binary_search(grid, 0, max_val)
  end

  defp binary_search(_grid, low, high) when low >= high, do: low

  defp binary_search(grid, low, high) do
    mid = div(low + high, 2)

    if reachable?(grid, mid) do
      binary_search(grid, low, mid)
    else
      binary_search(grid, mid + 1, high)
    end
  end

  defp reachable?(grid, t) do
    n = length(grid)

    if get_cell(grid, 0, 0) > t do
      false
    else
      bfs(grid, t, n)
    end
  end

  defp bfs(grid, t, n) do
    queue = :queue.new() |> :queue.in({0, 0})
    visited = MapSet.new([{0, 0}])
    bfs_loop(grid, t, n, queue, visited)
  end

  defp bfs_loop(_grid, _t, n, queue, _visited) do
    case :queue.out(queue) do
      {:empty, _} ->
        false

      {{:value, {i, j}}, rest_queue} ->
        if i == n - 1 and j == n - 1 do
          true
        else
          {new_queue, new_visited} =
            [{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}]
            |> Enum.reduce({rest_queue, MapSet.new()}, fn {ni, nj},
                                                          {q_acc, vis_acc} ->
              if ni >= 0 and nj >= 0 and ni < n and nj < n do
                val = get_cell(grid, ni, nj)

                if val <= t and not MapSet.member?(vis_acc, {ni, nj}) do
                  {:queue.in({ni, nj}, q_acc), MapSet.put(vis_acc, {ni, nj})}
                else
                  {q_acc, vis_acc}
                end
              else
                {q_acc, vis_acc}
              end
            end)

          bfs_loop(grid, t, n, new_queue, new_visited)
        end
    end
  end

  defp get_cell(grid, i, j) do
    grid |> Enum.at(i) |> Enum.at(j)
  end
end
```

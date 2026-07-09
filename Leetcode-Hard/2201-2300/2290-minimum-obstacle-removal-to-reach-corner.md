# 2290. Minimum Obstacle Removal to Reach Corner

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumObstacles(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        const int INF = 1e9;
        vector<vector<int>> dist(m, vector<int>(n, INF));
        deque<pair<int,int>> dq;
        dist[0][0] = 0;
        dq.emplace_front(0, 0);
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!dq.empty()) {
            auto [x, y] = dq.front();
            dq.pop_front();
            int d = dist[x][y];
            if (x == m - 1 && y == n - 1) return d;
            for (auto &dir : dirs) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                int nd = d + grid[nx][ny];
                if (nd < dist[nx][ny]) {
                    dist[nx][ny] = nd;
                    if (grid[nx][ny] == 0)
                        dq.emplace_front(nx, ny);
                    else
                        dq.emplace_back(nx, ny);
                }
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minimumObstacles(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int INF = Integer.MAX_VALUE;
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) {
            java.util.Arrays.fill(dist[i], INF);
        }
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};

        java.util.ArrayDeque<int[]> deque = new java.util.ArrayDeque<>();
        dist[0][0] = 0;
        deque.offerFirst(new int[]{0, 0});

        while (!deque.isEmpty()) {
            int[] cur = deque.pollFirst();
            int r = cur[0];
            int c = cur[1];
            if (r == m - 1 && c == n - 1) {
                return dist[r][c];
            }
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int w = grid[nr][nc]; // cost to enter neighbor
                    int nd = dist[r][c] + w;
                    if (nd < dist[nr][nc]) {
                        dist[nr][nc] = nd;
                        if (w == 0) {
                            deque.offerFirst(new int[]{nr, nc});
                        } else {
                            deque.offerLast(new int[]{nr, nc});
                        }
                    }
                }
            }
        }
        return -1; // should never reach here
    }
}
```

## Python

```python
class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        m = len(grid)
        n = len(grid[0])
        INF = 10 ** 9
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque()
        dq.append((0, 0))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            x, y = dq.popleft()
            cur = dist[x][y]
            if x == m - 1 and y == n - 1:
                return cur
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    w = grid[nx][ny]  # 0 or 1
                    nd = cur + w
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if w == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        return dist[m - 1][n - 1]
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = m * n + 5
        dist = [[INF] * n for _ in range(m)]
        dq = deque()
        dist[0][0] = 0
        dq.append((0, 0))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            x, y = dq.popleft()
            d = dist[x][y]
            if x == m - 1 and y == n - 1:
                return d
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = d + grid[nx][ny]
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        return -1
```

## C

```c
#include <limits.h>
#include <stdlib.h>

typedef struct {
    int d;
    int idx;
} Node;

static void heapPush(Node *heap, int *size, Node val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].d <= heap[i].d) break;
        Node tmp = heap[p];
        heap[p] = heap[i];
        heap[i] = tmp;
        i = p;
    }
}

static Node heapPop(Node *heap, int *size) {
    Node ret = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = l + 1, s = i;
        if (l < *size && heap[l].d < heap[s].d) s = l;
        if (r < *size && heap[r].d < heap[s].d) s = r;
        if (s == i) break;
        Node tmp = heap[i];
        heap[i] = heap[s];
        heap[s] = tmp;
        i = s;
    }
    return ret;
}

int minimumObstacles(int** grid, int gridSize, int* gridColSize){
    int rows = gridSize;
    int cols = gridColSize[0];
    int total = rows * cols;

    int *dist = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < total; ++i) dist[i] = INT_MAX;

    Node *heap = (Node*)malloc(total * sizeof(Node));
    int heapSize = 0;

    dist[0] = 0;
    heapPush(heap, &heapSize, (Node){0, 0});

    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    while (heapSize) {
        Node cur = heapPop(heap, &heapSize);
        if (cur.d != dist[cur.idx]) continue;
        if (cur.idx == total - 1) break; // reached target

        int r = cur.idx / cols;
        int c = cur.idx % cols;

        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            int nidx = nr * cols + nc;
            int w = grid[nr][nc]; // 0 or 1
            int nd = cur.d + w;
            if (nd < dist[nidx]) {
                dist[nidx] = nd;
                heapPush(heap, &heapSize, (Node){nd, nidx});
            }
        }
    }

    int answer = dist[total - 1];
    free(dist);
    free(heap);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    public int MinimumObstacles(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;
        const int INF = int.MaxValue;
        int[,] dist = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                dist[i, j] = INF;

        var deque = new LinkedList<(int r, int c)>();
        dist[0, 0] = 0;
        deque.AddFirst((0, 0));

        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (deque.Count > 0)
        {
            var cur = deque.First.Value;
            deque.RemoveFirst();
            int r = cur.r, c = cur.c;
            int curDist = dist[r, c];

            if (r == m - 1 && c == n - 1) break;

            for (int k = 0; k < 4; k++)
            {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;

                int ndist = curDist + grid[nr][nc];
                if (ndist < dist[nr, nc])
                {
                    dist[nr, nc] = ndist;
                    if (grid[nr][nc] == 0)
                        deque.AddFirst((nr, nc));
                    else
                        deque.AddLast((nr, nc));
                }
            }
        }

        return dist[m - 1, n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumObstacles = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const INF = 1 << 30;
    const dist = Array.from({ length: m }, () => Array(n).fill(INF));
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(item) {
            this.heap.push(item);
            this._up(this.heap.length - 1);
        }
        pop() {
            if (this.heap.length === 0) return null;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this._down(0);
            }
            return top;
        }
        _up(idx) {
            while (idx > 0) {
                const p = (idx - 1) >> 1;
                if (this.heap[p][0] <= this.heap[idx][0]) break;
                [this.heap[p], this.heap[idx]] = [this.heap[idx], this.heap[p]];
                idx = p;
            }
        }
        _down(idx) {
            const len = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < len && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < len && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }
    
    const heap = new MinHeap();
    dist[0][0] = 0;
    heap.push([0, 0, 0]); // [cost, row, col]
    
    while (heap.size() > 0) {
        const [cost, r, c] = heap.pop();
        if (cost !== dist[r][c]) continue;
        if (r === m - 1 && c === n - 1) return cost;
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            const newCost = cost + grid[nr][nc];
            if (newCost < dist[nr][nc]) {
                dist[nr][nc] = newCost;
                heap.push([newCost, nr, nc]);
            }
        }
    }
    
    return dist[m - 1][n - 1];
};
```

## Typescript

```typescript
function minimumObstacles(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const INF = Number.MAX_SAFE_INTEGER;

    const dist: number[][] = Array.from({ length: m }, () => new Array<number>(n).fill(INF));
    dist[0][0] = 0;

    class MinHeap {
        heap: [number, number, number][] = [];
        push(item: [number, number, number]): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        pop(): [number, number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const last = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        bubbleDown(idx: number): void {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
        isEmpty(): boolean {
            return this.heap.length === 0;
        }
    }

    const heap = new MinHeap();
    heap.push([0, 0, 0]);

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ];

    while (!heap.isEmpty()) {
        const cur = heap.pop()!;
        const cost = cur[0];
        const r = cur[1];
        const c = cur[2];

        if (cost > dist[r][c]) continue;
        if (r === m - 1 && c === n - 1) return cost;

        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            const newCost = cost + grid[nr][nc];
            if (newCost < dist[nr][nc]) {
                dist[nr][nc] = newCost;
                heap.push([newCost, nr, nc]);
            }
        }
    }

    return -1; // Should never reach here due to problem guarantees
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumObstacles($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        // distance matrix initialized to a large value
        $dist = array_fill(0, $m, array_fill(0, $n, PHP_INT_MAX));
        $dist[0][0] = 0;

        // deque for 0-1 BFS
        $deque = new SplDoublyLinkedList();
        $deque->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO);
        $deque->unshift([0, 0]);

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$deque->isEmpty()) {
            [$x, $y] = $deque->shift();
            $curDist = $dist[$x][$y];

            if ($x == $m - 1 && $y == $n - 1) {
                // reached target with minimal obstacles
                return $curDist;
            }

            foreach ($dirs as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];

                if ($nx < 0 || $nx >= $m || $ny < 0 || $ny >= $n) {
                    continue;
                }

                $cost = $grid[$nx][$ny]; // 0 or 1
                $newDist = $curDist + $cost;

                if ($newDist < $dist[$nx][$ny]) {
                    $dist[$nx][$ny] = $newDist;
                    if ($cost == 0) {
                        $deque->unshift([$nx, $ny]); // prioritize zero-cost moves
                    } else {
                        $deque->push([$nx, $ny]);    // costlier moves go to the back
                    }
                }
            }
        }

        return $dist[$m - 1][$n - 1];
    }
}
```

## Swift

```swift
import Foundation

struct Node {
    let cost: Int
    let row: Int
    let col: Int
}

struct MinHeap {
    private var elements: [Node] = []
    
    mutating func push(_ value: Node) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    mutating func pop() -> Node? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        }
        let top = elements[0]
        elements[0] = elements.removeLast()
        siftDown(from: 0)
        return top
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && elements[child].cost < elements[parent].cost {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < elements.count && elements[left].cost < elements[smallest].cost {
                smallest = left
            }
            if right < elements.count && elements[right].cost < elements[smallest].cost {
                smallest = right
            }
            if smallest == parent { break }
            elements.swapAt(parent, smallest)
            parent = smallest
        }
    }
}

class Solution {
    func minimumObstacles(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        let total = m * n
        var dist = Array(repeating: Int.max, count: total)
        func index(_ r: Int, _ c: Int) -> Int { r * n + c }
        
        var heap = MinHeap()
        dist[0] = 0
        heap.push(Node(cost: 0, row: 0, col: 0))
        
        let dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while let cur = heap.pop() {
            if cur.cost != dist[index(cur.row, cur.col)] { continue }
            if cur.row == m - 1 && cur.col == n - 1 {
                return cur.cost
            }
            for (dr, dc) in dirs {
                let nr = cur.row + dr
                let nc = cur.col + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                let newCost = cur.cost + grid[nr][nc]
                let idx = index(nr, nc)
                if newCost < dist[idx] {
                    dist[idx] = newCost
                    heap.push(Node(cost: newCost, row: nr, col: nc))
                }
            }
        }
        return dist[index(m - 1, n - 1)]
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun minimumObstacles(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val total = m * n
        val dist = IntArray(total) { Int.MAX_VALUE }
        val deque: ArrayDeque<Int> = ArrayDeque()
        dist[0] = 0
        deque.addFirst(0)

        val dr = intArrayOf(-1, 1, 0, 0)
        val dc = intArrayOf(0, 0, -1, 1)

        while (deque.isNotEmpty()) {
            val idx = deque.removeFirst()
            val curDist = dist[idx]
            val r = idx / n
            val c = idx % n

            for (k in 0 until 4) {
                val nr = r + dr[k]
                val nc = c + dc[k]
                if (nr !in 0 until m || nc !in 0 until n) continue
                val nid = nr * n + nc
                val cost = grid[nr][nc] // 0 or 1
                if (curDist + cost < dist[nid]) {
                    dist[nid] = curDist + cost
                    if (cost == 0) {
                        deque.addFirst(nid)
                    } else {
                        deque.addLast(nid)
                    }
                }
            }
        }

        return dist[total - 1]
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int minimumObstacles(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    const int INF = 1 << 30;
    List<List<int>> dist = List.generate(m, (_) => List.filled(n, INF));
    var deque = DoubleLinkedQueue<List<int>>();
    dist[0][0] = 0;
    deque.addFirst([0, 0]);
    const List<int> dr = [0, 1, 0, -1];
    const List<int> dc = [1, 0, -1, 0];

    while (deque.isNotEmpty) {
      var cur = deque.removeFirst();
      int r = cur[0], c = cur[1];
      if (r == m - 1 && c == n - 1) return dist[r][c];
      for (int k = 0; k < 4; ++k) {
        int nr = r + dr[k];
        int nc = c + dc[k];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
        int w = grid[nr][nc];
        int nd = dist[r][c] + w;
        if (nd < dist[nr][nc]) {
          dist[nr][nc] = nd;
          if (w == 0) {
            deque.addFirst([nr, nc]);
          } else {
            deque.addLast([nr, nc]);
          }
        }
      }
    }

    return dist[m - 1][n - 1];
  }
}
```

## Golang

```go
package main

import (
	"container/list"
)

func minimumObstacles(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	total := m * n
	const INF = int(^uint(0) >> 1) // max int

	dist := make([]int, total)
	for i := range dist {
		dist[i] = INF
	}
	startIdx := 0
	dist[startIdx] = 0

	type node struct{ x, y int }
	deq := list.New()
	deq.PushFront(node{0, 0})

	dir := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for deq.Len() > 0 {
		cur := deq.Remove(deq.Front()).(node)
		curIdx := cur.x*n + cur.y
		if curIdx == total-1 {
			return dist[curIdx]
		}
		for _, d := range dir {
			nx, ny := cur.x+d[0], cur.y+d[1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n {
				continue
			}
			nextIdx := nx*n + ny
			cost := grid[nx][ny] // 0 or 1
			if dist[curIdx]+cost < dist[nextIdx] {
				dist[nextIdx] = dist[curIdx] + cost
				if cost == 0 {
					deq.PushFront(node{nx, ny})
				} else {
					deq.PushBack(node{nx, ny})
				}
			}
		}
	}
	return -1
}
```

## Ruby

```ruby
def minimum_obstacles(grid)
  m = grid.size
  n = grid[0].size
  inf = 1 << 60
  dist = Array.new(m) { Array.new(n, inf) }
  dist[0][0] = 0

  heap = MinHeap.new
  heap.push([0, 0, 0])

  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  until heap.empty?
    cost, r, c = heap.pop
    next if cost != dist[r][c]

    return cost if r == m - 1 && c == n - 1

    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next unless nr.between?(0, m - 1) && nc.between?(0, n - 1)

      new_cost = cost + grid[nr][nc]
      if new_cost < dist[nr][nc]
        dist[nr][nc] = new_cost
        heap.push([new_cost, nr, nc])
      end
    end
  end

  dist[m - 1][n - 1]
end

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

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent][0] <= @data[idx][0]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = idx * 2 + 2
      smallest = idx
      if left < size && @data[left][0] < @data[smallest][0]
        smallest = left
      end
      if right < size && @data[right][0] < @data[smallest][0]
        smallest = right
      end
      break if smallest == idx
      @data[idx], @data[smallest] = @data[smallest], @data[idx]
      idx = smallest
    end
  end
end
```

## Scala

```scala
import java.util.ArrayDeque

object Solution {
  def minimumObstacles(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val dist = Array.fill(m)(Array.fill(n)(Int.MaxValue))
    val dq = new ArrayDeque[(Int, Int)]()
    dist(0)(0) = 0
    dq.addFirst((0, 0))

    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (!dq.isEmpty) {
      val (r, c) = dq.pollFirst()
      if (r == m - 1 && c == n - 1) return dist(r)(c)
      val cur = dist(r)(c)
      var i = 0
      while (i < 4) {
        val nr = r + dirs(i)._1
        val nc = c + dirs(i)._2
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
          val w = grid(nr)(nc)
          val nd = cur + w
          if (nd < dist(nr)(nc)) {
            dist(nr)(nc) = nd
            if (w == 0) dq.addFirst((nr, nc))
            else dq.addLast((nr, nc))
          }
        }
        i += 1
      }
    }

    dist(m - 1)(n - 1)
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn minimum_obstacles(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![i32::MAX; m * n];
        let mut deque: VecDeque<(usize, usize)> = VecDeque::new();

        dist[0] = 0;
        deque.push_front((0, 0));

        let dirs = [(1_i32, 0_i32), (-1, 0), (0, 1), (0, -1)];

        while let Some((r, c)) = deque.pop_front() {
            let cur_idx = r * n + c;
            let cur_dist = dist[cur_idx];
            for &(dr, dc) in &dirs {
                let nr_i32 = r as i32 + dr;
                let nc_i32 = c as i32 + dc;
                if nr_i32 < 0 || nr_i32 >= m as i32 || nc_i32 < 0 || nc_i32 >= n as i32 {
                    continue;
                }
                let nr = nr_i32 as usize;
                let nc = nc_i32 as usize;
                let w = grid[nr][nc];
                let ndist = cur_dist + w;
                let nidx = nr * n + nc;
                if ndist < dist[nidx] {
                    dist[nidx] = ndist;
                    if w == 0 {
                        deque.push_front((nr, nc));
                    } else {
                        deque.push_back((nr, nc));
                    }
                }
            }
        }

        dist[m * n - 1]
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (minimum-obstacles grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length grid))
         (n (if (= m 0) 0 (length (first grid))))
         (grid-vec (list->vector (map list->vector grid)))
         (INF 1000000000)
         (dist (make-vector m)))
    ;; initialize distance matrix
    (for ([i (in-range m)])
      (vector-set! dist i (make-vector n INF)))
    (define heap (make-heap (lambda (a b) (< (first a) (first b)))))
    ;; start cell
    (begin
      (vector-set! (vector-ref dist 0) 0 0)
      (heap-insert! heap (list 0 0 0)))
    (define dirs '((1 0) (-1 0) (0 1) (0 -1)))
    (let loop ()
      (if (heap-empty? heap)
          (vector-ref (vector-ref dist (- m 1)) (- n 1))
          (let* ((item (heap-pop! heap))
                 (cost (first item))
                 (r (second item))
                 (c (third item)))
            ;; if we have already found a better path to (r,c), skip
            (when (< cost (vector-ref (vector-ref dist r) c))
              (vector-set! (vector-ref dist r) c cost))
            (if (and (= r (- m 1)) (= c (- n 1)))
                cost
                (begin
                  (for ([d dirs])
                    (define nr (+ r (first d)))
                    (define nc (+ c (second d)))
                    (when (and (>= nr 0) (< nr m)
                               (>= nc 0) (< nc n))
                      (let* ((cell (vector-ref (vector-ref grid-vec nr) nc))
                             (new-cost (+ cost cell)))
                        (when (< new-cost (vector-ref (vector-ref dist nr) nc))
                          (vector-set! (vector-ref dist nr) nc new-cost)
                          (heap-insert! heap (list new-cost nr nc))))))
                  (loop))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_obstacles/1]).

-spec minimum_obstacles(Grid :: [[integer()]]) -> integer().
minimum_obstacles(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    GridArray = array:from_list([array:from_list(Row) || Row <- Grid]),
    Directions = [{1,0},{-1,0},{0,1},{0,-1}],
    Dist0 = maps:put({0,0}, 0, #{}),
    Q0 = queue:in_r({0,0}, queue:new()),
    bfs(Q0, Dist0, GridArray, M, N, Directions).

bfs(Queue, DistMap, _GridA, M, N, _Directions) when Queue == queue:new() ->
    -1;
bfs(Queue, DistMap, GridA, M, N, Directions) ->
    case queue:out(Queue) of
        {empty, _} -> -1;
        {{value, {R,C}}, QRest} ->
            D = maps:get({R,C}, DistMap),
            if R == M-1 andalso C == N-1 ->
                D;
               true ->
                {QNew, DistNew} = process_neighbors(R, C, D, QRest, DistMap,
                                                   GridA, M, N, Directions),
                bfs(QNew, DistNew, GridA, M, N, Directions)
            end
    end.

process_neighbors(R, C, D, Queue0, Dist0, GridA, M, N, Directions) ->
    lists:foldl(fun({DR,DC}, {QAcc, DistAcc}) ->
        Nr = R + DR,
        Nc = C + DC,
        if Nr >= 0, Nr < M, Nc >= 0, Nc < N ->
                RowArr = array:get(Nr, GridA),
                Val = array:get(Nc, RowArr),
                NewD = D + Val,
                case maps:find({Nr,Nc}, DistAcc) of
                    error ->
                        Dist1 = maps:put({Nr,Nc}, NewD, DistAcc),
                        Q1 = if Val == 0 -> queue:in_r({Nr,Nc}, QAcc);
                                 true      -> queue:in({Nr,Nc}, QAcc)
                             end,
                        {Q1, Dist1};
                    {ok, Old} when NewD < Old ->
                        Dist1 = maps:put({Nr,Nc}, NewD, DistAcc),
                        Q1 = if Val == 0 -> queue:in_r({Nr,Nc}, QAcc);
                                 true      -> queue:in({Nr,Nc}, QAcc)
                             end,
                        {Q1, Dist1};
                    _ ->
                        {QAcc, DistAcc}
                end;
            true ->
                {QAcc, DistAcc}
        end
    end, {Queue0, Dist0}, Directions).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_obstacles(grid :: [[integer]]) :: integer
  def minimum_obstacles(grid) do
    m = length(grid)
    n = length(List.first(grid))
    total = m * n
    inf = total + 5

    # Convert grid to a tuple of tuples for O(1) access
    grid_tt =
      grid
      |> Enum.map(&List.to_tuple/1)
      |> List.to_tuple()

    dist = :array.new(total, default: inf)
    dist = :array.set(0, 0, dist)

    q = :queue.in_r({0, 0}, :queue.new())
    bfs(q, grid_tt, m, n, dist)
  end

  defp bfs(queue, grid, m, n, dist) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {r, c}}, q2} ->
        idx = r * n + c
        cur_dist = :array.get(idx, dist)

        if r == m - 1 and c == n - 1 do
          cur_dist
        else
          dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

          {new_queue, new_dist} =
            Enum.reduce(dirs, {q2, dist}, fn {dr, dc}, {qq, dd} ->
              nr = r + dr
              nc = c + dc

              if nr >= 0 and nr < m and nc >= 0 and nc < n do
                nidx = nr * n + nc
                row_tuple = elem(grid, nr)
                cell_val = elem(row_tuple, nc) # 0 or 1
                ndist = cur_dist + cell_val
                old = :array.get(nidx, dd)

                if ndist < old do
                  dd2 = :array.set(nidx, ndist, dd)

                  qq2 =
                    if cell_val == 0 do
                      :queue.in_r({nr, nc}, qq)   # front for cost 0
                    else
                      :queue.in({nr, nc}, qq)     # back for cost 1
                    end

                  {qq2, dd2}
                else
                  {qq, dd}
                end
              else
                {qq, dd}
              end
            end)

          bfs(new_queue, grid, m, n, new_dist)
        end
    end
  end
end
```

# 1368. Minimum Cost to Make at Least One Valid Path in a Grid

## Cpp

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        const int INF = 1e9;
        vector<vector<int>> dist(m, vector<int>(n, INF));
        deque<pair<int,int>> dq;
        dist[0][0] = 0;
        dq.emplace_front(0,0);
        
        // direction order: right, left, down, up
        int dr[4] = {0, 0, 1, -1};
        int dc[4] = {1, -1, 0, 0};
        
        while (!dq.empty()) {
            auto [r,c] = dq.front();
            dq.pop_front();
            int curDist = dist[r][c];
            for (int d = 0; d < 4; ++d) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int w = (grid[r][c] == d+1) ? 0 : 1;
                if (curDist + w < dist[nr][nc]) {
                    dist[nr][nc] = curDist + w;
                    if (w == 0) dq.emplace_front(nr, nc);
                    else dq.emplace_back(nr, nc);
                }
            }
        }
        return dist[m-1][n-1];
    }
};
```

## Java

```java
class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int INF = Integer.MAX_VALUE;
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) {
            java.util.Arrays.fill(dist[i], INF);
        }
        java.util.Deque<int[]> deque = new java.util.ArrayDeque<>();
        dist[0][0] = 0;
        deque.offerFirst(new int[]{0, 0});
        int[] dr = {0, 0, 1, -1}; // right, left, down, up
        int[] dc = {1, -1, 0, 0};
        while (!deque.isEmpty()) {
            int[] cur = deque.pollFirst();
            int r = cur[0], c = cur[1];
            int curDist = dist[r][c];
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int w = (grid[r][c] == k + 1) ? 0 : 1;
                if (curDist + w < dist[nr][nc]) {
                    dist[nr][nc] = curDist + w;
                    if (w == 0) {
                        deque.offerFirst(new int[]{nr, nc});
                    } else {
                        deque.offerLast(new int[]{nr, nc});
                    }
                }
            }
        }
        return dist[m - 1][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        # direction vectors: right, left, down, up
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        INF = 10 ** 9
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque()
        dq.append((0, 0))

        while dq:
            r, c = dq.popleft()
            cur = dist[r][c]
            # if we already reached target with minimal cost, can break early
            if r == m - 1 and c == n - 1:
                continue
            for i, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # cost is 0 if current cell's arrow already points to this neighbor
                    w = 0 if grid[r][c] == i + 1 else 1
                    nd = cur + w
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        if w == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m - 1][n - 1]
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**9
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque()
        dq.appendleft((0, 0))
        # directions: right, left, down, up
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while dq:
            r, c = dq.popleft()
            cur = dist[r][c]
            for i, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    w = 0 if grid[r][c] == i + 1 else 1
                    nd = cur + w
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        if w == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        return dist[m - 1][n - 1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

struct Node {
    int r;
    int c;
};

int minCost(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    const int dr[4] = {0, 0, 1, -1};
    const int dc[4] = {1, -1, 0, 0};

    /* distance matrix */
    int **dist = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        dist[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) dist[i][j] = INT_MAX;
    }
    dist[0][0] = 0;

    /* deque for 0-1 BFS */
    int cap = m * n * 4 + 5;
    struct Node *dq = (struct Node *)malloc(cap * sizeof(struct Node));
    int head = cap / 2, tail = cap / 2;          // empty

    /* push start node to front */
    head = (head - 1 + cap) % cap;
    dq[head].r = 0;
    dq[head].c = 0;

    while (head != tail) {
        struct Node cur = dq[head];
        head = (head + 1) % cap;
        int r = cur.r, c = cur.c;

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            int w = (grid[r][c] == d + 1) ? 0 : 1;
            if (dist[nr][nc] > dist[r][c] + w) {
                dist[nr][nc] = dist[r][c] + w;
                struct Node nxt = {nr, nc};
                if (w == 0) {
                    head = (head - 1 + cap) % cap;
                    dq[head] = nxt;
                } else {
                    dq[tail] = nxt;
                    tail = (tail + 1) % cap;
                }
            }
        }
    }

    int ans = dist[m - 1][n - 1];
    for (int i = 0; i < m; ++i) free(dist[i]);
    free(dist);
    free(dq);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinCost(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int[,] dist = new int[rows, cols];
        const int INF = int.MaxValue / 2;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dist[i, j] = INF;
            }
        }

        // directions: right, left, down, up
        int[] dr = new int[] { 0, 0, 1, -1 };
        int[] dc = new int[] { 1, -1, 0, 0 };
        int[] dirVal = new int[] { 1, 2, 3, 4 };

        var deque = new LinkedList<(int r, int c)>();
        dist[0, 0] = 0;
        deque.AddFirst((0, 0));

        while (deque.Count > 0) {
            var cur = deque.First.Value;
            deque.RemoveFirst();
            int curDist = dist[cur.r, cur.c];

            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;

                int cost = (grid[cur.r][cur.c] == dirVal[k]) ? 0 : 1;
                int ndist = curDist + cost;
                if (ndist < dist[nr, nc]) {
                    dist[nr, nc] = ndist;
                    if (cost == 0) {
                        deque.AddFirst((nr, nc));
                    } else {
                        deque.AddLast((nr, nc));
                    }
                }
            }
        }

        return dist[rows - 1, cols - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minCost = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dist = Array.from({ length: m }, () => Array(n).fill(INF));
    
    // direction vectors: right, left, down, up
    const dr = [0, 0, 1, -1];
    const dc = [1, -1, 0, 0];
    
    // custom deque using two parallel arrays
    const maxSize = m * n * 4 + 10;               // enough space for all pushes
    const qr = new Array(maxSize);
    const qc = new Array(maxSize);
    let front = Math.floor(maxSize / 2);          // start in the middle
    let back = front;
    
    const pushFront = (r, c) => {
        front--;
        qr[front] = r;
        qc[front] = c;
    };
    const pushBack = (r, c) => {
        qr[back] = r;
        qc[back] = c;
        back++;
    };
    
    // initialize
    dist[0][0] = 0;
    pushBack(0, 0);
    
    while (front < back) {
        const r = qr[front];
        const c = qc[front];
        front++;
        const curDist = dist[r][c];
        
        for (let k = 0; k < 4; k++) {
            const nr = r + dr[k];
            const nc = c + dc[k];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            
            // cost is 0 if current cell already points to this direction
            const w = (grid[r][c] === k + 1) ? 0 : 1;
            if (dist[nr][nc] > curDist + w) {
                dist[nr][nc] = curDist + w;
                if (w === 0) {
                    pushFront(nr, nc);
                } else {
                    pushBack(nr, nc);
                }
            }
        }
    }
    
    return dist[m - 1][n - 1];
};
```

## Typescript

```typescript
function minCost(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dist: number[][] = Array.from({ length: m }, () => new Array(n).fill(INF));
    dist[0][0] = 0;

    // direction vectors: right, left, down, up
    const dr = [0, 0, 1, -1];
    const dc = [1, -1, 0, 0];

    type Node = { r: number; c: number };
    const deque: Node[] = [{ r: 0, c: 0 }]; // use as double-ended queue (shift/unshift)

    while (deque.length) {
        const { r, c } = deque.shift()!; // pop front
        const curDist = dist[r][c];

        for (let i = 0; i < 4; ++i) {
            const nr = r + dr[i];
            const nc = c + dc[i];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;

            // cost is 0 if current cell's arrow already points to this neighbor
            const extraCost = grid[r][c] === i + 1 ? 0 : 1;
            const newDist = curDist + extraCost;
            if (newDist < dist[nr][nc]) {
                dist[nr][nc] = newDist;
                const node: Node = { r: nr, c: nc };
                if (extraCost === 0) {
                    deque.unshift(node); // prioritize zero-cost edges
                } else {
                    deque.push(node);
                }
            }
        }
    }

    return dist[m - 1][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minCost($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        // direction vectors: right, left, down, up
        $dirs = [
            [0, 1],   // 1
            [0, -1],  // 2
            [1, 0],   // 3
            [-1, 0]   // 4
        ];
        $dist = array_fill(0, $m, array_fill(0, $n, PHP_INT_MAX));
        $dist[0][0] = 0;
        $deque = new SplDoublyLinkedList();
        $deque->unshift([0, 0]); // start from (0,0)

        while (!$deque->isEmpty()) {
            [$r, $c] = $deque->shift();
            $curDist = $dist[$r][$c];
            for ($i = 0; $i < 4; $i++) {
                $nr = $r + $dirs[$i][0];
                $nc = $c + $dirs[$i][1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) {
                    continue;
                }
                // cost is 0 if current cell points to this direction, else 1
                $cost = ($grid[$r][$c] == $i + 1) ? 0 : 1;
                $newDist = $curDist + $cost;
                if ($newDist < $dist[$nr][$nc]) {
                    $dist[$nr][$nc] = $newDist;
                    if ($cost === 0) {
                        $deque->unshift([$nr, $nc]);
                    } else {
                        $deque->push([$nr, $nc]);
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
class Solution {
    func minCost(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var dist = Array(repeating: Array(repeating: Int.max, count: n), count: m)
        dist[0][0] = 0
        
        struct Node {
            var cost: Int
            var r: Int
            var c: Int
        }
        
        struct Heap<T> {
            var elements: [T] = []
            let priorityFunction: (T, T) -> Bool
            
            init(sort: @escaping (T, T) -> Bool) {
                self.priorityFunction = sort
            }
            
            var isEmpty: Bool { elements.isEmpty }
            
            mutating func push(_ value: T) {
                elements.append(value)
                siftUp(from: elements.count - 1)
            }
            
            mutating func pop() -> T? {
                guard !elements.isEmpty else { return nil }
                if elements.count == 1 {
                    return elements.removeLast()
                } else {
                    let value = elements[0]
                    elements[0] = elements.removeLast()
                    siftDown(from: 0)
                    return value
                }
            }
            
            private mutating func siftUp(from index: Int) {
                var child = index
                var parent = (child - 1) / 2
                while child > 0 && priorityFunction(elements[child], elements[parent]) {
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
                    var candidate = parent
                    if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                        candidate = left
                    }
                    if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                        candidate = right
                    }
                    if candidate == parent { return }
                    elements.swapAt(parent, candidate)
                    parent = candidate
                }
            }
        }
        
        var heap = Heap<Node>(sort: { $0.cost < $1.cost })
        heap.push(Node(cost: 0, r: 0, c: 0))
        
        let dr = [0, 0, 1, -1]   // right, left, down, up
        let dc = [1, -1, 0, 0]
        
        while let cur = heap.pop() {
            if cur.cost > dist[cur.r][cur.c] { continue }
            if cur.r == m - 1 && cur.c == n - 1 {
                return cur.cost
            }
            for dir in 0..<4 {
                let nr = cur.r + dr[dir]
                let nc = cur.c + dc[dir]
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                var newCost = cur.cost
                // grid direction: 1=right,2=left,3=down,4=up (convert to 0‑based)
                if grid[cur.r][cur.c] - 1 != dir {
                    newCost += 1
                }
                if newCost < dist[nr][nc] {
                    dist[nr][nc] = newCost
                    heap.push(Node(cost: newCost, r: nr, c: nc))
                }
            }
        }
        return dist[m - 1][n - 1]
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun minCost(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dist = Array(m) { IntArray(n) { Int.MAX_VALUE } }
        val dr = intArrayOf(0, 0, 1, -1)
        val dc = intArrayOf(1, -1, 0, 0)

        val deque: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        dist[0][0] = 0
        deque.addFirst(Pair(0, 0))

        while (deque.isNotEmpty()) {
            val (r, c) = deque.removeFirst()
            val curDist = dist[r][c]

            for (k in 0..3) {
                val nr = r + dr[k]
                val nc = c + dc[k]
                if (nr !in 0 until m || nc !in 0 until n) continue

                val w = if (grid[r][c] == k + 1) 0 else 1
                if (curDist + w < dist[nr][nc]) {
                    dist[nr][nc] = curDist + w
                    if (w == 0) {
                        deque.addFirst(Pair(nr, nc))
                    } else {
                        deque.addLast(Pair(nr, nc))
                    }
                }
            }
        }

        return dist[m - 1][n - 1]
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int minCost(List<List<int>> grid) {
    final int m = grid.length;
    final int n = grid[0].length;
    const List<int> dr = [0, 0, 1, -1]; // right, left, down, up
    const List<int> dc = [1, -1, 0, 0];

    const int INF = 1 << 30;
    final List<List<int>> dist =
        List.generate(m, (_) => List.filled(n, INF), growable: false);

    final Queue<List<int>> deque = Queue<List<int>>();
    dist[0][0] = 0;
    deque.addFirst([0, 0]);

    while (deque.isNotEmpty) {
      final cur = deque.removeFirst();
      final int r = cur[0];
      final int c = cur[1];

      for (int i = 0; i < 4; ++i) {
        final int nr = r + dr[i];
        final int nc = c + dc[i];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;

        final int w = (grid[r][c] == i + 1) ? 0 : 1;
        if (dist[nr][nc] > dist[r][c] + w) {
          dist[nr][nc] = dist[r][c] + w;
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

func minCost(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	const INF = int(^uint(0) >> 1)
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = INF
		}
	}
	dr := []int{0, 0, 1, -1}
	dc := []int{1, -1, 0, 0}

	deq := list.New()
	dist[0][0] = 0
	deq.PushFront([2]int{0, 0})

	for deq.Len() > 0 {
		elem := deq.Front()
		deq.Remove(elem)
		pos := elem.Value.([2]int)
		r, c := pos[0], pos[1]
		curDist := dist[r][c]

		for d := 0; d < 4; d++ {
			nr, nc := r+dr[d], c+dc[d]
			if nr < 0 || nr >= m || nc < 0 || nc >= n {
				continue
			}
			cost := 1
			if grid[r][c] == d+1 {
				cost = 0
			}
			newDist := curDist + cost
			if newDist < dist[nr][nc] {
				dist[nr][nc] = newDist
				if cost == 0 {
					deq.PushFront([2]int{nr, nc})
				} else {
					deq.PushBack([2]int{nr, nc})
				}
			}
		}
	}

	return dist[m-1][n-1]
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
# @return {Integer}
def min_cost(grid)
  m = grid.size
  n = grid[0].size
  dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
  inf = 1 << 60
  dist = Array.new(m) { Array.new(n, inf) }

  heap = MinHeap.new
  dist[0][0] = 0
  heap.push([0, 0, 0])

  until heap.empty?
    cost, r, c = heap.pop
    next if cost != dist[r][c]

    dirs.each_with_index do |(dr, dc), idx|
      nr = r + dr
      nc = c + dc
      next unless nr.between?(0, m - 1) && nc.between?(0, n - 1)

      w = (grid[r][c] == idx + 1) ? 0 : 1
      new_cost = cost + w
      if new_cost < dist[nr][nc]
        dist[nr][nc] = new_cost
        heap.push([new_cost, nr, nc])
      end
    end
  end

  dist[m - 1][n - 1]
end
```

## Scala

```scala
object Solution {
  def minCost(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val INF = Int.MaxValue / 2
    val dist = Array.fill(m)(Array.fill(n)(INF))
    val dr = Array(0, 0, 1, -1)
    val dc = Array(1, -1, 0, 0) // right, left, down, up
    val deque = new java.util.ArrayDeque[(Int, Int)]()
    dist(0)(0) = 0
    deque.addFirst((0, 0))
    while (!deque.isEmpty) {
      val (r, c) = deque.pollFirst()
      val curDist = dist(r)(c)
      for (i <- 0 until 4) {
        val nr = r + dr(i)
        val nc = c + dc(i)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
          val cost = if (grid(r)(c) - 1 == i) 0 else 1
          val nd = curDist + cost
          if (nd < dist(nr)(nc)) {
            dist(nr)(nc) = nd
            if (cost == 0) deque.addFirst((nr, nc))
            else deque.addLast((nr, nc))
          }
        }
      }
    }
    dist(m - 1)(n - 1)
  }
}
```

## Rust

```rust
pub struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![i32::MAX; n]; m];
        let mut dq: VecDeque<(usize, usize)> = VecDeque::new();

        dist[0][0] = 0;
        dq.push_front((0, 0));

        // directions: right, left, down, up
        let dirs: [(isize, isize); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];

        while let Some((x, y)) = dq.pop_front() {
            let cur = dist[x][y];
            for (i, &(dx, dy)) in dirs.iter().enumerate() {
                let nx_i = x as isize + dx;
                let ny_i = y as isize + dy;
                if nx_i < 0 || ny_i < 0 {
                    continue;
                }
                let nx = nx_i as usize;
                let ny = ny_i as usize;
                if nx >= m || ny >= n {
                    continue;
                }

                // cost to move in this direction
                let w = if grid[x][y] == (i as i32 + 1) { 0 } else { 1 };
                if dist[nx][ny] > cur + w {
                    dist[nx][ny] = cur + w;
                    if w == 0 {
                        dq.push_front((nx, ny));
                    } else {
                        dq.push_back((nx, ny));
                    }
                }
            }
        }

        dist[m - 1][n - 1]
    }
}
```

## Racket

```racket
(define/contract (min-cost grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length grid))
         (cols (if (zero? rows) 0 (length (first grid))))
         (INF 1000000)
         (dist (make-vector rows)))
    ;; initialise distance matrix
    (for ([i rows])
      (vector-set! dist i (make-vector cols INF)))
    (vector-set! (vector-ref dist 0) 0 0)

    ;; deque represented by two mutable lists: front and back
    (define front null)
    (define back null)
    (set! front (cons (list 0 0) front))

    (let loop ()
      (if (and (null? front) (null? back))
          ;; finished, return distance to bottom‑right cell
          (vector-ref (vector-ref dist (- rows 1)) (- cols 1))
          (begin
            ;; ensure there is an element in front; if not, move reversed back list
            (when (null? front)
              (set! front (reverse back))
              (set! back null))
            (define cur (car front))
            (set! front (cdr front))
            (define r (first cur))
            (define c (second cur))
            (define curDist (vector-ref (vector-ref dist r) c))

            ;; explore four neighbours
            (for ([d (in-list (list (cons 0 1)   ; right
                                    (cons 0 -1)  ; left
                                    (cons 1 0)   ; down
                                    (cons -1 0)))]) ; up
              (define dr (car d))
              (define dc (cdr d))
              (define nr (+ r dr))
              (define nc (+ c dc))
              (when (and (>= nr 0) (< nr rows)
                         (>= nc 0) (< nc cols))
                ;; direction that would be needed to move from (r,c) to (nr,nc)
                (define need-dir
                  (cond [(and (= dr 0) (= dc 1)) 1]   ; right
                        [(and (= dr 0) (= dc -1)) 2]  ; left
                        [(and (= dr 1) (= dc 0)) 3]   ; down
                        [else 4]))                    ; up
                (define cell-dir (list-ref (list-ref grid r) c))
                (define extra (if (= cell-dir need-dir) 0 1))
                (define nd (+ curDist extra))
                (when (< nd (vector-ref (vector-ref dist nr) nc))
                  (vector-set! (vector-ref dist nr) nc nd)
                  (if (= extra 0)
                      ;; zero‑cost edge → push to front
                      (set! front (cons (list nr nc) front))
                      ;; cost‑1 edge → push to back
                      (set! back (cons (list nr nc) back))))))
            (loop)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_cost/1]).

-spec min_cost(Grid :: [[integer()]]) -> integer().
min_cost(Grid) ->
    M = length(Grid),
    N = case Grid of
            [] -> 0;
            [Row|_] -> length(Row)
        end,
    Dist0 = maps:put({0,0}, 0, #{}),
    Deque0 = {[{0,0}], []},
    bfs(Deque0, Dist0, Grid, M, N).

bfs(Deque, Dist, _Grid, M, N) ->
    case dequeue(Deque) of
        empty -> maps:get({M-1,N-1}, Dist);
        {{R,C}, DeqRest} ->
            Curr = maps:get({R,C}, Dist),
            RowList = lists:nth(R+1, _Grid),
            Val = lists:nth(C+1, RowList),
            {Dist2, Deq2} = explore_neighbors(
                [{0,1,0},{0,-1,1},{1,0,2},{-1,0,3}],
                {R,C}, Curr, Val, Dist, DeqRest, _Grid, M, N),
            bfs(Deq2, Dist2, _Grid, M, N)
    end.

explore_neighbors([], _Pos, _CurrDist, _Val, Dist, Deque, _Grid, _M, _N) ->
    {Dist, Deque};
explore_neighbors([{DR,DC,Idx}|Rest], {R,C}, CurrDist, Val, Dist, Deque, Grid, M, N) ->
    NR = R + DR,
    NC = C + DC,
    if
        NR >= 0, NR < M, NC >= 0, NC < N ->
            EdgeCost = if Idx == Val-1 -> 0; true -> 1 end,
            NewDist = CurrDist + EdgeCost,
            case maps:find({NR,NC}, Dist) of
                {ok, Existing} when Existing =< NewDist ->
                    explore_neighbors(Rest, {R,C}, CurrDist, Val, Dist, Deque, Grid, M, N);
                _ ->
                    Dist1 = maps:put({NR,NC}, NewDist, Dist),
                    Deque1 = if EdgeCost == 0 -> push_front({NR,NC}, Deque); true -> push_back({NR,NC}, Deque) end,
                    explore_neighbors(Rest, {R,C}, CurrDist, Val, Dist1, Deque1, Grid, M, N)
            end;
        true ->
            explore_neighbors(Rest, {R,C}, CurrDist, Val, Dist, Deque, Grid, M, N)
    end.

dequeue({[], []}) -> empty;
dequeue({[H|T], B}) -> {H, {T, B}};
dequeue({[], B}) ->
    case lists:reverse(B) of
        [] -> empty;
        [H2|T2] -> {H2, {T2, []}}
    end.

push_front(Node, {F,B}) -> {[Node|F], B}.
push_back(Node, {F,B}) -> {F, [Node|B]}.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(grid :: [[integer]]) :: integer
  def min_cost(grid) do
    rows = length(grid)
    cols = length(hd(grid))
    dirs = [{0, 1, 1}, {0, -1, 2}, {1, 0, 3}, {-1, 0, 4}]
    start_key = {0, 0}
    dist = %{start_key => 0}
    queue = :queue.in_r(start_key, :queue.new())
    final_dist = bfs(grid, rows, cols, dirs, dist, queue)
    Map.get(final_dist, {rows - 1, cols - 1})
  end

  defp bfs(grid, rows, cols, dirs, dist, queue) do
    case :queue.out(queue) do
      {:empty, _} ->
        dist

      {{:value, {r, c}}, q_rest} ->
        d = Map.get(dist, {r, c})

        {new_dist, new_queue} =
          Enum.reduce(dirs, {dist, q_rest}, fn {dr, dc, expected},
                                               {cur_dist, cur_q} ->
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols do
              {cur_dist, cur_q}
            else
              extra =
                if get_cell(grid, r, c) == expected do
                  0
                else
                  1
                end

              nd = d + extra
              key = {nr, nc}
              old = Map.get(cur_dist, key, 1_000_000)

              if nd < old do
                updated_dist = Map.put(cur_dist, key, nd)

                updated_q =
                  if extra == 0 do
                    :queue.in_r(key, cur_q)
                  else
                    :queue.in(key, cur_q)
                  end

                {updated_dist, updated_q}
              else
                {cur_dist, cur_q}
              end
            end
          end)

        bfs(grid, rows, cols, dirs, new_dist, new_queue)
    end
  end

  defp get_cell(grid, r, c) do
    grid |> Enum.at(r) |> Enum.at(c)
  end
end
```

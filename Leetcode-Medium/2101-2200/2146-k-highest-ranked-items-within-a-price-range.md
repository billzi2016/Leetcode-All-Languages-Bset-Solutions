# 2146. K Highest Ranked Items Within a Price Range

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> highestRankedKItems(vector<vector<int>>& grid, vector<int>& pricing, vector<int>& start, int k) {
        int m = grid.size(), n = grid[0].size();
        int low = pricing[0], high = pricing[1];
        vector<vector<int>> dist(m, vector<int>(n, -1));
        queue<pair<int,int>> q;
        int sr = start[0], sc = start[1];
        dist[sr][sc] = 0;
        q.push({sr, sc});
        
        vector<array<int,4>> candidates; // {dist, price, row, col}
        if (grid[sr][sc] >= low && grid[sr][sc] <= high) {
            candidates.push_back({0, grid[sr][sc], sr, sc});
        }
        
        const int dr[4] = {-1, 1, 0, 0};
        const int dc[4] = {0, 0, -1, 1};
        
        while (!q.empty()) {
            auto [r, c] = q.front(); q.pop();
            int d = dist[r][c];
            for (int dir = 0; dir < 4; ++dir) {
                int nr = r + dr[dir];
                int nc = c + dc[dir];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (grid[nr][nc] == 0) continue; // obstacle
                if (dist[nr][nc] != -1) continue;
                dist[nr][nc] = d + 1;
                q.push({nr, nc});
                int price = grid[nr][nc];
                if (price >= low && price <= high) {
                    candidates.push_back({d + 1, price, nr, nc});
                }
            }
        }
        
        sort(candidates.begin(), candidates.end(),
             [](const array<int,4>& a, const array<int,4>& b){
                 if (a[0] != b[0]) return a[0] < b[0];          // distance
                 if (a[1] != b[1]) return a[1] < b[1];          // price
                 if (a[2] != b[2]) return a[2] < b[2];          // row
                 return a[3] < b[3];                            // col
             });
        
        vector<vector<int>> ans;
        for (int i = 0; i < (int)candidates.size() && i < k; ++i) {
            ans.push_back({candidates[i][2], candidates[i][3]});
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final int[][] DIRS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    private static class Item implements Comparable<Item> {
        int dist;
        int price;
        int row;
        int col;
        Item(int d, int p, int r, int c) {
            this.dist = d;
            this.price = p;
            this.row = r;
            this.col = c;
        }
        @Override
        public int compareTo(Item o) {
            if (this.dist != o.dist) return Integer.compare(this.dist, o.dist);
            if (this.price != o.price) return Integer.compare(this.price, o.price);
            if (this.row != o.row) return Integer.compare(this.row, o.row);
            return Integer.compare(this.col, o.col);
        }
    }
    
    public List<List<Integer>> highestRankedKItems(int[][] grid, int[] pricing, int[] start, int k) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{start[0], start[1], 0});
        visited[start[0]][start[1]] = true;
        
        int low = pricing[0];
        int high = pricing[1];
        List<Item> candidates = new ArrayList<>();
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1], d = cur[2];
            int val = grid[r][c];
            if (val >= low && val <= high) {
                candidates.add(new Item(d, val, r, c));
            }
            for (int[] dir : DIRS) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (visited[nr][nc] || grid[nr][nc] == 0) continue;
                visited[nr][nc] = true;
                q.offer(new int[]{nr, nc, d + 1});
            }
        }
        
        Collections.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        int limit = Math.min(k, candidates.size());
        for (int i = 0; i < limit; i++) {
            Item it = candidates.get(i);
            List<Integer> pos = new ArrayList<>(2);
            pos.add(it.row);
            pos.add(it.col);
            result.add(pos);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start

        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((sr, sc, 0))
        visited[sr][sc] = True

        candidates = []

        while q:
            r, c, d = q.popleft()
            val = grid[r][c]
            if low <= val <= high:
                candidates.append((d, val, r, c))

            nd = d + 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, nd))

        candidates.sort()
        return [[r, c] for _, _, r, c in candidates[:k]]
```

## Python3

```python
class Solution:
    def highestRankedKItems(self, grid, pricing, start, k):
        from collections import deque
        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start
        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((sr, sc, 0))
        visited[sr][sc] = True
        candidates = []
        while q:
            r, c, d = q.popleft()
            val = grid[r][c]
            if low <= val <= high:
                candidates.append((d, val, r, c))
            nd = d + 1
            if r > 0 and not visited[r-1][c] and grid[r-1][c] != 0:
                visited[r-1][c] = True
                q.append((r-1, c, nd))
            if r < m-1 and not visited[r+1][c] and grid[r+1][c] != 0:
                visited[r+1][c] = True
                q.append((r+1, c, nd))
            if c > 0 and not visited[r][c-1] and grid[r][c-1] != 0:
                visited[r][c-1] = True
                q.append((r, c-1, nd))
            if c < n-1 and not visited[r][c+1] and grid[r][c+1] != 0:
                visited[r][c+1] = True
                q.append((r, c+1, nd))
        candidates.sort()
        return [[r, c] for _, _, r, c in candidates[:k]]
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int dist;
    int price;
    int row;
    int col;
} Item;

static int cmpItem(const void *a, const void *b) {
    const Item *ia = (const Item *)a;
    const Item *ib = (const Item *)b;
    if (ia->dist != ib->dist) return ia->dist - ib->dist;
    if (ia->price != ib->price) return ia->price - ib->price;
    if (ia->row != ib->row) return ia->row - ib->row;
    return ia->col - ib->col;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** highestRankedKItems(int** grid, int gridSize, int* gridColSize,
                         int* pricing, int pricingSize,
                         int* start, int startSize,
                         int k, int* returnSize, int** returnColumnSizes) {
    int m = gridSize;
    int n = gridColSize[0];
    int low = pricing[0], high = pricing[1];
    int sr = start[0], sc = start[1];

    int totalCells = m * n;
    char *visited = (char *)calloc(totalCells, 1);
    int *qr = (int *)malloc(totalCells * sizeof(int));
    int *qc = (int *)malloc(totalCells * sizeof(int));
    int *qd = (int *)malloc(totalCells * sizeof(int));

    int head = 0, tail = 0;
    qr[tail] = sr; qc[tail] = sc; qd[tail] = 0; tail++;
    visited[sr * n + sc] = 1;

    Item *items = (Item *)malloc(totalCells * sizeof(Item));
    int cnt = 0;

    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    while (head < tail) {
        int r = qr[head];
        int c = qc[head];
        int d = qd[head];
        head++;

        int price = grid[r][c];
        if (price >= low && price <= high) {
            items[cnt].dist = d;
            items[cnt].price = price;
            items[cnt].row = r;
            items[cnt].col = c;
            cnt++;
        }

        for (int dir = 0; dir < 4; ++dir) {
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (grid[nr][nc] == 0) continue;
            int idx = nr * n + nc;
            if (visited[idx]) continue;
            visited[idx] = 1;
            qr[tail] = nr; qc[tail] = nc; qd[tail] = d + 1; tail++;
        }
    }

    free(visited);
    free(qr); free(qc); free(qd);

    if (cnt > 0) {
        qsort(items, cnt, sizeof(Item), cmpItem);
    }

    int outCnt = cnt < k ? cnt : k;
    *returnSize = outCnt;
    *returnColumnSizes = (int *)malloc(outCnt * sizeof(int));
    int **ans = (int **)malloc(outCnt * sizeof(int *));
    for (int i = 0; i < outCnt; ++i) {
        ans[i] = (int *)malloc(2 * sizeof(int));
        ans[i][0] = items[i].row;
        ans[i][1] = items[i].col;
        (*returnColumnSizes)[i] = 2;
    }

    free(items);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> HighestRankedKItems(int[][] grid, int[] pricing, int[] start, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        bool[,] visited = new bool[m, n];
        var queue = new Queue<(int r, int c, int d)>();
        queue.Enqueue((start[0], start[1], 0));
        visited[start[0], start[1]] = true;

        int low = pricing[0];
        int high = pricing[1];

        var candidates = new List<(int dist, int price, int row, int col)>();

        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (queue.Count > 0) {
            var (r, c, d) = queue.Dequeue();
            int val = grid[r][c];
            if (val >= low && val <= high) {
                candidates.Add((d, val, r, c));
            }
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                    !visited[nr, nc] && grid[nr][nc] != 0) {
                    visited[nr, nc] = true;
                    queue.Enqueue((nr, nc, d + 1));
                }
            }
        }

        candidates.Sort((a, b) => {
            int cmp = a.dist.CompareTo(b.dist);
            if (cmp != 0) return cmp;
            cmp = a.price.CompareTo(b.price);
            if (cmp != 0) return cmp;
            cmp = a.row.CompareTo(b.row);
            if (cmp != 0) return cmp;
            return a.col.CompareTo(b.col);
        });

        IList<IList<int>> result = new List<IList<int>>();
        int limit = Math.Min(k, candidates.Count);
        for (int i = 0; i < limit; i++) {
            var item = candidates[i];
            result.Add(new List<int> { item.row, item.col });
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @param {number[]} pricing
 * @param {number[]} start
 * @param {number} k
 * @return {number[][]}
 */
var highestRankedKItems = function(grid, pricing, start, k) {
    const [low, high] = pricing;
    const m = grid.length, n = grid[0].length;
    const visited = Array.from({ length: m }, () => new Uint8Array(n));
    
    const qR = [], qC = [];
    let head = 0;
    qR.push(start[0]);
    qC.push(start[1]);
    visited[start[0]][start[1]] = 1;
    
    let dist = 0;
    const candidates = []; // [dist, price, row, col]
    
    while (head < qR.length) {
        const levelSize = qR.length - head; // nodes at current distance
        for (let i = 0; i < levelSize; ++i) {
            const r = qR[head];
            const c = qC[head];
            head++;
            
            const price = grid[r][c];
            if (price >= low && price <= high) {
                candidates.push([dist, price, r, c]);
            }
            
            // explore 4 directions
            if (r > 0 && !visited[r - 1][c] && grid[r - 1][c] !== 0) {
                visited[r - 1][c] = 1;
                qR.push(r - 1);
                qC.push(c);
            }
            if (r + 1 < m && !visited[r + 1][c] && grid[r + 1][c] !== 0) {
                visited[r + 1][c] = 1;
                qR.push(r + 1);
                qC.push(c);
            }
            if (c > 0 && !visited[r][c - 1] && grid[r][c - 1] !== 0) {
                visited[r][c - 1] = 1;
                qR.push(r);
                qC.push(c - 1);
            }
            if (c + 1 < n && !visited[r][c + 1] && grid[r][c + 1] !== 0) {
                visited[r][c + 1] = 1;
                qR.push(r);
                qC.push(c + 1);
            }
        }
        dist++;
    }
    
    candidates.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];          // distance
        if (a[1] !== b[1]) return a[1] - b[1];          // price
        if (a[2] !== b[2]) return a[2] - b[2];          // row
        return a[3] - b[3];                             // col
    });
    
    const result = [];
    const limit = Math.min(k, candidates.length);
    for (let i = 0; i < limit; ++i) {
        result.push([candidates[i][2], candidates[i][3]]);
    }
    return result;
};
```

## Typescript

```typescript
function highestRankedKItems(grid: number[][], pricing: number[], start: number[], k: number): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const low = pricing[0];
    const high = pricing[1];

    // distance matrix, -1 means unvisited
    const dist: Int32Array[] = Array.from({ length: m }, () => new Int32Array(n).fill(-1));

    const qRow: number[] = [];
    const qCol: number[] = [];
    let head = 0;

    const sr = start[0];
    const sc = start[1];
    dist[sr][sc] = 0;
    qRow.push(sr);
    qCol.push(sc);

    const candidates: [number, number, number, number][] = [];

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];

    while (head < qRow.length) {
        const r = qRow[head];
        const c = qCol[head];
        head++;

        const d = dist[r][c];
        const price = grid[r][c];
        if (price >= low && price <= high) {
            candidates.push([d, price, r, c]);
        }

        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (grid[nr][nc] === 0) continue; // obstacle
            if (dist[nr][nc] !== -1) continue; // visited
            dist[nr][nc] = d + 1;
            qRow.push(nr);
            qCol.push(nc);
        }
    }

    candidates.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];          // distance
        if (a[1] !== b[1]) return a[1] - b[1];          // price
        if (a[2] !== b[2]) return a[2] - b[2];          // row
        return a[3] - b[3];                             // col
    });

    const result: number[][] = [];
    for (let i = 0; i < Math.min(k, candidates.length); ++i) {
        const [, , r, c] = candidates[i];
        result.push([r, c]);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer[] $pricing
     * @param Integer[] $start
     * @param Integer $k
     * @return Integer[][]
     */
    function highestRankedKItems($grid, $pricing, $start, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $low = $pricing[0];
        $high = $pricing[1];
        $sr = $start[0];
        $sc = $start[1];

        // visited matrix
        $visited = array_fill(0, $m, null);
        for ($i = 0; $i < $m; $i++) {
            $visited[$i] = array_fill(0, $n, false);
        }

        $queue = new SplQueue();
        $queue->enqueue([$sr, $sc, 0]); // row, col, distance
        $visited[$sr][$sc] = true;

        $items = [];

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];

        while (!$queue->isEmpty()) {
            [$r, $c, $d] = $queue->dequeue();

            $price = $grid[$r][$c];
            if ($price >= $low && $price <= $high) {
                // store as [distance, price, row, col]
                $items[] = [$d, $price, $r, $c];
            }

            foreach ($dirs as $dir) {
                $nr = $r + $dir[0];
                $nc = $c + $dir[1];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n &&
                    !$visited[$nr][$nc] && $grid[$nr][$nc] != 0) {
                    $visited[$nr][$nc] = true;
                    $queue->enqueue([$nr, $nc, $d + 1]);
                }
            }
        }

        usort($items, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];          // distance
            if ($a[1] !== $b[1]) return $a[1] <=> $b[1];          // price
            if ($a[2] !== $b[2]) return $a[2] <=> $b[2];          // row
            return $a[3] <=> $b[3];                              // col
        });

        $result = [];
        $limit = min($k, count($items));
        for ($i = 0; $i < $limit; $i++) {
            $result[] = [$items[$i][2], $items[$i][3]];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func highestRankedKItems(_ grid: [[Int]], _ pricing: [Int], _ start: [Int], _ k: Int) -> [[Int]] {
        let m = grid.count
        let n = grid[0].count
        let total = m * n
        var visited = [Bool](repeating: false, count: total)
        func index(_ r: Int, _ c: Int) -> Int { r * n + c }
        
        var queueR = [Int]()
        var queueC = [Int]()
        var dist = [Int](repeating: 0, count: total)
        var head = 0
        
        let sr = start[0], sc = start[1]
        visited[index(sr, sc)] = true
        queueR.append(sr)
        queueC.append(sc)
        
        let low = pricing[0], high = pricing[1]
        var candidates: [(dist: Int, price: Int, r: Int, c: Int)] = []
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while head < queueR.count {
            let r = queueR[head]
            let c = queueC[head]
            let curDist = dist[index(r, c)]
            
            let price = grid[r][c]
            if price >= low && price <= high {
                candidates.append((dist: curDist, price: price, r: r, c: c))
            }
            
            for (dr, dc) in dirs {
                let nr = r + dr
                let nc = c + dc
                if nr >= 0 && nr < m && nc >= 0 && nc < n {
                    let idx = index(nr, nc)
                    if !visited[idx] && grid[nr][nc] != 0 {
                        visited[idx] = true
                        dist[idx] = curDist + 1
                        queueR.append(nr)
                        queueC.append(nc)
                    }
                }
            }
            head += 1
        }
        
        candidates.sort { a, b in
            if a.dist != b.dist { return a.dist < b.dist }
            if a.price != b.price { return a.price < b.price }
            if a.r != b.r { return a.r < b.r }
            return a.c < b.c
        }
        
        var result: [[Int]] = []
        let limit = min(k, candidates.count)
        for i in 0..<limit {
            result.append([candidates[i].r, candidates[i].c])
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun highestRankedKItems(grid: Array<IntArray>, pricing: IntArray, start: IntArray, k: Int): List<List<Int>> {
        val m = grid.size
        val n = grid[0].size
        val low = pricing[0]
        val high = pricing[1]

        val visited = Array(m) { BooleanArray(n) }
        val maxSize = m * n
        val qRow = IntArray(maxSize)
        val qCol = IntArray(maxSize)
        var head = 0
        var tail = 0

        val sr = start[0]
        val sc = start[1]
        visited[sr][sc] = true
        qRow[tail] = sr
        qCol[tail] = sc
        tail++

        data class Item(val dist: Int, val price: Int, val r: Int, val c: Int)

        val candidates = mutableListOf<Item>()
        var dist = 0
        val dirs = intArrayOf(-1, 0, 1, 0, -1)

        while (head < tail) {
            val levelSize = tail - head
            repeat(levelSize) {
                val r = qRow[head]
                val c = qCol[head]
                head++

                val price = grid[r][c]
                if (price in low..high) {
                    candidates.add(Item(dist, price, r, c))
                }

                for (d in 0 until 4) {
                    val nr = r + dirs[d]
                    val nc = c + dirs[d + 1]
                    if (nr in 0 until m && nc in 0 until n && !visited[nr][nc] && grid[nr][nc] != 0) {
                        visited[nr][nc] = true
                        qRow[tail] = nr
                        qCol[tail] = nc
                        tail++
                    }
                }
            }
            dist++
        }

        candidates.sortWith(
            compareBy<Item> { it.dist }
                .thenBy { it.price }
                .thenBy { it.r }
                .thenBy { it.c }
        )

        val result = mutableListOf<List<Int>>()
        val limit = minOf(k, candidates.size)
        for (i in 0 until limit) {
            val item = candidates[i]
            result.add(listOf(item.r, item.c))
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

class _Item {
  int dist;
  int price;
  int r;
  int c;
  _Item(this.dist, this.price, this.r, this.c);
}

class Solution {
  List<List<int>> highestRankedKItems(
      List<List<int>> grid, List<int> pricing, List<int> start, int k) {
    final int m = grid.length;
    final int n = grid[0].length;
    final int low = pricing[0];
    final int high = pricing[1];
    final int sr = start[0];
    final int sc = start[1];

    final List<List<bool>> visited =
        List.generate(m, (_) => List.filled(n, false));
    final List<List<int>> dist =
        List.generate(m, (_) => List.filled(n, -1));

    Queue<int> q = ListQueue();
    int encode(int r, int c) => r * n + c;

    visited[sr][sc] = true;
    dist[sr][sc] = 0;
    q.addLast(encode(sr, sc));

    final List<_Item> candidates = [];

    const List<List<int>> dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1]
    ];

    while (q.isNotEmpty) {
      final int cur = q.removeFirst();
      final int r = cur ~/ n;
      final int c = cur % n;
      final int d = dist[r][c];
      final int price = grid[r][c];

      if (price >= low && price <= high) {
        candidates.add(_Item(d, price, r, c));
      }

      for (final dir in dirs) {
        final int nr = r + dir[0];
        final int nc = c + dir[1];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
        if (visited[nr][nc]) continue;
        if (grid[nr][nc] == 0) continue;
        visited[nr][nc] = true;
        dist[nr][nc] = d + 1;
        q.addLast(encode(nr, nc));
      }
    }

    candidates.sort((a, b) {
      if (a.dist != b.dist) return a.dist - b.dist;
      if (a.price != b.price) return a.price - b.price;
      if (a.r != b.r) return a.r - b.r;
      return a.c - b.c;
    });

    final int limit = k < candidates.length ? k : candidates.length;
    final List<List<int>> ans = [];
    for (int i = 0; i < limit; ++i) {
      ans.add([candidates[i].r, candidates[i].c]);
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

type item struct {
	r, c  int
	price int
	dist  int
}

func highestRankedKItems(grid [][]int, pricing []int, start []int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	low, high := pricing[0], pricing[1]

	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	dir := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	queue := make([]item, 0, m*n)
	sr, sc := start[0], start[1]
	queue = append(queue, item{sr, sc, grid[sr][sc], 0})
	visited[sr][sc] = true

	candidates := []item{}
	if p := grid[sr][sc]; p >= low && p <= high {
		candidates = append(candidates, item{sr, sc, p, 0})
	}

	for front := 0; front < len(queue); front++ {
		cur := queue[front]
		for _, d := range dir {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n {
				continue
			}
			if visited[nr][nc] || grid[nr][nc] == 0 {
				continue
			}
			visited[nr][nc] = true
			ndist := cur.dist + 1
			queue = append(queue, item{nr, nc, grid[nr][nc], ndist})
			if p := grid[nr][nc]; p >= low && p <= high {
				candidates = append(candidates, item{nr, nc, p, ndist})
			}
		}
	}

	sort.Slice(candidates, func(i, j int) bool {
		a, b := candidates[i], candidates[j]
		if a.dist != b.dist {
			return a.dist < b.dist
		}
		if a.price != b.price {
			return a.price < b.price
		}
		if a.r != b.r {
			return a.r < b.r
		}
		return a.c < b.c
	})

	if k > len(candidates) {
		k = len(candidates)
	}
	ans := make([][]int, k)
	for i := 0; i < k; i++ {
		ans[i] = []int{candidates[i].r, candidates[i].c}
	}
	return ans
}
```

## Ruby

```ruby
def highest_ranked_k_items(grid, pricing, start, k)
  m = grid.size
  n = grid[0].size
  low, high = pricing
  sr, sc = start

  visited = Array.new(m) { Array.new(n, false) }
  queue = []
  head = 0
  queue << [sr, sc, 0]
  visited[sr][sc] = true

  candidates = []
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  while head < queue.length
    r, c, d = queue[head]
    head += 1
    val = grid[r][c]
    if val >= low && val <= high
      candidates << [d, val, r, c]
    end
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next unless nr.between?(0, m - 1) && nc.between?(0, n - 1)
      next if visited[nr][nc] || grid[nr][nc] == 0
      visited[nr][nc] = true
      queue << [nr, nc, d + 1]
    end
  end

  candidates.sort_by! { |d, val, r, c| [d, val, r, c] }
  result = []
  candidates.first(k).each do |_, _, r, c|
    result << [r, c]
  end
  result
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def highestRankedKItems(grid: Array[Array[Int]], pricing: Array[Int], start: Array[Int], k: Int): List[List[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val low = pricing(0)
    val high = pricing(1)

    val visited = Array.ofDim[Boolean](m, n)
    val queue = new mutable.Queue[(Int, Int, Int)]() // row, col, distance

    val sr = start(0)
    val sc = start(1)
    visited(sr)(sc) = true
    queue.enqueue((sr, sc, 0))

    val candidates = new mutable.ArrayBuffer[(Int, Int, Int, Int)]() // (dist, price, row, col)
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))

    while (queue.nonEmpty) {
      val (r, c, d) = queue.dequeue()
      val price = grid(r)(c)
      if (price >= low && price <= high) {
        candidates.append((d, price, r, c))
      }
      for ((dr, dc) <- dirs) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited(nr)(nc) && grid(nr)(nc) != 0) {
          visited(nr)(nc) = true
          queue.enqueue((nr, nc, d + 1))
        }
      }
    }

    val sorted = candidates.sortBy(t => (t._1, t._2, t._3, t._4))
    sorted.take(k).map { case (_, _, r, c) => List(r, c) }.toList
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn highest_ranked_k_items(grid: Vec<Vec<i32>>, pricing: Vec<i32>, start: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let low = pricing[0];
        let high = pricing[1];
        let sr = start[0] as usize;
        let sc = start[1] as usize;

        let mut visited = vec![vec![false; n]; m];
        let mut q: VecDeque<(usize, usize, i32)> = VecDeque::new();
        visited[sr][sc] = true;
        q.push_back((sr, sc, 0));

        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        let mut candidates: Vec<(i32, i32, i32, i32)> = Vec::new();

        while let Some((r, c, d)) = q.pop_front() {
            let price = grid[r][c];
            if price >= low && price <= high {
                candidates.push((d, price, r as i32, c as i32));
            }
            for (dr, dc) in dirs.iter() {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                    continue;
                }
                let ur = nr as usize;
                let uc = nc as usize;
                if !visited[ur][uc] && grid[ur][uc] != 0 {
                    visited[ur][uc] = true;
                    q.push_back((ur, uc, d + 1));
                }
            }
        }

        candidates.sort_by(|a, b| {
            if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else if a.1 != b.1 {
                a.1.cmp(&b.1)
            } else if a.2 != b.2 {
                a.2.cmp(&b.2)
            } else {
                a.3.cmp(&b.3)
            }
        });

        let limit = k as usize;
        let mut result: Vec<Vec<i32>> = Vec::new();
        for i in 0..candidates.len().min(limit) {
            result.push(vec![candidates[i].2, candidates[i].3]);
        }
        result
    }
}
```

## Racket

```racket
(require racket/queue)

(define (highest-ranked-k-items grid pricing start k)
  (let* ((rows (list->vector (map list->vector grid)))
         (m (vector-length rows))
         (n (if (= m 0) 0 (vector-length (vector-ref rows 0))))
         (low (first pricing))
         (high (second pricing))
         (sr (first start))
         (sc (second start))
         (visited (make-vector m))
         (q (make-queue))
         (items '()))
    ;; initialize visited matrix
    (for ([i (in-range m)])
      (vector-set! visited i (make-vector n #f)))
    ;; enqueue start position
    (enqueue! q (list sr sc 0))
    (vector-set! (vector-ref visited sr) sc #t)
    (let loop ()
      (unless (queue-empty? q)
        (define cur (dequeue! q))
        (define r (first cur))
        (define c (second cur))
        (define d (third cur))
        (define price (vector-ref (vector-ref rows r) c))
        ;; collect if within price range
        (when (and (>= price low) (<= price high))
          (set! items (cons (list d price r c) items)))
        ;; explore neighbors
        (for ([drdc '((-1 . 0) (1 . 0) (0 . -1) (0 . 1))])
          (define dr (car drdc))
          (define dc (cdr drdc))
          (define nr (+ r dr))
          (define nc (+ c dc))
          (when (and (>= nr 0) (< nr m)
                     (>= nc 0) (< nc n)
                     (not (vector-ref (vector-ref visited nr) nc)))
            (define cell-price (vector-ref (vector-ref rows nr) nc))
            (when (> cell-price 0)
              (vector-set! (vector-ref visited nr) nc #t)
              (enqueue! q (list nr nc (+ d 1))))))
        (loop)))
    ;; sort collected items by distance, price, row, column
    (define sorted-items
      (sort items
            (lambda (a b)
              (or (< (first a) (first b))
                  (and (= (first a) (first b))
                       (or (< (second a) (second b))
                           (and (= (second a) (second b))
                                (or (< (third a) (third b))
                                    (and (= (third a) (third b))
                                         (< (fourth a) (fourth b))))))))))
    ;; take first k positions
    (let ((result '()))
      (for ([i (in-range (min k (length sorted-items)))])
        (define item (list-ref sorted-items i))
        (set! result (cons (list (third item) (fourth item)) result)))
      (reverse result))))
```

## Erlang

```erlang
-spec highest_ranked_k_items(Grid :: [[integer()]], Pricing :: [integer()], Start :: [integer()], K :: integer()) -> [[integer()]].
highest_ranked_k_items(Grid, Pricing, Start, K) ->
    {Low, High} = case Pricing of
        [L, H] -> {L, H}
    end,
    [SR, SC] = Start,
    M = length(Grid),
    N = case Grid of
            [] -> 0;
            [Row | _] -> length(Row)
        end,
    GridTuples = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    Visited0 = maps:put({SR, SC}, true, #{}),
    Queue0 = queue:in({SR, SC, 0}, queue:new()),
    Items0 = [],
    {_Visited, Items} = bfs(Queue0, Visited0, Items0, GridTuples, M, N, Low, High),
    Sorted = lists:sort(fun compare/2, Items),
    TopK = lists:sublist(Sorted, K),
    [ [R, C] || {_Dist, _Price, R, C} <- TopK ].

compare({D1, P1, R1, C1}, {D2, P2, R2, C2}) ->
    case D1 < D2 of
        true -> true;
        false when D1 > D2 -> false;
        false ->
            case P1 < P2 of
                true -> true;
                false when P1 > P2 -> false;
                false ->
                    case R1 < R2 of
                        true -> true;
                        false when R1 > R2 -> false;
                        false -> C1 =< C2
                    end
            end
    end.

bfs(Queue, Visited, Items, GridTuples, M, N, Low, High) ->
    case queue:out(Queue) of
        {empty, _} ->
            {Visited, Items};
        {{value, {R, C, D}}, Q1} ->
            Value = get_value(GridTuples, R, C),
            Items1 = if Value >= Low, Value =< High -> [{D, Value, R, C} | Items];
                     true -> Items
                     end,
            Directions = [{-1,0}, {1,0}, {0,-1}, {0,1}],
            {Q2, Visited2} = lists:foldl(
                fun({DR, DC}, {QAcc, VAcc}) ->
                    NR = R + DR,
                    NC = C + DC,
                    if NR >= 0, NR < M, NC >= 0, NC < N,
                       not maps:is_key({NR, NC}, VAcc) ->
                           ValN = get_value(GridTuples, NR, NC),
                           if ValN =/= 0 ->
                                   {queue:in({NR, NC, D + 1}, QAcc), maps:put({NR, NC}, true, VAcc)};
                              true -> {QAcc, VAcc}
                           end;
                       true -> {QAcc, VAcc}
                    end
                end,
                {Q1, Visited},
                Directions),
            bfs(Q2, Visited2, Items1, GridTuples, M, N, Low, High)
    end.

get_value(GridTuples, R, C) ->
    RowTuple = element(R + 1, GridTuples),
    element(C + 1, RowTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec highest_ranked_k_items(grid :: [[integer]], pricing :: [integer], start :: [integer], k :: integer) :: [[integer]]
  def highest_ranked_k_items(grid, pricing, start, k) do
    low = Enum.at(pricing, 0)
    high = Enum.at(pricing, 1)

    rows = length(grid)
    cols = grid |> hd() |> length()

    sr = Enum.at(start, 0)
    sc = Enum.at(start, 1)

    queue = :queue.from_list([{sr, sc, 0}])
    visited = MapSet.new()
    items = bfs_collect(grid, low, high, rows, cols, queue, visited, [])

    sorted =
      items
      |> Enum.sort_by(fn {dist, price, r, c} -> {dist, price, r, c} end)

    sorted
    |> Enum.take(k)
    |> Enum.map(fn {_d, _p, r, c} -> [r, c] end)
  end

  defp bfs_collect(_grid, _low, _high, _rows, _cols, queue, _visited, acc) do
    case :queue.out(queue) do
      {:empty, _} ->
        acc

      {{:value, {r, c, d}}, q_rest} ->
        # we will handle visited inside recursion to avoid re-adding same cell multiple times
        bfs_collect_step(_grid, _low, _high, _rows, _cols, {r, c, d}, q_rest, acc)
    end
  end

  defp bfs_collect_step(grid, low, high, rows, cols, {r, c, d}, queue, acc) do
    visited = MapSet.new()
    bfs(
      grid,
      low,
      high,
      rows,
      cols,
      :queue.in({r, c, d}, queue),
      visited,
      acc
    )
  end

  defp bfs(grid, low, high, rows, cols, queue, visited, acc) do
    case :queue.out(queue) do
      {:empty, _} ->
        acc

      {{:value, {r, c, d}}, q_rest} ->
        if MapSet.member?(visited, {r, c}) do
          bfs(grid, low, high, rows, cols, q_rest, visited, acc)
        else
          visited = MapSet.put(visited, {r, c})
          val = get_cell(grid, r, c)

          acc =
            if val >= low and val <= high do
              [{d, val, r, c} | acc]
            else
              acc
            end

          dirs = [{1, 0}, {-1, 0}, {0, 1}, {0, -1}]

          q_next =
            Enum.reduce(dirs, q_rest, fn {dr, dc}, q ->
              nr = r + dr
              nc = c + dc

              if nr >= 0 and nr < rows and nc >= 0 and nc < cols do
                nval = get_cell(grid, nr, nc)

                if nval != 0 and not MapSet.member?(visited, {nr, nc}) do
                  :queue.in({nr, nc, d + 1}, q)
                else
                  q
                end
              else
                q
              end
            end)

          bfs(grid, low, high, rows, cols, q_next, visited, acc)
        end
    end
  end

  defp get_cell(grid, r, c) do
    grid |> Enum.at(r) |> Enum.at(c)
  end
end
```

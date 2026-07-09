# 1970. Last Day Where You Can Still Cross

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> p, sz;
        DSU(int n) : p(n), sz(n,1) { iota(p.begin(), p.end(), 0); }
        int find(int x){ return p[x]==x? x : p[x]=find(p[x]); }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(sz[a]<sz[b]) swap(a,b);
            p[b]=a; sz[a]+=sz[b];
        }
    };
    
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        int n = row * col;
        DSU dsu(n + 2);
        const int TOP = n;
        const int BOTTOM = n + 1;
        vector<char> land(n, false);
        const int dr[4] = {-1, 1, 0, 0};
        const int dc[4] = {0, 0, -1, 1};
        
        for (int i = n - 1; i >= 0; --i) {
            int r = cells[i][0] - 1;
            int c = cells[i][1] - 1;
            int idx = r * col + c;
            land[idx] = true;
            
            if (r == 0) dsu.unite(idx, TOP);
            if (r == row - 1) dsu.unite(idx, BOTTOM);
            
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
                    int nidx = nr * col + nc;
                    if (land[nidx]) dsu.unite(idx, nidx);
                }
            }
            
            if (dsu.find(TOP) == dsu.find(BOTTOM)) return i;
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    private static class DSU {
        int[] parent;
        int[] size;
        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }

    public int latestDayToCross(int row, int col, int[][] cells) {
        int total = row * col;
        DSU dsu = new DSU(total + 2);
        int top = total;       // virtual top node
        int bottom = total + 1; // virtual bottom node

        boolean[] land = new boolean[total];
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

        for (int i = cells.length - 1; i >= 0; --i) {
            int r = cells[i][0] - 1;
            int c = cells[i][1] - 1;
            int id = r * col + c;
            land[id] = true;

            if (r == 0) dsu.union(id, top);
            if (r == row - 1) dsu.union(id, bottom);

            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
                    int nid = nr * col + nc;
                    if (land[nid]) {
                        dsu.union(id, nid);
                    }
                }
            }

            if (dsu.find(top) == dsu.find(bottom)) {
                return i + 1; // days are 1-indexed
            }
        }
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        # day when each cell becomes water (1-indexed)
        flood_day = [[0] * col for _ in range(row)]
        for i, (r, c) in enumerate(cells):
            flood_day[r - 1][c - 1] = i + 1

        from collections import deque

        def can_cross(day):
            """return True if there is a path using only cells with flood_day > day"""
            visited = [[False] * col for _ in range(row)]
            q = deque()
            # start from any land cell in the top row
            for c in range(col):
                if flood_day[0][c] > day:
                    visited[0][c] = True
                    q.append((0, c))
            while q:
                r, c = q.popleft()
                if r == row - 1:   # reached bottom
                    return True
                nr = r + 1
                if nr < row and not visited[nr][c] and flood_day[nr][c] > day:
                    visited[nr][c] = True
                    q.append((nr, c))
                nr = r - 1
                if nr >= 0 and not visited[nr][c] and flood_day[nr][c] > day:
                    visited[nr][c] = True
                    q.append((nr, c))
                nc = c + 1
                if nc < col and not visited[r][nc] and flood_day[r][nc] > day:
                    visited[r][nc] = True
                    q.append((r, nc))
                nc = c - 1
                if nc >= 0 and not visited[r][nc] and flood_day[r][nc] > day:
                    visited[r][nc] = True
                    q.append((r, nc))
            return False

        low, high = 0, row * col
        while low < high:
            mid = (low + high + 1) // 2
            if can_cross(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## Python3

```python
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        total = row * col
        top = total          # virtual node for top row
        bottom = total + 1   # virtual node for bottom row
        dsu = DSU(total + 2)

        land = [[False] * col for _ in range(row)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i]
            r -= 1
            c -= 1
            land[r][c] = True
            idx = r * col + c

            if r == 0:
                dsu.union(idx, top)
            if r == row - 1:
                dsu.union(idx, bottom)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and land[nr][nc]:
                    nidx = nr * col + nc
                    dsu.union(idx, nidx)

            if dsu.find(top) == dsu.find(bottom):
                return i

        return -1
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static bool canCross(int day, int row, int col, int **cells) {
    int n = row * col;
    char *water = (char *)calloc(n, sizeof(char));
    for (int i = 0; i < day; ++i) {
        int r = cells[i][0] - 1;
        int c = cells[i][1] - 1;
        water[r * col + c] = 1;
    }

    char *vis = (char *)calloc(n, sizeof(char));
    int *queue = (int *)malloc(n * sizeof(int));
    int head = 0, tail = 0;

    for (int c = 0; c < col; ++c) {
        int idx = c; // top row (row 0)
        if (!water[idx]) {
            vis[idx] = 1;
            queue[tail++] = idx;
        }
    }

    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    while (head < tail) {
        int cur = queue[head++];
        int r = cur / col;
        int c = cur % col;
        if (r == row - 1) {
            free(water);
            free(vis);
            free(queue);
            return true;
        }
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
                int nid = nr * col + nc;
                if (!water[nid] && !vis[nid]) {
                    vis[nid] = 1;
                    queue[tail++] = nid;
                }
            }
        }
    }

    free(water);
    free(vis);
    free(queue);
    return false;
}

int latestDayToCross(int row, int col, int** cells, int cellsSize, int* cellsColSize) {
    (void)cellsColSize; // unused
    int low = 0, high = cellsSize; // inclusive range of days
    while (low < high) {
        int mid = low + (high - low + 1) / 2;
        if (canCross(mid, row, col, cells))
            low = mid;
        else
            high = mid - 1;
    }
    return low;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int LatestDayToCross(int row, int col, int[][] cells) {
        int left = 1;
        int right = row * col;
        int ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (CanCross(mid, row, col, cells)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    private bool CanCross(int day, int row, int col, int[][] cells) {
        bool[,] water = new bool[row, col];
        for (int i = 0; i < day; i++) {
            var c = cells[i];
            water[c[0] - 1, c[1] - 1] = true;
        }

        Queue<(int r, int c)> q = new Queue<(int, int)>();
        bool[,] visited = new bool[row, col];

        for (int j = 0; j < col; j++) {
            if (!water[0, j]) {
                q.Enqueue((0, j));
                visited[0, j] = true;
            }
        }

        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };

        while (q.Count > 0) {
            var cur = q.Dequeue();
            if (cur.r == row - 1) return true;

            for (int k = 0; k < 4; k++) {
                int nr = cur.r + dr[k];
                int nc = cur.c + dc[k];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                    !water[nr, nc] && !visited[nr, nc]) {
                    visited[nr, nc] = true;
                    q.Enqueue((nr, nc));
                }
            }
        }

        return false;
    }
}
```

## Javascript

```javascript
var latestDayToCross = function(row, col, cells) {
    const total = row * col;
    const canCross = (day) => {
        const water = new Uint8Array(total);
        for (let i = 0; i < day; i++) {
            const [r, c] = cells[i];
            water[(r - 1) * col + (c - 1)] = 1;
        }
        const visited = new Uint8Array(total);
        const queue = [];
        for (let c = 0; c < col; c++) {
            const idx = c; // top row index
            if (!water[idx]) {
                visited[idx] = 1;
                queue.push(idx);
            }
        }
        let head = 0;
        while (head < queue.length) {
            const cur = queue[head++];
            const r = Math.floor(cur / col);
            const c = cur % col;
            if (r === row - 1) return true;
            // up
            if (r > 0) {
                const nb = cur - col;
                if (!water[nb] && !visited[nb]) {
                    visited[nb] = 1;
                    queue.push(nb);
                }
            }
            // down
            if (r < row - 1) {
                const nb = cur + col;
                if (!water[nb] && !visited[nb]) {
                    visited[nb] = 1;
                    queue.push(nb);
                }
            }
            // left
            if (c > 0) {
                const nb = cur - 1;
                if (!water[nb] && !visited[nb]) {
                    visited[nb] = 1;
                    queue.push(nb);
                }
            }
            // right
            if (c < col - 1) {
                const nb = cur + 1;
                if (!water[nb] && !visited[nb]) {
                    visited[nb] = 1;
                    queue.push(nb);
                }
            }
        }
        return false;
    };
    let left = 0, right = total;
    while (left < right) {
        const mid = Math.floor((left + right + 1) / 2);
        if (canCross(mid)) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function latestDayToCross(row: number, col: number, cells: number[][]): number {
    const total = row * col;

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ] as const;

    const canCross = (day: number): boolean => {
        // build grid where 1 = water, 0 = land
        const grid: Uint8Array[] = Array.from({ length: row }, () => new Uint8Array(col));
        for (let i = 0; i < day; ++i) {
            const [r, c] = cells[i];
            grid[r - 1][c - 1] = 1;
        }

        const visited: Uint8Array[] = Array.from({ length: row }, () => new Uint8Array(col));
        const queue: number[] = [];
        let qIdx = 0;

        // start from all land cells in top row
        for (let c = 0; c < col; ++c) {
            if (!grid[0][c]) {
                visited[0][c] = 1;
                queue.push(c); // position encoded as r*col + c, here r=0
            }
        }

        while (qIdx < queue.length) {
            const pos = queue[qIdx++];
            const r = Math.floor(pos / col);
            const c = pos % col;

            if (r === row - 1) return true; // reached bottom

            for (const [dr, dc] of dirs) {
                const nr = r + dr;
                const nc = c + dc;
                if (
                    nr >= 0 && nr < row &&
                    nc >= 0 && nc < col &&
                    !grid[nr][nc] &&
                    !visited[nr][nc]
                ) {
                    visited[nr][nc] = 1;
                    queue.push(nr * col + nc);
                }
            }
        }

        return false;
    };

    let low = 0;
    let high = total; // inclusive upper bound where crossing is impossible

    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (canCross(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }

    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $row
     * @param Integer $col
     * @param Integer[][] $cells
     * @return Integer
     */
    function latestDayToCross($row, $col, $cells) {
        $n = $row * $col;
        $low = 1;
        $high = $n;
        $ans = 0;

        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canCross($mid, $row, $col, $cells)) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }

        return $ans;
    }

    private function canCross($day, $row, $col, $cells) {
        // build grid: true = water, false = land
        $grid = array_fill(0, $row, array_fill(0, $col, false));
        for ($i = 0; $i < $day; $i++) {
            [$r, $c] = $cells[$i];
            $grid[$r - 1][$c - 1] = true;
        }

        $queue = new SplQueue();
        $visited = array_fill(0, $row, array_fill(0, $col, false));

        // enqueue all land cells in the top row
        for ($c = 0; $c < $col; $c++) {
            if (!$grid[0][$c]) {
                $queue->enqueue([0, $c]);
                $visited[0][$c] = true;
            }
        }

        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        while (!$queue->isEmpty()) {
            [$r, $c] = $queue->dequeue();
            if ($r == $row - 1) {
                return true;
            }
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $row && $nc >= 0 && $nc < $col &&
                    !$grid[$nr][$nc] && !$visited[$nr][$nc]) {
                    $visited[$nr][$nc] = true;
                    $queue->enqueue([$nr, $nc]);
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
    func latestDayToCross(_ row: Int, _ col: Int, _ cells: [[Int]]) -> Int {
        var left = 1
        var right = row * col
        var answer = 0
        
        while left <= right {
            let mid = (left + right) / 2
            if canCross(day: mid, row: row, col: col, cells: cells) {
                answer = mid
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return answer
    }
    
    private func canCross(day: Int, row: Int, col: Int, cells: [[Int]]) -> Bool {
        var water = Array(repeating: false, count: row * col)
        for i in 0..<day {
            let r = cells[i][0] - 1
            let c = cells[i][1] - 1
            water[r * col + c] = true
        }
        
        var visited = Array(repeating: false, count: row * col)
        var queue = [Int]()
        var head = 0
        
        // enqueue all land cells in the top row
        for c in 0..<col {
            let idx = c
            if !water[idx] {
                visited[idx] = true
                queue.append(idx)
            }
        }
        
        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while head < queue.count {
            let cur = queue[head]
            head += 1
            let r = cur / col
            let c = cur % col
            
            if r == row - 1 { // reached bottom row
                return true
            }
            
            for (dr, dc) in directions {
                let nr = r + dr
                let nc = c + dc
                if nr >= 0 && nr < row && nc >= 0 && nc < col {
                    let nIdx = nr * col + nc
                    if !water[nIdx] && !visited[nIdx] {
                        visited[nIdx] = true
                        queue.append(nIdx)
                    }
                }
            }
        }
        
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun latestDayToCross(row: Int, col: Int, cells: Array<IntArray>): Int {
        val total = row * col
        val rArr = IntArray(total)
        val cArr = IntArray(total)
        for (i in 0 until total) {
            rArr[i] = cells[i][0] - 1
            cArr[i] = cells[i][1] - 1
        }

        fun canCross(day: Int): Boolean {
            val flooded = BooleanArray(total)
            for (i in 0 until day) {
                flooded[rArr[i] * col + cArr[i]] = true
            }
            val dsu = DSU(total + 2)
            val top = total
            val bottom = total + 1
            val dirs = intArrayOf(-1, 0, 1, 0, -1)

            for (r in 0 until row) {
                for (c in 0 until col) {
                    val idx = r * col + c
                    if (flooded[idx]) continue
                    if (r == 0) dsu.union(idx, top)
                    if (r == row - 1) dsu.union(idx, bottom)
                    for (k in 0 until 4) {
                        val nr = r + dirs[k]
                        val nc = c + dirs[k + 1]
                        if (nr < 0 || nr >= row || nc < 0 || nc >= col) continue
                        val nIdx = nr * col + nc
                        if (!flooded[nIdx]) dsu.union(idx, nIdx)
                    }
                }
            }
            return dsu.find(top) == dsu.find(bottom)
        }

        var low = 0
        var high = total
        while (low < high) {
            val mid = (low + high + 1) / 2
            if (canCross(mid)) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }

    private class DSU(n: Int) {
        private val parent = IntArray(n) { it }
        private val rank = IntArray(n)

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra
            } else {
                parent[rb] = ra
                rank[ra]++
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  int latestDayToCross(int row, int col, List<List<int>> cells) {
    bool canCross(int day) {
      List<List<bool>> water = List.generate(row, (_) => List.filled(col, false));
      for (int i = 0; i < day; ++i) {
        var rc = cells[i];
        int r = rc[0] - 1;
        int c = rc[1] - 1;
        water[r][c] = true;
      }
      List<List<bool>> visited = List.generate(row, (_) => List.filled(col, false));
      int total = row * col;
      List<int> q = List.filled(total, 0);
      int qs = 0, qe = 0;
      for (int c = 0; c < col; ++c) {
        if (!water[0][c]) {
          visited[0][c] = true;
          q[qe++] = c;
        }
      }
      while (qs < qe) {
        int idx = q[qs++];
        int r = idx ~/ col;
        int c = idx % col;
        if (r == row - 1) return true;
        if (r > 0 && !water[r - 1][c] && !visited[r - 1][c]) {
          visited[r - 1][c] = true;
          q[qe++] = (r - 1) * col + c;
        }
        if (r + 1 < row && !water[r + 1][c] && !visited[r + 1][c]) {
          visited[r + 1][c] = true;
          q[qe++] = (r + 1) * col + c;
        }
        if (c > 0 && !water[r][c - 1] && !visited[r][c - 1]) {
          visited[r][c - 1] = true;
          q[qe++] = r * col + (c - 1);
        }
        if (c + 1 < col && !water[r][c + 1] && !visited[r][c + 1]) {
          visited[r][c + 1] = true;
          q[qe++] = r * col + (c + 1);
        }
      }
      return false;
    }

    int left = 0, right = cells.length;
    while (left < right) {
      int mid = (left + right + 1) >> 1;
      if (canCross(mid)) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }
    return left;
  }
}
```

## Golang

```go
func latestDayToCross(row int, col int, cells [][]int) int {
	type dsu struct {
		parent []int
		rank   []int
	}
	newDSU := func(n int) *dsu {
		p := make([]int, n)
		r := make([]int, n)
		for i := 0; i < n; i++ {
			p[i] = i
			r[i] = 1
		}
		return &dsu{parent: p, rank: r}
	}
	var find func(*dsu, int) int
	find = func(d *dsu, x int) int {
		if d.parent[x] != x {
			d.parent[x] = find(d, d.parent[x])
		}
		return d.parent[x]
	}
	union := func(d *dsu, a, b int) {
		ra := find(d, a)
		rb := find(d, b)
		if ra == rb {
			return
		}
		if d.rank[ra] < d.rank[rb] {
			ra, rb = rb, ra
		}
		d.parent[rb] = ra
		if d.rank[ra] == d.rank[rb] {
			d.rank[ra]++
		}
	}

	n := row * col
	top := n
	bottom := n + 1
	ds := newDSU(n + 2)
	visited := make([]bool, n)

	dirR := []int{-1, 1, 0, 0}
	dirC := []int{0, 0, -1, 1}

	for i := n - 1; i >= 0; i-- {
		r := cells[i][0] - 1
		c := cells[i][1] - 1
		idx := r*col + c
		visited[idx] = true

		if r == 0 {
			union(ds, idx, top)
		}
		if r == row-1 {
			union(ds, idx, bottom)
		}

		for d := 0; d < 4; d++ {
			nr := r + dirR[d]
			nc := c + dirC[d]
			if nr >= 0 && nr < row && nc >= 0 && nc < col {
				nIdx := nr*col + nc
				if visited[nIdx] {
					union(ds, idx, nIdx)
				}
			}
		}

		if find(ds, top) == find(ds, bottom) {
			return i
		}
	}
	return 0
}
```

## Ruby

```ruby
def latest_day_to_cross(row, col, cells)
  total = row * col
  top = total
  bottom = total + 1
  parent = Array.new(total + 2) { |i| i }
  rank = Array.new(total + 2, 0)
  land = Array.new(total, false)

  dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if rank[ra] < rank[rb]
      parent[ra] = rb
    elsif rank[ra] > rank[rb]
      parent[rb] = ra
    else
      parent[rb] = ra
      rank[ra] += 1
    end
  end

  (cells.length - 1).downto(0) do |i|
    r, c = cells[i]
    r -= 1
    c -= 1
    idx = r * col + c
    land[idx] = true

    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= row || nc < 0 || nc >= col
      nidx = nr * col + nc
      union.call(idx, nidx) if land[nidx]
    end

    union.call(idx, top) if r == 0
    union.call(idx, bottom) if r == row - 1

    return i if find.call(top) == find.call(bottom)
  end

  0
end
```

## Scala

```scala
object Solution {
  class DSU(size: Int) {
    private val parent = Array.tabulate(size)(i => i)
    private val rank = new Array[Int](size)

    def find(x: Int): Int = {
      var v = x
      while (parent(v) != v) {
        parent(v) = parent(parent(v))
        v = parent(v)
      }
      v
    }

    def union(a: Int, b: Int): Unit = {
      var ra = find(a)
      var rb = find(b)
      if (ra == rb) return
      if (rank(ra) < rank(rb)) {
        parent(ra) = rb
      } else if (rank(ra) > rank(rb)) {
        parent(rb) = ra
      } else {
        parent(rb) = ra
        rank(ra) += 1
      }
    }

    def connected(a: Int, b: Int): Boolean = find(a) == find(b)
  }

  def latestDayToCross(row: Int, col: Int, cells: Array[Array[Int]]): Int = {
    val total = row * col
    val top = total
    val bottom = total + 1
    val dsu = new DSU(total + 2)
    val land = new Array[Boolean](total)

    val dirs = Array((-1, 0), (1, 0), (0, -1), (0, 1))

    for (i <- (cells.length - 1) to 0 by -1) {
      val r = cells(i)(0) - 1
      val c = cells(i)(1) - 1
      val idx = r * col + c
      land(idx) = true

      if (r == 0) dsu.union(idx, top)
      if (r == row - 1) dsu.union(idx, bottom)

      for ((dr, dc) <- dirs) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < row && nc >= 0 && nc < col) {
          val nIdx = nr * col + nc
          if (land(nIdx)) dsu.union(idx, nIdx)
        }
      }

      if (dsu.connected(top, bottom)) return i + 1 // days are 1‑based in answer
    }
    0
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let r = row as usize;
        let c = col as usize;
        let n = r * c;
        let mut flood_day = vec![0i32; n];
        for (i, cell) in cells.iter().enumerate() {
            let rr = (cell[0] - 1) as usize;
            let cc = (cell[1] - 1) as usize;
            let idx = rr * c + cc;
            flood_day[idx] = (i + 1) as i32; // day when this cell becomes water
        }

        fn can_cross(day: i32, r: usize, c: usize, flood_day: &Vec<i32>) -> bool {
            let mut visited = vec![false; r * c];
            let mut q = VecDeque::new();

            // start from any land cell in the top row
            for col in 0..c {
                let idx = col;
                if flood_day[idx] > day {
                    visited[idx] = true;
                    q.push_back(idx);
                }
            }

            while let Some(cur) = q.pop_front() {
                let cr = cur / c;
                let cc = cur % c;
                if cr == r - 1 {
                    return true; // reached bottom row
                }
                // up
                if cr > 0 {
                    let nidx = (cr - 1) * c + cc;
                    if !visited[nidx] && flood_day[nidx] > day {
                        visited[nidx] = true;
                        q.push_back(nidx);
                    }
                }
                // down
                if cr + 1 < r {
                    let nidx = (cr + 1) * c + cc;
                    if !visited[nidx] && flood_day[nidx] > day {
                        visited[nidx] = true;
                        q.push_back(nidx);
                    }
                }
                // left
                if cc > 0 {
                    let nidx = cr * c + (cc - 1);
                    if !visited[nidx] && flood_day[nidx] > day {
                        visited[nidx] = true;
                        q.push_back(nidx);
                    }
                }
                // right
                if cc + 1 < c {
                    let nidx = cr * c + (cc + 1);
                    if !visited[nidx] && flood_day[nidx] > day {
                        visited[nidx] = true;
                        q.push_back(nidx);
                    }
                }
            }
            false
        }

        // binary search for the last feasible day
        let mut left = 0i32;
        let mut right = n as i32; // inclusive upper bound (day where all cells are water)
        while left < right {
            let mid = (left + right + 1) / 2;
            if can_cross(mid, r, c, &flood_day) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        left
    }
}
```

## Racket

```racket
(define (make-uf n)
  (values (make-vector n 0) (make-vector n 0)))

(define (find parent x)
  (let ((p (vector-ref parent x)))
    (if (= p x)
        x
        (let ((root (find parent p)))
          (vector-set! parent x root)
          root))))

(define (union! parent rank x y)
  (let ((rx (find parent x))
        (ry (find parent y)))
    (when (not (= rx ry))
      (let ((rankx (vector-ref rank rx))
            (ranky (vector-ref rank ry)))
        (cond
          [(< rankx ranky) (vector-set! parent rx ry)]
          [(> rankx ranky) (vector-set! parent ry rx)]
          [else
           (vector-set! parent ry rx)
           (vector-set! rank rx (+ rankx 1))])))))

(define (latest-day-to-cross row col cells)
  (let* ((total (* row col))
         (day-vec (make-vector total)))
    ;; map each day to its cell index (0‑based)
    (for ([i (in-range total)])
      (let* ((cell (list-ref cells i))
             (r (- (first cell) 1))
             (c (- (second cell) 1))
             (idx (+ (* r col) c)))
        (vector-set! day-vec i idx)))
    ;; predicate: can we cross after `day` floods?
    (define (can-cross? day)
      (let ((land (make-vector total #t)))
        ;; mark flooded cells
        (for ([i (in-range day)])
          (let ((idx (vector-ref day-vec i)))
            (vector-set! land idx #f)))
        ;; union‑find with two virtual nodes
        (define-values (parent rank) (make-uf (+ total 2)))
        (let ((virtual-top total)
              (virtual-bottom (+ total 1)))
          ;; initialise parents
          (for ([i (in-range (+ total 2))])
            (vector-set! parent i i))
          ;; process each land cell
          (for ([idx (in-range total)])
            (when (vector-ref land idx)
              (let* ((r (quotient idx col))
                     (c (remainder idx col)))
                (when (= r 0) (union! parent rank idx virtual-top))
                (when (= r (- row 1)) (union! parent rank idx virtual-bottom))
                ;; neighbours: up, down, left, right
                (let ((neighbors
                       (list (and (> r 0) (+ (* (- r 1) col) c))
                             (and (< r (- row 1)) (+ (* (+ r 1) col) c))
                             (and (> c 0) (+ (* r col) (- c 1)))
                             (and (< c (- col 1)) (+ (* r col) (+ c 1))))))
                  (for ([n neighbors])
                    (when n
                      (when (vector-ref land n)
                        (union! parent rank idx n)))))))))
          (= (find parent virtual-top) (find parent virtual-bottom)))))
    ;; binary search for the greatest feasible day
    (let loop ((lo 0) (hi total))
      (if (= lo hi)
          lo
          (let ((mid (quotient (+ lo hi 1) 2))) ; upper mid
            (if (can-cross? mid)
                (loop mid hi)
                (loop lo (- mid 1))))))))
```

## Erlang

```erlang
-spec latest_day_to_cross(Row :: integer(), Col :: integer(), Cells :: [[integer()]]) -> integer().
latest_day_to_cross(Row, Col, Cells) ->
    FloodMap = build_flood_map(Cells),
    N = length(Cells),
    binary_search(0, N, Row, Col, FloodMap).

build_flood_map(Cells) -> build_flood_map(Cells, 1, #{}).
build_flood_map([], _, Map) -> Map;
build_flood_map([[R, C] | Rest], Day, Map) ->
    NewMap = maps:put({R, C}, Day, Map),
    build_flood_map(Rest, Day + 1, NewMap).

binary_search(Low, High, Row, Col, FloodMap) when Low >= High -> Low;
binary_search(Low, High, Row, Col, FloodMap) ->
    Mid = (Low + High + 1) div 2,
    case can_cross(Mid, Row, Col, FloodMap) of
        true -> binary_search(Mid, High, Row, Col, FloodMap);
        false -> binary_search(Low, Mid - 1, Row, Col, FloodMap)
    end.

can_cross(Day, Row, Col, FloodMap) ->
    Top = [ {1, C}
            || C <- lists:seq(1, Col),
               maps:get({1, C}, FloodMap, 0) > Day ],
    Queue0 = queue:from_list(Top),
    bfs(Queue0, #{}, Day, Row, Col, FloodMap).

bfs(Queue, Visited, Day, Row, Col, FloodMap) ->
    case queue:is_empty(Queue) of
        true -> false;
        false ->
            {{value, {R, C}}, Q1} = queue:out(Queue),
            if maps:is_key({R, C}, Visited) ->
                    bfs(Q1, Visited, Day, Row, Col, FloodMap);
               R == Row ->
                    true;
               true ->
                    Vis1 = maps:put({R, C}, true, Visited),
                    Neigh = [{R - 1, C}, {R + 1, C}, {R, C - 1}, {R, C + 1}],
                    Q2 = lists:foldl(
                            fun ({Nr, Nc} = Pos, AccQ) ->
                                    if Nr >= 1, Nr =< Row,
                                       Nc >= 1, Nc =< Col,
                                       maps:get(Pos, FloodMap, 0) > Day,
                                       not maps:is_key(Pos, Vis1) ->
                                            queue:in(Pos, AccQ);
                                       true -> AccQ
                                    end
                            end,
                            Q1,
                            Neigh),
                    bfs(Q2, Vis1, Day, Row, Col, FloodMap)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec latest_day_to_cross(row :: integer, col :: integer, cells :: [[integer]]) :: integer
  def latest_day_to_cross(row, col, cells) do
    n = row * col
    top = n
    bottom = n + 1

    # initialize Union-Find structures
    parent =
      Enum.reduce(0..(n + 1), %{}, fn i, acc ->
        Map.put(acc, i, i)
      end)

    size =
      Enum.reduce(0..(n + 1), %{}, fn i, acc ->
        Map.put(acc, i, 1)
      end)

    # land array: false initially
    land = :array.new(n, default: false)

    go(n - 1, parent, size, land, cells, row, col, top, bottom)
  end

  defp go(-1, _parent, _size, _land, _cells, _row, _col, _top, _bottom), do: 0

  defp go(i, parent, size, land, cells, row, col, top, bottom) do
    [r, c] = Enum.at(cells, i)
    idx = (r - 1) * col + (c - 1)
    land2 = :array.set(idx, true, land)

    {parent1, size1} =
      if r == 1 do
        union(parent, size, idx, top)
      else
        {parent, size}
      end

    {parent2, size2} =
      if r == row do
        union(parent1, size1, idx, bottom)
      else
        {parent1, size1}
      end

    dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    {parent3, size3, _land3} =
      Enum.reduce(dirs, {parent2, size2, land2}, fn {dr, dc},
                                                   {p_acc, s_acc, l_acc} ->
        nr = r + dr
        nc = c + dc

        if nr >= 1 and nr <= row and nc >= 1 and nc <= col do
          nidx = (nr - 1) * col + (nc - 1)

          if :array.get(nidx, l_acc) do
            {p_new, s_new} = union(p_acc, s_acc, idx, nidx)
            {p_new, s_new, l_acc}
          else
            {p_acc, s_acc, l_acc}
          end
        else
          {p_acc, s_acc, l_acc}
        end
      end)

    # check connectivity between top and bottom
    {parent4, root_top} = find(parent3, top)
    {parent5, root_bottom} = find(parent4, bottom)

    if root_top == root_bottom do
      i
    else
      go(i - 1, parent5, size3, land2, cells, row, col, top, bottom)
    end
  end

  defp find(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      {parent, x}
    else
      {parent2, root} = find(parent, p)
      {Map.put(parent2, x, root), root}
    end
  end

  defp union(parent, size, a, b) do
    {parent1, ra} = find(parent, a)
    {parent2, rb} = find(parent1, b)

    if ra == rb do
      {parent2, size}
    else
      sa = Map.get(size, ra)
      sb = Map.get(size, rb)

      cond do
        sa < sb ->
          parent3 = Map.put(parent2, ra, rb)
          size3 = Map.put(size, rb, sa + sb)
          {parent3, size3}

        true ->
          parent3 = Map.put(parent2, rb, ra)
          size3 = Map.put(size, ra, sa + sb)
          {parent3, size3}
      end
    end
  end
end
```

# 0675. Cut Off Trees for Golf Event

## Cpp

```cpp
class Solution {
public:
    int bfs(const vector<vector<int>>& forest, int sr, int sc, int tr, int tc) {
        if (sr == tr && sc == tc) return 0;
        int R = forest.size(), C = forest[0].size();
        vector<vector<bool>> seen(R, vector<bool>(C, false));
        queue<tuple<int,int,int>> q;
        q.emplace(sr, sc, 0);
        seen[sr][sc] = true;
        const int dr[4] = {-1, 1, 0, 0};
        const int dc[4] = {0, 0, -1, 1};
        while (!q.empty()) {
            auto [r, c, d] = q.front(); q.pop();
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
                if (seen[nr][nc] || forest[nr][nc] == 0) continue;
                if (nr == tr && nc == tc) return d + 1;
                seen[nr][nc] = true;
                q.emplace(nr, nc, d + 1);
            }
        }
        return -1;
    }

    int cutOffTree(vector<vector<int>>& forest) {
        vector<tuple<int,int,int>> trees;
        int R = forest.size(), C = forest[0].size();
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (forest[i][j] > 1) {
                    trees.emplace_back(forest[i][j], i, j);
                }
            }
        }
        sort(trees.begin(), trees.end(),
             [](const auto& a, const auto& b){ return get<0>(a) < get<0>(b); });
        int sr = 0, sc = 0, ans = 0;
        for (auto &[h, tr, tc] : trees) {
            int d = bfs(forest, sr, sc, tr, tc);
            if (d == -1) return -1;
            ans += d;
            sr = tr; sc = tc;
            forest[tr][tc] = 1; // cut the tree
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static final int[] DR = {-1, 1, 0, 0};
    private static final int[] DC = {0, 0, -1, 1};

    public int cutOffTree(List<List<Integer>> forest) {
        int rows = forest.size();
        int cols = forest.get(0).size();

        // Collect all trees with height > 1
        List<int[]> trees = new ArrayList<>();
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                int val = forest.get(r).get(c);
                if (val > 1) {
                    trees.add(new int[]{val, r, c});
                }
            }
        }

        // Sort by height
        trees.sort(Comparator.comparingInt(a -> a[0]));

        int sr = 0, sc = 0;
        int totalSteps = 0;

        for (int[] tree : trees) {
            int tr = tree[1];
            int tc = tree[2];
            int dist = bfs(forest, sr, sc, tr, tc);
            if (dist == -1) {
                return -1;
            }
            totalSteps += dist;
            sr = tr;
            sc = tc;
        }

        return totalSteps;
    }

    private int bfs(List<List<Integer>> forest, int sr, int sc, int tr, int tc) {
        int rows = forest.size();
        int cols = forest.get(0).size();

        if (sr == tr && sc == tc) {
            return 0;
        }

        boolean[][] visited = new boolean[rows][cols];
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{sr, sc, 0});
        visited[sr][sc] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0], c = cur[1], d = cur[2];

            for (int i = 0; i < 4; ++i) {
                int nr = r + DR[i];
                int nc = c + DC[i];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                if (visited[nr][nc]) continue;
                if (forest.get(nr).get(nc) == 0) continue; // obstacle

                if (nr == tr && nc == tc) {
                    return d + 1;
                }

                visited[nr][nc] = true;
                queue.offer(new int[]{nr, nc, d + 1});
            }
        }

        return -1; // unreachable
    }
}
```

## Python

```python
import collections

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest or not forest[0]:
            return -1

        # collect all trees with height > 1
        trees = []
        for r in range(len(forest)):
            for c in range(len(forest[0])):
                h = forest[r][c]
                if h > 1:
                    trees.append((h, r, c))
        # sort by height
        trees.sort()

        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0
            R, C = len(forest), len(forest[0])
            visited = [[False] * C for _ in range(R)]
            dq = collections.deque()
            dq.append((sr, sc, 0))
            visited[sr][sc] = True
            while dq:
                r, c, d = dq.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return d + 1
                        visited[nr][nc] = True
                        dq.append((nr, nc, d + 1))
            return -1

        total_steps = 0
        cur_r = cur_c = 0

        # If starting cell is blocked, impossible
        if forest[0][0] == 0:
            return -1

        for _, tr, tc in trees:
            dist = bfs(cur_r, cur_c, tr, tc)
            if dist == -1:
                return -1
            total_steps += dist
            # cut the tree (make it walkable)
            forest[tr][tc] = 1
            cur_r, cur_c = tr, tc

        return total_steps
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        R, C = len(forest), len(forest[0])
        trees = []
        for i in range(R):
            for j in range(C):
                h = forest[i][j]
                if h > 1:
                    trees.append((h, i, j))
        trees.sort()

        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            if sr == tr and sc == tc:
                return 0
            visited = [[False] * C for _ in range(R)]
            q = deque()
            q.append((sr, sc, 0))
            visited[sr][sc] = True
            while q:
                r, c, d = q.popleft()
                nd = d + 1
                # up
                if r > 0:
                    nr, nc = r - 1, c
                    if not visited[nr][nc] and forest[nr][nc]:
                        if nr == tr and nc == tc:
                            return nd
                        visited[nr][nc] = True
                        q.append((nr, nc, nd))
                # down
                if r + 1 < R:
                    nr, nc = r + 1, c
                    if not visited[nr][nc] and forest[nr][nc]:
                        if nr == tr and nc == tc:
                            return nd
                        visited[nr][nc] = True
                        q.append((nr, nc, nd))
                # left
                if c > 0:
                    nr, nc = r, c - 1
                    if not visited[nr][nc] and forest[nr][nc]:
                        if nr == tr and nc == tc:
                            return nd
                        visited[nr][nc] = True
                        q.append((nr, nc, nd))
                # right
                if c + 1 < C:
                    nr, nc = r, c + 1
                    if not visited[nr][nc] and forest[nr][nc]:
                        if nr == tr and nc == tc:
                            return nd
                        visited[nr][nc] = True
                        q.append((nr, nc, nd))
            return -1

        sr = sc = 0
        total_steps = 0
        for _, tr, tc in trees:
            dist = bfs(sr, sc, tr, tc)
            if dist == -1:
                return -1
            total_steps += dist
            sr, sc = tr, tc
            forest[tr][tc] = 1  # cut the tree

        return total_steps
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int h;
    int r;
    int c;
} Tree;

static int bfs(int** forest, int rows, int cols,
               int sr, int sc, int tr, int tc) {
    if (sr == tr && sc == tc) return 0;
    static const int dr[4] = {-1, 1, 0, 0};
    static const int dc[4] = {0, 0, -1, 1};

    int visited[50][50];
    memset(visited, 0, sizeof(visited));

    int qR[2500], qC[2500];
    int head = 0, tail = 0;
    qR[tail] = sr; qC[tail] = sc; tail++;
    visited[sr][sc] = 1;

    int steps = 0;
    while (head < tail) {
        int curSize = tail - head;
        for (int i = 0; i < curSize; ++i) {
            int r = qR[head];
            int c = qC[head];
            head++;
            if (r == tr && c == tc) return steps;
            for (int d = 0; d < 4; ++d) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                    !visited[nr][nc] && forest[nr][nc] != 0) {
                    visited[nr][nc] = 1;
                    qR[tail] = nr;
                    qC[tail] = nc;
                    tail++;
                }
            }
        }
        steps++;
    }
    return -1;
}

static int treeCmp(const void* a, const void* b) {
    const Tree* t1 = (const Tree*)a;
    const Tree* t2 = (const Tree*)b;
    return (t1->h > t2->h) - (t1->h < t2->h);
}

int cutOffTree(int** forest, int forestSize, int* forestColSize) {
    int rows = forestSize;
    if (rows == 0) return 0;
    int cols = forestColSize[0];

    Tree trees[2500];
    int treeCount = 0;

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (forest[i][j] > 1) {
                trees[treeCount].h = forest[i][j];
                trees[treeCount].r = i;
                trees[treeCount].c = j;
                treeCount++;
            }
        }
    }

    qsort(trees, treeCount, sizeof(Tree), treeCmp);

    int totalSteps = 0;
    int curR = 0, curC = 0;

    for (int i = 0; i < treeCount; ++i) {
        int d = bfs(forest, rows, cols, curR, curC, trees[i].r, trees[i].c);
        if (d == -1) return -1;
        totalSteps += d;
        forest[trees[i].r][trees[i].c] = 1; // cut the tree
        curR = trees[i].r;
        curC = trees[i].c;
    }

    return totalSteps;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int CutOffTree(IList<IList<int>> forest) {
        int rows = forest.Count;
        int cols = forest[0].Count;
        
        var trees = new List<(int h, int r, int c)>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                int val = forest[r][c];
                if (val > 1) {
                    trees.Add((val, r, c));
                }
            }
        }
        
        trees.Sort((a, b) => a.h.CompareTo(b.h));
        
        int sr = 0, sc = 0;
        int totalSteps = 0;
        foreach (var tree in trees) {
            int dist = BFS(forest, sr, sc, tree.r, tree.c);
            if (dist == -1) return -1;
            totalSteps += dist;
            sr = tree.r;
            sc = tree.c;
        }
        
        return totalSteps;
    }
    
    private int BFS(IList<IList<int>> forest, int sr, int sc, int tr, int tc) {
        if (sr == tr && sc == tc) return 0;
        int rows = forest.Count;
        int cols = forest[0].Count;
        var visited = new bool[rows, cols];
        var queue = new Queue<(int r, int c, int d)>();
        queue.Enqueue((sr, sc, 0));
        visited[sr, sc] = true;
        int[] dr = new int[] { -1, 1, 0, 0 };
        int[] dc = new int[] { 0, 0, -1, 1 };
        
        while (queue.Count > 0) {
            var cur = queue.Dequeue();
            for (int i = 0; i < 4; i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                    !visited[nr, nc] && forest[nr][nc] != 0) {
                    if (nr == tr && nc == tc) {
                        return cur.d + 1;
                    }
                    visited[nr, nc] = true;
                    queue.Enqueue((nr, nc, cur.d + 1));
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
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function(forest) {
    const R = forest.length;
    const C = forest[0].length;

    // collect all trees with height > 1
    const trees = [];
    for (let r = 0; r < R; ++r) {
        for (let c = 0; c < C; ++c) {
            if (forest[r][c] > 1) {
                trees.push([forest[r][c], r, c]);
            }
        }
    }

    // sort by height ascending
    trees.sort((a, b) => a[0] - b[0]);

    const bfs = (sr, sc, tr, tc) => {
        if (sr === tr && sc === tc) return 0;
        const visited = Array.from({ length: R }, () => Array(C).fill(false));
        const queue = [];
        let head = 0;
        queue.push([sr, sc, 0]);
        visited[sr][sc] = true;
        const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        while (head < queue.length) {
            const [r, c, d] = queue[head++];
            for (const [dr, dc] of dirs) {
                const nr = r + dr;
                const nc = c + dc;
                if (
                    nr >= 0 && nr < R &&
                    nc >= 0 && nc < C &&
                    !visited[nr][nc] &&
                    forest[nr][nc] !== 0
                ) {
                    if (nr === tr && nc === tc) return d + 1;
                    visited[nr][nc] = true;
                    queue.push([nr, nc, d + 1]);
                }
            }
        }
        return -1;
    };

    let totalSteps = 0;
    let curR = 0, curC = 0;

    for (const [, tr, tc] of trees) {
        const steps = bfs(curR, curC, tr, tc);
        if (steps === -1) return -1;
        totalSteps += steps;
        curR = tr;
        curC = tc;
        // cut the tree: turn into walkable ground
        forest[tr][tc] = 1;
    }

    return totalSteps;
};
```

## Typescript

```typescript
function cutOffTree(forest: number[][]): number {
    const R = forest.length;
    const C = forest[0].length;
    const trees: [number, number, number][] = [];
    for (let r = 0; r < R; ++r) {
        for (let c = 0; c < C; ++c) {
            const v = forest[r][c];
            if (v > 1) trees.push([v, r, c]);
        }
    }
    trees.sort((a, b) => a[0] - b[0]);

    let sr = 0, sc = 0;
    let total = 0;

    for (const [, tr, tc] of trees) {
        const d = bfs(forest, sr, sc, tr, tc);
        if (d === -1) return -1;
        total += d;
        sr = tr;
        sc = tc;
        forest[tr][tc] = 1; // cut the tree
    }
    return total;
}

function bfs(forest: number[][], sr: number, sc: number, tr: number, tc: number): number {
    const R = forest.length;
    const C = forest[0].length;
    if (forest[sr][sc] === 0) return -1;
    if (sr === tr && sc === tc) return 0;

    const visited: boolean[][] = Array.from({ length: R }, () => Array(C).fill(false));
    const queue: [number, number, number][] = [];
    let head = 0;
    queue.push([sr, sc, 0]);
    visited[sr][sc] = true;

    const dirs = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ];

    while (head < queue.length) {
        const [r, c, d] = queue[head++];
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (
                nr >= 0 && nr < R &&
                nc >= 0 && nc < C &&
                !visited[nr][nc] &&
                forest[nr][nc] > 0
            ) {
                if (nr === tr && nc === tc) return d + 1;
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
     * @param Integer[][] $forest
     * @return Integer
     */
    function cutOffTree($forest) {
        $R = count($forest);
        $C = count($forest[0]);
        $trees = [];

        for ($r = 0; $r < $R; $r++) {
            for ($c = 0; $c < $C; $c++) {
                if ($forest[$r][$c] > 1) {
                    $trees[] = [$forest[$r][$c], $r, $c];
                }
            }
        }

        usort($trees, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $sr = 0;
        $sc = 0;
        $totalSteps = 0;

        foreach ($trees as $tree) {
            [$height, $tr, $tc] = $tree;
            $dist = $this->bfs($forest, $sr, $sc, $tr, $tc);
            if ($dist == -1) {
                return -1;
            }
            $totalSteps += $dist;
            $sr = $tr;
            $sc = $tc;
        }

        return $totalSteps;
    }

    private function bfs($forest, $sr, $sc, $tr, $tc) {
        if ($sr == $tr && $sc == $tc) {
            return 0;
        }
        $R = count($forest);
        $C = count($forest[0]);
        $visited = array_fill(0, $R, array_fill(0, $C, false));
        $queue = new SplQueue();
        $queue->enqueue([$sr, $sc, 0]);
        $visited[$sr][$sc] = true;
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];

        while (!$queue->isEmpty()) {
            [$r, $c, $d] = $queue->dequeue();
            foreach ($dirs as $dir) {
                $nr = $r + $dir[0];
                $nc = $c + $dir[1];
                if ($nr < 0 || $nr >= $R || $nc < 0 || $nc >= $C) continue;
                if ($visited[$nr][$nc]) continue;
                if ($forest[$nr][$nc] == 0) continue;
                if ($nr == $tr && $nc == $tc) {
                    return $d + 1;
                }
                $visited[$nr][$nc] = true;
                $queue->enqueue([$nr, $nc, $d + 1]);
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func cutOffTree(_ forest: [[Int]]) -> Int {
        let rows = forest.count
        let cols = forest[0].count
        var trees: [(height: Int, r: Int, c: Int)] = []
        for r in 0..<rows {
            for c in 0..<cols {
                let v = forest[r][c]
                if v > 1 {
                    trees.append((v, r, c))
                }
            }
        }
        trees.sort { $0.height < $1.height }
        var sr = 0, sc = 0
        var total = 0
        for tree in trees {
            let d = bfs(forest, sr, sc, tree.r, tree.c)
            if d < 0 { return -1 }
            total += d
            sr = tree.r
            sc = tree.c
        }
        return total
    }

    private func bfs(_ forest: [[Int]], _ sr: Int, _ sc: Int, _ tr: Int, _ tc: Int) -> Int {
        if sr == tr && sc == tc { return 0 }
        let rows = forest.count
        let cols = forest[0].count
        var visited = Array(repeating: Array(repeating: false, count: cols), count: rows)
        var queue: [(r: Int, c: Int, d: Int)] = []
        var head = 0
        queue.append((sr, sc, 0))
        visited[sr][sc] = true
        let dr = [-1, 1, 0, 0]
        let dc = [0, 0, -1, 1]
        while head < queue.count {
            let cur = queue[head]
            head += 1
            for i in 0..<4 {
                let nr = cur.r + dr[i]
                let nc = cur.c + dc[i]
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] && forest[nr][nc] != 0 {
                    if nr == tr && nc == tc {
                        return cur.d + 1
                    }
                    visited[nr][nc] = true
                    queue.append((nr, nc, cur.d + 1))
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
    fun cutOffTree(forest: List<List<Int>>): Int {
        val trees = mutableListOf<Triple<Int, Int, Int>>() // height, row, col
        for (r in forest.indices) {
            for (c in forest[r].indices) {
                val v = forest[r][c]
                if (v > 1) {
                    trees.add(Triple(v, r, c))
                }
            }
        }
        trees.sortBy { it.first }

        var sr = 0
        var sc = 0
        var steps = 0

        for ((_, tr, tc) in trees) {
            val d = bfs(forest, sr, sc, tr, tc)
            if (d == -1) return -1
            steps += d
            sr = tr
            sc = tc
        }
        return steps
    }

    private fun bfs(forest: List<List<Int>>, sr: Int, sc: Int, tr: Int, tc: Int): Int {
        val rows = forest.size
        val cols = forest[0].size
        if (sr == tr && sc == tc) return 0

        val visited = Array(rows) { BooleanArray(cols) }
        val queue: ArrayDeque<IntArray> = ArrayDeque()
        queue.add(intArrayOf(sr, sc, 0))
        visited[sr][sc] = true

        val dr = intArrayOf(-1, 1, 0, 0)
        val dc = intArrayOf(0, 0, -1, 1)

        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            val r = cur[0]
            val c = cur[1]
            val d = cur[2]

            if (r == tr && c == tc) return d

            for (i in 0..3) {
                val nr = r + dr[i]
                val nc = c + dc[i]
                if (nr in 0 until rows && nc in 0 until cols &&
                    !visited[nr][nc] && forest[nr][nc] != 0
                ) {
                    visited[nr][nc] = true
                    queue.add(intArrayOf(nr, nc, d + 1))
                }
            }
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int cutOffTree(List<List<int>> forest) {
    int rows = forest.length;
    int cols = forest[0].length;

    // Collect all trees with height > 1
    List<List<int>> trees = [];
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (forest[r][c] > 1) {
          trees.add([forest[r][c], r, c]);
        }
      }
    }

    // Sort by height
    trees.sort((a, b) => a[0].compareTo(b[0]));

    int sr = 0, sc = 0;
    int totalSteps = 0;

    for (var tree in trees) {
      int tr = tree[1];
      int tc = tree[2];
      int steps = _bfs(forest, sr, sc, tr, tc);
      if (steps == -1) return -1;
      totalSteps += steps;
      // Cut the tree
      forest[tr][tc] = 1;
      sr = tr;
      sc = tc;
    }

    return totalSteps;
  }

  int _bfs(List<List<int>> grid, int sr, int sc, int tr, int tc) {
    if (sr == tr && sc == tc) return 0;

    int rows = grid.length;
    int cols = grid[0].length;
    List<List<bool>> visited =
        List.generate(rows, (_) => List.filled(cols, false));

    Queue<List<int>> q = Queue();
    q.add([sr, sc, 0]);
    visited[sr][sc] = true;

    const List<int> dr = [-1, 1, 0, 0];
    const List<int> dc = [0, 0, -1, 1];

    while (q.isNotEmpty) {
      var cur = q.removeFirst();
      int r = cur[0], c = cur[1], d = cur[2];

      for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (nr < 0 ||
            nr >= rows ||
            nc < 0 ||
            nc >= cols ||
            visited[nr][nc] ||
            grid[nr][nc] == 0) continue;

        if (nr == tr && nc == tc) return d + 1;
        visited[nr][nc] = true;
        q.add([nr, nc, d + 1]);
      }
    }

    return -1; // unreachable
  }
}
```

## Golang

```go
import (
	"sort"
)

type treeInfo struct {
	h, r, c int
}

func cutOffTree(forest [][]int) int {
	if len(forest) == 0 || len(forest[0]) == 0 {
		return -1
	}
	R, C := len(forest), len(forest[0])

	// collect trees with height > 1
	trees := make([]treeInfo, 0)
	for i := 0; i < R; i++ {
		for j := 0; j < C; j++ {
			if forest[i][j] > 1 {
				trees = append(trees, treeInfo{forest[i][j], i, j})
			}
		}
	}
	// sort by height
	sort.Slice(trees, func(i, j int) bool { return trees[i].h < trees[j].h })

	sr, sc := 0, 0
	total := 0

	for _, t := range trees {
		dist := bfs(forest, sr, sc, t.r, t.c)
		if dist == -1 {
			return -1
		}
		total += dist
		sr, sc = t.r, t.c
	}
	return total
}

func bfs(forest [][]int, sr, sc, tr, tc int) int {
	if sr == tr && sc == tc {
		return 0
	}
	R, C := len(forest), len(forest[0])
	visited := make([][]bool, R)
	for i := range visited {
		visited[i] = make([]bool, C)
	}
	type node struct{ r, c, d int }
	queue := []node{{sr, sc, 0}}
	visited[sr][sc] = true
	dr := []int{-1, 1, 0, 0}
	dc := []int{0, 0, -1, 1}

	for head := 0; head < len(queue); head++ {
		cur := queue[head]
		for k := 0; k < 4; k++ {
			nr, nc := cur.r+dr[k], cur.c+dc[k]
			if nr >= 0 && nr < R && nc >= 0 && nc < C && !visited[nr][nc] && forest[nr][nc] != 0 {
				if nr == tr && nc == tc {
					return cur.d + 1
				}
				visited[nr][nc] = true
				queue = append(queue, node{nr, nc, cur.d + 1})
			}
		}
	}
	return -1
}
```

## Ruby

```ruby
def cut_off_tree(forest)
  rows = forest.size
  cols = forest[0].size

  trees = []
  forest.each_with_index do |row, r|
    row.each_with_index do |val, c|
      trees << [val, r, c] if val > 1
    end
  end
  trees.sort_by! { |t| t[0] }

  bfs = lambda do |sr, sc, tr, tc|
    return 0 if sr == tr && sc == tc
    visited = Array.new(rows) { Array.new(cols, false) }
    queue = []
    head = 0
    queue << [sr, sc, 0]
    visited[sr][sc] = true
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while head < queue.length
      r, c, d = queue[head]
      head += 1
      return d if r == tr && c == tc
      dirs.each do |dr, dc|
        nr = r + dr
        nc = c + dc
        next unless nr.between?(0, rows - 1) && nc.between?(0, cols - 1)
        next if visited[nr][nc] || forest[nr][nc] == 0
        visited[nr][nc] = true
        queue << [nr, nc, d + 1]
      end
    end
    -1
  end

  sr = sc = 0
  total_steps = 0
  trees.each do |_, tr, tc|
    dist = bfs.call(sr, sc, tr, tc)
    return -1 if dist == -1
    total_steps += dist
    sr, sc = tr, tc
  end
  total_steps
end
```

## Scala

```scala
object Solution {
  def cutOffTree(forest: List[List[Int]]): Int = {
    val rows = forest.length
    val cols = forest.head.length
    // Convert to mutable array for fast indexing and updates
    val grid = Array.ofDim[Int](rows, cols)
    for (i <- 0 until rows; j <- 0 until cols) {
      grid(i)(j) = forest(i)(j)
    }

    // Collect all trees with height > 1
    val trees = scala.collection.mutable.ArrayBuffer[(Int, Int, Int)]()
    for (i <- 0 until rows; j <- 0 until cols) {
      val v = grid(i)(j)
      if (v > 1) trees.append((v, i, j))
    }
    // Sort by height ascending
    val sortedTrees = trees.sortBy(_._1)

    var totalSteps = 0
    var curR = 0
    var curC = 0

    for ((_, tr, tc) <- sortedTrees) {
      val dist = bfs(grid, curR, curC, tr, tc)
      if (dist < 0) return -1
      totalSteps += dist
      // Cut the tree: turn it into walkable ground
      grid(tr)(tc) = 1
      curR = tr
      curC = tc
    }
    totalSteps
  }

  private def bfs(grid: Array[Array[Int]],
                  sr: Int, sc: Int,
                  tr: Int, tc: Int): Int = {
    val rows = grid.length
    val cols = grid(0).length
    val visited = Array.ofDim[Boolean](rows, cols)
    val queue = scala.collection.mutable.Queue[(Int, Int, Int)]()
    queue.enqueue((sr, sc, 0))
    visited(sr)(sc) = true

    val directions = Array((-1, 0), (1, 0), (0, -1), (0, 1))

    while (queue.nonEmpty) {
      val (r, c, d) = queue.dequeue()
      if (r == tr && c == tc) return d
      for ((dr, dc) <- directions) {
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
            !visited(nr)(nc) && grid(nr)(nc) != 0) {
          visited(nr)(nc) = true
          queue.enqueue((nr, nc, d + 1))
        }
      }
    }
    -1
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

pub struct Solution {}

impl Solution {
    pub fn cut_off_tree(forest: Vec<Vec<i32>>) -> i32 {
        let mut trees: Vec<(i32, usize, usize)> = Vec::new();
        for (r, row) in forest.iter().enumerate() {
            for (c, &v) in row.iter().enumerate() {
                if v > 1 {
                    trees.push((v, r, c));
                }
            }
        }
        trees.sort_by_key(|k| k.0);
        let mut total: i32 = 0;
        let (mut sr, mut sc) = (0usize, 0usize);
        for &(_, tr, tc) in &trees {
            let d = Self::bfs(&forest, sr, sc, tr, tc);
            if d < 0 {
                return -1;
            }
            total += d;
            sr = tr;
            sc = tc;
        }
        total
    }

    fn bfs(forest: &Vec<Vec<i32>>, sr: usize, sc: usize, tr: usize, tc: usize) -> i32 {
        if sr == tr && sc == tc {
            return 0;
        }
        let rows = forest.len();
        let cols = forest[0].len();
        let mut visited = vec![vec![false; cols]; rows];
        let mut q: VecDeque<(usize, usize, i32)> = VecDeque::new();
        visited[sr][sc] = true;
        q.push_back((sr, sc, 0));
        while let Some((r, c, d)) = q.pop_front() {
            const DIRS: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
            for &(dr, dc) in &DIRS {
                let nr_i = r as i32 + dr;
                let nc_i = c as i32 + dc;
                if nr_i >= 0 && nr_i < rows as i32 && nc_i >= 0 && nc_i < cols as i32 {
                    let nr = nr_i as usize;
                    let nc = nc_i as usize;
                    if !visited[nr][nc] && forest[nr][nc] != 0 {
                        if nr == tr && nc == tc {
                            return d + 1;
                        }
                        visited[nr][nc] = true;
                        q.push_back((nr, nc, d + 1));
                    }
                }
            }
        }
        -1
    }
}
```

## Racket

```racket
(require racket/deque)

(define drs '#(-1 1 0 0))
(define dcs '#(0 0 -1 1))

;; Breadth‑first search returning distance or -1
(define (bfs forest sr sc tr tc)
  (let* ((R (vector-length forest))
         (C (if (= R 0) 0 (vector-length (vector-ref forest 0))))
         (visited (make-vector (* R C) #f))
         (dq (deque)))
    (define (idx r c) (+ (* r C) c))
    (deque-push-back! dq (list sr sc 0))
    (vector-set! visited (idx sr sc) #t)
    (let loop ()
      (if (deque-empty? dq)
          -1
          (let* ((node (deque-pop-front! dq))
                 (r (first node))
                 (c (second node))
                 (d (third node)))
            (if (and (= r tr) (= c tc))
                d
                (begin
                  (for ([i (in-range 4)])
                    (let* ((nr (+ r (vector-ref drs i)))
                           (nc (+ c (vector-ref dcs i))))
                      (when (and (>= nr 0) (< nr R)
                                 (>= nc 0) (< nc C))
                        (let ((cell (vector-ref (vector-ref forest nr) nc)))
                          (when (and (> cell 0) (not (vector-ref visited (idx nr nc))))
                            (vector-set! visited (idx nr nc) #t)
                            (deque-push-back! dq (list nr nc (+ d 1)))))))))
                  (loop))))))))

(define/contract (cut-off-tree forest)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (length forest))
         (cols (if (= rows 0) 0 (length (first forest))))
         ;; convert to vector of vectors for O(1) indexing
         (vforest (list->vector (map list->vector forest)))
         ;; collect all trees with height > 1
         (trees (for/list ([r (in-range rows)]
                          [c (in-range cols)]
                          #:when (> (vector-ref (vector-ref vforest r) c) 1))
                  (list (vector-ref (vector-ref vforest r) c) r c)))
         ;; sort by height ascending
         (sorted-trees (sort trees < #:key (lambda (t) (first t)))))
    (let loop ((sr 0) (sc 0) (ans 0) (remaining sorted-trees))
      (if (null? remaining)
          ans
          (let* ((tree (car remaining))
                 (tr (second tree))
                 (tc (third tree))
                 (dist (bfs vforest sr sc tr tc)))
            (if (= dist -1)
                -1
                (loop tr tc (+ ans dist) (cdr remaining))))))))
```

## Erlang

```erlang
-spec cut_off_tree(Forest :: [[integer()]]) -> integer().
cut_off_tree(Forest) ->
    Trees = collect_trees(Forest),
    SortedTrees = lists:keysort(1, Trees),
    process_trees(SortedTrees, Forest, 0, 0, 0).

%% Collect all trees with height > 1 as {Height, Row, Col}
collect_trees(Forest) ->
    R = length(Forest),
    collect_rows(Forest, 0, R, []).

collect_rows(_Forest, RowIdx, MaxRow, Acc) when RowIdx >= MaxRow -> Acc;
collect_rows(Forest, RowIdx, MaxRow, Acc) ->
    Row = lists:nth(RowIdx + 1, Forest),
    C = length(Row),
    NewAcc = collect_cols(Row, RowIdx, 0, C, Acc),
    collect_rows(Forest, RowIdx + 1, MaxRow, NewAcc).

collect_cols(_Row, _RowIdx, ColIdx, MaxCol, Acc) when ColIdx >= MaxCol -> Acc;
collect_cols(Row, RowIdx, ColIdx, MaxCol, Acc) ->
    Val = lists:nth(ColIdx + 1, Row),
    NewAcc = if
        Val > 1 -> [{Val, RowIdx, ColIdx} | Acc];
        true -> Acc
    end,
    collect_cols(Row, RowIdx, ColIdx + 1, MaxCol, NewAcc).

%% Process each tree in order, accumulating steps
process_trees([], _Forest, _CurR, _CurC, Ans) ->
    Ans;
process_trees([{_H, Tr, Tc} | Rest], Forest, CurR, CurC, Ans) ->
    case bfs(Forest, CurR, CurC, Tr, Tc) of
        -1 -> -1;
        Dist ->
            NewAns = Ans + Dist,
            process_trees(Rest, Forest, Tr, Tc, NewAns)
    end.

%% Breadth‑first search returning distance or -1
bfs(Forest, Sr, Sc, Tr, Tc) when Sr == Tr, Sc == Tc -> 0;
bfs(Forest, Sr, Sc, Tr, Tc) ->
    Q0 = queue:new(),
    Q1 = queue:in({Sr, Sc, 0}, Q0),
    Visited0 = maps:put({Sr, Sc}, true, #{}),
    bfs_loop(Forest, Q1, Visited0, {Tr, Tc}).

bfs_loop(_Forest, Queue, _Visited, {Tr, Tc}) ->
    case queue:out(Queue) of
        {{value, {R, C, D}}, _QRest} when R == Tr, C == Tc -> D;
        {empty, _} -> -1
    end;
bfs_loop(Forest, Queue, Visited, Target = {Tr, Tc}) ->
    case queue:out(Queue) of
        {{value, {R, C, D}}, QRest} ->
            Neigh = [{R-1, C}, {R+1, C}, {R, C-1}, {R, C+1}],
            {NewQ, NewVis} = lists:foldl(
                fun({Nr, Nc}, {QAcc, VAcc}) ->
                    case valid(Forest, Nr, Nc) of
                        true ->
                            Key = {Nr, Nc},
                            case maps:is_key(Key, VAcc) of
                                false ->
                                    QNext = queue:in({Nr, Nc, D+1}, QAcc),
                                    VNext = maps:put(Key, true, VAcc),
                                    {QNext, VNext};
                                true -> {QAcc, VAcc}
                            end;
                        false -> {QAcc, VAcc}
                    end
                end,
                {QRest, Visited},
                Neigh),
            bfs_loop(Forest, NewQ, NewVis, Target);
        {empty, _} -> -1
    end.

valid(Forest, R, C) ->
    R >= 0,
    C >= 0,
    RowCount = length(Forest),
    ColCount = case Forest of [] -> 0; [First|_] -> length(First) end,
    R < RowCount,
    C < ColCount,
    cell(Forest, R, C) =/= 0.

cell(Forest, R, C) ->
    Row = lists:nth(R + 1, Forest),
    lists:nth(C + 1, Row).
```

## Elixir

```elixir
defmodule Solution do
  @spec cut_off_tree(forest :: [[integer]]) :: integer
  def cut_off_tree(forest) do
    trees =
      for {row, r} <- Enum.with_index(forest),
          {val, c} <- Enum.with_index(row),
          val > 1,
          do: {val, r, c}

    sorted = Enum.sort_by(trees, fn {h, _, _} -> h end)

    result =
      Enum.reduce_while(sorted, {0, 0, 0}, fn {_h, tr, tc}, {cr, cc, steps} ->
        d = bfs(forest, cr, cc, tr, tc)

        if d == -1 do
          {:halt, -1}
        else
          {:cont, {tr, tc, steps + d}}
        end
      end)

    case result do
      -1 -> -1
      {_r, _c, total} -> total
    end
  end

  defp bfs(forest, sr, sc, tr, tc) do
    rows = length(forest)
    cols = length(List.first(forest))

    queue = :queue.new() |> :queue.in({sr, sc, 0})
    visited = Map.put(%{}, {sr, sc}, true)

    bfs_loop(queue, visited, forest, rows, cols, tr, tc)
  end

  defp bfs_loop(queue, visited, forest, rows, cols, tr, tc) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {r, c, d}}, q} ->
        if r == tr and c == tc do
          d
        else
          dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

          {new_q, new_visited} =
            Enum.reduce(dirs, {q, visited}, fn {dr, dc}, {q_acc, vis_acc} ->
              nr = r + dr
              nc = c + dc

              if nr >= 0 and nr < rows and nc >= 0 and nc < cols do
                if not Map.has_key?(vis_acc, {nr, nc}) and get_cell(forest, nr, nc) != 0 do
                  q2 = :queue.in({nr, nc, d + 1}, q_acc)
                  vis2 = Map.put(vis_acc, {nr, nc}, true)
                  {q2, vis2}
                else
                  {q_acc, vis_acc}
                end
              else
                {q_acc, vis_acc}
              end
            end)

          bfs_loop(new_q, new_visited, forest, rows, cols, tr, tc)
        end
    end
  end

  defp get_cell(forest, r, c) do
    forest |> Enum.at(r) |> Enum.at(c)
  end
end
```

# 1591. Strange Printer II

## Cpp

```cpp
class Solution {
public:
    bool isPrintable(vector<vector<int>>& targetGrid) {
        int m = targetGrid.size();
        int n = targetGrid[0].size();
        const int MAXC = 60;
        vector<int> minR(MAXC + 1, m), maxR(MAXC + 1, -1);
        vector<int> minC(MAXC + 1, n), maxC(MAXC + 1, -1);
        vector<bool> present(MAXC + 1, false);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int c = targetGrid[i][j];
                present[c] = true;
                minR[c] = min(minR[c], i);
                maxR[c] = max(maxR[c], i);
                minC[c] = min(minC[c], j);
                maxC[c] = max(maxC[c], j);
            }
        }
        vector<vector<bool>> edge(MAXC + 1, vector<bool>(MAXC + 1, false));
        vector<int> indeg(MAXC + 1, 0);
        for (int c = 1; c <= MAXC; ++c) {
            if (!present[c]) continue;
            for (int i = minR[c]; i <= maxR[c]; ++i) {
                for (int j = minC[c]; j <= maxC[c]; ++j) {
                    int other = targetGrid[i][j];
                    if (other != c && !edge[c][other]) {
                        edge[c][other] = true;
                        indeg[other]++;
                    }
                }
            }
        }
        queue<int> q;
        int total = 0;
        for (int c = 1; c <= MAXC; ++c) {
            if (!present[c]) continue;
            total++;
            if (indeg[c] == 0) q.push(c);
        }
        int visited = 0;
        while (!q.empty()) {
            int cur = q.front(); q.pop();
            visited++;
            for (int nxt = 1; nxt <= MAXC; ++nxt) {
                if (edge[cur][nxt]) {
                    indeg[nxt]--;
                    if (indeg[nxt] == 0) q.push(nxt);
                }
            }
        }
        return visited == total;
    }
};
```

## Java

```java
class Solution {
    public boolean isPrintable(int[][] targetGrid) {
        int m = targetGrid.length;
        int n = targetGrid[0].length;
        int maxColor = 60; // per constraints
        int[] minRow = new int[maxColor + 1];
        int[] maxRow = new int[maxColor + 1];
        int[] minCol = new int[maxColor + 1];
        int[] maxCol = new int[maxColor + 1];
        boolean[] present = new boolean[maxColor + 1];
        for (int c = 1; c <= maxColor; ++c) {
            minRow[c] = Integer.MAX_VALUE;
            minCol[c] = Integer.MAX_VALUE;
            maxRow[c] = -1;
            maxCol[c] = -1;
        }
        // Determine bounds and presence
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int c = targetGrid[i][j];
                present[c] = true;
                if (i < minRow[c]) minRow[c] = i;
                if (i > maxRow[c]) maxRow[c] = i;
                if (j < minCol[c]) minCol[c] = j;
                if (j > maxCol[c]) maxCol[c] = j;
            }
        }
        // Build graph
        boolean[][] edgeAdded = new boolean[maxColor + 1][maxColor + 1];
        int[] indegree = new int[maxColor + 1];
        for (int c = 1; c <= maxColor; ++c) {
            if (!present[c]) continue;
            for (int i = minRow[c]; i <= maxRow[c]; ++i) {
                for (int j = minCol[c]; j <= maxCol[c]; ++j) {
                    int other = targetGrid[i][j];
                    if (other != c && !edgeAdded[c][other]) {
                        edgeAdded[c][other] = true;
                        indegree[other]++;
                    }
                }
            }
        }
        // Topological sort
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();
        int totalColors = 0;
        for (int c = 1; c <= maxColor; ++c) {
            if (present[c]) {
                totalColors++;
                if (indegree[c] == 0) queue.add(c);
            }
        }
        int visited = 0;
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            visited++;
            for (int nxt = 1; nxt <= maxColor; ++nxt) {
                if (edgeAdded[cur][nxt]) {
                    indegree[nxt]--;
                    if (indegree[nxt] == 0) queue.add(nxt);
                }
            }
        }
        return visited == totalColors;
    }
}
```

## Python

```python
class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        m = len(targetGrid)
        n = len(targetGrid[0])
        max_color = 60

        min_r = [m] * (max_color + 1)
        max_r = [-1] * (max_color + 1)
        min_c = [n] * (max_color + 1)
        max_c = [-1] * (max_color + 1)

        present = set()
        for i in range(m):
            row = targetGrid[i]
            for j in range(n):
                col = row[j]
                present.add(col)
                if i < min_r[col]:
                    min_r[col] = i
                if i > max_r[col]:
                    max_r[col] = i
                if j < min_c[col]:
                    min_c[col] = j
                if j > max_c[col]:
                    max_c[col] = j

        adj = [set() for _ in range(max_color + 1)]
        indeg = [0] * (max_color + 1)

        for color in present:
            r1, r2 = min_r[color], max_r[color]
            c1, c2 = min_c[color], max_c[color]
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    other = targetGrid[i][j]
                    if other != color and other not in adj[color]:
                        adj[color].add(other)
                        indeg[other] += 1

        from collections import deque
        q = deque([c for c in present if indeg[c] == 0])
        processed = 0
        while q:
            cur = q.popleft()
            processed += 1
            for nb in adj[cur]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)

        return processed == len(present)
```

## Python3

```python
from typing import List
from collections import defaultdict, deque

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set()
        # bounding boxes for each color
        min_r = {}
        max_r = {}
        min_c = {}
        max_c = {}
        for i in range(m):
            for j in range(n):
                col = targetGrid[i][j]
                colors.add(col)
                if col not in min_r:
                    min_r[col] = max_r[col] = i
                    min_c[col] = max_c[col] = j
                else:
                    min_r[col] = min(min_r[col], i)
                    max_r[col] = max(max_r[col], i)
                    min_c[col] = min(min_c[col], j)
                    max_c[col] = max(max_c[col], j)

        graph = defaultdict(set)
        indeg = {c: 0 for c in colors}

        # build dependencies
        for col in colors:
            r1, r2 = min_r[col], max_r[col]
            c1, c2 = min_c[col], max_c[col]
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    other = targetGrid[i][j]
                    if other != col and other not in graph[col]:
                        graph[col].add(other)
                        indeg[other] += 1

        # topological sort
        q = deque([c for c in colors if indeg[c] == 0])
        visited = 0
        while q:
            cur = q.popleft()
            visited += 1
            for nb in graph[cur]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)

        return visited == len(colors)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool isPrintable(int** targetGrid, int targetGridSize, int* targetGridColSize) {
    const int MAXC = 60;
    int minRow[MAXC + 1], maxRow[MAXC + 1];
    int minCol[MAXC + 1], maxCol[MAXC + 1];
    bool present[MAXC + 1] = {false};
    for (int c = 1; c <= MAXC; ++c) {
        minRow[c] = targetGridSize;
        maxRow[c] = -1;
        minCol[c] = *targetGridColSize;
        maxCol[c] = -1;
    }

    int m = targetGridSize;
    int n = targetGridColSize[0];
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int col = targetGrid[i][j];
            present[col] = true;
            if (i < minRow[col]) minRow[col] = i;
            if (i > maxRow[col]) maxRow[col] = i;
            if (j < minCol[col]) minCol[col] = j;
            if (j > maxCol[col]) maxCol[col] = j;
        }
    }

    bool adj[MAXC + 1][MAXC + 1] = {{false}};
    int indeg[MAXC + 1] = {0};

    for (int c = 1; c <= MAXC; ++c) {
        if (!present[c]) continue;
        for (int i = minRow[c]; i <= maxRow[c]; ++i) {
            for (int j = minCol[c]; j <= maxCol[c]; ++j) {
                int d = targetGrid[i][j];
                if (d != c && !adj[c][d]) {
                    adj[c][d] = true;
                    indeg[d]++;
                }
            }
        }
    }

    // Kahn's algorithm
    int queue[MAXC + 1];
    int qh = 0, qt = 0;
    int totalColors = 0;
    for (int c = 1; c <= MAXC; ++c) {
        if (!present[c]) continue;
        totalColors++;
        if (indeg[c] == 0) {
            queue[qt++] = c;
        }
    }

    int visited = 0;
    while (qh < qt) {
        int cur = queue[qh++];
        visited++;
        for (int nxt = 1; nxt <= MAXC; ++nxt) {
            if (adj[cur][nxt]) {
                indeg[nxt]--;
                if (indeg[nxt] == 0) {
                    queue[qt++] = nxt;
                }
            }
        }
    }

    return visited == totalColors;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsPrintable(int[][] targetGrid)
    {
        int m = targetGrid.Length;
        int n = targetGrid[0].Length;
        const int MAXC = 61; // colors are in [1,60]

        int[] minRow = new int[MAXC];
        int[] maxRow = new int[MAXC];
        int[] minCol = new int[MAXC];
        int[] maxCol = new int[MAXC];
        bool[] present = new bool[MAXC];

        for (int c = 0; c < MAXC; c++)
        {
            minRow[c] = m;
            maxRow[c] = -1;
            minCol[c] = n;
            maxCol[c] = -1;
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int c = targetGrid[i][j];
                present[c] = true;
                if (i < minRow[c]) minRow[c] = i;
                if (i > maxRow[c]) maxRow[c] = i;
                if (j < minCol[c]) minCol[c] = j;
                if (j > maxCol[c]) maxCol[c] = j;
            }
        }

        var adj = new List<HashSet<int>>();
        for (int i = 0; i < MAXC; i++) adj.Add(new HashSet<int>());
        int[] indegree = new int[MAXC];

        for (int c = 1; c < MAXC; c++)
        {
            if (!present[c]) continue;
            for (int i = minRow[c]; i <= maxRow[c]; i++)
            {
                for (int j = minCol[c]; j <= maxCol[c]; j++)
                {
                    int d = targetGrid[i][j];
                    if (d != c && adj[c].Add(d))
                    {
                        indegree[d]++;
                    }
                }
            }
        }

        var queue = new Queue<int>();
        int totalColors = 0;
        for (int c = 1; c < MAXC; c++)
        {
            if (!present[c]) continue;
            totalColors++;
            if (indegree[c] == 0) queue.Enqueue(c);
        }

        int processed = 0;
        while (queue.Count > 0)
        {
            int cur = queue.Dequeue();
            processed++;
            foreach (int nb in adj[cur])
            {
                indegree[nb]--;
                if (indegree[nb] == 0) queue.Enqueue(nb);
            }
        }

        return processed == totalColors;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} targetGrid
 * @return {boolean}
 */
var isPrintable = function(targetGrid) {
    const m = targetGrid.length;
    const n = targetGrid[0].length;
    const MAXC = 60;
    const INF = Number.MAX_SAFE_INTEGER;

    const minRow = new Array(MAXC + 1).fill(INF);
    const maxRow = new Array(MAXC + 1).fill(-1);
    const minCol = new Array(MAXC + 1).fill(INF);
    const maxCol = new Array(MAXC + 1).fill(-1);
    const present = new Array(MAXC + 1).fill(false);

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const c = targetGrid[i][j];
            present[c] = true;
            if (i < minRow[c]) minRow[c] = i;
            if (i > maxRow[c]) maxRow[c] = i;
            if (j < minCol[c]) minCol[c] = j;
            if (j > maxCol[c]) maxCol[c] = j;
        }
    }

    const adj = Array.from({length: MAXC + 1}, () => new Set());

    for (let c = 1; c <= MAXC; ++c) {
        if (!present[c]) continue;
        for (let i = minRow[c]; i <= maxRow[c]; ++i) {
            for (let j = minCol[c]; j <= maxCol[c]; ++j) {
                const other = targetGrid[i][j];
                if (other !== c) {
                    adj[c].add(other);
                }
            }
        }
    }

    const indeg = new Array(MAXC + 1).fill(0);
    let totalColors = 0;
    for (let c = 1; c <= MAXC; ++c) {
        if (!present[c]) continue;
        totalColors++;
        for (const v of adj[c]) {
            indeg[v]++;
        }
    }

    const queue = [];
    for (let c = 1; c <= MAXC; ++c) {
        if (present[c] && indeg[c] === 0) queue.push(c);
    }

    let processed = 0;
    while (queue.length) {
        const u = queue.shift();
        processed++;
        for (const v of adj[u]) {
            indeg[v]--;
            if (indeg[v] === 0) queue.push(v);
        }
    }

    return processed === totalColors;
};
```

## Typescript

```typescript
function isPrintable(targetGrid: number[][]): boolean {
    const m = targetGrid.length;
    const n = targetGrid[0].length;
    const MAX_COLOR = 61; // colors are in [1,60]
    const present = new Array(MAX_COLOR).fill(false);
    const minRow = new Array(MAX_COLOR).fill(Infinity);
    const maxRow = new Array(MAX_COLOR).fill(-1);
    const minCol = new Array(MAX_COLOR).fill(Infinity);
    const maxCol = new Array(MAX_COLOR).fill(-1);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const c = targetGrid[i][j];
            present[c] = true;
            if (i < minRow[c]) minRow[c] = i;
            if (i > maxRow[c]) maxRow[c] = i;
            if (j < minCol[c]) minCol[c] = j;
            if (j > maxCol[c]) maxCol[c] = j;
        }
    }

    const adj: Set<number>[] = Array.from({ length: MAX_COLOR }, () => new Set<number>());
    const indegree = new Array(MAX_COLOR).fill(0);

    for (let c = 1; c < MAX_COLOR; c++) {
        if (!present[c]) continue;
        for (let i = minRow[c]; i <= maxRow[c]; i++) {
            for (let j = minCol[c]; j <= maxCol[c]; j++) {
                const other = targetGrid[i][j];
                if (other !== c && !adj[c].has(other)) {
                    adj[c].add(other);
                    indegree[other]++;
                }
            }
        }
    }

    const queue: number[] = [];
    let processed = 0;
    for (let c = 1; c < MAX_COLOR; c++) {
        if (present[c] && indegree[c] === 0) queue.push(c);
    }

    while (queue.length) {
        const cur = queue.shift()!;
        processed++;
        for (const nb of adj[cur]) {
            indegree[nb]--;
            if (indegree[nb] === 0) queue.push(nb);
        }
    }

    let total = 0;
    for (let c = 1; c < MAX_COLOR; c++) if (present[c]) total++;

    return processed === total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $targetGrid
     * @return Boolean
     */
    function isPrintable($targetGrid) {
        $m = count($targetGrid);
        if ($m == 0) return true;
        $n = count($targetGrid[0]);
        $maxColor = 60; // given constraint

        $INF = $m + $n + 5;

        $minRow = array_fill(0, $maxColor + 1, $INF);
        $maxRow = array_fill(0, $maxColor + 1, -1);
        $minCol = array_fill(0, $maxColor + 1, $INF);
        $maxCol = array_fill(0, $maxColor + 1, -1);
        $present = array_fill(0, $maxColor + 1, false);

        // Determine bounds for each color
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $c = $targetGrid[$i][$j];
                $present[$c] = true;
                if ($i < $minRow[$c]) $minRow[$c] = $i;
                if ($i > $maxRow[$c]) $maxRow[$c] = $i;
                if ($j < $minCol[$c]) $minCol[$c] = $j;
                if ($j > $maxCol[$c]) $maxCol[$c] = $j;
            }
        }

        // Build graph
        $adj = array_fill(0, $maxColor + 1, array_fill(0, $maxColor + 1, false));
        $indeg = array_fill(0, $maxColor + 1, 0);

        for ($c = 1; $c <= $maxColor; $c++) {
            if (!$present[$c]) continue;
            for ($i = $minRow[$c]; $i <= $maxRow[$c]; $i++) {
                for ($j = $minCol[$c]; $j <= $maxCol[$c]; $j++) {
                    $other = $targetGrid[$i][$j];
                    if ($other != $c && !$adj[$c][$other]) {
                        $adj[$c][$other] = true;
                        $indeg[$other]++;
                    }
                }
            }
        }

        // Topological sort
        $queue = new SplQueue();
        $totalColors = 0;
        for ($c = 1; $c <= $maxColor; $c++) {
            if ($present[$c]) {
                $totalColors++;
                if ($indeg[$c] == 0) {
                    $queue->enqueue($c);
                }
            }
        }

        $visited = 0;
        while (!$queue->isEmpty()) {
            $cur = $queue->dequeue();
            $visited++;
            for ($next = 1; $next <= $maxColor; $next++) {
                if ($adj[$cur][$next]) {
                    $indeg[$next]--;
                    if ($indeg[$next] == 0) {
                        $queue->enqueue($next);
                    }
                }
            }
        }

        return $visited === $totalColors;
    }
}
```

## Swift

```swift
class Solution {
    func isPrintable(_ targetGrid: [[Int]]) -> Bool {
        let m = targetGrid.count
        let n = targetGrid[0].count
        let maxColor = 60
        
        var minRow = Array(repeating: Int.max, count: maxColor + 1)
        var maxRow = Array(repeating: -1, count: maxColor + 1)
        var minCol = Array(repeating: Int.max, count: maxColor + 1)
        var maxCol = Array(repeating: -1, count: maxColor + 1)
        var present = Array(repeating: false, count: maxColor + 1)
        
        for i in 0..<m {
            for j in 0..<n {
                let c = targetGrid[i][j]
                present[c] = true
                if i < minRow[c] { minRow[c] = i }
                if i > maxRow[c] { maxRow[c] = i }
                if j < minCol[c] { minCol[c] = j }
                if j > maxCol[c] { maxCol[c] = j }
            }
        }
        
        var adj = Array(repeating: Set<Int>(), count: maxColor + 1)
        var indegree = Array(repeating: 0, count: maxColor + 1)
        
        for c in 1...maxColor where present[c] {
            let r1 = minRow[c], r2 = maxRow[c]
            let col1 = minCol[c], col2 = maxCol[c]
            if r1 == Int.max { continue }
            for i in r1...r2 {
                for j in col1...col2 {
                    let other = targetGrid[i][j]
                    if other != c && !adj[c].contains(other) {
                        adj[c].insert(other)
                        indegree[other] += 1
                    }
                }
            }
        }
        
        var queue = [Int]()
        for c in 1...maxColor where present[c] && indegree[c] == 0 {
            queue.append(c)
        }
        var idx = 0
        var processed = 0
        
        while idx < queue.count {
            let cur = queue[idx]
            idx += 1
            processed += 1
            for nb in adj[cur] {
                indegree[nb] -= 1
                if indegree[nb] == 0 {
                    queue.append(nb)
                }
            }
        }
        
        var totalPresent = 0
        for c in 1...maxColor where present[c] { totalPresent += 1 }
        
        return processed == totalPresent
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPrintable(targetGrid: Array<IntArray>): Boolean {
        val m = targetGrid.size
        val n = targetGrid[0].size
        val MAX_COLOR = 61  // colors are in [1,60]
        val minRow = IntArray(MAX_COLOR) { Int.MAX_VALUE }
        val maxRow = IntArray(MAX_COLOR) { -1 }
        val minCol = IntArray(MAX_COLOR) { Int.MAX_VALUE }
        val maxCol = IntArray(MAX_COLOR) { -1 }
        val present = BooleanArray(MAX_COLOR)

        for (i in 0 until m) {
            for (j in 0 until n) {
                val c = targetGrid[i][j]
                present[c] = true
                if (i < minRow[c]) minRow[c] = i
                if (i > maxRow[c]) maxRow[c] = i
                if (j < minCol[c]) minCol[c] = j
                if (j > maxCol[c]) maxCol[c] = j
            }
        }

        val edge = Array(MAX_COLOR) { BooleanArray(MAX_COLOR) }
        val indeg = IntArray(MAX_COLOR)

        for (c in 1 until MAX_COLOR) {
            if (!present[c]) continue
            for (i in minRow[c]..maxRow[c]) {
                for (j in minCol[c]..maxCol[c]) {
                    val d = targetGrid[i][j]
                    if (d != c && !edge[c][d]) {
                        edge[c][d] = true
                        indeg[d]++
                    }
                }
            }
        }

        val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        var totalColors = 0
        for (c in 1 until MAX_COLOR) {
            if (present[c]) {
                totalColors++
                if (indeg[c] == 0) queue.add(c)
            }
        }

        var visited = 0
        while (!queue.isEmpty()) {
            val cur = queue.poll()
            visited++
            for (next in 1 until MAX_COLOR) {
                if (edge[cur][next]) {
                    indeg[next]--
                    if (indeg[next] == 0) queue.add(next)
                }
            }
        }

        return visited == totalColors
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  bool isPrintable(List<List<int>> targetGrid) {
    int m = targetGrid.length;
    int n = targetGrid[0].length;

    const int maxColor = 60;
    List<int> minRow = List.filled(maxColor + 1, m);
    List<int> maxRow = List.filled(maxColor + 1, -1);
    List<int> minCol = List.filled(maxColor + 1, n);
    List<int> maxCol = List.filled(maxColor + 1, -1);
    List<bool> present = List.filled(maxColor + 1, false);

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        int c = targetGrid[i][j];
        present[c] = true;
        if (i < minRow[c]) minRow[c] = i;
        if (i > maxRow[c]) maxRow[c] = i;
        if (j < minCol[c]) minCol[c] = j;
        if (j > maxCol[c]) maxCol[c] = j;
      }
    }

    List<Set<int>> adj = List.generate(maxColor + 1, (_) => <int>{});
    List<int> indegree = List.filled(maxColor + 1, 0);
    int totalColors = 0;

    for (int c = 1; c <= maxColor; ++c) {
      if (!present[c]) continue;
      totalColors++;
      for (int i = minRow[c]; i <= maxRow[c]; ++i) {
        for (int j = minCol[c]; j <= maxCol[c]; ++j) {
          int other = targetGrid[i][j];
          if (other != c && !adj[c].contains(other)) {
            adj[c].add(other);
            indegree[other]++;
          }
        }
      }
    }

    Queue<int> q = ListQueue<int>();
    for (int c = 1; c <= maxColor; ++c) {
      if (present[c] && indegree[c] == 0) {
        q.addLast(c);
      }
    }

    int processed = 0;
    while (q.isNotEmpty) {
      int cur = q.removeFirst();
      processed++;
      for (int nb in adj[cur]) {
        indegree[nb]--;
        if (indegree[nb] == 0) {
          q.addLast(nb);
        }
      }
    }

    return processed == totalColors;
  }
}
```

## Golang

```go
func isPrintable(targetGrid [][]int) bool {
	m := len(targetGrid)
	n := len(targetGrid[0])
	const maxC = 61

	minR := make([]int, maxC)
	maxR := make([]int, maxC)
	minC := make([]int, maxC)
	maxCcol := make([]int, maxC)
	present := make([]bool, maxC)

	for c := 1; c < maxC; c++ {
		minR[c] = m
		minC[c] = n
		maxR[c] = -1
		maxCcol[c] = -1
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			c := targetGrid[i][j]
			present[c] = true
			if i < minR[c] {
				minR[c] = i
			}
			if i > maxR[c] {
				maxR[c] = i
			}
			if j < minC[c] {
				minC[c] = j
			}
			if j > maxCcol[c] {
				maxCcol[c] = j
			}
		}
	}

	indeg := make([]int, maxC)
	adj := make([][]int, maxC)
	edge := make([][]bool, maxC)
	for i := 0; i < maxC; i++ {
		edge[i] = make([]bool, maxC)
	}

	for c := 1; c < maxC; c++ {
		if !present[c] {
			continue
		}
		for i := minR[c]; i <= maxR[c]; i++ {
			for j := minC[c]; j <= maxCcol[c]; j++ {
				d := targetGrid[i][j]
				if d != c && !edge[c][d] {
					edge[c][d] = true
					adj[c] = append(adj[c], d)
					indeg[d]++
				}
			}
		}
	}

	queue := make([]int, 0)
	total := 0
	for c := 1; c < maxC; c++ {
		if present[c] {
			total++
			if indeg[c] == 0 {
				queue = append(queue, c)
			}
		}
	}

	processed := 0
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		processed++
		for _, nb := range adj[cur] {
			indeg[nb]--
			if indeg[nb] == 0 {
				queue = append(queue, nb)
			}
		}
	}

	return processed == total
}
```

## Ruby

```ruby
require 'set'

# @param {Integer[][]} target_grid
# @return {Boolean}
def is_printable(target_grid)
  m = target_grid.size
  n = target_grid[0].size

  # bounding rectangles for each color: [min_row, max_row, min_col, max_col]
  rects = {}
  target_grid.each_with_index do |row, i|
    row.each_with_index do |c, j|
      if rects.key?(c)
        r = rects[c]
        r[0] = i if i < r[0]
        r[1] = i if i > r[1]
        r[2] = j if j < r[2]
        r[3] = j if j > r[3]
      else
        rects[c] = [i, i, j, j]
      end
    end
  end

  # build dependency graph: color -> set of colors that must be printed after it
  adj = Hash.new { |h, k| h[k] = Set.new }
  indeg = Hash.new(0)

  rects.each_key { |c| indeg[c] = 0 }

  rects.each do |color, (r1, r2, c1, c2)|
    (r1..r2).each do |i|
      (c1..c2).each do |j|
        other = target_grid[i][j]
        next if other == color
        unless adj[color].include?(other)
          adj[color] << other
          indeg[other] += 1
        end
      end
    end
  end

  # topological sort (Kahn's algorithm)
  queue = []
  indeg.each { |c, d| queue << c if d == 0 }

  processed = 0
  until queue.empty?
    cur = queue.shift
    processed += 1
    adj[cur].each do |nbr|
      indeg[nbr] -= 1
      queue << nbr if indeg[nbr] == 0
    end
  end

  processed == rects.size
end
```

## Scala

```scala
object Solution {
    def isPrintable(targetGrid: Array[Array[Int]]): Boolean = {
        val m = targetGrid.length
        val n = targetGrid(0).length
        val maxColor = 60
        val INF = Int.MaxValue

        val minR = Array.fill(maxColor + 1)(INF)
        val maxR = Array.fill(maxColor + 1)(-1)
        val minC = Array.fill(maxColor + 1)(INF)
        val maxC = Array.fill(maxColor + 1)(-1)

        val present = scala.collection.mutable.HashSet[Int]()

        var i = 0
        while (i < m) {
            var j = 0
            while (j < n) {
                val c = targetGrid(i)(j)
                present += c
                if (i < minR(c)) minR(c) = i
                if (i > maxR(c)) maxR(c) = i
                if (j < minC(c)) minC(c) = j
                if (j > maxC(c)) maxC(c) = j
                j += 1
            }
            i += 1
        }

        val adj = Array.fill(maxColor + 1)(scala.collection.mutable.HashSet[Int]())
        val indegree = Array.fill(maxColor + 1)(0)

        for (c <- present) {
            var r = minR(c)
            while (r <= maxR(c)) {
                var col = minC(c)
                while (col <= maxC(c)) {
                    val other = targetGrid(r)(col)
                    if (other != c && !adj(c).contains(other)) {
                        adj(c) += other
                        indegree(other) += 1
                    }
                    col += 1
                }
                r += 1
            }
        }

        val queue = new java.util.ArrayDeque[Int]()
        for (c <- present if indegree(c) == 0) {
            queue.add(c)
        }

        var visited = 0
        while (!queue.isEmpty) {
            val cur = queue.poll()
            visited += 1
            for (nbr <- adj(cur)) {
                indegree(nbr) -= 1
                if (indegree(nbr) == 0) queue.add(nbr)
            }
        }

        visited == present.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_printable(target_grid: Vec<Vec<i32>>) -> bool {
        const MAX_COLOR: usize = 61; // colors are in [1,60]
        let m = target_grid.len();
        if m == 0 {
            return true;
        }
        let n = target_grid[0].len();

        // bounding rectangles for each color
        let mut min_row = vec![i32::MAX; MAX_COLOR];
        let mut max_row = vec![-1; MAX_COLOR];
        let mut min_col = vec![i32::MAX; MAX_COLOR];
        let mut max_col = vec![-1; MAX_COLOR];

        for i in 0..m {
            for j in 0..n {
                let c = target_grid[i][j] as usize;
                if i as i32 < min_row[c] { min_row[c] = i as i32; }
                if i as i32 > max_row[c] { max_row[c] = i as i32; }
                if j as i32 < min_col[c] { min_col[c] = j as i32; }
                if j as i32 > max_col[c] { max_col[c] = j as i32; }
            }
        }

        // adjacency matrix and indegrees
        let mut adj = vec![vec![false; MAX_COLOR]; MAX_COLOR];
        let mut indeg = vec![0i32; MAX_COLOR];
        let mut present_cnt = 0usize;

        for c in 1..MAX_COLOR {
            if min_row[c] == i32::MAX { continue; } // color not present
            present_cnt += 1;
            let r_start = min_row[c] as usize;
            let r_end = max_row[c] as usize;
            let col_start = min_col[c] as usize;
            let col_end = max_col[c] as usize;

            for i in r_start..=r_end {
                for j in col_start..=col_end {
                    let other = target_grid[i][j] as usize;
                    if other != c && !adj[c][other] {
                        adj[c][other] = true;
                        indeg[other] += 1;
                    }
                }
            }
        }

        // Kahn's algorithm for cycle detection
        use std::collections::VecDeque;
        let mut q = VecDeque::new();
        for c in 1..MAX_COLOR {
            if min_row[c] != i32::MAX && indeg[c] == 0 {
                q.push_back(c);
            }
        }

        let mut processed = 0usize;
        while let Some(u) = q.pop_front() {
            processed += 1;
            for v in 1..MAX_COLOR {
                if adj[u][v] {
                    indeg[v] -= 1;
                    if indeg[v] == 0 {
                        q.push_back(v);
                    }
                }
            }
        }

        processed == present_cnt
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/sequence)

(define/contract (is-printable targetGrid)
  (-> (listof (listof exact-integer?)) boolean?)

  ;; Convert grid to vector of vectors for O(1) access
  (define rows (list->vector (map list->vector targetGrid)))
  (define m (vector-length rows))
  (define n (if (= m 0) 0 (vector-length (vector-ref rows 0))))

  ;; Compute bounding rectangle for each color
  (define bounds (make-hash)) ; color -> vector [minR maxR minC maxC]
  (for ([i (in-range m)])
    (let ((row (vector-ref rows i)))
      (for ([j (in-range n)])
        (define col (vector-ref row j))
        (if (hash-has-key? bounds col)
            (let* ((b (hash-ref bounds col))
                   (minR (vector-ref b 0))
                   (maxR (vector-ref b 1))
                   (minC (vector-ref b 2))
                   (maxC (vector-ref b 3)))
              (vector-set! b 0 (if (< i minR) i minR))
              (vector-set! b 1 (if (> i maxR) i maxR))
              (vector-set! b 2 (if (< j minC) j minC))
              (vector-set! b 3 (if (> j maxC) j maxC)))
            (hash-set! bounds col (vector i i j j)))))))

  ;; Initialize adjacency sets and indegree map
  (define adj (make-hash))      ; color -> hash set of neighbors
  (define indegree (make-hash)) ; color -> integer

  (for ([c (hash-keys bounds)])
    (hash-set! adj c (make-hash))
    (hash-set! indegree c 0))

  ;; Build graph edges based on rectangles
  (for ([c (hash-keys bounds)])
    (let* ((b (hash-ref bounds c))
           (minR (vector-ref b 0))
           (maxR (vector-ref b 1))
           (minC (vector-ref b 2))
           (maxC (vector-ref b 3)))
      (for ([i (in-range minR (add1 maxR))]
            [j (in-range minC (add1 maxC))])
        (define d (vector-ref (vector-ref rows i) j))
        (when (not (= d c))
          (define neigh-set (hash-ref adj c))
          (unless (hash-has-key? neigh-set d)
            (hash-set! neigh-set d #t)
            (hash-set! indegree d (+ 1 (hash-ref indegree d)))))))))

  ;; Kahn's algorithm for cycle detection
  (define total-colors (hash-count indegree))
  (define q (make-vector total-colors))
  (define front 0)
  (define back 0)

  (for ([c (hash-keys indegree)])
    (when (= (hash-ref indegree c) 0)
      (vector-set! q back c)
      (set! back (+ back 1))))

  (let loop ((processed 0))
    (if (>= front back)
        (= processed total-colors)
        (begin
          (define cur (vector-ref q front))
          (set! front (+ front 1))
          (set! processed (+ processed 1))
          (for ([nbr (hash-keys (hash-ref adj cur))])
            (define newdeg (- (hash-ref indegree nbr) 1))
            (hash-set! indegree nbr newdeg)
            (when (= newdeg 0)
              (vector-set! q back nbr)
              (set! back (+ back 1))))
          (loop processed)))) )
```

## Erlang

```erlang
-module(solution).
-export([is_printable/1]).
-spec is_printable(TargetGrid :: [[integer()]]) -> boolean().
is_printable(TargetGrid) ->
    Bounds = build_bounds(TargetGrid),
    AdjMap = build_adjacency(Bounds, TargetGrid),
    Colors = maps:keys(Bounds),
    Indeg0 = maps:from_list([{Color, 0} || Color <- Colors]),
    IndegMap = compute_indeg(AdjMap, Indeg0),
    Queue0 = [C || C <- Colors, maps:get(C, IndegMap) == 0],
    Processed = kahn(Queue0, AdjMap, IndegMap, 0),
    length(Colors) == Processed.

build_bounds(Grid) ->
    build_bounds(Grid, 0, #{}).

build_bounds([], _RowIdx, Bounds) -> Bounds;
build_bounds([Row|RestRows], RowIdx, Bounds) ->
    NewBounds = build_row(Row, RowIdx, 0, Bounds),
    build_bounds(RestRows, RowIdx+1, NewBounds).

build_row([], _RowIdx, _ColIdx, Bounds) -> Bounds;
build_row([Color|RestCols], RowIdx, ColIdx, Bounds) ->
    case maps:is_key(Color, Bounds) of
        true ->
            {MinR, MaxR, MinC, MaxC} = maps:get(Color, Bounds),
            NewMinR = min(MinR, RowIdx),
            NewMaxR = max(MaxR, RowIdx),
            NewMinC = min(MinC, ColIdx),
            NewMaxC = max(MaxC, ColIdx),
            Updated = {NewMinR, NewMaxR, NewMinC, NewMaxC},
            B2 = maps:put(Color, Updated, Bounds);
        false ->
            B2 = maps:put(Color, {RowIdx, RowIdx, ColIdx, ColIdx}, Bounds)
    end,
    build_row(RestCols, RowIdx, ColIdx+1, B2).

build_adjacency(Bounds, Grid) ->
    maps:fold(fun(Color, {MinR, MaxR, MinC, MaxC}, AdjAcc) ->
        lists:foldl(fun(R, Acc1) ->
            RowList = lists:nth(R+1, Grid),
            lists:foldl(fun(Cc, Acc2) ->
                D = lists:nth(Cc+1, RowList),
                if D =/= Color -> add_edge(Acc2, Color, D);
                   true -> Acc2
                end
            end, Acc1, lists:seq(MinC, MaxC))
        end, AdjAcc, lists:seq(MinR, MaxR))
    end, #{} , Bounds).

add_edge(AdjMap, From, To) ->
    Set = maps:get(From, AdjMap, #{}),
    case maps:is_key(To, Set) of
        true -> AdjMap;
        false ->
            NewSet = Set#{To => true},
            maps:put(From, NewSet, AdjMap)
    end.

compute_indeg(AdjMap, Indeg0) ->
    maps:fold(fun(_From, Set, AccIndeg) ->
        maps:fold(fun(To, _, Acc2) ->
            Cur = maps:get(To, Acc2),
            maps:put(To, Cur+1, Acc2)
        end, AccIndeg, Set)
    end, Indeg0, AdjMap).

kahn([], _AdjMap, _IndegMap, Processed) -> Processed;
kahn([C|RestQueue], AdjMap, IndegMap, Processed) ->
    NeighSet = maps:get(C, AdjMap, #{}),
    {NewIndegMap, NewQueue} = maps:fold(fun(To, _, {IM, Q}) ->
        Deg = maps:get(To, IM) - 1,
        IM2 = maps:put(To, Deg, IM),
        if Deg == 0 -> {IM2, Q ++ [To]};
           true -> {IM2, Q}
        end
    end, {IndegMap, RestQueue}, NeighSet),
    kahn(NewQueue, AdjMap, NewIndegMap, Processed+1).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_printable(target_grid :: [[integer]]) :: boolean
  def is_printable(target_grid) do
    rows = length(target_grid)
    cols = if rows == 0, do: 0, else: length(List.first(target_grid))

    # Compute bounding rectangles for each color
    bounds =
      Enum.reduce(Enum.with_index(target_grid), %{}, fn {row, r}, acc ->
        Enum.reduce(Enum.with_index(row), acc, fn {val, c}, acc2 ->
          case Map.get(acc2, val) do
            nil -> Map.put(acc2, val, {r, r, c, c})
            {min_r, max_r, min_c, max_c} ->
              new_rect = {
                if(r < min_r, do: r, else: min_r),
                if(r > max_r, do: r, else: max_r),
                if(c < min_c, do: c, else: min_c),
                if(c > max_c, do: c, else: max_c)
              }
              Map.put(acc2, val, new_rect)
          end
        end)
      end)

    # Build dependency graph: color -> set of colors that must be printed after it
    adjacency =
      Enum.reduce(bounds, %{}, fn {color, {min_r, max_r, min_c, max_c}}, acc ->
        deps =
          Enum.reduce(min_r..max_r, MapSet.new(), fn r, set_acc ->
            row = Enum.at(target_grid, r)

            Enum.reduce(min_c..max_c, set_acc, fn c, set2 ->
              other = Enum.at(row, c)
              if other != color do
                MapSet.put(set2, other)
              else
                set2
              end
            end)
          end)

        Map.put(acc, color, deps)
      end)

    colors = Map.keys(bounds)

    # Compute indegrees
    indegrees =
      Enum.reduce(colors, %{}, fn c, acc -> Map.put(acc, c, 0) end)

    indegrees =
      Enum.reduce(adjacency, indegrees, fn {_c, neigh_set}, indeg_acc ->
        Enum.reduce(neigh_set, indeg_acc, fn n, ia ->
          Map.update!(ia, n, &(&1 + 1))
        end)
      end)

    # Topological sort (Kahn's algorithm)
    initial_queue =
      colors
      |> Enum.filter(fn c -> Map.get(indegrees, c) == 0 end)
      |> :queue.from_list()

    {processed, _final_indeg} = bfs(initial_queue, indegrees, adjacency, 0)

    processed == length(colors)
  end

  defp bfs(queue, indegrees, adjacency, count) do
    case :queue.out(queue) do
      {:empty, _} ->
        {count, indegrees}

      {{:value, node}, q_rest} ->
        neighbors = Map.get(adjacency, node, MapSet.new())

        {new_queue, new_indegrees} =
          Enum.reduce(neighbors, {q_rest, indegrees}, fn nb, {q_acc, indeg_acc} ->
            cur_deg = Map.get(indeg_acc, nb)
            updated_deg = cur_deg - 1
            indeg_upd = Map.put(indeg_acc, nb, updated_deg)

            q_upd =
              if updated_deg == 0 do
                :queue.in(nb, q_acc)
              else
                q_acc
              end

            {q_upd, indeg_upd}
          end)

        bfs(new_queue, new_indegrees, adjacency, count + 1)
    end
  end
end
```

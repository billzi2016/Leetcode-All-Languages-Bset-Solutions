# 1129. Shortest Path with Alternating Colors

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges, vector<vector<int>>& blueEdges) {
        const int INF = 1e9;
        vector<vector<int>> redAdj(n), blueAdj(n);
        for (auto &e : redEdges) redAdj[e[0]].push_back(e[1]);
        for (auto &e : blueEdges) blueAdj[e[0]].push_back(e[1]);

        vector<array<int,2>> dist(n, {INF, INF}); // 0: came via red, 1: came via blue
        queue<pair<int,int>> q; // node, last edge color (0 red, 1 blue)

        dist[0][0] = dist[0][1] = 0;
        q.push({0,0});
        q.push({0,1});

        while (!q.empty()) {
            auto [u, col] = q.front(); q.pop();
            int nextCol = 1 - col;
            const vector<int>& neigh = (nextCol == 0) ? redAdj[u] : blueAdj[u];
            for (int v : neigh) {
                if (dist[v][nextCol] == INF) {
                    dist[v][nextCol] = dist[u][col] + 1;
                    q.push({v, nextCol});
                }
            }
        }

        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            int best = min(dist[i][0], dist[i][1]);
            ans[i] = (best == INF) ? -1 : best;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        List<Integer>[] redAdj = new ArrayList[n];
        List<Integer>[] blueAdj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            redAdj[i] = new ArrayList<>();
            blueAdj[i] = new ArrayList<>();
        }
        for (int[] e : redEdges) {
            redAdj[e[0]].add(e[1]);
        }
        for (int[] e : blueEdges) {
            blueAdj[e[0]].add(e[1]);
        }

        final int INF = Integer.MAX_VALUE / 2;
        int[][] dist = new int[n][2]; // 0: red last, 1: blue last
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], INF);
        }
        dist[0][0] = 0;
        dist[0][1] = 0;

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0}); // start assuming last edge red
        q.offer(new int[]{0, 1}); // start assuming last edge blue

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int node = cur[0];
            int color = cur[1]; // 0 red, 1 blue (last edge color)

            if (color == 0) { // need to take a blue edge next
                for (int nb : blueAdj[node]) {
                    if (dist[nb][1] > dist[node][0] + 1) {
                        dist[nb][1] = dist[node][0] + 1;
                        q.offer(new int[]{nb, 1});
                    }
                }
            } else { // need to take a red edge next
                for (int nb : redAdj[node]) {
                    if (dist[nb][0] > dist[node][1] + 1) {
                        dist[nb][0] = dist[node][1] + 1;
                        q.offer(new int[]{nb, 0});
                    }
                }
            }
        }

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            int best = Math.min(dist[i][0], dist[i][1]);
            answer[i] = (best == INF) ? -1 : best;
        }
        return answer;
    }
}
```

## Python

```python
import collections

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        adj = [ [[] for _ in range(n)],  # 0 -> red edges
                [[] for _ in range(n)] ] # 1 -> blue edges
        for u, v in redEdges:
            adj[0][u].append(v)
        for u, v in blueEdges:
            adj[1][u].append(v)

        INF = float('inf')
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = dist[0][1] = 0
        q = collections.deque()
        q.append((0, 0))  # last edge was red
        q.append((0, 1))  # last edge was blue

        while q:
            node, color = q.popleft()
            next_color = 1 - color
            for nb in adj[next_color][node]:
                if dist[nb][next_color] == INF:
                    dist[nb][next_color] = dist[node][color] + 1
                    q.append((nb, next_color))

        ans = []
        for d_red, d_blue in dist:
            best = min(d_red, d_blue)
            ans.append(-1 if best == INF else best)
        return ans
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Build adjacency lists for each color
        red_adj = [[] for _ in range(n)]
        blue_adj = [[] for _ in range(n)]
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)

        INF = 10**9
        # dist[node][color] where color 0=red last edge, 1=blue last edge
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = dist[0][1] = 0

        q = deque()
        q.append((0, 0))  # start assuming last edge was red (so next must be blue)
        q.append((0, 1))  # start assuming last edge was blue (next must be red)

        while q:
            node, color = q.popleft()
            cur_dist = dist[node][color]
            # Determine next edges: opposite color
            if color == 0:  # last was red, take blue edges
                for nei in blue_adj[node]:
                    if dist[nei][1] == INF:
                        dist[nei][1] = cur_dist + 1
                        q.append((nei, 1))
            else:          # last was blue, take red edges
                for nei in red_adj[node]:
                    if dist[nei][0] == INF:
                        dist[nei][0] = cur_dist + 1
                        q.append((nei, 0))

        answer = []
        for i in range(n):
            best = min(dist[i][0], dist[i][1])
            answer.append(best if best != INF else -1)
        return answer
```

## C

```c
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestAlternatingPaths(int n, int** redEdges, int redEdgesSize, int* redEdgesColSize,
                              int** blueEdges, int blueEdgesSize, int* blueEdgesColSize,
                              int* returnSize) {
    // adjacency for red and blue edges
    int *redCnt = calloc(n, sizeof(int));
    int *blueCnt = calloc(n, sizeof(int));
    for (int i = 0; i < redEdgesSize; ++i) {
        int u = redEdges[i][0];
        redCnt[u]++;
    }
    for (int i = 0; i < blueEdgesSize; ++i) {
        int u = blueEdges[i][0];
        blueCnt[u]++;
    }

    int **redAdj = malloc(n * sizeof(int*));
    int **blueAdj = malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        redAdj[i] = malloc(redCnt[i] * sizeof(int));
        blueAdj[i] = malloc(blueCnt[i] * sizeof(int));
        redCnt[i] = 0;
        blueCnt[i] = 0;
    }
    for (int i = 0; i < redEdgesSize; ++i) {
        int u = redEdges[i][0], v = redEdges[i][1];
        redAdj[u][redCnt[u]++] = v;
    }
    for (int i = 0; i < blueEdgesSize; ++i) {
        int u = blueEdges[i][0], v = blueEdges[i][1];
        blueAdj[u][blueCnt[u]++] = v;
    }

    // distances: dist[node][color] where color 0=red,1=blue (last edge color)
    int **dist = malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        dist[i] = malloc(2 * sizeof(int));
        dist[i][0] = -1;
        dist[i][1] = -1;
    }

    // BFS queue
    int maxQueue = n * 2 + 5;
    int *qNode = malloc(maxQueue * sizeof(int));
    int *qColor = malloc(maxQueue * sizeof(int));
    int head = 0, tail = 0;

    // start from node 0 with both colors (distance 0)
    dist[0][0] = dist[0][1] = 0;
    qNode[tail] = 0; qColor[tail] = 0; tail++;
    qNode[tail] = 0; qColor[tail] = 1; tail++;

    while (head < tail) {
        int u = qNode[head];
        int c = qColor[head];
        head++;
        int nextColor = 1 - c;
        int *neighbors;
        int cnt;
        if (nextColor == 0) { // need red edge
            neighbors = redAdj[u];
            cnt = redCnt[u];
        } else {
            neighbors = blueAdj[u];
            cnt = blueCnt[u];
        }
        for (int i = 0; i < cnt; ++i) {
            int v = neighbors[i];
            if (dist[v][nextColor] == -1) {
                dist[v][nextColor] = dist[u][c] + 1;
                qNode[tail] = v;
                qColor[tail] = nextColor;
                tail++;
            }
        }
    }

    int *answer = malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (dist[i][0] == -1 && dist[i][1] == -1) answer[i] = -1;
        else if (dist[i][0] == -1) answer[i] = dist[i][1];
        else if (dist[i][1] == -1) answer[i] = dist[i][0];
        else answer[i] = dist[i][0] < dist[i][1] ? dist[i][0] : dist[i][1];
    }

    // clean up
    for (int i = 0; i < n; ++i) {
        free(redAdj[i]);
        free(blueAdj[i]);
        free(dist[i]);
    }
    free(redAdj);
    free(blueAdj);
    free(redCnt);
    free(blueCnt);
    free(dist);
    free(qNode);
    free(qColor);

    *returnSize = n;
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ShortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        var redAdj = new List<int>[n];
        var blueAdj = new List<int>[n];
        for (int i = 0; i < n; i++) {
            redAdj[i] = new List<int>();
            blueAdj[i] = new List<int>();
        }
        foreach (var e in redEdges) {
            redAdj[e[0]].Add(e[1]);
        }
        foreach (var e in blueEdges) {
            blueAdj[e[0]].Add(e[1]);
        }

        int[] distRed = new int[n];
        int[] distBlue = new int[n];
        for (int i = 0; i < n; i++) {
            distRed[i] = -1;
            distBlue[i] = -1;
        }
        distRed[0] = 0;
        distBlue[0] = 0;

        var q = new Queue<(int node, int color)>();
        // color: 0 = red last edge, 1 = blue last edge
        q.Enqueue((0, 0));
        q.Enqueue((0, 1));

        while (q.Count > 0) {
            var (u, color) = q.Dequeue();
            if (color == 0) { // came via red, need blue next
                foreach (int v in blueAdj[u]) {
                    if (distBlue[v] == -1) {
                        distBlue[v] = distRed[u] + 1;
                        q.Enqueue((v, 1));
                    }
                }
            } else { // came via blue, need red next
                foreach (int v in redAdj[u]) {
                    if (distRed[v] == -1) {
                        distRed[v] = distBlue[u] + 1;
                        q.Enqueue((v, 0));
                    }
                }
            }
        }

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                ans[i] = 0;
                continue;
            }
            int dr = distRed[i];
            int db = distBlue[i];
            if (dr == -1 && db == -1) ans[i] = -1;
            else if (dr == -1) ans[i] = db;
            else if (db == -1) ans[i] = dr;
            else ans[i] = Math.Min(dr, db);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} redEdges
 * @param {number[][]} blueEdges
 * @return {number[]}
 */
var shortestAlternatingPaths = function(n, redEdges, blueEdges) {
    const RED = 0, BLUE = 1;
    const redAdj = Array.from({length: n}, () => []);
    const blueAdj = Array.from({length: n}, () => []);
    
    for (const [u, v] of redEdges) redAdj[u].push(v);
    for (const [u, v] of blueEdges) blueAdj[u].push(v);
    
    const dist = Array.from({length: n}, () => [Infinity, Infinity]);
    const queue = [];
    // start from node 0 with both possible last colors
    dist[0][RED] = 0;
    dist[0][BLUE] = 0;
    queue.push([0, RED]);
    queue.push([0, BLUE]);
    
    let qIdx = 0;
    while (qIdx < queue.length) {
        const [node, lastColor] = queue[qIdx++];
        const curDist = dist[node][lastColor];
        // next edges must be opposite color
        if (lastColor === RED) {
            for (const nei of blueAdj[node]) {
                if (dist[nei][BLUE] > curDist + 1) {
                    dist[nei][BLUE] = curDist + 1;
                    queue.push([nei, BLUE]);
                }
            }
        } else { // lastColor === BLUE
            for (const nei of redAdj[node]) {
                if (dist[nei][RED] > curDist + 1) {
                    dist[nei][RED] = curDist + 1;
                    queue.push([nei, RED]);
                }
            }
        }
    }
    
    const answer = new Array(n);
    for (let i = 0; i < n; ++i) {
        const best = Math.min(dist[i][RED], dist[i][BLUE]);
        answer[i] = best === Infinity ? -1 : best;
    }
    return answer;
};
```

## Typescript

```typescript
function shortestAlternatingPaths(n: number, redEdges: number[][], blueEdges: number[][]): number[] {
    const redAdj: number[][] = Array.from({ length: n }, () => []);
    const blueAdj: number[][] = Array.from({ length: n }, () => []);

    for (const [u, v] of redEdges) redAdj[u].push(v);
    for (const [u, v] of blueEdges) blueAdj[u].push(v);

    const INF = Number.MAX_SAFE_INTEGER;
    const dist: number[][] = Array.from({ length: n }, () => [INF, INF]);
    // 0 -> last edge was red, 1 -> last edge was blue
    dist[0][0] = 0;
    dist[0][1] = 0;

    const queue: [number, number][] = [[0, 0], [0, 1]]; // node, lastColor

    while (queue.length) {
        const [node, color] = queue.shift()!;
        const curDist = dist[node][color];
        const nextAdj = color === 0 ? blueAdj : redAdj; // need opposite color
        for (const nxt of nextAdj[node]) {
            if (dist[nxt][1 - color] === INF) {
                dist[nxt][1 - color] = curDist + 1;
                queue.push([nxt, 1 - color]);
            }
        }
    }

    const answer: number[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        const best = Math.min(dist[i][0], dist[i][1]);
        answer[i] = best === INF ? -1 : best;
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $redEdges
     * @param Integer[][] $blueEdges
     * @return Integer[]
     */
    function shortestAlternatingPaths($n, $redEdges, $blueEdges) {
        // 0 = red, 1 = blue
        $graph = array_fill(0, 2, []);
        for ($c = 0; $c < 2; $c++) {
            $graph[$c] = array_fill(0, $n, []);
        }
        foreach ($redEdges as $e) {
            $graph[0][$e[0]][] = $e[1];
        }
        foreach ($blueEdges as $e) {
            $graph[1][$e[0]][] = $e[1];
        }

        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n, [$INF, $INF]);

        $queue = new SplQueue();
        // start from node 0 with both possible last colors
        $dist[0][0] = 0;
        $dist[0][1] = 0;
        $queue->enqueue([0, 0]); // last edge red
        $queue->enqueue([0, 1]); // last edge blue

        while (!$queue->isEmpty()) {
            [$node, $color] = $queue->dequeue();
            $nextColor = 1 - $color; // need opposite color next
            foreach ($graph[$nextColor][$node] as $nei) {
                if ($dist[$nei][$nextColor] === $INF) {
                    $dist[$nei][$nextColor] = $dist[$node][$color] + 1;
                    $queue->enqueue([$nei, $nextColor]);
                }
            }
        }

        $answer = [];
        for ($i = 0; $i < $n; $i++) {
            $minDist = min($dist[$i][0], $dist[$i][1]);
            $answer[] = ($minDist === $INF) ? -1 : $minDist;
        }
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func shortestAlternatingPaths(_ n: Int, _ redEdges: [[Int]], _ blueEdges: [[Int]]) -> [Int] {
        var redAdj = [[Int]](repeating: [], count: n)
        var blueAdj = [[Int]](repeating: [], count: n)
        for e in redEdges where e.count == 2 {
            redAdj[e[0]].append(e[1])
        }
        for e in blueEdges where e.count == 2 {
            blueAdj[e[0]].append(e[1])
        }

        let INF = Int.max / 2
        var dist = [[Int]](repeating: [INF, INF], count: n)
        dist[0][0] = 0
        dist[0][1] = 0

        var queue = [(Int, Int)]()
        queue.append((0, 0)) // last edge was red, next must be blue
        queue.append((0, 1)) // last edge was blue, next must be red
        var idx = 0

        while idx < queue.count {
            let (node, color) = queue[idx]
            idx += 1
            let nextColor = 1 - color
            let neighbors = nextColor == 0 ? redAdj[node] : blueAdj[node]
            for nb in neighbors {
                if dist[nb][nextColor] == INF {
                    dist[nb][nextColor] = dist[node][color] + 1
                    queue.append((nb, nextColor))
                }
            }
        }

        var answer = [Int](repeating: -1, count: n)
        for i in 0..<n {
            let best = min(dist[i][0], dist[i][1])
            if best != INF {
                answer[i] = best
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestAlternatingPaths(n: Int, redEdges: Array<IntArray>, blueEdges: Array<IntArray>): IntArray {
        val redAdj = Array(n) { mutableListOf<Int>() }
        val blueAdj = Array(n) { mutableListOf<Int>() }
        for (e in redEdges) {
            redAdj[e[0]].add(e[1])
        }
        for (e in blueEdges) {
            blueAdj[e[0]].add(e[1])
        }

        val INF = 1_000_000
        val dist = Array(n) { IntArray(2) { INF } } // 0: red, 1: blue
        val queue: java.util.ArrayDeque<Pair<Int, Int>> = java.util.ArrayDeque()
        dist[0][0] = 0
        dist[0][1] = 0
        queue.add(Pair(0, 0))
        queue.add(Pair(0, 1))

        while (queue.isNotEmpty()) {
            val (node, color) = queue.poll()
            val curDist = dist[node][color]
            if (color == 0) { // last edge was red, need blue edges
                for (nbr in blueAdj[node]) {
                    if (dist[nbr][1] > curDist + 1) {
                        dist[nbr][1] = curDist + 1
                        queue.add(Pair(nbr, 1))
                    }
                }
            } else { // last edge was blue, need red edges
                for (nbr in redAdj[node]) {
                    if (dist[nbr][0] > curDist + 1) {
                        dist[nbr][0] = curDist + 1
                        queue.add(Pair(nbr, 0))
                    }
                }
            }
        }

        val answer = IntArray(n)
        for (i in 0 until n) {
            val best = kotlin.math.min(dist[i][0], dist[i][1])
            answer[i] = if (best == INF) -1 else best
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> shortestAlternatingPaths(int n, List<List<int>> redEdges, List<List<int>> blueEdges) {
    const int INF = 1 << 30;
    List<List<int>> redAdj = List.generate(n, (_) => <int>[]);
    List<List<int>> blueAdj = List.generate(n, (_) => <int>[]);

    for (var e in redEdges) {
      redAdj[e[0]].add(e[1]);
    }
    for (var e in blueEdges) {
      blueAdj[e[0]].add(e[1]);
    }

    List<int> distRed = List.filled(n, INF);
    List<int> distBlue = List.filled(n, INF);
    distRed[0] = 0;
    distBlue[0] = 0;

    List<List<int>> q = [];
    int head = 0;
    q.add([0, 0]); // last edge red
    q.add([0, 1]); // last edge blue

    while (head < q.length) {
      var cur = q[head++];
      int node = cur[0];
      int color = cur[1];
      int curDist = (color == 0) ? distRed[node] : distBlue[node];

      if (color == 0) { // last red, need blue edges
        for (int nb in blueAdj[node]) {
          if (distBlue[nb] > curDist + 1) {
            distBlue[nb] = curDist + 1;
            q.add([nb, 1]);
          }
        }
      } else { // last blue, need red edges
        for (int nb in redAdj[node]) {
          if (distRed[nb] > curDist + 1) {
            distRed[nb] = curDist + 1;
            q.add([nb, 0]);
          }
        }
      }
    }

    List<int> ans = List.filled(n, -1);
    for (int i = 0; i < n; i++) {
      int d = distRed[i] < distBlue[i] ? distRed[i] : distBlue[i];
      if (d != INF) ans[i] = d;
    }
    return ans;
  }
}
```

## Golang

```go
func shortestAlternatingPaths(n int, redEdges [][]int, blueEdges [][]int) []int {
	const (
		RED  = 0
		BLUE = 1
	)
	redAdj := make([][]int, n)
	blueAdj := make([][]int, n)
	for _, e := range redEdges {
		u, v := e[0], e[1]
		redAdj[u] = append(redAdj[u], v)
	}
	for _, e := range blueEdges {
		u, v := e[0], e[1]
		blueAdj[u] = append(blueAdj[u], v)
	}

	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = -1
	}
	ans[0] = 0

	type node struct {
		idx   int
		color int
		dist  int
	}
	queue := []node{{0, RED, 0}, {0, BLUE, 0}}
	visited := make([][2]bool, n)
	visited[0][RED], visited[0][BLUE] = true, true

	for front := 0; front < len(queue); front++ {
		cur := queue[front]
		var nextList []int
		if cur.color == RED {
			nextList = blueAdj[cur.idx]
		} else {
			nextList = redAdj[cur.idx]
		}
		nextColor := BLUE
		if cur.color == BLUE {
			nextColor = RED
		}
		for _, nb := range nextList {
			if visited[nb][nextColor] {
				continue
			}
			visited[nb][nextColor] = true
			if ans[nb] == -1 || ans[nb] > cur.dist+1 {
				ans[nb] = cur.dist + 1
			}
			queue = append(queue, node{nb, nextColor, cur.dist + 1})
		}
	}
	return ans
}
```

## Ruby

```ruby
def shortest_alternating_paths(n, red_edges, blue_edges)
  red_adj = Array.new(n) { [] }
  blue_adj = Array.new(n) { [] }

  red_edges.each { |u, v| red_adj[u] << v }
  blue_edges.each { |u, v| blue_adj[u] << v }

  inf = 1 << 30
  dist = Array.new(n) { [inf, inf] } # [last_red, last_blue]

  queue = []
  head = 0

  dist[0][0] = 0
  dist[0][1] = 0
  queue << [0, 0]
  queue << [0, 1]

  while head < queue.size
    node, color = queue[head]
    head += 1
    cur = dist[node][color]

    if color == 0
      blue_adj[node].each do |nbr|
        if dist[nbr][1] > cur + 1
          dist[nbr][1] = cur + 1
          queue << [nbr, 1]
        end
      end
    else
      red_adj[node].each do |nbr|
        if dist[nbr][0] > cur + 1
          dist[nbr][0] = cur + 1
          queue << [nbr, 0]
        end
      end
    end
  end

  result = Array.new(n)
  (0...n).each do |i|
    best = [dist[i][0], dist[i][1]].min
    result[i] = best == inf ? -1 : best
  end
  result
end
```

## Scala

```scala
object Solution {
    def shortestAlternatingPaths(n: Int, redEdges: Array[Array[Int]], blueEdges: Array[Array[Int]]): Array[Int] = {
        import scala.collection.mutable.{ArrayBuffer, Queue}
        val redAdj = Array.fill(n)(ArrayBuffer[Int]())
        val blueAdj = Array.fill(n)(ArrayBuffer[Int]())
        for (e <- redEdges) redAdj(e(0)) += e(1)
        for (e <- blueEdges) blueAdj(e(0)) += e(1)

        val INF = Int.MaxValue / 4
        val dist = Array.ofDim[Int](n, 2)
        for (i <- 0 until n; c <- 0 to 1) dist(i)(c) = INF
        dist(0)(0) = 0
        dist(0)(1) = 0

        val q: Queue[(Int, Int)] = Queue()
        q.enqueue((0, 0))
        q.enqueue((0, 1))

        while (q.nonEmpty) {
            val (u, color) = q.dequeue()
            val nextColor = 1 - color
            val neighbors = if (nextColor == 0) redAdj(u) else blueAdj(u)
            for (v <- neighbors) {
                if (dist(v)(nextColor) == INF) {
                    dist(v)(nextColor) = dist(u)(color) + 1
                    q.enqueue((v, nextColor))
                }
            }
        }

        val ans = new Array[Int](n)
        for (i <- 0 until n) {
            val best = math.min(dist(i)(0), dist(i)(1))
            ans(i) = if (best == INF) -1 else best
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn shortest_alternating_paths(n: i32, red_edges: Vec<Vec<i32>>, blue_edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut red_adj = vec![Vec::<usize>::new(); n];
        let mut blue_adj = vec![Vec::<usize>::new(); n];

        for e in red_edges.iter() {
            let from = e[0] as usize;
            let to = e[1] as usize;
            red_adj[from].push(to);
        }
        for e in blue_edges.iter() {
            let from = e[0] as usize;
            let to = e[1] as usize;
            blue_adj[from].push(to);
        }

        const INF: i32 = i32::MAX / 2;
        let mut dist = vec![vec![INF; 2]; n];
        let mut q = VecDeque::new();

        dist[0][0] = 0;
        dist[0][1] = 0;
        q.push_back((0usize, 0usize));
        q.push_back((0usize, 1usize));

        while let Some((u, color)) = q.pop_front() {
            let cur = dist[u][color];
            let next_color = 1 - color;
            let neighbors = if next_color == 0 { &red_adj[u] } else { &blue_adj[u] };
            for &v in neighbors.iter() {
                if dist[v][next_color] == INF {
                    dist[v][next_color] = cur + 1;
                    q.push_back((v, next_color));
                }
            }
        }

        let mut ans = vec![-1i32; n];
        for i in 0..n {
            let best = dist[i][0].min(dist[i][1]);
            if best != INF {
                ans[i] = best;
            }
        }
        ans
    }
}
```

## Racket

```racket
(require racket/queue)

(define/contract (shortest-alternating-paths n redEdges blueEdges)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ((red-adj (make-vector n '()))
         (blue-adj (make-vector n '())))
    ;; build adjacency lists
    (for ([e redEdges])
      (let* ((u (first e)) (v (second e)))
        (vector-set! red-adj u (cons v (vector-ref red-adj u)))))
    (for ([e blueEdges])
      (let* ((u (first e)) (v (second e)))
        (vector-set! blue-adj u (cons v (vector-ref blue-adj u)))))
    ;; distance matrix: for each node store [dist-red-last dist-blue-last]
    (define dist (make-vector n))
    (for ([i (in-range n)])
      (vector-set! dist i (vector -1 -1)))
    (let ((start-row (vector-ref dist 0)))
      (vector-set! start-row 0 0)
      (vector-set! start-row 1 0))
    ;; BFS queue
    (define q (make-queue))
    (enqueue! q (list 0 0)) ; last edge red
    (enqueue! q (list 0 1)) ; last edge blue
    (while (not (queue-empty? q))
      (define cur (dequeue! q))
      (define node (first cur))
      (define col (second cur))          ; 0 = red, 1 = blue
      (define cur-dist (vector-ref (vector-ref dist node) col))
      (if (= col 0)
          ;; need a blue edge next
          (for ([nbr (in-list (vector-ref blue-adj node))])
            (when (= (vector-ref (vector-ref dist nbr) 1) -1)
              (let ((row (vector-ref dist nbr)))
                (vector-set! row 1 (+ cur-dist 1))
                (enqueue! q (list nbr 1)))))
          ;; need a red edge next
          (for ([nbr (in-list (vector-ref red-adj node))])
            (when (= (vector-ref (vector-ref dist nbr) 0) -1)
              (let ((row (vector-ref dist nbr)))
                (vector-set! row 0 (+ cur-dist 1))
                (enqueue! q (list nbr 0)))))))
    ;; construct answer
    (for/list ([i (in-range n)])
      (if (= i 0)
          0
          (let* ((row (vector-ref dist i))
                 (d0 (vector-ref row 0))
                 (d1 (vector-ref row 1)))
            (cond [(and (= d0 -1) (= d1 -1)) -1]
                  [(= d0 -1) d1]
                  [(= d1 -1) d0]
                  [else (min d0 d1)])))))))
```

## Erlang

```erlang
-spec shortest_alternating_paths(N :: integer(), RedEdges :: [[integer()]], BlueEdges :: [[integer()]]) -> [integer()].
shortest_alternating_paths(N, RedEdges, BlueEdges) ->
    RedMap = build_map(RedEdges),
    BlueMap = build_map(BlueEdges),

    Inf = 1 bsl 30,
    InitDistR = maps:from_list([{I, Inf} || I <- lists:seq(0, N - 1)]),
    InitDistB = maps:from_list([{I, Inf} || I <- lists:seq(0, N - 1)]),

    DistR0 = maps:put(0, 0, InitDistR),
    DistB0 = maps:put(0, 0, InitDistB),

    Q0 = queue:new(),
    Q1 = queue:in({0, 0}, Q0),   % last edge considered red
    Q2 = queue:in({0, 1}, Q1),   % last edge considered blue

    {FinalDistR, FinalDistB} = bfs(Q2, RedMap, BlueMap, DistR0, DistB0),

    [ case min(maps:get(I, FinalDistR), maps:get(I, FinalDistB)) of
          D when D == Inf -> -1;
          D -> D
      end || I <- lists:seq(0, N - 1) ].

build_map([]) ->
    #{};
build_map([[U, V] | Rest]) ->
    Map = build_map(Rest),
    List = maps:get(U, Map, []),
    maps:put(U, [V | List], Map).

bfs(Queue, RedMap, BlueMap, DistR, DistB) ->
    case queue:is_empty(Queue) of
        true ->
            {DistR, DistB};
        false ->
            {{value, {Node, Color}}, QRest} = queue:out(Queue),
            CurrDist = case Color of
                0 -> maps:get(Node, DistR);
                1 -> maps:get(Node, DistB)
            end,
            NextColor = 1 - Color,
            AdjMap = if NextColor == 0 -> RedMap; true -> BlueMap end,
            Neighbors = maps:get(Node, AdjMap, []),
            {QNew, DistRNew, DistBNew} =
                process_neighbors(Neighbors, NextColor, CurrDist + 1, QRest, DistR, DistB),
            bfs(QNew, RedMap, BlueMap, DistRNew, DistBNew)
    end.

process_neighbors([], _Color, _Dist, Queue, DistR, DistB) ->
    {Queue, DistR, DistB};
process_neighbors([Nbr | Rest], Color, NewDist, Queue, DistR, DistB) ->
    case Color of
        0 ->
            Old = maps:get(Nbr, DistR),
            if NewDist < Old ->
                    DistR1 = maps:put(Nbr, NewDist, DistR),
                    Queue1 = queue:in({Nbr, 0}, Queue);
               true ->
                    DistR1 = DistR,
                    Queue1 = Queue
            end,
            process_neighbors(Rest, Color, NewDist, Queue1, DistR1, DistB);
        1 ->
            Old = maps:get(Nbr, DistB),
            if NewDist < Old ->
                    DistB1 = maps:put(Nbr, NewDist, DistB),
                    Queue1 = queue:in({Nbr, 1}, Queue);
               true ->
                    DistB1 = DistB,
                    Queue1 = Queue
            end,
            process_neighbors(Rest, Color, NewDist, Queue1, DistR, DistB1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_alternating_paths(n :: integer, red_edges :: [[integer]], blue_edges :: [[integer]]) :: [integer]
  def shortest_alternating_paths(n, red_edges, blue_edges) do
    red_adj = build_adj(red_edges)
    blue_adj = build_adj(blue_edges)

    ans = List.duplicate(-1, n) |> List.replace_at(0, 0)

    queue = :queue.from_list([{0, nil, 0}])
    visited = MapSet.new()

    bfs(queue, visited, ans, red_adj, blue_adj)
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [u, v], acc ->
      Map.update(acc, u, [v], &[v | &1])
    end)
  end

  defp bfs(queue, visited, ans, red_adj, blue_adj) do
    case :queue.out(queue) do
      {:empty, _} ->
        ans

      {{node, last_color, dist}, q} ->
        colors =
          cond do
            last_color == nil -> [:red, :blue]
            last_color == :red -> [:blue]
            true -> [:red]
          end

        {visited2, ans2, q2} =
          Enum.reduce(colors, {visited, ans, q}, fn color,
                                                    {vis_acc, ans_acc, q_acc} ->
            adj = case color do
              :red -> Map.get(red_adj, node, [])
              :blue -> Map.get(blue_adj, node, [])
            end

            Enum.reduce(adj, {vis_acc, ans_acc, q_acc}, fn nb,
                                                          {v_set, a_list,
                                                           q_queue} ->
              state = {nb, color}

              if MapSet.member?(v_set, state) do
                {v_set, a_list, q_queue}
              else
                v_set = MapSet.put(v_set, state)
                new_dist = dist + 1

                a_list =
                  if Enum.at(a_list, nb) == -1 do
                    List.replace_at(a_list, nb, new_dist)
                  else
                    a_list
                  end

                q_queue = :queue.in({nb, color, new_dist}, q_queue)
                {v_set, a_list, q_queue}
              end
            end)
          end)

        bfs(q2, visited2, ans2, red_adj, blue_adj)
    end
  end
end
```

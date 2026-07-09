# 2493. Divide Nodes Into the Maximum Number of Groups

## Cpp

```cpp
class Solution {
public:
    int magnificentSets(int n, vector<vector<int>>& edges) {
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            g[u].push_back(v);
            g[v].push_back(u);
        }
        vector<int> color(n, -1);
        vector<char> visited(n, 0);
        int totalGroups = 0;
        
        for (int i = 0; i < n; ++i) {
            if (visited[i]) continue;
            
            // BFS to collect component and check bipartite
            queue<int> q;
            q.push(i);
            color[i] = 0;
            visited[i] = 1;
            vector<int> comp;
            comp.push_back(i);
            bool ok = true;
            while (!q.empty() && ok) {
                int v = q.front(); q.pop();
                for (int nb : g[v]) {
                    if (color[nb] == -1) {
                        color[nb] = color[v] ^ 1;
                        visited[nb] = 1;
                        q.push(nb);
                        comp.push_back(nb);
                    } else if (color[nb] == color[v]) {
                        ok = false;
                        break;
                    }
                }
            }
            if (!ok) return -1;
            
            // Compute diameter of this component
            int diam = 0;
            for (int src : comp) {
                vector<int> dist(n, -1);
                queue<int> qq;
                dist[src] = 0;
                qq.push(src);
                while (!qq.empty()) {
                    int v = qq.front(); qq.pop();
                    for (int nb : g[v]) {
                        if (dist[nb] == -1) {
                            dist[nb] = dist[v] + 1;
                            qq.push(nb);
                        }
                    }
                }
                for (int node : comp) {
                    diam = max(diam, dist[node]);
                }
            }
            totalGroups += diam + 1;
        }
        return totalGroups;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int magnificentSets(int n, int[][] edges) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            adj[u].add(v);
            adj[v].add(u);
        }

        int[] color = new int[n];
        Arrays.fill(color, -1);
        boolean[] visitedComp = new boolean[n];
        int totalGroups = 0;

        for (int i = 0; i < n; i++) {
            if (visitedComp[i]) continue;

            // Gather component nodes and check bipartiteness
            List<Integer> compNodes = new ArrayList<>();
            Queue<Integer> q = new LinkedList<>();
            q.add(i);
            color[i] = 0;
            visitedComp[i] = true;
            boolean ok = true;

            while (!q.isEmpty()) {
                int u = q.poll();
                compNodes.add(u);
                for (int v : adj[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] ^ 1;
                        visitedComp[v] = true;
                        q.add(v);
                    } else if (color[v] == color[u]) {
                        ok = false;
                    }
                }
            }

            if (!ok) return -1;

            // Compute diameter of this component
            int maxDist = 0;
            for (int start : compNodes) {
                int[] dist = new int[n];
                Arrays.fill(dist, -1);
                Queue<Integer> bfs = new LinkedList<>();
                bfs.add(start);
                dist[start] = 0;

                while (!bfs.isEmpty()) {
                    int u = bfs.poll();
                    for (int v : adj[u]) {
                        if (dist[v] == -1) {
                            dist[v] = dist[u] + 1;
                            bfs.add(v);
                        }
                    }
                }

                for (int node : compNodes) {
                    maxDist = Math.max(maxDist, dist[node]);
                }
            }

            totalGroups += maxDist + 1; // groups = diameter + 1
        }

        return totalGroups;
    }
}
```

## Python

```python
class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import deque

        # build adjacency list (0-indexed)
        g = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)

        color = [-1] * n
        components = []

        # check bipartite and collect nodes of each component
        for i in range(n):
            if color[i] != -1:
                continue
            q = deque([i])
            color[i] = 0
            comp = [i]
            while q:
                u = q.popleft()
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                        comp.append(v)
                    elif color[v] == color[u]:
                        return -1
            components.append(comp)

        total_groups = 0

        # compute diameter (longest shortest path) for each component
        for comp in components:
            max_dist_in_comp = 0
            for start in comp:
                dist = [-1] * n
                dq = deque([start])
                dist[start] = 0
                while dq:
                    u = dq.popleft()
                    for v in g[u]:
                        if dist[v] == -1:
                            dist[v] = dist[u] + 1
                            dq.append(v)
                # farthest node within this component
                local_max = max(dist[node] for node in comp)
                if local_max > max_dist_in_comp:
                    max_dist_in_comp = local_max
            total_groups += max_dist_in_comp + 1

        return total_groups
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * n
        total_groups = 0

        for i in range(n):
            if color[i] != -1:
                continue

            # BFS to check bipartite and collect component nodes
            comp_nodes = []
            q = deque([i])
            color[i] = 0
            comp_nodes.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                        comp_nodes.append(v)
                    elif color[v] == color[u]:
                        return -1

            # Compute diameter of this component
            max_dist = 0
            for src in comp_nodes:
                dist = [-1] * n
                dq = deque([src])
                dist[src] = 0
                while dq:
                    u = dq.popleft()
                    for v in adj[u]:
                        if dist[v] == -1:
                            dist[v] = dist[u] + 1
                            dq.append(v)
                            if dist[v] > max_dist:
                                max_dist = dist[v]
            total_groups += max_dist + 1

        return total_groups
```

## C

```c
#include <stdlib.h>
#include <string.h>

int magnificentSets(int n, int** edges, int edgesSize, int* edgesColSize) {
    // adjacency list with fixed maximum size
    static int adj[501][501];
    static int deg[501];
    memset(deg, 0, sizeof(deg));

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0] - 1;
        int v = edges[i][1] - 1;
        adj[u][deg[u]++] = v;
        adj[v][deg[v]++] = u;
    }

    static int color[501];
    for (int i = 0; i < n; ++i) color[i] = -1;

    static int visitedComp[501];
    memset(visitedComp, 0, sizeof(visitedComp));

    int totalGroups = 0;
    static int queue[501];
    static int compNodes[501];
    static int dist[501];
    static int bfsQueue[501];

    for (int start = 0; start < n; ++start) {
        if (visitedComp[start]) continue;

        // BFS to collect component and check bipartite
        int qh = 0, qt = 0;
        queue[qt++] = start;
        visitedComp[start] = 1;
        color[start] = 0;
        int compCnt = 0;
        compNodes[compCnt++] = start;
        int isBipartite = 1;

        while (qh < qt) {
            int cur = queue[qh++];
            for (int i = 0; i < deg[cur]; ++i) {
                int nb = adj[cur][i];
                if (!visitedComp[nb]) {
                    visitedComp[nb] = 1;
                    color[nb] = color[cur] ^ 1;
                    queue[qt++] = nb;
                    compNodes[compCnt++] = nb;
                } else if (color[nb] == color[cur]) {
                    isBipartite = 0;
                }
            }
        }

        if (!isBipartite) return -1;

        // Compute diameter of this component
        int diam = 0;
        for (int i = 0; i < compCnt; ++i) {
            int src = compNodes[i];
            for (int j = 0; j < n; ++j) dist[j] = -1;
            int h = 0, t = 0;
            bfsQueue[t++] = src;
            dist[src] = 0;

            while (h < t) {
                int cur = bfsQueue[h++];
                for (int k = 0; k < deg[cur]; ++k) {
                    int nb = adj[cur][k];
                    if (dist[nb] == -1) {
                        dist[nb] = dist[cur] + 1;
                        bfsQueue[t++] = nb;
                    }
                }
            }

            for (int j = 0; j < compCnt; ++j) {
                int v = compNodes[j];
                if (dist[v] > diam) diam = dist[v];
            }
        }

        totalGroups += diam + 1;
    }

    return totalGroups;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int MagnificentSets(int n, int[][] edges) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            graph[u].Add(v);
            graph[v].Add(u);
        }

        var color = new int[n];
        for (int i = 0; i < n; i++) color[i] = -1;

        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (color[i] != -1) continue;

            // Color the component and collect its nodes
            var compNodes = new List<int>();
            var q = new Queue<int>();
            q.Enqueue(i);
            color[i] = 0;
            compNodes.Add(i);

            while (q.Count > 0) {
                int u = q.Dequeue();
                foreach (int v in graph[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] ^ 1;
                        q.Enqueue(v);
                        compNodes.Add(v);
                    } else if (color[v] == color[u]) {
                        return -1; // not bipartite
                    }
                }
            }

            // Compute the diameter of this component
            int diam = 0;
            foreach (int start in compNodes) {
                var dist = new int[n];
                for (int k = 0; k < n; k++) dist[k] = -1;
                var q2 = new Queue<int>();
                dist[start] = 0;
                q2.Enqueue(start);
                while (q2.Count > 0) {
                    int cur = q2.Dequeue();
                    foreach (int nb in graph[cur]) {
                        if (dist[nb] == -1) {
                            dist[nb] = dist[cur] + 1;
                            q2.Enqueue(nb);
                        }
                    }
                }
                foreach (int node in compNodes) {
                    if (dist[node] > diam) diam = dist[node];
                }
            }

            answer += diam + 1; // groups = diameter + 1
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var magnificentSets = function(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        const a = u - 1, b = v - 1;
        adj[a].push(b);
        adj[b].push(a);
    }

    const color = new Array(n).fill(-1);
    let answer = 0;

    for (let i = 0; i < n; ++i) {
        if (color[i] !== -1) continue;

        // BFS to collect component and check bipartite
        const queue = [i];
        color[i] = 0;
        const comp = [i];
        let head = 0;
        let ok = true;

        while (head < queue.length && ok) {
            const node = queue[head++];
            for (const nb of adj[node]) {
                if (color[nb] === -1) {
                    color[nb] = color[node] ^ 1;
                    queue.push(nb);
                    comp.push(nb);
                } else if (color[nb] === color[node]) {
                    ok = false;
                    break;
                }
            }
        }

        if (!ok) return -1;

        // Compute diameter of this component
        let maxDist = 0;
        for (const src of comp) {
            const dist = new Array(n).fill(-1);
            const q = [src];
            dist[src] = 0;
            let h = 0;
            while (h < q.length) {
                const cur = q[h++];
                for (const nb of adj[cur]) {
                    if (dist[nb] === -1) {
                        dist[nb] = dist[cur] + 1;
                        q.push(nb);
                    }
                }
            }
            let far = 0;
            for (const v of comp) {
                if (dist[v] > far) far = dist[v];
            }
            if (far > maxDist) maxDist = far;
        }

        answer += maxDist + 1; // groups = diameter + 1
    }

    return answer;
};
```

## Typescript

```typescript
function magnificentSets(n: number, edges: number[][]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        const a = u - 1;
        const b = v - 1;
        adj[a].push(b);
        adj[b].push(a);
    }

    const color: number[] = new Array(n).fill(-1);
    let totalGroups = 0;

    for (let i = 0; i < n; i++) {
        if (color[i] !== -1) continue;

        // BFS to color the component and collect its nodes
        const queue: number[] = [i];
        color[i] = 0;
        const componentNodes: number[] = [];
        let isBipartite = true;

        while (queue.length) {
            const u = queue.shift()!;
            componentNodes.push(u);
            for (const v of adj[u]) {
                if (color[v] === -1) {
                    color[v] = color[u] ^ 1;
                    queue.push(v);
                } else if (color[v] === color[u]) {
                    isBipartite = false;
                }
            }
        }

        if (!isBipartite) return -1;

        // Compute the diameter of this component
        let maxDist = 0;
        for (const start of componentNodes) {
            const dist: number[] = new Array(n).fill(-1);
            const q2: number[] = [start];
            dist[start] = 0;
            while (q2.length) {
                const cur = q2.shift()!;
                for (const nb of adj[cur]) {
                    if (dist[nb] === -1) {
                        dist[nb] = dist[cur] + 1;
                        maxDist = Math.max(maxDist, dist[nb]);
                        q2.push(nb);
                    }
                }
            }
        }

        totalGroups += maxDist + 1; // groups = diameter + 1
    }

    return totalGroups;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function magnificentSets($n, $edges) {
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        $color   = array_fill(0, $n + 1, -1);
        $visited = array_fill(0, $n + 1, false);
        $answer  = 0;

        for ($i = 1; $i <= $n; $i++) {
            if (!$visited[$i]) {
                // collect component and check bipartite
                $queue = [];
                $head  = 0;
                $queue[] = $i;
                $color[$i]   = 0;
                $visited[$i] = true;
                $component   = [];
                $isBipartite = true;

                while ($head < count($queue) && $isBipartite) {
                    $cur = $queue[$head++];
                    $component[] = $cur;
                    foreach ($adj[$cur] as $nei) {
                        if ($color[$nei] == -1) {
                            $color[$nei]   = 1 - $color[$cur];
                            $visited[$nei] = true;
                            $queue[]       = $nei;
                        } else {
                            if ($color[$nei] == $color[$cur]) {
                                $isBipartite = false;
                                break;
                            }
                        }
                    }
                }

                if (!$isBipartite) {
                    return -1;
                }

                // compute diameter of this component
                $maxDist = 0;
                foreach ($component as $src) {
                    $dist = array_fill(0, $n + 1, -1);
                    $q    = [];
                    $qh   = 0;
                    $dist[$src] = 0;
                    $q[]        = $src;

                    while ($qh < count($q)) {
                        $v = $q[$qh++];
                        foreach ($adj[$v] as $nei) {
                            if ($dist[$nei] == -1) {
                                $dist[$nei] = $dist[$v] + 1;
                                $q[]        = $nei;
                            }
                        }
                    }

                    foreach ($component as $node) {
                        if ($dist[$node] > $maxDist) {
                            $maxDist = $dist[$node];
                        }
                    }
                }

                $answer += $maxDist + 1; // groups = diameter + 1
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func magnificentSets(_ n: Int, _ edges: [[Int]]) -> Int {
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0] - 1
            let v = e[1] - 1
            adj[u].append(v)
            adj[v].append(u)
        }
        
        var color = Array(repeating: -1, count: n) // -1 unvisited, 0/1 colors
        var totalGroups = 0
        
        for i in 0..<n {
            if color[i] != -1 { continue }
            
            // BFS to check bipartite and collect component nodes
            var queue = [Int]()
            var qIndex = 0
            queue.append(i)
            color[i] = 0
            var componentNodes = [Int]()
            
            while qIndex < queue.count {
                let node = queue[qIndex]
                qIndex += 1
                componentNodes.append(node)
                
                for nb in adj[node] {
                    if color[nb] == -1 {
                        color[nb] = color[node] ^ 1
                        queue.append(nb)
                    } else if color[nb] == color[node] {
                        return -1   // not bipartite
                    }
                }
            }
            
            // Compute diameter of this component
            var maxDistInComp = 0
            for start in componentNodes {
                var dist = Array(repeating: -1, count: n)
                var q2 = [Int]()
                var idx2 = 0
                dist[start] = 0
                q2.append(start)
                
                while idx2 < q2.count {
                    let cur = q2[idx2]
                    idx2 += 1
                    for nb in adj[cur] {
                        if dist[nb] == -1 {
                            dist[nb] = dist[cur] + 1
                            q2.append(nb)
                        }
                    }
                }
                
                var localMax = 0
                for v in componentNodes {
                    if dist[v] > localMax {
                        localMax = dist[v]
                    }
                }
                if localMax > maxDistInComp {
                    maxDistInComp = localMax
                }
            }
            
            totalGroups += maxDistInComp + 1   // groups = diameter + 1
        }
        
        return totalGroups
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun magnificentSets(n: Int, edges: Array<IntArray>): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0] - 1
            val v = e[1] - 1
            adj[u].add(v)
            adj[v].add(u)
        }

        val color = IntArray(n) { -1 }
        var totalGroups = 0
        val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()

        for (i in 0 until n) {
            if (color[i] != -1) continue

            // BFS to check bipartite and collect component nodes
            val compNodes = mutableListOf<Int>()
            queue.clear()
            queue.add(i)
            color[i] = 0
            while (!queue.isEmpty()) {
                val cur = queue.poll()
                compNodes.add(cur)
                for (nb in adj[cur]) {
                    if (color[nb] == -1) {
                        color[nb] = color[cur] xor 1
                        queue.add(nb)
                    } else if (color[nb] == color[cur]) {
                        return -1
                    }
                }
            }

            // Compute diameter of this component
            var maxDist = 0
            val dist = IntArray(n)
            for (src in compNodes) {
                java.util.Arrays.fill(dist, -1)
                queue.clear()
                queue.add(src)
                dist[src] = 0
                while (!queue.isEmpty()) {
                    val v = queue.poll()
                    for (nb in adj[v]) {
                        if (dist[nb] == -1) {
                            dist[nb] = dist[v] + 1
                            queue.add(nb)
                        }
                    }
                }
                var localMax = 0
                for (v in compNodes) {
                    if (dist[v] > localMax) localMax = dist[v]
                }
                if (localMax > maxDist) maxDist = localMax
            }

            totalGroups += maxDist + 1
        }

        return totalGroups
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int magnificentSets(int n, List<List<int>> edges) {
    // Build adjacency list (0-indexed)
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0] - 1;
      int v = e[1] - 1;
      adj[u].add(v);
      adj[v].add(u);
    }

    // Color array for bipartite check: -1 = unvisited, 0/1 = colors
    List<int> color = List.filled(n, -1);
    int totalGroups = 0;

    for (int i = 0; i < n; ++i) {
      if (color[i] != -1) continue;

      // BFS to check bipartite and collect component nodes
      List<int> compNodes = [];
      Queue<int> q = ListQueue();
      q.add(i);
      color[i] = 0;
      while (q.isNotEmpty) {
        int node = q.removeFirst();
        compNodes.add(node);
        for (int nb in adj[node]) {
          if (color[nb] == -1) {
            color[nb] = color[node] ^ 1;
            q.add(nb);
          } else if (color[nb] == color[node]) {
            // Not bipartite
            return -1;
          }
        }
      }

      // Compute diameter of this component
      int maxDist = 0;
      for (int src in compNodes) {
        List<int> dist = List.filled(n, -1);
        Queue<int> bfs = ListQueue();
        bfs.add(src);
        dist[src] = 0;
        while (bfs.isNotEmpty) {
          int cur = bfs.removeFirst();
          for (int nb in adj[cur]) {
            if (dist[nb] == -1) {
              dist[nb] = dist[cur] + 1;
              bfs.add(nb);
            }
          }
        }
        for (int node in compNodes) {
          if (dist[node] > maxDist) maxDist = dist[node];
        }
      }

      // Number of groups for this component is diameter + 1
      totalGroups += maxDist + 1;
    }

    return totalGroups;
  }
}
```

## Golang

```go
func magnificentSets(n int, edges [][]int) int {
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0]-1, e[1]-1
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	color := make([]int, n)
	for i := 0; i < n; i++ {
		color[i] = -1
	}
	visited := make([]bool, n)

	totalGroups := 0

	for i := 0; i < n; i++ {
		if visited[i] {
			continue
		}
		// BFS to check bipartite and collect component nodes
		queue := []int{i}
		color[i] = 0
		compNodes := []int{}
		visited[i] = true

		for len(queue) > 0 {
			v := queue[0]
			queue = queue[1:]
			compNodes = append(compNodes, v)
			for _, nb := range adj[v] {
				if color[nb] == -1 {
					color[nb] = 1 - color[v]
				} else if color[nb] == color[v] {
					return -1
				}
				if !visited[nb] {
					visited[nb] = true
					queue = append(queue, nb)
				}
			}
		}

		// Compute diameter of this component
		maxDist := 0
		for _, src := range compNodes {
			dist := make([]int, n)
			for k := 0; k < n; k++ {
				dist[k] = -1
			}
			q := []int{src}
			dist[src] = 0
			for len(q) > 0 {
				v := q[0]
				q = q[1:]
				for _, nb := range adj[v] {
					if dist[nb] == -1 {
						dist[nb] = dist[v] + 1
						q = append(q, nb)
					}
				}
			}
			for _, node := range compNodes {
				if dist[node] > maxDist {
					maxDist = dist[node]
				}
			}
		}
		totalGroups += maxDist + 1
	}

	return totalGroups
}
```

## Ruby

```ruby
def magnificent_sets(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    u -= 1
    v -= 1
    adj[u] << v
    adj[v] << u
  end

  color = Array.new(n, -1)
  total_groups = 0

  (0...n).each do |i|
    next unless color[i] == -1

    # BFS to collect component and check bipartiteness
    queue = [i]
    q_idx = 0
    comp_nodes = []
    color[i] = 0
    while q_idx < queue.length
      u = queue[q_idx]
      q_idx += 1
      comp_nodes << u
      adj[u].each do |v|
        if color[v] == -1
          color[v] = color[u] ^ 1
          queue << v
        elsif color[v] == color[u]
          return -1
        end
      end
    end

    # Compute diameter of this component
    max_dist = 0
    comp_nodes.each do |src|
      dist = Array.new(n, -1)
      bfs_q = [src]
      bfs_idx = 0
      dist[src] = 0
      while bfs_idx < bfs_q.length
        u = bfs_q[bfs_idx]
        bfs_idx += 1
        adj[u].each do |v|
          next if dist[v] != -1
          dist[v] = dist[u] + 1
          bfs_q << v
        end
      end
      local_max = 0
      comp_nodes.each do |node|
        d = dist[node]
        local_max = d if d > local_max
      end
      max_dist = local_max if local_max > max_dist
    end

    total_groups += max_dist + 1
  end

  total_groups
end
```

## Scala

```scala
object Solution {
  def magnificentSets(n: Int, edges: Array[Array[Int]]): Int = {
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    for (e <- edges) {
      val u = e(0) - 1
      val v = e(1) - 1
      adj(u).append(v)
      adj(v).append(u)
    }

    val color = Array.fill(n)(-1)

    def bfsComponent(start: Int): (Boolean, scala.collection.mutable.ArrayBuffer[Int]) = {
      val q = new scala.collection.mutable.Queue[Int]()
      q.enqueue(start)
      color(start) = 0
      val nodes = new scala.collection.mutable.ArrayBuffer[Int]()
      var ok = true
      while (q.nonEmpty && ok) {
        val u = q.dequeue()
        nodes += u
        for (v <- adj(u)) {
          if (color(v) == -1) {
            color(v) = color(u) ^ 1
            q.enqueue(v)
          } else if (color(v) == color(u)) {
            ok = false
          }
        }
      }
      (ok, nodes)
    }

    def bfsFarthest(src: Int): (Int, Int) = {
      val dist = Array.fill(n)(-1)
      val q = new scala.collection.mutable.Queue[Int]()
      q.enqueue(src)
      dist(src) = 0
      var farNode = src
      var maxDist = 0
      while (q.nonEmpty) {
        val u = q.dequeue()
        for (v <- adj(u)) {
          if (dist(v) == -1) {
            dist(v) = dist(u) + 1
            q.enqueue(v)
            if (dist(v) > maxDist) {
              maxDist = dist(v)
              farNode = v
            }
          }
        }
      }
      (farNode, maxDist)
    }

    var answer = 0
    for (i <- 0 until n) {
      if (color(i) == -1) {
        val (ok, compNodes) = bfsComponent(i)
        if (!ok) return -1
        // compute diameter within this component
        val startNode = compNodes.head
        val (far1, _) = bfsFarthest(startNode)
        val (_, diam) = bfsFarthest(far1)
        answer += diam + 1
      }
    }
    answer
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn magnificent_sets(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let a = (e[0] - 1) as usize;
            let b = (e[1] - 1) as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        // color: -1 unvisited, 0 or 1 for bipartite sides
        let mut color: Vec<i32> = vec![-1; n_usize];
        let mut total_groups: usize = 0;

        // helper to compute diameter of a component
        fn component_diameter(
            comp_nodes: &Vec<usize>,
            adj: &Vec<Vec<usize>>,
            n: usize,
        ) -> usize {
            let mut max_dist = 0usize;
            for &start in comp_nodes.iter() {
                let mut dist: Vec<i32> = vec![-1; n];
                let mut q: VecDeque<usize> = VecDeque::new();
                dist[start] = 0;
                q.push_back(start);
                while let Some(u) = q.pop_front() {
                    let d = dist[u];
                    for &v in adj[u].iter() {
                        if dist[v] == -1 {
                            dist[v] = d + 1;
                            if dist[v] as usize > max_dist {
                                max_dist = dist[v] as usize;
                            }
                            q.push_back(v);
                        }
                    }
                }
            }
            max_dist
        }

        for i in 0..n_usize {
            if color[i] == -1 {
                // BFS to collect component and check bipartiteness
                let mut q: VecDeque<usize> = VecDeque::new();
                q.push_back(i);
                color[i] = 0;
                let mut comp_nodes: Vec<usize> = vec![i];
                let mut ok = true;

                while let Some(u) = q.pop_front() {
                    for &v in adj[u].iter() {
                        if color[v] == -1 {
                            color[v] = 1 - color[u];
                            q.push_back(v);
                            comp_nodes.push(v);
                        } else if color[v] == color[u] {
                            ok = false;
                        }
                    }
                }

                if !ok {
                    return -1;
                }

                let diam = component_diameter(&comp_nodes, &adj, n_usize);
                total_groups += diam + 1; // groups = diameter (edges) + 1
            }
        }

        total_groups as i32
    }
}
```

## Racket

```racket
(define (bfs-component start adj visited colors)
  (let loop ((queue (list start))
             (comp '())
             (conflict #f))
    (if conflict
        #f
        (if (null? queue)
            (reverse comp)
            (let* ([curr (car queue)]
                   [rest (cdr queue)])
              (define new-comp (cons curr comp))
              (define new-neigh '())
              (for ([nbr (in-list (vector-ref adj curr))])
                (cond
                  [(not (vector-ref visited nbr))
                   (vector-set! visited nbr #t)
                   (vector-set! colors nbr (- 1 (vector-ref colors curr))) ; toggle 0/1
                   (set! new-neigh (cons nbr new-neigh))]
                  [else
                   (when (= (vector-ref colors nbr) (vector-ref colors curr))
                     (set! conflict #t))]))
              (loop (append rest (reverse new-neigh)) new-comp conflict))))))

(define (component-diameter comp adj n)
  (let ((maxd 0))
    (for ([src comp])
      (let* ((dist (make-vector n -1))
             (queue (list src)))
        (vector-set! dist src 0)
        (let loop ((q queue) (curmax 0))
          (if (null? q)
              (set! maxd (max maxd curmax))
              (let* ([curr (car q)] [rest (cdr q)])
                (for ([nbr (in-list (vector-ref adj curr))])
                  (when (= (vector-ref dist nbr) -1)
                    (vector-set! dist nbr (+ 1 (vector-ref dist curr)))
                    (set! rest (append rest (list nbr)))))
                (let ((newmax (max curmax (vector-ref dist curr))))
                  (loop rest newmax)))))))
    maxd))

(define/contract (magnificent-sets n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([adj (make-vector n '())])
    (for ([e edges])
      (let* ([u (- (first e) 1)]
             [v (- (second e) 1)])
        (vector-set! adj u (cons v (vector-ref adj u)))
        (vector-set! adj v (cons u (vector-ref adj v)))))
    (define visited (make-vector n #f))
    (define colors (make-vector n -1))
    (let loop ((i 0) (ans 0))
      (cond
        [(= i n) ans]
        [(vector-ref visited i)
         (loop (+ i 1) ans)]
        [else
         (vector-set! colors i 0)
         (vector-set! visited i #t)
         (define comp (bfs-component i adj visited colors))
         (if (not comp)
             -1
             (let ((diam (component-diameter comp adj n)))
               (loop (+ i 1) (+ ans (+ diam 1)))))]))))
```

## Erlang

```erlang
-spec magnificent_sets(N :: integer(), Edges :: [[integer()]]) -> integer().
magnificent_sets(N, Edges) ->
    Adj0 = init_adj(N),
    Adj = add_edges(Adj0, Edges),
    case loop(1, N, Adj, sets:new(), 0) of
        {ok, Total} -> Total;
        error -> -1
    end.

init_adj(N) ->
    lists:foldl(fun(I, Acc) -> maps:put(I, [], Acc) end, #{}, lists:seq(1, N)).

add_edges(Adj, []) -> Adj;
add_edges(Adj, [[A, B] | Rest]) ->
    Adj1 = maps:update_with(A,
            fun(L) -> [B | L] end,
            [B],
            Adj),
    Adj2 = maps:update_with(B,
            fun(L) -> [A | L] end,
            [A],
            Adj1),
    add_edges(Adj2, Rest).

loop(I, N, _Adj, _Visited, Acc) when I > N ->
    {ok, Acc};
loop(I, N, Adj, Visited, Acc) ->
    case sets:is_element(I, Visited) of
        true ->
            loop(I + 1, N, Adj, Visited, Acc);
        false ->
            case bfs_component(I, Adj) of
                error -> error;
                {ok, CompSet, _ColorMap} ->
                    Nodes = sets:to_list(CompSet),
                    Diam = max_diameter(Nodes, Adj),
                    Groups = Diam + 1,
                    NewVisited = sets:union(Visited, CompSet),
                    loop(I + 1, N, Adj, NewVisited, Acc + Groups)
            end
    end.

bfs_component(Start, Adj) ->
    Queue0 = queue:in({Start, 0}, queue:new()),
    Visited0 = sets:add_element(Start, sets:new()),
    ColorMap0 = #{Start => 0},
    bfs_comp(Queue0, Visited0, ColorMap0, Adj).

bfs_comp(Queue, Visited, ColorMap, _Adj) ->
    case queue:out(Queue) of
        {empty, _} -> {ok, Visited, ColorMap};
        {{value, {Node, Col}}, Q1} ->
            Neighs = maps:get(Node, _Adj),
            Result = lists:foldl(
                fun(Nbr, Acc) ->
                    case Acc of
                        error -> error;
                        {QAcc, VAcc, CAcc} ->
                            if sets:is_element(Nbr, VAcc) ->
                                    ExistingCol = maps:get(Nbr, CAcc),
                                    if ExistingCol == Col -> error; true -> {QAcc, VAcc, CAcc}
                                    end;
                               true ->
                                    NewCol = 1 - Col,
                                    {queue:in({Nbr, NewCol}, QAcc), sets:add_element(Nbr, VAcc), maps:put(Nbr, NewCol, CAcc)}
                            end
                    end
                end,
                {Q1, Visited, ColorMap},
                Neighs),
            case Result of
                error -> error;
                {NewQueue, NewVisited, NewColorMap} ->
                    bfs_comp(NewQueue, NewVisited, NewColorMap, _Adj)
            end
    end.

bfs_farthest(Start, Adj) ->
    bfs_farthest(queue:in({Start, 0}, queue:new()), sets:add_element(Start, sets:new()), 0, Adj).

bfs_farthest(Queue, Visited, MaxD, Adj) ->
    case queue:out(Queue) of
        {empty, _} -> MaxD;
        {{value, {Node, Dist}}, Q1} ->
            NewMax = max(MaxD, Dist),
            Neighs = maps:get(Node, Adj),
            {Q2, Vis2} = lists:foldl(
                fun(Nbr, {QAcc, VAcc}) ->
                    if sets:is_element(Nbr, VAcc) -> {QAcc, VAcc};
                       true -> {queue:in({Nbr, Dist + 1}, QAcc), sets:add_element(Nbr, VAcc)}
                    end
                end,
                {Q1, Visited},
                Neighs),
            bfs_farthest(Q2, Vis2, NewMax, Adj)
    end.

max_diameter(Nodes, Adj) ->
    lists:max([bfs_farthest(Node, Adj) || Node <- Nodes]).
```

## Elixir

```elixir
defmodule Solution do
  @spec magnificent_sets(n :: integer, edges :: [[integer]]) :: integer
  def magnificent_sets(n, edges) do
    # Build adjacency map (0-indexed)
    adj =
      Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)

    adj =
      Enum.reduce(edges, adj, fn [a, b], acc ->
        a0 = a - 1
        b0 = b - 1

        acc
        |> update_in([a0], &[b0 | &1])
        |> update_in([b0], &[a0 | &1])
      end)

    colors = :array.new(n, default: -1)

    result =
      Enum.reduce_while(0..(n - 1), {colors, 0}, fn i, {col_arr, groups_acc} ->
        case :array.get(i, col_arr) do
          -1 ->
            case bfs_collect(i, adj, col_arr) do
              {:error} ->
                {:halt, -1}

              {:ok, new_colors, component_nodes} ->
                max_dist =
                  Enum.reduce(component_nodes, 0, fn node, cur_max ->
                    d = bfs_farthest(node, adj)
                    if d > cur_max, do: d, else: cur_max
                  end)

                {:cont, {new_colors, groups_acc + max_dist + 1}}
            end

          _ ->
            {:cont, {col_arr, groups_acc}}
        end
      end)

    case result do
      -1 -> -1
      {_final_colors, total} -> total
    end
  end

  # BFS to color a component and collect its nodes.
  defp bfs_collect(start, adj, colors) do
    q = :queue.new() |> :queue.in(start)
    colors = :array.set(start, 0, colors)
    bfs_collect_loop(q, adj, colors, [])
  end

  defp bfs_collect_loop(queue, adj, colors, comp) do
    case :queue.out(queue) do
      {:empty, _} ->
        {:ok, colors, comp}

      {{:value, node}, q2} ->
        comp = [node | comp]
        col_node = :array.get(node, colors)

        {colors, q3, ok} =
          Enum.reduce_while(Map.get(adj, node), {colors, q2, true}, fn nb,
                                                                     {col_acc, q_acc, _ok} ->
            col_nb = :array.get(nb, col_acc)

            cond do
              col_nb == -1 ->
                new_colors = :array.set(nb, 1 - col_node, col_acc)
                {:cont, {new_colors, :queue.in(nb, q_acc), true}}

              col_nb == col_node ->
                {:halt, {col_acc, q_acc, false}}

              true ->
                {:cont, {col_acc, q_acc, true}}
            end
          end)

        if ok do
          bfs_collect_loop(q3, adj, colors, comp)
        else
          {:error}
        end
    end
  end

  # BFS to find farthest distance from src within its component.
  defp bfs_farthest(src, adj) do
    q = :queue.new() |> :queue.in({src, 0})
    visited = MapSet.new([src])
    bfs_farthest_loop(q, adj, visited, 0)
  end

  defp bfs_farthest_loop(queue, adj, visited, far) do
    case :queue.out(queue) do
      {:empty, _} ->
        far

      {{:value, {node, dist}}, q2} ->
        new_far = if dist > far, do: dist, else: far

        {q3, visited2} =
          Enum.reduce(Map.get(adj, node), {q2, visited}, fn nb,
                                                          {q_acc, vis_acc} ->
            if MapSet.member?(vis_acc, nb) do
              {q_acc, vis_acc}
            else
              {
                :queue.in({nb, dist + 1}, q_acc),
                MapSet.put(vis_acc, nb)
              }
            end
          end)

        bfs_farthest_loop(q3, adj, visited2, new_far)
    end
  end
end
```

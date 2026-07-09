# 3203. Find Minimum Diameter After Merging Two Trees

## Cpp

```cpp
class Solution {
public:
    // Perform BFS and return pair {farthest node, its distance}
    pair<int,int> bfs(int start, const vector<vector<int>>& adj) {
        int n = adj.size();
        vector<int> dist(n, -1);
        queue<int> q;
        q.push(start);
        dist[start] = 0;
        int farNode = start;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                    if (dist[v] > dist[farNode]) farNode = v;
                }
            }
        }
        return {farNode, dist[farNode]};
    }
    
    int treeDiameter(const vector<vector<int>>& adj) {
        if (adj.empty()) return 0;
        // first BFS from any node (0)
        auto p1 = bfs(0, adj);
        // second BFS from farthest node found
        auto p2 = bfs(p1.first, adj);
        return p2.second;
    }
    
    int minimumDiameterAfterMerge(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n = (int)edges1.size() + 1;
        int m = (int)edges2.size() + 1;
        
        vector<vector<int>> adj1(n), adj2(m);
        for (auto &e : edges1) {
            int u = e[0], v = e[1];
            adj1[u].push_back(v);
            adj1[v].push_back(u);
        }
        for (auto &e : edges2) {
            int u = e[0], v = e[1];
            adj2[u].push_back(v);
            adj2[v].push_back(u);
        }
        
        int d1 = treeDiameter(adj1);
        int d2 = treeDiameter(adj2);
        
        long long combined = (d1 + 1) / 2 + (d2 + 1) / 2 + 1; // ceil division
        long long ans = max<long long>({d1, d2, combined});
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumDiameterAfterMerge(int[][] edges1, int[][] edges2) {
        int n = edges1.length + 1;
        int m = edges2.length + 1;

        List<Integer>[] g1 = buildGraph(n, edges1);
        List<Integer>[] g2 = buildGraph(m, edges2);

        int diam1 = treeDiameter(g1);
        int diam2 = treeDiameter(g2);

        int half1 = (diam1 + 1) / 2; // ceil(diam/2)
        int half2 = (diam2 + 1) / 2;

        int combined = half1 + half2 + 1;
        return Math.max(Math.max(diam1, diam2), combined);
    }

    private List<Integer>[] buildGraph(int size, int[][] edges) {
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[size];
        for (int i = 0; i < size; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            g[u].add(v);
            g[v].add(u);
        }
        return g;
    }

    private int treeDiameter(List<Integer>[] graph) {
        if (graph.length == 1) return 0;
        int farNode = bfsFarthest(0, graph);
        return bfsDistance(farNode, graph);
    }

    // returns the node farthest from start
    private int bfsFarthest(int start, List<Integer>[] adj) {
        int n = adj.length;
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        dist[start] = 0;
        int far = start;

        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                    if (dist[v] > dist[far]) far = v;
                }
            }
        }
        return far;
    }

    // returns the maximum distance from start
    private int bfsDistance(int start, List<Integer>[] adj) {
        int n = adj.length;
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        dist[start] = 0;
        int maxDist = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                    if (dist[v] > maxDist) maxDist = dist[v];
                }
            }
        }
        return maxDist;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        from collections import deque

        def build_adj(size, edges):
            adj = [[] for _ in range(size)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def bfs(adj, start):
            n = len(adj)
            dist = [-1] * n
            q = deque([start])
            dist[start] = 0
            far_node = start
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
                        if dist[v] > dist[far_node]:
                            far_node = v
            return far_node, dist

        def tree_diameter(adj):
            if not adj:  # empty tree (shouldn't happen with given constraints)
                return 0
            start = 0
            a, _ = bfs(adj, start)
            b, dist = bfs(adj, a)
            return dist[b]

        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        adj1 = build_adj(n1, edges1)
        adj2 = build_adj(n2, edges2)

        d1 = tree_diameter(adj1)
        d2 = tree_diameter(adj2)

        combined = (d1 + 1) // 2 + (d2 + 1) // 2 + 1
        return max(d1, d2, combined)
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build_adj(size: int, edges: List[List[int]]) -> List[List[int]]:
            adj = [[] for _ in range(size)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def bfs_farthest(start: int, adj: List[List[int]]) -> (int, int):
            n = len(adj)
            dist = [-1] * n
            q = deque([start])
            dist[start] = 0
            far_node = start
            while q:
                node = q.popleft()
                for nb in adj[node]:
                    if dist[nb] == -1:
                        dist[nb] = dist[node] + 1
                        q.append(nb)
                        if dist[nb] > dist[far_node]:
                            far_node = nb
            return far_node, dist[far_node]

        def tree_diameter(adj: List[List[int]]) -> int:
            if not adj:  # empty graph (shouldn't happen)
                return 0
            start = 0
            u, _ = bfs_farthest(start, adj)
            v, diam = bfs_farthest(u, adj)
            return diam

        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        adj1 = build_adj(n1, edges1)
        adj2 = build_adj(n2, edges2)

        d1 = tree_diameter(adj1)
        d2 = tree_diameter(adj2)

        combined = (d1 + 1) // 2 + (d2 + 1) // 2 + 1
        return max(d1, d2, combined)
```

## C

```c
#include <stdlib.h>

typedef struct {
    int to;
    int next;
} Edge;

static void addEdge(Edge *edges, int *head, int *cnt, int u, int v) {
    edges[*cnt].to = v;
    edges[*cnt].next = head[u];
    head[u] = (*cnt)++;
}

static int bfs_farthest(int start, int N, int *head, Edge *edges, int *outDist) {
    int *queue = (int *)malloc(N * sizeof(int));
    int *dist  = (int *)malloc(N * sizeof(int));
    for (int i = 0; i < N; ++i) dist[i] = -1;

    int front = 0, back = 0;
    queue[back++] = start;
    dist[start] = 0;
    int far = start;

    while (front < back) {
        int u = queue[front++];
        for (int e = head[u]; e != -1; e = edges[e].next) {
            int v = edges[e].to;
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                queue[back++] = v;
                if (dist[v] > dist[far]) far = v;
            }
        }
    }

    *outDist = dist[far];
    free(queue);
    free(dist);
    return far;
}

static int treeDiameter(int N, int *head, Edge *edges) {
    if (N == 0) return 0;
    int dummy;
    int a = bfs_farthest(0, N, head, edges, &dummy);
    int diam = bfs_farthest(a, N, head, edges, &dummy);
    return dummy;
}

int minimumDiameterAfterMerge(int** edges1, int edges1Size, int* edges1ColSize,
                              int** edges2, int edges2Size, int* edges2ColSize) {
    int n = edges1Size + 1;
    int m = edges2Size + 1;

    /* Build first tree */
    int *head1 = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head1[i] = -1;
    Edge *e1 = (Edge *)malloc(2 * edges1Size * sizeof(Edge));
    int cnt1 = 0;
    for (int i = 0; i < edges1Size; ++i) {
        int u = edges1[i][0];
        int v = edges1[i][1];
        addEdge(e1, head1, &cnt1, u, v);
        addEdge(e1, head1, &cnt1, v, u);
    }

    /* Build second tree */
    int *head2 = (int *)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) head2[i] = -1;
    Edge *e2 = (Edge *)malloc(2 * edges2Size * sizeof(Edge));
    int cnt2 = 0;
    for (int i = 0; i < edges2Size; ++i) {
        int u = edges2[i][0];
        int v = edges2[i][1];
        addEdge(e2, head2, &cnt2, u, v);
        addEdge(e2, head2, &cnt2, v, u);
    }

    int d1 = treeDiameter(n, head1, e1);
    int d2 = treeDiameter(m, head2, e2);

    int half1 = (d1 + 1) / 2;   // ceil(d1/2)
    int half2 = (d2 + 1) / 2;   // ceil(d2/2)
    long long combined = (long long)half1 + half2 + 1;

    int ans = d1;
    if (d2 > ans) ans = d2;
    if (combined > ans) ans = (int)combined;

    free(head1);
    free(e1);
    free(head2);
    free(e2);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumDiameterAfterMerge(int[][] edges1, int[][] edges2) {
        int n = edges1.Length + 1;
        int m = edges2.Length + 1;

        var adj1 = BuildAdjacency(n, edges1);
        var adj2 = BuildAdjacency(m, edges2);

        int d1 = GetDiameter(adj1);
        int d2 = GetDiameter(adj2);

        // ceil(d/2) can be computed as (d + 1) / 2
        long combined = ((long)d1 + 1) / 2 + ((long)d2 + 1) / 2 + 1;

        int result = Math.Max(d1, Math.Max(d2, (int)combined));
        return result;
    }

    private List<int>[] BuildAdjacency(int size, int[][] edges) {
        var adj = new List<int>[size];
        for (int i = 0; i < size; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }
        return adj;
    }

    private int GetDiameter(List<int>[] adj) {
        if (adj.Length == 0) return 0;
        var first = BFS(0, adj);
        var second = BFS(first.node, adj);
        return second.dist;
    }

    private (int node, int dist) BFS(int start, List<int>[] adj) {
        int n = adj.Length;
        var dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = -1;

        var q = new Queue<int>();
        q.Enqueue(start);
        dist[start] = 0;
        int farthest = start;

        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.Enqueue(v);
                    if (dist[v] > dist[farthest]) farthest = v;
                }
            }
        }

        return (farthest, dist[farthest]);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges1
 * @param {number[][]} edges2
 * @return {number}
 */
var minimumDiameterAfterMerge = function(edges1, edges2) {
    const buildAdj = (edges) => {
        const n = edges.length + 1;
        const adj = Array.from({ length: n }, () => []);
        for (const [u, v] of edges) {
            adj[u].push(v);
            adj[v].push(u);
        }
        return adj;
    };
    
    const bfsFarthest = (start, adj) => {
        const n = adj.length;
        const dist = new Int32Array(n).fill(-1);
        const q = new Array(n);
        let head = 0, tail = 0;
        q[tail++] = start;
        dist[start] = 0;
        let farNode = start;
        while (head < tail) {
            const u = q[head++];
            for (const v of adj[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    q[tail++] = v;
                    if (dist[v] > dist[farNode]) farNode = v;
                }
            }
        }
        return [farNode, dist[farNode]];
    };
    
    const treeDiameter = (adj) => {
        if (adj.length === 0) return 0;
        const [a] = bfsFarthest(0, adj);
        const [, diam] = bfsFarthest(a, adj);
        return diam;
    };
    
    const adj1 = buildAdj(edges1);
    const adj2 = buildAdj(edges2);
    
    const d1 = treeDiameter(adj1);
    const d2 = treeDiameter(adj2);
    
    const combined = Math.ceil(d1 / 2) + Math.ceil(d2 / 2) + 1;
    
    return Math.max(d1, d2, combined);
};
```

## Typescript

```typescript
function buildAdj(n: number, edges: number[][]): number[][] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    return adj;
}

function bfs(start: number, adj: number[][]): [number, number] {
    const n = adj.length;
    const dist = new Int32Array(n).fill(-1);
    const queue = new Int32Array(n);
    let head = 0,
        tail = 0;
    dist[start] = 0;
    queue[tail++] = start;
    let farNode = start;

    while (head < tail) {
        const u = queue[head++];
        for (const v of adj[u]) {
            if (dist[v] === -1) {
                dist[v] = dist[u] + 1;
                queue[tail++] = v;
                if (dist[v] > dist[farNode]) farNode = v;
            }
        }
    }
    return [farNode, dist[farNode]];
}

function minimumDiameterAfterMerge(edges1: number[][], edges2: number[][]): number {
    const n = edges1.length + 1;
    const m = edges2.length + 1;

    const adj1 = buildAdj(n, edges1);
    const adj2 = buildAdj(m, edges2);

    const [a] = bfs(0, adj1);
    const [, diam1] = bfs(a, adj1);

    const [b] = bfs(0, adj2);
    const [, diam2] = bfs(b, adj2);

    const combined = Math.ceil(diam1 / 2) + Math.ceil(diam2 / 2) + 1;
    return Math.max(diam1, diam2, combined);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $edges1
     * @param Integer[][] $edges2
     * @return Integer
     */
    function minimumDiameterAfterMerge($edges1, $edges2) {
        // Build adjacency list for first tree
        $n = count($edges1) + 1;
        $adj1 = array_fill(0, $n, []);
        foreach ($edges1 as $e) {
            [$u, $v] = $e;
            $adj1[$u][] = $v;
            $adj1[$v][] = $u;
        }
        // Build adjacency list for second tree
        $m = count($edges2) + 1;
        $adj2 = array_fill(0, $m, []);
        foreach ($edges2 as $e) {
            [$u, $v] = $e;
            $adj2[$u][] = $v;
            $adj2[$v][] = $u;
        }
        // Compute diameters
        $d1 = $this->treeDiameter($adj1);
        $d2 = $this->treeDiameter($adj2);
        // Combined diameter when connecting centers
        $combined = intdiv($d1 + 1, 2) + intdiv($d2 + 1, 2) + 1;
        return max($d1, $d2, $combined);
    }
    
    private function treeDiameter(&$adj) {
        if (empty($adj)) return 0;
        // First BFS from node 0
        [$farNode,] = $this->bfs($adj, 0);
        // Second BFS from farNode to get diameter
        [$otherFar, $dist] = $this->bfs($adj, $farNode);
        $diameter = 0;
        foreach ($dist as $d) {
            if ($d > $diameter) $diameter = $d;
        }
        return $diameter;
    }
    
    private function bfs(&$adj, $start) {
        $n = count($adj);
        $dist = array_fill(0, $n, -1);
        $queue = new SplQueue();
        $queue->enqueue($start);
        $dist[$start] = 0;
        $farNode = $start;
        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            foreach ($adj[$u] as $v) {
                if ($dist[$v] === -1) {
                    $dist[$v] = $dist[$u] + 1;
                    $queue->enqueue($v);
                    if ($dist[$v] > $dist[$farNode]) {
                        $farNode = $v;
                    }
                }
            }
        }
        return [$farNode, $dist];
    }
}
```

## Swift

```swift
class Solution {
    func minimumDiameterAfterMerge(_ edges1: [[Int]], _ edges2: [[Int]]) -> Int {
        let n = edges1.count + 1
        let m = edges2.count + 1
        
        let adj1 = buildAdjacency(n, edges1)
        let adj2 = buildAdjacency(m, edges2)
        
        let d1 = treeDiameter(adj1)
        let d2 = treeDiameter(adj2)
        
        let combined = ((d1 + 1) / 2) + ((d2 + 1) / 2) + 1
        return max(d1, d2, combined)
    }
    
    private func buildAdjacency(_ size: Int, _ edges: [[Int]]) -> [[Int]] {
        var adj = Array(repeating: [Int](), count: size)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        return adj
    }
    
    private func treeDiameter(_ adj: [[Int]]) -> Int {
        if adj.isEmpty { return 0 }
        let first = bfs(start: 0, in: adj)
        let second = bfs(start: first.node, in: adj)
        return second.distance
    }
    
    private func bfs(start: Int, in adj: [[Int]]) -> (node: Int, distance: Int) {
        var queue = [Int]()
        var head = 0
        let n = adj.count
        var dist = Array(repeating: -1, count: n)
        dist[start] = 0
        queue.append(start)
        var farNode = start
        
        while head < queue.count {
            let u = queue[head]
            head += 1
            for v in adj[u] {
                if dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    queue.append(v)
                    if dist[v] > dist[farNode] {
                        farNode = v
                    }
                }
            }
        }
        return (farNode, dist[farNode])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDiameterAfterMerge(edges1: Array<IntArray>, edges2: Array<IntArray>): Int {
        val n = edges1.size + 1
        val m = edges2.size + 1

        val adj1 = Array(n) { mutableListOf<Int>() }
        for (e in edges1) {
            val a = e[0]
            val b = e[1]
            adj1[a].add(b)
            adj1[b].add(a)
        }

        val adj2 = Array(m) { mutableListOf<Int>() }
        for (e in edges2) {
            val a = e[0]
            val b = e[1]
            adj2[a].add(b)
            adj2[b].add(a)
        }

        fun bfs(start: Int, adj: Array<MutableList<Int>>): Pair<Int, Int> {
            val dist = IntArray(adj.size) { -1 }
            val q: ArrayDeque<Int> = ArrayDeque()
            dist[start] = 0
            q.add(start)
            var farNode = start
            while (q.isNotEmpty()) {
                val u = q.removeFirst()
                for (v in adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1
                        q.add(v)
                        if (dist[v] > dist[farNode]) farNode = v
                    }
                }
            }
            return Pair(farNode, dist[farNode])
        }

        fun diameter(adj: Array<MutableList<Int>>): Int {
            if (adj.isEmpty()) return 0
            val first = bfs(0, adj).first
            return bfs(first, adj).second
        }

        val d1 = diameter(adj1)
        val d2 = diameter(adj2)

        val combined = (d1 + 1) / 2 + (d2 + 1) / 2 + 1

        return maxOf(d1, d2, combined)
    }
}
```

## Dart

```dart
class Solution {
  int minimumDiameterAfterMerge(List<List<int>> edges1, List<List<int>> edges2) {
    int n = edges1.length + 1;
    int m = edges2.length + 1;

    var adj1 = List.generate(n, (_) => <int>[]);
    for (var e in edges1) {
      int a = e[0];
      int b = e[1];
      adj1[a].add(b);
      adj1[b].add(a);
    }

    var adj2 = List.generate(m, (_) => <int>[]);
    for (var e in edges2) {
      int a = e[0];
      int b = e[1];
      adj2[a].add(b);
      adj2[b].add(a);
    }

    int d1 = _diameter(adj1);
    int d2 = _diameter(adj2);

    int combined = ((d1 + 1) ~/ 2) + ((d2 + 1) ~/ 2) + 1;
    return [d1, d2, combined].reduce((a, b) => a > b ? a : b);
  }

  int _diameter(List<List<int>> adj) {
    if (adj.isEmpty) return 0;
    int far = _bfsFarthest(0, adj);
    return _bfsMaxDist(far, adj);
  }

  int _bfsFarthest(int start, List<List<int>> adj) {
    int n = adj.length;
    var visited = List<bool>.filled(n, false);
    var dist = List<int>.filled(n, 0);
    var queue = List<int>.filled(n, 0);
    int head = 0, tail = 0;

    queue[tail++] = start;
    visited[start] = true;
    int farNode = start;

    while (head < tail) {
      int cur = queue[head++];
      for (int nb in adj[cur]) {
        if (!visited[nb]) {
          visited[nb] = true;
          dist[nb] = dist[cur] + 1;
          queue[tail++] = nb;
          if (dist[nb] > dist[farNode]) farNode = nb;
        }
      }
    }
    return farNode;
  }

  int _bfsMaxDist(int start, List<List<int>> adj) {
    int n = adj.length;
    var visited = List<bool>.filled(n, false);
    var dist = List<int>.filled(n, 0);
    var queue = List<int>.filled(n, 0);
    int head = 0, tail = 0;

    queue[tail++] = start;
    visited[start] = true;
    int maxDist = 0;

    while (head < tail) {
      int cur = queue[head++];
      for (int nb in adj[cur]) {
        if (!visited[nb]) {
          visited[nb] = true;
          dist[nb] = dist[cur] + 1;
          queue[tail++] = nb;
          if (dist[nb] > maxDist) maxDist = dist[nb];
        }
      }
    }
    return maxDist;
  }
}
```

## Golang

```go
func minimumDiameterAfterMerge(edges1 [][]int, edges2 [][]int) int {
	// helper to build adjacency list and node count
	build := func(edges [][]int) [][]int {
		maxNode := -1
		for _, e := range edges {
			if e[0] > maxNode {
				maxNode = e[0]
			}
			if e[1] > maxNode {
				maxNode = e[1]
			}
		}
		n := maxNode + 1
		if n == 0 { // tree with a single node
			n = 1
		}
		adj := make([][]int, n)
		for _, e := range edges {
			u, v := e[0], e[1]
			adj[u] = append(adj[u], v)
			adj[v] = append(adj[v], u)
		}
		return adj
	}

	bfs := func(start int, adj [][]int) (int, []int) {
		n := len(adj)
		dist := make([]int, n)
		for i := 0; i < n; i++ {
			dist[i] = -1
		}
		q := make([]int, 0, n)
		dist[start] = 0
		q = append(q, start)
		head := 0
		far := start
		for head < len(q) {
			u := q[head]
			head++
			for _, v := range adj[u] {
				if dist[v] == -1 {
					dist[v] = dist[u] + 1
					q = append(q, v)
					if dist[v] > dist[far] {
						far = v
					}
				}
			}
		}
		return far, dist
	}

	treeDiameter := func(adj [][]int) int {
		if len(adj) == 0 {
			return 0
		}
		f1, _ := bfs(0, adj)
		_, dist2 := bfs(f1, adj)
		maxd := 0
		for _, d := range dist2 {
			if d > maxd {
				maxd = d
			}
		}
		return maxd
	}

	adj1 := build(edges1)
	adj2 := build(edges2)

	d1 := treeDiameter(adj1)
	d2 := treeDiameter(adj2)

	combined := (d1+1)/2 + (d2+1)/2 + 1

	ans := d1
	if d2 > ans {
		ans = d2
	}
	if combined > ans {
		ans = combined
	}
	return ans
}
```

## Ruby

```ruby
def minimum_diameter_after_merge(edges1, edges2)
  # helper to determine number of nodes from edge list
  node_cnt = ->(edges) {
    return 1 if edges.empty?
    max_id = edges.flatten.max
    max_id + 1
  }

  build_adj = ->(n, edges) {
    adj = Array.new(n) { [] }
    edges.each do |u, v|
      adj[u] << v
      adj[v] << u
    end
    adj
  }

  bfs_farthest = ->(start, adj) {
    n = adj.size
    dist = Array.new(n, -1)
    queue = [start]
    head = 0
    dist[start] = 0
    far_node = start

    while head < queue.length
      u = queue[head]
      head += 1
      adj[u].each do |v|
        next if dist[v] != -1
        dist[v] = dist[u] + 1
        queue << v
        far_node = v if dist[v] > dist[far_node]
      end
    end
    [far_node, dist[far_node]]
  }

  tree_diameter = ->(adj) {
    # first bfs from any node (0)
    far1, _ = bfs_farthest.call(0, adj)
    _, diam = bfs_farthest.call(far1, adj)
    diam
  }

  n1 = node_cnt.call(edges1)
  n2 = node_cnt.call(edges2)

  adj1 = build_adj.call(n1, edges1)
  adj2 = build_adj.call(n2, edges2)

  d1 = tree_diameter.call(adj1)
  d2 = tree_diameter.call(adj2)

  combined = (d1 + 1) / 2 + (d2 + 1) / 2 + 1
  [d1, d2, combined].max
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.ArrayBuffer
  import java.util.ArrayDeque

  private def buildAdj(edges: Array[Array[Int]], n: Int): Array[ArrayBuffer[Int]] = {
    val adj = Array.fill(n)(new ArrayBuffer[Int]())
    var i = 0
    while (i < edges.length) {
      val a = edges(i)(0)
      val b = edges(i)(1)
      adj(a).append(b)
      adj(b).append(a)
      i += 1
    }
    adj
  }

  private def bfs(start: Int, adj: Array[ArrayBuffer[Int]]): (Int, Int) = {
    val n = adj.length
    val dist = Array.fill(n)(-1)
    val q = new ArrayDeque[Int]()
    dist(start) = 0
    q.add(start)
    var farNode = start

    while (!q.isEmpty) {
      val u = q.poll()
      val du = dist(u)
      val neighbors = adj(u)
      var idx = 0
      while (idx < neighbors.length) {
        val v = neighbors(idx)
        if (dist(v) == -1) {
          dist(v) = du + 1
          q.add(v)
          if (dist(v) > dist(farNode)) farNode = v
        }
        idx += 1
      }
    }
    (farNode, dist(farNode))
  }

  private def diameter(edges: Array[Array[Int]], n: Int): Int = {
    if (n == 0) return 0
    val adj = buildAdj(edges, n)
    val (u, _) = bfs(0, adj)
    val (_, d) = bfs(u, adj)
    d
  }

  private def ceilDiv(x: Int): Int = (x + 1) / 2

  def minimumDiameterAfterMerge(edges1: Array[Array[Int]], edges2: Array[Array[Int]]): Int = {
    val n = edges1.length + 1
    val m = edges2.length + 1

    val d1 = diameter(edges1, n)
    val d2 = diameter(edges2, m)

    val combined = ceilDiv(d1) + ceilDiv(d2) + 1
    math.max(d1, math.max(d2, combined))
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn minimum_diameter_after_merge(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>) -> i32 {
        // Helper to build adjacency list
        fn build_adj(size: usize, edges: Vec<Vec<i32>>) -> Vec<Vec<usize>> {
            let mut adj = vec![Vec::new(); size];
            for e in edges {
                let a = e[0] as usize;
                let b = e[1] as usize;
                adj[a].push(b);
                adj[b].push(a);
            }
            adj
        }

        // BFS to find farthest node and its distance from start
        fn bfs(start: usize, adj: &Vec<Vec<usize>>) -> (usize, i32) {
            let n = adj.len();
            let mut dist = vec![-1i32; n];
            let mut q = VecDeque::new();
            dist[start] = 0;
            q.push_back(start);
            let mut far_node = start;

            while let Some(u) = q.pop_front() {
                for &v in &adj[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                        if dist[v] > dist[far_node] {
                            far_node = v;
                        }
                    }
                }
            }
            (far_node, dist[far_node])
        }

        // Compute diameter of a tree given its adjacency list
        fn diameter(adj: &Vec<Vec<usize>>) -> i32 {
            if adj.is_empty() {
                return 0;
            }
            let (a, _) = bfs(0, adj);
            let (_, d) = bfs(a, adj);
            d
        }

        // Sizes of the trees
        let n = edges1.len() + 1;
        let m = edges2.len() + 1;

        // Build adjacency lists
        let adj1 = build_adj(n, edges1);
        let adj2 = build_adj(m, edges2);

        // Diameters
        let d1 = diameter(&adj1);
        let d2 = diameter(&adj2);

        // Combined diameter when connecting optimal centers
        let half1 = (d1 + 1) / 2; // ceil(d1/2)
        let half2 = (d2 + 1) / 2; // ceil(d2/2)
        let combined = half1 + half2 + 1;

        *[d1, d2, combined].iter().max().unwrap()
    }
}
```

## Racket

```racket
(define (ceil-half d)
  (quotient (+ d 1) 2))

(define (build-adj edges size)
  (let ([adj (make-vector size '())])
    (for ([e edges])
      (define a (first e))
      (define b (second e))
      (vector-set! adj a (cons b (vector-ref adj a)))
      (vector-set! adj b (cons a (vector-ref adj b))))
    adj))

(define (bfs-farthest adj start)
  (let* ([n (vector-length adj)]
         [visited (make-vector n #f)]
         [dist (make-vector n -1)]
         [queue (make-vector n 0)]
         [head 0]
         [tail 0])
    (vector-set! visited start #t)
    (vector-set! dist start 0)
    (vector-set! queue tail start)
    (set! tail (+ tail 1))
    (let loop ()
      (when (< head tail)
        (define u (vector-ref queue head))
        (set! head (+ head 1))
        (for ([v (vector-ref adj u)])
          (unless (vector-ref visited v)
            (vector-set! visited v #t)
            (vector-set! dist v (+ (vector-ref dist u) 1))
            (vector-set! queue tail v)
            (set! tail (+ tail 1))))
        (loop)))
    (let ([max-node start]
          [max-dist 0])
      (for ([i (in-range n)])
        (when (> (vector-ref dist i) max-dist)
          (set! max-dist (vector-ref dist i))
          (set! max-node i)))
      (values max-node max-dist))))

(define (tree-diameter adj)
  (if (= (vector-length adj) 1)
      0
      (let-values ([(far _) (bfs-farthest adj 0)])
        (let-values ([_ diam] (bfs-farthest adj far))
          diam))))

(define/contract (minimum-diameter-after-merge edges1 edges2)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (+ 1 (length edges1))]
         [m (+ 1 (length edges2))]
         [adj1 (build-adj edges1 n)]
         [adj2 (build-adj edges2 m)]
         [d1 (tree-diameter adj1)]
         [d2 (tree-diameter adj2)]
         [combined (+ (ceil-half d1) (ceil-half d2) 1)])
    (max d1 d2 combined)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_diameter_after_merge/2]).

-spec minimum_diameter_after_merge(Edges1 :: [[integer()]], Edges2 :: [[integer()]]) -> integer().
minimum_diameter_after_merge(Edges1, Edges2) ->
    N1 = length(Edges1) + 1,
    N2 = length(Edges2) + 1,
    Adj1 = build_adj(N1, Edges1),
    Adj2 = build_adj(N2, Edges2),
    D1 = tree_diameter(Adj1, N1),
    D2 = tree_diameter(Adj2, N2),
    Half1 = (D1 + 1) div 2,
    Half2 = (D2 + 1) div 2,
    Combined = Half1 + Half2 + 1,
    Max12 = max(D1, D2),
    max(Max12, Combined).

build_adj(_N, Edges) ->
    lists:foldl(fun([U,V], Acc) ->
        Acc1 = maps:update_with(U,
                fun(L) -> [V|L] end,
                [V],
                Acc),
        maps:update_with(V,
            fun(L) -> [U|L] end,
            [U],
            Acc1)
    end, #{}, Edges).

tree_diameter(Adj, N) ->
    case N of
        0 -> 0;
        _ ->
            {Farthest,_} = bfs(N, Adj, 0),
            {_ , D}= bfs(N, Adj, Farthest),
            D
    end.

bfs(_N, Adj, Start) ->
    Q0 = queue:new(),
    Q1 = queue:in({Start,0}, Q0),
    DistMap0 = maps:put(Start, 0, #{}),
    bfs_loop(Q1, Adj, DistMap0, Start, 0).

bfs_loop(Queue, Adj, DistMap, MaxNode, MaxDist) ->
    case queue:out(Queue) of
        {empty, _} -> {MaxNode, MaxDist};
        {{value,{Node,Dist}}, QRest} ->
            Neighs = maps:get(Node, Adj, []),
            {NewQ, NewDM, NewMNode, NewMDist} =
                lists:foldl(fun(Neighbor, {QAcc, DMAcc, MNode, MDist}) ->
                    case maps:is_key(Neighbor, DMAcc) of
                        true -> {QAcc, DMAcc, MNode, MDist};
                        false ->
                            D1 = Dist + 1,
                            Q2 = queue:in({Neighbor,D1}, QAcc),
                            DM2 = maps:put(Neighbor, D1, DMAcc),
                            if D1 > MDist -> {Q2, DM2, Neighbor, D1}
                               true -> {Q2, DM2, MNode, MDist}
                            end
                    end
                end,
                {QRest, DistMap, MaxNode, MaxDist},
                Neighs),
            bfs_loop(NewQ, Adj, NewDM, NewMNode, NewMDist)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_diameter_after_merge(edges1 :: [[integer]], edges2 :: [[integer]]) :: integer
  def minimum_diameter_after_merge(edges1, edges2) do
    n = length(edges1) + 1
    m = length(edges2) + 1

    adj1 = build_adj(edges1)
    adj2 = build_adj(edges2)

    d1 = tree_diameter(adj1, n)
    d2 = tree_diameter(adj2, m)

    half1 = div(d1 + 1, 2)
    half2 = div(d2 + 1, 2)
    combined = half1 + half2 + 1

    Enum.max([d1, d2, combined])
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)
  end

  defp tree_diameter(adj, n) do
    {far_node, _} = bfs_farthest(0, adj, n)
    {_node, diameter} = bfs_farthest(far_node, adj, n)
    diameter
  end

  defp bfs_farthest(start, adj, _n) do
    queue = :queue.in(start, :queue.new())
    distances = %{start => 0}
    bfs_loop(queue, distances, start, 0, adj)
  end

  defp bfs_loop(queue, dist_map, far_node, max_dist, adj) do
    case :queue.out(queue) do
      {:empty, _} ->
        {far_node, max_dist}

      {{:value, node}, q2} ->
        d = Map.get(dist_map, node)

        {new_far, new_max} =
          if d > max_dist do
            {node, d}
          else
            {far_node, max_dist}
          end

        neighbors = Map.get(adj, node, [])

        {next_queue, next_dist} =
          Enum.reduce(neighbors, {q2, dist_map}, fn nb, {q_acc, dm} ->
            if Map.has_key?(dm, nb) do
              {q_acc, dm}
            else
              {
                :queue.in(nb, q_acc),
                Map.put(dm, nb, d + 1)
              }
            end
          end)

        bfs_loop(next_queue, next_dist, new_far, new_max, adj)
    end
  end
end
```

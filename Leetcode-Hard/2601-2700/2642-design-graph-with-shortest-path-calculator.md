# 2642. Design Graph With Shortest Path Calculator

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Graph {
public:
    int n;
    vector<vector<pair<int,int>>> adj;
    const long long INF = 4e18;
    
    Graph(int n, vector<vector<int>>& edges) : n(n), adj(n) {
        for (const auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
        }
    }
    
    void addEdge(vector<int> edge) {
        int u = edge[0], v = edge[1], w = edge[2];
        adj[u].push_back({v, w});
    }
    
    int shortestPath(int node1, int node2) {
        if (node1 == node2) return 0;
        vector<long long> dist(n, INF);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        dist[node1] = 0;
        pq.push({0, node1});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            if (u == node2) return (int)d;
            for (auto& [v, w] : adj[u]) {
                long long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        return -1;
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */
```

## Java

```java
class Graph {
    private final int n;
    private final java.util.List<int[]>[] adj;

    @SuppressWarnings("unchecked")
    public Graph(int n, int[][] edges) {
        this.n = n;
        adj = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new java.util.ArrayList<>();
        }
        for (int[] e : edges) {
            addEdge(e);
        }
    }

    public void addEdge(int[] edge) {
        int from = edge[0];
        int to = edge[1];
        int cost = edge[2];
        adj[from].add(new int[]{to, cost});
    }

    public int shortestPath(int node1, int node2) {
        long INF = Long.MAX_VALUE / 4;
        long[] dist = new long[n];
        java.util.Arrays.fill(dist, INF);
        dist[node1] = 0;
        java.util.PriorityQueue<long[]> pq = new java.util.PriorityQueue<>(
                (a, b) -> Long.compare(a[0], b[0])
        );
        pq.offer(new long[]{0L, node1});
        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int u = (int) cur[1];
            if (d != dist[u]) continue;
            if (u == node2) return (int) d;
            for (int[] e : adj[u]) {
                int v = e[0];
                int w = e[1];
                long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.offer(new long[]{nd, v});
                }
            }
        }
        return -1;
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = new Graph(n, edges);
 * obj.addEdge(edge);
 * int param_2 = obj.shortestPath(node1,node2);
 */
```

## Python

```python
class Graph(object):
    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        import heapq

        INF = 10**18
        dist = [INF] * self.n
        dist[node1] = 0
        heap = [(0, node1)]

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            if u == node2:
                return d
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        return -1 if dist[node2] == INF else dist[node2]
```

## Python3

```python
from typing import List
import heapq

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        INF = 10**18
        dist = [INF] * self.n
        dist[node1] = 0
        heap = [(0, node1)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            if u == node2:
                return d
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        return -1
```

## C

```c
typedef struct {
    int n;
    long long **dist;
} Graph;

static const long long INF = (long long)4e15;

Graph* graphCreate(int n, int** edges, int edgesSize, int* edgesColSize) {
    Graph *obj = (Graph*)malloc(sizeof(Graph));
    obj->n = n;
    obj->dist = (long long**)malloc(n * sizeof(long long*));
    for (int i = 0; i < n; ++i) {
        obj->dist[i] = (long long*)malloc(n * sizeof(long long));
        for (int j = 0; j < n; ++j) {
            obj->dist[i][j] = (i == j) ? 0 : INF;
        }
    }
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];
        if ((long long)w < obj->dist[u][v]) {
            obj->dist[u][v] = w;
        }
    }
    // Floyd‑Warshall
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            if (obj->dist[i][k] == INF) continue;
            for (int j = 0; j < n; ++j) {
                if (obj->dist[k][j] == INF) continue;
                long long nd = obj->dist[i][k] + obj->dist[k][j];
                if (nd < obj->dist[i][j]) {
                    obj->dist[i][j] = nd;
                }
            }
        }
    }
    return obj;
}

void graphAddEdge(Graph* obj, int* edge, int edgeSize) {
    int u = edge[0];
    int v = edge[1];
    long long w = edge[2];
    if (w >= obj->dist[u][v]) {
        // no improvement on direct edge; still may improve via other paths,
        // but such improvement would require a shorter direct edge, so skip.
        return;
    }
    obj->dist[u][v] = w;
    int n = obj->n;
    for (int i = 0; i < n; ++i) {
        if (obj->dist[i][u] == INF) continue;
        long long iu = obj->dist[i][u];
        for (int j = 0; j < n; ++j) {
            if (obj->dist[v][j] == INF) continue;
            long long vj = obj->dist[v][j];
            long long nd = iu + w + vj;
            if (nd < obj->dist[i][j]) {
                obj->dist[i][j] = nd;
            }
        }
    }
}

int graphShortestPath(Graph* obj, int node1, int node2) {
    long long d = obj->dist[node1][node2];
    return (d >= INF/2) ? -1 : (int)d;
}

void graphFree(Graph* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->n; ++i) {
        free(obj->dist[i]);
    }
    free(obj->dist);
    free(obj);
}
```

## Csharp

```csharp
public class Graph
{
    private readonly int _n;
    private long[,] _dist;
    private const long INF = 1L << 60;

    public Graph(int n, int[][] edges)
    {
        _n = n;
        _dist = new long[n, n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                _dist[i, j] = i == j ? 0 : INF;

        foreach (var e in edges)
        {
            int u = e[0], v = e[1];
            long w = e[2];
            if (w < _dist[u, v]) _dist[u, v] = w;
        }

        FloydWarshall();
    }

    private void FloydWarshall()
    {
        for (int k = 0; k < _n; k++)
        {
            for (int i = 0; i < _n; i++)
            {
                if (_dist[i, k] == INF) continue;
                for (int j = 0; j < _n; j++)
                {
                    if (_dist[k, j] == INF) continue;
                    long nd = _dist[i, k] + _dist[k, j];
                    if (nd < _dist[i, j]) _dist[i, j] = nd;
                }
            }
        }
    }

    public void AddEdge(int[] edge)
    {
        int u = edge[0], v = edge[1];
        long w = edge[2];
        if (w < _dist[u, v])
        {
            _dist[u, v] = w;
            FloydWarshall();
        }
    }

    public int ShortestPath(int node1, int node2)
    {
        long d = _dist[node1, node2];
        return d == INF ? -1 : (int)d;
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = new Graph(n, edges);
 * obj.AddEdge(edge);
 * int param_2 = obj.ShortestPath(node1,node2);
 */
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 */
var Graph = function(n, edges) {
    this.n = n;
    this.adj = Array.from({ length: n }, () => []);
    for (const [from, to, cost] of edges) {
        this.adj[from].push([to, cost]);
    }
};

/** 
 * @param {number[]} edge
 * @return {void}
 */
Graph.prototype.addEdge = function(edge) {
    const [from, to, cost] = edge;
    this.adj[from].push([to, cost]);
};

/**
 * Min-heap for pairs [distance, node]
 */
class MinHeap {
    constructor() {
        this.heap = [];
    }
    size() {
        return this.heap.length;
    }
    push(val) {
        const h = this.heap;
        h.push(val);
        let i = h.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (h[p][0] <= h[i][0]) break;
            [h[p], h[i]] = [h[i], h[p]];
            i = p;
        }
    }
    pop() {
        const h = this.heap;
        if (h.length === 0) return null;
        const top = h[0];
        const last = h.pop();
        if (h.length > 0) {
            h[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1,
                    r = l + 1,
                    smallest = i;
                if (l < h.length && h[l][0] < h[smallest][0]) smallest = l;
                if (r < h.length && h[r][0] < h[smallest][0]) smallest = r;
                if (smallest === i) break;
                [h[i], h[smallest]] = [h[smallest], h[i]];
                i = smallest;
            }
        }
        return top;
    }
}

/** 
 * @param {number} node1 
 * @param {number} node2
 * @return {number}
 */
Graph.prototype.shortestPath = function(node1, node2) {
    if (node1 === node2) return 0;
    const dist = new Array(this.n).fill(Infinity);
    dist[node1] = 0;
    const heap = new MinHeap();
    heap.push([0, node1]);
    while (heap.size() > 0) {
        const [d, u] = heap.pop();
        if (d !== dist[u]) continue;
        if (u === node2) return d;
        for (const [v, w] of this.adj[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                heap.push([nd, v]);
            }
        }
    }
    return -1;
};

/** 
 * Your Graph object will be instantiated and called as such:
 * var obj = new Graph(n, edges)
 * obj.addEdge(edge)
 * var param_2 = obj.shortestPath(node1,node2)
 */
```

## Typescript

```typescript
class MinHeap {
    private data: [number, number][] = [];

    isEmpty(): boolean {
        return this.data.length === 0;
    }

    push(item: [number, number]): void {
        this.data.push(item);
        this.bubbleUp(this.data.length - 1);
    }

    pop(): [number, number] | undefined {
        if (this.data.length === 0) return undefined;
        const top = this.data[0];
        const end = this.data.pop()!;
        if (this.data.length > 0) {
            this.data[0] = end;
            this.sinkDown(0);
        }
        return top;
    }

    private bubbleUp(idx: number): void {
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (this.data[parent][0] <= this.data[idx][0]) break;
            [this.data[parent], this.data[idx]] = [this.data[idx], this.data[parent]];
            idx = parent;
        }
    }

    private sinkDown(idx: number): void {
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
}

class Graph {
    private n: number;
    private adj: [number, number][][]; // adjacency list: [to, cost]

    constructor(n: number, edges: number[][]) {
        this.n = n;
        this.adj = Array.from({ length: n }, () => [] as [number, number][]);
        for (const e of edges) {
            const [from, to, cost] = e;
            this.adj[from].push([to, cost]);
        }
    }

    addEdge(edge: number[]): void {
        const [from, to, cost] = edge;
        this.adj[from].push([to, cost]);
    }

    shortestPath(node1: number, node2: number): number {
        const INF = Number.MAX_SAFE_INTEGER;
        const dist = new Array(this.n).fill(INF);
        dist[node1] = 0;

        const heap = new MinHeap();
        heap.push([0, node1]);

        while (!heap.isEmpty()) {
            const cur = heap.pop()!;
            const d = cur[0];
            const u = cur[1];

            if (d !== dist[u]) continue;
            if (u === node2) return d;

            for (const [v, w] of this.adj[u]) {
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    heap.push([nd, v]);
                }
            }
        }

        return -1;
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * var obj = new Graph(n, edges)
 * obj.addEdge(edge)
 * var param_2 = obj.shortestPath(node1,node2)
 */
```

## Php

```php
class Graph {
    private $n;
    private $adj;

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     */
    public function __construct($n, $edges) {
        $this->n = $n;
        $this->adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $from = $e[0];
            $to   = $e[1];
            $cost = $e[2];
            $this->adj[$from][] = [$to, $cost];
        }
    }

    /**
     * @param Integer[] $edge
     * @return NULL
     */
    public function addEdge($edge) {
        $from = $edge[0];
        $to   = $edge[1];
        $cost = $edge[2];
        $this->adj[$from][] = [$to, $cost];
    }

    /**
     * @param Integer $node1
     * @param Integer $node2
     * @return Integer
     */
    public function shortestPath($node1, $node2) {
        $INF  = PHP_INT_MAX;
        $dist = array_fill(0, $this->n, $INF);
        $dist[$node1] = 0;

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        // priority is negative distance because SplPriorityQueue extracts max priority
        $pq->insert([$node1, 0], 0);

        while (!$pq->isEmpty()) {
            $cur = $pq->extract(); // [$u, $d]
            $u   = $cur[0];
            $d   = $cur[1];

            if ($d != $dist[$u]) {
                continue; // stale entry
            }
            if ($u === $node2) {
                return $d;
            }

            foreach ($this->adj[$u] as $edge) {
                $v        = $edge[0];
                $weight   = $edge[1];
                $newDist  = $d + $weight;
                if ($newDist < $dist[$v]) {
                    $dist[$v] = $newDist;
                    $pq->insert([$v, $newDist], -$newDist);
                }
            }
        }

        return -1;
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * $obj = new Graph($n, $edges);
 * $obj->addEdge($edge);
 * $ret_2 = $obj->shortestPath($node1, $node2);
 */
```

## Swift

```swift
class Graph {
    private var adj: [[(to: Int, cost: Int)]]

    init(_ n: Int, _ edges: [[Int]]) {
        adj = Array(repeating: [], count: n)
        for e in edges {
            let from = e[0]
            let to = e[1]
            let cost = e[2]
            adj[from].append((to, cost))
        }
    }

    func addEdge(_ edge: [Int]) {
        let from = edge[0]
        let to = edge[1]
        let cost = edge[2]
        adj[from].append((to, cost))
    }

    func shortestPath(_ node1: Int, _ node2: Int) -> Int {
        if node1 == node2 { return 0 }
        let n = adj.count
        let INF = Int.max / 4
        var dist = Array(repeating: INF, count: n)
        var visited = Array(repeating: false, count: n)
        dist[node1] = 0

        for _ in 0..<n {
            var u = -1
            var best = INF
            for i in 0..<n where !visited[i] && dist[i] < best {
                best = dist[i]
                u = i
            }
            if u == -1 { break }
            if u == node2 { return dist[u] }
            visited[u] = true
            for edge in adj[u] {
                let v = edge.to
                let w = edge.cost
                if !visited[v] && dist[u] + w < dist[v] {
                    dist[v] = dist[u] + w
                }
            }
        }

        return dist[node2] == INF ? -1 : dist[node2]
    }
}
```

## Kotlin

```kotlin
class Graph(n: Int, edges: Array<IntArray>) {
    private val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }

    init {
        for (e in edges) {
            addEdgeInternal(e[0], e[1], e[2])
        }
    }

    private fun addEdgeInternal(u: Int, v: Int, w: Int) {
        adj[u].add(Pair(v, w))
    }

    fun addEdge(edge: IntArray) {
        addEdgeInternal(edge[0], edge[1], edge[2])
    }

    fun shortestPath(node1: Int, node2: Int): Int {
        val INF = Long.MAX_VALUE / 4
        val dist = LongArray(adj.size) { INF }
        val pq = java.util.PriorityQueue<Pair<Long, Int>>(compareBy { it.first })
        dist[node1] = 0L
        pq.offer(Pair(0L, node1))
        while (pq.isNotEmpty()) {
            val (d, u) = pq.poll()
            if (d != dist[u]) continue
            if (u == node2) return d.toInt()
            for ((v, w) in adj[u]) {
                val nd = d + w
                if (nd < dist[v]) {
                    dist[v] = nd
                    pq.offer(Pair(nd, v))
                }
            }
        }
        return -1
    }
}

/**
 * Your Graph object will be instantiated and called as such:
 * var obj = Graph(n, edges)
 * obj.addEdge(edge)
 * var param_2 = obj.shortestPath(node1,node2)
 */
```

## Dart

```dart
class _Edge {
  final int to;
  final int w;
  _Edge(this.to, this.w);
}

class Graph {
  int n;
  late List<List<_Edge>> adj;

  Graph(this.n, List<List<int>> edges) {
    adj = List.generate(n, (_) => []);
    for (var e in edges) {
      addEdge(e);
    }
  }

  void addEdge(List<int> edge) {
    int from = edge[0];
    int to = edge[1];
    int w = edge[2];
    adj[from].add(_Edge(to, w));
  }

  int shortestPath(int node1, int node2) {
    const int INF = 1 << 60;
    List<int> dist = List.filled(n, INF);
    List<bool> visited = List.filled(n, false);
    dist[node1] = 0;

    for (int i = 0; i < n; i++) {
      int u = -1;
      int best = INF;
      for (int v = 0; v < n; v++) {
        if (!visited[v] && dist[v] < best) {
          best = dist[v];
          u = v;
        }
      }
      if (u == -1) break;
      if (u == node2) return dist[u];
      visited[u] = true;
      for (var e in adj[u]) {
        int v = e.to;
        int w = e.w;
        if (!visited[v] && dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
        }
      }
    }

    return dist[node2] == INF ? -1 : dist[node2];
  }
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = Graph(n, edges);
 * obj.addEdge(edge);
 * int param2 = obj.shortestPath(node1,node2);
 */
```

## Golang

```go
type Graph struct {
	n    int
	dist [][]int64
}

const INF int64 = 1 << 60

func Constructor(n int, edges [][]int) Graph {
	dist := make([][]int64, n)
	for i := 0; i < n; i++ {
		row := make([]int64, n)
		for j := 0; j < n; j++ {
			if i == j {
				row[j] = 0
			} else {
				row[j] = INF
			}
		}
		dist[i] = row
	}
	for _, e := range edges {
		u, v, w := e[0], e[1], int64(e[2])
		if w < dist[u][v] {
			dist[u][v] = w
		}
	}
	g := Graph{n: n, dist: dist}
	g.floyd()
	return g
}

func (g *Graph) AddEdge(edge []int) {
	u, v, w := edge[0], edge[1], int64(edge[2])
	if w < g.dist[u][v] {
		g.dist[u][v] = w
	}
	g.floyd()
}

func (g *Graph) ShortestPath(node1 int, node2 int) int {
	if g.dist[node1][node2] == INF {
		return -1
	}
	return int(g.dist[node1][node2])
}

func (g *Graph) floyd() {
	n := g.n
	d := g.dist
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			if d[i][k] == INF {
				continue
			}
			for j := 0; j < n; j++ {
				if d[k][j] == INF {
					continue
				}
				if nd := d[i][k] + d[k][j]; nd < d[i][j] {
					d[i][j] = nd
				}
			}
		}
	}
}

/**
 * Your Graph object will be instantiated and called as such:
 * obj := Constructor(n, edges);
 * obj.AddEdge(edge);
 * param_2 := obj.ShortestPath(node1,node2);
 */
```

## Ruby

```ruby
class Graph
  INF = (1 << 60)

  def initialize(n, edges)
    @n = n
    @dist = Array.new(n) { Array.new(n, INF) }
    n.times { |i| @dist[i][i] = 0 }
    edges.each do |e|
      u, v, w = e
      @dist[u][v] = w if w < @dist[u][v]
    end
    (0...n).each do |k|
      (0...n).each do |i|
        next if @dist[i][k] == INF
        (0...n).each do |j|
          nd = @dist[i][k] + @dist[k][j]
          @dist[i][j] = nd if nd < @dist[i][j]
        end
      end
    end
  end

  def add_edge(edge)
    u, v, w = edge
    return if w >= @dist[u][v]
    @dist[u][v] = w
    n = @n
    (0...n).each do |i|
      next if @dist[i][u] == INF
      (0...n).each do |j|
        next if @dist[v][j] == INF
        nd = @dist[i][u] + w + @dist[v][j]
        @dist[i][j] = nd if nd < @dist[i][j]
      end
    end
  end

  def shortest_path(node1, node2)
    d = @dist[node1][node2]
    d == INF ? -1 : d
  end
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer
import java.util.PriorityQueue

class Graph(_n: Int, _edges: Array[Array[Int]]) {

  private val n: Int = _n
  private val adj: Array[ArrayBuffer[(Int, Int)]] = Array.fill(n)(ArrayBuffer.empty[(Int, Int)])

  // initialize edges
  {
    var i = 0
    while (i < _edges.length) {
      val e = _edges(i)
      val from = e(0)
      val to = e(1)
      val cost = e(2)
      adj(from).append((to, cost))
      i += 1
    }
  }

  def addEdge(edge: Array[Int]): Unit = {
    val from = edge(0)
    val to = edge(1)
    val cost = edge(2)
    adj(from).append((to, cost))
  }

  def shortestPath(node1: Int, node2: Int): Int = {
    if (node1 == node2) return 0
    val dist: Array[Long] = Array.fill(n)(Long.MaxValue)
    dist(node1) = 0L

    val pq = new PriorityQueue[(Long, Int)](new java.util.Comparator[(Long, Int)] {
      override def compare(o1: (Long, Int), o2: (Long, Int)): Int =
        java.lang.Long.compare(o1._1, o2._1)
    })
    pq.offer((0L, node1))

    while (!pq.isEmpty) {
      val cur = pq.poll()
      val d = cur._1
      val u = cur._2

      if (d != dist(u)) {
        // outdated entry
      } else {
        if (u == node2) return d.toInt
        val neighbors = adj(u)
        var idx = 0
        while (idx < neighbors.length) {
          val (v, w) = neighbors(idx)
          val nd = d + w
          if (nd < dist(v)) {
            dist(v) = nd
            pq.offer((nd, v))
          }
          idx += 1
        }
      }
    }
    -1
  }

}

/**
 * Your Graph object will be instantiated and called as such:
 * val obj = new Graph(n, edges)
 * obj.addEdge(edge)
 * val param_2 = obj.shortestPath(node1,node2)
 */
```

## Rust

```rust
use std::i64;

const INF: i64 = 1_i64 << 60;

pub struct Graph {
    n: usize,
    dist: Vec<Vec<i64>>,
}

impl Graph {
    pub fn new(n: i32, edges: Vec<Vec<i32>>) -> Self {
        let n_usize = n as usize;
        let mut dist = vec![vec![INF; n_usize]; n_usize];
        for i in 0..n_usize {
            dist[i][i] = 0;
        }
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as i64;
            if w < dist[u][v] {
                dist[u][v] = w;
            }
        }
        // Floyd‑Warshall to compute all‑pairs shortest paths
        for k in 0..n_usize {
            for i in 0..n_usize {
                if dist[i][k] == INF { continue; }
                for j in 0..n_usize {
                    if dist[k][j] == INF { continue; }
                    let nd = dist[i][k] + dist[k][j];
                    if nd < dist[i][j] {
                        dist[i][j] = nd;
                    }
                }
            }
        }
        Graph { n: n_usize, dist }
    }

    pub fn add_edge(&mut self, edge: Vec<i32>) {
        let u = edge[0] as usize;
        let v = edge[1] as usize;
        let w = edge[2] as i64;
        if w < self.dist[u][v] {
            self.dist[u][v] = w;
        }
        // Relax paths that may use the new edge once
        for i in 0..self.n {
            if self.dist[i][u] == INF { continue; }
            let iu = self.dist[i][u];
            for j in 0..self.n {
                if self.dist[v][j] == INF { continue; }
                let nd = iu + w + self.dist[v][j];
                if nd < self.dist[i][j] {
                    self.dist[i][j] = nd;
                }
            }
        }
    }

    pub fn shortest_path(&self, node1: i32, node2: i32) -> i32 {
        let u = node1 as usize;
        let v = node2 as usize;
        if self.dist[u][v] >= INF / 2 {
            -1
        } else {
            self.dist[u][v] as i32
        }
    }
}

/*
Your Graph object will be instantiated and called as such:
let obj = Graph::new(n, edges);
obj.add_edge(edge);
let ret: i32 = obj.shortest_path(node1, node2);
*/
```

## Racket

```racket
#lang racket

(define graph%
  (class object%
    (init-field n edges)
    (field adj)

    (super-new)

    ;; initialize adjacency list
    (set! adj (make-vector n '()))
    (for ([e edges])
      (let* ([from (list-ref e 0)]
             [to   (list-ref e 1)]
             [cost (list-ref e 2)])
        (vector-set! adj from
                     (cons (cons to cost) (vector-ref adj from)))))

    ;; add a new edge
    (define/public (add-edge edge)
      (let* ([from (list-ref edge 0)]
             [to   (list-ref edge 1)]
             [cost (list-ref edge 2)])
        (vector-set! adj from
                     (cons (cons to cost) (vector-ref adj from)))))

    ;; Dijkstra with O(V^2) since V ≤ 100
    (define/public (shortest-path node1 node2)
      (if (= node1 node2)
          0
          (let* ([INF (+ (* n 1000000) 5)]
                 [dist (make-vector n INF)]
                 [visited (make-vector n #f)])
            (vector-set! dist node1 0)

            (let loop ()
              (define u -1)
              (define min-dist INF)
              (for ([v (in-range n)])
                (when (and (not (vector-ref visited v))
                           (< (vector-ref dist v) min-dist))
                  (set! min-dist (vector-ref dist v))
                  (set! u v)))
              (if (= u -1)
                  (void)
                  (begin
                    (vector-set! visited u #t)
                    (for ([edge (vector-ref adj u)])
                      (let* ([v (car edge)]
                             [w (cdr edge)]
                             [new (+ (vector-ref dist u) w)])
                        (when (< new (vector-ref dist v))
                          (vector-set! dist v new))))
                    (loop))))

            (define ans (vector-ref dist node2))
            (if (= ans INF) -1 ans)))))
```

## Erlang

```erlang
-spec graph_init_(N :: integer(), Edges :: [[integer()]]) -> any().
graph_init_(N, Edges) ->
    Adj0 = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    Adj = lists:foldl(fun([From, To, Cost], Acc) ->
                update_adj(Acc, From, {To, Cost})
            end, Adj0, Edges),
    put(graph_n, N),
    put(graph_adj, Adj).

-spec graph_add_edge(Edge :: [integer()]) -> any().
graph_add_edge([From, To, Cost]) ->
    Adj = get(graph_adj),
    NewAdj = update_adj(Adj, From, {To, Cost}),
    put(graph_adj, NewAdj).

-spec graph_shortest_path(Node1 :: integer(), Node2 :: integer()) -> integer().
graph_shortest_path(Node1, Node2) ->
    N = get(graph_n),
    Adj = get(graph_adj),
    Inf = 1 bsl 60,
    Dist0 = maps:from_list([{I, Inf} || I <- lists:seq(0, N - 1)]),
    Dist1 = maps:put(Node1, 0, Dist0),
    dijkstra(Adj, Dist1, [{0, Node1}], Node2).

%% internal helpers
update_adj(Map, From, Edge) ->
    List = maps:get(From, Map, []),
    maps:put(From, [Edge | List], Map).

dijkstra(_Adj, Dist, [], Target) ->
    case maps:get(Target, Dist) of
        Inf when Inf > 0 -> -1;
        D -> D
    end;
dijkstra(Adj, Dist, Queue, Target) ->
    {CurrCost, CurrNode, RestQueue} = select_min(Queue),
    if CurrNode =:= Target ->
            CurrCost;
       true ->
            Neighs = maps:get(CurrNode, Adj, []),
            {NewDist, NewQueue} = lists:foldl(
                fun({To, W}, {DAcc, QAcc}) ->
                    Old = maps:get(To, DAcc),
                    NewC = CurrCost + W,
                    if NewC < Old ->
                            {maps:put(To, NewC, DAcc), [{NewC, To} | QAcc]};
                       true ->
                            {DAcc, QAcc}
                    end
                end,
                {Dist, RestQueue},
                Neighs),
            dijkstra(Adj, NewDist, NewQueue, Target)
    end.

select_min([{C, N} | Tail]) -> select_min(Tail, C, N, []).
select_min([], MinC, MinN, Acc) -> {MinC, MinN, lists:reverse(Acc)};
select_min([{C, N} | Tail], MinC, MinN, Acc) ->
    if C < MinC ->
            select_min(Tail, C, N, [{MinC, MinN} | Acc]);
       true ->
            select_min(Tail, MinC, MinN, [{C, N} | Acc])
    end.
```

## Elixir

```elixir
defmodule Graph do
  @inf 1_000_000_000_000

  @spec init_(n :: integer, edges :: [[integer]]) :: any
  def init_(n, edges) do
    adj =
      Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Enum.reduce(edges, fn [from, to, cost], a ->
        Map.update(a, from, [{to, cost}], fn list -> [{to, cost} | list] end)
      end)

    Process.put(:graph_state, %{n: n, adj: adj})
    :ok
  end

  @spec add_edge(edge :: [integer]) :: any
  def add_edge([from, to, cost] = _edge) do
    state = Process.get(:graph_state)
    new_adj = Map.update(state.adj, from, [{to, cost}], fn list -> [{to, cost} | list] end)
    Process.put(:graph_state, %{state | adj: new_adj})
    :ok
  end

  @spec shortest_path(node1 :: integer, node2 :: integer) :: integer
  def shortest_path(node1, node2) do
    state = Process.get(:graph_state)
    dist = dijkstra(state.n, state.adj, node1, node2)

    if dist == @inf, do: -1, else: dist
  end

  # Dijkstra without heap (n ≤ 100)
  defp dijkstra(n, adj, src, dst) do
    dist0 = for i <- 0..(n - 1), into: %{}, do: {i, @inf}
    dist = Map.put(dist0, src, 0)
    visited = MapSet.new()
    dijkstra_loop(adj, dst, dist, visited)
  end

  defp dijkstra_loop(_adj, _dst, dist, visited) do
    # find unvisited node with smallest distance
    {u, du} =
      Enum.reduce(dist, {nil, @inf}, fn {node, dval}, {min_node, min_dist} = acc ->
        if not MapSet.member?(visited, node) and dval < min_dist do
          {node, dval}
        else
          acc
        end
      end)

    cond do
      u == nil or du == @inf ->
        Map.get(dist, _dst, @inf)

      u == _dst ->
        du

      true ->
        visited = MapSet.put(visited, u)
        neighbors = Map.get(_adj, u, [])

        dist =
          Enum.reduce(neighbors, dist, fn {v, cost}, dacc ->
            if not MapSet.member?(visited, v) do
              nd = du + cost

              if nd < Map.get(dacc, v, @inf) do
                Map.put(dacc, v, nd)
              else
                dacc
              end
            else
              dacc
            end
          end)

        dijkstra_loop(_adj, _dst, dist, visited)
    end
  end
end
```

# 1976. Number of Ways to Arrive at Destination

## Cpp

```cpp
class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        const long long INF = LLONG_MAX / 4;
        const int MOD = 1'000'000'007;
        vector<vector<pair<int,long long>>> g(n);
        for (auto &r : roads) {
            int u = r[0], v = r[1];
            long long w = r[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }
        vector<long long> dist(n, INF);
        vector<int> ways(n, 0);
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        dist[0] = 0;
        ways[0] = 1;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [d,u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto &[v,w] : g[u]) {
                long long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    ways[v] = ways[u];
                    pq.push({nd, v});
                } else if (nd == dist[v]) {
                    ways[v] += ways[u];
                    if (ways[v] >= MOD) ways[v] -= MOD;
                }
            }
        }
        return ways[n-1];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int countPaths(int n, int[][] roads) {
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] r : roads) {
            int u = r[0], v = r[1], w = r[2];
            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        long[] ways = new long[n];
        dist[0] = 0;
        ways[0] = 1;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0L, 0});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long d = cur[0];
            int node = (int) cur[1];

            if (d != dist[node]) continue;

            for (int[] edge : graph[node]) {
                int nb = edge[0];
                int w = edge[1];
                long nd = d + w;

                if (nd < dist[nb]) {
                    dist[nb] = nd;
                    ways[nb] = ways[node];
                    pq.offer(new long[]{nd, nb});
                } else if (nd == dist[nb]) {
                    ways[nb] = (ways[nb] + ways[node]) % MOD;
                }
            }
        }

        return (int) (ways[n - 1] % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        import heapq
        MOD = 10**9 + 7

        graph = [[] for _ in range(n)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (distance, node)
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(heap, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1] % MOD
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (distance, node)
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(heap, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1] % MOD
```

## C

```c
#include <limits.h>
#include <stdlib.h>

#define MOD 1000000007

typedef struct {
    long long d;
    int v;
} HeapNode;

static void heapSwap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapNode *heap, int *size, long long d, int v) {
    int i = (*size)++;
    heap[i].d = d;
    heap[i].v = v;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].d <= heap[i].d) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static HeapNode heapPop(HeapNode *heap, int *size) {
    HeapNode top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= *size) break;
        int smallest = l;
        if (r < *size && heap[r].d < heap[l].d) smallest = r;
        if (heap[i].d <= heap[smallest].d) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

int countPaths(int n, int** roads, int roadsSize, int* roadsColSize){
    /* adjacency list */
    int maxEdges = roadsSize * 2;
    int *to = (int*)malloc(sizeof(int) * maxEdges);
    long long *weight = (long long*)malloc(sizeof(long long) * maxEdges);
    int *next = (int*)malloc(sizeof(int) * maxEdges);
    int *head = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) head[i] = -1;
    int edgeCnt = 0;
    for (int i = 0; i < roadsSize; ++i) {
        int u = roads[i][0];
        int v = roads[i][1];
        long long w = (long long)roads[i][2];
        to[edgeCnt] = v;
        weight[edgeCnt] = w;
        next[edgeCnt] = head[u];
        head[u] = edgeCnt++;
        to[edgeCnt] = u;
        weight[edgeCnt] = w;
        next[edgeCnt] = head[v];
        head[v] = edgeCnt++;
    }

    long long *dist = (long long*)malloc(sizeof(long long) * n);
    int *ways = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) {
        dist[i] = LLONG_MAX;
        ways[i] = 0;
    }
    dist[0] = 0;
    ways[0] = 1;

    int heapCap = maxEdges + n + 5;
    HeapNode *heap = (HeapNode*)malloc(sizeof(HeapNode) * heapCap);
    int heapSize = 0;
    heapPush(heap, &heapSize, 0LL, 0);

    while (heapSize > 0) {
        HeapNode cur = heapPop(heap, &heapSize);
        long long d = cur.d;
        int u = cur.v;
        if (d != dist[u]) continue; // outdated
        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            long long nd = d + weight[e];
            if (nd < dist[v]) {
                dist[v] = nd;
                ways[v] = ways[u];
                heapPush(heap, &heapSize, nd, v);
            } else if (nd == dist[v]) {
                int sum = ways[v] + ways[u];
                if (sum >= MOD) sum -= MOD;
                ways[v] = sum;
            }
        }
    }

    int result = ways[n-1];

    free(to);
    free(weight);
    free(next);
    free(head);
    free(dist);
    free(ways);
    free(heap);

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;
    
    public int CountPaths(int n, int[][] roads) {
        var graph = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var r in roads) {
            int u = r[0], v = r[1], w = r[2];
            graph[u].Add((v, w));
            graph[v].Add((u, w));
        }
        
        var dist = new long[n];
        var ways = new long[n];
        for (int i = 0; i < n; i++) {
            dist[i] = long.MaxValue;
            ways[i] = 0;
        }
        dist[0] = 0;
        ways[0] = 1;
        
        var pq = new PriorityQueue<int, long>();
        pq.Enqueue(0, 0);
        
        while (pq.Count > 0) {
            int u = pq.Dequeue();
            long d = dist[u];
            // Since we cannot directly get priority from Dequeue, we rely on stored dist array.
            if (d != dist[u]) continue; // outdated entry check not needed because we use current dist
            
            foreach (var (v, w) in graph[u]) {
                long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    ways[v] = ways[u];
                    pq.Enqueue(v, nd);
                } else if (nd == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        
        return (int)(ways[n - 1] % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var countPaths = function(n, roads) {
    const MOD = 1000000007;
    if (n === 1) return 1;

    // Build adjacency list
    const graph = Array.from({ length: n }, () => []);
    for (const [u, v, w] of roads) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }

    // Min-heap implementation
    class MinHeap {
        constructor() { this.heap = []; }
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
        size() { return this.heap.length; }
    }

    const dist = new Array(n).fill(Infinity);
    const ways = new Array(n).fill(0);
    dist[0] = 0;
    ways[0] = 1;

    const pq = new MinHeap();
    pq.push([0, 0]); // [distance, node]

    while (pq.size() > 0) {
        const [d, u] = pq.pop();
        if (d > dist[u]) continue; // outdated entry
        for (const [v, w] of graph[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                ways[v] = ways[u];
                pq.push([nd, v]);
            } else if (Math.abs(nd - dist[v]) < 1e-9) { // equal shortest distance
                ways[v] = (ways[v] + ways[u]) % MOD;
            }
        }
    }

    return ways[n - 1] % MOD;
};
```

## Typescript

```typescript
function countPaths(n: number, roads: number[][]): number {
    const MOD = 1_000_000_007;
    // Build adjacency list
    const graph: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [u, v, w] of roads) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }

    // Min-heap implementation
    class MinHeap {
        private heap: [number, number][] = [];
        size(): number { return this.heap.length; }
        push(item: [number, number]): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        private bubbleDown(idx: number): void {
            const length = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let smallest = idx;

                if (left < length && this.heap[left][0] < this.heap[smallest][0]) {
                    smallest = left;
                }
                if (right < length && this.heap[right][0] < this.heap[smallest][0]) {
                    smallest = right;
                }
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const dist: number[] = new Array(n).fill(Infinity);
    const ways: number[] = new Array(n).fill(0);
    dist[0] = 0;
    ways[0] = 1;

    const pq = new MinHeap();
    pq.push([0, 0]);

    while (pq.size() > 0) {
        const cur = pq.pop()!;
        const d = cur[0];
        const u = cur[1];
        if (d > dist[u]) continue; // outdated entry
        for (const [v, w] of graph[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                ways[v] = ways[u];
                pq.push([nd, v]);
            } else if (nd === dist[v]) {
                ways[v] = (ways[v] + ways[u]) % MOD;
            }
        }
    }

    return ways[n - 1] % MOD;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $roads
     * @return Integer
     */
    function countPaths($n, $roads) {
        $mod = 1000000007;
        // Build adjacency list
        $graph = array_fill(0, $n, []);
        foreach ($roads as $r) {
            $u = $r[0];
            $v = $r[1];
            $w = $r[2];
            $graph[$u][] = [$v, $w];
            $graph[$v][] = [$u, $w];
        }

        // Distance and ways arrays
        $dist = array_fill(0, $n, PHP_INT_MAX);
        $ways = array_fill(0, $n, 0);
        $dist[0] = 0;
        $ways[0] = 1;

        // Min-heap using SplPriorityQueue (store negative distance as priority)
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert(0, 0); // node 0 with priority 0 (i.e., -distance)

        while (!$pq->isEmpty()) {
            $item = $pq->extract();
            $u = $item['data'];
            $currDist = -$item['priority'];

            if ($currDist > $dist[$u]) {
                continue;
            }

            foreach ($graph[$u] as $edge) {
                [$v, $w] = $edge;
                $newDist = $dist[$u] + $w;
                if ($newDist < $dist[$v]) {
                    $dist[$v] = $newDist;
                    $ways[$v] = $ways[$u];
                    $pq->insert($v, -$newDist);
                } elseif ($newDist == $dist[$v]) {
                    $ways[$v] = ($ways[$v] + $ways[$u]) % $mod;
                }
            }
        }

        return $ways[$n - 1] % $mod;
    }
}
```

## Swift

```swift
import Foundation

struct NodeDist {
    var node: Int
    var dist: Int64
}

final class MinHeap {
    private var heap: [NodeDist] = []
    
    var isEmpty: Bool { heap.isEmpty }
    
    func push(_ element: NodeDist) {
        heap.append(element)
        siftUp(heap.count - 1)
    }
    
    func pop() -> NodeDist? {
        guard !heap.isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeLast()
        } else {
            let top = heap[0]
            heap[0] = heap.removeLast()
            siftDown(0)
            return top
        }
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if heap[child].dist < heap[parent].dist {
                heap.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < heap.count && heap[left].dist < heap[smallest].dist {
                smallest = left
            }
            if right < heap.count && heap[right].dist < heap[smallest].dist {
                smallest = right
            }
            if smallest == parent { break }
            heap.swapAt(parent, smallest)
            parent = smallest
        }
    }
}

class Solution {
    func countPaths(_ n: Int, _ roads: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        var graph = Array(repeating: [(to: Int, w: Int64)](), count: n)
        for r in roads {
            let u = r[0], v = r[1]
            let w = Int64(r[2])
            graph[u].append((v, w))
            graph[v].append((u, w))
        }
        
        var dist = Array(repeating: Int64.max, count: n)
        var ways = Array(repeating: 0, count: n)
        dist[0] = 0
        ways[0] = 1
        
        let heap = MinHeap()
        heap.push(NodeDist(node: 0, dist: 0))
        
        while !heap.isEmpty {
            guard let cur = heap.pop() else { break }
            let d = cur.dist
            let u = cur.node
            if d > dist[u] { continue }
            for edge in graph[u] {
                let v = edge.to
                let nd = d + edge.w
                if nd < dist[v] {
                    dist[v] = nd
                    ways[v] = ways[u]
                    heap.push(NodeDist(node: v, dist: nd))
                } else if nd == dist[v] {
                    var sum = ways[v] + ways[u]
                    if sum >= MOD { sum -= MOD }
                    ways[v] = sum
                }
            }
        }
        
        return ways[n - 1] % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    private const val MOD = 1_000_000_007L

    data class Edge(val to: Int, val w: Long)
    data class Node(val d: Long, val v: Int) : Comparable<Node> {
        override fun compareTo(other: Node): Int = d.compareTo(other.d)
    }

    fun countPaths(n: Int, roads: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<Edge>() }
        for (road in roads) {
            val u = road[0]
            val v = road[1]
            val w = road[2].toLong()
            graph[u].add(Edge(v, w))
            graph[v].add(Edge(u, w))
        }

        val dist = LongArray(n) { Long.MAX_VALUE }
        val ways = LongArray(n)
        dist[0] = 0L
        ways[0] = 1L

        val pq = java.util.PriorityQueue<Node>()
        pq.add(Node(0L, 0))

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.d != dist[cur.v]) continue
            for (e in graph[cur.v]) {
                val nd = cur.d + e.w
                if (nd < dist[e.to]) {
                    dist[e.to] = nd
                    ways[e.to] = ways[cur.v]
                    pq.add(Node(nd, e.to))
                } else if (nd == dist[e.to]) {
                    ways[e.to] = (ways[e.to] + ways[cur.v]) % MOD
                }
            }
        }

        return (ways[n - 1] % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countPaths(int n, List<List<int>> roads) {
    // Build adjacency list
    final List<List<List<int>>> graph =
        List.generate(n, (_) => <List<int>>[]);
    for (var r in roads) {
      int u = r[0], v = r[1], w = r[2];
      graph[u].add([v, w]);
      graph[v].add([u, w]);
    }

    // Distance and ways arrays
    const int INF = 1 << 60;
    List<int> dist = List.filled(n, INF);
    List<int> ways = List.filled(n, 0);
    dist[0] = 0;
    ways[0] = 1;

    // Min-heap for Dijkstra
    final _MinHeap heap = _MinHeap();
    heap.push(_Item(0, 0));

    while (!heap.isEmpty) {
      final _Item cur = heap.pop();
      int u = cur.node;
      int d = cur.dist;
      if (d > dist[u]) continue; // outdated entry

      for (var edge in graph[u]) {
        int v = edge[0];
        int w = edge[1];
        int nd = d + w;

        if (nd < dist[v]) {
          dist[v] = nd;
          ways[v] = ways[u];
          heap.push(_Item(v, nd));
        } else if (nd == dist[v]) {
          ways[v] += ways[u];
          if (ways[v] >= _mod) ways[v] -= _mod;
        }
      }
    }

    return ways[n - 1] % _mod;
  }
}

class _Item {
  final int node;
  final int dist;
  _Item(this.node, this.dist);
}

class _MinHeap {
  final List<_Item> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void push(_Item item) {
    _heap.add(item);
    _siftUp(_heap.length - 1);
  }

  _Item pop() {
    final top = _heap[0];
    final last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_heap[parent].dist <= _heap[idx].dist) break;
      final tmp = _heap[parent];
      _heap[parent] = _heap[idx];
      _heap[idx] = tmp;
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    int n = _heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _heap[left].dist < _heap[smallest].dist) {
        smallest = left;
      }
      if (right < n && _heap[right].dist < _heap[smallest].dist) {
        smallest = right;
      }
      if (smallest == idx) break;

      final tmp = _heap[idx];
      _heap[idx] = _heap[smallest];
      _heap[smallest] = tmp;
      idx = smallest;
    }
  }
}
```

## Golang

```go
import (
	"container/heap"
)

const MOD int64 = 1000000007
const INF int64 = 1 << 60

type Edge struct {
	to int
	w  int64
}

type Item struct {
	node int
	dist int64
}

type PriorityQueue []Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].dist < pq[j].dist }
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(Item))
}
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[:n-1]
	return it
}

func countPaths(n int, roads [][]int) int {
	graph := make([][]Edge, n)
	for _, r := range roads {
		u, v, t := r[0], r[1], int64(r[2])
		graph[u] = append(graph[u], Edge{v, t})
		graph[v] = append(graph[v], Edge{u, t})
	}

	dist := make([]int64, n)
	for i := 0; i < n; i++ {
		dist[i] = INF
	}
	ways := make([]int64, n)

	dist[0] = 0
	ways[0] = 1

	pq := &PriorityQueue{}
	heap.Push(pq, Item{node: 0, dist: 0})

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(Item)
		if cur.dist > dist[cur.node] {
			continue
		}
		for _, e := range graph[cur.node] {
			nd := cur.dist + e.w
			if nd < dist[e.to] {
				dist[e.to] = nd
				ways[e.to] = ways[cur.node]
				heap.Push(pq, Item{node: e.to, dist: nd})
			} else if nd == dist[e.to] {
				ways[e.to] = (ways[e.to] + ways[cur.node]) % MOD
			}
		}
	}

	return int(ways[n-1] % MOD)
}
```

## Ruby

```ruby
def heap_push(heap, item)
  heap << item
  i = heap.size - 1
  while i > 0
    p = (i - 1) / 2
    break if heap[p][0] <= heap[i][0]
    heap[p], heap[i] = heap[i], heap[p]
    i = p
  end
end

def heap_pop(heap)
  top = heap[0]
  last = heap.pop
  unless heap.empty?
    heap[0] = last
    i = 0
    size = heap.size
    loop do
      l = i * 2 + 1
      r = i * 2 + 2
      smallest = i
      smallest = l if l < size && heap[l][0] < heap[smallest][0]
      smallest = r if r < size && heap[r][0] < heap[smallest][0]
      break if smallest == i
      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
  end
  top
end

def count_paths(n, roads)
  mod = 1_000_000_007
  adj = Array.new(n) { [] }
  roads.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  inf = (1 << 60)
  dist = Array.new(n, inf)
  ways = Array.new(n, 0)
  dist[0] = 0
  ways[0] = 1

  heap = []
  heap_push(heap, [0, 0])

  until heap.empty?
    d, u = heap_pop(heap)
    next if d > dist[u]
    adj[u].each do |v, w|
      nd = d + w
      if nd < dist[v]
        dist[v] = nd
        ways[v] = ways[u]
        heap_push(heap, [nd, v])
      elsif nd == dist[v]
        ways[v] += ways[u]
        ways[v] -= mod if ways[v] >= mod
      end
    end
  end

  ways[n - 1] % mod
end
```

## Scala

```scala
object Solution {
  def countPaths(n: Int, roads: Array[Array[Int]]): Int = {
    val MOD = 1000000007L
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[(Int, Long)]())
    var i = 0
    while (i < roads.length) {
      val u = roads(i)(0)
      val v = roads(i)(1)
      val w = roads(i)(2).toLong
      adj(u).append((v, w))
      adj(v).append((u, w))
      i += 1
    }

    val dist = Array.fill[Long](n)(Long.MaxValue)
    val ways = Array.fill[Long](n)(0L)
    dist(0) = 0L
    ways(0) = 1L

    case class State(d: Long, v: Int)

    val pq = new java.util.PriorityQueue[State](
      new java.util.Comparator[State] {
        override def compare(a: State, b: State): Int = java.lang.Long.compare(a.d, b.d)
      }
    )
    pq.offer(State(0L, 0))

    while (!pq.isEmpty) {
      val cur = pq.poll()
      if (cur.d != dist(cur.v)) {
        // outdated entry, skip
      } else {
        val neighbors = adj(cur.v)
        var idx = 0
        while (idx < neighbors.length) {
          val (to, w) = neighbors(idx)
          val nd = cur.d + w
          if (nd < dist(to)) {
            dist(to) = nd
            ways(to) = ways(cur.v)
            pq.offer(State(nd, to))
          } else if (nd == dist(to)) {
            ways(to) = (ways(to) + ways(cur.v)) % MOD
          }
          idx += 1
        }
      }
    }

    ((ways(n - 1) % MOD).toInt)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_paths(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut graph: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n_usize];
        for road in roads.iter() {
            let u = road[0] as usize;
            let v = road[1] as usize;
            let w = road[2] as i64;
            graph[u].push((v, w));
            graph[v].push((u, w));
        }

        const MOD: i64 = 1_000_000_007;
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let mut dist: Vec<i64> = vec![i64::MAX; n_usize];
        let mut ways: Vec<i64> = vec![0; n_usize];
        dist[0] = 0;
        ways[0] = 1;

        let mut heap = BinaryHeap::<Reverse<(i64, usize)>>::new();
        heap.push(Reverse((0_i64, 0usize)));

        while let Some(Reverse((d, u))) = heap.pop() {
            if d != dist[u] {
                continue;
            }
            for &(v, w) in &graph[u] {
                let nd = d + w;
                if nd < dist[v] {
                    dist[v] = nd;
                    ways[v] = ways[u];
                    heap.push(Reverse((nd, v)));
                } else if nd == dist[v] {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }

        (ways[n_usize - 1] % MOD) as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract
         racket/match
         racket/priority-queue)

(define MOD 1000000007)
(define INF (expt 10 18))

(define/contract (count-paths n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((adj (make-vector n '()))
         ;; build adjacency list
         (_ (for ([road roads])
              (match-define (list u v w) road)
              (vector-set! adj u (cons (list v w) (vector-ref adj u)))
              (vector-set! adj v (cons (list u w) (vector-ref adj v)))))
         (dist (make-vector n INF))
         (ways (make-vector n 0))
         (less? (lambda (a b) (< (first a) (first b))))
         (pq (make-pq #:less? less?)))
    ;; initialization
    (vector-set! dist 0 0)
    (vector-set! ways 0 1)
    (pq-add! pq (list 0 0))
    ;; Dijkstra with path counting
    (let recur ()
      (unless (pq-empty? pq)
        (define cur (pq-pop! pq))
        (define d (first cur))
        (define u (second cur))
        (when (= d (vector-ref dist u))
          (for ([edge (vector-ref adj u)])
            (define v (first edge))
            (define w (second edge))
            (define nd (+ d w))
            (cond
              [(< nd (vector-ref dist v))
               (vector-set! dist v nd)
               (vector-set! ways v (vector-ref ways u))
               (pq-add! pq (list nd v))]
              [(= nd (vector-ref dist v))
               (define new-ways (+ (vector-ref ways v) (vector-ref ways u)))
               (vector-set! ways v (modulo new-ways MOD))])))
        (recur)))
    (modulo (vector-ref ways (- n 1)) MOD)))
```

## Erlang

```erlang
-module(solution).
-export([count_paths/2]).

-define(MOD, 1000000007).

-spec count_paths(N :: integer(), Roads :: [[integer()]]) -> integer().
count_paths(N, Roads) ->
    Adj = build_adj(Roads, #{}),
    {_DistMap, WaysMap} = dijkstra(N, Adj),
    maps:get(N - 1, WaysMap, 0).

build_adj([], Acc) -> Acc;
build_adj([[U, V, T] | Rest], Acc) ->
    Acc1 = add_edge(U, {V, T}, Acc),
    Acc2 = add_edge(V, {U, T}, Acc1),
    build_adj(Rest, Acc2).

add_edge(Node, Edge, Map) ->
    List = maps:get(Node, Map, []),
    maps:put(Node, [Edge | List], Map).

dijkstra(N, Adj) ->
    Inf = 1 bsl 60,
    Dist0 = maps:put(0, 0, #{}),
    Ways0 = maps:put(0, 1, #{}),
    Visited0 = #{},
    dijkstra_loop(N, Adj, Inf, Dist0, Ways0, Visited0).

dijkstra_loop(N, Adj, Inf, DistMap, WaysMap, Visited) ->
    case find_min_unvisited(N, DistMap, Visited, Inf) of
        {none, _} -> {DistMap, WaysMap};
        {U, DistU} ->
            Visited1 = maps:put(U, true, Visited),
            Neighs = maps:get(U, Adj, []),
            {DistMap2, WaysMap2} =
                lists:foldl(
                    fun({V, W}, {DM, WM}) ->
                        NewDist = DistU + W,
                        CurDist = maps:get(V, DM, Inf),
                        if
                            NewDist < CurDist ->
                                DM1 = maps:put(V, NewDist, DM),
                                WM1 = maps:put(V, maps:get(U, WM), WM);
                            NewDist == CurDist ->
                                WaysV = (maps:get(V, WM, 0) + maps:get(U, WM)) rem ?MOD,
                                DM1 = DM,
                                WM1 = maps:put(V, WaysV, WM);
                            true ->
                                DM1 = DM,
                                WM1 = WM
                        end,
                        {DM1, WM1}
                    end,
                    {DistMap, WaysMap},
                    Neighs),
            dijkstra_loop(N, Adj, Inf, DistMap2, WaysMap2, Visited1)
    end.

find_min_unvisited(N, DistMap, Visited, Inf) ->
    find_min_unvisited_rec(0, N - 1, undefined, Inf, DistMap, Visited, Inf).

find_min_unvisited_rec(CurIdx, MaxIdx, MinNodeOpt, MinDist, _DistMap, _Visited, Inf)
        when CurIdx > MaxIdx ->
    case MinNodeOpt of
        undefined -> {none, Inf};
        _ -> {MinNodeOpt, MinDist}
    end;
find_min_unvisited_rec(CurIdx, MaxIdx, MinNodeOpt, MinDist, DistMap, Visited, Inf) ->
    if maps:is_key(CurIdx, Visited) ->
            find_min_unvisited_rec(CurIdx + 1, MaxIdx, MinNodeOpt, MinDist,
                                   DistMap, Visited, Inf);
       true ->
            D = maps:get(CurIdx, DistMap, Inf),
            if D < MinDist ->
                    find_min_unvisited_rec(CurIdx + 1, MaxIdx, CurIdx, D,
                                           DistMap, Visited, Inf);
               true ->
                    find_min_unvisited_rec(CurIdx + 1, MaxIdx, MinNodeOpt, MinDist,
                                           DistMap, Visited, Inf)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007
  @inf 1_000_000_000_000_000_000

  @spec count_paths(n :: integer, roads :: [[integer]]) :: integer
  def count_paths(n, roads) do
    # build adjacency list
    graph =
      Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Enum.reduce(roads, fn [u, v, w], acc ->
        acc
        |> Map.update!(u, fn lst -> [{v, w} | lst] end)
        |> Map.update!(v, fn lst -> [{u, w} | lst] end)
      end)

    # distance, ways and visited maps
    dist =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, i, @inf)
      end)
      |> Map.put(0, 0)

    ways =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, i, 0)
      end)
      |> Map.put(0, 1)

    visited =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, i, false)
      end)

    # Dijkstra without heap (O(n^2))
    {_, final_ways, _} =
      1..n
      |> Enum.reduce({dist, ways, visited}, fn _, {d_acc, w_acc, v_acc} ->
        # find unvisited node with smallest distance
        {u, u_dist} =
          Enum.reduce(0..(n - 1), {nil, @inf}, fn node, {cur_node, cur_dist} ->
            if not Map.get(v_acc, node) do
              d = Map.get(d_acc, node)

              if d < cur_dist do
                {node, d}
              else
                {cur_node, cur_dist}
              end
            else
              {cur_node, cur_dist}
            end
          end)

        # all nodes visited or unreachable
        if u == nil do
          {d_acc, w_acc, v_acc}
        else
          v_acc = Map.put(v_acc, u, true)

          {new_dist, new_ways} =
            Enum.reduce(Map.get(graph, u), {d_acc, w_acc}, fn {v, w},
                                                             {dist_map, ways_map} ->
              if not Map.get(v_acc, v) do
                nd = u_dist + w
                cur_v_dist = Map.get(dist_map, v)

                cond do
                  nd < cur_v_dist ->
                    {
                      Map.put(dist_map, v, nd),
                      Map.put(ways_map, v, Map.get(ways_map, u))
                    }

                  nd == cur_v_dist ->
                    {
                      dist_map,
                      Map.update!(ways_map, v, fn val ->
                        (val + Map.get(ways_map, u)) rem @mod
                      end)
                    }

                  true ->
                    {dist_map, ways_map}
                end
              else
                {dist_map, ways_map}
              end
            end)

          {new_dist, new_ways, v_acc}
        end
      end)

    Map.get(final_ways, n - 1) |> rem(@mod)
  end
end
```

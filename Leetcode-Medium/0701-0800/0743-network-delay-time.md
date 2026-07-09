# 0743. Network Delay Time

## Cpp

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        const long long INF = 1e18;
        vector<vector<pair<int,int>>> adj(n + 1);
        for (const auto& t : times) {
            adj[t[0]].push_back({t[1], t[2]});
        }
        vector<long long> dist(n + 1, INF);
        dist[k] = 0;
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        pq.push({0, k});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto& [v, w] : adj[u]) {
                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }
        long long ans = 0;
        for (int i = 1; i <= n; ++i) {
            if (dist[i] == INF) return -1;
            ans = max(ans, dist[i]);
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        List<int[]>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();
        for (int[] t : times) {
            graph[t[0]].add(new int[]{t[1], t[2]});
        }
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, k});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0], u = cur[1];
            if (d > dist[u]) continue;
            for (int[] edge : graph[u]) {
                int v = edge[0], w = edge[1];
                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    pq.offer(new int[]{dist[v], v});
                }
            }
        }
        int max = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) return -1;
            max = Math.max(max, dist[i]);
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        import heapq

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        max_dist = max(dist[1:])  # nodes are labeled from 1 to n
        return -1 if max_dist == INF else int(max_dist)
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        
        max_dist = max(dist[1:])
        return -1 if max_dist == INF else int(max_dist)
```

## C

```c
#include <limits.h>

int networkDelayTime(int** times, int timesSize, int* timesColSize, int n, int k) {
    // adjacency matrix, -1 indicates no edge
    int adj[101][101];
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            adj[i][j] = -1;
    
    for (int i = 0; i < timesSize; ++i) {
        int u = times[i][0];
        int v = times[i][1];
        int w = times[i][2];
        adj[u][v] = w;
    }
    
    int dist[101];
    int visited[101] = {0};
    const int INF = INT_MAX / 2;
    for (int i = 1; i <= n; ++i) dist[i] = INF;
    dist[k] = 0;
    
    for (int iter = 0; iter < n; ++iter) {
        int u = -1;
        int best = INF;
        for (int i = 1; i <= n; ++i) {
            if (!visited[i] && dist[i] < best) {
                best = dist[i];
                u = i;
            }
        }
        if (u == -1) break; // remaining nodes unreachable
        visited[u] = 1;
        for (int v = 1; v <= n; ++v) {
            if (adj[u][v] != -1 && !visited[v]) {
                int nd = dist[u] + adj[u][v];
                if (nd < dist[v]) dist[v] = nd;
            }
        }
    }
    
    int answer = 0;
    for (int i = 1; i <= n; ++i) {
        if (dist[i] == INF) return -1;
        if (dist[i] > answer) answer = dist[i];
    }
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int NetworkDelayTime(int[][] times, int n, int k) {
        var graph = new List<(int to, int weight)>[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new List<(int, int)>();
        foreach (var t in times) {
            int u = t[0], v = t[1], w = t[2];
            graph[u].Add((v, w));
        }

        var dist = new int[n + 1];
        const int INF = int.MaxValue / 2;
        for (int i = 1; i <= n; i++) dist[i] = INF;
        dist[k] = 0;

        var pq = new PriorityQueue<int, int>();
        pq.Enqueue(k, 0);

        while (pq.Count > 0) {
            int u = pq.Dequeue();
            int d = dist[u];
            // Since PriorityQueue does not provide priority on dequeue,
            // we need to ensure we process only if current distance matches.
            foreach (var edge in graph[u]) {
                int v = edge.to;
                int nd = d + edge.weight;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.Enqueue(v, nd);
                }
            }
        }

        int maxDist = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == INF) return -1;
            if (dist[i] > maxDist) maxDist = dist[i];
        }
        return maxDist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function(times, n, k) {
    // Build adjacency list
    const adj = Array.from({length: n + 1}, () => []);
    for (const [u, v, w] of times) {
        adj[u].push([v, w]);
    }

    // Min-heap priority queue
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(item) {
            this.heap.push(item);
            this._siftUp(this.heap.length - 1);
        }
        pop() {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this._siftDown(0);
            }
            return top;
        }
        _siftUp(idx) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][1] <= this.heap[idx][1]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        _siftDown(idx) {
            const length = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let smallest = idx;

                if (left < length && this.heap[left][1] < this.heap[smallest][1]) smallest = left;
                if (right < length && this.heap[right][1] < this.heap[smallest][1]) smallest = right;

                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const dist = new Array(n + 1).fill(Infinity);
    dist[k] = 0;

    const heap = new MinHeap();
    heap.push([k, 0]);

    while (heap.size() > 0) {
        const [node, d] = heap.pop();
        if (d > dist[node]) continue; // outdated entry
        for (const [nei, w] of adj[node]) {
            const nd = d + w;
            if (nd < dist[nei]) {
                dist[nei] = nd;
                heap.push([nei, nd]);
            }
        }
    }

    let maxDelay = 0;
    for (let i = 1; i <= n; ++i) {
        if (dist[i] === Infinity) return -1;
        if (dist[i] > maxDelay) maxDelay = dist[i];
    }
    return maxDelay;
};
```

## Typescript

```typescript
function networkDelayTime(times: number[][], n: number, k: number): number {
    // Build adjacency list
    const adj: Map<number, [number, number][]> = new Map();
    for (const [u, v, w] of times) {
        if (!adj.has(u)) adj.set(u, []);
        adj.get(u)!.push([v, w]);
    }

    // Min-heap implementation
    class MinHeap {
        private heap: [number, number][] = []; // [dist, node]

        size(): number {
            return this.heap.length;
        }

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

                if (left < length && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < length && this.heap[right][0] < this.heap[smallest][0]) smallest = right;

                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const dist: number[] = new Array(n + 1).fill(Infinity);
    dist[k] = 0;

    const heap = new MinHeap();
    heap.push([0, k]);

    while (heap.size() > 0) {
        const [d, u] = heap.pop()!;
        if (d !== dist[u]) continue; // outdated entry
        const edges = adj.get(u);
        if (!edges) continue;
        for (const [v, w] of edges) {
            if (dist[v] > d + w) {
                dist[v] = d + w;
                heap.push([dist[v], v]);
            }
        }
    }

    let maxDist = 0;
    for (let i = 1; i <= n; ++i) {
        if (dist[i] === Infinity) return -1;
        if (dist[i] > maxDist) maxDist = dist[i];
    }
    return maxDist;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $times
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function networkDelayTime($times, $n, $k) {
        // Build adjacency list
        $graph = [];
        foreach ($times as $t) {
            [$u, $v, $w] = $t;
            if (!isset($graph[$u])) {
                $graph[$u] = [];
            }
            $graph[$u][] = [$v, $w];
        }

        // Initialize distances
        $dist = array_fill(0, $n + 1, PHP_INT_MAX);
        $dist[$k] = 0;

        // Min-heap using SplPriorityQueue (invert priority)
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert($k, 0); // priority = -distance (0)

        while (!$pq->isEmpty()) {
            $item = $pq->extract();
            $node = $item['data'];
            $d = -$item['priority']; // actual distance

            if ($d > $dist[$node]) {
                continue; // outdated entry
            }

            foreach ($graph[$node] ?? [] as $edge) {
                [$nei, $w] = $edge;
                $newDist = $d + $w;
                if ($newDist < $dist[$nei]) {
                    $dist[$nei] = $newDist;
                    $pq->insert($nei, -$newDist);
                }
            }
        }

        // Determine the maximum distance
        $maxTime = 0;
        for ($i = 1; $i <= $n; $i++) {
            if ($dist[$i] === PHP_INT_MAX) {
                return -1;
            }
            if ($dist[$i] > $maxTime) {
                $maxTime = $dist[$i];
            }
        }

        return $maxTime;
    }
}
```

## Swift

```swift
struct Item {
    var node: Int
    var dist: Int
}

struct MinHeap {
    private var heap: [Item] = []
    
    mutating func push(_ item: Item) {
        heap.append(item)
        siftUp(heap.count - 1)
    }
    
    mutating func pop() -> Item? {
        guard !heap.isEmpty else { return nil }
        let top = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            siftDown(0)
        }
        return top
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if heap[child].dist < heap[parent].dist {
                heap.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = 2 * parent + 1
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
    func networkDelayTime(_ times: [[Int]], _ n: Int, _ k: Int) -> Int {
        var graph = [[(to: Int, weight: Int)]](repeating: [], count: n + 1)
        for edge in times {
            let u = edge[0], v = edge[1], w = edge[2]
            graph[u].append((to: v, weight: w))
        }
        
        var dist = [Int](repeating: Int.max, count: n + 1)
        dist[k] = 0
        
        var heap = MinHeap()
        heap.push(Item(node: k, dist: 0))
        
        while let cur = heap.pop() {
            if cur.dist > dist[cur.node] { continue }
            for e in graph[cur.node] {
                let nd = cur.dist + e.weight
                if nd < dist[e.to] {
                    dist[e.to] = nd
                    heap.push(Item(node: e.to, dist: nd))
                }
            }
        }
        
        var maxDist = 0
        for i in 1...n {
            if dist[i] == Int.max { return -1 }
            if dist[i] > maxDist { maxDist = dist[i] }
        }
        return maxDist
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
        val adj = Array(n + 1) { mutableListOf<Pair<Int, Int>>() }
        for (t in times) {
            val u = t[0]
            val v = t[1]
            val w = t[2]
            adj[u].add(Pair(v, w))
        }

        val dist = IntArray(n + 1) { Int.MAX_VALUE }
        dist[k] = 0
        val pq = java.util.PriorityQueue<Pair<Int, Int>>(compareBy { it.first })
        pq.offer(Pair(0, k))

        while (pq.isNotEmpty()) {
            val (d, u) = pq.poll()
            if (d != dist[u]) continue
            for ((v, w) in adj[u]) {
                val nd = d + w
                if (nd < dist[v]) {
                    dist[v] = nd
                    pq.offer(Pair(nd, v))
                }
            }
        }

        var maxTime = 0
        for (i in 1..n) {
            if (dist[i] == Int.MAX_VALUE) return -1
            if (dist[i] > maxTime) maxTime = dist[i]
        }
        return maxTime
    }
}
```

## Dart

```dart
class _MinHeap {
  final List<List<int>> _data = [];

  bool get isEmpty => _data.isEmpty;

  void push(List<int> item) {
    _data.add(item);
    _siftUp(_data.length - 1);
  }

  List<int> pop() {
    final result = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return result;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_data[parent][0] <= _data[idx][0]) break;
      final tmp = _data[parent];
      _data[parent] = _data[idx];
      _data[idx] = tmp;
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final n = _data.length;
    while (true) {
      final left = idx * 2 + 1;
      final right = left + 1;
      int smallest = idx;
      if (left < n && _data[left][0] < _data[smallest][0]) smallest = left;
      if (right < n && _data[right][0] < _data[smallest][0]) smallest = right;
      if (smallest == idx) break;
      final tmp = _data[idx];
      _data[idx] = _data[smallest];
      _data[smallest] = tmp;
      idx = smallest;
    }
  }
}

class Solution {
  int networkDelayTime(List<List<int>> times, int n, int k) {
    // Build adjacency list
    final List<List<List<int>>> graph = List.generate(n + 1, (_) => []);
    for (final t in times) {
      graph[t[0]].add([t[1], t[2]]);
    }

    const int INF = 1 << 60;
    final List<int> dist = List.filled(n + 1, INF);
    dist[k] = 0;

    final heap = _MinHeap();
    heap.push([0, k]);

    while (!heap.isEmpty) {
      final cur = heap.pop();
      final int d = cur[0];
      final int u = cur[1];
      if (d > dist[u]) continue;
      for (final edge in graph[u]) {
        final int v = edge[0];
        final int w = edge[1];
        if (dist[v] > d + w) {
          dist[v] = d + w;
          heap.push([dist[v], v]);
        }
      }
    }

    int maxDist = 0;
    for (int i = 1; i <= n; ++i) {
      if (dist[i] == INF) return -1;
      if (dist[i] > maxDist) maxDist = dist[i];
    }
    return maxDist;
  }
}
```

## Golang

```go
func networkDelayTime(times [][]int, n int, k int) int {
	type Edge struct{ to, w int }
	graph := make([][]Edge, n+1)
	for _, t := range times {
		u, v, w := t[0], t[1], t[2]
		graph[u] = append(graph[u], Edge{to: v, w: w})
	}
	const INF = int(^uint(0) >> 1) // max int
	dist := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dist[i] = INF
	}
	dist[k] = 0

	type Item struct{ node, d int }
	type PriorityQueue []Item
	func (pq PriorityQueue) Len() int { return len(pq) }
	func (pq PriorityQueue) Less(i, j int) bool { return pq[i].d < pq[j].d }
	func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
	func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(Item)) }
	func (pq *PriorityQueue) Pop() interface{} {
		old := *pq
		n := len(old)
		it := old[n-1]
		*pq = old[:n-1]
		return it
	}
	pq := &PriorityQueue{}
	heap.Push(pq, Item{node: k, d: 0})

	for pq.Len() > 0 {
		cur := heap.Pop(pq).(Item)
		if cur.d != dist[cur.node] {
			continue
		}
		u := cur.node
		for _, e := range graph[u] {
			if nd := cur.d + e.w; nd < dist[e.to] {
				dist[e.to] = nd
				heap.Push(pq, Item{node: e.to, d: nd})
			}
		}
	}

	maxDist := 0
	for i := 1; i <= n; i++ {
		if dist[i] == INF {
			return -1
		}
		if dist[i] > maxDist {
			maxDist = dist[i]
		}
	}
	return maxDist
}
```

## Ruby

```ruby
def network_delay_time(times, n, k)
  graph = Hash.new { |h, key| h[key] = [] }
  times.each do |u, v, w|
    graph[u] << [v, w]
  end

  dist = Array.new(n + 1, Float::INFINITY)
  visited = Array.new(n + 1, false)
  dist[k] = 0

  n.times do
    u = -1
    min_dist = Float::INFINITY
    (1..n).each do |i|
      if !visited[i] && dist[i] < min_dist
        min_dist = dist[i]
        u = i
      end
    end
    break if u == -1 || min_dist == Float::INFINITY

    visited[u] = true
    graph[u].each do |v, w|
      if dist[v] > dist[u] + w
        dist[v] = dist[u] + w
      end
    end
  end

  max_delay = dist[1..n].max
  max_delay == Float::INFINITY ? -1 : max_delay.to_i
end
```

## Scala

```scala
object Solution {
  import java.util.PriorityQueue

  def networkDelayTime(times: Array[Array[Int]], n: Int, k: Int): Int = {
    // Build adjacency list
    val graph = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (t <- times) {
      val u = t(0)
      val v = t(1)
      val w = t(2)
      graph(u).append((v, w))
    }

    // Dijkstra
    val INF = Long.MaxValue
    val dist = Array.fill[Long](n + 1)(INF)
    dist(k) = 0L

    val pq = new PriorityQueue[(Long, Int)](
      (a: (Long, Int), b: (Long, Int)) => java.lang.Long.compare(a._1, b._1)
    )
    pq.offer((0L, k))

    while (!pq.isEmpty) {
      val (d, u) = pq.poll()
      if (d != dist(u)) {
        // outdated entry
      } else {
        for ((v, w) <- graph(u)) {
          val nd = d + w
          if (nd < dist(v)) {
            dist(v) = nd
            pq.offer((nd, v))
          }
        }
      }
    }

    var maxDist = 0L
    for (i <- 1 to n) {
      if (dist(i) == INF) return -1
      if (dist(i) > maxDist) maxDist = dist(i)
    }
    maxDist.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let n_usize = n as usize;
        let mut graph: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n_usize + 1];
        for t in times.iter() {
            let u = t[0] as usize;
            let v = t[1] as usize;
            let w = t[2];
            graph[u].push((v, w));
        }

        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        const INF: i32 = i32::MAX / 4;
        let mut dist = vec![INF; n_usize + 1];
        let start = k as usize;
        dist[start] = 0;

        let mut heap = BinaryHeap::new();
        heap.push(Reverse((0i32, start)));

        while let Some(Reverse((d, u))) = heap.pop() {
            if d > dist[u] {
                continue;
            }
            for &(v, w) in &graph[u] {
                let nd = d + w;
                if nd < dist[v] {
                    dist[v] = nd;
                    heap.push(Reverse((nd, v)));
                }
            }
        }

        let mut ans = 0i32;
        for i in 1..=n_usize {
            if dist[i] == INF {
                return -1;
            }
            if dist[i] > ans {
                ans = dist[i];
            }
        }
        ans
    }
}
```

## Racket

```racket
(require data/heap)

(define/contract (network-delay-time times n k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  (let* ((adj (make-vector (+ n 1) '()))
         ;; build adjacency list
         (build-adj
          (lambda ()
            (for ([e times])
              (match-define (list u v w) e)
              (vector-set! adj u (cons (cons v w) (vector-ref adj u))))))
         (dist (make-vector (+ n 1) +inf.0))
         (pair< (lambda (a b) (< (first a) (first b))))
         (heap (make-heap pair<)))
    (build-adj)
    (vector-set! dist k 0)
    (heap-insert! heap (list 0 k))
    ;; Dijkstra
    (let loop ()
      (when (not (heap-empty? heap))
        (define cur (heap-extract-min! heap))
        (define d (first cur))
        (define u (second cur))
        (when (= d (vector-ref dist u))
          (for ([edge (in-list (vector-ref adj u))])
            (define v (car edge))
            (define w (cdr edge))
            (define nd (+ d w))
            (when (< nd (vector-ref dist v))
              (vector-set! dist v nd)
              (heap-insert! heap (list nd v)))))
        (loop)))
    ;; compute answer
    (let ((ans 0) (ok #t))
      (for ([i (in-range 1 (+ n 1))])
        (define d (vector-ref dist i))
        (if (= d +inf.0)
            (set! ok #f)
            (when (> d ans) (set! ans d))))
      (if ok ans -1))))
```

## Erlang

```erlang
-module(solution).
-export([network_delay_time/3]).

-spec network_delay_time(Times :: [[integer()]], N :: integer(), K :: integer()) -> integer().
network_delay_time(Times, N, K) ->
    Graph = build_graph(Times, #{}),
    Dist0 = #{K => 0},
    Visited0 = #{},
    Heap0 = [{0, K}],
    {DistMap, _} = dijkstra(Graph, Dist0, Visited0, Heap0),
    case reachable_all(DistMap, N) of
        true ->
            lists:max([maps:get(I, DistMap) || I <- lists:seq(1, N)]);
        false -> -1
    end.

build_graph([], G) -> G;
build_graph([[U,V,W]|Rest], G) ->
    Updated = maps:update_with(U,
                               fun(L) -> [{V,W}|L] end,
                               [{V,W}],
                               G),
    build_graph(Rest, Updated).

dijkstra(_Graph, Dist, Visited, []) ->
    {Dist, []};
dijkstra(Graph, Dist, Visited, Heap) ->
    Sorted = lists:keysort(1, Heap),
    [{D,U}|Rest] = Sorted,
    case maps:is_key(U, Visited) of
        true ->
            dijkstra(Graph, Dist, Visited, Rest);
        false ->
            Visited2 = maps:put(U, true, Visited),
            Adj = maps:get(U, Graph, []),
            {Dist2, Heap2} = lists:foldl(fun({V,W}, {DAcc,QAcc}) ->
                NewDist = D + W,
                case maps:get(V, DAcc, undefined) of
                    undefined ->
                        {maps:put(V, NewDist, DAcc), [{NewDist, V}|QAcc]};
                    Old when NewDist < Old ->
                        {maps:put(V, NewDist, DAcc), [{NewDist, V}|QAcc]};
                    _ ->
                        {DAcc, QAcc}
                end
            end, {Dist, Rest}, Adj),
            dijkstra(Graph, Dist2, Visited2, Heap2)
    end.

reachable_all(DistMap, N) ->
    lists:all(fun(I) -> maps:is_key(I, DistMap) end,
              lists:seq(1, N)).
```

## Elixir

```elixir
defmodule Solution do
  @spec network_delay_time(times :: [[integer]], n :: integer, k :: integer) :: integer
  def network_delay_time(times, n, k) do
    adj =
      Enum.reduce(times, %{}, fn [u, v, w], acc ->
        Map.update(acc, u, [{v, w}], fn list -> [{v, w} | list] end)
      end)

    inf = 1_000_000_000

    dist0 =
      1..n
      |> Enum.reduce(%{}, fn i, m -> Map.put(m, i, inf) end)
      |> Map.put(k, 0)

    final_dist = dijkstra(dist0, MapSet.new(), adj, n, inf)

    max_delay = final_dist |> Map.values() |> Enum.max()

    if max_delay == inf, do: -1, else: max_delay
  end

  defp dijkstra(dist, visited, adj, n, inf) do
    if MapSet.size(visited) == n do
      dist
    else
      {u, min_dist} =
        1..n
        |> Enum.reduce({nil, inf}, fn i, {cur_u, cur_d} ->
          if not MapSet.member?(visited, i) do
            d = Map.get(dist, i)
            if d < cur_d, do: {i, d}, else: {cur_u, cur_d}
          else
            {cur_u, cur_d}
          end
        end)

      if min_dist == inf do
        dist
      else
        visited = MapSet.put(visited, u)

        new_dist =
          case Map.get(adj, u) do
            nil ->
              dist

            neighbors ->
              Enum.reduce(neighbors, dist, fn {v, w}, dacc ->
                du = Map.get(dacc, u)
                dv = Map.get(dacc, v)

                if du + w < dv do
                  Map.put(dacc, v, du + w)
                else
                  dacc
                end
              end)
          end

        dijkstra(new_dist, visited, adj, n, inf)
      end
    end
  end
end
```

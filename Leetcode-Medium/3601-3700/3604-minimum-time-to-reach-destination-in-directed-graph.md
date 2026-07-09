# 3604. Minimum Time to Reach Destination in Directed Graph

## Cpp

```cpp
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges) {
        using ll = long long;
        const ll INF = (1LL<<60);
        struct Edge {int to; int start; int end;};
        vector<vector<Edge>> adj(n);
        for (auto &e : edges) {
            int u=e[0], v=e[1], s=e[2], en=e[3];
            adj[u].push_back({v,s,en});
        }
        vector<ll> dist(n, INF);
        priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
        dist[0]=0;
        pq.push({0,0});
        while(!pq.empty()){
            auto [t,u]=pq.top(); pq.pop();
            if(t!=dist[u]) continue;
            if(u==n-1) break; // earliest reached destination
            for(const auto &ed: adj[u]){
                if(t>ed.end) continue; // cannot use this edge
                ll depart = max<ll>(t, ed.start);
                ll arrival = depart + 1;
                if(arrival < dist[ed.to]){
                    dist[ed.to]=arrival;
                    pq.push({arrival, ed.to});
                }
            }
        }
        return dist[n-1]==INF ? -1 : (int)dist[n-1];
    }
};
```

## Java

```java
class Solution {
    static class Edge {
        int v;
        int start;
        int end;
        Edge(int v, int start, int end) {
            this.v = v;
            this.start = start;
            this.end = end;
        }
    }

    public int minTime(int n, int[][] edges) {
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Edge>[] graph = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], s = e[2], en = e[3];
            graph[u].add(new Edge(v, s, en));
        }

        long INF = Long.MAX_VALUE;
        long[] dist = new long[n];
        java.util.Arrays.fill(dist, INF);
        dist[0] = 0;

        java.util.PriorityQueue<long[]> pq = new java.util.PriorityQueue<>(
                (a, b) -> Long.compare(a[0], b[0])
        );
        pq.offer(new long[]{0L, 0});

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long time = cur[0];
            int u = (int) cur[1];
            if (time != dist[u]) continue;
            for (Edge e : graph[u]) {
                if (time > e.end) continue; // cannot use this edge
                long depart = Math.max(time, e.start);
                long arrival = depart + 1;
                if (arrival < dist[e.v]) {
                    dist[e.v] = arrival;
                    pq.offer(new long[]{arrival, e.v});
                }
            }
        }

        return dist[n - 1] == INF ? -1 : (int) dist[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minTime(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        import heapq

        adj = [[] for _ in range(n)]
        for u, v, s, e in edges:
            adj[u].append((v, s, e))

        INF = 10**20
        dist = [INF] * n
        dist[0] = 0
        heap = [(0, 0)]  # (time, node)

        while heap:
            t, u = heapq.heappop(heap)
            if t != dist[u]:
                continue
            if u == n - 1:
                return t
            for v, start, end in adj[u]:
                if t > end:
                    continue
                depart = start if t < start else t
                arrival = depart + 1
                if arrival < dist[v]:
                    dist[v] = arrival
                    heapq.heappush(heap, (arrival, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, s, e in edges:
            adj[u].append((v, s, e))
        
        INF = 10**20
        dist = [INF] * n
        dist[0] = 0
        heap = [(0, 0)]  # (time, node)
        
        while heap:
            t, u = heapq.heappop(heap)
            if t != dist[u]:
                continue
            if u == n - 1:
                return t
            for v, start, end in adj[u]:
                if t > end:
                    continue
                depart = start if t < start else t
                arrival = depart + 1
                if arrival < dist[v]:
                    dist[v] = arrival
                    heapq.heappush(heap, (arrival, v))
        
        return -1 if dist[n - 1] == INF else dist[n - 1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int to;
    int start;
    int end;
    int next;
} Edge;

typedef struct {
    long long time;
    int node;
} HeapNode;

static void heapSwap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapNode *heap, int *size, long long t, int v) {
    int i = (*size)++;
    heap[i].time = t;
    heap[i].node = v;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].time <= heap[i].time) break;
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
        if (r < *size && heap[r].time < heap[l].time) smallest = r;
        if (heap[i].time <= heap[smallest].time) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

int minTime(int n, int** edges, int edgesSize, int* edgesColSize){
    if (n == 1) return 0; // already at destination

    /* Build adjacency list using forward star */
    int *head = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    Edge *E = (Edge*)malloc(edgesSize * sizeof(Edge));

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int s = edges[i][2];
        int e = edges[i][3];
        E[i].to = v;
        E[i].start = s;
        E[i].end = e;
        E[i].next = head[u];
        head[u] = i;
    }

    long long *dist = (long long*)malloc(n * sizeof(long long));
    for (int i = 0; i < n; ++i) dist[i] = LLONG_MAX;
    dist[0] = 0;

    /* Heap capacity: at most edgesSize + n */
    int heapCap = edgesSize + n + 5;
    HeapNode *heap = (HeapNode*)malloc(heapCap * sizeof(HeapNode));
    int heapSize = 0;
    heapPush(heap, &heapSize, 0LL, 0);

    while (heapSize) {
        HeapNode cur = heapPop(heap, &heapSize);
        long long t = cur.time;
        int u = cur.node;
        if (t != dist[u]) continue; // outdated entry
        for (int idx = head[u]; idx != -1; idx = E[idx].next) {
            int v = E[idx].to;
            int s = E[idx].start;
            int e = E[idx].end;
            if (t > (long long)e) continue; // cannot use
            long long depart = t < (long long)s ? (long long)s : t;
            long long arrive = depart + 1LL;
            if (arrive < dist[v]) {
                dist[v] = arrive;
                heapPush(heap, &heapSize, arrive, v);
            }
        }
    }

    free(head);
    free(E);
    free(dist);
    free(heap);

    return (dist[n-1] == LLONG_MAX) ? -1 : (int)dist[n-1];
}
```

## Csharp

```csharp
public class Solution {
    public int MinTime(int n, int[][] edges) {
        var adj = new List<(int v, int start, int end)>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<(int, int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], s = e[2], en = e[3];
            adj[u].Add((v, s, en));
        }

        const long INF = long.MaxValue / 4;
        var dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[0] = 0;

        var pq = new PriorityQueue<(int node, long time), long>();
        pq.Enqueue((0, 0L), 0L);

        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int u = cur.node;
            long t = cur.time;
            if (t != dist[u]) continue; // outdated entry

            foreach (var (v, start, end) in adj[u]) {
                if (t > end) continue; // cannot use this edge
                long depart = t < start ? start : t;
                long arrival = depart + 1;
                if (arrival < dist[v]) {
                    dist[v] = arrival;
                    pq.Enqueue((v, arrival), arrival);
                }
            }
        }

        return dist[n - 1] == INF ? -1 : (int)dist[n - 1];
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
var minTime = function(n, edges) {
    // Build adjacency list
    const adj = Array.from({length: n}, () => []);
    for (const [u, v, s, e] of edges) {
        adj[u].push({to: v, start: s, end: e});
    }

    // Min-heap priority queue
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(item) {
            const h = this.heap;
            h.push(item);
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
                    let l = i * 2 + 1, r = i * 2 + 2, smallest = i;
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

    const INF = Number.MAX_SAFE_INTEGER;
    const dist = new Array(n).fill(INF);
    dist[0] = 0;

    const pq = new MinHeap();
    pq.push([0, 0]); // [time, node]

    while (pq.size() > 0) {
        const [curTime, u] = pq.pop();
        if (curTime !== dist[u]) continue;
        if (u === n - 1) break; // early exit possible
        for (const e of adj[u]) {
            if (curTime > e.end) continue; // cannot use this edge
            const depart = curTime < e.start ? e.start : curTime;
            const arrive = depart + 1;
            if (arrive < dist[e.to]) {
                dist[e.to] = arrive;
                pq.push([arrive, e.to]);
            }
        }
    }

    return dist[n - 1] === INF ? -1 : dist[n - 1];
};
```

## Typescript

```typescript
function minTime(n: number, edges: number[][]): number {
    const adj: { to: number; start: number; end: number }[][] = Array.from({ length: n }, () => []);
    for (const [u, v, s, e] of edges) {
        adj[u].push({ to: v, start: s, end: e });
    }

    const INF = Number.MAX_SAFE_INTEGER;
    const dist = new Array<number>(n).fill(INF);
    dist[0] = 0;

    class MinHeap {
        heap: [number, number][] = [];
        push(item: [number, number]): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        bubbleUp(idx: number): void {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        pop(): [number, number] | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const last = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = last;
                this.bubbleDown(0);
            }
            return top;
        }
        bubbleDown(idx: number): void {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1,
                    right = left + 1,
                    smallest = idx;
                if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
        isEmpty(): boolean {
            return this.heap.length === 0;
        }
    }

    const pq = new MinHeap();
    pq.push([0, 0]);

    while (!pq.isEmpty()) {
        const [t, u] = pq.pop()!;
        if (t !== dist[u]) continue;
        if (u === n - 1) break;
        for (const e of adj[u]) {
            if (t > e.end) continue; // cannot depart
            const depart = t < e.start ? e.start : t;
            const arrival = depart + 1;
            if (arrival < dist[e.to]) {
                dist[e.to] = arrival;
                pq.push([arrival, e.to]);
            }
        }
    }

    return dist[n - 1] === INF ? -1 : dist[n - 1];
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
    function minTime($n, $edges) {
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $start, $end] = $e;
            $adj[$u][] = [$v, $start, $end];
        }

        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n, $INF);
        $dist[0] = 0;

        $pq = new SplPriorityQueue();
        // We need smallest time first, so use negative priority
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert(0, 0); // node 0 with time 0 (priority -0)

        while (!$pq->isEmpty()) {
            $elem = $pq->extract();
            $u = $elem['data'];
            $t = -$elem['priority']; // restore original time

            if ($t != $dist[$u]) {
                continue; // outdated entry
            }

            foreach ($adj[$u] as $edge) {
                [$v, $start, $end] = $edge;
                if ($t > $end) {
                    continue; // edge no longer usable
                }
                $newTime = max($t, $start) + 1;
                if ($newTime < $dist[$v]) {
                    $dist[$v] = $newTime;
                    $pq->insert($v, -$newTime);
                }
            }
        }

        return $dist[$n - 1] === $INF ? -1 : $dist[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    struct Edge {
        let to: Int
        let start: Int
        let end: Int
    }
    
    struct HeapNode {
        var time: Int
        var node: Int
    }
    
    class MinHeap {
        private var heap: [HeapNode] = []
        
        func push(_ element: HeapNode) {
            heap.append(element)
            siftUp(heap.count - 1)
        }
        
        func pop() -> HeapNode? {
            guard !heap.isEmpty else { return nil }
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                siftDown(0)
            }
            return top
        }
        
        private func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) >> 1
                if heap[child].time < heap[parent].time {
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
                if left < heap.count && heap[left].time < heap[smallest].time {
                    smallest = left
                }
                if right < heap.count && heap[right].time < heap[smallest].time {
                    smallest = right
                }
                if smallest == parent { break }
                heap.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }
    
    func minTime(_ n: Int, _ edges: [[Int]]) -> Int {
        var adj = Array(repeating: [Edge](), count: n)
        for e in edges {
            let u = e[0], v = e[1], s = e[2], en = e[3]
            adj[u].append(Edge(to: v, start: s, end: en))
        }
        
        let INF = Int.max / 4
        var dist = Array(repeating: INF, count: n)
        dist[0] = 0
        
        let heap = MinHeap()
        heap.push(HeapNode(time: 0, node: 0))
        
        while let cur = heap.pop() {
            let t = cur.time
            let u = cur.node
            if t != dist[u] { continue }
            if u == n - 1 { return t }
            for e in adj[u] {
                if t > e.end { continue }
                let depart = max(t, e.start)
                let arrival = depart + 1
                if arrival < dist[e.to] {
                    dist[e.to] = arrival
                    heap.push(HeapNode(time: arrival, node: e.to))
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
    fun minTime(n: Int, edges: Array<IntArray>): Int {
        data class Edge(val to: Int, val start: Int, val end: Int)
        val adj = Array(n) { mutableListOf<Edge>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val s = e[2]
            val en = e[3]
            adj[u].add(Edge(v, s, en))
        }
        val INF = Long.MAX_VALUE / 4
        val dist = LongArray(n) { INF }
        dist[0] = 0L

        data class Node(val time: Long, val v: Int) : Comparable<Node> {
            override fun compareTo(other: Node): Int = time.compareTo(other.time)
        }

        val pq = java.util.PriorityQueue<Node>()
        pq.add(Node(0L, 0))

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.time != dist[cur.v]) continue
            if (cur.v == n - 1) break
            for (e in adj[cur.v]) {
                if (cur.time > e.end.toLong()) continue
                val depart = maxOf(cur.time, e.start.toLong())
                val arrival = depart + 1L
                if (arrival < dist[e.to]) {
                    dist[e.to] = arrival
                    pq.add(Node(arrival, e.to))
                }
            }
        }

        return if (dist[n - 1] == INF) -1 else dist[n - 1].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minTime(int n, List<List<int>> edges) {
    // Edge representation
    class Edge {
      int to;
      int start;
      int end;
      Edge(this.to, this.start, this.end);
    }

    // Build adjacency list
    List<List<Edge>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      int s = e[2];
      int en = e[3];
      adj[u].add(Edge(v, s, en));
    }

    // Distance array
    const int INF = 9007199254740991; // large enough (2^53-1)
    List<int> dist = List.filled(n, INF);
    dist[0] = 0;

    // Min-heap implementation for Dijkstra
    class State {
      int time;
      int node;
      State(this.time, this.node);
    }

    class MinHeap {
      List<State> heap = [];

      bool get isEmpty => heap.isEmpty;

      void push(State s) {
        heap.add(s);
        _siftUp(heap.length - 1);
      }

      State pop() {
        State top = heap[0];
        State last = heap.removeLast();
        if (heap.isNotEmpty) {
          heap[0] = last;
          _siftDown(0);
        }
        return top;
      }

      void _siftUp(int idx) {
        while (idx > 0) {
          int parent = (idx - 1) >> 1;
          if (heap[parent].time <= heap[idx].time) break;
          var tmp = heap[parent];
          heap[parent] = heap[idx];
          heap[idx] = tmp;
          idx = parent;
        }
      }

      void _siftDown(int idx) {
        int n = heap.length;
        while (true) {
          int left = idx * 2 + 1;
          int right = left + 1;
          int smallest = idx;

          if (left < n && heap[left].time < heap[smallest].time) {
            smallest = left;
          }
          if (right < n && heap[right].time < heap[smallest].time) {
            smallest = right;
          }
          if (smallest == idx) break;
          var tmp = heap[idx];
          heap[idx] = heap[smallest];
          heap[smallest] = tmp;
          idx = smallest;
        }
      }
    }

    MinHeap pq = MinHeap();
    pq.push(State(0, 0));

    while (!pq.isEmpty) {
      State cur = pq.pop();
      int t = cur.time;
      int u = cur.node;
      if (t != dist[u]) continue; // outdated entry
      if (u == n - 1) return t;

      for (Edge e in adj[u]) {
        if (t > e.end) continue; // cannot start before edge closes
        int depart = t < e.start ? e.start : t;
        int arrive = depart + 1;
        if (arrive < dist[e.to]) {
          dist[e.to] = arrive;
          pq.push(State(arrive, e.to));
        }
      }
    }

    return -1;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type edge struct {
	to    int
	start int64
	end   int64
}

type item struct {
	node int
	time int64
}
type priorityQueue []item

func (pq priorityQueue) Len() int { return len(pq) }
func (pq priorityQueue) Less(i, j int) bool {
	return pq[i].time < pq[j].time
}
func (pq priorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *priorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(item))
}
func (pq *priorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[:n-1]
	return it
}

func minTime(n int, edges [][]int) int {
	graph := make([][]edge, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		s, en := int64(e[2]), int64(e[3])
		graph[u] = append(graph[u], edge{to: v, start: s, end: en})
	}

	const INF int64 = 1<<60 - 1
	dist := make([]int64, n)
	for i := range dist {
		dist[i] = INF
	}
	dist[0] = 0

	pq := &priorityQueue{}
	heap.Push(pq, item{node: 0, time: 0})

	for pq.Len() > 0 {
		it := heap.Pop(pq).(item)
		u, cur := it.node, it.time
		if cur != dist[u] {
			continue
		}
		if u == n-1 {
			break
		}
		for _, e := range graph[u] {
			if cur > e.end {
				continue
			}
			depart := cur
			if depart < e.start {
				depart = e.start
			}
			arrival := depart + 1
			if arrival < dist[e.to] {
				dist[e.to] = arrival
				heap.Push(pq, item{node: e.to, time: arrival})
			}
		}
	}

	if dist[n-1] == INF {
		return -1
	}
	return int(dist[n-1])
}
```

## Ruby

```ruby
def min_time(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |u, v, start_e, end_e|
    adj[u] << [v, start_e, end_e]
  end

  INF = (1 << 62)
  dist = Array.new(n, INF)
  dist[0] = 0

  # Simple binary min-heap
  class MinHeap
    def initialize
      @data = []
    end

    def empty?
      @data.empty?
    end

    def push(item) # item = [key, value]
      @data << item
      i = @data.size - 1
      while i > 0
        p = (i - 1) >> 1
        break if @data[p][0] <= @data[i][0]
        @data[p], @data[i] = @data[i], @data[p]
        i = p
      end
    end

    def pop
      return nil if @data.empty?
      top = @data[0]
      last = @data.pop
      unless @data.empty?
        @data[0] = last
        i = 0
        size = @data.size
        loop do
          l = (i << 1) + 1
          r = l + 1
          break if l >= size
          smallest = l
          smallest = r if r < size && @data[r][0] < @data[l][0]
          break if @data[i][0] <= @data[smallest][0]
          @data[i], @data[smallest] = @data[smallest], @data[i]
          i = smallest
        end
      end
      top
    end
  end

  heap = MinHeap.new
  heap.push([0, 0]) # [time, node]

  until heap.empty?
    cur_time, u = heap.pop
    next if cur_time != dist[u] # stale entry

    adj[u].each do |v, start_e, end_e|
      next if cur_time > end_e
      depart = cur_time < start_e ? start_e : cur_time
      arrival = depart + 1
      if arrival < dist[v]
        dist[v] = arrival
        heap.push([arrival, v])
      end
    end
  end

  ans = dist[n - 1]
  ans == INF ? -1 : ans
end
```

## Scala

```scala
object Solution {
    import java.util.PriorityQueue
    def minTime(n: Int, edges: Array[Array[Int]]): Int = {
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[(Int, Int, Int)]())
        var i = 0
        while (i < edges.length) {
            val e = edges(i)
            val u = e(0)
            val v = e(1)
            val s = e(2)
            val en = e(3)
            adj(u).append((v, s, en))
            i += 1
        }

        val INF: Long = Long.MaxValue / 4
        val dist = Array.fill[Long](n)(INF)
        dist(0) = 0L

        val pq = new PriorityQueue[(Long, Int)](
            (a: (Long, Int), b: (Long, Int)) => java.lang.Long.compare(a._1, b._1)
        )
        pq.offer((0L, 0))

        while (!pq.isEmpty) {
            val cur = pq.poll()
            val time = cur._1
            val u = cur._2
            if (time != dist(u)) {
                // stale entry
                continue
            }
            val edgesFromU = adj(u)
            var idx = 0
            while (idx < edgesFromU.length) {
                val (v, start, end) = edgesFromU(idx)
                if (time <= end) {
                    val depart = math.max(time, start.toLong)
                    if (depart <= end) {
                        val arrival = depart + 1L
                        if (arrival < dist(v)) {
                            dist(v) = arrival
                            pq.offer((arrival, v))
                        }
                    }
                }
                idx += 1
            }
        }

        if (dist(n - 1) == INF) -1 else dist(n - 1).toInt
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<(usize, i64, i64)>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let start = e[2] as i64;
            let end = e[3] as i64;
            adj[u].push((v, start, end));
        }

        const INF: i64 = i64::MAX / 4;
        let mut dist = vec![INF; n_usize];
        dist[0] = 0;

        let mut heap: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
        heap.push(Reverse((0_i64, 0_usize)));

        while let Some(Reverse((time, u))) = heap.pop() {
            if time != dist[u] {
                continue;
            }
            if u == n_usize - 1 {
                return time as i32;
            }
            for &(v, start, end) in &adj[u] {
                if time > end {
                    continue; // edge already closed
                }
                let depart = if time < start { start } else { time };
                let arrival = depart + 1;
                if arrival < dist[v] {
                    dist[v] = arrival;
                    heap.push(Reverse((arrival, v)));
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
(require racket/match)
(require racket/heap)

(define/contract (min-time n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((adj (make-vector n '()))
         (INF (+ (* 2 (expt 10 9)) n)))
    ;; build adjacency list
    (for ([e edges])
      (match-define (list u v s e) e)
      (vector-set! adj u (cons (list v s e) (vector-ref adj u))))
    (define dist (make-vector n INF))
    (vector-set! dist 0 0)
    (define heap (make-heap (lambda (a b) (< (first a) (first b)))))
    (heap-push! heap (list 0 0))
    (let loop ()
      (if (heap-empty? heap)
          -1
          (let* ((pair (heap-pop! heap))
                 (time (first pair))
                 (u (second pair)))
            (cond
              [(> time (vector-ref dist u)) (loop)]
              [(= u (- n 1)) time]
              [else
               (for ([edge (vector-ref adj u)])
                 (match-define (list v s e) edge)
                 (when (<= time e)
                   (let ((newt (if (< time s) (+ s 1) (+ time 1))))
                     (when (< newt (vector-ref dist v))
                       (vector-set! dist v newt)
                       (heap-push! heap (list newt v))))))
               (loop)])))))))
```

## Erlang

```erlang
-module(solution).
-export([min_time/2]).

-define(INF, 1000000000000000).

min_time(N, Edges) ->
    Adj = build_adj(Edges, #{}),
    dijkstra(N, Adj).

build_adj([], Adj) -> Adj;
build_adj([[U,V,S,E]|Rest], Adj) ->
    List = maps:get(U, Adj, []),
    NewAdj = maps:put(U, [{V,S,E}|List], Adj),
    build_adj(Rest, NewAdj).

dijkstra(N, Adj) ->
    Target = N - 1,
    Dist0 = #{0 => 0},
    Heap0 = gb_sets:add({0, 0}, gb_sets:new()),
    loop(Heap0, Dist0, Adj, Target).

loop(Heap, _Dist, _Adj, _Target) when gb_sets:is_empty(Heap) ->
    -1;
loop(Heap, Dist, Adj, Target) ->
    {Time, Node} = gb_sets:smallest(Heap),
    Heap1 = gb_sets:del_element({Time, Node}, Heap),
    CurrentDist = maps:get(Node, Dist, ?INF),
    if Time > CurrentDist ->
            loop(Heap1, Dist, Adj, Target);
       true ->
            case Node of
                Target -> Time;
                _ ->
                    EdgesFrom = maps:get(Node, Adj, []),
                    {NewHeap, NewDist} = relax_edges(EdgesFrom, Time, Dist, Heap1),
                    loop(NewHeap, NewDist, Adj, Target)
            end
    end.

relax_edges([], _CurTime, Dist, Heap) ->
    {Heap, Dist};
relax_edges([{V,S,E}|Rest], CurTime, Dist, Heap) ->
    if CurTime =< E ->
            NewTime = max(CurTime, S) + 1,
            OldDist = maps:get(V, Dist, ?INF),
            case NewTime < OldDist of
                true ->
                    Dist1 = maps:put(V, NewTime, Dist),
                    Heap1 = gb_sets:add({NewTime, V}, Heap);
                false ->
                    Dist1 = Dist,
                    Heap1 = Heap
            end,
            relax_edges(Rest, CurTime, Dist1, Heap1);
       true ->
            relax_edges(Rest, CurTime, Dist, Heap)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time(n :: integer, edges :: [[integer]]) :: integer
  def min_time(n, edges) do
    adj = Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)

    adj =
      Enum.reduce(edges, adj, fn [u, v, s, e], acc ->
        Map.update!(acc, u, fn lst -> [{v, s, e} | lst] end)
      end)

    inf = 1 <<< 60
    dist = %{0 => 0}
    heap = :gb_sets.add_element({0, 0}, :gb_sets.new())
    result = dijkstra(heap, dist, adj, n - 1, inf)

    case result do
      nil -> -1
      val -> val
    end
  end

  defp dijkstra(heap, dist, adj, target, inf) do
    if :gb_sets.is_empty(heap) do
      Map.get(dist, target)
    else
      {{time, u}, heap2} = :gb_sets.take_smallest(heap)
      cur_dist = Map.get(dist, u)

      if time > cur_dist do
        dijkstra(heap2, dist, adj, target, inf)
      else
        {dist2, heap3} =
          Enum.reduce(adj[u] || [], {dist, heap2}, fn {v, s, e},
                                                    {dacc, hacc} ->
            if time <= e do
              depart = if time < s, do: s, else: time
              arrival = depart + 1
              prev = Map.get(dacc, v, inf)

              if arrival < prev do
                {
                  Map.put(dacc, v, arrival),
                  :gb_sets.add_element({arrival, v}, hacc)
                }
              else
                {dacc, hacc}
              end
            else
              {dacc, hacc}
            end
          end)

        dijkstra(heap3, dist2, adj, target, inf)
      end
    end
  end
end
```

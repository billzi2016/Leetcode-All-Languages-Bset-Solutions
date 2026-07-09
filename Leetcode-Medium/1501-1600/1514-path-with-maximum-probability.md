# 1514. Path with Maximum Probability

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb,
                          int start_node, int end_node) {
        if (start_node == end_node) return 1.0;
        vector<vector<pair<int,double>>> adj(n);
        for (size_t i = 0; i < edges.size(); ++i) {
            int u = edges[i][0], v = edges[i][1];
            double p = succProb[i];
            adj[u].push_back({v, p});
            adj[v].push_back({u, p});
        }
        vector<double> prob(n, 0.0);
        prob[start_node] = 1.0;
        priority_queue<pair<double,int>> pq; // max-heap by probability
        pq.push({1.0, start_node});
        
        while (!pq.empty()) {
            auto [curProb, u] = pq.top();
            pq.pop();
            if (curProb < prob[u]) continue; // outdated entry
            if (u == end_node) return curProb;
            for (auto &e : adj[u]) {
                int v = e.first;
                double newProb = curProb * e.second;
                if (newProb > prob[v] + 1e-12) {
                    prob[v] = newProb;
                    pq.push({newProb, v});
                }
            }
        }
        return 0.0;
    }
};
```

## Java

```java
class Solution {
    private static class Edge {
        int to;
        double prob;
        Edge(int to, double prob) {
            this.to = to;
            this.prob = prob;
        }
    }
    
    private static class State {
        int node;
        double prob;
        State(int node, double prob) {
            this.node = node;
            this.prob = prob;
        }
    }
    
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        if (start_node == end_node) return 1.0;
        
        // Build adjacency list
        List<List<Edge>> graph = new ArrayList<>(n);
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            double p = succProb[i];
            graph.get(a).add(new Edge(b, p));
            graph.get(b).add(new Edge(a, p));
        }
        
        double[] maxProb = new double[n];
        maxProb[start_node] = 1.0;
        
        PriorityQueue<State> pq = new PriorityQueue<>(
            (s1, s2) -> Double.compare(s2.prob, s1.prob) // max-heap based on probability
        );
        pq.offer(new State(start_node, 1.0));
        
        while (!pq.isEmpty()) {
            State cur = pq.poll();
            int u = cur.node;
            double prob = cur.prob;
            
            if (prob < maxProb[u]) continue; // outdated entry
            
            if (u == end_node) return prob;
            
            for (Edge e : graph.get(u)) {
                double newProb = prob * e.prob;
                if (newProb > maxProb[e.to] + 1e-12) { // small epsilon to avoid precision issues
                    maxProb[e.to] = newProb;
                    pq.offer(new State(e.to, newProb));
                }
            }
        }
        
        return 0.0;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        if start_node == end_node:
            return 1.0

        graph = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        heap = [(-1.0, start_node)]  # max-heap using negative probabilities

        while heap:
            cur_neg, node = heapq.heappop(heap)
            cur = -cur_neg
            if node == end_node:
                return cur
            if cur < max_prob[node] - 1e-12:
                continue  # outdated entry
            for nei, w in graph[node]:
                new_prob = cur * w
                if new_prob > max_prob[nei] + 1e-12:
                    max_prob[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return 0.0
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        if start_node == end_node:
            return 1.0

        graph = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        heap = [(-1.0, start_node)]  # max-heap via negative probability

        while heap:
            cur_neg, node = heapq.heappop(heap)
            cur = -cur_neg
            if node == end_node:
                return cur
            if cur < max_prob[node] - 1e-12:
                continue  # outdated entry
            for nei, w in graph[node]:
                new_prob = cur * w
                if new_prob > max_prob[nei] + 1e-12:
                    max_prob[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return 0.0
```

## C

```c
#include <stdlib.h>

typedef struct {
    int to;
    double prob;
    int next;
} AdjEdge;

typedef struct {
    int node;
    double prob;
} HeapNode;

/* Max-heap functions */
static void heap_swap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heap_push(HeapNode **heap, int *size, int *capacity, int node, double prob) {
    if (*size + 1 >= *capacity) {
        *capacity = (*capacity == 0) ? 64 : (*capacity * 2);
        *heap = (HeapNode *)realloc(*heap, (*capacity) * sizeof(HeapNode));
    }
    int i = ++(*size);
    (*heap)[i].node = node;
    (*heap)[i].prob = prob;
    while (i > 1 && (*heap)[i].prob > (*heap)[i / 2].prob) {
        heap_swap(&(*heap)[i], &(*heap)[i / 2]);
        i /= 2;
    }
}

static HeapNode heap_pop(HeapNode *heap, int *size) {
    HeapNode top = heap[1];
    heap[1] = heap[*size];
    (*size)--;
    int i = 1;
    while (1) {
        int left = i * 2;
        int right = left + 1;
        if (left > *size) break;
        int largest = left;
        if (right <= *size && heap[right].prob > heap[left].prob)
            largest = right;
        if (heap[i].prob >= heap[largest].prob) break;
        heap_swap(&heap[i], &heap[largest]);
        i = largest;
    }
    return top;
}

double maxProbability(int n, int** edges, int edgesSize, int* edgesColSize,
                      double* succProb, int succProbSize,
                      int start_node, int end_node) {
    if (start_node == end_node) return 1.0;

    /* Build adjacency list */
    int totalAdj = edgesSize * 2;
    AdjEdge *adj = (AdjEdge *)malloc(totalAdj * sizeof(AdjEdge));
    int *head = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;

    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        double p = succProb[i];

        int idx = i * 2;
        adj[idx].to = b;
        adj[idx].prob = p;
        adj[idx].next = head[a];
        head[a] = idx;

        adj[idx + 1].to = a;
        adj[idx + 1].prob = p;
        adj[idx + 1].next = head[b];
        head[b] = idx + 1;
    }

    /* Dijkstra with max-heap */
    double *dist = (double *)calloc(n, sizeof(double));
    dist[start_node] = 1.0;

    HeapNode *heap = NULL;
    int heapSize = 0, heapCap = 0;
    heap_push(&heap, &heapSize, &heapCap, start_node, 1.0);

    while (heapSize > 0) {
        HeapNode cur = heap_pop(heap, &heapSize);
        int u = cur.node;
        double probU = cur.prob;

        if (probU < dist[u]) continue;          // outdated entry
        if (u == end_node) break;

        for (int e = head[u]; e != -1; e = adj[e].next) {
            int v = adj[e].to;
            double newProb = probU * adj[e].prob;
            if (newProb > dist[v]) {
                dist[v] = newProb;
                heap_push(&heap, &heapSize, &heapCap, v, newProb);
            }
        }
    }

    double result = dist[end_node];
    free(dist);
    free(adj);
    free(head);
    free(heap);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public double MaxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        var graph = new List<(int to, double prob)>[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new List<(int, double)>();
        }
        for (int i = 0; i < edges.Length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            double p = succProb[i];
            graph[a].Add((b, p));
            graph[b].Add((a, p));
        }

        var maxProb = new double[n];
        maxProb[start_node] = 1.0;

        var pq = new PriorityQueue<int, double>();
        pq.Enqueue(start_node, -1.0); // use negative for max-heap behavior

        while (pq.Count > 0) {
            int cur = pq.Dequeue();
            if (cur == end_node) return maxProb[end_node];

            double curProb = maxProb[cur];
            foreach (var edge in graph[cur]) {
                int nxt = edge.to;
                double newProb = curProb * edge.prob;
                if (newProb > maxProb[nxt] + 1e-12) {
                    maxProb[nxt] = newProb;
                    pq.Enqueue(nxt, -newProb);
                }
            }
        }

        return 0.0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} succProb
 * @param {number} start_node
 * @param {number} end_node
 * @return {number}
 */
var maxProbability = function(n, edges, succProb, start_node, end_node) {
    if (start_node === end_node) return 1.0;

    // Build adjacency list
    const graph = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; ++i) {
        const [u, v] = edges[i];
        const p = succProb[i];
        graph[u].push([v, p]);
        graph[v].push([u, p]);
    }

    // Max-heap priority queue
    class MaxHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(item) {
            const h = this.heap;
            h.push(item);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p][0] >= h[i][0]) break;
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
                    let left = i * 2 + 1;
                    let right = left + 1;
                    let largest = i;
                    if (left < h.length && h[left][0] > h[largest][0]) largest = left;
                    if (right < h.length && h[right][0] > h[largest][0]) largest = right;
                    if (largest === i) break;
                    [h[i], h[largest]] = [h[largest], h[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    const maxProb = new Array(n).fill(0);
    maxProb[start_node] = 1.0;

    const pq = new MaxHeap();
    pq.push([1.0, start_node]);

    while (pq.size() > 0) {
        const [prob, u] = pq.pop();
        if (prob < maxProb[u]) continue; // outdated entry
        if (u === end_node) return prob;
        for (const [v, edgeP] of graph[u]) {
            const newProb = prob * edgeP;
            if (newProb > maxProb[v] + 1e-12) {
                maxProb[v] = newProb;
                pq.push([newProb, v]);
            }
        }
    }

    return maxProb[end_node];
};
```

## Typescript

```typescript
function maxProbability(n: number, edges: number[][], succProb: number[], start_node: number, end_node: number): number {
    const graph: Array<Array<[number, number]>> = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; i++) {
        const [u, v] = edges[i];
        const p = succProb[i];
        graph[u].push([v, p]);
        graph[v].push([u, p]);
    }

    class MaxHeap {
        heap: Array<[number, number]> = [];
        size() { return this.heap.length; }
        push(item: [number, number]) {
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
        private bubbleUp(idx: number) {
            while (idx > 0) {
                const parent = Math.floor((idx - 1) / 2);
                if (this.heap[parent][0] >= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        private bubbleDown(idx: number) {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let largest = idx;
                if (left < n && this.heap[left][0] > this.heap[largest][0]) largest = left;
                if (right < n && this.heap[right][0] > this.heap[largest][0]) largest = right;
                if (largest === idx) break;
                [this.heap[idx], this.heap[largest]] = [this.heap[largest], this.heap[idx]];
                idx = largest;
            }
        }
    }

    const probArr = new Array(n).fill(0);
    probArr[start_node] = 1;

    const pq = new MaxHeap();
    pq.push([1, start_node]);

    while (pq.size() > 0) {
        const [curProb, node] = pq.pop()!;
        if (node === end_node) return curProb;
        if (curProb < probArr[node]) continue;

        for (const [nbr, edgeP] of graph[node]) {
            const newProb = curProb * edgeP;
            if (newProb > probArr[nbr]) {
                probArr[nbr] = newProb;
                pq.push([newProb, nbr]);
            }
        }
    }

    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Float[] $succProb
     * @param Integer $start_node
     * @param Integer $end_node
     * @return Float
     */
    function maxProbability($n, $edges, $succProb, $start_node, $end_node) {
        // Build adjacency list
        $graph = array_fill(0, $n, []);
        foreach ($edges as $i => $e) {
            $a = $e[0];
            $b = $e[1];
            $p = $succProb[$i];
            $graph[$a][] = [$b, $p];
            $graph[$b][] = [$a, $p];
        }

        // Probabilities to reach each node
        $prob = array_fill(0, $n, 0.0);
        $prob[$start_node] = 1.0;

        // Max-heap priority queue (higher probability first)
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert($start_node, 1.0);

        while (!$pq->isEmpty()) {
            $curr = $pq->extract(); // ['data'=>node,'priority'=>prob]
            $node = $curr['data'];
            $curProb = $curr['priority'];

            if ($node === $end_node) {
                return $curProb;
            }

            // Skip outdated entries
            if ($curProb < $prob[$node] - 1e-12) {
                continue;
            }

            foreach ($graph[$node] as $neighbor) {
                [$next, $edgeP] = $neighbor;
                $newProb = $curProb * $edgeP;
                if ($newProb > $prob[$next] + 1e-12) {
                    $prob[$next] = $newProb;
                    $pq->insert($next, $newProb);
                }
            }
        }

        return $prob[$end_node];
    }
}
```

## Swift

```swift
import Foundation

struct MaxHeap {
    private var data: [(prob: Double, node: Int)] = []
    
    var isEmpty: Bool { data.isEmpty }
    
    mutating func push(_ element: (Double, Int)) {
        data.append((element.0, element.1))
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> (Double, Int) {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return (top.prob, top.node)
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[child].prob > data[parent].prob {
                data.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var largest = parent
            if left < data.count && data[left].prob > data[largest].prob {
                largest = left
            }
            if right < data.count && data[right].prob > data[largest].prob {
                largest = right
            }
            if largest == parent { break }
            data.swapAt(parent, largest)
            parent = largest
        }
    }
}

class Solution {
    func maxProbability(_ n: Int, _ edges: [[Int]], _ succProb: [Double], _ start_node: Int, _ end_node: Int) -> Double {
        var graph = Array(repeating: [(Int, Double)](), count: n)
        for i in 0..<edges.count {
            let a = edges[i][0]
            let b = edges[i][1]
            let p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))
        }
        
        var maxProb = Array(repeating: 0.0, count: n)
        maxProb[start_node] = 1.0
        
        var heap = MaxHeap()
        heap.push((1.0, start_node))
        
        while !heap.isEmpty {
            let (prob, node) = heap.pop()
            if prob < maxProb[node] { continue } // outdated entry
            if node == end_node { return prob }
            
            for (next, edgeProb) in graph[node] {
                let newProb = prob * edgeProb
                if newProb > maxProb[next] + 1e-12 {
                    maxProb[next] = newProb
                    heap.push((newProb, next))
                }
            }
        }
        
        return 0.0
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    fun maxProbability(
        n: Int,
        edges: Array<IntArray>,
        succProb: DoubleArray,
        start_node: Int,
        end_node: Int
    ): Double {
        if (start_node == end_node) return 1.0
        val graph = Array(n) { mutableListOf<Pair<Int, Double>>() }
        for (i in edges.indices) {
            val a = edges[i][0]
            val b = edges[i][1]
            val p = succProb[i]
            graph[a].add(Pair(b, p))
            graph[b].add(Pair(a, p))
        }

        val prob = DoubleArray(n) { 0.0 }
        prob[start_node] = 1.0

        data class State(val node: Int, val prob: Double)

        val pq = PriorityQueue<State>(compareByDescending { it.prob })
        pq.offer(State(start_node, 1.0))

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.node == end_node) return cur.prob
            if (cur.prob < prob[cur.node] - 1e-12) continue
            for ((next, edgeProb) in graph[cur.node]) {
                val newProb = cur.prob * edgeProb
                if (newProb > prob[next] + 1e-12) {
                    prob[next] = newProb
                    pq.offer(State(next, newProb))
                }
            }
        }

        return 0.0
    }
}
```

## Dart

```dart
class Solution {
  double maxProbability(int n, List<List<int>> edges, List<double> succProb,
      int start_node, int end_node) {
    // Build adjacency list
    List<List<_Edge>> graph = List.generate(n, (_) => []);
    for (int i = 0; i < edges.length; i++) {
      int a = edges[i][0];
      int b = edges[i][1];
      double p = succProb[i];
      graph[a].add(_Edge(b, p));
      graph[b].add(_Edge(a, p));
    }

    // Max probability to each node
    List<double> maxProb = List.filled(n, 0.0);
    maxProb[start_node] = 1.0;

    // Max-heap implementation
    List<_Node> heap = [];

    void push(_Node node) {
      heap.add(node);
      int i = heap.length - 1;
      while (i > 0) {
        int parent = (i - 1) >> 1;
        if (heap[parent].prob >= heap[i].prob) break;
        var tmp = heap[parent];
        heap[parent] = heap[i];
        heap[i] = tmp;
        i = parent;
      }
    }

    _Node pop() {
      var top = heap[0];
      var last = heap.removeLast();
      if (heap.isNotEmpty) {
        heap[0] = last;
        int i = 0;
        while (true) {
          int left = i * 2 + 1;
          int right = left + 1;
          int largest = i;
          if (left < heap.length && heap[left].prob > heap[largest].prob)
            largest = left;
          if (right < heap.length && heap[right].prob > heap[largest].prob)
            largest = right;
          if (largest == i) break;
          var tmp = heap[i];
          heap[i] = heap[largest];
          heap[largest] = tmp;
          i = largest;
        }
      }
      return top;
    }

    push(_Node(start_node, 1.0));

    while (heap.isNotEmpty) {
      var cur = pop();
      int u = cur.v;
      double prob = cur.prob;

      if (prob < maxProb[u]) continue; // outdated entry
      if (u == end_node) return prob;

      for (var e in graph[u]) {
        double newProb = prob * e.prob;
        if (newProb > maxProb[e.to] + 1e-12) {
          maxProb[e.to] = newProb;
          push(_Node(e.to, newProb));
        }
      }
    }

    return maxProb[end_node];
  }
}

class _Edge {
  int to;
  double prob;
  _Edge(this.to, this.prob);
}

class _Node {
  int v;
  double prob;
  _Node(this.v, this.prob);
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type edge struct {
	to   int
	prob float64
}

type item struct {
	node int
	prob float64
}

// maxHeap implements a priority queue where the highest probability has highest priority.
type maxHeap []item

func (h maxHeap) Len() int { return len(h) }
func (h maxHeap) Less(i, j int) bool {
	// we want larger prob first
	return h[i].prob > h[j].prob
}
func (h maxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(item))
}

func (h *mut) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// Since we need a pointer receiver for Pop, define a type alias.
type mut maxHeap

func (h *mut) Push(x interface{}) {
	*h = append(*h, x.(item))
}
func (h *mut) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// maxProbability finds the maximum success probability from start_node to end_node.
func maxProbability(n int, edges [][]int, succProb []float64, start_node int, end_node int) float64 {
	if n == 0 {
		return 0.0
	}
	graph := make([][]edge, n)
	for i, e := range edges {
		u, v := e[0], e[1]
		p := succProb[i]
		graph[u] = append(graph[u], edge{to: v, prob: p})
		graph[v] = append(graph[v], edge{to: u, prob: p})
	}

	probTo := make([]float64, n)
	for i := range probTo {
		probTo[i] = 0.0
	}
	probTo[start_node] = 1.0

	h := &mut{}
	heap.Init(h)
	heap.Push(h, item{node: start_node, prob: 1.0})

	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		if cur.node == end_node {
			return cur.prob
		}
		// Skip if we have already found a better probability for this node.
		if cur.prob < probTo[cur.node] {
			continue
		}
		for _, nb := range graph[cur.node] {
			newProb := cur.prob * nb.prob
			if newProb > probTo[nb.to] {
				probTo[nb.to] = newProb
				heap.Push(h, item{node: nb.to, prob: newProb})
			}
		}
	}
	return 0.0
}
```

## Ruby

```ruby
def heap_push(heap, item)
  heap << item
  i = heap.size - 1
  while i > 0
    p = (i - 1) / 2
    break if heap[p][0] >= heap[i][0]
    heap[p], heap[i] = heap[i], heap[p]
    i = p
  end
end

def heap_pop(heap)
  return nil if heap.empty?
  top = heap[0]
  last = heap.pop
  unless heap.empty?
    heap[0] = last
    i = 0
    size = heap.size
    loop do
      l = i * 2 + 1
      r = l + 1
      break if l >= size
      child = (r < size && heap[r][0] > heap[l][0]) ? r : l
      break if heap[i][0] >= heap[child][0]
      heap[i], heap[child] = heap[child], heap[i]
      i = child
    end
  end
  top
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Float[]} succ_prob
# @param {Integer} start_node
# @param {Integer} end_node
# @return {Float}
def max_probability(n, edges, succ_prob, start_node, end_node)
  return 1.0 if start_node == end_node

  graph = Array.new(n) { [] }
  edges.each_with_index do |(a, b), idx|
    p = succ_prob[idx]
    graph[a] << [b, p]
    graph[b] << [a, p]
  end

  max_prob = Array.new(n, 0.0)
  max_prob[start_node] = 1.0

  heap = []
  heap_push(heap, [1.0, start_node])

  while (item = heap_pop(heap))
    prob, node = item
    next if prob < max_prob[node] - 1e-12
    return prob if node == end_node

    graph[node].each do |nbr, edge_p|
      new_prob = prob * edge_p
      if new_prob > max_prob[nbr] + 1e-12
        max_prob[nbr] = new_prob
        heap_push(heap, [new_prob, nbr])
      end
    end
  end

  0.0
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, PriorityQueue}

  case class State(prob: Double, node: Int)

  def maxProbability(
      n: Int,
      edges: Array[Array[Int]],
      succProb: Array[Double],
      start_node: Int,
      end_node: Int
  ): Double = {
    if (start_node == end_node) return 1.0

    val graph = Array.fill(n)(new ArrayBuffer[(Int, Double)]())
    for (i <- edges.indices) {
      val a = edges(i)(0)
      val b = edges(i)(1)
      val p = succProb(i)
      graph(a).append((b, p))
      graph(b).append((a, p))
    }

    val maxProb = Array.fill[Double](n)(0.0)
    maxProb(start_node) = 1.0

    implicit val ord: Ordering[State] = Ordering.by[State, Double](_.prob)
    val pq = PriorityQueue.empty[State]

    pq.enqueue(State(1.0, start_node))

    while (pq.nonEmpty) {
      val cur = pq.dequeue()
      if (cur.node == end_node) return cur.prob
      if (cur.prob < maxProb(cur.node)) {
        // outdated entry
      } else {
        for ((nbr, edgeP) <- graph(cur.node)) {
          val newProb = cur.prob * edgeP
          if (newProb > maxProb(nbr) + 1e-12) {
            maxProb(nbr) = newProb
            pq.enqueue(State(newProb, nbr))
          }
        }
      }
    }

    maxProb(end_node)
  }
}
```

## Rust

```rust
use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Copy, Clone)]
struct State {
    prob: f64,
    position: usize,
}

impl PartialEq for State {
    fn eq(&self, other: &Self) -> bool {
        self.prob == other.prob && self.position == other.position
    }
}
impl Eq for State {}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        // larger probability should be considered greater for max‑heap
        self.prob.partial_cmp(&other.prob)
    }
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap()
    }
}

impl Solution {
    pub fn max_probability(
        n: i32,
        edges: Vec<Vec<i32>>,
        succ_prob: Vec<f64>,
        start_node: i32,
        end_node: i32,
    ) -> f64 {
        let n_usize = n as usize;
        let start = start_node as usize;
        let end = end_node as usize;

        if start == end {
            return 1.0;
        }

        // Build adjacency list
        let mut graph: Vec<Vec<(usize, f64)>> = vec![Vec::new(); n_usize];
        for (i, e) in edges.iter().enumerate() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            let p = succ_prob[i];
            graph[a].push((b, p));
            graph[b].push((a, p));
        }

        // Dijkstra-like max probability
        let mut best: Vec<f64> = vec![0.0; n_usize];
        best[start] = 1.0;

        let mut heap = BinaryHeap::new();
        heap.push(State { prob: 1.0, position: start });

        while let Some(State { prob, position }) = heap.pop() {
            if prob < best[position] - 1e-12 {
                continue; // outdated entry
            }
            if position == end {
                return prob;
            }
            for &(next, edge_p) in &graph[position] {
                let new_prob = prob * edge_p;
                if new_prob > best[next] + 1e-12 {
                    best[next] = new_prob;
                    heap.push(State { prob: new_prob, position: next });
                }
            }
        }

        0.0
    }
}
```

## Racket

```racket
#lang racket
(require racket/priority-queue)

(define/contract (max-probability n edges succProb start_node end_node)
  (-> exact-integer? (listof (listof exact-integer?)) (listof flonum?) exact-integer? exact-integer? flonum?)
  (let* ((adj (make-vector n '()))
         (len (length edges)))
    (for ([i (in-range len)])
      (let* ((e (list-ref edges i))
             (a (first e))
             (b (second e))
             (p (list-ref succProb i)))
        (vector-set! adj a (cons (cons b p) (vector-ref adj a)))
        (vector-set! adj b (cons (cons a p) (vector-ref adj b)))))
    (define max-prob (make-vector n 0.0))
    (vector-set! max-prob start_node 1.0)
    (define pq (make-pq >))
    (pq-add! pq 1.0 start_node)
    (let recur ()
      (cond
        [(zero? (pq-count pq)) (vector-ref max-prob end_node)]
        [else
         (define top (pq-pop! pq))
         (define prob (first top))
         (define node (second top))
         (if (< prob (vector-ref max-prob node))
             (recur)
             (if (= node end_node)
                 prob
                 (begin
                   (for ([nbr-pair (in-list (vector-ref adj node))])
                     (define nbr (car nbr-pair))
                     (define edgep (cdr nbr-pair))
                     (define newp (* prob edgep))
                     (when (> newp (vector-ref max-prob nbr))
                       (pq-add! pq newp nbr)))
                   (recur))))])))))
```

## Erlang

```erlang
-module(solution).
-export([max_probability/5]).

-spec max_probability(N :: integer(), Edges :: [[integer()]], SuccProb :: [float()], Start_node :: integer(), End_node :: integer()) -> float().
max_probability(N, Edges, SuccProb, Start_node, End_node) ->
    Adj0 = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    Adj = build_adj(lists:zip(Edges, SuccProb), Adj0),
    MaxMap0 = maps:put(Start_node, 1.0, maps:new()),
    Tree0 = gb_trees:empty(),
    {Tree1, Counter1} = heap_push(Tree0, 0, 1.0, Start_node),
    dijkstra(Adj, MaxMap0, End_node, Tree1, Counter1).

%% Build adjacency list
build_adj(Pairs, Adj) ->
    lists:foldl(fun({Edge, P}, Acc) ->
        [A, B] = Edge,
        L1 = maps:get(A, Acc),
        L2 = maps:get(B, Acc),
        Acc1 = maps:put(A, [{B, P} | L1], Acc),
        maps:put(B, [{A, P} | L2], Acc1)
    end, Adj, Pairs).

%% Dijkstra main loop
dijkstra(_Adj, MaxMap, End_node, Tree, _Counter) when gb_trees:is_empty(Tree) ->
    0.0;
dijkstra(Adj, MaxMap, End_node, Tree, Counter) ->
    {Prob, Node, NewTree} = heap_pop(Tree),
    Stored = maps:get(Node, MaxMap, 0.0),
    case Prob < Stored of
        true ->
            dijkstra(Adj, MaxMap, End_node, NewTree, Counter);
        false ->
            case Node of
                End_node -> Prob;
                _ ->
                    {NewMaxMap, UpdatedTree, NewCounter} = relax_neighbors(Node, Prob, Adj, MaxMap, NewTree, Counter),
                    dijkstra(Adj, NewMaxMap, End_node, UpdatedTree, NewCounter)
            end
    end.

%% Relax edges from current node
relax_neighbors(_Node, _ProbNode, _Adj, MaxMap, Tree, Counter) ->
    {MaxMap, Tree, Counter}.
relax_neighbors(Node, ProbNode, Adj, MaxMap, Tree, Counter) ->
    Neighbors = maps:get(Node, Adj),
    lists:foldl(fun({Nb, EdgeProb}, {MMap, T, C}) ->
        NewProb = ProbNode * EdgeProb,
        OldProb = maps:get(Nb, MMap, 0.0),
        if
            NewProb > OldProb ->
                MMap2 = maps:put(Nb, NewProb, MMap),
                {T2, C2} = heap_push(T, C, NewProb, Nb),
                {MMap2, T2, C2};
            true ->
                {MMap, T, C}
        end
    end, {MaxMap, Tree, Counter}, Neighbors).

%% Heap operations using gb_trees as a max‑heap (negative probability as key)
heap_push(Tree, Counter, Prob, Node) ->
    Key = {-Prob, Counter},
    NewTree = gb_trees:insert(Key, Node, Tree),
    {NewTree, Counter + 1}.

heap_pop(Tree) ->
    {{NegProb, _Cnt}, Node} = gb_trees:smallest(Tree),
    NewTree = gb_trees:delete_smallest(Tree),
    { -NegProb, Node, NewTree }.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_probability(
          n :: integer,
          edges :: [[integer]],
          succ_prob :: [float],
          start_node :: integer,
          end_node :: integer
        ) :: float
  def max_probability(n, edges, succ_prob, start_node, end_node) do
    adj = build_adj(edges, succ_prob)

    probs =
      :array.from_list(
        Enum.map(0..(n - 1), fn _ -> 0.0 end)
      )
      |> :array.set(start_node, 1.0)

    tree =
      :gb_trees.empty()
      |> :gb_trees.insert({-1.0, start_node}, {start_node, 1.0})

    dijkstra(tree, adj, probs, end_node)
  end

  defp build_adj(edges, succ_prob) do
    Enum.reduce(Enum.zip(edges, succ_prob), %{}, fn {{a, b}, p}, acc ->
      acc
      |> Map.update(a, [{b, p}], fn list -> [{b, p} | list] end)
      |> Map.update(b, [{a, p}], fn list -> [{a, p} | list] end)
    end)
  end

  defp dijkstra(tree, adj, probs, target) do
    if :gb_trees.is_empty(tree) do
      :array.get(target, probs)
    else
      {{neg_prob, node}, {^node, prob}, rest_tree} = :gb_trees.take_smallest(tree)

      current_best = :array.get(node, probs)

      # skip outdated entry
      if prob < current_best - 1.0e-12 do
        dijkstra(rest_tree, adj, probs, target)
      else
        if node == target do
          prob
        else
          {new_tree, new_probs} =
            Enum.reduce(Map.get(adj, node, []), {rest_tree, probs}, fn {nbr, edge_p},
                                                                      {t_acc, p_acc} ->
              new_prob = prob * edge_p

              if new_prob > :array.get(nbr, p_acc) + 1.0e-12 do
                updated_probs = :array.set(nbr, new_prob, p_acc)
                updated_tree = :gb_trees.insert({-new_prob, nbr}, {nbr, new_prob}, t_acc)
                {updated_tree, updated_probs}
              else
                {t_acc, p_acc}
              end
            end)

          dijkstra(new_tree, adj, new_probs, target)
        end
      end
    end
  end
end
```

# 2045. Second Minimum Time to Reach Destination

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        vector<vector<int>> adj(n + 1);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        const long long INF = LLONG_MAX / 4;
        vector<long long> dist1(n + 1, INF), dist2(n + 1, INF);
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        dist1[1] = 0;
        pq.emplace(0, 1);
        
        auto nextTime = [&](long long cur) -> long long {
            long long cycles = cur / change;
            if (cycles % 2 == 1) { // red
                cur = (cycles + 1) * change;
            }
            return cur + time;
        };
        
        while (!pq.empty()) {
            auto [t, u] = pq.top(); pq.pop();
            if (t > dist2[u]) continue; // already have better two times
            
            for (int v : adj[u]) {
                long long nt = nextTime(t);
                
                if (nt < dist1[v]) {
                    dist2[v] = dist1[v];
                    dist1[v] = nt;
                    pq.emplace(nt, v);
                } else if (nt > dist1[v] && nt < dist2[v]) {
                    dist2[v] = nt;
                    pq.emplace(nt, v);
                }
            }
        }
        return static_cast<int>(dist2[n]);
    }
};
```

## Java

```java
class Solution {
    public int secondMinimum(int n, int[][] edges, int time, int change) {
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0L, 1});
        int[] cnt = new int[n + 1];

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            long curTime = cur[0];
            int u = (int) cur[1];

            if (cnt[u] >= 2) continue;
            cnt[u]++;

            if (u == n && cnt[u] == 2) return (int) curTime;

            for (int v : graph[u]) {
                long depart = curTime;
                long cycles = depart / change;
                if ((cycles & 1L) == 1L) { // red light, wait for next green
                    depart = (cycles + 1) * change;
                }
                long arrival = depart + time;
                pq.offer(new long[]{arrival, v});
            }
        }

        return -1; // should never reach here per problem guarantees
    }
}
```

## Python

```python
class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        from heapq import heappush, heappop

        # build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def next_time(t):
            # wait if current signal is red
            if (t // change) % 2 == 1:
                t = (t // change + 1) * change
            return t + time

        # dist[node] stores up to two distinct smallest arrival times
        dist = [[] for _ in range(n + 1)]
        heap = [(0, 1)]  # (time, node)

        while heap:
            cur_time, u = heappop(heap)

            # if we already have two times and this one is larger than the second, skip
            if len(dist[u]) == 2 and cur_time > dist[u][1]:
                continue

            # record distinct time
            if not dist[u] or cur_time != dist[u][-1]:
                dist[u].append(cur_time)

            # we only need first two times per node
            if len(dist[u]) > 2:
                continue

            # if destination reached second time, answer found
            if u == n and len(dist[u]) == 2:
                return dist[n][1]

            for v in adj[u]:
                nxt = next_time(cur_time)
                heappush(heap, (nxt, v))

        # problem guarantees a solution exists
        return -1
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        heap = [(0, 1)]  # (current_time, node)
        cnt = [0] * (n + 1)  # how many times each node has been popped

        while heap:
            cur, node = heapq.heappop(heap)
            cnt[node] += 1
            if node == n and cnt[n] == 2:
                return cur
            if cnt[node] > 2:
                continue
            for nb in graph[node]:
                nxt = cur
                # wait if the signal is red
                if (nxt // change) % 2 == 1:
                    nxt = (nxt // change + 1) * change
                nxt += time
                heapq.heappush(heap, (nxt, nb))
        return -1
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int node;
    int time;
} HeapNode;

static void heapSwap(HeapNode *a, HeapNode *b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapNode **heap, int *sz, int *cap, HeapNode val) {
    if (*sz >= *cap) {
        *cap = (*cap == 0) ? 64 : (*cap * 2);
        *heap = (HeapNode *)realloc(*heap, (*cap) * sizeof(HeapNode));
    }
    int i = (*sz)++;
    (*heap)[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if ((*heap)[p].time <= (*heap)[i].time) break;
        heapSwap(&(*heap)[p], &(*heap)[i]);
        i = p;
    }
}

static HeapNode heapPop(HeapNode *heap, int *sz) {
    HeapNode ret = heap[0];
    heap[0] = heap[--(*sz)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = l + 1, smallest = i;
        if (l < *sz && heap[l].time < heap[smallest].time) smallest = l;
        if (r < *sz && heap[r].time < heap[smallest].time) smallest = r;
        if (smallest == i) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return ret;
}

int secondMinimum(int n, int** edges, int edgesSize, int* edgesColSize, int time, int change) {
    // degree count
    int *deg = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }
    // allocate adjacency lists
    int **adj = (int **)malloc((n + 1) * sizeof(int *));
    for (int i = 1; i <= n; ++i) {
        adj[i] = (int *)malloc(deg[i] * sizeof(int));
    }
    int *idx = (int *)calloc(n + 1, sizeof(int));
    // fill adjacency
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][idx[u]++] = v;
        adj[v][idx[v]++] = u;
    }
    free(idx);
    // Dijkstra-like with up to two visits per node
    int *cnt = (int *)calloc(n + 1, sizeof(int));
    HeapNode *heap = NULL;
    int heapSize = 0, heapCap = 0;
    heapPush(&heap, &heapSize, &heapCap, (HeapNode){1, 0});
    while (heapSize) {
        HeapNode cur = heapPop(heap, &heapSize);
        int u = cur.node;
        int t = cur.time;
        if (cnt[u] >= 2) continue;
        cnt[u]++;
        if (u == n && cnt[u] == 2) {
            // clean up
            for (int i = 1; i <= n; ++i) free(adj[i]);
            free(adj);
            free(deg);
            free(cnt);
            free(heap);
            return t;
        }
        for (int i = 0; i < deg[u]; ++i) {
            int v = adj[u][i];
            int nt = t;
            int cycles = nt / change;
            if (cycles % 2 == 1) {
                nt = (cycles + 1) * change;
            }
            nt += time;
            heapPush(&heap, &heapSize, &heapCap, (HeapNode){v, nt});
        }
    }
    // Should never reach here per problem guarantees
    for (int i = 1; i <= n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(cnt);
    free(heap);
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int SecondMinimum(int n, int[][] edges, int time, int change) {
        var graph = new List<int>[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            graph[u].Add(v);
            graph[v].Add(u);
        }

        var pq = new PriorityQueue<(int node, int time), int>();
        pq.Enqueue((1, 0), 0);

        int[] visited = new int[n + 1];

        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int u = cur.node;
            int t = cur.time;

            visited[u]++;
            if (u == n && visited[u] == 2) return t;
            if (visited[u] > 2) continue; // already processed two shortest arrivals

            foreach (int v in graph[u]) {
                int depart = t;
                int mod = depart % (2 * change);
                if (mod >= change) {
                    depart += (2 * change - mod); // wait for green
                }
                int newTime = depart + time;
                pq.Enqueue((v, newTime), newTime);
            }
        }

        return -1; // should never reach here per problem guarantees
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} time
 * @param {number} change
 * @return {number}
 */
var secondMinimum = function(n, edges, time, change) {
    // Build adjacency list
    const adj = Array.from({length: n + 1}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // Distance arrays: dist[node][0] = shortest, dist[node][1] = second shortest
    const INF = Number.MAX_SAFE_INTEGER;
    const dist = Array.from({length: n + 1}, () => [INF, INF]);
    dist[1][0] = 0;

    // Min-heap implementation
    class MinHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(item) {
            this.heap.push(item);
            this._siftUp(this.heap.length - 1);
        }
        pop() {
            if (this.heap.length === 0) return null;
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
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        _siftDown(idx) {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let smallest = idx;
                if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const pq = new MinHeap();
    pq.push([0, 1]);

    while (pq.size() > 0) {
        const [curTime, u] = pq.pop();

        // If this time is larger than the second best known for u, skip
        if (curTime > dist[u][1]) continue;

        // If we have reached destination with its second shortest time, return it
        if (u === n && curTime === dist[n][1]) {
            return curTime;
        }

        for (const v of adj[u]) {
            let depart = curTime;
            const cycles = Math.floor(depart / change);
            if (cycles % 2 === 1) { // red light, wait for next green
                depart = (cycles + 1) * change;
            }
            const arrival = depart + time;

            if (arrival < dist[v][0]) {
                // shift current shortest to second shortest
                dist[v][1] = dist[v][0];
                dist[v][0] = arrival;
                pq.push([arrival, v]);
            } else if (arrival > dist[v][0] && arrival < dist[v][1]) {
                dist[v][1] = arrival;
                pq.push([arrival, v]);
            }
        }
    }

    // Fallback (should not happen with given constraints)
    return dist[n][1];
};
```

## Typescript

```typescript
function secondMinimum(n: number, edges: number[][], time: number, change: number): number {
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

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

                if (left < length && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < length && this.heap[right][0] < this.heap[smallest][0]) smallest = right;

                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
    }

    const heap = new MinHeap();
    heap.push([0, 1]); // [time, node]

    const cnt: number[] = Array(n + 1).fill(0);

    while (heap.size() > 0) {
        const cur = heap.pop()!;
        let curTime = cur[0];
        const u = cur[1];

        if (cnt[u] >= 2) continue;
        cnt[u]++;

        if (u === n && cnt[n] === 2) return curTime;

        for (const v of adj[u]) {
            // compute earliest departure time from u
            let depart = curTime;
            const cycles = Math.floor(depart / change);
            if (cycles % 2 === 1) {
                depart = (cycles + 1) * change;
            }
            const arrive = depart + time;
            heap.push([arrive, v]);
        }
    }

    return -1; // should never reach here per problem guarantees
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $time
     * @param Integer $change
     * @return Integer
     */
    function secondMinimum($n, $edges, $time, $change) {
        // Build adjacency list
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        // Count how many times each node has been popped (max 2)
        $cnt = array_fill(0, $n + 1, 0);

        // Min-heap using SplPriorityQueue (store negative distance as priority)
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert([1, 0], 0); // node 1 at time 0

        while (!$pq->isEmpty()) {
            $elem = $pq->extract(); // ['data'=>[node, dist], 'priority'=>...]
            $node = $elem['data'][0];
            $curDist = $elem['data'][1];

            if ($cnt[$node] >= 2) {
                continue;
            }
            $cnt[$node]++;

            if ($node == $n && $cnt[$node] == 2) {
                return $curDist;
            }

            foreach ($adj[$node] as $nei) {
                if ($cnt[$nei] >= 2) {
                    continue;
                }

                // Determine waiting time based on traffic lights
                $period = intdiv($curDist, $change);
                if ($period % 2 == 1) { // red light
                    $wait = $change - ($curDist % $change);
                    $nextDist = $curDist + $wait + $time;
                } else { // green light
                    $nextDist = $curDist + $time;
                }

                $pq->insert([$nei, $nextDist], -$nextDist);
            }
        }

        return 0; // Should never reach here for valid inputs
    }
}
```

## Swift

```swift
class Solution {
    func secondMinimum(_ n: Int, _ edges: [[Int]], _ time: Int, _ change: Int) -> Int {
        var adj = Array(repeating: [Int](), count: n + 1)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        
        var dist1 = Array(repeating: Int.max, count: n + 1)
        var dist2 = Array(repeating: Int.max, count: n + 1)
        dist1[1] = 0
        
        var heap = MinHeap()
        heap.push((0, 1))
        
        while let (curTime, u) = heap.pop() {
            if curTime > dist2[u] { continue }
            
            for v in adj[u] {
                // determine departure time from u
                let cycles = curTime / change
                var depart: Int
                if cycles % 2 == 0 {
                    depart = curTime
                } else {
                    depart = (cycles + 1) * change
                }
                let newTime = depart + time
                
                if newTime < dist1[v] {
                    dist2[v] = dist1[v]
                    dist1[v] = newTime
                    heap.push((newTime, v))
                } else if newTime > dist1[v] && newTime < dist2[v] {
                    dist2[v] = newTime
                    heap.push((newTime, v))
                }
            }
        }
        
        return dist2[n]
    }
}

// Simple binary min-heap for (Int time, Int node) pairs
struct MinHeap {
    private var data: [(Int, Int)] = []
    
    mutating func push(_ element: (Int, Int)) {
        data.append(element)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> (Int, Int)? {
        guard !data.isEmpty else { return nil }
        if data.count == 1 {
            return data.removeLast()
        }
        let top = data[0]
        data[0] = data.removeLast()
        siftDown(0)
        return top
    }
    
    var isEmpty: Bool {
        return data.isEmpty
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[child].0 < data[parent].0 {
                data.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < data.count && data[left].0 < data[smallest].0 {
                smallest = left
            }
            if right < data.count && data[right].0 < data[smallest].0 {
                smallest = right
            }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class Solution {
    fun secondMinimum(n: Int, edges: Array<IntArray>, time: Int, change: Int): Int {
        val adj = Array(n + 1) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        val INF = Int.MAX_VALUE / 2
        val dist1 = IntArray(n + 1) { INF }
        val dist2 = IntArray(n + 1) { INF }

        val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.first })
        dist1[1] = 0
        pq.add(Pair(0, 1))

        while (pq.isNotEmpty()) {
            val (curTime, node) = pq.poll()
            if (curTime > dist2[node]) continue

            for (nei in adj[node]) {
                var depart = curTime
                if ((depart / change) % 2 == 1) {
                    depart = (depart / change + 1) * change
                }
                val newTime = depart + time

                if (newTime < dist1[nei]) {
                    dist2[nei] = dist1[nei]
                    dist1[nei] = newTime
                    pq.add(Pair(newTime, nei))
                } else if (newTime > dist1[nei] && newTime < dist2[nei]) {
                    dist2[nei] = newTime
                    pq.add(Pair(newTime, nei))
                }
            }
        }

        return dist2[n]
    }
}
```

## Dart

```dart
class _Node {
  int time;
  int node;
  _Node(this.time, this.node);
}

class Solution {
  int secondMinimum(int n, List<List<int>> edges, int time, int change) {
    // Build adjacency list
    List<List<int>> adj = List.generate(n + 1, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    const int INF = 1 << 60;
    List<int> dist1 = List.filled(n + 1, INF);
    List<int> dist2 = List.filled(n + 1, INF);
    dist1[1] = 0;

    // Min-heap implementation
    List<_Node> heap = [];

    void push(int t, int node) {
      heap.add(_Node(t, node));
      int i = heap.length - 1;
      while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].time <= heap[i].time) break;
        var tmp = heap[p];
        heap[p] = heap[i];
        heap[i] = tmp;
        i = p;
      }
    }

    _Node pop() {
      var top = heap[0];
      var last = heap.removeLast();
      if (heap.isNotEmpty) {
        heap[0] = last;
        int i = 0;
        while (true) {
          int l = i * 2 + 1, r = l + 1, smallest = i;
          if (l < heap.length && heap[l].time < heap[smallest].time) smallest = l;
          if (r < heap.length && heap[r].time < heap[smallest].time) smallest = r;
          if (smallest == i) break;
          var tmp = heap[i];
          heap[i] = heap[smallest];
          heap[smallest] = tmp;
          i = smallest;
        }
      }
      return top;
    }

    push(0, 1);

    while (heap.isNotEmpty) {
      var cur = pop();
      int curTime = cur.time;
      int u = cur.node;

      if (curTime > dist2[u]) continue; // we already have better two times

      for (int v in adj[u]) {
        int depart = curTime;
        // If the signal is red, wait until it turns green
        if ((depart ~/ change) % 2 == 1) {
          depart = (depart ~/ change + 1) * change;
        }
        int arrival = depart + time;

        if (arrival < dist1[v]) {
          dist2[v] = dist1[v];
          dist1[v] = arrival;
          push(arrival, v);
        } else if (arrival > dist1[v] && arrival < dist2[v]) {
          dist2[v] = arrival;
          push(arrival, v);
        }
      }
    }

    return dist2[n];
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type item struct {
	time int
	node int
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

func secondMinimum(n int, edges [][]int, time int, change int) int {
	const INF = int(1e18)

	adj := make([][]int, n+1)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	dist := make([][2]int, n+1)
	for i := 1; i <= n; i++ {
		dist[i][0] = INF
		dist[i][1] = INF
	}
	dist[1][0] = 0

	pq := &priorityQueue{}
	heap.Init(pq)
	heap.Push(pq, item{0, 1})

	for pq.Len() > 0 {
		curItem := heap.Pop(pq).(item)
		curTime, u := curItem.time, curItem.node

		// If this time is larger than the second best known for u, skip
		if curTime > dist[u][1] {
			continue
		}

		for _, v := range adj[u] {
			depart := curTime
			if (depart/change)%2 == 1 { // red light, wait until next green
				depart = ((depart / change) + 1) * change
			}
			arrival := depart + time

			if arrival < dist[v][0] {
				dist[v][1] = dist[v][0]
				dist[v][0] = arrival
				heap.Push(pq, item{arrival, v})
			} else if arrival > dist[v][0] && arrival < dist[v][1] {
				dist[v][1] = arrival
				heap.Push(pq, item{arrival, v})
			}
		}
	}

	return dist[n][1]
}
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(item)
    @data << item
    i = @data.size - 1
    while i > 0
      p = (i - 1) / 2
      break if @data[p][0] <= @data[i][0]
      @data[p], @data[i] = @data[i], @data[p]
      i = p
    end
  end

  def pop
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      size = @data.size
      loop do
        l = i * 2 + 1
        r = l + 1
        smallest = i
        smallest = l if l < size && @data[l][0] < @data[smallest][0]
        smallest = r if r < size && @data[r][0] < @data[smallest][0]
        break if smallest == i
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
    top
  end

  def empty?
    @data.empty?
  end
end

def second_minimum(n, edges, time, change)
  adj = Array.new(n + 1) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  inf = Float::INFINITY
  dist1 = Array.new(n + 1, inf)
  dist2 = Array.new(n + 1, inf)
  cnt   = Array.new(n + 1, 0)

  heap = MinHeap.new
  dist1[1] = 0
  heap.push([0, 1])

  until heap.empty?
    cur_time, u = heap.pop
    # Skip if this entry is outdated (larger than second best known)
    next if cur_time > dist2[u]

    cnt[u] += 1
    return cur_time if u == n && cnt[u] == 2

    adj[u].each do |v|
      depart = cur_time
      # wait if the signal is red at departure time
      if (depart.div(change)).odd?
        depart = (depart.div(change) + 1) * change
      end
      arrival = depart + time

      if arrival < dist1[v]
        dist2[v] = dist1[v]
        dist1[v] = arrival
        heap.push([arrival, v])
      elsif arrival > dist1[v] && arrival < dist2[v]
        dist2[v] = arrival
        heap.push([arrival, v])
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, PriorityQueue}

  case class State(time: Long, node: Int)

  def secondMinimum(n: Int, edges: Array[Array[Int]], time: Int, change: Int): Int = {
    val adj = Array.fill(n + 1)(new ArrayBuffer[Int]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      adj(u) += v
      adj(v) += u
    }

    val INF: Long = Long.MaxValue / 4
    val dist1 = Array.fill(n + 1)(INF)
    val dist2 = Array.fill(n + 1)(INF)

    implicit val ordering: Ordering[State] = Ordering.by((s: State) => -s.time)
    val pq = PriorityQueue.empty[State]

    dist1(1) = 0L
    pq.enqueue(State(0L, 1))

    while (pq.nonEmpty) {
      val cur = pq.dequeue()
      val curTime = cur.time
      val u = cur.node

      if (curTime > dist2(u)) {
        // This time is already worse than the second best known for this node.
        // No need to expand it.
        continue
      }

      for (v <- adj(u)) {
        var depart = curTime
        val cycles = curTime / change
        if ((cycles & 1L) == 1L) {
          depart = (cycles + 1) * change
        }
        val arrive = depart + time

        if (arrive < dist1(v)) {
          dist2(v) = dist1(v)
          dist1(v) = arrive
          pq.enqueue(State(arrive, v))
        } else if (arrive > dist1(v) && arrive < dist2(v)) {
          dist2(v) = arrive
          pq.enqueue(State(arrive, v))
        }
      }
    }

    dist2(n).toInt
  }

  // Helper to emulate continue in while loop
  private def continue: Unit = {}
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn second_minimum(n: i32, edges: Vec<Vec<i32>>, time: i32, change: i32) -> i32 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize + 1];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        let time_i64 = time as i64;
        let change_i64 = change as i64;

        let mut heap: BinaryHeap<(Reverse<i64>, usize)> = BinaryHeap::new();
        heap.push((Reverse(0), 1));

        let mut cnt = vec![0usize; n_usize + 1];

        while let Some(((Reverse(cur_time)), u)) = heap.pop() {
            if cnt[u] >= 2 {
                continue;
            }
            cnt[u] += 1;
            if u == n_usize && cnt[u] == 2 {
                return cur_time as i32;
            }

            // Determine departure time after possible waiting at a red signal
            let mut depart = cur_time;
            if (depart / change_i64) % 2 == 1 {
                depart = ((depart / change_i64) + 1) * change_i64;
            }
            let arrival = depart + time_i64;

            for &v in adj[u].iter() {
                heap.push((Reverse(arrival), v));
            }
        }

        0
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (second-minimum n edges time change)
  (-> exact-integer?
      (listof (listof exact-integer?))
      exact-integer?
      exact-integer?
      exact-integer?)
  (let* ([adj (make-vector (+ n 1) '())]
         [_ (for-each
                (lambda (e)
                  (define u (first e))
                  (define v (second e))
                  (vector-set! adj u (cons v (vector-ref adj u)))
                  (vector-set! adj v (cons u (vector-ref adj v))))
                edges)]
         [INF (expt 10 12)]
         [dist1 (make-vector (+ n 1) INF)]
         [dist2 (make-vector (+ n 1) INF)]
         [cnt (make-vector (+ n 1) 0)]
         [heap (make-heap (lambda (a b) (< (first a) (first b))))])
    (vector-set! dist1 1 0)
    (heap-push! heap (list 0 1))
    (let loop ()
      (if (heap-empty? heap)
          (vector-ref dist2 n) ; should never happen
          (let* ([item (heap-pop! heap)]
                 [d (first item)]
                 [u (second item)])
            ;; skip if this entry is worse than the current second best for u
            (when (> d (vector-ref dist2 u))
              (loop))
            (define newcnt (+ 1 (vector-ref cnt u)))
            (vector-set! cnt u newcnt)
            (if (and (= u n) (= newcnt 2))
                d
                (begin
                  (for-each
                    (lambda (v)
                      (let* ([cycle (quotient d change)]
                             [newt (if (odd? cycle)
                                       (+ (* (+ cycle 1) change) time)
                                       (+ d time))])
                        (cond
                          [(< newt (vector-ref dist1 v))
                           (vector-set! dist2 v (vector-ref dist1 v))
                           (vector-set! dist1 v newt)
                           (heap-push! heap (list newt v))]
                          [(and (> newt (vector-ref dist1 v))
                                (< newt (vector-ref dist2 v)))
                           (vector-set! dist2 v newt)
                           (heap-push! heap (list newt v))])))
                    (vector-ref adj u))
                  (loop))))))))
```

## Erlang

```erlang
-spec second_minimum(N :: integer(), Edges :: [[integer()]], Time :: integer(), Change :: integer()) -> integer().
second_minimum(N, Edges, Time, Change) ->
    ?INF = 1 bsl 60,
    Adj0 = build_adj(Edges, #{}),
    Adj = ensure_all_nodes(N, Adj0),
    DistInit = maps:from_list(lists:map(fun(I) -> {I, ?INF} end, lists:seq(1, N))),
    Dist1 = maps:put(1, 0, DistInit),
    Dist2 = DistInit,
    Set0 = gb_sets:add({0, 0, 1}, gb_sets:new()),
    process(Set0, 1, Dist1, Dist2, Adj, N, Time, Change).

build_adj([], Acc) -> Acc;
build_adj([[U, V] | Rest], Acc) ->
    Acc1 = maps:update_with(U,
            fun(L) -> [V | L] end,
            [V],
            Acc),
    Acc2 = maps:update_with(V,
            fun(L) -> [U | L] end,
            [U],
            Acc1),
    build_adj(Rest, Acc2).

ensure_all_nodes(N, Adj) -> ensure_all_nodes(1, N, Adj).
ensure_all_nodes(I, N, Adj) when I > N -> Adj;
ensure_all_nodes(I, N, Adj) ->
    case maps:is_key(I, Adj) of
        true -> ensure_all_nodes(I + 1, N, Adj);
        false -> ensure_all_nodes(I + 1, N, maps:put(I, [], Adj))
    end.

next_time(Cur, Change, Time) ->
    case ((Cur div Change) rem 2) of
        1 -> % red
            Wait = Change - (Cur rem Change),
            Cur + Wait + Time;
        _ -> % green
            Cur + Time
    end.

process(Set, Counter, Dist1, Dist2, Adj, Target, Time, Change) ->
    case gb_sets:is_empty(Set) of
        true -> 0; % should not happen
        false ->
            {Elem, Set1} = pop_min(Set),
            {CurTime, _Cnt, Node} = Elem,
            D1 = maps:get(Node, Dist1),
            if Node == Target andalso CurTime > D1 ->
                    CurTime;
               true ->
                    OldDist2 = maps:get(Node, Dist2),
                    {NewDist1, NewDist2, Updated} =
                        if CurTime < D1 ->
                                OldBest = D1,
                                UpdatedDist2 = case OldBest of
                                                   ?INF -> OldDist2;
                                                   _ when OldBest > CurTime, OldBest < OldDist2 -> OldBest;
                                                   _ -> OldDist2
                                               end,
                                {maps:put(Node, CurTime, Dist1), maps:put(Node, UpdatedDist2, Dist2), true};
                           CurTime > D1, CurTime < OldDist2 ->
                                {Dist1, maps:put(Node, CurTime, Dist2), true};
                           true ->
                                {Dist1, Dist2, false}
                        end,
                    case Updated of
                        true ->
                            Neighs = maps:get(Node, Adj),
                            {Set2, Counter2} = lists:foldl(
                                fun(Nei, {S, C}) ->
                                    Arrival = next_time(CurTime, Change, Time),
                                    Elem2 = {Arrival, C, Nei},
                                    {gb_sets:add(Elem2, S), C + 1}
                                end,
                                {Set1, Counter},
                                Neighs),
                            process(Set2, Counter2, NewDist1, NewDist2, Adj, Target, Time, Change);
                        false ->
                            process(Set1, Counter, NewDist1, NewDist2, Adj, Target, Time, Change)
                    end
            end
    end.

pop_min(Set) ->
    Elem = gb_sets:smallest(Set),
    {Elem, gb_sets:delete(Elem, Set)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec second_minimum(n :: integer, edges :: [[integer]], time :: integer, change :: integer) :: integer
  def second_minimum(n, edges, time_per_edge, change) do
    adj = build_adj(edges)

    inf = 1_000_000_000

    min_dist = :array.new(n + 1, default: inf)
    sec_dist = :array.new(n + 1, default: inf)
    visits   = :array.new(n + 1, default: 0)

    min_dist = :array.set(1, 0, min_dist)

    {pq, _cnt} = PQ.new()
    {pq, _cnt} = PQ.push({pq, 0}, 0, 1)

    loop({pq, 0}, adj, time_per_edge, change, n, min_dist, sec_dist, visits)
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)
  end

  defp travel_time(cur, time_per_edge, change) do
    if rem(div(cur, change), 2) == 1 do
      wait = change - rem(cur, change)
      cur + wait + time_per_edge
    else
      cur + time_per_edge
    end
  end

  defp loop({pq_tree, cnt} = pq_state, adj, time_per_edge, change, target,
            min_dist, sec_dist, visits) do
    case PQ.pop(pq_state) do
      {:empty, _} ->
        -1

      {{:ok, cur_time, node}, new_pq_state} ->
        visit_cnt = :array.get(node, visits)

        if visit_cnt >= 2 do
          loop(new_pq_state, adj, time_per_edge, change, target,
               min_dist, sec_dist, visits)
        else
          visits = :array.set(node, visit_cnt + 1, visits)

          if node == target and visit_cnt + 1 == 2 do
            cur_time
          else
            {pq_next, min_next, sec_next} =
              Enum.reduce(Map.get(adj, node, []), {new_pq_state, min_dist, sec_dist},
                fn nb, {pq_acc, min_acc, sec_acc} ->
                  new_time = travel_time(cur_time, time_per_edge, change)

                  min_nb = :array.get(nb, min_acc)
                  sec_nb = :array.get(nb, sec_acc)

                  cond do
                    new_time < min_nb ->
                      sec_updated = :array.set(nb, min_nb, sec_acc)
                      min_updated = :array.set(nb, new_time, min_acc)
                      {pq_new, _} = PQ.push(pq_acc, new_time, nb)
                      {pq_new, min_updated, sec_updated}

                    new_time > min_nb and new_time < sec_nb ->
                      sec_updated = :array.set(nb, new_time, sec_acc)
                      {pq_new, _} = PQ.push(pq_acc, new_time, nb)
                      {pq_new, min_acc, sec_updated}

                    true ->
                      {pq_acc, min_acc, sec_acc}
                  end
                end)

            loop({pq_next, cnt}, adj, time_per_edge, change, target,
                 min_next, sec_next, visits)
          end
        end
    end
  end
end

defmodule PQ do
  def new(), do: {:gb_trees.empty(), 0}

  def push({tree, cnt}, priority, node) do
    key = {priority, cnt}
    {:gb_trees.insert(key, node, tree), cnt + 1}
  end

  def pop({tree, cnt}) do
    if :gb_trees.is_empty(tree) do
      {:empty, {tree, cnt}}
    else
      {{key, node}, new_tree} = :gb_trees.take_smallest(tree)
      priority = elem(key, 0)
      {{:ok, priority, node}, {new_tree, cnt}}
    end
  end
end
```

# 1928. Minimum Cost to Reach Destination in Time

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(int maxTime, vector<vector<int>>& edges, vector<int>& passingFees) {
        int n = passingFees.size();
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], t = e[2];
            adj[u].push_back({v, t});
            adj[v].push_back({u, t});
        }
        const int INF = 1e9;
        vector<vector<int>> dist(n, vector<int>(maxTime + 1, INF));
        priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<tuple<int,int,int>>> pq;
        dist[0][0] = passingFees[0];
        pq.emplace(passingFees[0], 0, 0);
        while (!pq.empty()) {
            auto [cost, u, time] = pq.top(); pq.pop();
            if (cost != dist[u][time]) continue;
            for (auto &[v, w] : adj[u]) {
                int nt = time + w;
                if (nt > maxTime) continue;
                int nc = cost + passingFees[v];
                if (nc < dist[v][nt]) {
                    dist[v][nt] = nc;
                    pq.emplace(nc, v, nt);
                }
            }
        }
        int ans = INF;
        for (int t = 0; t <= maxTime; ++t) ans = min(ans, dist[n-1][t]);
        return ans == INF ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minCost(int maxTime, int[][] edges, int[] passingFees) {
        int n = passingFees.length;
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], t = e[2];
            graph[u].add(new int[]{v, t});
            graph[v].add(new int[]{u, t});
        }

        final int INF = Integer.MAX_VALUE / 4;
        int[][] dp = new int[n][maxTime + 1];
        for (int i = 0; i < n; i++) Arrays.fill(dp[i], INF);
        dp[0][0] = passingFees[0];

        PriorityQueue<State> pq = new PriorityQueue<>();
        pq.offer(new State(passingFees[0], 0, 0));

        while (!pq.isEmpty()) {
            State cur = pq.poll();
            if (cur.cost != dp[cur.node][cur.time]) continue;
            if (cur.node == n - 1) return cur.cost;

            for (int[] nb : graph[cur.node]) {
                int v = nb[0];
                int nt = cur.time + nb[1];
                if (nt > maxTime) continue;
                int nc = cur.cost + passingFees[v];
                if (nc < dp[v][nt]) {
                    dp[v][nt] = nc;
                    pq.offer(new State(nc, v, nt));
                }
            }
        }
        return -1;
    }

    private static class State implements Comparable<State> {
        int cost;
        int node;
        int time;
        State(int c, int n, int t) {
            this.cost = c;
            this.node = n;
            this.time = t;
        }
        public int compareTo(State o) {
            return Integer.compare(this.cost, o.cost);
        }
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        n = len(passingFees)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        INF = 10 ** 9
        dp = [[INF] * (maxTime + 1) for _ in range(n)]
        dp[0][0] = passingFees[0]

        for cur_time in range(maxTime + 1):
            for u in range(n):
                cur_cost = dp[u][cur_time]
                if cur_cost == INF:
                    continue
                for v, w in adj[u]:
                    nt = cur_time + w
                    if nt <= maxTime:
                        new_cost = cur_cost + passingFees[v]
                        if new_cost < dp[v][nt]:
                            dp[v][nt] = new_cost

        ans = min(dp[n - 1])
        return -1 if ans == INF else ans
```

## Python3

```python
class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        from heapq import heappush, heappop

        n = len(passingFees)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = 10 ** 9
        dp = [[INF] * (maxTime + 1) for _ in range(n)]
        dp[0][0] = passingFees[0]

        heap = [(passingFees[0], 0, 0)]  # (cost, node, time)

        while heap:
            cost, u, t = heappop(heap)
            if cost != dp[u][t]:
                continue
            if u == n - 1:
                return cost
            for v, w in adj[u]:
                nt = t + w
                if nt > maxTime:
                    continue
                ncost = cost + passingFees[v]
                if ncost < dp[v][nt]:
                    dp[v][nt] = ncost
                    heappush(heap, (ncost, v, nt))

        ans = min(dp[n - 1])
        return -1 if ans == INF else ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minCost(int maxTime, int** edges, int edgesSize, int* edgesColSize, int* passingFees, int passingFeesSize) {
    int n = passingFeesSize;
    int T = maxTime;
    int INF = INT_MAX / 2;

    int *dp = (int *)malloc((n * (T + 1)) * sizeof(int));
    for (int i = 0; i < n * (T + 1); ++i) dp[i] = INF;
    dp[0 * (T + 1) + 0] = passingFees[0];

    for (int t = 0; t <= T; ++t) {
        for (int i = 0; i < edgesSize; ++i) {
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];

            int curU = dp[u * (T + 1) + t];
            if (curU != INF && t + w <= T) {
                int idxV = v * (T + 1) + (t + w);
                int newCost = curU + passingFees[v];
                if (newCost < dp[idxV]) dp[idxV] = newCost;
            }

            int curV = dp[v * (T + 1) + t];
            if (curV != INF && t + w <= T) {
                int idxU = u * (T + 1) + (t + w);
                int newCost = curV + passingFees[u];
                if (newCost < dp[idxU]) dp[idxU] = newCost;
            }
        }
    }

    int ans = INF;
    for (int t = 0; t <= T; ++t) {
        int cost = dp[(n - 1) * (T + 1) + t];
        if (cost < ans) ans = cost;
    }

    free(dp);
    return ans == INF ? -1 : ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinCost(int maxTime, int[][] edges, int[] passingFees) {
        int n = passingFees.Length;
        var graph = new List<(int to, int time)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], t = e[2];
            graph[u].Add((v, t));
            graph[v].Add((u, t));
        }

        const int INF = int.MaxValue / 2;
        var dp = new int[n][];
        for (int i = 0; i < n; i++) {
            dp[i] = new int[maxTime + 1];
            Array.Fill(dp[i], INF);
        }
        dp[0][0] = passingFees[0];

        var pq = new PriorityQueue<(int node, int time, int cost), int>();
        pq.Enqueue((0, 0, passingFees[0]), passingFees[0]);

        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int u = cur.node;
            int t = cur.time;
            int c = cur.cost;

            if (c != dp[u][t]) continue; // outdated entry

            foreach (var nb in graph[u]) {
                int v = nb.to;
                int nt = t + nb.time;
                if (nt > maxTime) continue;
                int nc = c + passingFees[v];
                if (nc < dp[v][nt]) {
                    dp[v][nt] = nc;
                    pq.Enqueue((v, nt, nc), nc);
                }
            }
        }

        int ans = INF;
        for (int t = 0; t <= maxTime; t++) {
            ans = Math.Min(ans, dp[n - 1][t]);
        }
        return ans == INF ? -1 : ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} maxTime
 * @param {number[][]} edges
 * @param {number[]} passingFees
 * @return {number}
 */
var minCost = function(maxTime, edges, passingFees) {
    const n = passingFees.length;
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, t] of edges) {
        adj[u].push([v, t]);
        adj[v].push([u, t]);
    }

    const INF = Number.MAX_SAFE_INTEGER;
    const dp = Array.from({ length: n }, () => Array(maxTime + 1).fill(INF));
    dp[0][0] = passingFees[0];

    class MinHeap {
        constructor() { this.heap = []; }
        push(item) {
            this.heap.push(item);
            this._up(this.heap.length - 1);
        }
        _up(i) {
            const h = this.heap;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p][0] <= h[i][0]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (!h.length) return null;
            const top = h[0];
            const last = h.pop();
            if (h.length) {
                h[0] = last;
                this._down(0);
            }
            return top;
        }
        _down(i) {
            const h = this.heap;
            const n = h.length;
            while (true) {
                let l = i * 2 + 1, r = l + 1, s = i;
                if (l < n && h[l][0] < h[s][0]) s = l;
                if (r < n && h[r][0] < h[s][0]) s = r;
                if (s === i) break;
                [h[i], h[s]] = [h[s], h[i]];
                i = s;
            }
        }
        size() { return this.heap.length; }
    }

    const pq = new MinHeap();
    pq.push([dp[0][0], 0, 0]);

    while (pq.size()) {
        const [cost, u, time] = pq.pop();
        if (cost !== dp[u][time]) continue;
        if (u === n - 1) return cost;

        for (const [v, w] of adj[u]) {
            const nt = time + w;
            if (nt > maxTime) continue;
            const nc = cost + passingFees[v];
            if (nc < dp[v][nt]) {
                dp[v][nt] = nc;
                pq.push([nc, v, nt]);
            }
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minCost(maxTime: number, edges: number[][], passingFees: number[]): number {
    const n = passingFees.length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dp: number[][] = Array.from({ length: n }, () => new Array(maxTime + 1).fill(INF));
    dp[0][0] = passingFees[0];

    for (let t = 0; t <= maxTime; ++t) {
        for (const edge of edges) {
            const u = edge[0];
            const v = edge[1];
            const w = edge[2];
            const nt = t + w;
            if (nt > maxTime) continue;

            const costU = dp[u][t];
            if (costU !== INF) {
                const newCost = costU + passingFees[v];
                if (newCost < dp[v][nt]) dp[v][nt] = newCost;
            }

            const costV = dp[v][t];
            if (costV !== INF) {
                const newCost = costV + passingFees[u];
                if (newCost < dp[u][nt]) dp[u][nt] = newCost;
            }
        }
    }

    let ans = INF;
    for (let t = 0; t <= maxTime; ++t) {
        if (dp[n - 1][t] < ans) ans = dp[n - 1][t];
    }
    return ans === INF ? -1 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $maxTime
     * @param Integer[][] $edges
     * @param Integer[] $passingFees
     * @return Integer
     */
    function minCost($maxTime, $edges, $passingFees) {
        $n = count($passingFees);
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $w] = $e;
            $adj[$u][] = [$v, $w];
            $adj[$v][] = [$u, $w];
        }

        // Large number for infinity
        $INF = 1 << 60;

        // dp[node][time] = min cost to reach node at exact time
        $dp = [];
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = array_fill(0, $maxTime + 1, $INF);
        }
        $dp[0][0] = $passingFees[0];

        // Dynamic programming over time
        for ($t = 0; $t <= $maxTime; $t++) {
            for ($u = 0; $u < $n; $u++) {
                $curCost = $dp[$u][$t];
                if ($curCost === $INF) continue;
                foreach ($adj[$u] as $edge) {
                    [$v, $w] = $edge;
                    $newT = $t + $w;
                    if ($newT > $maxTime) continue;
                    $newCost = $curCost + $passingFees[$v];
                    if ($newCost < $dp[$v][$newT]) {
                        $dp[$v][$newT] = $newCost;
                    }
                }
            }
        }

        // Find minimal cost to reach destination within maxTime
        $ans = $INF;
        for ($t = 0; $t <= $maxTime; $t++) {
            if ($dp[$n - 1][$t] < $ans) {
                $ans = $dp[$n - 1][$t];
            }
        }

        return $ans === $INF ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    struct Edge {
        let to: Int
        let time: Int
    }
    
    struct HeapElement {
        let cost: Int
        let node: Int
        let time: Int
    }
    
    class MinHeap {
        private var heap: [HeapElement] = []
        
        func isEmpty() -> Bool {
            return heap.isEmpty
        }
        
        func push(_ element: HeapElement) {
            heap.append(element)
            siftUp(heap.count - 1)
        }
        
        func pop() -> HeapElement? {
            guard !heap.isEmpty else { return nil }
            let result = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                siftDown(0)
            }
            return result
        }
        
        private func siftUp(_ index: Int) {
            var child = index
            while child > 0 {
                let parent = (child - 1) / 2
                if heap[child].cost < heap[parent].cost {
                    heap.swapAt(child, parent)
                    child = parent
                } else {
                    break
                }
            }
        }
        
        private func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var smallest = parent
                if left < heap.count && heap[left].cost < heap[smallest].cost {
                    smallest = left
                }
                if right < heap.count && heap[right].cost < heap[smallest].cost {
                    smallest = right
                }
                if smallest == parent { break }
                heap.swapAt(parent, smallest)
                parent = smallest
            }
        }
    }
    
    func minCost(_ maxTime: Int, _ edges: [[Int]], _ passingFees: [Int]) -> Int {
        let n = passingFees.count
        var graph = [[Edge]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1], t = e[2]
            graph[u].append(Edge(to: v, time: t))
            graph[v].append(Edge(to: u, time: t))
        }
        
        let INF = Int.max / 4
        var best = Array(repeating: Array(repeating: INF, count: maxTime + 1), count: n)
        best[0][0] = passingFees[0]
        
        let heap = MinHeap()
        heap.push(HeapElement(cost: passingFees[0], node: 0, time: 0))
        
        while !heap.isEmpty() {
            guard let cur = heap.pop() else { break }
            if cur.cost != best[cur.node][cur.time] {
                continue
            }
            if cur.node == n - 1 {
                return cur.cost
            }
            for edge in graph[cur.node] {
                let newTime = cur.time + edge.time
                if newTime > maxTime { continue }
                let newCost = cur.cost + passingFees[edge.to]
                if newCost < best[edge.to][newTime] {
                    best[edge.to][newTime] = newCost
                    heap.push(HeapElement(cost: newCost, node: edge.to, time: newTime))
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
    data class State(val cost: Int, val node: Int, val time: Int)

    fun minCost(maxTime: Int, edges: Array<IntArray>, passingFees: IntArray): Int {
        val n = passingFees.size
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val t = e[2]
            adj[u].add(Pair(v, t))
            adj[v].add(Pair(u, t))
        }

        val INF = Int.MAX_VALUE
        val minTime = IntArray(n) { INF }
        val pq = java.util.PriorityQueue<State>(compareBy { it.cost })
        pq.add(State(passingFees[0], 0, 0))
        minTime[0] = 0

        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.time > maxTime) continue
            if (cur.node == n - 1) return cur.cost
            if (cur.time > minTime[cur.node]) continue

            for ((next, edgeTime) in adj[cur.node]) {
                val newTime = cur.time + edgeTime
                if (newTime > maxTime) continue
                val newCost = cur.cost + passingFees[next]
                if (newTime < minTime[next]) {
                    minTime[next] = newTime
                    pq.add(State(newCost, next, newTime))
                }
            }
        }

        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minCost(int maxTime, List<List<int>> edges, List<int> passingFees) {
    const int INF = 1 << 60;
    int n = passingFees.length;
    List<List<int>> dp = List.generate(n, (_) => List.filled(maxTime + 1, INF));
    dp[0][0] = passingFees[0];
    for (int t = 0; t <= maxTime; ++t) {
      for (var e in edges) {
        int u = e[0], v = e[1], w = e[2];
        if (dp[u][t] != INF) {
          int nt = t + w;
          if (nt <= maxTime) {
            int newCost = dp[u][t] + passingFees[v];
            if (newCost < dp[v][nt]) dp[v][nt] = newCost;
          }
        }
        if (dp[v][t] != INF) {
          int nt = t + w;
          if (nt <= maxTime) {
            int newCost = dp[v][t] + passingFees[u];
            if (newCost < dp[u][nt]) dp[u][nt] = newCost;
          }
        }
      }
    }
    int ans = INF;
    for (int t = 0; t <= maxTime; ++t) {
      if (dp[n - 1][t] < ans) ans = dp[n - 1][t];
    }
    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func minCost(maxTime int, edges [][]int, passingFees []int) int {
    n := len(passingFees)
    type edge struct{ to, w int }
    adj := make([][]edge, n)
    for _, e := range edges {
        u, v, w := e[0], e[1], e[2]
        adj[u] = append(adj[u], edge{v, w})
        adj[v] = append(adj[v], edge{u, w})
    }

    const INF = int(1e9) // larger than any possible cost
    dp := make([][]int, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]int, maxTime+1)
        for t := 0; t <= maxTime; t++ {
            dp[i][t] = INF
        }
    }
    dp[0][0] = passingFees[0]

    for t := 0; t <= maxTime; t++ {
        for u := 0; u < n; u++ {
            curCost := dp[u][t]
            if curCost == INF {
                continue
            }
            for _, e := range adj[u] {
                nt := t + e.w
                if nt > maxTime {
                    continue
                }
                newCost := curCost + passingFees[e.to]
                if newCost < dp[e.to][nt] {
                    dp[e.to][nt] = newCost
                }
            }
        }
    }

    ans := INF
    for t := 0; t <= maxTime; t++ {
        if dp[n-1][t] < ans {
            ans = dp[n-1][t]
        }
    }
    if ans == INF {
        return -1
    }
    return ans
}
```

## Ruby

```ruby
def min_cost(max_time, edges, passing_fees)
  n = passing_fees.length
  adj = Array.new(n) { [] }
  edges.each do |x, y, t|
    adj[x] << [y, t]
    adj[y] << [x, t]
  end

  inf = (1 << 60)
  dp = Array.new(n) { Array.new(max_time + 1, inf) }
  dp[0][0] = passing_fees[0]

  heap = MinHeap.new
  heap.push([passing_fees[0], 0, 0])

  while !heap.empty?
    cost, u, time = heap.pop
    next if cost != dp[u][time]
    return cost if u == n - 1

    adj[u].each do |v, w|
      nt = time + w
      next if nt > max_time
      nc = cost + passing_fees[v]
      if nc < dp[v][nt]
        dp[v][nt] = nc
        heap.push([nc, v, nt])
      end
    end
  end

  ans = dp[n - 1].min
  ans == inf ? -1 : ans
end

class MinHeap
  def initialize
    @data = []
  end

  def push(item)
    @data << item
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    min
  end

  def empty?
    @data.empty?
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent][0] <= @data[idx][0]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def sift_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < size && @data[left][0] < @data[smallest][0]
        smallest = left
      end
      if right < size && @data[right][0] < @data[smallest][0]
        smallest = right
      end
      break if smallest == idx
      @data[smallest], @data[idx] = @data[idx], @data[smallest]
      idx = smallest
    end
  end
end
```

## Scala

```scala
object Solution {
    def minCost(maxTime: Int, edges: Array[Array[Int]], passingFees: Array[Int]): Int = {
        val n = passingFees.length
        val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer[(Int, Int)]())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            val w = e(2)
            adj(a).append((b, w))
            adj(b).append((a, w))
        }
        val INF = Int.MaxValue / 4
        val dp = Array.fill(n)(Array.fill(maxTime + 1)(INF))
        dp(0)(0) = passingFees(0)

        for (t <- 0 to maxTime) {
            var u = 0
            while (u < n) {
                val cur = dp(u)(t)
                if (cur != INF) {
                    val neighbors = adj(u)
                    var i = 0
                    while (i < neighbors.length) {
                        val (v, w) = neighbors(i)
                        val nt = t + w
                        if (nt <= maxTime) {
                            val newCost = cur + passingFees(v)
                            if (newCost < dp(v)(nt)) {
                                dp(v)(nt) = newCost
                            }
                        }
                        i += 1
                    }
                }
                u += 1
            }
        }

        var ans = INF
        for (t <- 0 to maxTime) {
            val cost = dp(n - 1)(t)
            if (cost < ans) ans = cost
        }
        if (ans == INF) -1 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(max_time: i32, edges: Vec<Vec<i32>>, passing_fees: Vec<i32>) -> i32 {
        let n = passing_fees.len();
        let max_t = max_time as usize;
        // Build adjacency list
        let mut adj: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2];
            adj[u].push((v, w));
            adj[v].push((u, w));
        }

        const INF: i32 = 1_000_000_007; // larger than any possible total fee
        let mut dp = vec![vec![INF; max_t + 1]; n];
        dp[0][0] = passing_fees[0];

        use std::cmp::Reverse;
        use std::collections::BinaryHeap;
        let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        heap.push(Reverse((dp[0][0], 0usize, 0usize)));

        while let Some(Reverse((cost, u, time))) = heap.pop() {
            if cost != dp[u][time] {
                continue;
            }
            if u == n - 1 {
                return cost;
            }
            for &(v, w) in &adj[u] {
                let new_time = time + w as usize;
                if new_time > max_t {
                    continue;
                }
                let new_cost = cost + passing_fees[v];
                if new_cost < dp[v][new_time] {
                    dp[v][new_time] = new_cost;
                    heap.push(Reverse((new_cost, v, new_time)));
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (min-cost maxTime edges passingFees)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof exact-integer?)
      exact-integer?)
  (let* ([n (length passingFees)]
         [adj (make-vector n '())]
         [_ (for ([e edges])
              (let* ((x (list-ref e 0))
                     (y (list-ref e 1))
                     (t (list-ref e 2)))
                (vector-set! adj x (cons (list y t) (vector-ref adj x)))
                (vector-set! adj y (cons (list x t) (vector-ref adj y)))))]
         [INF 1000000000]
         [best
          (let ([vec (make-vector n)])
            (for ([i (in-range n)])
              (vector-set! vec i (make-vector (+ maxTime 1) INF)))
            vec)]
         [_ (vector-set! (vector-ref best 0) 0 (list-ref passingFees 0))]
         [heap (make-heap (lambda (a b) (< (first a) (first b))))])
    (heap-add! heap (list (list-ref passingFees 0) 0 0))
    (let recur ()
      (if (heap-empty? heap)
          -1
          (let* ([state (heap-min heap)]
                 [_ (heap-remove-min! heap)]
                 [cost (first state)]
                 [node (second state)]
                 [time (third state)])
            (cond
              [(> cost (vector-ref (vector-ref best node) time))
               (recur)]
              [(= node (- n 1)) cost]
              [else
               (for ([nbr (vector-ref adj node)])
                 (let* ((nb (list-ref nbr 0))
                        (w (list-ref nbr 1))
                        (newt (+ time w)))
                   (when (<= newt maxTime)
                     (define newc (+ cost (list-ref passingFees nb)))
                     (let ([nodeBest (vector-ref best nb)])
                       (when (< newc (vector-ref nodeBest newt))
                         (vector-set! nodeBest newt newc)
                         (heap-add! heap (list newc nb newt))))))))
               (recur)])))))
```

## Erlang

```erlang
-spec min_cost(MaxTime :: integer(), Edges :: [[integer()]], PassingFees :: [integer()]) -> integer().
min_cost(MaxTime, Edges, PassingFees) ->
    N = length(PassingFees),
    FeesTuple = list_to_tuple(PassingFees),

    Adj = build_adj(Edges, #{}),

    EmptyMap = maps:new(),
    DP0 = erlang:make_tuple(N, EmptyMap),

    Buckets0 = erlang:make_tuple(MaxTime + 1, []),

    StartCost = element(1, FeesTuple),
    DP1 = set_dp(DP0, 0, 0, StartCost),
    Buckets1 = erlang:setelement(1, Buckets0, [{0, StartCost}]),

    FinalDP = loop(0, MaxTime, Adj, FeesTuple, DP1, Buckets1),

    DestMap = element(N, FinalDP), % node n-1 is at position N
    case maps:values(DestMap) of
        [] -> -1;
        Values -> lists:min(Values)
    end.

%% Build adjacency map {Node => [{Neighbor, Time}, ...]}
build_adj([], Acc) ->
    Acc;
build_adj([[X, Y, T] | Rest], Acc) ->
    Acc1 = maps:update_with(
                X,
                fun(L) -> [{Y, T} | L] end,
                [{Y, T}],
                Acc),
    Acc2 = maps:update_with(
                Y,
                fun(L) -> [{X, T} | L] end,
                [{X, T}],
                Acc1),
    build_adj(Rest, Acc2).

%% Set dp[node][time] = Cost
set_dp(DP, NodeIdx, Time, Cost) ->
    Map = element(NodeIdx + 1, DP),
    NewMap = maps:put(Time, Cost, Map),
    erlang:setelement(NodeIdx + 1, DP, NewMap).

%% Get dp[node][time]
get_dp(DP, NodeIdx, Time) ->
    Map = element(NodeIdx + 1, DP),
    case maps:find(Time, Map) of
        {ok, Val} -> Val;
        error -> undefined
    end.

%% Main loop over time buckets
loop(Time, MaxTime, _Adj, _FeesTuple, DP, _Buckets) when Time > MaxTime ->
    DP;
loop(Time, MaxTime, Adj, FeesTuple, DP, Buckets) ->
    Bucket = element(Time + 1, Buckets),
    {DP2, Buckets2} = process_bucket(Bucket, Time, MaxTime, Adj, FeesTuple, DP, Buckets),
    loop(Time + 1, MaxTime, Adj, FeesTuple, DP2, Buckets2).

%% Process all states in a bucket
process_bucket([], _Time, _MaxTime, _Adj, _FeesTuple, DP, Buckets) ->
    {DP, Buckets};
process_bucket([{NodeIdx, Cost} | Rest], Time, MaxTime, Adj, FeesTuple, DP, Buckets) ->
    case get_dp(DP, NodeIdx, Time) of
        undefined -> % should not happen
            process_bucket(Rest, Time, MaxTime, Adj, FeesTuple, DP, Buckets);
        StoredCost when StoredCost =/= Cost ->
            % outdated entry, ignore
            process_bucket(Rest, Time, MaxTime, Adj, FeesTuple, DP, Buckets);
        _StoredCost ->
            AdjList = maps:get(NodeIdx, Adj, []),
            {DP1, Buckets1} = lists:foldl(
                fun({Nb, EdgeT}, {DAcc, BAcc}) ->
                    NewTime = Time + EdgeT,
                    if NewTime =< MaxTime ->
                        NbFee = element(Nb + 1, FeesTuple),
                        NewCost = Cost + NbFee,
                        Existing = get_dp(DAcc, Nb, NewTime),
                        case Existing of
                            undefined ->
                                D2 = set_dp(DAcc, Nb, NewTime, NewCost),
                                BList = element(NewTime + 1, BAcc),
                                B2 = erlang:setelement(NewTime + 1, BAcc, [{Nb, NewCost} | BList]),
                                {D2, B2};
                            Prev when NewCost < Prev ->
                                D2 = set_dp(DAcc, Nb, NewTime, NewCost),
                                BList = element(NewTime + 1, BAcc),
                                B2 = erlang:setelement(NewTime + 1, BAcc, [{Nb, NewCost} | BList]),
                                {D2, B2};
                            _ ->
                                {DAcc, BAcc}
                        end;
                    true ->
                        {DAcc, BAcc}
                    end
                end,
                {DP, Buckets},
                AdjList),
            process_bucket(Rest, Time, MaxTime, Adj, FeesTuple, DP1, Buckets1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(max_time :: integer, edges :: [[integer]], passing_fees :: [integer]) :: integer
  def min_cost(max_time, edges, passing_fees) do
    n = length(passing_fees)
    adj = build_adj(n, edges)

    start_fee = Enum.at(passing_fees, 0)
    tree = :gb_trees.insert({start_fee, 0}, {0, 0}, :gb_trees.empty())
    best_map = %{{0, 0} => start_fee}
    dijkstra(tree, best_map, adj, passing_fees, max_time, n - 1, 1)
  end

  defp build_adj(n, edges) do
    init = Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)

    Enum.reduce(edges, init, fn [u, v, t], acc ->
      acc
      |> Map.update!(u, fn lst -> [{v, t} | lst] end)
      |> Map.update!(v, fn lst -> [{u, t} | lst] end)
    end)
  end

  defp dijkstra(tree, best_map, adj, fees, max_time, target, id_counter) do
    if :gb_trees.is_empty(tree) do
      -1
    else
      {{{cost, _id}, {node, time}}, new_tree} = :gb_trees.take_smallest(tree)

      case Map.get(best_map, {node, time}) do
        ^cost ->
          if node == target do
            cost
          else
            {updated_tree, updated_map, next_id} =
              Enum.reduce(Map.get(adj, node, []), {new_tree, best_map, id_counter}, fn {nbr, etime},
                                                                                 {t_acc, m_acc, id_acc} ->
                nt = time + etime

                if nt <= max_time do
                  ncost = cost + Enum.at(fees, nbr)

                  case Map.get(m_acc, {nbr, nt}) do
                    nil ->
                      t2 = :gb_trees.insert({ncost, id_acc}, {nbr, nt}, t_acc)
                      {t2, Map.put(m_acc, {nbr, nt}, ncost), id_acc + 1}

                    existing when ncost < existing ->
                      t2 = :gb_trees.insert({ncost, id_acc}, {nbr, nt}, t_acc)
                      {t2, Map.put(m_acc, {nbr, nt}, ncost), id_acc + 1}

                    _ ->
                      {t_acc, m_acc, id_acc}
                  end
                else
                  {t_acc, m_acc, id_acc}
                end
              end)

            dijkstra(updated_tree, updated_map, adj, fees, max_time, target, next_id)
          end

        _stale ->
          dijkstra(new_tree, best_map, adj, fees, max_time, target, id_counter)
      end
    end
  end
end
```

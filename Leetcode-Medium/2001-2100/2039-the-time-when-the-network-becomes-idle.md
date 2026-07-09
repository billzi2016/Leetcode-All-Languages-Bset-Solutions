# 2039. The Time When the Network Becomes Idle

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int networkBecomesIdle(vector<vector<int>>& edges, vector<int>& patience) {
        int n = patience.size();
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<int> dist(n, -1);
        queue<int> q;
        dist[0] = 0;
        q.push(0);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        long long maxIdle = 0;
        for (int i = 1; i < n; ++i) {
            long long roundTrip = 2LL * dist[i];
            long long p = patience[i];
            long long lastSend = 0;
            if (roundTrip > p) {
                long long k = (roundTrip - 1) / p;
                lastSend = k * p;
            }
            long long idleTime = lastSend + roundTrip;
            maxIdle = max(maxIdle, idleTime);
        }
        return (int)(maxIdle + 1);
    }
};
```

## Java

```java
class Solution {
    public int networkBecomesIdle(int[][] edges, int[] patience) {
        int n = patience.length;
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        int[] dist = new int[n];
        java.util.Arrays.fill(dist, -1);
        java.util.Queue<Integer> queue = new java.util.ArrayDeque<>();
        dist[0] = 0;
        queue.offer(0);
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            for (int nb : graph[cur]) {
                if (dist[nb] == -1) {
                    dist[nb] = dist[cur] + 1;
                    queue.offer(nb);
                }
            }
        }

        long maxTime = 0L;
        for (int i = 1; i < n; i++) {
            long roundTrip = 2L * dist[i];
            long p = patience[i];
            long lastSent = 0L;
            if (roundTrip > p) {
                long k = (roundTrip - 1) / p;
                lastSent = k * p;
            }
            long arrival = lastSent + roundTrip;
            if (arrival > maxTime) {
                maxTime = arrival;
            }
        }

        return (int) (maxTime + 1);
    }
}
```

## Python

```python
class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        from collections import deque

        n = len(patience)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to compute shortest distance from master server (0)
        dist = [-1] * n
        q = deque([0])
        dist[0] = 0
        while q:
            node = q.popleft()
            dnext = dist[node] + 1
            for nb in graph[node]:
                if dist[nb] == -1:
                    dist[nb] = dnext
                    q.append(nb)

        max_time = 0
        for i in range(1, n):
            round_trip = 2 * dist[i]
            p = patience[i]
            if round_trip <= p:
                last_arrival = round_trip
            else:
                # number of extra sends before first reply arrives
                k = (round_trip - 1) // p
                last_sent = k * p
                last_arrival = last_sent + round_trip
            if last_arrival > max_time:
                max_time = last_arrival

        return max_time + 1
```

## Python3

```python
class Solution:
    def networkBecomesIdle(self, edges, patience):
        from collections import deque
        n = len(patience)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist = [-1] * n
        q = deque([0])
        dist[0] = 0
        while q:
            node = q.popleft()
            d = dist[node] + 1
            for nb in adj[node]:
                if dist[nb] == -1:
                    dist[nb] = d
                    q.append(nb)

        max_time = 0
        for i in range(1, n):
            round_trip = dist[i] * 2
            p = patience[i]
            if round_trip <= p:
                last_arrival = round_trip
            else:
                last_send = ((round_trip - 1) // p) * p
                last_arrival = last_send + round_trip
            if last_arrival > max_time:
                max_time = last_arrival

        return max_time + 1
```

## C

```c
int networkBecomesIdle(int** edges, int edgesSize, int* edgesColSize, int* patience, int patienceSize) {
    int n = patienceSize;
    // adjacency list
    int **adj = (int**)calloc(n, sizeof(int*));
    int *adjSize = (int*)calloc(n, sizeof(int));
    int *adjCap = (int*)calloc(n, sizeof(int));

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];

        if (adjSize[u] == adjCap[u]) {
            int newCap = adjCap[u] ? adjCap[u] * 2 : 2;
            adj[u] = (int*)realloc(adj[u], newCap * sizeof(int));
            adjCap[u] = newCap;
        }
        adj[u][adjSize[u]++] = v;

        if (adjSize[v] == adjCap[v]) {
            int newCap = adjCap[v] ? adjCap[v] * 2 : 2;
            adj[v] = (int*)realloc(adj[v], newCap * sizeof(int));
            adjCap[v] = newCap;
        }
        adj[v][adjSize[v]++] = u;
    }

    // BFS to compute shortest distances from node 0
    int *dist = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) dist[i] = -1;

    int *queue = (int*)malloc(n * sizeof(int));
    int front = 0, rear = 0;
    queue[rear++] = 0;
    dist[0] = 0;

    while (front < rear) {
        int u = queue[front++];
        for (int idx = 0; idx < adjSize[u]; ++idx) {
            int v = adj[u][idx];
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                queue[rear++] = v;
            }
        }
    }

    long long maxTime = 0;
    for (int i = 1; i < n; ++i) {
        int d = dist[i];
        int roundTrip = 2 * d;
        int p = patience[i];
        int lastSent = 0;
        if (p < roundTrip) {
            int k = (roundTrip - 1) / p;
            lastSent = k * p;
        }
        long long total = (long long)lastSent + roundTrip;
        if (total > maxTime) maxTime = total;
    }

    // free allocated memory (optional for LeetCode)
    for (int i = 0; i < n; ++i) {
        free(adj[i]);
    }
    free(adj);
    free(adjSize);
    free(adjCap);
    free(dist);
    free(queue);

    return (int)(maxTime + 1);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int NetworkBecomesIdle(int[][] edges, int[] patience) {
        int n = patience.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            graph[u].Add(v);
            graph[v].Add(u);
        }

        var dist = new int[n];
        Array.Fill(dist, -1);
        var queue = new Queue<int>();
        dist[0] = 0;
        queue.Enqueue(0);

        while (queue.Count > 0) {
            int u = queue.Dequeue();
            foreach (int v in graph[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    queue.Enqueue(v);
                }
            }
        }

        long maxTime = 0;
        for (int i = 1; i < n; i++) {
            long roundTrip = (long)dist[i] * 2;
            long p = patience[i];
            long lastSent = 0;
            if (roundTrip > p) {
                long k = (roundTrip - 1) / p;
                lastSent = k * p;
            }
            long arrival = lastSent + roundTrip;
            if (arrival > maxTime) maxTime = arrival;
        }

        return (int)(maxTime + 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} patience
 * @return {number}
 */
var networkBecomesIdle = function(edges, patience) {
    const n = patience.length;
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    
    const dist = new Int32Array(n).fill(-1);
    const queue = new Int32Array(n);
    let head = 0, tail = 0;
    dist[0] = 0;
    queue[tail++] = 0;
    
    while (head < tail) {
        const node = queue[head++];
        const d = dist[node] + 1;
        for (const nb of adj[node]) {
            if (dist[nb] === -1) {
                dist[nb] = d;
                queue[tail++] = nb;
            }
        }
    }
    
    let maxTime = 0;
    for (let i = 1; i < n; ++i) {
        const roundTrip = dist[i] * 2;
        const p = patience[i];
        let lastArrival;
        if (roundTrip <= p) {
            lastArrival = roundTrip;
        } else {
            const k = Math.floor((roundTrip - 1) / p);
            const lastSent = k * p;
            lastArrival = lastSent + roundTrip;
        }
        if (lastArrival > maxTime) maxTime = lastArrival;
    }
    
    return maxTime + 1;
};
```

## Typescript

```typescript
function networkBecomesIdle(edges: number[][], patience: number[]): number {
    const n = patience.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const dist = new Int32Array(n);
    dist.fill(-1);
    const queue: number[] = [];
    let head = 0;
    dist[0] = 0;
    queue.push(0);

    while (head < queue.length) {
        const node = queue[head++];
        for (const nb of adj[node]) {
            if (dist[nb] === -1) {
                dist[nb] = dist[node] + 1;
                queue.push(nb);
            }
        }
    }

    let maxTime = 0;
    for (let i = 1; i < n; i++) {
        const d = dist[i];
        const roundTrip = d * 2;
        const p = patience[i];
        let lastSent = 0;
        if (roundTrip > p) {
            const k = Math.floor((roundTrip - 1) / p);
            lastSent = k * p;
        }
        const total = lastSent + roundTrip;
        if (total > maxTime) maxTime = total;
    }

    return maxTime + 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer[] $patience
     * @return Integer
     */
    function networkBecomesIdle($edges, $patience) {
        $n = count($patience);
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v] = $e;
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        // BFS to compute shortest distances from node 0
        $dist = array_fill(0, $n, -1);
        $queue = new SplQueue();
        $queue->enqueue(0);
        $dist[0] = 0;

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            foreach ($adj[$node] as $nei) {
                if ($dist[$nei] === -1) {
                    $dist[$nei] = $dist[$node] + 1;
                    $queue->enqueue($nei);
                }
            }
        }

        $maxTime = 0;
        for ($i = 1; $i < $n; ++$i) {
            $roundTrip = $dist[$i] * 2;
            $p = $patience[$i];
            if ($roundTrip <= $p) {
                $lastArrival = $roundTrip;
            } else {
                $tLast = intdiv($roundTrip - 1, $p) * $p;
                $lastArrival = $tLast + $roundTrip;
            }
            if ($lastArrival > $maxTime) {
                $maxTime = $lastArrival;
            }
        }

        return $maxTime + 1;
    }
}
```

## Swift

```swift
class Solution {
    func networkBecomesIdle(_ edges: [[Int]], _ patience: [Int]) -> Int {
        let n = patience.count
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            let u = e[0]
            let v = e[1]
            graph[u].append(v)
            graph[v].append(u)
        }
        
        // BFS to compute shortest distances from node 0
        var dist = Array(repeating: -1, count: n)
        var queue = [Int]()
        var head = 0
        dist[0] = 0
        queue.append(0)
        while head < queue.count {
            let node = queue[head]
            head += 1
            for nb in graph[node] {
                if dist[nb] == -1 {
                    dist[nb] = dist[node] + 1
                    queue.append(nb)
                }
            }
        }
        
        var maxTime = 0
        for i in 1..<n {
            let d = dist[i]
            let roundTrip = d * 2
            let p = patience[i]
            var lastSent = 0
            if roundTrip > p {
                // largest multiple of p that is less than roundTrip
                lastSent = ((roundTrip - 1) / p) * p
            }
            let lastReply = lastSent + roundTrip
            if lastReply > maxTime {
                maxTime = lastReply
            }
        }
        
        return maxTime + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun networkBecomesIdle(edges: Array<IntArray>, patience: IntArray): Int {
        val n = patience.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        // BFS to compute shortest distances from node 0
        val dist = IntArray(n) { -1 }
        val queue = IntArray(n)
        var head = 0
        var tail = 0
        queue[tail++] = 0
        dist[0] = 0

        while (head < tail) {
            val cur = queue[head++]
            for (nei in adj[cur]) {
                if (dist[nei] == -1) {
                    dist[nei] = dist[cur] + 1
                    queue[tail++] = nei
                }
            }
        }

        var maxTime = 0L
        for (i in 1 until n) {
            val roundTrip = dist[i] * 2
            val p = patience[i]
            val lastSent = if (roundTrip <= p) 0 else ((roundTrip - 1) / p) * p
            val idleTime = lastSent + roundTrip
            if (idleTime > maxTime) {
                maxTime = idleTime.toLong()
            }
        }

        return (maxTime + 1).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int networkBecomesIdle(List<List<int>> edges, List<int> patience) {
    int n = patience.length;
    List<List<int>> graph = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      graph[u].add(v);
      graph[v].add(u);
    }

    // BFS to compute shortest distances from node 0
    List<int> dist = List.filled(n, -1);
    List<int> queue = [];
    int head = 0;
    dist[0] = 0;
    queue.add(0);

    while (head < queue.length) {
      int cur = queue[head++];
      for (int nb in graph[cur]) {
        if (dist[nb] == -1) {
          dist[nb] = dist[cur] + 1;
          queue.add(nb);
        }
      }
    }

    int maxTime = 0;
    for (int i = 1; i < n; ++i) {
      int roundTrip = 2 * dist[i];
      int p = patience[i];
      int lastArrival;
      if (roundTrip <= p) {
        lastArrival = roundTrip;
      } else {
        int k = (roundTrip - 1) ~/ p;
        int lastSent = k * p;
        lastArrival = lastSent + roundTrip;
      }
      if (lastArrival > maxTime) maxTime = lastArrival;
    }

    return maxTime + 1;
  }
}
```

## Golang

```go
func networkBecomesIdle(edges [][]int, patience []int) int {
    n := len(patience)
    adj := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }

    dist := make([]int, n)
    for i := 0; i < n; i++ {
        dist[i] = -1
    }
    queue := make([]int, 0, n)
    dist[0] = 0
    queue = append(queue, 0)

    for head := 0; head < len(queue); head++ {
        cur := queue[head]
        for _, nb := range adj[cur] {
            if dist[nb] == -1 {
                dist[nb] = dist[cur] + 1
                queue = append(queue, nb)
            }
        }
    }

    maxTime := 0
    for i := 1; i < n; i++ {
        roundTrip := dist[i] * 2
        p := patience[i]
        var lastSend int
        if roundTrip <= p {
            lastSend = 0
        } else {
            k := (roundTrip - 1) / p
            lastSend = k * p
        }
        total := lastSend + roundTrip
        if total > maxTime {
            maxTime = total
        }
    }

    return maxTime + 1
}
```

## Ruby

```ruby
def network_becomes_idle(edges, patience)
  n = patience.length
  graph = Array.new(n) { [] }
  edges.each do |u, v|
    graph[u] << v
    graph[v] << u
  end

  dist = Array.new(n, -1)
  queue = [0]
  dist[0] = 0
  idx = 0
  while idx < queue.length
    cur = queue[idx]
    idx += 1
    ndist = dist[cur] + 1
    graph[cur].each do |nbr|
      if dist[nbr] == -1
        dist[nbr] = ndist
        queue << nbr
      end
    end
  end

  max_time = 0
  (1...n).each do |i|
    round_trip = dist[i] * 2
    p = patience[i]
    if round_trip <= p
      last_arrival = round_trip
    else
      t_last = ((round_trip - 1) / p) * p
      last_arrival = t_last + round_trip
    end
    max_time = last_arrival if last_arrival > max_time
  end

  max_time + 1
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.{ArrayBuffer, Queue}
    def networkBecomesIdle(edges: Array[Array[Int]], patience: Array[Int]): Int = {
        val n = patience.length
        val adj = Array.fill(n)(new ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            adj(v).append(u)
        }

        // BFS to compute shortest distances from node 0
        val dist = Array.fill(n)(-1)
        val q = new Queue[Int]()
        dist(0) = 0
        q.enqueue(0)

        while (q.nonEmpty) {
            val cur = q.dequeue()
            val dCur = dist(cur)
            for (nbr <- adj(cur)) {
                if (dist(nbr) == -1) {
                    dist(nbr) = dCur + 1
                    q.enqueue(nbr)
                }
            }
        }

        var maxTime: Long = 0L
        for (i <- 1 until n) {
            val roundTrip = 2L * dist(i).toLong
            val p = patience(i).toLong
            val lastSend =
                if (roundTrip <= p) 0L
                else ((roundTrip - 1) / p) * p
            val lastReply = lastSend + roundTrip
            if (lastReply > maxTime) maxTime = lastReply
        }

        (maxTime + 1).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn network_becomes_idle(edges: Vec<Vec<i32>>, patience: Vec<i32>) -> i32 {
        let n = patience.len();
        let mut graph: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            graph[u].push(v);
            graph[v].push(u);
        }

        // BFS to compute shortest distances from node 0
        let mut dist: Vec<i32> = vec![-1; n];
        let mut queue = std::collections::VecDeque::new();
        dist[0] = 0;
        queue.push_back(0usize);
        while let Some(node) = queue.pop_front() {
            let d = dist[node];
            for &nbr in graph[node].iter() {
                if dist[nbr] == -1 {
                    dist[nbr] = d + 1;
                    queue.push_back(nbr);
                }
            }
        }

        // Determine the latest time a reply arrives
        let mut max_time: i64 = 0;
        for i in 1..n {
            let d = dist[i] as i64;
            let round_trip = d * 2;               // time for message to go and return
            let p = patience[i] as i64;
            // last message sent before the reply arrives
            let last_sent = ((round_trip - 1) / p) * p;
            let arrival = last_sent + round_trip; // when its reply finally returns
            if arrival > max_time {
                max_time = arrival;
            }
        }

        (max_time + 1) as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (network-becomes-idle edges patience)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ((n (length patience))
         (adj (make-vector n '()))
         (dist (make-vector n -1)))
    ;; build adjacency list
    (for ([e edges])
      (define u (car e))
      (define v (cadr e))
      (vector-set! adj u (cons v (vector-ref adj u)))
      (vector-set! adj v (cons u (vector-ref adj v))))
    ;; BFS from node 0
    (define q (make-vector n 0))
    (define head 0)
    (define tail 0)
    (vector-set! dist 0 0)
    (vector-set! q tail 0)
    (set! tail (+ tail 1))
    (let bfs ()
      (when (< head tail)
        (define cur (vector-ref q head))
        (set! head (+ head 1))
        (for ([nbr (in-list (vector-ref adj cur))])
          (when (= (vector-ref dist nbr) -1)
            (vector-set! dist nbr (+ (vector-ref dist cur) 1))
            (vector-set! q tail nbr)
            (set! tail (+ tail 1))))
        (bfs)))
    (bfs)
    ;; compute the time when network becomes idle
    (define max-time 0)
    (for ([i (in-range 1 n)])
      (define d (* 2 (vector-ref dist i))) ; round‑trip time
      (define p (list-ref patience i))
      (define arrival
        (if (<= d p)
            d
            (+ (* (quotient (- d 1) p) p) d)))
      (when (> arrival max-time)
        (set! max-time arrival)))
    (+ max-time 1)))
```

## Erlang

```erlang
-module(solution).
-export([network_becomes_idle/2]).

-spec network_becomes_idle(Edges :: [[integer()]], Patience :: [integer()]) -> integer().
network_becomes_idle(Edges, Patience) ->
    N = length(Patience),
    Adj = build_adj(Edges, #{}),
    DistMap = bfs(Adj),
    PatTuple = list_to_tuple(Patience),
    MaxArrival =
        lists:foldl(
            fun(Node, Acc) ->
                Dist = maps:get(Node, DistMap),
                Pat = element(Node + 1, PatTuple),
                RoundTrip = 2 * Dist,
                LastSent = if
                    Pat == 0 -> 0;
                    true -> ((RoundTrip - 1) div Pat) * Pat
                end,
                Arrival = LastSent + RoundTrip,
                erlang:max(Acc, Arrival)
            end,
            0,
            lists:seq(1, N - 1)
        ),
    MaxArrival + 1.

%% Build adjacency map from edges
build_adj([], Adj) -> Adj;
build_adj([[U, V] | Rest], Adj) ->
    Adj1 = maps:update_with(U, fun(L) -> [V | L] end, [V], Adj),
    Adj2 = maps:update_with(V, fun(L) -> [U | L] end, [U], Adj1),
    build_adj(Rest, Adj2).

%% BFS to compute shortest distances from node 0
bfs(Adj) ->
    Q0 = queue:in(0, queue:new()),
    DistMap0 = #{0 => 0},
    bfs_loop(Q0, Adj, DistMap0).

bfs_loop(Q, Adj, DistMap) ->
    case queue:out(Q) of
        {empty, _} ->
            DistMap;
        {{value, Node}, Q1} ->
            CurrDist = maps:get(Node, DistMap),
            Neighbors = maps:get(Node, Adj, []),
            {Q2, DistMap2} =
                lists:foldl(
                    fun(Nei, {AccQ, AccMap}) ->
                        case maps:is_key(Nei, AccMap) of
                            true -> {AccQ, AccMap};
                            false ->
                                NewDist = CurrDist + 1,
                                {queue:in(Nei, AccQ), AccMap#{Nei => NewDist}}
                        end
                    end,
                    {Q1, DistMap},
                    Neighbors
                ),
            bfs_loop(Q2, Adj, DistMap2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec network_becomes_idle(edges :: [[integer]], patience :: [integer]) :: integer
  def network_becomes_idle(edges, patience) do
    n = length(patience)
    adj = build_adj(n, edges)

    dist = bfs(adj, n)

    max_time =
      1..(n - 1)
      |> Enum.reduce(0, fn i, acc ->
        rt = 2 * :array.get(i, dist)
        p = Enum.at(patience, i)
        last_send = if rt <= p, do: 0, else: div(rt - 1, p) * p
        total = last_send + rt
        if total > acc, do: total, else: acc
      end)

    max_time + 1
  end

  defp build_adj(n, edges) do
    Enum.reduce(edges, :array.new(n, []), fn [u, v], arr ->
      arr = :array.set(u, [v | :array.get(u, arr)], arr)
      :array.set(v, [u | :array.get(v, arr)], arr)
    end)
  end

  defp bfs(adj, n) do
    dist = :array.new(n, -1)
    dist = :array.set(0, 0, dist)
    queue = :queue.from_list([0])
    bfs_loop(queue, adj, dist)
  end

  defp bfs_loop(queue, adj, dist) do
    case :queue.out(queue) do
      {:empty, _} ->
        dist

      {{:value, node}, q2} ->
        d = :array.get(node, dist)
        neighbors = :array.get(node, adj)

        {new_queue, new_dist} =
          Enum.reduce(neighbors, {q2, dist}, fn nb, {qacc, dacc} ->
            if :array.get(nb, dacc) == -1 do
              ndist = d + 1
              dacc = :array.set(nb, ndist, dacc)
              qacc = :queue.in(nb, qacc)
              {qacc, dacc}
            else
              {qacc, dacc}
            end
          end)

        bfs_loop(new_queue, adj, new_dist)
    end
  end
end
```

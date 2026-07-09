# 2492. Minimum Score of a Path Between Two Cities

## Cpp

```cpp
class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int,int>>> adj(n + 1);
        for (auto &r : roads) {
            int u = r[0], v = r[1], w = r[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        vector<char> visited(n + 1, false);
        queue<int> q;
        q.push(1);
        visited[1] = true;
        int ans = INT_MAX;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : adj[u]) {
                int v = e.first, w = e.second;
                ans = min(ans, w);
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minScore(int n, int[][] roads) {
        DSU dsu = new DSU(n + 1);
        for (int[] r : roads) {
            dsu.union(r[0], r[1]);
        }
        int root = dsu.find(1);
        int ans = Integer.MAX_VALUE;
        for (int[] r : roads) {
            if (dsu.find(r[0]) == root && dsu.find(r[1]) == root) {
                ans = Math.min(ans, r[2]);
            }
        }
        return ans;
    }

    private static class DSU {
        int[] parent;
        byte[] rank;

        DSU(int size) {
            parent = new int[size];
            rank = new byte[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
        }

        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb;
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra;
            } else {
                parent[rb] = ra;
                rank[ra]++;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n + 1)]
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))

        from collections import deque
        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        min_score = float('inf')

        while q:
            u = q.popleft()
            for v, w in adj[u]:
                if w < min_score:
                    min_score = w
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        return min_score
```

## Python3

```python
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for a, b, w in roads:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * (n + 1)
        stack = [1]
        visited[1] = True
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        min_edge = float('inf')
        for a, b, w in roads:
            if visited[a] and visited[b]:
                if w < min_edge:
                    min_edge = w

        return min_edge
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minScore(int n, int** roads, int roadsSize, int* roadsColSize) {
    struct Edge { int to; int w; int next; };
    
    int m = roadsSize;
    int totalEdges = m * 2;
    struct Edge *edges = (struct Edge *)malloc(sizeof(struct Edge) * totalEdges);
    int *head = (int *)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; ++i) head[i] = -1;
    
    int idx = 0;
    for (int i = 0; i < m; ++i) {
        int a = roads[i][0];
        int b = roads[i][1];
        int d = roads[i][2];
        edges[idx].to = b;
        edges[idx].w = d;
        edges[idx].next = head[a];
        head[a] = idx++;
        
        edges[idx].to = a;
        edges[idx].w = d;
        edges[idx].next = head[b];
        head[b] = idx++;
    }
    
    char *vis = (char *)calloc(n + 1, sizeof(char));
    int *stack = (int *)malloc((n + 5) * sizeof(int));
    int top = 0;
    stack[top++] = 1;
    vis[1] = 1;
    
    int ans = INT_MAX;
    while (top) {
        int u = stack[--top];
        for (int e = head[u]; e != -1; e = edges[e].next) {
            int v = edges[e].to;
            int w = edges[e].w;
            if (w < ans) ans = w;
            if (!vis[v]) {
                vis[v] = 1;
                stack[top++] = v;
            }
        }
    }
    
    free(edges);
    free(head);
    free(vis);
    free(stack);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinScore(int n, int[][] roads) {
        var adj = new List<(int to, int w)>[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new List<(int, int)>();
        foreach (var r in roads) {
            int a = r[0], b = r[1], d = r[2];
            adj[a].Add((b, d));
            adj[b].Add((a, d));
        }

        var visited = new bool[n + 1];
        var q = new Queue<int>();
        visited[1] = true;
        q.Enqueue(1);
        int minDist = int.MaxValue;

        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (var (v, w) in adj[u]) {
                if (w < minDist) minDist = w;
                if (!visited[v]) {
                    visited[v] = true;
                    q.Enqueue(v);
                }
            }
        }

        return minDist;
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
var minScore = function(n, roads) {
    const adj = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of roads) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const visited = new Uint8Array(n + 1);
    const stack = [1];
    visited[1] = 1;

    while (stack.length) {
        const node = stack.pop();
        for (const nb of adj[node]) {
            if (!visited[nb]) {
                visited[nb] = 1;
                stack.push(nb);
            }
        }
    }

    let ans = Infinity;
    for (const [u, v, w] of roads) {
        if (visited[u] && visited[v] && w < ans) {
            ans = w;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minScore(n: number, roads: number[][]): number {
    const adj: [number, number][][] = Array.from({ length: n + 1 }, () => []);
    for (const [a, b, d] of roads) {
        adj[a].push([b, d]);
        adj[b].push([a, d]);
    }
    const visited = new Uint8Array(n + 1);
    let minDist = Number.MAX_SAFE_INTEGER;
    const stack: number[] = [1];
    visited[1] = 1;
    while (stack.length) {
        const u = stack.pop()!;
        for (const [v, w] of adj[u]) {
            if (w < minDist) minDist = w;
            if (!visited[v]) {
                visited[v] = 1;
                stack.push(v);
            }
        }
    }
    return minDist;
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
    function minScore($n, $roads) {
        // Build adjacency list
        $adj = array_fill(0, $n + 1, []);
        foreach ($roads as $road) {
            [$a, $b, $d] = $road;
            $adj[$a][] = [$b, $d];
            $adj[$b][] = [$a, $d];
        }

        // BFS to find all nodes reachable from city 1
        $visited = array_fill(0, $n + 1, false);
        $queue = new SplQueue();
        $queue->enqueue(1);
        $visited[1] = true;

        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            foreach ($adj[$u] as $edge) {
                [$v, $d] = $edge;
                if (!$visited[$v]) {
                    $visited[$v] = true;
                    $queue->enqueue($v);
                }
            }
        }

        // Minimum edge weight among edges whose both ends are in the reachable component
        $ans = PHP_INT_MAX;
        foreach ($roads as $road) {
            [$a, $b, $d] = $road;
            if ($visited[$a] && $visited[$b]) {
                if ($d < $ans) {
                    $ans = $d;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minScore(_ n: Int, _ roads: [[Int]]) -> Int {
        var adj = Array(repeating: [(to: Int, w: Int)](), count: n + 1)
        for r in roads {
            let a = r[0], b = r[1], w = r[2]
            adj[a].append((b, w))
            adj[b].append((a, w))
        }
        var visited = Array(repeating: false, count: n + 1)
        var stack = [Int]()
        stack.append(1)
        visited[1] = true
        var answer = Int.max
        while let node = stack.popLast() {
            for edge in adj[node] {
                if edge.w < answer { answer = edge.w }
                if !visited[edge.to] {
                    visited[edge.to] = true
                    stack.append(edge.to)
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minScore(n: Int, roads: Array<IntArray>): Int {
        val adj = Array(n + 1) { mutableListOf<Pair<Int, Int>>() }
        for (r in roads) {
            val a = r[0]
            val b = r[1]
            val d = r[2]
            adj[a].add(Pair(b, d))
            adj[b].add(Pair(a, d))
        }

        val visited = BooleanArray(n + 1)
        val deque: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        deque.add(1)
        visited[1] = true
        while (!deque.isEmpty()) {
            val u = deque.poll()
            for ((v, _) in adj[u]) {
                if (!visited[v]) {
                    visited[v] = true
                    deque.add(v)
                }
            }
        }

        var answer = Int.MAX_VALUE
        for (r in roads) {
            if (visited[r[0]] && visited[r[1]]) {
                answer = kotlin.math.min(answer, r[2])
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minScore(int n, List<List<int>> roads) {
    // Build adjacency list
    List<List<List<int>>> adj = List.generate(n + 1, (_) => []);
    for (var r in roads) {
      int u = r[0];
      int v = r[1];
      int w = r[2];
      adj[u].add([v, w]);
      adj[v].add([u, w]);
    }

    List<bool> visited = List.filled(n + 1, false);
    List<int> stack = [1];
    visited[1] = true;
    int minEdge = 1 << 30; // sufficiently large

    while (stack.isNotEmpty) {
      int u = stack.removeLast();
      for (var edge in adj[u]) {
        int v = edge[0];
        int w = edge[1];
        if (w < minEdge) minEdge = w;
        if (!visited[v]) {
          visited[v] = true;
          stack.add(v);
        }
      }
    }

    return minEdge;
  }
}
```

## Golang

```go
func minScore(n int, roads [][]int) int {
	adj := make([][]struct{ to, w int }, n+1)
	for _, r := range roads {
		a, b, d := r[0], r[1], r[2]
		adj[a] = append(adj[a], struct{ to, w int }{b, d})
		adj[b] = append(adj[b], struct{ to, w int }{a, d})
	}
	visited := make([]bool, n+1)
	queue := []int{1}
	visited[1] = true
	const INF = int(1e9)
	minScore := INF

	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		for _, e := range adj[u] {
			if e.w < minScore {
				minScore = e.w
			}
			if !visited[e.to] {
				visited[e.to] = true
				queue = append(queue, e.to)
			}
		}
	}
	return minScore
}
```

## Ruby

```ruby
def min_score(n, roads)
  adj = Array.new(n + 1) { [] }
  roads.each do |a, b, d|
    adj[a] << [b, d]
    adj[b] << [a, d]
  end

  visited = Array.new(n + 1, false)
  stack = [1]
  visited[1] = true
  min_val = (1 << 60)

  until stack.empty?
    u = stack.pop
    adj[u].each do |v, w|
      min_val = w if w < min_val
      next if visited[v]

      visited[v] = true
      stack << v
    end
  end

  min_val
end
```

## Scala

```scala
object Solution {
  def minScore(n: Int, roads: Array[Array[Int]]): Int = {
    val adj = Array.fill[List[(Int, Int)]](n + 1)(Nil)
    for (r <- roads) {
      val a = r(0)
      val b = r(1)
      val d = r(2)
      adj(a) = (b, d) :: adj(a)
      adj(b) = (a, d) :: adj(b)
    }

    val visited = new Array[Boolean](n + 1)
    val stack = scala.collection.mutable.Stack[Int]()
    stack.push(1)
    visited(1) = true

    while (stack.nonEmpty) {
      val u = stack.pop()
      for ((v, _) <- adj(u)) {
        if (!visited(v)) {
          visited(v) = true
          stack.push(v)
        }
      }
    }

    var ans = Int.MaxValue
    for (r <- roads) {
      val a = r(0)
      val b = r(1)
      val d = r(2)
      if (visited(a) || visited(b)) {
        if (d < ans) ans = d
      }
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize + 1];
        for r in &roads {
            let a = r[0] as usize;
            let b = r[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        let mut visited = vec![false; n_usize + 1];
        let mut stack = Vec::new();
        stack.push(1usize);
        visited[1] = true;

        while let Some(u) = stack.pop() {
            for &v in &adj[u] {
                if !visited[v] {
                    visited[v] = true;
                    stack.push(v);
                }
            }
        }

        let mut ans = i32::MAX;
        for r in &roads {
            let a = r[0] as usize;
            let b = r[1] as usize;
            let d = r[2];
            if visited[a] && visited[b] && d < ans {
                ans = d;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-score n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((adj (make-vector (+ n 1) '()))
         (add-edge
          (lambda (a b w)
            (vector-set! adj a (cons (list b w) (vector-ref adj a)))
            (vector-set! adj b (cons (list a w) (vector-ref adj b))))))
    ;; build adjacency list
    (for-each (lambda (road)
                (match road
                  [(list a b w) (add-edge a b w)]))
              roads)
    (let ((visited (make-vector (+ n 1) #f))
          (stack (list 1))
          (min-w (box 1000000))) ; larger than any possible distance
      (vector-set! visited 1 #t)
      (let loop ()
        (if (null? stack)
            (unbox min-w)
            (begin
              (define node (car stack))
              (set! stack (cdr stack))
              (for-each (lambda (nbr)
                          (match nbr
                            [(list nb w)
                             (when (< w (unbox min-w)) (set-box! min-w w))
                             (unless (vector-ref visited nb)
                               (vector-set! visited nb #t)
                               (set! stack (cons nb stack))) ]))
                        (vector-ref adj node))
              (loop)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_score/2]).

-spec min_score(N :: integer(), Roads :: [[integer()]]) -> integer().
min_score(_N, Roads) ->
    Adj = build_adj(Roads),
    bfs(queue:from_list([1]), #{1 => true}, Adj, 1000000).

build_adj(Roads) ->
    lists:foldl(fun([A,B,D], Acc) ->
        Acc1 = maps:update_with(A,
                fun(L) -> [{B,D}|L] end,
                [{B,D}],
                Acc),
        maps:update_with(B,
                fun(L) -> [{A,D}|L] end,
                [{A,D}],
                Acc1)
    end, #{}, Roads).

bfs(Queue, Visited, Adj, Min) ->
    case queue:out(Queue) of
        {empty, _} ->
            Min;
        {{value, Node}, Q1} ->
            Edges = maps:get(Node, Adj, []),
            {Vis2, Q2, Min2} =
                lists:foldl(fun({Nei,W}, {VAcc, QAcc, CurMin}) ->
                    NewMin = erlang:min(CurMin, W),
                    case maps:is_key(Nei, VAcc) of
                        true -> {VAcc, QAcc, NewMin};
                        false ->
                            {maps:put(Nei, true, VAcc), queue:in(Nei, QAcc), NewMin}
                    end
                end, {Visited, Q1, Min}, Edges),
            bfs(Q2, Vis2, Adj, Min2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_score(n :: integer, roads :: [[integer]]) :: integer
  def min_score(_n, roads) do
    adj =
      Enum.reduce(roads, %{}, fn [a, b, w], acc ->
        acc
        |> Map.update(a, [{b, w}], &[{b, w} | &1])
        |> Map.update(b, [{a, w}], &[{a, w} | &1])
      end)

    bfs(:queue.in(1, :queue.new()), adj, MapSet.new([1]), 1_000_001)
  end

  defp bfs(queue, adj, visited, min_w) do
    case :queue.out(queue) do
      {:empty, _} ->
        min_w

      {{:value, node}, q2} ->
        {new_min, new_vis, new_q} =
          Enum.reduce(Map.get(adj, node, []), {min_w, visited, q2}, fn {nbr, w},
                                                                      {cur_min, cur_vis,
                                                                       cur_q} ->
            min_val = if w < cur_min, do: w, else: cur_min

            if MapSet.member?(cur_vis, nbr) do
              {min_val, cur_vis, cur_q}
            else
              {min_val, MapSet.put(cur_vis, nbr), :queue.in(nbr, cur_q)}
            end
          end)

        bfs(new_q, adj, new_vis, new_min)
    end
  end
end
```

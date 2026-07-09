# 1761. Minimum Degree of a Connected Trio in a Graph

## Cpp

```cpp
class Solution {
public:
    int minTrioDegree(int n, vector<vector<int>>& edges) {
        vector<vector<char>> adj(n + 1, vector<char>(n + 1, 0));
        vector<int> deg(n + 1, 0);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u][v] = adj[v][u] = 1;
            ++deg[u];
            ++deg[v];
        }
        int ans = INT_MAX;
        for (int i = 1; i <= n; ++i) {
            for (int j = i + 1; j <= n; ++j) {
                if (!adj[i][j]) continue;
                for (int k = j + 1; k <= n; ++k) {
                    if (adj[i][k] && adj[j][k]) {
                        int cur = deg[i] + deg[j] + deg[k] - 6;
                        ans = min(ans, cur);
                    }
                }
            }
        }
        return ans == INT_MAX ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minTrioDegree(int n, int[][] edges) {
        boolean[][] adj = new boolean[n + 1][n + 1];
        int[] deg = new int[n + 1];
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            adj[u][v] = true;
            adj[v][u] = true;
            deg[u]++;
            deg[v]++;
        }
        int ans = Integer.MAX_VALUE;
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            for (int w = 1; w <= n; ++w) {
                if (w == u || w == v) continue;
                if (adj[u][w] && adj[v][w]) {
                    int degree = deg[u] + deg[v] + deg[w] - 6;
                    if (degree < ans) ans = degree;
                }
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
```

## Python

```python
class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [set() for _ in range(n + 1)]
        deg = [0] * (n + 1)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            deg[u] += 1
            deg[v] += 1

        ans = float('inf')
        for u in range(1, n + 1):
            for v in adj[u]:
                if v <= u:
                    continue
                # iterate over neighbors of v to find w forming a trio
                for w in adj[v]:
                    if w <= v:
                        continue
                    if w in adj[u]:  # triangle exists
                        cur = deg[u] + deg[v] + deg[w] - 6
                        if cur < ans:
                            ans = cur

        return -1 if ans == float('inf') else ans
```

## Python3

```python
from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        deg = [0] * (n + 1)
        neigh = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u][v] = adj[v][u] = True
            deg[u] += 1
            deg[v] += 1
            neigh[u].append(v)
            neigh[v].append(u)

        INF = float('inf')
        ans = INF

        for u, v in edges:
            # iterate over neighbors of the node with smaller degree to reduce work
            if len(neigh[u]) > len(neigh[v]):
                u, v = v, u
            for w in neigh[u]:
                if w == v:
                    continue
                if adj[v][w]:
                    cur = deg[u] + deg[v] + deg[w] - 6
                    if cur < ans:
                        ans = cur

        return -1 if ans == INF else ans
```

## C

```c
#include <limits.h>

int minTrioDegree(int n, int** edges, int edgesSize, int* edgesColSize) {
    static char adj[401][401];
    int deg[401] = {0};
    
    // Initialize adjacency matrix to 0 (static already zeroed)
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][v] = adj[v][u] = 1;
        deg[u]++;
        deg[v]++;
    }
    
    int ans = INT_MAX;
    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            if (!adj[i][j]) continue;
            for (int k = j + 1; k <= n; ++k) {
                if (adj[i][k] && adj[j][k]) {
                    int cur = deg[i] + deg[j] + deg[k] - 6;
                    if (cur < ans) ans = cur;
                }
            }
        }
    }
    
    return (ans == INT_MAX) ? -1 : ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinTrioDegree(int n, int[][] edges) {
        var adj = new bool[n + 1, n + 1];
        var degree = new int[n + 1];
        var graph = new List<int>[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new List<int>();

        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u, v] = adj[v, u] = true;
            degree[u]++;
            degree[v]++;
            graph[u].Add(v);
            graph[v].Add(u);
        }

        int minDegree = int.MaxValue;

        for (int u = 1; u <= n; u++) {
            var neighbors = graph[u];
            int cnt = neighbors.Count;
            for (int i = 0; i < cnt; i++) {
                int v = neighbors[i];
                if (v == u) continue;
                for (int j = i + 1; j < cnt; j++) {
                    int w = neighbors[j];
                    if (w == u) continue;
                    if (adj[v, w]) {
                        int trioDegree = degree[u] + degree[v] + degree[w] - 6;
                        if (trioDegree < minDegree) minDegree = trioDegree;
                    }
                }
            }
        }

        return minDegree == int.MaxValue ? -1 : minDegree;
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
var minTrioDegree = function(n, edges) {
    const deg = new Uint16Array(n + 1);
    const adj = Array.from({ length: n + 1 }, () => []);
    const mat = Array.from({ length: n + 1 }, () => new Uint8Array(n + 1));
    
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
        deg[u]++;
        deg[v]++;
        mat[u][v] = 1;
        mat[v][u] = 1;
    }
    
    let ans = Infinity;
    
    for (const [a, b] of edges) {
        let u = a, v = b;
        // iterate over neighbors of the node with smaller degree
        if (deg[u] > deg[v]) {
            [u, v] = [v, u];
        }
        for (const w of adj[u]) {
            if (w === v) continue;
            if (mat[w][v]) {
                const cur = deg[u] + deg[v] + deg[w] - 6;
                if (cur < ans) ans = cur;
            }
        }
    }
    
    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function minTrioDegree(n: number, edges: number[][]): number {
    const adj: Uint8Array[] = Array.from({ length: n + 1 }, () => new Uint8Array(n + 1));
    const degree = new Int32Array(n + 1);
    for (const [u, v] of edges) {
        adj[u][v] = 1;
        adj[v][u] = 1;
        degree[u]++;
        degree[v]++;
    }
    let ans = Infinity;
    for (let i = 1; i <= n; i++) {
        for (let j = i + 1; j <= n; j++) {
            if (!adj[i][j]) continue;
            for (let k = j + 1; k <= n; k++) {
                if (adj[i][k] && adj[j][k]) {
                    const cur = degree[i] + degree[j] + degree[k] - 6;
                    if (cur < ans) ans = cur;
                }
            }
        }
    }
    return ans === Infinity ? -1 : ans;
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
    function minTrioDegree($n, $edges) {
        // degree of each node
        $deg = array_fill(0, $n + 1, 0);
        // adjacency matrix
        $adj = array_fill(0, $n + 1, []);
        for ($i = 0; $i <= $n; $i++) {
            $adj[$i] = array_fill(0, $n + 1, false);
        }

        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][$v] = true;
            $adj[$v][$u] = true;
            $deg[$u]++;
            $deg[$v]++;
        }

        $minDegree = PHP_INT_MAX;

        for ($i = 1; $i <= $n - 2; $i++) {
            for ($j = $i + 1; $j <= $n - 1; $j++) {
                if (!$adj[$i][$j]) continue;
                for ($k = $j + 1; $k <= $n; $k++) {
                    if ($adj[$i][$k] && $adj[$j][$k]) {
                        $degree = $deg[$i] + $deg[$j] + $deg[$k] - 6;
                        if ($degree < $minDegree) {
                            $minDegree = $degree;
                        }
                    }
                }
            }
        }

        return $minDegree === PHP_INT_MAX ? -1 : $minDegree;
    }
}
```

## Swift

```swift
class Solution {
    func minTrioDegree(_ n: Int, _ edges: [[Int]]) -> Int {
        var adj = Array(repeating: Array(repeating: false, count: n + 1), count: n + 1)
        var degree = Array(repeating: 0, count: n + 1)
        
        for e in edges {
            let u = e[0]
            let v = e[1]
            adj[u][v] = true
            adj[v][u] = true
            degree[u] += 1
            degree[v] += 1
        }
        
        var answer = Int.max
        
        if n < 3 { return -1 }
        
        for u in 1...n {
            if u == n { break }
            for v in (u + 1)...n {
                if !adj[u][v] { continue }
                if v == n { continue }
                for w in (v + 1)...n {
                    if adj[u][w] && adj[v][w] {
                        let cur = degree[u] + degree[v] + degree[w] - 6
                        if cur < answer {
                            answer = cur
                        }
                    }
                }
            }
        }
        
        return answer == Int.max ? -1 : answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minTrioDegree(n: Int, edges: Array<IntArray>): Int {
        val adj = Array(n + 1) { BooleanArray(n + 1) }
        val degree = IntArray(n + 1)
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u][v] = true
            adj[v][u] = true
            degree[u]++
            degree[v]++
        }
        var ans = Int.MAX_VALUE
        for (i in 1..n) {
            val neighbors = mutableListOf<Int>()
            for (j in 1..n) {
                if (adj[i][j]) neighbors.add(j)
            }
            val sz = neighbors.size
            for (aIdx in 0 until sz) {
                val a = neighbors[aIdx]
                for (bIdx in aIdx + 1 until sz) {
                    val b = neighbors[bIdx]
                    if (adj[a][b]) {
                        val deg = degree[i] + degree[a] + degree[b] - 6
                        if (deg < ans) ans = deg
                    }
                }
            }
        }
        return if (ans == Int.MAX_VALUE) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  int minTrioDegree(int n, List<List<int>> edges) {
    // adjacency matrix
    List<List<bool>> adj = List.generate(n + 1, (_) => List.filled(n + 1, false));
    List<int> degree = List.filled(n + 1, 0);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u][v] = true;
      adj[v][u] = true;
      degree[u]++;
      degree[v]++;
    }

    const int INF = 1 << 30;
    int ans = INF;

    for (int i = 1; i <= n; ++i) {
      for (int j = i + 1; j <= n; ++j) {
        if (!adj[i][j]) continue;
        for (int k = j + 1; k <= n; ++k) {
          if (adj[i][k] && adj[j][k]) {
            int cur = degree[i] + degree[j] + degree[k] - 6;
            if (cur < ans) ans = cur;
          }
        }
      }
    }

    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func minTrioDegree(n int, edges [][]int) int {
    // adjacency matrix
    adj := make([][]bool, n+1)
    for i := 0; i <= n; i++ {
        adj[i] = make([]bool, n+1)
    }
    deg := make([]int, n+1)

    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u][v] = true
        adj[v][u] = true
        deg[u]++
        deg[v]++
    }

    const INF = int(^uint(0) >> 1) // max int
    ans := INF

    for i := 1; i <= n; i++ {
        for j := i + 1; j <= n; j++ {
            if !adj[i][j] {
                continue
            }
            for k := j + 1; k <= n; k++ {
                if adj[i][k] && adj[j][k] {
                    cur := deg[i] + deg[j] + deg[k] - 6
                    if cur < ans {
                        ans = cur
                    }
                }
            }
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
def min_trio_degree(n, edges)
  adj = Array.new(n + 1) { [] }
  mat = Array.new(n + 1) { Array.new(n + 1, false) }
  deg = Array.new(n + 1, 0)

  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
    mat[u][v] = true
    mat[v][u] = true
    deg[u] += 1
    deg[v] += 1
  end

  ans = Float::INFINITY

  edges.each do |u, v|
    adj[u].each do |w|
      next if w == v
      if mat[v][w]
        cur = deg[u] + deg[v] + deg[w] - 6
        ans = cur if cur < ans
      end
    end
  end

  ans == Float::INFINITY ? -1 : ans
end
```

## Scala

```scala
object Solution {
    def minTrioDegree(n: Int, edges: Array[Array[Int]]): Int = {
        val adj = Array.ofDim[Boolean](n + 1, n + 1)
        val degree = new Array[Int](n + 1)

        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u)(v) = true
            adj(v)(u) = true
            degree(u) += 1
            degree(v) += 1
        }

        var ans = Int.MaxValue

        for (i <- 1 to n) {
            for (j <- i + 1 to n if adj(i)(j)) {
                for (k <- j + 1 to n if adj(i)(k) && adj(j)(k)) {
                    val deg = degree(i) + degree(j) + degree(k) - 6
                    if (deg < ans) ans = deg
                }
            }
        }

        if (ans == Int.MaxValue) -1 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_trio_degree(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj = vec![vec![false; n + 1]; n + 1];
        let mut degree = vec![0i32; n + 1];

        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u][v] = true;
            adj[v][u] = true;
            degree[u] += 1;
            degree[v] += 1;
        }

        let mut ans = i32::MAX;

        for i in 1..=n {
            for j in (i + 1)..=n {
                if !adj[i][j] {
                    continue;
                }
                for k in (j + 1)..=n {
                    if adj[i][k] && adj[j][k] {
                        let deg = degree[i] + degree[j] + degree[k] - 6;
                        if deg < ans {
                            ans = deg;
                        }
                    }
                }
            }
        }

        if ans == i32::MAX { -1 } else { ans }
    }
}
```

## Racket

```racket
#lang racket
(define/contract (min-trio-degree n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([adj (make-vector (+ n 1) #f)]
         [deg (make-vector (+ n 1) 0)])
    ;; initialize adjacency vectors
    (for ([i (in-range (+ n 1))])
      (vector-set! adj i (make-vector (+ n 1) #f)))
    ;; fill edges and degrees
    (for ([e edges])
      (define u (first e))
      (define v (second e))
      (vector-set! (vector-ref adj u) v #t)
      (vector-set! (vector-ref adj v) u #t)
      (vector-set! deg u (+ 1 (vector-ref deg u)))
      (vector-set! deg v (+ 1 (vector-ref deg v))))
    (define min-degree #f)
    ;; search for triangles
    (for ([i (in-range 1 (+ n 1))])
      (for ([j (in-range (+ i 1) (+ n 1))])
        (when (vector-ref (vector-ref adj i) j)
          (for ([k (in-range (+ j 1) (+ n 1))])
            (when (and (vector-ref (vector-ref adj i) k)
                       (vector-ref (vector-ref adj j) k))
              (define d (- (+ (vector-ref deg i)
                              (vector-ref deg j)
                              (vector-ref deg k))
                           6))
              (when (or (not min-degree) (< d min-degree))
                (set! min-degree d)))))))
    (if min-degree
        min-degree
        -1)))
```

## Erlang

```erlang
-module(solution).
-export([min_trio_degree/2]).

-spec min_trio_degree(N :: integer(), Edges :: [[integer()]]) -> integer().
min_trio_degree(N, Edges) ->
    {Adj, Deg} = build_maps(Edges),
    Inf = N * 3 + 1,
    Min = loop_nodes(lists:seq(1, N), Adj, Deg, Inf),
    case Min of
        X when X == Inf -> -1;
        _ -> Min
    end.

build_maps(Edges) ->
    build_maps(Edges, #{}, #{}).

build_maps([], Adj, Deg) ->
    {Adj, Deg};
build_maps([[U, V] | Rest], Adj0, Deg0) ->
    Adj1 = add_adj(Adj0, U, V),
    Adj2 = add_adj(Adj1, V, U),
    Deg1 = inc_deg(Deg0, U),
    Deg2 = inc_deg(Deg1, V),
    build_maps(Rest, Adj2, Deg2).

add_adj(Adj, From, To) ->
    Set = maps:get(From, Adj, #{}),
    NewSet = maps:put(To, true, Set),
    maps:put(From, NewSet, Adj).

inc_deg(Deg, Node) ->
    case maps:is_key(Node, Deg) of
        true -> maps:update(Node, fun(C) -> C + 1 end, Deg);
        false -> maps:put(Node, 1, Deg)
    end.

loop_nodes([], _Adj, _Deg, Min) ->
    Min;
loop_nodes([U | Rest], Adj, Deg, Min) ->
    NeighU = maps:get(U, Adj, #{}),
    Vs = [V || {V, _} <- maps:to_list(NeighU), V > U],
    NewMin = loop_vs(Vs, U, Adj, Deg, Min),
    loop_nodes(Rest, Adj, Deg, NewMin).

loop_vs([], _U, _Adj, _Deg, Min) ->
    Min;
loop_vs([V | RestVs], U, Adj, Deg, Min) ->
    NeighU = maps:get(U, Adj, #{}),
    NeighV = maps:get(V, Adj, #{}),
    Ws = [W || {W, _} <- maps:to_list(NeighU), W > V, maps:is_key(W, NeighV)],
    Min1 = lists:foldl(
        fun(W, Acc) ->
            DegU = maps:get(U, Deg, 0),
            DegV = maps:get(V, Deg, 0),
            DegW = maps:get(W, Deg, 0),
            TrioDeg = DegU + DegV + DegW - 6,
            if TrioDeg < Acc -> TrioDeg; true -> Acc end
        end,
        Min,
        Ws),
    loop_vs(RestVs, U, Adj, Deg, Min1).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_trio_degree(n :: integer, edges :: [[integer]]) :: integer
  def min_trio_degree(n, edges) do
    # Build adjacency sets and degree map
    {adjacency, degree} =
      Enum.reduce(edges, {%{}, %{}}, fn [u, v], {adj, deg} ->
        adj = Map.update!(adj, u, &MapSet.put(&1, v))
        adj = Map.update!(adj, v, &MapSet.put(&1, u))

        deg = Map.update(deg, u, 1, &(&1 + 1))
        deg = Map.update(deg, v, 1, &(&1 + 1))

        {adj, deg}
      end)

    # Ensure every node has an entry in adjacency (even isolated nodes)
    adjacency =
      Enum.reduce(1..n, adjacency, fn i, acc ->
        Map.put_new(acc, i, MapSet.new())
      end)

    min_degree =
      Enum.reduce(edges, :infinity, fn [u0, v0], current_min ->
        du = Map.get(degree, u0, 0)
        dv = Map.get(degree, v0, 0)

        # iterate over neighbors of the node with smaller degree (or smaller id on tie)
        {u, v, du, dv} =
          if du > dv or (du == dv and u0 > v0) do
            {v0, u0, dv, du}
          else
            {u0, v0, du, dv}
          end

        neighbors_u = Map.get(adjacency, u)

        Enum.reduce(neighbors_u, current_min, fn w, inner_min ->
          if w != v and MapSet.member?(Map.get(adjacency, v), w) do
            dw = Map.get(degree, w, 0)
            trio_deg = du + dv + dw - 6
            min(inner_min, trio_deg)
          else
            inner_min
          end
        end)
      end)

    if min_degree == :infinity, do: -1, else: min_degree
  end
end
```

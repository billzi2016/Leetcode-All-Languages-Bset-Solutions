# 2368. Reachable Nodes With Restrictions

## Cpp

```cpp
class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted) {
        vector<vector<int>> adj(n);
        for (const auto& e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<char> isRestricted(n, 0), visited(n, 0);
        for (int node : restricted) isRestricted[node] = 1;
        
        queue<int> q;
        if (!isRestricted[0]) {
            q.push(0);
            visited[0] = 1;
        }
        int count = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            ++count;
            for (int v : adj[u]) {
                if (!visited[v] && !isRestricted[v]) {
                    visited[v] = 1;
                    q.push(v);
                }
            }
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int reachableNodes(int n, int[][] edges, int[] restricted) {
        // Build adjacency list
        @SuppressWarnings("unchecked")
        java.util.List<Integer>[] graph = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new java.util.ArrayList<>();
        }
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            graph[u].add(v);
            graph[v].add(u);
        }

        // Mark restricted nodes
        boolean[] isRestricted = new boolean[n];
        for (int r : restricted) {
            isRestricted[r] = true;
        }

        // BFS from node 0 avoiding restricted nodes
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();
        boolean[] visited = new boolean[n];
        if (!isRestricted[0]) {
            queue.add(0);
            visited[0] = true;
        }
        int count = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            count++;
            for (int nei : graph[node]) {
                if (!visited[nei] && !isRestricted[nei]) {
                    visited[nei] = true;
                    queue.add(nei);
                }
            }
        }

        return count;
    }
}
```

## Python

```python
class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        restricted_set = set(restricted)
        visited = set([0])
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in adj[node]:
                if nei not in restricted_set and nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        return len(visited)
```

## Python3

```python
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        restricted_set = set(restricted)
        visited = [False] * n
        from collections import deque
        q = deque([0])
        visited[0] = True
        count = 0

        while q:
            node = q.popleft()
            count += 1
            for nb in adj[node]:
                if not visited[nb] and nb not in restricted_set:
                    visited[nb] = True
                    q.append(nb)

        return count
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int reachableNodes(int n, int** edges, int edgesSize, int* edgesColSize, int* restricted, int restrictedSize) {
    int *degree = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        degree[a]++;
        degree[b]++;
    }

    int **adj = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int *)malloc(degree[i] * sizeof(int));
    }

    int *idx = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][ idx[a]++ ] = b;
        adj[b][ idx[b]++ ] = a;
    }
    free(idx);

    bool *isRestricted = (bool *)calloc(n, sizeof(bool));
    for (int i = 0; i < restrictedSize; ++i) {
        isRestricted[restricted[i]] = true;
    }

    bool *visited = (bool *)calloc(n, sizeof(bool));
    int *queue = (int *)malloc(n * sizeof(int));
    int head = 0, tail = 0;

    visited[0] = true;
    queue[tail++] = 0;
    int count = 1;

    while (head < tail) {
        int u = queue[head++];
        for (int j = 0; j < degree[u]; ++j) {
            int v = adj[u][j];
            if (!isRestricted[v] && !visited[v]) {
                visited[v] = true;
                queue[tail++] = v;
                ++count;
            }
        }
    }

    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(degree);
    free(isRestricted);
    free(visited);
    free(queue);

    return count;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int ReachableNodes(int n, int[][] edges, int[] restricted) {
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            adj[a].Add(b);
            adj[b].Add(a);
        }

        var isRestricted = new bool[n];
        foreach (int r in restricted) isRestricted[r] = true;

        var visited = new bool[n];
        var queue = new Queue<int>();
        if (!isRestricted[0]) {
            queue.Enqueue(0);
            visited[0] = true;
        }

        int count = 0;
        while (queue.Count > 0) {
            int node = queue.Dequeue();
            count++;
            foreach (int nb in adj[node]) {
                if (!visited[nb] && !isRestricted[nb]) {
                    visited[nb] = true;
                    queue.Enqueue(nb);
                }
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} restricted
 * @return {number}
 */
var reachableNodes = function(n, edges, restricted) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    
    const restrictedSet = new Set(restricted);
    const visited = new Uint8Array(n); // 0/1 flags
    let count = 0;
    const queue = [];
    if (!restrictedSet.has(0)) {
        queue.push(0);
        visited[0] = 1;
        count = 1;
    }
    
    for (let i = 0; i < queue.length; i++) {
        const node = queue[i];
        for (const nb of adj[node]) {
            if (!visited[nb] && !restrictedSet.has(nb)) {
                visited[nb] = 1;
                count++;
                queue.push(nb);
            }
        }
    }
    
    return count;
};
```

## Typescript

```typescript
function reachableNodes(n: number, edges: number[][], restricted: number[]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const restrictedSet = new Set<number>(restricted);
    const visited = new Uint8Array(n);
    let count = 0;
    const stack: number[] = [];
    if (!restrictedSet.has(0)) {
        stack.push(0);
        visited[0] = 1;
    }
    while (stack.length) {
        const node = stack.pop()!;
        count++;
        for (const nb of adj[node]) {
            if (!visited[nb] && !restrictedSet.has(nb)) {
                visited[nb] = 1;
                stack.push(nb);
            }
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $restricted
     * @return Integer
     */
    function reachableNodes($n, $edges, $restricted) {
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // Mark restricted nodes
        $restrictedSet = [];
        foreach ($restricted as $r) {
            $restrictedSet[$r] = true;
        }

        // BFS from node 0 avoiding restricted nodes
        $visited = array_fill(0, $n, false);
        $queue = new SplQueue();
        $queue->enqueue(0);
        $visited[0] = true;
        $count = 0;

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            $count++;
            foreach ($adj[$node] as $nei) {
                if (isset($restrictedSet[$nei]) || $visited[$nei]) {
                    continue;
                }
                $visited[$nei] = true;
                $queue->enqueue($nei);
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func reachableNodes(_ n: Int, _ edges: [[Int]], _ restricted: [Int]) -> Int {
        var graph = [[Int]](repeating: [], count: n)
        for edge in edges {
            let a = edge[0]
            let b = edge[1]
            graph[a].append(b)
            graph[b].append(a)
        }
        
        let restrictedSet = Set(restricted)
        var visited = [Bool](repeating: false, count: n)
        var stack = [Int]()
        if !restrictedSet.contains(0) {
            stack.append(0)
            visited[0] = true
        }
        
        var count = 0
        while let node = stack.popLast() {
            count += 1
            for neighbor in graph[node] {
                if !visited[neighbor] && !restrictedSet.contains(neighbor) {
                    visited[neighbor] = true
                    stack.append(neighbor)
                }
            }
        }
        
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reachableNodes(n: Int, edges: Array<IntArray>, restricted: IntArray): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }
        val isRestricted = BooleanArray(n)
        for (r in restricted) {
            isRestricted[r] = true
        }
        val visited = BooleanArray(n)
        var count = 0
        val queue: ArrayDeque<Int> = ArrayDeque()
        if (!isRestricted[0]) {
            queue.add(0)
            visited[0] = true
        }
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            count++
            for (next in adj[cur]) {
                if (!visited[next] && !isRestricted[next]) {
                    visited[next] = true
                    queue.add(next)
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int reachableNodes(int n, List<List<int>> edges, List<int> restricted) {
    // Build adjacency list
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      adj[a].add(b);
      adj[b].add(a);
    }

    // Set of restricted nodes for O(1) lookup
    final Set<int> restrictedSet = restricted.toSet();

    // Visited array
    List<bool> visited = List.filled(n, false);
    int count = 0;

    // Stack for DFS (iterative)
    List<int> stack = [];

    if (!restrictedSet.contains(0)) {
      stack.add(0);
      visited[0] = true;
      count = 1;
    }

    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      for (int neighbor in adj[node]) {
        if (!visited[neighbor] && !restrictedSet.contains(neighbor)) {
          visited[neighbor] = true;
          count++;
          stack.add(neighbor);
        }
      }
    }

    return count;
  }
}
```

## Golang

```go
func reachableNodes(n int, edges [][]int, restricted []int) int {
    adj := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }

    isRestricted := make([]bool, n)
    for _, r := range restricted {
        isRestricted[r] = true
    }

    visited := make([]bool, n)
    queue := []int{0}
    visited[0] = true
    count := 0

    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        count++
        for _, nb := range adj[node] {
            if !visited[nb] && !isRestricted[nb] {
                visited[nb] = true
                queue = append(queue, nb)
            }
        }
    }

    return count
}
```

## Ruby

```ruby
def reachable_nodes(n, edges, restricted)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  restricted_flag = Array.new(n, false)
  restricted.each { |x| restricted_flag[x] = true }

  visited = Array.new(n, false)
  stack = [0]
  visited[0] = true
  count = 0

  until stack.empty?
    node = stack.pop
    count += 1
    adj[node].each do |nbr|
      next if visited[nbr] || restricted_flag[nbr]
      visited[nbr] = true
      stack << nbr
    end
  end

  count
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, ListBuffer}

object Solution {
  def reachableNodes(n: Int, edges: Array[Array[Int]], restricted: Array[Int]): Int = {
    val adj = Array.fill[ListBuffer[Int]](n)(ListBuffer.empty[Int])
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a).append(b)
      adj(b).append(a)
    }

    val isRestricted = new Array[Boolean](n)
    for (r <- restricted) isRestricted(r) = true

    val visited = new Array[Boolean](n)
    val queue = new java.util.ArrayDeque[Int]()

    if (!isRestricted(0)) {
      visited(0) = true
      queue.add(0)
    }

    var count = 0
    while (!queue.isEmpty) {
      val cur = queue.poll()
      count += 1
      for (nbr <- adj(cur)) {
        if (!visited(nbr) && !isRestricted(nbr)) {
          visited(nbr) = true
          queue.add(nbr)
        }
      }
    }

    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn reachable_nodes(n: i32, edges: Vec<Vec<i32>>, restricted: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut adj = vec![Vec::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }
        let mut is_restricted = vec![false; n];
        for &r in restricted.iter() {
            is_restricted[r as usize] = true;
        }

        let mut visited = vec![false; n];
        let mut stack = Vec::new();
        if !is_restricted[0] {
            stack.push(0usize);
            visited[0] = true;
        }
        let mut count: i32 = 0;
        while let Some(node) = stack.pop() {
            count += 1;
            for &nbr in adj[node].iter() {
                if !visited[nbr] && !is_restricted[nbr] {
                    visited[nbr] = true;
                    stack.push(nbr);
                }
            }
        }
        count
    }
}
```

## Racket

```racket
#lang racket

(require racket/match
         racket/list)

(define/contract (reachable-nodes n edges restricted)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ([adj (make-vector n '())]
         [_ (for-each
               (lambda (e)
                 (match e
                   [(list a b)
                    (vector-set! adj a (cons b (vector-ref adj a)))
                    (vector-set! adj b (cons a (vector-ref adj b)))]))
               edges)]
         [restricted-set (let ([h (make-hash)])
                           (for-each (lambda (r) (hash-set! h r #t)) restricted)
                           h)]
         [visited (make-vector n #f)]
         [stack (list 0)])
    (vector-set! visited 0 #t)
    (let loop ((stk stack) (cnt 0))
      (if (null? stk)
          cnt
          (let* ([node (car stk)]
                 [rest (cdr stk)]
                 [neighbors (vector-ref adj node)]
                 [new-stack
                  (foldl (lambda (nbr acc)
                           (if (or (hash-has-key? restricted-set nbr)
                                   (vector-ref visited nbr))
                               acc
                               (begin
                                 (vector-set! visited nbr #t)
                                 (cons nbr acc))))
                         rest
                         neighbors)])
            (loop new-stack (+ cnt 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([reachable_nodes/3]).

-spec reachable_nodes(N :: integer(), Edges :: [[integer()]], Restricted :: [integer()]) -> integer().
reachable_nodes(_N, Edges, Restricted) ->
    RestrSet = maps:from_list([{R, true} || R <- Restricted]),
    Adj = lists:foldl(
        fun([A, B], Acc) ->
            Acc1 = maps:update_with(A, fun(L) -> [B | L] end, [B], Acc),
            maps:update_with(B, fun(L) -> [A | L] end, [A], Acc1)
        end,
        #{},
        Edges
    ),
    Visited0 = #{0 => true},
    bfs([0], Visited0, Adj, RestrSet).

bfs([], Visited, _Adj, _Restr) ->
    maps:size(Visited);
bfs([Curr | Stack], Visited, Adj, Restr) ->
    Neigh = maps:get(Curr, Adj, []),
    {NewVis, NewStack} = lists:foldl(
        fun(Nbr, {V, S}) ->
            case (maps:is_key(Nbr, V) orelse maps:is_key(Nbr, Restr)) of
                true -> {V, S};
                false -> {maps:put(Nbr, true, V), [Nbr | S]}
            end
        end,
        {Visited, Stack},
        Neigh
    ),
    bfs(NewStack, NewVis, Adj, Restr).
```

## Elixir

```elixir
defmodule Solution do
  @spec reachable_nodes(n :: integer, edges :: [[integer]], restricted :: [integer]) :: integer
  def reachable_nodes(_n, edges, restricted) do
    restricted_set = MapSet.new(restricted)

    adj =
      Enum.reduce(edges, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], fn list -> [b | list] end)
        |> Map.update(b, [a], fn list -> [a | list] end)
      end)

    visited = dfs([0], adj, restricted_set, MapSet.new())
    MapSet.size(visited)
  end

  defp dfs([], _adj, _restricted_set, visited), do: visited

  defp dfs([node | rest], adj, restricted_set, visited) do
    if MapSet.member?(visited, node) do
      dfs(rest, adj, restricted_set, visited)
    else
      visited = MapSet.put(visited, node)

      neighbors = Map.get(adj, node, [])

      new_stack =
        Enum.reduce(neighbors, rest, fn nb, acc ->
          cond do
            MapSet.member?(restricted_set, nb) -> acc
            MapSet.member?(visited, nb) -> acc
            true -> [nb | acc]
          end
        end)

      dfs(new_stack, adj, restricted_set, visited)
    end
  end
end
```

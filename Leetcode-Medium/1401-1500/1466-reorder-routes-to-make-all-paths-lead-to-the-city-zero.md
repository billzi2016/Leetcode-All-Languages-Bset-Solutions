# 1466. Reorder Routes to Make All Paths Lead to the City Zero

## Cpp

```cpp
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        vector<vector<pair<int,int>>> adj(n);
        for (const auto& e : connections) {
            int a = e[0], b = e[1];
            adj[a].push_back({b, 1}); // original direction
            adj[b].push_back({a, 0}); // reverse edge (artificial)
        }
        vector<char> visited(n, false);
        queue<int> q;
        q.push(0);
        visited[0] = true;
        int ans = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto [v, need] : adj[u]) {
                if (!visited[v]) {
                    ans += need;
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
    public int minReorder(int n, int[][] connections) {
        @SuppressWarnings("unchecked")
        java.util.List<int[]>[] adj = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new java.util.ArrayList<>();
        }
        for (int[] conn : connections) {
            int a = conn[0], b = conn[1];
            // original direction a -> b, needs reversal if traversed from a to b
            adj[a].add(new int[]{b, 1});
            // artificial reverse edge b -> a, does not need reversal
            adj[b].add(new int[]{a, 0});
        }
        boolean[] visited = new boolean[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        stack.push(0);
        visited[0] = true;
        int count = 0;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            for (int[] edge : adj[node]) {
                int nei = edge[0];
                int sign = edge[1];
                if (!visited[nei]) {
                    count += sign;
                    visited[nei] = true;
                    stack.push(nei);
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
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for a, b in connections:
            # original direction a -> b needs reversal if traversed from a to b
            adj[a].append((b, 1))
            # artificial reverse edge does not need reversal
            adj[b].append((a, 0))

        visited = [False] * n
        stack = [(0, -1)]
        visited[0] = True
        ans = 0

        while stack:
            node, _ = stack.pop()
            for nei, sign in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    ans += sign
                    stack.append((nei, node))

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append((b, 1))   # original direction needs reversal if traversed from a to b
            adj[b].append((a, 0))   # artificial edge, no reversal needed

        ans = 0
        import sys
        sys.setrecursionlimit(10 ** 6)

        def dfs(node: int, parent: int) -> None:
            nonlocal ans
            for nei, sign in adj[node]:
                if nei == parent:
                    continue
                ans += sign
                dfs(nei, node)

        dfs(0, -1)
        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int minReorder(int n, int** connections, int connectionsSize, int* connectionsColSize) {
    struct Edge {
        int to;
        int sign;   // 1 if original direction (needs reversal when traversed from parent), 0 otherwise
        int next;
    };
    
    int maxEdges = connectionsSize * 2;
    struct Edge *edges = (struct Edge *)malloc(maxEdges * sizeof(struct Edge));
    int *head = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    
    int edgeCnt = 0;
    for (int i = 0; i < connectionsSize; ++i) {
        int a = connections[i][0];
        int b = connections[i][1];
        // original direction a -> b
        edges[edgeCnt].to = b;
        edges[edgeCnt].sign = 1;
        edges[edgeCnt].next = head[a];
        head[a] = edgeCnt++;
        // artificial reverse direction b -> a
        edges[edgeCnt].to = a;
        edges[edgeCnt].sign = 0;
        edges[edgeCnt].next = head[b];
        head[b] = edgeCnt++;
    }
    
    bool *visited = (bool *)calloc(n, sizeof(bool));
    int *queue = (int *)malloc(n * sizeof(int));
    int front = 0, back = 0;
    queue[back++] = 0;
    visited[0] = true;
    
    int count = 0;
    while (front < back) {
        int node = queue[front++];
        for (int e = head[node]; e != -1; e = edges[e].next) {
            int nb = edges[e].to;
            if (!visited[nb]) {
                visited[nb] = true;
                count += edges[e].sign;
                queue[back++] = nb;
            }
        }
    }
    
    free(edges);
    free(head);
    free(visited);
    free(queue);
    
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinReorder(int n, int[][] connections)
    {
        var adj = new List<(int to, int sign)>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<(int, int)>();

        foreach (var conn in connections)
        {
            int a = conn[0], b = conn[1];
            // original direction a -> b needs reversal if traversed from a to b
            adj[a].Add((b, 1));
            // artificial reverse edge b -> a does not need reversal
            adj[b].Add((a, 0));
        }

        var visited = new bool[n];
        var queue = new Queue<int>();
        visited[0] = true;
        queue.Enqueue(0);
        int changes = 0;

        while (queue.Count > 0)
        {
            int cur = queue.Dequeue();
            foreach (var (next, sign) in adj[cur])
            {
                if (!visited[next])
                {
                    changes += sign;
                    visited[next] = true;
                    queue.Enqueue(next);
                }
            }
        }

        return changes;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function(n, connections) {
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b] of connections) {
        // original direction a -> b (needs reversal if traversed from a)
        adj[a].push([b, 1]);
        // artificial reverse edge b -> a (does not need reversal)
        adj[b].push([a, 0]);
    }
    let count = 0;
    const visited = new Array(n).fill(false);
    const stack = [0];
    while (stack.length) {
        const node = stack.pop();
        if (visited[node]) continue;
        visited[node] = true;
        for (const [nei, sign] of adj[node]) {
            if (!visited[nei]) {
                count += sign; // add 1 only for original edges traversed outward
                stack.push(nei);
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function minReorder(n: number, connections: number[][]): number {
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [a, b] of connections) {
        // original directed edge a -> b
        adj[a].push([b, 1]); // needs reversal if traversed from a to b
        adj[b].push([a, 0]); // artificial reverse edge
    }
    const visited = new Array<boolean>(n).fill(false);
    let count = 0;
    const stack: [number, number][] = [[0, -1]];
    while (stack.length) {
        const [node] = stack.pop()!;
        if (visited[node]) continue;
        visited[node] = true;
        for (const [nei, sign] of adj[node]) {
            if (!visited[nei]) {
                count += sign;
                stack.push([nei, node]);
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
     * @param Integer[][] $connections
     * @return Integer
     */
    function minReorder($n, $connections) {
        // Build adjacency list with direction flag:
        // 1 -> original edge (needs reversal if traversed from parent to child)
        // 0 -> artificial reverse edge (does not need reversal)
        $adj = array_fill(0, $n, []);
        foreach ($connections as $c) {
            $a = $c[0];
            $b = $c[1];
            $adj[$a][] = [$b, 1]; // original direction a -> b
            $adj[$b][] = [$a, 0]; // artificial reverse edge
        }

        $visited = array_fill(0, $n, false);
        $queue = new SplQueue();
        $queue->enqueue(0);
        $visited[0] = true;
        $ans = 0;

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            foreach ($adj[$node] as $edge) {
                [$nei, $sign] = $edge;
                if (!$visited[$nei]) {
                    $ans += $sign;   // count if this edge is originally directed away from 0
                    $visited[$nei] = true;
                    $queue->enqueue($nei);
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
    func minReorder(_ n: Int, _ connections: [[Int]]) -> Int {
        var adj = Array(repeating: [(Int, Int)](), count: n)
        for conn in connections {
            let a = conn[0]
            let b = conn[1]
            adj[a].append((b, 1)) // original direction
            adj[b].append((a, 0)) // reverse (artificial) edge
        }
        
        var visited = Array(repeating: false, count: n)
        var queue = [Int]()
        var head = 0
        queue.append(0)
        visited[0] = true
        var answer = 0
        
        while head < queue.count {
            let node = queue[head]
            head += 1
            for (neighbor, sign) in adj[node] {
                if !visited[neighbor] {
                    visited[neighbor] = true
                    answer += sign
                    queue.append(neighbor)
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
    fun minReorder(n: Int, connections: Array<IntArray>): Int {
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (c in connections) {
            val a = c[0]
            val b = c[1]
            adj[a].add(Pair(b, 1)) // original direction
            adj[b].add(Pair(a, 0)) // artificial reverse edge
        }
        val visited = BooleanArray(n)
        val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        visited[0] = true
        queue.add(0)
        var answer = 0
        while (queue.isNotEmpty()) {
            val node = queue.poll()
            for ((neighbor, sign) in adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true
                    answer += sign
                    queue.add(neighbor)
                }
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minReorder(int n, List<List<int>> connections) {
    // Build adjacency list with direction flag:
    // sign = 1 if the original edge goes from current node to neighbor,
    // sign = 0 otherwise.
    var adj = List<List<List<int>>>.generate(n, (_) => []);
    for (var conn in connections) {
      int a = conn[0];
      int b = conn[1];
      adj[a].add([b, 1]); // original direction a -> b
      adj[b].add([a, 0]); // artificial reverse edge
    }

    var visited = List<bool>.filled(n, false);
    int count = 0;
    var stack = <int>[];
    stack.add(0);
    visited[0] = true;

    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      for (var edge in adj[node]) {
        int nei = edge[0];
        int sign = edge[1];
        if (!visited[nei]) {
          visited[nei] = true;
          count += sign; // need to reverse if original direction is from node -> nei
          stack.add(nei);
        }
      }
    }

    return count;
  }
}
```

## Golang

```go
type edge struct {
	to   int
	sign int // 1 if original direction from current node to neighbor, 0 otherwise
}

func minReorder(n int, connections [][]int) int {
	adj := make([][]edge, n)
	for _, c := range connections {
		a, b := c[0], c[1]
		adj[a] = append(adj[a], edge{to: b, sign: 1}) // original direction a -> b
		adj[b] = append(adj[b], edge{to: a, sign: 0}) // artificial reverse edge
	}

	visited := make([]bool, n)
	queue := []int{0}
	visited[0] = true
	ans := 0

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]

		for _, e := range adj[v] {
			if !visited[e.to] {
				ans += e.sign
				visited[e.to] = true
				queue = append(queue, e.to)
			}
		}
	}

	return ans
}
```

## Ruby

```ruby
def min_reorder(n, connections)
  adj = Array.new(n) { [] }
  connections.each do |a, b|
    adj[a] << [b, 1]   # original direction a -> b
    adj[b] << [a, 0]   # artificial reverse edge
  end

  count = 0
  stack = [[0, -1]]
  until stack.empty?
    node, parent = stack.pop
    adj[node].each do |neighbor, sign|
      next if neighbor == parent
      count += sign
      stack << [neighbor, node]
    end
  end

  count
end
```

## Scala

```scala
object Solution {
  def minReorder(n: Int, connections: Array[Array[Int]]): Int = {
    val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (c <- connections) {
      val a = c(0)
      val b = c(1)
      adj(a).append((b, 1)) // original direction
      adj(b).append((a, 0)) // artificial reverse edge
    }
    val visited = new Array[Boolean](n)
    val queue = new java.util.ArrayDeque[Int]()
    queue.add(0)
    visited(0) = true
    var count = 0
    while (!queue.isEmpty) {
      val cur = queue.poll()
      for ((nbr, sign) <- adj(cur)) {
        if (!visited(nbr)) {
          visited(nbr) = true
          count += sign
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
    pub fn min_reorder(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n_usize];
        for conn in connections.iter() {
            let a = conn[0] as usize;
            let b = conn[1] as usize;
            // original direction a -> b (needs reversal if traversed from a to b)
            adj[a].push((b, 1));
            // artificial reverse edge
            adj[b].push((a, 0));
        }

        use std::collections::VecDeque;
        let mut visited = vec![false; n_usize];
        let mut queue = VecDeque::new();
        visited[0] = true;
        queue.push_back(0usize);
        let mut count: i32 = 0;

        while let Some(node) = queue.pop_front() {
            for &(neighbor, sign) in &adj[node] {
                if !visited[neighbor] {
                    visited[neighbor] = true;
                    count += sign;
                    queue.push_back(neighbor);
                }
            }
        }

        count
    }
}
```

## Racket

```racket
(define/contract (min-reorder n connections)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((adj (make-vector n '()))
         (add-edge
          (lambda (from to sign)
            (vector-set! adj from (cons (cons to sign) (vector-ref adj from))))))
    ;; build adjacency with direction flag: 1 = original direction, 0 = reverse (artificial)
    (for ([e connections])
      (define a (list-ref e 0))
      (define b (list-ref e 1))
      (add-edge a b 1)   ; a -> b (original)
      (add-edge b a 0))  ; b -> a (artificial)
    (let ((visited (make-vector n #f))
          (queue   (make-vector n 0))
          (count   0))
      (vector-set! visited 0 #t)
      (vector-set! queue 0 0)
      (let loop ((head 0) (tail 1))
        (when (< head tail)
          (define node (vector-ref queue head))
          (for ([pair (vector-ref adj node)])
            (define neighbor (car pair))
            (define sign     (cdr pair))
            (unless (vector-ref visited neighbor)
              (vector-set! visited neighbor #t)
              (when (= sign 1) (set! count (+ count 1)))
              (vector-set! queue tail neighbor)
              (set! tail (+ tail 1))))
          (loop (+ head 1) tail))
      count)))
```

## Erlang

```erlang
-module(solution).
-export([min_reorder/2]).

-spec min_reorder(N :: integer(), Connections :: [[integer()]]) -> integer().
min_reorder(N, Connections) ->
    Adj0 = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    Adj = build_adj(Connections, Adj0),
    dfs(0, -1, Adj).

build_adj([], Adj) -> Adj;
build_adj([[A, B] | Rest], Adj) ->
    Adj1 = maps:update_with(
        A,
        fun(L) -> [{B, 1} | L] end,
        [{B, 1}],
        Adj),
    Adj2 = maps:update_with(
        B,
        fun(L) -> [{A, 0} | L] end,
        [{A, 0}],
        Adj1),
    build_adj(Rest, Adj2).

dfs(Node, Parent, Adj) ->
    AdjNode = maps:get(Node, Adj),
    lists:foldl(
        fun({Nei, Sign}, Acc) ->
            if
                Nei == Parent -> Acc;
                true -> Acc + Sign + dfs(Nei, Node, Adj)
            end
        end,
        0,
        AdjNode).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_reorder(n :: integer, connections :: [[integer]]) :: integer
  def min_reorder(_n, connections) do
    adj = build_adj(connections, %{})
    bfs(:queue.in(0, :queue.new()), MapSet.new([0]), 0, adj)
  end

  defp build_adj([], acc), do: acc

  defp build_adj([[a, b] | rest], acc) do
    acc1 = Map.update(acc, a, [{b, 1}], fn lst -> [{b, 1} | lst] end)
    acc2 = Map.update(acc1, b, [{a, 0}], fn lst -> [{a, 0} | lst] end)
    build_adj(rest, acc2)
  end

  defp bfs(queue, visited, count, adj) do
    case :queue.out(queue) do
      {:empty, _} ->
        count

      {{:value, node}, q} ->
        {new_count, new_queue, new_visited} =
          Enum.reduce(Map.get(adj, node, []), {count, q, visited}, fn {nbr, sign},
                                                                      {c, qacc, vacc} ->
            if MapSet.member?(vacc, nbr) do
              {c, qacc, vacc}
            else
              {c + sign, :queue.in(nbr, qacc), MapSet.put(vacc, nbr)}
            end
          end)

        bfs(new_queue, new_visited, new_count, adj)
    end
  end
end
```
